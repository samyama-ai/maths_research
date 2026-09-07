---
id: 10-theoretical-cs/conway-thrackle-conjecture
title: "Conway Thrackle Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Conway Thrackle Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/conway-thrackle-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A **thrackle** is a drawing of a finite simple graph in the plane in which every two edges meet exactly once — either at a shared endpoint, or at a single transversal crossing in their interiors. No two edges may share an endpoint *and* cross, no two may cross twice, and no two may be disjoint.

**Conjecture (J. H. Conway, c. 1960s).** Every thrackle has at most as many edges as vertices:
$$e(G) \le n(G).$$

A proof must establish the bound for every graph admitting a thrackle drawing with arbitrary continuous (Jordan-arc) edges. A disproof requires a single explicit thrackle drawing with $e = n+1$. The bound is tight: every cycle $C_m$ with $m \ne 4$ is thrackleable, giving $e = n$, as is the star $K_{1,n-1}$ with $e = n-1$.

## 2. Mathematical Foundations

Let $G = (V,E)$, $|V| = n$, $|E| = e$. A **drawing** $D$ of $G$ maps vertices to distinct points of $\mathbb{R}^2$ and each edge $uv$ to a Jordan arc with endpoints $D(u), D(v)$, whose interior avoids all vertex points. Drawings are assumed generic: finitely many intersection points, no tangencies, no triple points.

For arcs $\alpha,\beta$ write $|\alpha \cap \beta|$ for the number of common points other than shared endpoints. $D$ is a **thrackle** if for all $f \ne g \in E$:
$$
|D(f)\cap D(g)| = \begin{cases} 0 & \text{if } f,g \text{ share an endpoint},\\ 1 & \text{if } f,g \text{ are independent,}\end{cases}
$$
with the single intersection in the second case a transversal crossing.

Two relaxations structure the theory:

- **Generalized thrackle:** every two independent edges cross an *odd* number of times and every two adjacent edges cross an *even* number of times. Every thrackle is a generalized thrackle; the converse fails.
- **Linear (straight-line) thrackle:** all edges are straight segments. Here Conway's bound is a theorem (Erdős).

The generalized notion is a $\mathbb{Z}_2$-homological condition. Fixing an arbitrary reference drawing, the parity vector of crossings defines a class in $H^1$ of the configuration space of the graph; changing a drawing by a homotopy alters crossing numbers in pairs, so parities are invariants of the drawing's homotopy class relative to a surface. This yields the central structural theorem:

**Theorem (Lovász–Pach–Szegedy 1997; Cairns–Nikolayevsky 2000/2009).** A bipartite graph $G$ admits a generalized thrackle drawing in the plane if and only if $G$ is planar. On an orientable surface $S_g$ of genus $g$, a bipartite $G$ is generalized-thrackleable iff $G$ embeds in $S_g$; for non-bipartite $G$ the criterion involves an embedding in a surface of Euler genus shifted by one.

Two elementary constraints on genuine thrackles:

1. **No $C_4$.** The 4-cycle has no thrackle drawing.
2. **Cycle parity.** $C_m$ is thrackleable for every $m \ne 4$; odd cycles admit the "musquash" drawing $\{i,i+k\}$ on a convex $m$-gon.

**Woodall's reformulation (1971).** Conway's conjecture is equivalent to: *no thrackleable graph contains a $C_4$, two vertex-disjoint even cycles, or two even cycles sharing exactly one vertex (a "figure-eight").* Equivalently, a graph is thrackleable iff it avoids these three configurations. This is the standard target of modern work: since a connected graph with $e \ge n+1$ contains two independent cycles, and a theta-subgraph with cycle lengths $a+b$, $b+c$, $a+c$ always contains an even cycle, ruling out even-cycle pairs suffices.

## 3. History & State of the Art (SOTA)

Conway posed the problem in the 1960s (reportedly offering a small prize, later raised to \$1000); the word "thrackle" is his. The first published treatment is Woodall's 1971 paper *Thrackles and deadlock*, which gave the configuration reformulation above, settled the linear case (attributing the argument to Erdős), and introduced musquashes.

Milestones on the linear bound $e \le c\,n$:

| Year | Authors | Bound |
|---|---|---|
| 1971 | Woodall / Erdős | $e \le n$ for **linear** thrackles |
| 1997 | Lovász, Pach, Szegedy | $e \le 2n - 3$ |
| 2000 | Cairns, Nikolayevsky | $e \le \tfrac{3}{2}(n-1)$ |
| 2011 | Fulek, Pach | $e \le \tfrac{167}{117}n < 1.428n$ |
| 2017 | Goddyn, Xu | $e \le 1.4n$ |
| 2019 | Fulek, Pach | $e \le 1.3984n$ |

The 1997 breakthrough came from a discharging/counting argument on the crossing structure; Cairns–Nikolayevsky obtained $\tfrac32(n-1)$ by showing a minimal counterexample has minimum degree $\ge 3$ and analysing the surface-embedding parity criterion. Fulek and Pach converted the figure-eight reduction into a finite case check on drawings of two even cycles, verified by computer; the 2019 refinement enlarged the discharging catalogue.

## 4. Partial Results / Verified Cases

- **Linear thrackles:** $e \le n$ (Erdős, in Woodall 1971). Straight-line thrackles contain no even cycle at all.
- **$x$-monotone thrackles:** $e \le n$ (Pach–Sterling, *Amer. Math. Monthly* 2011), where every edge meets each vertical line at most once.
- **Outerplanar thrackles:** $e \le n$ (Cairns–Nikolayevsky, *Graphs and Combinatorics* 2012).
- **Bipartite graphs:** the conjecture holds; bipartite thrackleable graphs satisfy $e \le n$ (Lovász–Pach–Szegedy 1997, via the planarity criterion of §2).
- **Small forbidden graphs:** $K_5$ and $K_{3,3}$ are not thrackleable (Cairns–McIntyre–Nikolayevsky, *Contemp. Math.* 342, 2004). Consequently no thrackleable graph contains a $K_5$- or $K_{3,3}$-subdivision drawn thrackle-wise.
- **Cycles:** complete classification — $C_m$ is thrackleable iff $m \ne 4$.
- **Small figure-eights:** pairs of even cycles $C_{2a}, C_{2b}$ sharing one vertex are non-thrackleable for the small values of $a,b$ checked by the Fulek–Pach computer search (2011).
- **Tangled thrackles** (adjacent edges may touch): $e = O(n)$ with explicit constant (Ruiz-Vargas–Suk–Tóth 2016), resolving a conjecture of Pach–Radoičić–Tóth.
- **Global constant:** unconditionally $e \le 1.3984n$ for all thrackles, so the conjecture is off by less than $40\%$.

## 5. Principal Obstacles

- **Parity is too coarse.** The $\mathbb{Z}_2$ machinery that solves the bipartite case only sees crossing *parities*, and generalized thrackles genuinely admit more edges than thrackles. Any purely homological argument therefore cannot distinguish a real thrackle of a figure-eight from an unrealizable parity pattern. The missing information is the passage from "odd number of crossings" to "exactly one".
- **No Euler-formula leverage.** Standard crossing-number and planarity tools bound edges via faces of a planar subdrawing. A thrackle is maximally non-planar — every independent pair crosses — so $e \le 3n-6$-style arguments and the crossing lemma are vacuous or point the wrong way.
- **Non-locality.** The thrackle condition is a global constraint on all $\binom{e}{2}$ pairs. Local moves (rerouting one edge, contracting, deleting a vertex) destroy it: deleting a vertex leaves a thrackle, but adding one back is not controllable, blocking induction and minimal-counterexample arguments beyond minimum-degree statements.
- **Discharging saturates.** The chain $2n \to 1.5n \to 1.428n \to 1.3984n$ comes from ever finer discharging over local configurations with diminishing returns; each step costs a larger case analysis for a few hundredths in the constant, and the method has no visible route to $1$.
- **Combinatorial explosion in the reduction.** Woodall's reduction is to infinitely many figure-eight graphs $C_{2a}\!\cdot\!C_{2b}$; computer verification handles only bounded $a,b$, and no uniform argument in $a,b$ is known.

## 6. The Gap

Proven: $e \le 1.3984n$ in general; $e \le n$ for bipartite, linear, monotone and outerplanar thrackles. Conjectured: $e \le n$ for all thrackles.

The precise gap is a single statement:

> **No figure-eight of two even cycles, and no vertex-disjoint pair of even cycles, is thrackleable.**

Granting this, Woodall's argument gives $e \le n$ immediately. Equivalently, one must show that a graph whose thrackle drawing exists cannot contain two independent cycles at all. The technical barrier is producing an invariant of *thrackle* drawings — not merely generalized ones — that separates even cycles: something strictly finer than $\mathbb{Z}_2$ crossing parity but still stable under isotopy of the arcs. Every known invariant (rotation numbers, Gauss codes, surface genus parity) collapses to the parity condition already exploited.

## 7. Current Research (as of June 2026)

- **Discharging refinements.** The Fulek–Pach programme continues at IST Austria / EPFL and Rényi Institute; incremental improvements below $1.39n$ are plausible but no announced result reaches $1.2n$. *(frontier — verify)*
- **Radial and monotone-like restrictions.** Following Pach–Sterling, several groups study thrackles whose edges are monotone with respect to a pencil of lines or circles, where $e \le n$ recurs; the interest is in identifying the weakest geometric restriction under which the bound survives.
- **Gauss-code and knot-theoretic encodings.** Encoding a thrackled figure-eight as a signed Gauss word and searching for realizability obstructions (Cairns–Nikolayevsky lineage, La Trobe University).
- **SAT/SMT and computational topology.** Encoding realizability of a prescribed crossing pattern as a constraint problem to push the verified range of figure-eight graphs $C_{2a}\cdot C_{2b}$ upward. *(frontier — verify)*
- **Generalizations.** Thrackles on surfaces of higher genus, "$k$-thrackles" where edges meet exactly $k$ times, and tangled/quasi-thrackles, where linear bounds are known and the extremal constants are open.

## 8. Future Work

- Prove the figure-eight case for *all* $a,b$ by a uniform argument, e.g. an induction on $a+b$ that removes a crossing-free "ear".
- Find a $\mathbb{Z}$-valued (not $\mathbb{Z}_2$-valued) invariant of thrackle drawings — a winding or rotation count — that is forced to be both even and odd for a thrackled even cycle pair.
- Settle the intermediate question: does every thrackle have a vertex of degree $\le 2$? A positive answer plus a suitable induction would give $e \le n$ directly, and the current minimum-degree results fall just short.
- Determine the true extremal constant for **generalized** thrackles, where the answer is *not* $n$; separating the two constants would locate exactly what the parity method loses.
- Classify musquashes and all extremal thrackles with $e = n$, which are conjecturally unicyclic with a single odd cycle.

## 9. Key References

- **[Foundational]** D. R. Woodall. *Thrackles and deadlock.* In: D. J. A. Welsh (ed.), Combinatorial Mathematics and its Applications, Academic Press, London, 1971, pp. 335–347.
- **[Foundational]** L. Lovász, J. Pach, M. Szegedy. *On Conway's thrackle conjecture.* Discrete & Computational Geometry 18 (1997), 369–376.
- **[Structural]** G. Cairns, Y. Nikolayevsky. *Bounds for generalized thrackles.* Discrete & Computational Geometry 23 (2000), 191–206.
- **[Structural]** G. Cairns, Y. Nikolayevsky. *Generalized thrackle drawings of non-bipartite graphs.* Discrete & Computational Geometry 41 (2009), 119–134.
- **[Special cases]** G. Cairns, M. McIntyre, Y. Nikolayevsky. *The thrackle conjecture for $K_5$ and $K_{3,3}$.* In: Towards a Theory of Geometric Graphs, Contemporary Mathematics 342, AMS, 2004, pp. 35–54.
- **[Special cases]** J. Pach, E. Sterling. *Conway's conjecture for monotone thrackles.* American Mathematical Monthly 118 (2011), 544–548.
- **[Special cases]** G. Cairns, Y. Nikolayevsky. *Outerplanar thrackles.* Graphs and Combinatorics 28 (2012), 85–96.
- **[SOTA]** R. Fulek, J. Pach. *A computational approach to Conway's thrackle conjecture.* Computational Geometry: Theory and Applications 44 (2011), 345–355.
- **[SOTA]** L. Goddyn, Y. Xu. *On the bounds of Conway's thrackles.* Discrete & Computational Geometry 58 (2017), 410–416.
- **[SOTA / Recent]** R. Fulek, J. Pach. *Thrackles: An improved upper bound.* Discrete Applied Mathematics 259 (2019), 226–231.
- **[Related]** A. J. Ruiz-Vargas, A. Suk, C. D. Tóth. *Disjoint edges in topological graphs and the tangled-thrackle conjecture.* European Journal of Combinatorics 51 (2016), 398–406.
- **[Survey]** P. Brass, W. Moser, J. Pach. *Research Problems in Discrete Geometry.* Springer, 2005 (Chapter 9, geometric graph theory; thrackle problems).

## 10. Worked Example / Concrete Special Case

**(a) $C_5$ is a thrackle with $e = n = 5$.** Place vertices at the fifth roots of unity, $v_j = (\cos(2\pi j/5), \sin(2\pi j/5))$, $j = 0,\dots,4$, and draw the straight segments $v_j v_{j+2}$ (indices mod 5) — the pentagram. The edge set is $\{v_0v_2, v_2v_4, v_4v_1, v_1v_3, v_3v_0\}$, a 5-cycle. Each edge is a "long diagonal"; two diagonals of a convex pentagon either share a vertex (and then do not cross) or cross exactly once. There are $\binom52 = 10$ pairs: $5$ adjacent, $5$ independent, and all $5$ independent pairs cross once inside the star. So $e = 5 = n$: the bound is attained. The same construction gives a thrackled $C_{2k+1}$ for every $k \ge 2$ using step $k$ on a convex $(2k+1)$-gon; these are Woodall's **musquashes**.

**(b) $C_4$ has no straight-line thrackle — full case check.** Let $a,b,c,d$ be four points in general position with edges $ab, bc, cd, da$. The independent pairs are $\{ab,cd\}$ and $\{bc,da\}$; both must cross.

- *Case 1: the four points are in convex position.* Among the three ways to pair them, exactly one pairing (the two diagonals) crosses; the other two pairings are pairs of opposite sides of the convex quadrilateral and are disjoint. If the convex order is $a,b,c,d$, then $ab, cd$ are opposite sides — no crossing. If the order is $a,c,b,d$, then $ab$ and $cd$ are the diagonals and do cross, but $bc$ and $da$ are then opposite sides — no crossing. Every relabelling reduces to one of these. So at most one of the two required crossings occurs.
- *Case 2: one point, say $d$, lies inside the triangle $abc$.* Then the segments $da$, $db$, $dc$ lie inside the triangle and meet the sides only at their endpoints; in particular $da$ does not cross $bc$. Failure again.

Hence no straight-line thrackle contains $C_4$. The same argument generalises: **a linear thrackle contains no even cycle**, and a graph in which every cycle is odd and no two cycles are independent has $e \le n$ — this is Erdős's proof of the conjecture in the linear case.

**(c) Where the general case departs.** $C_6$ *is* thrackleable with curved edges (draw the hexagon's vertices on a convex arc and route each edge as a long spiralling arc so that all $9$ independent pairs cross once), while by (b) it has no straight-line thrackle. So the linear proof does not transfer: curvature buys even cycles. What Conway's conjecture asserts is that curvature buys *at most one* independent cycle per component — and the smallest unresolved instance is exactly the figure-eight $C_6 \cdot C_6$ on $11$ vertices with $12$ edges, which would violate $e \le n$ if it were thrackleable.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*