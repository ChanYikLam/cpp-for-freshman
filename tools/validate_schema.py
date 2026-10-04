#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""最小 JSON Schema 校验器（draft-07 的子集），补引擎环境缺 `jsonschema` 的缺口。

用法：
    python3 -X utf8 -B validate_schema.py <schema.json> <data.yaml|data.json>

支持的关键字：type / required / properties / additionalProperties(false) / items /
enum / const / pattern / minimum / maximum / oneOf / format(date|date-time)。

为什么不用 `pip install jsonschema`：学习工作区的 Python 环境不该因为一次校验被改动；
这里要校验的 schema 只用到上面这些关键字，一百来行足够，且**报错带 JSON 路径**，
定位到具体是哪个节点的哪个字段，比装依赖省事。
"""

import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def type_ok(value, want):
    if want == 'object':
        return isinstance(value, dict)
    if want == 'array':
        return isinstance(value, list)
    if want == 'string':
        return isinstance(value, str)
    if want == 'number':
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if want == 'integer':
        return isinstance(value, int) and not isinstance(value, bool)
    if want == 'boolean':
        return isinstance(value, bool)
    if want == 'null':
        return value is None
    return True


DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
DATETIME_RE = re.compile(r'^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}')


def walk(node, schema, path, errors):
    """按 schema 检查 value，把问题按 `路径: 说明` 记进 errors。"""
    if 'type' in schema:
        wants = schema['type']
        wants = wants if isinstance(wants, list) else [wants]
        if not any(type_ok(node, w) for w in wants):
            errors.append(f'{path}: 类型应为 {"|".join(wants)}，实际是 {type(node).__name__}')
            return

    if 'enum' in schema and node not in schema['enum']:
        errors.append(f'{path}: 取值 {node!r} 不在允许集合 {schema["enum"]} 内')
    if 'const' in schema and node != schema['const']:
        errors.append(f'{path}: 取值应为 {schema["const"]!r}，实际 {node!r}')
    if isinstance(node, str):
        if 'pattern' in schema and not re.search(schema['pattern'], node):
            errors.append(f'{path}: {node!r} 不匹配模式 {schema["pattern"]}')
        if schema.get('format') == 'date' and not DATE_RE.match(node):
            errors.append(f'{path}: {node!r} 不是 YYYY-MM-DD 形式的日期'
                          '（YAML 里必须加引号，否则会被解析成日期对象）')
        if schema.get('format') == 'date-time' and not DATETIME_RE.match(node):
            errors.append(f'{path}: {node!r} 不是 YYYY-MM-DDTHH:MM:SS 形式的时间')
    if isinstance(node, (int, float)) and not isinstance(node, bool):
        if 'minimum' in schema and node < schema['minimum']:
            errors.append(f'{path}: {node} 小于下限 {schema["minimum"]}')
        if 'maximum' in schema and node > schema['maximum']:
            errors.append(f'{path}: {node} 大于上限 {schema["maximum"]}')

    if 'oneOf' in schema:
        matched = 0
        for sub in schema['oneOf']:
            sub_errors = []
            walk(node, sub, path, sub_errors)
            if not sub_errors:
                matched += 1
        if matched != 1:
            errors.append(f'{path}: 应恰好匹配 oneOf 中的一种结构，实际匹配 {matched} 种')

    if isinstance(node, dict):
        for key in schema.get('required', []):
            if key not in node:
                errors.append(f'{path}: 缺必填字段 `{key}`')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            for key in node:
                if key not in props:
                    allowed = '、'.join(sorted(props)) or '(无)'
                    errors.append(f'{path}: 多出未定义字段 `{key}`（schema 只允许：{allowed}）')
        for key, value in node.items():
            if key in props:
                walk(value, props[key], f'{path}.{key}', errors)
            elif isinstance(schema.get('additionalProperties'), dict):
                walk(value, schema['additionalProperties'], f'{path}.{key}', errors)

    if isinstance(node, list) and 'items' in schema:
        for i, item in enumerate(node):
            walk(item, schema['items'], f'{path}[{i}]', errors)


def load(path):
    text = open(path, encoding='utf-8').read()
    if path.endswith('.json'):
        return json.loads(text)
    if yaml is None:
        raise RuntimeError('需要 pyyaml 才能读 YAML')
    return yaml.safe_load(text)


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    schema = load(argv[1])
    data = load(argv[2])
    errors = []
    walk(data, schema, os.path.basename(argv[2]), errors)
    if errors:
        print(f'FAIL {argv[2]}：{len(errors)} 处 schema 违规')
        for e in errors:
            print(f'  {e}')
        return 1
    print(f'SCHEMA PASS  {argv[2]}  (对照 {os.path.basename(argv[1])})')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
