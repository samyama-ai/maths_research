---
id: 08-logic-set-theory/axiom-of-projective-determinacy-consistency
title: "Axiom of Projective Determinacy Consistency"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Axiom of Projective Determinacy Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/axiom-of-projective-determinacy-consistency` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Projective Determinacy (PD)** asserts: every two-player infinite game of perfect information with projective payoff set is determined — one of the players has a winning strategy.

The problem is the *consistency and justification* of PD:

1. **(Relative consistency.)** Is $\mathrm{ZFC} + \mathrm{PD}$ consistent, and relative to what? — **Answered.** Martin–Steel (1989) proved PD from large cardinals; Woodin proved the converse direction, giving
$$\mathrm{Con}(\mathrm{ZFC}+\mathrm{PD}) \iff \mathrm{Con}\big(\mathrm{ZFC} + \forall n\,\exists\, n \text{ Woodin cardinals}\big).$$
2. **(Absolute consistency / justification.)** Still open. By Gödel's second incompleteness theorem $\mathrm{ZFC}\nvdash \mathrm{Con}(\mathrm{ZFC}+\mathrm{PD})$, since PD proves $\mathrm{Con}(\mathrm{ZFC})$. So the residual question is whether the Woodin-cardinal hierarchy is itself consistent, and whether PD can be derived from principles not already of large-cardinal strength.

A complete resolution of the open part would be either (a) an inner-model-theoretic consistency proof of PD reducing it to a canonical fine-structural model whose consistency is verified by a combinatorial argument, or (b) a derivation of an inconsistency in $\mathrm{ZFC}+\text{“}\forall n\ \exists n$ Woodin cardinals”.

## 2. Mathematical Foundations

**Baire space.** $\omega^\omega$ with the product topology; "reals" means elements of $\omega^\omega$.

**Games.** For $A \subseteq \omega^\omega$, the game $G(A)$ has players I and II alternately playing $x(0), x(1), x(2), \dots \in \omega$; I wins iff $x \in A$. A *strategy* for I is $\sigma:\omega^{<\omega}_{\mathrm{even}} \to \omega$. $A$ is **determined**, written $\mathrm{Det}(A)$, iff
$$\exists \sigma\, \forall y\, [\sigma * y \in A] \ \ \vee\ \ \exists \tau\, \forall x\, [x * \tau \notin A].$$

**Projective hierarchy.** $\mathbf{\Sigma}^1_1$ = continuous images of closed sets (analytic); $\mathbf{\Pi}^1_n = \neg\mathbf{\Sigma}^1_n$; $\mathbf{\Sigma}^1_{n+1} = \exists^{\omega^\omega}\mathbf{\Pi}^1_n$; $\mathbf{\Delta}^1_n = \mathbf{\Sigma}^1_n \cap \mathbf{\Pi}^1_n$. Projective $= \bigcup_n \mathbf{\Sigma}^1_n$. Then
$$\mathrm{PD} :\equiv \forall n\ \mathrm{Det}(\mathbf{\Sigma}^1_n).$$

**Woodin cardinal.** $\delta$ is Woodin iff for every $f:\delta\to\delta$ there is $\kappa<\delta$ closed under $f$ and an elementary embedding $j: V \to M$ with critical point $\kappa$, $M$ transitive, and $V_{j(f)(\kappa)} \subseteq M$.

**Sharps.** $x^{\\#}$ is the (unique, if it exists) set of Gödel numbers of formulas true of the Silver indiscernibles of $L[x]$.

**Core theorems.**

- *Gale–Stewart (1953):* $\mathrm{ZFC}\vdash \mathrm{Det}(\mathbf{\Sigma}^0_1)$ (open determinacy).
- *Martin (1975):* $\mathrm{ZFC}\vdash \mathrm{Det}(\mathbf{\Delta}^1_1)$ (Borel determinacy); the proof needs $\aleph_1$-many iterations of the power set, and by H. Friedman this is optimal.
- *Martin (1970) + Harrington (1978):* $\mathrm{Det}(\mathbf{\Sigma}^1_1) \iff \forall x\in\omega^\omega\ (x^{\\#}\text{ exists})$.
- *Martin–Steel (1989):* if there are $n$ Woodin cardinals with a measurable above them, then $\mathrm{Det}(\mathbf{\Pi}^1_{n+1})$; hence $\omega$ Woodins with a measurable above $\Rightarrow \mathrm{PD}$.
- *Woodin; Neeman (1995, 2002):* for $n\ge 1$,
$$\mathrm{Det}(\mathbf{\Pi}^1_{n+1}) \iff \forall x \in \omega^\omega\ \big(M_n^{\\#}(x) \text{ exists and is } \omega_1\text{-iterable}\big),$$
where $M_n^{\\#}(x)$ is the minimal iterable fine-structural mouse over $x$ with $n$ Woodin cardinals. This is the exact equiconsistency, level by level.
- *Structural consequences:* under $\mathrm{Det}(\mathbf{\Delta}^1_{2n})$, $\mathbf{\Pi}^1_{2n+1}$ has the scale and uniformization properties (Moschovakis periodicity), $\delta^1_{2n+1}$ is measurable, and every projective set is Lebesgue measurable, has the Baire property, and the perfect set property.

## 3. History & State of the Art (SOTA)

- **1953.** Gale and Stewart introduce infinite perfect-information games; prove open determinacy; ask about higher classes.
- **1962.** Mycielski and Steinhaus propose the Axiom of Determinacy (AD), incompatible with AC; Mycielski–Świerczkowski show AD implies all sets of reals are Lebesgue measurable.
- **1967–70.** Solovay and Martin link determinacy to large cardinals; Martin proves a measurable cardinal gives analytic determinacy.
- **1970s.** The "Cabal" seminar (Kechris, Martin, Moschovakis, Solovay, Steel) develops the structure theory of $L(\mathbb{R})$ under AD: periodicity theorems, scales, the Wadge hierarchy, computation of the projective ordinals.
- **1975.** Martin proves Borel determinacy in ZFC — the ceiling of what choice alone yields.
- **1978.** Harrington's converse closes the $\mathbf{\Sigma}^1_1$ level.
- **1984–85.** Martin and Steel develop iteration trees; Foreman–Magidor–Shelah's saturated-ideal work supplies the Woodin-cardinal context; Woodin proves $\mathrm{AD}^{L(\mathbb{R})}$ from a supercompact, then from $\omega$ Woodins.
- **1989.** *A proof of projective determinacy* (Martin–Steel, JAMS) — the central positive result.
- **1990s–2000s.** Neeman gives optimal, level-by-level proofs; Steel proves $\mathrm{PFA}\Rightarrow \mathrm{AD}^{L(\mathbb{R})}$ (2005) via the core model induction; Woodin develops $\Omega$-logic and $\Sigma^2_1$-absoluteness.
- **2010s–2020s.** Sargsyan's HOD-mice program pushes descriptive inner model theory past $\mathrm{AD}_{\mathbb{R}}+\text{“}\Theta$ regular"; the Mouse Set Conjecture becomes the organizing open problem.

**SOTA summary.** PD is a *theorem* of ZFC + large cardinals, with exactly calibrated strength. What remains open is absolute justification and the extension of the inner model program to supercompact cardinals.

## 4. Partial Results / Verified Cases

| Level | Status | Hypothesis needed |
|---|---|---|
| $\mathbf{\Sigma}^0_1$, $\mathbf{\Sigma}^0_2$ | proved | ZFC (Gale–Stewart; Wolfe 1955) |
| $\mathbf{\Sigma}^0_3$ | proved | ZFC (Davis 1964) |
| $\mathbf{\Delta}^1_1$ (all Borel) | proved | ZFC; needs $V_{\omega_1}$-many power sets (Martin 1975; Friedman's optimality) |
| $\mathbf{\Sigma}^1_1$ | proved & equiconsistent | $\forall x\, x^{\\#}$ exists |
| $\mathbf{\Delta}^1_2$ | proved | $\forall x\ M_1^{\\#}(x)$ exists and is $\omega_1$-iterable |
| $\mathbf{\Pi}^1_{n+1}$ | proved & equiconsistent | $n$ Woodins + measurable above; equivalently $\forall x\, M_n^{\\#}(x)$ |
| full PD | proved | $\omega$ Woodins + measurable above |
| $\mathrm{AD}^{L(\mathbb{R})}$ | proved & equiconsistent | $\omega$ Woodin cardinals |

Derivations of PD from non-large-cardinal hypotheses: $\mathrm{MM}$ and $\mathrm{PFA}$ each imply $\mathrm{AD}^{L(\mathbb{R})}$ (Woodin; Steel 2005); the failure of $\square_{\kappa}$ at singular strong limits of uncountable cofinality plus SCH failure yields PD by core model induction; a saturated ideal on $\omega_1$ plus a measurable gives $\mathrm{Det}(\mathbf{\Pi}^1_1)$ and more.

## 5. Principal Obstacles

- **Gödelian ceiling.** PD proves $\mathrm{Con}(\mathrm{ZFC})$, $\mathrm{Con}(\mathrm{ZFC}+\text{“there is a measurable”})$, and unboundedly more. No proof of $\mathrm{Con}(\mathrm{ZFC}+\mathrm{PD})$ can be carried out in any theory PD interprets. This is not a defect of technique — it is a hard limitation.
- **Forcing is useless here.** Determinacy at the projective level is not a forcing-fragile combinatorial statement; it is preserved and reflected by large-cardinal structure. Cohen-style independence arguments produce no models of PD from ZFC alone.
- **Inner model theory stalls above Woodin limits.** Fine-structural models $M_n$ are built by comparison of mice via iteration trees. Beyond finitely many Woodins the comparison process meets the **iterability problem**: proving that all countable trees have well-founded branches requires the very determinacy one wants. At supercompact strength no fine-structural hierarchy is known (the "long extenders" barrier).
- **The descriptive inner model bootstrap.** The core model induction derives PD from combinatorial hypotheses, but it *presupposes* determinacy at level $n$ to reach level $n+1$ — it converts consistency, it does not create it from nothing.
- **No combinatorial characterization.** There is no known equivalent of PD phrased purely in terms of, e.g., cardinal arithmetic or partition properties on small cardinals; every equivalence found so far is again of large-cardinal character (mice, sharps, homogeneously Suslin representations).

## 6. The Gap

Proved: $\mathrm{ZFC}+\text{“}\omega$ Woodins with a measurable above” $\vdash \mathrm{PD}$, and the reverse consistency implication. So the gap is *not* about PD given large cardinals.

The gap is the **justification gap**:
$$\text{“}\mathrm{ZFC}+\mathrm{PD} \text{ is consistent”} \quad \Longleftarrow\!\!\!/\!\!\!\Longleftarrow \quad \text{any theory we can prove consistent.}$$
Crossing it requires either (i) an inner-model construction reaching supercompact cardinals, which by Woodin's "ultimate-$L$" analysis would make the whole hierarchy below it fine-structurally transparent and its consistency as evident as $\mathrm{Con}(L)$ is relative to ZF; or (ii) a *derivation* of an inconsistency. Woodin's **$\Omega$ Conjecture** and the **Mouse Set Conjecture** ($\mathbb{R}\cap\mathrm{HOD}^{L(\mathbb{R})}$ is exactly the set of reals in mice) are the two precise statements whose resolution decides how much of (i) is achievable.

## 7. Current Research (as of June 2026)

- **Ultimate-$L$ program (Woodin, Berkeley/Harvard).** Building a fine-structural, generically-absolute inner model compatible with a supercompact. If successful it delivers a canonical universe in which PD holds and whose consistency rests on a hierarchy with no known threat. Status: the "$\mathrm{HOD}$ Dichotomy" and $\Omega$ Conjecture remain unproven. *(frontier — verify)*
- **Descriptive inner model theory (Sargsyan, IMPAN Warsaw; Steel, Berkeley; Schindler, Münster).** HOD mice, hod pair constructions past $\mathrm{AD}_{\mathbb{R}} + \Theta$ regular; the *Largest Suslin Axiom* (LSA) as a new anchor for equiconsistencies.
- **Core model induction applications (Schindler, Steel, Adolf, Trang).** Extracting $\mathrm{AD}^{L(\mathbb{R})}$ and beyond from forcing axioms, ideal hypotheses, and failures of square; recent work targets $\mathrm{MM}^{++}$ and its consequences at $\omega_2$. *(frontier — verify)*
- **Long-game and generalized determinacy (Neeman, Trang).** Determinacy of games of length $\omega\cdot n$ and $\omega^2$ with projective payoff, calibrated against Woodin limits of Woodins.
- **Reverse mathematics of determinacy (Montalbán, Shore, Nemoto).** Locating $\mathbf{\Sigma}^0_n$ determinacy strictly between $\mathrm{ATR}_0$ and $\Pi^1_1\text{-}\mathrm{CA}_0$ — a low-level analogue of the projective phenomenon.

## 8. Future Work

- Prove or refute the **$\Omega$ Conjecture**; it decides whether generic absoluteness can be axiomatized and constrains the large-cardinal hierarchy's coherence.
- Settle the **Mouse Set Conjecture** at and above $\mathrm{AD}_{\mathbb{R}}+\text{“}\Theta$ regular”.
- Solve the **iterability problem** for long-extender models; Steel and Woodin both identify this as the single technical blocker to a supercompact inner model.
- Find a **combinatorial equivalent of PD** at the level of $\omega_1$ or $\omega_2$ — a statement about stationary sets or ideals provably equivalent to PD, which would allow independent plausibility checks.
- Continue **empirical consistency testing**: proof mining the large-cardinal hierarchy for contradictions (the Kunen inconsistency at $j:V\to V$ shows the method has bite).

## 9. Key References

- **[Foundational]** D. Gale and F. M. Stewart. *Infinite games with perfect information.* In *Contributions to the Theory of Games II*, Annals of Mathematics Studies 28, Princeton University Press, 1953, pp. 245–266.
- **[Foundational]** J. Mycielski and H. Steinhaus. *A mathematical axiom contradicting the axiom of choice.* Bulletin de l'Académie Polonaise des Sciences 10 (1962), 1–3.
- **[Foundational]** D. A. Martin. *Measurable cardinals and analytic games.* Fundamenta Mathematicae 66 (1970), 287–291.
- **[Foundational]** D. A. Martin. *Borel determinacy.* Annals of Mathematics 102 (1975), 363–371.
- **[Foundational]** L. Harrington. *Analytic determinacy and $0^{\\#}$.* Journal of Symbolic Logic 43 (1978), 685–693.
- **[SOTA]** D. A. Martin and J. R. Steel. *A proof of projective determinacy.* Journal of the American Mathematical Society 2 (1989), 71–125.
- **[SOTA]** D. A. Martin and J. R. Steel. *Iteration trees.* Journal of the American Mathematical Society 7 (1994), 1–73.
- **[SOTA]** W. H. Woodin. *Supercompact cardinals, sets of reals, and weakly homogeneous trees.* Proceedings of the National Academy of Sciences USA 85 (1988), 6587–6591.
- **[SOTA]** I. Neeman. *Optimal proofs of determinacy.* Bulletin of Symbolic Logic 1 (1995), 327–339; and *Optimal proofs of determinacy II*, Journal of Mathematical Logic 2 (2002), 227–258.
- **[SOTA]** J. R. Steel. *PFA implies $\mathrm{AD}^{L(\mathbb{R})}$.* Journal of Symbolic Logic 70 (2005), 1255–1296.
- **[Recent]** G. Sargsyan. *Hod Mice and the Mouse Set Conjecture.* Memoirs of the American Mathematical Society 236 (2014), no. 1111.
- **[Recent]** P. B. Larson. *Extensions of the Axiom of Determinacy.* University Lecture Series 78, American Mathematical Society, 2023.
- **[Survey]** P. Koellner and W. H. Woodin. *Large cardinals from determinacy.* In M. Foreman and A. Kanamori (eds.), *Handbook of Set Theory*, Springer, 2010, pp. 1951–2119.
- **[Survey]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Survey]** Y. N. Moschovakis. *Descriptive Set Theory.* 2nd ed., Mathematical Surveys and Monographs 155, AMS, 2009.
- **[Survey]** W. H. Woodin. *The Axiom of Determinacy, Forcing Axioms, and the Nonstationary Ideal.* 2nd ed., De Gruyter, 2010.

## 10. Worked Example / Concrete Special Case

**Open determinacy in ZFC, then the jump.**

Let $A \subseteq \omega^\omega$ be open: $A = \bigcup_{s \in S}[s]$ for some $S \subseteq \omega^{<\omega}$, where $[s]=\{x : s \subset x\}$.

Define, for a position $p \in \omega^{<\omega}$ with II to move, the relation "$p$ is *good for* I" by transfinite recursion:
$$p \in G_0 \iff \exists s\in S,\ s \subseteq p; \qquad p \in G_{\alpha+1} \iff \exists m\,\forall k\ \big(p^\frown\langle m,k\rangle \in \textstyle\bigcup_{\beta\le\alpha} G_\beta\big),$$
with unions at limits. Let $G=\bigcup_\alpha G_\alpha$ (the recursion closes off by $\alpha < |\omega^{<\omega}|^+ = \aleph_1$).

*Case 1: $\emptyset \in G$.* Assign to each $p\in G$ its rank $\rho(p)=\min\{\alpha : p\in G_\alpha\}$. I plays, from $p$, a witness $m$ that strictly lowers rank whatever II answers. Ranks are ordinals, so descent terminates: I reaches rank $0$, i.e. an $s\in S$ with $s\subseteq p$, so the play is in $[s]\subseteq A$. I wins.

*Case 2: $\emptyset \notin G$.* Then for every $m$ there is $k$ with $\langle m,k\rangle \notin G$; II plays such a $k$ each round, maintaining $p \notin G$ forever. Since $p\notin G \Rightarrow p\notin G_0$, no initial segment of the play lies in $S$, so $x \notin A$. II wins. $\square$

The whole argument uses only ZFC and a rank function of countable length.

**Where it breaks.** Take $A$ to be $\mathbf{\Sigma}^1_1$ — say $A=\{x : T_x \text{ is ill-founded}\}$ for a recursive tree assignment. The analogous rank recursion no longer terminates inside $V_{\omega_1}$; the natural "unraveling" (Martin's technique, which handles Borel by lifting to auxiliary games on trees of ordinals) needs an *auxiliary game* whose moves code branches through the Kleene–Brouwer ordering of $T_x$, and the winning condition of the auxiliary game is closed only if one has a **homogeneous tree** representation of $A$. Producing that tree requires a measurable cardinal $\kappa$: Martin's 1970 proof uses a $\kappa$-complete ultrafilter to select branches coherently. By Harrington's theorem the requirement is necessary — $\mathrm{Det}(\mathbf{\Sigma}^1_1)$ *implies* $\forall x\ x^{\\#}$ exists, hence implies $\mathrm{Con}(\mathrm{ZFC})$.

So the concrete gap is one quantifier wide: $\mathbf{\Sigma}^0_1$ determinacy is a page of ZFC; $\mathbf{\Sigma}^1_1$ determinacy already transcends ZFC, and each further projective quantifier costs exactly one more Woodin cardinal.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*