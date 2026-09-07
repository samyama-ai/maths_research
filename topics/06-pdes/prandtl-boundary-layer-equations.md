---
id: 06-pdes/prandtl-boundary-layer-equations
title: "Prandtl Boundary Layer Equations"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Prandtl Boundary Layer Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/prandtl-boundary-layer-equations` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two linked open questions:

**(P1) Well-posedness of the Prandtl system.** For which function spaces and which classes of data is the initial–boundary value problem for the Prandtl equations locally well-posed, and when do solutions form singularities in finite time? The system is well-posed in analytic and (in 2D) Gevrey-$2$ classes, and ill-posed in Sobolev spaces without structural assumptions. The gap between "Gevrey-$2$ well-posed" and "Sobolev ill-posed" is essentially closed in 2D; the 3D picture, and the global-in-time behaviour of monotone data, are not.

**(P2) Justification of the inviscid limit / Prandtl expansion.** Let $u^\nu$ solve the incompressible Navier–Stokes equations on a domain with a no-slip boundary. Does
$$u^\nu(t,x,y) \;=\; u^E(t,x,y) \;+\; u^P\!\left(t,x,\tfrac{y}{\sqrt\nu}\right) \;+\; o(1) \quad \text{in } L^\infty \text{ as } \nu \to 0,$$
with $u^E$ the Euler solution and $u^P$ the Prandtl corrector, hold on a time interval independent of $\nu$, for data merely Sobolev-smooth? A complete solution means either a proof for finite-regularity data, or a rigorous counterexample where the expansion fails at leading order in $L^\infty$ before the Euler solution's lifespan.

## 2. Mathematical Foundations

Take the half-plane $\Omega=\{(x,y): y>0\}$ and Navier–Stokes with viscosity $\nu=\varepsilon^2$:
$$\partial_t u^\nu + (u^\nu\!\cdot\!\nabla)u^\nu + \nabla p^\nu = \nu\,\Delta u^\nu,\qquad \nabla\!\cdot\! u^\nu=0,\qquad u^\nu|_{y=0}=0 .$$
Rescale $Y=y/\varepsilon$, $v=\varepsilon^{-1}u_2$. At leading order in $\varepsilon$ one obtains the **Prandtl equations** for $(u,v)(t,x,Y)$:
$$
\begin{cases}
\partial_t u + u\,\partial_x u + v\,\partial_Y u \;-\; \partial_Y^2 u \;=\; -\partial_x p^E(t,x),\\[2pt]
\partial_x u + \partial_Y v = 0,\\[2pt]
u|_{Y=0}=v|_{Y=0}=0,\qquad \lim_{Y\to\infty} u = U(t,x),
\end{cases}
$$
where $U=u^E_1|_{y=0}$ and Bernoulli gives $-\partial_x p^E = \partial_t U + U\partial_x U$. Note $v(t,x,Y)=-\int_0^Y \partial_x u\,dY'$: the vertical velocity is **one derivative worse** in $x$ than $u$, and the system has **no $\partial_x^2$ term**. This "loss of one tangential derivative" is the entire analytic difficulty.

**Degenerate structure.** Linearizing about a shear flow $u_s(t,Y)$ gives
$$\partial_t u + u_s \partial_x u + v\,u_s' - \partial_Y^2 u = 0,$$
whose symbol in $\xi$ (dual to $x$) has, for non-monotone $u_s$, growing modes with rate $\sim \sqrt{|\xi|}$ (Gérard-Varet–Dormy). Since $e^{c\sqrt{|\xi|}\,t}$ is bounded on Gevrey class $G^{\sigma}$ exactly for $\sigma\le 2$, **Gevrey-$2$ is the natural and optimal regularity threshold**.

**Crocco / Oleinik structure.** If $\partial_Y u>0$ (monotone profile), set $w=\partial_Y u$ and use the good unknown of Masmoudi–Wong,
$$g \;=\; \partial_Y u \;-\; \frac{\partial_Y^2 u}{\partial_Y u}\, u ,$$
which satisfies a transport–diffusion equation in which the dangerous term $v\,\partial_Y^2 u$ cancels. Equivalently, Crocco's transformation $\xi = u/U$, $w(t,x,\xi)=\partial_Y u$ converts the system to a scalar degenerate parabolic equation
$$\partial_t w + \xi U \partial_x w + \ldots = w^2 \partial_\xi^2 w .$$

**Gevrey class.** $f\in G^\sigma_\tau$ iff $\|\partial_x^k f\|\le C\,\tau^{-k}(k!)^{\sigma}$; $\sigma=1$ is analytic, $\sigma=\infty$ is $C^\infty$.

**Kato's criterion (1984).** The inviscid limit $u^\nu\to u^E$ in $L^\infty_t L^2_x$ holds on $[0,T]$ iff
$$\nu \int_0^T \!\!\int_{\{ \mathrm{dist}(z,\partial\Omega)<c\nu\}} |\nabla u^\nu|^2 \,dz\,dt \;\longrightarrow\; 0 .$$

## 3. History & State of the Art (SOTA)

- **1904.** Ludwig Prandtl, *Über Flüssigkeitsbewegung bei sehr kleiner Reibung*, Third Int. Congress of Mathematicians, Heidelberg — introduces the boundary layer and the equations.
- **1908.** Blasius computes the self-similar steady flat-plate profile.
- **1963.** O. A. Oleinik: local-in-time classical solutions for **monotone** data via Crocco; global existence for small $U$ (with Samokhin, monograph 1999).
- **1984.** T. Kato: energy-dissipation criterion for the inviscid limit.
- **1980–1990s.** van Dommelen–Shen: numerical evidence of finite-time separation singularity for impulsively started flow past a cylinder. E–Engquist (1997): rigorous finite-time blow-up for a class of Prandtl solutions.
- **1998.** Sammartino–Caflisch: well-posedness of Prandtl **and** validity of the inviscid limit for **analytic** data.
- **2010.** Gérard-Varet–Dormy: linear ill-posedness in Sobolev for non-monotone shear flows ($\sqrt{|\xi|}$ growth).
- **2015.** Alexandre–Wang–Xu–Yang (JAMS) and Masmoudi–Wong (CPAM), independently: local well-posedness in **Sobolev** for monotone data by pure energy methods, no Crocco.
- **2015–2019.** Gérard-Varet–Masmoudi: 2D well-posedness in Gevrey $\sigma=7/4$, improved by Dietert–Gérard-Varet (2019) to **Gevrey-$2$ with no structural assumption** — matching the instability threshold.
- **2017–2020.** Grenier–Nguyen: $L^\infty$ instability of Prandtl expansions; Kukavica–Vicol–Wang: rigorous van Dommelen–Shen singularity.

## 4. Partial Results / Verified Cases

| Class | Result | Reference |
|---|---|---|
| Analytic data, 2D & 3D | Local well-posedness + inviscid limit valid | Sammartino–Caflisch (1998); Nguyen–Nguyen (2018) short proof |
| Data analytic in $x$ only, Sobolev in $Y$ | Local well-posedness | Kukavica–Vicol (2013); Ignatova–Vicol (2016) — lifespan $T\gtrsim \varepsilon^{-1}$ for data of size $\varepsilon$ |
| 2D, Gevrey $\sigma\le 2$ in $x$, arbitrary profile | Local well-posedness | Dietert–Gérard-Varet (2019) |
| 2D, Gevrey $\sigma\le 3/2$ with a single non-degenerate critical curve | Well-posedness | Li–Yang (2020) |
| 2D, Sobolev $H^s$, $\partial_Y u_0>0$ | Local well-posedness; blow-up criterion | Alexandre–Wang–Xu–Yang (2015); Masmoudi–Wong (2015) |
| 2D, monotone + small analytic perturbation of Blasius | Global existence, $u\to$ self-similar | Wang–Wang–Zhang; Ignatova–Vicol type almost-global bounds |
| 2D, non-monotone Sobolev | **Ill-posed** (no Lipschitz solution map $H^s\to L^2$) | Gérard-Varet–Dormy (2010); Gérard-Varet–Nguyen (2012) |
| 3D, general | Ill-posed in Sobolev even for monotone-in-one-direction data unless the two components are aligned | Liu–Wang–Yang (2016, 2017) |
| Inviscid limit, data with vorticity vanishing near $\partial\Omega$ | Valid, $L^\infty$ | Maekawa (2014, CPAM) |
| Inviscid limit, Gevrey-$2$ shear + Sobolev perturbation | Valid | Gérard-Varet–Maekawa–Masmoudi (2018, 2020) |
| Steady Prandtl, favourable pressure gradient $\partial_x p^E\le 0$ | Global existence, no separation | Oleinik; Wang–Zhang for separation with adverse gradient |
| Singularity | Finite-time blow-up of $\partial_x u$ (van Dommelen–Shen) rigorously constructed | Kukavica–Vicol–Wang (2017); E–Engquist (1997) |

## 5. Principal Obstacles

- **Derivative loss with no smoothing in $x$.** The term $v\,\partial_Y u = -\left(\int_0^Y \partial_x u\right)\partial_Y u$ costs one $x$-derivative, and the only dissipation is $\partial_Y^2$. Standard parabolic energy estimates therefore close only if the loss is paid for by shrinking an analyticity/Gevrey radius (an abstract Cauchy–Kovalevskaya scheme) or cancelled by monotonicity. In Sobolev, neither is available.
- **Genuine instability, not a technical gap.** Gérard-Varet–Dormy exhibit growth $e^{\delta\sqrt{|\xi|}t}$, so ill-posedness is a property of the equation. No Sobolev theory can exist without structure.
- **Nonlinear instability is $L^\infty$-scale.** Grenier's construction and Grenier–Nguyen show the Prandtl expansion itself can fail at $O(1)$ in $L^\infty$: even a well-posed Prandtl solution need not describe the Navier–Stokes solution, because the $O(\sqrt\nu)$-scale layer amplifies Tollmien–Schlichting-type modes over times $\sim \nu^{1/4}|\log\nu|$.
- **Separation destroys monotonicity.** The Oleinik/Masmoudi–Wong hypothesis $\partial_Y u>0$ is exactly what fails at the separation point $\partial_Y u|_{Y=0}=0$ — the physically interesting regime.
- **Kato's criterion is not verifiable.** Controlling $\nu\int|\nabla u^\nu|^2$ in the $O(\nu)$ sublayer requires uniform gradient bounds, which is essentially the original problem.
- **3D has no Crocco.** The Crocco transform and the good unknown $g$ are one-dimensional in the tangential variable; the cross-flow term $w\,\partial_z u$ has no known cancellation.

## 6. The Gap

Precisely three fronts.

1. **Regularity threshold in 3D.** In 2D, well-posedness holds for $\sigma\le 2$ and fails for $\sigma>2$ — closed. In 3D, ill-posedness is known (Liu–Wang–Yang) but the sharp Gevrey index is not; no analogue of Dietert–Gérard-Varet exists.
2. **Finite-regularity inviscid limit.** All positive results ($L^\infty$ convergence for $\nu\to0$) require analyticity, Gevrey-$2$, or vorticity vanishing at the boundary. For general $H^s$ data ($s$ large), it is unknown whether $\|u^\nu-u^E\|_{L^2}\to0$ on a fixed time interval — and unknown whether it fails.
3. **Global behaviour of monotone 2D solutions.** Local existence is known; whether $\partial_Y u|_{Y=0}$ can vanish in finite time from smooth monotone data with adverse pressure gradient (i.e. rigorous separation as a boundary-layer-equation phenomenon, not a Lagrangian singularity) is open.

The step to cross for (2): an a priori bound on the boundary-layer vorticity in the $\nu$-sublayer that is uniform in $\nu$ and uses only finite regularity — equivalently, ruling out the transient algebraic growth of order $\nu^{-1/4}$ that the linearized Navier–Stokes operator near a shear layer genuinely produces.

## 7. Current Research (as of June 2026)

- **Gevrey optimality and hydrostatic analogues.** Gérard-Varet (Paris Cité), Masmoudi (NYU/NYUAD), Dietert (Jussieu): transfer of the Gevrey-$2$ method to hydrostatic Euler, MHD boundary layers (where a transverse magnetic field restores Sobolev well-posedness — Liu–Xie–Yang), and compressible layers.
- **Instability and transition.** Grenier (ENS Lyon), Nguyen (Penn State): sharp Tollmien–Schlichting growth rates $\nu^{-1/4}$ and construction of Navier–Stokes solutions violating the Prandtl expansion. *(frontier — verify)* Recent work aims at instability for **monotone, spectrally stable** Euler data, which would show that Prandtl well-posedness does not imply expansion validity.
- **Separation.** Wang–Zhang (Peking), Dalibard–Masmoudi: rigorous steady separation with adverse pressure gradient; the unsteady analogue remains partly numerical.
- **Steady 3D and moving boundaries.** Iyer–Masmoudi program on steady Prandtl over a plate, including global-in-$x$ stability of Blasius and the Triple Deck.
- **Data-driven/numerical.** High-precision Lagrangian computations of van Dommelen–Shen-type blow-up rates; spectral verification of the $\sqrt{|\xi|}$ growth law.

## 8. Future Work

- Prove or disprove Gevrey-$2$ well-posedness for 3D Prandtl without structural assumptions.
- Produce a counterexample to the inviscid limit in $L^2$ for $C^\infty$ (non-analytic) data — widely viewed as more likely than a positive theorem.
- Establish that Kato's criterion holds for data whose vorticity is initially concentrated away from the boundary, in a class stable under the flow.
- Extend the Masmoudi–Wong good unknown beyond monotonicity, e.g. to profiles with finitely many non-degenerate critical points in Sobolev-plus-Gevrey hybrid spaces.
- Classify the possible singularity types of unsteady Prandtl: Lagrangian (van Dommelen–Shen) vs. Eulerian separation.

## 9. Key References

- **[Foundational]** L. Prandtl. *Über Flüssigkeitsbewegung bei sehr kleiner Reibung.* Verh. III. Int. Math.-Kongr., Heidelberg, 1904, pp. 484–491.
- **[Foundational]** O. A. Oleinik, V. N. Samokhin. *Mathematical Models in Boundary Layer Theory.* Chapman & Hall/CRC, 1999.
- **[Foundational]** M. Sammartino, R. E. Caflisch. *Zero viscosity limit for analytic solutions of the Navier–Stokes equation on a half-space, I & II.* Comm. Math. Phys. 192 (1998), 433–461 and 463–491.
- **[Foundational]** T. Kato. *Remarks on zero viscosity limit for nonstationary Navier–Stokes flows with boundary.* In: Seminar on Nonlinear PDE, MSRI Publ. 2, Springer, 1984.
- **[Key]** W. E, B. Engquist. *Blowup of solutions of the unsteady Prandtl's equation.* Comm. Pure Appl. Math. 50 (1997), 1287–1293.
- **[Key]** D. Gérard-Varet, E. Dormy. *On the ill-posedness of the Prandtl equation.* J. Amer. Math. Soc. 23 (2010), 591–609.
- **[Key]** R. Alexandre, Y.-G. Wang, C.-J. Xu, T. Yang. *Well-posedness of the Prandtl equation in Sobolev spaces.* J. Amer. Math. Soc. 28 (2015), 745–784.
- **[Key]** N. Masmoudi, T. K. Wong. *Local-in-time existence and uniqueness of solutions to the Prandtl equations by energy methods.* Comm. Pure Appl. Math. 68 (2015), 1683–1741.
- **[SOTA]** H. Dietert, D. Gérard-Varet. *Well-posedness of the Prandtl equations without any structural assumption.* Analysis & PDE 12 (2019), 1273–1297.
- **[SOTA]** D. Gérard-Varet, N. Masmoudi. *Well-posedness for the Prandtl system without analyticity or monotonicity.* Ann. Sci. Éc. Norm. Supér. 48 (2015), 1273–1325.
- **[SOTA]** Y. Maekawa. *On the inviscid limit problem of the vorticity equations for viscous incompressible flows in the half-plane.* Comm. Pure Appl. Math. 67 (2014), 1045–1128.
- **[SOTA]** E. Grenier, T. Nguyen. *$L^\infty$ instability of Prandtl layers.* Annals of PDE 5 (2019), Article 18.
- **[SOTA]** I. Kukavica, V. Vicol, F. Wang. *The van Dommelen and Shen singularity in the Prandtl equations.* Advances in Mathematics 307 (2017), 288–311.
- **[Key]** C.-J. Liu, Y.-G. Wang, T. Yang. *On the ill-posedness of the Prandtl equations in three-dimensional space.* Arch. Ration. Mech. Anal. 220 (2016), 83–108.
- **[Survey]** D. Gérard-Varet, E. Dormy, M. Prestipino / D. Gérard-Varet, *Recent progress on the Prandtl equations*, and E. Grenier, *Boundary layers*, in: Handbook of Mathematical Fluid Dynamics, Vol. 3, North-Holland, 2004.
- **[Survey]** Y. Maekawa, A. Mazzucato. *The inviscid limit and boundary layers for Navier–Stokes flows.* In: Handbook of Mathematical Analysis in Mechanics of Viscous Fluids, Springer, 2018.

## 10. Worked Example / Concrete Special Case

**Blasius flow: the one case where Prandtl is completely solved.**

Take steady 2D flow over a half-infinite flat plate, $U(x)\equiv U_\infty$ constant so $\partial_x p^E=0$. The steady Prandtl system is
$$u\,\partial_x u + v\,\partial_Y u = \partial_Y^2 u,\qquad \partial_x u + \partial_Y v=0,\qquad u|_{Y=0}=v|_{Y=0}=0,\ u|_{Y\to\infty}=U_\infty .$$
The system is invariant under $x\mapsto\lambda^2 x$, $Y\mapsto\lambda Y$, $u\mapsto u$, $v\mapsto \lambda^{-1}v$. Seek a self-similar solution with
$$\eta = \frac{Y}{\sqrt{x/U_\infty}},\qquad \psi = \sqrt{U_\infty x}\;f(\eta),\qquad u=\partial_Y\psi = U_\infty f'(\eta),\quad v=-\partial_x\psi=\tfrac12\sqrt{\tfrac{U_\infty}{x}}\,(\eta f'-f).$$
Substituting: $u\partial_x u = -\tfrac{U_\infty^2}{2x}\eta f'f''$, $v\partial_Y u = \tfrac{U_\infty^2}{2x}(\eta f'-f)f''$, $\partial_Y^2 u = \tfrac{U_\infty^2}{x} f'''$. Summing, the $\eta f' f''$ terms cancel and one gets the **Blasius ODE**
$$f''' + \tfrac12 f f'' = 0,\qquad f(0)=f'(0)=0,\ \ f'(\infty)=1 .$$
This has a unique solution (Weyl, 1942) with $f''(0)=0.4696$ (in the $\nu=1$, $U_\infty=1$ normalization above; the classical value $0.332$ corresponds to $\eta=Y\sqrt{U_\infty/(2\nu x)}$-type scalings). Consequences:

- Wall shear: $\partial_Y u|_{Y=0} = U_\infty^{3/2} x^{-1/2} f''(0) > 0$ for all $x>0$ — the profile is **monotone**, so Oleinik/Masmoudi–Wong theory applies and no separation occurs. This is the favourable/zero pressure gradient case.
- Displacement thickness $\delta^*=\int_0^\infty(1-f')\,d\eta\cdot\sqrt{x/U_\infty}\approx 1.72\sqrt{\nu x/U_\infty}$ after restoring $\nu$.

**Where it breaks.** Replace $U(x)=U_\infty$ by a decelerating outer flow, e.g. Falkner–Skan $U(x)=U_\infty x^{m}$ with $m<0$: the similarity ODE becomes $f'''+\tfrac{m+1}{2}ff''+m(1-f'^2)=0$, and for $m<m_c\approx-0.0904$ no solution with $f''(0)>0$ exists. The wall shear hits zero: monotonicity fails, the Crocco transform degenerates, and **every** current well-posedness theorem loses its hypothesis. Unsteadily, van Dommelen–Shen's impulsively started cylinder ($U(x)=2U_\infty\sin x$) produces exactly this: $\partial_x u$ blows up at $t^*\approx1.5$ while $u$ itself stays bounded — a Lagrangian singularity, rigorously constructed in Kukavica–Vicol–Wang (2017). The open problem is precisely to describe the Navier–Stokes solution near such a point as $\nu\to 0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*