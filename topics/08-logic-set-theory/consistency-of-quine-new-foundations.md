---
id: 08-logic-set-theory/consistency-of-quine-new-foundations
title: "Consistency of Quine New Foundations"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Consistency of Quine's New Foundations (NF)

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/consistency-of-quine-new-foundations` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

New Foundations (NF) is the first-order set theory in the language $\{=,\in\}$ axiomatized by extensionality plus **stratified comprehension**. Quine introduced it in 1937. The problem, open for 86 years:

> Is NF consistent? Equivalently, is there no derivation of $\bot$ from the NF axioms?

A complete solution requires either (i) a relative consistency proof $\mathrm{Con}(T)\to\mathrm{Con}(\mathrm{NF})$ for a metatheory $T$ believed consistent, or (ii) an explicit contradiction.

**Resolution.** M. Randall Holmes announced a proof in 2010, revised it repeatedly through 2023, and it was machine-checked in Lean 4 by Sky Wilshaw in April 2024 (the `con-nf` project). NF is consistent relative to standard mathematics. Residual open problems remain and are catalogued in §6–§7: the exact consistency strength of NF, the structure of its models, and the status of choice-like and counting-like extensions.

## 2. Mathematical Foundations

**Stratification.** A formula $\varphi$ of $\{=,\in\}$ is *stratified* if there is a function $\sigma$ from its variables to $\mathbb{N}$ such that

$$\sigma(y)=\sigma(x)+1 \text{ for every subformula } x\in y, \qquad \sigma(x)=\sigma(y) \text{ for every subformula } x=y .$$

**NF axioms.**
$$\forall x\,\forall y\,\big(\forall z (z\in x \leftrightarrow z\in y)\to x=y\big) \qquad \text{(Extensionality)}$$
$$\exists A\,\forall x\,(x\in A \leftrightarrow \varphi(x)) \qquad \text{for every stratified } \varphi \text{ with } A \text{ not free.}$$

Quantifiers in $\varphi$ are unrestricted, so comprehension is impredicative. Russell's $x\notin x$ is unstratified, so the paradox is blocked; but $x=x$ is stratified, giving a universal set $V$ with $V\in V$.

**TST (simple type theory).** Variables carry types $n\in\mathbb{N}$; $x^n\in y^m$ is well-formed only when $m=n+1$; extensionality and full comprehension hold at each type. NF is exactly TST with all type distinctions erased.

**Ambiguity.** For a sentence $\varphi$ of TST let $\varphi^{+}$ raise every type index by $1$. The **Ambiguity scheme** is $\{\varphi\leftrightarrow\varphi^{+}\}$.

> **Specker's Theorem (1962).** $\mathrm{Con}(\mathrm{NF})\iff\mathrm{Con}(\mathrm{TST}+\mathrm{Ambiguity})$.

Equivalently, NF is consistent iff TST has a model with a type-shifting endomorphism, iff (by compactness + Ramsey) every finite fragment of Ambiguity is satisfiable.

**TTT (tangled type theory), Holmes 1995.** Types are indexed by a limit ordinal $\lambda$ (or any dense linear order). For $i<j$ the relation ${\in}$ holds between type-$i$ and type-$j$ objects; each type-$j$ set has, *for each* $i<j$, its own extension in type $i$. Axioms: for every increasing sequence, the corresponding TST axiom holds under the induced type assignment.

> **Theorem (Holmes 1995).** $\mathrm{Con}(\mathrm{TTT})\iff\mathrm{Con}(\mathrm{NF})$.

The proof of $\Rightarrow$ uses Ramsey's theorem to extract a homogeneous set of type-indices from a TTT model, yielding a model of TST satisfying arbitrary finite fragments of Ambiguity.

**Known NF theorems.** $V$ exists; $\{x\}\in V$; Cantor holds in the corrected form $|\mathcal{P}_1(x)|<|\mathcal{P}(x)|$ where $\mathcal{P}_1(x)=\{\{y\}:y\in x\}$, so $|\mathcal{P}_1(V)|<|V|$ with no contradiction — the map $x\mapsto\{x\}$ is not a set. **Specker (1953):** NF refutes the axiom of choice, hence proves Infinity.

## 3. History & State of the Art

- **1937.** Quine, *New foundations for mathematical logic*, Amer. Math. Monthly 44, 70–80. Motivated by economy: one sort, one comprehension scheme.
- **1944.** Hailperin: stratified comprehension is finitely axiomatizable (about ten set-existence axioms).
- **1953.** Specker: NF $\vdash\neg\mathrm{AC}$. This killed the hope of an easy ZFC-style model and made NF suspect.
- **1962.** Specker: NF $\equiv_{\mathrm{Con}}$ TST + Ambiguity. Every subsequent attack goes through this reduction.
- **1969.** Jensen: **NFU** (extensionality weakened to allow urelements) is consistent; NFU + Infinity + Choice is equiconsistent with TST + Infinity (Mac Lane set theory strength). Models via Ehrenfeucht–Mostowski/automorphism arguments on a nonstandard model of ZFC.
- **1969–1982.** Fragments: Grishin — NF$_3$ (three-type stratification) is consistent and decidable; Crabbé — NFI (predicative-ish impredicativity restriction) is consistent.
- **1988.** Boffa: reformulation via ZFJ and $\kappa$-automorphisms; sharpened the "what must a model look like" picture.
- **1995.** Holmes: TTT, and $\mathrm{Con}(\mathrm{TTT})\Leftrightarrow\mathrm{Con}(\mathrm{NF})$ — the framework in which the eventual proof was carried out.
- **2010–2023.** Holmes posts successive proofs of $\mathrm{Con}(\mathrm{TTT})$ via a Fraenkel–Mostowski-style "tangled webs of cardinals" construction. Several drafts contained repairable errors; the community did not certify them by hand.
- **2024-04.** Wilshaw completes the Lean 4 formalization (`leanprover-community/con-nf`) of the Holmes construction. This is now the accepted proof.

## 4. Partial Results / Verified Cases

| System | Status | Reference |
|---|---|---|
| NF$_3$ (stratification with 3 types) | Consistent, decidable | Grishin 1969 |
| NFI, NFP (restricted impredicativity) | Consistent, strength $\le$ that of $\mathrm{TST}+\mathrm{Inf}$ | Crabbé 1982 |
| NFU | Consistent; NFU + Inf + AC equiconsistent with TST + Inf (Mac Lane) | Jensen 1969 |
| NFU + "$V$ is strongly Cantorian"-type axioms | Consistent, strength up to $n$-Mahlo and beyond | Holmes 1998 |
| TST + finite fragments of Ambiguity | Satisfiable (all finite fragments) | Specker 1962 + Ramsey |
| NF + Counting | Consistent, and proves $\mathrm{Con}(\mathrm{NF})$ | Orey 1964 |
| Full NF | **Consistent** (relative to ZFC; machine-checked) | Holmes–Wilshaw 2024 |

The construction produces models of NF with $|V|$ of any suitable size arising from a "tangled web" over a model of ZFA/ZFC; models of NF built this way validate Infinity and refute AC, as Specker's theorem forces.

## 5. Principal Obstacles (why it stayed open 86 years)

- **No cumulative hierarchy.** $V\in V$ makes rank-induction, $\in$-recursion and Mostowski collapse unavailable. Every ZFC model-construction reflex fails at once.
- **Choice fails.** Specker's refutation of AC blocks interpretation into any ZFC-definable inner model and blocks Skolem-hull and EM-model techniques that gave NFU immediately.
- **Extensionality is the whole difficulty.** Jensen's NFU proof builds an automorphism $\sigma$ of a nonstandard $V_\alpha$ and takes $\{x : x\in\sigma(y)\}$; the collapse identifies distinct sets with equal extensions, which urelements absorb. Full extensionality forbids this, and there is no known repair by quotienting.
- **Ambiguity is not finitely reachable.** Each finite fragment of Ambiguity is satisfiable, but compactness needs a *single* model satisfying all of it; the homogeneous-set extraction requires Ramsey-type combinatorics on type-indices that only TTT supplies.
- **Combinatorial size.** The Holmes construction is a Fraenkel–Mostowski permutation model with an intricate bookkeeping of "clouds", litters, allowable permutations and a transfinite recursion on $\lambda$. Its verification burden — hundreds of interlocking definitions — is precisely why hand-refereeing stalled and formalization succeeded.

## 6. The Gap

Before 2024 the gap was: TST + *finite* Ambiguity (proved) vs. TST + *full* Ambiguity (needed). That gap is now closed by exhibiting a model of TTT.

What remains open:

1. **Exact consistency strength of NF.** The formalized proof runs in ZFC-strength Lean; Holmes argues the construction descends to a much weaker base, conjecturally around TST + Infinity / Mac Lane set theory. Pinning $\mathrm{Con}(\mathrm{NF})$'s exact position is open. *(frontier — verify)*
2. **NF + Counting** (Rosser's axiom $|\{1,\dots,n\}|=n$) proves $\mathrm{Con}(\mathrm{NF})$ (Orey), so its consistency is *not* settled by the 2024 result.
3. Structure theory: which cardinal arithmetic, which $\mathcal{P}_1$-behaviour, which "Cantorian" sets are realized in the Holmes models.

## 7. Current Research (as of June 2026)

- **Boise State (Holmes) and Cambridge (Wilshaw).** Consolidating the Lean development, extracting a human-readable proof of the same construction, and pushing the metatheory down. *(frontier — verify)*
- **Strength program.** Determining whether $\mathrm{Con}(\mathrm{TTT})$ is provable in Mac Lane set theory or Zermelo set theory; the answer would place NF firmly below ZFC. *(frontier — verify)*
- **Cambridge school (Forster and students).** Cardinal arithmetic in NF, the $T$-operation $T|x|=|\mathcal{P}_1(x)|$, and the status of $|V|$-type identities in the new models.
- **Formalization methodology.** `con-nf` is cited as a case study in mathematics where machine-checking settled priority for a contested informal proof, alongside the Kepler and Feit–Thompson formalizations.
- **NFU-side refinements.** Continued work on strong axioms of infinity in NFU-style theories, now with the goal of transferring them across to genuine NF.

## 8. Future Work

- Produce a 30-page human proof of $\mathrm{Con}(\mathrm{TTT})$ by isolating the essential combinatorics from the formalization's bookkeeping.
- Settle $\mathrm{Con}(\mathrm{NF}+\mathrm{Counting})$, and more generally NF plus Rosser-style axioms that raise strength.
- Develop forcing or permutation-model techniques *internal* to NF, to obtain independence results (e.g. of Counting) rather than only outer relative consistency.
- Determine whether NF interprets, or is interpreted in, natural fragments of ZFC — a two-sided calibration.
- Reassess NF as a foundation for mathematical practice now that consistency is not the obstruction.

## 9. Key References

- **[Foundational]** W. V. Quine. *New Foundations for Mathematical Logic.* American Mathematical Monthly 44 (1937), 70–80.
- **[Foundational]** E. Specker. *The Axiom of Choice in Quine's New Foundations for Mathematical Logic.* Proceedings of the National Academy of Sciences USA 39 (1953), 972–975.
- **[Foundational]** E. Specker. *Typical Ambiguity.* In: Logic, Methodology and Philosophy of Science (Proc. 1960 Int. Congress), Stanford University Press, 1962, 116–124.
- **[Foundational]** T. Hailperin. *A Set of Axioms for Logic.* Journal of Symbolic Logic 9 (1944), 1–19.
- **[Foundational]** R. B. Jensen. *On the Consistency of a Slight (?) Modification of Quine's New Foundations.* Synthese 19 (1969), 250–263.
- **[Foundational]** M. R. Holmes. *The Equivalence of NF-style Set Theories with "Tangled" Theories; the Construction of $\omega$-models of Predicative NF (and more).* Journal of Symbolic Logic 60 (1995), 178–190.
- **[SOTA / Recent]** M. R. Holmes and S. Wilshaw. *NF is Consistent.* Preprint / Lean 4 formalization, 2024. Formal development: `leanprover-community/con-nf`.
- **[Survey]** T. E. Forster. *Set Theory with a Universal Set: Exploring an Untyped Universe.* Oxford Logic Guides 31, 2nd ed., Oxford University Press, 1995.
- **[Survey]** M. R. Holmes. *Elementary Set Theory with a Universal Set.* Cahiers du Centre de Logique 10, Academia-Bruylant, 1998.
- **[Related]** S. Orey. *New Foundations and the Axiom of Counting.* Duke Mathematical Journal 31 (1964), 655–660.
- **[Related]** M. Crabbé. *On the Consistency of an Impredicative Subsystem of Quine's NF.* Journal of Symbolic Logic 47 (1982), 131–136.
- **[Related]** M. Boffa. *ZFJ and the Consistency Problem for NF.* Jahrbuch der Kurt-Gödel-Gesellschaft (1988), 102–106.

## 10. Worked Example / Concrete Special Case

**(a) Stratification arithmetic.** Try to build Russell's set $R=\{x: x\notin x\}$. Comprehension needs $\varphi(x)\equiv x\notin x$ stratified: the subformula $x\in x$ forces $\sigma(x)=\sigma(x)+1$, i.e. $0=1$. No such $\sigma$; the instance is not an axiom.

Now $\varphi(x)\equiv x=x$: take $\sigma(x)=0$. Stratified, so $V=\{x:x=x\}$ exists and $V\in V$.

Cantor's theorem does not collapse this. In NF the map $x\mapsto\{x\}$ is *not* a set of ordered pairs (its graph is unstratified: $\langle x,\{x\}\rangle$ needs $\sigma$ of the two coordinates equal, but $\{x\}$ sits one type above $x$). What NF proves is
$$|\mathcal{P}_1(V)| < |\mathcal{P}(V)| = |V|,$$
so $V$ is a set strictly larger than the set of its own singletons — a *non*-Cantorian set, not a contradiction.

**(b) Specker's reduction, small case.** Let $\varphi_0$ be the TST sentence "there exist exactly two objects of type $0$". Then $\varphi_0^{+}$ says "exactly two objects of type $1$", which in TST is refutable together with $\varphi_0$ (two type-$0$ objects give four type-$1$ sets). So the single instance $\varphi_0\leftrightarrow\varphi_0^{+}$ of Ambiguity already forces $\mathrm{TST}\models$ "type $0$ is infinite" — this is exactly Specker's route from Ambiguity to Infinity, and mirrors NF $\vdash$ Infinity.

**(c) Why NFU is easy and NF is not.** Take a nonstandard model $M\models\mathrm{ZFC}$ with a nontrivial automorphism-like map $\sigma$ and an ordinal $\alpha$ with $\sigma(\alpha)<\alpha$. Define a new membership on $V_{\sigma(\alpha)}^M$:
$$x \in^{*} y \iff x \in \sigma(y) \ \text{ and } \ y \in V^M_{\sigma(\alpha)+1}.$$
$(V^M_{\sigma(\alpha)},\in^{*})$ satisfies stratified comprehension, because $\sigma$ shifts types by one. But extensionality fails: distinct $y$'s with $\sigma(y)$ having the same members become $\in^{*}$-coextensional. Declaring those objects urelements yields NFU (Jensen). For NF one must instead build a genuine model of TTT, where each type-$j$ set carries a separate extension in every lower type $i<j$ — that is the content of the Holmes–Wilshaw construction, and the step Lean was needed to certify.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*