---
id: 01-number-theory/hardy-littlewood-second-conjecture
title: "Hardy-Littlewood Second Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hardy-Littlewood Second Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/hardy-littlewood-second-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Hardy-Littlewood Second Conjecture posits that the prime-counting function $\pi(x)$ is subadditive for all integers greater than or equal to 2. Specifically, it claims that the number of primes in any interval of length $y$ is never strictly greater than the number of primes in the initial interval $[1, y]$. 

Formally, the conjecture states that for all real numbers $x, y \ge 2$:
$$ \pi(x + y) \le \pi(x) + \pi(y) $$

Equivalently, this can be expressed in terms of primes in short intervals:
$$ \pi(x + y) - \pi(x) \le \pi(y) $$

A complete disproof of this conjecture requires either demonstrating a concrete, unconditional counterexample (a specific pair $(x, y)$ that violates the inequality) or unconditionally proving that such a pair must exist.

## 2. Mathematical Foundations

The conjecture rests on the distribution of prime numbers $\mathbb{P}$ within the integers. 

**The Prime-Counting Function:**
Let $\pi(x)$ denote the prime-counting function, defined as the number of primes less than or equal to $x$:
$$ \pi(x) = \sum_{\substack{p \le x \\ p \in \mathbb{P}}} 1 $$

**Admissible Sets:**
A finite set of integers $\mathcal{H} = \{h_1, h_2, \dots, h_k\}$ is called *admissible* if, for every prime $p$, the elements of $\mathcal{H}$ do not cover all possible residue classes modulo $p$. Formally:
$$ \forall p \in \mathbb{P}, \quad \left| \{ h_i \pmod p : 1 \le i \le k \} \right| < p $$
Let $\rho^*(y)$ denote the maximum size of an admissible set that can be contained within an interval of length $y$. 

**The Prime $k$-tuples Conjecture (Hardy-Littlewood First Conjecture):**
The second conjecture is inextricably linked to the first, which states that for any admissible set $\mathcal{H}$, there exist infinitely many integers $n$ such that the shifted set $n + \mathcal{H}$ consists entirely of prime numbers.

If the Prime $k$-tuples Conjecture is true, then the maximum number of primes in an interval of length $y$ as $x$ varies is exactly $\rho^*(y)$. Thus, the truth of both conjectures would imply $\rho^*(y) = \pi(y)$ for all $y \ge 2$.

## 3. History & State of the Art (SOTA)

G. H. Hardy and J. E. Littlewood proposed both the First and Second Conjectures in their seminal 1923 paper, *"Some problems of 'Partitio numerorum'; III"*. For decades, the Second Conjecture was widely believed to be true because prime density monotonically decreases asymptotically; intuitively, an interval $[x, x+y]$ for large $x$ should contain fewer primes than the initial interval $[1, y]$.

The major paradigm shift occurred in 1973–1974 when Douglas Hensley and Ian Richards proved that the First and Second Hardy-Littlewood Conjectures are mutually incompatible. They demonstrated that for sufficiently large $y$, one can construct admissible sets of length $y$ containing more than $\pi(y)$ elements (i.e., $\rho^*(y) > \pi(y)$). 

Because the First Conjecture (the Prime $k$-tuples Conjecture) is overwhelmingly supported by heuristic models, probabilistic arguments, and recent breakthroughs in bounded gaps between primes, the mathematical consensus is that the Second Hardy-Littlewood Conjecture is almost certainly false. However, an unconditional disproof remains elusive.

## 4. Partial Results / Verified Cases

Despite its presumed falsehood, the conjecture holds up under extensive constraints and verified cases:
- **Small Values:** The conjecture has been verified computationally for all $x, y \le 10^{10}$ and beyond. It holds naturally for small numbers due to the high density of primes near zero.
- **Asymptotic Cases:** Udrescu (1975) proved unconditionally that for any $\epsilon > 0$, there exists an $x_0(\epsilon)$ such that for all $x, y \ge x_0(\epsilon)$, the weakened bound $\pi(x+y) \le \pi(x) + (1+\epsilon)\pi(y)$ holds.
- **Sieve Bounds:** Utilizing the Selberg sieve and the Montgomery-Vaughan theorem, it is unconditionally known that $\pi(x+y) - \pi(x) \le \frac{2y}{\log y}$ for large $y$. While robust, this is a factor of 2 larger than $\pi(y) \sim \frac{y}{\log y}$, failing to prove subadditivity.
- **Conditional Disproof:** The conjecture is formally proven false *conditional* on the Prime $k$-tuples Conjecture being true.

## 5. Principal Obstacles

The problem remains unconditionally open due to profound limitations in modern sieve theory:
1. **The Parity Problem:** Traditional sieve methods cannot accurately distinguish between integers with an odd number of prime factors (like primes) and those with an even number (like semiprimes). This structural barrier prevents current analytic techniques from proving the unconditional existence of highly dense clusters of primes required to violate the inequality.
2. **Computational Infeasibility:** Finding a direct counterexample is vastly beyond current computational power. The smallest known interval length where $\rho^*(y) > \pi(y)$ is $y = 3159$. An admissible set of this size ($k=447$) would, according to the Bateman-Horn conjecture, first yield a prime constellation around $x \approx 10^{300}$ to $10^{400}$, dwarfing the capabilities of brute-force search.

## 6. The Gap

The exact mathematical barrier separating the current state of knowledge from a complete resolution is the transition from a *conditional* existence of dense prime constellations to an *unconditional* one. 

To resolve the conjecture unconditionally, mathematicians must cross the boundary of proving that at least one admissible set $\mathcal{H}$ of length $y$ where $|\mathcal{H}| > \pi(y)$ can be shifted by some integer $x$ such that all elements in $x + \mathcal{H}$ are simultaneously prime. We currently lack the tools to force primes into specific, maximally dense admissible sets without assuming the Prime $k$-tuples conjecture.

## 7. Current Research (as of June 2026)

Active research primarily focuses on narrowing the gap between theoretical limits and sieve boundaries:
- **Bounded Gaps:** Building on the monumental work of Zhang, Maynard, and Tao on bounded gaps between primes, researchers are attempting to generalize the Maynard-Tao multidimensional sieve to target specific, dense admissible configurations.
- **Admissible Set Density:** Computational groups (building on the legacy of the Polymath8 project) continue to calculate tighter bounds for $\rho^*(y)$. Discovering smaller values of $y$ where $\rho^*(y) > \pi(y)$ lowers the theoretical bound for a first counterexample.
- *(frontier — verify)* Advanced heuristic models utilizing random matrix theory are being deployed to predict the exact distributional behavior of prime clusters at astronomical scales, attempting to isolate ranges where an unconditional proof of cluster existence might bypass the parity barrier.

## 8. Future Work

Leading analytic number theorists suggest the following pathways:
- **Bypassing the Parity Problem:** Developing localized sieve variants that break the parity barrier for specific, highly structured admissible sets rather than general sequences.
- **Improved Upper Bounds:** Lowering the constant in the Montgomery-Vaughan upper bound for primes in short intervals from $2$ closer to $1$, which would tighten the asymptotic understanding of $\pi(x+y) - \pi(x)$.
- **Algorithmic Searches:** Developing novel distributed algorithms to search for prime constellations associated with small admissible sets that violate the conjecture, utilizing quantum search heuristics if hardware scales appropriately.

## 9. Key References

- **[Foundational]** Hardy, G. H., & Littlewood, J. E. *Some problems of 'Partitio numerorum'; III: On the expression of a number as a sum of primes.* Acta Mathematica, 1923.
- **[Foundational]** Hensley, D., & Richards, I. *On the incompatibility of two conjectures concerning primes.* Proceedings of Symposia in Pure Mathematics, 1973.
- **[SOTA / Recent]** Richards, I. *On the incompatibility of two conjectures concerning primes; a discussion of the use of computers in attacking a theoretical problem.* Bulletin of the American Mathematical Society, 1974.
- **[SOTA / Recent]** Maynard, J. *Small gaps between primes.* Annals of Mathematics, 2015.
- **[Survey]** Soundararajan, K. *Small gaps between prime numbers: The work of Goldston-Pintz-Yıldırım.* Bulletin of the American Mathematical Society, 2007.

## 10. Worked Example / Concrete Special Case

To understand why the conjecture holds for small numbers and how it is expected to fail at large scales, let us walk through a concrete example.

**A verified small case:**
Let $x = 14$ and $y = 10$.
1. Calculate $\pi(14)$: The primes are $\{2, 3, 5, 7, 11, 13\}$, so $\pi(14) = 6$.
2. Calculate $\pi(10)$: The primes are $\{2, 3, 5, 7\}$, so $\pi(10) = 4$.
3. Calculate $\pi(x+y) = \pi(24)$: The primes are $\{2, 3, 5, 7, 11, 13, 17, 19, 23\}$, so $\pi(24) = 9$.
4. Test the inequality: $9 \le 6 + 4 \implies 9 \le 10$. The conjecture holds.

**The blueprint for a counterexample:**
Consider $y = 3159$.
Computational counts show that $\pi(3159) = 446$.
However, researchers have found a specific admissible set $\mathcal{H}$ within an interval of length $3159$ that contains exactly $447$ integers. Because $\mathcal{H}$ is admissible, it does not occupy all residue classes for any prime $p$.

If the Prime $k$-tuples Conjecture is true, there exists some integer $x$ such that every integer in the shifted set $x + \mathcal{H}$ is prime. 
This shifted set falls entirely within the interval $[x, x + 3159]$. 
Therefore, for this specific $x$, the interval $[x, x + 3159]$ contains at least $447$ primes.

This would mean:
$$ \pi(x + 3159) - \pi(x) \ge 447 $$
But we know $\pi(3159) = 446$. Thus:
$$ 447 > 446 \implies \pi(x + 3159) - \pi(x) > \pi(3159) $$
which directly violates subadditivity, breaking the Second Hardy-Littlewood Conjecture. Finding this exact $x$ remains the missing unconditional step.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*