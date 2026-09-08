---
id: 01-number-theory/eulers-sum-of-powers-conjecture
title: "Euler's Sum of Powers Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Euler's Sum of Powers Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/eulers-sum-of-powers-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Euler's sum of powers conjecture, proposed by Leonhard Euler in 1769 as a generalization of Fermat's Last Theorem, posits that for any integer $k > 2$, the sum of $k-1$ strictly positive $k$-th powers cannot equal a $k$-th power. 

More formally, the conjecture states that the Diophantine equation
$$ \sum_{i=1}^{k-1} a_i^k = b^k $$
has no solutions where $a_1, a_2, \dots, a_{k-1}$ and $b$ are all strictly positive integers. To prove the conjecture for a given $k$ would be to demonstrate the non-existence of such solutions, while disproving it requires finding at least one counterexample (a set of positive integers satisfying the equation).

## 2. Mathematical Foundations

The conjecture can be framed in the language of Diophantine geometry by considering the homogeneous equation:
$$ X_1^k + X_2^k + \dots + X_{k-1}^k - Y^k = 0 $$
This equation defines a projective hypersurface $V \subset \mathbb{P}^{k-1}$ over the rational numbers $\mathbb{Q}$. Finding a positive integer solution to Euler's conjecture is equivalent to finding a rational point $[X_1 : X_2 : \dots : X_{k-1} : Y] \in V(\mathbb{Q})$ where all coordinates can be chosen to be strictly positive integers.

A critical geometric property of this family of hypersurfaces is that the degree of the equation ($d = k$) exactly equals the dimension of the ambient projective space ($n = k-1$) plus one. By the adjunction formula, the canonical bundle $\mathcal{O}_V(d - n - 1)$ simplifies to $\mathcal{O}_V(0)$. Thus, for every $k \ge 3$, the variety $V$ is a Calabi-Yau manifold of dimension $k-2$:
- For $k = 3$, it is a Calabi-Yau 1-fold (an elliptic curve).
- For $k = 4$, it is a Calabi-Yau 2-fold (a K3 surface).
- For $k \ge 5$, it is a higher-dimensional Calabi-Yau manifold.

The arithmetic of rational points on Calabi-Yau manifolds is central to understanding the existence of solutions.

## 3. History & State of the Art (SOTA)

Leonhard Euler formulated this conjecture in 1769 after studying Fermat's Last Theorem, which states that $a^n + b^n = c^n$ has no solutions for $n > 2$. Euler hypothesized that the number of terms required to sum to an $n$-th power must be at least $n$.

The conjecture stood for nearly two centuries until 1966, when L. J. Lander and T. R. Parkin used a CDC 6600 supercomputer to discover a counterexample for $k=5$.

In 1987, Noam Elkies achieved a major theoretical breakthrough for $k=4$. By analyzing the underlying K3 surface $X_1^4 + X_2^4 + X_3^4 = Y^4$, Elkies found an elliptic curve lying on this surface with a positive rank over $\mathbb{Q}$. This proved that rational points are Zariski dense on the surface, yielding an infinite family of counterexamples. Shortly thereafter in 1988, Roger Frye used Elkies' theoretical framework to conduct a targeted computer search, identifying the absolute smallest counterexample for $k=4$.

The problem remains unsolved for $k \ge 6$.

## 4. Partial Results / Verified Cases

The conjecture has been fully resolved for $k \le 5$, with different outcomes depending on the parameter:

- **$k=3$ (True):** The conjecture states that $a^3 + b^3 = c^3$ has no solutions, which is exactly Fermat's Last Theorem for $n=3$. Euler proved this using the method of infinite descent.
- **$k=4$ (False):** Elkies proved an infinite number of solutions exist. The absolute smallest, found by Frye, is:
  $$ 95800^4 + 217519^4 + 414560^4 = 422481^4 $$
- **$k=5$ (False):** Lander and Parkin provided a counterexample:
  $$ 27^5 + 84^5 + 110^5 + 133^5 = 144^5 $$
- **$k \ge 6$ (Open):** No counterexamples have been found, nor has there been any proof that solutions cannot exist. For instance, whether five strictly positive 6th powers sum to a 6th power is currently unknown.

## 5. Principal Obstacles

The main bottleneck for resolving the conjecture for $k \ge 6$ is the difficulty of studying rational points on higher-dimensional Calabi-Yau manifolds. 

For $k=4$, Elkies could exploit the rich geometric theory of K3 surfaces—specifically, the existence of a genus 1 curve (an elliptic curve) on the surface $V$. Once an elliptic curve with positive rank is identified, it generates infinitely many rational points. 

For $k \ge 5$, the variety $V$ is a Calabi-Yau 3-fold (or higher). The Diophantine geometry of Calabi-Yau 3-folds and 4-folds is profoundly underdeveloped compared to K3 surfaces. Mathematicians lack systematic methods to determine if these higher-dimensional varieties contain curves of genus $\le 1$ over $\mathbb{Q}$, or if rational points are Zariski dense. Without these geometric structures, we cannot narrow down the search space. Consequently, finding counterexamples for $k=6$ relies heavily on brute-force computational searches, which quickly become intractable due to the exponential growth of combinations at higher powers.

## 6. The Gap

The boundary between what is known and what remains unsolved lies precisely at $k = 6$. The fundamental gap is whether the existence of solutions for $k=4$ and $k=5$ is a low-dimensional coincidence or representative of a general property of Calabi-Yau Fermat hypersurfaces. Bridging this gap requires either vast leaps in computational lattice reduction algorithms capable of scanning astronomically large search spaces or entirely new theoretical frameworks in arithmetic geometry to bound or locate rational points on Calabi-Yau $n$-folds ($n \ge 4$).

## 7. Current Research (as of June 2026)

Active research primarily focuses on computational and arithmetic geometry approaches:
- **Massive Distributed Computing:** Large-scale computing projects continue to raise the lower bounds for $k=6$ and $k=7$ using highly optimized algorithms filtering modulo large primes.
- **Arithmetic Geometry:** Several theoretical groups are investigating the motives and Picard ranks of Fermat-like Calabi-Yau 3-folds and 4-folds.
- *(frontier — verify)* The application of machine learning and heuristic models to predict the existence of rational points on algebraic varieties is gaining traction, providing targeted bounding boxes to narrow classical lattice-reduction searches.

## 8. Future Work

Leading mathematicians suggest the following research pathways:
- Formulate a generalization of Elkies' method by investigating whether Calabi-Yau 3-folds and 4-folds contain algebraically tractable subvarieties (such as K3 surfaces with high Picard number) over $\mathbb{Q}$ that might harbor rational points.
- Improve theoretical bounds on the density of rational points for higher-degree Fermat hypersurfaces to either suggest solutions are plentiful or to rigorously prove they are non-existent for sufficiently large $k$.

## 9. Key References

- **[Foundational]** L. Euler. *Observationes circa biquadrata*. Novi Commentarii academiae scientiarum Petropolitanae, 1772.
- **[SOTA / Recent]** N. D. Elkies. *On $A^4 + B^4 + C^4 = D^4$*. Mathematics of Computation, 51(184):825-835, 1988.
- **[SOTA / Recent]** L. J. Lander and T. R. Parkin. *Counterexample to Euler's conjecture on sums of like powers*. Bulletin of the American Mathematical Society, 72(6):1079, 1966. [DOI](https://doi.org/10.1090/s0002-9904-1966-11654-3)
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory*. Springer, 3rd Edition, 2004.

## 10. Worked Example / Concrete Special Case

To ground the conjecture in a concrete calculation, consider the $k=5$ counterexample discovered by Lander and Parkin in 1966. The conjecture for $k=5$ posited that the equation $a^5 + b^5 + c^5 + d^5 = e^5$ has no strictly positive integer solutions.

Lander and Parkin identified the following 5th powers:
- $a = 27 \implies 27^5 = 14,348,907$
- $b = 84 \implies 84^5 = 4,182,119,424$
- $c = 110 \implies 110^5 = 16,105,100,000$
- $d = 133 \implies 133^5 = 41,615,795,893$

Summing these terms yields:
$$ 14,348,907 + 4,182,119,424 + 16,105,100,000 + 41,615,795,893 = 61,917,364,224 $$

Taking the 5th root of the sum:
$$ \sqrt[5]{61,917,364,224} = 144 $$

Since $144$ is exactly an integer, we see that $144^5 = 61,917,364,224$. This single calculation directly contradicts Euler's statement, conclusively disproving the general conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*