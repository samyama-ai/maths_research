---
id: 03-geometry/cartan-hadamard-conjecture
title: "Cartan-Hadamard Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cartan-Hadamard Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/cartan-hadamard-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(M^n, g)$ be a **Cartan–Hadamard manifold**: complete, simply connected, with sectional curvature $K \le 0$ everywhere. The conjecture asserts that domains in $M$ satisfy the *Euclidean* isoperimetric inequality: for every bounded domain $\Omega \subset M$ with rectifiable boundary,

$$|\partial \Omega| \;\ge\; n\,\omega_n^{1/n}\,|\Omega|^{\frac{n-1}{n}},$$

where $\omega_n$ is the volume of the unit ball in $\mathbb{R}^n$, with equality only if $\Omega$ is isometric to a Euclidean ball.

The **generalized (Aubin) form** replaces the bound $K\le 0$ by $K \le \kappa$ for a constant $\kappa \le 0$, and compares against the simply connected space form $M_\kappa^n$: if $\Omega^\ast \subset M_\kappa^n$ is a metric ball with $|\Omega^\ast| = |\Omega|$, then $|\partial\Omega| \ge |\partial\Omega^\ast|$.

A complete solution means a proof valid in every dimension $n$, for every Cartan–Hadamard metric and every finite-perimeter set — or a single counterexample manifold and domain violating the bound. The conjecture is **open for all $n \ge 5$**.

## 2. Mathematical Foundations

**Cartan–Hadamard theorem.** If $M^n$ is complete with $K \le 0$ and simply connected, then for each $p \in M$ the exponential map $\exp_p : T_pM \to M$ is a diffeomorphism. So $M \cong \mathbb{R}^n$ and geodesics between points are unique — the manifold is "at least as spread out" as $\mathbb{R}^n$, which is the intuition behind the conjecture.

**Perimeter.** For a set $\Omega$ of finite perimeter, $|\partial\Omega| := \mathcal{H}^{n-1}(\partial^\ast\Omega)$ (reduced boundary). The **isoperimetric profile** is
$$I_M(v) \;=\; \inf\{\,|\partial\Omega| : \Omega \subset M,\ |\Omega| = v\,\},$$
and the conjecture is the pointwise comparison $I_M \ge I_{\mathbb{R}^n}$, i.e. $I_M(v) \ge n\omega_n^{1/n} v^{(n-1)/n}$, or $I_M \ge I_{M_\kappa^n}$ in the generalized form.

**Regularity of minimizers.** By De Giorgi–Federer–Almgren theory, an isoperimetric region (when it exists) has boundary that is a smooth constant-mean-curvature hypersurface away from a singular set of Hausdorff dimension $\le n-8$. So for $n \le 7$ the competitor may be taken smooth.

**Gauss equation.** For a hypersurface $\Sigma \subset M$ with second fundamental form $A$ and principal curvatures $\kappa_1,\dots,\kappa_{n-1}$, the intrinsic and ambient sectional curvatures satisfy
$$K^\Sigma(e_i,e_j) \;=\; K^M(e_i,e_j) + \kappa_i\kappa_j .$$
For $K^M \le 0$ this gives $K^\Sigma \le \kappa_i \kappa_j$, converting an ambient curvature hypothesis into control on the Gauss–Kronecker curvature $\mathrm{GK} = \det A = \prod_i \kappa_i$.

**Gauss–Bonnet / total curvature.** For a closed hypersurface $\Sigma^{n-1} = \partial\Omega$ bounding a domain in $\mathbb{R}^n$, $\int_\Sigma \mathrm{GK}^+ \ge |\mathbb{S}^{n-1}| = n\omega_n$. The *total curvature conjecture* asserts the same lower bound in Cartan–Hadamard manifolds; it implies the isoperimetric statement in low dimensions via the Gauss equation and the arithmetic–geometric mean inequality
$$\Big(\tfrac{1}{n-1}\textstyle\sum_i \kappa_i\Big)^{n-1} \ge \prod_i \kappa_i .$$

**Santaló formula (integral geometry).** For $\Omega$ with boundary, integrating over the unit sphere bundle,
$$\int_{U\Omega} f \,=\, \int_{\partial^+ U\Omega} \int_0^{\ell(v)} f(\gamma_v(t))\,\langle v,\nu\rangle \,dt\,dv ,$$
which converts volume and boundary area into averages of geodesic chord lengths. Under $K \le 0$ geodesics spread, so chords are comparatively long — the mechanism behind Croke's proof.

## 3. History & State of the Art (SOTA)

- **1926.** André Weil, still a student, proved the $n=2$ case for simply connected surfaces with $K \le 0$ (*Sur les surfaces à courbure négative*), using conformal/isothermal coordinates. Beckenbach–Radó (1933) gave an independent subharmonicity proof.
- **1976.** Thierry Aubin formulated the general-dimension conjecture with model comparison in the Sobolev-inequality context; Gromov and Burago–Zalgaller subsequently propagated it, so it is variously attributed as the Cartan–Hadamard, Aubin, Gromov, or generalized Weil conjecture.
- **1984.** Christopher Croke proved the case $n = 4$, $\kappa = 0$, by an integral-geometric argument built on the Santaló formula and a Berger–Kazdan-type comparison. Dimension 4 is special: the chord-length estimate is sharp only there.
- **1992.** Bruce Kleiner proved $n = 3$ for all $\kappa \le 0$, using the Gauss equation on a smooth minimizing boundary plus Gauss–Bonnet on the 2-dimensional minimizer.
- **2008.** Felix Schulze developed flows by powers of mean curvature as a route to sharp isoperimetric and Michael–Simon-type inequalities; the method is limited by the $n \le 7$ regularity threshold and by singularity formation.
- **2019.** Benoît Kloeckner and Greg Kuperberg (*The Cartan–Hadamard conjecture and the Little Prince*) completed dimension 4 for all $\kappa \le 0$ and reorganized the whole problem, introducing a "sharp comparison for the isoperimetric profile of nested domains" framework and reducing the general case to a statement about the total curvature of minimizers.
- **2022.** Mohammad Ghomi and Joel Spruck proved a total-curvature (Gauss–Bonnet-type) inequality in Cartan–Hadamard manifolds, yielding a new proof of the $n = 4$ case and conditional statements in higher dimensions.

## 4. Partial Results / Verified Cases

- **$n = 2$, all $\kappa \le 0$:** Weil (1926), Beckenbach–Radó (1933). Complete, with rigidity.
- **$n = 3$, all $\kappa \le 0$:** Kleiner (1992).
- **$n = 4$, $\kappa = 0$:** Croke (1984). **$n = 4$, all $\kappa \le 0$:** Kloeckner–Kuperberg (2019); reproved by Ghomi–Spruck (2022) via total curvature.
- **All $n$, small volumes:** in a compact manifold (or under uniform curvature bounds) with $K \le \kappa$, the sharp model comparison $I_M(v) \ge I_{M_\kappa^n}(v)$ holds for $v$ below an explicit threshold — Morgan–Johnson (2000), refined by Druet (2002). Isoperimetric regions of small volume are nearly round balls, where curvature enters only perturbatively.
- **All $n$, non-sharp constants:** Croke (1984) and Michael–Simon-type arguments give $|\partial\Omega| \ge c(n)|\Omega|^{(n-1)/n}$ with $c(n) < n\omega_n^{1/n}$; the inequality is never in doubt, only its sharp constant.
- **All $n$, restricted classes:** domains that are convex, geodesic balls, or whose boundary satisfies the total-curvature hypothesis $\int_{\partial\Omega}\mathrm{GK}^+ \ge n\omega_n$ (Ghomi–Spruck 2022); products $M_1 \times \mathbb{R}^k$ and manifolds with sufficient symmetry reduce to lower-dimensional cases.
- **Opposite curvature sign, for contrast:** Brendle (2023) proved the sharp isoperimetric/Sobolev inequality on manifolds with nonnegative Ricci curvature and Euclidean volume growth by the Alexandrov–Bakelman–Pucci (ABP) method — a sharp result that does *not* transfer to $K \le 0$.

## 5. Principal Obstacles

- **No mass transport / ABP argument works.** ABP and optimal-transport proofs of sharp isoperimetric inequalities need a *lower* Ricci bound to control the Jacobian of the transport map. Under $K \le 0$ the Ricci curvature is unbounded below, and the Bishop–Gromov comparison used in those proofs points the wrong way.
- **Symmetrization has no target.** Euclidean and space-form proofs symmetrize to a ball; a general Cartan–Hadamard manifold has no group action, no pole-independent radial structure and no canonical rearrangement, so Schwarz symmetrization is unavailable.
- **Curvature enters only through the second fundamental form.** Kleiner's method needs Gauss–Bonnet on $\partial\Omega$, an intrinsic $(n-1)$-dimensional statement — available only for $n-1 = 2$. In higher dimensions the Chern–Gauss–Bonnet integrand is a curvature polynomial with mixed signs and no usable lower bound.
- **Croke's chord estimate degenerates.** The Santaló/Berger–Kazdan comparison is sharp precisely at $n = 4$; for $n \ge 5$ the resulting constant falls strictly below $n\omega_n^{1/n}$, and no known repair recovers the loss.
- **Non-compactness and existence.** Isoperimetric regions need not exist in a noncompact Cartan–Hadamard manifold (mass can escape to infinity), so one must argue with almost-minimizers or exhaustions, blocking direct variational arguments.
- **Singularities.** For $n \ge 8$ minimizing boundaries can be singular, and for $n\ge 8$ any Gauss-equation argument must handle a singular set.

## 6. The Gap

Proven: $n \le 4$ in full, plus all $n$ for small volume or under an assumed total-curvature bound. Conjectured: all $n \ge 5$ for arbitrary volume.

The precise missing step is a **dimension-free lower bound on the total curvature of a minimizing boundary**. Concretely: show that for a smooth closed hypersurface $\Sigma = \partial\Omega$ in a Cartan–Hadamard $n$-manifold,
$$\int_\Sigma \mathrm{GK}^+ \, d\mu \;\ge\; n\,\omega_n = |\mathbb{S}^{n-1}| .$$
Given this, the Gauss equation plus AM–GM upgrades a mean-curvature bound to the isoperimetric inequality. Equivalently, in Kloeckner–Kuperberg's formulation, one must show that the *normal-exponential map* from the outward-convex part of $\Sigma$ covers the unit sphere of directions at least once with the right multiplicity — a statement true in $\mathbb{R}^n$ by a support-hyperplane argument that has no Cartan–Hadamard analogue, because parallel transport in a curved space is path-dependent.

## 7. Current Research (as of June 2026)

- **Total curvature program (Ghomi, Ohio State; Spruck, Johns Hopkins).** Ongoing work extending the 2022 Gauss–Bonnet-type inequality to nonconvex hypersurfaces and to $n \ge 5$, together with rigidity statements for the equality case. *(frontier — verify)*
- **Kloeckner–Kuperberg school (Grenoble / UC Davis).** Refinement of the "Little Prince" reduction: identify the minimal set of comparison hypotheses on nested domains that force the sharp profile, and check them in dimension 5.
- **Geometric flows (Schulze and collaborators, Free University Berlin).** Flow by powers of mean curvature and inverse mean curvature flow with weak (level-set) formulations, aiming at monotone isoperimetric-type quantities that survive singularities.
- **Nonlinear potential theory / $p$-capacity.** Adaptation of Agostiniani–Fogagnolo–Mazzieri-style monotonicity formulas, developed for nonnegative Ricci curvature, to nonpositive sectional curvature. *(frontier — verify)*
- **Synthetic geometry.** CAT(0) and $\mathrm{RCD}$-space formulations, testing whether the conjecture is a metric-measure statement or genuinely Riemannian; a counterexample in the synthetic category would be informative either way.

## 8. Future Work

- Settle **$n = 5$** in the $\kappa = 0$ case; every commentator treats this as the decisive test, since it is the first dimension where both Croke's and Kleiner's mechanisms fail while minimizers are still smooth.
- Prove the **total curvature conjecture** in full; Ghomi and Spruck have argued this is the correct primary statement, with the isoperimetric inequality as a corollary.
- Develop a **curvature-adapted symmetrization** or a transport map whose Jacobian is controlled by an upper sectional bound rather than a lower Ricci bound.
- Look for **counterexamples** with large negative curvature concentrated on a thin set — Kloeckner–Kuperberg explicitly note the conjecture's plausibility is not overwhelming in high dimensions, and no heuristic rules out failure for $n \gg 1$.
- Establish **existence and structure of isoperimetric regions** in Cartan–Hadamard manifolds under mild asymptotic hypotheses, removing the compactness obstruction.

## 9. Key References

- **[Foundational]** A. Weil. *Sur les surfaces à courbure négative.* C. R. Acad. Sci. Paris **182** (1926), 1069–1071.
- **[Foundational]** E. F. Beckenbach and T. Radó. *Subharmonic functions and surfaces of negative curvature.* Transactions of the American Mathematical Society **35** (1933), 662–674. [DOI](https://doi.org/10.1090/s0002-9947-1933-1501708-x)
- **[Foundational]** T. Aubin. *Problèmes isopérimétriques et espaces de Sobolev.* Journal of Differential Geometry **11** (1976), 573–598. [DOI](https://doi.org/10.4310/jdg/1214433725)
- **[Foundational]** C. B. Croke. *A sharp four-dimensional isoperimetric inequality.* Commentarii Mathematici Helvetici **59** (1984), 187–192. [DOI](https://doi.org/10.1007/bf02566344)
- **[Foundational]** B. Kleiner. *An isoperimetric comparison theorem.* Inventiones Mathematicae **108** (1992), 37–47. [DOI](https://doi.org/10.1007/bf02100598)
- **[SOTA / Recent]** B. Kloeckner and G. Kuperberg. *The Cartan–Hadamard conjecture and the Little Prince.* Revista Matemática Iberoamericana **35** (2019), no. 4, 1195–1258. [DOI](https://doi.org/10.4171/rmi/1082)
- **[SOTA / Recent]** M. Ghomi and J. Spruck. *Total curvature and the isoperimetric inequality in Cartan–Hadamard manifolds.* Journal of Geometric Analysis **32** (2022), Paper No. 50. [DOI](https://doi.org/10.1007/s12220-021-00801-2)
- **[SOTA / Recent]** F. Schulze. *Nonlinear evolution by mean curvature and isoperimetric inequalities.* Journal of Differential Geometry **79** (2008), 197–241. [DOI](https://doi.org/10.4310/jdg/1211512640)
- **[SOTA / Recent]** S. Brendle. *Sobolev inequalities in manifolds with nonnegative curvature.* Communications on Pure and Applied Mathematics **76** (2023), 2192–2218. [DOI](https://doi.org/10.1002/cpa.22070)
- **[Related]** F. Morgan and D. L. Johnson. *Some sharp isoperimetric theorems for Riemannian manifolds.* Indiana University Mathematics Journal **49** (2000), 1017–1041. [DOI](https://doi.org/10.1512/iumj.2000.49.1929)
- **[Related]** O. Druet. *Sharp local isoperimetric inequalities involving the scalar curvature.* Proceedings of the American Mathematical Society **130** (2002), 2351–2361. [DOI](https://doi.org/10.1090/s0002-9939-02-06355-4)
- **[Survey]** Yu. D. Burago and V. A. Zalgaller. *Geometric Inequalities.* Grundlehren der mathematischen Wissenschaften 285, Springer, 1988.
- **[Survey]** M. Ritoré and C. Sinestrari. *Mean Curvature Flow and Isoperimetric Inequalities.* Advanced Courses in Mathematics CRM Barcelona, Birkhäuser, 2010. [DOI](https://doi.org/10.1007/978-3-0346-0213-6)

## 10. Worked Example / Concrete Special Case

**The case $n = 2$, proved in full.** Let $M^2$ be a Cartan–Hadamard surface ($K \le 0$, simply connected) and $\Omega \subset M$ a compact domain with smooth boundary, diffeomorphic to a disc.

Let $\Omega_s = \{x \in \Omega : \mathrm{dist}(x, \partial\Omega) \ge s\}$ be the inner parallel sets, $A(s) = |\Omega_s|$ and $L(s) = |\partial\Omega_s|$, defined for $s \in [0, s_{\max}]$ where $s_{\max}$ is the inradius.

**Step 1 (coarea).** $A'(s) = -L(s)$.

**Step 2 (Gauss–Bonnet).** For each regular value $s$, $\partial\Omega_s$ is a curve with geodesic curvature $\kappa_g$ (computed with respect to the inward normal), and
$$\int_{\partial\Omega_s}\kappa_g \, d\ell \;=\; 2\pi\chi(\Omega_s) - \int_{\Omega_s} K \, dA \;\ge\; 2\pi ,$$
using $\chi(\Omega_s) = 1$ (simply connected, so components are discs) and $K \le 0$.

**Step 3 (first variation of length).** $L'(s) = -\int_{\partial\Omega_s}\kappa_g\,d\ell \le -2\pi$.

**Step 4 (monotonicity of the isoperimetric deficit).** Set $D(s) = L(s)^2 - 4\pi A(s)$. Then
$$D'(s) = 2L L' - 4\pi A' = 2L L' + 4\pi L = 2L\big(L'(s) + 2\pi\big) \le 0 ,$$
since $L \ge 0$ and $L' \le -2\pi$. So $D$ is nonincreasing.

**Step 5 (extinction).** As $s \uparrow s_{\max}$ the sets $\Omega_s$ collapse: $A(s) \to 0$ and $L(s) \to 0$, hence $D(s) \to 0$.

**Conclusion.** $D(0) \ge \lim_{s\to s_{\max}} D(s) = 0$, i.e.
$$L(0)^2 \ge 4\pi A(0), \qquad\text{that is}\qquad |\partial\Omega| \ge 2\sqrt{\pi}\,|\Omega|^{1/2} = 2\omega_2^{1/2}|\Omega|^{1/2},$$
which is exactly the $n = 2$ case of Section 1. Equality forces $K \equiv 0$ on $\Omega$ and $\kappa_g \equiv$ const, so $\Omega$ is a Euclidean disc.

**Why this does not generalize.** Step 2 is Gauss–Bonnet on a *1-dimensional* boundary; in dimension $n$ the same step would require a sign-definite lower bound for the Chern–Gauss–Bonnet integrand of the $(n-1)$-dimensional hypersurface $\partial\Omega_s$, which fails for $n - 1 \ge 3$. Kleiner's $n = 3$ proof uses Gauss–Bonnet on the 2-dimensional minimizing boundary — the last dimension where the argument survives. Everything at $n \ge 5$ needs a genuinely new mechanism.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*