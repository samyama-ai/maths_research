---
id: 09-probability/lil-stochastic-heat-equation
title: "Law of the Iterated Logarithm for Stochastic Heat Equations"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Law of the Iterated Logarithm for Stochastic Heat Equations

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/lil-stochastic-heat-equation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the nonlinear stochastic heat equation (SHE) on $\mathbb{R}_+\times\mathbb{R}$ driven by space–time white noise $\dot W$,

$$\partial_t u(t,x) = \tfrac{1}{2}\partial_x^2 u(t,x) + \sigma(u(t,x))\,\dot W(t,x),\qquad u(0,\cdot)=u_0,$$

with $\sigma:\mathbb{R}\to\mathbb{R}$ globally Lipschitz. The problem is to determine **exact laws of the iterated logarithm (LIL)** — normalisation *and* constant — for the three natural limits:

1. **Local (small-time) LIL.** For fixed $x$, is
 $\limsup_{\varepsilon\downarrow 0}\dfrac{u(t+\varepsilon,x)-u(t,x)}{\varepsilon^{1/4}\sqrt{2\log\log(1/\varepsilon)}} = c_\sigma(t,x)$ a.s., with $c_\sigma(t,x)$ an explicit functional of $\sigma(u(t,x))$?
2. **Chung-type (liminf) LIL.** Is $\liminf_{\varepsilon\downarrow0}(\log\log(1/\varepsilon))^{1/4}\varepsilon^{-1/4}\sup_{0\le r\le\varepsilon}|u(t+r,x)-u(t,x)| = \kappa_\sigma$ a.s., and what is $\kappa_\sigma$?
3. **Global (large $t$, large $|x|$) LIL.** For the parabolic Anderson model (PAM) $\sigma(u)=u$, $u_0\equiv 1$: identify the a.s. second-order fluctuation of $\log u(t,x)$ around its Lyapunov drift $-t/24$, and the exact $\limsup$ constant in the spatial law
 $\limsup_{R\to\infty}(\log R)^{-2/3}\log\sup_{|x|\le R}u(t,x)$.

A complete solution means: for each regime, a normalising function $\varphi$ and a **finite, non-zero, explicitly identified** constant $c$ with $\limsup=c$ a.s. (or $\liminf=c$ for Chung's form), for a class of $\sigma$ beyond the Gaussian ($\sigma\equiv$ const) and exactly solvable ($\sigma(u)=u$) cases. Partial results give two-sided bounds $0<c_1\le\liminf\le\limsup\le c_2<\infty$; these do not count as solutions.

## 2. Mathematical Foundations

**Mild (Walsh) solution.** With heat kernel $p_t(x)=(2\pi t)^{-1/2}e^{-x^2/2t}$, $u$ is the a.s. unique adapted random field satisfying

$$u(t,x)=(p_t*u_0)(x)+\int_0^t\!\!\int_{\mathbb R} p_{t-s}(x-y)\,\sigma(u(s,y))\,W(\mathrm{d}s\,\mathrm{d}y),$$

the integral being a Walsh martingale measure integral. For $\sigma$ Lipschitz and $u_0$ bounded measurable, existence, uniqueness and $\sup_{t\le T}\sup_x\mathbb E|u(t,x)|^p<\infty$ hold (Walsh 1986; Dalang 1999).

**Regularity.** $u$ is a.s. Hölder continuous of every order $<\tfrac14$ in $t$ and $<\tfrac12$ in $x$; these exponents are sharp. Hence the correct local normalisations are $\varepsilon^{1/4}$ (time) and $h^{1/2}$ (space), i.e. the field behaves locally like fractional Brownian motion with $H=1/4$ in $t$ and $H=1/2$ in $x$.

**Additive case as reference Gaussian model.** For $\sigma\equiv1$, $u_0\equiv0$, the field is centred Gaussian with

$$\mathbb E[u(s,x)u(t,x)]=\frac{1}{\sqrt{2\pi}}\Big[(t+s)^{1/2}-|t-s|^{1/2}\Big],$$

so $t\mapsto u(t,x)$ is a **bifractional Brownian motion** $B^{H,K}$ with $H=K=1/2$, up to the constant $2^{-1/2}\pi^{-1/4}$ (Swanson 2007; Lei–Nualart 2009). Its quartic variation over $[0,t]$ equals $6t/\pi$ a.s.

**Moments and intermittency (PAM).** For $\sigma(u)=u$, $u_0\equiv1$, Bertini–Cancrini (1995) give
$$\lim_{t\to\infty}\frac1t\log\mathbb E[u(t,x)^n]=\frac{n(n^2-1)}{24},\qquad n\ge2,$$
while the a.s. behaviour is *negative*: $\lim_{t\to\infty}t^{-1}\log u(t,x)=-\tfrac1{24}$ a.s. (X. Chen). The gap between annealed and quenched exponents is the analytic signature of intermittency and is the reason a global LIL is delicate.

**Spatial asymptotics (PAM).** $\displaystyle \lim_{R\to\infty}(\log R)^{-2/3}\log\sup_{|x|\le R}u(t,x)=c\,t^{1/3}$ a.s., with $c$ explicit (X. Chen 2016). The exponent $2/3$ replaces the Gaussian $1/2$ precisely because of multiplicative noise.

## 3. History & State of the Art (SOTA)

- **1986–1999.** Walsh's Saint-Flour notes set up the martingale-measure calculus; Dalang extends it to coloured noise. Hölder exponents $1/4$–$1/2$ become folklore.
- **2007–2009.** Swanson computes the quartic variation of $t\mapsto u(t,x)$ for additive noise; Lei–Nualart identify the process as bifractional Brownian motion, importing the full Gaussian LIL toolkit (Tudor–Xiao's sample-path results) into SPDE.
- **2009–2013.** Foondun–Khoshnevisan establish intermittency criteria; Conus–Khoshnevisan (PTRF 2012) introduce *growth indices* locating the farthest peaks; Conus–Joseph–Khoshnevisan (Ann. Probab. 2013) prove the first spatial "chaos" estimates, obtaining matching-order bounds of size $(\log R)^{1/6}$ for $\sigma$ bounded above and below.
- **2015–2016.** X. Chen proves the exact a.s. temporal exponent $-1/24$ and the exact spatial constant with exponent $2/3$ for the $(1+1)$-dimensional PAM — the sharpest global results known.
- **2017–2018.** Khoshnevisan–Kim–Xiao develop *macroscopic multifractal analysis*: the tall peaks of $u$ over $|x|\le R$ form a random set of macroscopic (Barlow–Taylor) dimension computed exactly for the PAM, refining any single LIL into a whole spectrum.
- **2020–present.** KPZ-side input: since $h=\log u$ solves the KPZ equation, exact-solvability (Amir–Corwin–Quastel, Borodin–Corwin) supplies one-point distributions and hence sharp tail estimates that feed Borel–Cantelli arguments.

## 4. Partial Results / Verified Cases

- **Additive noise, $\sigma\equiv 1$ (fully solved).** $t\mapsto u(t,x)$ is bifractional Brownian motion; the classical LIL for locally-$H=1/4$ Gaussian processes gives
 $\limsup_{\varepsilon\downarrow0}\varepsilon^{-1/4}(2\log\log\tfrac1\varepsilon)^{-1/2}\,[u(t+\varepsilon,x)-u(t,x)]=(2/\pi)^{1/4}$ a.s. (see §10). Spatially, $h\mapsto u(t,x+h)-u(t,x)$ obeys the Brownian LIL with constant $1$ after normalisation $ \sqrt{2h\log\log(1/h)}$.
- **Chung's LIL, additive noise.** $\liminf$ with normalisation $\varepsilon^{1/4}(\log\log 1/\varepsilon)^{-1/4}$ is a.s. a finite positive constant (Tudor–Xiao, Bernoulli 2007, for bifractional BM); the constant equals a small-ball constant for $H=1/4$ fBm, **not known in closed form**.
- **PAM, $\sigma(u)=u$, $d=1$, $u_0\equiv1$.** Exact temporal exponent $\lim t^{-1}\log u(t,x)=-1/24$; exact spatial constant with $(\log R)^{2/3}$ scaling (X. Chen 2015, 2016). Second-order (LIL) corrections open.
- **Lipschitz $\sigma$ bounded above and below by positive constants.** Two-sided bounds $0<c_1\le\liminf_R(\log R)^{-1/6}\sup_{|x|\le R}u(t,x)\le\limsup\le c_2<\infty$ (Conus–Joseph–Khoshnevisan 2013).
- **Coloured noise / Riesz kernels $f(x)=|x|^{-\beta}$, $0<\beta<\min(d,2)$.** Temporal Hölder exponent becomes $(2-\beta)/4$; LIL normalisations $\varepsilon^{(2-\beta)/4}$ with two-sided constants (Chen 2016; Herrell–Song–Wu–Xiao 2020, exact moduli of continuity).
- **Multifractal refinement.** For the PAM the macroscopic dimension of $\{x: u(t,x)>\exp(\alpha(\log x)^{2/3})\}$ is computed exactly (Khoshnevisan–Kim–Xiao, Ann. Probab. 2017).

## 5. Principal Obstacles

- **No Gaussian comparison.** Exact LIL constants for Gaussian fields come from Slepian/Sudakov–Fernique comparison and Gaussian isoperimetry. For $\sigma$ non-constant, $u(t,\cdot)$ is a non-Gaussian, non-Markov functional of the noise; none of these tools apply.
- **Failure of exact scaling.** Classical LILs exploit self-similarity plus stationary increments (Brownian motion, fBm, Lévy processes) to turn the $\limsup$ into a $0$–$1$ event with a computable rate. The SHE is only *approximately* self-similar (weak scaling $u(a^4t,a^2x)$ holds in law only for $\sigma(u)=cu$ with $u_0$ scale-invariant), so blocking arguments lose the constant.
- **Intermittency destroys moment-to-a.s. transfer.** Because $\frac1t\log\mathbb E[u^n]\sim n^3/24$ grows cubically, Chebyshev bounds on $u$ are dominated by exponentially rare peaks; moment methods yield the right exponent but never the constant.
- **Second Borel–Cantelli needs sharp decorrelation.** Lower LIL bounds require near-independence of the field on well-separated blocks with quantitative error. For the SHE, decorrelation in $t$ is only polynomial and is not uniform in the value of $u$, so the independence-approximation error is of the same order as the sought fluctuation.
- **Chung-type constants are small-ball constants.** Even in the Gaussian case, $\kappa$ is the small-deviation constant of fBm with $H=1/4$; explicit small-ball constants are known only for $H=1/2$. This is a genuinely separate open problem.
- **Malliavin calculus gives densities, not extremes.** Malliavin-based tools (Nualart, Sanz-Solé) prove smooth densities and Gaussian-type tail bounds for $u(t,x)$, but with non-matching upper/lower constants, exactly the loss that kills LIL sharpness.

## 6. The Gap

Proved: correct **normalisations** in all regimes ($\varepsilon^{1/4}$, $h^{1/2}$, $(\log R)^{2/3}$, $t/24$) and exact **constants only** in (i) the Gaussian additive case and (ii) the exactly solvable PAM first-order exponents. Missing: the **constant** in every genuinely nonlinear or second-order regime. Concretely, the gap is one step: convert two-sided estimates $c_1\le\limsup\le c_2$ into $c_1=c_2$. This requires either

- a **localisation theorem** showing $u(t+\varepsilon,x)-u(t,x)$ is, to leading order, $\sigma(u(t,x))$ times an independent copy of the additive-noise increment, with error $o(\varepsilon^{1/4}(\log\log)^{1/2})$ *uniformly along a geometric sequence* $\varepsilon_n=\theta^n$ — currently available only in $L^p$, not a.s.; or
- a **sharp large-deviation rate** for $\log u(t,x)+t/24$ with matching upper and lower tail constants, at the second-order scale, which would follow from a KPZ-fixed-point-level control of the $t\to\infty$ fluctuations $t^{1/3}$ jointly in $t$.

## 7. Current Research (as of June 2026)

- **Utah/Michigan school (Khoshnevisan, Kim, Xiao and collaborators):** macroscopic multifractal analysis extended to $\sigma$ merely Lipschitz, and to coloured noise; goal is a full "LIL spectrum" replacing single constants.
- **X. Chen (Tennessee) and Le Chen (Auburn):** high-moment asymptotics and spatial ergodicity for SHE with rough/measure initial data; spatial CLTs (Huang–Nualart–Viitasaari) now give the fluctuation *distribution*, an ingredient for sharp Borel–Cantelli.
- **KPZ-integrability route (Corwin, Ghosal, Tsai and co-workers):** exact tail bounds for the KPZ equation give upper-tail rate $\exp(-\tfrac{4}{3}s^{3/2})$ and lower-tail rate $s^{5/2}$; combining these with a chaining argument is the most promising path to an exact temporal LIL constant for the PAM. *(frontier — verify)*
- **Regularity structures / paracontrolled route (Hairer school):** LILs for singular SPDEs such as PAM in $d=2$ and $\Phi^4_3$; here even the correct normalisation is partly conjectural. *(frontier — verify)*
- **Chung-type problems:** small-ball probabilities for solutions of nonlinear SPDEs, via Malliavin-calculus lower bounds on densities. *(frontier — verify)*

## 8. Future Work

- Prove a **quenched local limit theorem**: $\varepsilon^{-1/4}(u(t+\varepsilon\cdot,x)-u(t,x))\Rightarrow \sigma(u(t,x))\,B^{1/2,1/2}$ a.s.-jointly, then transfer the Gaussian LIL constant.
- Identify the second-order term in $\log u(t,x)=-t/24+\Theta(t^{1/3})$ and prove a $t^{1/3}(\log\log t)^{2/3}$ LIL for the KPZ height — the SPDE analogue of the LIL for last-passage percolation (Ledoux–Rider-type tail bounds).
- Determine the small-ball constant for $H=1/4$ fBm, unlocking Chung's LIL for additive-noise SHE.
- Extend to systems, to $\sigma$ non-Lipschitz ($\sigma(u)=|u|^\gamma$, $\gamma<1$), and to the SHE on bounded domains where the invariant measure changes the LIL.
- Establish LILs for the **Barlow–Taylor dimension** of peak sets, i.e. a functional LIL rather than a pointwise one.

## 9. Key References

- **[Foundational]** John B. Walsh. *An Introduction to Stochastic Partial Differential Equations.* École d'été de Probabilités de Saint-Flour XIV, Lecture Notes in Mathematics 1180, Springer, 1986.
- **[Foundational]** Robert C. Dalang. *Extending the martingale measure stochastic integral with applications to spatially homogeneous s.p.d.e.'s.* Electronic Journal of Probability, 4(6), 1999.
- **[Foundational]** Lorenzo Bertini and Nicoletta Cancrini. *The stochastic heat equation: Feynman–Kac formula and intermittence.* Journal of Statistical Physics, 78:1377–1401, 1995.
- **[Foundational]** Jason Swanson. *Variations of the solution to a stochastic heat equation.* Annals of Probability, 35(6):2122–2159, 2007.
- **[SOTA]** Pedro Lei and David Nualart. *A decomposition of the bifractional Brownian motion and some applications.* Statistics & Probability Letters, 79(5):619–624, 2009.
- **[SOTA]** Daniel Conus, Mathew Joseph and Davar Khoshnevisan. *On the chaotic character of the stochastic heat equation, before the onset of intermittency.* Annals of Probability, 41(3B):2225–2260, 2013.
- **[SOTA]** Xia Chen. *Precise intermittency for the parabolic Anderson equation with an $(1+1)$-dimensional time–space white noise.* Annales de l'Institut Henri Poincaré Probabilités et Statistiques, 51(4):1486–1499, 2015.
- **[SOTA]** Xia Chen. *Spatial asymptotics for the parabolic Anderson models with generalized time–space Gaussian noise.* Annals of Probability, 44(2):1535–1598, 2016.
- **[SOTA]** Davar Khoshnevisan, Kunwoo Kim and Yimin Xiao. *Intermittency and multifractality: a case study via parabolic stochastic PDEs.* Annals of Probability, 45(6A):3697–3751, 2017.
- **[SOTA]** Ciprian A. Tudor and Yimin Xiao. *Sample path properties of bifractional Brownian motion.* Bernoulli, 13(4):1023–1052, 2007.
- **[Survey]** Davar Khoshnevisan. *Analysis of Stochastic Partial Differential Equations.* CBMS Regional Conference Series in Mathematics 119, American Mathematical Society, 2014.
- **[Survey]** Ivan Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications, 1(1), 2012.

## 10. Worked Example / Concrete Special Case

**Exact temporal LIL for additive noise.** Take $\sigma\equiv1$, $u_0\equiv0$, $\partial_t u=\tfrac12\partial_x^2u+\dot W$. Then

$$u(t,x)=\int_0^t\!\!\int_{\mathbb R}p_{t-s}(x-y)\,W(\mathrm{d}s\,\mathrm{d}y).$$

*Variance.* Using $\int_{\mathbb R}p_r(y)^2\,\mathrm{d}y=(4\pi r)^{-1/2}$,
$$\mathrm{Var}\,u(t,x)=\int_0^t (4\pi r)^{-1/2}\mathrm{d}r=\sqrt{t/\pi}.$$

*Covariance.* A direct computation gives $\mathbb E[u(s,x)u(t,x)]=\frac{1}{\sqrt{2\pi}}[(t+s)^{1/2}-(t-s)^{1/2}]$ for $s\le t$ (consistency check at $s=t$: $\sqrt{2t}/\sqrt{2\pi}=\sqrt{t/\pi}$ ✓). This is bifractional Brownian motion with $H=K=1/2$.

*Increment variance.* For $\varepsilon\downarrow0$,
$$\mathbb E\big[(u(t+\varepsilon,x)-u(t,x))^2\big]=\tfrac{1}{\sqrt{2\pi}}\Big[\sqrt{2t+2\varepsilon}+\sqrt{2t}-2\sqrt{2t+\varepsilon}+2\sqrt{\varepsilon}\Big]=\sqrt{\tfrac{2}{\pi}}\,\sqrt{\varepsilon}\;+\;O(\varepsilon^{3/2}t^{-1}),$$
since $\sqrt{2t+2\varepsilon}+\sqrt{2t}-2\sqrt{2t+\varepsilon}=O(\varepsilon^2 t^{-3/2})$.

So the increment is asymptotically that of fBm with $H=1/4$ and variance parameter $\sqrt{2/\pi}$. The Gaussian LIL for such a locally stationary field yields

$$\limsup_{\varepsilon\downarrow0}\frac{u(t+\varepsilon,x)-u(t,x)}{\varepsilon^{1/4}\sqrt{2\log\log(1/\varepsilon)}}=\Big(\tfrac{2}{\pi}\Big)^{1/4}\approx 0.8932\quad\text{a.s., for each fixed }t>0,x\in\mathbb R.$$

**Where it breaks.** For $\sigma(u)=u$ the same expansion is only formal: the natural guess
$$\limsup_{\varepsilon\downarrow0}\frac{u(t+\varepsilon,x)-u(t,x)}{\varepsilon^{1/4}\sqrt{2\log\log(1/\varepsilon)}}=(2/\pi)^{1/4}\,|u(t,x)|$$
requires replacing $\sigma(u(s,y))$ by $u(t,x)$ inside the stochastic integral over the parabolic box $[t,t+\varepsilon]\times[x-\sqrt\varepsilon,x+\sqrt\varepsilon]$. The replacement error has $L^2$ norm $O(\varepsilon^{1/2})$ — smaller than the main term $\varepsilon^{1/4}$ — but summing along $\varepsilon_n=\theta^n$ needs an a.s. bound uniform in $n$, and the available moment bounds degrade because $\mathbb E[u^{2p}]$ grows like $e^{p^3t/24}$. Closing that estimate is exactly the gap in §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*