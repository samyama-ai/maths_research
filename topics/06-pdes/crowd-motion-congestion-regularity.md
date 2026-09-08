---
id: 06-pdes/crowd-motion-congestion-regularity
title: "Regularity of Solutions to the Monge-Kantorovich Flow with Congestion"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Regularity of Solutions to the Monge-Kantorovich Flow with Congestion

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/crowd-motion-congestion-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the macroscopic crowd-motion model of Maury–Roudneff-Chupin–Santambrogio: a population density $\rho_t$ on a domain $\Omega \subset \mathbb{R}^d$ is transported by a desired velocity field $u = -\nabla V$, subject to the hard congestion constraint $\rho \le 1$. The evolution is the Wasserstein gradient flow of $V$ restricted to the constraint set, and admits the formal PDE description

$$\partial_t \rho + \nabla\cdot\big(\rho\,(-\nabla V - \nabla p)\big) = 0, \qquad p \ge 0, \quad \rho \le 1, \quad p\,(1-\rho) = 0 .$$

The field $p$ is the *pressure*: the Lagrange multiplier of the constraint, supported on the saturated (congested) zone $\{\rho = 1\}$.

**Open problem.** Determine the optimal regularity of $(\rho, p)$ for the first-order (non-diffusive) flow in dimension $d \ge 2$:

1. **(P1) Pressure integrability.** Is $p \in L^\infty_{\mathrm{loc}}((0,T)\times\Omega)$, or even continuous, for $V$ smooth (say $C^\infty$ and $\lambda$-convex) and $\rho_0 = \mathbf{1}_\omega$ with $\omega$ smooth and bounded? Currently $p$ is only known to exist as a measure, or in $L^2_t H^1_x$ under added diffusion.
2. **(P2) Patch persistence and free-boundary regularity.** If $\rho_0 = \mathbf{1}_\omega$, does $\rho_t = \mathbf{1}_{\omega_t}$ persist for all $t>0$ with $\partial\omega_t$ rectifiable, and is $\partial\{\rho_t = 1\}$ smooth away from a closed singular set of codimension $\ge 1$?
3. **(P3) Time regularity.** Is $t \mapsto p(t,\cdot)$ of bounded variation, or does the topological merging of congested blobs force genuinely non-BV pressure jumps?

A complete solution of (P1) means either a proof of a local $L^\infty$ (or modulus-of-continuity) bound depending only on $\|V\|_{C^2}$, $d$, and $\operatorname{diam}\Omega$, or an explicit counterexample with smooth data and unbounded pressure. A solution of (P2) means an $\varepsilon$-regularity theorem for the free boundary or a counterexample producing a non-rectifiable interface in finite time.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^d$ be convex, bounded, with $|\Omega| > 1$. Write $\mathcal{P}(\Omega)$ for Borel probability measures and $W_2$ for the quadratic Wasserstein distance,

$$W_2^2(\mu,\nu) \;=\; \min_{\gamma \in \Pi(\mu,\nu)} \int_{\Omega\times\Omega} |x-y|^2 \, d\gamma(x,y).$$

Define the admissible set
$$K \;=\; \{ \rho \in \mathcal{P}(\Omega) : \rho \le \mathcal{L}^d,\ \text{i.e. } \rho = f\,dx \text{ with } 0 \le f \le 1 \},$$
a $W_2$-geodesically convex, weakly compact subset of $\mathcal{P}(\Omega)$.

**Variational formulation (JKO scheme).** For step $\tau>0$ set $\rho^0_\tau = \rho_0 \in K$ and
$$\rho^{k+1}_\tau \;\in\; \operatorname*{arg\,min}_{\rho \in K} \; \Big\{ \int_\Omega V \, d\rho \;+\; \frac{1}{2\tau} W_2^2(\rho, \rho^k_\tau) \Big\}.$$
Each step is strictly convex in $\rho$, so the minimizer is unique. As $\tau \to 0$, $\rho_\tau \to \rho$ locally uniformly in $W_2$, and $\rho$ is the unique gradient flow of $\mathcal{F} = \int V d\rho + \iota_K(\rho)$ in the sense of Ambrosio–Gigli–Savaré, since $\mathcal{F}$ is $\lambda$-convex along generalized geodesics when $V$ is $\lambda$-convex.

**Dual / pressure formulation.** The first-order optimality condition of the JKO step gives a Kantorovich potential $\varphi^{k+1}$ and a pressure $p^{k+1} \ge 0$ with
$$\frac{\varphi^{k+1}}{\tau} + V + p^{k+1} = \text{const on } \{\rho^{k+1} > 0\}, \qquad p^{k+1} = 0 \text{ on } \{\rho^{k+1} < 1\}.$$
Passing to the limit yields the continuity equation with velocity $v = -\nabla V - \nabla p$ and the complementarity system of Section 1. Equivalently, $v_t = P_{C_{\rho_t}}(-\nabla V)$, where
$$C_\rho \;=\; \overline{\{\nabla q : q \in H^1(\Omega),\ q \ge 0,\ q = 0 \text{ a.e. on } \{\rho<1\}\}}^{\,\perp \, L^2_\rho}$$
is the cone of *admissible* (non-compressing on the saturated zone) velocities; $P$ is the $L^2_\rho$-projection. On $\{\rho = 1\}$ the constraint $\nabla\cdot v = 0$ forces the elliptic problem
$$-\Delta p \;=\; \Delta V \quad \text{in } \{\rho_t = 1\}^\circ, \qquad p = 0 \text{ on } \partial\{\rho_t = 1\},$$
i.e. an *obstacle-type free boundary problem posed on an unknown, time-dependent set*.

**Soft-congestion approximation.** The flow arises as the $m\to\infty$ limit of porous-medium/Hele-Shaw dynamics
$$\partial_t \rho_m = \nabla\cdot(\rho_m \nabla V) + \Delta \rho_m^m, \qquad p_m = \tfrac{m}{m-1}\rho_m^{m-1},$$
which is the standard route to $L^\infty$ pressure bounds in the diffusive setting (Perthame–Quirós–Vázquez).

## 3. History & State of the Art (SOTA)

- **2010.** Maury, Roudneff-Chupin and Santambrogio introduce the macroscopic model as a $W_2$ gradient flow with the constraint $\rho \le 1$, prove existence and uniqueness of the flow, and identify the pressure as the multiplier (M3AS 20, 1787–1821).
- **2011.** Maury, Roudneff-Chupin, Santambrogio and Venel connect the macroscopic model to the microscopic granular (sweeping-process) model of Maury–Venel; the pressure appears as the contact-force limit.
- **2014.** Alexander, Kim and Yao study the quasi-static (Hele-Shaw) regime of congested crowd transport and prove patch persistence and regularity of the interface in that scaling (Nonlinearity 27, 823–858).
- **2016.** De Philippis, Mészáros, Santambrogio and Velichkov prove BV estimates propagate along the JKO scheme: $\mathrm{TV}(\rho_t) \le e^{Ct}\,\mathrm{TV}(\rho_0)$ with $C = C(\|D^2V\|_\infty)$ (ARMA 219, 829–860). This is the strongest general density estimate available.
- **2016.** Mészáros and Santambrogio treat the diffusive analogue $\partial_t\rho - \Delta\rho + \nabla\cdot(\rho(-\nabla V - \nabla p)) = 0$ and obtain $p \in L^2_t H^1_x$ (Anal. PDE 9, 615–644) — diffusion buys Sobolev pressure that the first-order flow lacks.
- **2016.** Cardaliaguet, Mészáros and Santambrogio show that in first-order mean field games with density constraints the multiplier "$p$ = price" is only a measure in general, with $L^\infty$/BV improvements under structural assumptions (SIAM J. Control Optim. 54, 2672–2709).
- **2018–2021.** Craig–Kim–Yao (ARMA 227, 1–67) obtain patch solutions for congested aggregation with Newtonian interaction; Jacobs–Kim–Tong develop $L^\infty$ pressure and stability theory for Darcy's law with a source.

The parallel *traffic-congestion* strand — where "congestion" enters as a superlinear metric cost rather than a hard density cap — is far better understood: Carlier–Jimenez–Santambrogio (SICON 2008) and Brasco–Carlier–Santambrogio (JMPA 2010) reduce Wardrop equilibria to the very degenerate elliptic equation $\nabla\cdot\big((|\nabla u|-1)_+ \tfrac{\nabla u}{|\nabla u|}\big) = f$, and Colombo–Figalli (JMPA 2014) prove $(|\nabla u|-1)_+ \nabla u / |\nabla u| \in C^{0,\alpha}_{\mathrm{loc}}$ in all dimensions.

## 4. Partial Results / Verified Cases

- **Dimension $d = 1$, all data.** Solutions are explicit: $\rho_t$ is a finite (or countable) union of saturated intervals plus a subcritical part; on each saturated interval $-p'' = V''$ with zero boundary data, so $p$ is piecewise $C^2$ and globally Lipschitz. Uniqueness and stability follow via monotone rearrangement (Di Marino–Mészáros, M3AS 26, 2016).
- **Diffusive case, all $d$.** With nondegenerate diffusion: $\rho \in L^2_t H^1_x$, $p \in L^2_t H^1_x$, and $\rho \in C([0,T];L^q)$ (Mészáros–Santambrogio 2016). Second-order MFG with density constraints inherit the same $H^1$ pressure (Mészáros–Silva, JMPA 2015).
- **BV propagation, all $d$.** $V \in C^{1,1}$, $\Omega$ convex, $\rho_0 \in BV$ $\Rightarrow$ $\rho_t \in BV$ with exponential-in-time bound (De Philippis–Mészáros–Santambrogio–Velichkov 2016). In particular $\rho_0 = \mathbf{1}_\omega$ with $\omega$ of finite perimeter keeps finite perimeter level sets.
- **Quasi-static / Hele-Shaw scaling, $d\ge2$.** Patch solutions persist and the free boundary is regular for star-shaped or Lipschitz initial patches under a strict-drift condition (Alexander–Kim–Yao 2014; Kim–Požár, Trans. AMS 370, 2018, for viscosity theory).
- **Newtonian aggregation drift, $d\ge2$.** $\rho_0 = \mathbf{1}_\omega$ stays a patch for all time; pressure is bounded on compact time intervals (Craig–Kim–Yao 2018).
- **Radial / self-similar data.** For $V(x) = |x|^2/2$ and $\rho_0 = \mathbf{1}_{B_R}$ the solution is an explicitly computable shrinking ball with quadratic pressure profile; $p$ is Lipschitz but never $C^1$ across the interface.
- **Congested traffic (soft congestion), all $d$.** Optimal $C^{0,\alpha}$ regularity of the flux is proved (Colombo–Figalli 2014), with $W^{1,p}$/continuity refinements in $d=2$ (Santambrogio–Vespri, Nonlinear Anal. 73, 2010).

## 5. Principal Obstacles

- **No smoothing mechanism.** The first-order flow is pure transport: the velocity is $L^2$ in time by the energy-dissipation identity and nothing more. Parabolic regularity theory, De Giorgi–Nash–Moser iteration, and heat-kernel arguments all require the diffusion that the hard-congestion model deletes.
- **The multiplier has no maximum principle.** $p$ solves $-\Delta p = \Delta V$ on the *unknown* set $\{\rho=1\}$, whose boundary can be arbitrarily rough at a given instant; the standard obstacle-problem machinery (Caffarelli's $C^{1,\alpha}$ free boundary theory) does not apply because the contact set is not the coincidence set of a fixed variational inequality — it is dragged along by the flow.
- **Topological changes.** Two saturated blobs approaching each other merge in finite time; at the merging instant the elliptic problem for $p$ changes domain discontinuously, so $p(t,\cdot)$ jumps in $L^\infty$. Whether the total variation in time of these jumps is finite is exactly (P3), and no compactness argument controls the number of merges.
- **Non-differentiability of the projection.** The constraint set $K$ has an "edge" at every saturated configuration: $\rho \mapsto P_K(\rho)$ is 1-Lipschitz in $W_2$ but nowhere differentiable, so linearization/perturbation of the flow around a solution is unavailable. Convexity of $\iota_K$ gives contraction ($W_2$ stability) but contraction gives no gain of derivatives.
- **Degeneracy on a set of positive measure.** In the traffic-congestion formulation, the operator is elliptic only where $|\nabla u| > 1$; it degenerates on a fat set, defeating classical Schauder and Krylov–Safonov estimates. Colombo–Figalli circumvented this by regularity of the *flux* rather than of $\nabla u$ — an argument with no known analogue for the hard-constraint flow.
- **BV is not enough.** BV control of $\rho$ gives no pointwise information on $\partial\{\rho=1\}$: a set of finite perimeter has a rectifiable reduced boundary, but the topological boundary can have positive measure, which is compatible with unbounded pressure.

## 6. The Gap

Proven (Section 4): $\rho_t \in BV$ with exponential bound; $p$ exists as a nonnegative distribution/measure; full regularity in $d=1$; $H^1$ pressure once diffusion is added; regularity in the quasi-static limit where time derivatives are dropped.

Claimed (Section 1): a *pointwise* bound on $p$ and a *structural* description of $\{\rho=1\}$ for the genuinely dynamic, non-diffusive flow in $d \ge 2$.

The precise missing step: an estimate of the form
$$\|p(t,\cdot)\|_{L^\infty} \;\le\; C\big(d, \|V\|_{C^{1,1}}, \operatorname{diam}\Omega\big)$$
uniform in $t$ and in the JKO step $\tau$. Every known route to such a bound uses either (i) the comparison principle for the porous-medium approximation, which requires $\Delta V$ to have a sign, or (ii) an $H^1$ bound from diffusion. Removing both hypotheses simultaneously is the barrier. Equivalently: control the geometry of $\{\rho_t = 1\}$ well enough that the Dirichlet problem $-\Delta p = \Delta V$ on it satisfies a uniform Wiener-type exterior-density condition — but the flow itself is the only source of such geometric information, making the argument circular.

## 7. Current Research (as of June 2026)

- **Lyon (Santambrogio, Institut Camille Jordan)** and **Durham (Mészáros)** continue the JKO/BV programme, pushing toward Sobolev estimates on $p$ under structural assumptions on $\Delta V$. *(frontier — verify)* recent work targets $p \in L^\infty_t BV_x$ for star-shaped saturated zones.
- **UCLA / ISTA (I. Kim, Y. Yao)** and collaborators develop viscosity-solution and patch-persistence theory for Hele-Shaw-type congested flows, including tumour-growth models where the same complementarity condition $p(1-\rho)=0$ appears with a source term.
- **UCSB / Purdue (M. Jacobs)** combines the back-and-forth method for numerical $W_2$ projections with rigorous $L^\infty$ pressure estimates for Darcy's law with a source; this is currently the most promising analytic route to (P1).
- **ETH Zürich (Figalli)** and the free-boundary school pursue $\varepsilon$-regularity for degenerate/very degenerate operators, feeding the traffic-congestion strand.
- **Numerics.** Entropic-regularized and back-and-forth JKO solvers produce high-resolution pressure fields; simulations consistently show bounded, apparently Lipschitz pressure with corner singularities at merging events — consistent with, but not proof of, a positive answer to (P1). *(frontier — verify)*

## 8. Future Work

- Prove or disprove a uniform $L^\infty$ pressure bound by transferring the Perthame–Quirós–Vázquez complementarity estimate to the $m\to\infty$ limit *without* a sign condition on $\Delta V$.
- Establish quantitative geometric control of $\{\rho_t=1\}$: an interior-density or exterior-cone estimate propagating in time, which would immediately give barriers for $p$.
- Develop an $\varepsilon$-regularity theorem for the free boundary in the spirit of Alt–Caffarelli, adapted to a moving contact set with a transport (not variational-inequality) structure.
- Settle (P3) by constructing an explicit example with infinitely many merging events in finite time, testing whether $t \mapsto p$ can fail to be BV.
- Extend the theory to nonlocal/interaction drifts $V = W * \rho$ and to multi-species crowd models, where even existence of the pressure is delicate.

## 9. Key References

- **[Foundational]** B. Maury, A. Roudneff-Chupin, F. Santambrogio. *A macroscopic crowd motion model of gradient flow type.* Mathematical Models and Methods in Applied Sciences, 20(10):1787–1821, 2010.
- **[Foundational]** L. Ambrosio, N. Gigli, G. Savaré. *Gradient Flows in Metric Spaces and in the Space of Probability Measures.* Birkhäuser, 2nd edition, 2008.
- **[Foundational]** B. Maury, A. Roudneff-Chupin, F. Santambrogio, J. Venel. *Handling congestion in crowd motion modeling.* Networks and Heterogeneous Media, 6(3):485–519, 2011.
- **[SOTA / Recent]** G. De Philippis, A. R. Mészáros, F. Santambrogio, B. Velichkov. *BV estimates in optimal transportation and applications.* Archive for Rational Mechanics and Analysis, 219:829–860, 2016.
- **[SOTA / Recent]** A. R. Mészáros, F. Santambrogio. *Advection–diffusion equations with density constraints.* Analysis & PDE, 9(3):615–644, 2016.
- **[SOTA / Recent]** P. Cardaliaguet, A. R. Mészáros, F. Santambrogio. *First order mean field games with density constraints: pressure equals price.* SIAM Journal on Control and Optimization, 54(5):2672–2709, 2016.
- **[SOTA / Recent]** K. Craig, I. Kim, Y. Yao. *Congested aggregation via Newtonian interaction.* Archive for Rational Mechanics and Analysis, 227:1–67, 2018.
- **[SOTA / Recent]** D. Alexander, I. Kim, Y. Yao. *Quasi-static evolution and congested crowd transport.* Nonlinearity, 27(4):823–858, 2014.
- **[SOTA / Recent]** M. Colombo, A. Figalli. *Regularity results for very degenerate elliptic equations.* Journal de Mathématiques Pures et Appliquées, 101(1):94–117, 2014.
- **[SOTA / Recent]** B. Perthame, F. Quirós, J. L. Vázquez. *The Hele-Shaw asymptotics for mechanical models of tumor growth.* Archive for Rational Mechanics and Analysis, 212:93–127, 2014.
- **[Survey]** F. Santambrogio. *Crowd motion and evolution PDEs under density constraints.* ESAIM: Proceedings and Surveys, 64:137–157, 2018.
- **[Survey]** F. Santambrogio. *Optimal Transport for Applied Mathematicians.* Birkhäuser, Progress in Nonlinear Differential Equations and Their Applications 87, 2015.
- **[Related]** L. Brasco, G. Carlier, F. Santambrogio. *Congested traffic dynamics, weak flows and very degenerate elliptic equations.* Journal de Mathématiques Pures et Appliquées, 93(6):652–671, 2010.
- **[Related]** S. Di Marino, A. R. Mészáros. *Uniqueness issues for evolution equations with density constraints.* Mathematical Models and Methods in Applied Sciences, 26(9):1761–1783, 2016.

## 10. Worked Example / Concrete Special Case

**Setting.** $d = 1$, $\Omega = \mathbb{R}$, $V(x) = x^2/2$ (drift $-\nabla V = -x$ pulls everyone to the origin), initial datum $\rho_0 = \mathbf{1}_{[c_0-\frac12,\,c_0+\frac12]}$ with $c_0 > 0$. Mass is $1$ and the datum is already saturated.

**Ansatz.** $\rho_t = \mathbf{1}_{[c(t)-\frac12,\, c(t)+\frac12]}$; the constraint $\rho \le 1$ plus mass conservation forces the support to be an interval of length exactly $1$ as long as no splitting occurs.

**Step 1 — incompressibility.** On the saturated zone $\partial_t\rho = 0$, so the continuity equation gives $\partial_x v = 0$: the velocity is a constant $\dot c(t)$ across the interval.

**Step 2 — solve for the pressure.** With $v = -x - p'(x)$ and $v$ constant,
$$0 = \partial_x v = -1 - p''(x) \quad\Longrightarrow\quad p''(x) = -1 \text{ on } (c-\tfrac12, c+\tfrac12),$$
with $p = 0$ at both endpoints (the complementarity condition, since $\rho < 1$ immediately outside). Integrating,
$$p(t,x) \;=\; \tfrac12\Big(c+\tfrac12 - x\Big)\Big(x - c + \tfrac12\Big) \;=\; \frac{1}{8} - \frac{(x-c(t))^2}{2}, \qquad |x - c| \le \tfrac12,$$
and $p \equiv 0$ elsewhere. Note $p \ge 0$, with maximum $p_{\max} = 1/8$ at the centre.

**Step 3 — recover the motion.** $p'(x) = -(x-c)$, hence $v = -x + (x - c) = -c$, so
$$\dot c = -c, \qquad c(t) = c_0 e^{-t}.$$
The crowd drifts to the origin at exponential rate while keeping unit width; the pressure profile is a rigid parabola translating with the crowd.

**What this shows.**
- $p$ is *Lipschitz but not $C^1$*: $p'(c\pm\frac12) = \mp\frac12$, jumping to $0$ outside. So $C^1$ pressure is false even in the best case, and $W^{1,\infty}$ is the natural target for (P1).
- $p_{\max} = 1/8$ is bounded and independent of $t$ — the positive evidence behind the conjectured $L^\infty$ bound.
- **Where it breaks in $d\ge2$.** Take instead two initially disjoint unit-mass patches in $\mathbb{R}^2$ under the same drift $-x$. Each evolves independently with its own bounded pressure until the instant $t_*$ when the patches touch. For $t > t_*$ the elliptic problem $-\Delta p = \Delta V = 2$ is posed on the *union*, whose Dirichlet problem has a strictly larger solution; $p(t,\cdot)$ jumps upward discontinuously in time, and the contact point is a corner of the free boundary where no known regularity theory applies. Iterating this with $N$ patches merging at a cascade of times $t_1 < t_2 < \dots$ is the mechanism that could defeat time-BV of $p$ — the concrete question (P3) asks to decide.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*