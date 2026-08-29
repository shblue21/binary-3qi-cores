# Cores of Binary 3-Qualitative Independence Hypergraphs

[![Verification](https://github.com/shblue21/binary-3qi-cores/actions/workflows/verify.yml/badge.svg)](https://github.com/shblue21/binary-3qi-cores/actions/workflows/verify.yml)

This repository contains the source, PDF, and verification programs for the
preprint *Cores of Binary 3-Qualitative Independence Hypergraphs*.  Its main
result is

\[
3\text{-}\mathrm{QI}(n,2)\text{ is a core for every }n\ge8.
\]

The proof establishes that the balanced layer is a core for every \(n\ge8\)
and then shows that every endomorphism of the full hypergraph is determined
by its restriction to that layer.

## Build and verify

Requirements:

- a LaTeX installation with pdflatex and bibtex;
- Python 3;
- Poppler pdfinfo for the release check.

Run:

    make all

Before packaging a release, run:

    make release-check

This also repeats the verifiers under `python3 -O` and confirms that the PDF
is bit-for-bit reproducible in a fresh temporary directory.  The build fixes
`SOURCE_DATE_EPOCH` to the release date; it may be overridden explicitly.

To regenerate the versioned PDF, source ZIP, and both checksum manifests, run:

    make package

The manuscript PDF is written to:

    output/pdf/binary-3qi-cores-preprint.pdf

The verification programs use only the Python standard library.

## Repository

The canonical source repository is:

    https://github.com/shblue21/binary-3qi-cores

## Mathematical status

The general arguments are given in the manuscript.  The Python programs check
the finite construction for \(n=12\), the boundary instance \(n=16\) of the
uniform construction, and small instances of the balanced-layer lift.  This is
a preprint and has not yet undergone independent specialist peer review; see
`AI_DISCLOSURE.md`.

## Previous result

For the odd almost-uniform balanced layers, see the companion manuscript:

- J. Kim, *Cores of the Merged Johnson Graphs J(2k+1,k) with Relations 2
  through k-2*, contained in the v1.0.0 software archive
  [10.5281/zenodo.22096460](https://doi.org/10.5281/zenodo.22096460).

## Licenses

- Manuscript and documentation: CC BY 4.0.
- Verification code: MIT.
- See the license files for details.

Zenodo's record-level license describes the manuscript package.  The included
Python source remains available under the MIT license.
