---
id: 08-logic-set-theory/prikry-forcing-generalization
title: "Prikry Forcing Generalization"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Prikry Forcing Generalization

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/prikry-forcing-generalization` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Prikry forcing changes the cofinality of a measurable cardinal $\kappa$ to $\omega$ while adding no bounded subsets of $\kappa$ and preserving all cardinals. Dozens of variants have been built ad hoc since 1970 (Magidor, Radin, extender-based, diagonal, supercompact, with interleaved collapses). The **Prikry forcing generalization problem** is the demand for a general theory instead of a catalog of constructions. It has three components.

1. **Axiomatization.** Find a class $\mathcal{K}$ of two-ordering forcing notions $(\mathbb{P},\le,\le^*)$ such that (i) every known Prikry-type forcing lies in $\mathcal{K}$, (ii) membership in $\mathcal{K}$ implies the Prikry property, no new bounded subsets, and the expected cardinal preservation, and (iii) $\mathcal{K}$ is closed under an iteration scheme of length $\ge\kappa^{+}$ with the correct limit behaviour.
2. **Uncountable cofinality.** Extend any such framework from $\mathrm{cf}(\kappa)=\omega$ to $\mathrm{cf}(\kappa)=\lambda$ for uncountable regular $\lambda$, where every currently known abstract framework fails.
3. **Classification (converse direction).** Is every cofinality change that adds no bounded subsets of $\kappa$ and preserves cardinals *generated* by a Prikry-type forcing over a core model — i.e. is there a representation theorem: $V\subseteq W$ with $\mathrm{cf}^{W}(\kappa)<\kappa=\mathrm{cf}^V(\kappa)$ and $\mathcal{P}(\alpha)^W=\mathcal{P}(\alpha)^V$ for all $\alpha<\kappa$ implies the existence of an inner model $M$ and a Prikry-type $\mathbb{P}\in M$ with $\kappa$ singularized by an $M$-generic for $\mathbb{P}$?

A complete solution to (1)–(2) is an axiom system plus proofs of the three closure theorems; a solution to (3) is a representation theorem or a counterexample model.

## 2. Mathematical Foundations

**Classical Prikry forcing.** Let $\kappa$ be measurable and $U$ a normal $\kappa$-complete ultrafilter on $\kappa$. Conditions of $\mathbb{P}_U$ are pairs $(s,A)$ with $s\in[\kappa]^{<\omega}$ (the *stem*), $A\in U$, $\max(s)<\min(A)$. Order:
$$(t,B)\le (s,A)\iff t\sqsupseteq s,\ \ t\setminus s\subseteq A,\ \ B\subseteq A.$$
The **direct extension** order is
$$(t,B)\le^{*}(s,A)\iff t=s\ \text{ and }\ B\subseteq A .$$

**Prikry property (PP).** $(\mathbb{P},\le,\le^*)$ has PP iff for every $p\in\mathbb{P}$ and every sentence $\sigma$ of the forcing language there is $q\le^{*}p$ with $q\Vdash\sigma$ or $q\Vdash\neg\sigma$. The **Complete Prikry Property (CPP)** strengthens this to: every $p$ has a direct extension $q$ and a set $W$ of $\le$-extensions of $q$ with fixed stem-length increment such that $W$ is predense above $q$ and each element decides $\sigma$.

**The three structural facts for $\mathbb{P}_U$.**
- $\le^{*}$ is $\kappa$-closed (by $\kappa$-completeness of $U$).
- $\mathbb{P}_U$ is $\kappa^{+}$-c.c.: two conditions with the same stem are compatible, and $|[\kappa]^{<\omega}|=\kappa$.
- PP holds (Prikry 1970). Hence: no new bounded subsets of $\kappa$, all cardinals preserved, and in $V[G]$ the *Prikry sequence* $\langle\kappa_n:n<\omega\rangle=\bigcup\{s:(s,A)\in G\}$ is cofinal in $\kappa$, so $\mathrm{cf}(\kappa)=\omega$.

Genericity is characterized combinatorially (Mathias 1973): $\langle\kappa_n\rangle$ is $\mathbb{P}_U$-generic over $V$ iff $\forall A\in U\ \exists m\ \forall n\ge m\ (\kappa_n\in A)$ — the *diagonalization criterion*.

**$\Sigma$-Prikry (the current best axiomatization).** Fix $\langle\mu_n:n<\omega\rangle$ increasing with $\kappa=\sup_n\mu_n$, $\kappa$ singular in the extension. A graded triple $(\mathbb{P},\le,\le^*)$ with grading $|\cdot|:\mathbb{P}\to\omega$ is $\Sigma$-Prikry (Poveda–Rinot–Sinapova) when, among other axioms:
$$\mathbb{P}=\biguplus_{n<\omega}\mathbb{P}_n,\quad \mathbb{P}_n=\{p:|p|=n\},\qquad \le^{*}\restriction\mathbb{P}_n\ \text{is}\ \mu_n\text{-directed-closed},$$
$\mathbb{1}\Vdash\check\kappa=\check\nu^{+}$ for a fixed singular $\nu$, the triple has the CPP, $\mathbb{P}$ is $\nu^{+}$-linked in a $\mu_n$-graded way (giving $\kappa^{+}$-c.c. and preservation of $\kappa^{+}$), and each $\mathbb{P}_n$ admits a *mixing* / *weak mixing* property used to amalgamate direct extensions along $\le^*$.

**Higher cofinality (Magidor forcing).** To get $\mathrm{cf}(\kappa)=\omega_1$ one needs not one measure but a $\lhd$-increasing sequence $\langle U_\alpha:\alpha<\omega_1\rangle$ (Mitchell order), i.e. $o(\kappa)\ge\omega_1$; conditions carry countable increasing stems together with measure-one sets attached at every stem point, and $\le^*$ is defined coordinatewise.

## 3. History & State of the Art (SOTA)

- **1970.** Karel Prikry's thesis (*Changing measurable into accessible cardinals*) introduces $\mathbb{P}_U$ and PP, answering a question of Solovay on singularizing a measurable without collapsing.
- **1973–1978.** Mathias's genericity criterion; Bukovský and Dehornoy independently identify Prikry generics with the critical sequences of iterated ultrapowers — the first *classification-type* result.
- **1978.** Magidor, *Changing cofinality of cardinals*: cofinality $\lambda>\omega$ from Mitchell-order towers.
- **1982.** Radin forcing: preserves regularity/measurability of $\kappa$ while adding a club of former regulars; unifies Prikry and Magidor as degenerate cases.
- **1986–1992.** Gitik's non-stationary-ideal forcing (cofinality change from a strongly compact-type hypothesis); Gitik–Magidor extender-based Prikry forcing gives $\mathrm{cf}(\kappa)=\omega$ with $2^{\kappa}=\kappa^{++}$ from a $(\kappa+2)$-strong cardinal — the optimal-hypothesis violation of SCH.
- **2003–2010.** Merimovich's extender-based Radin forcing; Gitik's *Prikry-type forcings* chapter (Handbook of Set Theory, 2010) becomes the reference taxonomy and explicitly poses the unification and classification questions.
- **2008–2012.** Gitik–Sharon diagonal supercompact Prikry forcing at $\aleph_{\omega}$/$\aleph_{\omega^2}$: SCH fails with the approachability property failing; Neeman and Sinapova add the tree property. These constructions are visibly variants of each other with individually re-proved PP — the concrete motivation for axiomatization.
- **2017–2024.** Cummings–Friedman–Magidor–Rinot–Sinapova give a general framework for forcings at successors of singulars; Poveda–Rinot–Sinapova's $\Sigma$-Prikry trilogy supplies axioms (I), an iteration scheme with $\kappa^{+}$-length limits (II), and a transfer down to $\aleph_\omega$ (III). This is the SOTA on component (1).

## 4. Partial Results / Verified Cases

- **$\mathrm{cf}(\kappa)=\omega$, single normal measure:** fully solved (Prikry 1970); genericity characterized (Mathias 1973).
- **$\mathrm{cf}(\kappa)=\lambda$ for regular $\lambda<\kappa$:** solved from $o(\kappa)\ge\lambda$ (Magidor 1978); generic sequences characterized by Fuchs (2005, 2014) for Magidor- and Prikry-type sequences over iterable inner models.
- **Class covered by $\Sigma$-Prikry axioms:** Prikry forcing, Prikry with interleaved collapses, the Gitik–Sharon diagonal forcing, extender-based Prikry forcing (with and without collapses), and the "$\aleph_\omega$" versions — all verified instances, all with $\mathrm{cf}(\kappa)=\omega$ and $\kappa$ a successor of a singular in the target model.
- **Iteration:** $\Sigma$-Prikry II proves closure of the class under iterations of length $\le\kappa^{+}$ with the right support, yielding e.g. $\mathrm{Refl}(\aleph_{\omega+1})$ together with $\neg\mathrm{SCH}_{\aleph_\omega}$ — previously each such combination needed a bespoke forcing.
- **Lower bounds (converse direction, partial):** by Dodd–Jensen covering and its extensions, singularizing $\kappa$ without collapsing requires inner-model measures; Gitik's analyses show $\mathrm{cf}(\kappa)$ changing with $\mathcal{P}(\alpha)$ unchanged for $\alpha<\kappa$ implies $\kappa$ carries measures in $K$ of Mitchell rank tied to the new cofinality. So (3) is proved *at the level of consistency strength*, not as a representation theorem.
- **Optimal hypotheses for SCH failure:** $\neg\mathrm{SCH}$ at $\kappa$ with $\mathrm{cf}(\kappa)=\omega$ is equiconsistent with a $(\kappa+2)$-strong cardinal (Gitik–Magidor upper bound, Gitik lower bound) — the sharpest quantitative success of the generalized machinery.

## 5. Principal Obstacles

- **Uncountable cofinality breaks the grading.** The $\Sigma$-Prikry axioms grade $\mathbb{P}$ by $\omega$ ($|p|\in\omega$) so that "one more stem point" is a finite step and $\le^*$-closure degrees $\mu_n$ increase cofinally. For $\mathrm{cf}(\kappa)=\omega_1$ stems are countable and *limit* stages appear: a $\le^*$-decreasing $\omega_1$-chain of conditions must be amalgamated at limits, and the natural diagonal intersection of $\omega_1$-many measure-one sets is not measure-one for a single measure. Magidor's fix — a Mitchell-increasing tower — is not expressible as a grading, so no known axiom set has both PP and an iteration theorem at uncountable cofinality.
- **Failure of Rowbottom-style homogeneity beyond normality.** The proof of PP for $\mathbb{P}_U$ uses normality to reduce a $[\kappa]^{n}$-colouring to a homogeneous set. Extender-based and diagonal variants replace $U$ by systems of non-normal or non-$\kappa$-complete objects; homogeneity must be recovered by hand each time, and no combinatorial invariant is known that predicts when it can be.
- **No canonical form for generics.** Mathias's criterion is a genuine characterization only for one measure. For extender-based forcings the generic object is a system of functions with commuting conditions; there is no known "diagonalization criterion", which blocks the representation theorem in (3).
- **Cardinal-arithmetic side conditions interact.** Adding collapses (needed to move to $\aleph_\omega$) destroys $\le^*$-closure unless the collapse is threaded through the grading; PCF-theoretic constraints (Shelah's bounds on $2^{\aleph_\omega}$, scales, approachability) mean the framework must control $\square$-like principles that are not part of any forcing-theoretic axiom.
- **Core-model limits.** The lower-bound machinery (covering lemmas) is available only up to the current reach of inner-model theory; a full converse for extender-based cofinality changes needs core models at the level of long extenders, which do not yet exist.

## 6. The Gap

Proven: an axiomatic class ($\Sigma$-Prikry) closed under $\kappa^{+}$-length iterations covering all known $\mathrm{cf}=\omega$ constructions, plus optimal consistency-strength calibrations for cofinality change. Sought: (a) an analogue where $\omega$ is replaced by an uncountable regular $\lambda$ — precisely, an axiom implying PP that is preserved at $\le^{*}$-limits of length $<\lambda$ and closed under iteration; and (b) a representation theorem replacing the consistency-strength lower bounds by an actual generic-extension decomposition. The exact step in (a) is a **limit-amalgamation lemma**: given a $\le^{*}$-decreasing sequence $\langle p_\alpha:\alpha<\delta\rangle$, $\delta<\lambda$, produce $p_\delta\le^{*}p_\alpha$ for all $\alpha$ using only the axioms — currently possible only via an externally supplied Mitchell tower. The exact step in (b) is to prove that the generic object of an arbitrary such extension satisfies a diagonalization criterion over a definable inner model.

## 7. Current Research (as of June 2026)

- **Tel Aviv / Bar-Ilan / Jerusalem (Gitik, Rinot, Ben-Neria, Hayut).** Extending $\Sigma$-Prikry to non-$\omega$ cofinality and to $\kappa$ not a successor of a singular; combining with reflection and stationary-set-splitting principles. *(frontier — verify)*
- **Poveda (Harvard/Hebrew University) and Sinapova (Rutgers).** Iteration schemes of length $>\kappa^{+}$ and "$\Sigma$-Prikry with collapses" applied to compactness at $\aleph_{\omega+1}$: tree property, failure of approachability, and stationary reflection simultaneously with $\neg$SCH. *(frontier — verify)*
- **Merimovich and collaborators.** Extender-based Radin/Magidor hybrids as candidate uncountable-cofinality instances of a future framework.
- **Inner-model side (Schindler, Steel school).** Covering-type theorems for extender models aimed at the converse direction.
- **Set-theoretic geology / generic-multiverse reformulation.** Asking whether $V$ is a Prikry-type extension of a ground model is a mantle/ground-model definability question; the Fuchs–Hamkins–Reitz ground-model definability theorem makes the question first-order expressible. *(frontier — verify)*

## 8. Future Work

- Isolate a **$\lambda$-graded Prikry axiom**: grade by $\lambda$ rather than $\omega$, with $\le^*$-closure and a built-in coherence requirement replacing the Mitchell tower, then prove PP and an iteration theorem.
- Prove or refute a **Mathias-type criterion for extender-based generics**; a positive answer would immediately give a representation theorem for the SCH-failure models.
- Develop a **category/comparison framework**: define morphisms between Prikry-type triples (projections, $\le^*$-preserving embeddings) and classify known forcings up to such morphisms — Radin forcing as a terminal object is the natural test case.
- Push the **lower bounds**: derive from a cardinal-preserving cofinality change at $\kappa$ with $\mathrm{cf}(\kappa)=\omega_1$ the existence of an inner model with $o(\kappa)\ge\omega_1$ in full generality.
- Apply the framework to **$\aleph_{\omega}$-specific arithmetic**: whether $2^{\aleph_\omega}$ can be made large while $\aleph_{\omega+1}$ has strong compactness-like properties, within one uniform iteration.

## 9. Key References

- **[Foundational]** K. Prikry. *Changing measurable into accessible cardinals.* Dissertationes Mathematicae 68 (1970), 5–52.
- **[Foundational]** M. Magidor. *Changing cofinality of cardinals.* Fundamenta Mathematicae 99 (1978), 61–71.
- **[Foundational]** A. R. D. Mathias. *On sequences generic in the sense of Prikry.* Journal of the Australian Mathematical Society 15 (1973), 409–414.
- **[Foundational]** L. B. Radin. *Adding closed cofinal sequences to large cardinals.* Annals of Mathematical Logic 22 (1982), 243–261.
- **[Foundational]** P. Dehornoy. *Iterated ultrapowers and Prikry forcing.* Annals of Mathematical Logic 15 (1978), 109–160.
- **[Survey]** M. Gitik. *Prikry-type forcings.* In: M. Foreman, A. Kanamori (eds.), *Handbook of Set Theory*, Springer, 2010, pp. 1351–1447.
- **[Foundational]** M. Gitik, M. Magidor. *The singular cardinal hypothesis revisited.* In: *Set Theory of the Continuum*, MSRI Publications 26, Springer, 1992, pp. 243–279.
- **[Foundational]** M. Gitik. *Changing cofinalities and the nonstationary ideal.* Israel Journal of Mathematics 56 (1986), 280–314.
- **[SOTA / Recent]** A. Poveda, A. Rinot, D. Sinapova. *Sigma-Prikry forcing I: The axioms.* Canadian Journal of Mathematics 73 (2021), 1205–1238.
- **[SOTA / Recent]** A. Poveda, A. Rinot, D. Sinapova. *Sigma-Prikry forcing II: Iteration scheme.* Journal of Mathematical Logic 22 (2022), no. 3.
- **[SOTA / Recent]** A. Poveda, A. Rinot, D. Sinapova. *Sigma-Prikry forcing III: Down to $\aleph_\omega$.* Preprint/article in the Sigma-Prikry series, 2020–2023.
- **[SOTA / Recent]** J. Cummings, S.-D. Friedman, M. Magidor, A. Rinot, D. Sinapova. *A framework for forcing constructions at successors of singular cardinals.* Transactions of the American Mathematical Society 369 (2017), 7405–7441.
- **[Recent]** M. Gitik, A. Sharon. *On SCH and the approachability property.* Proceedings of the American Mathematical Society 136 (2008), 311–320.
- **[Recent]** I. Neeman. *Aronszajn trees and failure of the singular cardinal hypothesis.* Journal of Mathematical Logic 9 (2009), 139–157.
- **[Recent]** D. Sinapova. *The tree property and the failure of the singular cardinal hypothesis at $\aleph_{\omega^2}$.* Journal of Symbolic Logic 77 (2012), 934–946.
- **[Recent]** C. Merimovich. *Extender-based Radin forcing.* Transactions of the American Mathematical Society 355 (2003), 1729–1772.
- **[Structural]** G. Fuchs. *A characterization of generalized Příkrý sequences.* Archive for Mathematical Logic 44 (2005), 935–971.
- **[Background]** A. Dodd, R. Jensen. *The core model.* Annals of Mathematical Logic 20 (1981), 43–75.

## 10. Worked Example / Concrete Special Case

**(a) PP for $\mathbb{P}_U$, computed.** Let $\sigma$ be a sentence and $p=(s,A)$. For each $n<\omega$ define a colouring $c_n:[A]^{n}\to\{0,1,2\}$ by
$$c_n(x)=\begin{cases}0 & \exists B\in U:\ (s\cup x,B)\Vdash\sigma,\\ 1 & \exists B\in U:\ (s\cup x,B)\Vdash\neg\sigma,\\ 2 & \text{otherwise.}\end{cases}$$
Since $\kappa\to(\kappa)^{n}_{3}$ holds for measurable $\kappa$ with homogeneous sets in $U$ (Rowbottom), pick $A_n\in U$, $A_n\subseteq A$, homogeneous for $c_n$ with colour $i_n$. Put $A^{*}=\bigcap_{n<\omega}A_n\in U$ ($\kappa$-completeness, in fact only $\sigma$-completeness used here) and $q=(s,A^{*})\le^{*}p$. Claim: some $i_n\ne 2$ and then $q$ decides $\sigma$. Indeed if every extension of $q$ decided $\sigma$ only via stem growth, take $r=(s\cup x,B)\le q$, $|x|=n$, with $r\Vdash\sigma$; then $c_n(x)=0$, so $i_n=0$, so *every* $x\in[A^{*}]^{n}$ has a measure-one set forcing $\sigma$, and shrinking by the diagonal intersection $B^{*}=\triangle_{x}B_x$ gives $(s,B^{*})\Vdash\sigma$. Hence $q$ itself (after this shrinking) decides $\sigma$. Consequently, if $f:\alpha\to 2$ with $\alpha<\kappa$ is added by $G$, each value $f(\beta)$ is decided by a single $\le^{*}$-extension; $\kappa$-closure of $\le^{*}$ concatenates $\alpha$-many such extensions into one condition computing $f$ in $V$. **No bounded subsets of $\kappa$ are added.**

**(b) Where the generalization to $\mathrm{cf}(\kappa)=\omega_1$ fails.** Attempt the same with countable stems: conditions $(s,A)$, $s\in[\kappa]^{\le\omega}$ increasing, $A\in U$, $\sup(s)<\min(A)$. Two failures are immediate and quantitative.
- *Cofinality of stems.* A $\le$-increasing $\omega$-chain of conditions with stems $s_0\subsetneq s_1\subsetneq\cdots$ has union with $\sup_n\sup(s_n)=\delta$; to continue one needs $\delta\in$ some measure-one set, but the generic sequence must be *continuous* at $\delta$, i.e. $\delta$ itself must appear in the sequence — and $\delta$ has cofinality $\omega$, so $\delta$ cannot be measurable and carries no measure to attach. A single $U$ provides nothing at $\delta$.
- *Repair by Mitchell towers.* Magidor's solution assigns to each stem point $\alpha$ a measure $U_{\alpha}$ from a $\lhd$-increasing sequence $\langle U_\xi:\xi<\omega_1\rangle$ with $U_\xi\in\mathrm{Ult}(V,U_\eta)$ for $\xi<\eta$; the condition at $\delta$ is then built from $U_{\mathrm{ot}(s)}$, and coherence of the tower makes the $\omega_1$-many measure-one sets amalgamate. This needs $o(\kappa)\ge\omega_1$, strictly stronger than measurability.

The gap of Section 6 is exactly the passage from step (a), which the $\Sigma$-Prikry axioms abstract successfully, to step (b), whose repair is still supplied by an external large-cardinal structure rather than by an axiom.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*