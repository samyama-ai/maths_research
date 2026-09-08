---
id: 08-logic-set-theory/definable-maximal-almost-disjoint-families
title: "Definability of Maximal Almost Disjoint Families"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Definability of Maximal Almost Disjoint Families

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/definable-maximal-almost-disjoint-families` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A family $\mathcal{A} \subseteq [\omega]^{\omega}$ is *almost disjoint* (a.d.) if $|A \cap B| < \omega$ for all distinct $A, B \in \mathcal{A}$, and *maximal* (MAD) if it is infinite and no $X \in [\omega]^{\omega}$ is almost disjoint from every member. ZFC proves MAD families exist (Zorn), but every such proof uses the axiom of choice in an essential way.

**The problem.** Determine exactly how definable an infinite MAD family can be, and which regularity hypotheses rule MAD families out entirely. Concretely:

1. **(Mathias's measurability question — open.)** Does $\mathsf{ZF} + \mathsf{DC} +$ "every set of reals is Lebesgue measurable" imply there are no infinite MAD families? Same question for the Baire property.
2. **(Projective calibration — partially solved.)** $\Sigma^1_1$ MAD families are impossible in ZFC; $\Pi^1_1$ ones exist in $L$. Is "there is a $\Sigma^1_2$ MAD family" compatible with $\omega_1^{L[x]} < \omega_1$ for every real $x$, i.e. must a projectively definable MAD family come from a canonical inner model?
3. **(Higher levels.)** Is it consistent with large cardinals that some $\Sigma^1_n$ MAD family exists while all $\Sigma^1_n$ sets are Lebesgue measurable?

A full solution to (1) is a ZF+DC proof that measurability kills maximality, or a model of ZF+DC with all sets measurable containing a MAD family. A solution to (2) is a forcing construction over a model with no reals coding $\omega_1$, or a theorem that $\Sigma^1_2$-definable maximality implies $\omega_1 = \omega_1^{L[x]}$.

## 2. Mathematical Foundations

Work in the Polish space $\mathcal{P}(\omega) \cong 2^{\omega}$ with the product topology; $[\omega]^{\omega}$ is the $G_\delta$ set of infinite subsets. Write $A \subseteq^* B$ for $|A \setminus B| < \omega$ and $A \perp B$ for $|A\cap B| < \omega$.

$$\mathcal{A} \text{ is MAD} \iff \mathcal{A}\subseteq[\omega]^\omega \text{ infinite},\ \forall A\neq B\in\mathcal A\ (A\perp B),\ \text{and}\ \forall X\in[\omega]^{\omega}\,\exists A\in\mathcal{A}\ |X\cap A|=\omega .$$

The associated cardinal characteristic is
$$\mathfrak{a} \;=\; \min\{\,|\mathcal{A}| : \mathcal{A}\ \text{is a MAD family}\,\},\qquad \aleph_1 \le \mathfrak{b}\le\mathfrak{a}\le\mathfrak{c}.$$
The inequality $\mathfrak{a}\ge\aleph_1$ is the elementary fact that no countable infinite a.d. family is maximal (Section 10); $\mathfrak b\le\mathfrak a$ is a theorem of Solomon.

**Projective hierarchy.** $\Sigma^1_1$ = analytic, $\Pi^1_1$ = co-analytic, $\Sigma^1_{n+1} = \exists^{\mathbb{R}}\Pi^1_n$. "$\mathcal A$ is $\Gamma$" means $\mathcal A\subseteq 2^\omega$ belongs to the pointclass $\Gamma$.

**Mathias's machinery.** A *happy family* (selective coideal) is $\mathcal{H}\subseteq[\omega]^{\omega}$, closed under $\supseteq^*$ and finite intersections modulo the ideal, such that every decreasing sequence $H_0\supseteq H_1\supseteq\cdots$ in $\mathcal{H}$ has a *diagonalization* $H\in\mathcal H$ with $H\setminus\{0,\dots,n\}\subseteq H_n$. For $\mathcal A$ a.d., put
$$\mathcal{I}(\mathcal{A})=\{X\subseteq\omega : X\subseteq^* A_1\cup\dots\cup A_k \text{ for some } A_i\in\mathcal{A}\},\qquad \mathcal{H}(\mathcal A)=[\omega]^\omega\setminus\mathcal I(\mathcal A).$$
$\mathcal A$ is MAD exactly when $\mathcal I(\mathcal A)^+ = \mathcal H(\mathcal A)$ contains no set a.d. from all of $\mathcal A$; the key lemma is that if $\mathcal{H}(\mathcal{A})$ is happy and *Ramsey* (every $\mathcal H$-positive set has a homogeneous $\mathcal H$-positive subset for any partition of $[\omega]^2$), then $\mathcal{A}$ is not maximal.

**Mathias–Prikry forcing.** $\mathbb{M}_{\mathcal H}$ consists of pairs $(s,H)$, $s\in[\omega]^{<\omega}$, $H\in\mathcal H$, $\max s<\min H$, ordered by $(t,K)\le(s,H)$ iff $s\sqsubseteq t$, $K\subseteq H$, $t\setminus s\subseteq H$. Mathias's theorem: for happy $\mathcal{H}$, $\mathbb M_{\mathcal H}$ has the *pure decision* and *Prikry* properties, and the generic real diagonalizes $\mathcal H$. This is the engine behind every non-existence result below.

## 3. History & State of the Art (SOTA)

- **1977 — Mathias.** In *Happy families*, A. R. D. Mathias proves there is **no analytic MAD family**, and that in the Solovay-style model $L(\mathbb{R})$ obtained from a Mahlo cardinal there are none at all. The proof runs through happy families and the Ramsey property.
- **1989 — Miller.** A. Miller shows $V=L$ yields a $\Pi^1_1$ MAD family (indeed a $\Pi^1_1$ maximal object for many combinatorial maximality notions), via a $\Sigma_1$-over-$L_{\omega_1}$ "fast" transfinite construction. Combined with Mathias this pins the exact boundary at $\Pi^1_1$.
- **2013 — Törnquist.** There is a $\Sigma^1_2$ MAD family **iff** there is a $\Pi^1_1$ MAD family. So the hierarchy collapses at level 2.
- **2013 — Brendle–Khomskii.** A $\Pi^1_1$ MAD family is consistent with $\mathfrak{b} = \mathfrak c = \aleph_2$: definability of a MAD family does not force the continuum's combinatorics to be $L$-like.
- **2017 — Fischer–Schrittesser–Törnquist.** Under $V=L$ there is a Cohen-indestructible $\Pi^1_1$ MAD family, hence a model with a $\Pi^1_1$ MAD family and $\mathfrak{a}=\aleph_1<\mathfrak{c}$.
- **2018 — Törnquist.** A short, forcing-free proof that no MAD family is analytic; also that no MAD family is "$\sigma$-compactly generated".
- **2018 — Neeman–Norwood.** Under $\mathsf{AD}^+$ (in particular in $L(\mathbb R)$ below suitable large cardinals) there are **no** infinite MAD families; so under PD no MAD family is projective.
- **2019 — Schrittesser–Törnquist.** $\mathsf{ZF}+\mathsf{DC}+$ "all sets of reals are Ramsey" $\Rightarrow$ no infinite MAD families. This answers the Ramsey-property case of Mathias's question.
- **2022 — Bakke Haga–Schrittesser–Törnquist.** A general "$\mathbb{P}$-measurability" framework: for strongly arboreal forcings (Sacks, Miller, Silver, …), universal measurability implies no MAD families; in particular there are none in Solovay's model, without a Mahlo cardinal.

## 4. Partial Results / Verified Cases

| Setting | Verdict on MAD families |
|---|---|
| Countable a.d. families | Never maximal (ZF, elementary) |
| Closed, $K_\sigma$, Borel, analytic ($\Sigma^1_1$) | Never maximal (Mathias 1977; Törnquist 2018) |
| $\Pi^1_1$, in $L$ | Exist (Miller 1989) |
| $\Sigma^1_2$ | Exists iff a $\Pi^1_1$ one does (Törnquist 2013) |
| $\Pi^1_1$ + $\mathfrak b>\aleph_1$ | Consistent, $\mathfrak b=\mathfrak c=\aleph_2$ (Brendle–Khomskii 2013) |
| $\Pi^1_1$ + $\mathfrak a=\aleph_1<\mathfrak c=\aleph_2$ | Consistent, Cohen model (Fischer–Schrittesser–Törnquist 2017) |
| All sets Ramsey ($\mathsf{ZF}+\mathsf{DC}$) | None (Schrittesser–Törnquist 2019) |
| Solovay's model; all sets Sacks/Miller measurable | None (Bakke Haga–Schrittesser–Törnquist 2022) |
| $\mathsf{AD}^+$, $L(\mathbb{R})$; PD + projective sets | None (Neeman–Norwood 2018) |

Contrast with neighbouring maximality notions: Horowitz and Shelah constructed in ZFC a **Borel** maximal eventually different family of functions and a **Borel** maximal cofinitary group — so the "no definable maximal object" phenomenon is specific to almost disjointness, not generic to combinatorial maximality.

## 5. Principal Obstacles

- **Ramsey vs. measure.** Every non-existence proof factors through a Ramsey-type diagonalization: one builds a Mathias real for $\mathcal H(\mathcal A)$ that is a.d. from all of $\mathcal A$. Lebesgue measurability and the Baire property give *no* infinite-dimensional pigeonhole; the ideal $\mathcal I(\mathcal A)$ can be null and meagre-positive simultaneously, so "all sets measurable" has no known handle on $\mathcal H(\mathcal A)$. This is the exact reason question (1) is still open after fifty years.
- **Happiness is not free.** For an arbitrary a.d. $\mathcal{A}$, $\mathcal H(\mathcal A)$ is a coideal but need not be selective; selectivity is obtained from definability plus a regularity axiom. Without one, $\mathbb M_{\mathcal H}$ loses pure decision.
- **$L$-constructions are too rigid, and too flexible.** Miller-type $\Pi^1_1$ constructions need a $\Sigma_1$-definable well-order of the reals — they run in $L$ and in "$\Sigma^1_2$-good" models where $\omega_1=\omega_1^{L[x]}$. No technique produces a projective MAD family when $\omega_1$ is inaccessible to reals; conversely no absoluteness argument shows this is impossible, because $\Sigma^1_2$ maximality statements are $\Pi^1_2$ overall and not decided by Shoenfield absoluteness.
- **Indestructibility engineering.** Getting a definable MAD family to survive an iteration requires the family to be *indestructible* by the iterand; each forcing (Cohen, Sacks, Miller) needs a bespoke preservation lemma coupled to the coding, and no uniform template exists.

## 6. The Gap

Proven: $\Sigma^1_1 \Rightarrow$ not MAD; $\Pi^1_1$ MAD consistent; Ramsey/Sacks-measurability of *all* sets $\Rightarrow$ no MAD. The gap is two-fold.

- **Regularity gap.** Between "all sets Ramsey" and "all sets Lebesgue measurable". The Ramsey property is exactly the hypothesis matched to Mathias forcing; measure corresponds to random forcing, which adds no dominating or diagonalizing real. One must either extract a diagonalizing real from a measure-theoretic hypothesis (no known mechanism), or force $\mathsf{ZF}+\mathsf{DC}+$"all measurable" with a MAD family — which requires a symmetric-extension technique that preserves maximality through the random algebra.
- **Definability gap.** Between $\Pi^1_1$-in-$L$ and $\Pi^1_1$-in-general. Every known projective MAD family lives in a model where reals code $\omega_1$. The missing step: decide whether $\exists\,\Sigma^1_2$ MAD family $\Rightarrow \exists x\,(\omega_1^{L[x]}=\omega_1)$.

## 7. Current Research (as of June 2026)

- **Copenhagen / Vienna axis** (Törnquist, Schrittesser, Fischer and collaborators): pushing the $\mathbb{P}$-measurability framework of the 2022 *Journal of Mathematical Logic* paper to Laver- and random-style ideals, and to maximal discrete sets in definable graphs and hypergraphs. Random-measurability remains the stubborn case. *(frontier — verify)*
- **Definable indestructible families:** Sacks-indestructible co-analytic maximal eventually different families and cofinitary groups (Fischer–Schrittesser and successors), aiming at models where $\mathfrak a$ is small and witnessed projectively while other characteristics are large.
- **Higher analogues:** MAD families on uncountable $\kappa$ and the generalized Baire space $\kappa^{\kappa}$, where the Mathias-forcing argument has no direct counterpart and $\Sigma^1_1(\kappa)$ MAD families can exist. *(frontier — verify)*
- **Descriptive-graph-combinatorics transfer:** viewing MAD families as maximal independent sets in a definable hypergraph, importing the Kechris–Solecki–Todorcevic dichotomy toolkit.

## 8. Future Work

1. Settle Mathias's question for the Baire property first: the Baire property already gives a Cohen-real diagonalization scheme, and a positive answer there is widely expected before the measure case.
2. Isolate the weakest ideal-measurability hypothesis $\Phi$ with $\Phi \Rightarrow$ "$\mathcal H(\mathcal A)$ is selective for a.d. $\mathcal A$"; the 2022 framework suggests this can be made a clean dichotomy.
3. Determine whether $\Delta^1_2$ MAD families can exist when $\omega_1$ is inaccessible to reals — a targeted attack on the definability gap.
4. Explain the Horowitz–Shelah asymmetry: give a structural invariant of a maximality notion that predicts whether Borel witnesses exist.

## 9. Key References

- **[Foundational]** A. R. D. Mathias. *Happy families.* Annals of Mathematical Logic **12** (1977), 59–111.
- **[Foundational]** A. W. Miller. *Infinite combinatorics and definability.* Annals of Pure and Applied Logic **41** (1989), 179–203.
- **[SOTA]** A. Törnquist. *$\Sigma^1_2$ and $\Pi^1_1$ mad families.* Archive for Mathematical Logic **52** (2013), 209–219.
- **[SOTA]** J. Brendle, Y. Khomskii. *Mad families constructed from perfect almost disjoint families.* Journal of Symbolic Logic **78** (2013), 1164–1180.
- **[SOTA]** V. Fischer, D. Schrittesser, A. Törnquist. *A co-analytic Cohen-indestructible maximal almost disjoint family.* Journal of Symbolic Logic **82** (2017), 861–871.
- **[SOTA]** A. Törnquist. *Definability and almost disjoint families.* Advances in Mathematics **330** (2018), 61–73.
- **[SOTA]** I. Neeman, Z. Norwood. *Happy and mad families in $L(\mathbb{R})$.* Journal of Symbolic Logic **83** (2018), 572–597.
- **[SOTA / Recent]** D. Schrittesser, A. Törnquist. *The Ramsey property implies no mad families.* Proceedings of the National Academy of Sciences **116** (2019), 18883–18887.
- **[SOTA / Recent]** K. Bakke Haga, D. Schrittesser, A. Törnquist. *Maximal almost disjoint families, determinacy, and forcing.* Journal of Mathematical Logic **22** (2022), no. 1.
- **[Related]** H. Horowitz, S. Shelah. *A Borel maximal eventually different family.* arXiv preprint, 2016.
- **[Related]** Z. Vidnyánszky. *Transfinite inductions producing coanalytic sets.* Fundamenta Mathematicae **224** (2014), 155–174.
- **[Survey]** A. Blass. *Combinatorial cardinal characteristics of the continuum.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 2010, 395–489.

## 10. Worked Example / Concrete Special Case

**(a) No countable a.d. family is maximal — an explicit diagonal.** Let $\mathcal A=\{A_0,A_1,\dots\}$ be infinite and a.d. Build $b_0<b_1<\cdots$ recursively:
$$b_n \in A_n \setminus \Big( (A_0\cup\cdots\cup A_{n-1}) \cup \{0,1,\dots,b_{n-1}\} \Big).$$
The set removed is finite: $A_n\cap A_i$ is finite for each $i<n$, so $A_n\setminus\bigcup_{i<n}A_i$ is infinite. Put $B=\{b_n:n\in\omega\}$. Then $B$ is infinite, and for each $k$, $n>k \Rightarrow b_n\notin A_k$, so
$$B\cap A_k \subseteq \{b_0,\dots,b_k\},\qquad |B\cap A_k|\le k+1<\omega .$$
So $B\perp A$ for every $A\in\mathcal A$: $\mathcal A$ is not maximal. Hence $\mathfrak{a}\ge\aleph_1$, and every MAD family is uncountable — the first, and easiest, instance of "definable $\Rightarrow$ not maximal", since a countable family is $\Sigma^0_2$.

**(b) A perfect, compact a.d. family that is not maximal.** Identify $\omega$ with $2^{<\omega}$. For $x\in 2^{\omega}$ set
$$b_x=\{x\restriction n : n\in\omega\}\subseteq 2^{<\omega}.$$
Each $b_x$ is infinite; for $x\neq y$ with $x\restriction m = y\restriction m$, $m$ least differing, $b_x\cap b_y=\{x\restriction n : n\le m\}$ has $m+1$ elements. So $\mathcal{B}=\{b_x : x\in2^\omega\}$ is a.d. of size $\mathfrak c$, and $x\mapsto b_x$ is a homeomorphism onto a compact perfect subset of $2^{2^{<\omega}}$: $\mathcal B$ is closed.

It is not maximal. Take the antichain $D=\{0^n 1 : n\in\omega\}$. Any $b_x$ is a chain under $\sqsubseteq$, so it contains at most one element of the antichain $D$:
$$|D\cap b_x|\le 1 \quad\text{for all } x\in2^{\omega}.$$
$D$ is infinite, so $\mathcal B\cup\{D\}$ is a strictly larger a.d. family.

**(c) What the theorems add.** Steps (a) and (b) are hands-on. Mathias's theorem says the same conclusion holds for *every* analytic a.d. family, but the witness $B$ is no longer explicit: one shows $\mathcal H(\mathcal A)$ is happy, forces with $\mathbb{M}_{\mathcal H(\mathcal A)}$, and uses analytic absoluteness to pull the diagonalizing real back into $V$. Miller's construction goes the other way: in $L$, enumerate the reals as $\langle x_\alpha:\alpha<\omega_1\rangle$ in the $\Sigma_1$-definable order and at stage $\alpha$ add a set killing $x_\alpha$ while coding the construction so that membership in the final family is $\Pi^1_1$. The two arguments meet exactly at the $\Sigma^1_1/\Pi^1_1$ line, and the open problems of Section 1 ask what happens on either side of it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*