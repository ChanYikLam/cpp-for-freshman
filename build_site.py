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
from urllib.parse import unquote
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
    # 页面在 docs/lessons/ 下，而资源在 docs/assets/ 下——**只差一层**，所以是 `../assets/`。
    # 早先写成 `../../assets/`，从 docs/lessons/ 出发会解析到 docs/ 之上（<repo>/assets/），
    # 于是 18 页 × 7 条资源引用全是断链（真实踩到过，而且断链自检当时没拦住）。
    ('../../../assets/', '../assets/'),
    ('../assets/', '../assets/'),
    ('../index.html', '../index.html'),
    # 注意：`lab/`、`code/` 这两棵目录的父级层数**因页面所在目录而异**（docs/lessons/ 要退两层、
    # docs/cpp-basics/lessons/ 只要退一层），所以不在这里写死规则——统一交给构建后的
    # `fix_generated_pages()` 按每个文件的真实深度重算。写死规则的结果是：一处放对、另一处放错
    # （真实踩到过：20 条死链，两个方向都有）。
]

# 打包时跳过的目录/文件名（编辑用与系统垃圾，发课程不需要）
# 生成页里指向 `xxx.md` 的链接：站点里那些 .md 是以编译后的 .html 形式存在的，
# 指回 .md 会 404。用替换函数而不是 `\1` 后向引用——后者容易在多层转义里被写坏。
MD_HREF_RE = re.compile(r'(href="[^"]+?)\.md(?![/\w])(#[^"]*)?"')

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
            text = read_text(os.path.join(src_subj, name))
            # `.md` 链接要改成 `.html`：站点里那些资料是以 gen_home.py 编译出的 .html
            # 形式存在的，指回 .md 会 404（真实踩到过）。
            text = MD_HREF_RE.sub(
                lambda m: 'href="' + m.group(1)[6:] + '.html'
                + (m.group(2) or '') + '"', text)
            write_text(os.path.join(dst_subj, name), rewrite(text, ref_rules))
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

        # 子目录里的编译产物：`gen_home.py` 会把科目下的 .md 编译成同名 .html 挂到附件区。
        # 它们必须跟着走，否则附件区那几条是死链（真实踩到过：168 条断链）。
        #
        # **相对路径按目录深度算**，别一套规则套所有层：
        #   深度 1（learning-records/、reference/ 的直下文件）→ 回链与组件各差一层
        #   深度 2（reference/<子目录>/）→ 再退一层
        # x.text() 的链接是 URL 编码的，os.listdir 给的是原文，两边不会撞。
        def sub_rules(depth):
            up = '../' * depth
            return [
                ('../../../index.html', up + 'index.html'),
                ('../../assets/', up + 'assets/'),
                ('assets/', up + 'assets/'),
            ]

        for sub in sorted(os.listdir(src_subj)):
            sub_dir = os.path.join(src_subj, sub)
            if sub.startswith('.') or not os.path.isdir(sub_dir):
                continue
            # reference/ 与 sources/ 的资料要**整份**跟着走（不只是 .html）：
            # 生成出来的 GLOSSARY/RESOURCES 页面会链到 `reference/xxx.md` 与
            # `sources/xxx.md`，只带 HTML 过去那些链接还是死的。
            # sources/ 按规范不挂科目主页，但它被 RESOURCES 页面引用，学生点进去也该能看到。
            # `sources/` 是**内部依据**（资料收集抓的原文，供讲解写课件时核对），
            # 不属于学生该看到的东西：它占 2.5 MB×2，而全站只有 1 条链接指向它。
            # 所以不发布它，那条链接在下面被替换成一句说明。
            keep_all = sub == 'reference'
            for root, dirs, files in os.walk(sub_dir):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
                depth = os.path.relpath(root, src_subj).count(os.sep) + 1
                for name in sorted(files):
                    if name in SKIP_DIRS or name.startswith('.'):
                        continue
                    if not keep_all and not name.endswith('.html'):
                        continue
                    rel = os.path.relpath(os.path.join(root, name), src_subj)
                    dst = os.path.join(dst_subj, rel)
                    src_path = os.path.join(root, name)
                    if name.endswith('.html'):
                        # 生成页里的 `.md` 链接要改成对应的 `.html`——那些 .md 在站点里
                        # 是以编译后的 .html 形式存在的，指回 .md 会 404。
                        text = read_text(src_path)
                        # 拼回整段匹配：结尾那个引号在两处捕获之外，只用 group(1)+group(2)
                        # 会把它吞掉，生成 `href="a.html` 这种半截属性（真实踩到过）。
                        text = MD_HREF_RE.sub(
                            lambda m: 'href="' + m.group(1)[6:] + '.html'
                            + (m.group(2) or '') + '"', text)
                        write_text(dst, rewrite(text, sub_rules(depth)))
                    else:
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy2(src_path, dst)
                    stats['reference'] += 1


    # ⑤ 根目录再放一份术语表与资源清单：方便直接翻，不经过科目主页
    for slug in slugs:
        src_subj = os.path.join(src_subjects, slug)
        for name in ('GLOSSARY.html', 'RESOURCES.html'):
            s = os.path.join(src_subj, name)
            if not os.path.isfile(s):
                continue
            text = read_text(s)
            # 根目录这份也在站点根，所以它引用的 `reference/…` 与 `sources/…` 必须在
            # **站点根**能找到（下面那步会把两棵资料树也拷到 docs/ 根）。同理改掉 .md 链接。
            text = MD_HREF_RE.sub(
                lambda m: 'href="' + m.group(1)[6:] + '.html'
                + (m.group(2) or '') + '"', text)
            write_text(
                os.path.join(docs, name),
                rewrite(text, [('../../../index.html', 'index.html'),
                               ('../../assets/', 'assets/'),
                               ('assets/', 'assets/')]),
            )

    # ⑤b 资料树也放一份到站点根：根上的 GLOSSARY/RESOURCES 页面链的是 `reference/…`
    #     与 `sources/…`（站点根相对路径），只拷到 `<slug>/` 下的话那些链接是死的。
    for slug in slugs:
        src = os.path.join(src_subjects, slug, 'reference')
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(docs, 'reference'), dirs_exist_ok=True)

    # ⑤c 构建后统一规范化：① 资产路径按文件深度算 ② 把「有同名 .html」的 .md 链接改成 .html。
    #
    # 两件事都必须**事后**做，因为深度由产物目录决定，写进规则表会随层级爆炸（真实踩到过：
    # reference/ 下三层的生成页把 `../../../assets/` 留了下来）。 .md 那件也不能无脑改：
    # 有些 .md 根本没有编译产物（gen_home.py 只编译 reference/ 与 learning-records/ 两类），
    # 改成 .html 反而制造新的死链——必须**先看文件在不在**。
    write_dir_indexes(docs)
    fix_generated_pages(docs)

    # ⑥ 术语表提到显眼位置：生成器把 GLOSSARY 放在科目页**底部**的附件区，而这份课程的对象
    #    是零基础新生——他们最需要的就是一个随时能翻的术语表，藏在最底下等于没有。
    inject_glossary_links(docs, slugs)

    # ⑦ 落一份建站产物说明，避免有人手改 docs/ 里的页面
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
                # **必须解码**：`gen_home.py` 生成的附件链接是 URL 编码的
                # （`C%2B%2BPrimerPlus…`），不解码就会把真实存在的文件判成断链
                # （真实踩到过：自检报 13 条断链，而独立复核解码后是 0 条）。
                target = os.path.normpath(os.path.join(
                    root, unquote(ref.split('#')[0])))
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

# 只匹配**路径段本身**（一串 `../` 后面跟 assets/），不碰引号、不碰 `href=` 前缀。
# 早先的写法把 `href="` 也框进匹配里，替换时拼不回原样，等于把每个 href 的路径都咬掉一截
# （真实踩到过：规范化这一步把课件里的 lab 链接全改坏了）。
# 相对引用（资产、lab、code）在生成页里都写成「一串 `../` + 目录名」，产物目录一变就对不上。
# 这里统一按**文件在站点里的实际深度**重算前缀，一次修对所有目录。
REL_REF_RE = re.compile(r'((?:\.\./)+)(assets|lab|code)/')


def write_dir_indexes(docs):
    """给 `lab/*/` 与配套源码目录补一份 `index.html` 落地页。

    这些目录里的说明是 `.md`，而 `gen_home.py` 只编译 `reference/` 与 `learning-records/` 两类，
    所以课件里 `.../README.html` 这类链接会 404（真实踩到过）。补一份**极简**落地页，
    列出目录里的文件；不发样式、不引组件，纯 HTML，学生双击就能看到有哪些文件。

    在**站点侧**生成而不是写回学习工作区：源树里只有 .md，站点里才是给人看的形态。
    """
    made = 0
    targets = []
    lab = os.path.join(docs, 'lab')
    if os.path.isdir(lab):
        for d in sorted(os.listdir(lab)):
            full = os.path.join(lab, d)
            if os.path.isdir(full) and d != 'solutions':
                targets.append(full)
    # 配套源码目录在站点里有**两份**：根上的 `sources/…` 与科目下的 `<slug>/sources/…`
    # （科目主页那份的附件区链的是后者）。两份都要落地页，否则总有一边是死链。
    for base in (os.path.join(docs, 'sources'), *(os.path.join(docs, d, 'sources')
                                                  for d in sorted(os.listdir(docs))
                                                  if os.path.isdir(os.path.join(docs, d)))):
        cand = os.path.join(base, 'C++PrimerPlus-第6版-官方配套源码')
        if os.path.isdir(cand):
            targets.append(cand)

    for d in targets:
        files = sorted(n for n in os.listdir(d) if os.path.isfile(os.path.join(d, n)))
        dirs = sorted(n for n in os.listdir(d) if os.path.isdir(os.path.join(d, n)))
        rows = []
        for sub in dirs:
            rows.append(f'<li><b>{html.escape(sub)}/</b></li>')
        for n in files:
            rows.append(f'<li><a href="{html.escape(n)}">{html.escape(n)}</a></li>')
        body = ('<!DOCTYPE html><html lang="zh-CN"><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{html.escape(os.path.basename(d))} · 文件列表</title>'
                '<style>body{font-family:system-ui,-apple-system,"PingFang SC",sans-serif;'
                'max-width:44em;margin:2em auto;padding:0 1em;line-height:1.7}'
                'li{margin:.15em 0}a{color:#0a6c4f}</style>'
                f'<h1>{html.escape(os.path.basename(d))}</h1>'
                '<p>这个目录里的文件（点开看或另存下来用）：</p><ul>' + ''.join(rows) + '</ul>'
                '<p><a href="../../index.html">← 回到课程首页</a></p>')
        # 文件名用 README.html：课件里的链接写的就是 `.../README.html`（渲染器把 .md 换成 .html）
        write_text(os.path.join(d, 'README.html'), body)
        made += 1
    print(f'  目录落地页：生成 {made} 份')


def fix_generated_pages(docs):
    """构建后统一修两件事：资产路径按深度算、`.md` 链接在确有 .html 时才改写。

    · 资产路径：生成页里可能是 `../../../assets/`（按源目录形状写的），产物目录一变就对不上。
      这里按**文件在站点里的实际深度**重算，深度不同也能一次修对。
    · `.md` 链接：只在该 .md 旁边确实存在同名 `.html` 时才改；没有编译产物的保持 `.md`
      （浏览器会按纯文本显示，仍然可用），避免把好链接改成死链。
    """
    fixed_assets = fixed_md = 0
    for root, dirs, files in os.walk(docs):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith('.html'):
                continue
            page = os.path.join(root, fn)
            text = read_text(page)
            rel_dir = os.path.relpath(root, docs)
            depth = 0 if rel_dir == '.' else rel_dir.count(os.sep) + 1
            up = '../' * depth

            def sub_asset(m):
                nonlocal fixed_assets
                if m.group(1) != up:
                    fixed_assets += 1
                return up + m.group(2) + '/'

            new = REL_REF_RE.sub(sub_asset, text)

            def sub_md(m):
                nonlocal fixed_md
                target = m.group(1)
                html = os.path.normpath(os.path.join(root, target + '.html'))
                if os.path.isfile(html):
                    fixed_md += 1
                    return 'href="%s.html%s"' % (target, m.group(2) or '')
                # 没有编译产物就别改成 .html——那会把一个能用的 .md 链接变成死链。
                return m.group(0)

            new = MD_HREF_RE.sub(sub_md, new)

            # 教材 OCR 原文里 `ar2[0]` 会被生成器当成标签（下标方括号 + 数字 → `<a ...>`），
            # 页面里就留下 `<a href="c">` 这种空链接，目标是字面量 `c`，必然 404。
            # 这不是内容缺陷而是**解析痕迹**，站点侧统一拆掉，只留下原文里的字面量。
            new = re.sub(r'<a href="c">\s*', '', new)

            # `sources/` 不发布，指向它的链接换成一句说明——**既不留死链，也不假装它在包里**
            new = re.sub(r'<a href="(?:\.\./)*(?:[\w.-]+/)?sources/[^"]*"[^>]*>(.*?)</a>',
                         lambda m: m.group(1) + '（内部依据，未随课程发布）', new)

            # 已知的坏链接：RESOURCES 里那条「官方配套源码/README.md」，那个目录下其实
            # 没有顶层 README（说明在 `Chapter N/` 子目录里）。指向目录落地页才点得开。
            new = new.replace(
                'href="sources/C++PrimerPlus-第6版-官方配套源码/README.html"',
                'href="sources/C++PrimerPlus-第6版-官方配套源码/README.html"')
            new = new.replace(
                'href="sources/C++PrimerPlus-第6版-官方配套源码/README.md"',
                'href="sources/C++PrimerPlus-第6版-官方配套源码/README.html"')
            if new != text:
                write_text(page, new)
    print(f'  构建后规范化：资产路径修 {fixed_assets} 处 · .md→.html 改写 {fixed_md} 处')


GLOSSARY_STYLE = """<style>
.learn-glossary-callout{margin:var(--syo-space-4,1rem) 0 0;padding:14px 16px;border-radius:12px;
 border:1px solid color-mix(in srgb,var(--syo-accent,#0a6c4f) 34%,transparent);
 background:color-mix(in srgb,var(--syo-accent,#0a6c4f) 7%,transparent)}
.learn-glossary-callout__head{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0}
.learn-glossary-callout__title{font-size:1rem;font-weight:600;margin:0}
.learn-glossary-callout__body{margin:6px 0 0;font-size:.875rem;line-height:1.7;color:var(--syo-fg-muted,#555)}
.learn-glossary-callout__go{display:inline-block;margin-top:10px;padding:7px 14px;border-radius:999px;
 background:var(--syo-accent,#0a6c4f);color:#fff;font-size:.875rem;font-weight:600;text-decoration:none}
.learn-glossary-callout__go:hover{filter:brightness(1.08)}
</style>"""

GLOSSARY_CALLOUT = GLOSSARY_STYLE + """
<section class="learn-glossary-callout" aria-label="术语表">
  <p class="learn-glossary-callout__head">
    <span class="learn-glossary-callout__title">📖 术语表 · 遇到不懂的词先翻这里</span>
  </p>
  <p class="learn-glossary-callout__body">每个计算机专有名词都在这里写了「为什么需要它、它是什么、不要用哪个说法代替它」。
  看书时卡在某个词上，直接来这里查——不用往前翻找它在哪一章出现过。</p>
  <a class="learn-glossary-callout__go" href="{HREF}">打开术语表 →</a>
</section>
"""


def in_comment(text, pos):
    """pos 这个位置是不是落在 HTML 注释里（`<!--` 比 `-->` 更靠后就算）。"""
    before = text[:pos]
    return before.rfind('<!--') > before.rfind('-->')


def inject_glossary_links(docs, slugs):
    """把术语表放到两个「一眼就能看到」的位置。

    生成器把 GLOSSARY 只挂在科目页**底部**的附件区（`术语与资源` 那一组）。这份课程的读者是
    零基础新生，术语正是他们最需要随手翻的东西——放在最底下等于没有。所以这里在**课程首页**
    与**科目页顶部**各插一张卡片。

    为什么在打包阶段做而不是改生成器模板：`docs/` 本来就是生成产物，而模板属于学习系统的引擎，
    改它会影响别的科目。卡片自带内联样式，不引外部文件，离线照样正常。
    """
    made = 0
    for slug in slugs:
        # ① 科目页：插在 <main> 开头，也就是「在做的项目」卡片之前，紧跟页头
        page = os.path.join(docs, slug, 'index.html')
        if os.path.isfile(page) and 'learn-glossary-callout' not in read_text(page):
            text = read_text(page)
            anchor = f'<main class="syo-container learn-main" id="learn-content">'
            if anchor in text and not in_comment(text, text.find(anchor)):
                text = text.replace(
                    anchor, anchor + '\n' + GLOSSARY_CALLOUT.replace('{HREF}', 'GLOSSARY.html'), 1)
                write_text(page, text)
                made += 1

        # ② 课程首页：插在 `<main>` 开头，也就是科目卡片列表之前，学生一进来就看得到。
        #
        # ⚠️ 锚点必须挑**注释之外**的字符串：模板会把大段说明注释原样留在产物里，注释里也写着
        # `<div class="learn-subject-list">` 这类字样，拿它当锚点会把卡片插进注释里——
        # 页面上什么都没有，而检查还"通过"（真实踩到过）。这里用 `<main …>` 开头那一行，
        # 并额外确认插入点不在注释里。
        home = os.path.join(docs, 'index.html')
        if os.path.isfile(home) and '<section class="learn-glossary-callout"' not in read_text(home):
            text = read_text(home)
            anchor = '<main class="syo-container learn-main" id="learn-content">'
            pos = text.find(anchor)
            if pos >= 0 and not in_comment(text, pos):
                # 首页在站点根，术语表在 <slug>/GLOSSARY.html，相对路径要带上科目目录
                text = text[:pos + len(anchor)] + '\n' + \
                    GLOSSARY_CALLOUT.replace('{HREF}', f'{slug}/GLOSSARY.html') + \
                    text[pos + len(anchor):]
                write_text(home, text)
                made += 1
    print(f'  术语表入口：插入 {made} 处（课程首页 + 科目页顶部）')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
