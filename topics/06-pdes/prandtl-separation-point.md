---
id: 06-pdes/prandtl-separation-point
title: "Prandtl Separation Point"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Prandtl Separation Point

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/prandtl-separation-point` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Boundary-layer separation is the event in which fluid near a solid wall reverses direction, the wall shear stress vanishes, and the layer detaches from the boundary. Prandtl (1904) predicted it with the equation that bears his name. The mathematical problem is to prove that this prediction is *correct as an asymptotic description of Navier–Stokes flow*.

Three linked statements, in increasing strength:

- **(S1) Separation in Prandtl.** For open classes of outer data $u_e$ (steady) or initial data $u_0$ (unsteady), the Prandtl system develops a separation singularity in finite $x$ or finite $t$: the wall shear $\partial_y u(x,0)$ reaches zero and the solution ceases to exist in $C^1$, with a quantified local profile.
- **(S2) Universality of the profile.** Near the separation point the solution obeys the Goldstein square-root law (steady) or the van Dommelen–Shen Lagrangian-compression law (unsteady), and this behaviour is stable under perturbation of the data.
- **(S3) The Navier–Stokes justification — the open core.** For Navier–Stokes with no-slip on a domain $\Omega$ at viscosity $\nu\to0$, with data whose formal boundary layer separates at $(x_s,t_s)$, the Navier–Stokes solution $u^\nu$ satisfies
$$\|u^\nu - u^E - u^P\|_{L^\infty} \longrightarrow 0 \quad (\nu\to 0)$$
on a time interval reaching up to (and, in a corrected form, past) $t_s$, where $u^E$ is the Euler solution and $u^P$ the Prandtl corrector; and the vorticity ejected at $(x_s,t_s)$ is of size $O(\nu^{-\alpha})$ for a determined $\alpha>0$.

A complete resolution means a proof or disproof of (S3) for a nontrivial class of data. (S1) is now proved in several regimes; (S3) is open in every regime where separation actually occurs.

## 2. Mathematical Foundations

**Prandtl system.** On the half-plane $\{(x,y): y>0\}$, after the scaling $y = \tilde y/\sqrt{\nu}$, $v = \sqrt{\nu}\,\tilde v$,
$$
\begin{cases}
\partial_t u + u\,\partial_x u + v\,\partial_y u = -\partial_x p_e + \partial_y^2 u,\\[2pt]
\partial_x u + \partial_y v = 0,\\[2pt]
u|_{y=0} = v|_{y=0} = 0, \qquad \lim_{y\to\infty} u(t,x,y) = u_e(t,x),
\end{cases}
$$
with the Bernoulli relation $-\partial_x p_e = \partial_t u_e + u_e\partial_x u_e$ inherited from the outer Euler flow. There is **no equation for $p$ in $y$**: the pressure is prescribed, and the system is degenerate — parabolic in $y$, hyperbolic-transport in $x$, with $v = -\int_0^y \partial_x u$ a nonlocal, one-derivative-losing term.

**Steady Prandtl.** $u\partial_x u + v\partial_y u = u_e u_e' + \partial_y^2 u$, treated as an evolution in $x$.

**Separation point.** $(t_s,x_s)$ with
$$\lambda(t,x) := \partial_y u(t,x,0), \qquad \lambda(t_s,x_s)=0,\quad \lambda>0 \text{ before}.$$
Downstream/afterwards $\lambda<0$ (reversed flow).

**Displacement thickness.** $\displaystyle \delta^*(x) = \int_0^\infty\Big(1-\frac{u}{u_e}\Big)\,dy$. Separation is characterised by $\partial_x\delta^*\to+\infty$, equivalently by $v$ becoming unbounded, which destroys the two-scale ansatz.

**Crocco transform** (steady, monotone case): with $\eta = u/u_e$ and $w = \partial_y u/u_e$, the system becomes the scalar degenerate parabolic equation
$$ \eta\,\partial_x w \;=\; w^2\partial_\eta^2 w \;-\; \frac{u_e'}{u_e}\Big(\ldots\Big), $$
degenerating exactly where $w\to 0$, i.e. at separation. Oleinik's theory is built here.

**Van Dommelen–Shen criterion.** In Lagrangian coordinates $\xi\mapsto X(t,\xi)$, unsteady separation is the event
$$\partial_\xi X(t,\xi) \to 0 \quad\text{at some } \xi_0,\ t\to t_s^-,$$
with $\partial_\xi Y$ correspondingly blowing up: an infinite-slope spike in the displacement thickness while $u$ itself stays bounded.

**Goldstein profile (steady).** As $x\uparrow x_s$,
$$\lambda(x) \sim a\,(x_s-x)^{1/2}, \qquad \delta^*(x) = \delta_0^* - c\,(x_s-x)^{1/2} + \cdots,\qquad \partial_x\delta^* \sim \tfrac{c}{2}(x_s-x)^{-1/2}.$$

**Well-posedness background theorems relied on.** Oleinik's local existence under $\partial_y u_0>0$; Sammartino–Caflisch analytic well-posedness and inviscid limit; Gérard-Varet–Dormy ill-posedness in Sobolev for non-monotone data; Gérard-Varet–Masmoudi Gevrey well-posedness.

## 3. History & State of the Art (SOTA)

- **1904.** Prandtl, Heidelberg ICM: the boundary layer, and the first drawing of a separation point.
- **1948.** Goldstein derives the steady square-root singularity and shows the boundary-layer hierarchy cannot be continued past it — the "Goldstein barrier".
- **1958.** Stewartson; **1969** Sychev, Neiland — triple-deck theory: an interactive $\nu^{3/8}$–$\nu^{1/2}$–$\nu^{5/8}$ structure that regularises Goldstein's singularity for *separation induced by an obstacle*. Free-interaction theory; still asymptotic, not rigorous.
- **1963–1967.** Oleinik: local-in-$x$ (steady) and local-in-$t$ (unsteady) existence/uniqueness under monotone-in-$y$ data via Crocco.
- **1980.** Van Dommelen & Shen: the impulsively started circular cylinder computed in Lagrangian variables blows up at $t_s\approx 1.5\,a/U_\infty$ — the first convincing unsteady separation singularity.
- **1997.** E & Engquist: rigorous finite-time blow-up for a class of unsteady Prandtl solutions (with a symmetry ansatz).
- **1998.** Sammartino & Caflisch: existence and the Prandtl inviscid limit for *analytic* data — short time, before separation.
- **2010.** Gérard-Varet & Dormy: linear/nonlinear ill-posedness in Sobolev spaces around non-monotone shear flows; combined with Grenier (2000), this shows the boundary-layer expansion itself fails for general Sobolev data.
- **2014–2019.** Maekawa (analyticity only near the boundary); Gérard-Varet–Masmoudi (Gevrey $7/4$); Dietert–Gérard-Varet (Gevrey 2, no monotonicity) — the current well-posedness frontier.
- **2017–2021.** Kukavica–Vicol–Wang give a rigorous construction of the van Dommelen–Shen singularity; Dalibard–Masmoudi prove steady separation with the Goldstein rate; Shen–Wang–Zhang refine the local structure at the separation point.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| Steady, $u_e'<0$ (adverse pressure gradient), monotone data | Solution exists up to a finite $x_s>0$ where $\lambda(x_s)=0$; $\lambda(x)\sim a\sqrt{x_s-x}$; $\partial_x\delta^*\to+\infty$ | Dalibard–Masmoudi 2019 |
| Steady, refined local structure at $x_s$ (higher-order expansion, $C^\infty$ away from wall) | Full asymptotic series in $(x_s-x)^{1/2}$ | Shen–Wang–Zhang 2021 |
| Unsteady, real-analytic data, symmetric ($u$ odd, $v$ even in $x$) | Finite-time blow-up of $\partial_x u$ | Kukavica–Vicol–Wang 2017 (also E–Engquist 1997) |
| Unsteady, $u_e\equiv0$, analytic | Blow-up of $\|\partial_x u\|_{L^\infty}$ in finite time with van Dommelen rate | Kukavica–Vicol–Wang 2017 |
| Burgers-with-transverse-viscosity model $\partial_t u+u\partial_x u=\partial_y^2u$ | Stable, generic, self-similar singularity with explicit profile; codimension-0 in the model | Collot–Ghoul–Masmoudi 2022 |
| 2D Prandtl, formal/matched-asymptotic self-similar separation profile | Constructed and stability-analysed | Collot–Ghoul–Masmoudi (arXiv:1808.05967) |
| Inviscid limit **before** separation, analytic data | $\|u^\nu-u^E-u^P\|\to0$ on $[0,T]$, $T$ independent of $\nu$ | Sammartino–Caflisch 1998 |
| Inviscid limit, data with $\omega_0$ vanishing near $\partial\Omega$ | Same conclusion, Sobolev-type data | Maekawa 2014 |

Numerically: the impulsively started cylinder separates at $t_s = 1.5023$ (in units $a/U_\infty$) at angle $\approx 111^\circ$ from the front stagnation point (van Dommelen–Shen); the steady Falkner–Skan separation exponent is $\beta_s = -0.198838$.

## 5. Principal Obstacles

- **The equation is ill-posed exactly where it is interesting.** Reverse flow ($\lambda<0$) means non-monotone profiles, and Gérard-Varet–Dormy show the linearised Prandtl operator has unstable modes with growth $e^{t\sqrt{|k|}}$ — derivative loss of order $1/2$ that no Sobolev energy estimate can absorb. Separation *produces* the data on which the equation is unstable.
- **Gevrey is not enough past the singularity.** The Gevrey-2 threshold (Dietert–Gérard-Varet) is sharp against the $\sqrt{|k|}$ growth, but Gevrey regularity is destroyed by the singularity itself; there is no functional framework in which to continue.
- **Goldstein's barrier is a genuine breakdown of the ansatz, not a technical loss.** At $x_s$, $v\sim(x_s-x)^{-1/2}$, so the neglected term $\nu\partial_x^2u$ is no longer subdominant. The correct object past separation is the triple deck, which is a *different* PDE system, itself lacking a well-posedness theory.
- **No maximum principle survives.** Crocco's transform requires $\partial_y u>0$; it degenerates at the wall precisely at separation, converting a parabolic problem into one with a vanishing diffusion coefficient on the boundary of the domain of interest.
- **The inviscid limit is unproved even without separation for generic Sobolev data.** Kato-type criteria ($\nu\int_0^T\|\nabla u^\nu\|_{L^2(\Gamma_{c\nu})}^2\,dt\to0$) are equivalent reformulations, not tools; separation is exactly the mechanism suspected to violate them.
- **Instability of the Euler leading order.** Grenier's nonlinear instability shows the expansion $u^\nu\approx u^E+u^P$ can fail at order $O(1)$ for boundary layers of inflectional type, so even a perfect Prandtl theory would not settle (S3).

## 6. The Gap

Proved: separation exists inside the Prandtl model, in steady adverse-gradient flow (Dalibard–Masmoudi) and in unsteady analytic/symmetric settings (Kukavica–Vicol–Wang), with the predicted rates.

Missing: everything connecting that model to Navier–Stokes at the separation time. Concretely, the gap is:

1. **Stability of the singularity in Prandtl** without symmetry or analyticity — an open set of Sobolev/Gevrey data producing the van Dommelen profile, with codimension-0.
2. **A continuation theory** — the triple-deck system, or an interactive boundary-layer system, shown to be locally well-posed and to match Goldstein's expansion on both sides.
3. **$\nu$-uniform control across $t_s$**: a bound on $u^\nu-u^E-u^P$ that does not degenerate as $t\to t_s$, on a time window of length $\gg \nu^{\alpha}$. Current proofs all lose at $t_s^-$ because the Prandtl remainder equation's forcing scales like $\|\partial_x^2 u^P\|\sim(t_s-t)^{-3/2}$ against a $\nu^{1/2}$ prefactor, so the estimate closes only until $t_s-t\sim\nu^{1/3}$.

Crossing (3) is the precise mathematical step.

## 7. Current Research (as of June 2026)

- **NYU / NYU Abu Dhabi (Masmoudi, Ghoul) and Sorbonne (Dalibard, Gérard-Varet).** Self-similar analysis of the Prandtl separation profile with modulation/spectral methods imported from wave-collapse theory; the transverse-viscosity Burgers model is the proving ground. *(frontier — verify: extension of the codimension-0 stability from the model to the full Prandtl system.)*
- **USC / Wisconsin (Kukavica, Vicol, Wang, Ionescu).** Lagrangian and analyticity-radius methods; quantitative lifespan lower bounds $T\gtrsim \varepsilon^{-1}$ for small data, and blow-up criteria phrased in terms of $\partial_x u$.
- **Peking / Chinese Academy of Sciences (Z. Zhang, C. Wang, Y. Wang, W. Shen).** Steady separation structure, the Triple Deck, and rigorous justification of interactive boundary-layer models. *(frontier — verify: claimed local well-posedness results for triple-deck systems.)*
- **ENS Lyon / Grenier–Nguyen school.** Sharp instability and the sub-layer (Tollmien–Schlichting) route to failure of the expansion; recent work on the $\nu^{1/8}$ threshold for validity of Prandtl asymptotics.
- **Computational.** High-resolution Lagrangian and spectral schemes verifying the van Dommelen rate $\partial_\xi X\sim(t_s-t)$ and the $|\ln(t_s-t)|$ corrections.

## 8. Future Work

- Prove stability of the van Dommelen–Shen singularity for an open set of Gevrey-2 data — the direct sequel to Collot–Ghoul–Masmoudi.
- Establish local well-posedness of the triple-deck / interactive boundary-layer system, then match it to the Goldstein expansion; this would give the first mathematically meaningful "past separation" statement.
- Attack (S3) in the simplest possible geometry: rotating disk, or steady flow over a bump with prescribed adverse gradient, where the separation point is fixed and the analysis is essentially one-dimensional in $x$.
- Sharpen Kato-type criteria into a *separation-aware* criterion: an anomalous-dissipation statement conditional on the wall-shear vanishing.
- Determine whether energy dissipation is anomalous at separation, i.e. whether $\nu\int|\nabla u^\nu|^2$ stays bounded below as $\nu\to0$ — the physical content of the whole question.

## 9. Key References

- **[Foundational]** L. Prandtl. *Über Flüssigkeitsbewegung bei sehr kleiner Reibung.* Verh. III. Int. Math.-Kongr., Heidelberg, 1904, pp. 484–491.
- **[Foundational]** S. Goldstein. *On laminar boundary-layer flow near a position of separation.* Quarterly Journal of Mechanics and Applied Mathematics 1 (1948), 43–69.
- **[Foundational]** O. A. Oleinik, V. N. Samokhin. *Mathematical Models in Boundary Layer Theory.* Chapman & Hall/CRC, 1999.
- **[Foundational]** L. L. van Dommelen, S. F. Shen. *The spontaneous generation of the singularity in a separating laminar boundary layer.* Journal of Computational Physics 38 (1980), 125–140.
- **[Foundational]** W. E, B. Engquist. *Blowup of solutions of the unsteady Prandtl's equation.* Communications on Pure and Applied Mathematics 50 (1997), 1287–1293.
- **[Foundational]** M. Sammartino, R. E. Caflisch. *Zero viscosity limit for analytic solutions of the Navier–Stokes equation on a half-space, I & II.* Communications in Mathematical Physics 192 (1998), 433–461 and 463–491.
- **[SOTA]** A.-L. Dalibard, N. Masmoudi. *Separation for the stationary Prandtl equation.* Publications mathématiques de l'IHÉS 130 (2019), 187–297.
- **[SOTA]** I. Kukavica, V. Vicol, F. Wang. *The van Dommelen and Shen singularity in the Prandtl equations.* Advances in Mathematics 307 (2017), 288–311.
- **[SOTA]** C. Collot, T.-E. Ghoul, N. Masmoudi. *Singularity formation for Burgers equation with transverse viscosity.* Annales Scientifiques de l'École Normale Supérieure 55 (2022), 1047–1133.
- **[SOTA]** C. Collot, T.-E. Ghoul, N. Masmoudi. *On singularity formation for the two-dimensional unsteady Prandtl system.* arXiv:1808.05967.
- **[SOTA]** W. Shen, Y. Wang, Z. Zhang. *Boundary layer separation and local behavior for the steady Prandtl equation.* Advances in Mathematics 389 (2021), 107896.
- **[SOTA]** D. Gérard-Varet, E. Dormy. *On the ill-posedness of the Prandtl equation.* Journal of the American Mathematical Society 23 (2010), 591–609.
- **[SOTA]** D. Gérard-Varet, N. Masmoudi. *Well-posedness for the Prandtl system without analyticity or monotonicity.* Annales Scientifiques de l'ENS 48 (2015), 1273–1325.
- **[SOTA]** H. Dietert, D. Gérard-Varet. *Well-posedness of the Prandtl equations without any structural assumption.* Annals of PDE 5 (2019), art. 8.
- **[SOTA]** Y. Maekawa. *On the inviscid limit problem of the vorticity equations for viscous incompressible flows in the half-plane.* Communications on Pure and Applied Mathematics 67 (2014), 1045–1128.
- **[Survey]** E. Grenier. *On the nonlinear instability of Euler and Prandtl equations.* Communications on Pure and Applied Mathematics 53 (2000), 1067–1091.
- **[Survey]** H. Schlichting, K. Gersten. *Boundary-Layer Theory.* 9th ed., Springer, 2017.
- **[Survey]** T. D. Drivas, H. Q. Nguyen. *Remarks on the emergence of weak Euler solutions in the vanishing viscosity limit.* Journal of Nonlinear Science 29 (2019), 709–721.

## 10. Worked Example / Concrete Special Case

**Steady separation and the Goldstein exponent, computed at the wall.**

Take steady Prandtl with outer flow $u_e(x)>0$, $u_e'(x)<0$ (deceleration). Evaluate the momentum equation at $y=0$, where $u=v=0$:
$$\partial_y^2 u(x,0) \;=\; -\,u_e(x)u_e'(x) \;=\; \partial_x p_e(x) \;>\;0 .$$
So the profile is convex at the wall whenever the pressure gradient is adverse. Write $\lambda(x)=\partial_y u(x,0)$ and expand:
$$u(x,y) = \lambda(x)\,y + \tfrac12\,p_e'(x)\,y^2 + O(y^3).$$
As long as $\lambda>0$ the profile rises monotonically; when $\lambda(x_s)=0$ the leading behaviour becomes $u\approx \tfrac12 p_e'(x_s) y^2 \ge 0$, and immediately downstream $\lambda<0$ produces a reversed-flow region $0<y<2|\lambda|/p_e'$.

**Rate.** Insert the ansatz $\lambda(x) = a\,(x_s-x)^{\gamma}$ into the integrated momentum (von Kármán) balance
$$\frac{d\theta}{dx} + (2\theta+\delta^*)\frac{u_e'}{u_e} = \frac{\lambda}{u_e^2},\qquad \theta=\int_0^\infty\frac{u}{u_e}\Big(1-\frac{u}{u_e}\Big)dy .$$
Goldstein's matched expansion in the inner region $y\sim(x_s-x)^{1/4}$ fixes $\gamma=1/2$: the inner variable is $\zeta = y/(x_s-x)^{1/4}$, and consistency of the $O(1)$ balance $u\partial_xu \sim \partial_y^2u$ with $u\sim (x_s-x)^{1/2}\zeta$ requires
$$\frac{(x_s-x)^{1/2}\cdot (x_s-x)^{-1/2}}{1}\;\sim\;\frac{(x_s-x)^{1/2}}{(x_s-x)^{1/2}} ,$$
which holds only for $\gamma=1/2$. Then
$$\delta^*(x)=\delta_0^*-c\,(x_s-x)^{1/2},\qquad \partial_x\delta^*(x)=\frac{c}{2}(x_s-x)^{-1/2}\xrightarrow[x\to x_s^-]{}+\infty,$$
and since $v(x,\infty)=u_e\,\partial_x\delta^*$ (up to $u_e'$ terms), the transverse velocity blows up like $(x_s-x)^{-1/2}$. This is exactly Dalibard–Masmoudi's theorem, made rigorous with $a>0$ determined by the data.

**A closed-form sanity check.** The self-similar Falkner–Skan family $u_e=Cx^m$, $u=u_ef'(\eta)$, $\eta=y\sqrt{u_e/x}$, gives
$$f'''+f f''+\beta\bigl(1-(f')^2\bigr)=0,\qquad \beta=\frac{2m}{m+1},\qquad f(0)=f'(0)=0,\ f'(\infty)=1.$$
Numerically $f''(0)=0$ at $\beta_s=-0.198838$ ($m\approx-0.0904$). At that value the wall shear vanishes identically for all $x>0$ — a *marginally separating* flow. For $\beta<\beta_s$ no solution with $f'\ge0$ exists: the boundary layer cannot remain attached. This single number is the exact self-similar shadow of the separation point, and it is the reason the Goldstein exponent is $1/2$ and not something else: perturbing $\beta$ below $\beta_s$ by $\varepsilon$ moves the separation location by $O(\varepsilon)$ while $\lambda$ scales like $\varepsilon^{1/2}$.

**Unsteady counterpart.** For the impulsively started cylinder, $u_e(x)=2U_\infty\sin(x/a)$, Lagrangian computation gives $\partial_\xi X(t,\xi_0)\to0$ linearly in $(t_s-t)$ at $t_s=1.5023\,a/U_\infty$, $x_s/a\approx1.94$ rad ($\approx111^\circ$), with $\delta^*\sim(t_s-t)^{-1/4}$ — bounded $u$, unbounded thickness. This is the singularity whose Navier–Stokes justification is (S3), and which remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*