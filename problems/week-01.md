# Week 1 Problems: LP Geometry

## 手推题

### 1. 可行域与顶点

考虑

\[
P=\{(x_1,x_2): x_1\ge0,\ x_2\ge0,\ x_1+x_2\le 1\}.
\]

1. 画出 (P)。
2. 列出所有 vertices。
3. 对目标 (\min -2x_1-x_2)，找出最优点。
4. 指出最优点处哪些约束 active。

### 2. 无界与无最优解

分别构造一个二维 LP，使得：

1. 可行域非空但目标无界；
2. 可行域为空；
3. 可行域无界但目标仍有有限最优值。

对每个例子画图并说明原因。

### 3. 连接到研究

用自己的话写一段说明：

> 为什么 MILP 的 branch-and-bound 可以被看作把一个非凸整数可行域拆成多个 LP 可处理的凸子问题？

并补充：LP relaxation 在这个过程中提供了什么信息？

## 复习清单

- [ ] 我能区分 polyhedron、polytope、face、vertex。
- [ ] 我能从不等式识别 active constraint。
- [ ] 我能解释为什么 linear objective 与 extreme point 有关。
- [ ] 我能说出 SDP 和 MILP 从 LP 分叉的方向。
- [ ] 我运行过 `python -m experiments.lp_geometry`。

