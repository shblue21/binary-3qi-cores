required **UQI** extension. The conclusion of Lemma 6 is nevertheless correct.

**PROPOSED REPAIR 1.** Write the four pair cells in the order

$$
A\cap B,\quad A\cap B^c,\quad A^c\cap B,\quad A^c\cap B^c,
$$

with sizes \(s,k-s,k-s,s\). For \(2\le s\le k-2\), choose \(C\) so that its intersections with these cells have sizes

$$
1,\quad 1,\quad k-s-1,\quad s-1.
$$

Their sum is \(k\), and each number lies strictly between \(0\) and the corresponding cell size. Hence \(C\) and \(C^c\) both meet all four cells. This is a balanced witness and completely repairs the implication.

Thomas–Akhtar’s printed argument selects one point from each cell and then invokes that construction in Lemma 6. That establishes the full-QI condition but leaves the uniformity requirement unproved for \(k>4\).

---

## 3. SOURCE TABLE

| Source/result                                                                                                                                                                                                                                         | Primary-source location                                                                                                                                | Exact concise content and hypotheses                                                                                                                                                                                                                                                                                                 | Audit status                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Peter J. Cameron and Priscila A. Kazanidis, **“Cores of Symmetric Graphs,”** *Journal of the Australian Mathematical Society* **85** (2008), 145–154. DOI: [https://doi.org/10.1017/S1446788708000815](https://doi.org/10.1017/S1446788708000815)     | Primary PDF verified. Corollary 2.2 is on PDF page 3 of 10, printed journal p. 147. Theorem 2.1 begins on printed p. 146.                              | Exact Corollary 2.2: “Let \(\Gamma\) be a non-edge-transitive graph. Then either the core of \(\Gamma\) is a complete graph, or \(\Gamma\) is a core.” The paper’s standing convention is that graphs are finite, undirected and simple. No connectedness, primitivity, or full automorphism classification is assumed.              | **VERIFIED**                                         |
| Mohammed Hamoud Aljohani, **“Synchronising and separating permutation groups through graphs,”** PhD thesis, University of St Andrews, 2022. DOI: [https://doi.org/10.17630/sta/227](https://doi.org/10.17630/sta/227)                                 | The repository record and complete-PDF bitstream were identified. The degree was awarded in 2022 and the repository supplies the complete thesis file. | Exact PDF page, exact wording of Theorem 3.66, its exceptional cases, the proof’s implication chain, and the statement of Theorem 3.64 could not be inspected because the primary bitstream repeatedly timed out. Search-index fragments are not promoted to primary-source verification.                                            | **SOURCE NOT VERIFIED**                              |
| Raina Mary Thomas and Yasmeen Akhtar, **“On the Cores of Uniform and Almost-Uniform 3-Qualitative Independence Hypergraphs,”** arXiv:2607.18674v2, 31 July 2026. Stable URL: [https://arxiv.org/abs/2607.18674v2](https://arxiv.org/abs/2607.18674v2) | Primary v2 PDF verified. Definitions are on PDF pp. 1–3.                                                                                               | Vertices are normalized strings/partitions; uniform binary vertices have equal class sizes. Their hypergraph-homomorphism definition requires preservation of edge cardinality in the image and calls a bijective endomorphism an automorphism.                                                                                      | **VERIFIED**                                         |
| Thomas–Akhtar, Proposition 4                                                                                                                                                                                                                          | PDF p. 8                                                                                                                                               | Exact direction: “If \([H]_2\) is a core, then so is \(H\).” The reverse direction is not stated.                                                                                                                                                                                                                                    | **STATEMENT VERIFIED; PRINTED PROOF REPAIRED BELOW** |
| Thomas–Akhtar, Proposition 5                                                                                                                                                                                                                          | PDF pp. 8–9                                                                                                                                            | The core of a graph \(G\) is isomorphic to the core of its shadow \(D_2(G)\). Here \(D_2(G)\) is the two-false-twin blow-up of \(G\).                                                                                                                                                                                                | **VERIFIED; NOT NEEDED**                             |
| Thomas–Akhtar, Condition 1 and Lemma 6                                                                                                                                                                                                                | PDF p. 9                                                                                                                                               | Condition 1 characterizes pair extendability in the full binary \(3\)-QI hypergraph by requiring all four pair cells to have size at least \(2\). Lemma 6 identifies the shadow \(D_2([3\text{-}\mathrm{UQI}(n,2)]_2)\), not the quotient itself, with the full merged Johnson graph having intersection set \(\{2,\ldots,n/2-2\}\). | **CONCLUSION VALID; UNIFORM-WITNESS GAP REPAIRED**   |
| Thomas–Akhtar, Proposition 6                                                                                                                                                                                                                          | PDF pp. 9–10                                                                                                                                           | If the core of the full merged Johnson/shadow graph has order \(\frac12\binom{n}{n/2}\), then \(3\)-UQI\((n,2)\) is a core.                                                                                                                                                                                                          | **VERIFIED; NOT USED**                               |

The Aljohani theorem is therefore not treated as an established citation in this audit. Its one load-bearing implication is replaced by the proof in Section 7.

---

## 4. OBJECT/QUOTIENT TABLE

### Exact hypergraph model

A binary uniform vertex of \(3\)-UQI\((2k,2)\) has \(k\) coordinates in each symbol class. Interchanging the two binary symbols replaces a \(k\)-subset \(A\) by \(A^c\). The normalization of symbol names selects one orientation of this pair, so the intrinsic object is the unordered equipartition

$$
[A]=\{A,A^c\},\qquad A\in\binom{[2k]}k.
$$

Consequently,

$$
|V(H_k)|
=\frac12\binom{2k}{k}
=\binom{2k-1}{k-1}
=:N_k.
$$

The last identity follows from

$$
\binom{2k}{k}=2\binom{2k-1}{k-1}.
$$

For three vertices \([A],[B],[C]\), put \(A^1=A\), \(A^0=A^c\), and similarly for \(B,C\). The qualitative-independence condition says precisely that every binary triple occurs in some coordinate. Thus

$$
\{[A],[B],[C]\}\in E(H_k)
$$

if and only if all eight cells

$$
A^{\varepsilon_1}\cap B^{\varepsilon_2}\cap C^{\varepsilon_3},
\qquad
(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{0,1\}^3,
$$

are nonempty.

Replacing any representative by its complement merely applies
\(\varepsilon_i\mapsto1-\varepsilon_i\) to one coordinate of the cell index. It permutes the eight cells and therefore does not change the condition.

### Exact 2-section relation

For two distinct quotient vertices choose representatives \(A,B\) and set

$$
s=|A\cap B|.
$$

The four pair cells are

$$
\begin{aligned}
P_{11}&=A\cap B, & |P_{11}|&=s,\\
P_{10}&=A\cap B^c, & |P_{10}|&=k-s,\\
P_{01}&=A^c\cap B, & |P_{01}|&=k-s,\\
P_{00}&=A^c\cap B^c, & |P_{00}|&=s.
\end{aligned}
$$

If \([A]\) and \([B]\) lie together in a hyperedge with \([C]\), each \(P_{ij}\) must meet both \(C\) and \(C^c\). Hence every \(P_{ij}\) has size at least \(2\), giving

$$
2\le s\le k-2.
$$

Conversely, suppose \(2\le s\le k-2\). Select \(C\) with

$$
\begin{aligned}
|C\cap P_{11}|&=1,\\
|C\cap P_{10}|&=1,\\
|C\cap P_{01}|&=k-s-1,\\
|C\cap P_{00}|&=s-1.
\end{aligned}
$$

The selected cardinalities total \(k\). Moreover,

$$
1\le |C\cap P_{ij}|\le |P_{ij}|-1
$$

for every cell. Thus \(C\) and \(C^c\) each meet all four pair cells, so all eight Boolean cells for \(A,B,C\) are nonempty. Therefore

$$
\boxed{
[A]\sim_{G_k}[B]
\iff
2\le |A\cap B|\le k-2.
}
$$

Complementing one representative changes \(s\) to \(k-s\), so the interval \(2\le s\le k-2\) is orientation-independent.

### Fixed-point quotient

Fix \(\infty\in[2k]\). Every equipartition has a unique part containing \(\infty\). Write it as

$$
\{\infty\}\cup X,
\qquad
X\in\binom{[2k]\setminus\{\infty\}}{k-1}.
$$

This gives a bijection

$$
V(H_k)\longleftrightarrow
\binom{[2k-1]}{k-1}.
$$

For two fixed-point representatives,

$$
A=\{\infty\}\cup X,\qquad
B=\{\infty\}\cup Y,
$$

we have

$$
|A\cap B|=1+|X\cap Y|.
$$

Hence

$$
\Gamma_1:
\quad
X\sim Y
\iff
|X\cap Y|\in\{0,k-2\},
$$

and

$$
G_k:
\quad
X\sim Y
\iff
1\le |X\cap Y|\le k-3.
$$

Thus, on distinct vertices,

$$
\boxed{G_k=\overline{\Gamma_1}.}
$$

### Object table

| Object                                     |                                                           Vertex set and order | Adjacency/hyperedge relation                                                                         | Exact role                                                                 |                                                       |                                                          |             |                                                           |
| ------------------------------------------ | -----------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------- | ----------- | --------------------------------------------------------- |
| \(H_k=3\text{-}\mathrm{UQI}(2k,2)\)        | Unordered equipartitions \([A]=\{A,A^c\}\); order \(N_k=\frac12\binom{2k}{k}\) | Three vertices form an edge iff all eight Boolean cells are nonempty                                 | The original 3-uniform hypergraph                                          |                                                       |                                                          |             |                                                           |
| \(G_k=[H_k]_2\)                            |                                                 Same \(N_k\) quotient vertices | (2\le                                                                                                | A\cap B                                                                    | \le k-2)                                              | Quotient 2-section to which Cameron–Kazanidis is applied |             |                                                           |
| \(\Gamma_1\)                               |                                                 Same \(N_k\) quotient vertices | (                                                                                                    | A\cap B                                                                    | \in{1,k-1}); equivalently, after fixing \(\infty\), ( | X\cap Y                                                  | \in{0,k-2}) | Exact complement of \(G_k\) on distinct quotient vertices |
| Full merged Johnson graph \(\mathcal J_k\) |           All labelled \(k\)-subsets of \([2k]\); order \(\binom{2k}{k}=2N_k\) | (                                                                                                    | A\cap B                                                                    | \in{2,\ldots,k-2})                                    | This is not \(G_k\); it has twice as many vertices       |             |                                                           |
| \(G_k[\overline K_2]\)                     |               Two false-twin copies of every vertex of \(G_k\); order \(2N_k\) | No edge within a fibre; a \(K_{2,2}\) between fibres exactly when the quotient vertices are adjacent | Isomorphic to \(\mathcal J_k\), and to Thomas–Akhtar’s shadow \(D_2(G_k)\) |                                                       |                                                          |             |                                                           |

Indeed, the fibre over \([A]\) consists of the two labelled sets \(A,A^c\). For different fibres, the four labelled intersections have sizes \(s\) or \(k-s\). Therefore either all four cross-pairs are edges or none are, exactly as in a false-twin blow-up.

For \(k=5\),

$$
|V(H_5)|=|V(G_5)|=126,
$$

whereas

$$
|V(\mathcal J_5)|=|V(G_5[\overline K_2])|=252.
$$

No core theorem about the \(252\)-vertex graph is transferred to the \(126\)-vertex quotient in this proof.

---

## 5. GATE TABLE

| Gate |     Status     | Audit result                                                                                                                                                                                                                                  |
| ---: | :------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    1 |    **VALID**   | The equipartition model, eight-cell condition and exact 2-section relation are proved directly. Thomas–Akhtar’s unbalanced witness is replaced by the balanced \(k\)-subset construction.                                                     |
|    2 |    **VALID**   | On the explicitly defined quotient, \(G_k=\overline{\Gamma_1}\). The \(N_k\)-vertex quotient, the \(2N_k\)-vertex full graph and the twin blow-up are distinguished. The exact thesis nomenclature remains source-unverified but is not used. |
|    3 |    **VALID**   | \(S_{2k}\) is directly proved transitive on ordered nonedges of \(G_k\). Cameron–Kazanidis Corollary 2.2 and all its hypotheses are verified.                                                                                                 |
|    4 |    **VALID**   | For finite simple graphs, complete core is proved equivalent to \(\chi=\omega\).                                                                                                                                                              |
|    5 | **UNRESOLVED** | The exact primary-source audit of Aljohani Theorems 3.64 and 3.66 is unresolved. The required implication \((d)\Rightarrow(c)\), however, is independently proved in Section 7 and is therefore mathematically valid.                         |
|    6 |    **VALID**   | The general \(\lambda_j\) formula is derived, and \(\lambda_{k-3}=(k+2)/2\) rules out the design for odd \(k\).                                                                                                                               |
|    7 |    **VALID**   | Using the self-contained Gate 5 replacement, \(\chi(G_k)\ne\omega(G_k)\); Cameron–Kazanidis then forces \(G_k\) to be a core.                                                                                                                 |
|    8 |    **VALID**   | The direction \([H]_2\) core \(\Rightarrow H\) core is proved directly. Thomas–Akhtar Proposition 4 is not used backwards.                                                                                                                    |
|    9 |    **VALID**   | Every argument specializes correctly to \(k=5\); the optional strongly regular parameters also check.                                                                                                                                         |

---

## 6. ALJOHANI VARIABLE MAP

Because the primary thesis PDF was not successfully opened, the following is an **independently established mathematical map** for the explicitly described graph. It is not represented as a certified transcription of Aljohani’s notation.

| Quantity in this problem         | Fixed-point/folded representation              | Role in the candidate Theorem 3.66                               |             |                                 |         |             |
| -------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- | ----------- | ------------------------------- | ------- | ----------- |
| Ground-set size                  | \(2k\)                                         | Ground set for equipartitions and for a possible \(S(k-1,k,2k)\) |             |                                 |         |             |
| Quotient vertex                  | \([A]=\{A,A^c\}\), (                           | A                                                                | =k)         | One unordered \(k+k\) partition |         |             |
| Quotient order                   | \(N_k=\frac12\binom{2k}{k}=\binom{2k-1}{k-1}\) | Number of vertices of \(\Gamma_1\) and \(G_k\)                   |             |                                 |         |             |
| Fixed point                      | \(\infty\in[2k]\)                              | Chooses one representative from each complement pair             |             |                                 |         |             |
| Fixed-point representative       | \(X=A_\infty\setminus\{\infty\}\)              | A \((k-1)\)-subset of a \((2k-1)\)-set                           |             |                                 |         |             |
| Subset block size                | \(k-1\)                                        | Design block size \(b\)                                          |             |                                 |         |             |
| \(\Gamma_1\) relation            | (                                              | A\cap B                                                          | \in{1,k-1}) | Equivalently (                  | X\cap Y | \in{0,k-2}) |
| Complement relation              | \(G_k=\overline{\Gamma_1}\)                    | (                                                                | X\cap Y     | \in{1,\ldots,k-3})              |         |             |
| Maximum \(\Gamma_1\)-clique size | \(k+1\)                                        | Proved independently in Section 7                                |             |                                 |         |             |
| Candidate independence equality  | \(\alpha(\Gamma_1)=N_k/(k+1)\)                 | Produces the Steiner block count                                 |             |                                 |         |             |
| Derived design parameters        | \((t,b,v)=(k-2,k-1,2k-1)\)                     | \(S(k-2,k-1,2k-1)\)                                              |             |                                 |         |             |

The four clauses attributed in the submission to Theorem 3.66 are

$$
\begin{aligned}
(a)\;&\text{a resolvable }S(k-1,k,2k)\text{ exists},\\
(b)\;&\alpha(\Gamma_1)=\frac{\binom{2k-1}{k-1}}{k+1},\\
(c)\;&S(k-2,k-1,2k-1)\text{ exists},\\
(d)\;&\chi(\overline{\Gamma_1})=\omega(\overline{\Gamma_1}).
\end{aligned}
$$

Their exact appearance as a four-way equivalence in the thesis, their page number, and the chain through Theorem 3.64 are **SOURCE NOT VERIFIED**.

Only

$$
(d)\Longrightarrow(c)
$$

is required, and that implication is proved next without the thesis.

---

## 7. SELF-CONTAINED DESIGN IMPLICATION

We prove the following statement.

$$
\boxed{
\chi(\overline{\Gamma_1})
=
\omega(\overline{\Gamma_1})
\Longrightarrow
S(k-2,k-1,2k-1)\text{ exists}.
}
$$

The proof works for every \(k>3\), without a parity assumption.

Set

$$
r=k-1,\qquad v=2r+1=2k-1,
$$

and identify the quotient vertex set with

$$
\Omega=\binom{V}{r},
\qquad |V|=v.
$$

Under this identification, let \(\Gamma\) be the graph

$$
X\sim_\Gamma Y
\iff
|X\cap Y|\in\{0,r-1\}.
$$

Thus \(\Gamma=\Gamma_1\) and

$$
F:=\overline{\Gamma}=G_k.
$$

### Maximum cliques of \(\Gamma\)

We first establish

$$
\boxed{\omega(\Gamma)=r+2=k+1.}
$$

A clique of size \(r+2\) is obtained by fixing an \((r-1)\)-subset \(D\) and taking

$$
\mathcal S_D
=
\{D\cup\{x\}:x\in V\setminus D\}.
$$

There are

$$
v-(r-1)=r+2
$$

members, and any two meet in exactly \(r-1\) points.

It remains to prove that no clique is larger.

#### Case 1: the clique contains two disjoint sets

Let \(A,B\in\Omega\) be disjoint. Since

$$
|A|=|B|=r,\qquad |V|=2r+1,
$$

there is a unique point

$$
x\in V\setminus(A\cup B).
$$

Let \(C\ne A,B\) be adjacent to both. Then

$$
|C\cap A|,\ |C\cap B|\in\{0,r-1\}.
$$

Writing \(\epsilon=1\) when \(x\in C\), the equality

$$
|C\cap A|+|C\cap B|+\epsilon=r
$$

shows that the only possibilities are

$$
C=(A\setminus\{a\})\cup\{x\}
\quad(a\in A)
$$

or

$$
C=(B\setminus\{b\})\cup\{x\}
\quad(b\in B).
$$

Two sets of the first type meet in \(r-1\) points, as do two sets of the second type. But one of each type meets in the singleton \(\{x\}\). Since \(r\ge3\),

$$
1\notin\{0,r-1\},
$$

so the two types cannot be mixed in a clique. Consequently such a clique has at most

$$
2+r=r+2
$$

vertices. This bound is attained by \(A,B\) and all \(r\) sets of either one of the two types.

#### Case 2: the clique has no disjoint pair

Then every two distinct members meet in exactly \(r-1\) points. Choose

$$
A=D\cup\{a\},
\qquad
B=D\cup\{b\},
$$

where \(|D|=r-1\) and \(a\ne b\).

For another member \(C\), the conditions

$$
|C\cap A|=|C\cap B|=r-1
$$

imply one of two alternatives:

1. \(D\subset C\); or
2. \(C\subset D\cup\{a,b\}\).

To see this, put \(q=|C\cap D|\) and let \(\epsilon_a,\epsilon_b\) indicate membership of \(a,b\) in \(C\). Then

$$
q+\epsilon_a=q+\epsilon_b=r-1,
$$

so \(\epsilon_a=\epsilon_b\). If both are \(0\), then \(q=r-1\) and \(D\subset C\). If both are \(1\), then \(q=r-2\), so \(C\) is an \(r\)-subset of the \((r+1)\)-set \(D\cup\{a,b\}\).

If every member contains \(D\), the clique lies in \(\mathcal S_D\) and has at most \(r+2\) members.

Otherwise there is a member

$$
C=(D\setminus\{d\})\cup\{a,b\}.
$$

Any set \(D\cup\{z\}\) with \(z\notin D\cup\{a,b\}\) meets \(C\) in only \(r-2\) points and therefore cannot belong to the clique. The entire clique is then contained in the family of all \(r\)-subsets of the \((r+1)\)-set \(D\cup\{a,b\}\), which has only \(r+1\) members.

This proves

$$
\omega(\Gamma)=r+2.
$$

The maximum cliques are therefore of the star type \(\mathcal S_D\), or of the disjoint-pair type described in Case 1. No automorphism classification is being used.

### Clique–coclique inequality

The natural \(S_v\)-action makes \(\Gamma\) vertex-transitive.

Let \(\mathcal Q\) be a clique and \(\mathcal I\) an independent set in \(\Gamma\). For every permutation \(g\in S_v\),

$$
|\mathcal Q^g\cap\mathcal I|\le1.
$$

Averaging over uniformly random \(g\),

$$
\mathbb E|\mathcal Q^g\cap\mathcal I|
=
\frac{|\mathcal Q||\mathcal I|}{|\Omega|}.
$$

Therefore

$$
|\mathcal Q||\mathcal I|\le|\Omega|.
$$

Taking a maximum clique and maximum independent set gives

$$
\boxed{
(r+2)\alpha(\Gamma)\le N_k.
}
$$

This is the only clique–coclique bound used.

### Consequences of \(\chi(F)=\omega(F)\)

Assume

$$
\chi(F)=\omega(F)=m.
$$

Because \(F=\overline\Gamma\),

$$
m=\omega(F)=\alpha(\Gamma).
$$

Take a proper \(m\)-colouring of \(F\). Every colour class is independent in \(F\), hence a clique in \(\Gamma\), so every colour class has at most \(r+2\) vertices. Therefore

$$
N_k\le m(r+2).
$$

On the other hand, the clique–coclique inequality gives

$$
m(r+2)=\alpha(\Gamma)(r+2)\le N_k.
$$

Thus equality holds throughout:

$$
\boxed{
m=\frac{N_k}{r+2}
=
\frac{\binom{2k-1}{k-1}}{k+1}.
}
$$

Every colour class consequently has exactly \(r+2=k+1\) vertices.

Now take a maximum clique \(\mathcal B\) of \(F\). It has \(m\) vertices and, since adjacent vertices receive different colours, it meets each of the \(m\) colour classes exactly once. Regard its vertices as \(r\)-subsets of \(V\).

Because \(\mathcal B\) is a clique in \(F\), it is an independent set in \(\Gamma\). Therefore no two members of \(\mathcal B\) intersect in \(r-1\) points. It follows that every \((r-1)\)-subset of \(V\) is contained in at most one member of \(\mathcal B\).

The number of incidences between members of \(\mathcal B\) and their \((r-1)\)-subsets is

$$
|\mathcal B|\binom r{r-1}
=
\frac{\binom vr}{r+2}\,r.
$$

Since \(v=2r+1\),

$$
\binom v{r-1}
=
\binom vr\frac{r}{v-r+1}
=
\binom vr\frac{r}{r+2}.
$$

Hence

$$
|\mathcal B|\,r=\binom v{r-1}.
$$

There are exactly as many incidences as there are \((r-1)\)-subsets, while each such subset occurs at most once. Therefore each occurs exactly once.

Thus \(\mathcal B\) is

$$
S(r-1,r,2r+1).
$$

Substituting \(r=k-1\) gives

$$
\boxed{
S(k-2,k-1,2k-1).
}
$$

This proves the required Aljohani direction directly.

---

## 8. STEINER DIVISIBILITY CALCULATION

Use the convention

$$
S(t,b,v)=t\text{-}(v,b,1).
$$

Fix a \(j\)-subset \(J\), with \(0\le j\le t\). Count pairs

$$
(T,B)
$$

such that

$$
J\subseteq T\subseteq B,
\qquad
|T|=t,
$$

and \(B\) is a block.

There are

$$
\binom{v-j}{t-j}
$$

choices for \(T\). Each is contained in exactly one block.

If \(\lambda_j\) blocks contain \(J\), each such block contains

$$
\binom{b-j}{t-j}
$$

eligible \(t\)-subsets \(T\). Consequently,

$$
\boxed{
\lambda_j
=
\frac{\binom{v-j}{t-j}}
     {\binom{b-j}{t-j}}.
}
$$

For the putative system

$$
t=k-2,\qquad b=k-1,\qquad v=2k-1,
$$

take

$$
j=k-3.
$$

Then \(t-j=1\), and

$$
v-j=(2k-1)-(k-3)=k+2,
$$

while

$$
b-j=(k-1)-(k-3)=2.
$$

Therefore

$$
\boxed{
\lambda_{k-3}
=
\frac{\binom{k+2}{1}}{\binom21}
=
\frac{k+2}{2}.
}
$$

For odd \(k\), the integer \(k+2\) is odd. Hence \((k+2)/2\) is not an integer, contradicting the necessary integrality of the number of blocks through a fixed \((k-3)\)-subset.

Thus

$$
\boxed{
S(k-2,k-1,2k-1)
\text{ does not exist for odd }k.
}
$$

This is uniform in \(k\) and uses no design database.

---

## 9. CAMERON–KAZANIDIS DEDUCTION

### Direct nonedge-transitivity

A nonedge of \(G_k\) consists of two distinct quotient vertices with

$$
|A\cap B|\in\{1,k-1\}.
$$

Choose the orientation of \(B\) so that

$$
|A\cap B|=1.
$$

Then the four pair cells have ordered sizes

$$
(1,k-1,k-1,1).
$$

Given two ordered nonedges

$$
([A],[B]),\qquad ([A'],[B']),
$$

choose orientations with intersection \(1\). Select arbitrary bijections

$$
A^{i}\cap B^{j}
\longrightarrow
(A')^{i}\cap(B')^{j}
\qquad (i,j\in\{0,1\}).
$$

The union of these four bijections is a permutation of the \(2k\)-point ground set sending

$$
A\mapsto A',
\qquad
B\mapsto B'.
$$

Therefore \(S_{2k}\) is transitive on ordered nonedges. Since intersection cardinalities are permutation-invariant,

$$
S_{2k}\le\operatorname{Aut}(G_k).
$$

Thus \(G_k\) is nonedge-transitive in the Cameron–Kazanidis sense.

### Complete cores and clique–chromatic equality

For every nonempty finite simple graph \(G\),

$$
\boxed{
\operatorname{core}(G)\cong K_r
\iff
\chi(G)=\omega(G)=r.
}
$$

If \(\operatorname{core}(G)\cong K_r\), then \(G\) and \(K_r\) admit homomorphisms in both directions. A homomorphism \(G\to K_r\) gives

$$
\chi(G)\le r.
$$

A homomorphism \(K_r\to G\) is injective because \(G\) has no loops, and its image is an \(r\)-clique. Hence

$$
r\le\omega(G).
$$

Together with \(\omega(G)\le\chi(G)\), this gives equality.

Conversely, suppose

$$
\chi(G)=\omega(G)=r.
$$

An embedded maximum clique gives a homomorphism

$$
K_r\longrightarrow G,
$$

while a proper \(r\)-colouring gives

$$
G\longrightarrow K_r.
$$

Thus \(G\) and \(K_r\) are homomorphically equivalent. Since \(K_r\) is a core, the core of \(G\) is \(K_r\). The empty graph is handled analogously under the convention \(K_0\).

### The Cameron–Kazanidis dichotomy

Corollary 2.2 applies directly to \(G_k\), not to \(\Gamma_1\). Its exact conclusion is:

$$
\boxed{
G_k\text{ is a core}
\quad\text{or}\quad
\operatorname{core}(G_k)\text{ is complete}.
}
$$

All parameters and hypotheses match:

$$
\begin{array}{c|c}
\text{Cameron--Kazanidis requirement}&G_k\\ \hline
\text{finite}&|V(G_k)|=N_k<\infty\\
\text{undirected and simple}&G_k\text{ is a 2-section graph}\\
\text{nonedge-transitive}&S_{2k}\text{ is transitive on ordered nonedges}
\end{array}
$$

No connectedness assumption and no determination of the full automorphism group are needed.

For completeness, the source’s hull argument has the correct direction. The hull \(\widehat G\) adds precisely those pairs that no endomorphism of \(G\) identifies. Since \(\operatorname{Aut}(G)\) preserves the hull and acts transitively on the nonedges, either no original nonedge is added, giving \(\widehat G=G\), or all are added, giving \(\widehat G=K_{|V(G)|}\). Theorem 2.1 identifies the core of the hull as a complete graph of order equal to the order of the core of \(G\). In the first case the core of \(G\) is complete; in the second the core has all \(|V(G)|\) vertices, so \(G\) itself is a core.

### Eliminating the complete-core branch

By Section 7,

$$
\chi(G_k)=\omega(G_k)
\Longrightarrow
S(k-2,k-1,2k-1).
$$

By Section 8, the design on the right cannot exist when \(k\) is odd. Therefore

$$
\chi(G_k)\ne\omega(G_k).
$$

Since always \(\chi(G_k)\ge\omega(G_k)\), in fact

$$
\chi(G_k)>\omega(G_k).
$$

The complete-core equivalence now gives

$$
\operatorname{core}(G_k)\text{ is not complete}.
$$

The exhaustive Cameron–Kazanidis alternative leaves only

$$
\boxed{G_k\text{ is a core}.}
$$

---

## 10. THOMAS–AKHTAR TRANSFER

Thomas–Akhtar Proposition 4 has exactly the required one-way direction:

$$
\boxed{
[H]_2\text{ core}
\Longrightarrow
H\text{ core}.
}
$$

It does not state the converse.

The proposition is valid, but its printed proof says that if \(H^\bullet\) is an induced subhypergraph of \(H\), then \([H^\bullet]_2\) is automatically an induced subgraph of \([H]_2\). That assertion does not follow merely from inducedness: a pair of retained vertices can be adjacent in \([H]_2\) through a hyperedge containing an omitted vertex. A direct endomorphism argument avoids this issue completely.

Let

$$
f:V(H)\longrightarrow V(H)
$$

be a hypergraph endomorphism. If \(xy\) is an edge of \([H]_2\), there is a hyperedge \(e\) containing \(x,y\). Under the cited homomorphism definition,

$$
|f(e)|=|e|
$$

and \(f(e)\) is contained in a hyperedge of the target. Hence \(f\) is injective on \(e\), so

$$
f(x)\ne f(y),
$$

and \(f(x),f(y)\) lie together in a hyperedge. Therefore

$$
f(x)f(y)\in E([H]_2).
$$

Thus every endomorphism of \(H\) induces an endomorphism of \([H]_2\).

If \([H]_2\) is a core, this induced graph endomorphism is an automorphism, and in particular is injective. Hence \(f\) is injective on \(V(H)\). Since \(H\) is finite, \(f\) is bijective.

Under Thomas–Akhtar’s stated convention, a bijective endomorphism is an automorphism. For \(H_k\), which is 3-uniform, the usual stronger edge-set formulation also follows: for every three-element edge \(e\), \(f(e)\) is a three-element subset of a three-element target edge, so it is itself an edge. Distinct edges have distinct images under a vertex permutation. The induced map

$$
E(H_k)\longrightarrow E(H_k)
$$

is therefore injective and, since the edge set is finite, surjective. Its inverse also preserves edges.

Consequently,

$$
\boxed{
G_k=[H_k]_2\text{ core}
\Longrightarrow
H_k\text{ core}.
}
$$

No converse is used.

Combining this with Section 9 yields

$$
\boxed{H_k\text{ is a core}.}
$$

---

## 11. BOUNDARY \(k=5\)

For

$$
k=5,\qquad n=10,
$$

the complete boundary check is:

| Quantity                               | Value/check                                                                                                                                                   |         |                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------- |
| Quotient order                         | (\displaystyle                                                                                                                                                | V(H_5)  | =\frac12\binom{10}{5}=126) |
| Full labelled graph order              | \(\displaystyle \binom{10}{5}=252\)                                                                                                                           |         |                            |
| Fixed-point representation             | \(4\)-subsets of a \(9\)-point set                                                                                                                            |         |                            |
| \(\Gamma_1\) adjacency                 | (                                                                                                                                                             | X\cap Y | \in{0,3})                  |
| \(G_5\) adjacency                      | (                                                                                                                                                             | X\cap Y | \in{1,2})                  |
| Complement identity                    | \(G_5=\overline{\Gamma_1}\)                                                                                                                                   |         |                            |
| Required design                        | \(S(k-2,k-1,2k-1)=S(3,4,9)\)                                                                                                                                  |         |                            |
| Divisibility number                    | \(\displaystyle \lambda_2=\frac{\binom72}{\binom21}\) is not the relevant expression; correctly, \(\displaystyle\lambda_2=\frac{\binom71}{\binom21}=\frac72\) |         |                            |
| Consequence                            | \(S(3,4,9)\) does not exist                                                                                                                                   |         |                            |
| Clique bound for \(\Gamma_1\)          | \(k+1=6\)                                                                                                                                                     |         |                            |
| Hypothetical design block count        | \(\displaystyle 126/6=21\)                                                                                                                                    |         |                            |
| Cameron–Kazanidis hypotheses           | finite simple graph; ordered-nonedge transitivity holds                                                                                                       |         |                            |
| Self-contained design lemma hypothesis | \(r=k-1=4\ge3\)                                                                                                                                               |         |                            |
| Final conclusion                       | \(G_5\) and \(H_5\) are cores                                                                                                                                 |         |                            |

The balanced Gate 1 construction also works at both possible adjacent intersection values:

$$
s=2:\quad (1,1,2,1),
$$

and

$$
s=3:\quad (1,1,1,2).
$$

In each case these are the numbers selected from the four pair cells, and they sum to \(5\).

The exact Aljohani primary-source hypothesis at \(k=5\) remains source-unverified because the thesis PDF could not be inspected. This does not leave the boundary conditional: the independent proof applies directly at \(k=5\).

### Strongly regular consistency check

In the fixed-point model, \(\Gamma_1\) has the \(126\) four-subsets of a nine-point set as vertices, with adjacency for intersection \(0\) or \(3\).

For a fixed four-subset \(A\), its degree is

$$
\binom54+\binom43\binom51
=
5+20
=
25.
$$

The common-neighbour counts depend only on the intersection size \(q=|A\cap B|\):

$$
\begin{array}{c|c|c}
q& A,B\text{ adjacent in }\Gamma_1&\text{common }\Gamma_1\text{-neighbours}\\ \hline
0&\text{yes}&8\\
3&\text{yes}&8\\
1&\text{no}&4\\
2&\text{no}&4
\end{array}
$$

For example, if \(A,B\) are disjoint, their union leaves one point \(x\); the common neighbours are the four sets obtained by replacing one point of \(A\) by \(x\), and the analogous four obtained from \(B\). If \(|A\cap B|=3\), the count is \(4+3+1=8\). The two nonadjacent intersection types each give \(4\).

Hence

$$
\boxed{
\Gamma_1=\operatorname{SRG}(126,25,8,4).
}
$$

The standard complement formulas give

$$
\begin{aligned}
d'&=126-1-25=100,\\
\lambda'&=126-2-2(25)+4=78,\\
\mu'&=126-2(25)+8=84.
\end{aligned}
$$

Therefore

$$
\boxed{
G_5=\operatorname{SRG}(126,100,78,84).
}
$$

This is only a consistency check; the general proof does not depend on strongly regular graph calculations.

---

## 12. FINAL THEOREM ACTUALLY ESTABLISHED

The following unconditional theorem has been proved:

$$
\boxed{
\text{For every odd integer }k\ge5,\quad
3\text{-}\mathrm{UQI}(2k,2)\text{ is a core}.
}
$$

Equivalently,

$$
\boxed{
n\equiv2\pmod4,\ n\ge10
\quad\Longrightarrow\quad
3\text{-}\mathrm{UQI}(n,2)\text{ is a core}.
}
$$

The complete repaired implication chain is

$$
\begin{aligned}
H_k
&=3\text{-}\mathrm{UQI}(2k,2),\\
G_k=[H_k]_2
&=\overline{\Gamma_1},\\
G_k\text{ nonedge-transitive}
&\Longrightarrow
\left(
G_k\text{ core}
\ \text{or}\
\operatorname{core}(G_k)\text{ complete}
\right),\\
\operatorname{core}(G_k)\text{ complete}
&\Longrightarrow
\chi(G_k)=\omega(G_k),\\
\chi(G_k)=\omega(G_k)
&\Longrightarrow
S(k-2,k-1,2k-1),\\
k\text{ odd}
&\Longrightarrow
S(k-2,k-1,2k-1)\text{ impossible},\\
&\Longrightarrow G_k\text{ core},\\
&\Longrightarrow H_k\text{ core}.
\end{aligned}
$$

No assertion about the \(2N_k\)-vertex full merged Johnson graph is transferred to \(G_k\). No reverse graph-to-hypergraph implication is used. No Aljohani theorem remains a premise.

---

## 13. REPAIRS

### PROPOSED REPAIR 1 — balanced UQI completion

Replace the four-point witness imported from full \(3\)-QI by a balanced \(k\)-subset \(C\) with pair-cell counts

$$
(1,1,k-s-1,s-1).
$$

This proves the missing sufficiency direction in Gate 1 and independently establishes the quotient 2-section relation used by all later gates.

### PROPOSED REPAIR 2 — remove the Aljohani dependency

Replace the citation-dependent implication

$$
\chi(\overline{\Gamma_1})=\omega(\overline{\Gamma_1})
\Longrightarrow
S(k-2,k-1,2k-1)
$$

by Section 7’s direct proof:

1. classify and bound \(\Gamma_1\)-cliques by \(k+1\);
2. prove the vertex-transitive clique–coclique inequality;
3. use an optimal colouring of \(\overline{\Gamma_1}\) to force equality;
4. take a maximum \(\overline{\Gamma_1}\)-clique;
5. count its \((k-2)\)-subsets to obtain the Steiner system.

This completely reruns Gates 6 and 7 without Theorems 3.64 or 3.66.

### PROPOSED REPAIR 3 — direct graph-to-hypergraph transfer

Replace the induced-2-section argument in Thomas–Akhtar’s printed proof with the endomorphism argument in Section 10. Every hypergraph endomorphism induces a 2-section endomorphism; core-ness of the 2-section forces injectivity; finiteness and uniformity give a hypergraph automorphism.

This completely reruns Gates 8 and 9.

OBJECT_IDENTIFICATION = VALID

CK_DICHOTOMY = VALID

ALJOHANI_DIRECTION = VALID

STEINER_OBSTRUCTION = VALID

HYPERGRAPH_TRANSFER = VALID

K5_BOUNDARY = PASS

VERDICT = VALID-BY-SELF-CONTAINED-REPAIR
