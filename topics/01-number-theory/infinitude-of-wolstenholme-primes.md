---
id: 01-number-theory/infinitude-of-wolstenholme-primes
title: "Infinitude of Wolstenholme Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Wolstenholme Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-wolstenholme-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there are infinitely many Wolstenholme primes. A Wolstenholme prime is defined as a prime number $p \ge 5$ that satisfies the congruence:

$$ \binom{2p-1}{p-1} \equiv 1 \pmod{p^4} $$

The problem asks for a rigorous mathematical proof (or disproof) that the cardinality of the set of all such primes is infinite. 

## 2. Mathematical Foundations

The conjecture is rooted in Wolstenholme's Theorem (1862), which established that for every prime $p \ge 5$:

$$ \binom{2p-1}{p-1} \equiv 1 \pmod{p^3} $$

For a prime $p$, the **Wolstenholme quotient** is defined as the integer:

$$ W_p = \frac{\binom{2p-1}{p-1} - 1}{p^3} $$

A prime $p \ge 5$ is a Wolstenholme prime if and only if $W_p \equiv 0 \pmod{p}$. 

The problem is deeply connected to **harmonic numbers** and **Bernoulli numbers**. Let $H_{n, k} = \sum_{i=1}^n \frac{1}{i^k}$ be the generalized harmonic number. Wolstenholme's theorem is equivalent to the conditions:

$$ H_{p-1, 1} \equiv 0 \pmod{p^2} \quad \text{and} \quad H_{p-1, 2} \equiv 0 \pmod{p} $$

A prime is a Wolstenholme prime if it satisfies the higher-order congruence $H_{p-1, 1} \equiv 0 \pmod{p^3}$. Furthermore, via Glaisher's congruence (1900), the binomial coefficient can be expanded in terms of Bernoulli numbers $B_n$:

$$ \binom{2p-1}{p-1} \equiv 1 - \frac{2}{3} p^3 B_{p-3} \pmod{p^4} $$

Thus, a prime $p \ge 5$ is a Wolstenholme prime if and only if $p$ divides the numerator of the Bernoulli number $B_{p-3}$. This classifies Wolstenholme primes as a specific subset of **irregular primes**, specifically those that form an irregular pair of the form $(p, p-3)$.

## 3. History & State of the Art (SOTA)

- **1862:** Joseph Wolstenholme proved his eponymous theorem, establishing the $p^3$ congruence for all $p \ge 5$.
- **1900:** J. W. L. Glaisher established the deep connection between the Wolstenholme quotient and the Bernoulli number $B_{p-3}$.
- **1964:** The first Wolstenholme prime, $p = 16843$, was discovered computationally by Selfridge and Pollack after a search up to $25,000$.
- **1993:** Buhler, Crandall, Ernvall, and Metsänkylä discovered the second Wolstenholme prime, $p = 2124679$, during a computational search for irregular primes up to $4 \times 10^6$.
- **2007:** McIntosh and Roettger extended the search space up to $10^9$. No further Wolstenholme primes were discovered.

The heuristic state of the art models the Wolstenholme quotient $W_p \pmod{p}$ as a uniformly distributed pseudo-random variable. Under this assumption, the probability that $p$ is a Wolstenholme prime is $1/p$. Summing these probabilities over primes $p \ge 5$ yields the expected number of Wolstenholme primes up to $x$:

$$ \sum_{5 \le p \le x} \frac{1}{p} \approx \log \log x + M - \frac{1}{2} - \frac{1}{3} $$

where $M \approx 0.261$ is the Meissel–Mertens constant. Since the harmonic sum of primes diverges, this heuristic implies there should be infinitely many Wolstenholme primes, albeit distributed extremely sparsely.

## 4. Partial Results / Verified Cases

Currently, the problem is only solved computationally for finite bounds.
- It has been strictly verified that there are exactly two Wolstenholme primes in the interval $[5, 10^9]$: $p_1 = 16843$ and $p_2 = 2124679$.
- The extreme sparsity is consistent with the heuristic model. For $x = 10^9$, the expected number of Wolstenholme primes is $\approx 2.5$. The discovery of exactly two primes perfectly aligns with probabilistic expectations. 
- No infinite classes or families of Wolstenholme primes have been proven to exist.

## 5. Principal Obstacles

The problem remains unsolved because algebraic number theory currently lacks the tools to deterministically control or predict the precise $p$-adic valuation of Bernoulli numbers at the specific index $p-3$. 

While K. L. Jensen proved in 1915 that there are infinitely many irregular primes (meaning $p$ divides the numerator of *some* $B_k$ for even $k < p-1$), modern mathematics provides no mechanism to "pin down" the irregularity to exactly $k = p-3$. Standard techniques in algebraic topology, Iwasawa theory, and $p$-adic L-functions yield broad structural congruences but do not govern the localized pseudo-random vanishing of $W_p \pmod{p}$. Without an underlying algebraic or geometric invariant that forces $W_p \equiv 0 \pmod{p}$ infinitely often, the problem resists deterministic proof.

## 6. The Gap

The exact boundary between current knowledge and a full resolution lies in transitioning from the global distribution of irregular primes to the localized evaluation of $B_{p-3}$. To cross this barrier, mathematicians must either:
1. Discover a new deterministic structural property (e.g., via modular forms or Galois representations) that forces $W_p$ to vanish infinitely often.
2. Develop a revolutionary sieve method capable of operating on the sequence of Bernoulli numerators unconditionally, bypassing the parity and pseudo-randomness barriers that paralyze traditional sieve theory.

## 7. Current Research (as of June 2026)

- **Algorithmic Searches:** Groups are leveraging large-scale GPU clusters and distributed computing to push the verification bound past $10^{12}$, hunting for a third Wolstenholme prime. 
- **Iwasawa Theory:** Theoretical research is concentrated on the properties of the ideal class groups of cyclotomic fields and the specific distribution of irregular pairs $(p, p-k)$.
- **Generalizations:** Active work surrounds "Wolstenholme pseudoprimes" (composite numbers satisfying the congruence) and connections to Fibonacci-Wieferich primes, hoping a generalized framework provides new insights.
- *(frontier — verify)* New probabilistic density arguments utilizing $p$-adic modular forms are attempting to establish unconditional upper bounds on the spacing between generalized Wolstenholme primes.

## 8. Future Work

Leading computational number theorists suggest pushing the search bounds to $x = 10^{15}$, at which point $\log \log x$ predicts a high likelihood of encountering a third Wolstenholme prime. Theoretically, future pathways involve searching for anomalies or biases in the distribution of $W_p \pmod{p}$. If a bias is discovered that contradicts the uniform distribution heuristic, it could either provide the structural mechanism needed for an infinitude proof or, conversely, suggest that the set of Wolstenholme primes is finite.

## 9. Key References

- **[Foundational]** Wolstenholme, J. *On Certain Properties of Prime Numbers.* The Quarterly Journal of Pure and Applied Mathematics, 1862.
- **[Foundational]** Glaisher, J. W. L. *Congruences relating to the sums of products of the first $n$ numbers and to other sums.* The Quarterly Journal of Pure and Applied Mathematics, 1900.
- **[SOTA / Recent]** Buhler, J. P., Crandall, R. E., Ernvall, R., and Metsänkylä, T. *Irregular primes and cyclotomic invariants to four million.* Mathematics of Computation, 1993.
- **[SOTA / Recent]** McIntosh, R. J., and Roettger, E. L. *A search for Fibonacci-Wieferich and Wolstenholme primes.* Mathematics of Computation, 2007.
- **[Survey]** Meštrović, R. *Wolstenholme's theorem: Its Generalizations and Extensions in the last hundred and fifty years (1862—2011).* arXiv preprint arXiv:1111.3057, 2011.

## 10. Worked Example / Concrete Special Case

We can illustrate the problem by testing whether $p=5$ and $p=7$ are Wolstenholme primes using different foundational definitions.

**Case 1: Testing $p=5$ via the Binomial Definition**
We calculate the binomial coefficient for $p=5$:
$$ \binom{2(5)-1}{5-1} = \binom{9}{4} = \frac{9 \times 8 \times 7 \times 6}{4 \times 3 \times 2 \times 1} = 126 $$
According to Wolstenholme's Theorem, this must be congruent to 1 modulo $p^3$ ($5^3 = 125$). Indeed:
$$ 126 = 125 + 1 \equiv 1 \pmod{125} $$
To be a Wolstenholme prime, it must satisfy the congruence modulo $p^4$ ($5^4 = 625$). However:
$$ 126 \not\equiv 1 \pmod{625} $$
Thus, $5$ is **not** a Wolstenholme prime.

**Case 2: Testing $p=7$ via the Bernoulli Number Definition**
A prime $p$ is a Wolstenholme prime if and only if $p$ divides the numerator of $B_{p-3}$.
For $p=7$, we look at the Bernoulli number $B_{7-3} = B_4$.
The value of $B_4$ is $-\frac{1}{30}$. 
The numerator is $-1$. Since $7$ does not divide $-1$, $p=7$ is **not** a Wolstenholme prime.

By contrast, for $p = 16843$, the value of $B_{16840}$ is an incredibly massive fraction, but its numerator is perfectly divisible by $16843$, making it the first Wolstenholme prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*