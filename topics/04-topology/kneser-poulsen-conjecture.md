---
id: 04-topology/kneser-poulsen-conjecture
title: "Kneser-Poulsen Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kneser-Poulsen Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/kneser-poulsen-conjecture` · **Status:** solved-recently (settled in the plane, 2002; open for $d \ge 3$)

## 1. Problem Statement / Conjecture

Let $p = (p_1,\dots,p_n)$ and $q = (q_1,\dots,q_n)$ be two configurations of $n$ points in Euclidean space $\mathbb{E}^d$. Call $q$ a **contraction** of $p$ if

$$\|q_i - q_j\| \le \|p_i - p_j\| \qquad \text{for all } 1 \le i < j \le n .$$

Fix radii $r_1,\dots,r_n > 0$ and write $B_i(p) = B^d(p_i, r_i)$ for the closed ball of radius $r_i$ centered at $p_i$.

**Conjecture (Kneser–Poulsen).** If $q$ is a contraction of $p$, then

$$\mathrm{vol}_d\Big(\bigcup_{i=1}^n B_i(q)\Big) \;\le\; \mathrm{vol}_d\Big(\bigcup_{i=1}^n B_i(p)\Big),$$

and dually (the **Kneser form**)

$$\mathrm{vol}_d\Big(\bigcap_{i=1}^n B_i(q)\Big) \;\ge\; \mathrm{vol}_d\Big(\bigcap_{i=1}^n B_i(p)\Big).$$

A complete proof must handle arbitrary $n$, arbitrary unequal radii, and arbitrary (not necessarily continuous or rigid-motion-realizable) contractions, in every dimension $d \ge 3$. A disproof requires an explicit finite configuration pair violating one of the two inequalities. The two statements are *not* known to be equivalent in general; they are equivalent in the plane, where both are theorems.

## 2. Mathematical Foundations

**Power diagram.** For a configuration $p$ and radii $r_i$, the *power distance* is $\pi_i(x) = \|x-p_i\|^2 - r_i^2$. The cell $P_i = \{x : \pi_i(x) \le \pi_j(x)\ \forall j\}$ is a convex polyhedron; the $P_i$ tile $\mathbb{E}^d$ (the Laguerre/power diagram). The *truncated cell* is $P_i \cap B_i$, and the **wall** between $i$ and $j$ is

$$W_{ij}(p) \;=\; P_i \cap P_j \cap \Big(\bigcup_k B_k(p)\Big),$$

a subset of the radical hyperplane $\{x : \pi_i(x) = \pi_j(x)\}$.

**Csikós's Schläfli-type formula (1998).** Let $t \mapsto p(t)$ be a smooth motion and $d_{ij}(t) = \|p_i(t)-p_j(t)\|$. Then

$$\frac{d}{dt}\,\mathrm{vol}_d\Big(\bigcup_i B_i(p(t))\Big) \;=\; \sum_{i<j} \mathrm{vol}_{d-1}\big(W_{ij}(p(t))\big)\,\frac{d\,d_{ij}}{dt},$$

with the analogous identity for intersections, where the wall is intersected with $\bigcap_k B_k$ and the sign is reversed. Since $\mathrm{vol}_{d-1}(W_{ij}) \ge 0$, monotonicity along any **continuous contracting motion** is immediate. This is the analytic engine of the whole subject.

**Leapfrog Lemma (Bezdek–Connelly).** If $q$ is a contraction of $p$ in $\mathbb{E}^d$, define in $\mathbb{E}^{2d}$

$$\gamma_i(t) = \big(\cos t\; p_i,\; \sin t\; q_i\big), \qquad t\in[0,\tfrac{\pi}{2}] .$$

Then $\|\gamma_i(t)-\gamma_j(t)\|^2 = \cos^2 t\,\|p_i-p_j\|^2 + \sin^2 t\,\|q_i-q_j\|^2$ is nonincreasing in $t$. So *every* contraction is realized by an analytic contracting motion, at the cost of doubling the dimension.

**Dimension-reduction principle.** Bezdek and Connelly proved that monotonicity of the union (resp. intersection) volume for all radii in $\mathbb{E}^{d+2}$ implies it in $\mathbb{E}^{d}$, via an integral-geometric identity expressing $\mathrm{vol}_d$ of a union of $d$-balls as a weighted integral of $\mathrm{vol}_{d+2}$ of the union of $(d+2)$-balls with the same centers, viewing $\mathbb{E}^d \subset \mathbb{E}^{d+2}$.

## 3. History & State of the Art (SOTA)

- **1954.** E. T. Poulsen poses the union form (unit disks/balls, shrinking centers) as a problem in *Mathematica Scandinavica*.
- **1955.** M. Kneser independently states the intersection form in *Archiv der Mathematik*, in connection with Minkowski surface measure. The joint attribution is standard; the intersection form is sometimes called the Kneser conjecture (not to be confused with Kneser's graph-colouring conjecture).
- **1968.** B. Bollobás proves the planar case for unit disks under a *continuous* contracting motion.
- **1985–1991.** R. Alexander studies the mean-curvature/perimeter analogues; Capoyleas and Pach prove that a contraction does not increase the perimeter of a union of congruent disks in the plane.
- **1987.** M. Gromov proves the intersection form for $n \le d+1$ balls in $\mathbb{E}^d$, using a "flower" decomposition argument.
- **1998–2001.** B. Csikós proves the derivative formula above, settling the continuous-motion case in **all** dimensions for both unions and intersections, and extends it to *flowers* (Boolean expressions in balls) and to space forms.
- **2002.** K. Bezdek and R. Connelly prove the full conjecture, both forms, in $\mathbb{E}^2$ — the central theorem of the field — by combining the Leapfrog Lemma (motion in $\mathbb{E}^4$), Csikós's formula in $\mathbb{E}^4$, and the $(d+2)\to d$ reduction.
- **2004–2018.** Extensions to spherical polytopes, large radii, uniform contractions, and central-set techniques. **No progress on the general case in $\mathbb{E}^3$.**

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $d = 2$, all $n$, all radii, both forms | **Theorem** | Bezdek–Connelly 2002 |
| All $d$, contractions along a continuous path | **Theorem** | Csikós 1998 |
| All $d$, $n \le d+1$, intersection form | **Theorem** | Gromov 1987 |
| All $d$, unions/intersections of *flowers* under continuous motion | **Theorem** | Csikós 2001 |
| $\mathbb{S}^d$: contractions of spherical *polytopes* / hemispheres | **Theorem** (special cases) | Bezdek–Connelly 2004 |
| All $d$, common radius $r$ larger than an explicit threshold $r_0(p,q)$; strict inequality | **Theorem** | Gorbovickis 2013 |
| All $d$, "uniform contractions" ($\|q_i-q_j\| \le \lambda \le \|p_i-p_j\|$) with $n \ge n_0(d)$ sufficiently large | **Theorem** | Bezdek–Naszódi 2018 |
| Configurations whose power-diagram combinatorics is preserved | Follows from Csikós formula | — |
| Perimeter ($\mathrm{vol}_1$ of boundary), $d=2$, congruent disks | **Theorem** | Capoyleas–Pach 1991 |

Additionally, the planar theorem transfers to $\mathbb{E}^4$-restricted configurations only through the reduction in the wrong direction; there is no dimension for $d\ge 3$ in which the unrestricted conjecture is known.

## 5. Principal Obstacles

- **Discreteness of the hypothesis.** The conjecture compares two *isolated* configurations. Every working tool (Csikós's formula, Schläfli-type identities, curvature integrals) is differential and needs a path. In $\mathbb{E}^d$ a contraction need not be joinable by a contracting path: the two configurations may lie in different connected components of the "contraction space", e.g. mirror images of a rigid simplex. This is the single structural obstruction.
- **The Leapfrog Lemma costs two dimensions at a time.** It manufactures a path, but only in $\mathbb{E}^{2d}$. The compensating reduction step goes down exactly two dimensions per application, so the argument closes only when $2d \le d+2$, i.e. $d \le 2$. For $d = 3$ one would need a path in $\mathbb{E}^6$ and a reduction $6 \to 3$, which no integral identity supplies.
- **Failure of the reduction to skip dimensions.** The identity relating $\mathrm{vol}_{d+2}$ to $\mathrm{vol}_d$ rests on the fact that the orthogonal complement of $\mathbb{E}^d$ in $\mathbb{E}^{d+2}$ is a plane, so that the fiber integral $\int (r^2-\rho^2)$-type weight is elementary. Iterating gives $d+2k \to d$, but the required source dimension $2d$ has the wrong parity/growth for $d \ge 3$.
- **Nonconvexity of the union.** Unions of balls are not convex, so Brunn–Minkowski, mixed-volume monotonicity, and Alexandrov–Fenchel inequalities do not apply. The intersection is convex, but the constraint (pairwise distances) is not a convex condition on configurations.
- **No monotone potential.** Attempts to find a function $F(p)$ that dominates the union volume and is monotone under every single-distance decrease have failed; decreasing one distance can force a global combinatorial rearrangement of the power diagram, and the wall areas $\mathrm{vol}_{d-1}(W_{ij})$ jump in their dependence on the combinatorics.

## 6. The Gap

Everything proven is either (a) two-dimensional, (b) path-dependent, or (c) asymptotic in $n$ or $r$. The general statement is discrete, arbitrary-dimensional, and finite. The precise missing step is one of:

1. **A one-dimension-down leapfrog:** embed a contraction of $\mathbb{E}^d$ into a contracting analytic motion in $\mathbb{E}^{d+2}$ rather than $\mathbb{E}^{2d}$. For $d = 3$ this means a motion in $\mathbb{E}^5$; existence is unknown even for $n = 5$ points.
2. **A skipping reduction:** an integral-geometric identity deducing the $\mathbb{E}^d$ inequality from $\mathbb{E}^{D}$ for $D > d+2$, in particular $6 \to 3$.
3. **A path-free proof:** a direct combinatorial or measure-theoretic argument (e.g. via the central set / medial axis, or a transportation/rearrangement inequality) that never differentiates.

Route 3 is where the least is known and the most is being attempted.

## 7. Current Research (as of June 2026)

- **Central-set and medial-axis methods.** Gorbovickis's central-set approach reformulates union volume via the medial axis of the complement, giving proofs for large radii and, in refined form, for configurations with few deep intersections. Extending the radius threshold downward to a dimension-free constant is an active target *(frontier — verify)*.
- **Uniform contractions and asymptotics.** Following Bezdek–Naszódi, several groups study contractions with a hard cap $\lambda$ on the new distances, where volume estimates become packing/covering-density estimates. Sharpening the threshold $n_0(d)$ to a polynomial in $d$ is open *(frontier — verify)*.
- **Non-Euclidean space forms.** Csikós–Horváth-style work on $\mathbb{S}^d$ and $\mathbb{H}^d$: in $\mathbb{S}^d$ the union form is known to fail for antipodal-type configurations without extra hypotheses, so identifying the exact curvature-dependent hypothesis is a live question. Calgary (Bezdek's discrete geometry group), Eötvös Loránd (Csikós), and Cornell (Connelly's rigidity school) remain the main centres.
- **Rigidity-theoretic reformulation.** Connelly's programme relates the connectivity of the contraction configuration space to tensegrity/stress arguments; a proof that the contraction space is connected in a suitable enlarged ambient space would immediately give route 1.
- **Discrete/measure analogues.** Versions for Gaussian and other log-concave measures, and for lattice point counts, are being explored as testbeds *(frontier — verify)*.

## 8. Future Work

- Attack $d = 3$, $n = 5$ or $n = 6$ with unequal radii by computer-assisted case analysis of power-diagram combinatorics — the smallest case not covered by Gromov's $n \le d+1$ bound.
- Prove or refute the "leapfrog in $\mathbb{E}^{d+2}$" statement; a counterexample would kill route 1 cleanly and focus effort on route 3.
- Develop a Schläfli-type formula valid for *piecewise* contractions with combinatorial jumps, controlling the wall areas across degenerate transitions.
- Settle the quermassintegral hierarchy: is the $k$-th intrinsic volume of a union of balls monotone under contraction for $1 \le k \le d-1$? The $k = d-1$ (surface area) case in $\mathbb{E}^3$ is open and may be more tractable than volume.
- Establish the hyperbolic $\mathbb{H}^2$ case unconditionally; the planar Euclidean proof does not transfer because the leapfrog construction uses the linear structure of $\mathbb{E}^{2d}$.

## 9. Key References

- **[Foundational]** E. T. Poulsen. *Problem 10.* Mathematica Scandinavica, vol. 2, 1954, p. 346.
- **[Foundational]** M. Kneser. *Einige Bemerkungen über das Minkowskische Flächenmaß.* Archiv der Mathematik, vol. 6, 1955, pp. 382–390. [DOI](https://doi.org/10.1007/bf01900510)
- **[Foundational]** B. Bollobás. *Area of the union of disks.* Elemente der Mathematik, vol. 23, 1968, pp. 60–61.
- **[Foundational]** M. Gromov. *Monotonicity of the volume of intersection of balls.* In: Geometrical Aspects of Functional Analysis, Lecture Notes in Mathematics 1267, Springer, 1987, pp. 1–4. [DOI](https://doi.org/10.1007/bfb0078131)
- **[Foundational]** V. Capoyleas, J. Pach. *On the perimeter of a point set in the plane.* In: Discrete and Computational Geometry (DIMACS Series in Discrete Mathematics and Theoretical Computer Science, vol. 6), AMS, 1991, pp. 67–76. [DOI](https://doi.org/10.1090/dimacs/006/04)
- **[Key technique]** B. Csikós. *On the volume of the union of balls.* Discrete & Computational Geometry, vol. 20, 1998, pp. 449–461. [DOI](https://doi.org/10.1007/pl00009395)
- **[Key technique]** B. Csikós. *On the volume of flowers in space forms.* Geometriae Dedicata, vol. 86, 2001, pp. 59–79. [DOI](https://doi.org/10.1023/a:1011983123985)
- **[SOTA]** K. Bezdek, R. Connelly. *Pushing disks apart — the Kneser–Poulsen conjecture in the plane.* Journal für die reine und angewandte Mathematik (Crelle), vol. 553, 2002, pp. 221–236. [DOI](https://doi.org/10.1515/crll.2002.101)
- **[SOTA]** K. Bezdek, R. Connelly. *The Kneser–Poulsen conjecture for spherical polytopes.* Discrete & Computational Geometry, vol. 32, 2004, pp. 101–106. [DOI](https://doi.org/10.1007/s00454-004-0831-1)
- **[SOTA]** B. Csikós. *A Schläfli-type formula for polytopes with curved faces and its application to the Kneser–Poulsen conjecture.* Monatshefte für Mathematik, vol. 147, 2006, pp. 255–274. [DOI](https://doi.org/10.1007/s00605-005-0363-7)
- **[SOTA / Recent]** I. Gorbovickis. *Strict Kneser–Poulsen conjecture for large radii.* Geometriae Dedicata, vol. 162, 2013, pp. 95–107. [DOI](https://doi.org/10.1007/s10711-012-9718-0)
- **[SOTA / Recent]** K. Bezdek, M. Naszódi. *The Kneser–Poulsen conjecture for special contractions.* Discrete & Computational Geometry, vol. 60, 2018, pp. 967–980. [DOI](https://doi.org/10.1007/s00454-018-9976-1)
- **[Survey]** K. Bezdek. *From the Kneser–Poulsen conjecture to ball-polyhedra.* European Journal of Combinatorics, vol. 29, 2008, pp. 1820–1830. [DOI](https://doi.org/10.1016/j.ejc.2008.01.011)
- **[Survey / Book]** K. Bezdek. *Classical Topics in Discrete Geometry.* CMS Books in Mathematics, Springer, 2010 (Part on the Kneser–Poulsen conjecture). [DOI](https://doi.org/10.1007/978-1-4419-0600-7)
- **[Survey / Book]** V. Klee, S. Wagon. *Old and New Unsolved Problems in Plane Geometry and Number Theory.* Mathematical Association of America, 1991. [DOI](https://doi.org/10.1090/dol/011)

## 10. Worked Example / Concrete Special Case

**Three unit disks with centers on an equilateral triangle of side $s$.** Take $n=3$, $d=2$, $r_i=1$, $p_i$ at the vertices of an equilateral triangle of side $s \in [\sqrt3, 2]$ (so that no triple overlap occurs, since three unit circles meet in a common point exactly at $s=\sqrt3$).

Pairwise lens area for two unit disks at distance $s$:

$$L(s) = 2\cos^{-1}\!\Big(\frac{s}{2}\Big) - \frac{s}{2}\sqrt{4-s^2}.$$

By inclusion–exclusion, the union area is $A(s) = 3\pi - 3L(s)$. Differentiate:

$$\frac{d}{ds}\Big[2\cos^{-1}(s/2)\Big] = \frac{-2}{\sqrt{4-s^2}}, \qquad \frac{d}{ds}\Big[\tfrac{s}{2}\sqrt{4-s^2}\Big] = \frac{2-s^2}{\sqrt{4-s^2}},$$

so

$$L'(s) = \frac{-2 - (2-s^2)}{\sqrt{4-s^2}} = \frac{s^2-4}{\sqrt{4-s^2}} = -\sqrt{4-s^2}, \qquad A'(s) = 3\sqrt{4-s^2} \;\ge\; 0 .$$

Contracting means decreasing $s$, and $A$ is nondecreasing in $s$; hence the union area drops. This is exactly Csikós's formula: the wall $W_{ij}$ between two unit disks at distance $s$ is the common chord of the two circles, of length $2\sqrt{1-s^2/4} = \sqrt{4-s^2}$, and summing over the three pairs gives $\sum_{i<j}\mathrm{vol}_1(W_{ij}) = 3\sqrt{4-s^2} = A'(s)$.

**A discrete contraction (no path needed).** Contract from $s=2$ to $s=1$. At $s=2$ the disks are pairwise tangent, so $A(2)=3\pi \approx 9.4248$ and the triple intersection is empty. At $s=1$:

$$L(1) = 2\cos^{-1}(1/2) - \tfrac{1}{2}\sqrt3 = \frac{2\pi}{3} - \frac{\sqrt3}{2} \approx 1.2284,$$

and the triple intersection is the Reuleaux triangle of width $1$, of area $\tfrac{1}{2}(\pi-\sqrt3) \approx 0.7048$. Hence

$$A(1) = 3\pi - 3(1.2284) + 0.7048 \approx 6.4444 \;<\; 9.4248 = A(2),$$

confirming the union form, while the intersection grew from $0$ to $0.7048$, confirming the Kneser form. In $\mathbb{E}^2$ this configuration path exists explicitly; the content of the general conjecture is that the same inequality must hold in $\mathbb{E}^3$ even for contractions — such as a reflected simplex — that admit no contracting path at all.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*