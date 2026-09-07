---
id: 01-number-theory/de-bruijn-newman-constant-problem
title: "De Bruijn-Newman Constant Problem"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# De Bruijn-Newman Constant Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/de-bruijn-newman-constant-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The De Bruijn-Newman constant, denoted $\Lambda$, governs the zeros of a family of entire functions $H_{\lambda}(z)$ formed by a continuous heat-flow deformation of the Riemann $\xi$-function. The Riemann Hypothesis (RH) is exactly equivalent to the statement that $\Lambda \le 0$. The De Bruijn-Newman Constant Problem, initially popularized via Newman's Conjecture, posited that $\Lambda \ge 0$. 

Together, these statements imply that if the Riemann Hypothesis is true, it is "barely" true, meaning $\Lambda = 0$. The lower bound problem (Newman's conjecture proving $\Lambda \ge 0$) was recently solved by Brad Rodgers and Terence Tao. However, the overarching problem of finding the exact value of $\Lambda$ and rigorously establishing the upper bound $\Lambda \le 0$ (thereby proving the Riemann Hypothesis) remains open.

## 2. Mathematical Foundations

The Riemann $\xi$-function is an entire function whose zeros precisely correspond to the non-trivial zeros of the Riemann zeta function $\zeta(s)$. It can be expressed via the Fourier cosine transform:
$$ \xi\left(\frac{1}{2} + iz\right) = E_0(z) = \int_0^{\infty} \Phi(t) \cos(zt) dt $$
where the super-exponentially decaying kernel $\Phi(t)$ is derived from Jacobi's theta function:
$$ \Phi(t) = \sum_{n=1}^{\infty} \left(2\pi^2 n^4 e^{9t} - 3\pi n^2 e^{5t}\right) \exp(-\pi n^2 e^{4t}) $$

In 1950, N.G. de Bruijn introduced a one-parameter family of entire functions $H_{\lambda}(z)$ by applying a Gaussian heat kernel, modifying the integral by a factor of $e^{\lambda t^2}$:
$$ H_{\lambda}(z) = \int_0^{\infty} \Phi(t) e^{\lambda t^2} \cos(zt) dt $$

The De Bruijn-Newman constant $\Lambda$ is defined as the infimum of all real $\lambda$ such that $H_{\lambda}(z)$ possesses exclusively real zeros:
$$ \Lambda = \inf \{ \lambda \in \mathbb{R} : H_{\lambda}(z) \text{ has only real zeros} \} $$
De Bruijn proved that if $H_{\lambda}$ has only real zeros for some $\lambda$, then $H_{\lambda'}$ has only real zeros for all $\lambda' \ge \lambda$. Because $H_0(z) = \xi(1/2 + iz)$, the Riemann Hypothesis is equivalent to the statement that $H_0$ has only real zeros, which translates algebraically to the strict bound $\Lambda \le 0$.

## 3. History & State of the Art (SOTA)

- **1950:** N.G. de Bruijn introduced the functions $H_{\lambda}(z)$ and proved the initial upper bound $\Lambda \le 1/2$. He also proved the fundamental property that the zeros are drawn toward the real axis as $\lambda$ increases.
- **1976:** Charles M. Newman proved that $\Lambda > -\infty$, showing that there exists some threshold where $H_{\lambda}$ possesses non-real zeros. He famously conjectured that $\Lambda \ge 0$.
- **2018-2020 (Rodgers & Tao):** Brad Rodgers and Terence Tao formally proved Newman's conjecture, establishing rigorously that $\Lambda \ge 0$. Combined with de Bruijn's framework, this implies that the Riemann Hypothesis is true if and only if $\Lambda = 0$.
- **2019 (Polymath15):** The collaborative Polymath15 project systematically improved the upper bounds of $\Lambda$ by analyzing the zeros of the Riemann zeta function, utilizing extensive computational methods to establish $\Lambda \le 0.22$.
- **2021 (Platt & Trudgian):** Dave Platt and Tim Trudgian pushed the Riemann zeta zero verification up to height $T = 3 \cdot 10^{12}$, establishing the tighter bound $\Lambda \le 0.2$. Subsequent algorithmic refinements have pushed this upper bound slightly below $0.18$.

## 4. Partial Results / Verified Cases

The lower bound of the problem is completely resolved: $\Lambda \ge 0$ (Rodgers-Tao). 

For the upper bound, progress strictly correlates with the computational verification of the Riemann Hypothesis up to massive heights in the critical strip. The verification of RH up to the height $T = 3 \cdot 10^{12}$ yields the unconditional upper bound of $\Lambda \le 0.2$. In theoretical special cases, local spacing analysis of the zeros of $\zeta(s)$ confirms that if the asymptotic gaps between zeros precisely follow the Gaussian Unitary Ensemble (GUE) random matrix distribution, then no macroscopic gaps exist that could force $\Lambda > 0$, structurally supporting $\Lambda = 0$.

## 5. Principal Obstacles

The pursuit of the exact upper bound ($\Lambda = 0$) runs into the exact same insurmountable wall as the Riemann Hypothesis itself. The primary mathematical bottleneck is tracking the global trajectory of zeros of $H_{\lambda}(z)$ as $\lambda$ flows backwards under the governing differential equation (from $\lambda > 0$ down to $\lambda = 0$). 

While the forward heat equation is smoothing and well-behaved, the backwards heat equation is notoriously ill-posed. Standard perturbation theory and Fourier analysis break down because microscopic deviations in the spacing of the zeros of the $\xi$-function can amplify exponentially under backwards heat flow. If consecutive zeros are spaced slightly too far apart, the backwards flow causes them to repel, collide with adjacent zeros, and violently scatter off the real line into the complex plane.

## 6. The Gap

The gap between the solved Newman Conjecture ($\Lambda \ge 0$) and the full resolution of the Riemann Hypothesis ($\Lambda \le 0$) is currently being closed strictly from above. Because we know $\Lambda \ge 0$, the exact barrier is rigorously establishing that no zeros of $H_{\lambda}$ ever split off the real axis as $\lambda$ decreases from its current upper bound (~$0.178$) down to $0$. Overcoming this requires a mathematical breakthrough in bounding the distance between consecutive zeros of the Riemann zeta function or formulating an entirely new spectral representation of $\xi(s)$ that side-steps the ill-posed nature of the backwards heat flow.

## 7. Current Research (as of June 2026)

Research on the De Bruijn-Newman constant currently operates predominantly in the computational and analytic realms, seeking to lower the upper bound:
- **Large Scale Verification:** Extensions of the Platt-Trudgian methodology to larger heights $T$ using distributed computing and rigorous interval arithmetic bounds.
- **Effective Approximations:** Refining the Polymath15 approach to computationally effectively approximate the heat flow evolution of the Riemann $\xi$ function.
- **Random Matrix Theory:** Investigating whether the exact GUE spacing statistics can deterministically rule out the existence of macroscopic zero-gaps that would force $\Lambda > 0$. *(frontier — verify)*

## 8. Future Work

Leading mathematicians suggest two parallel tracks for future inquiry:
1. **Computational:** Continuing the systematic verification of zeroes of $\zeta(1/2+it)$ to unconditionally lower the rigorous upper bound for $\Lambda$. This provides a quantitative, incremental metric for progress toward RH.
2. **Spectral Theory:** Formulating the De Bruijn-Newman heat operator in the context of spectral geometry or Hilbert-Pólya operator theory. The goal is to identify a self-adjoint operator whose spectrum corresponds exactly to the zeroes of $H_0$, thereby proving all zeros must remain real natively without relying on backwards flow.

## 9. Key References

- **[Foundational]** De Bruijn, N.G. *The roots of trigonometric integrals.* Duke Mathematical Journal, 1950.
- **[Foundational]** Newman, C.M. *Fourier transforms with only real zeros.* Proceedings of the American Mathematical Society, 1976.
- **[SOTA / Recent]** Rodgers, B., & Tao, T. *The De Bruijn-Newman constant is non-negative.* Forum of Mathematics, Pi, 2020.
- **[SOTA / Recent]** D.H.J. Polymath. *Effective approximation of heat flow evolution of the Riemann $\xi$ function, and a new upper bound for the de Bruijn-Newman constant.* Research in the Mathematical Sciences, 2019.
- **[SOTA / Recent]** Platt, D., & Trudgian, T. *The Riemann hypothesis is true up to $3 \cdot 10^{12}$.* Bulletin of the London Mathematical Society, 2021.

## 10. Worked Example / Concrete Special Case

To intuitively understand how the heat operator governs the zeros of $H_\lambda(z)$, we can analyze a simplified toy model. The function $H_\lambda(z)$ satisfies a differential equation analogous to the backwards heat equation: $\partial_\lambda H_\lambda(z) = -\partial_z^2 H_\lambda(z)$. 

Consider a simple quadratic function representing a local pair of zeros undergoing this flow:
$$ f_\lambda(z) = z^2 - c - 2\lambda $$
where $c > 0$ is a constant. We can easily verify that this toy function identically satisfies the flow equation:
$$ \partial_\lambda f_\lambda(z) = -2 \quad \text{and} \quad -\partial_z^2 f_\lambda(z) = -2 $$

The roots of this function are given by:
$$ z = \pm\sqrt{c + 2\lambda} $$
As $\lambda$ increases (the forward direction), the term $c + 2\lambda$ grows, shifting the parabola downward. The roots spread further apart on the real axis.
However, as $\lambda$ decreases (the backwards direction), the parabola shifts upward. The two real roots attract each other. At the critical threshold $\lambda^* = -c/2$, the roots violently collide at $z=0$ (a double root). For any $\lambda < \lambda^*$, the quantity $c + 2\lambda$ becomes negative, forcing the roots to split into a complex conjugate pair. 

The De Bruijn-Newman constant $\Lambda$ represents the global supremum of these collision thresholds $\lambda^*$ across the infinitely many zeros of the Riemann $\xi$-function. Rodgers and Tao essentially proved that due to the dense spacing of Riemann zeros, if one runs this flow backwards below $\lambda = 0$, at least one pair of zeros is mathematically forced to collide and scatter off the real axis, establishing that $\Lambda \ge 0$.