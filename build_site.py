#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把 StudyMate 学习工作区里的课程，打包成一个自包含、可离线打开的静态站点。

用法：
    python3 -X utf8 -B build_site.py <WS> <repo>

    <WS>    学习工作区根（含 index.html 与 .learning/）
    <repo>  目标 git 仓库根；站点输出到 <repo>/docs/

为什么要这一步：StudyMate 渲染出来的页面，引用路径是按「学习工作区」的目录形状写死的
（根主页用 `.learning/assets/…`，课件用 `../../../assets/…`）。直接把这些文件发给新生，
他们电脑上没有 `.learning/` 这一层，页面就会变成没有样式的裸 HTML。

本脚本只做一件事：把生成产物按「站点形状」重新摆放，并同步改写相对引用，让 `docs/index.html`
双击即开、离线可用、可整体压缩经微信发送。它**不改任何学习数据**，也不改 `.learning/` 里的源文件，
因此可以反复运行。

产出的站点形状：
    docs/
    ├── index.html              # 首页（所有章节的入口）
    ├── style.css               # 科目主页样式（由科目 index.html 内联引用改写为平级）
    ├── lessons/                # 每一章一个 HTML
    ├── assets/                 # 全部离线资源（Sayo UI / 主题层 / 课件组件 / KaTeX）
    └── reference/              # 术语表、资源清单等参考页
"""

import html
import os
import re
import shutil
import sys
import unicodedata

# ── 相对引用改写表 ──────────────────────────────────────────────────────────
# 键是学习工作区里的写法，值是站点里的写法。按长度倒序替换，避免前缀互相吃掉。
ROOT_REWRITES = [           # 对 <repo>/docs/index.html 用
    ('.learning/assets/', 'assets/'),
    ('.learning/subjects/', ''),
]
SUBJECT_REWRITES = [        # 对 <repo>/docs/<slug>/index.html 用
    ('../../assets/', '../assets/'),
    ('../../../index.html', '../index.html'),
]
LESSON_REWRITES = [         # 对 <repo>/docs/lessons/<NNNN>-<id>.html 用
    ('../../../assets/', '../../assets/'),
    ('../assets/', '../../assets/'),
    ('../index.html', '../index.html'),
]

# 打包时跳过的目录/文件名（编辑用与系统垃圾，发课程不需要）
SKIP_DIRS = {'.git', '.stage', '.studymate-stage', 'dist', '__pycache__', '.DS_Store'}


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def rewrite(text, rules):
    """按规则表改写相对引用。

    规则是 (完整写法, 站点里的写法) 成对给的，一次性用正则替换 —— 分多次 `str.replace`
    会踩顺序陷阱（先换 `assets/` 会把它从 `../assets/` 里咬掉一截，变成 `../assets/` → `../../assets/`）。
    用法上把「完整写法」写成路径整段（含 `../` 前缀）即可，各规则互不为前缀。
    """
    pattern = re.compile('|'.join(re.escape(old) for old, _ in rules))
    table = {old: new for old, new in rules}
    return pattern.sub(lambda m: table[m.group(0)], text)


def plain(md_text):
    """把一页 Markdown 压成一句纯文本，给首页摘要用。"""
    lines = md_text.splitlines()
    # 跳过一级标题
    body = []
    for line in lines:
        s = line.strip()
        if s.startswith('#') or not s:
            continue
        if s.startswith('>'):
            continue
        body.append(s)
        if len(' '.join(body)) > 160:
            break
    text = ' '.join(body)
    text = re.sub(r'[*`\[\]]', '', text)
    text = re.sub(r'\((?:https?://|reference/)[^)]*\)', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:180]


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    ws = os.path.abspath(argv[1])
    repo = os.path.abspath(argv[2])
    docs = os.path.join(repo, 'docs')

    src_home = os.path.join(ws, 'index.html')
    src_learning = os.path.join(ws, '.learning')
    src_subjects = os.path.join(src_learning, 'subjects')
    if not os.path.isfile(src_home) or not os.path.isdir(src_subjects):
        print(f'错误：{ws} 不像一个学习工作区（缺 index.html 或 .learning/subjects/）', file=sys.stderr)
        return 1

    slugs = sorted(
        d for d in os.listdir(src_subjects)
        if os.path.isdir(os.path.join(src_subjects, d)) and not d.startswith('.')
    )
    if not slugs:
        print('错误：工作区里没有任何科目', file=sys.stderr)
        return 1

    # 重建 docs/（保证可反复运行，不留上一次的孤儿文件）
    if os.path.isdir(docs):
        shutil.rmtree(docs)
    os.makedirs(docs)

    stats = {'lessons': 0, 'subjects': 0, 'assets': 0, 'reference': 0, 'lab': 0, 'code': 0}

    # ① 资源：整个共享层 + 每个科目的组件，一次性拷进 docs/assets/
    assets_dst = os.path.join(docs, 'assets')
    shutil.copytree(os.path.join(src_learning, 'assets'), assets_dst)
    for slug in slugs:
        subj_assets = os.path.join(src_subjects, slug, 'assets')
        if os.path.isdir(subj_assets):
            for name in sorted(os.listdir(subj_assets)):
                s = os.path.join(subj_assets, name)
                if os.path.isfile(s):
                    shutil.copy2(s, os.path.join(assets_dst, name))
                    stats['assets'] += 1
    stats['assets'] += sum(len(f) for _, _, f in os.walk(assets_dst))

    # ② 首页：`.learning/assets/` → `assets/`；科目卡片 .learning/subjects/<slug>/ → <slug>/
    write_text(os.path.join(docs, 'index.html'), rewrite(read_text(src_home), ROOT_REWRITES))

    # ③ 每个科目：主页 + 章节 + 参考页
    for slug in slugs:
        src_subj = os.path.join(src_subjects, slug)
        dst_subj = os.path.join(docs, slug)
        os.makedirs(dst_subj, exist_ok=True)

        page = os.path.join(src_subj, 'index.html')
        if os.path.isfile(page):
            write_text(
                os.path.join(dst_subj, 'index.html'),
                rewrite(read_text(page), SUBJECT_REWRITES),
            )
            stats['subjects'] += 1

        # 章节页：课件目录里的 HTML 平移到 docs/lessons/，引用同步改写
        src_lessons = os.path.join(src_subj, 'lessons')
        htmls = []
        if os.path.isdir(src_lessons):
            htmls = sorted(n for n in os.listdir(src_lessons) if n.endswith('.html'))
        dst_lessons = os.path.join(docs, 'lessons')
        for name in htmls:
            write_text(
                os.path.join(dst_lessons, name),
                rewrite(read_text(os.path.join(src_lessons, name)), LESSON_REWRITES),
            )
            stats['lessons'] += 1

        # 参考页：gen_home.py 会把 GLOSSARY.md / RESOURCES.md 编译成同名 HTML，放在科目根。
        # 这类页面由科目主页的附件区链接，组件写成科目根相对路径（`assets/style.css`），
        # 与科目主页用的 `../assets/` 差一层，所以要多一条改写规则。
        ref_rules = SUBJECT_REWRITES + [('assets/', '../assets/')]
        for name in sorted(os.listdir(src_subj)):
            if not name.endswith('.html') or name == 'index.html':
                continue
            write_text(
                os.path.join(dst_subj, name),
                rewrite(read_text(os.path.join(src_subj, name)), ref_rules),
            )
            stats['reference'] += 1

        # 子目录里的编译产物（如 gen_home.py 把「学习记录」编译成的 learning-records/*.html）：
        # 它们同样挂在科目主页的附件区，所以必须跟着走，否则主页上那几条是死链。
        # 目录深度与科目根相差一层，回链与组件的相对路径都要多退一层。
        sub_rules = [
            ('../../../index.html', '../index.html'),
            ('../../assets/', '../assets/'),
            ('assets/', '../assets/'),
        ]
        for sub in sorted(os.listdir(src_subj)):
            sub_dir = os.path.join(src_subj, sub)
            if sub.startswith('.') or not os.path.isdir(sub_dir):
                continue
            for name in sorted(os.listdir(sub_dir)):
                if not name.endswith('.html'):
                    continue
                write_text(
                    os.path.join(dst_subj, sub, name),
                    rewrite(read_text(os.path.join(sub_dir, name)), sub_rules),
                )
                stats['reference'] += 1

    # ④ 动手练习（lab/）与示例代码（code/）：整份拷进 docs/，让课件里那两条链接
    #    在发出去的包里也点得开。学生拿到的是「网页 + 可下载的代码文件」两样：
    #    手机上看网页、电脑上做题。
    #
    #    code/ 由 `tools/collect_code.py` 从各讲述批次的 examples/ 收拢而来。
    #    少了这一步，课件 `::: resources` 里的 `code/xxx.cpp` 就是死链。
    for sub in ('lab', 'code'):
        count = 0
        for slug in slugs:
            src_dir = os.path.join(src_subjects, slug, sub)
            if not os.path.isdir(src_dir):
                continue
            dst_dir = os.path.join(docs, sub)
            for root, dirs, files in os.walk(src_dir):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for fn in sorted(files):
                    if fn in SKIP_DIRS:
                        continue
                    src = os.path.join(root, fn)
                    dst = os.path.join(dst_dir, os.path.relpath(src, src_dir))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(src, dst)
                    count += 1
        stats[sub] = count

    # ⑤ 根目录再放一份术语表与资源清单：方便直接翻，不经过科目主页
    for slug in slugs:
        src_subj = os.path.join(src_subjects, slug)
        for name in ('GLOSSARY.html', 'RESOURCES.html'):
            s = os.path.join(src_subj, name)
            if os.path.isfile(s):
                write_text(
                    os.path.join(docs, name),
                    rewrite(read_text(s), [('../../../index.html', 'index.html'),
                                           ('../../assets/', 'assets/'),
                                           ('assets/', 'assets/')]),
                )

    # ⑥ 落一份建站产物说明，避免有人手改 docs/ 里的页面
    write_text(os.path.join(docs, 'BUILD.md'), BUILD_NOTE)

    broken = check_local_links(docs)
    print(f'站点已生成：{docs}')
    print(f"  科目主页 {stats['subjects']} 个 · 章节 {stats['lessons']} 个 · "
          f"参考页 {stats['reference']} 个 · 练习文件 {stats['lab']} 个 · 示例代码 {stats['code']} 个 · "
          f"资源文件 {stats['assets']} 个")
    if broken:
        print(f'  断链 {len(broken)} 条（必须修）：', file=sys.stderr)
        for page, ref in broken:
            print(f'    {page} → {ref}', file=sys.stderr)
        return 1
    print('  本地引用自检：全部可达')
    return 0


COMMENT_RE = re.compile(r'<!--.*?-->', re.S)
LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')


def check_local_links(docs):
    """站点内每一条本地引用都要真的能打开——发到新生手里才发现白板就晚了。

    HTML 注释里的路径是模板的写法示例，不算引用（与引擎 check_lesson.py 同口径）。
    """
    broken = []
    for root, _, files in os.walk(docs):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            page = os.path.join(root, fn)
            text = COMMENT_RE.sub('', read_text(page))
            for m in LINK_RE.finditer(text):
                ref = m.group(1)
                if re.match(r'^(?:https?:|//|mailto:|data:|#)', ref):
                    continue
                target = os.path.normpath(os.path.join(root, ref.split('#')[0]))
                if not os.path.exists(target):
                    broken.append((os.path.relpath(page, docs), ref))
    return broken


BUILD_NOTE = """# 这是生成产物，不要手改

`docs/` 里的所有文件都是 `build_site.py` 从学习工作区（`<WS>/.learning/`）**生成**的，
手工修改会在下次构建时被覆盖。

| 目录 | 是什么 | 从哪来 |
|------|--------|--------|
| `docs/lessons/` | 每一章一个 HTML | `render_lesson.py` 从内容文件渲染 |
| `docs/code/` | **课程里出现过的全部示例代码**（可直接编译运行） | `tools/collect_code.py` 从各讲述批次的 `examples/` 收拢 |
| `docs/lab/` | 动手任务与参考解 | 出题环节产出 |
| `docs/assets/` | 样式、脚本、字体（全本地，断网也能看） | 共享层 + 科目组件 |

要改课内容，改 `.learning/subjects/<slug>/lessons/<NNNN>-<节点id>.md`（讲解）
或同名的 `.quiz.json`（题目），然后在引擎目录重新渲染并重跑构建：

```bash
# 1. 重新生成课件页面（会同时算出上/下节课指针）
python3 -X utf8 -B <root>/scripts/render_lesson.py <WS>/.learning/subjects/<slug> <节点id>
# 2. 重新生成首页与科目主页
python3 -X utf8 -B <root>/scripts/gen_home.py <WS>
# 3. 重新打包出这个可离线打开的站点
python3 -X utf8 -B build_site.py <WS> <repo>
```
"""

if __name__ == '__main__':
    sys.exit(main(sys.argv))
