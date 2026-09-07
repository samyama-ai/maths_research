---
id: 06-pdes/magnetohydrodynamics-regularity
title: "Magnetohydrodynamics Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Magnetohydrodynamics Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/magnetohydrodynamics-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(u_0, b_0)$ be divergence-free vector fields on $\mathbb{R}^3$ (or $\mathbb{T}^3$) with $u_0, b_0 \in C^\infty$ and finite energy. **Does the incompressible viscous resistive MHD system with $\nu > 0$, $\eta > 0$ admit a unique smooth solution $(u, b)$ for all $t \in [0,\infty)$?**

Three graded versions are tracked here:

1. **3D full dissipation ($\nu,\eta>0$).** Global regularity — open. Exactly as hard as Navier–Stokes: any blow-up mechanism for Navier–Stokes with $b \equiv 0$ is a blow-up for MHD, so MHD regularity implies Navier–Stokes regularity. The converse is *not* known: the Lorentz force $b\cdot\nabla b$ supplies a second quadratic nonlinearity with no sign.
2. **2D partial dissipation.** With $\nu,\eta>0$ in two dimensions the answer is yes (classical). With exactly one of $\nu,\eta$ set to zero and *large* data, global regularity is open. This is the sharpest open case where the enemy is genuinely magnetic, not hydrodynamic.
3. **Ideal MHD ($\nu=\eta=0$).** Finite-time singularity formation from smooth data is expected but unproven; conversely, weak solutions are known to be wildly nonunique.

A complete resolution of (1) means: a proof that $\limsup_{t\to T^-}\big(\|u(t)\|_{H^s}+\|b(t)\|_{H^s}\big)<\infty$ for every $T<\infty$ and $s>5/2$, or an explicit smooth finite-energy datum whose solution loses regularity in finite time.

## 2. Mathematical Foundations

The system, in Alfvén (nondimensional) units, is

$$
\begin{cases}
\partial_t u + (u\cdot\nabla)u = -\nabla p + (b\cdot\nabla) b + \nu\,\Delta u,\\[2pt]
\partial_t b + (u\cdot\nabla)b = (b\cdot\nabla)u + \eta\,\Delta b,\\[2pt]
\nabla\cdot u = 0,\qquad \nabla\cdot b = 0,
\end{cases}
$$

with $p$ the total pressure (fluid plus magnetic, $p = \pi + \tfrac12|b|^2$), $\nu$ kinematic viscosity, $\eta = (\mu_0\sigma)^{-1}$ magnetic resistivity. The induction equation is the curl of Ohm's law $E + u\times b = \eta\,\mu_0^{-1}\nabla\times b$ combined with Faraday's law; $\nabla\cdot b = 0$ propagates from the datum.

**Energy law.** Testing with $(u,b)$ and using $\int (b\cdot\nabla b)\cdot u + \int (b\cdot\nabla u)\cdot b = 0$:

$$
\frac{1}{2}\frac{d}{dt}\big(\|u\|_{L^2}^2 + \|b\|_{L^2}^2\big) + \nu\|\nabla u\|_{L^2}^2 + \eta\|\nabla b\|_{L^2}^2 = 0 .
$$

**Scaling.** For $\nu=\eta$ the system is invariant under
$u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$, $b_\lambda(x,t)=\lambda b(\lambda x,\lambda^2 t)$, $p_\lambda = \lambda^2 p(\lambda x,\lambda^2 t)$.
Critical spaces are $\dot H^{1/2}(\mathbb{R}^3)$, $L^3$, $\dot B^{-1+3/p}_{p,q}$, $BMO^{-1}$ — the energy $\dot H^0$ is *supercritical* by half a derivative, identical to Navier–Stokes.

**Elsässer variables.** $z^\pm = u \pm b$ turn the system into

$$
\partial_t z^\pm + (z^\mp\cdot\nabla)z^\pm = -\nabla p + \frac{\nu+\eta}{2}\Delta z^\pm + \frac{\nu-\eta}{2}\Delta z^\mp .
$$

The nonlinearity becomes purely bilinear-crossed; when $\nu=\eta$ the coupling term drops and the pair is a symmetric system with a null-form structure exploited in Alfvén-wave stability arguments.

**Conserved quantities (ideal case).** Energy $E=\frac12\int(|u|^2+|b|^2)$; cross helicity $H_c=\int u\cdot b$; magnetic helicity $H_m=\int A\cdot b$ with $b=\nabla\times A$, in 3D. In 2D, with $b=\nabla^\perp\psi$, the flux function satisfies $\partial_t\psi + u\cdot\nabla\psi = \eta\Delta\psi$, giving the maximum principle $\|\psi(t)\|_{L^\infty}\le\|\psi_0\|_{L^\infty}$ for all $\eta\ge 0$.

**BKM-type criterion (Caflisch–Klapper–Steele, 1997).** A local smooth solution on $[0,T)$ extends past $T$ iff

$$
\int_0^{T}\big(\|\omega(t)\|_{L^\infty}+\|j(t)\|_{L^\infty}\big)\,dt<\infty,\qquad \omega=\nabla\times u,\; j=\nabla\times b .
$$

**Prodi–Serrin analogue.** $u\in L^p_tL^q_x$ with $2/p+3/q\le 1$, $q>3$, forces regularity — and the magnetic field needs no assumption at all (He–Xin 2005; Zhou 2005). The velocity alone controls the system.

## 3. History & State of the Art

- **1942** — Alfvén predicts hydromagnetic waves (*Nature* 150, 405), founding MHD.
- **1972** — Duvaut & Lions construct global Leray–Hopf weak solutions in 3D and prove 2D global regularity with $\nu,\eta>0$.
- **1983** — Sermange & Temam give the definitive functional-analytic treatment: local strong solutions in 3D, global in 2D, weak–strong uniqueness, and the first regularity criteria.
- **1989** — Kozono: weak solutions in exterior domains; $L^p$ theory.
- **1997** — Caflisch, Klapper & Steele: BKM criterion and Hausdorff-dimension bounds on singular sets for ideal MHD.
- **2005–2010** — Prodi–Serrin criteria refined to velocity-only and single-component conditions (He–Xin; Zhou; Cao–Wu).
- **2011** — Cao & Wu (*Adv. Math.* 226) prove 2D global regularity with **mixed partial dissipation**, e.g. $\nu\partial_{yy}u$ and $\eta\partial_{xx}b$ only. This opened the "how little dissipation suffices" program.
- **2014–2016** — Non-resistive MHD near a background field: Lin–Xu–Zhang; Ren–Wu–Xiang–Zhang; Fefferman–McCormick–Robinson–Rodrigo (local existence with $b_0\in H^s$, $u_0\in H^{s-1}$); Chemin–McCormick–Rodrigo–Zhang (critical Besov local theory).
- **2020–2021** — Convex integration reaches MHD: Beekie–Buckmaster–Vicol construct weak solutions of 3D ideal MHD violating magnetic-helicity conservation; Faraco–Lindberg–Székelyhidi construct bounded compactly supported ideal solutions, and prove Taylor's conjecture (helicity *is* conserved in the ideal limit of Leray–Hopf resistive solutions).

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| 3D, $\nu,\eta>0$, weak solutions | Global existence (Duvaut–Lions 1972); uniqueness open |
| 3D, $\nu,\eta>0$, small data in $\dot H^{1/2}$, $L^3$, $\dot B^{-1+3/p}_{p,q}$, $BMO^{-1}$ | Global regularity |
| 2D, $\nu>0,\eta>0$, arbitrary data | Global regularity (classical) |
| 2D, mixed partial dissipation $(\nu\partial_{yy}u,\ \eta\partial_{xx}b)$ | Global regularity, Cao–Wu 2011 |
| 2D generalized MHD, $(-\Delta)^\alpha u$, $(-\Delta)^\beta b$ | Global regularity for $\alpha\ge\frac12,\ \beta\ge1$; for $0\le\alpha<\frac12,\ 2\alpha+\beta>2$; and for $\alpha\ge2,\ \beta=0$ (Tran–Yu–Zhai, *JDE* 254, 2013) |
| 3D generalized MHD, $\alpha,\beta \ge 5/4$ | Global regularity (Wu, subcritical hyperdissipation) |
| 2D/3D non-resistive ($\eta=0$), data near a constant field $e_1$ | Global regularity and Alfvén-wave decay for small $H^s$ perturbations (Lin–Xu–Zhang 2015; Ren–Wu–Xiang–Zhang 2014; Wei–Zhang) |
| 3D, velocity criterion $u\in L^p_tL^q_x$, $2/p+3/q\le1$ | Regularity, no condition on $b$ (He–Xin 2005) |
| Ideal 3D, Onsager-type | Energy and cross-helicity conserved for $u,b\in C^{0,\theta}$, $\theta>1/3$; magnetic helicity conserved for $\theta>0$ |
| Partial regularity, 3D | Singular set has 1D parabolic Hausdorff measure zero for suitable weak solutions (He–Xin; Caffarelli–Kohn–Nirenberg analogue) |

Open in 2D with large data: $\nu>0,\eta=0$; $\nu=0,\eta>0$.

## 5. Principal Obstacles

- **Supercriticality.** The only coercive a priori bound is the energy identity, controlling $\dot H^1$ in time-average; the nonlinearity needs $\dot H^{1/2}$-level control. Every known estimate loses the same half derivative as Navier–Stokes. No scaling-invariant conserved quantity exists in 3D ($H_m$ has the wrong scaling: it is subcritical, and even so is only $L^2$-of-a-potential).
- **Vortex stretching plus current stretching.** In 3D the vorticity–current pair satisfies
 $\partial_t\omega + u\cdot\nabla\omega = \omega\cdot\nabla u + b\cdot\nabla j - j\cdot\nabla b + \nu\Delta\omega$,
 with a further quadratic-in-$\nabla u,\nabla b$ term in the $j$ equation. MHD therefore has *strictly more* stretching terms than Navier–Stokes; the magnetic terms are not sign-definite and the geometric depletion arguments that partially tame $\omega\cdot\nabla u$ (Constantin–Fefferman alignment) have no established magnetic analogue.
- **2D loses its saving grace.** For 2D Navier–Stokes the scalar vorticity obeys a maximum principle. For 2D MHD, $\omega$ is forced by $b\cdot\nabla j$, which is not controlled by any $L^\infty$ bound; only $\psi$ enjoys a maximum principle, and $\psi \mapsto j = \Delta\psi$ costs two derivatives. This is why 2D large-data $\eta=0$ resists.
- **No diffusion in the transported quantity.** With $\eta=0$, $b$ is Lie-transported (frozen-in). Its gradient grows like $\exp\!\int\|\nabla u\|_{L^\infty}$, so $\|j\|_{L^\infty}$ has only a double-exponential a priori bound at best; closing the loop through $b\cdot\nabla j$ is circular.
- **Convex integration cuts the other way.** Beekie–Buckmaster–Vicol show the weak formulation is far too flexible to be a route to uniqueness; any positive result must live at strong-solution regularity, where the tools are exactly the failing energy estimates.

## 6. The Gap

The proven statements stop at either (i) *two space dimensions with enough dissipation to give an $L^2$-in-time bound on $\nabla j$ or $\nabla\omega$*, or (ii) *smallness in a critical norm*. The general statement needs a bound on $\int_0^T\|\nabla u\|_{L^\infty}+\|\nabla b\|_{L^\infty}$ (equivalently $\int_0^T\|\omega\|_{L^\infty}+\|j\|_{L^\infty}$) from the energy alone.

Concretely, the missing step is control of the trilinear term

$$
\Big|\int_{\mathbb{R}^3} (b\cdot\nabla) j \cdot \omega \, dx\Big| \;\lesssim\; \|b\|_{L^\infty}\|\nabla j\|_{L^2}\|\omega\|_{L^2},
$$

where the energy supplies $\nabla b\in L^2_tL^2_x$ but not $b\in L^2_tL^\infty_x$ in 3D — a Sobolev-endpoint failure of exactly $\tfrac12$ derivative. In the 2D non-resistive case, the gap is one derivative: the maximum principle gives $\psi\in L^\infty$, the goal needs $\Delta\psi\in L^\infty$ or $\nabla\psi\in \dot B^{1}_{\infty,1}$.

## 7. Current Research (as of June 2026)

- **Stabilizing effect of a background magnetic field.** The largest active program (Wu and collaborators, Oklahoma State; Zhang's group, Peking; Wei, Beijing) shows that a constant field $b\equiv e_1$ turns the non-resistive system into a damped-wave system, yielding global small solutions with explicit decay. Extending "small" to "large in one variable" is the live frontier.
- **Partial and fractional dissipation.** Sharpening the $(\alpha,\beta)$ region for 2D generalized MHD toward the critical line $\alpha+\beta=1$, using commutator and modulus-of-continuity (De Giorgi–Kiselev–Nazarov–Volberg) methods. *(frontier — verify)* claims of global regularity for 2D MHD with $\alpha=0$ and logarithmically supercritical $\beta$ appear regularly and should be checked case by case.
- **Convex integration and nonuniqueness.** Extending Beekie–Buckmaster–Vicol to the *resistive* system, and locating the sharp Onsager exponent for magnetic helicity, following Faraco–Lindberg–Székelyhidi.
- **Self-similar and numerical blow-up hunts.** Adaptive computations of ideal MHD current-sheet collapse (Klein, Pouquet school; Hou-style high-resolution schemes) probe whether $j$ blows up in finite time with $\nu=\eta=0$; the Boussinesq/MHD analogy with Hou–Chen's 2022 boundary blow-up has renewed interest. *(frontier — verify)*
- **Machine-assisted search for unstable self-similar profiles**, transplanting the neural-network ansatz used for Boussinesq to axisymmetric MHD. *(frontier — verify)*

## 8. Future Work

- Find a *magnetic depletion* mechanism: a geometric condition on the alignment of $b$, $j$ and $\omega$ that forces cancellation in $b\cdot\nabla j - j\cdot\nabla b$, mirroring Constantin–Fefferman.
- Settle 2D large-data MHD with $\eta=0$, $\nu>0$. Most experts regard this as the decisive test case: it is genuinely magnetic and 2D, so hydrodynamic supercriticality is not the obstruction.
- Exploit $\|\psi\|_{L^\infty}$ better: build a logarithmically improved Beale–Kato–Majda inequality in which the flux-function maximum principle enters, closing a Gronwall loop for $\|j\|_{L^p}$ as $p\to\infty$.
- Decide whether ideal MHD develops singularities from smooth data — a positive answer would show the two-nonlinearity structure is essentially worse than Euler's and refocus effort on dissipative mechanisms.
- Prove or refute Taylor-type relaxation quantitatively: does the resistive limit select a unique force-free state?

## 9. Key References

- **[Foundational]** G. Duvaut, J.-L. Lions. *Inéquations en thermoélasticité et magnétohydrodynamique.* Archive for Rational Mechanics and Analysis 46, 241–279, 1972.
- **[Foundational]** M. Sermange, R. Temam. *Some mathematical questions related to the MHD equations.* Communications on Pure and Applied Mathematics 36(5), 635–664, 1983.
- **[Foundational]** H. Alfvén. *Existence of electromagnetic–hydrodynamic waves.* Nature 150, 405–406, 1942.
- **[Foundational]** R. Caflisch, I. Klapper, G. Steele. *Remarks on singularities, dimension and energy dissipation for ideal hydrodynamics and MHD.* Communications in Mathematical Physics 184, 443–455, 1997.
- **[SOTA / Recent]** C. Cao, J. Wu. *Global regularity for the two-dimensional MHD equations with mixed partial dissipation and magnetic diffusion.* Advances in Mathematics 226(2), 1803–1822, 2011.
- **[SOTA / Recent]** C. V. Tran, X. Yu, Z. Zhai. *On global regularity of 2D generalized magnetohydrodynamic equations.* Journal of Differential Equations 254(10), 4194–4216, 2013.
- **[SOTA / Recent]** F. Lin, L. Xu, P. Zhang. *Global small solutions of 2-D incompressible MHD system.* Journal of Differential Equations 259(10), 5440–5485, 2015.
- **[SOTA / Recent]** X. Ren, J. Wu, Z. Xiang, Z. Zhang. *Global existence and decay of smooth solution for the 2-D MHD equations without magnetic diffusion.* Journal of Functional Analysis 267(2), 503–541, 2014.
- **[SOTA / Recent]** C. L. Fefferman, D. S. McCormick, J. C. Robinson, J. L. Rodrigo. *Higher order commutator estimates and local existence for the non-resistive MHD equations and related models.* Journal of Functional Analysis 267(4), 1035–1056, 2014.
- **[SOTA / Recent]** R. Beekie, T. Buckmaster, V. Vicol. *Weak solutions of ideal MHD which do not conserve magnetic helicity.* Annals of PDE 6, article 1, 2020.
- **[SOTA / Recent]** D. Faraco, S. Lindberg, L. Székelyhidi Jr. *Bounded solutions of ideal MHD with compact support in space-time.* Archive for Rational Mechanics and Analysis 239, 51–93, 2021.
- **[Criteria]** C. He, Z. Xin. *On the regularity of weak solutions to the magnetohydrodynamic equations.* Journal of Differential Equations 213(2), 235–254, 2005.
- **[Survey]** J. Wu. *The 2D magnetohydrodynamic equations with partial or fractional dissipation.* In *Lectures on the Analysis of Nonlinear Partial Differential Equations*, Part 5, MLM 5, International Press, 2018.
- **[Survey / Book]** P. A. Davidson. *An Introduction to Magnetohydrodynamics.* Cambridge University Press, 2001 (2nd ed. 2016).
- **[Survey / Book]** D. Biskamp. *Nonlinear Magnetohydrodynamics.* Cambridge University Press, 1993.

## 10. Worked Example / Concrete Special Case

**2D MHD: why $\eta>0$ closes the estimate and $\eta=0$ does not.**

In 2D write $\omega = \partial_1 u_2 - \partial_2 u_1$ and $j = \partial_1 b_2 - \partial_2 b_1$. Taking curls, the stretching terms $\omega\cdot\nabla u$ and $j\cdot\nabla b$ vanish identically, leaving

$$
\partial_t \omega + u\cdot\nabla\omega = b\cdot\nabla j + \nu\Delta\omega,
$$
$$
\partial_t j + u\cdot\nabla j = b\cdot\nabla\omega + \eta\Delta j + 2\partial_1 b_1(\partial_2 u_1+\partial_1 u_2) - 2\partial_1 u_1(\partial_2 b_1 + \partial_1 b_2).
$$

**Case $\nu,\eta>0$.** Multiply the first by $\omega$, the second by $j$, add, and integrate. The two terms $\int (b\cdot\nabla j)\,\omega$ and $\int (b\cdot\nabla\omega)\, j$ cancel exactly, since $\nabla\cdot b=0$ gives $\int b\cdot\nabla(\omega j)=0$. The remaining quadratic terms $T$ satisfy $|T| \le C\|\nabla u\|_{L^2}\|\nabla b\|_{L^4}^2 \le C\|\nabla b\|_{L^2}\|j\|_{L^2}\|\nabla j\|_{L^2}$ by Ladyzhenskaya, so

$$
\frac{d}{dt}\big(\|\omega\|_{L^2}^2+\|j\|_{L^2}^2\big) + 2\nu\|\nabla\omega\|_{L^2}^2+2\eta\|\nabla j\|_{L^2}^2 \le \frac{C^2}{\eta}\|\nabla b\|_{L^2}^2\,\|j\|_{L^2}^2 + \eta\|\nabla j\|_{L^2}^2 .
$$

Since the energy identity gives $\int_0^\infty\|\nabla b\|_{L^2}^2\,dt \le \tfrac{1}{2\eta}(\|u_0\|_{L^2}^2+\|b_0\|_{L^2}^2)$, Gronwall yields for all $T$

$$
\|\omega(T)\|_{L^2}^2+\|j(T)\|_{L^2}^2 \le \big(\|\omega_0\|^2_{L^2}+\|j_0\|^2_{L^2}\big)\exp\!\Big(\frac{C^2}{2\eta^2}\big(\|u_0\|_{L^2}^2+\|b_0\|_{L^2}^2\big)\Big),
$$

a finite bound, hence global smoothness. Note the constant blows up like $e^{c/\eta^2}$.

**Case $\eta=0$.** The absorption step above is unavailable: there is no $\eta\|\nabla j\|_{L^2}^2$ on the left to soak up $T$. One is left with

$$
\frac{d}{dt}\|j\|_{L^2}^2 \lesssim \|\nabla u\|_{L^\infty}\|j\|_{L^2}^2,
$$

and $\|\nabla u\|_{L^\infty}$ must be recovered from $\omega$, which is forced by $b\cdot\nabla j$ — precisely the quantity being estimated. The only unconditional input is the flux-function maximum principle $\|\psi(t)\|_{L^\infty}=\|\psi_0\|_{L^\infty}$, two derivatives short of $j=\Delta\psi$. Smallness of $b_0 - e_1$ breaks the circle (the linearized system becomes a damped Alfvén wave equation $\partial_t^2 \psi - \partial_1^2\psi - \nu\Delta\partial_t\psi \approx 0$), which is exactly why every known 2D non-resistive theorem is perturbative.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*