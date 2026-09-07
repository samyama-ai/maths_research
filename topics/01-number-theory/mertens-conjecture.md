---
id: 01-number-theory/mertens-conjecture
title: "Mertens Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mertens Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/mertens-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Mertens Conjecture claims a strict upper bound on the absolute value of the Mertens function $M(n)$. Specifically, it asserts that for all integers $n > 1$:
$$ |M(n)| < \sqrt{n} $$

A complete proof of this statement would have automatically implied the Riemann Hypothesis. Because the conjecture posits a strict mathematical inequality over all positive integers greater than 1, resolving it required either a universal proof for all $n$ or an explicit disproof establishing the existence of at least one counterexample where $|M(n)| \ge \sqrt{n}$. The conjecture is now known to be false, though no explicit counterexample has ever been constructed.

## 2. Mathematical Foundations

The conjecture relies on the Möbius function, $\mu(n)$, an important multiplicative function in number theory. For any positive integer $n$, $\mu(n)$ is defined as:
$$ \mu(n) = 
\begin{cases} 
1 & \text{if } n \text{ is a square-free integer with an even number of prime factors,} \\
-1 & \text{if } n \text{ is a square-free integer with an odd number of prime factors,} \\
0 & \text{if } n \text{ has a squared prime factor.}
\end{cases} $$

The Mertens function, $M(x)$, is the summatory function of $\mu(n)$:
$$ M(x) = \sum_{1 \le n \le x} \mu(n) $$

The profound mathematical significance of the Mertens function stems from its connection to the Riemann zeta function, $\zeta(s)$, via the Mellin transform. For complex numbers $s$ with $\Re(s) > 1$, the following integral identity holds:
$$ \frac{1}{\zeta(s)} = s \int_1^\infty \frac{M(x)}{x^{s+1}} \, dx $$

If the Mertens Conjecture $|M(x)| < \sqrt{x}$ were true, the integral on the right-hand side would converge for all $s$ with $\Re(s) > \frac{1}{2}$. By analytic continuation, this would dictate that $1/\zeta(s)$ is analytic in the half-plane $\Re(s) > \frac{1}{2}$, thereby proving that $\zeta(s)$ has no zeros in this region. This is exactly the statement of the Riemann Hypothesis (RH). In addition, the bound would imply that all non-trivial zeros of $\zeta(s)$ are simple (multiplicity of 1).

## 3. History & State of the Art (SOTA)

Thomas Joannes Stieltjes first claimed a proof of this conjecture in an 1885 letter to Charles Hermite, though he never published a formal proof. In 1897, Franz Mertens published a paper calculating $M(n)$ up to $10,000$ and formally stated the conjecture, drawing significant interest due to its direct link to the Riemann Hypothesis.

For nearly a century, the conjecture remained an open plausibility. In 1985, Andrew Odlyzko and Herman te Riele dramatically proved the conjecture false. They demonstrated rigorously that:
$$ \limsup_{x \to \infty} \frac{M(x)}{\sqrt{x}} > 1.06 \quad \text{and} \quad \liminf_{x \to \infty} \frac{M(x)}{\sqrt{x}} < -1.009 $$

This guarantees that $M(x)/\sqrt{x}$ takes on values greater than $1$ and less than $-1$ infinitely many times. Their breakthrough relied on applying the Lenstra-Lenstra-Lovász (LLL) lattice basis reduction algorithm to find linear dependencies among the imaginary parts of the first 2,000 non-trivial zeros of $\zeta(s)$. While they definitively proved the existence of counterexamples, their method was non-constructive and did not identify a specific integer $n$ that breaks the bound.

## 4. Partial Results / Verified Cases

Despite being false globally, the Mertens Conjecture holds true for all easily computable numbers. 
- **Exhaustive Verification:** Greg Hurst (2018) fully computed $M(n)$ up to $n = 10^{16}$ and confirmed that $|M(n)| < \sqrt{n}$ for every integer in this range.
- **Counterexample Bounds:** The search space for the first counterexample has been strictly bounded. Pintz (1987) proved that the first counterexample must occur below $\exp(3.21 \times 10^{64})$. This upper limit was drastically reduced by Kotnik and te Riele (2006), who proved that a counterexample must exist below $\exp(1.59 \times 10^{40})$.

## 5. Principal Obstacles

The primary bottleneck preventing the full resolution (i.e., finding an explicit counterexample) is the limitation of modern computational power combined with the mathematical nature of the Odlyzko-te Riele proof.

The original disproof formulates an approximation $h(y) = \sum_{j=1}^N c_j \cos(\gamma_j y - \alpha_j)$ that models the behavior of $M(e^y) e^{-y/2}$, where $\gamma_j$ are the imaginary parts of the zeros of the zeta function. Finding a value where this sum exceeds $1$ requires simultaneous Diophantine approximation to force the cosine terms to align near $1$. Standard analytic and perturbation techniques fail because the alignment occurs seemingly randomly and extremely rarely. Because the upper bound for the first occurrence is currently near $10^{40}$, iterating point-by-point to find the exact value is computationally impossible, and LLL basis reduction only guarantees the *existence* of an alignment interval, not its precise localized peak among integers.

## 6. The Gap

The boundary defining the current gap is the difference between an existential theorem and a constructive witness. We know definitively that the conjecture fails, and we know it holds for $n \le 10^{16}$, but the exact first integer $n$ for which $|M(n)| \ge \sqrt{n}$ remains completely unknown. Closing this mathematical gap requires crossing the computational barrier to explicitly construct the first counterexample. This will require fundamentally new mathematics that can pinpoint extreme values of the chaotic oscillations of the Mertens function without requiring a brute-force sweep of all integers up to $10^{40}$.

## 7. Current Research (as of June 2026)

Active research on the Mertens function follows two primary tracks:
1. **Computational:** Pushing the verification limit past $10^{16}$ and utilizing massive clusters to reduce the theoretical upper bound of the first counterexample. 
2. **Theoretical (Weak Mertens Conjecture):** Exploring relaxed boundaries. The Weak Mertens Conjecture asks whether $M(x) = \mathcal{O}(x^{1/2 + \epsilon})$ for every $\epsilon > 0$. This remains entirely open and is equivalent to the Riemann Hypothesis.
3. *(frontier — verify)* Recent preprints explore higher-dimensional lattice reduction algorithms (such as BKZ) utilizing the first $10^6$ zeros of $\zeta(s)$, hypothesizing that the upper bound for the first counterexample could be rigorously lowered below $\exp(10^{30})$.

## 8. Future Work

Leading mathematicians and computational number theorists suggest the following pathways:
- Refining simultaneous Diophantine approximation algorithms to extract explicit witnesses from trigonometric sums, bypassing the need for point-by-point numerical evaluation.
- Studying the pseudorandomness and statistical properties of the sequence $\mu(n)$ to understand the exact density and spacing of values where the normalized Mertens function crosses the $\pm 1$ threshold.
- Exploring the generalized Gonek-Hughes-Keating conjectures, which aim to bound the maximum order of magnitude of $M(x)$ using random matrix theory.

## 9. Key References

- **[Foundational]** Odlyzko, A. M., and te Riele, H. J. J. *The resolution of the Mertens conjecture.* Journal für die reine und angewandte Mathematik 357 (1985): 138-160.
- **[Foundational]** Mertens, F. *Über eine zahlentheoretische Funktion.* Sitzungsberichte der Kaiserlichen Akademie der Wissenschaften, Mathematisch-Naturwissenschaftliche Klasse 106 (1897): 761–830.
- **[SOTA / Recent]** Hurst, G. *Computations of the Mertens function and improved bounds on the Mertens conjecture.* Mathematics of Computation 87(310) (2018): 1013-1028.
- **[Survey]** Kotnik, T., and te Riele, H. *The Mertens conjecture revisited.* International Symposium on Algorithmic Number Theory (ANTS), Springer (2006): 156-167.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, we can manually evaluate the Mertens Conjecture for the small range $1 < n \le 10$. 

First, we determine the Möbius function $\mu(k)$ for each integer $k$ from $1$ to $10$:
- $\mu(1) = 1$
- $\mu(2) = -1$ (one prime factor: 2)
- $\mu(3) = -1$ (one prime factor: 3)
- $\mu(4) = 0$ (divisible by $2^2 = 4$)
- $\mu(5) = -1$ (one prime factor: 5)
- $\mu(6) = 1$ (two distinct prime factors: 2, 3)
- $\mu(7) = -1$ (one prime factor: 7)
- $\mu(8) = 0$ (divisible by $2^2 = 4$)
- $\mu(9) = 0$ (divisible by $3^2 = 9$)
- $\mu(10) = 1$ (two distinct prime factors: 2, 5)

Next, we construct the cumulative sum $M(n) = \sum_{k=1}^n \mu(k)$ and compare $|M(n)|$ to the square root boundary $\sqrt{n}$:
- **$n=2$:** $M(2) = 1 - 1 = 0 \implies |0| < 1.414$ *(True)*
- **$n=3$:** $M(3) = 0 - 1 = -1 \implies |-1| < 1.732$ *(True)*
- **$n=4$:** $M(4) = -1 + 0 = -1 \implies |-1| < 2.000$ *(True)*
- **$n=5$:** $M(5) = -1 - 1 = -2 \implies |-2| < 2.236$ *(True)*
- **$n=6$:** $M(6) = -2 + 1 = -1 \implies |-1| < 2.449$ *(True)*
- **$n=7$:** $M(7) = -1 - 1 = -2 \implies |-2| < 2.645$ *(True)*
- **$n=8$:** $M(8) = -2 + 0 = -2 \implies |-2| < 2.828$ *(True)*
- **$n=9$:** $M(9) = -2 + 0 = -2 \implies |-2| < 3.000$ *(True)*
- **$n=10$:** $M(10) = -2 + 1 = -1 \implies |-1| < 3.162$ *(True)*

For these initial values, the conjecture clearly holds. The Mertens function $M(n)$ exhibits microscopic, gentle oscillations ranging between $0, -1$, and $-2$, which are comfortably constrained by the growing $\sqrt{n}$ boundary. The immense complexity of the problem stems from the fact that this bound does not fail until $n$ becomes unimaginably large.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*