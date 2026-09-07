---
id: 08-logic-set-theory/moore-boundary-problem
title: "Moore's Boundary Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Moore's Boundary Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/moore-boundary-problem` · **Status:** open

## 1. Problem Statement / Conjecture

"Moore's Boundary Problem" is the catalog name for the surviving open core of the **normal Moore space problem**: locating the exact *boundary* — in the lattice of set-theoretic hypotheses, and in consistency strength — at which normality forces metrizability in Moore spaces.

The original conjecture (F. B. Jones, 1937), the **Normal Moore Space Conjecture (NMSC)**:

> Every normal Moore space is metrizable.

NMSC is known to be independent of ZFC, so the *conjecture* itself is settled. What is open is the boundary:

**(B1) Consistency strength.** Determine $\mathrm{Con}$-strength of NMSC exactly. Known: $\mathrm{Con}(\text{strongly compact}) \Rightarrow \mathrm{Con}(\mathrm{NMSC}) \Rightarrow \mathrm{Con}(\text{measurable})$. The interval between "measurable" and "strongly compact" is unclosed.

**(B2) The cardinality boundary.** For which cardinals $\kappa$ is "every normal Moore space of cardinality $\le \kappa$ is metrizable" a theorem of ZFC, of ZFC + small hypotheses, or strictly large-cardinal-dependent? The boundary is known to sit at or below $2^{\aleph_0}$; its exact position is open.

**(B3) The axiom boundary.** Determine the consistency strength of the Product Measure Extension Axiom (PMEA), the standard sufficient hypothesis for NMSC.

A complete solution to (B1) is an equiconsistency: a large-cardinal property $\Phi$ with $\mathrm{Con}(\mathrm{ZFC}+\Phi) \leftrightarrow \mathrm{Con}(\mathrm{ZFC}+\mathrm{NMSC})$, proved by a forcing construction in one direction and a core-model / inner-model argument in the other.

## 2. Mathematical Foundations

**Development.** A *development* for a topological space $X$ is a sequence $\langle \mathcal{G}_n : n<\omega\rangle$ of open covers such that for every $x \in X$,
$$\{\,\mathrm{st}(x,\mathcal{G}_n) : n<\omega\,\}, \qquad \mathrm{st}(x,\mathcal{G}_n)=\bigcup\{\,G\in\mathcal{G}_n : x\in G\,\},$$
is a neighbourhood base at $x$. A **Moore space** is a regular $T_1$ space admitting a development (R. L. Moore, 1932).

**Separation.** $X$ is *normal* if disjoint closed sets are separated by disjoint open sets. $X$ is *collectionwise normal* (CWN) if every discrete family $\{F_\alpha\}_{\alpha<\kappa}$ of closed sets admits a pairwise disjoint open expansion $\{U_\alpha\}$ with $F_\alpha \subseteq U_\alpha$. *Collectionwise Hausdorff* (CWH) is the same with singletons.

**Bing–Heath metrization.** Bing (1951): a Moore space is metrizable iff it is collectionwise normal. Hence
$$\mathrm{NMSC} \iff \big(\text{normal Moore} \Rightarrow \mathrm{CWN}\big),$$
which converts a metrization question into a pure set-theoretic separation question about $\kappa$-many closed sets.

**Jones' cardinal-arithmetic lemma.** If $X$ is separable with a closed discrete subspace $D$, and $X$ is normal, then every $A\subseteq D$ is separated from $D\setminus A$; counting continuous-type traces on a countable dense set gives
$$2^{|D|} \le 2^{\aleph_0}.$$
Consequently $2^{\aleph_0} < 2^{\aleph_1}$ implies every separable normal Moore space is metrizable (Jones 1937).

**Q-sets.** $A \subseteq \mathbb{R}$ uncountable is a *Q-set* if every $B \subseteq A$ is a relative $F_\sigma$ in $A$. $\mathfrak{q}$ denotes the least cardinal $\kappa$ with no Q-set of size $\kappa$; $\mathrm{MA}+\neg\mathrm{CH}$ gives $\mathfrak{q}=\mathfrak{c}$, and CH gives $\mathfrak{q}=\aleph_1$ (no Q-sets).

**PMEA.** For every cardinal $\kappa$, the usual product measure $\mu$ on $2^{\kappa}$ extends to a $\mathfrak{c}$-additive measure defined on *all* subsets of $2^{\kappa}$. Kunen: a strongly compact cardinal yields a model of PMEA (add $\ge$ strongly-compact-many random reals).

**Nyikos' implication.** $\mathrm{PMEA} \Rightarrow$ every normal space of character $\le 2^{\aleph_0}$ is collectionwise normal; in particular $\mathrm{PMEA}\Rightarrow\mathrm{NMSC}$.

## 3. History & State of the Art (SOTA)

- **1932.** R. L. Moore axiomatizes developable spaces in *Foundations of Point Set Theory*; metrization of Moore spaces becomes the central problem of the Texas school.
- **1937.** F. B. Jones proves $2^{\aleph_0}<2^{\aleph_1}$ implies separable normal Moore spaces are metrizable, and conjectures NMSC outright.
- **1951.** Bing: CWN Moore $\Rightarrow$ metrizable; Bing's space $G$ gives a normal, non-metrizable *non-developable* space.
- **1964.** R. W. Heath: normal Moore $\Rightarrow$ metrizable iff CWN; Heath's tangent-disc subspaces link normality to Q-sets.
- **1960s–70s.** Silver, Tall: $\mathrm{MA}+\neg\mathrm{CH}$ gives Q-sets, hence a **separable normal non-metrizable Moore space** — NMSC is not a theorem of ZFC.
- **1974.** Fleissner: $V=L$ implies normal first-countable spaces are CWH; strong failures of NMSC follow from $\diamondsuit$-type principles.
- **1980.** Nyikos: PMEA $\Rightarrow$ NMSC — the "provisional solution", giving consistency modulo a strongly compact.
- **1982.** Fleissner: NMSC implies an inner model with a measurable cardinal. Large cardinals are *necessary*, not an artifact.
- **1984–1990.** Fleissner's Handbook chapter; Dow–Tall–Weiss give new consistency proofs, including from a supercompact via iterated forcing rather than measure extension.
- **2000s–2020s.** Tall's $\mathrm{PFA}(S)[S]$ programme and Dow–Tall work on locally compact normal spaces and normal manifolds keep the boundary questions technically active.

**SOTA summary:** upper bound strongly compact; lower bound "inner model with a measurable" (and, in refined forms, measurables of positive Mitchell order). No improvement to either endpoint has been verified.

## 4. Partial Results / Verified Cases

- **Separable Moore spaces.** Metrizability holds whenever $2^{\aleph_0}<2^{\aleph_1}$ (Jones). Fails under $\mathrm{MA}_{\aleph_1}$. Boundary here is *exactly* the cardinal arithmetic $2^{\aleph_0}$ vs. $2^{\aleph_1}$ combined with $\mathfrak{q}>\aleph_1$ — fully solved.
- **Locally compact case.** Under PMEA, and also under $\mathrm{MA}_{\omega_1}$-type hypotheses in Balogh's work, locally compact normal spaces are collectionwise normal; locally compact normal Moore spaces are metrizable.
- **Small cardinality.** Every normal Moore space of cardinality $<\mathfrak{q}$ (in particular $\le\aleph_1$ under CH-like hypotheses, and $\le\aleph_0$ always, where second countability is automatic) is metrizable. Cardinality $\le\aleph_1$ is the first non-trivial level.
- **Character bound.** PMEA settles all spaces of character $\le 2^{\aleph_0}$; every Moore space has character $\le\aleph_0$, so the difficulty is not character but the *width* $\kappa$ of the discrete family being separated.
- **$V=L$ side.** Under $V=L$, NMSC fails badly — Fleissner's constructions give normal non-metrizable Moore spaces, so the boundary genuinely lies above the constructible universe.
- **Consistency, both directions.** $\mathrm{Con}(\text{strongly compact})\Rightarrow\mathrm{Con}(\mathrm{NMSC})$ (Nyikos, Kunen; Dow–Tall–Weiss); $\mathrm{Con}(\mathrm{NMSC})\Rightarrow\mathrm{Con}(\text{measurable})$ (Fleissner).

## 5. Principal Obstacles

- **No inner-model theory at the strongly compact level.** Closing (B1) from below needs a core model $K$ for hypotheses near supercompactness. Core model induction currently reaches Woodin cardinals and a bit beyond; there is no $K$ for strong compactness, so the standard technique for converting a combinatorial failure into large-cardinal strength stops well short of the upper bound.
- **Measure-theoretic upper bound is rigid.** PMEA is proved only by random forcing over a strongly compact; the $\mathfrak{c}$-additivity of the extended measure on $\mathcal{P}(2^\kappa)$ for *all* $\kappa$ is exactly what a strongly compact ultrafilter supplies. No known forcing produces PMEA from anything weaker, and no known weakening of PMEA still implies NMSC.
- **Unboundedly many widths.** NMSC quantifies over Moore spaces of arbitrary cardinality; separation must be achieved simultaneously for discrete families of every size $\kappa$. Reflection arguments that work for $\kappa=\aleph_1$ (elementary submodels, $\mathrm{PFA}$) do not lift uniformly to arbitrary $\kappa$, and $\square_\kappa$-style principles at singulars obstruct them.
- **Forcing axioms cut the wrong way.** $\mathrm{MA}+\neg\mathrm{CH}$ and $\mathrm{PFA}$ produce Q-sets or related structures that *refute* NMSC at $\aleph_1$; the axioms mathematicians know best are counterexample-generators here, not proof tools.
- **CWH does not upgrade to CWN.** All the "cheap" hypotheses ($V=L$, $\diamondsuit$-fragments, PMEA at low character) control CWH. Bridging CWH $\to$ CWN in a normal Moore space needs a simultaneous open expansion of a discrete family of *closed sets*, which is not a pointwise selection problem and admits no known reduction to CWH.

## 6. The Gap

Proven (§4) is a two-sided but wide bracket:
$$\text{measurable} \;\;\le\;\; \mathrm{Con}\text{-}\mathrm{strength}(\mathrm{NMSC}) \;\;\le\;\; \text{strongly compact}.$$
The general statement (§1) demands a single point. The precise missing step is either:

1. **From above:** a forcing $\mathbb{P}$ over a model with a measurable (or a Woodin, or an $o(\kappa)=\kappa^{++}$ measurable) such that $V^{\mathbb{P}}\models$ every normal Moore space is CWN — i.e. an NMSC-model not routed through PMEA; or
2. **From below:** a core-model argument taking a failure of CWN-separation and producing an inner model with a strongly compact-strength hypothesis — blocked by the absence of $K$ there.

Sub-gap (B2): "normal Moore of size $\le\aleph_1$ metrizable" is known to be equiconsistent with ZFC alone, while "size $\le 2^{\aleph_0}$" already carries measurable strength. The exact cardinal $\lambda$ where measurable strength first appears is unlocated.

## 7. Current Research (as of June 2026)

- **Toronto / Charlotte (Tall, Dow).** Continued study of normality vs. paracompactness in locally compact spaces and of the $\mathrm{PFA}(S)[S]$ model, which combines $\mathrm{PFA}$-like reflection with coherent-Souslin-tree forcing and yields metrization theorems that $\mathrm{PFA}$ alone refutes. Whether $\mathrm{PFA}(S)[S]$ can be pushed to full NMSC-style separation at all widths is open *(frontier — verify)*.
- **Inner-model programme (Münster, UC Irvine, Jerusalem).** Core model induction beyond Woodin cardinals; any extension of $K$-theory toward strong compactness would immediately act on the lower bound *(frontier — verify)*.
- **Measure-extension axioms.** Renewed interest in weakenings of PMEA (measure extension for $2^{\kappa}$ with restricted $\kappa$, or $\aleph_1$-additive extensions) with an eye to reducing the strongly compact upper bound to a supercompact-free hypothesis *(frontier — verify)*.
- **Set-theoretic topology of manifolds.** Dow–Tall's consistency results on hereditarily normal manifolds of dimension $>1$ being metrizable use the same large-cardinal machinery and serve as a testbed for boundary-lowering techniques.

## 8. Future Work

- **Isolate a combinatorial principle** $\mathrm{P}$ with $\mathrm{PMEA}\Rightarrow\mathrm{P}\Rightarrow\mathrm{NMSC}$ and compute $\mathrm{Con}(\mathrm{P})$ directly; Nyikos and Fleissner both suggested this as the realistic route to lowering the upper bound.
- **Determine $\mathrm{Con}$-strength of PMEA in isolation.** It is not known whether PMEA is strictly weaker than a strongly compact.
- **Cardinality stratification.** Compute the strength of "$\mathrm{NMSC}_\lambda$: normal Moore spaces of size $\le\lambda$ are metrizable" for $\lambda=\aleph_2,\aleph_\omega,2^{\aleph_0}$; a strict hierarchy would decompose (B1).
- **Reflection at singulars.** Test whether Shelah-style singular-cardinal compactness gives CWN reflection for Moore spaces, avoiding measures altogether.
- **CWH $\to$ CWN transfer.** Find a structural hypothesis on Moore spaces (e.g. $\sigma$-discrete-like refinements of a development) under which the upgrade is a ZFC theorem.

## 9. Key References

- **[Foundational]** R. L. Moore. *Foundations of Point Set Theory.* AMS Colloquium Publications, Vol. 13, American Mathematical Society, 1932.
- **[Foundational]** F. B. Jones. *Concerning normal and completely normal spaces.* Bulletin of the American Mathematical Society **43** (1937), 671–677.
- **[Foundational]** R. H. Bing. *Metrization of topological spaces.* Canadian Journal of Mathematics **3** (1951), 175–186.
- **[Foundational]** R. W. Heath. *Screenability, pointwise paracompactness, and metrization of Moore spaces.* Canadian Journal of Mathematics **16** (1964), 763–770.
- **[Key]** W. G. Fleissner. *Normal Moore spaces in the constructible universe.* Proceedings of the American Mathematical Society **46** (1974), 294–298.
- **[Key]** P. J. Nyikos. *A provisional solution to the normal Moore space problem.* Proceedings of the American Mathematical Society **78** (1980), 429–435.
- **[Key]** W. G. Fleissner. *If all normal Moore spaces are metrizable, then there is an inner model with a measurable cardinal.* Transactions of the American Mathematical Society **273** (1982), 365–373.
- **[SOTA / Recent]** A. Dow, F. D. Tall, W. A. R. Weiss. *New proofs of the consistency of the normal Moore space conjecture, I and II.* Topology and its Applications **37** (1990), 33–51 and 115–129.
- **[Survey]** W. G. Fleissner. *The normal Moore space conjecture and large cardinals.* In: K. Kunen and J. E. Vaughan (eds.), *Handbook of Set-Theoretic Topology*, North-Holland, 1984, 733–760.
- **[Survey]** P. J. Nyikos. *A history of the normal Moore space problem.* In: C. E. Aull and R. Lowen (eds.), *Handbook of the History of General Topology*, Vol. 3, Kluwer, 2001, 1179–1212.
- **[Survey]** F. D. Tall. *Normality versus collectionwise normality.* In: *Handbook of Set-Theoretic Topology*, North-Holland, 1984, 685–732.

## 10. Worked Example / Concrete Special Case

**The Niemytzki (tangent disc) plane and the Q-set boundary.**

Let $\Gamma=\{(x,y)\in\mathbb{R}^2 : y>0\}$ with the Euclidean topology and $L=\mathbb{R}\times\{0\}$. For $A\subseteq\mathbb{R}$ put
$$X_A \;=\; \Gamma \cup (A\times\{0\}).$$
Topologize: points of $\Gamma$ keep Euclidean neighbourhoods; a basic neighbourhood of $p=(a,0)$ is $\{p\}\cup D_n(p)$, where $D_n(p)\subseteq\Gamma$ is the open disc of radius $1/n$ tangent to $L$ at $p$.

*Step 1 — $X_A$ is a Moore space.* Take $\mathcal{G}_n$ = all Euclidean balls in $\Gamma$ of radius $<1/n$ together with all $\{p\}\cup D_n(p)$ for $p\in A\times\{0\}$. Then $\mathrm{st}(p,\mathcal{G}_n)\subseteq \{p\}\cup D_{n/2}(p)$, so $\langle\mathcal{G}_n\rangle$ is a development. $X_A$ is regular and $T_1$.

*Step 2 — $A\times\{0\}$ is closed discrete.* Each $D_n(p)$ misses $L$, so $A\times\{0\}$ carries the discrete topology and is closed in $X_A$.

*Step 3 — normality $\Leftrightarrow$ Q-set.* If $B\subseteq A$, then $B\times\{0\}$ and $(A\setminus B)\times\{0\}$ are disjoint closed sets. Separating them by open sets amounts to choosing radii $f:B\to\omega$ and $g:A\setminus B\to\omega$ with the tangent discs disjoint. Decomposing $B=\bigcup_n f^{-1}(n)$ exhibits $B$ as a countable union of sets relatively closed in $A$. Hence $X_A$ normal $\iff$ every $B\subseteq A$ is a relative $F_\sigma$ in $A$ $\iff$ $A$ is a Q-set (Heath).

*Step 4 — metrizability.* $\Gamma\cap\mathbb{Q}^2$ is countable and dense, so $X_A$ is separable. A separable metrizable space is second countable, and second countable spaces have only countable closed discrete subsets. So $X_A$ metrizable $\iff$ $A$ is countable.

*Step 5 — the counting boundary.* Suppose $A$ is a Q-set with $|A|=\aleph_1$. Each $B\subseteq A$ is determined by an $F_\sigma$ subset of $\mathbb{R}$, and there are exactly $\mathfrak{c}^{\aleph_0}=2^{\aleph_0}$ such sets. Therefore
$$2^{\aleph_1}=|\mathcal{P}(A)| \le 2^{\aleph_0},$$
forcing $2^{\aleph_0}=2^{\aleph_1}$ — Jones' lemma, recovered by direct count.

*Conclusion.* Under $\mathrm{MA}+\neg\mathrm{CH}$ (so $2^{\aleph_0}=2^{\aleph_1}=\aleph_2$ and Q-sets of size $\aleph_1$ exist), $X_A$ is a **normal, non-metrizable Moore space**: NMSC fails. Under $2^{\aleph_0}<2^{\aleph_1}$ no such $X_A$ exists. This single family fixes the boundary completely in the *separable* case at $\aleph_1$ — and the open problem is precisely that no analogous count exists for non-separable Moore spaces with discrete families of arbitrary width, which is where the measurable-to-strongly-compact gap lives.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*