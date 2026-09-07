---
id: 01-number-theory/extended-riemann-hypothesis
title: "Extended Riemann Hypothesis"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Extended Riemann Hypothesis

> **Topic:** Number Theory · **ID:** `01-number-theory/extended-riemann-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

The Extended Riemann Hypothesis (ERH) posits that for every Dirichlet character $\chi$ modulo $q$, all non-trivial zeros of the associated Dirichlet L-function $L(s, \chi)$ lie precisely on the "critical line" where the real part of the complex variable $s$ is equal to $1/2$. 

Formally, if $s = \sigma + it$ is a complex number such that $0 < \sigma < 1$ and $L(s, \chi) = 0$, then $\sigma = 1/2$.

A complete proof must unconditionally establish this constraint for all possible integer moduli $q \ge 1$ and all associated Dirichlet characters, eliminating the possibility of any zeros in the regions $0 < \sigma < 1/2$ and $1/2 < \sigma < 1$. 

## 2. Mathematical Foundations

Let $q \ge 1$ be an integer. A Dirichlet character modulo $q$ is a function $\chi: \mathbb{Z} \to \mathbb{C}$ that is completely multiplicative ($\chi(mn) = \chi(m)\chi(n)$), periodic with period $q$ ($\chi(n+q) = \chi(n)$), and satisfies $\chi(n) = 0$ if $\gcd(n, q) > 1$.

For a complex variable $s = \sigma + it$ with $\sigma > 1$, the Dirichlet L-function is defined by the absolutely convergent Dirichlet series:
$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$$

Because $\chi$ is completely multiplicative, it also admits an Euler product over prime numbers $p$:
$$L(s, \chi) = \prod_{p} \left( 1 - \frac{\chi(p)}{p^s} \right)^{-1}$$

When $\chi$ is the principal character $\chi_0$ modulo $q$ (where $\chi_0(n) = 1$ for all $n$ coprime to $q$), $L(s, \chi_0)$ differs from the Riemann zeta function $\zeta(s)$ only by a finite Euler factor and has a simple pole at $s = 1$. For all non-principal characters $\chi$, $L(s, \chi)$ is an entire function, meaning it is analytically continuable to the whole complex plane without poles.

Dirichlet L-functions satisfy a functional equation. For a primitive character $\chi$ modulo $q$, one defines the completed L-function:
$$\Lambda(s, \chi) = \left( \frac{q}{\pi} \right)^{(s+a)/2} \Gamma\left( \frac{s+a}{2} \right) L(s, \chi)$$
where $a = 0$ if $\chi(-1) = 1$ (an even character), $a = 1$ if $\chi(-1) = -1$ (an odd character), and $\Gamma$ is the Gamma function. The functional equation relates $s$ to $1-s$:
$$\Lambda(s, \chi) = \frac{\tau(\chi)}{i^a \sqrt{q}} \Lambda(1-s, \overline{\chi})$$
where $\tau(\chi) = \sum_{k=1}^q \chi(k) e^{2\pi i k / q}$ is the Gauss sum. The trivial zeros of $L(s, \chi)$ occur at the poles of the Gamma factor (at negative even or negative odd integers depending on parity). All other zeros are the "non-trivial" zeros, which are restricted by the functional equation to the critical strip $0 < \sigma < 1$.

## 3. History & State of the Art (SOTA)

Peter Gustav Lejeune Dirichlet originally introduced L-functions in 1837 to prove his theorem on the infinitude of primes in arithmetic progressions. In 1859, Bernhard Riemann proposed his famous hypothesis for the Riemann zeta function $\zeta(s)$. 

The explicit extension of Riemann's hypothesis to Dirichlet L-functions was formulated by Adolf Piltz in 1884 to study the deeper distribution properties of primes in arithmetic progressions. *(Note: The ERH is closely related to the Generalized Riemann Hypothesis (GRH). While historically GRH refers specifically to Dedekind zeta functions of algebraic number fields, modern literature often uses ERH and GRH interchangeably).*

If true, the ERH implies the best possible error term for the prime number theorem in arithmetic progressions:
$$\pi(x; q, a) = \frac{\text{li}(x)}{\phi(q)} + O\left(\sqrt{x} \log(qx)\right)$$
where $\pi(x; q, a)$ counts primes $p \le x$ with $p \equiv a \pmod q$, $\text{li}(x)$ is the Eulerian logarithmic integral, and $\phi(q)$ is Euler's totient function. 

Despite intense effort, the hypothesis remains fundamentally unproven. The most significant historical achievements remain the classical zero-free regions established by Charles de la Vallée Poussin (1896) and later refined by Carl Siegel (1935) and Arnold Walfisz (1936), which are incredibly narrow strips near $\sigma = 1$.

## 4. Partial Results / Verified Cases

While the ERH has not been fully proven for any single L-function, substantial partial and empirical results exist:

- **Classical Zero-Free Regions:** It is proven that $L(1+it, \chi) \ne 0$. Furthermore, there exists a constant $c > 0$ such that $L(\sigma+it, \chi) \ne 0$ in the region:
$$\sigma > 1 - \frac{c}{\log(q(|t|+2))}$$
with the single possible exception of a real zero (the "Siegel zero") when $\chi$ is a real (quadratic) character.
- **Positive Proportion:** Analytical sieve and mollification techniques have proven that a strict positive proportion of the non-trivial zeros of $L(s, \chi)$ lie exactly on the critical line $\sigma = 1/2$.
- **Computational Verification:** The ERH has been verified empirically for billions of zeros. Rigorous interval arithmetic computations by D. J. Platt (2014) mathematically verified the ERH for all odd moduli $q \le 400,000$ up to a height in the critical strip of $t \approx 10^8/q$.
- **Function Field Analogues:** The geometric analogue of the ERH—for L-functions associated with curves over finite fields—was definitively proven by Pierre Deligne in 1974 as a consequence of his resolution of the Weil Conjectures.

## 5. Principal Obstacles

The primary barrier to proving the ERH is the total failure of standard analytic and harmonic techniques to transition from the well-behaved half-plane $\sigma > 1$ to the highly oscillatory critical line $\sigma = 1/2$.

- **The Siegel Zero Problem:** For real Dirichlet characters, current analytic methods cannot definitively rule out the existence of a single real zero exceptionally close to $s=1$. The potential existence of this "Siegel zero" drastically weakens unconditional bounds and sabotages standard contour integration techniques.
- **Lack of Spectral Interpretation:** The Hilbert-Pólya conjecture suggests that the imaginary parts of the zeros $1/2 + i\gamma$ correspond to the eigenvalues of a self-adjoint operator in a suitable Hilbert space (which would guarantee $\gamma$ is purely real). Over finite fields, Deligne achieved this by interpreting zeros via the action of the Frobenius endomorphism on étale cohomology. No analogous cohomological theory or geometric space over $\mathbb{Z}$ has been successfully constructed.
- **The Analytic Wall:** Positivity arguments derived from the Euler product representation strictly control the behavior of $L(s, \chi)$ for $\sigma > 1$. However, upon analytic continuation into the critical strip, this multiplicative structure is lost to additive oscillations that resist traditional bounding techniques like the large sieve or Fourier analysis.

## 6. The Gap

The gap between current unconditional knowledge and a full proof is staggering. Unconditionally, we only know that zeros are repelled infinitesimally from the boundaries $\sigma = 0$ and $\sigma = 1$ (except for the possible Siegel zero). The ERH demands proving that the vast, infinite regions of $0 < \sigma < 1/2$ and $1/2 < \sigma < 1$ are completely empty of zeros. Crossing this gap requires a radically new mathematical framework that imposes rigid geometric or algebraic constraints on the complex roots of L-functions.

## 7. Current Research (as of June 2026)

Research on the ERH spans several interconnected, highly active disciplines:

- **Random Matrix Theory (RMT):** Initiated by Montgomery, Katz, and Sarnak, RMT models the statistical distribution of the zeros of families of L-functions using the eigenvalues of matrices drawn from classical compact groups (e.g., Unitary, Symplectic). This accurately predicts precise moments and spacings of L-functions on the critical line.
- **Arithmetic Geometry and $\mathbb{F}_1$:** Schools of thought led by Connes, Consani, and others are attempting to construct non-commutative geometries or algebraic schemes over the "field with one element" ($\mathbb{F}_1$) to replicate the geometric setting of the Weil conjectures for $\mathbb{Z}$.
- **Decoupling and L-function Bounds:** Utilizing recent breakthroughs in harmonic analysis (such as Bourgain-Demeter decoupling), researchers are establishing sharper subconvexity bounds for Dirichlet L-functions, restricting the growth of the functions deep within the critical strip.
- **Siegel Zero Elimination:** Incremental progress continues in unconditionally pushing the theoretical boundary of the Siegel zero. *(frontier — verify)* Recent preprints frequently claim minor improvements to the effective constants in Siegel's theorem using shifted convolution sums and new sieve parity bounds, though complete elimination remains unachieved.

## 8. Future Work

Future strategies consistently articulated by leading mathematicians include:
- Finding a unified approach to unconditionally rule out the Siegel zero, possibly by exploiting the positivity of complicated polynomials within the Weil explicit formula.
- Expanding the Katz-Sarnak Random Matrix heuristics from asymptotic statistical predictions to rigid, rigorous structural constraints on the zeros of individual L-functions.
- Discovering a suitable étale-like cohomology theory for arithmetic schemes over $\text{Spec}(\mathbb{Z})$ that yields a trace formula mirroring the Lefschetz trace formula, thereby constructing the elusive Hilbert-Pólya operator.

## 9. Key References

- **[Foundational]** Piltz, A. *Über die Häufigkeit der Primzahlen in arithmetischen Progressionen und über verwandte Gesetze*. Habilitationsschrift, Jena, 1884.
- **[Foundational]** Davenport, H. *Multiplicative Number Theory*. Springer Graduate Texts in Mathematics, 3rd Edition, 2000.
- **[SOTA / Recent]** Platt, D. J. *Computing degree 1 L-functions rigorously*. LMS Journal of Computation and Mathematics, 17(1), 282-308, 2014.
- **[Survey]** Iwaniec, H., & Kowalski, E. *Analytic Number Theory*. American Mathematical Society Colloquium Publications, Vol. 53, 2004.
- **[Survey]** Katz, N. M., & Sarnak, P. *Zeroes of zeta functions and symmetry*. Bulletin of the American Mathematical Society, 36(1), 1-26, 1999.

## 10. Worked Example / Concrete Special Case

Consider the simplest non-principal Dirichlet character, which is the unique non-trivial character modulo $4$. We denote it $\chi_1$. Its values are assigned by periodicity and relative primality to 4:
$$\chi_1(1) = 1, \quad \chi_1(2) = 0, \quad \chi_1(3) = -1, \quad \chi_1(4) = 0$$

The associated Dirichlet L-function is defined by the series:
$$L(s, \chi_1) = \sum_{n=1}^\infty \frac{\chi_1(n)}{n^s} = 1 - \frac{1}{3^s} + \frac{1}{5^s} - \frac{1}{7^s} + \frac{1}{9^s} - \dots$$

For $s = 1$, this converges conditionally to the famous Gregory-Leibniz series:
$$L(1, \chi_1) = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots = \frac{\pi}{4}$$
Because $L(1, \chi_1) \ne 0$, it satisfies the unconditionally proven non-vanishing of $L$-functions at $\sigma = 1$, which algebraically confirms that primes are equally distributed asymptotically between the congruence classes $p \equiv 1 \pmod 4$ and $p \equiv 3 \pmod 4$.

The Euler product for this L-function elegantly partitions the primes by these classes:
$$L(s, \chi_1) = \prod_{p \equiv 1 \text{ (mod } 4)} \left(1 - \frac{1}{p^s}\right)^{-1} \prod_{p \equiv 3 \text{ (mod } 4)} \left(1 + \frac{1}{p^s}\right)^{-1}$$

The Extended Riemann Hypothesis applied specifically to $L(s, \chi_1)$ states that if $L(\sigma + it, \chi_1) = 0$ for a complex number inside the critical strip $0 < \sigma < 1$, then its real part must be exactly $\sigma = 1/2$. 

Rigorous computational methods confirm this constraint for the lower spectrum: the first, lowest-lying non-trivial zeros of $L(s, \chi_1)$ occur at exactly $s = 1/2 \pm i \gamma_1$, where $\gamma_1 \approx 6.02094$. Discovering a single zero for $L(s, \chi_1)$ with a real part off this line—for instance, at $\sigma = 0.51$—would immediately completely disprove the ERH.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*