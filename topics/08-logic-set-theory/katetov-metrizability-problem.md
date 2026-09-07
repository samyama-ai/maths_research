---
id: 08-logic-set-theory/katetov-metrizability-problem
title: "Katetov Metrizability Problem"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Katetov Metrizability Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/katetov-metrizability-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Katětov's problem.** Let $X$ be a compact Hausdorff space such that $X^2 = X \times X$ is hereditarily normal (every subspace of $X^2$ is normal, equivalently $X^2$ is *completely normal*). Must $X$ be metrizable?

Katětov (1948) proved the corresponding statement for the **cube**: if $X$ is compact Hausdorff and $X^3$ is hereditarily normal, then $X$ is metrizable. The square case was left open and is the problem catalogued here.

Resolution status: the question is **independent of ZFC**.

- **Negative side.** Gruenhage and Nyikos (1993) constructed, assuming CH, a compact non-metrizable $X$ with $X^2$ hereditarily normal.
- **Positive side.** Larson and Todorcevic (2002) produced a model of ZFC in which *every* compact space with hereditarily normal square is metrizable, relative to the consistency of ZFC alone.

A complete resolution of the residual problem would mean deciding which further hypotheses (e.g. $\mathrm{MA}_{\aleph_1}$, PFA, $\mathfrak{b}=\aleph_1$) imply which side, and whether the positive answer follows from a standard forcing axiom rather than from the specialised $\mathrm{MA}(S)[S]$ machinery.

## 2. Mathematical Foundations

Let $X$ be $T_1$ and Hausdorff throughout.

- $X$ is **normal** if disjoint closed $A,B$ have disjoint open neighbourhoods.
- $X$ is **hereditarily normal** (completely normal) iff every pair of *separated* sets $A,B$ (i.e. $\overline{A}\cap B = A \cap \overline{B} = \varnothing$) can be put into disjoint open sets.
- $X$ is **perfectly normal** iff $X$ is normal and every closed set is a $G_\delta$: $F=\bigcap_{n<\omega} U_n$ with $U_n$ open.
- $X$ has a **$G_\delta$-diagonal** iff $\Delta = \{(x,x): x\in X\}=\bigcap_{n<\omega}U_n$ for open $U_n\subseteq X^2$.

Three classical ingredients drive the whole problem.

**(T1) Katětov's lemma.** If $X\times Y$ is hereditarily normal, then either every countable subset of $X$ is closed and discrete, or $Y$ is perfectly normal.

**(T2)** Every infinite compact Hausdorff space contains a countable non-closed subset. Hence, for compact infinite $X$,
$$X^2 \text{ hereditarily normal} \implies X \text{ perfectly normal},$$
$$X^3 \text{ hereditarily normal} \implies X^2 \text{ perfectly normal}.$$

**(T3) Šneĭder's theorem (1945).** A compact Hausdorff space with a $G_\delta$-diagonal is metrizable.

Katětov's cube theorem follows: $X^2$ perfectly normal makes $\Delta$ a $G_\delta$ in $X^2$, so (T3) applies.

For the square, only the weaker conclusion survives. Since a perfectly normal compact space is hereditarily Lindelöf (each open set is $\sigma$-compact) and hence has countable spread and cardinality $\le \mathfrak{c}$, any counterexample $X$ satisfies
$$w(X) > \aleph_0,\quad hL(X)=hd(X)=s(X)=\aleph_0,\quad |X|\le\mathfrak{c},$$
i.e. $X$ is a **perfectly normal non-metrizable compactum** — a compact $L$-space-like object — with the extra requirement that $X^2$ be hereditarily normal.

## 3. History & State of the Art (SOTA)

- **1945.** Šneĭder: compact $+$ $G_\delta$-diagonal $\Rightarrow$ metrizable.
- **1948.** Katětov, *Complete normality of Cartesian products* (Fund. Math. 35): the lemma (T1) and the $X^3$ theorem; a correction appeared in Fund. Math. 40 (1953). The square question is posed there.
- **1970s.** Fedorchuk and Filippov construct, under $\diamondsuit$ and CH, perfectly normal non-metrizable compacta by inverse limits with fully closed bonding maps — showing the "perfectly normal" conclusion of (T2) is far weaker than metrizability. In ZFC the split interval (double arrow space) already witnesses this.
- **1993.** Gruenhage–Nyikos, *Normality in $X^2$ for compact $X$* (Trans. AMS 340): CH yields a compact non-metrizable $X$ with $X^2$ hereditarily normal, plus ZFC structure theorems constraining any counterexample.
- **2002.** Larson–Todorcevic, *Katětov's problem* (Trans. AMS 354): consistency of the positive answer, via forcing with a coherent Souslin tree $S$ over a model of $\mathrm{MA}(S)$ — the $\mathrm{MA}(S)[S]$ method. In such a model, every compact space with hereditarily normal square is metrizable.
- **2010s–2020s.** The $\mathrm{MA}(S)[S]$ technique becomes a standard tool for "all hereditarily normal $X$ are nice" statements; Dow–Tall (Trans. AMS 372, 2019) use it to show consistency of "every hereditarily normal manifold of dimension $>1$ is metrizable."

**SOTA summary:** the problem is settled as an independence result. What remains open is whether the positive answer is a consequence of a mainstream axiom such as PFA or $\mathrm{MA}_{\aleph_1}$.

## 4. Partial Results / Verified Cases

Positive (metrizability provable) cases, in ZFC unless stated:

- **Higher powers.** $X^n$ hereditarily normal for some $n\ge 3$ $\Rightarrow$ $X$ metrizable (Katětov).
- **$X^2$ perfectly normal** $\Rightarrow$ $X$ metrizable (immediately from (T3)); so a counterexample must have $X$ perfect but $X^2$ *not* perfect.
- **Dyadic compacta**, hence all compact topological groups: a perfectly normal dyadic compactum is metrizable, so $X^2$ hereditarily normal already suffices in this class.
- **Metrizably fibered / first-countable scattered classes**: perfect normality forces countable weight when the space is scattered compact (a perfectly normal scattered compactum is countable and metrizable).
- **Weight $\le \aleph_0$** is trivially the target; any counterexample has $\aleph_1 \le w(X) \le \mathfrak{c}$ and $|X|\le\mathfrak{c}$.
- **Model-theoretic case.** In $\mathrm{MA}(S)[S]$ models (Larson–Todorcevic 2002), *all* compact $X$ with $X^2$ hereditarily normal are metrizable — a consistency result covering every weight and cardinality.

Negative (counterexample) cases:

- **Under CH**, Gruenhage–Nyikos give a compact, hereditarily normal, non-metrizable $X$ of weight $\aleph_1$ with $X^2$ hereditarily normal, built by transfinite recursion of length $\omega_1$ enumerating all relevant separated pairs — CH is used to close off the bookkeeping at stage $\omega_1$.
- **Not counterexamples**, and instructive: the double arrow space $A$ (compact, perfectly normal, non-metrizable, ZFC) has $A^2$ *not* hereditarily normal (§10); ordinal space $\omega_1+1$ is hereditarily normal but not perfect, and $(\omega_1+1)^2$ is not hereditarily normal; a Souslin continuum $S$ is perfectly normal non-metrizable under $\diamondsuit$ but $S^2$ fails hereditary normality.

## 5. Principal Obstacles

- **Loss of one factor destroys the $G_\delta$-diagonal route.** All classical proofs go through "$X^2$ perfect $\Rightarrow$ $\Delta$ is $G_\delta$". With only $X^2$ hereditarily normal, Katětov's lemma returns perfect normality of $X$, not of $X^2$; there is no known way to upgrade separation properties of subspaces of $X^2$ to a countable family of open sets shrinking to $\Delta$.
- **Perfect normality is not a metrization property.** The split interval shows the natural first-order consequence of the hypothesis is strictly weaker than the conclusion, in ZFC. Any proof must use the *square* hypothesis on genuinely two-dimensional separated pairs — e.g. graphs of partial functions and anti-diagonals — which are combinatorial, not topological, objects.
- **Independence blocks all absolute methods.** Since CH gives a counterexample, no ZFC argument (compactness, measure/category, elementary submodel reflection, functional-analytic $C(X)$ techniques) can prove the positive answer. Conversely, the CH construction is a $\omega_1$-length recursion whose limit stages need a coherence hypothesis, so it does not survive to $\mathrm{MA}+\neg$CH.
- **Forcing axioms are the wrong shape.** $\mathrm{MA}_{\aleph_1}$ and PFA kill many $L$-space-like objects, but they also add reals and can create the very gaps and $\sigma$-directed families used to build hereditarily normal squares. The Larson–Todorcevic model needs the two-step $\mathrm{MA}(S)$-then-force-with-$S$ structure precisely because the Souslin tree $S$ destroys the $\aleph_1$-sized combinatorics after $\mathrm{MA}(S)$ has already tamed the ccc ones; no single-step forcing axiom is known to do both.
- **No structure theory for perfectly normal compacta.** Whether every perfectly normal compactum is, e.g., a continuous image of a nice space, is itself a long-standing open basis problem (Gruenhage–Moore); without such a classification, one cannot enumerate candidate counterexamples.

## 6. The Gap

Proven: metrizability from $X^3$ (ZFC); perfect normality of $X$ from $X^2$ (ZFC); metrizability from $X^2$ in $\mathrm{MA}(S)[S]$ models; a counterexample from CH.

The gap is therefore **not** "prove the conjecture" but: *identify the exact combinatorial principle equivalent, over ZFC, to "every compact $X$ with $X^2$ hereditarily normal is metrizable."* Concretely, the missing step is a characterisation of when a perfectly normal, non-metrizable compactum can have all separated pairs in $X^2$ — in particular pairs supported on uncountable "anti-diagonal" sets $\{(x,\sigma(x))\}$ for an involution-like $\sigma$ — simultaneously separated. CH supplies such a $\sigma$; $\mathrm{MA}(S)[S]$ refutes every $\sigma$. Nothing is known about the intermediate region, e.g. under $\mathfrak{b}=\aleph_1<\mathfrak{c}$, or under PFA.

## 7. Current Research (as of June 2026)

- **The $\mathrm{MA}(S)[S]$ programme** (Todorcevic, Larson, Dow, Tall and collaborators) continues to extract "hereditary normality implies metrizability" theorems in that model: manifolds, locally compact normal spaces, first-countable compacta. Katětov's problem is the template result of the programme.
- **Basis problems for perfectly normal compacta** (Gruenhage, Moore, Todorcevic): whether it is consistent that every perfectly normal compactum has a small basis of subspaces; a positive solution would give a structural, non-forcing route to Katětov-type theorems.
- **Whether PFA or $\mathrm{MA}_{\aleph_1}$ alone implies the positive answer remains, to our knowledge, unresolved** *(frontier — verify)*; several authors list this as the main remaining question.
- **Cardinal-invariant counterexamples.** Attempts to weaken CH in the Gruenhage–Nyikos construction to $\mathfrak{b}=\aleph_1$ or to the existence of a Luzin-type gap are active but unpublished *(frontier — verify)*.
- Groups: Toronto (Tall), Charlotte (Dow), Miami University (Larson), Paris/Toronto (Todorcevic), Auburn (Gruenhage, emeritus).

## 8. Future Work

- Determine the consistency strength and forcing-axiom status: does PFA decide Katětov's problem? Does $\mathrm{MA}_{\aleph_1}$?
- Isolate a single combinatorial statement (a partition or gap principle on $\omega_1$) provably equivalent to the positive answer, as Todorcevic's $\mathrm{OCA}$-style dichotomies do for other compactness problems.
- Weaken CH in the counterexample to a cardinal-invariant hypothesis, ideally one compatible with $\mathfrak{c}>\aleph_1$.
- Extend the $\mathrm{MA}(S)[S]$ results to hereditarily normal $X\times Y$ for non-homeomorphic compacta, where even the analogue of Katětov's lemma is not fully exploited.
- Settle the perfectly-normal-compacta basis problem, which would subsume much of the above.

## 9. Key References

- **[Foundational]** M. Katětov. *Complete normality of Cartesian products.* Fundamenta Mathematicae 35 (1948), 271–274; correction, Fund. Math. 40 (1953), 203–205.
- **[Foundational]** V. E. Šneĭder. *Continuous images of Suslin and Borel sets; metrization theorems.* Doklady Akad. Nauk SSSR 50 (1945), 77–79.
- **[Foundational]** V. V. Fedorchuk. *Fully closed mappings and the consistency of some theorems of general topology with the axioms of set theory.* Mathematics of the USSR–Sbornik 28 (1976), 3–33.
- **[SOTA]** G. Gruenhage, P. Nyikos. *Normality in $X^2$ for compact $X$.* Transactions of the American Mathematical Society 340 (1993), 563–586.
- **[SOTA]** P. Larson, S. Todorcevic. *Katětov's problem.* Transactions of the American Mathematical Society 354 (2002), 1783–1791.
- **[SOTA / Recent]** A. Dow, F. D. Tall. *Hereditarily normal manifolds of dimension $>1$ may all be metrizable.* Transactions of the American Mathematical Society 372 (2019), 6805–6851.
- **[Related]** P. Larson, S. Todorcevic. *Chain conditions in maximal models.* Fundamenta Mathematicae 168 (2001), 77–104.
- **[Survey]** G. Gruenhage. *Perfectly normal compacta, cosmic spaces, and some partition problems.* In: Open Problems in Topology (J. van Mill, G. M. Reed, eds.), North-Holland, 1990.
- **[Survey]** G. Gruenhage, J. T. Moore. *Perfect compacta and basis problems in topology.* In: Open Problems in Topology II (E. Pearl, ed.), Elsevier, 2007, 151–159.
- **[Reference]** R. Engelking. *General Topology*, revised ed., Heldermann Verlag, 1989.

## 10. Worked Example / Concrete Special Case

**The double arrow (split interval) space.** Let
$$A = \big((0,1]\times\{0\}\big)\cup\big([0,1)\times\{1\}\big)$$
with the order topology from the lexicographic order $(x,i)<(y,j)$ iff $x<y$, or $x=y$ and $i<j$.

*Facts.* $A$ is compact, zero-dimensional, first countable, separable, hereditarily Lindelöf, hence **perfectly normal**; and $A$ is **non-metrizable** (it is separable but not second countable: the clopen sets $[(x,1),\to)$ for $x\in(0,1)$ form an uncountable pairwise-incomparable family). So $A$ satisfies exactly the conclusion Katětov's lemma extracts from "$X^2$ hereditarily normal," yet is not metrizable. The square hypothesis must therefore do all the remaining work.

*Claim: $A^2$ is not hereditarily normal (ZFC).* Put
$$D=\{\,\big((x,0),(x,1)\big) : x\in(0,1)\,\},\qquad |D|=\mathfrak{c}.$$

1. **$D$ is discrete.** For $p=((x,0),(x,1))$ take $U=[(x,0),(x+\varepsilon,0)]$ and $V=[(x-\varepsilon,1),(x,1)]$. If $((y,0),(y,1))\in U\times V$ then $y\ge x$ from $U$ and $y\le x$ from $V$, so $y=x$.
2. **Closure of $D$ lies on the diagonal.** If $((x,i),(y,j))\in\overline D$, every basic box around it meets $D$, forcing $|x-y|<\varepsilon$ for all $\varepsilon>0$, so $x=y$. Hence $\overline D\subseteq \Delta'=\{((x,i),(x,j))\}$.
3. **A separable subspace.** Let $C=\{((p,0),(q,0)) : p,q\in\mathbb{Q}\cap(0,1),\ p\ne q\}$. Since $\{(q,0):q\in\mathbb{Q}\}$ is dense in $A$, $C$ is countable and dense in $A^2$; and $C\cap\Delta'=\varnothing$, so by (2) $C\cap\overline D=\varnothing$.
4. Put $Y=C\cup D$. Then $Y$ is separable (dense $C$), and $D$ is closed in $Y$ by (3) and discrete by (1), with $|D|=\mathfrak c$.
5. **Jones's lemma.** If $Y$ is normal and separable and $D\subseteq Y$ is closed discrete, then $2^{|D|}\le 2^{\aleph_0}$. Here that reads $2^{\mathfrak c}\le 2^{\aleph_0}$, contradicting Cantor's theorem.

Hence $Y$ is not normal, so $A^2$ is not hereditarily normal. $\blacksquare$

*Reading.* The obstruction is the anti-diagonal $D$: a $\mathfrak c$-sized discrete set living in the square of a separable space. Every known ZFC-provable perfectly normal non-metrizable compactum carries such a set, which is why no ZFC counterexample to Katětov's problem is available. The CH construction of Gruenhage–Nyikos manufactures a compactum of weight $\aleph_1$ whose anti-diagonals are all *small enough* to be separated; the $\mathrm{MA}(S)[S]$ model of Larson–Todorcevic shows that consistently no such compactum exists at all.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*