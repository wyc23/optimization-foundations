# Core Textbooks

The books below are not all meant to be read cover to cover. The roadmap uses
them as stable reference points, with a deliberately small primary path.

## T1. Bertsimas and Tsitsiklis — Introduction to Linear Optimization

**Citation key:** BertsimasTsitsiklis1997  
**Authors:** Dimitris Bertsimas and John N. Tsitsiklis  
**Publisher:** Athena Scientific  
**Role:** Main LP text for geometry, duality, simplex, interior-point methods,
network flows, and complexity.

**Why it belongs here:** This is the most direct textbook anchor for Modules
1–4. The authors describe it as a graduate-level treatment emphasizing the
geometry and intuition of linear optimization, together with algorithms and
large-scale applications.

**Read selectively:** polyhedral geometry, extreme points and basic feasible
solutions, duality, sensitivity/reduced costs, simplex, and interior-point
methods.

**Official author page:**  
https://www.mit.edu/~dbertsim/books.html

## T2. Boyd and Vandenberghe — Convex Optimization

**Citation key:** BoydVandenberghe2004  
**Authors:** Stephen Boyd and Lieven Vandenberghe  
**Publisher:** Cambridge University Press, 2004  
**Role:** Main convex-analysis, duality, KKT, cone, and SDP bridge.

**Why it belongs here:** The authors maintain an official Stanford page with
book material, course resources, examples, and errata. It is the common
language connecting LP, conic programming, SDP, Lagrangian duality, and
first-order methods.

**Read selectively:** convex sets and functions, convex optimization problems,
duality, approximation and fitting, geometric problems, and semidefinite
programming.

**Official book page and materials:**  
https://stanford.edu/~boyd/cvxbook/

## T3. Rockafellar — Convex Analysis

**Citation key:** Rockafellar1970  
**Author:** R. Tyrrell Rockafellar  
**Publisher:** Princeton University Press, 1970  
**Role:** Advanced reference for convex sets, conjugacy, separation, duality,
and variational analysis.

**Why it belongs here:** It is not the first book to read, but it gives the
mathematical foundations behind support functions, conjugate functions,
subgradients, and Fenchel-type duality that later appear in conic and
first-order optimization.

**Read selectively:** convex sets and functions, separation, conjugate
functions, subgradients, and duality. Use it as a reference when Boyd and
Vandenberghe leave a proof abbreviated.

**Publisher/library page:**  
https://www.jstor.org/stable/j.ctt14bs1ff

## T4. Nesterov and Nemirovskii — Interior-Point Polynomial Algorithms in
Convex Programming

**Citation key:** NesterovNemirovskii1994  
**Authors:** Yurii Nesterov and Arkadii Nemirovskii  
**Publisher:** SIAM, 1994  
**Role:** Advanced reference for self-concordant barriers and polynomial-time
interior-point methods beyond LP.

**Why it belongs here:** It explains why barrier and interior-point ideas
extend from LP to general convex and conic programs. It is useful for
understanding the conceptual origin of the Newton systems discussed in the
SDP part of the roadmap.

**Read selectively:** barrier functions, Newton steps, complexity framework,
and symmetric/conic programming. Defer the most technical proofs until the LP
and KKT modules are complete.

**SIAM page:**  
https://epubs.siam.org/doi/10.1137/1.9781611970791

## T5. Schrijver — Theory of Linear and Integer Programming

**Citation key:** Schrijver1986  
**Author:** Alexander Schrijver  
**Publisher:** Wiley, 1986; revised reprint, 1998  
**Role:** Advanced reference for polyhedral theory, integer hulls, total
duality, and the mathematical theory of linear/integer programming.

**Why it belongs here:** It is the long-term reference for the geometric side
of MILP: faces, valid inequalities, integral polyhedra, total unimodularity,
and the relationship between linear and integer descriptions.

**Read selectively:** polyhedral structure, integer polyhedra, valid
inequalities, total unimodularity, and complexity. It is a reference text,
not the first pass through MILP algorithms.

**Publisher page:**  
https://www.wiley.com/en-us/Theory%2Bof%2BLinear%2Band%2BInteger%2BProgramming-p-9780471982326

## T6. Nemhauser and Wolsey — Integer and Combinatorial Optimization

**Citation key:** NemhauserWolsey1988  
**Authors:** George L. Nemhauser and Laurence A. Wolsey  
**Publisher:** Wiley, first published 1988  
**Role:** Broad reference for integer programming, polyhedral theory,
relaxation, algorithms, and combinatorial optimization.

**Why it belongs here:** The Wiley contents expose a particularly useful
sequence: linear programming, polyhedral theory, valid inequalities, duality
and relaxation, general algorithms, and integral polyhedra.

**Read selectively:** linear programming, polyhedral theory, theory of valid
inequalities, duality and relaxation, general algorithms, and integral
polyhedra.

**Publisher page:**  
https://onlinelibrary.wiley.com/doi/book/10.1002/9781118627372

## T7. Wolsey — Integer Programming

**Citation key:** Wolsey2020  
**Author:** Laurence A. Wolsey  
**Publisher:** Wiley, second edition, 2020  
**Role:** Main practical MILP text for formulation, relaxation, cutting planes,
branch-and-bound, preprocessing, heuristics, and solver architecture.

**Why it belongs here:** It is the best fit for the transition from theory to
the behavior of modern MILP solvers. The second edition explicitly updates
presolve, primal heuristics, decomposition, and branch-(cut)-and-price.

**Read selectively:** modeling, LP relaxation, valid inequalities, branching,
cutting planes, presolve, primal heuristics, decomposition, and computational
practice.

**Publisher page:**  
https://onlinelibrary.wiley.com/doi/book/10.1002/9781119606475

## How these books map to the repository

- Use T1 for the first LP derivations.
- Use T2 for the LP-to-conic-to-SDP bridge.
- Use T3 and T4 only when a proof requires deeper convex analysis or
  interior-point theory.
- Use T5 and T6 for polyhedral and integer-hull questions.
- Use T7 for practical MILP solver behavior and the research transition.

