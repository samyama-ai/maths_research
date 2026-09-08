---
id: 03-geometry/bernstein-problem-higher-codimension
title: "Bernstein Problem for Minimal Graphs in Higher Codimension"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bernstein Problem for Minimal Graphs in Higher Codimension

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bernstein-problem-higher-codimension` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $f:\mathbb{R}^n \to \mathbb{R}^m$ be a smooth map whose graph
$$\Gamma_f = \{(x, f(x)) : x \in \mathbb{R}^n\} \subset \mathbb{R}^{n+m}$$
is a minimal submanifold (zero mean curvature). **Question (higher-codimension Bernstein problem):** for which pairs $(n,m)$ must $f$ be affine?

For $m=1$ the answer is known completely: yes for $n \le 7$, no for $n \ge 8$. For $m \ge 2$ the answer is known to be **no** in general — Lawson–Osserman (1977) produced entire Lipschitz, non-affine solutions for $n \ge 4$, $m \ge 3$ — so the live problem is threefold:

1. **Dimension gap.** Is every entire smooth minimal graph over $\mathbb{R}^3$ affine, for every $m$? (Open.)
2. **Codimension 2.** Is every entire minimal graph with $m = 2$ affine, for every $n$? (Open; no counterexample known.)
3. **Sharp slope threshold.** Find the optimal constant $\beta^\ast$ such that $\Delta_f := \sqrt{\det(I + df^{T}df)} \le \beta^\ast$ on $\mathbb{R}^n$ forces $f$ affine.

A complete resolution means: for each $(n,m)$, either a proof of affineness or an explicit non-affine entire solution; and for (3), a proof at the sharp constant together with a matching example.

## 2. Mathematical Foundations

$\Gamma_f$ is minimal iff $f$ solves the **minimal surface system** (Lawson–Osserman): with induced metric
$$g_{ij} = \delta_{ij} + \sum_{\alpha=1}^{m} \partial_i f^\alpha\, \partial_j f^\alpha, \qquad g = \det(g_{ij}),$$
$$\sum_{i,j=1}^{n} \partial_i\!\left( \sqrt{g}\, g^{ij} \right) = 0 \quad (i\text{-th eqn}), \qquad \sum_{i,j=1}^{n} \partial_i\!\left( \sqrt{g}\, g^{ij}\partial_j f^\alpha \right) = 0,\ \ \alpha = 1,\dots,m .$$
For $m=1$ the first $n$ equations are consequences of the last one and the system reduces to the scalar quasilinear elliptic equation
$$\operatorname{div}\!\left( \frac{\nabla f}{\sqrt{1+|\nabla f|^2}} \right) = 0 .$$
For $m \ge 2$ the system is **not** a determined elliptic system in the classical sense: the coefficient matrix depends on $df$ and the coordinate equations couple, destroying the maximum principle, the divergence-structure a priori gradient bound, and De Giorgi–Nash–Moser regularity.

**Slope.** With singular values $\lambda_1,\dots,\lambda_n \ge 0$ of $df$,
$$\Delta_f = \sqrt{g} = \prod_{i=1}^{n}\sqrt{1+\lambda_i^{2}} .$$
$\Delta_f \equiv 1$ iff $df \equiv 0$; "bounded slope" means $\Delta_f \le \beta_0 < \infty$.

**Gauss map.** $\gamma: \Gamma_f \to \mathbf{G}_{n,m} = SO(n+m)/SO(n)\times SO(m)$, $p \mapsto T_p\Gamma_f$. Minimality $\iff$ $\gamma$ is a harmonic map (Ruh–Vilms). For $m=1$, $\mathbf{G}_{n,1}=S^n$ and the image lies in a hemisphere; for $m\ge2$, $\mathbf{G}_{n,m}$ has nonnegative but **not** constant sectional curvature and contains totally geodesic flats, so convexity of the target is far weaker. Bernstein-type theorems then reduce to Liouville theorems for harmonic maps into geodesically convex subsets $\mathcal{U} \subset \mathbf{G}_{n,m}$, where $\mathcal{U}$ is cut out by a slope bound: $\{\Delta \le \beta_0\}$ is convex when $\beta_0 < 3$ (Jost–Xin–Yang).

**Blow-down.** Under a slope bound, the tangent cone at infinity $C = \lim_{r\to0} r\,\Gamma_f$ is an area-minimizing (in the codimension-1 case) or stationary minimal cone; Bernstein is equivalent to $C$ being a plane, i.e. to rigidity of the link $C \cap S^{n+m-1}$ as a minimal submanifold of the sphere.

## 3. History & State of the Art (SOTA)

- **1915–17.** Bernstein: an entire solution over $\mathbb{R}^2$, $m=1$, is affine.
- **1962–68.** Fleming ($n=3$), De Giorgi ($n=4$), Almgren ($n=5$), Simons ($n\le7$) settle $m=1$ up to dimension 7 via the nonexistence of stable minimal cones.
- **1969.** Bombieri–De Giorgi–Giusti: for $n \ge 8$, non-affine entire minimal graphs exist over the Simons cone $\{|x'|=|x''|\}\subset\mathbb{R}^8$. Codimension 1 closed.
- **1967–69.** Chern–Osserman: complete minimal surfaces in $\mathbb{R}^{2+m}$ with finite total curvature; entire minimal graphs over $\mathbb{R}^2$ are planes in every codimension.
- **1977.** Lawson–Osserman, *Acta Math.*: for $n\ge4$, $m\ge3$ the minimal surface system admits entire Lipschitz non-smooth solutions (Hopf cones), the Dirichlet problem is non-unique (three solutions for the same boundary data), and existence fails for large boundary data. This is the structural break from $m=1$.
- **1980.** Hildebrandt–Jost–Widman: Bernstein under a slope bound, via harmonic maps into a geodesic ball of radius $<\tfrac{\sqrt2}{4}\pi$ in $\mathbf{G}_{n,m}$.
- **1999–2013.** Jost–Xin, then Jost–Xin–Yang: successively enlarged the convex region; current best clean statement is $\Delta_f \le \beta_0 < 3$ (arbitrary $n,m$).
- **2002–03.** Mu-Tao Wang: mean curvature flow proof under an **area-decreasing** condition $\lambda_i\lambda_j < 1$ for all $i \ne j$; long-time existence and convergence of the graphical flow in arbitrary codimension.
- **2019–.** Assimos–Jost: refined maximum-principle geometry on $\mathbf{G}_{n,2}$, giving codimension-2 Bernstein theorems under weaker Gauss-image restrictions.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $n=1$, any $m$ | True (geodesics). |
| $n=2$, any $m$ | **True** (Chern–Osserman / Osserman). |
| $m=1$, $n\le7$ | **True** (Fleming–De Giorgi–Almgren–Simons). |
| $m=1$, $n\ge8$ | **False** (Bombieri–De Giorgi–Giusti). |
| $n\ge4$, $m\ge3$ | **False** for Lipschitz solutions (Lawson–Osserman). |
| $n=3$, any $m$ | **Open** in general. |
| $m=2$, $n\ge3$ | **Open**; no counterexample known. |

Conditional theorems, valid for all $n,m$:

- **Slope bound.** $\Delta_f \le \beta_0 < 3 \Rightarrow f$ affine (Jost–Xin–Yang, *JDG* 2012 / *Calc. Var. PDE* 2013). Earlier thresholds: Hildebrandt–Jost–Widman 1980, Jost–Xin 1999.
- **Area-decreasing.** $\lambda_i \lambda_j < 1$ for $i\ne j$ $\Rightarrow$ $f$ affine (M.-T. Wang, *Trans. AMS* 2003), proved by graphical mean curvature flow.
- **Bounded slope, low $n$.** For $n=3$ and $n=4$ with $\Delta_f$ bounded, affineness follows from rigidity of minimal cones with small-dimensional link (Barbosa 1979 for minimal $S^2$'s; Fischer-Colbrie 1980, *Acta Math.*).
- **Growth conditions.** $m=1$: $f(x) = o(|x|)$ growth control gives Bernstein in all dimensions (Ecker–Huisken, *JDG* 1990); Moser's theorem ($|\nabla f|$ bounded) is the classical case.
- **Codimension 2.** Assimos–Jost (2019+): Bernstein holds if the Gauss image avoids a suitable set of $\mathbf{G}_{n,2}$ strictly larger than the previously used convex balls.

## 5. Principal Obstacles

- **Loss of ellipticity structure.** For $m \ge 2$ the minimal surface system is a coupled system; there is no scalar maximum principle, no Harnack inequality for $|df|$, and no De Giorgi–Nash–Moser theory. Lawson–Osserman show this is not a defect of proof technique: solutions genuinely fail to be $C^1$.
- **No calibration/minimizing hypothesis.** In codimension 1 a graph is automatically area-*minimizing*, which powers the Simons stability inequality and Federer dimension reduction. In higher codimension a minimal graph is stationary but need not minimize, and it need not be calibrated; the entire stability machinery is unavailable.
- **Grassmannian geometry.** $\mathbf{G}_{n,m}$ for $m\ge2$ has flat totally geodesic subspaces and cut locus structure that limits convex geodesic balls; the largest known convex slope region ($\Delta<3$) is far from the whole space of admissible tangent planes.
- **Rigidity of spherical links fails.** Blow-down reduces Bernstein to: is every minimal cone in $\mathbb{R}^{n+m}$ arising as a graph a plane? For $n\ge4$, $m\ge3$ the Hopf link (a minimally immersed $S^3$ in $S^6$) is a genuine counterexample, so no purely dimensional rigidity theorem can hold.
- **Bernstein's conformal/holomorphic tools are 2-dimensional.** The $n=2$ proof uses holomorphicity of the Gauss map into a quadric; there is no complex structure for $n\ge3$.

## 6. The Gap

Two quantitative gaps and one dimensional gap:

1. **Slope gap.** Proved: $\Delta_f < 3$. The Lawson–Osserman counterexample has singular values $(\sqrt5/2,\ \sqrt5,\ \sqrt5,\ 0)$, hence
$$\Delta_f = \sqrt{1+\tfrac54}\cdot\sqrt{1+5}\cdot\sqrt{1+5}\cdot 1 = \tfrac32\cdot 6 = 9 .$$
Everything in $3 \le \beta_0 < 9$ is unknown. The sharp threshold $\beta^\ast \in [3,9]$ is undetermined even for $n=4$, $m=3$.
2. **Codimension gap.** Counterexamples need $m\ge3$ (they come from Hopf maps $S^3\to S^2$, $S^7\to S^4$, $S^{15}\to S^8$, i.e. $(n,m)=(4,3),(8,5),(16,9)$). Codimension 2 has neither a proof nor an example: one must either construct a non-affine minimal graph $\mathbb{R}^n\to\mathbb{R}^2$ or extend the Assimos–Jost convexity to all of $\mathbf{G}_{n,2}$.
3. **Dimension gap.** $n=3$: the link of a blow-down cone is a minimal surface in $S^{2+m}$; classifying which such surfaces can be graphical links, without a slope bound, is the missing step.

Additionally, all counterexamples are only Lipschitz. Whether a **smooth** entire non-affine minimal graph exists for any $m \ge 2$ is open — a positive answer would need a genuinely new construction, since cones are the only known source.

## 7. Current Research (as of June 2026)

- **MPI Leipzig (J. Jost, R. Assimos and collaborators).** Geometry of maximum principles on Grassmannians; the goal is a sharp description of the largest subset of $\mathbf{G}_{n,m}$ supporting a Liouville theorem, with codimension 2 as the target case.
- **Fudan University (Y. L. Xin, L. Yang, Q. Ding).** Slope-threshold improvements, curvature estimates for minimal submanifolds of higher codimension, and structure of Lawson–Osserman-type cones and their smoothing by minimal graphs. *(frontier — verify)* Work extending Lawson–Osserman cones to broader classes of $(n,m)$ and analysing which cones bound entire graphs.
- **Mean curvature flow school (M.-T. Wang, Columbia; K. Smoczyk, Hannover; M.-P. Tsui).** Preservation of area-decreasing and related two-convexity conditions along graphical MCF; curvature decay estimates yielding Bernstein statements under conditions weaker than $\lambda_i\lambda_j<1$.
- **Special holonomy / calibrated geometry.** Special Lagrangian graphs ($m=n$) form a tractable sub-case: entire special Lagrangian graphs with convex potential are governed by the Hessian equation $\sum \arctan\lambda_i = c$, where Yuan's Bernstein theorem applies. Transferring these convexity mechanisms to general codimension is an active line. *(frontier — verify)*

## 8. Future Work

- Determine the sharp slope constant $\beta^\ast$ for $(n,m)=(4,3)$; even proving $\beta^\ast > 3$ by extending the convex region would be a first quantitative advance since 2013.
- Settle codimension 2: either a Gauss-image Liouville theorem covering all of $\mathbf{G}_{n,2}$, or a new cone construction from a non-Hopf harmonic map to a 1-sphere-bundle target.
- Prove or disprove a **smooth** Bernstein theorem: is every *smooth* entire minimal graph with $m\ge2$ and $n \le 7$ affine?
- Develop dimension reduction without minimality: a Federer-type argument for stationary graphical cones, using the graph condition itself as a substitute for stability.
- Classify minimal 3-dimensional cones in $\mathbb{R}^{3+m}$ that are graphs, closing the $n=3$ case.

## 9. Key References

- **[Foundational]** S. Bernstein. *Sur un théorème de géométrie et ses applications aux équations aux dérivées partielles du type elliptique.* Comm. Soc. Math. Kharkov, 15 (1915–17), 38–45.
- **[Foundational]** E. De Giorgi. *Una estensione del teorema di Bernstein.* Ann. Scuola Norm. Sup. Pisa, 19 (1965), 79–85.
- **[Foundational]** J. Simons. *Minimal varieties in Riemannian manifolds.* Annals of Mathematics, 88 (1968), 62–105.
- **[Foundational]** E. Bombieri, E. De Giorgi, E. Giusti. *Minimal cones and the Bernstein problem.* Inventiones Mathematicae, 7 (1969), 243–268.
- **[Foundational]** H. B. Lawson, R. Osserman. *Non-existence, non-uniqueness and irregularity of solutions to the minimal surface system.* Acta Mathematica, 139 (1977), 1–17.
- **[Foundational]** S. S. Chern, R. Osserman. *Complete minimal surfaces in Euclidean $n$-space.* Journal d'Analyse Mathématique, 19 (1967), 15–34.
- **[Foundational]** S. Hildebrandt, J. Jost, K.-O. Widman. *Harmonic mappings and minimal submanifolds.* Inventiones Mathematicae, 62 (1980), 269–298.
- **[SOTA]** J. Jost, Y. L. Xin. *Bernstein type theorems for higher codimension.* Calculus of Variations and PDE, 9 (1999), 277–296.
- **[SOTA]** M.-T. Wang. *On graphic Bernstein type results in higher codimension.* Transactions of the AMS, 355 (2003), 265–271.
- **[SOTA]** M.-T. Wang. *Long-time existence and convergence of graphic mean curvature flow in arbitrary codimension.* Inventiones Mathematicae, 148 (2002), 525–543.
- **[SOTA]** J. Jost, Y. L. Xin, L. Yang. *The regularity of harmonic maps into spheres and applications to Bernstein problems.* Journal of Differential Geometry, 90 (2012), 131–176.
- **[SOTA / Recent]** J. Jost, Y. L. Xin, L. Yang. *The Gauss image of entire graphs of higher codimension and Bernstein type theorems.* Calculus of Variations and PDE, 47 (2013), 711–737.
- **[Recent]** R. Assimos, J. Jost. *The geometry of maximum principles and a Bernstein theorem in codimension 2.* arXiv:1811.09869.
- **[Related]** D. Fischer-Colbrie. *Some rigidity theorems for minimal submanifolds of the sphere.* Acta Mathematica, 145 (1980), 29–46.
- **[Related]** K. Ecker, G. Huisken. *A Bernstein result for minimal graphs of controlled growth.* Journal of Differential Geometry, 31 (1990), 397–400.
- **[Survey]** Y. L. Xin. *Minimal Submanifolds and Related Topics.* World Scientific, 2003 (2nd ed. 2018).
- **[Survey]** R. Osserman. *A Survey of Minimal Surfaces.* Dover, 1986.

## 10. Worked Example / Concrete Special Case

**The Lawson–Osserman cone, $(n,m)=(4,3)$.** Let $\eta: S^3 \to S^2$ be the Hopf map, $\eta(z_1,z_2) = (|z_1|^2-|z_2|^2,\ 2z_1\bar z_2)$ under $\mathbb{R}^4 \cong \mathbb{C}^2$. Define
$$f(x) = c\,|x|\,\eta\!\left(\frac{x}{|x|}\right), \qquad f(0)=0,\quad c>0 .$$
$f$ is homogeneous of degree 1, smooth on $\mathbb{R}^4\setminus\{0\}$, Lipschitz, and *not* differentiable at $0$.

**Step 1 — reduce to a link.** $\Gamma_f$ is the cone over
$$M_t = \{(\cos t\,\omega,\ \sin t\,\eta(\omega)) : \omega \in S^3\} \subset S^6, \qquad \tan t = c .$$
$\Gamma_f$ is minimal $\iff$ $M_t$ is minimal in $S^6$.

**Step 2 — the volume function.** $\eta$ is a Riemannian submersion onto $S^2$ up to a factor 2: it kills the Hopf-fibre direction and doubles lengths on the horizontal 2-plane. So the induced metric on $M_t$ has eigenvalues $\cos^2 t$ (fibre) and $\cos^2t + 4\sin^2 t$ (twice, horizontal). Hence
$$\operatorname{Vol}(M_t) = C_0 \cos t\,(\cos^2t + 4\sin^2 t) = C_0 \cos t\,(1+3\sin^2 t).$$

**Step 3 — critical points.** $\{M_t\}$ is the orbit family of an isometric $Sp(1)$ action, so $M_t$ is minimal $\iff$ $V'(t)=0$ with $V(t)=\cos t + 3\cos t \sin^2 t$:
$$V'(t) = -\sin t + 3\sin t(2\cos^2 t - \sin^2 t) = \sin t\,(9\cos^2 t - 4).$$
Solutions: $\sin t = 0$ (the totally geodesic $S^3$, i.e. $f \equiv 0$, the plane), or
$$\cos t = \tfrac23,\quad \sin t = \tfrac{\sqrt5}{3}, \quad\Longrightarrow\quad c = \tan t = \frac{\sqrt5}{2}.$$

**Step 4 — conclusion.** For $c = \sqrt5/2$, $f$ is an entire Lipschitz solution of the minimal surface system on $\mathbb{R}^4$ that is not affine. Its singular values at $x=\omega \in S^3$ are $\lambda = (c,\,2c,\,2c,\,0) = (\tfrac{\sqrt5}{2},\sqrt5,\sqrt5,0)$, so
$$\Delta_f = \tfrac32 \cdot \sqrt6 \cdot \sqrt6 \cdot 1 = 9, \qquad \lambda_2\lambda_3 = 5 > 1 .$$
Both the Jost–Xin–Yang bound ($\Delta_f<3$) and Wang's area-decreasing condition ($\lambda_i\lambda_j<1$) fail, as they must. The same boundary data $\varphi = c\,\eta$ on $S^3$ admits at least three distinct solutions of the Dirichlet problem for $c$ in a suitable range, and no solution at all for $c$ large (Lawson–Osserman) — the sharpest concrete illustration of how the higher-codimension theory departs from the scalar case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*