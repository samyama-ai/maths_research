---
id: 06-pdes/boussinesq-inviscid-limit
title: "Boussinesq Inviscid Limit"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boussinesq Inviscid Limit

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/boussinesq-inviscid-limit` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For the two-dimensional Boussinesq system with viscosity $\nu\ge 0$ and thermal diffusivity $\kappa\ge 0$, let $(u^{\nu,\kappa},\theta^{\nu,\kappa})$ denote the solution with fixed initial data $(u_0,\theta_0)$. The **Boussinesq inviscid limit problem** has two coupled parts.

**(A) Convergence.** Does $(u^{\nu,\kappa},\theta^{\nu,\kappa}) \to (u^{0,0},\theta^{0,0})$ as $(\nu,\kappa)\to(0,0)$, in what topology, at what rate, and on what time interval? On a domain with boundary and no-slip conditions, does convergence hold at all, or does a Prandtl boundary layer separate?

**(B) Global regularity of the limit.** Does the fully inviscid system ($\nu=\kappa=0$) with smooth, compactly supported (or periodic) data $u_0\in H^s$, $\theta_0\in H^s$, $s>2$, $\nabla\cdot u_0=0$, admit a global-in-time smooth solution on $\mathbb{R}^2$ or $\mathbb{T}^2$?

Part (B) is the open half. A complete resolution is either a global a priori bound on $\int_0^T\|\nabla\theta(t)\|_{L^\infty}\,dt$ for every $T$ (giving global regularity), or a construction of smooth boundaryless data whose solution blows up in finite time. Part (A) is settled on the maximal existence interval of the inviscid solution in the absence of boundaries, and open in the boundary case beyond Kato-type criteria.

## 2. Mathematical Foundations

On $\Omega=\mathbb{T}^2$, $\mathbb{R}^2$, or a domain with boundary, the Boussinesq system is
$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\Delta u + \theta e_2,\qquad
\partial_t\theta + (u\cdot\nabla)\theta = \kappa\Delta\theta,\qquad \nabla\cdot u = 0,$$
with $u=(u_1,u_2)$ the velocity, $p$ the pressure, $\theta$ the temperature (or density) fluctuation, and $e_2=(0,1)$ the direction of gravity.

In vorticity form, $\omega=\partial_1 u_2-\partial_2 u_1$,
$$\partial_t\omega + (u\cdot\nabla)\omega = \nu\Delta\omega + \partial_1\theta,\qquad u=\nabla^\perp\Delta^{-1}\omega .$$
The whole difficulty sits in the **vortex-stretching-like forcing** $\partial_1\theta$: one full derivative of a quantity that is only transported.

**A priori quantities.** For $\kappa=0$, $\|\theta(t)\|_{L^p}=\|\theta_0\|_{L^p}$ for all $p\in[1,\infty]$. Energy obeys
$$\tfrac{d}{dt}\tfrac12\|u\|_{L^2}^2 + \nu\|\nabla u\|_{L^2}^2 = \int_\Omega \theta u_2 \le \|\theta_0\|_{L^2}\|u\|_{L^2},$$
so $\|u(t)\|_{L^2}\le \|u_0\|_{L^2}+t\|\theta_0\|_{L^2}$ — linear growth, not a uniform bound. From the vorticity equation,
$$\|\omega(t)\|_{L^\infty} \le \|\omega_0\|_{L^\infty} + \int_0^t\|\nabla\theta(s)\|_{L^\infty}\,ds,$$
and $\nabla\theta$ satisfies $\partial_t\nabla\theta+(u\cdot\nabla)\nabla\theta = -(\nabla u)^{\!\top}\nabla\theta$, a linear amplification by $\nabla u$, which is $\log$-singular in $\omega$. This closes only into a Beale–Kato–Majda-type criterion.

**Theorem (Chae–Nam 1997).** For $\nu=\kappa=0$ and $(u_0,\theta_0)\in H^s\times H^s$, $s>2$, there is a unique local solution, and the maximal time $T^*<\infty$ forces
$$\int_0^{T^*}\|\nabla\theta(t)\|_{L^\infty}\,dt = \infty .$$

**Analogy with 3D Euler.** For axisymmetric 3D Euler without swirl-free reduction, write $u = u^r e_r + u^\theta e_\theta + u^z e_z$. Setting $\Theta=(r u^\theta)^2$ and $\Omega=\omega^\theta/r$, the equations away from the symmetry axis $r=0$ match the 2D Boussinesq system under $r\mapsto x_1$, $z\mapsto x_2$. This is why (B) is regarded as a genuine model for 3D Euler singularity formation rather than a 2D curiosity.

**Rescaling.** The system is invariant under $u_\lambda(x,t)=\lambda^{\alpha}u(\lambda x,\lambda^{1-\alpha}t)$ with $\theta$ scaling one power lower; unlike Navier–Stokes, no scaling-critical conserved quantity controls $\nabla\theta$.

## 3. History & State of the Art (SOTA)

The system originates with Boussinesq (1903) as a buoyancy approximation to stratified flow; the Rayleigh–Bénard convection literature uses it as the standard model. The first modern well-posedness theory is Cannon–DiBenedetto (1980), who treated $\nu,\kappa>0$ with $L^p$ data; global regularity in the fully dissipative case is classical and parallels 2D Navier–Stokes.

The problem became a focus of the singularity-formation community after Majda–Bertozzi (2002) publicised the axisymmetric-Euler analogy. The partial-dissipation cases were opened in 2005–2006 by Hou–Li and, independently, Chae: global well-posedness for $(\nu>0,\kappa=0)$ and $(\nu=0,\kappa>0)$. Hmidi–Keraani (2007, 2009) and Danchin–Paicu (2008, 2009, 2011) pushed these to critical and Yudovich-type data. Hmidi–Keraani–Rousset (2011) and Jiu–Miao–Wu–Zhang (2014) reached critical fractional dissipation.

The blow-up side moved decisively after Luo–Hou (2014) reported a numerically stable, nearly self-similar singularity for 3D axisymmetric Euler on a cylinder boundary — whose 2D Boussinesq counterpart is a boundary singularity in the half-plane. Elgindi–Jeong (2020) gave the first rigorous finite-time singularity for Boussinesq, in an infinite sector with scale-invariant data. Chen–Hou (2022 onward) gave a computer-assisted proof of finite-time blow-up for 2D Boussinesq in the half-space with **smooth** data and a boundary, and for 3D Euler with boundary.

The boundaryless smooth-data case (B) remains open. Current consensus: the boundary is not merely technical — it supplies the hyperbolic degeneracy that drives the known blow-up scenarios.

## 4. Partial Results / Verified Cases

- **Full dissipation $\nu>0,\kappa>0$, $d=2$:** global regularity for $H^s$ or $L^p$ data (Cannon–DiBenedetto 1980; Temam).
- **$\nu>0,\kappa=0$:** global well-posedness in $H^s$, $s>2$ (Hou–Li, *DCDS* 2005; Chae, *Adv. Math.* 2006); extended to $u_0\in H^s$, $\theta_0\in L^2$ and to critical Besov data $B^{2/p}_{p,1}$ (Hmidi–Keraani 2007; Danchin–Paicu 2008/2009).
- **$\nu=0,\kappa>0$:** global well-posedness for $u_0\in H^s$, $s>2$, $\theta_0\in H^{s}$ (Chae 2006), and for Yudovich data $\omega_0\in L^\infty$ (Danchin–Paicu, *CMP* 2009; Hmidi–Keraani, *Indiana* 2009).
- **Fractional dissipation** $\nu(-\Delta)^\alpha u$, $\kappa(-\Delta)^\beta\theta$: global regularity for $\alpha+\beta\ge 1$ with $\alpha\in(0,1)$ (Jiu–Miao–Wu–Zhang, *SIAM J. Math. Anal.* 2014); critical case $\alpha=1/2,\beta=0$ (Hmidi–Keraani–Rousset, *CPDE* 2011).
- **Anisotropic viscosity, no diffusion:** horizontal viscosity $\nu\partial_1^2 u$ alone with $\kappa=0$ gives global well-posedness (Larios–Lunasin–Titi, *JDE* 2013; Danchin–Paicu, *M3AS* 2011).
- **Inviscid, special data:** global existence for perturbations of the stratified hydrostatic equilibrium $\theta = x_2$ in $\mathbb{R}^2$, where the linearised operator disperses (Elgindi–Widmayer, *SIAM J. Math. Anal.* 2015; Widmayer 2018). Trivially global when $\theta_0$ is constant (reduces to 2D Euler, Wolibner/Yudovich).
- **Inviscid blow-up:** finite-time singularity in a sector with $C^\alpha$ scale-invariant data (Elgindi–Jeong, *Ann. PDE* 2020); computer-assisted blow-up for smooth data in the half-space $\{x_1>0\}$ with boundary (Chen–Hou 2022–).
- **Convergence (A):** on $\mathbb{T}^2$ or $\mathbb{R}^2$ without boundary, $\|u^{\nu,\kappa}-u^{0,0}\|_{L^2}+\|\theta^{\nu,\kappa}-\theta^{0,0}\|_{L^2}=O((\nu+\kappa)^{1/2})$ on any $[0,T]\subset[0,T^*)$; see Section 10.

## 5. Principal Obstacles

- **One-derivative loss.** The forcing $\partial_1\theta$ costs a derivative relative to the transported quantity $\theta$. No conserved norm of $\theta$ controls $\nabla\theta$; every energy estimate returns $\|\nabla u\|_{L^\infty}\|\nabla\theta\|_{L^\infty}$, which is not closable by Grönwall without an a priori $\omega$ bound — which is exactly what is being sought.
- **No 2D Euler-style maximum principle.** In 2D Euler $\omega$ is transported and $\|\omega\|_{L^\infty}$ is conserved, giving global regularity. Buoyancy destroys transport of $\omega$; the log-Lipschitz bound $\|\nabla u\|_{L^\infty}\lesssim \|\omega\|_{L^\infty}\log(e+\|\omega\|_{H^s})$ then only yields double-exponential-in-$t$ growth *if* $\|\omega\|_{L^\infty}$ were bounded.
- **Loss of scaling criticality.** Unlike Navier–Stokes, there is no scale-invariant coercive quantity; the energy grows linearly in $t$ and cannot serve as a supercritical-to-critical bridge.
- **Boundary layers block (A) with boundary.** Under no-slip, the vanishing-viscosity limit inherits all Prandtl pathologies: the limit is only known conditionally, e.g. via a Kato-type criterion requiring $\nu\int_0^T\|\nabla u^\nu\|_{L^2(\Gamma_{c\nu})}^2\to 0$ in an $O(\nu)$ boundary strip. Buoyancy adds a temperature boundary layer coupled to the velocity layer, with no unconditional theory.
- **The known blow-ups are boundary-driven.** Elgindi–Jeong and Chen–Hou both exploit a solid wall (or a corner) to pin the hyperbolic stagnation point. Removing the boundary removes the mechanism, so these proofs do not transfer to (B).
- **Computer-assisted proofs do not generalise.** Chen–Hou's rigorous interval-arithmetic control of the self-similar profile is tied to one specific, numerically located solution; it gives no structural criterion applicable to arbitrary smooth data.

## 6. The Gap

Proven: global regularity whenever *any* of viscosity, diffusivity, anisotropic viscosity, or fractional dissipation with $\alpha+\beta\ge1$ is present; and finite-time blow-up for the inviscid system *with a boundary* or with non-smooth scale-invariant data. Open: the fully inviscid system on $\mathbb{R}^2$ or $\mathbb{T}^2$ with smooth data.

The exact step is control of
$$A(T)=\int_0^T\|\nabla\theta(t)\|_{L^\infty}\,dt .$$
All dissipative results replace this by a smoothing estimate on $\theta$ or $\omega$; all blow-up results replace it by a boundary-anchored self-similar ansatz. Nothing available bounds $A(T)$ using only the inviscid conservation laws $\|\theta\|_{L^p}$ and the linearly growing energy. Bridging the gap means either (i) finding a new conserved or monotone functional coercive over $\nabla\theta$, or (ii) producing a boundary-free self-similar profile with smooth data, presumably at $\alpha$-Hölder regularity first and then bootstrapped.

## 7. Current Research (as of June 2026)

- **Caltech (Hou, Chen and collaborators).** Extension of the computer-assisted self-similar framework from half-space Boussinesq/3D Euler with boundary toward boundary-free settings; refined numerics on interior stagnation points. *(frontier — verify)*
- **Duke / NYU (Elgindi and collaborators).** Constructions of $C^{1,\alpha}$ blow-up for Euler-type systems, aiming to push $\alpha\to 0$ and reach $C^\infty$ data. The Boussinesq sector result is the model case.
- **Analysis of the inviscid limit with boundary (Masmoudi, Nguyen, Maekawa schools).** Analytic and Gevrey-class justification of Prandtl expansions for buoyant flows; conditional Kato criteria adapted to coupled thermal layers. *(frontier — verify)*
- **Critical dissipation and eventual regularity.** Supercritical fractional Boussinesq ($\alpha+\beta<1$): partial regularity and eventual regularity via nonlinear maximum principles (Constantin–Vicol-type De Giorgi arguments).
- **Stability of stratified equilibria.** Long-time and global results for $\theta$ near a linear profile, using the anisotropic dispersion of the linearised operator, extended to partially damped and rotating variants.

## 8. Future Work

- Search for a monotone functional along the inviscid flow controlling $\nabla\theta$, plausibly a weighted local quantity adapted to the hyperbolic structure near stagnation points.
- Construct a self-similar blow-up profile for inviscid Boussinesq on $\mathbb{R}^2$ with no boundary; then upgrade the regularity of the data from $C^{1,\alpha}$ to $C^\infty$.
- Establish an unconditional vanishing-viscosity limit for Boussinesq in a bounded domain with **Navier slip** boundary conditions, where the velocity layer is weaker — a realistic intermediate target.
- Quantify the rate in (A) in stronger norms ($H^s$, $L^\infty$) and determine whether the exponent $1/2$ is sharp or improves to $1$ for boundaryless smooth data.
- Determine whether $\alpha+\beta\ge1$ is genuinely sharp for global regularity, or whether the threshold can be lowered.

## 9. Key References

- **[Foundational]** J. R. Cannon, E. DiBenedetto. *The initial value problem for the Boussinesq equations with data in $L^p$.* In: Approximation Methods for Navier–Stokes Problems, Lecture Notes in Mathematics 771, Springer, 1980, pp. 129–144.
- **[Foundational]** D. Chae, H.-S. Nam. *Local existence and blow-up criterion for the Boussinesq equations.* Proceedings of the Royal Society of Edinburgh Section A, 127 (1997), 935–946. [DOI](https://doi.org/10.1017/s0308210500026810)
- **[Foundational]** A. Majda, A. Bertozzi. *Vorticity and Incompressible Flow.* Cambridge University Press, 2002.
- **[Foundational]** T. Kato. *Remarks on zero viscosity limit for nonstationary Navier–Stokes flows with boundary.* In: Seminar on Nonlinear PDE, MSRI Publ. 2, Springer, 1984, pp. 85–98. [DOI](https://doi.org/10.1007/978-1-4612-1110-5_6)
- **[SOTA]** D. Chae. *Global regularity for the 2D Boussinesq equations with partial viscosity terms.* Advances in Mathematics, 203 (2006), 497–513. [DOI](https://doi.org/10.1016/j.aim.2005.05.001)
- **[SOTA]** T. Y. Hou, C. Li. *Global well-posedness of the viscous Boussinesq equations.* Discrete and Continuous Dynamical Systems, 12 (2005), 1–12. [DOI](https://doi.org/10.3934/dcds.2005.12.1)
- **[SOTA]** T. Hmidi, S. Keraani. *On the global well-posedness of the two-dimensional Boussinesq system with a zero diffusivity.* Advances in Differential Equations, 12 (2007), 461–480. [DOI](https://doi.org/10.57262/ade/1355867459)
- **[SOTA]** R. Danchin, M. Paicu. *Global well-posedness issues for the inviscid Boussinesq system with Yudovich's type data.* Communications in Mathematical Physics, 290 (2009), 1–14. [DOI](https://doi.org/10.1007/s00220-009-0821-5)
- **[SOTA]** T. Hmidi, S. Keraani, F. Rousset. *Global well-posedness for a Boussinesq–Navier–Stokes system with critical dissipation.* Communications in Partial Differential Equations, 36 (2011), 420–445. [DOI](https://doi.org/10.1016/j.jde.2010.07.008)
- **[SOTA]** Q. Jiu, C. Miao, J. Wu, Z. Zhang. *The two-dimensional incompressible Boussinesq equations with general critical dissipation.* SIAM Journal on Mathematical Analysis, 46 (2014), 3426–3454. [DOI](https://doi.org/10.1137/140958256)
- **[SOTA]** A. Larios, E. Lunasin, E. S. Titi. *Global well-posedness for the 2D Boussinesq system with anisotropic viscosity and without heat diffusion.* Journal of Differential Equations, 255 (2013), 2636–2654. [DOI](https://doi.org/10.1016/j.jde.2013.07.011)
- **[SOTA]** T. M. Elgindi, K. Widmayer. *Sharp decay estimates for an anisotropic linear semigroup and applications to the surface quasi-geostrophic and inviscid Boussinesq systems.* SIAM Journal on Mathematical Analysis, 47 (2015), 4672–4684. [DOI](https://doi.org/10.1137/14099036x)
- **[Recent]** T. M. Elgindi, I.-J. Jeong. *Finite-time singularity formation for strong solutions to the Boussinesq system.* Annals of PDE, 6 (2020), article 5. [DOI](https://doi.org/10.1007/s40818-020-00080-0)
- **[Recent]** G. Luo, T. Y. Hou. *Potentially singular solutions of the 3D axisymmetric Euler equations.* Proceedings of the National Academy of Sciences USA, 111 (2014), 12968–12973. [DOI](https://doi.org/10.1073/pnas.1405238111)
- **[Recent]** J. Chen, T. Y. Hou. *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data.* arXiv:2210.07191 (2022).
- **[Survey]** C. R. Doering, J. D. Gibbon. *Applied Analysis of the Navier–Stokes Equations.* Cambridge University Press, 1995.
- **[Survey]** R. Danchin, M. Paicu. *Global existence results for the anisotropic Boussinesq system in dimension two.* Mathematical Models and Methods in Applied Sciences, 21 (2011), 421–457. [DOI](https://doi.org/10.1142/s0218202511005106)

## 10. Worked Example / Concrete Special Case

**Claim.** On $\mathbb{T}^2$, let $(u,\theta)\in C([0,T];H^s)$, $s>2$, solve the inviscid system, $T<T^*$. Let $(u^{\nu,\kappa},\theta^{\nu,\kappa})$ solve the dissipative system with the same data. Then
$$\sup_{[0,T]}\big(\|u^{\nu,\kappa}-u\|_{L^2}^2+\|\theta^{\nu,\kappa}-\theta\|_{L^2}^2\big) \le (\nu+\kappa)\,K(T),\qquad
K(T)=e^{C\int_0^T(1+\|\nabla u\|_{L^\infty})}\!\!\int_0^T\!\big(\|\nabla u\|_{L^2}^2+\|\nabla\theta\|_{L^2}^2\big).$$

**Proof.** Put $w=u^{\nu,\kappa}-u$, $\eta=\theta^{\nu,\kappa}-\theta$. Subtracting,
$$\partial_t w + (u^{\nu,\kappa}\cdot\nabla)w + (w\cdot\nabla)u = -\nabla q + \nu\Delta u^{\nu,\kappa} + \eta e_2,\qquad
\partial_t\eta + (u^{\nu,\kappa}\cdot\nabla)\eta + (w\cdot\nabla)\theta = \kappa\Delta\theta^{\nu,\kappa}.$$
Test with $w$ and $\eta$. Divergence-free transport and the pressure drop out:
$$\tfrac12\tfrac{d}{dt}\|w\|_{L^2}^2 = -\!\int\! w\cdot\nabla u\cdot w \;+\; \nu\!\int\!\Delta u^{\nu,\kappa}\!\cdot w \;+\;\int\!\eta\,w_2 .$$
Write $\Delta u^{\nu,\kappa}=\Delta w+\Delta u$, so $\nu\int \Delta u^{\nu,\kappa}\cdot w = -\nu\|\nabla w\|_{L^2}^2 - \nu\int\nabla u:\nabla w \le -\tfrac{\nu}{2}\|\nabla w\|^2_{L^2}+\tfrac{\nu}{2}\|\nabla u\|_{L^2}^2$. The first term is $\le\|\nabla u\|_{L^\infty}\|w\|_{L^2}^2$ and the last is $\le\tfrac12(\|w\|^2+\|\eta\|^2)$.

The $\eta$-equation gives, identically,
$$\tfrac12\tfrac{d}{dt}\|\eta\|_{L^2}^2 \le \|\nabla\theta\|_{L^\infty}\|w\|_{L^2}\|\eta\|_{L^2} - \tfrac{\kappa}{2}\|\nabla\eta\|_{L^2}^2 + \tfrac{\kappa}{2}\|\nabla\theta\|_{L^2}^2 .$$
Set $E=\|w\|_{L^2}^2+\|\eta\|_{L^2}^2$. Adding and dropping the negative dissipation terms,
$$\tfrac{d}{dt}E \le C\big(1+\|\nabla u\|_{L^\infty}+\|\nabla\theta\|_{L^\infty}\big)E + \nu\|\nabla u\|_{L^2}^2 + \kappa\|\nabla\theta\|_{L^2}^2 .$$
Since $E(0)=0$, Grönwall gives the claim, with rate $(\nu+\kappa)^{1/2}$ in $L^2$.

**What this shows.** Convergence is unconditional and quantitative — but only *inside* the inviscid existence interval, and the constant $K(T)$ carries $\exp\!\big(\int_0^T\|\nabla\theta\|_{L^\infty}\big)$, the very quantity that Chae–Nam's criterion says must blow up at $T^*$. So the rate degenerates precisely as fast as the unresolved question (B) is unresolved: without a global bound on $A(T)=\int_0^T\|\nabla\theta\|_{L^\infty}$, the inviscid limit is only a local-in-time statement, and no amount of refinement of this energy argument extends it. On a domain with no-slip boundary the argument fails at the first step: $\nu\int\Delta u^{\nu}\cdot w$ produces an uncontrolled boundary term $\nu\int_{\partial\Omega}\partial_n u\cdot w$ because $w\ne 0$ on $\partial\Omega$ — the boundary layer.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*