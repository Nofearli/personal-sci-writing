# 段落、语气与句长节奏

本文件回答三个问题：**一段怎么组织、句子多长、用谁的口吻说**。这是"读起来像不像我们组的稿子"的核心。

## 一、段落的四段式内部结构

组内段落几乎都是「**主题句 → 展开 → 限定/转折 → 收束**」，4–8 句，很少超过 10 句。

### 范例（04 综述段，逐句标注功能）

> "**Recently,** multiple researches have discussed the defense strategy for the pursuer under complete information. ①主题句
> **In \cite{ref06},** a guaranteed pursuer winning strategy was developed by solving the Hamilton-Jacob-Isaacs (HJI) equation associated with a special subgame of degree. ②具体工作 1
> **Based on the time derivative of an appropriately defined risk metric,** a nonlinear state feedback strategy was given by \cite{ref07} for the multiplayer reach-avoid game. ③具体工作 2
> **In \cite{ref06}, \cite{ref07} and \cite{ref12}-\cite{ref14}, \cite{ref21},** the defense strategies were designed based on complete state information and formulated in closed-loop form. ④归纳共性
> **But,** the complete state information is not always available under partial information. ⑤局限（转折）"

**规则**
1. **主题句必带时间/范围状语**：`Recently,` / `In recent years,` / `To date,` / `In the framework of ...`。
2. 中间 2–3 句给"谁做了什么"，**每句一个工作**，句式错开（`was developed` / `was given by` / `were designed`）。
3. 第 4 句做**归纳**（把上面几个工作归成一类特性）。
4. **段末必有一句局限**，否则这段没有存在意义。
5. 段内不换主题；要换主题就分新段。

### 方法段的范例（03，说明设计动机）

> "In SFF research, satellite cooperative control is a crucial issue and has ... ①主题
> ... ②问题具体化
> **To this end,** ... ③对策"

## 二、句长节奏：中句为主，短句收束

实测基线（见 `00-style-fingerprint.md`）：平均 21 词、中位 18 词、>40 词仅 6.6%、<15 词占 30.6%。

### 节奏模式（组内最典型）

```
中句(20–28 词) → 中句(20–28 词) → 短句(8–14 词，下判断)
```

原文（05 的 Remark 3 结尾）：

> "In (9), the relationship between triggering speed and observer performance can be adaptively adjusted based on faulting data from neighbors: **the smaller $\iota_{si}(t)$ is, the more triggers there are but better performance is; the larger $\iota_{si}(t)$ is, the fewer triggers there are but worse performance is.**"

较长但**结构对称**，读起来不累——这是组内长句的正确形态：**用并列/对偶结构撑长，而不是用从句套从句**。

### 长句的正确用法

| 可长（30–45 词） | 不要长 |
|---|---|
| 并列条件：「if A, B, and C hold」 | 从句套三层 |
| 对偶说明：「the smaller X, the more Y; the larger X, the fewer Y」 | 一个句子里插入两个括号解释 |
| 定义式长句：「The ... is given by ..., where ... represents ...」 | 一个句子承载两个不同论点 |
| 系统描述：「The dynamics of ..., described by ..., are ...」 | 用 and 连接三个以上独立分句 |

### 拆句的三种手法（诊断到长句时的第一反应）

| 手法 | 示例 |
|---|---|
| 在第二个谓语处断句 + 加主语 | "..., and the controller can guarantee stability." → "..., and the controller guarantees stability. This property is ..." |
| 把条件提成独立句 | "The system is stable if A and B, implying C." → "If A and B hold, the system is stable. This implies C." |
| 用冒号引出解释 | 长句后半若是"解释前面"，改成 `...: <解释>` |

## 三、语气：无人称、被动为主

实测：第一人称 0–2.9 次/100 句，两篇为 0；被动密度 2.0–2.9 次/100 词。

### 三种"不用 we"的表达法

| 想说的 | 组内写法 | 不要写 |
|---|---|---|
| 我们提出了 | `A ... method is proposed in this article.` / `The proposed controller ...` | `We propose ...`（可少量，但别通篇） |
| 我们观察到 | `It can be observed from Fig. 3 that ...` | `We can see that ...` |
| 我们认为 | `It is reasonable to assume that ...` / 直接陈述 | `We believe ...`（语料 0 次） |
| 我们证明了 | `It is proven that ...` / `The stability ... is proven.` | `We prove ...` |

**允许的第一人称场景**：`In this article, we focus on ...`（每篇最多 1–2 次，用于交代范围）；结论段 `In the future, ... will be further investigated.`（无人称）。

### 时态规则

| 内容 | 时态 | 例子 |
|---|---|---|
| 陈述事实、模型、结论 | 现在时 | "The quadrotor has six degrees of freedom." |
| 叙述文献做了什么 | 过去时/现在完成 | "a strategy was developed in [x]" / "has been widely studied" |
| 描述本文工作 | 现在时/现在完成 | "A controller is proposed." / "sufficient conditions are established" |
| 图表展示 | 现在时 | "Fig. 3 depicts ..." / "It can be observed from Fig. 2 that ..." |

**常见错误**：整篇用过去时讲自己的方法（"we designed a controller"），与结论段现在时混用。

## 四、连接词体系（按逻辑功能）

| 功能 | 首选 | 备选 | 频次 | 注意 |
|---|---|---|---|---|
| 因果/推出 | Therefore, | Thus, / Hence, | 56 / 26 / 10 | 段内只用一种 |
| 因果从句 | Since ... | As ... / Because ... | 45 | `Since` 后接已知前提 |
| 转折（段末） | But, | However, | 27 / 43 | **But, 是组内特征**，保留但限 1 次/段 |
| 递进（综述） | Moreover, | Furthermore, / Besides, | 16 / 13 / 7 | 三段轮换，勿连用同一词 |
| 并列/类似 | Similarly, | Likewise, | 17 | 证明并列子系统时用 |
| 对比 | In contrast, | On the contrary, | 8 | 与"已有方法"对照 |
| 具体化 | Specifically, | In particular, | 8 | 抽象结论后举例 |
| 提醒 | Note that | It should be noted that | 16 | 边界条件、隐含前提 |
| 推导衔接 | It follows that | yielding / implying（分词状语） | 13 | 证明专用；禁 which |
| 步骤推进 | Then, | Next, | 56 | 方法步骤 |
| 综述起句 | Recently, | Over the past decades, | 5 | 每篇 1–2 次 |
| 转入本文 | Inspired by ... | In this article, | 3 | 每篇 1 次 |

**段落内连接词预算**（避免"连接词过密"这一常见 AI 味）：
- 每段 1–2 个句首连接词即可，其余靠内容衔接。
- 同一段不要出现两个同义连接词（`Therefore,` + `Thus,`）。

## 五、信息流：从已知到未知

组内句子的默认信息顺序：**旧信息在前（作主语），新信息在后（作谓语/宾语）**。

> 差：`A triggering function $\tau_{si,k}^c(t)$ is satisfied by the adaptive event-triggered scheme.`
> 好：`The adaptive event-triggered function $\tau_{si,k}^c(t)$ satisfies (9).`（旧信息"触发函数"作主语）

**三个可操作检查**
1. 每句主语是否是"上一句提过的东西"？不是则考虑调整语序或加过渡。
2. 句末是否是"最重要的新信息"？不是则移到句末。
3. 一句话是否只推进一个信息点？两个就拆。

## 六、改写动作库（诊断后按此执行）

| 症状 | 动作 | 效果 |
|---|---|---|
| 长句（>40 词） | 在第二个谓语/条件处拆句 | 句长回到 18–24 |
| 连续 4 个以上短句 | 合并其中两句（用 `and` 或分词结构） | 恢复节奏 |
| 段首无主题句 | 补一句"Recently, X has been widely studied." | 段落有入口 |
| 段末无评价 | 补 `But, ...` / `However, ...` | 动机浮现 |
| 全篇 `we` | 改被动或 `It can be observed` | 符合组内 |
| 连接词堆叠 | 每段删到 1–2 个 | 去掉 AI 味 |
| 同一段 `Therefore/Thus/Hence` 混用 | 统一为 `Therefore,` | 一致性 |
| 名词化过重（"the implementation of the design of ..."） | 改动词（"we design ..."→"the controller is designed"） | 更直接 |
| 逻辑跳跃（前后句无关联） | 加过渡：`To this end,` / `For this reason,` / `Based on (x),` | 可读性 |
