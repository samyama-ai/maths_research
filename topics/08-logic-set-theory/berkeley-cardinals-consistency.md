---
id: 08-logic-set-theory/berkeley-cardinals-consistency
title: "Berkeley Cardinals Consistency"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Berkeley Cardinals Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/berkeley-cardinals-consistency` · **Status:** open

## 1. Problem Statement / Conjecture

Is the theory $\mathrm{ZF} + \exists\,\delta\,(\delta \text{ is Berkeley})$ consistent?

A cardinal $\delta$ is **Berkeley** if for every transitive set $M$ with $\delta \in M$ and every $\eta < \delta$ there is an elementary embedding $j : M \to M$ with $\eta < \mathrm{crit}(j) < \delta$. Berkeley cardinals are the strongest large-cardinal notion currently studied. They are inconsistent with the Axiom of Choice (they yield rank-to-rank embeddings ruled out by Kunen's theorem), so the question is posed over $\mathrm{ZF}$ alone.

Three things would count as a resolution:

1. **A refutation:** a $\mathrm{ZF}$-proof that no Berkeley cardinal exists — the choiceless analogue of Kunen's inconsistency, obtained without $\mathrm{AC}$.
2. **A relative consistency proof:** derive $\mathrm{Con}(\mathrm{ZF} + \text{Berkeley})$ from a hypothesis independently believed consistent (e.g. an $\mathrm{ZFC}$ large cardinal), by construction of a model.
3. **A structure theory** strong enough to make the axiom "true" in the working sense large-cardinal axioms are: a canonical inner model, a coherent theory of $L(V_{\delta+1})$, and no derivable contradiction after sustained development.

No proof-theoretic reduction of $\mathrm{ZF}+\text{Berkeley}$ to any choiceful theory is known, and no contradiction is known. The problem is open.

## 2. Mathematical Foundations

Work in $\mathrm{ZF}$ (no $\mathrm{AC}$). For transitive $M$ let $\mathcal{E}(M)$ be the set of nontrivial elementary $j : M \to M$; $\mathrm{crit}(j)$ is the least ordinal moved.

**Reinhardt.** $\kappa$ is *Reinhardt* if there is a nontrivial elementary $j : V \to V$ (as a class, in $\mathrm{ZF}$ with a predicate for $j$, i.e. $\mathrm{ZF}_j$ with separation and replacement for $j$-formulas) with $\mathrm{crit}(j) = \kappa$.

**Berkeley.**
$$\delta \text{ is Berkeley} \iff \forall M \ (M \text{ transitive}, \delta \in M) \ \forall \eta < \delta \ \exists j \in \mathcal{E}(M) \ \big(\eta < \mathrm{crit}(j) < \delta\big).$$

**Proto-Berkeley:** drop the requirement $\mathrm{crit}(j) > \eta$; i.e. $\forall M \ni \delta$ transitive, $\mathcal{E}(M) \neq \emptyset$ with $\mathrm{crit}(j) < \delta$.

**Club Berkeley:** $\delta$ is regular and for every transitive $M \ni \delta$ and every club $C \subseteq \delta$ there is $j \in \mathcal{E}(M)$ with $\mathrm{crit}(j) \in C$.

**Limit club Berkeley:** club Berkeley and a limit of Berkeley cardinals.

**Derived measure.** If $j \in \mathcal{E}(V_\theta)$ with $\mathrm{crit}(j) = \kappa$ and $\kappa + 2 < \theta$, put
$$U_j = \{\, X \subseteq \kappa : \kappa \in j(X) \,\}.$$
In $\mathrm{ZF}$, $U_j$ is a $\kappa$-complete normal ultrafilter on $\kappa$; the completeness argument uses only elementarity applied to sequences $\langle X_\alpha : \alpha < \gamma\rangle \in V_\theta$ with $\gamma < \kappa$, and no choice.

**Kunen's theorem (ZFC).** There is no nontrivial elementary $j : V_{\lambda+2} \to V_{\lambda+2}$; equivalently no $j : V \to V$. With $\lambda = \sup_n j^n(\kappa)$ the *critical sequence*, the proof uses an $\omega$-Jónsson function $f : [\lambda]^\omega \to \lambda$ (Erdős–Hajnal), whose existence is proved from $\mathrm{AC}$.

**Basic implications** (Bagaria–Koellner–Woodin 2019): Berkeley $\Rightarrow$ proto-Berkeley; the least Berkeley $\delta_0$ equals the least proto-Berkeley cardinal; every Berkeley $\delta$ is a limit of measurable cardinals (Section 10); and $\mathrm{ZF}+\text{Berkeley} \vdash \mathrm{Con}(\mathrm{ZF} + \text{Reinhardt})$, so Berkeley sits strictly above Reinhardt in consistency strength.

## 3. History & State of the Art (SOTA)

- **1967–1974.** William Reinhardt's Berkeley dissertation proposes $j : V \to V$ as a maximal large-cardinal principle (Reinhardt, *Remarks on reflection principles, large cardinals, and elementary embeddings*, 1974).
- **1971.** Kunen refutes Reinhardt cardinals in $\mathrm{ZFC}$ (*Elementary embeddings and infinitary combinatorics*, JSL 36). His proof uses $\mathrm{AC}$ essentially; whether $\mathrm{ZF}$ alone refutes $j:V\to V$ has been open ever since.
- **1992.** In a seminar at Berkeley, Woodin (with Bagaria and others present) isolates the Berkeley property while probing how far past Reinhardt one can push without an immediate contradiction. The name records the venue.
- **1999.** Suzuki: in $\mathrm{ZF}$, no $j : V \to V$ is definable from parameters (JSL 64). This kills the easiest routes to a $\mathrm{ZF}$ refutation and the easiest routes to a model.
- **2010–2011.** Woodin's *Suitable extender models I–II* frames choiceless cardinals as a test of the Ultimate-$L$ programme: the HOD Dichotomy and the $\Omega$-conjecture become sensitive to whether the hierarchy terminates at Kunen's bound or continues.
- **2019.** Bagaria, Koellner, Woodin, *Large cardinals beyond choice* (BSL 25) is the definitive treatment: the Berkeley/club-Berkeley/$\alpha$-Berkeley hierarchy, its interaction with $\mathrm{DC}$, and the structural consequences.
- **2018–2024.** Cutolo develops $L(V_{\delta+1})$ under a Berkeley $\delta$; Schlutzenberg and Goldberg produce the first genuinely new $\mathrm{ZF}$-side results (below).

## 4. Partial Results / Verified Cases

Progress is by *localization*: fragments of the hierarchy where consistency or refutation is settled.

- **Below Kunen's bound, in $\mathrm{ZFC}$:** $I_0$–$I_3$ ($j : L(V_{\lambda+1}) \to L(V_{\lambda+1})$, $j : V_{\lambda+1}\to V_{\lambda+1}$, $j : V_\lambda \to V_\lambda$) are studied with no contradiction after 50 years; these are the strongest hypotheses compatible with choice.
- **Past Kunen's bound, in $\mathrm{ZF}$:** Schlutzenberg proved that $\mathrm{Con}(\mathrm{ZFC} + \text{an } I_0\text{-type hypothesis})$ implies $\mathrm{Con}(\mathrm{ZF} + \exists\,\lambda\,\exists j : V_{\lambda+2} \to V_{\lambda+2})$ — a hypothesis $\mathrm{ZFC}$ outright refutes. This is the only known relative-consistency proof of a genuinely post-Kunen embedding, and it stops far below Reinhardt.
- **Refuted strengthenings:** $\mathrm{ZF} + \mathrm{DC}$ refutes a *super Reinhardt* $\kappa$ with $V = \mathrm{HOD}(A)$-type definability; Suzuki's theorem refutes all definable $j : V\to V$ in $\mathrm{ZF}$; Hamkins–Kirmayer–Perlmutter (*Generalizations of the Kunen inconsistency*, APAL 163, 2012) refute $j : V \to \mathrm{HOD}$, $j : \mathrm{HOD}\to \mathrm{HOD}$ definable in $V$, and $j:V\to M$ for various inner models $M$, in $\mathrm{ZFC}$.
- **Choice fragments:** BKW show the least Berkeley $\delta_0$ satisfies $\mathrm{cf}(\delta_0) = \omega$ under $\mathrm{DC}$, and that a club Berkeley $\delta$ is incompatible with $\mathrm{DC}_\delta$. So Berkeley cardinals force choice to fail low, at a specific, computable place.
- **Structure theory:** Cutolo (*Berkeley cardinals and the structure of $L(V_{\delta+1})$*, JSL 83, 2018) proves $L(V_{\delta+1})$-analogues of $I_0$ structure theory when $\delta$ is Berkeley — the theory behaves, which is the empirical evidence for consistency.

## 5. Principal Obstacles

- **No inner model theory reaches here.** Fine-structural models are built from extenders and comparison arguments that presuppose $\mathrm{AC}$ locally and a well-ordering of the model; a Berkeley cardinal implies $\mathrm{AC}$ fails in $V$ and, by Suzuki, the witnessing embeddings are undefinable. There is no candidate $L$-like model to compare against, so the standard lower-bound machinery (core model induction) has nothing to induct on.
- **No forcing construction.** Every known technique for producing choiceless models — symmetric extensions, Solovay-style collapses, $L(\mathbb{R})$ under $\mathrm{AD}$ — starts from a $\mathrm{ZFC}$ ground model and produces failures of choice *below* the large cardinals it inherits. A Berkeley cardinal must move the ground model's own class of ordinals in a way no symmetric extension of a $\mathrm{ZFC}$ model can arrange.
- **Kunen's proof does not transfer.** The Erdős–Hajnal $\omega$-Jónsson function $f : [\lambda]^\omega \to \lambda$ needs $\mathrm{AC}$ on $\lambda^\omega$; the Woodin/Zapletal variants need $\mathrm{DC}$ or $\mathrm{AC}_\omega(\mathbb{R})$-type fragments. Berkeley cardinals sit exactly in the region where these fail: BKW's cofinality result says $\mathrm{DC}$ already breaks at $\delta_0$.
- **No reflection handle.** Consequences of a Berkeley cardinal are reflected downward, but not to any theory whose consistency we can independently gauge; the hypothesis proves $\mathrm{Con}(\mathrm{ZF}+\text{Reinhardt})$, itself of unknown status, so any reduction chain bottoms out in another open problem.
- **Absence of combinatorial content.** Small large cardinals have equivalent partition/tree characterizations that expose contradictions quickly. Berkeley is purely an embedding property with a universal quantifier over *all* transitive $M \ni \delta$; there is no known combinatorial reformulation to attack.

## 6. The Gap

Proven: (a) $\mathrm{AC}$ refutes everything from Reinhardt upward (Kunen); (b) $\mathrm{ZF}$ refutes all *definable* $j : V\to V$ (Suzuki); (c) $\mathrm{ZF}$ tolerates $j : V_{\lambda+2}\to V_{\lambda+2}$ relative to $I_0$-strength (Schlutzenberg); (d) Berkeley cardinals imply strong, coherent structure and pin down where $\mathrm{DC}$ fails (BKW, Cutolo).

Unproven: any statement connecting (c) to (a)/(b) at the level of Reinhardt or above. The exact step needed is either

- **an $\mathrm{AC}$-free Jónsson-type combinatorial device**: a $\mathrm{ZF}$-definable function $f : [\lambda]^\omega \to \lambda$ (or any coloring with the requisite non-uniformity) surviving the moves of $j$ at the critical sequence $\lambda = \sup_n j^n(\kappa)$ — which would kill Reinhardt and hence Berkeley; or
- **a symmetric/limit construction** producing a model of $\mathrm{ZF}$ with a nontrivial $j : V\to V$ from a $\mathrm{ZFC}$ hypothesis, extending Schlutzenberg's method from $V_{\lambda+2}$ to all of $V$.

Nobody has an approach that plausibly spans this gap. The interval $[V_{\lambda+2}\text{-embeddings}, \ \text{Reinhardt}]$ is entirely untouched.

## 7. Current Research (as of June 2026)

- **Goldberg (Berkeley / UC Berkeley).** The programme of extracting Kunen-style contradictions from weak choice fragments and parity/definability phenomena; *Even ordinals and the Kunen inconsistency* (Journal of Mathematical Logic, 2023) shows the Kunen argument admits $\mathrm{ZF}$-side leverage via the "even ordinals" hypothesis. Continued work on $\mathrm{ZF}$ ultrafilter theory (the Ultrapower Axiom recast without choice) *(frontier — verify)*.
- **Schlutzenberg (Münster/Bristol).** Extenders and rank-to-rank embeddings under $\mathrm{ZF}$; non-definability of Reinhardt embeddings; iterates of $V$. The Goldberg–Schlutzenberg work on periodicity in the cumulative hierarchy explains why $V_{\lambda+n}$ embeddings behave differently for even and odd $n$ — a structural reason the $\mathrm{ZFC}$/$\mathrm{ZF}$ boundary sits where it does *(frontier — verify)*.
- **Bagaria (ICREA/Barcelona) and Koellner (Wellesley).** Continuation of the BKW hierarchy: $\alpha$-Berkeley cardinals, super-Berkeley variants, and their interaction with $\mathrm{HOD}$ and set-forcing grounds.
- **Usuba (Waseda).** Ground-model and Löwenheim–Skolem-type theorems in $\mathrm{ZF}$ with choiceless cardinals, constraining how a Berkeley cardinal can arise in a forcing extension.
- **Cutolo (Napoli).** $L(V_{\delta+1})$ structure theory under Berkeley $\delta$: determinacy-like consequences and the search for an analogue of $\mathrm{AD}^{L(\mathbb{R})}$.
- **Woodin's Ultimate-$L$ programme** supplies the philosophical stakes: if the Ultimate-$L$ conjecture holds, choiceless cardinals cannot exist in $V$; a consistency proof for Berkeley cardinals would falsify the programme's maximality picture.

## 8. Future Work

- Push Schlutzenberg's relative-consistency method upward: from $j : V_{\lambda+2}\to V_{\lambda+2}$ to $j : V_{\lambda+n}\to V_{\lambda+n}$ for all $n$, then to $j : V_\theta \to V_\theta$ for $\theta$ inaccessible.
- Determine whether $\mathrm{ZF} + \mathrm{DC}_\omega$ (or $\mathrm{AC}_\omega$) already refutes Reinhardt cardinals; BKW's cofinality results suggest choice fragments are the right measuring stick.
- Find a combinatorial characterization of "Berkeley" — a partition or tree property equivalent to it over $\mathrm{ZF}$ — so that the hypothesis becomes attackable by non-embedding methods.
- Develop determinacy consequences: does a Berkeley $\delta$ imply $\mathrm{AD}^{L(V_{\delta+1})}$-type statements? A positive answer would give a consistency-strength calibration against known-consistent theories.
- Test the hypothesis empirically by deriving as many consequences as possible, the standard route by which $I_0$ became credible.

## 9. Key References

- **[Foundational]** Kenneth Kunen. *Elementary embeddings and infinitary combinatorics.* Journal of Symbolic Logic 36(3), 407–413, 1971.
- **[Foundational]** William N. Reinhardt. *Remarks on reflection principles, large cardinals, and elementary embeddings.* In Axiomatic Set Theory, Proceedings of Symposia in Pure Mathematics 13, Part 2, American Mathematical Society, 189–205, 1974.
- **[SOTA]** Joan Bagaria, Peter Koellner, W. Hugh Woodin. *Large cardinals beyond choice.* Bulletin of Symbolic Logic 25(3), 283–318, 2019.
- **[Foundational]** Akira Suzuki. *No elementary embedding from $V$ into $V$ is definable from parameters.* Journal of Symbolic Logic 64(4), 1591–1594, 1999.
- **[SOTA / Recent]** Farmer Schlutzenberg. *On the consistency of ZF with an elementary embedding from $V_{\lambda+2}$ into $V_{\lambda+2}$.* Preprint / Journal of Mathematical Logic, 2020–2024.
- **[SOTA / Recent]** Gabriel Goldberg. *Even ordinals and the Kunen inconsistency.* Journal of Mathematical Logic, 2023.
- **[Recent]** Raffaella Cutolo. *Berkeley cardinals and the structure of $L(V_{\delta+1})$.* Journal of Symbolic Logic 83(4), 1457–1476, 2018.
- **[Recent]** Joel David Hamkins, Greg Kirmayer, Norman Lewis Perlmutter. *Generalizations of the Kunen inconsistency.* Annals of Pure and Applied Logic 163(12), 1872–1890, 2012.
- **[Context]** W. Hugh Woodin. *Suitable extender models I.* Journal of Mathematical Logic 10(1–2), 101–339, 2010.
- **[Survey]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd edition, Springer, 2003.

## 10. Worked Example / Concrete Special Case

**Claim.** In $\mathrm{ZF}$: if $\delta$ is Berkeley, then $\delta$ is a limit of measurable cardinals.

*Proof.* Fix $\eta < \delta$. Choose $\theta > \delta$ with $V_\theta$ transitive and $\delta \in V_\theta$. By the Berkeley property applied to $M = V_\theta$ there is nontrivial elementary $j : V_\theta \to V_\theta$ with $\eta < \kappa := \mathrm{crit}(j) < \delta$. Set
$$U = \{\, X \subseteq \kappa : \kappa \in j(X) \,\} \in V_\theta .$$

*(i) Ultrafilter.* For $X \subseteq \kappa$, $j(\kappa \setminus X) = j(\kappa)\setminus j(X)$, and $\kappa < j(\kappa)$, so exactly one of $X, \kappa\setminus X$ is in $U$.

*(ii) $\kappa$-completeness, no choice used.* Let $\gamma < \kappa$ and let $\vec{X} = \langle X_\alpha : \alpha < \gamma\rangle \in V_\theta$ with each $X_\alpha \in U$. Then $j(\vec X) = \langle Y_\beta : \beta < j(\gamma)\rangle$ and $j(\gamma) = \gamma$, $j(\alpha)=\alpha$ for $\alpha<\gamma$, so $Y_\alpha = j(X_\alpha)$ and $\kappa \in j(X_\alpha)$ for all $\alpha<\gamma$. Hence $\kappa \in \bigcap_{\alpha<\gamma} j(X_\alpha) = j\!\left(\bigcap_{\alpha<\gamma} X_\alpha\right)$, i.e. $\bigcap_{\alpha<\gamma}X_\alpha \in U$. Note the sequence $\vec X$ is *given*, so no choice principle is invoked.

*(iii) Nonprincipality.* $\{\alpha\} \notin U$ for $\alpha<\kappa$ since $j(\{\alpha\}) = \{\alpha\} \not\ni \kappa$.

So $\kappa$ is measurable and $\eta < \kappa < \delta$. As $\eta<\delta$ was arbitrary, $\delta$ is a limit of measurables. $\square$

**Where Kunen would strike, and why he cannot.** Take the critical sequence $\kappa_0 = \kappa$, $\kappa_{n+1} = j(\kappa_n)$, $\lambda = \sup_n \kappa_n$. Under $\mathrm{AC}$, Erdős–Hajnal give an $\omega$-Jónsson $f : [\lambda]^\omega \to \lambda$; elementarity forces $j(f) = f$ on a set witnessing $f''[j''\lambda]^\omega = \lambda$, yet $\kappa \notin \mathrm{ran}$ — contradiction. Without $\mathrm{AC}$ no such $f$ is available, and by BKW the least Berkeley $\delta_0$ has $\mathrm{cf}(\delta_0)=\omega$ under $\mathrm{DC}$, so the relevant $\omega$-sequences exist while the choice needed to color them does not. That single missing function is the whole gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*