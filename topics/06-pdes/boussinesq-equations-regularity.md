---
id: 06-pdes/boussinesq-equations-regularity
title: "Boussinesq Equations Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boussinesq Equations Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/boussinesq-equations-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

**Question.** Do smooth, compactly supported (or periodic) initial data for the **two-dimensional inviscid Boussinesq system** on $\mathbb{R}^2$ or $\mathbb{T}^2$ produce solutions that stay smooth for all time?

$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \theta\, e_2, \qquad \partial_t\theta + (u\cdot\nabla)\theta = 0, \qquad \nabla\cdot u = 0 .$$

Here $u:\mathbb{R}^2\times[0,T)\to\mathbb{R}^2$ is velocity, $p$ pressure, $\theta$ a scalar (temperature or density), $e_2=(0,1)$.

A complete resolution means either:

- **(Regularity)** For every $u_0\in H^s$, $\theta_0\in H^s$, $s>2$, with $\nabla\cdot u_0=0$, the unique local solution extends to $[0,\infty)$ in $H^s$; or
- **(Blowup)** Explicit smooth data whose solution satisfies $\int_0^{T^*}\|\nabla\theta(t)\|_{L^\infty}\,dt=\infty$ for some $T^*<\infty$.

The same question is open for every **partially dissipative** variant weaker than those in §4, and for the **3D axisymmetric Euler equations without swirl away from the axis**, which are formally identical to the 2D Boussinesq system. Solving 2D inviscid Boussinesq is widely regarded as the accessible model problem for 3D Euler blowup.

## 2. Mathematical Foundations

**Vorticity formulation.** With $\omega=\partial_1u_2-\partial_2u_1$,

$$\partial_t\omega + (u\cdot\nabla)\omega = \partial_1\theta, \qquad \partial_t\theta+(u\cdot\nabla)\theta=0, \qquad u=\nabla^{\perp}\Delta^{-1}\omega,$$

with $\nabla^\perp=(-\partial_2,\partial_1)$. Unlike 2D Euler ($\theta\equiv0$), $\omega$ is **not** transported: the baroclinic term $\partial_1\theta$ is a source.

**Conserved / controlled quantities.**
$$\|\theta(t)\|_{L^p}=\|\theta_0\|_{L^p}\ \ (1\le p\le\infty), \qquad \frac{d}{dt}\Big(\tfrac12\|u\|_{L^2}^2\Big)=\int \theta\,u_2 ,$$
so energy grows at most linearly and $\|u(t)\|_{L^2}\le \|u_0\|_{L^2}+t\|\theta_0\|_{L^2}$. The gradient obeys
$$\frac{d}{dt}\|\nabla\theta\|_{L^\infty}\le \|\nabla u\|_{L^\infty}\|\nabla\theta\|_{L^\infty},\qquad \frac{d}{dt}\|\omega\|_{L^\infty}\le\|\nabla\theta\|_{L^\infty},$$
and $\|\nabla u\|_{L^\infty}\lesssim \|\omega\|_{L^\infty}\log(e+\|\omega\|_{H^s})$. The closed system is **supercritical**: no conserved quantity controls $\|\nabla\theta\|_{L^\infty}$.

**Blow-up criterion (Beale–Kato–Majda analogue, Chae–Nam 1997).** The $H^s$ solution, $s>2$, extends past $T$ iff
$$\int_0^{T}\|\nabla\theta(t)\|_{L^\infty}\,dt<\infty .$$

**Boussinesq–Navier–Stokes family.** With fractional dissipation,
$$\partial_t u+(u\cdot\nabla)u+\nu\Lambda^{\alpha}u=-\nabla p+\theta e_2,\qquad \partial_t\theta+(u\cdot\nabla)\theta+\kappa\Lambda^{\beta}\theta=0,\qquad \Lambda=(-\Delta)^{1/2}.$$
The regularity question is graded by $(\nu,\kappa,\alpha,\beta)$; the inviscid case is $\nu=\kappa=0$.

**Equivalence with 3D axisymmetric Euler.** For axisymmetric $u=u^r e_r+u^z e_z+u^\theta e_\theta$, set $\theta_{\mathrm{Bou}} = (r u^{\theta})^2$ and identify $(r,z)\leftrightarrow(x_2,x_1)$; away from the axis $r=0$ the swirl-carrying 3D Euler system becomes the 2D Boussinesq system with lower-order corrections in $1/r$.

## 3. History & State of the Art (SOTA)

- **1903 / classical.** The Boussinesq approximation (buoyancy retained only in the momentum forcing) enters geophysical fluid dynamics; see Majda–Bertozzi (2002) for the modern mathematical framing and the 3D-Euler analogy.
- **1997.** Chae & Nam prove local well-posedness in $H^s$, $s>2$, and the $\int\|\nabla\theta\|_{L^\infty}$ criterion.
- **2005–2006.** Two independent breakthroughs settle the **partially viscous** cases: Hou & Li (full viscosity in $u$, no diffusion in $\theta$) and Chae (either $\nu>0,\kappa=0$ or $\nu=0,\kappa>0$). Global regularity holds; best-known upper bounds on $\|\nabla\theta\|_{L^\infty}$ are double-exponential in $t$.
- **2010–2011.** Hmidi, Keraani & Rousset handle **critical** dissipation: $\nu>0$ with $\kappa\Lambda\theta$, and $\nu\Lambda u$ with $\kappa>0$, using the modified vorticity $\Gamma=\omega\pm\mathcal{R}\theta$ ($\mathcal{R}$ a Riesz transform) which cancels the baroclinic term to leading order.
- **2010–2013.** Anisotropic dissipation: Adhikari–Cao–Wu (vertical viscosity *and* vertical diffusivity), then Cao & Wu (vertical viscosity + horizontal diffusion, and relatives) give global regularity with only one directional derivative dissipated.
- **2014.** Luo & Hou's numerics on the 3D axisymmetric Euler equations in a cylinder exhibit a stable, nearly self-similar blowup **on the boundary** — the same mechanism in the Boussinesq reduction.
- **2020.** Elgindi & Jeong prove **finite-time singularity** for the inviscid 2D Boussinesq system in domains with a corner, for scale-invariant/$C^{0,\alpha}$-type data.
- **2021–2023.** Chen & Hou give a rigorous, computer-assisted proof of finite-time blowup for 2D Boussinesq and 3D Euler **with boundary** for $C^{1,\alpha}$ velocity (2021), then for **smooth data** with boundary (2022–2023 preprints, now peer-reviewed).
- **Still open:** smooth data, no boundary, no dissipation, on $\mathbb{R}^2$ or $\mathbb{T}^2$.

## 4. Partial Results / Verified Cases

Global regularity is **proved** for:

| Case | Result |
|---|---|
| $\nu>0$, $\kappa=0$, $\alpha=2$ (viscosity, no diffusion) | Hou–Li 2005; Chae 2006 — global in $H^s$, $s\ge3$ |
| $\nu=0$, $\kappa>0$, $\beta=2$ (diffusion, no viscosity) | Chae 2006 — global |
| $\nu>0$, $\kappa\Lambda\theta$ (critical diffusion) | Hmidi–Keraani–Rousset 2010 |
| $\nu\Lambda u$, $\kappa>0$ (critical viscosity) | Hmidi–Keraani–Rousset 2011 |
| $\nu\Lambda^\alpha u+\kappa\Lambda^\beta\theta$, $\alpha+\beta\ge1$ (roughly) | Hmidi–Keraani–Rousset and successors; sharp thresholds partly open |
| vertical viscosity $\nu\partial_{22}u$ + vertical diffusivity $\kappa\partial_{22}\theta$ | Adhikari–Cao–Wu 2010 |
| vertical viscosity + horizontal diffusion (and mirror case) | Cao–Wu 2013 |
| $\theta$ independent of $x_1$, or $\theta_0$ constant | reduces to 2D Euler — global (Yudovich/Wolibner) |
| $\nu=\kappa=0$, small data near hydrostatic equilibrium in $\mathbb{T}\times\mathbb{R}$ | long-time / stability results (Elgindi–Widmayer; Doering et al. for damped variants) |

Blowup is **proved** for:

- 2D inviscid Boussinesq on a **corner domain**, scale-invariant data, Elgindi–Jeong 2020.
- 2D inviscid Boussinesq on the **half-plane / cylinder boundary** with $C^{1,\alpha}$ velocity, $\alpha$ small: Chen–Hou 2021; and with **smooth** data: Chen–Hou 2022–2023 (computer-assisted).
- 1D and "hyperbolic" model equations retaining the baroclinic feedback: Kiselev–Tan 2018; Choi–Kiselev–Yao 2015 for the CKY model.

Numerics: Luo–Hou (2014) resolve $\|\omega\|_{L^\infty}\sim (T^*-t)^{-1}$ with $T^*\approx0.0035056$ in their axisymmetric setup, with $\sim10^{12}$ effective grid points near the boundary.

## 5. Principal Obstacles

- **Supercriticality.** The system has no coercive conserved quantity above the transport level: $\|\theta\|_{L^\infty}$ and $\|u\|_{L^2}$ scale below the critical norm controlling $\nabla u$. Every known a priori bound is one derivative short of closing $\int\|\nabla\theta\|_{L^\infty}$.
- **Loss of the vorticity maximum principle.** In 2D Euler $\|\omega\|_{L^\infty}$ is conserved, which is exactly what forbids blowup. The baroclinic source $\partial_1\theta$ destroys this, and no substitute quantity is known in the inviscid, boundary-free case. The Hmidi–Keraani–Rousset trick ($\Gamma=\omega-\mathcal{R}\theta$) needs dissipation to absorb the commutator $[\mathcal{R},u\cdot\nabla]\theta$; at $\nu=\kappa=0$ the commutator is of the same order as the term it cancels.
- **Nonlocality of $u=\nabla^\perp\Delta^{-1}\omega$.** The Biot–Savart law is a singular integral: $\nabla u$ is only log-controlled by $\|\omega\|_{L^\infty}$, so perturbative/Fourier arguments lose precisely the borderline logarithm. Paraproduct and Besov techniques recover $B^0_{\infty,1}$ endpoints but not the full nonlinear feedback.
- **Boundary vs. no boundary.** All rigorous blowup proofs use either a corner or a solid wall to suppress the "compressive" degrees of freedom and produce a stable hyperbolic stagnation point. Without a boundary, an unstable manifold of the self-similar profile appears, and the approximate self-similar solutions constructed by the same methods are no longer stable — the fixed-point argument has an unstable direction.
- **Computer-assisted proofs do not transfer.** Chen–Hou's interval-arithmetic control of the linearized operator is built around a specific boundary geometry; in free space the linearization has essential spectrum touching the imaginary axis and the numerical enclosures fail.

## 6. The Gap

Proved: blowup **with** a boundary or corner (§4), and regularity **with** any of a long list of dissipations. Open: the pure case $\nu=\kappa=0$, smooth data, $\mathbb{R}^2$ or $\mathbb{T}^2$.

The exact step is: construct a **stable, self-similar (or nearly self-similar) blowup profile of the 2D Boussinesq system in free space**, i.e. a solution of
$$-(1+c_\omega)\Omega+(c_l\, y\cdot\nabla)\Omega+U\cdot\nabla\Omega=\partial_1 H,\qquad -2c_\omega H+(c_l\,y\cdot\nabla)H+U\cdot\nabla H=0$$
in self-similar variables $y=x/(T^*-t)^{c_l}$, whose linearization has no unstable eigenvalue apart from those killed by symmetry — *or* prove an a priori bound on $\|\nabla\theta\|_{L^\infty}$ for free-space data that rules such profiles out. Equivalently: remove the boundary from the Chen–Hou construction, or find the missing conserved structure.

## 7. Current Research (as of June 2026)

- **Caltech / NYU (Hou, Chen, Elgindi, Jeong).** Extending computer-assisted, nearly-self-similar frameworks from boundary to free space; refining $C^{1,\alpha}$-to-$C^\infty$ transfer. *(frontier — verify)* Reports of interior-blowup scenarios for smooth Boussinesq data with a degenerate (non-boundary) hyperbolic point remain unpublished.
- **Princeton / Duke / Rice (Kiselev, Yao, and collaborators).** Small-scale creation and growth-rate lower bounds: double-exponential gradient growth for related 2D active-scalar systems, aiming at nonlinear amplification without a wall.
- **Oklahoma State / Notre Dame / Chinese groups (Wu and collaborators).** Sharpening the $(\alpha,\beta)$ dissipation frontier: current work pushes global regularity toward $\alpha+\beta$ strictly below $1$ under structural assumptions, and treats damping-only ($-\nu u$) and partially-damped models.
- **Stability-of-equilibrium school (Elgindi, Widmayer, Bianchini, Coti Zelati).** Global existence for small perturbations of stably stratified states $\theta_0=x_2$, where the buoyancy frequency provides dispersion.
- **Rigorous numerics / neural self-similar profiles.** Physics-informed-network searches for Boussinesq/Euler self-similar profiles followed by interval-arithmetic validation. *(frontier — verify)*

## 8. Future Work

1. **Free-space self-similar profiles.** Search for profiles with $c_l\ne1$ (non-Euler-scaling) admitted by the extra parameter in Boussinesq; prove stability by a Lyapunov/energy functional adapted to the $\Omega$–$H$ coupling.
2. **Replace the wall with symmetry.** Odd-in-$x_1$, even-in-$x_2$ data on $\mathbb{T}^2$ mimic the boundary hyperbolic point; quantify whether the induced compression is strong enough (Hou's stated program).
3. **Sharpen the blow-up criterion.** Prove a Constantin–Fefferman–Majda-type geometric criterion: regularity if $\nabla^\perp\theta/|\nabla^\perp\theta|$ stays Lipschitz on the region where $|\nabla\theta|$ is large.
4. **Close the $\alpha+\beta$ threshold.** Determine the sharp dissipation exponent separating global regularity from possible blowup; the conjectured line is $\alpha+\beta=1$ but neither side is settled at the endpoint.
5. **Transfer to 3D Euler.** Any free-space Boussinesq blowup should yield an axisymmetric-with-swirl 3D Euler singularity away from the axis; the $1/r$ correction terms must be shown subcritical.

## 9. Key References

- **[Foundational]** A. Majda and A. Bertozzi. *Vorticity and Incompressible Flow.* Cambridge Texts in Applied Mathematics, Cambridge University Press, 2002.
- **[Foundational]** D. Chae and H.-S. Nam. *Local existence and blow-up criterion for the Boussinesq equations.* Proceedings of the Royal Society of Edinburgh Section A, 127(5):935–946, 1997. [DOI](https://doi.org/10.1017/s0308210500026810)
- **[Foundational]** T. Y. Hou and C. Li. *Global well-posedness of the viscous Boussinesq equations.* Discrete and Continuous Dynamical Systems, 12(1):1–12, 2005. [DOI](https://doi.org/10.3934/dcds.2005.12.1)
- **[Foundational]** D. Chae. *Global regularity for the 2D Boussinesq equations with partial viscosity terms.* Advances in Mathematics, 203(2):497–513, 2006. [DOI](https://doi.org/10.1016/j.aim.2005.05.001)
- **[SOTA]** T. Hmidi, S. Keraani and F. Rousset. *Global well-posedness for a Boussinesq–Navier–Stokes system with critical dissipation.* Journal of Differential Equations, 249(9):2147–2174, 2010. [DOI](https://doi.org/10.1016/j.jde.2010.07.008)
- **[SOTA]** T. Hmidi, S. Keraani and F. Rousset. *Global well-posedness for Euler–Boussinesq system with critical dissipation.* Communications in Partial Differential Equations, 36(3):420–445, 2011. [DOI](https://doi.org/10.1080/03605302.2010.518657)
- **[SOTA]** D. Adhikari, C. Cao and J. Wu. *The 2D Boussinesq equations with vertical viscosity and vertical diffusivity.* Journal of Differential Equations, 249(5):1078–1088, 2010. [DOI](https://doi.org/10.1016/j.jde.2010.03.021)
- **[SOTA]** C. Cao and J. Wu. *Global regularity for the two-dimensional anisotropic Boussinesq equations with vertical dissipation.* Archive for Rational Mechanics and Analysis, 208(3):985–1004, 2013. [DOI](https://doi.org/10.1007/s00205-013-0610-3)
- **[SOTA / Recent]** T. M. Elgindi and I.-J. Jeong. *Finite-time singularity formation for strong solutions to the Boussinesq system.* Annals of PDE, 6, article 5, 2020. [DOI](https://doi.org/10.1007/s40818-020-00080-0)
- **[SOTA / Recent]** J. Chen and T. Y. Hou. *Finite time blowup of 2D Boussinesq and 3D Euler equations with $C^{1,\alpha}$ velocity and boundary.* Communications in Mathematical Physics, 383:1559–1667, 2021. [DOI](https://doi.org/10.1007/s00220-021-04067-1)
- **[SOTA / Recent]** J. Chen and T. Y. Hou. *Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data.* Parts I (Analysis) and II (Rigorous numerics), arXiv preprints 2210.07191 and 2305.05660, 2022–2023.
- **[Computational]** G. Luo and T. Y. Hou. *Potentially singular solutions of the 3D axisymmetric Euler equations.* Proceedings of the National Academy of Sciences USA, 111(36):12968–12973, 2014. [DOI](https://doi.org/10.1073/pnas.1405238111)
- **[Model equations]** A. Kiselev and C. Tan. *Finite time blow up in the hyperbolic Boussinesq system.* Advances in Mathematics, 325:34–55, 2018. [DOI](https://doi.org/10.1016/j.aim.2017.11.019)
- **[Survey]** T. M. Elgindi and I.-J. Jeong. Expository work on singularity formation for incompressible fluids; see also J. Wu, *Well-posedness of a class of partial differential equations with applications to fluids*, lecture notes/monograph series, and D. Chae, P. Constantin and J. Wu, *An incompressible 2D didactic model with singularity and explicit solutions of the 2D Boussinesq equations*, Journal of Mathematical Fluid Mechanics, 16:473–480, 2014.

## 10. Worked Example / Concrete Special Case

**An exact solution isolating the baroclinic source.** Look for data with $\theta$ depending only on $x_1$ and velocity purely vertical:
$$u(x,t)=\big(0,\;v(x_1,t)\big),\qquad \theta(x,t)=\theta_0(x_1).$$

*Check incompressibility:* $\nabla\cdot u=\partial_2 v(x_1,t)=0$. ✓

*Transport of $\theta$:* $u\cdot\nabla\theta = 0\cdot\partial_1\theta + v\,\partial_2\theta = 0$ since $\theta$ has no $x_2$-dependence. So $\partial_t\theta=0$ and $\theta(t)=\theta_0(x_1)$ for all $t$. ✓

*Vorticity:* $\omega=\partial_1v_2-\partial_2v_1=\partial_1 v$, and $u\cdot\nabla\omega=v\,\partial_2\omega=0$. The vorticity equation collapses to
$$\partial_t\omega=\partial_1\theta_0 \quad\Longrightarrow\quad \omega(x_1,t)=\omega_0(x_1)+t\,\theta_0'(x_1),$$
hence $v(x_1,t)=v_0(x_1)+t\,\Theta(x_1)$ with $\Theta'=\theta_0'$, i.e. $v(x_1,t)=v_0(x_1)+t\,\theta_0(x_1)$.

*Take concretely* $\theta_0(x_1)=\sin x_1$, $v_0\equiv0$ on $\mathbb{T}\times\mathbb{T}$. Then
$$\theta(t)=\sin x_1,\qquad u(t)=(0,\;t\sin x_1),\qquad \omega(t)=t\cos x_1,\qquad \|\omega(t)\|_{L^\infty}=t .$$

**What it shows.** A horizontal buoyancy gradient manufactures vorticity at a *linear* rate — this is the entire source term, laid bare. But $\|\nabla\theta\|_{L^\infty}=1$ for all time, so the Chae–Nam criterion $\int_0^T\|\nabla\theta\|_{L^\infty}dt=T<\infty$ holds and the solution is global. The example is degenerate precisely because the advection $u\cdot\nabla\theta$ vanishes identically: the new vorticity never feeds back into the buoyancy gradient.

**The open problem is the feedback.** In the Hou–Luo/Chen–Hou scenario the generated $\omega$ drives a hyperbolic velocity field $u\approx(-\lambda(t)x_1,\lambda(t)x_2)$ near a stagnation point, and then
$$\frac{d}{dt}|\partial_1\theta| \approx \lambda(t)\,|\partial_1\theta|,\qquad \frac{d\lambda}{dt}\gtrsim \|\partial_1\theta\|_{L^\infty},$$
a closed system $\lambda'\gtrsim g$, $g'\approx\lambda g$ whose solutions blow up in finite time (e.g. $g\sim(T^*-t)^{-2}$, $\lambda\sim(T^*-t)^{-1}$). Producing that hyperbolic point *stably and without a wall* — the boundary supplies it for free in the solved cases — is exactly the gap in §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*