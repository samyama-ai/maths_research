---
id: 01-number-theory/perfect-cuboid-problem
title: "Perfect Cuboid Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Perfect Cuboid Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/perfect-cuboid-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Perfect Cuboid Problem (also known as the Perfect Euler Brick Problem) asks whether there exists a cuboid (a rectangular parallelepiped) where all three of its edges, all three of its face diagonals, and its main space diagonal are all integers. 

Formally, the conjecture states that there exists no set of strictly positive integers $(a, b, c, d, e, f, g) \in \mathbb{Z}_{>0}^7$ that simultaneously satisfy the following system of Diophantine equations:
$$
\begin{cases}
a^2 + b^2 = d^2 \\
a^2 + c^2 = e^2 \\
b^2 + c^2 = f^2 \\
a^2 + b^2 + c^2 = g^2
\end{cases}
$$
where $a, b, c$ are the edge lengths, $d, e, f$ are the face diagonal lengths, and $g$ is the length of the space diagonal. The problem is to either find such a set of integers (thus proving existence) or rigorously prove that no such integers can exist.

## 2. Mathematical Foundations

The problem requires finding a rational point (other than the trivial origin or points with zero coordinates) on an algebraic variety. By dividing through by $g^2$, the system can be transformed into finding strictly positive rational solutions $(x, y, z)$ to the equations:
$$
x^2 + y^2 = u^2
$$
$$
x^2 + z^2 = v^2
$$
$$
y^2 + z^2 = w^2
$$
$$
x^2 + y^2 + z^2 = 1
$$
where $x, y, z, u, v, w \in \mathbb{Q}_{>0}$. 

Geometrically, this represents a system of quadrics. The intersection of these quadrics defines an algebraic surface $X$ in the projective space $\mathbb{P}^6$. The problem thus translates to determining the set of rational points $X(\mathbb{Q})$. 

The variety $X$ represents a surface of general type. Unlike algebraic curves (dimension 1), where Faltings' Theorem provides a deep structural limit on the number of rational points for curves of genus $g \ge 2$, surfaces of general type do not currently have a unified theorem analogous to Faltings' to guarantee finiteness or non-existence of rational points. The Bombieri-Lang conjecture suggests that rational points on surfaces of general type are not Zariski dense, but it does not rule out the existence of isolated rational points.

## 3. History & State of the Art (SOTA)

The history of the problem traces back to Paul Halcke (1719), who discovered the first "Euler brick" (a cuboid with integer edges and integer face diagonals, but a non-integer space diagonal). Leonhard Euler later provided a parametric solution that generates infinitely many Euler bricks.

Despite centuries of study, no perfect cuboid has ever been found. The problem saw a resurgence in the 20th century with the advent of computers. Maurice Kraitchik (1945) and John Leech (1977) formulated symmetries and modular constraints on the possible edge lengths. 

Modern computational searches have continually pushed the lower bounds for a potential perfect cuboid. Currently, it is known that the smallest edge of a perfect cuboid must exceed $3 \times 10^{12}$, and the space diagonal must exceed $9 \times 10^{12}$. On the theoretical side, algebraic geometers have studied the symmetries of the surface $X$ to find unramified covers or apply the Brauer-Manin obstruction, but local solutions (in $p$-adic fields) exist for all primes, meaning the Hasse principle does not strictly prevent a solution via local-global failures that are easily detectable.

## 4. Partial Results / Verified Cases

While the existence of a perfect cuboid remains unknown, numerous closely related problems and structural properties have been resolved:

1. **Euler Bricks Exist:** There are infinitely many cuboids where all edges and face diagonals are integers. The smallest is the Halcke brick with edges $(a, b, c) = (44, 117, 240)$.
2. **Almost Perfect Cuboids:** There are infinitely many cuboids where all edges, two face diagonals, and the space diagonal are integers.
3. **Complex Perfect Cuboids:** Perfect cuboids exist if one is allowed to use complex integers (e.g., Gaussian integers). A well-known example has edges $(a, b, c) = (ui, v, w)$ where the squares of the lengths are real.
4. **Modular Constraints:** If a perfect cuboid exists with edges $a, b, c$, strong divisibility conditions are proven. For instance:
   - One edge must be a multiple of 3.
   - One edge must be a multiple of 11.
   - One edge must be a multiple of 19.
   - At least one edge must be divisible by $2^4 = 16$.
   - The product of the edges $abc$ must be divisible by $2^6 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 \cdot 29 \cdot 37$.

## 5. Principal Obstacles

The primary bottleneck is the lack of a universal Diophantine theory for surfaces of general type. To solve Diophantine equations analytically, mathematicians often rely on mapping the problem to an elliptic curve (which has a well-understood group law) or a higher-genus curve (to invoke Faltings' Theorem). 

The perfect cuboid surface $X$ does not admit fibrations into elliptic curves over $\mathbb{Q}$ that would easily allow the determination of all rational points. Furthermore, the variety $X(\mathbb{Q}_p)$ is non-empty for all $p$-adic fields (meaning there are no local modular obstructions to a solution). Therefore, standard techniques such as the Hasse principle or simple modular arithmetic cannot rule out the existence of a perfect cuboid. Proving non-existence would require either demonstrating a novel Brauer-Manin obstruction on this specific surface or developing a major new theorem in arithmetic geometry.

## 6. The Gap

The boundary between what is known and what is unsolved lies in the final constraint: the space diagonal. We possess robust parametrizations for any three of the four Diophantine equations (e.g., the Saunderson parametrization for Euler bricks). The gap is the simultaneous intersection of this parameterized family with the fourth quadric $a^2 + b^2 + c^2 = g^2$. Bridging this gap requires either an unprecedentedly massive computation to find an unfathomably large solution or a breakthrough in rational point theory on algebraic surfaces to prove that the intersection of these specific four quadrics has no strictly positive rational points.

## 7. Current Research (as of June 2026)

Active research operates on two primary fronts:
1. **Computational:** Distributed computing efforts continue to expand the search space using highly optimized sieve methods and GPU-accelerated arithmetic, taking advantage of the strict modular constraints (e.g., searching only candidates where $a \equiv 0 \pmod{16}$).
2. **Arithmetic Geometry:** Algebraic geometers are actively mapping the automorphisms of the K3 surfaces and surfaces of general type associated with the cuboid equations. Recent works focus on computing the Picard rank of the surface and searching for rational curves embedded within it. There are periodic theoretical preprints attempting to definitively prove non-existence using descent methods or the étale Brauer-Manin obstruction, though these remain highly scrutinized * (frontier — verify) *.

## 8. Future Work

Leading mathematicians suggest that a resolution (if non-existence is true) will likely stem from advancements in the arithmetic of higher-dimensional varieties. Proposed strategies include:
- Finding a dominant rational map from a known rational variety to a surface that covers the perfect cuboid surface, and proving the covering surface has no rational points.
- Utilizing advanced lattice basis reduction (LLL algorithm) in combination with elliptic curve constraints to drastically narrow the high-dimensional search space for computational proofs of non-existence up to bounds where theoretical arguments might take over.

## 9. Key References

- **[Foundational]** Dickson, L. E. *History of the Theory of Numbers, Vol. II: Diophantine Analysis*. Carnegie Institution of Washington, 1920.
- **[SOTA / Recent]** Korec, I. "Lower bounds for perfect rational cuboids." *Mathematica Slovaca*, 42(5), 1992, pp. 565–582.
- **[SOTA / Recent]** Ulas, M. "Rational points on certain surfaces associated with perfect cuboids." *Colloquium Mathematicum*, 102, 2005, pp. 19-31.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. Springer, 3rd ed., 2004. (Section D18).

## 10. Worked Example / Concrete Special Case

To understand why the problem is difficult, we can examine the smallest known Euler brick (where the three face diagonals are integers, but the space diagonal fails the test). 

Consider the Halcke brick with edge lengths:
$$a = 44, \quad b = 117, \quad c = 240$$

Let us calculate the face diagonals $d, e, f$:
1. $d^2 = a^2 + b^2 = 44^2 + 117^2 = 1936 + 13689 = 15625$. Thus, $d = \sqrt{15625} = 125$.
2. $e^2 = a^2 + c^2 = 44^2 + 240^2 = 1936 + 57600 = 59536$. Thus, $e = \sqrt{59536} = 244$.
3. $f^2 = b^2 + c^2 = 117^2 + 240^2 = 13689 + 57600 = 71289$. Thus, $f = \sqrt{71289} = 267$.

All three face diagonals are perfectly integers. Now, we evaluate the space diagonal $g$:
$$g^2 = a^2 + b^2 + c^2 = 44^2 + 117^2 + 240^2 = 1936 + 13689 + 57600 = 73225$$
Taking the square root of $73225$:
$$g = \sqrt{73225} \approx 270.60118...$$
Because $73225$ is not a perfect square (it lies between $270^2 = 72900$ and $271^2 = 73441$), the space diagonal $g$ is irrational. This Euler brick comes remarkably close, but fails the fourth condition required to be a "perfect" cuboid.