# LaTeX 版式与模板要求

组内稿子统一 IEEEtran 双栏。本文件是**能直接照抄的骨架 + 踩过的坑**，避免重复调试。

## 一、文档骨架

```latex
\documentclass[journal]{IEEEtran}          % 早期访问稿（需奇偶页镜像页眉）加 twoside
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{bm}
% 需要复刻早期访问版式时再加：eso-pic, atbegshi

\begin{document}
\title{...}
\author{...}
\markboth{IEEE TRANSACTIONS ON XXX}{AUTHOR et al.: SHORT TITLE}
\maketitle
\begin{abstract}...\end{abstract}
\begin{IEEEkeywords}...\end{IEEEkeywords}
\input{sec_intro}
...
\input{refs}
\end{document}
```

**要点**
- `twoside` 只在需要**奇偶页页眉镜像**时加（IEEE 正式版/早期访问版都是镜像的）；单面打印稿不加。
- 章节拆分：`sec_intro.tex`、`sec_problem.tex`、`sec_<方法>.tex`、`sec_sim.tex`、`sec_conclusion.tex`、`refs.tex`，用 `\input{}` 引入（不带 `.tex` 后缀）。

## 二、标题与作者块

```latex
\title{Event-Triggered Data-Driven Security Formation Control for Quadrotors
Under Denial-of-Service Attacks and Communication Faults}

\author{Ziming~Ren,
        Hao~Liu,~\IEEEmembership{Senior Member, IEEE},
        Guanghui~Wen,~\IEEEmembership{Senior Member, IEEE},
        and~Jinhu~L\"{u},~\IEEEmembership{Fellow, IEEE}%
\thanks{Received 30 June 2024; revised 3 September 2024; accepted 21 September 2024.
This work was supported in part by the National Natural Science Foundation of China
under Grant 62273015 and Grant U23B2032. This article was recommended by Associate
Editor K. Zhang. (\textit{Corresponding author: Hao Liu.})}%
\thanks{Ziming Ren is with the School of Astronautics, Beihang University, Beijing
100191, China (e-mail: renziming@buaa.edu.cn).}%
% ... 每位作者一条 \thanks ...
\thanks{Digital Object Identifier 10.1109/TCYB.2024.3467178}}
```

**规则**
1. 姓名用 `~` 连接（`Hao~Liu`），防止断行拆名。
2. 会士等级用 `\IEEEmembership{Senior Member, IEEE}`，**会员等级放在逗号后**。
3. `\thanks` 在 IEEEtran journal 模式下是**不编号脚注**，第一条通常是「收稿/修回/录用 + 基金 + 推荐编辑 + 通讯作者」。
4. 每位作者一条 `\thanks`，格式 `X is with the <单位>, <城市> <邮编>, <国家> (e-mail: ...).`；双单位用 `and also with`。
5. 通讯作者标注：`(\textit{Corresponding author: Hao Liu.})`。
6. 最后两条：`Color versions ...` 与 `Digital Object Identifier 10.1109/...`（早期访问稿有）。
7. 上标符号用 `\thanks` 自动生成，不要手工写 `\footnotemark`。

## 三、摘要与关键词

```latex
\begin{abstract}
In this article, the security formation control problem is investigated for ... .
A security formation control method is proposed, including ... . The stability of the
constructed closed-loop control system is proven, and sufficient conditions are
established for ... . Simulation results demonstrate the advantages of the proposed
security control method.
\end{abstract}

\begin{IEEEkeywords}
Denial-of-service (DoS) attacks, formation control, multiagent system (MAS),
quadrotors, reinforcement learning (RL).
\end{IEEEkeywords}
```

**摘要的四句结构**（组内高度一致）
1. `In this article, the <问题> is investigated for <对象>, subject to <难点>.`
2. `A <方法> is proposed, including <组成 1> and <组成 2>.`
3. `The <性质> is proven, and sufficient conditions are established for <条件>.`
4. `Simulation results demonstrate the advantages of the proposed <方法>.`

**规则**
- 150–250 词，**不分段**，不用 `\cite`，不出现公式编号。
- 关键词 4–6 个，按字母序（IEEE 要求），逗号分隔，末尾句号。
- 摘要里首次出现的缩写要在摘要内定义（`denial-of-service (DoS)`）。

## 四、章节标题

- 源码写**普通大小写**：`\section{Simulation Results}`，IEEEtran 自动转成小型大写。
- 命名沿用组内惯例：`Introduction` / `Preliminaries and Problem Formulation` / `<X> Design` / `Simulation Results` / `Conclusion`（详见 `00-style-fingerprint.md` 第五节）。
- `\label{sec:xxx}` 放在 `\section{}` 之后；引用用 `Section~\ref{sec:xxx}`。

## 五、图

```latex
\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{figures/fig001_p02}
\caption{A one-versus-one reach-avoid game in $\mathbb{R}^2$. The pursuer strives to
capture the evader before the evader enters the target line.}
\label{fig:1}
\end{figure}
```

**规则**
1. 位置参数优先 `[!t]`（顶部），必要时 `[!b]`；**不要用 `[h]`**（IEEE 排版会挤乱）。
2. 单栏图 `width=\columnwidth`；跨栏图用 `figure*` 环境 + `width=\textwidth`。
3. 图片格式优先 **PDF（矢量）**；照片用 PNG/JPG；`\includegraphics` 不带扩展名。
4. caption **句首大写、句末句号**；先给"是什么"，再给"图里能看到什么"。
5. `\label` 放在 `\caption` **之后**。
6. 多子图：`subfigure` 或手工并排（`\includegraphics{a}\hspace{..}\includegraphics{b}`），子标 `(a)(b)` 与正文引用一致。
7. 正文引用统一 `Fig.~\ref{fig:1}`（带 `~` 防断行）；句首写 `Fig. 1`，句中写 `Fig.~\ref{}`。

## 六、表

```latex
\begin{table}[!t]
\centering
\caption{Comparison of Tracking Errors}
\label{tab:1}
\begin{tabular}{lcc}
\toprule
Method & RMSE & Time (s) \\
\midrule
Proposed & 0.012 & 3.2 \\
Existing [29] & 0.045 & 4.8 \\
\bottomrule
\end{tabular}
\end{table}
```

- 用 `booktabs`（`\toprule/\midrule/\bottomrule`），**不要竖线**。
- caption 在表**上方**，句末不加句号（IEEE 惯例：表题短语式）。
- 表内数字对齐用 `siunitx` 或手工 `r` 列。

## 七、算法框（组内做法：手工 ruled minipage）

**不要**用 `algorithm` 浮动体（会脱离原位）。用不浮动的手工框：

```latex
\noindent\begin{minipage}{\columnwidth}
\rule{\columnwidth}{0.8pt}\par\vspace{2pt}
\noindent\textbf{Algorithm 1}\quad Data-Driven Algorithm for Quadrotor Formation Control Subsystems\par
\vspace{2pt}\rule{\columnwidth}{0.4pt}\par\vspace{2pt}
\noindent\textbf{1. Initialization}\par
Apply an initial control law ...\par
\noindent\textbf{2. Policy evaluation}\par
Solve ...\par
\noindent\textbf{3. Policy improvement}\par
Let ...\par
\vspace{2pt}\rule{\columnwidth}{0.4pt}
\end{minipage}
\par\vspace{4pt}
```

- 顶线 0.8pt、标题下线与底线 0.4pt（目视与原版一致）。
- 标题行 `\textbf{Algorithm 1}` + **非粗体**描述（按原期刊版式定）。
- 三段粗体小标 + 正文。
- 框的**声明位置**决定它落在哪一栏：要它落在某页顶部，就把框声明在该页首个正文段之前。

## 八、页眉页脚（早期访问版式）

- 每页顶部 accepted-article 横幅 + 页脚 Xplore 水印可用 `eso-pic`：

```latex
\usepackage{eso-pic}
\usepackage{atbegshi}   % \AtBeginShipoutNext 需要
\newcommand{\paperfurniture}[1]{%
  \AtPageUpperLeft{\raisebox{-16pt}[0pt][0pt]{\makebox[\paperwidth][c]{\fontsize{7}{8}\selectfont <横幅文字>}}}%
  \AtPageLowerLeft{\raisebox{22pt}[0pt][0pt]{\makebox[\paperwidth][c]{\fontsize{7}{8}\selectfont <水印文字>}}}%
  #1}
\AddToShipoutPictureFG{\paperfurniture{}}     % 非星号：此后所有页
```

- 首页额外内容（版权块）只在第 1 页：用 `\AtBeginShipoutNext{\AddToShipoutPictureFG*{\paperfurniture{<版权块>}}}`。
  - **坑 1**：`\AddToShipoutPictureFG` 非星号 = 此后所有页；星号 = 仅当前页（并且是在现有内容上**追加**）。
  - **坑 2**：`\AtPageLowerLeft` 必须放在 `\AddToShipoutPictureFG{...}` **里面**，直接放在正文里会报 `You can't use \raise in vertical mode`。
  - **坑 3**：`\AtBeginShipoutNext` 来自 `atbegshi`，`eso-pic` 不自动提供。
- running head：`\markboth{期刊名}{作者 et al.: 短标题}`；IEEEtran 奇数页用 `\rightmark`、偶数页用 `\leftmark`，所以顺序是「期刊名在前、作者标题在后」。

## 九、参考文献

```latex
\begin{thebibliography}{29}
\bibitem{r1} A. Author, B. Author, and C. Author, ``Title,'' \emph{IEEE Trans. Xxx},
vol. 1, no. 2, pp. 1--10, Jan. 2024.
\end{thebibliography}
```

- 编号顺序 = 正文首次引用顺序。
- 末页栏平衡：在参考文献中插入 `\IEEEtriggeratref{<n>}`，让第 n 条落到右栏。
- 详细条目格式见 `07-citation-style.md`。

## 十、编译验收标准（每篇必查）

| 检查 | 命令/方法 | 通过标准 |
|---|---|---|
| 错误 | `grep -c '^! ' main.log` | **0** |
| 未解析引用/文献 | `grep -c 'undefined' main.log` | **0** |
| 渲染出的问号 | PDF 文字层搜 `??` | **0** |
| 超宽 | `grep 'Overfull \\hbox' main.log` | 最大 **< 20pt** |
| 页数 | 与原版一致（除特定期刊重排） | 相同 |
| 图表落位 | 逐页对比 | 同页同栏 |
| 图片缺失 | `grep 'File .* not found' main.log` | 0 |

**编译流程**：`pdflatex -interaction=nonstopmode main.tex` 连跑 **2 次**（第二遍收敛引用与目录）。

## 十一、其他实测坑

| 坑 | 现象 | 解决 |
|---|---|---|
| 行内长公式超宽 | Overfull 40–50pt | 把 `\left\{...\right\}` 改 `\{...\}`，逗号后加 `\allowbreak` |
| 简介被拉伸到页底 | 作者简介间距过大 | 用「去掉可拉伸 vskip」的 `IEEEbiography` 重定义 |
| 简介栏序不对（4 人应 2+2） | 3+1 | 在中间插 `\vfill\penalty-10000\relax` 强制分栏 |
| 浮动图跑到上一页 | 图落在正文页而非图表页 | 把 `figure` 声明移到目标页首个正文段之前 |
| 页脚装饰与正文重叠 | 版权块压住正文 | 用固定 `\raisebox` 距离（如距页底 34/43pt）定位 |
| 中文注释 | 一般无碍 | 但**不要**把中文留在正文/公式里（pdflatex 无法排版） |
| 连字符 vs 减号 | `-` 当负号 | 数学模式用 `-`（自动当负号），正文数值区间用 `--` |
