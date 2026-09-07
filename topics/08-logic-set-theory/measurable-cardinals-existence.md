---
id: 08-logic-set-theory/measurable-cardinals-existence
title: "Measurable Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Measurable Cardinals: Existence and Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/measurable-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

An uncountable cardinal $\kappa$ is **measurable** if there is a $\kappa$-complete non-principal ultrafilter $U$ on $\kappa$ — equivalently, a two-valued measure $\mu:\mathcal{P}(\kappa)\to\{0,1\}$ that is $\kappa$-additive, vanishes on singletons, and has $\mu(\kappa)=1$.

The problem has three layers:

1. **Existence.** Is there a measurable cardinal? ZFC cannot prove there is (Section 4), and ZFC cannot prove there is not, unless ZFC + "a measurable exists" is inconsistent.
2. **Consistency.** Is $\mathrm{ZFC} + \exists\,\text{measurable}$ consistent? By Gödel's second incompleteness theorem this is not provable in ZFC + "a measurable exists" itself, and no reduction to the consistency of ZFC is possible. A *disproof* — a formal contradiction from ZFC + $\exists\kappa$ measurable — is a live logical possibility, and would be a complete resolution in the negative.
3. **Justification.** Is there principled extra-mathematical or intra-mathematical evidence (reflection principles, inner model theory, determinacy consequences) that settles which way a set theorist should bet?

The problem is marked *partially-solved* because the metamathematical status (independence, relative consistency strength, structure of canonical inner models) is completely settled, while (1)–(3) are not.

## 2. Mathematical Foundations

Work in ZFC. Let $\kappa$ be an uncountable cardinal.

**Ultrafilter form.** $U\subseteq\mathcal{P}(\kappa)$ is a *$\kappa$-complete non-principal ultrafilter* if:
$$\emptyset\notin U,\quad A\in U \wedge A\subseteq B \Rightarrow B\in U,\quad A\notin U \Leftrightarrow \kappa\setminus A\in U,$$
$$\{A_i\}_{i<\lambda}\subseteq U,\ \lambda<\kappa \ \Longrightarrow\ \bigcap_{i<\lambda}A_i\in U, \qquad \{\alpha\}\notin U \ \ \forall\alpha<\kappa.$$

**Embedding form (Keisler, Scott).** $\kappa$ is measurable iff there is an elementary embedding
$$j:V\longrightarrow M,\qquad M \text{ transitive},\ j\neq\mathrm{id},\ \mathrm{crit}(j)=\kappa,$$
where $\mathrm{crit}(j)=\min\{\alpha: j(\alpha)\neq\alpha\}$. Given $U$, form the ultrapower $\mathrm{Ult}(V,U)=\{[f]_U : f:\kappa\to V\}$ with
$$[f]_U \in_U [g]_U \iff \{\alpha<\kappa : f(\alpha)\in g(\alpha)\}\in U,$$
and Łoś's theorem gives $V\models\varphi(a) \iff \mathrm{Ult}(V,U)\models\varphi([c_a]_U)$. $\kappa$-completeness makes $\in_U$ well-founded, so Mostowski collapse yields transitive $M$ and $j_U(x)=[c_x]_U$. Conversely $U_j=\{A\subseteq\kappa : \kappa\in j(A)\}$ is a $\kappa$-complete non-principal ultrafilter.

**Normality.** $U$ is *normal* if every regressive $f:\kappa\to\kappa$ ($f(\alpha)<\alpha$ on a set in $U$) is constant on a set in $U$; equivalently $U$ is closed under diagonal intersections $\triangle_{\alpha<\kappa}A_\alpha=\{\xi<\kappa:\xi\in\bigcap_{\alpha<\xi}A_\alpha\}$; equivalently $[\mathrm{id}]_U=\kappa$. Every measurable carries a normal measure (Scott).

**Closure.** For $U$ normal, ${}^{\kappa}M\subseteq M$, $V_{\kappa+1}\subseteq M$, but $U\notin M$ and $j(\kappa)<(2^\kappa)^+$.

**Real-valued variant.** $\kappa$ is *real-valued measurable* if there is a $\kappa$-additive, atomless probability measure $\mu:\mathcal{P}(\kappa)\to[0,1]$ vanishing on singletons. This is Banach's measure problem relaxed from two-valued to $[0,1]$-valued.

**Related large cardinals.** $\kappa$ is *inaccessible* if regular and $\forall\lambda<\kappa\,(2^\lambda<\kappa)$; *Mahlo* if the regulars below $\kappa$ are stationary; *weakly compact* if $\kappa\to(\kappa)^2_2$; *Ramsey* if $\kappa\to(\kappa)^{<\omega}_2$. The chain
$$\text{inaccessible} < \text{Mahlo} < \text{weakly compact} < \text{Ramsey} < \text{measurable} < \text{strong} < \text{Woodin} < \text{supercompact}$$
orders these by consistency strength.

## 3. History & State of the Art (SOTA)

- **1930.** Ulam, *Zur Masstheorie in der allgemeinen Mengenlehre*, poses the measure problem and defines measurable cardinals; proves the first measurable is inaccessible.
- **1930s–60s.** Tarski and the Berkeley school develop the "accessible/inaccessible" framework; Hanf (1964) shows the first measurable is far above the first inaccessible, weakly compact, and Mahlo cardinals.
- **1961.** **Scott's theorem**: if a measurable cardinal exists then $V\neq L$. This is the first proof that a large-cardinal axiom refutes a "minimality" axiom, and it kills the hope that measurables are provable in ZFC-plus-$V=L$-style settings.
- **1967.** Levy–Solovay: measurability is preserved by forcing of size $<\kappa$, so it decides nothing about CH.
- **1969–71.** Solovay: a measurable implies every $\Sigma^1_2$ set of reals is Lebesgue measurable; and real-valued measurable on $2^{\aleph_0}$ is equiconsistent with measurable (random forcing over a measurable / inner-model direction).
- **1970–71.** Kunen: iterated ultrapowers; $L[U]$ is a canonical inner model with a *unique* normal measure, satisfies GCH and $\diamondsuit$; the existence of $0^{\\#}$ follows from a measurable (Silver, Solovay).
- **1974–.** Mitchell: inner models $L[\vec U]$ for sequences of measures, Mitchell order $U \lhd W$; the core model program (Dodd–Jensen 1981) makes measurability *measure* strength from below.
- **2003–.** Kanamori's *The Higher Infinite* (2nd ed.) is the standard reference. Woodin's Ultimate-$L$ program and Goldberg's Ultrapower Axiom are the current structural frontier.

## 4. Partial Results / Verified Cases

Concrete, fully settled facts:

- **Unprovability in ZFC.** If $\kappa$ is measurable then $\kappa$ is inaccessible, so $V_\kappa\models\mathrm{ZFC}$; hence ZFC $\nvdash$ Con(ZFC) $\Rightarrow$ ZFC $\nvdash \exists$ measurable (Gödel II). Same for $\mathrm{ZFC}+\exists$ measurable proving its own consistency.
- **Failure in $L$ and in $L[U]$-fragments.** No measurable in $L$; in $L[U]$ there is exactly one measurable and exactly one normal measure on it (Kunen 1970).
- **Position in the hierarchy.** Below the first measurable $\kappa$ there are $\kappa$ inaccessibles, $\kappa$ Mahlos, $\kappa$ weakly compacts, $\kappa$ Ramseys — each such set has $U$-measure one. Measurability is strictly stronger in consistency than all of these, and strictly weaker than strong, Woodin, supercompact.
- **Small-cardinal cases resolved negatively.** $\aleph_1$ (and every successor cardinal) is not measurable under AC: Ulam matrices give a partition of $\lambda^+$ into $\lambda^+$ sets, none in the ultrafilter. Under AD, $\aleph_1$ and $\aleph_2$ *are* measurable — so the negative result is AC-dependent.
- **Equiconsistencies (exact calibrations).** Real-valued measurable on $\mathfrak{c}$ $\equiv$ measurable (Solovay 1971). $\neg\mathrm{SCH}$ $\equiv$ $\exists\kappa\,(o(\kappa)=\kappa^{++})$ (Gitik 1989, with Mitchell's lower bound). $\aleph_\omega$ strong limit with $2^{\aleph_\omega}>\aleph_{\omega_1}$ needs measurables of high Mitchell order.
- **Choiceless refutation.** Kunen (1971): there is no elementary $j:V\to V$ in ZFC. So the *upper* end of the hierarchy is provably bounded, showing that "large cardinal axioms are refutable" is not idle.

## 5. Principal Obstacles

- **Gödelian barrier.** Consistency of $\mathrm{ZFC}+\exists$ measurable is strictly stronger than ZFC's; no finitary or ZFC-internal proof can exist. Every "proof" must be a relative-consistency reduction to something at least as strong, which merely relocates the problem.
- **No forcing construction.** Forcing raises models to satisfy CH, $\neg$CH, SCH failure, etc., but cannot create a measurable from nothing: by Levy–Solovay small forcing preserves and does not create them, and any forcing extension's measurable is witnessed by embeddings whose restrictions reflect into the ground model core model. So the standard independence technology only proves *non*-refutability *given* consistency.
- **Inner model theory only works downward.** The core model $K$ (Dodd–Jensen, Steel) proves lower bounds: if some combinatorial statement holds and there is no inner model with a measurable, then $K$ exists and covering holds, contradiction. This *extracts* measurables from hypotheses of comparable strength — it never manufactures them from ZFC.
- **Iterability.** Extending inner-model theory past Woodin cardinals requires solving the iterability problem for long extender models; the fine-structural machinery is the bottleneck for the analogous questions one level up, and it is what makes uniqueness/canonicity arguments (which underwrite "there is no hidden contradiction") hard to push.
- **Justification is not a theorem.** Arguments from reflection, generic absoluteness, or "maximality" are heuristic. Reflection principles that formally imply measurability tend to be at least as strong, so the justificatory circle does not close.

## 6. The Gap

Proven: measurability is not refutable by any argument formalizable in ZFC + Con(ZFC + measurable); its consistency strength is exactly calibrated relative to a long list of combinatorial statements; its canonical inner models are fully analyzed up to $L[\vec U]$.

Not proven, and the precise boundary: **no absolute consistency proof, and no refutation.** Crossing the gap in the positive direction would require a *new* form of evidence — e.g. Woodin's Ultimate-$L$ conjecture, which if proved would give a single canonical inner model absorbing all large cardinals and thereby a structural coherence argument, without ever supplying a consistency proof in the Hilbertian sense. Crossing it negatively requires deriving $0=1$ from a $\kappa$-complete ultrafilter — the only known template being Kunen's reflection-of-Erdős–Hajnal-style argument, which bites only at the $j:V\to V$ level.

## 7. Current Research (as of June 2026)

- **Ultimate-$L$ (Woodin, Berkeley; Steel, Sargsyan, Rutgers).** The HOD dichotomy and the Ultimate-$L$ conjecture: if $\delta$ is extendible, either large cardinals are "close to" HOD or not; a positive resolution would give an $L$-like model with a supercompact, subsuming all measurables. Still open. *(frontier — verify)*
- **Ultrapower Axiom (Goldberg).** UA — any two ultrapowers have a common comparison — yields GCH above a supercompact and a linear order on measures; it is expected to hold in Ultimate-$L$ and is the sharpest current structure theory for measures.
- **Descriptive inner model theory (Sargsyan, Steel, Trang).** Hod mice, derived models, and $\mathrm{AD}^+$: calibrating determinacy hypotheses against long extender sequences.
- **Choiceless large cardinals (Bagaria, Koellner, Woodin; Cutolo, Goldberg).** Reinhardt/Berkeley cardinals in ZF: exploring whether the Kunen refutation extends without AC, which probes how close the hierarchy is to inconsistency.
- **Singular cardinal combinatorics (Gitik, Neeman, Sinapova).** Prikry-type forcings and PCF, continuing to convert cardinal-arithmetic statements into exact Mitchell-order requirements.

## 8. Future Work

- Prove or refute the **Ultimate-$L$ conjecture**; this is the single stated milestone whose resolution would most change the epistemic status of measurables (Woodin).
- Extend **core model induction** past current iterability limits to get exact equiconsistencies for statements at the level of supercompactness.
- Settle whether **UA is consistent with a supercompact** and whether it follows from Ultimate-$L$.
- Search systematically for **inconsistency** at the top: sharpen Kunen-style arguments to see how far below $j:V\to V$ they can be pushed in ZF.
- Develop **non-consistency evidence**: track the record of large-cardinal hypotheses predicting later-verified $\Sigma^1_n$ facts (Solovay-style regularity results) as inductive support.

## 9. Key References

- **[Foundational]** S. Ulam. *Zur Masstheorie in der allgemeinen Mengenlehre.* Fundamenta Mathematicae 16 (1930), 140–150.
- **[Foundational]** D. Scott. *Measurable cardinals and constructible sets.* Bulletin de l'Académie Polonaise des Sciences 9 (1961), 521–524.
- **[Foundational]** H. J. Keisler, A. Tarski. *From accessible to inaccessible cardinals.* Fundamenta Mathematicae 53 (1964), 225–308.
- **[Foundational]** A. Levy, R. Solovay. *Measurable cardinals and the continuum hypothesis.* Israel Journal of Mathematics 5 (1967), 234–248.
- **[Foundational]** K. Kunen. *Some applications of iterated ultrapowers in set theory.* Annals of Mathematical Logic 1 (1970), 179–227.
- **[Foundational]** K. Kunen. *Elementary embeddings and infinitary combinatorics.* Journal of Symbolic Logic 36 (1971), 407–413.
- **[Foundational]** R. Solovay. *Real-valued measurable cardinals.* In: Axiomatic Set Theory, Proc. Sympos. Pure Math. XIII, Part 1, AMS (1971), 397–428.
- **[SOTA]** W. Mitchell. *Sets constructible from sequences of ultrafilters.* Journal of Symbolic Logic 39 (1974), 57–66.
- **[SOTA]** A. Dodd, R. Jensen. *The core model.* Annals of Mathematical Logic 20 (1981), 43–75.
- **[SOTA]** M. Gitik. *The negation of the singular cardinal hypothesis from $o(\kappa)=\kappa^{++}$.* Annals of Pure and Applied Logic 43 (1989), 209–234.
- **[SOTA]** J. Steel. *The Core Model Iterability Problem.* Lecture Notes in Logic 8, Springer, 1996.
- **[SOTA / Recent]** G. Goldberg. *The Ultrapower Axiom.* De Gruyter, Series in Logic and Its Applications, 2022.
- **[SOTA / Recent]** J. Bagaria, P. Koellner, W. H. Woodin. *Large cardinals beyond choice.* Bulletin of Symbolic Logic 25 (2019), 283–318.
- **[Survey]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Survey]** T. Jech. *Set Theory.* 3rd millennium edition, Springer, 2003.
- **[Survey]** P. Maddy. *Believing the axioms, I & II.* Journal of Symbolic Logic 53 (1988), 481–511 and 736–764.
- **[Survey]** W. H. Woodin. *The Continuum Hypothesis, Part I / Part II.* Notices of the AMS 48 (2001), 567–576 and 681–690.

## 10. Worked Example / Concrete Special Case

**Claim.** If $U$ is a normal measure on $\kappa$, then $I=\{\alpha<\kappa:\alpha \text{ is inaccessible}\}\in U$. In particular $\kappa$ is the $\kappa$-th inaccessible.

Let $j=j_U:V\to M=\mathrm{Ult}(V,U)$, $\mathrm{crit}(j)=\kappa$, and recall $A\in U \iff \kappa\in j(A)$ and $[\mathrm{id}]_U=\kappa$.

*Step 1 — $\kappa$ is regular in $M$.* $M$ is closed under $\kappa$-sequences, and $j$ is elementary, so $M$ computes cofinalities correctly at $\kappa$. If $f:\lambda\to\kappa$ were cofinal with $\lambda<\kappa$, then $j(f)=j\restriction$-image is a cofinal map $\lambda\to j(\kappa)$ with range $\subseteq\kappa$, contradicting $j(\kappa)>\kappa$. So $M\models$ "$\kappa$ regular".

*Step 2 — $\kappa$ is a strong limit in $M$.* Fix $\lambda<\kappa$. Since $V_{\kappa+1}\subseteq M$ and $j(\lambda)=\lambda$, $M$ and $V$ agree on $\mathcal{P}(\lambda)$, so $(2^\lambda)^M=2^\lambda<\kappa$ because $\kappa$ is inaccessible in $V$ (Ulam's theorem, provable directly from $\kappa$-completeness).

*Step 3 — reflect.* Steps 1–2 give $M\models$ "$\kappa$ is inaccessible". Now $j(I)=\{\alpha<j(\kappa) : M\models \alpha\text{ inaccessible}\}$ by elementarity, and we just showed $\kappa\in j(I)$. By the defining property of $U$,
$$\kappa\in j(I)\ \Longrightarrow\ I\in U.$$

*Step 4 — count.* $U$ is $\kappa$-complete and non-principal, so every set in $U$ has size $\kappa$ and is unbounded in $\kappa$. Hence $\kappa$ carries $\kappa$ inaccessibles below it. Iterating the same argument with "inaccessible" replaced by "Mahlo", then "weakly compact", then "Ramsey" — each property is $\Delta_2$ and absolute between $V$ and $M$ by $V_{\kappa+1}\subseteq M$ — yields Hanf's result that the first measurable dwarfs the first weakly compact.

**Contrast (why this cannot bootstrap).** Every step above *presupposes* $U$. Nothing in ZFC produces the initial $\kappa$-complete ultrafilter: for any $\kappa$ definable in ZFC, $L$ is a model where $\kappa$ carries no such $U$ (Scott). That is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*