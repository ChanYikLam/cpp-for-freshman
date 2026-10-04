#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""逐个编译（并运行）课件里的示例代码 —— 「每章带可编译代码」这句话的证据。

用法：
    python3 -X utf8 -B check_examples.py <科目目录> [<目录名> ...]

`<科目目录>` 下按 `<目录名>`（默认扫 `.stage` 里所有 `learning-coach-*`）找
`examples/MANIFEST.txt`，逐行读：

    <stem>\t<所属节点id>\t<期望>      # 期望 ∈ run | compile | fail

三种期望的判定（**这是与写课件的人之间的契约，改这里要同步改派工说明**）：

| 期望 | 这份 .cpp 应该是什么 | 我验什么 |
|------|---------------------|---------|
| `run` | 完整正确、读者照着敲就能跑 | 必须编译通过 **且**运行成功（退出码 0） |
| `compile` | 正确但这次不想跑（例如需要交互输入） | 必须编译通过；不运行 |
| `fail` | **故意写错的反例**（少分号、类型不匹配…） | **必须编译失败**，否则说明反例根本没写错 |

有 `<stem>.in` 就把内容喂给标准输入；没有就给空 stdin（避免程序卡在等待输入上）。
运行崩溃或超时的（退出码非 0）→ 记为失败：**课件里的示例不该崩，崩溃演示请在正文里用代码
加文字讲，不要靠读者去跑一段注定要崩的程序。**

早先这里只有 `run=yes|no` 两种，把「故意编译不过的反例」与「故意崩溃的演示」混在一个取值里，
验证器无法区分二者，一个写得正确的反例会被误报成「编译失败」。分成三个取值后契约才闭合。

退出码：全绿 0；有任何不符 1（按 `<文件>` 逐条打印，可直接打回给写的人）。

为什么要有这个脚本：课件里的每一段完整代码都承诺「读者照着敲就能编译运行」。
这句话不能靠写的人自己声称——发到新生手里编译不过，这套课的信誉就没了。这里用
**编译器**做验收，跑出来的就是证据。
"""

import os
import subprocess
import sys
import tempfile

STD = '-std=c++17'
WARN = ['-Wall', '-Wextra', '-Wno-unused-parameter']
TIMEOUT = 10
EXPECTATIONS = ('run', 'compile', 'fail')


def parse_manifest(path):
    """读 MANIFEST.txt → [(stem, node, expect)]，同时报出格式不对的行（不静默跳过）。"""
    entries, bad = [], []
    with open(path, encoding='utf-8') as f:
        for lineno, line in enumerate(f, 1):
            line = line.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            parts = [p.strip() for p in line.split('\t')]
            if len(parts) < 2:
                bad.append((lineno, line, '少于两列（应为 <stem>\\t<节点id>\\t<run|compile|fail>）'))
                continue
            stem, node = parts[0], parts[1]
            expect = parts[2] if len(parts) > 2 else ''
            # 兼容早期写法 run=yes|no（yes→run，no→compile），但**报出来**提醒改，
            # 因为 run=no 无法表达「故意编译不过的反例」。
            legacy = None
            if expect.startswith('run='):
                legacy = expect
                expect = 'run' if expect.split('=', 1)[1].strip().lower() == 'yes' else 'compile'
            if expect not in EXPECTATIONS:
                bad.append((lineno, line,
                            f'第三列应为 run/compile/fail 之一，实际 {expect!r}'))
                continue
            entries.append((stem, node, expect, legacy))
    return entries, bad


def check_one(cpp_path, expect, workdir):
    """按期望编译（必要时运行）一个示例，返回 (状态, 详情)。"""
    exe = os.path.join(workdir, 'a.out')
    compile_cmd = ['g++', STD] + WARN + [cpp_path, '-o', exe]
    proc = subprocess.run(compile_cmd, capture_output=True, text=True)
    compiled = proc.returncode == 0
    diag = (proc.stderr or proc.stdout).strip()

    if expect == 'fail':
        if compiled:
            return '不符预期', '这份标了「故意写错的反例」，但它居然编译通过了——反例没写错，读者学不到东西'
        return '通过（反例确实编译不过）', ''

    if not compiled:
        return '编译失败', diag

    if expect == 'compile':
        return '通过（仅编译）', ''

    stdin_path = os.path.splitext(cpp_path)[0] + '.in'
    stdin_data = ''
    if os.path.isfile(stdin_path):
        with open(stdin_path, encoding='utf-8') as f:
            stdin_data = f.read()
    try:
        run = subprocess.run([exe], input=stdin_data, capture_output=True,
                             text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return '运行超时', f'超过 {TIMEOUT}s 还没结束（程序可能在等输入，或死循环）'
    if run.returncode != 0:
        detail = f'退出码 {run.returncode}'
        if run.returncode < 0:
            detail += f'（被信号 {-run.returncode} 终止，通常是段错误）'
        err = (run.stderr or '').strip()
        if err:
            detail += f'\n{err}'
        return '运行失败', detail
    return '通过', (run.stdout or '').strip()


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    dirs = argv[2:]
    if not dirs:
        stage = os.path.join(subject, '.stage')
        dirs = [d for d in sorted(os.listdir(stage)) if d.startswith('learning-coach-')] \
            if os.path.isdir(stage) else []
    if not dirs:
        print('找不到任何 examples/ 目录（没传目录名，且 .stage 下没有 learning-coach-*）')
        return 0

    total = passed = 0
    failures = []
    legacy_seen = []
    for name in dirs:
        base = name if os.path.isabs(name) else os.path.join(subject, '.stage', name)
        manifest = os.path.join(base, 'examples', 'MANIFEST.txt')
        print('=' * 74)
        print(f'{name}')
        if not os.path.isfile(manifest):
            print('  （没有 examples/MANIFEST.txt，跳过）')
            continue
        entries, bad = parse_manifest(manifest)
        for lineno, line, why in bad:
            print(f'  MANIFEST.txt:{lineno} 格式问题：{why}')
            print(f'    {line}')
            failures.append((f'{name}/examples/MANIFEST.txt:{lineno}', '格式问题', why))
        with tempfile.TemporaryDirectory() as tmp:
            for stem, node, expect, legacy in entries:
                if legacy:
                    legacy_seen.append(f'{name}: {stem} 用了旧写法 {legacy}')
                cpp = os.path.join(base, 'examples', f'{stem}.cpp')
                total += 1
                if not os.path.isfile(cpp):
                    print(f'  [缺文件] {stem}.cpp  （节点 {node}）')
                    failures.append((f'{name}/{stem}.cpp', '缺文件', 'MANIFEST 登记了但文件不存在'))
                    continue
                status, detail = check_one(cpp, expect, tmp)
                if status.startswith('通过'):
                    passed += 1
                    print(f'  [{status}] {stem}.cpp  （节点 {node}，期望 {expect}）')
                else:
                    print(f'  [{status}] {stem}.cpp  （节点 {node}，期望 {expect}）')
                    for line in detail.splitlines()[:12]:
                        print(f'      {line}')
                    failures.append((f'{name}/{stem}.cpp', status, detail))

    print('=' * 74)
    print(f'共 {total} 个示例：通过 {passed}，失败 {len(failures)}')
    if legacy_seen:
        print(f'\n提醒：{len(legacy_seen)} 行用了旧的 run=yes|no 写法，'
              '已按 yes→run、no→compile 兼容处理；请改成三取值：')
        for line in legacy_seen[:10]:
            print(f'  {line}')
    if failures:
        print('\n要修的地方：')
        for path, status, detail in failures:
            first = detail.splitlines()[0] if detail else ''
            print(f'  [{status}] {path} — {first}')
        return 1
    print('全部通过：run 的能编译且跑通，compile 的能编译，fail 的确实编译不过')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
