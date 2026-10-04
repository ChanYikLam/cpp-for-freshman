#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把课程里的 `std::` 写法统一成 `using namespace std;`。

用法：
    python3 -X utf8 -B tools/unify_std.py <科目目录> [--apply] [--keep-file <文件名>]

不带 `--apply` 只报告（dry-run），不动盘。

改什么（主编者定的口径：**第一课保留 `std::` 的来历讲解，其余代码全部改成 using**）：

1. 所有的 `std::cout` / `std::cin` / `std::endl` / `std::string` … 去掉 `std::` 前缀
   （因此 `std::string` 变成 `string`，这正是本书教法）；
2. **完整程序**（含 `int main`）在最后一个 `#include` 之后补一行 `using namespace std;`
   ——原本可能写在 `main` 里面，统一提到文件作用域（标准写法）；
3. 片段（没有 main 的代码块）只做第 1 步，不再插入 using——它可能本来就在某个函数体内；
4. `--keep-file` 指定的文件跳过第 1 步（第一课要靠它讲 `std::` 是什么）。

为什么必须带 dry-run：这是约 500 处机械替换，落盘前要能逐文件看清单。
改完必须重跑 `tools/check_examples.py`（86 个示例要重新编译）与
`tools/check_quiz_code.py`（题库里嵌的代码要重新编译）。
"""

import json
import os
import re
import sys

INCLUDE_RE = re.compile(r'^#include\s*[<"][^>"]+[>"]\s*$', re.M)
USING_RE = re.compile(r'^\s*using namespace std;\s*$', re.M)
MAIN_RE = re.compile(r'\bint\s+main\s*\(')


def transform_code(src):
    """一段 C++ 代码：去 std:: 前缀 + 需要时补 using。返回 (新代码, 做了哪些事)。"""
    notes = []
    out = src
    if 'std::' in out:
        out = out.replace('std::', '')
        notes.append('去 std:: 前缀')

    has_main = bool(MAIN_RE.search(out))
    if has_main and not USING_RE.search(out):
        incs = list(INCLUDE_RE.finditer(out))
        if incs:
            ins = incs[-1].end()
            out = out[:ins] + '\nusing namespace std;' + out[ins:]
            notes.append('补 using')
        else:
            out = 'using namespace std;\n' + out
            notes.append('补 using（无 include）')
    elif has_main:
        # 已经有 using，但可能写在 main 里 → 提到文件作用域
        m = USING_RE.search(out)
        if m and m.start() > out.find('int main'):
            out = out[:m.start()] + out[m.end():]
            incs = list(INCLUDE_RE.finditer(out))
            if incs:
                ins = incs[-1].end()
                out = out[:ins] + '\nusing namespace std;' + out[ins:]
            else:
                out = 'using namespace std;\n' + out
            notes.append('using 提到文件作用域')
    return out, notes


def transform_text(text):
    """markdown 正文：**只改代码围栏里**的代码，散文里的 `std::` 说明保持原样。

    散文改动很危险——「std::cout 读作 std 柜子里的 cout」这种句子去掉前缀就讲不通了。
    而且代码围栏之外的地方，作者是在讲这件事本身，不是在使用它。
    """
    notes, n = [], 0
    parts = re.split(r'(^```[^\n]*\n.*?^```\s*$)', text, flags=re.M | re.S)
    for i, part in enumerate(parts):
        if not part.startswith('```') or 'std::' not in part:
            continue
        head, _, rest = part.partition('\n')
        body, _, tail = rest.rpartition('\n```')
        new_body, ns = transform_code(body)
        if ns:
            parts[i] = head + '\n' + new_body + '\n```' + tail
            notes += ns
            n += 1
    return ''.join(parts), notes, n


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    apply = '--apply' in argv
    keep = set()
    if '--keep-file' in argv:
        i = argv.index('--keep-file')
        keep = set(argv[i + 1:])
        keep = {k for k in keep if not k.startswith('--')}

    targets = []
    lessons = os.path.join(subject, 'lessons')
    if os.path.isdir(lessons):
        targets += [os.path.join(lessons, n) for n in sorted(os.listdir(lessons))
                    if n.endswith('.md') and n not in keep]
    code = os.path.join(subject, 'code')
    if os.path.isdir(code):
        targets += [os.path.join(code, n) for n in sorted(os.listdir(code))
                    if n.endswith('.cpp')]
    lab = os.path.join(subject, 'lab')
    if os.path.isdir(lab):
        for root, dirs, files in os.walk(lab):
            targets += [os.path.join(root, n) for n in sorted(files)
                        if n.endswith('.cpp') or n == 'README.md']

    total_files = total_std = 0
    quiz_targets = []
    if os.path.isdir(lessons):
        quiz_targets = [os.path.join(lessons, n) for n in sorted(os.listdir(lessons))
                        if n.endswith('.quiz.json')]

    for path in targets:
        rel = os.path.relpath(path, subject)
        if path.endswith('.cpp'):
            src = open(path, encoding='utf-8').read()
            new, notes = transform_code(src)
        else:
            src = open(path, encoding='utf-8').read()
            new, notes, _ = transform_text(src)
        n_std = src.count('std::') - new.count('std::')
        if new != src:
            total_files += 1
            total_std += n_std
            print(f'  {rel}: 去 {n_std} 处 std:: · ' + '、'.join(sorted(set(notes))))
            if apply:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new)

    for path in quiz_targets:
        rel = os.path.relpath(path, subject)
        data = json.load(open(path, encoding='utf-8'))
        changed, n_std = False, 0
        for anchor, qs in data.items():
            for q in qs:
                for key in ('q', 'answer', 'criteria', 'why'):
                    if not q.get(key):
                        continue
                    new, notes, _ = transform_text(q[key])
                    if new != q[key]:
                        n_std += q[key].count('std::') - new.count('std::')
                        q[key] = new
                        changed = True
        if changed:
            total_files += 1
            total_std += n_std
            print(f'  {rel}: 去 {n_std} 处 std::（题面/答案）')
            if apply:
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    f.write('\n')

    print('-' * 74)
    print(f'{"已改" if apply else "将改"} {total_files} 个文件、共 {total_std} 处 std::')
    if keep:
        print(f'（跳过文件：{"、".join(sorted(keep))}）')
    if not apply:
        print('这是 dry-run。加 --apply 才落盘。')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
