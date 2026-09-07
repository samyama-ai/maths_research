---
id: 08-logic-set-theory/extender-models-core-model-problem
title: "Extender Models Core Model Problem"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Extender Models Core Model Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/extender-models-core-model-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Core Model Problem for Extender Models asks whether, for any arbitrary large cardinal hypothesis $\Phi$ strictly weaker than "there exists a supercompact cardinal", one can construct a canonical, fine-structural inner model of set theory $K$ (the "core model") satisfying the following properties:
1. **Extender Model Structure:** $K$ is a class-sized premouse constructed from a coherent sequence of extenders, satisfying the Generalized Continuum Hypothesis (GCH) and the Axiom of Choice (ZFC).
2. **Absoluteness:** $K$ is highly absolute and canonically defined; it is invariant under set-forcing extensions of the universe $V$.
3. **Weak Covering:** If the universe $V$ does not contain an inner model satisfying $\Phi$, then $K$ closely approximates $V$ in terms of large cardinals and successors of singular cardinals. Specifically, it must satisfy the Weak Covering Lemma: for every singular strong limit cardinal $\gamma$, the successor of $\gamma$ in $K$ is the true successor in $V$, meaning $(\gamma^+)^K = \gamma^+$.

The overarching conjecture is that the classical extender sequence framework can be extended to construct $K$ for all large cardinal hypotheses up to, but necessarily excluding, supercompact cardinals, fully characterizing the inner model theory of the lower-to-middle large cardinal hierarchy.

## 2. Mathematical Foundations

The problem relies on Inner Model Theory and fine structure theory. The base model is Gödel's constructible universe $L = \bigcup_{\alpha \in \text{Ord}} L_\alpha$, which serves as the core model when $\Phi$ is the existence of a measurable cardinal. 

To capture cardinals stronger than measurable, one uses **extenders**. Let $j: V \to M$ be a non-trivial elementary embedding with critical point $\kappa$, where $M$ is transitive. An extender $E$ of length $\lambda$ derived from $j$ is a sequence of ultrafilters $E_a$ over $[\kappa]^{|a|}$ for every finite sequence $a \in [\lambda]^{<\omega}$, defined by:
$$X \in E_a \iff a \in j(X)$$
An extender $E$ allows for the extraction of highly localized elementary embeddings $j_E: M \to \text{Ult}(M, E)$ without requiring the full class-sized embedding $j$. 

A **premouse** is a structure $\mathcal{M} = \langle J_\alpha^{\vec{E}}, \in, \vec{E}, F \rangle$ where $J_\alpha^{\vec{E}}$ is an acceptable Jensen hierarchy equipped with a coherent sequence of extenders $\vec{E} = \langle E_\beta \mid \beta < \alpha \rangle$. Coherence means that if $E_\beta \neq \emptyset$, it is an extender over $J_\beta^{\vec{E}}$ and the ultrapower map $i_{E_\beta}$ applied to the sequence $\vec{E}$ agrees with $\vec{E}$ up to $\beta$. The predicate $F$ is a top extender (potentially empty). 

An **iteration tree** $\mathcal{T}$ of length $\theta$ on a premouse $\mathcal{M}_0$ is a tree ordering $<_T$ on $\theta$ with models $\mathcal{M}_\alpha$ at nodes and extenders $E_\alpha \in \mathcal{M}_\alpha$ attached to edges. At successor steps, $\mathcal{M}_{\alpha+1} = \text{Ult}(\mathcal{M}_\alpha^*, E_\alpha)$, where $\mathcal{M}_\alpha^*$ is an initial segment of some $\mathcal{M}_\beta$ for $\beta \le \alpha$. At limit stages $\lambda < \theta$, a branch $b$ through $<_T$ of length $\lambda$ is chosen to form the direct limit $\mathcal{M}_b$.

A premouse is **iterable** (and thus a **mouse**) if there exists an iteration strategy $\Sigma$ that always selects a branch $b$ at limit stages such that the resulting direct limit model $\mathcal{M}_b$ is well-founded. 

The **Core Model $K$** for a hypothesis $\Phi$ is traditionally constructed by first defining an intermediate backgrounded model $K^c$ (the "core model up to a thick class of cardinals") utilizing extenders that possess certificates in $V$, and then extracting $K$ as the union of all sound, co-iterable mice that project to $\omega$.

## 3. History & State of the Art (SOTA)

The history of the Core Model Problem is defined by the gradual ascent up the large cardinal hierarchy:
- **1938:** Kurt Gödel introduces $L$, establishing the blueprint for canonical inner models.
- **1981:** Anthony Dodd and Ronald Jensen construct the first true core model $K^{DJ}$ for the hypothesis "there is no inner model with a measurable cardinal", proving it satisfies the Weak Covering Lemma.
- **1984:** William Mitchell extends the theory to sequences of measures, reaching hypermeasurable cardinals ($o(\kappa) = \kappa^{++}$).
- **1989–1994:** Mitchell and John Steel introduce iteration trees, revolutionizing the field. They construct $K$ assuming there is no Woodin cardinal.
- **1996:** Steel publishes *The Core Model Iterability Problem*, resolving the iterability barriers for constructing $K$ below a Woodin limit of Woodin cardinals.
- **2013:** Jensen and Steel remove the necessity of assuming a background measurable cardinal in $V$ to construct $K$ below a Woodin cardinal.
- **Current SOTA:** Driven by the Core Model Induction (pioneered by Woodin, Ketchersid, Sargsyan, and Schindler), researchers have pushed extender models up to the LSA (Limit of Subcompact and Active) level. Translating between descriptive set theory (Axiom of Determinacy in $L(\mathbb{R})$) and extender sequences allows for the construction of Hod mice, which currently represent the bleeding edge of the classical extender model problem.

## 4. Partial Results / Verified Cases

The Extender Models Core Model Problem is solved completely for several initial segments of the large cardinal hierarchy:
- **Measurable Cardinals:** Proven by Dodd and Jensen (1981). If there is no inner model with a measurable cardinal, $K^{DJ}$ exists, is unique, and $(\gamma^+)^K = \gamma^+$ for all singular strong limits $\gamma$.
- **Strong Cardinals:** Proven by Mitchell (1984).
- **One Woodin Cardinal:** Proven by Mitchell and Steel (1994). The Weak Covering Lemma for this model was verified by Mitchell, Schimmerling, and Steel.
- **Finitely Many Woodin Cardinals:** Proven by Steel (1996). 
- **Woodin Limit of Woodin Cardinals:** Proven by Steel (1996) by developing the core model iterability theory utilizing background certificates.
- **Jensen-Steel Theorem (2013):** Proved the existence of the core model below a Woodin cardinal solely from the hypothesis that there is no inner model with a Woodin cardinal, eliminating the historically required assumption of a measurable cardinal $\Omega \in V$ used to "background" the extenders.
- **LSA Level:** Grigor Sargsyan (2015) successfully applied Hod mice to construct core models corresponding to models of AD+ up to the Limit of Subcompact and Active cardinals.

## 5. Principal Obstacles

The fundamental bottleneck preventing the resolution of the Core Model Problem up to a supercompact cardinal is the **Iterability Problem**, and specifically the failure of the **Unique Branch Hypothesis (UBH)**.

For $K$ to be a well-defined, canonical class model independent of arbitrary choices, the iteration trees generated during its construction must have *unique* well-founded branches at limit stages. If a tree $\mathcal{T}$ of limit length $\lambda$ has two distinct branches $b_1$ and $b_2$ that both yield well-founded direct limit models $\mathcal{M}_{b_1}$ and $\mathcal{M}_{b_2}$, the iteration strategy $\Sigma$ must arbitrarily choose between them. This destroys the absoluteness and canonicity of $K$.

Martin and Steel proved that UBH holds for iteration trees on models that only contain Woodin cardinals. However, for models containing superstrong cardinals, UBH is known to fail. Extenders overlapping in their critical sequences create non-linear iteration trees with complex drop-offs. When generating trees to compare mice at the superstrong level or above, the trees naturally branch into incompatible well-founded limits.

Furthermore, the **Background Certificate Barrier** limits the $K^c$ construction. To prove iterability of $K^c$, the traditional method requires the universe $V$ to contain large cardinals (like a measurable limit of Woodin cardinals) that "certify" the extenders added to the sequence. When attempting to construct $K$ just below a supercompact cardinal, the required background cardinals would exceed the target hypothesis itself, leading to circularity. The Core Model Induction attempts to bootstrap this without background cardinals, but the descriptive set-theoretic translation mechanisms become intractably complex beyond LSA.

## 6. The Gap

The precise mathematical boundary of the unknown lies between the LSA (Limit of Subcompact and Active) level and a fully supercompact cardinal. 

The gap requires determining whether a pure fine-structural sequence of extenders $\vec{E}$ is even mathematically capable of capturing the combinatorial strength of a supercompact embedding without triggering fatal UBH failures in the comparison lemma. Crossing this barrier requires either a fundamentally new iteration strategy that dynamically resolves UBH failures without breaking definability, or a proof that classical extender models inherently cannot exceed a superstrong cardinal, necessitating a transition to alternative frameworks like Woodin's Ultimate $L$.

## 7. Current Research (as of June 2026)

Active research operates along three primary vectors:
1. **The Core Model Induction:** Led by Sargsyan, Schindler, and Steel, this school attempts to bootstrap the existence of large cardinals from determinacy hypotheses. Current work focuses on extending the induction from LSA towards a subcompact cardinal.
2. **Hod Mice Theory:** Investigating the hereditarily ordinal definable (HOD) sets of models of AD+. These models bypass some iterability issues because their strategies are inherently definable from the determinacy of the background universe.
3. **Ultimate $L$ vs. Extender Models:** *(frontier — verify)* The tension between classical Mitchell-Steel extender models and Woodin's Ultimate $L$. Woodin conjectures that the classical Core Model Problem has a negative answer for supercompact cardinals—meaning no purely fine-structural extender sequence $K$ exists there—and that Ultimate $L$, which avoids sequences of extenders in favor of an abstract strategy $\Sigma$, is the only mathematically viable core model at that height.

## 8. Future Work

Leading mathematicians have outlined the following open pathways:
- **Local UBH Resolution:** Formulate and prove a restricted version of the Unique Branch Hypothesis that applies exclusively to the specific class of iteration trees that arise during the $K^c$ construction near a superstrong cardinal, bypassing the generalized UBH failures identified by Neeman and Woodin.
- **Covering at Subcompact:** Construct a fine-structural core model $K$ satisfying the Weak Covering Lemma specifically for the hypothesis "there is no inner model with a subcompact cardinal".
- **Equivalence Translators:** Establish a rigid, bidirectional translation theorem between the fine structure of Hod mice at the superstrong level and the corresponding AD+ models in $L(\mathbb{R})$, effectively extending Sargsyan's 2015 framework.

## 9. Key References

- **[Foundational]** Dodd, A. J., & Jensen, R. B. *The core model.* Annals of Mathematical Logic, 1981. 
- **[Foundational]** Mitchell, W. J., & Steel, J. R. *Fine Structure and Iteration Trees.* Lecture Notes in Logic 3. Springer, 1994.
- **[SOTA / Recent]** Steel, J. R. *The Core Model Iterability Problem.* Lecture Notes in Logic 8. Springer, 1996.
- **[SOTA / Recent]** Jensen, R. B., & Steel, J. R. *K without the measurable.* The Journal of Symbolic Logic, 2013.
- **[Survey]** Sargsyan, G. *Hod Mice and the Mouse Set Conjecture.* Memoirs of the American Mathematical Society, Vol. 236, No. 1111. AMS, 2015.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, consider the simplest non-trivial core model beyond $L$: the Dodd-Jensen core model $K^{DJ}$ for the hypothesis $\Phi =$ "there is no inner model with a measurable cardinal."

In this case, the extenders simplify dramatically. An extender representing a measurable cardinal $\kappa$ is just a single normal ultrafilter $U$ on $\kappa$. A premouse here is a structure $\mathcal{M}_0 = \langle J_\alpha^U, \in, U \rangle$. 

To test if $\mathcal{M}_0$ is iterable (and thus a true mouse), we form an iteration tree. Because $U$ is just a normal measure, the extenders do not overlap in complex ways, and the tree is strictly linear. At step 0, we take the ultrapower of $\mathcal{M}_0$ by $U$:
$$j_0: \mathcal{M}_0 \to \mathcal{M}_1 = \text{Ult}(\mathcal{M}_0, U)$$
The critical point is $\kappa_0 = \kappa$. In $\mathcal{M}_1$, the image of $\kappa_0$ is $\kappa_1 = j_0(\kappa_0)$, and $j_0(U) = U_1$ is a normal measure on $\kappa_1$. 
We then iterate again:
$$j_1: \mathcal{M}_1 \to \mathcal{M}_2 = \text{Ult}(\mathcal{M}_1, U_1)$$
We can continue this transfinitely. For any ordinal limit stage $\lambda$, because the tree is a single linear branch, there is no ambiguity: the iteration strategy $\Sigma$ has only one choice of branch—the only branch that exists. The direct limit model $\mathcal{M}_\lambda$ is uniquely determined. By a classical theorem of Gaifman, because the original ultrafilter $U$ belongs to a well-founded universe, all such linear direct limits $\mathcal{M}_\lambda$ remain well-founded. 

Thus, every such premouse is unconditionally iterable. The Iterability Problem completely vanishes, UBH is trivially satisfied by linearity, and $K^{DJ}$ can be cleanly defined as the union of all such mice. The profound difficulty of the Core Model Problem only emerges at Woodin cardinals and beyond, where multiple overlapping extenders force the iteration trees to branch non-linearly, requiring a highly complex strategy $\Sigma$ to avoid ill-foundedness.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*