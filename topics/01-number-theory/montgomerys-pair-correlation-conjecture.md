---
id: 01-number-theory/montgomerys-pair-correlation-conjecture
title: "Montgomery's Pair Correlation Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Montgomery's Pair Correlation Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/montgomerys-pair-correlation-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Montgomery's Pair Correlation Conjecture is a profound hypothesis concerning the distribution of the spacings between the non-trivial zeros of the Riemann zeta function $\zeta(s)$. 

Assume the Riemann Hypothesis, which states that all non-trivial zeros of $\zeta(s)$ lie on the critical line $\operatorname{Re}(s) = 1/2$. We denote these zeros as $1/2 + i\gamma_n$, where the real ordinates $\gamma_n$ are ordered such that $0 < \gamma_1 \le \gamma_2 \le \dots$. The number of zeros $N(T)$ with $0 < \gamma \le T$ follows the asymptotic law:
$$ N(T) = \frac{T}{2\pi} \log\left(\frac{T}{2\pi e}\right) + O(\log T) $$

This implies that the average spacing between consecutive zeros at height $T$ is $2\pi / \log T$. To study the local spacing statistics, we define the normalized ordinates $\widetilde{\gamma} = \frac{\gamma}{2\pi} \log\left(\frac{\gamma}{2\pi}\right)$, which have a mean spacing of $1$.

Montgomery's Pair Correlation Conjecture states that for any fixed interval $[\alpha, \beta]$ where $0 < \alpha < \beta$, the proportion of pairs of normalized zeros that fall within this distance converges to the integral of a specific kernel as $N \to \infty$:
$$ \lim_{N \to \infty} \frac{1}{N} \left| \left\{ (j, k) : 1 \le j \neq k \le N, \alpha \le \widetilde{\gamma}_j - \widetilde{\gamma}_k \le \beta \right\} \right| = \int_{\alpha}^{\beta} \left( 1 - \left(\frac{\sin(\pi u)}{\pi u}\right)^2 \right) du $$

This limiting distribution exactly matches the pair correlation of eigenvalues of random Hermitian matrices in the Gaussian Unitary Ensemble (GUE).

## 2. Mathematical Foundations

The conjecture is formalized using the concept of a Fourier transform of the distribution of zero spacings. Let $w(u) = 4 / (4 + u^2)$ be a rapidly decaying weight function, and define the Montgomery form factor $F(\alpha, T)$ as:
$$ F(\alpha, T) = \left( \frac{T}{2\pi} \log T \right)^{-1} \sum_{0 < \gamma, \gamma' \le T} T^{i \alpha (\gamma - \gamma')} w(\gamma - \gamma') $$
where the sum runs over all pairs of ordinates in $(0, T]$.

The conjecture asserts the exact limiting behavior of the form factor $F(\alpha, T)$ as $T \to \infty$:
$$ F(\alpha) = \lim_{T \to \infty} F(\alpha, T) = \begin{cases} |\alpha| & \text{if } |\alpha| \le 1 \\ 1 & \text{if } |\alpha| \ge 1 \end{cases} $$

The expected pair correlation function is recovered by taking the Fourier transform of $F(\alpha)$. Since $F(\alpha)$ can be written as $1 - (1-|\alpha|)\chi_{[-1,1]}(\alpha)$, its Fourier transform (excluding the Dirac delta at $0$ which corresponds to the diagonal terms $\gamma = \gamma'$) is precisely $1 - \left(\frac{\sin(\pi u)}{\pi u}\right)^2$. 

The foundational implication of the conjecture is the *GUE Hypothesis*: the zeros of the Riemann zeta function statistically behave like the eigenvalues of infinitely large random random matrices.

## 3. History & State of the Art (SOTA)

The conjecture was formulated by Hugh L. Montgomery in 1973 after he proved a partial result regarding $F(\alpha, T)$ for $|\alpha| < 1$. During a chance tea-time conversation at the Institute for Advanced Study, physicist Freeman Dyson recognized that Montgomery's kernel exactly matched the pair correlation of eigenvalues of matrices in the Gaussian Unitary Ensemble (GUE), a core concept in random matrix theory used to model energy levels in heavy atomic nuclei.

In 1987, Andrew Odlyzko provided massive empirical validation for the conjecture, computing the zeros of the zeta function near the $10^{20}$-th zero to unprecedented precision. The resulting histograms of normalized spacings matched the GUE prediction flawlessly.

In 1996, Zeev Rudnick and Peter Sarnak expanded the conjecture to all $n$-level correlations, proving that for suitably restricted test functions, the $n$-level correlations of the Riemann zeta function (and other principal L-functions) match those of the GUE. 

## 4. Partial Results / Verified Cases

Montgomery rigorously proved the conjecture for a restricted range. He proved that, assuming the Riemann Hypothesis, the form factor satisfies:
$$ F(\alpha, T) \to |\alpha| \quad \text{as} \quad T \to \infty $$
uniformly for any closed sub-interval of $0 \le |\alpha| < 1$. 

Furthermore, by utilizing the non-negativity of $F(\alpha, T)$, Montgomery proved that at least $2/3$ of the non-trivial zeros of $\zeta(s)$ are simple (meaning their multiplicity is exactly $1$). This was later improved by Conrey, Ghosh, and Gonek to show that at least $0.4077$ of the zeros are simple (without assuming RH).

The Rudnick-Sarnak theorem verifies the $n$-level correlations for a restricted class of test functions whose Fourier transforms are supported in $\sum_{i=1}^n |\alpha_i| < 2$, confirming the multi-dimensional analog of the $|\alpha| < 1$ condition.

Computationally, the Pair Correlation Conjecture is one of the most thoroughly tested mathematical hypotheses, holding true well past the $10^{30}$-th zero.

## 5. Principal Obstacles

The fundamental barrier preventing the resolution of the Pair Correlation Conjecture is an absolute limit on our knowledge of the distribution of primes in extremely short intervals.

Montgomery's analysis evaluates $\sum T^{i\alpha(\gamma - \gamma')}$ using the *explicit formula*, which connects the zeros of $\zeta(s)$ to the prime numbers. Under this transformation, $F(\alpha, T)$ can be expressed in terms of sums over primes $p, q \le T^{|\alpha|}$:
$$ F(\alpha, T) \approx \frac{1}{T \log T} \sum_{p, q \le T^{|\alpha|}} \frac{\Lambda(p) \Lambda(q)}{\sqrt{pq}} \int_0^T \left(\frac{p}{q}\right)^{it} dt $$
where $\Lambda(x)$ is the von Mangoldt function.

When $|\alpha| < 1$, the integration over $t$ heavily dampens the off-diagonal terms ($p \neq q$). The sum is strictly dominated by the diagonal terms ($p = q$), allowing the Prime Number Theorem to cleanly evaluate the sum, yielding $|\alpha|$.

However, when $|\alpha| \ge 1$, the upper limit $T^{|\alpha|}$ exceeds the integration length $T$. The highly oscillatory off-diagonal terms no longer cancel out. The primes $p$ and $q$ become so densely packed that $p \approx q$, creating constructive interference. Evaluating these off-diagonal contributions requires understanding the exact covariance of prime numbers at very small scales—specifically, the pair correlation of primes (twin primes and generalized Hardy-Littlewood prime tuples)—which is completely intractable with modern analytic number theory.

## 6. The Gap

The exact boundary of human knowledge is the transition across $|\alpha| = 1$.
- **Proven:** $F(\alpha) = |\alpha|$ for $|\alpha| \le 1$ (controlled by independent prime distribution).
- **Conjectured:** $F(\alpha) = 1$ for $|\alpha| \ge 1$ (requires proving strong correlations among primes).

Bridging this gap requires proving a strong form of the Hardy-Littlewood prime tuples conjecture for short intervals. Daniel Goldston and Hugh Montgomery formally proved that the Pair Correlation Conjecture is strictly equivalent to an asymptotic formula for the variance of the number of primes in short intervals of length $h < X$. Moving past $|\alpha| = 1$ is thus equivalent to breaking major barriers in sieve theory and prime gaps.

## 7. Current Research (as of June 2026)

Current active research focuses on sidestepping the barrier at $|\alpha| = 1$ using auxiliary methods:
- **The Ratios Conjecture:** Formulated by Conrey, Farmer, and Zirnbauer, this conjecture uses a heuristic recipe from random matrix theory to predict all lower-order terms in the correlation functions perfectly, bypassing the limitations of Fourier analysis. *(frontier — verify)*
- **Families of L-functions:** Work spearheaded by Katz and Sarnak studies the "Montgomery-Odlyzko law" not just in the vertical aspect (as $t \to \infty$ for $\zeta(s)$) but in horizontal families of L-functions (e.g., Dirichlet L-functions, elliptic curves) as the conductor goes to infinity. 
- **Multiple Dirichlet Series:** Groups at Stanford and Brown are investigating moments of L-functions and zero correlations using the algebraic structure of multiple Dirichlet series, which sometimes allows for analytic continuation beyond standard boundaries.
- **Bounding simple zeros:** Improving unconditional and conditional lower bounds on the proportion of simple zeros of $\zeta(s)$ by optimizing the test functions used against the known $F(\alpha)$ bounds.

## 8. Future Work

Leading number theorists have identified several pathways for future exploration:
1. **Extending the Support:** Unconditionally extending the range of the Rudnick-Sarnak theorem for $n$-level correlations slightly beyond $\sum |\alpha_i| < 2$ by utilizing recent breakthroughs in bounded prime gaps (e.g., the Maynard-Tao method).
2. **Moments of Zeta:** Fully integrating the Keating-Snaith random matrix theory conjectures into rigorous bounds for the moments of $\zeta(1/2 + it)$, which are deeply tied to the spacing of the zeros.
3. **Mollifier Optimization:** Finding new families of mollifiers that can artificially suppress the off-diagonal prime interference, pushing partial evaluations of $F(\alpha, T)$ for $|\alpha| > 1$.

## 9. Key References

- **[Foundational]** Montgomery, H. L. *The pair correlation of zeros of the zeta function.* Analytic Number Theory, Proc. Sympos. Pure Math., Vol. XXIV, 181–193. American Mathematical Society, 1973.
- **[Foundational]** Odlyzko, A. M. *On the distribution of spacings between zeros of the zeta function.* Mathematics of Computation, 48(177), 273-308. 1987.
- **[Foundational]** Rudnick, Z., & Sarnak, P. *Zeros of principal L-functions and random matrix theory.* Duke Mathematical Journal, 81(2), 269-322. 1996.
- **[SOTA / Recent]** Conrey, J. B., Farmer, D. W., & Zirnbauer, M. R. *Autocorrelation of ratios of L-functions.* Communications in Number Theory and Physics, 2(3), 593-636. 2008.
- **[Survey]** Katz, N. M., & Sarnak, P. *Zeroes of zeta functions and symmetry.* Bulletin of the American Mathematical Society, 36(1), 1-26. 1999.

## 10. Worked Example / Concrete Special Case

To understand the tangible consequences of the conjecture, we can calculate the **"zero repulsion"** phenomenon by examining the expected number of normalized zeros found within an exceptionally short distance of a given zero.

Suppose we normalize the zeros so the average spacing is $1$. If the zeros were randomly distributed according to a Poisson process (like random events in time, which do not repel), the probability density for a zero spacing $u$ would simply be $1$. 

The expected number of zeros within a distance of $\beta = 0.5$ from a given zero under the Poisson model is:
$$ E_{\text{Poisson}}(0.5) = \int_0^{0.5} 1 \, du = 0.5 $$

However, Montgomery's conjecture asserts that the zeros behave like GUE matrix eigenvalues. The expected number of zeros is dictated by the pair correlation kernel:
$$ E_{\text{GUE}}(0.5) = \int_0^{0.5} \left( 1 - \left(\frac{\sin(\pi u)}{\pi u}\right)^2 \right) du $$

We can estimate the integral of the subtrahend. Using integration by parts, the integral of $\frac{\sin^2(\pi u)}{(\pi u)^2}$ involves the Sine Integral function $\operatorname{Si}(x) = \int_0^x \frac{\sin t}{t} dt$:
$$ \int_0^{0.5} \frac{\sin^2(\pi u)}{(\pi u)^2} du = \frac{1}{\pi} \int_0^{\pi/2} \frac{\sin^2 v}{v^2} dv = \frac{1}{\pi} \left( -\frac{2}{\pi} + \operatorname{Si}(\pi) \right) $$

Given $\operatorname{Si}(\pi) \approx 1.8519$, we evaluate the penalty term:
$$ \frac{1}{\pi} ( -0.6366 + 1.8519 ) \approx \frac{1.2153}{\pi} \approx 0.3868 $$

Substituting this back into our expectation:
$$ E_{\text{GUE}}(0.5) = 0.5 - 0.3868 = 0.1132 $$

**Conclusion:** A purely random Poisson distribution predicts you will find $0.5$ zeros on average in a $0.5$-width window. The GUE prediction states you will only find $0.1132$ zeros. The zeros of the Riemann zeta function actively "repel" one another, making tight clusters extremely rare—a property identical to the quantum energy levels modeled by Random Matrix Theory.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*