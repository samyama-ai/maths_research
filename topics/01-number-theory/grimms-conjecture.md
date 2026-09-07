---
id: 01-number-theory/grimms-conjecture
title: "Grimm's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Grimm's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/grimms-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Given a sequence of $k$ consecutive composite numbers $n+1, n+2, \ldots, n+k$, Grimm's conjecture states that there exist $k$ distinct prime numbers $p_1, p_2, \ldots, p_k$ such that each prime $p_i$ divides exactly one corresponding number $n+i$ in the sequence.

In other words, it is mathematically possible to assign a distinct prime factor to each composite number in any sequence of consecutive composites. A complete proof would require demonstrating that this injective mapping holds for any arbitrary positive integer $n$ and any gap between consecutive primes (since a sequence of consecutive composites lies strictly between two prime numbers $p$ and $q$, where $k = q - p - 1$). Disproof would require finding a "failing block": a specific sequence of consecutive composites $n+1, \ldots, n+k$ that possesses fewer than $k$ distinct prime factors in total for a subset of the composites, thereby making the distinct one-to-one prime assignment impossible by the Pigeonhole Principle.

## 2. Mathematical Foundations

Let $\omega(x)$ denote the number of distinct prime factors of an integer $x$. 
Let $\mathcal{C}_k = \{n+1, n+2, \ldots, n+k\}$ be a set of $k$ consecutive composite integers.

Grimm's conjecture asserts that there exists an injective function $f: \mathcal{C}_k \to \mathbb{P}$ (where $\mathbb{P}$ is the set of all prime numbers) such that for all $i \in \{1, 2, \ldots, k\}$:
$$f(n+i) \mid (n+i)$$

This problem is rigorously formulated in terms of extremal graph theory using **Hall's Marriage Theorem**. Construct a bipartite graph $G = (U, V, E)$ where the first vertex set $U = \mathcal{C}_k$ consists of the $k$ consecutive composite numbers, and the second vertex set $V$ consists of all prime numbers dividing at least one element of $\mathcal{C}_k$. An edge $e \in E$ connects $u \in U$ and $v \in V$ if and only if $v \mid u$. 

By Hall's Marriage Theorem, an injective mapping (a matching that covers $U$) exists if and only if Hall's condition is satisfied: for any subset $A \subseteq U$, the neighborhood $N(A)$ (the set of all prime factors of the numbers in $A$) satisfies:
$$|N(A)| \ge |A|$$
Thus, Grimm's conjecture is mathematically equivalent to asserting that for any set of consecutive composite numbers, the number of distinct prime factors of any subset is at least as large as the size of the subset.

## 3. History & State of the Art (SOTA)

The conjecture was proposed by Carl Albert Grimm in 1969. In his original paper, he proved the conjecture for small sequences and noted its deep connection to the distribution of primes and prime gaps. 

A weaker version of Grimm's Conjecture states that if $n+1, \ldots, n+k$ are composite, then the product $\prod_{i=1}^k (n+i)$ has at least $k$ distinct prime factors. This foundational relaxation was proven to be true unconditionally by Paul Erdős and John Selfridge in 1971.

A major focus of the state of the art is bounding the function $g(n)$, which is defined as the largest positive integer $k$ such that for *any* sequence $n+1, n+2, \ldots, n+k$, there exist distinct primes $p_i \mid (n+i)$. Since Grimm's conjecture naturally operates in the prime gap between a prime $p_m$ and $p_{m+1}$, proving $g(n)$ is larger than the maximum prime gap near $n$ would fully resolve the conjecture.
- Unconditionally, Shanta Laishram and M. Ram Murty (2012) established $g(n) = O(n^\alpha)$ for $0.45 < \alpha < 0.46$.
- Conditionally, standard conjectures about smooth numbers (integers whose prime factors are below a certain bound) in short intervals imply $g(n) = O(n^\epsilon)$ for any $\epsilon > 0$.

## 4. Partial Results / Verified Cases

- **Computational Bounds:** Grimm's conjecture has been verified computationally for all integers up to a high limit. Currently, no failing block has been found for any starting values $n \leq 1.9 \times 10^{10}$.
- **Short Sequences:** When the sequence of composites is relatively short compared to $n$, the conjecture is easily verified. Specifically, if $k \le \sqrt{n}$, the primes are well-distributed enough to systematically satisfy Hall's Marriage Theorem. 
- **Asymptotic Ranges:** Erdős and Pomerance proved the conjecture is true unconditionally for sequences of length $k \ll (n / \log n)^{1/3}$.

## 5. Principal Obstacles

The primary obstacle is the lack of strict lower bounds on the number of distinct prime factors in dense, local intervals. The conjecture inherently requires proving that short intervals contain numbers with uniquely large or highly distinct prime factors, avoiding clustering.

Traditional analytic number theory methods (such as sieve methods like the Selberg sieve) typically provide estimates for the *average* number of prime factors or the number of primes in an interval. However, Grimm's conjecture requires an absolute, worst-case combinatorial bound. When the gap between consecutive primes is extremely large (e.g., $k \gg \log^2 n$, as suggested by Cramér's conjecture), standard probabilistic heuristics fail to guarantee the localized existence of distinct prime factors for *every* number in the gap. 

The presence of highly "smooth" numbers in the interval (numbers with only very small prime factors) actively sabotages the bipartite matching. If too many smooth numbers exist closely together, they cluster edges onto a very small set of prime vertices in $V$, risking a direct violation of Hall's condition ($|N(A)| < |A|$).

## 6. The Gap

The precise boundary lies between the known distribution of maximal prime gaps and the known lower bounds on $g(n)$ (the distinct prime-matching capability). 
To fully resolve the conjecture, one must cross the barrier of showing that for any maximal prime gap $[p, p+k]$ where $k$ is the gap size, $g(p) \ge k$. 

Because Cramér's conjecture suggests prime gaps can be as large as $k \approx \log^2 p$, one must unconditionally prove that a distinct prime mapping can survive gaps of logarithmic size. Current unconditional bounds (like $O(n^{0.45})$) are macroscopic polynomial scales, whereas Grimm's conjecture requires microscopic precision over intervals of size $\log^2 n$.

## 7. Current Research (as of June 2026)

Current research is largely focused on the intersection of probabilistic number theory and extremal combinatorics.
- **Smooth Numbers in Short Intervals:** Researchers attempt to bound the number of smooth numbers that can exist in an interval of length $k$. If an interval contains too many smooth numbers, Hall's condition fails. Proving rigorous upper bounds on the density of smooth numbers in short intervals is the most active strategy.
- **Combinatorial Sieves:** Finding structural algebraic properties of subsets of $U$ (from the bipartite graph) that would restrict how small $|N(A)|$ can get.
- *(frontier — verify)* Recent preprints explore using connections to the ABC conjecture to bound the prime factors of adjacent integers to strictly forbid dense topological clusters of smooth numbers.

## 8. Future Work

Leading mathematicians suggest two primary pathways for future work:
1. **Refining $g(n)$:** Improving the unconditional bounds on $g(n)$ from polynomial bounds to polylogarithmic bounds to better reflect the size of actual maximal prime gaps.
2. **Conditional Proofs:** Formally proving Grimm's Conjecture assuming standard but unresolved conjectures like the Riemann Hypothesis (RH) or Cramér's Conjecture. While RH gives excellent bounds on prime gaps, it is not yet known if RH alone provides sufficient variance control to enforce the microscopic combinatorial constraints required by Grimm.

## 9. Key References

- **[Foundational]** C. A. Grimm. *A conjecture on consecutive composite numbers.* The American Mathematical Monthly, 1969.
- **[Foundational]** P. Erdős and J. L. Selfridge. *Some problems on the prime factors of consecutive integers II.* Proceedings of the Washington State University Conference on Number Theory, 1971.
- **[SOTA / Recent]** S. Laishram and M. Ram Murty. *Grimm's Conjecture and Smooth Numbers.* Michigan Mathematical Journal, 2012.

## 10. Worked Example / Concrete Special Case

Consider the sequence of consecutive composite numbers strictly between the primes $p = 23$ and $q = 29$.
Here, $n = 23$, and the gap contains $k = 5$ composite numbers: $\mathcal{C}_5 = \{24, 25, 26, 27, 28\}$.

To satisfy Grimm's Conjecture, we must find distinct primes $p_1, p_2, p_3, p_4, p_5$ such that $p_i \mid (23+i)$.
Let's factorize each number to find the available prime divisors (the neighborhoods $N(A)$ in the bipartite graph):
- $24 = 2^3 \cdot 3 \implies$ prime factors: $\{2, 3\}$
- $25 = 5^2 \implies$ prime factors: $\{5\}$
- $26 = 2 \cdot 13 \implies$ prime factors: $\{2, 13\}$
- $27 = 3^3 \implies$ prime factors: $\{3\}$
- $28 = 2^2 \cdot 7 \implies$ prime factors: $\{2, 7\}$

We must satisfy Hall's Marriage condition and extract an injective mapping. Notice how tightly constrained some numbers are:
- $25$ only has one prime factor, so we **must** assign $25 \rightarrow 5$.
- $27$ only has one prime factor, so we **must** assign $27 \rightarrow 3$.
- Because $3$ is taken by $27$, the number $24$ (factors $\{2, 3\}$) is forced to take its only remaining option. We **must** assign $24 \rightarrow 2$.
- Because $2$ is taken by $24$, the number $26$ (factors $\{2, 13\}$) is forced. We **must** assign $26 \rightarrow 13$.
- Because $2$ is taken, the number $28$ (factors $\{2, 7\}$) is forced. We **must** assign $28 \rightarrow 7$.

Our final distinct mapping is:
- $24 \rightarrow 2$
- $25 \rightarrow 5$
- $26 \rightarrow 13$
- $27 \rightarrow 3$
- $28 \rightarrow 7$

The chosen primes are $\{2, 5, 13, 3, 7\}$, which are all distinct prime numbers. Every composite in the sequence is assigned a unique prime factor, successfully demonstrating Grimm's Conjecture for this specific gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*