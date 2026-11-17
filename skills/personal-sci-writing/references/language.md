# Context-sensitive language rules

Read the current JSON configuration. Exact lexical forms are case-insensitive, with word boundaries and flexible whitespace between phrase words. Related inflections are not automatically prohibited.

| Conflict | Reconstruction |
|---|---|
| Restrictive relative clause | A suitable `that` clause, participial construction or separate sentence |
| Nonrestrictive relative clause | Separate sentence with an explicit noun referent |
| Temporal connector conflict | An explicit interval or condition, preserving the original time scope |
| Contrast connector conflict | Separate sentences with a suitable contrast relation |
| Simultaneity conflict | Coordinate the actions or state the shared interval |
| Abbreviated restatement | Define the object directly |
| Causal phrase conflict | Use a supported causal clause or an allowed causal phrase |
| Vague association | State the actual relation, dependency or mapping |
| First person | Use a method/result subject or grammatical passive |
| Semicolon | Split complete sentences or restructure the logical relation |

Prefer meaningful academic verb-object pairs: investigate a problem, develop a method, design an observer, derive a condition, construct a region, prove convergence, learn a policy, validate a finding. These collocations are common academic language, not uniquely personal vocabulary.

Use tense according to function: enduring model definitions and deductions generally use present tense, accounts of previous studies often use past tense, and recorded experimental events can use past tense alongside present-tense figure descriptions. Conclusions can use present, present perfect or past tense coherently.

Prefer concise sentences without forcing one simple clause into every sentence. Preserve conditions and citation scope when splitting complex prose. The linter does not determine passive voice, technical equivalence or logical validity.

## 禁用词的重写策略（组内实例）

下表左列取自语料原句（含禁用形式），右列是按你的禁令改写后的可用版本。**改写靠重构，不靠同义替换**。

| 原句（含禁用形式） | 可用改写 |
|---|---|
| "Multiplayer reach-avoid games have attracted much attention **due to** their applications in vehicle collision avoidance." | "... have attracted much attention **owing to** their applications in vehicle collision avoidance." |
| "the Hamilton-Jacob-Isaacs (HJI) equation **associated with** a special subgame of degree" | "the HJI equation **derived for** a special subgame of degree" |
| "**From (17), it can be concluded that** ..., **i.e.,** the estimated position deviation exponentially converges ..." | "From (17), the estimated position deviation **converges** exponentially to $r_{\delta i}$."（直接给结论，去掉 i.e.） |
| "a simulation example of nine heterogeneous spacecrafts is presented, **in which** six spacecrafts are leaders" | "A simulation example with nine heterogeneous spacecrafts is presented. Six of them are leaders."（拆句） |
| "the dense period of triggers **corresponds to** when communication faults change violently" | "the dense period of triggers **matches** the interval in which communication faults change violently" |
| "sufficient conditions are established for the DoS attacks, **which are** related to the time-varying topology" | "sufficient conditions are established for the DoS attacks **related to** the time-varying topology"（分词） |
| "$\dot V(t)\le -\mu V(t)$ **with** $\mu>0$, **which implies that** $V(t)\to0$" | "$\dot V(t)\le -\mu V(t)$ with $\mu>0$, **implying that** $V(t)\to0$" |
| "A holds**;** B follows." | "A holds. B follows."（分号一律拆句） |

**通用重构顺序**（先试前者）：
1. 改成分词状语：`, yielding ...` / `, implying ...` / `, thereby ensuring ...`
2. 拆成两句，用 `This` / `The result` / `Therefore,` 起第二句
3. 用 `that` 从句（限定性定语）
4. 用允许的因果短语：`owing to` / `because of` / `as a result of`
5. 重写整个归属关系（`associated with` → `derived for` / `defined on`）

**不要**为了避开禁用词而牺牲精确性：宁可拆成两句，也不要换成含义漂移的动词。
