---
id: 01-number-theory/irrationality-of-pi-plus-e
title: "Irrationality of Pi plus E"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Irrationality of Pi plus E

> **Topic:** Number Theory · **ID:** `01-number-theory/irrationality-of-pi-plus-e` · **Status:** open

## 1. Problem Statement / Conjecture

The problem asks whether the sum of the fundamental mathematical constants $\pi$ and $e$ is an irrational number. Formally, the conjecture states that:
$$\pi + e \in \mathbb{R} \setminus \mathbb{Q}$$
More broadly, this problem is a special case of the conjecture that $\pi$ and $e$ are algebraically independent over the field of rational numbers $\mathbb{Q}$. A complete proof of the irrationality of $\pi + e$ would require showing that there exist no integers $a, b$ (with $b \neq 0$) such that $\pi + e = \frac{a}{b}$. A disproof would consist of finding such integers, though it is universally suspected that the sum is both irrational and transcendental.

## 2. Mathematical Foundations

Let $\mathbb{Q}$ denote the field of rational numbers and $\mathbb{R}$ the field of real numbers. A real number $x$ is called irrational if $x \notin \mathbb{Q}$. Furthermore, a number is algebraic if it is a root of a non-zero polynomial with rational coefficients, and transcendental otherwise.

A finite set of complex numbers $S = \{z_1, z_2, \dots, z_n\}$ is said to be algebraically independent over $\mathbb{Q}$ if there is no non-zero polynomial $P(X_1, \dots, X_n) \in \mathbb{Q}[X_1, \dots, X_n]$ such that $P(z_1, \dots, z_n) = 0$.

The irrationality of $\pi + e$ relies heavily on the theory of transcendental numbers. It is a well-established theorem that both $e$ and $\pi$ are transcendental:
- For $e$: There is no non-zero polynomial $P \in \mathbb{Q}[X]$ such that $P(e) = 0$.
- For $\pi$: There is no non-zero polynomial $P \in \mathbb{Q}[X]$ such that $P(\pi) = 0$.

However, knowing that two numbers are transcendental does not automatically imply that their sum, product, or difference is transcendental or even irrational. For instance, $\pi$ and $1-\pi$ are both transcendental, but their sum is $1 \in \mathbb{Q}$.

## 3. History & State of the Art (SOTA)

The history of this problem is deeply intertwined with the development of transcendence theory in the 19th and 20th centuries. 
- **1873**: Charles Hermite proved the transcendence of $e$.
- **1882**: Ferdinand von Lindemann extended Hermite's method to prove the transcendence of $\pi$, utilizing the identity $e^{i\pi} + 1 = 0$. This resolved the ancient problem of squaring the circle.
- **1966**: Alan Baker's theorem on linear forms in logarithms revolutionized transcendence theory, but it applies to logarithms of algebraic numbers. Because $e$ is not the logarithm of an algebraic number, Baker's method fails to tackle $\pi + e$.
- **1996**: Yuri Nesterenko proved that $\pi$, $e^{\pi}$, and $\Gamma(1/4)$ are algebraically independent over $\mathbb{Q}$. This successfully addressed the transcendence of $\pi + e^{\pi}$, but $\pi + e$ remains unsolved.

To this day, there is no proof for the irrationality of $\pi + e$, $\pi - e$, $\pi e$, or $\pi / e$.

## 4. Partial Results / Verified Cases

While the primary conjecture is unresolved, there are several foundational verified cases and partial results:
- **Disjunction of Rationality**: It is mathematically proven that at least one of $\pi + e$ and $\pi e$ is irrational (and, in fact, transcendental).
- **Generalized Disjunction**: For any non-zero integer $n$, it is proven that at least one of $e^n + \pi$ and $e^n \pi$ is transcendental.
- **Schanuel's Conjecture Dependency**: It is known that if Schanuel's Conjecture is true, then $\pi$ and $e$ are algebraically independent, which would immediately imply that $\pi + e$ is irrational and transcendental. Schanuel's Conjecture states that if $z_1, \dots, z_n \in \mathbb{C}$ are linearly independent over $\mathbb{Q}$, then the extension field $\mathbb{Q}(z_1, \dots, z_n, e^{z_1}, \dots, e^{z_n})$ has transcendence degree at least $n$ over $\mathbb{Q}$.

## 5. Principal Obstacles

The fundamental bottleneck is that $e$ and $\pi$ originate from entirely different analytical domains, and we lack a mathematical tool capable of approximating both simultaneously without losing vital algebraic structure. 
- $e$ is characterized by the exponential function's power series and has excellent arithmetic properties that can be bounded using Padé approximants.
- $\pi$ appears as a period (specifically, $i\pi = \log(-1)$), deeply tied to geometry and the zeros of trigonometric functions.

Classical techniques like the Lindemann-Weierstrass theorem require the arguments of the exponential function to be algebraic. Since $\pi$ is transcendental, we cannot natively mix $e^1$ and $e^{i\pi}$ in the same linear forms without introducing unmanageable error bounds. Current Diophantine approximation methods cannot create a sequence of rational approximations $p_n/q_n \to \pi + e$ that converge rapidly enough to prove irrationality.

## 6. The Gap

The precise mathematical barrier lies in traversing from the known disjunctive claim ("Either $\pi + e \notin \mathbb{Q}$ or $\pi e \notin \mathbb{Q}$") to an isolated proof for just one of the constants. We understand that the pair $(\pi + e, \pi e)$ cannot map to $\mathbb{Q} \times \mathbb{Q}$. The gap requires discovering a new invariant, period integral, or measure of transcendence that exclusively isolates the additive relationship $\pi + e$ without requiring the multiplicative relationship $\pi e$ to bear the algebraic load. 

## 7. Current Research (as of June 2026)

Currently, number theorists are approaching this problem via abstract frameworks rather than direct numerical approximation:
- **Exponential Motives**: Following Grothendieck's period conjecture, researchers are studying the motivic Galois groups of exponential motives. By framing $\pi$ and $e$ as periods of different algebraic varieties, researchers aim to prove that no unexpected geometric relations exist between their governing varieties. 
- **E-functions and G-functions**: Extending Siegel's theory of E-functions (generalizations of the exponential function) and G-functions (generalizations of logarithmic functions). The frontier of this research attempts to find cross-evaluations or differential systems where both $\pi$ and $e$ appear as singular values. *(frontier — verify)*
- **Weak Schanuel Methods**: Attempting to prove isolated, low-dimensional cases of Schanuel's Conjecture that only involve constants like $1$, $i\pi$, and $e$.

## 8. Future Work

Leading researchers suggest the following pathways for future work:
- Establishing new irrationality measures that combine exponential metrics with logarithmic heights, potentially forcing an incompatibility if $\pi+e$ were rational.
- Expanding the scope of Nesterenko's modular function techniques. If a modular form could be constructed where both $e$ and $\pi$ naturally emerge in the quasi-periods, it might be possible to force an algebraic independence result.
- Resolving the algebraic independence of $e$ and Euler's constant $\gamma$, which shares similar Diophantine obstacles, as a stepping stone toward $\pi + e$.

## 9. Key References

- **[Foundational]** Baker, A. *Transcendental Number Theory.* Cambridge University Press, 1975.
- **[Foundational]** Nesterenko, Yu. V. "Modular functions and transcendence questions." *Sbornik: Mathematics*, 187(9):1319–1348, 1996.
- **[Survey]** Waldschmidt, M. "Open Diophantine problems." *Moscow Mathematical Journal*, 4(1):245-305, 2004.
- **[Survey]** Fel'dman, N. I. and Nesterenko, Yu. V. *Transcendental Numbers.* Number Theory IV, Encyclopaedia of Mathematical Sciences, Vol. 44, Springer, 1998.

## 10. Worked Example / Concrete Special Case

While we cannot prove $\pi + e$ is irrational directly, we can walk through the classical proof of the disjunctive case to illustrate the underlying algebraic mechanism.

**Theorem:** It is impossible for both $\pi + e$ and $\pi e$ to be rational numbers.

**Proof:**
1. Assume, for the sake of contradiction, that both values are rational. Let $\pi + e = q_1 \in \mathbb{Q}$ and $\pi e = q_2 \in \mathbb{Q}$.
2. Construct a monic quadratic polynomial with $\pi$ and $e$ as its roots:
   $$P(x) = (x - \pi)(x - e)$$
3. Expand this polynomial algebraically:
   $$P(x) = x^2 - (\pi + e)x + \pi e$$
4. Substitute our rational assumptions $q_1$ and $q_2$ into the polynomial:
   $$P(x) = x^2 - q_1 x + q_2$$
5. Because $q_1, q_2 \in \mathbb{Q}$, the polynomial $P(x)$ has strictly rational coefficients, meaning $P(x) \in \mathbb{Q}[x]$.
6. By definition, any root of a non-zero polynomial with rational coefficients is an algebraic number. Since $\pi$ and $e$ are the roots of $P(x)$, they must both be algebraic numbers of degree at most 2.
7. This directly contradicts Hermite's theorem (which states $e$ is transcendental) and Lindemann's theorem (which states $\pi$ is transcendental).
8. Because a contradiction has been reached, our initial assumption must be false. 

Therefore, at least one of $\pi + e$ or $\pi e$ must be irrational. This simple use of elementary symmetric polynomials highlights why additive and multiplicative properties of transcendental numbers are inextricably linked.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*