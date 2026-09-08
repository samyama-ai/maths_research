---
id: 01-number-theory/elliott-halberstam-conjecture
title: "Elliott-Halberstam Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Elliott-Halberstam Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/elliott-halberstam-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Elliott-Halberstam conjecture concerns the distribution of prime numbers in arithmetic progressions. By Dirichlet's theorem, we know that prime numbers are asymptotically evenly distributed among the coprime residue classes modulo any integer $q$. The conjecture quantifies the average error in this approximation over a wide range of moduli $q$.

Let $\pi(x; q, a)$ denote the number of prime numbers less than or equal to $x$ that are congruent to $a$ modulo $q$. The expected number of such primes is $\frac{\text{Li}(x)}{\phi(q)}$, where $\text{Li}(x) = \int_2^x \frac{dt}{\ln t}$ is the logarithmic integral function and $\phi(q)$ is Euler's totient function.

Define the error term for a specific arithmetic progression as:
$$ E(x; q, a) = \pi(x; q, a) - \frac{\text{Li}(x)}{\phi(q)} $$
and the maximum absolute error over all coprime residue classes modulo $q$ as:
$$ E(x; q) = \max_{\substack{1 \le a \le q \\ \gcd(a, q) = 1}} \left| E(x; q, a) \right| $$

**The Elliott-Halberstam Conjecture (EH($\vartheta$)):**
For every $\vartheta \in (0, 1)$ and every $A > 0$, there exists a constant $C > 0$ such that:
$$ \sum_{q \le x^\vartheta} E(x; q) \le \frac{C x}{(\ln x)^A} $$
for all $x \ge 2$.

Informally, the conjecture states that the primes are uniformly distributed in arithmetic progressions for moduli $q$ almost as large as $x$, specifically up to $x^\vartheta$ for any $\vartheta < 1$, on average.

## 2. Mathematical Foundations

The conjecture relies on the algebraic structures of residue classes and analytic functions governing prime distributions. 

**Euler's Totient Function $\phi(q)$:** The number of positive integers up to $q$ that are relatively prime to $q$. This is the order of the multiplicative group of integers modulo $q$, denoted $(\mathbb{Z}/q\mathbb{Z})^\times$.

**Logarithmic Integral $\text{Li}(x)$:**
$$ \text{Li}(x) = \int_{2}^{x} \frac{dt}{\ln t} \sim \frac{x}{\ln x} $$
By the Prime Number Theorem, $\pi(x) \sim \text{Li}(x)$.

**Prime Number Theorem in Arithmetic Progressions:**
For a fixed $q$ and $\gcd(a,q)=1$:
$$ \pi(x; q, a) \sim \frac{\text{Li}(x)}{\phi(q)} \quad \text{as } x \to \infty $$

**Siegel-Walfisz Theorem:**
For any $A > 0$, there exists a constant $C_A > 0$ such that if $q \le (\ln x)^A$ and $\gcd(a,q)=1$, then:
$$ \left| \pi(x; q, a) - \frac{\text{Li}(x)}{\phi(q)} \right| \le C_A x \exp\left(-c \sqrt{\ln x}\right) $$
for some absolute constant $c > 0$. This provides a strong asymptotic for small moduli, but is highly restrictive compared to the polynomial bounds in the Elliott-Halberstam conjecture.

## 3. History & State of the Art (SOTA)

- **1965 (Bombieri and Vinogradov):** Independently proved the Bombieri-Vinogradov theorem, which establishes that the Elliott-Halberstam conjecture holds unconditionally for any $\vartheta < 1/2$. This is often described as the primes having a "level of distribution" of $1/2$.
- **1968 (Elliott and Halberstam):** Proposed the conjecture, predicting that the level of distribution extends up to $\vartheta = 1$. It was originally posed that the bound holds for the full range up to $x / (\ln x)^A$, but later refined to $x^\vartheta$ for strictly $\vartheta < 1$.
- **1989 (Friedlander and Granville):** Demonstrated that the conjecture is definitively false at the endpoint $\vartheta = 1$. They proved that $\sum_{q \le x} E(x; q)$ grows much faster than $x / (\ln x)^A$, meaning the range must be restricted to $\vartheta < 1$.
- **2005 (Goldston, Pintz, Yıldırım - GPY):** Showed that if the Elliott-Halberstam conjecture is true for *any* $\vartheta > 1/2$, then there exist infinitely many pairs of primes within a bounded distance of each other (a massive step toward the Twin Prime Conjecture).
- **2013 (Yitang Zhang):** Proved a weak variant of the Elliott-Halberstam conjecture for $\vartheta = 1/2 + 1/1168$, restricted to "smooth" moduli (moduli without large prime factors). This unconditional breakthrough was sufficient to establish bounded gaps between primes without assuming any unproven conjectures.
- **2015 (James Maynard & Polymath8b):** Using a multidimensional sieve approach, Maynard showed that bounded gaps exist unconditionally (recovering and improving Zhang's work). Furthermore, assuming a Generalized Elliott-Halberstam Conjecture (GEH), the Polymath8 project established that $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 6$.

## 4. Partial Results / Verified Cases

The conjecture is proven for the parameter space $\vartheta < 1/2$.
Specifically, the **Bombieri-Vinogradov Theorem** states that for any $A > 0$, there exists $B > 0$ such that:
$$ \sum_{q \le \frac{x^{1/2}}{(\ln x)^B}} \max_{y \le x} \max_{\gcd(a,q)=1} \left| \pi(y; q, a) - \frac{\text{Li}(y)}{\phi(q)} \right| \ll_A \frac{x}{(\ln x)^A} $$

Furthermore, **Zhang's Theorem (2013)** and the subsequent **Polymath8a** project verified the conjecture beyond $1/2$ (up to $\vartheta = 1/2 + 7/300$), provided the sum is restricted to $q$ that are $y$-smooth (meaning all prime factors of $q$ are less than $y$, for $y = x^\delta$).

The **Barban-Davenport-Halberstam Theorem** provides another partial result by evaluating the mean square error instead of the maximum error. It shows that for $Q \le x / (\ln x)^B$:
$$ \sum_{q \le Q} \sum_{\substack{a=1 \\ \gcd(a,q)=1}}^{q} \left( \pi(x; q, a) - \frac{\text{Li}(x)}{\phi(q)} \right)^2 \ll x Q \ln x + \frac{x^2}{(\ln x)^A} $$
which holds for moduli up to $Q = x$, demonstrating that on average in the mean-square sense, the error is well-controlled even for large $q$.

## 5. Principal Obstacles

The fundamental barrier preventing the resolution of the Elliott-Halberstam conjecture is the $\vartheta = 1/2$ threshold, often referred to as the "square-root barrier."

1. **Parity Problem in Sieve Theory:** Classical sieve methods (like the Selberg sieve) cannot distinguish between integers with an even number of prime factors and those with an odd number of prime factors. Resolving EH($\vartheta$) for $\vartheta > 1/2$ requires effectively breaking the parity barrier for general sequences.
2. **Type-I, Type-II, and Type-III Sums:** The error term in prime distributions is evaluated using combinatorial identities (like Vaughan's identity or Heath-Brown's identity), decomposing the von Mangoldt function into bilinear and trilinear forms. For $q > x^{1/2}$, the critical "Type-II" bilinear sums (involving sequences $a_m$ and $b_n$ of lengths roughly $x^{1/2}$) fall out of the effective range of the Cauchy-Schwarz inequality and standard estimates for multidimensional Kloosterman sums.
3. **Siegel Zeros:** Exceptional, hypothetical real zeros of Dirichlet $L$-functions very close to $s = 1$ cause standard error estimates to balloon. While the Bombieri-Vinogradov theorem cleverly avoids the Siegel zero problem by averaging over $q$, pushing past $1/2$ without restrictions often re-introduces the vulnerability to these ineffective bounds.

## 6. The Gap

The exact boundary separating what is unconditionally proven from the general statement is the transition from $\vartheta \le 1/2$ (unconditional via Bombieri-Vinogradov) to any $\vartheta > 1/2$ for *all* moduli. 

While Zhang crossed the $1/2$ barrier, he explicitly avoided the hardest parts of the Type-III sums by restricting to smooth moduli (where the factorizations allow for alternative combinatorial rearrangements). The gap that must be crossed is proving the necessary bounds for bilinear forms over finite fields or bounding short character sums without relying on the prime factorization structure of the modulus $q$. Crossing this gap for general moduli would immediately imply a host of results regarding primes, particularly bounded gaps of width 16 or 6.

## 7. Current Research (as of June 2026)

Active research in analytic number theory aims to extend the smooth moduli results and bypass the strict $1/2$ barrier by importing tools from algebraic geometry and automorphic forms.

- **Multidimensional Kloosterman Sums:** Generalizations of the Weil bound and Deligne's work on the Riemann Hypothesis over finite fields to higher-dimensional algebraic varieties are being explored to directly attack the Type-III sums.
- **Automorphic Methods:** Using the spectral theory of automorphic forms (following the work of Iwaniec, Friedlander, and Kowalski) to understand the distribution of error terms on average.
- **Polymath and Collaborative Sieve Enhancements:** Building upon the multi-dimensional sieve introduced by Maynard to extract smaller gap bounds, researchers are probing whether a slight strengthening of the sieve can simulate the effect of EH($\vartheta > 1/2$) unconditionally.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- Expanding the class of moduli for which $\vartheta > 1/2$ holds beyond smooth numbers to "almost all" integers.
- Establishing an unconditional resolution of the Generalized Elliott-Halberstam (GEH) conjecture for $\vartheta = 1/2 + \varepsilon$, which concerns the distributions of primes in progressions weighted by higher-order divisor functions.
- Investigating the statistical distribution of the normalized error terms $E(x; q, a) / \sqrt{x / \phi(q)}$ to formulate precise probabilistic models that guide rigorous analytic bounds.

## 9. Key References

- **[Foundational]** Elliott, P. D. T. A., and Halberstam, H. *A Conjecture in Prime Number Theory*. Symposia Mathematica, Vol. 4 INDAM, Rome, pp. 59-72, 1968.
- **[Foundational]** Bombieri, E. *On the large sieve*. Mathematika, 12(2): 201–225, 1965.
- **[Foundational]** Friedlander, J., and Granville, A. *Limitations to the equi-distribution of primes I*. Annals of Mathematics, 129(2): 363-382, 1989. [DOI](https://doi.org/10.2307/1971450)
- **[SOTA / Recent]** Zhang, Y. *Bounded gaps between primes*. Annals of Mathematics, 179(3): 1121-1174, 2014.
- **[SOTA / Recent]** Maynard, J. *Small gaps between primes*. Annals of Mathematics, 181(1): 383-413, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)
- **[Survey]** Granville, A. *Primes in intervals of bounded length*. Bulletin of the American Mathematical Society, 52(2): 171-222, 2015. [DOI](https://doi.org/10.1090/s0273-0979-2015-01480-1)

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, consider the distribution of primes up to $x = 100$ for the modulus $q = 3$. We want to compute the error term $E(100; 3)$.

First, note $\phi(3) = 2$. The coprime residue classes modulo 3 are $a = 1$ and $a = 2$.
The number of primes up to $x=100$ is $\pi(100) = 25$. 
According to Dirichlet's theorem, we expect primes to be roughly split equally among the 2 residue classes.

Let us count $\pi(100; 3, a)$ manually:
- Primes $\equiv 1 \pmod 3$: 7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97. (Total: 11)
- Primes $\equiv 2 \pmod 3$: 2, 5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89. (Total: 13)
- The prime 3 divides the modulus, so it is not in a coprime residue class.

The total expected number of primes in each class based on the logarithmic integral $\text{Li}(100) \approx \pi(100) = 25$ is approximately $25 / 2 = 12.5$.
The error terms for each class are:
$$ E(100; 3, 1) = 11 - 12.5 = -1.5 $$
$$ E(100; 3, 2) = 13 - 12.5 = 0.5 $$
The maximum error for $q=3$ is:
$$ E(100; 3) = \max(|-1.5|, |0.5|) = 1.5 $$

The Elliott-Halberstam conjecture studies the sum of these maximum errors over all moduli $q$ up to $x^\vartheta$. For example, if we took $\vartheta = 0.9$, we would sum $E(100; q)$ for all $q \le 100^{0.9} \approx 63$. The conjecture boldly asserts that even when summing the maximum deviations for all these different moduli (some of which are nearly as large as $x$), the total aggregate error remains bounded by $\frac{C \cdot x}{(\ln x)^A}$, meaning the deviations cancel out or remain astonishingly small on average.