---
id: 01-number-theory/polignacs-conjecture
title: "Polignac's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Polignac's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/polignacs-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Polignac's conjecture makes a bold, universal assertion about the gaps between prime numbers. Let $(p_n)_{n=1}^\infty$ denote the ordered sequence of prime numbers. 

**Strong Form (Original Statement):** For every positive even integer $2k$, there exist infinitely many indices $n$ such that the gap between consecutive primes is exactly $2k$:
$$ p_{n+1} - p_n = 2k $$

**Weak Form:** For every positive even integer $2k$, there exist infinitely many pairs of primes $(p, p')$ such that:
$$ p' - p = 2k $$

When $2k = 2$, both forms reduce to the famous Twin Prime Conjecture. While the two forms are often conflated in modern informal discourse, the strong form strictly dictates that the primes must be *adjacent* in the prime sequence. A complete proof of Polignac's conjecture requires demonstrating that no even gap $2k$ eventually vanishes from the sequence of adjacent prime differences.

## 2. Mathematical Foundations

Let $\mathbb{P}$ be the set of prime numbers, and let $d_n = p_{n+1} - p_n$ define the $n$-th prime gap. The Prime Number Theorem (PNT) guarantees that the average prime gap up to $x$ grows logarithmically: $d_n \sim \ln p_n$. Thus, as $n \to \infty$, prime gaps of any fixed finite size $2k$ become statistically scarce compared to the average gap.

In terms of limits, the strong conjecture implies that for any $k \in \mathbb{Z}^+$:
$$ \limsup_{n \to \infty} \mathbb{1}_{\{2k\}}(d_n) = 1 $$
where $\mathbb{1}$ is the indicator function.

The First Hardy-Littlewood Conjecture provides a quantitative heuristic for the weak form. Let $\pi_{2k}(x)$ be the number of prime pairs $(p, p+2k)$ such that $p \le x$. The conjecture posits:
$$ \pi_{2k}(x) \sim 2 C_{2k} \int_2^x \frac{dt}{(\ln t)^2} $$
where $C_{2k}$ is the generalized twin prime constant, defined as an Euler product over primes $p$:
$$ C_{2k} = \prod_{p \ge 3} \left( 1 - \frac{1}{(p-1)^2} \right) \prod_{\substack{p | k \\ p \ge 3}} \frac{p-1}{p-2} $$
The leading constant $C_2 \approx 0.6601618$ is the traditional twin prime constant.

## 3. History & State of the Art (SOTA)

- **1849:** Alphonse de Polignac originally proposed the conjecture in its strong form.
- **1923:** G. H. Hardy and J. E. Littlewood applied the circle method to formulate rigorous asymptotic predictions for $\pi_{2k}(x)$.
- **1973:** Jingrun Chen proved that there are infinitely many primes $p$ such that $p+2$ is either a prime or a semiprime (a product of at most two primes).
- **2013:** Yitang Zhang achieved a historic breakthrough by proving $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 7 \times 10^7$. This unconditionally proved that *at least one* even number $2k \le 7 \times 10^7$ appears infinitely often as a gap between consecutive primes.
- **2014:** James Maynard and Terence Tao (independently) introduced a multidimensional sieve technique, vastly improving the bounded gap to $600$. 
- **2014:** The collaborative Polymath8b project optimized the Maynard-Tao sieve, bringing the unconditional bound down to $246$.

## 4. Partial Results / Verified Cases

- **Unconditional Bounded Gaps:** It is proven that there is some unknown integer $2k \in [2, 246]$ such that $p_{n+1} - p_n = 2k$ occurs infinitely often. 
- **Conditional Bounds:** Assuming the Generalized Elliott-Halberstam (GEH) Conjecture regarding the distribution of primes in arithmetic progressions, the bound reduces to $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 6$.
- **Semiprime Approximations:** Chen's theorem holds for all even gaps $2k$, meaning there are unconditionally infinitely many pairs $(p, p+2k)$ where $p \in \mathbb{P}$ and $p+2k \in P_2$ (where $P_2$ denotes a number with at most two prime factors).
- **Computational Verification:** The strong form of Polignac's conjecture has been empirically verified up to very large values. Consecutive prime gaps of all even sizes up to $10^5$ have been explicitly found, and twin prime pairs ($2k=2$) have been identified for numbers exceeding $10^{18}$.

## 5. Principal Obstacles

- **The Parity Barrier:** Current analytic techniques rely heavily on sieve theory (e.g., Selberg sieve, GPY sieve). As formalized by Atle Selberg (1949), sieves of dimension $\kappa = 1$ fundamentally cannot distinguish between integers with an odd number of prime factors and those with an even number. Consequently, a sieve alone cannot isolate pairs of primes (1 factor) from prime-semiprime pairs (1 factor and 2 factors).
- **Level of Distribution Limit:** The GPY (Goldston-Pintz-Yıldırım) method requires the primes to possess a level of distribution $\theta > 1/2$, which exceeds the unconditionally proven Bombieri-Vinogradov theorem ($\theta = 1/2$). Zhang bypassed this using smooth moduli, and Maynard-Tao bypassed it with multi-dimensional sieve weights (allowing $\theta < 1/2$). However, these multidimensional generalizations inherently sacrifice the ability to specify the exact gap $2k$. 
- Pinpointing a *specific* gap like $2k=2$ using the 1-dimensional GPY sieve would require $\theta = 1$, which is widely believed to be out of reach and contradicts current formulations of the Elliott-Halberstam conjecture.

## 6. The Gap

The precise mathematical boundary lies between proving the existence of *some unspecified* bounded gap (currently $2k \le 246$) and proving the existence of a *specifically chosen* bounded gap (like $2$ or $4$, or all even integers). The barrier to fully resolving Polignac's conjecture is constructing a completely novel analytic mechanism capable of breaking the parity parity to explicitly detect $P_1-P_1$ pairs at a chosen distance $2k$, rather than relying on the pigeonhole principle over an admissible $m$-tuple of "prime-like" numbers.

## 7. Current Research (as of June 2026)

- Optimization of the Maynard-Tao sieve weights, utilizing advanced variational calculus, to compress the unconditional bound below 246.
- Intensive study of the error terms in the Prime Number Theorem for arithmetic progressions to push the level of distribution $\theta$ as close to 1 as possible.
- Investigating the structure of Dirichlet $L$-functions and the potential existence of Siegel zeros (Landau-Siegel zeros). Paradoxically, due to the Deuring-Heilbronn phenomenon, the existence of a Siegel zero would actually force the Twin Prime Conjecture to be true.
- Generalizations to function fields (e.g., polynomials over finite fields $\mathbb{F}_q[t]$), where the Riemann Hypothesis analogue is resolved, offering a sandbox for testing variations of sieve weights. *(frontier — verify)*

## 8. Future Work

- **Breaking Parity:** The most critical open pathway is successfully integrating bilinear forms, exponential sums, and higher-order convolution structures into sieve methods to inherently distinguish primes from semiprimes.
- **Elliott-Halberstam:** Proving the Elliott-Halberstam conjecture unconditionally. While it would only yield bounded gaps of size $\le 6$, the required techniques would likely revolutionize analytic number theory.
- **Circle Method Advances:** Discovering a way to evaluate the major and minor arcs in the Hardy-Littlewood circle method for binary settings (Twin Primes / Goldbach) without relying on unproven hypotheses regarding massive cancellation in exponential sums over primes.

## 9. Key References

- **[Foundational]** A. de Polignac. *Recherches nouvelles sur les nombres premiers.* Comptes Rendus des Séances de l'Académie des Sciences, 1849.
- **[Foundational]** G. H. Hardy and J. E. Littlewood. *Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes.* Acta Mathematica, 1923. [DOI](https://doi.org/10.1007/bf02403921)
- **[SOTA / Recent]** Y. Zhang. *Bounded gaps between primes.* Annals of Mathematics, 2014.
- **[SOTA / Recent]** J. Maynard. *Small gaps between primes.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)
- **[SOTA / Recent]** D. H. J. Polymath. *Variants of the Selberg sieve, and bounded intervals containing many primes.* Research in the Mathematical Sciences, 2014. [DOI](https://doi.org/10.1186/s40687-014-0012-7)
- **[Survey]** A. Granville. *Primes in intervals of bounded length.* Bulletin of the American Mathematical Society, 2015. [DOI](https://doi.org/10.1090/s0273-0979-2015-01480-1)

## 10. Worked Example / Concrete Special Case

Let us examine the strong form of Polignac's Conjecture for $2k=4$, which concerns **cousin primes**.
The conjecture asserts that there are infinitely many indices $n$ such that consecutive primes $p_n$ and $p_{n+1}$ satisfy $p_{n+1} - p_n = 4$.

Consider the early prime sequence:
$$ p_1=2, p_2=3, p_3=5, p_4=7, p_5=11, p_6=13, p_7=17, p_8=19, p_9=23 $$

We search for exact gaps $p_{n+1} - p_n = 4$:
- $p_5 - p_4 = 11 - 7 = 4$  **(Consecutive Cousin Pair)**
- $p_7 - p_6 = 17 - 13 = 4$ **(Consecutive Cousin Pair)**
- $p_9 - p_8 = 23 - 19 = 4$ **(Consecutive Cousin Pair)**

For the weak form of the conjecture (which asks for *any* pairs of primes with a difference of 4), we can also identify pairs like $(3, 7)$. Here, $7 - 3 = 4$, but they are not consecutive because the prime $5$ lies between them ($p_2=3$, $p_4=7$).

According to the Hardy-Littlewood conjecture, the asymptotic density of cousin primes is governed by the constant $C_4$. Because $k=2$ has no odd prime factors, the product term over odd primes dividing $k$ is empty. Therefore:
$$ C_4 = C_2 \times 1 \approx 0.66016 $$
This remarkable result implies that asymptotically, $\pi_4(x) \sim \pi_2(x)$. Twin primes and cousin primes are expected to appear with approximately the exact same frequency as $x \to \infty$. In contrast, for "sexy primes" ($2k=6$, so $k=3$), we find $C_6 = 2 C_2$, meaning pairs of primes differing by 6 should be asymptotically twice as common.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*