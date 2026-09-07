---
id: 07-combinatorics/cap-set-problem
title: "Cap Set Problem"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cap Set Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/cap-set-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Cap Set Problem asks for the maximum possible size of a subset $A \subseteq \mathbb{F}_3^n$ such that $A$ contains no three distinct elements forming an arithmetic progression. In the context of the finite field $\mathbb{F}_3$, three elements $x, y, z$ form an arithmetic progression if and only if they sum to the zero vector, $x + y + z = 0$. Geometrically, this is equivalent to asking for the maximum size of a subset of the $n$-dimensional affine space over $\mathbb{F}_3$ that contains no complete affine line. 

Let $c_n$ denote the maximum size of a cap set in $\mathbb{F}_3^n$. The historical conjecture—often attributed to Frankl, Graham, and Rödl—was that $c_n = o(3^n)$. The modern, fully resolved asymptotic version of the problem establishes that $c_n$ is exponentially smaller than $3^n$, meaning there exists a constant $c < 3$ such that $c_n \le c^n$. 

The current open frontier of the Cap Set Problem is determining the exact value of the asymptotic base, known as the cap set capacity, defined as:
$$ c = \lim_{n \to \infty} (c_n)^{1/n} $$
A complete resolution of the problem now requires proving whether the true capacity matches the established upper bound of $c \approx 2.7552$, matches the current constructive lower bound of $c \approx 2.2202$, or lies strictly between them.

## 2. Mathematical Foundations

The problem is formalized in the $n$-dimensional vector space $V = \mathbb{F}_3^n$ over the finite field of three elements. A subset $A \subseteq V$ is defined as a *cap set* if for all $x, y, z \in A$, the equation:
$$ x + y + z = 0 $$
implies $x = y = z$. In $\mathbb{F}_3$, the relation $x + y + z = 0$ can be rewritten as $y = \frac{x+z}{2}$, which is the algebraic definition of a three-term arithmetic progression.

Because the Cartesian product of a cap set in $\mathbb{F}_3^n$ and a cap set in $\mathbb{F}_3^m$ is a cap set in $\mathbb{F}_3^{n+m}$, the sequence of maximal sizes $c_n$ is supermultiplicative:
$$ c_{n+m} \ge c_n c_m $$
By Fekete's Subadditive Lemma, this supermultiplicativity guarantees that the limit $c = \lim_{n \to \infty} (c_n)^{1/n}$ exists and is equal to $\sup_{n} (c_n)^{1/n}$.

The modern resolution of the exponential upper bound relies on the **slice rank** of a tensor, a concept introduced by Terence Tao to symmetricize the polynomial method of Croot, Lev, Pach, Ellenberg, and Gijswijt. For a field $\mathbb{F}$, a tensor $T: V \times V \times V \to \mathbb{F}$ has *slice rank 1* if it can be factored such that one variable is separated from the other two; i.e., it can be written in one of the following forms:
$$ f(x)g(y,z), \quad f(y)g(x,z), \quad \text{or} \quad f(z)g(x,y) $$
The slice rank of an arbitrary tensor $T$, denoted $\text{srank}(T)$, is the minimum integer $k$ such that $T$ can be expressed as a sum of $k$ tensors of slice rank 1. The fundamental theorem of this algebraic framework is that if $T$ is a diagonal tensor on $A \times A \times A$ (meaning $T(x,y,z) \neq 0$ if and only if $x=y=z$), then $\text{srank}(T) = |A|$.

## 3. History & State of the Art (SOTA)

The cap set problem has been a driving force in additive combinatorics for decades. In 1982, Brown and Buhler first proved that $c_n = o(3^n)$. This was significantly tightened by Meshulam in 1995, who adapted Roth's theorem and the Hardy-Littlewood circle method to finite fields, establishing $c_n \le 2 \cdot 3^n / n$. In 2012, Bateman and Katz achieved a major breakthrough in Fourier-analytic methods by proving $c_n = O(3^n / n^{1+\epsilon})$ for a small $\epsilon > 0$. However, Fourier methods were fundamentally incapable of proving an exponential bound.

The landscape was permanently altered in 2016. Croot, Lev, and Pach introduced a novel polynomial method to bound progression-free sets in $\mathbb{Z}_4^n$. Within weeks, Ellenberg and Gijswijt adapted this method to $\mathbb{F}_3^n$, proving the landmark result that $c_n \le O(c^n)$ for $c \approx 2.756$. Terence Tao subsequently streamlined their proof using the slice rank of tensors. 

On the constructive side (lower bounds), progress has been slow. Edel (2004) proved $c \ge 2.2173$ by identifying large cap sets in small dimensions (up to $n=6$) and taking tensor products. This bound stood for nearly two decades until Tyrrell (2022) made a marginal improvement to $c \ge 2.218$. 

In 2023, the state of the art for lower bounds was advanced by Google DeepMind's FunSearch, an AI system that combined Large Language Models (LLMs) with automated evaluators. By exploring the space of programmatic cap set generators rather than the sets themselves, FunSearch discovered novel, larger cap sets in $n=8$, raising the lower bound of the cap set capacity to $c \ge 2.2202$.

## 4. Partial Results / Verified Cases

The exact maximal size of a cap set, $c_n$, is only known for dimensions up to $n=6$. The verified exact values are:
- $c_1 = 2$
- $c_2 = 4$
- $c_3 = 9$
- $c_4 = 20$
- $c_5 = 45$ (Proved by Edel, Ferret, Landjev, and Storme in 2002)
- $c_6 = 112$ (Proved by Potechin in 2008 via an exhaustive, symmetry-breaking SAT-solver search)

For dimensions $n \ge 7$, exact exact maximums are unknown because the search space of $2^{3^n}$ subsets becomes computationally intractable. For $n=7$, the current bounds are $236 \le c_7 \le 293$. For $n=8$, FunSearch verified the existence of an independent cap set of size 512 that exhibits structural asymmetries not found in previous product-based constructions. 

The general asymptotic bounds currently stand precisely at:
$$ 2.2202^n \le c_n \le 3 \cdot (2.7552)^n $$

## 5. Principal Obstacles

The problem remains open regarding the exact capacity $c$ because both the analytic upper-bounding techniques and the constructive lower-bounding techniques have hit fundamental, hard mathematical barriers.

**1. The Density Increment Bottleneck (Fourier Analysis):**
Traditional methods evaluate the Fourier transform of the indicator function $\widehat{1_A}(\xi)$. If $A$ lacks 3-term arithmetic progressions, one can locate a non-zero frequency $\xi$ with a large Fourier coefficient and apply a density increment on a hyperplane. However, passing to a hyperplane reduces the ambient dimension and incurs a density loss. This "Bogolyubov-Ruzsa barrier" structurally limits Fourier methods to bounds of the form $O(3^n / \log^k n)$.

**2. Slice Rank Rigidity (Polynomial Method):**
The Ellenberg-Gijswijt upper bound relies on the specific polynomial:
$$ P(x,y,z) = \prod_{i=1}^n (1 - (x_i + y_i + z_i)^2) $$
By pigeonholing the degree of the monomials $x^\alpha y^\beta z^\gamma$ representing $P$, one variable must have a degree $\le 2n/3$. The upper bound is therefore dictated by the number of monomials in $n$ variables over $\mathbb{F}_3$ of degree $\le 2n/3$. Using Cramér's theorem for large deviations, this size is asymptotic to $c^n$, where $c = \min_{x > 0} \frac{1 + x + x^2}{x^{2/3}} \approx 2.7552$. This bound is completely rigid: it is a topological property of the space of monomials. There is no known mathematical operation to "compress" the slice rank further without breaking the diagonal property of the tensor.

**3. Computational Intractability:**
To find better lower bounds, one must search for cap sets in $n \ge 7$. The search space for $n=7$ is $2^{2187}$. Even heavily pruned branch-and-bound algorithms cannot traverse a space of this magnitude, making brute-force or traditional heuristic discovery impossible.

## 6. The Gap

The core mathematical gap is the discrepancy between $c \approx 2.2202$ and $c \approx 2.7552$. 

Closing this gap requires crossing a specific barrier: we must either prove that maximum cap sets are highly pseudo-random and unstructured (which would allow constructions approaching $2.7552^n$), or we must find a sharper algebraic invariant than slice rank. If the true capacity is $2.2202$, it implies that the polynomial $P(x,y,z)$ contains massive algebraic redundancies that the slice rank formulation is too coarse to detect.

## 7. Current Research (as of June 2026)

Active research operates along three primary axes:
1. **AI-Guided Programmatic Search:** Following the success of FunSearch, researchers at DeepMind and MIT are utilizing LLMs integrated with evolutionary algorithms to mutate programmatic generators, exploring the space of highly irregular, asymmetric cap sets in dimensions $n=7, 8, 9$.
2. **Higher-Order Slice Rank:** Algebraic geometers are attempting to generalize slice rank to higher-dimensional tensors and different algebraic varieties. By mapping the cap set problem to the geometry of schemes over finite fields, there is an active effort to lower the theoretical upper bound. *(frontier — verify)*
3. **Multi-color Sum-Free Equivalences:** Techniques developed for the cap set problem are being exported to adjacent problems, notably the Sunflower Conjecture and the Erdős-Szemerédi sunflower bounds, establishing deep categorical equivalences between arithmetic progressions and set-system intersections.

## 8. Future Work

Leading additive combinatorialists have suggested the following pathways to fully resolve the Cap Set Problem:
- **Determine the exact value of $c_7$:** Achieving this will likely require a hybrid approach combining SAT solvers, reinforcement learning, and new theoretical symmetry-breaking techniques. Knowing $c_7$ exactly would clarify whether the sequence $(c_n)^{1/n}$ plateaus or continues to grow.
- **Sub-slice-rank invariants:** Develop an algebraic invariant $I(T) \le \text{srank}(T)$ that is strictly smaller than the slice rank for the specific identity tensor $\prod (1 - (x_i + y_i + z_i)^2)$, but which still acts as an upper bound for the size of the diagonal subset $A$.
- **Randomized tensor products:** Investigate the asymptotic behavior of randomized, non-Cartesian product constructions (e.g., twisted products of $n=5$ and $n=6$ cap sets) to push the lower bound closer to $2.5$.

## 9. Key References

- **[Foundational]** Meshulam, R. *On subsets of finite abelian groups with no 3-term arithmetic progressions.* Journal of Combinatorial Theory, Series A, 1995. 
- **[Foundational]** Ellenberg, J. S., & Gijswijt, D. *On large subsets of $\mathbb{F}_q^n$ with no three-term arithmetic progression.* Annals of Mathematics, 2017.
- **[SOTA / Recent]** Romera-Paredes, B., et al. *Mathematical discoveries from program search with large language models.* Nature, 2023.
- **[Survey]** Tao, T. *A symmetric formulation of the Croot-Lev-Pach-Ellenberg-Gijswijt capset bound.* Blog post / Preprint, 2016.
- **[Survey]** Lovett, S. *The algebraic method in additive combinatorics and computer science.* Bulletin of the American Mathematical Society, 2017.

## 10. Worked Example / Concrete Special Case

To ground the problem, we prove that the maximum size of a cap set in $n=2$ dimensions is $c_2 = 4$. 

The vector space $\mathbb{F}_3^2$ contains $3^2 = 9$ points. An affine line in this space is defined by an equation $ax + by = c \pmod 3$. There are 4 distinct directions (parallel classes) of lines, corresponding to slopes $0, 1, 2,$ and $\infty$. Each parallel class partitions the 9 points into exactly 3 parallel lines of size 3. Consequently, there are $4 \times 3 = 12$ total lines in $\mathbb{F}_3^2$.

Assume for the sake of contradiction that there exists a cap set $C \subset \mathbb{F}_3^2$ of size $|C| = 5$. 
By definition, a cap set contains no complete line, so $|C \cap L| \le 2$ for any line $L$. 

Consider a single parallel class consisting of three lines $L_1, L_2, L_3$. Because these lines partition the space, the sum of the intersections must be the total size of the cap set:
$$ |C \cap L_1| + |C \cap L_2| + |C \cap L_3| = 5 $$
Since each intersection is bounded by 2, the only integer partition of 5 into three parts of size at most 2 is $2 + 2 + 1$. Therefore, in *every* parallel class, exactly two lines contain 2 points of $C$, and one line contains 1 point of $C$.

Any line $L$ that intersects $C$ in 2 points contains exactly $\binom{2}{2} = 1$ pair of points from $C$. A line intersecting in 1 point contains $\binom{1}{2} = 0$ pairs. Thus, each parallel class contains exactly $1 + 1 + 0 = 2$ pairs of points from $C$. 

Since there are 4 parallel classes, and every pair of points in $C$ defines exactly one unique line, the total number of pairs of points in $C$ must be:
$$ 4 \text{ classes} \times 2 \text{ pairs/class} = 8 \text{ pairs} $$

However, the total number of pairs in a set of size 5 is trivially given by the binomial coefficient:
$$ \binom{5}{2} = 10 \text{ pairs} $$

This yields the contradiction $8 = 10$. Therefore, no cap set of size 5 can exist in $\mathbb{F}_3^2$. A cap set of size 4 is easily constructed (e.g., $C = \{(0,1), (0,2), (1,0), (2,0)\}$), proving $c_2 = 4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*