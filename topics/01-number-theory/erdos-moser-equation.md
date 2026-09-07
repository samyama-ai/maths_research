---
id: 01-number-theory/erdos-moser-equation
title: "Erdos-Moser Equation"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Moser Equation

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-moser-equation` · **Status:** open

## 1. Problem Statement / Conjecture

The Erdős-Moser equation is the Diophantine equation given by:

$$ 1^k + 2^k + \dots + (m-1)^k = m^k $$

where $m$ and $k$ are strictly positive integers. The Erdős-Moser conjecture states that the only integer solution to this equation is the trivial case where $m=3$ and $k=1$ (yielding $1^1 + 2^1 = 3^1$). Specifically, for any integer $k \ge 2$, it is conjectured that there are no integer solutions for $m$. 

A complete proof of the conjecture requires unconditionally demonstrating that no other pairs $(m, k)$ can satisfy the equality. Conversely, a disproof would require explicitly finding, or mathematically proving the existence of, a second pair of integers satisfying the equation.

## 2. Mathematical Foundations

The problem fundamentally explores the asymptotic behavior of sums of integer powers. Let $S_k(n)$ denote the sum of the first $n$ positive $k$-th powers:

$$ S_k(n) = \sum_{i=1}^n i^k $$

The equation can be rewritten as $S_k(m-1) = m^k$. By Faulhaber's formula, the sum of powers can be expressed analytically using the Bernoulli numbers $B_j$:

$$ S_k(n) = \frac{1}{k+1} \sum_{j=0}^k \binom{k+1}{j} B_j n^{k+1-j} $$

where the sequence of Bernoulli numbers begins $B_0 = 1, B_1 = -\frac{1}{2}, B_2 = \frac{1}{6}$, etc. 

The structure of the equation inextricably links it to the prime factorization of $m-1, m,$ and $m+1$, as well as the denominators of the Bernoulli numbers governed by the von Staudt-Clausen theorem. Analytically, if $m$ and $k$ are large, the equation forces a rigid approximation constraint. Specifically, it can be shown that the fraction $\frac{2^k}{2m-3}$ must be an exceptionally close rational approximation (a convergent) of $\log 2$, embedding the problem deep into the theory of Diophantine approximations and continued fractions.

## 3. History & State of the Art (SOTA)

The problem was posed around 1953 by Paul Erdős and Leo Moser. Moser made the first major breakthrough in the same year by proving that if any non-trivial solution exists, $k$ must be even and $m$ must be staggeringly large: specifically, $m > 10^{10^6}$. 

For decades, advancements were made by computational refinements of Moser's modular arithmetic approach. In 1999, Butske, Jaje, and Mayernik improved Moser's lower bound to $m > 1.485 \times 10^{9,321,155}$.

The current State of the Art was established in 2011 by Yves Gallot, Pieter Moree, and Wadim Zudilin. They pivoted away from purely modular arithmetic bounds and instead utilized the continued fraction expansion of $\log 2$. By computing the convergents of $\log 2$ to extreme precision, they definitively raised the lower bound to $m > 10^{10^9}$.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, several powerful constraints and specific cases have been verified:

- **The Trivial Solution:** The case $m=3, k=1$ is analytically and computationally verified as the sole known solution.
- **Parity Constraints:** Moser proved that for any non-trivial solution $(m,k)$, the power $k$ must be an even integer.
- **Congruence Constraints:** Any solution $m$ must satisfy strict congruences, including $m \equiv 3 \pmod 4$ or $m \equiv 1 \pmod 4$, with specific prime divisor restrictions. Furthermore, $k$ must be a multiple of the least common multiple of all primes up to a massive bound.
- **Computational Verification:** There are unconditionally no solutions in the range $m \le 10^{10^9}$, ruling out any small or mid-scale counterexamples.

## 5. Principal Obstacles

The primary obstacle preventing the resolution of the Erdős-Moser equation is the sheer magnitude of the established lower bounds. Moser's foundational method translates the existence of a solution into a system of congruences modulo prime numbers, establishing that any hypothetical $m$ must be divisible by an astronomically large number of primes. This pushes the minimum possible size of $m$ into a regime where standard computations fail.

However, this method is purely additive and modular; it continually pushes the lower bound higher without producing a theoretical, absolute upper limit. Standard analytic number theory tools fail because the size of $m$ lies far beyond regions where properties of primes, or error terms in Bernoulli number estimates, can be controlled effectively. 

Furthermore, the Gallot-Moree-Zudilin Diophantine approximation method requires knowing the exact partial quotients of the irrational number $\log 2$. Because the continued fraction digits of $\log 2$ lack a known periodic or predictable algebraic pattern, they can only be computed to finite depths. It is therefore impossible to categorically rule out the existence of some incredibly distant convergent satisfying the equation via computation alone.

## 6. The Gap

The central mathematical gap lies between a computationally established lower bound ($m > 10^{10^9}$) and the requirement for an absolute, unconditional upper bound. To resolve the conjecture, one must bridge the methodology of lower bounds—derived from prime factor congruences and numerical convergents—with a structural theorem that strictly limits the maximum possible size of $m$. A theoretical constraint is required to prove that the stringent divisibility and congruence requirements for $m$ inherently contradict the irrationality measure of $\log 2$ at infinity.

## 7. Current Research (as of June 2026)

Active research on the Erdős-Moser conjecture follows two primary trajectories:

1. **High-Precision Diophantine Approximation:** Computational number theorists continue to push the limits of calculating the continued fraction convergents of $\log 2$, seeking to raise the lower bound of $m$ further using the Gallot-Moree-Zudilin framework.
2. **Generalized Equations:** Researchers study generalized forms of the equation, such as $1^k + 2^k + \dots + (m-1)^k = a m^k$, hoping that proving structural invariants in generalized cases will collapse back onto the original equation. 

Additionally, connections between the Erdős-Moser equation and the ABC conjecture represent an active theoretical frontier `*(frontier — verify)*`. Strong effective forms of the ABC conjecture are theorized to provide the necessary upper bound for $m$, which would instantly close the gap and resolve the problem.

## 8. Future Work

Leading mathematicians suggest that fully resolving the conjecture without relying on unproven general axioms (like ABC) will require a fundamental breakthrough in $p$-adic analysis regarding sums of powers. Open pathways include:
- Establishing a novel irrationality measure for $\log 2$ that fundamentally restricts the properties of its convergents in a way that is mathematically incompatible with the modular constraints of the Erdős-Moser equation.
- Deepening the understanding of the distribution of prime numbers that divide the denominators of Bernoulli numbers in relation to specific polynomial sequences.

## 9. Key References

- **[Foundational]** Moser, L. *On the diophantine equation $1^n + 2^n + \cdots + (m-1)^n = m^n$*. Scripta Mathematica, 19, 1953.
- **[Foundational]** Butske, W., Jaje, L. M., & Mayernik, D. R. *On the equation $\sum_{p|N} \frac{1}{p} + \frac{1}{N} = 1$, pseudoperfect numbers, and perfectly weighted graphs*. Mathematics of Computation, 68(226), 1999.
- **[SOTA / Recent]** Gallot, Y., Moree, P., & Zudilin, W. *The Erdős–Moser Equation $1^k + 2^k + \dots + (m-1)^k = m^k$ Revisited using Continued Fractions*. Mathematics of Computation, 80(274), 2011.

## 10. Worked Example / Concrete Special Case

To intuitively understand why trivial algebraic solutions fail rapidly for $k \ge 2$, consider the concrete special case where $k=2$. The equation asks for integer solutions to:

$$ 1^2 + 2^2 + \dots + (m-1)^2 = m^2 $$

Using the standard, verified formula for the sum of squares, we substitute the left side:

$$ \frac{(m-1)m(2m-1)}{6} = m^2 $$

Since any valid solution requires a positive integer $m \ge 1$, $m$ cannot be zero. We can safely divide both sides by $m$:

$$ \frac{(m-1)(2m-1)}{6} = m $$

Expanding the numerator and multiplying by 6 yields:

$$ 2m^2 - 3m + 1 = 6m $$

By bringing all terms to one side, we form a standard quadratic equation:

$$ 2m^2 - 9m + 1 = 0 $$

To find the solutions for $m$, we apply the quadratic formula:

$$ m = \frac{-(-9) \pm \sqrt{(-9)^2 - 4(2)(1)}}{2(2)} = \frac{9 \pm \sqrt{81 - 8}}{4} = \frac{9 \pm \sqrt{73}}{4} $$

Because $73$ is not a perfect square, $\sqrt{73}$ is irrational. Therefore, there is no integer solution for $m$ when $k=2$. 

This demonstrates how, for small specific values of $k$, basic algebraic manipulations force $m$ into irrationality, effortlessly disproving the existence of a solution. The Erdős-Moser conjecture asserts that this fundamental algebraic failure persists universally for all $k \ge 2$, no matter how large the numbers become.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*