# 第 1 课：LP 是什么，以及为什么它是 SDP/MILP 的共同起点

## 1. 一个 LP 的三个组成部分

以标准形式为例：

\[
\begin{aligned}
\min_x\quad & c^T x\\
\text{s.t.}\quad & Ax=b,\\
& x\ge 0.
\end{aligned}
\]

它由三部分组成：

1. 线性目标 (c^T x)；
2. 仿射约束 (Ax=b)；
3. 一个可行性结构 (x\in\mathbb R_+^n)。

第三部分尤其重要。LP 并不只是“目标和约束都是线性的”，它还要求变量落在非负正交锥中。

## 2. 几何图像

不等式形式

\[
P=\{x\mid Ax\le b\}
\]

定义了一个 polyhedron。每一行约束对应一个 halfspace；所有 halfspace 的交就是可行域。

在二维中，目标函数的等值线平移到不能继续改进的位置。在线性目标有有限最优解时，至少存在一个最优 extreme point。这个事实是 simplex 方法和 basic feasible solution 理论的几何基础。

### 需要区分的概念

- **polyhedron**：有限个线性不等式的交，可能无界。
- **polytope**：有界的 polyhedron。
- **face**：由一个有效线性不等式取等得到的边界结构。
- **vertex / extreme point**：不能表示为两个不同可行点的严格凸组合的点。
- **active constraint**：在当前点恰好取等的约束。

## 3. 从 LP 分叉到 SDP 与 MILP

### SDP：替换可行锥

把

\[
x\in\mathbb R_+^n
\]

推广成

\[
X\in\mathbb S_+^n,
\]

得到

\[
\begin{aligned}
\min_X\quad &\langle C,X\rangle\\
\text{s.t.}\quad &\mathcal A(X)=b,\\
&X\succeq0.
\end{aligned}
\]

因此 SDP 可以看成使用 PSD cone 的 conic linear program。

### MILP：加入整数结构

在 LP 的线性约束之外加入

\[
x_i\in\mathbb Z,\qquad i\in I,
\]

就得到 MILP。它不再是凸连续优化问题，但其核心算法仍然反复求解 LP relaxation。

## 4. 第一个统一视角

LP、SDP 和 MILP 的共同对象不是某个具体求解器，而是：

- 可行集合的几何结构；
- 目标函数与支持超平面；
- 对偶变量和下界/证书；
- 通过松弛、分解或附加约束处理困难结构。

后面的课程会逐步把这四个对象具体化。

## 5. 本课最低要求

完成 `problems/week-01.md`，并能不看笔记回答：

1. 为什么 LP 的最优解常常可以在 vertex 处找到？
2. active constraint 与 vertex 是什么关系？
3. SDP 相比 LP 改变了什么？
4. MILP 相比 LP 改变了什么？
5. 为什么 MILP 求解器仍然高度依赖 LP？

