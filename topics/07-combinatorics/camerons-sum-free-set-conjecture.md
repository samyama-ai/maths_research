---
id: 07-combinatorics/camerons-sum-free-set-conjecture
title: "Cameron's Sum-Free Set Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cameron's Sum-Free Set Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/camerons-sum-free-set-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Cameron's Sum-Free Set Conjecture—almost universally recognized in the literature as the **Cameron-Erdős Conjecture**—asserts that the total number of sum-free subsets of the first $N$ positive integers, denoted by $[N] = \{1, 2, \dots, N\}$, is bounded by $O(2^{N/2})$. 

A subset $A \subseteq [N]$ is defined to be *sum-free* if it contains no solution to the equation $x + y = z$ for any $x, y, z \in A$ (where $x$ and $y$ are not necessarily distinct). 

There are two natural constructions that trivially yield large families of sum-free sets:
1. **The set of all odd integers:** $O_N = \{1, 3, 5, \dots, 2\lceil N/2 \rceil - 1\}$. Since the sum of two odd integers is always even, $O_N$ is sum-free. Any subset of $O_N$ is also sum-free, yielding $2^{\lceil N/2 \rceil}$ sum-free sets.
2. **The upper half of the interval:** $U_N = \{\lfloor N/2 \rfloor + 1, \dots, N\}$. The sum of any two elements in $U_N$ strictly exceeds $N$, meaning the sum cannot reside in $U_N$. This similarly yields $2^{\lceil N/2 \rceil}$ sum-free sets.

The conjecture formally states that the total cardinality of the sum-free set family $\mathcal{F}_N$ in $[N]$ is asymptotically dominated by these two trivial families. Specifically, Cameron and Erdős conjectured that there exist absolute constants $c_0$ and $c_1$ such that, as $N \to \infty$:
- $|\mathcal{F}_N| \sim c_0 2^{N/2}$ when $N$ is even.
- $|\mathcal{F}_N| \sim c_1 2^{N/2}$ when $N$ is odd.

A secondary, significantly harder conjecture proposed simultaneously was that the number of *maximal* sum-free sets in $[N]$ (sum-free sets not properly contained in any other sum-free set) is bounded by $O(2^{N/4})$.

## 2. Mathematical Foundations

The problem lies at the intersection of additive combinatorics, group theory, and graph enumeration. We formalize the environment mathematically. Let $(Z, +)$ be an abelian group, which for this conjecture is the integers $\mathbb{Z}$. For any subset $A \subseteq \mathbb{Z}$, we define the sumset:
$$ A + A = \{a_1 + a_2 \mid a_1, a_2 \in A\} $$
A set $A$ is sum-free if and only if:
$$ (A + A) \cap A = \emptyset $$

The family of sum-free sets in the finite interval is defined as:
$$ \mathcal{F}_N = \{ A \subseteq [N] \mid (A+A) \cap A = \emptyset \} $$
The size of this family is bounded from below by the union of the power sets of $O_N$ and $U_N$:
$$ |\mathcal{F}_N| \ge 2^{|O_N|} + 2^{|U_N|} - 2^{|O_N \cap U_N|} = 2^{\lceil N/2 \rceil} + 2^{\lceil N/2 \rceil} - 2^{\lfloor N/4 \rfloor} $$

To prove the conjecture, one must show that the vast majority of sum-free sets are structurally "close" to either $O_N$ or $U_N$. The theoretical foundation for handling such additive structures relies heavily on **Freiman's Theorem**, which dictates that sets with small doubling (i.e., $|A+A| \le K|A|$) must be densely contained within a Generalized Arithmetic Progression (GAP) of bounded dimension $d(K)$ and size $f(K)|A|$.

In the continuous analytic approach, the foundations rely on **Fourier analysis over finite abelian groups**. By embedding $[N]$ into a cyclic group $\mathbb{Z}_p$ for a prime $p > 2N$, one can analyze the indicator function $1_A : \mathbb{Z}_p \to \{0, 1\}$. The condition that $A$ is sum-free implies that the convolution integral (or discrete sum) vanishes:
$$ \sum_{x, y \in \mathbb{Z}_p} 1_A(x) 1_A(y) 1_A(x+y) = 0 $$
By applying the discrete Fourier transform $\widehat{1_A}(r) = \sum_{x} 1_A(x) e^{-2\pi i r x / p}$, this condition can be translated into a spectral constraint on the Fourier coefficients (the large spectrum / Bohr sets), mapping additive structural constraints into analytic bounds.

## 3. History & State of the Art (SOTA)

The conjecture was first formally articulated by Peter J. Cameron and Paul Erdős in their 1990 paper *"On the number of sets of integers with various properties"*, presented at the Banff Number Theory Conference. The problem immediately became a central touchstone in enumerative additive combinatorics. 

For over a decade, the problem remained open, resisting standard probabilistic and structural methods. The first major breakthrough was achieved by Noga Alon in 1991. By cleverly translating the sum-free condition into an independent set problem on Cayley-type graphs and utilizing an early, implicit form of hypergraph container theory, Alon proved that $|\mathcal{F}_N| = 2^{N/2 + o(N)}$.

The full Cameron-Erdős conjecture was decisively resolved in 2003–2004 by two distinct, independent methods:
1. **Alexander Sapozhenko (2003):** Utilizing deep graph-theoretic enumeration techniques, Sapozhenko developed a method to count independent sets in highly unbalanced bipartite graphs. By covering independent sets with "containers" closely approximating the extremal odd/upper-half sets, he successfully derived the exact asymptotic formulas, confirming the existence of constants $c_0, c_1$.
2. **Ben Green (2004):** Approaching the problem via arithmetic combinatorics, Green published a rigorous proof using Fourier analysis over $\mathbb{Z}_p$. He imported a continuous analogue of Freiman's theorem and utilized an arithmetic Regularity Lemma to definitively upper-bound the number of exceptional sum-free sets, independently confirming the $O(2^{N/2})$ bound.

The secondary conjecture regarding *maximal* sum-free sets—$O(2^{N/4})$—remained open for another decade. It was finally resolved in 2015 by József Balogh, Hong Liu, Maryam Sharifzadeh, and Andrew Treglown, who utilized the modern, highly refined **Method of Hypergraph Containers** to secure the precise $O(2^{N/4})$ bound. 

## 4. Partial Results / Verified Cases

Prior to the independent proofs by Sapozhenko and Green, the problem was subjected to extensive partial verification and computational checks:
- **Small Values of $N$:** Cameron computed the exact cardinality of $\mathcal{F}_N$ for all $N \le 40$. This computational evidence was critical; it revealed that the ratio $|\mathcal{F}_N| / 2^{N/2}$ did not converge to a single limit but instead oscillated depending on the parity of $N$, firmly motivating the $c_0 \neq c_1$ hypothesis.
- **Sets with Specific Distributions:** Neil Calkin (1990) proved the $O(2^{N/2})$ bound for the restricted class of sum-free sets that contain no elements less than $N/3$, demonstrating that the "upper half" local structure enforces the exponential bound.
- **Abelian Group Analogues:** Green and Ruzsa (2005) investigated the generalized problem of counting sum-free sets in finite abelian groups $G$. Let $\mu(G)$ be the cardinality of the largest sum-free subset of $G$. They verified that the total number of sum-free sets is asymptotically $O(2^{\mu(G)})$ for a large class of groups, specifically those whose order possesses prime factors congruent to $2 \pmod 3$. 

## 5. Principal Obstacles

The primary mathematical bottleneck that stalled progress for over a decade was the appearance of exponential error terms natively generated by structural combinatorial tools. 

To bound the number of sum-free sets, the standard method translates the problem to bounding the number of independent sets in a graph $G$ on $N$ vertices. Applying structural theorems like Szemerédi's Regularity Lemma yields an upper bound of the form $2^{\alpha(G) + \epsilon N}$, where $\alpha(G)$ is the independence number (here, $N/2$) and $\epsilon N$ is the error term inherent to the regularity partition.

Stripping away the $\epsilon N$ term to obtain a sharp $O(2^{N/2})$ bound is exceptionally difficult. It requires shifting from coarse density approximations to exact structural stability theorems. One must prove that if a sum-free set $A$ deviates from the extremal constructions $O_N$ or $U_N$ by $k$ elements, it must systematically "pay" for this deviation by losing at least $\approx 2k$ degrees of freedom from its available choices. Summing the valid configurations across all possible deviations $k$ produces a convergent geometric series:
$$ \sum_{k=1}^{N/2} \binom{N/2}{k} 2^{N/2 - 2k} < \infty $$
replacing the exponential error $2^{\epsilon N}$ with a constant factor.

Executing this required overcoming severe technical obstacles. For Green's Fourier method, embedding the non-periodic interval $[N]$ into a cyclic group $\mathbb{Z}_p$ introduces "edge effects" that distort the arithmetic structure; his continuous removal lemma had to be meticulously engineered to avoid absorbing these edge effects into an exponential error. For Sapozhenko, the Cayley graphs constructed over the integers exhibit irregular degree distributions and boundary expansion properties, requiring bespoke isoperimetric inequalities to prevent the number of bipartite containers from blowing up.

## 6. The Gap

The historical gap bridged by Green and Sapozhenko was the transition from $2^{N/2 + o(N)}$ to exactly $O(2^{N/2})$ by proving rigorous structural stability for sets that are "almost" sum-free. 

Today, a precise boundary exists between what is known for classical sum-free sets and the broader frontier of **sparse random enumeration**. Given a random subset $R \subseteq [N]$ where each integer is included independently with probability $p = p(N)$, the gap lies in perfectly characterizing the exact probability thresholds at which the sum-free subsets of $R$ transition from being dominated by random noise to being dominated by the intersections $R \cap O_N$ and $R \cap U_N$. While Balogh, Morris, and Samotij have closed much of this gap using hypergraph containers, proving exact asymptotic formulas (the $c_0, c_1$ equivalents) in the sparse random regime remains computationally and analytically out of reach.

## 7. Current Research (as of June 2026)

The resolution of the Cameron-Erdős Conjecture directly catalyzed the invention of the **Method of Hypergraph Containers** (Balogh, Morris, Samotij, 2015; Saxton, Thomason, 2015), which now dominates this sector of combinatorics. Current research, heavily concentrated at institutions like Cambridge, Oxford, and IMPA, leverages these tools to resolve generalized systems.

- **Arbitrary Linear Systems:** The frontier has moved to counting subsets of $[N]$ that avoid solutions to arbitrary systems of linear equations $\mathcal{L}(x_1, \dots, x_k) = 0$ (generalizations of Rado's criterion). Researchers are mapping the structural stability of such sets in high-dimensional integer lattices.
- **Non-Abelian Groups *(frontier — verify)*:** Researchers are currently attempting to establish exact enumerative bounds for sum-free sets in non-abelian groups (e.g., nilpotent groups and the Heisenberg group), where the lack of commutative Fourier analysis outright breaks Green's methodology.
- **Higher-Order Asymptotics:** Efforts are underway to determine the precise secondary terms in the asymptotic expansion of $|\mathcal{F}_N|$, moving beyond the leading constants $c_0, c_1$.

## 8. Future Work

Leading additive combinatorialists highlight several open pathways:
1. **Algorithmic Enumeration & Sampling:** Developing sub-exponential time algorithms to efficiently approximate the exact cardinality of $\mathcal{F}_N$, or to sample uniformly from the space of all sum-free sets in $[N]$. Currently, the structural theorems guarantee the sets exist, but generating them uniformly without massive rejection rates is unresolved.
2. **Structure of the Secondary Maximal Sets:** While the maximum sum-free sets are well understood, the distribution of the sizes of *all* maximal sum-free sets remains entirely unknown. 
3. **Density in the Primes:** Modifying the underlying set from $[N]$ to the primes up to $N$. Determining the exact number of sum-free subsets of primes relies heavily on advances in the Gowers norms and the Green-Tao machinery, and remains largely open.

## 9. Key References

- **[Foundational]** Cameron, P. J., & Erdős, P. *On the number of sets of integers with various properties.* Number Theory (Banff, AB, 1988), de Gruyter, Berlin, 61–79, 1990.
- **[Foundational]** Alon, N. *Independent sets in regular graphs and sum-free subsets of finite groups.* Israel Journal of Mathematics, 73(2), 247–256, 1991.
- **[SOTA / Recent]** Sapozhenko, A. A. *The Cameron-Erdős conjecture.* Doklady Mathematics, 68(1), 183–185, 2003.
- **[SOTA / Recent]** Green, B. *The Cameron-Erdős conjecture.* Bulletin of the London Mathematical Society, 36(6), 769–778, 2004.
- **[SOTA / Recent]** Balogh, J., Liu, H., Sharifzadeh, S., & Treglown, A. *The number of maximal sum-free subsets of integers.* Journal of the European Mathematical Society, 17(12), 2785–2835, 2015.
- **[Survey]** Samotij, W. *Counting independent sets in graphs.* European Journal of Combinatorics, 48, 5–18, 2015.

## 10. Worked Example / Concrete Special Case

To ground the abstract formula $O(2^{N/2})$, consider the small, concrete instance where $N = 5$. We want to find the exact number of sum-free sets in $[5] = \{1, 2, 3, 4, 5\}$. The total number of subsets is $2^5 = 32$.

First, we identify the two trivial extremal families:
1. The odd integers $O_5 = \{1, 3, 5\}$. The subsets of $O_5$ are guaranteed to be sum-free. There are $2^3 = 8$ such sets.
2. The upper half $U_5 = \{3, 4, 5\}$. The subsets of $U_5$ are guaranteed to be sum-free. There are $2^3 = 8$ such sets.

The intersection is $O_5 \cap U_5 = \{3, 5\}$, which produces $2^2 = 4$ sets counted twice. Thus, sets fully contained in either $O_5$ or $U_5$ account for $8 + 8 - 4 = 12$ sum-free sets.

To find the remaining sum-free sets, we must look for sets that contain elements not strictly bounded by $O_5$ or $U_5$. These "defect" sets must navigate the restrictive arithmetic of $[5]$.
Let's evaluate subsets based on cardinality:
- **Size 0 and 1:** $\emptyset, \{1\}, \{2\}, \{3\}, \{4\}, \{5\}$. (Total: 6 sets. All are sum-free. Note $\{2\}$ and $\{4\}$ are not in $O_5 \cup U_5$.)
- **Size 2:** There are $\binom{5}{2} = 10$ possible pairs. A pair is NOT sum-free if $x + x = y$. Thus, we must exclude the pairs $\{1, 2\}$ (since $1+1=2$) and $\{2, 4\}$ (since $2+2=4$). The remaining $10 - 2 = 8$ pairs are sum-free. The pairs not in $O_5 \cup U_5$ are $\{1, 4\}, \{2, 3\}, \{2, 5\}$.
- **Size 3:** There are $\binom{5}{3} = 10$ possible triplets. A triplet is NOT sum-free if it contains the forbidden pairs $\{1, 2\}$ or $\{2, 4\}$, or if it forms a solution $x+y=z$ with distinct elements. 
  The distinct equations in $[5]$ are: $1+2=3$, $1+3=4$, $1+4=5$, and $2+3=5$. 
  Every single triplet that triggers one of these equations or contains a forbidden pair must be discarded. Exhausting the list:
  - Contains $\{1, 2\}$: $\{1, 2, 3\}, \{1, 2, 4\}, \{1, 2, 5\}$
  - Contains $\{2, 4\}$: $\{1, 2, 4\}, \{2, 3, 4\}, \{2, 4, 5\}$
  - Distinct sums: $\{1, 3, 4\}, \{1, 4, 5\}, \{2, 3, 5\}$
  This excludes exactly 8 of the 10 triplets. The remaining 2 triplets are $\{1, 3, 5\}$ and $\{3, 4, 5\}$. Both are already fully contained in $O_5$ and $U_5$.
- **Size 4 and 5:** None are sum-free, as they inevitably trigger the Pigeonhole Principle on the integer partitions.

Total sum-free sets for $N=5$: $6 \text{ (size } \le 1) + 8 \text{ (size 2)} + 2 \text{ (size 3)} = 16$. 
This matches the theoretical foundation: the vast majority (12 out of 16) are structurally constrained to the trivial domains $O_5$ and $U_5$, with a rapidly decaying tail of 4 "exceptional" defect sets ($\{2\}, \{4\}, \{1, 4\}, \{2, 3\}, \{2, 5\}$), perfectly reflecting the behavior that generates the global asymptotic $O(2^{N/2})$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*