---
id: 09-probability/empirical-measure-wasserstein-rate-high-dimension
title: "Optimal Transport Cost Between Empirical and True Measures in High Dimension"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Transport Cost Between Empirical and True Measures in High Dimension

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/empirical-measure-wasserstein-rate-high-dimension` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mu$ be a Borel probability measure on $\mathbb{R}^d$, let $X_1,\dots,X_n$ be i.i.d. samples from $\mu$, and let
$$\mu_n = \frac{1}{n}\sum_{i=1}^n \delta_{X_i}$$
be the empirical measure. For $p \ge 1$, how fast does the $p$-Wasserstein cost $W_p(\mu_n,\mu)$ tend to $0$?

The **order** of the rate is known: for $\mu$ absolutely continuous on $\mathbb{R}^d$ with enough moments and $d > 2p$, $\mathbb{E}\,W_p(\mu_n,\mu) \asymp n^{-1/d}$ (Fournier–Guillin 2015; Weed–Bach 2019). What remains open is everything sharper than the order.

**Main open questions.**

1. **(Limiting constant.)** Does the limit
$$c_{p,d}(\mu) \;:=\; \lim_{n\to\infty} n^{1/d}\,\mathbb{E}\,W_p(\mu_n,\mu)$$
exist for all $p>1$ and all $d\ge 3$, and does it obey the conjectured *Dobrić–Yukich scaling law*
$$c_{p,d}(\mu)^p \;=\; \beta(p,d)\left(\int_{\mathbb{R}^d} f(x)^{\frac{d-p}{d}}\,dx\right),$$
where $f = d\mu/dx$ and $\beta(p,d)$ is a universal constant depending only on $p,d$? A complete solution must (a) prove existence of the limit, (b) establish the separation of the measure-dependent factor from the universal factor, and (c) determine $\beta(p,d)$, or at least its behaviour as $d\to\infty$.
2. **(Fluctuations.)** Identify the limit law of $n^{1/d}\big(W_p(\mu_n,\mu) - \mathbb{E}W_p(\mu_n,\mu)\big)$ for $d\ge 3$. No non-degenerate central limit theorem is known in this regime.
3. **(Structure vs. dimension.)** Characterize exactly which measures escape the $n^{-1/d}$ curse — i.e. give a sharp intrinsic-dimension functional $\dim^*(\mu)$ such that $\mathbb{E}W_p(\mu_n,\mu) = n^{-1/\dim^*(\mu)+o(1)}$ for all $\mu$.

## 2. Mathematical Foundations

**Wasserstein distance.** For $\mu,\nu \in \mathcal{P}_p(\mathbb{R}^d)$ (finite $p$-th moment),
$$W_p(\mu,\nu) \;=\; \left(\inf_{\pi\in\Pi(\mu,\nu)} \int_{\mathbb{R}^d\times\mathbb{R}^d} \|x-y\|^p \, d\pi(x,y)\right)^{1/p},$$
$\Pi(\mu,\nu)$ being the couplings with marginals $\mu,\nu$. Kantorovich duality for $p=1$:
$$W_1(\mu,\nu) \;=\; \sup_{\|\varphi\|_{\mathrm{Lip}}\le 1}\int \varphi\, d(\mu-\nu),$$
which exhibits $W_1(\mu_n,\mu)$ as the supremum of an empirical process indexed by the unit Lipschitz ball — the source of both the entropy-based upper bounds and the curse of dimensionality (the $\varepsilon$-entropy of Lipschitz functions on $[0,1]^d$ grows like $\varepsilon^{-d}$).

**Fournier–Guillin bound.** If $\int \|x\|^q d\mu < \infty$ for some $q>p$, then for a constant $C = C(p,q,d)$,
$$\mathbb{E}\,W_p^p(\mu_n,\mu) \;\le\; C\, M_q^{p/q}(\mu) \times
\begin{cases}
n^{-1/2} + n^{-(q-p)/q}, & p > d/2,\\[2pt]
n^{-1/2}\log(1+n) + n^{-(q-p)/q}, & p = d/2,\\[2pt]
n^{-p/d} + n^{-(q-p)/q}, & p < d/2 .
\end{cases}$$

**Dyadic / multiscale decomposition.** The standard upper-bound machine partitions $[0,1]^d$ into $2^{k d}$ dyadic cubes at scale $2^{-k}$ and uses
$$W_p^p(\mu_n,\mu) \;\lesssim\; \sum_{k\ge 0} 2^{-kp} \sum_{Q\in\mathcal{D}_k} \big|\mu_n(Q)-\mu(Q)\big|,$$
each level contributing $2^{-kp}\cdot 2^{kd/2} n^{-1/2}$ by binomial fluctuations. The sum diverges geometrically when $p<d/2$, and truncating at scale $2^{-k}\sim n^{-1/d}$ gives the $n^{-p/d}$ rate.

**Linearization (PDE) heuristic.** For $p=2$ and smooth $f$, the Benamou–Brenier / weighted-$H^{-1}$ linearization gives
$$W_2^2(\mu_n,\mu) \;\approx\; \|\mu_n - \mu\|_{\dot H^{-1}(\mu)}^2 \;=\;\int \frac{|\nabla u|^2}{f}\,dx,\qquad -\nabla\!\cdot\!(f\nabla u) = \mu_n - \mu .$$
This is rigorous in $d=2$ after regularization (Ambrosio–Stra–Trevisan) and is the conjectural route to sharp constants in $d\ge3$.

**Intrinsic dimension (Weed–Bach).** With $N_\varepsilon(\mu)$ the $\varepsilon$-covering number of the support and the $(\varepsilon,\tau)$-covering number $N_\varepsilon(\mu,\tau)$ counting balls needed to capture mass $1-\tau$,
$$d_p^*(\mu) = \inf\{s>2p:\ \limsup_{\varepsilon\to0}\ \tfrac{\log N_\varepsilon(\mu)}{-\log\varepsilon} \le s\}\ \Longrightarrow\ \mathbb{E}W_p^p(\mu_n,\mu)\lesssim n^{-p/d_p^*}.$$

## 3. History & State of the Art (SOTA)

- **1969.** Dudley proves the first general rates for $\mathbb{E}\|\mu_n-\mu\|_{\mathrm{Lip}^*}$, obtaining $n^{-1/d}$ for $d\ge3$ and identifying $d=2$ as critical.
- **1984.** Ajtai, Komlós and Tusnády solve the two-dimensional matching problem: for $n$ uniform points in $[0,1]^2$, $\mathbb{E}W_\infty$-type matching cost is $\asymp \sqrt{\log n / n}$ — the celebrated extra $\sqrt{\log n}$.
- **1995.** Dobrić and Yukich prove the subadditivity/limit theorem for $W_1$: $n^{1/d}\mathbb{E}W_1(\mu_n,\mu)\to \beta(1,d)\int f^{(d-1)/d}$ for $d\ge3$. This is the template the general-$p$ conjecture imitates.
- **2013–2014.** Dereich–Scheutzow–Schottstedt and Boissard–Le Gouic give non-asymptotic bounds under moment and concentration hypotheses.
- **2015.** Fournier–Guillin give the definitive non-asymptotic upper bound stated above, with matching lower bounds in order.
- **2019.** Weed–Bach establish sharp finite-sample upper *and* lower bounds and the intrinsic-dimension refinement; Ambrosio–Stra–Trevisan prove the sharp two-dimensional constant, $n\,\mathbb{E}W_2^2(\mu_n,\mu)/\log n \to 1/(4\pi)$ on the flat torus.
- **2019–2024.** Statistical era: minimax density estimation in $W_p$ (Niles-Weed–Berthet), entropic/Sinkhorn surrogates with $n^{-1/2}$ rates at fixed regularization (Genevay et al.; Chizat et al.), sharp rates for smooth costs (Manole–Niles-Weed), and adaptivity to the lower-complexity marginal (Hundrieser–Staudt–Munk).

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $d=1$, any $p\ge1$ | Exact: $W_p^p(\mu_n,\mu)=\int_0^1|F^{-1}-F_n^{-1}|^p$; complete moment characterisation of $\mathbb{E}W_p(\mu_n,\mu)$ | Bobkov–Ledoux (2019) |
| $d<2p$ | $\mathbb{E}W_p^p \asymp n^{-1/2}$ (parametric rate), CLT known | Fournier–Guillin (2015); del Barrio–Loubes (2019) |
| $d=2p$ | $\mathbb{E}W_p^p \asymp n^{-1/2}\log n$ | Fournier–Guillin (2015) |
| $d=2$, $p=2$, uniform on torus/square | Sharp constant: $\lim n\,\mathbb{E}W_2^2/\log n = 1/(4\pi)$ | Ambrosio–Stra–Trevisan (2019) |
| $d=2$, $p\in(1,2)$ and general domains | Sharp constant and Hölder densities | Ambrosio–Goldman–Trevisan (2022) |
| $d\ge3$, $p=1$ | Limit $n^{1/d}\mathbb{E}W_1 \to \beta(1,d)\int f^{(d-1)/d}$ exists | Dobrić–Yukich (1995) |
| Gaussian $\mu$, $d\ge3$ | Two-sided bounds with correct logarithmic corrections | Ledoux (2017) |
| $\mathrm{supp}(\mu)$ of Minkowski dimension $s<2p$ | $\mathbb{E}W_p^p \lesssim n^{-p/s}$, matching lower bound under regularity | Weed–Bach (2019) |
| $f\in C^s$, density estimation (not empirical measure) | Minimax rate $n^{-(s+1)/(2s+d)}$ in $W_1$, beating $n^{-1/d}$ | Niles-Weed–Berthet (2022) |
| Entropic OT, fixed $\varepsilon>0$ | $\mathbb{E}|S_\varepsilon(\mu_n,\mu)| \lesssim \varepsilon^{-d/2} n^{-1/2}$ | Genevay et al. (2019); Chizat et al. (2020) |

## 5. Principal Obstacles

- **Chaining is lossy at the sharp-constant level.** The dyadic/generic-chaining upper bound sums independent scale contributions; the true transport plan correlates scales. Chaining loses a constant factor at every level, and these compound into an unbounded error in the constant even though the exponent survives.
- **The PDE linearization fails below $d=3$'s regularity threshold.** In $d=2$, $\mu_n-\mu$ is close to white noise and $-\Delta u = \mu_n-\mu$ has $\dot H^{-1}$ norm computable by Fourier series. In $d\ge3$ the leading contribution comes from the *smallest* scale $n^{-1/d}$, where the empirical measure is atomic, not noise-like. Linearization is exactly invalid where the mass of the answer sits.
- **No exact subadditivity for $p>1$.** Dobrić–Yukich's proof for $p=1$ uses the Kantorovich dual and the fact that $W_1$ costs add across a partition of the cube up to boundary terms. For $p>1$, the concavity/subadditivity across cubes fails: transporting locally is not almost-optimal, and superadditivity arguments (Talagrand's) give only two-sided bounds with a gap.
- **Lower bounds are combinatorial, upper bounds are analytic.** Lower bounds come from counting empty cubes/mass deficits; upper bounds from function-class entropy. The two use disjoint information and only ever meet up to constants.
- **Concentration is degenerate.** $W_p(\mu_n,\mu)$ concentrates at scale $n^{-1/2}$ (bounded-differences), far tighter than its mean $n^{-1/d}$. So the fluctuation is a lower-order object invisible to standard concentration machinery — a CLT would need a completely different, local expansion.

## 6. The Gap

Proven: $c_1 n^{-1/d} \le \mathbb{E}W_p(\mu_n,\mu)\le c_2 n^{-1/d}$ for $d>2p$, with $c_2/c_1$ a dimension-dependent (and generally unquantified) factor, plus the full sharp answer at $d\le 2$ and at $p=1$.

Missing: the single step of showing that the rescaled cost $n^{p/d}W_p^p(\mu_n,\mu)$ *localizes* — that it decomposes, up to $o(1)$, into a sum over cells of side $\varepsilon \gg n^{-1/d}$ of independent local matching costs, each asymptotically the Poisson-process matching constant $\beta(p,d)$ times the local density factor $f^{(d-p)/d}$. For $p=1$ this localization is Dobrić–Yukich's subadditivity lemma. For $p>1$, no localization lemma exists: the obstruction is bounding the *cross-cell* transport, which for $p>1$ is not controlled by the mass imbalance alone.

## 7. Current Research (as of June 2026)

- **PDE/Sobolev school** (Ambrosio, Goldman, Trevisan, Trillos, Peyre–Otto): extending the $d=2$ regularization method upward; partial results for $d\ge3$ in the *semi-discrete* and *bipartite matching* settings. *(frontier — verify)* Reports of a rigorous localization at $d=3$ under smoothness of $f$ circulate as preprints but no complete constant.
- **Statistical OT** (Niles-Weed, Manole, Rigollet, Munk's Göttingen group, Bach/Chizat in Paris): shifting from empirical measures to *estimators* — wavelet, kernel, and smoothed plug-ins that achieve $n^{-(s+1)/(2s+d)}$ and thus dodge the curse when the density is smooth.
- **Entropic regularization** as an analytic bridge: rates interpolating between $\varepsilon^{-d/2}n^{-1/2}$ and $n^{-1/d}$ as $\varepsilon\to0$; the joint scaling $\varepsilon = \varepsilon(n)$ that recovers the unregularized constant is open.
- **Structured/low-dimensional models**: spiked transport, manifold supports, and $d^*_p(\mu)$-sharpness; the question of whether $d^*_p$ is *the* right functional for all $\mu$ (Question 3 above) is actively pursued.
- **High-dimensional asymptotics of $\beta(p,d)$**: the conjecture $\beta(2,d)^{1/2}\sim \sqrt{d/(2\pi e)}$ as $d\to\infty$, by analogy with quantization/random assignment constants. *(frontier — verify)*

## 8. Future Work

- Prove a **localization lemma** for $p>1$: control cross-cell transport by mass imbalance plus a lower-order term. This is the single identified bottleneck.
- Transfer **Poisson-process matching** results (where translation invariance gives exact subadditivity) back to i.i.d. samples via de-Poissonization at the level of constants, not orders.
- Develop a **second-order (fluctuation) expansion** for $W_p(\mu_n,\mu)$ in $d\ge3$; even identifying the variance order is open.
- Establish **matching minimax lower bounds** for smooth-density estimation in $W_p$ for $p>1$, closing the gap left by Niles-Weed–Berthet.
- Quantify the **$\varepsilon \to 0$, $n\to\infty$ joint limit** of Sinkhorn divergences.

## 9. Key References

- **[Foundational]** R. M. Dudley. *The speed of mean Glivenko–Cantelli convergence.* Annals of Mathematical Statistics 40 (1969), 40–50.
- **[Foundational]** M. Ajtai, J. Komlós, G. Tusnády. *On optimal matchings.* Combinatorica 4 (1984), 259–264.
- **[Foundational]** V. Dobrić, J. E. Yukich. *Asymptotics for transportation cost in high dimensions.* Journal of Theoretical Probability 8 (1995), 97–118.
- **[SOTA]** N. Fournier, A. Guillin. *On the rate of convergence in Wasserstein distance of the empirical measure.* Probability Theory and Related Fields 162 (2015), 707–738.
- **[SOTA]** J. Weed, F. Bach. *Sharp asymptotic and finite-sample rates of convergence of empirical measures in Wasserstein distance.* Bernoulli 25 (2019), 2620–2648.
- **[SOTA]** L. Ambrosio, F. Stra, D. Trevisan. *A PDE approach to a 2-dimensional matching problem.* Probability Theory and Related Fields 173 (2019), 433–477.
- **[SOTA]** L. Ambrosio, M. Goldman, D. Trevisan. *On the quadratic random matching problem in two-dimensional domains.* Electronic Journal of Probability 27 (2022), paper 129.
- **[SOTA]** T. Manole, J. Niles-Weed. *Sharp convergence rates for empirical optimal transport with smooth costs.* Annals of Applied Probability 34 (2024), 1108–1135.
- **[SOTA]** J. Niles-Weed, Q. Berthet. *Minimax estimation of smooth densities in Wasserstein distance.* Annals of Statistics 50 (2022), 1519–1540.
- **[SOTA]** E. del Barrio, J.-M. Loubes. *Central limit theorems for empirical transportation cost in general dimension.* Annals of Probability 47 (2019), 926–951.
- **[SOTA]** S. Hundrieser, T. Staudt, A. Munk. *Empirical optimal transport between different measures adapts to lower complexity.* Annales de l'Institut Henri Poincaré (B) 60 (2024).
- **[SOTA]** A. Genevay, L. Chizat, F. Bach, M. Cuturi, G. Peyré. *Sample complexity of Sinkhorn divergences.* AISTATS 2019, PMLR 89, 1574–1583.
- **[Survey]** S. Bobkov, M. Ledoux. *One-dimensional empirical measures, order statistics, and Kantorovich transport distances.* Memoirs of the AMS 261 (2019), no. 1259.
- **[Survey]** M. Talagrand. *Upper and Lower Bounds for Stochastic Processes.* Springer, 2014.
- **[Survey]** C. Villani. *Optimal Transport: Old and New.* Grundlehren der mathematischen Wissenschaften 338, Springer, 2009.
- **[Survey]** G. Peyré, M. Cuturi. *Computational Optimal Transport.* Foundations and Trends in Machine Learning 11 (2019), 355–607.

## 10. Worked Example / Concrete Special Case

**Case $d=1$, $p=1$, $\mu=\mathrm{Unif}[0,1]$ — the constant is computable exactly.**

In one dimension $W_1(\mu_n,\mu)=\int_0^1 |F_n(t)-F(t)|\,dt$ with $F(t)=t$. For fixed $t$, $nF_n(t)\sim\mathrm{Bin}(n,t)$, so by the CLT $\sqrt{n}(F_n(t)-t)\Rightarrow \mathcal{N}(0,t(1-t))$ and $\mathbb{E}|Z|=\sqrt{2\sigma^2/\pi}$ gives
$$\sqrt{n}\,\mathbb{E}|F_n(t)-t| \longrightarrow \sqrt{\tfrac{2}{\pi}}\sqrt{t(1-t)} .$$
Integrating (uniform integrability holds since $|F_n-F|\le1$), and using $\int_0^1\sqrt{t(1-t)}\,dt=\pi/8$:
$$\lim_{n\to\infty}\sqrt{n}\;\mathbb{E}\,W_1(\mu_n,\mu) \;=\; \sqrt{\tfrac{2}{\pi}}\cdot\frac{\pi}{8}\;=\;\sqrt{\frac{\pi}{32}}\;\approx\;0.31333 .$$
Both the rate $n^{-1/2}$ and the constant are exact. This matches $d<2p$ in the table.

**Contrast: $d=3$, $p=1$, $\mu=\mathrm{Unif}[0,1]^3$ — lower bound by cube counting.**

Partition $[0,1]^3$ into $m^3$ cubes of side $1/m$ with $m=\lfloor n^{1/3}\rfloor$, so each cube has expected count $n/m^3\approx1$. Let $N_Q$ be the sample count in cube $Q$. Any transport plan must move the excess mass $\frac1n(N_Q - n/m^3)^+$ out of $Q$ over distance at least $\Omega(1/m)$ if the neighbouring cells are also saturated; a standard test-function argument with a $1/m$-Lipschitz bump $\varphi_Q$ gives
$$\mathbb{E}\,W_1(\mu_n,\mu)\;\gtrsim\;\frac{1}{m}\cdot\frac{1}{m^3}\sum_{Q}\mathbb{E}\Big|\tfrac{N_Q}{n} \cdot m^3 - 1\Big| \;\gtrsim\;\frac{1}{m}\cdot c \;\asymp\; n^{-1/3},$$
since $N_Q$ is asymptotically Poisson$(1)$ and $\mathbb{E}|N_Q-1|=2/e>0$ is bounded away from zero. Combined with Fournier–Guillin's matching $O(n^{-1/3})$ upper bound, the exponent is settled.

**Where the open problem bites.** The lower bound above yields a constant of order $\tfrac{2}{e}\cdot(\text{geometric factor})$; the upper bound's constant comes from summing dyadic scales and is larger by a factor that no argument currently controls. The true value $\beta(1,3)=\lim n^{1/3}\mathbb{E}W_1(\mu_n,\mathrm{Unif}[0,1]^3)$ is *known to exist* by Dobrić–Yukich but its numerical value is unknown; numerically it is estimated near $0.65$ *(frontier — verify)*. For $p=2$ in $d=3$, even existence of $\lim n^{2/3}\mathbb{E}W_2^2$ is open — that is precisely Question 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*