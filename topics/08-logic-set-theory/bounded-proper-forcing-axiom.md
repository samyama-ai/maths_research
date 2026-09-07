---
id: 08-logic-set-theory/bounded-proper-forcing-axiom
title: "Bounded Proper Forcing Axiom"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bounded Proper Forcing Axiom

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/bounded-proper-forcing-axiom` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Bounded Proper Forcing Axiom (BPFA) is the restriction of the Proper Forcing Axiom to families of $\aleph_1$ maximal antichains each of size at most $\aleph_1$:

> **BPFA.** For every proper poset $\mathbb{P}$ and every family $\{A_\alpha : \alpha < \omega_1\}$ of maximal antichains of the Boolean completion $\mathrm{ro}(\mathbb{P})$ with $|A_\alpha| \le \aleph_1$ for each $\alpha$, there is a filter $G \subseteq \mathrm{ro}(\mathbb{P})$ meeting every $A_\alpha$.

BPFA is strictly weaker than PFA in consistency strength — it follows from a *reflecting cardinal* rather than a supercompact — yet it decides much of the combinatorics of $H(\omega_2)$. The catalog problem is the cluster of questions left open by this mismatch:

1. **Which PFA consequences at $\omega_2$ does BPFA decide?** In particular: does BPFA imply the tree property at $\omega_2$, the failure of $\square(\omega_2)$, or stationary reflection at $\omega_2$? (All are PFA theorems; none is known for BPFA, and consistency-strength considerations forbid some of them.)
2. **What is the exact consistency strength of Bounded Martin's Maximum (BMM)?** BPFA's strength is pinned at a reflecting cardinal; BMM's is known only to lie between a reflecting cardinal-plus and, under extra hypotheses, an inner model with a Woodin cardinal.
3. **How much of the $H(\omega_2)$ theory of PFA is already BPFA's?** Equivalently: is there a $\Pi_2$ sentence about $H(\omega_2)$ that PFA proves and BPFA does not?

A resolution of (1) or (2) means a ZFC proof from BPFA, or a model of BPFA plus the negation, obtained by forcing over a model with a reflecting cardinal (upper bound) together with a core-model lower-bound computation.

## 2. Mathematical Foundations

**Proper forcing.** For a poset $\mathbb{P}$ and regular $\theta$ with $\mathbb{P}\in H(\theta)$, $\mathbb{P}$ is *proper* iff for every countable elementary $N \prec H(\theta)$ with $\mathbb{P}\in N$ and every $p \in \mathbb{P}\cap N$ there is $q \le p$ that is $(N,\mathbb{P})$-generic: for every maximal antichain $A \in N$ of $\mathbb{P}$, $A \cap N$ is predense below $q$. Properness preserves stationary subsets of $[\lambda]^{\omega}$ and is preserved by countable support iteration (Shelah).

**Bounded forcing axioms.** For a class $\Gamma$ of posets,
$$\mathrm{BFA}(\Gamma):\quad \forall \mathbb{P}\in\Gamma\ \ \forall \langle A_\alpha:\alpha<\omega_1\rangle \big(\textstyle\bigwedge_\alpha |A_\alpha|\le\aleph_1 \wedge A_\alpha \text{ max.\ antichain in } \mathrm{ro}(\mathbb{P})\big)\ \exists\, G\ \forall \alpha\, (G\cap A_\alpha \neq \emptyset).$$
$\mathrm{BFA}(\text{proper}) = $ BPFA; $\mathrm{BFA}(\text{ccc}) = \mathrm{MA}_{\aleph_1}$; $\mathrm{BFA}(\text{stationary-set-preserving}) = $ BMM.

**Bagaria's absoluteness characterization.** BFA$(\Gamma)$ is equivalent to $\Sigma_1$-generic absoluteness for $H(\omega_2)$:
$$\mathrm{BFA}(\Gamma) \iff \forall \mathbb{P}\in\Gamma:\ H(\omega_2)^{V} \prec_{\Sigma_1} H(\omega_2)^{V^{\mathbb{P}}},$$
i.e. for every $\Sigma_1$ formula $\varphi$ and parameter $a \in H(\omega_2)^V$, if $\Vdash_{\mathbb{P}} H(\omega_2)\models\varphi(a)$ then $H(\omega_2)^V \models \varphi(a)$ (Bagaria 2000). This recasts BPFA as a *principle of generic absoluteness*, and is the form in which almost all consequences are derived.

**Reflecting cardinals.** $\kappa$ is *reflecting* iff $\kappa$ is regular and for every $a\in H_\kappa$ and formula $\varphi$, if $H_\lambda \models \varphi(a)$ for some $\lambda$, then $H_\mu\models\varphi(a)$ for some $\mu<\kappa$ (equivalently: $\kappa$ is inaccessible and $\Sigma_2$-reflecting). Reflecting cardinals sit below Mahlo cardinals in strength — they are consistent with $V=L$.

## 3. History & State of the Art (SOTA)

- **1988.** Foreman, Magidor and Shelah prove Martin's Maximum consistent from a supercompact, establishing the maximal forcing axiom and the framework BPFA weakens.
- **1995.** Goldstern and Shelah introduce BPFA (*JSL* 60), prove $\mathrm{Con}(\mathrm{ZFC} + \exists\text{ reflecting }\kappa) \Rightarrow \mathrm{Con}(\mathrm{ZFC}+\mathrm{BPFA})$ by a countable support iteration of length $\kappa$ with a $\Sigma_2$-reflecting bookkeeping, and conversely that BPFA implies $\omega_2^V$ is reflecting in $L$. **Strength: exactly a reflecting cardinal.**
- **2000.** Bagaria proves the $\Sigma_1$-absoluteness characterization; also that the unrestricted bounded axiom for all posets is inconsistent.
- **2001.** Schindler calibrates related axioms: $\Sigma^1_3$-absoluteness for proper forcing is equiconsistent with a *remarkable* cardinal (*JSL* 66), separating "boldface projective" absoluteness from BPFA.
- **2001–2002.** Asperó–Bagaria (*APAL* 109) and Todorčević (*Math. Res. Lett.* 9) study the continuum under bounded axioms; Todorčević proves **BPFA $\Rightarrow 2^{\aleph_0}=\aleph_2$**.
- **2005–2006.** Moore's *set mapping reflection* (MRP) follows from BPFA and implies $2^{\aleph_0}=\aleph_2$; Moore then proves the **five-element basis for uncountable linear orders from BPFA** (*Annals* 163), a theorem previously known only from PFA.
- **2006.** Caicedo–Veličković: BPFA implies a $\Delta_1$-definable well-ordering of $\mathbb{R}$ with a parameter in $H(\omega_2)$, hence a $\Sigma_3$ well-ordering of the reals — so BPFA is compatible with strong definability, unlike large-cardinal axioms.
- **2012.** Claverie–Schindler: BMM $+$ "$\mathrm{NS}_{\omega_1}$ is precipitous" implies an inner model with a Woodin cardinal — BMM is strictly stronger than BPFA.
- **2021.** Asperó–Schindler prove $\mathrm{MM}^{++}\Rightarrow(*)$, sharpening the map of the forcing-axiom hierarchy above BPFA.

## 4. Partial Results / Verified Cases

- **Restricted classes.** $\mathrm{BFA}(\text{ccc})=\mathrm{MA}_{\aleph_1}$ exactly (boundedness is vacuous for ccc posets, whose antichains are countable). $\mathrm{BFA}(\Gamma)$ for $\Gamma=$ all posets is refutable in ZFC.
- **Cardinal arithmetic.** BPFA $\Rightarrow 2^{\aleph_0}=\aleph_2$ (Todorčević 2002; independently via Moore's MRP 2005). So BPFA settles CH, and $\mathfrak{b}=\mathfrak{d}=\aleph_2$ follows from $\mathrm{MA}_{\aleph_1}$.
- **Combinatorics of $\omega_1$.** BPFA $\Rightarrow$ MRP $\Rightarrow$ failure of $\square(\kappa)$ for $\kappa$ where MRP applies, plus: every two $\aleph_1$-dense suborders question aside, the **five-element basis** $\{X, \omega_1, \omega_1^*, C, C^*\}$ for uncountable linear orders holds (Moore 2006), and $\mathrm{OCA}$-type consequences of MRP hold.
- **Definability.** BPFA $\Rightarrow$ there is a well-ordering of $\mathbb{R}$ that is $\Delta_1$ over $H(\omega_2)$ in a parameter $A\subseteq\omega_1$ (Caicedo–Veličković 2006); hence $\mathrm{BPFA}\Rightarrow \mathbb{R}$ has a $\Sigma_3$ well-order.
- **Consistency strength (exact).** $\mathrm{Con}(\mathrm{ZFC}+\mathrm{BPFA}) \iff \mathrm{Con}(\mathrm{ZFC}+\exists\text{ reflecting cardinal})$ (Goldstern–Shelah 1995). The same bound holds for the bounded semiproper forcing axiom.
- **Negative separations.** Since PFA implies $\neg\square_\kappa$ for all uncountable $\kappa$ — a statement whose strength exceeds an inner model with a Woodin cardinal — and BPFA has strength only a reflecting cardinal, **BPFA cannot imply $\neg\square_\kappa$ for singular $\kappa$**. This is a proof-free separation by strength alone, and it fixes the ceiling on what BPFA can decide at cardinals $>\omega_2$.

## 5. Principal Obstacles

- **Strength ceiling.** Any BPFA consequence must be provable in a model built by a countable-support iteration over a reflecting cardinal, i.e. over an $L$-like ground model. Every technique that derives PFA consequences from *elementary embeddings* (generic ultrapowers, ideal saturation, stationary tower) is unavailable: BPFA is consistent with $V=L[A]$-style fine structure below $\omega_2$.
- **Only $\Sigma_1$ reflection.** Bagaria's characterization gives absoluteness for $\Sigma_1$ statements about $H(\omega_2)$. Tree property at $\omega_2$, stationary reflection at $\omega_2$ and $\neg\square(\omega_2)$ are naturally $\Pi_1$ or $\Pi_2$ over $H(\omega_3)$; there is no known way to convert them into a $\Sigma_1(H(\omega_2))$ witness, because the witness (a branch, a reflecting point, a thread) has size $\aleph_2$ and does not live in $H(\omega_2)$.
- **Boundedness kills genericity.** In PFA one meets $\aleph_1$ *dense sets*, which produces a filter generic enough to build objects of size $\aleph_1$ by transfinite recursion. BPFA only meets antichains of size $\le\aleph_1$, so the resulting filter need not be $N$-generic for a chosen countable model, and the standard "run the recursion inside the extension, pull it back" argument breaks at limit stages.
- **Core model induction stalls.** Lower-bound computations for BMM require a precipitous or saturated ideal on $\omega_1$ as an extra hypothesis (Claverie–Schindler). Without it, $K$ exists but the $\Sigma_1$-absoluteness supplied by BMM does not obviously contradict its covering properties.

## 6. The Gap

Proven: BPFA $\Rightarrow$ $2^{\aleph_0}=\aleph_2$, MRP, five-element basis, $\Delta_1$-well-order, and BPFA is equiconsistent with a reflecting cardinal. Unproven: any statement about $\omega_2$ itself whose consistency strength exceeds a reflecting cardinal, and any $\Pi_2$ statement about $H(\omega_2)$ that needs an $\aleph_2$-sized witness.

The precise barrier: **exhibit a model of BPFA $+$ $\square(\omega_2)$ (or BPFA $+$ an $\omega_2$-Aronszajn tree), or convert the $\Pi_1$ tree-property statement into $\Sigma_1(H(\omega_2))$ form.** The first is expected — the standard Goldstern–Shelah iteration over $L$-like grounds plausibly preserves a square sequence — but no preservation theorem for $\square(\omega_2)$ under countable support proper iteration of length a reflecting cardinal is known. The second is likely impossible, and a proof of impossibility would be a genuine theorem about the expressive strength of bounded axioms.

## 7. Current Research (as of June 2026)

- **Münster (Schindler and collaborators).** Inner-model-theoretic calibration of BMM and of BPFA$^{++}$-style strengthenings; core model induction under bounded axioms plus ideal hypotheses. *(frontier — verify)* Continuing work on whether BMM $+$ "$\omega_1$ is $V$-generically inaccessible" reaches $\mathrm{AD}^{L(\mathbb{R})}$.
- **Barcelona (Bagaria, Asperó).** Generic absoluteness principles graded by quantifier complexity ($\Sigma_2$-absoluteness for $H(\omega_2)$, $(*)$-style axioms), and the effect of bounded axioms on the continuum.
- **Toronto/Cornell (Todorčević, Moore school).** Walks on ordinals, $\rho$-functions and oscillation used to squeeze further $\Sigma_1(H(\omega_2))$ consequences out of BPFA; the open status of Baumgartner's axiom (all $\aleph_1$-dense sets of reals isomorphic) under BPFA is a live target *(frontier — verify)*.
- **Vienna/Jerusalem.** Preservation theorems for iterated proper forcing aimed at producing BPFA models with prescribed behaviour at $\omega_2$ and $\omega_3$.

## 8. Future Work

- Prove or refute a preservation theorem: countable support iterations forcing BPFA over $L[A]$ preserve $\square(\omega_2)$.
- Determine whether BPFA implies the tree property at $\omega_2$; strength considerations do not immediately forbid it, since the tree property at $\omega_2$ has weakly-compact strength, below a reflecting cardinal.
- Pin BMM's strength without ideal hypotheses; Schindler's programme suggests the answer is an inner model with a Woodin cardinal.
- Classify which $\Sigma_1(H(\omega_2))$ consequences of PFA are already theorems of BPFA — a complete answer would say that PFA and BPFA have the same $\Sigma_2$ theory of $H(\omega_2)$.
- Study bounded versions of $(*)$ and their interaction with Asperó–Schindler's $\mathrm{MM}^{++}\Rightarrow(*)$.

## 9. Key References

- **[Foundational]** M. Goldstern, S. Shelah. *The Bounded Proper Forcing Axiom.* Journal of Symbolic Logic 60(1), 58–73, 1995.
- **[Foundational]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics 127(1), 1–47, 1988.
- **[Foundational]** J. Bagaria. *Bounded forcing axioms as principles of generic absoluteness.* Archive for Mathematical Logic 39(6), 393–401, 2000.
- **[SOTA]** S. Todorčević. *Generic absoluteness and the continuum.* Mathematical Research Letters 9(4), 465–471, 2002.
- **[SOTA]** J. T. Moore. *Set mapping reflection.* Journal of Mathematical Logic 5(1), 87–97, 2005.
- **[SOTA]** J. T. Moore. *A five element basis for the uncountable linear orders.* Annals of Mathematics 163(2), 669–688, 2006.
- **[SOTA]** A. E. Caicedo, B. Veličković. *The bounded proper forcing axiom and well orderings of the reals.* Mathematical Research Letters 13(3), 393–408, 2006.
- **[SOTA]** R. Schindler. *Proper forcing and remarkable cardinals II.* Journal of Symbolic Logic 66(3), 1481–1492, 2001.
- **[SOTA]** B. Claverie, R. Schindler. *Woodin's axiom $(*)$, bounded forcing axioms, and precipitous ideals on $\omega_1$.* Journal of Symbolic Logic 77(2), 475–498, 2012.
- **[Recent]** D. Asperó, R. Schindler. *Martin's Maximum$^{++}$ implies Woodin's Axiom $(*)$.* Annals of Mathematics 193(3), 793–835, 2021.
- **[Survey]** D. Asperó, J. Bagaria. *Bounded forcing axioms and the continuum.* Annals of Pure and Applied Logic 109(3), 3–14, 2001.
- **[Survey]** J. T. Moore. *The Proper Forcing Axiom.* Proceedings of the International Congress of Mathematicians, Hyderabad, Vol. II, 3–29, 2010.
- **[Textbook]** S. Shelah. *Proper and Improper Forcing.* 2nd ed., Springer, 1998.

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathrm{BFA}(\text{ccc}) = \mathrm{MA}_{\aleph_1}$, so BPFA $\Rightarrow \mathrm{MA}_{\aleph_1}$; but the bound cannot be dropped for arbitrary posets.

*Step 1 (boundedness is free for ccc).* Let $\mathbb{P}$ be ccc and $\{D_\alpha:\alpha<\omega_1\}$ dense open. For each $\alpha$ choose a maximal antichain $A_\alpha \subseteq D_\alpha$. By ccc, $|A_\alpha|\le\aleph_0 \le \aleph_1$. Applying BPFA (ccc posets are proper) yields a filter $G$ with $G\cap A_\alpha \ne\emptyset$ for all $\alpha$, hence $G\cap D_\alpha \ne\emptyset$. That is exactly $\mathrm{MA}_{\aleph_1}$.

*Step 2 (a numeric instance).* Let $T$ be an Aronszajn tree of size $\aleph_1$ and $\mathbb{P}_T$ the poset of finite specializing functions $p: T \to \omega$ with $p(s)\ne p(t)$ whenever $s <_T t$. Baumgartner–Malitz–Reinhardt: $\mathbb{P}_T$ is ccc. For $t\in T$ set $D_t=\{p : t\in\mathrm{dom}(p)\}$; there are $\aleph_1$ such dense sets and each maximal antichain inside $D_t$ is countable. BPFA gives $G$ meeting all $D_t$; $f=\bigcup G$ specializes $T$. Consequence: under BPFA every Aronszajn tree is special, so there are no Suslin trees.

*Step 3 (why "bounded" matters).* Take $\mathbb{P}=\mathrm{Coll}(\omega,\omega_1)$, which is not proper. The sentence $\varphi$ = "there is a surjection $f:\omega\to\omega_1^V$" is $\Sigma_1$ over $H(\omega_2)$ with parameter $\omega_1^V$, and $\Vdash_{\mathbb{P}}\varphi$, but $\varphi$ fails in $V$. By Bagaria's characterization, $\mathrm{BFA}(\{\mathbb{P}\})$ fails; unrestricted BFA is inconsistent. Concretely, the maximal antichains $A_n=\{p : n\in\mathrm{dom}(p)\}$-refinements have size $\aleph_1$, and a filter meeting all of them would code a surjection $\omega\to\omega_1$ in $V$.

*Step 4 (where BPFA stops).* Contrast with $\square(\omega_2)$: a thread through a coherent sequence $\langle C_\alpha : \alpha<\omega_2\rangle$ is a club subset of $\omega_2$, an object of size $\aleph_2 \notin H(\omega_2)$. No $\Sigma_1(H(\omega_2))$ formula can assert its existence with the sequence as a parameter, so Step 1's method — read the witness out of $H(\omega_2)$ — has no analogue. This is the gap of Section 6 in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*