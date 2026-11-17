---
name: personal-sci-writing
description: 按个人硬规则 + 课题组 IEEE 期刊风格诊断、改写或起草英文 SCI 稿件。Use when the user asks 个人论文美化、按组内风格润色、论文润色、论文改写、Introduction 怎么写、贡献怎么列、符号定义、公式写法、定理证明句式、IEEEtran 排版要求、投稿前自查. Combines explicit personal lexical bans with a quantitative style baseline mined from 12 IEEE journal papers; includes a deterministic style linter.
---

# Personal SCI Writing

个人硬规则优先，组内风格层其次。前者是用户明确指令，**覆盖**历史用量；后者只在不违反硬规则时适用。

## 0. 硬约束（每次调用先读 `language-rules.json`）

| 规则 | 内容 | 违反时的处理 |
|---|---|---|
| 禁用词 | `which`、`while`、`i.e.`、`namely`、`due to`、`associated with`、`corresponds`（大小写不敏感、词边界匹配，其屈折形式不自动禁用） | 按 `references/language.md` 的「禁用词的重写策略」**重构句子**，不做同义替换 |
| 禁用标点 | 分号 `;` | 拆成两句，或改 `and` / `thereby` |
| 第一人称 | `we`、`our`、`us` | 改被动，或用 `This paper` / `The proposed method` / `The results` 作主语 |
| 语态偏好 | 偏好语法被动与明确的无生命主语 | — |
| 句子长度 | 单句 ≤ 45 词 | 拆句，条件与引用范围不得丢失 |
| 重复开头 | 同一开头词连续出现 ≤ 3 次为阈值 | 属启发式，可提示不强改 |
| 保护内容 | 公式、变量、量词、假设、不等式、单位、数据、引用身份、保证强度 | 只改语言，不动数学与事实；必要/充分条件不可互换；候选策略不得升格为全局最优 |
| 引用纪律 | 每个文献对比都要有真实支撑 | 缺证据时**指出缺口**，不编造引用或新颖性声明 |

软阈值（句子长度、重复度）是编辑启发式，不是习得定律。被动语态、技术等价性、引用支撑与论证质量必须人工/LLM 复核，linter 判不了。

## 1. 两个层次与冲突处理

- **个人硬规则层**：上表。优先级最高。
- **组内风格层**：见 `references/00-style-fingerprint.md`（12 篇 IEEE 稿实测：平均句长 21.0 词、中位 18、>40 词占 6.6%、<15 词占 30.6%、被动 2.0–2.9/100 词、句首连接词覆盖约 23%）。
- **冲突判定**：语料里出现过 `which` / `due to` / `i.e.` / `associated with` / `corresponds` / 分号 —— 属于历史用法，**不是本次许可**。命中即按 `language.md` 重构。

## 2. 按任务路由

| 任务 | 读什么 |
|---|---|
| Abstract | `references/abstract.md`（问题优先 / 方法优先 / 理论+学习三种序列） |
| Introduction、文献与贡献 | `references/02-introduction.md`（六个 move + 四种贡献写法） |
| 模型与问题描述 | `references/03-problem-formulation.md` |
| 方法 / 理论 / 证明 | `references/04-theory-and-proof.md`、`references/sections.md` |
| 符号定义与公式写法 | `references/05-notation-and-math.md`（用户最关心，改之前必读） |
| 换词、术语统一 | `references/06-lexicon.md`（动词白名单、易错词对、术语表） |
| 引用句法与文献格式 | `references/07-citation-style.md` |
| 段落组织、句长、语气 | `references/01-paragraph-voice.md` |
| LaTeX 模板与版式 | `references/08-latex-conventions.md` |
| 收尾自查 | `references/09-preflight-checklist.md`（40 项 + 个人硬规则项） |
| 整句替换 | `references/10-sentence-bank.md`（102 条原句；含禁用形式的 7 条只能学结构） |
| 按功能找模板 | `references/phrase-bank.json`（problem / method / theory / results 等功能键，均不含禁用形式） |
| 禁用词重写 | `references/language.md` |
| 风格来源与边界 | `references/style-profile.md` |
| 新增授权论文后更新画像 | `references/learning.md` |
| 运行检查与受保护内容 | `references/usage.md` |

## 3. 工作流

1. **提取事实与断言边界**：先把用户给的数据、条件、贡献抽成清单；缺证据的断言先标注"待补"，不要先写成结论。
2. **诊断（默认先做，不直接改写）**：按六维过——结构 moves / 句长节奏 / 逻辑连接 / 术语搭配 / 符号与公式 / 引用与版式。每条给「定位 + 原句 + 依据 + 组内参照」。
3. **改写**：逐段重写；保持 `\cite`/`\label`/`\ref`/`\eqref` 与公式本体不变；禁用形式全部重构；给出「原句 → 改句 → 理由」三列。
4. **起草（按需）**：按对应章节的 move 结构生成，每句标功能；每个填槽必须来自用户事实，不得自创假设。
5. **跑 linter**：
   ```bash
   python <skill-dir>/scripts/style_lint.py <manuscript.tex> --format json
   ```
   先修 hard violations（禁用词/分号/第一人称/超长句），再复跑。长度与重复度只作提示。
6. **独立复检**：语态、技术含义、gap-贡献对齐、新颖性范围、引用支撑——linter 不覆盖这些。
7. **交付**：
   - 改写稿（可直接粘贴）
   - 对照表（原句 / 改句 / 理由）
   - **保留项说明**：哪些组内习惯刻意为"个人规则"让步（例如语料常用 `which yields`，成稿改为 `yielding`）
   - **可改可不改**清单（更地道但可能偏离组内读感的写法）
   - linter 结果（hard violations 必须为 0）
   - 40 项自查中的不合规项

## 4. 模式

| 模式 | 输入 | 输出 |
|---|---|---|
| Writing | 事实 + 目标章节 | 干净正文，未解决的事实依赖单列 |
| Rewriting | 已有段落/整节 | 改写稿 + 三列对照 + linter 结果 |
| Review | 已有稿件 | 定位到句的发现与建议，不改原文 |
| Learning | 新增授权论文 | 先出"变更提案"，确认后再改画像；旧证据与硬规则不动 |

## 5. 硬性禁止

1. 不创造结果、引用或新颖性声明。
2. 不把必要/充分条件互换，不把候选策略写成全局最优。
3. 不改公式、变量、量词、单位与数据。
4. 不用笼统评价代替定位（"整体不错"= 无效诊断）。
5. 不覆盖用户原文件；改写稿单独给出。
6. 不把未填槽的模板当成品交付。

## 6. 交付前 30 秒自检

- [ ] `language-rules.json` 的禁用词/分号/人称：0 命中？
- [ ] 单句 ≤45 词？拆句后条件与引用范围没丢？
- [ ] 数学、引用、数据一个没动？
- [ ] 每条诊断都有定位与依据？
- [ ] 交付里包含保留项说明与可改可不改清单？
