---
id: 01-number-theory/lehmers-totient-problem
title: "Lehmer's Totient Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lehmer's Totient Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/lehmers-totient-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Lehmer's Totient Problem (also known as Lehmer's Conjecture) asks whether there exists any composite integer $n$ such that Euler's totient function $\varphi(n)$ divides $n - 1$. 

More formally, the conjecture states that for all integers $n > 1$:
$$ \varphi(n) \mid (n - 1) \implies n \text{ is prime.} $$

If a composite number $n$ satisfying this condition exists, it is called a *Lehmer number*. The problem remains open, and a complete proof of the conjecture requires demonstrating that no Lehmer numbers can possibly exist. A disproof requires finding at least one composite integer satisfying the condition.

## 2. Mathematical Foundations

The problem is grounded in elementary and analytic number theory, primarily revolving around the properties of Euler's totient function, $\varphi(n)$, which counts the number of positive integers less than or equal to $n$ that are coprime to $n$.

By the fundamental theorem of arithmetic, any integer $n$ can be uniquely factored as $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$. The totient function is multiplicative and is given by:
$$ \varphi(n) = n \prod_{i=1}^k \left( 1 - \frac{1}{p_i} \right) $$

The problem asks for solutions to the Diophantine-like equation:
$$ n - 1 = K \cdot \varphi(n) $$
for some integer $K \ge 2$ (since if $n$ is composite, $\varphi(n) \le n - \sqrt{n}$, forcing $K \ge 2$).

Two foundational theorems severely constrain the structure of any hypothetical Lehmer number:
1. **Square-free condition:** If $n$ is a Lehmer number, $n$ must be square-free. If there exists a prime $p$ such that $p^2 \mid n$, then $p \mid \varphi(n)$. But $\varphi(n) \mid (n - 1)$, which implies $p \mid (n - 1)$. This requires $p$ to divide both $n$ and $n - 1$, which is impossible.
2. **Carmichael property:** Because $n$ is square-free, $n = p_1 p_2 \cdots p_k$. The condition $\varphi(n) \mid (n - 1)$ requires that $(p_i - 1) \mid (n - 1)$ for every prime factor $p_i$. This implies that $n$ must be a Carmichael number (a composite number $n$ such that $a^{n-1} \equiv 1 \pmod n$ for all $a$ coprime to $n$).

## 3. History & State of the Art (SOTA)

The problem was introduced by Derrick Henry Lehmer in 1932 in his paper *On Euler's totient function*. Lehmer himself proved that any counterexample must be odd, square-free, and possess at least seven distinct prime factors.

Over the decades, computational and analytic bounds have been continuously improved. In 1977, Carl Pomerance proved that the number of Lehmer numbers up to $x$, denoted $L(x)$, is bounded by $O(x^{1/2} (\log x)^{3/4})$, establishing that they are exceptionally rare, if they exist at all.

In 1980, G. L. Cohen and P. Hagis Jr. significantly advanced the lower bounds, proving computationally that any Lehmer number must have at least $14$ distinct prime factors. They further demonstrated the astonishing result that if $3 \mid n$, the number must have at least $298,848$ prime factors. 

Currently, large-scale distributed computing efforts and improved sieve methods have established that any Lehmer number must have at least $15$ prime factors and be larger than $10^{30}$.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, the non-existence of Lehmer numbers has been rigidly verified under several conditions:

- **Parity:** No even Lehmer numbers exist.
- **Divisibility by 3:** No Lehmer number exists with fewer than $298,848$ prime factors if it is divisible by $3$.
- **Number of Prime Factors $\omega(n)$:** It is unconditionally proven that no Lehmer number exists with $\omega(n) \le 14$. 
- **The $K$-value:** The multiplier $K = \frac{n-1}{\varphi(n)}$ cannot be even, nor can $K=3$. Furthermore, $K$ is bounded; for instance, if $\omega(n) = 15$, $K$ cannot exceed certain strictly constrained limits.
- **Specific Structural Forms:** No Lehmer numbers exist in the sequence of Fibonacci numbers, nor can any be formed as the product of specific highly structured prime families (like Mersenne or Fermat primes alone).

## 5. Principal Obstacles

The primary bottleneck in solving Lehmer's problem is the mathematical difficulty of resolving mixed multiplicative-additive equations over the primes. The equation:
$$ \prod_{i=1}^k p_i - 1 = K \prod_{i=1}^k (p_i - 1) $$
requires deep coordination between the product of a set of primes and the product of their shifts. 

Standard analytic number theory tools (like the Hardy-Littlewood circle method or sieve methods) are highly effective at providing statistical bounds and density theorems (as Pomerance demonstrated), but they are inherently ill-equipped to prove the absolute non-existence of solutions in sparse sets.

Algebraic geometry is similarly stymied because the condition $(p_i - 1) \mid (n - 1)$ does not translate well into the language of varieties over finite fields or characteristic zero spaces without losing the arithmetic rigidity of the integers. Consequently, mathematicians are forced to rely on elementary bounding arguments and computational exhaustion, which cannot cover the infinite space of potential solutions.

## 6. The Gap

The gap lies between asymptotic density bounds and absolute exclusion. We currently know that Lehmer numbers are incredibly rare, behaving locally like Carmichael numbers but subject to far more restrictive constraints. The exact mathematical barrier is finding an invariant or a contradiction in the $p$-adic valuation of $n-1$ versus $\varphi(n)$ for arbitrarily large configurations of primes. Until we can algebraically prove that the defect $K \cdot \varphi(n) - n + 1$ can never identically vanish for $k \ge 15$, the conjecture will remain open.

## 7. Current Research (as of June 2026)

Active research primarily flows through two channels:
1. **Analytic Bounds:** Researchers at institutions like Dartmouth and the University of Georgia continue to refine the upper bounds on the counting function $L(x)$, attempting to push the exponent below $1/2$ to show that $L(x) = O(x^\epsilon)$ for arbitrarily small $\epsilon$.
2. **Computational Combinatorics:** Massive integer programming (IP) techniques and boolean satisfiability (SAT) solvers are being employed to extend the Cohen-Hagis bounds. Current grid-computing initiatives aim to push the unconditional lower bound of $\omega(n)$ from 14 to 20. 
3. *Recent Preprints:* Several recent approaches attempt to bind Lehmer's problem to the structural graph of Carmichael numbers, arguing that the cycle structure of the Carmichael function $\lambda(n)$ precludes the existence of $K > 1$. *(frontier — verify)*

## 8. Future Work

Leading mathematicians suggest the following pathways for future breakthroughs:
- **Refining the $K$-Index:** Proving unconditionally that specific small odd values of $K$ (e.g., $K=5, 7$) are impossible for any number of prime factors.
- **Connection to the $abc$ Conjecture:** Exploring whether assuming the $abc$ conjecture or its variants can provide a conditional proof of Lehmer's problem by restricting the additive shift between the highly factored $\varphi(n)$ and $n-1$.
- **Cyclotomic Polynomial Constraints:** Utilizing the properties of cyclotomic polynomials $\Phi_d(n)$ to show that the simultaneous prime divisibility required by Lehmer numbers forces a contradiction in cyclotomic fields.

## 9. Key References

- **[Foundational]** D. H. Lehmer. *On Euler's totient function.* Bulletin of the American Mathematical Society, 38 (1932): 745-751.
- **[Foundational]** C. Pomerance. *On composite $n$ for which $\phi(n) \mid n-1$, II.* Pacific Journal of Mathematics, 69 (1977): 177-186.
- **[SOTA / Recent]** G. L. Cohen and P. Hagis Jr. *On the number of prime factors of $n$ if $\phi(n)$ divides $n-1$.* Nieuw Archief voor Wiskunde, 28 (1980): 177-185.
- **[SOTA / Recent]** F. Luca and C. Pomerance. *On composite integers $n$ for which $\varphi(n) \mid n-1$.* Revista Matemática Iberoamericana, 23 (2007): 273-288.
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory.* Springer, 3rd Edition, 2004 (Section B37).

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, we can manually prove that no composite number with exactly $k = 2$ prime factors can be a Lehmer number.

Let $n = p \cdot q$, where $p$ and $q$ are distinct primes with $p < q$.
Because $n$ is a Lehmer number, we require:
$$ \varphi(n) \mid (n - 1) $$

Substitute the formulas for $n$ and $\varphi(n)$:
$$ \varphi(n) = (p - 1)(q - 1) $$
$$ n - 1 = pq - 1 $$

We can rewrite $n - 1$ algebraically in terms of $\varphi(n)$:
$$ pq - 1 = (p - 1)(q - 1) + p + q - 2 $$

For $(p - 1)(q - 1)$ to divide $pq - 1$, it must also divide the remainder $p + q - 2$. Therefore, we must have:
$$ (p - 1)(q - 1) \le p + q - 2 $$
*(assuming $p + q - 2 > 0$, which is true since $p \ge 2, q \ge 3$)*

However, since $p < q$, the smallest possible prime for $p$ is $2$.
If $p = 2$:
$$ (2 - 1)(q - 1) = q - 1 $$
And we require $(q - 1)$ to divide $(2 + q - 2) = q$. The only way $q - 1$ divides $q$ is if $q - 1 = 1$, yielding $q = 2$. But we assumed $p < q$, which contradicts $p=2, q=2$.

If $p \ge 3$:
$$ (p - 1)(q - 1) \ge 2(q - 1) = 2q - 2 $$
Since $p < q$, we have:
$$ p + q - 2 < q + q - 2 = 2q - 2 $$
Thus, $(p - 1)(q - 1) > p + q - 2$. 

A larger number cannot divide a strictly smaller positive number. Thus, we have reached a contradiction. This concrete proof demonstrates why a Lehmer number, if it exists, is forced to have a massive number of prime factors to overcome this geometric growth disparity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*