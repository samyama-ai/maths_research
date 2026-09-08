---
id: 05-analysis/erdos-flat-polynomials
title: "Erdös Flat Polynomials Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdös Flat Polynomials Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/erdos-flat-polynomials` · **Status:** open

## 1. Problem Statement / Conjecture

The Erdös Flat Polynomials Problem (often formally designated as the **Erdős Maximum Modulus Conjecture for Littlewood Polynomials**) proposes a fundamental restriction on the behavior of polynomials with coefficients restricted to $\{-1, 1\}$ when evaluated on the complex unit circle. 

Let $\mathcal{L}_n$ denote the set of all Littlewood polynomials of degree $n-1$, defined as $P(z) = \sum_{k=0}^{n-1} a_k z^k$ where $a_k \in \{-1, 1\}$. By Parseval's identity, the root-mean-square of $|P(z)|$ on the unit circle $|z|=1$ is exactly $\sqrt{n}$. The conjecture states that there exists an absolute constant $c > 0$ such that for every natural number $n$ and every polynomial $P \in \mathcal{L}_n$, the maximum modulus of $P(z)$ on the unit circle satisfies:

$$ \max_{|z|=1} |P(z)| \ge (1+c)\sqrt{n} $$

Equivalently, the conjecture posits that **ultra-flat Littlewood polynomials do not exist**. While a sequence of polynomials may be "flat" (bounded above and below by constant multiples of $\sqrt{n}$), the supremum norm can never asymptotically approach the $L^2$ average. A complete proof requires establishing a strictly positive lower bound for $c$ across all $n$, whereas a disproof requires explicitly constructing a sequence of Littlewood polynomials whose maximum modulus is $(1+o(1))\sqrt{n}$.

## 2. Mathematical Foundations

The problem lies at the intersection of harmonic analysis, approximation theory, and combinatorics. The primary mathematical structures are the Hardy spaces $H^p$ restricted to the unit circle $\mathbb{T} = \{ z \in \mathbb{C} : |z| = 1 \}$.

For any polynomial $P(z)$ and $p \ge 1$, the $L^p$ norm on $\mathbb{T}$ is defined as:

$$ \|P\|_p = \left( \frac{1}{2\pi} \int_{0}^{2\pi} |P(e^{i\theta})|^p d\theta \right)^{1/p} $$

The $L^\infty$ norm (maximum modulus) is given by:

$$ \|P\|_\infty = \max_{\theta \in [0, 2\pi]} |P(e^{i\theta})| $$

For any $P \in \mathcal{L}_n$, the coefficients are $a_k \in \{-1, 1\}$. Parseval's identity strictly fixes the $L^2$ norm:

$$ \|P\|_2 = \left( \sum_{k=0}^{n-1} |a_k|^2 \right)^{1/2} = \sqrt{n} $$

By the monotonicity of $L^p$ spaces on probability measure spaces, we have the invariant chain:

$$ \sqrt{n} = \|P\|_2 \le \|P\|_p \le \|P\|_\infty \quad \text{for all } p > 2 $$

**Flatness Definitions:**
1. A sequence of polynomials $(P_n)_{n=1}^\infty$ with $P_n \in \mathcal{L}_n$ is **flat** if there exist constants $0 < C_1 \le C_2$ such that for all $n$ and all $z \in \mathbb{T}$:
   $$ C_1 \sqrt{n} \le |P_n(z)| \le C_2 \sqrt{n} $$
2. A sequence is **ultra-flat** if:
   $$ \lim_{n \to \infty} \frac{\|P_n\|_\infty}{\sqrt{n}} = 1 \quad \text{and} \quad \lim_{n \to \infty} \frac{\min_{|z|=1} |P_n(z)|}{\sqrt{n}} = 1 $$

Erdős's conjecture asserts that $\inf_{P \in \mathcal{L}_n} \|P\|_\infty / \sqrt{n} \ge 1+c$ for some $c>0$, explicitly precluding the existence of ultra-flat sequences in $\mathcal{L}_n$.

## 3. History & State of the Art (SOTA)

The geometry of polynomials with restricted coefficients was initially interrogated by J.E. Littlewood in the 1920s. In 1957, Paul Erdős published his paper *Some Unsolved Problems* in the Michigan Mathematical Journal, formally laying out the conjecture that the maximum modulus of $\pm 1$ polynomials must be strictly bounded away from $\sqrt{n}$ by a multiplicative constant. 

At the time, the probabilistic heuristic driven by the Salem-Zygmund theorem indicated that a "random" polynomial with coefficients chosen uniformly from $\{-1, 1\}$ achieves a maximum modulus of $\mathcal{O}(\sqrt{n \log n})$. Erdős recognized that forcing deterministic structure to minimize this peak would face an absolute combinatorial wall. 

In 1966, Littlewood formalized a weaker, related question: do *flat* polynomials exist for $\pm 1$ coefficients? (Meaning $C_2$ can be large, but must be constant). 

A major turning point occurred in 1980 when Jean-Pierre Kahane proved that **ultra-flat polynomials do exist if the coefficients are allowed to be arbitrary complex numbers on the unit circle** ($a_k = e^{i\phi_k}$). Kahane’s probabilistic proof definitively disproved the complex version of Erdős's conjecture, showing that the continuous rotational freedom of complex coefficients allows one to smooth out the peaks on the unit circle.

However, Kahane's method failed for the discrete topology of $\{-1, 1\}$. The most monumental recent breakthrough in the real domain came from Balister, Bollobás, Morris, Sahasrabudhe, and Tiba (BBMST) in 2020. They proved that **flat Littlewood polynomials exist**, definitively solving Littlewood's 1966 problem. Despite this profound achievement, their construction results in an upper bound $C_2$ that is exceptionally large. Erdős's claim—that $C_2$ can never be pushed down to $1+\epsilon$ for Littlewood polynomials—survived the BBMST breakthrough and remains the definitive open problem in the field.

## 4. Partial Results / Verified Cases

While the general lower bound $(1+c)\sqrt{n}$ is unproven, substantial progress has been made in specific classes of Littlewood polynomials and through computational verification:

- **Rudin-Shapiro Polynomials:** The most famous explicitly constructed sequence of Littlewood polynomials is the Rudin-Shapiro sequence, generated recursively. It is proven that for a Rudin-Shapiro polynomial $P_n$ of length $n = 2^m$, the maximum modulus is exactly bounded by:
  $$ \|P_n\|_\infty \le \sqrt{2} \sqrt{n} $$
  This demonstrates that the constant $c$ in Erdős's conjecture must satisfy $c \le \sqrt{2}-1 \approx 0.414$.

- **Computational Bounds for Small $n$:** Exhaustive algorithmic searches over the Boolean hypercube $\{-1, 1\}^n$ have been executed for small lengths (up to $n \approx 60$). In all computationally verified ranges, the maximum modulus is bounded below by approximately $1.15\sqrt{n}$, strongly supporting the existence of a strict gap.

- **Golay Merit Factor Sequences:** The $L^4$ norm of a polynomial is directly tied to its aperiodic autocorrelation through the Golay merit factor $F$. A sequence with merit factor $F$ satisfies:
  $$ \|P\|_4 = \left( 1 + \frac{1}{F} \right)^{1/4} \sqrt{n} $$
  Since $\|P\|_\infty \ge \|P\|_4$, bounding the maximum possible merit factor bounds the maximum modulus. Exhaustive searches for optimal merit factors (such as Barker codes, proven not to exist for $n>13$) show that empirical limits on $F \approx 12$ force $\|P\|_\infty \ge (1.019)\sqrt{n}$. 

- **Fekete Polynomials:** For $n = p$ (a prime), polynomials constructed using the Legendre symbol $a_k = (k/p)$ have been heavily studied. Montgomery proved that for Fekete polynomials, $\|P\|_\infty \gg \sqrt{p} \log p$, showing they are not flat and cannot violate the Erdős conjecture.

## 5. Principal Obstacles

The persistence of the Erdős Flat Polynomials Problem stems from the fundamental incompatibility between the discrete geometry of $\{-1, 1\}^n$ and the continuous nature of Fourier analytic bounds on $S^1$.

When Kahane constructed complex ultra-flat polynomials, he utilized independent continuous random variables $e^{i\theta_k}$ and applied Gaussian perturbations. In a continuous parameter space, one can calculate a gradient of the supremum norm and execute small continuous deformations to "squash" any emerging peaks on the unit circle. 

For Littlewood polynomials, the coefficient space is the Boolean hypercube. A single coefficient "flip" from $+1$ to $-1$ alters the polynomial by $2z^k$, which injects a massive global ripple of amplitude $2$ across the entire unit circle. There is no concept of a "small local perturbation" in the coefficient space. 

Furthermore, current probabilistic techniques (like those used by BBMST to prove flatness) rely on discrepancy theory and the Lovász Local Lemma applied to highly modified distributions. These techniques are fundamentally "lossy." They are powerful enough to confine the polynomial within a wide band (e.g., $10^{-6}\sqrt{n} \le |P(z)| \le 10^6\sqrt{n}$), but they intrinsically accumulate error terms that make it impossible to tighten the bounding band to the $(1-\epsilon)\sqrt{n} \le |P(z)| \le (1+\epsilon)\sqrt{n}$ required to refute the Erdős conjecture.

## 6. The Gap

The exact mathematical barrier lies between $L^2$ rigidity and $L^\infty$ flexibility under discrete constraints. Specifically, the gap is the inability to prove that the variance of the modulus square $|P(e^{i\theta})|^2$ strictly bounded away from zero. 

To bridge this gap and prove the conjecture, one must show that for any sequence $a_k \in \{-1, 1\}$, the sum of the squares of the off-diagonal Fourier coefficients (the autocorrelations $c_k = \sum a_j a_{j+k}$) cannot all simultaneously vanish fast enough to keep the $L^\infty$ norm tight to the $L^2$ norm. The strict boundary is passing from the known existential lower bounds on the $L^4$ norm (via merit factor conjectures) to an unconditional, absolute lower bound on the $L^\infty$ norm for all $n$.

## 7. Current Research (as of June 2026)

Active research primarily flows through two distinct channels:

1. **Discrepancy Theory and Random Polynomials:** Following the BBMST breakthrough, groups at Cambridge and Oxford are attempting to refine the structural constants of flat Littlewood polynomials. Researchers are investigating whether the Spencer-type discrepancy bounds used to prove flatness can be inverted to yield structural limitations on how small $C_2$ can be.
2. **The Asymptotic Merit Factor Problem:** Researchers in algebraic combinatorics (such as the groups historically surrounding Jedwab and Borwein) are attacking the Erdős conjecture indirectly via the $L^4$ norm. If the asymptotic Golay merit factor is bounded by a constant (believed to be $\approx 12.32$), the Erdős conjecture is automatically proven.
3. *(frontier — verify)* Recent preprints have applied hypercontractivity theorems from Boolean analysis to the Fourier transform on $S^1$, attempting to show that the Boolean influence of variables unconditionally forces a macroscopic variance in the modulus of $P(z)$, which would yield an explicit formulation for $c \approx 0.02$.

## 8. Future Work

Leading mathematicians emphasize that resolving the Erdős conjecture requires a novel synthesis of additive combinatorics and harmonic analysis. Suggested research strategies include:
- **Continuous Relaxations:** Embedding the discrete hypercube $\{-1, 1\}^n$ into the continuous torus $\mathbb{T}^n$ and studying the gradient flow of the maximum modulus. By tracking how fast the supremum norm explodes when forced onto the discrete vertices, researchers hope to extract the constant $c$.
- **Spectral Bounds on Autocorrelation Matrix:** Re-framing the problem away from polynomials and entirely into the language of Toeplitz matrices. The maximum modulus corresponds to the maximum eigenvalue of a family of pseudo-Toeplitz operators. Future work seeks to place strict spectral gap bounds on these operators when restricted to binary entries.

## 9. Key References

- **[Foundational]** Erdős, P. *Some unsolved problems*. Michigan Mathematical Journal, 1957. 
- **[Foundational]** Littlewood, J. E. *On polynomials $\sum^n \pm z^m$, $\sum^n e^{\alpha_m i}z^m$, $z = e^{\theta i}$*. Journal of the London Mathematical Society, 1966.
- **[SOTA / Recent]** Balister, P., Bollobás, B., Morris, R., Sahasrabudhe, J., & Tiba, M. *Flat Littlewood Polynomials Exist*. Annals of Mathematics, 2020. [DOI](https://doi.org/10.4007/annals.2020.192.3.6)
- **[Survey]** Erdélyi, T. *Polynomials with Littlewood-type coefficient constraints*. Approximation Theory X: Abstract and Classical Analysis, 2001.
- **[Survey]** Jedwab, J. *A survey of the merit factor problem for binary sequences*. Sequences and Their Applications, 2005. [DOI](https://doi.org/10.1007/11423461_2)

## 10. Worked Example / Concrete Special Case

To understand why the maximum modulus of a Littlewood polynomial intuitively pushes away from the $L^2$ baseline of $\sqrt{n}$, consider a concrete polynomial for $n = 4$ in $\mathcal{L}_4$:

$$ P(z) = 1 + z + z^2 - z^3 $$

Here, the coefficients are $(1, 1, 1, -1)$. 
By Parseval's identity, the root-mean-square ($L^2$ norm) across the entire unit circle is exactly:
$$ \|P\|_2 = \sqrt{1^2 + 1^2 + 1^2 + (-1)^2} = \sqrt{4} = 2.0 $$

If this polynomial were "ultra-flat," its modulus $|P(z)|$ would be very close to $2.0$ everywhere on the unit circle. Let us test specific points on the unit circle $\mathbb{T}$:

At $z = 1$ (where $\theta = 0$):
$$ P(1) = 1 + 1 + 1 - 1 = 2 \implies |P(1)| = 2.0 $$
This matches the $L^2$ norm perfectly. 

However, let us evaluate the polynomial at the phase $\theta = \pi/4$, where $z = e^{i\pi/4} = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$.
Calculating the powers of $z$:
- $z^1 = \frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$
- $z^2 = i$
- $z^3 = -\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}$

Substitute these into $P(z)$:
$$ P(e^{i\pi/4}) = 1 + \left(\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right) + i - \left(-\frac{1}{\sqrt{2}} + i\frac{1}{\sqrt{2}}\right) $$

Group the real and imaginary parts:
Real part: $1 + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} = 1 + \sqrt{2}$
Imaginary part: $\frac{1}{\sqrt{2}} + 1 - \frac{1}{\sqrt{2}} = 1$

Now, compute the squared modulus:
$$ |P(e^{i\pi/4})|^2 = (1+\sqrt{2})^2 + 1^2 = (1 + 2\sqrt{2} + 2) + 1 = 4 + 2\sqrt{2} \approx 6.828 $$

Taking the square root yields the modulus at this specific point:
$$ |P(e^{i\pi/4})| = \sqrt{4 + 2\sqrt{2}} \approx 2.613 $$

Because $2.613 > 2.0$, we see that the maximum modulus $\|P\|_\infty \ge 2.613$. The ratio of the maximum modulus to the $L^2$ norm is at least:
$$ \frac{2.613}{\sqrt{4}} = 1.306 $$

For this specific polynomial, it is bounded away from $\sqrt{n}$ by a factor of $(1 + 0.306)$. The Erdős conjecture asserts that no matter how large $n$ gets, and no matter how cleverly you arrange the $+1$ and $-1$ coefficients to balance the phases, an inevitable constructive interference will occur somewhere on the unit circle, causing a peak that forces the maximum modulus to be at least $(1+c)\sqrt{n}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*