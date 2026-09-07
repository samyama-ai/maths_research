---
id: 02-algebra-group-theory/macdonald-positivity-conjecture
title: "Macdonald Positivity Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Macdonald Positivity Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/macdonald-positivity-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Macdonald (1988) introduced a two-parameter family of symmetric functions $P_\lambda(x;q,t)$ interpolating between Schur, Hall–Littlewood, Jack and zonal polynomials. Expanding their integral form $J_\mu(x;q,t)$ in a plethystically twisted Schur basis defines the **$q,t$-Kostka coefficients** $K_{\lambda\mu}(q,t)$:

$$J_\mu(x;q,t) \;=\; \sum_{\lambda \vdash n} K_{\lambda\mu}(q,t)\, s_\lambda\!\left[X(1-t)\right].$$

**Conjecture (Macdonald, 1988).** For all partitions $\lambda,\mu \vdash n$,
$$K_{\lambda\mu}(q,t) \in \mathbb{N}[q,t],$$
i.e. every coefficient is a non-negative integer.

Macdonald only knew $K_{\lambda\mu}(q,t)\in\mathbb{Q}(q,t)$ from the definition; even polynomiality was unclear. A complete resolution requires (a) proving non-negativity, and ideally (b) exhibiting a *representation-theoretic* or *combinatorial* reason — a bigraded module whose Frobenius character is $\tilde H_\mu$, or statistics $\mathrm{stat}_q,\mathrm{stat}_t$ on standard Young tableaux with $\tilde K_{\lambda\mu}(q,t)=\sum_{T\in \mathrm{SYT}(\lambda)} q^{\mathrm{stat}_q(T)}t^{\mathrm{stat}_t(T)}$.

**Status.** Part (a) was proved by Mark Haiman (2001). Part (b) — a manifestly positive combinatorial rule — remains open in general, as does positivity for Macdonald polynomials attached to root systems other than type $A$.

## 2. Mathematical Foundations

Let $\Lambda_{\mathbb{Q}(q,t)}$ be symmetric functions in $x=(x_1,x_2,\dots)$. Macdonald's $P_\lambda(x;q,t)$ are the unique basis that is (i) unitriangular against monomial symmetric functions in dominance order, $P_\lambda = m_\lambda + \sum_{\nu<\lambda} c_{\lambda\nu} m_\nu$, and (ii) orthogonal for the inner product
$$\langle p_\lambda, p_\mu\rangle_{q,t} \;=\; \delta_{\lambda\mu}\, z_\lambda \prod_{i\ge 1}\frac{1-q^{\lambda_i}}{1-t^{\lambda_i}}.$$

For a cell $s\in\mu$ write $a(s)$ (arm) and $l(s)$ (leg). The integral form is $J_\mu = \prod_{s\in\mu}\bigl(1-q^{a(s)}t^{l(s)+1}\bigr)\,P_\mu$. The **modified Macdonald polynomial** is
$$\tilde H_\mu(x;q,t) \;=\; t^{n(\mu)} J_\mu\!\left[\tfrac{X}{1-t^{-1}};q,t^{-1}\right], \qquad n(\mu)=\sum_i (i-1)\mu_i,$$
so that $\tilde H_\mu = \sum_\lambda \tilde K_{\lambda\mu}(q,t)\, s_\lambda$ with $\tilde K_{\lambda\mu}(q,t) = t^{n(\mu)}K_{\lambda\mu}(q,t^{-1})$. Macdonald positivity is equivalent to $\tilde K_{\lambda\mu}(q,t)\in\mathbb{N}[q,t]$.

**Garsia–Haiman module.** Order the cells of $\mu\vdash n$ as $(p_1,q_1),\dots,(p_n,q_n)$ and set
$$\Delta_\mu(x,y) \;=\; \det\bigl(x_i^{p_j} y_i^{q_j}\bigr)_{i,j=1}^n,$$
$$R_\mu \;=\; \mathbb{C}\bigl[\partial_{x},\partial_{y}\bigr]\,\Delta_\mu \;\subseteq\; \mathbb{C}[x_1,\dots,x_n,y_1,\dots,y_n].$$
$R_\mu$ is bigraded and carries the diagonal $S_n$-action.

**$n!$ Conjecture (Garsia–Haiman 1993).** $\dim_{\mathbb{C}} R_\mu = n!$, and then
$$\mathcal{F}\bigl(R_\mu;q,t\bigr) \;=\; \sum_{r,s} q^r t^s \,\mathrm{ch}\bigl(R_\mu^{(r,s)}\bigr) \;=\; \tilde H_\mu(x;q,t),$$
which forces $\tilde K_{\lambda\mu}(q,t)\in\mathbb{N}[q,t]$ since these are multiplicities of irreducibles in bidegree $(r,s)$.

**Geometric input.** Let $\mathrm{Hilb}^n(\mathbb{C}^2)$ be the Hilbert scheme of $n$ points in the plane (smooth, dimension $2n$, Fogarty) and $X_n \subset \mathrm{Hilb}^n \times (\mathbb{C}^2)^n$ the **isospectral Hilbert scheme**, the reduced fibre product of the Hilbert–Chow morphism with $(\mathbb{C}^2)^n \to S^n\mathbb{C}^2$. Haiman's central theorem: $X_n$ is normal, Cohen–Macaulay and Gorenstein; equivalently $\mathbb{C}[x,y]$ is a free module over the invariant subring in the relevant polygraph sense. Fibres of $X_n\to\mathrm{Hilb}^n$ over torus-fixed points $I_\mu$ have coordinate ring $R_\mu$, of dimension $n!$.

## 3. History & State of the Art (SOTA)

- **1988** — Macdonald defines $P_\lambda(x;q,t)$ and states the positivity conjecture (Séminaire Lotharingien B20a); he verifies it for $n\le 6$ by hand/computer.
- **1988–1995** — Specializations recover known positivity: $q=0$ gives Kostka–Foulkes $K_{\lambda\mu}(t)$, positive by the Lascoux–Schützenberger charge statistic (1978); $q=t$ gives $s_\lambda$; $t=1$, $q=1$ trivial.
- **1993** — Garsia and Haiman propose $R_\mu$ and the $n!$ conjecture (PNAS 90), converting an identity of formal power series into a statement about a concrete polynomial module.
- **1996–1997** — Polynomiality $K_{\lambda\mu}(q,t)\in\mathbb{Z}[q,t]$ proved independently by Garsia–Tesler (plethystic operators), Kirillov–Noumi and Lapointe–Vinet (Rodrigues/creation operators), Knop and Sahi (interpolation polynomials). None gives positivity.
- **2001** — **Haiman proves the $n!$ conjecture and hence Macdonald positivity** ("Hilbert schemes, polygraphs and the Macdonald positivity conjecture", *JAMS* 14, 941–1006), via the polygraph freeness theorem and Cohen–Macaulayness of $X_n$.
- **2002** — Haiman proves the companion $(n+1)^{n-1}$ theorem for diagonal harmonics (*Invent. Math.* 149).
- **2005** — Haglund–Haiman–Loehr give a combinatorial formula for $\tilde H_\mu$ in the *monomial* basis (*JAMS* 18).
- **2015** — Assaf gives a combinatorial (dual equivalence graph) proof of Schur positivity for LLT and Macdonald polynomials (*Forum Math. Sigma* 3).

SOTA: positivity is a theorem in type $A$; the open frontier is combinatorial (explicit tableau statistics) and structural (other root systems, wreath/affine analogues).

## 4. Partial Results / Verified Cases

Before 2001, positivity was known for:

- **Hooks** $\mu=(a,1^b)$ — Garsia–Haiman (1993/1996), with explicit module decomposition.
- **Two-row shapes** $\mu=(\mu_1,\mu_2)$ and **two-column shapes** $\mu=(2^a1^b)$ — Fishel (1995) via rigged configurations, refined by Lapointe–Morse and Zabrocki with explicit statistics.
- **Augmented hooks** $\mu=(a,2,1^b)$ — Garsia–Haiman.
- **Small $n$**: computer verification of the $n!$ conjecture for $n\le 8$ (Garsia–Haiman tables); $K_{\lambda\mu}(q,t)$ tabulated for $n \le 9$.
- **Specializations**: $t=0$ (Hall–Littlewood/cocharge), $q=0$, $q=t$, $q=1$, $t=1$, and $q=t^{-1}$ all positive by classical results.
- **Integrality** $K_{\lambda\mu}\in\mathbb{Z}[q,t]$ for all $\lambda,\mu$ — Knop (1997), Sahi (1996), Garsia–Tesler (1996), Lapointe–Vinet (1997).

Post-2001, positivity holds for **all** $\lambda,\mu$ in type $A$. Explicit *combinatorial statistics* $(\mathrm{stat}_q,\mathrm{stat}_t)$ on $\mathrm{SYT}(\lambda)$ producing $\tilde K_{\lambda\mu}$ are known only for: $\mu$ a hook, $\mu$ with at most two columns or two rows, $\mu$ a rectangle in special cases, and the specializations above.

## 5. Principal Obstacles

- **No manifest positivity in the definition.** $K_{\lambda\mu}(q,t)$ arises from Gram–Schmidt against a $q,t$-deformed inner product; the resulting rational functions have large cancelling numerators. Nothing in the construction produces a set to count.
- **Failure of naive representation theory.** $R_\mu$ is *not* a coinvariant algebra of a reflection group, has no obvious basis, and its Hilbert series jumps discontinuously in $\mu$; standard Gröbner/straightening arguments give only $\dim R_\mu \ge$ or $\le n!$ in isolated shapes. Upper bounds $\dim R_\mu \le n!$ resisted all direct commutative-algebra attacks.
- **Singularities of $X_n$.** The isospectral Hilbert scheme is singular in codimension $\ge 2$; ordinary resolution or deformation arguments do not apply. Haiman's proof needs the *polygraph* theorem — freeness of $R(n,l)=\mathbb{C}[x,y,a,b]/I(Z(n,l))$ over $\mathbb{C}[y]$ — proved by an intricate induction on $l$ and on $n$ with no shortcut known.
- **Combinatorics of the residual gap.** The HHL formula expands $\tilde H_\mu$ in monomials with signs *absent*, but converting monomial positivity to Schur positivity requires cancellation; LLT polynomials sit in between and their Schur positivity has only non-elementary proofs (Grojnowski–Haiman via affine Hecke algebras, unpublished; Assaf via dual equivalence). No statistic-based rule survives beyond two rows/columns because candidate statistics fail crossing-symmetry $\tilde K_{\lambda\mu}(q,t)=\tilde K_{\lambda'\mu}(t,q)$ tests.

## 6. The Gap

Positivity itself: **closed** (Haiman 2001). The remaining gap is threefold.

1. **Combinatorial gap.** Find a family of sets $\mathcal{S}_{\lambda\mu}$ with statistics such that $\tilde K_{\lambda\mu}(q,t)=\sum_{T\in\mathcal{S}_{\lambda\mu}} q^{\mathrm{stat}_q(T)}t^{\mathrm{stat}_t(T)}$, generalizing charge ($q=0$). Known only for restricted $\mu$; the general case is open.
2. **Elementary-proof gap.** Haiman's proof is algebro-geometric and does not give a basis of $R_\mu$. An explicit $n!$-element basis of $R_\mu$ is still unknown for general $\mu$.
3. **Type gap.** For a reduced root system $R\ne A_{n-1}$, positivity of the $q,t$-analogues of Kostka numbers (Macdonald's conjecture in the general setting, and Cherednik-algebra analogues) is open; there is no Hilbert-scheme substitute for $\mathrm{Hilb}^n(\mathbb{C}^2)$.

## 7. Current Research (as of June 2026)

- **Elliptic Hall / shuffle-theorem school** (Berkeley, Penn, Virginia, Michigan): Carlsson–Mellit's proof of the shuffle theorem (*JAMS* 31, 2018) and Mellit's compositional refinement fed into Blasiak–Haiman–Morse–Pun–Seelinger, "A shuffle theorem for paths under any line" (*Forum Math. Pi* 11, 2023) and their work expressing LLT polynomials inside the Schiffmann algebra — a route toward uniform, positivity-explaining formulas. *(frontier — verify)*
- **Dual equivalence and crystal methods** (Assaf and collaborators): extending dual equivalence graphs and "$k$-Schur / queer crystal" structures to produce statistic-level proofs of $\tilde K_{\lambda\mu}$ positivity for wider $\mu$. *(frontier — verify)*
- **Categorification**: Gorsky–Negut–Rasmussen and successors relate Hilbert-scheme sheaves to Khovanov–Rozansky homology, giving homological interpretations of $q,t$-statistics.
- **Non-symmetric and wreath analogues**: Haglund–Haiman–Loehr non-symmetric Macdonald polynomials, and Orellana–Zabrocki / Bergeron work on Macdonald polynomials for $G\wr S_n$ and the "delta conjecture" family (D'Adderio–Mellit's proof of the compositional delta conjecture, 2022). *(frontier — verify)*
- **Other root systems**: Cherednik-algebra and affine-Springer-fibre approaches (Gorsky, Oblomkov, Yun) aiming at geometric models beyond type $A$.

## 8. Future Work

- Construct an explicit basis of $R_\mu$ indexed by a natural $n!$-set (standard tableaux pairs, or "$\mu$-compatible" monomials), which would give a self-contained algebraic proof of the $n!$ theorem.
- Produce statistics $(\mathrm{stat}_q,\mathrm{stat}_t)$ on $\mathrm{SYT}(\lambda)$ specializing to cocharge at $t=0$ and respecting $\lambda\mapsto\lambda'$ conjugation symmetry — Haiman's stated priority problem.
- Find a purely combinatorial proof of LLT Schur positivity that replaces the Grojnowski–Haiman affine Hecke argument; this would essentially deliver Macdonald positivity combinatorially through HHL.
- Identify a geometric object playing the role of $X_n$ for other root systems or for $\mathrm{Hilb}$ of surfaces with singularities, aiming at positivity beyond type $A$.

## 9. Key References

- **[Foundational]** I. G. Macdonald. *A new class of symmetric functions.* Séminaire Lotharingien de Combinatoire, 20 (1988), Article B20a.
- **[Foundational]** I. G. Macdonald. *Symmetric Functions and Hall Polynomials*, 2nd edition. Oxford University Press, 1995 (Chapter VI).
- **[Foundational]** A. M. Garsia and M. Haiman. *A graded representation model for Macdonald's polynomials.* Proc. Natl. Acad. Sci. USA, 90 (1993), 3607–3610.
- **[SOTA]** M. Haiman. *Hilbert schemes, polygraphs and the Macdonald positivity conjecture.* Journal of the American Mathematical Society, 14 (2001), 941–1006.
- **[SOTA]** M. Haiman. *Vanishing theorems and character formulas for the Hilbert scheme of points in the plane.* Inventiones Mathematicae, 149 (2002), 371–407.
- **[SOTA]** J. Haglund, M. Haiman and N. Loehr. *A combinatorial formula for Macdonald polynomials.* Journal of the American Mathematical Society, 18 (2005), 735–761.
- **[Recent]** S. Assaf. *Dual equivalence graphs I: A new paradigm for Schur positivity.* Forum of Mathematics, Sigma, 3 (2015), e12.
- **[Recent]** J. Blasiak, M. Haiman, J. Morse, A. Pun and G. Seelinger. *A shuffle theorem for paths under any line.* Forum of Mathematics, Pi, 11 (2023), e5.
- **[Recent]** E. Carlsson and A. Mellit. *A proof of the shuffle conjecture.* Journal of the American Mathematical Society, 31 (2018), 661–697.
- **[Partial results]** F. Knop. *Integrality of two variable Kostka functions.* Journal für die reine und angewandte Mathematik, 482 (1997), 177–189.
- **[Partial results]** S. Sahi. *Interpolation, integrality, and a generalization of Macdonald's polynomials.* International Mathematics Research Notices, 1996, no. 10, 457–471.
- **[Partial results]** A. M. Garsia and G. Tesler. *Plethystic formulas for Macdonald $q,t$-Kostka coefficients.* Advances in Mathematics, 123 (1996), 144–222.
- **[Partial results]** S. Fishel. *Statistics for special $q,t$-Kostka polynomials.* Proceedings of the American Mathematical Society, 123 (1995), 2961–2969.
- **[Survey]** J. Haglund. *The $q,t$-Catalan Numbers and the Space of Diagonal Harmonics.* AMS University Lecture Series 41, 2008.
- **[Survey]** M. Haiman. *Combinatorics, symmetric functions and Hilbert schemes.* Current Developments in Mathematics 2002, International Press, 2003, 39–111.

## 10. Worked Example / Concrete Special Case

Take $\mu=(2,1)$, $n=3$. Its cells are $(0,0),(1,0),(0,1)$ in $(\text{column},\text{row})$ exponent coordinates, so
$$\Delta_{(2,1)}(x,y)=\det\begin{pmatrix}1&x_1&y_1\\ 1&x_2&y_2\\ 1&x_3&y_3\end{pmatrix}
= (x_2y_3-x_3y_2)-(x_1y_3-x_3y_1)+(x_1y_2-x_2y_1).$$

$\Delta_{(2,1)}$ is bihomogeneous of bidegree $(1,1)$ and alternating. Applying $\partial_{x_i},\partial_{y_i}$:

| bidegree $(r,s)$ | spanning elements | $\dim$ | $S_3$-character |
|---|---|---|---|
| $(1,1)$ | $\Delta_{(2,1)}$ | 1 | $s_{111}$ |
| $(1,0)$ | $\partial_{y_i}\Delta$: spans $\{x_i-x_j\}$ | 2 | $s_{21}$ |
| $(0,1)$ | $\partial_{x_i}\Delta$: spans $\{y_i-y_j\}$ | 2 | $s_{21}$ |
| $(0,0)$ | $\partial_{x_i}\partial_{y_j}\Delta$ | 1 | $s_3$ |

Total dimension $1+2+2+1=6=3!$, confirming the $n!$ theorem here, and the bigraded Frobenius character is
$$\mathcal{F}(R_{(2,1)};q,t)\;=\; s_3 + (q+t)\,s_{21} + qt\,s_{111}\;=\;\tilde H_{(2,1)}(x;q,t).$$

Hence $\tilde K_{(3),(2,1)}=1$, $\tilde K_{(2,1),(2,1)}=q+t$, $\tilde K_{(1^3),(2,1)}=qt$ — all in $\mathbb{N}[q,t]$.

**Consistency checks.** Setting $q=t$ gives $s_3+2t\,s_{21}+t^2 s_{111}$, and indeed $\tilde H_\mu(x;t,t)$ is the Hall–Littlewood-type specialization whose $t=1$ value is $h_1^3 = s_3+2s_{21}+s_{111}$, the regular representation. Setting $t=0$ gives $s_3 + q\,s_{21}$, matching the cocharge Kostka–Foulkes polynomials $K_{\lambda,(2,1)}(q)$: $K_{(3),(2,1)}(q)=1$, $K_{(2,1),(2,1)}(q)=q$ — the charge statistic on the two standard tableaux of shape $(2,1)$. Conjugation symmetry also holds: $\tilde K_{\lambda'\mu}(q,t)$ for $\mu=(2,1)$ (self-conjugate) swaps $q\leftrightarrow t$ in $q+t$, as required.

The general problem is that no analogue of the charge statistic is known that reproduces the $q,t$-bigrading above for arbitrary $\mu$, even though Haiman's theorem guarantees the coefficients count *something*.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*