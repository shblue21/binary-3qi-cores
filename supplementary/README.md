# Supplementary verification

The programs use only the Python standard library.

Run:

    python3 verify_certificates.py
    python3 verify_lift_small.py

`verify_certificates.py` checks the 55 anchors in the \(n=12\) obstruction
and the 630 anchors in the \(n=16\) boundary construction.

`verify_lift_small.py` independently checks the crossing-clique values
\(q(4),q(5),q(6)\) and constructs a directed balanced-anchor separation
witness for every ordered pair of distinct vertices at \(n=8,9,10\).

These finite checks are falsification and transcription checks. The
general theorems are proved symbolically in the manuscript.
