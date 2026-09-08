---
id: 01-number-theory/bounded-gaps-between-primes
title: "Bounded Gaps Between Primes"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bounded Gaps Between Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/bounded-gaps-between-primes` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Bounded Gaps Between Primes problem (formerly a conjecture) asks whether there exists a finite real number $C > 0$ such that there are infinitely many pairs of consecutive primes $(p_n, p_{n+1})$ satisfying the inequality:
$$ p_{n+1} - p_n \le C $$
where $p_n$ denotes the $n$-th prime number. Equivalently, the statement asserts that:
$$ \liminf_{n \to \infty} (p_{n+1} - p_n) < \infty $$
This serves as a weaker, albeit structurally profound, version of the Twin Prime Conjecture, which claims that $C = 2$ is achievable infinitely often (i.e., $\liminf_{n \to \infty} (p_{n+1} - p_n) = 2$). A complete resolution of the bounded gaps problem required proving the existence of such a finite constant $C$, which was successfully achieved in 2013. Subsequent collaborative work dramatically lowered the unconditionally proven value of $C$ to $246$.

## 2. Mathematical Foundations

The problem lies at the intersection of analytic number theory and sieve theory. Let $\mathbb{P}$ denote the set of prime numbers and $p_n$ the $n$-th prime. The Prime Number Theorem (PNT) implies that the average gap between primes around $x$ is asymptotically $\ln(x)$:
$$ p_{n+1} - p_n \sim \ln(p_n) $$
Thus, bounded gaps between primes represent intervals where primes are clustered much more tightly than their average spacing.

The foundation for modern approaches relies on the generalized Hardy-Littlewood prime tuple conjecture and Dickson's conjecture. To rigorously bound gaps, mathematicians employ the **Goldston-Pintz-Yıldırım (GPY) sieve** method. Consider a set of distinct non-negative integers $\mathcal{H} = \{h_1, h_2, \dots, h_k\}$. $\mathcal{H}$ is called an *admissible $k$-tuple* if, for every prime $p$, the set of residues $\{h_1 \pmod p, \dots, h_k \pmod p\}$ does not contain all $p$ residue classes modulo $p$.

The GPY method studies the smoothed sum:
$$ S = \sum_{N \le n < 2N} \left( \sum_{i=1}^k \theta(n+h_i) - \rho \right) w(n)^2 $$
where $\theta$ is a prime-detecting function (like the von Mangoldt function $\Lambda$, or a normalized indicator), $\rho > 0$ is a positive threshold, and $w(n)$ is a non-negative multidimensional sieve weight. If one can prove that $S > 0$ for sufficiently large $N$, it implies that for at least one integer $n \in [N, 2N)$, the shifted tuple $(n+h_1, \dots, n+h_k)$ contains more than $\rho$ primes. Choosing $\rho = 1$ ensures at least two primes exist in the tuple, yielding a bounded gap $C \le \max_{i,j} |h_i - h_j|$.

## 3. History & State of the Art (SOTA)

The study of gaps between primes has a rich history:
- **1926:** Hardy and Littlewood formulated the prime $k$-tuples conjecture, predicting the asymptotic distribution of prime constellations.
- **2005:** Goldston, Pintz, and Yıldırım introduced the GPY sieve. They unconditionally proved that $\liminf_{n \to \infty} \frac{p_{n+1}-p_n}{\ln p_n} = 0$. They also established that if the primes have a level of distribution $\theta > 1/2$ (a relaxation of the Elliott-Halberstam conjecture), then bounded gaps exist.
- **2013:** Yitang Zhang stunned the mathematical world by unconditionally proving bounded gaps between primes. By cleverly modifying the GPY weights and establishing a weakened variant of the Elliott-Halberstam conjecture for a specific smooth moduli regime, he proved that $\liminf_{n \to \infty} (p_{n+1}-p_n) \le 70,000,000$.
- **2013-2014 (Polymath8a & James Maynard):** The Polymath8a project rapidly optimized Zhang's constant to $4,680$. Independently, James Maynard developed a generalized multi-dimensional sieve weight scheme, pushing the bound down to $600$ and generalizing the result to intervals containing arbitrarily many primes ($m$ primes in an interval of bounded length). Terence Tao independently discovered a similar multi-dimensional sieve approach.
- **2014 (Polymath8b):** By extensively optimizing the Maynard-Tao sieve and improving error terms through variational calculus, the Polymath8b project reduced the unconditional bound to $246$.

## 4. Partial Results / Verified Cases

The problem is fully solved in the affirmative, with the state-of-the-art verified cases being:
- **Unconditional Bound:** $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 246$. (Polymath8b, 2014)
- **Conditional Bounds:** 
  - Assuming the Generalized Elliott-Halberstam (GEH) conjecture, the bound drops to $6$.
  - Assuming the standard Elliott-Halberstam (EH) conjecture, the bound is $12$.
- **Higher Prime Multiplicities:** Maynard (and later Polymath8b) proved that for any integer $m \ge 2$, there exists a constant $C_m$ such that $\liminf_{n \to \infty} (p_{n+m-1} - p_n) \le C_m$. For instance, assuming EH, it is proven that $C_3 \le 252$ (three primes in a bounded interval). Unconditionally, the bounds scale as $C_m \ll m^3 e^{4m}$.

## 5. Principal Obstacles

Although the bounded gap problem is resolved (yielding $C=246$), the ultimate goal—the Twin Prime Conjecture ($C=2$)—remains elusive due to the **parity problem** in sieve theory. 

Sieve methods, including the GPY and Maynard-Tao sieves, fundamentally struggle to distinguish between integers with an odd number of prime factors and those with an even number of prime factors. The weights $w(n)$ in these methods are constructed from sums over divisors. Because the Möbius function $\mu(d)$ (which governs inclusion-exclusion in sieving) oscillates based on the parity of the number of prime factors, standard linear sieves cannot isolate true primes (1 prime factor, odd parity) from "almost primes" like semiprimes (2 prime factors, even parity) without external analytic input (like the Bombieri-Vinogradov theorem). 

To cross the barrier from $C=246$ to $C=2$, mathematicians would need a revolutionary technique that fundamentally bypasses the parity barrier, or an entirely new formulation of the error terms in prime distribution across arithmetic progressions.

## 6. The Gap

The explicit mathematical gap is the distance between $246$ and $2$. 

Currently, the theoretical limit of the Maynard-Tao multi-dimensional sieve method, even if one assumes the most powerful unproven conjectures on the distribution of primes in arithmetic progressions (like the Generalized Elliott-Halberstam conjecture), can only achieve a gap of $6$. The distance from $6$ down to $2$ requires breaking the parity barrier. The gap represents a hard limitation of current sieve architectures; they cannot capture the simultaneous primality of $n$ and $n+2$ without inadvertently capturing numbers of the form $p_1 p_2$ (almost primes) in the same mathematical net.

## 7. Current Research (as of June 2026)

Research continues along two major axes:
1. **Distribution of Primes in Arithmetic Progressions:** Efforts to unconditionally improve the level of distribution beyond the Bombieri-Vinogradov bound of $\theta = 1/2$. While Zhang broke $\theta=1/2$ for smooth moduli, proving standard EH up to any $\theta > 1/2$ for general moduli remains a massive focus. Work on Dirichlet polynomials and large sieve inequalities pushes this frontier.
2. **Dense Prime Constellations:** Extending the bounds on $C_m$ (intervals containing $m$ primes). *(frontier — verify)* Recent preprints explore using higher-order Fourier analysis and algebraic geometry over finite fields to better understand the spacing of zeros of Dirichlet L-functions, which governs the error terms in prime counting.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- Develop non-linear sieve weights or sieve methods that incorporate automorphic forms to directly count primes, circumventing the parity problem inherent in Möbius-based summations.
- Extend the structural results of Zhang and Maynard to other rings, such as prime polynomials over finite fields $\mathbb{F}_q[t]$, where the Riemann Hypothesis and related distribution theorems are already established and the parity barrier behaves differently.
- Refine the bounds on the first occurrence of small gaps, studying not just $\liminf_{n \to \infty} (p_{n+1}-p_n)$, but the asymptotic density of pairs $(p, p+246)$.

## 9. Key References

- **[Foundational]** Goldston, D. A., Pintz, J., & Yıldırım, C. Y. *Primes in tuples I*. Annals of Mathematics, 170(2), 2009. [DOI](https://doi.org/10.4007/annals.2009.170.819)
- **[SOTA / Recent]** Zhang, Yitang. *Bounded gaps between primes*. Annals of Mathematics, 179(3), 1121-1174, 2014.
- **[SOTA / Recent]** Maynard, James. *Small gaps between primes*. Annals of Mathematics, 181(1), 383-413, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.1.7)
- **[Survey]** Polymath, D. H. J. *Variants of the Selberg sieve, and bounded intervals containing many primes*. Research in the Mathematical Sciences, 1(1), 12, 2014. [DOI](https://doi.org/10.1186/s40687-014-0012-7)

## 10. Worked Example / Concrete Special Case

To understand how the sieve methodology guarantees a bounded gap, consider the concept of admissible tuples. Let $k=3$ and $\mathcal{H} = \{0, 2, 6\}$. 

This is an admissible 3-tuple because it does not cover all possible residue classes modulo any prime $p$:
- For $p=2$: The residues are $\{0 \pmod 2, 2 \pmod 2, 6 \pmod 2\} = \{0\}$. Residue $1$ is completely missed.
- For $p=3$: The residues are $\{0 \pmod 3, 2 \pmod 3, 6 \pmod 3\} = \{0, 2\}$. Residue $1$ is missed.
- For $p \ge 5$: A set of 3 elements trivially cannot cover all $p$ residues.

The twin prime conjecture essentially asks if the admissible 2-tuple $\mathcal{H} = \{0, 2\}$ yields infinitely many simultaneous primes. Because of the parity problem, standard sieves cannot guarantee two primes purely in $\{n, n+2\}$. 

Instead, the Maynard-Tao sieve leverages a much larger admissible $k$-tuple (where $k = 50$). By designing a multi-dimensional sieve weight function $w(n)$, the method proves that for infinitely many integers $n$, the sum of prime indicator functions over the elements $n+h_i$ (for $h_i \in \mathcal{H}$) is strictly greater than 1:
$$ \sum_{i=1}^k \theta(n+h_i) > 1 $$
Because the sum exceeds 1, it forces at least 2 elements of the shifted tuple $\{n+h_1, \dots, n+h_{50}\}$ to be prime. The gap between these two primes is therefore strictly bounded by the maximum difference in the tuple: $\max(h_i) - \min(h_i)$. The Polymath8b project successfully constructed an explicit admissible 50-tuple with a maximum element of exactly 246, unconditionally proving that a gap of at most 246 occurs infinitely often.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*