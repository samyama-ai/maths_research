---
id: 08-logic-set-theory/covering-lemma-for-extender-models
title: "Covering Lemma for Extender Models"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Covering Lemma for Extender Models

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/covering-lemma-for-extender-models` · **Status:** open

## 1. Problem Statement / Conjecture

Jensen's Covering Lemma says: if $0^{\\#}$ does not exist, then every uncountable set $X$ of ordinals is contained in some $Y \in L$ with $|Y| = |X|$. The problem is to extend this to **extender models** — the fine-structural inner models $L[\vec E]$ that carry large cardinals.

**Central open question.** Let $\mathcal{A}$ be an anti-large-cardinal hypothesis strictly weaker than the existence of a supercompact, e.g.

$$\mathcal{A}_{\mathrm{sup}} : \quad \text{there is no inner model with a superstrong cardinal.}$$

Assume $\mathcal{A}_{\mathrm{sup}}$. Does there exist a definable, iterable extender model $K$ (the *core model*) such that

$$\text{(Weak Covering)}\qquad \forall \lambda \ \big(\lambda \text{ a singular cardinal} \ \Longrightarrow\ (\lambda^{+})^{K} = \lambda^{+}\big)?$$

A complete solution requires: (i) a construction of $K$ from $\mathcal{A}$, (ii) a proof that $K$ is $\Sigma_2$-definable, generically absolute, and iterable, and (iii) a proof of weak covering at every singular $\lambda$, including $\lambda$ of cofinality $\omega$ and $\lambda$ below the first measurable. A disproof would exhibit a model of $\mathcal{A}$ in which every candidate $K$ computes some successor incorrectly. The statement is currently a **theorem below one Woodin cardinal** and **open at every level at or above it**.

Strong covering (in Jensen's original form) is *false* for all extender models past $L$; see §10. The correct general formulations are weak covering and covering *modulo systems of indiscernibles*.

## 2. Mathematical Foundations

**Extenders.** For transitive $M \models \mathrm{ZFC}^-$ and $\kappa < \nu$, a $(\kappa,\nu)$-extender over $M$ is a system $E = \langle E_a : a \in [\nu]^{<\omega}\rangle$ where each $E_a$ is a $\kappa$-complete ultrafilter on $[\kappa]^{|a|} \cap M$, coherent and satisfying normality, so that the direct limit
$$i_E : M \longrightarrow \mathrm{Ult}(M,E) \cong \varinjlim_a \mathrm{Ult}(M,E_a)$$
is elementary with $\mathrm{crit}(i_E)=\kappa$ and $\nu \le i_E(\kappa)$. Write $\mathrm{lh}(E)$ for the length.

**Extender models.** $L[\vec E]$ is built from a coherent sequence $\vec E = \langle E_\alpha : \alpha \in \mathrm{dom}(\vec E)\rangle$ satisfying the Mitchell–Steel indexing and initial-segment conditions: each $E_\alpha$ is an extender over $J^{\vec E \restriction \alpha}_\alpha$, and $i_{E_\alpha}(\vec E \restriction \alpha)\restriction(\alpha+1) = \vec E\restriction \alpha ^\frown \emptyset$. Levels $\mathcal{M} = (J^{\vec E}_\alpha, \in, \vec E\restriction\alpha, E_\alpha)$ are **premice**; a premouse all of whose countable elementary submodels are $\omega_1+1$-iterable (every iteration tree has a cofinal wellfounded branch) is a **mouse**.

**Fine structure.** Each level admits projecta $\rho_n(\mathcal M)$, standard parameters $p_n(\mathcal M)$, and $\Sigma_n$-hulls; solidity and universality of $p_n$ give **condensation**: if $\pi : \mathcal{H} \to \mathcal{M}$ is $\Sigma_1$-elementary with $\mathcal{H}$ countable, then $\mathcal H$ is an initial segment of $\mathcal M$ or of an ultrapower of one.

**Core model.** Under an anti-large-cardinal hypothesis $\mathcal{A}$, one runs the maximal *background-certified* construction $K^c$ and defines $K$ as the common core of its iterable levels. Steel's $K$ (below one Woodin, with a measurable $\Omega$) satisfies: $K$ is universal, rigid, $\Sigma_2$-definable, and $K^{V[g]}=K^V$ for set forcing $g$.

**Covering variants.** For an inner model $W$:
- *Strong covering*: every uncountable $X \subseteq \mathrm{Ord}$ has $Y \in W$, $X\subseteq Y$, $|Y|=|X|$.
- *Weak covering*: $(\lambda^+)^W = \lambda^+$ for all singular cardinals $\lambda$.
- *Covering modulo indiscernibles*: strong covering holds in $W[C]$ for a generic system $C$ of Prikry-like sequences.

Weak covering has the standard corollary $\square$-type combinatorics transfer and, via Solovay, the failure of SCH implies inner models with measurables of high Mitchell order.

## 3. History & State of the Art (SOTA)

- **1974/75.** Jensen proves covering for $L$ (Devlin–Jensen, *Marginalia to a theorem of Silver*). Immediate consequences: $\neg 0^\\#$ implies SCH, and Silver's singular cardinal results.
- **1981–82.** Dodd and Jensen build $K^{\mathrm{DJ}}$ (the core model below a measurable) and prove covering for it, plus covering for $L[U]$ **modulo a Prikry sequence**.
- **1984.** Mitchell's $K$ for sequences of measures, with covering modulo a *system of indiscernibles*, up to $o(\kappa)=\kappa^{++}$.
- **1994.** Mitchell–Steel, *Fine Structure and Iteration Trees*: extender models with Woodin cardinals; the modern indexing.
- **1996.** Steel, *The Core Model Iterability Problem*: $K$ exists assuming no inner model with a Woodin cardinal plus a measurable $\Omega$; weak covering at $\lambda$ with $\mathrm{cf}(\lambda)>\omega$ and countable closure.
- **1995–97.** Mitchell–Schimmerling remove countable closure; Mitchell–Schimmerling–Steel prove weak covering "up to a Woodin cardinal" in full.
- **1999.** Schimmerling–Steel, *The maximality of the core model*: $K$ is maximal, closing the theory below one Woodin.
- **2001–02.** Andretta–Neeman–Steel: domestic levels of $K^c$ are iterable (below superstrong); Neeman: iterability in the region of a Woodin limit of Woodins.
- **2010–17.** Woodin's suitable extender models and the HOD Dichotomy give a *covering-type* theorem above an extendible cardinal; Sargsyan's hod mice push descriptive-set-theoretic core model theory to $\mathrm{AD}_{\mathbb R}+\Theta$ regular.
- **2013.** Jensen–Steel, *K without the measurable*: removes the measurable $\Omega$ from the hypothesis.

## 4. Partial Results / Verified Cases

| Level | Hypothesis | Covering result |
|---|---|---|
| $L$ | $\neg 0^\\#$ | Strong covering (Jensen 1975) |
| $K^{\mathrm{DJ}}$ | no inner model with a measurable | Strong covering (Dodd–Jensen 1982) |
| $L[U]$ | no inner model with two measurables | Covering modulo one Prikry sequence (Dodd–Jensen 1982) |
| $\vec U$-sequences, $o(\kappa)<\kappa^{++}$ | no inner model with $o(\kappa)=\kappa^{++}$ | Covering modulo a system of indiscernibles (Mitchell 1984) |
| Below a strong cardinal | no inner model with a strong | Weak covering (Mitchell, Schimmerling, Zeman) |
| Below one Woodin | no inner model with a Woodin, $\Omega$ measurable | Weak covering: $(\lambda^+)^K=\lambda^+$ for all singular $\lambda<\Omega$, all cofinalities (MSS 1997) |
| Below one Woodin | as above, $\mathrm{cf}(\lambda)=\omega$, no countable closure | Weak covering (Mitchell–Schimmerling 1995) |
| Below one Woodin | no measurable assumed | $K$ exists, weak covering (Jensen–Steel 2013) |
| Tame mice / domestic $K^c$ | no superstrong | Iterability of $K^c$ levels (Andretta–Neeman–Steel 2001) — **$K$ itself not constructed** |
| $\mathrm{HOD}$ | $\kappa$ extendible | $(\lambda^+)^{\mathrm{HOD}}=\lambda^+$ for singular $\lambda>\kappa$ (Woodin's HOD Dichotomy) |

Thus weak covering is a theorem for every $\lambda \ge \aleph_2$ under "no inner model with a Woodin cardinal", and is unknown for any $\mathcal A$ weaker than that.

## 5. Principal Obstacles

1. **The iterability problem.** Defining $K$ needs $\omega_1+1$-iterability for countable premice. Martin–Steel's branch-uniqueness argument requires trees whose extenders do not overlap badly; past a superstrong, iteration trees admit long extenders with $\mathrm{crit}(E) < \mathrm{lh}(F) $ patterns for which no known strategy picks a canonical branch. No absolutely definable iteration strategy is known at the superstrong level.
2. **Failure of the anti-large-cardinal covering argument.** The proof of weak covering below one Woodin is a reductio: if $(\lambda^+)^K<\lambda^+$, one builds a "bad" $\Sigma_1$-hull and iterates it to contradict universality. This needs $K$ to be *universal* — comparable with every extender model — which is proved by a Woodin-cardinal-free reflection. With a Woodin in play, comparison need not terminate.
3. **Condensation breaks.** Solidity/universality of standard parameters (Mitchell–Steel, Schindler–Zeman) is proved by induction on mouse complexity; at long extenders the "$\Sigma_1$-hull is an initial segment" step fails, so the interpolation lemma used in every covering proof has no substitute.
4. **Genuine counterexamples to strong covering.** Prikry, Magidor and Radin forcings add cofinal sequences not covered by ground-model sets of small size (§10). Any general theorem must therefore be *weak*, and the bookkeeping of indiscernible systems grows combinatorially unmanageable past $o(\kappa)=\kappa^{++}$.
5. **No canonical model past supercompact.** Woodin's work suggests only an *Ultimate-L*-style model can carry a supercompact, and its existence is itself conjectural; there is no candidate $L[\vec E]$ whose covering could be analysed.

## 6. The Gap

Proven: an anti-large-cardinal hypothesis at the level of one Woodin cardinal yields $K$ with weak covering. Wanted: the same at the level of superstrong, or of a Woodin limit of Woodins, or ultimately no supercompact.

The exact step to cross is: **produce a $\Sigma_2$-definable, generically absolute, universal core model $K$ from "there is no inner model with a superstrong cardinal".** All the covering machinery (interpolation, hull condensation, the reductio at $\lambda^+$) is known to relativize once such a $K$ is in hand; what is missing is the iterability of $K^c$ for non-domestic levels and the termination of comparison. Equivalently: solve the *core model iterability problem* past superstrong.

## 7. Current Research (as of June 2026)

- **Münster school** (Schindler, Schlutzenberg, Fuchs, Müller): iterability from long extenders, $\mathsf{MM}^{++}$ and core-model-induction applications; Schlutzenberg's work on the self-iterability and definability of $\mathrm{Ult}(V,j)$-style models is the most active thread. *(frontier — verify)*
- **Berkeley/UCLA** (Steel, Sargsyan and collaborators, now partly at IMPAN Warsaw): the Least Branch Hierarchy (lbr-hod mice), which merges hod-mouse and extender-model methods and is the leading candidate for a $K$ past superstrong. Steel's *A Comparison Process for Mouse Pairs* (2022) is the reference text. *(frontier — verify)*
- **Core model induction** as the working substitute: rather than a global $K$, one proves weak-covering-strength consequences level by level from determinacy hypotheses (Sargsyan, Steel, Trang).
- **Ultimate-L programme** (Woodin): the $V=\mathrm{Ultimate}\text{-}L$ axiom would provide a covering-type analysis at all levels via the HOD Dichotomy; contingent on the $\Omega$-conjecture and the HOD Conjecture.
- Applications keep the problem live: Cox's covering theorems for stationary set reflection, and the derivation of failures of $\square$ and SCH from weak covering.

## 8. Future Work

- Prove iterability for *non-domestic* $K^c$ levels: find a canonical branch condition for trees with overlapping long extenders (Neeman's $\Sigma$-guided strategies extended past a Woodin limit of Woodins).
- Establish a comparison theorem for **mouse pairs** (model + strategy) strong enough to yield universality of an lbr-hod $K$; then transplant the MSS reductio verbatim.
- Isolate the weakest hypothesis for which weak covering *provably* fails, if any — currently none is known, so the answer may be "weak covering holds outright for the right $K$".
- Settle whether weak covering for $\mathrm{HOD}$ can be proved from hypotheses well below extendibility, decoupling covering from the HOD Conjecture.
- Develop a covering theory for models of $\mathrm{AD}^{+}$-derived hod mice, where comparison is by strategy rather than by extender.

## 9. Key References

- **[Foundational]** K. Devlin and R. B. Jensen. *Marginalia to a theorem of Silver.* In: Logic Colloquium '73, Lecture Notes in Mathematics 499, Springer, 1975.
- **[Foundational]** A. Dodd and R. B. Jensen. *The core model.* Annals of Mathematical Logic 20 (1981), 43–75.
- **[Foundational]** A. Dodd and R. B. Jensen. *The covering lemma for K.* Annals of Mathematical Logic 22 (1982), 1–30; and *The covering lemma for L[U].* Annals of Mathematical Logic 22 (1982), 127–135.
- **[Foundational]** W. J. Mitchell. *The core model for sequences of measures I.* Mathematical Proceedings of the Cambridge Philosophical Society 95 (1984), 229–260.
- **[Foundational]** W. J. Mitchell and J. R. Steel. *Fine Structure and Iteration Trees.* Lecture Notes in Logic 3, Springer, 1994.
- **[SOTA]** J. R. Steel. *The Core Model Iterability Problem.* Lecture Notes in Logic 8, Springer, 1996.
- **[SOTA]** W. J. Mitchell and E. Schimmerling. *Weak covering without countable closure.* Mathematical Research Letters 2 (1995), 595–609.
- **[SOTA]** W. J. Mitchell, E. Schimmerling and J. R. Steel. *The covering lemma up to a Woodin cardinal.* Annals of Pure and Applied Logic 84 (1997), 219–255.
- **[SOTA]** E. Schimmerling and J. R. Steel. *The maximality of the core model.* Transactions of the American Mathematical Society 351 (1999), 3119–3141.
- **[SOTA]** A. Andretta, I. Neeman and J. R. Steel. *The domestic levels of $K^c$ are iterable.* Israel Journal of Mathematics 125 (2001), 157–201.
- **[SOTA]** I. Neeman. *Inner models in the region of a Woodin limit of Woodins.* Annals of Pure and Applied Logic 116 (2002), 67–155.
- **[SOTA]** R. B. Jensen and J. R. Steel. *K without the measurable.* Journal of Symbolic Logic 78 (2013), 708–734.
- **[SOTA]** G. Sargsyan. *Hod Mice and the Mouse Set Conjecture.* Memoirs of the American Mathematical Society 236, 2015.
- **[SOTA]** J. R. Steel. *A Comparison Process for Mouse Pairs.* Lecture Notes in Logic 51, Cambridge University Press, 2022.
- **[Survey]** W. J. Mitchell. *The covering lemma.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 2010, 1497–1594.
- **[Survey]** R. Schindler and M. Zeman. *Fine structure.* In: Handbook of Set Theory, Springer, 2010, 605–656.
- **[Survey]** E. Schimmerling. *The ABC's of mice.* Bulletin of Symbolic Logic 7 (2001), 485–503.
- **[Survey]** M. Zeman. *Inner Models and Large Cardinals.* de Gruyter Series in Logic and its Applications 5, 2002.
- **[Context]** W. H. Woodin. *Suitable extender models I.* Journal of Mathematical Logic 10 (2010), 101–339; and *In search of Ultimate-L.* Bulletin of Symbolic Logic 23 (2017), 1–109.
- **[Application]** S. Cox. *Covering theorems for the core model, and an application to stationary set reflection.* Annals of Pure and Applied Logic 161 (2010), 66–93.

## 10. Worked Example / Concrete Special Case

**Prikry forcing over $L[U]$: strong covering fails, weak covering survives.**

Let $V = L[U]$ where $U$ is a normal measure on $\kappa$. Prikry forcing $\mathbb P_U$ has conditions $(s,A)$ with $s\in[\kappa]^{<\omega}$, $A\in U$, $\max(s)<\min(A)$, ordered by $(t,B)\le(s,A)$ iff $t\supseteq s$, $B\subseteq A$, $t\setminus s\subseteq A$. Let $G$ be generic and $C=\bigcup\{s : (s,A)\in G\}=\{\kappa_n : n<\omega\}$, increasing and cofinal in $\kappa$. Work in $W=L[U][G]$.

*Strong covering fails.* Suppose $Y\in L[U]$, $Y\subseteq\kappa$, $|Y|^{L[U]}<\kappa$, and $C\subseteq Y$. Since $U$ is $\kappa$-complete and nonprincipal, every set of $L[U]$-size $<\kappa$ is $U$-null, so $Y\notin U$, hence $A:=\kappa\setminus Y\in U$. By the genericity of $C$ (the *Prikry property*: for each $A\in U$, the set of conditions $(s,B)$ with $B\subseteq A$ is dense), $C\setminus\max(s)\subseteq A$ for some finite $s$ — i.e. $C\subseteq^{*}A=\kappa\setminus Y$, contradicting $C\subseteq Y$ with $C$ infinite. So the countable set $C$ has **no** $L[U]$-cover of size $<\kappa$. Extending $C$ to a set of size $\aleph_1$ by adding an interleaved $\aleph_1$-sequence gives an uncountable $X$ with no $L[U]$-cover of the same cardinality: Jensen-style covering is outright false for $L[U]$.

*Weak covering holds.* $\mathbb P_U$ has the *Prikry property*: for every sentence $\sigma$ and condition $(s,A)$ there is $B\subseteq A$, $B\in U$, with $(s,B)$ deciding $\sigma$. Together with $\kappa^{+}$-c.c. (there are only $2^{\kappa}=\kappa^{+}$ conditions in $L[U]$, and any two with the same stem are compatible, so the antichain bound is $\kappa$ many stems), this gives: no new bounded subsets of $\kappa$, and all cardinals preserved. Hence
$$(\kappa^{+})^{L[U]} = (\kappa^{+})^{W},\qquad \mathrm{cf}^{W}(\kappa)=\omega .$$
So $\kappa$ becomes singular but the successor is computed correctly.

*What this shows.* The correct general statement is weak covering, and the Dodd–Jensen repair is *covering modulo indiscernibles*: every $X$ is covered by a set in $L[U][C]$ of the same size. The open problem of §1 is whether, replacing $L[U]$ by an extender model with (say) superstrong-level extenders and $C$ by a Radin-like system of indiscernibles, the displayed equation $(\lambda^{+})^{K}=\lambda^{+}$ can still be proved for every singular $\lambda$. Below one Woodin cardinal it can (MSS 1997); above, both the model $K$ and the proof are missing.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*