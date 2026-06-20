---
id: 01-number-theory/riemann-hypothesis
title: "Riemann Hypothesis"
topic: 01-number-theory
status: open
first_added: 2026-06
last_reviewed: 2026-06
last_substantive_update: 2026-06
stale_since: ""
provenance: synthesized
---

# Riemann Hypothesis

> **Topic:** Number Theory · **ID:** `01-number-theory/riemann-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

The Riemann Hypothesis states that all non-trivial zeros of the Riemann zeta function $\zeta(s)$ have a real part equal to $1/2$. 

That is, if $\zeta(s) = 0$ and $s$ is not a negative even integer (which are the trivial zeros), then:
$$\Re(s) = \frac{1}{2}$$

## 2. Mathematical Foundations

The Riemann zeta function is defined for complex numbers $s$ with $\Re(s) > 1$ by the Dirichlet series:
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$$

It can be analytically continued to a meromorphic function on the entire complex plane $\mathbb{C}$, with its only pole being a simple pole at $s = 1$ with residue 1.

The zeta function satisfies the functional equation:
$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

where $\Gamma(s)$ is the gamma function. From the functional equation, the trivial zeros occur at $s = -2, -4, -6, \dots$ due to the $\sin(\frac{\pi s}{2})$ term. The non-trivial zeros must lie in the "critical strip" defined by $0 < \Re(s) < 1$.

## 3. History & State of the Art (SOTA)

* **1859**: Bernhard Riemann formulated the hypothesis in his landmark paper, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (On the Number of Primes Less Than a Given Quantity).
* **1896**: Hadamard and de la Vallée Poussin independently proved the Prime Number Theorem by showing that $\zeta(s) \neq 0$ on the line $\Re(s) = 1$.
* **1914**: G. H. Hardy proved that infinitely many zeros of $\zeta(s)$ lie on the critical line $\Re(s) = 1/2$.
* **1942**: Atle Selberg proved that a positive proportion of the non-trivial zeros of $\zeta(s)$ lie on the critical line.
* **1989**: J. Brian Conrey proved that at least $40.77\%$ of the zeros in the critical strip lie on the critical line.

## 4. Partial Results / Verified Cases

* **Numerical Verification**: In 2020, Platt and Trudgian verified that the first $3 \times 10^{12}$ non-trivial zeros of $\zeta(s)$ lie on the critical line and are simple.
* **Analogous Conjectures**: The Riemann Hypothesis has been proven for function fields of algebraic curves over finite fields (proven by André Weil in 1948, and generalized as the Weil Conjectures by Pierre Deligne in 1974).

## 5. Principal Obstacles

* **Limitations of Real/Complex Analysis**: Standard tools of complex analysis can only locate zeros within regions, not exact lines.
* **Lack of Algebraic Framework**: Unlike function fields over finite fields, there is no natural geometric structure (like an algebraic curve over $\mathbb{Q}$) to which we can apply algebraic geometry tools.
* **Spectral Operator**: The Hilbert-Pólya conjecture suggests that the non-trivial zeros correspond to eigenvalues of a self-adjoint operator, but no such operator has been successfully constructed.

## 6. The Gap

The gap is between the critical strip $0 < \Re(s) < 1$ and the critical line $\Re(s) = 1/2$. We currently cannot prove that a zero cannot exist at $s = \sigma + it$ where $\sigma \neq 1/2$ and $0 < \sigma < 1$, although we know $\sigma$ must be strictly bounded away from $0$ and $1$.

## 7. Current Research (as of June 2026)

* **Random Matrix Theory**: Analyzing the correlation of zeta zeros, which match the eigenvalues of Random Hermite Matrices (the Montgomery-Odlyzko law).
* **Noncommutative Geometry**: Alain Connes and others have formulated spectral interpretations of the Riemann Hypothesis using adele spaces and noncommutative geometry.
* **De Bruijn-Newman Constant**: Research into the constant $\Lambda$; the Riemann Hypothesis is equivalent to $\Lambda \leq 0$. Recent results (Rodgers and Tao, 2018) proved $\Lambda \geq 0$, pinning it exactly to $\Lambda = 0$ if RH is true.

## 8. Future Work

* Developing a theory of motives over the hypothetical "field with one element" $\mathbb{F}_1$.
* Constructing an explicit self-adjoint operator whose eigenvalues correspond to the non-trivial zeros of $\zeta(s)$.

## 9. Key References

- **[Foundational]** Riemann, Bernhard. *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse.* Monatsberichte der Königlichen Preussischen Akademie der Wissenschaften zu Berlin, 1859.
- **[SOTA / Recent]** Platt, D. J., & Trudgian, T. S. *The Riemann hypothesis is true up to $3 \cdot 10^{12}$.* Research in Number Theory, 2021.
- **[Survey]** Conrey, J. Brian. *The Riemann Hypothesis.* Notices of the AMS, 2003.

## 10. Worked Example / Concrete Special Case

The first non-trivial zero of $\zeta(s)$ occurs at:
$$s_1 \approx \frac{1}{2} + i \cdot 14.134725$$

At this value, we can approximate the summation using Euler-Maclaurin summation. Let $s = \frac{1}{2} + 14.134725 i$. The value of $\zeta(s)$ is:
$$\zeta(s_1) \approx 0.000000 + 0.000000 i$$

This confirms that the first zero lies exactly on the critical line $\Re(s) = 1/2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*
