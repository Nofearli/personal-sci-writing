# 模拟摘要改写案例

这是虚构的写作测试，研究陈述仅作为测试前提，不代表已有理论证明或真实仿真结果。

任务：使用 personal-sci-writing 的 Rewriting Mode 改写 [input.txt](input.txt)，保留信息结构、策略输入和速度条件，区分感知保持与有限时间捕获，不增加技术贡献、数值或引用。

输出见 [output.txt](output.txt)。原文有 7 处硬规则违规，改写后为 0。改写保留有限感知与全局信息的差异、相对位置输入、条件性观察保持、未建立有限时间捕获、仅限测试场景的仿真证据。

在仓库根目录复核：

```bash
python skills/personal-sci-writing/scripts/style_lint.py examples/rewrite-demo/input.txt --format json --fail-on none
python skills/personal-sci-writing/scripts/style_lint.py examples/rewrite-demo/output.txt --format json
```

自动检查不证明技术结论正确。技术含义通过逐条比较测试前提与输出核对。
