---
id: 01-number-theory/mahlers-3-2-problem
title: "Mahler's 3/2 Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mahler's 3/2 Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/mahlers-3-2-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Mahler's 3/2 Problem is a long-standing open question in number theory concerning the distribution of the fractional parts of a geometric progression. 

The problem asks: **Does there exist a positive real number $x$ such that the fractional part of $x(3/2)^n$ is strictly less than $1/2$ for all non-negative integers $n$?**

If such a number exists, it is called a **Z-number**. Mahler explicitly conjectured that no Z-numbers exist. A complete proof requires mathematically demonstrating that the set of all Z-numbers is empty. Conversely, a disproof requires the explicit construction or proof of existence of at least one such real number.

## 2. Mathematical Foundations

Let $\mathbb{R}_{>0}$ denote the set of positive real numbers and $\mathbb{Z}_{\ge 0}$ denote the set of non-negative integers. For any real number $y$, define its fractional part as:
$$ \{y\} = y - \lfloor y \rfloor $$
where $\lfloor y \rfloor$ is the greatest integer less than or equal to $y$. 

A real number $x \in \mathbb{R}_{>0}$ is defined as a **Z-number** if it satisfies the infinite system of inequalities:
$$ 0 \le \left\{ x \left(\frac{3}{2}\right)^n \right\} < \frac{1}{2} \quad \text{for all } n \in \mathbb{Z}_{\ge 0}. $$

This problem can also be framed within the context of dynamical systems. Consider the transformation $T: \mathbb{R}/\mathbb{Z} \to \mathbb{R}/\mathbb{Z}$ given by multiplication by $3/2$ modulo 1:
$$ T(\theta) = \frac{3}{2}\theta \pmod 1. $$
Mahler's conjecture asserts that there is no initial condition $x$ on the real line whose forward trajectory under this expanding map (accounting for the carry-over from the integer part) permanently avoids the interval $[1/2, 1)$.

## 3. History & State of the Art (SOTA)

The problem was formalized by the German-Australian mathematician Kurt Mahler in 1968 in his paper *"An unsolved problem on the fractional parts of the powers of a rational number"*. Mahler was investigating the broader Diophantine question of how the fractional parts of $\xi (p/q)^n$ distribute in the unit interval $[0, 1)$, a topic deeply connected to Waring's problem.

Mahler proved that the set of Z-numbers (if it is not empty) must be at most countably infinite. Despite over half a century of study, the core conjecture remains completely open. 

The most significant structural milestone was achieved by Flatto, Lagarias, and Pollington in 1995. They analyzed the general sequence $\xi(p/q)^n$ and proved a hard lower bound on the size of any interval that can contain the entire sequence of fractional parts. For $p/q = 3/2$, their theorem implies that the sequence cannot be confined to any interval strictly smaller than $1/3$ in length. 

## 4. Partial Results / Verified Cases

While the general conjecture is unsolved, several partial and quantitative results have been verified:

1.  **Cardinality and Density:** Mahler proved that there is at most one Z-number in any unit interval. Furthermore, he established a quantitative upper bound showing that for a sufficiently large $X$, the number of Z-numbers less than or equal to $X$ is $O(X^{\alpha})$ for an exponent $\alpha \approx 0.7$, proving that Z-numbers are incredibly sparse if they exist at all.
2.  **The $1/3$ Bound Limit:** By the Flatto-Lagarias-Pollington theorem, we know that if we replace Mahler's $1/2$ bound with $1/3$, the corresponding set is strictly empty. That is, there is no real number $x$ such that $\{x(3/2)^n\} \in [0, c]$ for any $c < 1/3$.
3.  **Computational Verification:** Algorithmic searches have exhaustively ruled out the existence of integer Z-numbers up to massive computational limits, and no rational Z-numbers with small denominators have been found. 

## 5. Principal Obstacles

The problem remains intractable because standard techniques from different mathematical branches fail to apply simultaneously:

-   **Measure Theory & Ergodic Theory:** The map $x \mapsto \frac{3}{2}x \pmod 1$ is chaotic, and basic ergodic theory easily proves that the Lebesgue measure of the set of Z-numbers is exactly zero. However, measure theory provides no tools to distinguish between a set of measure zero and the strictly empty set.
-   **Diophantine Approximation:** Powerful tools like Roth's theorem, the Subspace theorem, or Baker's method of linear forms in logarithms require the starting number $x$ to be algebraic. Since we do not know the arithmetic nature of a hypothetical Z-number (it could very well be transcendental), these algebraic techniques cannot be universally applied.
-   **Symbolic Dynamics:** While multiplication by an integer (e.g., base-2 or base-3 maps) yields clean Markov partitions and simple shift spaces, multiplication by the non-integer rational $3/2$ introduces overlapping cylinder sets and infinitely complex symbolic grammars (often studied as $\beta$-expansions for $\beta = 1.5$). This destroys the combinatorial regularity needed to rule out specific infinite sequences.

## 6. The Gap

The exact mathematical barrier lies in the numerical gap between **$1/3$** and **$1/2$**.

The Flatto-Lagarias-Pollington state-of-the-art result strictly prohibits the sequence of fractional parts from being confined to an interval of length strictly less than $1/3$. However, Mahler's problem asks to rule out the confinement within the interval $[0, 1/2)$, which has a length of $1/2$. 

Because $1/3 < 1/2$, the proven constraints are currently too weak to force the sequence out of the $[0, 1/2)$ interval. To resolve the conjecture, one must bridge this $1/6$ gap by finding a new structural property of the interplay between the primes 2 and 3 that raises the theoretical lower bound of the range from $1/3$ to at least $1/2$.

## 7. Current Research (as of June 2026)

Active research on Mahler's 3/2 problem operates at the intersection of Diophantine approximation, fractal geometry, and theoretical computer science. Current directions include:

-   **Finite Automata and De Bruijn Graphs:** Researchers are mapping the valid state transitions of the fractional parts into directed graphs to computationally prove that all paths must eventually hit the $[1/2, 1)$ interval.
-   **Connections to the Collatz Conjecture:** Because both problems fundamentally rely on the interaction between multiplication by 3 and division by 2, heuristic models from the $3x+1$ problem are being ported to study the pseudo-random distribution of $x(3/2)^n$.
-   *(frontier — verify)* **Rational Base Number Systems:** Recent preprints are exploring whether techniques used to study the digit distribution in non-integer bases can rigorously rule out Z-numbers in specific transcendental extensions.

## 8. Future Work

Leading mathematicians suggest several pathways to attack the conjecture:

-   **Improving the Range Bound:** The most direct, albeit highly difficult, approach is to refine the Flatto-Lagarias-Pollington theorem specifically for $p=3, q=2$, attempting to push the minimal interval length bound from $1/3$ to $1/2$.
-   **$p$-adic Ergodic Theory:** Investigating the joint distribution of the powers of 3 and 2 using $p$-adic analysis to establish a rigidity theorem that prevents the fractional parts from being artificially bounded.
-   **Algebraic Independence:** Establishing a conditional proof: e.g., proving that *if* a Z-number exists, it must be transcendental, which would at least rule out the existence of algebraic Z-numbers.

## 9. Key References

-   **[Foundational]** K. Mahler. *An unsolved problem on the fractional parts of the powers of a rational number.* Journal of the Australian Mathematical Society, 1968.
-   **[SOTA / Recent]** L. Flatto, J. C. Lagarias, and A. D. Pollington. *On the range of fractional parts of $\xi(p/q)^n$.* Acta Arithmetica, 1995.
-   **[Survey]** Y. Bugeaud. *Distribution modulo one and Diophantine approximation.* Cambridge Tracts in Mathematics, 2012.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, let us test whether the rational number $x = 4/3$ is a Z-number. We must check if $\{x(3/2)^n\} < 1/2$ holds for all $n \ge 0$.

-   **Step $n = 0$:**
    $$ x \left(\frac{3}{2}\right)^0 = \frac{4}{3} \approx 1.333 $$
    The fractional part is $\left\{\frac{4}{3}\right\} = \frac{1}{3}$. Since $1/3 < 1/2$, the condition holds.

-   **Step $n = 1$:**
    $$ \frac{4}{3} \left(\frac{3}{2}\right)^1 = 2 $$
    The fractional part is $\{2\} = 0$. Since $0 < 1/2$, the condition holds.

-   **Step $n = 2$:**
    $$ 2 \left(\frac{3}{2}\right)^1 = 3 $$
    The fractional part is $\{3\} = 0$. Since $0 < 1/2$, the condition holds.

-   **Step $n = 3$:**
    $$ 3 \left(\frac{3}{2}\right)^1 = \frac{9}{2} = 4.5 $$
    The fractional part is $\{4.5\} = 1/2$. 

At $n=3$, the condition strictly fails because the fractional part is exactly $1/2$, which is not strictly less than $1/2$. Therefore, $x = 4/3$ is **not** a Z-number. Mahler's conjecture posits that a failure of this kind will inevitably happen for *any* starting number $x > 0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*