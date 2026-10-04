#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""验收动手任务（lab）：**留白态必须不满足预期、参考解必须满足预期**。

用法：
    python3 -X utf8 -B tools/check_lab.py <科目目录> [<lab 目录名> ...]

不给目录名就扫科目下 `lab/`（跳过 `lab/solutions/`）的每个任务目录。

对每个任务目录，用它的 README 与文件结构判定：

1. **留白态**：任务目录里的 `.cpp`（不放 `solutions/` 的）必须**编译通过但不满足预期输出**
   ——它本来就是留给学生补的。编译不过也算不合格（学生一上来就撞编译错误，那不是「留白」，
   是「残破」）。
2. **参考解**：`lab/solutions/<同名目录>/` 里的 `.cpp` 必须**编译通过、运行成功、退出码 0**。
   参考解是学生卡住后要对照的成品，跑不起来就毫无意义。
3. **自包含**：参考解里只包含 `#include` 标准库头文件，不引用任务目录之外的自定义文件
   （规范要求：学生把 `solutions/` 拷进自己的任务目录后要能直接编译直接跑）。

判据的写法（README 里怎么表达「预期输出」，我按这个读）：

- README 里用 ` ```term ` / ` ```text ` 围栏给出的**预期输出**会被抓出来，与运行结果对首行；
- 需要标准输入的任务，找同名的 `.in` 文件喂进去；没有就喂空 stdin（给 2 秒超时）。

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
OUT_FENCE_RE = re.compile(r'^```(?:term|text|sh|bash)\s*$', re.M)
INCLUDE_RE = re.compile(r'^\s*#\s*include\s*[<"]([^">]+)[">]')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def cpp_files(d):
    out = []
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x != 'solutions']
        for fn in sorted(files):
            if fn.endswith('.cpp'):
                out.append(os.path.join(root, fn))
    return out


def compile_only(path, workdir):
    exe = os.path.join(workdir, 'a.out')
    p = subprocess.run(['g++', STD] + WARN + [path, '-o', exe],
                       capture_output=True, text=True)
    return p.returncode == 0, exe, (p.stderr or p.stdout).strip()


def run(exe, dirpath, stem):
    stdin_path = os.path.join(dirpath, stem + '.in')
    data = read(stdin_path) if os.path.isfile(stdin_path) else ''
    try:
        p = subprocess.run([exe], input=data, capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return None, None, f'超过 {TIMEOUT}s 没结束（可能在等输入）'
    return p.returncode, (p.stdout or ''), (p.stderr or '').strip()


def is_output_fence(body):
    """判断一段终端围栏是「预期输出」还是「编译/运行命令」。

    判据：含有编译或运行命令的，是命令块；否则是输出块。README 里两者都可能有，
    而且命令块通常排在前——早先取第一条围栏，把 `g++ main.cpp -o main && ./main`
    当成了预期输出，真实误报过一次。
    """
    if re.search(r'\bg\+\+|\bclang\+\+|\bmake\b|\./|>\s*\S+\.(txt|in)\b', body):
        return False
    return bool(body.strip())


def first_output_line(readme):
    """从 README 里取第一段**预期输出**围栏的正文首行，作为对照用的代表行。"""
    for m in re.finditer(r'^```(?:term|text|sh|bash)\s*$', readme, re.M):
        rest = readme[m.end():]
        body = rest.split('```', 1)[0]
        if not is_output_fence(body):
            continue
        for line in body.splitlines():
            line = line.strip()
            if line:
                return line
    return None


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
        readme = os.path.join(task, 'README.md')
        expected = first_output_line(read(readme)) if os.path.isfile(readme) else None
        tasks = cpp_files(task)
        sols = cpp_files(sol) if os.path.isdir(sol) else []

        print(f'{name}: 留白任务 {len(tasks)} 个 · 参考解 {len(sols)} 个'
              + (f' · README 预期输出「{expected[:28]}…」' if expected else ' · README 里没找到预期输出块'))

        if not tasks:
            problems.append((name, '任务目录里没有 .cpp——学生没有可补的起点'))
        if not sols:
            problems.append((name, 'solutions/ 里没有参考解——学生卡住后无处对照'))

        with tempfile.TemporaryDirectory() as tmp:
            # ① 留白态：编译通过，但不该满足预期输出
            for path in tasks:
                total += 1
                stem = os.path.splitext(os.path.basename(path))[0]
                ok, exe, err = compile_only(path, tmp)
                if not ok:
                    problems.append((os.path.relpath(path, subject),
                                     f'留白态编译不过（学生一上手就撞编译错误）：'
                                     f'{err.splitlines()[0] if err else ""}'))
                    continue
                rc, out, rerr = run(exe, os.path.dirname(path), stem)
                if rc is None:
                    problems.append((os.path.relpath(path, subject), f'留白态运行{rc if rc is not None else ""}：{rerr}'))
                    continue
                if rc != 0:
                    problems.append((os.path.relpath(path, subject),
                                     f'留白态运行退出码 {rc}（学生跑到一半崩了，那不是「留白」是「残破」）'))
                elif expected and expected in (out or ''):
                    problems.append((os.path.relpath(path, subject),
                                     '留白态**已经满足了** README 里的预期输出——'
                                     '任务没有留白，学生照着跑就过了，学不到东西'))

            # ② 参考解：编译通过、运行成功
            for path in sols:
                total += 1
                stem = os.path.splitext(os.path.basename(path))[0]
                ok, exe, err = compile_only(path, tmp)
                if not ok:
                    problems.append((os.path.relpath(path, subject),
                                     f'参考解编译不过：{err.splitlines()[0] if err else ""}'))
                    continue
                rc, out, rerr = run(exe, os.path.dirname(path), stem)
                if rc is None:
                    problems.append((os.path.relpath(path, subject), f'参考解运行{rerr}'))
                elif rc != 0:
                    problems.append((os.path.relpath(path, subject),
                                     f'参考解运行退出码 {rc}：{rerr.splitlines()[0] if rerr else ""}'))
                elif expected and expected not in (out or ''):
                    problems.append((os.path.relpath(path, subject),
                                     f'参考解的输出里没有 README 写的预期行「{expected[:30]}」'
                                     '——学生对照时会对不上'))

                # ③ 自包含：只允许标准库头文件
                src = read(path)
                for inc in INCLUDE_RE.findall(src):
                    if inc.endswith('.h') or inc.endswith('.hpp'):
                        problems.append((os.path.relpath(path, subject),
                                         f'参考解引用了自定义头文件 `{inc}`——'
                                         '学生拷进任务目录后编不过（参考解要自包含）'))

    print('-' * 74)
    print(f'共检查 {total} 个 .cpp')
    if problems:
        print(f'不合格 {len(problems)} 项：')
        for path, why in problems:
            print(f'  - {path}: {why}')
        return 1
    print('lab 验收通过：留白态都不满足预期，参考解都能编译并跑出预期输出')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
