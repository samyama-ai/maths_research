---
id: 08-logic-set-theory/i2-cardinals-existence
title: "I2 Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# I2 Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/i2-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The axiom **I2** asserts:

> There is a nontrivial elementary embedding $j : V \to M$ of the set-theoretic universe into a transitive class $M$ such that $V_\lambda \subseteq M$, where $\lambda = \sup_{n<\omega} \kappa_n$ with $\kappa_0 = \operatorname{crit}(j)$ and $\kappa_{n+1} = j(\kappa_n)$.

The open problem is twofold.

1. **Consistency.** Is $\mathrm{ZFC} + \mathrm{I2}$ consistent? No proof of $\mathrm{Con}(\mathrm{ZFC}) \to \mathrm{Con}(\mathrm{ZFC}+\mathrm{I2})$ can exist (Gödel), so what is wanted is either (a) an inconsistency proof, extending Kunen's method past the $V_{\lambda+2}$ barrier, or (b) structural evidence of the kind that legitimised measurable and supercompact cardinals — a canonical inner model, a fine-structural analysis, or a robust forcing theory.
2. **Exact location.** Pin down I2 in the consistency-strength order relative to its neighbours I3, I1, I0, the Wholeness Axiom, and $n$-huge cardinals, and determine whether I2 is equivalent to a statement about $V_\lambda$ alone.

A complete resolution of (1) is either a $\mathrm{ZFC}$-refutation of the displayed sentence or a reduction of its consistency to an accepted hypothesis. The status is *partially-solved*: the hierarchy placement, several equivalent formulations, and many consequences are theorems; consistency is not.

## 2. Mathematical Foundations

Work in $\mathrm{ZFC}$ with the cumulative hierarchy $V_0=\emptyset$, $V_{\alpha+1}=\mathcal P(V_\alpha)$, $V_\gamma=\bigcup_{\alpha<\gamma}V_\alpha$.

**Critical sequence.** For a nontrivial elementary $j$ with $\operatorname{crit}(j)=\kappa_0$, set $\kappa_{n+1}=j(\kappa_n)$ and
$$\lambda \;=\; \lambda_j \;=\; \sup_{n<\omega}\kappa_n .$$
Then $j(\lambda)=\lambda$, $\operatorname{cf}(\lambda)=\omega$, and $\lambda$ is a strong limit cardinal.

**Kunen's inconsistency (1971).** In $\mathrm{ZFC}$ there is no nontrivial elementary $j:V\prec M$ with $V_{\lambda_j+2}\subseteq M$; in particular no $j:V\prec V$. The proof uses an $\omega$-Jónsson function $f:[\lambda]^\omega\to\lambda$ (Erdős–Hajnal): if $V_{\lambda+2}\subseteq M$ then $j(f)=f$ on a set forcing $f$ to omit a value on $j''\lambda$, a contradiction.

**The rank-into-rank hierarchy**, all with $\lambda$ the critical sequence supremum:
- **I3:** $\exists\, j : V_\lambda \prec V_\lambda$, $j \neq \mathrm{id}$.
- **I2:** $\exists\, j : V \prec M$, $V_\lambda \subseteq M$.
- **I1:** $\exists\, j : V_{\lambda+1} \prec V_{\lambda+1}$, $j \neq \mathrm{id}$.
- **I0:** $\exists\, j : L(V_{\lambda+1}) \prec L(V_{\lambda+1})$ with $\operatorname{crit}(j)<\lambda$.

$$\mathrm{I0}\;\Longrightarrow\;\mathrm{I1}\;\Longrightarrow\;\mathrm{I2}\;\Longrightarrow\;\mathrm{I3},$$
each implication strict in consistency strength (Kanamori, *The Higher Infinite*, §24). I2 is exactly the last surviving "$j:V\to M$ with rank-segment closure" statement below Kunen's $V_{\lambda+2}$ wall: $V_\lambda\subseteq M$ is permitted, $V_{\lambda+2}\subseteq M$ is refutable.

**Second-order characterisation (Martin; Kanamori §24).** I2 holds iff there is $j:V_\lambda\prec V_\lambda$ which is *$\Sigma^1_1$-elementary*: for every $\Sigma^1_1$ formula $\varphi$ over $\langle V_\lambda,\in\rangle$ and every $A\in V_{\lambda+1}$,
$$\langle V_\lambda,\in,A\rangle \models \varphi \iff \langle V_\lambda,\in,j_+(A)\rangle \models \varphi ,\qquad j_+(A)=\textstyle\bigcup_{\alpha<\lambda} j(A\cap V_\alpha).$$
Thus I2 is a statement about $V_{\lambda+1}$: it is I3 plus a definable degree of extendibility of $j$ to subsets of $V_\lambda$. I1 is the same demand for full second-order elementarity.

**Derived ultrafilters.** For $j$ witnessing I2 and $X \subseteq \mathcal P(\kappa_n)$,
$$U_n=\{\,X\subseteq \mathcal P(\kappa_{n}) \;:\; j''\kappa_{n}\in j(X)\,\}$$
is a $\kappa_0$-complete normal fine ultrafilter, because $j''\kappa_n\subseteq \kappa_{n+1}\subseteq V_\lambda\subseteq M$.

## 3. History & State of the Art (SOTA)

- **1967–1970.** Reinhardt proposed $j:V\prec V$ as the limiting large-cardinal axiom.
- **1971.** Kunen refuted it in $\mathrm{ZFC}$ (JSL 36), leaving I0–I3 as the strongest hypotheses not known to be inconsistent. The $V_{\lambda+1}$/$V_{\lambda+2}$ gap has not moved in 55 years.
- **1974–1978.** Gaifman, and Solovay–Reinhardt–Kanamori (*Ann. Math. Logic* 13, 1978), organised the hierarchy, fixed the notation I0–I3, and proved the basic implications and non-reversibilities.
- **1980.** Martin derived $\Pi^1_2$-determinacy from an iterable rank-into-rank–type hypothesis in the I2 neighbourhood — the first serious *application*. It was later superseded: Martin–Steel and Woodin reproved $\Pi^1_2$-determinacy from a Woodin cardinal with a measurable above, far below I2.
- **1989–1997.** Laver's algebraic era: the iterates of an I3 embedding under application generate the free left-distributive algebra on one generator (*Adv. Math.* 91, 1992), giving the first decision procedure for the free LD word problem. Dougherty (1993) and Dougherty–Jech (1997) quantified the associated finite structures.
- **1997–2001.** Laver proved rank-into-rank embeddings lift through suitably closed forcing; Corazza isolated the Wholeness Axiom $\mathrm{WA}$ (a $j:V\prec V$ with separation only for $j$-free formulas), strictly between super-$n$-huge for all $n$ and I3; Hamkins showed $\mathrm{WA}$ is consistent with $V=\mathrm{HOD}$.
- **2010–present.** Woodin's I0 programme (*Suitable Extender Models I*) revealed that $L(V_{\lambda+1})$ under I0 mirrors $L(\mathbb R)$ under $\mathrm{AD}$ — the strongest structural evidence for the whole family, I2 included. Dimonte's 2018 survey is the standard reference.

## 4. Partial Results / Verified Cases

Established theorems (all in $\mathrm{ZFC}$ unless noted):

- **Upper bound is sharp at $V_{\lambda+2}$.** Kunen: closure of $M$ under $V_{\lambda+2}$ is refutable; I2's $V_\lambda$-closure is not. No known argument reaches $V_{\lambda+1}$.
- **Hierarchy placement.** $\mathrm{I1}\Rightarrow$ there are many $\bar\lambda<\lambda$ at which I2 holds, so $\mathrm{Con}(\mathrm{I1})>\mathrm{Con}(\mathrm{I2})>\mathrm{Con}(\mathrm{I3})$; and $\mathrm{I3}\Rightarrow \kappa_0$ is $n$-huge for every $n<\omega$, so I2 dwarfs the huge hierarchy.
- **Equivalence.** I2 $\iff$ $\Sigma^1_1$-elementary $j:V_\lambda\prec V_\lambda$ (Martin) — a *local* reformulation, verified for the parameter class $V_{\lambda+1}$.
- **Free LD algebras.** Laver (1992): $\{j_k\}$ generated from an I3 embedding under $a\cdot b$ is free left-distributive; consequence: the word problem for one-generated free LD algebras is decidable. Later given a $\mathrm{ZFC}$ proof by Dehornoy via braid orderings — an I2/I3-motivated theorem *removed* from large cardinals.
- **Laver tables.** For the finite quotients $A_n$ ($2^n$ elements), the period $p(n)$ of the first row satisfies $p(n)\to\infty$ — proved from I3, still open in $\mathrm{ZFC}$. Dougherty: the least $n$ with $p(n)\ge 32$ exceeds $\mathrm{Ack}(9,\mathrm{Ack}(8,\mathrm{Ack}(8,255)))$; verified computationally $p(n)\le 16$ for all feasible $n$.
- **Forcing.** Laver (1997) and Corazza: I3/I1-type embeddings survive $<\kappa_0$-directed closed forcing and Laver-style preparations. Dimonte–Wu (2016) produced models of I1 with $2^\lambda>\lambda^+$, i.e. GCH can fail at $\lambda$.
- **Choiceless fragment.** Without AC, Kunen's proof breaks. Schlutzenberg showed $\mathrm{ZF}$ alone refutes $j:V_{\lambda+2}\prec V_{\lambda+2}$; Goldberg's "even ordinals" method gives further $\mathrm{ZF}$ Kunen-type refutations. Reinhardt cardinals remain open in $\mathrm{ZF}$.

## 5. Principal Obstacles

- **No inner-model theory.** Fine structure and extender models are constructed at the level of Woodin cardinals and, conjecturally, up to supercompactness (Woodin's ultimate-$L$ programme). There is no candidate $L$-like model for I2. Comparison arguments rely on iteration trees built from extenders in $V_{\lambda}$; an I2 embedding is not captured by any $\lambda$-extender, since the closure $V_\lambda \subseteq M$ is precisely the amount of information a $(\kappa,\lambda)$-extender loses.
- **Kunen's method saturates.** The $\omega$-Jónsson function argument needs $j''\lambda$, an element of $V_{\lambda+1}$, to be recognised *inside* $M$ together with the function $f\in V_{\lambda+2}$. With only $V_\lambda\subseteq M$, neither $j\restriction V_\lambda$ nor $j''\lambda$ need be in $M$ in a usable way, and every known combinatorial witness (Jónsson, Erdős–Hajnal, Woodin's variant) lives at $V_{\lambda+2}$.
- **$\operatorname{cf}(\lambda)=\omega$ blocks reflection.** Standard reflection and elementary-substructure arguments require uncountable cofinality or $\lambda$-closure of ultrapowers; here $\lambda$ is a countable-cofinality strong limit and $^{\omega}\lambda \not\subseteq M$ can fail badly, so square, scale, and PCF machinery at $\lambda$ interacts with, rather than resolves, the axiom.
- **Consistency is unfalsifiable by construction.** Any consistency proof must come from a stronger axiom (I1, I0), which merely relocates the question; the only decidable outcome is inconsistency.
- **Descriptive-set-theoretic analogy is incomplete.** The $L(V_{\lambda+1})\leftrightarrow L(\mathbb R)$ analogy is proved for I0. I2 is too weak to run it, so the strongest evidence does not descend to the axiom in question.

## 6. The Gap

Proven: nothing above $V_{\lambda+2}$-closure is consistent; everything at or below I0 is consistent-as-far-as-known; I2 is strictly between I3 and I1 in strength and admits a $\Sigma^1_1$ local characterisation.

Unproven: whether the interval $[\mathrm{I3},\ V_{\lambda+2}\text{-closure})$ contains any inconsistency at all. The precise unbridged step is:

> Produce a $\mathrm{ZFC}$-definable structure $S \in V_{\lambda+1}$ (not $V_{\lambda+2}$) whose $j$-image is forced to contradict elementarity — or prove that no such $S$ exists, e.g. by showing every $\Sigma^1_1$-elementary $j:V_\lambda\prec V_\lambda$ is consistent relative to a weaker hypothesis.

Equivalently: is the second-order gap between "$j$ preserves $\Sigma^1_1$ facts about $V_\lambda$" (I2) and "$j$ preserves all second-order facts" (I1) a genuine consistency gap, or does one of the two collapse into contradiction?

## 7. Current Research (as of June 2026)

- **I0 structure theory.** Woodin, Cramer (inverse-limit reflection, *JML* 2015), Shi (higher degree theory under I0, *JSL* 2015), Dimonte, Shi. Programme: transfer the $L(\mathbb R)$/$\mathrm{AD}$ dictionary down the hierarchy; consequences for I2 are being extracted by restricting to $\Sigma^1_1$ fragments. *(frontier — verify)*
- **Choiceless Kunen boundary.** Goldberg, Schlutzenberg, Bagaria–Koellner–Woodin. Determining exactly which $j:V_\alpha\prec V_\alpha$ are $\mathrm{ZF}$-refutable is the most active line, and each new $\mathrm{ZF}$ refutation tightens the intuition about where an AC-free analogue of I2 sits. *(frontier — verify)*
- **Forcing and independence.** Dimonte, Wu, Friedman: generalised Baire space $\lambda^\lambda$ at rank-into-rank $\lambda$; preservation of I1/I2 under $\lambda$-Prikry-like and Radin-like forcings; controlling $2^\lambda$, $\Diamond$-principles and trees at $\lambda^+$ while keeping I2.
- **Algebraic/self-distributive.** Dehornoy, Lebed, and the Laver-table community: periodicity of $p(n)$ in $\mathrm{ZFC}$ remains the flagship open combinatorial shadow of I3/I2.
- **Institutions.** Berkeley (Woodin, Goldberg), Udine/Torino (Dimonte), Beijing AMSS (Wu, Shi), Münster (Schlutzenberg), Barcelona ICREA (Bagaria).

## 8. Future Work

- Search for an $\omega$-Jónsson-style obstruction using only sets in $V_{\lambda+1}$ coded by $j$-fixed points; Woodin's variants of the Kunen argument are the natural starting point.
- Develop extender-like representations for I2 embeddings — a "$V_\lambda$-closure extender" — which would be the entry point for comparison and hence for inner models.
- Settle whether I2 implies the existence of a transitive model of I3 *with the same $\lambda$*, sharpening the strictness of the hierarchy from consistency strength to direct implication.
- Prove $p(n)\to\infty$ for Laver tables in $\mathrm{ZFC}$: an unconditional proof would remove the last widely-cited "theorem needing I3", while a $\mathrm{ZFC}$-refutation of it would refute I3 and hence I2.
- Extend the $L(V_{\lambda+1})$ analogy to $L(V_{\lambda+1})$-fragments definable from $\Sigma^1_1$-elementary embeddings, giving I2 its own structural signature.

## 9. Key References

- **[Foundational]** Kunen, K. *Elementary embeddings and infinitary combinatorics.* Journal of Symbolic Logic 36 (1971), 407–413.
- **[Foundational]** Solovay, R. M., Reinhardt, W. N., Kanamori, A. *Strong axioms of infinity and elementary embeddings.* Annals of Mathematical Logic 13 (1978), 73–116.
- **[Foundational]** Gaifman, H. *Elementary embeddings of models of set theory and certain subtheories.* In: Axiomatic Set Theory, Proc. Sympos. Pure Math. 13 II, AMS, 1974.
- **[Survey]** Kanamori, A. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003 (§24: rank-into-rank axioms).
- **[Survey]** Dimonte, V. *I0 and rank-into-rank axioms.* Bollettino dell'Unione Matematica Italiana 11 (2018), 315–361.
- **[Foundational]** Laver, R. *The left distributive law and the freeness of an algebra of elementary embeddings.* Advances in Mathematics 91 (1992), 209–231.
- **[SOTA]** Dougherty, R. *Critical points in an algebra of elementary embeddings.* Annals of Pure and Applied Logic 65 (1993), 211–241.
- **[SOTA]** Dougherty, R., Jech, T. *Finite left-distributive algebras and embedding algebras.* Advances in Mathematics 130 (1997), 201–241.
- **[SOTA]** Laver, R. *Implications between strong large cardinal axioms.* Annals of Pure and Applied Logic 90 (1997), 79–90.
- **[SOTA]** Corazza, P. *The wholeness axiom and Laver sequences.* Annals of Pure and Applied Logic 105 (2000), 157–260.
- **[SOTA]** Hamkins, J. D. *The wholeness axioms and V=HOD.* Archive for Mathematical Logic 40 (2001), 1–8.
- **[SOTA]** Woodin, W. H. *Suitable extender models I.* Journal of Mathematical Logic 10 (2010), 101–339.
- **[SOTA]** Cramer, S. *Inverse limit reflection and the structure of $L(V_{\lambda+1})$.* Journal of Mathematical Logic 15 (2015).
- **[SOTA]** Shi, X. *Axiom I0 and higher degree theory.* Journal of Symbolic Logic 80 (2015), 970–1021.
- **[SOTA]** Dimonte, V., Wu, L. *A general tool for consistency results related to I1.* European Journal of Mathematics 2 (2016), 474–492.
- **[Recent]** Bagaria, J., Koellner, P., Woodin, W. H. *Large cardinals beyond choice.* Bulletin of Symbolic Logic 25 (2019), 283–318.
- **[Recent]** Goldberg, G. *Even ordinals and the Kunen inconsistency.* Journal of Mathematical Logic, 2024.

## 10. Worked Example / Concrete Special Case

**Claim.** If $j:V\prec M$ witnesses I2 with critical sequence $\kappa_0<\kappa_1<\cdots$, then $\kappa_0$ is $n$-huge for every $n<\omega$.

*Step 1 — locate $j''\kappa_n$.* Each $\kappa_n<\lambda$, so $\kappa_{n+1}\subseteq V_\lambda$. Since $j''\kappa_n\subseteq\kappa_{n+1}$ and $\lambda$ is a limit ordinal, $j''\kappa_n\in V_\lambda$. By I2's closure hypothesis $V_\lambda\subseteq M$, hence
$$j''\kappa_n \in M .$$
This is the whole content of the axiom being used; I3 alone does not hand it to you at the level of $V$.

*Step 2 — derive the measure.* Fix $n$ and put
$$U \;=\; \{\, X \subseteq \mathcal P(\kappa_n) \;:\; j''\kappa_n \in j(X) \,\}.$$
$U$ is well-defined by Step 1. It is an ultrafilter (elementarity: $j(\mathcal P(\kappa_n)\setminus X)=j(\mathcal P(\kappa_n))\setminus j(X)$), and $\kappa_0$-complete: if $\langle X_\alpha : \alpha<\gamma\rangle$ with $\gamma<\kappa_0$ are in $U$, then $j(\langle X_\alpha\rangle)=\langle j(X_\alpha)\rangle$ since $\operatorname{crit}(j)=\kappa_0>\gamma$, so $j''\kappa_n\in\bigcap_\alpha j(X_\alpha)=j(\bigcap_\alpha X_\alpha)$.

*Step 3 — fineness and normality.* For $\alpha<\kappa_n$, $\{\,x : \alpha\in x\,\}\in U$ because $j(\alpha)\in j''\kappa_n$; and if $f$ is regressive on a $U$-large set then $[f]_U<[\mathrm{id}]_U$ collapses to a constant by the usual Rowbottom argument. So $U$ is a normal fine $\kappa_0$-complete ultrafilter on $\mathcal P_{\kappa_0}(\kappa_n)$ concentrating on sets of order type $\kappa_{n-1}$-many below; the resulting ultrapower $i_U:V\to N\cong \mathrm{Ult}(V,U)$ has $\operatorname{crit}(i_U)=\kappa_0$, $i_U(\kappa_0)=\kappa_1$, and $^{\kappa_n}N\subseteq N$. That is exactly the definition of "$\kappa_0$ is $n$-huge with targets $\kappa_1,\dots,\kappa_n$".

*Step 4 — reflection.* $n$-hugeness of $\kappa_0$ is expressible in $V_{\kappa_0+2}$-parameters, so by elementarity $\{\alpha<\kappa_0 : \alpha \text{ is } n\text{-huge}\}$ is in the normal measure $\{X\subseteq\kappa_0 : \kappa_0\in j(X)\}$; in particular $\kappa_0$ is the $\kappa_0$-th $n$-huge cardinal for each fixed $n$.

*What the example shows.* One line of the axiom — $V_\lambda\subseteq M$ — instantly yields the entire $n$-huge hierarchy, which is why no consistency proof from below is possible. Pushing the same computation one rank higher, to $j''\lambda\in M$ with $V_{\lambda+2}\subseteq M$, is where Kunen's Jónsson function fires and the whole scheme collapses. I2 lives in the two ranks between these two facts, and nothing currently known decides that interval.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*