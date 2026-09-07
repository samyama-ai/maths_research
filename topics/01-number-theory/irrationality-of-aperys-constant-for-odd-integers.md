---
id: 01-number-theory/irrationality-of-aperys-constant-for-odd-integers
title: "Irrationality of Apery's Constant for Odd Integers"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Irrationality of Apery's Constant for Odd Integers

> **Topic:** Number Theory · **ID:** `01-number-theory/irrationality-of-aperys-constant-for-odd-integers` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The problem concerns the arithmetic nature of the values of the Riemann zeta function $\zeta(s)$ at odd integers $s = 2k+1$ for integers $k \geq 1$.
Specifically, Apéry's constant is defined as $\zeta(3) = \sum_{n=1}^\infty \frac{1}{n^3}$, which was proven to be irrational by Roger Apéry in 1978. The overarching conjecture, often loosely referred to under the umbrella of "Apéry's constant for odd integers", posits that:

**Conjecture (Irrationality):** For all integers $k \geq 1$, the value $\zeta(2k+1)$ is irrational.

**Strong Conjecture (Algebraic Independence):** The numbers $\pi, \zeta(3), \zeta(5), \zeta(7), \dots$ are algebraically independent over the field of rational numbers $\mathbb{Q}$.

A complete proof of the weak conjecture would demonstrate that there are no integers $p, q$ such that $\zeta(2k+1) = p/q$ for any $k \geq 1$. Currently, while it is known that infinitely many odd zeta values are irrational, we cannot pinpoint any single specific odd zeta value beyond $\zeta(3)$ that is strictly irrational.

## 2. Mathematical Foundations

The primary mathematical object is the **Riemann zeta function**, defined for complex numbers $s$ with real part $\Re(s) > 1$ by the absolutely convergent Dirichlet series:
$$ \zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} $$
For even integers, Leonhard Euler proved the exact formula:
$$ \zeta(2k) = (-1)^{k+1} \frac{B_{2k} (2\pi)^{2k}}{2(2k)!} $$
where $B_{2k}$ are the rational Bernoulli numbers. Because $\pi$ is a transcendental number (proven by von Lindemann in 1882), it immediately follows that $\zeta(2k)$ is transcendental, and hence irrational, for all $k \geq 1$.

However, for odd integers $s = 2k+1$, no such closed-form relationship with powers of $\pi$ or any other known transcendental constants exists. The arithmetic nature of $\zeta(2k+1)$ is studied by evaluating specific combinations of **Multiple Zeta Values (MZVs)** or through Padé approximations of hypergeometric series. 

A number $\alpha \in \mathbb{R}$ is irrational if and only if there exists an infinite sequence of rational approximations $p_n / q_n$ such that:
$$ 0 < \left| \alpha - \frac{p_n}{q_n} \right| < \frac{\epsilon}{q_n} $$
for appropriate error bounds $\epsilon$, typically achieved when $p_n, q_n$ are solutions to higher-order linear recurrences with polynomial coefficients (the so-called Apéry-like sequences).

## 3. History & State of the Art (SOTA)

- **1734:** Euler evaluates $\zeta(2) = \pi^2/6$ (the Basel problem) and eventually finds the general formula for $\zeta(2k)$, proving their irrationality conditional on the irrationality of $\pi^2$.
- **1978:** Roger Apéry shocks the mathematical community by presenting a proof that $\zeta(3)$ is irrational. His proof used a highly unexpected second-order linear recurrence relation.
- **1979:** Frits Beukers elegantly re-framed Apéry's proof using multiple integrals of shifted Legendre polynomials, making the underlying structure slightly less mysterious.
- **2000:** Tanguy Rivoal achieved a massive breakthrough by proving that infinitely many values of $\zeta(2k+1)$ are irrational. Specifically, he showed that the dimension of the $\mathbb{Q}$-vector space spanned by $\{1, \zeta(3), \zeta(5), \dots, \zeta(2a+1)\}$ grows at least logarithmically with $a$.
- **2001:** Wadim Zudilin tightened Rivoal's bounds, proving a famous specific result: at least one of the four numbers $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ must be irrational.
- **2018:** Stéphane Fischler and Wadim Zudilin proved further asymptotic properties of the sequence of odd zeta values, bounding the density of irrational values.

## 4. Partial Results / Verified Cases

To date, the exact status of the problem holds the following verified bounds and solved cases:
- $\zeta(3) \notin \mathbb{Q}$ (Apéry, 1978).
- Let $V_a = \text{span}_{\mathbb{Q}} \{1, \zeta(3), \zeta(5), \dots, \zeta(2a+1)\}$. Then $\dim_{\mathbb{Q}}(V_a) \geq \frac{1}{3} \log(a)$ for sufficiently large $a$ (Rivoal, 2000).
- At least one element of the set $\{\zeta(5), \zeta(7), \zeta(9), \zeta(11)\}$ is irrational (Zudilin, 2001).
- At least two elements of the set $\{\zeta(5), \zeta(7), \dots, \zeta(69)\}$ are irrational.
- For any large $a$, the number of irrational odd zeta values in the interval $[3, a]$ is bounded below by $C \log a$ for some absolute constant $C > 0$.

## 5. Principal Obstacles

The main bottleneck lies in the rigidity of **hypergeometric series constructions**. Apéry's proof required the existence of a sequence of integers $a_n, b_n$ growing at a specific exponential rate such that $a_n \zeta(3) - b_n$ approaches $0$ extremely quickly. This requires finding rational approximations that converge faster than the denominators grow.

Current analytic techniques rely on well-poised hypergeometric series evaluated at $z=1$ (or multiple integrals over the unit hypercube). When attempting to isolate a *single* odd zeta value like $\zeta(5)$, the hypergeometric sums naturally involve linear combinations of *several* odd zeta values (e.g., $c_0 + c_1 \zeta(3) + c_2 \zeta(5)$). We lack the analytical "filters" to cancel out all but one specific zeta value while maintaining the strict arithmetic properties (such as common denominators growing sufficiently slowly) needed to prove irrationality.

## 6. The Gap

The boundary between Section 4 and Section 1 is precisely transitioning from **existential irrationality** to **specific irrationality**. 
We possess structural proofs that the vector space of odd zeta values has infinite dimension over $\mathbb{Q}$. However, taking any single specific integer $k \geq 2$, we have absolutely no method to decide if $\zeta(2k+1)$ is irrational. The exact gap is constructing a linear form $L_n = q_n \zeta(5) - p_n$ such that $L_n \to 0$ rapidly enough without inadvertently pulling $\zeta(7)$ or $\zeta(9)$ into the coefficient matrix.

## 7. Current Research (as of June 2026)

Research continues heavily within the framework of **Motivic periods** and the theory of Multiple Zeta Values (MZVs). 
- **Periods of Mixed Tate Motives:** Following Francis Brown's work proving Hoffman's conjecture (every MZV is a $\mathbb{Q}$-linear combination of MZVs with elements in $\{2,3\}$), researchers are attempting to derive algebraic independence bounds.
- **Saddle-Point Method Refinements:** Teams are analyzing new multidimensional contour integrals to find better bounds for Zudilin's sets, attempting to reduce the set $\{\zeta(5), \zeta(7), \zeta(9), \zeta(11)\}$ down to three or two elements. 
- *(frontier — verify)* The construction of generalized modular forms and Apéry-like limits on Calabi-Yau manifolds of higher dimension to isolate $\zeta(5)$.

## 8. Future Work

Leading number theorists propose several specific paths:
1. **Denominator elimination:** Finding new transformations for hypergeometric series where the arithmetic primes dividing the denominators cancel out more efficiently than bounded by the Prime Number Theorem, allowing the survival of only $\zeta(5)$.
2. **$q$-analogues:** Investigating $q$-analogues of Apéry numbers and odd zeta values (e.g., Jackson $q$-Bessel functions) where structural algebraic independence might be easier to prove, then pushing the limit as $q \to 1$.
3. **Calabi-Yau Differential Equations:** Generalizing the Picard-Fuchs equations that produce the Apéry numbers to higher dimensions to systematically discover Apéry-like sequences for higher odd zeta values.

## 9. Key References

- **[Foundational]** Apéry, R. *Irrationalité de $\zeta(2)$ et $\zeta(3)$.* Astérisque, 1979.
- **[Foundational]** Beukers, F. *A note on the irrationality of $\zeta(2)$ and $\zeta(3)$.* Bulletin of the London Mathematical Society, 1979.
- **[SOTA / Recent]** Rivoal, T. *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs.* Comptes Rendus de l'Académie des Sciences - Series I - Mathematics, 2000.
- **[SOTA / Recent]** Zudilin, W. *One of the numbers $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ is irrational.* Russian Mathematical Surveys, 2001.
- **[Survey]** Fischler, S. *Irrationalité de valeurs de zêta (d'après Apéry, Rivoal, ...).* Séminaire Bourbaki, 2002.

## 10. Worked Example / Concrete Special Case

To understand the mechanics of Apéry's proof for the irrationality of $\zeta(3)$, consider the construction of rational approximations using the famous Apéry sequence.

Define the sequence of integers $A_n$ (the Apéry numbers) by:
$$ A_n = \sum_{k=0}^n \binom{n}{k}^2 \binom{n+k}{k}^2 $$
The first few values are $1, 5, 73, 1445, 33001$.
Apéry miraculously discovered that $A_n$ satisfies the second-order linear recurrence:
$$ (n+1)^3 A_{n+1} - (34n^3 + 51n^2 + 27n + 5)A_n + n^3 A_{n-1} = 0 $$
By taking a companion sequence $B_n$ satisfying the exact same recurrence, but with initial values $B_0 = 0$ and $B_1 = 6$, one can form the rational numbers $p_n/q_n = B_n / A_n$.

By analyzing the recurrence, Apéry showed that $B_n / A_n$ converges to $\zeta(3)$ at an exponential rate. Specifically, the error term behaves as:
$$ \left| \zeta(3) - \frac{B_n}{A_n} \right| = \mathcal{O}\left( (\sqrt{2}-1)^{4n} \right) $$
Because $A_n$ grows at the rate of $(\sqrt{2}+1)^{4n}$, and observing that the denominators of $B_n$ involve the least common multiple of integers up to $n$ cubed (i.e., $\text{lcm}(1, 2, \dots, n)^3 \approx e^{3n}$), the total approximation error shrinks faster than the algebraic complexity of the denominator grows. 
Since $(\sqrt{2}-1)^4 e^3 \approx 0.0294 \times 20.08 < 1$, the approximations are too accurate for $\zeta(3)$ to be rational, thus proving $\zeta(3) \notin \mathbb{Q}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*