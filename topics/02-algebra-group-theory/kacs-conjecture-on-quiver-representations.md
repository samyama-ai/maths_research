---
id: 02-algebra-group-theory/kacs-conjecture-on-quiver-representations
title: "Kac's Conjecture on Quiver Representations"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kac's Conjecture on Quiver Representations

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kacs-conjecture-on-quiver-representations` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $Q=(I,\Omega)$ be a finite quiver (directed graph, loops and multiple arrows allowed) and let $\alpha\in\mathbb{Z}_{\ge0}^{I}$ be a dimension vector. For a finite field $\mathbb{F}_q$, let $A_\alpha(q)$ be the number of isomorphism classes of **absolutely indecomposable** representations of $Q$ over $\mathbb{F}_q$ of dimension vector $\alpha$.

Kac proved that $A_\alpha(q)$ is a polynomial in $q$ with integer coefficients, independent of the orientation $\Omega$, and conjectured two properties of it:

- **(K1) Positivity.** $A_\alpha(q)\in\mathbb{Z}_{\ge0}[q]$.
- **(K2) Constant term.** For $Q$ without loops, $A_\alpha(0)=\operatorname{mult}_{\alpha}\mathfrak{g}_Q$, the multiplicity of $\alpha$ as a root of the Kac–Moody algebra $\mathfrak{g}_Q$ attached to the underlying graph.

A complete proof of (K1) requires exhibiting, for every $Q$ and every $\alpha$, either a graded vector space or a variety with polynomial point count whose Betti numbers are the coefficients of $A_\alpha$ — or any other argument forcing non-negativity. (K2) requires matching a point-count constant term with a Lie-theoretic multiplicity that has no known closed formula. Both are now theorems: (K2) by Crawley-Boevey–Van den Bergh (2004, indivisible $\alpha$) and Hausel (2010, all $\alpha$); (K1) by Hausel–Letellier–Rodriguez-Villegas (2013). What remains open is the **effective** content: a manifestly positive combinatorial formula for $A_\alpha(q)$, and the loop/cuspidal refinements.

## 2. Mathematical Foundations

**Representations.** A representation of $Q$ over a field $k$ of dimension vector $\alpha$ is $x=(x_a)_{a\in\Omega}$ with $x_a\in\operatorname{Hom}_k(k^{\alpha_{s(a)}},k^{\alpha_{t(a)}})$. The representation space and gauge group are
$$\operatorname{Rep}(Q,\alpha)=\bigoplus_{a\in\Omega}\operatorname{Mat}_{\alpha_{t(a)}\times\alpha_{s(a)}}(k),\qquad G_\alpha=\prod_{i\in I}\mathrm{GL}_{\alpha_i}(k),$$
with $G_\alpha$ acting by $g\cdot x_a=g_{t(a)}x_ag_{s(a)}^{-1}$. Isomorphism classes are $G_\alpha$-orbits. A representation over $\mathbb{F}_q$ is *absolutely indecomposable* if it stays indecomposable after base change to $\overline{\mathbb{F}_q}$.

**Forms and root system.** The Euler form and Tits form are
$$\langle\alpha,\beta\rangle=\sum_{i\in I}\alpha_i\beta_i-\sum_{a\in\Omega}\alpha_{s(a)}\beta_{t(a)},\qquad q(\alpha)=\tfrac12\big(\langle\alpha,\alpha\rangle+\langle\alpha,\alpha\rangle\big)=\langle\alpha,\alpha\rangle .$$
For loop-free $Q$ the matrix $C=(c_{ij})$, $c_{ii}=2$, $c_{ij}=-\\#\{\text{edges }i\!-\!j\}$ for $i\neq j$, is a symmetric generalized Cartan matrix; $\mathfrak{g}_Q$ is the associated Kac–Moody algebra with root lattice $\mathbb{Z}^I$ and root multiplicities $\operatorname{mult}_\alpha=\dim(\mathfrak{g}_Q)_\alpha$.

**Kac's theorems (1980, 1983).**
1. $A_\alpha\in\mathbb{Z}[q]$, independent of orientation.
2. $A_\alpha\neq0$ if and only if $\alpha$ is a positive root of $\mathfrak{g}_Q$.
3. $\deg A_\alpha=1-q(\alpha)$. In particular $A_\alpha=1$ for real roots ($q(\alpha)=1$), and $\deg A_\alpha\ge1$ for imaginary roots.

**Hua's formula (2000).** With $\boldsymbol\pi=(\pi^i)_{i\in I}$ a tuple of partitions, $\langle\lambda,\mu\rangle=\sum_k\lambda'_k\mu'_k$, $b_\lambda(q)=\prod_{k\ge1}\prod_{j=1}^{m_k(\lambda)}(1-q^{j})$, and $\operatorname{Exp}$ the plethystic exponential,
$$\sum_{\boldsymbol\pi}\frac{\prod_{a\in\Omega}q^{\langle\pi^{s(a)},\pi^{t(a)}\rangle}}{\prod_{i\in I}q^{\langle\pi^i,\pi^i\rangle}\,b_{\pi^i}(q^{-1})}\prod_{i\in I}X_i^{|\pi^i|}\;=\;\operatorname{Exp}\!\Big(\sum_{\alpha>0}\frac{A_\alpha(q)}{q-1}\,X^{\alpha}\Big).$$
This computes every $A_\alpha$ in finitely many steps but manifests no positivity: the left side is an alternating sum after taking $\operatorname{Log}$.

**Deformed preprojective algebras.** For $\lambda\in k^I$, $\Pi^\lambda(Q)=k\overline{Q}/\big(\sum_{a}[a,a^*]-\sum_i\lambda_ie_i\big)$, where $\overline{Q}$ is the double. Its representation variety is $\mu^{-1}(\lambda)\subset T^*\operatorname{Rep}(Q,\alpha)$ for the moment map $\mu(x,y)=\sum_a[x_a,y_a]$. For $\lambda$ generic on $\alpha$ (i.e. $\lambda\cdot\beta\neq0$ for all $0<\beta<\alpha$), the quotient $\mathcal{M}_\lambda(\alpha)=\mu^{-1}(\lambda)/\!\!/G_\alpha$ is a smooth symplectic variety of dimension $2-2q(\alpha)$ when $\alpha$ is a positive root (Crawley-Boevey, 2001).

## 3. History & State of the Art (SOTA)

- **1980–1983.** Kac introduced the count $A_\alpha(q)$ in *Infinite root systems, representations of graphs and invariant theory* (Invent. Math. 56) and stated (K1), (K2) in the 1982 Montecatini lectures. The motivation: Gabriel's theorem ($Q$ of finite representation type $\iff$ underlying graph is ADE, indecomposables $\leftrightarrow$ positive roots) suggested that quiver counting should compute Kac–Moody root multiplicities, which have no known formula in the indefinite case.
- **2000.** Hua gave the closed generating function above, making $A_\alpha$ computable and confirming (K1)–(K2) on large tables.
- **2004.** Crawley-Boevey and Van den Bergh proved, for $\alpha$ **indivisible** ($\gcd_i\alpha_i=1$),
$$A_\alpha(q)=\sum_{i\ge0}\dim H^{2i}\big(\mathcal{M}_\lambda(\alpha)\big)\,q^{i},$$
via counting $\mathbb{F}_q$-points of $\mathcal{M}_\lambda(\alpha)$ and purity of its cohomology. This gives (K1) and (K2) for indivisible $\alpha$.
- **2010.** Hausel proved (K2) in full generality using Nakajima quiver varieties, Nakajima's realization of weight spaces of integrable highest-weight modules, and the Weyl–Kac character formula.
- **2013.** Hausel, Letellier and Rodriguez-Villegas proved (K1) for all $Q$ and all $\alpha$, by relating $A_\alpha$ to the pure part of mixed Hodge polynomials of twisted character/quiver varieties and reducing divisible $\alpha$ to an indivisible dimension vector of an enlarged quiver.
- **2013.** Mozgovoy gave a second proof of (K1) via motivic Donaldson–Thomas theory, identifying $A_\alpha$ with a DT invariant of the tripled quiver with potential.
- **2020–2025.** Davison, and Davison–Hennecart–Schlegel Mejia, produced a canonical graded vector space — BPS cohomology of the 2-Calabi–Yau category of $\Pi(Q)$-modules — whose Poincaré polynomial is $A_\alpha(q)$, with a BPS Lie algebra structure containing $\mathfrak{g}_Q$.

## 4. Partial Results / Verified Cases

- **Real roots** ($q(\alpha)=1$): $A_\alpha(q)=1$ exactly; unique indecomposable, positivity trivial (Kac 1980).
- **ADE quivers**: all positive roots real, $A_\alpha\equiv1$; Gabriel's theorem.
- **Affine (extended Dynkin) quivers**: $\alpha=n\delta$ imaginary, $A_{n\delta}(q)=q+\operatorname{mult}_\delta$-type expressions; for the Kronecker quiver $A_{(n,n)}(q)=q+1$ for all $n\ge1$.
- **Indivisible $\alpha$, any $Q$**: (K1) and (K2) proved by Crawley-Boevey–Van den Bergh (2004) with an explicit Betti-number interpretation.
- **All $\alpha$, loop-free $Q$**: (K2) proved by Hausel (2010); (K1) proved by HLRV (2013) and independently Mozgovoy (2013).
- **Quivers with loops**: Bozec–Schiffmann (2019) proved integrality and positivity of the *absolutely cuspidal* polynomials $C_\alpha(q)$ refining $A_\alpha$, and Bozec (2016) built the corresponding generalized crystal/Borcherds-algebra framework.
- **Computations**: Hua's formula has been evaluated for hundreds of $(Q,\alpha)$ pairs, e.g. the $g$-loop quiver, star-shaped quivers with legs of length $\le4$, and $\alpha$ with $|\alpha|\le20$; all consistent with (K1)–(K2).

## 5. Principal Obstacles

The historical obstacles, several still binding for the effective refinements:

- **No canonical variety for divisible $\alpha$.** For $\gcd_i\alpha_i>1$ there is no generic $\lambda$, so $\mathcal{M}_\lambda(\alpha)$ is singular and its cohomology is not pure; the CBVdB point-count argument breaks down exactly where semistable-but-not-stable representations appear. HLRV's fix is an indirect reduction, not a construction of the missing space.
- **Alternating combinatorics.** Hua's formula only yields $A_\alpha$ after a plethystic logarithm, which subtracts terms; no rewriting of $\operatorname{Log}$ into a sum of monomials with non-negative coefficients is known. Standard partition-combinatorics identities (Hall–Littlewood, Macdonald) produce rational functions whose positivity is itself as hard as the original problem.
- **Root multiplicities are not computable in closed form.** For indefinite Kac–Moody algebras, $\operatorname{mult}_\alpha$ is given only by recursive formulas (Peterson, Berman–Moody); so (K2) could not be checked term-by-term, only structurally.
- **Perverse/weight machinery is orientation-sensitive.** The obvious geometric candidates (Lusztig's nilpotent variety, orbit closures) depend on the orientation while $A_\alpha$ does not, so no naive Deligne-weight argument transfers.
- **Wall-crossing loses purity.** DT-style proofs give positivity only after integrality theorems whose own proofs need cohomological vanishing that fails for non-symmetric or non-2CY situations, blocking generalization to modulated/valued quivers over non-split fields.

## 6. The Gap

The gap in the original conjecture is closed. The residual gap is between *existence* and *effectivity*:

1. **Proven:** $A_\alpha(q)$ has non-negative coefficients and $A_\alpha(0)=\operatorname{mult}_\alpha\mathfrak{g}_Q$; the coefficients are dimensions of BPS cohomology groups $\dim\mathrm{BPS}_{\alpha}^{2i}$.
2. **Not proven:** any *manifestly positive* formula — a set of combinatorial objects (crystals, cells, paths) of cardinality $A_\alpha(q)$'s coefficients, computable without cancellation. Equivalently, no cell decomposition of a space with $\mathbb{F}_q$-point count $A_\alpha(q)$ is known for divisible $\alpha$.
3. **Not proven:** the loop analogue of (K2) beyond Bozec's crystal framework, and the conjectural equality of cuspidal polynomials $C_\alpha$ with multiplicities in the BPS Lie algebra for arbitrary quivers with loops.

## 7. Current Research (as of June 2026)

- **Cohomological Hall algebras and BPS Lie algebras.** Davison (Edinburgh), Hennecart, Schlegel Mejia: the BPS cohomology of $\Pi(Q)$ is a Lie algebra $\mathfrak{g}^{\mathrm{BPS}}_Q$ whose $\alpha$-graded piece has Poincaré polynomial $A_\alpha(q)$ and whose degree-zero part is $\mathfrak{g}_Q$ — a structural strengthening of both (K1) and (K2). *(frontier — verify)*
- **Nonabelian Hodge theory for stacks**, relating Kac polynomials for a quiver to Betti/Dolbeault invariants of character stacks of punctured surfaces (Hausel–Letellier–Rodriguez-Villegas programme; Schiffmann and Fedorov–Soibelman–Soibelman on Higgs bundles).
- **Curve analogues.** Schiffmann's counting of absolutely indecomposable vector bundles/Higgs bundles on curves over $\mathbb{F}_q$ produces polynomials with the same expected positivity; genus-$g$ analogues of Kac polynomials remain partly conjectural. *(frontier — verify)*
- **Quivers with loops and Borcherds algebras.** Bozec–Schiffmann–Vasserot on cuspidal polynomials and the Lusztig nilpotent variety.
- **Categorification/crystals.** Attempts to build a crystal basis whose weight-graded pieces reproduce Kac polynomial coefficients directly.

## 8. Future Work

- Construct, for divisible $\alpha$, an explicit smooth or cellular space with $\mathbb{F}_q$-point count $A_\alpha(q)$ — the direct analogue of $\mathcal{M}_\lambda(\alpha)$; this would replace the HLRV reduction by a uniform proof.
- Extract from the BPS Lie algebra an explicit basis indexed combinatorially, giving the first cancellation-free formula for $A_\alpha$ and hence a positive formula for indefinite Kac–Moody root multiplicities.
- Prove the cuspidal-positivity conjectures for all quivers with loops, completing the Borcherds-algebra picture.
- Extend the counting to modulated quivers (species) over non-algebraically-closed fields, where even polynomiality is open in general.
- Determine the second-highest coefficients of $A_\alpha$ and their Lie-theoretic meaning; only $\deg A_\alpha=1-q(\alpha)$ and $A_\alpha(0)$ are currently understood.

## 9. Key References

- **[Foundational]** V. G. Kac. *Infinite root systems, representations of graphs and invariant theory.* Inventiones Mathematicae 56 (1980), 57–92.
- **[Foundational]** V. G. Kac. *Root systems, representations of quivers and invariant theory.* In: Invariant Theory (Montecatini 1982), Lecture Notes in Mathematics 996, Springer, 1983, 74–108.
- **[Foundational]** V. G. Kac. *Infinite Dimensional Lie Algebras.* 3rd edition, Cambridge University Press, 1990.
- **[Computational]** J. Hua. *Counting representations of quivers over finite fields.* Journal of Algebra 226 (2000), 1011–1033.
- **[Structural]** W. Crawley-Boevey. *Geometry of the moment map for representations of quivers.* Compositio Mathematica 126 (2001), 257–293.
- **[Milestone]** W. Crawley-Boevey and M. Van den Bergh. *Absolutely indecomposable representations and Kac's conjecture.* Inventiones Mathematicae 155 (2004), 537–559.
- **[Milestone]** T. Hausel. *Kac's conjecture from Nakajima quiver varieties.* Inventiones Mathematicae 181 (2010), 21–37.
- **[SOTA]** T. Hausel, E. Letellier, F. Rodriguez-Villegas. *Arithmetic harmonic analysis on character and quiver varieties.* Duke Mathematical Journal 160 (2011), 323–400.
- **[SOTA]** T. Hausel, E. Letellier, F. Rodriguez-Villegas. *Positivity for Kac polynomials and DT-invariants of quivers.* Annals of Mathematics (2) 177 (2013), 1147–1168.
- **[SOTA]** S. Mozgovoy. *Motivic Donaldson–Thomas invariants and the Kac conjecture.* Compositio Mathematica 149 (2013), 495–504.
- **[Recent]** T. Bozec, O. Schiffmann. *Counting absolutely cuspidals for quivers.* Mathematische Zeitschrift 292 (2019), 133–149.
- **[Recent]** B. Davison. *The integrality conjecture and the cohomology of 2CY categories.* Preprint, arXiv:2007.03289 (2020).
- **[Recent]** B. Davison, L. Hennecart, S. Schlegel Mejia. *BPS Lie algebras for totally negative 2-Calabi–Yau categories and nonabelian Hodge theory for stacks.* Preprint, arXiv:2212.07668 (2022).
- **[Survey]** O. Schiffmann. *Kac polynomials and Lie algebras associated to quivers and curves.* Proceedings of the International Congress of Mathematicians, Rio de Janeiro 2018, Vol. II, 1411–1442.
- **[Background]** H. Nakajima. *Instantons on ALE spaces, quiver varieties, and Kac–Moody algebras.* Duke Mathematical Journal 76 (1994), 365–416.

## 10. Worked Example / Concrete Special Case

**The Kronecker quiver.** $Q$: two vertices $1,2$ and two arrows $a,b:1\to2$. Then
$$q(\alpha)=\alpha_1^2+\alpha_2^2-2\alpha_1\alpha_2=(\alpha_1-\alpha_2)^2,$$
and $\mathfrak{g}_Q=\widehat{\mathfrak{sl}_2}$ (affine $A_1^{(1)}$). Positive roots: real roots with $(\alpha_1-\alpha_2)^2=1$, i.e. $(n,n\pm1)$; imaginary roots $n\delta=(n,n)$, each of multiplicity $1$.

**Case $\alpha=(1,1)$.** $\operatorname{Rep}(Q,\alpha)=\{(x,y)\in\mathbb{F}_q^2\}$, $G_\alpha=\mathbb{F}_q^\times\times\mathbb{F}_q^\times$ acting by $(\lambda,\mu)\cdot(x,y)=(\mu\lambda^{-1}x,\ \mu\lambda^{-1}y)$, i.e. through the single scalar $t=\mu\lambda^{-1}\in\mathbb{F}_q^\times$. The zero representation $(0,0)$ decomposes as $S_1\oplus S_2$; every nonzero $(x,y)$ is indecomposable, and absolutely so (its endomorphism ring is $\mathbb{F}_q$). Orbits of $\mathbb{F}_q^\times$ on $\mathbb{F}_q^2\setminus\{0\}$ are the points of $\mathbb{P}^1(\mathbb{F}_q)$:
$$A_{(1,1)}(q)=\\#\mathbb{P}^1(\mathbb{F}_q)=q+1 .$$
Checks: $\deg A=1=1-q(\alpha)=1-0$ ✓; coefficients $1,1\ge0$ so (K1) holds ✓; $A_{(1,1)}(0)=1=\operatorname{mult}_{\delta}\widehat{\mathfrak{sl}_2}$ ✓.

**Case $\alpha=(n,n)$, $n\ge2$.** Kronecker modules of dimension $(n,n)$ that are indecomposable are the *regular* ones $R_{x,m}$, indexed by a closed point $x\in\mathbb{P}^1_{\mathbb{F}_q}$ of degree $d$ and a multiplicity $m$ with $dm=n$. Absolute indecomposability forces $d=1$ (otherwise $R_{x,m}$ splits into $d$ conjugate summands over $\overline{\mathbb{F}_q}$), so $m=n$ and the count is again the number of rational points:
$$A_{(n,n)}(q)=q+1\quad\text{for all }n\ge1 .$$
Constant term $1=\operatorname{mult}_{n\delta}=1$ for every $n$ ✓, matching the fact that all imaginary roots of $\widehat{\mathfrak{sl}_2}$ have multiplicity $1$ ($=\operatorname{rank}$).

**Case $\alpha=(2,1)$.** Here $q(\alpha)=1$, a real root, so $\deg A_\alpha=0$ and $A_{(2,1)}(q)=1$: the unique indecomposable is $x=(1\ 0)$, $y=(0\ 1)$ acting $\mathbb{F}_q^2\to\mathbb{F}_q$, with $\operatorname{End}=\mathbb{F}_q$.

**Where the difficulty starts.** Replace the two arrows by three ($Q=K_3$, the $3$-Kronecker quiver). Then $q(\alpha)=\alpha_1^2+\alpha_2^2-3\alpha_1\alpha_2$, $\mathfrak{g}_Q$ is indefinite, and e.g. $q((1,1))=-1$ gives $\deg A_{(1,1)}=2$, with $A_{(1,1)}(q)=q^2+q+1=\\#\mathbb{P}^2(\mathbb{F}_q)$ — still transparently positive. But for $\alpha=(2,2)$, $q(\alpha)=-4$, $\deg A_{(2,2)}=5$, $\alpha$ is divisible, and no smooth $\mathcal{M}_\lambda(\alpha)$ exists: this is precisely the regime where Hua's formula gives the answer only through an alternating $\operatorname{Log}$, and where positivity needed the HLRV/Mozgovoy machinery rather than a point count.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*