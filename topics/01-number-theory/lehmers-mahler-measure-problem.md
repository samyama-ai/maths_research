---
id: 01-number-theory/lehmers-mahler-measure-problem
title: "Lehmer's Mahler Measure Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lehmer's Mahler Measure Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/lehmers-mahler-measure-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Mahler measure $M(P)$ of a non-zero polynomial $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0 \in \mathbb{C}[z]$ with roots $\alpha_1, \alpha_2, \dots, \alpha_n$ is defined as:
$$ M(P) = |a_n| \prod_{i=1}^n \max(1, |\alpha_i|) $$

Lehmer's Conjecture (posed in 1933) states that there exists an absolute constant $c > 1$ such that for every non-cyclotomic polynomial $P \in \mathbb{Z}[z]$ with integer coefficients, if $M(P) > 1$, then:
$$ M(P) \ge c $$

Specifically, it is conjectured that the minimum Mahler measure strictly greater than 1 for an integer polynomial is achieved by "Lehmer's polynomial" of degree 10:
$$ L(z) = z^{10} + z^9 - z^7 - z^6 - z^5 - z^4 - z^3 + z + 1 $$
which has a Mahler measure of $M(L) \approx 1.176280818$.

## 2. Mathematical Foundations

The problem lies at the intersection of algebraic number theory, Diophantine approximation, and harmonic analysis. The Mahler measure is linked to the analytic behavior of the polynomial on the unit circle through Jensen's formula:
$$ \log M(P) = \int_0^1 \log \left| P(e^{2\pi i \theta}) \right| \, d\theta $$

By Kronecker's Theorem (1857), an algebraic integer has all its Galois conjugates strictly on the unit circle (or inside it) if and only if it is a root of unity (or zero). Consequently, for a monic integer polynomial, $M(P) = 1$ if and only if $P(z)$ is a product of cyclotomic polynomials and the monomial $z$.

A polynomial $P(z)$ of degree $d$ is called *reciprocal* if $P(z) = \pm z^d P(1/z)$. This property implies that if $\alpha$ is a root, then $1/\alpha$ is also a root, providing a deep symmetry about the unit circle that makes isolating roots difficult.

Two special classes of real algebraic integers are fundamentally connected to this problem:
- **Pisot–Vijayaraghavan (PV) numbers:** Real algebraic integers $>1$ whose remaining conjugates all lie strictly inside the open unit disk. 
- **Salem numbers:** Real algebraic integers $>1$ whose remaining conjugates lie inside the closed unit disk, with at least one strictly on the unit circle boundary. Lehmer's polynomial roots include a Salem number.

## 3. History & State of the Art (SOTA)

The problem was introduced by Derrick Henry Lehmer in 1933 during his search for large primes using generalizations of Lucas sequences. He noticed that the growth rate of the terms in his sequences was dictated by the roots of the corresponding characteristic polynomials, leading him to ask if a polynomial could have a Mahler measure arbitrarily close to 1 without being identically 1. He found the degree-10 polynomial $L(z)$, which remains the smallest known Mahler measure $>1$ to this day.

A major breakthrough occurred in 1979 when E. Dobrowolski established a powerful, general lower bound that relies on the degree $d$ of the polynomial, proving:
$$ M(P) > 1 + c \left( \frac{\log \log d}{\log d} \right)^3 $$
for some absolute constant $c > 0$. While this bound decays to 1 as $d \to \infty$, it represents a massive improvement over trivial bounds.

In the 1980s and 1990s, extensive computational searches by David W. Boyd and Michael J. Mossinghoff verified the conjecture for polynomials up to high degrees (degree $d \le 180$, and later up to $d \le 400$), all confirming that $M(L)$ remains the absolute minimum. 

## 4. Partial Results / Verified Cases

The conjecture has been unequivocally verified for several broad classes of polynomials:
- **Non-reciprocal polynomials:** In 1971, C. J. Smyth proved that if $P(z) \in \mathbb{Z}[z]$ is monic and not reciprocal, then $M(P) \ge \theta_0 \approx 1.324718$, where $\theta_0$ is the real root of $z^3 - z - 1$ (the smallest Pisot number). Thus, Lehmer's conjecture is completely resolved for the non-reciprocal case.
- **Totally real algebraic integers:** Schinzel (1973) proved that if all roots of $P$ are real, then $M(P) \ge \left( \frac{1+\sqrt{5}}{2} \right)^{d/2}$, effectively solving it for totally real fields.
- **Odd-degree polynomials:** It has been proven that any reciprocal polynomial of odd degree must have at least one real root (specifically $1$ or $-1$), which allows bounds to be pushed further than general even-degree reciprocal polynomials.
- **Computational Verification:** Exhaustive searches using modern supercomputers and sophisticated lattice-reduction algorithms (like LLL) have verified Lehmer's conjecture for all integer polynomials up to degree $d = 180$, and for specific sparse families (like trinomials) up to much higher degrees.

## 5. Principal Obstacles

The fundamental bottleneck is the behavior of roots of even-degree reciprocal polynomials. Because of the $P(z) = z^d P(1/z)$ symmetry, roots appear in pairs $(\alpha, 1/\alpha)$. As the degree $d$ increases, it is mathematically possible to distribute these roots uniformly around the unit circle at a microscopic distance $1 \pm \epsilon$, balancing out the contributions inside and outside the unit circle. 

Standard techniques (e.g., using resultants, discriminants, or bounding the trace of $P$) are too coarse. When evaluating the resultant of a polynomial and its derivative (or a related cyclotomic polynomial), the algebraic norm creates a product over all conjugates. Distributing $d$ conjugates extremely close to the unit circle allows the resultant to remain an integer while the product $\prod \max(1, |\alpha_i|)$ scales infinitesimally close to $1$, defeating classical algebraic bounds.

## 6. The Gap

The exact mathematical barrier lies in eliminating the degree dependence in Dobrowolski-type bounds. The current state of the art guarantees a gap of size $\sim (\log \log d / \log d)^3$ which converges to zero as $d \to \infty$. The required gap is a hard, strictly positive absolute constant floor (conjectured to be $\approx 1.17628$). Moving from an asymptotic decay to an absolute non-zero bound for high-degree reciprocal polynomials remains the critical missing step.

## 7. Current Research (as of June 2026)

Current research approaches Lehmer's Problem from a few highly active angles:
- **Connections to Arithmetic Geometry:** Formulating Mahler measures as special values of $L$-functions of elliptic curves and varieties (a direction pioneered by Deninger and Boyd). These conjectures link $M(P)$ to the Bloch group and K-theory.
- **Schinzel-Zassenhaus Techniques:** Following Vesselin Dimitrov's 2019 proof of the related Schinzel-Zassenhaus conjecture (which bounded the maximum modulus of a conjugate, the "house" of an algebraic integer, by $\ge 2^{c/d}$), researchers are attempting to adapt his usage of power series and the Pólya-Carlson theorem to bound the Mahler measure.
- **Multivariate Mahler Measure:** Generalizing the problem to polynomials in multiple variables (e.g., $P(x, y)$) to leverage structural constraints in higher dimensional algebraic tori.

## 8. Future Work

Leading mathematicians suggest that future breakthroughs will require a fundamental departure from single-variable complex analysis and root-bounding. Proposed pathways include:
- Establishing a sharp lower bound on the density of roots of integer polynomials near the unit circle (using advanced equidistribution theorems).
- Extending Dimitrov’s power series method (which currently only bounds the maximum absolute value among roots) to control the *product* of all roots outside the unit circle.
- Proving the conjecture for specific structured families of reciprocal polynomials, such as Littlewood polynomials (where all $a_i \in \{+1, -1\}$).

## 9. Key References

- **[Foundational]** Lehmer, D. H. *Factorization of certain cyclotomic functions.* Annals of Mathematics, 1933.
- **[Foundational]** Smyth, C. J. *On the product of the conjugates outside the unit circle of an algebraic integer.* Bulletin of the London Mathematical Society, 1971.
- **[Foundational]** Dobrowolski, E. *On a theorem of Schinzel and Zassenhaus.* Acta Arithmetica, 1979.
- **[SOTA / Recent]** Dimitrov, V. *A proof of the Schinzel-Zassenhaus conjecture on algebraic integers.* Annals of Mathematics, 2021.
- **[SOTA / Recent]** Mossinghoff, M. J., Rhind, G., and Ryan, C. J. *Computed bounds for the Mahler measure of polynomials.* Mathematics of Computation, (various years / updates).
- **[Survey]** Smyth, C. J. *The Mahler measure of algebraic numbers: a survey.* Number Theory and Polynomials, LMS Lecture Note Series, 2008.

## 10. Worked Example / Concrete Special Case

To clearly ground the definition, we will calculate the Mahler measure for two concrete examples.

**Example 1: A Non-Reciprocal Polynomial**
Let $P(z) = 2z^2 - 5z + 2$.
First, find the roots:
$$ 2z^2 - 5z + 2 = (2z - 1)(z - 2) = 0 $$
The roots are $\alpha_1 = 1/2$ and $\alpha_2 = 2$. The leading coefficient is $a_n = 2$.
Using the formula:
$$ M(P) = |2| \cdot \max(1, |1/2|) \cdot \max(1, |2|) = 2 \cdot 1 \cdot 2 = 4. $$

**Example 2: A Reciprocal Polynomial (Salem Number)**
Consider a simpler reciprocal polynomial that generates a Salem number: $P(z) = z^4 - z^3 - z^2 - z + 1$.
This polynomial is symmetric: $z^4 P(1/z) = P(z)$.
By numerical calculation, the roots are approximately:
- $\alpha_1 \approx 1.72208$ (Real, outside the unit circle)
- $\alpha_2 \approx 0.58066$ (Real, inside the unit circle; exactly $1/\alpha_1$)
- $\alpha_3, \alpha_4 \approx -0.15137 \pm 0.98847 i$ (Complex conjugate pair)

Notice that for the complex pair, $|\alpha_3|^2 = (-0.15137)^2 + (0.98847)^2 = 1.00000$. They lie exactly on the unit circle.
The leading coefficient is $a_4 = 1$.
Calculating the Mahler measure:
$$ M(P) = 1 \cdot \max(1, 1.72208) \cdot \max(1, 0.58066) \cdot \max(1, 1) \cdot \max(1, 1) $$
$$ M(P) = 1 \cdot 1.72208 \cdot 1 \cdot 1 \cdot 1 \approx 1.72208. $$
Because $\alpha_1$ is the only root outside the unit circle, the Mahler measure simplifies exactly to $\alpha_1$, demonstrating why Salem numbers are pivotal in minimizing $M(P)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*