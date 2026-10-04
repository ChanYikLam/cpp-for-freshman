#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把课程打包成一个可以直接通过微信发送的压缩包。

用法：
    python3 -X utf8 -B make_package.py [<repo>]

产出：<repo>/dist/cpp-零基础入门-微信版.zip，解压后第一层就是文件夹本身，
里面 `docs/index.html` 双击即开学，不需要联网、不需要装任何东西。

只打包发出去该有的东西：`docs/`、`lab/`、`README.md`。
**不打包** `.git/`（冗余且带历史）、`.learning/` 与 `build_site.py`（编辑用的源文件，
发课程不需要），`dist/` 自己也不进包。

微信对单个文件有大小限制，脚本结束时报告包体积；超过 20MB 会提醒改用「文件夹分卷发送」。
"""

import os
import sys
import zipfile

INCLUDE_DIRS = ('docs', 'texts')
# 解压后最外层看到的：`texts/` 里的三份引导说明（1-先读我 / 2-建议用电脑打开 / 3-学习指南）
# 与 `README.md`（给维护者看的）。**文件名带数字前缀是有意的**——解压后按名字排序时，
# 这三份会排在 `docs`、`README.md` 前面，学生一眼就看到；不带前缀的话它们会被夹在中间。
INCLUDE_FILES = ('README.md',)
SKIP_DIRS = {'.git', '.studymate-stage', '.stage', 'dist', '__pycache__', '.DS_Store'}
WARN_BYTES = 20 * 1024 * 1024


def main(argv):
    repo = os.path.abspath(argv[1]) if len(argv) > 1 else os.getcwd()
    docs = os.path.join(repo, 'docs')
    if not os.path.isfile(os.path.join(docs, 'index.html')):
        print(f'错误：{docs}/index.html 不存在，先跑 build_site.py', file=sys.stderr)
        return 1

    dist = os.path.join(repo, 'dist')
    os.makedirs(dist, exist_ok=True)
    name = os.path.basename(repo.rstrip(os.sep)) or 'cpp-course'
    zip_path = os.path.join(dist, f'{name}-微信版.zip')

    count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for d in INCLUDE_DIRS:
            base = os.path.join(repo, d)
            if not os.path.isdir(base):
                continue
            for root, dirs, files in os.walk(base):
                dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
                for fn in sorted(files):
                    if fn in SKIP_DIRS:
                        continue
                    src = os.path.join(root, fn)
                    # `texts/` 里的引导说明**平铺到压缩包最外层**，不放进子目录——
                    # 学生解压后要一眼看到「1-先读我」，而不是先点进一个 texts 文件夹
                    # （真实踩到过：引导放进子目录等于没有引导）。
                    inner = fn if d == 'texts' else os.path.relpath(src, repo)
                    z.write(src, os.path.join(name, inner))
                    count += 1
        for fn in INCLUDE_FILES:
            src = os.path.join(repo, fn)
            if os.path.isfile(src):
                z.write(src, os.path.join(name, fn))
                count += 1

    size = os.path.getsize(zip_path)
    print(f'压缩包已生成：{zip_path}')
    print(f'  打包 {count} 个文件 · 体积 {size / 1024:.0f} KB')
    print('  对方解压后：先看最外层的「1-先读我.md」，再双击 docs/index.html')
    if size > WARN_BYTES:
        print(f'  注意：超过 20MB，微信传文件可能较慢，也可直接发整个文件夹', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
