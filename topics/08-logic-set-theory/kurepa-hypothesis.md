---
id: 08-logic-set-theory/kurepa-hypothesis
title: "Kurepa Hypothesis"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kurepa Hypothesis

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/kurepa-hypothesis` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The **Kurepa Hypothesis** ($\mathsf{KH}$) asserts:

> There exists a tree $T$ of height $\omega_1$ all of whose levels are countable and which has at least $\aleph_2$ cofinal branches.

Such a $T$ is a **Kurepa tree**. Written compactly:

$$\mathsf{KH} \iff \exists T\ \big[\operatorname{ht}(T)=\omega_1 \ \wedge\ \forall \alpha<\omega_1\ |T_\alpha|\le\aleph_0 \ \wedge\ |[T]|\ge\aleph_2\big],$$

where $[T]$ is the set of branches of $T$ of order type $\omega_1$.

The problem as originally posed — decide $\mathsf{KH}$ from $\mathsf{ZFC}$ — is **settled negatively**: $\mathsf{KH}$ is independent of $\mathsf{ZFC}$, and its negation has exactly the consistency strength of one inaccessible cardinal. What remains open is the *generalized* problem: for which cardinals $\kappa$, and in combination with which cardinal-arithmetic hypotheses, is "there is no $\kappa$-Kurepa tree" consistent, and at what large-cardinal cost. A complete resolution means an equiconsistency for each $\kappa$ in the style of Silver's theorem at $\omega_1$.

*(Disambiguation: unrelated to "Kurepa's conjecture" in number theory, $\gcd(!n,n!)=2$ for $n>2$, by the same author.)*

## 2. Mathematical Foundations

**Trees.** A *tree* is a partial order $(T,<_T)$ such that $\operatorname{pred}_T(x)=\{y: y<_T x\}$ is well-ordered for each $x$. The *height* of $x$ is $\operatorname{ot}(\operatorname{pred}_T(x))$; the $\alpha$-th level is $T_\alpha=\{x:\operatorname{ht}(x)=\alpha\}$; $\operatorname{ht}(T)=\min\{\alpha: T_\alpha=\varnothing\}$. A *branch* is a maximal chain; it is *cofinal* if it meets every nonempty level. An *$\omega_1$-tree* has height $\omega_1$ and countable levels.

**The three classical $\omega_1$-tree dichotomies.** For an $\omega_1$-tree $T$:

- $T$ is **Aronszajn** if $|[T]|=0$ (exists in $\mathsf{ZFC}$; König's lemma fails at $\omega_1$).
- $T$ is **Suslin** if it has no uncountable chain and no uncountable antichain (independent of $\mathsf{ZFC}$).
- $T$ is **Kurepa** if $|[T]|\ge\aleph_2$.

In $\mathsf{ZFC}$ one always has $|[T]|\le 2^{\aleph_0}\cdot\aleph_1$ for *Suslin-like* restrictions but in general only $|[T]|\le 2^{\aleph_1}$; so $\mathsf{KH}$ is a statement that many branches are *realized*, not merely permitted.

**Kurepa families.** $\mathsf{KH}$ has a purely combinatorial equivalent: there is $\mathcal{F}\subseteq\mathcal{P}(\omega_1)$ with $|\mathcal{F}|\ge\aleph_2$ and

$$\forall \alpha<\omega_1:\quad |\mathcal{F}\!\restriction\!\alpha| = |\{A\cap\alpha : A\in\mathcal{F}\}| \le \aleph_0 .$$

The tree $T=\{A\cap\alpha : A\in\mathcal{F},\ \alpha<\omega_1\}$ ordered by end-extension is then Kurepa.

**Generalization.** For regular $\kappa$, a **$\kappa$-Kurepa tree** has height $\kappa$, levels of size $<\kappa$, and at least $\kappa^+$ cofinal branches. $\mathsf{KH}(\kappa)$ says one exists; $\mathsf{KH}=\mathsf{KH}(\omega_1)$.

**Principles used.** Jensen's $\diamondsuit^+$: a sequence $\langle \mathcal{A}_\alpha:\alpha<\omega_1\rangle$ with $\mathcal{A}_\alpha\subseteq\mathcal{P}(\alpha)$ countable such that for every $X\subseteq\omega_1$ there is a club $C\subseteq\omega_1$ with $X\cap\alpha\in\mathcal{A}_\alpha$ and $C\cap\alpha\in\mathcal{A}_\alpha$ for all $\alpha\in C$. Also the Lévy collapse $\operatorname{Coll}(\omega_1,{<}\kappa)$ with countable conditions, which is ${<}\omega_1$-closed and $\kappa$-c.c. when $\kappa$ is inaccessible.

## 3. History & State of the Art (SOTA)

- **1935.** Đuro Kurepa, in his Paris thesis *Ensembles ordonnés et ramifiés*, isolates ramified sets and asks whether a tree with countable levels and $\ge\aleph_2$ branches exists.
- **1960s.** Solovay observes $V=L\Rightarrow\mathsf{KH}$; Jensen isolates $\diamondsuit^+$ (which holds in $L$) and shows $\diamondsuit^+\Rightarrow\mathsf{KH}$. So $\mathsf{KH}$ is not refutable.
- **1966.** D. H. Stewart (Bristol M.Sc.) constructs a model of $\neg\mathsf{KH}$ from an inaccessible.
- **1971.** Jack Silver publishes the definitive result: forcing with $\operatorname{Coll}(\omega_1,{<}\kappa)$ over $L$ for $\kappa$ inaccessible gives $\mathsf{ZFC}+\mathsf{CH}+\neg\mathsf{KH}$; conversely $\neg\mathsf{KH}$ implies $\omega_2$ is inaccessible in $L$. **Equiconsistency:**

$$\operatorname{Con}(\mathsf{ZFC}+\neg\mathsf{KH}) \iff \operatorname{Con}(\mathsf{ZFC}+\exists\text{ inaccessible}).$$

- **1969.** Jensen–Kunen: for inaccessible $\kappa$, $\kappa$ is **ineffable** iff there is no $\kappa$-Kurepa tree. This converts the higher-$\kappa$ problem into a large-cardinal characterization at inaccessibles.
- **1971–72.** Jech's *Trees* systematizes the forcing constructions (adding a Kurepa tree by a ${<}\omega_1$-closed forcing).
- **1980s.** Todorčević (Handbook chapter): adding a single Cohen real adds a Kurepa tree — so $\neg\mathsf{KH}$ is fragile under mild forcing. Baumgartner/Todorčević: $\mathsf{PFA}$ (hence $\mathsf{MM}$) implies $\neg\mathsf{KH}$, consistent with $\mathsf{PFA}$'s large-cardinal strength.
- **2000s–2020s.** Focus shifts to $\mathsf{KH}(\kappa)$ for $\kappa=\omega_2$, $\kappa$ successor of a singular, and to interactions with the tree property, square principles and Prikry-type forcing.

## 4. Partial Results / Verified Cases

| Hypothesis | Verdict on $\mathsf{KH}$ | Source |
|---|---|---|
| $V=L$ (or $\diamondsuit^+$) | $\mathsf{KH}$ holds | Solovay; Jensen |
| $\mathsf{ZFC}+\mathsf{GCH}$ | undecided (both directions consistent) | Silver 1971 |
| $\mathsf{CH}$ | undecided; $\mathsf{CH}+\neg\mathsf{KH}$ consistent from an inaccessible | Silver 1971 |
| After adding one Cohen real | $\mathsf{KH}$ holds | Todorčević 1984 |
| $\mathsf{PFA}$, $\mathsf{MM}$ | $\neg\mathsf{KH}$ | Baumgartner 1984 |
| $\mathsf{MA}_{\omega_1}+2^{\aleph_0}=\aleph_2$ | undecided (compatible with both) | Silver; Jech |
| $\kappa$ inaccessible | no $\kappa$-Kurepa tree $\iff$ $\kappa$ ineffable | Jensen–Kunen 1969 |
| $\kappa$ ineffable, generic extension | $\neg\mathsf{KH}(\kappa)$ | Jensen–Kunen |
| $\neg\mathsf{KH}$ holds | $\omega_2$ inaccessible in $L$; $\omega_2^{L}<\omega_2$ | Silver 1971 |

Concrete parameter ranges where the answer is fully determined: (i) $\kappa=\omega_1$ — exact strength one inaccessible; (ii) $\kappa$ inaccessible — exact strength ineffability; (iii) $\kappa=\omega$ — no $\omega$-Kurepa trees, by König's lemma the tree has $\le 2^{\aleph_0}$ branches and finitely branching levels force $\le\aleph_0$; the statement is vacuous/false in $\mathsf{ZFC}$.

## 5. Principal Obstacles

- **Absoluteness ceiling.** Branches of an $\omega_1$-tree are added by any forcing that codes new subsets of $\omega_1$ with countable approximations. Cohen forcing already adds a Kurepa tree, so $\neg\mathsf{KH}$ is not preserved by even the tamest forcing. Any consistency proof for $\neg\mathsf{KH}$ at a new cardinal must be a *terminal* construction, not an iteration step one can absorb.
- **Fine structure forces $\mathsf{KH}$ upward.** In $L$ and in all currently known core models, $\diamondsuit^+_\kappa$ (or $\square_\kappa$ plus $\mathsf{GCH}$) holds at essentially every relevant $\kappa$, and each yields a $\kappa$-Kurepa tree. Killing Kurepa trees therefore demands destroying condensation, i.e. genuine large cardinals — this is the content of Silver's converse.
- **Collapse arguments do not iterate at $\omega_2$.** Silver's method works because $\operatorname{Coll}(\omega_1,{<}\kappa)$ is ${<}\omega_1$-closed, preserving $\mathsf{CH}$ and $\omega_1$. The analogue at $\omega_2$ requires a ${<}\omega_2$-closed collapse, which needs $\mathsf{CH}$ in the ground model to be $\omega_2$-c.c.-friendly, and the closure then reintroduces $\diamondsuit_{\omega_2}$-type sequences on the $\omega_2$ side. This tension is exactly why $\mathsf{CH}+\neg\mathsf{KH}(\omega_2)$ is hard.
- **No reflection tool at successors of singulars.** For $\kappa=\mu^+$ with $\mu$ singular, $\square_\mu$-type principles are near-unavoidable below large-cardinal thresholds (Jensen's covering lemma), and every known weak square yields a $\kappa$-Kurepa tree.

## 6. The Gap

Everything in Section 4 pins $\mathsf{KH}$ at $\omega_1$ and at inaccessibles. The gap is the *successor* case above $\omega_1$ under cardinal-arithmetic constraints:

1. **Is $\mathsf{CH}+$ "there is no $\omega_2$-Kurepa tree" consistent (relative to large cardinals)?** *(frontier — verify)* Without $\mathsf{CH}$ the collapse of an inaccessible above $\omega_2$ works; with $\mathsf{CH}$ the closure of the collapse manufactures branch-carrying structures at $\omega_2$.
2. **Exact strength of $\neg\mathsf{KH}(\mu^+)$ for $\mu$ singular strong limit.** Known upper bounds run through supercompactness (via Prikry-type forcing); no matching lower bound at the level of an ineffable-style characterization is known.
3. **Weak Kurepa trees.** The weak hypothesis ($\aleph_2$ branches replaced by "more branches than levels-size permits in a weaker sense") has different behaviour under $\mathsf{MA}$; its exact strength at $\omega_2$ is unsettled.

The technical step to cross: a forcing that is sufficiently closed to preserve $\mathsf{CH}$ yet destroys *all* $\aleph_2$-sized almost-disjoint families of $\omega_2$-approximations — no known iteration or collapse achieves both simultaneously.

## 7. Current Research (as of June 2026)

- **Prague school (Honzík, Stejskalová).** Systematic work on the coexistence of Kurepa trees with the tree property and with prescribed continuum functions; models where $\mathsf{KH}(\omega_2)$ fails while the tree property holds at $\omega_2$. *(frontier — verify)*
- **Bar-Ilan / Rinot group.** Constructions of higher Souslin and Kurepa trees from $\square$-like and $\diamondsuit$-like parametrized principles ($P(\kappa,\mu,\mathcal{R},\theta)$ proxy principle), aimed at ZFC-provable existence at successors of singulars. *(frontier — verify)*
- **$\Sigma$-Prikry framework (Poveda, Rinot, Sinapova).** Iteration schemes at singular cardinals that in principle allow killing trees at $\mu^+$ while preserving $\mathsf{GCH}$ below; application to $\neg\mathsf{KH}(\mu^+)$ is an active target. *(frontier — verify)*
- **Forcing axioms.** Continued analysis of which fragments of $\mathsf{PFA}$ suffice for $\neg\mathsf{KH}$; Rado's Conjecture and Chang-type two-cardinal transfer are being used as intermediate principles, following Silver's original link between $\mathsf{KH}$ and two-cardinal model theory.
- **Descriptive/definable variants.** Whether there is a $\Sigma^1_2$ or $L$-definable Kurepa tree in models of $\neg\diamondsuit^+$.

## 8. Future Work

- Prove or refute $\operatorname{Con}(\mathsf{CH}+\neg\mathsf{KH}(\omega_2))$; a positive answer likely needs a new species of ${<}\omega_2$-closed, $\omega_3$-c.c. collapse, or a Mitchell-style two-step forcing adapted from the tree-property literature.
- Find the ineffability analogue at successors: identify a combinatorial large-cardinal property $P(\kappa)$ with $\neg\mathsf{KH}(\kappa^+)\iff$ "$\kappa^+$ has $P$ in the core model".
- Extend Jensen–Kunen to *generic* ineffability, giving a uniform statement covering both $\omega_1$ (inaccessible in $L$) and inaccessible $\kappa$ (ineffable).
- Chart the exact relation between the tree property at $\kappa$ and $\neg\mathsf{KH}(\kappa)$; they are known to be independent of one another, but no model separates all four combinations at $\omega_2$ under $\mathsf{GCH}$.

## 9. Key References

- **[Foundational]** Đ. Kurepa. *Ensembles ordonnés et ramifiés.* Publications mathématiques de l'Université de Belgrade, 4 (1935), 1–138.
- **[Foundational]** J. Silver. *The independence of Kurepa's conjecture and two-cardinal conjectures in model theory.* In: Axiomatic Set Theory, Proceedings of Symposia in Pure Mathematics XIII, Part 1, American Mathematical Society, 1971, pp. 383–390.
- **[Foundational]** R. B. Jensen and K. Kunen. *Some combinatorial properties of $L$ and $V$.* Unpublished manuscript, 1969 (widely circulated; ineffability ⟺ no $\kappa$-Kurepa tree).
- **[Foundational]** T. Jech. *Trees.* The Journal of Symbolic Logic, 36 (1971), 1–14.
- **[Foundational]** D. H. Stewart. *The consistency of the Kurepa hypothesis.* M.Sc. thesis, University of Bristol, 1966.
- **[Survey]** S. Todorčević. *Trees and linearly ordered sets.* In: Handbook of Set-Theoretic Topology (K. Kunen and J. Vaughan, eds.), North-Holland, 1984, pp. 235–293.
- **[Survey]** K. Devlin. *Constructibility.* Perspectives in Mathematical Logic, Springer-Verlag, 1984.
- **[Reference]** T. Jech. *Set Theory, The Third Millennium Edition.* Springer Monographs in Mathematics, Springer, 2003 (Chapters 9, 15, 28).
- **[Reference]** K. Kunen. *Set Theory: An Introduction to Independence Proofs.* North-Holland, 1980.
- **[SOTA / Recent]** A. Rinot. *Higher Souslin trees and the GCH, revisited.* Advances in Mathematics, 311 (2017), 510–531.
- **[SOTA / Recent]** J. Baumgartner. *Applications of the Proper Forcing Axiom.* In: Handbook of Set-Theoretic Topology, North-Holland, 1984, pp. 913–959.

## 10. Worked Example / Concrete Special Case

**Claim.** $\diamondsuit^+\Rightarrow\mathsf{KH}$. (Hence $\mathsf{KH}$ holds in $L$.)

Fix a $\diamondsuit^+$-sequence $\langle\mathcal{A}_\alpha:\alpha<\omega_1\rangle$, each $\mathcal{A}_\alpha\subseteq\mathcal{P}(\alpha)$ countable.

**Step 1 — build the tree.** Put

$$T_\alpha=\{\,A : A\in\mathcal{A}_\alpha\,\},\qquad T=\bigcup_{\alpha<\omega_1}T_\alpha\times\{\alpha\},$$

ordered by $(A,\alpha)<_T(B,\beta)$ iff $\alpha<\beta$ and $A=B\cap\alpha$. Each $\operatorname{pred}_T$ is well-ordered by $\alpha$, so $T$ is a tree; $|T_\alpha|\le\aleph_0$ by hypothesis; $\operatorname{ht}(T)=\omega_1$ (add $\varnothing$ to each $\mathcal{A}_\alpha$ so no level is empty).

**Step 2 — many branches.** Let $X\subseteq\omega_1$. By $\diamondsuit^+$ there is a club $C_X$ with $X\cap\alpha\in\mathcal{A}_\alpha$ for all $\alpha\in C_X$. The set

$$b_X=\{(X\cap\alpha,\alpha):\alpha\in C_X\}$$

is a chain of order type $\omega_1$, cofinal in $T$ (as $C_X$ is unbounded). Extend $b_X$ to a maximal chain; it is a cofinal branch.

**Step 3 — counting.** If $X\ne Y$, pick $\gamma$ with $X\cap\gamma\ne Y\cap\gamma$; for all $\alpha\in C_X\cap C_Y$ above $\gamma$ we get $X\cap\alpha\ne Y\cap\alpha$, so $b_X\ne b_Y$. Hence

$$|[T]|\ \ge\ 2^{\aleph_1}\ \ge\ \aleph_2 .$$

$T$ is a Kurepa tree. $\square$

**Why $\aleph_2$ and not $\aleph_1$ is the right threshold.** In $\mathsf{ZFC}$ there are $\omega_1$-trees with exactly $\aleph_1$ cofinal branches — e.g. take the tree of all functions $f:\alpha\to\omega$ ($\alpha<\omega_1$) that are eventually $0$ off a finite set together with a fixed injection $e_\alpha:\alpha\to\omega$; the "canonical" branches indexed by $\alpha<\omega_1$ give $\aleph_1$ of them. So "$\ge\aleph_1$ branches" is a theorem, "$\ge\aleph_2$" is the independent statement, and the entire content of Silver's theorem is that pushing from $\aleph_1$ to $\aleph_2$ branches costs — in the negative direction — exactly one inaccessible cardinal.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*