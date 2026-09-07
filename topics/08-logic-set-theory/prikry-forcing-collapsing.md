---
id: 08-logic-set-theory/prikry-forcing-collapsing
title: "Prikry Forcing with Collapsing"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Prikry Forcing with Collapsing

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/prikry-forcing-collapsing` · **Status:** open

## 1. Problem Statement / Conjecture

Prikry-type forcings singularize a large cardinal $\kappa$ without adding bounded subsets. Interleaving Lévy collapses between the points of the Prikry sequence pushes $\kappa$ down to a *small* singular — typically $\aleph_\omega$ — carrying the large-cardinal combinatorics with it. The central open problem is how much of that combinatorics survives the collapses.

**Principal open question.** Is it consistent, relative to large cardinals, that
$$\aleph_\omega \text{ is a strong limit},\qquad 2^{\aleph_\omega} > \aleph_{\omega+1},\qquad \text{and the tree property holds at } \aleph_{\omega+1}?$$

Equivalently: can a Prikry-type forcing with interleaved collapses make the singular cardinal hypothesis (SCH) fail at $\aleph_\omega$ while there is no $\aleph_{\omega+1}$-Aronszajn tree?

**Secondary questions of the same family.**
1. Can failure of SCH at $\aleph_\omega$ be forced together with *stationary reflection* at $\aleph_{\omega+1}$?
2. Is failure of SCH at $\aleph_\omega$ consistent with the failure of the approachability property $\mathrm{AP}_{\aleph_\omega}$?
3. Can $2^{\aleph_\omega} = \aleph_{\omega+2}$ be forced with a Prikry-with-collapses construction from an optimal hypothesis (a cardinal $\kappa$ with $o(\kappa) = \kappa^{++}$) rather than from supercompactness?

A complete solution is a model of ZFC (from a consistent large-cardinal hypothesis) satisfying the configuration, or a ZFC theorem — plausibly from PCF theory — showing the configuration is impossible.

## 2. Mathematical Foundations

**Prikry forcing.** Let $U$ be a normal ultrafilter on a measurable $\kappa$. Conditions are pairs $(s, A)$ with $s \in [\kappa]^{<\omega}$, $A \in U$, $\max(s) < \min(A)$; $(t,B) \le (s,A)$ iff $t \sqsupseteq s$, $B \subseteq A$, $t \setminus s \subseteq A$. The key structural fact is the **Prikry property**: for every condition $(s,A)$ and every sentence $\varphi$ of the forcing language there is $B \subseteq A$, $B \in U$, with $(s,B)$ deciding $\varphi$. With the $\kappa^+$-chain condition this gives:

$$\mathbb{P}_U \text{ adds no bounded subsets of } \kappa, \text{ preserves all cardinals, and } \mathrm{cf}(\kappa)^{V[G]} = \omega .$$

**Interleaved collapses.** A condition of a *Prikry forcing with collapses* has the form
$$p = \langle \kappa_1, c_1, \ldots, \kappa_n, c_n, A, F \rangle,$$
where $\langle \kappa_1 < \cdots < \kappa_n \rangle$ is the stem, $c_i \in \mathrm{Col}(\kappa_{i-1}^{+\alpha}, <\kappa_i)$ is a collapsing condition below $\kappa_i$, $A$ is a large set (measure one for $U$, or for a coherent sequence of extenders/supercompactness measures), and $F$ is a function assigning to each $\nu \in A$ a collapsing condition in $\mathrm{Col}(\kappa_n^{+\alpha}, <\nu)$. Direct extension shrinks $A$ and strengthens $c_i, F$; end extension appends a new pair $(\nu, F(\nu))$.

If each $\kappa_{n}^{+\alpha}$ is collapsed to be a fixed small ordinal-indexed successor of $\kappa_{n-1}$, then in the extension $\kappa_n = \aleph_{\alpha \cdot n}$ and $\kappa = \sup_n \kappa_n = \aleph_\omega$.

**Guiding generics.** For the quotient analysis one needs, inside the target model $M = \mathrm{Ult}(V,U)$, a filter $H$ that is $M$-generic for $\mathrm{Col}(\kappa^{+\alpha}, <j(\kappa))^M$ and lies in $V$. Existence of such $H$ is the technical crux; it is what forces extra hypotheses ($2^\kappa = \kappa^+$, or supercompactness, or a $\kappa^{++}$-closed guiding generic on an extender).

**Relevant combinatorics.** $\mathrm{SCH}$ at $\aleph_\omega$: if $\aleph_\omega$ is strong limit then $2^{\aleph_\omega} = \aleph_{\omega+1}$. **Tree property** $\mathrm{TP}(\lambda)$: every tree of height $\lambda$ with levels of size $<\lambda$ has a cofinal branch. **Approachability** $\mathrm{AP}_\mu$: $\mu^+ \in I[\mu^+]$. **Very good scale**: a scale $\langle f_\alpha : \alpha < \mu^+\rangle$ in $\prod_n \mu_n$ with a club of $\delta$ on which it is exactly (not just eventually) increasing. Shelah's PCF bound $2^{\aleph_\omega} < \aleph_{\omega_4}$ (for $\aleph_\omega$ strong limit) constrains all such constructions.

## 3. History & State of the Art (SOTA)

- **1970.** Prikry introduces the forcing in *Changing measurable into accessible cardinals*.
- **1977.** Magidor's two papers on the singular cardinal problem give the first models where $\mathrm{SCH}$ fails at $\aleph_\omega$, using supercompactness and Prikry-type forcing with interleaved collapses; Magidor also shows $\mathrm{GCH}$ can first fail at $\aleph_\omega$.
- **1989.** Gitik forces $\neg\mathrm{SCH}$ from $o(\kappa) = \kappa^{++}$, matching the Gitik–Mitchell lower bound; this is optimal for a measurable, but the *collapsed* $\aleph_\omega$ version costs more.
- **1991.** Foreman–Woodin: GCH can fail everywhere, via a Prikry-style analysis over a supercompact.
- **1998.** Cummings–Foreman: the tree property at every $\aleph_n$, $2 \le n < \omega$ — the ancestor of all "tree property at small cardinals" work.
- **2008.** Gitik–Sharon: diagonal supercompact Prikry forcing with collapses gives $\neg\mathrm{SCH}$ at $\aleph_{\omega^2}$ together with the failure of approachability, and (after collapsing) at $\aleph_\omega$; they also produce a very good scale, an obstruction to the tree property.
- **2009–2014.** Neeman gets the tree property at $\aleph_{\omega+1}$ with $\aleph_\omega$ strong limit *and* SCH holding; Sinapova and Sinapova–Unger get the tree property at $\aleph_{\omega^2+1}$ and at $\aleph_{\omega+1}$ with $\neg\mathrm{SCH}$ at uncountable cofinality.
- **2021–2024.** Poveda–Rinot–Sinapova isolate the **$\Sigma$-Prikry** axiom framework, giving a general iteration theorem for Prikry-type forcings with collapses and reaching $\aleph_\omega$ in a modular way.

## 4. Partial Results / Verified Cases

| Configuration | Status | Source |
|---|---|---|
| $\neg\mathrm{SCH}$ at $\aleph_\omega$, $\aleph_\omega$ strong limit | Consistent from a supercompact | Magidor 1977 |
| $\neg\mathrm{SCH}$ at a measurable-turned-singular $\kappa$ | Consistent from $o(\kappa)=\kappa^{++}$ (optimal) | Gitik 1989 |
| $\neg\mathrm{SCH}$ at $\aleph_{\omega^2}$ $+$ $\neg\mathrm{AP}$ | Consistent from a supercompact | Gitik–Sharon 2008 |
| $\mathrm{TP}(\aleph_{\omega+1})$, $\aleph_\omega$ strong limit, SCH **holds** | Consistent | Neeman 2009 |
| $\mathrm{TP}(\kappa^+)$ with $\neg\mathrm{SCH}$, $\mathrm{cf}(\kappa)=\omega$, $\kappa$ *not* $\aleph_\omega$ | Consistent | Sinapova 2012 |
| $\mathrm{TP}(\aleph_{\omega^2+1})$ | Consistent | Sinapova–Unger 2014 |
| $\neg\mathrm{SCH}$ at $\aleph_\omega$ $+$ stationary reflection at $\aleph_{\omega+1}$ | Consistent (large hypotheses) | Ben-Neria–Hayut–Unger |
| $\neg\mathrm{SCH}$ at $\aleph_\omega$ $+$ $\mathrm{TP}(\aleph_{\omega+1})$ | **Open** | — |

So the two ingredients are each available at $\aleph_\omega$, and available *together* at every singular of countable cofinality that is a limit of large cardinals in the ground model but is not made equal to $\aleph_\omega$. The value $\aleph_\omega$ — i.e. the presence of the collapses — is precisely what is missing.

## 5. Principal Obstacles

- **Guiding generics restrict the large sets.** To get the Prikry property with collapses one must choose, coherently along the measure sequence, generic filters for collapses computed in ultrapowers. Building them in $V$ needs $2^\kappa = \kappa^+$ locally or extra closure, which conflicts with the very $\neg\mathrm{SCH}$ one is trying to force. Extender-based versions replace ultrafilters with extenders, but then the ultrapowers are not closed enough to run the branch-counting arguments.
- **Very good scales appear automatically.** The Gitik–Sharon construction yields a very good scale at the target cardinal. A very good scale on $\aleph_\omega$ implies $\square^*_{\aleph_\omega}$-like approachability and yields a special $\aleph_{\omega+1}$-Aronszajn tree — directly contradicting $\mathrm{TP}(\aleph_{\omega+1})$. Removing the scale requires the collapses to be arranged so that the generic sequence is not "exact" on a club, which no known collapse pattern achieves at $\aleph_\omega$.
- **Branch-preservation lemmas need closure the quotient lacks.** Proofs of the tree property factor the forcing as $\mathbb{Q} * \dot{\mathbb{R}}$ with $\mathbb{Q}$ of small size and $\dot{\mathbb{R}}$ highly closed, then apply a "$\kappa^+$-cc $\times$ closed adds no branch" lemma. Interleaved collapses destroy the closure of the tail: the quotient is a full-support-like product of Lévy collapses whose lengths depend on the generic sequence, so it is neither $\kappa$-closed nor of size $<\kappa$.
- **Optimality gaps.** The known consistency strength for $\neg\mathrm{SCH}$ at $\aleph_\omega$ with collapses is a supercompact, far above the Gitik–Mitchell $o(\kappa)=\kappa^{++}$ bound that suffices without collapses. There is no known inner-model argument raising the lower bound to match.

## 6. The Gap

Everything proved lives at singulars that are large cardinal limits, or at $\aleph_\omega$ with SCH intact. The gap is a single interaction: the collapses that make $\kappa = \aleph_\omega$ and the measure-theoretic apparatus that makes $2^\kappa$ large together generate a very good scale, and a very good scale kills the tree property. The precise step needed is a Prikry-type forcing with collapses whose generic singularizing sequence carries **no very good scale** on the resulting $\aleph_\omega$ — equivalently, a collapse scheme compatible with $\neg\mathrm{AP}_{\aleph_\omega}$ *and* with the branch-preservation factorization. Alternatively, a ZFC theorem showing that any $\aleph_\omega$ obtained as a Prikry-type limit with collapses and $2^{\aleph_\omega} > \aleph_{\omega+1}$ must carry an $\aleph_{\omega+1}$-Aronszajn tree.

## 7. Current Research (as of June 2026)

- **$\Sigma$-Prikry programme** (Poveda, Rinot, Sinapova; Bar-Ilan / Jerusalem / UIC). The axioms isolate exactly the class of Prikry-type posets closed under the relevant iteration, and the third paper in the series descends to $\aleph_\omega$, killing prescribed weak-square-like objects while preserving $\neg\mathrm{SCH}$. This is currently the most flexible machinery for the problem. *(frontier — verify: extensions handling the full tree property.)*
- **Extender-based Prikry with collapses** (Gitik, Merimovich). Aims at $\neg\mathrm{SCH}$ at $\aleph_\omega$ from hypotheses near $o(\kappa)=\kappa^{++}$; Merimovich's supercompact extender-based framework is the main tool.
- **Reflection versus trees** (Ben-Neria, Hayut, Unger, Levine). Stationary reflection at $\aleph_{\omega+1}$ with $\neg\mathrm{SCH}$ is known; the analogous tree-property statement resists the same method because reflection is a $\Pi^1_1$ statement about stationary sets while branches require closure.
- **Consistency-strength side** (Gitik, Sharon; inner model theorists). Attempts to show supercompactness is *not* needed for the collapsed version.

## 8. Future Work

- Design a collapse scheme in which the interleaved posets are indexed so that the resulting scale is *good but not very good*, following the Gitik–Sharon $\neg\mathrm{AP}$ template but at $\aleph_\omega$.
- Prove a branch-preservation lemma for quotients of Prikry-with-collapses forcings that uses the Prikry property in place of closure — a "Prikry-property branch lemma".
- Extend Sinapova's $\aleph_{\omega^2+1}$ argument by a final collapse of $\aleph_{\omega^2}$ to $\aleph_\omega$, tracking which trees survive; the obstruction is that the final collapse is not $\aleph_{\omega^2}$-distributive.
- Settle whether $\neg\mathrm{SCH}$ at $\aleph_\omega$ from $o(\kappa) = \kappa^{++}$ alone is consistent, isolating the exact cost of the collapses.

## 9. Key References

- **[Foundational]** K. Prikry. *Changing measurable into accessible cardinals.* Dissertationes Mathematicae 68, 1970.
- **[Foundational]** M. Magidor. *On the singular cardinals problem I.* Israel Journal of Mathematics 28, 1–31, 1977. **and** *On the singular cardinals problem II.* Annals of Mathematics 106, 517–547, 1977.
- **[Foundational]** M. Gitik. *The negation of the singular cardinal hypothesis from $o(\kappa)=\kappa^{++}$.* Annals of Pure and Applied Logic 43, 209–234, 1989.
- **[Survey]** M. Gitik. *Prikry-type forcings.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 1351–1447, 2010.
- **[Survey]** J. Cummings. *Iterated forcing and elementary embeddings.* In: Handbook of Set Theory, Springer, 775–883, 2010.
- **[SOTA]** M. Gitik, A. Sharon. *On SCH and the approachability property.* Proceedings of the American Mathematical Society 136, 311–320, 2008.
- **[SOTA]** I. Neeman. *Aronszajn trees and failure of the singular cardinal hypothesis.* Journal of Mathematical Logic 9, 139–157, 2009.
- **[SOTA]** D. Sinapova. *The tree property at $\aleph_{\omega+1}$.* Journal of Symbolic Logic 77, 279–290, 2012.
- **[SOTA]** D. Sinapova, S. Unger. *The tree property at $\aleph_{\omega^2+1}$.* Journal of Symbolic Logic 79, 429–443, 2014.
- **[SOTA]** A. Poveda, A. Rinot, D. Sinapova. *Sigma-Prikry forcing I: The axioms.* Canadian Journal of Mathematics 73, 1205–1238, 2021; *II: Iteration scheme.* Journal of Mathematical Logic 22, 2022.
- **[Foundational]** M. Foreman, W. H. Woodin. *The generalized continuum hypothesis can fail everywhere.* Annals of Mathematics 133, 1–35, 1991.
- **[Foundational]** J. Cummings, M. Foreman. *The tree property.* Advances in Mathematics 133, 1–32, 1998.
- **[Background]** S. Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994.

## 10. Worked Example / Concrete Special Case

**Goal.** Build the guiding generic that makes a one-step Prikry-with-collapse work, and see how $\kappa$ becomes $\aleph_\omega$.

Assume $\kappa$ is measurable, $\mathrm{GCH}$ holds, $U$ is a normal ultrafilter on $\kappa$, and $j : V \to M = \mathrm{Ult}(V,U)$ with $M^\kappa \subseteq M$.

*Step 1 — count the dense sets.* Let $\mathbb{C} = \mathrm{Col}(\kappa^{+}, <j(\kappa))^M$. Every element of $M$ is $j(f)(\kappa)$ for some $f : \kappa \to V$. So the dense subsets of $\mathbb{C}$ lying in $M$ are indexed by functions $f : \kappa \to V_{\kappa+2}$, and
$$|\{ D \in M : D \text{ dense in } \mathbb{C}\}| \le |{}^{\kappa}V_{\kappa+2}| = 2^{\kappa^+} = \kappa^{++} .$$
Refining: dense sets can be taken to be represented by $f$ with $f(\alpha)$ a dense subset of $\mathrm{Col}(\alpha^+, <\kappa)$, of which there are $2^\kappa = \kappa^+$ many; so we need to meet only $\kappa^+$ dense sets.

*Step 2 — closure.* In $M$, $\mathbb{C}$ is $\kappa^{+}$-closed. Since $M^\kappa \subseteq M$, any descending $\kappa$-sequence from $V$ lies in $M$ and has a lower bound. Hence $\mathbb{C}$ is $\kappa^+$-closed *in $V$* for sequences of length $\le\kappa$; using $\mathrm{GCH}$ one enumerates the $\kappa^+$ dense sets as $\langle D_i : i < \kappa^+ \rangle$ and builds a descending chain $\langle p_i : i<\kappa^+\rangle$ with $p_{i+1} \in D_i$, taking lower bounds at limits of cofinality $\le \kappa$ (which exist by closure) — and at limits of cofinality $\kappa^+$ there are none, so one instead builds along a $\le\kappa$-cofinal tree of length $\kappa^+$ using the $\kappa^{+}$-closure of $\mathbb{C}$ in $M$ together with $M^\kappa\subseteq M$. The resulting filter $H \in V$ is $M$-generic for $\mathbb{C}$.

*Step 3 — the forcing.* Conditions are $\langle \kappa_1, c_1, \ldots, \kappa_n, c_n, A, F\rangle$ with $A \in U$, $c_i \in \mathrm{Col}(\kappa_{i-1}^{+}, <\kappa_i)$, and $F$ a function on $A$ with $F(\nu) \in \mathrm{Col}(\kappa_n^{+}, <\nu)$ and $[F]_U \in H$. The condition "$[F]_U \in H$" is exactly what a guiding generic supplies, and it is what makes the *diagonal intersection* argument for the Prikry property go through: given $\varphi$, for each $\nu \in A$ shrink to decide, then diagonalize; the collapse coordinates are handled because $H$ is a filter, so finitely many demands are compatible.

*Step 4 — the outcome.* Let $G$ give the sequence $\langle \kappa_n : n<\omega\rangle$. In $V[G]$, $\mathrm{Col}(\kappa_n^{+}, <\kappa_{n+1})$ has been forced, so $\kappa_{n+1} = \kappa_n^{++}$. With $\kappa_1$ arranged to be $\aleph_2$:
$$\kappa_n = \aleph_{2n}, \qquad \kappa = \sup_n \kappa_n = \aleph_\omega, \qquad \mathrm{cf}(\aleph_\omega) = \omega .$$
No bounded subsets of $\kappa$ beyond those added by the collapses appear, and $\kappa^+ = \aleph_{\omega+1}$ is preserved.

*Where the open problem bites.* In $V[G]$ the sequence $\langle \kappa_n \rangle$ generates a scale on $\prod_n \kappa_n^+$ that is *very good* on a club: for a club of $\delta < \aleph_{\omega+1}$ of uncountable cofinality, the scale is exactly increasing below $\delta$, because the collapses are indexed directly by the generic sequence. From that scale one reads off a special $\aleph_{\omega+1}$-Aronszajn tree. So this construction — and every published variant that reaches $\aleph_\omega$ with $2^{\aleph_\omega}>\aleph_{\omega+1}$ — refutes $\mathrm{TP}(\aleph_{\omega+1})$ in its own extension. Breaking that link is exactly the open problem of Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*