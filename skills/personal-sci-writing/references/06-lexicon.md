# 高频词汇与搭配（组内词表）

改写时的**换词白名单**：只在语料里出现过的词与搭配里选，避免引入不协调的生僻词。

## 一、核心动词（按 10k 词归一，越高越"是我们组的词"）

| 动词 | 频次 | 必背搭配 |
|---|---|---|
| propose | 17.6 | `a <方法> is proposed for/to ...`、`the proposed controller` |
| obtain | 17.0 | `one can obtain that ...`、`the <解> is obtained by solving ...` |
| design | 15.0 | `a <控制器> is designed for ...`、`the designed observer` |
| consider | 12.9 | `Consider a ...`、`the problem is considered under ...` |
| guarantee | 12.3 | `the <方案> guarantees <性质>`、`stability is guaranteed` |
| develop | 10.1 | `a strategy was developed in [x]`、`a scheme is developed to ...` |
| show | 8.4 | `it is shown that ...`、`Fig. x shows ...`、`simulation results show that` |
| satisfy | 8.3 | `satisfying the constraint`、`the condition is satisfied` |
| require | 8.1 | `requires the knowledge of ...`、`is required to ...` |
| derive | 7.2 | `the <表达式> is derived by ...` |
| yield | 6.5 | `yielding ...`、`yielding the following`（禁 which yields） |
| construct | 6.5 | `a Lyapunov function is constructed`、`construct the winning region` |
| achieve | 6.4 | `achieve the desired formation`、`achieve optimal tracking performance` |
| converge | 5.2 | `converges to zero/equilibrium` |
| ensure | 4.7 | `ensure the boundedness of ...`、`ensuring that ...` |
| formulate | 3.1 | `the problem is formulated as ...` |
| establish | 2.8 | `sufficient conditions are established for ...` |
| investigate | 2.7 | `the <问题> is investigated in [x]` |
| demonstrate | 2.6 | `simulation results demonstrate the advantages of ...` |
| illustrate | 3.1 | `Fig. x illustrates ...` |

## 二、高频名词短语与固定表达

| 表达 | 用途 |
|---|---|
| `the proposed <X>` | 指本文方法（**不用** "our method"） |
| `the existing works in [x]` | 指文献（复数用 works） |
| `sufficient conditions` | 充分条件（**不用** "adequate conditions"） |
| `the effectiveness of the proposed <X>` | 结果段评价（实测 11 次） |
| `the advantages of the proposed <X>` | 同上，变体 |
| `the tradeoff between A and B` | 权衡 |
| `a class of <系统>` | 一类系统 |
| `under <条件>` | `under partial information`、`under DoS attacks`、`under switching topologies` |
| `subject to <约束>` | 受约束 |
| `in the presence of <干扰>` | 存在干扰时 |
| `for the case of <情形>` | 情形区分 |
| `compared with [x]` | 对比（结果段） |
| `the upper/lower bound of ...` | 界 |

## 三、组内特有的非母语习惯（默认保留）

用户口径：**这些不是错误，是组内特征，默认保留**；只在"可选优化"里提示。

| 习惯 | 原文 | 保留理由 | 可选改法 |
|---|---|---|---|
| 句首 `But,` | "But, the complete state information is not always available..." | 全组 27 次，导师稿件惯用 | `However, ...` |
| `researches`（可数） | "Recently, multiple researches have discussed..." | 组内习惯 | `studies` / `works` |
| `processes`（动词作"处理"） | "the evader processes global information" | 组内习惯 | `has access to` / `utilizes` |
| `as elaborated in` / `as indicated in` | 引用引导 | 组内固定搭配 | `as shown in` |
| `Similarly to [x],` | 与文献一致的做法 | 组内 5+ 次 | `Similar to [x],` |
| `follows eq where is` 式紧凑写法 | 公式后直接 `where ... is ...` | 组内习惯 | 补全主语 |

**判定原则**：只要在语料里出现过 ≥3 次，就算"组内可接受"；0 次才算"外来词"。

## 四、易错词对（诊断时优先抓这些）

| 易错点 | 正确 | 错误 |
|---|---|---|
| affect / effect | `affect`（动词影响）、`effect`（名词效应） | "effects the system" |
| respectively 位置 | 句末，且并列数一致 | "respectively, A and B are ..." |
| such that / so that | `such that`（使得，数学） | "so that the condition holds"（在数学语境） |
| consist of / consist in | `consist of`（由…组成） | "is consisted of" |
| compare with / compare to | `compared with`（与…比较） | "comparing to" |
| robust to / robust against | `robust to`（组内常用） | "robust for" |
| dependent on / depend on | `depends on` | "is depended on" |
| owing to / because of | 用这两个（`due to` 属禁用词） | "due to that" |
| 单复数一致 | "the open-loop phase ... was not investigated" | "the phase were not" |
| 冠词 | "the proposed controller"、"a class of systems" | 缺冠词（`controller is designed`） |

## 五、慎用/禁用词（语料 0 次，出现即视为"外来腔"）

| 禁用 | 替换 |
|---|---|
| leverage | utilize / employ / use |
| utilize（过度） | use（组内更常用简单词） |
| unveil / shed light on | reveal / show |
| a myriad of / a plethora of | various / many |
| novel（自夸） | 直接说做了什么（组内少用 novel 自评） |
| to the best of our knowledge | 语料 0 次，删除 |
| obviously / clearly（无证明时） | it can be observed / it follows |
| very / quite / rather | 删 |
| a lot of | various / many |
| In order to（高频滥用） | To |

## 六、术语一致性词表（同一概念只用一个词）

| 概念 | 选定词 | 不要混用 |
|---|---|---|
| 多智能体系统 | multiagent systems (MASs) | multi-agent system（连字符版） |
| 编队控制 | formation control | formation-control（作名词时不加连字符） |
| 拒绝服务攻击 | denial-of-service (DoS) attacks | DoS attack（单数混用） |
| 事件触发 | event-triggered | event triggered / event based |
| 自触发 | self-triggered (ST) | self triggered |
| 强化学习 | reinforcement learning (RL) | RL-based（作定语可） |
| 观测器 | observer | estimator（混用需全篇统一） |
| 一致性 | consensus | synchronization（除非确为同步问题） |
| 轨迹跟踪 | trajectory tracking | path tracking（除非确为路径） |
| 仿真结果 | simulation results | simulation studies / numerical results |

**规则**：缩写首次出现给全称 `spacecraft formation flying (SFF)`，之后只用缩写；全文不要出现"SFF (spacecraft formation flying)"这种二次定义。
