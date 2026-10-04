#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""检查课件用词是否与「术语表」一致 —— 全课「同一个概念只用一个说法」的证据。

用法：
    python3 -X utf8 -B check_glossary.py <科目目录>

读 `<科目目录>/GLOSSARY.md` 里每个术语的 `_Avoid_:` 项，再在 `lessons/*.md` 与
`lessons/*.quiz.json` 里找这些别名的出现。术语表自己声明了两种写法的区别（见它开头的
「用词纪律」），检查器照它判：

| 术语表里的写法 | 含义 | 检查器怎么处理 |
|---|---|---|
| `操作符、算符` | 同一个概念的另一种叫法 | 出现即报错 |
| `二进制（**这是另一个概念**：…）` | 不同概念，不是禁用词 | 跳过，不报 |

判定分两条，**都得看**：

1. **只有「行文里把别名当术语用」才算错** —— 别名被加粗（`**操作符**`）或加引号
   （`「操作符」`、`` `操作符` ``）地写出，说明作者在给它下定义、在给读者建立叫法。
   顺带提到的（「把 `a` 和 `b` 连接起来」）不算错：那是正常用词，不是术语选择。
2. **别名是另一个规范名的一部分时跳过** —— 规范名「形参 / 实参」里含「参数」，
   规范名「编译」里含「编译过程」。

为什么要收紧到「加粗/加引号」这一条：早先版本按「出现即报错」判，第一轮就误报 45 处，
把「运行」「命令行」「过程」甚至英文单词 `command` 里的 `and` 都判成违规——**术语表自己
把不同概念写成了「避免的别名」**才是根因（已修）。检查器一旦爱报警，作者就会开始绕开它，
那比不检查更糟。
"""

import json
import os
import re
import sys

TERM_RE = re.compile(r'^\*\*(.+?)\*\*\s*[:：]\s*$')
AVOID_RE = re.compile(r'^_Avoid_\s*[:：]\s*(.+?)\s*$')
# 冒号半角全角都认：中文正文里两种都会出现（自己写术语表时就踩过全角冒号）
DISTINCT_RE = re.compile(r'^_另需分清[^_]*_\s*[:：]\s*(.+?)\s*$')
NOCHECK_RE = re.compile(r'^_别检查_\s*[:：]\s*(.+?)\s*$')
FENCE_RE = re.compile(r'^```.*?^```', re.S | re.M)
# 术语表用这个标记说明「这是另一个概念，不是禁用词」
DISTINCT_MARK = '另一个概念'
# 把别名「当术语用」的写法：加粗、中文引号、反引号包裹
AS_TERM_RE = r'(?:\*\*{a}\*\*|「{a}」|『{a}』|`{a}`)'


def split_items(text):
    """按顿号/逗号/斜杠切分，但**括号内的分隔符不算**。

    必须做括号感知：`_Avoid_: 操作符、算符（口语可用，正式表述统一说「运算符」）` 这一行里，
    括号内有一个逗号；若按分隔符硬切，`算符` 会与后半句粘连、甚至被丢掉，而检查器会**静默漏报**
    （比误报更危险：真实课件曾因此「通过」，其实该报的没报）。

    **半角与全角括号都要数**：中文正文里写的是全角 `（）`。只统计半角时深度永远不归零，
    于是一整行的分隔符全被当成「括号内」，`算符` 那种第二条起的别名会被整条吞掉（真实踩到过）。
    """
    items, buf, depth = [], [], 0
    for ch in text:
        if ch in '（(':
            depth += 1
        elif ch in '）)':
            depth = max(0, depth - 1)
        if ch in '、，,／/' and depth == 0:
            items.append(''.join(buf))
            buf = []
            continue
        buf.append(ch)
    items.append(''.join(buf))
    return [i.strip() for i in items if i.strip()]


def parse_glossary(path):
    """→ [(规范名, [作为同义词应避免的别名], [该条不检查的词])]。

    三种行的处理：

    - `_Avoid_:` —— 同一个概念的另一种叫法，正文里**不该**出现（跳过标了「另一个概念」的项）。
    - `_另需分清…_:` —— 不同概念，不是禁用词，**不检查**。
    - `_别检查_:` —— 这个词另有常用的普通含义（例如 `参数` 在泛指时是正常用词），**不检查**。

    后两种行**常跟在某些条目后面而不是每个条目后面**，所以 `current` 要一直保留到下一个
    `**术语**:` 行为止——早先每条读完就把它清空，导致这些行被静默忽略（检查因此漏判）。

    后两种行的豁免**只作用于它所在的这一条术语**，不做全局屏蔽：同一个词可能在甲术语那里
    是「另有含义」，在乙术语那里确实是该避免的别名，全局屏蔽会把后者一起放过。
    """
    terms = []
    current, aliases, skip = None, None, None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        m = TERM_RE.match(line)
        if m:
            if current and aliases:
                terms.append((current, aliases, skip or []))
            current, aliases, skip = m.group(1).strip(), [], []
            continue
        if not current:
            continue
        m = DISTINCT_RE.match(line) or NOCHECK_RE.match(line)
        if m:
            skip.extend(split_words(m.group(1)))
            continue
        m = AVOID_RE.match(line)
        if not m:
            continue
        for chunk in split_items(m.group(1)):
            note = ''
            if '（' in chunk:
                head, _, rest = chunk.partition('（')
                note = rest
                chunk = head.strip()
            if DISTINCT_MARK in note:
                continue
            if chunk:
                aliases.append(chunk)
    if current and aliases:
        terms.append((current, aliases, skip or []))
    return terms


def is_part_of_a_term_name(alias, term_names):
    """别名是不是某个规范名**本身的一个组成部分**。

    这类别名要放过：规范名「形参 / 实参」里含「参数」，正文里谈「参数」这个词本身是必要的。

    判据是「按规范名里的分隔符切开后，某一整段等于别名」，**不是裸子串**——
    裸子串会让「算符」被判成「运算符」的一部分（「运**算符**」）而被整体漏检，真实踩到过。
    """
    for name in term_names:
        for piece in re.split(r'[\s/／、和与]+', name):
            if piece == alias:
                return True
    return False


def split_words(text):
    """从 `_另需分清_:` / `_别检查_:` 那一行取词：括号或冒号之前的那部分才是词，说明丢掉。"""
    words = []
    for chunk in split_items(text):
        head = re.split(r'[（()：:]', chunk, maxsplit=1)[0].strip()
        if head:
            words.append(head)
    return words


def strip_fences(text):
    """把代码围栏整段换成等长空白（保留行号），返回 (正文, 围栏内文本)。"""
    inside = []

    def repl(m):
        inside.append(m.group(0))
        return '\n' * m.group(0).count('\n')

    return FENCE_RE.sub(repl, text), '\n'.join(inside)


def context(text, start, end, width=16):
    return text[max(0, start - width):min(len(text), end + width)].replace('\n', ' ')


# 「对比说明」的标志词：出现在别名**前面**一小段里时，作者是在解释叫法的区别，不是用错了词。
# 例如「这个概念在别的书里也叫**生存期**，本课程统一说生命周期」——这是必要的对比教学。
#
# 为什么必须豁免：术语表里的别名有一半正是**正文该主动讲清**的东西（「别人这么叫，我们那么叫」）。
# 不豁免就会逼着作者不敢讲区别，而讲清区别恰恰是这门课对零基础读者最大的价值之一。
CONTRAST_RE = re.compile(r'(也叫|又称|也叫作|常叫|俗称|别名|换句话说|有人叫|不要叫|不叫|避免|别用|不要用)')


def has_contrast_before(text, start, window=24):
    """别名出现处往前看一小段，判断它是不是在被「对比着说」。"""
    return bool(CONTRAST_RE.search(text[max(0, start - window):start]))


def as_term_hits(text, alias):
    """找出「把 alias 当术语用」的位置：加粗、引号、反引号包裹。

    拉丁字母/数字的别名（例如 `and`）额外要求词边界，否则会命中 `command` 里的 `and`。

    四种包裹形式**逐个各扫一遍**：写成一个交替正则再用 `finditer` 会漏——同一处附近若同时
    有 `**操作符**` 与 `「算符」` 两种形式，交替只会在该位置给出一个最长匹配，另一个就丢了
    （真实踩到过：一句里两种写法只报出一种）。

    边界断言**只加在别名后面**，不写前向断言——`「算符」` 紧跟 `「操作符」` 时，前一个匹配
    结束后光标落在两个引号之间，前向断言会把 `算符` 这条漏掉（真实踩到过）。
    """
    escaped = re.escape(alias)
    tail = r'(?![A-Za-z0-9_])' if re.fullmatch(r'[A-Za-z0-9_]+', alias) else ''
    hits = []
    for wrapper in (r'\*\*{}\*\*', '「{}」', '『{}』', '`{}`'):
        hits.extend(re.finditer(wrapper.format(escaped + tail), text))
    return hits


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    subject = os.path.abspath(argv[1])
    glossary = os.path.join(subject, 'GLOSSARY.md')
    lessons_dir = os.path.join(subject, 'lessons')
    if not os.path.isfile(glossary):
        print(f'没有 {glossary}，跳过')
        return 0

    terms = parse_glossary(glossary)
    skipped = sorted({w for _, _, sk in terms for w in sk})
    print(f'术语表：{len(terms)} 条带「避免的别名」的术语'
          + (f'，{len(skipped)} 个词在各自条目里声明「另有含义、不检查」' if skipped else ''))

    targets = []
    if os.path.isdir(lessons_dir):
        for name in sorted(os.listdir(lessons_dir)):
            if name.endswith('.md') or name.endswith('.quiz.json'):
                targets.append(os.path.join(lessons_dir, name))
    if not targets:
        print('lessons/ 下还没有课件文件，跳过')
        return 0

    errors, notes = [], []
    term_names = [t for t, _, _ in terms]
    for path in targets:
        raw = open(path, encoding='utf-8').read()
        body, fenced = strip_fences(raw)
        for term, aliases, skip in terms:
            for alias in aliases:
                # 别名是某个规范名本身的组成部分 → 忽略（规范名「形参 / 实参」里含「参数」）
                if is_part_of_a_term_name(alias, term_names):
                    continue
                # 这条术语自己声明「这个词另有含义、不检查」→ 跳过
                # （例如「参数」：术语表自己就要求正文解释「为什么不能只说参数」）
                if alias in skip:
                    continue
                # 判据：只有「加粗/加引号地把别名当术语给出」才算错
                for m in as_term_hits(body, alias):
                    ctx = context(body, m.start(), m.end())
                    if has_contrast_before(body, m.start()):
                        # 作者在讲「别人这么叫、我们那么叫」——这是必要的对比教学，不算错
                        notes.append((path, alias, term, '正文（对比说明）', ctx))
                    else:
                        errors.append((path, alias, term, '正文', ctx))
                # 代码块里的写法另记，只提示：代码里出现某个词往往是被注释引用的原文
                for m in as_term_hits(fenced, alias):
                    ctx = context(fenced, m.start(), m.end())
                    notes.append((path, alias, term, '代码块', ctx))

    def show(rows, tag):
        for path, alias, term, where, ctx in rows:
            print(f'  [{tag}] {os.path.basename(path)}：用了「{alias}」，'
                  f'术语表规定用「{term}」（{where}）')
            print(f'        …{ctx}…')

    if errors:
        print(f'\n需要改（{len(errors)} 处）：'
              '正文里把术语表明令避免的别名当成术语给出（加粗或加引号），读者会对不上号')
        show(errors, '错')
    if notes:
        print(f'\n提示（{len(notes)} 处，不算错）：或是「别人这么叫、我们那么叫」的对比说明，或是代码块里被引用的原文')
        show(notes[:8], '提示')
        if len(notes) > 8:
            print(f'  …其余 {len(notes) - 8} 处略')

    if errors:
        return 1
    print('\n用词检查通过：正文里没有把术语表避免的别名当成术语用')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
