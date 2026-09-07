---
id: 10-theoretical-cs/harborth-conjecture
title: "Harborth Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Harborth Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/harborth-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Harborth, 1987).** Every planar graph admits a plane straight-line drawing in which every edge has integer length.

Precisely: for every planar graph $G=(V,E)$ there is an injective map $p: V \to \mathbb{R}^2$ such that

1. the open segments $\overline{p(u)p(v)}$, $uv \in E$, are pairwise disjoint and meet no $p(w)$, $w \notin \{u,v\}$ (a *plane* drawing, in the sense of Fáry's theorem);
2. $\|p(u)-p(v)\|_2 \in \mathbb{Z}_{>0}$ for every $uv \in E$.

Such a drawing is called an **integral Fáry embedding**. No condition is imposed on non-adjacent pairs, on the size of the coordinates, or on the area of the drawing; the vertices need not be lattice points, and the integers need not be distinct or bounded.

A complete resolution is either (a) a construction (or existence proof) valid for every planar graph, or (b) a single planar graph $G$ together with a proof that no plane straight-line drawing of $G$ has all edge lengths integral. Because scaling by a common denominator turns rational lengths into integers, the conjecture is equivalent to its **rational** version: every planar graph has a plane straight-line drawing with all edge lengths in $\mathbb{Q}$.

## 2. Mathematical Foundations

**Fáry's theorem** (Fáry 1948; also Wagner 1936, Stein 1951): every simple planar graph has a plane drawing with straight-line edges. Harborth's conjecture asks to refine the *metric* of such drawings while keeping the *topology*.

**Realization space.** Fix a plane straight-line drawing $p_0$ of $G$ and let
$$\mathcal{R}(G,p_0) = \{\, p \in (\mathbb{R}^2)^V : p \text{ is plane and combinatorially equivalent to } p_0 \,\}.$$
$\mathcal{R}$ is a semialgebraic set, open in $(\mathbb{R}^2)^V \cong \mathbb{R}^{2n}$ (crossing-freeness and orientation conditions are strict polynomial inequalities). The edge-length map is
$$\ell: \mathcal{R} \to \mathbb{R}^{E}_{>0}, \qquad \ell(p)_{uv} = \|p(u)-p(v)\|_2 .$$
The conjecture asserts $\ell(\mathcal{R}) \cap \mathbb{Z}^{E} \neq \emptyset$ for some choice of $p_0$. Since $\ell$ involves square roots, the natural algebraic object is the squared-length map $\ell^2(p)_{uv} = \|p(u)-p(v)\|^2$, and the constraint "$\ell_{uv}\in\mathbb{Z}$" is the arithmetic condition that $\ell^2_{uv}$ be a perfect square — a Diophantine, not merely algebraic, requirement.

**Rational distance sets.** $S \subseteq \mathbb{R}^2$ is a *rational distance set* if $\|x-y\|\in\mathbb{Q}$ for all $x,y \in S$. The key positive tool is:

**Theorem (Almering 1963).** Let $T = \{a,b,c\}$ be a triangle with all three side lengths rational (a *rational triangle*). Then
$$D(T) = \{\, x \in \mathbb{R}^2 : \|x-a\|,\|x-b\|,\|x-c\| \in \mathbb{Q} \,\}$$
is dense in $\mathbb{R}^2$, and moreover every point of $D(T)$ together with any two of $a,b,c$ again spans a rational triangle.

Berry (1992) extended this to triangles with one rational side and two sides whose squares are rational. Almering's theorem gives a *dense* supply of new vertices at rational distance from an existing rational triangle — the engine behind all known partial results.

**Complexity backdrop (TCS framing).** The decision problem "given $G$ and prescribed integer edge lengths, is there a plane straight-line realization?" is NP-hard (Eades–Wormald 1990, even for prescribed unit lengths and fixed embedding), and general realizability questions of this type sit in $\exists\mathbb{R}$, the class of problems polynomial-time reducible to the existential theory of the reals. Harborth's conjecture is the *existential-over-all-length-assignments* relaxation, which removes the combinatorial hardness but replaces it with Diophantine difficulty.

## 3. History & State of the Art (SOTA)

- **1987.** Harborth, Kemnitz, Möller and Süssenbach (*Elemente der Mathematik* 42) give integral plane drawings of the graphs of the five Platonic solids, and Harborth poses the general conjecture. It sits alongside Harborth's other metric graph-drawing problems (matchstick graphs, integral point sets).
- **2001.** Kemnitz and Harborth, *Plane integral drawings of planar graphs* (Discrete Mathematics 236), systematize the question: integral drawings for further small and structured families, minimum-length integral drawings, and the reduction to rational lengths.
- **2008.** Geelen, Guo and McKinnon prove the conjecture for **planar graphs of maximum degree 3** (in particular all cubic planar graphs), using Almering's density theorem to place vertices one at a time.
- **2011.** Biedl (CCCG) extends integral drawings to further classes, notably planar graphs of **maximum degree 4** and certain 3-tree-like families, at the cost of allowing drawings that are not strictly convex.
- **2010–2020.** The "dense rational point set" route is closed off conditionally: Solymosi and de Zeeuw show that a rational distance set cannot be dense in the plane assuming the Bombieri–Lang conjecture; Shaffaf and, independently, Tao give related conditional arguments; Ascher, Braune and Turchet (2020) derive uniformity consequences. This says the *strongest possible* tool (a dense rational distance set, which would immediately prove Harborth by perturbation) almost certainly does not exist.

**SOTA summary.** Proved for max degree $\le 4$ and several structural families; open for max degree $\ge 5$, and in particular for maximal planar graphs (triangulations) of large degree. No planar graph is known or suspected to be a counterexample.

## 4. Partial Results / Verified Cases

| Class | Status | Source |
|---|---|---|
| Platonic solid graphs ($K_4$, cube, octahedron, dodecahedron, icosahedron) | integral drawings exhibited explicitly | Harborth–Kemnitz–Möller–Süssenbach 1987 |
| Planar graphs with $\Delta(G) \le 3$ | proved | Geelen–Guo–McKinnon 2008 |
| Planar graphs with $\Delta(G) \le 4$ | proved | Biedl 2011 |
| Trees, forests, outerplanar graphs, subdivisions of any planar graph | proved (trees: place leaves greedily via Almering density; every graph has an integrally drawable subdivision) | folklore / Kemnitz–Harborth 2001 |
| Planar 3-trees and related stacked triangulations | proved for the classes treated in Biedl 2011 *(scope varies by paper — check statement)* | Biedl 2011 |
| Small integral point sets in $\mathbb{Z}^2$ (minimum diameter, up to $\sim 100$ points) | exhaustively computed | Kurz–Wassermann, and Kurz's integral point set tables |
| Complete graphs $K_n$, $n\ge 5$ | not planar; irrelevant to the conjecture, but rational-distance $n$-point sets in general position are known only for $n \le 7$-type configurations | Erdős–Ulam circle |

Note the degree threshold is not an artifact of laziness: degree $\le 4$ is exactly where "add one vertex at a time and use density" still has enough freedom.

## 5. Principal Obstacles

- **Density is not enough at high degree.** Almering's theorem gives a dense set of points rational to *three* fixed anchors. Placing a vertex $v$ of degree $d$ requires rationality to $d$ already-placed neighbours simultaneously. For $d \le 3$ the anchors are a triangle and density applies directly; for $d \ge 4$ one needs a point rational to four prescribed points in general position, and no density theorem for four anchors is known. This is the exact place the induction stops.
- **The obvious global fix is (conditionally) false.** If some rational distance set were dense in $\mathbb{R}^2$, one could take any Fáry drawing, perturb every vertex into the dense set, and finish. Solymosi–de Zeeuw show this is impossible under Bombieri–Lang: an infinite rational distance set in general position must lie on a curve of genus $\le 1$ after finitely many exceptions. So no purely "topological perturbation" proof can work.
- **Rigidity of triangulations.** In a maximal planar graph, the combinatorial structure plus the edge lengths nearly determines the drawing (a triangulated plane framework is infinitesimally rigid in the sense of Cauchy-type arguments), so lengths cannot be adjusted edge-by-edge; changing one length propagates through the whole drawing. There is very little slack to round into $\mathbb{Q}$.
- **Arithmetic, not algebraic, difficulty.** The constraint set is a rational-point question on a variety of large dimension; standard tools (Fourier analysis, incidence geometry, the polynomial method) address *counting* rational distances, not *constructing* full drawings.
- **No hardness barrier to exploit.** The problem is existential over an uncountable parameter space, so the NP-hardness of fixed-length realizability (Eades–Wormald) gives no leverage either way.

## 6. The Gap

Everything proven flows from one statement: *a point at rational distance from three fixed rational-triangle vertices can be found in any open disc.* Everything unproven begins one degree higher. The precise missing step:

> **Four-anchor density.** Given four points $a,b,c,d \in \mathbb{R}^2$ in general position with all six pairwise distances rational, is $\{x : \|x-a\|,\|x-b\|,\|x-c\|,\|x-d\| \in \mathbb{Q}\}$ infinite? Dense in some open set?

Solymosi–de Zeeuw's conditional theorem suggests the four-anchor set is *not* dense — it is a curve-constrained set — but it does not rule out being infinite, nor does it rule out a smarter argument that also moves the anchors. Bridging the gap therefore requires either (i) a mechanism that places a high-degree vertex while simultaneously relocating its neighbours, i.e. a genuinely global rather than incremental construction, or (ii) a decomposition reducing arbitrary planar graphs to bounded-degree pieces whose integral drawings can be glued without breaking planarity or the already-fixed lengths.

## 7. Current Research (as of June 2026)

- **Graph-drawing community (CCCG/GD circles; Biedl's group at Waterloo and collaborators).** Continued extension of integral drawings to structured planar classes — series-parallel graphs, bounded-treewidth planar graphs, and drawings allowing polyline edges with integer segment lengths as a relaxation. *(frontier — verify: no published proof beyond $\Delta \le 4$ for straight-line drawings.)*
- **Arithmetic geometry.** Post-Ascher–Braune–Turchet work on uniformity for rational distance sets, quantifying how large a rational distance set in general position can be. Any unconditional four-anchor result would be a major advance and would immediately move the conjecture.
- **Computational search.** Exhaustive and SAT/SMT-assisted searches for integral drawings of specific small triangulations with a degree-5 or degree-6 vertex; every graph tested so far has been drawable. *(frontier — verify: results are scattered across notes and the Open Problem Garden entry rather than a single refereed source.)*
- **Relaxations.** Integer *squared* lengths, integer lengths with bends, and integral drawings on the sphere or with edges as circular arcs are being used as testbeds for which part of the difficulty is metric and which is topological.

## 8. Future Work

- Prove or refute infinitude of the four-anchor rational-distance set; even a single infinite family would likely push the theorem to $\Delta \le 5$.
- Develop a *simultaneous* placement method: instead of adding one vertex, perturb a whole triangulated patch inside its realization space, using the implicit function theorem to solve for rational lengths on a positive-dimensional family. The obstruction is that the resulting system is overdetermined once $|E| > 2|V| - 3$, which is exactly the triangulation regime.
- Settle the smallest genuinely open instance: a maximal planar graph with a vertex of degree 5 and no low-degree separator. A construction there would be strong evidence and might reveal the general mechanism.
- Attack the conjecture unconditionally under Bombieri–Lang and, separately, under its negation, to see whether Harborth is insensitive to that dichotomy.

## 9. Key References

- **[Foundational]** H. Harborth, A. Kemnitz, M. Möller, A. Süssenbach. *Ganzzahlige planare Darstellungen der platonischen Körper.* Elemente der Mathematik 42 (1987), 118–122.
- **[Foundational]** J. H. J. Almering. *Rational quadrilaterals.* Indagationes Mathematicae 25 (1963), 192–199.
- **[Foundational]** I. Fáry. *On straight line representation of planar graphs.* Acta Scientiarum Mathematicarum (Szeged) 11 (1948), 229–233.
- **[Key partial result]** J. Geelen, A. Guo, D. McKinnon. *Straight line embeddings of cubic planar graphs with integer edge lengths.* Journal of Graph Theory 58(3) (2008), 270–274.
- **[Key partial result]** T. Biedl. *Drawing some planar graphs with integer edge-lengths.* Proceedings of the 23rd Canadian Conference on Computational Geometry (CCCG), 2011.
- **[SOTA / Recent]** J. Solymosi, F. de Zeeuw. *On a question of Erdős and Ulam.* Discrete & Computational Geometry 43(2) (2010), 393–401.
- **[SOTA / Recent]** K. Ascher, L. Braune, A. Turchet. *The Erdős–Ulam problem, Lang's conjecture and uniformity.* Bulletin of the London Mathematical Society 52(6) (2020), 1053–1063.
- **[Related]** A. Kemnitz, H. Harborth. *Plane integral drawings of planar graphs.* Discrete Mathematics 236(1–3) (2001), 191–195.
- **[Complexity]** P. Eades, N. C. Wormald. *Fixed edge-length graph drawing is NP-hard.* Discrete Applied Mathematics 28(2) (1990), 111–134.
- **[Survey]** P. Brass, W. Moser, J. Pach. *Research Problems in Discrete Geometry.* Springer, 2005 (Chapter 5, integral distances).
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory,* 3rd ed., Springer, 2004 (Problem D20, rational distances).

## 10. Worked Example / Concrete Special Case

**Integral plane drawing of $K_4$.** $K_4$ is planar; its only plane straight-line embedding type is a triangle with one vertex inside, joined to all three corners. Take

$$A=(0,0),\quad B=(16,0),\quad C=(8,15),\quad P=(8,6).$$

Outer triangle:
$$\|AB\| = 16,\qquad \|AC\| = \sqrt{8^2+15^2} = \sqrt{289} = 17,\qquad \|BC\| = \sqrt{(-8)^2+15^2} = 17 .$$

Interior vertex:
$$\|PA\| = \sqrt{8^2+6^2} = \sqrt{100} = 10,\qquad \|PB\| = \sqrt{(-8)^2+6^2} = 10,\qquad \|PC\| = |15-6| = 9 .$$

All six edge lengths — $16,17,17,10,10,9$ — are integers.

*Planarity check.* $P=(8,6)$ lies strictly inside $\triangle ABC$: it is above the base $y=0$, and the lines $AC: 15x - 8y = 0$ and $BC: 15x + 8y = 240$ give $15\cdot 8 - 8\cdot 6 = 72 > 0$ and $15\cdot 8 + 8\cdot 6 = 168 < 240$, so $P$ is on the interior side of both. Hence $PA, PB, PC$ are contained in the closed triangle and meet only at $P$; no two edges cross. No three of the four points are collinear (the triangle has positive area $\tfrac12\cdot16\cdot15 = 120$).

*What this illustrates.* The point $P$ is exactly an Almering-style witness: it realizes a point at integer distance from all three vertices of the integral triangle $ABC$. Almering's theorem says such $P$ can be found in *any* disc, which is what lets Geelen–Guo–McKinnon insert vertices of degree $\le 3$ without disturbing planarity. The conjecture becomes hard the moment a vertex needs integer distances to four prescribed points at once — here, if $K_4$ were extended to a triangulation forcing a degree-5 interior vertex, no analogue of the calculation above is available.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*