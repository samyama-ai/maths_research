---
id: 01-number-theory/firoozbakhts-conjecture
title: "Firoozbakht's Conjecture"
topic: 01-number-theory
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Firoozbakht's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/firoozbakhts-conjecture` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Firoozbakht's conjecture states that the $n$-th root of the $n$-th prime number is a strictly decreasing function of $n$. Formally, if $p_n$ denotes the $n$-th prime number, then the conjecture asserts that:
$$ p_n^{1/n} > p_{n+1}^{1/(n+1)} $$
for all integers $n \ge 1$. 

A complete proof of this conjecture would unconditionally establish one of the strongest known upper bounds on the gaps between consecutive primes, significantly stronger than even Cramér's conjecture. Conversely, a disproof requires finding a specific integer $n$ for which $p_{n+1}^{1/(n+1)} \ge p_n^{1/n}$.

## 2. Mathematical Foundations

Let $\mathbb{P} = \{2, 3, 5, 7, 11, \dots\}$ be the ordered set of prime numbers, where $p_n$ is the $n$-th prime. The prime gap between consecutive primes is defined as $g_n = p_{n+1} - p_n$.

By raising both sides of the conjecture to the power of $n(n+1)$, we obtain the equivalent formulation:
$$ p_n^{n+1} > p_{n+1}^n \iff p_{n+1} < p_n^{1 + 1/n} $$

This algebraic formulation reveals how Firoozbakht's conjecture bounds the prime gap $g_n$. We can take the Maclaurin series expansion of the exponent for large $n$:
$$ p_n^{1 + 1/n} = p_n \cdot p_n^{1/n} = p_n \exp\left(\frac{\log p_n}{n}\right) $$
$$ p_n^{1 + 1/n} = p_n \left( 1 + \frac{\log p_n}{n} + \frac{\log^2 p_n}{2n^2} + O\left(\frac{\log^3 p_n}{n^3}\right) \right) $$

By the Prime Number Theorem, we know that $n \sim \frac{p_n}{\log p_n}$ as $n \to \infty$. Substituting this asymptotic into the expansion gives:
$$ p_n^{1 + 1/n} \approx p_n + \log^2 p_n $$

Therefore, Firoozbakht's conjecture rigorously implies that for all sufficiently large $n$, the prime gap is bounded by:
$$ g_n < \log^2 p_n - \log p_n - 1 $$
This establishes a profound structural bound on the distribution of primes, positing that maximum prime gaps grow marginally slower than $\log^2 p_n$.

## 3. History & State of the Art (SOTA)

The conjecture was proposed by Iranian mathematician Farideh Firoozbakht (1962–2019) from the University of Isfahan in 1982. It gained international prominence after being published in Paulo Ribenboim's 1996 book, *The New Book of Prime Number Records*.

Historically, evaluating prime gaps has relied on Cramér's probabilistic model (1936), which models the primes as a random sequence where the probability of $x$ being prime is $1/\log x$. Cramér's model suggests that the limit superior of the prime gap scales as $g_n \sim \log^2 p_n$. Firoozbakht's conjecture essentially states that $g_n$ is strictly bounded by a function slightly smaller than $\log^2 p_n$.

However, the modern State of the Art views Firoozbakht's conjecture with skepticism. In 1985, Helmut Maier proved that Cramér's model fails for short intervals because it assumes prime probabilities are independent, ignoring the divisibility conditions imposed by small primes. In 1995, Andrew Granville generalized Maier's matrix method, creating a refined probabilistic model which predicts that maximum prime gaps will occasionally be much larger, specifically predicting $\limsup_{n \to \infty} \frac{g_n}{\log^2 p_n} \ge 2e^\gamma \approx 3.562$. If Granville's heuristic holds, Firoozbakht's conjecture must fail for sufficiently large numbers. 

## 4. Partial Results / Verified Cases

Despite theoretical skepticism, empirical support for the conjecture is exceptionally strong. 

- **Computational Range:** Alexei Kourbatov (2015) verified that Firoozbakht's conjecture holds for all primes up to $4 \times 10^{18}$ (four quintillion).
- **Maximal Prime Gaps:** The conjecture has been verified for all known "maximal prime gaps" (primes $p_n$ where $g_n$ is strictly greater than any previous gap). Tomas Oliveira e Silva's extensive computations of maximal gaps up to $4 \times 10^{18}$ show no violations.
- **Specific Structural Cases:** The conjecture is unconditionally satisfied wherever $g_n \le \log p_n$ (which is true on average, as the average gap is $\log p_n$), meaning it only faces potential failure at extremely rare, unusually large gaps.

## 5. Principal Obstacles

The problem remains unsolved due to an immense mismatch between the strength of the conjecture and the limitations of modern analytic number theory. 

1. **Failure of Complex Analysis:** The standard technique for bounding prime gaps involves the explicit formula mapping the zeros of the Riemann zeta function $\zeta(s)$ to the distribution of primes. Even assuming the Riemann Hypothesis (RH) is true, the best conditionally proven bound on prime gaps is $g_n = O(\sqrt{p_n} \log p_n)$. Closing the theoretical gap from $\sqrt{p_n}$ to $\log^2 p_n$ requires understanding the vertical spacing and correlations of zeta zeros (e.g., via the Montgomery Pair Correlation Conjecture) far beyond what RH provides.
2. **Asymptotic Disagreement:** Unconditional sieve methods (like those used by Maynard and Tao) have revolutionized *lower bounds* for gaps, but *upper bounds* remain intractable. Furthermore, techniques cannot currently resolve the conflict between Cramér's random model (which marginally supports Firoozbakht) and Granville's modified heuristic (which strongly contradicts it). 

## 6. The Gap

The boundary between what is proven and the general statement is one of the widest in number theory.
1. **The Theoretical Gap:** The best unconditional upper bound on prime gaps, proven by Baker, Harman, and Pintz (2001), is $g_n = O(p_n^{0.525})$. This is astronomically larger than the Firoozbakht bound of $O(\log^2 p_n)$.
2. **The Empirical Gap:** The conjecture is true up to $10^{19}$, yet theoretical heuristics suggest it is asymptotically false. Bridging this gap requires either a monumental breakthrough to unconditionally bound $g_n$, or a computational discovery of a counterexample—which probabilists predict lies beyond the computational reach of modern hardware (well beyond $10^{30}$).

## 7. Current Research (as of June 2026)

Active research operates on two separated fronts:
- **Computational Mathematics:** Groups utilizing distributed computing, such as PrimeGrid and GIMPS, continue to map maximal prime gaps at unprecedented scales. While they primarily search for large primes, the byproducts of their sieves are used to test Firoozbakht's conjecture at new frontiers.
- **Analytic Number Theory:** Theoretical work focuses heavily on refining the Maier matrix method and sieve theory. Building on the foundational 2014-2016 work of Ford, Green, Konyagin, Maynard, and Tao on large gaps between primes, mathematicians are attempting to prove unconditionally that $g_n / \log^2 p_n$ can exceed $1$, which would directly disprove the conjecture.
- *(frontier — verify)* Active consensus remains that Firoozbakht's conjecture is likely an artifact of small numbers. The crossover point where the Granville-Maier phenomenon produces prime gaps large enough to violate the condition $p_{n+1} < p_n^{1+1/n}$ is expected to exist, but remains out of reach.

## 8. Future Work

Leading mathematicians suggest the following pathways to resolve the conjecture:
- **Proving the Granville Heuristic:** Developing a rigorous proof that $\limsup_{n \to \infty} g_n / \log^2 p_n = 2e^\gamma$, which would unconditionally disprove Firoozbakht's conjecture by showing gaps eventually exceed the $\log^2 p_n$ bound.
- **Prime Deserts:** Constructing explicit algorithmic methods to generate intervals free of primes ("prime deserts") that are strictly larger than $\log^2 p_n$.
- **Improving Unconditional Bounds:** Pushing the Baker-Harman-Pintz bound of $O(p^{0.525})$ closer to $O(p^{0.5})$, which remains the natural barrier of current exponential sum techniques.

## 9. Key References

- **[Foundational]** Ribenboim, Paulo. *The New Book of Prime Number Records*. Springer-Verlag, 1996. 
- **[Foundational]** Baker, R. C., Harman, G., Pintz, J. *The difference between consecutive primes, II*. Proceedings of the London Mathematical Society, 2001.
- **[Survey]** Granville, Andrew. *Unexpected irregularities in the distribution of prime numbers*. Proceedings of the International Congress of Mathematicians (Zürich, 1994), Birkhäuser, 1995.
- **[SOTA / Recent]** Kourbatov, Alexei. *Verification of the Firoozbakht conjecture for primes up to four quintillion*. International Mathematical Forum, 2015.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, we can evaluate the conjecture manually for $n = 4$.

The ordered set of primes is $\mathbb{P} = \{2, 3, 5, 7, 11, 13, \dots\}$.
For $n = 4$, the $4$-th prime is $p_4 = 7$ and the $5$-th prime is $p_5 = 11$.

The conjecture states that $p_4^{1/4} > p_5^{1/5}$. We calculate the numerical values of both sides:
- $p_4^{1/4} = 7^{1/4} = \sqrt[4]{7} \approx 1.62657$
- $p_5^{1/5} = 11^{1/5} = \sqrt[5]{11} \approx 1.61539$

Comparing the values, $1.62657 > 1.61539$, so the inequality strictly holds. 

We can also verify the equivalent bounding formulation, $p_{n+1} < p_n^{1 + 1/n}$:
- We calculate $p_4^{1 + 1/4} = 7^{5/4} = 7 \cdot \sqrt[4]{7} \approx 7 \times 1.62657 = 11.386$
- We check if $p_5 < 11.386$. 

Since $p_5 = 11$, and $11 < 11.386$, the equivalent formulation holds. The true prime gap here is $g_4 = 11 - 7 = 4$, and the upper bound maximum permitted by Firoozbakht's conjecture is $11.386 - 7 = 4.386$, showing that the conjecture successfully (and tightly) bounds this specific prime gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*