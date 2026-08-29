# Cores of Binary 3-Qualitative Independence Hypergraphs

This repository contains a preprint and finite verification programs for the
claim

\[
3\text{-}\mathrm{QI}(n,2)\text{ is a core for every }n\ge8.
\]

The proof establishes all even uniform middle layers, combines them with the
previous odd almost-uniform result, and proves a middle-layer rigidity lift
from the balanced layer to the full hypergraph.

## Build and verify

Requirements:

- a LaTeX installation with pdflatex and bibtex;
- Python 3;
- Poppler pdfinfo for the release check.

Run:

    make all

The release PDF is written to:

    output/pdf/binary-3qi-cores-preprint.pdf

The verification programs use only the Python standard library.

## Mathematical status

The manuscript contains human-readable symbolic proofs. The programs verify
the finite \(n=12\) and \(n=16\) critical-fold certificates and small
middle-layer-lift instances. AI systems assisted discovery, drafting, code,
and adversarial audits. No qualified human specialist has peer reviewed the
complete argument.

## Previous result

The odd almost-uniform middle layer is supplied by:

- J. Kim, Cores of the Merged Johnson Graphs
  \(J(2k+1,k)_{\{2,\ldots,k-2\}}\),
  DOI: [10.5281/zenodo.22096460](https://doi.org/10.5281/zenodo.22096460).

## Licenses

- Manuscript and documentation: CC BY 4.0.
- Verification code: MIT.
- See the license files for details.
