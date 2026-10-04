#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把各讲述批次的 examples/ 收拢到课程科目下的 `code/`，让学生真的拿得到代码。

用法：
    python3 -X utf8 -B collect_code.py <科目目录> [--check]

背景：写课件时，示例代码落在各批次的暂存目录里
（`<科目>/.stage/learning-coach-batchN/examples/`）。那是**编辑期的临时位置**，交付前会清掉，
所以它不能出现在课件正文里——读者点开只会 404（真实发生过：五篇指针课的 `::: resources`
里写着 `.stage/learning-coach-batch3/examples/…`）。

本脚本把每个示例**原样拷进 `<科目>/code/`**（连同 `MANIFEST.txt` 合并成一份总表），
课件正文统一引用 `code/<名字>.cpp`。这样：

- 学生拿到的课程包里有一份完整、可编译、带说明的代码目录；
- 正文里的引用是稳定的相对路径，站点构建时整份拷进 `docs/code/`；
- 谁改过哪个示例，看这份 MANIFEST 就清楚（stem → 节点 → 期望 run/compile/fail）。

`--check` 只报告不写盘：列出会收集哪些、有没有重名冲突。
退出码：0 正常；1 有重名冲突（同名不同内容会让读者拿到错的代码，必须人工解决）。
"""

import hashlib
import os
import shutil
import sys


def batches(subject):
    stage = os.path.join(subject, '.stage')
    if not os.path.isdir(stage):
        return []
    out = []
    for name in sorted(os.listdir(stage)):
        if name.startswith('learning-coach-'):
            man = os.path.join(stage, name, 'examples', 'MANIFEST.txt')
            if os.path.isfile(man):
                out.append((name, os.path.join(stage, name, 'examples')))
    return out


def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    check_only = '--check' in argv[2:]
    dst = os.path.join(subject, 'code')

    found = batches(subject)
    if not found:
        print('没找到任何 learning-coach-*/examples/（可能已经收集过，或还没开始写）')
        return 0

    # 先查重名冲突：同名不同内容必须人工处理，静默覆盖等于把读者的代码换成别的
    seen, conflicts = {}, []
    plan = []
    for batch, ex_dir in found:
        for fn in sorted(os.listdir(ex_dir)):
            if not fn.endswith(('.cpp', '.in')) and fn != 'MANIFEST.txt':
                continue
            if fn == 'MANIFEST.txt':
                continue
            src = os.path.join(ex_dir, fn)
            digest = md5(src)
            if fn in seen and seen[fn][1] != digest:
                conflicts.append((fn, seen[fn][0], batch))
            seen[fn] = (batch, digest)
            plan.append((batch, src, fn))

    print(f'批次 {len(found)} 个，示例文件 {len(plan)} 个'
          + (f'，目标 {dst}' if not check_only else '（--check：不写盘）'))
    for batch, ex_dir in found:
        n = len([1 for b, _, _ in plan if b == batch])
        print(f'  {batch}: {n} 个文件')

    if conflicts:
        print(f'\n重名冲突 {len(conflicts)} 处（同名不同内容，必须人工解决）：')
        for fn, b1, b2 in conflicts:
            print(f'  {fn}: {b1} 与 {b2} 内容不同')
        return 1

    if check_only:
        print('\n没有重名冲突，可以收集')
        return 0

    os.makedirs(dst, exist_ok=True)
    for _, src, fn in plan:
        shutil.copy2(src, os.path.join(dst, fn))

    # 合并成一份总表，标出来源批次，便于日后追溯
    lines = ['# 本课程全部示例代码', '',
             '每行：`文件`  TAB  `所属节点`  TAB  `期望（run=能跑通 / compile=只编译 / fail=故意编译不过）`  TAB  `来源批次`',
             '']
    for batch, ex_dir in found:
        for line in open(os.path.join(ex_dir, 'MANIFEST.txt'), encoding='utf-8'):
            line = line.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            lines.append(line + '\t' + batch)
    with open(os.path.join(dst, 'MANIFEST.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f'\n已收集到 {dst}：'
          f'{len(plan)} 个示例文件 + MANIFEST.txt（总表）')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
