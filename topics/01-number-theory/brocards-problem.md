---
id: 01-number-theory/brocards-problem
title: "Brocard's Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brocard's Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/brocards-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Brocard's problem is a question in number theory that asks to find all integer pairs $(n, m)$ such that:
$$n! + 1 = m^2$$
where $n!$ is the factorial of $n$.

Pairs of numbers $(n, m)$ that satisfy this Diophantine equation are referred to as **Brown numbers**. The conjecture, often attributed to Paul Erdős, states that the only valid solutions are $(4, 5)$, $(5, 11)$, and $(7, 71)$, and that no further solutions exist for any integer $n > 7$. A complete proof requires either demonstrating definitively that no other solutions can exist or producing a new counterexample and proving a strict classification of all such pairs.

## 2. Mathematical Foundations

The problem concerns a specific exponential Diophantine equation:
$$n! + 1 = m^2$$

where $n, m \in \mathbb{Z}^+$ (positive integers). 
The factorial function is defined as $n! = \prod_{i=1}^n i = 1 \cdot 2 \cdot 3 \cdots n$.

The equation can be rewritten algebraically as a factorization problem:
$$n! = m^2 - 1 = (m - 1)(m + 1)$$
Since $m-1$ and $m+1$ have the same parity, and their product is $n!$ (which is heavily divisible by 2 for $n \ge 2$), they must both be even. This implies $m$ must be odd. The greatest common divisor of $m-1$ and $m+1$ is 2. Therefore, the problem asks whether the highly composite number $n!$ can be written as the product of two even integers that differ exactly by 2.

The problem is intimately connected to the **abc conjecture**. If the abc conjecture holds true, it imposes severe constraints on the solutions to polynomial-exponential equations. While $n!$ does not directly fit the standard $a+b=c$ formulation without translation, Marius Overholt demonstrated in 1993 that the weak form of the abc conjecture implies there are only finitely many solutions to Brocard's problem.

## 3. History & State of the Art (SOTA)

The problem is named after the French mathematician Henri Brocard, who first proposed it in a pair of articles in 1876 and 1885 in the *Nouvelles Annales de Mathématiques*. It was later independently discovered and popularized by Srinivasa Ramanujan in 1913, who published it as Question 469 in the *Journal of the Indian Mathematical Society*. 

The major milestones in its history are divided between theoretical conditional bounds and massive computational searches:
- **1876 / 1885**: Henri Brocard proposes the problem.
- **1913**: Srinivasa Ramanujan rediscovers the problem.
- **1993**: Marius Overholt proves that if the abc conjecture is true, then $n! + 1 = m^2$ has only finitely many solutions.
- **1996**: Andrzej Dąbrowski generalizes Overholt's result, showing that the abc conjecture implies that $n! + A = m^2$ has only finitely many solutions for any non-zero integer $A$.
- **2000**: Bruce Berndt and William Galway perform a rigorous computational search, verifying that no further solutions exist up to $n = 10^9$.
- **2017**: A computational search by Matson extends the verified range up to $n = 10^{15}$ without finding any new solutions.

## 4. Partial Results / Verified Cases

The conjecture has not been solved theoretically for general $n$, but the following cases and constraints have been rigorously established:
1. **Known Solutions:** It is rigorously proven that $(n,m) \in \{(4,5), (5,11), (7,71)\}$ are valid solutions. 
2. **Computational Verification:** By utilizing fast prime sieving and quadratic residue checks, it has been verified that there are no other solutions for $n \le 10^{15}$. 
3. **Modulo Constraints:** For $n! + 1$ to be a perfect square, $n! + 1$ must be a quadratic residue modulo $p$ for any prime $p$. As $n$ grows, $n! \equiv 0 \pmod p$ for all $p \le n$, which means $n! + 1 \equiv 1 \pmod p$, which is trivially a quadratic residue (since $1^2 = 1$). However, studying the equation modulo primes $p > n$ provides highly efficient computational sieves to eliminate candidate values of $n$.
4. **Conditional Finiteness:** Unconditionally, we do not even know if the set of solutions is finite. Finiteness is currently verified only conditional on the abc conjecture.

## 5. Principal Obstacles

The primary difficulty in solving Brocard's problem lies in the structural mismatch between the factorial function (which is purely multiplicative and grows super-exponentially) and perfect squares (which are defined algebraically). 

Key bottlenecks include:
- **Lack of Algebraic Structure:** The factorial $n!$ does not behave well under standard algebraic manipulations used in Diophantine equations, such as elliptic curves, modular forms, or Pell equations. While $n! = (m-1)(m+1)$, the fact that $n!$ involves the product of *all* integers up to $n$ makes it impossible to apply local-to-global (Hasse) principles effectively. Local obstructions vanish because $n!$ is highly divisible by any local prime basis for $p \le n$.
- **Inadequacy of Congruences:** Traditional modular arithmetic fails to constrain the problem for large $n$. For any prime $p \le n$, the equation $n! + 1 \equiv m^2 \pmod p$ reduces to $1 \equiv m^2 \pmod p$, which always has trivial solutions ($m \equiv \pm 1 \pmod p$), preventing the derivation of a contradiction.
- **Ineffectivity of abc:** Even assuming the abc conjecture, the resulting bounds on the size of finite solutions are inherently *ineffective*. This means the abc conjecture guarantees a finite maximum solution but does not specify what that upper limit is, rendering it useless for closing the gap with computational searches.

## 6. The Gap

The precise mathematical gap lies between the conditionally finite bounds derived from the abc conjecture and the strictly empirical bounds of computational searches ($n > 10^{15}$). To fully resolve the conjecture, one must either:
1. Develop an *effective* version of the abc conjecture (or a similar transcendence theory bound, like Baker's method for logarithmic forms) that applies directly to factorials and produces a strict numeric upper bound $N_{\max}$, followed by a computational sweep up to $N_{\max}$.
2. Discover a novel algebraic, combinatorial, or $p$-adic constraint on the valuations of $n! + 1$ that unconditionally proves it cannot be a perfect square for $n > 7$.

## 7. Current Research (as of June 2026)

Active research on Brocard's problem largely focuses on two distinct areas:
- **Computational Mathematics:** Optimizing massive parallel searches to push the verification bound far beyond $10^{15}$ by using distributed computing networks, highly optimized modular arithmetic algorithms, and multi-layered quadratic residue sieves.
- **Effective Generalizations:** Exploring whether Shinichi Mochizuki's Inter-universal Teichmüller (IUT) theory, or other modern frameworks for the abc conjecture, can yield computationally *effective* constants. If an effective constant is established and universally accepted, it would instantly reduce Brocard's problem to a finite computation. *(frontier — verify)*
- **Polynomial Extensions:** Studying related generalized equations of the form $n! + A = y^k$ (for $A \in \mathbb{Z}$ and $k \ge 2$) or $P(n) = y^k$ where $P(n)$ is a polynomial in $n!$, attempting to find unconditional finiteness proofs for these neighboring problems.

## 8. Future Work

Leading mathematicians suggest the following pathways for tackling the conjecture:
- **Effective Baker-type Bounds:** Attempting to apply advanced forms of Baker's theorem on linear forms in logarithms. Although standard Baker methods apply poorly to factorials compared to standard exponentials, refining these estimates for highly composite numbers remains a theoretical pathway.
- **$p$-adic Methods:** Investigating the $p$-adic distances between factorials and perfect squares. Utilizing Strassman's theorem or Skolem-Mahler-Lech-type methods could theoretically constrain the solutions, though adapting these to the non-linear sequence of factorials requires a breakthrough in $p$-adic analysis.
- **Heuristic Probabilistic Models:** Expanding on Cramér-type probabilistic models for Diophantine equations to rigorously estimate the vanishing probability of $n! + 1$ being a square, which strongly implies there should be zero solutions for large $n$.

## 9. Key References

- **[Foundational]** Brocard, H. *Question 166.* Nouvelles Annales de Mathématiques, 1876.
- **[Foundational]** Ramanujan, S. *Question 469.* Journal of the Indian Mathematical Society, 1913.
- **[SOTA / Recent]** Berndt, B. C., & Galway, W. F. *On the Brocard–Ramanujan Diophantine Equation $n! + 1 = m^2$.* The Ramanujan Journal, 2000.
- **[SOTA / Recent]** Matson, B. *Brocard’s Problem 4th Solution Search Utilizing Quadratic Residues.* Preprint, 2017.
- **[Survey]** Overholt, M. *The Diophantine Equation $n! + 1 = m^2$.* Bulletin of the London Mathematical Society, 1993.
- **[Survey]** Dąbrowski, A. *On the Diophantine Equation $x! + A = y^2$.* Nieuw Archief voor Wiskunde, 1996.

## 10. Worked Example / Concrete Special Case

To understand the mechanics of the equation, consider the search for solutions among the first few integers:

**Case $n = 4$:**
We evaluate $n! + 1$:
$$4! + 1 = (4 \times 3 \times 2 \times 1) + 1 = 24 + 1 = 25$$
We check if 25 is a perfect square: $25 = 5^2$.
Thus, $m = 5$. This yields the first Brown number pair: **(4, 5)**.

**Case $n = 5$:**
We evaluate $n! + 1$:
$$5! + 1 = (5 \times 24) + 1 = 120 + 1 = 121$$
Since $121 = 11^2$, this yields the second known pair: **(5, 11)**.

**Case $n = 6$:**
We evaluate $n! + 1$:
$$6! + 1 = (6 \times 120) + 1 = 720 + 1 = 721$$
The square root of 721 is approximately $26.85$, which is not an integer. Therefore, $n=6$ provides no solution.

**Case $n = 7$:**
We evaluate $n! + 1$:
$$7! + 1 = (7 \times 720) + 1 = 5040 + 1 = 5041$$
We check if 5041 is a perfect square. Noting that $70^2 = 4900$, we test the next integer $71$:
$$71^2 = (70+1)^2 = 4900 + 140 + 1 = 5041$$
This yields the third (and final known) pair: **(7, 71)**.

This demonstrates how rapidly the values of the factorials grow and how increasingly sparse perfect squares become relative to the factorial gaps, offering an intuitive reason why further solutions are highly unlikely to exist.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*