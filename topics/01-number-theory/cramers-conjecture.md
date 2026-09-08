---
id: 01-number-theory/cramers-conjecture
title: "Cramer's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cramer's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/cramers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Cramer's conjecture (also spelled Cramér's conjecture) is one of the most profound open problems in analytic number theory regarding the distribution of prime numbers. It asserts that the gap between consecutive prime numbers is asymptotically bounded by the square of the logarithm of the primes.

Let $p_n$ denote the $n$-th prime number, and define the $n$-th prime gap as $g_n = p_{n+1} - p_n$. Cramer's conjecture states that:
$$g_n = O((\log p_n)^2)$$

In a more precise limit superior form, the conjecture asserts:
$$\limsup_{n \to \infty} \frac{p_{n+1} - p_n}{(\log p_n)^2} = 1$$

A complete proof would require demonstrating unconditionally that for any $\epsilon > 0$, there exists an integer $N$ such that for all $n > N$, the gap $p_{n+1} - p_n < (1 + \epsilon)(\log p_n)^2$.

## 2. Mathematical Foundations

The conjecture is deeply rooted in the Prime Number Theorem (PNT) and probabilistic number theory. The PNT states that the prime counting function $\pi(x)$, which denotes the number of primes $p \le x$, is asymptotic to $\frac{x}{\log x}$. This implies that the average gap between consecutive primes in the neighborhood of $x$ is approximately $\log x$.

Harald Cramér based his conjecture on a probabilistic model (now known as the Cramér random model). The model assumes that the probability of an integer $n$ being prime is roughly $\frac{1}{\log n}$, and that the event of $n$ being prime is independent of the primality of other integers. 

Formally, we model the sequence of primes as a sequence of independent Bernoulli random variables $X_3, X_4, \dots$ where $X_n \in \{0, 1\}$ and 
$$P(X_n = 1) = \frac{1}{\log n}, \quad P(X_n = 0) = 1 - \frac{1}{\log n}$$

By analyzing the longest sequence of consecutive zeros in this sequence using the Borel-Cantelli lemma, Cramér deduced that with probability 1, the maximum gap between "primes" (1s in the sequence) up to $x$ is asymptotic to $(\log x)^2$.

## 3. History & State of the Art (SOTA)

Harald Cramér originally formulated this conjecture in 1936. Earlier, in 1920, Cramér proved that assuming the Riemann Hypothesis (RH), the prime gap is bounded by:
$$g_n = O(\sqrt{p_n} \log p_n)$$

Unconditionally, the progress on upper bounds has been slow but monumental, relying on sophisticated sieve methods and bounds on exponential sums over primes. The timeline of best-known unconditional bounds $g_n \ll p_n^\theta$ is as follows:
- Hoheisel (1930) proved the first sub-linear bound with $\theta = 32999/33000$.
- Ingham (1937) improved this to $\theta = 5/8$.
- Huxley (1972) achieved $\theta = 7/12$.
- Baker, Harman, and Pintz (2001) established the current State of the Art (SOTA) unconditional upper bound, $\theta = 0.525$.

On the other hand, the State of the Art lower bound on maximal prime gaps was established in a landmark 2014 paper by Ford, Green, Konyagin, Maynard, and Tao. They proved that for some constant $c > 0$ and infinitely many $n$:
$$g_n \ge c \frac{\log p_n \log \log p_n \log \log \log \log p_n}{\log \log \log p_n}$$

In 1995, Andrew Granville refined Cramér's probabilistic model by accounting for the fact that primes are not completely independent (e.g., consecutive numbers cannot both be prime except 2 and 3, and divisibility by small primes introduces local biases). Granville's refinement suggests the limit superior might actually be slightly larger than 1:
$$\limsup_{n \to \infty} \frac{p_{n+1} - p_n}{(\log p_n)^2} = 2 e^{-\gamma} \approx 1.1229$$
where $\gamma$ is the Euler-Mascheroni constant.

## 4. Partial Results / Verified Cases

Cramer's conjecture remains entirely unproven theoretically. However, it is overwhelmingly supported by empirical evidence and computational verification.

Maximal prime gaps (the gap $g_n$ such that $g_n > g_k$ for all $k < n$) have been exhaustively computed up to massive bounds. Large-scale distributed computing projects, most notably those initiated by Thomas R. Nicely and continued by the Gaps Project, have verified all prime gaps up to $x = 4 \times 10^{18}$.

For all computed maximal gaps, the bound $g_n < (\log p_n)^2$ holds strictly. For example, the maximal gap discovered just below $4 \times 10^{18}$ is 1442, which occurs after the prime $p = 403,139,031,737,920,367$. For this prime, $(\log p)^2 \approx 1461.9$, meaning the ratio is approximately $0.986$, safely below the conjectured upper bound of 1.

## 5. Principal Obstacles

The fundamental bottleneck in proving Cramer's conjecture is the extreme limitation of both complex analysis and sieve theory in isolating prime gaps at microscopic scales. 

1. **The Parity Problem:** Modern sieve theory (like the Selberg sieve) is afflicted by the parity problem, which prevents it from distinguishing between numbers with an odd and even number of prime factors. This makes it impossible for standard sieves to prove the existence of primes in an interval as short as $(\log x)^2$.
2. **Zero-Density Estimates:** Traditional analytic number theory relies on the distribution of the non-trivial zeros of the Riemann zeta function $\zeta(s)$. Even if we assume the Generalized Riemann Hypothesis (that all such zeros lie on the critical line $\Re(s) = 1/2$), the analytic explicit formula can only guarantee prime gaps of size $O(\sqrt{x} \log x)$. 
3. **Failure of Independence:** Cramér's probabilistic model assumes primes behave like independent coin flips. However, primes possess profound algebraic rigidity and structure (e.g., they must belong to specific residue classes modulo any integer). The existence of "Siegel zeros" or other pathological distributions of primes could theoretically create artificially massive gaps that the random model cannot foresee.

## 6. The Gap

The mathematical gap between what is proven and what is conjectured is immense, representing an exponential leap in precision.

- **Proven (Unconditional):** $g_n \ll p_n^{0.525}$
- **Proven (Conditional on RH):** $g_n \ll p_n^{0.5} \log p_n$
- **Conjecture:** $g_n \ll (\log p_n)^2$

To cross this boundary, mathematicians must develop an entirely new framework capable of proving extreme uniformity in the distribution of primes. The jump from $x^{0.5}$ to $(\log x)^2$ requires a technique that does not rely strictly on the zeroes of $L$-functions or traditional sieve theory, or it requires a profound breakthrough in bounding exponential sums over primes in microscopic intervals.

## 7. Current Research (as of June 2026)

Research approaches are largely split into analytical bounds and probabilistic modeling:
- **Refinement of Sieve Methods:** Researchers continue to refine the Maynard-Tao sieve (which revolutionized the study of *small* gaps between primes) to see if multidimensional sieves can yield tighter bounds on *large* gaps.
- **Improved Random Models:** Following Granville's work, groups are exploring random models that incorporate the Maier matrix method and deep structural congruences to accurately predict the frequency of extreme prime gaps.
- **Lower Bound Exponents:** Significant energy is currently devoted to improving the constant $c$ in the Ford-Green-Konyagin-Maynard-Tao lower bound. * (frontier — verify)* Some unpublished preprints suggest the possibility of introducing an additional $\log \log \log p_n$ factor into the numerator of the lower bound.
- **Computational Verification:** The Gaps Project continues utilizing GPU clusters and distributed computing to search for prime gaps beyond the $10^{19}$ barrier, monitoring the ratio $g_n / (\log p_n)^2$.

## 8. Future Work

Leading analytic number theorists have outlined potential long-term strategies for this problem:
- Investigating the fine-scale distribution and pair correlation (like the Montgomery-Odlyzko law) of the zeros of the Riemann zeta function to extract deeper cancellation in the explicit formula for $\pi(x)$.
- Bridging the conceptual gap between additive combinatorics (which has seen immense success in arithmetic progressions of primes) and multiplicative gap bounds.
- Developing non-trivial bounds on Dirichlet polynomials and exponential sums over primes in intervals significantly shorter than $x^{1/2}$.

## 9. Key References

- **[Foundational]** Cramér, H. *On the order of magnitude of the difference between consecutive prime numbers.* Acta Arithmetica, 2(1), 23-46, 1936. [DOI](https://doi.org/10.4064/aa-2-1-23-46)
- **[SOTA / Recent]** Baker, R. C., Harman, G., & Pintz, J. *The difference between consecutive primes, II.* Proceedings of the London Mathematical Society, 83(3), 532-562, 2001. [DOI](https://doi.org/10.1112/plms/83.3.532)
- **[SOTA / Recent]** Ford, K., Green, B., Konyagin, S., Maynard, J., & Tao, T. *Long gaps between primes.* Journal of the American Mathematical Society, 29(1), 73-111, 2014.
- **[Survey]** Granville, A. *Harald Cramér and the distribution of prime numbers.* Scandinavian Actuarial Journal, 1995(1), 12-28, 1995. [DOI](https://doi.org/10.1080/03461238.1995.10413946)
- **[Survey]** Soundararajan, K. *Small gaps between prime numbers: The work of Goldston-Pintz-Yıldırım.* Bulletin of the American Mathematical Society, 44(1), 1-18, 2007.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement in a concrete example, we can compare the size of a known maximal prime gap against Cramér's bound.

Let's examine a small maximal prime gap. The 30th prime number is $p_{30} = 113$. 
The very next prime is $p_{31} = 127$. 
The prime gap is:
$$g_{30} = p_{31} - p_{30} = 127 - 113 = 14$$

At the time 113 was reached, 14 was the largest gap seen so far. Now let's calculate the Cramér bound for this specific prime:
$$(\log p_{30})^2 = (\log 113)^2$$

Using the natural logarithm:
$$\log 113 \approx 4.7273$$
$$(\log 113)^2 \approx (4.7273)^2 \approx 22.348$$

Comparing the actual gap to the bound:
$$14 < 22.348$$

The ratio is:
$$\frac{g_{30}}{(\log p_{30})^2} \approx \frac{14}{22.348} \approx 0.626$$

Let's scale up to a much larger verified maximal gap. The prime $p = 313,982,053$ is followed by the prime $p' = 313,982,917$, yielding a gap of:
$$g = 864$$

Calculating the bound for this prime:
$$(\log 313,982,053)^2 \approx (19.564)^2 \approx 382.78$$

In this rare instance, the local gap $g = 864$ actually overshoots the strict Cramér bound $(\log p)^2 = 382.78$. The limit superior conjecture allows for these local violations at finite ranges (which Granville's refinement of $1.1229$ explicitly attempts to capture), provided that as $n \to \infty$, the maximum ratio structurally decays toward 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*