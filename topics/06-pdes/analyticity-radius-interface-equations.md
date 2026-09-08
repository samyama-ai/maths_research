---
id: 06-pdes/analyticity-radius-interface-equations
title: "Analyticity Radius Lower Bounds for Solutions of the Muskat and SQG Equations"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Analyticity Radius Lower Bounds for Solutions of the Muskat and SQG Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/analyticity-radius-interface-equations` · **Status:** open

## 1. Problem Statement / Conjecture

For a solution $u(t)$ of an interface or active-scalar evolution equation that is real-analytic in the space variable, define the **analyticity radius** (uniform analyticity strip width)

$$\tau(t) \;=\; \sup\Big\{\,\tau>0 \;:\; u(t,\cdot)\ \text{extends holomorphically and boundedly to}\ \{z\in\mathbb{C}^d:\ |\mathrm{Im}\,z|<\tau\,\}\Big\}.$$

The problem is to determine sharp lower bounds on $\tau(t)$ for two model equations:

1. **Muskat (two-phase Hele-Shaw / porous medium interface).** Conjecture: every Rayleigh–Taylor-stable Muskat solution with sub-critical or critical data becomes instantly analytic and satisfies a *global* lower bound $\tau(t)\ge \tau_\ast(t)>0$ for all $t>0$, with $\tau_\ast$ depending only on the interface slope; equivalently, no stable Muskat solution loses analyticity in finite time.
2. **Inviscid SQG.** Conjecture: for analytic data $\theta_0$, the analyticity radius obeys the *at-most-exponential* collapse bound
$$\tau(t)\;\ge\;\tau_0\exp\Big(-C\!\int_0^t\|\nabla\theta(s)\|_{L^\infty}\,ds\Big),$$
and this is sharp in the sense that $\tau(t)\to 0$ in finite time **iff** $\int_0^T\|\nabla\theta\|_{L^\infty}\,dt=\infty$.

A complete solution requires either a proof of these bounds with explicit constants, or a construction of analytic data whose analyticity radius vanishes at a time strictly before any Sobolev-norm blow-up (a *complex* singularity reaching the real axis while the real solution stays smooth).

## 2. Mathematical Foundations

**Muskat.** For a graph interface $y=f(t,x)$ separating two fluids of densities $\rho^\pm$ and equal viscosity in a porous medium with Darcy's law $\frac{\mu}{\kappa}v=-\nabla p-(0,g\rho)$, the contour equation in 2D is

$$\partial_t f(t,x)\;=\;\frac{\rho^--\rho^+}{2\pi}\,\mathrm{P.V.}\!\int_{\mathbb{R}}\frac{\big(\partial_x f(t,x)-\partial_x f(t,x-\alpha)\big)\,\alpha}{\alpha^2+\big(f(t,x)-f(t,x-\alpha)\big)^2}\,d\alpha .$$

Linearizing at $f\equiv 0$ gives $\partial_t f = -\frac{\rho^--\rho^+}{2}\,\Lambda f$, $\Lambda=(-\Delta)^{1/2}$: the problem is parabolic of order one exactly when the **Rayleigh–Taylor condition** $\rho^->\rho^+$ (denser fluid below) holds. The critical scaling $f_\lambda(t,x)=\lambda^{-1}f(\lambda t,\lambda x)$ makes $\dot H^{3/2}(\mathbb{R})$, $\dot B^1_{\infty,1}$, and the Wiener-type norm $\|f\|_1=\int|\xi|\,|\hat f(\xi)|\,d\xi$ critical.

**SQG.** The inviscid surface quasi-geostrophic equation is
$$\partial_t\theta+u\cdot\nabla\theta=0,\qquad u=\nabla^\perp(-\Delta)^{-1/2}\theta=\mathcal{R}^\perp\theta ,$$
with $\mathcal{R}$ the Riesz transform; $\nabla u$ is a singular integral of $\theta$, and $\nabla^\perp\theta$ satisfies the same commutator structure as vorticity in 3D Euler (Constantin–Majda–Tabak).

**Analyticity radius machinery.** Two equivalent devices:

- *Gevrey norms* (Foias–Temam): $\;\|e^{\tau(t)\Lambda}u(t)\|_{X}$ for a Banach space $X$; differentiating gives
 $$\frac{d}{dt}\|e^{\tau\Lambda}u\|_X\;\le\;\dot\tau\,\|\Lambda e^{\tau\Lambda}u\|_X\;+\;\big\|e^{\tau\Lambda}\mathcal{N}(u,u)\big\|_X,$$
 so a lower bound on $\tau$ follows from an algebra/commutator estimate for the nonlinearity $\mathcal{N}$ in $e^{\tau\Lambda}X$.
- *Complex-strip continuation*: extend $f(t,\cdot)$ to $f(t,x+i\xi)$ for $|\xi|<\tau(t)$ and control $\|f\|_{\mathcal{S}_\tau}=\sup_{|\xi|<\tau}\|f(\cdot+i\xi)\|$, tracking whether complex singularities of the Birkhoff–Rott / Cauchy integral kernel $\alpha^2+(f(x)-f(x-\alpha))^2=0$ approach $\mathbb{R}$.

For Muskat the Wiener norm $\|f\|_{1,\tau}=\int e^{\tau|\xi|}|\xi|\,|\hat f(\xi)|\,d\xi$ turns the derivative-loss into a gain when $\dot\tau<\tfrac12$, which is the origin of the linear-in-time growth $\tau(t)\sim ct$.

## 3. History & State of the Art (SOTA)

- **1983** — Sulem, Sulem and Frisch introduce the *analyticity-strip method*: fit $|\hat u(k)|\sim C(t)k^{-\beta}e^{-\tau(t)|k|}$ from spectral data and read off $\tau(t)$; blow-up corresponds to $\tau\to0$. This remains the operational definition in numerics.
- **1989** — Foias and Temam prove Gevrey-class regularity for Navier–Stokes, giving $\tau(t)\gtrsim\min(t,1)$ for small data; Levermore–Oliver (1997) and Kukavica–Vicol (2009, 2011) adapt the method to Euler, obtaining only a *double-exponential* lower bound $\tau(t)\ge\tau_0\exp(-\exp(Ct))$ in 2D.
- **1994** — Constantin, Majda and Tabak propose SQG as a 2D analogue of 3D Euler; numerics suggest a hyperbolic saddle closing in finite time. Córdoba (1998) and Córdoba–Fefferman (JAMS 2002) rule out the simplest closing-saddle scenario; Constantin–Nie–Schörghofer and Ohkitani–Yamada report the analyticity radius decaying only exponentially, not to zero.
- **2007–2013** — Córdoba–Gancedo derive the modern Muskat contour equation; Castro, Córdoba, Fefferman, Gancedo and López-Fernández prove *turning waves* (Annals 2012) and finite-time **loss of smoothness** (ARMA 2013): analytic stable data that turn over, become unstable, and leave $C^4$. These solutions are constructed by controlling a *complex strip that pinches*, making $\tau(t)\to0$ the actual mechanism of breakdown.
- **2013–2016** — Constantin, Córdoba, Gancedo and Strain (JEMS 2013; with Rodríguez-Piazza, Amer. J. Math. 2016) prove global existence for $\|f_0\|_1<1/3$ in 2D (an explicit smaller constant in 3D) *together with* instant analyticity in the growing strip $|\mathrm{Im}\,z|<ct$ — the strongest positive $\tau$-bound known for any of these models.
- **2017–2022** — Large-slope and critical-regularity global results: Constantin–Gancedo–Shvydkoy–Vicol (finite slope), Cameron (slope $<1$ via a modulus of continuity), Córdoba–Lazar ($\dot H^{3/2}$ in 2D), Gancedo–Lazar ($\dot H^2$ in 3D), Alazard–Lazar (paralinearization), Alazard–Nguyen (endpoint Sobolev). None of these carries a quantitative $\tau(t)$.

## 4. Partial Results / Verified Cases

| Regime | Result | Radius bound |
|---|---|---|
| Muskat 2D, $\|f_0\|_1<1/3$ | Global existence, instant analyticity (CCGS, JEMS 2013) | $\tau(t)\ge ct$, linear growth, $c$ explicit |
| Muskat 3D, small Wiener norm | Same scheme (CCGRS, Amer. J. Math. 2016) | $\tau(t)\ge ct$ |
| Muskat, stable, $H^s$ data $s>3/2$ | Instantaneous analyticity of the interface (Matioc, Anal. PDE 2019; Escher–Matioc school, via analytic semigroups) | qualitative $\tau(t)>0$, no rate |
| Muskat, RT-unstable / turning | Analyticity radius collapses (CCFG, ARMA 2013) | $\tau(t)\to 0$ at finite $t$ — a *proved negative* case |
| SQG, subcritical dissipative $(-\Delta)^{\alpha}$, $\alpha>1/2$ | Global analyticity (Dong–Li, ARMA 2008) | $\tau(t)\gtrsim\min(t^{1/2\alpha},1)$, growing |
| SQG, critical $\alpha=1/2$ | Global smoothness (Kiselev–Nazarov–Volberg 2007; Caffarelli–Vasseur 2010) | $\tau$ bounded below on $[t_0,\infty)$ |
| SQG, inviscid, $\theta_0$ analytic | Local analyticity, BKM-type criterion | $\tau(t)\ge\tau_0e^{-C\int_0^t\|\nabla\theta\|_\infty}$ locally in time only |
| gSQG patches $u=\nabla^\perp\Lambda^{\beta-2}\theta$, $\beta\in(1,2)$, half-plane | Finite-time singularity (Kiselev–Ryzhik–Yao–Zlatoš, Annals 2016) | $\tau\to0$ for the patch boundary |

## 5. Principal Obstacles

- **Loss of a derivative in the strip.** For Muskat, $\dot\tau\,\|\Lambda e^{\tau\Lambda}f\|$ must absorb the nonlinearity. This works only while the nonlinear term has a factor smaller than $\tfrac12$ — precisely the origin of the $1/3$ Wiener-norm threshold. Beyond it there is no coercive term to pay for $\dot\tau>0$, and existing large-data global results (Cameron; Córdoba–Lazar) use maximum-principle/modulus-of-continuity or paradifferential arguments that are *non-analytic by construction*: a modulus of continuity carries no information about $\hat f$ at large $|\xi|$.
- **Non-locality of the kernel.** The Muskat denominator $\alpha^2+(f(x)-f(x-\alpha))^2$ vanishes for complex $\alpha$ when the *complexified* slope reaches $\pm i$. Controlling this is a statement about $f$ off the real axis; real-variable energy methods give no access to it. CCFG's breakdown proof shows the pinch is genuinely reachable, so no soft argument can preclude it in general.
- **Transport without dissipation (SQG).** The inviscid equation has no smoothing, so $\tau$ can only decrease; every known bound is Grönwall in $\|\nabla\theta\|_{L^\infty}$, the same quantity a blow-up proof would need. The bound is therefore *circular as a regularity criterion*.
- **Double-exponential slack.** Euler-type Gevrey estimates lose a second exponential because the commutator $[e^{\tau\Lambda},u\cdot\nabla]$ is estimated by an algebra property that costs $\|e^{\tau\Lambda}\nabla u\|$, itself controlled only by the analytic norm. Removing this to a single exponential is open even for 2D Euler.
- **Criticality mismatch.** Global existence is now known at critical regularity ($\dot H^{3/2}$, $\dot B^1_{\infty,1}$), but analyticity is a supercritical property: scaling maps $\tau\mapsto\lambda^{-1}\tau$, so no scaling-invariant norm can control $\tau$ from below.

## 6. The Gap

Proven: (a) instant analyticity plus $\tau(t)\gtrsim t$ for Muskat *below an explicit small-data threshold*; (b) qualitative instant analyticity for stable $H^s$ data with no rate and no lower bound uniform in $t$; (c) finite-time collapse of $\tau$ in the RT-unstable/turning regime; (d) a Grönwall bound for SQG that is not self-improving.

Missing: a lower bound on $\tau(t)$ for stable Muskat solutions that (i) does not require small Wiener norm, (ii) is quantitative in the slope $\|\partial_xf\|_{L^\infty}$, and (iii) survives to $t=\infty$. The single obstruction is an estimate showing that for RT-stable data the complexified interface cannot self-intersect — i.e. that $\inf_{|\xi|<\tau}\inf_\alpha|\alpha^2+(f(x+i\xi)-f(x+i\xi-\alpha))^2|$ stays bounded away from $0$ — for slopes of arbitrary size. For SQG, the gap is to decide whether $\tau(t)>0$ can fail while $\|\theta(t)\|_{H^s}$ stays finite; no example is known in either direction.

## 7. Current Research (as of June 2026)

- **Madrid / ICMAT school (Córdoba, Gancedo, Gómez-Serrano, Lazar).** Extending the complex-strip technology from small-data Muskat to the finite-slope regime, and computer-assisted control of the complexified kernel. *(frontier — verify)* Reported quantitative $\tau(t)$ bounds for $\|\partial_xf_0\|_\infty<1$ in preprint form.
- **Paris (Alazard, Nguyen).** Paradifferential and Lyapunov-functional methods (Alazard–Meunier–Smets) reformulate Muskat as a gradient flow; whether the Lyapunov structure propagates Gevrey norms is being studied.
- **Princeton/Duke (Kiselev, Zlatoš, Yao and collaborators).** Modified-SQG patch singularities and their analyticity-radius signature; the goal is to transplant the boundary-based blow-up to the whole plane.
- **Numerics.** High-precision spectral fits of $\tau(t)$ for SQG following Sulem–Sulem–Frisch; current computations show exponential, not finite-time, decay up to resolvable times. *(frontier — verify)*

## 8. Future Work

1. Prove a *slope-only* analyticity bound: $\tau(t)\ge \Phi(\|\partial_xf_0\|_{L^\infty})\,t$ for stable Muskat, interpolating between CCGS small data and Cameron's slope-$<1$ global theory.
2. Establish a **complex Rayleigh–Taylor condition** — a sign condition on the complexified pressure jump implying non-pinching of the strip — and show it is propagated by the flow.
3. Remove the second exponential in Euler/SQG Gevrey estimates by exploiting the commutator structure $\nabla^\perp\theta$ rather than a crude algebra property.
4. Determine whether analyticity-radius collapse can precede Sobolev blow-up; a rigidity theorem "$\tau(T^-)=0\Rightarrow\|\nabla\theta\|_{L^1_TL^\infty}=\infty$" would upgrade the Grönwall bound to a genuine criterion.
5. Computer-assisted proofs (in the style of the Muskat turning-wave and splash constructions) to certify $\tau(t)$ over finite time windows at large slope.

## 9. Key References

- **[Foundational]** P. Constantin, A. J. Majda, E. Tabak. *Formation of strong fronts in the 2-D quasigeostrophic thermal active scalar.* Nonlinearity 7 (1994), 1495–1533.
- **[Foundational]** C. Foias, R. Temam. *Gevrey class regularity for the solutions of the Navier–Stokes equations.* J. Funct. Anal. 87 (1989), 359–369.
- **[Foundational]** C. Sulem, P.-L. Sulem, H. Frisch. *Tracing complex singularities with spectral methods.* J. Comput. Phys. 50 (1983), 138–161.
- **[Foundational]** A. Córdoba, C. Fefferman. *Growth of solutions for QG and 2D Euler equations.* J. Amer. Math. Soc. 15 (2002), 665–670.
- **[SOTA]** P. Constantin, D. Córdoba, F. Gancedo, R. M. Strain. *On the global existence for the Muskat problem.* J. Eur. Math. Soc. 15 (2013), 201–227.
- **[SOTA]** P. Constantin, D. Córdoba, F. Gancedo, L. Rodríguez-Piazza, R. M. Strain. *On the Muskat problem: global in time results in 2D and 3D.* Amer. J. Math. 138 (2016), 1455–1494.
- **[SOTA]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo, M. López-Fernández. *Rayleigh–Taylor breakdown for the Muskat problem with applications to water waves.* Ann. of Math. 175 (2012), 909–948.
- **[SOTA]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo. *Breakdown of smoothness for the Muskat problem.* Arch. Ration. Mech. Anal. 208 (2013), 805–909.
- **[SOTA]** S. Cameron. *Global well-posedness for the two-dimensional Muskat problem with slope less than 1.* Anal. PDE 12 (2019), 997–1022.
- **[SOTA]** D. Córdoba, O. Lazar. *Global well-posedness for the 2D stable Muskat problem in $H^{3/2}$.* Ann. Sci. Éc. Norm. Supér. 54 (2021), 1315–1351.
- **[SOTA]** F. Gancedo, O. Lazar. *Global well-posedness for the 3D Muskat problem in the critical Sobolev space.* Arch. Ration. Mech. Anal. 246 (2022), 141–207.
- **[SOTA]** H. Dong, D. Li. *Spatial analyticity of the solutions to the subcritical dissipative quasi-geostrophic equations.* Arch. Ration. Mech. Anal. 189 (2008), 131–158.
- **[SOTA]** A. Kiselev, L. Ryzhik, Y. Yao, A. Zlatoš. *Finite time singularity for the modified SQG patch equation.* Ann. of Math. 184 (2016), 909–948.
- **[SOTA]** T. Alazard, O. Lazar. *Paralinearization of the Muskat equation and application to the Cauchy problem.* Arch. Ration. Mech. Anal. 237 (2020), 545–583.
- **[Survey]** F. Gancedo. *A survey for the Muskat problem and a new estimate.* SeMA J. 74 (2017), 21–35.
- **[Survey]** A. Kiselev. *Regularity and blow up for active scalars.* Math. Model. Nat. Phenom. 5 (2010), 225–255.
- **[Survey]** I. Kukavica, V. Vicol. *On the analyticity and Gevrey-class regularity up to the boundary for the Euler equations.* Nonlinearity 24 (2011), 765–796.

## 10. Worked Example / Concrete Special Case

**Linear Muskat with a single mode, and the effect of one nonlinear correction.**

Take $\rho^--\rho^+=2$ so the linearized equation on $\mathbb{T}$ is $\partial_tf=-\Lambda f$, i.e. $\partial_t\hat f(k)=-|k|\hat f(k)$. For $f_0(x)=\varepsilon\cos x + \sum_{k\ge2}a_k\cos kx$ with $|a_k|=A\,e^{-\tau_0 k}$, the solution has
$$|\hat f(t,k)|=A\,e^{-(\tau_0+t)|k|}\quad(k\ge2),$$
so the analyticity radius is exactly $\tau(t)=\tau_0+t$: the linear semigroup $e^{-t\Lambda}$ is the Poisson kernel and widens the strip at unit speed. This is the mechanism behind the $\tau(t)\ge ct$ theorem of Constantin–Córdoba–Gancedo–Strain.

**Where the nonlinearity fights back.** In the Wiener norm $\|f\|_{1,\tau}=\sum_k e^{\tau|k|}|k||\hat f(k)|$, the Muskat equation gives (CCGS, Section 3)
$$\frac{d}{dt}\|f\|_{1,\tau}\;\le\;-\big(1-\dot\tau\big)\!\sum_k e^{\tau|k|}k^2|\hat f(k)|\;+\;C\|f\|_{1,\tau}\!\sum_k e^{\tau|k|}k^2|\hat f(k)| \cdot \underbrace{\big(1+\|f\|_{1,\tau}\big)}_{\text{Taylor series of }\frac{1}{1+(\delta f/\alpha)^2}} .$$
Choosing $\dot\tau=\kappa<1$, the right side is negative as soon as
$$C\|f\|_{1,\tau}\big(1+\|f\|_{1,\tau}\big)<1-\kappa ,$$
which for the sharp constant yields the threshold $\|f_0\|_1<1/3$. The nonlinear term is a geometric series in $\delta f/\alpha=(f(x)-f(x-\alpha))/\alpha$; it converges only while $|\delta f/\alpha|<1$, i.e. slope below $1$. **At slope $1$ the series diverges and the estimate has no content** — this is exactly the analytic shadow of Cameron's slope-$<1$ threshold, and the concrete arithmetic obstacle in Section 6.

**Contrast with collapse.** Castro–Córdoba–Fefferman–Gancedo start from analytic data whose complexified curve $z(t,\alpha)=(z_1,z_2)(t,\alpha+i\xi)$ satisfies, after turning, $\partial_\alpha z_1(t,\alpha_0)=0$ at some real $\alpha_0$; tracking the complex zero of $\partial_\alpha z_1$ shows it migrates to the real axis at a finite time $t^\ast$, so $\tau(t^\ast)=0$ while $f$ is still in $C^3$ just before. The two computations bracket the problem: strip growth $\tau=\tau_0+t$ in the small-slope stable case, strip collapse $\tau\to0$ once stability is lost. Nothing quantitative is known in between.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*