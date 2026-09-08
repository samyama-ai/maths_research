---
id: 04-topology/khovanov-homotopy-type-properties
title: "Khovanov Homotopy Type Properties"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Khovanov Homotopy Type Properties

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/khovanov-homotopy-type-properties` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Lipshitz and Sarkar (2014) constructed, for each oriented link $L \subset S^3$, a family of spectra $\mathcal{X}^j(L)$ indexed by the quantum grading $j$, whose reduced cohomology recovers Khovanov homology:
$$\widetilde{H}^{i}\big(\mathcal{X}^j(L)\big) \;\cong\; Kh^{i,j}(L).$$
The stable homotopy type of $\mathcal{X}^j(L)$ is a link invariant. The problem is to determine **what this refinement actually knows**:

1. **Strictly stronger?** Is $\mathcal{X}(L)$ a strictly finer invariant than $Kh(L)$ — and how much finer? (Yes, strictly finer; the quantitative question is open.)
2. **Formality.** For which links is $\mathcal{X}^j(L)$ a wedge of Moore spectra (i.e. carries no information beyond $Kh$)?
3. **Geometric content.** Do the higher structures (Steenrod operations, Postnikov data, $\pi_*$-level products) give bounds on the slice genus, unknotting number, or ribbon/exotic phenomena that $Kh$ alone cannot?
4. **Identification.** Is $\mathcal{X}^j(L)$ the suspension spectrum of a space? Is it, as conjectured, related to the Seiberg–Witten Floer stable homotopy type of the branched double cover $\Sigma(L)$?
5. **Functoriality.** Is $L \mapsto \mathcal{X}(L)$ functorial for link cobordisms in $[0,1]\times S^3$ (and in more general 4-manifolds), up to sign or up to homotopy?

A complete resolution means: an intrinsic (diagram-free) characterization of $\mathcal{X}(L)$, a decision procedure for when it is formal, and a proof or disproof of the Floer-theoretic identification.

## 2. Mathematical Foundations

**Khovanov's cube.** Fix a diagram $D$ of $L$ with $n$ crossings, $n_+$ positive and $n_-$ negative. Each vertex $v \in \{0,1\}^n$ gives a complete resolution, a disjoint union of $|v|$-circles; apply the Frobenius algebra $A = \mathbb{Z}[X]/(X^2)$, $\deg 1 = 1$, $\deg X = -1$, with
$$m(1\otimes 1)=1,\; m(1\otimes X)=X,\; m(X\otimes X)=0, \qquad \Delta(1)=1\otimes X + X\otimes 1,\; \Delta(X)=X\otimes X.$$
Summing edge maps with signs gives $CKh^{*,*}(D)$ and $Kh^{i,j}(L)=H^{i,j}$ after the shift $[-n_-]\{n_+-2n_-\}$. The graded Euler characteristic is the Jones polynomial: $\sum_{i,j}(-1)^i q^j \dim Kh^{i,j} = (q+q^{-1})J(L)(q)$.

**Spatial refinement.** The Khovanov complex is realized as the cellular cochain complex of a CW spectrum via a *framed flow category* $\mathscr{C}_{Kh}^j(D)$: objects are generators $x$ with grading $|x|$, morphism spaces $\mathcal{M}(x,y)$ are $\langle$framed$\rangle$ manifolds with corners of dimension $|x|-|y|-1$, with
$$\partial \mathcal{M}(x,y) = \bigcup_{|x|>|z|>|y|} \mathcal{M}(x,z)\times \mathcal{M}(z,y).$$
Cohen–Jones–Segal machinery then produces a finite CW spectrum $\mathcal{X}^j(D)$ by a Pontryagin–Thom embedding into $\mathbb{R}^N$. Invariance under Reidemeister moves is proved by explicit stable equivalences.

**Burnside category model.** Lawson–Lipshitz–Sarkar reformulate the data as a strictly unitary lax $2$-functor
$$F : \underline{2}^n \longrightarrow \mathscr{B}\text{urn},$$
from the cube category to the Burnside $2$-category (objects: finite sets; $1$-morphisms: finite correspondences $X \leftarrow A \rightarrow Y$). Homotopy colimit of $F$ after realization gives $\mathcal{X}^j$, and this makes the construction computer-implementable and extendable to tangles (where the target is a category of spectral bimodules).

**Steenrod squares.** Over $\mathbb{F}_2$ one obtains operations
$$Sq^k : Kh^{i,j}(L;\mathbb{F}_2)\longrightarrow Kh^{i+k,j}(L;\mathbb{F}_2),$$
invariants of $L$. $Sq^1$ is the Bockstein of the integral lift (so determined by $Kh(L;\mathbb{Z})$), while $Sq^2$ is genuinely new: it is computed from the second-order structure of the flow category via framed cobordisms of $0$- and $1$-dimensional moduli spaces.

**Refined $s$-invariant.** Rasmussen's $s(K)$ comes from the Lee deformation and satisfies $|s(K)| \le 2g_4(K)$. Lipshitz–Sarkar define $s_{Sq^i}(K)$ using the $Sq^i$-action on the Khovanov spectrum, with
$$|s_{Sq^i}(K)| \le 2 g_4(K), \qquad s_{Sq^i}(K) \in \{s(K)-2,\, s(K),\, s(K)+2\}\ \text{(up to normalization)}.$$

## 3. History & State of the Art (SOTA)

- **2000.** Khovanov categorifies the Jones polynomial (Duke Math. J.).
- **2006–2010.** Rasmussen's $s$ gives a combinatorial proof of the Milnor conjecture; the question "is $Kh$ the homology of a natural space/spectrum?" becomes explicit, motivated by Cohen–Jones–Segal's program for Floer homotopy types (1995).
- **2011–2014.** Lipshitz–Sarkar build $\mathcal{X}^j(L)$ (JAMS 2014), compute $Sq^2$ combinatorially (J. Topology 2014), and use it to refine $s$ (Duke 2014). Hu–Kriz–Kriz give an independent construction via cube diagrams and a Real/cobordism-theoretic model.
- **2012.** Seed computes $Sq^2$ for tabulated knots and finds pairs with isomorphic Khovanov homology (all gradings, integrally) but non-isomorphic Khovanov spectra — proving $\mathcal{X}$ is *strictly stronger* than $Kh$.
- **2015–2022.** Lawson–Lipshitz–Sarkar: Burnside-category formulation, products (the spectrum-level analogue of the $Kh$ module structure), and Khovanov spectra for tangles with a gluing theorem.
- **2017–2020.** Extensions: colored links (Lobb–Orson–Schütz), $\mathfrak{sl}_n$ matched diagrams (Jones–Lobb–Schütz), odd Khovanov homotopy type (Sarkar–Scaduto–Stoffregen).
- **2020–2024.** Equivariant methods: Lipshitz–Sarkar and Stoffregen–Zhang prove Smith-type inequalities for periodic links using the $\mathbb{Z}/p$-equivariant structure — the first *geometric* applications where no purely homological proof is known.

## 4. Partial Results / Verified Cases

- **Existence and invariance:** proven for all links, all quantum gradings $j$, over $\mathbb{Z}$ (Lipshitz–Sarkar 2014).
- **Strict refinement:** $Sq^2 \neq 0$ for the torus knots $T(3,4)=8_{19}$ and $T(3,5)=10_{124}$, and for infinitely many links obtained from them by disjoint union/connected sum. Seed's computations over knots up to 14 crossings (and links) exhibit pairs with equal $Kh$ but different $Sq^2$.
- **Formality (trivial cases):** for any diagram with $\le 3$ crossings, and for all links whose Khovanov homology is "thin" (alternating and quasi-alternating links), $\mathcal{X}^j(L)$ is a wedge of Moore spectra — $Sq^2$ vanishes for grading reasons since $Kh$ is supported on two diagonals $j-2i \in \{s\pm 1\}$ and $Sq^2$ shifts $i$ by $2$ at fixed $j$.
- **Refined slice bounds:** $s_{Sq^2}$ is strictly stronger than $s$ for explicit families, e.g. certain $(3,q)$-cables and knots built from $T(3,4)$; Lipshitz–Sarkar exhibit knots where $s_{Sq^2}$ improves the slice-genus bound by $2$.
- **Localization:** for $p$-periodic links, $\dim_{\mathbb{F}_p} Kh(L) \ge \dim_{\mathbb{F}_p} Kh(L/(\mathbb{Z}/p))$-type Smith inequalities hold (Lipshitz–Sarkar 2020; Stoffregen–Zhang 2024), proved via the equivariant spectrum, not via the chain complex.
- **Tangles:** the invariant extends to a spectral-bimodule-valued invariant of tangles with a gluing/derived tensor formula (Lawson–Lipshitz–Sarkar 2022).
- **Functoriality:** cobordism maps exist at the spectrum level for elementary cobordisms; well-definedness up to homotopy and sign is known in restricted settings, not in general.

## 5. Principal Obstacles

- **The construction is diagrammatic, not intrinsic.** $\mathcal{X}^j$ is built from a specific projection; invariance is proved by checking Reidemeister moves. There is no known space/moduli problem whose homotopy type is $\mathcal{X}^j(L)$ *a priori*, so structural questions ("is it a suspension spectrum?") have no leverage.
- **Combinatorial explosion.** The flow category has $O(2^n)$ objects; embedding it to produce a CW structure needs an ambient $\mathbb{R}^N$ with $N$ growing rapidly. Direct computation beyond ~15 crossings is infeasible, so empirical exploration of higher operations is thin.
- **Only second-order data is accessible.** $Sq^2$ requires understanding $0$- and $1$-dimensional moduli spaces. $Sq^4$, $Sq^8$, and general Postnikov/$k$-invariant data require framed $3$-manifolds with corners and their framings; no combinatorial formula is known. Consequently "is $\mathcal{X}$ formal?" cannot even be tested past $Sq^2$ for most links.
- **Thinness kills the invariant.** For the large classes where knot theory is best understood (alternating, quasi-alternating), the homotopy type is forced to be formal by grading support — the refinement is invisible exactly where computation is easy, and hardest where it might matter.
- **No 4-dimensional TQFT.** Functoriality obstructions (sign ambiguity in Khovanov's cobordism maps, resolved homologically by Sano/Beliakova et al.) become homotopy-coherence problems at the spectrum level: one needs coherent higher homotopies, not just chain maps up to sign.
- **Gauge theory bridge is absent.** The conjectural relation to $SWF(\Sigma(L))$ has no map in either direction; the Ozsváth–Szabó spectral sequence $Kh(\overline{L}) \Rightarrow \widehat{HF}(\Sigma(L))$ is not known to be induced by any spectrum-level map.

## 6. The Gap

Proven: $\mathcal{X}(L)$ exists, is invariant, and $Sq^2$ separates links that $Kh$ does not. Open: everything about the invariant *beyond* $Sq^2$.

The precise barrier is the passage from **first-order framed data** (moduli spaces of dimension $\le 1$, which admit a finite combinatorial description via the Burnside functor $F:\underline{2}^n \to \mathscr{B}\mathrm{urn}$) to **higher coherence data** (the full $\infty$-functor, equivalently all $k$-invariants of $\mathcal{X}^j$). Concretely: give an algorithm computing $Sq^4$, or a criterion for formality of $\mathcal{X}^j(L)$ in terms of the diagram, or a natural map $\mathcal{X}^j(L) \to \Sigma^m SWF(\Sigma(L))$ realizing the Ozsváth–Szabó spectral sequence. Crossing any one of these would convert the refinement from a computable-in-principle gadget into a structural tool.

## 7. Current Research (as of June 2026)

- **Oregon / Princeton (Lipshitz, Sarkar) and collaborators:** spectrum-level products and module structures, equivariant refinements, and applications of $s_{Sq^i}$ to 4-dimensional questions.
- **Equivariant and localization school (Stoffregen, Zhang, Sarkar–Scaduto–Stoffregen):** Smith inequalities, odd Khovanov homotopy, and $\mathbb{Z}/2$-equivariant refinements of $s$.
- **Durham (Lobb, Schütz, Jones):** $\mathfrak{sl}_n$ and colored refinements, plus fast computational tools (`KnotJob`) that extend $Sq^2$ tables.
- **Skein lasagna frontier:** Ren–Willis (2024) computed Khovanov skein lasagna modules and used them to detect exotic $\mathbb{R}^4$-like phenomena and distinguish exotic pairs of $4$-manifolds *(frontier — verify)*; whether a homotopy-type-level lasagna invariant exists and is stronger is actively pursued *(frontier — verify)*.
- **Floer-homotopy comparison:** the conjectural identification with $SWF(\Sigma(L))$ remains the organizing conjecture; partial evidence exists in low crossing number and for connected sums *(frontier — verify)*.

## 8. Future Work

- Find an intrinsic model: realize $\mathcal{X}^j(L)$ as a homotopy colimit over a category built from the link, not the diagram (e.g. via a spectral Bar-Natan cobordism category).
- Produce a computable formula for $Sq^4$ / the first nontrivial $k$-invariant; even a single example with $Sq^2=0$ but $Sq^4\ne 0$ would show the invariant has depth beyond current reach.
- Establish full cobordism functoriality at the spectrum level, then define $\mathcal{X}$-valued invariants of surfaces in $B^4$ and 4-manifolds.
- Extend the tangle theory (LLS) to a genuine $(\infty,2)$-categorical local TQFT; this would make computation local and break the $2^n$ barrier.
- Construct the comparison map to Seiberg–Witten Floer spectra and deduce new spectral sequences.
- Systematically test the conjecture "*$\mathcal{X}^j$ is formal iff $Kh$ is thin*" — currently consistent with data, but with no proof in either direction.

## 9. Key References

- **[Foundational]** M. Khovanov. *A categorification of the Jones polynomial.* Duke Mathematical Journal 101 (2000), 359–426. [DOI](https://doi.org/10.1215/s0012-7094-00-10131-7)
- **[Foundational]** R. L. Cohen, J. D. S. Jones, G. B. Segal. *Floer's infinite-dimensional Morse theory and homotopy theory.* In "The Floer Memorial Volume", Birkhäuser, 1995. [DOI](https://doi.org/10.1007/978-3-0348-9217-9_13)
- **[Foundational]** R. Lipshitz, S. Sarkar. *A Khovanov stable homotopy type.* Journal of the American Mathematical Society 27 (2014), 983–1042. [DOI](https://doi.org/10.1090/s0894-0347-2014-00785-2)
- **[Foundational]** R. Lipshitz, S. Sarkar. *A Steenrod square on Khovanov homology.* Journal of Topology 7 (2014), 817–848. [DOI](https://doi.org/10.1112/jtopol/jtu005)
- **[SOTA]** R. Lipshitz, S. Sarkar. *A refinement of Rasmussen's s-invariant.* Duke Mathematical Journal 163 (2014), 923–952.
- **[SOTA]** T. Lawson, R. Lipshitz, S. Sarkar. *Khovanov homotopy type, Burnside category, and products.* arXiv:1505.00213, 2015.
- **[SOTA]** T. Lawson, R. Lipshitz, S. Sarkar. *Khovanov spectra for tangles.* Journal of Topology 15 (2022), 1054–1131. [DOI](https://doi.org/10.1017/s147474802100044x)
- **[SOTA]** S. Sarkar, C. Scaduto, M. Stoffregen. *An odd Khovanov homotopy type.* Advances in Mathematics 367 (2020), 107112. [DOI](https://doi.org/10.1016/j.aim.2020.107112)
- **[SOTA]** R. Lipshitz, S. Sarkar. *Khovanov homotopy type, periodic links and localizations.* Mathematische Annalen 377 (2020), 459–503. [DOI](https://doi.org/10.1007/s00208-021-02157-y)
- **[SOTA]** M. Stoffregen, M. Zhang. *Localization in Khovanov homology.* Geometry & Topology 28 (2024). [DOI](https://doi.org/10.2140/gt.2024.28.1501)
- **[Computational]** C. Seed. *Computations of the Lipshitz–Sarkar Steenrod square on Khovanov homology.* arXiv:1210.1882, 2012.
- **[Related]** P. Hu, D. Kriz, I. Kriz. *Field theories, stable homotopy theory, and Khovanov homology.* Topology Proceedings 48 (2016), 327–360.
- **[Related]** D. Jones, A. Lobb, D. Schütz. *An $\mathfrak{sl}_n$ stable homotopy type for matched diagrams.* Advances in Mathematics 356 (2019), 106816.
- **[Related]** A. Lobb, P. Orson, D. Schütz. *A Khovanov stable homotopy type for colored links.* Algebraic & Geometric Topology 17 (2017), 1261–1281. [DOI](https://doi.org/10.2140/agt.2017.17.1261)
- **[Related]** J. Rasmussen. *Khovanov homology and the slice genus.* Inventiones Mathematicae 182 (2010), 419–447. [DOI](https://doi.org/10.1007/s00222-010-0275-6)
- **[Survey]** R. Lipshitz, S. Sarkar. *Spatial refinements and Khovanov homology.* Proceedings of the ICM 2018, Rio de Janeiro, Vol. II, 1153–1173. [DOI](https://doi.org/10.1142/9789813272880_0091)

## 10. Worked Example / Concrete Special Case

**Unknot and Hopf link (formal cases).** For the $0$-crossing unknot diagram, $CKh$ has one circle, so $A = \mathbb{Z}\{1, X\}$ splits by quantum grading: $\mathcal{X}^{1}(U)=\mathcal{X}^{-1}(U)=\mathbb{S}^0$ and $\mathcal{X}^j = *$ otherwise. All Steenrod operations vanish.

For the positive Hopf link $H$ ($n=2$, $n_+=2$), $Kh(H)$ is free of rank $4$, concentrated in $(i,j) \in \{(0,0),(0,2),(2,4),(2,6)\}$. Each $\mathcal{X}^j(H)$ has cohomology $\mathbb{Z}$ in a single degree, so each is a sphere spectrum $\mathbb{S}^{i}$ (up to shift). No higher structure: $H$ is alternating, hence thin, hence formal. This is why $Sq^2$ cannot see it: $Sq^2$ maps $Kh^{i,j}\to Kh^{i+2,j}$ at **fixed** $j$, and thin homology has at most one nonzero group in each $j$-column per diagonal.

**$T(3,4)=8_{19}$ (non-formal).** Its Khovanov homology over $\mathbb{F}_2$ has, in quantum grading $j=13$, nonzero groups in homological gradings $i=3$ and $i=5$:
$$Kh^{3,13}(8_{19};\mathbb{F}_2)\cong \mathbb{F}_2, \qquad Kh^{5,13}(8_{19};\mathbb{F}_2)\cong \mathbb{F}_2 .$$
Lipshitz–Sarkar's computation gives
$$Sq^2 : Kh^{3,13}(8_{19};\mathbb{F}_2) \xrightarrow{\ \cong\ } Kh^{5,13}(8_{19};\mathbb{F}_2),$$
non-zero. Hence $\mathcal{X}^{13}(8_{19})$ is **not** a wedge of Moore spectra: the two cells are attached by a map of Hopf-invariant-one type, so the relevant subquotient is stably $\Sigma^{3}\mathbb{CP}^2$ rather than $\mathbb{S}^3 \vee \mathbb{S}^5$.

**How this is computed.** In the Burnside model, one takes the two generators $x \in \{0,1\}^8$-vertices contributing to $(3,13)$ and $y$ contributing to $(5,13)$. The moduli space $\mathcal{M}(x,y)$ is a framed $1$-manifold: a disjoint union of circles and intervals assembled from the ladybug matching on $2$-dimensional faces of the cube where a $1$-resolution splits a circle into two. Each closed circle carries a framing in $\pi_1(O) = \mathbb{Z}/2$; $Sq^2\langle x^\vee \rangle = \sum_y \langle \text{framing obstruction of } \mathcal{M}(x,y)\rangle\, y^\vee$. For $8_{19}$ the total obstruction is $1 \in \mathbb{F}_2$.

**Consequence.** Because $Sq^2 \ne 0$, the refined invariant $s_{Sq^2}$ is defined and, for suitable satellites/cables of $8_{19}$, yields $|s_{Sq^2}| = |s| + 2$, improving the slice-genus bound $|s| \le 2g_4$ by one unit of genus — a bound no purely homological Khovanov computation supplies. Extending this from $Sq^2$ to the full homotopy type is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*