---
id: 01-number-theory/infinitude-of-amicable-numbers
title: "Infinitude of Amicable Numbers"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Amicable Numbers

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-amicable-numbers` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there exist infinitely many pairs of amicable numbers. 

Two distinct positive integers $m$ and $n$ form an amicable pair if the sum of the proper divisors of $m$ equals $n$, and the sum of the proper divisors of $n$ equals $m$. 

A complete proof of this conjecture requires unconditionally demonstrating that the set of all such pairs has infinite cardinality. Conversely, a disproof would require demonstrating that there is a strict upper bound on the maximum size of an amicable pair, rendering the set finite.

## 2. Mathematical Foundations

The formal mathematical framework relies on the sum-of-divisors function, an arithmetic function denoted by $\sigma(n)$. For any positive integer $n$, $\sigma(n)$ is defined as the sum of all positive divisors of $n$:

$$ \sigma(n) = \sum_{d \mid n} d $$

The function $\sigma(n)$ is weakly multiplicative; that is, if $\gcd(a, b) = 1$, then $\sigma(ab) = \sigma(a)\sigma(b)$. For a prime power $p^k$, the value is given by:

$$ \sigma(p^k) = \frac{p^{k+1} - 1}{p - 1} $$

The aliquot sum, denoted as $s(n)$, is the sum of the *proper* divisors of $n$, defined as:

$$ s(n) = \sigma(n) - n $$

An amicable pair is defined as a pair of distinct positive integers $(m, n)$ satisfying the mutual relationship:

$$ s(m) = n \quad \text{and} \quad s(n) = m $$

Equivalently, this can be written as a symmetric Diophantine-like system:

$$ \sigma(m) = \sigma(n) = m + n $$

Let $A(x)$ denote the counting function of amicable numbers up to $x$. The conjecture posits that $\lim_{x \to \infty} A(x) = \infty$.

## 3. History & State of the Art (SOTA)

The study of amicable numbers dates back to antiquity. The Pythagoreans were aware of the smallest amicable pair, $(220, 284)$. In the 9th century, Thabit ibn Qurra derived a profound algebraic rule for generating amicable pairs, which was later rediscovered by Fermat (who found the pair $17296$ and $18416$ in 1636) and Descartes (who found another pair in 1638). 

Leonhard Euler systematically studied the problem in the 18th century, developing "Euler's rule" and compiling a list of 59 amicable pairs. 

In the modern era, the focus shifted to asymptotic density and computational searches. In 1955, Paul Erdős proved that the asymptotic density of amicable numbers is zero. In 1981, Carl Pomerance established a strict upper bound on $A(x)$, proving that amicable numbers are comparatively rare. Today, the state of the art largely involves immense distributed computing projects that have discovered over 1.2 billion amicable pairs, alongside heuristic arguments suggesting that $A(x)$ should grow faster than $x^{1-\epsilon}$, implying their infinitude.

## 4. Partial Results / Verified Cases

While the infinitude remains unproven, several highly significant partial results and conditional generating formulas are verified:

- **Thabit ibn Qurra's Theorem:** For an integer $n > 1$, if $p = 3 \cdot 2^{n-1} - 1$, $q = 3 \cdot 2^n - 1$, and $r = 9 \cdot 2^{2n-1} - 1$ are all prime, then $2^n p q$ and $2^n r$ form an amicable pair. This rule conditionally generates pairs (working for $n=2, 4,$ and $7$), but it is unknown if it yields infinitely many primes.
- **Density Bounds:** Erdős (1955) proved unconditionally that the set of amicable numbers has density $0$. Pomerance (1981) proved the upper bound: 
  $$ A(x) \le x \exp(-c (\log x \log \log \log x / \log \log x)^{1/2}) $$
- **Computational Verification:** Exhaustive computational searches have verified all amicable pairs up to $10^{14}$ (e.g., Moews and Moews, 1993, and further expanded by subsequent supercomputing efforts). The total number of individually known amicable pairs currently exceeds $1.2 \times 10^9$.
- **Parity Constraints:** It is verified that no mutually coprime amicable pairs exist below vast computational limits, and no "even-odd" amicable pairs (where one is even and the other odd) have ever been found.

## 5. Principal Obstacles

The problem remains unsolved because analytic number theory currently lacks the tools to evaluate the simultaneous distribution of the divisor function $\sigma(n)$ on the equation $\sigma(m) = \sigma(n) = m+n$. 

The primary bottleneck is that all known systematic methods for generating amicable pairs (like Thabit's, Euler's, or Borho's rules) force the integers into a specific algebraic template (e.g., $E \cdot p \cdot q$ and $E \cdot r$). These templates only yield amicable pairs if several polynomial expressions evaluate to prime numbers simultaneously. Proving that such simultaneous primes occur infinitely often requires a proof of Schinzel's Hypothesis H or Dickson's Conjecture. 

Standard techniques, such as sieve methods (Brun, Selberg), fail to establish these prime occurrences due to the well-known "parity problem" in sieve theory, which prevents sieves from distinguishing between integers with an even versus an odd number of prime factors. Thus, unconditional existence proofs via these templates are strictly blocked.

## 6. The Gap

The exact boundary between what is proven (Section 4) and the general conjecture (Section 1) lies in transitioning from *conditional* algebraic templates and *empirical* computation to an *unconditional* lower bound. 

We can empirically generate billions of pairs, but we do not have a single mathematical proof that guarantees $A(x)$ is bounded away from a constant as $x \to \infty$. To cross this gap, mathematicians must either bypass the parity problem to prove simultaneous primality for a generation rule, or entirely abandon template-based generation in favor of a novel, likely ergodic or statistical method capable of unconditionally demonstrating the existence of solutions to $\sigma(m) = \sigma(n) = m+n$.

## 7. Current Research (as of June 2026)

Current active research spans two primary domains:

1. **Massive Distributed Computation:** Projects utilizing BOINC frameworks and GPU clusters (such as those maintained by S. Chernykh and other computational number theorists) continuously stretch the exhaustive search limit and look for statistical anomalies, specifically searching for coprime pairs or odd-even pairs.
2. **Heuristic & Asymptotic Analysis:** Researchers are actively attempting to tighten Pomerance's upper bound and formalize lower-bound heuristic models. There is also significant interest in the algebraic geometry of "amicable curves" and extending the aliquot sequence to finite fields.
3. * (frontier — verify)* Recent preprints have attempted to apply ergodic theory on the directed graph of the aliquot function to locate positive-density invariant measures, though these have not yet yielded unconditional lower bounds for standard amicable pairs in $\mathbb{Z}^+$.

## 8. Future Work

Leading mathematicians have articulated several distinct open pathways:
- **Unconditional Lower Bounds:** Developing a sieve or analytic method capable of proving $\lim_{x \to \infty} A(x) = \infty$, completely independent of Hypothesis H.
- **Existence of Odd-Even Pairs:** Finding a single amicable pair where $m \not\equiv n \pmod 2$, or proving that such a pair is mathematically impossible.
- **Coprime Amicable Pairs:** Discovering an amicable pair $(m, n)$ such that $\gcd(m, n) = 1$.
- **Sociable Numbers (Aliquot Cycles):** Generalizing the research to aliquot cycles of length $k > 2$ (e.g., $s(n_1)=n_2, s(n_2)=n_3, \dots, s(n_k)=n_1$). It remains an open question whether there are infinitely many cycles for any fixed $k$.

## 9. Key References

- **[Foundational]** Erdős, P. "On amicable numbers." *Publicationes Mathematicae Debrecen*, 4, 108–111, 1955.
- **[Foundational]** Pomerance, C. "On the distribution of amicable numbers II." *Journal für die reine und angewandte Mathematik*, 325, 183–188, 1981.
- **[SOTA / Recent]** Moews, D., & Moews, P. C. "A search for aliquot cycles and amicable pairs." *Mathematics of Computation*, 61(204), 935-938, 1993.
- **[SOTA / Recent]** Borho, W., & Hoffmann, H. "Breeding amicable numbers in abundance." *Mathematics of Computation*, 46(173), 281-293, 1986.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. Springer, 3rd Edition, 2004. (Section B4: Amicable Numbers).

## 10. Worked Example / Concrete Special Case

The simplest concrete instance of the problem is the first amicable pair: $(220, 284)$. We can walk through both the basic arithmetic and its relation to Thabit's rule.

**Step 1: Direct Verification**
Calculate the proper divisors of $220$: 
$1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110$.
Summing these gives:
$$ s(220) = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284 $$

Calculate the proper divisors of $284$: 
$1, 2, 4, 71, 142$.
Summing these gives:
$$ s(284) = 1 + 2 + 4 + 71 + 142 = 220 $$
Since $s(220) = 284$ and $s(284) = 220$, they are an amicable pair.

**Step 2: Generation via Thabit's Rule**
Thabit ibn Qurra's rule states that if $p = 3 \cdot 2^{n-1} - 1$, $q = 3 \cdot 2^n - 1$, and $r = 9 \cdot 2^{2n-1} - 1$ are all prime, then $2^n p q$ and $2^n r$ are amicable.
Let us evaluate for $n = 2$:
$$ p = 3 \cdot 2^{2-1} - 1 = 3 \cdot 2 - 1 = 5 $$
$$ q = 3 \cdot 2^2 - 1 = 3 \cdot 4 - 1 = 11 $$
$$ r = 9 \cdot 2^{2(2)-1} - 1 = 9 \cdot 2^3 - 1 = 72 - 1 = 71 $$
Since $5$, $11$, and $71$ are strictly prime, the rule guarantees an amicable pair:
$$ m = 2^2 \cdot p \cdot q = 4 \cdot 5 \cdot 11 = 220 $$
$$ n = 2^2 \cdot r = 4 \cdot 71 = 284 $$
This demonstrates precisely how algebraic rules map polynomials yielding simultaneous primes directly to amicable pairs.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*