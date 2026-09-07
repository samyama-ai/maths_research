---
id: 09-probability/kesten-stumpf-conjecture-on-random-walks
title: "Kesten-Stumpf Conjecture on Conditioned Random Walks"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kesten-Stumpf Conjecture on Conditioned Random Walks

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/kesten-stumpf-conjecture-on-random-walks` · **Status:** partially-solved

*Naming note: the label used here is a catalog convention for a problem cluster whose analytic content descends from Kesten's ratio theorems for random walks (1963) and from the modern theory of walks in cones. It is not a universally standardized name; the mathematical statements below are the ones to check against the literature.*

## 1. Problem Statement / Conjecture

Let $X, X_1, X_2, \dots$ be i.i.d. random vectors in $\mathbb{R}^d$ with $\mathbb{E}X = 0$ and identity covariance, and let $S_n = x + X_1 + \dots + X_n$. Let $K \subset \mathbb{R}^d$ be an open cone with apex $0$ whose intersection with the unit sphere is a regular domain, and let
$$\tau_x := \inf\{n \ge 1 : S_n \notin K\}, \qquad S_0 = x \in K .$$
Let $p = p(K) > 0$ be the homogeneity exponent of the (unique) positive harmonic function of Brownian motion killed on exiting $K$.

**Conjecture (three parts).**

**(A) Sharpness of the moment threshold.** The classical asymptotic
$$\mathbb{P}(\tau_x > n) \;\sim\; \varkappa\, V(x)\, n^{-p/2}, \qquad n \to \infty,$$
holds **if and only if** $\mathbb{E}|X|^{p} < \infty$ (with the convention that no condition beyond finite variance is imposed when $p \le 2$). In particular, the moment condition of Denisov–Wachtel (2015) cannot be weakened.

**(B) Big-jump regime.** If instead $\mathbb{P}(|X| > t)$ is regularly varying of index $-\alpha$ with $2 < \alpha < p$, then
$$\mathbb{P}(\tau_x > n) \;\asymp\; n^{-\alpha/2},$$
and, conditionally on $\{\tau_x > n\}$, survival is realized by a *single* jump of order $\sqrt{n}$ into the interior of $K$ occurring at a time $O(1)$; the rescaled path $(S_{\lfloor nt \rfloor}/\sqrt n)_{t\in[0,1]}$ converges to a Brownian motion started from a random interior point and conditioned only to remain in $K$.

**(C) Uniqueness of the discrete harmonic function.** Under $\mathbb{E}|X|^2 < \infty$ alone, the killed walk on $K$ admits, up to positive scalars, a *unique* positive harmonic function $V$, i.e. a unique solution of
$$V(x) = \mathbb{E}\!\left[V(x + X)\,\mathbf{1}\{x + X \in K\}\right], \quad x \in K, \qquad V > 0 \text{ on } K,$$
so the minimal Martin boundary of the killed walk in a cone is a single point.

A complete resolution requires (i) a counterexample walk with $\mathbb{E}|X|^{p} = \infty$ violating (A), (ii) matching upper and lower bounds establishing (B), and (iii) a Martin boundary identification for (C) with no moment assumption beyond variance.

## 2. Mathematical Foundations

**Cone and its exponent.** Write $\Sigma = K \cap \mathbb{S}^{d-1}$. Let $\lambda_1 > 0$ be the principal Dirichlet eigenvalue of the Laplace–Beltrami operator $\Delta_{\mathbb{S}^{d-1}}$ on $\Sigma$ with eigenfunction $m_1 > 0$:
$$\Delta_{\mathbb{S}^{d-1}} m_1 = -\lambda_1 m_1 \text{ on } \Sigma, \qquad m_1|_{\partial\Sigma}=0 .$$
Then
$$u(x) := |x|^{p}\, m_1\!\left(\tfrac{x}{|x|}\right), \qquad p = \sqrt{\lambda_1 + \left(\tfrac{d-2}{2}\right)^{2}} - \tfrac{d-2}{2},$$
is harmonic ($\Delta u = 0$) in $K$ and vanishes on $\partial K$. For Brownian motion $B$ with exit time $\tau^{bm}_x$,
$$\mathbb{P}(\tau^{bm}_x > t) \;\sim\; \varkappa_0\, u(x)\, t^{-p/2}, \qquad t \to \infty .$$
Examples: $K = (0,\infty)$ gives $p = 1$, $u(x)=x$; $K = (0,\infty)^2$ gives $p = 2$, $u(x,y)=xy$; the Weyl chamber $K = \{x_1 < \dots < x_d\}$ gives $p = d(d-1)/2$ with $u$ the Vandermonde determinant $\prod_{i<j}(x_j - x_i)$.

**Discrete harmonic function.** Denisov and Wachtel construct
$$V(x) = \lim_{n\to\infty} \mathbb{E}\!\left[u(S_n)\,\mathbf{1}\{\tau_x > n\}\right],$$
the limit existing because $u(S_{n \wedge \tau_x})$ is a submartingale of bounded increments in the relevant scale. $V$ satisfies $V(x)/u(x) \to 1$ as $\mathrm{dist}(x,\partial K)\to\infty$.

**Doob $h$-transform.** The walk conditioned to stay in $K$ forever is the Markov chain with kernel
$$\hat{P}(x,\mathrm{d}y) = \frac{V(y)}{V(x)}\,P(x,\mathrm{d}y)\,\mathbf{1}\{y \in K\},$$
which is honest exactly because $V$ is harmonic. Part (C) is the assertion that this $h$-process is canonical.

**One-dimensional backbone.** For $d=1$, Sparre Andersen's identity gives
$$\sum_{n\ge 0}\mathbb{P}(\tau_0 > n)\,s^{n} = \exp\!\left(\sum_{n\ge1}\frac{s^{n}}{n}\,\mathbb{P}(S_n > 0)\right),$$
so under Spitzer's condition $\frac1n\sum_{k\le n}\mathbb{P}(S_k>0)\to \rho$ the tail $\mathbb{P}(\tau_0>n)$ is regularly varying of index $-\rho$; finite variance gives $\rho = 1/2$, i.e. $p=1$. No further moments are needed — the fact that motivates the conjectured threshold $\mathbb{E}|X|^p$, vacuous at $p=1$.

## 3. History & State of the Art (SOTA)

- **1963.** Kesten's ratio theorems for random walks give the first systematic renewal-type asymptotics for killed walks, and Spitzer's fluctuation theory supplies the $d=1$ machinery.
- **1994.** Bertoin and Doney construct the random walk conditioned to stay nonnegative as a Doob $h$-transform with $h$ the renewal function of strict descending ladder heights, and prove it is the weak limit of the walk conditioned on $\{\tau > n\}$.
- **2008.** Caravenna–Chaumont prove functional invariance principles for conditioned walks (limit: Brownian meander / Bessel(3) bridge); Eichelsbacher–König handle ordered random walks in the Weyl chamber under strong moment assumptions.
- **2009.** Vatutin–Wachtel obtain local limit theorems for walks conditioned to stay positive, including the non-finite-variance stable regime.
- **2015 (SOTA).** Denisov–Wachtel, *Random walks in cones* (Ann. Probab. 43): for general regular cones, $\mathbb{P}(\tau_x>n)\sim \varkappa V(x)n^{-p/2}$ and the corresponding conditional invariance principle toward the Brownian motion in $K$ conditioned to stay in $K$, under $\mathbb{E}|X|^{p}<\infty$ (and $\mathbb{E}|X|^{2}<\infty$ always; $p \vee 2$ in practice). This is the theorem whose hypotheses Part (A) asserts to be sharp.
- **2019–2020.** Denisov–Wachtel give alternative constructions of $V$; Duraj–Wachtel prove invariance principles under weaker regularity; Duraj (2014) and Garbit–Raschel (2016) settle the nonzero-drift case, where the decay is exponential with a polynomial correction.
- **Uniqueness/Martin boundary.** Ignatiouk-Robert's work on killed walks in half-spaces and on cones, and Bouaziz–Mustapha–Sifi for orthants under exponential-moment or Cramér-type assumptions, give (C) in restricted settings.

## 4. Partial Results / Verified Cases

- **$d = 1$, $K=(0,\infty)$, $p=1$:** fully solved. Finite variance (indeed, only the domain-of-attraction/Spitzer condition) yields $\mathbb{P}(\tau_x>n)\sim c\,V(x)n^{-1/2}$ with $V$ the ladder renewal function; uniqueness of $V$ is classical. Consistent with (A) since $\mathbb{E}|X|^{1}<\infty$ is automatic.
- **$p \le 2$ cones** (half-spaces, quadrant in $d=2$, any cone with $\lambda_1$ small enough): the Denisov–Wachtel condition $\mathbb{E}|X|^{p}<\infty$ is implied by finite variance, so (A) holds trivially and the asymptotic is a theorem.
- **Cones with $p > 2$ under $\mathbb{E}|X|^{p}<\infty$:** the "only if" direction of (A) — sufficiency — is Denisov–Wachtel (2015). What is open is necessity.
- **Weyl chambers / ordered walks:** $p=d(d-1)/2$; asymptotics and Dyson-Brownian-motion limits proven under moment conditions much weaker than Eichelsbacher–König's original ones, but still $p$-dependent.
- **Lattice walks in $\mathbb{Z}^2_{\ge0}$ with finite step sets:** exact exponents and constants are known by analytic combinatorics (Fayolle–Iasnogorodski–Malyshev, Raschel, Bostan et al.); all such walks have bounded steps, so all moments exist and (A)–(C) are non-issues there. They serve as an exact-solution testbed.
- **Nonzero drift:** for drift pointing out of $K$, Duraj (2014) and Garbit–Raschel (2016) give $\mathbb{P}(\tau_x>n) \asymp \rho^{n} n^{-p/2 - ?}$-type asymptotics under Cramér conditions; the polynomial correction is governed by the same $p$.
- **Exponential moments:** under $\mathbb{E}e^{\delta|X|}<\infty$, (C) is known for orthants and half-spaces via Martin boundary methods (Ignatiouk-Robert; Bouaziz–Mustapha–Sifi).

## 5. Principal Obstacles

- **Submartingale control breaks.** The core of Denisov–Wachtel is showing $u(S_{n\wedge\tau})$ is nearly a martingale with controllable increments. The error term involves $\mathbb{E}[u(x+X) - u(x)]$, and since $u$ grows like $|x|^{p}$, its Taylor remainder is only integrable when $\mathbb{E}|X|^{p}<\infty$. With fewer moments the compensator diverges and the whole normalization is lost. No substitute functional with slower growth is known that is still harmonic for the cone.
- **Coupling with Brownian motion.** The KMT/Sakhanenko strong approximation error over $n$ steps is $o(\sqrt n)$ only with matching moments; the boundary of $K$ must be resolved at scale $o(\sqrt n)$, so weakening moments destroys the coupling exactly where it is needed.
- **No Wiener–Hopf in $d\ge 2$.** In $d=1$ the ladder-structure factorization is exact and moment-free; there is no multidimensional analogue for a general cone, so the moment-free 1D proofs cannot be lifted.
- **Boundary geometry.** Near a non-smooth $\partial K$ (edges, corners), $u$ has unbounded derivatives, and estimates of the form $|u(x+y)-u(x)| \lesssim |y|\,|x|^{p-1}$ fail; harmonic-measure estimates in Lipschitz cones lose the uniformity needed for a big-jump decomposition.
- **Martin boundary methods need Cramér.** Large-deviation-based identification of positive harmonic functions (Ignatiouk-Robert) uses the existence of an exponential moment to build the twisted walks; under only finite variance the associated rate function is degenerate.

## 6. The Gap

Proven: sufficiency of $\mathbb{E}|X|^{p}<\infty$ for the $n^{-p/2}$ asymptotic and the conditional invariance principle in regular cones. Conjectured: that this is exactly the threshold, and that below it a single-big-jump mechanism replaces it.

The precise missing step is a **two-sided estimate that separates the "diffusive" and "one big jump" contributions**:
$$\mathbb{P}(\tau_x>n) \;\asymp\; V_{\text{trunc}}(x)\,n^{-p/2} \;+\; n\,\mathbb{P}\big(|X| > \sqrt{n},\; \text{jump lands deep in } K\big).$$
The lower bound is straightforward (condition on one big jump); the **upper bound is the barrier**: it requires ruling out survival strategies built from many moderate jumps, which needs a maximal inequality for $u(S_{n\wedge\tau})$ valid without $p$-th moments. For (C), the gap is between "a positive harmonic function exists (Denisov–Wachtel construction)" and "the cone of positive harmonic functions is one-dimensional" without exponential moments.

## 7. Current Research (as of June 2026)

- **Augsburg / Bielefeld (Wachtel and collaborators)** continue the program on harmonic functions for killed walks: alternative constructions, integrated random walks, and walks with dependent increments. Extensions to Markov-modulated and self-interacting walks are active. *(frontier — verify)*
- **Tours / CNRS (Raschel and coauthors)** work on exact asymptotics for walks in cones via analytic combinatorics and boundary value problems, providing exactly solvable benchmarks against which conjectured constants $\varkappa$ can be tested.
- **Heavy-tail school (Aachen/Munich/Moscow).** Big-jump principles for constrained functionals of random walks are being adapted to cone-exit problems; the "one big jump" description in Part (B) is the natural target. *(frontier — verify)*
- **Martin boundary program (Ignatiouk-Robert and school).** Extension of boundary identification beyond Cramér-type assumptions, using $t$-Martin boundaries and Harnack inequalities at the boundary of cones. *(frontier — verify)*
- **Numerical/simulation work.** Monte Carlo estimates of $\mathbb{P}(\tau>n)$ for Pareto-$\alpha$ increments in Weyl chambers ($p=3,6$) are consistent with the $n^{-\alpha/2}$ prediction of Part (B) for $2<\alpha<p$; no published proof matches it. *(frontier — verify)*

## 8. Future Work

- Build a **truncated harmonic function** $V_T$ adapted to the walk with jumps capped at $T=\varepsilon\sqrt n$, prove the diffusive asymptotic for the truncated walk, and control the truncation error by a big-jump expansion. This is the most concrete route to (A) and (B).
- Establish a **boundary Harnack principle for killed random walks** in Lipschitz cones under only finite variance; this would deliver (C) immediately by standard Martin boundary arguments.
- Test sharpness on exactly solvable cases: place a Pareto tail on a lattice walk in $\mathbb{Z}^2_{\ge0}$ where the finite-step-set asymptotics are known exactly, and compare.
- Extend to **integrated random walks** and other degenerate cones where $p$ is non-integer (e.g. $p=1/4$ for the integrated walk persistence exponent), where moment thresholds have a different flavor.

## 9. Key References

- **[Foundational]** H. Kesten. *Ratio theorems for random walks II.* Journal d'Analyse Mathématique 11 (1963), 323–379.
- **[Foundational]** F. Spitzer. *Principles of Random Walk.* 2nd ed., Springer, 1976.
- **[Foundational]** J. Bertoin, R. A. Doney. *On conditioning a random walk to stay nonnegative.* Annals of Probability 22 (1994), 2152–2167.
- **[SOTA]** D. Denisov, V. Wachtel. *Random walks in cones.* Annals of Probability 43 (2015), no. 3, 992–1044.
- **[SOTA]** D. Denisov, V. Wachtel. *Alternative constructions of a harmonic function for a random walk in a cone.* Electronic Journal of Probability 24 (2019), paper no. 92.
- **[SOTA]** J. Duraj, V. Wachtel. *Invariance principles for random walks in cones.* Stochastic Processes and their Applications 130 (2020), 3920–3942.
- **[Recent]** J. Duraj. *Random walks in cones: the case of nonzero drift.* Stochastic Processes and their Applications 124 (2014), 1503–1518.
- **[Recent]** R. Garbit, K. Raschel. *On the exit time from a cone for random walks with drift.* Revista Matemática Iberoamericana 32 (2016), 511–532.
- **[Recent]** V. A. Vatutin, V. Wachtel. *Local probabilities for random walks conditioned to stay positive.* Probability Theory and Related Fields 143 (2009), 177–217.
- **[Recent]** F. Caravenna, L. Chaumont. *Invariance principles for random walks conditioned to stay positive.* Annales de l'IHP Probabilités et Statistiques 44 (2008), 170–190.
- **[Recent]** P. Eichelsbacher, W. König. *Ordered random walks.* Electronic Journal of Probability 13 (2008), 1307–1336.
- **[Survey]** G. Fayolle, R. Iasnogorodski, V. Malyshev. *Random Walks in the Quarter Plane: Algebraic Methods, Boundary Value Problems, Applications to Queueing Systems and Analytic Combinatorics.* 2nd ed., Springer, 2017.
- **[Survey]** K. Raschel. *Random walks in the quarter plane, discrete harmonic functions and conformal mappings.* Stochastic Processes and their Applications 124 (2014), 3147–3178.
- **[Related]** I. Ignatiouk-Robert. *Martin boundary of a killed random walk on a half-space.* Journal of Theoretical Probability 21 (2008), 35–68.

## 10. Worked Example / Concrete Special Case

**(i) The half-line, $p=1$.** Take simple random walk on $\mathbb{Z}$, $S_0=1$, $K=(0,\infty)$. The reflection principle gives, for the first hitting time of $0$,
$$\mathbb{P}(\tau_1 > 2n) = \binom{2n}{n}2^{-2n} \sim \frac{1}{\sqrt{\pi n}} .$$
Here $V(x)=x$ is exactly harmonic: $\tfrac12\big((x+1)+(x-1)\big)=x$ for $x\ge2$, and at $x=1$ the killed step contributes $\tfrac12\cdot 2 \cdot \mathbf{1}\{\cdot\} = 1$. The exponent $p/2=1/2$ matches $p=1$, and no moment beyond variance is used.

**(ii) The quadrant, $p=2$.** Take $K=(0,\infty)^2$ and a walk whose two coordinates are independent copies of (i). Then $\tau = \tau^{(1)}\wedge\tau^{(2)}$ and
$$\mathbb{P}(\tau_{(1,1)}>2n) = \left(\binom{2n}{n}2^{-2n}\right)^{2} \sim \frac{1}{\pi n} = \Theta(n^{-p/2}), \quad p=2,$$
with $V(x,y)=xy = u(x,y)$. Since $p=2$, the Denisov–Wachtel condition is just finite variance: (A) is a theorem here.

**(iii) Where the threshold should bite: $p=3$.** Take $d=3$ and the Weyl chamber $K=\{x_1<x_2<x_3\}$, so $p = 3\cdot2/2 = 3$ and $u = \prod_{i<j}(x_j-x_i)$. Let the increments have i.i.d. symmetric Pareto coordinates with $\mathbb{P}(|X|>t)=t^{-\alpha}$, $t\ge1$, and $2 < \alpha < 3$. Then $\mathbb{E}|X|^2<\infty$ but $\mathbb{E}|X|^{3}=\infty$, so Denisov–Wachtel does not apply.

Lower bound by one big jump: for the walk to survive $n$ steps, it suffices that the first step lands at distance $\ge M\sqrt n$ inside $K$ (an event of probability $\asymp c_M n^{-\alpha/2}$), after which the diffusive approximation gives survival probability bounded below by a constant $q(M) \to 1$ as $M\to\infty$. Hence
$$\mathbb{P}(\tau_x>n) \;\ge\; c\, n^{-\alpha/2} \;\gg\; n^{-3/2}.$$
So the $n^{-p/2}$ law **fails** for this walk, which is the content of the "only if" half of (A). What is *not* proven is the matching upper bound $\mathbb{P}(\tau_x>n) \le C n^{-\alpha/2}$: excluding survival built from many jumps of intermediate size $n^{\beta}$, $0<\beta<1/2$, requires a maximal inequality for $u(S_{n\wedge\tau})$ that no current method supplies without $\mathbb{E}|X|^{p}<\infty$. That single missing inequality is the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*