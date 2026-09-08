---
id: 08-logic-set-theory/definable-wellordering-chang-model
title: "Existence of a Definable Well-Ordering in the Chang Model"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existence of a Definable Well-Ordering in the Chang Model

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/definable-wellordering-chang-model` · **Status:** open

## 1. Problem Statement / Conjecture

The **Chang model** $C$ is the least inner model of ZF that contains all ordinals and is closed under countable sequences. Equivalently $C = L(\mathrm{Ord}^{\omega})$: the constructible closure of the class of all $\omega$-sequences of ordinals.

**Question.** For which large-cardinal or forcing-axiom hypotheses does $C$ carry a well-ordering of its universe that is definable in $C$ (by a single formula, with parameters from $C$)?

Three concrete forms of the problem:

1. **(Main)** Determine the exact consistency-strength boundary: the sup of the large-cardinal hypotheses compatible with $C \models \mathrm{AC}$, and the inf of those refuting it.
2. **(Local)** Is there a hypothesis $H$, strictly stronger than "$\omega_1$ measurable cardinals exist" and strictly weaker than "there is a proper class of Woodin limits of Woodin cardinals", under which $C \models \mathrm{AC}$? Or does $C \models \neg\mathrm{AC}$ already at the level of, say, a single strong cardinal?
3. **(Parameter-free)** When $C \models \mathrm{AC}$, is the well-ordering $\Sigma_n$-definable in $C$ without parameters, i.e. does $C \models V = \mathrm{HOD}$?

A complete solution is either (a) a proof from a specified hypothesis $H$ that $C$ has a definable well-ordering, together with a proof that $H$ is optimal, or (b) a proof that some hypothesis below the known determinacy threshold already yields $C \models \neg\mathrm{AC}$, again with optimality.

## 2. Mathematical Foundations

**Definition (Chang model).** Let $\mathrm{Ord}^{\omega}$ denote the class of functions $s:\omega\to\mathrm{Ord}$. Then
$$C \;=\; L\big(\mathrm{Ord}^{\omega}\big) \;=\; \bigcup_{\alpha\in\mathrm{Ord}} L_\alpha\big(\mathrm{Ord}^{\omega}\big),$$
where $L_0(A)=\mathrm{trcl}(A)$, $L_{\alpha+1}(A)=\mathrm{Def}(L_\alpha(A))$ and unions are taken at limits. Chang's original definition: $C$ is the class of sets constructible using the infinitary logic $L_{\omega_1\omega_1}$, i.e. the hierarchy obtained by replacing first-order definability with $L_{\omega_1\omega_1}$-definability.

**Basic facts.**
- $C \models \mathrm{ZF} + \mathrm{DC}$. Dependent choice holds because $C$ is closed under $\omega$-sequences: $({}^{\omega}C)\cap V \subseteq C$ for sequences of *ordinals*, and closure under countable sequences of elements of $C$ follows since each element is coded by a countable sequence of ordinals plus an ordinal.
- $C \models V = L(\mathrm{Ord}^{\omega})$. Hence every $x\in C$ is definable in $C$ from an ordinal and a countable sequence of ordinals:
$$C \models \forall x\,\exists \alpha\,\exists s\in\mathrm{Ord}^{\omega}\;\; x \in \mathrm{Def}\big(L_\alpha(\mathrm{Ord}^{\omega}),\{\alpha,s\}\big).$$

**Reduction lemma (why "definable well-ordering" $\equiv$ AC here).** Because $C\models V=L(A)$ with $A = \mathrm{Ord}^{\omega}$, the following are equivalent in $C$:
$$\mathrm{AC} \iff \exists\text{ a well-ordering of } \mathrm{Ord}^{\omega} \iff \forall\kappa\;\exists\text{ a well-ordering of } {}^{\omega}\kappa \iff \exists\text{ a formula-definable (with parameters) well-ordering of } V.$$
The last equivalence uses the standard $L(A)$ argument: a well-ordering $\vartriangleleft$ of $A$ lifts canonically, level by level along the $\mathrm{Def}$ hierarchy, to a definable global well-ordering with parameter $\vartriangleleft$. So the problem is *literally* the AC problem for $C$, with the extra refinement of parameter-freeness in item 3 of §1.

**Determinacy side.** $\mathbb{R}\subseteq C$ and $L(\mathbb{R})\subseteq C$. If $C \models \mathrm{AD}$ then $C\models\neg\mathrm{AC}$ and no definable well-ordering exists (a well-ordering of $\mathbb{R}$ in $C$ yields a non-determined set by the classical Bernstein-style construction, which uses only $\mathrm{DC}$ plus a well-ordering).

**Generalized Chang models.** For a cardinal $\kappa$, $C_\kappa = L(\mathrm{Ord}^{<\kappa})$, the least inner model closed under $<\kappa$-sequences; $C = C_{\omega_1}$. For a logic $\mathcal{L}^{*}$, $C(\mathcal{L}^{*})$ is the constructible hierarchy with $\mathrm{Def}$ replaced by $\mathcal{L}^{*}$-definability; $C = C(L_{\omega_1\omega_1})$.

## 3. History & State of the Art (SOTA)

- **1971 — Chang.** C. C. Chang introduces the model in *Sets constructible using $L_{\kappa\kappa}$*, asking whether AC holds in it and whether it equals $L$.
- **1970 — Kunen.** Using iterated ultrapowers, Kunen shows that if there are uncountably many ($\omega_1$-many) measurable cardinals, then $\mathrm{AC}$ fails in $C$. The measurables' critical sequence $\langle \kappa_\alpha : \alpha<\omega_1\rangle$ generates, inside $C$, an uncountable set of order-indiscernibles from which a non-well-orderable set is extracted. This is the first and still the crispest negative result.
- **1970s — the $L$ side.** If $V=L$ then every countable sequence of ordinals is in $L$, so $C=L$ and $<_L$ is a $\Sigma_1$ parameter-free well-ordering. The same holds under any hypothesis forcing $\mathrm{Ord}^{\omega}\subseteq L$-like core models (covering-type arguments).
- **1980s–1990s — Woodin.** From a proper class of Woodin cardinals, the theory of $L(\mathbb{R})$ is generically absolute and $L(\mathbb{R})\models\mathrm{AD}$; from a proper class of **Woodin limits of Woodin cardinals**, $C\models\mathrm{AD}$ — the strongest known negative answer, and it kills every definable well-ordering of $C$ outright.
- **2000s — inner model theory.** Steel's and Sargsyan's work on derived models and hod mice provides the machinery for computing $C$ (or approximating it) inside canonical models, where $\mathrm{AC}$ *does* hold; the difficulty is that the covering/comparison technology is only available well below the Woodin-limit-of-Woodins level.
- **2021 — Kennedy–Magidor–Väänänen.** *Inner models from extended logics* studies $C(\mathcal{L}^{*})$ for many logics; several of these models (notably $C^{*}$, built from the cofinality quantifier $Q^{\mathrm{cf}}_{\omega}$) provably satisfy $\mathrm{ZFC}$ with a definable well-ordering, in sharp contrast to $C=C(L_{\omega_1\omega_1})$. This isolates *closure under $\omega$-sequences of arbitrary ordinals* as the precise culprit.

## 4. Partial Results / Verified Cases

**Positive (definable well-ordering exists):**
- $V=L$, or more generally $V=L[x]$ for a real $x$: $C=L[x]$ with a $\Sigma_2$ well-ordering definable from $x$; parameter-free if $x$ is definable.
- Any set-forcing extension of $L$ by a poset $\mathbb{P}\in L$ of size $\le\aleph_0$ (e.g. Cohen, random, Sacks over $L$): $C = L[G]$, definable well-ordering with parameter $G$.
- Under $\neg 0^{\\#}$ (and more generally when the relevant core model $K$ exists and covering holds), $C$ is a small extension of $K$ and $C\models\mathrm{AC}$: verified through the region below "there is a measurable of Mitchell order $\kappa^{++}$", where $K$-theory is fully developed.
- Fewer than $\omega_1$ measurable cardinals: no known refutation; Kunen's argument needs the full uncountable sequence.
- Logic variants: $C(\mathcal{L}^{2})=\mathrm{HOD}$-like and $C^{*}$ satisfy ZFC with definable well-orderings (Kennedy–Magidor–Väänänen).

**Negative (no definable well-ordering):**
- $\omega_1$ measurable cardinals $\Rightarrow C\models\neg\mathrm{AC}$ (Kunen 1970).
- A proper class of Woodin limits of Woodin cardinals $\Rightarrow C\models\mathrm{AD}$, so $\mathbb{R}$ is not well-orderable in $C$ (Woodin).
- Under the latter hypothesis, $C$ also satisfies "$\omega_1$ and $\omega_2$ are measurable", so failure is not merely a coding artifact.

## 5. Principal Obstacles

1. **No fine structure for $C$.** The chief tool for definable well-orderings — condensation plus a $\Sigma_1$-Skolem-hull argument as in $L$ — fails because $L_\alpha(\mathrm{Ord}^{\omega})$ has as parameters countable sequences of *arbitrarily large* ordinals. Collapsing a hull does not collapse those sequences coherently: the image of $s\in{}^{\omega}\kappa$ under the transitive collapse need not lie in the smaller level's sequence class in a canonical way.
2. **Indiscernibility is generated, not avoided.** Any hypothesis strong enough to produce $\omega_1$-many "independent" critical points hands $C$ an uncountable set of indiscernibles as a *single element* (the $\omega_1$-sequence is not itself in $C$, but all its countable subsequences are), which is exactly what Kunen's argument exploits. Weakening this seems to require bounding the number of measurables, which is not a robust large-cardinal condition.
3. **Comparison breaks above Woodin limits.** Inner-model-theoretic computation of $C$ (the only route to a canonical well-ordering at high strength) requires iterability and comparison for mice at the relevant level; hod-mouse technology currently stops far below a proper class of Woodin limits of Woodins.
4. **Generic absoluteness cuts both ways.** From a proper class of Woodins, the theory of $C$ is invariant under set forcing, so forcing cannot be used to *create* a well-ordering in $C$ — the usual method of adding a definable coding of the universe (e.g. Jensen-style coding) is unavailable.
5. **The gap region is unmapped.** Between "$\omega_1$ measurables" (negative) and "$\neg 0^{\\#}$-style core models" (positive) sits an enormous range — strong cardinals, Woodins, superstrongs — where neither Kunen's ultrapower argument nor $K$-covering applies.

## 6. The Gap

Proven: $C\models\mathrm{AC}$ below the core-model barrier; $C\models\neg\mathrm{AC}$ from $\omega_1$ measurables; $C\models\mathrm{AD}$ from a class of Woodin limits of Woodins.

Not proven: anything about the *exact* threshold. Kunen's hypothesis and the Woodin-limit hypothesis are wildly far apart in consistency strength, yet both are negative — so the real open frontier is the *positive* side. The precise step required is a **canonical-inner-model computation of $C$ under a hypothesis with at least one measurable but fewer than $\omega_1$ of them, or under hypotheses (strong, Woodin) whose critical points are not "spread out"**, showing $\mathrm{Ord}^{\omega}\cap C$ admits a definable well-ordering. Equivalently: does *one* measurable cardinal already refute $\mathrm{AC}^{C}$? No proof and no consistency result is known in either direction.

## 7. Current Research (as of June 2026)

- **Descriptive inner model theory** (Sargsyan, Steel, Trang, Schindler and collaborators): computing derived models and hod pairs whose Chang-model-like closures can be analyzed; the goal is a "$C$ = derived model of a hod mouse" theorem in a restricted region. *(frontier — verify)*
- **Extended-logic inner models** (Kennedy, Magidor, Väänänen and successors, Helsinki/Jerusalem): mapping which logics $\mathcal{L}^{*}$ give $C(\mathcal{L}^{*})\models\mathrm{ZFC}$ with a definable well-ordering, isolating the $\omega$-sequence-closure obstruction. Follow-up parts of the *Inner models from extended logics* program are active.
- **Generalized Chang models** $C_\kappa=L(\mathrm{Ord}^{<\kappa})$ for $\kappa>\omega_1$: determinacy-style failures of AC propagate upward; sharper thresholds for $\kappa=\omega_2$ are under investigation. *(frontier — verify)*
- **HOD-analysis inside $C$**: whether $C\models V=\mathrm{HOD}(\mathrm{Ord}^{\omega})$ can be improved to $V=\mathrm{HOD}$ under $\mathrm{AC}$-friendly hypotheses (parameter-free version of the problem).

## 8. Future Work

- Determine whether a single measurable cardinal suffices for $C\models\neg\mathrm{AC}$; a positive answer would collapse the gap from above almost entirely.
- Prove a covering lemma for $C$ over a core model $K$ in the region between $0^{\P}$ and a Woodin cardinal, yielding $C\models\mathrm{AC}$ there.
- Establish or refute: $\mathrm{Con}(\mathrm{ZFC}+\text{a strong cardinal})\Rightarrow \mathrm{Con}(\mathrm{ZFC}+\text{a strong cardinal}+ C\models\mathrm{AC})$.
- Identify a logic $\mathcal{L}^{*}$ with $L_{\omega_1\omega} \le \mathcal{L}^{*} < L_{\omega_1\omega_1}$ such that $C(\mathcal{L}^{*})$ still has a definable well-ordering under large cardinals — a "maximal AC-preserving closure" theorem.
- Compute the exact large-cardinal strength of "$C\models\mathrm{AD}$", currently bracketed between $\mathrm{AD}^{L(\mathbb{R})}$ and a proper class of Woodin limits of Woodins.

## 9. Key References

- **[Foundational]** C. C. Chang. *Sets constructible using $L_{\kappa\kappa}$.* In: Axiomatic Set Theory, Proceedings of Symposia in Pure Mathematics XIII, Part I, American Mathematical Society, 1971, pp. 1–8.
- **[Foundational]** Kenneth Kunen. *Some applications of iterated ultrapowers in set theory.* Annals of Mathematical Logic 1 (1970), 179–227.
- **[Reference]** Thomas Jech. *Set Theory* (Third Millennium Edition). Springer, 2003. (Chang model, closure under $\omega$-sequences, failure of AC.)
- **[Reference]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings*, 2nd ed. Springer, 2003.
- **[SOTA]** Peter Koellner and W. Hugh Woodin. *Large cardinals from determinacy.* In: Handbook of Set Theory (M. Foreman, A. Kanamori, eds.), Springer, 2010, pp. 1951–2119.
- **[SOTA]** W. Hugh Woodin. *The Axiom of Determinacy, Forcing Axioms, and the Nonstationary Ideal*, 2nd revised ed. De Gruyter Series in Logic and Its Applications 1, 2010.
- **[SOTA / Recent]** Juliette Kennedy, Menachem Magidor, Jouko Väänänen. *Inner models from extended logics: Part I.* Journal of Mathematical Logic 21 (2021), no. 2, 2150012.
- **[Survey]** John R. Steel. *An outline of inner model theory.* In: Handbook of Set Theory, Springer, 2010, pp. 1595–1684.
- **[Survey]** Paul B. Larson. *The Stationary Tower: Notes on a Course by W. Hugh Woodin.* University Lecture Series 32, American Mathematical Society, 2004.
- **[Technique]** Ralf Schindler and John R. Steel. *The self-iterability of $L[E]$.* Journal of Symbolic Logic 74 (2009), 751–779.

## 10. Worked Example / Concrete Special Case

**Case A: $V=L$ — the well-ordering exists and is optimal.**
Every $s:\omega\to\mathrm{Ord}$ is a set of ordered pairs of ordinals; by $V=L$, $s\in L$. Hence $\mathrm{Ord}^{\omega}\subseteq L$ and
$$C = L(\mathrm{Ord}^{\omega}) = L.$$
The canonical well-ordering $<_L$ is $\Sigma_1$ over $L$ without parameters, so $C\models V=\mathrm{HOD}$ and all three forms of §1 are answered positively.

**Case B: $V=L[G]$, $G$ Cohen-generic over $L$ for $\mathrm{Add}(\omega,1)$ — a *parametrized* well-ordering.**
The generic real $c=\bigcup G \in {}^{\omega}2 \subseteq \mathrm{Ord}^{\omega}$, so $c\in C$ and $L[c]\subseteq C$. Since $\mathrm{Add}(\omega,1)$ is countable, $L[G]=L[c]$, so
$$L[c]\subseteq C\subseteq V=L[c]\quad\Longrightarrow\quad C=L[c].$$
Then $<_{L[c]}$ well-orders $C$ definably **with parameter $c$**. Parameter-freeness genuinely fails in the naive sense: $c$ is not ordinal-definable in $L[c]$ (homogeneity of $\mathrm{Add}(\omega,1)$ gives $\mathrm{HOD}^{L[c]}=L$), so $C \models V \ne \mathrm{HOD}$ while $C\models\mathrm{AC}$. This separates form 3 from forms 1–2 of the problem.

**Case C: $\omega_1$ measurables — the well-ordering dies.**
Let $\langle \kappa_\alpha : \alpha<\omega_1\rangle$ be increasing measurables with normal measures $U_\alpha$. Every countable subsequence $\langle\kappa_{\alpha_n}:n<\omega\rangle$ lies in $\mathrm{Ord}^{\omega}\subseteq C$. Iterating the $U_\alpha$'s produces, for each $\alpha$, a class of indiscernibles for the corresponding iterated ultrapower; Kunen's computation shows the resulting family of countable sets of indiscernibles cannot be uniformized inside $C$: any $C$-definable choice function on it would, by indiscernibility, be invariant under the shift $\kappa_{\alpha_n}\mapsto\kappa_{\alpha_{n+1}}$, contradicting injectivity. Hence $C\models\neg\mathrm{AC}$, and no formula with parameters well-orders $C$.

The three cases bracket the problem: definability of the well-ordering is *not* a fixed feature of $C$ but a function of $V$'s large-cardinal content, and the interval between Case B and Case C is exactly what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*