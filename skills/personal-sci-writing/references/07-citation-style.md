# 引用与参考文献的写法

组内引用风格：**"引用即评价"**——每处引用都嵌在句子里，说明该文献做了什么，而不是句末挂一个 [12]。

## 一、四种引用句法（覆盖 90% 以上场景）

### 1. `In \cite{x}, ...` —— 最高频（实测 79 次）

> "**In \cite{ref06},** a guaranteed pursuer winning strategy was developed by solving the Hamilton-Jacob-Isaacs (HJI) equation associated with a special subgame of degree." — 04
> "**In \cite{ref08},** three phases in partial information target defense games were investigated and a defense strategy was designed." — 04

**结构**：`In [x], <谁> <做了什么> <用什么方法>.`

### 2. `... was developed/proposed/designed in \cite{x}` —— 被动式

> "The event-triggered guaranteed cost control method [8], the linearization-based quantized control scheme [9], the finite-time sliding mode control approach [10], and the adaptive control strategy [11]." — 05（罗列式）
> "Based on the time derivative of an appropriately defined risk metric, a nonlinear state feedback strategy **was given by \cite{ref07}** for the multiplayer reach-avoid game." — 04

### 3. `(see \cite{a}-\cite{c})` —— 区间引用

> "Reach-avoid differential games have attracted much interest from various communities, owing to wide range of applications, including robot competition, path planning, safety verification, reachability analysis **(see, \cite{ref01}-\cite{ref05})**." — 04

> "as elaborated in \cite{r1}" / "as indicated in \cite{b01}" / "as stated by Isaacs" — 05/03/04

### 4. 转折式（组内特征）：`But, in \cite{a}, \cite{b}, ... was not ...`

> "**But,** in \cite{ref08}, \cite{ref09}, the construction of the winning region under partial information was not further considered..." — 04
> "**But,** the strategies developed in \cite{ref08}, \cite{ref09} did not fully analyze the changes of the winning region with varying sensing radius." — 04
> "**But,** only linear systems were considered." — 05

**这是组内最有辨识度的引用+评价组合**：先承认文献做了什么，再指出没做什么。

## 二、引用密度与排布规则

| 规则 | 说明 |
|---|---|
| 综述段：3–6 处/段 | 每处都要有"做了什么"的谓语 |
| 方法段：0–2 处/段 | 只在借用他人结论时引用（如 `By Young's inequality [9]`） |
| 结果段：1–3 处 | 用于对比：`compared with the method in [29]` |
| 结论段：0 处 | 不引新文献 |
| 禁止 | 句末孤立 `[12]`（没有谓语或评价） |
| 禁止 | 一句话堆 5 个以上引用且无区分（应拆成两句或按类归纳） |

**堆叠引用的两种合法形态**

> 逐个列出：`in \cite{ref06}, \cite{ref07} and \cite{ref12}-\cite{ref14}, \cite{ref21}` — 04
> 按类归纳：`the event-triggered guaranteed cost control method [8], the linearization-based quantized control scheme [9], the finite-time sliding mode control approach [10], and the adaptive control strategy [11]` — 05

## 三、引用动词（按时间/贡献类型）

| 动词 | 语义 | 例子 |
|---|---|---|
| was developed | 提出方法 | "a strategy was developed in [x]" |
| was proposed | 提出方案 | "a controller was proposed for ..." |
| was investigated / studied | 研究问题 | "the problem was investigated in [x]" |
| was designed | 设计 | "two subcontrollers were designed based on ..." |
| was derived | 推导出 | "a value function was derived" |
| was established | 建立（条件/定理） | "sufficient conditions were established" |
| was given by | 给出（变体，避免重复） | "a strategy was given by [x]" |
| can be found in | 综述指向 | "a comprehensive survey can be found in [x]" |
| was applied / employed | 应用 | "the ADP algorithm was applied for ..." |

**规则**：同一段内不要连续三次用同一个动词（`was developed` ×3 是典型症状）。

## 四、文献条目格式（IEEE thebibliography）

组内统一写法（示例取自 05 的 refs.tex）：

```latex
\begin{thebibliography}{29}
\bibitem{r1} L.-X. Xu, Y.-L. Wang, X. Wang, and C. Peng, ``Distributed active disturbance
rejection formation tracking control for quadrotor UAVs,'' \emph{IEEE Trans. Cybern.},
vol. 54, no. 8, pp. 4678--4689, Aug. 2024.

\bibitem{r15} J. Sun, Z. Xu, H. Zhang, T. Chai, and S. Wang, ``Adaptive distributed control
of nonlinear multiagent systems with event-triggered for communication faults and
dead-zone inputs,'' \emph{IEEE Trans. Cybern.}, early access, Aug. 19, 2024,
doi: 10.1109/TCYB.2024.3440356.
\end{thebibliography}
```

**格式要点**

| 元素 | 规范 |
|---|---|
| 作者 | 名首字母 + 姓，`A. B. Author`；最后一位前加 `and`；IEEE 作者缩写用 `L.-X.`（带连字符的复姓） |
| 标题 | 双引号用 LaTeX `` ''（不是 " "） |
| 期刊名 | `\emph{}` 斜体，用 IEEE 官方缩写（`IEEE Trans. Cybern.`、`IEEE Trans. Autom. Control`） |
| 卷期页 | `vol. 54, no. 8, pp. 4678--4689`（页码用 en dash `--`） |
| 年月 | `Aug. 2024`（月份缩写 + 年） |
| early access | `early access, Aug. 19, 2024, doi: 10.1109/...` |
| 会议 | `in Proc. IEEE Conf. Decision Control, 2023, pp. 1--6.` |
| 书 | `Cambridge, U.K.: Cambridge Univ. Press, 2019.` |
| arXiv | `arXiv:2401.00001, 2024.` |

**编号一致性**：`\bibitem` 顺序必须与正文首次引用顺序一致；末页栏平衡用 `\IEEEtriggeratref{<n>}`。

## 五、诊断清单

| 检查项 | 判定 | 修法 |
|---|---|---|
| 是否有孤立 `[12]`（无谓语无评价） | 逐句扫 | 补 `In [12], ... was ...` 或 `... was proposed in [12]` |
| 转折是否只点一个缺陷 | 看 `But,` 句 | 一个 `But,` 句只留一个缺陷 |
| 同段三连 `was developed` | 计数 | 换 `was proposed/designed/given` |
| 引用是否按首次出现排序 | 对照 `\bibitem` | 重排或调整引用顺序 |
| early access / doi 是否完整 | 缺项 | 补 `early access, <date>, doi: ...` |
| 期刊缩写是否 IEEE 标准 | 非标准缩写 | 查 IEEE Abbreviations 列表 |
| 引用键是否与 `\bibitem` 一致 | 编译无 `??` | 修键名 |
| 是否引用自己的系列工作但没有区分 | 连续同作者 | 每处说明差异 |
