#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""验收动手任务（lab）：**留白态必须不满足预期、参考解必须满足预期**。

用法：
    python3 -X utf8 -B tools/check_lab.py <科目目录> [<lab 目录名> ...]

不给目录名就扫科目下 `lab/`（跳过 `lab/solutions/`）的每个任务目录。

判据的信源是 **lab 自己的 `预期输出.txt`**，不去猜。它的格式（lab 里逐份一致）：

```text
# 以 # 开头的行是给人看的说明，不参与判定

$ ./程序名 < 输入文件名
这一组的预期输出第一行
第二行
```

于是验收这么走：

| 检查 | 判据 |
|---|---|
| 留白态能编译 | 任务目录的 `.cpp` 必须编译通过——一上手撞编译错误不是「留白」是「残破」 |
| 留白态没留白 | 它在**任何一组输入**下都不该满足预期（满足了就是学生照着跑就过，学不到东西） |
| 参考解能编译 | `lab/solutions/<同名目录>/` 的 `.cpp` 必须编译通过 |
| 参考解满足预期 | 它在**至少一组输入**下要满足那一组的预期 |
| 参考解自包含 | 只 `#include` 标准库头，不引用任务目录之外的自定义文件 |

**「满足预期」不是逐字相等**：`预期输出.txt` 自己写着「你的程序多打几行也算对——下面这些行
必须出现，而且数字要对」。所以判定是**按顺序包含**（允许中间多打别的行），且忽略行尾空白。

退出码：0 全过；1 有不合格项（逐条打印 `<文件> <问题>`）。
"""

import os
import re
import subprocess
import sys
import tempfile

STD = '-std=c++17'
WARN = ['-Wall', '-Wextra', '-Wno-unused-parameter']
TIMEOUT = 8
INCLUDE_RE = re.compile(r'^\s*#\s*include\s*[<"]([^">]+)[">]')
SECTION_RE = re.compile(r'^\$\s+\./(\S+)(?:\s*<\s*(\S+))?\s*$')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def cpp_files(d):
    out = []
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x != 'solutions']
        out += [os.path.join(root, fn) for fn in sorted(files) if fn.endswith('.cpp')]
    return out


def parse_expected(text):
    """把 `预期输出.txt` 解析成 [{'input': 文件名或 None, 'lines': [预期行]}]。"""
    sections, cur = [], None
    for line in (text or '').splitlines():
        m = SECTION_RE.match(line.rstrip())
        if m:
            cur = {'input': m.group(2), 'lines': []}
            sections.append(cur)
            continue
        if line.lstrip().startswith('#'):
            continue                        # 说明行，不参与判定
        if cur is None:
            continue                        # 第一组之前的内容（若有）忽略
        if line.strip():
            cur['lines'].append(line.rstrip())
    return [s for s in sections if s['lines']]


def contains_in_order(actual, expected):
    """expected 的每一行要按顺序出现在 actual 里（允许中间多打别的行）。"""
    a, i = [ln.rstrip() for ln in (actual or '').splitlines()], 0
    for want in expected:
        while i < len(a) and a[i] != want:
            i += 1
        if i >= len(a):
            return False
        i += 1
    return True


def compile_src(src_path, workdir):
    exe = os.path.join(workdir, 'a.out')
    if os.path.exists(exe):
        os.remove(exe)
    p = subprocess.run(['g++', STD] + WARN + [src_path, '-o', exe],
                       capture_output=True, text=True)
    return os.path.exists(exe), exe, (p.stderr or p.stdout).strip()


def run_exe(exe, stdin_text):
    try:
        p = subprocess.run([exe], input=stdin_text, capture_output=True,
                           text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, None
    return p.returncode, (p.stdout or '')


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    lab_root = os.path.join(subject, 'lab')
    if not os.path.isdir(lab_root):
        print(f'没有 {lab_root}（lab 还没产出，跳过）')
        return 0

    names = argv[2:] or sorted(
        d for d in os.listdir(lab_root)
        if os.path.isdir(os.path.join(lab_root, d)) and d != 'solutions'
    )
    if not names:
        print('lab/ 下没有任务目录（还没产出，跳过）')
        return 0

    problems, total = [], 0
    for name in names:
        task = os.path.join(lab_root, name)
        sol = os.path.join(lab_root, 'solutions', name)
        exp_path = os.path.join(task, '预期输出.txt')
        expect_md = read(exp_path) if os.path.isfile(exp_path) else None
        sections = parse_expected(expect_md)
        tasks_cpp, sols_cpp = cpp_files(task), cpp_files(sol)

        print(f'{name}: 留白 {len(tasks_cpp)} · 参考解 {len(sols_cpp)} · '
              f'输入组 {len(sections)} · 预期输出 {"有" if expect_md else "缺"}')

        if not tasks_cpp:
            problems.append((name, '任务目录里没有 .cpp——学生没有可补的起点'))
        if not sols_cpp:
            problems.append((name, 'solutions/ 里没有参考解——学生卡住后无处对照'))
        if not expect_md:
            problems.append((name, '没有 `预期输出.txt`——学生做完了没有可对照的标准'))
            continue
        if not sections:
            problems.append((name, '`预期输出.txt` 里没有可判定的分组'
                                   '（应当有 `$ ./程序 < 输入文件` 这样的行）'))
            continue

        def stdin_of(sec, base):
            """取这一组的输入：按 `$ ./prog < 文件名` 里的文件名去 base 下找。"""
            fn = sec['input']
            if not fn:
                return ''
            p = os.path.join(base, fn)
            return read(p) if os.path.isfile(p) else None

        with tempfile.TemporaryDirectory() as tmp:
            # ① 留白态
            for path in tasks_cpp:
                total += 1
                rel = os.path.relpath(path, subject)
                ok, exe, err = compile_src(path, tmp)
                if not ok:
                    problems.append((rel, '留白态编译不过（学生一上手就撞编译错误）：'
                                          + ' / '.join((err or '').splitlines()[:1])))
                    continue
                for sec in sections:
                    s = stdin_of(sec, task)
                    if s is None:
                        continue
                    rc, out = run_exe(exe, s)
                    if rc == 0 and contains_in_order(out, sec['lines']):
                        problems.append((rel, f'留白态**已经满足**了预期输出'
                                              f'（输入 `{sec["input"] or "无"}`）——'
                                              '任务没有留白，学生照着跑就过了，学不到东西'))
                        break

            # ② 参考解
            for path in sols_cpp:
                total += 1
                rel = os.path.relpath(path, subject)
                ok, exe, err = compile_src(path, tmp)
                if not ok:
                    problems.append((rel, '参考解编译不过：'
                                          + ' / '.join((err or '').splitlines()[:1])))
                    continue
                for inc in INCLUDE_RE.findall(read(path)):
                    if inc.endswith(('.h', '.hpp')):
                        problems.append((rel, f'参考解引用了自定义头文件 `{inc}`——'
                                              '学生拷进任务目录后编不过（参考解要自包含）'))
                hit, tried, miss = False, 0, []
                for sec in sections:
                    s = stdin_of(sec, sol)
                    if s is None:
                        s = stdin_of(sec, task)
                    if s is None:
                        miss.append(f'{sec["input"]}（找不到输入文件）')
                        continue
                    tried += 1
                    rc, out = run_exe(exe, s)
                    if rc == 0 and contains_in_order(out, sec['lines']):
                        hit = True
                        break
                    miss.append(sec['input'] or '无输入')
                if not hit:
                    problems.append((rel, f'参考解在 {tried} 组输入（{"、".join(miss)}）下'
                                          '都没跑出 `预期输出.txt` 的内容——学生对照时会对不上'))

    print('-' * 74)
    print(f'共检查 {total} 个 .cpp')
    if problems:
        print(f'不合格 {len(problems)} 项：')
        for path, why in problems:
            print(f'  - {path}: {why}')
        return 1
    print('lab 验收通过：留白态都没留白、参考解都跑出预期、参考解自包含')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
