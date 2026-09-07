---
id: 06-pdes/navier-stokes-smoothness
title: "Navier-Stokes Smoothness"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Navier-Stokes Smoothness

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/navier-stokes-smoothness` · **Status:** open

## 1. Problem Statement / Conjecture

The Clay Millennium Problem asks whether smooth, finite-energy solutions of the incompressible Navier-Stokes equations in three space dimensions exist for all time.

Take $\nu > 0$ and unknowns $u : \mathbb{R}^3 \times [0,\infty) \to \mathbb{R}^3$ (velocity) and $p : \mathbb{R}^3 \times [0,\infty) \to \mathbb{R}$ (pressure) solving

$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu \Delta u, \qquad \nabla\cdot u = 0, \qquad u(x,0) = u_0(x).$$

**Statement (existence and smoothness, $\mathbb{R}^3$).** For every divergence-free $u_0 \in C^\infty(\mathbb{R}^3;\mathbb{R}^3)$ satisfying the decay bound $|\partial_x^\alpha u_0(x)| \le C_{\alpha K}(1+|x|)^{-K}$ for all multi-indices $\alpha$ and all $K$, there exist $u \in C^\infty(\mathbb{R}^3\times[0,\infty))$ and $p \in C^\infty(\mathbb{R}^3\times[0,\infty))$ solving the system with bounded energy $\int_{\mathbb{R}^3}|u(x,t)|^2\,dx < C$ for all $t \ge 0$.

A resolution requires either a proof of this statement (or its periodic analogue on $\mathbb{T}^3 = \mathbb{R}^3/\mathbb{Z}^3$), or a counterexample: smooth decaying data whose solution develops a singularity in finite time — no smooth finite-energy solution exists on $[0,\infty)$. Fefferman's official problem description also accepts a disproof of the corresponding statements for the Euler-free forced variants under stated hypotheses; a breakdown result for the *inviscid* Euler equations alone does **not** settle the problem.

## 2. Mathematical Foundations

**Function spaces.** Let $H = \overline{\{u\in C_c^\infty(\mathbb{R}^3;\mathbb{R}^3): \nabla\cdot u = 0\}}^{L^2}$ and let $\mathbb{P} = I - \nabla\Delta^{-1}\nabla\cdot$ be the Leray projector onto $H$. Applying $\mathbb{P}$ removes the pressure:

$$\partial_t u = \nu\Delta u - \mathbb{P}\,\nabla\cdot(u\otimes u), \qquad u(0)=u_0 .$$

Pressure is recovered from the elliptic relation $-\Delta p = \partial_i\partial_j(u_iu_j)$, i.e. $p = R_iR_j(u_iu_j)$ with $R_i$ the Riesz transforms; the nonlinearity is therefore *nonlocal*.

**Energy and enstrophy.** Smooth solutions satisfy the identity (the transport term cancels because $\int (u\cdot\nabla)u\cdot u = 0$ when $\nabla \cdot u = 0$):

$$\frac{1}{2}\frac{d}{dt}\|u(t)\|_{L^2}^2 + \nu\|\nabla u(t)\|_{L^2}^2 = 0 .$$

The vorticity $\omega = \nabla\times u$ obeys $\partial_t\omega + (u\cdot\nabla)\omega = (\omega\cdot\nabla)u + \nu\Delta\omega$. The term $(\omega\cdot\nabla)u$ — *vortex stretching* — is absent in 2D and is the sole source of the difficulty.

**Leray-Hopf weak solutions.** $u \in L^\infty_t L^2_x \cap L^2_t \dot H^1_x$ solving the equation distributionally and satisfying the energy inequality $\|u(t)\|_2^2 + 2\nu\int_0^t\|\nabla u\|_2^2 \le \|u_0\|_2^2$. These exist globally for any $u_0\in H$ (Leray 1934, Hopf 1951) but are not known to be unique or smooth.

**Scaling and criticality.** If $(u,p)$ solves the system, so does

$$u_\lambda(x,t) = \lambda\, u(\lambda x, \lambda^2 t), \qquad p_\lambda(x,t)=\lambda^2 p(\lambda x,\lambda^2 t), \qquad \lambda>0 .$$

Norms invariant under this scaling are *critical*: $\dot H^{1/2}(\mathbb{R}^3)$, $L^3(\mathbb{R}^3)$, $\dot B^{-1+3/p}_{p,\infty}$, $BMO^{-1}$. The energy $\|u\|_{L^2}$ scales as $\lambda^{-1/2}$ and is therefore **supercritical** in 3D — the conserved quantity is weaker than the invariant one. This single mismatch is the structural core of the problem.

**Regularity criteria.** *Prodi-Serrin-Ladyzhenskaya:* a Leray-Hopf solution with $u\in L^q_tL^p_x$, $\frac{2}{q}+\frac{3}{p}\le 1$, $p>3$, is smooth. *Beale-Kato-Majda type:* blowup at $T$ forces $\int_0^T\|\omega(t)\|_{L^\infty}dt = \infty$. *Leray's lower bound:* if $T$ is a first blowup time then $\|u(t)\|_{L^p} \ge c_p (T-t)^{-(1-3/p)/2}$ for $p>3$.

## 3. History & State of the Art (SOTA)

- **1934.** Leray constructs global weak ("turbulent") solutions in $\mathbb{R}^3$, proves local-in-time smoothness, and shows the set of singular times has $1/2$-dimensional Hausdorff measure zero. Hopf extends to bounded domains (1951).
- **1959-1969.** Ladyzhenskaya proves 2D global well-posedness and writes the standard monograph; Prodi and Serrin obtain the conditional regularity classes (1959-1962).
- **1968.** Ladyzhenskaya, and independently Uchovskii-Yudovich, prove global regularity for axisymmetric flow **without swirl**.
- **1976-1982.** Scheffer initiates partial regularity; Caffarelli, Kohn and Nirenberg prove that the singular set $S$ of a suitable weak solution has vanishing one-dimensional parabolic Hausdorff measure, $\mathcal{P}^1(S)=0$.
- **1993.** Constantin-Fefferman: regularity holds if the vorticity direction $\omega/|\omega|$ is Lipschitz-continuous in regions of large vorticity — geometric depletion of stretching.
- **2001.** Koch-Tataru: global well-posedness for small data in the largest known critical space $BMO^{-1}$.
- **2003.** Escauriaza-Seregin-Šverák: solutions bounded in the critical $L^\infty_t L^3_x$ are regular — the endpoint $p=3$ of Prodi-Serrin, proved by backward-uniqueness for parabolic operators. Seregin (2012) upgrades to $\|u(t)\|_{L^3}\to\infty$ at a blowup time.
- **2016.** Tao constructs finite-time blowup for an *averaged* Navier-Stokes equation with the same energy identity and scaling, showing that no purely "abstract" energy/scaling argument can suffice.
- **2019.** Buckmaster-Vicol prove non-uniqueness of finite-energy distributional (non-Leray-Hopf) weak solutions by convex integration; Albritton-Brué-Colombo (2022) prove non-uniqueness of *Leray-Hopf* solutions for the forced equation.
- **2019-2021.** Tao gives quantitative blowup rates: at a first singular time, $\|u(t)\|_{L^3} \gtrsim \left(\log\log\log\frac{1}{T-t}\right)^{c}$; Palasek sharpens the axisymmetric case.
- **2021-2023.** Elgindi proves finite-time singularity for 3D Euler with $C^{1,\alpha}$ data; Chen-Hou give a computer-assisted proof of self-similar blowup for 3D Euler with boundary and 2D Boussinesq.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| $d=2$ (plane, torus, bounded domain) | Global smoothness and uniqueness for $u_0\in H$ (Ladyzhenskaya 1959) |
| Short time, $d=3$ | Local existence and uniqueness for $u_0 \in H^s$, $s\ge 1/2$, or $L^3$ (Kato-Fujita 1962; Kato 1984) |
| Small critical data | Global regularity if $\|u_0\|_{\dot H^{1/2}}$, $\|u_0\|_{L^3}$ or $\|u_0\|_{BMO^{-1}}$ is below an absolute constant (Koch-Tataru 2001) |
| Large viscosity / short time | Global for $\|u_0\|_{L^2}\|\nabla u_0\|_{L^2} \le c\nu^2$ |
| Axisymmetric, no swirl | Global smoothness (Ladyzhenskaya; Uchovskii-Yudovich 1968) |
| Axisymmetric with swirl, scale-invariant bound | Regular under $|u(x,t)| \le C/|x'|$ (Koch-Nadirashvili-Seregin-Šverák 2009, Acta) |
| Partial regularity | $\mathcal{P}^1(S)=0$; in particular $S$ contains no space-time curve of positive 1D measure and singularities are isolated in time on a set of $1/2$-measure zero (CKN 1982) |
| Hyperdissipation $(-\Delta)^\alpha$ | Global regularity for $\alpha\ge 5/4$ (Ladyzhenskaya, Lions); logarithmically supercritical $\alpha=5/4$ with $\log$ correction (Tao 2009); CKN-type bound for $1<\alpha<5/4$ (Katz-Pavlović 2002) |
| Conditional criteria | $u\in L^q_tL^p_x$ with $2/q+3/p\le1$, $p>3$; $u\in L^\infty_tL^3_x$; one velocity component or $\partial_3 u$ criteria; Constantin-Fefferman vorticity-direction criterion |

## 5. Principal Obstacles

- **Supercriticality.** The only globally controlled quantity, $\|u\|_{L^2}$, scales as $\lambda^{-1/2}$ under the symmetry that preserves the equation. At small scale $\lambda\to 0$ the energy bound gives *no* information: any iteration loses powers of $\lambda$ and the standard local-to-global bootstrap fails. There is a scale-invariant gap of $1/2$ derivative between $L^2$ and $\dot H^{1/2}$.
- **Vortex stretching.** The term $(\omega\cdot\nabla)u$ is quadratic in $\omega$ with $\nabla u$ recovered from $\omega$ by an order-zero singular integral. The naive enstrophy estimate gives $\frac{d}{dt}\|\omega\|_2^2 \lesssim \|\omega\|_2^3 - \nu\|\nabla\omega\|_2^2$ — a Riccati inequality whose solution can blow up.
- **Nonlocality of pressure.** $p = R_iR_j(u_iu_j)$ destroys any maximum principle: there is no pointwise comparison, no Harnack, no scalar-type barrier argument, unlike for scalar quasilinear parabolic equations.
- **No usable conserved quantity beyond energy.** Helicity $\int u\cdot\omega$ is conserved only for Euler and is sign-indefinite; it does not control any Sobolev norm.
- **Tao's obstruction.** The averaged Navier-Stokes counterexample (2016) satisfies the identical energy identity, scaling, and the divergence-free cancellation structure, yet blows up. Hence any proof must exploit fine features of the *specific* Euler quadratic form — genuinely non-perturbative input that current harmonic analysis does not supply.
- **Convex integration is one-directional.** The Buckmaster-Vicol machinery produces wild non-unique weak solutions but cannot yet produce *Leray-Hopf* solutions in the unforced case, nor smooth blowup; the constructions are non-smooth by design.

## 6. The Gap

Proven: regularity under any *critical* control, down to and including $L^\infty_tL^3_x$ (ESŠ 2003), with quantitative lower bounds $\|u(t)\|_{L^3}\gtrsim(\log\log\log(T-t)^{-1})^c$ (Tao 2019). Also proven: the singular set is at most parabolic-1-dimensional (CKN).

Wanted: to derive a critical bound from the *supercritical* energy bound. Concretely, the missing step is an a priori estimate of the form

$$\|u_0\|_{L^2} \le M \;\Longrightarrow\; \sup_{t<T}\|u(t)\|_{L^3} \le F(M,\nu)$$

for some function $F$, or equivalently an improvement of CKN from $\mathcal{P}^1(S)=0$ to $S=\emptyset$. Every known route loses exactly one half-derivative of scaling; closing that half-derivative — or showing it cannot be closed by exhibiting a blowup mechanism — is the entire problem. Tao's averaged construction shows the gap cannot be closed by any argument insensitive to the exact form of $\mathbb{P}\nabla\cdot(u\otimes u)$.

## 7. Current Research (as of June 2026)

- **Computer-assisted self-similar blowup (Caltech/NYU/Courant, Hou, Chen, Gómez-Serrano, Buckmaster).** After the Chen-Hou proof of 3D Euler blowup with boundary, the programme targets *unstable* self-similar profiles for Navier-Stokes with force, and then $\nu>0$ genuinely; the viscous case is hindered by the fact that exact self-similar Navier-Stokes blowup is ruled out by Nečas-Růžička-Šverák (1996) and Tsai (1998). Neural-network-assisted profile searches (Wang-Lai-Gómez-Serrano-Buckmaster) continue to yield new unstable Euler profiles *(frontier — verify)*.
- **Quantitative regularity (Tao, Palasek, Barker, Prange).** Explicit triple-exponential and epsilon-regularity-based bounds under critical hypotheses; extension to $L^\infty_tL^p_x$, $p>3$, and to axisymmetric settings with weaker swirl assumptions.
- **Convex integration for Leray-Hopf solutions (Albritton, Brué, Colombo, De Lellis, Székelyhidi).** After forced non-uniqueness in 2022, the target is unforced non-uniqueness or sharp $L^q_tL^p_x$ ill-posedness thresholds.
- **Non-uniqueness/instability of Leray solutions and vortex-ring instabilities (Vishik-type unbounded-vorticity 2D Euler results, extended to viscous settings).**
- **Model equations and dyadic/shell models (Katz-Pavlović, Cheskidov, Friedlander).** Establishing where the supercritical barrier truly bites.
- **Geometric depletion.** Refinements of Constantin-Fefferman via Lagrangian and Clebsch structures; numerical evidence that vorticity alignment suppresses stretching in near-singular Euler flows.

## 8. Future Work

- Seek a *non-scale-invariant* monotone quantity — Tao has argued explicitly that a "supercritical Lyapunov functional" or a barrier propagating from large to small scales would evade his averaged obstruction; none is known.
- Push CKN below dimension 1: any improvement to $\mathcal{P}^{1-\varepsilon}(S)=0$ would be a genuine step, since a point singularity has parabolic dimension $0$.
- Close the hyperdissipative window: prove global regularity for $(-\Delta)^\alpha$ with $\alpha<5/4$ down to $\alpha=1$, or find the exact $\alpha$ where blowup begins.
- Build a Navier-Stokes analogue of Elgindi's $C^{1,\alpha}$ Euler mechanism, accepting non-smooth data as an intermediate target.
- Machine-assisted rigorous search: interval-arithmetic verification of approximate blowup profiles for forced Navier-Stokes, then removal of the force.

## 9. Key References

- **[Foundational]** J. Leray. *Sur le mouvement d'un liquide visqueux emplissant l'espace.* Acta Mathematica 63 (1934), 193–248.
- **[Foundational]** E. Hopf. *Über die Anfangswertaufgabe für die hydrodynamischen Grundgleichungen.* Mathematische Nachrichten 4 (1951), 213–231.
- **[Foundational]** O. A. Ladyzhenskaya. *The Mathematical Theory of Viscous Incompressible Flow.* 2nd ed., Gordon and Breach, 1969.
- **[Foundational]** L. Caffarelli, R. Kohn, L. Nirenberg. *Partial regularity of suitable weak solutions of the Navier-Stokes equations.* Communications on Pure and Applied Mathematics 35 (1982), 771–831.
- **[Problem statement]** C. L. Fefferman. *Existence and smoothness of the Navier-Stokes equation.* In The Millennium Prize Problems, Clay Mathematics Institute / AMS, 2006, 57–67.
- **[Foundational]** J. Serrin. *On the interior regularity of weak solutions of the Navier-Stokes equations.* Archive for Rational Mechanics and Analysis 9 (1962), 187–195.
- **[Foundational]** J. T. Beale, T. Kato, A. Majda. *Remarks on the breakdown of smooth solutions for the 3-D Euler equations.* Communications in Mathematical Physics 94 (1984), 61–66.
- **[SOTA]** L. Escauriaza, G. Seregin, V. Šverák. *$L_{3,\infty}$-solutions of Navier-Stokes equations and backward uniqueness.* Russian Mathematical Surveys 58 (2003), 211–250.
- **[SOTA]** H. Koch, D. Tataru. *Well-posedness for the Navier-Stokes equations.* Advances in Mathematics 157 (2001), 22–35.
- **[SOTA]** T. Tao. *Finite time blowup for an averaged three-dimensional Navier-Stokes equation.* Journal of the American Mathematical Society 29 (2016), 601–674.
- **[SOTA]** T. Buckmaster, V. Vicol. *Nonuniqueness of weak solutions to the Navier-Stokes equation.* Annals of Mathematics 189 (2019), 101–144.
- **[SOTA]** D. Albritton, E. Brué, M. Colombo. *Non-uniqueness of Leray solutions of the forced Navier-Stokes equations.* Annals of Mathematics 196 (2022), 415–455.
- **[SOTA]** T. M. Elgindi. *Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$.* Annals of Mathematics 194 (2021), 647–727.
- **[SOTA]** P. Constantin, C. Fefferman. *Direction of vorticity and the problem of global regularity for the Navier-Stokes equations.* Indiana University Mathematics Journal 42 (1993), 775–789.
- **[SOTA]** N. Katz, N. Pavlović. *A cheap Caffarelli-Kohn-Nirenberg inequality for Navier-Stokes equations with hyper-dissipation.* Geometric and Functional Analysis 12 (2002), 355–379.
- **[Survey]** C. L. Fefferman, T. Buckmaster, V. Vicol. *Navier-Stokes equations.* In: various expository accounts; see also T. Buckmaster, V. Vicol, *Convex integration and phenomenologies in turbulence*, EMS Surveys in Mathematical Sciences 6 (2019), 173–263.
- **[Survey]** P. Constantin, C. Foias. *Navier-Stokes Equations.* University of Chicago Press, 1988.
- **[Survey]** J. C. Robinson, J. L. Rodrigo, W. Sadowski. *The Three-Dimensional Navier-Stokes Equations: Classical Theory.* Cambridge University Press, 2016.

## 10. Worked Example / Concrete Special Case

**(a) Why 2D is solved and 3D is not — the enstrophy computation.**

Take the torus $\mathbb{T}^d$ and a smooth solution. Multiply the vorticity equation by $\omega$ and integrate. Transport contributes nothing ($\int (u\cdot\nabla)\omega\cdot\omega = \frac12\int u\cdot\nabla|\omega|^2 = 0$), so

$$\frac{1}{2}\frac{d}{dt}\|\omega\|_{L^2}^2 = \underbrace{\int (\omega\cdot\nabla)u\cdot\omega\,dx}_{\text{stretching}} - \nu\|\nabla\omega\|_{L^2}^2 .$$

*In 2D:* $\omega = \omega_3 e_3$ is a scalar transported quantity and $(\omega\cdot\nabla)u \equiv 0$. Hence $\frac{d}{dt}\|\omega\|_2^2 = -2\nu\|\nabla\omega\|_2^2 \le 0$, so $\|\omega(t)\|_{L^2}\le\|\omega_0\|_{L^2}$ for all $t$. Since $\|\nabla u\|_{L^2}=\|\omega\|_{L^2}$ in 2D, the $H^1$ norm never grows and the local solution extends globally. Enstrophy is a *critical* quantity in 2D.

*In 3D:* estimate the stretching term with Hölder and Gagliardo-Nirenberg, $\|\omega\|_{L^3}\lesssim\|\omega\|_{L^2}^{1/2}\|\nabla\omega\|_{L^2}^{1/2}$:

$$\left|\int(\omega\cdot\nabla)u\cdot\omega\right| \le \|\nabla u\|_{L^3}\|\omega\|_{L^3}^{2} \lesssim \|\omega\|_{L^2}^{3/2}\|\nabla\omega\|_{L^2}^{3/2} \le \frac{\nu}{2}\|\nabla\omega\|_{L^2}^2 + \frac{C}{\nu^3}\|\omega\|_{L^2}^{6}.$$

Writing $E(t)=\|\omega(t)\|_{L^2}^2$ this gives $E' \le C\nu^{-3}E^{3}$, i.e.

$$E(t) \le \frac{E(0)}{\sqrt{1 - 2C\nu^{-3}E(0)^2 t}},$$

which is finite only for $t < T_* = \nu^3/(2CE(0)^2)$. The estimate provides *no* control past $T_*$, and no conserved quantity replaces it, because the only global bound $\|u\|_{L^2}$ is one half-derivative too weak.

**(b) The scaling ledger, made explicit.** For $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$:

$$\|u_\lambda(0)\|_{L^2(\mathbb{R}^3)} = \lambda^{-1/2}\|u_0\|_{L^2}, \qquad \|u_\lambda(0)\|_{L^3(\mathbb{R}^3)} = \|u_0\|_{L^3}, \qquad \|u_\lambda(0)\|_{\dot H^{1/2}} = \|u_0\|_{\dot H^{1/2}} .$$

Rescale to a small ball of radius $\lambda = 10^{-6}$: the available energy bound degrades by a factor $\lambda^{-1/2}=10^3$, while the quantity that would guarantee regularity is unchanged. Iterating the local theory over $N$ dyadic scales costs $2^{N/2}$; the bootstrap therefore diverges. In $d=2$ the exponent is $\lambda^{-1/2}\to\lambda^{0}$: energy is critical, and the same iteration closes. **The entire Millennium Problem sits in that one exponent.**

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*