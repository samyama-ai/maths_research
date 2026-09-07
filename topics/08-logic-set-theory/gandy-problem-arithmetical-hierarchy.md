---
id: 08-logic-set-theory/gandy-problem-arithmetical-hierarchy
title: "Gandy's Problem on the Arithmetical Hierarchy"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gandy's Problem on the Arithmetical Hierarchy

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/gandy-problem-arithmetical-hierarchy` · **Status:** open

## 1. Problem Statement / Conjecture

Call a real $x \in 2^{\omega}$ an **arithmetical singleton** if the one-element set $\{x\}$ is arithmetically definable, i.e. $\{x\} = \{y : \mathcal{N} \models \varphi(y)\}$ for some formula $\varphi$ of second-order arithmetic with only number quantifiers and a single free set variable. If $\varphi$ can be taken $\Pi^0_n$, call $x$ a **$\Pi^0_n$ singleton**.

Gandy's problem, in the form circulated in recursion theory since about 1960, asks for a structural characterization of this class:

1. **(Level collapse.)** Does the hierarchy of $\Pi^0_n$ singletons collapse at a finite level — concretely, is every arithmetical singleton already a $\Pi^0_3$ singleton?
2. **(Degree characterization.)** Which Turing degrees contain arithmetical singletons? Is every arithmetical singleton Turing-equivalent to a jump hierarchy $H_a$ along some recursive well-ordering, and conversely is every hyperarithmetical degree the degree of an arithmetical singleton?

A complete solution is either a proof that the $\Pi^0_n$-singleton hierarchy is proper (an explicit $x$ that is a $\Pi^0_{n+1}$ but not a $\Pi^0_n$ singleton, for each $n \ge 3$), together with an exact description of $\{\deg_T(x) : x \text{ an arithmetical singleton}\}$; or a proof of collapse at level 3 with the matching degree characterization.

*Attribution note:* the questions are recorded as folklore attributed to R. O. Gandy, arising from his 1960 hierarchy work; no single paper of Gandy's states them in exactly this form. The mathematics below is independent of the attribution.

## 2. Mathematical Foundations

**Arithmetical hierarchy.** For $A \subseteq \omega$, $A \in \Sigma^0_{n+1}$ iff there is a recursive relation $R$ with
$$A = \{k : \exists m_1 \forall m_2 \cdots Q m_{n+1}\, R(k, m_1,\dots,m_{n+1})\},$$
$\Pi^0_n = \operatorname{co}\text{-}\Sigma^0_n$, $\Delta^0_n = \Sigma^0_n \cap \Pi^0_n$. Post's theorem: $A \in \Sigma^0_{n+1} \iff A$ is r.e. in $0^{(n)}$, and $\Delta^0_{n+1} \iff A \le_T 0^{(n)}$. The same classification applies to subsets of $2^\omega$ with $x$ as a free set variable; there $\Pi^0_1$ classes are the effectively closed sets.

**Analytical classes.** $\Sigma^1_1$ = projections of arithmetical (equivalently $\Pi^0_1$) relations on $2^\omega$; $\Delta^1_1 = \Sigma^1_1 \cap \Pi^1_1$. Kleene: $\Delta^1_1 = \mathrm{HYP}$, the hyperarithmetical reals.

**Jump hierarchies.** For a recursive linear order $\prec$ on $\omega$, $x$ is a *jump hierarchy along $\prec$* iff
$$\forall n\ \Big( x^{[n]} = \big( \textstyle\bigoplus_{m \prec n} x^{[m]} \big)' \Big),$$
where $x^{[n]} = \{k : \langle n,k\rangle \in x\}$ and $'$ is the Turing jump. If $\prec$ is a well-order of type $\alpha < \omega_1^{\mathrm{CK}}$, the hierarchy exists and is unique, and its columns give $0^{(\beta)}$ for $\beta \le \alpha$; $H_a$ denotes the hierarchy set for a notation $a \in \mathcal{O}$.

**Key foundational theorem (uniqueness of $\Sigma^1_1$ singletons).** If $\{x\}$ is $\Sigma^1_1$ then $x \in \Delta^1_1$: from $\{x\} = A$ with $A$ nonempty $\Sigma^1_1$,
$$x(n) = k \iff \exists y\,(y \in A \wedge y(n)=k) \iff \forall y\,(y \in A \rightarrow y(n)=k),$$
giving $x$ both a $\Sigma^1_1$ and a $\Pi^1_1$ definition. Since arithmetical $\subseteq \Delta^1_1 \subseteq \Sigma^1_1$ as pointclasses, **every arithmetical singleton is hyperarithmetical**, hence $\le_T H_a$ for some $a \in \mathcal{O}$.

**Contrast with $\Pi^1_1$.** Kleene's $\mathcal{O}$ is a $\Pi^1_1$ singleton and is not hyperarithmetical, so the argument above is sharp: uniqueness upgrades definability only up to $\Sigma^1_1$.

## 3. History & State of the Art (SOTA)

- **1943–1947.** Kleene ("Recursive predicates and quantifiers") and Mostowski ("On definable sets of positive integers") independently introduce the arithmetical hierarchy and prove it proper: $\Sigma^0_n \ne \Pi^0_n$ for all $n \ge 1$, via the universal-set/diagonal argument.
- **1955.** Kleene proves $\Delta^1_1 = \mathrm{HYP}$ and develops $\mathcal{O}$, making "definable by a unique-solution condition" a natural refinement of "definable".
- **1960.** Gandy's hierarchy papers ("Proof of Mostowski's conjecture"; with Kreisel and Tait, "Set existence"; "On a problem of Kleene's") isolate the theme that *uniqueness of solution* is a definability resource distinct from complexity of the defining formula. The singleton questions belong to this circle.
- **1967–1978.** Rogers's textbook and Hinman's *Recursion-Theoretic Hierarchies* codify singletons as a pointclass invariant; the Gandy basis theorem (every nonempty $\Sigma^1_1$ set has a member $x$ with $\omega_1^x = \omega_1^{\mathrm{CK}}$) becomes the standard tool at the $\Sigma^1_1$ level.
- **1970s.** Enderton–Putnam (JSL 1970) and Jockusch–Simpson (Ann. Math. Logic 1976) give degree-theoretic results on $0^{(\omega)}$ and on definability of hierarchies from degrees, supplying the only known lower-bound techniques for singleton degrees.
- **1990–2009.** Sacks's *Higher Recursion Theory* and Simpson's *Subsystems of Second Order Arithmetic* fix the modern framework: existence of jump hierarchies along all well-orderings is equivalent to $\mathrm{ATR}_0$ over $\mathrm{RCA}_0$, which places the whole question inside reverse mathematics.

State of the art: the *upper* bound (arithmetical singleton $\Rightarrow$ hyperarithmetical) and the *lower* construction ($H_a$ is a $\Pi^0_3$ singleton for every $a$) are classical and match in strength at the level of cofinality in $\mathrm{HYP}$. Nothing between them — neither a collapse theorem nor a properness theorem for $n \ge 3$ — is known.

## 4. Partial Results / Verified Cases

- **$n = 1$ in Cantor space (solved).** If $\{x\} \subseteq 2^\omega$ is $\Pi^0_1$, then $x$ is recursive. Proof: $\{x\}$ is the set of paths through a recursive tree $T$; uniqueness plus compactness makes $\{\sigma \in T : \sigma \text{ extendible}\}$ decidable, so $x$ is computed by following $T$.
- **$n = 2$ (solved, level by level).** For every $n$, $0^{(n)}$ is a $\Delta^0_{n+1}$ singleton; conversely a $\Delta^0_{n+1}$ singleton is $\le_T 0^{(n)}$ by Post's theorem. Thus at the $\Delta$-levels the singleton notion is exactly the arithmetical reals, and the classification is complete.
- **$n = 3$ (lower bound, all recursive ordinals).** For every recursive well-order $\prec$ of type $\alpha < \omega_1^{\mathrm{CK}}$, the jump hierarchy along $\prec$ is a $\Pi^0_3$ singleton (§10). Hence $\{0^{(\alpha)} : \alpha < \omega_1^{\mathrm{CK}}\}$ lies inside the $\Pi^0_3$ singletons, and the arithmetical singletons are cofinal in the hyperarithmetical degrees.
- **Upper bound (all $n$).** Every arithmetical singleton is $\Delta^1_1$, hence $\le_T H_a$ for some $a \in \mathcal{O}$, and the class of arithmetical singletons is countable.
- **Relativized and reverse-math cases.** Over $\mathrm{ATR}_0$ the uniqueness argument for hierarchies along arbitrary well-orderings is available; over $\mathrm{ACA}_0$ alone it is not, and the $\Pi^0_3$ singleton of §10 may be empty in an $\omega$-model of $\mathrm{ACA}_0$.

## 5. Principal Obstacles

- **No diagonalization at the singleton level.** Properness of $\Sigma^0_n$ vs. $\Pi^0_n$ comes from a universal set plus diagonalization. Singletons are not closed under the operations diagonalization needs: the family of $\Pi^0_n$ *singletons* is not itself uniformly $\Pi^0_n$-parametrized, because "the $e$-th $\Pi^0_n$ class has exactly one element" is $\Pi^1_1$-hard in general. The standard hierarchy machine has no traction.
- **Forcing and genericity destroy uniqueness.** Cohen/Sacks-style forcing, the main source of separations in the arithmetical degrees, produces sets with continuum-many conjugates; a generic real is never a singleton of anything. Every construction that would separate levels must be *rigid*, and the only known rigidifying device is jump-hierarchy uniqueness, which lands at level 3 and no higher.
- **Basis theorems are one level too coarse.** The Gandy basis theorem and the Kleene basis theorem give members of $\Sigma^1_1$ sets with controlled $\omega_1^x$, but they say nothing about the *arithmetical* complexity of the defining condition; they cannot distinguish a $\Pi^0_3$ from a $\Pi^0_7$ singleton.
- **Priority arguments are the wrong tool.** Finite- and infinite-injury constructions build sets by approximations that are stable only in the limit; they yield $\Delta^0_2$-type objects whose defining conditions have many solutions, so they cannot certify singleton-ness.
- **Absoluteness cuts both ways.** The property "$\{x\}$ is $\Pi^0_n$" is arithmetical in $x$ and hence absolute between $\omega$-models, so no independence/forcing argument over $\mathrm{ZFC}$ can settle it — the problem is a genuine theorem-or-refutation, not a candidate for independence.

## 6. The Gap

Proven: arithmetical singleton $\Rightarrow$ hyperarithmetical, and $\Pi^0_3$ singletons already realize every $H_a$, $a \in \mathcal{O}$. Open: whether any *additional* real becomes uniquely arithmetically definable at levels $\Pi^0_4, \Pi^0_5, \dots$

The missing step is a **transfer or separation lemma for uniqueness**: given a $\Pi^0_{n+1}$ condition $\varphi(x)$ with a unique solution, either (a) uniformly convert it into a $\Pi^0_3$ condition with the same unique solution — which would require replacing the extra quantifier alternations by a hierarchy-style fixed-point recursion, and no such normal form is known; or (b) construct a real whose unique definition provably needs $n+1$ alternations, which requires a rigidity-preserving diagonalization, i.e. a diagonal argument compatible with the object being the *only* solution. Neither direction has a known prototype. The degree question inherits the same gap: showing that some hyperarithmetical degree contains no arithmetical singleton would require a lower-bound method for "no unique arithmetical definition", of which none exists.

## 7. Current Research (as of June 2026)

- **Reverse mathematics of jump hierarchies.** Groups working in the Simpson–Shore tradition (Penn State, Cornell, Notre Dame, Berkeley) study exactly which well-orderings admit hierarchies in which $\omega$-models; this calibrates part 2 of the problem inside the $\mathrm{ACA}_0^+$/$\mathrm{ATR}_0$ interval.
- **Computable structure theory.** Ash–Knight-style $\alpha$-systems and Montalbán's work on "true stage" arguments give the most flexible currently available machinery for producing rigid objects at transfinite levels; adapting true-stage constructions to certify unique arithmetical definability is an active line *(frontier — verify)*.
- **Effective descriptive set theory.** Refinements of the Gandy–Harrington topology are being pushed downward toward the arithmetical pointclasses, aiming at level-by-level basis theorems *(frontier — verify)*.
- **Nonstandard-model methods.** Work relating arithmetical singletons to the standard system of models of $\mathrm{PA}$ (Kossak–Schmerl school) reformulates part 2 as a question about which sets are coded in every model of a given arithmetical theory *(frontier — verify)*.

## 8. Future Work

1. Seek a **normal form for uniquely-satisfiable arithmetical formulas**: prove or refute that every arithmetical singleton is the unique solution of a "hierarchy-like" $\Pi^0_3$ recursion, the analogue of Kleene normal form for singleton conditions.
2. Develop a **rigid diagonalization**, e.g. by a fixed-point/self-reference construction that manufactures a unique solution at level $n+1$ while defeating all $\Pi^0_n$ conditions with a unique solution.
3. Settle the **degree side first**: decide whether every arithmetical singleton is $\equiv_T H_a$ for some $a$, using Enderton–Putnam-style join theorems on $0^{(\omega)}$ and $0^{(\alpha)}$.
4. Study the **relativized problem** $\Pi^0_n(z)$ singletons for $z$ ranging over the hyperarithmetical reals; a uniform answer would likely propagate to the unrelativized case.
5. Calibrate the whole question in **reverse mathematics**: locate the statement "every arithmetical singleton is a $\Pi^0_3$ singleton" among the standard subsystems.

## 9. Key References

- **[Foundational]** S. C. Kleene. *Recursive predicates and quantifiers.* Transactions of the American Mathematical Society 53 (1943), 41–73.
- **[Foundational]** A. Mostowski. *On definable sets of positive integers.* Fundamenta Mathematicae 34 (1947), 81–112.
- **[Foundational]** S. C. Kleene. *Arithmetical predicates and function quantifiers.* Transactions of the American Mathematical Society 79 (1955), 312–340.
- **[Foundational]** R. O. Gandy. *Proof of Mostowski's conjecture.* Bulletin de l'Académie Polonaise des Sciences 8 (1960), 571–575.
- **[Foundational]** R. O. Gandy, G. Kreisel, W. W. Tait. *Set existence.* Bulletin de l'Académie Polonaise des Sciences 8 (1960), 577–582.
- **[Foundational]** H. Rogers, Jr. *Theory of Recursive Functions and Effective Computability.* McGraw-Hill, 1967.
- **[Survey]** P. G. Hinman. *Recursion-Theoretic Hierarchies.* Springer (Perspectives in Mathematical Logic), 1978.
- **[Survey]** G. E. Sacks. *Higher Recursion Theory.* Springer (Perspectives in Mathematical Logic), 1990.
- **[Survey]** P. Odifreddi. *Classical Recursion Theory*, Vols. I–II. North-Holland, 1989 and 1999.
- **[SOTA / Recent]** H. B. Enderton, H. Putnam. *A note on the hyperarithmetical hierarchy.* Journal of Symbolic Logic 35 (1970), 429–430.
- **[SOTA / Recent]** C. G. Jockusch, Jr., S. G. Simpson. *A degree-theoretic definition of the ramified analytical hierarchy.* Annals of Mathematical Logic 10 (1976), 1–32.
- **[SOTA / Recent]** C. J. Ash, J. F. Knight. *Computable Structures and the Hyperarithmetical Hierarchy.* Elsevier, 2000.
- **[SOTA / Recent]** S. G. Simpson. *Subsystems of Second Order Arithmetic*, 2nd ed. Cambridge University Press, 2009.
- **[Reference]** A. S. Kechris. *Classical Descriptive Set Theory.* Springer (GTM 156), 1995.
- **[Reference]** R. I. Soare. *Turing Computability: Theory and Applications.* Springer, 2016.

## 10. Worked Example / Concrete Special Case

**Claim.** Let $\prec$ be a recursive well-ordering of $\omega$ of order type $\alpha < \omega_1^{\mathrm{CK}}$. Then the jump hierarchy along $\prec$ is a $\Pi^0_3$ singleton.

*Definition.* Let $\varphi(x)$ say: $\forall n\ \big[\, x^{[n]} = \big(\bigoplus_{m \prec n} x^{[m]}\big)' \,\big]$.

*Complexity.* Fix $n$. Write $z_n = \bigoplus_{m \prec n} x^{[m]}$; membership $k \in z_n$ is recursive in $x$ (as $\prec$ is recursive), i.e. $\Delta^0_1(x)$. Now
$$x^{[n]} = z_n' \iff \forall e\,\big[\, e \in x^{[n]} \leftrightarrow \exists s\, T^{z_n}(e,e,s) \,\big],$$
where $T$ is Kleene's $T$-predicate and $T^{z_n}(e,e,s)$ is $\Delta^0_1(x)$. The bracket is a conjunction of $(\Sigma^0_1(x) \to \Sigma^0_1(x))$-type clauses, hence $\Delta^0_2(x)$; prefixing $\forall e$ and then $\forall n$ keeps it $\Pi^0_2(x)$. Allowing for the coding of $\oplus$ this is at worst $\Pi^0_3$ in $x$ with no parameters beyond the index of $\prec$. So $\{x : \varphi(x)\}$ is a $\Pi^0_3$ class.

*Uniqueness.* Suppose $\varphi(x)$ and $\varphi(y)$. By transfinite induction along $\prec$: if $x^{[m]} = y^{[m]}$ for all $m \prec n$, then $\bigoplus_{m\prec n} x^{[m]} = \bigoplus_{m \prec n} y^{[m]}$, and applying the jump gives $x^{[n]} = y^{[n]}$. Well-foundedness of $\prec$ makes the induction legitimate, so $x = y$.

*Existence.* Define $x^{[n]}$ by recursion on $\prec$; the recursion terminates because $\prec$ is a well-order (this step is exactly what $\mathrm{ATR}_0$ supplies and $\mathrm{ACA}_0$ does not).

*Consequence.* Taking $\prec$ of type $\omega$ gives $x \equiv_T 0^{(\omega)}$, a $\Pi^0_3$ singleton that is not arithmetical. Taking $\prec$ of type $\omega^\omega$, $\varepsilon_0$, etc., gives $\Pi^0_3$ singletons of degree $0^{(\omega^\omega)}$, $0^{(\varepsilon_0)}$, unbounded in $\mathrm{HYP}$. Meanwhile §2 caps every arithmetical singleton inside $\mathrm{HYP}$.

**The problem, in one line.** Level 3 already reaches the top of the known range and the $\Delta^1_1$ ceiling caps it — but no argument shows that levels $4, 5, \dots$ add nothing, and no construction shows that they add something. That single missing implication is Gandy's problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*