---
id: 01-number-theory/irrationality-of-catalans-constant
title: "Irrationality of Catalan's Constant"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Irrationality of Catalan's Constant

> **Topic:** Number Theory · **ID:** `01-number-theory/irrationality-of-catalans-constant` · **Status:** open

## 1. Problem Statement / Conjecture

Catalan's constant, denoted by $G$ (and occasionally $C$ or $K$), is a famous numerical constant appearing in number theory, combinatorics, and topology. It is defined by the alternating series:

$$ G = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2} = 1 - \frac{1}{9} + \frac{1}{25} - \frac{1}{49} + \cdots \approx 0.91596559... $$

The primary mathematical claim (the conjecture) states that **$G$ is an irrational number**. That is, there do not exist integers $p, q$ with $q \neq 0$ such that $G = p/q$.

A stronger, natural extension of this conjecture is that $G$ is a **transcendental number**, meaning it is not the root of any non-zero polynomial equation with rational coefficients. A complete proof of the open problem requires producing a rigorous sequence of rational approximations or a topological/motivic argument that contradicts the assumption that $G \in \mathbb{Q}$.

## 2. Mathematical Foundations

Catalan's constant is fundamentally tied to the **Dirichlet beta function**, $\beta(s)$, which is the $L$-function associated with the non-principal Dirichlet character modulo 4, denoted $\chi_4(n)$. The function is defined for $\text{Re}(s) > 0$ as:

$$ \beta(s) = L(s, \chi_4) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^s} $$

Under this definition, $G = \beta(2)$.

The constant also appears naturally in various analytic and geometric identities. It can be represented by several definite integrals over the unit square and unit interval:

$$ G = \int_0^1 \int_0^1 \frac{1}{1+x^2 y^2} \,dx \,dy = -\int_0^1 \frac{\ln(x)}{1+x^2} \,dx = \frac{1}{2} \int_0^{\pi/2} \frac{x}{\sin x} \,dx $$

Geometrically, $G$ is linked to the volumes of ideal hyperbolic polyhedra. Specifically, the volume of an ideal hyperbolic octahedron in 3-dimensional hyperbolic space $\mathbb{H}^3$ is precisely $3.6638... = 4G$. In algebraic geometry, $G$ is expected to be a **period** in the sense of Kontsevich and Zagier, given that it is the integral of a rational function over a domain defined by polynomial inequalities.

## 3. History & State of the Art (SOTA)

The constant is named after the Belgian mathematician Eugène Charles Catalan, who first studied its properties in 1865 while investigating rapidly converging series for mathematical constants. 

Historically, the modern pursuit of an irrationality proof for $G$ was heavily inspired by Roger Apéry’s shocking 1978 proof that $\zeta(3)$ is irrational. Apéry achieved this by constructing a sequence of fast-converging rational approximations derived from hypergeometric recurrence relations (specifically, P-recursive sequences). Since $\beta(2)$ shares profound analytic similarities with $\zeta(2)$ and $\zeta(3)$, it was widely anticipated that an Apéry-style proof would quickly be found for $G$.

However, more than four decades later, standard hypergeometric methods have failed to yield an irrationality measure for $G$. Computationally, $G$ has been calculated to trillions of decimal digits (e.g., using the highly efficient Ramanujan-type series discovered by Jesús Guillera and others). Analysis of its continued fraction expansion shows no discernable patterns, providing strong heuristic support for both its irrationality and transcendence.

## 4. Partial Results / Verified Cases

While the irrationality of $G$ remains unsolved, deep structural results have been proven for the Dirichlet beta function at even integer values.

In 2003, Tanguy Rivoal and Wadim Zudilin applied the saddle-point method to generalized hypergeometric series to prove that **infinitely many of the values $\beta(2n)$ are irrational**, where $n \in \mathbb{Z}^+$. 

By refining these bounds using a specific multivariate linear form, they established the most significant partial result regarding $G$ to date: at least one of the following six constants must be irrational:

$$ \beta(2), \beta(4), \beta(6), \beta(8), \beta(10), \beta(12) $$

Since $G = \beta(2)$, this verified that $G$ belongs to a small, finite set of constants where irrationality is guaranteed for at least one member. Unfortunately, their method does not provide a mechanism to isolate $G$ and prove its irrationality independently.

## 5. Principal Obstacles

The fundamental bottleneck in proving the irrationality of $G$ lies in the arithmetic growth of denominators in rational approximations. 

Standard techniques rely on finding a sequence of integers $p_n, q_n$ such that the approximation error shrinks faster than the denominator grows. By Dirichlet's irrationality criterion, one needs:

$$ 0 < |q_n G - p_n| < \frac{c}{q_n^\delta} $$

for some constants $c > 0$ and $\delta > 0$. 

When constructing Padé approximations or hypergeometric integrals for $G$, the resulting linear forms $q_n G - p_n$ can be made analytically very small. However, the coefficients $p_n, q_n$ are typically rational numbers, not integers. To clear the denominators, one must multiply by their least common multiple, denoted $d_n$. 

For Apéry’s proof of $\zeta(3)$, the prime number theorem and specific $p$-adic valuations cause $d_n$ to grow slowly enough (a phenomenon known as the "Apéry miracle") that the bound holds. For Catalan's constant, all known hypergeometric constructions yield denominators $d_n$ that grow exponentially faster than the analytic remainder shrinks. Consequently, after multiplying by $d_n$ to make the coefficients integers, the error term $|d_n q_n G - d_n p_n|$ diverges to infinity instead of converging to zero.

## 6. The Gap

The exact mathematical gap is the lack of a known linear form or rational hypergeometric integral evaluated over the unit hypercube that simultaneously achieves:
1. **Analytic proximity:** An exponentially decaying remainder term as $n \to \infty$.
2. **Arithmetic control:** A highly constrained denominator growth for the resulting L-combinations.

To cross this barrier, mathematicians must either discover a radically new family of identities for $G$ with hidden arithmetic cancellation (e.g., unprecedented prime-factor vanishing in the denominators), or completely abandon the Padé approximation approach in favor of deeper geometric, motivic, or $K$-theoretic methods that do not rely on constructing explicit rational bounds.

## 7. Current Research (as of June 2026)

Active research continues in two main directions: the search for new hypergeometric integrals (often utilizing algorithmic searches and automated integer-relation algorithms like PSLQ) and the study of motives associated with Feynman integrals, where $G$ occasionally appears.

A highly notable event occurred in September 2026, when a preprint by Zhi-Wei Sun (arXiv:2609.04176) was released claiming a full proof of the irrationality of $G$. 

*(frontier — verify)*: The paper proposes a method involving "specially chosen weights" and finite matrices of "residual sums" to derive a contradiction assuming $G \in \mathbb{Q}$. While the author claims the proof was aided and verified by AI (ChatGPT 5.6 Solar), early scrutiny from independent researchers has identified potential fatal errors in the handling of tail recurrences and the vanishing of certain matrix minors. As of late 2026, the mathematical consensus is that the problem remains open pending rigorous peer review and human verification.

## 8. Future Work

Leading mathematicians suggest that future breakthroughs might not come from classical analysis, but rather from algebraic geometry. Specifically, Grothendieck's Period Conjecture posits that any algebraic relations between periods of algebraic varieties over $\mathbb{Q}$ must arise from geometric morphisms (isomorphisms of motives). 

If $G$ and $\pi$ can be placed into the appropriate cohomological framework, proving their algebraic independence would trivially imply the irrationality (and transcendence) of $G$. Future work is heavily focused on developing a more robust, unconditionally proven theory of mixed Tate motives over $\mathbb{Z}[1/2]$ where values of $\beta(s)$ naturally live.

## 9. Key References

- **[Foundational]** Tanguy Rivoal, Wadim Zudilin. *Diophantine properties of numbers related to Catalan's constant.* Mathematische Annalen, 326(4), 705–721, 2003. (doi:10.1007/s00208-003-0433-3)
- **[SOTA / Recent]** Zhi-Wei Sun. *Irrationality of Catalan's Constant* (Preprint). arXiv:2609.04176, 2026.
- **[Survey]** Wadim Zudilin. *Arithmetic of linear forms involving odd zeta values.* Journal de Théorie des Nombres de Bordeaux, 16(1), 251-291, 2004.

## 10. Worked Example / Concrete Special Case

To understand the core obstacle (Section 5) mathematically, consider the following classical integral sequence over the unit square, which attempts to approximate $G$:

$$ I_n = \int_0^1 \int_0^1 \frac{x^n (1-x)^n y^n (1-y)^n}{1+x^2 y^2} \,dx \,dy $$

**Base Case ($n=0$):**
Evaluating the integral for $n=0$:
$$ I_0 = \int_0^1 \int_0^1 \frac{1}{1+x^2y^2} \,dx \,dy $$
Integrating with respect to $x$ yields $\frac{\arctan(y)}{y}$. Substituting the Taylor series $\arctan(y) = \sum_{k=0}^\infty \frac{(-1)^k y^{2k+1}}{2k+1}$, we get:
$$ I_0 = \int_0^1 \sum_{k=0}^\infty \frac{(-1)^k y^{2k}}{2k+1} \,dy = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)^2} = G $$

**General Case ($n > 0$):**
Because $x^n(1-x)^n y^n(1-y)^n$ is a polynomial in $x, y$ with integer coefficients, expanding it and performing polynomial division by $(1+x^2y^2)$ will leave a remainder. Integrating this polynomial structure guarantees that $I_n$ can always be written in the form:
$$ I_n = a_n G + b_n $$
where $a_n, b_n \in \mathbb{Q}$.

Since $0 < \frac{x(1-x)y(1-y)}{1+x^2y^2} < \frac{1}{16}$ for $x, y \in (0, 1)$, it is clear that $I_n \to 0$ exponentially fast as $n \to \infty$. This implies that $a_n G + b_n \to 0$.

**The Failure:**
To prove irrationality, $a_n$ and $b_n$ must be integers. Because they are fractions resulting from integrating polynomials like $\int x^k dx = \frac{1}{k+1}$, their common denominator $d_n$ is approximately the least common multiple of $\{1, 2, \dots, 2n\}$, which is bounded by $e^{2n}$ (by the Prime Number Theorem). 
When we scale the equation by $d_n$ to ensure integer coefficients $A_n = d_n a_n$ and $B_n = d_n b_n$, we analyze the new error:
$$ d_n I_n = A_n G + B_n $$
Unfortunately, the arithmetic growth of $d_n \approx e^{2n} \approx 7.38^n$ overwhelms the analytic decay of $I_n \le (1/16)^n$. Therefore, $d_n I_n \to \infty$, failing Dirichlet's criteria for irrationality and demonstrating precisely why finding the "right" integral for Catalan's constant remains an unsolved problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*