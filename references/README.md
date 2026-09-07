# Reference Library

This directory is the evidence layer for the LP–SDP–MILP learning project.
Future lessons should be written from these sources and should cite them,
rather than presenting uncited material as if it were established fact.

## What is included

- references/core-textbooks.md: primary textbooks for the common LP/conic trunk
  and the MILP branch.
- references/core-papers.md: classic papers, surveys, and a small number of
  direct research bridges to GPU and first-order optimization.
- references/bibliography.bib: stable citation keys used by notes and reports.

We store metadata and links by default. Many textbooks and journal papers are
copyrighted, so the repository does not redistribute full books or PDFs unless
an author, publisher, repository, or license clearly permits it. Open author
copies and official open-access pages are linked where available.

## Reading policy

For each new lesson:

1. Start with the assigned textbook section.
2. Use a survey or classic paper to see the original formulation and notation.
3. Use a modern bridge paper only after the basic concept is understood.
4. Write the lesson in our own words and cite the source of every nontrivial
   theorem, algorithm, or historical claim.

The repository notes may be in Chinese or English. Titles, author names,
notation, and citations should remain faithful to the original source.

## Recommended reading order

| Roadmap module | First source | Then read |
|---|---|---|
| 1–2: linear algebra and LP geometry | Bertsimas & Tsitsiklis | Boyd & Vandenberghe; Schrijver |
| 3: duality and certificates | Boyd & Vandenberghe | Bertsimas & Tsitsiklis; Rockafellar |
| 4: simplex and interior point | Bertsimas & Tsitsiklis | Karmarkar; Nesterov & Nemirovskii |
| 5: convex/conic bridge | Boyd & Vandenberghe | Nesterov & Nemirovskii |
| 6: SDP fundamentals | Vandenberghe & Boyd | Laurent & Rendl; Goemans & Williamson |
| 7: ALM, ADMM, first-order methods | Boyd et al. | Chambolle & Pock; Applegate et al. |
| 8: low-rank SDP and GPU connection | Burer & Monteiro | Burer & Monteiro; Boumal et al.; current project papers |
| 9: integer hull and formulations | Wolsey; Nemhauser & Wolsey | Schrijver |
| 10: branch-and-bound | Wolsey; Nemhauser & Wolsey | Land & Doig; Bixby |
| 11: cuts and disjunctions | Wolsey; Nemhauser & Wolsey | Gomory; Balas |
| 12: solver architecture and benchmarks | Wolsey; Bixby | PDLP; MIPLIB 2017 |

## Source levels

- **Core**: should be read before the corresponding module is taught.
- **Classic paper**: original formulation or a foundational theoretical result.
- **Survey**: useful for organizing a field, but not a replacement for a
  primary source when proving a result.
- **Bridge**: connects the foundation to the user's GPU SDP, BM/ALM, or MILP
  learning/solver research.

## Future lesson contract

Every substantial lesson should end with:

    ## Sources

    - [short-key] Author, title, and the exact chapter/section or pages used.
    - A note identifying which parts are source-based explanations and which
      parts are our own experiments or interpretations.

