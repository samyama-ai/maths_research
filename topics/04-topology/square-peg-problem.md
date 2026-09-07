---
id: 04-topology/square-peg-problem
title: "Square Peg Problem"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Square Peg Problem (Toeplitz Conjecture)

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/square-peg-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Toeplitz, 1911).** Every continuous simple closed curve $\gamma \subset \mathbb{R}^2$ (a Jordan curve) contains four points that are the vertices of a square.

Precisely: for every injective continuous map $\gamma : S^1 \to \mathbb{R}^2$ there exist parameters $t_1, t_2, t_3, t_4 \in S^1$, cyclically ordered, such that the points $p_i = \gamma(t_i)$ satisfy
$$|p_1p_2| = |p_2p_3| = |p_3p_4| = |p_4p_1| \quad\text{and}\quad |p_1p_3| = |p_2p_4| \neq 0 .$$
The square is *inscribed* — its vertices lie on $\gamma$ — but it need not lie inside the bounded complementary region, and it need not be non-degenerate in any stronger sense than $p_1 \neq p_3$.

No regularity beyond continuity is assumed. This is the whole difficulty: for smooth, piecewise-analytic, convex, or locally monotone curves the statement is a theorem. A complete resolution requires either (i) a proof valid for arbitrary Jordan curves, including nowhere-differentiable ones of Hausdorff dimension $>1$, or (ii) a single counterexample curve admitting no inscribed square.

Two standard generalizations are tracked alongside it. **Rectangular peg problem:** for each $r > 0$, does every Jordan curve inscribe a rectangle of aspect ratio $r$? **Cyclic-quadrilateral problem:** does every Jordan curve inscribe a quadrilateral similar to a given cyclic quadrilateral $Q$?

## 2. Mathematical Foundations

Let $\gamma: S^1 \hookrightarrow \mathbb{R}^2$ be a Jordan curve with image $\Gamma$. Work in the configuration space of unordered pairs
$$M = \big( \Gamma \times \Gamma \setminus \Delta \big) / (p,q)\sim(q,p),$$
which is an open Möbius band; its natural compactification $\overline{M}$ has boundary the diagonal $\Delta \cong S^1$.

**Vaughan's map.** Define
$$\Phi(\{p,q\}) = \Big( \tfrac{p+q}{2},\; |p-q| \Big) \in \mathbb{R}^2 \times \mathbb{R}_{\geq 0} \cong \mathbb{R}^3_+ .$$
$\Phi$ is continuous, maps $\partial\overline{M}$ homeomorphically onto $\Gamma \subset \mathbb{R}^2 \times \{0\}$, and is transverse to that plane. A rectangle inscribed in $\Gamma$ is exactly a pair of *distinct* pairs $\{p_1,p_3\} \neq \{p_2,p_4\}$ with $\Phi(\{p_1,p_3\}) = \Phi(\{p_2,p_4\})$: equal midpoints and equal diagonal lengths force a rectangle with those diagonals. So "$\Gamma$ inscribes no rectangle" $\Leftrightarrow$ "$\Phi$ is injective", i.e. the Möbius band embeds in the closed half-space with boundary circle in the boundary plane — impossible, since capping with the disc bounded by $\Gamma$ would embed $\mathbb{RP}^2$ in $S^3$.

**Aspect ratio and the symplectic reformulation.** For $\theta \in (0,\pi/2)$, an inscribed rectangle of aspect ratio $\cot\theta$ corresponds to a coincidence for the twisted map
$$\Phi_\theta(\{p,q\}) = \Big( \tfrac{p+q}{2},\; e^{i\theta}\,\tfrac{p-q}{2} \Big) .$$
Identify $\mathbb{R}^4 \cong \mathbb{C}^2$ with the standard symplectic form $\omega = \tfrac{i}{2}(dz_1\wedge d\bar z_1 + dz_2 \wedge d\bar z_2)$. Greene and Lobb observe that for smooth $\gamma$ the map
$$\iota(s,t) = \frac{1}{\sqrt 2}\Big( \gamma(s) + \gamma(t),\; i\big(\gamma(s)-\gamma(t)\big) \Big)$$
descends to a **Lagrangian** embedding of the open Möbius band, i.e. $\iota^*\omega = 0$. Rotating one factor by $e^{i\theta}$ gives a second Lagrangian $\iota_\theta$. If $\Gamma$ inscribed no rectangle of ratio $\cot\theta$, the two Lagrangian Möbius bands would be disjoint, and a surgery along their common cylindrical end produces an embedded **Lagrangian Klein bottle** in $\mathbb{R}^4$. This contradicts:

**Theorem (Shevchishin 2009; Nemirovski 2009).** There is no Lagrangian embedding of the Klein bottle into $\mathbb{R}^4$ (more generally into any uniruled symplectic 4-manifold).

**Degeneration obstruction.** For merely continuous $\gamma$, standard smoothing gives squares $Q_n$ inscribed in approximants $\gamma_n \to \gamma$ uniformly. Compactness yields a limit "square" $Q$ inscribed in $\gamma$ with side length $\ell \geq 0$. The conjecture is equivalent to ruling out $\ell = 0$ in every approximating sequence.

## 3. History & State of the Art (SOTA)

- **1911** — Otto Toeplitz poses the problem in a talk to the Swiss Mathematical Society.
- **1913** — Arnold Emch proves it for convex curves, and for piecewise-analytic curves, via a continuity/parity argument on inscribed rhombi.
- **1929/1944** — L. Šnirel'man proves it for curves of class $C^2$ (published 1944; the argument was later corrected and sharpened by Guggenheimer, 1965, to $C^2$-smooth curves).
- **1961** — R. P. Jerrard: analytic curves, by a degree argument counting inscribed squares with multiplicity.
- **1989** — Walter Stromquist: **locally monotone** curves (each point has a neighbourhood that is a graph over some line), the widest classical regularity class; also curves that are "small-perturbation" limits.
- **circa 1977** — H. Vaughan: *every* Jordan curve inscribes a **rectangle** (Möbius-band argument, §2).
- **2014** — Benjamin Matschke's *Notices of the AMS* survey consolidates the field and records results for special quadrilaterals and for curves without arbitrarily small "flat" degenerations.
- **2017** — Terence Tao: an integral-geometric identity proving the square peg problem for curves formed by two Lipschitz graphs of constant $<1$, with an explicit "square-counting" integral rather than a degree argument.
- **2018–2020** — Cole Hugelmeyer introduces knot theory into the problem: smooth Jordan curves inscribe rectangles of aspect ratio $\sqrt 3$, and then at least one-third of all aspect ratios, by studying the torus knot type of the trace of $\Phi_\theta$ in $\mathbb{R}^3 \times S^1$.
- **2021** — **Joshua Greene and Andrew Lobb** prove the **smooth rectangular peg problem**: every smooth Jordan curve inscribes rectangles of *every* aspect ratio (*Inventiones* 226). This subsumes the smooth square peg problem.
- **2023** — Greene–Lobb: every smooth Jordan curve inscribes a quadrilateral similar to any given **cyclic quadrilateral** (*Inventiones* 234).
- **Present.** The general continuous case is open, for squares and for rectangles of aspect ratio $\neq$ those given by Vaughan's argument.

## 4. Partial Results / Verified Cases

| Class of curve | Result | Source |
|---|---|---|
| Convex curves | inscribed square exists | Emch 1913 |
| Piecewise-analytic / analytic | square exists | Emch 1913; Jerrard 1961 |
| $C^2$ and smooth | square exists | Šnirel'man 1944; Guggenheimer 1965 |
| Locally monotone (bounded turning at each point) | square exists | Stromquist 1989 |
| Union of two Lipschitz graphs, constant $<1$ | square exists | Tao 2017 |
| **All** Jordan curves | **rectangle** (some aspect ratio) exists | Vaughan (Möbius band) |
| Smooth curves | rectangle of **every** aspect ratio $r \in (0,\infty)$ | Greene–Lobb 2021 |
| Smooth curves | **every** cyclic quadrilateral, up to similarity | Greene–Lobb 2023 |
| Smooth convex curves | every cyclic quadrilateral | Akopyan–Avvakumov 2018 |
| Smooth curves | aspect ratio $\sqrt3$; then $\geq 1/3$ of all ratios | Hugelmeyer 2018, 2019 |
| Jordan loops, non-smooth | trichotomy: the set of inscribed aspect ratios is all of $(0,\infty)$, or a specific restricted form | Schwartz 2020 |

Curves admitting squares form a dense $G_\delta$-type set in the uniform topology, so any counterexample must be a limit of square-inscribing curves in which the inscribed squares shrink to a point.

## 5. Principal Obstacles

- **No degree theory without regularity.** Every classical proof counts inscribed squares modulo 2 or computes an intersection number of a map $\overline{M} \to \mathbb{R}^k$. Transversality — and hence a well-defined count — requires derivatives. A continuous curve gives no transversality, and the intersection set may be a Cantor set rather than a finite set.
- **Degeneration to a point.** The compactness argument of §2 loses exactly at $\ell = 0$. Since a fractal curve can carry inscribed squares of side $\varepsilon$ at every scale, the naive limit is uninformative; one needs a *quantitative* lower bound $\ell \geq c(\gamma) > 0$ depending only on continuous data, and no such bound is known.
- **The symplectic method is intrinsically smooth.** The Greene–Lobb Lagrangian $\iota$ requires $\gamma \in C^1$ to be immersed and $C^\infty$ (or at least $C^1$ with control) for the Lagrangian neighbourhood theorem and the Klein-bottle surgery. Lagrangian submanifolds are not defined for merely continuous input; $C^0$-symplectic geometry does not yet supply a Klein-bottle obstruction.
- **Failure of approximation.** Smoothing $\gamma$ changes small-scale geometry, precisely the scale where the square might live. There is no known "square-stability" estimate under $C^0$ perturbation.
- **Squares are rigid.** Vaughan's argument works for rectangles because the constraint (equal midpoints, equal diagonals) is codimension 3 in a 4-dimensional problem and matches an embedding obstruction. Fixing the aspect ratio adds one more equation and destroys the purely topological argument; that extra equation is what the symplectic machinery buys.

## 6. The Gap

Proven: smooth (in fact $C^1$-controlled) Jordan curves inscribe every rectangle and every cyclic quadrilateral. Also proven: all Jordan curves inscribe *some* rectangle. Conjectured: all Jordan curves inscribe a square.

The gap is a single implication:
$$\text{smooth square peg} \;+\; C^0\text{-approximation} \;\Longrightarrow\; \text{continuous square peg},$$
which fails only because the inscribed squares of the approximants may degenerate. Formally, one must show: for every Jordan curve $\gamma$ there exists $\varepsilon(\gamma) > 0$ such that every smooth curve $\gamma'$ with $\|\gamma - \gamma'\|_\infty < \varepsilon$ inscribes a square of side $\geq \varepsilon$. Equivalently, produce a $C^0$-continuous, non-vanishing invariant (a "square count" or a $C^0$-symplectic Klein-bottle obstruction) replacing the smooth intersection number.

## 7. Current Research (as of June 2026)

- **Symplectic/gauge-theoretic school (Greene, Brown; Lobb, Durham).** Extending the Lagrangian-Klein-bottle argument to rougher curves: rectifiable curves, curves with finitely many corners, and quasiconformal images of circles. *(frontier — verify)* Partial extensions to piecewise-$C^1$ curves are in circulation.
- **Low-dimensional-topology school (Feller, Golla).** Non-orientable slice-genus bounds on the surfaces built from $\Phi_\theta$ give aspect-ratio ranges for classes of non-smooth curves, independent of symplectic input.
- **Knot-theoretic counting (Hugelmeyer).** Torus-link invariants of the trace curve give explicit measure bounds on the inscribed aspect-ratio set; the target is to push measure-theoretic bounds to curves of finite total curvature.
- **Metric/analytic school (Schwartz, Brown).** Direct study of the "rectangle set" of arbitrary Jordan loops; the 2020 trichotomy is the main structural tool, and current work targets loops of bounded turning and of Hausdorff dimension close to 1.
- **Higher-dimensional analogues.** Inscribing regular simplices, cross-polytopes and cubes in $S^{n-1}$-embedded spheres (Makeev, Karasev, Hausel–Makai–Szűcs lineage) remains largely open above dimension 3.

## 8. Future Work

1. **Quantitative square-existence.** Prove a bound of the form: any smooth curve of diameter $1$ contained in an annulus of modulus $m$ inscribes a square of side $\geq c(m)$. This would immediately close the continuous case by compactness.
2. **$C^0$-symplectic obstruction.** Develop a Klein-bottle non-embedding theorem for Lagrangian-type objects defined only up to $C^0$-limits (Humilière–Leclercq–Seyfaddini-style $C^0$ rigidity), then apply it to $\iota_\theta$ for non-smooth $\gamma$.
3. **Rectangles of prescribed ratio for all Jordan curves.** Even the ratio-$r$ rectangle problem is open in full generality; Vaughan's argument gives no control on $r$. A ratio-independent topological proof would be a decisive intermediate step.
4. **Search for a counterexample.** Construct a self-similar curve whose square-inscribing configurations all degenerate; numerical scans of Koch-type and Julia-set curves have so far always found squares.
5. **Peg problems in Riemannian surfaces** and for non-cyclic quadrilaterals, where Greene–Lobb's cyclic-quadrilateral theorem is known to be sharp.

## 9. Key References

- **[Foundational]** A. Emch. *Some properties of closed convex curves in a plane.* American Journal of Mathematics 35 (1913), 407–412.
- **[Foundational]** L. G. Šnirel'man. *On certain geometrical properties of closed curves.* Uspekhi Matematicheskikh Nauk 10 (1944), 34–44.
- **[Foundational]** R. P. Jerrard. *Inscribed squares in plane curves.* Transactions of the American Mathematical Society 98 (1961), 234–241.
- **[Foundational]** W. Stromquist. *Inscribed squares and square-like quadrilaterals in closed curves.* Mathematika 36 (1989), 187–197.
- **[SOTA]** J. E. Greene and A. Lobb. *The rectangular peg problem.* Inventiones Mathematicae 226 (2021), 1005–1027.
- **[SOTA]** J. E. Greene and A. Lobb. *Cyclic quadrilaterals and smooth Jordan curves.* Inventiones Mathematicae 234 (2023), 931–935.
- **[SOTA]** T. Tao. *An integration approach to the Toeplitz square peg problem.* Forum of Mathematics, Sigma 5 (2017), e30.
- **[SOTA]** C. Hugelmeyer. *Every smooth Jordan curve has an inscribed rectangle with aspect ratio equal to $\sqrt3$.* arXiv:1803.07417 (2018); and *Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios*, arXiv:1911.07336 (2019).
- **[Related]** A. Akopyan and S. Avvakumov. *Any cyclic quadrilateral can be inscribed in any closed convex smooth curve.* Forum of Mathematics, Sigma 6 (2018), e7.
- **[Related]** R. E. Schwartz. *A trichotomy for rectangles inscribed in Jordan loops.* Geometriae Dedicata 208 (2020), 177–196.
- **[Related]** V. Shevchishin. *Lagrangian embeddings of the Klein bottle and combinatorial properties of mapping class groups.* Izvestiya: Mathematics 73 (2009), 797–859. S. Nemirovski. *Lagrangian Klein bottles in $\mathbb{R}^{2n}$.* Geometric and Functional Analysis 19 (2009), 902–909.
- **[Survey]** B. Matschke. *A survey on the square peg problem.* Notices of the American Mathematical Society 61 (2014), no. 4, 346–352.
- **[Survey]** R. E. Schwartz. *Rectangles, curves, and Klein bottles.* Bulletin of the American Mathematical Society 59 (2022), 1–17.

## 10. Worked Example / Concrete Special Case

**The ellipse: all aspect ratios explicitly.** Let
$$\Gamma = \Big\{ (a\cos t,\; b\sin t) : t \in [0,2\pi) \Big\},\qquad a \geq b > 0 .$$
For $\theta \in (0,\pi/2)$ take the four points $t = \pm\theta,\ \pi \pm \theta$:
$$P_{1,2} = (\pm a\cos\theta,\; b\sin\theta), \qquad P_{3,4} = (\pm a\cos\theta,\; -b\sin\theta).$$
By the $(x,y) \mapsto (-x,y)$ and $(x,y)\mapsto(x,-y)$ symmetries these four points form an axis-parallel rectangle with side lengths
$$w(\theta) = 2a\cos\theta, \qquad h(\theta) = 2b\sin\theta, \qquad r(\theta) = \frac{w}{h} = \frac{a}{b}\cot\theta .$$
As $\theta$ runs over $(0,\pi/2)$, $r(\theta)$ is continuous and strictly decreasing from $+\infty$ to $0$, so **every** aspect ratio is attained exactly once — the ellipse verifies the rectangular peg problem by direct computation.

Setting $r(\theta) = 1$ gives $\tan\theta_0 = a/b$, hence
$$\cos\theta_0 = \frac{b}{\sqrt{a^2+b^2}}, \qquad \sin\theta_0 = \frac{a}{\sqrt{a^2+b^2}},$$
and the inscribed square has vertices $(\pm s, \pm s)$ with
$$s = a\cos\theta_0 = b\sin\theta_0 = \frac{ab}{\sqrt{a^2+b^2}} .$$
Check: $s^2/a^2 + s^2/b^2 = \frac{a^2b^2}{a^2+b^2}\cdot\frac{a^2+b^2}{a^2b^2} = 1$, so the points lie on $\Gamma$. Side length $2s = 2ab/\sqrt{a^2+b^2}$. For the circle $a=b=1$ this returns $s = 1/\sqrt2$, the unit square.

**Where the general problem breaks.** The above uses the ellipse's two reflection symmetries; a generic curve has none, and the existence proof must instead run the parity/degree argument on the Möbius band $\overline{M}$ of §2. Replace $\Gamma$ by a curve built as the graph of a nowhere-differentiable function over most of its length: the map $\Phi_\theta$ is still continuous, but its self-coincidence set is no longer cut out transversally, the smooth intersection count is undefined, and inscribed squares found in smooth approximants may have side $\to 0$. That single failure mode — not any known geometric obstruction — is all that separates the ellipse computation above from the general theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*