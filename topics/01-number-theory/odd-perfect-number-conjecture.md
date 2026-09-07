---
id: 01-number-theory/odd-perfect-number-conjecture
title: "Odd Perfect Number Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Odd Perfect Number Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/odd-perfect-number-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Odd Perfect Number Conjecture posits that there are no odd perfect numbers. 

A perfect number is a positive integer $n$ such that the sum of its proper positive divisors is equal to $n$. Equivalently, the sum of all its positive divisors, denoted by $\sigma(n)$, is equal to $2n$. While it is known that infinitely many even perfect numbers likely exist (in a one-to-one correspondence with Mersenne primes), the existence of an odd perfect number remains one of the oldest unsolved problems in mathematics. A complete proof requires showing that the equation $\sigma(n) = 2n$ has no solutions in the positive odd integers, whereas a disproof requires finding a single, concrete example of an odd perfect number.

## 2. Mathematical Foundations

The problem relies on the properties of the sum-of-divisors function, $\sigma : \mathbb{Z}^+ \to \mathbb{Z}^+$, defined as:
$$ \sigma(n) = \sum_{d|n} d $$

The function $\sigma(n)$ is a multiplicative arithmetic function. This means that if $\gcd(a, b) = 1$, then $\sigma(ab) = \sigma(a)\sigma(b)$. Consequently, if $n$ has the unique prime factorization $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, the sum of its divisors can be computed via:
$$ \sigma(n) = \prod_{i=1}^k \sigma(p_i^{a_i}) = \prod_{i=1}^k \frac{p_i^{a_i+1}-1}{p_i-1} $$

A positive integer $N$ is perfect if and only if:
$$ \sigma(N) = 2N $$

Leonhard Euler established the foundational structural requirement for any hypothetical odd perfect number. Euler proved that if $N$ is an odd perfect number, it must have the factorization form:
$$ N = p^\alpha m^2 $$
where:
- $p$ is prime and $p \equiv 1 \pmod 4$
- $\alpha \equiv 1 \pmod 4$
- $p \nmid m$
- $m$ is a positive odd integer.

In this context, $p$ is referred to as the "special prime" of the odd perfect number.

## 3. History & State of the Art (SOTA)

The study of perfect numbers dates back to ancient Greek mathematics, notably Euclid's *Elements* and Nicomachus's *Introduction to Arithmetic*. However, they primarily considered even perfect numbers. In 1638, René Descartes discovered what is now known as a "spoof" odd perfect number: $D = 3^2 \cdot 7^2 \cdot 11^2 \cdot 13^2 \cdot 22021^1$. If 22021 is mistakenly treated as a prime, the multiplicative formula yields $\sigma(D) = 2D$. This demonstrated that the algebraic equation governing perfect numbers has solutions outside the strict realm of genuine prime factorization.

In modern times, research has largely focused on pushing computational bounds and proving structural constraints. Heuristic arguments by Carl Pomerance in 1974 strongly suggest that odd perfect numbers do not exist, as the constraints required to satisfy $\sigma(N) = 2N$ are overly restrictive.

The state-of-the-art computational bound was significantly advanced in 2012 when Ochem and Rao proved that any odd perfect number must be greater than $10^{1500}$. In 2015, Pace P. Nielsen proved that an odd perfect number must have at least 10 distinct prime factors.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, the problem has been solved (i.e., odd perfect numbers ruled out) for vast computational ranges and specific structural classes:

- **Size Bound:** There is no odd perfect number $N < 10^{1500}$ (Ochem and Rao, 2012).
- **Number of Prime Factors:** $N$ must have at least $10$ distinct prime factors (Nielsen, 2015). If $3 \nmid N$, then $N$ must have at least $12$ distinct prime factors.
- **Largest Prime Factor:** The largest prime factor of $N$ must be strictly greater than $10^8$ (Goto and Ohno, 2008).
- **Second Largest Prime Factor:** The second largest prime factor of $N$ must exceed $10^4$ (Iannucci, 1999).
- **Abundancy Index:** If $N$ is an odd perfect number, it must be the case that $\frac{\sigma(m^2)}{m^2} < \frac{2p}{p+1}$, restricting the density of the factors making up the square part of $N$.
- **Strictly Bounded Sub-classes:** Dickson (1913) proved that for any fixed number of prime factors $k$, there are at most finitely many odd perfect numbers.

## 5. Principal Obstacles

The principal obstacle in resolving the conjecture is the erratic nature of the multiplicative function $\sigma(n)$ combined with the density of prime numbers. To satisfy $\sigma(N) = 2N$, the rational fraction expansion must align perfectly:
$$ \frac{p+1}{p} \approx \frac{p^{\alpha+1}-1}{p^{\alpha}(p-1)} \cdot \prod_{q|m} \frac{q^{2\beta+1}-1}{q^{2\beta}(q-1)} = 2 $$

No algebraic principle directly prevents this rational product from hitting exactly $2$. Descartes's spoof number proves that the purely algebraic structure of the problem *does* allow for solutions if we relax the condition that all bases must be true primes. Because traditional analytic number theory, sieve methods, and algebraic topology rely on averages, error terms, or continuous approximations, they struggle to rule out isolated, exact Diophantine equations at astronomically large scales.

## 6. The Gap

The gap lies between *conditional finiteness* and *absolute non-existence*. Current techniques easily prove that if an odd perfect number exists, it must be exceptionally large, have many prime factors, and adhere to tight structural congruences (Section 4). However, the algorithmic branching factor used to construct these lower bounds grows exponentially with $k$ (the number of distinct prime factors). 

There is currently no theoretical bridge that generalizes finite computational exhaustion to an absolute algebraic or analytic contradiction. We can say "it is not any number up to $10^{1500}$," but we lack the mechanism to say "the intersection of the abundant numbers and the deficient numbers at exactly $\sigma(n)/n = 2$ is empty for the odd integers."

## 7. Current Research (as of June 2026)

Active research primarily branches into three areas:
1. **Algorithmic Exhaustion:** Teams are working to push the lower bounds to $N > 10^{2500}$ and $k \ge 11$ by parallelizing the factor-tree traversal techniques originally developed by Nielsen and Ochem.
2. **Theory of Spoofs:** Studying Descartes numbers and broader classes of "spoof" perfect numbers to isolate the precise arithmetic properties (unique to genuine primes) that prevent the product equation from reaching exactly 2.
3. **Diophantine Connections:** *(frontier — verify)* Recent preprints explore utilizing effective forms of the ABC conjecture and Baker's method on linear forms in logarithms to find absolute upper bounds on $N$ for a given $k$, hoping to squeeze the possible domain of $N$ into an empty set when combined with existing lower bounds.

## 8. Future Work

Leading mathematicians suggest that brute-force computation will never resolve the conjecture. Future breakthroughs are anticipated to come from new, uninvented tools in analytic number theory—perhaps involving the distribution of smooth numbers, or new sieve theories capable of handling exact rational equalities. Alternatively, a complete classification of the solutions to the $\sigma(N) = 2N$ equation over algebraic number fields or polynomial rings could reveal a structural obstruction that maps back to the rational integers.

## 9. Key References

- **[Foundational]** Euler, L. *Tractatus de numerorum doctrina capita sedecim, quae supersunt*. Opera Omnia, Series 1, Vol. 5, 1849.
- **[SOTA / Recent]** Ochem, P. and Rao, M. *Odd perfect numbers are greater than $10^{1500}$*. Mathematics of Computation, Vol. 81, 2012.
- **[SOTA / Recent]** Nielsen, P. P. *Odd perfect numbers have at least 10 distinct prime factors*. Mathematics of Computation, Vol. 84, 2015.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. 3rd Edition, Springer, 2004. (Section B1: Perfect Numbers).

## 10. Worked Example / Concrete Special Case

To ground the abstract requirements of the conjecture, we can walk through a proof of **Euler's condition**—why an odd perfect number *must* take the form $N = p^\alpha m^2$ with $p \equiv 1 \pmod 4$ and $\alpha \equiv 1 \pmod 4$.

Assume $N = q_1^{e_1} q_2^{e_2} \cdots q_k^{e_k}$ is an odd perfect number. 
Since $N$ is perfect, $\sigma(N) = 2N$.
Since $N$ is odd, $2N$ must be *singly even* (divisible by 2, but not by 4).
Because $\sigma(n)$ is multiplicative:
$$ \sigma(N) = \sigma(q_1^{e_1}) \cdot \sigma(q_2^{e_2}) \cdots \sigma(q_k^{e_k}) $$

For this product to be singly even, exactly **one** of the factors $\sigma(q_i^{e_i})$ must be even (and strictly not divisible by 4), and all other factors must be odd.

Consider the formula for a prime power: 
$$ \sigma(q^e) = 1 + q + q^2 + \dots + q^e $$
Because $q$ is odd, each term in the sum is odd. 
- If $e$ is even, there is an odd number of odd terms, making the sum $\sigma(q^e)$ **odd**.
- If $e$ is odd, there is an even number of odd terms, making the sum $\sigma(q^e)$ **even**.

Since exactly one factor in the product is even, exactly one prime factor—let's call it $p = q_1$—must have an odd exponent $\alpha = e_1$. All other prime factors ($q_2, \dots, q_k$) must have even exponents, meaning their product forms a perfect square, $m^2$. 
Thus, $N = p^\alpha m^2$.

Furthermore, $\sigma(p^\alpha)$ must be singly even. 
Since $\alpha$ is odd, we can write $\alpha = 2j + 1$. The sum factors by pairing adjacent terms:
$$ \sigma(p^\alpha) = (1+p) + p^2(1+p) + \dots + p^{2j}(1+p) = (1+p)(1 + p^2 + \dots + p^{2j}) $$

For this product to be divisible by 2 but not 4:
1. $(1+p)$ must be singly even, which means $1+p \equiv 2 \pmod 4 \implies p \equiv 1 \pmod 4$.
2. The second bracket $(1 + p^2 + \dots + p^{2j})$ must be odd. It contains $j+1$ terms, all of which are odd. Therefore, $j+1$ must be odd, which means $j$ is even. 
Since $j$ is even (let $j=2c$), $\alpha = 2(2c) + 1 = 4c + 1$, meaning $\alpha \equiv 1 \pmod 4$.

This elegantly proves Euler's foundational constraint using basic parity and modular arithmetic.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*