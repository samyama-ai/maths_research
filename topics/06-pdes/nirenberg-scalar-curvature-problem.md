---
id: 06-pdes/nirenberg-scalar-curvature-problem
title: "Nirenberg Prescribed Scalar Curvature Problem"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nirenberg Prescribed Scalar Curvature Problem

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/nirenberg-scalar-curvature-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(S^n, g_0)$ be the round sphere of dimension $n \ge 2$ with its standard metric. **Nirenberg's problem** asks:

> Given a smooth function $K : S^n \to \mathbb{R}$, does there exist a metric $g$ **conformal** to $g_0$ whose scalar curvature (Gauss curvature when $n = 2$) equals $K$?

Equivalently: characterize the set
$$\mathcal{K}_n \;=\; \{\, K \in C^\infty(S^n) \;:\; K = R_g \text{ for some } g \in [g_0] \,\},$$
where $[g_0] = \{ e^{2u} g_0 : u \in C^\infty(S^n)\}$ is the conformal class.

A complete solution must give **necessary and sufficient** conditions on $K$. The difficulty is that $\mathcal{K}_n$ is neither open nor closed in any obvious topology, and is genuinely obstructed: $K$ positive everywhere is **not** sufficient. The obstruction is caused by the noncompact conformal group $\mathrm{Conf}(S^n) \cong \mathrm{SO}(n+1,1)$, which makes the variational problem invariant under a noncompact action and produces blow-up.

The same question on a general compact manifold $(M^n,g_0)$ is the **Kazdan–Warner problem**; it is *solved* when the Yamabe invariant is $\le 0$, and $S^n$ is the hardest remaining case.

## 2. Mathematical Foundations

**Case $n \ge 3$.** Write $g = u^{4/(n-2)} g_0$ with $u > 0$. The conformal transformation law for scalar curvature gives the semilinear elliptic PDE
$$-\,\frac{4(n-1)}{n-2}\,\Delta_{g_0} u \;+\; R_{g_0}\, u \;=\; K\, u^{\frac{n+2}{n-2}}, \qquad u > 0 \ \text{ on } S^n,$$
with $R_{g_0} = n(n-1)$. The exponent $\frac{n+2}{n-2}$ is the **critical Sobolev exponent**: $H^1(S^n) \hookrightarrow L^{2n/(n-2)}(S^n)$ is continuous but *not compact*.

**Case $n = 2$.** With $g = e^{2u} g_0$ and $K_{g_0} = 1$,
$$-\Delta_{g_0} u + 1 = K e^{2u}.$$
Gauss–Bonnet forces $\int_{S^2} K e^{2u}\, dV_{g_0} = 4\pi$, so $K$ must be positive somewhere.

**Variational structure.** For $n \ge 3$ solutions are critical points of
$$J_K(u) \;=\; \frac{\int_{S^n}\big(\tfrac{4(n-1)}{n-2}|\nabla u|^2 + R_{g_0}u^2\big) dV_{g_0}}{\Big(\int_{S^n} K\, |u|^{\frac{2n}{n-2}} dV_{g_0}\Big)^{\frac{n-2}{n}}},$$
restricted to $\int K u^{2n/(n-2)} > 0$. Palais–Smale sequences fail to be compact: by the Struwe decomposition they split into a weak limit plus finitely many **bubbles**, rescaled copies of the Aubin–Talenti instanton
$$U_\lambda(x) = \Big(\tfrac{\lambda}{1+\lambda^2|x|^2}\Big)^{\frac{n-2}{2}} \quad\text{on } \mathbb{R}^n \ (\text{after stereographic projection}),$$
each carrying energy $S_n = n(n-1)\,\omega_n^{2/n}$, $\omega_n = |S^n|$.

**Kazdan–Warner obstruction.** If $u$ solves the equation, then for each ambient coordinate function $x_j$ ($j = 1,\dots,n+1$), restricted to $S^n \subset \mathbb{R}^{n+1}$,
$$\int_{S^n} \langle \nabla K, \nabla x_j\rangle_{g_0}\; u^{\frac{2n}{n-2}} \, dV_{g_0} = 0 \qquad (n\ge 3), \qquad \int_{S^2} \langle \nabla K, \nabla x_j\rangle\, e^{2u}\, dV_{g_0} = 0.$$
The functions $x_j$ are the first spherical harmonics, $\Delta_{g_0} x_j = -n x_j$; they generate the conformal vector fields. This identity (Kazdan–Warner 1974; conformal-field version, Bourguignon–Ezin 1987) rules out all monotone $K$, e.g. $K = 2 + x_{n+1}$.

## 3. History & State of the Art (SOTA)

- **1974–75.** Kazdan and Warner classify prescribed curvature on compact $M^n$ by the sign of the Yamabe invariant, and discover the obstruction identity on $S^n$.
- **1973/1971.** Moser proves: on $S^2$, every positive $K$ **even** under the antipodal map $x \mapsto -x$ is attained. Symmetry restores compactness by halving the critical Moser–Trudinger constant.
- **1986.** Escobar–Schoen treat $n\ge 3$, giving existence for $K$ close to constant and for locally conformally flat manifolds.
- **1987–88.** Chang–Yang give the first genuinely nonperturbative Morse-theoretic criterion on $S^2$, later extended to $S^3$ (Chang–Gursky–Yang, 1993).
- **1991.** Bahri–Coron develop the "critical points at infinity" theory, giving a topological existence result on $S^3$.
- **1995–96.** Y.Y. Li proves sharp blow-up estimates and a general degree-counting theorem for all $n \ge 3$ under a **flatness condition** of order $\beta \in (n-2, n)$ at critical points of $K$.
- **1996.** Schoen–Zhang prove existence on $S^3$ for $K$ with nondegenerate critical points and an index condition, via a Pohozaev-type analysis.
- **2000s.** Ambrosetti–Malchiodi, Chen–Lin, and Malchiodi–Struwe develop perturbative and finite-dimensional-reduction techniques; the $Q$-curvature and fractional analogues appear.
- **Status.** No characterization of $\mathcal{K}_n$ is known for any $n \ge 2$. Sufficient conditions (index counts, flatness, symmetry) and necessary conditions (Kazdan–Warner) do not meet.

## 4. Partial Results / Verified Cases

- **Non-spherical base, $Y(M,[g_0]) \le 0$:** completely solved (Kazdan–Warner 1975; Escobar–Schoen 1986). If $Y < 0$, $K$ is attained iff $K < 0$ somewhere and a further integral condition holds; if $Y = 0$, iff $K \equiv 0$ or $K$ changes sign with $\int_M K\, dV_{g_0} < 0$.
- **$S^2$, antipodally symmetric $K > 0$:** always solvable (Moser).
- **$S^2$, Chang–Yang criterion:** if $K > 0$ is Morse with $\Delta K \ne 0$ at every critical point and
  $$\sum_{\{\nabla K(q) = 0,\ \Delta K(q) < 0\}} (-1)^{\mathrm{ind}(q)} \;\ne\; 1,$$
  then $K \in \mathcal{K}_2$. Example: $K$ with exactly two local maxima and one saddle, all with $\Delta K<0$, gives count $2 - 1$… index arithmetic must be checked per case, but the criterion is verifiable in finitely many evaluations.
- **$S^3$:** Bahri–Coron (1991), Chang–Gursky–Yang (1993), Schoen–Zhang (1996) — existence for positive Morse $K$ with $\Delta K \ne 0$ at critical points under an analogous index count.
- **$S^n$, all $n \ge 3$, flatness order $\beta \in (n-2,n)$:** Y.Y. Li's theorem. If near each critical point $q$, in suitable coordinates,
  $$K(y) = K(q) + \sum_{i=1}^n b_i |y_i|^\beta + \text{lower order}, \qquad \sum_i b_i \ne 0,\ b_i \ne 0,$$
  then a Leray–Schauder degree is computable and nonvanishing degree gives existence.
- **Perturbative regime:** $K = 1 + \varepsilon h$ with $\varepsilon$ small — solvable iff $h$ satisfies a nondegenerate critical point condition for the reduced Melnikov-type function (Ambrosetti–Malchiodi).
- **Rotationally symmetric $K$ on $S^n$:** reduces to an ODE; existence characterized by explicit sign conditions (Chen–Lin and others).

## 5. Principal Obstacles

- **Critical exponent / lack of compactness.** The Sobolev embedding at exponent $2n/(n-2)$ is noncompact, so minimizing sequences can concentrate at a point and converge to a bubble carrying all the energy. Direct methods, mountain-pass, and standard Ljusternik–Schnirelmann all fail without extra structure.
- **Noncompact symmetry group.** $\mathrm{Conf}(S^n)$ is noncompact; when $K \equiv \text{const}$ the solution set is an entire $(n+1)$-dimensional noncompact family. Any $K$ is a perturbation of this degenerate situation, and the degeneracy is exactly the source of the Kazdan–Warner identity.
- **Obstruction is not a characterization.** The Kazdan–Warner conditions are necessary but far from sufficient; there is no known finite list of invariants of $K$ that decides membership in $\mathcal{K}_n$.
- **Blow-up with unbounded multiplicity.** For $n \ge 4$ the flatness order $\beta$ controls whether a single bubble or multiple bubbles form; when $\beta \ge n$ (very flat $K$) or $\beta \le n-2$ (sharp peaks) the known a priori estimates break, and degree theory has no compactness to run on.
- **Non-Morse and degenerate $K$.** Every general theorem assumes $\Delta K \ne 0$ at critical points or a flatness hypothesis. For $K$ with a critical manifold, or with $\Delta K = 0$ at a critical point, the reduced finite-dimensional problem is degenerate and no substitute Morse theory exists.
- **Sign-changing $K$.** When $K$ changes sign the functional is not bounded below on the natural constraint and the Pohozaev identities lose their sign, so almost nothing beyond special symmetry is known for $n \ge 4$.

## 6. The Gap

Section 4 supplies **sufficient** conditions of the form "positive $K$, nondegenerate in a prescribed sense, plus a nonzero index/degree count". Section 1 asks for an **iff**. The gap has three concrete edges:

1. **Degenerate $K$.** No criterion exists when $\Delta K$ vanishes at a critical point, or when $K$ is merely continuous. This is not a technicality: the degree formula depends discontinuously on the local model of $K$ near its critical set.
2. **The vanishing-degree case.** When the index count *equals* the excluded value, the degree is zero and both existence and nonexistence occur among such $K$. Distinguishing them requires an invariant finer than degree — none is known.
3. **Necessity.** Nobody has produced a nonexistence mechanism beyond Kazdan–Warner and its refinements. Whether Kazdan–Warner-type identities plus a topological condition are *jointly* necessary and sufficient is entirely open, even for $n = 2$.

## 7. Current Research (as of June 2026)

- **Fractional and higher-order analogues.** Prescribing $Q$-curvature (the Paneitz operator, $n \ge 4$) and fractional scalar curvature for $(-\Delta)^s$ on $S^n$; blow-up analysis mirrors the classical case but positivity of Green's functions is the new obstacle. Active at Princeton, Rutgers, SISSA, and Chinese Academy of Sciences groups.
- **Sharp blow-up analysis at critical flatness.** Attempts to push Y.Y. Li's degree theory to $\beta = n-2$ and $\beta \ge n$ using refined Pohozaev identities and non-radial expansions of bubbles. *(frontier — verify)*
- **Multi-bubble gluing.** Lyapunov–Schmidt constructions producing solutions with prescribed numbers of concentration points at prescribed critical points of $K$; these give existence results *not* covered by any single degree formula.
- **Compactness of the full solution set.** Whether the set of solutions for fixed generic $K$ is compact in $C^2$ — related to the (now known to fail in high dimension) compactness of the Yamabe problem solution set after Brendle and Brendle–Marques. *(frontier — verify)*
- **Sign-changing and boundary versions.** Prescribed scalar curvature on manifolds with boundary (with prescribed mean curvature), and on non-compact and singular spaces.

## 8. Future Work

- Find a **nonexistence mechanism** independent of Kazdan–Warner — e.g. a degree/homotopy obstruction visible only through the topology of $\{K > c\}$ sublevel sets.
- Build a Morse theory for the functional *at infinity* that is valid without flatness hypotheses, extending Bahri–Coron's "critical points at infinity" to arbitrary $C^2$ data.
- Settle the $n = 2$ case first: characterize $\mathcal{K}_2$ for positive Morse $K$ where the Chang–Yang count is exactly $1$.
- Develop a stable-under-perturbation invariant of $K$ (a "conformal Morse index") whose nonvanishing is both necessary and sufficient in a dense class.
- Extend the complete Kazdan–Warner classification (Yamabe invariant $\le 0$) to a full classification for all positive-Yamabe manifolds other than $S^n$, where partial compactness is available.

## 9. Key References

- **[Foundational]** J. L. Kazdan and F. W. Warner. *Curvature functions for compact 2-manifolds.* Annals of Mathematics, 99 (1974), 14–47.
- **[Foundational]** J. L. Kazdan and F. W. Warner. *Scalar curvature and conformal deformation of Riemannian structure.* Journal of Differential Geometry, 10 (1975), 113–134.
- **[Foundational]** J. Moser. *On a nonlinear problem in differential geometry.* In *Dynamical Systems* (M. Peixoto, ed.), Academic Press, 1973, 273–280.
- **[Foundational]** J. F. Escobar and R. M. Schoen. *Conformal metrics with prescribed scalar curvature.* Inventiones Mathematicae, 86 (1986), 243–254.
- **[Foundational]** J.-P. Bourguignon and J.-P. Ezin. *Scalar curvature functions in a conformal class of metrics and conformal transformations.* Transactions of the American Mathematical Society, 301 (1987), 723–736.
- **[SOTA]** S.-Y. A. Chang and P. C. Yang. *Prescribing Gaussian curvature on $S^2$.* Acta Mathematica, 159 (1987), 215–259.
- **[SOTA]** S.-Y. A. Chang and P. C. Yang. *Conformal deformation of metrics on $S^2$.* Journal of Differential Geometry, 27 (1988), 259–296.
- **[SOTA]** A. Bahri and J.-M. Coron. *The scalar-curvature problem on the standard three-dimensional sphere.* Journal of Functional Analysis, 95 (1991), 106–172.
- **[SOTA]** S.-Y. A. Chang, M. J. Gursky and P. C. Yang. *The scalar curvature equation on 2- and 3-spheres.* Calculus of Variations and PDE, 1 (1993), 205–229.
- **[SOTA]** Y. Y. Li. *Prescribing scalar curvature on $S^n$ and related problems, Part I.* Journal of Differential Equations, 120 (1995), 319–410.
- **[SOTA]** Y. Y. Li. *Prescribing scalar curvature on $S^n$ and related problems, Part II: existence and compactness.* Communications on Pure and Applied Mathematics, 49 (1996), 541–597.
- **[SOTA]** R. Schoen and D. Zhang. *Prescribed scalar curvature on the $n$-sphere.* Calculus of Variations and PDE, 4 (1996), 1–25.
- **[Survey]** T. Aubin. *Some Nonlinear Problems in Riemannian Geometry.* Springer Monographs in Mathematics, Springer, 1998.
- **[Survey]** A. Ambrosetti and A. Malchiodi. *Perturbation Methods and Semilinear Elliptic Problems on $\mathbb{R}^n$.* Progress in Mathematics 240, Birkhäuser, 2006.
- **[Survey]** S.-Y. A. Chang. *Non-linear Elliptic Equations in Conformal Geometry.* Zurich Lectures in Advanced Mathematics, European Mathematical Society, 2004.

## 10. Worked Example / Concrete Special Case

**Claim.** On $S^2 \subset \mathbb{R}^3$ with coordinates $(x_1,x_2,x_3)$, the smooth, strictly positive function
$$K(x) = 2 + x_3$$
is **not** the Gauss curvature of any metric conformal to $g_0$.

*Proof.* Suppose $-\Delta_{g_0} u + 1 = K e^{2u}$ has a solution $u$. Apply the Kazdan–Warner identity with $j = 3$:
$$\int_{S^2} \langle \nabla K, \nabla x_3 \rangle_{g_0}\, e^{2u}\, dV_{g_0} = 0.$$
Since $K = 2 + x_3$, we have $\nabla K = \nabla x_3$, hence the integrand is $|\nabla_{g_0} x_3|^2 e^{2u}$.

Compute $|\nabla_{g_0} x_3|^2$. In spherical coordinates $x_3 = \cos\theta$, and $|\nabla_{g_0} f|^2 = (\partial_\theta f)^2 + \sin^{-2}\theta\,(\partial_\varphi f)^2$, so
$$|\nabla_{g_0} x_3|^2 = \sin^2\theta = 1 - x_3^2 .$$
Therefore
$$0 = \int_{S^2} (1 - x_3^2)\, e^{2u}\, dV_{g_0}.$$
But $1 - x_3^2 \ge 0$, vanishing only on the two poles (a measure-zero set), and $e^{2u} > 0$ everywhere. So the integral is **strictly positive** — contradiction. $\square$

**What this shows.** $K = 2 + x_3$ is smooth, strictly positive ($1 \le K \le 3$), and arbitrarily close to the constant $2$ after rescaling the perturbation ($K_\varepsilon = 2 + \varepsilon x_3$ fails for every $\varepsilon \neq 0$). So positivity of $K$ is far from sufficient, and $\mathcal{K}_2$ has empty interior around no-constant directions of first-spherical-harmonic type.

**Contrast with a solvable case.** Take $K(x) = 2 + x_3^2$. Now $\nabla K = 2x_3 \nabla x_3$ and the identity for $j=3$ reads $\int 2x_3(1-x_3^2)e^{2u} = 0$, which is *not* violated automatically — indeed $K$ is antipodally symmetric ($K(-x) = K(x)$) and positive, so Moser's theorem gives an antipodally symmetric solution $u$. The two examples differ only by the parity of the perturbation: **odd** first-harmonic content is obstructed, **even** content is not. Quantifying the space between these two extremes is exactly the open part of the Nirenberg problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*