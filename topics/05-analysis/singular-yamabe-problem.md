---
id: 05-analysis/singular-yamabe-problem
title: "Singular Yamabe Problem"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Singular Yamabe Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/singular-yamabe-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M^n, g)$ be a smooth compact Riemannian manifold, $n \ge 3$, and let $\Lambda \subsetneq M$ be a closed subset. The **singular Yamabe problem** asks:

> For which $\Lambda$ does there exist a metric $\tilde g$, conformal to $g$ on $M \setminus \Lambda$, which is **complete** on $M \setminus \Lambda$ and has **constant scalar curvature** $R_{\tilde g} \equiv \varepsilon\, n(n-1)$ with $\varepsilon \in \{-1, 0, +1\}$?

Writing $\tilde g = u^{4/(n-2)} g$ with $u > 0$ on $M \setminus \Lambda$, this is the question of existence of a positive solution to a semilinear elliptic PDE that blows up at $\Lambda$ fast enough to make the metric complete.

The problem splits sharply by sign:

- **Negative case ($\varepsilon = -1$).** Essentially settled: existence holds iff $\Lambda$ is "large enough" in a capacity sense; solutions are unique. The remaining open questions are about **regularity** — the precise boundary expansion of $u$ and the vanishing of a local obstruction.
- **Positive case ($\varepsilon = +1$).** Open. Only necessary conditions ($\dim_{\mathcal H} \Lambda \le (n-2)/2$) and constructions for special $\Lambda$ are known.

A complete solution would give a necessary-and-sufficient geometric/measure-theoretic characterization of admissible $\Lambda$ in each sign class, together with the structure of the moduli space of solutions.

## 2. Mathematical Foundations

**Conformal transformation of scalar curvature.** For $\tilde g = u^{4/(n-2)} g$, $u>0$,
$$
R_{\tilde g} \;=\; u^{-\frac{n+2}{n-2}}\left(-\,\frac{4(n-1)}{n-2}\,\Delta_g u \;+\; R_g\, u\right).
$$
Set $c_n = \frac{4(n-1)}{n-2}$ and $p = \frac{n+2}{n-2}$ (the critical Sobolev exponent, $p+1 = \frac{2n}{n-2}$). The **singular Yamabe equation** is
$$
-\,c_n \Delta_g u + R_g u \;=\; \varepsilon\, n(n-1)\, u^{p} \quad \text{on } M \setminus \Lambda, \qquad u > 0,
$$
subject to the **completeness condition** $u(x) \to \infty$ as $\operatorname{dist}_g(x,\Lambda) \to 0$ at a rate making $\int_\gamma u^{2/(n-2)} \, ds = \infty$ for every curve $\gamma$ reaching $\Lambda$.

**Model asymptotics.** If $\Lambda$ is a smooth submanifold of dimension $k$ and $d(x) = \operatorname{dist}_g(x,\Lambda)$, the leading behaviour compatible with the equation is
$$
u(x) \;\sim\; A_{n,k}\, d(x)^{-\frac{n-2}{2}}\ (\varepsilon=-1), \qquad u(x) \;\sim\; A_{n,k}\, d(x)^{-\frac{n-k-2}{2}}\ (\varepsilon=+1).
$$
The first requires $\frac{n-2}{2} > k$-independent balance; the second requires $k < \frac{n-2}{2}$ for the exponent to be positive. This exponent dichotomy at $k = \frac{n-2}{2}$ is the fundamental dimensional threshold of the subject.

**Negative case, $\Lambda = \partial\Omega$ (Loewner–Nirenberg problem).** For $\Omega \Subset \mathbb{R}^n$ with smooth boundary and $g = \delta$, the equation reduces to
$$
\Delta u \;=\; \tfrac{n(n-2)}{4}\, u^{\frac{n+2}{n-2}} \ \text{ in } \Omega, \qquad u \to +\infty \text{ on } \partial\Omega.
$$
Existence and uniqueness follow from sub/supersolution barriers plus the Keller–Osserman bound. The solution is polyhomogeneous: with $\rho$ a defining function for $\partial\Omega$,
$$
u \;=\; \rho^{-\frac{n-2}{2}}\Big(\sum_{j=0}^{n-1} u_j\,\rho^{\,j} \;+\; \mathcal{B}_{\partial\Omega}\,\rho^{\,n}\log\rho \;+\; O(\rho^n)\Big),
$$
where $u_0 = 1$, the $u_j$ for $j < n$ are universal local expressions in the second fundamental form and ambient curvature, and $\mathcal{B}_{\partial\Omega}$ is the **Andersson–Chruściel–Friedrich (ACF) obstruction** — a scalar local invariant of the embedding $\partial\Omega \hookrightarrow M$, conformally invariant of weight $-n$.

**Capacity.** For $s>0$, $q>1$, the Bessel capacity $C_{s,q}$ is defined by $C_{s,q}(E) = \inf\{\|f\|_{L^q}^q : G_s * f \ge 1 \text{ on } E,\ f\ge0\}$, $G_s$ the Bessel kernel. The relevant exponent for the critical equation is $q' = \frac{p}{p-1} = \frac{n+2}{4}$, giving $C_{2,\,(n+2)/4}$.

## 3. History & State of the Art (SOTA)

- **1974 — Loewner & Nirenberg.** In *Contributions to Analysis*, they solve the negative case on $S^n$ (equivalently domains in $\mathbb{R}^n$) for $\Lambda$ a smooth closed submanifold of dimension $k$, and prove the sharp dichotomy: a complete conformal metric with $R \equiv -n(n-1)$ exists **iff** $k > \frac{n-2}{2}$. Uniqueness follows from the maximum principle.
- **1988 — Aviles & McOwen.** (Duke Math. J. 56) Extend existence to arbitrary compact $(M^n,g)$ and $\Lambda$ a smooth closed submanifold with $\dim \Lambda > \frac{n-2}{2}$, with no assumption on the sign of $R_g$.
- **1988 — Schoen & Yau.** (Invent. Math. 92) Prove the fundamental **necessary condition** in the positive case: if $\tilde g$ is a complete conformal metric on $S^n \setminus \Lambda$ with $R_{\tilde g} > 0$, then $\dim_{\mathcal H} \Lambda \le \frac{n-2}{2}$. The proof uses the developing map and positive mass.
- **1988 — Schoen.** (CPAM 41) Constructs solutions in the positive case for $\Lambda$ a finite set of $\ge 2$ points in $S^n$, and for limit sets of certain Kleinian groups, by a gluing/Lyapunov–Schmidt argument on Delaunay ends.
- **1991 — Mazzeo.** Introduces the **edge calculus** and proves polyhomogeneous regularity of Loewner–Nirenberg solutions along smooth $\Lambda$.
- **1992 — Andersson, Chruściel & Friedrich.** (CMP 149) Discover the log obstruction $\mathcal{B}$ in the boundary expansion; motivation was smooth hyperboloidal initial data in general relativity.
- **1996–1999 — Mazzeo, Pacard, Pollack, Uhlenbeck, Korevaar, Schoen.** Positive-case constructions for $\Lambda$ a union of smooth submanifolds of dimensions $k_i \in (0, \frac{n-2}{2})$; the moduli space of solutions with $k$ isolated singularities on $S^n$ is a locally real-analytic set of dimension $k$; refined asymptotics show every isolated singularity is asymptotically **Delaunay**.
- **2003 — Labutin.** Gives a Wiener-type criterion: solvability of the negative singular Yamabe problem for a general closed $\Lambda$ is governed by the Bessel capacity $C_{2,\,(n+2)/4}$ of $\Lambda$ at every scale — effectively closing the existence question in the negative case.
- **2017–2021 — Graham, Gover & Waldron.** Show $\mathcal{B}_\Sigma$ is the variational gradient of the renormalized volume energy of the singular Yamabe metric, and equals the Willmore invariant when $n=3$. This turns "when does the obstruction vanish?" into a conformal hypersurface geometry question.

## 4. Partial Results / Verified Cases

| Case | Result | Status |
|---|---|---|
| $\varepsilon=-1$, $\Lambda$ smooth submanifold, $\dim\Lambda = k$ | Exists and is unique iff $k > \frac{n-2}{2}$ (Loewner–Nirenberg; Aviles–McOwen) | Solved |
| $\varepsilon=-1$, $\Lambda$ general closed set | Capacity criterion $C_{2,(n+2)/4}$ (Labutin) | Solved |
| $\varepsilon=-1$, $\Lambda = \partial\Omega$ smooth | $u$ polyhomogeneous; smooth to order $n-1$; $\rho^n\log\rho$ term with coefficient $\mathcal{B}$ | Solved |
| $\varepsilon=-1$, $\Lambda=\partial\Omega$ Lipschitz/conic | Optimal expansions in domains with corners and conic singularities (Han–Shen, JFA 2020) | Partial |
| $\varepsilon=+1$, $\Lambda$ = 1 point | **No** solution: singularity is removable (Caffarelli–Gidas–Spruck; Schoen–Yau) | Solved |
| $\varepsilon=+1$, $\Lambda$ = 2 points on $S^n$ | Exactly the 1-parameter Delaunay family on $\mathbb{R}\times S^{n-1}$ | Solved |
| $\varepsilon=+1$, $\Lambda$ finite, $\\#\Lambda \ge 2$ | Solutions exist (Schoen 1988); moduli space is $\\#\Lambda$-dimensional (Mazzeo–Pollack–Uhlenbeck) | Solved |
| $\varepsilon=+1$, $\Lambda = \bigsqcup \Lambda_i$ smooth, $0 < \dim\Lambda_i < \frac{n-2}{2}$ | Existence (Mazzeo–Pacard, JDG 1996) | Solved |
| $\varepsilon=+1$, $\Lambda$ a Kleinian limit set with $\dim_{\mathcal H}\Lambda < \frac{n-2}{2}$ | Existence via Schoen–Yau developing map | Solved |
| $\varepsilon=+1$, $\Lambda$ general with $\dim_{\mathcal H}\Lambda \le \frac{n-2}{2}$ | **Open** | Open |
| $\varepsilon=0$ | Reduces to $\Delta_g u = $ (linear) — solvable only in restricted flat settings | Mostly understood |

Dimension $n=3$: threshold $\frac{n-2}{2} = \frac12$, so positive-case singular sets must have Hausdorff dimension $\le 1/2$ — only Cantor-type sets and points. Dimension $n=4$: threshold $1$, curves are exactly borderline.

## 5. Principal Obstacles

- **No variational structure in the positive case.** For $\varepsilon = -1$ the nonlinearity $u^p$ has the sign that makes sub/supersolutions and the maximum principle work: comparison gives both existence and uniqueness in one stroke. For $\varepsilon = +1$ the sign reverses, the maximum principle gives nothing, and the energy functional $\int |\nabla u|^2 - \int u^{p+1}$ is unbounded below with critical exponent — the Palais–Smale condition fails at exactly the concentration scale generated by the singular set.
- **Gluing methods need model geometry.** All positive-case constructions (Schoen; Mazzeo–Pacard; KMPS) attach explicit Delaunay or Fowler ends to a smooth model. This requires $\Lambda$ to be a smooth submanifold, or a set with a uniformly self-similar structure. There is no known end model for a generic compact set of dimension $\le \frac{n-2}{2}$.
- **Edge calculus assumes regularity of $\Lambda$.** Mazzeo's elliptic theory of differential edge operators produces polyhomogeneity precisely because the singular set carries a fibration structure. For rough $\Lambda$, the linearized operator is not edge-elliptic and its indicial roots are not defined.
- **Capacity is not conformally natural in the positive case.** Labutin's criterion works because in the negative case the equation obeys a comparison principle that converts existence into a potential-theoretic thinness test. No analogue exists when solutions must be constructed rather than compared.
- **The log obstruction is a genuine local invariant.** $\mathcal{B}_\Sigma$ is not removable by choice of defining function; it caps the regularity of the negative-case solution at $C^{n-1,\alpha}$ in general, and computing it in dimension $n \ge 5$ requires long conformal-invariant computations that resist closed form.

## 6. The Gap

Two precise gaps remain.

1. **Positive case, sufficiency.** Schoen–Yau prove $\dim_{\mathcal H}\Lambda \le \frac{n-2}{2}$ is **necessary**. Constructions prove existence for $\Lambda$ a finite union of smooth submanifolds of dimension $< \frac{n-2}{2}$, and for Kleinian limit sets. The gap is everything in between: is there a capacity- or Minkowski-content criterion, analogous to Labutin's $C_{2,(n+2)/4}$ criterion in the negative case, that is both necessary and sufficient? Even the borderline smooth case $\dim\Lambda = \frac{n-2}{2}$ exactly (e.g. curves in $n=4$) is not resolved.
2. **Negative case, obstruction.** Characterize the hypersurfaces $\Sigma^{n-1} \subset M^n$ with $\mathcal{B}_\Sigma \equiv 0$, i.e. those for which the singular Yamabe metric is smooth (conormally) to all orders. Umbilic $\Sigma$ give $\mathcal{B}=0$; for $n=3$, $\mathcal{B}=0$ iff $\Sigma$ is Willmore. **Conjecture:** for $n \ge 4$, $\mathcal{B}_\Sigma \equiv 0$ characterizes a nontrivial "higher Willmore" class, and $\mathcal{B}$ is never identically zero for a generic embedding.

## 7. Current Research (as of June 2026)

- **Conformal hypersurface geometry (Gover–Waldron, Auckland/UC Davis; Graham, Washington).** Tractor-calculus machinery computes the singular Yamabe obstruction $\mathcal{B}$ and the associated renormalized volume anomaly in fixed low dimensions. Explicit formulas are known through $n=5$; $n=6$ is being pushed *(frontier — verify)*.
- **Low-regularity Loewner–Nirenberg (Han, Notre Dame; Shen, Jiang; Jin & Xiong, HKUST/Peking).** Sharp boundary expansions and optimal regularity in domains with corners, edges and conic points, and for singular sets that are not submanifolds. This is the most active direction with concrete recent output.
- **Fractal singular sets in the positive case.** Extending Schoen–Yau/Kleinian constructions to self-similar $\Lambda$ of dimension close to $\frac{n-2}{2}$ using thermodynamic-formalism estimates on limit sets *(frontier — verify)*.
- **Relativity applications.** Hyperboloidal initial data and conformal compactification of asymptotically flat spacetimes continue to drive the obstruction question (Chruściel and collaborators, Vienna).
- **Fully nonlinear analogues.** Singular $\sigma_k$-Yamabe problems (Gonzalez, Li, Nguyen) where $\sigma_k(A_g) = $ const; the Schoen–Yau dimension bound has $\sigma_k$-analogues but the existence theory is far thinner.

## 8. Future Work

- Develop a **capacity theory adapted to the critical nonlinearity with the wrong sign**, replacing comparison principles with a concentration-compactness bookkeeping keyed to $\Lambda$.
- Prove or disprove existence in the **borderline smooth case** $\dim \Lambda = \frac{n-2}{2}$; this would fix whether Schoen–Yau's bound is attained.
- Classify **complete positive-scalar-curvature conformal metrics on $S^n\setminus\Lambda$ with $\Lambda$ a Cantor set** of prescribed dimension — the simplest non-manifold test case.
- Give a **closed-form or recursive formula for $\mathcal{B}_\Sigma$ in all dimensions**, ideally as the Euler–Lagrange operator of an explicit energy, generalizing Willmore.
- Extend **moduli-space theory** (Mazzeo–Pollack–Uhlenbeck) from isolated points to positive-dimensional singular sets: is the space of Mazzeo–Pacard solutions a manifold, and what is its dimension?

## 9. Key References

- **[Foundational]** C. Loewner, L. Nirenberg. *Partial differential equations invariant under conformal or projective transformations.* In: Contributions to Analysis, Academic Press, 1974, pp. 245–272.
- **[Foundational]** P. Aviles, R. McOwen. *Complete conformal metrics with negative scalar curvature in compact Riemannian manifolds.* Duke Mathematical Journal 56 (1988), 395–398. [DOI](https://doi.org/10.1215/s0012-7094-88-05616-5)
- **[Foundational]** R. Schoen, S.-T. Yau. *Conformally flat manifolds, Kleinian groups and scalar curvature.* Inventiones Mathematicae 92 (1988), 47–71. [DOI](https://doi.org/10.1007/bf01393992)
- **[Foundational]** R. Schoen. *The existence of weak solutions with prescribed singular behavior for a conformally invariant scalar equation.* Communications on Pure and Applied Mathematics 41 (1988), 317–392. [DOI](https://doi.org/10.1002/cpa.3160410305)
- **[Foundational]** L. Caffarelli, B. Gidas, J. Spruck. *Asymptotic symmetry and local behavior of semilinear elliptic equations with critical Sobolev growth.* Communications on Pure and Applied Mathematics 42 (1989), 271–297. [DOI](https://doi.org/10.1002/cpa.3160420304)
- **[Foundational]** R. Mazzeo. *Regularity for the singular Yamabe problem.* Indiana University Mathematics Journal 40 (1991), 1277–1299.
- **[Foundational]** L. Andersson, P. T. Chruściel, H. Friedrich. *On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einstein's field equations.* Communications in Mathematical Physics 149 (1992), 587–612. [DOI](https://doi.org/10.1007/bf02096944)
- **[SOTA]** R. Mazzeo, F. Pacard. *A construction of singular solutions for a semilinear elliptic equation using asymptotic analysis.* Journal of Differential Geometry 44 (1996), 331–370. [DOI](https://doi.org/10.4310/jdg/1214458975)
- **[SOTA]** R. Mazzeo, D. Pollack, K. Uhlenbeck. *Moduli spaces of singular Yamabe metrics.* Journal of the American Mathematical Society 9 (1996), 303–344. [DOI](https://doi.org/10.1090/s0894-0347-96-00208-1)
- **[SOTA]** R. Mazzeo, F. Pacard. *Constant scalar curvature metrics with isolated singularities.* Duke Mathematical Journal 99 (1999), 353–418. [DOI](https://doi.org/10.1215/s0012-7094-99-09913-1)
- **[SOTA]** N. Korevaar, R. Mazzeo, F. Pacard, R. Schoen. *Refined asymptotics for constant scalar curvature metrics with isolated singularities.* Inventiones Mathematicae 135 (1999), 233–272. [DOI](https://doi.org/10.1007/s002220050285)
- **[SOTA]** D. A. Labutin. *Wiener regularity for large solutions of nonlinear equations.* Arkiv för Matematik 41 (2003), 307–339. [DOI](https://doi.org/10.1007/bf02390818)
- **[SOTA / Recent]** C. R. Graham. *Volume renormalization for singular Yamabe metrics.* Proceedings of the American Mathematical Society 145 (2017), 1781–1792. [DOI](https://doi.org/10.1090/proc/13530)
- **[SOTA / Recent]** A. R. Gover, A. Waldron. *Conformal hypersurface geometry via a boundary Loewner–Nirenberg–Yamabe problem.* Communications in Contemporary Mathematics 23 (2021). [DOI](https://doi.org/10.4310/cag.2021.v29.n4.a2)
- **[SOTA / Recent]** Q. Han, W. Shen. *The Loewner–Nirenberg problem in singular domains.* Journal of Functional Analysis 279 (2020), 108604. [DOI](https://doi.org/10.1016/j.jfa.2020.108604)
- **[Survey]** R. Mazzeo. *Elliptic theory of differential edge operators I.* Communications in Partial Differential Equations 16 (1991), 1615–1664. [DOI](https://doi.org/10.1080/03605309108820815)
- **[Survey]** J. M. Lee, T. H. Parker. *The Yamabe problem.* Bulletin of the American Mathematical Society 17 (1987), 37–91.

## 10. Worked Example / Concrete Special Case

**The unit ball: an exact Loewner–Nirenberg solution.**

Take $M = \mathbb{R}^n$ with $g = \delta$, $\Omega = B_1(0)$, $\Lambda = \partial B_1 = S^{n-1}$. We seek $\tilde g = u^{4/(n-2)}\delta$, complete on $B_1$, with $R_{\tilde g} = -n(n-1)$. With $c_n = \frac{4(n-1)}{n-2}$ and $R_\delta = 0$, the equation becomes
$$
\Delta u \;=\; \frac{n(n-2)}{4}\, u^{\frac{n+2}{n-2}}, \qquad u>0 \text{ in } B_1, \quad u\to\infty \text{ on } \partial B_1.
$$

**Ansatz.** The hyperbolic metric on the ball, $g_{\mathrm{hyp}} = \frac{4}{(1-|x|^2)^2}\,\delta$, has $R = -n(n-1)$. Matching $u^{4/(n-2)} = \frac{4}{(1-r^2)^2}$ with $r=|x|$ gives
$$
u(x) \;=\; \left(\frac{2}{1-r^2}\right)^{\frac{n-2}{2}} \;=\; c\,(1-r^2)^{-\alpha}, \qquad \alpha=\tfrac{n-2}{2},\ \ c = 2^{\alpha}.
$$

**Verification.** With $u = c(1-r^2)^{-\alpha}$,
$$
u' = 2c\alpha\, r\,(1-r^2)^{-\alpha-1},\qquad
u'' = 2c\alpha (1-r^2)^{-\alpha-1} + 4c\alpha(\alpha+1) r^2 (1-r^2)^{-\alpha-2}.
$$
Then, using $\Delta u = u'' + \frac{n-1}{r}u'$,
$$
\Delta u = (1-r^2)^{-\alpha-2}\Big[\,2c\alpha n\,(1-r^2) + 4c\alpha(\alpha+1) r^2\Big]
= 2c\alpha\,(1-r^2)^{-\alpha-2}\Big[\,n + r^2\big(2\alpha+2-n\big)\Big].
$$
Since $2\alpha = n-2$, the bracket's $r^2$ coefficient is $2\alpha+2-n = 0$, so
$$
\Delta u \;=\; 2c\alpha n\,(1-r^2)^{-\alpha-2} \;=\; c\,n(n-2)\,(1-r^2)^{-\frac{n+2}{2}}.
$$
On the right-hand side, $\alpha p = \frac{n-2}{2}\cdot\frac{n+2}{n-2} = \frac{n+2}{2} = \alpha+2$, so
$$
\frac{n(n-2)}{4}u^{p} = \frac{n(n-2)}{4}\,c^{p}\,(1-r^2)^{-\frac{n+2}{2}}.
$$
Equality holds iff $c\,n(n-2) = \frac{n(n-2)}{4}c^{p}$, i.e. $c^{\,p-1} = 4$. And $p-1 = \frac{4}{n-2}$, so $c^{\,p-1} = \big(2^{(n-2)/2}\big)^{4/(n-2)} = 2^2 = 4$. ✔

**Reading off the geometry.** Let $d = 1-r$ be the distance to $\partial B_1$. Then $1-r^2 = d(2-d)$, so
$$
u \;=\; \big(2/(d(2-d))\big)^{\frac{n-2}{2}} \;=\; d^{-\frac{n-2}{2}}\Big(1 + \tfrac{n-2}{4}d + O(d^2)\Big).
$$
This confirms the universal leading coefficient $u_0 = 1$ in the expansion of Section 2. The metric is complete: along a radial ray, $\int_0^1 u^{2/(n-2)}\,dr = \int_0 d^{-1}(1+O(d))\,dd = \infty$.

**Obstruction check.** The sphere $S^{n-1}\subset\mathbb{R}^n$ is totally umbilic, and the whole solution is a round hyperbolic metric, conformally flat. Every term in the expansion is explicit and there is **no** $d^{n}\log d$ term: $\mathcal{B}_{S^{n-1}} = 0$. Perturbing $\partial\Omega$ to a non-umbilic hypersurface makes $\mathcal{B}$ generically nonzero — for $n=3$, $\mathcal{B}$ becomes a multiple of the Willmore operator $\Delta_\Sigma H + 2H(H^2-K)$, which vanishes only on Willmore surfaces. This is exactly the residual open problem of Section 6 in the negative case.

**Contrast with the positive case.** Replace $\Lambda = \partial B_1$ by $\Lambda = \{0\}$ in $S^n$ and ask for $R_{\tilde g} = +n(n-1)$. By Caffarelli–Gidas–Spruck, every positive solution of $\Delta u + \frac{n(n-2)}{4}u^{p} = 0$ on a punctured ball is asymptotically radial, and either extends smoothly across $0$ (giving an incomplete metric) or blows up like $|x|^{-(n-2)/2}$ — which for a single point yields a metric of finite distance to the puncture. Hence **no** complete solution: one point is too small, consistent with $\dim_{\mathcal H}\{0\} = 0$ and the Delaunay obstruction. Two points, by contrast, admit the full Delaunay family — the smallest nontrivial positive-case example.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*