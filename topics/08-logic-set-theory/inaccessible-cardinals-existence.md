---
id: 08-logic-set-theory/inaccessible-cardinals-existence
title: "Inaccessible Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Inaccessible Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/inaccessible-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

An uncountable cardinal $\kappa$ is **(strongly) inaccessible** if it is regular and a strong limit:
$$\operatorname{cf}(\kappa)=\kappa \quad\text{and}\quad \forall \lambda<\kappa\;\; 2^{\lambda}<\kappa .$$

**The problem.** Does an inaccessible cardinal exist? Equivalently, is the sentence
$$\mathrm{IC}:\quad \exists \kappa\,(\kappa>\omega \wedge \operatorname{cf}(\kappa)=\kappa \wedge \forall\lambda<\kappa\,(2^\lambda<\kappa))$$
true of the intended cumulative hierarchy $V$?

Two facts fix the shape of the question and are *theorems*, not conjectures:

1. **ZFC $\nvdash$ IC** (assuming ZFC consistent). If $\kappa$ is inaccessible then $V_\kappa \models \mathrm{ZFC}$, so $\mathrm{ZFC}+\mathrm{IC}\vdash \mathrm{Con}(\mathrm{ZFC})$; Gödel's second incompleteness theorem then blocks any ZFC proof of IC.
2. **ZFC $\nvdash \neg$IC is not provable in ZFC either.** If ZFC proved $\neg\mathrm{IC}$, that would be a ZFC-internal refutation; but no such proof is known, and by (1) no consistency proof of $\mathrm{ZFC}+\mathrm{IC}$ from ZFC is possible. So the *independence* of IC from ZFC cannot itself be established from ZFC alone — only the unprovability half can.

A complete resolution therefore means one of: (a) a derivation of a contradiction from $\mathrm{ZFC}+\mathrm{IC}$ (settling it negatively and outright); or (b) a philosophically and mathematically decisive argument — a new axiom or a canonical inner-model / reflection principle accepted as true of $V$ — that entails IC. The status **partially-solved** reflects that the *formal* metamathematics is completely settled while the *truth* question is not.

## 2. Mathematical Foundations

**Cumulative hierarchy.** $V_0=\varnothing$, $V_{\alpha+1}=\mathcal{P}(V_\alpha)$, $V_\lambda=\bigcup_{\alpha<\lambda}V_\alpha$ for limit $\lambda$; $V=\bigcup_{\alpha\in\mathrm{Ord}}V_\alpha$.

**Cofinality.** $\operatorname{cf}(\alpha)$ is the least order type of a cofinal subset of $\alpha$. $\kappa$ is *regular* iff $\operatorname{cf}(\kappa)=\kappa$, i.e. $\kappa$ is not the union of $<\kappa$ sets each of size $<\kappa$.

**Beth function.** $\beth_0=\aleph_0$, $\beth_{\alpha+1}=2^{\beth_\alpha}$, $\beth_\lambda=\sup_{\alpha<\lambda}\beth_\alpha$. Then $\kappa$ is a strong limit iff $\kappa=\beth_\kappa$ (for $\kappa>\omega$ a limit).

**Weak vs. strong.** $\kappa$ is *weakly inaccessible* iff regular and a limit cardinal ($\kappa=\aleph_\kappa$ suffices with regularity). Under GCH the two notions coincide, since $2^\lambda=\lambda^+$.

**Key theorem (Zermelo 1930; Shepherdson 1952).**
$$\kappa \text{ inaccessible} \;\Longrightarrow\; V_\kappa \models \mathrm{ZFC},\qquad |V_\kappa|=\kappa,\qquad V_\kappa = H_\kappa,$$
where $H_\kappa$ is the class of sets of hereditary cardinality $<\kappa$. Regularity yields Replacement; strong limit yields Power Set.

**Consistency-strength ordering.** For theories $T,S$ write $T\le_{\mathrm{Con}} S$ iff $\mathrm{PA}\vdash \mathrm{Con}(S)\to\mathrm{Con}(T)$. Then
$$\mathrm{ZFC} <_{\mathrm{Con}} \mathrm{ZFC}+\mathrm{Con}(\mathrm{ZFC}) <_{\mathrm{Con}} \mathrm{ZFC}+\exists\text{ transitive model of ZFC} <_{\mathrm{Con}} \mathrm{ZFC}+\exists\text{ worldly }\kappa <_{\mathrm{Con}} \mathrm{ZFC}+\mathrm{IC}.$$
($\kappa$ is *worldly* iff $V_\kappa\models\mathrm{ZFC}$; worldly cardinals need not be regular, and the least worldly cardinal has cofinality $\omega$.)

**Second-order categoricity (Zermelo 1930).** The models of second-order ZFC are exactly the $\langle V_\kappa,\in\rangle$ for $\kappa$ inaccessible, and they are linearly ordered by end-extension — Zermelo's *quasi-categoricity*. Under this reading "no inaccessibles" says second-order ZFC has no models at all.

**Grothendieck universes.** A universe $U$ is a transitive set closed under pairing, power set and $U$-indexed unions with $\omega\in U$. Tarski's Axiom (every set lies in a universe) is equivalent over ZFC to "there is a proper class of inaccessibles"; and $U=V_\kappa$ for $\kappa$ inaccessible is the only nontrivial form.

## 3. History & State of the Art (SOTA)

- **1908.** Hausdorff isolates regular limit cardinals (*Grundzüge einer Theorie der geordneten Mengen*), noting their existence cannot be established by the usual operations.
- **1930.** Sierpiński and Tarski, and independently Zermelo, define the strongly inaccessible cardinals; Zermelo's *Über Grenzzahlen und Mengenbereiche* gives the $V_\kappa$ characterization and the quasi-categoricity theorem.
- **1931/1938.** Gödel's incompleteness theorems, then $L$; Gödel later argues explicitly that inaccessibles follow from the iterative conception's reflection idea.
- **1952–53.** Shepherdson's *Inner models for set theory* fixes the modern proof that ZFC cannot prove IC.
- **1960s.** Lévy's reflection schema shows ZFC proves each finite fragment reflects; IC is exactly the "one model does it all" strengthening. Feferman–Lévy models expose the role of inaccessibles in choiceless analysis.
- **1970.** Solovay: from an inaccessible, a model of $\mathrm{ZF}+\mathrm{DC}$ in which every set of reals is Lebesgue measurable, has the Baire property and the perfect set property.
- **1984.** Shelah: the inaccessible is *necessary* for full Lebesgue measurability, but removable for the Baire property — the first sharp equiconsistency pinning IC to a statement of analysis.
- **1972 onward.** SGA 4 adopts universes for Grothendieck's cohomological machinery; McLarty (2010, 2020) shows the number-theoretic applications, including Wiles' proof of FLT, do not need them.
- **Current SOTA.** IC is the base of the large-cardinal hierarchy; every stronger axiom (Mahlo, weakly compact, measurable, Woodin, supercompact) implies IC and is calibrated against it. No contradiction has surfaced in ~95 years, and the hierarchy's linear ordering by consistency strength is the main empirical evidence for its coherence.

## 4. Partial Results / Verified Cases

- **Unprovability, sharp form.** $\mathrm{ZFC}+\mathrm{IC}\vdash\mathrm{Con}(\mathrm{ZFC})$, indeed $\vdash\mathrm{Con}(\mathrm{ZFC}+\mathrm{Con}(\mathrm{ZFC}))$ and every finite iterate. So ZFC $\nvdash$ IC.
- **Weak $\to$ strong.** If $\kappa$ is weakly inaccessible in $V$, then $\kappa$ is strongly inaccessible in $L$ (GCH holds in $L$; regularity and limit-ness are downward absolute). Hence $\mathrm{Con}(\mathrm{ZFC}+\exists\text{ weakly inacc.}) \Leftrightarrow \mathrm{Con}(\mathrm{ZFC}+\mathrm{IC})$.
- **Descriptive set theory, exact calibrations.**
 * "Every $\Sigma^1_2$ set of reals is Lebesgue measurable" $\Leftrightarrow_{\mathrm{Con}}$ IC (Solovay, Shelah); equivalently "$\aleph_1^V$ is inaccessible in $L[r]$ for every real $r$".
 * "Every set of reals is Lebesgue measurable" (ZF+DC) $\Leftrightarrow_{\mathrm{Con}}$ IC (Solovay 1970 up; Shelah 1984 down).
 * "Every set of reals has the Baire property" (ZF+DC) is equiconsistent with ZFC alone — **no** inaccessible needed (Shelah 1984). This is the sharp negative case.
- **Forcing behaviour.** Inaccessibility is preserved by $\kappa$-c.c. forcing of size $<\kappa$ and by $\mathrm{Add}(\kappa,\lambda)$; Lévy collapse $\mathrm{Coll}(\omega,<\kappa)$ turns an inaccessible $\kappa$ into $\aleph_1$. Any inaccessible can be destroyed by adding a Cohen subset of some $\lambda<\kappa$ enlarging $2^\lambda$.
- **Downward implications verified.** Measurable $\Rightarrow$ Mahlo $\Rightarrow$ inaccessible; a measurable $\kappa$ is the $\kappa$-th inaccessible. Conversely $L$ can contain inaccessibles but never a measurable (Scott 1961: $V=L$ refutes measurables).
- **Ordinary mathematics.** For arithmetic and number theory, universes are eliminable: McLarty (2020) formalizes Grothendieck's étale-cohomological apparatus, and thereby the FLT proof, in finite-order arithmetic — strength far below ZFC, let alone IC.

## 5. Principal Obstacles

- **Gödelian barrier.** Any proof of IC inside ZFC would yield $\mathrm{ZFC}\vdash\mathrm{Con}(\mathrm{ZFC})$. This is not a gap in technique; it is a theorem that the technique cannot exist.
- **Forcing is the wrong tool for the positive direction.** Forcing extensions $V[G]$ have the same ordinals as $V$ and cannot manufacture an inaccessible where none exists — set forcing preserves "$\kappa$ is not inaccessible" in the sense that large cardinals can only be *created* from prior large-cardinal strength. Hence the standard independence machinery, which settles CH and Souslin's hypothesis, is structurally unable to produce a model of IC from a model of ZFC.
- **Inner models are downward, not upward.** $L$, $L[U]$ and the fine-structural core models extract large cardinals from $V$; they never add strength. Core model theory gives lower bounds ("if X then there is an inner model with an inaccessible") but no absolute existence.
- **Consistency evidence is inductive.** The case for IC is that ninety-five years of work, including deep fine-structure and determinacy theory, has produced no contradiction, and the hierarchy is linearly ordered — but Kunen's inconsistency theorem (no nontrivial $j:V\to V$) shows the hierarchy does terminate in contradiction somewhere, so "no contradiction yet" is not decisive.
- **No arithmetic consequence forces it.** Unlike Woodin cardinals (which decide projective statements), IC has no known $\Pi^0_1$ or combinatorial consequence in ordinary mathematics that is independently compelling — the FLT/universes case turned out eliminable, removing the most-cited applied motive.

## 6. The Gap

Proven: the exact consistency-strength position of IC, its equiconsistency with $\Sigma^1_2$ measurability and with full Lebesgue measurability in ZF+DC, and its unprovability in ZFC. Not proven: whether $V$ *contains* such a $\kappa$.

The precise barrier is that IC is a $\Sigma_2$ statement about $V$ with no reduction to any absolute or forcing-invariant core. Crossing it requires one of:

1. a formal contradiction in $\mathrm{ZFC}+\mathrm{IC}$ (which would collapse the whole large-cardinal hierarchy above it); or
2. an accepted extrinsic/intrinsic justification — a reflection principle of the form "any property of $V$ holds in some $V_\kappa$" strong enough to yield IC while itself being motivated by the iterative conception rather than by its consequences.

Reflection schemas provable in ZFC (Lévy) reflect only *first-order* formulas one at a time; the step to reflecting the *satisfaction relation* is exactly the step that produces an inaccessible, and it is precisely the step ZFC cannot take.

## 7. Current Research (as of June 2026)

- **Inner model program (Woodin; Steel; Schindler; Sargsyan; Jensen).** Ultimate-$L$ aims at a canonical inner model absorbing all known large cardinals; if the Ultimate-$L$ conjecture holds, large-cardinal axioms including IC gain strong extrinsic justification through a single canonical picture of $V$. *(frontier — verify)*
- **Reflection and structural principles (Bagaria, Barcelona; Koellner, Harvard).** $C^{(n)}$-cardinals and higher-order reflection principles (Bagaria, *Archive for Mathematical Logic* 51, 2012) recast the hierarchy as an ascending sequence of reflection strengths, with IC as the first genuine level.
- **Multiverse views (Hamkins, Oxford/Notre Dame; Väänänen, Helsinki).** On the multiverse picture the question "does an inaccessible exist?" is not determinate; it is replaced by the study of which universes have them. Väänänen's second-order/internal-categoricity work bears directly on Zermelo's quasi-categoricity reading.
- **Reverse mathematics of Grothendieck machinery (McLarty, Case Western).** Ongoing formalization work continues to push universe-free foundations for algebraic geometry, with proof assistants (Lean's mathlib, Coq/UniMath) making the elimination checkable rather than programmatic.
- **Set-theoretic geology and forcing axioms (Viale, Turin; Asperó–Schindler).** The 2021 proof that $\mathrm{MM}^{++}\Rightarrow(*)$ has renewed interest in whether forcing axioms give a preferred theory of $H_{\omega_2}$; their large-cardinal cost sits far above IC.

## 8. Future Work

- Settle the Ultimate-$L$ conjecture; a positive answer would make the large-cardinal hierarchy, IC included, part of a single canonical structure theory rather than a menu of assumptions (Woodin's stated program).
- Find an *intrinsically* motivated reflection principle entailing IC that does not presuppose a satisfaction class — the philosophical target set by Gödel, Maddy (*Believing the axioms*) and Koellner.
- Search for concrete incompleteness: Harvey Friedman's Boolean relation theory aims at finitary combinatorial statements provably equivalent to large-cardinal consistency, which would give IC a mathematical rather than metamathematical warrant.
- Continue mechanized reverse mathematics of "universe-using" arguments to establish, case by case, where universes are essential rather than convenient.
- Map the region between $\mathrm{Con}(\mathrm{ZFC})$ and IC (worldly cardinals, $\Sigma_n$-correct cardinals, transitive-model hypotheses) more finely; this is where a contradiction, if any, would first be visible.

## 9. Key References

- **[Foundational]** E. Zermelo. *Über Grenzzahlen und Mengenbereiche: Neue Untersuchungen über die Grundlagen der Mengenlehre.* Fundamenta Mathematicae 16 (1930), 29–47.
- **[Foundational]** W. Sierpiński, A. Tarski. *Sur une propriété caractéristique des nombres inaccessibles.* Fundamenta Mathematicae 15 (1930), 292–300.
- **[Foundational]** J. C. Shepherdson. *Inner models for set theory — Part II / Part III.* Journal of Symbolic Logic 17 (1952), 225–237; 18 (1953), 145–167.
- **[Foundational]** R. M. Solovay. *A model of set-theory in which every set of reals is Lebesgue measurable.* Annals of Mathematics 92 (1970), 1–56.
- **[SOTA / Recent]** S. Shelah. *Can you take Solovay's inaccessible away?* Israel Journal of Mathematics 48 (1984), 1–47.
- **[SOTA / Recent]** C. McLarty. *What does it take to prove Fermat's Last Theorem? Grothendieck and the logic of number theory.* Bulletin of Symbolic Logic 16 (2010), 359–377.
- **[SOTA / Recent]** C. McLarty. *The large structures of Grothendieck founded on finite-order arithmetic.* Review of Symbolic Logic 13 (2020), 296–325.
- **[SOTA / Recent]** J. Bagaria. *$C^{(n)}$-cardinals.* Archive for Mathematical Logic 51 (2012), 213–240.
- **[SOTA / Recent]** J. D. Hamkins. *The set-theoretic multiverse.* Review of Symbolic Logic 5 (2012), 416–449.
- **[Survey]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Survey]** T. Jech. *Set Theory: The Third Millennium Edition.* Springer, 2003.
- **[Survey]** F. R. Drake. *Set Theory: An Introduction to Large Cardinals.* North-Holland, 1974.
- **[Survey]** P. Maddy. *Believing the Axioms, I.* Journal of Symbolic Logic 53 (1988), 481–511.
- **[Survey]** M. Foreman, A. Kanamori (eds.). *Handbook of Set Theory.* Springer, 2010.
- **[Context]** M. Artin, A. Grothendieck, J.-L. Verdier. *Théorie des topos et cohomologie étale des schémas (SGA 4), Tome 1*, Appendix "Univers" by N. Bourbaki. Lecture Notes in Mathematics 269, Springer, 1972.

## 10. Worked Example / Concrete Special Case

**(a) Regularity and strong-limit are independent — a computation.** Take $\kappa=\beth_\omega$. Compute the beth sequence:
$$\beth_0=\aleph_0,\quad \beth_1=2^{\aleph_0},\quad \beth_2=2^{2^{\aleph_0}},\ \dots,\quad \beth_\omega=\sup_{n<\omega}\beth_n.$$
$\beth_\omega$ **is** a strong limit: for $\lambda<\beth_\omega$ pick $n$ with $\lambda<\beth_n$, then $2^\lambda\le 2^{\beth_n}=\beth_{n+1}<\beth_\omega$. But $\{\beth_n : n<\omega\}$ is cofinal of order type $\omega$, so $\operatorname{cf}(\beth_\omega)=\omega<\beth_\omega$: not regular. By König's theorem $\beth_\omega^{\;\omega}>\beth_\omega$. So ZFC *proves* strong limits of any size exist; the whole difficulty of IC lies in regularity.

Symmetrically, $\aleph_1$ is regular (ZFC) but not a strong limit, since $2^{\aleph_0}\ge\aleph_1$. Neither half alone is hard; only their conjunction is unprovable.

**(b) Why $V_\kappa\models\mathrm{ZFC}$ for $\kappa$ inaccessible.** First, by induction, $|V_{\omega+\alpha}|=\beth_\alpha$; strong-limit-ness gives $|V_\alpha|<\kappa$ for all $\alpha<\kappa$, and regularity then gives $|V_\kappa|=\kappa$.

*Power Set.* Let $x\in V_\kappa$, say $x\subseteq V_\alpha$ with $\alpha<\kappa$. Then $\mathcal{P}(x)\subseteq V_{\alpha+1}$ and $|\mathcal P(x)|\le 2^{|V_\alpha|}<\kappa$ because $|V_\alpha|<\kappa$ and $\kappa$ is a strong limit. Hence $\mathcal P(x)\in V_{\alpha+2}\subseteq V_\kappa$.

*Replacement.* Let $a\in V_\kappa$ and $F:a\to V_\kappa$ definable in $V_\kappa$. Each $F(u)$ has rank $\rho(u)<\kappa$, and $|a|<\kappa$. The set $\{\rho(u):u\in a\}$ is a subset of $\kappa$ of size $<\kappa$, so by **regularity** it is bounded: $\sup_{u\in a}\rho(u)=\beta<\kappa$. Therefore $F[a]\subseteq V_\beta$ and $F[a]\in V_{\beta+1}\subseteq V_\kappa$. (This is the only place regularity is used, and it is exactly the axiom that fails for $\beth_\omega$: the map $n\mapsto \beth_n$ sends the set $\omega\in V_{\beth_\omega}$ cofinally into $\beth_\omega$.)

Foundation, Extensionality, Pairing, Union, Infinity and Choice are immediate from transitivity and $\omega\in V_\kappa$.

**(c) The Gödelian punchline.** From (b), $\mathrm{ZFC}+\mathrm{IC}$ proves "there is a set model of ZFC", hence $\mathrm{Con}(\mathrm{ZFC})$. If ZFC proved IC, ZFC would prove its own consistency, contradicting Gödel's second incompleteness theorem (ZFC interprets PA). Hence:
$$\mathrm{Con}(\mathrm{ZFC}) \;\Longrightarrow\; \mathrm{ZFC}\nvdash \mathrm{IC}.$$
Note the asymmetry that makes the problem *partially* solved: the same argument gives no model of $\mathrm{ZFC}+\neg\mathrm{IC}$-refuting information, and — by the second incompleteness theorem again — no ZFC proof of $\mathrm{Con}(\mathrm{ZFC}+\mathrm{IC})$ can exist. The existence question is therefore not merely open but provably beyond ZFC's own means.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*