# 这是生成产物，不要手改

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
