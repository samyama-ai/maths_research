---
id: 06-pdes/einstein-euler-shock-formation
title: "Einstein-Euler Shock Formation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Einstein-Euler Shock Formation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/einstein-euler-shock-formation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(\mathcal{M}, g)$ be a $3+1$-dimensional Lorentzian manifold solving the Einstein equations coupled to a relativistic perfect fluid. The problem has three layers, of increasing difficulty:

1. **Shock formation.** Prove that there exist open sets of smooth, asymptotically flat (or spatially compact) initial data for the Einstein–Euler system whose maximal globally hyperbolic development terminates in finite time because $\partial u$ (a first derivative of a fluid variable) blows up while $u$ itself, the metric $g$, and the curvature $\mathrm{Riem}[g]$ remain bounded. Describe the geometry of the singular set as the degeneracy of an acoustical eikonal foliation.
2. **Shock development in GR.** Continue the solution past the first singular time as a weak solution with a hypersurface of discontinuity across which the relativistic Rankine–Hugoniot jump conditions hold, the metric is only Lipschitz, and entropy increases.
3. **Cosmic censorship interaction.** Determine whether fluid shocks can be a mechanism for the breakdown of the metric's regularity — i.e., whether a shock-wave singularity in the matter is ever a genuine spacetime singularity or is always removable by a change of coordinates.

**Conjecture (the working statement).** For a barotropic or general perfect fluid that is genuinely nonlinear ($c_s \neq 0$, and not the stiff/Chaplygin exceptional cases), open sets of Einstein–Euler data form shocks in finite proper time; the shock is a *matter* singularity only, the metric extending to $C^{1,1}$ (hence $g$ locally inertial and $\mathrm{Riem}$ bounded, $L^\infty$) across the singular boundary.

A complete solution requires either a stable-shock-formation theorem for the coupled system (not just for Euler on a fixed background) plus a GR shock-development theorem, or a counterexample.

## 2. Mathematical Foundations

**The system.** With $T_{\mu\nu} = (\rho + p) u_\mu u_\nu + p\, g_{\mu\nu}$, $g(u,u) = -1$:

$$
\mathrm{Ric}_{\mu\nu} - \tfrac12 R\, g_{\mu\nu} = 8\pi T_{\mu\nu}, \qquad \nabla^\mu T_{\mu\nu} = 0, \qquad \nabla_\mu (n u^\mu) = 0 ,
$$

with $n$ the baryon density, $\rho = \rho(n,s)$, $p = p(n,s)$, $u^\mu \nabla_\mu s = 0$. The (acoustical) sound speed is

$$
c_s^2 = \left.\frac{\partial p}{\partial \rho}\right|_{s} \in (0,1).
$$

**Acoustical metric.** Sound propagation is governed by the inverse acoustical metric

$$
(h^{-1})^{\mu\nu} = (g^{-1})^{\mu\nu} + \left(1 - \frac{1}{c_s^{2}}\right) u^\mu u^\nu ,
$$

whose null cones lie strictly inside the light cones of $g$ when $c_s < 1$. For irrotational, isentropic flow there is a potential $\phi$ with $u_\mu = \partial_\mu\phi / \sqrt{-(g^{-1})^{\alpha\beta}\partial_\alpha\phi\,\partial_\beta\phi}$, and Euler reduces to the quasilinear wave equation

$$
\Box_{h(\partial\phi)} \phi = 0 .
$$

**Eikonal function and inverse foliation density.** Let $\vartheta$ solve $(h^{-1})^{\mu\nu}\partial_\mu \vartheta\, \partial_\nu \vartheta = 0$, so its level sets are outgoing acoustically null cones. Define

$$
\mu := -\frac{1}{(h^{-1})^{\alpha\beta}\partial_\alpha t \,\partial_\beta \vartheta} > 0 .
$$

A **shock** is the event $\mu \to 0$ in finite time with $|\partial\phi|$ bounded; then $|\partial^2\phi| \sim \mu^{-1} \to \infty$ and the characteristics cross. This is Christodoulou's geometric reformulation: the singularity is a degeneracy of the change of variables $(t,\vartheta,\omega) \mapsto (t,x)$, not of the solution's amplitude.

**Genuine nonlinearity.** In $1+1$ with linear EOS $p = c_s^2 \rho$, $v = \tanh\theta$, $\tanh\theta_s = c_s$, the characteristic speeds and Riemann invariants are

$$
\lambda_\pm = \frac{v \pm c_s}{1 \pm c_s v} = \tanh(\theta \pm \theta_s), \qquad J_\pm = \theta \pm \frac{c_s}{1+c_s^2}\ln n .
$$

**Jump conditions.** Across a hypersurface $\Sigma$ with unit conormal $\xi$, weak solutions satisfy $[\![ T^{\mu\nu} ]\!]\,\xi_\nu = 0$ and $[\![ n u^\mu ]\!]\,\xi_\mu = 0$, together with the entropy condition $[\![ s ]\!] \ge 0$ across the shock in the direction of flow. On the gravitational side these are the Israel junction conditions: $g \in C^{0,1}$, $[\![ g ]\!] = 0$, second fundamental form jumps balanced by the surface stress (zero here, so $[\![ K ]\!]$ is constrained).

## 3. History & State of the Art (SOTA)

- **1858–1965.** Riemann's simple-wave blowup; Lax's genuine-nonlinearity criterion; John's 1974 blowup theorem for $1$-d systems. Glimm's 1965 scheme gives global BV weak solutions in one space dimension.
- **1958.** Choquet-Bruhat: local well-posedness of Einstein-Euler in harmonic-type gauges; **Rendall (1992)** treats fluid bodies with a free boundary and vacuum interface.
- **1993–2004.** Smoller–Temple construct exact and global spherically symmetric shock-wave GR solutions; **Groah–Temple (Memoirs AMS, 2004)** prove existence for spherically symmetric Einstein-Euler with shocks via a *locally inertial* Glimm scheme, with metric regularity only $C^{0,1}$.
- **2004–2011.** **Barnes–LeFloch–Schmidt–Stewart** run Glimm on plane-symmetric Gowdy spacetimes; **LeFloch–Rendall (2011)** obtain a global areal foliation for $T^3$-Gowdy Einstein-Euler with shocks.
- **2007.** **Christodoulou**, *The Formation of Shocks in 3-Dimensional Fluids*: the landmark result. For irrotational, isentropic **relativistic** Euler on *fixed Minkowski space*, he gives a sharp, fully geometric proof of shock formation from small data, and a complete description of the boundary of the maximal development. The Newtonian analogue follows in **Christodoulou–Miao (2014)**.
- **2016–2019.** Speck's monograph extends the machinery to general quasilinear wave equations; **Miao–Yu (2017)** handle large-data short-pulse shock formation; **Christodoulou (2019)**, *The Shock Development Problem*, solves the restricted development problem in Minkowski.
- **2018–2024.** **Luk–Speck (Invent. Math. 2018)** break the irrotationality barrier in 2D with nonzero vorticity; the 3D version with vorticity and entropy follows. **Disconzi–Speck (2019)** find the null structures making the *relativistic* Euler system with vorticity and entropy amenable to the same methods. **Buckmaster–Shkoller–Vicol (CPAM 2022, 2023)** give self-similar constructions of 2D and 3D point shocks.
- **Gravity side.** **Reintjes–Temple (2015)** show apparent "regularity singularities" at shock interactions; their later RT-equation program (2020–) recovers optimal $C^{1,1}$ metric regularity by elliptic theory in $L^p$, indicating shocks do *not* create spacetime singularities.

## 4. Partial Results / Verified Cases

| Setting | Result | Status |
|---|---|---|
| Special relativistic Euler, irrotational, isentropic, $3+1$ Minkowski, small data | Christodoulou 2007: stable shock formation, full description of maximal development boundary | Proven |
| Non-relativistic 3D Euler, irrotational barotropic | Christodoulou–Miao 2014 | Proven |
| 2D compressible Euler, nonzero vorticity, plane-symmetric-perturbed simple waves | Luk–Speck 2018 | Proven |
| 3D Euler with vorticity **and** entropy, near simple plane waves | Luk–Speck (Adv. Math., 2024) | Proven |
| 3D isentropic Euler, generic point shock, self-similar | Buckmaster–Shkoller–Vicol 2022/2023 | Proven |
| Shock development, Minkowski, restricted (irrotational upstream) | Christodoulou 2019; Abbrescia–Speck on the crease/singular-boundary emergence | Proven / near-complete |
| Einstein-Euler with shocks, **spherical symmetry**, BV data | Groah–Temple 2004: global existence, metric $C^{0,1}$ | Proven |
| Einstein-Euler with shocks, **plane / $T^3$ Gowdy symmetry** | Barnes–LeFloch–Schmidt–Stewart 2004; LeFloch–Rendall 2011 | Proven |
| $1+1$ relativistic Euler, genuinely nonlinear EOS | Guo–Tahvildar-Zadeh 1999; Athanasiou–Zhu 2021: finite-time gradient blowup | Proven |
| Metric regularity at shocks | Reintjes–Temple: $C^{1,1}$ liftable in symmetric cases | Partially proven |
| **Full $3+1$ Einstein-Euler, no symmetry, shock formation + development** | — | **Open** |

## 5. Principal Obstacles

- **No fixed background.** Christodoulou's proof rests on constructing an eikonal function for the acoustical metric $h$ and controlling $\mu$ to top order. In Einstein-Euler, $h$ depends on $g$, which itself solves a wave system sourced by the fluid. One must run a *coupled* eikonal-plus-Bianchi hierarchy; the two null structures (acoustic and gravitational) are distinct and non-aligned.
- **Derivative loss in the eikonal.** The connection coefficients of the acoustical foliation are one derivative *less* regular than $\phi$; recovering that derivative requires a renormalized elliptic/Raychaudhuri argument. Coupling to gravity introduces the same loss on the metric side, and the two losses compound rather than cancel.
- **Gauge.** Harmonic (wave) coordinates are adapted to the light cone, not the sound cone. There is no known gauge simultaneously regular across the acoustic characteristic degeneracy and hyperbolic for Einstein's equations. A shock in the fluid feeds a $\delta$-type source into $\mathrm{Ric}$, so $g$ can be at best $C^{1,1}$; standard energy estimates for Einstein need $H^{s}$, $s > 5/2$.
- **Weak-solution theory absent above 1D.** Glimm's scheme, the only tool giving GR shock spacetimes, is intrinsically one-dimensional (BV compactness fails in $\ge 2$ space dimensions); it also gives no uniqueness and no control of the metric beyond Lipschitz.
- **Vorticity and entropy.** Post-shock flow is rotational and non-isentropic even if the upstream flow was not, so any development theorem must handle the full Euler system, where the transport-div-curl structure is only barely compatible with the wave-equation estimates (Disconzi–Speck null structures are the current best handle).
- **Constraint propagation.** The Einstein constraint equations must be preserved across a discontinuity; verifying this for a $C^{0,1}$ metric requires a distributional formulation in which products like $\Gamma \cdot \Gamma$ are not classically defined.

## 6. The Gap

Everything proven splits into two disjoint camps: (i) **sharp shock analysis with no gravity** (Christodoulou, Luk–Speck, BSV) and (ii) **gravity with shocks but under symmetry and only in BV** (Groah–Temple, LeFloch–Rendall). The gap is the union: a theorem valid in $3+1$ dimensions, with no symmetry, in which the metric is dynamical and the singularity is resolved geometrically rather than via BV compactness.

Concretely, the missing step is a **coupled acoustical–gravitational energy estimate**: construct an eikonal function $\vartheta$ for $h[g,u]$ and a gauge for $g$ such that the top-order energies $\mathbb{E}_N$ obey $\mathbb{E}_N \lesssim \mu_\star^{-c}$ with $c$ *independent* of the gravitational coupling, and such that $\mu_\star \to 0$ occurs strictly before any curvature blowup. No one has produced even a formal hierarchy with a closed $\mu$-dependence in the coupled setting.

## 7. Current Research (as of June 2026)

- **Vanderbilt (Disconzi) / MIT (Speck) school:** relativistic Euler with vorticity and entropy, low-regularity local well-posedness at $H^{2+}$, and the geometry of the singular boundary (Abbrescia–Speck crease results). Extension of the Disconzi–Speck null-structure framework to a curved, dynamical background is the stated target. *(frontier — verify)*
- **Monash (Oliynyk) / AEI:** relativistic liquid bodies with free boundary, Fuchsian methods for cosmological Einstein-Euler; used to control the fluid–vacuum interface that a shock would strike.
- **Sorbonne (LeFloch):** weak-solution GR, "bounded variation spacetimes", and the Einstein-Euler Cauchy problem for low-regularity metrics; continued work on symmetric global foliations.
- **Reintjes–Temple RT-equation program:** proving optimal metric regularity ($C^{0,1} \to C^{1,1}$) by solving an elliptic system for the coordinate transformation, in $L^p$. If completed without symmetry, it settles layer 3 of the problem. *(frontier — verify)*
- **Princeton/NYU (Buckmaster, Shkoller, Vicol) self-similar methods:** stable point shocks and shock development for Euler; a relativistic version exists in the non-gravitational case, and the modulation approach is being probed as an alternative to eikonal geometry for coupled systems. *(frontier — verify)*

## 8. Future Work

- Prove shock formation for Einstein-Euler in **spherical symmetry with a dynamical metric and no BV limitation**, using the acoustical eikonal directly. This is the smallest genuinely coupled case.
- Develop a **double-null / double-cone gauge** foliating spacetime simultaneously by gravitational and acoustical null cones, so that $\mu$ and the metric's null connection are estimated in the same hierarchy.
- Establish the **relativistic shock development problem** in Minkowski with vorticity and entropy (Christodoulou 2019 is restricted); then couple.
- Settle whether a shock can seed a curvature singularity: does $[\![ \mathrm{Riem} ]\!] \in L^\infty$ always, or can shock-interaction points be genuine singularities? Reintjes–Temple predict no.
- Numerical relativity input: high-resolution shock-capturing simulations of neutron-star mergers exhibit exactly this regime and can suggest, though not prove, the shape of the singular boundary.

## 9. Key References

- **[Foundational]** D. Christodoulou. *The Formation of Shocks in 3-Dimensional Fluids.* EMS Monographs in Mathematics, European Mathematical Society, 2007.
- **[Foundational]** D. Christodoulou, S. Miao. *Compressible Flow and Euler's Equations.* Surveys of Modern Mathematics 9, International Press, 2014.
- **[Foundational]** D. Christodoulou. *The Shock Development Problem.* EMS Monographs in Mathematics, European Mathematical Society, 2019.
- **[Foundational]** A. D. Rendall. *The initial value problem for a class of general relativistic fluid bodies.* Journal of Mathematical Physics 33 (1992), 1047–1053.
- **[Foundational]** Y. Choquet-Bruhat. *General Relativity and the Einstein Equations.* Oxford University Press, 2009.
- **[SOTA / Recent]** J. Luk, J. Speck. *Shock formation in solutions to the 2D compressible Euler equations in the presence of non-zero vorticity.* Inventiones Mathematicae 214 (2018), 1–169.
- **[SOTA / Recent]** M. M. Disconzi, J. Speck. *The relativistic Euler equations: Remarkable null structures and regularity properties.* Annales Henri Poincaré 20 (2019), 2173–2270.
- **[SOTA / Recent]** T. Buckmaster, S. Shkoller, V. Vicol. *Formation of point shocks for 3D compressible Euler.* Communications on Pure and Applied Mathematics 76 (2023), 2073–2191.
- **[SOTA / Recent]** S. Miao, P. Yu. *On the formation of shocks for quasilinear wave equations.* Inventiones Mathematicae 207 (2017), 697–831.
- **[SOTA / Recent]** M. M. Disconzi, C. Luo, G. Mazzone, J. Speck. *Rough sound waves in 3D compressible Euler flow with vorticity.* Selecta Mathematica 28 (2022), Article 41.
- **[SOTA / Recent]** L. Abbrescia, J. Speck. *The emergence of the singular boundary from the crease in 3D compressible Euler flow.* arXiv:2207.07107, 2022.
- **[SOTA / Recent]** J. Groah, B. Temple. *Shock-Wave Solutions of the Einstein Equations with Perfect Fluid Sources: Existence and Consistency by a Locally Inertial Glimm Scheme.* Memoirs of the American Mathematical Society 172, no. 813, 2004.
- **[SOTA / Recent]** P. G. LeFloch, A. D. Rendall. *A global foliation of Einstein-Euler spacetimes with Gowdy-symmetry on $T^3$.* Archive for Rational Mechanics and Analysis 201 (2011), 841–870.
- **[SOTA / Recent]** A. Barnes, P. G. LeFloch, B. G. Schmidt, J. M. Stewart. *The Glimm scheme for perfect fluids on plane-symmetric Gowdy spacetimes.* Classical and Quantum Gravity 21 (2004), 5043–5074.
- **[SOTA / Recent]** M. Reintjes, B. Temple. *Points of general relativistic shock wave interaction are "regularity singularities" where space-time is not locally flat.* Proceedings of the Royal Society A 471 (2015), 20140834.
- **[SOTA / Recent]** N. Athanasiou, S. Zhu. *Formation of singularities for the relativistic Euler equations.* Journal of Differential Equations 284 (2021), 284–317.
- **[Survey]** J. Speck. *Shock Formation in Small-Data Solutions to 3D Quasilinear Wave Equations.* Mathematical Surveys and Monographs 214, American Mathematical Society, 2016.
- **[Survey]** J. Smoller, B. Temple. *Global solutions of the relativistic Euler equations.* Communications in Mathematical Physics 156 (1993), 67–99.
- **[Survey]** T. A. Oliynyk. *A priori estimates for relativistic liquid bodies.* Bulletin des Sciences Mathématiques 141 (2017), 105–222.

## 10. Worked Example / Concrete Special Case

**Plane-symmetric radiation fluid: explicit shock time, then the gravitational correction.**

Take $p = c_s^2 \rho$ with $c_s^2 = 1/3$ (radiation), $v = \tanh\theta$, and flow depending on $(t,x)$ only. On Minkowski space the system diagonalizes in the Riemann invariants of §2:

$$
\partial_t J_\pm + \lambda_\pm \,\partial_x J_\pm = 0, \qquad \lambda_\pm = \tanh(\theta \pm \theta_s), \quad \theta = \tfrac12 (J_+ + J_-).
$$

**Simple wave.** Choose data with $J_-(0,x) \equiv 0$, so $J_- \equiv 0$ everywhere and $\theta = J_+/2$. Then $\lambda_+ = \tanh(\tfrac12 J_+ + \theta_s)$ is a function of $J_+$ alone, and

$$
\frac{d\lambda_+}{dJ_+} = \tfrac12\,\mathrm{sech}^2(\theta + \theta_s) > 0 ,
$$

so the $+$-family is genuinely nonlinear. Setting $w = \partial_x J_+$ and differentiating the transport equation:

$$
\frac{Dw}{Dt} = -\frac{d\lambda_+}{dJ_+}\, w^2 \quad\Longrightarrow\quad w(t) = \frac{w_0}{1 + t\,(d\lambda_+/dJ_+)\,w_0}.
$$

**Numbers.** Since $\tanh\theta_s = c_s = 1/\sqrt3$, $\cosh\theta_s = (1-c_s^2)^{-1/2} = \sqrt{3/2} = 1.2247$, so $\mathrm{sech}^2\theta_s = 2/3$. Take initial data $J_+(0,x) = -\varepsilon \sin x$, $\varepsilon \ll 1$. At $x = 0$: $\theta = 0$, $w_0 = -\varepsilon$, and $d\lambda_+/dJ_+ = \tfrac12 \cdot \tfrac23 = \tfrac13$. Hence

$$
T_\star = \frac{1}{-w_0\,(d\lambda_+/dJ_+)} = \frac{3}{\varepsilon}.
$$

At $t = T_\star$, $|\partial_x J_+| \to \infty$ while $|J_+| \le \varepsilon$ stays bounded — density, velocity and pressure remain small and bounded; only their gradients blow up. Equivalently $\mu \to 0$: the $+$-characteristics emanating from $x \in (-\delta,\delta)$ focus into a single point. For $\varepsilon = 10^{-2}$ the shock forms at $T_\star = 300$ in units where $c = 1$.

**Adding gravity.** In plane symmetry write $g = -N^2 dt^2 + a^2 dx^2 + b^2(dy^2 + dz^2)$. The characteristic speeds become $\lambda_\pm^{(g)} = (N/a)\tanh(\theta \pm \theta_s)$, and the transport equations acquire source terms proportional to the expansion $\partial_t \ln b$ and to $\partial_x \ln N$ (which the momentum constraint ties to the fluid's own energy density). The Riccati equation for $w$ becomes

$$
\frac{Dw}{Dt} = -\frac{N}{a}\frac{d\lambda_+}{dJ_+}w^2 + \Big(\text{terms linear in } w \text{ with coefficient } O(\sqrt{8\pi\rho})\Big).
$$

For $8\pi \rho \ll \varepsilon^2$, the quadratic term dominates and the shock time is $T_\star = 3/\varepsilon \cdot (1 + O(\sqrt{\rho}/\varepsilon))$: gravity perturbs but does not prevent shock formation. **What the example does not give**, and what makes the general problem open: this argument is one-dimensional and uses BV/characteristic bookkeeping unavailable in $3+1$; and once $w \to \infty$, the metric functions $N, a, b$ are only $C^{0,1}$ in $x$, so the Einstein evolution equations hold only distributionally and there is no theorem asserting the continuation is unique.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*