#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把中文字体裁成「课程实际用到的字」子集，打进课程包，让任何设备都能看到仿宋。

用法：
    python3 -X utf8 -B tools/subset_font.py <课程目录> [--src <字体文件>] [--out <输出路径>]

为什么必须随包带字体：主编者要求中文字体统一用**仿宋**（仿宋_GB2312）。那个字体不是
macOS/Windows/手机自带，而是主编者本机手动安装的（`~/Library/Fonts/仿宋_GB2312.ttf`）。
不打包的话，只有装过这个字体的电脑能看到仿宋——学生的 Windows、手机、iPad 全都会回退到
黑体或宋体，等于没改。而原字体 3.8 MB，整个塞进要发微信的包太沉。

做法：**按课程里真正出现过的汉字取子集**（本课程约 2900 个不同汉字），只保留这些字的字形，
文件能小一个数量级；再把子集的 `unicode-range` 限定在汉字区，**英文与数字继续用原来的字体栈**
（主编者要求「英文字体不要改」）。

改课程内容后如果出现了新汉字，重跑一次本脚本即可（缺字会回退到系统字体，不会显示成方框）。
"""

import argparse
import os
import sys
import unicodedata
from collections import Counter


def cjk_chars(root):
    """扫课程产物，收集所有出现过的汉字与中文标点。"""
    got = Counter()
    exts = ('.html', '.md', '.txt', '.cpp', '.json', '.yaml', '.yml')
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ('.git', 'dist', '__pycache__')]
        for fn in files:
            if not fn.endswith(exts):
                continue
            try:
                text = open(os.path.join(dirpath, fn), encoding='utf-8').read()
            except (OSError, UnicodeDecodeError):
                continue
            for ch in text:
                # 汉字 + 中文标点与全角符号（这些也想用仿宋的样子）
                if '\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f' \
                        or '\uff00' <= ch <= '\uffef':
                    got[ch] += 1
    return got


def main(argv):
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('root')
    ap.add_argument('--src', default=os.path.expanduser('~/Library/Fonts/仿宋_GB2312.ttf'))
    ap.add_argument('--out', default=None)
    args, _ = ap.parse_known_args(argv[1:])

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f'错误：{root} 不是目录', file=sys.stderr)
        return 2
    if not os.path.isfile(args.src):
        print(f'错误：找不到源字体 {args.src}', file=sys.stderr)
        return 2

    out = args.out or os.path.join(root, 'assets', 'fonts', 'fangsong-subset.woff2')
    os.makedirs(os.path.dirname(out), exist_ok=True)

    chars = cjk_chars(root)
    if not chars:
        print('没扫到任何汉字，放弃（是不是目录给错了？）', file=sys.stderr)
        return 2
    text = ''.join(sorted(chars))
    print(f'课程里的汉字：{len(chars)} 种（共出现 {sum(chars.values())} 次）')

    try:
        from fontTools import subset
    except ImportError:
        print('需要 fontTools：pip install fonttools brotli', file=sys.stderr)
        return 2

    options = subset.Options()
    options.flavor = 'woff2'          # 浏览器支持最广的压缩格式
    options.desubroutinize = True
    options.hinting = False           # 网页显示不需要微调指令，能显著减小体积
    options.layout_features = ['*']
    options.drop_tables += ['DSIG']
    options.notdef_outline = True     # 缺字时至少给个轮廓，而不是空白

    font = subset.load_font(args.src, options)
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    subset.save_font(font, out, options)
    font.close()

    src_mb = os.path.getsize(args.src) / 1024 / 1024
    out_kb = os.path.getsize(out) / 1024
    print(f'子集已生成：{out}')
    print(f'  {src_mb:.1f} MB → {out_kb:.0f} KB（{out_kb / (src_mb * 1024) * 100:.1f}%）')
    print('  改课内容后若出现新汉字，重跑本脚本即可；缺字会回退系统字体，不会显示成方框')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
