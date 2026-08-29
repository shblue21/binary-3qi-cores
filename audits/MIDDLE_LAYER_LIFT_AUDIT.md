## 1. OVERALL VERDICT

**VALID-AFTER-REPAIR**

The implication

$$
B_n\text{ is a core}\Longrightarrow H_n\text{ is a core}
\qquad(n\ge 8)
$$

is true.

The submitted gate sequence is not literally valid as written: in odd dimension, the two middle blocks have different crossing-clique numbers, so maximum crossing families on the two blocks cannot be paired bijectively. Replacing the larger maximum family by a \(q(b)\)-element subfamily repairs Gate 2 completely. After that repair, middle-layer invariance, directed separation, the power trick, and the final lift all hold.

---

## 2. FIRST ERROR

**Gate 2, lower-bound construction, steps 1–2:**

> “choose a maximum crossing family on each block; pair the two families by a bijection.”

For odd \(n=2k+1\), the middle blocks have sizes \(k\) and \(k+1\). Gate 1 gives

$$
\omega(\mathrm{Cross}(k))=q(k),
\qquad
\omega(\mathrm{Cross}(k+1))=q(k+1),
$$

and strict monotonicity gives

$$
q(k+1)>q(k).
$$

Thus maximum families on the two blocks have unequal cardinalities and cannot be paired by a bijection.

The smallest occurrence is \(n=9\):

$$
q(4)=3,\qquad q(5)=4.
$$

**PROPOSED REPAIR:** use a maximum \(q(b)\)-family on the \(b\)-block and any \(q(b)\)-element subfamily of a maximum family on the \((b+1)\)-block.

---

## 3. GATE TABLE

| Gate                                 |    Audit mark | Post-repair result                                     |
| ------------------------------------ | ------------: | ------------------------------------------------------ |
| Gate 1 — crossing-family theorem     |     **VALID** | Exact formula and strict monotonicity proved           |
| Gate 2 — link bound and invariance   |   **INVALID** | Valid after replacing the odd-block bijection as above |
| Gate 3 — restriction and power trick | **DEPENDENT** | Valid once Gate 2 is repaired                          |
| Gate 4 — directed separation         |     **VALID** | Valid symbolically for every \(n\ge8\)                 |
| Gate 5 — finite checks               |     **VALID** | All \(12+19+34\) orbits pass                           |
| Gate 6 — final lift                  | **DEPENDENT** | Valid after repaired Gate 2 and valid Gates 3–4        |

---

## 4. EXACT CROSSING-FAMILY PROOF

Flipping the orientation of an unordered bipartition merely exchanges the two corresponding rows or columns of its common-refinement table. Hence the property that all four cells are nonempty is orientation-independent.

### Even case: \(t=2r\)

Fix \(p\in T\) and write

$$
U=T\setminus\{p\},\qquad |U|=2r-1.
$$

Orient every bipartition by its unique side \(A\) containing \(p\), and write

$$
A=\{p\}\cup F,\qquad F\subsetneq U.
$$

For two oriented sides \(A=\{p\}\cup F\) and \(B=\{p\}\cup G\), their four refinement cells are

$$
\begin{aligned}
A\cap B&=\{p\}\cup(F\cap G),\\
A\cap B^c&=F\setminus G,\\
A^c\cap B&=G\setminus F,\\
A^c\cap B^c&=U\setminus(F\cup G).
\end{aligned}
$$

If the two cuts cross, then in particular

$$
F\setminus G\ne\varnothing,
\qquad
G\setminus F\ne\varnothing.
$$

Thus \(F\) and \(G\) are incomparable. Consequently, the traces of a crossing clique form an antichain in \(2^U\). Sperner’s theorem gives

$$
|\mathcal F|
\le
\binom{2r-1}{r-1}.
$$

This proves

$$
\omega(\mathrm{Cross}(2r))
\le
\binom{2r-1}{r-1}.
$$

For equality, take all \(r\)-subsets of \(T\) containing \(p\):

$$
\mathcal A
=
\{[A]:p\in A,\ |A|=r\}.
$$

There are

$$
|\mathcal A|=\binom{2r-1}{r-1}
$$

such cuts. For distinct \(A,B\in\mathcal A\),

$$
A\cap B\supseteq\{p\},
$$

and, because \(A,B\) are distinct and have equal size,

$$
A\setminus B\ne\varnothing,
\qquad
B\setminus A\ne\varnothing.
$$

Finally,

$$
|T\setminus(A\cup B)|
=
2r-\bigl(2r-|A\cap B|\bigr)
=
|A\cap B|
\ge1.
$$

All four crossing cells are nonempty. Hence

$$
\boxed{\omega(\mathrm{Cross}(2r))
=
\binom{2r-1}{r-1}}.
$$

### Odd case: \(t=2r+1\)

Again fix \(p\in T\), set \(U=T\setminus\{p\}\), so \(|U|=2r\), and orient every cut by its side

$$
A=\{p\}\cup F.
$$

The same four-cell formulas hold. Define

$$
C_F=U\setminus F.
$$

For crossing cuts arising from \(F,G\),

$$
C_F\cap C_G
=
U\setminus(F\cup G)
\ne\varnothing.
$$

Moreover, \(F,G\) are incomparable, so their complements \(C_F,C_G\) are also incomparable. Therefore the family

$$
\mathcal C=\{C_F\}
$$

is an **intersecting antichain** on a \(2r\)-element ground set.

We need the following exact result.

### Milner’s intersecting-antichain theorem

If \(\mathcal J\subseteq 2^{[m]}\) is both intersecting and an antichain, then

$$
|\mathcal J|
\le
\binom{m}{\left\lceil (m+1)/2\right\rceil}.
$$

For \(m=2r\), this becomes

$$
|\mathcal J|
\le
\binom{2r}{r+1}
=
\binom{2r}{r-1}.
$$

A short shadow-and-cyclic-order proof of this exact theorem is standard; the proof below includes all needed steps. ([Mathematical Institute][1])

#### Proof of the theorem

For odd \(m\), the stated binomial coefficient is a middle-level coefficient, so ordinary Sperner already proves the result. It remains to consider

$$
m=2k.
$$

Take a maximum-cardinality intersecting antichain \(\mathcal J\). For a uniform family \(\mathcal A\subseteq\binom{[2k]}s\), let \(\partial^+\mathcal A\) and \(\partial^-\mathcal A\) denote its upper and lower shadows.

Double-counting incidences gives

$$
|\partial^+\mathcal A|(s+1)
\ge
|\mathcal A|(2k-s).
$$

Consequently,

$$
s<k\quad\Longrightarrow\quad
|\partial^+\mathcal A|\ge|\mathcal A|.
$$

Likewise,

$$
|\partial^-\mathcal A|(2k-s+1)
\ge
|\mathcal A|s,
$$

so

$$
s>k\quad\Longrightarrow\quad
|\partial^-\mathcal A|\ge|\mathcal A|.
$$

Suppose the minimum set size occurring in \(\mathcal J\) is \(s<k\). Replace its \(s\)-uniform part \(\mathcal J_s\) by \(\partial^+\mathcal J_s\).

This preserves intersection: two new sets contain intersecting members of \(\mathcal J_s\), and a new set contains an old \(A\in\mathcal J_s\), which intersects every untouched member.

It preserves the antichain property: if a new \((s+1)\)-set and an untouched old set were nested, the original \(s\)-set contained in the new set would be nested in that old set. The shadow is also disjoint from the untouched family for the same reason.

The cardinality does not decrease. Repeating, we may assume every member has size at least \(k\).

Now suppose the maximum set size is \(s>k+1\). Replace \(\mathcal J_s\) by \(\partial^-\mathcal J_s\). Every new set has size \(s-1\ge k+1\), while every untouched set has size at least \(k\). Thus any new set meets every untouched set simply because their sizes sum to more than \(2k\); any two new sets also intersect. The antichain property follows as before from the original antichain property. Cardinality again does not decrease.

Repeating gives a maximum family of the form

$$
\mathcal J=\mathcal J_k\cup\mathcal J_{k+1}.
$$

Let

$$
\mathcal G=\partial^+\mathcal J_k.
$$

The families \(\mathcal G\) and \(\mathcal J_{k+1}\) are disjoint, since a member of \(\mathcal J_{k+1}\) cannot contain a member of \(\mathcal J_k\).

It remains to prove

$$
|\mathcal G|\ge|\mathcal J_k|.
$$

Consider a cyclic order \(c\) of the \(2k\) ground points. Let \(f(c)\) be the number of members of \(\mathcal J_k\) that occur as cyclic intervals, and let \(g(c)\) be the number of members of \(\mathcal G\) occurring as cyclic \((k+1)\)-intervals.

The \(2k\) cyclic \(k\)-intervals come in \(k\) complementary pairs. Since \(\mathcal J_k\) is intersecting, it contains at most one interval from each pair. Hence

$$
f(c)\le k.
$$

Index the cyclic \(k\)-intervals by their starting positions. Each selected \(k\)-interval has two cyclic \((k+1)\)-interval extensions. If the selected start set is nonempty, its union with its one-step translate has at least one additional point, because it is a proper subset of the \(2k\)-cycle. Therefore

$$
g(c)\ge f(c)+1
$$

whenever \(f(c)>0\). Since \(f(c)\le k\),

$$
g(c)\ge \frac{k+1}{k}f(c)
$$

also when \(f(c)=0\).

A fixed \(k\)-set is a cyclic interval in

$$
(k!)^2
$$

cyclic orders, while a fixed \((k+1)\)-set is a cyclic interval in

$$
(k+1)!(k-1)!
$$

cyclic orders. Summing over all cyclic orders,

$$
(k+1)!(k-1)!\,|\mathcal G|
\ge
\frac{k+1}{k}(k!)^2|\mathcal J_k|.
$$

But

$$
\frac{k+1}{k}(k!)^2
=
(k+1)!(k-1)!,
$$

so

$$
|\mathcal G|\ge|\mathcal J_k|.
$$

Therefore

$$
\begin{aligned}
|\mathcal J|
&=
|\mathcal J_k|+|\mathcal J_{k+1}|\\
&\le
|\mathcal G|+|\mathcal J_{k+1}|\\
&\le
\binom{2k}{k+1}.
\end{aligned}
$$

This proves Milner’s bound.

Returning to \(\mathrm{Cross}(2r+1)\), Milner gives

$$
\omega(\mathrm{Cross}(2r+1))
\le
\binom{2r}{r+1}
=
\binom{2r}{r-1}.
$$

For equality, take all \(r\)-subsets \(A\subseteq T\) containing \(p\). Their number is

$$
\binom{2r}{r-1}.
$$

For distinct such \(A,B\),

$$
A\cap B\supseteq\{p\},
\qquad
A\setminus B\ne\varnothing,
\qquad
B\setminus A\ne\varnothing,
$$

and

$$
|T\setminus(A\cup B)|
=
2r+1-\bigl(2r-|A\cap B|\bigr)
=
1+|A\cap B|
\ge2.
$$

Thus all four cells are nonempty and

$$
\boxed{\omega(\mathrm{Cross}(2r+1))
=
\binom{2r}{r-1}}.
$$

Combining the parities,

$$
\boxed{
\omega(\mathrm{Cross}(t))
=
q(t)
=
\binom{t-1}{\lfloor t/2\rfloor-1}
}.
$$

### Strict monotonicity

For \(r\ge2\),

$$
\frac{q(2r+1)}{q(2r)}
=
\frac{\binom{2r}{r-1}}{\binom{2r-1}{r-1}}
=
\frac{2r}{r+1}
>1.
$$

For the other parity transition,

$$
\frac{q(2r+2)}{q(2r+1)}
=
\frac{\binom{2r+1}{r}}{\binom{2r}{r-1}}
=
\frac{2r+1}{r}
>1.
$$

Hence

$$
\boxed{q(t+1)>q(t)\qquad(t\ge4)}.
$$

In particular,

$$
\boxed{q(4)=3,\qquad q(5)=4,\qquad q(6)=10}.
$$

---

## 5. MIDDLE-LAYER INVARIANCE

Let

$$
T=[T_0],\qquad |T_0|=t\le b,
\qquad T_1=\Omega\setminus T_0.
$$

### Link upper bound

For a global partition \(R=\{R_0,R_1\}\), its restriction to \(T_0\) is the unordered cut

$$
\rho_T(R)
=
\{T_0\cap R_0,\ T_0\cap R_1\}.
$$

This does not depend on the orientation of \(R\), since reversing the orientation only swaps the two parts.

Let \(K\) be a clique in \(L_T\) with \(|K|\ge2\). For distinct \(R,S\in K\),

$$
\{T,R,S\}\in E(H_n).
$$

Restricting the eight Boolean cells to the block \(T_0\), all four cells

$$
T_0\cap R_i\cap S_j,
\qquad i,j\in\{0,1\},
$$

are nonempty. Thus \(\rho_T(R)\) and \(\rho_T(S)\) cross in \(T_0\).

They cannot induce the same unordered cut. Indeed, if their cuts were equal, orient them so that

$$
T_0\cap R_0=T_0\cap S_0.
$$

Then

$$
T_0\cap R_0\cap S_1
=
T_0\cap R_1\cap S_0
=
\varnothing,
$$

contradicting the hyperedge condition.

Therefore \(\rho_T\) injects every link clique of size at least two into a clique in \(\mathrm{Cross}(t)\). Cliques of size at most one already satisfy the desired numerical bound because \(q(t)\ge q(4)=3\). Hence

$$
\boxed{\omega(L_T)\le q(t)}.
$$

### Repaired middle-layer lower bound

Let \(T\in B_n\), with blocks \(T_0,T_1\) of sizes

$$
|T_0|=b,\qquad |T_1|=n-b.
$$

For a finite set \(A\) of size \(s\ge4\), fix \(p_A\in A\) and use the explicit maximum crossing family

$$
\mathcal C(A)
=
\left\{
[U]_A:
p_A\in U,\quad |U|=\left\lfloor\frac s2\right\rfloor
\right\}.
$$

Gate 1 shows

$$
|\mathcal C(A)|=q(s).
$$

On \(T_0\), take all of \(\mathcal C(T_0)\), of size \(q(b)\).

If \(n\) is even, \(|T_1|=b\), so take all of \(\mathcal C(T_1)\).

If \(n\) is odd, \(|T_1|=b+1\), and

$$
|\mathcal C(T_1)|=q(b+1)>q(b).
$$

Take any \(q(b)\)-element subfamily

$$
\mathcal C'(T_1)\subseteq\mathcal C(T_1).
$$

Now pair \(\mathcal C(T_0)\) bijectively with \(\mathcal C'(T_1)\). Write the paired oriented local sides as

$$
A_j\subseteq T_0,\qquad C_j\subseteq T_1,
$$

and define the global vertex

$$
W_j=[A_j\cup C_j].
$$

Every \(W_j\) is valid because

$$
|A_j|=\left\lfloor\frac{|T_0|}{2}\right\rfloor\ge2,
\qquad
|C_j|=\left\lfloor\frac{|T_1|}{2}\right\rfloor\ge2,
$$

so

$$
|A_j\cup C_j|\ge4.
$$

Its complementary block has size

$$
\left\lceil\frac{|T_0|}{2}\right\rceil
+
\left\lceil\frac{|T_1|}{2}\right\rceil
\ge4.
$$

The boundary cases are:

$$
\begin{array}{c|c|c|c}
n&( |T_0|,|T_1|)&|A_j\cup C_j|&
|(A_j\cup C_j)^c|\\ \hline
8&(4,4)&4&4\\
9&(4,5)&4&5\\
10&(5,5)&4&6
\end{array}
$$

For \(i\ne j\), the cuts \(A_i,A_j\) cross in \(T_0\), and \(C_i,C_j\) cross in \(T_1\). Thus, for each of the two \(T\)-blocks and each pair of membership bits in \(W_i,W_j\), the corresponding cell is nonempty. Hence

$$
\{T,W_i,W_j\}\in E(H_n).
$$

The global vertices are distinct. If

$$
[A_i\cup C_i]=[A_j\cup C_j],
$$

restriction to \(T_0\) would give the same unordered local cut

$$
[A_i]_{T_0}=[A_j]_{T_0},
$$

forcing \(i=j\).

Thus \(\{W_j\}\) is a clique of size \(q(b)\) in \(L_T\), and the upper bound gives

$$
\boxed{\omega(L_T)=q(b)\qquad(T\in B_n)}.
$$

### Endomorphisms do not move a middle vertex out of the middle layer

First note that every link \(L_T\) contains an edge. Select four points in each block of \(T\), colour them \(00,01,10,11\), and colour all remaining points \(00\). The two bit-coordinate cuts are valid \(H_n\)-vertices and, together with \(T\), form an edge. Hence every maximum link clique has size at least two.

Let \(K\) be a maximum clique in \(L_T\). If \(R,S\in K\) are distinct, then

$$
\{T,R,S\}\in E(H_n),
$$

so

$$
\{f(T),f(R),f(S)\}\in E(H_n).
$$

In particular, \(f(T),f(R),f(S)\) are distinct. It follows that \(f\) is injective on \(K\), no image vertex equals \(f(T)\), and \(f(K)\) is a clique in \(L_{f(T)}\). Therefore

$$
\omega(L_T)\le\omega(L_{f(T)}).
$$

Now let \(T\in B_n\), and let the smaller block size of \(f(T)\) be \(t'\le b\). Then

$$
q(b)
=
\omega(L_T)
\le
\omega(L_{f(T)})
\le
q(t').
$$

Since \(q\) is strictly increasing and \(t'\le b\), necessarily

$$
t'=b.
$$

Thus \(f(T)\) is again a middle-layer vertex:

$$
\boxed{f(B_n)\subseteq B_n}.
$$

---

## 6. DIRECTED BALANCED-ANCHOR SEPARATION

Let

$$
X=\{X_0,X_1\},
\qquad
Y=\{Y_0,Y_1\}
$$

be distinct unordered partitions.

### Choice of the obstructing \(Y\)-block

Suppose neither block of \(Y\) meets both blocks of \(X\). Then each \(Y_j\) is contained in one \(X_i\). Since \(Y_0\cup Y_1=\Omega\) and both \(X\)-blocks are nonempty, the two \(Y\)-blocks must be contained in different \(X\)-blocks.

If, after relabelling,

$$
Y_0\subseteq X_0,\qquad Y_1\subseteq X_1,
$$

then every point of \(X_0\) lies in \(Y_0\), because it cannot lie in \(Y_1\subseteq X_1\). Hence \(X_0=Y_0\), and similarly \(X_1=Y_1\). This contradicts \(X\ne Y\).

Therefore some block \(E\in Y\) meets both \(X_0\) and \(X_1\). Let

$$
D=E^c,
$$

the other block of \(Y\). Then

$$
D^c\cap X_0\ne\varnothing,
\qquad
D^c\cap X_1\ne\varnothing.
$$

### Partial colouring

For \(i=0,1\), choose

$$
p_i\in X_i\cap D^c
$$

and assign \(p_i\) the colour \(11\).

Because every \(X_i\) has size at least \(4\), choose three further distinct points in \(X_i\) and assign them the colours

$$
00,\qquad 01,\qquad 10.
$$

The eight selected points are all distinct. At this stage, every \(X_i\) contains all four colours, and the global partial colour counts are

$$
(2,2,2,2).
$$

### Completion of the colouring

For \(n=2k\), the target multiplicities are

$$
(2,k-2,k-2,2).
$$

The deficits after the partial colouring are

$$
(0,k-4,k-4,0).
$$

They are nonnegative for \(k\ge4\), and their sum is

$$
2k-8=n-8,
$$

exactly the number of uncoloured points.

For \(n=2k+1\), the target multiplicities are

$$
(3,k-2,k-2,2).
$$

The deficits are

$$
(1,k-4,k-4,0),
$$

again nonnegative for \(k\ge4\), with total

$$
1+2(k-4)=2k-7=n-8.
$$

Thus every remaining point can be coloured arbitrarily according to these deficits.

The boundary cases are

$$
\begin{array}{c|c|c}
n&\text{target multiplicities}&\text{deficits after the first eight points}\\ \hline
8&(2,2,2,2)&(0,0,0,0)\\
9&(3,2,2,2)&(1,0,0,0)\\
10&(2,3,3,2)&(0,1,1,0)
\end{array}
$$

If an \(X_i\) has size exactly \(4\), its four points are precisely the four initially selected points and it already contains one point of every colour. No additional local capacity is needed.

Define

$$
R=\{x:c(x)\in\{10,11\}\},
\qquad
S=\{x:c(x)\in\{01,11\}\}.
$$

### Verification of all required properties

For even \(n=2k\),

$$
|R|=c_{10}+c_{11}=(k-2)+2=k,
$$

and similarly \(|S|=k\). Thus \(R,S\in B_n\).

For odd \(n=2k+1\),

$$
|R|=|S|=k,
$$

and their complements have size \(k+1\), so again \(R,S\in B_n\).

The two unordered partitions are distinct. Since

$$
c_{10}=c_{01}=k-2>0,
$$

we have \(R\ne S\). Moreover,

$$
c_{11}=2>0,\qquad c_{00}\ge2,
$$

so \(R\ne S^c\). Hence

$$
[R]\ne[S].
$$

Every block \(X_i\) contains all four colours. Therefore, for both choices of the \(X\)-block and all four pairs of \(R,S\)-membership bits, the corresponding cell is nonempty. Thus

$$
\{X,[R],[S]\}\in E(H_n).
$$

The only points coloured \(11\) are \(p_0,p_1\), and both lie in \(D^c\). Consequently,

$$
D\cap R\cap S=\varnothing.
$$

Since \(D\) is a block of \(Y\), this is one empty Boolean cell for the triple \(Y,[R],[S]\). Therefore

$$
\{Y,[R],[S]\}\notin E(H_n).
$$

This construction works for every ordered pair \(X\ne Y\), so

$$
\boxed{I(X)\not\subseteq I(Y)\qquad(X\ne Y)}.
$$

This proves directed separation, not merely signature inequality or injectivity.

---

## 7. FINITE CHECK n=10,11,12

### SYMBOLIC STATUS

**VALID after the Gate 2 repair.**

Gate 4 has been proved symbolically for every \(n\ge8\); the finite calculations below are consistency checks only.

### Orbit enumeration

An ordered pair of unordered partitions is determined up to \(S_n\) by the cell-count matrix

$$
M=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
=
\begin{pmatrix}
|X_0\cap Y_0|&|X_0\cap Y_1|\\
|X_1\cap Y_0|&|X_1\cap Y_1|
\end{pmatrix}.
$$

The entries are nonnegative and sum to \(n\). Row and column sums must each be at least \(4\). Because the two partitions are unordered, matrices are identified under independent row and column swaps:

$$
(a,b,c,d),\quad
(c,d,a,b),\quad
(b,a,d,c),\quad
(d,c,b,a).
$$

The cases

$$
b=c=0
\quad\text{or}\quad
a=d=0
$$

are excluded because they represent \(X=Y\).

Lexicographic canonicalization under these four transformations gives exactly:

$$
\begin{array}{c|c}
n&\text{ordered-pair orbits}\\ \hline
10&12\\
11&19\\
12&34
\end{array}
$$

For every canonical matrix, two independent checks were performed:

1. the prescribed Gate 4 colouring was instantiated and all multiplicity, middle-layer, distinctness, eight-cell, and obstructing-cell assertions were checked;
2. all eligible middle-layer anchor pairs were scanned directly until a pair satisfying the directed condition was found.

The direct search sizes were:

$$
\begin{array}{c|c|c|c|c}
n&|B_n|&
\text{eligible unordered anchor pairs}&
\text{orbits with direct witness}&
\text{Gate 4 construction passes}\\ \hline
10&126&7{,}875&12/12&12/12\\
11&462&105{,}105&19/19&19/19\\
12&462&106{,}491&34/34&34/34
\end{array}
$$

“Eligible” means that the four \(R,S\)-colour cells are all nonempty, a necessary condition for \(\{X,R,S\}\) to be an edge.

There were no failures.

### Crossing-clique values

The exact crossing graphs were also exhaustively generated by orienting every cut toward one fixed point. The computational data are

$$
\begin{array}{c|c|c|c}
t&|V(\mathrm{Cross}(t))|&|E(\mathrm{Cross}(t))|&
\omega(\mathrm{Cross}(t))\\ \hline
4&7&3&3\\
5&15&30&4\\
6&31&195&10
\end{array}
$$

Thus the finite clique values agree with

$$
\boxed{q(4)=3,\qquad q(5)=4,\qquad q(6)=10}.
$$

### FINITE STATUS

**PASS.**

All \(12\), \(19\), and \(34\) ordered-pair orbits admit directed middle-layer anchors. No comparison of signature sizes was used.

---

## 8. POWER-TRICK AND FINAL DEDUCTION

Assume \(B_n\) is a core, and let

$$
f:H_n\longrightarrow H_n
$$

be an endomorphism.

By middle-layer invariance,

$$
f(B_n)\subseteq B_n.
$$

Hence the restriction

$$
g=f|_{B_n}
$$

is an endomorphism of \(B_n\): an edge of \(B_n\) is an \(H_n\)-edge whose vertices lie in \(B_n\), and its image is again an \(H_n\)-edge with all three image vertices in \(B_n\).

Since \(B_n\) is a core, \(g\) is an automorphism. Because \(B_n\) is finite, \(g\) has finite order. Let

$$
d=\operatorname{ord}(g)
$$

and define

$$
h=f^d.
$$

Because every iterate of \(f\) preserves \(B_n\),

$$
h|_{B_n}
=
g^d
=
\mathrm{id}_{B_n}.
$$

No automorphism-group classification and no extension theorem are being used.

Suppose for contradiction that some \(X\in V(H_n)\) satisfies

$$
h(X)=Y\ne X.
$$

Directed separation supplies distinct \(R,S\in B_n\) with

$$
\{X,R,S\}\in E(H_n),
\qquad
\{Y,R,S\}\notin E(H_n).
$$

But \(h\) fixes \(B_n\) pointwise, so

$$
h(R)=R,\qquad h(S)=S.
$$

Applying \(h\) to the source edge gives

$$
\{h(X),h(R),h(S)\}
=
\{Y,R,S\}\in E(H_n),
$$

contradicting the choice of \(R,S\). Therefore

$$
h=\mathrm{id}_{H_n}.
$$

Since \(h=f^d\),

$$
f^d=\mathrm{id}_{H_n}.
$$

It follows that

$$
f^{d-1}\circ f=f^d=\mathrm{id},
\qquad
f\circ f^{d-1}=f^d=\mathrm{id}.
$$

Thus \(f\) is bijective, with inverse \(f^{d-1}\). Moreover \(f^{d-1}\), being a power of an endomorphism, is itself an endomorphism. Hence \(f\) is an automorphism.

Every endomorphism of \(H_n\) is therefore an automorphism.

---

## 9. FINAL THEOREM ACTUALLY ESTABLISHED

After the stated Gate 2 repair, the following theorem is proved for every integer \(n\ge8\):

$$
\boxed{
B_n\text{ is a core}
\quad\Longrightarrow\quad
H_n=3\text{-}\mathrm{QI}(n,2)\text{ is a core}.
}
$$

The proof uses:

$$
\omega(\mathrm{Cross}(t))=q(t),
$$

strict monotonicity of \(q\), repaired middle-link equality

$$
\omega(L_T)=q(b)\qquad(T\in B_n),
$$

middle-layer invariance under all endomorphisms, the power trick, and the symbolic directed-separation theorem

$$
I(X)\not\subseteq I(Y)\qquad(X\ne Y).
$$

---

## 10. REPAIRS

**R1 — mandatory odd-\(n\) repair.**
For \(n=2k+1\), replace “pair maximum families on both blocks bijectively” by:

$$
\text{maximum }q(k)\text{-family on the }k\text{-block}
$$

paired with

$$
\text{a }q(k)\text{-element subfamily of a maximum }q(k+1)\text{-family}
$$

on the \((k+1)\)-block.

**R2 — quantifier-safe link-clique formulation.**
If the link graph is regarded as having all vertices of \(H_n\setminus\{T\}\), including isolated vertices, the statement that *every* singleton clique maps into the target link need not be justified by edge preservation. The exact needed statement is:

$$
\text{every link clique of size at least two maps injectively to a link clique.}
$$

Every \(L_T\) contains an edge, so this applies to maximum cliques and proves the required clique-number monotonicity.

**R3 — unordered-vertex distinctness made explicit.**
It is not enough to check only \(R\ne S\) as oriented subsets. One must also exclude \(R=S^c\). The construction does so because the \(00\)- and \(11\)-classes are both nonempty, while the \(01\)- and \(10\)-classes are both nonempty. Therefore

$$
[R]\ne[S].
$$

Q_FORMULA =
VALID

MIDDLE_INVARIANCE =
VALID

SEPARATION =
VALID

POWER_TRICK =
VALID

VERDICT =
VALID-AFTER-REPAIR

[1]: https://people.maths.ox.ac.uk/scott/Papers/milnershort.pdf?utm_source=chatgpt.com "https://people.maths.ox.ac.uk/scott/Papers/milnershort.pdf"
