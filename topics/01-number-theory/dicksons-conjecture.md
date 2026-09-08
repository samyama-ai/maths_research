---
id: 01-number-theory/dicksons-conjecture
title: "Dickson's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dickson's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/dicksons-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Dickson's Conjecture (formulated by L. E. Dickson in 1904) states that for any finite set of linear polynomials $L_1(n) = a_1n + b_1, L_2(n) = a_2n + b_2, \dots, L_k(n) = a_kn + b_k$ with integer coefficients where each $a_i \ge 1$, if there is no prime number $p$ that divides the product $L_1(n)L_2(n)\dots L_k(n)$ for every integer $n$, then there exist infinitely many positive integers $n$ such that $L_1(n), L_2(n), \dots, L_k(n)$ are all prime numbers simultaneously.

The condition that no prime $p$ divides the product for all $n$ is known as the "admissibility" condition. A complete proof of Dickson's Conjecture would establish a vast generalization of Dirichlet's theorem on arithmetic progressions and prove the existence of infinitely many prime constellations of any admissible pattern, subsuming the famous Twin Prime Conjecture.

## 2. Mathematical Foundations

Let $\mathcal{L} = \{L_1, \dots, L_k\}$ be a set of linear polynomials where $L_i(x) = a_i x + b_i$ with $a_i, b_i \in \mathbb{Z}$ and $a_i \ge 1$ for all $1 \le i \le k$.

The set $\mathcal{L}$ is called **admissible** if, for every prime number $p$, there exists an integer $n_p$ such that $p$ does not divide the product $\prod_{i=1}^k L_i(n_p)$. Equivalently, the number of solutions $\omega(p)$ to the polynomial congruence
$$ \prod_{i=1}^k L_i(n) \equiv 0 \pmod p $$
satisfies $\omega(p) < p$ for all primes $p$.

**Dickson's Conjecture:** If $\mathcal{L}$ is an admissible set of linear polynomials, then the set
$$ \mathcal{N} = \{n \in \mathbb{N} \mid L_1(n), \dots, L_k(n) \text{ are all prime} \} $$
has infinite cardinality (i.e., $|\mathcal{N}| = \infty$).

This conjecture relies on the fundamental theorem of arithmetic and modular arithmetic. The condition $\omega(p) < p$ is a necessary local condition (to avoid a local obstruction where some prime always divides one of the polynomial values). The conjecture asserts that this local necessary condition is also sufficient for the global property of simultaneous primality infinitely often.

## 3. History & State of the Art (SOTA)

- **1837:** Peter Gustav Lejeune Dirichlet proved his theorem on primes in arithmetic progressions, establishing the conjecture for $k=1$.
- **1904:** Leonard Eugene Dickson formulated the conjecture for general $k$, recognizing that extending Dirichlet's theorem to tuples of primes required a precise local admissibility condition to avoid trivial divisibility barriers.
- **1923:** G. H. Hardy and J. E. Littlewood proposed the First Hardy-Littlewood Conjecture (Prime Tuple Conjecture), which not only asserts the existence of infinitely many such $n$ but also gives a precise asymptotic formula for their distribution density.
- **1958:** Andrzej Schinzel and Wacław Sierpiński generalized Dickson's Conjecture to polynomials of arbitrary degree, known today as Schinzel's Hypothesis H.
- **2004:** Ben Green and Terence Tao proved the Green-Tao Theorem, showing that the sequence of prime numbers contains arbitrarily long arithmetic progressions. While a landmark result in additive combinatorics, it does not prove Dickson's conjecture for specific admissible sets (like the twin primes).
- **2013:** Yitang Zhang proved bounded gaps between primes. This was subsequently improved by James Maynard, Terence Tao, and the Polymath8 project, culminating in the Maynard-Tao theorem, which proves a weak, collective form of Dickson's Conjecture.

## 4. Partial Results / Verified Cases

- **$k=1$ (Dirichlet's Theorem):** If $\gcd(a_1, b_1) = 1$, then $L_1(n) = a_1n + b_1$ is prime infinitely often. This is fully resolved.
- **Bounded Gaps:** We know unconditionally that there exists some integer $h \le 246$ such that the set $\{n, n+h\}$ yields two primes infinitely often (though a specific $h$, such as $h=2$ for twin primes, has not been proven to work).
- **Chen's Theorem (1966):** A near-miss for $k=2$. For $L_1(n) = n$ and $L_2(n) = n+2$, Jingrun Chen proved that there are infinitely many $n$ such that $L_1(n)$ is prime and $L_2(n)$ is either a prime or a semiprime (a product of exactly two primes).
- **Maynard-Tao Theorem (2013):** For any integer $m \ge 2$, there exists an integer $k \ge m$ such that for *any* admissible set of $k$ linear polynomials, at least $m$ of them are simultaneously prime infinitely often. However, the exact subset of $m$ polynomials can vary with $n$, so this does not prove the conjecture for any *specific* set of $m$ polynomials.

## 5. Principal Obstacles

The primary technical bottleneck is the **"parity problem"** in sieve theory, first formalized by Atle Selberg. Classical sieve methods (such as the Brun sieve or the Selberg sieve) operate on bounds of prime divisors and are fundamentally unable to distinguish between integers with an odd number of prime factors and integers with an even number of prime factors. 

Because prime numbers have exactly one prime factor (an odd number), sieves alone cannot isolate absolute primes from semiprimes (which have two prime factors). To break the parity barrier, one must inject additional structural or bilinear information into the sieve weights (e.g., using the Bombieri-Vinogradov theorem). While this worked for Chen's theorem (allowing a prime and a semiprime) and the Maynard-Tao results (yielding *some* primes in a sufficiently large tuple), it completely fails to pinpoint simultaneous primality for a *specific* small tuple like $k=2$ for $\{n, n+2\}$.

## 6. The Gap

The gap lies precisely between proving that "at least $m$ out of $k$ admissible polynomials are prime" (the Maynard-Tao milestone) and proving that "all $k$ out of $k$ admissible polynomials are prime" (Dickson's Conjecture). 

To cross this mathematical barrier, the field requires a fundamentally new analytic or combinatorial tool that bypasses the parity problem of sieve theory for small tuples. We need a mechanism to detect prime values directly in dense subsets of the integers without being spoofed by products of two primes, potentially through unprecedented advances in higher-order Fourier analysis, automorphic forms, or algebraic geometry over finite fields.

## 7. Current Research (as of June 2026)

Active research directions and schools of thought include:
- **Multidimensional Sieve Refinements:** Efforts to refine the multidimensional Selberg sieve weights (pioneered by Maynard) to aggressively reduce the required size of $k$ for a given $m$ in the Maynard-Tao theorem, pushing closer to $k=m$.
- **Higher-Order Fourier Analysis:** Building on the Gowers norms and the work of Green, Tao, and Ziegler, researchers are investigating the distribution of primes in more complex polynomial orbits.
- **Analytic Number Theory & Error Bounds:** Investigating the zeros of Dirichlet L-functions to improve error bounds in the distribution of primes in arithmetic progressions, which directly feeds the efficiency of sieve weights.
- *(frontier — verify)* Recent preprints explore non-abelian trace formulas and higher-dimensional expander graphs to bypass the parity barrier, though none have successfully demonstrated simultaneous primality for fixed $k \ge 2$.

## 8. Future Work

Leading mathematicians suggest the following open pathways:
- **Improving the Bombieri-Vinogradov Theorem:** Proving the Elliott-Halberstam conjecture, which bounds the error terms of primes in arithmetic progressions beyond the square-root barrier. Assuming a generalized Elliott-Halberstam conjecture, the bounded gap between primes drops to 2 (proving the Twin Prime Conjecture).
- **Breaking the Parity Problem:** Developing a "Type III" sum or a completely novel combinatorial identity that allows sieves to definitively isolate numbers with exactly one prime factor within a specific $k$-tuple.
- **Algebraic Geometry over $\mathbb{F}_p$:** Utilizing techniques originating from the Weil conjectures to study the equidistribution of polynomial roots modulo primes in ways that inform the global distribution of prime tuples.

## 9. Key References

- **[Foundational]** Dickson, L. E. *A new extension of Dirichlet's theorem on prime numbers.* Messenger of Mathematics, 1904.
- **[Foundational]** Hardy, G. H., and Littlewood, J. E. *Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes.* Acta Mathematica, 1923. [DOI](https://doi.org/10.1007/bf02403921)
- **[SOTA / Recent]** Maynard, J. *Small gaps between primes.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)
- **[SOTA / Recent]** Green, B., and Tao, T. *The primes contain arbitrarily long arithmetic progressions.* Annals of Mathematics, 2008. [DOI](https://doi.org/10.4007/annals.2008.167.481)
- **[Survey]** Granville, A. *Primes in intervals of bounded length.* Bulletin of the American Mathematical Society, 2015. [DOI](https://doi.org/10.1090/s0273-0979-2015-01480-1)
- **[Survey]** Soundararajan, K. *Small gaps between prime numbers: The work of Goldston-Pintz-Yıldırım.* Bulletin of the American Mathematical Society, 2007.

## 10. Worked Example / Concrete Special Case

Consider the case $k=3$ with the simple linear polynomials:
- $L_1(n) = n$
- $L_2(n) = n + 2$
- $L_3(n) = n + 4$

Is this set of polynomials admissible? We must check if there is a prime $p$ that divides the product $P(n) = n(n+2)(n+4)$ for *every* integer $n$. 
Let's check small primes:
- For $p=2$: If $n=1$, $P(1) = 1 \cdot 3 \cdot 5 = 15$, which is not divisible by 2.
- For $p=3$:
  - If $n \equiv 0 \pmod 3$, then $3 \mid n$, so $3 \mid P(n)$.
  - If $n \equiv 1 \pmod 3$, then $n+2 \equiv 3 \equiv 0 \pmod 3$, so $3 \mid (n+2)$ and $3 \mid P(n)$.
  - If $n \equiv 2 \pmod 3$, then $n+4 \equiv 6 \equiv 0 \pmod 3$, so $3 \mid (n+4)$ and $3 \mid P(n)$.

For every possible integer $n$, $P(n)$ is divisible by 3. The necessary local condition fails at $p=3$. Therefore, this set of polynomials is **not admissible**. There cannot be infinitely many primes of the form $(p, p+2, p+4)$. (In fact, the only such prime triplet is $(3, 5, 7)$, because for any other starting prime, one of the three numbers must be a multiple of 3).

Now consider a modified case: $L_1(n) = n, L_2(n) = n+2, L_3(n) = n+6$ (the Prime Triplet).
- For $p=2$: $P(1) = 1 \cdot 3 \cdot 7 = 21 \not\equiv 0 \pmod 2$.
- For $p=3$: $P(2) = 2 \cdot 4 \cdot 8 = 64 \not\equiv 0 \pmod 3$.
- For $p=5$: $P(1) = 21 \not\equiv 0 \pmod 5$.

For any prime $p > 3$, the polynomial $P(n)$ of degree 3 has at most 3 roots modulo $p$. Since $3 < p$, there is always at least one congruence class $n \pmod p$ such that $P(n) \not\equiv 0 \pmod p$. 

Thus, this set is **admissible**. Dickson's Conjecture predicts that there are infinitely many positive integers $n$ such that $n, n+2,$ and $n+6$ are all simultaneously prime. 
Concrete instances of this include:
- $n=5 \implies (5, 7, 11)$
- $n=11 \implies (11, 13, 17)$
- $n=17 \implies (17, 19, 23)$
- $n=41 \implies (41, 43, 47)$

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*