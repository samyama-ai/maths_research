---
id: 09-probability/optimal-stopping-problem-for-fractional-brownian-motion
title: "Optimal Stopping Problem for Fractional Brownian Motion"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Stopping Problem for Fractional Brownian Motion

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/optimal-stopping-problem-for-fractional-brownian-motion` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $B^H = (B^H_t)_{t \ge 0}$ be a standard fractional Brownian motion (fBm) with Hurst parameter $H \in (0,1)$, $H \neq 1/2$, on its natural filtration $\mathbb{F}^H = (\mathcal{F}^H_t)_{t\ge 0}$. For a measurable gain function $G$ and a discount/cost rate $c > 0$, the problem is to compute

$$V \;=\; \sup_{\tau \in \mathcal{T}} \; \mathbb{E}\!\left[ G(\tau, B^H_\tau) - c\,\tau \right],$$

where $\mathcal{T}$ is the set of $\mathbb{F}^H$-stopping times, and to *characterize the optimal stopping rule* $\tau^\ast$ attaining it.

**The open problem.** For no non-trivial $G$ and no $H \neq 1/2$ is an explicit optimal stopping boundary known. Concretely:

1. **(Structure)** Is the continuation region $C = \{(t,\omega) : V_t(\omega) > G(t, B^H_t(\omega))\}$ describable by a finite-dimensional statistic of the path — i.e. does there exist a $d$-dimensional sufficient statistic $Y_t$ and a boundary $b$ with $\tau^\ast = \inf\{t : Y_t \ge b(t)\}$?
2. **(Explicit solution)** Determine $V$ and $\tau^\ast$ in closed form for the canonical cases $G(x) = x$ with linear cost, $G(x)=(K - e^x)^+$ (fractional American put), and $G(x) = \max_{s\le t} B^H_s$ (fractional Russian/lookback problem).
3. **(Regularity)** Prove smooth-fit / continuity of the stopping boundary in $(t, H)$, and monotonicity of $V$ in $H$.

A complete solution means: an explicit or PDE/path-dependent-PDE-characterized value function with a proved verification theorem, valid on an interval of $H$ of positive length excluding $1/2$. A disproof of (1) means exhibiting $G$ for which the continuation region provably admits no finite-dimensional Markovian representation.

## 2. Mathematical Foundations

**Fractional Brownian motion.** $B^H$ is the centered Gaussian process with $B^H_0 = 0$ and covariance

$$R_H(s,t) = \mathbb{E}[B^H_s B^H_t] = \tfrac{1}{2}\left( t^{2H} + s^{2H} - |t-s|^{2H} \right).$$

It is the unique (up to scale) $H$-self-similar Gaussian process with stationary increments:

$$(B^H_{at})_{t\ge 0} \stackrel{d}{=} (a^H B^H_t)_{t \ge 0}, \qquad a > 0 .$$

Its Mandelbrot–Van Ness moving-average representation is

$$B^H_t = \frac{1}{\Gamma(H+\tfrac12)} \int_{-\infty}^{0}\!\big[(t-s)^{H-\frac12} - (-s)^{H-\frac12}\big]dW_s + \frac{1}{\Gamma(H+\frac12)}\int_0^t (t-s)^{H-\frac12} dW_s .$$

Increment correlation: $\rho(n) = \mathbb{E}[B^H_1 (B^H_{n+1}-B^H_n)] \sim H(2H-1)n^{2H-2}$, so increments are positively correlated (long memory, $\sum_n \rho(n) = \infty$) for $H>1/2$ and negatively correlated for $H<1/2$.

**Structural failures.** For $H \neq 1/2$, $B^H$ is (i) *not a semimartingale* — its $p$-variation is finite and nonzero for $p = 1/H$, so quadratic variation is $0$ for $H>1/2$ and $\infty$ for $H<1/2$ (Rogers 1997; Cheridito 2001); (ii) *not Markov* — by Lévy's characterization of Gaussian Markov processes, $R_H$ is of the triangular form $u(s)v(t)$ only when $H=1/2$; (iii) *not a Dirichlet process* for $H<1/2$.

**General theory that survives.** For $G$ continuous with $\mathbb{E}[\sup_{t \le T}|G(t,B^H_t)|] < \infty$, the Snell envelope
$$V_t = \operatorname*{ess\,sup}_{\tau \ge t} \mathbb{E}\big[G(\tau, B^H_\tau)\,\big|\,\mathcal{F}^H_t\big]$$
exists as the minimal càdlàg supermartingale dominating the gain, and $\tau^\ast = \inf\{t \ge 0 : V_t = G(t,B^H_t)\}$ is optimal on a finite horizon (El Karoui 1981). What fails is *computation*: there is no infinitesimal generator, hence no free-boundary PDE
$$\mathcal{L}V = 0 \ \text{ in } C, \qquad V = G \ \text{ on } \partial C, \qquad \partial_x V = \partial_x G \ \text{ on } \partial C,$$
the standard route of Peskir–Shiryaev.

**Maximal inequality (the main quantitative tool).** Novikov & Valkeila (1999): for every $p>0$ there is $c_{p,H}$ with
$$\mathbb{E}\Big[\sup_{s \le \tau} |B^H_s|^{\,p}\Big] \le c_{p,H}\, \mathbb{E}\big[\tau^{pH}\big]$$
for all stopping times $\tau$ — a fractional Burkholder–Davis–Gundy substitute.

## 3. History & State of the Art (SOTA)

- **1940 / 1968.** Kolmogorov introduces the "Wiener spiral"; Mandelbrot & Van Ness name and popularize fBm in *SIAM Review*.
- **1963–1978.** Snell envelope and general optimal stopping theory (Snell; Chow–Robbins–Siegmund; Bismut–Skalli; El Karoui) — applies to fBm but is non-constructive.
- **1997–2003.** Rogers proves arbitrage in fBm markets; Cheridito (2001, 2003) and Guasoni (2006) show transaction costs or mixing with an independent Wiener process restores no-arbitrage. This settles *which* fBm optimal-stopping problems are economically meaningful.
- **1999–2003.** Stochastic calculus for fBm: Decreusefond–Üstünel (Potential Analysis, 1999), Duncan–Hu–Pasik-Duncan (SIAM J. Control Optim., 2000), Alòs–Mazet–Nualart, Hu–Øksendal (2003) Wick–Itô fractional white-noise calculus. Hu–Øksendal derive "fractional Black–Scholes" prices; Björk & Hult (2005) show the Wick self-financing condition has no economic interpretation, undercutting the resulting American-option formulations.
- **2007–2013.** Functional Itô calculus (Dupire; Cont–Fournié) gives a path-dependent PDE framework, but fBm's non-semimartingale character puts it outside the standard hypotheses.
- **2019–2023.** Numerics take over. Becker–Cheridito–Jentzen (*Deep optimal stopping*, JMLR 2019) compute $\sup_\tau \mathbb{E}[B^H_\tau]$ over $\tau \le 1$ on a $100$-step grid for $H = 0.01,\dots,0.99$; Bayer–Hager–Riedel–Schoenmakers (*Optimal stopping with signatures*, Ann. Appl. Probab. 2023) give a convergent linear-programming/signature scheme for non-Markovian payoffs including fBm.
- **State of the art:** no closed form for any $H \neq 1/2$; sharp *scaling laws* and numerical value functions with error control.

## 4. Partial Results / Verified Cases

- **$H = 1/2$.** Fully solved: Wiener case, all classical free-boundary results (American put, Russian option, Chernoff problem).
- **Infinite-horizon linear payoff with proportional cost, all $H \in (0,1)$.** $V(c) = \sup_\tau \mathbb{E}[B^H_\tau - c\tau]$ satisfies exactly $V(c) = K_H\, c^{-H/(1-H)}$ with $K_H = V(1) \in (0,\infty)$ (Section 10). The exponent is known; $K_H$ and $\tau^\ast$ are not.
- **Finiteness / existence.** For continuous $G$ of at most polynomial growth and finite horizon, an optimal $\tau^\ast$ exists via the Snell envelope (El Karoui 1981); the Novikov–Valkeila inequality yields finiteness on the infinite horizon whenever the cost is superlinear relative to $t^H$.
- **Discrete-time and approximation regimes.** Sottinen (2001) binary-market approximations of fBm converge weakly, giving convergent Bermudan value sequences. Signature-LP (Bayer et al. 2023) and deep-learning (Becker et al. 2019, 2021) schemes give two-sided bounds: e.g. for $H = 0.05$ over $[0,1]$, the reported value of $\sup_\tau \mathbb{E}[B^H_\tau]$ is $\approx 1.5$, decreasing monotonically in the numerics to $\approx 0$ near $H \to 1$.
- **Mixed models.** For $B_t + B^H_t$ with $H \in (3/4, 1)$, the mixed process is a semimartingale equivalent in law to Brownian motion (Cheridito 2001) — optimal stopping there reduces to the classical case.
- **Markovian lifts.** For the fractional Ornstein–Uhlenbeck / rough-volatility family, Abi Jaber–El Euch (2019) and Cuchiero–Teichmann (2020) provide infinite-dimensional Markov lifts; American-option values in the Volterra Heston model are characterized (Chevalier–Pulido–Zúñiga, 2022) as infinite-dimensional variational inequalities — characterized, not solved.
- **Perturbative regime.** $|H - 1/2| \ll 1$: first-order expansions of Bermudan values around the Brownian boundary are numerically stable but lack proved error bounds. *(frontier — verify)*

## 5. Principal Obstacles

- **No generator, no free-boundary PDE.** Every explicit solution in the classical catalog comes from solving $\mathcal{L}V=0$ with smooth fit. $B^H$ has no infinitesimal generator on functions of $B^H_t$ alone; $V_t$ genuinely depends on the whole path $(B^H_s)_{s\le t}$.
- **No martingale toolbox.** No Itô formula in the pathwise-integral sense usable for verification ($H<1/2$ has infinite quadratic variation; $H>1/2$ has zero quadratic variation, so Itô's formula is first-order and gives no gain from convexity). Doob–Meyer decomposition of the Snell envelope exists but its finite-variation part has no computable form.
- **Wick calculus is analytically clean but economically empty.** Hu–Øksendal integrals make the fractional market "arbitrage-free," but Björk–Hult (2005) show the corresponding self-financing portfolios are not portfolios; verification theorems built on it do not answer the stated problem.
- **Time-inconsistency of naive dynamic programming.** Conditional laws of $B^H$ given $\mathcal{F}^H_t$ have a drift depending on the entire past through a Volterra kernel $\int_{-\infty}^t (t-s)^{\cdots}$; the "state" is an element of an infinite-dimensional function space, so Bellman's equation is a PPDE with a non-local, singular kernel.
- **No scaling beyond self-similarity.** Self-similarity plus stationary increments determines exponents but not constants; the constants are hitting-probability functionals of a non-Markov Gaussian field, for which no exact computation technique exists (this is the same barrier as the unknown persistence exponents of fBm).

## 6. The Gap

Proven: existence of $\tau^\ast$, sharp maximal inequalities, exact scaling exponent $H/(1-H)$ for the linear-cost problem, convergent numerical schemes with a posteriori bounds.

Missing: any *closed-form or PDE-characterized* description of $\partial C$. The precise step is to produce a **verification theorem without a semimartingale decomposition** — either (a) a Markovian lift $Y_t = (B^H_t, (\text{Volterra state}))$ on a Banach space together with a well-posed variational inequality for $V$ *and* a proof that the value of the lifted problem equals the original, or (b) a proof that no finite-dimensional lift exists, forcing genuinely infinite-dimensional methods. Even the constant $K_H$ in $V(c) = K_H c^{-H/(1-H)}$ is unknown for a single $H \neq 1/2$.

## 7. Current Research (as of June 2026)

- **Signature methods.** Bayer, Hager, Riedel, Schoenmakers and collaborators (WIAS Berlin, TU Berlin) extend the signature-LP framework of Ann. Appl. Probab. 2023 to give dual (upper) bounds for fBm stopping with explicit truncation error in the signature depth. *(frontier — verify)*
- **Deep optimal stopping.** Cheridito, Becker, Jentzen and successors (ETH Zürich, Münster) — neural stopping-time parameterizations plus dual martingale bounds; the fBm example is now a standard benchmark.
- **Markovian lifts / rough volatility.** Abi Jaber (École Polytechnique), Cuchiero–Teichmann (Vienna/ETH), Bayer–Breneis (WIAS): finite-dimensional approximations of the fractional kernel $t^{H-1/2}$ by sums of exponentials, converting American pricing into a moderate-dimensional free-boundary problem with quantified kernel-approximation error.
- **Path-dependent PDEs and viscosity theory.** Extensions of Cont–Fournié functional Itô calculus to Volterra/rough settings, aiming at a viscosity characterization of $V$. *(frontier — verify)*
- **Fine properties of fBm.** Continued work on persistence exponents, first-passage densities, and Gaussian-process hitting times feeds directly into any exact boundary computation.

## 8. Future Work

- Compute $K_H$ for one value $H \ne 1/2$ — the smallest non-trivial exact result available, and a natural target.
- Prove monotonicity and continuity of $H \mapsto V(H)$ for the finite-horizon linear problem, matching the numerics of Becker et al.
- Establish a rigorous verification theorem in the two-parameter Markov lift $(t, \int_0^t (t-s)^{H-1/2}dW_s$-family$)$ with error bounds under exponential-sum kernel approximation.
- Perturbative expansion of the stopping boundary in $\varepsilon = H - 1/2$ with proved remainder estimates.
- Formulate the correct economically meaningful American-option problem under transaction costs (Guasoni framework) rather than Wick calculus, and solve it asymptotically for small costs.

## 9. Key References

- **[Foundational]** B. B. Mandelbrot, J. W. Van Ness. *Fractional Brownian motions, fractional noises and applications.* SIAM Review 10(4), 422–437, 1968.
- **[Foundational]** L. C. G. Rogers. *Arbitrage with fractional Brownian motion.* Mathematical Finance 7(1), 95–105, 1997.
- **[Foundational]** N. El Karoui. *Les aspects probabilistes du contrôle stochastique.* Lecture Notes in Mathematics 876, Springer, 1981.
- **[Foundational]** G. Peskir, A. Shiryaev. *Optimal Stopping and Free-Boundary Problems.* Birkhäuser (Lectures in Mathematics, ETH Zürich), 2006.
- **[Key tool]** A. Novikov, E. Valkeila. *On some maximal inequalities for fractional Brownian motions.* Statistics & Probability Letters 44(1), 47–54, 1999.
- **[Structural]** P. Cheridito. *Mixed fractional Brownian motion.* Bernoulli 7(6), 913–934, 2001.
- **[Structural]** P. Guasoni. *No arbitrage under transaction costs, with fractional Brownian motion and beyond.* Mathematical Finance 16(3), 569–582, 2006.
- **[Calculus]** T. E. Duncan, Y. Hu, B. Pasik-Duncan. *Stochastic calculus for fractional Brownian motion I. Theory.* SIAM Journal on Control and Optimization 38(2), 582–612, 2000.
- **[Calculus]** Y. Hu, B. Øksendal. *Fractional white noise calculus and applications to finance.* Infinite Dimensional Analysis, Quantum Probability and Related Topics 6(1), 1–32, 2003.
- **[Critique]** T. Björk, H. Hult. *A note on Wick products and the fractional Black–Scholes model.* Finance and Stochastics 9(2), 197–209, 2005.
- **[SOTA / Recent]** S. Becker, P. Cheridito, A. Jentzen. *Deep optimal stopping.* Journal of Machine Learning Research 20(74), 1–25, 2019.
- **[SOTA / Recent]** C. Bayer, P. Hager, S. Riedel, J. Schoenmakers. *Optimal stopping with signatures.* Annals of Applied Probability 33(1), 238–273, 2023.
- **[SOTA / Recent]** E. Abi Jaber, O. El Euch. *Multifactor approximation of rough volatility models.* SIAM Journal on Financial Mathematics 10(2), 309–349, 2019.
- **[SOTA / Recent]** E. Chevalier, S. Pulido, E. Zúñiga. *American options in the Volterra Heston model.* SIAM Journal on Financial Mathematics 13(2), 426–458, 2022.
- **[Survey / Book]** F. Biagini, Y. Hu, B. Øksendal, T. Zhang. *Stochastic Calculus for Fractional Brownian Motion and Applications.* Springer, 2008.
- **[Survey / Book]** Y. Mishura. *Stochastic Calculus for Fractional Brownian Motion and Related Processes.* Lecture Notes in Mathematics 1929, Springer, 2008.
- **[Survey]** I. Nourdin. *Selected Aspects of Fractional Brownian Motion.* Bocconi & Springer Series, 2012.

## 10. Worked Example / Concrete Special Case

**Problem.** Fix $H \in (0,1)$ and $c>0$. Compute the scaling of
$$V(c) = \sup_{\tau \in \mathcal{T}} \mathbb{E}\big[B^H_\tau - c\,\tau\big].$$

**Step 1 — finiteness.** By Novikov–Valkeila with $p=1$, $\mathbb{E}[\sup_{s\le\tau} |B^H_s|] \le c_{1,H}\,\mathbb{E}[\tau^{H}]$. Hence
$$\mathbb{E}[B^H_\tau - c\tau] \;\le\; \mathbb{E}\big[c_{1,H}\tau^H - c\tau\big] \;\le\; \sup_{t\ge 0}\big(c_{1,H}t^H - ct\big) \;=\; (1-H)H^{\frac{H}{1-H}}\,c_{1,H}^{\frac{1}{1-H}}\, c^{-\frac{H}{1-H}} \;<\;\infty,$$
using $H<1$ so $t\mapsto c_{1,H}t^H - ct$ is bounded above, with maximizer $t^\ast = (Hc_{1,H}/c)^{1/(1-H)}$. Also $V(c) > 0$: take $\tau \equiv t$ deterministic small — $\mathbb{E}[B^H_t] = 0$, so instead take $\tau = \inf\{t: B^H_t \ge 1\} \wedge t_0$, which gives a strictly positive value for $t_0$ large and $c$ finite. So $0 < V(c) < \infty$.

**Step 2 — exact scaling by self-similarity.** Fix $a>0$. The time-change $t \mapsto at$ maps $\mathcal{T}$ bijectively onto itself ($\tau \mapsto a\tau$) and $(B^H_{at})_t \stackrel{d}{=} (a^H B^H_t)_t$ as processes with the corresponding filtrations. Therefore

$$V(c) = \sup_\tau \mathbb{E}\big[B^H_{a\tau} - c\,a\tau\big] = \sup_\tau \mathbb{E}\big[a^H B^H_{\tau} - ca\,\tau\big] = a^H \sup_\tau \mathbb{E}\big[B^H_\tau - c\,a^{1-H}\tau\big] = a^H\, V\!\left(c\,a^{1-H}\right).$$

Choose $a = c^{-1/(1-H)}$ so that $c\,a^{1-H} = 1$:

$$\boxed{\;V(c) = K_H\, c^{-\frac{H}{1-H}}, \qquad K_H := V(1) \in (0,\infty).\;}$$

**Step 3 — sanity check at $H=1/2$.** The exponent is $-\frac{1/2}{1/2} = -1$, so $V(c) = K_{1/2}/c$. Classically, for Brownian motion the optimal rule for $\sup_\tau\mathbb{E}[W_\tau - c\tau]$ is $\tau^\ast = \inf\{t: W_t \ge b\}$; with $\mathbb{E}[\tau_b] = \infty$ the one-sided problem degenerates, and the standard regularized version $\sup_\tau \mathbb{E}[e^{-c\tau}W_\tau^+]$ gives value $\propto c^{-1/2}$ — the $1/c$ scaling above is the correct homogeneity for the linear-cost formulation. Note $H/(1-H) \to 0$ as $H\to 0$ (value nearly cost-insensitive: the path oscillates so fast that a large value is reached almost immediately) and $H/(1-H) \to \infty$ as $H \to 1$ (the path is nearly the straight line $t\,\xi$, $\xi \sim N(0,1)$, so waiting pays only if $\xi > c$, and the value collapses).

**What remains open in this example.** The scaling argument fixes the exponent exactly and *for every* $H$, but yields nothing about $K_H$ or about the shape of $\tau^\ast$. Since $B^H$ is not Markov, $\tau^\ast$ cannot be a hitting time of a level or of a deterministic curve by $B^H$ alone: the conditional drift $\mathbb{E}[dB^H_t \mid \mathcal{F}^H_t]$ depends on the entire past through a Volterra kernel, so the optimal rule must compare $B^H_t$ against a functional of the whole path. Exhibiting that functional — even for one $H \neq 1/2$ — is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*