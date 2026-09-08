---
id: 01-number-theory/hardy-littlewood-first-tuple-conjecture
title: "Hardy-Littlewood First Tuple Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hardy-Littlewood First Tuple Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/hardy-littlewood-first-tuple-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Hardy-Littlewood First Tuple Conjecture (also known as the Prime Tuple Conjecture) provides a precise asymptotic formula for the distribution of prime constellations. 

Let $\mathcal{H} = (h_1, h_2, \dots, h_k)$ be a $k$-tuple of distinct non-negative integers. A prime tuple occurs at an integer $n$ if all shifted values $n+h_1, n+h_2, \dots, n+h_k$ are prime numbers. 

The conjecture states that if $\mathcal{H}$ is *admissible* (meaning there is no prime $p$ such that the elements of $\mathcal{H}$ cover all possible residue classes modulo $p$), then the number of integers $n \le x$ for which $(n+h_1, n+h_2, \dots, n+h_k)$ are all prime, denoted by $\pi(x; \mathcal{H})$, satisfies the asymptotic relation:

$$ \pi(x; \mathcal{H}) \sim \mathfrak{S}(\mathcal{H}) \int_2^x \frac{dt}{(\ln t)^k} $$

as $x \to \infty$. Here, $\mathfrak{S}(\mathcal{H})$ is the *singular series*, a constant dependent only on the tuple $\mathcal{H}$, which governs the local probability of the tuple elements being prime simultaneously. A complete proof requires establishing this asymptotic limit for all admissible $k$-tuples.

## 2. Mathematical Foundations

The conjecture relies on the fundamental theorem of arithmetic, modular arithmetic, and the asymptotic distribution of primes.

**Admissibility:** Let $\nu_{\mathcal{H}}(p)$ denote the number of distinct residue classes modulo $p$ occupied by the elements of $\mathcal{H}$:
$$ \nu_{\mathcal{H}}(p) = \left| \{ h_i \pmod p \mid 1 \le i \le k \} \right| $$
A tuple $\mathcal{H}$ is called **admissible** if $\nu_{\mathcal{H}}(p) < p$ for all prime numbers $p$. If $\nu_{\mathcal{H}}(p) = p$ for some prime $p$, then for any integer $n$, at least one of $n+h_1, \dots, n+h_k$ must be a multiple of $p$, preventing them from all being prime (except possibly for finitely many $n$), making the tuple inadmissible.

**Singular Series:** If $\mathcal{H}$ is admissible, the singular series $\mathfrak{S}(\mathcal{H})$ is defined as an infinite Euler product over all primes $p$:
$$ \mathfrak{S}(\mathcal{H}) = \prod_{p} \left( 1 - \frac{1}{p} \right)^{-k} \left( 1 - \frac{\nu_{\mathcal{H}}(p)}{p} \right) $$
This product encodes the local conditions. The term $(1 - 1/p)^k$ represents the probability that $k$ independent, random integers are not divisible by $p$, while $(1 - \nu_{\mathcal{H}}(p)/p)$ represents the actual probability that none of $n+h_1, \dots, n+h_k$ is divisible by $p$.

The integral $\int_2^x \frac{dt}{(\ln t)^k}$ naturally generalizes the logarithmic integral function $\text{Li}(x)$, representing the global density of primes.

## 3. History & State of the Art (SOTA)

The conjecture was formulated in 1923 by G. H. Hardy and J. E. Littlewood in their seminal paper "Some problems of 'Partitio numerorum'". It was a monumental generalization of the Prime Number Theorem and the Twin Prime Conjecture, introducing the circle method as a heuristic tool for linear prime equations.

In 1962, Paul T. Bateman and Roger A. Horn vastly generalized this to the Bateman-Horn conjecture, which considers values of sets of polynomials evaluated at prime arguments, rather than just linear shifts $n+h_i$.

Historically, progress toward proving the conjecture for $k \ge 2$ has been slow. A massive breakthrough occurred in the 21st century regarding *bounded gaps* between primes. In 2013, Yitang Zhang proved that there exist infinitely many prime pairs separated by at most 70,000,000. Soon after, James Maynard and Terence Tao independently developed a multi-dimensional sieve method proving that for any $m$, there exist infinitely many intervals of bounded length containing at least $m$ primes. This effectively proved that a positive proportion of admissible tuples contain infinitely many prime instantiations, although it falls short of proving the exact asymptotic for any specific chosen tuple.

## 4. Partial Results / Verified Cases

- **$k=1$:** When $\mathcal{H} = (0)$, the singular series $\mathfrak{S}(\mathcal{H}) = 1$. The conjecture exactly recovers the Prime Number Theorem ($\pi(x) \sim \text{Li}(x)$), proven in 1896 by Hadamard and de la Vallée Poussin.
- **Average results:** While the asymptotic for a single specific tuple $\mathcal{H}$ where $k \ge 2$ is unknown, average versions of the Hardy-Littlewood conjecture over many tuples of length $k$ have been proven to be consistent with the conjecture, relying on the Elliott-Halberstam conjecture or unconditional bounds (like the Bombieri-Vinogradov theorem).
- **Upper bounds:** Sieve methods (such as the Selberg sieve) unconditionally prove an upper bound for the conjecture that is correct up to a constant factor. That is, $\pi(x; \mathcal{H}) \ll \mathfrak{S}(\mathcal{H}) \frac{x}{(\ln x)^k}$.
- **Computational Verification:** The formula has been empirically verified to incredible precision. For example, for twin primes ($k=2$), triplets ($k=3$), and quadruplets ($k=4$), the predicted counts match actual prime counts up to $x = 10^{18}$ and beyond, with the error term behaving similarly to $O(x^{1/2+\epsilon})$.

## 5. Principal Obstacles

The primary barrier preventing the resolution of this conjecture is the **parity problem**, first identified by Atle Selberg. Standard sieve methods operate by tracking divisibility conditions. However, the Möbius function $\mu(n)$, which determines whether an integer has an even or odd number of prime factors, cannot be accurately bounded or distinguished using purely divisibility-based sieve methods. Because primes have exactly one prime factor (which is odd parity), and sieve methods cannot break the "parity barrier", they can at best yield "almost primes" (numbers with at most 2 or 3 prime factors, such as in Chen's Theorem) rather than strict primes.

Furthermore, the Hardy-Littlewood circle method, which successfully proves the asymptotic for additive problems with sufficiently many variables (like Vinogradov's proof of the weak Goldbach conjecture for 3 primes), fails for linear equations of the form $p_i = n + h_i$. The equations lack the necessary degrees of freedom (we have $k$ constraints but only 1 free variable $n$) for the minor arcs in the Fourier analytic setup to be bounded strictly below the major arcs.

## 6. The Gap

The exact boundary of human mathematical knowledge is the gap between the *Maynard-Tao existence theorem* and *tuple-specific asymptotics*. We know that for any large integer $m$, there is *some* admissible tuple of length $k \gg m e^{2m}$ that generates infinitely many prime tuples. However, we cannot pinpoint *which* tuple it is, nor can we prove that a *specific* narrow tuple like $\mathcal{H}=(0, 2)$ (twin primes) operates infinitely often. The gap requires a fundamentally new analytic or algebraic method that bypasses the parity problem to isolate individual primes rather than weight-averaged clusters of primes.

## 7. Current Research (as of June 2026)

Current research operates along several highly technical fronts:
- **Higher-order Fourier Analysis:** Expanding on the Green-Tao theorem (which established arbitrarily long arithmetic progressions in primes), researchers are using nilsequences and Gowers uniformity norms to capture the behavior of the von Mangoldt function $\Lambda(n)$ in linear systems. 
- **Sieve Refinements:** Generalizations of the Maynard-Tao multi-dimensional sieve weights are continuously optimized to lower the upper bound for bounded prime gaps. 
- **Connections to $L$-functions:** Proving subconvexity bounds and zero-density estimates for Dirichlet $L$-functions.
- *(frontier — verify)* Recent preprints explore using algebraic geometry over $\mathbb{F}_p(t)$ (function fields) to identify geometric analogues of the parity barrier, hoping to pull structural insights back to the integers $\mathbb{Z}$.

## 8. Future Work

Leading analytic number theorists point toward the Elliott-Halberstam (EH) conjecture as the most crucial stepping stone. If the EH conjecture (or its generalized forms) can be proven, the error terms in the distribution of primes in arithmetic progressions would be drastically minimized, allowing sieve methods to push much closer to $k$-tuple bounds. Additionally, breaking the parity problem will require injecting new arithmetic information—such as modular forms or automorphic representations—into sieve weights to distinguish primes from numbers with two prime factors.

## 9. Key References

- **[Foundational]** Hardy, G. H., & Littlewood, J. E. *Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes.* Acta Mathematica, 1923. [DOI](https://doi.org/10.1007/bf02403921)
- **[Foundational]** Bateman, P. T., & Horn, R. A. *A heuristic asymptotic formula concerning the distribution of prime numbers.* Mathematics of Computation, 1962. [DOI](https://doi.org/10.1090/s0025-5718-1962-0148632-7)
- **[SOTA / Recent]** Zhang, Y. *Bounded gaps between primes.* Annals of Mathematics, 2014.
- **[SOTA / Recent]** Maynard, J. *Small gaps between primes.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)
- **[Survey]** Granville, A. *Primes in intervals of bounded length.* Bulletin of the American Mathematical Society, 2015. [DOI](https://doi.org/10.1090/s0273-0979-2015-01480-1)
- **[Survey]** Soundararajan, K. *Small gaps between prime numbers: The work of Goldston-Pintz-Yıldırım.* Bulletin of the American Mathematical Society, 2007.

## 10. Worked Example / Concrete Special Case

Consider the famous Twin Prime Conjecture, which is the Hardy-Littlewood First Tuple Conjecture for $k=2$ with the tuple $\mathcal{H} = (0, 2)$. 

We wish to count the number of twin primes $(p, p+2)$ up to $x$.
First, we verify **admissibility**:
- For $p=2$: The elements of $\mathcal{H}$ modulo $2$ are $\{0 \pmod 2, 2 \pmod 2\} \equiv \{0\}$. Thus, $\nu_{\mathcal{H}}(2) = 1$. Since $1 < 2$, it is admissible at $p=2$.
- For $p > 2$: The elements $\{0, 2\}$ occupy at most 2 distinct residue classes modulo $p$. Thus $\nu_{\mathcal{H}}(p) \le 2 < p$, so it is admissible for all odd primes.

Next, we calculate the **singular series** $\mathfrak{S}(\mathcal{H})$:
$$ \mathfrak{S}(\mathcal{H}) = \prod_{p} \left( 1 - \frac{1}{p} \right)^{-2} \left( 1 - \frac{\nu_{\mathcal{H}}(p)}{p} \right) $$

Split the product into $p=2$ and $p>2$:
- For $p=2$, the factor is: $\left(1 - \frac{1}{2}\right)^{-2} \left(1 - \frac{1}{2}\right) = \left(\frac{1}{2}\right)^{-1} = 2$.
- For $p>2$, $\nu_{\mathcal{H}}(p) = 2$, so the factor is: $\left(1 - \frac{1}{p}\right)^{-2} \left(1 - \frac{2}{p}\right) = \frac{1 - 2/p}{(1 - 1/p)^2} = \frac{p(p-2)}{(p-1)^2}$.

Thus, the singular series evaluates to the celebrated **Twin Prime Constant** $C_2$:
$$ \mathfrak{S}(\mathcal{H}) = 2 \prod_{p \ge 3} \frac{p(p-2)}{(p-1)^2} \approx 2 \times 0.6601618... \approx 1.3203236 $$

The Hardy-Littlewood conjecture then provides the striking prediction that the number of twin primes up to $x$, denoted $\pi_2(x)$, is:
$$ \pi_2(x) \sim 2 C_2 \int_2^x \frac{dt}{(\ln t)^2} $$
This theoretical integral precisely matches the empirical counts of twin primes discovered by modern supercomputers.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*