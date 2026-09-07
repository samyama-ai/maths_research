---
id: 08-logic-set-theory/definability-of-the-jump-operator
title: "Definability of the Jump Operator"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Definability of the Jump Operator

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/definability-of-the-jump-operator` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The problem of the "Definability of the Jump Operator" encompasses two deeply related open conjectures in computability theory concerning the Turing degrees $\mathcal{D}$. 

First, in the global structure of the Turing degrees, the conjecture asks whether there exists a *natural*, purely order-theoretic first-order definition of the Turing jump operator, $\mathbf{a} \mapsto \mathbf{a}'$, in the language of partial orders. While Shore and Slaman (1999) definitively proved that the jump operator *is* logically definable, their formula relies on highly complex metamathematical coding (the Slaman-Woodin machinery) to interpret standard models of Peano Arithmetic within the degrees. A "natural" definition—one constructed exclusively from structural geometric properties such as joins, meets, exact pairs, and minimal covers—remains an open problem.

Second, in the local structure of the Turing degrees $\mathcal{D}(\leq \mathbf{0}')$, the overarching conjecture asks whether specific jump classes are first-order definable. The most prominent open question is whether the class of $\text{Low}_1$ degrees (degrees $\mathbf{a} \leq \mathbf{0}'$ such that $\mathbf{a}' = \mathbf{0}'$) is definable in the local poset $\mathcal{D}(\leq \mathbf{0}')$.

## 2. Mathematical Foundations

The fundamental structure in question is the upper semi-lattice of Turing degrees, denoted $\mathcal{D} = (D, \leq_T)$, where $D$ is the set of all equivalence classes of sets of natural numbers under Turing reducibility, and $\leq_T$ denotes Turing reducibility. In the context of definability, $\mathcal{D}$ is typically treated purely as a partially ordered set in the language $L = \{\leq\}$.

For a set $A \subseteq \mathbb{N}$, its Turing jump $A'$ is the halting problem relative to $A$:
$$ A' = \{e \in \mathbb{N} \mid \Phi_e^A(e) \downarrow\} $$
where $\Phi_e^A$ is the $e$-th Turing machine executing with oracle $A$. The jump respects Turing equivalence and strict order ($A \leq_T B \implies A' \leq_T B'$ and $A <_T A'$), thereby inducing a strictly monotonic operator on the degrees: $\mathbf{a} \mapsto \mathbf{a}'$.

A relation $R \subseteq D^n$ is *first-order definable* in $\mathcal{D}$ if there exists an $L$-formula $\varphi(x_1, \dots, x_n)$ such that:
$$ \mathcal{D} \models \varphi(\mathbf{a}_1, \dots, \mathbf{a}_n) \iff R(\mathbf{a}_1, \dots, \mathbf{a}_n) \text{ holds.} $$

The jump operation induces a natural stratification of the degrees below $\mathbf{0}'$, known as the jump hierarchy:
- The **Low hierarchy**: $\text{Low}_n = \{\mathbf{a} \leq \mathbf{0}' \mid \mathbf{a}^{(n)} = \mathbf{0}^{(n)}\}$
- The **High hierarchy**: $\text{High}_n = \{\mathbf{a} \leq \mathbf{0}' \mid \mathbf{a}^{(n)} = \mathbf{0}^{(n+1)}\}$

The local structure of the Turing degrees is the sub-poset $\mathcal{D}(\leq \mathbf{0}') = \{\mathbf{a} \in D \mid \mathbf{a} \leq \mathbf{0}'\}$. The definability of $\text{Low}_1$ asks for a formula $\chi(x)$ in $L$ such that $\mathcal{D}(\leq \mathbf{0}') \models \chi(\mathbf{a}) \iff \mathbf{a}' = \mathbf{0}'$.

## 3. History & State of the Art (SOTA)

The Turing jump was formalized by Alan Turing and Emil Post in the late 1930s and 1940s. Understanding the relationship between the order-theoretic structure of $\mathcal{D}$ and the jump operator has driven computability theory for over 80 years.

In 1986, Slaman and Woodin proved a monumental coding theorem: the partial order of Turing degrees is sufficiently rich to code arbitrary countable models of second-order arithmetic. Consequently, any relation invariant under the double jump is definable in $\mathcal{D}$. However, this logical definability was considered highly "artificial."

In 1990, S. B. Cooper announced a resolution to the natural definability problem in his paper *"The Jump is Definable in the Structure of the Degrees of Unsolvability"* (Bulletin of the AMS). His proposed definition used purely structural properties based on the theory of splittings and pseudo-jump operators over $2$-REA (Recursively Enumerable in and Above) degrees.

In 1999, Richard Shore and Theodore Slaman published *"Defining the Turing jump"*, in which they uncovered a fatal flaw in Cooper’s structural proof, demonstrating that the specific splitting properties Cooper relied upon failed to hold uniformly across different base degrees. To resolve the overarching definability question, Shore and Slaman provided a correct proof that $\mathbf{a} \mapsto \mathbf{a}'$ is definable. Their breakthrough approach circumvented the double-jump requirement of the original Slaman-Woodin theorem, but it fundamentally relied on metamathematical coding, leaving the existence of a *natural* definition strictly open. 

Today, the SOTA acknowledges global logical definability but recognizes the natural definability of the jump, and the local definability of $\text{Low}_1$, as premier unsolved problems.

## 4. Partial Results / Verified Cases

While the natural and local definability remain open, logical definability is well-understood:

- **Global Jump Definability (Shore and Slaman, 1999):** The relation $\mathbf{y} = \mathbf{x}'$ is first-order definable in $\mathcal{D}$. By extension, any degree class defined via the jump (e.g., the $\text{High}_n$ and $\text{Low}_n$ hierarchies globally, the set of arithmetic degrees) is first-order definable in $\mathcal{D}$.
- **Double Jump Definability (Jockusch and Shore, 1984):** The operator $\mathbf{a} \mapsto \mathbf{a}''$ is definable on the cone of degrees $\geq \mathbf{0}'$, using the theory of pseudo-jump operators.
- **Definability in the C.E. Degrees (Nies, Shore, Slaman, 1998):** In the upper semi-lattice of the computably enumerable degrees $\mathcal{R}$, any relation invariant under the double jump is definable if and only if it is definable in first-order true arithmetic. 
- **Bi-interpretability (Slaman, Woodin, Shore):** The structure $\mathcal{D}$ is bi-interpretable with true second-order arithmetic, meaning that the expressive power of the poset $\mathcal{D}$ is logically equivalent to the expressive power of arithmetic.

## 5. Principal Obstacles

The primary mathematical bottleneck in achieving a natural definition is that pure order-theoretic properties in $\mathcal{D}$ (e.g., forming a minimal pair, bounding exact pairs, capping, or cupping) are extraordinarily difficult to tightly couple with the rigid, computational properties of the jump operator without invoking metamathematics.

1. **The Coding Barrier:** The Slaman-Woodin machinery works by utilizing exact pairs (degrees $\mathbf{c}, \mathbf{d}$ bounding an ideal $I_{\mathbf{c}, \mathbf{d}} = \{\mathbf{w} \mid \mathbf{w} \leq \mathbf{c} \land \mathbf{w} \leq \mathbf{d}\}$) to represent coded models of Peano Arithmetic. The definition of the jump is then extracted by explicitly stating, inside the logical language of $\mathcal{D}$, that the ideal maps to the arithmetic formula for the Turing jump. This inherently bypasses the geometric structure of the poset entirely, resulting in massive formulas with thousands of quantifiers that yield zero structural intuition.
2. **Failure of Monotonicity in Splittings:** Purely structural attempts (like Cooper's) rely on the hypothesis that certain degree classes exhibit rigid splitting behaviors unconditionally above arbitrary degrees. It has been empirically and theoretically shown that structural properties in $\mathcal{D}$ are highly sensitive to the base degree, causing uniform structural definitions to collapse under relativization.
3. **Local Structure Constraints:** In the local structure $\mathcal{D}(\leq \mathbf{0}')$, the jump operator maps degrees outside the universe of discourse, since $\mathbf{a}' \not\leq \mathbf{0}'$ for non-low degrees. Because the jump is not a closed operation in $\mathcal{D}(\leq \mathbf{0}')$, researchers cannot leverage global jump-inversion techniques. The lack of a local bi-interpretability theorem for $\mathcal{D}(\leq \mathbf{0}')$ further exacerbates the inability to construct even an artificial definition for $\text{Low}_1$.

## 6. The Gap

The exact boundary separating what is proven (logical definability) from the conjecture (natural definability) is the transition from a *metamathematical* formula to a *structural* formula. 

Mathematically, a resolution requires finding a first-order $L$-formula $\psi(x,y)$ such that:
$$ \mathcal{D} \models \psi(\mathbf{a}, \mathbf{b}) \iff \mathbf{b} = \mathbf{a}' $$
where $\psi$ is constructed exclusively from pure poset-theoretic primitives (e.g., minimal covers, infima, suprema, and bounding properties of ideals), explicitly avoiding any sub-formulas that decode standard models of arithmetic.

For the local structure, the gap is absolute: there is currently no known formula $\chi(x)$—artificial or natural—such that $\mathcal{D}(\leq \mathbf{0}') \models \chi(\mathbf{a}) \iff \mathbf{a}' = \mathbf{0}'$. Defining $\text{Low}_1$ locally requires uncovering a structural asymmetry between low and non-low degrees that is expressible entirely strictly below $\mathbf{0}'$.

## 7. Current Research (as of June 2026)

Active research by groups at the University of Chicago, UC Berkeley, and Victoria University of Wellington continues to center on the interplay between computability, randomness, and structural definability.

- **Structural Properties of C.E. Degrees:** Researchers are exploring subclasses of the c.e. degrees, such as totally $\omega$-c.e. degrees, $K$-trivial degrees, and array noncomputable degrees. The goal is to determine whether their robust structural capping and cupping properties uniquely identify jump classes without arithmetic coding.
- **Automorphism Group of $\mathcal{D}(\leq \mathbf{0}')$:** The search for definability is deeply intertwined with the rigidity of the local degrees. If $\mathcal{D}(\leq \mathbf{0}')$ is rigid (meaning the only automorphism is the identity), a natural definition of $\text{Low}_1$ could theoretically be extracted from the automorphism base.
- *(frontier — verify)* Recent preprints explore utilizing topological invariants transferred from the enumeration degrees ($\mathcal{D}_e$) to induce rigid structural definitions back into the local Turing degrees, attempting to circumvent the Slaman-Woodin coding mechanism altogether.

## 8. Future Work

Leading theoreticians have outlined specific research pathways to traverse the definability gap:
1. **Identify a Robust Pseudo-Jump Operator:** The original intuition behind Cooper's attempt was conceptually sound. Future work seeks a pseudo-jump operator that behaves canonically across all cones, bypassing the relativization counterexamples that fractured previous proofs.
2. **Local Bi-interpretability:** Establish whether the local structure $\mathcal{D}(\leq \mathbf{0}')$ is bi-interpretable with first-order arithmetic. Proving local bi-interpretability is widely viewed as a mandatory prerequisite to finding any definition (even an artificial one) for the local $\text{Low}_1$ degrees.
3. **C.E. Definability:** Find a natural definition for the class of computably enumerable degrees within the global structure $\mathcal{D}$. Since the jump is intimately tied to enumerability (via Post's Theorem), a structural definition of the c.e. degrees would immediately yield a structural definition of the jump.

## 9. Key References

- **[Foundational]** Shore, R. A., & Slaman, T. A. *Defining the Turing jump.* Mathematical Research Letters, 6(5-6), 711-722, 1999.
- **[Foundational]** Cooper, S. B. *The Jump is Definable in the Structure of the Degrees of Unsolvability.* Bulletin of the American Mathematical Society, 23(1), 151-158, 1990.
- **[Survey]** Nies, A. *Computability and Randomness.* Oxford University Press, 2009.
- **[SOTA / Recent]** Downey, R., & Hirschfeldt, D. R. *Algorithmic Randomness and Complexity.* Springer, 2010.

## 10. Worked Example / Concrete Special Case

To concretely illustrate the difference between a natural structural definition and a metamathematical one, consider how one defines the least degree $\mathbf{0}$ versus the Turing jump $\mathbf{0}'$ globally.

The least degree $\mathbf{0}$ admits a trivial, beautifully "natural" definition in $L = \{\leq\}$ as the unique global minimum:
$$ \phi_0(x) := \forall y (x \leq y) $$

If we possessed a natural structural formula $\psi(x, y)$ for the jump operation $y = x'$, we could define $\mathbf{0}'$ purely geometrically as the unique element $y$ satisfying:
$$ \exists z (\phi_0(z) \land \psi(z, y)) $$

A natural candidate for the geometric property $\psi(x,y)$ might attempt to use the concept of a *minimal cover*. A degree $\mathbf{v}$ is a minimal cover of $\mathbf{u}$ if:
$$ M(\mathbf{u}, \mathbf{v}) := \mathbf{u} < \mathbf{v} \land \neg \exists \mathbf{w} (\mathbf{u} < \mathbf{w} < \mathbf{v}) $$
One might historically hypothesize that $\mathbf{a}'$ could be defined structurally as the supremum of all minimal covers over $\mathbf{a}$, or via some exact pair bounding a specific ideal of minimal covers.

However, because of the chaotic geometric nature of the Turing degrees, simple structural formulas inevitably fail. Instead, the Shore-Slaman theorem mathematically guarantees that $\psi(x, y)$ exists, but constructs it via coding:
1. It uses exact pairs $\mathbf{c}, \mathbf{d}$ to define an order-theoretic ideal $I_{\mathbf{c}, \mathbf{d}} = \{\mathbf{w} \mid \mathbf{w} \leq \mathbf{c} \land \mathbf{w} \leq \mathbf{d}\}$.
2. It asserts, via thousands of quantifiers, that the poset structure of $I_{\mathbf{c}, \mathbf{d}}$ algebraically encodes a standard model of arithmetic $\mathcal{M}$.
3. It states that inside this coded model $\mathcal{M}$, the integer element representing $\mathbf{y}$ satisfies the arithmetic relation of being the Turing jump of the integer element representing $\mathbf{x}$.

This $\psi(x,y)$ undeniably isolates $y = x'$ logically, but completely obfuscates the intrinsic "shape" of the jump operator in the partial order, perfectly highlighting the mathematical gap that defines this open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*