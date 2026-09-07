---
id: 01-number-theory/erdos-straus-conjecture
title: "Erdos-Straus Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Straus Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-straus-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Erdős-Straus conjecture asserts that for every integer $n \ge 2$, the rational number $4/n$ can be expressed as the sum of exactly three positive unit fractions. 

Formally, for all $n \in \mathbb{Z}$ with $n \ge 2$, there exist positive integers $x, y, z$ such that:
$$ \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} $$

A complete proof of the conjecture requires demonstrating that this Diophantine equation has at least one positive integer solution $(x,y,z)$ for every $n \ge 2$. A disproof would require finding a single counterexample—an integer $n \ge 2$ for which no such representation exists.

## 2. Mathematical Foundations

The conjecture belongs to the study of **Diophantine equations** and **Egyptian fractions**. An Egyptian fraction representation of a rational number is a finite sum of unit fractions. While standard Egyptian fractions require the denominators to be distinct, the Erdős-Straus conjecture permits $x, y$, and $z$ to be identical.

By multiplying the primary equation by the common denominator $nxyz$, the problem is algebraically equivalent to finding positive integer solutions to the non-linear Diophantine equation:
$$ 4xyz = n(xy + yz + zx) $$

Without loss of generality, we may impose the ordering $x \le y \le z$. 
A fundamental reduction in the problem relies on the multiplicative property of the equation. If $n$ is composite, say $n = pq$, and there exists a solution for $p$ such that $\frac{4}{p} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$, then dividing both sides by $q$ yields a solution for $n$:
$$ \frac{4}{n} = \frac{4}{pq} = \frac{1}{qx} + \frac{1}{qy} + \frac{1}{qz} $$
Thus, to prove the conjecture for all integers $n \ge 2$, it is both necessary and sufficient to prove it for all prime numbers $n = p$.

## 3. History & State of the Art (SOTA)

Paul Erdős and Ernst G. Straus formulated the conjecture in 1948. It emerged as a generalization of a broader question concerning the minimal length of Egyptian fraction representations. 

Historically, progress has been divided into verifying congruence classes and establishing asymptotic bounds on the number of potential exceptions. In 1970, R. C. Vaughan applied the Hardy-Littlewood circle method to prove that the number of exceptional $n \le N$ for which no solution exists is bounded by $N \exp(-c (\log N)^{2/3})$ for some constant $c > 0$. 

The current analytical state of the art was established by Christian Elsholtz and Terence Tao in 2013. Instead of merely looking for a single solution, they studied the function $f(p)$, which counts the total number of solutions for a prime $p$. They provided rigorous upper and lower bounds on the average value of $f(p)$ and proved that the number of exceptions $n \le N$ is at most $N \exp(-c \log N / \log \log N)$.

## 4. Partial Results / Verified Cases

The conjecture has been proven for the vast majority of cases:
- **Polynomial Identities and Modular Classes:** The conjecture is known to hold for all $n$ except those in certain highly restricted congruence classes. For example, if $n \equiv 2 \pmod 3$, the identity $\frac{4}{n} = \frac{1}{n} + \frac{1}{(n+1)/3} + \frac{1}{n(n+1)/3}$ provides a guaranteed solution. Similar polynomial identities cover $n \equiv 3 \pmod 4$, $n \equiv 2 \pmod 5$, $n \equiv 3 \pmod 5$, etc.
- **Mordell's Reduction:** L.J. Mordell (1967) applied covering congruences to show that if a counterexample exists, it must be congruent to $1, 121, 169, 289, 361,$ or $529 \pmod{840}$. 
- **Computational Verification:** Through highly optimized parallel sieve algorithms utilizing these restricted congruence classes, computer searches have verified the conjecture for all $n \le 10^{18}$.

## 5. Principal Obstacles

The central obstacle to a complete resolution is the failure of purely algebraic methods. Andrzej Schinzel proved that polynomial identities (like the one for $n \equiv 2 \pmod 3$) can never form a complete covering system for all residue classes. Therefore, no finite set of such algebraic identities will ever suffice to prove the conjecture for all primes.

Standard analytic techniques, such as the Hardy-Littlewood circle method or sieve theory, also fail to cross the finish line. While these methods excel at showing that the density of exceptions tends to $0$, they are inherently probabilistic in nature. They cannot distinguish between a set of counterexamples that is empty and a set that is finite or exceptionally sparse. Because the local-to-global principle (Hasse Principle) does not strictly enforce integer solutions for this specific non-linear Diophantine surface, traditional tools cannot definitively rule out the existence of isolated, large prime counterexamples.

## 6. The Gap

The precise mathematical barrier lies in traversing the gap from **"density one"** to **"all."** We possess rigorous proof that the proportion of primes satisfying the conjecture approaches $100\%$, and computational proof that there are no small counterexamples. The missing step is a structural or geometric mechanism that guarantees at least one rational point exists on the Diophantine surface $4xyz = p(xy+yz+zx)$ for all arbitrarily large primes $p$ that evade the known polynomial covering systems. 

## 7. Current Research (as of June 2026)

Active research on the conjecture largely proceeds along three tracks:
1. **Arithmetic Geometry:** Investigating the properties of the varieties defined by the Erdős-Straus equation over finite fields, aiming to force the existence of global integer points via Hasse-Weil bounds.
2. **Divisor Distribution:** Building on Elsholtz and Tao's work, researchers are analyzing the fine-scale distribution of divisors of shifted primes, such as $p+1$ and $p+2$, which dictate the existence of solutions.
3. **Computational Advances:** *(frontier — verify)* Research groups specializing in high-performance computing are deploying specialized GPU sieves and heuristic pruning to push the exhaustive verification boundary toward $10^{19}$ and refine the asymptotic bounds on potential exceptions.

## 8. Future Work

Future breakthroughs may require synthesizing sieve theory with additive combinatorics. Leading number theorists suggest that instead of trying to construct explicit polynomial identities, future work should focus on the existence of smooth numbers in the shifted intervals surrounding a prime $p$. Another proposed pathway is the resolution of the broader Sierpiński conjecture (that $\frac{5}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ for all $n \ge 2$), which might yield a generalized structural theorem of which Erdős-Straus is merely a corollary.

## 9. Key References

- **[Foundational]** Erdős, P. "Az $1/x_1 + 1/x_2 + \dots + 1/x_n = a/b$ egyenlet egész számú megoldásairól" (On a Diophantine Equation). *Mat. Lapok*, 1, 1950, pp. 192-210.
- **[Foundational]** Vaughan, R. C. "On a problem of Erdős, Straus and Schinzel." *Mathematika*, 17, 1970, pp. 193-198.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. Springer, 3rd Edition, 2004. (Section D11).
- **[SOTA / Recent]** Elsholtz, C., & Tao, T. "Counting the number of solutions to the Erdős–Straus equation on unit fractions." *Journal of the Australian Mathematical Society*, 94(1), 2013, pp. 50-105.

## 10. Worked Example / Concrete Special Case

Let us verify the conjecture for the prime $n = 5$. We seek integers $x, y, z \ge 1$ such that:
$$ \frac{4}{5} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} $$

Because $5 \equiv 2 \pmod 3$, we can utilize the explicit polynomial identity derived for this congruence class:
$$ \frac{4}{n} = \frac{1}{n} + \frac{1}{(n+1)/3} + \frac{1}{n(n+1)/3} $$

Substituting $n = 5$ into the identity:
1. The first term is $\frac{1}{5}$.
2. The second term denominator is $(5+1)/3 = 6/3 = 2$, yielding $\frac{1}{2}$.
3. The third term denominator is $5 \times ((5+1)/3) = 5 \times 2 = 10$, yielding $\frac{1}{10}$.

Checking the sum:
$$ \frac{1}{5} + \frac{1}{2} + \frac{1}{10} = \frac{2}{10} + \frac{5}{10} + \frac{1}{10} = \frac{8}{10} = \frac{4}{5} $$

Thus, the triplet $(x, y, z) = (2, 5, 10)$ is a valid solution. Note that this is not the only solution for $n=5$; another valid representation is $\frac{1}{2} + \frac{1}{4} + \frac{1}{20}$, demonstrating that solutions to the Erdős-Straus equation are typically not unique.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*