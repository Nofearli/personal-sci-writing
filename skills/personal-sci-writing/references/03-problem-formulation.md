# 问题描述与建模的写法

这一节决定审稿人对「你到没把问题讲清楚」的判断。组内写法是**四段式**：场景 → 符号 → 假设 → 目标。

## 一、场景引入（1 段）

**固定起句**：`Consider a <场景> with ...`

> "Consider a reach-avoid game with two players: one pursuer $P$ and one evader $E$." — 04
> "Consider the reach-avoid game between two adversarial teams in an infinite planar domain divided into ..." — 06

**要点**
1. 一句话交代**参与者**（几个、叫什么、用什么字母表示）。
2. 第二句交代**空间与图示**：`The players move in the two-dimensional Euclidean space $\mathbb{R}^2$, as shown in Fig.~\ref{fig:1}.`
3. 第三句开始给**几何对象**，一边给一边定义符号：
   > "The target line $\mathcal{T}$ is a line segment with endpoints $m$ and $n$ on the game space of length $\|m - n\|_2 = l$, **where the symbol** $\|\cdot\|_2$ **represents** the Euclidean norm (also called $L_2$ norm) in $\mathbb{R}^2$."
4. 用 `The affine hull of two endpoints divides the plane $\mathbb{R}^2$ into two parts, the target region $\Omega_{tar}$ and the play region $\Omega_{play}$.` 这类"剖分句"引入区域。

**场景段常用动词**：`concern / consider / consist of / divide into / be composed of / model as / be regarded as`。

> "All players are considered as massless points with simple motion, as stated by Isaacs." — 04（引用经典假设时的写法）

## 二、符号引入（与场景交织）

### 2.1 两种主流句式（择一，全篇统一）

| 句式 | 例子 | 适用 |
|---|---|---|
| `Let $x$ denote ...` | "Let $\mathbf{x}_P(t) = (x_P(t), y_P(t))$ and $\mathbf{x}_E(t) = (x_E(t), y_E(t))$ denote the pursuer's and evader's position at the time $t$, respectively." — 04 | 单个/少量符号 |
| `Denote $x$ as ...` | "Denote $c_{M,k}\in\mathbb{R}^{M\times1}$ as a vector with $1$ on the $k$th item and $0$s on the other items." — 05 | 批量给符号（3 个以上） |

### 2.2 批量符号的三种写法

> "Denote $\hat{\Xi}_I=\{\hat{E}_I^x,\hat{E}_I^y,\hat{E}_I^z\}$ as the inertial coordinate system and its origin is attached to the Earth center." — 03
> "Denote $\varsigma_{oi}(t)$ as the observer state of satellite $i$ and $\{t_k^i\}$ as the triggering sequence of observer $i$." — 03
> "Denote $\mathcal{N}_i=\{j|(v_j,v_i)\in\mathcal{E}\}$ as the neighborhood set of the node $v_i$." — 03

**规则**：`Denote A as ..., and B as ...` 一口气给 2–3 个，超过 3 个改用列表或分段。

### 2.3 集合/区域定义

固定模板：`$<\mathcal{S}> = \{<元素> \mid <条件>\}$`

> "The sensing region of the pursuer $P$ is given by $\mathcal{S} = \{\mathbf{z}\in\mathbb{R}^2 \mid \|\mathbf{z} - \mathbf{x}_P\|_2 \le r\}$." — 04
> "Therefore, the overall terminal set of the game is given by $\mathcal{T} = \mathcal{T}_E \cup \mathcal{T}_P$." — 04

**注意**：`\mid` 比 `|` 间距好看；集合用花体 `\mathcal`；元素属域写 `\in \mathbb{R}^n`。

### 2.4 系统/动力学

> "The dynamics of the players are described by the system for $t \ge 0$ as"
> ```latex
> \begin{equation}
> \begin{aligned}
> \dot{\mathbf{x}}_P(t) &= v_P\mathbf{u}_P(t),\ \ \mathbf{x}_P(0) = \mathbf{x}_P^0, \\
> \dot{\mathbf{x}}_E(t) &= v_E\mathbf{u}_E(t),\ \ \mathbf{x}_E(0) = \mathbf{x}_E^0,
> \end{aligned}
> \end{equation}
> ```
> "where $\mathbf{x}_P^0$ and $\mathbf{x}_E^0$ are the initial positions of $P$ and $E$, and $v_P$ and $v_E$ denote their speeds, respectively. The control inputs $\mathbf{u}_P(t)$ and $\mathbf{u}_E(t)$ represent their instantaneous headings, satisfying the constraint ..."

**公式引出句的三选一**（全篇交替用，不要重复）

| 句式 | 例子 |
|---|---|
| `The dynamics of ... are described by the system for $t \ge 0$ as` | 04 |
| `The <模型> can be represented as` | 05 的 "the dynamical model of the ith underactuated quadrotor can be represented as" |
| `... is given by` | "The sensing region ... is given by ..." |

**公式后的 `where` 段规则**
- 逐个解释**本式新出现的**符号，不复述前面已定义的。
- 用 `respectively` 收口并列：`$v_P$ and $v_E$ denote their speeds, respectively.`（实测 `respectively` 70 次，高频）。
- 初始条件可直接写进公式行：`\mathbf{x}_P(0) = \mathbf{x}_P^0`。

### 2.5 约定句（缩短后文）

> "Note that all players can instantly change their headings. **For simplicity, time $t$ will be omitted hereafter.**" — 04

可套用：
- `For simplicity, the time index $t$ is omitted hereafter.`
- `Hereafter, $\mathbf{x}_i$ denotes $\mathbf{x}_i(t)$ for brevity.`
- `Without loss of generality, ...`
- `Note that ...`（提醒边界条件，实测 16 次）

## 三、假设（Assumption）

**两段式**：假设本体 + 一句解释其必要性。

> "\textit{Assumption 1:} The initial positions of the players under partial information are randomly generated at the beginning of the game and satisfy that $\|\mathbf{x}_P^0 - \mathbf{x}_E^0\|_2 > 0$.
>
> Assumption 1 **ensures that** the game does not enter a terminal state at the initial time." — 04

> "\textit{Assumption 2:} The speed ratio $\alpha = v_P/v_E$ satisfies that $\alpha > 1$.
>
> Assumption 2 **ensures that** the pursuer is faster than the evader and it is critical for analyzing practical pursuit scenarios since the pursuer typically requires a speed advantage to catch the evader successfully." — 04

**规则**
1. 编号用**手工** `\textit{Assumption 1:}` 或 `\newtheorem{assumption}`（语料 9 次用环境，其余手写）——同一篇统一。
2. 每个假设后**必跟** `Assumption N ensures that ...` 或 `and it is common/fairly mild in practice`。
3. 假设的合理性要挂靠文献：`Similarly to \cite{26}, it is assumed that ...`（05 原文）、`as stated by Isaacs`（04）。
4. 不要在假设里塞结论；一条假设只给一个约束。

## 四、问题目标（收尾段）

> "The objective of this article is to achieve the security formation flying for the underactuated quadrotors involving couplings, nonlinearities, and unknown system parameters, provided that the frequency and duration of DoS attacks satisfy certain conditions related to the time-varying topology affected by uncertain communication faults." — 05

**模板**

| 句式 | 用途 |
|---|---|
| `The objective of this article is to <达成什么> for <对象>, provided that <前提条件>.` | 最标准 |
| `The problem addressed in this article is to design <控制器> such that <性质 1> and <性质 2> are satisfied under <约束>.` | 控制类 |
| `This article aims to <目标> subject to <约束>.` | 简洁版 |
| `The game terminates when <终止条件>.` | 博弈类 |

**要点**：目标段要把「**达到什么 + 在什么条件下**」都说全，且与后文定理条件对齐。

## 五、常见错误

| 症状 | 问题 | 改法 |
|---|---|---|
| 符号第一次出现就在公式里，正文没定义 | 读者要回头找 | 公式前用 `Let/Denote` 先给，或公式后 `where` 补全 |
| `where` 段把已定义的符号又解释一遍 | 冗余 | 只解释本式新符号 |
| 假设没有"为什么合理" | 审稿人会质疑 | 补 `ensures that ...` / `is mild in practice` / `similarly to \cite{}` |
| 目标段只写"设计一个控制器" | 没有可验证的指标 | 写清要保证的性质（稳定/收敛/最优/避碰） |
| `respectively` 位置错（放在句首或漏掉） | 并列对象对应不清 | 永远放在句末，且并列项数一致 |
| 同一段里 `Let` 与 `Denote` 混用到 10 次以上 | 句法单调 | 交替：`Let ... denote` 与 `Denote ... as` |
