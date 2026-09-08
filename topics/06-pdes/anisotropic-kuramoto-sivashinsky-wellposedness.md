---
id: 06-pdes/anisotropic-kuramoto-sivashinsky-wellposedness
title: "Global Well-posedness of the Two-Dimensional Kuramoto–Sivashinsky Equation with Anisotropic Viscosity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Well-posedness of the Two-Dimensional Kuramoto–Sivashinsky Equation with Anisotropic Viscosity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/anisotropic-kuramoto-sivashinsky-wellposedness` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbb{T}^2_L = [0,L_1]\times[0,L_2]$ with periodic boundary conditions, and let $\nu_1,\nu_2 > 0$, $\lambda_1,\lambda_2 \ge 0$. Consider the anisotropic two-dimensional Kuramoto–Sivashinsky (KS) equation in scalar ("integrated", flame-front) form:

$$\partial_t u + \nu_1\,\partial_x^4 u + \nu_2\,\partial_y^4 u + \lambda_1\,\partial_x^2 u + \lambda_2\,\partial_y^2 u + \tfrac12|\nabla u|^2 = 0, \qquad u(\cdot,0) = u_0 .$$

**Conjecture (GWP).** For every $\nu_1,\nu_2>0$, every $\lambda_1,\lambda_2\ge 0$, every $L_1,L_2>0$ and every $u_0 \in H^2(\mathbb{T}^2_L)$, there is a unique global solution $u \in C([0,\infty);H^2)\cap L^2_{loc}([0,\infty);H^4)$, which is real-analytic for $t>0$ and whose $H^s$ norms remain bounded uniformly in $t$ (so the semigroup has a bounded absorbing set and a compact global attractor).

A complete resolution requires either (a) a proof of the above, or (b) an explicit initial datum and parameter set for which the maximal existence time $T^\ast$ is finite, with $\limsup_{t\to T^\ast}\|u(t)\|_{H^2} = \infty$. The problem is open even in the isotropic case $\nu_1=\nu_2=\lambda_1=\lambda_2=1$; the anisotropic family is the natural setting because the known global results all exploit a directional imbalance, and because the degenerate limit $\nu_2\downarrow 0$ isolates the mechanism that blocks the general proof.

## 2. Mathematical Foundations

**Linear part.** The Fourier symbol on $\mathbb{T}^2_L$, $k = 2\pi(m/L_1, n/L_2)$, is

$$\sigma(k) = \lambda_1 k_1^2 + \lambda_2 k_2^2 - \nu_1 k_1^4 - \nu_2 k_2^4 .$$

Modes with $\sigma(k)>0$ grow; the unstable set is the bounded region $\{\nu_1k_1^4 + \nu_2 k_2^4 < \lambda_1 k_1^2+\lambda_2 k_2^2\}$, an "astroid-like" lens whose area scales like $(\lambda_1/\nu_1)^{1/2}(\lambda_2/\nu_2)^{1/2}$ up to a constant, so the number of linearly unstable modes is $\asymp L_1L_2(\lambda_1\lambda_2)^{1/2}(\nu_1\nu_2)^{-1/2}$. Because $\nu_1\xi^4+\nu_2\eta^4 \ge \tfrac12\min(\nu_1,\nu_2)(\xi^2+\eta^2)^2$, the fourth-order operator is coercive and comparable to $\Delta^2$ as long as $\min(\nu_i)>0$: anisotropy of *strength* does not change the scaling class, only constants. Genuine degeneracy occurs only at $\nu_2=0$.

**Reduction.** Setting $u(x,y,t)=c\,v(\alpha x,\beta y,\gamma t)$ with $\gamma = \nu_1\alpha^4=\nu_2\beta^4$, i.e. $\beta = (\nu_1/\nu_2)^{1/4}\alpha$, and $c = 2\gamma/\alpha^2$, the system becomes

$$\partial_t v + \Delta^2 v + \tilde\lambda_1 \partial_X^2 v + \tilde\lambda_2\partial_Y^2 v + (\partial_X v)^2 + \rho\,(\partial_Y v)^2 = 0, \qquad \rho = (\nu_1/\nu_2)^{1/2},$$

on a torus of aspect ratio rescaled by $\rho^{1/2}$. So anisotropic viscosity is equivalent to an *isotropic* bilaplacian with an *anisotropic nonlinearity* on a stretched torus. The limits $\rho\to 0$ and $\rho\to\infty$ are the anisotropically reduced equations $\partial_t v + \Delta^2 v + \Delta v + (\partial_X v)^2 = 0$ studied by Larios–Yamazaki.

**Gradient form.** With $\mathbf{v}=\nabla u$ (curl-free), the equation becomes a Burgers-type system

$$\partial_t \mathbf v + \mathcal{L}\mathbf v + (\mathbf v\cdot\nabla)\mathbf v = 0, \qquad \mathcal L = \nu_1\partial_x^4+\nu_2\partial_y^4+\lambda_1\partial_x^2+\lambda_2\partial_y^2 .$$

**Structural facts.** (i) $u\mapsto u+a$ is a symmetry; (ii) the mean is monotone, $\frac{d}{dt}\bar u = -\frac{1}{2|\mathbb{T}^2_L|}\int|\nabla u|^2 \le 0$, so no $L^2$-type conservation is available; (iii) local well-posedness in $H^s$, $s>0$, follows from semigroup theory (the nonlinearity is quadratic in $\nabla u$ and the linear semigroup $e^{-t\mathcal L}$ is analytic), together with Gevrey-class analyticity by the Foias–Temam method.

**Working tool.** Global control is typically sought via anisotropic interpolation, e.g. on $\mathbb{T}^2$ for mean-zero $f$,

$$\|f\|_{L^\infty} \lesssim \|f\|_{L^2}^{1/4}\|\partial_x f\|_{L^2}^{1/4}\|\partial_y f\|_{L^2}^{1/4}\|\partial_x\partial_y f\|_{L^2}^{1/4},$$

which distributes derivative cost unevenly between directions — the reason the anisotropic formulation is the technically favourable one.

## 3. History & State of the Art (SOTA)

The equation arises from Kuramoto and Tsuzuki's phase-turbulence analysis of reaction–diffusion systems (1976) and Sivashinsky's derivation of flame-front dynamics (1977); the multidimensional scalar form with $|\nabla u|^2$ is the physical one for a front graph over $\mathbb{R}^2$.

- **1D:** Tadmor (1986) established global well-posedness; Collet–Eckmann–Epstein–Stubbe (1993), Goodman (1994), Bronski–Gambill (2006), Giacomelli–Otto (2005) and Otto (2009) progressively sharpened the bound on $\limsup_t\|u_x\|_{L^2}$ from $O(L^{5/2})$ towards $o(L^{3/2})$ and $L\log^{\ast}$-type estimates. In one dimension the derivative form has the conservative nonlinearity $vv_x$, and $\int v^2v_x\,dx=0$ — the whole 1D theory rests on this identity.
- **2D thin domains:** Sell–Taboada (1992) proved existence of a global attractor on $(0,2\pi)\times(0,\varepsilon)$ for small $\varepsilon$. Molinet (2000) established $L^2$ local dissipativity in dimension two for thin-domain-type geometries and a bounded absorbing set for the related Burgers–Sivashinsky equation.
- **2D anisotropic estimates:** Benachour–Kukavica–Rusin–Ziane (2014) developed the anisotropic Sobolev machinery for 2D KS and obtained global existence under directional smallness/aspect-ratio hypotheses.
- **Modern SOTA:** Ambrose–Mazzucato (2019, 2021) proved global existence and analyticity when the number of linearly growing modes is small — first one growing direction, then one growing mode in each direction — for data satisfying explicit smallness in a Wiener-type analytic algebra. Larios–Yamazaki (2020) proved global well-posedness for the anisotropically *reduced* equation. Coti Zelati–Dolce–Feng–Mazzucato (2021) and Feng–Mazzucato (2022) proved global existence when a strong advecting shear or mixing flow is added, using enhanced dissipation.

No global result is known for the full equation at generic $\nu_1,\nu_2>0$, generic $L_1,L_2$, and arbitrary large data.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| $d=1$, all $L$, all data | GWP + global attractor (Tadmor 1986; Collet et al. 1993) |
| Thin domain $L_2 \ll L_1$ (equivalently $\nu_2/\nu_1 \gg 1$ after rescaling) | Global attractor for $L_2$ below an explicit threshold (Sell–Taboada 1992; Molinet 2000) |
| Reduced nonlinearity $\tfrac12(\partial_x u)^2$ in place of $\tfrac12|\nabla u|^2$ | GWP for large data (Larios–Yamazaki 2020) |
| $\le 1$ linearly growing mode per direction, i.e. $\lambda_i (L_i/2\pi)^2 < 4\nu_i$-type conditions | Global existence and analyticity for data small in an analytic Wiener norm (Ambrose–Mazzucato 2019, 2021) |
| Any $\nu_i, L_i$, small data | Global existence by perturbation of the (finitely unstable) linear semigroup |
| Advection added: $\partial_t u + A\,b(y)\partial_x u + \ldots$, $A$ large | Global existence via enhanced dissipation (Coti Zelati–Dolce–Feng–Mazzucato 2021; Feng–Mazzucato 2022) |
| Any data, any parameters | Local well-posedness in $H^s$, $s>0$; Gevrey/analytic regularization on $(0,T^\ast)$; blow-up criterion $\int_0^{T^\ast}\|\nabla u\|_{L^\infty}^2\,dt = \infty$ |
| Degenerate $\nu_2=0$ | Open even locally in $H^s$ for general data; short-time results require analytic or one-directional data |

## 5. Principal Obstacles

1. **No good energy structure.** The $L^2$ identity for $\mathbf v = \nabla u$ reads
 $$\tfrac12\tfrac{d}{dt}\|\mathbf v\|_{L^2}^2 = -\nu_1\|\partial_x^2\mathbf v\|^2 - \nu_2\|\partial_y^2\mathbf v\|^2 + \lambda_1\|\partial_x\mathbf v\|^2 + \lambda_2\|\partial_y \mathbf v\|^2 + \tfrac12\int (\nabla\!\cdot\!\mathbf v)\,|\mathbf v|^2 .$$
 In 1D the last term is exactly zero. In 2D $\nabla\cdot\mathbf v = \Delta u \not\equiv 0$, so a genuinely cubic, sign-indefinite term survives. Estimating it costs $\|\Delta u\|_{L^2}\|\nabla u\|_{L^4}^2 \lesssim \|\Delta u\|^2\|\nabla u\|$ by Ladyzhenskaya, which is *supercritical* against the available dissipation: the bad term is quadratic in the same norm the dissipation controls, times a growing factor.
2. **Backward heat term.** The energy input $\lambda_i\|\partial_i \mathbf v\|^2$ acts on a band of $O(L_1L_2)$ modes; unlike Navier–Stokes there is no *a priori* dissipative bound at any level to start a bootstrap.
3. **No scaling-critical conserved quantity.** KS is not scale-invariant (the three terms scale differently), so the Navier–Stokes-style critical-space toolbox — Koch–Tataru spaces, mild-solution scaling, Kato methods — gives only local or small-data statements.
4. **Anisotropic estimates are lossy in the balanced case.** The anisotropic Agmon/Ladyzhenskaya inequalities gain only when one direction is genuinely cheap ($\rho \ll 1$ or $\rho\gg1$). At $\rho \approx 1$ they degenerate to the isotropic ones and the smallness constants in Benachour–Kukavica–Rusin–Ziane and Ambrose–Mazzucato become vacuous.
5. **Growth of the unstable band.** All existing global proofs cap the number of unstable modes at $O(1)$; the dynamically interesting spatiotemporal-chaos regime has $\Theta(L_1L_2)$ unstable modes, and the analytic-norm arguments lose an exponential factor in that count.
6. **Degenerate direction.** For $\nu_2=0$ the operator provides no smoothing in $y$; the system resembles an anisotropically-viscous Burgers system where $y$-derivatives can only be transported, and finite-time gradient steepening in $y$ cannot be excluded by any current parabolic argument.

## 6. The Gap

The known global theorems all require the *unstable dynamics to be effectively one-dimensional*: a thin direction (Sell–Taboada), a nonlinearity that sees only one direction (Larios–Yamazaki), $O(1)$ growing modes with small analytic data (Ambrose–Mazzucato), or an imposed mixing flow (Feng–Mazzucato). The general statement requires *no* such reduction. The precise missing step is a bound, uniform on $[0,T^\ast)$ and independent of the aspect ratio $\rho$, on the sign-indefinite cubic term:

$$\Big|\int_{\mathbb{T}^2_L} \Delta u\,|\nabla u|^2 \Big| \le \tfrac{\nu}{2}\|\nabla \Delta u\|_{L^2}^2 + C(L,\nu,\lambda)\big(1+\|\nabla u\|_{L^2}^2\big),$$

or any substitute — a Lyapunov functional, a monotonicity/entropy structure, or a dispersive/Strichartz gain from the fourth-order symbol — that converts local $H^2$ control into a global one. Equivalently: extend the class $\rho \in (0,\varepsilon)\cup(\varepsilon^{-1},\infty)$ where global existence is known to all $\rho \in (0,\infty)$, and remove the smallness requirement on the analytic norm of $u_0$.

## 7. Current Research (as of June 2026)

- **Penn State / Drexel (Mazzucato, Ambrose, Feng).** Analytic Wiener-algebra methods; extending the growing-mode count from $O(1)$ towards $O(\log L)$, and enhanced-dissipation thresholds for shear-advected KS.
- **USC / Nebraska (Kukavica, Larios, Massatt, Yamazaki).** Anisotropic Sobolev estimates, attractor dimension bounds, and interpolation between the reduced equation ($\rho=0$) and the full one ($\rho=1$) — a continuation argument in $\rho$ is the natural target. *(frontier — verify)*
- **Bonn / MPI-MIS lineage (Otto school).** Transfer of the Giacomelli–Otto and Goldman–Josien–Otto bootstrap (which gave near-optimal 1D bounds via a mixed $L^1$/harmonic-analysis argument) to a genuinely two-dimensional setting. *(frontier — verify)*
- **Computer-assisted analysis.** Rigorous validated-numerics continuation of 2D KS equilibria and unstable manifolds on moderate tori; no computer-assisted blow-up scenario has been produced. *(frontier — verify)*
- **Blow-up side.** Self-similar and modulation-ansatz searches for singularity formation, modelled on the Merle–Raphaël–Rodnianski–Szeftel program; no candidate profile for the KS quadratic-gradient nonlinearity with fourth-order dissipation is known.

## 8. Future Work

1. Prove global existence for $\rho$ in a *fixed* interval around $1$ by a continuation argument in the anisotropy parameter, quantifying how the Larios–Yamazaki proof degrades as $\rho$ leaves $0$.
2. Establish an $L^1$ or negative-Sobolev *a priori* bound (2D analogue of the Giacomelli–Otto argument) that survives the non-conservative nonlinearity.
3. Settle local well-posedness for the degenerate case $\nu_2=0$ in Sobolev (not analytic) classes; this decides whether $\nu_2\downarrow 0$ is a singular limit.
4. Replace the smallness of the analytic norm in Ambrose–Mazzucato by smallness of a scaling-adapted seminorm, allowing large data with concentrated spectrum.
5. Numerically probe whether $\sup_t \|\nabla u(t)\|_{L^2}$ grows algebraically in $L$ (as in 1D, $\sim L^{3/2}$) or faster in 2D — a superalgebraic rate would be evidence against uniform bounds.

## 9. Key References

- **[Foundational]** Y. Kuramoto, T. Tsuzuki. *Persistent Propagation of Concentration Waves in Dissipative Media Far from Thermal Equilibrium.* Progress of Theoretical Physics 55 (1976), 356–369.
- **[Foundational]** G. I. Sivashinsky. *Nonlinear analysis of hydrodynamic instability in laminar flames — I. Derivation of basic equations.* Acta Astronautica 4 (1977), 1177–1206.
- **[Foundational]** E. Tadmor. *The well-posedness of the Kuramoto–Sivashinsky equation.* SIAM Journal on Mathematical Analysis 17 (1986), 884–893.
- **[Foundational]** P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe. *A global attracting set for the Kuramoto–Sivashinsky equation.* Communications in Mathematical Physics 152 (1993), 203–214.
- **[2D thin domains]** G. R. Sell, M. Taboada. *Local dissipativity and attractors for the Kuramoto–Sivashinsky equation in thin 2D domains.* Nonlinear Analysis: Theory, Methods & Applications 18 (1992), 671–687.
- **[2D]** L. Molinet. *Local dissipativity in $L^2$ for the Kuramoto–Sivashinsky equation in spatial dimension 2.* Journal of Dynamics and Differential Equations 12 (2000), 533–556.
- **[Anisotropic]** S. Benachour, I. Kukavica, W. Rusin, M. Ziane. *Anisotropic estimates for the two-dimensional Kuramoto–Sivashinsky equation.* Journal of Dynamics and Differential Equations 26 (2014), 461–476.
- **[SOTA]** D. M. Ambrose, A. L. Mazzucato. *Global existence and analyticity for the 2D Kuramoto–Sivashinsky equation.* Journal of Dynamics and Differential Equations 31 (2019), 1525–1547.
- **[SOTA]** D. M. Ambrose, A. L. Mazzucato. *Global solutions of the two-dimensional Kuramoto–Sivashinsky equation with a linearly growing mode in each direction.* Journal of Nonlinear Science 31 (2021), article 96.
- **[SOTA]** A. Larios, K. Yamazaki. *On the well-posedness of an anisotropically-reduced two-dimensional Kuramoto–Sivashinsky equation.* Physica D: Nonlinear Phenomena 411 (2020), 132560.
- **[SOTA]** M. Coti Zelati, M. Dolce, Y. Feng, A. L. Mazzucato. *Global existence for the two-dimensional Kuramoto–Sivashinsky equation with a shear flow.* Journal of Evolution Equations 21 (2021), 5079–5099.
- **[SOTA]** Y. Feng, A. L. Mazzucato. *Global existence for the two-dimensional Kuramoto–Sivashinsky equation with advection.* Communications in Partial Differential Equations 47 (2022), 279–306.
- **[1D bounds]** L. Giacomelli, F. Otto. *New bounds for the Kuramoto–Sivashinsky equation.* Communications on Pure and Applied Mathematics 58 (2005), 297–318.
- **[1D bounds]** F. Otto. *Optimal bounds on the Kuramoto–Sivashinsky equation.* Journal of Functional Analysis 257 (2009), 2188–2245.
- **[Survey/Background]** R. Temam. *Infinite-Dimensional Dynamical Systems in Mechanics and Physics.* 2nd ed., Springer, 1997.

## 10. Worked Example / Concrete Special Case

**Why the 1D proof breaks in 2D.** Take $\lambda_1=\lambda_2=1$ and write $\mathbf v = \nabla u$, so $\partial_t\mathbf v + \nu_1\partial_x^4\mathbf v + \nu_2\partial_y^4\mathbf v + \Delta\mathbf v + (\mathbf v\cdot\nabla)\mathbf v = 0$. Pair with $\mathbf v$ and integrate over $\mathbb{T}^2_L$:

$$\int (\mathbf v\cdot\nabla)\mathbf v\cdot\mathbf v = \int \mathbf v\cdot\nabla\frac{|\mathbf v|^2}{2} = -\frac12\int (\nabla\cdot\mathbf v)|\mathbf v|^2 = -\frac12\int \Delta u\,|\nabla u|^2 .$$

In one dimension the same computation gives $\int v\,v_x\,v\,dx = \frac13\int (v^3)_x\,dx = 0$: the nonlinearity is energy-neutral, and Tadmor's global bound follows from the linear terms alone. In two dimensions the residue $-\tfrac12\int \Delta u|\nabla u|^2$ is not zero and has no sign.

**Size of the residue.** By Ladyzhenskaya, $\|\nabla u\|_{L^4}^2 \le C\|\nabla u\|_{L^2}\|\nabla u\|_{H^1}$, hence

$$\Big|\tfrac12\int\Delta u|\nabla u|^2\Big| \le C\|\Delta u\|_{L^2}^2\|\nabla u\|_{L^2}.$$

The dissipation available at this level is $\nu_1\|\partial_x^2\mathbf v\|^2+\nu_2\|\partial_y^2\mathbf v\|^2 \gtrsim \min(\nu_i)\|\nabla\Delta u\|_{L^2}^2$, which is *two* derivatives above $\|\Delta u\|_{L^2}^2$; interpolating, $\|\Delta u\|^2 \lesssim \|\nabla u\|^{2/3}\|\nabla\Delta u\|^{4/3}$, giving

$$\Big|\tfrac12\int\Delta u|\nabla u|^2\Big| \lesssim \|\nabla u\|_{L^2}^{5/3}\|\nabla\Delta u\|_{L^2}^{4/3} \le \tfrac{\nu}{2}\|\nabla\Delta u\|^2 + C\nu^{-2}\|\nabla u\|_{L^2}^{5}.$$

So $E(t)=\|\nabla u(t)\|_{L^2}^2$ satisfies only $E' \le C_1 E + C_2\nu^{-2}E^{5/2}$ — a Riccati-type inequality whose solutions blow up in finite time unless $E(0)$ is small. This is exactly the small-data restriction in the literature; no known estimate replaces the $E^{5/2}$ term by something subquadratic.

**Where anisotropy helps.** Suppose $\nu_2 \gg \nu_1$, i.e. $\rho=(\nu_1/\nu_2)^{1/2}\ll1$. After the rescaling of §2 the nonlinearity is $(\partial_X v)^2 + \rho(\partial_Y v)^2$, and the residue splits as

$$-\tfrac12\int \Delta v\big[(\partial_X v)^2 + \rho(\partial_Y v)^2\big].$$

At $\rho=0$ the second piece vanishes and the remaining term is controlled by the anisotropic Agmon inequality of §2, yielding the Larios–Yamazaki global result. For $\rho>0$ the extra term contributes $C\rho\,\|\Delta v\|^2\|\nabla v\|$, absorbable only while $\rho\|\nabla v(t)\|_{L^2} \le c\,\nu$. Since no *a priori* bound on $\|\nabla v(t)\|_{L^2}$ exists, this smallness cannot be propagated for $\rho$ of order one — the concrete form of the gap in §6.

**Numerical illustration (two modes).** On $\mathbb{T}^2_{2\pi}$ with $\nu_1=\nu_2=1$, only $|k|=1$ modes are unstable ($\sigma = 1-1 = 0$ at $|k|=1$ for $\lambda=1$; taking $\lambda=2$ gives $\sigma=1>0$). The Galerkin truncation onto $k=(1,0),(0,1),(1,1)$ with $u = a\cos x + b\cos y + c\cos x\cos y$ produces $\dot a = \sigma_1 a + \tfrac12 bc\,(\cdot)$-type couplings: energy injected into $(1,0)$ and $(0,1)$ transfers to $(1,1)$, where $\sigma(1,1) = 2\lambda-2\nu<0$ for $\nu>\lambda$, and is dissipated. Global boundedness of this truncation is elementary; the open problem is whether that mode-by-mode balance survives when $\Theta(L_1L_2)$ modes are unstable and the transfer cascade is not a priori downhill.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*