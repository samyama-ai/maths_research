---
id: 06-pdes/euler-maxwell-two-fluid-global
title: "Global Solutions of the Two-Fluid Euler–Maxwell System"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Solutions of the Two-Fluid Euler–Maxwell System

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/euler-maxwell-two-fluid-global` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The two-fluid Euler–Maxwell system models a collisionless plasma of positively charged ions and negatively charged electrons, each treated as a compressible fluid, coupled through the self-consistent electromagnetic field. The constant state $(n_\pm, v_\pm, E, B) = (1, 0, 0, 0)$ — a uniform, quasi-neutral, motionless plasma — is an exact equilibrium.

**Central question.** Is this equilibrium globally nonlinearly stable? That is: for initial data close to the equilibrium in a sufficiently strong norm, does the Cauchy problem admit a unique global smooth solution that scatters to a linear one, or do shocks/plasma collapse form in finite time?

**Status.** Guo–Ionescu–Pausader (*Annals of Mathematics*, 2016) answered this affirmatively in **three space dimensions** for small, smooth, localized perturbations. The problem is listed as *partially-solved* because the following remain open:

1. **Dimension $d = 2$** for the genuine two-fluid system (only the one-fluid electron model is settled).
2. **Large data**: no global existence or blow-up criterion outside the perturbative regime; whether smooth solutions can develop singularities from generic large data is unknown.
3. **General vorticity and non-neutral / non-constant backgrounds**, where the linearized structure changes character.

A complete resolution requires either a global existence theorem without a smallness hypothesis, or an explicit finite-time singularity construction.

## 2. Mathematical Foundations

Let $d \in \{2,3\}$, $x \in \mathbb{R}^d$, $t \ge 0$. Write $n_\pm > 0$ for the ion/electron densities, $v_\pm$ for their velocities, $m_\pm > 0$ for masses, $E$ and $B$ for the electric and magnetic fields. In normalized units (light speed $c = 1$, unit charge):

$$\partial_t n_\pm + \nabla\cdot(n_\pm v_\pm) = 0,$$

$$m_\pm\big(\partial_t v_\pm + (v_\pm\cdot\nabla) v_\pm\big) + \frac{\nabla p_\pm(n_\pm)}{n_\pm} = \pm\big(E + v_\pm \times B\big),$$

$$\partial_t B + \nabla\times E = 0, \qquad \partial_t E - \nabla\times B = -\big(n_+ v_+ - n_- v_-\big),$$

with the constraints, propagated by the flow,

$$\nabla\cdot B = 0, \qquad \nabla\cdot E = n_- - n_+ .$$

The pressure is a barotropic law $p_\pm(n) = K_\pm n^{\gamma_\pm}$, $\gamma_\pm > 1$, with linearized sound speeds $b_\pm^2 = p_\pm'(1)/m_\pm$.

**Local theory.** The system is symmetrizable hyperbolic; Kato–Majda theory gives local well-posedness in $H^s(\mathbb{R}^d)$ for $s > 1 + d/2$ as long as $n_\pm$ stay positive (Jerome, 2003). The difficulty is entirely global.

**Linearization.** Set $n_\pm = 1 + \rho_\pm$ and drop quadratic terms. Splitting into curl-free (longitudinal) and divergence-free (transverse) parts gives three dispersion branches. Transverse electromagnetic waves obey

$$\omega^2 = \omega_p^2 + |\xi|^2, \qquad \omega_p^2 := \frac{1}{m_+} + \frac{1}{m_-},$$

a Klein–Gordon relation with mass $\omega_p$ (the plasma frequency). The longitudinal modes satisfy the quartic

$$\Big(\omega^2 - b_+^2|\xi|^2 - \tfrac{1}{m_+}\Big)\Big(\omega^2 - b_-^2|\xi|^2 - \tfrac{1}{m_-}\Big) = \frac{1}{m_+ m_-},$$

whose two roots $\Lambda_1 \le \Lambda_2$ are, respectively, a **massless acoustic branch** with $\Lambda_1(\xi) \sim c_s|\xi|$ as $\xi \to 0$, where

$$c_s^2 = \frac{m_+ b_+^2 + m_- b_-^2}{m_+ + m_-},$$

and a **Langmuir (plasma-oscillation) branch** with $\Lambda_2(0) = \omega_p$.

So the linearized two-fluid system is a coupled **wave + two Klein–Gordon** system with three distinct propagation speeds. Decay rates in $L^\infty$ for localized data are $t^{-(d-1)/2}$ (wave) and $t^{-d/2}$ (Klein–Gordon); the nonlinearity is quadratic and quasilinear.

**Space-time resonances** (Germain–Masmoudi–Shatah). For a quadratic interaction of branches $(\Lambda_a,\Lambda_b) \to \Lambda_c$, set the phase

$$\Phi_{abc}(\xi,\eta) = \Lambda_c(\xi) - \Lambda_a(\xi-\eta) - \Lambda_b(\eta).$$

Time resonances are $\{\Phi = 0\}$, space resonances $\{\nabla_\eta\Phi = 0\}$; the intersection controls whether normal forms or vector-field/dispersive estimates can absorb the quadratic terms. The obstruction is that neither $\Phi$ nor $\nabla_\eta\Phi$ vanishes alone but their common zero set is nonempty and, for Euler–Maxwell, of positive dimension.

## 3. History & State of the Art (SOTA)

- **1980s foundations.** Klainerman (*CPAM*, 1985) and Shatah (*CPAM*, 1985) proved global existence for small-data quadratic Klein–Gordon in $\mathbb{R}^{3+1}$ via vector fields and normal forms — the two techniques on which everything downstream rests.
- **1998.** Guo proved global existence of smooth irrotational flows for the **electron Euler–Poisson** system in $\mathbb{R}^{3+1}$, using the mass term generated by the Poisson coupling to lift decay from $t^{-1}$ to $t^{-3/2}$. This identified the "dispersive regularization by plasma frequency" mechanism.
- **2000s.** Chen–Jerome–Wang set up the compressible Euler–Maxwell framework; Jerome (2003) gave the local smooth theory. With relaxation (collision) terms, global existence near equilibrium is comparatively easy: Duan (2011) and Peng (2012) obtained global smooth solutions and decay for the **relaxed** two-fluid Euler–Maxwell system by energy methods, since damping supplies dissipation.
- **2011–2014.** Guo–Pausader (*CMP*, 2011) handled ion dynamics in Euler–Poisson; Ionescu–Pausader (*IMRN*, 2013) and Jang–Li–Zhang (*Forum Math.*, 2014) settled the harder 2D Euler–Poisson case. Germain–Masmoudi (*Ann. Sci. ÉNS*, 2014) proved global existence for the **one-fluid** (electron) Euler–Maxwell system in 3D.
- **2016 — SOTA.** Guo, Ionescu, and Pausader, *Global solutions of the Euler–Maxwell two-fluid system in 3D*, *Annals of Mathematics* 183 (2016), 377–498: global stability of the constant equilibrium in $d=3$ for small smooth localized perturbations, with scattering. This is the reference result.
- **2017.** Deng–Ionescu–Pausader (*ARMA*) proved global existence in **2D for the electron Euler–Maxwell system** (fixed ion background), a genuinely borderline case since 2D Klein–Gordon decays only like $t^{-1}$.

## 4. Partial Results / Verified Cases

| Case | Dimension | Result | Reference |
|---|---|---|---|
| Two-fluid Euler–Maxwell, no relaxation | $d=3$ | Global smooth solutions + scattering, small data | Guo–Ionescu–Pausader 2016 |
| One-fluid (electron) Euler–Maxwell | $d=3$ | Global small solutions | Germain–Masmoudi 2014 |
| One-fluid (electron) Euler–Maxwell | $d=2$ | Global small solutions | Deng–Ionescu–Pausader 2017 |
| Euler–Poisson (electrostatic limit, $B\equiv 0$) | $d=3$ | Global irrotational small solutions | Guo 1998; Guo–Pausader 2011 (ions) |
| Euler–Poisson | $d=2$ | Global small solutions | Ionescu–Pausader 2013; Jang–Li–Zhang 2014 |
| Non-neutral electron Euler–Poisson | $d=3$ | Global solutions | Germain–Masmoudi–Pausader 2013 |
| Two-fluid Euler–Maxwell **with relaxation** $-\nu_\pm v_\pm$ | $d=3$ | Global near-equilibrium solutions, exponential/algebraic decay | Duan 2011; Peng 2012 |

Quantitatively, the 3D two-fluid theorem requires data small in a combined high-Sobolev / weighted norm — roughly $\|U_0\|_{H^{N}} + \|xU_0\|_{H^{N'}} \le \varepsilon_0$ with $N$ in the range $10^2$–$10^3$ derivatives after the bootstrap, and yields the sharp linear decay $\|U(t)\|_{L^\infty} \lesssim \varepsilon_0 (1+t)^{-1}$ dictated by the slowest (acoustic) branch. The analysis is carried out under an irrotationality-type condition on the generalized vorticities $\nabla\times v_\pm \mp B/m_\pm$, which are transported rather than dispersed.

## 5. Principal Obstacles

1. **Slow decay from the acoustic branch.** Because $\Lambda_1(\xi) \sim c_s|\xi|$ is massless, the longitudinal acoustic mode decays only at the wave rate $t^{-1}$ in 3D. A quadratic nonlinearity with $t^{-1}$ decay is exactly borderline: $\int^t s^{-1}\,ds$ diverges logarithmically. Klainerman's null-condition machinery does not apply, because the quadratic interactions of *different* branches carry no null structure.
2. **Three distinct speeds.** The branches propagate at $c_s$, at the light speed $1$, and at the Langmuir group velocity, all different. Vector-field methods rely on a common Lorentz/scaling symmetry group; no single group commutes with a multi-speed system, and the scaling vector field is not available for Klein–Gordon.
3. **Nonempty space-time resonant set.** The 2-to-1 phase $\Phi_{abc}$ has a common zero set of $\{\Phi = 0\} \cap \{\nabla_\eta\Phi = 0\}$ that is not a point but a sphere-like set of positive dimension for certain speed configurations. Normal forms produce a division by $\Phi$ that is singular there, so the quadratic terms cannot be removed outright.
4. **Quasilinearity and derivative loss.** The nonlinearity contains one derivative of the unknown; normal forms cost a derivative, so any gain must be paid for by a high-order energy estimate, forcing the huge $N$ and a delicate coupling between weighted low-regularity and unweighted high-regularity norms.
5. **Vorticity does not disperse.** The generalized vorticity satisfies a transport equation; it neither decays nor gains regularity, so all dispersive gains must be extracted from the curl-free part alone.
6. **$d=2$ is critically worse.** Klein–Gordon decay drops to $t^{-1}$, the wave branch to $t^{-1/2}$, and the quadratic nonlinearity becomes genuinely non-integrable; only the one-fluid case, where the massless acoustic branch is absent, has been pushed through.

## 6. The Gap

Proven (Section 4): global existence and scattering for *small, smooth, spatially localized, essentially irrotational* perturbations in $d=3$, and for the *one-fluid* reductions in $d = 2,3$.

Claimed (Section 1): unconditional understanding of the Cauchy problem.

The precise gaps are:

- **(G1) Two-fluid in 2D.** The acoustic branch decays like $t^{-1/2}$ in the plane. No known combination of normal forms, weighted energy, and $Z$-norm bootstrap closes at this rate against a quadratic derivative nonlinearity. Crossing it requires either a hidden null/resonance cancellation between the acoustic and Langmuir branches, or a modified (long-range) scattering ansatz.
- **(G2) Large data.** Even the 1D compressible Euler system forms shocks from arbitrarily smooth data; whether the Lorentz force can prevent, or instead accelerate, that mechanism at large amplitude is unknown. There is no continuation criterion for Euler–Maxwell comparable to Beale–Kato–Majda for incompressible Euler.
- **(G3) Vorticity.** Removing the irrotationality-type restriction demands controlling a transported, non-decaying quantity coupled to the dispersive part over infinite time.

## 7. Current Research (as of June 2026)

- **Princeton / Brown / Courant school (Ionescu, Pausader, Deng, Germain, Masmoudi, Guo).** The $Z$-norm method matured through this program and was then exported to the Einstein–Klein–Gordon problem (Ionescu–Pausader, Annals of Math. Studies 213, 2022). Present effort is on wave–Klein–Gordon systems with slowly decaying massless branches, precisely the (G1) obstruction. *(frontier — verify)*
- **Vector-field/hyperboloidal methods** (LeFloch–Ma-type hyperboloidal foliations, Wang, Katayama) provide an alternative route to coupled wave–Klein–Gordon systems and are being tested on plasma models; their weakness is compact-support hypotheses on data. *(frontier — verify)*
- **Relaxation and quasi-neutral limits.** Rigorous convergence of two-fluid Euler–Maxwell to Euler–Poisson ($c \to \infty$) and to MHD or the incompressible limit ($\lambda_D \to 0$) is an active analytic thread, with uniform-in-parameter global existence still incomplete.
- **Non-constant backgrounds.** Stability of magnetized equilibria $B \equiv B_0 \ne 0$, where the linear operator loses isotropy and Landau/cyclotron resonances appear, is largely open.

## 8. Future Work

- Identify a **null structure adapted to multiple speeds** — a quadratic-form condition on the interaction coefficients that automatically vanishes on the space-time resonant set — which would mechanize the 3D proof and open 2D.
- Develop **modified scattering** for the acoustic branch, in the spirit of long-range scattering for 2D Schrödinger and gravity water waves, rather than pursuing pure linear asymptotics.
- Prove a **BKM-type continuation criterion** for Euler–Maxwell in terms of $\|\nabla v_\pm\|_{L^\infty}$ and $\|E,B\|_{L^\infty}$, a prerequisite for any large-data statement.
- Construct **explicit finite-time blow-up** in symmetry classes (spherically symmetric, or 1D with transverse fields) to delimit the perturbative theorem from above.
- Lower the regularity threshold $N$ from several hundred derivatives toward the scaling-critical range, which would signal that the mechanism, not just the bookkeeping, is understood.

## 9. Key References

- **[Foundational]** S. Klainerman. *Global existence of small amplitude solutions to nonlinear Klein–Gordon equations in four space-time dimensions.* Communications on Pure and Applied Mathematics 38 (1985), 631–641.
- **[Foundational]** J. Shatah. *Normal forms and quadratic nonlinear Klein–Gordon equations.* Communications on Pure and Applied Mathematics 38 (1985), 685–696.
- **[Foundational]** Y. Guo. *Smooth irrotational flows in the large to the Euler–Poisson system in $\mathbb{R}^{3+1}$.* Communications in Mathematical Physics 195 (1998), 249–265.
- **[Foundational]** P. Germain, N. Masmoudi, J. Shatah. *Global solutions for 3D quadratic Schrödinger equations.* International Mathematics Research Notices 2009, no. 3, 414–432. (introduces space-time resonances)
- **[Foundational]** J. W. Jerome. *The Cauchy problem for compressible hydrodynamic-Maxwell systems: a local theory for smooth solutions.* Differential and Integral Equations 16 (2003), 1345–1368.
- **[SOTA]** Y. Guo, A. D. Ionescu, B. Pausader. *Global solutions of the Euler–Maxwell two-fluid system in 3D.* Annals of Mathematics 183 (2016), no. 2, 377–498.
- **[SOTA]** P. Germain, N. Masmoudi. *Global existence for the Euler–Maxwell system.* Annales Scientifiques de l'École Normale Supérieure 47 (2014), 469–503.
- **[SOTA]** Y. Deng, A. D. Ionescu, B. Pausader. *The Euler–Maxwell system for electrons: global solutions in 2D.* Archive for Rational Mechanics and Analysis 225 (2017), 771–871.
- **[Related]** A. D. Ionescu, B. Pausader. *The Euler–Poisson system in 2D: global stability of the constant equilibrium solution.* International Mathematics Research Notices 2013, no. 4, 761–826.
- **[Related]** J. Jang, D. Li, X. Zhang. *Smooth global solutions for the two-dimensional Euler–Poisson system.* Forum Mathematicum 26 (2014), 645–701.
- **[Related]** Y. Guo, B. Pausader. *Global smooth ion dynamics in the Euler–Poisson system.* Communications in Mathematical Physics 303 (2011), 89–125.
- **[Related]** P. Germain, N. Masmoudi, B. Pausader. *Nonneutral global solutions for the electron Euler–Poisson system in three dimensions.* SIAM Journal on Mathematical Analysis 45 (2013), 267–278.
- **[Relaxation case]** R.-J. Duan. *Global smooth flows for the compressible Euler–Maxwell system: relaxation case.* Journal of Hyperbolic Differential Equations 8 (2011), 375–413.
- **[Relaxation case]** Y.-J. Peng. *Global existence and long-time behavior of smooth solutions of two-fluid Euler–Maxwell equations.* Annales de l'Institut Henri Poincaré, Analyse Non Linéaire 29 (2012), 737–759.
- **[Modeling]** G.-Q. Chen, J. W. Jerome, D. Wang. *Compressible Euler–Maxwell equations.* Transport Theory and Statistical Physics 29 (2000), 311–331.
- **[Survey / Method]** A. D. Ionescu, B. Pausader. *The Einstein–Klein–Gordon Coupled System: Global Stability of the Minkowski Solution.* Annals of Mathematics Studies 213, Princeton University Press, 2022.

## 10. Worked Example / Concrete Special Case

**Goal:** exhibit the massless acoustic branch that makes the two-fluid problem strictly harder than the one-fluid one.

Take $d = 3$, isentropic pressures with linearized sound speeds $b_\pm$, and consider **curl-free, electrostatic** perturbations ($B \equiv 0$, $v_\pm = \nabla\phi_\pm$). Write $n_\pm = 1 + \rho_\pm$ and keep linear terms:

$$\partial_t\rho_\pm + \nabla\cdot v_\pm = 0, \qquad \partial_t v_\pm + b_\pm^2\nabla\rho_\pm = \pm \frac{1}{m_\pm} E, \qquad \nabla\cdot E = \rho_- - \rho_+.$$

Take $\partial_t$ of the first equation and substitute the second:

$$\partial_t^2 \rho_\pm = b_\pm^2 \Delta\rho_\pm \mp \frac{1}{m_\pm}\nabla\cdot E = b_\pm^2\Delta\rho_\pm \mp \frac{1}{m_\pm}(\rho_- - \rho_+).$$

Insert the plane wave $\rho_\pm = \hat\rho_\pm e^{i(x\cdot\xi - \omega t)}$. With $A := b_+^2|\xi|^2 + \tfrac{1}{m_+}$ and $C := b_-^2|\xi|^2 + \tfrac{1}{m_-}$, vanishing of the determinant gives

$$\omega^4 - (A + C)\,\omega^2 + \Big(AC - \tfrac{1}{m_+m_-}\Big) = 0 .$$

**Step 1 — evaluate at $\xi = 0$.** Then $A + C = \omega_p^2$ and $AC - \frac{1}{m_+m_-} = 0$ exactly, so

$$\omega^2\big(\omega^2 - \omega_p^2\big) = 0 \implies \omega = 0 \ \text{ or } \ \omega = \omega_p .$$

The quartic has a **root at the origin**: one longitudinal branch is massless.

**Step 2 — expand the small root.** The constant term is

$$AC - \tfrac{1}{m_+m_-} = \Big(\tfrac{b_+^2}{m_-} + \tfrac{b_-^2}{m_+}\Big)|\xi|^2 + b_+^2 b_-^2|\xi|^4 ,$$

so for $|\xi| \ll 1$, $\ \omega^2 \approx \big(AC - \frac{1}{m_+m_-}\big)/(A+C)$, i.e.

$$\Lambda_1(\xi)^2 = \frac{\big(b_+^2/m_- + b_-^2/m_+\big)}{1/m_+ + 1/m_-}\,|\xi|^2 + O(|\xi|^4) = c_s^2|\xi|^2 + O(|\xi|^4), \qquad c_s^2 = \frac{m_+ b_+^2 + m_- b_-^2}{m_+ + m_-}.$$

This is the ion-acoustic wave. The other root is $\Lambda_2(\xi)^2 = \omega_p^2 + O(|\xi|^2)$, a Klein–Gordon branch.

**Step 3 — read off the consequence.** Localized data on $\Lambda_2$ decay like $t^{-3/2}$, so quadratic terms are integrable in time and Guo's 1998 argument runs. Data on $\Lambda_1$ decay only like $t^{-1}$: a quadratic self-interaction contributes $\int_1^t s^{-1}\,ds = \log t$, which is not summable. Freezing the ion fluid (setting $m_+ = \infty$) removes the equation for $\rho_+$ entirely, the quartic degenerates to $\omega^2 = b_-^2|\xi|^2 + 1/m_-$, and the massless branch disappears — which is exactly why the one-fluid problem was solved first and why the two-fluid theorem required the full space-time resonance analysis of Guo–Ionescu–Pausader.

**Step 4 — the resonance that must be handled.** For the acoustic self-interaction feeding the Langmuir branch, $\Phi(\xi,\eta) = \Lambda_2(\xi) - \Lambda_1(\xi-\eta) - \Lambda_1(\eta)$. At small frequencies $\Phi \approx \omega_p - c_s(|\xi - \eta| + |\eta|) $, which vanishes on the sphere $|\xi-\eta| + |\eta| = \omega_p/c_s$, while $\nabla_\eta\Phi = c_s\big(\tfrac{\xi-\eta}{|\xi-\eta|} - \tfrac{\eta}{|\eta|}\big)$ vanishes whenever $\eta \parallel \xi - \eta$ with the same orientation. The two conditions are simultaneously satisfiable on a nontrivial set, so neither integration by parts in $\eta$ (space resonance) nor division by $\Phi$ (normal form) works alone — the technical heart of the 3D proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*