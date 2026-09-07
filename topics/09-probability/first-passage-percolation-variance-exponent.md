---
id: 09-probability/first-passage-percolation-variance-exponent
title: "First-Passage Percolation Variance Exponent"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# First-Passage Percolation Variance Exponent

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/first-passage-percolation-variance-exponent` · **Status:** open

## 1. Problem Statement / Conjecture

Put i.i.d. non-negative weights $(\tau_e)_{e \in E(\mathbb{Z}^d)}$ on the nearest-neighbour edges of $\mathbb{Z}^d$ and let $T(x,y)$ be the minimal total weight of a lattice path from $x$ to $y$. The **variance exponent** $\chi$ is defined (when it exists) by

$$\operatorname{Var} T(0, n e_1) = n^{2\chi + o(1)}, \qquad n \to \infty .$$

**Conjecture (KPZ prediction for FPP).** For $d = 2$ and any weight distribution in the KPZ universality class (non-degenerate, sufficient moments, $\mathbb{P}(\tau = \tau_{\min}) < p_c$),

$$\chi = \tfrac13, \qquad \xi = \tfrac23,$$

where $\xi$ is the transversal (wandering) exponent of the geodesic, and moreover $n^{-1/3}\big(T(0,ne_1) - \mathbb{E}T(0,ne_1)\big)$ converges to a Tracy–Widom GUE law up to scale.

A complete solution requires, at minimum: (i) proof that $\operatorname{Var} T(0,ne_1) = n^{2/3+o(1)}$ for one non-solvable i.i.d. weight distribution; (ii) proof of universality — the exponent does not depend on the law of $\tau$; (iii) identification of $\chi(d)$ for $d \ge 3$, where even the conjectural value is unknown (the upper critical dimension question). Disproof would consist of a distribution with $\liminf$ and $\limsup$ exponents differing from $1/3$, or a proof that no exponent exists.

## 2. Mathematical Foundations

**Passage time.** For a finite path $\gamma$, $T(\gamma) = \sum_{e \in \gamma} \tau_e$, and
$$T(x,y) = \inf\{ T(\gamma) : \gamma \text{ a path from } x \text{ to } y \}.$$
A minimizing path is a **geodesic**; it exists a.s. and is unique when $\tau$ is continuous.

**Shape theorem (Cox–Durrett).** If $\mathbb{E}\big[\min_{i=1}^{2d} \tau_i^d\big] < \infty$ then there is a norm $g$ on $\mathbb{R}^d$ (the time constant) with
$$\lim_{n\to\infty} \frac{T(0,\lfloor nx \rfloor)}{n} = g(x) \quad \text{a.s. and in } L^1,$$
and $B_t/t \to \mathcal{B} = \{x : g(x) \le 1\}$ in Hausdorff distance, where $B_t = \{x : T(0,x) \le t\}$. Subadditivity ($T(0,x+y) \le T(0,x) + T(x,x+y)$) plus Kingman's theorem gives existence of $g$.

**Exponents.** With $F_n = T(0,ne_1) - \mathbb{E}T(0,ne_1)$,
$$\chi = \lim \frac{\log \operatorname{Var}(F_n)}{2\log n}, \qquad \xi = \inf\Big\{ a>0 : \text{geodesic to } ne_1 \text{ stays in a cylinder of radius } n^{a} \text{ w.h.p.}\Big\}.$$

**KPZ scaling relation.** Chatterjee (2013), refined by Auffinger–Damron (2014):
$$\chi = 2\xi - 1$$
holds whenever the exponents exist in a suitable (mean-based) sense; in $d=2$, $(\chi,\xi)=(1/3,2/3)$ is the unique solution consistent with the conjectured $\xi$.

**Wehr–Aizenman / Newman–Piza inequality.**
$$\chi \ \ge\ \frac{1 - (d-1)\xi}{2}.$$

**Variance machinery.** Efron–Stein: if $T^{(e)}$ resamples $\tau_e$,
$$\operatorname{Var}(T) \le \tfrac12 \sum_e \mathbb{E}\big[(T - T^{(e)})^2\big].$$
Talagrand's $L^1$–$L^2$ inequality (basis of BKS): for $f$ of $n$ i.i.d. bits,
$$\operatorname{Var}(f) \le C \sum_{i} \frac{\|\partial_i f\|_2^2}{1 + \log\big(\|\partial_i f\|_2 / \|\partial_i f\|_1\big)} .$$

## 3. History & State of the Art (SOTA)

- **1965.** Hammersley and Welsh introduce FPP as a model of fluid flow in random media; subadditive ergodic theory is developed in the same paper.
- **1981–1986.** Cox–Durrett prove the shape theorem under minimal moments; Kesten's Saint-Flour lectures (1986) set the modern agenda, including the fluctuation question.
- **1986–1993.** Kesten proves $\operatorname{Var} T(0,ne_1) \le Cn$ (so $\chi \le 1/2$) under an exponential moment, plus concentration of order $\sqrt{n}$ — the first non-trivial upper bound, unimproved at the polynomial scale to this day.
- **1990–1996.** Wehr–Aizenman and Newman–Piza establish lower bounds: divergence of the variance, $\operatorname{Var} \ge c\log n$ in $d=2$ for Bernoulli-type weights, and the exponent inequality $\chi \ge (1-(d-1)\xi)/2$. Licea–Newman–Piza obtain $\xi' \ge 3/5$ in $d=2$ for a modified transversal exponent, and $\xi' \le 3/4$.
- **1999–2000.** Baik–Deift–Johansson and Johansson prove $\chi = 1/3$ and Tracy–Widom GUE limits for *exactly solvable* last-passage percolation (exponential/geometric weights, Poissonian Hammersley model). This fixes the conjectural value for FPP by universality heuristics.
- **2003.** Benjamini–Kalai–Schramm: sublinear variance, $\operatorname{Var} T(0,ne_1) \le Cn/\log n$, for two-valued weights — the first improvement over Kesten.
- **2008–2015.** Benaïm–Rossignol extend BKS to "nearly gamma" laws with exponential concentration; Damron–Hanson–Sosoe extend $O(n/\log n)$ to general distributions with $\mathbb{E}[\tau^2 \log \tau] < \infty$.
- **2013–2014.** Chatterjee proves $\chi = 2\xi-1$ (superconcentration framework); Auffinger–Damron give a simplified proof under weaker hypotheses.
- **2022–2024.** Dembin–Elboim–Peled resolve the BKS midpoint problem and prove quantitative coalescence of geodesics in planar FPP, giving a polylogarithmic improvement on the variance upper bound *(frontier — verify)*.

**SOTA in $d=2$, general i.i.d. weights:**
$$c \log n \ \le\ \operatorname{Var} T(0,ne_1) \ \le\ C\, \frac{n}{\log n}.$$
No power-law improvement on either side is known.

## 4. Partial Results / Verified Cases

- **Exactly solvable LPP, $\chi = 1/3$ proven.** Corner-growth model with i.i.d. $\mathrm{Exp}(1)$ or geometric site weights (Johansson 2000): $G(n,n) \approx 4n$, fluctuations of order $n^{1/3}$ with Tracy–Widom GUE limit. Same for the Poissonian Hammersley/longest-increasing-subsequence model (Baik–Deift–Johansson 1999) and the log-gamma directed polymer at stationarity (Seppäläinen 2012).
- **Stationary/Busemann methods.** Balázs–Cator–Seppäläinen (2006) prove $\operatorname{Var} \asymp n^{2/3}$ and $\xi = 2/3$ for exponential LPP and Hammersley's process by a purely probabilistic (non-determinantal) route.
- **Exponential FPP on $\mathbb{Z}^2$ is *not* covered:** the solvable results are for *directed* last-passage, not undirected FPP.
- **Upper bounds.** $\chi \le 1/2$ in all $d \ge 2$ (Kesten 1993, exponential moment). $\operatorname{Var} = O(n/\log n)$ for all $d\ge 2$ with $\mathbb{E}[\tau^2\log\tau]<\infty$ (Damron–Hanson–Sosoe 2015).
- **Lower bounds.** $\operatorname{Var} \ge c\log n$ in $d = 2$ for Bernoulli weights (Newman–Piza 1995; Pemantle–Peres for related models), extended to general non-degenerate distributions by Damron–Hanson–Houdré–Xu (2020).
- **Scaling relation.** $\chi = 2\xi - 1$ holds unconditionally in the mean-exponent formulation, all $d \ge 2$ (Chatterjee 2013; Auffinger–Damron 2014).
- **Transversal exponent, $d=2$.** $3/5 \le \xi' \le 3/4$ for the Licea–Newman–Piza variants; combined with $\chi = 2\xi-1$ these do not close on $1/3$.
- **Convergence rate.** $\mathbb{E}T(0,ne_1) - n g(e_1) = O(\sqrt{n}\log n)$ (Alexander 1997), and $\Omega(\log n)$ lower bounds for the non-random correction.

## 5. Principal Obstacles

- **No integrable structure.** All proofs of $\chi = 1/3$ rest on determinantal formulas, RSK correspondence, or Burke-type stationarity — each available only for one specific weight law and only in the *directed* (LPP/polymer) setting. Undirected FPP with a general law admits no exact transition kernel, no Schur measure, and no stationary Busemann field with explicit marginals.
- **The logarithmic barrier of hypercontractivity.** Talagrand's $L^1$–$L^2$ bound converts "all influences are small" into a $1/\log$ gain and nothing more. Since the total influence $\sum_e \mathrm{Inf}_e \asymp \mathbb{E}|\text{geodesic}| \asymp n$ and each influence is $n^{-1+o(1)}$, the method saturates at $n/\log n$. Reaching $n^{2/3}$ needs a polynomial gain, i.e. a genuinely different concentration mechanism.
- **Sub-additivity is too weak.** Kingman-type arguments control $\mathbb{E}T$ but say nothing about second-order structure; the martingale/Efron–Stein decompositions they support give exactly $\operatorname{Var} \le C\,\mathbb{E}|\text{geodesic}| \le Cn$.
- **Geodesic geometry is largely unknown.** Bounding $\xi$ from above requires ruling out long geodesic excursions; bounding it from below requires constructing them. Existence and uniqueness of semi-infinite geodesics in fixed directions, and non-existence of bigeodesics, remain open for general weights in $d=2$ — so the $\chi = 2\xi-1$ relation cannot be closed from either end.
- **Lower bounds are structurally hard.** Any lower bound must exhibit macroscopic randomness. Known arguments produce a single-edge contribution ($\log n$ from a martingale/entropy argument) and cannot aggregate $n^{2/3}$ worth of correlated fluctuation without knowing the geodesic's transversal spread.
- **No FKG or monotonicity in the right direction.** $T$ is a min over paths: it is concave and 1-Lipschitz in the weights, but the geodesic is not a monotone function of the environment, blocking Russo/OSSS-type derivative formulas that succeed in Bernoulli percolation.

## 6. The Gap

Proven: $c\log n \le \operatorname{Var} T_n \le Cn/\log n$, i.e.
$$0 \le \chi \le \tfrac12 \quad \text{(with the caveat that $\chi$ is not known to exist).}$$
Conjectured: $\chi = 1/3$. The gap is therefore **the entire polynomial scale** — no bound of the form $\operatorname{Var} \le n^{1-\delta}$ or $\operatorname{Var} \ge n^{\delta}$ is known for any $\delta > 0$ in undirected FPP with general weights.

The precise missing step is a *quantitative geodesic-coalescence estimate*: a bound showing that geodesics from $0$ to $ne_1$ and from a nearby point coalesce within distance $n^{2/3+o(1)}$, with a power-law probability tail. Such an estimate would feed into the Chatterjee/Auffinger–Damron relation and into a chaos/superconcentration argument to upgrade $1/\log n$ to $n^{-1/3}$. Equivalently: transfer the KPZ scaling proven for the *directed landscape* (Dauvergne–Virág) to a model with no exact solvability.

## 7. Current Research (as of June 2026)

- **Geodesic structure programme.** Dembin, Elboim and Peled (ETH Zürich / Weizmann / Tel Aviv & IAS) have driven the coalescence route: resolution of the BKS midpoint problem and quantitative coalescence in planar FPP, yielding variance bounds $O(n/\log n)$ improved by additional log factors and strong bounds on geodesic tree structure *(frontier — verify the exact exponent claimed in the latest version)*.
- **Superconcentration and chaos.** Chatterjee's framework (Courant/Berkeley school) ties $\chi < 1/2$ to disorder chaos and multiple-valley structure; ongoing work seeks a spectral/Fourier-weight criterion for polynomial superconcentration.
- **Variational and empirical-measure methods.** Bates (NC State) develops a variational formula for the time constant via empirical weight distributions along geodesics, giving new differentiability and shape-boundary results.
- **Integrable-to-universal transfer.** Groups around Corwin (Columbia), Seppäläinen (Wisconsin), Virág and Dauvergne (Toronto), and Basu (ICTS Bengaluru) study the directed landscape as a universal limit; a major theme is proving KPZ exponents for *perturbations* of solvable models.
- **General-distribution BKS refinements.** Damron, Hanson, Sosoe and collaborators (Georgia Tech / CUNY / Cornell) continue extending sublinearity, concentration and non-existence-of-bigeodesic results to minimal moment assumptions.
- **Higher dimensions.** Almost nothing beyond $\chi \le 1/2$; numerical work suggests $\chi(3) \approx 0.18$–$0.24$, and whether $\chi(d) \to 0$ at finite $d$ (an upper critical dimension) is open.

## 8. Future Work

- Prove $\operatorname{Var} T_n \le n^{1-\delta}$ for some $\delta>0$ and *some* i.i.d. law on $\mathbb{Z}^2$ — a first polynomial gain would be a landmark independent of the value $1/3$.
- Prove $\xi < 3/4$ strictly, and combine with $\chi = 2\xi-1$ to get a nontrivial two-sided constraint.
- Establish existence of the limit defining $\chi$ (currently only $\limsup$/$\liminf$ statements are available) — even existence is open.
- Construct a stationary version of undirected FPP (Busemann-measure cocycle) with tractable increments, mirroring Balázs–Cator–Seppäläinen.
- Prove non-existence of bigeodesics in $d=2$ for general continuous weights, a Licea–Newman-type statement, which would remove one obstruction in the coalescence route.
- Settle whether $\chi(d)$ is decreasing in $d$ and whether a mean-field/upper-critical-dimension phenomenon occurs.

## 9. Key References

- **[Foundational]** J. M. Hammersley and D. J. A. Welsh. *First-passage percolation, subadditive processes, stochastic networks, and generalized renewal theory.* In *Bernoulli–Bayes–Laplace Anniversary Volume*, Springer, 1965.
- **[Foundational]** H. Kesten. *Aspects of first passage percolation.* École d'Été de Probabilités de Saint-Flour XIV, Lecture Notes in Mathematics 1180, Springer, 1986.
- **[Foundational]** H. Kesten. *On the speed of convergence in first-passage percolation.* Annals of Applied Probability 3(2):296–338, 1993.
- **[Foundational]** J. Wehr and M. Aizenman. *Fluctuations of extensive functions of quenched random couplings.* Journal of Statistical Physics 60:287–306, 1990.
- **[Foundational]** C. M. Newman and M. S. T. Piza. *Divergence of shape fluctuations in two dimensions.* Annals of Probability 23(3):977–1005, 1995.
- **[Foundational]** C. Licea, C. M. Newman and M. S. T. Piza. *Superdiffusivity in first-passage percolation.* Probability Theory and Related Fields 106:559–591, 1996.
- **[SOTA]** I. Benjamini, G. Kalai and O. Schramm. *First passage percolation has sublinear distance variance.* Annals of Probability 31(4):1970–1978, 2003.
- **[SOTA]** M. Benaïm and R. Rossignol. *Exponential concentration for first passage percolation through modified Poincaré inequalities.* Annales de l'IHP Probabilités et Statistiques 44(3):544–573, 2008.
- **[SOTA]** M. Damron, J. Hanson and P. Sosoe. *Sublinear variance in first-passage percolation for general distributions.* Probability Theory and Related Fields 163:223–258, 2015.
- **[SOTA]** S. Chatterjee. *The universal relation between scaling exponents in first-passage percolation.* Annals of Mathematics 177(2):663–697, 2013.
- **[SOTA]** A. Auffinger and M. Damron. *A simplified proof of the relation between scaling exponents in first-passage percolation.* Annals of Probability 42(3):1197–1211, 2014.
- **[SOTA]** K. Johansson. *Shape fluctuations and random matrices.* Communications in Mathematical Physics 209:437–476, 2000.
- **[SOTA]** J. Baik, P. Deift and K. Johansson. *On the distribution of the length of the longest increasing subsequence of random permutations.* Journal of the AMS 12(4):1119–1178, 1999.
- **[SOTA]** M. Balázs, E. Cator and T. Seppäläinen. *Cube root fluctuations for the corner growth model associated to the exclusion process.* Electronic Journal of Probability 11:1094–1132, 2006.
- **[SOTA]** T. Seppäläinen. *Scaling for a one-dimensional directed polymer with boundary conditions.* Annals of Probability 40(1):19–73, 2012.
- **[Recent]** B. Dembin, D. Elboim and R. Peled. *Coalescence of geodesics and the BKS midpoint problem in planar first-passage percolation.* arXiv:2204.02332, 2022 *(frontier — verify final journal version)*.
- **[Survey]** A. Auffinger, M. Damron and J. Hanson. *50 Years of First-Passage Percolation.* University Lecture Series 68, American Mathematical Society, 2017.
- **[Survey]** S. Chatterjee. *Superconcentration and Related Topics.* Springer Monographs in Mathematics, 2014.
- **[Survey]** K. Alexander. *Approximation of subadditive functions and convergence rates in limiting-shape results.* Annals of Probability 25(1):30–55, 1997.

## 10. Worked Example / Concrete Special Case

**(a) Why the linear bound is easy, and why it stops there.** Take bounded weights $a \le \tau_e \le b$ on $\mathbb{Z}^2$ and $T_n = T(0,ne_1)$. Resampling one edge changes $T_n$ only if $e$ lies on a geodesic before or after the resample, and then by at most $b-a$:
$$|T_n - T_n^{(e)}| \le (b-a)\,\mathbf{1}\{e \in \gamma_n \cup \gamma_n^{(e)}\}.$$
Efron–Stein then gives
$$\operatorname{Var}(T_n) \le \tfrac12\sum_e \mathbb{E}(T_n - T_n^{(e)})^2 \le (b-a)^2\,\mathbb{E}|\gamma_n| \le \frac{(b-a)^2}{a}\,\mathbb{E}T_n \le C n,$$
using $a|\gamma_n| \le T(\gamma_n) = T_n$ and $\mathbb{E}T_n \le n\,\mathbb{E}\tau$. This is Kesten's $\chi \le 1/2$.

Now feed the same influences into Talagrand's $L^1$–$L^2$ bound. Each edge has $\|\partial_e T\|_1 \approx \mathbb{P}(e \in \gamma_n) \approx n^{-1}$ times a constant when the geodesic spreads over $\asymp n$ candidate edges, so the denominator $1+\log(\|\partial_e\|_2/\|\partial_e\|_1) \asymp \log n$, and
$$\operatorname{Var}(T_n) \ \lesssim\ \frac{\sum_e \|\partial_e T\|_2^2}{\log n} \ \asymp\ \frac{n}{\log n}.$$
The whole BKS gain is this single $\log$. To reach $n^{2/3}$ one would need influences of size $n^{-1}$ *and* a mechanism converting them into a factor $n^{-1/3}$ — hypercontractivity cannot do this.

**(b) An exactly solvable instance where the answer is known.** In the corner-growth model with i.i.d. $\mathrm{Exp}(1)$ site weights $w_{i,j}$ and up-right paths,
$$G(2,2) = w_{11} + \max(w_{12}, w_{21}) + w_{22}.$$
With $M = \max(w_{12},w_{21})$ we have $M \overset{d}{=} E_1/2 + E_2$ with $E_i$ i.i.d. $\mathrm{Exp}(1)$, so $\mathbb{E}M = 3/2$, $\operatorname{Var}M = 1/4 + 1 = 5/4$. Hence
$$\mathbb{E}G(2,2) = 1 + \tfrac32 + 1 = \tfrac72, \qquad \operatorname{Var}G(2,2) = 1 + \tfrac54 + 1 = \tfrac{13}{4}.$$
Asymptotically Johansson's theorem gives $\mathbb{E}G(n,n) = 4n - c\,n^{1/3} + o(n^{1/3})$ and
$$\frac{G(n,n) - 4n}{2^{4/3} n^{1/3}} \Longrightarrow \mathrm{TW}_{\mathrm{GUE}},$$
so $\operatorname{Var}G(n,n) \asymp n^{2/3}$, i.e. $\chi = 1/3$ exactly. Replace $\mathrm{Exp}(1)$ by, say, $\mathrm{Uniform}[1,2]$, or replace up-right paths by all lattice paths, and every step of this computation collapses: no memoryless property, no Burke stationarity, no determinantal kernel. That collapse is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*