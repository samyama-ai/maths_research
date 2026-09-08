---
id: 01-number-theory/erdos-ulam-problem
title: "Erdos Ulam Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Ulam Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-ulam-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Erdős-Ulam problem (sometimes referred to as Ulam's question) asks whether there exists a subset $S$ of the Euclidean plane $\mathbb{R}^2$ such that $S$ is dense in $\mathbb{R}^2$ and the Euclidean distance between any two points $p, q \in S$ is a rational number.

The problem is widely conjectured to have a negative answer: no such dense rational-distance set exists in the plane. A complete mathematical proof would demonstrate that any set $S \subset \mathbb{R}^2$ with pairwise rational distances must be nowhere dense (e.g., asserting that all but finitely many points must be contained within a single line or a single circle).

## 2. Mathematical Foundations

Let $\mathbb{R}^2$ be the Euclidean plane. The distance between points $p = (x_1, y_1)$ and $q = (x_2, y_2)$ is given by the standard metric:
$$d(p, q) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

A set $S \subseteq \mathbb{R}^2$ is a *rational distance set* if for all $p, q \in S$, $d(p, q) \in \mathbb{Q}$.
The set $S$ is *dense* in $\mathbb{R}^2$ if its topological closure $\bar{S}$ equals $\mathbb{R}^2$ with respect to the standard topology.

The problem is deeply connected to Diophantine geometry and the theory of algebraic surfaces. An algebraic variety $V$ over a number field $K$ is of *general type* if its Kodaira dimension equals its complex dimension. The **Bombieri-Lang Conjecture** states that if $V$ is a variety of general type defined over a number field $K$, then the set of $K$-rational points $V(K)$ is not Zariski dense in $V$. Similarly, the **$abc$-conjecture** bounds the prime factors of integers satisfying $a+b=c$, which profoundly limits the rational points on certain algebraic curves and surfaces.

## 3. History & State of the Art (SOTA)

The question was originally formulated by Stanisław Ulam in 1945 and widely popularized by Paul Erdős.
- **1945**: Paul Erdős and Norman Anning proved that any infinite set of points in the plane with *integer* distances must be collinear. However, this proof fundamentally relied on the discrete nature of integers and could not be extended to rational numbers.
- **2010**: József Solymosi and Frank de Zeeuw proved Erdős's conjecture for the case of algebraic curves, showing that no irreducible algebraic curve other than a line or a circle can contain an infinite rational distance set.
- **2017**: Hector Pasten demonstrated that a uniform version of the $abc$-conjecture implies a negative answer to the Erdős-Ulam problem.
- **2018**: Jafar Shaffaf established a deep geometric link, proving that assuming the Bombieri-Lang conjecture for algebraic surfaces, the Erdős-Ulam problem is solved in the negative.

Despite these massive theoretical leaps, the problem remains unconditionally open.

## 4. Partial Results / Verified Cases

- **Integer Distances**: The Erdős-Anning theorem resolves the integer analogue completely: any infinite set in $\mathbb{R}^2$ with integer distances must lie on a single straight line.
- **Infinite Non-Collinear Rational Sets**: It is known that infinite rational distance sets exist and can be dense on one-dimensional algebraic curves. For example, one can construct a dense set of rational points on the unit circle $\mathbb{S}^1$ where pairwise chordal distances are rational.
- **Algebraic Curves Constraint**: Solymosi and de Zeeuw (2010) unconditionally proved that if an infinite rational distance set lies on a plane algebraic curve, that curve must be a straight line or a circle.
- **Conditional Solutions**: It is proven that no dense rational distance set exists in the plane *if* the Bombieri-Lang conjecture is true (Shaffaf, 2018), or *if* the $abc$-conjecture is true (Pasten, 2017).

## 5. Principal Obstacles

Standard geometric and combinatorial techniques fail precisely because of the dense nature of rational numbers. In the integer case (Erdős-Anning), the triangle inequality bounds the differences in distances from any point to a finite set of integers, restricting points to a finite union of hyperbolas. Because rational numbers do not possess a minimum positive difference, this "discreteness" argument breaks down entirely, allowing for infinitely many hyperbolas that can intersect in dense patterns.

To solve the problem algebraically, one must study the surfaces defined by the distance constraints $x_{ij}^2 + y_{ij}^2 = d_{ij}^2$. When considering multiple points in the putative dense set, the resulting algebraic surface is of *general type*. Proving unconditionally that rational points on arbitrary surfaces of general type are not Zariski dense requires solving the Bombieri-Lang conjecture, which is widely considered one of the most impenetrable problems in modern arithmetic geometry.

## 6. The Gap

The precise mathematical boundary lies between conditional arithmetic geometry and unconditional Diophantine bounds. To cross this gap unconditionally, one must prove that rational points are not Zariski dense for the *specific, restricted class of surfaces of general type* that arise from planar Euclidean distance equations, without needing to prove the full, generalized Bombieri-Lang or $abc$-conjectures. Current Diophantine techniques (like Faltings's Theorem or the Chabauty-Coleman method) operate unconditionally on curves (dimension 1), but extending these to the higher-dimensional surfaces required by the Erdős-Ulam problem remains a massive barrier.

## 7. Current Research (as of June 2026)

Active research remains highly concentrated in Diophantine geometry and model theory:
- **Diophantine Geometry**: Arithmetic geometers are attempting to explicitly describe the canonical divisors and automorphisms of the specific "distance varieties" to find an unconditional geometric proof of rational paucity.
- **Logic and Definability**: Following Pasten's work, logicians are studying the definability of integers within rings of integers to find alternative, weaker arithmetic conditions that might suffice to prove the theorem.
- *(frontier — verify)* Non-abelian Chabauty methods and refined Selmer group bounds are being investigated for application to the highly symmetric surfaces of general type generated by Erdős-Ulam configurations.

## 8. Future Work

Leading researchers suggest two primary pathways for future breakthroughs:
1.  **Specialized Surface Bounds**: Isolate the moduli space of the Erdős-Ulam distance surfaces. If one can show that these specific algebraic surfaces contain algebraic curves of genus $\le 1$ that cannot form a dense subset, an unconditional proof bypassing Bombieri-Lang might be achievable.
2.  **Higher Dimensional Analogues**: Analyzing the problem in $\mathbb{R}^3$ or higher. In higher dimensions, the algebraic constraints become even more rigid (the associated varieties are of higher dimension but lower relative degree), potentially offering an easier unconditional rigidity proof that could subsequently be projected down to $\mathbb{R}^2$.

## 9. Key References

- **[Foundational]** Erdős, P., & Anning, N. H. *Integral distances*. Bulletin of the American Mathematical Society, 1945. [DOI](https://doi.org/10.1090/s0002-9904-1945-08490-0)
- **[Foundational]** Solymosi, J., & de Zeeuw, F. *On a question of Erdős and Ulam*. Discrete & Computational Geometry, 2010. [DOI](https://doi.org/10.1007/s00454-009-9179-x)
- **[SOTA / Recent]** Pasten, H. *Definability of Frobenius orbits and a result on rational distance sets*. Monatshefte für Mathematik, 2017. [DOI](https://doi.org/10.1007/s00605-016-0973-2)
- **[SOTA / Recent]** Shaffaf, J. *A solution of the Erdős-Ulam problem on rational distance sets assuming the Bombieri-Lang conjecture*. Discrete & Computational Geometry, 2018. [DOI](https://doi.org/10.1007/s00454-018-0003-3)

## 10. Worked Example / Concrete Special Case

To understand why the Erdős-Anning theorem succeeds for integers but fails for rationals, consider three non-collinear points $A, B, C$ in the plane. We wish to place a fourth point $P$ such that $d(P, A)$ and $d(P, B)$ are both of the same arithmetic type (integer or rational). 

By the triangle inequality:
$$ |d(P, A) - d(P, B)| \le d(A, B) $$

**Case 1: Distances are integers.**
If the distance $d(A, B)$ is a fixed integer $k$, the difference $|d(P, A) - d(P, B)|$ must be an integer $m \in \{0, 1, 2, \dots, k\}$.
The geometric locus of points $P$ satisfying $|d(P, A) - d(P, B)| = m$ is a hyperbola (or a straight line if $m=0$ or $m=k$) with foci $A$ and $B$.
Since there are only $k+1$ possible integer values for $m$, the point $P$ is constrained to lie on a finite union of hyperbolas. Applying this logic to points $B$ and $C$ produces another finite set of hyperbolas. The intersection of these two finite sets yields only a *finite* number of possible locations for $P$. Thus, an infinite set of points with integer distances cannot spread out into the plane; they must be collinear.

**Case 2: Distances are rational (Erdős-Ulam).**
If the distance $d(A, B)$ is a fixed rational $q$, the difference $|d(P, A) - d(P, B)|$ can be *any* rational number $r \in [0, q]$.
Because the rational numbers are dense, there are *infinitely many* possible values for $r$. This generates an infinite, dense family of hyperbolas. The intersection of these infinite families of hyperbolas for multiple pairs of foci allows for infinitely many intersection points. This illustrates why the simple combinatorial constraint fails for rationals, leaving the Erdős-Ulam problem an open question solvable only through deep algebraic geometry.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*