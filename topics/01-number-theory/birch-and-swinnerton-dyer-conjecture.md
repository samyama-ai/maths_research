---
id: 01-number-theory/birch-and-swinnerton-dyer-conjecture
title: "Birch and Swinnerton-Dyer Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Birch and Swinnerton-Dyer Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/birch-and-swinnerton-dyer-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Birch and Swinnerton-Dyer (BSD) Conjecture asserts a profound and exact connection between the algebraic, geometric properties of an elliptic curve and the analytic behavior of its associated L-function. 

Let $E$ be an elliptic curve defined over a number field $K$. The conjecture states two primary claims:
1. **Weak BSD Conjecture:** The algebraic rank $r$ of the group of $K$-rational points, $E(K)$, is exactly equal to the order of vanishing of the Hasse-Weil L-function $L(E, s)$ at $s = 1$. This order of vanishing is termed the *analytic rank* of $E$.
2. **Strong BSD Conjecture:** The leading non-zero Taylor coefficient of $L(E, s)$ at $s = 1$ is given by an exact formula constructed from fundamental arithmetic invariants of the curve:
   $$ \lim_{s \to 1} \frac{L(E, s)}{(s-1)^r} = \frac{\Omega \cdot \operatorname{Reg}(E) \cdot |\text{UI}(E/K)| \cdot \prod_v c_v}{|E(K)_{\text{tors}}|^2} $$
   A complete proof of the conjecture requires validating both the rank equality and the precise arithmetic formula, including the implicit assertion that the Tate-Shafarevich group $\text{UI}(E/K)$ is finite.

## 2. Mathematical Foundations

Let $E/K$ be an elliptic curve over a number field $K$, which for simplicity we can take as $\mathbb{Q}$, defined by a Weierstrass equation $y^2 = x^3 + ax + b$ with $a, b \in \mathbb{Q}$ and non-zero discriminant $\Delta$.

- **Mordell-Weil Theorem:** The group of rational points $E(\mathbb{Q})$ forms a finitely generated abelian group:
  $$ E(\mathbb{Q}) \cong E(\mathbb{Q})_{\text{tors}} \oplus \mathbb{Z}^r $$
  where $E(\mathbb{Q})_{\text{tors}}$ is the finite torsion subgroup and $r \ge 0$ is the algebraic rank.
- **Hasse-Weil L-function:** Defined for $\operatorname{Re}(s) > \frac{3}{2}$ by the Euler product over prime numbers $p$:
  $$ L(E, s) = \prod_{p \nmid \Delta} (1 - a_p p^{-s} + p^{1-2s})^{-1} \prod_{p \mid \Delta} (1 - a_p p^{-s})^{-1} $$
  where $a_p = p + 1 - \\#E(\mathbb{F}_p)$ for primes of good reduction. By the Modularity Theorem, $L(E, s)$ admits an analytic continuation to the entire complex plane.
- **Tate-Shafarevich Group $\text{UI}(E/\mathbb{Q})$:** The group of equivalence classes of principal homogeneous spaces for $E$ over $\mathbb{Q}$ that possess rational points over every local field $\mathbb{Q}_p$ and $\mathbb{R}$. It measures the failure of the Hasse principle.
- **Real Period $\Omega$:** The integration of the invariant differential $\omega = \frac{dx}{2y + \dots}$ over the real locus $E(\mathbb{R})$. If $E(\mathbb{R})$ has two components, it is twice the fundamental real period.
- **Regulator $\operatorname{Reg}(E)$:** The $r \times r$ determinant of the canonical Néron-Tate height pairing matrix $\langle P_i, P_j \rangle$ evaluated on a basis $P_1, \dots, P_r$ of the free part of $E(\mathbb{Q})$. By convention, if $r=0$, $\operatorname{Reg}(E) = 1$.
- **Tamagawa Numbers $c_p$:** Local intersection multiplicities at primes of bad reduction, defined as the index $c_p = [E(\mathbb{Q}_p) : E_0(\mathbb{Q}_p)]$, where $E_0$ constitutes points with non-singular reduction modulo $p$.

## 3. History & State of the Art (SOTA)

The conjecture was formulated in the early 1960s by Bryan Birch and Peter Swinnerton-Dyer. Using the EDSAC 2 computer at the University of Cambridge, they computed the number of points modulo $p$ ($N_p$) for curves of the form $y^2 = x^3 - dx$. They observed empirically that the asymptotic growth of the product $\prod_{p \le X} \frac{N_p}{p}$ scaled as $(\log X)^r$, directly leading to the conjectured behavior of the L-function at $s=1$.

The SOTA achieved monumental leaps between the late 1970s and 1990s:
- **1977:** John Coates and Andrew Wiles proved that if $E$ has complex multiplication (CM) and $L(E,1) \neq 0$, then $E(\mathbb{Q})$ is finite.
- **1986:** Benedict Gross and Don Zagier proved that if the analytic rank is exactly 1, there exists a specific rational point (a Heegner point) of infinite order, proving $r \ge 1$.
- **1989:** Victor Kolyvagin introduced Euler systems to show that if $L(E,1) \neq 0$ or $L'(E,1) \neq 0$, the algebraic rank precisely equals the analytic rank, and $\text{UI}(E/\mathbb{Q})$ is finite.
- **2001:** The proof of the Modularity Theorem (Wiles, Taylor, Breuil, Conrad, Diamond) ensured that $L(E,s)$ is well-defined at $s=1$ for all elliptic curves over $\mathbb{Q}$.

## 4. Partial Results / Verified Cases

- **Analytic Rank 0 and 1 over $\mathbb{Q}$:** Combined, the Gross-Zagier theorem and Kolyvagin's Euler systems completely resolve the weak BSD conjecture for all elliptic curves over $\mathbb{Q}$ with analytic rank $\le 1$. If $L(E, 1) \neq 0$, then $r = 0$ and $\text{UI}$ is finite. If $L(E, 1) = 0$ and $L'(E, 1) \neq 0$, then $r = 1$ and $\text{UI}$ is finite. 
- **Positive Proportion of Curves:** Manjul Bhargava and Arul Shankar (2015) proved that a positive proportion of all elliptic curves over $\mathbb{Q}$ (ordered by height) have algebraic rank 0, and a positive proportion have algebraic rank 1. Thus, the BSD conjecture holds for a strictly positive percentage of all elliptic curves.
- **The $p$-part of the Strong Form:** For analytic ranks 0 and 1, the exact numerical formula of the strong conjecture has been verified up to the $p$-primary components of $\text{UI}$ for specific primes $p$, using Iwasawa theory (Kato, Skinner-Urban).

## 5. Principal Obstacles

The conjecture remains profoundly resistant for elliptic curves of rank $r \ge 2$, owing to three principal technical barriers:
1. **Failure of Heegner Points:** The entire edifice of Gross-Zagier and Kolyvagin relies on constructing points from modular curves (Heegner points). However, when the analytic rank is $2$ or greater, these constructed points are provably torsion (they become zero in the free group). There is currently no known systematic geometric or analytic mechanism to construct points of infinite order for $r \ge 2$.
2. **Finiteness of $\text{UI}$:** Proving that the Tate-Shafarevich group is finite is a prerequisite for the strong BSD formula to even make sense. For $r \ge 2$, we have absolutely no unconditional proof of finiteness for any single elliptic curve.
3. **Analytic Continuation over General Fields:** For elliptic curves over general number fields (other than totally real or some CM fields), we still lack the generalized modularity theorems required to analytically continue $L(E, s)$ to $s=1$, meaning the analytic rank is not yet universally defined.

## 6. The Gap

The exact boundary of human knowledge is the jump from analytic rank $1$ to analytic rank $2$. We have a mathematically rigid bridge (Euler systems) connecting the first derivative of the L-function to the height of a singular rational point. The required mathematical step to cross the gap is the discovery of a "higher-rank Euler system" or a generalized Gross-Zagier formula—a theoretical apparatus capable of interpreting the $r$-th derivative $L^{(r)}(E, 1)$ as the determinant of a height pairing matrix (the Regulator) of $r$ linearly independent points, independent of modular parametrizations that only yield single points.

## 7. Current Research (as of June 2026)

Active research on BSD largely flows through the lens of modern arithmetic geometry:
- **Iwasawa Theory for Higher Ranks:** Researchers are heavily engaged with $p$-adic L-functions, seeking to bound Selmer groups via main conjectures.
- **Stark-Heegner Points (Darmon Points):** A major program by Henri Darmon and collaborators to construct rational points over real quadratic fields using $p$-adic uniformization, bypassing standard modular curves. *(frontier — verify the precise field of definition for higher rank constructions).*
- **Arithmetic Invariant Theory:** Expanding the Bhargava-Shankar methodologies from bounding ranks on average to extracting exact structures of Selmer groups over global fields.
- **Computational Verification:** Ongoing projects (e.g., by Noam Elkies and the LMFDB consortium) computing curves of record-breaking rank (e.g., $r \ge 28$) and checking the strong BSD formula numerically to hundreds of decimal places.

## 8. Future Work

Leading mathematicians suggest the following open pathways:
- Develop a robust theory of equivariant BSD conjectures, integrating Galois representations to factor L-functions over extensions of $\mathbb{Q}$.
- Establish the finiteness of $\text{UI}(E/K)$ algebraically, possibly via higher-dimensional Arakelov geometry or an unconditional proof of the finiteness of the $p$-primary Selmer group for $r \ge 2$.
- Fully resolve the Langlands functoriality conjectures required to guarantee the analytic continuation of L-functions for abelian varieties over arbitrary number fields.

## 9. Key References

- **[Foundational]** Birch, B. J., & Swinnerton-Dyer, H. P. F. *Notes on Elliptic Curves (I and II).* Journal für die reine und angewandte Mathematik, 1963/1965.
- **[Foundational]** Gross, B., & Zagier, D. *Heegner points and derivatives of L-series.* Inventiones mathematicae, 1986.
- **[SOTA / Recent]** Kolyvagin, V. A. *Euler systems.* The Grothendieck Festschrift, 1990.
- **[SOTA / Recent]** Bhargava, M., & Shankar, A. *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.2.4)
- **[Survey]** Wiles, A. *The Birch and Swinnerton-Dyer Conjecture.* Clay Mathematics Institute, Millennium Prize Problems, 2006.

## 10. Worked Example / Concrete Special Case

**The Congruent Number Problem**
A positive integer $n$ is a "congruent number" if it is the area of a right-angled triangle with rational side lengths. Geometrically, $n$ is a congruent number if and only if the elliptic curve $E_n: y^2 = x^3 - n^2 x$ has an infinite number of rational points (i.e., algebraic rank $r \ge 1$).

By the weak BSD conjecture, $r \ge 1 \iff L(E_n, 1) = 0$. 

In 1983, Jerrold Tunnell used this connection to provide a perfectly checkable condition. Assuming BSD, for an odd square-free integer $n$, $n$ is a congruent number if and only if:
$$ 2 \cdot \\#\{(x,y,z) \in \mathbb{Z}^3 \mid n = 2x^2 + y^2 + 8z^2\} = \\#\{(x,y,z) \in \mathbb{Z}^3 \mid n = 2x^2 + y^2 + 32z^2\} $$

**Concrete Calculation for $n = 5$:**
Consider $E_5: y^2 = x^3 - 25x$. We test if $5$ is congruent by plugging $n=5$ into Tunnell's equations.
- $2x^2 + y^2 + 8z^2 = 5$ has no integer solutions (the counts are $0$).
- $2x^2 + y^2 + 32z^2 = 5$ has no integer solutions (the counts are $0$).
Since $2(0) = 0$, Tunnell's condition holds. Thus, $L(E_5, 1) = 0$, which by BSD implies $r \ge 1$. Indeed, $E_5$ has algebraic rank 1, generated by the rational point $(-4, -6)$. This maps to a right triangle with rational sides $3/2$, $20/3$, and $41/6$, which has exactly area $5$.

**Concrete Calculation for $n = 1$:**
Consider $E_1: y^2 = x^3 - x$. 
- $2x^2 + y^2 + 8z^2 = 1$ has two solutions: $(x,y,z) \in \{(0,1,0), (0,-1,0)\}$.
- $2x^2 + y^2 + 32z^2 = 1$ has two solutions: $(x,y,z) \in \{(0,1,0), (0,-1,0)\}$.
Since $2(2) \neq 2$, Tunnell's condition fails. Thus, $L(E_1, 1) \neq 0$, implying $r = 0$. The curve $E_1$ has only finitely many rational points (all torsion), meaning $1$ is not a congruent number.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*