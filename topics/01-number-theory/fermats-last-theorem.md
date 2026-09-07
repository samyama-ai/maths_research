---
id: 01-number-theory/fermats-last-theorem
title: "Fermat's Last Theorem"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fermat's Last Theorem

> **Topic:** Number Theory · **ID:** `01-number-theory/fermats-last-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Fermat's Last Theorem (FLT) states that there are no three positive integers $x$, $y$, and $z$ that satisfy the Diophantine equation:
$$x^n + y^n = z^n$$
for any integer value of $n > 2$. 

A complete proof requires showing the non-existence of non-trivial integer solutions for all integer exponents $n \ge 3$. Since any integer $n > 2$ is divisible by either $4$ or an odd prime $p$, it is mathematically sufficient to prove the theorem for $n = 4$ and all odd prime exponents $n = p$.

## 2. Mathematical Foundations

The modern resolution of Fermat's Last Theorem relies on deep connections between algebraic number theory, algebraic geometry, and complex analysis. The foundations involve the properties of elliptic curves and modular forms.

- **Elliptic Curves:** An elliptic curve $E$ over the rationals $\mathbb{Q}$ can be written in Weierstrass form as:
  $$y^2 = x^3 + Ax + B$$
  where $A, B \in \mathbb{Q}$ and the discriminant $\Delta = -16(4A^3 + 27B^2) \neq 0$.
- **Modular Forms:** A modular form of weight $k$ for the congruence subgroup $\Gamma_0(N)$ is a holomorphic function $f$ on the upper half-plane $\mathbb{H} = \{ \tau \in \mathbb{C} \mid \Im(\tau) > 0 \}$ satisfying certain functional equations and growth conditions, with a Fourier expansion $f(\tau) = \sum_{n=1}^\infty a_n q^n$ where $q = e^{2\pi i \tau}$.
- **Galois Representations:** To both an elliptic curve $E/\mathbb{Q}$ and a cuspidal eigenform $f$, one can associate two-dimensional representations of the absolute Galois group $G_\mathbb{Q} = \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$:
  $$\rho_{E, p} : G_\mathbb{Q} \to \operatorname{GL}_2(\mathbb{F}_p)$$
- **The Frey Curve:** If a hypothetical non-trivial solution $(a, b, c)$ exists for an odd prime $p \ge 5$ such that $a^p + b^p = c^p$, one can construct the Frey curve $E_{a,b,c}$:
  $$y^2 = x(x - a^p)(x + b^p)$$
  This is a semistable elliptic curve with a highly unusual discriminant $\Delta = 16(abc)^{2p}$, leading to a Galois representation that is wildly ramified at $2$ and unramified outside of $2$ and the primes dividing $abc$.

## 3. History & State of the Art (SOTA)

- **1637:** Pierre de Fermat originally formulated the theorem in the margin of a copy of Diophantus's *Arithmetica*, claiming to have a "truly marvelous demonstration" which the margin was too narrow to contain.
- **18th - 19th Century:** Special cases were solved by mathematicians including Euler, Legendre, Dirichlet, and Lamé.
- **1847:** Ernst Kummer introduced "ideal numbers" (the genesis of ideal theory in rings) and proved the theorem for all regular primes.
- **1984:** Gerhard Frey conjectured that the Frey curve constructed from a hypothetical solution to Fermat's equation would be so unusual that it could not be modular.
- **1986:** Ken Ribet proved the "epsilon conjecture" (Ribet's Theorem), rigorously demonstrating that the Frey curve cannot be modular. This reduced FLT to proving the Modularity Theorem for semistable elliptic curves.
- **1994:** Andrew Wiles, with the assistance of Richard Taylor to fix a gap in the original 1993 announcement, successfully proved the Modularity Theorem for semistable elliptic curves, thus proving Fermat's Last Theorem. The proof was published in 1995.
- **2001:** Christophe Breuil, Brian Conrad, Fred Diamond, and Richard Taylor extended Wiles's methods to prove the full Modularity Theorem for all elliptic curves over $\mathbb{Q}$.

## 4. Partial Results / Verified Cases

Before Wiles's full proof in 1994, the theorem was proven for several specific cases and ranges:
- **$n=4$:** Proven by Fermat himself using the method of infinite descent.
- **$n=3$:** Proven by Leonhard Euler in 1770 using integers of the form $a + b\sqrt{-3}$ (with a gap later fixed by Legendre).
- **$n=5$ and $n=7$:** Proven by Dirichlet and Legendre (1825), and Gabriel Lamé (1839).
- **Regular Primes:** Ernst Kummer (1847) proved FLT for all regular primes $p$, which are primes that do not divide the class number of the $p$-th cyclotomic field $\mathbb{Q}(\zeta_p)$.
- **Computational Verification:** By 1993, using modern computing, the theorem had been verified for all prime exponents up to $n = 4,000,000$.

## 5. Principal Obstacles

The historical obstacle to solving Fermat's Last Theorem for arbitrary exponent $n$ was the failure of unique prime factorization in the ring of integers of cyclotomic fields $\mathbb{Z}[\zeta_p]$ for $p \ge 23$. The classical algebraic approach involves factoring $x^p + y^p = (x+y)(x+\zeta_p y)\cdots(x+\zeta_p^{p-1}y) = z^p$. If unique factorization held, each factor would essentially be a $p$-th power, leading to a contradiction via infinite descent. Because unique factorization fails, traditional algebraic manipulation collapses.

In the late 20th century, the obstacle shifted to proving the Taniyama-Shimura-Weil conjecture (the Modularity Theorem). The difficulty lay in bridging two completely different domains of mathematics: the algebraic geometry of elliptic curves over finite fields, and the complex analytic world of modular forms. The key bottleneck was finding a way to successfully "lift" a residual modular Galois representation $\overline{\rho}_{E,3}$ modulo $3$ to a characteristic zero representation $\rho_{E,3}$ without destroying the modularity, a technical barrier uniquely overcome by Wiles's deformation theory of Galois representations and the introduction of Taylor-Wiles systems.

## 6. The Gap

Because the theorem was fully resolved by Andrew Wiles in 1994, there is no remaining gap for the classical statement of Fermat's Last Theorem. 

However, looking at the generalized framework, the "gap" now exists in extending these modularity lifting techniques to higher-dimensional varieties (Shimura varieties) and establishing the Langlands Program. There is also a gap between Wiles's heavily machinery-dependent proof and the search for an elementary proof, though most mathematicians strongly suspect that an elementary proof using only the mathematics available in Fermat's time is impossible.

## 7. Current Research (as of June 2026)

Current research downstream of Fermat's Last Theorem is centered on broad generalisations and formal verifications:
- **Formal Verification:** A massive collaborative effort within the interactive theorem proving community is underway to fully formalize Wiles's proof in Lean 4. The project, spearheaded by Kevin Buzzard and the Lean math community, aims to establish absolute machine-checked certainty of the intricate commutative algebra and Galois cohomology required. *(frontier — verify)*
- **Fermat-Catalan Conjecture:** Research continues on the generalized Fermat equation $x^p + y^q = z^r$. Solutions are classified based on the value of $\frac{1}{p} + \frac{1}{q} + \frac{1}{r}$. The hyperbolic case (where the sum is $< 1$) is conjectured to have only finitely many coprime integer solutions.
- **The ABC Conjecture:** Proving the ABC conjecture would yield a nearly immediate proof of Fermat's Last Theorem for sufficiently large $n$, establishing uniform asymptotic bounds for Diophantine equations.

## 8. Future Work

Leading number theorists emphasize the following pathways originating from the resolution of FLT:
- Completing the full formalization of the Taylor-Wiles methods and subsequent generalizations by Kisin and others into proof assistants.
- Generalizing the Serre Modularity Conjecture and modularity lifting theorems to representations of Galois groups over arbitrary totally real or CM number fields.
- Developing new techniques to bound Selmer groups in Iwasawa theory to tackle unresolved cases of the generalized Fermat-Catalan equations.

## 9. Key References

- **[Foundational]** Wiles, A. *Modular elliptic curves and Fermat's Last Theorem.* Annals of Mathematics, 1995.
- **[Foundational]** Taylor, R. and Wiles, A. *Ring-theoretic properties of certain Hecke algebras.* Annals of Mathematics, 1995.
- **[Foundational]** Ribet, K. *On modular representations of $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms.* Inventiones Mathematicae, 1990.
- **[Survey]** Darmon, H., Diamond, F., and Taylor, R. *Fermat's Last Theorem.* Current Developments in Mathematics, 1995.
- **[SOTA / Recent]** Breuil, C., Conrad, B., Diamond, F., and Taylor, R. *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises.* Journal of the American Mathematical Society, 2001.

## 10. Worked Example / Concrete Special Case

The case $n=4$ provides a concrete example of Fermat's technique of "infinite descent". Fermat originally proved a slightly stronger statement: the equation $x^4 + y^4 = z^2$ has no solutions in strictly positive, coprime integers.

**Proof steps for $x^4 + y^4 = z^2$:**
1. Assume there exists a minimal positive integer $z$ satisfying $x^4 + y^4 = z^2$ for coprime $x, y$.
2. We can rewrite the equation as $(x^2)^2 + (y^2)^2 = z^2$. This means $(x^2, y^2, z)$ is a primitive Pythagorean triple.
3. By the properties of Pythagorean triples, there exist coprime integers $u, v$ (with opposite parity) such that:
   $$x^2 = u^2 - v^2, \quad y^2 = 2uv, \quad z = u^2 + v^2$$
4. Rearranging the first equation gives $x^2 + v^2 = u^2$. This implies $(x, v, u)$ is another primitive Pythagorean triple.
5. Therefore, there exist coprime integers $r, s$ such that:
   $$x = r^2 - s^2, \quad v = 2rs, \quad u = r^2 + s^2$$
6. Substituting $u$ and $v$ into $y^2 = 2uv$, we get:
   $$y^2 = 2(r^2 + s^2)(2rs) = 4rs(r^2 + s^2)$$
7. Because $u$ and $v$ are coprime, the terms $r$, $s$, and $(r^2+s^2)$ are pairwise coprime. Since their product multiplied by a square ($4$) is a square ($y^2$), the numbers $r$, $s$, and $r^2+s^2$ must themselves be perfect squares:
   $$r = a^2, \quad s = b^2, \quad r^2 + s^2 = c^2$$
8. Substituting $a^2$ for $r$ and $b^2$ for $s$ into the third relation yields:
   $$a^4 + b^4 = c^2$$
9. We have found a new solution $(a, b, c)$ to the original equation. However, observe the size of $c$:
   $$c \le c^2 = r^2 + s^2 = u \le u^2 < u^2 + v^2 = z$$
10. Since $c < z$, we have produced a strictly smaller positive integer solution. Repeating this process creates an infinitely decreasing sequence of positive integers ($z > c > \dots > 0$), which is impossible. 

This contradiction proves that no minimal $z$ exists, and therefore, $x^4 + y^4 = z^2$ has no positive integer solutions. This trivially implies that $x^4 + y^4 = z^4$ has no solutions, verifying Fermat's Last Theorem for $n=4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*