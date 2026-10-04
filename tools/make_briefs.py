#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""给讲解角色准备派工清单：把大纲里每个节点的「前置节点摘要」算出来。

用法：
    python3 -X utf8 -B make_briefs.py <curriculum.yaml> [<节点id> ...]

不给节点 id 就输出全部节点。

为什么要有这一步：派讲解时，前置节点摘要必须是**从「课程大纲」算出来的**，
不能凭记忆转述（转述会漂移，而课件之间的一致性全靠这条）。这里按 `edges`/`prerequisites`
递归取「上一层已经学过什么」，加上本节点自己的 objective/problem/practice 与课型，
拼成一段可直接贴进派工 prompt 的文本。
"""

import os
import re
import sys

try:
    import yaml
except ImportError:
    print('需要 pyyaml', file=sys.stderr)
    raise SystemExit(2)


def load(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def prereqs_of(data, node_id):
    """节点的真实前置：**从 `edges` 反推**（所有 `→ node_id` 的 from）。

    注意别改读节点的 `prerequisites` 字段：那是**实验课的验收清单**（schema 要求它存在，
    但普通节点一律为空数组），不是依赖关系。这门课的真实依赖全在 `edges` 里，
    早先按 `prerequisites` 取会得到「每个概念课都没有前置」的错结论。
    """
    from_nodes = [e['from'] for e in data.get('edges', []) if e.get('to') == node_id]
    node = next((n for n in data['nodes'] if n['id'] == node_id), {})
    # 实验课额外带上它的验收清单（那些正是它的前置）
    for pid in node.get('prerequisites') or []:
        if pid not in from_nodes:
            from_nodes.append(pid)
    return from_nodes


def brief(data, node_id, depth=1, seen=None):
    """递归收集前置节点的一句话摘要。"""
    seen = seen if seen is not None else set()
    by_id = {n['id']: n for n in data['nodes']}
    out = []
    for pid in prereqs_of(data, node_id):
        if pid in seen or pid not in by_id:
            continue
        seen.add(pid)
        p = by_id[pid]
        out.append(f"- `{pid}`（{p['kind']}）{p['title']} —— {p['objective']}")
        if depth > 1:
            out.extend(brief(data, pid, depth - 1, seen))
    return out


def resolve_reference(subject_path, pointer, refs, title=''):
    """把大纲里的 reference 指针解析成 reference/ 下的真实文件名。

    大纲写的指针（如 `reference/cpp-primer-plus-6th.md`）是**建课时按语义起的名字**，
    与资料收集最终落盘的文件名（如 `reference/C++PrimerPlus-第6版-中文版-04-复合类型.md`）
    对不上。解析顺序：

    1. 文件名精确命中；
    2. **按章节号命中**——大纲的资源名里写「第 4 章」，落盘文件名里带 `-04-`，
       这是最可靠的一条（比字符串包含稳：「复合类型」这类章名可能在别处也出现）；
    3. 宽松字符串包含（去掉非字母数字后互相包含）。

    解析不出来返回 None，让派人自己看见指针并改从本地资料清单里挑——不静默丢弃。
    """
    name = os.path.basename(pointer)
    if name in refs:
        return name
    chapter = re.search(r'第\s*(\d+)\s*章', title)
    if chapter:
        num = int(chapter.group(1))
        # 只认 `-NN-` 这种**章节段**。别用「文件名里出现过这个数字」：`第6版` 里的 6 会让
        # 「第 6 章」匹到第 1 章那个文件上（真实踩到过）。
        for cand in refs:
            if re.search(rf'-0*{num}-', cand):
                return cand
        for cand in refs:
            if re.search(rf'(?:^|[^0-9])0*{num}(?:[^0-9]|$)', cand):
                return cand
    key = re.sub(r'[^0-9a-z\u4e00-\u9fff]+', '', name.lower())
    for cand in refs:
        ckey = re.sub(r'[^0-9a-z\u4e00-\u9fff]+', '', cand.lower())
        if key and (key in ckey or ckey in key):
            return cand
    return None


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    data = load(argv[1])
    subject_path = os.path.dirname(os.path.abspath(argv[1]))
    ref_dir = os.path.join(subject_path, 'reference')
    refs = sorted(n for n in os.listdir(ref_dir) if n.endswith('.md')) if os.path.isdir(ref_dir) else []

    index = {n['id']: i for i, n in enumerate(data['nodes'], 1)}
    wanted = argv[2:] or list(index)
    for nid in wanted:
        node = next(n for n in data['nodes'] if n['id'] == nid)
        pre = brief(data, nid)
        print('=' * 78)
        print(f"节点位次：{index[nid]}／{len(index)}")
        print(f"节点 id：{nid}")
        print(f"课型 kind：{node['kind']}")
        print(f"标题：{node['title']}")
        print(f"目标 objective：{node['objective']}")
        print(f"侧重 practice：{node['practice']}")
        print(f"场景钩子 problem：{node['problem']}")
        if node.get('concepts'):
            print(f"知识点：{'、'.join(node['concepts'])}")
        if node.get('pitfalls'):
            print('常见错误：')
            for p in node['pitfalls']:
                print(f"  - {p}")
        if node.get('realworld'):
            print(f"现实关联：{node['realworld']}")
        res = node.get('resources') or []
        if res:
            print('依据（本轮可用来源）：')
            for r in res:
                line = f"  - [{r.get('type')}] {r['title']}"
                if r.get('url'):
                    line += f"  → {r['url']}"
                print(line)
                ptr = r.get('reference')
                if ptr:
                    real = resolve_reference(subject_path, ptr, refs, r["title"])
                    if real:
                        print(f"      本地落盘：reference/{real}（大纲指针写的是 {ptr}）")
                    else:
                        print(f"      大纲指针 {ptr} 在 reference/ 下**找不到对应文件**，"
                              '别用这个指针，改从下面的本地资料清单里挑')
        if refs:
            print('本科目 reference/ 下已落盘的本地资料：')
            for n in refs:
                size = os.path.getsize(os.path.join(ref_dir, n)) // 1024
                print(f"  - reference/{n}  ({size} KB)")
        print('前置节点摘要：')
        print('\n'.join(pre) if pre else '  （无：这是第一课）')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
