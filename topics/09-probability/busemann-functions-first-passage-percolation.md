---
id: 09-probability/busemann-functions-first-passage-percolation
title: "Uniqueness of Busemann Functions in First-Passage Percolation"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Uniqueness of Busemann Functions in First-Passage Percolation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/busemann-functions-first-passage-percolation` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(\tau_e)_{e \in E(\mathbb{Z}^d)}$ be i.i.d. non-negative edge weights and $T(x,y)$ the induced first-passage time. For a direction $\xi \in S^{d-1}$, the **Busemann function** in direction $\xi$ is the candidate limit

$$B_\xi(x,y) \;=\; \lim_{n \to \infty} \big( T(x, z_n) - T(y, z_n) \big), \qquad z_n/\|z_n\| \to \xi .$$

**Conjecture (uniqueness / existence of Busemann functions).** For every fixed $\xi$, under mild moment and continuity assumptions on the weight distribution, the limit exists almost surely, is independent of the choice of sequence $(z_n)$, and defines the unique (in law, among shift-covariant integrable cocycles with the correct mean) solution of the FPP recovery equation in direction $\xi$.

A complete resolution must either (a) prove a.s. convergence and uniqueness for a fixed direction under assumptions verifiable for a concrete weight law (e.g. $\tau_e \sim \mathrm{Exp}(1)$ on $\mathbb{Z}^2$), or (b) exhibit a distribution and a direction where two distinct Busemann-type cocycles with the same mean coexist, or where the subsequential limits genuinely differ.

The problem is equivalent, modulo standard arguments, to: *uniqueness and coalescence of semi-infinite geodesics in a fixed direction*, and it is the main missing input for the conjectured **non-existence of bi-infinite geodesics** (the "Benjamini–Kesten–Peres / Newman midpoint problem").

## 2. Mathematical Foundations

**Model.** $\Omega = [0,\infty)^{E(\mathbb{Z}^d)}$ with product measure $\mathbb{P} = \nu^{\otimes E}$, shifts $\theta_x$. Passage time of a lattice path $\gamma$: $T(\gamma) = \sum_{e \in \gamma} \tau_e$, and
$$T(x,y) = \inf\{ T(\gamma) : \gamma \text{ a path from } x \text{ to } y \}.$$
A **geodesic** is a path attaining the infimum; it exists a.s. when $\nu(\{0\}) < p_c(d)$.

**Shape theorem** (Cox–Durrett, Kesten). If $\mathbb{E}[\min\{\tau_{e_1},\dots,\tau_{e_{2d}}\}^d] < \infty$ then there is a deterministic norm-like $g$ with unit ball $\mathcal{B}$ compact and convex, and
$$\lim_{\|x\|\to\infty} \frac{|T(0,x) - g(x)|}{\|x\|} = 0 \quad \text{a.s.}$$
$g$ is homogeneous and subadditive: $g(x+y) \le g(x) + g(y)$.

**Cocycle formulation.** A measurable $B: \Omega \times \mathbb{Z}^d \times \mathbb{Z}^d \to \mathbb{R}$ is a **shift-covariant cocycle** if
$$B(x,y) + B(y,z) = B(x,z), \qquad B(\theta_w \omega; x,y) = B(\omega; x+w, y+w).$$
It **recovers** the weights if for every $x$
$$B(x, y) \le \tau_{\{x,y\}} \ \ \forall y \sim x, \qquad \min_{y \sim x} \big( \tau_{\{x,y\}} - B(x,y) \big) = 0 ,$$
i.e. $\tau_{\{x,y\}} = B(x,y)$ for at least one neighbour. Any Busemann limit satisfies these two identities: cocycle from telescoping, recovery from $T(x,z) = \min_{y\sim x}(\tau_{\{x,y\}} + T(y,z))$.

**Asymptotic velocity.** If $B$ is ergodic and integrable, $\mathbb{E}[B(0,x)] = -h(x)$ for a linear $h$, and the Busemann function in direction $\xi$ should satisfy $h = $ the supporting linear functional of $\mathcal{B}$ at $\xi$, so
$$\mathbb{E}\,B_\xi(0,x) = \nabla g(\xi)\cdot x \quad \text{when } g \text{ is differentiable at } \xi .$$
Uniqueness is the claim that this mean condition pins down $B$ uniquely a.s.

**Newman's curvature hypothesis.** $\partial\mathcal{B}$ is uniformly curved: there is $\kappa < \infty$ with $\mathcal{B} \subseteq B(z, \kappa)$ for every ball of radius $\kappa$ containing... formally, every boundary point admits an inscribed sphere of radius $\kappa$. This is unproven for *every* non-degenerate $\nu$.

## 3. History & State of the Art (SOTA)

- **1965.** Hammersley–Welsh introduce FPP; subadditive ergodic theory gives $g$.
- **1995–96.** Newman's ICM survey *A surface view of first-passage percolation* formulates the geodesic program: under curvature plus exponential moments, every semi-infinite geodesic has a direction and geodesics in a fixed direction coalesce (Licea–Newman, *Ann. Probab.* 1996; Newman 1995). Busemann functions appear as the tool converting geodesic coalescence into a stationary cocycle.
- **2005–08.** Hoffman removes curvature at the price of weaker conclusions: *Coexistence for Richardson type competing spatial growth models* (2005) and *Geodesics in first passage percolation* (*Ann. Appl. Probab.* 2008) construct Busemann-like subadditive limits and prove existence of at least $4$ distinct semi-infinite geodesics in $d=2$.
- **2014.** Damron–Hanson, *Busemann functions and infinite geodesics in two-dimensional first-passage percolation* (*Comm. Math. Phys.* 325): build **Busemann increment distributions** as weak subsequential limits on a compactified space, giving cocycles with all recovery/covariance properties without curvature — but only in distribution, and without uniqueness.
- **2016–17.** Ahlberg–Hoffman, *Random coalescing geodesics in first-passage percolation*: for **Lebesgue-a.e.** direction, geodesics coalesce and the direction-indexed geodesic measure is unique. Auffinger–Damron–Hanson's monograph *50 Years of First-Passage Percolation* (AMS, 2017) codifies the state of the art.
- **2017–20.** Exactly solvable side: Georgiou–Rassoul-Agha–Seppäläinen (*PTRF* 2017) construct the full family of stationary cocycles for the exponential corner growth model; Seppäläinen (*AIHP* 2020) gives a self-contained existence/uniqueness/coalescence proof there.
- **2020–22.** Non-existence of bi-infinite geodesics proved in exponential LPP by Balázs–Busani–Seppäläinen (*Forum Math. Sigma* 2020) and independently Basu–Hoffman–Sly (*Comm. Math. Phys.* 2022) — both use integrability, not general FPP arguments.
- **2024.** Busani–Seppäläinen–Sorensen, *The stationary horizon and semi-infinite geodesics in the directed landscape*: complete classification of Busemann limits in the KPZ scaling limit, including the exceptional-direction structure.

**Status:** open for general i.i.d. FPP in every $d \ge 2$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $\mathbb{Z}^2$, curvature + exponential moments | $B_\xi$ exists, unique, geodesics coalesce | Licea–Newman 1996; Newman 1995 |
| $\mathbb{Z}^2$, general $\nu$ with $\nu(\{0\})<p_c$, continuous | Busemann *increment distributions* exist as subsequential limits; if $\partial\mathcal{B}$ is differentiable at $\xi$ and $\xi$ is exposed, geodesic directions are asymptotically $\xi$ | Damron–Hanson 2014, 2017 |
| $\mathbb{Z}^2$, Lebesgue-a.e. $\xi$ | unique coalescing geodesic measure; Busemann limit exists for a.e. direction | Ahlberg–Hoffman 2016 |
| $\mathbb{Z}^d$, $d \ge 2$, general | non-existence of bigeodesics with two prescribed *fixed* directions of differentiability | Alexander, *Geodesics, bigeodesics, and coalescence in FPP in general dimension* (2020s) |
| Exponential corner growth model (LPP, $d=2$) | full one-parameter family $\{B^\rho\}_{\rho\in(0,1)}$ exists, explicit product-form marginals; unique for each fixed $\rho$; discontinuity set countable and random | GRAS 2017; Seppäläinen 2020 |
| Directed landscape / KPZ limit | Busemann process = stationary horizon; exceptional directions fully classified | Busani–Seppäläinen–Sorensen 2024 |
| Trees, $\mathbb{Z}\times\{1,\dots,K\}$ strips, Poisson LPP | uniqueness by direct computation / Burke property | Cator–Pimentel 2012 |

Uniqueness therefore holds where either **exact solvability** or an **unproven curvature axiom** is available.

## 5. Principal Obstacles

- **No curvature theorem.** For no single non-degenerate i.i.d. weight law is $\partial \mathcal{B}$ known to be differentiable at a single point, let alone uniformly curved. Newman-type arguments (Licea–Newman) need curvature to force geodesic wandering exponent $< 1$ and hence coalescence; without it the transversal fluctuation estimate $|\gamma_n| = o(n)$ is unavailable.
- **Flat edges are real.** For Bernoulli weights with $\nu(\{0\}) = p$ close to $p_c$, $\partial\mathcal{B}$ provably contains flat segments (Durrett–Liggett, Marchand). In a flat direction the supporting functional is non-unique, so the mean condition of §2 cannot select a single cocycle; a family of distinct cocycles is expected.
- **Weak limits lose a.s. information.** Damron–Hanson build cocycles as limits *in distribution* on a compactified path space. Uniqueness in law of the increment field does not imply the a.s. limit $T(x,z_n)-T(y,z_n)$ converges; passing from distributional tightness to almost-sure convergence is exactly the missing step.
- **No integrability.** All complete proofs (exponential LPP, Poisson LPP, directed landscape) use the Burke/queueing property, a distributional invariance with no analogue for general $\nu$. There is no known "soft" replacement.
- **Ergodicity of the Busemann field.** Even given existence, one must show the cocycle is measurable with respect to the weight $\sigma$-field and ergodic under shifts; extremality arguments (Ahlberg–Hoffman) currently deliver this only after averaging over directions, which is why a.e.-$\xi$ statements are the ceiling.

## 6. The Gap

Proven: for a.e. $\xi$ (Ahlberg–Hoffman) or under curvature (Newman), uniqueness holds; and for every $\xi$ a *distributional* cocycle exists (Damron–Hanson).

Missing: promoting "a.e. direction" to "every direction" and "distributional limit" to "a.s. limit", for a *fixed* weight law. Concretely, the single open step is:

> Show that for fixed $\xi$ and continuous $\nu$ with $\mathbb{E}\tau^{2+\epsilon}<\infty$, any two shift-covariant, integrable, recovering cocycles $B, B'$ with the same mean vector satisfy $B = B'$ a.s. — equivalently, that the set of Busemann measures in direction $\xi$ is a singleton.

Everything else (bigeodesic non-existence, coalescence, the midpoint problem in general FPP) follows from standard arguments once this is available. The barrier is that the natural comparison $B \le B'$ or $\ge$ (available in LPP via monotone couplings of the stationary cocycle family in $\rho$) has no general-FPP counterpart, because the family $\{B_\xi\}$ is not known to be monotone in $\xi$.

## 7. Current Research (as of June 2026)

- **Seppäläinen's group (Wisconsin) and Busani (Bristol/IMPA), Sorensen (Toronto).** Stationary-horizon program: extend the classification of Busemann processes from the directed landscape down to pre-limit models, hoping universality arguments transfer uniqueness. *(frontier — verify)*
- **Damron and collaborators (Georgia Tech).** Structural FPP: quantitative geodesic coalescence without curvature; sharper versions of the 2014 increment construction with a.s. convergence along sparse subsequences. *(frontier — verify)*
- **Basu, Sly, and the KPZ-integrability school (ICTS Bangalore, Caltech).** Transferring the geometric bigeodesic arguments of Basu–Hoffman–Sly to models with weaker integrability (e.g. LPP with general weights), aimed at removing the exact-solvability crutch.
- **Ahlberg (Stockholm).** Ergodic-theoretic treatment of the direction-indexed geodesic measures, with the aim of shrinking the exceptional direction set from Lebesgue-null to empty.
- **Alexander (USC).** Higher-dimensional coalescence and bigeodesic exclusion in $d \ge 3$, where even Hoffman-type multiplicity results are weaker.

## 8. Future Work

- Prove **any** non-trivial curvature or differentiability statement for $\partial\mathcal{B}$ for a specific i.i.d. law; this alone unlocks Newman's program.
- Develop a **monotone coupling** of Busemann cocycles across directions in general FPP, replicating the $\rho$-monotonicity of the exponential model; monotonicity plus continuity of the mean would give uniqueness off a countable set immediately.
- Establish an FPP analogue of the **Burke property** in an approximate/perturbative sense (e.g. for weights near exponential).
- Settle the **flat-edge case** deliberately: characterise the full set of Busemann cocycles in a flat direction for supercritical Bernoulli weights, as a proof-of-concept that non-uniqueness is exactly a flat-edge phenomenon.
- Prove absence of bi-infinite geodesics in $d=2$ FPP unconditionally — currently known only under curvature (Damron–Hanson 2017) or in integrable LPP.

## 9. Key References

- **[Foundational]** C. M. Newman. *A surface view of first-passage percolation.* Proceedings of the ICM (Zürich 1994), Birkhäuser, 1995, pp. 1017–1023.
- **[Foundational]** C. Licea, C. M. Newman. *Geodesics in two-dimensional first-passage percolation.* Annals of Probability 24(1):399–410, 1996.
- **[Foundational]** C. Hoffman. *Geodesics in first passage percolation.* Annals of Applied Probability 18(5):1944–1969, 2008.
- **[Foundational]** C. Hoffman. *Coexistence for Richardson type competing spatial growth models.* Annals of Applied Probability 15(1B):739–747, 2005.
- **[SOTA]** M. Damron, J. Hanson. *Busemann functions and infinite geodesics in two-dimensional first-passage percolation.* Communications in Mathematical Physics 325(3):917–963, 2014.
- **[SOTA]** M. Damron, J. Hanson. *Bigeodesics in first-passage percolation.* Communications in Mathematical Physics 349(2):753–776, 2017.
- **[SOTA]** D. Ahlberg, C. Hoffman. *Random coalescing geodesics in first-passage percolation.* arXiv:1609.02447, 2016.
- **[SOTA]** N. Georgiou, F. Rassoul-Agha, T. Seppäläinen. *Stationary cocycles and Busemann functions for the corner growth model.* Probability Theory and Related Fields 169:177–222, 2017.
- **[SOTA]** T. Seppäläinen. *Existence, uniqueness and coalescence of directed planar geodesics: proof via the increment-stationary growth process.* Annales de l'IHP Probabilités et Statistiques 56(3):1775–1791, 2020.
- **[SOTA]** M. Balázs, O. Busani, T. Seppäläinen. *Non-existence of bi-infinite geodesics in the exponential corner growth model.* Forum of Mathematics, Sigma 8, e46, 2020.
- **[SOTA]** R. Basu, C. Hoffman, A. Sly. *Nonexistence of bigeodesics in planar exponential last passage percolation.* Communications in Mathematical Physics 389:1–30, 2022.
- **[SOTA]** O. Busani, T. Seppäläinen, E. Sorensen. *The stationary horizon and semi-infinite geodesics in the directed landscape.* Annals of Probability 52(1), 2024.
- **[Related]** E. Cator, L. P. R. Pimentel. *Busemann functions and equilibrium measures in last passage percolation models.* Probability Theory and Related Fields 154:89–125, 2012.
- **[Survey]** A. Auffinger, M. Damron, J. Hanson. *50 Years of First-Passage Percolation.* AMS University Lecture Series 68, 2017.
- **[Survey]** C. Janjigian, F. Rassoul-Agha. *Busemann functions and semi-infinite geodesics in a random environment.* Annales de l'IHP Probabilités et Statistiques 56(1):373–430, 2020.

## 10. Worked Example / Concrete Special Case

**Exponential corner growth model, $d=2$.** Take i.i.d. $\omega_x \sim \mathrm{Exp}(1)$ on vertices of $\mathbb{Z}^2_{\ge 0}$ and last-passage times $G(0,x) = \max_{\pi} \sum_{v \in \pi} \omega_v$ over up-right paths. Here the shape function is known exactly (Rost):
$$g(x_1,x_2) = (\sqrt{x_1} + \sqrt{x_2})^2 .$$

Fix $\rho \in (0,1)$. The Busemann cocycle $B^\rho$ has the explicit description: the increments
$$I_x = B^\rho(x, x+e_1), \qquad J_x = B^\rho(x, x+e_2)$$
satisfy, for each fixed $x$, $I_x \sim \mathrm{Exp}(1-\rho)$ and $J_x \sim \mathrm{Exp}(\rho)$, **independent**.

*Check the recovery equation.* In LPP recovery reads $\omega_x = I_x \wedge J_x$. For independent exponentials,
$$\mathbb{P}(I_x \wedge J_x > t) = e^{-(1-\rho)t} e^{-\rho t} = e^{-t},$$
so $I_x \wedge J_x \sim \mathrm{Exp}(1)$ — exactly the weight law. The Burke property upgrades this pointwise identity to the statement that $(\omega_x)$ recovered this way is again i.i.d. $\mathrm{Exp}(1)$, which is what makes the construction consistent.

*Check the mean/shape relation.* By the cocycle property, for $x = (x_1,x_2)$ with $x_1,x_2 \ge 0$,
$$\mathbb{E}\,B^\rho(0,x) = \frac{x_1}{1-\rho} + \frac{x_2}{\rho}.$$
Minimising over $\rho$: $\frac{d}{d\rho}\big[\frac{x_1}{1-\rho} + \frac{x_2}{\rho}\big] = \frac{x_1}{(1-\rho)^2} - \frac{x_2}{\rho^2} = 0$, giving
$$\rho^\ast = \frac{\sqrt{x_2}}{\sqrt{x_1}+\sqrt{x_2}}, \qquad \frac{x_1}{1-\rho^\ast} + \frac{x_2}{\rho^\ast} = (\sqrt{x_1}+\sqrt{x_2})^2 = g(x).$$
So the family $\{B^\rho\}$ is the Legendre-dual parametrisation of $\partial\mathcal{B}$, and $\rho$ is in bijection with the direction
$$\xi(\rho) = \frac{\big((1-\rho)^2,\ \rho^2\big)}{(1-\rho)^2 + \rho^2}.$$

*Where uniqueness lives.* Because $g$ here is **strictly concave** on the simplex, each direction $\xi$ has exactly one supporting parameter $\rho$, and Seppäläinen (2020) shows $B^{\rho-} = B^{\rho+}$ a.s. for each fixed $\rho$; the random set of $\rho$ where the left and right limits differ is countable and dense, and misses any deterministic $\rho$ almost surely. Uniqueness holds.

*Where it should fail.* Replace the weights by Bernoulli FPP weights $\tau_e \in \{a, b\}$ with $\mathbb{P}(\tau_e = a) = p > \vec{p}_c$. Then $\partial\mathcal{B}$ contains a genuine flat segment around the axis direction (Durrett–Liggett; Marchand). On that segment the supporting linear functional $h$ is constant across a whole arc of directions $\xi$, so the mean condition $\mathbb{E}B_\xi(0,x) = h(x)$ cannot distinguish the cocycles associated to different $\xi$ in the arc. Whether the resulting Busemann cocycles genuinely coincide or form a non-trivial family is precisely the open question of §6 — and the contrast between these two lines is the whole content of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*