---
id: 08-logic-set-theory/conjugacy-problem-for-braid-groups
title: "Conjugacy Problem for Braid Groups"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Conjugacy Problem for Braid Groups

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/conjugacy-problem-for-braid-groups` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

One of Dehn's three decision problems (1911), specialised to Artin's braid groups $B_n$.

**Decision problem.** Given $n$ and two words $u,v$ in the generators $\sigma_1^{\pm1},\dots,\sigma_{n-1}^{\pm1}$, decide whether there is $c \in B_n$ with $c^{-1}uc = v$.

**Search problem.** If so, output such a $c$.

Decidability was settled by Garside (1969). The live question is **complexity**:

> **(Q)** Is there an algorithm deciding conjugacy in $B_n$ in time polynomial in $n$ and $\ell = |u| + |v|$?

A complete answer requires either (i) an algorithm with a proved bound $\mathrm{poly}(n,\ell)$, or (ii) a hardness result placing the problem outside $\mathsf{P}$ under a standard assumption. The status is *solved-recently* in a precise sense: Bell–Webb (2016) give an algorithm polynomial in $\ell$ for each **fixed** surface, hence for each fixed $n$; uniformity in $n$, and any polynomial bound inside the classical Garside framework, remain open.

The **conjugacy search problem** (CSP) with a promise that $u\sim v$ is the security assumption of braid-group cryptography and is tracked separately below.

## 2. Mathematical Foundations

**Artin presentation.**
$$B_n=\Big\langle \sigma_1,\dots,\sigma_{n-1}\ \Big|\ \sigma_i\sigma_j=\sigma_j\sigma_i\ (|i-j|\ge2),\ \ \sigma_i\sigma_{i+1}\sigma_i=\sigma_{i+1}\sigma_i\sigma_{i+1}\Big\rangle .$$
Equivalently $B_n\cong \mathrm{MCG}(D_n)$, the mapping class group of the disk with $n$ punctures fixing $\partial D$.

**Garside structure.** Let $B_n^+$ be the monoid of positive words. It has left/right cancellation and lattice structure for the prefix order $a\preccurlyeq b \iff a^{-1}b\in B_n^+$. The **Garside element** is
$$\Delta=(\sigma_1)(\sigma_2\sigma_1)\cdots(\sigma_{n-1}\cdots\sigma_1),\qquad \Delta^2\in Z(B_n),\quad \tau(x)=\Delta^{-1}x\Delta .$$
The **simple elements** (permutation braids) are the divisors $1\preccurlyeq s\preccurlyeq\Delta$; there are $n!$ of them, in bijection with $S_n$.

**Left normal form.** Every $x\in B_n$ factors uniquely as
$$x=\Delta^{p}s_1s_2\cdots s_r,\qquad 1\neq s_i\neq\Delta,\ \ s_is_{i+1}\ \text{left-weighted},$$
where left-weighted means $\alpha(s_{i+1}) \preccurlyeq \ \text{(the maximal simple prefix of } s_{i+1})$ is absorbed by $s_i$. Set $\inf(x)=p$, $\sup(x)=p+r$, canonical length $\ell_c(x)=r$. Normal form is computable in $O(\ell^2 n\log n)$ (Thurston).

**Conjugacy invariants.** With $\inf_s(x)=\max\{\inf(y):y\sim x\}$, $\sup_s(x)=\min\{\sup(y):y\sim x\}$,
$$\mathrm{SSS}(x)=\{y\sim x:\inf(y)=\inf_s(x),\ \sup(y)=\sup_s(x)\}$$
is the **super summit set** — finite, nonempty, and computable, and $x\sim y \iff \mathrm{SSS}(x)\cap\mathrm{SSS}(y)\neq\emptyset$ (El-Rifai–Morton).

**Cycling / decycling / sliding.** If $x=\Delta^{p}s_1\cdots s_r$,
$$\mathbf{c}(x)=\big(\tau^{-p}(s_1)\big)^{-1}\,x\,\tau^{-p}(s_1),\qquad \mathbf{d}(x)=s_r\,x\,s_r^{-1}.$$
Iterating $\mathbf{c}$ and $\mathbf{d}$ at most $O(\ell_c(x)\,n(n-1)/2)$ times reaches $\mathrm{SSS}(x)$ (Birman–Gebhardt–González-Meneses). Refinements: **ultra summit set** $\mathrm{USS}(x)=\{y\in\mathrm{SSS}(x): \mathbf{c}^m(y)=y \text{ some } m\ge1\}$ (Gebhardt 2005) and the **set of sliding circuits** $\mathrm{SC}(x)$ under cyclic sliding $\mathfrak{s}(x)=\mathfrak{p}(x)^{-1}x\,\mathfrak{p}(x)$, with $\mathfrak{p}(x)$ the preferred prefix (Gebhardt–González-Meneses 2010). Always $\mathrm{SC}(x)\subseteq\mathrm{USS}(x)\subseteq\mathrm{SSS}(x)$.

**Nielsen–Thurston trichotomy.** Each $x\in B_n$ is periodic ($x^k\in\{\Delta^{2m},\delta^{m}\}$), reducible (preserves a family of disjoint essential curves), or pseudo-Anosov (preserves a pair of transverse measured foliations with dilatation $\lambda(x)>1$), and $\lambda$ is a conjugacy invariant.

## 3. History & State of the Art (SOTA)

- **1925/1947 — Artin.** *Theorie der Zöpfe* introduces $B_n$; the 1947 *Theory of braids* solves the word problem via combing and sketches, incompletely, a conjugacy argument.
- **1969 — Garside.** Summit sets give the first correct decision procedure. Bound: exponential in $\ell$ and $n$.
- **1994 — El-Rifai–Morton.** Super summit sets; cycling/decycling reduce $\ell_c$ monotonically. Complexity $O(\ell^2 n\log n)$ per conjugation step, but $|\mathrm{SSS}|$ may be exponential.
- **1998 — Birman–Ko–Lee.** The dual (BKL) Garside structure with $\delta=\sigma_{n-1}\cdots\sigma_1$ and Catalan-many simple elements; word problem in $O(\ell^2 n)$.
- **2003–2005 — Franco–González-Meneses; Gebhardt.** SSS and then USS computed by a *convexity* argument: closure under minimal simple conjugators, giving a connected-graph search of cost $O(|\mathrm{USS}(x)|\cdot \ell_c \cdot n \cdot \text{(simple elements)})$.
- **2007–2010 — Birman–Gebhardt–González-Meneses.** Structure theory of USS: rigidity, stable ultra summit sets, periodic elements handled separately; then cyclic sliding and $\mathrm{SC}(x)$, the current canonical Garside-theoretic invariant.
- **2011 — Prasolov.** Explicit braids of small word length whose ultra summit sets are exponentially large — the Garside route is not polynomial as stated.
- **2013 — Tao.** Linearly bounded conjugator property for mapping class groups: if $u\sim v$ there is $c$ with $|c| = O(|u|+|v|)$. Puts conjugacy in $\mathsf{NP}$ for fixed $n$.
- **2016 — Bell–Webb.** Polynomial-time algorithms for the curve complex yield a polynomial-time (in word length) solution of the conjugacy problem in $\mathrm{MCG}$ of a fixed punctured surface, hence in $B_n$ for fixed $n$. This is the "solved-recently" result.

## 4. Partial Results / Verified Cases

- **All $n$, decidability:** solved since Garside 1969; also solvable via Nielsen–Thurston + train tracks (Bestvina–Handel).
- **Fixed $n$, polynomial in $\ell$:** Bell–Webb (2016); the degree of the polynomial depends on $n$ and is not made small.
- **$n\le 3$:** $B_3$ is the trefoil knot group, $\langle a,b\mid a^2=b^3\rangle$; conjugacy is linear-time via the central quotient $B_3/Z \cong \mathrm{PSL}_2(\mathbb Z)\cong \mathbb Z/2 * \mathbb Z/3$ and cyclic reduction in a free product.
- **$n=4$:** Calvez–Wiest give a quadratic-time algorithm — $O(\ell^2)$ — for conjugacy in $B_4$, using the fact that the curve complex of $D_4$ is a Farey graph.
- **Periodic braids (all $n$):** conjugacy decidable in polynomial time; classification is by $\inf_s$ and the power of $\delta$ or $\gamma=\sigma_1\delta$ (BGGM III).
- **Rigid pseudo-Anosov braids:** if $x$ is rigid then $\mathrm{SC}(x)=\{\tau^k(\mathbf{c}^j(x))\}$ has size $O(\ell_c \cdot n)$, giving polynomial cost.
- **Generic braids:** for a random word of length $\ell$ in $B_n$, the sliding-circuit set is with high probability of size $O(\ell_c n)$ (rigidity is generic), so the Garside algorithm is generically polynomial.
- **Structural:** $n$-th roots are unique up to conjugacy in $B_n$ (González-Meneses 2003); centralisers are finitely generated with a polynomial-size generating set for rigid elements.

## 5. Principal Obstacles

- **Exponential invariant sets.** The Garside algorithms are search procedures over $\mathrm{SSS}$/$\mathrm{USS}$/$\mathrm{SC}$, and Prasolov's examples show $|\mathrm{USS}|$ grows exponentially in $\ell$ for braids of bounded canonical length. No invariant subset of an SSS is known that is both provably polynomial-size and provably a complete conjugacy invariant.
- **Reducible braids are the hard core.** Periodic and rigid pseudo-Anosov cases are controlled; reducible braids force recursion into the components of the canonical reduction system, and the interaction between the tubular braid on components and the interior braids resists a clean complexity accounting.
- **Geometric methods are not uniform in $n$.** Bell–Webb's bound hides constants and exponents growing with the complexity of the curve complex (equivalently with $n$); the same is true of train-track and Masur–Minsky hierarchy arguments, where the distance formula's threshold constant depends on the surface.
- **Linearity does not help.** Bigelow/Krammer linearity of $B_n$ gives faithful matrix representations, but conjugacy of matrices in $\mathrm{GL}_m(\mathbb Z[q^{\pm1},t^{\pm1}])$ restricted to the image subgroup is not known to be easier than the original problem.
- **Dilatation is a weak certificate.** $\lambda(x)$ separates most pseudo-Anosov classes but is a real algebraic number whose comparison costs, and non-conjugate braids can share it.

## 6. The Gap

Proven: decidability (all $n$); polynomial time in $\ell$ for each fixed $n$ (Bell–Webb); explicit low-degree polynomial algorithms only for $n\le4$; polynomial time for periodic, rigid, and generic braids at all $n$.

Missing: a single algorithm with an explicit bound $\mathrm{poly}(n,\ell)$ covering all inputs — equivalently, either (a) a proof that $|\mathrm{SC}(x)|$ can be replaced by a polynomially-computable complete invariant for reducible and non-rigid pseudo-Anosov braids, or (b) an extraction of an $n$-uniform complexity bound from the curve-complex machinery. The crossing step is control of the reducible case: bounding the recursion depth and the cost of locating the canonical reduction system in time polynomial in $n$ *and* $\ell$ simultaneously.

## 7. Current Research (as of June 2026)

- **Garside/geometry synthesis** (Rennes, Sevilla, Santiago): Calvez, Wiest and González-Meneses relate the Garside "sliding circuits" graph to the additive structure of the curve graph, aiming at an $n$-uniform bound. Announced quasi-polynomial bounds for reducible braids remain unpublished *(frontier — verify)*.
- **Curve-complex algorithmics** (Bell, Webb, and the `flipper`/`curver` software line): explicit implementations giving conjugacy decisions for $n\le 12$ on words of length $10^4$ *(frontier — verify)*.
- **Cryptanalysis** (Myasnikov–Shpilrain–Ushakov school): length-based and linear-representation attacks continue to break braid-based key exchange in practice, evidence that the *search* problem is easy on the distributions used, though no worst-case algorithm follows.
- **Garside theory beyond braids** (Dehornoy, Digne, Godelle, Michel, Paris): conjugacy complexity in Artin groups of spherical type and of FC type, where the same $\mathrm{SC}$ machinery applies verbatim.

## 8. Future Work

1. Prove or refute $|\mathrm{SC}(x)|\le \mathrm{poly}(n,\ell)$ for reducible braids after passing to the canonical reduction system.
2. Make Tao's linear conjugator bound effective and uniform in $n$; this would put conjugacy in $\mathsf{NP}$ uniformly, and with a matching co-certificate in $\mathsf{NP}\cap\mathsf{coNP}$.
3. Extract an explicit exponent from Bell–Webb as a function of $n$.
4. Settle the complexity of the conjugacy *search* problem with adversarially chosen instances — the missing ingredient for any honest security claim in braid cryptography.
5. Extend to the twisted/orbifold settings: conjugacy in $\mathrm{MCG}$ of closed surfaces with the same bounds.

## 9. Key References

- **[Foundational]** E. Artin. *Theorie der Zöpfe.* Abh. Math. Sem. Univ. Hamburg 4 (1925), 47–72.
- **[Foundational]** E. Artin. *Theory of Braids.* Annals of Mathematics 48 (1947), 101–126.
- **[Foundational]** F. A. Garside. *The braid group and other groups.* Quarterly Journal of Mathematics (Oxford) 20 (1969), 235–254.
- **[Foundational]** E. A. El-Rifai, H. R. Morton. *Algorithms for positive braids.* Quarterly Journal of Mathematics (Oxford) 45 (1994), 479–497.
- **[SOTA]** J. Birman, K. H. Ko, S. J. Lee. *A new approach to the word and conjugacy problems in the braid group.* Advances in Mathematics 139 (1998), 322–353.
- **[SOTA]** N. Franco, J. González-Meneses. *Conjugacy problem for braid groups and Garside groups.* Journal of Algebra 266 (2003), 112–132.
- **[SOTA]** V. Gebhardt. *A new approach to the conjugacy problem in Garside groups.* Journal of Algebra 292 (2005), 282–302.
- **[SOTA]** J. Birman, V. Gebhardt, J. González-Meneses. *Conjugacy in Garside groups I: cyclings, powers and rigidity.* Groups, Geometry and Dynamics 1 (2007), 221–279.
- **[SOTA]** V. Gebhardt, J. González-Meneses. *The cyclic sliding operation in Garside groups.* Mathematische Zeitschrift 265 (2010), 85–114.
- **[SOTA / Recent]** M. Bell, R. Webb. *Polynomial-time algorithms for the curve complex.* arXiv:1605.08983, 2016.
- **[SOTA / Recent]** J. Tao. *Linearly bounded conjugator property for mapping class groups.* Geometric and Functional Analysis 23 (2013), 415–466.
- **[SOTA / Recent]** M. Calvez, B. Wiest. *Fast algorithmic Nielsen–Thurston classification of four-strand braids.* Journal of Knot Theory and Its Ramifications 21 (2012), 1250043.
- **[Related]** M. V. Prasolov. *Small braids with large ultra summit set.* Mathematical Notes 89 (2011), 545–554.
- **[Related]** K. H. Ko, S. J. Lee, J. H. Cheon, J. W. Han, J. Kang, C. Park. *New public-key cryptosystem using braid groups.* CRYPTO 2000, LNCS 1880, 166–183.
- **[Related]** S. Bigelow. *Braid groups are linear.* Journal of the AMS 14 (2001), 471–486.
- **[Survey]** P. Dehornoy, F. Digne, E. Godelle, D. Krammer, J. Michel. *Foundations of Garside Theory.* EMS Tracts in Mathematics 22, 2015.
- **[Survey]** J. González-Meneses. *Basic results on braid groups.* Annales Mathématiques Blaise Pascal 18 (2011), 15–59.

## 10. Worked Example / Concrete Special Case

**Claim.** In $B_3$, $\sigma_1\sigma_2 \sim \sigma_2\sigma_1$, but $\sigma_1\sigma_2 \not\sim \sigma_1^2$.

*Simple elements of $B_3$.* $\Delta=\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2$; the divisors of $\Delta$ are $\{1,\sigma_1,\sigma_2,\sigma_1\sigma_2,\sigma_2\sigma_1,\Delta\}$, matching the six elements of $S_3$.

*Normal forms.* $\sigma_1\sigma_2$ is simple, so its left normal form is $\Delta^0\cdot(\sigma_1\sigma_2)$ with $\inf=0$, $\sup=1$, $\ell_c=1$. For $\sigma_1^2$: $\sigma_1\cdot\sigma_1$ is left-weighted (the maximal simple prefix of the second factor is $\sigma_1$, already a right factor of the first), so $\inf=0$, $\sup=2$, $\ell_c=2$.

*Cycling.* Both are already cyclically reduced: $\mathbf{c}(\sigma_1\sigma_2)=(\sigma_1\sigma_2)^{-1}(\sigma_1\sigma_2)(\sigma_1\sigma_2)=\sigma_1\sigma_2$, and $\mathbf{c}(\sigma_1^2)=\sigma_1^{-1}\sigma_1^2\sigma_1=\sigma_1^2$. Since neither cycling nor decycling raises $\inf$ or lowers $\sup$, we have $\inf_s=0$, $\sup_s(\sigma_1\sigma_2)=1$, $\sup_s(\sigma_1^2)=2$.

*Conclusion 1 (non-conjugacy).* $\sup_s$ is a conjugacy invariant and $1\neq2$, so $\sigma_1\sigma_2\not\sim\sigma_1^2$. Cross-check by Nielsen–Thurston: $(\sigma_1\sigma_2)^3=\Delta^2$ is central, so $\sigma_1\sigma_2$ is periodic; $\sigma_1^2$ fixes the curve around punctures $1,2$, so it is reducible. Distinct types, hence non-conjugate.

*Conclusion 2 (conjugacy).* $\mathrm{SSS}(\sigma_1\sigma_2)$ consists of simple elements of canonical length $1$ conjugate to $\sigma_1\sigma_2$. Conjugating by the minimal simple conjugators $\sigma_1$ and $\sigma_2$:
$$\sigma_1^{-1}(\sigma_1\sigma_2)\sigma_1=\sigma_2\sigma_1,\qquad \sigma_2^{-1}(\sigma_2\sigma_1)\sigma_2=\sigma_1\sigma_2 ,$$
using $\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2$. The search closes: $\mathrm{SSS}(\sigma_1\sigma_2)=\{\sigma_1\sigma_2,\ \sigma_2\sigma_1\}$, of size $2$, and $\sigma_1$ is an explicit conjugator.

*What this illustrates.* The whole algorithm is visible: normalise, cycle to the summit set, then breadth-first search the summit graph along minimal simple conjugators. Here the graph has $2$ vertices. Prasolov's braids have summit graphs with exponentially many vertices for words barely longer than this one — that gap, not decidability, is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*