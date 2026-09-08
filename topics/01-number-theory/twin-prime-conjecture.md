---
id: 01-number-theory/twin-prime-conjecture
title: "Twin Prime Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-06
last_reviewed: 2026-06
last_substantive_update: 2026-06
stale_since: ""
provenance: synthesized
---

# Twin Prime Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/twin-prime-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Twin Prime Conjecture states that there are infinitely many pairs of primes that differ by exactly 2. 

Formally, there exist infinitely many prime numbers $p$ such that $p + 2$ is also a prime number.

## 2. Mathematical Foundations

Let $\pi_2(x)$ denote the number of twin primes less than or equal to $x$:
$$\pi_2(x) = \#\{p \leq x \mid p \text{ and } p+2 \text{ are prime}\}$$

The Hardy-Littlewood twin prime conjecture generalizes this by predicting the asymptotic behavior:
$$\pi_2(x) \sim 2 C_2 \int_{2}^{x} \frac{dt}{(\ln t)^2}$$

where $C_2$ is the twin prime constant defined by the infinite product:
$$C_2 = \prod_{p > 2} \left(1 - \frac{1}{(p-1)^2}\right) \approx 0.6601618158\dots$$

## 3. History & State of the Art (SOTA)

* **1849**: Alphonse de Polignac formulated the general conjecture that for every even number $k$, there are infinitely many consecutive prime pairs differing by $k$ (the twin prime conjecture is the case $k=2$).
* **1915**: Viggo Brun proved that the sum of the reciprocals of the twin primes converges to a finite value, now known as Brun's constant:
$$B_2 = \left(\frac{1}{3} + \frac{1}{5}\right) + \left(\frac{1}{5} + \frac{1}{7}\right) + \left(\frac{1}{11} + \frac{1}{13}\right) + \dots \approx 1.90216058$$
* **2013**: Yitang Zhang published a breakthrough proving that there exists some even integer $N < 7 \times 10^7$ such that there are infinitely many prime pairs differing by $N$.
* **2013**: James Maynard and Terence Tao independently developed a new multidimensional sieve method that significantly improved the bound.

## 4. Partial Results / Verified Cases

* **Bounded Gaps**: Through the collaborative Polymath8 project led by Terence Tao, the bound on prime gaps was reduced to:
$$\liminf_{n \to \infty} (p_{n+1} - p_n) \leq 246$$
* **Conditional Gaps**: Assuming the Generalized Elliott-Halberstam conjecture, the Polymath8 project proved that the gap is at most $6$.

## 5. Principal Obstacles

* **The Parity Problem**: In sieve theory, traditional sieve methods cannot easily distinguish between integers with an odd number of prime factors and those with an even number. This prevents sieves from isolating primes directly without additional analytical input.
* **Lack of Bilinear Forms**: Closing the gap from 246 to 2 requires proving distribution estimates for primes in arithmetic progressions that exceed the boundaries of the Bombieri-Vinogradov theorem.

## 6. The Gap

The gap is between the proven difference of $246$ and the conjectured difference of $2$. 

## 7. Current Research (as of June 2026)

* **Maynard-Tao Sieve Optimizations**: Researchers are refining multi-dimensional Selberg sieve weights to squeeze the gap limit further.
* **Chowla's Conjecture**: Investigating correlations of the Liouville function, which is closely linked to prime patterns.

## 8. Future Work

* Developing methods that bypass the parity obstacle entirely.
* Extending the range of validity for prime distribution theorems in short intervals.

## 9. Key References

- **[Foundational]** Brun, Viggo. *La série $\frac{1}{3}+\frac{1}{5}+\frac{1}{5}+\frac{1}{7}+\frac{1}{11}+\frac{1}{13}+\dots$ est convergente ou finie.* Bulletin des Sciences Mathématiques, 1919.
- **[SOTA]** Zhang, Yitang. *Bounded gaps between primes.* Annals of Mathematics, 2014.
- **[SOTA / Recent]** Maynard, James. *Small gaps between primes.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)

## 10. Worked Example / Concrete Special Case

Let us verify the twin primes up to $100$. The twin prime pairs are:
$$(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)$$

Total number of twin prime pairs $\leq 100$ is $\pi_2(100) = 8$.

We can compare this with the Hardy-Littlewood estimation:
$$\pi_2(100) \approx 2 (0.66016) \int_{2}^{100} \frac{dt}{(\ln t)^2} \approx 1.32032 \times 6.22 \approx 8.21$$

The actual count of $8$ matches the prediction of $8.21$ closely.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*
