# Core Papers and Surveys

The papers are organized by the role they play in the roadmap. Read the
foundational papers for their original formulation; read the surveys for
notation and context; read the bridge papers only after the relevant basics are
understood.

## A. LP, convex optimization, and first-order methods

### P1. Karmarkar (1984)

**Citation key:** Karmarkar1984  
N. Karmarkar, “A New Polynomial-Time Algorithm for Linear Programming,”
Combinatorica, 4, 373–395, 1984. DOI: 10.1007/BF02579150.

**Use in the roadmap:** Module 4. This is a historical and theoretical bridge
from simplex-centered LP to polynomial-time interior-point methods.

**Official page:**  
https://link.springer.com/article/10.1007/BF02579150

### P2. Chambolle and Pock (2011)

**Citation key:** ChambollePock2011  
A. Chambolle and T. Pock, “A First-Order Primal-Dual Algorithm for Convex
Problems with Applications to Imaging,” Journal of Mathematical Imaging and
Vision, 40, 120–145, 2011. DOI: 10.1007/s10851-010-0251-1.

**Use in the roadmap:** Module 5 and Module 7. This is the primal-dual
first-order bridge needed before reading PDHG/PDLP.

**Official page:**  
https://link.springer.com/article/10.1007/s10851-010-0251-1

### P3. Boyd et al. (2011)

**Citation key:** BoydADMM2011  
S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, “Distributed
Optimization and Statistical Learning via the Alternating Direction Method of
Multipliers,” Foundations and Trends in Machine Learning, 3(1), 1–122, 2011.

**Use in the roadmap:** Module 7. Use this for the relationship among ADMM,
the method of multipliers, dual decomposition, proximal methods, and splitting.

**Author page and open draft:**  
https://stanford.edu/~boyd/papers/admm_distr_stats.html

### P4. Applegate et al. (2021)

**Citation key:** ApplegatePDLP2021  
D. Applegate, M. Díaz, O. Hinder, H. Lu, M. Lubin, B. O'Donoghue, and
W. Schudy, “Practical Large-Scale Linear Programming using Primal-Dual Hybrid
Gradient,” Advances in Neural Information Processing Systems 34, 2021.

**Use in the roadmap:** Module 4, Module 7, and Module 12. This is a modern
computational bridge from LP saddle-point formulations and PDHG to presolve,
diagonal preconditioning, adaptive step sizes, restarting, and large-scale
matrix-vector computation.

**Conference page:**  
https://proceedings.neurips.cc/paper/2021/hash/a8fbbd3b11424ce032ba813493d95ad7-Abstract.html

**Open preprint:**  
https://arxiv.org/abs/2106.04756

## B. SDP, relaxations, and low-rank methods

### P5. Vandenberghe and Boyd (1996)

**Citation key:** VandenbergheBoyd1996  
L. Vandenberghe and S. Boyd, “Semidefinite Programming,” SIAM Review, 38(1),
49–95, 1996.

**Use in the roadmap:** Module 5 and Module 6. This is the primary SDP survey
for standard form, duality, applications, geometry, and primal-dual
interior-point methods.

**Author page with official PDF:**  
https://stanford.edu/~boyd/papers/sdp.html

### P6. Laurent and Rendl (2005)

**Citation key:** LaurentRendl2005  
M. Laurent and F. Rendl, “Semidefinite Programming and Integer Programming,”
in Discrete Optimization, 2005.

**Use in the roadmap:** Module 6 and the Max-Cut case. It explains how SDP
relaxations arise from 0/1 and integer programs and surveys their use in
combinatorial optimization.

**Author-hosted chapter:**  
https://homepages.cwi.nl/~monique/ow-seminar-sdp/laurent-rendl.pdf

### P7. Goemans and Williamson (1995)

**Citation key:** GoemansWilliamson1995  
M. X. Goemans and D. P. Williamson, “Improved Approximation Algorithms for
Maximum Cut and Satisfiability Problems Using Semidefinite Programming,”
Journal of the ACM, 42(6), 1115–1145, 1995. DOI: 10.1145/227683.227684.

**Use in the roadmap:** Module 6 and the Max-Cut case. This is the canonical
example showing how an SDP relaxation can be combined with randomized
rounding for a combinatorial problem.

**Author-hosted PDF:**  
https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf

**ACM record:**  
https://dl.acm.org/doi/10.1145/227683.227684

### P8. Burer and Monteiro (2003)

**Citation key:** BurerMonteiro2003  
S. Burer and R. D. C. Monteiro, “A Nonlinear Programming Algorithm for Solving
Semidefinite Programs via Low-Rank Factorization,” Mathematical Programming,
95, 329–357, 2003. DOI: 10.1007/s10107-002-0352-8.

**Use in the roadmap:** Module 8. This is the foundational reference for
replacing X with RRᵀ and studying a lower-dimensional nonlinear problem.

**Publisher page:**  
https://link.springer.com/article/10.1007/s10107-002-0352-8

### P9. Burer and Monteiro (2005)

**Citation key:** BurerMonteiro2005  
S. Burer and R. D. C. Monteiro, “Local Minima and Convergence in Low-Rank
Semidefinite Programming,” Mathematical Programming, 103, 427–444, 2005.
DOI: 10.1007/s10107-004-0564-1.

**Use in the roadmap:** Module 8. Read this after the 2003 paper to separate
the computational motivation of factorization from results about local minima
and convergence.

**Publisher page:**  
https://link.springer.com/article/10.1007/s10107-004-0564-1

### P10. Pataki (1998)

**Citation key:** Pataki1998  
G. Pataki, “On the Rank of Extreme Matrices in Semidefinite Programs and the
Multiplicity of Optimal Eigenvalues,” Mathematics of Operations Research,
23(2), 339–358, 1998. DOI: 10.1287/moor.23.2.339.

**Use in the roadmap:** Module 6 and Module 8. This is an advanced reference
for the geometry and rank structure of SDP extreme points.

**INFORMS page:**  
https://pubsonline.informs.org/doi/pdf/10.1287/moor.23.2.339

### P11. Boumal, Voroninski, and Bandeira (2016)

**Citation key:** BoumalVoroninskiBandeira2016  
N. Boumal, V. Voroninski, and A. S. Bandeira, “The Non-Convex Burer–Monteiro
Approach Works on Smooth Semidefinite Programs,” Advances in Neural Information
Processing Systems 29, 2016.

**Use in the roadmap:** Module 8, as a bridge from classical BM to modern
nonconvex optimization theory.

**Open preprint:**  
https://arxiv.org/abs/1606.04970

## C. Integer programming, branching, and cutting planes

### P12. Land and Doig (1960)

**Citation key:** LandDoig1960  
A. H. Land and A. G. Doig, “An Automatic Method of Solving Discrete
Programming Problems,” Econometrica, 28(3), 497–520, 1960.

**Use in the roadmap:** Module 10. This is the classic branch-and-bound paper
for discrete programming.

**JSTOR record:**  
https://www.jstor.org/stable/1910129

### P13. Gomory (1958)

**Citation key:** Gomory1958  
R. E. Gomory, “Outline of an Algorithm for Integer Solutions to Linear
Programs,” Bulletin of the American Mathematical Society, 64, 275–278, 1958.
DOI: 10.1090/S0002-9904-1958-10224-4.

**Use in the roadmap:** Module 11. This is the foundational reference for
Gomory fractional cutting planes.

**Project Euclid record and PDF:**  
https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-64/issue-5/Outline-of-an-algorithm-for-integer-solutions-to-linear-programs/bams/1183522679.full

### P14. Balas (1979)

**Citation key:** Balas1979  
E. Balas, “Disjunctive Programming,” Annals of Discrete Mathematics, 5,
3–51, 1979.

**Use in the roadmap:** Module 10 and Module 11. This provides the
disjunctive-programming viewpoint that connects branching, unions of
polyhedra, convexification, and cutting planes.

**Publisher record:**  
https://www.sciencedirect.com/science/chapter/bookseries/pii/S016750600870342X

### P15. Bixby (2012)

**Citation key:** Bixby2012  
R. E. Bixby, “A Brief History of Linear and Mixed-Integer Programming
Computation,” Documenta Mathematica, Extra Volume: ISMP, 2012.

**Use in the roadmap:** Module 4 and Module 12. Read it for the historical
relationship among simplex, interior point, presolve, branch-and-bound,
branch-and-cut, hardware, and commercial solver development.

**Open chapter:**  
https://ems.press/content/book-chapter-files/27357

### P16. Gleixner et al. (2021)

**Citation key:** MIPLIB2017  
A. Gleixner et al., “MIPLIB 2017: Data-Driven Compilation of the 6th Mixed
Integer Programming Library,” Mathematical Programming Computation, 13,
443–490, 2021. DOI: 10.1007/s12532-020-00194-3.

**Use in the roadmap:** Module 12. This is the reference for the benchmark
library and for thinking about instance selection and computational
evaluation in MILP research.

**Open-access paper:**  
https://link.springer.com/article/10.1007/s12532-020-00194-3

**Official library:**  
https://miplib.zib.de/

## D. Direct research bridges for this project

These are not replacements for the classics. They are included because they
connect the foundations to the user's current GPU SDP and first-order research.

### P17. Ding, Lu, and Yang (2025)

**Citation key:** DingLuYang2025  
L. Ding, H. Lu, and J. Yang, “New Understandings and Computation on Augmented
Lagrangian Methods for Low-Rank Semidefinite Programming,” arXiv:2505.15775,
2025.

**Use in the roadmap:** Module 7 and Module 8, after Burer–Monteiro and ALM
basics.

**Open preprint:**  
https://arxiv.org/abs/2505.15775

### P18. Han et al. (2024)

**Citation key:** HanGPUlowrankSDP2024  
Q. Han, Z. Lin, H. Liu, C. Chen, Q. Deng, D. Ge, and Y. Ye, “Accelerating
Low-Rank Factorization-Based Semidefinite Programming Algorithms on GPU,”
arXiv:2407.15049, 2024.

**Use in the roadmap:** Module 8 and Module 12, as a systems case study for
GPU-resident low-rank SDP computation.

**Open preprint:**  
https://arxiv.org/abs/2407.15049
