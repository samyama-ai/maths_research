---
id: 01-number-theory/erdos-graham-problem
title: "Erdos-Graham Problem"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Graham Problem

> **Topic:** 01-number-theory · **ID:** `01-number-theory/erdos-graham-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Erdős–Graham problem (also known as the Erdős–Graham conjecture on Egyptian fractions) asks whether, for any partition of the integers greater than 1 into finitely many subsets, at least one of the subsets contains a finite collection of integers whose reciprocals sum exactly to 1.

Formally, if the set of integers $\mathbb{Z}_{\ge 2} = \{2, 3, 4, \dots\}$ is partitioned into $r$ disjoint subsets (colors) such that $\mathbb{Z}_{\ge 2} = A_1 \cup A_2 \cup \dots \cup A_r$, does there always exist an index $i \in \{1, \dots, r\}$ and a finite subset $S \subset A_i$ such that:
$$ \sum_{n \in S} \frac{1}{n} = 1 $$

A strictly stronger statement, known as the **density conjecture**, posits that any subset of the natural numbers with strictly positive upper density must inherently contain a finite subset whose reciprocals sum to 1, regardless of how the set was partitioned. Both the original coloring conjecture and the density conjecture have been proven to be true.

## 2. Mathematical Foundations

The problem lies at the intersection of Ramsey theory, additive combinatorics, and analytic number theory.

- **Egyptian Fractions:** An Egyptian fraction is a representation of a rational number as a sum of distinct unit fractions (fractions with a numerator of 1). The constraint mathematically requires finding a set $S$ satisfying $\sum_{n \in S} \frac{1}{n} = 1$.
- **Upper Density:** The upper density of a subset $A \subseteq \mathbb{N}$ is defined as the limit supremum of the proportion of the set in the first $N$ integers:
  $$ \overline{d}(A) = \limsup_{N \to \infty} \frac{|A \cap [1, N]|}{N} $$
- **Diophantine Equivalence:** Finding a set $S \subset A$ that sums to 1 is algebraically equivalent to solving a highly non-linear symmetric Diophantine equation of degree $|S|$ over the set $A$:
  $$ \sum_{n \in S} \prod_{m \in S \setminus \{n\}} m = \prod_{n \in S} n $$

## 3. History & State of the Art (SOTA)

- **1980:** Paul Erdős and Ronald Graham formally proposed the coloring conjecture in their monograph *Old and New Problems and Results in Combinatorial Number Theory*. Erdős famously offered a cash prize for its resolution, recognizing its difficulty due to the highly non-linear nature of unit fractions.
- **2003:** Ernie Croot achieved a major breakthrough by proving the coloring version of the conjecture. He adapted the Hardy-Littlewood circle method to discrete harmonic analysis over $\mathbb{Z}/q\mathbb{Z}$.
- **2021/2025:** Thomas Bloom solved the much stronger density version of the conjecture (preprint released in 2021, published in 2025). Bloom built upon Croot's foundational Fourier analysis techniques but introduced highly optimized methods for estimating the $L^1$ norms of the associated exponential sums, securing a proof that density strictly bounds the existence of Egyptian fraction representations.

## 4. Partial Results / Verified Cases

Because the density version of the conjecture has been proven, the verified cases now cover all subsets satisfying the density condition:

- **The Coloring Version (Verified):** Proven by Croot (2003). Any finite $r$-coloring of $\mathbb{Z}_{\ge 2}$ will yield at least one monochromatic subset $S$ such that $\sum_{n \in S} 1/n = 1$.
- **The Density Version (Verified):** Proven by Bloom (2021). Any set $A \subseteq \mathbb{N}$ with $\overline{d}(A) > 0$ contains a finite $S \subset A$ such that $\sum_{n \in S} 1/n = 1$. 
- **Sub-linear Quantitative Bounds (Verified):** Bloom's theorem actually extends beyond strictly positive density. He proved the result holds for zero-density sets that decay slowly enough, specifically any set $A$ satisfying $|A \cap [1, N]| \ge \frac{N}{(\log \log N)^c}$ for a sufficiently small absolute constant $c > 0$.

## 5. Principal Obstacles

Historically, the Erdős–Graham problem resisted standard additive combinatorics techniques (like those used to prove Szemerédi's theorem) because the constraint $\sum 1/n = 1$ entirely lacks translation invariance. 

Analytically, researchers attempt to count solutions using the Hardy-Littlewood circle method via the integral:
$$ \int_0^1 \left( \sum_{n \in A} e^{2\pi i \alpha / n} \right)^k e^{-2\pi i \alpha} \, d\alpha $$
However, the variables $1/n$ are rational. To apply standard Fourier bounds on minor arcs, one must clear denominators by multiplying by $L = \text{lcm}(n \in A)$. Because the lowest common multiple of a set of integers grows exponentially, the resulting coefficients $L/n$ vary wildly and are intractably large. This causes classical Weyl bounds on the exponential sums to blow up and fail completely. Croot and Bloom bypassed this by factoring the variables over primes and bounding the $L^p$ norms of the exponential sums continuously without relying on a global denominator.

## 6. The Gap

With the density conjecture fully resolved, the remaining mathematical gap lies in determining the precise behavior of **zero-density sets** whose reciprocal sums diverge. 

It is known that the sum of the reciprocals of the primes diverges ($\sum 1/p = \infty$), yet no finite subset of primes can sum to an integer, demonstrating that divergence alone is insufficient to guarantee an Egyptian fraction of 1. Bloom established that sets of size $\frac{N}{(\log \log N)^c}$ contain solutions, while primes (of size $\frac{N}{\log N}$) do not. The precise mathematical gap is finding the exact critical threshold function $f(N)$ for the counting function $|A \cap [1, N]|$ where the property transitions from guaranteed existence to structural failure.

## 7. Current Research (as of June 2026)

- **Optimizing Quantitative Bounds:** Researchers are actively working to shrink the gap between Bloom's logarithmic bound ($1/(\log \log N)^c$) and the prime density barrier ($1/\log N$) to find the true threshold for zero-density Egyptian fractions.
- **Formal Verification:** There is an active movement to formalize deep results in additive combinatorics using proof assistants like Lean. Thomas Bloom and the Lean mathlib community are heavily involved in digitizing these proofs to create verified libraries of exponential sum estimates. *(frontier — verify)*
- **Arbitrary Rational Targets:** Generalizing the density results to find representations for arbitrary rational targets $p/q$ using subsets restricted by specific prime factorizations.

## 8. Future Work

Leading mathematicians suggest exploring variations of the problem where the denominators are constrained to specific sparse sequences (such as the shifted primes $\{p-1\}$ or polynomial sequences $\{n^2 + 1\}$). Another major open pathway is linking the newly developed $L^1$ norm estimates for exponential sums to the notoriously open **Erdős–Straus conjecture**, which conjectures that $4/n = 1/x + 1/y + 1/z$ always has a solution for $n \ge 2$.

## 9. Key References

- **[Foundational]** P. Erdős and R. L. Graham. *Old and New Problems and Results in Combinatorial Number Theory*. Monographies de L'Enseignement Mathématique, 1980.
- **[SOTA / Recent]** T. F. Bloom. *On a density conjecture about unit fractions*. Journal of the European Mathematical Society (JEMS), 27(11), 2025.
- **[SOTA / Recent]** E. S. Croot III. *On a coloring conjecture about unit fractions*. Annals of Mathematics, 157(2), 2003.
- **[Survey]** T. F. Bloom and C. Elsholtz. *Egyptian fractions*. Nieuw Archief voor Wiskunde, 2022.

## 10. Worked Example / Concrete Special Case

Consider a simple $2$-coloring partition of $\mathbb{Z}_{\ge 2}$ into **even** and **odd** numbers. The Erdős–Graham problem asserts that at least one of these color classes contains a finite subset whose reciprocals sum to exactly $1$. In this specific case, *both* color classes inherently contain such a subset.

For the **even** numbers, we can find a small, simple subset $S_{\text{even}} = \{2, 4, 6, 12\}$:
$$ \frac{1}{2} + \frac{1}{4} + \frac{1}{6} + \frac{1}{12} = \frac{6 + 3 + 2 + 1}{12} = \frac{12}{12} = 1 $$

For the **odd** numbers, finding a monochromatic subset summing to 1 is more computationally demanding but explicitly possible. Let $S_{\text{odd}} = \{3, 5, 7, 9, 11, 15, 21, 135, 10395\}$. We can verify the sum by grouping terms:
$$ \left(\frac{1}{3} + \frac{1}{5} + \frac{1}{15}\right) = \frac{5 + 3 + 1}{15} = \frac{9}{15} = \frac{3}{5} $$
$$ \left(\frac{1}{7} + \frac{1}{21}\right) = \frac{3 + 1}{21} = \frac{4}{21} $$
Now, add the remaining terms using the common denominator $10395$:
$$ \frac{3}{5} + \frac{4}{21} + \frac{1}{9} + \frac{1}{11} + \frac{1}{135} + \frac{1}{10395} $$
Converting each fraction to have a denominator of $10395$:
$$ \frac{6237}{10395} + \frac{1980}{10395} + \frac{1155}{10395} + \frac{945}{10395} + \frac{77}{10395} + \frac{1}{10395} = \frac{10395}{10395} = 1 $$
This explicitly confirms that both finite partitions natively harbor a monochromatic solution to the Diophantine equation.