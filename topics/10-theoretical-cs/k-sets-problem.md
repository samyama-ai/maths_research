---
id: 10-theoretical-cs/k-sets-problem
title: "K-sets Problem"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# K-sets Problem

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/k-sets-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $P \subset \mathbb{R}^d$ be a set of $n$ points in general position (no $d+1$ on a common hyperplane). A **$k$-set** of $P$ is a subset $S \subseteq P$ with $|S| = k$ that can be cut off by a hyperplane: there is an open halfspace $H$ with $S = P \cap H$. Write $a_k(P)$ for the number of $k$-sets of $P$ and

$$a_{k,d}(n) \;=\; \max_{|P| = n,\ P \subset \mathbb{R}^d \text{ generic}} a_k(P).$$

**The problem:** determine the asymptotic growth of $a_{k,d}(n)$, in particular of the planar function $a_{k,2}(n)$ and of the *halving-line* function $h(n) = a_{n/2,2}(n)$ for even $n$.

The gap in the plane is still exponentially wide in $\log k$:

$$n \cdot 2^{\Omega(\sqrt{\log k})} \;\le\; a_{k,2}(n) \;=\; O\!\left(n (k+1)^{1/3}\right).$$

A complete resolution means an upper and a lower bound matching to within a constant (or at least a $n^{o(1)}$) factor. Even the qualitative question — **is $h(n) = n^{1+o(1)}$, or is it $n^{1+\varepsilon}$ for some $\varepsilon > 0$?** — is open, and is widely regarded as the central unsolved problem of combinatorial geometry.

## 2. Mathematical Foundations

**$k$-edges.** For $P \subset \mathbb{R}^2$ in general position and $0 \le j \le n-2$, an ordered pair $\{p,q\} \subset P$ spans a **$j$-edge** if the open halfplane to the left of the directed line $pq$ contains exactly $j$ points of $P$. Let $e_j(P)$ denote the number of $j$-edges. Then

$$\sum_{j=0}^{n-2} e_j(P) = 2\binom{n}{2}, \qquad e_j(P) = e_{n-2-j}(P),$$

and by rotating a directed line one gets the standard correspondence $a_k(P) = e_{k-1}(P)$; the $k$-set and $k$-edge problems are therefore the same problem. When $n$ is even, the $\left(\tfrac{n}{2}-1\right)$-edges are the **halving edges**, and their supporting lines are the halving lines.

**Dual / level formulation.** Under the duality $p = (a,b) \mapsto p^* : y = ax - b$, the $k$-sets of $P$ correspond to the vertices of the **$k$-level** of the arrangement $\mathcal{A}(P^*)$ of $n$ lines: the closure of the set of points lying on some line and strictly above exactly $k$ others. So $a_{k,2}(n)$ is exactly the maximum complexity of a $k$-level in an arrangement of $n$ lines.

**Exact facts anchoring the problem.**

- *(≤k)-edges, upper.* $\sum_{j<k} e_j(P) \le nk$ for $k \le n/2$, with equality attainable (Alon–Győri 1986; Peck 1986). Hence $a_{k,2}(n) = O(n)$ *on average* over $k$ — the difficulty is entirely in the concentration at a single $k$.
- *(≤k)-edges, lower (generalized lower bound theorem).* $\sum_{j<k} e_j(P) \ge 3\binom{k+1}{2}$ for $k < n/3$, sharp; refinements by Aichholzer–García–Orden–Ramos (2007) and Ábrego et al. (2012) raise this and feed directly into rectilinear crossing numbers.
- *Lovász's Lemma (1971).* Any line $\ell$ crosses $O(n)$ of the $k$-edges of $P$. Combined with a sweep this yields $a_{k,2}(n) = O(n\sqrt{k})$.
- *Crossing Lemma* (Ajtai–Chvátal–Newborn–Szemerédi; Leighton). A graph drawn in the plane with $n$ vertices and $m \ge 4n$ edges has at least $m^3/(64n^2)$ crossings. This is the engine of Dey's bound.

**Higher dimensions.** A **$k$-facet** in $\mathbb{R}^d$ is a $(d-1)$-tuple... more precisely a $d$-subset of $P$ whose spanned hyperplane has exactly $k$ points of $P$ on one open side. The counts $e_k^{(d)}(P)$ generalize $e_k$, and $a_{k,d}(n)$ is polynomially tied to $\max_P e_k^{(d)}(P)$.

## 3. History & State of the Art (SOTA)

- **1971.** Lovász, in a two-page note, proves $h(n) = O(n^{3/2})$ via the crossing lemma for halving lines.
- **1973.** Erdős, Lovász, Simmons and Straus formalize the $k$-set problem, prove $a_{k,2}(n) = O(n\sqrt{k})$ and construct point sets with $\Omega(n \log k)$ $k$-sets. They conjecture $h(n) = n^{1+o(1)}$; Erdős repeatedly offered prizes.
- **1992.** Pach, Steiger and Szemerédi shave the first factor: $a_{k,2}(n) = O(n\sqrt{k}/\log^\ast k)$.
- **1998.** Dey proves $a_{k,2}(n) = O(n(k+1)^{1/3})$, hence $h(n) = O(n^{4/3})$, by decomposing $k$-edges into convex chains and applying the Crossing Lemma. This remains the best planar upper bound after 28 years.
- **2001.** G. Tóth constructs point sets with $n \cdot 2^{\Omega(\sqrt{\log k})}$ $k$-sets, superseding $\Omega(n\log k)$; Nivasch (2008) gives a simpler recursive construction with better constants.
- **3D.** Bárány–Füredi–Lovász (1990) first proved $o(n^3)$ for halving planes; Sharir–Smorodinsky–Tardos (2001) give $a_{k,3}(n) = O(nk^{3/2})$, i.e. $O(n^{5/2})$ halving planes. Edelsbrunner–Valtr–Welzl (1997) give the $\Omega(n^{d-1}\log n)$ lower bound for halving facets in $\mathbb{R}^d$.
- **General $d$.** $a_{k,d}(n) = O(n^{d-\varepsilon_d})$ with an explicit but tiny $\varepsilon_d > 0$ (Alon–Bárány–Füredi–Kleitman 1992, via the Second Selection Lemma and colored Tverberg theory).

## 4. Partial Results / Verified Cases

- **Extreme $k$.** $a_{1,d}(n) = n$ (all points can be vertices of the convex hull). For $k$ constant, $a_{k,2}(n) = \Theta(n)$; the general bound $O(n(k+1)^{1/3})$ is tight up to constants exactly in this regime.
- **$k = \Theta(n)$ but not central.** For points in convex position the $j$-edges are exactly the "chords of skip $j+1$", so $e_j = n$ for all $j < n/2 - 1$ and $h = n/2$ — linear, far from extremal. Convexity kills the problem.
- **Averaged version, solved.** $\sum_{j<k} e_j \le nk$ is exact (Alon–Győri, Peck), and the minimum $3\binom{k+1}{2}$ is exact for $k<n/3$. The *cumulative* $k$-set problem is therefore closed; only the single-layer version is open.
- **Small $n$, exhaustive.** The maximum number of halving lines is known exactly for small even $n$ by order-type enumeration (Aichholzer et al., using the complete database of order types up to $n=11$ and extensions): $h(4)=3$, $h(6)=6$, $h(8)=9$, $h(10)=13$, $h(12)=18$. Values grow visibly faster than $n$ but no small case discriminates $n^{1+o(1)}$ from $n^{4/3}$.
- **Structured inputs.** For points on a convex curve, on a grid $\{1,\dots,\sqrt n\}^2$, or in "dense" position (spread $O(\sqrt n)$), sharper bounds are available; Edelsbrunner–Valtr–Welzl show dense sets have $O(n^{4/3}/\log^{*}n)$-type behavior in the plane and $\Omega(n^{d-1}\log n)$ in $\mathbb{R}^d$.
- **Related counts fully solved.** The order-$k$ Voronoi diagram of $n$ planar points has complexity $\Theta(k(n-k))$ (Lee 1982) — a $k$-set-adjacent quantity that is *not* open, which sharpens how special the $k$-level difficulty is.

## 5. Principal Obstacles

- **The Crossing Lemma is tight and already spent.** Dey's argument converts $k$-edges into a graph whose crossings are bounded by $O(n^2)$ and then applies the cubic crossing inequality. Both steps are individually optimal for the objects used, so no reshuffling of the same two ingredients can go below $n(k+1)^{1/3}$. Improving requires a *structural* constraint on $k$-edge families that the crossing framework does not see.
- **No usable global structure.** A family of $k$-edges is only known to satisfy convex-chain decomposability and the Lovász crossing bound. There is no known forbidden sub-configuration, no VC-type shatter bound beyond the trivial one, and no algebraic identity that separates realizable $k$-edge sets from abstract ones.
- **Lower-bound constructions are recursive and lossy.** Tóth's and Nivasch's constructions build point sets by substituting scaled copies into a base configuration. Each recursion level multiplies the count by a constant while squaring-ish the size, which is exactly what produces $2^{\Theta(\sqrt{\log k})}$ and not a power of $k$. Nobody knows a construction paradigm that is not self-similar in this way, and self-similar ones provably cannot exceed $n^{1+o(1)}$.
- **Topological methods stall in high $d$.** The $\varepsilon_d$ in $O(n^{d-\varepsilon_d})$ comes from Tverberg-type / equivariant topology arguments whose quantitative content degrades doubly-exponentially in $d$; the topology gives existence of deep points, not counting.
- **Algebraic methods do not attach.** Polynomial partitioning (Guth–Katz) controls incidences between points and low-degree varieties. $k$-edges are not an incidence structure: the defining condition is an *order* condition (exactly $k$ points on one side), which is semialgebraic of high complexity and not preserved by the partition cells.

## 6. The Gap

Proven, for the plane: $a_{k,2}(n) \le c\, n(k+1)^{1/3}$ and $a_{k,2}(n) \ge n\,2^{c'\sqrt{\log k}}$. Setting $k = n/2$, the quantity $h(n)$ is pinned only between $n\,2^{c'\sqrt{\log n}} = n^{1+o(1)}$ and $c\,n^{4/3}$.

The precise unresolved step is: **exhibit a super-polylogarithmic structural obstruction, or a construction with a genuine power gain.** Concretely, either

1. prove $a_{k,2}(n) = O(n\,k^{\delta})$ for some $\delta < 1/3$ — which requires an argument that uses more about $k$-edge families than "few crossings, convex chains"; or
2. build a point set with $\Omega(n k^{\delta})$ $k$-sets for some $\delta>0$ — which requires abandoning self-similar substitution, since every known recursion caps out at $n^{1+o(1)}$.

Nobody has a candidate for either. The community is split on which is true, with a mild majority expecting $h(n) = n^{1+o(1)}$, matching Erdős's original guess.

## 7. Current Research (as of June 2026)

- **Exact $(\le k)$-edge inequalities and rectilinear crossing numbers.** The Ábrego–Fernández-Merchant school (CSU Northridge) and Salazar–Cetina–Leaños (CIMAT / UASLP) continue to push lower bounds on $\sum_{j<k}e_j$, because $\overline{\mathrm{cr}}(K_n)$ is a linear functional of the $(\le k)$-edge vector. Each improvement tightens the constant in the rectilinear crossing constant $q^\ast \approx 0.3800$.
- **Order-type enumeration.** Aichholzer's group (TU Graz) extends the order-type database and abstract-order-type search to certify $h(n)$ for further $n$; the bottleneck is the doubly-exponential number of order types. *(frontier — verify)*
- **Levels in arrangements of curves.** Chan and others study $k$-levels for pseudolines, algebraic curves, and in the "generalized configuration" (allowable sequence) setting, testing whether the $O(nk^{1/3})$ bound is a fact about points or about the weaker combinatorial abstraction. Current evidence: it is about the abstraction, which suggests the true point-set bound is smaller.
- **Higher-dimensional $k$-facets.** Work continues on improving $\varepsilon_d$ and on the $O(nk^{3/2})$ 3D bound via Sharir-style charging and second-order Lovász lemmas.
- **Semialgebraic / hypergraph containers.** Attempts to import container and regularity methods for semialgebraic hypergraphs (Fox–Pach–Suk) into $k$-set counting; so far these give structure theorems for dense settings but no new bound. *(frontier — verify)*

## 8. Future Work

- Prove a "second Lovász lemma": bound the number of $k$-edges crossed by a *convex curve* or by another $k$-edge family, not just by a line. Dey's proof would then iterate.
- Find any non-self-similar lower-bound construction. Nivasch explicitly poses this; a random or algebraic construction with $\Omega(n^{1+\varepsilon})$ halving lines would settle the qualitative question at once.
- Settle the pseudoline/allowable-sequence version. If $O(nk^{1/3})$ is tight for pseudolines but not for points, the separation itself identifies the missing geometric axiom.
- Extend the exact $(\le k)$-edge theory upward: exact determination of $\sum_{j<k}e_j$ for $k$ near $n/2$ would essentially determine $h(n)$.
- Computational: certify $h(n)$ for $n \ge 14$ by SAT/ILP over abstract order types with realizability filtering.

## 9. Key References

- **[Foundational]** L. Lovász. *On the number of halving lines.* Annales Universitatis Scientiarum Budapestinensis, Sectio Mathematica, 14 (1971), 107–108.
- **[Foundational]** P. Erdős, L. Lovász, A. Simmons, E. G. Straus. *Dissection graphs of planar point sets.* In *A Survey of Combinatorial Theory*, North-Holland, 1973, 139–149.
- **[Foundational]** N. Alon, E. Győri. *The number of small semispaces of a finite set of points in the plane.* Journal of Combinatorial Theory, Series A, 41 (1986), 154–157.
- **[Foundational]** G. W. Peck. *On k-sets in the plane.* Discrete & Computational Geometry, 1 (1986), 95–100.
- **[SOTA]** T. K. Dey. *Improved bounds for planar k-sets and related problems.* Discrete & Computational Geometry, 19 (1998), 373–382.
- **[SOTA]** G. Tóth. *Point sets with many k-sets.* Discrete & Computational Geometry, 26 (2001), 187–194.
- **[SOTA]** G. Nivasch. *An improved, simple construction of many halving edges.* In *Surveys on Discrete and Computational Geometry*, Contemporary Mathematics 453, AMS, 2008, 299–305.
- **[SOTA]** M. Sharir, S. Smorodinsky, G. Tardos. *An improved bound for k-sets in three dimensions.* Discrete & Computational Geometry, 26 (2001), 195–204.
- **[Prior SOTA]** J. Pach, W. Steiger, E. Szemerédi. *An upper bound on the number of planar k-sets.* Discrete & Computational Geometry, 7 (1992), 109–123.
- **[Higher dimensions]** I. Bárány, Z. Füredi, L. Lovász. *On the number of halving planes.* Combinatorica, 10 (1990), 175–183.
- **[Higher dimensions]** N. Alon, I. Bárány, Z. Füredi, D. Kleitman. *Point selections and weak ε-nets for convex hulls.* Combinatorics, Probability and Computing, 1 (1992), 189–200.
- **[Structure]** H. Edelsbrunner, P. Valtr, E. Welzl. *Cutting dense point sets in half.* Discrete & Computational Geometry, 17 (1997), 243–255.
- **[Applications]** L. Lovász, K. Vesztergombi, U. Wagner, E. Welzl. *Convex quadrilaterals and k-sets.* Contemporary Mathematics, 342 (2004), 139–148.
- **[Applications]** O. Aichholzer, J. García, D. Orden, P. Ramos. *New lower bounds for the number of (≤k)-edges and the rectilinear crossing number of $K_n$.* Discrete & Computational Geometry, 38 (2007), 1–14.
- **[Survey]** U. Wagner. *k-Sets and k-Facets.* In *Surveys on Discrete and Computational Geometry*, Contemporary Mathematics 453, AMS, 2008, 443–513.
- **[Survey / Textbook]** J. Matoušek. *Lectures on Discrete Geometry.* Graduate Texts in Mathematics 212, Springer, 2002, Chapter 11.

## 10. Worked Example / Concrete Special Case

**Claim: $h(4) = 3$, and the maximizer is *not* in convex position.**

Take $n=4$ points in general position. A halving edge is a pair $\{p,q\}$ with exactly one of the remaining two points on each side of the line $pq$. There are $\binom{4}{2} = 6$ pairs, and each pair is either a $0$-edge (both others on one side) or a $1$-edge (halving).

*Case A — convex position.* Let $P = \{(0,0),(1,0),(1,1),(0,1)\}$, labelled $p_1,p_2,p_3,p_4$ in cyclic order.

- Side $\{p_1,p_2\}$: line $y=0$; $p_3=(1,1)$ and $p_4=(0,1)$ both have $y>0$. A $0$-edge. Same for the other three sides.
- Diagonal $\{p_1,p_3\}$: line $y=x$; $p_2=(1,0)$ has $y-x=-1<0$, $p_4=(0,1)$ has $y-x=+1>0$. Halving.
- Diagonal $\{p_2,p_4\}$: line $x+y=1$; $p_1$ gives $0<1$, $p_3$ gives $2>1$. Halving.

So $e_0 = 4$, $e_1 = 2$, total $6$ ✓. Convex position yields **2** halving lines.

*Case B — triangle plus interior point.* Let $a=(0,0)$, $b=(4,0)$, $c=(2,3)$, $d=(2,1)$ (inside $\triangle abc$).

- $\{a,b\}$: line $y=0$; $c$ and $d$ both have $y>0$. $0$-edge. Likewise $\{b,c\}$ and $\{a,c\}$ are $0$-edges, since $d$ is interior and hence on the same side as the third vertex.
- $\{a,d\}$: line $y = x/2$; $b=(4,0)$ gives $0 - 2 = -2 < 0$, $c=(2,3)$ gives $3-1 = +2 > 0$. Halving.
- $\{b,d\}$: line through $(4,0),(2,1)$, i.e. $x + 2y = 4$; $a$ gives $0 < 4$, $c$ gives $2+6=8 > 4$. Halving.
- $\{c,d\}$: line $x = 2$; $a$ gives $0<2$, $b$ gives $4>2$. Halving.

So $e_0 = 3$, $e_1 = 3$, total $6$ ✓ — **3** halving lines, and this is optimal since $e_0 \ge 3$ always (the generalized lower bound theorem at $k=1$: $\sum_{j<1}e_j \ge 3\binom{2}{2} = 3$, the convex hull has at least 3 edges), forcing $e_1 \le 3$.

**What this illustrates.** Pushing points *inside* the hull converts $0$-edges into halving edges. The whole lower-bound program — Erdős–Lovász–Simmons–Straus, then Tóth, then Nivasch — is this move applied recursively: replace each point of a good small configuration by a tiny scaled copy of the whole configuration, so that halving edges of the inner copies survive as halving edges of the whole. Each recursion level costs a squaring of $n$ and buys a constant factor, which is exactly why the best known gain is $2^{\Theta(\sqrt{\log n})}$ and not $n^{\varepsilon}$. Closing the gap to Dey's $O(n^{4/3})$ requires a fundamentally different construction, or a fundamentally different counting argument.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*