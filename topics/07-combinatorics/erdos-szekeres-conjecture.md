---
id: 07-combinatorics/erdos-szekeres-conjecture
title: "Erdős-Szekeres Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Szekeres Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-szekeres-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $ES(n)$ denote the smallest integer $N$ such that every set of $N$ points in the plane in **general position** (no three collinear) contains $n$ points in **convex position** (forming the vertex set of a convex $n$-gon).

The Erdős–Szekeres theorem (1935) says $ES(n)$ is finite. The conjecture, stated by Erdős and Szekeres in 1960, is:

$$ES(n) = 2^{n-2} + 1 \qquad \text{for all } n \ge 3.$$

The lower bound $ES(n) \ge 2^{n-2}+1$ is **proved**: Erdős and Szekeres constructed, for every $n$, a set of $2^{n-2}$ points in general position with no $n$ points in convex position. The open content is the matching upper bound: every set of $2^{n-2}+1$ points in general position contains a convex $n$-gon.

A complete resolution requires either (a) a proof of the upper bound $ES(n) \le 2^{n-2}+1$ for all $n$, or (b) a construction of $2^{n-2}+1$ points in general position with no convex $n$-gon for some $n \ge 7$.

## 2. Mathematical Foundations

**General position.** $P \subset \mathbb{R}^2$, $|P| = N$, with no three points collinear. Only the **order type** of $P$ matters: the map $\chi: P^3 \to \{+,-\}$ recording the orientation sign
$$\chi(p,q,r) = \operatorname{sgn} \det \begin{pmatrix} q_x - p_x & r_x - p_x \\ q_y - p_y & r_y - p_y \end{pmatrix}.$$
Convex position, cups, and caps are all determined by $\chi$, so the problem is finite-combinatorial for each $N$ — but the number of order types on $N$ points grows as $N^{4N(1+o(1))}$ (Goodman–Pollack).

**Cups and caps.** Order $P$ by $x$-coordinate: $p_1 \prec \cdots \prec p_N$. A subsequence $p_{i_1} \prec \cdots \prec p_{i_k}$ is a **$k$-cup** if it is convex (turns left throughout), i.e. the slopes increase; a **$k$-cap** if concave, slopes decrease.

**Cup–cap lemma (Erdős–Szekeres 1935).** Let $f(k,\ell)$ be the least $N$ forcing a $k$-cup or an $\ell$-cap. Then
$$f(k,\ell) = \binom{k+\ell-4}{k-2} + 1,$$
proved by the recursion $f(k,\ell) \le f(k-1,\ell) + f(k,\ell-1) - 1$ and a matching construction. Since a $n$-cup or $n$-cap is in convex position,
$$ES(n) \le f(n,n) = \binom{2n-4}{n-2} + 1 = 4^{n(1+o(1))/1}\cdot \Theta(n^{-1/2}).$$

**Lower-bound construction.** Define sets $S_{k,\ell}$ recursively with $|S_{k,\ell}| = \binom{k+\ell-4}{k-2}$, containing no $k$-cup and no $\ell$-cap: place a scaled copy of $S_{k-1,\ell}$ far to the left and a copy of $S_{k,\ell-1}$ far to the right, with every slope in the left block smaller than every slope between blocks, and every slope in the right block larger. The union
$$X_n = \bigcup_{k=2}^{n-1} S_{k,\,n+1-k}, \qquad |X_n| = \sum_{k=2}^{n-1}\binom{n-3}{k-2} = 2^{n-3}\cdot 2 = 2^{n-2},$$
assembled with the blocks placed so that no convex $n$-gon spans two blocks, has no $n$ points in convex position. Hence $ES(n) \ge 2^{n-2}+1$.

**Related sequence lemma.** The same 1935 paper proved the Monotone Subsequence Theorem: any sequence of $(r-1)(s-1)+1$ distinct reals contains an increasing subsequence of length $r$ or a decreasing one of length $s$ — the pigeonhole ancestor of the whole subject.

## 3. History & State of the Art (SOTA)

- **1932–33.** Esther Klein observed that any 5 points in general position contain a convex quadrilateral, and asked for the general $n$. Szekeres rediscovered Ramsey's theorem to prove finiteness; Erdős named it the **Happy Ending Problem** (Klein and Szekeres later married).
- **1935.** Erdős & Szekeres, *Compositio Mathematica*: finiteness plus the cup–cap bound $\binom{2n-4}{n-2}+1$.
- **1960/61.** Erdős & Szekeres publish the $2^{n-2}$ construction and conjecture equality.
- **1998.** First improvements on the 1935 upper bound in 63 years: Chung–Graham shaved 1, Kleitman–Pachter reduced to $\binom{2n-4}{n-2}+7-2n$, and Tóth–Valtr obtained $\binom{2n-5}{n-2}+2$ — roughly a factor-2 gain, still $4^{n(1+o(1))}$.
- **2006.** Szekeres & Peters settle $ES(6) = 17$ by a large computer search over order types.
- **2017.** **Andrew Suk** proves $ES(n) \le 2^{n + o(n)}$, specifically $ES(n) \le 2^{n+4n^{2/3}\log n}$ for large $n$ — matching the conjectured base $2$ in the exponent. Published in *J. Amer. Math. Soc.*
- **2020.** Holmsen, Mojarrad, Pach, Tardos sharpen the error term to $ES(n) \le 2^{n + O(\sqrt{n \log n})}$, the current record.

**Status of the exponent:** $2^{n-2}+1 \le ES(n) \le 2^{n+O(\sqrt{n\log n})}$. The conjecture is confirmed to first order in the exponent; the remaining gap is a subexponential-but-superpolynomial factor $2^{O(\sqrt{n\log n})}$.

## 4. Partial Results / Verified Cases

| $n$ | $ES(n)$ | $2^{n-2}+1$ | Established by |
|---|---|---|---|
| 3 | 3 | 3 | trivial |
| 4 | 5 | 5 | Klein (1930s) |
| 5 | 9 | 9 | Kalbfleisch, Kalbfleisch & Stanton (1970) |
| 6 | 17 | 17 | Szekeres & Peters (2006), computer proof |
| $\ge 7$ | unknown | 65 | open |

- $ES(6)=17$ was re-verified with a **formally checked** proof by Marić (2019) in Isabelle/HOL, using a SAT encoding over order types — removing doubt about the unverified 2006 search.
- **Exact for cups/caps:** $f(k,\ell) = \binom{k+\ell-4}{k-2}+1$ is exact for all $k,\ell$; the conjecture is only open because convex polygons that are neither a cup nor a cap are hard to force.
- **Restricted point sets:** the conjecture holds for point sets that are the union of few convex chains, for sets in "monotone" or "dense" configurations, and for several structured families where the order type is constrained.
- **Empty-polygon variant (Horton/Gerken/Nicolás/Heule–Scheucher):** every sufficiently large set contains an **empty** hexagon; the exact threshold is $30$ (Heule & Scheucher, TACAS 2024, SAT proof with a verified certificate). Horton (1983) showed empty $7$-gons need not exist at all. This variant is now settled in the ranges where the main conjecture is not.

## 5. Principal Obstacles

- **Combinatorial explosion.** Deciding $ES(7) \le 65$ by exhaustive search means checking all order types on 65 points — a number around $65^{260}$ before symmetry reduction. Current SAT/SMT encodings for $ES(6)=17$ already involve millions of clauses; $n=7$ is far beyond reach, and the search space grows superexponentially in $N$.
- **Cup–cap is intrinsically lossy.** Every proof descending from 1935 forces a *monotone* convex chain. But the extremal sets are built precisely to have no long cup or cap while still avoiding convex $n$-gons that mix a cup and a cap. Suk's argument overcomes part of this by a "positive-fraction"/cup–cap decomposition applied at scale, but its induction still bleeds a $2^{O(\sqrt{n\log n})}$ factor.
- **No structural characterisation of extremal sets.** Unlike Ramsey problems with algebraic extremal constructions, the $2^{n-2}$ construction is not known to be unique or even locally rigid; there is no stability theorem saying "any near-extremal set looks like $X_n$", which would be the natural route to an exact bound.
- **Ramsey-type lower-bound techniques give nothing.** Probabilistic and random-construction methods, which usually supply matching lower bounds in extremal combinatorics, produce point sets with convex polygons of logarithmic size at best — far weaker than the deterministic $X_n$. So the truth is expected to be the *deterministic* bound, and no counting argument can certify it.
- **Loss in the recursion.** Suk's proof partitions the point set and recurses; each level of recursion costs an $n^{o(1)}$-type factor, and $\Theta(\sqrt{n/\log n})$ levels are needed. Removing this loss needs a one-shot argument, not induction on $n$.

## 6. The Gap

Proven: $2^{n-2}+1 \le ES(n) \le 2^{n+c\sqrt{n\log n}}$ for an absolute constant $c$; equality verified for $n \le 6$.

The gap is the multiplicative factor
$$\frac{ES(n)_{\text{upper}}}{ES(n)_{\text{lower}}} \;=\; 2^{\,O(\sqrt{n\log n})\,+\,2},$$
which is $1$ in the conjecture. Crossing it requires an argument that forces a convex $n$-gon from $2^{n-2}+1$ points *without* an inductive step that loses more than $O(1)$ per unit increase in $n$ — equivalently, a proof that the extremal number obeys the exact recursion $ES(n) = 2\,(ES(n-1)-1)+1$. Even reducing the error to $2^{O(\log^2 n)}$ or $2^{n+O(\log n)}$ would be a major advance; nobody currently has a mechanism producing an $O(1)$ additive error. The first genuinely new data point would be deciding whether $ES(7) = 65$.

## 7. Current Research (as of June 2026)

- **SAT/automated reasoning.** The Heule (Carnegie Mellon) and Scheucher (TU Berlin) programme has produced verified DRAT certificates for the empty-hexagon number 30 and for $ES(6)=17$. Extensions target $6$-holes with additional constraints and partial $ES(7)$ obstructions — no full $ES(7)$ attack is considered feasible with current encodings. *(frontier — verify)*
- **Refining Suk's method.** Groups around Suk (UC San Diego), Pach and Tardos (Rényi Institute / Central European University), and Holmsen (KAIST) work on tightening the error exponent below $\sqrt{n\log n}$, and on higher-dimensional and hypergraph-Ramsey analogues where the same cup–cap machinery applies.
- **Order-type enumeration.** Aichholzer's Graz database of realisable order types (complete to 11 points, abstract order types further) underpins all exhaustive verification; extending it is a bottleneck of independent interest.
- **Semi-algebraic Ramsey theory.** Conlon–Fox–Pach–Sudakov–Suk-style results on Ramsey numbers of semi-algebraic hypergraphs give the general framework in which Erdős–Szekeres is the $d=2$, $k=3$ case; improvements there transfer directly.
- **Variants under active study.** Convex position with prescribed interior point counts, $k$-holes in higher dimension, the "many convex polygons" (positive-fraction) versions, and the modular/colored Erdős–Szekeres problems.

## 8. Future Work

- Prove a **stability theorem**: any point set of size close to $2^{n-2}$ with no convex $n$-gon is combinatorially close to the Erdős–Szekeres construction $X_n$. This is the standard route from an asymptotic to an exact extremal result.
- Find an alternative to induction on $n$ — for instance a direct entropy or compression argument that maps convex-$n$-gon-free sets injectively into a set of size $2^{n-2}$.
- Settle **$ES(7)$**, or at least prove $ES(7) \le 128$ (i.e. beat $2^{n-1}$) by hand-crafted arguments plus computer assistance; even $ES(7) < 2^6\cdot 2$ with a human-readable proof would test whether the exact recursion is plausible.
- Determine whether the extremal configuration is unique up to order type for $n=5,6$ — the 2006 and 2019 computations contain the data, and uniqueness for small $n$ is evidence for rigidity.
- Push the exponent error to $O(\log^2 n)$ using multi-scale cup–cap decompositions, as suggested in Suk's concluding remarks.

## 9. Key References

- **[Foundational]** P. Erdős and G. Szekeres. *A combinatorial problem in geometry.* Compositio Mathematica, 2:463–470, 1935.
- **[Foundational]** P. Erdős and G. Szekeres. *On some extremum problems in elementary geometry.* Annales Universitatis Scientiarum Budapestinensis, Eötvös Sect. Math., 3–4:53–62, 1960/61.
- **[SOTA]** A. Suk. *On the Erdős–Szekeres convex polygon problem.* Journal of the American Mathematical Society, 30(4):1047–1053, 2017.
- **[SOTA]** A. Holmsen, H. N. Mojarrad, J. Pach, G. Tardos. *Two extensions of the Erdős–Szekeres problem.* Journal of the European Mathematical Society, 22(12):3981–3995, 2020.
- **[Survey]** W. Morris and V. Soltan. *The Erdős–Szekeres problem on points in convex position — a survey.* Bulletin of the American Mathematical Society, 37(4):437–458, 2000.
- **[Survey]** G. Tóth and P. Valtr. *The Erdős–Szekeres theorem: upper bounds and related results.* In *Combinatorial and Computational Geometry*, MSRI Publications 52, pp. 557–568, Cambridge University Press, 2005.
- **[Computational]** G. Szekeres and L. Peters. *Computer solution to the 17-point Erdős–Szekeres problem.* ANZIAM Journal, 48(2):151–164, 2006.
- **[Computational]** J. D. Kalbfleisch, J. G. Kalbfleisch, R. G. Stanton. *A combinatorial problem on convex $n$-gons.* Proc. Louisiana Conference on Combinatorics, Graph Theory and Computing, pp. 180–188, 1970.
- **[Formal verification]** F. Marić. *Fast formal proof of the Erdős–Szekeres conjecture for convex polygons with at most 6 points.* Journal of Automated Reasoning, 62:301–329, 2019.
- **[Recent / variant]** M. J. H. Heule and M. Scheucher. *Happy ending: an empty hexagon in every set of 30 points.* TACAS 2024, LNCS 14570, Springer, 2024.
- **[Variant]** J. D. Horton. *Sets with no empty convex 7-gons.* Canadian Mathematical Bulletin, 26(4):482–484, 1983.
- **[Improvement]** F. R. K. Chung and R. L. Graham. *Forced convex $n$-gons in the plane.* Discrete & Computational Geometry, 19:367–371, 1998.
- **[Improvement]** D. Kleitman and L. Pachter. *Finding convex sets among points in the plane.* Discrete & Computational Geometry, 19:405–410, 1998.

## 10. Worked Example / Concrete Special Case

**Case $n = 4$: $ES(4) = 5$ (Klein's argument).**

*Lower bound.* Take $2^{4-2} = 4$ points: $(0,0), (4,0), (2,3)$ and $(2,1)$. The fourth lies strictly inside the triangle, so the convex hull has 3 vertices and no convex quadrilateral exists. Hence $ES(4) \ge 5$.

*Upper bound.* Let $P$ be 5 points in general position, $H = \operatorname{conv}(P)$.
- If $|H| = 5$ or $|H| = 4$: a convex quadrilateral is immediate.
- If $|H| = 3$, say hull $\{a,b,c\}$ with $d,e$ inside. The line $\ell$ through $d,e$ misses $a,b,c$ (general position), so it splits $\{a,b,c\}$ into a side with two points, say $\{a,b\}$, and a side with one. Then $a, b, d, e$ are in convex position: $d$ and $e$ both lie on the same side of line $ab$, and $a,b$ both lie on the same side of $\ell$, so the quadrilateral $a\,b\,e\,d$ (in the right cyclic order) is convex.

So $ES(4) = 5 = 2^2+1$. ∎

**Case $n = 5$: the lower bound $ES(5) \ge 9$.** The cup–cap sets give $|S_{2,4}| = \binom{2}{0}=1$, $|S_{3,3}| = \binom{2}{1}=2$, $|S_{4,2}| = \binom{2}{2}=1$, total $\sum = 4$... this counts $\sum_{k=2}^{4}\binom{2}{k-2} = 1+2+1 = 4$ blocks-worth, and the Erdős–Szekeres assembly scales each $S_{k,6-k}$ into a cluster, yielding $2^{5-2} = 8$ points with no convex pentagon. A concrete such 8-point set (from the Kalbfleisch–Kalbfleisch–Stanton verification) consists of two clusters of 4 placed so that every convex 5-subset would need 3 points from one cluster forming a cap and 2 from the other forming the wrong turn. Exhaustive search over all order types on 9 points confirms $ES(5)=9$.

**Comparing the bounds at $n = 7$.** Conjecture: $ES(7) = 65$. Cup–cap (1935): $\binom{10}{5}+1 = 253$. Tóth–Valtr (1998): $\binom{9}{5}+2 = 128$. Suk's asymptotic bound is not effective in this range. So for the very first open case the best proven statement is $65 \le ES(7) \le 128$ — a factor-2 gap that no method has closed in nearly three decades.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*