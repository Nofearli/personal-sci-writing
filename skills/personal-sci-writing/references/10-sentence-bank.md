# 句型库（按功能分类，全部摘自组内原文）

用法：改写时**优先整句替换**成下面的句式，比重组词汇更稳。每条后标注出处（`04` = `04_tcst2026_defense_partial_info`，其余按编号类推）。

> **禁用词提醒（重要）**：本库 102 条中有 7 条含你的禁用形式（#3、#19、#72、#79、#90、#93、#97 分别涉及 due to / associated with / i.e. / which / corresponds / which）。这些是**原文证据**，只用来学结构，**不得原样搬进成稿**。套用前按下表转换：
>
> | 禁用形式 | 转换写法 | 示例（原句 → 可用句） |
> |---|---|---|
> | `which`（非限定从句） | 分词状语 / 另起一句 / `that` 从句 | "... , which yields $X$" → "... , yielding $X$" |
> | `which`（限定从句） | `that` 从句 / 分词短语 | "the condition which ensures stability" → "the condition that ensures stability" |
> | `due to` | `owing to` / `because of` / `as a result of` | "... attention due to its applications" → "... attention owing to its applications" |
> | `i.e.` | `that is` / 直接改写定义 | "..., i.e., the estimate converges" → "..., that is, the estimate converges" |
> | `associated with` | `related to` / 重写归属关系 | "the equation associated with a subgame" → "the equation derived for a subgame" |
> | `corresponds` | `matches` / `is consistent with` / `maps to` | "the period corresponds to when ..." → "the period matches the interval in which ..." |
> | `;`（分号） | 拆成两句，或改用 `and` / `thereby` | "A holds; B follows" → "A holds. B follows." |
>
> **引用形式说明**：例句按**原刊印刷形式**给出（如 `[8]`、`Figs. 1–5`）。在 `.tex` 源码中，`[8]` 对应 `\cite{r8}`，`Figs.~1--5` 对应源码里的换行写法。核对原句时以 PDF 印刷文字为准。


## 一、开篇起势

1. "Satellite formation flying (SFF) has received extensive attention owing to its applications for various space missions, such as Earth co-observation, communication service, and meteorological observation, as indicated in \cite{b01}." — 03
2. "Reach-avoid differential games have attracted much interest from various communities, owing to wide range of applications, including robot competition, path planning, safety verification, reachability analysis (see, \cite{ref01}-\cite{ref05})." — 04
3. "Multiplayer reach-avoid games have attracted much attention due to their applications in vehicle collision avoidance, aircraft conflict resolution, and robot competitions." — 06
4. "As A typical application of consensus/synchronization of multiagent systems, the formation control problem of quadrotors has attracted much attention from various research communities, as elaborated in \cite{r1}." — 10
5. "In recent years, unmanned aerial vehicles have emerged as versatile platforms for a wide range of autonomous ..." — 12
6. "Over the past decades, spacecraft formation flying (SFF) ..." — 02
7. "In recent years, quadrotor formation, as one typical application of multiagent systems (MASs), has received significant interest owing to its exceptional superiority in achieving complicated tasks, such as remote sensing, telecommunication relay, and load transportation, as illustrated in [1], [2], and [3]." — 05

## 二、把问题具体化、点出困难

8. "Consider a reach-avoid game between two adversarial players in an infinite planar domain divided into a target region and a play region: a pursuer, limited by its sensing radius, can only obtain information within its sensing range; an evader, unaffected by sensing radius, can process global information, leading the game to be conducted under partial information with a finite sensing radius." — 04
9. "However, partial information constrains the design of effective defense strategies for the pursuer, and it is difficult to solve the equilibrium of the game and construct the winning region." — 04
10. "However, the design of a security formation controller for quadrotors is challenging because of the inherent nonlinearities, couplings, and parametric uncertainties in system dynamics." — 05
11. "Thus, it is crucial to address the security formation control problem for underactuated quadrotors involving nonlinear coupled dynamics and unknown dynamical parameters under both DoS attacks and communication faults." — 05
12. "The design of ... is challenging because of ..., thereby motivating this article." — 通用模板（已按禁用词改写）

## 三、文献综述起句

13. "Recently, multiple researches have discussed the defense strategy for the pursuer under complete information." — 04
14. "Moreover, several works studied the defense strategy for the pursuer under partial information." — 04
15. "Furthermore, the resolution of reach-avoid games involves solving the corresponding HJI equations." — 04
16. "One of the typical security concerns in MASs lies in DoS attacks, destroying the transmission of interaction information over communication networks, as indicated in [7]." — 05
17. "The inner connections of MASs can be deteriorated by communication faults resulting from fading channels, unpredictable communication environmental change, and channel manipulation attacks, as elaborated in [14]." — 05
18. "Several security control approaches were investigated for MASs under uncertain communication faults, such as the $H_\infty$ control method [14], the adaptive event-triggered scheme [15], and the adaptive fault-tolerant control approach [16]." — 05

## 四、引用具体工作（三种句式，轮换使用）

19. "In \cite{ref06}, a guaranteed pursuer winning strategy was developed by solving the Hamilton-Jacob-Isaacs (HJI) equation associated with a special subgame of degree." — 04
20. "Based on the time derivative of an appropriately defined risk metric, a nonlinear state feedback strategy was given by \cite{ref07} for the multiplayer reach-avoid game." — 04
21. "In \cite{ref08}, three phases in partial information target defense games were investigated and a defense strategy was designed." — 04
22. "In [20], the optimal control problem for unknown heterogeneous MASs subject to asymmetric input constraints was studied via RL and neural networks (NNs)." — 05
23. "The data-driven controller was designed for multiple quadrotors under communication faults in [23], but the couplings in quadrotors were neglected." — 05

## 五、转折指出局限（组内特征）

24. "But, the complete state information is not always available under partial information." — 04
25. "But, the strategies developed in \cite{ref08}, \cite{ref09} did not fully analyze the changes of the winning region with varying sensing radius." — 04
26. "But, the graph in DoS-asleep periods was ideal and static in [8], [9], [10], and [11], the connectivity of the graph was unchanged in [14], [15], and [16], and the above-mentioned works cannot guarantee optimal performance for MASs." — 05
27. "But, the triggering schemes in [8], [15], and [17] were designed based on the undirected graph and the triggering methods in [4], [11], [13], and [18] were not resilient to both DoS attacks and communication faults." — 05
28. "However, the existing works in [8], [9], [10], [11], [12], and [13] did not further study uncertain communication faults in DoS-asleep periods." — 05
29. "But, only linear systems were considered." — 05（短句重锤）

## 六、本文思路

30. "Inspired by the aforementioned research, a feasible defense strategy under partial information is obtained by decomposing the game into a deployment phase and a capture phase and solving the corresponding strategies." — 04
31. "In the current article, the distributed optimal security formation control problem of a group of quadrotors under unreliable networks is addressed." — 05
32. "Under the aforementioned challenging conditions, therefore, a data-driven ST robust optimal cooperative control laws are proposed for the satellites to achieve SFF in this article." — 03

## 七、贡献引导与条目

33. "The main contributions are shown in the following aspects." — 04
34. "The main contributions include the following three aspects." — 05
35. "First, the winning region under partial information and the optimal deployment positions under partial information scenarios are derived by introducing the nonsensible region and the pursuit sensing winning region." — 04
36. "Second, the feasible defense strategy for pursuer is proposed, and the optimality is discussed for the deployment phase and the capture phase under partial information." — 04
37. "The proposed formation controller can achieve optimal tracking performance for quadrotors under both DoS attacks and communication faults, and sufficient conditions for the features of DoS attacks related to time-varying communication faults are established." — 05
38. "The hierarchical optimal control laws are learned without knowledge of systems dynamics and the effects of the rotational motion on position dynamics in the underactuated nonlinear quadrotors can be restrained." — 05

## 八、组织段

39. "The remaining sections in this paper are organized as follows. Section II introduces the problem description. Section III gives the closed-loop strategy in the one-versus-one game." — 04
40. "The remainder of this article is organized as follows. Section II provides the preliminaries and formulates the security formation control problem ... The security formation controller is proposed in Section III." — 05
41. "The rest parts of this article are organized as follows. In Section II, the preliminaries on the graph theory, the quadrotor model, and the problem formulation are introduced." — 10
42. "... and conclusions are drawn in Section V." / "Concluding remarks are drawn in Section V." — 04/05

## 九、场景与符号引入

43. "Consider a reach-avoid game with two players: one pursuer $P$ and one evader $E$." — 04
44. "The players move in the two-dimensional Euclidean space $\mathbb{R}^2$, as shown in Fig.~\ref{fig:1}." — 04
45. "The target line $\mathcal{T}$ is a line segment with endpoints $m$ and $n$ on the game space of length $\|m - n\|_2 = l$, where the symbol $\|\cdot\|_2$ represents the Euclidean norm (also called $L_2$ norm) in $\mathbb{R}^2$." — 04
46. "Let $\mathbf{x}_P(t) = (x_P(t), y_P(t))$ and $\mathbf{x}_E(t) = (x_E(t), y_E(t))$ denote the pursuer's and evader's position ($P$ and $E$) at the time $t$, respectively." — 04
47. "Let $t_c = \inf\{t > 0 \mid \mathbf{x}_E(t) \in \mathcal{S}(t)\}$ denote the first sensing time." — 01
48. "Denote $\varsigma_{oi}(t)$ as the observer state of satellite $i$ and $\{t_k^i\}$ as the triggering sequence of observer $i$." — 03
49. "Denote $\mathcal{N}_i=\{j|(v_j,v_i)\in\mathcal{E}\}$ as the neighborhood set of the node $v_i$." — 03
50. "Denote $c_{M,k}\in\mathbb{R}^{M\times1}$ as a vector with $1$ on the $k$th item and $0$s on the other items." — 02
51. "The sensing region of the pursuer $P$ is given by $\mathcal{S} = \{\mathbf{z}\in\mathbb{R}^2 \mid \|\mathbf{z} - \mathbf{x}_P\|_2 \le r\}$." — 04
52. "The dynamics of the players are described by the system for $t \ge 0$ as" — 04
53. "For simplicity, time $t$ will be omitted hereafter." — 04
54. "Note that the target line belongs to the target region $\Omega_{tar}$, but its extension line belongs to the play region $\Omega_{play}$." — 04

## 十、假设

55. "Assumption 1: The initial positions of the players under partial information are randomly generated at the beginning of the game and satisfy that $\|\mathbf{x}_P^0 - \mathbf{x}_E^0\|_2 > 0$." — 04
56. "Assumption 1 ensures that the game does not enter a terminal state at the initial time." — 04
57. "Assumption 2 ensures that the pursuer is faster than the evader and it is critical for analyzing practical pursuit scenarios since the pursuer typically requires a speed advantage to catch the evader successfully." — 04
58. "Similarly to [26], it is assumed that G without DoS attacks contains a spanning tree with the leader as its root node." — 05
59. "From the practical perspective, assumptions in (2)–(4) are common and fairly mild, and allow DoS attacks to happen aperiodically." — 05

## 十一、问题目标

60. "The objective of this article is to achieve the security formation flying for the underactuated quadrotors involving couplings, nonlinearities, and unknown system parameters, provided that the frequency and duration of DoS attacks satisfy certain conditions related to the time-varying topology affected by uncertain communication faults." — 05
61. "The game terminates when the evader is captured or reaches the target line." — 04

## 十二、定理陈述

62. "The distributed observer in \eqref{eq:obs} can guarantee ..." — 02
63. "Assume that the communication graph $G$ contains a spanning tree. The estimation error $\tilde{o}_{pi}$ will converge to 0 if $\chi$ is large enough." — 10
64. "The position augmented system using the control protocol $u_{pi}^*$ in (16) satisfies the disturbance attenuation condition (13) and is asymptotically stable if $\Delta_{pi}=0$ and $\beta_i\leq 2(\|P_{mi}Q_{pi}\|)^{1/2}$, where $P_{mi}=B_{pi}R_{pi}^{-1}B_{pi}^T+D_{pi}D_{pi}^T/(\gamma_p^2)$." — 10
65. "Considering the proposed distributed observer \eqref{eq:observer} triggered by the ST scheme \eqref{eq:strule} under switching topologies subject to communication link faults, the observation error $\tilde{\varsigma}_{oi}(t)$ of satellite $i$ converges to 0, and the Zeno-free behavior of all observers can be guaranteed." — 03

## 十三、证明

66. "Consider the following Lyapunov function as:" — 05
67. "Fix an arbitrary time $t$ before capture." — 01
68. "Consider any $\mathbf{x}_E \in \widetilde{\mathcal{B}}(t)$." — 01
69. "From (3), (10), and (13), one can obtain that" — 05
70. "Letting $\tilde{k}_{\delta} > 0$ and using Young's inequality [9] yield" — 05
71. "It follows that $\dot{V}_{\delta 1}(t)\leq-\mu_{\delta 1}V_{\delta 1}(t)$ with $\mu_{\delta 1}>0$." — 05
72. "From (17), it can be concluded that $\lim_{t\to\infty}\tilde{r}_{\delta i}(t) = 0$, i.e., the estimated position deviation $\hat{r}_{\delta i}(t)$ exponentially converges to $r_{\delta i}$." — 05
73. "Substituting (44) into (36) and (37) yields" — 05
74. "Because it holds for any given $u_{pi}$ and $\kappa^{d}_{pi}$, $u^{n+1}_{pi} = u'_{pi}$ and $\kappa^{dn+1}_{pi} = \kappa^{d'}_{pi}$." — 05

## 十四、Remark

75. "It can be observed from (1) that the quadrotor has six degrees of freedom and only four actuators, and the dynamics cannot simply be split into the position and attitude dynamics." — 05
76. "It should be noted that the fault model (2) can cover the DoS attacks in [26] and the communication faults in [15]." — 05
77. "As shown in (7)–(9), the resilient observer is designed to estimate the reference ... using faulting data at triggering times under the directed time-varying graph subject to DoS attacks and communication faults." — 05
78. "The smaller $\iota_{si}(t)$ is, the more triggers there are but better performance is; the larger $\iota_{si}(t)$ is, the fewer triggers there are but worse performance is." — 05（对偶说明 tradeoff）

## 十五、仿真节

79. "In this section, a simulation example of nine heterogeneous spacecrafts is presented, in which six spacecrafts are leaders and three spacecrafts are followers." — 02
80. "In this section, quadrotor safe navigation experiments are conducted to validate the effectiveness and generalizability of the proposed method." — 12
81. "In this section, a formation flying system consisting of one virtual leader and four following quadrotors under DoS attacks and communication faults is constructed." — 05
82. "The following quadrotors are modeled by (5) with parameters being ..." — 05
83. "The basic static graph $\mathcal{G}$ satisfies that $\rho_{13}=\rho_{21}=\rho_{31}=\rho_{43}=1$ and $\rho_{01}=\rho_{03}=1$." — 05
84. "The quadrotor initial states are set as: ..." — 05
85. "The learning parameters for Algorithm 1 are selected as $Q^q_{pi} = 15I_6$, ..." — 05

## 十六、结果解读

86. "Figs. 1–5 depict the 3-D trajectory, convergence of the NN weights, observation errors, observation gains, triggering gains, successful observation trigger instants, and tracking errors of the quadrotor formation system, respectively." — 05
87. "It can be observed from Fig. 2 that the weight matrices for the NNs converge lower to threshold $o_q$ within six iterations." — 05
88. "Figs. 1 and 5 validate the effectiveness of the proposed control method for fixed and time-varying formation tasks." — 05
89. "Fig. 4 indicates avoidance of Zeno behavior occurrence." — 05
90. "Besides, the dense period of triggers corresponds to when communication faults change violently, and when the DoS-activated period switches to the communication-faulting period, since more packets are required for performance maintenance or system recovery." — 05

## 十七、对比实验

91. "To provide comparison results, a security controller based on the resilient cooperative control method in [29] is added for the quadrotors under DoS attacks and communication faults." — 05
92. "Fig. 6 depicts the comparison results of the tracking errors of the fourth quadrotor." — 05
93. "The quadrotor shows an undesirable tracking performance using the existing method against DoS attacks, due to communication faults." — 05
94. "Therefore, one can conclude that, via the proposed security formation controller, better-tracking performance can be obtained for the networked quadrotors over the unreliable network with both DoS attacks and communication faults." — 05

## 十八、结论

95. "In this article, the security formation control problem of nonlinear coupled quadrotors is addressed by using a data-driven method." — 05
96. "A security formation controller is proposed, involving a distributed event-triggered observer to restrain the co-influences of DoS attacks and communication faults, and a hierarchical data-driven optimal controller to learn the position and attitude optimal control laws without knowledge of dynamical models." — 05
97. "The stability of the closed-loop system is proven, and sufficient conditions are established for the frequency and duration of DoS attacks, which are related to the time-varying topology affected by uncertain communication faults." — 05
98. "This paper studied a multiple-pursuer single-evader reach-avoid game under finite sensing." — 01
99. "This article proposes a robust optimal formation flying control approach for a group of satellites under the effects of nonlinear coupled relative translational dynamics, unknown system parameters, and external disturbances." — 03
100. "This paper proposes a model-free off-policy safe reinforcement learning method, termed Graph-based Lyapunov Actor-Critic, for quadrotor navigation in obstacle-cluttered environments." — 12

## 十九、展望

101. "In the future, the self-triggered security time-varying formation control problems of quadrotors will be further investigated." — 05
102. "In the future, ... will be further investigated." — 通用模板（组内惯用被动将来时）

## 使用建议

- **改写时**：先确定这句话的功能（综述/转折/结论/推导），再从对应小节挑 2–3 条句式替换。
- **不要**把不同功能的句式混搭（如用定理句式写综述）。
- **同一篇内**每种功能保留 1–2 个主用句式，其余作变体，避免整篇句式雷同。
