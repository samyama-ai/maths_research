---
id: 01-number-theory/infinitude-of-fermat-primes
title: "Infinitude of Fermat Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Fermat Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-fermat-primes` · **Status:** open

## 1. Problem Statement / Conjecture

A Fermat number is defined as a positive integer of the form $F_n = 2^{2^n} + 1$, where $n$ is a non-negative integer. If a Fermat number is prime, it is called a Fermat prime.

The classical conjecture regarding the infinitude of Fermat primes takes two opposing forms depending on historical context vs. modern heuristics:
1. **Fermat's Original Conjecture (Historical):** All numbers of the form $F_n$ are prime. (This was famously disproven by Leonhard Euler).
2. **Modern Standard Conjecture:** There are only finitely many Fermat primes—and it is widely believed that the only Fermat primes are the five currently known ($F_0, F_1, F_2, F_3, F_4$). 

The open formal mathematical question remains: **Is the set $\{n \in \mathbb{N} \mid 2^{2^n} + 1 \text{ is prime}\}$ infinite or finite?** 

A complete resolution requires proving either that an infinite sequence of $n$ yields primes (disproving the heuristic), or establishing a rigorous finite upper bound on $n$ for which $F_n$ can be prime.

## 2. Mathematical Foundations

Fermat numbers are sequences parameterized by $n \in \mathbb{N}_0$:
$$ F_n = 2^{2^n} + 1 $$

The sequence grows double-exponentially. The numbers exhibit several deep algebraic properties:
* **Coprimality (Goldbach's Theorem):** Any two distinct Fermat numbers are coprime. That is, if $m \neq n$, then $\gcd(F_m, F_n) = 1$. This property provides a classic proof of the infinitude of prime numbers.
* **Recurrence Relation:** They satisfy $F_n = \prod_{i=0}^{n-1} F_i + 2$.
* **Pépin's Test (1877):** A deterministic primality test specifically formulated for Fermat numbers. For $n \ge 1$, $F_n$ is prime if and only if:
  $$ 3^{(F_n - 1)/2} \equiv -1 \pmod{F_n} $$
* **Geometric Constructibility (Gauss-Wantzel Theorem):** A regular $k$-gon is constructible with a compass and straightedge if and only if $k$ is the product of a power of $2$ and any number of distinct Fermat primes:
  $$ k = 2^a \cdot p_1 \cdot p_2 \cdots p_m $$
  where $a \ge 0$, $m \ge 0$, and the $p_i$ are distinct Fermat primes.

## 3. History & State of the Art (SOTA)

Pierre de Fermat observed in 1650 that $F_0 = 3$, $F_1 = 5$, $F_2 = 17$, $F_3 = 257$, and $F_4 = 65537$ were all prime. He hypothesized that $F_n$ is prime for all $n$. The conjecture stood until 1732 when Leonhard Euler proved that $F_5$ is divisible by $641$, rendering it composite.

Since Euler's discovery, no additional Fermat primes have been found. Over the 19th and 20th centuries, Edouard Lucas and Proth established systematic divisor theorems, specifically that any divisor of $F_n$ must be of the form $k \cdot 2^{n+2} + 1$. 

In the late 20th and 21st centuries, distributed computing projects (most notably PrimeGrid) and specialized software implementing Pépin's test using Fast Fourier Transform (FFT) multiplication algorithms have been deployed to factor or prove the compositeness of larger Fermat numbers.

## 4. Partial Results / Verified Cases

* **Proven Primes:** Only five Fermat primes are known, corresponding to $n = 0, 1, 2, 3, 4$.
* **Proven Composite:** It has been computationally verified that $F_n$ is composite for all $n \in [5, 32]$. 
* **Complete Factorizations:** $F_n$ is completely factored into prime powers only for $n \in \{5, 6, 7, 8, 9, 10, 11\}$. 
* **Specific Large $n$:** Many larger Fermat numbers are known to be composite because specific Proth divisors have been found (e.g., $F_{33473}$ is known to be composite).
* **Smallest Open Case:** As of recent tracking, the smallest Fermat number whose primality status remains completely unknown is $F_{33}$.

## 5. Principal Obstacles

The primary barrier to answering the conjecture is the double-exponential growth of the sequence. 

* **Computational Intractability:** To apply Pépin's test to $F_{33}$, one must perform $2^{33}$ (over 8.5 billion) modular squarings. Since $F_{33}$ itself has $2,585,827,973$ decimal digits, each squaring involves a number that requires gigabytes of memory to store. The FFT convolutions required for multiplication at this scale overwhelm current supercomputing and distributed hardware.
* **Failure of Analytic Number Theory:** Traditional analytic techniques (like the Hardy-Littlewood circle method or sieve theory) rely on the density of the sequence being studied. Because $F_n$ grows double-exponentially, the sequence is far too sparse for standard statistical sieve limits to apply.
* **Lack of Special Structure:** While Mersenne primes ($2^p - 1$) benefit from the highly efficient Lucas-Lehmer test and dense algebraic sieves, Fermat numbers only afford Proth's theorem for divisors, which still leaves vast, intractable search spaces for potential prime factors if $k$ is large.

## 6. The Gap

The exact boundary that needs crossing is the transition from a **probabilistic heuristic** to a **rigorous asymptotic proof**. 

Using the Prime Number Theorem, the probability that a random integer near $F_n$ is prime is roughly $1/\ln(F_n)$. Thus, the expected number of Fermat primes is approximately:
$$ \sum_{n=0}^{\infty} \frac{1}{\ln(F_n)} = \sum_{n=0}^{\infty} \frac{1}{\ln(2^{2^n} + 1)} \approx \sum_{n=0}^{\infty} \frac{1}{2^n \ln 2} = \frac{2}{\ln 2} \approx 2.88 $$
This convergence strongly suggests there are only finitely many Fermat primes (even accounting for local coprimality adjustments, the tail sum $\sum_{n=5}^{\infty}$ is mathematically tiny). However, probability cannot rigorously govern deterministic integer sequences. The gap lies in discovering a novel sieve method or an algebraic geometry mapping that structurally forbids prime characteristics in the sequence $2^{2^n} + 1$ for large $n$.

## 7. Current Research (as of June 2026)

* **Distributed Computing (PrimeGrid):** Ongoing systematic sieving to find small Proth divisors $k \cdot 2^{n+2} + 1$ for unverified Fermat numbers, continuously pushing the lower bound of completely checked divisors.
* **Algorithmic Improvements:** Hardware-level optimizations of the Harvey–van der Hoeven $O(N \log N)$ integer multiplication algorithm are being explored to make FFT-based squarings viable for billion-digit numbers.
* **Generalized Fermat Primes:** Mathematicians actively study numbers of the form $a^{2^n} + 1$ and $k \cdot 2^n + 1$ (Cullen/Woodall paradigms) to identify structural patterns in divisibility that might map backward to the strict $a=2$ case. *(frontier — verify)* New bounds in cyclotomic field theory are sometimes posited to rule out certain prime ideal structures, though they have yet to yield definitive bounds for $F_n$.

## 8. Future Work

Leading mathematical consensus points to three long-term strategies:
1. Identifying deep theoretical limits on the divisors of values of cyclotomic polynomials $\Phi_{2^{n+1}}(2)$.
2. The possible advent of quantum algorithms for modular exponentiation, which may bypass the memory bottlenecks of FFT squarings for Pépin's test on $F_{33}$ and slightly beyond.
3. Establishing that the number of prime factors of $F_n$ scales strictly greater than 1 as $n \to \infty$, perhaps via unproven hypotheses in ABC-conjecture territory or arithmetic dynamics.

## 9. Key References

- **[Foundational]** Křížek, M., Luca, F., Somer, L. *17 Lectures on Fermat Numbers: From Number Theory to Geometry.* Springer-Verlag New York, 2001.
- **[Foundational]** Pépin, T. *Sur la formule $2^{2^n}+1$.* Comptes Rendus de l'Académie des Sciences, 1877.
- **[SOTA / Recent]** Crandall, R. E., Mayer, E. W., Papadopoulos, J. S. *The twenty-fourth Fermat number is composite.* Mathematics of Computation, 2003.
- **[Survey]** Boklan, K. D., Conway, J. H. *Expect at most one billionth of a new Fermat Prime!* The Mathematical Intelligencer 39(1), 2017.

## 10. Worked Example / Concrete Special Case

To understand why Euler was able to disprove Fermat's original conjecture, we can walk through his elegant proof that $641$ divides $F_5 = 2^{2^5} + 1 = 2^{32} + 1$. 

Euler noticed that $641$ can be expressed in two useful algebraic ways:
1. $641 = 5 \cdot 2^7 + 1$ 
2. $641 = 5^4 + 2^4$

From the first equation, working modulo $641$:
$$ 5 \cdot 2^7 \equiv -1 \pmod{641} $$

If we raise both sides to the 4th power:
$$ (5 \cdot 2^7)^4 \equiv (-1)^4 \pmod{641} $$
$$ 5^4 \cdot 2^{28} \equiv 1 \pmod{641} $$

From the second equation, we know:
$$ 5^4 = 641 - 2^4 \implies 5^4 \equiv -2^4 \pmod{641} $$

Substitute this congruence into the previous result:
$$ (-2^4) \cdot 2^{28} \equiv 1 \pmod{641} $$
$$ -2^{32} \equiv 1 \pmod{641} $$
$$ 2^{32} + 1 \equiv 0 \pmod{641} $$

This confirms that $F_5 \equiv 0 \pmod{641}$. Thus, $F_5 = 4,294,967,297$ is composite (specifically, $641 \times 6,700,417$), shattering the claim that all Fermat numbers are prime without requiring exhaustive trial division up to $\sqrt{F_5}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*