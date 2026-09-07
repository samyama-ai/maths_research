---
id: 06-pdes/proudman-johnson-singularities
title: "Proudman-Johnson Equation Singularities"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Proudman–Johnson Equation Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/proudman-johnson-singularities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The generalized Proudman–Johnson equation is the one-dimensional evolution problem

$$\partial_t u_{xx} + u\,u_{xxx} - a\,u_x u_{xx} = \nu\,u_{xxxx} + \lambda(t),$$

for $u(x,t)$ on either $\mathbb{T}=[0,2\pi)$ (periodic, $\lambda$ fixed by zero-mean normalization) or the interval $(-1,1)$ with no-slip data $u(\pm1)=u_x(\pm1)=0$ (then $\lambda(t)$ is a Lagrange multiplier coming from the pressure). Here $a\in\mathbb{R}$ is a fixed parameter and $\nu\ge 0$ the viscosity.

**Open problem.** Classify the pairs $(a,\nu)$ — and, within each, the initial data $u_0$ — for which the solution stays smooth for all $t>0$, versus those for which $\|u_x(\cdot,t)\|_{L^\infty}$ blows up in finite time. A complete answer must give, for each $a$ and each $\nu\ge0$, either (i) a global-in-time regularity theorem for all smooth data satisfying the boundary conditions, or (ii) an explicit class of smooth data with a finite blow-up time $T<\infty$ and a proof that $\limsup_{t\to T}\|u_x(t)\|_{L^\infty}=\infty$.

The equation is not a toy: $a=1$ is *exactly* two-dimensional Navier–Stokes restricted to stagnation-point (self-similar) velocity fields, so blow-up there would be a genuine Navier–Stokes singularity within that invariant class. The interest of general $a$ is that the family interpolates between equations with known, opposite behaviour, so the transition mechanism is isolated in a single scalar parameter.

## 2. Mathematical Foundations

**Derivation ($a=1$).** Take 2D incompressible Navier–Stokes with stream function $\psi(x,y,t)=x\,f(y,t)$, so $(u,v)=(\psi_y,-\psi_x)=(x f_y,\,-f)$ and vorticity $\omega=-\Delta\psi=-x f_{yy}$. Substituting into $\omega_t+u\omega_x+v\omega_y=\nu\Delta\omega$ and dividing by $-x$:

$$f_{yyt}+f_y f_{yy}-f f_{yyy}=\nu f_{yyyy}.$$

This is the Proudman–Johnson equation. Replacing the coefficient $1$ of $f_yf_{yy}$ by $-a$ (after renaming $f\mapsto u$, $y\mapsto x$) gives the generalized family. Special values:

| $a$ | reduction |
|---|---|
| $1$ | 2D Navier–Stokes, stagnation-point form (original PJ) |
| $2$ | axisymmetric self-similar flow (Okamoto–Zhu) |
| $-1$ | pure transport–diffusion of $u_x$ (no vortex stretching) |
| $-2$ | Hunter–Saxton equation $u_{txx}+uu_{xxx}+2u_xu_{xx}=0$ |
| $-3$ | twice-differentiated inviscid Burgers equation |

**Vorticity form.** Put $v=u_x$ (the "vorticity amplitude"). Since $\partial_x(v_t+uv_x)=v_{tx}+uv_{xx}+vv_x$, the equation integrates once in $x$ to

$$v_t+u\,v_x=\frac{a+1}{2}\Big(v^2-\fint v^2\,dx\Big)+\nu v_{xx},\qquad u_x=v,\quad \fint v\,dx=0,$$

on $\mathbb{T}$, where $\fint = \frac{1}{2\pi}\int_{\mathbb{T}}$. This is the canonical structure: **local Riccati amplification with a nonlocal mean-zero constraint**. Along characteristics $\dot X(\alpha,t)=u(X,t)$, $X(\alpha,0)=\alpha$, the inviscid equation is the scalar Riccati ODE

$$\dot v = \tfrac{a+1}{2}\big(v^2-I(t)\big),\qquad I(t)=\fint v^2\,dx,$$

coupled to all other characteristics only through $I(t)$. A short computation gives $\frac{d}{dt}\int_{\mathbb{T}} v^2 = (a+2)\int_{\mathbb{T}} v^3$, so $I$ is conserved exactly at $a=-2$.

**Sign of the stretching coefficient.** The factor $(a+1)/2$ controls everything. For $a>-1$, large positive $v$ self-amplifies ($v\to+\infty$); for $a<-1$, large negative $v$ self-amplifies ($v\to-\infty$); at $a=-1$ the Riccati term vanishes identically.

**Function-space setting.** Local well-posedness holds in $H^s(\mathbb{T})$, $s>3/2$ for $\nu=0$ and $s\ge 0$ for $\nu>0$, by standard energy/parabolic-smoothing arguments; the only issue is global continuation, controlled by a Beale–Kato–Majda-type criterion: the solution persists as long as $\int_0^T\|u_x(t)\|_{L^\infty}dt<\infty$.

## 3. History & State of the Art (SOTA)

- **1962.** Proudman and Johnson introduce the equation while studying boundary-layer growth near a rear stagnation point (*J. Fluid Mech.* **12**, 161–168), obtaining the similarity reduction and an inviscid outer solution with exponentially thinning structure.
- **1989.** Childress, Ierley, Spiegel and Young (*J. Fluid Mech.* **203**, 1–22) study stagnation-point-form solutions of 2D Euler and Navier–Stokes on unbounded domains and exhibit finite-time blow-up of $u_x$, showing the ansatz is not automatically globally regular.
- **2000.** Okamoto and Zhu (*Taiwanese J. Math.* **4**, 65–103) introduce the parameter $a$, catalogue the reductions above, and report numerical evidence for a blow-up/global-existence transition in $a$.
- **2000, 2002.** Chen and Okamoto prove global existence for the viscous problem, first for the original equation and then for the generalized one over a range of $a$ (*Proc. Japan Acad. Ser. A* **76**, 149–152; **78**, 136–139).
- **2008–2011.** Okamoto, Sakajo and Wunsch (*Nonlinearity* **21**, 2447–2461) place the family alongside the Constantin–Lax–Majda/De Gregorio family; Okamoto (2009) and Wunsch (2011) settle well-posedness questions for the inviscid periodic problem.
- **2013–2015.** Sarria and Saxton obtain an explicit representation formula for $u_x$ in the inviscid case and use it to give sharp, data-dependent blow-up and global-existence criteria organized by $a$ and by the local structure (sign and curvature) of $u_0'$ near its extrema.

## 4. Partial Results / Verified Cases

- **$a=-1$, any $\nu\ge0$, any domain:** global regularity. The Riccati term vanishes, $v_t+uv_x=\nu v_{xx}$, and the maximum principle gives $\|v(t)\|_{L^\infty}\le\|v_0\|_{L^\infty}$.
- **$a=-3$, $\nu=0$:** equivalent to inviscid Burgers for $v$ modulo the nonlocal term; gradient blow-up for essentially all nonconstant data. For $\nu>0$ the viscous Burgers structure gives global smoothness.
- **$a=-2$, $\nu=0$ (Hunter–Saxton):** $I(t)\equiv I_0$ is conserved and the dynamics decouple into scalar Riccati ODEs. If $\min_x u_0'(x)<-\sqrt{I_0}$ then $u_x\to-\infty$ in finite time; the blow-up time along the minimizing characteristic is explicit (Section 10). Global weak (dissipative/conservative) continuations exist past $T$.
- **$\nu>0$, no-slip on $(-1,1)$, $a$ in a neighbourhood of the physical value $a=1$:** global existence in time (Chen–Okamoto 2000, 2002) *(precise admissible $a$-range as reported — verify against the original statements)*.
- **Small data, $\nu>0$, any $a$:** if $\|u_0\|_{H^2}$ is small relative to $\nu$, the Riccati term is dominated by dissipation and solutions are global by standard perturbative energy estimates.
- **$a<-1$, $\nu=0$, periodic:** blow-up for open sets of data, by the sign argument on $\dot v=\frac{a+1}{2}(v^2-I)$ whenever a characteristic starts with $v_0$ sufficiently negative and $I(t)$ can be controlled from above.
- **Numerics:** Okamoto–Zhu and subsequent computations locate a transition in $a$ with self-similar blow-up profiles on one side and relaxation to steady states or time-periodic states on the other.

## 5. Principal Obstacles

- **The nonlocal term is not a perturbation.** Blow-up requires $v^2$ to beat $I(t)=\fint v^2$, but $I$ is itself driven by the same growth. Local Riccati comparison gives blow-up only if one first knows $I(t)$ stays small — exactly the quantity that grows. This feedback is what defeats naive ODE comparison for $a\ne -2$ (where $I$ is conserved) and $a\ne-1$ (where the term is absent).
- **Characteristics compress.** The spatial measure near the peak of $v$ contracts, so $L^p$-based quantities can stay bounded while $L^\infty$ diverges; energy methods in $H^s$ see only integrated quantities and miss the concentration.
- **Viscosity is critical against the stretching.** The equation is invariant under $u\mapsto \mu u(\mu x,\mu^2 t)$ only for $\nu$ scaled along; the $L^\infty$ norm of $v$ is scaling-critical for the parabolic problem, so $\nu v_{xx}$ and $\frac{a+1}{2}v^2$ balance at every scale. There is no gap for a smallness argument to exploit near a would-be singularity.
- **Fourier/dispersive tools are unavailable.** The equation has no dispersion and no conserved coercive energy for general $a$ (only $a=-2$ has $\int v^2$ conserved), so the standard toolkit — Strichartz, conservation-law-driven a priori bounds, monotonicity formulae — has nothing to act on.
- **Boundary vs. periodic geometry differ.** No-slip walls supply a stabilizing mechanism absent on $\mathbb{T}$; results proved with $\lambda(t)$ as a boundary multiplier do not transfer to the periodic normalization, and vice versa.

## 6. The Gap

Proven behaviour is confined to the exactly solvable coefficients ($a=-3,-2,-1$), to small data, and to $a$-windows for which a monotone quantity or maximum principle happens to close. The general statement of Section 1 asks for the entire $(a,\nu)$ plane. The exact step to be crossed is a two-sided control of the nonlocal quantity $I(t)$ in terms of the local peak $\|v(t)\|_{L^\infty}$: a lower bound of the form $I(t)\le (1-\epsilon)\|v(t)\|_{L^\infty}^2$ propagated in time would convert the Riccati ODE into a genuine blow-up proof; an upper bound of the reverse type would give global regularity. No mechanism currently produces either bound for $a\notin\{-3,-2,-1\}$, because both require quantitative control on how the characteristic map concentrates mass near the extremum of $v_0$ — precisely the information that Sarria–Saxton's representation formula supplies for $\nu=0$ but that no known formula supplies once $\nu>0$.

## 7. Current Research (as of June 2026)

- **Transfer from the De Gregorio/CLM family.** The same $L^\infty$-critical Riccati-plus-nonlocal structure was cracked for the 1D models of 3D Euler: Elgindi and Jeong on the effect of advection versus stretching, and Chen–Hou–Huang's computer-assisted stability analysis of self-similar profiles. Groups in Princeton/NYU, Caltech and Duke are adapting the modulation + computer-assisted spectral-gap method to the Proudman–Johnson family *(frontier — verify)*.
- **Computer-assisted proofs of self-similar profiles.** Rigorous interval-arithmetic enclosures of a stationary profile of the renormalized equation, plus a spectral-gap certificate, would settle blow-up for individual $a$ values. This is the most likely near-term route to a first unconditional blow-up theorem at $a>0$ with $\nu>0$ *(frontier — verify)*.
- **Japanese school (Kyoto/Gakushuin).** Continued numerical bifurcation analysis of steady and time-periodic states of the viscous problem as $a$ varies, mapping the boundary of the global-existence region.
- **Weak/continuation theory.** Extension of the Hunter–Saxton conservative/dissipative weak-solution framework to other $a$, to make "what happens after $T$" a well-posed question.

## 8. Future Work

1. Prove or disprove finite-time blow-up for the viscous equation at a single value $a>1$; this is the cleanest decisive target and Okamoto has repeatedly flagged large $a$ as the place blow-up should first appear.
2. Extend the Sarria–Saxton explicit representation to $\nu>0$ by a Duhamel/characteristic hybrid, even in a small-viscosity asymptotic regime.
3. Determine the sharp critical $a^\ast(\nu)$ separating global existence from blow-up, and establish whether the transition is continuous in $\nu$ as $\nu\downarrow0$.
4. Construct a Lyapunov functional monotone along the flow for $a$ in the unresolved band — the analogue of the $\int v^2$ conservation that trivializes $a=-2$.
5. Settle whether no-slip boundaries can *cause* rather than prevent blow-up, in parallel with the Chen–Hou boundary-driven 3D Euler scenario.

## 9. Key References

- **[Foundational]** I. Proudman, K. Johnson. *Boundary-layer growth near a rear stagnation point.* Journal of Fluid Mechanics **12** (1962), 161–168.
- **[Foundational]** S. Childress, G. R. Ierley, E. A. Spiegel, W. R. Young. *Blow-up of unsteady two-dimensional Euler and Navier–Stokes solutions having stagnation-point form.* Journal of Fluid Mechanics **203** (1989), 1–22.
- **[Foundational]** H. Okamoto, J. Zhu. *Some similarity solutions of the Navier–Stokes equations and related topics.* Taiwanese Journal of Mathematics **4** (2000), 65–103.
- **[SOTA]** X. Chen, H. Okamoto. *Global existence of solutions to the Proudman–Johnson equation.* Proceedings of the Japan Academy, Series A **76** (2000), 149–152.
- **[SOTA]** X. Chen, H. Okamoto. *Global existence of solutions to the generalized Proudman–Johnson equation.* Proceedings of the Japan Academy, Series A **78** (2002), 136–139.
- **[Survey]** H. Okamoto, T. Sakajo, M. Wunsch. *On a generalization of the Constantin–Lax–Majda equation.* Nonlinearity **21** (2008), 2447–2461.
- **[SOTA]** H. Okamoto. *Well-posedness of the generalized Proudman–Johnson equation without viscosity.* Journal of Mathematical Fluid Mechanics **11** (2009), 46–59.
- **[SOTA]** A. Constantin, M. Wunsch. *On the inviscid Proudman–Johnson equation.* Proceedings of the Japan Academy, Series A **85** (2009), 81–83.
- **[SOTA]** M. Wunsch. *The generalized Proudman–Johnson equation revisited.* Journal of Mathematical Fluid Mechanics **13** (2011), 147–154.
- **[SOTA / Recent]** A. Sarria, R. Saxton. *Blow-up of solutions to the generalized inviscid Proudman–Johnson equation.* Journal of Mathematical Fluid Mechanics **15** (2013), 493–523.
- **[SOTA / Recent]** A. Sarria, R. Saxton. *The role of initial curvature in solutions to the generalized inviscid Proudman–Johnson equation.* Quarterly of Applied Mathematics **73** (2015), 55–91.
- **[Related]** J. K. Hunter, R. Saxton. *Dynamics of director fields.* SIAM Journal on Applied Mathematics **51** (1991), 1498–1521.
- **[Related]** T. Y. Hou, J. Chen, D. Huang. *Asymptotically self-similar blowup of the Hou–Luo model for the 3D Euler equations.* Annals of PDE / arXiv preprint series, 2021–2022.

## 10. Worked Example / Concrete Special Case

**Case $a=-2$, $\nu=0$, $\mathbb{T}=[0,2\pi)$, $u_0(x)=-\cos x$.**

Then $v_0=u_0'=\sin x$ and $\fint v_0\,dx=0$, as required. Since $\frac{d}{dt}\int v^2=(a+2)\int v^3=0$ at $a=-2$, the nonlocal quantity is a constant:

$$I(t)\equiv I_0=\fint_{\mathbb T}\sin^2x\,dx=\tfrac12,\qquad k:=\sqrt{I_0}=\tfrac{1}{\sqrt2}\approx0.7071.$$

Along a characteristic the equation of Section 2 becomes the autonomous Riccati ODE

$$\dot v=\tfrac{a+1}{2}(v^2-k^2)=-\tfrac12\big(v^2-k^2\big).$$

Separating variables, $\int \frac{dv}{v^2-k^2}=\frac{1}{2k}\ln\left|\frac{v-k}{v+k}\right|$, so

$$t=\frac{1}{k}\left[\ln\left|\frac{v_0-k}{v_0+k}\right|-\ln\left|\frac{v-k}{v+k}\right|\right].$$

Take the characteristic starting at $\alpha=3\pi/2$, where $v_0=\min_x\sin x=-1$. Because $-1<-k$, both $v-k$ and $v+k$ stay negative and $\dot v=-\frac12(v^2-k^2)<0$: the value decreases monotonically and escapes to $-\infty$. Letting $v\to-\infty$ makes the second logarithm vanish, so

$$T=\frac1k\ln\frac{v_0-k}{v_0+k}=\sqrt2\,\ln\frac{-1-\frac{1}{\sqrt2}}{-1+\frac{1}{\sqrt2}}=\sqrt2\,\ln\big(3+2\sqrt2\big)=2\sqrt2\,\ln(1+\sqrt2)\approx 2.4929.$$

At $t=T$ one has $u_x\to-\infty$ at a single point while $u$ itself remains bounded (indeed $\|u\|_{L^\infty}$ is controlled by $\int|v|\le\sqrt{2\pi I_0}$): a **cusp / gradient singularity**, not a blow-up of the velocity.

**Contrast at $a=-1$ with the same data.** The Riccati coefficient $(a+1)/2$ is zero, so $\dot v=0$ along characteristics and $\|u_x(t)\|_{L^\infty}\equiv1$ for all time — global smooth existence.

The two computations use identical initial data and differ only in the single coefficient $a$. They show that the question of Section 1 is genuinely a question about the balance between the local Riccati amplification $\frac{a+1}{2}v^2$ and the nonlocal subtraction $\frac{a+1}{2}I(t)$ — and that for every $a$ other than $-2$, where $I$ happens to be conserved, that balance is not yet under control.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*