---
id: 01-number-theory/collatz-conjecture
title: "Collatz Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Collatz Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/collatz-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Collatz Conjecture, also known as the $3x+1$ problem, the Syracuse problem, or Ulam's conjecture, posits that for any given positive integer $n$, a specific iteratively applied arithmetic function will always eventually reach the value $1$. 

Formally, define a function $f : \mathbb{Z}^+ \to \mathbb{Z}^+$ on the positive integers as follows:
$$ f(n) = \begin{cases} \frac{n}{2} & \text{if } n \equiv 0 \pmod 2 \\[6pt] 3n + 1 & \text{if } n \equiv 1 \pmod 2 \end{cases} $$

Consider the sequence of integers formed by repeated applications of $f$, defined recursively as:
$$ a_0 = n $$
$$ a_k = f(a_{k-1}) \quad \text{for } k > 0 $$

The conjecture claims that for every positive integer $n$, there exists an integer $k \ge 0$ such that $a_k = 1$. A complete proof requires showing that no starting value $n$ can lead to an sequence that diverges to infinity, and that there are no periodic cycles other than the trivial cycle $(1 \mapsto 4 \mapsto 2 \mapsto 1)$.

## 2. Mathematical Foundations

The problem can be modeled as a dynamical system over the integers. It is often convenient to study the "shortcut" Collatz function $T: \mathbb{Z}^+ \to \mathbb{Z}^+$, which eliminates the deterministic division by $2$ that always immediately follows a $3n+1$ step:
$$ T(n) = \begin{cases} \frac{n}{2} & \text{if } n \equiv 0 \pmod 2 \\[6pt] \frac{3n + 1}{2} & \text{if } n \equiv 1 \pmod 2 \end{cases} $$

The sequence of iterates is called the **orbit** or **trajectory** of $n$: $\mathcal{O}(n) = \{n, T(n), T^2(n), T^3(n), \dots\}$.
The conjecture asserts that $1 \in \mathcal{O}(n)$ for all $n \in \mathbb{Z}^+$.

To formalize the growth of these trajectories, researchers study the **stopping time** $\sigma(n)$, defined as the smallest $k$ such that $T^k(n) < n$:
$$ \sigma(n) = \inf \{ k \in \mathbb{Z}^+ \mid T^k(n) < n \} $$
The Collatz conjecture is equivalent to the statement that every integer $n > 1$ has a finite stopping time.

The problem can also be embedded into the $2$-adic integers $\mathbb{Z}_2$, since the operations of multiplying by $3$, adding $1$, and dividing by $2$ are continuous in the $2$-adic metric. The extension of $T$ to $\mathbb{Z}_2$ is a continuous, measure-preserving ergodic transformation.

## 3. History & State of the Art (SOTA)

The conjecture was introduced in 1937 by Lothar Collatz, shortly after he received his doctorate. It circulated widely by word of mouth through the mathematical community in the 1950s and 60s, acquiring various names depending on who championed it (e.g., Kakutani's problem, Hasse's algorithm, Ulam's conjecture).

Paul Erdős famously stated about the conjecture: *"Mathematics may not yet be ready for such problems,"* reflecting the lack of structural tools to deal with the chaotic behavior of the map. He offered a \$500 prize for its solution.

For decades, the state of the art involved proving that the conjecture holds for "most" numbers, establishing lower bounds for the number of valid cases. In 1976, Terras proved that almost all integers have a finite stopping time (their trajectory eventually drops below their starting value). In 2019, Terence Tao achieved a major breakthrough by proving that almost all Collatz orbits attain almost bounded values. Specifically, Tao showed that for any function $g(n)$ diverging to infinity (no matter how slowly), the logarithmic density of integers $n$ for which the minimum value of their orbit falls below $g(n)$ is $1$.

## 4. Partial Results / Verified Cases

While a general proof remains elusive, significant partial results exist:
- **Computational Verification:** As of 2020, David Barina and others have computationally verified the conjecture for all starting values up to $n = 2^{68} \approx 2.95 \times 10^{20}$. Every integer in this range eventually collapses to $1$.
- **Absence of Small Cycles:** Shalom Eliahou (1993) proved that if a non-trivial cycle exists, its length must be at least $17,087,915$. Using modern verified limits ($2^{68}$), the minimum length of any non-trivial cycle is now known to exceed $10^{11}$ steps, and it must contain at least tens of billions of odd integers.
- **Lower Bounds on Valid Integers:** Krasikov and Lagarias (2003) proved that the number of integers in the interval $[1, x]$ that eventually reach $1$ is at least proportional to $x^{0.84}$.

## 5. Principal Obstacles

The Collatz Conjecture defies resolution due to the deep structural dissonance between its two operations. The function $n \mapsto 3n+1$ operates in a multiplicative structure defined by powers of $3$ (with an additive translation), while the function $n \mapsto n/2$ operates on the binary structure of the number (powers of $2$). 

Traditional techniques in number theory fail because:
1. **Lack of Algebraic Structure:** There is no known natural polynomial or modular algebraic structure that is preserved by both operations simultaneously. 
2. **Pseudo-Randomness:** The sequence of operations (whether a number in the orbit is even or odd) behaves remarkably like a pseudo-random coin flip. While this heuristic strongly suggests the conjecture is true (since a sequence of random flips yields an expected growth factor of $\frac{3}{4}$ per step, shrinking the number), probabilistic arguments do not yield absolute proofs for deterministic sequences.
3. **Undecidability Analogs:** John Conway (1972) generalized the Collatz map to arbitrary modular piecewise linear functions and proved that, in general, determining if a given number reaches $1$ in such a system is an undecidable problem. This suggests that the $3x+1$ problem might lie close to the boundary of formal unprovability.

## 6. The Gap

The boundary between current knowledge and a full proof is precisely the difference between "almost all" and "all," as well as "arbitrarily small" and "one." 

Tao's result guarantees that for 99.99...% of numbers $n$, the sequence drops below $\ln(\ln(n))$, for example. However, to fully close the gap, one must definitively prove two negative claims for **all** integers:
1. **No divergent trajectories:** No sequence $a_k$ goes to infinity as $k \to \infty$.
2. **No non-trivial cycles:** The sequence never loops back on itself (aside from $1 \to 4 \to 2 \to 1$). 

Current probabilistic and density methods fundamentally cannot rule out the existence of a highly anomalous, astronomically large integer that happens to hit an exact sequence of arithmetic modular properties allowing it to form a closed loop or escape to infinity.

## 7. Current Research (as of June 2026)

Active research primarily focuses on refining probabilistic models and expanding computational boundaries:
- **Ergodic Theory and $p$-adic Analysis:** Extending the Collatz map to $2$-adic integers and utilizing measure theory to study invariant measures of the system. 
- **Holomorphic Dynamics:** Extending the function analytically to the complex plane. The function $f(z) = \frac{z}{2}\cos^2\left(\frac{\pi z}{2}\right) + \frac{3z+1}{2}\sin^2\left(\frac{\pi z}{2}\right)$ interpolates the Collatz map, and researchers are studying the Julia sets of this continuous analog.
- **Improved Density Bounds:** * (frontier — verify)* Researchers are attempting to improve the Krasikov-Lagarias lower bound from $x^{0.84}$ closer to $x^{1-\epsilon}$, leveraging modern sieve theory paired with Tao's logarithmic density framework.

## 8. Future Work

Leading mathematicians suggest that proving the Collatz conjecture will require entirely new branches of mathematics that can cleanly bridge additive and multiplicative number theory. Future pathways include:
- Establishing that the set of integers with divergent trajectories has a Hausdorff dimension of strictly zero.
- Proving conditional results: showing that the non-existence of non-trivial cycles implies the non-existence of divergent trajectories, or vice-versa.
- Finding a "witness" algebraic invariant—a hidden quantity that strictly decreases along the orbit of $T$, acting as a Lyapunov function for the Collatz dynamical system.

## 9. Key References

- **[Foundational]** Lagarias, J. C. *The 3x+1 problem and its generalizations.* The American Mathematical Monthly, 1985. [DOI](https://doi.org/10.2307/2322189)
- **[Foundational]** Lagarias, J. C. (Ed.). *The Ultimate Challenge: The 3x+1 Problem.* American Mathematical Society, 2010. [DOI](https://doi.org/10.5860/choice.48-6964)
- **[SOTA / Recent]** Tao, T. *Almost all orbits of the Collatz map arrive at almost bounded values.* Forum of Mathematics, Pi, 2022.
- **[SOTA / Recent]** Barina, D. *Convergence verification of the Collatz problem.* The Journal of Supercomputing, 2021. [DOI](https://doi.org/10.1007/s11227-020-03368-x)
- **[Survey]** Krasikov, I., & Lagarias, J. C. *Bounds for the 3x+1 problem using difference inequalities.* Acta Arithmetica, 2003. [DOI](https://doi.org/10.4064/aa109-3-4)

## 10. Worked Example / Concrete Special Case

To illustrate the chaotic growth and collapse of a trajectory, consider the starting integer $n = 7$.

We apply the standard function $f(n)$:
1. $7$ is odd $\implies 3(7) + 1 = 22$
2. $22$ is even $\implies 22 / 2 = 11$
3. $11$ is odd $\implies 3(11) + 1 = 34$
4. $34$ is even $\implies 34 / 2 = 17$
5. $17$ is odd $\implies 3(17) + 1 = 52$
6. $52$ is even $\implies 52 / 2 = 26$
7. $26$ is even $\implies 26 / 2 = 13$
8. $13$ is odd $\implies 3(13) + 1 = 40$
9. $40$ is even $\implies 40 / 2 = 20$
10. $20$ is even $\implies 20 / 2 = 10$
11. $10$ is even $\implies 10 / 2 = 5$
12. $5$ is odd $\implies 3(5) + 1 = 16$

At this point, we have reached $16$, which is a power of $2$ ($2^4$). The sequence will now strictly halve:
13. $16 / 2 = 8$
14. $8 / 2 = 4$
15. $4 / 2 = 2$
16. $2 / 2 = \mathbf{1}$

The orbit of $7$ is: $\{7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1\}$. 
It takes $16$ steps to reach $1$, and the sequence peaks at $52$, demonstrating how numbers can grow significantly larger than their starting value before ultimately collapsing to $1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*