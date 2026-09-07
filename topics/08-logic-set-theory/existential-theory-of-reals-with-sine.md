---
id: 08-logic-set-theory/existential-theory-of-reals-with-sine
title: "Existential Theory of Reals with Sine"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existential Theory of Reals with Sine

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/existential-theory-of-reals-with-sine` · **Status:** open

## 1. Problem Statement / Conjecture

The problem asks whether the existential first-order theory of the real numbers equipped with the sine function is decidable. Formally, does there exist a general algorithm (such as a Turing machine) that takes as input any existential sentence $\phi$ over the language $\mathcal{L}_{\sin} = \{+, \cdot, 0, 1, <, \sin\}$ and outputs in finite time whether $\phi$ is true in the standard model of the reals $\mathcal{R}_{\sin} = \langle \mathbb{R}, +, \cdot, 0, 1, <, \sin \rangle$?

An existential sentence in this language is of the form:
$$ \exists x_1, x_2, \dots, x_n \in \mathbb{R} : \psi(x_1, \dots, x_n) $$
where $\psi$ is a quantifier-free Boolean combination (using $\land, \lor, \neg$) of polynomial inequalities and equations that may include the $\sin$ function applied to variables and terms.

The prevailing **conjecture** is that this theory is **undecidable**. The primary justification is that the periodic nature of the sine function allows for the encoding of discrete structures within the continuous real numbers. Specifically, because the roots of the sine function correspond to integer multiples of $\pi$, this theory can embed the existential theory of the rational numbers $\mathbb{Q}$. Consequently, the undecidability of the existential theory of $\mathcal{R}_{\sin}$ is tightly bound to Hilbert's Tenth Problem over the rationals, $H10(\mathbb{Q})$, one of the most prominent open problems in Diophantine geometry.

## 2. Mathematical Foundations

The foundation of the problem lies in model theory and real algebraic geometry.

Let $\mathcal{L}_{\text{or}} = \{+, \cdot, 0, 1, <\}$ be the standard language of ordered rings. Tarski's famous theorem (1951) establishes that the full first-order theory of the real closed field $\langle \mathbb{R}, +, \cdot, 0, 1, < \rangle$ admits quantifier elimination and is decidable. The existential fragment of this theory, known as the Existential Theory of the Reals ($\exists\mathbb{R}$), is equivalent to deciding the non-emptiness of semi-algebraic sets and is known to be in PSPACE (Canny, 1988).

The structure in question is the expansion $\mathcal{R}_{\sin} = \langle \mathbb{R}, +, \cdot, 0, 1, <, \sin \rangle$. We restrict our attention to the existential fragment $Th_{\exists}(\mathcal{R}_{\sin})$, which consists of all true sentences of the form $\exists \mathbf{x} \in \mathbb{R}^n : \psi(\mathbf{x})$.

The presence of the sine function completely breaks the tameness (specifically, the o-minimality) of the real field. The set defined by the formula $\phi(x) \equiv \sin(x) = 0$ is exactly the discrete lattice $\pi \mathbb{Z}$.

This leads to a profound model-theoretic consequence. In the full first-order theory $Th(\mathcal{R}_{\sin})$, the constant $\pi$ is definable via the formula:
$$ \phi_{\pi}(p) \equiv \sin(p) = 0 \land p > 0 \land \forall y \, (0 < y < p \implies \sin(y) \neq 0) $$
Once $\pi$ is defined, the integers $\mathbb{Z}$ are definable via $x \in \mathbb{Z} \iff \exists k \in \mathbb{R} \, (x = k \land \sin(\pi k) = 0)$. By Gödel's Incompleteness Theorem and the Davis-Putnam-Robinson-Matiyasevich theorem (which proves $H10(\mathbb{Z})$ is undecidable), the full first-order theory $Th(\mathcal{R}_{\sin})$ is undeniably undecidable.

However, the existential theory $Th_{\exists}(\mathcal{R}_{\sin})$ lacks the universal quantifier $\forall$ needed to enforce that $p$ is the *smallest* positive root of sine. An existential formula can only state $\sin(p) = 0$, which ensures $p = m\pi$ for some unknown $m \in \mathbb{Z}$. Because of this, variables constrained by $\sin(x_i) = 0$ map to $n_i \pi$. Ratios of such variables take the form $(n_i \pi) / (m \pi) = n_i / m \in \mathbb{Q}$. Therefore, the language naturally models Diophantine problems over the rationals $\mathbb{Q}$ rather than over $\mathbb{Z}$.

## 3. History & State of the Art (SOTA)

The history of decision problems for elementary functions traces back to Hilbert's Tenth Problem (1900), which asked for an algorithm to solve Diophantine equations. Following the resolution of $H10(\mathbb{Z})$ in 1970, attention shifted to subrings and fields of algebraic numbers, most notably $\mathbb{Q}$.

In the realm of real continuous functions, Richardson's Theorem (1968) was a major milestone. Richardson proved that if one considers the theory of real numbers equipped with both the sine function and the exponential function (along with a few other primitives), the identity problem is undecidable. This heavily implied that adding periodic and transcendental functions to the reals immediately leads to uncomputability.

In 1996, Macintyre and Wilkie proved a monumental result: the full first-order theory of the reals with the exponential function, $Th(\mathcal{R}_{\exp})$, is decidable conditionally on Schanuel's Conjecture in transcendental number theory. The exponential function preserves a property called o-minimality (first established for $\mathbb{R}_{\exp}$ by van den Dries). O-minimality prevents infinite discrete definable sets. 

The sine function, by its very nature, is periodic and thereby anti-o-minimal. As such, the approach of Macintyre and Wilkie cannot be applied. The problem of $\exists\mathcal{R}_{\sin}$ was thus isolated as a boundary case: it is the simplest transcendental extension of the real field that shatters o-minimality but for which the existential fragment's undecidability remains unproven, largely because it hinges on the deep number-theoretic open problem of $H10(\mathbb{Q})$.

Currently, the state of the art resides in the intersection of model theory and arithmetic geometry. Mathematicians are approaching the problem via Mazur's conjectures on the topology of rational points on varieties, and via effective methods for restricted analytic functions (Pfaffian functions).

## 4. Partial Results / Verified Cases

While the general problem is open, several highly restricted variants have been fully solved and verified:

- **Bounded Existential Quantifiers:** If the existential quantifiers are constrained to a bounded hypercube, e.g., $\exists x_1, \dots, x_n \in [-R, R]$, the problem is decidable. Over a compact domain, the sine function only possesses finitely many roots, preventing the encoding of arbitrary rational numbers. Tools from effective real analytic geometry, specifically adaptations of Cylindrical Algebraic Decomposition (CAD) for sub-analytic sets, provide algorithms to decide such bounded formulas, provided non-degeneracy conditions are met.
- **The Restricted Sine Function $\sin|_{[-\pi, \pi]}$:** Adding only a truncated version of the sine function (which is evaluated as $0$ outside $[-\pi, \pi]$) preserves o-minimality. The existential theory of this structure, denoted $\mathbb{R}_{\text{an}}$ (the real field with restricted analytic functions), is decidable.
- **Existential Theory with Constants:** If the constant $\pi$ is explicitly added to the language to form $\mathcal{L}_{\sin, \pi} = \{+, \cdot, 0, 1, <, \pi, \sin\}$, the existential theory is proven to be unconditionally **undecidable**. The formula $\exists x (\sin(\pi x) = 0 \land \dots)$ allows exact encoding of integers, trivially reducing $H10(\mathbb{Z})$ to $Th_{\exists}(\mathcal{R}_{\sin, \pi})$.

## 5. Principal Obstacles

The core reason this problem remains unsolved is the structural rigidity of the "scale invariance" enforced by the existential fragment.

To prove undecidability, one typically embeds a known undecidable structure (like the integers $\mathbb{Z}$ with addition and multiplication) into the target structure. In $\exists\mathcal{R}_{\sin}$, we can define an infinite discrete grid by forcing variables into the set of roots $Z(\sin) = \{k\pi \mid k \in \mathbb{Z}\}$. 

However, multiplication over this grid yields $(n\pi) \cdot (m\pi) = nm\pi^2$. To map this back into the grid of roots, one must divide out by $\pi$, which requires the explicit constant $\pi$. Because $\pi$ cannot be defined existentially, we are forced to introduce a proxy period parameter, say $p$, where $\sin(p) = 0$ and $p \neq 0$. Any Diophantine system $P(y_1, \dots, y_k) = 0$ is translated to $P(x_1/p, \dots, x_k/p) = 0$. Since $p$ could be *any* $m\pi$, the existence of a solution merely guarantees that there exist integers $n_1, \dots, n_k, m$ ($m \neq 0$) such that $P(n_1/m, \dots, n_k/m) = 0$. 

This means the language perfectly captures the existence of **rational** solutions, not strictly integer solutions. Since the decidability of Hilbert's Tenth Problem over the rationals ($H10(\mathbb{Q})$) is widely considered to be one of the most intractable open problems in modern mathematics, establishing the undecidability of $\exists\mathcal{R}_{\sin}$ via this route is severely blocked. 

Furthermore, standard algorithmic techniques for continuous real fields (like Gröbner bases, Sturm sequences, and Tarski-Seidenberg projections) rely heavily on polynomials having finite roots and algebraically well-behaved limits. The infinite oscillations of the sine function introduce topological properties—such as the roots being Zariski dense in the real plane—that inherently break the algebraic termination conditions of these classical geometric algorithms.

## 6. The Gap

The exact mathematical barrier separating what is known from a full resolution lies in the equivalence space between $\exists\mathcal{R}_{\sin}$ and $H10(\mathbb{Q})$. 

We know that a negative resolution (undecidability) of $H10(\mathbb{Q})$ immediately implies the undecidability of $\exists\mathcal{R}_{\sin}$. The gap is whether $\exists\mathcal{R}_{\sin}$ is *strictly stronger* than $H10(\mathbb{Q})$. Could $\exists\mathcal{R}_{\sin}$ be undecidable even if $H10(\mathbb{Q})$ were to be proven decidable?

Crossing this gap requires exploiting the transcendental properties of the sine function evaluated at non-root points. For example, expressions like $\sin(\sin(x)) = \sin(y)$ or combinations of algebraic operations on transcendental values might be used to encode undecidable word problems or matrix mortality problems. If a researcher can construct an existential definition of $\mathbb{Z}$ in $\mathbb{R}_{\sin}$ that leverages transcendental evaluations (perhaps relying on deep theorems in transcendence theory like Lindemann-Weierstrass or Baker's theorem on linear forms in logarithms), the problem could be resolved independently of $H10(\mathbb{Q})$.

## 7. Current Research (as of June 2026)

Current active research attacking this problem proceeds along two distinct but interconnected tracks:

1.  **Diophantine Geometry and $H10(\mathbb{Q})$:** The dominant school of thought focuses on resolving $H10(\mathbb{Q})$, which would close the sine problem as a corollary. Institutions such as MIT and the Institute for Advanced Study are deeply engaged in utilizing elliptic curves of rank 1 to model integers over rationals. Koenigsmann's celebrated 2016 result successfully defined $\mathbb{Z}$ in $\mathbb{Q}$ using a universal-existential ($\forall\exists$) formula, bringing the field agonizingly close to an existential definition.
2.  **Effective O-minimality:** Researchers like Binyamini and Novikov are analyzing restricted analytic structures and Pfaffian functions. By understanding the precise computational complexity of algorithms on bounded intervals, researchers hope to identify exactly where the phase transition to undecidability occurs as the bounds are lifted to infinity. 
3.  *(frontier — verify)* Recent preprints have claimed that one can simulate universal quantifiers conditionally using topological degree theory and the intermediate value theorem embedded within existential formulas over continuous curves. If verified, this technique might allow a localized "smallest positive root" definition, establishing $\pi$ existentially and proving undecidability outright without waiting for $H10(\mathbb{Q})$.

## 8. Future Work

Leading mathematicians suggest the following pathways for future research:
- **Elliptic Curves of Rank 1:** Complete the program of defining $\mathbb{Z}$ existentially over $\mathbb{Q}$ by proving that the Shafarevich-Tate group is finite for a specific class of elliptic curves. This would allow elliptic curves to model integer sequences, rendering $H10(\mathbb{Q})$—and by extension $\exists\mathcal{R}_{\sin}$—undecidable.
- **Transcendence-Based Encodings:** Investigate whether the existential theory of $\langle \mathbb{R}, +, \cdot, \sin \rangle$ can define subsets of $\mathbb{R}$ that are not definable in the rational field. Specifically, can the uncomputability of irrationality measures for certain transcendental numbers be exploited existentially?
- **Decidability of the Universal-Existential Fragment:** While the existential fragment is open, determining the exact complexity hierarchy of alternating quantifier blocks (e.g., $\Sigma_2$) in $\mathcal{R}_{\sin}$ might provide structural insights into the purely existential limit.

## 9. Key References

- **[Foundational]** Tarski, A. *A Decision Method for Elementary Algebra and Geometry.* RAND Corporation, 1951.
- **[Foundational]** Richardson, D. *Some Undecidable Problems Involving Elementary Functions of a Real Variable.* Journal of Symbolic Logic, 1968.
- **[Foundational]** Matiyasevich, Y. *Hilbert's Tenth Problem.* MIT Press, 1993. 
- **[SOTA / Recent]** Koenigsmann, J. *Defining $\mathbb{Z}$ in $\mathbb{Q}$.* Annals of Mathematics, 2016.
- **[SOTA / Recent]** Poonen, B. *Undecidability in Number Theory.* Notices of the AMS, 2008.
- **[Survey]** Binyamini, G., Novikov, D. *Effective o-minimality for restricted Pfaffian functions.* Duke Mathematical Journal, 2023.
- **[Survey]** Marker, D. *Model Theory and Exponentiation.* Notices of the AMS, 1996.

## 10. Worked Example / Concrete Special Case

To understand why the existential theory of reals with sine encodes rational (rather than integer) arithmetic, we can walk through a concrete formula attempting to solve the equation $y^2 = 2$.

Suppose we want to ask whether $\sqrt{2} \in \mathbb{Q}$. In standard mathematics, this is equivalent to asking if there exist integers $n, m$ (with $m \neq 0$) such that $(n/m)^2 = 2$, or equivalently, $n^2 - 2m^2 = 0$.

We encode this into an existential sentence in $\mathcal{L}_{\sin}$ as follows:
$$ \phi \equiv \exists x, p \in \mathbb{R} : \left( p \neq 0 \land \sin(p) = 0 \land \sin(x) = 0 \land x^2 - 2p^2 = 0 \right) $$

**Step-by-Step Resolution in $\mathcal{R}_{\sin}$:**

1.  **Enforcing the Grid:** The condition $\sin(p) = 0 \land p \neq 0$ forces $p = m\pi$ for some non-zero integer $m \in \mathbb{Z} \setminus \{0\}$.
2.  **Variable Generation:** The condition $\sin(x) = 0$ forces $x = n\pi$ for some integer $n \in \mathbb{Z}$.
3.  **Polynomial Evaluation:** We substitute these restricted variables into the algebraic component of the formula:
    $$ (n\pi)^2 - 2(m\pi)^2 = 0 $$
    $$ n^2\pi^2 - 2m^2\pi^2 = 0 $$
4.  **Cancellation:** Because $m \neq 0$ and $\pi \neq 0$, we can divide the entire equation by $\pi^2$:
    $$ n^2 - 2m^2 = 0 \implies \left(\frac{n}{m}\right)^2 = 2 $$

Because no such integers $n, m$ exist (as $\sqrt{2}$ is irrational), the sentence $\phi$ is correctly evaluated as **False** in $\mathcal{R}_{\sin}$.

Notice that if the equation in the formula was instead $x^2 - 4p^2 = 0$, the algebraic reduction would yield $n^2 - 4m^2 = 0 \implies n = 2m$. Choosing $m=1 \implies p=\pi$ and $n=2 \implies x=2\pi$ satisfies all conditions, making the sentence **True**. 

This example illustrates the central technical bottleneck: because we cannot write an existential formula that strictly forces $p = 1\pi$ (which would require isolating $\pi$ exclusively, a task demanding a universal quantifier), we are forced to carry the arbitrary scaling factor $m$ through the entire equation, which irreversibly shifts the domain from the integers to the rationals.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*