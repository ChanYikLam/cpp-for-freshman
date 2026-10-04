# 这个仓库里都有什么

面向第一次打开这个仓库的人（同学、助教、下一个维护者）。**只想学课的人只需要 `docs/`**，其余都是制作课程用的。

## 目录一览

```text
cpp-for-freshman/
├── docs/                  # ★ 课程正文，离线可打开的网页。学课从这里进
│   ├── index.html         #   首页：18 章目录 + 进度
│   ├── lessons/           #   每一章一个 HTML
│   ├── assets/            #   样式、脚本、字体（全部本地，无 CDN，断网也能看）
│   ├── cpp-basics/        #   科目页、术语表、资源清单、学习记录
│   └── BUILD.md           #   提醒：docs/ 是生成产物，别手改
├── lab/                   # 动手练习：留白任务 + solutions/ 参考解
├── code/                  # 全部示例代码（tools/collect_code.py 从各批次 examples/ 收拢）
├── assets/fonts/          # 中文字体子集（仿宋，随包发布；见文末「字体」一节）
├── build_site.py          # 构建①：把课程工作区打包成 docs/ 静态站点
├── make_package.py        # 构建②：打成可发微信的 zip（产出在 dist/）
├── tools/                 # 校验与构建辅助脚本（见下）
│   ├── validate_schema.py #   数据文件的 schema 校验器
│   ├── check_examples.py  #   用编译器验收课件里的每个示例
│   ├── check_glossary.py  #   用词是否与术语表一致
│   ├── check_course.py    #   每章有没有动手块、示例引用对不对得上
│   ├── collect_code.py    #   把示例代码收拢到 code/
│   └── make_briefs.py     #   从大纲算每个节点的派工说明
└── README.md
```

## 谁该看什么

| 你是谁 | 你要看的 |
|---|---|
| 来学 C++ 的同学 | 只需 `docs/index.html`；要写代码时看 `lab/` 里对应章节的目录 |
| 想改课内容的人 | README 的「给维护者」一节 + `build_site.py` 顶部的注释 |
| 想在这里找 `.learning/` 的人 | **它不随仓库发布**（见下） |

## 关于 `.learning/`：编辑用的源文件不在这个仓库里

课件的真正源头不是 HTML，而是一套「内容文件」：

```text
<课程工作区>/.learning/subjects/cpp-basics/
├── curriculum.yaml     # 18 章的大纲（节点、依赖边、课型）
├── GLOSSARY.md         # 术语表：正文用词以此为准
├── MISSION.md          # 这门课为什么教、教成什么样、不教什么
├── progress.yaml       # 编写/学习进度
├── lessons/
│   ├── <序号>-<节点id>.md        # 讲义正文（含 ::: quiz 题目位置锚点）
│   ├── <序号>-<节点id>.quiz.json # 题目（题面、选项、参考答案、判分要点）
│   └── <序号>-<节点id>.html      # ← 渲染产物，就是 docs/lessons/ 里那一份
└── reference/          # 本地教材与延伸阅读
```

流程是：**改 `.md` / `.quiz.json` → 渲染 → 打包**。HTML 全程由脚本产出，所以同一个知识点的讲法与题目永远对得上，上/下一章的链接也不会错。

`.learning/` 不发布的原因是它对学课的人没用，而里面的内容文件体积不小。**如果你想长期维护这门课**，把它单独存一份（或放进同仓库的另一个分支），否则下次只能改 HTML——那会在下次渲染时被覆盖。

## 两个构建脚本怎么用

```bash
# ① 从课程工作区打包出 docs/（自带断链自检，发出去之前必须看到「本地引用自检：全部可达」）
python3 -X utf8 -B build_site.py <课程工作区> .

# ② 打成微信可发的 zip（产出 dist/，不进 git）
python3 -X utf8 -B make_package.py .
```

`<课程工作区>` 是含 `index.html` 与 `.learning/` 的那个目录。两个脚本都**可反复运行**：`docs/` 每次整体重建，不留上一次的孤儿文件。

## 数据文件校验

`curriculum.yaml`、`subject.yaml`、`progress.yaml` 都有 JSON Schema。本机 python 环境没装 `jsonschema`，所以用仓库里这个只做 draft-07 子集的校验器补位，**报错会指出是哪个节点的哪个字段**：

```bash
python3 -X utf8 -B tools/validate_schema.py <schema.json> <数据文件>
# 例：python3 -X utf8 -B tools/validate_schema.py <root>/schemas/curriculum.schema.json <工作区>/.learning/subjects/cpp-basics/curriculum.yaml
```

不要为了跑校验去改 python 环境——这个项目刻意不依赖 `pip install`。

## 字体（重要，涉及授权与可替换性）

课程正文的中文字体是**仿宋**。这个字体**不是** macOS / Windows / 手机自带的，所以**随包带了一份子集**，
否则只有装过它的电脑能显示仿宋，学生的设备会全部回退成黑体或宋体。

### 现在的做法

| 项 | 说明 |
|---|---|
| 字体来源 | 主编者本机的 `~/Library/Fonts/仿宋_GB2312.ttf`（**版权方：长城计算机公司，1994，商标 GreatWall**） |
| 实际发布物 | `assets/fonts/fangsong-subset.woff2`，**按课程用到的 2884 个汉字取子集** |
| 体积 | 3.8 MB → 405 KB（10.4%） |
| 生效范围 | `@font-face` 用 `unicode-range` 限定在汉字与中文标点 —— **英文、数字、代码完全不受影响** |
| 缺字行为 | 字体里没有的字按栈回退（仿宋_GB2312 → 方正仿宋_GBK → STFangsong → 仿宋 → 宋体 → 衬线），**不会显示成方框** |

### ⚠️ 授权提醒（请自行确认）

长城仿宋是**商业字体**。本课程是免费发给学生自学用的教育材料，风险不高，但**「把字体文件放进压缩包分发给一群人」与「在自己电脑上用」是两件事**。
如果这套课以后要放到公开仓库或更大范围传播，建议换成**开源许可**的仿宋／宋体替代，例如：

- **Noto Serif CJK SC**（SIL OFL 1.1，可自由分发）
- **思源宋体 / Source Han Serif SC**（SIL OFL 1.1）
- **霞鹜文楷 LXGW WenKai**（SIL OFL 1.1）

换法只有两步：把字体文件放到 `assets/fonts/`，改 `tools/subset_font.py` 的 `--src`，
再改引擎的 `templates/assets/learn-theme.css` 里 `@font-face` 的 `font-family` 与字体栈首项。

### 内容改了之后

课程新增了汉字时，**重跑一次子集脚本**（缺字不会报错、只会回退成宋体，所以要主动跑）：

```bash
python3 -X utf8 -B tools/subset_font.py .
```

脚本会报告「课程汉字 N 种、子集缺 M 种」，**缺 0 种才算全课程命中仿宋**。

### 引擎侧改了什么（如需回滚）

为了让字体与字号调节对所有页面生效，改了 StudyMate 引擎的共享层（**这些文件不是 git 仓库，原文件已备份**）：

| 文件 | 改动 | 备份位置 |
|---|---|---|
| `templates/assets/learn-theme.css` | 加 `@font-face`、中文字体栈、字号缩放变量 `--learn-font-scale`、阅读条样式 | `templates/assets/.orig-backup-2026-10-04/` |
| `templates/assets/learn-reading.js` | **新增**：字号调节 + 主题开关 + 术语表版本切换与首次引导 | 新增文件，删除即可 |
| `scripts/lessonfile.py` | `SHARED_FILES` 登记 `learn-reading.js` | 同上备份目录 |

阅读条的 HTML 是**打包时注入**的（`build_site.py` 的 `inject_reading_bar`），**没有改引擎的页面模板** ——
模板有占位符契约，加自定义标记会让引擎的模板校验报错。
