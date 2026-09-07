---
id: 06-pdes/kuramoto-sivashinsky-rigorous-bounds
title: "Kuramoto Sivashinsky Rigorous Bounds"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rigorous Amplitude Bounds for the Kuramoto–Sivashinsky Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kuramoto-sivashinsky-rigorous-bounds` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the one-dimensional Kuramoto–Sivashinsky (KS) equation on the periodic interval $[0,L]$,

$$\partial_t u + \partial_x^4 u + \partial_x^2 u + u\,\partial_x u = 0, \qquad u(x+L,t)=u(x,t),$$

with mean-zero initial data $u_0 \in L^2$. Solutions exist globally and are analytic for $t>0$; the equation has a compact global attractor. The open problem is the **scaling of the attractor's amplitude in $L$**.

**Conjecture (optimal $L^2$ bound).** There is an absolute constant $C$, independent of $L$ and of the initial data, such that

$$\limsup_{t\to\infty}\ \|u(\cdot,t)\|_{L^2(0,L)} \le C\,L^{1/2},$$

equivalently: the root-mean-square amplitude $L^{-1/2}\|u\|_{L^2}$ stays $O(1)$ as $L\to\infty$, so KS turbulence is *extensive* — energy grows proportionally to system size, not faster.

A complete resolution requires either (i) a proof of the $O(L^{1/2})$ bound (or of $O(L^{1/2+\varepsilon})$ for every $\varepsilon>0$ in the strong $L^2$ norm, which most authors would accept as settling the scaling), or (ii) a construction of a family of initial data and times with $\|u\|_{L^2} \gg L^{1/2}$, i.e. a genuine anomalous-amplitude mechanism. The best proven upper bound is $o(L^{3/2})$: a full power of $L$ away.

## 2. Mathematical Foundations

Write $u = \sum_{k\in\frac{2\pi}{L}\mathbb{Z}} \hat u_k e^{ikx}$. The linear symbol is

$$\lambda(k) = k^2 - k^4,$$

so modes with $0<|k|<1$ grow, modes with $|k|>1$ are damped, and the most unstable wavenumber is $k_\ast = 1/\sqrt{2}$. The number of linearly unstable modes is $\asymp L/2\pi$, which is why $L$ plays the role of a Reynolds number.

The mean $\bar u = L^{-1}\int_0^L u$ is conserved; set $\bar u = 0$ (a Galilean shift $u \mapsto u - c$, $x \mapsto x - ct$ maps mean-$c$ to mean-zero solutions). The energy identity for mean-zero solutions is

$$\frac{1}{2}\frac{d}{dt}\|u\|_{L^2}^2 = \|\partial_x u\|_{L^2}^2 - \|\partial_x^2 u\|_{L^2}^2 ,$$

because $\int u^2 u_x\,dx = 0$: **the nonlinearity is energy-neutral**. The right-hand side is not sign-definite, and Fourier interpolation gives only $\|\partial_x u\|^2 \le \|u\|\,\|\partial_x^2 u\|$, hence at best $\frac{d}{dt}\|u\|^2 \le \frac{1}{4}\|u\|^2$ — no bound at all. All progress therefore comes from *gauge* (background/Lyapunov) arguments: fix an $L$-periodic $\phi$, set $v = u-\phi$, and compute

$$\frac{1}{2}\frac{d}{dt}\|v\|_{L^2}^2 = -\|\partial_x^2 v\|^2 + \|\partial_x v\|^2 - \frac{1}{2}\int_0^L \phi' v^2\,dx - \int_0^L \phi\phi' v\,dx - \int_0^L (\phi''''+\phi'')\,v\,dx. \tag{2.1}$$

The term $-\tfrac12\int \phi' v^2$ is the only mechanism converting the nonlinearity into dissipation; it is coercive where $\phi' > 0$. The whole subject is the optimisation of $\phi$ against the cost terms $\int\phi\phi' v$ and $\int(\phi''''+\phi'')v$.

Related formulations: with $u = \partial_x h$, KS becomes the Kardar–Parisi–Zhang-type surface equation $\partial_t h + \partial_x^4 h + \partial_x^2 h + \tfrac12 (\partial_x h)^2 = \mathrm{const}$; the conjecture is then that $h$ has $O(L^{1/2})$ roughness, i.e. roughness exponent $1/2$ and dynamic exponent $z=3/2$ (KPZ class).

## 3. History & State of the Art (SOTA)

The equation arose independently in Kuramoto's phase-turbulence analysis of reaction–diffusion systems (Kuramoto–Tsuzuki, 1976) and Sivashinsky's derivation of flame-front instability (1977). Well-posedness in the periodic setting was established by Tadmor (1986); analyticity in a strip and existence of a compact global attractor by Collet–Eckmann–Epstein–Stubbe (1993) and Temam.

Upper bounds on $\limsup_t\|u\|_{L^2}$, all up to absolute constants:

| Result | Bound | Class |
|---|---|---|
| Nicolaenko–Scheurer–Temam 1985 | $L^{5/2}$ | odd data |
| Collet–Eckmann–Epstein–Stubbe 1993 | $L^{8/5}$ | odd data |
| Goodman 1994 | $L^{8/5}$, simplified proof | general mean-zero |
| Bronski–Gambill 2006 | $L^{3/2}$ | general mean-zero |
| Giacomelli–Otto 2005 | $o(L^{3/2})$ | general mean-zero |
| Otto 2009 / Goldman–Josien–Otto 2015 | logarithmic-order bounds in weaker norms | general |

Giacomelli–Otto (CPAM 2005) proved the first bound beating every power $L^{3/2}$ — $\|u\|_{L^2} = o(L^{3/2})$ in the time-averaged sense — by an interpolation/localisation scheme rather than a single gauge. Otto (JFA 2009) and then Goldman–Josien–Otto (Comm. PDE 2015) treated KS as an inhomogeneously forced Burgers equation and obtained, for the space–time average of $|u|$, a bound of order $\ln^{2/3}L$ per unit length — i.e. essentially the conjectured $O(1)$ amplitude up to a logarithm, but in an $L^1$-type norm, not $L^2$.

Numerically, Wittenberg–Holmes (1999) computed KS to $L \sim 400$ and found $L^{-1/2}\|u\|_{L^2}$ converging to a constant $\approx 1.2$ with no drift, and Cvitanović–Davidchack–Siminos (2010) mapped the attractor's state-space geometry. Goluskin–Fantuzzi (2019) computed *rigorous-in-principle* bounds by semidefinite programming over polynomial gauges, obtaining numbers within a small factor of the observed value for $L$ up to $\approx 60$.

## 4. Partial Results / Verified Cases

- **Odd (reflection-symmetric) subspace.** For $u(-x,t) = -u(x,t)$, the bounds $L^{5/2}$ (NST 1985) and $L^{8/5}$ (CEES 1993) hold with explicit constants; oddness kills $\int\phi\phi' v$ for odd $\phi$.
- **General mean-zero periodic data.** $\|u\|_{L^2} \lesssim L^{3/2}$ (Bronski–Gambill 2006, via an uncertainty-principle lemma for $\int \phi' v^2$), improved to $o(L^{3/2})$ (Giacomelli–Otto 2005).
- **Weak-norm near-optimality.** $\limsup_{T}\frac{1}{TL}\int_0^T\!\!\int_0^L |u| \lesssim \ln^{2/3} L$ (Goldman–Josien–Otto 2015). This is the conjectured extensive scaling up to a log, in $L^1$ average.
- **Steady and travelling waves.** Bounded solutions of the steady ODE $u''' + u' + \tfrac12 u^2 = c$ satisfy $|u| \le C$ with $C$ independent of $L$ (Michelson 1986); so the conjecture holds on the whole family of equilibria and travelling waves — the amplitude is $O(1)$ there.
- **Small $L$.** For $L < 2\pi$ every mode is damped, $u \equiv 0$ is globally exponentially stable, and $\|u\|_{L^2}\to 0$. Computer-assisted proofs (Zgliczyński–Mischaikow 2001; Arioli–Koch 2010) verify existence, stability and connecting orbits for specific solutions at fixed moderate $L$, hence rigorous $O(1)$ amplitudes there.
- **Attractor dimension.** $\dim_{\mathrm{f}}\mathcal{A} \lesssim L^{1.5}$ (Collet–Eckmann–Epstein–Stubbe 1993), with the extensive lower bound $\gtrsim L$; the conjectured optimum is $\asymp L$.
- **2D.** Global existence is *open* in general; it is proven for small data, for thin/anisotropic domains, and when a large shear advection is added (Ambrose–Mazzucato 2019, 2021; Coti Zelati–Dolce–Feng–Mazzucato 2021).

## 5. Principal Obstacles

- **The nonlinearity does nothing in the energy norm.** $\int u^2u_x = 0$, so no a priori estimate follows from energy alone; unlike Navier–Stokes there is no dissipation-driven balance to exploit.
- **Gauge functions cost what they gain.** In (2.1), making $\phi'$ large and positive over the whole period is impossible for a periodic $\phi$ — $\int_0^L\phi' = 0$. Any $\phi$ has regions of $\phi'<0$, and the cost terms $\int\phi\phi'v$ and $\int(\phi''''+\phi'')v$ scale up with $\|\phi\|_\infty$. Optimising this trade-off *within the single-gauge framework* is provably limited: Goluskin–Fantuzzi's SDP computations indicate that the background method with polynomial gauges saturates and cannot reach $L^{1/2}$.
- **No maximum principle, no conserved positive quantity.** The fourth-order operator destroys comparison arguments; $L^\infty$ control cannot be bootstrapped from below.
- **Fourier methods lose the phase information.** The bound $\|u_x\|^2 \le \|u\|\|u_{xx}\|$ is sharp mode-by-mode but blind to the fact that the KS attractor is a *spatially localised* pattern of cells of size $O(1)$ — the mechanism that should give extensivity. Turning "cells decorrelate over distance $O(1)$" into an estimate requires quantitative decorrelation that no current technique supplies.
- **Chaos.** The attractor is genuinely chaotic for large $L$, so no invariant-manifold or normal-form reduction closes; and there is no known Lyapunov functional.

## 6. The Gap

Proven: $o(L^{3/2})$ in $L^2$, and $O(\ln^{2/3}L)$ per unit length in $L^1$-average. Conjectured: $O(L^{1/2})$ in $L^2$, i.e. $O(1)$ per unit length.

The gap is a full power of $L$ in the strong norm, and technically it is the passage from **weak/averaged control** to **pointwise-in-time $L^2$ control**. The Goldman–Josien–Otto argument controls $u$ where it is typical; the missing step is excluding rare large excursions — bounding $\int u^2$ requires ruling out intermittent bursts on small spatial sets, which an $L^1$ average cannot see. Equivalently: prove that the KS attractor's energy density has uniformly bounded moments of order $2$, not just order $1$.

## 7. Current Research (as of June 2026)

- **Convex-optimisation / auxiliary-function bounds.** The Goluskin–Fantuzzi programme (Imperial College London, UC San Diego) constructs Lyapunov-type auxiliary functionals by sum-of-squares programming; current effort is on non-polynomial and spatially localised ansätze intended to break the saturation of the classical background method. *(frontier — verify)* Reports of SDP-certified bounds pushing past $L\approx 100$ with amplitude ratio still flat.
- **Optimal-transport / Burgers-forcing methods.** Otto's school (MPI MiS Leipzig) continues the inhomogeneous-Burgers route; the target is upgrading $L^1$-average control to $L^2$ via entropy-type estimates.
- **Rigorous computation.** Interval-arithmetic and Chebyshev-series validated numerics (Kraków, Rutgers, VU Amsterdam) now certify periodic orbits and connecting orbits at moderate $L$; extending certificates to invariant-measure statistics is active. *(frontier — verify)*
- **2D KS.** Global existence with anisotropic or advective stabilisation (Mazzucato, Larios, Yamazaki, Coti Zelati) remains the most active adjacent frontier.
- **Data-driven Lyapunov functions.** Neural-network-parameterised auxiliary functions with a posteriori SDP verification, applied to KS as the benchmark chaotic PDE. *(frontier — verify)*

## 8. Future Work

1. **Localised multi-gauge estimates.** Replace the single global $\phi$ by a family $\phi_j$ adapted to windows of length $O(1)$, and sum; the obstruction is controlling flux between windows.
2. **Second-moment bootstrap.** Combine the $\ln^{2/3}L$ $L^1$-bound with a smoothing estimate for $\partial_x^4$ to upgrade to $L^2$; a quantitative "no-burst" lemma is the missing ingredient.
3. **Lower bounds.** Almost nothing is proven below $O(1)$ amplitude; constructing data with amplitude $\gg L^{1/2}$ (even transiently, for time $O(1)$) would be equally informative.
4. **Attractor dimension.** Prove $\dim_{\mathrm f}\mathcal A \lesssim L$, matching the lower bound; this is widely expected to be easier than, and a precursor to, the amplitude conjecture.
5. **Stochastic/statistical framing.** Prove that invariant measures of KS are asymptotically product-like over $O(1)$ blocks — extensivity at the level of measures implies the conjectured scaling.

## 9. Key References

- **[Foundational]** Y. Kuramoto and T. Tsuzuki. *Persistent Propagation of Concentration Waves in Dissipative Media Far from Thermal Equilibrium.* Progress of Theoretical Physics, 55(2):356–369, 1976.
- **[Foundational]** G. I. Sivashinsky. *Nonlinear analysis of hydrodynamic instability in laminar flames — I. Derivation of basic equations.* Acta Astronautica, 4:1177–1206, 1977.
- **[Foundational]** B. Nicolaenko, B. Scheurer, R. Temam. *Some global dynamical properties of the Kuramoto–Sivashinsky equations: nonlinear stability and attractors.* Physica D, 16(2):155–183, 1985.
- **[Foundational]** E. Tadmor. *The well-posedness of the Kuramoto–Sivashinsky equation.* SIAM Journal on Mathematical Analysis, 17(4):884–893, 1986.
- **[Foundational]** D. Michelson. *Steady solutions of the Kuramoto–Sivashinsky equation.* Physica D, 19(1):89–111, 1986.
- **[Bounds]** P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe. *A global attracting set for the Kuramoto–Sivashinsky equation.* Communications in Mathematical Physics, 152(1):203–214, 1993.
- **[Bounds]** J. Goodman. *Stability of the Kuramoto–Sivashinsky and related systems.* Communications on Pure and Applied Mathematics, 47(3):293–306, 1994.
- **[Bounds]** L. Giacomelli and F. Otto. *New bounds for the Kuramoto–Sivashinsky equation.* Communications on Pure and Applied Mathematics, 58(3):297–318, 2005.
- **[Bounds]** J. C. Bronski and T. N. Gambill. *Uncertainty estimates and $L_2$ bounds for the Kuramoto–Sivashinsky equation.* Nonlinearity, 19(9):2023–2039, 2006.
- **[SOTA]** F. Otto. *Optimal bounds on the Kuramoto–Sivashinsky equation.* Journal of Functional Analysis, 257(7):2188–2245, 2009.
- **[SOTA]** M. Goldman, M. Josien, F. Otto. *New bounds for the inhomogeneous Burgers and the Kuramoto–Sivashinsky equations.* Communications in Partial Differential Equations, 40(12):2237–2265, 2015.
- **[SOTA / Computational]** D. Goluskin and G. Fantuzzi. *Bounds on mean energy in the Kuramoto–Sivashinsky equation computed using semidefinite programming.* Nonlinearity, 32(5):1705–1730, 2019.
- **[Computational]** R. W. Wittenberg and P. Holmes. *Scale and space localization in the Kuramoto–Sivashinsky equation.* Chaos, 9(2):452–465, 1999.
- **[Computational]** P. Zgliczyński and K. Mischaikow. *Rigorous numerics for partial differential equations: the Kuramoto–Sivashinsky equation.* Foundations of Computational Mathematics, 1(3):255–288, 2001.
- **[Survey / Dynamics]** P. Cvitanović, R. L. Davidchack, E. Siminos. *On the state space geometry of the Kuramoto–Sivashinsky flow in a periodic domain.* SIAM Journal on Applied Dynamical Systems, 9(1):1–33, 2010.
- **[2D]** D. M. Ambrose and A. L. Mazzucato. *Global existence and analyticity for the 2D Kuramoto–Sivashinsky equation.* Journal of Dynamics and Differential Equations, 31:1525–1547, 2019.

## 10. Worked Example / Concrete Special Case

**Goal.** Derive an explicit gauge bound from (2.1) and see exactly where the loss of $L$-powers occurs.

Take $u$ odd and $L$-periodic, and choose an odd, $L$-periodic gauge $\phi$ with $\|\phi\|_\infty \le M$ and

$$\phi'(x) \ge \gamma > 0 \quad\text{except on a set } B\subset[0,L] \text{ of measure } |B| \le \delta, \qquad \|\phi'\|_\infty \le \Gamma .$$

A concrete choice: a smoothed sawtooth of slope $\gamma = 2M/L$ over most of the period with a turnaround layer of width $\delta$, so $M \asymp \gamma L$ and $\Gamma \asymp M/\delta$. Oddness of $\phi$ and $u$ makes $\phi\phi'$ odd, so $\int \phi\phi' v = 0$ for odd $v$. Equation (2.1) becomes

$$\frac{1}{2}\frac{d}{dt}\|v\|^2 \le -\|v_{xx}\|^2 + \|v_x\|^2 - \frac{\gamma}{2}\|v\|^2 + \frac{\gamma+\Gamma}{2}\int_B v^2 + \|\phi''''+\phi''\|_{L^2}\,\|v\| .$$

Two estimates close the loop. First, $\|v_x\|^2 \le \tfrac{1}{4}\|v\|^2 + \|v_{xx}\|^2$ (Young on $\|v_x\|^2\le\|v\|\|v_{xx}\|$), which cancels the fourth-order term at the price of $+\tfrac14\|v\|^2$. Second, the localisation term is handled by Agmon / Gagliardo–Nirenberg,

$$\int_B v^2 \le |B|\,\|v\|_\infty^2 \le \delta\,\|v\|\,\|v_x\| \le \delta\big(\tfrac12\|v\|^{3/2}\|v_{xx}\|^{1/2}\big),$$

so choosing $\gamma > 1/2$ and $\delta$ small enough that $\tfrac{\Gamma\delta}{2}$ is absorbed by the remaining $\|v_{xx}\|^2$ and $\gamma\|v\|^2/4$ yields

$$\frac{d}{dt}\|v\|^2 \le -\frac{\gamma}{2}\|v\|^2 + C\,\|\phi''''+\phi''\|_{L^2}^2/\gamma ,$$

hence $\limsup_t \|v\| \lesssim \gamma^{-1}\|\phi''''+\phi''\|_{L^2}$ and $\limsup_t\|u\|_{L^2} \lesssim \gamma^{-1}\|\phi''''+\phi''\|_{L^2} + M L^{1/2}$.

**Where the loss happens.** The gauge must have $\gamma = O(1)$ to beat the linear instability, so $M \asymp \gamma L \asymp L$, and the $M L^{1/2}$ term alone gives $\|u\|_{L^2} = O(L^{3/2})$. Sharpening $\phi$ near the turnaround layer (CEES) trades $M$ against $\Gamma\delta$ and improves the exponent to $8/5$; Bronski–Gambill's uncertainty lemma replaces the crude $\int_B v^2 \le |B|\|v\|_\infty^2$ step and recovers $3/2$ for general data. But **every version pays $\|\phi\|_\infty \gtrsim 1 \cdot L$**, because a periodic $\phi$ with $\phi'\gtrsim 1$ on most of $[0,L]$ must climb a height $\asymp L$. Reaching the conjectured $O(L^{1/2})$ therefore cannot come from any single global gauge — it demands a genuinely local argument in which the "climb" is reset every $O(1)$ length. That is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*