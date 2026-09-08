---
id: 05-analysis/schoen-conjecture
title: "Schoen Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Schoen Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/schoen-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbb{H}^n$ ($n \ge 2$) be real hyperbolic $n$-space with ideal boundary $\partial_\infty \mathbb{H}^n \cong S^{n-1}$ carrying its standard conformal structure.

**Conjecture (Schoen, 1993; higher-dimensional form often attributed to Schoen–Li–Tam).**
Every quasiconformal homeomorphism $f: S^{n-1} \to S^{n-1}$ is the ideal boundary extension of a **unique harmonic quasi-isometric diffeomorphism**
$$u : \mathbb{H}^n \longrightarrow \mathbb{H}^n , \qquad \tau(u) = 0, \qquad u|_{\partial_\infty} = f .$$
For $n = 2$, "quasiconformal on $S^1$" means quasisymmetric.

A complete solution must supply three separate things: (i) **existence** of a harmonic $u$ with boundary value $f$; (ii) **uniqueness** in the class of harmonic maps with that boundary extension (equivalently, at bounded distance from a given quasi-isometry); (iii) the **regularity/injectivity** claim that $u$ is a diffeomorphism with $\det du \neq 0$ everywhere and is itself quasiconformal. A disproof requires a quasiconformal $f$ admitting no harmonic quasi-isometric extension, two distinct ones, or one whose Jacobian vanishes somewhere.

## 2. Mathematical Foundations

**Harmonic maps.** For $u : (M,g) \to (N,h)$ smooth, the energy is
$$E(u) = \tfrac12 \int_M |du|^2 \, dv_g, \qquad |du|^2 = g^{ij} h_{\alpha\beta}(u)\, \partial_i u^\alpha \partial_j u^\beta .$$
Criticality gives the tension field equation
$$\tau(u)^\gamma \;=\; \Delta_g u^\gamma + g^{ij}\, \Gamma^\gamma_{\alpha\beta}(u)\, \partial_i u^\alpha \partial_j u^\beta \;=\; 0 ,$$
a quasilinear elliptic system (Eells–Sampson, 1964). On a noncompact domain $E(u)=\infty$ for quasi-isometries, so $u$ cannot be obtained by direct minimization.

**Quasi-isometry and quasiconformality.** $u$ is an $(L,C)$-quasi-isometric map if
$$L^{-1} d(x,y) - C \le d(u(x),u(y)) \le L\, d(x,y) + C .$$
By Mostow-type boundary theory, $(L,C)$-quasi-isometries of $\mathbb{H}^n$ induce $K$-quasiconformal maps of $S^{n-1}$ with $K = K(L,C)$, and conversely every quasiconformal $f$ of $S^{n-1}$ is the boundary map of some (non-harmonic) quasi-isometry — e.g. its Ahlfors–Beurling or barycentric (Douady–Earle) extension.

**Bochner formula.** With $\mathrm{Sec}_N \le -1$ and $\mathrm{Ric}_M \ge -(n-1)$,
$$\tfrac12 \Delta |du|^2 = |\nabla du|^2 + \langle du \cdot \mathrm{Ric}_M , du\rangle - \sum_{i,j} \big\langle R^N(du(e_i), du(e_j))\, du(e_j), du(e_i)\big\rangle ,$$
whence $\Delta e(u) \ge -2(n-1) e(u) + 2 |du \wedge du|^2$; this is the engine of every a priori estimate and of the uniqueness (convexity of $t \mapsto d(u_1(\gamma(t)),u_2(\gamma(t)))$ along geodesics).

**Dimension 2 (complex-analytic form).** For $u : \mathbb{H}^2 \to \mathbb{H}^2$, write $z$ for a conformal coordinate on the domain, $\rho^2|dw|^2$ for the target metric, and set
$$\mathcal{H} = \rho^2(u)\,|u_z|^2, \qquad \mathcal{L} = \rho^2(u)\,|u_{\bar z}|^2, \qquad \mu = \frac{u_{\bar z}}{u_z}, \qquad |\mu|^2 = \mathcal{L}/\mathcal{H} .$$
Harmonicity is $u_{z\bar z} + (\partial_w \log \rho^2)(u)\, u_z u_{\bar z} = 0$, and the **Hopf differential**
$$\Phi(u) = \big(u^*h\big)^{2,0} = \rho^2(u)\, u_z \overline{u_{\bar z}} \, dz^2$$
is holomorphic. The Bochner identities become
$$\Delta_0 \log \mathcal{H} = 2(\mathcal{H} - \mathcal{L}), \qquad \Delta_0 \log \mathcal{L} = -2(\mathcal{H}-\mathcal{L}) \quad (\mathcal{H},\mathcal{L}>0),$$
for curvature $-1$ target. Quasiconformality of $u$ is $\|\mu\|_\infty < 1$; the Jacobian is $J = \mathcal{H} - \mathcal{L}$.

**Wan's correspondence.** Orientation-preserving quasiconformal harmonic diffeomorphisms of $\mathbb{H}^2$ correspond bijectively to holomorphic quadratic differentials $\Phi$ on $\mathbb{H}^2$ of finite hyperbolic sup-norm $\|\Phi\|_\infty = \sup |\Phi| / \rho^2 < \infty$ (Wan 1992; Tam–Wan 1995). Equivalently such $u$ correspond to complete spacelike constant-mean-curvature (CMC) surfaces in Minkowski $3$-space $\mathbb{R}^{2,1}$.

## 3. History & State of the Art (SOTA)

- **1964.** Eells–Sampson establish the heat-flow existence theory for compact targets of nonpositive curvature.
- **1978.** Schoen–Yau and Sampson: a harmonic homeomorphism between surfaces with nonpositively curved target has nonvanishing Jacobian, hence is a diffeomorphism. This is why in $n = 2$ item (iii) of Section 1 is automatic once (i)–(ii) hold.
- **1991–1993.** Li–Tam solve the Dirichlet problem at infinity for proper harmonic maps of $\mathbb{H}^n$ with sufficiently regular ($C^1$, later Hölder-type) boundary data, and prove uniqueness of proper harmonic maps with given continuous boundary values under bounded-distance normalizations.
- **1993.** Schoen states the conjecture in *The role of harmonic mappings in rigidity and deformation problems*, framing it as the harmonic-map analogue of the Ahlfors–Beurling extension and a tool for Teichmüller theory.
- **1992–1995.** Wan, then Tam–Wan, give the Hopf-differential classification in $n = 2$ and prove existence for boundary maps whose associated quadratic differential has small norm; small-dilatation cases follow.
- **1997.** Hardt–Wolf show that harmonic extensions of quasiconformal boundary maps of $\mathbb{H}^n$ are quasi-isometric under smallness hypotheses.
- **2015–2018.** Marković proves uniqueness for $\mathbb{H}^3$, then the full conjecture for $n = 2$; Lemm–Marković establish existence for $\mathbb{H}^n$, $n \ge 3$, by heat flow.
- **2017–2021.** Benoist–Hulin prove the bounded-distance statement in the greatest generality now known: rank-one symmetric spaces, then pinched negatively curved Hadamard manifolds.

**SOTA summary.** Existence and uniqueness *up to bounded distance* are theorems in all dimensions. The **diffeomorphism and quasiconformality of the harmonic extension remain open for $n \ge 3$**.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n = 2$, all quasisymmetric $f$ | Full conjecture: existence, uniqueness, and (via Schoen–Yau/Sampson) diffeomorphism | Marković, JAMS 2017 |
| $n = 2$, $\|\Phi\|_\infty$ small / small dilatation $K \to 1$ | Explicit correspondence $u \leftrightarrow \Phi$; existence and uniqueness | Wan 1992; Tam–Wan 1995 |
| $n = 3$ | Uniqueness of quasi-isometric harmonic maps with prescribed boundary map | Marković, Invent. Math. 2015 |
| $n \ge 3$, quasi-isometries of $\mathbb{H}^n$ | Existence of a harmonic map at bounded distance | Lemm–Marković, JDG 2018 |
| Rank-one symmetric spaces $X \to Y$ (real, complex, quaternionic hyperbolic, $\mathbb{O}H^2$) | Every quasi-isometric map is at bounded distance from a **unique** harmonic map | Benoist–Hulin, Ann. of Math. 2017 |
| Hadamard manifolds with $-b^2 \le \mathrm{Sec} \le -a^2 < 0$ | Same bounded-distance existence/uniqueness | Benoist–Hulin II, JEMS 2021 |
| Boundary data $f \in C^1$ or $C^{1,\alpha}$, any $n$ | Proper harmonic extension exists, is unique, boundary-regular | Li–Tam 1993 |
| CAT(0) Gromov-hyperbolic targets | Bounded-distance harmonic (energy-minimizing) representatives | Sidler–Wenger, 2019–2022 |

## 5. Principal Obstacles

- **Infinite energy.** For a quasi-isometry of $\mathbb{H}^n$, $E(u) = \infty$; direct variational methods and standard heat-flow convergence (which use energy monotonicity) do not apply. One must run the flow with only $L^\infty$-type control, which is what Lemm–Marković and Benoist–Hulin engineer.
- **Loss of the Hopf differential in $n \ge 3$.** The whole $n = 2$ machinery — holomorphicity of $\Phi$, the $\mathcal{H}/\mathcal{L}$ system, the CMC-surface dictionary, Wan's bijection — is a two-dimensional accident. There is no holomorphic invariant of a harmonic map in dimension $\ge 3$, so the pullback metric $u^*h$ is uncontrolled beyond the crude Bochner inequality.
- **No Jacobian maximum principle.** The Schoen–Yau/Sampson argument that $J = \mathcal{H} - \mathcal{L}$ obeys $\Delta \log J \ge 0$ is a surface computation. In $n \ge 3$ nothing prevents $\det du$ from vanishing on a set of codimension one; hence "harmonic quasi-isometry" $\not\Rightarrow$ "diffeomorphism".
- **Boundary regularity is degenerate.** The hyperbolic metric blows up at $\partial_\infty$; the harmonic map system becomes singular there, and Schauder theory at the boundary requires $f$ to be at least $C^1$ — the conjecture assumes only quasiconformality, i.e. $f$ can be nowhere differentiable with singular boundary dilatation.
- **Quasiconformality is not preserved.** A harmonic map at bounded distance from a quasi-isometry is itself a quasi-isometry, but pointwise dilatation bounds ($|\mu| \le k < 1$-type control on the whole of $\mathbb{H}^n$) do not follow from Bochner estimates; they need a two-sided lower bound on $\det du$, which is exactly what is missing.

## 6. The Gap

Section 4 gives, for every $n$ and every quasi-isometry $\psi$ of $\mathbb{H}^n$, a unique harmonic $u$ with $\sup_x d(u(x),\psi(x)) < \infty$; hence for every quasiconformal $f$ a harmonic quasi-isometry with $u|_{\partial_\infty} = f$. Section 1 asks additionally that $u$ be a **diffeomorphism**, i.e. $\det du \neq 0$ everywhere, and quasiconformal.

The precise missing step for $n\ge 3$: **prove a uniform lower bound $\det du \ge c(L,C,n) > 0$ (or merely $\det du \neq 0$) for a harmonic quasi-isometry of $\mathbb{H}^n$**, without a Hopf-differential surrogate. Equivalently: show that the smallest singular value of $du$ cannot vanish. No maximum-principle quantity is known whose subharmonicity forces this in dimension $\ge 3$.

## 7. Current Research (as of June 2026)

- **Benoist–Hulin school (Paris-Saclay/ENS).** Extension of the bounded-distance theorem to quotients, to targets with unbounded curvature ratio, and to non-Riemannian settings. Their $L^\infty$–Bochner ("harmonic maps are at bounded distance") technique is now the standard tool.
- **Marković and collaborators (Oxford).** Heat-flow methods on $\mathbb{H}^n$, and the related uniqueness/rigidity circle for harmonic maps between hyperbolic spaces.
- **Injectivity program.** Attempts to bound $\det du$ from below via monotonicity of the Jacobian along the harmonic heat flow, or via convexity of the distance function on the target applied to nearby fibres. *(frontier — verify)* Several preprints claim partial injectivity for harmonic quasi-isometries of $\mathbb{H}^3$ with dilatation $K$ close to $1$.
- **Metric-space generalizations.** Sidler–Wenger-type results on Gromov hyperbolic CAT(0) targets, and Korevaar–Schoen theory for singular targets, being pushed toward buildings and $\mathbb{R}$-trees.
- **Higher rank.** The analogue fails for higher-rank symmetric spaces in its naive form; identifying the correct statement (e.g. for maps to $\mathrm{SL}(n,\mathbb{R})/\mathrm{SO}(n)$) is an active question connected to Anosov representations and Hitchin components. *(frontier — verify)*

## 8. Future Work

- Find a dimension-free replacement for the Hopf differential: a tensorial, divergence-free quantity attached to a harmonic map controlling the conformal distortion of $u^*h$.
- Develop boundary Schauder theory at $\partial_\infty \mathbb{H}^n$ for merely quasiconformal data; a Carleson-measure or $A_\infty$-weight formulation of quasiconformality on $S^{n-1}$ may be the right regularity class.
- Settle whether a harmonic quasi-isometry $\mathbb{H}^3 \to \mathbb{H}^3$ can have a degenerate Jacobian at a point — even a single counterexample would refute the conjecture as stated and reframe the correct statement as bounded-distance only.
- Quantify: prove $K$-quasiconformality of $u$ with $K' = K'(K,n)$, i.e. an effective harmonic analogue of the Ahlfors–Beurling extension.
- Applications: a positive answer would give a canonical, conformally natural, real-analytic section of the extension operator on the universal Teichmüller space $T(1)$ in all dimensions.

## 9. Key References

- **[Foundational]** J. Eells, J. H. Sampson. *Harmonic mappings of Riemannian manifolds.* American Journal of Mathematics 86 (1964), 109–160.
- **[Foundational]** R. Schoen, S.-T. Yau. *On univalent harmonic maps between surfaces.* Inventiones Mathematicae 44 (1978), 265–278. [DOI](https://doi.org/10.1007/bf01403164)
- **[Foundational]** R. Schoen. *The role of harmonic mappings in rigidity and deformation problems.* In *Complex Geometry (Osaka, 1990)*, Lecture Notes in Pure and Applied Mathematics 143, Marcel Dekker, 1993, 179–200.
- **[Foundational]** P. Li, L.-F. Tam. *Uniqueness and regularity of proper harmonic maps.* Annals of Mathematics 137 (1993), 167–201; and *II*, Indiana University Mathematics Journal 42 (1993), 591–635. [DOI](https://doi.org/10.2307/2946622)
- **[Foundational]** T. Y.-H. Wan. *Constant mean curvature surface, harmonic maps, and universal Teichmüller space.* Journal of Differential Geometry 35 (1992), 643–657. [DOI](https://doi.org/10.4310/jdg/1214448260)
- **[Foundational]** L.-F. Tam, T. Y.-H. Wan. *Quasi-conformal harmonic diffeomorphism and the universal Teichmüller space.* Journal of Differential Geometry 42 (1995), 368–410. [DOI](https://doi.org/10.4310/jdg/1214457235)
- **[SOTA / Recent]** V. Marković. *Harmonic maps between 3-dimensional hyperbolic spaces.* Inventiones Mathematicae 199 (2015), 921–951. [DOI](https://doi.org/10.1007/s00222-014-0536-x)
- **[SOTA / Recent]** V. Marković. *Harmonic maps and the Schoen conjecture.* Journal of the American Mathematical Society 30 (2017), 799–817. [DOI](https://doi.org/10.1090/jams/881)
- **[SOTA / Recent]** Y. Benoist, D. Hulin. *Harmonic quasi-isometric maps between rank one symmetric spaces.* Annals of Mathematics (2) 185 (2017), 895–917. [DOI](https://doi.org/10.4007/annals.2017.185.3.4)
- **[SOTA / Recent]** Y. Benoist, D. Hulin. *Harmonic quasi-isometric maps II: negatively curved manifolds.* Journal of the European Mathematical Society 23 (2021), 2861–2911. [DOI](https://doi.org/10.4171/jems/1065)
- **[SOTA / Recent]** M. Lemm, V. Marković. *Heat flows on hyperbolic spaces.* Journal of Differential Geometry 108 (2018), 495–529. [DOI](https://doi.org/10.4310/jdg/1519959624)
- **[Related]** R. Hardt, M. Wolf. *Harmonic extensions of quasiconformal maps to hyperbolic space.* Indiana University Mathematics Journal 46 (1997), 155–163. [DOI](https://doi.org/10.1512/iumj.1997.46.1351)
- **[Survey]** R. Schoen, S.-T. Yau. *Lectures on Harmonic Maps.* International Press, 1997.
- **[Survey]** J. Eells, L. Lemaire. *Two Reports on Harmonic Maps.* World Scientific, 1995. [DOI](https://doi.org/10.1142/2088)

## 10. Worked Example / Concrete Special Case

**Claim.** There is an explicit one-parameter family of harmonic diffeomorphisms of $\mathbb{H}^2$ whose ideal boundary map is the *identity* but which are not the identity. They are not quasiconformal — showing that the normalization in Section 1 is not decorative.

Use the upper half-plane $\mathbb{H}^2 = \{(x,y): y>0\}$, $h = y^{-2}(dx^2+dy^2)$. For a map $u = (U,V)$ from a conformally flat surface into $\mathbb{H}^2$, the Christoffel symbols $\Gamma^U_{UV} = -1/V$, $\Gamma^V_{UU} = 1/V$, $\Gamma^V_{VV} = -1/V$ give
$$\Delta U - \frac{2}{V}\nabla U\!\cdot\!\nabla V = 0, \qquad \Delta V + \frac{1}{V}\big(|\nabla U|^2 - |\nabla V|^2\big) = 0 .$$

Take the parabolic-invariant ansatz $U = x$, $V = V(y)$. The first equation holds identically. The second becomes the ODE
$$V'' + \frac{1 - (V')^2}{V} = 0 .$$
Set $q = (V')^2$ as a function of $V$: $\tfrac12 q' = (1-q)/V$, so $\dfrac{dq}{q-1} = \dfrac{2\,dV}{V}$ and $q - 1 = cV^2$, i.e.
$$V'(y) = \sqrt{1 + c\,V(y)^2}.$$

- $c = 0$: $V = y$, the identity map.
- $c = -k^2 < 0$: $V = k^{-1}\sin(ky)$, image is a bounded band — not surjective, not proper.
- $c = k^2 > 0$: $\boxed{\,u_k(x,y) = \big(x,\ k^{-1}\sinh(ky)\big)\,}$, a smooth bijection of $\mathbb{H}^2$ onto itself with $\partial_y V = \cosh(ky) > 0$, hence a **harmonic diffeomorphism**.

**Boundary behaviour.** As $y \to 0$, $V = y + O(y^3)$, so $u_k \to \mathrm{id}$ on $\mathbb{R} = \partial_\infty\mathbb{H}^2 \setminus \{\infty\}$, and $u_k(\infty) = \infty$. The boundary extension is the identity of $S^1$, yet $u_k \ne \mathrm{id}$ for $k \ne 0$.

**Why no contradiction with uniqueness.** Compute the Hopf differential with $z = x+iy$:
$$u_k^*h = \frac{dx^2 + (V')^2 dy^2}{V^2}, \qquad \Phi = \frac{1 - (V')^2}{4V^2}\, dz^2 = -\frac{c}{4}\,dz^2 = -\frac{k^2}{4}\,dz^2 ,$$
holomorphic as required. Its hyperbolic norm is $|\Phi|/\rho^2 = \tfrac{k^2}{4}y^2 \to \infty$: **unbounded**, so by Wan's theorem $u_k$ is not quasiconformal. Directly: the Beltrami coefficient of $(x,y)\mapsto (x,k^{-1}\sinh ky)$ has $|\mu| = \frac{\cosh(ky)-1}{\cosh(ky)+1} \to 1$. And $d\big(u_k(0,y),(0,y)\big) = |\log(\sinh(ky)/(ky))| \to \infty$, so $u_k$ is at unbounded distance from the identity and is not a quasi-isometry.

**Reading.** In the class the conjecture specifies — harmonic *quasi-isometric* maps — Marković's theorem says the identity is the unique extension of $\mathrm{id}_{S^1}$; the family $\{u_k\}$ shows that dropping quasi-isometry destroys uniqueness at once, in the simplest dimension, with an ODE that can be solved in closed form. The open part of the conjecture is that in $\mathbb{H}^n$, $n\ge3$, the analogous rigidity persists all the way to $\det du \ne 0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*