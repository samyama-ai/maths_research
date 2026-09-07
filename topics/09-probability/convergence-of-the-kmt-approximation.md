---
id: 09-probability/convergence-of-the-kmt-approximation
title: "Convergence of the KMT Approximation"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Convergence of the KMT Approximation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/convergence-of-the-kmt-approximation` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Komlós–Major–Tusnády (KMT) strong approximation problem asks for the **optimal rate** at which a random walk can be coupled with a Brownian motion on a common probability space, and for the exact conditions under which that rate holds.

Let $X_1, X_2, \dots$ be i.i.d. with $\mathbb{E}X_1 = 0$, $\mathbb{E}X_1^2 = \sigma^2 < \infty$, and $S_n = \sum_{i \le n} X_i$. One seeks a probability space carrying both $(X_i)$ and a standard Brownian motion $(B(t))_{t\ge 0}$ such that the **discrepancy** $\Delta_n = \max_{k\le n} |S_k - \sigma B(k)|$ is as small as possible.

Three linked questions:

1. **(One-dimensional, exponential moments — settled.)** If $\mathbb{E}e^{t_0|X_1|} < \infty$ for some $t_0>0$, is the rate $\Delta_n = O(\log n)$ a.s., with an exponential tail bound, and is $\log n$ optimal? *Answered yes by KMT (1975–76); optimality is classical.*
2. **(Moment-optimal versions — settled.)** For $\mathbb{E}|X_1|^p < \infty$, $p>2$, is $|S_n - \sigma B(n)| = o(n^{1/p})$ a.s. the sharp rate? *Yes (Major 1976; Sakhanenko 1985; Zaitsev).*
3. **(Multidimensional and dependent versions — open.)** In $\mathbb{R}^d$, is the optimal bound $C(d)\log n$ with $C(d)$ growing polynomially in $d$, and what is the true rate for empirical processes indexed by classes richer than half-lines, or for weakly dependent sequences?

A complete resolution of the remaining open parts requires either a construction achieving the conjectured rate with explicit dimension/complexity dependence, or a matching lower-bound counterexample.

## 2. Mathematical Foundations

**KMT Theorem (1975).** If $(X_i)$ are i.i.d., centered, with $\mathbb{E}e^{t_0|X_1|}<\infty$, there exist constants $C,K,\lambda>0$ depending only on the law of $X_1$, and a construction with a Brownian motion $B$, such that for all $n$ and all $x>0$
$$\mathbb{P}\Big(\max_{1\le k\le n}|S_k - \sigma B(k)| > C\log n + x\Big) \le K e^{-\lambda x}.$$
Borel–Cantelli gives $\max_{k\le n}|S_k-\sigma B(k)| = O(\log n)$ a.s.

**Optimality.** For non-Gaussian $X_1$ the $\log n$ term cannot be improved: any coupling satisfies $\limsup_n |S_n - \sigma B(n)|/\log n > 0$ a.s. (Bártfai-type lower bounds; see Csörgő–Révész 1981, Ch. 2).

**Moment-graded rate.** If $\mathbb{E}|X_1|^p<\infty$, $p>2$, there is a coupling with
$$|S_n - \sigma B(n)| = o(n^{1/p}) \quad \text{a.s.},$$
and $n^{1/p}$ is unimprovable, since $\max_{k\le n}|X_k| \asymp n^{1/p}$.

**Empirical version (KMT II).** For $U_1,\dots,U_n$ i.i.d. uniform on $[0,1]$ with empirical process $\alpha_n(t)=\sqrt n\,(F_n(t)-t)$, there is a sequence of Brownian bridges $B_n$ with
$$\mathbb{P}\Big(\sup_{t\in[0,1]}|\alpha_n(t)-B_n(t)| > n^{-1/2}(C\log n + x)\Big)\le K e^{-\lambda x}.$$
Bretagnolle–Massart (1989) made $C,K,\lambda$ explicit ($C=12$, $K=2$, $\lambda=1/6$ suffice).

**The construction.** KMT is a *dyadic (Tusnády) quantile coupling*. Conditionally on $S_{2m}$, the midpoint $S_m$ has a lattice conditional law; the Gaussian analogue has conditional law $N(S_{2m}/2, m/2)$. The **quantile transform** $X=F^{-1}(\Phi_{m}(Y))$ satisfies the Tusnády inequality
$$|X - Y| \le \frac{c_1 + c_2 Y^2}{\sqrt m},$$
so each dyadic level contributes $O(1)$ with exponential tails; there are $\log_2 n$ levels, giving $O(\log n)$.

**Multidimensional (Zaitsev 1998).** For i.i.d. $\mathbb{R}^d$-vectors with $\mathbb{E}e^{t_0|X_1|}<\infty$ and identity covariance, there is a coupling with
$$\mathbb{P}\Big(\max_{k\le n}|S_k - B(k)| > C_1(d)\log n + x\Big)\le K e^{-x/C_2(d)},$$
but the growth of $C_1(d), C_2(d)$ in $d$ is not explicit and conjecturally polynomial.

## 3. History & State of the Art (SOTA)

- **1961–1968.** Skorokhod embedding and the Strassen invariance principle give $O(n^{1/4}\log^{1/2} n \,(\log\log n)^{1/4})$ — far from optimal.
- **1975–1976.** Komlós, Major, Tusnády, *An approximation of partial sums of independent RV's and the sample DF, I & II* (Z. Wahrscheinlichkeitstheorie): the $O(\log n)$ rate under exponential moments, plus the empirical-process version. This is the decisive breakthrough and the origin of "Hungarian construction".
- **1976.** Major: the $o(n^{1/p})$ rate under $p$-th moments.
- **1985.** Sakhanenko: sharp quantitative estimates in the invariance principle under Bernstein-type conditions, with best-possible constants in $d=1$.
- **1989.** Einmahl extends KMT to $\mathbb{R}^d$ with $O(\log^2 n)$; Bretagnolle–Massart give a nonasymptotic Hungarian construction with explicit constants; Massart extends KMT to multivariate empirical processes.
- **1994.** Rio proves local invariance principles refining the empirical KMT and improves logarithmic factors in the multivariate case.
- **1998.** Zaitsev attains the optimal $\log n$ rate in $\mathbb{R}^d$ (ESAIM P&S), with dimension-dependent constants.
- **2012.** Chatterjee gives a conceptually new proof of the one-dimensional strong embedding via Stein's method, replacing the dyadic quantile machinery.
- **2012–2014.** Merlevède–Rio, and Berkes–Liu–Wu, extend KMT to dependent (mixing, physical-dependence) sequences.

The one-dimensional i.i.d. problem is therefore **settled** — rate, tail bound, moment thresholds, and optimality all match. The open frontier is dimension/complexity dependence and dependence structure.

## 4. Partial Results / Verified Cases

| Setting | Best rate | Status |
|---|---|---|
| i.i.d., $d=1$, $\mathbb{E}e^{t_0|X|}<\infty$ | $O(\log n)$, exponential tail | Solved, optimal (KMT 1975) |
| i.i.d., $d=1$, $\mathbb{E}|X|^p<\infty$, $p>2$ | $o(n^{1/p})$ | Solved, optimal (Major 1976; Sakhanenko 1985) |
| i.i.d., $d=1$, $p=2$ only | $o(\sqrt{n\log\log n})$ (Strassen); no $o(\sqrt n)$ in general | Sharp |
| Uniform empirical process on $[0,1]$ | $n^{-1/2}\log n$, explicit constants $C=12,K=2,\lambda=1/6$ | Solved (Bretagnolle–Massart 1989) |
| Empirical process on $[0,1]^d$, orthants, $d\ge 2$ | $n^{-1/(2d)}$ up to log factors | Rate known; exact log power open (Massart 1989; Rio 1994) |
| i.i.d. vectors in $\mathbb{R}^d$, exponential moments | $C(d)\log n$ | Solved qualitatively (Zaitsev 1998); $d$-dependence open |
| Stationary sequences under $\beta$-mixing / physical dependence | $o(n^{1/p})$-type rates under moment + dependence conditions | Partial (Merlevède–Rio 2012; Berkes–Liu–Wu 2014) |
| Independent non-identically distributed, $d=1$ | Sakhanenko-type bounds with Lindeberg-style conditions | Solved |

Bernoulli$(\pm 1)$ walks, Poisson processes, and bounded increments are fully covered with explicit constants; these are the cases where Tusnády's inequality has been verified by direct computation and, for small $n$, numerically.

## 5. Principal Obstacles

- **The quantile coupling is one-dimensional.** Tusnády's inequality $|X-Y|\le (c_1+c_2Y^2)/\sqrt m$ relies on the monotone quantile transform $F^{-1}\circ\Phi$, which has no canonical analogue in $\mathbb{R}^d$: the optimal-transport (Brenier) map replacing it is not explicit and lacks the pointwise second-order control needed at each dyadic level.
- **Constants compound multiplicatively across scales.** With $\log_2 n$ levels, a per-level error of $1+\varepsilon(d)$ yields $C(d)$ growing like a product; controlling $C(d)$ requires uniform-in-$d$ conditional CLT bounds with Edgeworth-quality error terms, which are only available with dimension-dependent losses.
- **Complexity of index classes.** For empirical processes indexed by a class $\mathcal F$, the Hungarian construction needs a *nested* partition of the index set that behaves like dyadic intervals. Orthants in $\mathbb{R}^d$ admit one at cost $n^{-1/(2d)}$; general VC or Donsker classes do not, and no KMT-rate coupling is known for them.
- **Dependence destroys conditional independence.** The dyadic scheme conditions on block sums and requires the two halves to be conditionally independent. Mixing coefficients only give approximate conditional independence, and the approximation error accumulates over the $\log n$ levels.
- **Stein's-method route loses sharpness.** Chatterjee's approach avoids quantile coupling but currently reproduces, rather than beats, the classical constants, and has not been pushed to $d\ge 2$ with polynomial $C(d)$.

## 6. The Gap

Proven: for $d=1$ i.i.d., a coupling with tail $\mathbb{P}(\Delta_n > C\log n + x)\le Ke^{-\lambda x}$, matched by a lower bound of the same order. For $d\ge 2$, existence of *some* finite $C_1(d), C_2(d)$.

Not proven: any bound of the form $C_1(d)\le \mathrm{poly}(d)$; any KMT-rate coupling for a general Donsker class $\mathcal F$ with rate expressed in its metric entropy; the exact power of $\log n$ in the $d$-dimensional empirical bound $n^{-1/(2d)}(\log n)^{\gamma}$, where the known upper bound $\gamma$ exceeds the conjectured optimum $\gamma=1$.

The precise step to cross: replace the monotone rearrangement in Tusnády's lemma with a multivariate transport map admitting a bound $|T(y)-y| \le (c_1 + c_2|y|^2)\,\mathrm{poly}(d)/\sqrt m$ that is stable under conditioning on block sums.

## 7. Current Research (as of June 2026)

- **Optimal-transport reformulations.** Smoothed-transport and Bobkov–Ledoux-style Kantorovich estimates for empirical measures are being used to attack the multivariate quantile step directly. *(frontier — verify)*
- **Stein's method and exchangeable pairs.** Extensions of Chatterjee's 2012 embedding to vector-valued and locally dependent settings, aiming for explicit $d$-dependence. *(frontier — verify)*
- **Dependent sequences.** Continuation of the Merlevède–Rio and Berkes–Liu–Wu programs (Université Gustave Eiffel, Univ. Chicago) toward KMT rates for dynamical systems, Markov chains with spectral gaps, and long-memory linear processes.
- **Applications driving sharpness.** Random walks in random environment, KPZ-type models, and nonparametric confidence bands need couplings with explicit constants, which sustains interest in Bretagnolle–Massart–style nonasymptotic bounds.
- **Steklov Institute (St. Petersburg)** remains the centre for Zaitsev's line on multidimensional strong-approximation constants.

## 8. Future Work

- Prove or refute $C_1(d) = O(d^{a})$ for some finite $a$ in Zaitsev's theorem; even $C_1(d) = e^{o(d)}$ would be progress.
- Establish a KMT-rate coupling indexed by a VC class with rate depending only on the VC dimension.
- Determine the optimal $\gamma$ in $n^{-1/(2d)}(\log n)^{\gamma}$ for orthant-indexed empirical processes.
- Develop a self-contained transport proof of KMT that yields the classical constants, providing a route that generalizes past $d=1$.
- Extend to non-stationary and heavy-tailed regimes ($p\in(1,2)$) with $\alpha$-stable limit processes replacing $B$.

## 9. Key References

- **[Foundational]** J. Komlós, P. Major, G. Tusnády. *An approximation of partial sums of independent RV's, and the sample DF. I.* Z. Wahrscheinlichkeitstheorie verw. Gebiete **32** (1975), 111–131.
- **[Foundational]** J. Komlós, P. Major, G. Tusnády. *An approximation of partial sums of independent RV's, and the sample DF. II.* Z. Wahrscheinlichkeitstheorie verw. Gebiete **34** (1976), 33–58.
- **[Foundational]** P. Major. *The approximation of partial sums of independent RV's.* Z. Wahrscheinlichkeitstheorie verw. Gebiete **35** (1976), 213–220.
- **[Survey]** M. Csörgő, P. Révész. *Strong Approximations in Probability and Statistics.* Academic Press, 1981.
- **[Survey]** M. Csörgő, L. Horváth. *Weighted Approximations in Probability and Statistics.* Wiley, 1993.
- **[SOTA]** J. Bretagnolle, P. Massart. *Hungarian constructions from the nonasymptotic viewpoint.* Annals of Probability **17** (1989), 239–256.
- **[SOTA]** P. Massart. *Strong approximation for multivariate empirical and related processes, via KMT constructions.* Annals of Probability **17** (1989), 266–291.
- **[SOTA]** U. Einmahl. *Extensions of results of Komlós, Major, and Tusnády to the multivariate case.* Journal of Multivariate Analysis **28** (1989), 20–68.
- **[SOTA]** A. Yu. Zaitsev. *Multidimensional version of the results of Komlós, Major and Tusnády for vectors with finite exponential moments.* ESAIM: Probability and Statistics **2** (1998), 41–108.
- **[SOTA]** E. Rio. *Local invariance principles and their application to density estimation.* Probability Theory and Related Fields **98** (1994), 21–45.
- **[Recent]** S. Chatterjee. *A new approach to strong embeddings.* Probability Theory and Related Fields **152** (2012), 231–264.
- **[Recent]** F. Merlevède, E. Rio. *Strong approximation of partial sums under dependence conditions with application to dynamical systems.* Stochastic Processes and their Applications **122** (2012), 386–417.
- **[Recent]** I. Berkes, W. Liu, W. B. Wu. *Komlós–Major–Tusnády approximation under dependence.* Annals of Probability **42** (2014), 794–817.
- **[Recent]** S. Bobkov, M. Ledoux. *One-dimensional empirical measures, order statistics, and Kantorovich transport distances.* Memoirs of the AMS **261** (2019), no. 1259.

## 10. Worked Example / Concrete Special Case

**Simple random walk, one dyadic level.** Take $X_i = \pm1$ with probability $1/2$, $n=8$, and condition on $S_8 = 4$ (six $+1$'s, two $-1$'s). The midpoint $S_4 = 2k-4$, where $k$ is the number of $+1$'s among the first four steps, is hypergeometric:
$$\mathbb{P}(k)=\frac{\binom{4}{k}\binom{4}{6-k}}{\binom{8}{6}},\qquad \binom{8}{6}=28,$$
giving $\mathbb{P}(S_4=0)=\tfrac{6}{28}$, $\mathbb{P}(S_4=2)=\tfrac{16}{28}$, $\mathbb{P}(S_4=4)=\tfrac{6}{28}$. Mean $2$, variance $\tfrac{48}{28}=\tfrac{12}{7}\approx1.714$.

The Brownian counterpart, conditioned on $B(8)=4$, has midpoint $B(4)\sim N(2,\,2)$ (variance $8/4=2$).

**Quantile coupling.** Set $S_4 = F^{-1}(\Phi_{2,2}(B(4)))$. The discrete cut points are at cumulative masses $6/28 = 0.2143$ and $22/28 = 0.7857$; the corresponding Gaussian quantiles are $z = \mp 0.7916$, i.e.
$$y_1 = 2 - \sqrt2\,(0.7916) = 0.881,\qquad y_2 = 2 + \sqrt2\,(0.7916) = 3.119 .$$
So the coupling is: $B(4)<0.881 \Rightarrow S_4=0$; $0.881\le B(4)<3.119 \Rightarrow S_4=2$; $B(4)\ge 3.119 \Rightarrow S_4=4$.

**Error accounting.** For $B(4)=2$ (the mode) the error is $0$; for $B(4)=0.9$ it is $|2-0.9|=1.1$; for $B(4)=4.5$ it is $0.5$. The error is bounded by half the lattice spacing plus a curvature term, consistent with Tusnády's inequality
$$|S_4 - B(4)| \le \frac{c_1 + c_2\,\tilde y^{\,2}}{\sqrt m},\qquad \tilde y = \frac{B(4)-2}{\sqrt2},\ m=8,$$
i.e. $O(1)$ with a Gaussian-square tail.

**Why $\log n$.** Repeating this at every dyadic scale $n, n/2, n/4, \dots, 1$ produces $\log_2 n$ independent-ish levels, each contributing an $O(1)$ error with an exponential tail. Summing gives $\max_{k\le n}|S_k - B(k)| = O(\log n)$; for $n=8$ that is three levels. Conversely, since the walk is lattice-valued while $B$ is continuous, the discrepancy cannot be $o(\log n)$: a matching lower bound follows from the fact that $S_n - B(n)$ must absorb the total lattice rounding across all scales.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*