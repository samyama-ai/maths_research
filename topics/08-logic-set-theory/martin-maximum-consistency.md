---
id: 08-logic-set-theory/martin-maximum-consistency
title: "Martin Maximum Consistency"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Martin's Maximum: Consistency Strength and Maximality

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/martin-maximum-consistency` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Martin's Maximum ($\mathrm{MM}$) is the forcing axiom $\mathrm{FA}_{\aleph_1}(\Gamma)$ for $\Gamma$ the class of all stationary-set-preserving posets. Foreman, Magidor and Shelah (1988) proved $\mathrm{Con}(\text{supercompact}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{MM})$, and that $\Gamma$ is provably the largest class for which such an axiom can hold. What remains open is the **exact consistency strength**:

> **Problem.** Determine the least large-cardinal hypothesis $\Phi$ with $\mathrm{Con}(\mathrm{ZFC}+\Phi) \Leftrightarrow \mathrm{Con}(\mathrm{ZFC}+\mathrm{MM})$. In particular: does $\mathrm{ZFC} + \mathrm{MM}$ prove $\mathrm{Con}(\mathrm{ZFC} + \exists\,\text{supercompact})$?

A resolution means either (a) an inner-model / core-model-induction argument deriving a supercompact-strength model from $\mathrm{MM}$, or (b) a forcing construction producing a model of $\mathrm{MM}$ from a strictly weaker hypothesis. Subsidiary open questions: is $\mathrm{MM}$ strictly weaker than $\mathrm{MM}^{++}$? Does plain $\mathrm{MM}$ imply Woodin's axiom $(*)$?

## 2. Mathematical Foundations

**Stationarity.** For a regular $\kappa > \omega$, $S \subseteq \kappa$ is *stationary* if $S \cap C \neq \emptyset$ for every club $C \subseteq \kappa$. Write $E^{\kappa}_{\lambda} = \{\alpha<\kappa : \mathrm{cf}(\alpha)=\lambda\}$. $\mathrm{NS}_{\omega_1}$ is the nonstationary ideal on $\omega_1$.

**Preservation class.** A poset $\mathbb{P}$ is *stationary-set-preserving* (SSP) if
$$\Vdash_{\mathbb{P}}\ \check{S}\ \text{is stationary in}\ \omega_1 \quad\text{for every stationary } S\subseteq\omega_1 .$$
Note $\text{proper} \subsetneq \text{semiproper} \subsetneq \mathrm{SSP}$, and every SSP poset preserves $\omega_1$.

**Forcing axiom.** For a class $\Gamma$,
$$\mathrm{FA}_{\aleph_1}(\Gamma):\quad \forall\,\mathbb{P}\in\Gamma\ \ \forall\,\langle D_\alpha : \alpha<\omega_1\rangle \text{ dense in } \mathbb{P}\ \ \exists\ \text{filter } G \text{ with } G\cap D_\alpha\neq\emptyset\ \forall\alpha .$$
Then $\mathrm{MA}_{\aleph_1} = \mathrm{FA}_{\aleph_1}(\mathrm{ccc})$, $\mathrm{PFA} = \mathrm{FA}_{\aleph_1}(\text{proper})$, $\mathrm{SPFA}=\mathrm{FA}_{\aleph_1}(\text{semiproper})$, and
$$\boxed{\ \mathrm{MM} \;=\; \mathrm{FA}_{\aleph_1}(\mathrm{SSP}).\ }$$

**Plus versions.** $\mathrm{MM}^{++}$ additionally demands that for any $\aleph_1$-sized family $\langle \dot{S}_i : i<\omega_1\rangle$ of $\mathbb{P}$-names for stationary subsets of $\omega_1$, the filter $G$ can be chosen so that $\{\alpha : \exists p \in G\ p\Vdash \check\alpha\in\dot S_i\}$ is stationary for each $i$. Viale's $\mathrm{MM}^{+++}$ strengthens this to a generic-absoluteness scheme for the $\Sigma_2$-theory of $H_{\aleph_2}$ under SSP forcing.

**Consequences (all theorems of $\mathrm{ZFC}+\mathrm{MM}$).**
$$2^{\aleph_0}=\aleph_2,\qquad \mathrm{NS}_{\omega_1}\ \text{is}\ \aleph_2\text{-saturated},\qquad \mathrm{SCH},$$
$$\square_\kappa \text{ fails for all uncountable } \kappa,\qquad \text{every stationary } S\subseteq E^{\omega_2}_{\omega} \text{ reflects},$$
$$\mathrm{AD}^{L(\mathbb{R})},\qquad \omega_2 \text{ is generically supercompact via SSP forcing.}$$

**Key equivalence (Shelah).** $\mathrm{SPFA} \Leftrightarrow \mathrm{MM}$: $\mathrm{SPFA}$ implies $\mathrm{NS}_{\omega_1}$ is saturated, which implies every SSP poset is semiproper.

## 3. History & State of the Art (SOTA)

- **1984.** Baumgartner and Todorcevic establish $\mathrm{PFA}$'s consistency from a supercompact via countable-support iteration; Todorcevic proves $\mathrm{PFA}\Rightarrow \neg\square_\kappa$.
- **1988.** Foreman, Magidor, Shelah, *Annals of Mathematics* 127 (Parts I and II): definition of $\mathrm{MM}$, the maximality theorem, consistency from a supercompact $\kappa$ via a revised-countable-support iteration of length $\kappa$ with Laver-function bookkeeping, and the derivations $2^{\aleph_0}=\aleph_2$ and saturation of $\mathrm{NS}_{\omega_1}$.
- **1999.** Woodin's $\mathbb{P}_{\max}$ machinery isolates $(*)$: $\mathrm{AD}$ holds in $L(\mathbb{R})$ and $L(\mathcal{P}(\omega_1))$ is a $\mathbb{P}_{\max}$-extension of $L(\mathbb{R})$. Woodin proves $\mathrm{MM}^{++}\Rightarrow \psi_{\mathrm{AC}}$.
- **2005.** Steel: $\mathrm{PFA}\Rightarrow \mathrm{AD}^{L(\mathbb{R})}$, by core model induction — the first lower bound past measurables for the whole axiom.
- **2015–2024.** Sargsyan's hod-mouse program and Sargsyan–Trang's *Largest Suslin Axiom* raise core-model-induction lower bounds for $\mathrm{PFA}/\mathrm{MM}$ well into the region of $\mathrm{AD}_{\mathbb{R}} + \text{"}\Theta$ regular$\text{"}$ and beyond.
- **2021.** Asperó–Schindler, *Annals of Mathematics* 193: $\mathrm{MM}^{++} \Rightarrow (*)$. This settled a 25-year-old question and unified the two maximality programs for $H_{\aleph_2}$.

**Current bounds.** Upper: one supercompact. Lower: determinacy-level hypotheses (far below a Woodin limit of Woodins, hence far below a supercompact). The gap is the entire hierarchy from $\mathrm{AD}_{\mathbb{R}}$-style axioms through superstrong and subcompact cardinals.

## 4. Partial Results / Verified Cases

- **Upper bound, exact form.** From $\kappa$ supercompact, the FMS iteration gives $\mathrm{MM}^{++}$ (indeed $\mathrm{MM}^{+\omega_1}$) in $V^{\mathbb{P}}$ with $\kappa=\omega_2^{V^{\mathbb{P}}}$. Viale showed $\mathrm{MM}^{+++}$ is forceable from the same hypothesis.
- **Fragments with known exact strength.** $\mathrm{MA}_{\aleph_1}$: equiconsistent with $\mathrm{ZFC}$. $\mathrm{BPFA}$ (bounded PFA): equiconsistent with a $\Sigma_2$-reflecting cardinal (Goldstern–Shelah). $\mathrm{BMM}$ (bounded MM): strictly stronger — Claverie–Schindler show $\mathrm{BMM}$ plus a precipitous ideal on $\omega_1$ yields inner models with Woodin cardinals; $\mathrm{BMM}$ alone gives inner models with strong cardinals for every set.
- **$(*)$ has exact strength.** $\mathrm{Con}((*)) \Leftrightarrow \mathrm{Con}(\mathrm{ZF}+\mathrm{AD}) \Leftrightarrow \mathrm{Con}(\omega \text{ Woodin cardinals})$. Since $\mathrm{MM}^{++}\Rightarrow(*)$ but not conversely (e.g. $(*)$ is consistent with $\square_{\omega_2}$-type failures of $\mathrm{MM}$'s reflection), $\mathrm{MM}^{++}$ is strictly stronger than $\omega$ Woodins.
- **Localized versions.** $\mathrm{MM}(\mathfrak{c})$ and $\mathrm{MM}^{++}(\mathfrak{c})$, restricted to posets of size $\le \mathfrak{c}$, have been separated from the full axiom by Larson.
- **Maximality is a theorem, not a conjecture.** For any $\mathbb{P}$ that destroys the stationarity of some $S\subseteq\omega_1$, $\mathrm{FA}_{\aleph_1}(\{\mathbb{P}\})$ is outright false (Section 10).

## 5. Principal Obstacles

- **No inner model theory at the supercompact level.** Core model induction produces canonical inner models with Woodin cardinals and, via hod mice, models of $\mathrm{AD}_{\mathbb{R}}$-strength. There is no fine-structural $K^{\text{supercompact}}$: iterability at the level of long extenders confronts the Kunen inconsistency-adjacent phenomena and the unsolved *iterability conjecture* for background-certified $\Sigma$-mice. Without such a model, one cannot run the covering/condensation dichotomy that converts $\mathrm{MM}$'s reflection into a supercompactness measure.
- **$\mathrm{MM}$ only sees $H_{\aleph_2}$ directly.** All of $\mathrm{MM}$'s combinatorial power is a statement about $\aleph_1$-many dense sets, i.e. about $H_{\aleph_2}$; supercompactness is a statement about arbitrarily large $\lambda$. The generic supercompactness of $\omega_2$ that $\mathrm{MM}$ yields is *generic*, and generic embeddings need not have well-founded targets in $V$, so they cannot be directly turned into $V$-measures.
- **Iteration-theoretic ceiling on the upper bound.** Every known method for forcing $\mathrm{MM}$ needs a Laver function on the iteration length to anticipate arbitrary SSP posets appearing at later stages; only supercompactness (or Neeman-style virtual variants) supplies such anticipation. Reflection principles below a supercompact do not close the bookkeeping.
- **Semiproperness is not preserved by iteration in general.** RCS iteration of semiproper posets requires the saturation of $\mathrm{NS}_{\omega_1}$ or Shelah's semiproper-iteration theorem with strong cardinal-arithmetic side conditions; weakening the hypothesis breaks preservation at inaccessible stages.

## 6. The Gap

Proven: $\mathrm{Con}(\text{supercompact}) \Rightarrow \mathrm{Con}(\mathrm{MM}^{+++}) \Rightarrow \mathrm{Con}(\mathrm{MM}^{++}) \Rightarrow \mathrm{Con}(\mathrm{MM}) \Rightarrow \mathrm{Con}(\mathrm{AD}^{L(\mathbb{R})} + \text{hod-mouse hypotheses})$.

The gap is everything strictly between "determinacy-level" and "supercompact": Woodin limits of Woodins, superstrongs, subcompacts, extendibles. Crossing it from below requires a **core model induction that survives past the Solovay hierarchy** — a self-iterable hierarchy of hod mice at long-extender level. Crossing it from above requires an **anticipation device weaker than a Laver function**, i.e. a forcing construction of $\mathrm{MM}$ from, say, a Woodin limit of Woodins. Neither direction has a candidate proof; even the analogous, easier question for $\mathrm{PFA}$ is open after 40 years.

## 7. Current Research (as of June 2026)

- **Hod mice and $\mathrm{LSA}$.** Sargsyan (Gdańsk/IMPAN) and Trang (North Texas) continue extending the core model induction beyond the Largest Suslin Axiom; the target is a lower bound for $\mathrm{PFA}$/$\mathrm{MM}$ at the level of "$\mathrm{AD}^+ + \Theta$ is a limit of Woodins in HOD" and past *Sealing*. *(frontier — verify)*
- **Consequences of $(*)$-type axioms.** Post-Asperó–Schindler work (Schindler's Münster group, Asperó in East Anglia) studies $(*)^{++}$, $\mathrm{MM}^{+++}$ and whether $\mathrm{MM}$ itself implies $(*)$; also whether $(*)^{++}$ follows from $\mathrm{MM}^{++}$.
- **Virtual and generic large cardinals.** Programs replacing supercompactness with generic/virtual embeddings (Gitman, Schindler, Bagaria) explore whether $\mathrm{MM}$-fragments can be forced from remarkable-cardinal-level hypotheses.
- **Higher forcing axioms.** Neeman-style side-condition forcing and Asperá–Mota's finite-condition iterations give $\mathrm{MM}$-like axioms at $\aleph_2$ and above; their strengths sit in the same unresolved region. *(frontier — verify)*

## 8. Future Work

- Prove $\mathrm{MM}\Rightarrow \mathrm{Con}(\text{superstrong})$: the natural next milestone past the current determinacy-level bounds.
- Settle whether $\mathrm{MM}$ and $\mathrm{MM}^{++}$ are equiconsistent, or produce a model of $\mathrm{MM} + \neg(*)$.
- Develop background-certified long-extender mice with a proved iterability, closing the inner-model gap.
- Isolate a "Laver-like" reflection principle strictly below supercompactness sufficient for the RCS bookkeeping.
- Determine the strength of $\mathrm{BMM}$ exactly — a tractable test case with the same obstruction profile.

## 9. Key References

- **[Foundational]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and nonregular ultrafilters. Part I.* Annals of Mathematics 127 (1988), 1–47.
- **[Foundational]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and nonregular ultrafilters. Part II.* Annals of Mathematics 127 (1988), 521–545.
- **[Foundational]** S. Shelah. *Proper and Improper Forcing.* 2nd ed., Springer, 1998.
- **[Foundational]** S. Todorcevic. *A note on the proper forcing axiom.* Contemporary Mathematics 31 (1984), 209–218.
- **[SOTA / Recent]** D. Asperó, R. Schindler. *Martin's Maximum$^{++}$ implies Woodin's axiom $(*)$.* Annals of Mathematics 193 (2021), 793–835.
- **[SOTA / Recent]** M. Viale. *Martin's maximum revisited.* Archive for Mathematical Logic 55 (2016), 295–317.
- **[SOTA / Recent]** J. R. Steel. *PFA implies $\mathrm{AD}^{L(\mathbb{R})}$.* Journal of Symbolic Logic 70 (2005), 1255–1296.
- **[SOTA / Recent]** B. Claverie, R. Schindler. *Woodin's axiom $(*)$, bounded forcing axioms, and precipitous ideals on $\omega_1$.* Journal of Symbolic Logic 77 (2012), 475–498.
- **[SOTA / Recent]** P. Larson. *Martin's Maximum and the $\mathbb{P}_{\max}$ axiom $(*)$.* Annals of Pure and Applied Logic 106 (2000), 135–149.
- **[SOTA / Recent]** G. Sargsyan, N. Trang. *The Largest Suslin Axiom.* Lecture Notes in Logic, Cambridge University Press / ASL, 2024.
- **[Survey]** W. H. Woodin. *The Axiom of Determinacy, Forcing Axioms, and the Nonstationary Ideal.* De Gruyter, 1999; 2nd revised ed. 2010.
- **[Survey]** J. T. Moore. *The proper forcing axiom.* Proceedings of the ICM 2010, Vol. II, 3–29.
- **[Survey]** M. Foreman. *Ideals and generic elementary embeddings.* In: Handbook of Set Theory, Springer, 2010, 885–1147.
- **[Survey]** P. Larson. *The Stationary Tower: Notes on a Course by W. Hugh Woodin.* AMS University Lecture Series 32, 2004.
- **[Reference]** T. Jech. *Set Theory,* 3rd millennium edition. Springer, 2003.

## 10. Worked Example / Concrete Special Case

**Claim (FMS maximality).** No forcing axiom at $\aleph_1$ can extend beyond SSP posets. Concretely: if $\mathbb{P}$ destroys the stationarity of some $S\subseteq\omega_1$, then $\mathrm{FA}_{\aleph_1}(\{\mathbb{P}\})$ is false.

**Instance.** Fix $S\subseteq\omega_1$ stationary with $T=\omega_1\setminus S$ also stationary (such $S$ exists by Solovay's splitting theorem). Let
$$\mathbb{P}_T=\{\,p \subseteq T : p \text{ is a countable, closed, bounded subset of } \omega_1\,\},$$
ordered by end-extension: $q\le p$ iff $q\cap(\max p + 1)=p$.

*Step 1 — $\mathbb{P}_T$ is nontrivial and the dense sets exist.* For $\alpha<\omega_1$ put $D_\alpha=\{p\in\mathbb{P}_T : \max p>\alpha\}$. Given any $p$ and $\alpha$, since $T$ is stationary it is unbounded, so pick $\gamma\in T$ with $\gamma>\max(\alpha,\max p)$. Then $q=p\cup\{\gamma\}$ is countable, closed (its only new point is isolated at the top), contained in $T$, and $q\le p$, $q\in D_\alpha$. So each $D_\alpha$ is dense, and there are exactly $\aleph_1$ of them.

*Step 2 — a generic filter yields a club.* Suppose $G$ is a filter meeting every $D_\alpha$. Let $C=\bigcup G$. Since $G$ meets each $D_\alpha$, $C$ is unbounded in $\omega_1$. $C$ is closed: if $\delta=\sup(C\cap\delta)<\omega_1$, choose $p\in G$ with $\max p>\delta$ (possible via $D_\delta$). Because $G$ is a filter and conditions are end-extensions, $C\cap\delta = p\cap\delta$, so $\delta$ is a limit point of $p$; $p$ is closed, hence $\delta\in p\subseteq C$. Thus $C$ is club.

*Step 3 — contradiction.* $C\subseteq T=\omega_1\setminus S$, so $C\cap S=\emptyset$, contradicting the stationarity of $S$. Hence $\mathrm{FA}_{\aleph_1}(\{\mathbb{P}_T\})$ fails outright in $\mathrm{ZFC}$.

*Step 4 — what this shows.* $\mathbb{P}_T$ is $\omega_1$-preserving (it is even $\sigma$-distributive under $\diamondsuit$-style hypotheses on $T$) yet not SSP: it kills the stationarity of $S$. So the class SSP in the definition of $\mathrm{MM}$ cannot be enlarged, and $\mathrm{MM}$ is the literal maximum among forcing axioms at $\aleph_1$. Everything that remains open concerns not *which* class, but *how much large-cardinal strength* the resulting axiom encodes — the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*