---
id: 09-probability/blank-shiryaev-problem
title: "Blank-Shiryaev Problem"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Blank-Shiryaev Problem

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/blank-shiryaev-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Blank–Shiryaev problem is the **Bayesian quickest-detection (disorder) problem for Brownian motion with a general prior on the disorder time and a finite horizon**, asked in the strong form: *give the optimal stopping boundary in closed form, or prove that none exists in any elementary class.*

Setting. On a filtered space carry a standard Brownian motion $B$ and an independent random time $\theta \ge 0$ with prior law $\Pi$ (so $\mathsf P(\theta = 0) = \pi$, $\mathsf P(\theta > t \mid \theta > 0) = G(t)$). The observed process is

$$X_t \;=\; \mu \int_0^t \mathbf 1_{\{\theta \le s\}}\, ds \;+\; \sigma B_t , \qquad \mu \neq 0,\ \sigma > 0 .$$

An observer sees only $\mathcal F^X_t = \sigma(X_s, s \le t)$ and must choose an $\mathcal F^X$-stopping time $\tau \le T$ minimising the Bayes risk

$$V(\pi) \;=\; \inf_{\tau \le T} \Big[\, \mathsf P(\tau < \theta) \;+\; c\, \mathsf E (\tau-\theta)^+ \Big], \qquad c>0 .$$

Open components:

1. **Closed-form boundary.** For $T=\infty$ and exponential prior $G(t)=e^{-\lambda t}$ the solution is a constant threshold on the posterior probability process; for **every** other case — finite $T$, or $T=\infty$ with non-exponential $\Pi$ — no closed-form boundary is known, and it is not known whether the boundary can be characterised other than as the solution of a nonlinear Volterra integral equation.
2. **General prior.** Determine, for arbitrary $\Pi$ (including priors with atoms, heavy tails, or non-Markov structure), whether the problem admits a finite-dimensional sufficient statistic; conjecturally it does not outside the Markov (exponential / Erlang / deterministic-atom) family.
3. **Boundary regularity.** Prove or disprove that the finite-horizon boundary $b:[0,T)\to(0,1)$ is $C^\infty$ on $[0,T)$, strictly increasing, and admits a convergent asymptotic expansion at $t \uparrow T$ for general $\Pi$.

A complete resolution means: an explicit boundary (or a proof of non-existence within a specified class), plus a proof of uniqueness of the integral-equation characterisation for general $\Pi$.

*(Attribution note — verify: the eponym circulates in the Russian sequential-analysis school; the primary printed formulations are Shiryaev 1961, 1963.)*

## 2. Mathematical Foundations

**Posterior probability process.** Set $\pi_t = \mathsf P(\theta \le t \mid \mathcal F^X_t)$. The likelihood-ratio process is

$$L_t \;=\; \exp\!\Big( \frac{\mu}{\sigma^2} X_t - \frac{\mu^2}{2\sigma^2} t \Big),$$

and for the exponential prior with rate $\lambda$, $\pi_t$ solves the **Shiryaev stochastic differential equation**

$$d\pi_t \;=\; \lambda(1-\pi_t)\,dt \;+\; \frac{\mu}{\sigma}\,\pi_t(1-\pi_t)\, d\bar B_t ,\qquad \pi_0 = \pi,$$

where $\bar B_t = \frac{1}{\sigma}\big(X_t - \mu\int_0^t \pi_s ds\big)$ is the **innovation Brownian motion**, itself an $\mathcal F^X$-Brownian motion. For a general prior with hazard rate $\lambda(t) = -G'(t)/G(t)$ the drift term becomes $\lambda(t)(1-\pi_t)\,dt$, so $(t,\pi_t)$ is Markov only when $\lambda$ is deterministic in $t$; for non-absolutely-continuous $\Pi$ no such finite-dimensional reduction exists.

**Reduction.** Standard Bayesian reduction gives

$$\mathsf P(\tau<\theta) + c\,\mathsf E(\tau-\theta)^+ \;=\; \mathsf E\Big[ (1-\pi_\tau) + c\int_0^\tau \pi_s\,ds \Big],$$

so the problem is the Markovian optimal stopping problem

$$V(t,\pi) \;=\; \inf_{\tau \le T-t} \mathsf E_{t,\pi}\Big[ (1-\pi_{t+\tau}) + c\int_0^{\tau} \pi_{t+s}\,ds \Big].$$

**Free-boundary formulation.** With generator
$$\mathbb L \;=\; \partial_t + \lambda(t)(1-\pi)\,\partial_\pi + \tfrac12 \tfrac{\mu^2}{\sigma^2}\pi^2(1-\pi)^2\,\partial_{\pi\pi},$$
$V$ is the unique solution of

$$\mathbb L V = -c\pi \ \text{ on } C=\{(t,\pi): \pi < b(t)\}, \qquad V(t,b(t)) = 1-b(t), \qquad V_\pi(t,b(t)) = -1,$$

the last identity being **smooth fit**. The optimal rule is $\tau_* = \inf\{t: \pi_t \ge b(t)\}$.

**Integral equation.** By the local time–space (Itô–Tanaka–Meyer) formula, $b$ satisfies for $t\in[0,T)$

$$1-b(t) \;=\; \mathsf E_{t,b(t)}\big[1-\pi_T\big] \;+\; c\,\mathsf E_{t,b(t)}\!\!\int_0^{T-t}\!\!\pi_{t+s}\,\mathbf 1_{\{\pi_{t+s} < b(t+s)\}}\,ds ,$$

a nonlinear Volterra equation of the second kind whose solution is unique in the class of continuous decreasing boundaries (Peskir's uniqueness method).

## 3. History & State of the Art

- **1961–1963.** Shiryaev formulates the disorder problem and solves the infinite-horizon exponential-prior case: the optimal rule is $\tau_* = \inf\{t: \pi_t \ge A^*\}$ with $A^*$ determined by an explicit transcendental equation. This is the origin of the Shiryaev–Roberts statistic.
- **1971–1986.** Non-Bayesian counterparts settle: Lorden's minimax asymptotic optimality of CUSUM, then Moustakides' exact optimality of CUSUM for Lorden's criterion.
- **1978/2008.** *Optimal Stopping Rules* consolidates the Markovian theory and states the general-prior and finite-horizon cases as unsolved.
- **2002.** Peskir–Shiryaev solve the Poisson disorder problem (compound-jump observations), exposing how the boundary structure depends on the sign of $\lambda - $ jump-intensity change.
- **2006.** Gapeev–Peskir, *The Wiener disorder problem with finite horizon*: the boundary is shown continuous and increasing, characterised as the **unique** solution of the nonlinear integral equation above; no closed form obtained. This remains the SOTA for $T<\infty$.
- **2010.** Shiryaev's retrospective "fifty years later" lists general priors, finite horizon, and multi-dimensional/dependent observations as the standing open directions.
- **2012–2015.** Zhitlukhin–Shiryaev treat disorder problems on general filtered spaces (no Markov reduction) via the Snell envelope; Ekström–Vaicenavicius handle general priors in the related *sequential testing* problem, obtaining boundary monotonicity but not closed form.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $T=\infty$, exponential prior, Brownian observations | **Solved** (Shiryaev 1963): constant threshold $A^*$, explicit value function on $[0,A^*]$ |
| $T=\infty$, Poisson observations, exponential prior | **Solved** (Peskir–Shiryaev 2002; Bayraktar–Dayanik–Karatzas 2006) |
| $T<\infty$, exponential prior | **Characterised, not closed form** (Gapeev–Peskir 2006): $b$ continuous, increasing, unique Volterra solution |
| Prior = Erlang$(k,\lambda)$, $k\ge2$ | Reduces to a $k$-dimensional degenerate free-boundary PDE; solved numerically only |
| Deterministic disorder time $\theta \equiv t_0$ | Trivial ($\tau_* = t_0$) |
| Zero delay cost $c \downarrow 0$ | $b(t)\to1$; first-order asymptotics $1-b(t) \asymp c^{1/3}$-type scaling known in the exponential case |
| $t \uparrow T$ | $b(T-)=1$ with local expansion $1-b(T-s)\sim \kappa\, s\log(1/s)$-type known for exponential prior |
| Non-Markov filtrations | Existence/optimality of the Snell-envelope stopping time only (Zhitlukhin–Shiryaev) |

## 5. Principal Obstacles

- **Loss of scaling.** The diffusion coefficient $\pi^2(1-\pi)^2$ degenerates at both endpoints and the drift $\lambda(t)(1-\pi)$ breaks time-homogeneity. There is no self-similarity, so the standard reduction of parabolic free boundaries to a one-parameter similarity variable (as for the American put / Stefan problems) fails outright.
- **No closed-form heat kernel.** The transition density of $\pi_t$ has no elementary expression; Laplace/Mellin transform methods that solve infinite-horizon problems by ODEs give confluent-hypergeometric solutions whose finite-horizon analogues do not close.
- **General priors destroy Markovianity.** With arbitrary $\Pi$ the pair $(t,\pi_t)$ is no longer Markov; the sufficient statistic is the whole path of the likelihood ratio. Free-boundary PDE technology has no state space to be posed on, and one is left with abstract Snell envelopes that give existence but no computability.
- **Nonlinear Volterra rigidity.** The integral characterisation is proved unique but is not solvable in quadrature; no known transform linearises it, and its kernel involves the very boundary being sought.
- **Verification-theorem fragility.** Smooth fit at $b(t)$ is proved case-by-case using the strong Markov property and local time on curves; for priors with atoms $V_\pi$ can fail to be continuous at the atom times, so the usual verification argument breaks.

## 6. The Gap

Proven: for exponential priors and $T<\infty$, the boundary exists, is continuous and increasing, and is the unique solution of a nonlinear Volterra equation. Wanted: (i) an explicit or asymptotically complete description of that boundary, and (ii) any characterisation at all for general $\Pi$.

The exact barrier is the passage from *existence + uniqueness of an implicit characterisation* to *constructive description*. Concretely: no method is known to convert the local time–space integral equation into a linear equation with an explicit kernel, and no method is known to compress the path-dependent sufficient statistic of a general prior into finitely many coordinates. Either a new integral-transform identity for the Shiryaev diffusion, or a proof that the boundary is non-elementary (a transcendence result for free boundaries — a type of theorem that does not yet exist), would close the gap.

## 7. Current Research (as of June 2026)

- **Integral-equation numerics and rigorous error bounds.** Manchester (Peskir school) and Michigan (Bayraktar) continue to develop local time–space calculus and provable-convergence schemes for boundaries of this type.
- **General-prior sequential problems.** Uppsala (Ekström and collaborators) extend the "monotone boundary via stochastic comparison" technique from sequential testing to disorder detection with non-exponential priors; monotonicity and continuity are being pushed to broad prior classes *(frontier — verify)*.
- **Non-Markov / general filtration formulations.** Steklov Institute (Zhitlukhin, Shiryaev school) work with Snell envelopes and optional decompositions, targeting structural (not explicit) results.
- **Multi-source and networked detection.** Extensions to several observation streams with a common or coupled disorder time; the free boundary becomes a hypersurface, and even regularity is open *(frontier — verify)*.
- **Machine-learned boundaries.** Deep-BSDE and neural optimal-stopping solvers are used as conjecture generators for asymptotic forms of $b$ near $t=T$ *(frontier — verify)*.

## 8. Future Work

- Seek an exact asymptotic expansion of $b(T-s)$ as $s\downarrow0$ to all orders for the exponential prior; a full expansion would strongly constrain any candidate closed form.
- Attack the general-prior case through the hazard-rate function: classify priors whose hazard rate is a solution of a Riccati ODE, since exactly these keep the posterior a one-dimensional diffusion.
- Develop a transcendence/obstruction theory for parabolic free boundaries — a proof that $b$ is not algebraic over the natural differential field would resolve the problem negatively and be of independent interest.
- Transfer techniques from the finite-horizon American put, where analogous integral equations are also unsolved; progress in either problem plausibly transfers.

## 9. Key References

- **[Foundational]** A. N. Shiryaev. *The problem of the most rapid detection of a disturbance in a stationary process.* Soviet Mathematics — Doklady, 2 (1961), 795–799.
- **[Foundational]** A. N. Shiryaev. *On optimum methods in quickest detection problems.* Theory of Probability and Its Applications, 8(1) (1963), 22–46.
- **[Foundational]** A. N. Shiryaev. *Optimal Stopping Rules.* Springer, 1978 (reprinted, Stochastic Modelling and Applied Probability 8, 2008).
- **[Foundational]** G. Peskir and A. N. Shiryaev. *Optimal Stopping and Free-Boundary Problems.* Lectures in Mathematics ETH Zürich, Birkhäuser, 2006.
- **[SOTA / Recent]** P. V. Gapeev and G. Peskir. *The Wiener disorder problem with finite horizon.* Stochastic Processes and their Applications, 116(12) (2006), 1770–1791.
- **[SOTA / Recent]** G. Peskir and A. N. Shiryaev. *Solving the Poisson disorder problem.* In: Advances in Finance and Stochastics, Springer, 2002, 295–312.
- **[SOTA / Recent]** E. Bayraktar, S. Dayanik and I. Karatzas. *The standard Poisson disorder problem revisited.* Stochastic Processes and their Applications, 116(9) (2006), 1437–1450.
- **[SOTA / Recent]** M. V. Zhitlukhin and A. N. Shiryaev. *Bayesian disorder problems on filtered probability spaces.* Theory of Probability and Its Applications, 57(3) (2013), 497–511.
- **[SOTA / Recent]** E. Ekström and J. Vaicenavicius. *Bayesian sequential testing of the drift of a Brownian motion.* ESAIM: Probability and Statistics, 19 (2015), 626–648.
- **[Survey]** A. N. Shiryaev. *Quickest detection problems: fifty years later.* Sequential Analysis, 29(4) (2010), 345–385.
- **[Survey]** G. V. Moustakides. *Optimal stopping times for detecting changes in distributions.* Annals of Statistics, 14(4) (1986), 1379–1387.
- **[Survey]** G. Lorden. *Procedures for reacting to a change in distribution.* Annals of Mathematical Statistics, 42(6) (1971), 1897–1908.

## 10. Worked Example / Concrete Special Case

**Infinite horizon, exponential prior — the solvable anchor.** Take $\sigma=1$, drift $\mu$, prior rate $\lambda$, delay cost $c$, and $T=\infty$. Write $\rho = \mu^2/2$. On the continuation region $\{\pi<A\}$ the free-boundary problem is the ODE

$$\rho\,\pi^2(1-\pi)^2 V''(\pi) + \lambda(1-\pi)V'(\pi) = -c\pi ,$$

with $V(A)=1-A$, $V'(A)=-1$ (smooth fit) and $V$ bounded at $0$. Integrating once with the integrating factor $\exp\!\big(\int \frac{\lambda}{\rho \pi^2(1-\pi)}d\pi\big)$ gives

$$V'(\pi) \;=\; -\frac{c}{\rho}\,\frac{1}{\pi(1-\pi)}\, e^{\Lambda(\pi)}\int_{\pi}^{A}\frac{e^{-\Lambda(u)}}{u(1-u)}\,du \Big/ \text{(normalisation)},\qquad \Lambda(\pi)=\frac{\lambda}{\rho}\Big(\log\frac{\pi}{1-\pi}+\frac1\pi\Big),$$

and the smooth-fit condition $V'(A)=-1$ pins $A=A^*$ as the unique root of

$$\frac{c}{\rho}\int_0^{A}\frac{e^{-\Lambda(u)}}{u(1-u)}\,du \;=\; A(1-A)\,e^{-\Lambda(A)} .$$

Numerically, with $\mu=1$ ($\rho=1/2$), $\lambda=1$, $c=1$ this yields $A^*\approx0.72$: stop the first time the posterior probability of disorder reaches about $0.72$; the corresponding Bayes risk is $V(0)\approx0.35$.

**Where the problem starts.** Now impose $T=10$. The same computation cannot be run: the value $V(t,\pi)$ genuinely depends on $t$, the ODE becomes the parabolic PDE $\mathbb LV=-c\pi$, and the threshold becomes a curve $b(t)$ with $b(0)<A^*$ and $b(10^-)=1$. All that is proved is that $b$ is continuous, increasing, and the unique continuous solution of the Volterra equation of Section 2. Solving that equation by Picard iteration on a grid of $10^3$ points gives, for the same parameters, $b(0)\approx0.66$ and $b(9)\approx0.93$ — but no closed formula for a single one of those numbers is known, and replacing the exponential prior by, say, a Pareto prior removes even the PDE on which the iteration is built.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*