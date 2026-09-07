---
id: 06-pdes/kelvin-helmholtz-ill-posedness
title: "Kelvin-Helmholtz Ill Posedness"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kelvin–Helmholtz Ill-Posedness for Vortex Sheets

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kelvin-helmholtz-ill-posedness` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

A **vortex sheet** is a solution of the incompressible Euler equations whose vorticity is a measure concentrated on a curve, across which the tangential velocity jumps. The Kelvin–Helmholtz problem asks for the evolution of such a sheet.

**Core claim (established).** The initial-value problem for a two-dimensional vortex sheet without surface tension is *Hadamard ill-posed* in every Sobolev class $H^s$: for each $s$ and each $T>0$ the solution map, where defined, is not continuous from $H^s$ into any $H^{s'}$ neighbourhood, and generic $H^s$ data admits no solution on $[0,T]$. The problem is *well-posed only in classes of analytic data*, where solutions are unique and — by the analyticity theorem — every $H^s$-regular solution of the Birkhoff–Rott equation is forced to be analytic.

**What remains open.** Three questions, all still unresolved:

1. **Singularity formation.** Moore's asymptotics predict a finite-time curvature (cusp) singularity from analytic data. A rigorous proof for general analytic data is open.
2. **Continuation past the singularity.** Which weak solution of Euler, if any, is the physical continuation? Infinitely many admissible (energy-dissipating) weak solutions exist for the same flat-sheet data.
3. **Selection criterion.** Find an admissibility condition singling out one continuation, and prove it is the zero-viscosity / zero-surface-tension limit.

A complete resolution means: a proof of finite-time singularity, a selection principle, and a convergence theorem identifying the selected solution as a vanishing-regularization limit.

## 2. Mathematical Foundations

Let $u:\mathbb{R}^2\times[0,T)\to\mathbb{R}^2$ solve
$$\partial_t u + (u\cdot\nabla)u + \nabla p = 0,\qquad \nabla\cdot u = 0 .$$
Vortex-sheet data: $\omega_0 = \nabla^\perp\!\cdot u_0 = \gamma\,\delta_{\Sigma_0}$, a measure on a curve $\Sigma_0$ with sheet strength $\gamma$. Then $u_0 \in L^2_{\mathrm{loc}}$, $\omega_0 \in \mathcal{M}(\mathbb{R}^2) \cap H^{-1}_{\mathrm{loc}}$.

**Birkhoff–Rott equation.** Parametrize the sheet by circulation $\Gamma$, $z(\Gamma,t)\in\mathbb{C}$. The sheet moves with the mean of the two one-sided velocities:
$$\partial_t \overline{z}(\Gamma,t) \;=\; \frac{1}{2\pi i}\,\mathrm{p.v.}\!\int \frac{d\Gamma'}{z(\Gamma,t)-z(\Gamma',t)} .$$
This is a nonlocal, quadratically nonlinear equation; the principal part is the Hilbert transform $H$, whose symbol $-i\,\mathrm{sgn}(k)$ is of order $0$ but appears in a system whose linearization has *elliptic* character in $(x,t)$.

**Linearization about the flat sheet** $z=\Gamma$. Writing $z=\Gamma+s(\Gamma,t)$ and Fourier-transforming in $\Gamma$,
$$\partial_t \overline{\hat s}_k = \tfrac{|k|}{2}\,\hat s_k \quad\Longrightarrow\quad \partial_t^2 \hat s_k = \tfrac{k^2}{4}\,\hat s_k,\qquad \hat s_k(t)\sim e^{|k|t/2}.$$
The growth rate is **linear in frequency**, with no upper bound: this is the analytic signature of ill-posedness. Equivalently, the linearized operator is $\partial_t^2 - \tfrac14|D|^2$ up to sign — a Laplace-type (elliptic) operator, so the Cauchy problem is a backward-heat-type problem.

**Two-fluid dispersion relation.** With densities $\rho_1$ (upper), $\rho_2$ (lower), velocities $U_1,U_2$, gravity $g$, surface tension $\sigma$, the classical Kelvin criterion gives instability at wavenumber $k$ iff
$$\frac{\rho_1\rho_2}{(\rho_1+\rho_2)^2}\,(U_1-U_2)^2 |k| \;>\; \frac{(\rho_2-\rho_1)g + \sigma k^2}{\rho_1+\rho_2}.$$
Surface tension supplies an $O(k^2)$ restoring term that defeats the $O(|k|)$ growth at high $k$ — the mechanism behind all regularized well-posedness results.

**Function-space setting.** Well-posedness holds in the analytic scale $\{X_\rho\}$, $\|f\|_{X_\rho}=\sum_k |\hat f_k| e^{\rho|k|}$, via the abstract Cauchy–Kovalevskaya theorem (Nirenberg–Nishida), with radius $\rho(t)=\rho_0-Ct$.

## 3. History & State of the Art (SOTA)

- **1868/1871.** Helmholtz introduces discontinuous fluid motions; Kelvin derives the dispersion relation and the instability criterion.
- **1932.** Birkhoff and, independently, Rott (1956) derive the integro-differential evolution equation now bearing their names.
- **1979.** Moore's matched asymptotics predict a finite-time $3/2$-power curvature singularity from analytic periodic data, at a time $t_c$ exponentially close to the analyticity radius.
- **1981.** Sulem–Sulem–Bardos–Frisch prove short-time existence and uniqueness for analytic data (2D and 3D), the first rigorous result.
- **1986.** Krasny's vortex-blob desingularization computes roll-up past $t_c$, showing spiral formation and confirming that unregularized numerics are dominated by round-off amplified at rate $e^{|k|t/2}$.
- **1988–89.** Ebin proves ill-posedness of the Helmholtz (and Rayleigh–Taylor) problems; Duchon–Robert construct global-in-time analytic solutions for small, near-flat analytic data; Caflisch–Orellana construct explicit exact solutions exhibiting both singularity formation and $H^s$ ill-posedness.
- **1991.** Delort proves global existence of weak solutions for vortex-sheet data of *distinguished sign* — but with no uniqueness.
- **2002/2006.** Lebeau, then Wu, establish the definitive regularity statement: any sufficiently regular (chord-arc, $H^s$) solution of Birkhoff–Rott is analytic in the space variable away from singular points. Ill-posedness in Sobolev spaces is thereby complete — Sobolev solutions cannot exist unless they were analytic all along.
- **2011–2023.** Székelyhidi Jr. applies convex integration to flat-sheet data, producing infinitely many admissible weak Euler solutions; Mengual–Székelyhidi Jr. extend this to general (non-flat) vortex sheets with *dissipating* energy, and identify a subsolution whose mixing zone grows at the linear Kelvin–Helmholtz rate.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| 2D/3D analytic data | Local existence + uniqueness, $t < \rho_0/C$ | Sulem–Sulem–Bardos–Frisch 1981 |
| 2D analytic, small near-flat | Global analytic solution | Duchon–Robert 1988 |
| 2D, $H^s$ chord-arc solutions | Forced analyticity ⇒ no genuine $H^s$ theory | Lebeau 2002; Wu 2006 |
| Exact singular solutions | Explicit $H^s$ ill-posedness, curvature blow-up | Caflisch–Orellana 1989 |
| Surface tension $\sigma>0$, 2D | Local well-posedness in $H^s$, $s\ge 3$ | Ambrose 2003 |
| Surface tension $\sigma>0$, 3D | Local well-posedness | Ambrose–Masmoudi 2007 |
| Compressible 2D, relative Mach $M>\sqrt2$ | Nonlinear local well-posedness (weakly stable, loss of derivatives) | Coulombel–Secchi 2008 |
| Compressible, $M<\sqrt2$; all 3D compressible sheets | Violently unstable (Miles 1958; Fejer–Miles) | — |
| MHD current-vortex sheets, Syrovatskij condition | A priori estimates, weak stability | Coulombel–Morando–Secchi–Trakhinin 2012 |
| Vorticity of distinguished sign | Global weak solutions exist (non-unique) | Delort 1991 |
| Flat sheet, weak solutions | Infinitely many admissible solutions | Székelyhidi 2011 |
| General vortex sheets | Infinitely many energy-dissipating solutions | Mengual–Székelyhidi 2023 |

Numerically: Krasny's blob regularization with $\delta \to 0$, and point-vortex computations at $N=2^{10}$–$2^{16}$ nodes, reproduce Moore's $t_c$ to three digits and exhibit self-similar spiral roll-up.

## 5. Principal Obstacles

- **Elliptic Cauchy problem.** The linearization is $\partial_t^2 - \tfrac14|D|^2$; the Cauchy problem for an elliptic operator has no energy estimate in any Sobolev norm. Every symmetrizer, para-differential or Nash–Moser scheme requires a *hyperbolic* or at worst weakly hyperbolic principal symbol. Here the symbol has genuinely complex characteristic roots at every $k\ne0$, so no loss-of-derivative bookkeeping can close.
- **No smoothing, no dispersion.** Unlike Prandtl (where a heat operator supplies parabolic smoothing in the normal variable) or water waves (where gravity/capillarity give dispersive decay), the unregularized vortex sheet has no dissipative or dispersive term at all. The frequency $|k|$ enters purely as a growth exponent.
- **Analyticity is a rigid trap.** Wu's and Lebeau's theorems mean one cannot even *hope* for a low-regularity solution theory: any candidate solution is instantly analytic, so the class of solvable data is a set of infinite codimension in $H^s$. There is no intermediate space (Gevrey $G^\alpha$, $\alpha>1$) known to be a genuinely larger well-posedness class.
- **Convex integration is too flexible.** The tool that *does* produce solutions past the singularity produces too many: the Tartar relaxation of the Euler differential inclusion at a shear interface has a large lamination-convex hull, so admissibility (energy dissipation) fails to cut the solution set down to a point. No known relaxed criterion (local energy inequality, entropy, maximal dissipation) is known to restore uniqueness.
- **Singular limits do not commute.** Vanishing viscosity, vanishing surface tension and vanishing blob-size regularizations are not known to have the same limit, and none is known to converge at all past $t_c$.

## 6. The Gap

Proven: (i) ill-posedness in $H^s$; (ii) well-posedness in analytic data up to time $t\sim\rho_0$; (iii) non-uniqueness of weak continuations. The gap is a **triple** of missing links.

1. Between "Moore predicts a $|\Gamma-\Gamma_c|^{3/2}$ cusp" and "a theorem that analytic data of arbitrary size develops a singularity in finite time." Caflisch–Orellana give *examples*; genericity is open.
2. Between "infinitely many dissipating weak solutions exist" and "one distinguished solution is the physical one." The precise missing object is an admissibility functional $\mathcal{A}$ on weak solutions with (a) $\mathcal{A}$-minimizers unique, (b) $\mathcal{A}$-minimizers = limits of Navier–Stokes as $\nu\to 0$.
3. Between the 2D theory and 3D: even the analytic local theory in 3D lacks a global or singularity-formation counterpart, and the geometry of 3D sheet folding is unmapped.

## 7. Current Research (as of June 2026)

- **Convex-integration school** (Leipzig / MPI MiS, Székelyhidi Jr. and collaborators; Mengual, Bern/Basel). Subsolution constructions with prescribed mixing-zone growth; current effort targets *sharp* turbulent-zone rates matched to the linear Kelvin–Helmholtz rate $|k|t/2$ and to Rayleigh–Taylor mixing-layer exponents. *(frontier — verify)* Recent work claims subsolutions with maximal dissipation among self-similar profiles.
- **Regularized-limit analysis** (Ambrose, Drexel; Cerfon/Hou-style numerics). Quantitative $\sigma\to0$ asymptotics for capillary vortex sheets, aiming to show that $\sigma$-solutions converge to Birkhoff–Rott before $t_c$ and to a specific mixing solution after.
- **Compressible / MHD stability** (Coulombel, Secchi, Trakhinin, Morando; Wang–Yu, Chinese groups). Extension of the $M>\sqrt2$ well-posedness to non-flat reference sheets, to relativistic MHD, and to elastic interfaces; a stabilizing tangential magnetic field is the model regularization.
- **Water-wave interfaces** (Lannes, Bordeaux; Bresch, Grenoble). The Lannes criterion quantifies how surface tension tames Kelvin–Helmholtz in a gravity-capillary two-fluid problem; ongoing work treats internal waves with density stratification.
- **Singularity formation** (self-similar / computer-assisted analysis groups following the Chen–Hou program). Attempts to transplant computer-assisted fixed-point proofs of blow-up to the Birkhoff–Rott cusp. *(frontier — verify)*

## 8. Future Work

- Prove a genericity theorem: analytic data in an open dense subset of $X_{\rho_0}$ develops a Moore cusp at some $t_c<\infty$, with $|z_{\Gamma\Gamma}|\to\infty$ at rate $(t_c-t)^{-1/2}$.
- Identify a Gevrey class $G^\alpha$, $1<\alpha<2$, with local well-posedness — or prove none exists, sharpening the analyticity trap.
- Establish a *selection theorem*: show that the $\sigma\to0$ limit of Ambrose's capillary solutions exists globally and coincides with a maximally dissipative subsolution.
- Settle whether zero-viscosity limits of 2D Navier–Stokes with vortex-sheet data are unique (an Euler-equations analogue of the Kato criterion).
- Develop 3D vortex-sheet theory beyond Sulem–Sulem–Bardos–Frisch: analytic global existence for small data, and a classification of 3D folding singularities.

## 9. Key References

- **[Foundational]** H. von Helmholtz. *Über discontinuirliche Flüssigkeitsbewegungen.* Monatsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin, 1868.
- **[Foundational]** W. Thomson (Lord Kelvin). *Hydrokinetic solutions and observations.* Philosophical Magazine, Series 4, 42:362–377, 1871.
- **[Foundational]** G. Birkhoff. *Helmholtz and Taylor instability.* Proceedings of Symposia in Applied Mathematics XIII, AMS, 1962, pp. 55–76.
- **[Foundational]** D. W. Moore. *The spontaneous appearance of a singularity in the shape of an evolving vortex sheet.* Proceedings of the Royal Society of London A, 365:105–119, 1979.
- **[Foundational]** C. Sulem, P.-L. Sulem, C. Bardos, U. Frisch. *Finite time analyticity for the two and three dimensional Kelvin–Helmholtz instability.* Communications in Mathematical Physics, 80:485–516, 1981.
- **[Foundational]** J. Duchon, R. Robert. *Global vortex sheet solutions of Euler equations in the plane.* Journal of Differential Equations, 73:215–224, 1988.
- **[Foundational]** R. E. Caflisch, O. F. Orellana. *Singular solutions and ill-posedness for the evolution of vortex sheets.* SIAM Journal on Mathematical Analysis, 20(2):293–307, 1989.
- **[Foundational]** D. G. Ebin. *Ill-posedness of the Rayleigh–Taylor and Helmholtz problems for incompressible fluids.* Communications in Partial Differential Equations, 13(10):1265–1295, 1988.
- **[Foundational]** J.-M. Delort. *Existence de nappes de tourbillon en dimension deux.* Journal of the American Mathematical Society, 4:553–586, 1991.
- **[SOTA]** G. Lebeau. *Régularité du problème de Kelvin–Helmholtz pour l'équation d'Euler 2d.* ESAIM: Control, Optimisation and Calculus of Variations, 8:801–825, 2002.
- **[SOTA]** S. Wu. *Mathematical analysis of vortex sheets.* Communications on Pure and Applied Mathematics, 59(8):1065–1206, 2006.
- **[SOTA]** D. M. Ambrose. *Well-posedness of vortex sheets with surface tension.* SIAM Journal on Mathematical Analysis, 35(1):211–244, 2003.
- **[SOTA]** D. M. Ambrose, N. Masmoudi. *Well-posedness of 3D vortex sheets with surface tension.* Communications in Mathematical Sciences, 5(2):391–430, 2007.
- **[SOTA]** J.-F. Coulombel, P. Secchi. *Nonlinear compressible vortex sheets in two space dimensions.* Annales Scientifiques de l'École Normale Supérieure, 41(1):85–139, 2008.
- **[SOTA]** L. Székelyhidi Jr. *Weak solutions to the equations of incompressible Euler with vortex sheet initial data.* Comptes Rendus Mathématique, 349(19–20):1063–1066, 2011.
- **[SOTA / Recent]** F. Mengual, L. Székelyhidi Jr. *Dissipative Euler flows for vortex sheet evolution.* Archive for Rational Mechanics and Analysis, 247, article 40, 2023.
- **[SOTA]** D. Lannes. *A stability criterion for two-fluid interfaces and applications.* Archive for Rational Mechanics and Analysis, 208:481–567, 2013.
- **[Computational]** R. Krasny. *Desingularization of periodic vortex sheet roll-up.* Journal of Computational Physics, 65(2):292–313, 1986.
- **[Survey]** A. J. Majda, A. L. Bertozzi. *Vorticity and Incompressible Flow.* Cambridge University Press, 2002 (Chapters 9–11).
- **[Survey]** J.-F. Coulombel, A. Morando, P. Secchi, P. Trakhinin. *A priori estimates for 3D incompressible current-vortex sheets.* Communications in Mathematical Physics, 311:247–275, 2012.

## 10. Worked Example / Concrete Special Case

**(a) Growth rate from the linearized Birkhoff–Rott equation.** Take the $2\pi$-periodic flat sheet $z(\Gamma,t)=\Gamma+s(\Gamma,t)$ with $|s|\ll1$. Substituting into Birkhoff–Rott and keeping first order:
$$\partial_t\overline{s}(\Gamma,t)=\frac{1}{2\pi i}\,\mathrm{p.v.}\!\int_0^{2\pi}\frac{s(\Gamma)-s(\Gamma')}{(\Gamma-\Gamma')^2}\,d\Gamma' \cdot(-1) = \tfrac{1}{2}\,H[\partial_\Gamma s],$$
whose Fourier symbol is $\tfrac12|k|$. With $s=\sum_k \hat s_k e^{ik\Gamma}$,
$$\partial_t \overline{\hat s_{-k}} = \tfrac{|k|}{2}\hat s_k,\qquad \partial_t^2 \hat s_k = \tfrac{k^2}{4}\hat s_k,\qquad \hat s_k(t)= A_k e^{|k|t/2}+B_ke^{-|k|t/2}.$$

**(b) Failure of continuous dependence.** Fix $s\ge0$ and $N>s$. Take data $s^{(k)}_0(\Gamma)=k^{-N}e^{ik\Gamma}$ with the growing mode excited. Then
$$\|s^{(k)}_0\|_{H^s}\approx k^{s-N}\xrightarrow[k\to\infty]{}0,\qquad \|s^{(k)}(t)\|_{H^s}\approx k^{s-N}e^{kt/2}\xrightarrow[k\to\infty]{}\infty \ \ \text{for every } t>0 .$$
Data converging to $0$ in $H^s$ produces solutions diverging in $H^s$ at every positive time: the solution map is nowhere continuous. Any $\sup_k$-bounded lifespan is impossible, so a genuine $H^s$ theory cannot exist. Analyticity rescues it: if $|\hat s_k(0)|\le Ce^{-\rho_0|k|}$, then $|\hat s_k(t)|\le Ce^{-(\rho_0-t/2)|k|}$, giving existence on $[0,2\rho_0)$ with shrinking radius $\rho(t)=\rho_0-t/2$.

**(c) The surface-tension threshold, computed.** Insert $\sigma>0$ into the Kelvin criterion with $U_1-U_2=U$, $\rho_1=\rho_2=\rho$ upper/lower reversed for gravity ($\Delta\rho=\rho_2-\rho_1>0$). Stability for all $k$ requires
$$\frac{\rho_1\rho_2}{\rho_1+\rho_2}U^2 \;\le\; \min_{k>0}\ \frac{\Delta\rho\, g + \sigma k^2}{|k|} .$$
The minimum is attained at $k_\ast=\sqrt{\Delta\rho\,g/\sigma}$ and equals $2\sqrt{\sigma\,\Delta\rho\,g}$. Hence
$$U_{\mathrm{crit}}^2 = \frac{2(\rho_1+\rho_2)}{\rho_1\rho_2}\sqrt{\sigma\,\Delta\rho\,g}.$$
For air over water ($\rho_1=1.2$, $\rho_2=1000$ kg m$^{-3}$, $\sigma=0.073$ N m$^{-1}$, $g=9.81$): $k_\ast\approx 366$ m$^{-1}$ (wavelength $\approx1.7$ cm) and $U_{\mathrm{crit}}\approx 6.6$ m s$^{-1}$. Below this wind speed the interface is linearly stable at *all* wavenumbers; the $O(k^2)$ capillary term has removed the unbounded $O(|k|)$ growth entirely, which is exactly the mechanism converting the ill-posed problem into Ambrose's $H^s$-well-posed one. Letting $\sigma\to0$ sends $U_{\mathrm{crit}}\to0$ and $k_\ast\to\infty$, recovering ill-posedness in the limit.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*