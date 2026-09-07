---
id: 06-pdes/nonlinear-schrodinger-3d-regularity
title: "Nonlinear Schrodinger 3D Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Regularity for the Energy-Supercritical Nonlinear Schrödinger Equation in Three Dimensions

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/nonlinear-schrodinger-3d-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the semilinear nonlinear Schrödinger equation (NLS) on $\mathbb{R}^{1+3}$,

$$i\partial_t u + \Delta u = \mu\,|u|^{p-1}u,\qquad u(0,\cdot)=u_0,\qquad u:\mathbb{R}\times\mathbb{R}^3\to\mathbb{C},$$

with $\mu=+1$ (defocusing) or $\mu=-1$ (focusing) and $p>1$.

**Main open question.** For the *defocusing* equation with $p>5$ (energy-supercritical), does every Schwartz initial datum $u_0\in\mathcal{S}(\mathbb{R}^3)$ generate a solution that is smooth and global in time, with $\|u(t)\|_{\dot H^{s_c}}$ bounded and scattering to a free solution as $t\to\pm\infty$?

A complete resolution is either (a) a proof of global existence, uniqueness, persistence of regularity and scattering for all such data, or (b) construction of a datum whose maximal solution has $\lim_{t\to T^-}\|u(t)\|_{\dot H^{s_c}}=\infty$ for some $T<\infty$ (or $\|u(t)\|_{\dot H^{s_c}}$ unbounded in infinite time). Partial credit results — conditional theorems assuming an a priori $\dot H^{s_c}$ bound — do not resolve the question.

Two companion open problems live in the same file and are treated below: the *large-data focusing* energy-critical problem ($p=5$, data above the ground-state threshold), and the *unconditional* description of dynamics (soliton resolution) for focusing 3D NLS.

## 2. Mathematical Foundations

**Conserved quantities.** For sufficiently regular decaying solutions:

$$M(u)=\int_{\mathbb{R}^3}|u|^2\,dx,\qquad E(u)=\frac12\int|\nabla u|^2\,dx+\frac{\mu}{p+1}\int|u|^{p+1}\,dx,$$

together with momentum $P(u)=\operatorname{Im}\int\bar u\nabla u$.

**Scaling.** If $u$ solves the equation, so does

$$u_\lambda(t,x)=\lambda^{\frac{2}{p-1}}\,u(\lambda^2 t,\lambda x),\qquad \lambda>0,$$

and $\|u_\lambda(0)\|_{\dot H^s}=\lambda^{\,s-s_c}\|u_0\|_{\dot H^s}$ with **critical Sobolev exponent**

$$s_c=\frac{d}{2}-\frac{2}{p-1}=\frac32-\frac{2}{p-1}\quad (d=3).$$

Thus $s_c=0$ (mass-critical) at $p=7/3$, $s_c=1$ (energy-critical) at $p=5$, and $s_c>1$ (energy-supercritical) for $p>5$. Since $M$ scales as $\lambda^{-2s_c}$ and $E$ as $\lambda^{2(1-s_c)}$, for $p>5$ **no conserved quantity is scale-invariant or supercritical-coercive**: both are powerless against concentration.

**Local theory.** Strichartz estimates for $e^{it\Delta}$ (Strichartz 1977; Ginibre–Velo; Keel–Tao 1998) state that for admissible pairs $(q,r)$ with $\tfrac2q+\tfrac3r=\tfrac32$, $2\le q\le\infty$,

$$\|e^{it\Delta}f\|_{L^q_tL^r_x}\lesssim\|f\|_{L^2},\qquad \Big\|\int_0^t e^{i(t-s)\Delta}F(s)\,ds\Big\|_{L^q_tL^r_x}\lesssim\|F\|_{L^{\tilde q'}_tL^{\tilde r'}_x}.$$

Contraction in $\dot H^{s_c}$-critical Strichartz spaces gives local well-posedness for $u_0\in\dot H^{s_c}\cap\dot H^1$ with existence time depending on the *profile* of $u_0$, not just its norm (Cazenave–Weissler 1990). Consequently the standard blow-up criterion is: the solution extends as long as $\|u(t)\|_{\dot H^{s_c}}$ stays finite.

**Virial / Morawetz.** With $V(t)=\int|x|^2|u|^2dx$,

$$V''(t)=8\int|\nabla u|^2dx-\frac{4d(p-1)}{p+1}\,\mu'\int|u|^{p+1}dx,$$

($\mu'=-\mu$; see §10). The interaction Morawetz estimate of Colliander–Keel–Staffilani–Takaoka–Tao gives, for defocusing 3D NLS,

$$\int_I\!\!\int_{\mathbb{R}^3}|u(t,x)|^4\,dx\,dt\lesssim \|u_0\|_{L^2}^2\,\|u_0\|_{\dot H^{1/2}}^2 ,$$

a *subcritical* spacetime bound once $p>3$.

## 3. History & State of the Art

- **1970s–80s.** Ginibre–Velo (*J. Funct. Anal.* 32, 1979) establish global well-posedness in $H^1$ for defocusing energy-subcritical NLS ($1<p<5$ in 3D) via the conservation of $E$ and $M$. Glassey (1977) proves finite-time blow-up for focusing NLS with negative energy and finite variance.
- **1985–1990.** Cazenave–Weissler set up the critical local theory; Kato develops the $H^s$ framework.
- **1999.** Bourgain (*JAMS* 12) proves global well-posedness and scattering for the defocusing **energy-critical** quintic NLS in $\mathbb{R}^3$ for *radial* data, via induction on energy plus localized Morawetz. Grillakis (2000) gives an independent regularity proof in the radial case.
- **2008.** Colliander, Keel, Staffilani, Takaoka, Tao (*Annals of Math.* 167, 767–865) remove radiality: defocusing quintic NLS in $\mathbb{R}^3$ is globally well-posed and scatters for all $H^1$ data. Ryckman–Vişan ($d=4$, 2007) and Vişan ($d\ge5$, *Duke* 2007) complete other dimensions.
- **2006.** Kenig–Merle (*Invent. Math.* 166) introduce the concentration-compactness/rigidity ("road map") method and settle the **focusing** energy-critical problem for radial data below the ground state $W(x)=(1+|x|^2/3)^{-1/2}$.
- **2012.** Dodson (*JAMS* 25) proves global well-posedness and scattering for the defocusing **mass-critical** NLS in $d\ge3$, hence $p=7/3$ in 3D.
- **2022.** Merle, Raphaël, Rodnianski, Szeftel (*Invent. Math.* 227, 247–413) construct **finite-time blow-up for defocusing energy-supercritical NLS** — but only in dimensions $d\ge5$ and for a restricted (non-explicit, large) range of $p$, by importing self-similar implosion profiles from compressible Euler (*Annals* 196, 2022).

Dimension 3, the physically central case, is untouched by both the positive and the negative theory in the supercritical regime.

## 4. Partial Results / Verified Cases

| Regime (3D) | Status |
|---|---|
| Defocusing $1<p<7/3$ ($s_c<0$), $L^2$ data | GWP; scattering known for $p>7/3$ only |
| Defocusing $p=7/3$ (mass-critical) | GWP + scattering, all $L^2$ data — Dodson 2012 |
| Defocusing $7/3<p<5$, $H^1$ data | GWP (Ginibre–Velo 1979); scattering — Ginibre–Velo 1985, Nakanishi |
| Defocusing cubic $p=3$, critical data $u_0\in\dot H^{1/2}$ | GWP + scattering — Dodson (2021), conditional-free |
| Defocusing $p=5$ (energy-critical), $H^1$ | GWP + scattering — CKSTT 2008 |
| Focusing $p=5$, radial, $E(u_0)<E(W)$, $\|\nabla u_0\|_2<\|\nabla W\|_2$ | GWP + scattering — Kenig–Merle 2006 |
| Focusing $p=3$, $M(u_0)E(u_0)<M(Q)E(Q)$ | Scattering / blow-up dichotomy — Holmer–Roudenko (*CMP* 282, 2008), Duyckaerts–Holmer–Roudenko (2008) |
| Focusing $p=7/3$, $\|u_0\|_2<\|Q\|_2$ | GWP + scattering — Dodson 2015 |
| Focusing $p=7/3$, slightly supercritical mass | log-log blow-up rate — Merle–Raphaël (*Annals* 161, 2005) |
| Defocusing $p>5$, **assuming** $\sup_t\|u(t)\|_{\dot H^{s_c}}<\infty$ | Scattering — Killip–Vişan (*Comm. PDE* 35, 2010), and radial refinements |
| Defocusing supercritical, $d\ge5$, large $p$ | Blow-up exists — Merle–Raphaël–Rodnianski–Szeftel 2022 |

## 5. Principal Obstacles

- **Supercriticality of conserved quantities.** For $p>5$, $E$ and $M$ scale with negative powers relative to $\dot H^{s_c}$. Rescaling data to small amplitude and large frequency drives conserved quantities to zero while $\dot H^{s_c}$ stays fixed. Every global-in-time argument that runs on a coercive conservation law therefore fails at the first step.
- **No monotone quantity at critical scaling.** The interaction Morawetz bound controls $\|u\|_{L^4_{t,x}}$, which is $\dot H^{1/2}$-critical; for $p>5$ this is far below $s_c$ and gives no control of concentration.
- **Concentration-compactness gives only a conditional reduction.** The Kenig–Merle scheme reduces failure of scattering to an almost-periodic "minimal blow-up solution", and Killip–Vişan then exclude such solutions — *but only after assuming the a priori $\dot H^{s_c}$ bound*. Removing that assumption is exactly the open problem, not a technical step.
- **Norm inflation below $s_c$.** Christ–Colliander–Tao (2003) show ill-posedness in $H^s$ for $s<s_c$: instantaneous norm inflation. So there is no room to work in a weaker space and bootstrap upward.
- **Dimension 3 blocks the implosion construction.** The MRRS blow-up uses self-similar imploding solutions of compressible Euler with adiabatic index tied to $p$ and $d$; the required smooth self-similar profiles are constructed for $d\ge5$ (and the analogous fluid statements for $d=2,3$ need different profile ranges). Transferring the mechanism to $d=3$ requires new ODE/profile analysis and a WKB parameter regime that has not been made to work.
- **Focusing large data.** Above the ground-state threshold, Duyckaerts–Merle-type classification handles only energies slightly above $E(W)$; the general dynamics (multi-bubble, resolution into solitons plus radiation) resist because compactness is lost to multiple concurrent scales.

## 6. The Gap

Everything proven at $p\ge5$ is either (i) at the exact critical exponent, where energy conservation is *scale-invariant* and supplies the coercivity, or (ii) supercritical but **conditional on** $\sup_{t\in I}\|u(t)\|_{\dot H^{s_c}}<\infty$.

The gap is the single implication

$$\text{(smooth, decaying }u_0) \;\Longrightarrow\; \sup_{t\in I_{\max}}\|u(t)\|_{\dot H^{s_c}}<\infty .$$

Nothing in the current toolbox produces a scale-invariant a priori bound. Crossing the gap requires either a new monotone functional invariant under the scaling $u\mapsto\lambda^{2/(p-1)}u(\lambda^2t,\lambda x)$, or a 3D construction of a genuinely blowing-up defocusing solution. Both directions are open; the MRRS theorem shows the second is not vacuous in high dimension, which shifts the prior toward blow-up rather than regularity.

## 7. Current Research (as of June 2026)

- **Implosion transfer to low dimension.** Groups around Merle (IHES/CY Cergy), Raphaël (Cambridge), Rodnianski (Princeton) and Szeftel (Sorbonne) are pushing the self-similar Euler machinery toward $d=3,4$; the obstruction is the existence and smoothness of the required nonlinear profile in the relevant $(d,\gamma)$ window. *(frontier — verify)*
- **Numerical searches for supercritical blow-up.** Spectral simulations of defocusing 3D NLS with $p=7,9$ report no concentration up to resolved times — consistent with either regularity or a very narrow unstable blow-up manifold. *(frontier — verify)*
- **Long-time dynamics / soliton resolution.** Duyckaerts–Kenig–Martel–Merle's channel-of-energy and modulation methods, proven for energy-critical wave, are being adapted to NLS; full resolution for 3D focusing NLS remains open. *(frontier — verify)*
- **Growth of Sobolev norms and weak turbulence.** Colliander–Keel–Staffilani–Takaoka–Tao (*Invent. Math.* 181, 2010) on $\mathbb{T}^2$, and subsequent work by Hani, Pausader, Tzvetkov, Visciglia, and Guardia–Kaloshin, probe cascade mechanisms that are the natural candidate route to loss of regularity.
- **Probabilistic well-posedness.** Bourgain-style randomized data (Burq–Tzvetkov; Bényi–Oh–Pocovnicu; Dodson–Lührmann–Mendelson) yields almost-sure global results for supercritical-*data* problems in 3D, but does not touch the deterministic supercritical-*equation* question.

## 8. Future Work

- Construct an exactly self-similar or discretely self-similar blow-up profile for defocusing 3D NLS with large $p$, following the MRRS route but with a 3D-admissible Euler profile.
- Find a scaling-critical monotonicity formula. Candidates suggested in the literature: higher-order interaction Morawetz identities with critical weights, or virial identities localized at the self-similar scale.
- Weaken the Killip–Vişan hypothesis from a uniform $\dot H^{s_c}$ bound to a spacetime-integrated or frequency-localized surrogate that conservation laws can actually deliver.
- Settle focusing energy-critical 3D dynamics at and above the threshold $E(u_0)=E(W)$, extending Duyckaerts–Merle beyond the near-threshold regime.
- Clarify the relationship to Navier–Stokes: both are supercritical scalar-scaling problems with a subcritical coercive quantity; a transferable "critical bound implies regularity" mechanism would be a major structural advance.

## 9. Key References

- **[Foundational]** J. Ginibre, G. Velo. *On a class of nonlinear Schrödinger equations. I. The Cauchy problem, general case.* Journal of Functional Analysis, 32 (1979), 1–32.
- **[Foundational]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes in Mathematics 10, AMS, 2003.
- **[Foundational]** M. Keel, T. Tao. *Endpoint Strichartz estimates.* American Journal of Mathematics, 120 (1998), 955–980.
- **[Foundational]** J. Bourgain. *Global wellposedness of defocusing critical nonlinear Schrödinger equation in the radial case.* Journal of the AMS, 12 (1999), 145–171.
- **[SOTA]** J. Colliander, M. Keel, G. Staffilani, H. Takaoka, T. Tao. *Global well-posedness and scattering for the energy-critical nonlinear Schrödinger equation in $\mathbb{R}^3$.* Annals of Mathematics, 167 (2008), 767–865.
- **[SOTA]** C. Kenig, F. Merle. *Global well-posedness, scattering and blow-up for the energy-critical, focusing, non-linear Schrödinger equation in the radial case.* Inventiones Mathematicae, 166 (2006), 645–675.
- **[SOTA]** B. Dodson. *Global well-posedness and scattering for the defocusing, $L^2$-critical nonlinear Schrödinger equation when $d\ge3$.* Journal of the AMS, 25 (2012), 429–463.
- **[SOTA]** R. Killip, M. Vişan. *Energy-supercritical NLS: critical $\dot H^s$-bounds imply scattering.* Communications in PDE, 35 (2010), 945–987.
- **[SOTA / Recent]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On blow up for the energy super critical defocusing nonlinear Schrödinger equations.* Inventiones Mathematicae, 227 (2022), 247–413.
- **[SOTA / Recent]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On the implosion of a compressible fluid II: singularity formation.* Annals of Mathematics, 196 (2022), 779–889.
- **[Foundational]** F. Merle, P. Raphaël. *The blow-up dynamic and upper bound on the blow-up rate for critical NLS.* Annals of Mathematics, 161 (2005), 157–222.
- **[Survey]** R. Killip, M. Vişan. *Nonlinear Schrödinger equations at critical regularity.* In *Evolution Equations*, Clay Mathematics Proceedings 17, AMS, 2013, 325–437.
- **[Survey]** T. Tao. *Nonlinear Dispersive Equations: Local and Global Analysis.* CBMS Regional Conference Series 106, AMS, 2006.
- **[Ill-posedness]** M. Christ, J. Colliander, T. Tao. *Ill-posedness for nonlinear Schrödinger and wave equations.* arXiv:math/0311048, 2003.
- **[Focusing subcritical]** J. Holmer, S. Roudenko. *A sharp condition for scattering of the radial 3D cubic nonlinear Schrödinger equation.* Communications in Mathematical Physics, 282 (2008), 435–467.

## 10. Worked Example / Concrete Special Case

**(a) Virial identity in 3D, exactly computed.** Let $u$ solve $i\partial_t u+\Delta u+|u|^{p-1}u=0$ (focusing) with $xu_0\in L^2$, and set $V(t)=\int|x|^2|u|^2dx$. Differentiating twice and using the equation,

$$V'(t)=4\operatorname{Im}\int \bar u\,(x\cdot\nabla u)\,dx,\qquad V''(t)=8\int|\nabla u|^2dx-\frac{4d(p-1)}{p+1}\int|u|^{p+1}dx .$$

Take $d=3$, $p=3$ (focusing cubic). Then $\frac{4\cdot3\cdot2}{4}=6$ and

$$V''(t)=8\int|\nabla u|^2-6\int|u|^4 .$$

The energy is $E=\frac12\int|\nabla u|^2-\frac14\int|u|^4$, so $16E=8\int|\nabla u|^2-4\int|u|^4$ and

$$V''(t)=16E(u_0)-2\int|u|^4\;\le\;16E(u_0).$$

If $E(u_0)<0$ then $V(t)\le V(0)+V'(0)t+8E(u_0)t^2\to-\infty$, contradicting $V\ge0$. Hence the maximal existence time is finite: **Glassey blow-up**. This is the concrete sense in which the focusing problem is understood at $p=3$.

**(b) Why the same computation says nothing for defocusing $p=7$.** Now $\mu=+1$, $d=3$, $p=7$, so $\frac{4\cdot3\cdot6}{8}=9$ and

$$V''(t)=8\int|\nabla u|^2+9\int|u|^{8}\;>\;0 .$$

Positivity gives dispersion in an averaged sense but no bound on any critical norm. Compute the scaling exponents: $s_c=\frac32-\frac26=\frac76>1$. Under $u_\lambda(t,x)=\lambda^{1/3}u(\lambda^2t,\lambda x)$,

$$M(u_\lambda)=\lambda^{-7/3}M(u),\qquad E(u_\lambda)=\lambda^{-1/3}E(u),\qquad \|u_\lambda(0)\|_{\dot H^{7/6}}=\|u_0\|_{\dot H^{7/6}} .$$

Send $\lambda\to0$: the datum spreads to large scales, $M$ and $E$ blow up; send $\lambda\to\infty$: the datum concentrates and $M,E\to0$ while the critical norm is unchanged. So a hypothetical concentrating solution can carry arbitrarily small mass and energy. Every conserved quantity is blind to it. That is the whole difficulty of §6, visible in three lines of arithmetic.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*