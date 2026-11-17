# 组内英文写作风格指纹（量化基线）

本文件是 `paper-polish` 的**判断基准**。所有「这句话不合组内风格」的判断，都要能落到这里的某个数字或某条句型上。

## 语料与统计口径

- **语料**：`~/桌面/课题组论文整理/latex_converted/` 下 12 篇 IEEE 期刊稿的 .tex 正文（01–10、12–14），**不含** Elsevier 的 `11_ast2026_robust_optimal_fixedwing`（单栏 pre-proof，行文体系不同）。
- **范围**：各篇 `main.tex` 的 `\begin{document}` 之后 + `sec_*.tex`；排除 `refs.tex`、`bios.tex` 与 `\begin{IEEEbiography}` 内容（作者简介是模板套话，会污染统计）。
- **清洗**：去掉 `%` 注释、公式环境（替换为占位符）、`\cite`/`\ref`、`\setlength` 等排版命令；按 `[.!?]` + 大写字母切句；只保留 4–120 词的句子。
- **体量**：约 78,000 词正文，3,020 个句子。

## 一句话总结

**以中等长度的主动陈述句为主干（中位 18 词），用短句收束逻辑，用句首连接词显式推进论证；极少用第一人称，靠被动语态与"it can be observed"式无人称句承担观察与结论；术语、句型和章节结构高度模板化，同一功能永远用同一句式。**

## 一、核心量化指标

| 指标 | 12 篇实测 | 建议区间（写作/改写时自查） | 偏离含义 |
|---|---|---|---|
| 平均句长 | **21.0 词** | 18–24 | >28：句子偏拖，读着累 |
| 句长中位数 | **18 词** | 16–21 | — |
| 长句占比（>40 词） | **6.6%** | ≤8% | >12%：典型的"中式长句链"，需拆 |
| 短句占比（<15 词） | **30.6%** | 25–35% | <15%：缺乏节奏，全是长句 |
| 被动语态密度 | 整篇 **2.0–2.9 / 100 词**（各篇 1.29–2.88） | 整篇 1.5–3.0；**单节可到 4.0**（引言/理论节偏高） | 过低：太口语；过高：读着绕 |
| 第一人称（we/our/I） | **0–2.9 / 100 句**，其中 2 篇为 **0** | 0–3 | >5：不符合组内习惯 |
| 句首逻辑连接词覆盖率 | 约 **23%** 的句子以连接词起句 | 20–30% | 过低：段落缺"路标" |

**结论**：不是"长句学术腔"，而是**中等句长 + 高连接词密度 + 高被动**。改写时不要把短句合并成长句（这是最常见的破坏风格动作）。

### 适用条件（重要）

- 上表阈值适用于**整篇**或**≥20 句的连续正文段**（引言、综述、结论、仿真描述）。
- **理论密集型节**（含大量公式与推导，如观测器/控制器证明节）允许偏离：短句比例可低于 25%、平均句长可到 25–28 词；此时**只看句长是否失控（>32 词）**，不要强求短句比例。
- 单段 5–10 句的样本不要硬套阈值，噪声太大。

## 二、句首连接词（句子起始位置的实测次数）

| 连接词 | 次数 | 用法定位 |
|---|---|---|
| Then | 56 | 步骤推进（"Then, the ... is obtained"） |
| Therefore, | 56 | 结论落地，最高频的收束词 |
| Since | 45 | 引出前提（"Since ... , one can obtain"） |
| However, | 43 | 转折（比 But 更书面） |
| Consider | 37 | 建模/举例开头（"Consider a ... with ..."） |
| **But,** | **27** | **组内特征**：段内转折，后接"现有工作没做到什么" |
| Thus, | 26 | 与 Therefore 同义，偏数学推导 |
| Similarly, | 17 | 并列证明/并列子系统 |
| Moreover, | 16 | 递进（新增一类问题） |
| Furthermore, | 13 | 递进（更进一步） |
| It follows that | 13 | 推导衔接 |
| Note that | 16 | 提醒前提/边界条件 |
| Hence, | 10 | 推导收束 |
| In contrast, | 8 | 对比（与"已有方法"对照） |
| Specifically, | 8 | 具体化 |
| Besides, | 7 | 补充 |
| Recently, | 5 | 文献综述段起句 |
| Inspired by ... | 3 | 转入本文方法 |

**使用规则**
1. `Therefore,` / `Thus,` / `Hence,` 三者择一，不要在同一段里混用三种表"因此"。
2. **`But,` 是组内习惯**：默认保留（用户明确要求），但每段最多 1 次；若一段里出现 2 次以上，改成 `However,` 一次 + 删一次。
3. 综述段起句用 `Recently,` / `Moreover,` / `Furthermore,` 三件套轮流，不要连着三段都用 `Moreover,`。
4. 数学推导段优先 `Since ... , it follows that ...` 与 `Substituting (x) into (y) yields ...`。

## 三、高频动词（按 10k 词归一）

| 动词 | 频次 | 典型搭配 |
|---|---|---|
| propose | 17.6 | a method/controller/algorithm **is proposed** (to/for ...) |
| obtain | 17.0 | one can **obtain** that ...; the ... is **obtained** by solving ... |
| design | 15.0 | a ... is **designed** for/to ...; the **designed** controller |
| consider | 12.9 | **Consider** a ...; the problem is **considered** under ... |
| guarantee | 12.3 | the ... **guarantees** that ...; stability is **guaranteed** |
| develop | 10.1 | a strategy **was developed** in [x] |
| show | 8.4 | it is **shown** that ...; Fig. X **shows** ... |
| satisfy | 8.3 | **satisfying** the constraint ...; the condition is **satisfied** |
| require | 8.1 | **requires** the knowledge of ... |
| derive | 7.2 | the ... **is derived** by ... |
| yield | 6.5 | `yielding the following ...`、`and yields ...`（禁用 which yields） |
| construct | 6.5 | a Lyapunov function is **constructed** |
| achieve | 6.4 | **achieve** the desired formation |
| converge | 5.2 | the error **converges** to zero |
| ensure | 4.7 | **ensure** the ... ; **ensuring** that |
| formulate | 3.1 | the problem is **formulated** as ... |
| establish | 2.8 | sufficient conditions are **established** |

**改写时优先从这张表里换词**，不要引入语料里没有的花哨动词（如 orchestrate、leverage、unveil）。

## 四、数学写作习惯（12 篇合计）

| 项目 | 计数 | 说明 |
|---|---|---|
| `\mathcal{}` 花体 | 1,235 | 集合/图/区域首选（$\mathcal{G}$、$\mathcal{V}$、$\mathcal{S}$） |
| `\mathbf{}` 粗体 | 975 | 向量（$\mathbf{x}$、$\mathbf{u}$） |
| `\|`（范数） | 673 | 统一 `\|x\|`、`\|x\|_2`、`\|x\|_F` |
| `\mathrm{}` | 465 | 算子/直立体（diag、Proj、dist、or） |
| `\bm{}` | 300 | 需要斜粗体时（$\bm{\theta}$ 类） |
| `equation` 环境 | 294 | 编号公式主用 equation |
| `\eqref{}` | 263 | **三种流派并存**：01/02/03/07/14 用 `\eqref`；05/06/10/14 用文本 `(3)`；04/12 用 `\ref{eq:}`。篇内统一即可，详见 `05-notation-and-math.md` 3.2 |
| `\text{}` | 204 | 公式内中文/说明性文字 |
| `aligned`（equation 内） | 114 | 多行共号的标准写法 |
| `\otimes` | 111 | Kronecker 积 |
| 公式后紧跟 `where` | 103 / 294（**35%**） | 约 1/3 公式用 where 从句解释符号 |

**结论**：符号体系固定为「花体=集合/图，粗体=向量，mathrm=算子名，范数用 `\|`」，公式引用用 `\eqref`，多行公式用 `equation+aligned`（共用一个编号）。

## 五、章节结构共性（12 篇）

几乎全部遵循同一骨架（命名有变体）：

| 位置 | 主流命名 | 变体（按期刊） |
|---|---|---|
| 1 | Introduction | — |
| 2 | Preliminaries and Problem Formulation | Preliminaries / Problem Formulation / Problem Description / Game Formulation / Model Description |
| 3 | <对象> Design（Controller / Protocol / Strategy / Observer Design，可多节） | Methodology / Closed-Loop Strategies |
| 4 | Simulation Results | Experimental Results / Case Studies / Case Study Results / Experimental Study / Experimental Validation |
| 5 | Conclusion | Conclusions（TAC、T-ITS 用复数，且节标题全大写） |

- TAC（01）、T-ITS（14）的 section 标题为**全大写**（IEEEtran 自动处理，源码写普通大小写即可）。
- 方法部分常拆成 2–4 节（如 07：Adaptive Velocity Observer Design / Visual Servoing Controller Design / Attitude Controller Design），**每节对应一个子系统或一个设计层次**。

## 六、定理类环境使用

| 环境 | 次数 | 用途 |
|---|---|---|
| theorem | 21 | 主结论（收敛性、稳定性、最优性） |
| remark | 20 | 解释、边界、与文献对比（几乎与定理同等高频） |
| lemma | 10 | 证明中间结论 |
| assumption | 9 | 建模前提 |
| corollary | 6 | 推论 |
| definition | 3 | 新概念定义 |

- **不用 proposition、不用 example**。
- 证明写法：`\begin{IEEEproof}`（33 处）远多于手写 `\textit{Proof:}`（4 处）→ 统一用 IEEEproof 环境。
- 定理陈述几乎都是**单句条件式**：「The <对象> can guarantee <性质> if <条件>」，或「<对象> satisfies <条件> and is <性质> if A and B, where ...」。

## 七、期刊间差异（不要当成组内铁律）

| 维度 | 差异 |
|---|---|
| 句长 | 01（TAC）、13/14（T-ASE/T-ITS）偏短（17–18 词）；02（TAES）、10（TNNLS）偏长（24–25 词），长句占比 12–15% |
| 第一人称 | 06（TMech）、09（TSMC）为 0，全篇无人称；05、14 有少量 we/our |
| 结果节命名 | 实验类期刊（12/13）用 "Case Studies"、"Experimental Validation"；理论类（01/04/06）用 "Simulation Results" / "Experimental Results" |
| 贡献段 | 04/05 用段落式 `First, ... Second, ...`；02/10 也可用 `\begin{enumerate}` |

**判断优先级**：单篇内一致性 > 全组共性 > 目标期刊惯例。同一篇稿子里不要混用两种结果节命名风格。

## 八、如何复算

若以后新增论文想更新基线，按上面的「统计口径」重算：清洗注释与公式 → 按句切分 → 统计句长/被动/第一人称/句首连接词 → 统计 `\mathcal/\mathbf/\mathrm/\eqref` 与环境计数。**阈值以本表为准**，新增 1–2 篇不必改基线，新增 ≥5 篇才重算。
