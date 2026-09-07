---
id: 01-number-theory/non-vanishing-of-central-l-values
title: "Non-vanishing of Central L-values"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Non-vanishing of Central L-values

> **Topic:** Number Theory · **ID:** `01-number-theory/non-vanishing-of-central-l-values` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that for well-behaved families of L-functions, the value of the L-function at the central symmetry point of its critical strip, $s = 1/2$, is non-zero, provided there is no trivial algebraic reason for it to vanish. 

The most classical formulation is **Chowla's Conjecture** (1965), which asserts that for every real primitive Dirichlet character $\chi$, the central value does not vanish: $L(1/2, \chi) \neq 0$. In the broader Langlands program, the Generalized Non-vanishing Conjecture asserts that for any family of self-dual automorphic L-functions possessing an even root number (which forces a positive sign in the functional equation), the proportion of L-functions in the family that do not vanish at $s = 1/2$ is $100\%$ as the analytic conductor tends to infinity.

## 2. Mathematical Foundations

Let $\pi$ be an automorphic representation of $GL(n, \mathbb{A}_K)$ for a number field $K$, encompassing classical arithmetic objects like Dirichlet characters, modular forms, and elliptic curves. The associated standard L-function is defined for $\Re(s) > 1$ by an Euler product and Dirichlet series:
$$ L(s, \pi) = \sum_{n=1}^\infty \frac{a_\pi(n)}{n^s} $$
Langlands' grand conjectures (proven in many classical cases) assert that $L(s, \pi)$ admits an analytic continuation to the entire complex plane and satisfies a functional equation relating $s$ to $1-s$:
$$ \Lambda(s, \pi) = L(s, \pi) \Gamma_\mathbb{R}(s, \pi) = \varepsilon(\pi) q_\pi^{1/2 - s} \Lambda(1-s, \tilde{\pi}) $$
where $\Gamma_\mathbb{R}(s, \pi)$ encapsulates the archimedean gamma factors, $q_\pi$ is the analytic conductor, $\tilde{\pi}$ is the contragredient representation, and $\varepsilon(\pi) \in \mathbb{C}$ (with $|\varepsilon(\pi)| = 1$) is the root number.

The *critical strip* is $0 \le \Re(s) \le 1$, and the *central point* is $s = 1/2$. For self-dual representations ($\pi \cong \tilde{\pi}$), the root number is strictly $\varepsilon(\pi) \in \{\pm 1\}$. If $\varepsilon(\pi) = -1$, the functional equation is odd and forces $L(1/2, \pi) = 0$ trivially. The Non-vanishing Conjecture concerns the "even" families where $\varepsilon(\pi) = +1$, where one generically expects $L(1/2, \pi) \neq 0$.

## 3. History & State of the Art (SOTA)

The systematic study of non-vanishing at the central point began with Sarvadaman Chowla in 1965. Over subsequent decades, the problem became a cornerstone of modern analytic number theory due to its deep connections to the Birch and Swinnerton-Dyer (BSD) Conjecture and the Generalized Riemann Hypothesis.

A monumental conceptual shift occurred in 1999 when Nicholas Katz and Peter Sarnak applied Random Matrix Theory (RMT) to model families of L-functions. They proved that the distribution of low-lying zeros near $s=1/2$ matches the eigenvalue distributions of large random matrices from classical compact groups (Orthogonal, Symplectic, or Unitary). RMT structurally predicts that zeros exactly at $s=1/2$ are statistical anomalies unless compelled by symmetry, theoretically justifying the expectation of $100\%$ non-vanishing for even families.

Currently, the state of the art relies on the analytic "mollification" method, pioneered by Selberg and vastly expanded by Iwaniec, Luo, Sarnak, and Soundararajan. This method has successfully proven strict positive proportions of non-vanishing for various prominent families.

## 4. Partial Results / Verified Cases

Substantial progress has been made bounding the proportion of non-vanishing cases in specific families from below:
- **Dirichlet L-functions:** Soundararajan (2000) proved that at least $87.5\%$ of quadratic Dirichlet L-functions $L(1/2, \chi_d)$ are non-zero.
- **Holomorphic Modular Forms:** Iwaniec, Luo, and Sarnak (2000) established that at least $50\%$ of the central values of L-functions associated with holomorphic cusp forms of large weight or large level are non-zero.
- **Elliptic Curves:** Bhargava, Shankar, et al. (2015) proved that a positive proportion (at least $50\%$ of those with root number $+1$) of elliptic curves over $\mathbb{Q}$ have algebraic rank 0. Combined with the Coates-Wiles theorem and Gross-Zagier formulas, this unconditionally implies $L(1/2, E) \neq 0$ for a positive proportion of all elliptic curves.

## 5. Principal Obstacles

The primary analytic strategy to establish non-vanishing across a family $\mathcal{F}$ uses the first and second mollified moments:
$$ M_1 = \sum_{\pi \in \mathcal{F}} L(1/2, \pi) M(\pi), \quad M_2 = \sum_{\pi \in \mathcal{F}} |L(1/2, \pi)|^2 |M(\pi)|^2 $$
where $M(\pi)$ is a short Dirichlet polynomial mimicking $L(1/2, \pi)^{-1}$. By the Cauchy-Schwarz inequality, the proportion $p$ of non-vanishing values satisfies $p \ge |M_1|^2 / (|\mathcal{F}| M_2)$.

To drive $p$ towards $100\%$, the length of the mollifier $M(\pi)$ must approach the maximum possible length allowed by the analytic conductor of the family. However, computing the variance $M_2$ introduces highly complex cross-terms. Expanding these terms via trace formulas (such as Kuznetsov or Petersson) yields character sums and Kloosterman sums. When the mollifier length exceeds a specific threshold (the "mollifier barrier"), the error terms—even bounded by Deligne's Weil Conjectures—explode and overpower the main term, inherently capping the non-vanishing density below $100\%$.

## 6. The Gap

The gap resides precisely at the boundary between a proven *positive proportion* (e.g., $87.5\%$) and *full density* ($100\%$ asymptotically) or *universal non-vanishing* (0 exceptions, as in Chowla's conjecture). Because analytic methods intrinsically operate on averages and probabilistic variances, they can only lower-bound non-vanishing. Even if asymptotic $100\%$ density were analytically achieved via higher moments, probabilistic techniques cannot inherently rule out the existence of sparse, finite subsets of counterexamples. Bridging the gap from "almost all" to "all" requires entirely novel rigid geometric or algebraic invariants.

## 7. Current Research (as of June 2026)

Active research involves bypassing classical trace formulas by studying the analytical properties of multiple Dirichlet series (the school of Bump, Friedberg, and Hoffstein). Additionally, researchers are refining asymptotic evaluations of higher moments of L-functions based on the CFKRS (Conrey-Farmer-Keating-Rubinstein-Snaith) conjectures. There is also intense focus on leveraging Iwasawa theory and Galois representations to find algebraic constraints that force non-vanishing, bypassing the mollifier barrier entirely.
*Frontier claims — verify*: Recent preprints claim localized advances in pushing the mollifier length slightly past the standard $\Delta = 1/2$ barrier using advanced spectral methods on $GL(3) \times GL(2)$ Rankin-Selberg convolutions, aiming to raise the theoretical baseline proportion limits.

## 8. Future Work

Future breakthroughs require either a radical evolution of the mollification technique—capable of cleanly evaluating third or fourth moments without off-diagonal explosions—or deep integration with arithmetic geometry. For elliptic curves, proving that the Tate-Shafarevich group is generically finite, or making unconditional progress on the Birch and Swinnerton-Dyer Conjecture, offers a distinct "algebraic backdoor": proving $L(1/2, E) \neq 0$ by independently proving that the arithmetic rank of $E(\mathbb{Q})$ is zero.

## 9. Key References

- **[Foundational]** S. Chowla. *The Riemann Hypothesis and Hilbert's Tenth Problem.* Gordon and Breach, New York, 1965.
- **[Foundational]** H. Iwaniec, W. Luo, and P. Sarnak. *Low lying zeros of families of L-functions.* Publications Mathématiques de l'IHÉS, 2000.
- **[Foundational]** K. Soundararajan. *Nonvanishing of quadratic Dirichlet L-functions at s=1/2.* Annals of Mathematics, 2000.
- **[SOTA / Recent]** M. Radziwiłł and K. Soundararajan. *Moments and distribution of central L-values of quadratic twists of elliptic curves.* Inventiones mathematicae, 2015.
- **[SOTA / Recent]** M. Bhargava and A. Shankar. *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0.* Annals of Mathematics, 2015.
- **[Survey]** N. Katz and P. Sarnak. *Zeroes of zeta functions and symmetry.* Bulletin of the American Mathematical Society, 1999.

## 10. Worked Example / Concrete Special Case

We can rigorously verify Chowla's non-vanishing conjecture for a small, concrete case: the unique non-principal, primitive quadratic character modulo 3, denoted $\chi_{-3}$. The values of $\chi_{-3}(n)$ for $n \equiv 1, 2, 0 \pmod 3$ are $1, -1$, and $0$ respectively.

The associated Dirichlet L-function is:
$$ L(s, \chi_{-3}) = \sum_{n=1}^\infty \frac{\chi_{-3}(n)}{n^s} = 1 - \frac{1}{2^s} + \frac{1}{4^s} - \frac{1}{5^s} + \frac{1}{7^s} - \frac{1}{8^s} + \dots $$
Because $\chi_{-3}$ is non-principal, this series converges conditionally for $\Re(s) > 0$. We evaluate it directly at the central point $s = 1/2$:
$$ L(1/2, \chi_{-3}) = 1 - \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{4}} - \frac{1}{\sqrt{5}} + \frac{1}{\sqrt{7}} - \frac{1}{\sqrt{8}} + \dots $$
To definitively prove $L(1/2, \chi_{-3}) \neq 0$, we strategically group the terms into adjacent pairs:
$$ L(1/2, \chi_{-3}) = \sum_{k=0}^\infty \left( \frac{1}{\sqrt{3k+1}} - \frac{1}{\sqrt{3k+2}} \right) $$
For any integer $k \ge 0$, it is strictly true that $3k+1 < 3k+2$, which implies $\sqrt{3k+1} < \sqrt{3k+2}$. Therefore, the reciprocal differences in each grouping are strictly positive:
$$ \frac{1}{\sqrt{3k+1}} - \frac{1}{\sqrt{3k+2}} > 0 $$
Because the L-value evaluates to an infinite sum of strictly positive terms (which converges by the Leibniz alternating series test), the total sum is strictly bounded from below by its very first paired term:
$$ L(1/2, \chi_{-3}) > 1 - \frac{1}{\sqrt{2}} \approx 0.2928 > 0 $$
Thus, $L(1/2, \chi_{-3})$ evaluates to a strictly positive real number and is demonstrably non-zero, serving as a foundational, mathematically rigorous verification of the conjecture for this specific L-function.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*