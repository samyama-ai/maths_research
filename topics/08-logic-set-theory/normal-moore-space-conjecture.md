---
id: 08-logic-set-theory/normal-moore-space-conjecture
title: "Normal Moore Space Conjecture"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Normal Moore Space Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/normal-moore-space-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Normal Moore Space Conjecture (NMSC).** Every normal Moore space is metrizable.

A *Moore space* is a regular $T_1$ space with a development (Section 2). The conjecture asks whether the separation axiom "normal" upgrades a development to a metric.

The conjecture is **not a theorem or a refutation of ZFC**: it is independent.

- $\mathrm{Con}(\mathrm{ZFC} + \text{strongly compact cardinal}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{NMSC})$ (Nyikos 1980, using Kunen's PMEA).
- $\mathrm{NMSC} \Rightarrow$ there is an inner model with a measurable cardinal (Fleissner 1982). In particular NMSC is not provable in ZFC, and its consistency is not provable from $\mathrm{Con}(\mathrm{ZFC})$.

What remains open is the **exact consistency strength**: is NMSC equiconsistent with a measurable cardinal, or does it require substantially more (up to a strongly compact)? A complete resolution means either (a) a model of NMSC built from a measurable (or from any hypothesis strictly below strong compactness), or (b) a proof that NMSC implies a large-cardinal hypothesis beyond a measurable, ideally matching the upper bound.

## 2. Mathematical Foundations

**Development.** A *development* for a topological space $X$ is a sequence $\langle \mathcal{G}_n : n \in \omega \rangle$ of open covers of $X$ such that for every $x \in X$ the collection
$$\{\, \mathrm{st}(x,\mathcal{G}_n) : n \in \omega \,\}, \qquad \mathrm{st}(x,\mathcal{G}_n) = \bigcup \{\, G \in \mathcal{G}_n : x \in G \,\},$$
is a neighbourhood base at $x$. A **Moore space** is a regular $T_1$ developable space. Every metric space is Moore (take $\mathcal{G}_n = \{ B(x,2^{-n}) : x \in X\}$).

**Normal.** Disjoint closed $A,B$ have disjoint open neighbourhoods. **Collectionwise normal (cwn).** Every discrete family $\{F_\alpha\}_{\alpha<\kappa}$ of closed sets can be separated by a pairwise disjoint open family $\{U_\alpha\}$ with $F_\alpha \subseteq U_\alpha$. **Collectionwise Hausdorff (cwH).** The same for discrete families of singletons, i.e. closed discrete subsets are separated.

**Bing's metrization theorem (1951).** A regular space is metrizable iff it has a $\sigma$-discrete base. Corollary used throughout:
$$\text{Moore} \;+\; \text{collectionwise normal} \;\Longleftrightarrow\; \text{metrizable}.$$
So NMSC is exactly the statement *normal $\Rightarrow$ collectionwise normal for Moore spaces*. For Moore spaces, cwH already suffices in the presence of normality via a refinement argument, so the combinatorial core is the separation of closed discrete sets of size $\aleph_1$.

**$Q$-set.** An uncountable $X \subseteq \mathbb{R}$ is a $Q$-set if every $A \subseteq X$ is relatively $F_\sigma$ in $X$ (equivalently $G_\delta$). $\mathsf{MA}_{\aleph_1}$ implies every set of reals of size $\aleph_1$ is a $Q$-set; $\mathsf{CH}$ implies none exists.

**PMEA (Product Measure Extension Axiom).** For every cardinal $\kappa$, the usual product measure $\mu_\kappa$ on $2^{\kappa}$ extends to a $2^{\aleph_0}$-additive measure defined on *all* subsets of $2^\kappa$. Kunen: Lévy-collapsing a strongly compact $\kappa$ to $\mathfrak{c}$ (adding $\kappa$ random reals) yields PMEA.

**Jones's cardinal inequality.** If $X$ is separable and normal with a closed discrete $D \subseteq X$, then $2^{|D|} \le 2^{\aleph_0}$, since each $A \subseteq D$ yields a distinct open separation and hence a distinct trace on a countable dense set.

## 3. History & State of the Art (SOTA)

- **1937 — F. B. Jones.** Poses the problem and proves: $2^{\aleph_0} < 2^{\aleph_1}$ implies every **separable** normal Moore space is metrizable. He also proves NMSC outright for separable spaces under his hypothesis, launching four decades of work.
- **1951 — R. H. Bing.** Metrization theorem plus *Example G*: a normal, non-metrizable, non-Moore space, and the identification cwn $=$ the missing ingredient. Bing also shows a Moore space is metrizable iff it is cwn.
- **1964 — R. W. Heath.** The tangent-disc (Niemytzki-type) space over $X \subseteq \mathbb{R}$ is normal iff $X$ is a $Q$-set; combined with Silver's $\mathsf{MA}+\neg\mathsf{CH}$ construction of $Q$-sets this refutes NMSC in models of $\mathsf{MA}_{\aleph_1}$.
- **1970s — F. D. Tall, W. Fleissner.** Tall's *Dissertationes Mathematicae* 148 (1977) systematises the consistency results. Fleissner (1974) proves $V=L$ implies every normal space of character $\le \aleph_1$ is cwH — so under $V=L$ no *first-countable* counterexample of that type, yet $V=L$ still yields normal non-metrizable Moore spaces at higher character (Fleissner's "George").
- **1980 — P. Nyikos, "A provisional solution".** PMEA $\Rightarrow$ NMSC. Upper bound: a strongly compact cardinal.
- **1982 — W. Fleissner.** NMSC $\Rightarrow$ an inner model with a measurable cardinal, via the Dodd–Jensen core model and the covering lemma: if no such inner model exists, $\square$-like principles in $K$ build a normal non-metrizable Moore space. Companion PNAS note: a counterexample follows from $\mathsf{CH}$ *or* from the non-existence of inner models with measurables.
- **1990 — Dow, Tall, Weiss.** New, more transparent consistency proofs from a supercompact, isolating the reflection content rather than the measure-theoretic content.

State of the art: the problem is *solved as an independence question* and *open as a strength question*. The interval between "inner model with a measurable" and "strongly compact" has not been closed since 1982.

## 4. Partial Results / Verified Cases

| Class / hypothesis | Result |
|---|---|
| Separable Moore spaces, $2^{\aleph_0}<2^{\aleph_1}$ | Normal $\Rightarrow$ metrizable (Jones 1937) |
| Metacompact (or screenable, or para-Lindelöf) Moore spaces | Normal $\Rightarrow$ metrizable, in ZFC (Bing / Traylor-type arguments: metacompact + normal $\Rightarrow$ cwn for Moore spaces) |
| Moore spaces of cardinality $\le \aleph_1$ under $\mathsf{MA}_{\aleph_1}$ | Normal $\Rightarrow$ metrizable at cardinality $<\mathfrak c$ (Tall 1977) — while $Q$-sets simultaneously give counterexamples of size $\aleph_1$ in the *separable* tangent-disc form; the two are reconciled by weight, not cardinality |
| Locally compact normal Moore spaces | Metrizable under $\mathsf{MA}_{\aleph_1}$ (Fleissner); non-metrizable examples under $V=L$. Balogh (1991): a supercompact gives *locally compact normal $\Rightarrow$ cwn* in general |
| Character $\le \aleph_1$, $V=L$ | Every normal space of character $\le\aleph_1$ is cwH (Fleissner 1974) |
| All Moore spaces, under PMEA | Normal $\Rightarrow$ metrizable (Nyikos 1980) |
| All Moore spaces, under $\mathsf{CH}$ or $\mathsf{MA}_{\aleph_1}$ or $V=L$ | Counterexamples exist |

## 5. Principal Obstacles

- **The result is a consistency-strength problem, not a topology problem.** Ordinary topological technique (metrization theorems, refinement of covers, $\sigma$-discrete bases) is exhausted: everything reduces to separating an $\aleph_1$-sized closed discrete set, which is a purely combinatorial statement about $[\kappa]^{\aleph_0}$.
- **Measure vs. reflection.** The only known routes to NMSC are (i) PMEA, whose $2^{\aleph_0}$-additive measure on $2^\kappa$ is essentially a strong-compactness artefact, and (ii) supercompact reflection (Dow–Tall–Weiss). Neither is known to survive down to a measurable; measure extension of that additivity on *all* subsets of $2^\kappa$ for *all* $\kappa$ is not obtainable from a single measurable by any known forcing.
- **Core-model lower bound is not tight.** Fleissner's argument uses the Dodd–Jensen covering lemma for $K$; the modern core-model machinery (Mitchell–Steel, $K^{\mathrm{DJ}} \to K^{\text{strong}}$) has not been pushed through the same construction, so we do not know whether NMSC really implies more than one measurable. The obstruction is that the Moore-space construction consumes a $\square$-sequence-like object, and the failure of $\square$ at singulars is a *low*-strength phenomenon compared with strong compactness.
- **No canonical inner model at the top.** There is no fine-structural inner model theory reaching strongly compact cardinals, so one cannot compute the strength of NMSC by comparison with a canonical model.

## 6. The Gap

Precisely:
$$\mathrm{Con}(\exists \text{ measurable}) \;\overset{?}{\le}\; \mathrm{Con}(\mathrm{ZFC}+\mathrm{NMSC}) \;\le\; \mathrm{Con}(\exists \text{ strongly compact}).$$
The lower bound (Fleissner 1982) is "an inner model with a measurable". Everything between one measurable and a strongly compact — measurables of high Mitchell order, strong cardinals, Woodins, superstrongs — is unclassified for NMSC. The single missing step is either:

1. a forcing construction producing NMSC from a hypothesis provably weaker than strong compactness (equivalently: an axiom weaker than PMEA that still separates $\aleph_1$-many closed discrete points in every normal Moore space); or
2. a strengthening of Fleissner's core-model argument that extracts, from a counterexample-free universe, an inner model with a strong cardinal or beyond.

## 7. Current Research (as of June 2026)

- **Set-theoretic topology after Balogh.** Work continues on the locally compact normal spaces programme (Balogh's theorem that a supercompact makes locally compact normal $\Rightarrow$ cwn), asking whether the supercompact can be reduced. This is the closest live analogue of the NMSC strength question. *(frontier — verify)*
- **Core-model induction.** Groups working on core-model induction (Schindler, Steel and successors) have pushed lower bounds for combinatorial statements from measurables to Woodin-cardinal territory. Whether NMSC or its cwH fragment admits such an induction is an open target. *(frontier — verify)*
- **Measure-theoretic weakenings of PMEA.** Variants such as "there is a $\mathfrak c$-additive measure on $2^{\aleph_1}$" and the Covering Property Axiom setting are studied to see which suffice for the separation step. *(frontier — verify)*
- Key venues: *Topology and its Applications*, *Fundamenta Mathematicae*, the annual Spring Topology and Dynamics Conference; groups historically at Toronto (Tall, Dow), Auburn (Nyikos), Kansas (Fleissner).

## 8. Future Work

- Determine whether PMEA itself is equiconsistent with a strongly compact cardinal; if it is strictly weaker, NMSC's upper bound drops immediately.
- Isolate the exact reflection principle used in Dow–Tall–Weiss and test it against Mitchell-order hypotheses.
- Push Fleissner's construction through $K^{\text{Mitchell–Steel}}$: obtain a normal non-metrizable Moore space from "no inner model with a strong cardinal".
- Settle the *locally compact* NMSC strength (Balogh's supercompact vs. Fleissner's measurable) — expected to be a strictly easier proxy.

## 9. Key References

- **[Foundational]** F. B. Jones. *Concerning normal and completely normal spaces.* Bulletin of the American Mathematical Society **43** (1937), 671–677.
- **[Foundational]** R. H. Bing. *Metrization of topological spaces.* Canadian Journal of Mathematics **3** (1951), 175–186.
- **[Foundational]** R. W. Heath. *Screenability, pointwise paracompactness, and metrization of Moore spaces.* Canadian Journal of Mathematics **16** (1964), 763–770.
- **[Key]** W. G. Fleissner. *Normal Moore spaces in the constructible universe.* Proceedings of the American Mathematical Society **46** (1974), 294–298.
- **[Key]** F. D. Tall. *Set-theoretic consistency results and topological theorems concerning the normal Moore space conjecture and related problems.* Dissertationes Mathematicae **148** (1977).
- **[SOTA]** P. J. Nyikos. *A provisional solution to the normal Moore space problem.* Proceedings of the American Mathematical Society **78** (1980), 429–435.
- **[SOTA]** W. G. Fleissner. *If all normal Moore spaces are metrizable, then there is an inner model with a measurable cardinal.* Transactions of the American Mathematical Society **273** (1982), 365–373.
- **[SOTA]** W. G. Fleissner. *Normal nonmetrizable Moore space from continuum hypothesis or nonexistence of inner models with measurable cardinals.* Proceedings of the National Academy of Sciences USA **79** (1982), 1371–1372.
- **[SOTA]** A. Dow, F. D. Tall, W. A. R. Weiss. *New proofs of the consistency of the normal Moore space conjecture I, II.* Topology and its Applications **37** (1990), 33–51 and 115–129.
- **[Related]** Z. Balogh. *On collectionwise normality of locally compact, normal spaces.* Transactions of the American Mathematical Society **323** (1991), 389–411.
- **[Survey]** W. G. Fleissner. *The normal Moore space conjecture and large cardinals*, and F. D. Tall, *Normality versus collectionwise normality*, in K. Kunen and J. E. Vaughan (eds.), *Handbook of Set-Theoretic Topology*, North-Holland, 1984.
- **[Survey]** P. J. Nyikos. *A history of the normal Moore space problem*, in C. E. Aull and R. Lowen (eds.), *Handbook of the History of General Topology*, Vol. 3, Kluwer, 2001.

## 10. Worked Example / Concrete Special Case

**The tangent-disc space $M(X)$.** Fix $X \subseteq \mathbb{R}$. Let
$$M(X) = (\mathbb{R} \times (0,\infty)) \;\cup\; (X \times \{0\}).$$
Points of the open upper half-plane get their usual Euclidean neighbourhoods. A point $p = (x,0)$ with $x \in X$ gets basic neighbourhoods
$$D_n(p) = \{p\} \cup \{\text{open disc of radius } 1/n \text{ tangent to the } x\text{-axis at } p\}.$$

**(a) $M(X)$ is a Moore space.** Put $\mathcal{G}_n = \{\, B(q,1/n) : q \in \mathbb{R}\times(0,\infty)\,\} \cup \{\, D_n(p) : p \in X\times\{0\}\,\}$. For $p=(x,0)$, any $\mathcal G_n$-element containing $p$ is exactly $D_n(p)$ (Euclidean balls in the open half-plane miss $p$), so $\mathrm{st}(p,\mathcal G_n) = D_n(p)$, giving a base at $p$. For interior points the stars shrink to Euclidean balls of radius $\le 2/n$. Regularity is routine. So $\langle \mathcal G_n\rangle$ is a development.

**(b) $M(X)$ is separable and, for $X$ uncountable, non-metrizable.** $\mathbb{Q}\times\mathbb{Q}^{+}$ is countable dense. The set $D = X\times\{0\}$ is closed and discrete (each $D_n(p)$ meets $D$ only in $p$). A separable metric space is second countable, hence hereditarily Lindelöf, hence has no uncountable closed discrete subspace. So $|X| \ge \aleph_1$ forces non-metrizability.

**(c) Normality $\Leftrightarrow$ $X$ is a $Q$-set.** Suppose $M(X)$ is normal and $A \subseteq X$. Then $A\times\{0\}$ and $(X\setminus A)\times\{0\}$ are disjoint closed sets; separating open sets $U \supseteq A\times\{0\}$ give, for each $n$, $A_n = \{x\in A: D_n((x,0)) \subseteq U\}$, and one checks $A = \bigcup_n \overline{A_n}\cap X$ with each $\overline{A_n}\cap X$ closed in $X$ — so $A$ is $F_\sigma$ in $X$, i.e. $X$ is a $Q$-set. Conversely, a $Q$-set lets one choose radii uniformly on each $F_\sigma$ piece and build the separation.

**(d) The independence, in one line.**
- Under $\mathsf{MA}+\neg\mathsf{CH}$: every $X\subseteq\mathbb{R}$ with $|X|=\aleph_1$ is a $Q$-set, so $M(X)$ is a **normal non-metrizable Moore space** — NMSC fails.
- Under $\mathsf{CH}$: $2^{\aleph_0}=\aleph_1<2^{\aleph_1}$, so Jones's inequality $2^{|D|}\le 2^{\aleph_0}$ with $|D|=\aleph_1$ fails; hence no $Q$-set exists and $M(X)$ is never normal for uncountable $X$. (Other, non-separable counterexamples exist under $\mathsf{CH}$ — Fleissner 1982 — so NMSC fails there too, just not via $M(X)$.)

This single family shows that the separable case of NMSC is decided by cardinal arithmetic alone, while the general case escapes into large-cardinal territory.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*