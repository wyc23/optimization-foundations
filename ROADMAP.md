# Learning Roadmap

## 总体路线

```text
Linear algebra
    ↓
Convexity, geometry, separation
    ↓
LP: primal, dual, KKT, simplex, interior point
    ↓
Conic optimization ─────────────── Integer programming
    ↓                                      ↓
SDP fundamentals                       MILP fundamentals
    ↓                                      ↓
SDP algorithms                         B&B, cuts, solver architecture
    ↓                                      ↓
BM / ALM / GPU                         learning to branch/cut
```

## 十周主线

| 周次 | 主题 | 需要形成的能力 |
|---|---|---|
| 1 | 线性代数与 LP 几何 | 解释 polyhedron、face、vertex、active constraint、BFS |
| 2 | LP 对偶性 | 从 Lagrangian 推 dual，理解 weak/strong duality 与互补松弛 |
| 3 | LP 算法 | 理解 basis、reduced cost、simplex、KKT 与 Newton system |
| 4 | 凸优化与锥优化 | 理解 cone、dual cone、separation、conic duality |
| 5 | SDP 基础 | PSD cone、Schur complement、SDP primal/dual、dual slack |
| 6 | SDP 算法 | IPM、ALM、ADMM、低秩因子化与 BM |
| 7 | 整数规划基础 | LP relaxation、integer hull、valid inequality、integrality gap |
| 8 | Branch-and-Bound | bounds、branching、fathoming、node selection |
| 9 | Cutting planes | Gomory/C-G cuts、cover cuts、disjunction、separation |
| 10 | 求解器与研究连接 | presolve、root processing、heuristics、节点 LP、学习方法 |

## 贯穿案例：Max-Cut

我们会把一个小型 Max-Cut 实例作为共同案例：

1. 从二元组合问题出发。
2. 写出 MILP formulation 和 LP relaxation。
3. 观察 branching 与 valid inequalities 如何收紧 relaxation。
4. 通过 (X = xx^T) 得到 SDP relaxation。
5. 推导 SDP dual，理解 dual slack 与最小特征值证书。
6. 再连接到 BM、ALM 和 GPU 实现。

## 与当前研究的连接

- LP dual slack → reduced cost fixing、strong branching、MILP 特征。
- Farkas/对偶证书 → SDP dual certificate 与 infeasibility certificate。
- PSD cone → BM 低秩因子化、ALM、矩阵自由算子。
- Integer hull → cut selection、cardinality branching、safe fixing。
- 小实验与统一指标 → residual、gap、运行时间、内存和可复现性。

