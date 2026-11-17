# Introduction 的写法

组内 Introduction 是**强模板**：六个 move 固定顺序，每个 move 有固定句型。改写时先判断「缺哪个 move」，再改句子。

## 六个 move 与对应句型

### Move 1：领域起势（1 段，3–5 句）

**功能**：说明这个方向重要、应用广、有挑战。

实测四种开头（原文）：

> **A. 应用驱动型**
> "Satellite formation flying (SFF) has received extensive attention owing to its applications for various space missions, such as Earth co-observation, communication service, and meteorological observation, as indicated in \cite{b01}." — 03

> **B. 价值判断型（最常见）**
> "Reach-avoid differential games have attracted much interest from various communities, owing to wide range of applications, including robot competition, path planning, safety verification, reachability analysis (see, \cite{ref01}-\cite{ref05})." — 04

> "Multiplayer reach-avoid games have attracted much attention due to their applications in vehicle collision avoidance, aircraft conflict resolution, and robot competitions. (see [1]-[5])." — 06

> "As A typical application of consensus/synchronization of multiagent systems, the formation control problem of quadrotors has attracted much attention from various research communities, as elaborated in \cite{r1}." — 10

> **C. 时代趋势型**
> "In recent years, unmanned aerial vehicles have emerged as versatile platforms for a wide range of autonomous ..." — 12

**可套用句式**

| 句式 | 备注 |
|---|---|
| `X have attracted much attention / much interest from various communities / extensive attention, owing to / because of its applications in A, B, and C, as indicated in \cite{...}.` | 最高频，优先用 |
| `X has received extensive attention owing to its applications for ..., such as A, B, and C, as indicated in \cite{...}.` | 单数主语时 |
| `Over the past decades, X has been widely studied for ...` | 时间状语起句，适合做"背景铺陈" |
| `In recent years, X have emerged as versatile platforms for ...` | 新兴方向 |

**细节**
- 首次出现的**缩写要就地定义**：`spacecraft formation flying (SFF)`、`multiagent systems (MASs)`、`denial-of-service (DoS)`。
- 首字下沉：双栏 IEEE 稿用 `\IEEEPARstart{M}{ultiplayer}`（06、10、12），或 `R\textsc{each-avoid}`（04 的写法）；单栏/不分栏时不用。
- 起势段末尾要**落到"难在哪"**，为 move 2 铺路：
  > "However, partial information constrains the design of effective defense strategies for the pursuer, and it is difficult to solve the equilibrium of the game and construct the winning region." — 04

### Move 2：按主题分段的文献综述（2–4 段）

**结构**：每段一个子主题，先正面综述（谁做了什么），段末用 `But,` / `However,` 点出**这一类的共同缺陷**。

段落起句固定用三个词轮换：`Recently,` / `Moreover,` / `Furthermore,`。

原文骨架（04）：

> "**Recently,** multiple researches have discussed the defense strategy for the pursuer under complete information. In \cite{ref06}, a guaranteed pursuer winning strategy was developed by solving the Hamilton-Jacob-Isaacs (HJI) equation... Based on the time derivative of an appropriately defined risk metric, a nonlinear state feedback strategy was given by \cite{ref07}... **But,** the complete state information is not always available under partial information."
>
> "**Moreover,** several works studied the defense strategy for the pursuer under partial information. In \cite{ref08}, three phases in partial information target defense games were investigated and a defense strategy was designed... **But,** the strategies developed in \cite{ref08}, \cite{ref09} did not fully analyze the changes of the winning region with varying sensing radius."
>
> "**Furthermore,** the resolution of reach-avoid games involves solving the corresponding HJI equations. In \cite{ref10}, ... **However,** the consideration of the partial information complicates the solution to the HJI equation."

**综述句的两大模板**（占 `In \cite{}` 用法的绝大多数，实测 79 次）

| 模板 | 例子 |
|---|---|
| `In \cite{x}, a <方法> was developed / proposed / designed for <问题>.` | "In \cite{ref06}, a guaranteed pursuer winning strategy was developed by solving the HJI equation." |
| `The <问题> was investigated / studied / considered in \cite{x}.` | "In \cite{ref08}, three phases ... were investigated." |
| `... was given by \cite{x}` / `... were designed based on ...` | 变体，避免连续用同一句式 |

**段末转折模板**（组内特征，实测 `But,` 27 次、`However,` 43 次）

| 模板 | 例子 |
|---|---|
| `But, the <对象> in \cite{a}, \cite{b} did not ...` | "But, the strategies developed in \cite{ref08}, \cite{ref09} did not fully analyze ..." |
| `But, <某条件> is not always available under <新场景>.` | "But, the complete state information is not always available under partial information." |
| `However, the existing works in \cite{a}, \cite{b} did not further study ...` | 05 原文 |
| `But, only linear systems were considered.` | 极短句收束，很有力 |

**要点**
- 一个 `But,` 句只点**一个**缺陷，不要罗列三个。
- 引用堆叠写法：`in \cite{a}, \cite{b}, and \cite{c}`（逐个列出）或 `(see \cite{a}-\cite{c})`（区间）；组内更常用逐个列出。
- 不要把综述写成"某某做了什么"的清单，每段必须有**评价性收尾**。

### Move 3：本文思路（1 段，`Inspired by` 开头或 `In this article,`）

原文（04）：

> "**Inspired by the aforementioned research,** a feasible defense strategy under partial information is obtained by decomposing the game into a deployment phase and a capture phase and solving the corresponding strategies. **First,** the closed-loop strategies ... are constructed based on a geometric method, and the optimality of the capture strategy is proven under exact velocity conditions. **Then,** the concepts of ... are introduced to construct the winning regions under partial information. **Furthermore,** the deployment strategy is obtained by solving a constrained optimization problem ..., and the defense strategy ... is then derived. **The main contributions are shown in the following aspects.**"

原文（05，另一变体）：

> "**In the current article,** the distributed optimal security formation control problem ... is addressed. The networks are considered subject to DoS attacks ... A distributed observer-based data-driven controller is developed ... **The main contributions include the following three aspects.**"

**句型**

| 句式 | 用途 |
|---|---|
| `Inspired by the aforementioned research, a <方法> is obtained/proposed by ...` | 说明方法来源 |
| `In this article, the <问题> is addressed/investigated.` | 直接切入 |
| `To this end, ...` / `Under the aforementioned challenging conditions, therefore, ...` | 承上启下（组内偶用） |
| `The main contributions are shown in the following aspects.` | 引出贡献（实测 9 次） |
| `The main contributions include the following three aspects.` | 明确数量（3 条最常见） |

### Move 4：贡献列表（1 段，3 条）

**两种排版**：段落式 `First, ... Second, ... Third, ...`（04、05）或 `\begin{enumerate}`（少数）。

**条目内部结构 = 「做了什么 + 为什么难/好在哪 + 对比文献」**

原文（04）：

> "**First,** the winning region under partial information and the optimal deployment positions under partial information scenarios are derived by introducing the nonsensible region and the pursuit sensing winning region. **But,** in \cite{ref08}, \cite{ref09}, the construction of the winning region under partial information was not further considered and the corresponding resulted strategies were confined to simple circular target domains in \cite{ref08} or limited escape time in \cite{ref09}. In \cite{ref22}, the area of the evasion winning region is analyzed, but the barrier was constructed through an approximate method without consideration of its hyperbolic segments."

原文（05，更紧凑的三条）：

> "1) The proposed formation controller can achieve optimal tracking performance for quadrotors under both DoS attacks and communication faults, and sufficient conditions ... are established. **But,** the graph in DoS-asleep periods was ideal and static in [8], [9], [10], and [11], ... and the above-mentioned works cannot guarantee optimal performance for MASs."
> "2) The proposed triggering method is adaptively adjusted for the tradeoff between ... **But,** the triggering schemes in [8], [15], and [17] were designed based on the undirected graph ..."
> "3) The hierarchical optimal control laws are learned without knowledge of systems dynamics ... The accurate system parameters were required in [8], [9], ... and the underactuated systems ... were not discussed in [21], ..., [25]."

**写法规则**
1. 每条**一个贡献**，开头动词固定：`The proposed <对象> can achieve ...` / `<方法> is/are proposed/designed to ...` / `The <性质> is established/proven ...`
2. 每条**必须**有对照：`But, ... in \cite{}`（组内高频）或 `Compared with \cite{}, the proposed ... avoids ...`
3. 三条的"贡献类型"要错开：**方法创新 / 性能保证 / 适用性放宽**（不要三条都说"提出了一个控制器"）。
4. 不要出现 "To the best of our knowledge, this is the first ..."（语料里 0 次）。

### Move 5：组织段（1 段，4–6 句）

原文变体（选一，全篇统一）：

> "The remaining sections in this paper are organized as follows. Section II introduces the problem description. Section III gives the closed-loop strategy in the one-versus-one game. ... In Section V, the defense strategy ... is proposed. The experimental results are given in Section VI, and conclusions are drawn in Section VII." — 04

> "The remainder of this article is organized as follows. Section II provides the preliminaries and formulates the security formation control problem ... The security formation controller is proposed in Section III. A simulation example and the results are provided in Section IV. Concluding remarks are drawn in Section V." — 05

> "The rest parts of this article are organized as follows. In Section II, the preliminaries ... are introduced. The robust formation controller is designed ... in Section III. The simulation results are shown in Section IV ..." — 10

**句型对照表**

| 起句（择一） | 分节句（交替使用） | 末句 |
|---|---|---|
| The remaining sections in this paper are organized as follows. | `Section II introduces / provides / describes / covers ...` | `... and conclusions are drawn in Section V.` |
| The remainder of this article is organized as follows. | `The <X> is proposed / constructed / designed in Section III.` | `Concluding remarks are drawn in Section V.` |
| The rest of this article is organized as follows. | `In Section IV, the <X> is derived.` | `Section V concludes this article.` |

**注意**
- 术语一致：全篇要么都用 `Section`，要么都用 `Sec.`，不要混。
- 用 `\ref{sec:xxx}` 时确保 `\label` 存在，否则会出 `??`。

## 起草用的骨架（填空即用）

```latex
\section{Introduction}
\IEEEPARstart{<首字母>}{<首词>} <领域> have/has attracted much attention from various
communities, owing to wide range of applications, including <A>, <B>, and <C>, as indicated
in \cite{<r1>}. <一两句把问题具体化：谁对谁、在什么条件下、要达成什么。> However,
<核心困难 1> and <核心困难 2>, thereby motivating this article.

Recently, <子主题 1> has been widely studied. In \cite{<r2>}, a <方法> was developed for
<问题>. <方法细节一句>. The <问题> was investigated in \cite{<r3>}, where <做法>.
But, the <共同缺陷 1>.

Moreover, several works focused on <子主题 2>. In \cite{<r4>}, ... But, the <共同缺陷 2>.

Furthermore, <子主题 3>. In \cite{<r5>}, ... However, <共同缺陷 3>.

Inspired by the aforementioned research, a <方法> is proposed for <问题> in this article.
First, ... Then, ... Furthermore, ... The main contributions are shown in the following aspects.

First, ... But, in \cite{<rx>}, ... was not considered.
Second, ... But, ... were not resilient to ...
Third, ... The accurate system parameters were required in \cite{...}, and ... were not discussed.

The remaining sections in this paper are organized as follows. Section II <introduces> ...
The <X> is proposed in Section III. Simulation results are provided in Section IV, and
conclusions are drawn in Section V.
```

## 常见错误（诊断时按此判定）

| 症状 | 说明 | 改法 |
|---|---|---|
| 综述段只有罗列、没有 `But,`/`However,` 收尾 | 读者看不出你的动机 | 每段末补一句缺陷 |
| 一段里 3 个以上 `But,` | 转折过密，显得零碎 | 只留 1 个，其余改 `However,` 或删 |
| 贡献条目不提对比文献 | 贡献显得没有参照系 | 每条补 `But, in \cite{}` |
| 贡献条目全是"提出/设计" | 贡献同质化 | 改成「方法 / 保证 / 适用性」三类 |
| 综述段里 `\cite` 堆成一片无评价 | 读着像参考文献列表 | 每个 `\cite` 后加半句评价 |
| 组织段句子全部同一句式（都用 "Section X does Y"） | 单调 | 交替 "Section X + 动词" 与 "In Section X, ..." |


## 附录 A：贡献条目的四种写法（来自个人规则版）

## Contribution-first options

1. Compact capability and comparison:

`A {method} is developed to {capability} under {condition}. In {verified references}, {limiting assumption} was required.`

2. Mechanism and guarantee before comparison:

`A {construction} is proposed for {problem}. The {mechanism} is used to {effect}, and {guarantee} is established under {conditions}. The methods in {verified references} were developed for {narrower setting}.`

3. Evidence before comparison:

`The {specific capability} is achieved using {mechanism}. The {actual validation} supports {scoped finding}. In {verified references}, {different assumption} was required.`

4. Explicit four-step option:

`A {specific result} is established for {condition}. The {mechanism} is introduced to {technical action}. In {verified references}, {specific assumption} was imposed. Under {stated conditions}, the proposed method {supported capability}.`

The fourth form expresses a current optional preference, not an invariant historical sequence. Use its final sentence only when it adds information. Vary the structure across contributions when the scientific logic warrants it.


## 附录 B：先综述后指缺口（文献段专用）

## Prior-work-first option

Use in a literature/gap paragraph:

`The {method family} has been studied for {task}. In {verified references}, {achieved result}. However, {specific restriction} was imposed. Therefore, {precise unresolved capability} is required.`

Before drafting, map each gap to a concrete contribution and actual evidence. Specify whether the distinction concerns a model factor, assumption, information condition, theorem scope or validation setting. Avoid unsupported priority claims and vague superiority. Do not import citation numbers from other manuscripts.
