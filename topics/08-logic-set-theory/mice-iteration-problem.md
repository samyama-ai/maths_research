---
id: 08-logic-set-theory/mice-iteration-problem
title: "Mice Iteration Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mice Iteration Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/mice-iteration-problem` · **Status:** open

## 1. Problem Statement / Conjecture

A *mouse* is a countably iterable fine-structural model $M = (J_\alpha^{\vec E}, \in, \vec E)$ built from a coherent sequence of extenders. Iterability — the existence of a winning strategy for the "good player" in the iteration game, choosing wellfounded branches through iteration trees — is the hypothesis that makes the whole theory work: comparison, condensation, the Dodd–Jensen lemma, and hence $\square$, $\diamondsuit$, and the fine-structural analysis of $\mathrm{HOD}$ all presuppose it.

**Iterability Conjecture (Steel).** Every countable premouse arising as a level of a $K^c$-construction is $(\omega_1,\omega_1+1)$-iterable. Equivalently, in the standard formulation: every countable *1-small* premouse $M$ satisfying $\Sigma_1$-soundness is $\omega_1+1$-iterable.

**The Mice Iteration Problem** is the family of open questions surrounding this:

1. **(Core Model Iterability Problem.)** Prove iterability for the levels of $K^c$ past the point where "1-small" fails — i.e. above a Woodin cardinal, and in particular at and beyond a superstrong cardinal.
2. **(Uniqueness.)** Identify the correct replacement for the *Unique Branches Hypothesis* (UBH), which is false for iteration trees on $V$ (Neeman–Steel 2006), yet whose analogue for countable mice is expected to hold.
3. **(Definability.)** Is the (unique) iteration strategy for a countable mouse definable over the mouse itself, or over its derived structures — the *self-iterability* and *strategy-mouse* questions?

A complete solution would produce, for every countable premouse in the relevant class, a canonical $\omega_1+1$-iteration strategy, provably in $\mathsf{ZFC}$ (plus the large-cardinal hypothesis needed to build the mouse at all).

## 2. Mathematical Foundations

**Extenders.** For $M \models \mathsf{ZFC}^-$ and $j: M \to N$ elementary with critical point $\kappa$, the $(\kappa,\lambda)$-extender derived from $j$ is
$$E = \{(a,X) : a \in [\lambda]^{<\omega},\ X \subseteq [\kappa]^{|a|},\ a \in j(X)\}.$$
$E$ codes $\mathrm{Ult}(M,E)$, whose elements are $[a,f]_E$ for $a \in [\lambda]^{<\omega}$, $f: [\kappa]^{|a|} \to M$, with
$$[a,f]_E \in [b,g]_E \iff \{u : f(u_a) \in g(u_b)\} \in E_{a\cup b}.$$
Write $\mathrm{crit}(E)=\kappa$, $\mathrm{lh}(E)=\lambda$, and $\nu(E)$ for the natural length (the sup of generators).

**Premice.** A *premouse* is $M=(J_\alpha^{\vec E},\in,\vec E, E_\alpha)$ where $\vec E$ is a *coherent* sequence in the sense of Mitchell–Steel: if $E_\beta \ne \emptyset$ then $\mathrm{Ult}(J_\beta^{\vec E \restriction \beta}, E_\beta)$ has extender sequence agreeing with $\vec E$ below $\mathrm{lh}(E_\beta)$ and is empty at $\mathrm{lh}(E_\beta)$. Fine structure attaches to each $M$ a projectum $\rho_n(M)$, standard parameter $p_n(M)$, and $n$-th core $\mathfrak{C}_n(M)$; $M$ is *sound* if $M = \mathrm{Hull}^M_{n+1}(\rho_{n+1}(M)\cup p_{n+1}(M))$.

**Iteration trees.** An iteration tree $\mathcal{T}$ on $M$ of length $\theta$ consists of a tree order $T$ on $\theta$, models $M_\xi^{\mathcal T}$, extenders $E_\xi \in \vec E^{M_\xi}$, and embeddings $i^{\mathcal T}_{\xi\eta}$, with
$$M^{\mathcal T}_{\xi+1} = \mathrm{Ult}_n(M^{*\mathcal T}_{\xi+1}, E_\xi), \qquad T\text{-pred}(\xi+1) = \text{least }\eta\text{ with } \mathrm{crit}(E_\xi) < \nu(E_\eta),$$
and direct limits at limit stages along $T$-branches. The tree is non-linear exactly because extenders *overlap*: $\mathrm{crit}(E_\xi)$ may be below $\nu(E_\eta)$ for $\eta < \xi - 1$.

$M$ is $(\alpha,\beta)$-*iterable* if player II wins the length-$\beta$ iteration game with $\alpha$ simultaneous trees: II must choose a cofinal wellfounded branch at each limit stage, and all models must be wellfounded.

**Common part and $Q$-structures.** For $\mathcal T$ of limit length $\lambda$, set
$$\delta(\mathcal T) = \sup_{\xi<\lambda}\mathrm{lh}(E_\xi), \qquad \mathcal M(\mathcal T) = \bigcup_{\xi<\lambda} M^{\mathcal T}_\xi \restriction \mathrm{lh}(E_\xi),$$
and for a branch $b$, let $Q(b,\mathcal T)$ be the shortest initial segment of $M_b^{\mathcal T}$ that either projects below $\delta(\mathcal T)$ or defines a failure of the Woodinness of $\delta(\mathcal T)$.

**Uniqueness Theorem (Martin–Steel).** If $b \ne c$ are distinct cofinal wellfounded branches of $\mathcal T$, then $\delta(\mathcal T)$ is a Woodin cardinal in $L(\mathcal M(\mathcal T))$ — indeed $Q(b,\mathcal T)$ and $Q(c,\mathcal T)$ cannot both exist. Hence: **when a $Q$-structure exists and is itself iterable, the branch is unique and identifiable.**

**UBH.** *Every iteration tree on $V$ of limit length has at most one cofinal wellfounded branch.* This is the naive strengthening; it is refutable (§3).

## 3. History & State of the Art (SOTA)

- **1970s.** Dodd and Jensen introduce the core model $K^{\mathrm{DJ}}$ below a measurable, with *linear* iterations; wellfoundedness follows from countable completeness of the measures (Gaifman, Kunen).
- **1994.** Martin and Steel, *Iteration trees* (JAMS), introduce non-linear trees to handle overlapping extenders, and prove the uniqueness theorem above. Mitchell and Steel, *Fine Structure and Iteration Trees* (LNL 3), give the $\vec E$-sequence framework and prove comparison **assuming** iterability.
- **1996.** Steel, *The Core Model Iterability Problem* (LNL 8), constructs $K$ below a Woodin cardinal, assuming a measurable cardinal, and isolates the iterability problem as the central obstruction. Levels of $K^c$ are shown iterable by a *countable-certificate* argument plus $Q$-structure branch identification.
- **1995–2002.** Neeman develops the $Q$-structure/genericity-iteration method: optimal determinacy proofs, and inner models at a Woodin limit of Woodins.
- **2001.** Andretta–Neeman–Steel: the *domestic* levels of $K^c$ are iterable — the current published ceiling of the "background-certified $\Rightarrow$ iterable" technique in the tame/domestic region.
- **2006.** Neeman–Steel, *Counterexamples to the unique and cofinal branches hypotheses* (JSL): UBH and CBH fail for trees on $V$ under large-cardinal hypotheses. This killed the hope of a soft general uniqueness theorem.
- **2009–2013.** Schindler–Steel prove *self-iterability of $L[\vec E]$*: $L[\vec E]$ can iterate its own countable elementary substructures. Jensen–Steel construct $K$ *without* a measurable cardinal.
- **2015.** Sargsyan, *Hod mice and the Mouse Set Conjecture*: iterability for hod mice in the region below $\mathsf{AD}_{\mathbb R} + \text{“}\Theta$ regular", via hod-pair strategy comparison.
- **2013–2021.** Schlutzenberg, and Steel's *normalizing iteration trees* programme, give the *full normalization* / positional-and-commuting strategy framework, which is the current engine for strategy comparison and iterability for stacks of trees.

## 4. Partial Results / Verified Cases

| Class | Status |
|---|---|
| Linear iterations of a single normal measure ($L[U]$) | **Solved** (Kunen 1970): all iterates wellfounded, all countable iterations. |
| Premice below a Woodin ("1-small", $\Sigma_1^2$-correct levels) | **Solved**: $Q$-structures exist and are $\delta$-small, so branches are unique and definable; $K$ exists (Steel 1996; Jensen–Steel 2013). |
| Tame premice (no extender overlaps a Woodin of the model) | **Solved** for $K^c$-levels; $\mathrm{AD}^{L(\mathbb R)}$ from $\mathsf{ZFC}$ + tameness fails at $\omega$ Woodins. |
| Domestic levels of $K^c$ (no superstrong-type overlap) | **Solved** (Andretta–Neeman–Steel 2001). |
| Countable premice with $\omega$ Woodin cardinals, $M_n^\sharp$ | **Solved** for each fixed $n<\omega$: $M_n^\sharp$ exists and is $\omega_1+1$-iterable from $\boldsymbol\Pi^1_n$-determinacy (Neeman, Woodin). |
| Hod mice below $\mathsf{AD}_{\mathbb R}+\text{“}\Theta$ regular" | **Solved** (Sargsyan 2015; Sargsyan–Trang for the Largest Suslin Axiom region). |
| Stacks of normal trees, given a normal strategy with hull condensation | **Solved** (Schlutzenberg 2021; Steel's normalization). |
| Levels of $K^c$ at/above a superstrong cardinal | **Open.** |
| UBH for trees on $V$ | **Refuted** (Neeman–Steel 2006). |

## 5. Principal Obstacles

- **Loss of $Q$-structures.** The whole branch-identification technology rests on: at a limit stage, $\delta(\mathcal T)$ is *not* Woodin in the right model, so a $Q$-structure exists and pins down $b$ uniquely. Past a Woodin cardinal in the model, $\delta(\mathcal T)$ *is* Woodin in $\mathcal M(\mathcal T)$-based models, $Q$ vanishes, and there is no first-order way to see which branch to take.
- **Non-tame overlaps.** When an extender on the sequence overlaps a Woodin cardinal of the model, the tree order becomes wildly non-linear: $T$-predecessors can drop back arbitrarily far, causing *drops in degree/model*, which destroy the elementarity needed for the Dodd–Jensen lemma.
- **UBH is false.** Neeman–Steel produce trees on $V$ with two cofinal wellfounded branches. So no purely combinatorial "there is at most one branch" argument can be the answer; the strategy must be *chosen*, not discovered.
- **Countable-completeness certificates run out.** For $K^c$ built with background extenders, wellfoundedness of a branch is shown by embedding a countable tree into $V$ and using countable completeness. Above a superstrong, the background condition (Jensen-style or Mitchell–Steel-style) cannot certify the required extenders while keeping the sequence coherent — this is exactly the *iterability at superstrong* barrier.
- **Circularity with determinacy.** Iterability for $M_n^\sharp$ is equivalent (Woodin, Neeman) to $\boldsymbol\Pi^1_n$-determinacy; so proving iterability outright is at least as hard as proving determinacy at the corresponding level, and beyond $L(\mathbb R)$ this becomes the core-model-induction bottleneck.

## 6. The Gap

Proven: for premice where every limit-length tree admits a $Q$-structure that is itself iterable by induction, branch selection is *canonical and definable* — this covers everything up to and including the tame/domestic region, and (with determinacy input) the $M_n$ hierarchy and hod mice below $\mathsf{AD}_{\mathbb R}+\text{“}\Theta$ regular".

Sought: a branch-selection rule at limit stages when $\delta(\mathcal T)$ *is* Woodin in every candidate $Q$-level. The exact step to be crossed:

> Given a countable premouse $M$ with a superstrong (or long) extender on its sequence and a tree $\mathcal T$ on $M$ of limit length with $\mathcal M(\mathcal T) \models$ "$\delta(\mathcal T)$ is Woodin", specify a cofinal wellfounded branch $b$, uniformly in $\mathcal T$, such that the resulting strategy has *hull condensation* and *normalizes well*.

Everything below this line is theorem; everything above is conjecture.

## 7. Current Research (as of June 2026)

- **Steel's normalization programme** (Berkeley/Münster): *full normalization*, "least branch hod pairs", and the conjecture that strategies with hull condensation admit strategy-comparison. Steel's monograph *A Comparison Process for Mouse Pairs* (LNL, 2022) is the reference text.
- **Schlutzenberg (Münster/Vienna):** definability of the extender sequence over $L[\vec E]$, self-iterability, iterability for transfinite stacks, and the study of *long extenders* / rank-to-rank premice — the most direct assault on the superstrong barrier. *(frontier — verify)*
- **Sargsyan and Trang (Rényi Institute / UNT):** core model induction past the Largest Suslin Axiom; hod mice with strategies indexed on the sequence.
- **Jensen-style $\lambda$-indexing school (Bonn/Münster):** Jensen's "stacking mice" and $\Sigma^*$-fine structure as an alternative route to iterability, avoiding some Mitchell–Steel indexing pathologies.
- **Larson, Neeman, Woodin:** the interaction of iterability with $\mathsf{AD}^+$, the Mouse Set Conjecture, and the ultimate-$L$ programme, where iterability of the hoped-for $\mathrm{Ultimate}\text{-}L$ premice at supercompact level is the key unproven hypothesis. *(frontier — verify)*

## 8. Future Work

- Prove the **Iterability Conjecture for $K^c$ at a superstrong cardinal**, or produce a $\mathsf{ZFC}$-provable counterexample tree with no wellfounded branch.
- Isolate the correct **weakening of UBH** for countable trees on mice ("unique branches with $Q$-structures relative to a fixed strategy"), and show it is consistent with the Neeman–Steel counterexamples.
- Establish **strategy comparison** for least-branch hod pairs in full generality; Steel conjectures this yields a fine-structural model of "there is a supercompact".
- Push **core model induction** past $\mathsf{AD}_{\mathbb R}+\text{“}\Theta$ regular" by constructing the required hod mice and verifying their iterability.
- Settle whether the iteration strategy of a countable mouse is **definable over the mouse's derived model**, generalizing Schindler–Steel self-iterability.

## 9. Key References

- **[Foundational]** Donald A. Martin and John R. Steel. *Iteration trees.* Journal of the American Mathematical Society 7 (1994), 1–73.
- **[Foundational]** William J. Mitchell and John R. Steel. *Fine Structure and Iteration Trees.* Lecture Notes in Logic 3, Springer, 1994.
- **[Foundational]** John R. Steel. *The Core Model Iterability Problem.* Lecture Notes in Logic 8, Springer, 1996.
- **[Foundational]** A. J. Dodd and Ronald B. Jensen. *The core model.* Annals of Mathematical Logic 20 (1981), 43–75.
- **[SOTA]** Itay Neeman and John R. Steel. *Counterexamples to the unique and cofinal branches hypotheses.* Journal of Symbolic Logic 71 (2006), 977–988.
- **[SOTA]** Alessandro Andretta, Itay Neeman, John R. Steel. *The domestic levels of $K^c$ are iterable.* Israel Journal of Mathematics 125 (2001), 157–201.
- **[SOTA]** Ralf Schindler and John R. Steel. *The self-iterability of $L[E]$.* Journal of Symbolic Logic 74 (2009), 751–779.
- **[SOTA]** Ronald B. Jensen and John R. Steel. *$K$ without the measurable.* Journal of Symbolic Logic 78 (2013), 708–734.
- **[SOTA]** Grigor Sargsyan. *Hod Mice and the Mouse Set Conjecture.* Memoirs of the American Mathematical Society 236, no. 1111, 2015.
- **[SOTA]** Farmer Schlutzenberg. *Iterability for (transfinite) stacks.* Journal of Mathematical Logic 21 (2021), 2150008.
- **[SOTA]** John R. Steel. *A Comparison Process for Mouse Pairs.* Lecture Notes in Logic 51, Cambridge University Press, 2022.
- **[Survey]** John R. Steel. *An outline of inner model theory.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 2010, 1595–1684.
- **[Survey]** Itay Neeman. *Determinacy in $L(\mathbb R)$.* In: Handbook of Set Theory, Springer, 2010, 1877–1950.

## 10. Worked Example / Concrete Special Case

**(a) The solved case: linear iteration of one measure.** Let $M_0 = L[U]$, $U$ a normal measure on $\kappa_0$. Define $M_{\alpha+1} = \mathrm{Ult}(M_\alpha, U_\alpha)$ where $U_\alpha = i_{0\alpha}(U)$, and take direct limits at limits. Set $\kappa_\alpha = i_{0\alpha}(\kappa_0)$.

Wellfoundedness at a limit $\lambda$: suppose $x_n \in M_\lambda$ with $x_{n+1} \mathbin{\in} x_n$, say $x_n = i_{\alpha_n \lambda}([a_n, f_n])$. Countable completeness of $U$ gives an order-preserving $\sigma: \{\kappa_{\alpha_n}\} \to \kappa_0$ with $\sigma``a_n \in \bigcap$ of the relevant measure-one sets, producing an infinite $\in$-descending sequence in $M_0$ — contradiction. So $L[U]$ is fully iterable, and Kunen's comparison shows $\{\kappa_\alpha\}$ is a club class of indiscernibles; any two such mice compare after $< \max(|M_0|,|M_1|)^+$ steps. **No branch choice ever arises**: the tree order is a linear order.

**(b) Where the problem starts.** Now let $M$ have two extenders $E_0, E_1 \in \vec E^M$ with
$$\mathrm{crit}(E_0) = \kappa_0 < \mathrm{crit}(E_1) = \kappa_1 < \nu(E_0) < \mathrm{lh}(E_0) < \mathrm{lh}(E_1).$$
$E_1$ *overlaps* $E_0$. Build $\mathcal T$: $M_1 = \mathrm{Ult}(M_0,E_0)$. To use $E_1' = E_1^{M_1}$ next we must apply it to the least $M_\eta$ with $\mathrm{crit}(E_1') < \nu(E_\eta)$. Since $\mathrm{crit}(E_1)<\nu(E_0)$, the rule gives $T\text{-pred}(2)=0$:
$$M_2 = \mathrm{Ult}(M_0, E_1'), \qquad 0 \mathbin{T} 2, \quad 1 \not\mathbin{T} 2 .$$
The tree order is now $\{0T1, 0T2\}$ — genuinely branching. Continue alternating: extenders with small critical points applied low, extenders with large critical points applied high, giving a length-$\omega$ tree with two infinite branches
$$b = \{0,2,4,\dots\}, \qquad c = \{0,1,3,5,\dots\}.$$
At stage $\omega$ the iterator must pick one. Compute $\delta(\mathcal T)=\sup_n \mathrm{lh}(E_n)$ and $\mathcal M(\mathcal T)=\bigcup_n M_n\restriction \mathrm{lh}(E_n)$.

- If $\mathcal M(\mathcal T) \models$ "$\delta(\mathcal T)$ is **not** Woodin", let $Q$ be the least level of $M_b^{\mathcal T}$ past $\mathcal M(\mathcal T)$ defining a failure of Woodinness via some $A \subseteq \delta(\mathcal T)$. By Martin–Steel, $Q(c,\mathcal T)$ then cannot exist, so $b$ is the **unique** branch with a $Q$-structure. The strategy is: *choose the branch $b$ such that $Q(b,\mathcal T)$ exists and is iterable.* This is $\Pi^1_1$-definable from $\mathcal T$ in the 1-small case, and is exactly Steel's $K^c$-iterability argument.
- If instead $\mathcal M(\mathcal T)\models$ "$\delta(\mathcal T)$ is Woodin" — which happens precisely once $M$ has a Woodin cardinal below the relevant extenders — then $Q(b,\mathcal T)$ and $Q(c,\mathcal T)$ are both undefined, both branches may be wellfounded, and nothing in $\mathcal M(\mathcal T)$ distinguishes them.

Case (b), second bullet, iterated up through superstrong extenders, *is* the Mice Iteration Problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*