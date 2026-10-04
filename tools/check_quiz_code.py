#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""验收题库里嵌的代码与输出：**题面声称的输出必须真是那份代码跑出来的**。

用法：
    python3 -X utf8 -B tools/check_quiz_code.py <科目目录>

题目里的程序片段与输出块，是学生用来对照自己结果的凭据。它们错了，学生就会怀疑自己——
这比题目出得浅更伤。这个脚本把题库里每一段围栏代码拿出来，按三种情形验收：

| 情形 | 判据（怎么识别） | 验收 |
|---|---|---|
| **完整程序** | 围栏里有 `main(` | 编译通过；若题面给了输出块，**运行结果必须与它逐行一致** |
| **片段** | 没 `main(`、没有语法错误特征 | 补一层 `main` 包起来能编译过（用来证明它不是错的代码） |
| **故意写坏的反例** | 含 `error:` / `warning:` 字样的输出块，或代码明显缺东西 | **必须编译不过**，否则说明「反例」其实是对的 |

片段包装的写法：把片段放进 `int main() { … return 0; }` 里试编译。它不保证能跑（很多片段
本来就依赖上下文，例如已经声明好的变量），所以**片段只判「像不像合法 C++」，不判运行结果**。

退出码：0 全过；1 有对不上的地方（逐条打印 `<题库文件> <锚点> <问题>`）。
"""

import json
import os
import re
import subprocess
import sys
import tempfile

STD = '-std=c++17'
TIMEOUT = 8
FENCE_RE = re.compile(r'^```(\w*)\s*$')
CPP_LANGS = ('cpp', 'c', 'cc', 'cxx', 'c++')
OUT_LANGS = ('text', 'term', 'sh', 'bash')
# 两类「反例」判据不同：给了 error 输出的必须编译不过；只给 warning 的**编译过也算对**
# （`漏 return` 那种正是编译得过、只有 -Wall 才看得见），此时要核实警告能复现。
ERROR_HINT_RE = re.compile(r'\berror:|编译错误')
WARN_HINT_RE = re.compile(r'\bwarning:|警告')
BROKEN_HINT_RE = re.compile(r'\berror:|\bwarning:|编译错误|报错|警告')


def _first(text, n=1):
    """取诊断信息的前 n 行，用来把「哪里不对」说清而不是只说「编不过」。"""
    return ' / '.join((text or '').splitlines()[:n])


def _context_dependent(diag):
    """判断是「依赖上下文的片段」——这类编不过是正常的，不算缺陷。

    课件里的片段大量引用了别处声明好的变量（`sum`、`scores`、`N`），单独拎出来必然报
    `use of undeclared identifier`；`for`/`if` 这类语句片段脱离函数体还会报
    `expected unqualified-id`。这些都说明「它是片段」，不是「它是错代码」。
    """
    joined = (diag or '')
    return any(h in joined for h in
               ('undeclared', 'was not declared', 'expected expression',
                'expected unqualified-id', 'use of undeclared'))


def blocks(text):
    """把一段文本里的围栏拆成 [(语言, 正文)]。"""
    out, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if m:
            lang, body = m.group(1).lower(), []
            i += 1
            while i < len(lines) and not re.match(r'^```\s*$', lines[i]):
                body.append(lines[i]); i += 1
            out.append((lang, '\n'.join(body)))
        i += 1
    return out


# 判「这段是完整程序还是片段」的两种写法（都要认，各有真实例子）：
#   a) 文件作用域上出现 `main` 的定义——完整的程序；
#   b) 文件作用域上定义了别的函数（`^类型 名字(` 在行首、且没有 main）——例如
#      `int total(const int *p, int n) { … }` 这种，是一段可编译的**函数定义片段**。
MAIN_RE = re.compile(r'\bmain\s*\([^;]*\)\s*\{?', re.M)
# 题面里的代码为省篇幅常省略 `#include`。编译时补上标准头，让「能不能编译」只取决于代码本身；
# 这不是放水——每一章都教过这些头文件的用途，学生自己那份是有的。
HEADERS = ('#include <iostream>\n#include <iomanip>\n#include <cstring>\n'
           '#include <cmath>\n#include <cstdlib>\n')


# 返回类型写成「标识符 + 可选的 * / &」，**函数名紧跟 `(`**（中间只许有空白）。
#
# 为什么强调「紧跟」：赋值式 `int n = total(nums, 5);` 里的 `n` 后面是 ` = `，不是 `(`，
# 于是不会被误判成函数定义。反过来，`{` 允许在下一行——真实课件里的片段常常写成
# `int total(int table[5])` 换行再 `{`，早先要求 `{` 同行，把这种函数定义全漏了（真实误报过）。
TOP_FUNC_RE = re.compile(r'^[A-Za-z_]\w*(?:\s*[*&])?\s+\w+\s*\(', re.M)


def looks_complete(src):
    """这段是「能独立成程序的块」还是「依赖上下文的片段」。

    判据：**文件作用域上**有没有函数定义（含 `main`）。不能只看「有没有 `main(` 字样」，
    也不能只看「某行像函数定义」——`main` 体内的一行 `int total(nums, n)` 长得也像函数定义，
    早先因此把好几段片段误判成完整程序（真实误报过）。所以这里数括号深度：只在深度 0 处认。
    """
    depth = 0
    for line in src.splitlines():
        if depth == 0:
            if MAIN_RE.search(line) or TOP_FUNC_RE.search(line):
                return True
            # 一行里可能同时出现函数名与开括号（`int add(int a) {`）
        depth += line.count('{') - line.count('}')
        if depth < 0:
            depth = 0
    return False


def with_headers(src):
    """题面里的代码为省篇幅常省略 `#include` 和 `using`。编译时补上，让「能不能编译」
    只取决于代码本身——这不放水：每一章都教过这些头文件与命名空间的用途，学生自己那份是有的。
    """
    pre = ''
    # **总是**补齐这套标准头：题面为省篇幅往往只写 `#include <iostream>`（甚至一个都不写），
    # 于是 `setprecision`、`strcmp` 之类会被报到「未声明」，而那些都是本章教过的。
    # 早先写成「没有 include 才补」，只写了一个 include 的代码就漏补了，真实误报过。
    pre += HEADERS
    # 用了裸 `cout`/`cin`（没写 std::）就补一行 using，否则必然是 undeclared。
    # 括号要加对：`not A or B` 会被解析成 `(not A) or B`，早先因此漏补过头文件。
    if (not re.search(r'using\s+namespace', src)
            and re.search(r'(?<![\w:])cout\b|(?<![\w:])cin\b', src)):
        pre += 'using namespace std;\n'
    return pre + src


def syntax_only(src, workdir, name='s.cpp'):
    """只做语法与语义检查（`-fsyntax-only`），**不链接**。

    判「这段代码是不是合法 C++」必须用这个，不能用「有没有产出可执行文件」——链接要求有
    `main`，而题库里大量片段（单个函数定义、单条语句）本来就没有 `main`。用链接判，
    这些片段会被一律判成「编不过」，然后我再去试「包一层 main」，而包一层对函数定义片段
    又是语法错误，最后报出来的是一堆假问题（这一条改了三轮，每轮都误报一批，根因都在这里）。
    """
    path = os.path.join(workdir, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(src)
    p = subprocess.run(['g++', STD, '-Wall', '-fsyntax-only', path],
                       capture_output=True, text=True)
    return p.returncode == 0, (p.stderr or p.stdout).strip()


def compile_src(src, workdir, name='t.cpp'):
    """编译源码 → (有没有产出可执行文件, 可执行文件路径, 诊断信息)。

    **「编过」的判据是拿到了可执行文件**，不是「g++ 退出码为 0」。原因：一段只有函数定义、
    没有 `main` 的片段语法完全正确，但链接会报 `Undefined symbols: _main`。把它当「编不过」，
    就会再试包一层 main 的写法，而那种写法对函数定义片段是语法错误——最后把包装的错误
    当成结论报出来（真实误报过一批）。看可执行文件在不在，这两种情形就分得干净。
    """
    path = os.path.join(workdir, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(src)
    exe = os.path.join(workdir, 'a.out')
    if os.path.exists(exe):
        os.remove(exe)
    p = subprocess.run(['g++', STD, '-Wall', path, '-o', exe],
                       capture_output=True, text=True)
    return os.path.exists(exe), exe, (p.stderr or p.stdout).strip()


def run_exe(exe):
    try:
        p = subprocess.run([exe], input='', capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, None
    return p.returncode, (p.stdout or '').rstrip('\n')


def normalize(text):
    """比较输出时只看有效内容行：去掉首尾空行与行尾空格。"""
    return [ln.rstrip() for ln in text.strip().splitlines() if ln.strip()]


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    lessons = os.path.join(subject, 'lessons')
    if not os.path.isdir(lessons):
        print(f'没有 {lessons}')
        return 1
    pools = sorted(n for n in os.listdir(lessons) if n.endswith('.quiz.json'))
    if not pools:
        print('还没有题库文件，跳过')
        return 0

    problems, checked = [], 0
    for name in pools:
        data = json.load(open(os.path.join(lessons, name), encoding='utf-8'))
        for anchor, questions in data.items():
            for qi, q in enumerate(questions, 1):
                fields = [q.get('q', '')]
                for key in ('answer', 'criteria', 'why'):
                    if q.get(key):
                        fields.append(q[key])
                # field 0 是题面；answer/criteria/why 是**参考答案与判分要点**——
                # 那些代码是给人看的参考写法，不一定要能独立跑（例如读输入的程序），
                # 所以对它们只做语法验收、不跑、也不与题面输出对账。
                for fi, field in enumerate(fields):
                    is_answer_field = fi > 0
                    bl = blocks(field)
                    cpp = [(l, b) for l, b in bl if l in CPP_LANGS]
                    outs = [b for l, b in bl if l in OUT_LANGS]
                    claim = '\n'.join(outs)
                    is_err_claim = bool(ERROR_HINT_RE.search(claim))
                    is_warn_claim = bool(WARN_HINT_RE.search(claim))
                    looks_broken = bool(BROKEN_HINT_RE.search(claim))
                    for ci, (lang, src) in enumerate(cpp, 1):
                        checked += 1
                        tag = f'{name}｜{anchor[:24]}…｜题{qi}·段{fi}·代码{ci}'
                        with tempfile.TemporaryDirectory() as tmp:
                            # 统一处理：先**按原样**编（补上头文件），编不过就**再包一层 main**试。
                            #
                            # 为什么不分「完整程序/片段」两类走两条路：真实题库里三类都有，
                            # 而边界情况分不干净——
                            #   · 完整程序（有 main）：原样编就能过；
                            #   · 文件作用域的函数定义片段（`int total(int t[5]) { … }`）：
                            #     原样编能过语法，但链接缺 `_main`；包一层 main 正好补上；
                            #   · 语句片段（`double avg = total / 3;`）：原样编语法就错，包一层才对。
                            # 试两条路而不是先分类，既不会漏也不会误判（分类判据改了三轮，
                            # 每一轮都误报过一批——试编译才是唯一可靠的判据）。
                            base = with_headers(src)
                            wrapped = with_headers('int main() {\n' + src + '\nreturn 0;\n}\n')
                            # 「合法 C++」用语法检查判（不链接）；「能跑」用编译判（要 main）。
                            ok_syntax, syn_err = syntax_only(base, tmp)
                            if not ok_syntax:
                                wrapped_syntax, wrapped_syn_err = syntax_only(wrapped, tmp)
                            else:
                                wrapped_syntax, wrapped_syn_err = False, ''
                            usable = ok_syntax or wrapped_syntax
                            diag = syn_err if not ok_syntax else ''
                            # 只有原样就能独立成程序时，才编译 + 运行 + 与题面输出对账
                            ok, exe, err = compile_src(base, tmp)

                            if is_err_claim:
                                if usable:
                                    problems.append((tag, '题面给了「编译错误」输出，'
                                                          '但它其实能编译——反例不对'))
                                continue
                            if is_warn_claim:
                                if not usable:
                                    problems.append((tag, '题面说它「只是警告、能编译」，'
                                                          f'但它编译不过：{_first(diag)}'))
                                elif 'warning' not in (err + syn_err + wrapped_syn_err):
                                    problems.append((tag, '题面说编译器给了那条警告，'
                                                          '但这次编译没复现出来'))
                                continue
                            if not usable:
                                if looks_broken:
                                    continue        # 题面本来就给了报错/崩溃输出
                                if _context_dependent(diag):
                                    continue        # 依赖别处声明的变量，属正常
                                problems.append((tag, '这段代码编不过：' + _first(diag, 2)))
                                continue

                            # 能编过：只在「原样就能独立成程序」时才跑，并把输出与题面对账
                            if not ok:
                                continue
                            if is_answer_field:
                                continue        # 参考答案只验语法，不跑
                            rc, out = run_exe(exe)
                            if rc is None:
                                problems.append((tag, '运行超时（可能在等输入）'))
                            elif rc != 0:
                                if not looks_broken:
                                    problems.append((tag, f'运行退出码 {rc}'))
                            elif claim.strip() and normalize(claim) != normalize(out or ''):
                                problems.append((tag, '运行结果与题面给出的输出对不上：\n'
                                                      f'        题面说：{normalize(claim)[:3]}\n'
                                                      f'        实际是：{normalize(out or "")[:3]}'))

    print(f'题库 {len(pools)} 份，检查了 {checked} 段代码')
    if problems:
        print(f'对不上 {len(problems)} 处：')
        for tag, why in problems:
            print(f'  - {tag}')
            print(f'      {why}')
        return 1
    print('题库代码验收通过：完整程序的输出与题面一致、反例确实编译不过、片段是合法 C++')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
