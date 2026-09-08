---
id: 05-analysis/nirenberg-problem
title: "Nirenberg Problem"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nirenberg Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/nirenberg-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(S^2, g_0)$ be the round $2$-sphere with Gaussian curvature $K_{g_0} \equiv 1$. **Nirenberg's problem** asks:

> For which functions $K \in C^\infty(S^2)$ does there exist a metric $g$ conformal to $g_0$ whose Gaussian curvature is exactly $K$?

Writing $g = e^{2u} g_0$, this is the solvability question for the semilinear elliptic PDE
$$-\Delta_{g_0} u + 1 = K e^{2u} \quad \text{on } S^2 ,$$
where $\Delta_{g_0}$ is the Laplace–Beltrami operator of the round metric.

The $n$-dimensional analogue (the **prescribed scalar curvature problem on $S^n$**, $n \ge 3$) asks, for $K \in C^\infty(S^n)$, for a positive solution $u$ of
$$-\frac{4(n-1)}{n-2}\,\Delta_{g_0} u + n(n-1)\,u = K\, u^{\frac{n+2}{n-2}},$$
so that $g = u^{4/(n-2)} g_0$ has scalar curvature $R_g = K$.

A complete resolution would be a set of conditions on $K$ that are **both necessary and sufficient** for solvability — currently unavailable in any dimension. The problem is therefore classified *partially-solved*: large sufficient classes and one sharp family of obstructions are known, with a gap between them.

## 2. Mathematical Foundations

**Conformal change in dimension 2.** If $g = e^{2u}g_0$ on a surface, the Gaussian curvatures satisfy
$$K_g = e^{-2u}\big(K_{g_0} - \Delta_{g_0} u\big).$$
With $K_{g_0}=1$ this gives the equation of §1. Gauss–Bonnet forces the integral constraint
$$\int_{S^2} K\, e^{2u}\, dA_{g_0} = 2\pi\chi(S^2) = 4\pi,$$
so $K$ must be **positive somewhere**. Also, integrating the PDE, $\int_{S^2}(K e^{2u}-1)=0$.

**Variational structure.** Solutions are critical points of
$$J_K[u] = \frac{1}{2}\int_{S^2} |\nabla u|^2 \,dA + 2\!\int_{S^2} u \, dA - 4\pi \log\!\left(\int_{S^2} K e^{2u}\,dA\right),$$
on $H^1(S^2)$. The relevant borderline embedding is the **Moser–Trudinger inequality**
$$\log \fint_{S^2} e^{2(u-\bar u)}\,dA \le \frac{1}{4\pi}\int_{S^2}|\nabla u|^2\,dA ,$$
which makes $J_K$ bounded below when $K \equiv \text{const}$ but with a *noncompact* minimizing structure: equality holds along the noncompact family of conformal dilations.

**Conformal group and loss of compactness.** The Möbius group $\mathrm{Conf}(S^2)\cong PSL(2,\mathbb{C})$ acts by $\varphi_{p,t}$ (dilations of factor $t$ centred at $p\in S^2$); $J_1$ is invariant under it. Palais–Smale sequences fail to converge precisely by concentrating as bubbles $e^{2u}\,dA \rightharpoonup 4\pi\,\delta_p$.

**The Kazdan–Warner obstruction.** If $u$ solves $-\Delta u + 1 = Ke^{2u}$ then for each first spherical harmonic $x_j$ ($j=1,2,3$, the restriction of a linear coordinate),
$$\int_{S^2} \langle \nabla K, \nabla x_j\rangle\, e^{2u}\, dA_{g_0} = 0 .$$
The $n\ge3$ analogue (Kazdan–Warner, Bourguignon–Ezin) reads $\int_{S^n}\langle\nabla K,\nabla x_j\rangle\, u^{\frac{2n}{n-2}}\,dA = 0$. These identities come from testing the equation against the conformal Killing fields $\nabla x_j$.

**Degree / index data.** For $K$ a positive Morse function with $\Delta K \ne 0$ at every critical point, set
$$\mathcal{S}^- = \{p : \nabla K(p)=0,\ \Delta K(p) < 0\}, \qquad \sigma(K) = \sum_{p \in \mathcal{S}^-} (-1)^{\mathrm{ind}(p)} .$$
Poincaré–Hopf gives $\sum_{\text{all }p}(-1)^{\mathrm{ind}(p)}=\chi(S^2)=2$.

## 3. History & State of the Art (SOTA)

- **Early 1970s.** Louis Nirenberg poses the question in seminars at NYU; it circulates as "Nirenberg's problem".
- **1973.** J. Moser proves solvability for $K$ **even** ($K(-x)=K(x)$) and positive somewhere, by restricting $J_K$ to the antipodally symmetric subspace where the Moser–Trudinger constant doubles, killing the bubbling.
- **1974–75.** Kazdan and Warner obtain the identity above, showing e.g. $K = 1+\varepsilon x_3$ is *not* attainable — the first genuine obstruction. They also settle the analogous question on surfaces of genus $\ge 1$ and $\chi \le 0$ completely.
- **1986–87.** Chen–Ding, Hong, and Chang–Yang give sufficient conditions via careful blow-up analysis; Chang–Yang (*Acta Math.*, 1987) prove solvability when $K>0$ is Morse, $\Delta K\ne0$ at critical points, and $\sigma(K)\ne -1$.
- **1988.** Chang–Yang extend to symmetric and degenerate settings (*JDG*).
- **1991.** Bahri–Coron settle a broad case on $S^3$ using critical points at infinity.
- **1993.** Chang–Gursky–Yang remove the nondegeneracy hypotheses on $S^2$ and $S^3$ under a general index-count condition.
- **1995–97.** Y.Y. Li develops a full blow-up/degree theory on $S^n$ under "flatness conditions" of order $\beta$; Chen–Lin give sharp a priori estimates via moving planes.
- **2005.** Struwe gives a flow-based proof (a normalised curvature flow) recovering and extending the Chang–Yang criterion on $S^2$.

**SOTA summary.** Sufficient criteria are index-theoretic or flatness-type; the only known necessary conditions are Gauss–Bonnet positivity and Kazdan–Warner. No characterisation exists.

## 4. Partial Results / Verified Cases

- **$K$ even on $S^2$, positive somewhere** — solvable (Moser 1973). Extends to $K$ invariant under a group acting without fixed points.
- **$K > 0$ Morse on $S^2$ with $\Delta K \ne 0$ at critical points and $\sigma(K) \ne -1$** — solvable (Chang–Yang 1987). Since $\sigma(K)\in\mathbb{Z}$ and the total index is $2$, "generic" $K$ satisfies this.
- **$K>0$ on $S^2$ with only nondegenerate critical points and $\max K/\min K$ close to $1$** — solvable by perturbation (Chen–Ding 1987; Moser).
- **Rotationally symmetric $K = K(x_3)$ on $S^2$**: solvable iff $K$ is positive somewhere and *not* monotone on $[-1,1]$ in the strict sense forced by Kazdan–Warner; monotone non-constant $K$ has no solution (the identity with $j=3$ gives a strictly signed integral).
- **$S^3$**: Bahri–Coron (1991) — $K>0$ Morse, $\Delta K\ne 0$ at critical points, and $\sum_{p\in\mathcal S^-}(-1)^{3-\mathrm{ind}(p)}\ne -1$.
- **$S^n$, $n\ge 3$, flatness order $\beta \in (n-2, n)$**: Y.Y. Li (1995, 1996) proves existence and computes a Leray–Schauder degree $-\sum_{p\in\mathcal S^-}(-1)^{n-\mathrm{ind}(p)}$; compactness of the solution set holds for $\beta\ge n-2$.
- **Locally conformally flat manifolds and $n=3$**: Escobar–Schoen (1986) give existence for $K$ positive with a nondegenerate maximum-type condition.
- **Antipodally symmetric $K>0$ on $S^n$**: solvable for all $n$ (Escobar–Schoen; Hebey), the higher-dimensional Moser phenomenon.
- **Multiplicity**: Ambrosetti–Malchiodi and Malchiodi produce arbitrarily many solutions for perturbative $K = 1 + \varepsilon f$ with $f$ Morse and suitable index data.

## 5. Principal Obstacles

- **Critical exponent / borderline embedding.** In $n=2$ the nonlinearity $e^{2u}$ sits exactly at the Moser–Trudinger threshold; for $n\ge3$ the exponent $\frac{n+2}{n-2}$ is the critical Sobolev exponent. The functional fails the Palais–Smale condition at *every* level of the form $J_1 + k\cdot(\text{bubble energy})$, so direct variational methods (mountain pass, minimisation) give no compactness.
- **Non-compact conformal group.** Bubbling is not a technical nuisance but an exact symmetry: $J_1$ has a noncompact manifold of minimisers. Any sufficient condition must break this degeneracy using $K$ itself, which is why all criteria are perturbative around the critical points of $K$.
- **Kazdan–Warner is not the only obstruction.** The identity rules out some $K$, but examples (rotationally symmetric $K$ with prescribed critical structure) show non-solvable $K$ satisfying it. So the obstruction set is strictly larger than the identity's zero set, and no algebraic description of it is known.
- **Degenerate critical points.** When $\Delta K = 0$ at a critical point, the finite-dimensional reduction's leading term vanishes; the expansion of $J_K$ along bubbles becomes order-dependent and no uniform theory covers all degeneracies.
- **Non-Morse / low regularity $K$.** Index-count conditions are meaningless for merely continuous $K$; approximation does not preserve solvability because solutions may blow up in the limit.
- **Moving-plane methods** give a priori bounds only under flatness assumptions on $K$ near critical points; without them, blow-up with *multiple* bubbles and non-simple blow-up points cannot be excluded in general.

## 6. The Gap

Proven necessary: $\max K > 0$, plus $\int \langle \nabla K, \nabla x_j\rangle e^{2u}=0$ (a condition on the *solution*, usable only through sign arguments). Proven sufficient: index-count conditions on the critical set of a Morse $K$ (with $\Delta K \ne 0$), or symmetry, or smallness of oscillation.

The gap is the entire zone between: functions $K$ that are positive somewhere, evade the Kazdan–Warner sign obstruction, but are degenerate or have $\sigma(K) = -1$. Concretely, the missing step is a **complete blow-up classification**: characterise which $K$ admit a sequence $u_k$ with $J_K$ energy approaching a multi-bubble level and no subsequential limit, in terms of $K$'s critical structure alone — including degenerate critical points and non-Morse $K$. Whether a purely local, checkable condition on $K$ characterising solvability exists is itself open; some believe the answer is genuinely non-local.

## 7. Current Research (as of June 2026)

- **Flow methods.** Descendants of Struwe's 2005 normalised curvature flow are used to obtain existence and convergence under weakened index hypotheses; groups in Germany (ETH/Zürich school lineage) and China continue this line. *(frontier — verify)*
- **Critical points at infinity / Bahri theory.** Continued by Bahri's students (Ben Ayed, Chtioui, El Mehdi and collaborators, largely in Tunisia and France), extending index counts to degenerate $K$ and to boundary-value analogues on the ball. Recent work targets $\sigma(K)=-1$ borderline cases. *(frontier — verify)*
- **Fractional and higher-order versions.** Prescribing $Q$-curvature (Paneitz operator, $n=4$) and fractional curvature for $(-\Delta)^s$ on $S^n$; these replicate the Nirenberg structure with new Kazdan–Warner-type identities. Active work by Jin, Xiong, Y.Y. Li and collaborators.
- **Sharp compactness.** Extensions of Chen–Lin a priori estimates to lower flatness orders $\beta \le n-2$, where multi-bubbling is expected.
- **Numerical/computational exploration.** Continuation methods on rotationally symmetric and low-mode $K$ to map the solvability boundary empirically.

## 8. Future Work

- Determine whether solvability for $K \in C^\infty(S^2)$ admits a characterisation by finitely many local invariants of $K$, or prove no such characterisation exists.
- Handle $\sigma(K) = -1$: decide solvability there, presumably via higher-order terms in the bubble expansion.
- Build a blow-up theory that does not assume $\Delta K \ne 0$ — e.g. via a full asymptotic expansion of $J_K$ near multi-bubble configurations with degenerate $K$.
- Extend to general compact manifolds with positive Yamabe invariant, where the conformal group is trivial but the bubbling persists.
- Transfer the $S^2$ techniques to $Q$-curvature and fractional curvature, where index conditions are only partially understood.

## 9. Key References

- **[Foundational]** J. Moser. *On a nonlinear problem in differential geometry.* In *Dynamical Systems* (M. Peixoto, ed.), Academic Press, 1973, pp. 273–280.
- **[Foundational]** J. Kazdan, F. Warner. *Curvature functions for compact 2-manifolds.* Annals of Mathematics 99 (1974), 14–47. [DOI](https://doi.org/10.2307/1971012)
- **[Foundational]** J. Kazdan, F. Warner. *Scalar curvature and conformal deformation of Riemannian structure.* Journal of Differential Geometry 10 (1975), 113–134. [DOI](https://doi.org/10.4310/jdg/1214432678)
- **[SOTA]** S.-Y. A. Chang, P. Yang. *Prescribing Gaussian curvature on $S^2$.* Acta Mathematica 159 (1987), 215–259.
- **[SOTA]** S.-Y. A. Chang, P. Yang. *Conformal deformation of metrics on $S^2$.* Journal of Differential Geometry 27 (1988), 259–296. [DOI](https://doi.org/10.4310/jdg/1214441783)
- **[SOTA]** A. Bahri, J.-M. Coron. *The scalar curvature problem on the standard three-dimensional sphere.* Journal of Functional Analysis 95 (1991), 106–172. [DOI](https://doi.org/10.1016/0022-1236(91)90026-2)
- **[SOTA]** S.-Y. A. Chang, M. Gursky, P. Yang. *The scalar curvature equation on 2- and 3-spheres.* Calculus of Variations and PDE 1 (1993), 205–229. [DOI](https://doi.org/10.1007/bf01191617)
- **[SOTA]** Y.-Y. Li. *Prescribing scalar curvature on $S^n$ and related problems, Part I.* Journal of Differential Equations 120 (1995), 319–410; *Part II: existence and compactness.* Communications on Pure and Applied Mathematics 49 (1996), 541–597.
- **[SOTA]** C.-C. Chen, C.-S. Lin. *Estimates of the conformal scalar curvature equation via the method of moving planes.* Communications on Pure and Applied Mathematics 50 (1997), 971–1017. [DOI](https://doi.org/10.1002/(sici)1097-0312(199710)50:10<971::aid-cpa2>3.0.co;2-d)
- **[SOTA]** M. Struwe. *A flow approach to Nirenberg's problem.* Duke Mathematical Journal 128 (2005), 19–64.
- **[Related]** J. Escobar, R. Schoen. *Conformal metrics with prescribed scalar curvature.* Inventiones Mathematicae 86 (1986), 243–254. [DOI](https://doi.org/10.1007/bf01389071)
- **[Related]** W. Chen, W. Ding. *Scalar curvatures on $S^2$.* Transactions of the AMS 303 (1987), 365–382.
- **[Survey]** J. Kazdan. *Prescribing the Curvature of a Riemannian Manifold.* CBMS Regional Conference Series in Mathematics 57, AMS, 1985. [DOI](https://doi.org/10.1090/cbms/057)
- **[Survey]** T. Aubin. *Some Nonlinear Problems in Riemannian Geometry.* Springer Monographs in Mathematics, 1998. [DOI](https://doi.org/10.1007/978-3-662-13006-3)

## 10. Worked Example / Concrete Special Case

**Claim.** For any $\varepsilon \ne 0$ with $|\varepsilon| < 1$, the function $K = 1 + \varepsilon x_3$ on $S^2$ (where $x_3$ is the third coordinate of $S^2 \subset \mathbb{R}^3$) is **not** the Gaussian curvature of any metric conformal to $g_0$ — even though $K > 0$ everywhere and every naive necessary condition (positivity, Gauss–Bonnet sign) is met.

**Step 1 — the identity.** Suppose $u$ solves $-\Delta u + 1 = K e^{2u}$. Multiply by $\langle \nabla x_3, \nabla u\rangle$ and integrate; using that $\nabla x_3$ is a conformal Killing field on $S^2$ with $\mathrm{div}(\nabla x_3) = \Delta x_3 = -2x_3$, one obtains the Kazdan–Warner identity
$$\int_{S^2} \langle \nabla K, \nabla x_3 \rangle\, e^{2u}\, dA = 0 .$$

**Step 2 — evaluate the gradient pairing.** Here $\nabla K = \varepsilon \nabla x_3$, so
$$\langle \nabla K, \nabla x_3\rangle = \varepsilon\, |\nabla x_3|^2 .$$
On $S^2$, $x_3 = \cos\theta$ in polar coordinates about the north pole, so $|\nabla x_3|^2 = \sin^2\theta = 1 - x_3^2$.

**Step 3 — contradiction.** Substituting,
$$0 = \varepsilon \int_{S^2} (1-x_3^2)\, e^{2u}\, dA .$$
The integrand $(1-x_3^2)e^{2u}$ is $\ge 0$ and vanishes only at the two poles (a set of measure zero), so the integral is strictly positive. Hence $\varepsilon = 0$. $\blacksquare$

**Step 4 — the contrast.** Now take $K = 1 + \varepsilon x_3^2$. This is even, so **Moser's theorem applies** and a conformal metric with this curvature exists. Check the identity is consistent: $\nabla K = 2\varepsilon x_3 \nabla x_3$, so
$$\int_{S^2} 2\varepsilon\, x_3 (1-x_3^2)\, e^{2u}\, dA = 0$$
is satisfiable because the factor $x_3$ changes sign — an antipodally symmetric solution $u(-x)=u(x)$ makes the integrand odd and the integral vanish identically.

**Reading.** The two examples differ only in the parity of the perturbation, yet one is obstructed and the other is solvable. This is the whole difficulty in miniature: solvability is governed by the fine interaction between $K$'s critical structure and the three-dimensional space of first spherical harmonics generating the conformal group, and no known invariant captures that interaction in general.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*