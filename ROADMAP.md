# LP–SDP–MILP Learning Roadmap

这是一条面向“已经做过实际研究，但理论主干不够系统”的学习路线。目标不是把三门课彼此孤立地学完，而是从同一个优化语言出发，理解它们为什么相通、又在哪里分叉。

    线性代数
        ↓
    凸性、几何、分离定理
        ↓
    LP：原始问题、对偶、KKT、算法、敏感性
        ├──────────────────────┐
        ↓                      ↓
    锥优化 / SDP              整数规划 / MILP
        ↓                      ↓
    PSD cone、SDP 对偶         LP relaxation、integer hull
    BM、ALM、一阶法、GPU        B&B、cuts、presolve、学习型求解器

## 1. 学习目标

完成这条路线后，应当能够：

1. 从几何、代数和 primal–dual 三个角度解释一个 LP。
2. 不依赖公式表，从 Lagrangian 推导 LP 和 SDP 的对偶问题。
3. 理解 simplex、interior-point、ALM 和 ADMM 分别在处理什么结构。
4. 把 SDP 看成使用 PSD cone 的 conic linear program。
5. 把 MILP 看成 LP relaxation 加上整数性和组合搜索。
6. 看懂 reduced cost、dual slack、互补性、Farkas certificate、LP bound、integer hull 之间的关系。
7. 将这些概念映射回 GPU SDP、BM/ALM、MILP branching/cutting、变量固定和图表示研究。

## 2. 每个主题的学习闭环

每个模块都按同一个闭环推进：

    概念 → 手推 → 小实验 → 解释自己的研究 → 记录未解决问题

每学一个概念，都回答四个问题：

1. **它是什么？** 给出定义和一个最小例子。
2. **为什么需要它？** 说明它解决了什么困难。
3. **数学上怎么推？** 至少完整手推一次。
4. **它在哪里出现？** 连接到本项目或当前研究代码。

不要把“能调用求解器”当成学会。最低要求是：能够解释求解器输出的变量、对偶变量、slack、bound、residual 和 termination reason。

## 3. 主路线：四个阶段、十二个模块

时间只是建议。若某个模块不能完成手推和小实验，就延长该模块，不要为了赶周数跳过对偶性和几何。

### 阶段 A：共同主干——线性代数、几何与 LP

#### Module 1 — 线性代数与优化语言

**核心内容**

- 向量空间、线性无关、rank、range、null space。
- 正交投影、最小二乘、对称矩阵、特征值和二次型。
- 仿射空间、线性映射、矩阵内积与 Frobenius 范数。

**手推与代码**

- 推导最小二乘的 normal equations，并理解零空间为什么导致解的非唯一性。
- 证明 xᵀXx ≥ 0 与对称矩阵 PSD 的联系。
- 用 NumPy 实现投影、残差和最小特征值检查。

**研究连接**

- SDP 中的 PSD、最小特征值和 dual certificate。
- BM 因子 X = RRᵀ 与 rank 结构。
- 矩阵自由算子中的 range/null-space 思维。

**完成标准**

能够解释“一个线性系统不可解”“一个矩阵不是 PSD”“一个最小二乘解不唯一”分别由什么线性代数结构导致。

#### Module 2 — LP 的几何结构

**核心内容**

- hyperplane、halfspace、polyhedron、polytope、face。
- feasible point、active constraint、vertex、extreme point。
- basic solution、basic feasible solution 与 vertex 的关系。
- 线性目标的等值线、最优面和无界性。

**手推与代码**

- 对二维 LP 画出可行域，列出所有 vertices，并检查每个点的 active constraints。
- 构造空集、无界、有限最优值和多重最优解的例子。
- 完成 experiments/lp_geometry.py，再加入二维 halfspace 的顶点枚举实验。

**研究连接**

- simplex 在 vertices 之间移动。
- MILP 的 LP relaxation 为什么提供 bound。
- cutting plane 为什么是在逼近 integer hull。

**完成标准**

能用图形解释为什么线性目标的有限最优解可以在 extreme point 处取得。

#### Module 3 — LP 对偶、Lagrangian 与证书

**核心内容**

- 标准形式和不同约束方向之间的转换。
- weak duality、strong duality、complementary slackness。
- Lagrangian、dual function、Farkas lemma。
- dual variable、shadow price、reduced cost。

**手推与代码**

- 从 Lagrangian 而不是背规则推导 LP dual。
- 用 weak duality 证明一个候选解是下界。
- 为一个不可行系统写出 Farkas certificate。
- 对小 LP 同时计算 primal/dual 值，并检查 residual、slack 和互补性。

**研究连接**

- SDP 中的 S(y) = C − A*(y) 是 LP dual slack 的矩阵版本。
- reduced-cost fixing、strong branching 和 MILP 特征。
- dual certificate、infeasibility certificate 与最小特征值验证。

**完成标准**

给定一个新的 LP，能够自己写出 primal、dual、Lagrangian 和互补条件，并解释每个 dual quantity 的意义。

#### Module 4 — LP 算法与 KKT

**核心内容**

- simplex 的 basis、pivot、reduced cost 和退化。
- primal/dual feasible 与 optimality。
- barrier method、central path、KKT system。
- Newton step、Schur complement、数值稳定性。

**手推与代码**

- 手算一个小 LP 的 simplex pivot。
- 从 barrier objective 推导一阶条件，并说明 Newton system 如何出现。
- 将 LP 的 KKT 条件写成 residual 和 complementarity。
- 实现一个教育用途的 tiny simplex 或 primal-dual residual 检查器。

**研究连接**

- 为什么传统 SDP IPM 需要大规模 Newton system。
- ALM/ADMM 中 primal residual、dual residual 和 penalty parameter 的来源。
- MILP 节点为什么反复调用 LP solver。

**完成标准**

能解释 simplex 与 interior-point 分别利用了哪一种几何结构，并能读懂一个 LP 求解器的基本 termination 信息。

### 阶段 B：从 LP 到锥优化与 SDP

#### Module 5 — 凸优化与锥优化桥梁

**核心内容**

- convex set、convex function、epigraph。
- separating hyperplane 和 supporting hyperplane。
- cone、dual cone、self-dual cone。
- 一般 conic program：

      min  <c, x>
      s.t. A(x) = b,  x ∈ K.

- conic dual：

      max  bᵀy
      s.t. c − A*(y) ∈ K*.

**手推与代码**

- 由一般 conic program 推导 dual。
- 分别取 K = Rⁿ₊ 和 K = Sⁿ₊，观察 LP/SDP 的统一形式。
- 用小例子检查非负锥和 PSD 锥的 membership。

**完成标准**

能准确说明：LP 与 SDP 的主要差别是使用了不同的可行锥，而不是“SDP 只是一个更大的 LP”。

#### Module 6 — SDP 基础与 Max-Cut relaxation

**核心内容**

- 对称矩阵、PSD、谱分解、rank、trace、Schur complement。
- SDP primal、dual、dual slack 与 PSD cone 的自对偶性。
- matrix complementarity：

      X ⪰ 0,  S ⪰ 0,  <X, S> = 0.

- 从 X = xxᵀ 和 rank-one constraint 得到 Max-Cut 的 SDP relaxation。

**手推与代码**

- 对一个小图写出 Max-Cut 的组合形式、矩阵形式和 SDP relaxation。
- 推导对应的 dual，并解释每个约束的来源。
- 构造 SDP 数据矩阵，计算 primal residual、dual residual、gap 和最小特征值。

**研究连接**

- 量子 ordered search 中的 SDP 数据如何被视为线性算子和 PSD 变量。
- dual slack 的最小特征值为什么能作为证书的一部分。

**完成标准**

看到一个 SDP 时，能明确指出变量是什么、线性映射是什么、PSD 约束是什么、目标是什么，以及 dual slack 如何构造。

#### Module 7 — SDP 算法：IPM、ALM、ADMM

**核心内容**

- SDP IPM 的 KKT/Newton 系统和可扩展性瓶颈。
- augmented Lagrangian、penalty term、dual update。
- ADMM 的 splitting、primal residual、dual residual。
- 低秩结构、存储复杂度与矩阵乘法。

**手推与代码**

- 从约束违反项推导 augmented Lagrangian 的梯度。
- 解释 penalty 增大时为什么可行性通常变强，但子问题可能更病态。
- 说明 ALM 与 ADMM 在变量分裂上的关系。
- 对极小 SDP 实现 penalty method 原型，记录 residual、gap、penalty 和 wall time。

**研究连接**

- cuLoRADS、CARDAL、BM-ALM 中的 residual 和 reoptimization。
- 为什么单独观察 dual residual 可能不足以判断整体收敛。

**完成标准**

能够区分 primal feasibility、dual feasibility、stationarity 和 complementarity，并解释 penalty parameter 的数值作用。

#### Module 8 — Burer–Monteiro 与 GPU 视角

**核心内容**

- X = RRᵀ 如何自动满足 PSD constraint。
- rank restriction 带来的变量减少与非凸性。
- factor-space gradient、矩阵自由线性算子。
- 一阶法、GPU-resident design、memory traffic 和 kernel parallelism。

**手推与代码**

- 对 <C, RRᵀ> 求关于 R 的梯度。
- 解释低秩因子化为什么改变 memory/computation profile，但不自动保证等价。
- 对一个小问题写出 S(y)R 形式的 stationarity。
- 实现低秩因子化的 toy SDP 梯度下降，比较显式形成 X 与只计算 R 相关矩阵乘的内存和时间。

**研究连接**

- BM-ALM、cuLoRADS、CARDAL、cuHALLaR 和 matrix-free GPU SDP。
- GPU kernel、Lanczos/eigenvalue validation 和 dual certificate 实验。

**完成标准**

能清楚区分原始 SDP 的凸性、BM 因子问题的非凸性、低秩结构带来的计算收益，以及等价性/全局最优性所需的额外理论条件。

### 阶段 C：从 LP relaxation 到 MILP

#### Module 9 — 整数规划、integer hull 与 formulation

**核心内容**

- integer feasible set、convex hull、integer hull。
- LP relaxation、valid inequality、integrality gap。
- binary/integer modeling、big-M、indicator constraint。
- totally unimodular matrix 的基本直觉。

**手推与代码**

- 对 knapsack、set cover 和 facility/location 小例子写 MILP 与 LP relaxation。
- 计算 LP bound、integer optimum 和 integrality gap。
- 用枚举得到 integer optimum，再与 LP relaxation 对比。
- 保存实例、随机种子、目标值和 gap，建立可复现实验格式。

**研究连接**

- 变量固定为什么可能排除最优解。
- “安全 fixing”需要哪些 bound 或证书条件。
- 预训练 MILP 图表示中变量节点、约束节点和边特征的优化含义。

**完成标准**

能准确解释 MILP 难在哪里、LP relaxation 提供什么，以及 integer hull 为什么是理想但通常不可直接得到的对象。

#### Module 10 — Branch-and-Bound 与 branching

**核心内容**

- incumbent、global bound、node bound、fathoming。
- fractional variable branching、disjunction。
- strong branching、reliability branching、pseudo-cost。
- node selection、depth-first、best-bound 和 hybrid strategy。

**手推与代码**

- 从 fractional LP solution 展开完整的小型 B&B tree。
- 在每个节点写出 bound 更新和 pruning 原因。
- 解释 cardinality branching：

      Σ(i ∈ S) xᵢ ≤ k   or   Σ(i ∈ S) xᵢ ≥ k + 1.

- 实现只支持小规模 binary problem 的教学版 B&B，记录节点 bound、depth、branching rule 和 pruning reason。

**研究连接**

- learn to branch、probabilistic multi-variable branching 和 cardinality branching。
- 学习型 branching 真正应该优化的是树大小、bound progress 还是最终 wall time。

**完成标准**

能把 branching 解释为 disjunction，把 B&B 解释为用多个 convex LP 子问题处理非凸整数集合。

#### Module 11 — Cutting planes 与 separation

**核心内容**

- valid inequality、separation problem、cut violation。
- Gomory fractional cuts、Chvátal–Gomory cuts。
- cover inequalities、clique/flow cuts 的基本思想。
- disjunctive cuts 与 split cuts。

**手推与代码**

- 从 fractional tableau 推出 Gomory cut。
- 对 set cover 构造 cover inequality，验证整数解保留而 fractional 解被排除。
- 比较 cut 强度和 cut 对 LP 求解成本的权衡。
- 写小规模 separation 例程，统计 violation、bound improvement 和数值稳定性。

**研究连接**

- learn to cut 与 cut selection。
- safe cut、预测误差和不损失最优性的条件。
- 为什么更强的 relaxation 不一定带来更短的总运行时间。

**完成标准**

能从 integer hull 的角度解释 cut，而不是只把 cut 当作额外约束；能区分 valid、violated、有效但昂贵等概念。

### 阶段 D：统一、复现与研究化

#### Module 12 — 求解器架构与研究连接

基本流程：

    建模
      ↓
    presolve / scaling
      ↓
    root LP 或 root relaxation
      ↓
    cuts + heuristics
      ↓
    branch-and-bound
      ↓
    node LPs / bounds / incumbent
      ↓
    termination certificate

**核心内容**

- presolve、scaling、warm start、basis reuse。
- primal/dual bound、gap、residual、证书和 termination。
- solver time、memory、preprocessing、数据传输和 kernel time 的拆分。
- 学习方法应优化的真实系统目标，而不只是预测准确率。

**综合任务**

1. 对同一个小问题分别写出 LP、MILP、SDP 或 relaxation 版本。
2. 对每个版本报告目标值、bound、gap、残差、运行时间和内存。
3. 解释哪一种松弛或搜索结构更适合该实例，以及代价是什么。
4. 把实验结果写成一个 short technical note，而不是只保存日志。

**研究连接**

- GPU SDP：算子、内存、Lanczos、证书和精度。
- MILP：图表示、variable fixing、branching/cut learning 和端到端加速。
- 统一实验规范：实例生成规则、随机种子、容差、时限和硬件信息。

**完成标准**

能从一个具体研究问题出发，判断它属于 relaxation、search、certificate、numerical linear algebra 还是 systems optimization，并选择相应的理论工具和实验指标。

## 4. 三个贯穿案例

### 案例 A：二维 LP

用于理解 halfspace、vertex、active constraint、dual 和敏感性。当前入口是 notes/01-lp-foundations.md 与 experiments/lp_geometry.py。

### 案例 B：Set Cover / Knapsack

用于理解 MILP formulation、LP relaxation、integrality gap、branching、cover cut 和变量固定。它也和现有 MILP 图表示数据最接近。

### 案例 C：Max-Cut

用于把组合问题、MILP、LP relaxation、SDP relaxation、dual slack、BM 和 GPU 计算连起来：

    组合问题
       ↓
    MILP formulation → LP relaxation → B&B / cuts
       ↓
    矩阵提升 X = xxᵀ → 去掉 rank-one → SDP relaxation
       ↓
    SDP dual → PSD slack → BM / ALM / GPU

## 5. 与当前研究的概念映射

| 基础概念 | SDP 研究中的对应物 | MILP 研究中的对应物 |
|---|---|---|
| LP dual slack | S = C − A*(y) | reduced cost、LP dual features |
| Complementarity | <X,S> = 0、XS = 0 | variable/bound complementarity |
| Farkas certificate | dual certificate、PSD/eigenvalue check | infeasibility certificate、valid inequality |
| Relaxation | 低秩或其他 SDP relaxation | LP relaxation |
| Cone / feasible set | PSD cone | integer feasible set / integer hull |
| Bound | primal/dual objective bound | node LP bound、global bound |
| Disjunction | cone/face 结构的分解视角 | branching、split/cardinality branching |
| First-order operation | S(y)R、算子与矩阵乘 | 节点 LP、启发式、学习策略 |
| Numerical certificate | residual、gap、最小特征值 | gap、bound、integrality、feasibility |

## 6. 每周产出格式

每个模块至少留下四类内容：

1. notes/：定义、推导和自己的解释。
2. problems/：手推题、答案或仍未解决的步骤。
3. experiments/：最小可运行代码和固定随机种子。
4. journal/：本周理解、疑问、研究连接和下一步。

推荐的周总结结构：

    # Week N — Topic

    ## 我现在能解释什么
    ## 我亲手推导了什么
    ## 我运行了什么实验
    ## 它和我的 SDP/MILP 研究有什么关系
    ## 仍然不清楚的问题
    ## 下一周的最小任务

## 7. 建议参考材料

不需要同时读完很多书。建议按功能使用：

- LP：Bertsimas & Tsitsiklis, Introduction to Linear Optimization。
- 凸优化与对偶：Boyd & Vandenberghe, Convex Optimization。
- SDP：Vandenberghe & Boyd, Semidefinite Programming。
- MILP 入门：Wolsey, Integer Programming。
- MILP 深入：Conforti, Cornuéjols, and Zambelli, Integer Programming。

阅读顺序优先于阅读数量：先完成 Module 1–4 的手推，再按 Module 5–8 和 Module 9–11 分叉，最后用 Module 12 重新解释自己的研究。

