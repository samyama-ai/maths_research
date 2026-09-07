---
id: 07-combinatorics/harborths-conjecture
title: "Harborth's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Harborth's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/harborths-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Harborth, 1987).** Every planar graph admits a plane straight-line drawing in which every edge has integer Euclidean length.

Formally: for every planar graph $G=(V,E)$ there is an injective map $\varphi : V \to \mathbb{R}^2$ such that

1. the open straight segments $\varphi(u)\varphi(v)$, $uv \in E$, are pairwise disjoint and contain no image of a vertex (a *Fáry embedding*), and
2. $\lVert \varphi(u)-\varphi(v)\rVert \in \mathbb{Z}_{>0}$ for every $uv \in E$.

Such a $\varphi$ is called an **integral Fáry embedding**. A proof must supply (or prove the existence of) such a drawing for every planar $G$; a disproof must exhibit one planar graph for which no integral Fáry embedding exists.

Two normalizations are harmless. Rational edge lengths suffice: scaling by the least common denominator gives integer lengths. And it suffices to treat maximal planar graphs (triangulations), since every planar graph is a spanning subgraph of one — but the added edges must also be integral, so this reduction *strengthens* the problem rather than weakening it. It is not known whether the vertex coordinates can additionally be taken rational.

## 2. Mathematical Foundations

**Fáry's theorem.** Every simple planar graph has a plane drawing with straight-line edges (Fáry 1948; Wagner 1936; Stein 1951). Harborth's conjecture asks whether the metric constraint of integrality can be imposed on top of this topological fact.

**Distance variety.** Fix a combinatorial embedding of $G$ with $n=|V|$, $m=|E|$. The realization space is cut out in $\mathbb{R}^{2n}$ by

$$\big(x_u-x_v\big)^2+\big(y_u-y_v\big)^2 \;=\; \ell_{uv}^2, \qquad uv\in E,\ \ell_{uv}\in\mathbb{Z}_{>0},$$

subject to the open conditions that all faces be simple and correctly oriented. Modulo the $3$-dimensional group of orientation-preserving isometries, there are $2n-3$ free parameters against $m$ equations. For a triangulation $m=3n-6$, so the system is overdetermined by $n-3$ equations: integrality cannot be achieved by generic parameter counting and must exploit arithmetic.

**Rational-distance sets.** For $S\subset\mathbb{R}^2$ let $\mathcal{R}(S)=\{p : \lVert p-s\rVert\in\mathbb{Q}\ \ \forall s\in S\}$.

- **Almering's theorem (1963).** If $T=\{A,B,C\}$ is a non-degenerate triangle with all pairwise distances rational, then $\mathcal{R}(T)$ is *dense* in $\mathbb{R}^2$, and every point of $\mathcal{R}(T)$ is again at rational distance from all of $T$, so the configuration extends.
- **Berry (1992)** extended density to triangles with rational squared side lengths and one rational side.
- **Erdős–Anning theorem (1945).** An infinite set with all pairwise distances integral is collinear. Hence integral point sets in general position are finite, and lengths must grow with $n$.
- **Erdős–Ulam problem.** Is there a dense $S\subset\mathbb{R}^2$ with all pairwise distances rational? Solymosi and de Zeeuw (2010) proved a rational-distance set can be infinite on an algebraic curve only if the curve is a line or a circle; Ascher, Braune and Turchet (2020) showed that the Bombieri–Lang conjecture implies no dense rational-distance set exists. So the "one universal dense rational grid" route is blocked.

**Degree bookkeeping.** Adding a vertex $v$ of degree $d$ to an already-integral partial drawing requires a point at rational distance from $d$ prescribed points. For $d\le 3$ Almering supplies a dense supply of choices (so the point can be placed in any prescribed open region, preserving planarity). For $d\ge 4$ no analogue is known — this is exactly the Erdős–Ulam barrier.

## 3. History & State of the Art (SOTA)

Heiko Harborth (TU Braunschweig) and collaborators studied *integral point sets* and *integral drawings* through the 1980s. The conjecture is standardly attributed to Harborth, Kemnitz, Möller and Süssenbach, *Ganzzahlige planare Darstellungen der platonischen Körper* (Elemente der Mathematik, 1987), which exhibits integral plane straight-line drawings of the graphs of all five Platonic solids. Kemnitz and Harborth, *Plane integral drawings of planar graphs* (Discrete Mathematics 236, 2001), gave further constructions and small-graph results and recorded the general conjecture explicitly.

Milestones:

- **1963/1992 — arithmetic engine.** Almering's density theorem, later refined by Berry, supplies the tool used by every subsequent positive result.
- **2008 — cubic planar graphs.** Geelen, Guo and McKinnon proved every planar graph of maximum degree $3$ has an integral Fáry embedding, by an incremental vertex-insertion argument built on Almering density (Journal of Graph Theory 58).
- **2013 — degree four.** T. Sun, *Rigidity-theoretic constructions of integral Fáry embeddings* (CCCG 2013), extended the class to planar graphs of maximum degree $4$, and gave constructions based on flexing rational-distance frameworks. *(frontier — verify exact scope of the degree-4 statement)*
- **Ongoing — computational.** Explicit small integral drawings (Platonic and Archimedean skeleta, wheels, small triangulations) are catalogued, along with minimum-diameter integral point sets (Kurz and Wassermann).

No planar graph is known to lack an integral Fáry embedding, and no counterexample candidate has been proposed; the conjecture is widely believed true.

## 4. Partial Results / Verified Cases

- **Trees and forests.** Trivial: place vertices greedily on rational-distance circles; any tree has an integral plane drawing.
- **Cycles, and hence all outerplanar graphs of maximum degree $\le 3$.** Covered by the degree-$3$ theorem.
- **Maximum degree $\le 3$ (cubic planar graphs).** Fully proved, Geelen–Guo–McKinnon (2008). Covers the cube $Q_3$, the dodecahedron, the Petersen-like planar cubic families, all $3$-regular planar triangulation duals.
- **Maximum degree $4$.** Proved by Sun (2013), covering the octahedron and all $4$-regular planar (medial) graphs. *(frontier — verify)*
- **The five Platonic skeleta.** Explicit integral drawings, all five, Harborth–Kemnitz–Möller–Süssenbach (1987) — including the icosahedron, whose maximum degree is $5$ and which is therefore *not* covered by any general theorem.
- **Small $n$.** Exhaustive/constructive verifications exist for all planar graphs on few vertices; $K_4$, $K_{2,3}$, wheels $W_n$ for small $n$, and prisms have published integral drawings.
- **Crossings allowed.** *Every* graph (planar or not) has a straight-line drawing with rational edge lengths — place all vertices in a dense rational-distance subset of a circle. Planarity is the entire difficulty.

## 5. Principal Obstacles

- **Degree $\ge 5$ insertion has no arithmetic tool.** All proofs place one vertex at a time at rational distance from its already-placed neighbours. The known density theorems (Almering, Berry) handle at most three prescribed points. Producing a point at rational distance from four points in general position is an open Diophantine problem in its own right, tied to the Erdős–Ulam problem; the Solymosi–de Zeeuw and Ascher–Braune–Turchet results say a *dense* universal solution set does not exist (unconditionally on curves, conditionally in the plane under Bombieri–Lang). So the degree-$4$ frontier is not a technical gap but a genuine arithmetic wall.
- **Overdetermination.** For triangulations the constraint count $3n-6$ exceeds the $2n-3$ moduli. Continuous deformation methods (rigidity theory, perturbation of an approximate solution) cannot absorb $n-3$ extra equations; one needs the variety to carry rational points, which is a global arithmetic question about a high-dimensional variety with no known structure.
- **No compactness or limit argument.** Erdős–Anning forces edge lengths to blow up; there is no bound on the diameter of an integral drawing in terms of $n$, so approximate-then-round schemes fail: rounding a real drawing to integer lengths destroys planarity or feasibility.
- **Order matters.** Vertex-insertion orders (canonical orderings, Schnyder woods) control planarity but not degree; every planar triangulation on $n\ge 5$ vertices has a vertex of degree $\ge 5$ somewhere in any insertion order, and the minimum-degree bound $\delta\le 5$ is sharp (icosahedron).
- **No obstruction theory.** There is also no candidate invariant that could certify a counterexample, so the problem is one-sided: nobody knows what a "hard" planar graph would look like.

## 6. The Gap

Proved: planar graphs with $\Delta(G)\le 4$. Conjectured: all planar graphs, i.e. $\Delta(G)$ unbounded.

The precise step to be crossed is one of the following two, either would suffice for a big advance:

1. **Local arithmetic step.** Given points $P_1,\dots,P_k$ ($k\ge 4$) in the plane with pairwise rational distances, show that $\mathcal{R}(\{P_1,\dots,P_k\})$ is nonempty in every prescribed open disc — or at least in the discs arising from planar insertion. Note this cannot hold for *all* configurations in the strong dense form without contradicting the expected answer to Erdős–Ulam, so the correct statement must exploit the freedom to *move the earlier vertices too*.
2. **Global flexing step.** Prove that the real realization space of an integral partial triangulation contains a rational point in each of its connected components — a Hasse-principle-type statement for Cayley–Menger varieties. Current rigidity arguments produce one-parameter flexes with only finitely many rational specializations, insufficient once $n-3$ extra constraints appear.

## 7. Current Research (as of June 2026)

- **Rigidity-theoretic constructions.** Following Sun, groups in computational geometry (Columbia, TU Braunschweig, Waterloo) study frameworks that keep a subset of edges flexible while integrality is imposed on the rest — moving from "insert one vertex" to "insert one rigid gadget". *(frontier — verify)*
- **Diophantine geometry of Cayley–Menger varieties.** The Erdős–Ulam circle (Solymosi, de Zeeuw, Ascher, Braune, Turchet, Tao's expository work) supplies the negative side: which rational-distance configurations *cannot* be dense. This is now the standard reference frame for why degree-$4$ insertion is hard.
- **Integral point sets.** Kurz, Wassermann and collaborators continue exhaustive computation of integral point sets in general position, minimum diameter, and characteristic — the raw material for explicit drawings.
- **Relaxations.** Integral drawings with polyline edges, with edges of prescribed *rational-square* length, or after subdividing each edge a bounded number of times, are studied as approachable surrogates. *(frontier — verify current best subdivision bound)*
- **Related conjecture.** Whether every planar graph has a plane drawing with integer *coordinates* and integer edge lengths is open even for $\Delta\le3$.

## 8. Future Work

- Prove a "moving-target" density theorem: given a rational-distance set $S$ and a target region $U$, show one may perturb $S$ within its rational-distance realization space so that some point of $U$ is at rational distance from a prescribed $4$-subset.
- Settle the icosahedron-style case structurally: characterize which degree-$5$ insertions into an integral triangulation are realizable, generalizing the ad hoc 1987 constructions.
- Attack $4$-connected planar triangulations directly using Schnyder woods, where each region-of-freedom is combinatorially controlled.
- Establish or refute integral drawings for maximal outerplanar graphs (polygon triangulations) of unbounded degree — the simplest family outside current theorems.
- Develop a certified search: SAT/SMT plus number-theoretic filters to decide integrality for specific small triangulations of high degree, to test whether counterexample candidates exist at all.

## 9. Key References

- **[Foundational]** H. Harborth, A. Kemnitz, M. Möller, A. Süssenbach. *Ganzzahlige planare Darstellungen der platonischen Körper.* Elemente der Mathematik, 42 (1987), 118–122.
- **[Foundational]** A. Kemnitz, H. Harborth. *Plane integral drawings of planar graphs.* Discrete Mathematics, 236 (2001), 191–195.
- **[Foundational]** J. H. J. Almering. *Rational quadrilaterals.* Indagationes Mathematicae, 25 (1963), 192–199.
- **[Foundational]** T. G. Berry. *Points at rational distance from the vertices of a triangle.* Acta Arithmetica, 62 (1992), 391–398.
- **[Foundational]** P. Erdős, N. H. Anning. *Integral distances.* Bulletin of the American Mathematical Society, 51 (1945), 598–600.
- **[SOTA]** J. Geelen, A. Guo, D. McKinnon. *Straight line embeddings of cubic planar graphs with integer edge lengths.* Journal of Graph Theory, 58 (2008), 270–274.
- **[SOTA]** T. Sun. *Rigidity-theoretic constructions of integral Fáry embeddings.* Proceedings of the 25th Canadian Conference on Computational Geometry (CCCG), 2013.
- **[SOTA]** J. Solymosi, F. de Zeeuw. *On a question of Erdős and Ulam.* Discrete & Computational Geometry, 43 (2010), 393–401.
- **[SOTA]** K. Ascher, L. Braune, A. Turchet. *The Erdős–Ulam problem, Lang's conjecture and uniformity.* Bulletin of the London Mathematical Society, 52 (2020), 1053–1063.
- **[Survey]** P. Brass, W. Moser, J. Pach. *Research Problems in Discrete Geometry.* Springer, 2005 (integral distances and integral drawings).
- **[Survey]** S. Kurz, A. Wassermann. *On the minimum diameter of plane integral point sets.* Ars Combinatoria, 101 (2011), 265–287.
- **[Context]** I. Fáry. *On straight line representation of planar graphs.* Acta Scientiarum Mathematicarum (Szeged), 11 (1948), 229–233.

## 10. Worked Example / Concrete Special Case

**Goal:** an integral Fáry embedding of $K_4$ — the smallest planar graph where all six pairwise distances must be integers *and* one vertex sits inside the triangle of the other three.

Take an isosceles frame with the fourth vertex on the axis of symmetry:

$$A=(-12,0),\qquad B=(12,0),\qquad C=(0,35),\qquad P=(0,16).$$

Distances:

$$|AB| = 24,\qquad |AC|=|BC|=\sqrt{12^2+35^2}=\sqrt{144+1225}=\sqrt{1369}=37,$$
$$|AP|=|BP|=\sqrt{12^2+16^2}=\sqrt{144+256}=\sqrt{400}=20,\qquad |CP| = 35-16 = 19.$$

All six edge lengths $\{24,37,37,20,20,19\}$ are integers. Since $0<16<35$ and $P$ lies on the axis strictly between $AB$ and $C$, $P$ is interior to triangle $ABC$; the drawing with outer face $ABC$ and three internal edges $PA,PB,PC$ has no crossings. This is an integral Fáry embedding of $K_4$.

**Where the numbers come from.** The construction needs $x$ with two distinct solutions of $x^2+t^2=\square$. For $x=12$, factoring $(m-t)(m+t)=144$ over same-parity pairs gives $t\in\{5,9,16,35\}$ with hypotenuses $\{13,15,20,37\}$. Choosing the largest for $C$ and another for $P$ makes $|CP|=35-16=19$ automatically integral, because both lie on the $y$-axis. By contrast $x=6$ admits only $t=8$ (the pair $(2,18)$), so no such pair of heights exists — this is the arithmetic scarcity that makes the general problem hard.

**Where it breaks down.** Extend to $K_4$ plus one vertex $Q$ inside triangle $APB$ joined to $A,P,B$: this vertex has degree $3$, and Almering's theorem applied to the rational triangle $\{A,P,B\}$ gives a dense set of admissible positions, so a valid $Q$ exists inside the required face — this is precisely the Geelen–Guo–McKinnon step. But if $Q$ must also join $C$ (degree $4$), density is no longer available: one needs a point at rational distance from all four of $A,B,C,P$ simultaneously, and no theorem guarantees such a point exists in the prescribed face. That single jump from three neighbours to four is the whole of Harborth's conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*