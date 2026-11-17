# 理论部分的写法：定理、证明与推导

组内理论写作是**"结论先行、条件写全、链条短促"**：定理一句话给结论+条件，证明按"构造 → 求导 → 放缩 → 得负定"推进，每步用固定连接词。

## 一、定理类环境的使用分工

| 环境 | 用途 | 语料次数 |
|---|---|---|
| `theorem` | 主结果：稳定性、收敛性、最优性、唯一性 | 21 |
| `remark` | 解释为什么这样设计、与文献的区别、边界条件 | 20 |
| `lemma` | 证明中需要的中间结论 | 10 |
| `assumption` | 建模前提（见 03-problem-formulation） | 9 |
| `corollary` | 由定理直接推出 | 6 |
| `definition` | 新概念（如"感知获胜域"） | 3 |

**不用** proposition、example。**证明统一** `\begin{IEEEproof} ... \end{IEEEproof}`（33 处 vs 手写 `\textit{Proof:}` 4 处）。

环境定义（main.tex）：

```latex
\makeatletter
\def\@begintheorem#1#2{\trivlist
   \item[\hskip\labelsep{\scshape #1\ #2}]\normalfont\ignorespaces}
\def\@endtheorem{\endtrivlist}
\makeatother
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{remark}{Remark}
```

（定理头用**小型大写**、正文正体——与 IEEE 期刊排版一致。）

## 二、定理陈述的三种句式

### 1. 「条件 + 结论」单句式（最常用）

> "The distributed observer in \eqref{eq:obs} can guarantee <性质>." — 03

### 2. 「若 ... 则 ...」式

> "**Assume that** the communication graph $G$ contains a spanning tree. The estimation error $\tilde{o}_{pi}$ **will converge to** 0 **if** $\chi$ is large enough." — 03

### 3. 「满足条件 + 稳定/收敛 + where ...」式

> "The position augmented system using the control protocol $u_{pi}^*$ in (16) **satisfies** the disturbance attenuation condition (13) **and is asymptotically stable if** $\Delta_{pi}=0$ and $\beta_i\leq 2(\|P_{mi}Q_{pi}\|)^{1/2}$, **where** $P_{mi}=B_{pi}R_{pi}^{-1}B_{pi}^T+D_{pi}D_{pi}^T/(\gamma_p^2)$." — 10

> "Considering the proposed distributed observer \eqref{eq:observer} triggered by the ST scheme \eqref{eq:strule} under switching topologies subject to communication link faults, the observation error $\tilde{\varsigma}_{oi}(t)$ of satellite $i$ converges to 0, and the Zeno-free behavior of all observers can be guaranteed." — 03

### 陈述模板（填空）

```latex
\begin{theorem}
Consider <系统/对象> \eqref{eq:sys} and <控制器/观测器> \eqref{eq:ctrl}. There exists <参数条件>
such that, if <条件 1> and <条件 2> hold, the <误差/状态> converges to <目标> and
<附加性质，如 Zeno 行为可排除> is guaranteed.
\end{theorem}
```

**规则**
1. 定理**不给证明思路**，只给条件与结论。
2. 条件要**可验证**（写成不等式或结构条件），不要写"若参数选得合适"。
3. 结论用现在时：`converges`、`is asymptotically stable`、`can be guaranteed`、`is excluded`。
4. 需要引用先前公式时用 `\eqref`。

## 三、证明的骨架

### 骨架 A：Lyapunov 稳定性（控制类论文最常用）

```latex
\begin{IEEEproof}
Consider the following Lyapunov function:
\begin{equation}
V(t) = <具体构造>
\end{equation}
Taking the time derivative of $V(t)$ along \eqref{eq:sys} yields
\begin{equation}
\dot{V}(t) \leq <经过放缩的上界>
\end{equation}
where <放缩中引入的常数>. By Young's inequality, one has <放缩步骤>. It follows that
$\dot{V}(t)\leq -\mu V(t)$ with $\mu>0$, implying that $V(t)$ converges to zero
exponentially. This completes the proof.
\end{IEEEproof}
```

原文对应：

> "Consider the following Lyapunov function as: $V_{\delta}(t) = (1-\kappa^{a}(t))V_{\delta1}(t) + \kappa^{a}(t)V_{\delta2}(t)$" — 05
> "From (3), (10), and (13), one can obtain that $\dot{V}_{\delta1}(t) \leq ...$" — 05
> "Letting $\tilde{k}_{\delta} > 0$ and using Young's inequality [9] yield ..." — 05
> "It follows that $\dot{V}_{\delta1}(t) \leq -\mu_{\delta1}V_{\delta1}(t)$ with $\mu_{\delta1} > 0$." — 05
> "From (17), it can be concluded that $\lim_{t\to\infty}\tilde{r}_{\delta i}(t) = 0$, i.e., the estimated position deviation $\hat{r}_{\delta i}(t)$ exponentially converges to $r_{\delta i}$." — 05

### 骨架 B：反证 / 构造（博弈、几何类）

> "\begin{IEEEproof} Consider any $\mathbf{x}_E \in \widetilde{\mathcal{B}}(t)$." — 01
> "\begin{IEEEproof} Fix an arbitrary time $t$ before capture." — 04

**要点**：`Fix an arbitrary ...` / `For a given ..., consider any ...` 开头，然后构造策略/路径，最后 `contradicting ...` 或 `thus the claim holds`。

### 骨架 C：唯一性 / 收敛性（迭代算法类）

> "From (43), one can obtain that ... Because it holds for any given $u_{pi}$ and $\kappa^{d}_{pi}$, $u^{n+1}_{pi} = u'_{pi}$ and $\kappa^{dn+1}_{pi} = \kappa^{d'}_{pi}$. Similarly to [28], one can conclude that $\{J^{n}_{pi}, u^{n+1}_{pi}, \kappa^{dn+1}_{pi}\}$ is the unique solution to (33), and thus converges to $\{J^{*}_{pi}, u^{*}_{pi}, \kappa^{d*}_{pi}\}$." — 05

## 四、推导衔接词（按功能选，勿重复）

| 功能 | 组内用词 | 频次 |
|---|---|---|
| 代入 | `Substituting (x) into (y) yields ...` | 12 |
| 求导 | `Taking the time derivative of $V$ along (x) yields ...` | — |
| 放缩 | `By Young's inequality, one has ...` / `one can obtain that ...` | — |
| 推出 | `It follows that ...` / `implying that ...` / `yielding ...` | 13 / — / 1 |
| 得到 | `one can obtain that ...` | **50** |
| 结论 | `Therefore, ...` / `Thus, ...` / `Hence, ...` | 56 / 26 / 10 |
| 对比情形 | `Similarly, ...` / `In contrast, ...` | 17 / 8 |
| 充分性 | `sufficient conditions are established for ...` | 9 |

**规则**
1. 一个证明里 `one can obtain that` 最多 2 次，其余换成 `yielding ...` / `it follows that`。
2. `Therefore,` / `Thus,` / `Hence,` 同一段只用一种。
3. 每步推导都要**指明来源**：`From (3) and (10), one can obtain ...`，不要出现无来源的"\(\dot V \le ...\)"。

## 五、Remark 的写法（组内高频，20 次）

**三种功能**

| 功能 | 句式 |
|---|---|
| 解释设计与动机 | `It can be observed from (1) that ...` / `It should be noted that ...` |
| 与文献对比 | `The fault model (2) can cover the DoS attacks in [26] and the communication faults in [15].` |
| 说明假设合理性 | `From the practical perspective, assumptions in (2)–(4) are common and fairly mild, and allow DoS attacks to happen aperiodically.` |

原文（05）：

> "**Remark 1:** It can be observed from (1) that the quadrotor has six degrees of freedom and only four actuators, and the dynamics cannot simply be split into the position and attitude dynamics. Furthermore, system parameters in (1) are challenging to precisely obtain because of different propeller types and payloads, and air density changes in practical applications."

> "**Remark 3:** As shown in (7)–(9), the resilient observer is designed to estimate the reference ... In (9), the relationship between triggering speed and observer performance can be adaptively adjusted based on faulting data from neighbors: the smaller $\iota_{si}(t)$ is, the more triggers there are but better performance is; the larger $\iota_{si}(t)$ is, the fewer triggers there are but worse performance is."

**规则**
1. Remark 开头用 `It can be observed/noted that` 或 `As shown in (x)`。
2. 一个 Remark 讲**一件事**（设计动机 或 对比 或 边界），不要混。
3. `the smaller ... the more ...` 这类对偶句式很适合解释权衡（tradeoff）。

## 六、常见错误

| 症状 | 问题 | 改法 |
|---|---|---|
| 定理里出现"证明见下文" | 定理应自洽 | 删掉，条件写全 |
| 条件写成"参数合适时" | 不可验证 | 写成显式不等式 |
| 证明里公式无来源 | 无法复核 | 每步标 `From (x)` |
| 一个证明里 5 次 `one can obtain` | 单调 | 换 `yielding ... / it follows that` |
| 直接给结论不写放缩 | 审稿人无法验证 | 补 Young/不等式步骤 |
| Remark 与定理重复 | 冗余 | Remark 只加"解释/对比" |
| 证明结尾没有收束 | 显得没写完 | 加 `This completes the proof.`（IEEEproof 自带 ■ 时可不写） |
