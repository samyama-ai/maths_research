---
id: 08-logic-set-theory/axiom-of-real-determinacy-consistency
title: "Axiom of Real Determinacy Consistency"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Axiom of Real Determinacy Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/axiom-of-real-determinacy-consistency` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

$\mathsf{AD}_\mathbb{R}$ is the assertion that every two-player infinite game of length $\omega$ in which the players alternately play **real numbers** is determined. The problem is to calibrate its consistency strength exactly:

1. **(Relative consistency.)** Find the weakest large-cardinal hypothesis $\Phi$ with $\mathrm{Con}(\mathsf{ZFC} + \Phi) \Rightarrow \mathrm{Con}(\mathsf{ZF} + \mathsf{AD}_\mathbb{R})$, and a matching inner-model converse $\mathrm{Con}(\mathsf{ZF}+\mathsf{AD}_\mathbb{R}) \Rightarrow \mathrm{Con}(\mathsf{ZFC}+\Phi)$.
2. **(Solovay hierarchy.)** Determine the exact strengths of the strictly increasing theories
$$\mathsf{AD}_\mathbb{R} \;<\; \mathsf{AD}_\mathbb{R}+\mathsf{DC} \;<\; \mathsf{AD}_\mathbb{R}+\text{“}\Theta\text{ is regular”} \;<\; \mathsf{LSA},$$
where "$<$" means strictly greater consistency strength.

By Gödel's second incompleteness theorem $\mathrm{Con}(\mathsf{AD}_\mathbb{R})$ is not provable in $\mathsf{ZFC}$ (indeed $\mathsf{AD}_\mathbb{R}$ proves $\mathrm{Con}(\mathsf{ZFC}+\text{infinitely many Woodin cardinals})$), so "solution" means a two-sided equiconsistency with an independently formulated large-cardinal axiom, proved by a derived-model construction in one direction and a fine-structural inner-model (hod mouse) construction in the other. The status is **partially-solved**: upper bounds and a converse exist for the whole hierarchy in the presence of iterability hypotheses, but the exact strength of $\mathsf{AD}_\mathbb{R}$ itself, and unconditional converses, remain open.

## 2. Mathematical Foundations

**Games on reals.** Fix $\mathbb{R} = {}^{\omega}\omega$ (Baire space). For $A \subseteq {}^{\omega}\mathbb{R}$, the game $G(A)$ has players I and II alternately playing $x_0, x_1, x_2, \dots \in \mathbb{R}$; I wins the run iff $\langle x_n : n<\omega\rangle \in A$. Then
$$\mathsf{AD}_\mathbb{R} \;:\equiv\; \forall A \subseteq {}^{\omega}\mathbb{R}\;\big(\exists \sigma\,(\sigma \text{ w.s. for I}) \;\vee\; \exists\tau\,(\tau \text{ w.s. for II})\big).$$
$\mathsf{AD}$ is the same statement with moves in $\omega$. Since $\mathbb{R}$ codes $\omega$-sequences, $\mathsf{AD}_\mathbb{R} \Rightarrow \mathsf{AD}$; both contradict $\mathsf{AC}$, so the ambient theory is $\mathsf{ZF}$ (optionally $+\,\mathsf{DC}$).

**Uniformization.** $\mathsf{Unif}$: for every $R \subseteq \mathbb{R}\times\mathbb{R}$ there is $f$ with $\mathrm{dom}(f) = \{x : \exists y\, R(x,y)\}$ and $R(x,f(x))$ for all $x \in \mathrm{dom}(f)$.
> **Theorem (Solovay; Kechris 1988).** $\mathsf{AD}_\mathbb{R} \Rightarrow \mathsf{Unif}$, and $\mathsf{ZF}+\mathsf{AD}+\mathsf{Unif}$ is equivalent to "half-$\mathsf{AD}_\mathbb{R}$", hence to $\mathsf{AD}_\mathbb{R}$.

**The ordinal $\Theta$.**
$$\Theta = \sup\{\alpha \in \mathrm{Ord} : \exists\, \text{surjection } \pi : \mathbb{R} \twoheadrightarrow \alpha\}.$$
Under $\mathsf{AD}$, $\Theta$ is a limit cardinal of uncountable cofinality-in-$\mathsf{DC}$ contexts; under $\mathsf{AD}_\mathbb{R}$, $\Theta$ is a limit of Suslin cardinals and $\mathrm{cf}(\Theta) > \omega$. The **Solovay sequence** $\langle \theta_\alpha \rangle$ is defined by: $\theta_0$ = sup of ordinals that are $\mathrm{OD}$-surjective images of $\mathbb{R}$; $\theta_{\alpha+1}$ = sup of ordinals that are $\mathrm{OD}(A)$-images of $\mathbb{R}$ for some $A \subseteq \mathbb{R}$ of Wadge rank $\theta_\alpha$; limits by suprema. Then $\Theta = \theta_\lambda$ for some $\lambda$.

**Suslin sets.** $A \subseteq \mathbb{R}$ is $\kappa$-Suslin if $A = p[T]$ for a tree $T$ on $\omega\times\kappa$, i.e. $x \in A \iff \exists f \in {}^{\omega}\kappa\,\forall n\, (x{\upharpoonright}n, f{\upharpoonright}n) \in T$.
> **Theorem (Woodin).** Assume $\mathsf{AD}^+$. Then $\mathsf{AD}_\mathbb{R}$ holds iff every set of reals is Suslin.

Here $\mathsf{AD}^+$ is $\mathsf{AD}+\mathsf{DC}_\mathbb{R}+\ $"every set of reals is $\infty$-Borel"$+\ $ordinal determinacy for games on $\omega$ with payoff continuously reducible in $\lambda < \Theta$.

**Derived model.** Let $\lambda$ be a limit of Woodin cardinals, $G \subseteq \mathrm{Coll}(\omega,{<}\lambda)$ generic, $\mathbb{R}^*_G = \bigcup_{\alpha<\lambda}\mathbb{R}^{V[G{\upharpoonright}\alpha]}$, and $\mathrm{Hom}^*$ the $\mathbb{R}^*$-sets with $\lambda$-absolutely-complemented trees. The derived model is $D(V,\lambda) = L(\mathbb{R}^*, \mathrm{Hom}^*)$.
> **Derived Model Theorem (Woodin).** $D(V,\lambda) \models \mathsf{AD}^+$. If moreover $\lambda$ is a limit of cardinals $\kappa < \lambda$ that are ${<}\lambda$-strong, then $D(V,\lambda) \models \mathsf{AD}_\mathbb{R}$.

**Large-cardinal side.** A **Woodin limit of Woodins** is a Woodin cardinal $\delta$ that is a limit of Woodin cardinals — the current calibration point for $\mathsf{AD}_\mathbb{R} + \text{“}\Theta\text{ regular”}$.

## 3. History & State of the Art (SOTA)

- **1962.** Mycielski–Steinhaus propose $\mathsf{AD}$; Mycielski soon isolates the stronger $\mathsf{AD}_\mathbb{R}$ ("$\mathsf{AD}$ for games with moves in an arbitrary set") and observes $\mathsf{AD}_{\mathbb{R}} \Rightarrow \mathsf{AD}$ while $\mathsf{AD}_X$ for $|X| \ge |\mathcal{P}(\mathbb{R})|$ is outright inconsistent.
- **1970s (Solovay).** $\mathsf{AD}_\mathbb{R}$ implies uniformization; $\mathsf{AD}_\mathbb{R}+\mathsf{DC}$ yields a normal fine measure on $\mathcal{P}_{\omega_1}(\mathbb{R})$, from which $\mathsf{AD}_\mathbb{R}+\mathsf{DC} \vdash \mathrm{Con}(\mathsf{AD}_\mathbb{R})$ — so $\mathsf{DC}$ is *not* provable from $\mathsf{AD}_\mathbb{R}$ (Solovay 1978). This is the first strictness result in the hierarchy and the reason "$\mathsf{AD}_\mathbb{R}$ consistency" is a hierarchy problem, not a single question.
- **1980s (Woodin, Martin, Steel).** $\mathsf{AD}^{L(\mathbb{R})}$ from $\omega$ Woodin cardinals with a measurable above (Martin–Steel 1989 for $\mathsf{PD}$; Woodin for the full $L(\mathbb{R})$ result). The derived model machinery gives the upper bound for $\mathsf{AD}_\mathbb{R}$.
- **1990s–2000s.** $\mathsf{AD}^+$ theory; the Suslin characterization of $\mathsf{AD}_\mathbb{R}$; Steel's exposition of the derived model theorem (2009).
- **2010s (Sargsyan).** Core model induction plus the **hod mouse** hierarchy: $\mathsf{AD}_\mathbb{R}+\text{“}\Theta\text{ is regular”}$ is consistent relative to $\mathsf{ZFC}+$ "there is a Woodin limit of Woodins" (Sargsyan, *Hod Mice and the Mouse Set Conjecture*, Memoirs AMS, 2015), a dramatic reduction of the previously known upper bounds.
- **2020s (Sargsyan–Trang).** The **Largest Suslin Axiom** ($\mathsf{LSA}$: $\mathsf{AD}^+$ + $\Theta = \theta_{\alpha+1}$ where $\theta_\alpha$ is the largest Suslin cardinal) is developed as the next calibration point above $\mathsf{AD}_\mathbb{R}+\Theta$-regular; *The Largest Suslin Axiom* (Lecture Notes in Logic 56, ASL/Cambridge, 2024) proves its consistency and derives it as a lower bound from combinatorial hypotheses.

## 4. Partial Results / Verified Cases

- **Upper bound, base case.** If $\lambda$ is a limit of Woodin cardinals *and* a limit of ${<}\lambda$-strong cardinals, then $D(V,\lambda) \models \mathsf{AD}_\mathbb{R}$. Hence $\mathrm{Con}(\mathsf{ZFC}+\exists\lambda\,\text{such})\Rightarrow \mathrm{Con}(\mathsf{ZF}+\mathsf{AD}_\mathbb{R})$.
- **$\mathsf{DC}$ version.** When $\mathrm{cf}(\lambda) > \omega$ the derived model additionally satisfies $\mathsf{DC}$, giving $\mathrm{Con}(\mathsf{AD}_\mathbb{R}+\mathsf{DC})$ from the same hypothesis with $\lambda$ of uncountable cofinality.
- **$\Theta$ regular.** $\mathrm{Con}(\mathsf{ZFC}+\text{Woodin limit of Woodins}) \Rightarrow \mathrm{Con}(\mathsf{AD}_\mathbb{R}+\text{“}\Theta\text{ regular”})$ (Sargsyan 2015).
- **Strictness (lower bounds inside the hierarchy).** $\mathsf{AD}_\mathbb{R}+\mathsf{DC} \vdash \mathrm{Con}(\mathsf{AD}_\mathbb{R})$; $\mathsf{AD}_\mathbb{R}+\text{“}\Theta$ regular$\text{”} \vdash \mathrm{Con}(\mathsf{AD}_\mathbb{R}+\mathsf{DC})$; $\mathsf{LSA}$ (in the relevant models) proves $\mathrm{Con}(\mathsf{AD}_\mathbb{R}+\Theta\text{ regular})$. All four theories are pairwise non-equiconsistent.
- **Segments of the Solovay sequence.** For theories $\mathsf{AD}^+ + \Theta = \theta_\alpha$ with $\alpha$ small (notably $\alpha = 0,1,2$, and successor stages below the minimal model of $\mathsf{AD}_\mathbb{R}$), hod-mouse analysis yields exact equiconsistencies with hypotheses about Woodin cardinals in hod mice; these are the "verified dimensions" of the calibration.
- **Converse direction, conditional.** Under $\mathsf{AD}^+ + \mathsf{MSC}$ (Mouse Set Conjecture) and the relevant iterability hypotheses, $\mathrm{HOD}$ of a model of $\mathsf{AD}_\mathbb{R}+\Theta$-regular is a hod premouse with a Woodin limit of Woodins-like structure, closing the loop to an equiconsistency modulo iterability.

## 5. Principal Obstacles

- **Iterability.** Every inner-model-theoretic lower bound requires that the constructed hod premice be *iterable* — i.e. that iteration strategies exist and can be selected coherently. At and above $\mathsf{AD}_\mathbb{R}$ the strategies must themselves be self-scaled ($\Sigma$ must be captured by mice built from $\Sigma$), and no unconditional construction of such strategies is known past the current hierarchy. This is the single largest obstruction; it is why results are stated "modulo iterability" or under $\mathsf{MSC}$.
- **Failure of $\mathsf{AC}$-based fine structure.** Classical comparison arguments use choice and linear iterations; long games and Suslin representations at $\Theta$ force *tree* iterations with branch-selection ambiguity (the "branch existence" problem), which comparison arguments cannot resolve by counting.
- **No Suslin representation at the top.** Under $\mathsf{AD}$ alone, sets past the largest Suslin cardinal have no tree representation, so scales, uniformization and the Third Periodicity theorem — the standard toolkit for producing definable winning strategies — simply stop applying. $\mathsf{AD}_\mathbb{R}$ is precisely the assertion that this failure never occurs, so it cannot be proved by that toolkit.
- **Core model induction saturates.** The induction proceeds through levels of the Solovay sequence; at limit stages of uncountable cofinality (exactly where $\Theta$ becomes regular) one needs a new "hod pair" at a limit level, and the direct-limit system used to build it is not known to be well-founded without additional hypotheses.
- **$\mathsf{DC}$ is not free.** Solovay's result shows the choice-theoretic strength is entangled with the determinacy strength: any upper-bound construction must decide $\mathsf{DC}$ in the target model, which the derived model does only under a cofinality assumption on $\lambda$.

## 6. The Gap

Proven (Section 4): a *sufficient* large-cardinal hypothesis for each of $\mathsf{AD}_\mathbb{R}$, $\mathsf{AD}_\mathbb{R}+\mathsf{DC}$, $\mathsf{AD}_\mathbb{R}+\Theta$-regular, and a converse that is conditional on iterability/$\mathsf{MSC}$.

Missing: (i) an *exact* large-cardinal characterization of plain $\mathsf{AD}_\mathbb{R}$ — the derived-model hypothesis (limit of Woodins that is also a limit of ${<}\lambda$-strongs) is not known to be optimal, and no matching inner model has been constructed from $\mathsf{AD}_\mathbb{R}$ alone; (ii) an unconditional proof that hod pairs at the $\mathsf{AD}_\mathbb{R}$ level are iterable, removing the $\mathsf{MSC}$/iterability hypothesis from the converse. The precise step to cross is: *from $\mathsf{ZF}+\mathsf{AD}_\mathbb{R}$, construct in $\mathrm{HOD}$ a fully iterable hod premouse whose Woodin cardinals witness the derived-model hypothesis*, i.e. prove $\mathrm{HOD}^{\mathsf{AD}_\mathbb{R}}\models\mathsf{ZFC}+\Phi$ with $\Phi$ the same $\Phi$ used in the upper bound.

## 7. Current Research (as of June 2026)

- **Sargsyan–Trang programme (Gdańsk / IMPAN, UNT).** Post-$\mathsf{LSA}$ hod mice: extending the hod hierarchy past the Largest Suslin Axiom toward "$\mathsf{AD}_\mathbb{R} + \Theta$ is measurable" and Woodin-in-$\mathrm{HOD}$ configurations. *(frontier — verify)*
- **Core model induction from combinatorics.** Deriving $\mathsf{LSA}$-strength determinacy from $\mathsf{PFA}$, from the failure of square principles at singulars, and from generic-absoluteness/Sealing hypotheses (Woodin's Sealing theorem and its consistency-strength consequences). *(frontier — verify)*
- **$\mathsf{Sealing}$ and $\mathsf{LSA}$-over-uB.** Woodin's Sealing theorem (from a supercompact, Sealing holds in all set-generic extensions) has reoriented work on how much determinacy is forced by generic absoluteness of the theory of the universally Baire sets.
- **Long games.** Games of length $\omega\cdot n$ and clopen length-$\omega_1$ games on $\omega$ as an alternative route to $\mathsf{AD}_\mathbb{R}$-strength (Trang, Woodin, Neeman's long-game machinery).
- **Descriptive inner model theory schools.** Berkeley/UC Irvine (Steel, Martin lineage), Münster (Schindler, core model induction), Vienna/Wien logic group, Carnegie Mellon.

## 8. Future Work

- Prove the **Mouse Set Conjecture** at the $\mathsf{AD}_\mathbb{R}$ level: every real that is $\mathrm{OD}$ from a countable sequence of reals and ordinal-definable is in a mouse. This would unconditionalize the converse.
- Develop **generic iterability** for hod pairs whose strategies have hull condensation past $\mathsf{LSA}$, removing the branch-selection obstacle.
- Settle whether the derived-model hypothesis for $\mathsf{AD}_\mathbb{R}$ is optimal, or whether plain $\mathsf{AD}_\mathbb{R}$ is equiconsistent with something strictly weaker than "limit of Woodins that is a limit of ${<}\lambda$-strongs".
- Compute the exact strength of $\mathsf{AD}_\mathbb{R}+\text{“}\Theta$ is measurable$\text{”}$ and of "$\Theta$ is a limit of measurable cardinals in the Solovay sequence sense".
- Extract $\mathsf{AD}_\mathbb{R}$-strength lower bounds from purely combinatorial statements ($\mathsf{PFA}$, $\mathsf{MM}^{++}$, saturation of the nonstationary ideal), giving independent evidence for consistency.

## 9. Key References

- **[Foundational]** Jan Mycielski, Hugo Steinhaus. *A mathematical axiom contradicting the axiom of choice.* Bulletin de l'Académie Polonaise des Sciences 10, 1962.
- **[Foundational]** Robert M. Solovay. *The independence of DC from AD.* In: Cabal Seminar 76–77, Lecture Notes in Mathematics 689, Springer, 1978, pp. 171–183.
- **[Foundational]** Donald A. Martin, John R. Steel. *A proof of projective determinacy.* Journal of the American Mathematical Society 2(1), 1989, pp. 71–125.
- **[Foundational]** Alexander S. Kechris. *AD + UNIFORMIZATION is equivalent to half-$\mathsf{AD}_\mathbb{R}$.* Journal of Symbolic Logic 53(1), 1988, pp. 15–24.
- **[SOTA / Recent]** Grigor Sargsyan. *Hod Mice and the Mouse Set Conjecture.* Memoirs of the American Mathematical Society 236(1111), 2015.
- **[SOTA / Recent]** Grigor Sargsyan, Nam Trang. *The Largest Suslin Axiom.* Lecture Notes in Logic 56, Association for Symbolic Logic / Cambridge University Press, 2024.
- **[Survey]** John R. Steel. *The derived model theorem.* In: Logic Colloquium 2006, Lecture Notes in Logic 32, ASL/Cambridge University Press, 2009, pp. 280–327.
- **[Survey]** John R. Steel. *An outline of inner model theory.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 2010, pp. 1595–1684.
- **[Reference]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Reference]** Alexander S. Kechris, Benedikt Löwe, John R. Steel (eds.). *Games, Scales, and Suslin Cardinals: The Cabal Seminar, Volume I.* Lecture Notes in Logic 31, ASL/Cambridge University Press, 2008.

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathsf{AD}_\mathbb{R}$ implies uniformization — and the proof shows exactly why moves in $\mathbb{R}$, not in $\omega$, are needed.

Let $R \subseteq \mathbb{R}\times\mathbb{R}$ be arbitrary. Consider the length-2 game on reals $G_R$: I plays $x \in \mathbb{R}$, II answers $y \in \mathbb{R}$; **II wins** iff $\big(\exists z\, R(x,z) \to R(x,y)\big)$.

- *I has no winning strategy.* A strategy for I is just a real $x_0$. If $\exists z\,R(x_0,z)$, II answers such a $z$ and wins; if no such $z$ exists, the implication is vacuously true and II wins with any $y$. So every play by I is answerable.
- By $\mathsf{AD}_\mathbb{R}$ (a clopen, hence trivially reducible, length-2 game on $\mathbb{R}$), II has a winning strategy $\tau : \mathbb{R} \to \mathbb{R}$.
- Set $f(x) = \tau(x)$ for $x \in \mathrm{dom}(R) := \{x : \exists z\,R(x,z)\}$. By the winning condition, $R(x,f(x))$ for all such $x$. So $f$ uniformizes $R$. $\square$

**Why $\mathsf{AD}$ cannot do this.** The same argument with moves in $\omega$ produces only a uniformizing function on a *countable* move set. Under $\mathsf{AD}$ alone, uniformization holds for $\Sigma^1_2$-like pointclasses by the Third Periodicity Theorem, which needs the payoff set to be **Suslin** (to build a scale and hence a definable strategy). For a set $A$ past the largest Suslin cardinal, no scale exists and no strategy can be extracted — matching Woodin's theorem that under $\mathsf{AD}^+$, $\mathsf{AD}_\mathbb{R}$ is *equivalent* to "every set of reals is Suslin".

**Solovay's measure, concretely.** Assume $\mathsf{AD}_\mathbb{R}+\mathsf{DC}$ and let $A \subseteq \mathcal{P}_{\omega_1}(\mathbb{R})$. Play $G^*_A$: I and II alternate reals $x_0,x_1,x_2,\dots$; let $\sigma = \{x_n : n<\omega\}$, a countable subset of $\mathbb{R}$; I wins iff $\sigma \in A$. Define
$$\mu(A) = 1 \iff \text{I has a winning strategy in } G^*_A .$$
$\mathsf{AD}_\mathbb{R}$ gives that exactly one of $A$, its complement has $\mu$-measure 1 (determinacy), a strategy-composition argument gives countable additivity, and a diagonal play gives normality and fineness (each $x \in \mathbb{R}$ is played at some stage, so $\{\sigma : x \in \sigma\}$ has measure 1). Solovay then shows the ultrapower by $\mu$ yields a model witnessing $\mathrm{Con}(\mathsf{AD}_\mathbb{R})$; since $\mathsf{AD}_\mathbb{R}$ alone cannot prove its own consistency, $\mathsf{DC}$ is unprovable from $\mathsf{AD}_\mathbb{R}$ — the first rung of the Solovay hierarchy in Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*