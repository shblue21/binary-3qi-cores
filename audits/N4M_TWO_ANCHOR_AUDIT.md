## 1. OVERALL VERDICT

**VALID-AFTER-REPAIR**

The two-anchor construction and the critical-fold argument do establish

$$
\boxed{3\text{-}\mathrm{UQI}(4m,2)\text{ is a core for every integer }m\ge 4,}
$$

but the submitted note contains one false numerical statement in Gate 6: in the \(D_{11}\) case, the literal minimum of the seven required atom sizes is not \(m-3\) for all \(m\ge4\). The actual minimum is

$$
\min\{1,m-3\}=1\qquad(m\ge4).
$$

The two atoms of size \(m-3\) are nevertheless the only potentially vanishing atoms, so the claimed threshold \(m\ge4\) remains correct. No structural change to the construction is needed. The false minimum statement appears explicitly in the submitted note. 

---

## 2. FIRST ERROR — gate and exact formula

**Gate 6, \(D_{11}\) exceptional row.**

The submission asserts, in effect,

$$
\min\bigl(
|000|,|001|,|010|,|011|,|100|,|101|,|110|
\bigr)=m-3.
$$

The independently derived \(D_{11}\) row, with bit order \((P,E,R_A)\), is

$$
\boxed{
(000,001,010,011,100,101,110)
=
(2,1,m-3,m,m,m-3,1).
}
$$

Therefore

$$
\boxed{
\min(2,1,m-3,m,m,m-3,1)=\min\{1,m-3\}.
}
$$

Consequently:

$$
\min=1\quad\text{for every }m\ge4,
$$

not \(m-3\) unless \(m=4\). At \(m=3\), the \(010\) and \(101\) atoms both have size zero, so the construction indeed fails at that boundary.

There is **no earlier false implication** in Gates 1–5.

---

## 3. GATE TABLE — Gates 1–8

| Gate | Status        | Audit finding                                                                                                                               |
| ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **VALID**     | Exact finite model, hyperedge criterion, and 2-section characterization all hold.                                                           |
| 2    | **VALID**     | The two finite nonedge types merge into one orbit under the full \(S_{4m}\)-action; all normalization steps hold.                           |
| 3    | **VALID**     | Link traces form an injective antichain; Sperner gives the claimed bound.                                                                   |
| 4    | **VALID**     | All three type counts are correct; the classes are disjoint and exhaustive; the union of typewise bijections is a genuine global bijection. |
| 5    | **VALID**     | Every distinct central pair has the \(Q\)-anchor; all seven atom sizes are positive.                                                        |
| 6    | **INVALID**   | The three anchor assertions are correct, but the claimed \(D_{11}\) minimum \(m-3\) is false as a literal minimum.                          |
| 7    | **VALID**     | An independent exact \(m=4\) construction passes all \(630\) anchor checks.                                                                 |
| 8    | **DEPENDENT** | The fold argument is valid once Gate 6 is repaired; the repaired Gate 6 supplies every required anchor edge.                                |

### Gate 1 — exact object and 2-section

Let \(U\) be a set of size \(4m\), and fix \(\infty\in U\). Put

$$
\Omega=U\setminus\{\infty\},
\qquad |\Omega|=4m-1.
$$

A vertex is an unordered balanced bipartition

$$
\{C,U\setminus C\},\qquad |C|=2m.
$$

Exactly one of the two classes contains \(\infty\). Write that class uniquely as

$$
\widehat X=\{\infty\}\cup X,
\qquad X\subseteq\Omega,\quad |X|=2m-1.
$$

Conversely, every \(X\in\binom{\Omega}{2m-1}\) determines the unordered partition

$$
\bigl\{\{\infty\}\cup X,\ \Omega\setminus X\bigr\}.
$$

Thus

$$
\boxed{
V(H_m)=\binom{\Omega}{2m-1}.
}
$$

For three vertices \(X,Y,Z\), orient their partition classes toward the classes containing \(\infty\). For \(\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)\in\{0,1\}^3\), let the finite Boolean atom be

$$
A_\epsilon
=
X^{\epsilon_1}\cap Y^{\epsilon_2}\cap Z^{\epsilon_3}
\subseteq\Omega,
$$

where \(X^1=X\) and \(X^0=\Omega\setminus X\), and similarly for \(Y,Z\).

In the full \(4m\)-point space, the \(111\) atom is

$$
\{\infty\}\cup(X\cap Y\cap Z),
$$

so it is automatically nonempty. Every other full atom lies in \(\Omega\) and equals the corresponding finite atom. Hence

$$
\boxed{
\{X,Y,Z\}\in E(H_m)
\iff
A_\epsilon\ne\varnothing
\quad\text{for all }\epsilon\ne111.
}
$$

The homomorphism convention is the strict relational one: \(H_m\) is a simple, irreflexive \(3\)-uniform hypergraph with

$$
E(H_m)\subseteq\binom{V(H_m)}3.
$$

An endomorphism \(f\) must satisfy

$$
\{X,Y,Z\}\in E(H_m)
\Longrightarrow
\{f(X),f(Y),f(Z)\}\in E(H_m).
$$

In particular, the three images of a hyperedge must remain pairwise distinct.

Now put

$$
r=2m-1
$$

and take distinct \(X,Y\in\binom{\Omega}{r}\). Let

$$
a=|X\cap Y|.
$$

The four regions determined by \(X,Y\) have sizes

$$
\begin{aligned}
|X\cap Y|&=a,\\
|X\setminus Y|&=r-a,\\
|Y\setminus X|&=r-a,\\
|\Omega\setminus(X\cup Y)|
&=(4m-1)-(2r-a)=a+1.
\end{aligned}
$$

If some \(Z\) completes \(X,Y\) to a hyperedge, then:

* \(X\cap Y\setminus Z\ne\varnothing\), so \(a\ge1\);
* both \(X\setminus Y\) atoms, according to membership in \(Z\), must be nonempty, so \(r-a\ge2\);
* the same holds for \(Y\setminus X\).

Therefore

$$
1\le a\le r-2=2m-3.
$$

Conversely, suppose \(1\le a\le r-2\). Choose \(Z\) with the following numbers of elements from the four pair-regions:

$$
\begin{array}{c|c|c}
\text{region}&\text{region size}&\text{number chosen into }Z\\ \hline
X\cap Y&a&0\\
X\setminus Y&r-a&1\\
Y\setminus X&r-a&r-a-1\\
\Omega\setminus(X\cup Y)&a+1&a
\end{array}
$$

All four choices are possible under \(1\le a\le r-2\), and

$$
|Z|=0+1+(r-a-1)+a=r.
$$

The seven required atom sizes are then

$$
(000,001,010,011,100,101,110)
=
(1,a,1,r-a-1,r-a-1,1,a),
$$

all positive. Hence

$$
\boxed{
X\sim_{[H_m]_2}Y
\iff
1\le |X\cap Y|\le2m-3.
}
$$

### Gate 2 — collision orbit and normalization

Distinct \(r\)-subsets have intersection at most \(r-1=2m-2\). Gate 1 therefore gives

$$
X\not\sim_{[H_m]_2}Y,\quad X\ne Y
\iff
|X\cap Y|\in\{0,2m-2\}.
$$

It remains essential to use the full \(S_{4m}\)-action, not merely the stabilizer \(S_\Omega\).

Let

$$
k=2m,
\qquad
\widehat X=\{\infty\}\cup X,
\qquad
\widehat Y=\{\infty\}\cup Y.
$$

Then \(|\widehat X|=|\widehat Y|=k\), and if

$$
d=|\widehat X\cap\widehat Y|=1+|X\cap Y|,
$$

the four cells determined by \(\widehat X,\widehat Y\) have sizes

$$
(d,k-d,k-d,d).
$$

Because each bipartition is unordered, replacing \(\widehat Y\) by its complement represents the same vertex and replaces \(d\) by \(k-d\).

For a finite nonedge:

$$
|X\cap Y|=0
\Longrightarrow d=1,
$$

while

$$
|X\cap Y|=2m-2=k-2
\Longrightarrow d=k-1.
$$

The values \(1\) and \(k-1\) are interchanged by complementing one partition class. Thus in both cases the two unordered partitions can be oriented so that the four cell sizes are

$$
(k-1,1,1,k-1).
$$

Any two pairs of oriented subsets with these four cell sizes are carried to each other by a permutation of \(U\), obtained by mapping each cell bijectively to the corresponding cell. Relabeling points preserves qualitative independence, so \(S_U=S_{4m}\) acts by automorphisms of \(H_m\).

For

$$
\Omega=K\sqcup\{p,q\}\sqcup W,
\quad |K|=2m-2,
\quad |W|=2m-1,
$$

put

$$
P=K\cup\{p\},
\qquad
Q=K\cup\{q\}.
$$

Their \(\infty\)-containing classes have cells

$$
\begin{aligned}
\widehat P\cap\widehat Q&=\{\infty\}\cup K,
&&\text{size }2m-1=k-1,\\
\widehat P\setminus\widehat Q&=\{p\},
&&\text{size }1,\\
\widehat Q\setminus\widehat P&=\{q\},
&&\text{size }1,\\
U\setminus(\widehat P\cup\widehat Q)&=W,
&&\text{size }2m-1=k-1.
\end{aligned}
$$

Therefore every distinct 2-section nonedge lies in the orbit of \(\{P,Q\}\).

Now let \(f\) be an endomorphism.

1. If \(X,Y\) form a 2-section edge, there is a \(Z\) with \(\{X,Y,Z\}\in E(H_m)\). If \(f(X)=f(Y)\), the image would not be a three-element hyperedge. Hence \(f\) cannot identify a 2-section edge.

2. If \(f\) is noninjective, choose \(X\ne Y\) with \(f(X)=f(Y)\). They are a 2-section nonedge. By the orbit result, there is \(\alpha\in\operatorname{Aut}(H_m)\) with

   $$
   \{\alpha(P),\alpha(Q)\}=\{X,Y\}.
   $$

   Thus \(g=f\circ\alpha\) satisfies

   $$
   g(P)=g(Q).
   $$

3. The \(S_{4m}\)-action is vertex-transitive. If \(T=g(P)=g(Q)\) and \(T_0\) is any fixed vertex, there is \(\beta\in\operatorname{Aut}(H_m)\) with \(\beta(T)=T_0\). Then

   $$
   h=\beta\circ g
   $$

   has \(h(P)=h(Q)=T_0\).

4. Suppose auxiliary vertices \(R,S\) satisfy

   $$
   \{P,R,S\}\in E(H_m)
   \quad\text{or}\quad
   \{Q,R,S\}\in E(H_m).
   $$

   Under a normalized endomorphism with \(f(P)=f(Q)=T\), either case gives

   $$
   \{T,f(R),f(S)\}\in E(H_m).
   $$

   Irreflexivity implies

   $$
   f(R)\ne f(S),\qquad f(R)\ne T,\qquad f(S)\ne T.
   $$

   Thus the images are distinct vertices in the link \(L_T\), and \(f(R)f(S)\) is an edge of \(L_T\).

### Gate 3 — link–Sperner bound

Fix \(T\in V(H_m)\), and let \(\mathcal C\) be a clique in \(L_T\). For distinct \(R,S\in\mathcal C\),

$$
\{T,R,S\}\in E(H_m).
$$

Using bit order \((T,R,S)\), the \(110\) atom is

$$
T\cap R\cap(\Omega\setminus S)
=
(T\cap R)\setminus(T\cap S),
$$

and the \(101\) atom is

$$
T\cap(\Omega\setminus R)\cap S
=
(T\cap S)\setminus(T\cap R).
$$

Both must be nonempty. Therefore

$$
(T\cap R)\setminus(T\cap S)\ne\varnothing,
\qquad
(T\cap S)\setminus(T\cap R)\ne\varnothing.
$$

So neither trace contains the other:

$$
T\cap R\nsubseteq T\cap S,
\qquad
T\cap S\nsubseteq T\cap R.
$$

In particular, the trace map

$$
R\longmapsto T\cap R
$$

is injective on \(\mathcal C\), and its image is an antichain in \(2^T\). Since

$$
|T|=2m-1,
$$

Sperner’s theorem gives

$$
|\mathcal C|
\le
\binom{2m-1}{\lfloor(2m-1)/2\rfloor}
=
\binom{2m-1}{m-1}.
$$

Hence

$$
\boxed{
\omega(L_T)\le M_m:=\binom{2m-1}{m-1}.
}
$$

### Gate 4 — type counts and complement-pair bijection

Let

$$
Q=K\cup\{q\},
\qquad |Q|=2m-1,
$$

and consider \(A\in\binom Q{m-1}\).

For \(D_0\), exclude \(x\) and choose all \(m-1\) elements from \(Q\setminus\{x\}\), which has size \(2m-2\):

$$
|D_0|=\binom{2m-2}{m-1}.
$$

For \(D_{10}\), include \(x\), exclude \(q\), and choose the remaining \(m-2\) elements from \(K\setminus\{x\}\), of size \(2m-3\):

$$
|D_{10}|=\binom{2m-3}{m-2}.
$$

For \(D_{11}\), include \(x,q\) and choose the remaining \(m-3\) elements from \(K\setminus\{x\}\):

$$
|D_{11}|=\binom{2m-3}{m-3}.
$$

These classes are disjoint and exhaustive: either \(x\notin A\), or \(x\in A\), and in the latter case exactly one of \(q\notin A\) and \(q\in A\) holds.

Now

$$
O=\{p\}\cup W,
\qquad |O|=2m.
$$

Every complement pair

$$
[B]=\{B,O\setminus B\},
\qquad |B|=m,
$$

has a unique \(p\)-free representative \(F\): precisely one of \(B,O\setminus B\) contains \(p\). Thus complement pairs are in bijection with

$$
F\in\binom Wm.
$$

Write

$$
W_0=W\setminus\{u,v\},
\qquad |W_0|=2m-3.
$$

For \(C_0\), \(F\) contains exactly one of \(u,v\). Therefore

$$
|C_0|
=
2\binom{2m-3}{m-1}.
$$

By symmetry,

$$
\binom{2m-3}{m-1}
=
\binom{2m-3}{m-2},
$$

so Pascal’s identity gives

$$
|C_0|
=
\binom{2m-3}{m-1}
+
\binom{2m-3}{m-2}
=
\binom{2m-2}{m-1}.
$$

For \(C_{10}\), the \(p\)-free representative contains both \(u,v\), leaving \(m-2\) choices from \(W_0\):

$$
|C_{10}|=\binom{2m-3}{m-2}.
$$

For \(C_{11}\), it contains neither \(u,v\), so it is an \(m\)-subset of \(W_0\):

$$
|C_{11}|
=
\binom{2m-3}{m}
=
\binom{2m-3}{m-3}.
$$

The \(C\)-classes are disjoint and exhaustive because the unique \(p\)-free representative contains zero, one, or two members of \(\{u,v\}\). Hence the verified counts are

$$
\begin{array}{c|ccc}
&0&10&11\\ \hline
|D_\bullet|
&
\binom{2m-2}{m-1}
&
\binom{2m-3}{m-2}
&
\binom{2m-3}{m-3}\\[2mm]
|C_\bullet|
&
\binom{2m-2}{m-1}
&
\binom{2m-3}{m-2}
&
\binom{2m-3}{m-3}.
\end{array}
$$

Choose bijections

$$
\phi_i:D_i\longrightarrow C_i
\qquad(i\in\{0,10,11\}).
$$

Because the \(D_i\) partition the complete \(A\)-set and the \(C_i\) partition the complete complement-pair set, the union

$$
\phi=\phi_0\cup\phi_{10}\cup\phi_{11}
$$

is well-defined. It is injective because the \(\phi_i\) are injective and their codomains are disjoint; it is surjective because each \(C_i\) is covered by \(\phi_i\). Thus it is a genuine bijection on the complete sets, not merely three unrelated cardinality matches.

For \(A\in D_0\), choose either representative of \(\phi(A)\). For \(A\in D_{10}\cup D_{11}\), choose its unique \(p\)-free representative. Call the result \(B_A\), and put

$$
R_A=A\cup B_A.
$$

Since \(A\subseteq Q\), \(B_A\subseteq O\), and \(Q\cap O=\varnothing\),

$$
|R_A|=(m-1)+m=2m-1.
$$

Thus every \(R_A\) is a vertex. Moreover,

$$
R_A\cap Q=A,
$$

so \(A\ne A'\) implies \(R_A\ne R_{A'}\).

### Gate 5 — every central pair has the \(Q\)-anchor

Take distinct \(A,A'\), and abbreviate

$$
B=B_A,\qquad B'=B_{A'},\qquad
s=|A\cap A'|,\qquad t=|B\cap B'|.
$$

Because \(A,A'\) are distinct \((m-1)\)-subsets,

$$
0\le s\le m-2.
$$

The assigned complement pairs \([B]\) and \([B']\) are distinct because the global assignment \(\phi\) is injective. Consequently:

* \(B\ne B'\), since equality would give \([B]=[B']\);
* \(B\ne O\setminus B'\), since complementarity would also give \([B]=[B']\).

Both \(B,B'\) are \(m\)-subsets of the \(2m\)-set \(O\). If \(t=m\), then \(B=B'\), impossible. If \(t=0\), then \(B\) and \(B'\) are disjoint \(m\)-subsets whose union is all of \(O\), so they are complementary, also impossible. Therefore

$$
\boxed{1\le t\le m-1.}
$$

With bit order \((Q,R_A,R_{A'})\), the seven required atoms have sizes

$$
(t,m-t,m-t,t,s+1,m-1-s,m-1-s).
$$

Indeed, outside \(Q\), the relevant sets are \(B,B'\), giving

$$
\begin{aligned}
000&=|O\setminus(B\cup B')|=t,\\
001&=|B'\setminus B|=m-t,\\
010&=|B\setminus B'|=m-t,\\
011&=|B\cap B'|=t.
\end{aligned}
$$

Inside \(Q\), the relevant sets are \(A,A'\), giving

$$
\begin{aligned}
100&=|Q\setminus(A\cup A')|
=(2m-1)-(2m-2-s)=s+1,\\
101&=|A'\setminus A|=m-1-s,\\
110&=|A\setminus A'|=m-1-s.
\end{aligned}
$$

All are positive under the displayed bounds. Thus

$$
\boxed{
\{Q,R_A,R_{A'}\}\in E(H_m)
\quad\text{for every }A\ne A'.
}
$$

This argument is independent of the exceptional type of either \(A\).

### Gate 6 — exceptional vertex tables

Define

$$
E=\{x,p\}\cup(W\setminus\{u,v\}).
$$

Since \(|W\setminus\{u,v\}|=2m-3\),

$$
|E|=2+(2m-3)=2m-1,
$$

so \(E\) is a vertex.

For \(D_0\), use anchor \(Q\). Here

$$
Q\cap E=\{x\},
\qquad x\notin A.
$$

Thus the \(110\) atom is \(\{x\}\). All \(m-1\) elements of \(A\) lie in \(Q\setminus E\), producing \(101=m-1\), while the remaining part of \(Q\setminus E\) produces \(100=m-1\).

Outside \(Q\),

$$
O\setminus E=\{u,v\}.
$$

A type-\(0\) representative contains exactly one of \(u,v\), regardless of which representative of its complement pair was selected. Hence \(000=001=1\), and \(B_A\) has exactly \(m-1\) elements in \(E\cap O\), giving \(010=011=m-1\).

Therefore

$$
\{Q,E,R_A\}\in E(H_m).
$$

For \(D_{10}\), use anchor \(P\). Here \(A\) contains \(x\), excludes \(q\), and \(B_A\) is \(p\)-free and contains \(u,v\). We have

$$
P\cap E=\{x,p\}.
$$

Of these, \(x\in R_A\) and \(p\notin R_A\), giving \(111=1\) and \(110=1\). Among \(K\setminus\{x\}\), exactly \(m-2\) elements lie in \(A\), giving \(101=m-2\), and \(m-1\) do not, giving \(100=m-1\).

Outside \(P\),

$$
(\Omega\setminus P)\setminus E=\{q,u,v\}.
$$

The vertex \(R_A\) contains \(u,v\) but not \(q\), so \(001=2\) and \(000=1\). In \(W\setminus\{u,v\}\), \(B_A\) contains \(m-2\) elements and excludes \(m-1\), giving \(011=m-2\) and \(010=m-1\). Thus

$$
\{P,E,R_A\}\in E(H_m).
$$

For \(D_{11}\), again use anchor \(P\). Now \(A\) contains \(x,q\), while \(B_A\) is \(p\)-free and excludes \(u,v\). As before, \(x\) contributes to \(111\) and \(p\) to \(110\).

Among \(K\setminus\{x\}\), exactly \(m-3\) elements lie in \(A\), so

$$
101=m-3,
\qquad
100=(2m-3)-(m-3)=m.
$$

The set \(B_A\) consists of \(m\) elements of \(W\setminus\{u,v\}\), so

$$
011=m,
\qquad
010=(2m-3)-m=m-3.
$$

Finally, among \(\{q,u,v\}\), \(R_A\) contains exactly \(q\), giving

$$
001=1,\qquad 000=2.
$$

Thus the triple is a hyperedge exactly when \(m-3>0\), and in particular for every \(m\ge4\):

$$
\{P,E,R_A\}\in E(H_m).
$$

The edge assertion is valid. The error is solely the stated literal minimum.

### Gate 7 — independent \(m=4\) consistency check

At \(m=4\),

$$
M_4=\binom73=35.
$$

The exact type sizes are

$$
\binom63=20,\qquad
\binom52=10,\qquad
\binom51=5.
$$

An independently instantiated typewise bijection gives \(35\) distinct central vertices. Direct membership enumeration, without using the symbolic atom formulas, verifies all

$$
\binom{35}{2}+35=595+35=630
$$

required anchor triples. The code and complete output appear in Section 5.

### Gate 8 — fold contradiction and core conclusion

Set

$$
\mathcal R
=
\{E\}\cup
\{R_A:A\in\textstyle\binom Q{m-1}\}.
$$

The central vertices are pairwise distinct. Also

$$
E\cap Q=\{x\},
\qquad
R_A\cap Q=A,
\qquad |A|=m-1.
$$

For \(m\ge4\), \(m-1\ge3\), so \(E\ne R_A\) for every \(A\). Therefore

$$
|\mathcal R|
=
1+\binom{2m-1}{m-1}
=
M_m+1.
$$

Suppose an endomorphism has been normalized so that

$$
f(P)=f(Q)=T.
$$

For distinct central vertices \(R_A,R_{A'}\), Gate 5 gives

$$
\{Q,R_A,R_{A'}\}\in E(H_m),
$$

and hence

$$
\{T,f(R_A),f(R_{A'})\}\in E(H_m).
$$

For \(E,R_A\), the repaired Gate 6 gives either

$$
\{Q,E,R_A\}\in E(H_m)
$$

or

$$
\{P,E,R_A\}\in E(H_m),
$$

depending on the type of \(A\). In either case,

$$
\{T,f(E),f(R_A)\}\in E(H_m).
$$

Thus every distinct pair of members of \(\mathcal R\) maps to a pair forming an edge in \(L_T\). Irreflexivity of the image hyperedge proves simultaneously that:

$$
f(R)\ne f(S)\quad(R\ne S\in\mathcal R)
$$

and

$$
f(R)\ne T\quad(R\in\mathcal R).
$$

Consequently the images form a clique of size exactly

$$
M_m+1
$$

in \(L_T\), contradicting

$$
\omega(L_T)\le M_m.
$$

Therefore no endomorphism can identify \(P,Q\). Gate 2 shows that every possible collision can be moved to \(P,Q\), so no endomorphism has any collision. Every endomorphism is injective.

Since \(H_m\) is finite, an injective endomorphism is a bijection on vertices. The induced map on all three-element vertex subsets is then a bijection. Its restriction sends \(E(H_m)\) injectively into \(E(H_m)\), so

$$
|f(E(H_m))|=|E(H_m)|,
\qquad
f(E(H_m))\subseteq E(H_m),
$$

and therefore

$$
f(E(H_m))=E(H_m).
$$

Thus \(f^{-1}\) also preserves hyperedges, and \(f\) is an automorphism.

---

## 4. SYMBOLIC ATOM TABLES

### Gate 1 sufficiency witness

Let \(r=2m-1\), \(a=|X\cap Y|\), and assume \(1\le a\le r-2\). With bit order \((X,Y,Z)\), the explicit witness construction gives

$$
\begin{array}{c|ccccccc}
\text{atom}&000&001&010&011&100&101&110\\ \hline
\text{size}
&1&a&1&r-a-1&r-a-1&1&a
\end{array}
$$

and \(111=0\). All seven required entries are positive.

### Gate 5 central-pair table

For

$$
s=|A\cap A'|,
\qquad
t=|B_A\cap B_{A'}|,
$$

with bit order \((Q,R_A,R_{A'})\),

$$
\begin{array}{c|ccccccc}
\text{atom}&000&001&010&011&100&101&110\\ \hline
\text{size}
&t&m-t&m-t&t&s+1&m-1-s&m-1-s
\end{array}
$$

and \(111=s\). The bounds

$$
0\le s\le m-2,
\qquad
1\le t\le m-1
$$

make every required atom positive.

### Gate 6 exceptional tables

The requested bit order is \((\text{anchor},E,R_A)\).

$$
\begin{array}{c|c|ccccccc|c}
A\text{-type}
&\text{anchor}
&000&001&010&011&100&101&110
&\text{actual minimum}\\ \hline
D_0
&Q
&1&1&m-1&m-1&m-1&m-1&1
&1\\[1mm]
D_{10}
&P
&1&2&m-1&m-2&m-1&m-2&1
&1\\[1mm]
D_{11}
&P
&2&1&m-3&m&m&m-3&1
&\min\{1,m-3\}
\end{array}
$$

The omitted \(111\) sizes are respectively

$$
0,\quad 1,\quad 1.
$$

For \(m\ge4\), every required atom is positive. In the \(D_{11}\) row the actual minimum is \(1\), while the two range-determining atoms \(010\) and \(101\) have size \(m-3\). At \(m=3\), both vanish.

---

## 5. M=4 INDEPENDENT CHECK

The exact checker constructs:

$$
|D_0|=|C_0|=20,\qquad
|D_{10}|=|C_{10}|=10,\qquad
|D_{11}|=|C_{11}|=5.
$$

It uses a deterministic sorted typewise bijection. In type \(0\), it alternates between the \(p\)-free and \(p\)-containing representatives, so both allowed representative choices are exercised. The Boolean cells are recomputed directly from point membership.

Exact code used: [audit_m4.py](sandbox:/mnt/data/audit_m4.py)

The complete output was:

```text
OMEGA_SIZE=15 VERTEX_SIZE=7
D_COUNTS {'D0': 20, 'D10': 10, 'D11': 5}
C_COUNTS {'C0': 20, 'C10': 10, 'C11': 5}
CENTRAL_VERTICES=35 UNIQUE=35
E_SIZE=7 E_DISTINCT_FROM_CENTRAL=True
EXCEPTIONAL_TABLES {'D0': [(1, 1, 3, 3, 3, 3, 1)], 'D10': [(1, 2, 3, 2, 3, 2, 1)], 'D11': [(2, 1, 1, 4, 4, 1, 1)]}
CENTRAL_CHECKS=595
EXCEPTIONAL_CHECKS=35
TOTAL_ANCHOR_CHECKS=630
MIN_REQUIRED_ATOM=1
FAILURES=0
```

Thus

$$
\boxed{\text{all }630\text{ required anchor conditions pass at }m=4.}
$$

This is a consistency check only; the arbitrary-\(m\) conclusion comes from the symbolic derivation.

---

## 6. REPAIRS, if any

### PROPOSED REPAIR

Replace the Gate 6 sentence asserting that the smallest \(D_{11}\) atom is \(m-3\) by:

> In the \(D_{11}\) case, the seven required atom sizes are
>
> $$
> (2,1,m-3,m,m,m-3,1).
> $$
>
> Hence the actual minimum is \(\min\{1,m-3\}\). The only potentially vanishing atoms are \(010\) and \(101\), both of size \(m-3\). Therefore this row is valid for every \(m\ge4\) and fails at \(m=3\).

### Rerun of affected gates

**Gate 6 after repair:** VALID. All three exceptional anchor statements hold for every \(m\ge4\).

**Gate 7 after repair:** VALID. The independent \(m=4\) enumeration has zero failures.

**Gate 8 after repair:** VALID. The repaired Gate 6 supplies the exceptional-pair anchors needed for the \(M_m+1\) link clique contradiction.

No modification to \(E\), the type partition, the complement-pair bijection, the representatives \(B_A\), or the fold argument is required.

---

## 7. FINAL THEOREM ACTUALLY ESTABLISHED

The hostile audit establishes the following theorem:

$$
\boxed{
\text{For every integer }m\ge4,\quad
3\text{-}\mathrm{UQI}(4m,2)
\text{ is a core.}
}
$$

Equivalently, for every \(n\equiv0\pmod4\) with \(n\ge16\), every endomorphism of \(3\text{-}\mathrm{UQI}(n,2)\) is an automorphism.

This audit does **not** establish the all-even theorem. In particular, the two-anchor construction audited here does not cover \(m=3\), since the \(D_{11}\) row then has two empty required atoms. Any result for \(n=12\), \(n=8\), or \(n\equiv2\pmod4\) requires its separate argument.

SYMBOLIC = VALID-AFTER-REPAIR

FINITE_M4 = PASS

VERDICT = VALID-AFTER-REPAIR
