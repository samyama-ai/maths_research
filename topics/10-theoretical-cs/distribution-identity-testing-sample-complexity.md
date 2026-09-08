---
id: 10-theoretical-cs/distribution-identity-testing-sample-complexity
title: "Sample Complexity of Distribution Testing under Structure"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sample Complexity of Distribution Testing under Structure

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/distribution-identity-testing-sample-complexity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Given sample access to an unknown distribution $p$ over a domain $\Omega$, a known reference $q$, and a proximity parameter $\varepsilon \in (0,1)$, an **identity tester** must distinguish $p = q$ from $d_{TV}(p,q) > \varepsilon$ with probability $\ge 2/3$. For $\Omega = [n]$ with no assumptions, the sample complexity is settled: $\Theta(\sqrt{n}/\varepsilon^2)$.

The open problem is the **structured** version. Fix a class $\mathcal{C}$ of distributions (monotone, log-concave, $t$-histogram, product, Bayes net of bounded degree, Ising model, mixture of $k$ Gaussians). Under the promise $p, q \in \mathcal{C}$, define

$$m(\mathcal{C},\varepsilon) \;=\; \min\{\, m : \exists\ \text{an } m\text{-sample tester correct on all } p,q \in \mathcal{C} \,\}.$$

**The question.** Is there a single structural complexity measure $\kappa(\mathcal{C})$ — an effective dimension, a metric-entropy or VC-type parameter, or an $\mathcal{A}_k$-approximation parameter — such that

$$m(\mathcal{C},\varepsilon) \;=\; \tilde\Theta\!\left(\frac{\sqrt{\kappa(\mathcal{C})}}{\varepsilon^{2}}\right)$$

for all "reasonable" $\mathcal{C}$? A complete resolution means either a general theorem with matching upper and lower bounds in terms of $\kappa$, or an explicit class exhibiting a provable separation between $\sqrt{\kappa}$ and the true complexity. Two allied sub-problems are open in the same sense: (i) the **tolerant** version, distinguishing $d_{TV}(p,q)\le\varepsilon_1$ from $\ge\varepsilon_2$, where the unstructured answer jumps to $\Theta(n/\log n)$; (ii) **two-sample (closeness) testing** under structure, where both $p$ and $q$ are unknown.

## 2. Mathematical Foundations

Let $p,q$ be probability measures on $[n]$. Total variation distance:

$$d_{TV}(p,q) \;=\; \tfrac12 \sum_{i=1}^{n} |p_i - q_i| \;=\; \max_{S \subseteq [n]} \big(p(S) - q(S)\big).$$

**$\mathcal{A}_k$ distance.** For $k \ge 1$, restrict the maximizing set to unions of at most $k$ intervals of $[n]$:

$$\|p-q\|_{\mathcal{A}_k} \;=\; \max_{\substack{I_1,\dots,I_k \\ \text{disjoint intervals}}} \left| \sum_{j=1}^{k} \big(p(I_j) - q(I_j)\big) \right|.$$

Always $\|p-q\|_{\mathcal{A}_k} \le 2\,d_{TV}(p,q)$, with equality at $k=n$. The key structural fact: if $p,q$ are each $\varepsilon$-close in $d_{TV}$ to some $t$-piecewise constant distribution, then $d_{TV}(p,q) \le \|p-q\|_{\mathcal{A}_{2t}} + 4\varepsilon$. Estimating $\|\cdot\|_{\mathcal{A}_k}$ costs samples scaling with $k$, not $n$ — the source of all structured speedups.

**Collision / $\ell_2$ machinery.** With $m$ i.i.d. samples, let $C$ be the number of colliding pairs. Then

$$\mathbb{E}[C] \;=\; \binom{m}{2}\,\|p\|_2^2, \qquad \|p\|_2^2 = \sum_i p_i^2 .$$

For uniform $u$ on $[n]$, $\|u\|_2^2 = 1/n$; and $d_{TV}(p,u) > \varepsilon \Rightarrow \|p\|_2^2 > \frac{1}{n}(1+4\varepsilon^2)$ by Cauchy–Schwarz. Separating these requires $m = \Theta(\sqrt{n}/\varepsilon^2)$ (Paninski 2008; Goldreich–Ron 2011 for the upper bound).

**Instance-optimal identity.** Valiant–Valiant (2017) show that for known $q$, the complexity is

$$\Theta\!\left(\frac{\big\|q_{-\varepsilon}^{-\max}\big\|_{2/3}}{\varepsilon^{2}}\right), \qquad \|q\|_{2/3} = \Big(\sum_i q_i^{2/3}\Big)^{3/2},$$

where $q^{-\max}_{-\varepsilon}$ removes the heaviest element and the smallest elements of total mass $\varepsilon$. This is the only known *complete* characterization in the field, and it is per-instance rather than per-class.

**Structured classes.** $\mathcal{M}_n$ = monotone non-increasing on $[n]$; $\mathcal{L}_n$ = log-concave; $\mathcal{H}_{t,n}$ = $t$-histograms; $\mathcal{B}_{d,n}$ = Bayes nets on $\{0,1\}^n$ with in-degree $\le d$; Ising models $p(x)\propto\exp(\sum_{i<j}\theta_{ij}x_ix_j + \sum_i h_ix_i)$.

## 3. History & State of the Art (SOTA)

- **1996–2000.** Goldreich–Ron introduce collision-based uniformity testing in the context of expansion testing; Batu, Fortnow, Rubinfeld, Smith, White (FOCS 2000) formalize closeness testing of discrete distributions, opening the field.
- **2008.** Paninski proves the tight $\Theta(\sqrt{n}/\varepsilon^2)$ uniformity lower bound via a Poissonized coincidence argument.
- **2011–2014.** Valiant–Valiant establish the $n/\log n$ barrier for tolerant testing, entropy and support-size estimation; Chan–Diakonikolas–Valiant–Valiant (SODA 2014) settle closeness at $\Theta\!\big(\max(n^{2/3}/\varepsilon^{4/3},\,\sqrt{n}/\varepsilon^2)\big)$.
- **2015.** Diakonikolas–Kane–Nikishkin (SODA 2015) initiate *structured* identity testing via the $\mathcal{A}_k$ distance, giving $\mathrm{poly}(\log n)$ testers for monotone and log-concave families. Acharya–Daskalakis–Kamath (NIPS 2015) give an optimal $\chi^2$-based identity tester matching the Valiant–Valiant bound.
- **2016.** Diakonikolas–Kane (FOCS 2016) present a unified reduction-based framework ("flattening" plus $\chi^2$ statistics) recovering nearly all known optimal bounds and settling monotonicity and independence testing.
- **2017–2019.** Canonne–Diakonikolas–Kane–Stewart (COLT 2017) settle identity testing for bounded-degree Bayes nets with known structure at $\tilde\Theta(2^{d/2}\sqrt{n}/\varepsilon^2)$-type bounds; Daskalakis–Dikkala–Kamath handle Ising models; Diakonikolas–Kane–Peebles treat multidimensional histograms.
- **2018–2022.** Extensions to conditional-independence testing (Canonne–Diakonikolas–Kane–Stewart, STOC 2018), to constrained models (privacy, communication, memory), and to conditional-sampling oracles. Canonne's monograph (2022) is the standard reference.

The SOTA is a large but unorganized zoo: dozens of classes, each with a bespoke tester and a bespoke lower bound.

## 4. Partial Results / Verified Cases

| Class / setting | Sample complexity | Source |
|---|---|---|
| Uniformity on $[n]$ | $\Theta(\sqrt{n}/\varepsilon^2)$ | Paninski 2008; Goldreich–Ron 2011 |
| Identity to arbitrary known $q$ | $\Theta(\|q^{-\max}_{-\varepsilon}\|_{2/3}/\varepsilon^2)$ | Valiant–Valiant 2017; ADK 2015 |
| Closeness (both unknown) | $\Theta(\max(n^{2/3}/\varepsilon^{4/3},\sqrt n/\varepsilon^2))$ | CDVV 2014 |
| $t$-histograms on $[n]$ | $\tilde\Theta(\sqrt{t}/\varepsilon^{O(1)})$, independent of $n$ | DKN 2015 |
| Monotone / log-concave / MHR on $[n]$ | $\mathrm{poly}(\log n)/\varepsilon^{O(1)}$ (near-optimal in $n$) | DKN 2015; DK 2016 |
| Independence on $[n]\times[m]$, $m\le n$ | $\tilde\Theta(n^{2/3}m^{1/3}/\varepsilon^{4/3} + \sqrt{nm}/\varepsilon^2)$ | DK 2016 |
| Degree-$d$ Bayes nets, known structure | $\tilde\Theta(2^{d/2}\sqrt{n}/\varepsilon^2)$ | CDKS 2017 |
| Ferromagnetic / high-temperature Ising | $\tilde O(n/\varepsilon^2)$-type, vs. $2^{\Theta(n)}$ generic | Daskalakis–Dikkala–Kamath 2019 |
| Tolerant identity, unstructured | $\Theta(n/\log n)$ | Valiant–Valiant 2011/2017 |

So the conjectured $\sqrt{\kappa}/\varepsilon^2$ law is *verified* whenever $\kappa$ can be read off as an $\mathcal{A}_k$-parameter ($k$ pieces), a product dimension, or $2^d n$ for Bayes nets. It is **not** verified for: unknown-structure Bayes nets, general graphical models at low temperature, mixtures of $k$ Gaussians in $\mathbb{R}^d$, and every tolerant variant.

## 5. Principal Obstacles

- **No canonical complexity measure.** VC dimension and metric entropy govern *learning*, not testing. Testing $\mathcal{C}$ can be strictly easier than learning it ($\sqrt{\kappa}$ vs. $\kappa$), but the exponent-$1/2$ saving is proved case by case; no functional on $\mathcal{C}$ is known that reproduces all rows of the table above.
- **$\chi^2$ statistics need a flat reference.** The optimal testers control $\mathrm{Var}$ of $\sum_i (X_i - m q_i)^2/(mq_i)$, which blows up on light elements. "Flattening" (splitting heavy bins) fixes this on $[n]$ but has no analogue when the structure is combinatorial (a DAG, a coupling graph) rather than geometric.
- **$\mathcal{A}_k$ reductions are one-dimensional.** Interval-based approximation is intrinsically ordered; in $[n]^d$ the number of "pieces" needed grows like $k^d$, so the reduction degrades exponentially in dimension.
- **Lower bounds are Poissonized-moment-matching arguments.** They construct two ensembles whose first $\ell$ moments agree. Imposing a structural promise (monotonicity, log-concavity, a Markov property) destroys the freedom to permute mass, and no general technique exists for building moment-matching ensembles *inside* a constrained class.
- **Tolerant testing is estimation in disguise.** Distinguishing $\varepsilon_1$ from $\varepsilon_2$ requires estimating $d_{TV}$, and the polynomial-approximation lower bounds (Chebyshev-type, Valiant–Valiant; Jiao et al.; Wu–Yang) show the $n/\log n$ rate is intrinsic to $\ell_1$-functional estimation, not an artifact.

## 6. The Gap

Proven: for each *individual* structured class studied, a tester and a matching (often up to $\log$ factors and $\varepsilon$-exponents) lower bound. Missing: the quantifier swap — a theorem quantified over all classes. Concretely, the boundary is

1. **A structural functional.** Define $\kappa(\mathcal{C})$ intrinsically (not "the number of pieces in the best $\mathcal{A}_k$ approximation", which already presumes an ordered domain) and prove $m(\mathcal{C},\varepsilon)=\tilde\Theta(\sqrt{\kappa}/\varepsilon^2)$.
2. **$\varepsilon$-dependence.** Even where the $n$-dependence is tight, structured testers pay $\varepsilon^{-2.5}$ or worse; whether $\varepsilon^{-2}$ is always achievable is open for histograms and log-concave families.
3. **Unknown structure.** For Bayes nets, the gap between known-structure $\tilde\Theta(2^{d/2}\sqrt n/\varepsilon^2)$ and the unknown-structure case (where superpolynomial lower bounds are known for $d\ge 2$ in some formulations) is not understood.

## 7. Current Research (as of June 2026)

- **Unified frameworks.** Groups around Diakonikolas (UW–Madison), Kane (UCSD), Canonne (Sydney) continue to push reduction-based meta-theorems that convert a *learning* algorithm in $\mathcal{A}_k$ into a tester; the aim is a black-box "learner $\Rightarrow$ tester with square-root savings" theorem. *(frontier — verify)*
- **Testing under constraints.** Sample complexity of identity testing under local/central differential privacy, communication limits, and $O(\log n)$-bit memory (Acharya, Canonne, Kamath, Tyagi, Ullman and co-authors) — here structure interacts with the constraint, and tight bounds are open for most structured classes.
- **Graphical models beyond Ising.** Testing for higher-order Markov random fields and continuous graphical models; the high-temperature/low-temperature phase boundary appears to control testability. *(frontier — verify)*
- **Tolerant testing with structure.** Whether the $n/\log n$ barrier collapses to $\mathrm{poly}(\log n)$ for monotone or log-concave families — partial positive results exist for histograms. *(frontier — verify)*
- **Robust/contaminated testing.** Testing when an $\eta$-fraction of samples is adversarial, merging the distribution-testing and robust-statistics literatures.

## 8. Future Work

- Identify a *testing dimension* analogous to VC dimension: a combinatorial parameter with a Yao-principle lower bound and a matching generic tester.
- Develop moment-matching lower-bound constructions constrained to lie inside a structured class (e.g., monotone ensembles with matched Chebyshev moments).
- Settle the exact $\varepsilon$-dependence for $\mathcal{A}_k$-based testers; conjecturally $\Theta(\sqrt{k}/\varepsilon^2)$.
- Extend the $\mathcal{A}_k$ machinery to unordered/combinatorial domains, perhaps via spectral or coupling-based surrogates.
- Determine whether conditional-sampling oracles collapse structured testing to $O(\mathrm{poly}(1/\varepsilon))$ for all natural classes, as they do for uniformity.

## 9. Key References

- **[Foundational]** T. Batu, L. Fortnow, R. Rubinfeld, W. D. Smith, P. White. *Testing that distributions are close.* FOCS 2000 (journal version: JACM 2013).
- **[Foundational]** L. Paninski. *A coincidence-based test for uniformity given very sparsely sampled discrete data.* IEEE Transactions on Information Theory, 54(10), 2008.
- **[Foundational]** O. Goldreich, D. Ron. *On testing expansion in bounded-degree graphs.* In *Studies in Complexity and Cryptography*, Springer LNCS 6650, 2011.
- **[SOTA]** G. Valiant, P. Valiant. *An automatic inequality prover and instance optimal identity testing.* SIAM Journal on Computing, 46(1), 2017.
- **[SOTA]** S. Chan, I. Diakonikolas, G. Valiant, P. Valiant. *Optimal algorithms for testing closeness of discrete distributions.* SODA 2014.
- **[SOTA]** I. Diakonikolas, D. M. Kane, V. Nikishkin. *Testing identity of structured distributions.* SODA 2015.
- **[SOTA]** I. Diakonikolas, D. M. Kane. *A new approach for testing properties of discrete distributions.* FOCS 2016.
- **[SOTA]** J. Acharya, C. Daskalakis, G. Kamath. *Optimal testing for properties of distributions.* NIPS 2015.
- **[SOTA]** C. L. Canonne, I. Diakonikolas, D. M. Kane, A. Stewart. *Testing Bayesian networks.* COLT 2017 (journal version: IEEE Trans. Inf. Theory, 2020).
- **[SOTA]** C. Daskalakis, N. Dikkala, G. Kamath. *Testing Ising models.* IEEE Transactions on Information Theory, 65(11), 2019.
- **[Survey]** C. L. Canonne. *A Survey on Distribution Testing: Your Data is Big. But is it Blue?* Theory of Computing Graduate Surveys, No. 9, 2020.
- **[Survey]** C. L. Canonne. *Topics and Techniques in Distribution Testing: A Biased but Representative Sample.* Foundations and Trends in Communications and Information Theory, 2022.
- **[Book]** O. Goldreich. *Introduction to Property Testing.* Cambridge University Press, 2017 (Chapter 11).

## 10. Worked Example / Concrete Special Case

**Setup.** $n = 10^6$, $\varepsilon = 0.1$. Reference $q$ is uniform on $[n]$.

*Unstructured cost.* Draw $m$ samples, count collisions $C$. Under $p=q$: $\mathbb{E}[C]=\binom{m}{2}/n$. Under $d_{TV}(p,q)>\varepsilon$: since $\|p\|_2^2 \ge \frac1n + \frac{4\varepsilon^2}{n}$ (Cauchy–Schwarz applied to $\sum_i (p_i - 1/n)^2 \ge \frac{1}{n}(2\varepsilon)^2$... i.e. $\|p-u\|_2^2 \ge \|p-u\|_1^2/n = 4\varepsilon^2/n$), the means separate by $\binom{m}{2}\cdot 4\varepsilon^2/n$. The standard deviation of $C$ in the null is $\Theta(m/\sqrt{n})$, so detection needs

$$\frac{m^2\varepsilon^2}{n} \;\gtrsim\; \frac{m}{\sqrt n} \quad\Longrightarrow\quad m \;\gtrsim\; \frac{\sqrt n}{\varepsilon^2} \;=\; \frac{10^3}{0.01} \;=\; 10^5 .$$

*Structured cost.* Now impose the promise $p \in \mathcal{H}_{2,n}$: $p$ is constant on $[1,n/2]$ and on $[n/2+1,n]$, with masses $(a, 1-a)$; $q$ has $a = 1/2$. Then

$$d_{TV}(p,q) = \tfrac12\big(|a - \tfrac12| + |(1-a)-\tfrac12|\big) = |a - \tfrac12| = \|p-q\|_{\mathcal{A}_1}.$$

The tester ignores $n$ entirely: let $\hat a = \frac{1}{m}\\#\{\text{samples in } [1,n/2]\}$ and reject if $|\hat a - 1/2| > \varepsilon/2$. By Hoeffding, $\Pr[|\hat a - a| > \varepsilon/2] \le 2e^{-m\varepsilon^2/2}$, so

$$m \;=\; \left\lceil \frac{2\ln 6}{\varepsilon^{2}} \right\rceil \;=\; \left\lceil \frac{3.58}{0.01} \right\rceil \;=\; 358$$

samples suffice — a $280{\times}$ saving, with the $\sqrt{n}=10^3$ factor replaced by $\sqrt{k}=\sqrt{2}$ (absorbed into constants).

**What the example does not settle.** Generalize to $p \in \mathcal{H}_{t,n}$ with *unknown* breakpoints: one must estimate $\|p-q\|_{\mathcal{A}_{2t}}$ by maximizing over $\binom{n}{2t}$ interval systems. DKN 2015 achieve $\tilde O(\sqrt{t})$ samples with a worse $\varepsilon$-exponent than $2$. Whether $\Theta(\sqrt t/\varepsilon^2)$ is achievable — and what plays the role of $t$ when $[n]$ is replaced by a DAG or a lattice $[n]^d$ — is exactly the open problem of Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*