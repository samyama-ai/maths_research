---
id: 06-pdes/benjamin-bona-mahony-asymptotics
title: "Benjamin-Bona-Mahony Long Time Asymptotics"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Benjamin-Bona-Mahony Long Time Asymptotics

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/benjamin-bona-mahony-asymptotics` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Benjamin–Bona–Mahony (BBM), or regularized long-wave, equation on the line,

$$u_t + u_x + u u_x - u_{xxt} = 0, \qquad (x,t)\in\mathbb{R}\times\mathbb{R}_{+},\qquad u(\cdot,0)=u_0\in H^1(\mathbb{R}).$$

**Problem.** Describe the behaviour of $u(t)$ as $t\to+\infty$ for general $H^1$ data. The expected picture (BBM soliton resolution) is:

> **Conjecture.** For every $u_0\in H^1(\mathbb{R})$ there exist $N\in\mathbb{N}_{\ge0}$, speeds $c_1>\dots>c_N>1$ and shifts $x_j(t)=c_jt+o(t)$ such that
> $$u(t) \;=\; \sum_{j=1}^{N}\phi_{c_j}\big(\cdot-x_j(t)\big) \;+\; \eta(t),$$
> where $\phi_c$ is the BBM solitary wave and the remainder $\eta(t)$ **converges to $0$ locally**: $\|\eta(t)\|_{H^1(|x|\le R + \varepsilon t)}\to0$ for every $R>0$ and small $\varepsilon>0$.

Two features make the statement different from KdV-type resolution and are part of what must be proved or disproved:

1. **No scattering in the usual sense.** $\|u(t)\|_{H^1}$ is exactly conserved, and the linear BBM group is unitary on $H^1$, so no global energy decay is available; only *local* decay can hold.
2. **The radiation need not be asymptotically linear.** It is open whether $\eta$ behaves like a solution of the linear BBM equation, and whether the residual high-frequency energy stays trapped near a fixed region.

A complete resolution means: a proof of the decomposition above (with a rate for $\eta$), or a counterexample — e.g. an $H^1$ solution whose local $H^1$ norm does not converge along any subsequence to a finite sum of solitary waves.

## 2. Mathematical Foundations

**Formulation.** BBM is a nonlocal transport equation. With $\Lambda^{-2}:=(1-\partial_x^2)^{-1}$, which has kernel $\tfrac12 e^{-|x|}$,

$$u_t \;=\; -\,\partial_x\,\Lambda^{-2}\!\Big(u+\tfrac12u^2\Big).$$

Since $\partial_x\Lambda^{-2}$ is bounded on $H^s$ for every $s$, BBM is a bounded perturbation of an ODE in $H^s$, $s\ge 0$; global well-posedness in $H^1$ is classical (Benjamin–Bona–Mahony 1972), sharp well-posedness in $H^s$ for $s\ge0$ and ill-posedness for $s<0$ are due to Bona–Tzvetkov (2009).

**Linear symbol and dispersion.** The linear part has phase $\omega(\xi)=\dfrac{\xi}{1+\xi^{2}}$, so $e^{tL}$ has symbol $e^{-it\omega(\xi)}$ and is unitary on every $H^s$. The group velocity is

$$\omega'(\xi)=\frac{1-\xi^{2}}{(1+\xi^{2})^{2}},\qquad \omega''(\xi)=\frac{2\xi^{3}-6\xi}{(1+\xi^{2})^{3}} .$$

Thus $\omega'$ takes values only in $[-\tfrac18,\,1]$, $\omega''$ vanishes at $\xi=0,\pm\sqrt3$ (degenerate stationary phase), and — decisively — $\omega'(\xi)=O(|\xi|^{-2})$ as $|\xi|\to\infty$. Dispersion **degenerates at high frequency**, the opposite of KdV where $\omega_{\mathrm{KdV}}'(\xi)\sim-3\xi^{2}$.

**Conservation laws.** BBM conserves
$$I_1=\int u\,dx,\qquad I_2=\int (u^{2}+u_x^{2})\,dx=\|u\|_{H^1}^2,\qquad I_3=\int (u^{3}+3u^{2})\,dx .$$
Olver (1979) proved these are the **only** nontrivial polynomial conservation laws: BBM is not integrable and admits no inverse-scattering transform.

**Solitary waves.** For each $c>1$,
$$\phi_c(y)=3(c-1)\,\operatorname{sech}^{2}\!\Big(\tfrac12\sqrt{\tfrac{c-1}{c}}\;y\Big),\qquad u(x,t)=\phi_c(x-ct),$$
obtained from $(1-c)\phi+\tfrac12\phi^{2}+c\phi''=0$. These are orbitally stable in $H^1$ for all $c>1$ (Benjamin 1972; Bona 1975; Grillakis–Shatah–Strauss theory), with $\tfrac{d}{dc}\!\int\phi_c^2>0$.

## 3. History & State of the Art (SOTA)

- **1966.** Peregrine introduces the regularized long-wave equation to model an undular bore (*J. Fluid Mech.* 25, 321–330).
- **1972.** Benjamin, Bona and Mahony propose it as an alternative to KdV: same formal accuracy at the Boussinesq order, but well-posed and numerically stable because $\Lambda^{-2}$ damps high frequencies (*Phil. Trans. R. Soc. A* 272).
- **1979–1980.** Olver shows only three conservation laws exist; Bona–Pritchard–Scott compute two-solitary-wave collisions numerically and find them **inelastic**, with a small residual tail — first quantitative evidence that BBM is not integrable and that resolution must include radiation.
- **1986–1989.** Albert obtains local decay for small-energy generalized BBM; Amick–Bona–Schonbek settle the **dissipative** analogue $u_t+u_x+uu_x-u_{xxt}=\nu u_{xx}$ with sharp $L^2$ rate $t^{-1/4}$ and diffusion-wave asymptotics.
- **1996.** Miller–Weinstein prove **asymptotic stability** of BBM solitary waves in an exponentially weighted space, for speeds $c$ near $1$.
- **2004–2005.** El Dika, and El Dika–Martel, transport the Martel–Merle monotonicity/Liouville machinery to BBM: asymptotic stability of a single solitary wave and of well-separated $N$-solitary-wave configurations in $H^1$, with local convergence in a moving window.
- **2009.** Bona–Tzvetkov fix the sharp well-posedness threshold $s=0$.
- **2019–present.** Kwak–Muñoz and collaborators develop virial/Morawetz methods giving decay of *small* solutions in expanding regions for generalized BBM and related weakly dispersive Boussinesq (abcd) systems.

State of the art: **local** asymptotics near solitary waves and for small data are known; **global** soliton resolution for arbitrary $H^1$ data is open.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| $c>1$, single solitary wave, $H^1$ perturbation | Orbital stability for all $c>1$ (Benjamin 1972, Bona 1975); asymptotic stability in the moving frame, $u(t)-\phi_{c^+}(\cdot-x(t))\rightharpoonup0$ in $H^1(x>\varepsilon t)$ (El Dika 2005) |
| $c\to1^{+}$ (KdV scaling limit), exponentially weighted data $e^{ax}u\in L^2$ | Full asymptotic stability with exponential local rate (Miller–Weinstein, *CPAM* 49, 1996) |
| $N$ solitary waves, speeds $1<c_1<\dots<c_N$ well separated, small $H^1$ perturbation | Stability and asymptotic stability of the $N$-wave configuration (El Dika–Martel 2004) |
| Small $H^1$ data, generalized BBM $u_t+u_x+(u^{p})_x-u_{xxt}=0$, $p\ge2$ | Decay to $0$ in $L^2_{loc}$ of expanding intervals $|x|\lesssim t^{\theta}$, $\theta<1$, by virial estimates (Kwak–Muñoz 2019) |
| Dissipative BBM–Burgers, $u_0\in L^1\cap H^1$ | Complete asymptotics: $\|u(t)\|_{L^2}\simeq C t^{-1/4}$, $\|u(t)\|_{L^\infty}\simeq Ct^{-1/2}$, leading profile a self-similar diffusion wave (Amick–Bona–Schonbek 1989) |
| Linear BBM, data with $\hat u_0$ compactly supported away from $\infty$ | Stationary-phase decay $\|e^{tL}u_0\|_{L^\infty}=O(t^{-1/3})$ (degenerate point $\xi=\pm\sqrt3$) |
| Numerics | Inelastic $2$-soliton collisions with residual tail of relative size $\sim10^{-3}$–$10^{-4}$ in amplitude (Bona–Pritchard–Scott 1980); large-data simulations consistently show resolution into solitary waves plus slowly dispersing rear radiation |

## 5. Principal Obstacles

- **Degenerate high-frequency dispersion.** Because $\omega'(\xi)=O(\xi^{-2})$, a wave packet localized at frequency $N$ moves at speed $\sim N^{-2}$ and needs time $\sim N^{2}$ to leave a unit interval. No local smoothing or Strichartz estimate holds uniformly in frequency; every local decay estimate must pay derivatives, so $H^1$ data — the natural energy class — sits exactly at the threshold where the loss is unaffordable.
- **No dispersive decay at the level of the energy norm.** $\|u(t)\|_{H^1}$ is exactly conserved, so the standard "energy leaks to infinity" mechanism is unavailable. One can only hope to prove weak convergence to $0$ locally, which requires rigidity, not estimates.
- **Non-integrability.** Olver's theorem rules out inverse scattering, Lax pairs, or Riemann–Hilbert asymptotics — the tools that give complete long-time asymptotics for KdV and mKdV.
- **Virial/Morawetz weights fail.** Martel–Merle-type monotonicity for gKdV uses that $\partial_x^3$ produces a positive commutator with a monotone weight. For BBM, the commutator of $\partial_x\Lambda^{-2}$ with a weight $\chi(x/A)$ is a *nonlocal* operator whose positivity holds only after high frequencies are cut off; the discarded piece is not small in $H^1$.
- **No Liouville theorem outside the soliton neighbourhood.** El Dika's rigidity argument uses closeness to $\phi_c$ from the start; for general data there is no compactness mechanism forcing the limiting object to be a solitary wave.
- **Possible trapped high-frequency modes.** Nothing currently excludes solutions carrying a bounded, non-decaying amount of $H^1$ energy at frequencies $\to\infty$ near a fixed spatial region — a "frozen" residue that would falsify the conjecture as stated.

## 6. The Gap

Proven: local asymptotic stability *of* solitary-wave configurations, i.e. resolution for data already in a small $H^1$ neighbourhood of $\sum_j\phi_{c_j}$, plus local decay for small data. Conjectured: resolution for *all* $H^1$ data.

The exact missing step is a **global rigidity / no-trapping theorem**: show that for any $u_0\in H^1$, the weak limits of $u(t_n,\cdot+x_n)$ along arbitrary sequences $t_n\to\infty$ are either $0$ or solitary waves. Equivalently, prove a local energy-decay statement of the form
$$\int_{|x-vt|\le R}\big(\eta^2+\eta_x^2\big)(x,t)\,dx\;\longrightarrow\;0\qquad (t\to\infty)$$
for the non-soliton part $\eta$, **uniformly over frequency**, i.e. without a $\|u_0\|_{H^s}$, $s>1$, on the right-hand side. Every existing argument either restricts to a moving window where the nonlinearity is small, or spends $\varepsilon$ derivatives that $H^1$ data do not have.

## 7. Current Research (as of June 2026)

- **Virial/Morawetz school (Muñoz, Kwak, Poblete, Pozo; Universidad de Chile, CNRS).** Transported-virial functionals adapted to $\Lambda^{-2}$, giving decay in expanding regions $|x|\le t^{\theta}$ for small data of generalized BBM and Hamiltonian abcd Boussinesq systems. Extension to $\theta=1$ and to large data is the active target. *(frontier — verify)*
- **Martel–Merle-type rigidity beyond the soliton tube (France/Chile).** Attempts to combine monotonicity of localized mass with the conserved $I_3$ to exclude non-soliton compact limits. *(frontier — verify)*
- **Weighted-space asymptotic stability at general $c$.** Extending Miller–Weinstein beyond $c\approx1$ requires spectral control of the linearized BBM operator uniformly in $c$; partial resolvent estimates exist. *(frontier — verify)*
- **High-accuracy numerics.** Spectral simulations quantifying the residual tail of BBM collisions and the persistence time of high-frequency packets, used to test whether trapped modes exist.
- **Comparison/model-validity programme.** Continuing the Bona–Pritchard–Scott line: how BBM asymptotics differ from KdV asymptotics on the physically relevant time scale $t\sim\varepsilon^{-3/2}$, and whether the divergence is caused precisely by the degenerate high-frequency regime.

## 8. Future Work

1. **Frequency-localized virial identities.** Build a Morawetz weight adapted to the group velocity map $\xi\mapsto\omega'(\xi)$, so that the positivity of the commutator survives at frequency $N$ with constant $\sim N^{-2}$, and sum dyadically against the conserved $I_2$.
2. **Prove or disprove trapped high-frequency modes.** Construct an $H^1$ solution with $\liminf_t\|u(t)\|_{H^1(|x|\le1)}>0$ and no solitary-wave component — or exclude it. This is the sharpest binary question in the area.
3. **Kink/front asymptotics.** Analyse data with distinct limits at $\pm\infty$ (Peregrine's undular bore), where the conjecture must be restated in terms of a dispersive shock.
4. **Uniform-in-$c$ linearized spectral theory** for $L_c=\partial_x\Lambda^{-2}(1+\phi_c)-c\partial_x$, including absence of embedded eigenvalues and resonances, which would upgrade El Dika's weak convergence to a rate.
5. **Generalized BBM $u^pu_x$.** Determine whether resolution is easier for $p\ge2$ (better nonlinear decay) and whether instability of solitary waves for large $p$ (Souganidis–Strauss) produces new asymptotic regimes.

## 9. Key References

- **[Foundational]** T. B. Benjamin, J. L. Bona, J. J. Mahony. *Model equations for long waves in nonlinear dispersive systems.* Philosophical Transactions of the Royal Society of London A **272** (1972), 47–78.
- **[Foundational]** D. H. Peregrine. *Calculations of the development of an undular bore.* Journal of Fluid Mechanics **25** (1966), 321–330. [DOI](https://doi.org/10.1017/s0022112066001678)
- **[Structure]** P. J. Olver. *Euler operators and conservation laws of the BBM equation.* Mathematical Proceedings of the Cambridge Philosophical Society **85** (1979), 143–160. [DOI](https://doi.org/10.1017/s0305004100055572)
- **[Stability]** T. B. Benjamin. *The stability of solitary waves.* Proceedings of the Royal Society of London A **328** (1972), 153–183.
- **[Stability]** J. L. Bona. *On the stability theory of solitary waves.* Proceedings of the Royal Society of London A **344** (1975), 363–374.
- **[SOTA]** J. R. Miller, M. I. Weinstein. *Asymptotic stability of solitary waves for the regularized long-wave equation.* Communications on Pure and Applied Mathematics **49** (1996), 399–441. [DOI](https://doi.org/10.1002/(sici)1097-0312(199604)49:4<399::aid-cpa4>3.0.co;2-7)
- **[SOTA]** K. El Dika. *Asymptotic stability of solitary waves for the Benjamin–Bona–Mahony equation.* Discrete and Continuous Dynamical Systems **13** (2005), 583–622. [DOI](https://doi.org/10.3934/dcds.2005.13.583)
- **[SOTA]** K. El Dika, Y. Martel. *Stability of N solitary waves for the generalized BBM equations.* Dynamics of PDE **1** (2004), 401–437. [DOI](https://doi.org/10.4310/dpde.2004.v1.n4.a3)
- **[Dissipative case]** C. J. Amick, J. L. Bona, M. E. Schonbek. *Decay of solutions of some nonlinear wave equations.* Journal of Differential Equations **81** (1989), 1–49. [DOI](https://doi.org/10.1016/0022-0396(89)90176-9)
- **[Decay]** J. P. Albert. *Dispersion of low-energy waves for the generalized Benjamin–Bona–Mahony equation.* Journal of Differential Equations **63** (1986), 117–134. [DOI](https://doi.org/10.1016/0022-0396(86)90057-4)
- **[Well-posedness]** J. L. Bona, N. Tzvetkov. *Sharp well-posedness results for the BBM equation.* Discrete and Continuous Dynamical Systems **23** (2009), 1241–1252. [DOI](https://doi.org/10.3934/dcds.2009.23.1241)
- **[Instability]** P. E. Souganidis, W. A. Strauss. *Instability of a class of dispersive solitary waves.* Proceedings of the Royal Society of Edinburgh A **114** (1990), 195–212. [DOI](https://doi.org/10.1016/s0198-0254(06)80202-5)
- **[Recent]** C. Kwak, C. Muñoz. *Extended decay properties for generalized BBM equation.* Fields Institute Communications **83** (2019), 397–411. [DOI](https://doi.org/10.1007/978-1-4939-9806-7_8)
- **[Numerics / model validity]** J. L. Bona, W. G. Pritchard, L. R. Scott. *An evaluation of a model equation for water waves.* Philosophical Transactions of the Royal Society of London A **302** (1981), 457–510.
- **[Method, comparison]** Y. Martel, F. Merle. *Asymptotic stability of solitons for subcritical generalized KdV equations.* Archive for Rational Mechanics and Analysis **157** (2001), 219–254. [DOI](https://doi.org/10.1007/s002050100138)

## 10. Worked Example / Concrete Special Case

**Linear BBM: where decay comes from, and where it fails.**

Take $u_t+u_x-u_{xxt}=0$, so $\hat u(\xi,t)=e^{-it\omega(\xi)}\hat u_0(\xi)$, $\omega(\xi)=\xi/(1+\xi^2)$, and
$$u(x,t)=\frac{1}{2\pi}\int_{\mathbb R}e^{i t\,\varphi(\xi)}\hat u_0(\xi)\,d\xi,\qquad \varphi(\xi)=\xi\tfrac{x}{t}-\omega(\xi).$$

*(a) Interior of the light cone.* Stationary points solve $\omega'(\xi)=x/t$. Since $\omega'$ ranges over $[-\tfrac18,1]$, for $x/t\notin[-\tfrac18,1]$ there is no real stationary point and $u$ decays faster than any power on that ray. On the two degenerate rays we have $\omega''(\pm\sqrt3)=0$: at $\xi=\sqrt3$, $\omega'(\sqrt3)=(1-3)/16=-\tfrac18$, and $\omega'''(\sqrt3)\ne0$, so the Airy-type stationary phase gives on the ray $x=-t/8$

$$|u(x,t)| \;\lesssim\; t^{-1/3}\,\|\hat u_0\|_{L^\infty(\text{near }\sqrt3)} ,$$

the best power available anywhere. At $\xi=0$ (also $\omega''=0$, $\omega'(0)=1$) the same $t^{-1/3}$ appears on the ray $x=t$.

*(b) The obstruction.* Take $\hat u_0$ supported in $\xi\in[N,2N]$ with $\|u_0\|_{L^2}=1$, spatially concentrated in $|x|\le1$. On that band
$$\omega'(\xi)=\frac{1-\xi^2}{(1+\xi^2)^2}\;=\;-\frac{1}{\xi^{2}}+O(\xi^{-4}),\qquad \text{so}\quad \omega'\in\big[-N^{-2},\,-\tfrac14N^{-2}\big]+O(N^{-4}).$$
The packet drifts at speed $\le N^{-2}$ and its internal spread of velocities is $\tfrac34N^{-2}$. Hence for all $t\le \tfrac{1}{2}N^{2}$ the packet is still essentially inside $|x|\le 2$:
$$\int_{|x|\le 2}|u(x,t)|^{2}dx\;\ge\;\tfrac12\qquad\text{for }0\le t\le \tfrac12 N^{2}.$$
Letting $N\to\infty$ shows there is **no** estimate $\|u(t)\|_{L^2(|x|\le2)}\le C\,g(t)\|u_0\|_{L^2}$ with $g(t)\to0$. Any local decay must lose derivatives; matching the two computations, a rate $t^{-\alpha}$ costs roughly $2\alpha$ derivatives, so $H^1$ data buys at best $\alpha\approx\tfrac12$ and only after the nonlinearity is controlled.

*(c) Nonlinear consequence.* Add the solitary wave $\phi_c$, $c=2$: $\phi_2(y)=3\operatorname{sech}^{2}(y/(2\sqrt2))$, amplitude $3$, speed $2$, so it exits the group-velocity cone $[-\tfrac18,1]$ and separates from all linear radiation at rate $\ge t$. This separation is exactly what El Dika's proof exploits, and it is why one solitary wave is tractable. The conjecture in Section 1 asks for the same conclusion when the leftover field $\eta$ is *not* small — and part (b) is the precise reason no existing estimate delivers it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*