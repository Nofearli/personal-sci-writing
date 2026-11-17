# personal-sci-writing

面向英文 SCI 论文的个人写作 Skill：支持诊断、改写、起草、审查与增量学习。**个人硬规则优先，课题组 IEEE 期刊风格层其次**。

## 两层规则

| 层 | 内容 | 优先级 |
|---|---|---|
| 个人硬规则 | 禁用 `which` / `while` / `i.e.` / `namely` / `due to` / `associated with` / `corresponds`、禁用分号、禁用 we/our/us、偏好被动、单句 ≤45 词 | 最高（用户明确指令，覆盖历史用量） |
| 组内风格层 | 12 篇 IEEE 期刊稿的实测基线（句长、被动密度、连接词、章节 moves、符号与公式写法、LaTeX 版式、40 项自查） | 仅在不违反硬规则时适用 |

组内基线：平均句长 21.0 词、中位 18、>40 词占 6.6%、<15 词占 30.6%、被动 2.0–2.9/100 词、句首连接词覆盖约 23%。语料中的 `which yields`、`due to its applications`、分号并句属**历史用法，不是本次许可**——命中即重构句子。

## 功能

- **诊断**：六维（结构 moves / 句长节奏 / 逻辑连接 / 术语搭配 / 符号与公式 / 引用与版式），每条给定位、原句、依据与组内参照。
- **改写**：逐段重写，输出「原句 → 改句 → 理由」三列；数学、引用、数据保持不动。
- **起草**：按章节 move 结构生成，逐句标功能；填槽必须来自用户事实。
- **自查**：40 项清单 + 个人硬规则 8 项；`style_lint.py` 自动检查确定性规则。
- **符号与公式**：符号定义五类句式、复合下标约定、`\mathcal/\mathbf/\mathrm` 体系、公式引用篇内统一、Overfull 处置。
- **版式**：IEEEtran 模板、标题作者块、图表 caption、算法框、页眉页脚、编译验收。

## 安装与调用

将 `skills/personal-sci-writing` 放入技能目录（ZCode 为 `~/.zcode/skills/`），保留 `SKILL.md` 层级。之后在新会话调用：

```text
/personal-sci-writing 按组内风格润色这段 Introduction
/personal-sci-writing 这段符号定义和公式写法有问题吗
/personal-sci-writing 用组内套路起草 Section II
```

## 命令行检查

只需 Python 3 标准库：

```bash
python skills/personal-sci-writing/scripts/style_lint.py manuscript.tex
python skills/personal-sci-writing/scripts/style_lint.py manuscript.md --format json
python -m unittest discover -s skills/personal-sci-writing/tests -v
```

禁用词与阈值在 `skills/personal-sci-writing/language-rules.json` 修改。检查器不改写源文件：返回码 0 无违规、1 有违规、2 输入或配置错误；超长句与重复开头默认只作建议。

## 目录

```text
skills/personal-sci-writing/
  SKILL.md
  agents/openai.yaml
  language-rules.json
  references/
    00-style-fingerprint.md      量化指纹（含适用条件）
    01-paragraph-voice.md        段落、句长、语气、连接词
    02-introduction.md           六个 move + 四种贡献写法
    03-problem-formulation.md    场景/符号/假设/目标
    04-theory-and-proof.md       定理三句式、证明三骨架
    05-notation-and-math.md      符号定义语言 + 公式写法
    06-lexicon.md                动词白名单、易错词、术语表
    07-citation-style.md         引用句法与 IEEE 文献格式
    08-latex-conventions.md      IEEEtran 模板与实测坑
    09-preflight-checklist.md    40 项 + 个人硬规则项
    10-sentence-bank.md          102 条原句（7 条含禁用形式，仅可学结构）
    abstract.md / sections.md / language.md / learning.md / usage.md
    style-profile.md             来源、两层优先级与边界
    phrase-bank.json             功能化模板（不含禁用形式）
  scripts/style_lint.py
  tests/test_style_lint.py
examples/rewrite-demo/
```

## 边界

自动检查只验证确定性语言规则。语态、技术正确性、引用支持与创新点质量仍需人工或 LLM 复核。LaTeX 检查器是保守词法扫描器，不展开自定义宏，不自动读取 `\input` 的其他文件。禁词属个人偏好，不代表通用期刊规范。

详细使用与边界见 [usage.md](skills/personal-sci-writing/references/usage.md)。
