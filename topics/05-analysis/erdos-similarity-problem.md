---
id: 05-analysis/erdos-similarity-problem
title: "Erdos Similarity Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Similarity Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/erdos-similarity-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The Erdős Similarity Problem (also known as the Erdős Similarity Conjecture) is a profound open question in geometric measure theory and real analysis that asks whether there exists any infinite sequence of real numbers that can be affinely embedded into every set of positive Lebesgue measure. 

The conjecture states: For every infinite sequence of real numbers $A$ converging to zero, there exists a Lebesgue measurable set $E \subset \mathbb{R}$ of positive measure such that $E$ contains no affine copy of $A$. 

In other words, the conjecture posits that no infinite sequence $A$ can be a "measure universal set." A complete proof requires demonstrating a method to construct a positive measure set $E$ that successfully avoids affine copies of $A$ for all infinite sequences, or alternatively, constructing a specific infinite sequence $A$ and proving it forces its way into every single set of positive Lebesgue measure (which would disprove the conjecture).

## 2. Mathematical Foundations

The problem is rigorously formulated within the framework of Lebesgue measure theory and real analysis.

- **Lebesgue Measure Space:** Let $(\mathbb{R}, \mathcal{L}, m)$ be the standard Lebesgue measure space, where $\mathcal{L}$ is the $\sigma$-algebra of Lebesgue measurable sets and $m$ is the Lebesgue measure. A set $E \in \mathcal{L}$ is said to have positive measure if $m(E) > 0$. The Erdős Similarity Problem is fundamentally concerned with the microscopic geometric structure and porosity of such sets.
- **Affine Copy:** For a set $A \subset \mathbb{R}$, an affine copy of $A$ is a set of the form:
  $$ x + tA = \{x + ta \mid a \in A\} $$
  where $x \in \mathbb{R}$ is a translation parameter and $t \in \mathbb{R} \setminus \{0\}$ is a scaling parameter.
- **Measure Universal Set (Sequence of Similarity):** A set $A \subset \mathbb{R}$ is called *measure universal* if for every Lebesgue measurable set $E \subset \mathbb{R}$ with $m(E) > 0$, there exists an affine copy of $A$ entirely contained within $E$. 
- **The Formal Conjecture:** The conjecture states that if $A = \{a_n\}_{n=1}^{\infty}$ is an infinite sequence with $\lim_{n \to \infty} a_n = 0$, then $A$ is not measure universal:
  $$ \forall A = \{a_n\}_{n=1}^\infty \text{ s.t. } \lim_{n \to \infty} a_n = 0, \exists E \subset \mathbb{R} \text{ with } m(E) > 0 \text{ such that } \forall x \in \mathbb{R}, \forall t \neq 0, \exists a \in A \text{ with } x + ta \notin E. $$
- **Hausdorff Dimension Context:** The Hausdorff dimension $\dim_H(E)$ characterizes the fractal complexity of a set. While $m(E) > 0$ implies $\dim_H(E) = 1$ in $\mathbb{R}$, many modern approaches study variants of the conjecture on sets where $0 < \dim_H(E) < 1$ to understand how fractal rigidity forces configurations.

## 3. History & State of the Art (SOTA)

The problem was formally posed by Paul Erdős in 1974, emerging naturally from his investigations into the geometric properties of large sets and generalizations of Steinhaus's Theorem (1920). While Steinhaus's work easily implied that every finite set is measure universal, the leap to infinite sets proved exceptionally challenging.

The first major breakthrough occurred a decade later when K. J. Falconer (1984) proved the conjecture for "slowly decaying" sequences. Utilizing the Lebesgue Density Theorem and careful metric arguments, Falconer established that sequences behaving like polynomials cannot be measure universal.

In 1997, M. N. Kolountzakis vastly expanded the class of non-universal sequences by formulating a generalized finite-gap criterion. He introduced probabilistic constructions of sets that avoid specific patterns, showing that as long as the gaps between sequence elements do not shrink too rapidly, a positive measure set can be built to avoid them.

The intersection of this problem with fractal geometry and additive combinatorics was further illuminated by researchers such as I. Łaba and M. Pramanik (2009). They studied the existence of finite arithmetic progressions in sets of fractional dimension, connecting the continuous measure-theoretic perspective to discrete structural rigidity.

Currently, the state of the art is that the conjecture is fully resolved for sequences with slow or moderate decay. However, it remains a heavily studied, wide-open problem for rapidly decaying sequences, most famously the geometric sequence $A = \{2^{-n} : n \in \mathbb{N}\}$.

## 4. Partial Results / Verified Cases

The conjecture has been definitively solved for several specific classes of sets and sequences:

- **Finite Sets (Verified Universal):** By Steinhaus's Theorem, if $m(E) > 0$, the difference set $E - E$ contains an open interval around the origin. This implies $E$ contains an affine copy of any finite set $A$. Thus, all finite sets are unconditionally measure universal.
- **Slowly Decaying Sequences (Verified Non-Universal):** Proved by Falconer (1984). If $A = \{a_n\}$ is a sequence of positive numbers strictly decreasing to 0 such that the ratio of consecutive terms approaches 1, i.e.,
  $$ \limsup_{n \to \infty} \frac{a_{n+1}}{a_n} = 1, $$
  then $A$ is not measure universal. This establishes that sequences with polynomial decay, such as $A = \{1/n : n \in \mathbb{N}\}$, are firmly excluded from being sets of similarity.
- **The Sub-Exponential Gap Criterion:** Proved by Kolountzakis (1997). Let $A = \{a_n\}$ be a decreasing sequence converging to 0. Define the minimum gap at stage $n$ as $\delta_n = \min_{1 \le i < n} (a_i - a_{i+1})$. If the sequence satisfies the condition:
  $$ -\log(\delta_n) = o(n), $$
  then $A$ is not measure universal. This criterion successfully covers a vast array of sequences that decay polynomially or sub-exponentially, such as $a_n = 1/n^2$ and $a_n = e^{-\sqrt{n}}$.
- **Fractional Dimensional Arithmetic Progressions:** Laba and Pramanik (2009) verified that if a set $E$ has Hausdorff dimension close to 1 and satisfies specific Fourier decay properties (Salem sets), it must contain affine copies of finite arithmetic progressions of arbitrary length, though this does not strictly guarantee infinite sequence embedding.

## 5. Principal Obstacles

The conjecture remains unsolved primarily due to the severe technical bottlenecks encountered when analyzing exponentially decaying sequences.

- **Exponential Decay and Scale Alignment:** The primary roadblock is sequences that decay exponentially, such as $a_n = 2^{-n}$. For these sequences, the gap parameter $-\log(\delta_n)$ grows linearly with $n$, failing the Kolountzakis criterion. An exponentially decaying sequence exhibits extreme scaling self-similarity. When attempting to build a counterexample set $E$ to avoid $a_n = 2^{-n}$, the standard technique is to use a "fat Cantor set"—a set constructed by iteratively removing open intervals from $[0, 1]$ while ensuring a positive residual measure. However, it is mathematically conceivable that there exists a scaling factor $t > 0$ such that the rapidly shrinking points of $t \cdot 2^{-n}$ perfectly align with the solid retained intervals of $E$ at every inductive scale simultaneously. Because the gaps in the sequence shrink as rapidly as the removed intervals, no mathematical contradiction is easily forced.
- **Failure of Density Point Arguments:** For finite sets or slowly decaying sequences, one can anchor the sequence at a Lebesgue density point of $E$. Because the gaps between points in $A$ don't shrink too fast, the points cannot "escape" the high-density regions of $E$. For fast-decaying sequences, an infinite number of points pile up near the limit point, and the microscopic density fluctuations of $E$ (the regions of density 0) are large enough to let points of $x+tA$ fall into the gaps, causing density arguments to break down.
- **Limitations of Fourier Analysis:** While Fourier analysis is the premier tool for finding patterns in sets (e.g., using the Fourier transform of the indicator measure $1_E$), it struggles with the exact affine conditions of the Erdős Similarity Problem. Fourier methods can easily detect the *existence* of distances or average configurations, but evaluating the highly rigid, exact infinite intersection $\bigcap_{n=1}^\infty (E - t a_n)$ requires controlling the phase cancellations of an infinite product of exponential sums, which exceeds the currently known bounds for Lebesgue measurable sets lacking rigid arithmetic structure.

## 6. The Gap

The precise mathematical boundary of the problem lies at the exponential decay threshold. 

The non-universality is rigorously proven for sequences where the minimum gap $\delta_n$ shrinks sub-exponentially ($-\log \delta_n = o(n)$). The insurmountable gap is evaluating sequences where $\delta_n \le c^n$ for some constant $c < 1$. 

To fully resolve the conjecture, the field requires a novel structural theorem regarding the microscopic "porosity" of Lebesgue measurable sets. Specifically, researchers must cross the barrier of proving that for *any* arbitrarily constructed positive measure set $E$, its microscopic gaps (the regions of density 0) are distributed in such a disorganized or pervasive manner that absolutely no choice of continuous scaling factor $t$ can perfectly synchronize the points of $\{t \cdot 2^{-n}\}$ to evade these gaps across infinite spatial scales.

## 7. Current Research (as of June 2026)

Active research continues at the intersection of harmonic analysis, fractal geometry, and additive combinatorics. 

- **Fourier Decay and Arithmetic Combinatorics:** Schools of thought led by the mathematical descendants of Łaba, Pramanik, and Kolountzakis are attempting to use advanced tools from additive combinatorics. By studying sets that satisfy specific Fourier decay conditions, researchers are trying to determine if highly structured subsets of positive measure can systematically avoid geometric progressions.
- **Non-Linear Similarity:** Researchers are actively investigating whether sets of positive measure must contain polynomial patterns, such as $x + t A^2 = \{x + t a^2 : a \in A\}$. These non-linear variants sometimes offer better Fourier analytic properties because the non-linear map introduces a "curvature" that enhances the decay of the associated exponential sums.
- **Similarity in the Large:** A recent parallel track of research investigates the "similarity problem in the large," analyzing whether sets of positive density in $\mathbb{R}$ or $\mathbb{Z}$ must contain scaled copies of infinite discrete sets growing to infinity, reversing the topological scale of the problem.
- *(frontier — verify)*: Recent preprints from leading institutes suggest that employing higher-order Fourier analysis—specifically Gowers norms adapted for continuous measure spaces—might provide the necessary analytic bounds to control the intersection of $E$ with exponentially decaying sequences, though a definitive, universally accepted proof for the $\{2^{-n}\}$ case remains elusive.

## 8. Future Work

Leading mathematicians have outlined several strategic pathways for future breakthroughs:

1. **The $2^{-n}$ Benchmark:** Achieving an explicit resolution of whether $A = \{2^{-n} : n \in \mathbb{N}\}$ is a measure universal set. Solving this specific sequence is widely considered the "holy grail" of the Erdős Similarity Problem.
2. **Unified Geometric Measure Framework:** Developing a unified theory that bridges the discrete methods of additive combinatorics (such as Szemerédi's theorem) with the continuous requirements of geometric measure theory to evaluate infinite pattern avoidance.
3. **Randomized Set Construction:** Developing new probabilistic and stochastic models for constructing sets of positive measure that possess highly controlled, adversarial microscopic geometry, effectively bypassing the predictable limitations of standard Cantor-type constructions.

## 9. Key References

- **[Foundational]** K. J. Falconer. *On a problem of Erdős on sequences and measurable sets.* Proceedings of the American Mathematical Society, 1984.
- **[SOTA / Recent]** M. N. Kolountzakis. *Infinite patterns that can be avoided by measure.* Bulletin of the London Mathematical Society, 1997.
- **[Survey]** I. Łaba, M. Pramanik. *Arithmetic progressions in sets of fractional dimension.* Geometric and Functional Analysis, 2009.

## 10. Worked Example / Concrete Special Case

To ground the abstract concept of measure universality, let us walk through the concrete proof that the finite set $A = \{0, 1\}$ is a sequence of similarity—meaning every single positive measure set contains an affine copy of it. This relies heavily on Steinhaus's Theorem.

Let $E \subset \mathbb{R}$ be any Lebesgue measurable set with positive measure, $m(E) > 0$. We want to find a translation $x \in \mathbb{R}$ and a scaling factor $t > 0$ such that $x \in E$ and $x + t(1) \in E$. This is algebraically equivalent to finding a strict distance $t > 0$ such that $t = y - x$ for some $x, y \in E$.

**Step 1: The Difference Set**
The difference set is defined mathematically as $E - E = \{x - y : x, y \in E\}$. Steinhaus's Theorem rigorously states that if $E$ is Lebesgue measurable with $m(E) > 0$, then $0$ is an interior point of $E - E$. 

**Step 2: The Lebesgue Density Theorem**
To understand why this is true, because $m(E) > 0$, almost every point in $E$ is a Lebesgue density point. Let $x_0 \in E$ be such a density point. By definition, the density of $E$ inside an infinitesimally small interval around $x_0$ approaches 1:
$$ \lim_{r \to 0} \frac{m(E \cap [x_0 - r, x_0 + r])}{2r} = 1 $$

**Step 3: Choosing a High-Density Interval**
For a sufficiently small radius $r > 0$, the set $E$ is so dense that it occupies more than $3/4$ of the interval $I = [x_0 - r, x_0 + r]$.
$$ m(E \cap I) > \frac{3}{4}(2r) = \frac{3}{2}r $$

**Step 4: The Intersection Argument**
Consider the set $E \cap I$ and its translated copy $(E \cap I) - t$ for some very small parameter $t \in (0, r/2)$. Both of these sets are entirely contained within a slightly larger boundary interval of total length $2r + t < 2.5r$.

If the two sets were completely disjoint, their combined measure would simply be the sum of their individual measures. However:
$$ m(E \cap I) + m((E \cap I) - t) = \frac{3}{2}r + \frac{3}{2}r = 3r $$
Because the combined measure $3r$ is strictly greater than the length of the container $2.5r$, the two sets mathematically cannot be disjoint. They are forced to overlap:
$$ m\left( (E \cap I) \cap ((E \cap I) - t) \right) > 0 $$

**Step 5: The Conclusion**
Because the intersection is non-empty, there exists some specific point $x$ that belongs to both $E$ and $E - t$.
$$ x \in E \quad \text{and} \quad x \in E - t \implies x + t \in E $$
Thus, both $x$ and $x + t$ are definitively in $E$. We have successfully embedded the affine copy $x + t\{0, 1\}$ entirely within $E$. 

This exact density overlap principle guarantees that all finite sets can always be embedded into positive measure sets. However, the available "overlap" margin shrinks to zero when extended to infinite sets, which is precisely why the Erdős Similarity Problem for sequences like $\{2^{-n}\}$ remains a massive open frontier.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*