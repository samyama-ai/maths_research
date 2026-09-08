---
id: 06-pdes/boussinesq-stratification-limit
title: "Boussinesq Stratification Limit"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boussinesq Stratification Limit

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/boussinesq-stratification-limit` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two singular limits carry the name "Boussinesq stratification limit", and the open problem is the second one in the regime where the first breaks down.

- **(A) Derivation.** Justify the Oberbeck–Boussinesq system as the joint low-Mach / low-Froude limit of the compressible Navier–Stokes–Fourier system, with error estimates and on unbounded domains.
- **(B) Strong-stratification asymptotics.** For the 3D Boussinesq system with buoyancy frequency $N \to \infty$, prove that solutions exist on a time interval $[0, T_N]$ with $T_N \to \infty$, and converge to the solution of the limit ("slow manifold") system.

**Conjecture (strong-stratification global limit).** Let $u^N_0 \in H^s(\mathbb{R}^3)$, $s > 5/2$, be divergence-free with $\theta^N_0 \in H^s$, uniformly bounded in $N$ and *not* small. For the inviscid stably stratified Boussinesq system, the lifespan satisfies $T_N \to \infty$ as $N \to \infty$, and on any fixed $[0,T]$ the solution converges (strongly in $C([0,T];H^{s'})$, $s' < s$) to the solution of the limit system obtained by projecting the nonlinearity onto the resonant set of the dispersion relation $\omega(\xi) = N|\xi_h|/|\xi|$.

A complete resolution requires either (i) a proof of uniform-in-$N$ energy bounds on time scales growing without bound for general large data, together with the strong convergence statement, or (ii) a counterexample: a family of data, uniformly bounded in $H^s$, whose lifespan stays bounded as $N\to\infty$, or which converges to something other than the resonant limit system.

## 2. Mathematical Foundations

The non-dimensional 3D Boussinesq system on $\Omega = \mathbb{R}^3$ or $\mathbb{T}^3$, in Boussinesq variables $u:\Omega\to\mathbb{R}^3$ (velocity), $\theta$ (buoyancy / density fluctuation), $p$ (pressure):

$$
\begin{cases}
\partial_t u + (u\cdot\nabla)u + \nabla p = -N\,\theta\, e_3 + \nu\,\Delta u,\\[2pt]
\partial_t \theta + (u\cdot\nabla)\theta = N\, u_3 + \kappa\,\Delta\theta,\\[2pt]
\operatorname{div} u = 0,
\end{cases}
$$

with $e_3 = (0,0,1)$ and $N = \mathrm{Fr}^{-1}$ the (non-dimensional) Brunt–Väisälä frequency, $\mathrm{Fr}$ the Froude number. The energy $E(t) = \tfrac12\|u\|_{L^2}^2 + \tfrac12\|\theta\|_{L^2}^2$ is conserved when $\nu=\kappa=0$, because the stratification terms form a skew-symmetric pair.

Write $U = (u,\theta)$. The linear part is $\partial_t U + N\,\mathcal{L}U = 0$ with
$$
\mathcal{L}U = \big(\mathbb{P}(\theta e_3),\, -u_3\big),\qquad \mathbb{P} = \mathrm{Id} - \nabla\Delta^{-1}\operatorname{div},
$$
$\mathcal{L}$ skew-adjoint on $L^2_\sigma\times L^2$. Its Fourier symbol has eigenvalues $0,0,\pm i\,\omega(\xi)$ with the **anisotropic dispersion relation**
$$
\omega(\xi) \;=\; N\,\frac{|\xi_h|}{|\xi|},\qquad \xi_h = (\xi_1,\xi_2).
$$

**Kernel (slow manifold).** $\ker\mathcal{L} = \{(u_h,0,\theta):\ \operatorname{div}_h u_h = 0,\ \theta = \theta(x_3)\}$ modulo the standard closure, i.e. *vertically sheared horizontal flows* (VSHF) $u = (u_h(x_3),0)$ together with $x_3$-dependent stratification profiles. The formal limit as $N\to\infty$ is obtained by conjugating with the group $e^{-N t\mathcal{L}}$, applying the Poincaré–Riemann–Lebesgue averaging of Schochet and Grenier, and keeping only the interactions on the **resonant set**
$$
\mathcal{R} = \{(\xi,\eta)\ :\ \pm\omega(\xi)\pm\omega(\eta)\pm\omega(\xi+\eta)=0\}.
$$

Since $\omega$ is homogeneous of degree $0$ and degenerate on $\{\xi_h=0\}$, $\mathcal{R}$ is large: it contains a codimension-one manifold plus the whole degenerate set. This is the structural difference from the rotating case, where $\omega(\xi) = \Omega\,\xi_3/|\xi|$ and resonances can be killed on non-resonant tori (Babin–Mahalov–Nicolaenko).

For (A), the starting point is the Navier–Stokes–Fourier system with Mach number $\varepsilon$ and Froude number $\varepsilon^{a}$; the Oberbeck–Boussinesq system arises for $a = 1/2$ (equivalently $\mathrm{Fr}^2 \sim \mathrm{Ma}$), while $a=0$ yields the **anelastic** system with non-constant background density $\bar\rho(x_3)$.

## 3. History & State of the Art

- **1879–1903.** Oberbeck and Boussinesq introduce the approximation: density variations are neglected except in the buoyancy term. Boussinesq, *Théorie analytique de la chaleur* (1903).
- **1996.** Rajagopal, Růžička, Srinivasa give a systematic asymptotic derivation and identify the scaling regimes where the approximation is (in)consistent.
- **1996–2003.** Embid–Majda develop the fast-wave averaging framework for geophysical flows with arbitrary potential vorticity; Majda's CIMS lecture notes codify it. Bourgeois–Beale (1994) had justified the quasigeostrophic limit for rotating stratified flow.
- **1999–2000.** Babin–Mahalov–Nicolaenko prove global regularity of 3D rotating Navier–Stokes and of the primitive equations for large rotation on resonant/non-resonant tori — the template for (B).
- **2004–2005.** Charve treats the rotating–stratified (primitive) system, proving convergence to the quasigeostrophic system with anisotropic viscosity and error rates.
- **2007–2009.** Masmoudi rigorously derives the anelastic approximation; Feireisl–Novotný prove the Oberbeck–Boussinesq limit from Navier–Stokes–Fourier for weak solutions, resolving (A) in the bounded-domain, weak-solution setting.
- **2015–2018.** Elgindi–Widmayer, Lee–Takada, Widmayer establish dispersive decay for the *purely stratified* semigroup and global small-data results plus convergence to stratified flow — the current SOTA for (B).

## 4. Partial Results / Verified Cases

- **(A) Weak-solution derivation.** Feireisl–Novotný (JMFM 2009; monograph 2009) prove convergence of finite-energy weak solutions of Navier–Stokes–Fourier to Oberbeck–Boussinesq on bounded domains with $\mathrm{Ma}=\varepsilon$, $\mathrm{Fr}=\sqrt{\varepsilon}$, for conservative boundary conditions. Masmoudi (JMPA 2007) covers the anelastic regime $\mathrm{Fr}=O(1)$.
- **(B) Small data, whole space, $\nu=\kappa=0$.** Elgindi–Widmayer (SIAM J. Math. Anal. 47, 2015) prove decay $\lesssim t^{-1/2}$ (anisotropic, with loss) for $e^{-Nt\mathcal{L}}$ and global existence for small, sufficiently regular data. Lee–Takada (Indiana Univ. Math. J. 66, 2017) obtain $L^p$–$L^q$ Strichartz estimates for the stratified semigroup and global well-posedness for data small in $\dot H^{1/2}\cap\dot H^{s}$ with $N$ large.
- **(B) Large data, long lifespan.** Widmayer (Commun. Math. Sci. 16, 2018) proves that for the inviscid 3D Boussinesq the solution converges, as $N\to\infty$ on time intervals of fixed length, to the corresponding *stratified* (VSHF-type) flow for data in $H^s$, $s>5/2$ — convergence on $[0,T]$ with $T$ independent of $N$, not $T_N\to\infty$.
- **Rotating + stratified, periodic.** Babin–Mahalov–Nicolaenko (M2AN 34, 2000) and Charve (Comm. PDE 29, 2004) give global regularity / convergence for $\Omega, N \to\infty$ with viscosity, on tori with non-resonance conditions on the aspect ratio, and for the ratio $N/\Omega$ away from a bad set. Koba–Mahalov–Yoneda (2012) extend to large data in scaling-critical Besov-type spaces for the rotating stratified system with $\nu>0$.
- **Anisotropic viscosity.** Scrobogna (DCDS 37, 2017) derives limit equations for a 3D periodic Boussinesq system with vanishing vertical viscosity and identifies the limit as a coupled 2D/VSHF system.
- **2D.** Global regularity holds with partial dissipation: Chae (Adv. Math. 203, 2006) and Hou–Li (DCDS 12, 2005) for viscosity in $u$ only or diffusion in $\theta$ only. The fully inviscid 2D case remains open in free space; with a boundary, Chen–Hou construct stable nearly self-similar blowup.

## 5. Principal Obstacles

- **Resonance abundance.** For $\omega(\xi)=N|\xi_h|/|\xi|$, the resonant set $\mathcal{R}$ is not removable by a Diophantine condition on the domain, unlike the rotating case. Averaging therefore leaves a genuinely nonlinear limit system — one cannot conclude regularity from a 2D limit equation.
- **Degeneracy at $\xi_h = 0$.** $\omega$ vanishes on a whole plane in Fourier space, so the Hessian $\nabla^2_\xi\omega$ is degenerate and stationary-phase / Strichartz estimates lose derivatives. Elgindi–Widmayer's decay is anisotropic and costs regularity; the loss is exactly what prevents closing large-data estimates.
- **Zero-order homogeneity.** $\omega$ is homogeneous of degree $0$: there is no gain from high frequencies, so dispersive smallness does not beat the quadratic nonlinearity uniformly in the frequency support. Bootstrapping "$T_N\gtrsim \log N$" or "$N^\delta$" is the natural output; $T_N\to\infty$ with a rate is not.
- **Slow-manifold instability.** VSHF profiles $u_h(x_3)$ are unstable (Kelvin–Helmholtz / Miles–Howard: stability needs Richardson number $\mathrm{Ri}\ge 1/4$). The limit dynamics is itself not globally regular in any known sense, so a convergence theorem cannot inherit global existence from the limit.
- **(A) on unbounded domains.** The acoustic waves are not compactly supported in frequency and the gravity field breaks the uniform pressure estimates; the standard Lighthill/local-decay argument for acoustic dispersion does not directly extend when buoyancy is present at the same order.

## 6. The Gap

Proven: convergence on $[0,T]$ with $T$ fixed and $N$-independent, plus global existence for *small* data. Conjectured: lifespan $T_N\to\infty$ for *bounded, non-small* data.

The exact missing step is a **uniform-in-$N$ a priori estimate in $H^s$, $s>5/2$, on time scales $\to\infty$**, which requires quantifying the cancellation in the non-resonant part of the nonlinearity beyond one normal-form step. Concretely: after one normal form, the remaining terms are (i) resonant, controlled only by the limit system's own regularity theory, and (ii) near-resonant terms with small denominators $|\omega(\xi)\pm\omega(\eta)\pm\omega(\xi+\eta)|$ that are not bounded below by any power of $N$ because $\omega$ is degree-0 homogeneous. Closing (ii) needs a genuinely new multilinear estimate; closing (i) needs global regularity for the VSHF-coupled limit system, itself open.

## 7. Current Research (as of June 2026)

- **Dispersive/normal-form school** (Widmayer, Ionescu, Pausader, Pusateri, and collaborators): space-time resonance methods for anisotropic degenerate dispersion; the rotating 3D Euler stabilization result of Guo–Huang–Pausader–Widmayer (CPAM 2023) is the model to transfer to the stratified case. Extending it to $\omega=N|\xi_h|/|\xi|$ is an active target. *(frontier — verify)*
- **Stratified shear stability** (Bianchini, Coti Zelati, Dolce, Zelati's group at Imperial/SISSA): inviscid damping and enhanced dissipation near stratified Couette flow at $\mathrm{Ri}>1/4$, giving quantitative control of the slow manifold's own dynamics.
- **Japanese school** (Takada, Lee, Iwabuchi): sharper Strichartz and bilinear estimates for the stratified and rotating-stratified semigroups; scaling-critical global well-posedness with $N$-dependent smallness thresholds.
- **Compressible derivation** (Feireisl, Novotný, Bella, Brezina): stratified/anelastic limits with variable background density and on domains with large volume, and quantitative relative-energy error rates. *(frontier — verify)*
- **Numerical/asymptotic** (Wingate, Julien, Knobloch): reduced models at low Rossby with finite Froude number, and identification of which resonant families survive.

## 8. Future Work

- Prove $T_N \gtrsim N^{\delta}$ for some $\delta>0$ with large $H^s$ data — even a logarithmic lifespan gain over the $N$-uniform $T$ would be new.
- Establish local (and conditional global) well-posedness for the resonant limit system including the VSHF sector; this is a prerequisite for any $T_N\to\infty$ statement.
- Construct a counterexample family exploiting the degeneracy at $\xi_h\to 0$: data concentrating near the slow manifold whose lifespan is $N$-independent.
- Extend (A) to unbounded domains and to the *ill-prepared* data case with error rates in the relative-energy functional.
- Settle whether strong stratification regularizes or destabilizes the 2D inviscid Boussinesq blowup scenarios of Chen–Hou and Elgindi.

## 9. Key References

- **[Foundational]** J. Boussinesq. *Théorie analytique de la chaleur*, vol. 2. Gauthier-Villars, Paris, 1903.
- **[Foundational]** K. R. Rajagopal, M. Růžička, A. R. Srinivasa. *On the Oberbeck–Boussinesq approximation.* Mathematical Models and Methods in Applied Sciences 6(8), 1996.
- **[Foundational]** A. Babin, A. Mahalov, B. Nicolaenko. *Fast singular oscillating limits and global regularity for the 3D primitive equations of geophysics.* M2AN Mathematical Modelling and Numerical Analysis 34(2), 2000. [DOI](https://doi.org/10.1051/m2an:2000138)
- **[Foundational]** P. F. Embid, A. J. Majda. *Averaging over fast gravity waves for geophysical flows with arbitrary potential vorticity.* Communications in Partial Differential Equations 21, 1996.
- **[Foundational]** D. Bourgeois, J. T. Beale. *Validity of the quasigeostrophic model for large-scale flow in the atmosphere and ocean.* SIAM Journal on Mathematical Analysis 25(4), 1994. [DOI](https://doi.org/10.1137/s0036141092234980)
- **[SOTA]** T. M. Elgindi, K. Widmayer. *Sharp decay estimates for an anisotropic linear semigroup and applications to the surface quasi-geostrophic and inviscid Boussinesq systems.* SIAM Journal on Mathematical Analysis 47(6), 2015. [DOI](https://doi.org/10.1137/14099036x)
- **[SOTA]** S. Lee, R. Takada. *Dispersive estimates for the stably stratified Boussinesq equations.* Indiana University Mathematics Journal 66(6), 2017. [DOI](https://doi.org/10.1512/iumj.2017.66.6179)
- **[SOTA]** K. Widmayer. *Convergence to stratified flow for an inviscid 3D Boussinesq system.* Communications in Mathematical Sciences 16(6), 2018. [DOI](https://doi.org/10.4310/cms.2018.v16.n6.a10)
- **[SOTA]** N. Masmoudi. *Rigorous derivation of the anelastic approximation.* Journal de Mathématiques Pures et Appliquées 88(3), 2007. [DOI](https://doi.org/10.1016/j.matpur.2007.06.001)
- **[SOTA]** E. Feireisl, A. Novotný. *The Oberbeck–Boussinesq approximation as a singular limit of the full Navier–Stokes–Fourier system.* Journal of Mathematical Fluid Mechanics 11, 2009.
- **[SOTA]** F. Charve. *Global well-posedness and asymptotics for a geophysical fluid system.* Communications in Partial Differential Equations 29, 2004. [DOI](https://doi.org/10.1081/pde-200043510)
- **[SOTA]** R. Bianchini, M. Coti Zelati, M. Dolce. *Linear inviscid damping for shear flows near Couette in the 2D stably stratified regime.* Indiana University Mathematics Journal 71(4), 2022. [DOI](https://doi.org/10.1512/iumj.2022.71.9040)
- **[Survey/Book]** J.-Y. Chemin, B. Desjardins, I. Gallagher, E. Grenier. *Mathematical Geophysics: An Introduction to Rotating Fluids and the Navier–Stokes Equations.* Oxford University Press, 2006.
- **[Survey/Book]** E. Feireisl, A. Novotný. *Singular Limits in Thermodynamics of Viscous Fluids.* Birkhäuser, 2009 (2nd ed. 2017). [DOI](https://doi.org/10.1007/978-3-7643-8843-0)
- **[Survey/Book]** A. J. Majda. *Introduction to PDEs and Waves for the Atmosphere and Ocean.* Courant Lecture Notes 9, AMS, 2003. [DOI](https://doi.org/10.1090/cln/009)

## 10. Worked Example / Concrete Special Case

**Goal:** exhibit an exact resonant triad that survives the $N\to\infty$ average, showing the limit system is *not* 2D Euler.

Work on $\mathbb{T}^3$, inviscid, and expand $U = \sum_\xi \hat U(\xi)e^{i\xi\cdot x}$. The nonlinear interaction of modes $\xi,\eta$ producing $\xi+\eta$ carries the oscillatory factor
$$
\exp\!\Big(i t\big(\pm\omega(\xi)\pm\omega(\eta)\mp\omega(\xi+\eta)\big)\Big),\qquad \omega(\xi)=N\frac{|\xi_h|}{|\xi|}.
$$
By stationary phase / Riemann–Lebesgue, terms with a nonzero phase average to $0$ as $N\to\infty$; terms with zero phase persist.

**Take** $\xi = (1,0,1)$, $\eta = (0,0,-2)$, so $\xi+\eta = (1,0,-1)$. Then
$$
\omega(\xi)=N\frac{1}{\sqrt2},\qquad \omega(\eta)=N\frac{0}{2}=0,\qquad \omega(\xi+\eta)=N\frac{1}{\sqrt2}.
$$
The phase $\omega(\xi)+\omega(\eta)-\omega(\xi+\eta) = N(\tfrac{1}{\sqrt2}+0-\tfrac{1}{\sqrt2}) = 0$: **exactly resonant for every $N$**.

This is not accidental. Take any $\xi=(\xi_h,\xi_3)$ with $\xi_h\ne 0$ and set $\eta=(0,0,-2\xi_3)$. Then $\xi+\eta=(\xi_h,-\xi_3)$, so $|\xi+\eta|=|\xi|$ and $\omega(\xi+\eta)=\omega(\xi)$, while $\omega(\eta)=0$ because $\eta_h=0$. Every such triad is resonant. The mode $\eta$ lies in $\ker\mathcal{L}$ — it is a VSHF/stratification mode, purely $x_3$-dependent.

**Consequence.** The averaged limit system retains the coupling
$$
\partial_t \hat U(\xi+\eta) \;\ni\; \mathcal{B}\big(\hat U(\xi),\,\hat U^{\mathrm{VSHF}}(\eta)\big),\qquad \eta=(0,0,-2\xi_3),
$$
i.e. the wave modes are advected and refracted by the shear $u_h(x_3)$ at order $1$, uniformly in $N$. So:

1. the limit is a coupled *wave $\times$ VSHF* system, not a decoupled 2D Euler flow;
2. no non-resonance condition on the torus's aspect ratio can remove these triads (the phase is identically zero, independent of the lattice), which is the structural obstacle noted in Section 5;
3. control of the limit requires control of the VSHF shear, whose stability is governed by the Richardson number $\mathrm{Ri} = N^2/|\partial_3 u_h|^2$ and the Miles–Howard threshold $\mathrm{Ri}\ge 1/4$ — precisely the mechanism studied by Bianchini–Coti Zelati–Dolce.

Contrast with pure rotation, $\omega_{\mathrm{rot}}(\xi)=\Omega\,\xi_3/|\xi|$: there the analogous "catalytic" family is empty on generic tori, which is why Babin–Mahalov–Nicolaenko obtain a 2D limit and global regularity, and why the same argument does not transfer to stratification.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*