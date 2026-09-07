---
id: 10-theoretical-cs/permanent-versus-determinant
title: "Permanent versus Determinant"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Permanent versus Determinant

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/permanent-versus-determinant` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K$ be a field of characteristic $\neq 2$ and let $\mathrm{perm}_n$ and $\det_m$ be the permanent and determinant polynomials in $n^2$ and $m^2$ variables. The **determinantal complexity** $\mathrm{dc}(\mathrm{perm}_n)$ is the least $m$ such that there is an $m \times m$ matrix $M$ whose entries are affine-linear forms in the $x_{ij}$ with

$$\mathrm{perm}_n(x) = \det{}_m\big(M(x)\big).$$

**Conjecture (Valiant, 1979).** $\mathrm{dc}(\mathrm{perm}_n)$ grows faster than any polynomial in $n$; i.e. $\mathrm{dc}(\mathrm{perm}_n) \neq n^{O(1)}$.

This is the "permanent versus determinant" problem, the flagship concrete instance of Valiant's algebraic $\mathsf{VP} \neq \mathsf{VNP}$ conjecture. A complete resolution requires either (i) a proof that $\mathrm{dc}(\mathrm{perm}_n) = n^{\omega(1)}$, or (ii) an explicit polynomial-size affine-linear determinantal representation of the permanent. Best known bounds:

$$\tfrac{n^2}{2} \;\le\; \mathrm{dc}(\mathrm{perm}_n) \;\le\; 2^n - 1 .$$

The gap between quadratic and exponential is the whole problem.

## 2. Mathematical Foundations

For $x = (x_{ij}) \in K^{n\times n}$,

$$\det{}_n(x) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma)\prod_{i=1}^n x_{i\sigma(i)}, \qquad \mathrm{perm}_n(x) = \sum_{\sigma \in S_n} \prod_{i=1}^n x_{i\sigma(i)} .$$

They differ only by the sign character, yet $\det_n$ is computable by $O(n^3)$ arithmetic operations (Gaussian elimination; Berkowitz's division-free $O(n^{3.03})$ algorithm), while computing $\mathrm{perm}_n$ over $\{0,1\}$ matrices is $\\#\mathsf{P}$-complete (Valiant 1979).

**Algebraic complexity classes.** $\mathsf{VP}$ is the class of families $(f_n)$ of polynomials with $\deg f_n = n^{O(1)}$ computed by arithmetic circuits of size $n^{O(1)}$. $\mathsf{VNP}$ consists of families with

$$f_n(x) = \sum_{e \in \{0,1\}^{p(n)}} g_n(x,e), \qquad (g_n) \in \mathsf{VP}.$$

$\mathsf{VBP}$ (algebraic branching programs) sits between; $\det_n$ is $\mathsf{VBP}$-complete under $p$-projections, and $\mathrm{dc}(f)$ is, up to $\pm 1$, the ABP size of $f$ (Toda; Malod–Portier). **Valiant's theorem:** $\mathrm{perm}_n$ is $\mathsf{VNP}$-complete under $p$-projections when $\mathrm{char}\,K \neq 2$. Hence $\mathsf{VBP} \neq \mathsf{VNP}$ iff $\mathrm{dc}(\mathrm{perm}_n)$ is superpolynomial, and $\mathsf{VP}\neq\mathsf{VNP}$ follows from a superpolynomial circuit lower bound for $\mathrm{perm}_n$. In characteristic $2$, $\mathrm{perm}_n = \det_n$ and the question is vacuous.

**Geometric formulation (GCT).** Set $N = m^2$ and consider the padded permanent $\ell^{\,m-n}\mathrm{perm}_n \in \mathrm{Sym}^m(K^N)$, where $\ell$ is a new variable. Define the orbit closures

$$\overline{\Omega}_m := \overline{GL_N \cdot \det{}_m}, \qquad Z_{n,m} := \overline{GL_N \cdot \big(\ell^{\,m-n}\mathrm{perm}_n\big)} .$$

Then $\mathrm{dc}(\mathrm{perm}_n) \le m$ implies $Z_{n,m} \subseteq \overline{\Omega}_m$; the *border* version $\overline{\mathrm{dc}}(\mathrm{perm}_n)$ is exactly the least $m$ with this containment. Mulmuley–Sohoni proposed separating the two varieties by representation-theoretic *obstructions*: irreducible $GL_N$-modules $S_\lambda(K^N)$ occurring in the coordinate ring $K[Z_{n,m}]$ but not in $K[\overline{\Omega}_m]$.

## 3. History & State of the Art (SOTA)

- **1812** — Cauchy and Binet introduce the permanent alongside the determinant.
- **1913** — Pólya asks whether signs can be attached to entries so that the determinant equals the permanent; Szegő (1913) shows this fails for $n \ge 3$, the first "no cheap reduction" theorem.
- **1979** — Valiant, *Completeness classes in algebra* (STOC) and *The complexity of computing the permanent* (TCS): $\\#\mathsf{P}$-completeness, the classes $\mathsf{VP}/\mathsf{VNP}$, and the $2^{O(n)}$ upper bound via a Ryser-type branching program.
- **1980s–90s** — von zur Gathen (1987) proves $\mathrm{dc}(\mathrm{perm}_n) \ge \sqrt{2}\,n$ using local-differential arguments; Cai (1990) improves to $\sqrt{3}\,n$; Meshulam and Babai–Seress give related linear bounds.
- **2004** — Mignon and Ressayre: $\mathrm{dc}(\mathrm{perm}_n) \ge n^2/2$ over characteristic-$0$ fields, via the rank of the Hessian of $\det$ at a point of the affine section. This is still, up to constants, the best unconditional bound.
- **2010** — Cai, Chen and Li extend $n^2/2$ to all fields with $\mathrm{char} \neq 2$.
- **2011** — Grenet: $\mathrm{dc}(\mathrm{perm}_n) \le 2^n - 1$ by a subset-lattice ABP, improving Valiant's constant.
- **2016–2019** — Bürgisser, Ikenmeyer and Panova (FOCS 2016; *J. AMS* 2019): *occurrence obstructions do not exist* for the padded-permanent formulation — a negative result that forced GCT to shift toward multiplicity obstructions.
- **2017** — Landsberg and Ressayre: if one demands the determinantal representation be *equivariant* under the symmetry group of $\mathrm{perm}_n$, then $m = 2^n-1$ is optimal; Grenet's construction is the unique minimal equivariant one.

## 4. Partial Results / Verified Cases

- **$n = 2$:** $\mathrm{dc}(\mathrm{perm}_2) = 2$, since $\mathrm{perm}_2\!\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix} = ad+bc = \det\!\begin{psmallmatrix}a&-b\\c&d\end{psmallmatrix}$.
- **$n = 3$:** $\mathrm{dc}(\mathrm{perm}_3) = 7$, matching Grenet exactly. The lower bound $\ge 7$ is due to Alper, Bogart and Velasco, *A lower bound for the determinantal complexity of a hypersurface* (Found. Comput. Math., 2017), using the singular locus of the hypersurface $\{\mathrm{perm}_3 = 0\}$.
- **$n = 4$:** $8 \le \mathrm{dc}(\mathrm{perm}_4) \le 15$; the lower bound is Mignon–Ressayre's $n^2/2$, the upper Grenet's. No exact value is known for any $n \ge 4$.
- **General $n$:** $n^2/2 \le \mathrm{dc}(\mathrm{perm}_n) \le 2^n - 1$ over $\mathrm{char} \neq 2$.
- **Restricted models where exponential bounds hold:** equivariant representations ($2^n-1$, Landsberg–Ressayre 2017); read-once oblivious ABPs; multilinear formulas of depth $O(\log n)$ (Raz); monotone circuits over $\mathbb{R}_{\ge 0}$, where $\mathrm{perm}_n$ requires $2^{\Omega(n)}$ (Jerrum–Snir 1982).
- **Border version:** $\overline{\mathrm{dc}}(\mathrm{perm}_n) \ge n^2/2$ follows from degeneration-closed arguments of Lehmkuhl–Lickteig (1989)-type; exact small-case border values ($\overline{\mathrm{dc}}(\mathrm{perm}_3) = 5$) have been reported recently *(frontier — verify)*.
- **Characteristic 2:** solved trivially, $\mathrm{dc}(\mathrm{perm}_n) = n$.

## 5. Principal Obstacles

- **Rank/Hessian methods saturate at $n^2$.** Mignon–Ressayre bound the corank of the Hessian of $\det_m$; since the Hessian is an $m^2 \times m^2$ object and $\mathrm{perm}_n$ has $n^2$ variables, any second-order local invariant is capped at $O(n^2)$. Higher derivatives do not escape: the relevant tensors of a linear section of $\det_m$ remain low-rank by construction.
- **Degree-lowering by padding.** The padding $\ell^{m-n}\mathrm{perm}_n$ makes the permanent's own symmetry group nearly invisible: as $m$ grows, the padded orbit closure becomes representation-theoretically "thin", and its highest weights are hard to distinguish from those of $\overline{\Omega}_m$. This is precisely the mechanism behind the Bürgisser–Ikenmeyer–Panova no-obstruction theorem.
- **Kronecker and plethysm coefficients are intractable.** GCT needs to decide positivity of plethysm coefficients $a_\lambda(\mathrm{Sym}^m)$ and rectangular Kronecker coefficients. Ikenmeyer–Panova showed rectangular Kronecker coefficients are almost always positive, killing the "occurrence" strategy; computing multiplicities is itself $\\#\mathsf{P}$-hard (Ikenmeyer–Mulmuley–Walter), so the obstruction certificates may be as hard as the problem.
- **Algebraic natural proofs.** Chatterjee, Kumar, Ramya, Saptharishi and Tengse (FOCS 2020) show that the equations vanishing on $\mathsf{VP}$-like classes are themselves hard to construct in natural regimes — an algebraic analogue of the Razborov–Rudich barrier.
- **No known "hard" invariant of the determinant hypersurface.** $\det_m$ is singular in codimension $4$ with a huge symmetry group $(GL_m\times GL_m)\rtimes \mathbb{Z}_2$; almost every geometric invariant one can compute for a generic linear section is dictated by that symmetry and grows too slowly in $m$.

## 6. The Gap

Everything proven is *quadratic*; the target is *superpolynomial*. Concretely, the missing step is a lower-bound technique whose value scales with the *number of variables of the ambient determinant* $m^2$ rather than with $n^2$ — that is, an invariant $\mu$ of hypersurfaces satisfying $\mu(\det_m) \le \mathrm{poly}(m)$ but $\mu(\mathrm{perm}_n) \ge n^{\omega(1)}$, and monotone under affine-linear substitution. Every currently known monotone invariant (Hessian corank, singular-locus dimension, local differential dimension, low-order partial derivative spaces) is bounded by $O(n^2)$ on the permanent side, so *none of them can ever prove more than a quadratic bound*, regardless of how sharply they are analysed. Removing the padding — proving a lower bound on unpadded $\mathrm{dc}$ that is not shared by $\overline{\mathrm{dc}}$ — is the other side of the same gap.

## 7. Current Research (as of June 2026)

- **GCT after the no-go theorem.** Groups around Bürgisser (TU Berlin), Ikenmeyer (Warwick), Panova (USC) and Landsberg (Texas A&M) work on *multiplicity obstructions* and on separating varieties other than the padded permanent (e.g. iterated matrix multiplication vs. determinant, or power sums vs. Waring-type varieties), where obstructions have actually been exhibited in small cases.
- **Border complexity and debordering.** A very active line: converting border (approximate) computation into exact computation with controlled blow-up. Dutta, Dwivedi, Gesmundo, Ikenmeyer, Jindal, Lysikov and Saxena have debordering results for width-2 ABPs, Waring rank and depth-3 circuits *(frontier — verify for the newest 2025–2026 preprints)*.
- **Symmetry-restricted models.** Extending Landsberg–Ressayre beyond full equivariance — e.g. to representations equivariant only under a large subgroup of $S_n\times S_n$ — is seen as the most plausible route to a first superquadratic bound.
- **Set-multilinear and low-depth lower bounds.** The Limaye–Srinivasan–Tavenas superpolynomial lower bound for constant-depth algebraic circuits (FOCS 2021) is the largest recent breakthrough adjacent to the problem; whether its set-multilinear machinery can be pushed to unbounded depth for $\mathrm{perm}_n$ is under active investigation.
- **Algebraic natural proofs / meta-complexity.** Kumar, Saptharishi, Tengse and collaborators study when equations for hardness are efficiently constructible.

## 8. Future Work

- Find a *third-order or higher* substitution-monotone invariant that beats the $n^2$ ceiling; Landsberg has repeatedly identified this as the decisive technical goal.
- Prove any bound of the form $\mathrm{dc}(\mathrm{perm}_n) \ge n^{2+\epsilon}$ — even $\epsilon = 0.01$ would be the first genuinely new phenomenon in two decades.
- Exhibit a single explicit *multiplicity obstruction* for a nontrivial pair $(n,m)$, validating the GCT program's revised form.
- Determine $\mathrm{dc}(\mathrm{perm}_4)$ exactly (is it $15$?), via computer algebra on the $16$-variable hypersurface's singularities.
- Settle whether $\overline{\mathrm{dc}}(\mathrm{perm}_n)$ and $\mathrm{dc}(\mathrm{perm}_n)$ are polynomially related — a positive answer legitimises all geometric approaches.
- Prove exponential lower bounds for progressively larger symmetry-restricted classes, interpolating between equivariant ($2^n-1$, known) and general (open).

## 9. Key References

- **[Foundational]** L. G. Valiant. *Completeness classes in algebra.* Proc. 11th ACM Symposium on Theory of Computing (STOC), 1979, pp. 249–261.
- **[Foundational]** L. G. Valiant. *The complexity of computing the permanent.* Theoretical Computer Science 8(2), 1979, pp. 189–201.
- **[Foundational]** T. Mignon, N. Ressayre. *A quadratic bound for the determinant and permanent problem.* International Mathematics Research Notices, 2004(79), pp. 4241–4253.
- **[SOTA]** J.-Y. Cai, X. Chen, D. Li. *Quadratic lower bound for permanent vs. determinant in any characteristic.* Computational Complexity 19(1), 2010, pp. 37–56.
- **[SOTA]** B. Grenet. *An upper bound for the permanent versus determinant problem.* Manuscript / ACM Trans. Comput. Theory submission, 2011.
- **[SOTA]** J. M. Landsberg, N. Ressayre. *Permanent v. determinant: an exponential lower bound assuming symmetry.* Proc. ACM ITCS, 2016.
- **[SOTA]** P. Bürgisser, C. Ikenmeyer, G. Panova. *No occurrence obstructions in geometric complexity theory.* Journal of the AMS 32(1), 2019, pp. 163–193.
- **[SOTA]** J. Alper, T. Bogart, M. Velasco. *A lower bound for the determinantal complexity of a hypersurface.* Foundations of Computational Mathematics 17(3), 2017, pp. 829–836.
- **[Survey]** K. D. Mulmuley, M. Sohoni. *Geometric complexity theory I: An approach to the P vs. NP and related problems.* SIAM Journal on Computing 31(2), 2001, pp. 496–526.
- **[Survey]** R. Saptharishi. *A survey of lower bounds in arithmetic circuit complexity.* Living survey, continuously updated (v9.0.3 and later).
- **[Survey]** P. Bürgisser, M. Clausen, M. A. Shokrollahi. *Algebraic Complexity Theory.* Grundlehren der mathematischen Wissenschaften 315, Springer, 1997.
- **[Related]** M. Jerrum, M. Snir. *Some exact complexity results for straight-line computations over semirings.* Journal of the ACM 29(3), 1982, pp. 874–897.
- **[Related]** N. Limaye, S. Srinivasan, S. Tavenas. *Superpolynomial lower bounds against low-depth algebraic circuits.* Proc. IEEE FOCS, 2021.

## 10. Worked Example / Concrete Special Case

**Grenet's construction for $n=3$, achieving $m = 2^3 - 1 = 7$.**

Build a directed graph whose vertices are the proper subsets of $[3]$, with $\emptyset$ and $[3]$ *merged* into a single vertex $u$. Vertices: $u$; singletons $a_1,a_2,a_3$; pairs $b_{12},b_{13},b_{23}$ — seven in total. Edges go $u \to a_i$ with label $x_{1i}$; $a_i \to b_{S}$ (where $S=\{i,j\}$) with label $x_{2j}$; and $b_S \to u$ with label $x_{3k}$, $k$ the element missing from $S$.

Let $M$ be the $7\times7$ matrix with these labels as entries, $1$ on the diagonal for the six non-$u$ vertices, and $0$ elsewhere (ordering $u,a_1,a_2,a_3,b_{12},b_{13},b_{23}$):

$$
M=\begin{pmatrix}
0 & x_{11} & x_{12} & x_{13} & 0 & 0 & 0\\
0 & 1 & 0 & 0 & x_{22} & x_{23} & 0\\
0 & 0 & 1 & 0 & x_{21} & 0 & x_{23}\\
0 & 0 & 0 & 1 & 0 & x_{21} & x_{22}\\
x_{33} & 0 & 0 & 0 & 1 & 0 & 0\\
x_{32} & 0 & 0 & 0 & 0 & 1 & 0\\
x_{31} & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}.
$$

$\det M$ sums over cycle covers. Since $M_{uu}=0$, every cycle cover contains a cycle through $u$; the graph is layered, so that cycle has length exactly $3$ ($u \to a_i \to b_S \to u$), and the remaining four vertices take self-loops of weight $1$. A permutation that is one $3$-cycle plus fixed points is even, so every surviving term has sign $+1$. Enumerating the six paths:

| path | monomial |
|---|---|
| $u\to a_1\to b_{12}\to u$ | $x_{11}x_{22}x_{33}$ |
| $u\to a_1\to b_{13}\to u$ | $x_{11}x_{23}x_{32}$ |
| $u\to a_2\to b_{12}\to u$ | $x_{12}x_{21}x_{33}$ |
| $u\to a_2\to b_{23}\to u$ | $x_{12}x_{23}x_{31}$ |
| $u\to a_3\to b_{13}\to u$ | $x_{13}x_{21}x_{32}$ |
| $u\to a_3\to b_{23}\to u$ | $x_{13}x_{22}x_{31}$ |

Hence $\det M = \mathrm{perm}_3(x)$, all six terms with coefficient $+1$ — no sign cancellation survives, which is exactly the point Pólya's question already touched. By Alper–Bogart–Velasco, $7$ is optimal here. The general construction gives $2^n-1$, and the open problem is whether the exponential subset lattice can be replaced by anything polynomial.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*