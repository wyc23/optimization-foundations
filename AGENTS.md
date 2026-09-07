# Repository Instructions for Learning Materials

## Source-first rule

This repository is a source-grounded learning project. Before creating or
substantially revising a lesson, problem set, derivation, or research note:

1. Read references/README.md.
2. Read the relevant entries in references/core-textbooks.md and
   references/core-papers.md.
3. Use the source bibliography and record citations in a Sources section.
4. Clearly distinguish:
   - a statement directly supported by a reference;
   - a pedagogical explanation or reorganization;
   - an inference or a research hypothesis.
5. If the references do not settle a question, say so and add the question to
   the learning journal instead of filling the gap with an unsupported claim.

The assistant may explain a source in simpler language, but should not silently
replace the source with an invented textbook-style treatment.

## Study order

The default order is:

    LP → convex/conic optimization → SDP → MILP

This order is intentional. LP geometry, duality, KKT conditions, and
certificates are the common language for the later SDP and MILP material.

## Citation and source maintenance

- Use the short keys from references/bibliography.bib, for example
  BertsimasTsitsiklis1997 or VandenbergheBoyd1996.
- Include chapter/section numbers when the edition is known.
- Prefer publisher, author, journal, conference, DOI, arXiv, or official
  project pages over informal copies.
- Do not commit full copyrighted textbooks or papers unless redistribution
  permission is clear. Store bibliographic metadata, stable links, and
  source-grounded notes instead.
- When adding a reference, record why it is useful for this roadmap and which
  module it supports.

## Writing style

Learning material should be rigorous but readable. Use small examples and
complete derivations before general notation. Connect each abstract concept to
one of the repository cases: a small LP, Set Cover/Knapsack, or Max-Cut.

