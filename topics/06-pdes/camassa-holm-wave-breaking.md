---
id: 06-pdes/camassa-holm-wave-breaking
title: "Camassa Holm Wave Breaking"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Camassa–Holm Wave Breaking

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/camassa-holm-wave-breaking` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Camassa–Holm (CH) equation is the shallow-water model

$$u_t - u_{txx} + 3uu_x = 2u_x u_{xx} + u u_{xxx}, \qquad x \in \mathbb{R} \ \text{or}\ x \in \mathbb{S}^1 = \mathbb{R}/\mathbb{Z}, \ t > 0 .$$

Its solutions do **not** blow up in amplitude; instead they *break*: the solution stays bounded while its slope becomes unbounded in finite time. The problem cluster is:

1. **Characterization.** Give a necessary *and* sufficient condition on the initial datum $u_0$ for wave breaking, i.e. for existence of $T < \infty$ with
$$\sup_{t<T}\|u(t)\|_{L^\infty} < \infty, \qquad \liminf_{t\to T^-}\ \inf_{x} u_x(t,x) = -\infty .$$
2. **Rate and set.** Determine the asymptotics of $\inf_x u_x(t,\cdot)$ as $t \to T^-$ and the structure (measure, cardinality) of the breaking set.
3. **Continuation.** Decide whether the solution can be continued past $T$ uniquely, and in what class — energy is carried into a singular measure at breaking, and the choice of what happens to it (return it, or dissipate it) selects distinct semigroups.

A complete resolution requires: an explicit criterion decidable from $u_0$; a sharp blow-up rate; and existence **and uniqueness** of a global semiflow beyond breaking in a well-specified solution class.

Items (1)–(2) are settled. Item (3) is settled for the two canonical classes (conservative and dissipative). What remains genuinely open is listed in §6.

## 2. Mathematical Foundations

**Momentum form.** With the momentum density $m := u - u_{xx} = (1-\partial_x^2)u$, CH reads
$$m_t + u m_x + 2 u_x m = 0,$$
a transport equation with a stretching term. Equivalently, after inverting $1-\partial_x^2$ with Green's function $G(x) = \tfrac12 e^{-|x|}$ on $\mathbb{R}$,
$$u_t + u u_x + \partial_x G * \Big( u^2 + \tfrac12 u_x^2 \Big) = 0 .$$
This nonlocal form makes the model a Burgers equation with a smoothing, but nonlocal, pressure-type correction.

**Conserved quantities.** CH is completely integrable with a bi-Hamiltonian structure and a Lax pair; it is the geodesic flow of the right-invariant $H^1$ metric on the diffeomorphism group. The two lowest invariants are
$$E(u) = \int \big(u^2 + u_x^2\big)\,dx = \|u\|_{H^1}^2, \qquad F(u) = \int \big(u^3 + u\,u_x^2\big)\,dx .$$
Since $H^1(\mathbb{R}) \hookrightarrow L^\infty$ with $\|u\|_{L^\infty}^2 \le \tfrac12 \|u\|_{H^1}^2$, the amplitude is a priori bounded — blow-up can only be in the gradient.

**Characteristics.** Let $q(t,\xi)$ solve $q_t = u(t,q)$, $q(0,\xi)=\xi$. Then $q_\xi = \exp\!\big(\int_0^t u_x(s,q)\,ds\big) > 0$ and
$$m(t,q(t,\xi))\, q_\xi(t,\xi)^2 = m_0(\xi),$$
so $m$ keeps its sign along characteristics. Differentiating the nonlocal form along $q$ gives the Riccati-type law
$$\frac{d}{dt}\,u_x(t,q) = \tfrac12 u^2 - \tfrac12 u_x^2 - G*\big(u^2 + \tfrac12 u_x^2\big),$$
whence $\frac{d}{dt} u_x \le \tfrac12 u^2 - \tfrac12 u_x^2$, the engine of every breaking proof.

**Local theory.** For $u_0 \in H^s$, $s > 3/2$, there is a unique maximal solution $u \in C([0,T);H^s)\cap C^1([0,T);H^{s-1})$, and (Constantin–Escher) the solution persists as long as $\inf_x u_x$ stays bounded below — the **precise blow-up scenario**.

**Peakons.** $u(t,x) = c\,e^{-|x-ct|}$ is a weak solution with $m = 2c\,\delta_{x-ct}$; $N$-peakon superpositions $u=\sum_i p_i(t)e^{-|x-q_i(t)|}$ reduce CH to a finite-dimensional integrable Hamiltonian system with $H=\tfrac12\sum_{i,j}p_ip_je^{-|q_i-q_j|}$.

## 3. History & State of the Art (SOTA)

- **1993.** Camassa and Holm derive the equation as a model for unidirectional shallow-water waves with a bi-Hamiltonian structure, and exhibit the peaked soliton. (The equation appears earlier in Fokas–Fuchssteiner 1981 as a member of an integrable family.)
- **1998.** Constantin and Escher prove the precise blow-up scenario and the first sufficient conditions: breaking occurs if $m_0$ changes sign in a specific ordered way, or if $u_0'$ is sufficiently negative somewhere. *Wave breaking for nonlinear nonlocal shallow water equations*, Acta Math. 181.
- **2000.** Constantin–Escher determine the blow-up rate; Constantin gives a geometric (diffeomorphism-group) criterion in Ann. Inst. Fourier.
- **2000.** Xin and Zhang construct global weak (viscosity-limit, dissipative) solutions in $H^1$ for arbitrary data.
- **2004.** McKean gives a **necessary and sufficient** condition for breakdown in terms of the sign pattern of $m_0$ — the sharp answer to item (1).
- **2007.** Bressan and Constantin construct global **conservative** and global **dissipative** semigroups past breaking via a change to energy-based variables.
- **2015.** Bressan, Chen and Zhang prove **uniqueness** of conservative solutions by characterizing them via characteristics — removing the dependence on a particular construction.

SOTA: breaking is fully characterized; both post-breaking semigroups exist and are unique in their classes; generic-in-a-Baire-sense descriptions of the singularity structure are the current frontier.

## 4. Partial Results / Verified Cases

- **Precise blow-up scenario (all $s>3/2$).** Blow-up occurs iff $\inf_x u_x \to -\infty$; $\|u\|_{L^\infty}$ and $\|u\|_{H^1}$ stay bounded. (Constantin–Escher 1998.)
- **No breaking when $m_0$ has one sign.** If $m_0 = u_0-u_0'' \ge 0$ (or $\le 0$) on $\mathbb{R}$, the solution is global and $u$ stays positive (resp. negative); solitary waves and their smooth approximants are in this class.
- **Antisymmetric data.** If $u_0$ is odd with $u_0'(0)<0$, then $u_x(t,0)$ satisfies $\frac{d}{dt}u_x(0) \le -\tfrac12 u_x(0)^2$ exactly (the $u^2$ and convolution terms vanish at $x=0$ by symmetry), so breaking occurs by time $T \le -2/u_0'(0)$.
- **McKean's criterion (sharp).** Breakdown happens **iff** some portion of the positive part of $m_0$ lies to the *left* of some portion of its negative part — i.e. the wave "runs into itself". Otherwise the solution is global.
- **Blow-up rate.** $\displaystyle \lim_{t\to T^-} \big[(T-t)\,\inf_x u_x(t,\cdot)\big] = -2$, and the breaking set for the classical scenario is a single point moving along a characteristic (Constantin–Escher, Math. Z. 233, 2000).
- **Continuation.** For every $u_0 \in H^1(\mathbb{R})$ with $u_0 - u_{0,xx}$ a Radon measure — and indeed for all $u_0 \in H^1$ — there is a global conservative solution ($\|u(t)\|_{H^1}$ constant for a.e. $t$) and a global dissipative solution ($\|u(t)\|_{H^1}$ nonincreasing). Both depend continuously on data in suitable metrics; conservative solutions are unique.
- **Peakon–antipeakon.** The two-peakon system with $p_1=-p_2$ breaks at an explicit finite time with $u\equiv 0$ at the collision instant (see §10).

## 5. Principal Obstacles

- **Loss of the transport structure at breaking.** $m$ is a measure whose absolutely continuous part concentrates; at $t=T$ energy density $ (u^2+u_x^2)\,dx$ develops a singular part. Standard $H^s$ energy methods only give a continuation criterion, not the continuation.
- **Riccati inequality is one-sided.** $\frac{d}{dt}u_x \le \tfrac12 u^2 - \tfrac12 u_x^2$ proves blow-up under an initial sign hypothesis but gives no information about *which* data trigger it; the nonlocal term $G*(u^2+\tfrac12 u_x^2)$ is positive and can defeat the negative term for long times. Sharpness required McKean's integrable-structure argument (a spectral/sign analysis of $m$), not PDE estimates.
- **Non-uniqueness in the raw weak class.** In $H^1$-weak formulations there exist infinitely many continuations at a breaking time (all convex combinations of conservative/dissipative behaviour on separate characteristics). No entropy condition in the scalar-conservation-law sense selects one: CH is not a hyperbolic system with a convex entropy.
- **Loss of Lipschitz dependence.** The natural $H^1$ norm is *not* a metric in which the conservative flow is Lipschitz; one must build Finsler-type or optimal-transport metrics, in which the flow is only locally Lipschitz and the geometry is data-dependent.
- **Discontinuity of the semigroup structure.** Dissipative solutions form a semigroup that is not time-reversible and not continuous in $H^1$; uniqueness proofs cannot rely on Gronwall in a fixed Banach norm.

## 6. The Gap

Settled: characterization, rate, existence of both semigroups, uniqueness of the conservative one. The residual boundary is:

1. **Uniqueness in classes intermediate between conservative and dissipative** — a full classification of admissible continuations (a "selection principle" theorem) is missing.
2. **Generic structure of the singular set.** It is expected that for data in a generic (open dense / residual) subset of $H^1$ the breaking set is finite in space-time and the singularities are of two normal forms; a complete generic-regularity theorem for CH is at the frontier.
3. **Lipschitz metrics.** Whether a metric exists making the conservative flow *globally* Lipschitz on bounded energy sets, with explicit modulus, is unresolved.
4. **Higher-dimensional / two-component analogues.** For the two-component CH and $\mu$-CH systems, sharp necessary-and-sufficient breaking criteria of McKean type are not known.

## 7. Current Research (as of June 2026)

- **Penn State (Bressan and collaborators)** — generic regularity, Lipschitz metrics, and structural stability of conservative solutions to CH-type and variational wave equations. *(frontier — verify)* Extensions of the generic-singularity program from the variational wave equation to CH remain the most active line.
- **NTNU Trondheim (Holden, Raynaud and successors)** — Lagrangian coordinates, $\alpha$-dissipative interpolating semigroups, and convergent numerical schemes that reproduce conservative/dissipative behaviour through breaking.
- **Vienna / Lund (Constantin school; Lenells, Ehrnström)** — integrable structure, inverse scattering with singular $m$, and traveling-wave classification.
- **Uniqueness of dissipative solutions** has been argued via a Lagrangian-characteristics framework (Jamróz, Cieślak–Jamróz). *(frontier — verify)*
- **Two-component and $\mu$-CH systems** — sufficient breaking criteria proliferate; sharp criteria remain open.
- **Numerics** — multi-symplectic and Lagrangian-particle schemes for peakon–antipeakon interaction, tested against exact solutions.

## 8. Future Work

- Prove a **generic regularity theorem** for CH: for $u_0$ in a residual subset of $H^1$, singularities are isolated and of finitely many normal forms.
- Establish a **selection principle** (physical or variational) that singles out one continuation, analogous to entropy conditions for conservation laws.
- Build a metric in which the conservative semigroup is globally Lipschitz with an explicit constant, enabling error estimates for numerical schemes.
- Transfer McKean's sharp criterion to two-component CH, Degasperis–Procesi, and $\mu$-CH.
- Quantify **stability of breaking**: is the breaking time a continuous (or merely lower semicontinuous) function of $u_0$ in $H^1$?

## 9. Key References

- **[Foundational]** R. Camassa, D. D. Holm. *An integrable shallow water equation with peaked solitons.* Physical Review Letters 71 (1993), 1661–1664.
- **[Foundational]** A. Constantin, J. Escher. *Wave breaking for nonlinear nonlocal shallow water equations.* Acta Mathematica 181 (1998), 229–243.
- **[Foundational]** A. Constantin, J. Escher. *On the blow-up rate and the blow-up set of breaking waves for a shallow water equation.* Mathematische Zeitschrift 233 (2000), 75–91.
- **[SOTA]** H. P. McKean. *Breakdown of the Camassa–Holm equation.* Communications on Pure and Applied Mathematics 57 (2004), 416–418.
- **[SOTA]** A. Bressan, A. Constantin. *Global conservative solutions of the Camassa–Holm equation.* Archive for Rational Mechanics and Analysis 183 (2007), 215–239.
- **[SOTA]** A. Bressan, A. Constantin. *Global dissipative solutions of the Camassa–Holm equation.* Analysis and Applications 5 (2007), 1–27.
- **[SOTA / Recent]** A. Bressan, G. Chen, Q. Zhang. *Uniqueness of conservative solutions to the Camassa–Holm equation via characteristics.* Discrete and Continuous Dynamical Systems 35 (2015), 25–42.
- **[SOTA]** H. Holden, X. Raynaud. *Global conservative solutions of the Camassa–Holm equation — a Lagrangian point of view.* Communications in Partial Differential Equations 32 (2007), 1511–1549.
- **[SOTA]** Z. Xin, P. Zhang. *On the weak solutions to a shallow water equation.* Communications on Pure and Applied Mathematics 53 (2000), 1411–1433.
- **[Survey]** A. Constantin. *Nonlinear Water Waves with Applications to Wave–Current Interactions and Tsunamis.* CBMS-NSF Regional Conference Series in Applied Mathematics 81, SIAM, 2011.
- **[Survey]** A. Constantin, D. Lannes. *The hydrodynamical relevance of the Camassa–Holm and Degasperis–Procesi equations.* Archive for Rational Mechanics and Analysis 192 (2009), 165–186.

## 10. Worked Example / Concrete Special Case

**Peakon–antipeakon collision.** Take the two-peakon ansatz
$$u(t,x) = p_1(t)\,e^{-|x-q_1(t)|} + p_2(t)\,e^{-|x-q_2(t)|},$$
with Hamiltonian $H = \tfrac12\big(p_1^2+p_2^2+2p_1p_2 e^{-|q_1-q_2|}\big)$ and equations $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$.

Impose antisymmetry: $q_1 = -q_2 =: q > 0$, $p_1 = -p_2 =: p > 0$. Then $u$ is odd, $H = \tfrac12\cdot 2p^2 - p^2 e^{-2q} = p^2(1-e^{-2q})$ is conserved, and the reduced system is
$$\dot q = -p\big(1 - e^{-2q}\big)\cdot\frac{1}{?}\ \Longrightarrow\ \dot q = -p\big(1-e^{-2q}\big)^{0}\ \text{—compute directly:}\quad \dot q = p\big(e^{-2q} - 1\big)\cdot 1,\qquad \dot p = -p^2 e^{-2q}\cdot 2 \cdot \tfrac12 .$$

Concretely, writing $E := \|u\|_{H^1}^2 = 2H = 2p^2(1-e^{-2q})$ (constant), one gets from $\dot q = -p(1-e^{-2q})$:
$$\dot q = -\frac{E}{2p} .$$
Since $p^2 = \dfrac{E}{2(1-e^{-2q})} \to \infty$ as $q \to 0^+$ only if $E$ is fixed and $1-e^{-2q}\to 0$ — indeed $p \sim \sqrt{E/(4q)}$, so
$$\dot q \sim -\frac{E}{2}\sqrt{\frac{4q}{E}} = -\sqrt{E q}\quad\Longrightarrow\quad \sqrt{q}\ \text{decreases linearly},\ \ q(t) \sim \tfrac{E}{4}(T-t)^2 .$$
Hence $q$ reaches $0$ at a finite time $T$ while $p(t) \sim \sqrt{E/(4q)} \sim \dfrac{1}{T-t}$.

**Reading off the breaking.** At $x=0$ the odd solution has $u(t,0)=0$ for all $t$, and $\|u(t)\|_{L^\infty} \le \sqrt{E/2}$ stays bounded — no amplitude blow-up. But the slope between the peaks is
$$u_x(t,0) = -2p(t)\,e^{-q(t)} \sim -\frac{2}{T-t} \longrightarrow -\infty ,$$
matching the general rate $(T-t)\inf u_x \to -2$. At $t=T$ the profile collapses to $u(T,\cdot)\equiv 0$, and the entire energy $E$ has concentrated into a Dirac mass at the origin.

**The continuation dichotomy, explicit.** After $T$ there are two natural solutions of the same initial-value problem:
- *conservative*: the peakon and antipeakon pass through each other, $p$ decreasing from $+\infty$, $q$ growing again as $q(t)\sim \tfrac{E}{4}(t-T)^2$, with $\|u\|_{H^1}^2 = E$ for all $t \ne T$;
- *dissipative*: $u \equiv 0$ for $t \ge T$, with $\|u\|_{H^1}^2$ dropping from $E$ to $0$.

Both are weak solutions in $H^1$; neither is excluded by the equation alone. This single explicit example exhibits, in closed form, why wave breaking forces a *choice* of solution class — the content of §1(3) and the reason the Bressan–Constantin and Bressan–Chen–Zhang theorems are needed.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*