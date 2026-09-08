---
id: 06-pdes/calabi-conjecture
title: "Calabi Conjecture"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Calabi Conjecture

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/calabi-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(M,\omega)$ be a compact Kähler manifold of complex dimension $n$ without boundary. Calabi (1954, 1957) asked: **is the Ricci form of a Kähler metric prescribable within a fixed Kähler class?**

Precisely: the Ricci form $\mathrm{Ric}(\omega)$ of a Kähler metric is a closed real $(1,1)$-form representing $2\pi c_1(M)$ in de Rham cohomology. Given any closed real $(1,1)$-form $R$ with $[R] = 2\pi c_1(M)$, does there exist a **unique** Kähler metric $\tilde\omega$ with $[\tilde\omega] = [\omega] \in H^{1,1}(M,\mathbb{R})$ such that
$$\mathrm{Ric}(\tilde\omega) = R\,?$$

Equivalently (the "volume form" version): given a smooth positive volume form $\Omega$ on $M$ with $\int_M \Omega = \int_M \omega^n/n!$, there is a unique Kähler $\tilde\omega \in [\omega]$ with $\tilde\omega^n/n! = \Omega$.

Calabi proved uniqueness in 1957; existence was the open part. **Yau proved existence in 1976–78** (announced 1976, full proof *Comm. Pure Appl. Math.* 1978), work cited in his 1982 Fields Medal. The conjecture is therefore **solved**; the page is retained because its natural extensions — the Kähler–Einstein problem for $c_1 > 0$, degenerate-class versions, and Calabi-type problems on non-Kähler backgrounds — remain live and partly open.

A complete proof must produce, for each admissible datum, a smooth solution and establish uniqueness; the analytic core is solvability of a fully nonlinear complex Monge–Ampère equation with a priori estimates up to $C^{2,\alpha}$.

## 2. Mathematical Foundations

**Kähler setting.** $M$ a compact complex $n$-manifold, $\omega = \tfrac{i}{2}\sum g_{j\bar k}\,dz^j\wedge d\bar z^k$ a Kähler form ($d\omega = 0$, $(g_{j\bar k})>0$). The Ricci form is
$$\mathrm{Ric}(\omega) = -i\,\partial\bar\partial \log\det(g_{j\bar k}),$$
a closed real $(1,1)$-form whose class is $2\pi c_1(M)$, independent of the metric.

**Reduction by the $\partial\bar\partial$-lemma.** If $R$ is closed, real, $(1,1)$ and $[R]=[\mathrm{Ric}(\omega)]$, then $\mathrm{Ric}(\omega)-R = i\partial\bar\partial f$ for $f \in C^\infty(M,\mathbb{R})$, unique up to a constant. Any $\tilde\omega \in [\omega]$ is $\tilde\omega = \omega + i\partial\bar\partial\varphi > 0$ for a **Kähler potential** $\varphi$. The problem becomes the **complex Monge–Ampère equation**
$$(\omega + i\partial\bar\partial\varphi)^n = e^{f}\,\omega^n, \qquad \omega+i\partial\bar\partial\varphi > 0,$$
in local coordinates
$$\det\!\left(g_{j\bar k} + \frac{\partial^2\varphi}{\partial z^j \partial\bar z^k}\right) = e^{f}\det(g_{j\bar k}),$$
subject to the **compatibility condition** $\int_M e^f \omega^n = \int_M \omega^n$, with normalization $\int_M \varphi\,\omega^n = 0$ fixing the constant.

**Structure.** The operator $\varphi \mapsto \log\frac{(\omega+i\partial\bar\partial\varphi)^n}{\omega^n}$ is second-order, fully nonlinear, elliptic and concave in the Hessian ($\log\det$ is concave on positive-definite Hermitian matrices), defined on the convex set of $\omega$-plurisubharmonic potentials. Its linearization at $\varphi$ is $\Delta_{\tilde\omega}$, whose kernel on a compact manifold is the constants — the one-dimensional cokernel handled by the normalization.

**Continuity method.** Solve $(\omega+i\partial\bar\partial\varphi_t)^n = e^{tf + c_t}\omega^n$ for $t\in[0,1]$. Openness: implicit function theorem in $C^{k,\alpha}$ (invertibility of $\Delta_{\tilde\omega}$ on mean-zero functions). Closedness demands a priori estimates:

- $C^0$: Yau's Moser iteration on $\|\varphi\|_{L^p}$, giving $\|\varphi\|_{C^0} \le C(n,\omega,\|f\|_{C^0})$.
- $C^2$: the key estimate, from applying $\Delta_{\tilde\omega}$ to $\log(n+\Delta_\omega\varphi) - A\varphi$ and using a lower bound on the bisectional curvature of $\omega$, yielding $0 < n + \Delta_\omega\varphi \le C e^{A(\varphi - \inf\varphi)}$.
- $C^{2,\alpha}$: Calabi's third-order identity bounding $S = |\nabla^3\varphi|^2_{\tilde\omega}$; today replaced by Evans–Krylov theory for concave fully nonlinear equations.
- Higher orders: Schauder bootstrap.

**Corollary (Calabi–Yau theorem).** If $c_1(M)=0$, taking $R=0$ gives a unique Ricci-flat Kähler metric in each Kähler class; holonomy lies in $SU(n)$ when $M$ is simply connected with trivial canonical bundle — the **Calabi–Yau manifolds**.

## 3. History & State of the Art (SOTA)

- **1954/1957** — Eugenio Calabi states the conjecture (ICM Amsterdam 1954 short communication; "On Kähler manifolds with vanishing canonical class," in *Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz*, Princeton, 1957) and proves **uniqueness** by a maximum-principle argument.
- **1960s–70s** — The continuity method is set up; the $C^2$ estimate is the recognized obstruction.
- **1976** — Shing-Tung Yau announces the proof; **1978** full publication, "On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I," *Comm. Pure Appl. Math.* **31**, 339–411.
- **1978** — Thierry Aubin independently solves the negative case $c_1(M)<0$ (Kähler–Einstein, negative scalar curvature); Yau's theorem covers this too.
- **1980s** — Consequences: Miyaoka–Yau inequality $c_1^2 \le 3c_2$ for surfaces of general type; characterization of $\mathbb{CP}^2$; Calabi–Yau threefolds as string compactifications (Candelas–Horowitz–Strominger–Witten 1985).
- **1990s–2000s** — Pluripotential theory: Kołodziej's $L^p$ $C^0$-estimate (*Acta Math.* 1998) removes smoothness of the data; Guedj–Zeriahi finite-energy classes.
- **2015** — Chen–Donaldson–Sun prove the Yau–Tian–Donaldson conjecture: for $c_1(M)>0$, a Kähler–Einstein metric exists iff $(M,-K_M)$ is K-polystable (*J. Amer. Math. Soc.* **28**).
- **2021–2023** — Guo–Phong–Song–Sturm–Tong obtain **PDE-based, pluripotential-free** $L^\infty$ estimates for complex Monge–Ampère and related equations (*Ann. of Math.* 2023), a new proof of the $C^0$ bound valid in degenerating families.

## 4. Partial Results / Verified Cases

The original conjecture is proved in **all** complex dimensions $n\ge 1$ on all compact Kähler manifolds. Status of the surrounding program:

| Setting | Status |
|---|---|
| Compact Kähler, prescribed Ricci form in $2\pi c_1$ | **Solved** (Yau 1978); uniqueness Calabi 1957 |
| $n=1$ (Riemann surfaces) | Classical; linear, equivalent to prescribed-curvature/uniformization |
| $c_1(M)<0$ Kähler–Einstein | **Solved** (Aubin 1978; Yau 1978), unique up to scale |
| $c_1(M)=0$ Ricci-flat | **Solved**; one metric per point of the Kähler cone |
| $c_1(M)>0$ Kähler–Einstein | **Solved modulo stability**: exists iff K-polystable (Chen–Donaldson–Sun 2015; Tian 2015) |
| Degenerate classes on the boundary of the Kähler cone | Solved for big and semi-ample classes (Eyssidieux–Guedj–Zeriahi 2009); potentials in $L^\infty$, smooth on a Zariski-open set |
| Compact Hermitian, non-Kähler ($\partial\bar\partial\omega\ne 0$) | Solved (Tosatti–Weinkove, *J. Amer. Math. Soc.* 2010) |
| Complete non-compact: ALE, asymptotically cylindrical, Tian–Yau ends | Largely solved (Tian–Yau 1990/91, Joyce, Hein); some conical and Poincaré-type cases open |
| Strominger system (non-Kähler heterotic) | **Open in general**; Fu–Yau (2008) solve a torus-fibration ansatz |
| Rough data $e^f \in L^p$, $p>1$ | Solved with continuous potential (Kołodziej 1998); fails at $p=1$ |

## 5. Principal Obstacles

Historical for the compact Kähler case; structural for the extensions.

- **Full nonlinearity.** $\det(\text{Hessian})$ is not divergence-form; no coercive linear leading term, so $H^1$ energy methods give no compactness. The Aubin–Mabuchi functional is convex only along geodesics in the space of Kähler potentials, and those geodesics themselves solve a degenerate Monge–Ampère equation.
- **Curvature input in the $C^2$ estimate.** Yau's second-order bound consumes a lower bisectional-curvature bound of the *background* metric. On Hermitian backgrounds the Chern connection has torsion, the Bochner terms fail to cancel, and new commutation identities are required.
- **Degeneracy at the cone boundary.** As $[\omega]$ degenerates, ellipticity degenerates and $C^2$ bounds blow up (collapsing fibres). Only $L^\infty$ control survives, forcing pluripotential or comparison methods.
- **Genuine obstructions in the Fano case.** The continuity method fails at $t=1$: the Futaki invariant and Matsushima's reductivity theorem obstruct existence. Handling bubbling requires Cheeger–Colding–Gromov–Hausdorff limit theory and partial $C^0$-estimates for Bergman kernels — not a maximum-principle argument.
- **Coupled systems.** With torsion the equation couples to a metric on an auxiliary bundle (Strominger system); the unknown is not a single scalar, ellipticity is only of the whole system, and no scalar maximum principle governs the Hermitian–Yang–Mills part.

## 6. The Gap

For the original conjecture there is no gap: Yau's estimates close the continuity method, and uniqueness is Calabi's. The live boundary lies one step out.

- **Fano PDE gap.** K-polystability characterizes existence but is algebro-geometric, not an analytic criterion checkable by local estimates. No purely PDE proof of Chen–Donaldson–Sun avoiding metric-limit theory is known.
- **Regularity gap in degenerate classes.** Solutions in big classes are smooth off a proper analytic subset; the exact structure of the singular set, and whether such singular spaces are always Gromov–Hausdorff limits of smooth Calabi–Yau metrics, is only partly settled.
- **Torsion gap.** No analogue of the $C^2$ estimate exists for the full Strominger system with general anomaly-cancellation data. Existence for general non-Kähler threefolds with holomorphic $(3,0)$-form is open.

## 7. Current Research (as of June 2026)

- **Pluripotential-free $L^\infty$ estimates** — Guo, Phong, Song, Sturm, Tong: an auxiliary-Monge–Ampère comparison technique giving uniform bounds for wide families of fully nonlinear equations, including Hessian equations and degenerating families. Now a standard tool; parabolic and Hermitian extensions active. *(frontier — verify current scope of the parabolic case.)*
- **Collapsing and metric limits** — Tosatti, Zhang, Hein, Sun, Székelyhidi: behavior of Ricci-flat metrics as the Kähler class degenerates to a fibration class (SYZ collapse), semiflat approximations, non-collapsed singularity models.
- **Non-Kähler geometry** — Fu, Yau, Phong, Picard, Zhang: the Anomaly flow, whose stationary points solve the Strominger system.
- **Singular Calabi–Yau spaces** — Eyssidieux–Guedj–Zeriahi framework combined with the minimal model program; klt pairs, orbifold and conical Kähler–Einstein metrics.
- **Groups** — Harvard / Tsinghua YMSC (Yau), Columbia (Phong), Northwestern (Tosatti, Weinkove), Stony Brook and the Simons Center (Sun, Donaldson), Grenoble–Toulouse (Guedj, Zeriahi), Northwestern/Chicago (Székelyhidi).

## 8. Future Work

- Prove existence for the **Strominger system** on general compact non-Kähler Calabi–Yau threefolds; the Anomaly flow is the leading candidate.
- Find a purely analytic proof of the **Yau–Tian–Donaldson** criterion, replacing Gromov–Hausdorff compactness with uniform Bergman-kernel estimates.
- Classify **Gromov–Hausdorff limits** of Ricci-flat Kähler metrics with bounded diameter and volume, matching them to algebro-geometric moduli.
- Extend the new $L^\infty$ machinery to **Hessian quotient equations**, the $J$-equation, and deformed Hermitian–Yang–Mills, where analogous stability criteria are conjectured.
- Quantitative uniqueness: effective moduli of continuity for $\varphi$ in terms of $\|e^f\|_{L^p}$ as $p \to 1^+$.

## 9. Key References

- **[Foundational]** E. Calabi. *On Kähler manifolds with vanishing canonical class.* In "Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz," Princeton University Press, 1957, pp. 78–89. [DOI](https://doi.org/10.1515/9781400879915-006)
- **[Foundational]** S.-T. Yau. *On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I.* Communications on Pure and Applied Mathematics **31** (1978), 339–411. [DOI](https://doi.org/10.1002/cpa.3160310304)
- **[Foundational]** T. Aubin. *Équations du type Monge–Ampère sur les variétés kählériennes compactes.* Bulletin des Sciences Mathématiques **102** (1978), 63–95.
- **[Foundational]** S. Kołodziej. *The complex Monge–Ampère equation.* Acta Mathematica **180** (1998), 69–117.
- **[SOTA]** X. Chen, S. Donaldson, S. Sun. *Kähler–Einstein metrics on Fano manifolds, I, II, III.* Journal of the American Mathematical Society **28** (2015), 183–197, 199–234, 235–278.
- **[SOTA]** P. Eyssidieux, V. Guedj, A. Zeriahi. *Singular Kähler–Einstein metrics.* Journal of the American Mathematical Society **22** (2009), 607–639.
- **[SOTA]** V. Tosatti, B. Weinkove. *The complex Monge–Ampère equation on compact Hermitian manifolds.* Journal of the American Mathematical Society **23** (2010), 1187–1195.
- **[SOTA / Recent]** B. Guo, D. H. Phong, F. Tong. *On $L^\infty$ estimates for complex Monge–Ampère equations.* Annals of Mathematics **198** (2023), 393–418. [DOI](https://doi.org/10.4007/annals.2023.198.1.4)
- **[Recent]** J.-X. Fu, S.-T. Yau. *The theory of superstring with flux on non-Kähler manifolds and the complex Monge–Ampère equation.* Journal of Differential Geometry **78** (2008), 369–428. [DOI](https://doi.org/10.4310/jdg/1207834550)
- **[Survey]** D. D. Joyce. *Compact Manifolds with Special Holonomy.* Oxford University Press, 2000.
- **[Survey]** V. Guedj, A. Zeriahi. *Degenerate Complex Monge–Ampère Equations.* EMS Tracts in Mathematics 26, European Mathematical Society, 2017. [DOI](https://doi.org/10.4171/167)
- **[Survey]** G. Székelyhidi. *An Introduction to Extremal Kähler Metrics.* Graduate Studies in Mathematics 152, American Mathematical Society, 2014.

## 10. Worked Example / Concrete Special Case

**Complex tori: the conjecture proved by hand in every dimension.**

Let $M = \mathbb{C}^n/\Lambda$ with $\Lambda$ a full lattice, and $\omega_0 = \tfrac{i}{2}\sum_j dz^j\wedge d\bar z^j$ the flat Kähler form. Here $c_1(M)=0$ and $\mathrm{Ric}(\omega_0)=0$.

Prescribe $R=0$: find all Ricci-flat metrics in $[\omega_0]$. The equation is
$$\det\!\left(\delta_{j\bar k} + \varphi_{j\bar k}\right) = 1, \qquad \omega_0 + i\partial\bar\partial\varphi > 0,$$
with $\varphi$ $\Lambda$-periodic. Claim: the only solutions are $\varphi \equiv \text{const}$.

*Proof.* Set $A = (\delta_{j\bar k}+\varphi_{j\bar k}) > 0$, so $\det A = 1$. The arithmetic–geometric mean inequality on the eigenvalues of $A$ gives
$$\tfrac{1}{n}\operatorname{tr} A \ \ge\ (\det A)^{1/n} = 1 \quad\Longrightarrow\quad \operatorname{tr} A = n + \Delta_0\varphi \ \ge\ n,$$
where $\Delta_0 = \sum_j \partial^2/\partial z^j\partial\bar z^j$. So $\Delta_0\varphi \ge 0$: $\varphi$ is subharmonic on a compact manifold, hence constant by the maximum principle. Then $A = I$ and $\tilde\omega = \omega_0$. $\square$

The flat metric is the unique Ricci-flat representative of its class. Yau's theorem is exactly the statement that the AM–GM step can be replaced, on a curved background, by the estimate $0 < n + \Delta_\omega\varphi \le Ce^{A(\varphi-\inf\varphi)}$.

**Nontrivial datum, $n=1$.** For $M=\mathbb{C}/\Lambda$ of area $V$, prescribing $\tilde\omega = e^{f}\omega_0$ reduces to the *linear* Poisson equation
$$\Delta_0\varphi = e^f - 1,$$
solvable iff $\int_M (e^f-1)\,\omega_0 = 0$, i.e. $\int_M e^f\omega_0 = V$ — precisely the compatibility condition. The solution is unique up to an additive constant, and positivity $1+\Delta_0\varphi = e^f > 0$ is automatic. Complex dimension $1$ is linear; the nonlinearity, and the whole difficulty of the conjecture, first appears at $n=2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*