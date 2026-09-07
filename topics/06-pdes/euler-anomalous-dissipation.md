---
id: 06-pdes/euler-anomalous-dissipation
title: "Euler Anomalous Dissipation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Euler Anomalous Dissipation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/euler-anomalous-dissipation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The anomalous dissipation problem for the incompressible Euler equations—frequently referred to as the mathematical formulation of the Zeroth Law of Turbulence—investigates the vanishing viscosity limit of the Navier-Stokes equations at high Reynolds numbers. It questions whether the macroscopic kinetic energy of a turbulent fluid continues to dissipate at a strictly positive rate in the limit as the kinematic viscosity $\nu \to 0$.

Let $u^\nu(x,t)$ be a family of solutions to the 3D incompressible Navier-Stokes equations. The global energy dissipation rate is defined by $\epsilon_\nu(t) = \nu \int_\Omega |\nabla u^\nu(x,t)|^2 \,dx$. The Zeroth Law conjectures that for sufficiently turbulent initial data, the infinite Reynolds number limit exhibits anomalous dissipation:
$$ \lim_{\nu \to 0} \epsilon_\nu(t) = \epsilon(t) > 0. $$
Because the limit $u^\nu \to u$ formally satisfies the inviscid Euler equations, this strictly positive limit necessitates that the resulting weak solution of the Euler equations cannot conserve energy. 

This leads to the **Onsager Conjecture** (now a proven theorem), which forms the core of the problem: Weak solutions to the Euler equations with Hölder regularity exponent $\alpha < 1/3$ can spontaneously dissipate kinetic energy, whereas solutions with $\alpha > 1/3$ strictly conserve it. The overarching open conjecture is whether the specific weak Euler solutions arising as physically realizable limits of Navier-Stokes are precisely these energy-dissipating "rough" solutions.

## 2. Mathematical Foundations

The fluid motion in a domain $\Omega \subseteq \mathbb{R}^3$ (often the torus $\mathbb{T}^3$ or $\mathbb{R}^3$) is governed by the incompressible Navier-Stokes equations:
$$ \partial_t u^\nu + (u^\nu \cdot \nabla)u^\nu + \nabla p^\nu = \nu \Delta u^\nu, \quad \nabla \cdot u^\nu = 0 $$
where $u^\nu$ is the velocity vector field, $p^\nu$ is the scalar pressure, and $\nu > 0$ is the kinematic viscosity. 

Formally setting $\nu = 0$ yields the incompressible Euler equations:
$$ \partial_t u + (u \cdot \nabla)u + \nabla p = 0, \quad \nabla \cdot u = 0 $$

The total kinetic energy of the fluid at time $t$ is $E^\nu(t) = \frac{1}{2} \int_\Omega |u^\nu(x,t)|^2 \,dx$. By taking the $L^2$ inner product of the Navier-Stokes equations with $u^\nu$ and integrating by parts, the energy balance is given by:
$$ \frac{d}{dt} E^\nu(t) = -\nu \int_\Omega |\nabla u^\nu(x,t)|^2 \,dx \equiv -\epsilon_\nu(t). $$
For classical, smooth solutions to the Euler equations, the analogous computation without the viscous term forces $\frac{d}{dt}E(t) = 0$. However, weak solutions $u \in L^\infty(0, T; L^2(\Omega))$ satisfy the Euler equations only in the sense of distributions and lack the regularity required to justify the integration by parts.

The critical regularity scale for this phenomenon is measured in Hölder spaces or, more precisely, Besov spaces. A function is in the Hölder space $C^\alpha$ if $|u(x) - u(y)| \le K |x - y|^\alpha$. The Besov space $B^\alpha_{p,\infty}$ is often used as a finer scale, where the $1/3$ exponent originates directly from the Kolmogorov 1941 (K41) scaling law for structure functions in fully developed turbulence:
$$ \langle |u(x+r) - u(x)|^3 \rangle \sim \epsilon r. $$

Duchon and Robert (2000) formalized the local energy dissipation measure $D(u)$ for weak Euler solutions using mollifiers $\phi_\ell$:
$$ D(u) = \lim_{\ell \to 0} \frac{1}{4} \int \nabla \phi_\ell (y) \cdot \delta_y u |\delta_y u|^2 \,dy $$
where $\delta_y u = u(x+y) - u(x)$. Anomalous dissipation requires $D(u) > 0$.

## 3. History & State of the Art (SOTA)

The history of the problem bridges statistical physics and rigorous partial differential equations. In 1941, A.N. Kolmogorov established the phenomenological necessity of non-vanishing dissipation ($\epsilon > 0$) as $\nu \to 0$ in his theory of turbulence.

In 1949, Lars Onsager published *Statistical Hydrodynamics*, framing Kolmogorov's hypothesis as a mathematical property of the Euler equations. He conjectured the exact $1/3$ Hölder exponent threshold separating conservative from dissipative solutions. 

**The Conservative Regime ($\alpha > 1/3$):** 
The rigid half of the conjecture was proven by Constantin, E, and Titi (1994), building on Eyink (1994). They demonstrated rigorously that if a weak solution belongs to the Besov space $L^3(0, T; B^{\alpha}_{3,\infty}(\mathbb{R}^3))$ with $\alpha > 1/3$, the Duchon-Robert dissipation measure vanishes ($D(u) = 0$), and energy is strictly conserved. 

**The Dissipative Regime ($\alpha < 1/3$):** 
The flexible half of the conjecture resisted proof for decades. In 2009, De Lellis and Székelyhidi Jr. introduced convex integration (developed by Gromov for isometric embeddings) into fluid dynamics, generating highly non-unique, low-regularity weak Euler solutions. Iterative improvements to the convex integration scheme culminated in 2018 when Philip Isett proved the existence of non-trivial Euler solutions in $C^\alpha$ for $\alpha < 1/3$ that strictly dissipate energy. Buckmaster, De Lellis, Székelyhidi, and Vicol (2019) subsequently proved that one could construct dissipative weak solutions that are continuous in time and spatial Hölder continuous up to the critical threshold.

The State of the Art completely resolves the Onsager conjecture for the Euler equations. However, the overarching problem—whether the physical Navier-Stokes limits actually select these specific wild solutions to achieve anomalous dissipation—remains largely unsolved.

## 4. Partial Results / Verified Cases

While the Zeroth Law for the 3D unforced Navier-Stokes equations remains open, anomalous dissipation has been rigorously verified in Several reduced regimes:

1. **Burgers' Equation (1D):** For the one-dimensional viscous Burgers' equation $\partial_t u^\nu + u^\nu \partial_x u^\nu = \nu \partial_{xx} u^\nu$, anomalous dissipation is proven. The formation of shocks creates regions where $\partial_x u^\nu \sim \mathcal{O}(\nu^{-1})$, forcing the dissipation integral to remain strictly positive as $\nu \to 0$.
2. **Passive Scalar Turbulence:** Anomalous dissipation of scalar variance has been rigorously proven for passive scalars advected by sufficiently rough velocity fields. Bedrossian, Blumenthal, and Punshon-Smith (2022) established anomalous dissipation for the advection-diffusion equation when driven by a stochastic Navier-Stokes velocity field, verifying Batchelor scaling.
3. **Bounded Domains (Kato's Condition):** Tosio Kato (1984) proved that anomalous dissipation in domains with no-slip boundaries occurs if and only if the dissipation strictly within a boundary layer of thickness proportional to $\nu$ remains positive: $\lim_{\nu \to 0} \nu \int_0^T \int_{\Gamma_{c\nu}} |\nabla u^\nu|^2 \,dx \,dt > 0$. Constantin and Nguyen (2018) verified related localized boundary conditions.
4. **Forced and Stochastic Navier-Stokes:** In systems equipped with additive Gaussian noise forcing at low wavenumbers, rigorous bounds on the invariant measures (stationary statistical solutions) demonstrate a non-vanishing average energy dissipation rate (Flandoli, Romito).

## 5. Principal Obstacles

The fundamental bottleneck separating current PDE methods from the resolution of the Navier-Stokes limit is the intractability of bounding singularity formation and tracking high-frequency energy cascades.

1. **Weak Compactness and Energy Drop:** To prove that $\lim_{\nu \to 0} u^\nu$ is a dissipative Euler solution, one needs strong compactness in $L^2$. Standard a priori energy estimates yield only weak compactness in $L^2$. Consequently, an observed energy drop in the limit could technically result from the lower semi-continuity of the weak limit (energy escaping to infinite frequencies) rather than genuine physical dissipation via nonlinear cascading.
2. **Non-Uniqueness of Wild Solutions:** Convex integration constructs an infinite dimensional manifold of dissipative Euler solutions. There is no known mathematical "entropy condition" (analogous to the Kružkov entropy for scalar conservation laws) that uniquely identifies which, if any, of these wild solutions represents the physical $\nu \to 0$ limit.
3. **Absence of Uniform Enstrophy Lower Bounds:** Proving anomalous dissipation strictly requires establishing $\int |\nabla u^\nu|^2 \,dx \ge c \nu^{-1}$. This demands proving that the fluid *must* generate sufficiently small scales everywhere (eddies of size $\sim \nu^{3/4}$ per Kolmogorov scaling). Current nonlinear estimates are incapable of ruling out scenarios where the fluid spontaneously self-organizes into a smooth, laminar state that bypasses the cascade entirely.

## 6. The Gap

The exact mathematical gap lies in establishing the mapping between viscous regularization and convex integration. We have two isolated facts:
- (A) Navier-Stokes solutions $u^\nu$ exist for $\nu > 0$ and possess strong dissipative mechanisms.
- (B) Dissipative weak Euler solutions $u$ exist in $C^{\alpha}$ for $\alpha < 1/3$ via convex integration.

The barrier is proving that for a generic, open set of high-Reynolds initial data $u_0 \in L^2$, the deterministic sequence of viscous solutions $u^\nu(t)$ specifically satisfies $\lim_{\nu \to 0} \epsilon_\nu(t) > 0$. Convex integration inherently relies on adding high-frequency, non-local oscillations to the flow field; however, these exact high-frequency modes are aggressively damped by the Laplacian $\nu \Delta u^\nu$ in the Navier-Stokes equations, making it currently impossible to smoothly bridge the viscous construction with the inviscid wild solutions.

## 7. Current Research (as of June 2026)

Active research directions are heavily focused on probabilistic and computational approaches:

- **Spontaneous Stochasticity:** Researchers including Eyink, Drivas, and Flandoli are pursuing the hypothesis that deterministic rough initial data leads to a probabilistic ensemble of solutions in the $\nu \to 0$ limit. Under this framework, the trajectories $u^\nu$ converge to a Markovian measure on the space of trajectories. *(frontier — verify)* Anomalous dissipation is formulated as a property of this limiting measure rather than a single deterministic limit.
- **Computer-Assisted Singularity Profiling:** Following Hou and Chen's recent breakthroughs (2022) demonstrating finite-time singularity formation for the 3D Euler equations, efforts are underway to perturb these singular profiles with small viscosity to analytically extract a strictly positive anomalous dissipation rate as the blow-up is regularized.
- **Intermittency Corrections:** Exploring the discrepancy between the $1/3$ Onsager threshold and the slightly lower exponents observed empirically in turbulent flows due to spatial intermittency (multifractal models), requiring fine-tuned Besov and Triebel-Lizorkin space analysis.

## 8. Future Work

Leading researchers have articulated several strategic pathways to cross the current barriers:
- **Formulation of Admissibility Criteria:** Develop a rigorous selection principle for the 3D Euler equations that acts as a definitive filter, capable of singling out the unique Navier-Stokes limit from the vast pool of convex integration solutions.
- **Localized Dissipation Bounds:** Focus on proving anomalous dissipation locally in space—specifically around vortex tubes or singular sets—rather than demanding a global lower bound. This requires high-resolution localized extensions of the Kármán-Howarth-Monin turbulence relations.
- **Resolution of Kato's Boundary Limit:** Fully resolve the vanishing viscosity limit for smooth initial data in bounded domains. Since solid boundaries continuously inject vorticity into the bulk fluid, proving that boundary layer detachment scales exactly to satisfy Kato's criterion is a highly viable path to proving anomalous dissipation.

## 9. Key References

- **[Foundational]** Onsager, L. *Statistical hydrodynamics.* Il Nuovo Cimento (1943-1954), 6(2), 279-287, 1949.
- **[Foundational]** Constantin, P., E, W., & Titi, E. S. *Onsager's conjecture on the energy conservation for solutions of Euler's equation.* Communications in Mathematical Physics, 165(1), 207-209, 1994.
- **[Foundational]** Duchon, J., & Robert, R. *Inertial energy dissipation for weak solutions of incompressible Euler and Navier-Stokes equations.* Nonlinearity, 13(1), 249, 2000.
- **[SOTA / Recent]** Isett, P. *A proof of Onsager's conjecture.* Annals of Mathematics, 188(3), 871-963, 2018.
- **[SOTA / Recent]** Buckmaster, T., De Lellis, C., Székelyhidi Jr, L., & Vicol, V. *Onsager's conjecture for admissible weak solutions.* Communications on Pure and Applied Mathematics, 72(2), 229-274, 2019.
- **[SOTA / Recent]** Bedrossian, J., Blumenthal, A., & Punshon-Smith, S. *The Batchelor spectrum of passive scalar turbulence in stochastic fluid mechanics.* Communications on Pure and Applied Mathematics, 75(1), 143-221, 2022.
- **[Survey]** Eyink, G. L. *Review of the Onsager "Ideal Turbulence" Theory.* arXiv preprint arXiv:1803.02223, 2018.

## 10. Worked Example / Concrete Special Case

To explicitly understand the mechanism by which vanishing viscosity results in strict energy dissipation, we analyze the 1D viscous Burgers' equation, a rigorous mathematical analogue for fluid compression:
$$ \partial_t u^\nu + u^\nu \partial_x u^\nu = \nu \partial_{xx} u^\nu. $$

Consider smooth, periodic initial data $u_0(x) = -\sin(x)$ on the domain $[-\pi, \pi]$. 
In the inviscid case ($\nu = 0$), the method of characteristics indicates that the wave profile steepens. The velocity at $x=0$ remains $0$, but the fluid at $x>0$ travels left ($u < 0$) and at $x<0$ travels right ($u > 0$). At a critical time $T_c = 1$, the spatial gradient at $x=0$ blows up to infinity, forming a shock wave.

For $\nu > 0$, the Laplacian term prevents a strict discontinuity. Instead, it forms a "viscous shock"—a rapid transition layer localized around $x=0$ that connects the positive velocity state to the negative velocity state. The spatial width of this transition layer is heavily compressed by the flow and scales exactly as $\mathcal{O}(\nu)$.

Across this layer, the velocity $u^\nu$ jumps from an amplitude of approximately $U$ to $-U$. 
Therefore, the spatial derivative inside the shock layer is highly concentrated and scales inversely with viscosity:
$$ \partial_x u^\nu \approx \frac{\Delta u}{\text{width}} \sim \frac{-2U}{\nu} \sim \mathcal{O}(\nu^{-1}). $$

The global energy dissipation rate is determined by the integral of the squared gradient over the entire domain:
$$ \epsilon_\nu(t) = \nu \int_{-\pi}^\pi |\partial_x u^\nu|^2 \,dx. $$
Because the dominant contribution to this integral arises strictly from the viscous shock layer of width $\mathcal{O}(\nu)$, we can accurately estimate the integral for $t > T_c$:
$$ \epsilon_\nu(t) \approx \nu \cdot \left(\text{width}\right) \cdot (\partial_x u^\nu)^2 \sim \nu \cdot (\nu) \cdot \left(\frac{1}{\nu}\right)^2 = \mathcal{O}(1). $$

Taking the exact limit as $\nu \to 0$ after the shock formation time yields:
$$ \lim_{\nu \to 0} \epsilon_\nu(t) = \epsilon > 0. $$
This computation isolates the core mechanism of anomalous dissipation: the physical gradients in the fluid become increasingly sharp (blowing up at a rate of $1/\nu$), perfectly counterbalancing the vanishing viscosity prefactor $\nu$. The limiting inviscid solution $u$ is rough (a step function, meaning $\alpha \to 0 < 1/3$), and its kinetic energy strictly decreases, explicitly demonstrating the turbulent energy cascade theorized for 3D Navier-Stokes.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*