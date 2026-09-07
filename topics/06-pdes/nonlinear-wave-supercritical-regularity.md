---
id: 06-pdes/nonlinear-wave-supercritical-regularity
title: "Nonlinear Wave Supercritical Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Regularity for Energy-Supercritical Defocusing Nonlinear Wave Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/nonlinear-wave-supercritical-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the defocusing nonlinear wave equation (NLW) on $\mathbb{R}^{1+d}$,
$$-\partial_t^2 u + \Delta u = |u|^{p-1}u, \qquad u(0,\cdot)=u_0,\ \partial_t u(0,\cdot)=u_1,$$
with $u:\mathbb{R}^{1+d}\to\mathbb{R}$ and $p>1$.

**Conjecture (global regularity).** For every $d\ge 3$, every $p$ with $1<p<\infty$, and every $(u_0,u_1)\in C_c^\infty(\mathbb{R}^d)\times C_c^\infty(\mathbb{R}^d)$, the unique maximal smooth solution is global: $T_{\max}=+\infty$, and it scatters to a free wave in the energy space.

The unresolved regime is **energy-supercritical**: $p > 1 + \frac{4}{d-2}$, equivalently the scaling-critical Sobolev exponent
$$s_c := \frac{d}{2}-\frac{2}{p-1} > 1 .$$
A complete resolution requires either (i) a proof of global smoothness for all $p$ (with a quantitative a priori bound replacing the energy), or (ii) an explicit smooth compactly supported datum whose solution forms a singularity in finite time. Conditional theorems that *assume* $\sup_{t}\|u(t)\|_{\dot H^{s_c}}<\infty$ do not count as a resolution.

## 2. Mathematical Foundations

**Scaling.** If $u$ solves the equation, so does
$$u_\lambda(t,x)=\lambda^{\frac{2}{p-1}}u(\lambda t,\lambda x),\qquad \lambda>0,$$
and $\|u_\lambda(0)\|_{\dot H^s(\mathbb{R}^d)}=\lambda^{\,s-s_c}\|u_0\|_{\dot H^{s}}$. Thus $\dot H^{s_c}\times\dot H^{s_c-1}$ is the scaling-invariant data space.

**Conserved energy.**
$$E(u)=\int_{\mathbb{R}^d}\Big(\tfrac12|\partial_t u|^2+\tfrac12|\nabla u|^2+\tfrac{1}{p+1}|u|^{p+1}\Big)\,dx,\qquad \frac{d}{dt}E(u)=0,$$
and $E(u_\lambda)=\lambda^{2(1-s_c)}E(u)$. For $s_c>1$ the energy of a rescaled bubble **tends to $0$ as $\lambda\to\infty$**: the conserved quantity is supercritical with respect to the scaling, and gives no control at small scales.

**Local theory.** Strichartz estimates for $\Box$: for admissible $(q,r)$ with $\frac1q+\frac{d-1}{2r}\le\frac{d-1}{4}$,
$$\|u\|_{L^q_tL^r_x}\lesssim \|u_0\|_{\dot H^{s}}+\|u_1\|_{\dot H^{s-1}}+\|\Box u\|_{L^{\tilde q'}_tL^{\tilde r'}_x}.$$
These give local well-posedness in $\dot H^{s_c}\times\dot H^{s_c-1}$ for all $p$ (Lindblad–Sogge, 1995), with the standard **blowup criterion**: if $T_{\max}<\infty$ then $\|u\|_{L^{q_c}_tL^{r_c}_x([0,T_{\max})\times\mathbb{R}^d)}=\infty$ for the critical Strichartz pair, and (Kenig–Merle-type) $\limsup_{t\to T_{\max}}\|u(t)\|_{\dot H^{s_c}}=\infty$ is *expected* but is exactly what is not proven unconditionally.

**Morawetz / virial control.** In $d=3$ the conformal and Morawetz identities give
$$\int_0^T\!\!\int_{\mathbb{R}^3}\frac{|u|^{p+1}}{|x|}\,dx\,dt \lesssim E(u),$$
a bound at unit scale only; it is likewise supercritical.

**Finite speed of propagation.** The solution on the backward cone $K(t_0,x_0)=\{(t,x):|x-x_0|\le t_0-t\}$ depends only on data in $B(x_0,t_0)$, and the flux
$$\mathrm{Flux}(t_1,t_2)=\frac{1}{\sqrt2}\int_{M_{t_1}^{t_2}}\Big(\tfrac12\big|\tfrac{x}{|x|}\partial_t u+\nabla u\big|^2+\tfrac{1}{p+1}|u|^{p+1}\Big)$$
is monotone; $\mathrm{Flux}\to 0$ at a putative singular point. This is the engine of the critical theory (Struwe, Grillakis).

## 3. History & State of the Art (SOTA)

- **1961–1972.** Jörgens proves global regularity in $d=3$ for $p<5$ (energy-subcritical); Segal and Strauss develop the general subcritical theory.
- **1988.** Struwe: global regularity for the energy-critical case $d=3$, $p=5$, for **radial** data, via the flux/cone monotonicity argument.
- **1990, 1992.** Grillakis removes radial symmetry for $d=3$, $p=5$, and extends to $3\le d\le 5$.
- **1993–1994.** Shatah–Struwe give a streamlined proof of global regularity and scattering for the defocusing energy-critical NLW $p=1+\frac{4}{d-2}$ in all dimensions $d\ge 3$, using Strichartz spaces rather than pointwise estimates.
- **2006–2008.** Kenig–Merle introduce the **concentration-compactness / rigidity** method; applied to focusing energy-critical NLW ($d=3$) it characterises the threshold by the ground state $W(x)=(1+|x|^2/3)^{-1/2}$.
- **2007.** Tao proves global regularity for a *logarithmically* energy-supercritical defocusing NLW $\Box u = u^5\log^{c}(2+u^2)$, radial, $d=3$, $c\le\tfrac{3}{2}$ — currently the strongest **unconditional** step past the critical exponent.
- **2011.** Killip–Visan: for $d=3$ and $p>5$ (and radially in all $d$), any solution with $\sup_t\|u(t)\|_{\dot H^{s_c}\times\dot H^{s_c-1}}<\infty$ is global and scatters — a *conditional* resolution.
- **2016.** Tao constructs finite-time blowup for a **defocusing supercritical nonlinear wave system** $\Box u = \nabla F(u)$, $u:\mathbb{R}^{1+3}\to\mathbb{R}^{40}$, $F\ge0$ coercive. This shows that no argument using only energy conservation, Morawetz monotonicity, and finite speed of propagation can prove the scalar conjecture.
- **2022.** Merle–Raphaël–Rodnianski–Szeftel construct self-similar finite-time blowup for the *defocusing* energy-supercritical NLS and for compressible Euler/Navier–Stokes, overturning the folk expectation that defocusing sign always implies regularity.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $s_c<1$ (energy-subcritical), all $d$, smooth data | **Solved** (Jörgens; Ginibre–Velo): global, scattering for $p>1+\frac{4}{d}$ |
| $s_c=1$: $d=3,p=5$; $d=4,p=3$; $d\ge3$, $p=1+\frac{4}{d-2}$ | **Solved**: Struwe (radial, 1988), Grillakis (1990/92), Shatah–Struwe (1993/94) — global regularity **and** scattering |
| $s_c=1$, focusing, $E<E(W)$ | **Solved** (Kenig–Merle 2008): dichotomy scattering vs. blowup; type-II blowup exists (Krieger–Schlag–Tataru 2009) |
| Log-supercritical, $d=3$, radial, $\Box u=u^5\log^c(2+u^2)$, $c\le 3/2$ | **Solved** (Tao 2007) |
| $s_c>1$, $d=3$, $p>5$, *assuming* $\|u\|_{L^\infty_t\dot H^{s_c}}<\infty$ | **Conditionally solved** (Killip–Visan 2011); radial version all $d\ge3$ |
| $s_c>1$, small data in $\dot H^{s_c}\times\dot H^{s_c-1}$ | **Solved** (Lindblad–Sogge 1995): global + scattering |
| $s_c>1$, $d=3$, $p=7$ or any $p>5$, general large smooth data | **OPEN** |
| Supercritical **systems** with coercive defocusing potential, $d=3$ | **Blowup exists** (Tao 2016) |
| Supercritical wave maps $\mathbb{R}^{1+d}\to S^d$, $d\ge3$ | Self-similar blowup (Shatah 1988; Bizoń–Biernat) |

## 5. Principal Obstacles

- **No coercive critical quantity.** Every conserved or monotone quantity ($E$, momentum, Morawetz, conformal energy) scales with a strictly negative power of frequency relative to $\dot H^{s_c}$. Energy at frequency $N$ controls only $N^{2-2s_c}$ worth of the critical norm, which is vacuous as $N\to\infty$. All perturbative continuation arguments need the critical norm, and there is no mechanism producing it.
- **Concentration-compactness is conditional by construction.** The Kenig–Merle machine extracts a minimal-norm almost-periodic solution *given* a uniform critical-norm bound; without it the profile decomposition has no compactness to exploit. The rigidity step then also fails: for $s_c>1$ the standard virial/Morawetz contradiction is not available at the correct scaling.
- **Tao's system blocks the "soft" route.** The 2016 blowup for a defocusing supercritical *system* is compatible with energy conservation, positivity of the potential, finite speed of propagation and Morawetz monotonicity. Any proof of the scalar conjecture must therefore use a structural feature of the scalar nonlinearity $|u|^{p-1}u$ (e.g. the algebra of the single unknown, or a hidden monotonicity), not general principles.
- **Defocusing sign is not a barrier to blowup.** MRRS (2022) constructed self-similar implosion for supercritical defocusing NLS. This removes the heuristic that repulsive nonlinearity forbids concentration and makes the *direction* of the conjecture itself uncertain.
- **Numerics are inconclusive.** Discretising a putative singularity at $s_c>1$ requires resolving self-similar scales; simulations in $d=3$, $p=7$ show no blowup for the data tried, but cannot rule out a codimension-$k$ unstable blowup profile.

## 6. The Gap

Everything hinges on one implication:
$$T_{\max}<\infty \ \Longrightarrow\ \limsup_{t\uparrow T_{\max}}\big\|(u,\partial_t u)(t)\big\|_{\dot H^{s_c}\times\dot H^{s_c-1}}=\infty ?$$
Killip–Visan proved the contrapositive is *sufficient*; the missing step is the **a priori bound**. Concretely, one needs a quantity $Q(u)$ that (a) is controlled by the smooth data, and (b) dominates $\|u(t)\|_{\dot H^{s_c}}$, or an "almost-conservation"/$I$-method-type propagation of a supercritical quantity upward through frequencies. No such $Q$ is known, and Tao's system shows that $Q$ cannot be built from energy + Morawetz + locality alone. Alternatively, the gap is closed from the other side by exhibiting a genuinely scalar, defocusing, finite-time singular solution — the MRRS spectral/self-similar route, not yet realised for $\Box$.

## 7. Current Research (as of June 2026)

- **Self-similar/implosion transfer.** Groups extending the Merle–Raphaël–Rodnianski–Szeftel front-compression method from NLS and compressible Euler to hyperbolic scalar equations; the obstruction is that the wave operator has no analogue of the NLS phase/modulus decomposition. *(frontier — verify)*
- **Conditional theory sharpening.** Killip, Visan, Bulut, Dodson and collaborators refine the scattering-under-a-priori-bound statements to weaker norms ($L^\infty_t L^{d(p-1)/2}_x$-type) and to non-radial higher dimensions.
- **Soliton resolution.** Duyckaerts–Kenig–Merle (radial energy-critical, all odd $d$, Acta 2023) and its non-radial extensions supply the rigidity technology that a supercritical proof would need to imitate.
- **Numerical/spectral hunting for unstable blowup profiles** for $d=3$, $p=7$ and for supercritical wave maps (Bizoń, Biernat, Glogić, Schörkhuber), using stability analysis of self-similar solutions in similarity variables. *(frontier — verify)*
- **Randomised data.** Almost-sure global well-posedness below the critical regularity (Burq–Tzvetkov programme) extended to supercritical exponents, giving generic-in-measure statements rather than deterministic ones.

## 8. Future Work

1. Find a monotone functional adapted to $\dot H^{s_c}$, not $\dot H^1$ — e.g. a weighted virial with weight $|x|^{2(s_c-1)}$ — and determine whether its defect terms have a sign for the scalar nonlinearity.
2. Push Tao's logarithmic gain: replace $\log^{3/2}$ by $\log^{c}$ with $c$ large, or by a power $|u|^{\epsilon}$, in the radial $d=3$ case; each increment tests whether the criticality barrier is soft or hard.
3. Adapt the MRRS spectral method: construct a smooth self-similar profile for $\Box u=|u|^{p-1}u$ in similarity variables $y=x/(T-t)$, $s=-\log(T-t)$, and count unstable directions.
4. Reduce Tao's blowup system from $\mathbb{R}^{40}$ toward $\mathbb{R}^{1}$; identify the minimal number of components for which defocusing supercritical blowup persists.
5. Settle the supercritical wave-map / Yang–Mills analogues, where explicit self-similar solutions already exist, as a laboratory for scalar NLW.

## 9. Key References

- **[Foundational]** M. Struwe. *Globally regular solutions to the $u^5$ Klein–Gordon equation.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. (4) 15 (1988), 495–513.
- **[Foundational]** M. Grillakis. *Regularity and asymptotic behaviour of the wave equation with a critical nonlinearity.* Annals of Mathematics 132 (1990), 485–509.
- **[Foundational]** J. Shatah, M. Struwe. *Well-posedness in the energy space for semilinear wave equations with critical growth.* International Mathematics Research Notices 1994, no. 7, 303–309.
- **[Foundational]** H. Lindblad, C. D. Sogge. *On existence and scattering with minimal regularity for semilinear wave equations.* Journal of Functional Analysis 130 (1995), 357–426.
- **[SOTA]** T. Tao. *Global regularity for a logarithmically supercritical defocusing nonlinear wave equation for spherically symmetric data.* Journal of Hyperbolic Differential Equations 4 (2007), 259–265.
- **[SOTA]** R. Killip, M. Visan. *The defocusing energy-supercritical nonlinear wave equation in three space dimensions.* Transactions of the American Mathematical Society 363 (2011), 3893–3934.
- **[SOTA]** R. Killip, M. Visan. *The radial defocusing energy-supercritical nonlinear wave equation in all space dimensions.* Proceedings of the American Mathematical Society 139 (2011), 1805–1817.
- **[SOTA]** T. Tao. *Finite time blowup for a supercritical defocusing nonlinear wave system.* Analysis & PDE 9 (2016), 1999–2030.
- **[SOTA]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On blow up for the energy super critical defocusing nonlinear Schrödinger equations.* Inventiones Mathematicae 227 (2022), 247–413.
- **[SOTA]** C. Kenig, F. Merle. *Global well-posedness, scattering and blow-up for the energy-critical focusing non-linear wave equation.* Acta Mathematica 201 (2008), 147–212.
- **[SOTA]** T. Duyckaerts, C. Kenig, F. Merle. *Soliton resolution for the radial critical wave equation in all odd space dimensions.* Acta Mathematica 230 (2023), 1–92.
- **[Survey]** T. Tao. *Nonlinear Dispersive Equations: Local and Global Analysis.* CBMS Regional Conference Series in Mathematics 106, American Mathematical Society, 2006.
- **[Survey]** C. Kenig. *Lectures on the Energy Critical Nonlinear Wave Equation.* CBMS Regional Conference Series in Mathematics 122, American Mathematical Society, 2015.

## 10. Worked Example / Concrete Special Case

Take $d=3$, $p=7$: $\ \Box u = |u|^{6}u$ on $\mathbb{R}^{1+3}$, defocusing, smooth compactly supported data.

**Step 1 — criticality.** $s_c=\frac{3}{2}-\frac{2}{7-1}=\frac32-\frac13=\frac76>1$. Energy-supercritical.

**Step 2 — how much the energy controls.** Let $u$ be concentrated at frequency $N$ in a ball of radius $N^{-1}$. Then $\|u(t)\|_{\dot H^{7/6}}\approx N^{7/6-1}\|u(t)\|_{\dot H^{1}}\le N^{1/6}\sqrt{2E}$. As $N\to\infty$ this bound diverges: energy conservation gives **no** uniform control of the critical norm. By contrast, for $p=5$ ($s_c=1$) the same computation gives $\|u\|_{\dot H^{s_c}}\le\sqrt{2E}$ — the whole reason the critical case is solved.

**Step 3 — the local existence time.** The contraction argument in $\dot H^{7/6}\times\dot H^{1/6}$ gives
$$T_{\mathrm{loc}}\gtrsim \big\|(u_0,u_1)\big\|_{\dot H^{7/6}\times\dot H^{1/6}}^{-\alpha},\qquad \alpha=\frac{p-1}{1-\ (\text{scaling deficit})}>0,$$
i.e. $T_{\mathrm{loc}}$ depends on the *critical* norm only. Iterating to a global solution needs an a priori bound on that norm; energy supplies $\|u(t)\|_{\dot H^1}$ instead, and the two are not comparable.

**Step 4 — the rescaled bubble.** Put $u_\lambda(t,x)=\lambda^{1/3}u(\lambda t,\lambda x)$ (here $\frac{2}{p-1}=\frac13$). Then
$$E(u_\lambda)=\lambda^{2(1-7/6)}E(u)=\lambda^{-1/3}E(u)\xrightarrow[\lambda\to\infty]{}0,$$
while $\|u_\lambda(0)\|_{\dot H^{7/6}}=\|u_0\|_{\dot H^{7/6}}$ is unchanged. A hypothetical singularity could form out of an *arbitrarily low-energy*, arbitrarily small bubble. Energy conservation cannot exclude it, and the Morawetz bound $\int\!\!\int |u|^{8}/|x|\lesssim E$ degenerates the same way under $u\mapsto u_\lambda$.

**Step 5 — what survives.** If one *assumes* $\sup_{t\in[0,T_{\max})}\|(u,\partial_tu)(t)\|_{\dot H^{7/6}\times\dot H^{1/6}}\le A<\infty$, Killip–Visan (2011) conclude $T_{\max}=\infty$ and $u$ scatters, with a scattering norm bounded by a function of $A$ alone. The entire open problem for $d=3,p=7$ is: **prove that $A$ exists.**

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*