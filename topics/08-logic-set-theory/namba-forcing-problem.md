---
id: 08-logic-set-theory/namba-forcing-problem
title: "Namba Forcing Problem"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Namba Forcing Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/namba-forcing-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Namba forcing changes the cofinality of $\omega_2$ to $\omega$ while preserving $\omega_1$. Two natural versions exist — the *Namba* poset $\mathrm{Nm}$ (splitting sets of size $\aleph_2$) and the *Bukovský–Namba* poset $\mathrm{Nm}'$ (stationary splitting sets). The "Namba forcing problem" is the cluster of questions left open once the original independence question was settled:

1. **Equivalence.** Is it a theorem of ZFC that $\mathrm{Nm}$ and $\mathrm{Nm}'$ are forcing equivalent (produce the same generic extensions)? Shelah proved equivalence under CH; without CH the question is open.
2. **Distributivity without CH.** Under CH, Namba forcing adds no new reals. Is $\neg\mathrm{CH}\ +\ $"Namba forcing adds no new reals" consistent, and at what consistency strength?
3. **Semiproperness.** Exactly which hypotheses characterize "Namba forcing is semiproper"? It follows from Martin's Maximum and implies Chang's Conjecture; neither implication is known to reverse.

A complete solution means, for (1), a ZFC proof of equivalence or a model where the two posets yield different extensions; for (2), a model of $2^{\aleph_0}>\aleph_1$ in which $\mathrm{Nm}$ is $\omega$-distributive on reals, or a ZFC proof that CH is necessary; for (3), a combinatorial statement provably equivalent to semiproperness of $\mathrm{Nm}$.

## 2. Mathematical Foundations

Work in ZFC. Write $\omega_2^{<\omega}$ for the tree of finite sequences of ordinals $<\omega_2$. For a tree $T\subseteq\omega_2^{<\omega}$ and $t\in T$ set
$$\mathrm{Succ}_T(t)=\{\alpha<\omega_2 : t^\frown\langle\alpha\rangle\in T\}.$$

**Namba forcing.** $\mathrm{Nm}$ is the set of trees $T\subseteq\omega_2^{<\omega}$ with a stem $s_T$ (all $t\in T$ are $\subseteq$- or $\supseteq$-comparable with $s_T$) such that
$$\forall t\in T\ (t\supseteq s_T\ \Rightarrow\ |\mathrm{Succ}_T(t)|=\aleph_2),$$
ordered by $S\le T \iff S\subseteq T$.

**Bukovský–Namba forcing.** $\mathrm{Nm}'$ is defined identically except the splitting condition is
$$\mathrm{Succ}_T(t)\ \text{is stationary in }\omega_2 .$$
Since every stationary subset of $\omega_2$ has size $\aleph_2$, $\mathrm{Nm}'\subseteq\mathrm{Nm}$, and the inclusion is not dense.

**Generic object.** If $G$ is generic, $b_G=\bigcup\{s_T : T\in G\}\in(\omega_2^V)^{\omega}$ is strictly increasing and cofinal in $\omega_2^V$; hence
$$V[G]\models \mathrm{cf}(\omega_2^V)=\omega .$$

**Core theorem (Namba 1971; Bukovský 1976).** $\mathrm{Nm}$ and $\mathrm{Nm}'$ preserve $\omega_1$. Consequently $|\omega_2^V|=\aleph_1$ in $V[G]$: $\omega_2^V$ is collapsed, and $(\omega,\omega_1)$-distributivity of the Boolean algebra $\mathcal{P}(\omega_1)/\mathrm{NS}$-style two-cardinal distributive laws separate.

**Distributivity.** $\mathbb{P}$ is *$\omega$-distributive* if it adds no new $\omega$-sequences of ground-model elements; it *adds no reals* if $(2^\omega)^{V[G]}=(2^\omega)^V$. Namba forcing is never $\omega$-distributive (it adds $b_G$), so the sharp question is only about reals.

**Semiproperness (Shelah).** $\mathbb{P}$ is semiproper if for club-many countable $M\prec H_\theta$ with $\mathbb{P}\in M$ and every $p\in\mathbb{P}\cap M$ there is $q\le p$ such that
$$q\Vdash M[\dot G]\cap\omega_1 = M\cap\omega_1 .$$
Semiproper forcings preserve $\omega_1$ and are iterable with revised countable support (RCS). Namba forcing is stationary-set-preserving but **never proper**: proper forcings preserve stationarity of subsets of $[\omega_2]^{\omega}$, which fails once $\mathrm{cf}(\omega_2)=\omega$.

**Chang's Conjecture.** $(\omega_2,\omega_1)\twoheadrightarrow(\omega_1,\omega)$: every structure $\mathfrak{A}=\langle\omega_2,\omega_1,\dots\rangle$ in a countable language has an elementary submodel $\mathfrak{B}$ with $|B|=\aleph_1$ and $|B\cap\omega_1|=\aleph_0$.

## 3. History & State of the Art (SOTA)

- **1969–71.** Kanji Namba, studying two-cardinal distributive laws, constructed $\mathrm{Nm}$ and proved $(\omega,\omega_1)$-DL does not imply $(\omega,\omega_1)$-WDL, i.e. $\omega_2$ can be made of cofinality $\omega$ with $\omega_1$ intact.
- **1970s.** Lev Bukovský independently obtained the stationary-splitting variant $\mathrm{Nm}'$ and framed it as "changing the cofinality of $\aleph_2$."
- **Jensen.** Under CH, Namba forcing adds no new reals — a genuinely two-cardinal phenomenon: new $\omega$-sequences of ordinals appear with no new reals. The argument (a fusion/rank analysis of names) is presented in Shelah's *Proper and Improper Forcing*, Ch. XI.
- **Shelah (1980s).** Under CH, $\mathrm{Nm}$ and $\mathrm{Nm}'$ are forcing equivalent. Namba forcing is Shelah's canonical example separating "stationary-set-preserving" from "semiproper", motivating RCS iteration and the semiproper forcing axiom.
- **Foreman–Magidor–Shelah (1988).** Martin's Maximum implies every stationary-set-preserving poset is semiproper, hence $\mathrm{Nm}$ is semiproper; MM also gives Chang's Conjecture.
- **2010s.** Krueger, and Cox–Krueger, tied "Namba forcing adds no reals" to failures of good scales, weak approximation, and guessing models, providing the first structural obstructions to a $\neg$CH version.

## 4. Partial Results / Verified Cases

- **$\kappa=\omega_2$, ZFC.** $\omega_1$-preservation and $\mathrm{cf}(\omega_2)=\omega$ hold outright, with no large-cardinal hypothesis (Namba, Bukovský).
- **Under CH.** (i) $\mathrm{Nm}\equiv\mathrm{Nm}'$ (Shelah); (ii) neither adds a real (Jensen); (iii) hence CH persists in the extension. This settles the whole cluster in the CH case.
- **Under MM / SPFA.** $\mathrm{Nm}$ is semiproper (Foreman–Magidor–Shelah; Shelah). Consistency strength: supercompact.
- **Implication direction.** Semiproperness of Namba forcing implies Chang's Conjecture $(\omega_2,\omega_1)\twoheadrightarrow(\omega_1,\omega)$, whose strength is exactly an $\omega_1$-Erdős cardinal (Donder–Levinski, Silver).
- **General regular $\kappa\ge\omega_2$.** Namba-style trees on $\kappa$ with $\kappa$-splitting change $\mathrm{cf}(\kappa)$ to $\omega$ preserving $\omega_1$; preserving *more* cardinals (e.g. keeping $\aleph_2$ while $\mathrm{cf}(\aleph_3)=\omega$) requires measurable-type hypotheses via Prikry/Gitik forcing.
- **Structural corollaries.** If Namba forcing adds no reals, then there is no good scale on suitable $[\omega_2]^{\omega}$-type structures (Krueger), and weak-approximation/guessing-model principles fail (Cox–Krueger). These are strong necessary conditions, verified as theorems.

## 5. Principal Obstacles

- **No fusion without CH.** Jensen's no-new-reals proof enumerates all $\aleph_1$-many relevant names/dense sets in order type $\omega_1$ and builds an $\omega_1$-length fusion of Namba trees. With $2^{\aleph_0}\ge\aleph_2$ the enumeration has length $\ge\omega_2$ and the fusion has no place to close off: a decreasing $\omega_2$-chain of Namba trees can have empty intersection.
- **Trees are not $\sigma$-closed and not ccc.** $\mathrm{Nm}$ sits in neither of the two regimes where preservation arguments are routine; it is $\aleph_2$-branching but every branch is countable, so neither $\Delta$-system nor closure arguments apply.
- **Absence of a Prikry property.** Prikry forcing has pure decision, letting one decide statements without changing stems. Namba forcing has no such property in general, so combinatorics of names cannot be reduced to the stem.
- **Stationarity is not absolute enough.** The difference between $\mathrm{Nm}$ and $\mathrm{Nm}'$ is exactly $|\mathrm{Succ}_T(t)|=\aleph_2$ versus stationarity. Under $\neg$CH there is no known way to thin a large-but-nonstationary splitting set to a stationary one inside a single tree, and no known invariant of the generic extension that can tell the two apart.
- **Semiproperness is a $\Pi_2$ statement over $H_{\omega_2}$** whose failure is witnessed by countable elementary submodels; no combinatorial reflection principle of the usual strength (square, stationary reflection, Chang variants) has been shown to be equivalent to it.

## 6. The Gap

Proven: everything under CH, plus one-directional implications (MM $\Rightarrow$ semiproper $\Rightarrow$ CC) and necessary conditions for a $\neg$CH no-reals model.

Missing, precisely:

- A construction that, given a $\le$-decreasing sequence $\langle T_\alpha:\alpha<\omega_2\rangle$ in $\mathrm{Nm}$ arising from name-fusion, produces a lower bound — or a ZFC proof that $\neg$CH forces $\mathrm{Nm}$ to add a real.
- A forcing-theoretic invariant separating $\mathrm{Nm}$ from $\mathrm{Nm}'$ (e.g. a set of ordinals in one extension but not the other), or a dense embedding argument valid without CH.
- A reversal: from Chang's Conjecture (or a strengthening of $\omega_1$-Erdős strength) to semiproperness of $\mathrm{Nm}$, closing the gap between an $\omega_1$-Erdős cardinal and a supercompact.

## 7. Current Research (as of June 2026)

- **Guessing-model programme.** Cox and Krueger's framework — Namba forcing versus weak approximation, guessing models, and internal approachability — remains the main engine; work continues on whether guessing-model principles at $\omega_2$ outright refute "Namba adds no reals" under $\neg$CH. *(frontier — verify)*
- **PCF-side obstructions.** Analysis of good scales on $\prod_n\aleph_n$-type products and their interaction with $\mathrm{cf}(\omega_2)=\omega$ extensions, following Krueger's "no good scale" theorem.
- **Semiproperness axioms.** Descendants of Doebler–Schindler's work on $\Pi_2$ consequences of bounded forcing axioms, aiming at "every stationary-set-preserving forcing is semiproper" from hypotheses far below supercompactness.
- **Groups.** Set theory groups at Kobe/Nagoya (Japanese school, Namba's lineage), Vienna (KGRC), Bonn/Münster (inner model side), and North Texas.

## 8. Future Work

- Develop an $\omega_2$-fusion calculus for $\aleph_2$-branching trees adapted to $\neg$CH, perhaps using side conditions or virtual/generic elementary embeddings instead of raw enumeration.
- Iterate Namba-type forcing with RCS to build models where $\mathrm{Nm}$ and $\mathrm{Nm}'$ are demonstrably different, e.g. by making $\mathrm{Nm}'$ semiproper and $\mathrm{Nm}$ not.
- Determine the exact consistency strength of "Namba forcing is semiproper", currently bracketed between $\omega_1$-Erdős and supercompact.
- Extend the analysis to $\mathrm{cf}(\aleph_{\omega+1})=\omega$ with $\omega_1$ preserved, where PCF theory imposes hard ZFC restrictions.

## 9. Key References

- **[Foundational]** K. Namba. *Independence proof of $(\omega,\omega_1)$-WDL from $(\omega,\omega_1)$-DL.* Commentarii Mathematici Universitatis Sancti Pauli, vol. 19, 1971, pp. 1–12.
- **[Foundational]** L. Bukovský. *Changing cofinality of $\aleph_2$.* In: Set Theory and Hierarchy Theory (Bierutowice 1975), Lecture Notes in Mathematics 537, Springer, 1976.
- **[Foundational]** S. Shelah. *Proper and Improper Forcing*, 2nd edition. Perspectives in Mathematical Logic, Springer, 1998. (Chapters XI–XII: Namba forcing, semiproperness, RCS iteration.)
- **[Foundational]** T. Jech. *Set Theory*, 3rd millennium edition. Springer Monographs in Mathematics, 2003. (Namba forcing and $\omega_1$-preservation.)
- **[SOTA / Recent]** J. Krueger. *Namba forcing and no good scale.* The Journal of Symbolic Logic, vol. 78, 2013.
- **[SOTA / Recent]** S. Cox and J. Krueger. *Namba forcing, weak approximation, and guessing.* The Journal of Symbolic Logic, vol. 83, 2018.
- **[SOTA / Recent]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics, vol. 127, 1988, pp. 1–47.
- **[Survey]** L. Bukovský and E. Copláková-Hájková. *Minimal collapsing extensions of models of ZFC.* Annals of Pure and Applied Logic, vol. 46, 1990.
- **[Survey]** H.-D. Donder and J.-P. Levinski. *Some principles related to Chang's conjecture.* Annals of Pure and Applied Logic, vol. 45, 1989.

## 10. Worked Example / Concrete Special Case

**Namba forcing over $L$.** Let $V=L$, so GCH holds; in particular CH holds and the CH-case theorems apply. Force with $\mathrm{Nm}$ and let $G$ be generic, $b_G=\langle\beta_0<\beta_1<\cdots\rangle$.

*Step 1 — the generic sequence is cofinal.* Fix $\gamma<\omega_2$ and $T\in\mathrm{Nm}$ with stem $s$. Since $|\mathrm{Succ}_T(s)|=\aleph_2$, pick $\alpha\in\mathrm{Succ}_T(s)$ with $\alpha>\gamma$ and let $S=\{t\in T: t\subseteq s^\frown\langle\alpha\rangle \text{ or } t\supseteq s^\frown\langle\alpha\rangle\}$. Then $S\le T$ and $S$ forces $\gamma\in\mathrm{ran}(b_G)$'s supremum range. So $D_\gamma=\{S:S\Vdash \exists n\,\beta_n>\gamma\}$ is dense: $\sup_n\beta_n=\omega_2^L$.

*Step 2 — $\omega_1$ survives, $\omega_2^L$ dies.* By the Namba–Bukovský theorem $\omega_1^{L[G]}=\omega_1^L$. Since $\mathrm{cf}^{L[G]}(\omega_2^L)=\omega$ and $\omega_2^L$ is an uncountable limit cardinal-successor of $L$, it cannot be a cardinal in $L[G]$; as $\omega_1$ is preserved, $|\omega_2^L|^{L[G]}=\aleph_1$.

*Step 3 — no new reals, so CH persists.* By Jensen's theorem $(2^\omega)^{L[G]}=(2^\omega)^L$, so $L[G]\models 2^{\aleph_0}=\aleph_1$. This is the striking calculation: a new $\omega$-sequence $b_G\in{}^{\omega}(\omega_2^L)$ exists, yet $\mathcal{P}(\omega)$ is unchanged. The poset is not $\omega$-distributive but is "$\omega$-distributive for reals".

*Step 4 — a cardinal bound.* In $L$, $|\mathrm{Nm}|\le 2^{\aleph_2}=\aleph_3$, so $\mathrm{Nm}$ is $\aleph_4$-c.c. and every $L$-cardinal $\ge\aleph_4^L$ is preserved. Combined with Steps 2–3: $\omega_1^{L[G]}=\omega_1^L$, $\omega_2^{L[G]}\le\aleph_3^L$.

*Step 5 — where the problem bites.* Repeat over a model of $2^{\aleph_0}=\aleph_2$ instead. Step 1 and Step 2 go through verbatim; Step 3 collapses, because Jensen's $\omega_1$-length fusion must now handle $\aleph_2$-many names for reals and there is no lower bound for a decreasing $\omega_2$-sequence of Namba trees. Whether some other argument recovers Step 3 — or whether $\neg$CH provably makes $\mathrm{Nm}$ add a real — is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*