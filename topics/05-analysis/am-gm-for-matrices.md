---
id: 05-analysis/am-gm-for-matrices
title: "AM-GM for Matrices"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# AM-GM for Matrices

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/am-gm-for-matrices` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The scalar arithmetic–geometric mean inequality $\sqrt{ab}\le\frac{a+b}{2}$ ($a,b\ge 0$) has several inequivalent matrix analogues. Two remain open.

**(A) Bhatia–Kittaneh conjecture (2008).** For positive semidefinite $A,B\in\mathbb{M}_n(\mathbb{C})$ and *every* unitarily invariant norm $\vertiii{\cdot}$,
$$4\,\vertiii{AB}\;\le\;\vertiii{(A+B)^2}.$$
A complete proof must cover all unitarily invariant norms simultaneously (equivalently, prove the weak majorization $4\,s(AB)\prec_w s((A+B)^2)$ of singular value vectors). A disproof requires an explicit pair $(A,B)$ and a norm violating it.

**(B) Recht–Ré noncommutative AM–GM conjecture (2012).** For PSD $A_1,\dots,A_n$, is sampling *without* replacement dominated by sampling *with* replacement:
$$\Big\|\frac{1}{n!}\sum_{\sigma\in S_n}A_{\sigma(1)}\cdots A_{\sigma(n)}\Big\|\;\le\;\Big\|\frac{1}{n^n}\sum_{i_1,\dots,i_n=1}^{n}A_{i_1}\cdots A_{i_n}\Big\|\;?$$
This is now known to be **false** in general; the surviving questions are the small-$n$ cases and what constant-factor substitute is true.

Status is `partially-solved`: (A) is proved for the operator norm and several structured classes but open for general unitarily invariant norms; (B) is settled negatively for large $n$ with $n=4$ open.

## 2. Mathematical Foundations

Let $\mathbb{P}_n$ denote the cone of positive semidefinite $n\times n$ complex matrices, $\mathbb{P}_n^{+}$ the positive definite ones. For $X\in\mathbb{M}_n$, $s_1(X)\ge\cdots\ge s_n(X)$ are the singular values and $\lambda_j$ the eigenvalues ordered by decreasing modulus.

**Unitarily invariant norms.** $\vertiii{UXV}=\vertiii{X}$ for all unitary $U,V$. By von Neumann's theorem, each such norm is a symmetric gauge function of $s(X)$. The key comparison principle: if $s(X)\prec_w s(Y)$ (weak majorization, $\sum_{j\le k}s_j(X)\le\sum_{j\le k}s_j(Y)$ for all $k$) then $\vertiii{X}\le\vertiii{Y}$ for every unitarily invariant norm. Extremes are the operator norm $\|X\|=s_1$ and the trace norm $\|X\|_1=\sum_j s_j$.

**Loewner order and the geometric mean.** $A\preceq B$ means $B-A\in\mathbb{P}_n$. For $A\in\mathbb{P}_n^{+},B\in\mathbb{P}_n$ the Kubo–Ando geometric mean is
$$A \\# B \;=\; A^{1/2}\big(A^{-1/2}BA^{-1/2}\big)^{1/2}A^{1/2},$$
the unique PSD solution of $XA^{-1}X=B$. It satisfies the *operator* AM–GM inequality
$$A \\# B \;\preceq\; \frac{A+B}{2},$$
with equality iff $A=B$ — a theorem, not a conjecture, following from $\left(\frac{A+B}{2}\right) - A\\#B = \frac12 A^{1/2}\big(I-(A^{-1/2}BA^{-1/2})^{1/2}\big)^2A^{1/2}\succeq 0$.

**Why (A) is not elementary.** The product $AB$ of two PSD matrices is generally non-Hermitian, so no Loewner-order statement about $AB$ is available. The symmetrized version *is* elementary:
$$(A+B)^2-2(AB+BA)=A^2-AB-BA+B^2=(A-B)^2\succeq 0
\quad\Longrightarrow\quad \frac{AB+BA}{2}\preceq\frac{(A+B)^2}{4}.$$
Conjecture (A) asks for the same $\tfrac14$ constant for the *unsymmetrized* product at the level of singular values.

**The proved singular-value AM–GM.** Bhatia–Kittaneh (1990): for arbitrary $X,Y\in\mathbb{M}_n$,
$$2\,s_j(XY)\;\le\;s_j(X^*X+YY^*),\qquad j=1,\dots,n.$$
Putting $X=A^{1/2}$, $Y=B^{1/2}$ gives $2\,s_j(A^{1/2}B^{1/2})\le\lambda_j(A+B)$, hence $2\vertiii{A^{1/2}B^{1/2}}\le\vertiii{A+B}$ for every unitarily invariant norm. Conjecture (A) is the "full-power" version obtained by formally replacing $A^{1/2}B^{1/2}$ by $AB$ and $A+B$ by $(A+B)^2$; this replacement is *not* justified by any known operator-monotonicity argument.

## 3. History & State of the Art (SOTA)

- **1980.** Kubo and Ando classify operator means via operator monotone functions, placing $A\\#B$ and $\frac{A+B}{2}$ in a single axiomatic framework; the Loewner-order AM–GM inequality becomes standard.
- **1990.** Bhatia and Kittaneh prove the singular-value inequality $2s_j(XY)\le s_j(X^*X+YY^*)$ (SIAM J. Matrix Anal. Appl.), the first genuinely matricial AM–GM at the level of all unitarily invariant norms.
- **1994–2002.** Ando–Hiai log-majorization and Zhan's *Matrix Inequalities* consolidate the majorization toolkit and list AM–GM-type questions as open problems.
- **2004–2012.** Multivariable geometric means: Ando–Li–Mathias axioms, the Riemannian (Karcher) mean of Bhatia–Holbrook, and the monotonicity theorems of Lawson–Lim and Bhatia–Karandikar. Here the $n$-variable AM–GM $G(A_1,\dots,A_n)\preceq\frac1n\sum_j A_j$ is a theorem.
- **2008.** Bhatia and Kittaneh revisit the problem and pose conjecture (A), proving the operator-norm case.
- **2012.** Recht and Ré, motivated by convergence of without-replacement SGD, pose (B) in COLT.
- **2016.** Israel, Krahmer and Ward prove the three-matrix case of (B).
- **2020.** Lai and Lim construct explicit counterexamples disproving (B) for products of length $n\ge 5$ (ICML), redirecting the field toward constant-factor and typical-case versions.

## 4. Partial Results / Verified Cases

**Conjecture (A) is proved for:**

- **The operator norm** ($j=1$ case): $4\|AB\|\le\|(A+B)^2\|$, Bhatia–Kittaneh (2008).
- **Rank-one products.** If $\operatorname{rank}(AB)\le 1$ the inequality for every unitarily invariant norm reduces to the operator-norm case, since $\vertiii{X}=s_1(X)\vertiii{E_{11}}$ for rank-one $X$ and $\vertiii{(A+B)^2}\ge s_1((A+B)^2)\vertiii{E_{11}}$. In particular it holds whenever $A$ or $B$ has rank $1$.
- **Commuting $A,B$.** Simultaneous diagonalization reduces the statement to $4a_jb_j\le(a_j+b_j)^2$ entrywise, which after reordering gives the majorization and hence all unitarily invariant norms.
- **Normal products.** If $AB$ is normal, $s_j(AB)=\lambda_j(A^{1/2}BA^{1/2})$ and the log-majorization machinery of Ando–Hiai applies.
- **Equality analysis.** $A=B$ gives $4\vertiii{A^2}=\vertiii{(2A)^2}$: the constant $4$ is sharp and cannot be improved for any norm.
- **The half-power form.** $2\vertiii{A^{1/2}B^{1/2}}\le\vertiii{A+B}$ holds unconditionally in all dimensions (Bhatia–Kittaneh 1990).
- **Low dimension.** $n=2$ is tractable by direct computation with the two invariants $\operatorname{tr}$ and $\det$; no counterexample has been produced in extensive numerical searches over $n\le 10$.
- Drury, *On a question of Bhatia and Kittaneh* (LAA 437, 2012), analyses the eigenvalue formulation $\lambda_j(AB)\le\frac14\lambda_j((A+B)^2)$ directly; consult it for the precise state of that variant *(verify)*.

**Conjecture (B):** true for $n=2$ (immediate from $\|AB+BA\|\le\frac12\|(A+B)^2\|$-type bounds) and for $n=3$ (Israel–Krahmer–Ward 2016, operator norm, PSD matrices of any size); **false** for $n\ge 5$ with explicit small PSD counterexamples (Lai–Lim 2020). $n=4$ remains open.

## 5. Principal Obstacles

- **Non-Hermitian products.** $AB$ is not PSD and not normal, so Loewner-order arguments, operator monotonicity of $t\mapsto t^{1/2}$, and variational characterizations of eigenvalues (Courant–Fischer) do not apply to $AB$ itself. One must work with $s_j(AB)=\lambda_j^{1/2}(BA^2B)$, which destroys the symmetry between $A$ and $B$.
- **Majorization does not tensorize with powers.** From $2s_j(A^{1/2}B^{1/2})\le\lambda_j(A+B)$ one would like to square. But $s(X)\prec_w s(Y)$ does *not* imply $s(X^2)\prec_w s(Y^2)$ for non-normal $X$; only log-majorization ($\prec_{\log}$) is stable under powers, and the half-power inequality is not known in log-majorized form with the required constant.
- **Ky Fan reduction is not available.** Weak majorization needs the inequality for every partial sum $\sum_{j\le k}s_j$. The known proof of the $k=1$ (operator norm) case uses a two-dimensional compression / $2\times2$ block argument that has no known $k$-dimensional analogue: compressing to a $k$-dimensional subspace does not commute with taking the product $AB$.
- **No convexity/interpolation route.** Complex interpolation (Stein–Hirschman) gives Schatten-$p$ inequalities with $p$-dependent constants; the conjecture requires the *same* constant $4$ across the whole scale, ruling out interpolation-with-loss arguments.
- **Free-probability heuristics fail at the extremes.** Asymptotic freeness predicts the inequality holds with room to spare for generic large random PSD pairs, so random search does not locate the extremal configurations, which (if they exist) must be highly degenerate.
- **For (B), the failure mechanism is combinatorial.** Lai–Lim's counterexamples show that the permutation sum can develop cancellation patterns absent from the with-replacement sum; no norm-monotonicity principle separates the two sums, so the conjecture's plausibility rested on small-$n$ evidence only.

## 6. The Gap

Everything proved for (A) lives at $k=1$: the operator-norm/top-singular-value level, plus classes (commuting, rank-one, normal product) where the top-level statement propagates. The general statement is the family of $n$ inequalities
$$4\sum_{j=1}^{k}s_j(AB)\;\le\;\sum_{j=1}^{k}s_j\big((A+B)^2\big),\qquad k=1,\dots,n.$$
The precise missing step is a $k$-dimensional compression lemma: a subspace $\mathcal{M}$ of dimension $k$ realizing $\sum_{j\le k}s_j(AB)$ on which the pair $(A,B)$ can be replaced by compressions $(P_\mathcal{M}AP_\mathcal{M}, P_\mathcal{M}BP_\mathcal{M})$ without increasing the ratio. No such lemma is known, because the compression of a product is not the product of compressions. Equivalently, one needs to upgrade $2s_j(A^{1/2}B^{1/2})\le\lambda_j(A+B)$ from weak majorization to a form stable under squaring.

## 7. Current Research (as of June 2026)

- **Log-majorization route.** Attempts to prove $4\,s(AB)\prec_{\log}s((A+B)^2)$ using Ando–Hiai type complementary Golden–Thompson inequalities; log-majorization implies weak majorization for the required ordering and is closed under powers. Groups working in matrix analysis at ISI Delhi (Bhatia school), Kuwait University (Kittaneh school) and Sungkyunkwan / Chungbuk (Lim, Lawson, Pálfia) are the natural centres.
- **Computer-assisted search.** SDP/SOS relaxations of the $k=2$ case in dimensions $n\le 6$, parameterized by the joint invariants of $(A,B)$, aiming either at a certificate or a violating pair *(frontier — verify)*.
- **Post-Recht–Ré programme.** After Lai–Lim, effort has shifted to constant-factor noncommutative AM–GM bounds — inequalities of the form $\|\text{avg over }S_n\|\le C(n)\|\text{avg with replacement}\|$ with $C(n)$ polynomially bounded — driven by the analysis of random-reshuffling SGD in optimization theory.
- **Operator-algebra generalizations.** Formulations for $\tau$-measurable operators in semifinite von Neumann algebras, where singular values are replaced by generalized $s$-numbers; the operator-norm case transfers, the majorization case does not.

## 8. Future Work

1. Prove or refute the $k=2$ Ky Fan case of (A) — the smallest genuinely new instance; a proof would likely supply the missing compression technique, a counterexample would settle the conjecture.
2. Determine whether $s(AB)\prec_{\log}\frac14 s((A+B)^2)$; this stronger statement may in fact be easier because log-majorization interacts well with the map $X\mapsto X^2$.
3. Settle $n=4$ for the Recht–Ré conjecture, closing the gap between Israel–Krahmer–Ward ($n=3$, true) and Lai–Lim ($n\ge5$, false).
4. Identify the sharp constant $C_n$ in $\vertiii{\frac1{n!}\sum_\sigma A_{\sigma(1)}\cdots A_{\sigma(n)}}\le C_n\vertiii{\frac1{n^n}\sum A_{i_1}\cdots A_{i_n}}$ and decide whether $\sup_n C_n<\infty$.
5. Extend verified classes: pairs $(A,B)$ with $\operatorname{rank}(AB)\le 2$, or with $A$ a projection, where the top-level argument may still propagate.

## 9. Key References

- **[Foundational]** R. Bhatia and F. Kittaneh. *On the singular values of a product of operators.* SIAM Journal on Matrix Analysis and Applications, 11(2):272–277, 1990. [DOI](https://doi.org/10.1137/0611018)
- **[Foundational]** F. Kubo and T. Ando. *Means of positive linear operators.* Mathematische Annalen, 246:205–224, 1980. [DOI](https://doi.org/10.1007/bf01371042)
- **[Foundational]** R. Bhatia. *Matrix Analysis.* Graduate Texts in Mathematics 169, Springer, 1997.
- **[SOTA]** R. Bhatia and F. Kittaneh. *The matrix arithmetic–geometric mean inequality revisited.* Linear Algebra and its Applications, 428(8–9):2177–2189, 2008. [DOI](https://doi.org/10.1016/j.laa.2007.11.030)
- **[SOTA]** S. W. Drury. *On a question of Bhatia and Kittaneh.* Linear Algebra and its Applications, 437(8):1955–1960, 2012.
- **[SOTA / Recent]** B. Recht and C. Ré. *Beneath the valley of the noncommutative arithmetic-geometric mean inequality: conjectures, case-studies, and consequences.* Proceedings of COLT 2012, JMLR Workshop and Conference Proceedings 23.
- **[SOTA / Recent]** A. Israel, F. Krahmer and R. Ward. *An arithmetic–geometric mean inequality for products of three matrices.* Linear Algebra and its Applications, 488:1–12, 2016. [DOI](https://doi.org/10.1016/j.laa.2015.09.013)
- **[SOTA / Recent]** Z. Lai and L.-H. Lim. *Recht–Ré noncommutative arithmetic-geometric mean conjecture is false.* Proceedings of ICML 2020, PMLR 119.
- **[Survey]** X. Zhan. *Matrix Inequalities.* Lecture Notes in Mathematics 1790, Springer, 2002.
- **[Survey]** R. Bhatia. *Positive Definite Matrices.* Princeton University Press, 2007.
- **[Related]** T. Ando and F. Hiai. *Log majorization and complementary Golden–Thompson type inequalities.* Linear Algebra and its Applications, 197/198:113–131, 1994. [DOI](https://doi.org/10.1016/0024-3795(94)90484-7)
- **[Related]** J. Lawson and Y. Lim. *Monotonic properties of the least squares mean.* Mathematische Annalen, 351:267–279, 2011. [DOI](https://doi.org/10.1007/s00208-010-0603-6)

## 10. Worked Example / Concrete Special Case

Take the singular PSD pair
$$A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

**Left side.** $AB=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, so $(AB)(AB)^*=\begin{pmatrix}2&0\\0&0\end{pmatrix}$ and $s(AB)=(\sqrt2,0)$. Hence
$$4\|AB\|=4\|AB\|_1=4\|AB\|_F=4\sqrt2\approx 5.6569 .$$

**Right side.** $A+B=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, $\det(A+B)=1$, and
$$(A+B)^2=\begin{pmatrix}5&3\\3&2\end{pmatrix},\qquad \operatorname{tr}=7,\ \det=1 .$$
Its eigenvalues are $\frac{7\pm\sqrt{45}}{2}$, i.e. $6.8541$ and $0.1459$.

**Comparison.**

| norm | $4\vertiii{AB}$ | $\vertiii{(A+B)^2}$ | ratio |
|---|---|---|---|
| operator | $5.6569$ | $6.8541$ | $0.825$ |
| Frobenius | $5.6569$ | $6.8557$ | $0.825$ |
| trace | $5.6569$ | $7.0000$ | $0.808$ |

The conjecture holds here with about $18\%$ slack. Note this instance is covered by the proved rank-one case ($\operatorname{rank}(AB)=1$), which is exactly why all three norms give the same left side.

**Sharpness.** With $A=B$ we get $4\vertiii{A^2}=\vertiii{4A^2}=\vertiii{(A+B)^2}$: equality in every unitarily invariant norm, so the constant $4$ cannot be lowered.

**Where the elementary argument stops.** The symmetrized inequality is exact and trivial here:
$$(A+B)^2-2(AB+BA)=(A-B)^2=\begin{pmatrix}0&-1\\-1&-1\end{pmatrix}^2=\begin{pmatrix}1&1\\1&2\end{pmatrix}\succeq 0 .$$
This proves $\frac{AB+BA}{2}\preceq\frac{(A+B)^2}{4}$ in the Loewner order for all PSD $A,B$. But $AB=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is not Hermitian and $\|AB\|=\sqrt2 > \|\frac{AB+BA}{2}\|$ is possible in general, so this identity does **not** yield the singular-value statement of Section 1. That single step — from the symmetrized product to the raw product, uniformly over all Ky Fan norms — is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*