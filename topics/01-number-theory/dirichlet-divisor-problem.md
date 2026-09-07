---
id: 01-number-theory/dirichlet-divisor-problem
title: "Dirichlet Divisor Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dirichlet Divisor Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/dirichlet-divisor-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Dirichlet Divisor Problem asks for the optimal asymptotic bound on the error term in the sum of the divisor function.

Let $d(n)$ denote the number of positive divisors of an integer $n$. The sum of the divisor function up to a real number $x$ is denoted by $D(x)$:
$$D(x) = \sum_{n \le x} d(n)$$

Dirichlet (1849) proved that the asymptotic behavior of $D(x)$ is given by:
$$D(x) = x \log x + (2\gamma - 1)x + \Delta(x)$$
where $\gamma$ is the Euler-Mascheroni constant, and $\Delta(x)$ is an error term.

**The Conjecture:**
The Dirichlet Divisor Problem conjectures that the infimum of all real numbers $\theta$ such that $\Delta(x) = O(x^{\theta + \epsilon})$ for any $\epsilon > 0$ is exactly $\theta = 1/4$.
Equivalently, it asserts that for any $\epsilon > 0$:
$$\Delta(x) = O(x^{1/4 + \epsilon})$$

A complete proof requires demonstrating this upper bound. A disproof would require showing that the $\limsup$ of $|\Delta(x)| / x^{\theta}$ diverges for some $\theta > 1/4$.

## 2. Mathematical Foundations

The problem lies at the intersection of analytic number theory, harmonic analysis, and exponential sums.

**The Divisor Function:**
The divisor function $d(n)$ is a multiplicative arithmetic function defined as $d(n) = \sum_{d|n} 1$. It can also be expressed through the Riemann zeta function, as its Dirichlet series is exactly $\zeta^2(s)$:
$$\sum_{n=1}^\infty \frac{d(n)}{n^s} = \zeta^2(s) \quad \text{for } \Re(s) > 1$$

**Perron's Formula:**
The sum $D(x)$ can be represented analytically using Perron's formula, expressing the partial sums of the Dirichlet series as a contour integral over the complex plane:
$$D(x) = \frac{1}{2\pi i} \int_{c-i\infty}^{c+i\infty} \zeta^2(s) \frac{x^s}{s} \, ds$$
where $c > 1$. Shifting the contour to the left past the double pole at $s=1$ yields the main term $x \log x + (2\gamma - 1)x$ as the residue, leaving the error term $\Delta(x)$ bounded by the remaining integral, heavily linking the problem to the growth rate of $\zeta(s)$ in the critical strip $0 < \Re(s) < 1$.

**Voronoi's Identity:**
An alternative geometric and Fourier-analytic approach utilizes Voronoi's formula (1904), which provides an exact expression for the error term $\Delta(x)$ in terms of Bessel functions:
$$\Delta(x) = \frac{x^{1/4}}{\pi \sqrt{2}} \sum_{n=1}^\infty \frac{d(n)}{n^{3/4}} \cos\left(4\pi \sqrt{nx} - \frac{\pi}{4}\right) + O(x^{-1/4})$$
This identity transforms the problem into bounding highly oscillatory trigonometric sums.

## 3. History & State of the Art (SOTA)

The history of the problem is characterized by gradual, hard-won improvements to the exponent $\theta$:

- **1849:** Dirichlet introduced the problem, providing the trivial bound $\theta \le 1/2$ using the hyperbola method.
- **1903:** G. Voronoi reduced the bound to $\theta \le 1/3$ using his summation formula.
- **1915-1916:** G. H. Hardy and E. Landau independently proved the lower bound $\theta \ge 1/4$. Hardy demonstrated that $\Delta(x)$ is not $o(x^{1/4})$.
- **1922:** J. G. van der Corput introduced novel techniques for estimating exponential sums, reducing the bound to $\theta \le 33/100 = 0.33$.
- **1969-1982:** G. Kolesnik progressively refined van der Corput's method, culminating in $\theta \le 35/108 \approx 0.324$.
- **1988:** H. Iwaniec and C. J. Mozzochi introduced the Bombieri-Iwaniec method (using discrete geometry and the large sieve), achieving $\theta \le 7/22 \approx 0.318$.
- **2003:** M. N. Huxley refined the Bombieri-Iwaniec method using the "discrete Hardy-Littlewood method", achieving the current **State of the Art (SOTA)** bound of $\theta \le 131/416 \approx 0.3149$.
- **2017:** A preprint by J. Bourgain and N. Watt (arXiv:1709.04340) claimed an improvement to $\theta \le 517/1648 \approx 0.3137$ via decoupling theory. However, the authors subsequently **withdrew** the paper after discovering a critical technical gap in the application of Bourgain-Guth reduction theory. Thus, Huxley's 2003 bound remains the SOTA.

## 4. Partial Results / Verified Cases

While the general conjecture $\theta = 1/4$ remains open, there are specific domains and variations where the $1/4$ exponent or analogous tight bounds have been established:

- **Mean Square Bound:** While the pointwise bound on $\Delta(x)$ is highly elusive, Cramér (1922) proved that the conjecture holds "on average" in the mean square sense:
  $$\frac{1}{X} \int_1^X |\Delta(x)|^2 \, dx = O(X^{1/2})$$
  This strongly supports the heuristic that $\Delta(x) \approx x^{1/4}$ most of the time.
- **Function Field Analogue:** The analogue of the Dirichlet Divisor Problem for the ring of polynomials $\mathbb{F}_q[t]$ over a finite field has been completely resolved. The Riemann Hypothesis for curves over finite fields (proven by A. Weil) implies the equivalent bound of $\theta = 1/4$ in the function field setting.
- **Omega Results (Lower Bounds):** Following Hardy, more precise $\Omega$ (lower bound) results have been verified. Soundararajan (2003) proved that $\Delta(x) = \Omega( (x \log x)^{1/4} (\log \log x)^{(3+\log 4)/4} \exp(-c \sqrt{\log \log \log x}) )$, showing the exact nature of the oscillations preventing anything smaller than $1/4$.

## 5. Principal Obstacles

The fundamental barrier to achieving $\theta = 1/4$ lies in the limitations of current exponential sum estimation techniques.

The problem requires establishing massive cancellation in the Voronoi sum:
$$\sum_{N \le n \le 2N} d(n) e(2\sqrt{nx})$$
where $e(z) = e^{2\pi i z}$. 
- **Method of Exponent Pairs:** Classical methods (Weyl, van der Corput) rely on differentiating the phase function to approximate the sum via stationary phase. However, the sequence of "exponent pairs" generated by these methods strictly limits how much cancellation can be theoretically proven. It is a known structural limitation that the traditional method of exponent pairs cannot yield $\theta < 1/4$.
- **Bombieri-Iwaniec Barrier:** Modern methods convert the 1D exponential sum into a 2D sum (using rational approximations to the derivatives of the phase function). While this breaks the exponent pair barrier, it introduces a "spacing problem" (counting the number of integer points near a curve). Current discrete geometry techniques cannot bound this spacing problem tightly enough to reach $1/4$; they plateau around $131/416$.
- **Decoupling Limitations:** While Bourgain's decoupling theory revolutionized the related Lindelöf hypothesis for the Riemann zeta function, directly translating this to the divisor problem introduces phase cross-terms that currently resist decoupling-style bounds.

## 6. The Gap

The gap lies precisely between $\theta \le 131/416$ (proven) and $\theta = 1/4$ (conjectured). 
Mathematically, closing this gap requires a completely new mechanism to exploit the arithmetic nature of $d(n)$ within the Voronoi series. The current framework treats $d(n)$ almost purely analytically (by smoothing the sums). To cross the barrier at $\approx 0.3149$, researchers need a technique that accurately captures the deep algebraic correlation between the divisor function $d(n)$ and the highly oscillatory phase $e^{i 4\pi \sqrt{nx}}$ over exceptionally long ranges, beyond what the discrete Hardy-Littlewood method can track.

## 7. Current Research (as of June 2026)

Research approaches are currently bifurcated:
1. **Refining the Discrete Hardy-Littlewood Method:** Researchers are attempting to optimize the spacing problem in the Bombieri-Iwaniec-Huxley method using higher-dimensional incidence geometry, though gains here are expected to be microscopic (in the fourth decimal place).
2. **Decoupling and Efficient Congruencing:** Following Bourgain's success with the Riemann zeta function, groups are trying to modify $l^2$ decoupling theory to apply to the specific phase function $\sqrt{x}$ characteristic of the divisor problem. 
3. **Connections to Automorphic Forms:** *(frontier — verify)* The spectral theory of automorphic forms (e.g., via the Kuznetsov trace formula) naturally outputs sums similar to the Voronoi formula. Some researchers are attempting to embed the divisor problem into the spectral theory of $GL(2)$ to utilize Deligne's bounds on Kloosterman sums.

## 8. Future Work

Leading analytic number theorists suggest the following pathways:
- **Breaking the $131/416$ Barrier:** A major intermediate goal is to reach $\theta < 3/10 = 0.300$. This would psychologically and mathematically prove that a fundamentally new geometric or analytic tool has been successfully developed.
- **Understanding Large Values:** Further research is directed at understanding the large fluctuations of $\Delta(x)$. By studying the moments $\int_1^X |\Delta(x)|^k dx$ for $k > 2$, researchers hope to understand the rare events where the error term is unusually large, which dictates the pointwise upper bound.
- **The Gauss Circle Problem Link:** The Dirichlet Divisor Problem is deeply analogous to the Gauss Circle Problem (counting integer points in a circle). Future breakthroughs in one are universally expected to translate directly to the other due to the structural similarities of their underlying exponential sums.

## 9. Key References

- **[Foundational]** Voronoi, G. *Sur une fonction transcendante et ses applications à la sommation de quelques séries tirées de la théorie des nombres.* Annales Scientifiques de l'École Normale Supérieure, 1904.
- **[Foundational]** Hardy, G. H. *On Dirichlet's divisor problem.* Proceedings of the London Mathematical Society, 1916.
- **[SOTA / Recent]** Huxley, M. N. *Exponential Sums and Lattice Points III.* Proceedings of the London Mathematical Society, 2003.
- **[Survey]** Ivić, A. *The Riemann Zeta-Function: Theory and Applications.* Dover Publications, 2003. (Contains extensive discussion on the divisor problem and exponential sums).
- **[Survey]** Titchmarsh, E. C. (Revised by Heath-Brown, D. R.). *The Theory of the Riemann Zeta-Function.* Oxford University Press, 1986.

## 10. Worked Example / Concrete Special Case

To visualize the problem, we can manually compute $D(x)$ and the error term $\Delta(x)$ for a small value, say $x = 10$.

First, we calculate $d(n)$ for $n \in \{1, \dots, 10\}$:
- $d(1) = 1$ (divisors: 1)
- $d(2) = 2$ (divisors: 1, 2)
- $d(3) = 2$ (divisors: 1, 3)
- $d(4) = 3$ (divisors: 1, 2, 4)
- $d(5) = 2$ (divisors: 1, 5)
- $d(6) = 4$ (divisors: 1, 2, 3, 6)
- $d(7) = 2$ (divisors: 1, 7)
- $d(8) = 4$ (divisors: 1, 2, 4, 8)
- $d(9) = 3$ (divisors: 1, 3, 9)
- $d(10) = 4$ (divisors: 1, 2, 5, 10)

Summing these up gives the exact discrete value:
$$D(10) = 1 + 2 + 2 + 3 + 2 + 4 + 2 + 4 + 3 + 4 = 27$$

Now, we compute Dirichlet's main asymptotic term $M(x) = x \log x + (2\gamma - 1)x$ for $x = 10$. 
Using $\log(10) \approx 2.30258$ and $\gamma \approx 0.57721$:
$$M(10) = 10(2.30258) + (2(0.57721) - 1)(10)$$
$$M(10) = 23.0258 + (1.15442 - 1)(10) = 23.0258 + 1.5442 = 24.57$$

The error term $\Delta(10)$ is the difference between the exact sum and the main term:
$$\Delta(10) = D(10) - M(10) = 27 - 24.57 = 2.43$$

Dirichlet's $O(x^{1/2})$ bound suggests the error should scale roughly with $\sqrt{10} \approx 3.16$. Indeed, $2.43 < 3.16$. 
The conjecture states that for very large $x$, the error $\Delta(x)$ will be bounded by $O(x^{1/4})$, meaning the exact discrete sum $D(x)$ adheres astonishingly closely to the smooth continuous curve $M(x)$ as the scale increases.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*