# 符号定义的语言 + 公式写法

这是组内稿子最"可复制"的部分：符号体系、定义句式、公式排版几乎逐篇一致。改写时优先按本文件纠偏，因为公式区域的错误最难被审稿人原谅。

## 一、符号体系（12 篇实测，统一约定）

| 类别 | 字体 | 示例 | 说明 |
|---|---|---|---|
| 集合、图、区域、空间 | `\mathcal{}` | $\mathcal{G},\mathcal{V},\mathcal{E},\mathcal{P},\mathcal{S},\mathcal{T},\mathcal{N}_i$ | 语料 **1235** 次，最高频 |
| 向量 | `\mathbf{}` | $\mathbf{x},\mathbf{u},\mathbf{z},\mathbf{p}$ | **975** 次；不用 `\vec{}` |
| 标量、时变量 | 普通斜体 | $t,\alpha,\rho_{ij},\mu$ | — |
| 斜粗体（特殊向量） | `\bm{}` | $\bm{\theta}$ 类 | **300** 次，仅在需要斜体加粗时 |
| 算子名、函数名 | `\mathrm{}` | `\mathrm{diag}`, `\mathrm{Proj}`, `\mathrm{dist}`, `\mathrm{or}` | **465** 次，不写成斜体 |
| 范数 | `\|` | $\|x\|_2$、$\|x\|_F$、$\|\cdot\|$ | **673** 次；不用 `\mid`、不用 `||` |
| 实数域 | `\mathbb{R}` | $\mathbb{R}^2,\mathbb{R}^{3\times3}$ | — |
| Kronecker 积 | `\otimes` | $A\otimes I_6$ | **111** 次 |
| 转置 | `^{T}` 或 `^{\top}` | $A^{T}$、$B^{\top}$ | **篇内统一**，不要混用 |
| 单位阵/零阵 | $I_3$、$I_N$、$0_{3\times3}$ | — | `I` 用普通斜体，不加 `\mathbf` |
| 基向量 | $c_{6,1}$、$c_{12,6}$ | — | 小写斜体 c，下标"行,列" |

### 复合下标的写法（易错）

组内写**平铺下标**，不是嵌套：

| 正确 | 错误 | 例子 |
|---|---|---|
| `m_{qi}` | `m_{q_i}` | 第 $i$ 个四旋翼的质量 |
| `\kappa^{d}_{pi}` | `\kappa^{d}_{p_i}` | 位置子系统的耦合扰动 |
| `F_{qi}`、`\tau_{qi}` | `F_{q_i}` | 外力/外力矩 |
| `X_{pi}`、`S_{p0}` | `X_{p_i}` | 增广状态/领队矩阵 |
| `t^{\delta i}_{k}` | `t^{\delta}_{i,k}` | 触发时刻（注意上标 δi 也是平铺） |

**判断依据**：q/p/Θ/δ 与 i 同字号同基线即为平铺。改写时保持与全文一致，不要"顺手改成嵌套"。

### 全 1 向量与零向量

- 全 1 向量：`1_a`、`1_N`——**不加粗**（组内如此，不要改 `\mathbf{1}`）。
- 零向量：`0_{3\times1}`；零矩阵：`0_{3\times3}`。

## 二、定义符号的语言（五类句式）

### 1. 单个符号：`Let ... denote ...`

> "Let $\mathbf{x}_P(t) = (x_P(t), y_P(t))$ and $\mathbf{x}_E(t) = (x_E(t), y_E(t))$ denote the pursuer's and evader's position ($P$ and $E$) at the time $t$, **respectively**." — 04
> "Let $t_c = \inf\{t > 0 \mid \mathbf{x}_E(t) \in \mathcal{S}(t)\}$ denote the first sensing time." — 04
> "Let $\chi(t) = \mathrm{Proj}_{\Omega_{\mathrm{tar}}}(\vartheta^*(t))$ denote the corresponding closest point in the target region." — 04

### 2. 批量符号：`Denote A as ..., and B as ...`

> "Denote $\varsigma_{oi}(t)$ as the observer state of satellite $i$ and $\{t_k^i\}$ as the triggering sequence of observer $i$." — 03
> "Denote $c_{M,k}\in\mathbb{R}^{M\times1}$ as a vector with $1$ on the $k$th item and $0$s on the other items." — 05
> "Denote $\mathcal{N}_i=\{j|(v_j,v_i)\in\mathcal{E}\}$ as the neighborhood set of the node $v_i$." — 03
> "Denote the sensing pursuer set at time $t$ by $\mathcal{P}^s(t) = \{P_i \mid \mathbf{x}_E(t) \in \mathcal{S}_i(t)\}$." — 04（`by` 变体）

### 3. 就地解释：`where the symbol ... represents ...`

> "..., on the game space of length $\|m - n\|_2 = l$, **where the symbol** $\|\cdot\|_2$ **represents** the Euclidean norm (also called $L_2$ norm) in $\mathbb{R}^2$." — 04

**用途**：只解释**唯一一次**、且不在别处再定义的基础记号（范数、距离、投影）。全篇只用 1–2 次，不要每句都 "where the symbol".

### 4. 集合定义：`... is given by $X = \{ \cdot \mid \cdot \}$`

> "The sensing region of the pursuer $P$ is given by $\mathcal{S} = \{\mathbf{z}\in\mathbb{R}^2 \mid \|\mathbf{z} - \mathbf{x}_P\|_2 \le r\}$." — 04

### 5. 满足关系：`satisfying / such that / subject to`

| 句式 | 例子 |
|---|---|
| `satisfying the constraint ...` | "satisfying the constraint $\mathbf{u}_P(t), \mathbf{u}_E(t) \in \mathcal{U} = \{\mathbf{u}\in\mathbb{R}^2 \mid \|\mathbf{u}\|_2 = 1 \ \mathrm{or} \ \mathbf{u} = 0\}$" |
| `such that ...` | "satisfy that $\alpha > 1$" / "such that $Q_aS_{p0}+S^{T}_{p0}Q_a-\mu_{p2}Q_a<0$" |
| `subject to` | "quadrotors under DoS attacks", "subject to switching topologies" |

**注意区分**：
- `satisfy that <命题>`（后面接从句）
- `satisfying <条件>`（分词短语，作定语）
- 不要写 `satisfying that`。

## 三、公式排版规则

### 3.1 环境选择

| 场景 | 写法 | 证据 |
|---|---|---|
| 单个编号公式 | `\begin{equation} ... \end{equation}` | 294 个 equation 环境 |
| 多行共用一个编号 | `equation` + `aligned`，对齐点用 `&=` | 114 次 aligned |
| 无编号行间式 | `\[ ... \]` | 少量 |
| 分段函数 | `\begin{cases}` 或 `\left\{\begin{array}{l}...\end{array}\right.` | 05 的 (8)(22)(23) |

多行示例（组内标准形态）：

```latex
\begin{equation}
\begin{aligned}
\dot{\mathbf{x}}_P(t) &= v_P\mathbf{u}_P(t),\ \ \mathbf{x}_P(0) = \mathbf{x}_P^0, \\
\dot{\mathbf{x}}_E(t) &= v_E\mathbf{u}_E(t),\ \ \mathbf{x}_E(0) = \mathbf{x}_E^0,
\end{aligned}
\end{equation}
```

### 3.2 引用公式：篇内统一（三种流派，不要混用）

实测三种写法在组内**并存**，按篇划分：

| 流派 | 用法 | 使用篇目 | 计数 |
|---|---|---|---|
| `\eqref{eq:x}` | 自动带括号，最稳 | 01、02、03、07、14 | 5+30+47+74+47 = 203 |
| 文本 `(3)` | 源码里手写编号 | 05、06、10、14 | 91+10+82+66 = 249 |
| `\ref{eq:x}` | 需手工补括号 | 04、12 | 18+7 = 25 |

**规则**
1. **判断用户原稿属于哪一流派，然后全篇沿用**——这是最重要的规则。不要把一个用 `(3)` 的稿子改成 `\eqref`（会与全文不一致、且改动面过大）。
2. 若用户**新起一篇**、没有既定风格：优先 `\eqref{}`（编号自动、不会漂移）。
3. **同一篇内混用是缺陷**：14 号同时用了 `\eqref` 47 次与文本 `(66)` 次，属于真实存在的不一致，诊断时应报出。
4. 文本式 `(3)` 的代价：增删公式后编号会错，必须人工复核；发现用户用文本式时，在交付里提示这一风险（但不强制改）。
5. 不要用 `\ref{eq:x}` 又不补括号（会输出 "eq:3" 样式或裸数字）。

### 3.3 公式后的 `where` 段

- 出现率：**35%** 的 equation 后面紧跟 `where`。
- 规则：只解释本式新符号；以 `where ... and ... , respectively.` 收口。
- 若符号较多，可分成两句：`where $A$ denotes ... . $B$ and $C$ represent ..., respectively.`

### 3.4 单位、数、量纲

| 规则 | 正确 | 错误 |
|---|---|---|
| 单位用正体、与数值间留窄空格 | `1\,\mathrm{kg}`、`0.5\,\mathrm{m}`、`\times 10^{-3}\,\mathrm{kg\cdot m^2}` | `1 kg`（斜体 kg）、`0.5m` |
| 数值与单位不可拆行 | `1~kg` 或 `1\,\mathrm{kg}` | 换行处断成 `1` / `kg` |
| 数值区间用 en dash | `139--157`、`0.2--0.5` | `139-157`（连字符） |
| 百分比直接写 | `6.6\%` | `6.6 percent` |

### 3.5 公式内的文字

- 公式里的说明词用 `\mathrm{}`：`\mathrm{diag}\{...\}`、`\mathrm{Proj}`、`\mathrm{or}`、`\mathrm{total}`。
- 需要真正文本时用 `\text{}`（语料 204 次），但**优先 `\mathrm{}`**，因为 `\text` 会继承正文字体大小。
- 下标里的多字母词：`n^{a}_{\mathrm{total}}`、`T^{a}_{\mathrm{total}}`（正体，不斜体）。

### 3.6 括号与断行（实战教训）

- `\left\{ ... \right\}` 会把整段变成一个**不可断行**的原子；如果这串公式出现在**行内**且很长，会导致 Overfull hbox。
- 行内长公式的处理顺序：
  1. 改成 `\{ ... \}`（普通括号，允许断行）；
  2. 在逗号处加 `\allowbreak`（数学模式里逗号默认不产生断点）；
  3. 仍超宽则改写成分式/提取公因子，或改为行间公式。
- 行间公式里的 `\left(\right)` 保留（会自动配大小，且行间不需要断行）。

### 3.7 矩阵与分块

```latex
S_{\Theta i}(x_{\Theta i}) =
\begin{bmatrix}
0_{3\times3} & I_3 \\
0_{3\times3} & -\tilde{J}^{-1}_{\Theta i}C(\Theta_i,\dot{\Theta}_i)
\end{bmatrix} x_{\Theta i}
```

- 分块矩阵用 `bmatrix`；只有一行一列的堆叠用 `aligned` 或 `\left[\begin{array}{c}\end{array}\right]`。
- 下标记号 `0_{3\times3}`、`0_{6\times1}` 一律写全维度。

## 四、符号命名习惯（新符号怎么起名）

| 含义 | 组内常用 | 说明 |
|---|---|---|
| 图/拓扑 | $\mathcal{G}=\{\mathcal{V},\mathcal{E},\mathcal{P}\}$ | 顶点/边/邻接矩阵 |
| 拉普拉斯 | $\mathcal{L}$、$\tilde{\mathcal{L}}(t)$ | 故障版本加 tilde |
| 状态/位置 | $\mathbf{x}_i$、$\mathbf{p}_i$ | 位置常用 p |
| 参考/期望 | $r_i$、$x^d$、$\mathbf{x}^{d}$ | 上标 d 表 desired |
| 误差 | $\tilde{x}=x-\hat{x}$ | tilde 表误差（估计误差）；$e$ 表跟踪误差 |
| 估计 | $\hat{x}$ | hat 表估计 |
| 触发时刻 | $t_k$、$t^{i}_{k}$ | 上标为智能体编号 |
| 区间 | $[a,b)$ | 半开区间明确写出 |
| 增益 | $k_1,k_2$、$\mu$、$\beta$ | 希腊字母表参数 |
| 未知/最优 | $x^{*}$ | 星号 |

**规则**：同一篇里一个字母只表示一个含义；tilde/hat/star/d 上标含义固定；新符号首次出现必须定义。

## 五、诊断清单（符号与公式）

| 检查项 | 判定 | 修法 |
|---|---|---|
| 集合是否用了花体 | `\mathcal` | 统一 |
| 向量是否用 `\mathbf` 而非 `\vec` | — | 替换 |
| 算子名是否 `\mathrm`（diag/Proj/dist/or） | — | 替换，防斜体 |
| 范数是否统一 `\|·\|` | — | 替换 `||`、`\mid` |
| 公式引用是否篇内统一（`\eqref` / 文本 `(n)` / `\ref`，三选一） | 搜三种写法 | 按原稿流派统一，不混用 |
| 多行公式是否共用一个编号 | — | `equation+aligned` |
| 复合下标是否与全文一致（平铺/嵌套） | — | 按 00-style-fingerprint 的裁定 |
| 单位是否正体、有窄空格 | — | `\,\mathrm{kg}` |
| 长行内公式是否触发 Overfull | 编译日志 | `\{ \}` + `\allowbreak` |
| 每个符号是否先定义后使用 | — | 补 `Let/Denote/where` |
| 同一字母是否一符多义 | — | 换符号 |
| 转置 `T` 与 `\top` 是否混用 | — | 篇内统一 |
