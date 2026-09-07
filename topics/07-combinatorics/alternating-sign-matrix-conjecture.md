---
id: 07-combinatorics/alternating-sign-matrix-conjecture
title: "Alternating Sign Matrix Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alternating Sign Matrix Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/alternating-sign-matrix-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

An **alternating sign matrix** (ASM) of order $n$ is an $n \times n$ matrix with entries in $\{0, 1, -1\}$ such that in every row and every column the nonzero entries alternate in sign and sum to $1$. Permutation matrices are exactly the ASMs with no $-1$ entry.

**The conjecture (Mills–Robbins–Rumsey, 1983).** The number $A(n)$ of alternating sign matrices of order $n$ satisfies

$$A(n) \;=\; \prod_{j=0}^{n-1} \frac{(3j+1)!}{(n+j)!} \;=\; \frac{1!\,4!\,7!\cdots(3n-2)!}{n!\,(n+1)!\cdots(2n-1)!}.$$

A **refined** form was conjectured simultaneously: if $A(n,k)$ counts ASMs whose unique $1$ in the top row sits in column $k$, then

$$A(n,k) \;=\; \binom{n+k-2}{k-1}\,\frac{(2n-k-1)!}{(n-k)!}\,\prod_{j=0}^{n-2}\frac{(3j+1)!}{(n+j)!}.$$

A complete resolution requires a proof of the closed product formula for all $n \ge 1$ (achieved: Zeilberger 1996, Kuperberg 1996). What remains **open** is the *bijective* content originally sought: the numbers $A(n)$ also count descending plane partitions with parts $\le n$ (Andrews 1979) and totally symmetric self-complementary plane partitions in a $2n$-box (Andrews 1994), and no explicit bijection between ASMs and either family — respecting the natural statistics — was known for four decades. This page tracks both the settled enumeration and the still-live bijective and higher-symmetry problems.

## 2. Mathematical Foundations

**Monotone triangles.** ASMs of order $n$ are in bijection with monotone triangles: triangular arrays $(a_{i,j})_{1\le j\le i\le n}$ of integers with
$$a_{i,j} < a_{i,j+1}, \qquad a_{i+1,j} \le a_{i,j} \le a_{i+1,j+1},$$
bottom row $(1,2,\dots,n)$. The map takes partial column sums: row $i$ of the triangle records the positions of the $1$s in $\sum_{k\le i} M_{k,\bullet}$.

**Six-vertex model with domain wall boundary conditions.** ASMs biject with configurations of the square-ice model on an $n \times n$ grid with all horizontal external edges pointing in and all vertical ones out. The partition function is
$$Z_n(a,b,c;\,x_1,\dots,x_n;\,y_1,\dots,y_n) = \sum_{\text{configs}} \prod_{\text{vertices}} w,$$
and the **Izergin–Korepin determinant formula** (Izergin 1987; Korepin 1982) gives, for weights parametrized by $a=\sin(\lambda-\mu)$, $b=\sin(\lambda+\mu)$, $c=\sin 2\lambda$,
$$Z_n = \frac{\prod_{i,j}\sin(x_i - y_j + \eta)\sin(x_i-y_j-\eta)}{\prod_{i<j}\sin(x_i-x_j)\sin(y_j-y_i)}\;\det\!\left[\frac{\sin 2\eta}{\sin(x_i-y_j+\eta)\sin(x_i-y_j-\eta)}\right]_{i,j=1}^n.$$
Setting all spectral parameters equal and specializing to the **combinatorial point** $\Delta = \frac{a^2+b^2-c^2}{2ab} = -\tfrac12$ (i.e. $\eta = \pi/3$) makes every configuration weight $1$, so $Z_n = A(n)$, and the determinant evaluates by a Hankel/continuous-Hahn orthogonal-polynomial computation to the product above.

**The $x$-enumeration.** Weighting each ASM by $x^{\\#(-1)}$ gives $A(n;x) = \sum_M x^{N_-(M)}$. Product formulas exist only at $x \in \{1,2,3\}$:
$$A(n;2) = 2^{\binom{n}{2}}, \qquad A(n;3) = 3^{\binom{n}{2}}\prod_{j=0}^{n-1}\frac{(3j+1)!}{(n+j)!}\Big|_{\text{$q$-analogue}},$$
corresponding to $\Delta = 0$ (free-fermion) and $\Delta = 1/2$. General $x$ has no known closed form.

**Descending plane partitions (DPPs).** A DPP with parts $\le n$ is a strict-column, weak-row array with $\lambda_i$ rows offset so that the first part of each row exceeds the row length and the last part is at most the row length. Andrews proved their number is $\prod_{j=0}^{n-1}\frac{(3j+1)!}{(n+j)!}$ — the same number, by a wholly different argument.

## 3. History & State of the Art (SOTA)

- **1979.** Andrews evaluates the DPP count in the course of proving the Macdonald conjecture on cyclically symmetric plane partitions, producing the number $\prod (3j+1)!/(n+j)!$.
- **1982–83.** Mills, Robbins and Rumsey, studying Dodgson condensation (Lewis Carroll's determinant algorithm), define ASMs and observe the sequence $1, 2, 7, 42, 429, 7436, \dots$ (OEIS A005130). They state the enumeration and refined enumeration conjectures in *"Alternating sign matrices and descending plane partitions"* (JCTA, 1983).
- **1986.** Robbins and Rumsey link ASMs to the $\lambda$-determinant, showing ASMs are the natural index set for Dodgson condensation expansions.
- **1992.** Robbins conjectures product formulas for the eight symmetry classes of ASMs (vertically symmetric, half-turn symmetric, quarter-turn symmetric, etc.).
- **1996.** **Zeilberger** proves the refined conjecture in *"Proof of the alternating sign matrix conjecture"* — an 84-page argument with 88 checkers, using constant-term identities and a matching of two multivariate generating functions.
- **1996.** **Kuperberg** gives a short proof via the Izergin–Korepin determinant, importing the Yang–Baxter/quantum-integrability machinery from statistical mechanics.
- **2001–02.** Kuperberg and Okada extend the six-vertex method to most symmetry classes; Razumov and Stroganov formulate the conjecture connecting the $O(1)$ dense loop model ground state to refined ASM counts.
- **2011.** Cantini and Sportiello prove the **Razumov–Stroganov conjecture** (*"Proof of the Razumov–Stroganov conjecture"*, JCTA 2011).
- **2020–2023.** Fischer and Konvalinka construct the first **bijective proof** that $|\mathrm{ASM}_n| = |\mathrm{DPP}_n|$, via "signed sets" and sijections — a bijection between signed sets rather than sets.

Current status: the original enumeration conjecture is a **theorem**; the surrounding bijective and symmetry-class program remains partly open.

## 4. Partial Results / Verified Cases

| Statement | Status |
|---|---|
| $A(n) = \prod_{j=0}^{n-1}(3j+1)!/(n+j)!$ | Proved (Zeilberger 1996; Kuperberg 1996) |
| Refined $A(n,k)$ | Proved (Zeilberger 1996) |
| Doubly refined / triply refined enumerations | Proved (Fischer 2007; Behrend–Di Francesco–Zinn-Justin 2012) |
| Vertically symmetric ASMs $A_V(2n+1)=\prod_{j=1}^{n}\frac{(3j-1)!}{(n+j-1)!}$ | Proved (Kuperberg 2002) |
| Half-turn, quarter-turn symmetric classes | Proved (Kuperberg 2002; Razumov–Stroganov 2005) |
| Diagonally and diagonally-antidiagonally symmetric ASMs | Open in general; odd-order DASM case settled by Behrend–Fischer–Koutschan (2017) |
| $x$-enumeration | Closed form only for $x = 1, 2, 3$ |
| ASM $\leftrightarrow$ DPP bijection | Sijection (Fischer–Konvalinka 2020, 2022); no classical statistic-preserving bijection |
| ASM $\leftrightarrow$ TSSCPP bijection | **Open** |
| $q$-analogue $\sum_M q^{\mathrm{inv}(M)}$ | No product formula known |
| Numerical verification | $A(n)$ computed to $n$ in the hundreds via the product; brute-force enumeration feasible to $n \approx 11$ |

Small values: $A(1)=1$, $A(2)=2$, $A(3)=7$, $A(4)=42$, $A(5)=429$, $A(6)=7436$, $A(7)=218348$.

## 5. Principal Obstacles

- **Bijections vs. determinants.** Both proofs are *computational*: they evaluate two expressions and observe equality. The Izergin–Korepin determinant is a global object with no local combinatorial reading, so it explains the answer only after a Hankel determinant is evaluated. Nothing in either proof produces a map $\mathrm{ASM}_n \to \mathrm{DPP}_n$.
- **Statistic mismatch.** The joint distribution of $(\text{number of }{-1}\text{s},\ \text{position of top }1)$ on ASMs matches $(\text{number of special parts},\ \text{number of parts equal to }n)$ on DPPs, but the two sets carry incompatible natural partial orders (ASMs form a distributive lattice, the MacNeille completion of the Bruhat order; DPPs do not). Any bijection must therefore break the lattice structure.
- **Signed sets are not sets.** The Fischer–Konvalinka sijection cancels positive against negative elements. Extracting an honest injection requires a *canonical* cancellation, and the involutions supplied are not canonical — this is the same obstruction that keeps sign-reversing-involution proofs from being bijective.
- **Integrability breaks off the special point.** Yang–Baxter solvability holds only at isolated $\Delta$. For generic $x$-enumeration the transfer matrices do not commute, so the determinant method has nothing to say; this is why $x \ne 1,2,3$ resists.
- **Symmetry classes with no free-fermion point.** Diagonally symmetric ASMs impose a boundary condition that is not compatible with domain-wall reflection equations, so Kuperberg's technique gives no determinant at all.

## 6. The Gap

Proved: the cardinalities agree, for all $n$, with all currently known refinements. Missing: a *structural* explanation. Precisely, the open step is to construct an explicit, polynomial-time computable bijection
$$\Phi_n:\ \mathrm{ASM}_n \longrightarrow \mathrm{TSSCPP}_n$$
such that $\Phi_n$ carries the ASM statistics $(\rho, \nu, \mu)$ — inversion number, number of $-1$s, position of the top $1$ — to the corresponding TSSCPP statistics, and such that $\Phi_n$ is defined by local moves rather than by a chain of enumerations. The analogous ASM–DPP map now exists only in the weakened sijection sense. Equivalently: find a combinatorial object $\mathcal{O}_n$ and two "obvious" bijections $\mathrm{ASM}_n \to \mathcal{O}_n \to \mathrm{DPP}_n$.

## 7. Current Research (as of June 2026)

- **Fischer's school (Vienna).** Ilse Fischer and collaborators continue the operator-formula program: her "monotone triangle operator formula" gives $\alpha(n;k_1,\dots,k_n)$ as a polynomial, and recent work extends sijections to alternating sign trapezoids and to the DASM classes. *(frontier — verify)* Ongoing extensions to $(-1)$-enumerations of symmetry classes.
- **Integrable-probability groups (Paris–Saclay, MIT).** Zinn-Justin and Di Francesco relate refined ASM counts to quantum Knizhnik–Zamolodchikov equations; the qKZ solution vectors give the Razumov–Stroganov correspondence a representation-theoretic footing.
- **Cluster algebras and the $\lambda$-determinant.** ASMs index terms in the Laurent expansion of the octahedron recurrence; work by Lai, Musiker and others on double-dimer models is producing new ASM identities.
- **Higher spin / $U_q(\widehat{\mathfrak{sl}}_2)$ generalizations.** Higher-spin domain-wall partition functions produce ASM analogues whose enumeration formulas remain conjectural.
- **Computer algebra.** Koutschan's `HolonomicFunctions` and Zeilberger-style creative telescoping remain the workhorse for verifying conjectured determinant evaluations in symmetry classes.

## 8. Future Work

- Construct the ASM–TSSCPP bijection; Robbins regarded this as the real problem and the enumeration as a symptom.
- Upgrade Fischer–Konvalinka sijections to genuine bijections by finding a canonical sign-cancellation rule.
- Prove the remaining diagonally symmetric ASM enumerations (Behrend–Fischer–Koutschan conjectures).
- Find the correct statistic for a $q$-analogue: identify a Mahonian-type statistic on ASMs whose generating function factors.
- Understand the $x$-enumeration at general $x$: is there a Painlevé/isomonodromy description off the integrable points?
- Extend Razumov–Stroganov to other boundary conditions and to higher rank loop models.

## 9. Key References

- **[Foundational]** W. H. Mills, D. P. Robbins, H. Rumsey Jr. *Alternating sign matrices and descending plane partitions.* Journal of Combinatorial Theory Series A, 34 (1983), 340–359.
- **[Foundational]** G. E. Andrews. *Plane partitions III: The weak Macdonald conjecture.* Inventiones Mathematicae, 53 (1979), 193–225.
- **[Proof]** D. Zeilberger. *Proof of the alternating sign matrix conjecture.* Electronic Journal of Combinatorics, 3(2) (1996), \#R13.
- **[Proof]** G. Kuperberg. *Another proof of the alternating sign matrix conjecture.* International Mathematics Research Notices, 1996, no. 3, 139–150.
- **[SOTA]** G. Kuperberg. *Symmetry classes of alternating-sign matrices under one roof.* Annals of Mathematics, 156 (2002), 835–866.
- **[SOTA]** L. Cantini, A. Sportiello. *Proof of the Razumov–Stroganov conjecture.* Journal of Combinatorial Theory Series A, 118 (2011), 1549–1574.
- **[SOTA]** I. Fischer, M. Konvalinka. *A bijective proof of the ASM theorem, Part I: the operator formula.* Electronic Journal of Combinatorics, 27(3) (2020), \#P3.35; *Part II: ASM enumeration and ASM–DPP relation.* International Mathematics Research Notices, 2022, no. 10, 7203–7263.
- **[SOTA]** R. E. Behrend, I. Fischer, C. Koutschan. *Diagonally and antidiagonally symmetric alternating sign matrices of odd order.* Advances in Mathematics, 315 (2017), 324–365.
- **[Survey]** D. M. Bressoud. *Proofs and Confirmations: The Story of the Alternating Sign Matrix Conjecture.* Cambridge University Press / MAA, 1999.
- **[Survey]** D. P. Robbins. *The story of $1, 2, 7, 42, 429, 7436, \dots$* The Mathematical Intelligencer, 13 (1991), 12–19.

## 10. Worked Example / Concrete Special Case

**Case $n = 3$.** The formula predicts
$$A(3) = \frac{1!\cdot 4!\cdot 7!}{3!\cdot 4!\cdot 5!} = \frac{1 \cdot 24 \cdot 5040}{6 \cdot 24 \cdot 120} = \frac{120960}{17280} = 7.$$

Enumerate directly. The six $3\times3$ permutation matrices are ASMs. Exactly one further matrix has a $-1$:
$$M = \begin{pmatrix} 0 & 1 & 0 \\ 1 & -1 & 1 \\ 0 & 1 & 0\end{pmatrix}.$$
Check: row 2 reads $+,-,+$ (alternating, sum $1$); column 2 reads $+,-,+$ (sum $1$). No other placement works, since a $-1$ needs a $+1$ above, below, left and right of it, forcing it into the centre. Total $6 + 1 = 7$. ✔

**Refined check.** $A(3,k)$ for $k = 1,2,3$: matrices with top-row $1$ in column 1 are the two permutations starting $e_1$; column 3 likewise gives 2; column 2 gives the remaining $2$ permutations plus $M$, so $3$. Thus $(A(3,1),A(3,2),A(3,3)) = (2,3,2)$, summing to 7. The formula gives $A(3,1) = \binom{2}{0}\frac{4!}{2!}\cdot\frac{1!\,4!}{3!\,4!} = 12 \cdot \tfrac16 = 2$. ✔

**Monotone triangle view.** The matrix $M$ corresponds to
$$\begin{matrix} & & 2 & & \\ & 1 & & 3 & \\ 1 & & 2 & & 3\end{matrix}$$
— the only triangle of order 3 whose middle row is $(1,3)$, matching the single $-1$: a $-1$ appears exactly where a row of the triangle "spreads" past both neighbours below.

**DPP side.** Descending plane partitions with parts $\le 3$: the empty one, and $(2)$, $(3)$, $(3\,1)$, $(3\,2)$, $(3\,3)$, $(3\,3\,2)$ — seven objects. The statistic "number of parts equal to $3$" distributes as $1,1,1,2,2,2,3 \mapsto$ counts matching the ASM $\mu$-statistic $(2,3,2)$ after the standard shift. No rule is known that sends $M$ to a *specific* one of these seven — that missing rule is precisely the open problem of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*