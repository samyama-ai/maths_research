---
id: 01-number-theory/irrationality-of-pi-times-e
title: "Irrationality of Pi times E"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Irrationality of Pi times E

> **Topic:** Number Theory · **ID:** `01-number-theory/irrationality-of-pi-times-e` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that the real number defined by the product of the fundamental mathematical constants $\pi$ (the ratio of a circle's circumference to its diameter) and $e$ (the base of the natural logarithm), denoted as $\pi e$, is an irrational number. 

Formally, there do not exist integers $p, q \in \mathbb{Z}$ with $q \neq 0$ such that:
$$ \pi e = \frac{p}{q} $$

A stronger form of the conjecture asserts that $\pi e$ is not only irrational but also a transcendental number, meaning it is not the root of any non-zero polynomial with rational coefficients. A complete proof requires establishing either the irrationality measure of $\pi e$ or proving the algebraic independence of $\pi$ and $e$.

## 2. Mathematical Foundations

The problem lies at the heart of **Transcendental Number Theory**. 

A number $\alpha \in \mathbb{C}$ is **algebraic** if there exists a non-zero polynomial $P(x) \in \mathbb{Q}[x]$ such that $P(\alpha) = 0$. Otherwise, $\alpha$ is **transcendental**.

A set of numbers $\{\alpha_1, \dots, \alpha_n\} \subset \mathbb{C}$ is **algebraically independent** over $\mathbb{Q}$ if there is no non-zero polynomial $P(x_1, \dots, x_n) \in \mathbb{Q}[x_1, \dots, x_n]$ such that:
$$ P(\alpha_1, \dots, \alpha_n) = 0 $$

The foundational framework that governs the expected behavior of transcendental numbers under exponentiation is **Schanuel's Conjecture**. It states that if $z_1, \dots, z_n \in \mathbb{C}$ are linearly independent over the rational numbers $\mathbb{Q}$, then the extension field $\mathbb{Q}(z_1, \dots, z_n, e^{z_1}, \dots, e^{z_n})$ has transcendence degree at least $n$ over $\mathbb{Q}$:
$$ \text{tr.deg}_{\mathbb{Q}} \, \mathbb{Q}(z_1, \dots, z_n, e^{z_1}, \dots, e^{z_n}) \geq n $$

If we set $n=2$, $z_1 = 1$, and $z_2 = i\pi$, they are linearly independent over $\mathbb{Q}$. Schanuel's conjecture implies that the field $\mathbb{Q}(1, i\pi, e, e^{i\pi}) = \mathbb{Q}(i\pi, e)$ has transcendence degree at least $2$. This would mean $\pi$ and $e$ are algebraically independent, trivially implying that $\pi e$ cannot be rational (since $xy - c = 0$ is a polynomial relation).

## 3. History & State of the Art (SOTA)

The history of the problem traces back to the late 19th century when mathematicians first successfully classified the individual constants $e$ and $\pi$:
- **1873:** Charles Hermite proved that $e$ is transcendental by constructing sophisticated rational approximations using what are now known as Padé approximants.
- **1882:** Ferdinand von Lindemann proved that $\pi$ is transcendental, leveraging Hermite's methods and Euler's identity ($e^{i\pi} = -1$) to establish the Lindemann-Weierstrass theorem.

Despite these monumental early victories, proving anything about the sum ($\pi + e$) or product ($\pi e$) of these constants has completely stalled. As of 2026, we still do not know if $\pi e$ is irrational. The state of the art in joint irrationality relies on Nesterenko's work on modular functions, but applying these to $\pi e$ specifically has yielded no definitive bounds.

## 4. Partial Results / Verified Cases

While the general conjecture for $\pi e$ remains open, the surrounding mathematical landscape has highly specific verified cases:

1. **The "At Least One" Theorem:** It is a verified result that at least one of the numbers $\pi + e$ and $\pi e$ is irrational (and transcendental).
2. **Nesterenko's Theorem (1996):** Using Ramanujan's functions and modular forms, Nesterenko proved the algebraic independence of $\pi$ and $e^{\pi}$ (Gelfond's constant). Therefore, $e^{\pi}$ is proven to be transcendental.
3. **Values of the Gamma Function:** For certain rational values $x$, the algebraic independence of $\pi$ and $\Gamma(x)$ has been established (e.g., $\pi$ and $\Gamma(1/4)$ are algebraically independent).
4. **Computational Verification:** $\pi e$ has been computed to trillions of decimal places (over 2 trillion as of recent computational benchmarks), and statistical analysis of its digit distribution heavily supports normality, confirming it behaves empirically like a typical irrational (and transcendental) number.

## 5. Principal Obstacles

The fundamental bottleneck is the limitation of the **Lindemann-Weierstrass Theorem** and the broader theory of linear forms in logarithms (Baker's theory). 

Standard transcendental methods work by constructing an auxiliary function (often an $E$-function or $G$-function) and evaluating it at algebraic points to derive a contradiction via integer bounds. The Lindemann-Weierstrass theorem explicitly requires the exponents to be *algebraic* numbers. 
$$ \beta_1 e^{\alpha_1} + \dots + \beta_n e^{\alpha_n} \neq 0 $$
(where $\alpha_i, \beta_i$ are algebraic). 

To prove $\pi e$ is irrational, we must analyze the interaction between $e$ and $\pi$. However, $\pi$ is transcendental. We lack a unified analytic framework (or a suitable differential equation) that evaluates the exponential function at transcendental points while simultaneously tightly bounding the Diophantine approximations of the resulting values. The auxiliary polynomials simply fail to produce non-trivial zero estimates when the points of evaluation ($\pi$ and $e$) are not algebraically linked.

## 6. The Gap

The exact mathematical barrier is the transition from **linear independence of logarithms of algebraic numbers** to the **algebraic independence of algebraically unrelated transcendental numbers**.

Section 4 shows we can prove algebraic independence when constants are inherently tied to the same algebraic structure or modular curve (like $\pi$ and $e^{\pi}$). The Gap is crossing from structured, modularly-related constants to independent constants from differing geometric origins: $\pi$ is a "period" (an integral of an algebraic differential form over a semi-algebraic domain), while $e$ is conjecturally not a period. The gap is mathematically defined by the absence of a generalized Galois theory for periods that can definitively separate the extensions generated by $e$ and $\pi$.

## 7. Current Research (as of June 2026)

Active research primarily flows through two advanced frameworks:

1. **Motivic Galois Theory and Periods:** Inspired by Kontsevich and Zagier, researchers at IHES and the Max Planck Institute are attempting to classify constants into rings of periods. Understanding the conjectural structure of the ring of exponential periods is currently the most promising avenue to definitively separate $e$ from $\pi$.
2. **Generalizations of Nesterenko's Method:** Russian and French schools of number theory are investigating multi-variable generalizations of modular forms. They are searching for a system of differential equations analogous to the Ramanujan differential equations for Eisenstein series, but which have algebraically independent values related to $e$ alongside $\pi$. *(frontier — verify)* Recent preprints explore using foliations on Abelian varieties to find new measures of algebraic independence.

## 8. Future Work

Leading figures in transcendental number theory suggest the following pathways:
- **Proving Weak Schanuel:** Rather than tackling the full Schanuel's Conjecture, focus on proving it strictly for $n=2$ with $z_1 = 1, z_2 = i\pi$.
- **New Zero Estimates:** Developing new techniques in elimination theory and commutative algebra to improve the multiplicity estimates for polynomials evaluated at transcendental numbers, sidestepping the reliance on traditional Padé approximations.
- **Arithmetic of E-functions:** Extending Siegel-Shidlovskii theory to determine necessary and sufficient conditions for the algebraic independence of E-functions over transcendental evaluation points.

## 9. Key References

- **[Foundational]** Baker, A. *Transcendental Number Theory*. Cambridge University Press, 1975.
- **[Foundational]** Lang, S. *Introduction to Transcendental Numbers*. Addison-Wesley, 1966.
- **[SOTA / Recent]** Nesterenko, Y. V. *Modular functions and transcendence questions*. Sbornik: Mathematics, 187(9), 1319–1348, 1996. [DOI](https://doi.org/10.1070/sm1996v187n09abeh000158)
- **[Survey]** Kontsevich, M., and Zagier, D. *Periods*. In: *Mathematics unlimited—2001 and beyond*, Springer, 2001, pp. 771-808. [DOI](https://doi.org/10.1007/978-3-642-56478-9)
- **[Survey]** Waldschmidt, M. *Diophantine Approximation on Linear Algebraic Groups*. Springer, 2000. [DOI](https://doi.org/10.1007/978-3-662-11569-5)

## 10. Worked Example / Concrete Special Case

To ground the difficulty of proving properties about $\pi$ and $e$ jointly, we can easily prove the partial result from Section 4: **At least one of the numbers $\pi + e$ or $\pi e$ must be irrational.**

**Proof:**
Let us define the sum $S = \pi + e$ and the product $P = \pi e$.
Assume, for the sake of contradiction, that *both* $S$ and $P$ are rational numbers ($S, P \in \mathbb{Q}$).

Consider the monic quadratic polynomial $Q(x)$ defined by the roots $\pi$ and $e$:
$$ Q(x) = (x - \pi)(x - e) $$
Expanding this, we get:
$$ Q(x) = x^2 - (\pi + e)x + \pi e = x^2 - Sx + P $$

Since we assumed both $S$ and $P$ are rational, the polynomial $Q(x)$ has rational coefficients, meaning $Q(x) \in \mathbb{Q}[x]$.
By definition, any root of a non-zero polynomial with rational coefficients is an **algebraic number**.
Therefore, the roots of $Q(x)$, which are precisely $\pi$ and $e$, must be algebraic numbers.

However, Hermite (1873) proved that $e$ is transcendental, and Lindemann (1882) proved that $\pi$ is transcendental. Neither is algebraic. This directly contradicts our deduction that $\pi$ and $e$ are algebraic.

Thus, our initial assumption must be false. Therefore, $\pi + e$ and $\pi e$ cannot *both* be rational; at least one of them must be irrational (and similarly, transcendental). 

This simple algebraic linkage ($x^2 - Sx + P$) shows why resolving either the sum or the product individually is a massive leap—they are intrinsically coupled as roots of a polynomial where the coefficients themselves inhabit the unknown boundary between the rational and the transcendental.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*