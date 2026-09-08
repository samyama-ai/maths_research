---
id: 06-pdes/fitzhugh-nagumo-spiral-waves
title: "FitzHugh Nagumo Spiral Waves"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# FitzHugh-Nagumo Spiral Waves

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/fitzhugh-nagumo-spiral-waves` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The problem concerns the existence, stability, and bifurcation dynamics of two-dimensional rotating wave solutions (spiral waves) and three-dimensional scroll waves within the FitzHugh-Nagumo (FHN) reaction-diffusion system. The FHN equations serve as the canonical mathematical model for excitable media, originally formulated as a dimensionally reduced approximation of the Hodgkin-Huxley equations for action potential propagation in squid giant axons.

The formal mathematical problem is three-fold:
1. **Existence:** Rigorously prove the existence of rigidly rotating spiral wave solutions $u(x,y,t) = U^*(r, \theta - \omega t)$ on $\mathbb{R}^2$ across the parameter regimes of excitability and scale separation ($\epsilon$).
2. **Stability:** Classify the spectral and nonlinear stability of these rotating waves, specifically resolving the conditions under which the essential spectrum of the linearized operator crosses the imaginary axis.
3. **Bifurcation:** Analytically capture the transition from rigidly rotating spirals to meandering (quasi-periodic) spirals, and subsequently to spatiotemporal chaos (spiral break-up/fibrillation), mapping these transitions precisely to the parameter space of the PDE without relying on reduced kinematic approximations.

A complete resolution requires proving global existence and stability constraints for the full infinite-dimensional dynamical system on an unbounded domain, fully bridging the fast-slow reaction kinetics at the spiral core with the far-field radiation conditions of Archimedean spirals.

## 2. Mathematical Foundations

The FitzHugh-Nagumo model is a two-component system of parabolic partial differential equations. On a spatial domain $\Omega \subseteq \mathbb{R}^n$ (typically $n=2$ or $3$), the system is given by:

$$ \frac{\partial u}{\partial t} = D_u \Delta u + f(u) - v $$
$$ \frac{\partial v}{\partial t} = D_v \Delta v + \epsilon (g(u) - \gamma v) $$

Here:
- $u(x, t)$ represents the excitatory variable (e.g., membrane potential).
- $v(x, t)$ is the recovery or inhibitory variable.
- $D_u, D_v \ge 0$ are the diffusion coefficients. Often $D_v = 0$ or $D_v \ll D_u$.
- $f(u)$ is a bistable cubic nonlinearity, standardly taken as $f(u) = u(1-u)(u-a)$ with threshold parameter $0 < a < 1$.
- $g(u)$ is a monotonically increasing function, often linear $g(u) = u$.
- $\epsilon > 0$ is a scale separation parameter determining the ratio of time scales between the fast excitation $u$ and the slow recovery $v$.
- $\gamma > 0$ determines the resting state kinetics.

A **rigidly rotating spiral wave** in $\mathbb{R}^2$ is a solution invariant under a continuous helical group action. In polar coordinates $(r, \theta)$, it is defined as:

$$ (u,v)(r, \theta, t) = (U^*, V^*)(r, \theta - \omega t) $$

where $\omega \in \mathbb{R} \setminus \{0\}$ is the angular frequency. By setting $\psi = \theta - \omega t$, the PDEs transform into an elliptic boundary value problem (the co-rotating frame):

$$ D_u \left( \frac{\partial^2 U^*}{\partial r^2} + \frac{1}{r} \frac{\partial U^*}{\partial r} + \frac{1}{r^2} \frac{\partial^2 U^*}{\partial \psi^2} \right) + \omega \frac{\partial U^*}{\partial \psi} + f(U^*) - V^* = 0 $$
$$ D_v \left( \frac{\partial^2 V^*}{\partial r^2} + \frac{1}{r} \frac{\partial V^*}{\partial r} + \frac{1}{r^2} \frac{\partial^2 V^*}{\partial \psi^2} \right) + \omega \frac{\partial V^*}{\partial \psi} + \epsilon (U^* - \gamma V^*) = 0 $$

To be a valid spiral wave, the solution must satisfy periodic boundary conditions in $\psi$ (i.e., $(U^*, V^*)$ are $2\pi$-periodic) and physical conditions at the boundaries of $r$:
- **Core Condition:** $\partial_\psi U^*(0, \psi) = \partial_\psi V^*(0, \psi) = 0$ (continuity at the origin).
- **Far-field Condition:** As $r \to \infty$, the solution asymptotically approaches a one-dimensional periodic wavetrain (an Archimedean spiral).

## 3. History & State of the Art (SOTA)

The mathematical abstraction originated with Richard FitzHugh (1961) and Jin-Ichi Nagumo et al. (1962). While they primarily analyzed 1D pulse propagation, Arthur Winfree (1970s) computationally and theoretically popularized the existence of 2D spiral waves and 3D scroll waves in excitable media, specifically in the context of the Belousov-Zhabotinsky reaction and ventricular fibrillation.

Historically, the analysis of spirals has been divided into two camps:
1. **Kinematic Theory:** (Keener, Tyson, Mikhailov). By treating the spiral wave merely as a 1D curve (the wavefront) parameterized by curvature and normal velocity, researchers mapped out the phase boundaries of rigidly rotating spirals in the $\epsilon \to 0$ limit. This bypassed the full PDEs.
2. **Bifurcation and Spectral Theory:** (Barkley, Sandstede, Scheel, Fiedler). In the 1990s, Barkley computationally demonstrated that rigidly rotating spirals lose stability via a Hopf bifurcation, leading to a meandering state (a quasi-periodic flower-like tip trajectory).

The current SOTA in rigorous mathematics is dominated by the spatial dynamics techniques pioneered by Sandstede and Scheel (2000s). They formalized the spectral mapping theorems for rotating waves on unbounded domains. They proved that the essential spectrum of the linearized FHN operator $\mathcal{L}$ around a spiral wave is entirely determined by the far-field periodic wavetrain. If the absolute spectrum of the far-field wavetrain is bounded away from the imaginary axis, the spiral is robust. 

However, proving the full global existence of the profile $(U^*, V^*)$ analytically from the fundamental FHN PDE—without relying on numerical shooting methods or heavily abstracted kinematic reductions—remains an active barrier.

## 4. Partial Results / Verified Cases

While a general global proof remains elusive, several foundational partial results are established:

- **1D Traveling Pulses:** For $D_v = 0$ and $\epsilon > 0$ sufficiently small, the existence and stability of isolated traveling pulses and periodic wavetrains are fully solved using geometric singular perturbation theory (Jones 1984, Yanagida 1985).
- **The Kinematic Limit ($\epsilon \to 0$):** Under the assumption of infinite scale separation, the existence of the Archimedean spiral is verified via the eikonal equation. The spiral wave frequency $\omega$ has been rigorously shown to scale as $\mathcal{O}(\epsilon^{1/2})$ or $\mathcal{O}(\epsilon)$ depending on the excitability parameters (Keener 1986).
- **Fredholm Properties on $\mathbb{R}^2$:** It has been proven that the linearized operator $\mathcal{L}$ in the co-rotating frame is Fredholm of index zero when formulated in suitably chosen exponentially weighted Sobolev spaces (Sandstede & Scheel 2000). This handles the non-compactness of the spatial domain.
- **Spiral Meandering Bifurcation:** Using center manifold reductions with $SE(2)$ (Special Euclidean group) symmetry, the transition from rigid rotation to meandering has been rigorously classified as a Hopf bifurcation modulo the Euclidean symmetries. The ensuing dynamics (epicycloid vs. hypocycloid meandering) match normal form predictions (Golubitsky et al., 1997).

## 5. Principal Obstacles

The enduring openness of the full FHN spiral wave problem stems from three compounding analytical pathologies:

**1. The Essential Spectrum on Unbounded Domains:**
Because $\mathbb{R}^2$ is unbounded, the spectrum $\sigma(\mathcal{L})$ of the linearization around the spiral contains an essential continuous spectrum. Furthermore, due to the translational and rotational symmetries of the plane, the essential spectrum always touches the imaginary axis at $\lambda = 0$. This precludes the direct application of standard invariant manifold theorems and implicit function theorems, which typically require a strict spectral gap.

**2. Spatial Singularities at the Core:**
In the fast-slow limit ($\epsilon \ll 1$), one typically applies Fenichel's geometric singular perturbation theory. In 1D, this seamlessly splices fast wavefronts with slow recovery pulses. However, in 2D polar coordinates, the spatial dynamics equations treat $r$ as a "time" variable. The terms $1/r$ and $1/r^2$ in the Laplacian create a non-autonomous dynamical system with a severe singularity at $r=0$. At the spiral core, the phase (or wavefront normal) is topologically undefined (a defect). Standard geometric matching fails because the "slow manifold" breaks down at the origin.

**3. Boundary Condition Mismatch:**
Analytical proofs must simultaneously satisfy the zero-derivative conditions at $r=0$ and the radiation conditions matching an exact periodic wavetrain as $r \to \infty$. Finding a heteroclinic connecting orbit in the spatial dynamics formulation that successfully bridges the core singularity to the far-field limit torus is highly complex and currently beyond the reach of standard Melnikov methods.

## 6. The Gap

The precise mathematical barrier lies in the inability to rigorously track the full PDE dynamics across the core-to-far-field spatial transition. The gap is defined by the following missing link:
We currently have rigorous spectral theory mapping out the *implications* of spiral wave existence (i.e., if a spiral exists, here is how it bifurcates), and we have rigorous existence proofs for the *asymptotic extremes* (the 1D far field, and the $\epsilon \to 0$ kinematic curve). 

What is missing is a constructive, analytic existence proof of the stationary profile $(U^*(r,\psi), V^*(r,\psi))$ for $\epsilon > 0$ that maps the local core geometry exactly to the global frequency selection mechanism $\omega(\epsilon)$. The resolution requires a novel extension of geometric singular perturbation theory that can accommodate rotational symmetry and non-autonomous spatial singularities concurrently.

## 7. Current Research (as of June 2026)

Current mathematical approaches are heavily focused on operator theory and spatial dynamics:

- **Exponential Weights and Resolvent Estimates:** Groups at Brown University and the University of Minnesota are extending Fredholm theory using algebraic rather than exponential weights to better capture the algebraic decay of perturbations in the far field of the spiral.
- **Koopman Operator and DMD:** Applied mathematics groups are utilizing Data-Driven approximations (Dynamic Mode Decomposition) to iteratively approximate the eigenfunctions associated with the critical eigenvalues near $\lambda = 0$.
- **Interaction of Multiple Defects:** Research is active regarding the binding and annihilation of multiple spiral wave cores (viewed as topological defects with charges $\pm 1$). The Ginzburg-Landau equation is frequently used as a simplified proxy for FHN in this context.
- **3D Scroll Wave Tension *(frontier — verify)*:** Recent preprints claim to have established a rigorous upper bound on the filament tension of 3D scroll waves in the FHN system, proving that negative tension inevitably leads to filament turbulence (Winfree turbulence).

## 8. Future Work

Leading researchers, including Arnd Scheel and Björn Sandstede, have articulated several necessary pathways to close the gap:
- **Resolution of the Core Singularity:** Developing a spatial blow-up technique (similar to those used in celestial mechanics or fluid dynamics) to regularize the $1/r$ singularity at the core, allowing Fenichel theory to be extended inward to $r=0$.
- **Absolute vs. Convective Instability:** Deriving exact parameter boundaries in the $(a, \epsilon)$ plane for when a spiral wave undergoes absolute instability (the perturbation grows locally at the core) versus convective instability (the perturbation is swept outward to the far-field).
- **Extension to Anisotropic Media:** Analyzing the existence of spirals where the Laplacian is replaced by a tensor $\nabla \cdot (\mathbf{D} \nabla u)$, which breaks the rotational symmetry of the core. This is biologically critical for modeling realistic cardiac tissue.

## 9. Key References

- **[Foundational]** FitzHugh, R. *Impulses and physiological states in theoretical models of nerve membrane.* Biophysical Journal, 1(6):445-466, 1961. (https://doi.org/10.1016/S0006-3495(61)86902-6)
- **[Foundational]** Keener, J. P. *A geometrical theory for spiral waves in excitable media.* SIAM Journal on Applied Mathematics, 46(6):1039-1056, 1986. [DOI](https://doi.org/10.1137/0146062)
- **[SOTA / Spectral Theory]** Sandstede, B., & Scheel, A. *Absolute and convective instabilities of waves on unbounded and large bounded domains.* Physica D: Nonlinear Phenomena, 145(3-4):233-277, 2000. [DOI](https://doi.org/10.1016/s0167-2789(00)00114-7)
- **[SOTA / Bifurcation]** Barkley, D. *Linear stability analysis of rotating spiral waves in excitable media.* Physical Review Letters, 68(13):2090, 1992. [DOI](https://doi.org/10.1103/physrevlett.68.2090)
- **[Survey]** Fiedler, B., & Scheel, A. *Spatio-temporal dynamics of reaction-diffusion patterns.* In Trends in Nonlinear Analysis, Springer, 2003. [DOI](https://doi.org/10.1007/978-3-662-05281-5_2)

## 10. Worked Example / Concrete Special Case

To ground the abstract PDE, consider the **kinematic approximation** of the spiral wave, which simplifies the full FHN system into a geometric boundary value problem. In the limit $\epsilon \to 0$, the sharp excitation wavefront is treated as a 1D curve. 

According to the eikonal equation, the normal velocity $N$ of this curve is given by:
$$ N = c_0 - D \kappa $$
where $c_0$ is the speed of a planar wavefront (a constant derived from the 1D FHN pulse), $D$ is the diffusion coefficient, and $\kappa$ is the local curvature of the front.

Assume the spiral rigidly rotates with angular velocity $\omega$. In polar coordinates $(r, \theta)$, the wavefront is parameterized by $\theta(r, t) = \omega t - \phi(r)$. 
Using differential geometry, the normal velocity and curvature for this curve are:
$$ N = \frac{\omega r}{\sqrt{1 + (r \phi')^2}}, \quad \kappa = \frac{r \phi'' + \phi' (1 + (r \phi')^2)}{r (1 + (r \phi')^2)^{3/2}} $$
where primes denote differentiation with respect to $r$.

Substituting these into the eikonal equation yields a second-order nonlinear ODE for the shape of the spiral arm $\phi(r)$:
$$ \frac{\omega r}{\sqrt{1 + (r \phi')^2}} = c_0 - D \frac{r \phi'' + \phi' (1 + (r \phi')^2)}{r (1 + (r \phi')^2)^{3/2}} $$

**Calculated Instance:**
To find a physical spiral, we must solve this ODE subject to boundary conditions. 
1. **At the core ($r=0$):** The wavefront must be smooth, so $\phi'(0) = 0$.
2. **In the far-field ($r \to \infty$):** The curvature $\kappa \to 0$. The normal velocity approaches the plane wave speed $c_0$. Therefore, $\frac{\omega r}{\sqrt{1 + (r \phi')^2}} \approx \frac{\omega r}{r \phi'} = \frac{\omega}{\phi'} = c_0$. This gives the Archimedean spiral condition $\phi'(r) \to \omega/c_0$ as $r \to \infty$.

This forms a nonlinear eigenvalue problem. The frequency $\omega$ is not arbitrary; it acts as an eigenvalue that must be tuned so that the solution satisfying the core condition $\phi'(0)=0$ successfully limits to the required asymptotic slope $\omega/c_0$ at infinity. This kinematic reduction elegantly illustrates how the temporal frequency of the 2D spiral is fundamentally selected by the medium's local excitability ($c_0$) and diffusion ($D$), circumventing the infinite-dimensional PDE.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*