---
id: 01-number-theory/agoh-giuga-conjecture
title: "Agoh-Giuga Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Agoh-Giuga Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/agoh-giuga-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Agoh-Giuga conjecture is an open problem in number theory asserting that an integer $n \ge 2$ is a prime number if and only if it satisfies the congruence relation:
$$ n B_{n-1} \equiv -1 \pmod n $$
where $B_{n-1}$ is the $(n-1)$-th Bernoulli number. 

This statement is mathematically equivalent to the earlier formulation by Giuseppe Giuga, which states that an integer $n \ge 2$ is prime if and only if:
$$ \sum_{k=1}^{n-1} k^{n-1} \equiv -1 \pmod n $$

A complete proof of the conjecture requires demonstrating that no composite integer $n$ satisfies these congruences. Conversely, a disproof requires finding a single composite "counterexample" that satisfies the condition. 

## 2. Mathematical Foundations

The conjecture relies deeply on the properties of sums of powers and Bernoulli numbers. The Bernoulli numbers $B_k$ are formally defined via the exponential generating function:
$$ \frac{x}{e^x - 1} = \sum_{k=0}^{\infty} B_k \frac{x^k}{k!} $$

For any prime number $p$, Fermat's Little Theorem guarantees that $k^{p-1} \equiv 1 \pmod p$ for all integers $1 \le k < p$. Summing these evaluations trivially yields:
$$ \sum_{k=1}^{p-1} k^{p-1} \equiv \sum_{k=1}^{p-1} 1 = p-1 \equiv -1 \pmod p $$
Thus, all prime numbers satisfy the congruence. The difficulty lies entirely in proving the non-existence of composite numbers that masquerade as primes under this test.

The equivalence between Giuga's sum of powers and Agoh's Bernoulli formulation is governed by the von Staudt–Clausen theorem, which dictates the fractional part of Bernoulli numbers. For any even integer $k$:
$$ B_k + \sum_{p-1 \mid k} \frac{1}{p} \in \mathbb{Z} $$
where the sum ranges over all primes $p$ such that $p-1$ divides $k$. 

Any composite number satisfying the conjecture must simultaneously be a **Carmichael number** and a **Giuga number**.
*   **Carmichael number**: A composite integer $n$ such that for all prime factors $p \mid n$, we have $(p-1) \mid (n-1)$.
*   **Giuga number**: A composite integer $n$ such that for all prime factors $p \mid n$, we have $p \mid \left(\frac{n}{p} - 1\right)$. Equivalently, a Giuga number satisfies the Diophantine equation:
$$ \sum_{p \mid n} \frac{1}{p} - \frac{1}{n} = \nu $$
for some positive integer $\nu \in \mathbb{N}$.

## 3. History & State of the Art (SOTA)

Giuseppe Giuga proposed the original sum-of-powers conjecture in 1950, computationally verifying it for all integers up to $10^{1000}$. 

In 1990, Takashi Agoh independently arrived at the Bernoulli number formulation, realizing its deep connection to Giuga's work. Agoh formally published the proof of equivalence between his Bernoulli formulation and Giuga's conjecture in a 1995 paper in *Manuscripta Mathematica*.

Because potential counterexamples must satisfy phenomenally strict multiplicative properties, state-of-the-art computational verifications do not rely on brute-force sequential checking. Instead, researchers use algebraic sieve methods to rule out the existence of prime factors. The computational bounds have progressed as follows:
*   **1985**: E. Bedocchi increased the lower bound to $10^{1700}$.
*   **1996**: D. Borwein, J. M. Borwein, P. B. Borwein, and R. Girgensohn proved that any counterexample must have at least 13,800 decimal digits.
*   **2013**: J. M. Borwein, C. Maitland, and M. Skerritt established the current SOTA bound, pushing the minimum size of a counterexample to 19,908 decimal digits.

## 4. Partial Results / Verified Cases

While the conjecture remains open in its general form, highly restrictive structural constraints have been mathematically proven for any potential composite counterexample $n$:
*   **Square-free:** $n$ cannot be divisible by the square of any prime number.
*   **Odd Parity:** Since $n$ must be a Carmichael number (and all Carmichael numbers are odd), any counterexample must be an odd number. Consequently, $n$ must be an *odd Giuga number*.
*   **Factor Density:** $n$ must be composed of at least 4,771 distinct prime factors.
*   **Size Limits:** $n$ must exceed $10^{19908}$ (i.e., it must have at least 19,908 decimal digits).

To date, all known Giuga numbers (e.g., 30, 858, 1722, 66198) are even. No odd Giuga numbers have ever been discovered. 

## 5. Principal Obstacles

The primary obstacle is the heavily constrained, seemingly contradictory nature of the hypothetical counterexamples. Standard techniques in analytic number theory are generally too loose to categorically rule out the existence of a highly composite, odd Giuga-Carmichael number.

Furthermore, the problem reduces to solving nonlinear Diophantine equations involving Egyptian fractions. Specifically, finding an odd Giuga number requires solving the reciprocal sum $\sum_{p \mid n} \frac{1}{p} - \frac{1}{n} = \nu$ with strictly odd denominators. Bounding or proving the impossibility of such a sum, while simultaneously enforcing the multiplicative Carmichael constraint ($(p-1) \mid (n-1)$), is a notoriously intractable bottleneck. This intertwines additive and multiplicative prime constraints in a way that modern sieve theories struggle to parse.

## 6. The Gap

The exact boundary lies between the massive computational evidence—which unconditionally rules out counterexamples below 19,908 digits—and a rigorous algebraic or analytic proof that the intersection of the set of odd Giuga numbers and the set of Carmichael numbers is strictly empty. Bridging this gap requires either an unprecedented sieve method capable of demonstrating that the combined algebraic constraints are mutually exclusive, or a definitive proof that the set of odd Giuga numbers is entirely empty.

## 7. Current Research (as of June 2026)

Active research primarily focuses on computational and algorithmic number theory, leveraging highly parallelized searches to iteratively improve the lower bounds on the number of prime factors and total digits. Researchers are also heavily investigating the generalized Egyptian fraction problem for odd denominators.

*(frontier — verify)* Recent preprints explore connections between the Agoh-Giuga conjecture and the odd greedy algorithm for Egyptian fractions, attempting to prove structurally that the sum of reciprocals of odd primes cannot equal an integer plus $1/n$ under Korselt's criteria. 

## 8. Future Work

Leading mathematicians outline the following pathways for future resolution:
*   **Odd Giuga Numbers:** Formally proving the non-existence of odd Giuga numbers. Because a counterexample must be an odd Giuga number, this proof would immediately resolve the Agoh-Giuga conjecture in the affirmative.
*   **Improved Bounds:** Pushing the minimum number of prime factors beyond 4,771 to force the size of a potential counterexample into theoretically impossible ranges, creating a proof by exhaustion via structural limits.
*   **Algebraic Sieve Methods:** Developing new generalized sieve methodologies capable of parsing simultaneous multiplicative congruences and additive Egyptian fraction topologies.

## 9. Key References

*   **[Foundational]** Giuga, G. *Su una presumibile proprietà caratteristica dei numeri primi.* Istituto Lombardo di Scienze e Lettere, Rendiconti, 1950.
*   **[Foundational]** Agoh, T. *On Giuga's conjecture.* Manuscripta Mathematica, 1995.
*   **[SOTA / Recent]** Borwein, D., Borwein, J. M., Borwein, P. B., & Girgensohn, R. *Giuga's Conjecture on Primality.* American Mathematical Monthly, 1996.
*   **[SOTA / Recent]** Borwein, J. M., Maitland, C., & Skerritt, M. *Computation of an improved lower bound to Giuga's primality conjecture.* Integers, 2013.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, consider the conjecture evaluated at a small prime ($n = 5$) and a small composite number ($n = 4$).

**Case 1: A Prime Number ($n = 5$)**
Using Giuga's sum of powers formulation:
$$ \sum_{k=1}^{4} k^{4} = 1^4 + 2^4 + 3^4 + 4^4 = 1 + 16 + 81 + 256 = 354 $$
Taking the result modulo 5:
$$ 354 = 5 \times 70 + 4 \equiv -1 \pmod 5 $$

Using Agoh's Bernoulli formulation:
The 4th Bernoulli number is $B_4 = -1/30$.
$$ n B_{n-1} = 5 B_4 = 5 \left(-\frac{1}{30}\right) = -\frac{1}{6} $$
To evaluate $-1/6 \pmod 5$, we find the modular inverse of $6 \pmod 5$. Since $6 \equiv 1 \pmod 5$, its inverse is $1$.
$$ -\frac{1}{6} \equiv -1 \times 1 \equiv -1 \pmod 5 $$
Both formulations correctly identify 5 as prime.

**Case 2: A Composite Number ($n = 4$)**
Using Giuga's sum of powers formulation:
$$ \sum_{k=1}^{3} k^{3} = 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 $$
Taking the result modulo 4:
$$ 36 = 4 \times 9 \equiv 0 \pmod 4 $$

Using Agoh's Bernoulli formulation:
The 3rd Bernoulli number is $B_3 = 0$.
$$ n B_{n-1} = 4 B_3 = 4 \times 0 = 0 \equiv 0 \pmod 4 $$
Both formulations yield $0 \not\equiv -1 \pmod 4$, correctly classifying 4 as a composite number.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*