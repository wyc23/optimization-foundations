# Optimization Foundations

一个面向实践研究者的优化基础学习仓库：从线性规划（LP）出发，逐步连接半正定规划（SDP）与混合整数线性规划（MILP）。

这个项目不是把三门课彼此孤立地罗列，而是围绕一条共同主线学习：

```text
线性代数 → 凸性与几何 → 对偶性与证书 → LP
                                      ↙   ↘
                            SDP / conic   MILP / integrality
                              ↙             ↘
                       BM / ALM / GPU   B&B / cuts / learning
```

## 学习目标

- 能从几何、代数和 primal–dual 三个角度解释 LP。
- 能从 LP 的语言理解 SDP 的 PSD cone、dual slack、互补性和证书。
- 能从 LP relaxation、整数包和 disjunction 的角度理解 MILP 求解器。
- 能把这些基础概念重新映射到 GPU SDP、BM/ALM、MILP branching/cutting 和图表示研究。

## 仓库结构

```text
.
├── README.md
├── ROADMAP.md
├── pyproject.toml
├── notes/                 # 课程笔记与推导
│   └── 01-lp-foundations.md
├── problems/              # 手推题与复习清单
│   └── week-01.md
├── experiments/           # 尽量小、可复现的数值实验
│   └── lp_geometry.py
└── journal/               # 学习日志；每次学习后记录疑问和联系
    └── README.md
```

## 快速开始

```bash
python -m experiments.lp_geometry
```

第一周建议先阅读：

1. [`ROADMAP.md`](ROADMAP.md)
2. [`notes/01-lp-foundations.md`](notes/01-lp-foundations.md)
3. [`problems/week-01.md`](problems/week-01.md)
4. 运行 [`experiments/lp_geometry.py`](experiments/lp_geometry.py)

## 学习约定

每个主题都尽量回答四个问题：

1. 它是什么？
2. 为什么需要它？
3. 数学上如何推导？
4. 它在当前的 SDP/MILP 研究中出现在哪里？

后续每次学习，我们会在仓库中加入一小块内容，并通过推导、实验或复盘把它和已有内容连接起来。

