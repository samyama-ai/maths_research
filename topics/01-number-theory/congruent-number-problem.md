---
id: 01-number-theory/congruent-number-problem
title: "Congruent Number Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Congruent Number Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/congruent-number-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Congruent Number Problem asks for a general algorithmic method to determine whether a given positive rational number $n$ is a *congruent number*. A positive number $n$ is defined as a congruent number if it is the area of a right-angled triangle with rational side lengths.

Formally, a rational number $n \in \mathbb{Q}_{>0}$ is a congruent number if there exist rational numbers $a, b, c \in \mathbb{Q}_{>0}$ such that:
1. $a^2 + b^2 = c^2$
2. $\frac{1}{2}ab = n$

Without loss of generality, it suffices to consider square-free positive integers $n$, since the area of a rational right triangle multiplied by $s^2$ is simply the area of a scaled rational right triangle. 

The problem remains open in its general algorithmic form. Although Jerrold Tunnell provided a simple arithmetic condition in 1983, proving that this condition is always sufficient depends on the unresolved Birch and Swinnerton-Dyer (BSD) conjecture.

## 2. Mathematical Foundations

The modern approach to the Congruent Number Problem translates the geometric definition into the language of arithmetic geometry and elliptic curves.

Given the geometric equations $a^2 + b^2 = c^2$ and $\frac{1}{2}ab = n$, we can apply the algebraic transformations:
$$ x = \left( \frac{c}{2} \right)^2, \quad y = \frac{(a^2 - b^2)c}{8} $$

This mapping demonstrates that $n$ is a congruent number if and only if there exists a rational point $(x,y)$ with $y \neq 0$ on the elliptic curve $E_n$ given by the Weierstrass equation:
$$ E_n : y^2 = x^3 - n^2 x $$

By the Mordell-Weil theorem, the group of rational points $E_n(\mathbb{Q})$ is finitely generated and takes the form:
$$ E_n(\mathbb{Q}) \cong E_n(\mathbb{Q})_{\text{tors}} \oplus \mathbb{Z}^r $$
where $r \ge 0$ is the algebraic rank of the curve, and $E_n(\mathbb{Q})_{\text{tors}}$ is the torsion subgroup. It is a proven fact that for $E_n$, the torsion points in $E_n(\mathbb{Q})$ are strictly restricted to the 2-torsion points $(0,0), (n, 0), (-n, 0)$ and the point at infinity $\mathcal{O}$. These correspond mathematically to degenerate triangles with side lengths equal to zero or infinity. 

Therefore, a rational point of infinite order must exist for $n$ to be congruent. Equivalently, $n$ is a congruent number if and only if the algebraic rank of $E_n(\mathbb{Q})$ is strictly positive ($r > 0$).

The analytic rank of $E_n$ is the order of vanishing of its Hasse-Weil L-function $L(E_n, s)$ at the central point $s = 1$. The Birch and Swinnerton-Dyer (BSD) conjecture posits that the algebraic rank equals the analytic rank, directly connecting the area of geometric triangles to the complex analysis of L-functions.

## 3. History & State of the Art (SOTA)

The problem boasts a long history, dating back to the Persian mathematician Al-Karaji (10th century) and the Arab mathematician Al-Samawal (12th century). Fibonacci (1225) studied the problem extensively, showing that 5 and 7 are congruent. He famously stated, without rigorous proof, that 1 is not a congruent number. The first valid proof that 1 is not congruent was constructed by Pierre de Fermat in 1659, utilizing his newly developed method of infinite descent.

In 1983, Jerrold Tunnell achieved a monumental breakthrough by connecting the problem to modular forms. Relying on Waldspurger's theorem—which links the central value of an elliptic curve's L-function to the Fourier coefficients of half-integral weight modular forms—Tunnell derived a purely combinatorial and highly efficient condition.

**Tunnell's Theorem:** Let $n$ be a square-free positive integer. Define:
- $f(n) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 2x^2 + y^2 + 8z^2 = n \}$
- $g(n) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 2x^2 + y^2 + 32z^2 = n \}$
- $h(n) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 8x^2 + 2y^2 + 16z^2 = n \}$
- $k(n) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 8x^2 + 2y^2 + 64z^2 = n \}$

If $n$ is odd, and $n$ is congruent, then $f(n) = 2g(n)$.
If $n$ is even, and $n$ is congruent, then $h(n) = 2k(n)$.

Tunnell proved this condition is unconditionally necessary. Crucially, he also proved that if the weak BSD conjecture holds for $E_n$, these conditions are also sufficient, which would fully resolve the Congruent Number Problem.

## 4. Partial Results / Verified Cases

Unconditionally, the following constraints and cases have been rigorously verified:
- Tunnell's criterion is rigorously necessary. If $f(n) \neq 2g(n)$ (for odd $n$) or $h(n) \neq 2k(n)$ (for even $n$), $n$ is absolutely *not* a congruent number.
- Coates and Wiles (1977) proved that if an elliptic curve with complex multiplication (like $E_n$) has $L(E_n, 1) \neq 0$, then $E_n(\mathbb{Q})$ is finite (rank 0). This confirms Tunnell's sufficiency for curves of analytic rank 0.
- Gross and Zagier (1986), together with Kolyvagin (1989), proved that if $L(E_n, 1) = 0$ and $L'(E_n, 1) \neq 0$ (analytic rank 1), the algebraic rank is exactly 1. This confirms Tunnell's sufficiency for curves of analytic rank 1.
- Specific prime classes are fully resolved: For prime numbers $p$, if $p \equiv 3 \pmod 8$, $p$ is not congruent. If $p \equiv 5, 7 \pmod 8$, $p$ is congruent. 
- Ye Tian (2014) proved the existence of infinitely many congruent numbers with any arbitrary number of prime factors.
- Computational searches have verified Tunnell's criterion and the BSD conjecture for $E_n$ for all $n < 10^{12}$.

## 5. Principal Obstacles

The fundamental bottleneck blocking the full resolution of the problem is proving the weak Birch and Swinnerton-Dyer conjecture for elliptic curves of analytic rank $\geq 2$. 

If the central L-value $L(E_n, 1) = 0$ and the derivative $L'(E_n, 1) = 0$, the Heegner point constructed by the Gross-Zagier formula is a torsion point (often the identity). Consequently, Kolyvagin's Euler system machinery—which relies on a non-torsion Heegner point as a base—becomes entirely ineffective.

Currently, mathematics lacks a comprehensive theoretical framework to construct rational points of infinite order on elliptic curves when the analytic rank is strictly greater than 1. Without an unconditional analogue to Heegner points for rank $\geq 2$, or the ability to explicitly bound the Selmer groups in high-rank cases, confirming Tunnell's sufficiency for these specific values of $n$ remains impossible.

## 6. The Gap

The exact boundary between what is mathematically proven (Section 4) and the full resolution of the conjecture is defined by the parity and higher derivatives of the L-function.

We possess unconditional proofs for:
- $L(E_n, 1) \neq 0 \implies \operatorname{rank}(E_n) = 0$
- $L(E_n, 1) = 0, L'(E_n, 1) \neq 0 \implies \operatorname{rank}(E_n) = 1$

The specific mathematical barrier that must be crossed is the higher-rank scenario:
- $L(E_n, 1) = 0, L'(E_n, 1) = 0 \implies \operatorname{rank}(E_n) \ge 2$

Tunnell's combinatorial criteria equate directly to the analytic statement $L(E_n, 1) = 0$. If a square-free integer $n$ satisfies Tunnell's criteria, we know only that its analytic rank is at least 1. If it happens to be 2 or higher, we cannot unconditionally prove that $E_n(\mathbb{Q})$ has positive algebraic rank, leaving the gap open.

## 7. Current Research (as of June 2026)

Research directions are largely partitioned into a few distinct approaches:
1. **Algebraic Number Theory and Selmer Groups:** Techniques pioneered by Bhargava, Smith, and others study the distribution of $2^k$-Selmer groups in families of quadratic twists. Alexander Smith's breakthrough work on Goldfeld's conjecture provided deep insights into the distribution of Selmer groups for curves with full 2-torsion (which $E_n$ possesses).
2. **Analytic Number Theory and Random Matrix Theory:** Understanding the moments of L-functions of elliptic curves in the family $E_n$. Researchers utilize Katz-Sarnak random matrix theory heuristics to predict the asymptotic distributions of the ranks of $E_n$.
3. *(frontier — verify)* **Non-abelian Euler Systems:** Efforts rooted in the $p$-adic Langlands program (e.g., Bertolini, Darmon, Prasanna) attempt to construct "higher Heegner cycles" or generalized Euler systems that do not vanish trivially when the rank is $\ge 2$, offering a potential mechanism to produce points of infinite order.

## 8. Future Work

Open pathways and strategies articulated by experts aiming to resolve the problem:
- **Explicit Point Construction:** The most direct, albeit historically elusive, strategy is developing novel algebraic geometric tools to explicitly construct points of infinite order on curves with $L(E_n, 1) = L'(E_n, 1) = 0$, completely bypassing the need for a general proof of BSD.
- **Bounding the Tate-Shafarevich Group:** Advancing proofs on the finiteness of the Tate-Shafarevich group $\Sha(E_n)$ for ranks $\ge 2$. Understanding the precise mechanics of $\Sha(E_n)$ would bridge the gap between the computable Selmer group bounds and the true Mordell-Weil group rank.
- **Sharpening Selmer Statistics:** Pushing distribution statistics for the 2-part of the class group and Selmer groups in $E_n$ twists to derive exact asymptotic densities, establishing exactly what proportion of integers are congruent.

## 9. Key References

- **[Foundational]** Tunnell, Jerrold B. *A classical Diophantine problem and modular forms of weight 3/2.* Inventiones Mathematicae, 72(2):323–334, 1983. [DOI](https://doi.org/10.1007/bf01389327)
- **[Foundational]** Gross, Benedict H., and Zagier, Don B. *Heegner points and derivatives of L-series.* Inventiones Mathematicae, 84(2):225–320, 1986.
- **[SOTA / Recent]** Smith, Alexander. *The distribution of $\ell^\infty$-Selmer groups in quadratic twist families.* Annals of Mathematics, 2024.
- **[SOTA / Recent]** Tian, Ye. *Congruent numbers with many prime factors.* Proceedings of the National Academy of Sciences, 111(9):3177–3178, 2014.
- **[Survey]** Koblitz, Neal. *Introduction to Elliptic Curves and Modular Forms.* Graduate Texts in Mathematics, Springer, 1993.

## 10. Worked Example / Concrete Special Case

Consider the fundamental problem of determining whether $n = 6$ is a congruent number.

By definition, we seek a right triangle with rational sides $a,b,c$ such that $a^2 + b^2 = c^2$ and $\frac{1}{2}ab = 6$.
We can satisfy this by identifying the standard 3-4-5 right triangle:
- Let $a = 3$, $b = 4$, $c = 5$
- Pythagorean check: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$
- Area check: $\frac{1}{2}(3)(4) = \frac{12}{2} = 6$
Thus, 6 is unconditionally a congruent number.

We can independently verify this using Tunnell's Theorem. Since $n = 6$ is an even integer, we compute $h(6)$ and $k(6)$:
$$ h(6) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 8x^2 + 2y^2 + 16z^2 = 6 \} $$
Because $8x^2 \ge 8$ for any non-zero integer $x$, and $16z^2 \ge 16$ for any non-zero integer $z$, any integer solution must set $x = 0$ and $z = 0$.
Substituting these leaves $2y^2 = 6 \implies y^2 = 3$, which has no integer solutions. Thus, $h(6) = 0$.

Next, compute $k(6)$:
$$ k(6) = \\# \{ (x,y,z) \in \mathbb{Z}^3 \mid 8x^2 + 2y^2 + 64z^2 = 6 \} $$
By identical reasoning, $x=0$ and $z=0$, leaving $2y^2 = 6$, which again yields no integer solutions. Thus, $k(6) = 0$.

Tunnell's necessary condition for an even congruent number dictates that $h(n) = 2k(n)$.
For $n=6$, $0 = 2(0)$, which mathematically holds true.

Furthermore, translating this to the elliptic curve formulation, the associated curve is:
$$ E_6 : y^2 = x^3 - 36x $$
Using our triangle side lengths $(a,b,c) = (3,4,5)$, the transformation equations yield a rational point $(x,y)$ on $E_6$:
$$ x = \left(\frac{5}{2}\right)^2 = \frac{25}{4} $$
$$ y = \frac{(3^2 - 4^2)(5)}{8} = \frac{(9-16)(5)}{8} = -\frac{35}{8} $$
The generated point $(25/4, -35/8)$ on the curve $E_6$ is a point of infinite order, demonstrating computationally that the algebraic rank of $E_6(\mathbb{Q})$ is at least 1, fulfilling the overarching elliptic curve condition.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*