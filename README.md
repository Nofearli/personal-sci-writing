# personal-sci-writing

面向英文 SCI 论文的个人写作 Skill：支持起草、改写、审查和增量学习，重点处理 Abstract、Introduction 和贡献段的论证顺序。

## 功能

- 按章节加载写作规则和表达模板。
- 优先使用清晰、正式的非人称表达和语法正确的被动语态。
- 保留技术含义、公式、条件、引用和结论强度。
- 自动检查禁用词、第一人称、分号、重复开头和超长句。
- 支持 Markdown、纯文本和 LaTeX，保护常见数学、注释、引用及代码区域。

本仓库是个人 Skill 的公开整理版。私人论文全文、历史原句库、审稿材料、逐篇分析和本机路径不随仓库分发。公开模板是可适配的表达结构，不是已经证明的技术结果。此 Skill 也不代表通用期刊规范，禁词属于个人偏好。

## 安装与调用

将 `skills/personal-sci-writing` 文件夹放入你的 Codex 技能目录，保留 `SKILL.md` 的层级。之后可以在新会话中调用：

```text
$personal-sci-writing 根据以下模型、结论和实验写一版 Abstract。
$personal-sci-writing 改写这段 Introduction，保留技术含义和引用。
$personal-sci-writing 以 Review Mode 检查这份 LaTeX 文稿。
```

## 命令行检查

只需要 Python 3 标准库，无需下载模型或配置 API Key。在仓库根目录执行：

```bash
python skills/personal-sci-writing/scripts/style_lint.py manuscript.tex
python skills/personal-sci-writing/scripts/style_lint.py manuscript.md --format json
python -m unittest discover -s skills/personal-sci-writing/tests -v
```

可在 `skills/personal-sci-writing/language-rules.json` 修改禁词和建议阈值。默认硬规则不允许 `which`、`while`、`i.e.`、`namely`、`due to`、`associated with`、`corresponds`、`we/our/us` 和分号。历史引文、专有名称和数学表达需要按说明保护。

检查器不改写源文件。返回码 0 表示未发现达到失败等级的问题，1 表示发现违规，2 表示输入或配置错误。超长句和重复开头默认为建议项。

## 测试与案例

仓库包含 20 项单元测试，以及 [模拟改写案例](examples/rewrite-demo/README.md)。案例原文有 7 处硬规则违规，改写后为 0，仍保留条件和未建立捕获保证的技术边界。案例是虚构输入，没有实际仿真或理论证明。

自动检查只能验证确定性的语言规则。语态、技术正确性、引用支持和创新点质量仍需语言模型或人工复核。LaTeX 检查器是保守词法扫描器，不会展开自定义宏或自动读取 `\input` 的其他文件。

## 目录

```text
skills/personal-sci-writing/
  SKILL.md
  agents/openai.yaml
  language-rules.json
  references/
  scripts/style_lint.py
  tests/test_style_lint.py
examples/rewrite-demo/
```

详细使用与边界见 [usage.md](skills/personal-sci-writing/references/usage.md)。
