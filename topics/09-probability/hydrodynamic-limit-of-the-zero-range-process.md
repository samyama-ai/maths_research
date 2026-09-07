---
id: 09-probability/hydrodynamic-limit-of-the-zero-range-process
title: "Hydrodynamic Limit of the Zero-Range Process"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hydrodynamic Limit of the Zero-Range Process

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/hydrodynamic-limit-of-the-zero-range-process` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The zero-range process (ZRP) is an interacting particle system on a lattice in which each site $x$ holds $\eta_x \in \mathbb{N}$ particles and emits one particle at rate $g(\eta_x)$, depending only on the occupation of the departure site. The **hydrodynamic limit** problem asks: under diffusive scaling (symmetric jumps) or Euler scaling (asymmetric jumps), does the empirical density field converge in probability to the solution of a deterministic PDE, and is that PDE

$$\partial_t \rho = \Delta \Phi(\rho) \qquad\text{(symmetric)}, \qquad \partial_t \rho + \nabla\cdot\big(m\,\Phi(\rho)\big) = 0 \qquad\text{(asymmetric)},$$

where $\Phi$ is the mean-jump-rate function determined by the invariant product measures and $m$ is the drift of the jump kernel?

A complete solution requires: (i) identification of $\Phi$; (ii) a law of large numbers for the empirical measure $\pi^N_t = N^{-d}\sum_x \eta_{x}(tN^2)\,\delta_{x/N}$ valid for all initial profiles in a natural class; (iii) uniqueness of the limiting PDE in the relevant weak/entropy class.

For **Lipschitz, non-decreasing** $g$ the problem is *solved* (Rezakhanlou 1991; Kipnis–Landim 1999). It remains **open** in the following regimes, which is why the page is not marked closed:

- $g$ **sublinear and decreasing to a limit**, e.g. $g(k)=1+b/k^{\gamma}$, where the invariant measures have a *critical density* $\rho_c<\infty$ and **condensation** occurs. The conjectured hydrodynamic equation is $\partial_t\rho=\Delta\Phi(\rho)$ with the *flat* extension $\Phi(\rho)=\Phi(\rho_c)$ for $\rho>\rho_c$ — a degenerate (fast-diffusion-with-plateau) equation. This is proved only for subcritical data.
- $g$ **superlinear / unbounded growth** without a Lipschitz bound, where the process may not even be well defined on $\mathbb{Z}^d$ for all configurations.
- **Asymmetric, non-attractive, $d\ge2$** dynamics, where entropy-solution uniqueness and the relative-entropy method both break down.

## 2. Mathematical Foundations

**State space.** Fix $d\ge1$ and a torus $\mathbb{T}^d_N=(\mathbb{Z}/N\mathbb{Z})^d$ (or $\mathbb{Z}^d$). Configurations $\eta=(\eta_x)_{x}\in\Omega_N=\mathbb{N}^{\mathbb{T}^d_N}$. Let $p(\cdot)$ be a finite-range irreducible probability kernel on $\mathbb{Z}^d$ with drift $m=\sum_z z\,p(z)$.

**Generator.** For $g:\mathbb{N}\to[0,\infty)$ with $g(0)=0$, $g(k)>0$ for $k\ge1$,

$$(L_N f)(\eta) \;=\; \sum_{x}\sum_{z} g(\eta_x)\,p(z)\,\big[f(\eta^{x,x+z}) - f(\eta)\big],$$

where $\eta^{x,y}$ moves one particle from $x$ to $y$. Andjel (1982) constructed the process on $\mathbb{Z}^d$ for $g$ with bounded increments, $\sup_k|g(k+1)-g(k)|<\infty$.

**Invariant measures.** Set $g(k)! = g(1)g(2)\cdots g(k)$, $g(0)!=1$. For fugacity $\varphi\ge0$ define the single-site law

$$\bar\nu_\varphi(\eta_0=k)=\frac{1}{Z(\varphi)}\frac{\varphi^k}{g(k)!},\qquad Z(\varphi)=\sum_{k\ge0}\frac{\varphi^k}{g(k)!},$$

and let $\nu_\varphi=\bigotimes_x\bar\nu_\varphi$ on $\Omega_N$. These are the translation-invariant stationary measures; they satisfy the defining identity

$$\mathbb{E}_{\nu_\varphi}\big[g(\eta_0)\big]=\varphi .$$

Let $\varphi_c=\big(\limsup_k (g(k)!)^{-1/k}\big)^{-1}$ be the radius of convergence and

$$R(\varphi)=\mathbb{E}_{\nu_\varphi}[\eta_0]=\varphi\,\partial_\varphi\log Z(\varphi),\qquad \rho_c=\lim_{\varphi\uparrow\varphi_c}R(\varphi)\in(0,\infty].$$

$R$ is strictly increasing; on $[0,\rho_c)$ define $\Phi=R^{-1}$, so $\Phi(\rho)$ is the mean jump rate at density $\rho$. If $\rho_c<\infty$ the family $\{\nu_\varphi\}$ does not reach densities above $\rho_c$: the excess mass condenses onto a single site.

**Hydrodynamic scaling.** For $p$ symmetric (mean zero), speed up time by $N^2$; the conjectured limit is the nonlinear heat equation $\partial_t\rho=\Delta\Phi(\rho)$, $\rho(0,\cdot)=\rho_0$. For $m\neq0$, speed up by $N$; the limit is the scalar conservation law $\partial_t\rho+m\cdot\nabla\Phi(\rho)=0$ in the sense of **Kružkov entropy solutions** — needed since $\Phi$ is nonlinear and shocks form in finite time.

**Structure exploited by proofs.** The ZRP is a *gradient* system: the instantaneous current across the bond $(x,x+z)$ is $g(\eta_x)$, a function of a single coordinate, so $W_{x,x+z}=\tau_x h - \tau_{x+z} h$ with $h(\eta)=g(\eta_0)$. Gradient structure removes the need for a non-gradient Varadhan-type decomposition. Attractiveness (monotone coupling preserving the partial order $\eta\le\xi$) holds **iff $g$ is non-decreasing**.

## 3. History & State of the Art (SOTA)

- **1970** — Spitzer introduces zero-range interaction in "Interaction of Markov processes", *Adv. Math.* 5.
- **1982** — Andjel, "Invariant measures for the zero range process", *Ann. Probab.* 10: existence on $\mathbb{Z}^d$ and full classification of extremal invariant measures.
- **1984** — Ferrari, Presutti, Vares and, independently, Andjel–Vares (*J. Stat. Phys.* 1987) obtain hydrodynamics for one-dimensional attractive ZRP by coupling/subadditivity.
- **1991** — **Rezakhanlou**, "Hydrodynamic limit for attractive particle systems on $\mathbb{Z}^d$", *Comm. Math. Phys.* 140: entropy-solution hydrodynamics for asymmetric attractive ZRP and exclusion in all dimensions. Landim (1991, *Ann. Probab.*) treats attractive asymmetric systems with general initial data.
- **1994–95** — Large deviations from the hydrodynamic limit: Benois, Kipnis, Landim, "Large deviations from the hydrodynamical limit of mean zero asymmetric attractive processes", *Stoch. Proc. Appl.* 55 (1995); Landim, *Ann. Probab.* 1992.
- **1999** — Kipnis & Landim, *Scaling Limits of Interacting Particle Systems*, Springer Grundlehren 320: the entropy method (Guo–Papanicolaou–Varadhan) and the relative-entropy method (Yau) applied to the ZRP; Chapter 5 gives the symmetric case under $g$ Lipschitz and non-decreasing.
- **2002** — Bahadoran, Guiol, Ravishankar, Saada, "A constructive approach to Euler hydrodynamics for attractive processes", *Ann. IHP Probab. Stat.* 38: removes finite-range/technical conditions; extended in later work to non-translation-invariant environments.
- **2003** — Grosskinsky, Schütz, Spohn, "Condensation in the zero range process: stationary and dynamical properties", *J. Stat. Phys.* 113: identifies condensation for $g(k)=1+b/k$ with $b>2$ and predicts the plateau hydrodynamics.
- **2012–17** — Metastability of the condensate: Beltrán & Landim, *PTRF* 152 (2012); Armendáriz, Grosskinsky, Loulakis, *PTRF* 169 (2017), condensate motion on the thermodynamic-limit timescale $N^{1+b}$ (in $d=1$ mean-field/reversible settings).
- **2015** — Stamatakis, "Hydrodynamic limit of mean zero condensing zero range processes with sub-critical initial profiles", *J. Stat. Phys.* 158: the sharpest general result in the condensing regime.
- **2014→** — Fluctuation theory: Gonçalves & Jara, "Nonlinear fluctuations of weakly asymmetric interacting particle systems", *Arch. Ration. Mech. Anal.* 212 (2014), deriving KPZ/energy-solution behaviour for weakly asymmetric ZRP.

## 4. Partial Results / Verified Cases

Solved, with explicit hypotheses:

| Regime | Hypotheses | Result |
|---|---|---|
| Symmetric, $d\ge1$ | $g$ non-decreasing, $\sup_k|g(k+1)-g(k)|<\infty$ (Lipschitz) | $\partial_t\rho=\Delta\Phi(\rho)$, weak solution unique; entropy method (Kipnis–Landim Ch. 5) |
| Mean-zero asymmetric, $d\ge1$ | same, plus $\sum z p(z)=0$ | same diffusive limit, with a symmetrized diffusivity |
| Asymmetric, $d\ge1$ | $g$ non-decreasing (attractive), finite range | Kružkov entropy solution of $\partial_t\rho+m\cdot\nabla\Phi(\rho)=0$ (Rezakhanlou 1991; Landim 1991) |
| Constant rate $g\equiv 1_{k\ge1}$, $d=1$, totally asymmetric | — | $\Phi(\rho)=\rho/(1+\rho)$; equivalent to TASEP via the height/ gap mapping; sharp shock and rarefaction results |
| Smooth data, any $\Phi\in C^2$ | $\rho_0$ smooth, bounded away from $0$ and $\rho_c$ | Yau's relative-entropy method gives the limit up to the blow-up time of the PDE, with rate $o(N^{-1})$ in specific entropy |
| Condensing $g(k)=1+b/k$, $b>2$, mean zero | initial profile **strictly subcritical**: $\|\rho_0\|_\infty<\rho_c$ | Stamatakis (2015): $\partial_t\rho=\Delta\Phi(\rho)$ holds; requires $\Phi$ concave and control of the tail |
| Large deviations | $d=1$, attractive, mean zero | rate function of Freidlin–Wentzell type (Benois–Kipnis–Landim 1995) |
| Inhomogeneous rates | $g(k)$ site-dependent, totally asymmetric, $d=1$ | Landim (1996), *Ann. Probab.* 24: hydrodynamics with a spatially varying flux; condensation at slow sites |

## 5. Principal Obstacles

- **Loss of the one-block/two-block estimate above $\rho_c$.** The entropy method replaces $g(\eta_x)$ by $\Phi(\rho)$ using the local equilibrium of the canonical measures. When $\rho>\rho_c$, the canonical measure $\nu_{N,K}$ with $K/N^d>\rho_c$ is *not* asymptotically equivalent to any grand-canonical $\nu_\varphi$: it splits into a fluid part at $\rho_c$ plus one macroscopically occupied site (equivalence of ensembles fails; Großkinsky–Schütz–Spohn 2003; Armendáriz–Loulakis, *PTRF* 145, 2009). The two-block estimate, which is the heart of the method, therefore has no valid replacement statement.
- **Degenerate PDE.** With $\Phi$ constant on $[\rho_c,\infty)$ the equation $\partial_t\rho=\Delta\Phi(\rho)$ has no uniqueness theory in the class produced by the probabilistic estimates; a "Stefan-like" free boundary at $\{\rho=\rho_c\}$ appears, and the natural weak formulation loses information about the condensate mass.
- **Timescale separation.** The condensate moves on time scale $N^{1+b}$ (or $N^2\log N$ variants), far beyond diffusive $N^2$. So on the hydrodynamic scale the condensate is *frozen*, but its slow motion cannot be seen by the empirical measure — the correct limiting object may be a measure with atoms, not a function.
- **Non-attractive rates.** Rezakhanlou's proof for the Euler scaling uses coupling monotonicity to get the entropy inequalities. Without $g$ non-decreasing there is no order-preserving coupling; the only alternative, the relative-entropy method, fails at shocks.
- **Superlinear $g$.** Bounded increments is needed for non-explosion on $\mathbb{Z}^d$; for $g(k)\sim k^\alpha$, $\alpha>1$, the process can be non-unique, and moment bounds needed for tightness of $\pi^N$ are unavailable.

## 6. The Gap

The gap is sharp and can be stated in one line. For condensing $g$ with $\rho_c<\infty$:

> **Proven:** hydrodynamics for initial data with $\|\rho_0\|_\infty < \rho_c$ (subcritical).
> **Conjectured:** for arbitrary $\rho_0\in L^\infty$, possibly exceeding $\rho_c$, the empirical measure converges to the unique solution of $\partial_t\rho=\Delta\Phi(\rho)$ with $\Phi$ extended by $\Phi(\rho)=\varphi_c$ for $\rho\ge\rho_c$.

Crossing it requires an *equivalence-of-ensembles substitute at supercritical density*: a statement of the form
$$\lim_{k\to\infty}\lim_{N\to\infty}\ \mathbb{E}_{\mu_N}\Big|\frac{1}{|\Lambda_k|}\sum_{y\in\Lambda_k}\big(g(\eta_y)-\Phi(\rho^k_x)\big)\Big| = 0$$
that survives when $\rho^k_x>\rho_c$. Since the excess sits on $O(1)$ sites, the block average of $g$ still converges to $\varphi_c$ — the heuristic is correct — but no proof controls the fluctuation of the condensate location on the diffusive time scale.

## 7. Current Research (as of June 2026)

- **Condensing hydrodynamics beyond subcriticality.** Groups around Stamatakis (Athens), Grosskinsky (Augsburg), Loulakis and Armendáriz (Athens / Buenos Aires) pursue the supercritical case via a two-scale decomposition: fluid phase + point-mass condensate tracked as a separate measure-valued process. *(frontier — verify)* Preprints propose a limit in the space of finite measures where the condensate contributes a Dirac atom whose weight solves a mass-balance ODE coupled to the PDE.
- **Metastable condensate motion.** Beltrán–Landim martingale/trace-process approach and the Armendáriz–Grosskinsky–Loulakis thermodynamic-limit result are being pushed to $d\ge2$ and non-reversible kernels.
- **Fluctuations and KPZ.** Weakly asymmetric ZRP as a microscopic model for the KPZ equation via energy solutions (Gonçalves–Jara; Gubinelli–Perkowski uniqueness, *JAMS* 31, 2018). Open: KPZ fluctuations at criticality $\rho=\rho_c$.
- **Constructive / variational Euler hydrodynamics.** Bahadoran–Saada school (Clermont, Paris 13) extending Euler hydrodynamics to random environments and to non-translation-invariant condensing rates.
- **Non-attractive Euler limit.** Relative-entropy and $L^1$-stability approaches (following Jara–Menezes-type quantitative hydrodynamics) *(frontier — verify)*.

## 8. Future Work

- Prove or disprove the plateau equation $\partial_t\rho=\Delta\Phi(\rho)$, $\Phi\equiv\varphi_c$ on $[\rho_c,\infty)$, for supercritical initial data in $d=1$ first; the correct uniqueness class is likely that of entropy solutions of a degenerate parabolic equation (Carrillo-type).
- Develop a replacement lemma robust to atoms — plausibly via size-biased or "typical-configuration" decompositions of canonical measures rather than uniform relative-entropy bounds.
- Establish hydrodynamics for non-attractive $g$ under Euler scaling; this would also settle open cases for misanthrope processes.
- Extend quantitative rates (Jara–Menezes relative-entropy with rates) to condensing dynamics, giving error bounds in $N$ rather than bare convergence.
- Understand the joint scaling limit in which condensate motion and diffusive transport are visible simultaneously (a coupled PDE/jump-process limit).

## 9. Key References

- **[Foundational]** F. Spitzer. *Interaction of Markov processes.* Advances in Mathematics 5, 246–290, 1970.
- **[Foundational]** E. D. Andjel. *Invariant measures for the zero range process.* Annals of Probability 10(3), 525–547, 1982.
- **[Foundational]** F. Rezakhanlou. *Hydrodynamic limit for attractive particle systems on $\mathbb{Z}^d$.* Communications in Mathematical Physics 140(3), 417–448, 1991.
- **[Foundational]** C. Landim. *Hydrodynamical limit for asymmetric attractive particle systems on $\mathbb{Z}^d$.* Annales de l'IHP Probabilités et Statistiques 27, 559–581, 1991.
- **[Book / Survey]** C. Kipnis, C. Landim. *Scaling Limits of Interacting Particle Systems.* Grundlehren der mathematischen Wissenschaften 320, Springer, 1999.
- **[Book]** T. M. Liggett. *Interacting Particle Systems.* Springer, 1985 (reprinted 2005).
- **[SOTA]** S. Grosskinsky, G. M. Schütz, H. Spohn. *Condensation in the zero range process: stationary and dynamical properties.* Journal of Statistical Physics 113, 389–410, 2003.
- **[SOTA]** I. Armendáriz, M. Loulakis. *Thermodynamic limit for the invariant measures in supercritical zero range processes.* Probability Theory and Related Fields 145, 175–188, 2009.
- **[SOTA]** M. Stamatakis. *Hydrodynamic limit of mean zero condensing zero range processes with sub-critical initial profiles.* Journal of Statistical Physics 158, 87–104, 2015.
- **[SOTA]** I. Armendáriz, S. Grosskinsky, M. Loulakis. *Metastability in a condensing zero-range process in the thermodynamic limit.* Probability Theory and Related Fields 169, 105–175, 2017.
- **[SOTA]** J. Beltrán, C. Landim. *Metastability of reversible condensed zero range processes on a finite set.* Probability Theory and Related Fields 152, 781–807, 2012.
- **[SOTA]** C. Bahadoran, H. Guiol, K. Ravishankar, E. Saada. *A constructive approach to Euler hydrodynamics for attractive processes.* Annales de l'IHP Probabilités et Statistiques 38, 657–673, 2002.
- **[Fluctuations]** P. Gonçalves, M. Jara. *Nonlinear fluctuations of weakly asymmetric interacting particle systems.* Archive for Rational Mechanics and Analysis 212, 597–644, 2014.
- **[Large deviations]** O. Benois, C. Kipnis, C. Landim. *Large deviations from the hydrodynamical limit of mean zero asymmetric interacting particle systems.* Stochastic Processes and their Applications 55, 65–89, 1995.

## 10. Worked Example / Concrete Special Case

**Constant-rate, totally asymmetric ZRP in $d=1$.** Take $g(k)=\mathbf{1}\{k\ge1\}$ and $p(1)=1$, so $m=1$.

*Step 1 — invariant measures.* $g(k)!=1$ for all $k$, so $Z(\varphi)=\sum_{k\ge0}\varphi^k=(1-\varphi)^{-1}$ for $\varphi<1$, and $\bar\nu_\varphi(\eta_0=k)=(1-\varphi)\varphi^k$: geometric with parameter $\varphi$. Here $\varphi_c=1$.

*Step 2 — the flux.* $R(\varphi)=\mathbb{E}_{\nu_\varphi}[\eta_0]=\varphi/(1-\varphi)$, so $\rho_c=\lim_{\varphi\uparrow1}R(\varphi)=\infty$: **no condensation**. Inverting, $\Phi(\rho)=R^{-1}(\rho)=\rho/(1+\rho)$, which is exactly $\mathbb{P}_{\nu_\varphi}(\eta_0\ge1)$ — the fraction of occupied sites — as it must be, since a site emits at rate $1$ iff occupied.

*Step 3 — hydrodynamic equation.* Since $g$ is non-decreasing, Rezakhanlou's theorem applies with Euler scaling $t\mapsto tN$:

$$\partial_t\rho+\partial_x\!\left(\frac{\rho}{1+\rho}\right)=0,$$

with $\rho(t,\cdot)$ the unique Kružkov entropy solution. The flux $\Phi$ is strictly concave: $\Phi''(\rho)=-2(1+\rho)^{-3}<0$.

*Step 4 — a Riemann problem.* Start from a product measure with $\mathbb{E}[\eta_x]=\rho_-=1$ for $x<0$ and $\rho_+=3$ for $x\ge0$. Fluxes: $\Phi(1)=1/2$, $\Phi(3)=3/4$. Concave flux with $\rho_-<\rho_+$ gives a **shock**; Rankine–Hugoniot speed

$$v=\frac{\Phi(\rho_+)-\Phi(\rho_-)}{\rho_+-\rho_-}=\frac{3/4-1/2}{3-1}=\frac18,$$

matching the closed form $v=\big[(1+\rho_-)(1+\rho_+)\big]^{-1}=1/(2\cdot4)=1/8$. The Lax condition holds since $\Phi'(1)=1/4>1/8>\Phi'(3)=1/16$. So $\rho(t,x)=1$ for $x<t/8$ and $3$ for $x>t/8$: the microscopic density profile at time $tN$ has a sharp step travelling at macroscopic speed $1/8$.

*Step 5 — contrast with the open case.* Replace $g$ by $g(k)=1+b/k$ with $b=4$. Then $g(k)!=\prod_{j\le k}(1+4/j)\sim C k^{4}$, so $\bar\nu_1(\eta_0=k)\propto k^{-4}$ is summable with finite mean: $\varphi_c=1$ and

$$\rho_c=\frac{\sum_{k\ge1}k\cdot k^{-4}}{\sum_{k\ge0}(g(k)!)^{-1}}<\infty .$$

Now $\Phi$ is only defined on $[0,\rho_c)$ and saturates at $\varphi_c=1$. For $\rho_0<\rho_c$ everywhere, Stamatakis (2015) gives $\partial_t\rho=\Delta\Phi(\rho)$ under mean-zero jumps. For $\rho_0>\rho_c$ on a set of positive measure, no proof exists: this single change of $g$ from $1$ to $1+4/k$ moves the problem from textbook to open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*