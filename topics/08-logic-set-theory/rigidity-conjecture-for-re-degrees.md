---
id: 08-logic-set-theory/rigidity-conjecture-for-re-degrees
title: "Rigidity Conjecture for RE Degrees"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rigidity Conjecture for RE Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/rigidity-conjecture-for-re-degrees` · **Status:** open

## 1. Problem Statement / Conjecture

The Rigidity Conjecture for Recursively Enumerable (RE) Degrees asserts that the upper semi-lattice of RE Turing degrees, denoted $\mathcal{R} = \langle \mathbf{R}, \le_T \rangle$, is globally rigid. That is, the only automorphism of this structure is the trivial identity map.

Formally, an automorphism of the RE degrees is a bijection $\pi : \mathbf{R} \to \mathbf{R}$ such that for all RE degrees $\mathbf{a}, \mathbf{b} \in \mathbf{R}$:
$$ \mathbf{a} \le_T \mathbf{b} \iff \pi(\mathbf{a}) \le_T \pi(\mathbf{b}) $$
The Rigidity Conjecture posits that if $\pi$ is such an automorphism, then $\pi(\mathbf{a}) = \mathbf{a}$ for all $\mathbf{a} \in \mathbf{R}$.

This conjecture is intimately connected to the stronger **Bi-interpretability Conjecture** for $\mathcal{R}$ (formulated by Harrington and Slaman), which claims that the standard model of first-order arithmetic $\mathbb{N}$ is bi-interpretable with $\mathcal{R}$ without the use of parameters. If the Bi-interpretability Conjecture holds, rigidity follows as a direct mathematical consequence, because every individual RE degree would be uniquely definable by a parameter-free first-order formula in the language of upper semi-lattices. A complete proof of the Rigidity Conjecture would require either demonstrating this parameter-free definability for all degrees, or fundamentally proving that any non-trivial order-preserving bijection on this structure is impossible due to the structural density and coding capabilities of $\mathcal{R}$.

## 2. Mathematical Foundations

The study of the RE degrees is situated in Computability Theory (Recursion Theory). A set $A \subseteq \mathbb{N}$ is **recursively enumerable (RE)** (or computably enumerable, c.e.) if it is the domain of a partial computable function, equivalent to being definable by a $\Sigma_1^0$ formula in the arithmetical hierarchy.

**Turing Reducibility:** For sets $A, B \subseteq \mathbb{N}$, we say $A$ is Turing reducible to $B$, denoted $A \le_T B$, if there exists an oracle Turing machine $\Phi_e$ such that $\Phi_e^B = A$. The relation $\le_T$ is a preorder. 

**Turing Degrees:** The equivalence relation $A \equiv_T B \iff (A \le_T B \land B \le_T A)$ partitions the power set of $\mathbb{N}$ into Turing degrees. The set of all Turing degrees containing at least one RE set is denoted $\mathbf{R}$. 

**Upper Semi-Lattice Structure:** The structure $\mathcal{R} = \langle \mathbf{R}, \le, \mathbf{0}, \mathbf{0}', \vee \rangle$ forms an upper semi-lattice where:
*   $\mathbf{0}$ is the degree of recursive (computable) sets, acting as the global minimum.
*   $\mathbf{0}'$ is the degree of the Halting Problem (e.g., the set $K = \{e \mid \Phi_e(e) \downarrow\}$), acting as the global maximum.
*   The supremum or *join* of two degrees $\mathbf{a}, \mathbf{b}$, denoted $\mathbf{a} \vee \mathbf{b}$, is induced by the effective disjoint union of sets: $A \oplus B = \{2x \mid x \in A\} \cup \{2x+1 \mid x \in B\}$.

**The Turing Jump:** The jump operator $\mathbf{a} \mapsto \mathbf{a}'$ corresponds to the relativized Halting Problem. A class of degrees is defined by their jump behavior. For $n \ge 1$, the High-$n$ and Low-$n$ classes are:
$$ \mathbf{H}_n = \{\mathbf{a} \in \mathbf{R} \mid \mathbf{a}^{(n)} = \mathbf{0}^{(n+1)}\} $$
$$ \mathbf{L}_n = \{\mathbf{a} \in \mathbf{R} \mid \mathbf{a}^{(n)} = \mathbf{0}^{(n)}\} $$

**Interpretability:** A structure $\mathcal{A}$ is interpretable in $\mathcal{B}$ if the domain of $\mathcal{A}$ and its relations can be defined by first-order formulas in the language of $\mathcal{B}$ (possibly quotiented by a definable equivalence relation). Bi-interpretability between $\mathcal{R}$ and the standard model of arithmetic $\langle \mathbb{N}, +, \times, 0, 1 \rangle$ implies that there is a map from $\mathbb{N}$ to a definable subset of $\mathcal{R}$, and vice versa, such that the compositions are definable without parameters.

## 3. History & State of the Art (SOTA)

The internal structure of the RE degrees has been intensely scrutinized since the 1950s. Early milestones include the Friedberg-Muchnik Theorem (1956), which proved that $\mathbf{R}$ is not a linear order by constructing two incomparable RE degrees, thus demonstrating that non-trivial structure exists.

In the 1960s, Gerald Sacks proved the Density Theorem (between any $\mathbf{a} < \mathbf{b}$ in $\mathbf{R}$, there exists a $\mathbf{c}$ such that $\mathbf{a} < \mathbf{c} < \mathbf{b}$). This sparked Shoenfield's Conjecture, which posited a form of homogeneity that would imply $\mathcal{R}$ admits many automorphisms. Shoenfield's Conjecture was thoroughly refuted by Lachlan and Yates (1966) using the Minimal Pair Theorem and the Non-Diamond Theorem, revealing the extreme algebraic complexity of $\mathcal{R}$.

In the 1980s, Leo Harrington and Theodore Slaman initiated the modern approach to the Automorphism Problem by formulating the Bi-interpretability Conjecture. Their insight was that rather than being homogeneous, $\mathcal{R}$ was wildly rigid, capable of coding arbitrary models of arithmetic. They proved that one can interpret true arithmetic in $\mathcal{R}$ *with parameters*. 

The defining SOTA breakthrough occurred in 1998, when Nies, Shore, and Slaman published a landmark result proving that one can define the standard model of arithmetic in $\mathcal{R}$ without parameters. This constrained the automorphism group severely, establishing that any automorphism must preserve all relations definable in first-order arithmetic.

The problem faced a dramatic episode in 1997 when S. B. Cooper circulated a manuscript claiming to construct a non-trivial automorphism of the RE degrees. Cooper’s construction was a colossal, infinite-injury priority argument on a tree of strategies of extraordinary complexity ($\mathbf{0}'''$-priority). For a brief period, the Rigidity Conjecture was thought to be false. However, subsequent intensive verification by Slaman, Shore, and others revealed a fatal, irreparable flaw in the interaction between the requirements preserving the join operation and the requirements driving the non-triviality of the mapping. The conjecture returned to its status as one of the most prominent open problems in computability theory.

## 4. Partial Results / Verified Cases

While full global rigidity is not yet proven, the automorphism group of $\mathcal{R}$, denoted $Aut(\mathcal{R})$, has been shown to be exceptionally restricted. The following structural rigidity results are mathematically verified:

1.  **Countability of Automorphisms:** Slaman and Woodin proved that the global Turing degrees $\mathcal{D}$ possess at most countably many automorphisms. Harrington and Slaman adapted this framework to prove that $Aut(\mathcal{R})$ is at most countable.
2.  **Preservation of Jump Classes:** By the fundamental definability result of Nies, Shore, and Slaman (1998), any automorphism $\pi \in Aut(\mathcal{R})$ must preserve all relations definable in first-order logic over $\mathcal{R}$. Consequently, $\pi$ must preserve the High-$n$ and Low-$n$ classes for $n \ge 2$:
    $$ \forall \mathbf{a} \in \mathbf{R}, \mathbf{a} \in \mathbf{H}_n \iff \pi(\mathbf{a}) \in \mathbf{H}_n $$
    $$ \forall \mathbf{a} \in \mathbf{R}, \mathbf{a} \in \mathbf{L}_n \iff \pi(\mathbf{a}) \in \mathbf{L}_n $$
3.  **Preservation of Specific Ideals:** The ideal of $K$-trivial degrees (degrees corresponding to sets that are highly compressible in terms of Kolmogorov complexity) is structurally definable in $\mathcal{R}$ (as proved by André Nies). Thus, any automorphism must fix the ideal of $K$-trivial degrees as a set.
4.  **Local Rigidity:** A degree $\mathbf{a}$ is an *exact pair* for an ideal $I$ if it is an upper bound for $I$, and any other upper bound $\mathbf{b}$ for $I$ must satisfy $\mathbf{b} \ge \mathbf{a}$. Shore established that automorphisms behave identically on degrees that can be represented as specific algebraic limits of such ideals, narrowing the scope where an automorphism could hypothetically deviate from the identity.

## 5. Principal Obstacles

The Rigidity Conjecture remains unsolved because it sits exactly at the nexus of two disparate methodologies that current mathematics cannot easily merge: global order-theoretic coding and constructive priority arguments. 

**The Limits of Priority Arguments:** Constructing a non-trivial automorphism $\pi$ requires building an effective procedure that simultaneously satisfies:
1.  $\pi(\mathbf{a}) \neq \mathbf{a}$ for some specific $\mathbf{a}$.
2.  $\pi(\mathbf{x} \vee \mathbf{y}) = \pi(\mathbf{x}) \vee \pi(\mathbf{y})$ for all $\mathbf{x}, \mathbf{y}$.
3.  The mapping is a bijection.

Satisfying these requirements across the uncountable domain of real numbers restricted to RE degrees demands a dynamic tree of strategies of at least $\mathbf{0}'''$ complexity (often framed as a $\Pi_3^0$ or $\Sigma_3^0$ priority argument). Standard techniques like traditional forcing, finite extension arguments, or finite-injury priority fail entirely. When researchers scale priority arguments to the $\mathbf{0}'''$ level, the "injury" to lower-priority requirements becomes infinitely profound. The failure of Cooper’s proof demonstrated that forcing structural homomorphisms over infinite joins inevitably collapses the non-triviality conditions—the constraints of the semi-lattice are too tight.

**The Limits of Definability:** Conversely, proving that $Aut(\mathcal{R})$ contains *only* the identity map requires proving that every single degree $\mathbf{x} \in \mathbf{R}$ is parameter-free definable. The primary mechanism for defining structures in $\mathcal{R}$ is Slaman-Woodin coding, which uses independent subsets to encode relations. However, this coding relies on *parameters* (e.g., choosing specific degrees $\vec{p}$ to serve as the "basis" for the coded model of arithmetic). While Nies, Shore, and Slaman managed to remove the parameters to define the standard model of arithmetic $\mathbb{N}$ as a whole, their technique cannot uniformly isolate every individual degree $\mathbf{a} \in \mathcal{R}$. 

## 6. The Gap

The exact mathematical barrier separating the proven partial results (Section 4) from the full Rigidity Conjecture (Section 1) is the transition from **parameter-based definability** to **pointwise, parameter-free definability of arbitrary relations**.

Currently, we know that if $f: \mathbb{N} \to \mathcal{R}$ is a coding map, there exists a tuple of parameters $\vec{p} \in \mathbf{R}$ such that the image of $f$ and its relations are definable from $\vec{p}$. To cross the gap, one must prove the following logical equivalence for the structure $\mathcal{R}$:
For any degree $\mathbf{a}$, there exists a first-order formula $\varphi_{\mathbf{a}}(x)$ in the language of partial orders $\langle \le \rangle$ such that for all $\mathbf{x} \in \mathbf{R}$:
$$ \mathcal{R} \models \varphi_{\mathbf{a}}(\mathbf{x}) \iff \mathbf{x} = \mathbf{a} $$
If this parameter-free identification holds pointwise, then any automorphism $\pi$ must preserve the formula $\varphi_{\mathbf{a}}$. Thus, $\mathcal{R} \models \varphi_{\mathbf{a}}(\pi(\mathbf{a}))$, which immediately forces $\pi(\mathbf{a}) = \mathbf{a}$, proving rigidity. Bridging this gap requires discovering an entirely new structural invariant in $\mathcal{R}$ that does not rely on Slaman-Woodin coding intervals.

## 7. Current Research (as of June 2026)

Active research into the Rigidity Conjecture has bifurcated into two primary schools of thought:

1.  **Algorithmic Randomness and Structural Definability:** Led by researchers affiliated with institutions like the University of Auckland (Nies) and the University of Chicago (Hirschfeldt, Slaman), this approach looks at classes derived from algorithmic randomness. Because the $K$-trivial degrees form a robust, naturally definable ideal in $\mathcal{R}$, there is heavy investigation into whether intermediate degrees can be uniquely specified by their lattice-theoretic distances from the $K$-trivials. 
2.  **Machine-Assisted Verification of Priority Arguments:** *(frontier — verify)* Given the historical trauma of Cooper’s flawed 1997 proof, there is a rising movement employing interactive theorem provers (like Lean and Coq) to formalize higher-order computability theory. Groups at Carnegie Mellon and Cambridge are actively transcribing the mechanics of $\mathbf{0}'''$-priority trees into formalized mathematics. The goal is to either exhaustively prove the impossibility of an automorphism by formalizing the structural collapse, or to find a path through the priority conflicts that a human mathematician could not reliably manage. 

## 8. Future Work

Leading logicians suggest two actionable pathways to eventually resolve the conjecture:
*   **The Theory of $\mathcal{R}$:** Understand the complexity of the first-order theory $Th(\mathcal{R})$. It is known to be recursively isomorphic to true arithmetic. A deeper understanding of the quantifier complexity required to define specific intervals $[\mathbf{a}, \mathbf{b}]$ could yield a generic parameter-free definition.
*   **Refuting Bi-Interpretability via Automorphism:** If the conjecture is false, constructing the automorphism will likely require abandoning traditional priority trees. Future work suggests examining automorphisms on the degree structure of continuous degrees or Medvedev degrees, and attempting to pull an automorphism down to the RE degrees via some powerful topological fixed-point theorem, circumventing effective construction entirely.

## 9. Key References

- **[Foundational]** Slaman, T. A., & Woodin, W. H. *Definability in the Turing degrees.* Illinois Journal of Mathematics, 1986.
- **[Foundational]** Nies, A., Shore, R. A., & Slaman, T. A. *Interpretability and definability in the recursively enumerable degrees.* Proceedings of the London Mathematical Society, 1998.
- **[Survey]** Shore, R. A. *The recursively enumerable degrees.* Handbook of Computability Theory, 1999.
- **[SOTA / Recent]** Soare, R. I. *Turing Computability: Theory and Applications.* Springer, 2016. (Contains detailed accounts of the automorphism problem and coding methodologies).
- **[SOTA / Recent]** Nies, A. *Computability and Randomness.* Oxford University Press, 2009.

## 10. Worked Example / Concrete Special Case

To ground the abstract concept of rigidity, consider the simplest possible degrees in the structure: the global minimum $\mathbf{0}$ and the global maximum $\mathbf{0}'$. We can easily demonstrate that any proposed automorphism $\pi: \mathbf{R} \to \mathbf{R}$ must act as the identity on these two points.

**Proof that $\pi(\mathbf{0}) = \mathbf{0}$:**
The degree $\mathbf{0}$ (the degree of all computable sets) is uniquely characterized by the first-order formula:
$$ \varphi_{min}(x) \equiv \forall y (x \le y) $$
Because $\pi$ is an automorphism, it preserves the order $\le$. If $\mathbf{0} \le \mathbf{y}$ for all $\mathbf{y}$, then applying $\pi$ yields $\pi(\mathbf{0}) \le \pi(\mathbf{y})$ for all $\mathbf{y}$. Since $\pi$ is a bijection, as $\mathbf{y}$ ranges over all of $\mathbf{R}$, $\pi(\mathbf{y})$ also ranges over all of $\mathbf{R}$. Thus, $\pi(\mathbf{0})$ must be $\le$ every element in $\mathbf{R}$. Since $\mathbf{0}$ is the unique element with this property, it must follow that $\pi(\mathbf{0}) = \mathbf{0}$.

**Proof that $\pi(\mathbf{0}') = \mathbf{0}'$:**
Similarly, $\mathbf{0}'$ is the unique maximum of the RE degrees, characterized by:
$$ \varphi_{max}(x) \equiv \forall y (y \le x) $$
By an identical bijection argument, $\pi(\mathbf{0}')$ must also be the maximum element, forcing $\pi(\mathbf{0}') = \mathbf{0}'$.

**Branching and Incomparability:**
Now consider the classic Friedberg-Muchnik theorem, which states there exist RE degrees $\mathbf{a}, \mathbf{b}$ such that $\mathbf{a} \not\le \mathbf{b}$ and $\mathbf{b} \not\le \mathbf{a}$ (they are incomparable). If $\pi$ is an automorphism, it must preserve this structural feature exactly:
$$ \mathbf{a} \not\le \mathbf{b} \iff \pi(\mathbf{a}) \not\le \pi(\mathbf{b}) $$
If one attempts to build a non-trivial automorphism where $\pi(\mathbf{x}) \neq \mathbf{x}$, one cannot simply shift $\mathbf{x}$ "up" or "down" the order without causing cascading structural violations. For instance, if $\mathbf{x} = \mathbf{a} \vee \mathbf{b}$, then the new degree $\pi(\mathbf{x})$ must be exactly the join $\pi(\mathbf{a}) \vee \pi(\mathbf{b})$. 

Because every RE degree is tightly interwoven with infinitely many incomparable pairs and joins (due to the Sacks Density Theorem and splitting theorems), a shift in a single degree $\mathbf{x}$ demands a synchronized, mathematically perfect shift of uncountably many intersecting algebraic relations. The Rigidity Conjecture posits that this tight web simply leaves no "room" for any global mapping other than the identity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*