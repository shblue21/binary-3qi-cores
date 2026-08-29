# FINAL STATUS

$$
\boxed{\texttt{SOLVED-CORE}}
$$

$$
\boxed{H=3\text{-}\mathrm{UQI}(12,2)\text{ is a core}.}
$$

The decisive result is a small, explicit critical-fold obstruction. It rules out **every** noninjective endomorphism directly, without assuming equal fibres, minimum rank, a Witt colouring, equivariance, or a graph-pseudocore theorem.

---

## 1. Exact object and conventions

Write

$$
U=\{\infty\}\cup[11],\qquad V(H)=\binom{[11]}5.
$$

A vertex \(X\) represents the unordered \(6+6\) partition

$$
\widehat X\mid(U\setminus \widehat X),
\qquad
\widehat X=\{\infty\}\cup X.
$$

For three vertices \(X,Y,Z\), choose in each partition the side containing \(\infty\) as side \(1\). Qualitative independence requires all eight Boolean intersections to be nonempty. The \(111\) intersection automatically contains \(\infty\); the other seven intersections are exactly the seven cells in the question. Therefore the proposed seven-cell definition is correct.

Two independent implementations of this predicate were compared on all

$$
\binom{462}{3}=16\,328\,620
$$

triples. They agree everywhere. The resulting hypergraph has

$$
|E(H)|=6\,098\,400,
\qquad
d_H(X)=39\,600.
$$

The original twelve-point atom multisets of hyperedges fall into exactly the two types

$$
(3,3,1,1,1,1,1,1)
$$

and

$$
(2,2,2,2,1,1,1,1),
$$

occurring \(1\,108\,800\) and \(4\,989\,600\) times respectively.

---

## 2. The \(2\)-section

Fix distinct \(X,Y\), let \(k=|X\cap Y|\), and put

$$
A=X\cap Y,\quad B=X\setminus Y,\quad
C=Y\setminus X,\quad
D=[11]\setminus(X\cup Y).
$$

Their sizes are

$$
|A|=k,\qquad |B|=|C|=5-k,\qquad |D|=1+k.
$$

A third set \(Z\) forms a hyperedge with \(X,Y\) precisely when:

$$
A\setminus Z\ne\varnothing,
$$

and both \(Z\) and \(Z^c\) meet each of \(B,C,D\).

This forces

$$
k\ge1,\qquad 5-k\ge2,
$$

and hence \(1\le k\le3\). Conversely, for \(k=1,2,3\), choose the intersection sizes of \(Z\) with \(A,B,C,D\) as follows:

$$
\begin{array}{c|c}
k&(|Z\cap A|,|Z\cap B|,|Z\cap C|,|Z\cap D|)\\ \hline
1&(0,2,2,1)\\
2&(1,1,1,2)\\
3&(2,1,1,1).
\end{array}
$$

Each row sums to five and satisfies every required splitting condition. Thus

$$
\boxed{X\sim_GY\iff |X\cap Y|\in\{1,2,3\}.}
$$

The exhaustive pair codegrees are

$$
\lambda_1=136,\qquad
\lambda_2=243,\qquad
\lambda_3=136,
$$

and zero for intersections \(0\) and \(4\). Consequently \(G\) is \(425\)-regular.

---

## 3. The distinct nonedges form one \(S_{12}\)-orbit

In the twelve-point partition model, choose one six-set \(A\) from the first partition and one six-set \(B\) from the second. If \(h=|A\cap B|\), their four pair cells have sizes

$$
h,\quad 6-h,\quad 6-h,\quad h.
$$

Replacing \(B\) by its complementary side exchanges \(h\) and \(6-h\). Moreover, \(S_{12}\) is transitive on pairs with a fixed four-cell size pattern.

In the \(\binom{[11]}5\) orientation,

$$
h=1+|X\cap Y|.
$$

Thus the two nonedge cases

$$
|X\cap Y|=0,\qquad |X\cap Y|=4
$$

correspond to \(h=1\) and \(h=5\), which are equivalent after swapping one side. Hence all distinct nonedges lie in one \(S_{12}\)-orbit.

The same \(S_{12}\)-action is vertex-transitive and preserves \(H\), because point permutations and side swaps only permute the original eight Boolean cells.

---

## 4. Independence number of \(G\)

An independent family \(\mathcal I\) has pairwise intersections \(0\) or \(4\).

### Case 1: \(\mathcal I\) contains disjoint \(A,B\)

Let \(p\) be the unique point outside \(A\cup B\). Every further member must be either

$$
(A\setminus\{a\})\cup\{p\}
$$

or the analogous set obtained from \(B\). A set of the first kind and one of the second kind intersect only in \(p\), which is forbidden. Therefore all additional members come from one side, giving

$$
|\mathcal I|\le 2+5=7.
$$

Equality gives an \(F_B\)-family.

### Case 2: no two members are disjoint

Then every distinct pair intersects in four points. Choose

$$
A=S\cup\{a\},\qquad B=S\cup\{b\},\qquad |S|=4.
$$

Any further member is either

$$
S\cup\{c\}
$$

or

$$
(S\setminus\{s\})\cup\{a,b\}.
$$

A member of the first form with \(c\notin\{a,b\}\) intersects one of the second form in only three points, so the family lies either in the seven-member star through \(S\), or in the six-member top inside \(S\cup\{a,b\}\).

Therefore

$$
\boxed{\alpha(G)=7.}
$$

This also corrects one of the supplied leads: maximum independent sets are **not** all of the form \(F_B\). There are two types:

$$
F_B=\{B\}\cup\{X:X\cap B=\varnothing\},
$$

and the seven-member stars

$$
\{X:T\subseteq X\}
$$

for fixed \(T\in\binom{[11]}4\).

I also found and verified a mixed 66-colouring consisting of 36 \(F_B\)-classes and 30 four-subset stars. Thus even partitions into 66 maximum independent sets need not be all-Witt.

---

# 5. The decisive link bound

For \(T\in V(H)\), define the link graph \(L_T\) by

$$
R\sim_{L_T}S
\iff
\{T,R,S\}\in E(H).
$$

Let \(\mathcal C\) be a clique in \(L_T\). For distinct \(R,S\in\mathcal C\), the required \(110\) and \(101\) atoms imply

$$
(T\cap R)\setminus(T\cap S)\ne\varnothing,
$$

and

$$
(T\cap S)\setminus(T\cap R)\ne\varnothing.
$$

Hence the sets

$$
\{T\cap R:R\in\mathcal C\}
$$

are pairwise incomparable: they form an antichain in the Boolean lattice \(2^T\), where \(|T|=5\).

The LYM chain count gives

$$
\sum_{A\in\mathcal A}\frac1{\binom5{|A|}}\le1
$$

for every antichain \(\mathcal A\subseteq2^T\). Since

$$
\binom5{|A|}\le\binom52=10,
$$

every summand is at least \(1/10\). Therefore

$$
|\mathcal A|\le10.
$$

Consequently,

$$
\boxed{\omega(L_T)\le10\quad\text{for every }T\in V(H).}
$$

This is a human combinatorial bound; no maximum-clique computation is being used in the proof.

---

# 6. Explicit critical-fold obstruction

Set

$$
P=\{0,1,2,3,4\},
\qquad
Q=\{0,1,2,3,5\}.
$$

Consider the following eleven vertices:

$$
\begin{array}{c|l}
1&\{1,2,3,5,10\}\\
2&\{0,3,8,9,10\}\\
3&\{0,2,7,9,10\}\\
4&\{2,3,4,9,10\}\\
5&\{1,3,4,8,10\}\\
6&\{1,2,4,7,10\}\\
7&\{0,5,7,8,9\}\\
8&\{0,1,6,7,10\}\\
9&\{3,4,5,7,9\}\\
10&\{2,4,5,6,9\}\\
11&\{1,4,5,7,8\}.
\end{array}
$$

For each pair \(i<j\), the following table supplies an anchor. Entry \(P\) means

$$
\{P,R_i,R_j\}\in E(H),
$$

and entry \(Q\) means

$$
\{Q,R_i,R_j\}\in E(H).
$$

```text
       2 3 4 5 6 7 8 9 10 11
  1    P P P P P P P P P  P
  2      P Q Q Q Q P P P  P
  3        Q Q Q Q P P P  P
  4          P P P Q Q Q  Q
  5            P P P Q Q  Q
  6              P Q P Q  Q
  7                Q Q P  Q
  8                  P P  P
  9                    P  P
 10                       P
```

All 55 assertions are direct substitutions into the seven-cell definition. The certificate CSV records the eight finite atom sizes for each assertion; all first seven entries are positive.

Now suppose that an endomorphism \(f\) satisfied

$$
f(P)=f(Q)=P.
$$

For every \(i<j\), apply \(f\) to the hyperedge selected by the table. Whether its anchor is \(P\) or \(Q\), its image is

$$
\{P,f(R_i),f(R_j)\}\in E(H).
$$

It follows that

$$
f(R_1),\ldots,f(R_{11})
$$

are pairwise adjacent in \(L_P\). They are also all distinct: equality of any two would turn one of the target hyperedges into a triple with a repeated vertex.

Thus \(L_P\) would contain an 11-clique, contradicting

$$
\omega(L_P)\le10.
$$

Therefore

$$
\boxed{\text{there is no endomorphism }f\text{ with }f(P)=f(Q)=P.}
$$

---

# 7. Global core theorem

Suppose \(f:H\to H\) is noninjective. Choose distinct \(X,Y\) with

$$
f(X)=f(Y).
$$

The pair \(X,Y\) cannot be adjacent in \(G\). Otherwise some \(Z\) satisfies

$$
\{X,Y,Z\}\in E(H),
$$

and its image would have the repeated vertex \(f(X)=f(Y)\), so it could not be a hyperedge.

Hence \(X,Y\) is a distinct nonedge. Since all distinct nonedges form one \(S_{12}\)-orbit, choose an automorphism \(\alpha\) with

$$
\alpha(P)=X,\qquad \alpha(Q)=Y.
$$

Let \(W=f(X)=f(Y)\). By vertex transitivity choose an automorphism \(\beta\) with

$$
\beta(W)=P.
$$

Then

$$
g=\beta\circ f\circ\alpha
$$

is an endomorphism satisfying

$$
g(P)=g(Q)=P,
$$

contradicting the critical-fold obstruction.

Therefore every endomorphism is injective. Since \(H\) is finite, every endomorphism is bijective. A bijective edge-preserving self-map permutes the finite edge set, so its inverse also preserves edges. Thus every endomorphism is an automorphism.

$$
\boxed{H\text{ is a core}.}
$$

---

## 8. The standard Witt lead

I independently reconstructed the Witt structures from the ternary matrix

$$
\begin{pmatrix}
1&0&0&0&0&0&1&1&1&1&1\\
0&1&0&0&0&0&1&1&2&2&0\\
0&0&1&0&0&0&1&2&1&0&2\\
0&0&0&1&0&0&2&1&0&1&2\\
0&0&0&0&1&0&2&0&1&2&1\\
0&0&0&0&0&1&0&2&2&1&1
\end{pmatrix}
$$

over \(\mathbf F_3\), followed by the relabelling

$$
(1\ 6\ 10\ 8\ 2\ 7\ 4\ 3\ 9\ 5),
$$

with \(0\) fixed.

The verifier establishes directly that:

* the distinct weight-five supports form an \(S(4,5,11)\) with 66 blocks;
* after adding the zero-sum twelfth coordinate, the 132 weight-six supports form an \(S(5,6,12)\);
* complementary hexads pair into the required 66 vertices;
* the 66 classes \(F_B\) partition all 462 vertices;
* the map

  $$
  r_D(X)=\text{the unique }B\in D\text{ with }X=B\text{ or }X\cap B=\varnothing
  $$

  fixes its 66-vertex image and preserves every edge of \(G\).

Thus this is an actual total graph retraction, not merely a colouring.

For the supplied triple, the reconstructed map gives exactly

$$
\begin{aligned}
\{0,1,2,3,4\}&\mapsto\{5,6,7,8,10\},\\
\{0,1,2,5,6\}&\mapsto\{3,4,7,8,9\},\\
\{0,1,3,5,9\}&\mapsto\{2,4,7,8,10\}.
\end{aligned}
$$

The source finite atoms, ordered as

$$
000,100,010,001,110,101,011,111,
$$

are

$$
\{7,8,10\},\{4\},\{6\},\{9\},
\{2\},\{3\},\{5\},\{0,1\}.
$$

For the image they are

$$
\{0,1\},\{5,6\},\{3,9\},\{2\},
\varnothing,\{10\},\{4\},\{7,8\}.
$$

Therefore the intermediate result is confirmed:

$$
\boxed{\texttt{STANDARD-WITT-MAP-FAILS}.}
$$

---

## 9. Equal-fibre reduction

For completeness, the equal-fibre theorem does apply to this finite vertex-transitive relational structure.

Let \(r:A\to C\) be a retraction onto a core \(C\), and let a transitive group \(\Gamma\le\operatorname{Aut}(A)\) act on \(A\). For every \(g\in\Gamma\),

$$
(r\circ g)|_C:C\to C
$$

is an endomorphism of the core, hence a permutation.

Fix \(y\in C\) and count pairs \((g,c)\in\Gamma\times C\) satisfying \(r(g(c))=y\). Counting first over \(g\) gives \(|\Gamma|\). Counting first over \(c\), using transitivity, gives

$$
|C|\frac{|\Gamma|}{|A|}|r^{-1}(y)|.
$$

Therefore

$$
|r^{-1}(y)|=\frac{|A|}{|C|},
$$

independently of \(y\).

Since a fibre is independent in \(G\), its size \(s\) satisfies

$$
s\mid462,\qquad s\le7.
$$

The proper possibilities are therefore

$$
s\in\{2,3,6,7\},
$$

with image orders

$$
231,\ 154,\ 77,\ 66.
$$

The critical-fold proof eliminates all four possibilities simultaneously; it makes no rank assumption.

---

## 10. Independently checkable computation disclosure

No SAT solver, random search, or uncheckable timeout conclusion is used. The C++ verifier uses only the standard library and performs the complete finite checks described above.

Certificate files:

* [Complete certificate bundle](sandbox:/mnt/data/uqi_core_certificate.zip)
* [Readable proof and reproduction instructions](sandbox:/mnt/data/uqi_core_certificate/README.md)
* [Independent C++ verifier](sandbox:/mnt/data/uqi_core_certificate/uqi_core_verifier.cpp)
* [Recorded verifier output](sandbox:/mnt/data/uqi_core_certificate/verification_output.txt)
* [Critical-fold atom certificate: all 55 pairs](sandbox:/mnt/data/uqi_core_certificate/fold_obstruction.csv)
* [All 462 values of the reconstructed Witt graph retraction](sandbox:/mnt/data/uqi_core_certificate/witt_retraction_map.csv)
* [Mixed 36-\(F_B\)/30-star 66-colouring certificate](sandbox:/mnt/data/uqi_core_certificate/mixed_66_coloring.csv)
* [SHA-256 manifest](sandbox:/mnt/data/uqi_core_certificate/SHA256SUMS)

The bundle SHA-256 is

```text
473464915df486cc8799f884428188c8327b288e38781536cc5cd27d2318a7d1
```

Reproduction:

```bash
g++ -O3 -std=c++20 uqi_core_verifier.cpp -o uqi_core_verifier
./uqi_core_verifier .
```

---

## 11. What remains unresolved

Nothing remains unresolved concerning the requested verdict: all possible noninjective endomorphisms are excluded by the single nonedge-orbit normalization and the explicit link obstruction.

The auxiliary classification questions about every possible \(K_{66}\), every mixed 66-colouring, and every relative Witt-design position are not needed and are not asserted to be fully classified.

The smallest operative obstruction found here is the normalized fold

$$
P,Q\mapsto P
$$

together with the eleven displayed auxiliary vertices: their union-link clique has size \(11\), while every single link has clique number at most \(10\).
