---
id: 05-analysis/kazdan-warner-problem
title: "Kazdan-Warner Problem"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kazdan-Warner Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kazdan-warner-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a smooth compact manifold without boundary, $\dim M = n$.

- **Prescribed curvature problem (unrestricted).** Which functions $f \in C^\infty(M)$ arise as the Gaussian curvature ($n=2$) or scalar curvature ($n \ge 3$) of some Riemannian metric on $M$?
- **Conformal Kazdan-Warner problem.** Fix a metric $g_0$. Which $f \in C^\infty(M)$ arise as the curvature of a metric $g$ conformal to $g_0$, i.e. $g = e^{2u} g_0$ ($n=2$) or $g = u^{4/(n-2)} g_0$ ($n \ge 3$)?

The unrestricted problem is fully answered in dimension 2 and — modulo the classification of manifolds admitting positive scalar curvature — in dimension $\ge 3$. The **conformal** problem remains open. Its hardest instance is the case $M = S^n$ with the round metric, the **Nirenberg problem** ($n=2$) and its higher-dimensional analogue: give necessary *and* sufficient conditions on $f$ for solvability. A complete resolution means an intrinsic, checkable characterization of the admissible $f$ on each conformal class, together with a description of the solution set (multiplicity, compactness, degree).

## 2. Mathematical Foundations

**Dimension 2.** Under $g = e^{2u} g_0$ the Gauss curvature transforms by
$$-\Delta_{g_0} u + K_0 = K\, e^{2u},$$
where $\Delta_{g_0}$ is the (negative-spectrum) Laplace-Beltrami operator and $K_0$ is the curvature of $g_0$. Integrating and using Gauss-Bonnet,
$$\int_M K\, e^{2u}\, dA_{g_0} = \int_M K_0\, dA_{g_0} = 2\pi\chi(M),$$
so $\operatorname{sign}\chi(M)$ forces $K$ to be positive somewhere ($\chi>0$), negative somewhere ($\chi<0$), or to change sign / vanish identically ($\chi=0$). Normalizing $K_0 \equiv$ const splits the problem into three regimes by $\chi(M)$.

The energy functional on $H^1(M)$ is
$$J(u) = \int_M |\nabla u|^2\, dA + 2\int_M K_0 u\, dA - 2\pi\chi(M)\,\log\!\Big(\int_M K e^{2u} dA\Big),$$
whose criticality is controlled by the **Moser-Trudinger inequality**: for $\int_M u = 0$,
$$\int_M e^{4\pi u^2 / \|\nabla u\|_2^2}\, dA \le C|M|.$$
The constant $4\pi$ (equivalently $8\pi$ in the $\int e^{2u}$ normalization) is sharp; the functional loses coercivity exactly at $\chi(M) = 2$, i.e. on $S^2$.

**Kazdan-Warner obstruction.** On $(S^2, g_{S^2})$, with $x_j$ the restriction of the $j$-th coordinate function (a first spherical harmonic, $\Delta x_j = -2x_j$), every solution satisfies
$$\int_{S^2} \langle \nabla K, \nabla x_j\rangle\, e^{2u}\, dA = 0, \qquad j = 1,2,3.$$
Bourguignon-Ezin (1987) generalized this: $\int_M X(R_g)\, dV_g = 0$ for any conformal Killing field $X$.

**Dimension $n \ge 3$.** With $g = u^{4/(n-2)}g_0$, $u > 0$, the scalar curvature equation is the Yamabe-type semilinear equation
$$-\frac{4(n-1)}{n-2}\,\Delta_{g_0} u + R_0\, u = R\, u^{\frac{n+2}{n-2}},$$
critical for the Sobolev embedding $H^1 \hookrightarrow L^{2n/(n-2)}$, so Palais-Smale sequences fail compactness by bubbling at the Aubin threshold $S = n(n-1)\omega_n^{2/n}$.

**Kazdan-Warner trichotomy.** Every compact $M^n$, $n\ge 3$, lies in exactly one class:
$(P)$ admits a metric of positive scalar curvature; $(Z)$ admits a scalar-flat metric but no positive one; $(N)$ every metric has scalar curvature negative somewhere.

## 3. History & State of the Art (SOTA)

- **1971-73.** Berger studies conformal deformation on surfaces; Moser proves that on $S^2$ any $K$ that is positive somewhere and **antipodally symmetric** ($K(-x)=K(x)$) is admissible, exploiting the doubled Moser-Trudinger constant on the symmetric subspace.
- **1974-75.** Kazdan and Warner publish the defining series in *Annals of Mathematics* and *J. Differential Geometry*: compact surfaces, open surfaces, conformal deformation, and the scalar curvature trichotomy. They also discover the obstruction identity, which rules out $K = 2 + x_3$ on $S^2$ and shows the problem is not merely a sign condition.
- **1980s.** Aubin and Schoen-Yau settle the Yamabe problem (constant $R$), providing the compactness technology. Bahri-Coron introduce critical-points-at-infinity / algebraic topology of sublevel sets.
- **1987-88.** Chang and Yang give the first general sufficient condition on $S^2$ beyond symmetry: a Morse-theoretic index count at the critical points of $K$.
- **1991-96.** Bahri-Coron ($S^3$), Chang-Gursky-Yang ($S^2, S^3$), and Y. Li ($S^n$, all $n$) develop degree-theoretic and flatness-order criteria.
- **2005-present.** Struwe's flow approach, Borer-Galimberti-Struwe's "large" metrics on higher-genus surfaces, and blow-up/Lyapunov-Schmidt analyses for non-generic $K$.

## 4. Partial Results / Verified Cases

- **$\chi(M) < 0$ (genus $\ge 2$).** $K$ admissible in the conformal class if $K \le 0$, $K \not\equiv 0$ (Berger; Kazdan-Warner). If $K$ changes sign, there is a threshold: writing $K_t = K + t$ with $\bar K < 0$, there exists $t^*(K) \in (0,\infty]$ such that $K_t$ is solvable for $t < t^*$ and not for $t > t^*$. Borer-Galimberti-Struwe (2015) construct a **second**, "large" solution for $t < t^*$ when $\max K > 0$.
- **$\chi(M) = 0$ (torus, Klein bottle).** Complete answer (Kazdan-Warner 1974): $K$ is conformally admissible iff $K \equiv 0$, or $K$ changes sign and $\int_M K\, dA_{g_0} < 0$.
- **$\chi(M) > 0$, $M = \mathbb{RP}^2$.** Complete: $K$ admissible iff $K > 0$ somewhere (no conformal group obstruction, since $\mathbb{RP}^2$ has no nontrivial conformal Killing fields beyond isometries).
- **$M = S^2$ (Nirenberg problem).** Solvable when: $K$ antipodally symmetric and positive somewhere (Moser 1973); $K$ a positive Morse function with $\Delta K \ne 0$ at every critical point and
 $$\sum_{\{\nabla K(q)=0,\ \Delta K(q)<0\}} (-1)^{\operatorname{ind}(q)} \ne -1$$
 (Chang-Yang 1987/88); $K$ close to a positive constant (perturbative, Chang-Yang, Ambrosetti-Malchiodi).
- **$S^n$, $n \ge 3$.** Bahri-Coron (1991) solve $S^3$ under a Morse index-count/degree condition; Y. Li (1995, 1996) proves solvability on $S^n$ for $K$ with prescribed **flatness order** $\beta \in (n-2, n)$ at critical points plus a degree condition $\deg \ne 0$; Chen-Lin obtain a priori estimates by moving planes.
- **Unrestricted problem, $n \ge 3$.** Fully solved by Kazdan-Warner: in class $(N)$, $f$ is a scalar curvature iff $f$ is negative somewhere; in $(Z)$, iff $f \equiv 0$ or $f<0$ somewhere; in $(P)$, **every** $f \in C^\infty(M)$ is a scalar curvature. Membership in $(P)$ is topological: Gromov-Lawson/Schoen-Yau for surgery and enlargeability; Stolz (1992) proves for simply connected $M^n$, $n\ge5$, that $(P)$ holds iff $M$ is non-spin, or spin with vanishing $\alpha$-invariant.
- **Singular case.** Troyanov (1991) settles surfaces with conical singularities in the subcritical regime via a Trudinger-type inequality with modified constant.

## 5. Principal Obstacles

1. **Critical-exponent noncompactness.** In $n=2$ the Moser-Trudinger constant is achieved exactly at the $S^2$ energy level; in $n\ge3$ the nonlinearity $u^{(n+2)/(n-2)}$ sits at the Sobolev exponent. Minimizing sequences can concentrate into bubbles modeled on the conformal group $\mathrm{Conf}(S^n) \cong SO(n+1,1)$, which is non-compact. Direct variational methods therefore fail without an energy quantization argument.
2. **The obstruction is not an obstruction theory.** The Kazdan-Warner identity is a necessary condition, but no one has produced a family of conditions that is also sufficient. It shows the admissible set is neither open nor closed in $C^\infty$ in any obvious way, so implicit-function/perturbation methods only reach neighbourhoods of constants.
3. **Degenerate critical points.** All sharp criteria (Chang-Yang, Bahri-Coron, Li) assume $K$ Morse or of prescribed flatness order. When $\Delta K = 0$ at a critical point, or $K$ vanishes on a set of positive measure, the finite-dimensional reduction's reduced functional degenerates and the interaction between bubbles is no longer governed by the leading Taylor term.
4. **Sign-changing $K$ and the threshold $t^*$.** For $\chi<0$ nobody knows whether $t^*(K)$ is finite in general, nor what happens at $t = t^*$; blow-up analysis at the threshold mixes bubbling with degeneracy of the linearized operator.
5. **Multiple-bubble configurations.** Beyond one bubble, the critical points at infinity form a stratified space whose Morse theory is only computed in low dimensions or under strong nondegeneracy.

## 6. The Gap

Proven: solvability under (a) symmetry, (b) perturbation of a constant, (c) Morse/flatness genericity with a nonvanishing degree count. Wanted: a characterization of $\{K : K \text{ admissible in } [g_0]\}$ valid for **all** $K \in C^\infty$, on **all** conformal classes.

Concretely, the missing step for $S^n$ is a topological degree formula for the equation that is valid without genericity — i.e. an extension of Li's degree $\deg(K) = \sum_{q} (-1)^{n - \operatorname{ind}(q)}$ over degenerate $K$ — together with a proof that $\deg \ne 0$ is necessary as well as sufficient. Equivalently: is there a computable invariant $I(K)$, refining the Kazdan-Warner/Bourguignon-Ezin identity, whose non-vanishing is *equivalent* to solvability?

## 7. Current Research (as of June 2026)

- **Flow methods.** Struwe-type prescribed-curvature flows and their blow-up analysis remain the main tool for existence beyond perturbation; work on convergence for sign-changing $K$ on higher genus surfaces continues in the Zurich (ETH) and Basel circles.
- **Finite-dimensional reduction at degenerate points.** Groups around Y. Li (Rutgers), J. Wei (UBC/Chinese University of Hong Kong), and M. Musso / A. Pistoia (Bath / Sapienza) push Lyapunov-Schmidt to non-Morse $K$ and to towers of bubbles. *(frontier — verify)*
- **Mean-field / Liouville connections.** The $n=2$ equation is the Liouville / mean-field equation $\Delta u + \rho(Ke^{u}/\int Ke^u - 1) = 0$; degree formulas of Chen-Lin at non-critical $\rho$ inform the curvature problem.
- **Nonlocal analogues.** Prescribed $Q$-curvature and fractional GJMS operators reproduce the same trichotomy with different obstruction identities; results transfer partially back to the classical case.
- **Singular and non-compact settings.** Prescribed curvature on surfaces with conical singularities and on complete open surfaces (the second 1974 Kazdan-Warner paper) is active, driven by ties to hyperbolic geometry and integrable systems.

## 8. Future Work

- Prove or disprove finiteness of the threshold $t^*(K)$ for $\chi(M)<0$ and classify the borderline behaviour at $t=t^*$.
- Develop a degree theory for the curvature equation robust under degeneracy of $K$ — the analogue of Li's index formula without flatness hypotheses.
- Determine sharp a priori bounds for solutions on $S^n$ with sign-changing $K$; current moving-plane estimates require $K>0$.
- Establish compactness/multiplicity for the full solution set: how many conformal metrics realize a given admissible $K$?
- Extend Kazdan-Warner's unrestricted trichotomy to prescribing the full Ricci tensor, where even local solvability is delicate (DeTurck).

## 9. Key References

- **[Foundational]** J. L. Kazdan and F. W. Warner. *Curvature functions for compact 2-manifolds.* Annals of Mathematics 99 (1974), 14-47.
- **[Foundational]** J. L. Kazdan and F. W. Warner. *Curvature functions for open 2-manifolds.* Annals of Mathematics 99 (1974), 203-219.
- **[Foundational]** J. L. Kazdan and F. W. Warner. *Existence and conformal deformation of metrics with prescribed Gaussian and scalar curvatures.* Annals of Mathematics 101 (1975), 317-331.
- **[Foundational]** J. L. Kazdan and F. W. Warner. *Scalar curvature and conformal deformation of Riemannian structure.* Journal of Differential Geometry 10 (1975), 113-134.
- **[Foundational]** J. Moser. *On a nonlinear problem in differential geometry.* In *Dynamical Systems* (Salvador, 1971), Academic Press, 1973, 273-280.
- **[SOTA]** S.-Y. A. Chang and P. C. Yang. *Prescribing Gaussian curvature on $S^2$.* Acta Mathematica 159 (1987), 215-259.
- **[SOTA]** S.-Y. A. Chang and P. C. Yang. *Conformal deformation of metrics on $S^2$.* Journal of Differential Geometry 27 (1988), 259-296.
- **[SOTA]** A. Bahri and J.-M. Coron. *The scalar curvature problem on the standard three-dimensional sphere.* Journal of Functional Analysis 95 (1991), 106-172.
- **[SOTA]** Y. Li. *Prescribing scalar curvature on $S^n$ and related problems, Part I.* Journal of Differential Equations 120 (1995), 319-410; *Part II*, Communications on Pure and Applied Mathematics 49 (1996), 541-597.
- **[SOTA]** M. Struwe. *A flow approach to Nirenberg's problem.* Duke Mathematical Journal 128 (2005), 19-64.
- **[SOTA]** F. Borer, L. Galimberti and M. Struwe. *"Large" conformal metrics of prescribed Gauss curvature on surfaces of higher genus.* Commentarii Mathematici Helvetici 90 (2015), 407-428.
- **[Related]** J.-P. Bourguignon and J.-P. Ezin. *Scalar curvature functions in a conformal class of metrics and conformal transformations.* Transactions of the AMS 301 (1987), 723-736.
- **[Related]** M. Troyanov. *Prescribing curvature on compact surfaces with conical singularities.* Transactions of the AMS 324 (1991), 793-821.
- **[Related]** S. Stolz. *Simply connected manifolds of positive scalar curvature.* Annals of Mathematics 136 (1992), 511-540.
- **[Survey]** J. L. Kazdan. *Prescribing the Curvature of a Riemannian Manifold.* CBMS Regional Conference Series in Mathematics 57, AMS, 1985.
- **[Survey]** T. Aubin. *Some Nonlinear Problems in Riemannian Geometry.* Springer Monographs in Mathematics, 1998.

## 10. Worked Example / Concrete Special Case

**Claim.** On $(S^2, g_{S^2})$ the function $K(x) = 2 + x_3$ (smooth, strictly positive, $1 \le K \le 3$) is **not** the Gauss curvature of any conformal metric — even though it satisfies the obvious sign condition demanded by Gauss-Bonnet ($\chi = 2 > 0$ requires only $K>0$ somewhere).

*Step 1 — the equation.* With $K_0 \equiv 1$, a conformal metric $g = e^{2u}g_{S^2}$ has curvature $K$ iff
$$-\Delta u + 1 = K e^{2u} \quad \text{on } S^2 .$$

*Step 2 — the Kazdan-Warner identity.* Let $x_3$ be the third coordinate function, so $\Delta x_3 = -2x_3$. Multiply the equation by $\langle\nabla u, \nabla x_3\rangle$ and integrate; using the conformal Killing property of $\nabla x_3$ (i.e. $\nabla^2 x_3 = -x_3\, g_{S^2}$) and integrating by parts, all terms involving $u$ cancel and one is left with
$$\int_{S^2} \langle \nabla K, \nabla x_3\rangle\, e^{2u}\, dA = 0 .$$
(Equivalently: the flow of $\nabla x_3$ generates conformal diffeomorphisms, and the identity is the first-order condition for invariance of the functional $J$ along that flow.)

*Step 3 — evaluate.* Here $\nabla K = \nabla x_3$, so the identity forces
$$\int_{S^2} |\nabla x_3|^2\, e^{2u}\, dA = 0 .$$
But $|\nabla x_3|^2 = 1 - x_3^2 > 0$ off the two poles and $e^{2u} > 0$, so the integrand is positive on a set of full measure. Contradiction. Hence no solution $u$ exists. $\square$

*Step 4 — contrast.* Replace $K$ by $\tilde K(x) = 2 + x_3^2$. Now $\tilde K(-x) = \tilde K(x)$ and $\tilde K > 0$, so Moser's theorem applies: minimize $J$ over the antipodally symmetric subspace of $H^1(S^2)$, where the Moser-Trudinger constant doubles to $8\pi$ and $J$ becomes coercive; the minimizer is smooth by elliptic regularity, and by uniqueness of the symmetric critical point it solves the unsymmetrized equation. So $\tilde K$ **is** admissible.

The pair $(2+x_3,\; 2+x_3^2)$ is the canonical illustration: two positive functions, arbitrarily close in $C^0$ after scaling, on opposite sides of the admissibility boundary. Locating that boundary in general is the open part of the Kazdan-Warner problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*