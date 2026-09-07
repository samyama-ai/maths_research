---
id: 01-number-theory/lander-parkin-selfridge-conjecture
title: "Lander-Parkin-Selfridge Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lander-Parkin-Selfridge Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/lander-parkin-selfridge-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Lander-Parkin-Selfridge Conjecture (often referred to in the context of equal sums of like powers) posits a lower bound on the number of terms required to form a non-trivial equality between sums of perfect $k$-th powers. 

Formally, if there exists a non-trivial solution to the Diophantine equation:
$$ \sum_{i=1}^m a_i^k = \sum_{j=1}^n b_j^k $$
where $k > 1$ is a positive integer, $a_1, \dots, a_m$ and $b_1, \dots, b_n$ are strictly positive integers, and the solution is non-trivial—meaning the multi-sets $\{a_1, \dots, a_m\}$ and $\{b_1, \dots, b_n\}$ are disjoint—then the total number of terms involved must satisfy the inequality:
$$ m + n \ge k $$

A complete proof of this conjecture would entail rigorously demonstrating that no solutions exist for $m + n < k$, effectively ruling out any "short" integer relations between high powers.

## 2. Mathematical Foundations

The conjecture belongs to the study of additive number theory and Diophantine equations. Let $S(k, m, n)$ denote the problem of finding integer solutions to the equation:
$$ \sum_{i=1}^m X_i^k - \sum_{j=1}^n Y_j^k = 0 $$
where $X_i, Y_j \in \mathbb{Z}^+$.

Geometrically, this equation defines a projective hypersurface $V$ over the rational numbers $\mathbb{Q}$ in the ambient projective space $\mathbb{P}^{m+n-1}(\mathbb{Q})$. The degree of this hypersurface is $k$. 
The conjecture claims that if $V$ contains any rational points that do not lie on the trivial locus (subvarieties defined by $X_i = Y_j$ for some $i, j$), then the dimension of the ambient projective space plus two must be greater than or equal to the degree of the hypersurface:
$$ (m + n - 1) + 1 \ge k \implies m + n \ge k $$

This conjecture acts as a modern, generalized replacement for Euler's sum of powers conjecture, integrating the theoretical bounds imposed by algebraic geometry (such as the genus and general type of higher-degree varieties) with empirical computational evidence.

## 3. History & State of the Art (SOTA)

In 1769, Leonhard Euler formulated his "sum of powers conjecture," which stated that $m \ge k$ when $n=1$. In other words, Euler believed that it took at least $k$ $k$-th powers to sum to another $k$-th power. 

Euler's conjecture stood for nearly two centuries until 1966, when L. J. Lander and T. R. Parkin used a CDC 6600 supercomputer to discover a counterexample for $k=5$:
$$ 27^5 + 84^5 + 110^5 + 133^5 = 144^5 $$
Because $m=4$ and $n=1$, Euler's conjecture ($m \ge 5$) was disproven. In 1967, expanding on this discovery, Lander, Parkin, and J. L. Selfridge proposed their broader conjecture that $m+n \ge k$. 

Later, in 1988, Noam Elkies found a geometric method using elliptic curves to systematically generate counterexamples to Euler's conjecture for $k=4$, yielding $m=3, n=1$. Elkies' discovery still respected the Lander-Parkin-Selfridge bound since $m+n = 4 \ge 4$. 

Today, the Lander-Parkin-Selfridge conjecture remains unbroken. Massive computational searches have verified the absence of counterexamples up to extremely large bounds, but a general theoretical proof remains out of reach.

## 4. Partial Results / Verified Cases

The conjecture has been proven for $k \le 4$:
- **For $k \le 3$:** The conjecture states $m+n \ge 3$. Fermat's Last Theorem for $k=3$ proves that $a^3 + b^3 = c^3$ has no non-trivial solutions (which would be $m+n=3$). Therefore, any valid solution requires $m+n > 3$, strictly satisfying the conjecture.
- **For $k = 4$:** The conjecture states $m+n \ge 4$. The only cases where $m+n < 4$ are $m=2, n=1$ and $m=1, n=2$. Both correspond to the equation $a^4 + b^4 = c^4$, which has no positive integer solutions per Fermat's Last Theorem for $k=4$. Thus, the conjecture is verified for all $k \le 4$.

For $k=5$, the conjecture implies $m+n \ge 5$. The open cases (potential counterexamples) are:
1. $a^5 + b^5 = c^5 + d^5$ ($m=2, n=2 \implies m+n=4 < 5$)
2. $a^5 + b^5 + c^5 = d^5$ ($m=3, n=1 \implies m+n=4 < 5$)

Computational searches have rigorously verified that no solutions exist for these $k=5$ equations for bases up to heavily constrained computational limits (well into the trillions). Similar empirical verifications have been conducted for $k=6$ and $a^6 + b^6 + c^6 = d^6 + e^6$.

## 5. Principal Obstacles

The main technical limitation in resolving the conjecture is the lack of effective tools in algebraic geometry for higher-dimensional varieties. 
- **Faltings' Theorem:** Faltings' Theorem (the Mordell Conjecture) establishes that curves (1-dimensional varieties) of genus $g \ge 2$ over $\mathbb{Q}$ have only finitely many rational points. However, equations like $a^5 + b^5 = c^5 + d^5$ define *surfaces* (2-dimensional varieties) in $\mathbb{P}^3$. Faltings' theorem does not generalize effectively to surfaces.
- **The Bombieri-Lang Conjecture:** For surfaces of general type (which includes $X^5 + Y^5 = Z^5 + W^5$, since its degree $d=5$ exceeds the dimension of the ambient space plus one), the Bombieri-Lang conjecture suggests the rational points are not Zariski dense. Even if proven, it would only imply that solutions are sparse (or finite outside of rational curves), not that they strictly do not exist.
- **The Hardy-Littlewood Circle Method:** Traditional analytic number theory techniques require the number of variables ($s = m+n$) to be significantly larger than the degree $k$ (e.g., $s > k^2$) to prove asymptotic behavior. The circle method cannot establish non-existence bounds when the number of variables is extremely small ($m+n < k$).

## 6. The Gap

The boundary between what is proven and the general statement lies at the intersection of local constraints and global geometry. Modular arithmetic and $p$-adic analysis (Hasse principle) often fail to obstruct solutions to these equations because local solutions exist for almost all primes $p$. The exact mathematical barrier is developing an arithmetic-geometric machinery capable of outright proving the emptiness of the rational point set on specific, high-degree hypersurfaces over $\mathbb{Q}$ when the dimension of the variety is $\ge 2$.

## 7. Current Research (as of June 2026)

Active research primarily flows through two channels:
1. **Algorithmic Searches:** Specialized algorithms utilizing highly optimized lattice reduction (LLL) and clever algebraic sieving methods are continuously running to push the empirical lower bounds for $k=5, 6, 7$. 
2. **Arithmetic Geometry:** The study of rational lines on surfaces of general type, particularly focusing on whether the trivial solutions form the entirety of the Picard group for these specific Fermat-like surfaces. Some researchers are attempting to bridge the gap using modern étale cohomology, though breakthroughs remain *frontier*.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- Expanding on Elkies' elliptic curve methodology to higher-genus fibrations in hopes of finding a structured way to either locate counterexamples for $k=5$ or prove that such fibrations contain no rational points of infinite order.
- Proving explicit versions of the Bombieri-Lang conjecture for Fermat surfaces, which could reduce the search space for potential counterexamples to a finite, computable bound.
- Advancing "descent" methods—historically successful for curves—into higher dimensions to establish theoretical barriers against solutions to $a^5 + b^5 = c^5 + d^5$.

## 9. Key References

- **[Foundational]** Lander, L. J., Parkin, T. R., and Selfridge, J. L. "A Survey of Equal Sums of Like Powers." *Mathematics of Computation*, 21(99), 1967.
- **[Foundational]** Lander, L. J., and Parkin, T. R. "Counterexample to Euler's conjecture on sums of like powers." *Bulletin of the American Mathematical Society*, 72(6), 1966.
- **[SOTA / Recent]** Elkies, N. D. "On $A^4 + B^4 + C^4 = D^4$." *Mathematics of Computation*, 51(184), 1988.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. Springer, 3rd Edition, 2004. (See Section D1).

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, consider the conjecture applied to the parameters $k=3$, $k=4$, and $k=5$.

**Case 1: $k=3$**
The renowned Ramanujan-Hardy taxicab number yields:
$$ 1^3 + 12^3 = 9^3 + 10^3 = 1729 $$
Here, $m=2$ terms equal $n=2$ terms. The sum is $m+n = 4$. The conjecture states $m+n \ge k$, which evaluates to $4 \ge 3$. This holds true.

**Case 2: $k=4$**
Elkies' counterexample to Euler's original conjecture provides:
$$ 2682440^4 + 15365639^4 + 18796760^4 = 20615673^4 $$
Here, $m=3$ terms equal $n=1$ term. The sum is $m+n = 4$. The conjecture requires $4 \ge 4$, which holds perfectly, showing that while Euler's requirement ($3 \ge 4$) failed, the Lander-Parkin-Selfridge bound succeeds.

**Case 3: $k=5$**
Lander and Parkin's original discovery:
$$ 27^5 + 84^5 + 110^5 + 133^5 = 144^5 $$
Here, $m=4$ terms equal $n=1$ term. The sum is $m+n = 5$. The conjecture states $5 \ge 5$, which is exactly tight. For this conjecture to be broken at $k=5$, someone would need to find a valid equality with $m+n = 4$, such as three 5th powers summing to one ($m=3, n=1$) or two 5th powers summing to two others ($m=2, n=2$).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*