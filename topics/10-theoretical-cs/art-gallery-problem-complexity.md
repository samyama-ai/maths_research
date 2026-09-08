---
id: 10-theoretical-cs/art-gallery-problem-complexity
title: "Art Gallery Problem Complexity"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Art Gallery Problem Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/art-gallery-problem-complexity` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Given a simple polygon $P$ with $n$ vertices and an integer $k$, decide whether there is a set $G \subseteq P$ of at most $k$ points ("guards") such that every point of $P$ is visible from some guard, where two points see each other iff the closed segment joining them lies inside $P$.

The combinatorial question — how many guards always suffice — was settled in 1975 ($\lfloor n/3 \rfloor$, tight). The **complexity** question was the long-standing open problem: the decision version was known NP-hard since 1986, but for four decades no one could prove it lay in NP, because optimal guard coordinates were not known to be describable by polynomially many bits.

This was resolved: the problem is **complete for the existential theory of the reals** $\exists\mathbb{R}$ (Abrahamsen, Adamaszek, Miltzow, STOC 2018; JACM 2022). Consequently it is in NP iff $\exists\mathbb{R} = \mathrm{NP}$, which is not expected.

What remains open, and is what this page tracks:

1. **Approximability.** Does point guarding of a simple polygon admit a constant-factor approximation in polynomial time? Best known is $O(\log \mathrm{OPT})$.
2. **Restricted geometries.** Is the point-guard problem on *orthogonal* polygons in NP?
3. **Vertex guards.** Does the NP-hard vertex-guard version on simple polygons admit a PTAS?

A complete resolution of (1) means either a polynomial $O(1)$-approximation algorithm or an APX-hardness-style lower bound ruling one out under a standard assumption.

## 2. Mathematical Foundations

**Polygon and visibility.** Let $P \subset \mathbb{R}^2$ be a closed simply connected region bounded by a closed polygonal curve with vertex sequence $v_1,\dots,v_n \in \mathbb{Q}^2$. Define

$$\mathrm{Vis}(x) \;=\; \{\, y \in P \;:\; [x,y] \subseteq P \,\}, \qquad [x,y] = \{(1-t)x + ty : t \in [0,1]\}.$$

$G \subseteq P$ *guards* $P$ iff $\bigcup_{g \in G} \mathrm{Vis}(g) = P$. Write $\mathrm{OPT}(P) = \min\{|G| : G \text{ guards } P\}$ (the minimum exists; $\mathrm{Vis}$ is a semialgebraic family).

**Variants.** *Point guards*: $G \subseteq P$. *Vertex guards*: $G \subseteq \{v_1,\dots,v_n\}$. *Boundary/perimeter guards*: $G \subseteq \partial P$. *Edge guards*: guards are full edges.

**Chvátal's Art Gallery Theorem.** For every simple $n$-gon, $\mathrm{OPT}(P) \le \lfloor n/3 \rfloor$, and this is tight. For orthogonal polygons the bound is $\lfloor n/4 \rfloor$ (Kahn–Klawe–Kleitman). For polygons with $h$ holes, $\lfloor (n+h)/3 \rfloor$ guards suffice.

**The complexity class $\exists\mathbb{R}$.** The *existential theory of the reals* (ETR) is the set of true sentences

$$\exists x_1,\dots,x_m \in \mathbb{R} : \Phi(x_1,\dots,x_m),$$

with $\Phi$ quantifier-free over the signature $(+,\cdot,\,=,\,<,\,0,\,1)$. $\exists\mathbb{R}$ is the class of problems polynomial-time many-one reducible to ETR. Canny (1988) proved $\mathrm{ETR} \in \mathrm{PSPACE}$, and NP-hardness is immediate, so

$$\mathrm{NP} \;\subseteq\; \exists\mathbb{R} \;\subseteq\; \mathrm{PSPACE}.$$

**Membership.** ART GALLERY $\in \exists\mathbb{R}$: introduce coordinates $(x_i,y_i)$ for $k$ guards; the arrangement of the $O(n^2)$ lines through vertex pairs cuts $P$ into $O(n^4)$ cells with the property that a cell is either fully seen or fully unseen from a guard in a fixed cell, so full coverage is expressible by a polynomial-size existential formula.

**Hardness core.** The reduction of Abrahamsen–Adamaszek–Miltzow builds polygon gadgets whose guard positions along "corridors" encode real variables $x \in [0,1]$, with further gadgets forcing $x + y = z$ and $x \cdot y = z$ by projective (perspective) relations between corridors. This realises ETR-in-the-range-$[1/2,2]$ inside a polygon of size polynomial in the formula.

## 3. History & State of the Art (SOTA)

- **1973.** Victor Klee poses the guarding question to Chvátal.
- **1975.** Chvátal proves $\lfloor n/3 \rfloor$ suffices and is tight (*J. Combin. Theory Ser. B*).
- **1978.** Fisk gives the celebrated three-line proof by triangulation and 3-colouring.
- **1983.** Kahn, Klawe, Kleitman: $\lfloor n/4 \rfloor$ for orthogonal polygons.
- **1986.** Lee and Lin: minimum vertex guarding is NP-hard (reduction from 3SAT); Aggarwal extends to point and edge guards.
- **1987/2010.** Ghosh: $O(\log n)$-approximation for vertex and edge guards.
- **1998–2001.** Eidenbenz, Stamm, Widmayer: APX-hardness for simple polygons; $\Omega(\log n)$ inapproximability for polygons with holes unless $\mathrm{P}=\mathrm{NP}$.
- **2002.** Efrat and Har-Peled: randomized $O(\log \mathrm{OPT})$-approximation for vertex guards, via $\varepsilon$-nets for the visibility set system.
- **2017.** Abrahamsen, Adamaszek, Miltzow: *irrational guards are sometimes needed* — a polygon with rational vertices whose optimal 3-guard solutions all use irrational coordinates. This killed the standard route to NP-membership.
- **2018/2022.** Same authors: **ART GALLERY is $\exists\mathbb{R}$-complete** (STOC 2018; *Journal of the ACM* 69(1), 2022). This is the headline resolution.
- **2023–2024.** Stade shows the *point-boundary* and boundary-guarding variants are $\exists\mathbb{R}$-hard; Stade and Tucker-Foltz prove topological universality — solution spaces of art gallery instances realise arbitrary (compact semialgebraic, up to homotopy) topology.

## 4. Partial Results / Verified Cases

- **Combinatorial bounds (fully solved).** $\lfloor n/3 \rfloor$ for simple polygons; $\lfloor n/4 \rfloor$ for orthogonal; $\lfloor (n+h)/3 \rfloor$ for $h$ holes (Bjorling-Sachs–Souvaine; Hoffmann–Kaufmann–Kriegel, 1991–95).
- **Vertex guards.** Finitely many candidates $\Rightarrow$ the problem is in NP, hence **NP-complete** for simple polygons and for polygons with holes.
- **$\exists\mathbb{R}$-completeness.** Holds for point guards in simple polygons with rational vertices, already for the "guard everything" version; also for guards restricted to $\partial P$ (Stade).
- **Terrain guarding** ($x$-monotone chains): NP-hard (King and Krohn, 2011) but admits a **PTAS** (Gibson, Kanade, Krohn, Varadarajan, 2009) — a strictly easier landscape than general polygons.
- **Weak visibility polygons** (every point seen from some edge): constant-factor approximation for vertex guarding (Bhattacharya, Ghosh, Roy, *Discrete Applied Mathematics*, 2017), and this bootstraps to $O(\log \mathrm{OPT})$ overall.
- **Point guards, simple polygons:** $O(\log \mathrm{OPT})$-approximation (Bonnet and Miltzow, SoCG 2017); perimeter guarding of simple galleries: $O(\log\log \mathrm{OPT})$ (King and Kirkpatrick, 2011).
- **Practice.** Exact IP/CP solvers (Couto, de Rezende, de Souza) solve vertex-guard instances with $n$ in the thousands; Hengeveld and Miltzow (SoCG 2021) give a practical algorithm with guarantees for the point-guard case.
- **Special shapes solved in $O(n)$ or $O(n\log n)$:** spiral polygons, monotone polygons for certain guard types, and $r$-guarding (rectangle visibility) of orthogonal polygons, which is polynomial via perfect-graph / matching structure (Worman and Keil, 2007; Katz and Roisman).

## 5. Principal Obstacles

- **No finite candidate set.** Almost every combinatorial optimisation technique (LP/IP relaxation, set cover, local search, kernelization) presumes a polynomial universe of candidate solutions. The irrational-guards construction shows optimal guards can be forced to algebraic irrationals, so discretising the polygon at any polynomial-size grid loses optimality.
- **Real-algebraic bit complexity.** The $\exists\mathbb{R}$-completeness proof yields instances whose optimal guard coordinates require doubly exponential precision to write down. Any NP certificate would have to compress that; no known technique does.
- **Infinite VC-type covering.** The set system $\{\mathrm{Vis}(g)\}_{g\in P}$ has bounded VC dimension, so $\varepsilon$-net machinery gives $O(\log \mathrm{OPT})$, but breaking $\log$ needs *shallow* or *union-complexity* bounds for visibility regions. Visibility polygons have union complexity $\Theta(n^2)$ in the worst case, which is exactly the regime where net-based methods stall at logarithmic factors.
- **Local search fails.** For geometric set cover, local search yields PTASs when the range space admits sublinear separators. Visibility regions are non-convex and non-fat; no separator theorem is known for them, and terrain guarding's PTAS relies on the *order claim* (a total order along the terrain making visibility "laminar"), which has no analogue in a general polygon.
- **Hardness side is blocked too.** APX-hardness gives only a constant lower bound $(1+\varepsilon)$; ruling out an $O(1)$-approximation would need a gap-amplifying, geometry-preserving reduction, and geometric embeddings tend to destroy expander-like gap structure.

## 6. The Gap

Proven: exact solving is $\exists\mathbb{R}$-complete; approximation is possible to factor $O(\log \mathrm{OPT})$ and impossible to factor $1+\varepsilon$ for small $\varepsilon>0$ unless $\mathrm{P}=\mathrm{NP}$.

The gap is the interval between $1+\varepsilon$ and $O(\log \mathrm{OPT})$. Closing it from above requires an $\varepsilon$-net of size $O(1/\varepsilon)$ for the visibility range space of a simple polygon — equivalently, a proof that the natural LP has $O(1)$ integrality gap. Closing it from below requires a PCP-style reduction into planar visibility that preserves a super-constant gap.

A second, sharper gap: for orthogonal polygons with integer vertices, no irrational-guard example is known and no NP-membership proof is known. The exact step needed is a *rationality theorem*: show every orthogonal instance has an optimum on a polynomial-size grid (e.g. half-integral), which would place it in NP; or transfer the AAM gadgets to axis-parallel geometry, which currently fails because the perspective gadgets that implement multiplication need non-axis-parallel sightlines.

## 7. Current Research (as of June 2026)

- **$\exists\mathbb{R}$ as a geometry-wide framework.** Groups at TU Eindhoven (Miltzow), Utrecht, FU Berlin (Mulzer, Cardinal), and Copenhagen (Abrahamsen) are pushing $\exists\mathbb{R}$-completeness through packing, Nash equilibria, geometric embedding and training neural networks; art gallery is the template reduction.
- **Topological universality.** Stade and Tucker-Foltz (SoCG 2024) show art gallery solution spaces are universal, implying no "combinatorial normal form" for optima can exist — a strong structural barrier.
- **Boundary and restricted-guard variants.** Stade's $\exists\mathbb{R}$-hardness for point-boundary guarding closes one of the main sub-cases left open in the JACM paper.
- **Approximation.** Continuing effort on constant-factor point guarding of simple polygons via weak-visibility decomposition; incremental improvements to constants for weak-visibility and monotone polygons. *(frontier — verify: several arXiv preprints claim $O(1)$ approximations for restricted classes; none is accepted for the general simple-polygon point-guard case.)*
- **Exact practical solvers.** Cutting-plane and semi-infinite-programming solvers converging to provable optima on polygons with hundreds of vertices, including irrational witnesses handled symbolically.

## 8. Future Work

- Prove or refute a constant integrality gap for the visibility set-cover LP on simple polygons.
- Establish a separator or union-complexity bound for visibility regions inside a simple polygon that would enable local-search PTAS analysis.
- Settle NP-membership for orthogonal point guarding by a rationality/grid theorem.
- Determine the complexity of art gallery variants with *bounded guard range* or *fat* polygons, where candidate discretisation may be recoverable.
- Extend $\exists\mathbb{R}$-completeness to 3D guarding (polyhedral terrains, illumination of polyhedra), where even the combinatorial theory has no $\lfloor n/3\rfloor$ analogue.
- Parameterized complexity: is vertex guarding FPT in $k$? Known W[1]-hard for polygons with holes; the simple-polygon case remains a target.

## 9. Key References

- **[Foundational]** V. Chvátal. *A combinatorial theorem in plane geometry.* Journal of Combinatorial Theory, Series B, 18(1):39–41, 1975.
- **[Foundational]** S. Fisk. *A short proof of Chvátal's watchman theorem.* Journal of Combinatorial Theory, Series B, 24(3):374, 1978.
- **[Foundational]** J. Kahn, M. Klawe, D. Kleitman. *Traditional galleries require fewer watchmen.* SIAM Journal on Algebraic and Discrete Methods, 4(2):194–206, 1983.
- **[Foundational]** D. T. Lee, A. K. Lin. *Computational complexity of art gallery problems.* IEEE Transactions on Information Theory, 32(2):276–282, 1986.
- **[Foundational]** J. Canny. *Some algebraic and geometric computations in PSPACE.* Proc. 20th ACM Symposium on Theory of Computing (STOC), 460–467, 1988.
- **[SOTA]** M. Abrahamsen, A. Adamaszek, T. Miltzow. *The Art Gallery Problem is $\exists\mathbb{R}$-complete.* Journal of the ACM, 69(1), Article 4, 2022. (Conference version: STOC 2018.)
- **[SOTA]** M. Abrahamsen, A. Adamaszek, T. Miltzow. *Irrational guards are sometimes needed.* Proc. 33rd International Symposium on Computational Geometry (SoCG), 2017.
- **[SOTA]** É. Bonnet, T. Miltzow. *An approximation algorithm for the art gallery problem.* Proc. 33rd International Symposium on Computational Geometry (SoCG), 2017.
- **[SOTA]** J. Stade, J. Tucker-Foltz. *Topological universality of the art gallery problem.* Proc. 40th International Symposium on Computational Geometry (SoCG), 2024.
- **[Recent]** S. Hengeveld, T. Miltzow. *A practical algorithm with performance guarantees for the art gallery problem.* Proc. 37th International Symposium on Computational Geometry (SoCG), 2021.
- **[Recent]** M. Gibson, G. Kanade, E. Krohn, K. Varadarajan. *An approximation scheme for terrain guarding.* APPROX-RANDOM, LNCS 5687, 140–148, 2009.
- **[Recent]** J. King, E. Krohn. *Terrain guarding is NP-hard.* SIAM Journal on Computing, 40(5):1316–1339, 2011.
- **[Recent]** S. Eidenbenz, C. Stamm, P. Widmayer. *Inapproximability results for guarding polygons and terrains.* Algorithmica, 31(1):79–113, 2001.
- **[Survey]** J. O'Rourke. *Art Gallery Theorems and Algorithms.* Oxford University Press, 1987.
- **[Survey]** S. K. Ghosh. *Visibility Algorithms in the Plane.* Cambridge University Press, 2007.
- **[Survey]** M. Schaefer, D. Štefankovič. *Fixed points, Nash equilibria, and the existential theory of the reals.* Theory of Computing Systems, 60(2):172–193, 2017.

## 10. Worked Example / Concrete Special Case

**(a) The comb: tightness of $\lfloor n/3 \rfloor$.** Fix $m \ge 1$ and build a comb with $m$ prongs: a horizontal base with $m$ thin spikes rising from it, spike $i$ having apex $a_i$ and two base corners. The vertex count is $n = 3m$.

Each spike is a thin triangle whose apex $a_i$ is visible only from points inside spike $i$'s own wedge; the wedges are pairwise disjoint. So no single guard sees two apexes, forcing $\mathrm{OPT} \ge m = n/3$. Placing one guard at each spike's base midpoint sees the whole spike plus a slab of the base, and $m$ such guards cover $P$. Hence $\mathrm{OPT} = m = \lfloor n/3 \rfloor$ exactly.

**(b) Fisk's upper bound on a hexagon.** Take $P$ with vertices
$$v_1=(0,0),\; v_2=(4,0),\; v_3=(4,4),\; v_4=(2,2),\; v_5=(0,4),\; v_6=(-1,2),$$
a hexagon with one reflex vertex at $v_4$ (the notch). Triangulate: $\{v_1v_2v_4\}$? — check visibility; a valid triangulation is $T_1=v_1v_2v_4$, $T_2=v_2v_3v_4$, $T_3=v_1v_4v_5$, $T_4=v_1v_5v_6$. The dual of a triangulation of a simple polygon is a tree, so the triangulation graph is 3-colourable; one valid colouring is

$$c(v_1)=1,\; c(v_2)=2,\; c(v_4)=3,\; c(v_3)=1,\; c(v_5)=2,\; c(v_6)=3.$$

Every triangle carries all three colours, so each colour class is a guard set. Class sizes are $|c^{-1}(1)|=|c^{-1}(2)|=|c^{-1}(3)|=2$, so $\mathrm{OPT} \le 2 = \lfloor 6/3 \rfloor$. Here in fact $\mathrm{OPT}=1$: the point $(2,0.5)$ sees all of $P$ — showing the theorem is a worst-case bound, not an algorithm.

**(c) Why irrationality enters.** In the AAM construction, two guards $g$ and $g'$ sit on parallel corridors at abscissae $x$ and $x'$. A pocket forces the sightline from $g$ through a fixed pivot $p$ to reach past $g'$, which after similar triangles gives a relation of the form
$$x' \;=\; \frac{\alpha x + \beta}{\gamma x + \delta},\qquad \alpha\delta - \beta\gamma \ne 0 ,$$
a Möbius map with rational coefficients. Composing several such gadgets around a cycle produces a fixed-point condition $x = M(x)$ with $M$ a rational Möbius map, i.e. a quadratic $\gamma x^2 + (\delta - \alpha)x - \beta = 0$. Choosing $\gamma=\delta=\alpha=1,\beta=1$ gives $x^2 = 1 + x$ — wait, explicitly $x = (x+1)/x$ yields
$$x^2 - x - 1 = 0, \qquad x = \frac{1+\sqrt{5}}{2},$$
an irrational forced position in a polygon with rational vertices. Chaining $O(m)$ such constraints lets the polygon simulate arbitrary polynomial systems, and repeated squaring gadgets force coordinates of doubly exponential height — the precise reason no polynomial-size certificate is available and the problem sits at $\exists\mathbb{R}$ rather than NP.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*