---
id: 08-logic-set-theory/borel-conjecture-strong-measure-zero
title: "Borel's Conjecture on Strong Measure Zero Sets"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borel's Conjecture on Strong Measure Zero Sets

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/borel-conjecture-strong-measure-zero` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

A set $X \subseteq \mathbb{R}$ has **strong measure zero** (smz) if for every sequence $(\varepsilon_n)_{n \in \omega}$ of positive reals there is a sequence of intervals $(I_n)_{n \in \omega}$ with $|I_n| \le \varepsilon_n$ and $X \subseteq \bigcup_{n \in \omega} I_n$.

**Borel's Conjecture (BC, 1919).** Every strong measure zero set of reals is countable.

The conjecture is *not* a theorem or a refutable statement of ZFC: it is independent. Sierpiński (1928) showed $\mathrm{CH} \Rightarrow \neg\mathrm{BC}$; Laver (1976) showed $\mathrm{Con}(\mathrm{ZFC}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{BC})$. What remains open is the *comparative* theory: which combinations of BC, its dual, generalisations to metric spaces and Polish groups, and values of $\mathfrak{c}$ are consistent, and by which forcing technology. A complete resolution of any one of these means exhibiting a forcing extension (or an inner-model/absoluteness argument) settling the combination outright.

## 2. Mathematical Foundations

Work in $2^\omega$ or $\mathbb{R}$ with Lebesgue measure $\lambda$ and the ideals $\mathcal{N}$ (null), $\mathcal{M}$ (meager), $\mathcal{SN}$ (strong measure zero).

**Definition (smz, general form).** For a metric space $(Z,d)$, $X \subseteq Z$ is smz if
$$\forall (\varepsilon_n)_{n\in\omega} \in (0,\infty)^\omega \ \exists (A_n)_{n\in\omega} \ \big(\operatorname{diam}(A_n) \le \varepsilon_n \ \wedge \ X \subseteq \textstyle\bigcup_n A_n\big).$$

**Fact 2.1.** $\mathcal{SN} \subsetneq \mathcal{N}$. Taking $\varepsilon_n = \delta 2^{-n-1}$ gives $\lambda^*(X) \le \delta$ for all $\delta > 0$.

**Fact 2.2 (dimension).** smz $\Rightarrow$ $\mathcal{H}^s(X) = 0$ for every $s>0$, hence $\dim_H X = 0$: given $s,\delta$, pick $\varepsilon_n$ with $\sum_n \varepsilon_n^s < \delta$; then any admissible cover satisfies $\sum_n |I_n|^s < \delta$.

**Fact 2.3.** $\mathcal{SN}$ is a $\sigma$-ideal containing all countable sets, invariant under translation, and closed under uniformly continuous images.

**Theorem 2.4 (Galvin–Mycielski–Solovay).** For $X \subseteq \mathbb{R}$ (or any locally compact Polish group),
$$X \in \mathcal{SN} \iff \forall M \in \mathcal{M} \ (X + M \neq \mathbb{R}).$$
This turns a measure-theoretic notion into a category-theoretic one and is the engine of nearly all later work.

**Definition (dual notions).** $X$ is **strongly meager** if $X + N \neq \mathbb{R}$ for every $N \in \mathcal{N}$. The **Dual Borel Conjecture (dBC)** asserts every strongly meager set is countable.

**Cardinal characteristics.** Every $X$ with $|X| < \operatorname{cov}(\mathcal{M})$ is smz, so
$$\operatorname{cov}(\mathcal{M}) \le \operatorname{non}(\mathcal{SN}), \qquad \mathrm{BC} \Rightarrow \operatorname{cov}(\mathcal{M}) = \aleph_1 .$$
Also $\operatorname{add}(\mathcal{SN}) \ge \operatorname{add}(\mathcal{M})$ and $\operatorname{cof}(\mathcal{SN}) \ge \mathfrak{d}$. Note BC is strictly stronger than $\operatorname{non}(\mathcal{SN}) = \aleph_1$: it asserts $\mathcal{SN} = [\mathbb{R}]^{\le \omega}$.

**Luzin sets.** $L$ is *Luzin* if $|L| = \aleph_1$ and $|L \cap M| \le \aleph_0$ for every $M \in \mathcal{M}$. CH (or $\operatorname{cov}(\mathcal{M}) = \mathfrak{c} = \aleph_1$) yields one by transfinite recursion.

**Laver forcing $\mathbb{L}$.** Conditions are trees $p \subseteq \omega^{<\omega}$ with a stem $s$ such that every $t \supseteq s$ in $p$ has infinitely many immediate successors; ordering is $\subseteq$. $\mathbb{L}$ is proper, adds a dominating real, and has the **Laver property**: every new $g \le f$ (with $f$ ground-model) is contained in a ground-model slalom $S$ with $|S(n)| \le n$.

## 3. History & State of the Art (SOTA)

- **1919** — Borel, *Sur la classification des ensembles de mesure nulle*, isolates the notion (his "mesure asymptotique nulle") and states the conjecture, remarking he can neither prove nor refute it.
- **1928** — Sierpiński: a Luzin set is smz. Under CH this is an uncountable smz set, so $\mathrm{CH} \Rightarrow \neg \mathrm{BC}$. (Martin's Axiom likewise refutes BC, since $\operatorname{cov}(\mathcal{M}) = \mathfrak{c}$.)
- **1970s** — Galvin, Mycielski and Solovay prove the translation characterisation (Theorem 2.4), announced as an AMS abstract; the full proof appeared only in 2017.
- **1976** — Laver proves $\mathrm{Con}(\mathrm{BC})$ by a countable support iteration of $\mathbb{L}$ of length $\omega_2$ over a model of CH. This is the first substantial use of countable support iteration of a non-$\omega^\omega$-bounding proper forcing and a template for the whole subject.
- **1989–1990** — Corazza gives generalised BC for arbitrary "$\sigma$-totally bounded" settings via strongly proper orders; Judah, Shelah and Woodin show BC is consistent with $\mathfrak{c}$ arbitrarily large, decoupling BC from $\mathfrak{c} = \aleph_2$.
- **1993** — Carlson proves $\mathrm{Con}(\mathrm{dBC})$: adding $\aleph_2$ Cohen reals makes every strongly meager set countable.
- **2014** — Goldstern, Kellner, Shelah, Wohofsky prove $\mathrm{Con}(\mathrm{BC} + \mathrm{dBC})$, an ~60-page argument combining a non-elementary "partial countable support" product/iteration with preservation theorems. This is the "solved-recently" milestone.
- **2016–present** — Hrušák, Wohofsky, Zindulka and others move the question to non-locally-compact Polish groups, where GMS can fail.

## 4. Partial Results / Verified Cases

- **Countable sets** and, more generally, all $\sigma$-compact-in-a-zero-dimensional-sense sets of size $< \operatorname{cov}(\mathcal{M})$: smz, so BC forces $\operatorname{cov}(\mathcal{M}) = \aleph_1$.
- **BC holds** in the Laver model ($\mathfrak{c} = \aleph_2$, $\mathfrak{b} = \mathfrak{d} = \aleph_2$, $\operatorname{cov}(\mathcal{M}) = \aleph_1$) and in the Mathias model.
- **BC with large continuum**: Judah–Shelah–Woodin — $\mathrm{BC} + \mathfrak{c} = \kappa$ is consistent for any regular $\kappa \ge \aleph_2$ of uncountable cofinality.
- **dBC holds** in the Cohen model (Carlson).
- **BC $+$ dBC** consistent (GKSW 2014), with $\mathfrak{c} = \aleph_2$ in the published model.
- **BC fails** outright under CH, MA, or any hypothesis giving a Luzin set; also whenever $\operatorname{cov}(\mathcal{M}) \ge \aleph_2$.
- **Borel sets**: every smz Borel (indeed analytic) set is countable in ZFC — an analytic smz set has $\dim_H = 0$ and hence contains no perfect set, so by the perfect set property it is countable. BC is thus purely a statement about non-definable sets.
- **Metric-space versions**: BC for $2^\omega$ with the standard metric is equivalent to BC for $\mathbb{R}$; for the Polish group $\mathbb{Z}^\omega$ the GMS equivalence consistently fails (Hrušák–Wohofsky–Zindulka).

## 5. Principal Obstacles

- **No absoluteness.** BC quantifies over arbitrary uncountable sets of reals, a $\Pi^1_3$-over-$\mathcal{P}(\mathbb{R})$-style statement not decided by forcing axioms, large cardinals, or determinacy. Every proof must be a consistency proof.
- **Iteration incompatibility.** BC needs a dominating/Laver-type real at cofinally many stages (to kill old smz sets); dBC needs Cohen-like reals (to kill strongly meager sets). These preservation requirements are in tension: a Cohen real makes ground-model reals smz-ish and destroys the Laver property; a dominating real destroys Cohen-genericity. Straightforward finite- or countable-support iteration cannot do both, which is exactly why $\mathrm{Con}(\mathrm{BC}+\mathrm{dBC})$ took 21 years after Carlson.
- **Preservation theorems are fragile.** Laver's argument rests on a fusion/pure-decision analysis showing an uncountable ground-model set stays non-smz through an $\omega_2$-length countable support iteration; the analogous preservation for strongly meager sets requires controlling null sets in the *iterated* extension, where the "$X + N \ne \mathbb{R}$" quantifier reflects badly.
- **Failure of GMS beyond local compactness.** In $\mathbb{Z}^\omega$ or general Polish groups the translation characterisation is not a theorem, so the whole category-theoretic toolkit evaporates and one must argue with covers directly.
- **Continuum-size rigidity.** The GKSW construction is tuned to $\aleph_2$; pushing to $\mathfrak{c} > \aleph_2$ needs a genuinely new bookkeeping/product argument, not a longer iteration.

## 6. The Gap

Proven: BC alone with arbitrary $\mathfrak{c}$; dBC alone; BC $+$ dBC with $\mathfrak{c} = \aleph_2$.

Open boundary: **$\mathrm{Con}(\mathrm{BC} + \mathrm{dBC} + \mathfrak{c} > \aleph_2)$** (explicitly asked by Goldstern–Kellner–Shelah–Wohofsky). The technical step is a forcing that (i) is proper and $\aleph_2$-cc-like at length $> \omega_2$, (ii) preserves "old uncountable sets are non-smz" *and* "old uncountable sets are not strongly meager" simultaneously, and (iii) supports bookkeeping over $\ge \aleph_3$ many potential counterexamples. Countable support caps $\mathfrak{c}$ at $\aleph_2$; finite support adds Cohen reals and kills BC. The gap is precisely the absence of an iteration/support notion in between with both preservation properties.

Secondary gaps: BC for the Marczewski ideal $s_0$; a ZFC-provable characterisation of $\mathcal{SN}$ in non-locally-compact Polish groups; whether $\mathrm{BC} \Rightarrow \mathfrak{b} > \aleph_1$ (no known implication either way in full generality).

## 7. Current Research (as of June 2026)

- **Vienna / TU Wien school** (Goldstern, Kellner, Wohofsky, with Shelah): creature forcing and non-linear iteration templates aimed at BC-type statements with $\mathfrak{c} > \aleph_2$; the same technology drives the "many values in Cichoń's diagram" results.
- **Mexico–Kobe axis** (Hrušák; Mejía, Cardona, Rivera-Madrid): cardinal invariants of $\mathcal{SN}$, Yorioka ideals $\mathcal{I}_f$, and the invariants of the meager-additive and null-additive ideals; the higher-dimensional/$\kappa$-analogue of $\mathcal{SN}$ on $2^\kappa$ *(frontier — verify)*.
- **Prague geometric-measure school** (Zindulka): smz and meager-additivity recast through fractal/gauge measures and monotone metric-space maps, giving ZFC characterisations of $\mathcal{E}$-additive sets.
- **Polish-group generalisations**: after Hrušák–Wohofsky–Zindulka (2016), the status of GMS in $\mathbb{Z}^\omega$, $S_\infty$ and non-locally-compact groups is an active line *(frontier — verify)*.

## 8. Future Work

- Design a support notion interpolating finite and countable support (e.g. a "partial countable support" product as in GKSW, generalised to length $\omega_3$) to obtain $\mathrm{BC}+\mathrm{dBC}+\mathfrak{c} = \aleph_3$.
- Isolate an abstract preservation property ("$\mathcal{SN}$-preserving $+$ strongly-meager-preserving") that is provably closed under the intended iteration, in the style of Shelah's preservation theorems for proper forcing.
- Settle $\operatorname{cof}(\mathcal{SN})$ and $\operatorname{add}(\mathcal{SN})$ in ZFC beyond Yorioka's CH-characterisation.
- Determine whether BC has any consequence for $\mathfrak{b}$, $\mathfrak{d}$ or the Cichoń diagram beyond $\operatorname{cov}(\mathcal{M}) = \aleph_1$.
- Develop a non-locally-compact substitute for the Galvin–Mycielski–Solovay theorem.

## 9. Key References

- **[Foundational]** É. Borel. *Sur la classification des ensembles de mesure nulle.* Bulletin de la Société Mathématique de France 47 (1919), 97–125.
- **[Foundational]** W. Sierpiński. *Sur un ensemble non dénombrable, dont toute image continue est de mesure nulle.* Fundamenta Mathematicae 11 (1928), 302–304.
- **[Foundational]** R. Laver. *On the consistency of Borel's conjecture.* Acta Mathematica 137 (1976), 151–169.
- **[Foundational]** F. Galvin, J. Mycielski, R. Solovay. *Strong measure zero and infinite games.* Archive for Mathematical Logic 56 (2017), 725–732.
- **[SOTA / Recent]** M. Goldstern, J. Kellner, S. Shelah, W. Wohofsky. *Borel conjecture and dual Borel conjecture.* Transactions of the AMS 366 (2014), 245–307.
- **[Key]** T. Carlson. *Strong measure zero and strongly meager sets.* Proceedings of the AMS 118 (1993), 577–586.
- **[Key]** H. Judah, S. Shelah, W. H. Woodin. *The Borel conjecture.* Annals of Pure and Applied Logic 50 (1990), 255–269.
- **[Key]** P. Corazza. *The generalized Borel conjecture and strongly proper orders.* Transactions of the AMS 316 (1989), 115–140.
- **[Key]** T. Yorioka. *The cofinality of the strong measure zero ideal.* Journal of Symbolic Logic 67 (2002), 1373–1384.
- **[Recent]** M. Hrušák, W. Wohofsky, O. Zindulka. *Strong measure zero in separable metric spaces and Polish groups.* Archive for Mathematical Logic 55 (2016), 105–131.
- **[Survey]** T. Bartoszyński, H. Judah. *Set Theory: On the Structure of the Real Line.* A K Peters, 1995 (Chapter 8).
- **[Survey]** A. W. Miller. *Special subsets of the real line.* In: Handbook of Set-Theoretic Topology, North-Holland, 1984, 201–233.

## 10. Worked Example / Concrete Special Case

**(a) The Cantor set is measure zero but not strong measure zero.** Let $C$ be the middle-thirds set, $\dim_H C = \log 2/\log 3 \approx 0.6309$. Put $s = 0.5 < \dim_H C$, so $\mathcal{H}^s(C) = \infty$. If $C$ were smz, choose $\varepsilon_n = 2^{-n}$; then $\sum_n \varepsilon_n^s = \sum_n 2^{-n/2} = (1-2^{-1/2})^{-1} \approx 3.41 < \infty$, and rescaling $\varepsilon_n \mapsto t\varepsilon_n$ makes this sum $< \delta$ for any $\delta$. Any admissible cover gives $\mathcal{H}^s_\infty(C) \le \sum_n |I_n|^s < \delta$, contradiction. So $\mathcal{SN} \subsetneq \mathcal{N}$ strictly, and smz is a genuinely finer notion.

**(b) Sierpiński's refutation of BC under CH.** Assume CH and let $L = \{x_\alpha : \alpha < \omega_1\}$ be Luzin: enumerate all meager $F_\sigma$ sets as $(M_\alpha)_{\alpha<\omega_1}$ and pick $x_\alpha \notin \bigcup_{\beta \le \alpha} M_\beta \cup \{x_\beta : \beta<\alpha\}$ (possible: $\mathbb{R}$ is not meager). Then $|L \cap M| \le \aleph_0$ for every meager $M$.

*Claim: $L$ is smz.* Fix $(\varepsilon_n)_{n\in\omega}$. Split $\omega = A \sqcup B$ into two infinite sets, and fix bijections $A \to \mathbb{Q}$, $n \mapsto q_n$. Put
$$U = \bigcup_{n \in A} \Big( q_n - \tfrac{\varepsilon_n}{2},\ q_n + \tfrac{\varepsilon_n}{2} \Big).$$
$U$ is open and dense (it contains every rational), so $F = \mathbb{R} \setminus U$ is closed nowhere dense, hence meager. By Luzinness $L \cap F$ is countable; enumerate it as $\{y_k : k \in \omega\}$ and let $b_0 < b_1 < \cdots$ enumerate $B$. Cover $y_k$ by $J_k = (y_k - \varepsilon_{b_k}/2,\ y_k + \varepsilon_{b_k}/2)$. Then
$$L \subseteq U \cup \bigcup_{k\in\omega} J_k,$$
a cover by intervals with $|I_n| \le \varepsilon_n$ for all $n$. Hence $L \in \mathcal{SN}$ while $|L| = \aleph_1$, so BC fails. $\square$

Note where CH is used: only to build $L$, i.e. $\operatorname{cov}(\mathcal{M}) = \mathfrak{c}$ suffices. Laver's model kills this by making $\operatorname{cov}(\mathcal{M}) = \aleph_1 < \mathfrak{c}$ *and* by iteratively adding, for each candidate uncountable set $X$ appearing at some stage $\alpha < \omega_2$ (properness plus $\aleph_2$-cc guarantee every such $X$ of size $\aleph_1$ appears at a stage of cofinality $\omega_1$), a Laver real whose associated $(\varepsilon_n)$ defeats every possible cover of $X$; the Laver property, preserved by countable support iteration, ensures no later stage undoes this.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*