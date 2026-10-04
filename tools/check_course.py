#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""课程内容自检：验那些引擎的渲染器/检查器不管、但「这套课能不能自学」必须成立的部分。

用法：
    python3 -X utf8 -B check_course.py <科目目录>

引擎的 `render_lesson.py` / `check_lesson.py` 管的是**格式与结构**（语法、锚点、上下章指针、
组件引用）。这个脚本补的是**学习体验**层面的确定性检查——它们同样能用文件判出来，不该靠人眼抽查：

| 检查 | 为什么必须自动验 |
|---|---|
| ① 每章至少一处动手 | 课程承诺「每章带代码实操」。`::: practice` 是读者动手的入口；一章一个都没有，那一章就是纯阅读。 |
| ② 动手块里得能看见结果 | 读者要照着敲，就得有**编译命令**与**预期输出**。只有代码、没说怎么跑、跑出来该长什么样，零基础读者会卡死在第一步。 |
| ③ 代码块点名了文件名 | 读者要把代码存成文件才能编译。正文写的文件名必须与 `examples/` 里的实际文件对得上，否则「照着敲」无处可照。 |
| ④ 覆盖度 | `kind: 实操/实验` 的节点必须有配套示例；`概念` 节点也应有示例（本课程要求概念课也能动手）。 |
| ⑤ 题目位置存在 | 每个内容文件都应有 `::: quiz` 锚点，否则这一章没有任何检验理解的地方。 |

退出码：0 全过；1 有需要改的项（逐条打印 `<文件> <问题>`，可直接打回给写课件的人）。
"""

import json
import os
import re
import sys

FENCE_RE = re.compile(r'^```(\w*)\s*$', re.M)
PRACTICE_RE = re.compile(r'^::: practice .+?$', re.M)
PRACTICE_BLOCK_RE = re.compile(r'^::: practice .*?$(.*?)^:::\s*$', re.M | re.S)
QUIZ_RE = re.compile(r'^::: quiz\s+(\S+)\s+锚点：(.+?)\s*$', re.M)
SVG_RE = re.compile(r'^::: svg\s*$', re.M)

# 「能看出怎么跑、跑出来是什么」的判据：块里出现编译命令，或出现一段终端输出
RUN_HINT_RE = re.compile(r'g\+\+|\bclang\+\+|\bmake\b|\./a\.out|\./[A-Za-z_][\w.-]*')
OUTPUT_FENCE_RE = re.compile(r'^```(?:term|text|sh|bash)\s*$', re.M)
# 正文里点名的示例文件名。只认两种**明确**写法：反引号包裹（`` `io-02.cpp` ``）
# 或 `code/` 前缀（`code/io-02.cpp`）。
#
# 为什么不用「裸的 xxx.cpp」：那会把 `zh.cppreference.com` 这种域名尾巴吃成文件名
# （真实误报过），也会把散文里泛指的文件名当成课程示例。窄化判据宁可少报，也不误报——
# 误报会让写课件的人开始绕开检查器，比不检查更糟。
CPP_MENTION_RE = re.compile(r'`(?:code/)?([A-Za-z][\w.-]*\.cpp)`|(?:^|[^`\w/])code/([A-Za-z][\w.-]*\.cpp)')


def code_fences(text):
    """→ [(围栏起始行号, 块内容)]，带语言标记的 ``` 围栏。行号从 1 起，指向 ``` 那一行。"""
    out, lines = [], text.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r'^```(\w*)\s*$', lines[i])
        if m:
            start, body = i + 1, []
            i += 1
            while i < len(lines) and not re.match(r'^```\s*$', lines[i]):
                body.append(lines[i]); i += 1
            out.append((start, '\n'.join(body)))
        i += 1
    return out


def mentions_in(text):
    """取正文里点名的示例文件名（两组捕获拍平，去掉 `code/` 前缀已由正则处理）。"""
    out = []
    for a, b in CPP_MENTION_RE.findall(text):
        name = a or b
        if name:
            out.append(name)
    return out


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def load_curriculum(subject):
    path = os.path.join(subject, 'curriculum.yaml')
    if not os.path.isfile(path):
        return None
    try:
        import yaml
    except ImportError:
        return None
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def collect_examples(subject):
    """扫 .stage 下所有 learning-coach-*/examples/，返回 {stem: (节点id, 期望)}。"""
    out = {}
    stage = os.path.join(subject, '.stage')
    if not os.path.isdir(stage):
        return out
    for name in sorted(os.listdir(stage)):
        if not name.startswith('learning-coach-'):
            continue
        man = os.path.join(stage, name, 'examples', 'MANIFEST.txt')
        if not os.path.isfile(man):
            continue
        for line in read(man).splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            parts = [p.strip() for p in line.split('\t')]
            if len(parts) >= 2:
                out[parts[0]] = (parts[1], parts[2] if len(parts) > 2 else '')
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    lessons_dir = os.path.join(subject, 'lessons')
    if not os.path.isdir(lessons_dir):
        print(f'没有 {lessons_dir}')
        return 1

    cur = load_curriculum(subject)
    kinds = {}
    order = []
    if cur:
        for i, n in enumerate(cur['nodes'], 1):
            kinds[n['id']] = n['kind']
            order.append((i, n['id'], n['kind']))

    examples = collect_examples(subject)
    ex_by_node = {}
    for stem, (node, exp) in examples.items():
        ex_by_node.setdefault(node, []).append((stem, exp))

    files = sorted(n for n in os.listdir(lessons_dir) if n.endswith('.md'))
    problems, infos = [], []

    for name in files:
        path = os.path.join(lessons_dir, name)
        text = read(path)
        m = re.match(r'^(\d{4})-(.+)\.md$', name)
        pos = int(m.group(1)) if m else None
        node = m.group(2) if m else name[:-3]
        kind = kinds.get(node, '?')

        # ① 至少一处动手
        practices = PRACTICE_RE.findall(text)
        if not practices:
            problems.append(f'{name}: 没有任何 `::: practice` 动手块——课程承诺每章都能动手，'
                            '纯阅读的一章不符合要求')

        # ② 每个「完整示例」代码块，正文要告诉读者存成什么文件名
        #
        # 这是零基础读者真正的卡点：看到一段完整程序，不知道要存成文件、更不知道存成什么名字，
        # 就没法照着做。判据取「块里出现 main(」——那是完整可编译程序的标志；
        # 短片段（一行声明、报错输出、终端交互）不适用，跳过。
        #
        # 早先这里判的是「每个 `::: practice` 块里都得有编译命令或预期输出」，
        # 结果把多步骤练习的第 2、3 步（在第 1 步已给命令的基础上继续改）全判成了缺陷——
        # **一次误报 8 处，逐块看下来全是假的**。检查器一爱报警，写课件的人就会开始绕开它，
        # 那比不检查更糟，所以这条判据整个换掉了。
        for lineno, block in code_fences(text):
            if 'main(' not in block:
                continue
            head = '\n'.join(text.splitlines()[max(0, lineno - 6):lineno - 1])
            if not re.search(r'[A-Za-z][\w.-]*\.cpp', head):
                problems.append(f'{name}:{lineno}: 这段完整程序的代码块前面没有说明存成什么文件名'
                                '——零基础读者不知道该把这代码存到哪里，就没法照着编译')

        # ⑥ 不许把内部暂存路径写进正文
        #    `.stage/…` 是编辑期的临时位置，交付前会清掉；学生点开只会 404。
        #    课件里引用代码应写 `code/<名字>.cpp`（由 tools/collect_code.py 收集到科目下）。
        for lineno, line in enumerate(text.splitlines(), 1):
            if '.stage/' in line:
                problems.append(f'{name}:{lineno}: 正文里出现了内部暂存路径 `.stage/…`——'
                                '那个目录交付前会被清掉，读者点开是死链；'
                                '请改成引用 `code/<名字>.cpp`')

        # ⑦ 正文点名的 .cpp 与课程自带示例的对账
        #
        # 这里**只提示、不报错**：正文点名一个 examples/ 里没有的文件名，有两种情况——
        #   a) 作者让读者**自己新建**的文件（第 1 章的 `hello.cpp` 就是，那是教学模板名，不该收录）；
        #   b) 作者引用了课程自带示例但名字写错（真错，但渲染器与站点断链自检会拦下并指出）。
        # 两者在这里分不出来，所以降级成提示——**分不出来的判据不该阻断**（早先按错误拦过，假阳性）。
        # 真正要报错的是 `code/` 前缀写错（下面单列），那种是明确的引用意图落空。
        mentioned = set(mentions_in(text))
        have = {stem for stem, _ in ex_by_node.get(node, [])}
        all_stems = set(examples)
        unregistered = sorted(x[:-4] for x in mentioned if x[:-4] not in all_stems)
        cross = sorted(x[:-4] for x in mentioned
                       if x[:-4] in all_stems and x[:-4] not in have)
        if unregistered:
            infos.append(f'{name}: 点名的 `{"`、`".join(unregistered)}.cpp` 不在课程自带示例里'
                         '（若是让读者自己新建的文件，属正常）')
        if cross:
            infos.append(f'{name}: 引用了其它节点的示例（正常，作回指用）：' + '、'.join(cross))

        # ④ 覆盖度
        if kind in ('实操', '实验') and not have:
            problems.append(f'{name}: 课型是 `{kind}`，但 examples/ 里没有本节点的示例——'
                            '实操课必须有可跑的东西')
        if kind == '概念' and not have:
            infos.append(f'{name}: 概念课没有配套示例文件（本课程要求概念课也能动手，建议补）')

        # ⑤ 题目位置
        quizzes = QUIZ_RE.findall(text)
        if kind != '实验' and not quizzes:
            problems.append(f'{name}: 没有任何 `::: quiz` 题目位置——'
                            '这一章没有任何检验读者是否理解的地方')

        infos.append(f'{name}: 课型 {kind}｜动手块 {len(practices)}｜图 {len(SVG_RE.findall(text))}'
                     f'｜题位 {len(quizzes)}｜示例 {len(have)}')

    print(f'共 {len(files)} 篇内容文件；examples/ 登记 {len(examples)} 个示例'
          f'（覆盖 {len(ex_by_node)} 个节点）')
    print('-' * 74)
    for line in infos:
        print('  ' + line)

    # 覆盖度总表：大纲里每个节点是否都有内容文件
    if cur:
        have_nodes = {re.match(r'^\d{4}-(.+)\.md$', n).group(1) for n in files
                      if re.match(r'^\d{4}-(.+)\.md$', n)}
        print('-' * 74)
        exp_nodes = [nid for _, nid, k in order if k == '实验']
        missing_files = [nid for _, nid, k in order if nid not in have_nodes and k != '实验']
        if missing_files:
            print(f'还没写内容文件的普通节点（{len(missing_files)} 个）：' + '、'.join(missing_files))
        else:
            print(f'普通节点内容文件齐了（{len(have_nodes)} 篇）；'
                  f'实验说明页 {len(exp_nodes)} 个由出题评估产：' + '、'.join(exp_nodes))

    print('=' * 74)
    if problems:
        print(f'需要改（{len(problems)} 项）：')
        for p in problems:
            print('  - ' + p)
        return 1
    print('内容自检通过：每章都有动手块与题目位置，正文点名的示例文件都能对上')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
