---
id: 06-pdes/muskat-problem-singularities
title: "Muskat Problem Singularities"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Muskat Problem Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/muskat-problem-singularities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Muskat problem describes the interface between two immiscible incompressible fluids of different densities (and possibly viscosities) in a porous medium, evolving by Darcy's law. The central open question is a **global regularity vs. finite-time singularity dichotomy in the stable (Rayleigh–Taylor stable) regime**:

> **Conjecture (global regularity for stable graphs).** Let $f_0 \in H^s(\mathbb{R}^d)$, $s > 1 + d/2$, $d \in \{1,2\}$, describe an initial interface $\{y = f_0(x)\}$ with the denser fluid below. Then the Muskat solution exists for all $t>0$, remains a graph, and $\|f(t)\|_{H^s} \to 0$.

The conjecture is **false as stated without a slope restriction** for the *interface* problem: Castro–Córdoba–Fefferman–Gancedo–López-Fernández (2012) produced analytic initial interfaces, initially graphs in the stable regime, that "turn over" in finite time; and (2013) solutions that turn and later cease to be $C^4$. What remains open is the sharp threshold:

- **(Q1)** Is there a finite-time curvature blow-up for data that stay graphs, i.e. does $\|\partial_x f(t)\|_{L^\infty} \to \infty$ in finite time for some smooth stable $f_0$? Equivalently, is the class of globally regular graph data characterized by a slope/critical-norm condition, and what is the sharp constant?
- **(Q2)** For the two-phase problem, which singularity mechanisms are admissible? Splash singularities are *excluded* (Gancedo–Strain 2014), so any breakdown must be curvature/self-intersection-free.

A complete resolution means either a proof of global regularity for all stable graph data, or an explicit blow-up construction with $\sup_{t<T^*}\|f(t)\|_{\dot W^{1,\infty}} = \infty$.

## 2. Mathematical Foundations

**Darcy's law.** For velocity $u$, pressure $p$, viscosity $\mu$, permeability $\kappa$, density $\rho$, gravity $g$:
$$\frac{\mu}{\kappa}\,u = -\nabla p - (0,\dots,0,g\rho), \qquad \nabla\cdot u = 0 .$$

The density is a two-valued function $\rho = \rho^1 \mathbf{1}_{\Omega^1} + \rho^2\mathbf{1}_{\Omega^2}$ transported by $u$, with $\Omega^2$ the lower region. The vorticity is a measure supported on the interface $z(\alpha,t)$ with amplitude $\varpi$, giving the contour-dynamics formulation (Córdoba–Gancedo 2007) via Birkhoff–Rott.

**Graph equation (equal viscosities, $d=1$).** With $z(\alpha,t) = (\alpha, f(\alpha,t))$ and $A_\rho = \dfrac{\kappa g(\rho^2-\rho^1)}{2\pi\mu}$:
$$\partial_t f(x,t) = A_\rho\,\mathrm{p.v.}\!\int_{\mathbb{R}} \frac{\big(\partial_x f(x,t) - \partial_x f(x-\alpha,t)\big)\,\alpha}{\alpha^2 + \big(f(x,t)-f(x-\alpha,t)\big)^2}\,d\alpha .$$

Equivalently, writing $\Delta_\alpha f = \frac{f(x)-f(x-\alpha)}{\alpha}$,
$$\partial_t f = A_\rho \int_{\mathbb{R}} \frac{\partial_x f(x) - \partial_x f(x-\alpha)}{\alpha\,\big(1 + (\Delta_\alpha f)^2\big)}\,d\alpha .$$

**Linearization at $f\equiv 0$.**
$$\partial_t f = -A_\rho \pi\, |D| f, \qquad \widehat{f}(\xi,t) = e^{-A_\rho \pi |\xi| t}\,\widehat{f_0}(\xi).$$
So the equation is a **nonlocal, nonlinear, degenerate parabolic equation of order one**; it is *critical* at scaling $f_\lambda(x,t)=\lambda^{-1}f(\lambda x,\lambda t)$, whose invariant spaces are $\dot H^{3/2}(\mathbb{R})$, $\dot W^{1,\infty}$, and $\dot B^1_{\infty,1}$.

**Rayleigh–Taylor condition.** The sign function
$$\sigma(\alpha,t) = -\big[\nabla p\big](z(\alpha,t))\cdot \partial_\alpha^\perp z(\alpha,t) > 0$$
is required for local well-posedness (parabolicity). For a graph with $\rho^2 > \rho^1$, $\sigma > 0$ automatically. If $\rho^2 < \rho^1$ the problem is ill-posed in every Sobolev space (Siegel–Caflisch–Howison 2004; Córdoba–Gancedo 2007).

**Viscosity jump.** With $\mu^1\neq\mu^2$ the amplitude $\varpi$ solves a Fredholm equation
$$\varpi(\alpha) + A_\mu\, \partial_\alpha z(\alpha)\cdot \mathrm{p.v.}\!\int \frac{(\alpha-\beta)^\perp \varpi(\beta)}{|z(\alpha)-z(\beta)|^2}d\beta = -2A_\rho\,\partial_\alpha z_2(\alpha), \quad A_\mu = \frac{\mu^2-\mu^1}{\mu^2+\mu^1}\in(-1,1),$$
invertible for $|A_\mu|<1$ in the graph case.

**Known conserved/monotone quantities.** $\|f(t)\|_{L^\infty}$ (maximum principle), $\|f(t)\|_{L^2}$, and $\|\partial_x f(t)\|_{L^\infty}$ are non-increasing in the stable graph regime (Córdoba–Gancedo 2009; Cameron 2019).

## 3. History & State of the Art (SOTA)

- **1934** — M. Muskat introduces the model for water encroaching into oil sand.
- **1984–2004** — Formal and numerical analysis; Siegel–Caflisch–Howison prove ill-posedness in the unstable regime and global existence for small analytic data.
- **2007** — Córdoba–Gancedo give the contour-dynamics formulation and local well-posedness in $H^3$ under Rayleigh–Taylor, in 2D and 3D, with and without viscosity jump.
- **2012** — *Turning waves*: Castro–Córdoba–Fefferman–Gancedo–López-Fernández (Annals of Math.) construct stable analytic graphs that in finite time develop a vertical tangent — the interface stays smooth as a curve but is no longer a graph.
- **2013** — *Breakdown of smoothness* (ARMA): the same authors construct solutions starting in $H^4$ that turn and later leave $C^4$.
- **2013–2016** — Constantin–Córdoba–Gancedo–(Rodríguez-Piazza)–Strain: global existence for medium-size data in the Wiener-type algebra.
- **2014** — Gancedo–Strain: **no splash singularities** for two-phase Muskat (interfaces cannot self-touch).
- **2016** — Castro–Córdoba–Fefferman–Gancedo: splash *does* occur for the one-phase (water-wave-like) Muskat problem in stable regimes.
- **2017–2022** — Critical-regularity revolution: Deng–Lei–Lin (monotone data), Cameron (slope $<1$), Alazard–Lazar and Nguyen–Pausader (paradifferential local theory at $H^{3/2+}$), Córdoba–Lazar ($\dot H^{3/2}$ small), Gancedo–Lazar (3D critical $\dot H^2$), Alazard–Nguyen (endpoint theory, quasilinearization).
- **2019–2024** — Convex-integration non-uniqueness / mixing solutions in the unstable regime (Székelyhidi; Castro–Faraco–Mengual); self-similar solutions and corner desingularization (García-Juárez–Gómez-Serrano–Haziot–Pausader).

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\|f_0\|_{1} := \int |\xi|\,|\widehat{f_0}(\xi)|\,d\xi < 1/3$ | Global existence, $\|f\|_1$ decays | Constantin–Córdoba–Gancedo–Strain, JEMS 2013 |
| $\|f_0\|_{\dot B^1_{\infty,1}}$ small; 3D version | Global existence, 2D and 3D, viscosity jump allowed | CCGRS, Amer. J. Math. 2016 |
| $\|\partial_x f_0\|_{L^\infty} < 1$ (2D), arbitrary size in every other norm | Global well-posedness, instant analyticity | Cameron, Anal. PDE 2019 |
| Monotone $f_0$ (arbitrarily large, arbitrary slope) | Global existence | Deng–Lei–Lin, CPAM 2017 |
| $f_0 \in \dot H^{3/2}(\mathbb{R})$ with $\|f_0\|_{\dot H^{3/2}}$ small | Global well-posedness in the critical space | Córdoba–Lazar, Ann. ENS 2021 |
| $f_0 \in \dot H^{2}(\mathbb{R}^2)$ small (3D critical) | Global well-posedness | Gancedo–Lazar, CPAM 2022 |
| $f_0 \in H^{s}$, $s>3/2$ ($d=1$), RT stable | Local well-posedness | Alazard–Lazar ARMA 2020; Nguyen–Pausader ARMA 2020 |
| $f_0 \in \dot W^{1,\infty}\cap \dot B^{1}_{\infty,1}$ endpoint | Local existence/uniqueness at the endpoint | Alazard–Nguyen, CMP 2023 |
| Two-phase, any regularity | Splash singularity **impossible** | Gancedo–Strain, PNAS 2014 |
| One-phase, stable regime | Splash singularity **occurs** in finite time | CCFG, ARMA 2016 |
| Some stable analytic graphs | Finite-time turning; later loss of $C^4$ | CCFGL Annals 2012; CCFG ARMA 2013 |

## 5. Principal Obstacles

- **Criticality.** The equation is exactly critical at slope regularity: the parabolic term $|D|f$ and the nonlinearity $\partial_x f\cdot$(order-one operator) balance at the same scaling. No coercive quantity dominates $\|\partial_x f\|_{L^\infty}$ from above, so smallness cannot be propagated by energy methods alone.
- **Nonlocality with sign-indefinite kernel.** The kernel $\frac{1}{\alpha(1+(\Delta_\alpha f)^2)}$ degenerates as $|\Delta_\alpha f|\to\infty$: large slopes *suppress* the smoothing. Standard De Giorgi–Nash–Moser machinery for nonlocal operators requires uniform ellipticity $\lambda \le K \le \Lambda$, which fails precisely in the regime where blow-up would occur.
- **Slope 1 is a technical, not structural, threshold.** The condition $\|\partial_x f_0\|_\infty<1$ enters through pointwise comparison arguments; numerics of Córdoba–Gómez-Serrano show global behavior well beyond slope 1, but no proof reaches it.
- **The turning mechanism is invisible in graph coordinates.** Existing singularity constructions rely on complex-analytic extension and a Cauchy–Kovalevskaya argument in the *arc-chord* formulation; they cannot be run in Sobolev graph variables, and they are computer-assisted, giving no scaling-invariant blow-up profile.
- **No known self-similar blow-up profile** in the stable regime; the only exact self-similar solutions found so far *desingularize* rather than form singularities.
- **Convex integration gives non-uniqueness but no regular singularity.** Mixing solutions live in the unstable regime and are only weak $L^\infty$ solutions.

## 6. The Gap

Proven: global regularity for (i) critically-small data, (ii) monotone data, (iii) $\|\partial_x f_0\|_{L^\infty}<1$. Proven singular: turning + $C^4$-breakdown for special analytic data (which necessarily have slope $\to\infty$ at the turning time, hence violate (iii)).

The gap is the **medium-slope, non-monotone, large-critical-norm window**:
$$1 \le \|\partial_x f_0\|_{L^\infty} < \infty, \qquad \|f_0\|_{\dot H^{3/2}} \text{ large}, \qquad f_0 \text{ non-monotone}.$$

Crossing it requires either (a) a maximum principle or nonlinear-parabolic argument that survives kernel degeneracy at large slope — i.e. showing the modulus of continuity $\omega$ with $\omega'(0)=\infty$ is preserved for *all* slopes — or (b) a blow-up construction, presumably self-similar or via a moving-corner ansatz, exhibiting $\|\partial_x f\|_{L^\infty}\to\infty$ in finite time while remaining a graph. Which alternative holds is not known even conjecturally with consensus.

## 7. Current Research (as of June 2026)

- **Critical/endpoint well-posedness.** Alazard–Nguyen's quasilinearization and paradifferential toolbox continue to be pushed toward $\dot B^1_{\infty,1}$ globally-in-time for medium slope. Chen–Nguyen–Zhou and collaborators work on global results with slope bounds independent of the viscosity jump. *(frontier — verify)*
- **Corner dynamics and desingularization.** García-Juárez, Gómez-Serrano, Haziot and Pausader constructed exact self-similar solutions for the Muskat equation and proved that small moving corners are instantaneously desingularized — evidence that Lipschitz-type singularities are unstable, i.e. *against* finite-time slope blow-up. *(frontier — verify)*
- **Computer-assisted proofs.** Gómez-Serrano's school (Brown / Barcelona) applies rigorous interval arithmetic to Muskat-type contour dynamics, both for turning constructions and for candidate self-similar profiles.
- **Unstable regime and mixing.** Castro, Faraco, Mengual, Székelyhidi: degraded mixing solutions, subsolutions, and selection criteria; the question of which weak solution is the "physical" one is open.
- **Viscosity jump and three dimensions.** Gancedo–García-Juárez–Patel–Strain-type global results with $A_\mu\neq 0$; 3D large-data theory remains far behind 2D.
- **Key groups:** ICMAT Madrid (Córdoba, Gancedo, Lazar), Princeton/Brown (Fefferman, Gómez-Serrano), Sorbonne/ENS (Alazard), Brown & Temple (Nguyen), UPenn (García-Juárez).

## 8. Future Work

1. **Sharp slope threshold.** Determine whether the true global-existence threshold is slope $1$, some larger explicit constant, or $+\infty$. Cameron's proof loses a factor at exactly the point where the kernel $1+(\Delta_\alpha f)^2$ is compared to $1$.
2. **Modulus of continuity method.** Adapt Kiselev–Nazarov–Volberg-type moduli to the Muskat kernel; the obstruction is that the dissipation constant degrades like $(1+\|\partial_x f\|_\infty^2)^{-1}$.
3. **Self-similar blow-up search.** Systematically search for $f(x,t) = (T-t)F\!\left(\frac{x}{T-t}\right)$ solutions with unbounded $F'$; combine with computer-assisted validation.
4. **Graph-to-non-graph transition in Sobolev classes.** Extend the turning theorem from analytic to merely $H^s$ data with quantitative turning time.
5. **Three-dimensional turning.** Show whether turning waves exist in 3D — expected, unproved.
6. **Selection principle for mixing solutions**, connecting convex integration to the physical Darcy limit with capillarity/surface tension vanishing.

## 9. Key References

- **[Foundational]** M. Muskat. *Two fluid systems in porous media. The encroachment of water into an oil sand.* Physics **5** (1934), 250–264.
- **[Foundational]** D. Córdoba, F. Gancedo. *Contour dynamics of incompressible 3-D fluids in a porous medium with different densities.* Comm. Math. Phys. **273** (2007), 445–471.
- **[Foundational]** M. Siegel, R. Caflisch, S. Howison. *Global existence, singular solutions, and ill-posedness for the Muskat problem.* Comm. Pure Appl. Math. **57** (2004), 1374–1411.
- **[Singularity]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo, M. López-Fernández. *Rayleigh–Taylor breakdown for the Muskat problem with applications to water waves.* Ann. of Math. **175** (2012), 909–948.
- **[Singularity]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo. *Breakdown of smoothness for the Muskat problem.* Arch. Ration. Mech. Anal. **208** (2013), 805–909.
- **[Singularity]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo. *Splash singularities for the one-phase Muskat problem in stable regimes.* Arch. Ration. Mech. Anal. **222** (2016), 213–243.
- **[Structure]** F. Gancedo, R. M. Strain. *Absence of splash singularities for surface quasi-geostrophic sharp fronts and the Muskat problem.* Proc. Natl. Acad. Sci. USA **111** (2014), 635–639.
- **[Global]** P. Constantin, D. Córdoba, F. Gancedo, R. M. Strain. *On the global existence for the Muskat problem.* J. Eur. Math. Soc. **15** (2013), 201–227.
- **[Global]** P. Constantin, D. Córdoba, F. Gancedo, L. Rodríguez-Piazza, R. M. Strain. *On the Muskat problem: global in time results in 2D and 3D.* Amer. J. Math. **138** (2016), 1455–1494.
- **[SOTA]** S. Cameron. *Global well-posedness for the two-dimensional Muskat problem with slope less than 1.* Analysis & PDE **12** (2019), 997–1022.
- **[SOTA]** F. Deng, Z. Lei, F. Lin. *On the two-dimensional Muskat problem with monotone large initial data.* Comm. Pure Appl. Math. **70** (2017), 1115–1145.
- **[SOTA]** D. Córdoba, O. Lazar. *Global well-posedness for the 2D stable Muskat problem in $H^{3/2}$.* Ann. Sci. Éc. Norm. Supér. **54** (2021), 1315–1351.
- **[SOTA]** F. Gancedo, O. Lazar. *Global well-posedness for the three dimensional Muskat problem in the critical Sobolev space.* Comm. Pure Appl. Math. **75** (2022), 2586–2620.
- **[SOTA]** T. Alazard, O. Lazar. *Paralinearization of the Muskat equation and application to the Cauchy problem.* Arch. Ration. Mech. Anal. **237** (2020), 545–583.
- **[SOTA]** H. Q. Nguyen, B. Pausader. *A paradifferential approach for well-posedness of the Muskat problem.* Arch. Ration. Mech. Anal. **237** (2020), 35–100.
- **[SOTA]** T. Alazard, Q.-H. Nguyen. *Endpoint Sobolev theory for the Muskat equation.* Comm. Math. Phys. **397** (2023), 1043–1102.
- **[Weak solutions]** L. Székelyhidi Jr. *Relaxation of the incompressible porous media equation.* Ann. Sci. Éc. Norm. Supér. **45** (2012), 491–509.
- **[Weak solutions]** Á. Castro, D. Faraco, F. Mengual. *Degraded mixing solutions for the Muskat problem.* Calc. Var. Partial Differential Equations **58** (2019), art. 58.
- **[Survey]** F. Gancedo. *A survey for the Muskat problem and a new estimate.* SeMA Journal **74** (2017), 21–35.

## 10. Worked Example / Concrete Special Case

**(a) Linear decay.** Take $A_\rho\pi = 1$ and $f_0(x) = \varepsilon\cos(x)$ on the torus. The linearized equation $\partial_t f = -|D|f$ gives $f(x,t) = \varepsilon e^{-t}\cos x$, so $\|\partial_x f(t)\|_{L^\infty} = \varepsilon e^{-t}$: exponential smoothing, no singularity. The whole difficulty is that the true nonlinear kernel weakens this dissipation by $(1+(\Delta_\alpha f)^2)^{-1}$.

**(b) Where $1/3$ comes from.** Set $\|f\|_s := \int_{\mathbb{R}} |\xi|^s\,|\widehat f(\xi)|\,d\xi$, so $\|\partial_x f\|_{L^\infty} \le \|f\|_1$. Expand the kernel as a geometric series, valid when $|\Delta_\alpha f| \le \|f\|_1 < 1$:
$$\frac{1}{1+(\Delta_\alpha f)^2} = \sum_{n\ge 0} (-1)^n (\Delta_\alpha f)^{2n}.$$
Substituting into the graph equation and taking the Fourier transform, the $n=0$ term contributes exactly the linear dissipation $-\|f\|_2$ to $\frac{d}{dt}\|f\|_1$, while each $n\ge1$ term is a $(2n+1)$-fold multilinear expression bounded in absolute value by $\|f\|_2\,\|f\|_1^{2n}$ with combinatorial factor $(2n+1)$. Hence
$$\frac{d}{dt}\|f\|_1(t) \;\le\; -\|f\|_2(t)\Big(1 - \sum_{n\ge1}(2n+1)\,\|f\|_1^{2n}(t)\Big).$$
The series $\sum_{n\ge1}(2n+1)x^{2n} = \frac{3x^2-x^4}{(1-x^2)^2}$ equals $1$ at $x \approx 0.4859$ but the estimate is closed with the cruder majorant $\sum_{n\ge1}(2n+1)x^{2n} \le 3\frac{x^2}{1-x^2}\cdot\frac{1}{1-x^2}$, and requiring the bracket to stay positive yields the clean sufficient condition
$$\|f_0\|_1 < \tfrac13 \;\Longrightarrow\; \tfrac{d}{dt}\|f\|_1 < 0 \ \text{ for all } t,$$
so $\|f\|_1$ is decreasing, the smallness is self-improving, and the solution is global with $\|f(t)\|_1 \le \|f_0\|_1 e^{-ct}$.

**(c) Why this cannot reach the open regime.** For $f_0(x)=\varepsilon\cos x$ one computes $\|f_0\|_1 = \varepsilon$, so the theorem covers $\varepsilon<1/3$ — a slope bound of $1/3$. Cameron's argument raises this to slope $<1$. But the turning solutions of CCFGL have $\|\partial_x f\|_{L^\infty}\to\infty$; every known proof of global regularity breaks exactly where $(1+(\Delta_\alpha f)^2)^{-1}$ stops being comparable to $1$. The unresolved window is $1 \le \|\partial_x f_0\|_{L^\infty} < \infty$ with non-monotone data.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*