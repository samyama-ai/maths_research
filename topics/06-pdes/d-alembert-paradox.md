---
id: 06-pdes/d-alembert-paradox
title: "D Alembert Paradox"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# D'Alembert's Paradox

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/d-alembert-paradox` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Classical statement: a body moving at constant velocity through an incompressible, inviscid fluid in steady, irrotational, potential flow experiences **zero drag**. This contradicts every measurement ever made. D'Alembert (1752) derived it; the contradiction with observation is the paradox.

The physical resolution — viscosity, however small, creates boundary layers that separate and shed vorticity — is not in dispute. What remains open is its **mathematical** content, which is a family of precise PDE questions about the vanishing-viscosity limit:

**(P1) Inviscid limit with no-slip.** Let $u^\nu$ solve the incompressible Navier–Stokes equations in an exterior domain $\Omega = \mathbb{R}^d \setminus \bar{B}$ with $u^\nu|_{\partial B} = 0$ and $u^\nu \to U e_1$ at infinity. Does $u^\nu \to u^0$ (a solution of Euler) as $\nu \to 0$, and in what topology? A complete answer requires either a proof of convergence for a stated class of data/domains, or a counterexample with quantified failure.

**(P2) The drag law.** Is
$$\liminf_{\nu \to 0} D(\nu) > 0, \qquad D(\nu) = \int_{\partial B} \left(\rho\, \nu\, \partial_n u^\nu - p^\nu n\right)\cdot e_1 \, dS \,,$$
for a bluff body? Equivalently: does the drag coefficient $C_D = 2D/(\rho U^2 A)$ stay bounded away from $0$ as $\mathrm{Re} = UL/\nu \to \infty$? Empirically $C_D \approx 0.4$–$1.2$ for spheres and cylinders over $10^3 < \mathrm{Re} < 2\times 10^5$. No proof exists that $C_D \not\to 0$ for any bluff body.

**(P3) Anomalous dissipation.** Does the energy dissipation rate $\varepsilon^\nu = \nu \int |\nabla u^\nu|^2$ remain bounded below as $\nu \to 0$? (P2) and (P3) are the two halves of a rigorous "resolution": nonzero drag is exactly the failure of the Euler limit to be energy-conserving.

## 2. Mathematical Foundations

**Navier–Stokes, exterior domain.** For $\Omega\subset\mathbb{R}^d$ ($d=2,3$) the exterior of a smooth compact body,
$$\partial_t u^\nu + (u^\nu\cdot\nabla) u^\nu = -\nabla p^\nu + \nu \Delta u^\nu, \qquad \nabla\cdot u^\nu = 0,$$
with **no-slip** $u^\nu|_{\partial\Omega}=0$. The Euler equations are the formal $\nu=0$ case, but admit only the **no-penetration** condition $u^0\cdot n|_{\partial\Omega}=0$. The boundary-condition mismatch — one scalar constraint instead of $d$ — is the entire source of the difficulty: the limit is a **singular perturbation**, the highest-order term losing its coefficient.

**Potential flow and the paradox.** If the flow is steady, irrotational ($\omega=\nabla\times u=0$) and incompressible, then $u=\nabla\phi$ with $\Delta\phi=0$, $\partial_n\phi|_{\partial B}=0$, $\nabla\phi\to Ue_1$. Bernoulli gives $p = p_\infty + \tfrac12\rho(U^2 - |\nabla\phi|^2)$, and the force is
$$F = -\int_{\partial B} p\, n \, dS = 0 \quad (d=3).$$
The vanishing follows from the decay $\nabla\phi - Ue_1 = O(|x|^{-d})$ plus momentum-flux conservation on a large sphere. In $d=2$ simple connectivity fails and the harmonic conjugate admits a circulation $\Gamma$; drag still vanishes but lift is $-\rho U\Gamma$ (Kutta–Joukowski). So the paradox is a **theorem** about the potential model, not an error.

**Prandtl boundary layer.** Rescaling $y = Y/\sqrt{\nu}$ near a flat boundary gives, at leading order,
$$\partial_t u + u\partial_x u + v\partial_Y u = -\partial_x p^E + \partial_Y^2 u, \quad \partial_x u + \partial_Y v = 0, \quad u|_{Y=0}=v|_{Y=0}=0, \quad u|_{Y\to\infty}=u^E.$$
This system is degenerate (no $\partial_x^2$), and is where separation and the failure of the potential model live.

**Kato's criterion (1984).** Let $\Gamma_{c\nu} = \{x : \mathrm{dist}(x,\partial\Omega) < c\nu\}$. Then $u^\nu \to u^0$ in $L^\infty_t L^2_x$ on $[0,T]$ **iff**
$$\nu \int_0^T \!\!\int_{\Gamma_{c\nu}} |\nabla u^\nu|^2 \, dx\, dt \;\longrightarrow\; 0 .$$
The layer of width $O(\nu)$, not $O(\sqrt{\nu})$, is what matters. Equivalent reformulations in terms of $\nu\|\nabla u^\nu\|^2_{L^2(\Gamma_{c\nu})}$, the tangential velocity, or the vorticity flux were given by Kelliher (2007) and Constantin–Kukavica–Vicol.

**Onsager/anomalous dissipation.** A weak Euler solution in $L^3_t B^{s}_{3,\infty}$ with $s>1/3$ conserves energy (Constantin–E–Titi; Isett for the sharp converse). Nonzero drag as $\nu\to0$ forces the limit to be rougher than $1/3$ or to lose energy through the boundary.

## 3. History & State of the Art (SOTA)

- **1752** — Jean le Rond d'Alembert, *Essai d'une nouvelle théorie de la résistance des fluides*, Paris. States the zero-resistance result and calls it "a singular paradox which I leave to geometers to elucidate."
- **1768** — Euler notes the same for his own equations; the paradox is a standing indictment of theoretical hydrodynamics for 150 years ("fluids that flow but do not resist", in Birkhoff's phrasing).
- **1904** — Prandtl, *Über Flüssigkeitsbewegung bei sehr kleiner Reibung* (Heidelberg ICM). Introduces boundary layers and separation. This is the accepted **physical** resolution.
- **1950** — Birkhoff, *Hydrodynamics: A Study in Logic, Fact and Similitude*, isolates the unproved assumptions (existence, steadiness, symmetry, irrotationality) behind the classical derivation.
- **1965** — Finn constructs "physically reasonable" steady exterior Navier–Stokes solutions in 3D with $O(|x|^{-1})$ wake decay; drag is finite and well defined for each $\nu>0$, but no lower bound uniform in $\nu$.
- **1981** — Stewartson's SIAM Review survey, *D'Alembert's paradox*, is the standard account of triple-deck theory and the Goldstein separation singularity.
- **1984** — Kato's criterion turns (P1) into a sharp, checkable statement about an $O(\nu)$ boundary strip.
- **1998** — Sammartino–Caflisch: first rigorous inviscid limit with no-slip, for analytic data on a half-space.
- **2010** — Hoffman–Johnson, *Resolution of d'Alembert's paradox* (JMFM), argue from computation that the true mechanism is instability of potential flow at separation rather than a thin Prandtl layer. Widely cited, and contested.
- **2014–present** — Maekawa's Gevrey/vorticity-support results, Gérard-Varet–Dormy ill-posedness, Grenier–Nguyen instability, and Constantin–Vicol's criteria define the current frontier.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| Analytic initial data, half-space $\mathbb{R}^3_+$ | Inviscid limit holds on a time interval independent of $\nu$ (Sammartino–Caflisch 1998, I & II) |
| 2D half-plane, initial vorticity supported at distance $\delta>0$ from the wall | Limit holds for a $\nu$-independent time (Maekawa, CPAM 2014); extended to Gevrey-$\tfrac{1}{2}$ data by Gérard-Varet–Maekawa–Masmoudi |
| **Navier (slip) boundary conditions**, $u\cdot n=0$, $(\mathbb{S}u\, n)_\tau + \alpha u_\tau = 0$ | Inviscid limit **proved** in 2D and 3D (Iftimie–Sueur; Masmoudi–Rousset). The paradox's mathematical difficulty is specific to no-slip. |
| Symmetric/plane-parallel and circularly symmetric flows | Limit holds (Mazzucato–Taylor; Lopes Filho–Mazzucato–Nussenzveig Lopes) — but these geometries **suppress** separation, so drag genuinely vanishes there |
| Steady exterior NS, $d=3$, small $U/\nu$ | Existence, uniqueness, asymptotics, finite drag (Finn 1965; Galdi 2011). Drag $\to 0$ linearly in the Stokes regime, as it should |
| $d=2$ steady exterior, small data | **Stokes paradox**: no decaying solution of the linearized problem; resolved by Oseen matching — a distinct pathology of the same family |
| Kato-type criteria | Inviscid limit $\iff$ vanishing dissipation in $\Gamma_{c\nu}$ (Kato 1984); several equivalent conditions (Kelliher 2007; Constantin–Kukavica–Vicol 2015) |

## 5. Principal Obstacles

- **Singular perturbation with lost boundary conditions.** Energy estimates give $\|u^\nu\|_{L^2}$ bounds but no control of $\nabla u^\nu$ at the wall uniformly in $\nu$; the standard $H^s$ machinery for Euler does not survive the mismatch.
- **Prandtl is ill-posed in Sobolev spaces.** Gérard-Varet–Dormy (JAMS 2010) prove linear ill-posedness around non-monotone shear profiles: the growth rate of the mode with tangential frequency $k$ is $\sim \sqrt{|k|}$, so no $H^s$-to-$H^{s'}$ estimate can hold. Well-posedness requires either monotone profiles (Oleinik; Alexandre–Wang–Xu–Yang; Masmoudi–Wong) or analytic/Gevrey regularity. Hence the natural asymptotic expansion cannot be justified in the very regime — separation — that produces drag.
- **Boundary-layer expansions fail even when Prandtl is solvable.** Grenier (CPAM 2000) shows the expansion $u^\nu \approx u^E + u^P$ is nonlinearly unstable: sublayer instabilities of size $\nu^{1/4}$ amplify to $O(1)$, invalidating the ansatz.
- **Goldstein singularity.** At separation the steady Prandtl solution develops a square-root singularity in finite $x$ (van Dommelen–Shen blow-up in the unsteady case, proved by Kukavica–Vicol–Wang 2023 for analytic data). The model destroys itself exactly where drag is created.
- **No lower-bound technology for dissipation.** Nothing in the Navier–Stokes toolkit produces a *lower* bound on $\nu\int|\nabla u^\nu|^2$; all a priori estimates are upper bounds. Proving (P2) means proving that a quantity we can only bound above is bounded below.
- **Turbulence and 3D regularity.** For $\mathrm{Re}\sim 10^5$ the flow is unsteady and turbulent; the wake is not a small perturbation of anything. Nonuniqueness of Leray–Hopf-class weak solutions (Buckmaster–Vicol, Annals 2019, for fractional dissipation; convex-integration constructions more generally) means "the" solution whose drag one computes may not be canonically defined.

## 6. The Gap

Proven: the inviscid limit **with slip**, and with no-slip under analyticity, Gevrey regularity, vorticity separated from the wall, or symmetry — all conditions that either remove the boundary layer's tangential-shear singularity or preclude separation.

Wanted: a statement for **finite-regularity data on a bluff body**, where separation happens. The precise missing step, in Kato's language, is a **uniform lower bound**
$$\liminf_{\nu\to 0} \; \nu \int_0^T\!\!\int_{\Gamma_{c\nu}} |\nabla u^\nu|^2 \, dx \, dt \; \geq \; c(B,U) > 0$$
for a sphere or cylinder in uniform flow. Kato's theorem already says this is *equivalent* to failure of the Euler limit; nobody can prove either side. Equally open: whether the limit as $\nu\to0$ of $u^\nu$ even exists (in any subsequence-free sense) past a bluff body.

## 7. Current Research (as of June 2026)

- **Gevrey-class inviscid limits.** Gérard-Varet, Maekawa, Masmoudi (Duke, 2020) prove stability of boundary layers in Gevrey-$\tfrac{3}{2}$; pushing the Gevrey index toward the Sobolev threshold identified by Grenier–Nguyen's instability is the sharp-threshold program. Groups at Paris (ENS/Sorbonne), NYU/NYU-Abu Dhabi, Kyoto.
- **Anomalous dissipation constructions.** Explicit velocity fields (Drivas–Elgindi–Iyer–Jeong; Armstrong–Vicol, 2023–2025, for passive scalars and forced Navier–Stokes) exhibiting $\varepsilon^\nu \not\to 0$. These are advection or interior constructions, not wall-generated drag — the transfer to (P2) is the open step. *(frontier — verify)*
- **Convex integration at boundaries.** Extending Isett/Buckmaster–De Lellis–Székelyhidi non-conservative Euler solutions to domains with boundary, aiming at rough Euler limits carrying drag. *(frontier — verify)*
- **Separation blow-up.** Rigorous van Dommelen–Shen singularity formation (Collot–Ghoul–Ibrahim–Masmoudi; Kukavica–Vicol–Wang) — the analytic-category description of the moment potential flow ceases to describe reality.
- **Hoffman–Johnson program.** Continued computational claims (KTH/Chalmers lineage) that the drag mechanism is 3D instability of the potential solution rather than a Prandtl layer. Not accepted as a proof; the numerics do not settle the $\nu\to0$ limit. *(frontier — verify)*

## 8. Future Work

- Prove $\liminf_\nu C_D > 0$ for **any** body in **any** dimension, even with a symmetry ansatz or in a channel geometry. This would be the first rigorous statement that drag survives the inviscid limit.
- Close the Sobolev/Gevrey gap: identify the exact regularity index separating stable inviscid limits from instability, matching Grenier–Nguyen's counterexamples.
- Establish a boundary version of the Onsager theorem: what is the critical regularity above which a weak Euler solution in a domain with boundary conserves energy? (Bardos–Titi and Drivas–Nguyen have partial results; the boundary flux term is the obstruction.)
- Develop lower-bound machinery for dissipation — e.g., via vorticity-flux identities $\nu\partial_n\omega|_{\partial\Omega}$ or entropy-production functionals — since energy methods are structurally one-sided.
- Settle the steady bluff-body problem: does the family of steady exterior Navier–Stokes solutions with $\mathrm{Re}\to\infty$ converge, or does the loss of steadiness (Hopf bifurcation near $\mathrm{Re}\approx47$ for the cylinder) preclude any steady limit?

## 9. Key References

- **[Foundational]** J. le R. d'Alembert. *Essai d'une nouvelle théorie de la résistance des fluides.* David l'aîné, Paris, 1752.
- **[Foundational]** L. Prandtl. *Über Flüssigkeitsbewegung bei sehr kleiner Reibung.* Verhandlungen des III. Internationalen Mathematiker-Kongresses, Heidelberg, 1904, pp. 484–491.
- **[Foundational]** G. Birkhoff. *Hydrodynamics: A Study in Logic, Fact and Similitude.* Princeton University Press, 1950.
- **[Foundational]** T. Kato. *Remarks on zero viscosity limit for nonstationary Navier–Stokes flows with boundary.* In: Seminar on Nonlinear Partial Differential Equations (S. S. Chern, ed.), MSRI Publications 2, Springer, 1984, pp. 85–98. [DOI](https://doi.org/10.1007/978-1-4612-1110-5_6)
- **[Survey]** K. Stewartson. *D'Alembert's paradox.* SIAM Review 23(3), 308–343, 1981.
- **[Survey]** G. K. Batchelor. *An Introduction to Fluid Dynamics.* Cambridge University Press, 1967 (§6.4, §5.11).
- **[Survey]** G. P. Galdi. *An Introduction to the Mathematical Theory of the Navier–Stokes Equations: Steady-State Problems.* 2nd ed., Springer, 2011.
- **[Foundational]** R. Finn. *On the exterior stationary problem for the Navier–Stokes equations, and associated perturbation problems.* Archive for Rational Mechanics and Analysis 19, 363–406, 1965. [DOI](https://doi.org/10.1007/bf00253485)
- **[SOTA]** M. Sammartino, R. E. Caflisch. *Zero viscosity limit for analytic solutions of the Navier–Stokes equation on a half-space, I & II.* Communications in Mathematical Physics 192, 433–461 and 463–491, 1998. [DOI](https://doi.org/10.1007/s002200050305)
- **[SOTA]** E. Grenier. *On the nonlinear instability of Euler and Prandtl equations.* Communications on Pure and Applied Mathematics 53(9), 1067–1091, 2000. [DOI](https://doi.org/10.1002/1097-0312(200009)53:9<1067::aid-cpa1>3.0.co;2-q)
- **[SOTA]** D. Gérard-Varet, E. Dormy. *On the ill-posedness of the Prandtl equation.* Journal of the American Mathematical Society 23(2), 591–609, 2010. [DOI](https://doi.org/10.1090/s0894-0347-09-00652-3)
- **[SOTA]** Y. Maekawa. *On the inviscid limit problem of the vorticity equations for viscous incompressible flows in the half-plane.* Communications on Pure and Applied Mathematics 67(7), 1045–1128, 2014. [DOI](https://doi.org/10.1002/cpa.21516)
- **[SOTA]** D. Gérard-Varet, Y. Maekawa, N. Masmoudi. *Gevrey stability of Prandtl expansions for 2-dimensional Navier–Stokes flows.* Duke Mathematical Journal 167(13), 2531–2631, 2018. [DOI](https://doi.org/10.1215/00127094-2018-0020)
- **[SOTA]** P. Constantin, V. Vicol. *Remarks on high Reynolds numbers hydrodynamics and the inviscid limit.* Journal of Nonlinear Science 28, 711–724, 2018. [DOI](https://doi.org/10.1007/s00332-017-9424-z)
- **[SOTA]** J. P. Kelliher. *On Kato's conditions for vanishing viscosity limit.* Indiana University Mathematics Journal 56(4), 1711–1721, 2007.
- **[Contested]** J. Hoffman, C. Johnson. *Resolution of d'Alembert's paradox.* Journal of Mathematical Fluid Mechanics 12, 321–334, 2010.
- **[SOTA]** T. Buckmaster, V. Vicol. *Nonuniqueness of weak solutions to the Navier–Stokes equation.* Annals of Mathematics 189(1), 101–144, 2019. [DOI](https://doi.org/10.4007/annals.2019.189.1.3)

## 10. Worked Example / Concrete Special Case

**Potential flow past a sphere: the drag is exactly zero.**

Take a sphere of radius $a$ centred at the origin in a uniform stream $U e_z$, incompressible and irrotational. Solve $\Delta\phi=0$ with $\partial_r\phi|_{r=a}=0$ and $\nabla\phi\to Ue_z$. The dipole ansatz gives
$$\phi(r,\theta) = U\cos\theta\left(r + \frac{a^3}{2r^2}\right).$$
Check: $\partial_r\phi = U\cos\theta(1 - a^3/r^3)$, which vanishes at $r=a$. ✔

Surface velocity is purely tangential:
$$u_\theta\big|_{r=a} = \frac{1}{r}\partial_\theta\phi\Big|_{r=a} = -\frac{3}{2}U\sin\theta, \qquad |u|^2\big|_{r=a} = \frac{9}{4}U^2\sin^2\theta.$$

Bernoulli on the surface:
$$p(\theta) = p_\infty + \frac{1}{2}\rho U^2\left(1 - \frac{9}{4}\sin^2\theta\right).$$

Drag is the $z$-component of the pressure force, with $n = \hat r$, $n_z = \cos\theta$, $dS = 2\pi a^2\sin\theta \, d\theta$:
$$D = -\int_0^{\pi} p(\theta)\cos\theta \; 2\pi a^2 \sin\theta \, d\theta .$$
Split into two integrals:
$$\int_0^\pi \sin\theta\cos\theta \, d\theta = \left[\tfrac{1}{2}\sin^2\theta\right]_0^\pi = 0, \qquad \int_0^\pi \sin^3\theta\cos\theta \, d\theta = \left[\tfrac{1}{4}\sin^4\theta\right]_0^\pi = 0 .$$
Hence $D = 0$ exactly. The pressure distribution is **fore–aft symmetric**: $p(\theta) = p(\pi - \theta)$, so the high pressure at the rear stagnation point ($\theta=\pi$, $p = p_\infty + \tfrac12\rho U^2$) exactly cancels the push at the front.

**Where reality breaks the symmetry.** Along the rear surface ($\theta > \pi/2$) the pressure gradient is adverse, $dp/ds > 0$. In the Prandtl layer this decelerates the near-wall fluid until $\partial_Y u|_{Y=0} = 0$ — separation, at $\theta \approx 82°$ for a laminar layer. Downstream of separation the wake pressure stays near the separation value, roughly $p_\infty - 0.5\rho U^2$, instead of recovering to $p_\infty + \tfrac12\rho U^2$. The uncancelled base suction is the drag: measured $C_D \approx 0.47$ for a sphere at $\mathrm{Re}\sim10^4$, against the computed $C_D=0$ above.

**Why this is not yet a theorem.** Every step of the separation argument uses the Prandtl system, whose linearization around the non-monotone profile induced by this adverse gradient is ill-posed in $H^s$ (Gérard-Varet–Dormy). So the calculation above is a rigorous theorem about the *wrong model*, and the correction that fixes it is a formal asymptotic whose justification is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*