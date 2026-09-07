---
id: 06-pdes/kuramoto-sivashinsky-2d-regularity
title: "Kuramoto-Sivashinsky 2D Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kuramoto–Sivashinsky 2D Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kuramoto-sivashinsky-2d-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the Kuramoto–Sivashinsky (KS) equation on the two-dimensional torus $\mathbb{T}^2_{L} = [0,L_1]\times[0,L_2]$, in scalar ("growth") form

$$\partial_t \phi + \Delta \phi + \Delta^2 \phi + \tfrac12 |\nabla \phi|^2 = 0, \qquad \phi(\cdot,0)=\phi_0,$$

or equivalently, for $u=\nabla\phi$, in gradient ("derivative") form

$$\partial_t u + \Delta u + \Delta^2 u + (u\cdot\nabla) u = 0, \qquad \nabla\times u = 0 .$$

**Open problem.** Do smooth periodic initial data on a fixed 2D torus generate solutions that remain smooth for all $t>0$? Equivalently: is there an a priori bound on $\|u(t)\|_{L^2(\mathbb{T}^2_L)}$ (or any subcritical norm) depending only on the data and on $L_1,L_2$, valid on the whole maximal interval of existence?

A complete resolution is either (i) a proof that for every $L_1,L_2>0$ and every $\phi_0\in C^\infty(\mathbb{T}^2_L)$ the local solution extends globally and stays $C^\infty$, together with a bound on the global attractor; or (ii) an explicit construction (possibly computer-assisted) of data whose solution has $\limsup_{t\to T^-}\|\nabla\phi(t)\|_{L^\infty}=\infty$ for some finite $T$.

## 2. Mathematical Foundations

**Linear part.** In Fourier variables $\phi(x,t)=\sum_{k\in\Lambda^*}\hat\phi_k(t)e^{ik\cdot x}$ with $\Lambda^*=2\pi(\mathbb{Z}/L_1\times\mathbb{Z}/L_2)$, the linear operator $-(\Delta+\Delta^2)$ has symbol

$$\sigma(k) = |k|^2 - |k|^4 .$$

Modes with $0<|k|<1$ grow; modes with $|k|>1$ are damped at rate $\sim|k|^4$. The number of linearly unstable modes is $\\#\{k\in\Lambda^*: 0<|k|<1\} \sim L_1L_2/(4\pi)$, so large boxes are strongly unstable and the dynamics is spatiotemporally chaotic.

**Mean and gauge.** Integrating the scalar form, $\frac{d}{dt}\int\phi = -\frac12\int|\nabla\phi|^2 \le 0$: the mean is not conserved but decreases monotonically, and the equation is invariant under $\phi\mapsto\phi+c(t)$ modulo a forcing term. The gradient form is therefore the natural object; $u$ has zero mean and is curl-free.

**Scaling.** Dropping the lower-order $\Delta u$, the equation $\partial_tu+\Delta^2u+(u\cdot\nabla)u=0$ is invariant under $u_\lambda(x,t)=\lambda^{3}u(\lambda x,\lambda^{4}t)$, so the critical Sobolev index in dimension $d$ is $s_c=\frac{d}{2}-3$, i.e. $s_c=-2$ in 2D. **$L^2$ is thus strongly subcritical**, and local well-posedness in $L^2$ (indeed in $H^{-2+\varepsilon}$ and in Wiener/analytic classes) is standard by Duhamel plus the smoothing $\|e^{-t\Delta^2}f\|_{H^s}\lesssim t^{-(s-r)/4}\|f\|_{H^r}$.

**Energy identity.** For mean-zero $u=\nabla\phi$,

$$\frac12\frac{d}{dt}\|u\|_{L^2}^2 = \|\nabla u\|_{L^2}^2 - \|\Delta u\|_{L^2}^2 + \frac12\int_{\mathbb{T}^2}(\nabla\!\cdot\! u)\,|u|^2\,dx .$$

In $d=1$ the last term is $\frac12\int u_x u^2 = \frac16\int(u^3)_x=0$; the nonlinearity is energy-neutral and global regularity follows. In $d=2$, $\nabla\!\cdot\!u=\Delta\phi\not\equiv0$, and the cubic term does **not** vanish. This single algebraic fact is the whole difficulty.

**Dissipative dynamical system.** When global existence holds, the semigroup $S(t)$ is compact and possesses a finite-dimensional global attractor $\mathcal{A}\subset H^s$, with dimension polynomial in $L_1L_2$ (Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 1997).

## 3. History & State of the Art (SOTA)

- **1976–1977.** Kuramoto and Tsuzuki derive the equation for phase turbulence in reaction–diffusion systems; Sivashinsky derives it independently for the diffusive–thermal instability of laminar flames. The 2D form is the physically native one (flame fronts, thin liquid films are surfaces).
- **1985.** Nicolaenko, Scheurer and Temam prove global existence and an absorbing ball for the 1D equation with odd data, using the background-flow test function $u-\Phi$.
- **1993–2009.** Sharpening of the 1D bound on $\limsup_t L^{-1/2}\|u\|_{L^2}$: $O(L^{3/5})$ (Collet–Eckmann–Epstein–Stubbe 1993, also Goodman 1994), then $O(L)$ via Lyapunov/Gagliardo–Nirenberg arguments (Bronski–Gambill 2006), then $o(L)$ (Giacomelli–Otto 2005), and finally $O(\log^{5/3}L)$ (Otto 2009). The conjectured truth is $O(1)$.
- **1992–2000.** Sell–Taboada and Molinet obtain global existence, local dissipativity and attractor bounds for 2D KS on **thin** domains $(0,L_1)\times(0,\varepsilon)$.
- **2014–2020.** Anisotropically reduced 2D models (nonlinearity $\frac12(\partial_x\phi)^2$ instead of $\frac12|\nabla\phi|^2$) are shown globally well-posed (Benachour–Kukavica–Rusin–Ziane; Larios–Yamazaki).
- **2019–2022.** Ambrose–Mazzucato prove global existence and analyticity for classes of 2D data with few growing modes; Coti Zelati–Dolce–Feng–Mazzucato and Feng–Mazzucato prove global existence for 2D KS with a strong advecting shear or mixing flow.
- **Numerics.** Large-scale simulations (Kalogirou–Keaveny–Papageorgiou 2015; Tomlin–Kalogirou–Papageorgiou 2018) find no evidence of blow-up on any box tested, and support energy growth roughly proportional to the box area — i.e. $O(1)$ energy per unit area.

**Status: open in full generality; empirically supported for global regularity.**

## 4. Partial Results / Verified Cases

- **Dimension 1, all $L$, all data.** Global existence, analyticity, finite-dimensional attractor. Best a priori bound on the time-averaged normalized $L^2$ norm: $O(\log^{5/3} L)$ (Otto 2009).
- **2D, small data.** If $\|u_0\|_{L^2(\mathbb{T}^2_L)}$ is below an explicit threshold depending only on the Ladyzhenskaya constant and the smallest wavenumber, the solution is global (see Section 10).
- **2D thin domains.** $\Omega=(0,L_1)\times(0,\varepsilon)$ with $\varepsilon$ small enough relative to $L_1$: global existence and a global attractor (Sell–Taboada 1992; Molinet 2000). Here at most finitely many modes vary in $y$, and the problem is a perturbation of the 1D case.
- **2D with few growing modes.** Ambrose–Mazzucato (2019) prove global existence and analyticity on $[0,2\pi\lambda_1]\times[0,2\pi\lambda_2]$ when the growing-mode set is restricted (essentially $\lambda_2\le1$), in analytic Wiener spaces; their 2021 paper extends this to **one linearly growing mode in each direction** with a smallness condition on the data's growing-mode content.
- **2D anisotropic reduction.** For $\partial_t\phi+\Delta^2\phi+\partial_{xx}\phi+\frac12(\partial_x\phi)^2=0$ on $\mathbb{T}^2$: global well-posedness for arbitrary data (Benachour–Kukavica–Rusin–Ziane 2014; Larios–Yamazaki 2020).
- **2D with advection.** $\partial_t\phi + A\,v\cdot\nabla\phi + \Delta\phi+\Delta^2\phi+\frac12|\nabla\phi|^2=0$ with $v$ a shear or a mixing/relaxation-enhancing flow: global existence for $A$ sufficiently large (Coti Zelati–Dolce–Feng–Mazzucato 2021; Feng–Mazzucato 2022). Enhanced dissipation beats the nonlinearity.
- **Radial/one-mode truncations.** Finite Galerkin truncations of any fixed dimension are globally well-posed (the quadratic nonlinearity is locally Lipschitz and the linear part dominates at high $|k|$).

## 5. Principal Obstacles

- **No coercive conserved quantity.** Unlike 2D Navier–Stokes (enstrophy) or nonlinear Schrödinger (mass/energy), KS has neither a conservation law nor a Lyapunov functional. The only structural input is the sign of the biharmonic dissipation, and it must fight both the antidiffusion $-\Delta$ and the nonlinearity.
- **The cubic term does not cancel.** $\int(\nabla\!\cdot\!u)|u|^2$ vanishes identically in 1D and for divergence-free fields; here $u$ is curl-free, exactly the opposite structure. All 1D proofs (background flow $\Phi$, Nicolaenko–Scheurer–Temam) are built on that cancellation and have no 2D analogue.
- **Borderline Ladyzhenskaya estimate.** The best generic bound is $|\int(\nabla\!\cdot\!u)|u|^2|\le C\|u\|_{L^2}\|\Delta u\|_{L^2}^{2}$ — the same power of the dissipation, not less. So the nonlinearity is *exactly* critical against the dissipation at the level of $L^2$ energy, and can be absorbed only under a smallness assumption. There is no room for a Grönwall argument.
- **Subcriticality is useless without a global bound.** Because $s_c=-2$, local theory is easy in every reasonable space; the failure is purely global. Improving local well-posedness (Besov, Wiener algebras, critical spaces) does not touch the problem.
- **Large-box instability.** Any proof must accommodate $\sim L_1L_2/4\pi$ unstable modes, so perturbative and continuation-from-small-domain arguments degenerate as $L\to\infty$.
- **No self-similar candidate.** The two-term linear operator breaks scaling invariance, so the standard route to constructing blow-up — a self-similar or approximately self-similar profile with a stable spectral picture — has no obvious starting ansatz. Blow-up, if it exists, would be at scale $\ll 1$ where $\Delta^2$ dominates $\Delta$, i.e. governed by $\partial_tu+\Delta^2u+(u\cdot\nabla)u=0$; but that equation itself has no known blow-up in 2D.

## 6. The Gap

Proven: global regularity when the nonlinearity can be dominated — small data, thin domains, few growing modes, strong advection, or an anisotropic reduction that restores a 1D-type cancellation. Unproven: everything else. The precise missing step is

$$\sup_{t<T^*}\|u(t)\|_{L^2(\mathbb{T}^2_L)} \le F\big(L_1,L_2,\|u_0\|_{L^2}\big) < \infty$$

for arbitrary $L_1,L_2$ and arbitrary data, with **no** smallness. Equivalently: control $\int_0^T\!\!\int(\nabla\!\cdot\!u)|u|^2$ by the dissipation $\int_0^T\|\Delta u\|^2$ with a constant that does not require $\|u\|_{L^2}$ small — i.e. exploit the curl-free constraint $u=\nabla\phi$, which is currently used only to define the problem and never as an estimate. Whether that constraint is a help (it forbids the vortical mechanisms that drive 3D Euler-type growth) or irrelevant is itself open.

## 7. Current Research (as of June 2026)

- **Enhanced-dissipation program** (Coti Zelati, Dolce, Feng, Mazzucato and collaborators; Penn State, Maryland, Imperial): quantify how much mixing/advection is needed for global existence, and whether the threshold amplitude $A$ can be pushed to zero along some family. Currently the most active analytic line.
- **Analytic-space methods** (Ambrose, Mazzucato; Drexel/Penn State): Wiener-algebra and Gevrey estimates tracking the growing-mode budget mode by mode, aiming to increase the number of admissible growing modes from $O(1)$ toward $O(L^2)$.
- **Anisotropic and hierarchical reductions** (Kukavica, Larios, Yamazaki, Massatt): interpolate between the solvable reduced nonlinearity $\frac12\phi_x^2$ and the full $\frac12|\nabla\phi|^2$ by a parameter $\theta$, and locate the $\theta$ at which the method breaks. *(frontier — verify)*
- **Computer-assisted analysis**: rigorous-numerics validation of 2D KS trajectories and attractor structure (CAPD/Zgliczyński-school techniques, and Chen–Hou-style neural-network-assisted searches for approximate self-similar profiles transplanted to KS). No blow-up candidate has been produced. *(frontier — verify)*
- **Statistical/turbulence bounds**: background-flow and auxiliary-function (SOS/convex-optimization) methods to bound time-averaged energy in 2D, following the 1D program of Goluskin and collaborators. *(frontier — verify)*

## 8. Future Work

1. **Use the gradient structure.** Find an estimate that distinguishes curl-free $u$ from general vector fields — e.g. exploiting that $\nabla\!\cdot\!u=\Delta\phi$ is a full Laplacian of the potential, giving $\int \Delta\phi|\nabla\phi|^2 = -\int \nabla\phi\cdot\nabla|\nabla\phi|^2$ and thus a possible integration-by-parts gain.
2. **Transplant Otto's 1D method.** The $\log^{5/3}$ bound rests on a clever choice of test function and a maximum-principle-flavoured argument for the 1D Burgers structure. A 2D analogue would need a substitute for the missing entropy.
3. **Bound the attractor, not the solution.** Prove that any suitably weak (Leray-type) 2D KS solution is eventually bounded, then upgrade regularity — the analogue of weak–strong uniqueness programs.
4. **Decide the blow-up side.** Study $\partial_tu+\Delta^2u+(u\cdot\nabla)u=0$ (scale-invariant, curl-free) as a stand-alone problem; a blow-up there would strongly suggest KS blow-up on large boxes.
5. **Sharpen numerics.** Adaptive-mesh 2D runs at $L\gtrsim 200$ with rigorous a posteriori error control, testing whether $\|u\|_{L^2}^2/(L_1L_2)$ stays $O(1)$.

## 9. Key References

- **[Foundational]** Y. Kuramoto, T. Tsuzuki. *Persistent propagation of concentration waves in dissipative media far from thermal equilibrium.* Progress of Theoretical Physics **55** (1976), 356–369.
- **[Foundational]** G. I. Sivashinsky. *Nonlinear analysis of hydrodynamic instability in laminar flames — I. Derivation of basic equations.* Acta Astronautica **4** (1977), 1177–1206.
- **[Foundational]** B. Nicolaenko, B. Scheurer, R. Temam. *Some global dynamical properties of the Kuramoto–Sivashinsky equations: nonlinear stability and attractors.* Physica D **16** (1985), 155–183.
- **[Foundational / 1D SOTA]** F. Otto. *Optimal bounds on the Kuramoto–Sivashinsky equation.* Journal of Functional Analysis **257** (2009), 2188–2245.
- **[1D bounds]** J. C. Bronski, T. N. Gambill. *Uncertainty estimates and $L^2$ bounds for the Kuramoto–Sivashinsky equation.* Nonlinearity **19** (2006), 2023–2039.
- **[1D bounds]** P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe. *A global attracting set for the Kuramoto–Sivashinsky equation.* Communications in Mathematical Physics **152** (1993), 203–214.
- **[2D thin domains]** G. R. Sell, M. Taboada. *Local dissipativity and attractors for the Kuramoto–Sivashinsky equation in thin 2D domains.* Nonlinear Analysis: TMA **18** (1992), 671–687.
- **[2D]** L. Molinet. *Local dissipativity in $L^2$ for the Kuramoto–Sivashinsky equation in spatial dimension 2.* Journal of Dynamics and Differential Equations **12** (2000), 533–556.
- **[2D anisotropic]** S. Benachour, I. Kukavica, W. Rusin, M. Ziane. *Anisotropic estimates for the two-dimensional Kuramoto–Sivashinsky equation.* Journal of Dynamics and Differential Equations **26** (2014), 461–476.
- **[SOTA / Recent]** D. M. Ambrose, A. L. Mazzucato. *Global existence and analyticity for the 2D Kuramoto–Sivashinsky equation.* Journal of Dynamics and Differential Equations **31** (2019), 1525–1547.
- **[SOTA / Recent]** D. M. Ambrose, A. L. Mazzucato. *Global solutions of the two-dimensional Kuramoto–Sivashinsky equation with a linearly growing mode in each direction.* Journal of Nonlinear Science **31** (2021), article 96.
- **[SOTA / Recent]** M. Coti Zelati, M. Dolce, Y. Feng, A. L. Mazzucato. *Global existence for the two-dimensional Kuramoto–Sivashinsky equation with a shear flow.* Journal of Evolution Equations **21** (2021), 5079–5099.
- **[SOTA / Recent]** Y. Feng, A. L. Mazzucato. *Global existence for the two-dimensional Kuramoto–Sivashinsky equation with advection.* Communications in Partial Differential Equations **47** (2022), 279–306.
- **[SOTA / Recent]** A. Larios, K. Yamazaki. *On the well-posedness of an anisotropically-reduced two-dimensional Kuramoto–Sivashinsky equation.* Physica D **411** (2020), 132560.
- **[Computational]** A. Kalogirou, E. E. Keaveny, D. T. Papageorgiou. *An in-depth numerical study of the two-dimensional Kuramoto–Sivashinsky equation.* Proceedings of the Royal Society A **471** (2015), 20140932.
- **[Survey]** R. Temam. *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed. Springer Applied Mathematical Sciences 68, 1997.

## 10. Worked Example / Concrete Special Case

**Claim (small-data global existence, with explicit threshold).** Let $u=\nabla\phi$ solve 2D KS on $\mathbb{T}^2_L$, mean zero, and let $\kappa=2\pi/\max(L_1,L_2)$ be the smallest nonzero wavenumber. Then there is $\varepsilon_0=\varepsilon_0(\kappa)>0$ such that $\|u_0\|_{L^2}<\varepsilon_0$ implies global regularity.

*Step 1 — energy identity.* Multiply by $u$ and integrate:

$$\frac12\frac{d}{dt}\|u\|_{2}^2 = \|\nabla u\|_2^2 - \|\Delta u\|_2^2 + \tfrac12\int (\nabla\!\cdot\!u)|u|^2 .$$

*Step 2 — the bad term.* By Cauchy–Schwarz and Ladyzhenskaya's inequality $\|f\|_{L^4}^2\le C_L\|f\|_{L^2}\|\nabla f\|_{L^2}$ (valid on $\mathbb{T}^2$ for mean-zero $f$, $C_L\le\sqrt2$ on $\mathbb{R}^2$):

$$\tfrac12\Big|\int(\nabla\!\cdot\!u)|u|^2\Big| \le \tfrac12\|\nabla\!\cdot\!u\|_{2}\,\|u\|_{L^4}^2 \le \tfrac{C_L}{2}\,\|\nabla u\|_2\,\|u\|_2\,\|\nabla u\|_2 = \tfrac{C_L}{2}\|u\|_2\|\nabla u\|_2^2 .$$

By interpolation $\|\nabla u\|_2^2 \le \|u\|_2\|\Delta u\|_2 \le \frac{1}{2\delta}\|u\|_2^2+\frac{\delta}{2}\|\Delta u\|_2^2$.

*Step 3 — absorb.* With $E=\|u\|_2^2$ and $D=\|\Delta u\|_2^2$, and using $\|\nabla u\|_2^2\le \frac{1}{2\delta}E+\frac{\delta}{2}D$ in both the linear antidiffusion term and Step 2,

$$\frac12\dot E \;\le\; \Big(1+\tfrac{C_L}{2}E^{1/2}\Big)\Big(\tfrac{1}{2\delta}E+\tfrac{\delta}{2}D\Big) - D .$$

Choose $\delta$ so that $\big(1+\frac{C_L}{2}E^{1/2}\big)\frac{\delta}{2}\le \frac12$, i.e. $\delta = \big(1+\frac{C_L}{2}E^{1/2}\big)^{-1}$. Then

$$\frac12\dot E \le \tfrac12\big(1+\tfrac{C_L}{2}E^{1/2}\big)^{2}E - \tfrac12 D \le \tfrac12\big(1+\tfrac{C_L}{2}E^{1/2}\big)^{2}E - \tfrac12\kappa^{4}E,$$

using the Poincaré-type bound $D=\|\Delta u\|_2^2\ge\kappa^4 E$. Hence $\dot E<0$ whenever

$$\big(1+\tfrac{C_L}{2}E^{1/2}\big)^{2} < \kappa^{4}, \qquad\text{i.e.}\qquad E < \varepsilon_0^2 := \Big(\tfrac{2(\kappa^{2}-1)}{C_L}\Big)^{2}, \quad \kappa>1 .$$

So on a **small** torus ($\kappa>1$: no linearly unstable mode at all) with $\|u_0\|_2<\varepsilon_0$, the energy decays monotonically to zero and the solution is global and analytic.

*Step 4 — where it breaks.* For a large torus $\kappa\ll1$: the right-hand side is positive even at $E=0$ (the flat state is linearly unstable), $\varepsilon_0$ is vacuous, and the nonlinear term $\frac{C_L}{2}E^{1/2}D$ scales with **the same power of $D$** as the dissipation $-D$. Absorption therefore requires $E^{1/2}\lesssim 1/C_L$ — a smallness condition that no a priori estimate supplies, and which numerics say is violated (observed $E \sim c\,L_1L_2$, growing without bound with the box). That is exactly the open gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*