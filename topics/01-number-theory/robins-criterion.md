---
id: 01-number-theory/robins-criterion
title: "Robin's Criterion"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Robin's Criterion

> **Topic:** Number Theory · **ID:** `01-number-theory/robins-criterion` · **Status:** open

## 1. Problem Statement / Conjecture

Robin's Criterion provides an elementary, purely arithmetic condition that is strictly equivalent to the Riemann Hypothesis (RH). The conjecture states that the inequality

$$ \sigma(n) < e^\gamma n \ln \ln n $$

holds for all integers $n > 5040$, where $\sigma(n)$ is the sum of the positive divisors of $n$, and $\gamma$ is the Euler-Mascheroni constant. 

Proving this inequality for all $n > 5040$ constitutes a complete proof of the Riemann Hypothesis. Conversely, disproving the inequality for any $n > 5040$ would disprove the Riemann Hypothesis.

## 2. Mathematical Foundations

The problem revolves around the asymptotic growth of the divisor sum function $\sigma(n)$. We define the relevant mathematical objects as follows:

- **The Divisor Function**, $\sigma(n)$, is defined as the sum of all positive divisors of $n$:
  $$ \sigma(n) = \sum_{d \mid n} d $$
- **The Euler-Mascheroni Constant**, $\gamma$, is defined as the limiting difference between the harmonic series and the natural logarithm:
  $$ \gamma = \lim_{m \to \infty} \left( \sum_{k=1}^m \frac{1}{k} - \ln m \right) \approx 0.5772156649 $$
- **Colossally Abundant Numbers (CAN)**: An integer $n$ is colossally abundant if there exists an $\epsilon > 0$ such that for all integers $k > 1$,
  $$ \frac{\sigma(n)}{n^{1+\epsilon}} \ge \frac{\sigma(k)}{k^{1+\epsilon}} $$
  These numbers are characterized by a highly specific prime factorization structure and are the optimal candidates for maximizing $\frac{\sigma(n)}{n \ln \ln n}$.

The foundation of the criterion relies on Grönwall's Theorem (1913), which establishes the asymptotic supremum limit of the divisor function:
$$ \limsup_{n \to \infty} \frac{\sigma(n)}{n \ln \ln n} = e^\gamma $$
Robin's criterion transforms this asymptotic upper bound into a strict, explicit inequality for all sufficiently large $n$, contingent on the Riemann Hypothesis.

## 3. History & State of the Art (SOTA)

The study of the maximal order of the divisor function dates back to Srinivasa Ramanujan's extensive 1915 paper on highly composite numbers, and Thomas Hakon Grönwall's 1913 theorem establishing the limit superior of $\frac{\sigma(n)}{n \ln \ln n}$.

In 1984, the French mathematician Guy Robin proved the conditional equivalence in his paper *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*. He showed that if RH is true, then $\sigma(n) < e^\gamma n \ln \ln n$ for all $n > 5040$. Furthermore, he proved that if RH is false, the inequality will fail for infinitely many values of $n$.

In the modern era, verifying Robin's inequality focuses on superabundant and colossally abundant numbers. Computational efforts have exhaustively verified the inequality up to enormously large bounds. Despite this, a theoretical proof eludes the community because the maximum values of $\sigma(n)$ are deeply intertwined with the precise distribution of prime numbers, which are dictated by the non-trivial zeros of the Riemann zeta function $\zeta(s)$.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, several major partial results have been strictly verified:

- **Computations:** Robin's inequality has been verified for all integers up to massive computational limits (e.g., Akbary and Friggstad verified it for all numbers $n$ up to $10^{10^{10}}$ by checking the necessary CAN conditions).
- **Square-free Integers:** The inequality holds unconditionally for all square-free integers (and more broadly, for integers not divisible by the squares of certain primes).
- **Odd Integers:** Choie, Lichiardopol, Moree, and Solé (2007) unconditionally proved that Robin's inequality holds for all odd integers $n > 9$. 
- **Restriction on Counterexamples:** Akbary and Friggstad (2009) proved that if the Riemann Hypothesis is false, the smallest counterexample $n > 5040$ to Robin's inequality must be a superabundant number (and specifically, colossally abundant). 

## 5. Principal Obstacles

The fundamental bottleneck is that Robin's criterion is rigorously equivalent to the Riemann Hypothesis; thus, proving it requires overcoming the same obstacles as proving RH itself. 

Analytic bounds on the divisor sum function rely on explicit bounds for Chebyshev's functions, $\theta(x) = \sum_{p \le x} \ln p$ and the prime counting function $\pi(x)$. Under the assumption of RH, the error term in the Prime Number Theorem is tightly bounded by $O(x^{1/2} \ln x)$. However, the best unconditional error terms (e.g., from zero-free regions proven by Vinogradov and Korobov) are far too weak to rule out large, highly composite integers constructed from a hypothetical clustering of primes. Standard sieve methods and traditional Fourier analysis on the zeros of $\zeta(s)$ cannot bridge the gap without unconditionally extending the zero-free region of the zeta function to the critical line $\Re(s) = \frac{1}{2}$.

## 6. The Gap

The boundary between verified mathematics and a full proof is precisely the difference between empirical, finite verification on colossally abundant numbers and an infinite, asymptotic guarantee. 

We unconditionally know that $\limsup_{n \to \infty} \frac{\sigma(n)}{n \ln \ln n} = e^\gamma$. We also know that the largest "spikes" in $\frac{\sigma(n)}{n}$ occur at colossally abundant numbers. The gap is demonstrating unconditionally that for all $n > 5040$, the error term in Mertens' 3rd Theorem converges fast enough such that the sequence never pierces the $e^\gamma \ln \ln n$ ceiling. Crossing this gap requires unconditionally proving that the prime-counting function does not possess fluctuations large enough to over-saturate the prime factors of a colossally abundant number.

## 7. Current Research (as of June 2026)

Active research primarily proceeds along two fronts:

1.  **Refining Unconditional Bounds:** Researchers working in analytic number theory continue to sharpen the explicit, unconditional constants for the Rosser-Schoenfeld bounds on Chebyshev’s $\theta(x)$ and $\pi(x)$. Improving these constants directly narrows the theoretical space where a counterexample to Robin's criterion could exist.
2.  **Structural properties of Colossally Abundant Numbers:** Groups at various institutions analyze the highly restrictive arithmetic conditions a counterexample must possess. 
3.  **Alternative Criteria:** Researchers frequently study Robin's criterion in tandem with Nicolas' criterion (concerning Euler's totient function) and Lagarias' criterion (concerning harmonic numbers). 
    * *(frontier — verify)* Recent preprints explore using advanced optimization heuristics to find tighter, purely arithmetic contradictions in the prime signatures of theoretical CAN counterexamples, aiming for an unconditional disproof of a counterexample's existence.

## 8. Future Work

Leading mathematicians suggest the following pathways for approaching the problem:
- **Tighter Bounds on Prime Gaps:** Formulating sharper explicit bounds for the distance between consecutive primes could help bound the prime factorization exponents of colossally abundant numbers.
- **Harmonic Number Equivalences:** Focusing on Lagarias' equivalent elementary problem ($ \sigma(n) < H_n + e^{H_n} \ln(H_n) $ for all $n$, where $H_n$ is the $n$-th harmonic number) because it lacks the exceptional small values ($n \le 5040$) seen in Robin's criterion, potentially offering a more unified algebraic approach.
- **Mertens Product Discrepancies:** Directly attacking the error term of the Mertens product $\prod_{p \le x} (1 - \frac{1}{p})^{-1}$ exclusively evaluated at the prime factors of superabundant numbers.

## 9. Key References

- **[Foundational]** Robin, G. *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*. Journal de Mathématiques Pures et Appliquées, 1984.
- **[Foundational]** Grönwall, T. H. *Some asymptotic expressions in the theory of numbers*. Transactions of the American Mathematical Society, 1913.
- **[SOTA / Recent]** Choie, Y., Lichiardopol, N., Moree, P., & Solé, P. *On Robin's criterion for the Riemann hypothesis*. Journal de Théorie des Nombres de Bordeaux, 2007.
- **[SOTA / Recent]** Akbary, A., & Friggstad, Z. *Superabundant numbers and the Riemann hypothesis*. The American Mathematical Monthly, 2009.
- **[Survey]** Lagarias, J. C. *An elementary problem equivalent to the Riemann hypothesis*. The American Mathematical Monthly, 2002.

## 10. Worked Example / Concrete Special Case

To understand why the condition $n > 5040$ is strictly necessary, we can manually check Robin's inequality for $n = 5040$ (which is a colossally abundant number) and a number slightly larger.

Let $n = 5040$. The prime factorization is $5040 = 2^4 \cdot 3^2 \cdot 5 \cdot 7$.
The sum of divisors $\sigma(n)$ is a multiplicative function:
$$ \sigma(5040) = \sigma(2^4) \sigma(3^2) \sigma(5) \sigma(7) $$
$$ \sigma(5040) = (16+8+4+2+1)(9+3+1)(5+1)(7+1) $$
$$ \sigma(5040) = 31 \times 13 \times 6 \times 8 = 19344 $$

Now, evaluate the right-hand side of Robin's inequality: $e^\gamma n \ln \ln n$.
Using $e^\gamma \approx 1.781072$:
$$ \ln(5040) \approx 8.525161 $$
$$ \ln \ln(5040) \approx 2.143003 $$
$$ \text{RHS} \approx 1.781072 \times 5040 \times 2.143003 \approx 19237.84 $$

Comparing the two sides:
$$ 19344 > 19237.84 $$
Thus, $\sigma(5040) > e^\gamma (5040) \ln \ln (5040)$. The inequality **fails** for $n = 5040$. This is the largest known exception.

Now, let's examine a larger highly composite number, $n = 10080 = 2^5 \cdot 3^2 \cdot 5 \cdot 7$:
$$ \sigma(10080) = \sigma(2^5) \times 13 \times 6 \times 8 = 63 \times 13 \times 6 \times 8 = 39312 $$
Evaluate the right-hand side for $n = 10080$:
$$ \ln(10080) \approx 9.218309 $$
$$ \ln \ln(10080) \approx 2.221191 $$
$$ \text{RHS} \approx 1.781072 \times 10080 \times 2.221191 \approx 39877.58 $$

Comparing the two sides for $n = 10080$:
$$ 39312 < 39877.58 $$
Here, the inequality **holds**. Robin's theorem establishes that if the Riemann Hypothesis is true, this inequality will hold continuously for all integers extending to infinity beyond 5040.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*