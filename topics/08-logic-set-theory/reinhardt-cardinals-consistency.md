---
id: 08-logic-set-theory/reinhardt-cardinals-consistency
title: "Reinhardt Cardinals Consistency"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Reinhardt Cardinals Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/reinhardt-cardinals-consistency` · **Status:** open

## 1. Problem Statement / Conjecture

A **Reinhardt cardinal** is the critical point of a nontrivial elementary embedding $j : V \to V$ of the set-theoretic universe into itself. Kunen (1971) proved that no such $j$ exists in $\mathsf{ZFC}$. The open problem is whether the notion survives once the Axiom of Choice is dropped:

> **Question (Reinhardt consistency).** Is $\mathsf{ZF}_j + $ "$j : V \to V$ is a nontrivial elementary embedding" consistent, assuming $\mathsf{ZFC}$ (or $\mathsf{ZFC}$ plus conventional large cardinals) is?

Here $\mathsf{ZF}_j$ is $\mathsf{ZF}$ in the two-symbol language $\{\in, j\}$ with Separation and Replacement schemes for **all** formulas, including those mentioning $j$. This formulation matters: with only $\in$-Separation the statement is provably weaker and easier to satisfy.

A resolution means one of:

1. **Inconsistency:** a $\mathsf{ZF}_j$-proof of $\bot$ from nontrivial elementarity — a choiceless Kunen theorem.
2. **Relative consistency:** an interpretation of $\mathsf{ZF}_j + \exists$ Reinhardt inside a model of $\mathsf{ZFC} + \Phi$ for some large-cardinal axiom $\Phi$ believed consistent.

No absolute consistency proof is possible (Gödel), so (2) means a relative interpretation. The problem is open in both directions, and its resolution is the standard test of whether the large-cardinal hierarchy has a ceiling.

## 2. Mathematical Foundations

**Elementary embedding.** For transitive classes $M, N$, a map $j : M \to N$ is elementary if for every formula $\varphi$ and $a_1,\dots,a_n \in M$,
$$M \models \varphi(a_1,\dots,a_n) \iff N \models \varphi(j(a_1),\dots,j(a_n)).$$
For $M = N = V$ this is a scheme, one instance per $\varphi$; $j$ is a class, so the ambient theory must be $\mathsf{ZF}_j$ or $\mathsf{NBG}$/$\mathsf{GB}$ with $j$ as a predicate.

**Critical point.** $j$ is *nontrivial* if $j \neq \mathrm{id}$. Then $j$ moves an ordinal, and
$$\mathrm{crit}(j) = \kappa_0 = \min\{\alpha \in \mathrm{Ord} : j(\alpha) \neq \alpha\},$$
with $j(\kappa_0) > \kappa_0$. Note $\kappa_0 \notin \mathrm{ran}(j)$: if $j(\alpha)=\kappa_0$ then $\alpha < \kappa_0$ forces $j(\alpha)=\alpha=\kappa_0$, and $\alpha \geq \kappa_0$ forces $j(\alpha) \geq j(\kappa_0) > \kappa_0$.

**Critical sequence.** Set $\kappa_{n+1} = j(\kappa_n)$ and
$$\lambda = \sup_{n<\omega} \kappa_n .$$
Then $j(\lambda)=\lambda$, $\mathrm{cf}(\lambda) = \omega$, and $j \restriction V_\lambda : V_\lambda \to V_\lambda$ is elementary — an $I_3$-style rank-into-rank embedding sitting under any Reinhardt $j$.

**Kunen's theorem (ZFC).** There is no nontrivial elementary $j : V \to V$; equivalently there is no nontrivial elementary $j : V_{\lambda+2} \to V_{\lambda+2}$. The proof needs one choice-dependent ingredient, the Erdős–Hajnal theorem: for every infinite $\lambda$ there is an $\omega$-Jónsson function
$$f : [\lambda]^{\omega} \to \lambda, \qquad \forall A \subseteq \lambda \ \big(|A| = \lambda \Rightarrow f\,''[A]^{\omega} = \lambda\big).$$

**Choiceless hierarchy above Reinhardt** (Bagaria–Koellner–Woodin):

- $\kappa$ is **super Reinhardt** if for every ordinal $\alpha$ there is elementary $j : V \to V$ with $\mathrm{crit}(j) = \kappa$ and $j(\kappa) > \alpha$.
- $\delta$ is **Berkeley** if for every transitive $M$ with $\delta \in M$ and every $\eta < \delta$ there is elementary $j : M \to M$ with $\eta < \mathrm{crit}(j) < \delta$.
- $\delta$ is **club Berkeley** if in addition the set of such critical points is club in $\delta$.

Berkeley $\Rightarrow$ proper class of super Reinhardts below, so $\mathrm{Con}(\mathsf{ZF}+\text{Berkeley}) \Rightarrow \mathrm{Con}(\mathsf{ZF}+\text{Reinhardt})$.

## 3. History & State of the Art (SOTA)

- **1967–1974.** William Reinhardt, in his Berkeley dissertation and in *Remarks on reflection principles, large cardinals, and elementary embeddings* (AMS Proc. Sympos. Pure Math. XIII/2, 1974), proposes $j : V \to V$ as the natural terminus of the embedding hierarchy.
- **1971.** Kenneth Kunen, *Elementary embeddings and infinitary combinatorics* (JSL 36), refutes it in $\mathsf{ZFC}$. The community reads the theorem as bounding the hierarchy; attention moves to $I_0$–$I_3$ at $V_{\lambda+1}$, the strongest axioms not known to be inconsistent.
- **1996.** Zapletal gives a short alternative proof (Proc. AMS 124) via stationary-set splitting; Woodin and Harada give others. **Every known proof uses AC**, and Woodin isolated that they all route through some form of the Erdős–Hajnal / Solovay splitting machinery.
- **1999.** Suzuki (JSL 64) proves in $\mathsf{ZF}$ that no nontrivial $j : V \to V$ is definable from parameters. So a Reinhardt embedding must be a genuinely new class.
- **2012.** Hamkins–Kirmayer–Perlmutter (APAL 163) extend Kunen to embeddings between inner models: in $\mathsf{ZFC}$ there is no nontrivial elementary $j : V \to M$ with $V_{\lambda+2} \subseteq M$, none $j : \mathrm{HOD} \to \mathrm{HOD}$ definable in $V$, and none $j:V\to V$ even in $\mathsf{ZFC}$ minus Replacement-for-$j$ variants they identify.
- **2019.** Bagaria, Koellner and Woodin, *Large cardinals beyond choice* (BSL 25), build the modern choiceless hierarchy: Reinhardt $<$ super Reinhardt $<$ totally Reinhardt $<$ Berkeley, with structure theory and several refutations of choice fragments.
- **2020–2024.** Schlutzenberg obtains the first genuine positive-direction result: from a strong $I_0$-type hypothesis in $\mathsf{ZFC}$, a choiceless model of $\mathsf{ZF}$ with an elementary $j : V_{\lambda+2} \to V_{\lambda+2}$ — the exact statement Kunen refuted under AC. Goldberg, *Even ordinals and the Kunen inconsistency*, pushes the choiceless refutation program using cardinal-arithmetic-free combinatorics.

Status: no inconsistency, no consistency proof, and no known reduction of Reinhardt to any $\mathsf{ZFC}$ large cardinal.

## 4. Partial Results / Verified Cases

**Refuted cases (all under AC or a choice fragment).**

- $\mathsf{ZFC} \vdash \neg \exists\, j : V \to V$ nontrivial (Kunen 1971).
- $\mathsf{ZFC} \vdash \neg \exists\, j : V_{\lambda+2} \to V_{\lambda+2}$ nontrivial, for every $\lambda$. The rank $\lambda+2$ is sharp: $I_1$ ($j : V_{\lambda+1}\to V_{\lambda+1}$) is open.
- $\mathsf{ZFC} \vdash \neg\exists\, j : V \to M$ with $M$ transitive and $V_{j(\mathrm{crit}(j))} \subseteq M$ (Hamkins–Kirmayer–Perlmutter 2012).
- $\mathsf{ZF} \vdash$ no nontrivial $j : V \to V$ definable from parameters (Suzuki 1999). Corollary: under $\mathsf{ZF}+$Reinhardt, $V \neq \mathrm{HOD}_A$ for every set $A$; in particular $V \neq L[A]$ and $V\neq\mathrm{HOD}$.
- **Club Berkeley $\Rightarrow \neg \mathsf{DC}_\delta$** (Bagaria–Koellner–Woodin 2019): choiceless cardinals kill dependent choice at their own level.
- Usuba: the choiceless Löwenheim–Skolem property is incompatible with a Reinhardt cardinal (*Choiceless Löwenheim–Skolem property and uniform definability of grounds*, Springer Proc. Math. Stat., 2021).

**Positive/consistency-direction cases.**

- Schlutzenberg: from $\mathsf{ZFC} + $ an $I_0$-strength hypothesis at $\lambda$, one builds a symmetric/choiceless model of $\mathsf{ZF} + \exists \lambda\, \exists j : V_{\lambda+2} \to V_{\lambda+2}$. This is the strongest known evidence that Kunen's argument is *about choice*, not about embeddings.
- Below $\lambda+2$, in $\mathsf{ZFC}$, $I_3$ / $I_2$ / $I_1$ have rich structure theory (Kanamori, *The Higher Infinite*, §24; Woodin on $L(V_{\lambda+1})$), showing the $V_\lambda$-fragment of a Reinhardt $j$ is not itself pathological.
- Under $\mathsf{ZF}+$Reinhardt with critical sequence sup $\lambda$: $\mathrm{cf}(\lambda)=\omega$, $\lambda$ is a limit of measurable cardinals in the relevant sense, and $V_\lambda \prec_{\Sigma} V$ fragments hold — the model is not obviously degenerate.

## 5. Principal Obstacles

- **All known Kunen proofs consume AC at one point and no substitute is known.** Erdős–Hajnal $\omega$-Jónsson functions, Solovay's splitting of stationary subsets of $\{\alpha<\lambda^+ : \mathrm{cf}(\alpha)=\omega\}$, and Woodin's $\omega$-club filter argument all require well-ordering a set of size $\ge 2^\lambda$. In $\mathsf{ZF}$ these objects may simply not exist: $[\lambda]^\omega$ need not be well-orderable, and $\lambda^+$ can be singular.
- **Non-definability blocks internal construction.** Suzuki's theorem means a Reinhardt $j$ can never be produced by an ultrapower, extender, or any $\mathrm{HOD}$-style definable construction — the standard toolkit for building embeddings. Any consistency proof must produce $j$ as a *new* class, e.g. via symmetric extension of a class forcing, and then verify the full $\mathsf{ZF}_j$ replacement scheme for $j$-formulas.
- **Forcing does not reach class embeddings.** Symmetric extensions kill choice locally, but $j$ is a proper class; preserving elementarity of a class map through a class-length symmetric construction while keeping $j$-Replacement is exactly where Schlutzenberg's method stops at $V_{\lambda+2}$.
- **No inner model theory above choice.** The comparison/iterability machinery that certifies consistency for Woodin cardinals and beyond is built on well-orderings and fine structure; there is no candidate canonical inner model for a Reinhardt cardinal, so the usual "consistency by construction" route is unavailable.
- **Reflection is unavailable at the top.** Because $j(\lambda)=\lambda$ and $j$ fixes $\mathrm{Ord}$ cofinally, one cannot reflect the hypothesis down to a set-sized structure and argue by induction on rank.

## 6. The Gap

Proven: $\neg \exists j:V_{\lambda+2}\to V_{\lambda+2}$ **with AC**; consistent: $\exists j:V_{\lambda+2}\to V_{\lambda+2}$ **without AC** (relative to $I_0$-strength). Asked: $\exists j : V \to V$ without AC, with full $j$-Replacement.

The gap has two edges:

1. **From $V_{\lambda+2}$ to $V$.** Schlutzenberg's models realize the embedding only on a set-sized rank initial segment. Extending to a class embedding requires a construction of unbounded length whose limit stages preserve elementarity — the amalgamation of $\omega$-many (or $\mathrm{Ord}$-many) local embeddings into one global $j$ has no known technique.
2. **From "AC-free" to "AC-free with $\mathsf{DC}$-like structure."** Whether $\mathsf{ZF}+\mathsf{DC}+$Reinhardt is consistent is separately open. Bagaria–Koellner–Woodin show choice fragments fail at Berkeley level; nobody knows how much choice a Reinhardt cardinal tolerates. If $\mathsf{ZF}+\mathsf{DC}_\lambda$ suffices to run a Kunen-style argument, the whole notion collapses.

Crossing the gap in the negative direction means: find a $\mathsf{ZF}$-provable combinatorial object at $\lambda^+$ (or $[\lambda]^\omega$) that a $j$ fixing $\lambda$ cannot fix. Every candidate so far has been shown to require choice for its existence.

## 7. Current Research (as of June 2026)

- **Berkeley/UC Irvine/Münster axis.** Goldberg (Berkeley) and Schlutzenberg (Münster) drive the technical program: Schlutzenberg on choiceless rank-into-rank models and on how much $\mathsf{ZF}_j$-Replacement survives; Goldberg on refuting Reinhardt from weak choice-like principles — his *Even ordinals and the Kunen inconsistency* isolates parity/club combinatorics that make a Kunen argument go through under hypotheses strictly weaker than AC.
- **Woodin's programme.** The $\mathrm{HOD}$ dichotomy and *Suitable extender models* framework predicts that if $\mathsf{ZF}+$Reinhardt is consistent, $V$ must be very far from $\mathrm{HOD}$, and Woodin has argued the Ultimate-$L$ conjecture would refute choiceless cardinals outright. *(frontier — verify)*
- **Structure theory of $L(V_{\delta+1})$ under Berkeley cardinals** (Cutolo, Naples/Amsterdam) — determinacy-flavoured consequences that make the choiceless hierarchy look regular rather than incoherent.
- **Reverse-mathematical calibration.** Ongoing work asks exactly which choice fragment ($\mathsf{DC}_\lambda$, $\mathsf{AC}_{V_\lambda}$, "$\lambda^+$ regular", "$[\lambda]^\omega$ well-orderable") suffices for Kunen. Each such theorem shrinks the space where Reinhardt could live.
- No claimed proof of $\mathrm{Con}(\mathsf{ZF}+\text{Reinhardt})$ or of $\neg$Reinhardt in $\mathsf{ZF}$ has survived refereeing.

## 8. Future Work

- **Amalgamate local embeddings.** Iterate Schlutzenberg's symmetric construction through $\mathrm{Ord}$; identify the exact obstruction to a direct-limit $j : V \to V$.
- **Determine the choice threshold.** Prove or refute $\mathrm{Con}(\mathsf{ZF}+\mathsf{DC}+\text{Reinhardt})$. Koellner has pointed to this as the single most informative next data point.
- **Choiceless combinatorics at $\lambda^+$.** Decide whether $\mathsf{ZF}$ alone proves enough about $\lambda^+$-stationary sets to run Woodin's version of Kunen.
- **Inner-model candidates.** Look for a canonical $\mathsf{ZF}$ model of a Reinhardt cardinal built from $L(V_{\lambda+1})$-style hierarchies, following Cutolo and Woodin.
- **Formal verification.** Machine-check Kunen's proof in a proof assistant with AC tracked as an explicit hypothesis, to certify that no hidden choice-free route exists.

## 9. Key References

- **[Foundational]** W. N. Reinhardt. *Remarks on reflection principles, large cardinals, and elementary embeddings.* In *Axiomatic Set Theory*, Proc. Sympos. Pure Math. XIII, Part II, American Mathematical Society, 1974, pp. 189–205.
- **[Foundational]** K. Kunen. *Elementary embeddings and infinitary combinatorics.* Journal of Symbolic Logic 36 (1971), 407–413.
- **[Foundational]** P. Erdős and A. Hajnal. *On a problem of B. Jónsson.* Bulletin de l'Académie Polonaise des Sciences 14 (1966), 19–23.
- **[Foundational]** A. Suzuki. *No elementary embedding from $V$ into $V$ is definable from parameters.* Journal of Symbolic Logic 64 (1999), 1591–1594.
- **[Alternative proof]** J. Zapletal. *A new proof of Kunen's inconsistency.* Proceedings of the American Mathematical Society 124 (1996), 2203–2204.
- **[SOTA]** J. Bagaria, P. Koellner, W. H. Woodin. *Large cardinals beyond choice.* Bulletin of Symbolic Logic 25 (2019), 283–318.
- **[SOTA / Recent]** F. Schlutzenberg. *On the consistency of ZF with an elementary embedding from $V_{\lambda+2}$ into $V_{\lambda+2}$.* Preprint / Journal of Mathematical Logic, 2020–2024.
- **[SOTA / Recent]** G. Goldberg. *Even ordinals and the Kunen inconsistency.* Journal of Mathematical Logic, 2024.
- **[Recent]** J. D. Hamkins, G. Kirmayer, N. L. Perlmutter. *Generalizations of the Kunen inconsistency.* Annals of Pure and Applied Logic 163 (2012), 1872–1890.
- **[Recent]** T. Usuba. *Choiceless Löwenheim–Skolem property and uniform definability of grounds.* In *Advances in Mathematical Logic*, Springer Proceedings in Mathematics & Statistics, 2021.
- **[Recent]** R. Cutolo. *Berkeley cardinals and the structure of $L(V_{\delta+1})$.* Journal of Symbolic Logic 83 (2018), 1457–1476.
- **[Survey / Text]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd edition, Springer, 2003 (§23–24).
- **[Survey / Text]** T. Jech. *Set Theory: The Third Millennium Edition.* Springer, 2003.
- **[Programme]** W. H. Woodin. *Suitable extender models I.* Journal of Mathematical Logic 10 (2010), 101–339.

## 10. Worked Example / Concrete Special Case

**Kunen's proof, with the choice step isolated.** Suppose $j : V \to V$ is elementary and nontrivial. Let $\kappa_0=\mathrm{crit}(j)$, $\kappa_{n+1}=j(\kappa_n)$, $\lambda=\sup_n \kappa_n$.

*Step 1 — $j$ fixes $\lambda$.* $j(\lambda) = j(\sup_n \kappa_n) = \sup_n j(\kappa_n) = \sup_n \kappa_{n+1} = \lambda$.

*Step 2 (uses AC) — pick an $\omega$-Jónsson function.* By Erdős–Hajnal there is
$$f : [\lambda]^{\omega} \to \lambda \quad \text{with} \quad f\,''[A]^{\omega} = \lambda \ \text{ for every } A\subseteq\lambda,\ |A|=\lambda .$$
Constructing $f$ needs a well-ordering of $[\lambda]^\omega$ — **this is the only step that uses choice.**

*Step 3 — transfer by elementarity.* $j(f)$ is, in $V$, an $\omega$-Jónsson function for $j(\lambda)=\lambda$, so $j(f) : [\lambda]^\omega \to \lambda$ is onto every $[A]^\omega$ with $|A|=\lambda$.

*Step 4 — apply it to the range of $j$.* Put $A = j\,''\lambda$. Then $|A| = \lambda$, so there is $s \in [j\,''\lambda]^{\omega}$ with
$$j(f)(s) = \kappa_0 .$$

*Step 5 — pull back.* Since $s$ is a countable subset of $j\,''\lambda$, we have $s = j\,''t$ for $t = \{\alpha : j(\alpha)\in s\} \in [\lambda]^{\omega}$. For countable $t$, elementarity gives $j(f)(j\,''t) = j\big(f(t)\big)$. Hence
$$\kappa_0 = j(f)(s) = j\big(f(t)\big) \in \mathrm{ran}(j).$$

*Step 6 — contradiction.* $\kappa_0 \notin \mathrm{ran}(j)$, as shown in Section 2. Contradiction. $\square$

**What this shows about the open problem.** Delete Step 2 and the argument evaporates: in $\mathsf{ZF}$, $[\lambda]^\omega$ need not be well-orderable and no $\omega$-Jónsson function for $\lambda$ need exist. Every other step is choice-free. Concretely: take $\lambda$ with $\mathrm{cf}(\lambda)=\omega$ in a symmetric model where $\lambda^+$ is singular and $[\lambda]^\omega$ carries no well-ordering — then Steps 1, 3, 4, 5 remain valid statements about any embedding present, and Step 2's hypothesis is simply false. Schlutzenberg's models realize exactly this configuration at $V_{\lambda+2}$: a nontrivial elementary $j : V_{\lambda+2}\to V_{\lambda+2}$ coexisting with the failure of the Jónsson machinery. The remaining question is whether the same configuration can be pushed all the way to $V$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*