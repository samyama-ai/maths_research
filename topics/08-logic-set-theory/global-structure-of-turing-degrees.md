---
id: 08-logic-set-theory/global-structure-of-turing-degrees
title: "Global Structure of Turing Degrees"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Structure of Turing Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/global-structure-of-turing-degrees` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathcal{D} = (\mathcal{D}, \leq_T)$ be the partial order of Turing degrees. The global structure problem asks for a complete algebraic and definability-theoretic description of $\mathcal{D}$. Three interlocking questions organize the area:

1. **Rigidity.** Is $\mathrm{Aut}(\mathcal{D})$ trivial? Equivalently, is every automorphism of $(\mathcal{D},\leq_T)$ the identity?
2. **Definability / Biinterpretability Conjecture (Slaman–Woodin).** Is $\mathcal{D}$ biinterpretable with second-order arithmetic $Z_2$ **without parameters**? Concretely: is there a first-order interpretation of a standard model $(\mathbb{N},+,\cdot,\mathcal{P}(\mathbb{N}))$ in $\mathcal{D}$, together with a definable map sending each degree $\mathbf{a}$ to the set of indices of reals in $\mathbf{a}$?
3. **Homogeneity (Sacks).** Is $\mathcal{D}(\geq \mathbf{a}) \cong \mathcal{D}$ for every $\mathbf{a}$, and is $\mathrm{Th}(\mathcal{D}(\geq\mathbf{a})) = \mathrm{Th}(\mathcal{D})$?

A resolution of (2) settles (1) and pins down the definable relations exactly: biinterpretability implies rigidity, and implies that a degree-invariant relation on $\mathcal{D}$ is definable **iff** it is definable in $Z_2$. Question (3) is answered negatively (Section 4); (1) and (2) are open.

A complete solution requires either a construction of a nontrivial automorphism (with a verified priority/forcing argument), or a proof that the parameter-free coding of arithmetic in $\mathcal{D}$ succeeds uniformly on all degrees, not merely above some cone base.

## 2. Mathematical Foundations

For $A, B \subseteq \mathbb{N}$, $A \leq_T B$ means $A$ is computable from $B$ by an oracle Turing machine. Turing equivalence $A \equiv_T B$ is $A\leq_T B \wedge B \leq_T A$; degrees are the classes $\mathbf{a} = \deg(A)$, ordered by $\leq_T$. The structure is an upper semilattice with least element $\mathbf{0} = \deg(\emptyset)$ and join
$$\deg(A) \vee \deg(B) = \deg(A \oplus B), \qquad A\oplus B = \{2n : n\in A\}\cup\{2n+1: n\in B\}.$$
$|\mathcal{D}| = 2^{\aleph_0}$; every degree has $\aleph_0$ predecessors; every countable subset has an upper bound, so $\mathcal{D}$ is not a lattice but is $\aleph_1$-directed-free of least upper bounds in general.

The **jump** is $\mathbf{a}' = \deg(A')$ where $A' = \{e : \Phi_e^A(e)\!\downarrow\}$; $\mathbf{a} < \mathbf{a}'$ and $\mathbf{a}\leq\mathbf{b} \Rightarrow \mathbf{a}'\leq\mathbf{b}'$. Iterates $\mathbf{0}^{(n)}$ stratify the arithmetic degrees.

**Cones.** $\mathcal{D}(\geq\mathbf{a}) = \{\mathbf{x} : \mathbf{x}\geq\mathbf{a}\}$. Martin's theorem: under $\mathsf{AD}$, the Turing-cone filter is an ultrafilter on the degree-invariant Borel sets, so every degree-invariant statement is true on a cone or fails on a cone.

**Coding and biinterpretability.** A *coding of arithmetic with parameters* is a tuple of formulas $\varphi_{\mathrm{dom}}, \varphi_{+},\varphi_{\times}, \varphi_{\in}$ and parameters $\bar{p}\in\mathcal{D}^{<\omega}$ such that the interpreted structure $\mathcal{M}(\bar p)$ is isomorphic to $(\mathbb{N},+,\cdot,\leq,\mathcal{P}(\mathbb{N}),\in)$. Biinterpretability with parameters additionally demands a formula $\psi(\mathbf{x}, n, \bar p)$ such that
$$\psi(\mathbf{x},n,\bar p) \iff n \text{ codes (in } \mathcal{M}(\bar p)) \text{ a real of degree } \mathbf{x}.$$
The **Biinterpretability Conjecture** asserts this holds with $\bar p = \emptyset$.

**Key relativizable facts used throughout:**
- *Kleene–Post/ Friedberg–Muchnik forcing:* finite-extension arguments build $A,B$ with $\deg(A)\mid\deg(B)$ below $\mathbf{0}'$.
- *Posner–Robinson (1981):* if $\mathbf{a} \neq \mathbf{0}$ then there is $\mathbf{g}$ with $\mathbf{a}\vee\mathbf{g} = \mathbf{g}' = \mathbf{0}'$; relativized, for $\mathbf{a}\not\leq\mathbf{x}$ there is $\mathbf{g}\geq \mathbf x$ with $\mathbf{a}\vee\mathbf{g} = \mathbf{g}'$.
- *Slaman–Woodin coding:* any countable relation on $\mathcal{D}$ is uniformly definable from finitely many parameters, via coding into an exact pair over a definable ideal.

## 3. History & State of the Art (SOTA)

- **1944.** Post poses the study of degrees of unsolvability; Post's problem opens the local theory.
- **1954.** Kleene and Post, *The upper semi-lattice of degrees of recursive unsolvability* (Ann. of Math.), initiate the structure theory: incomparable degrees below $\mathbf{0}'$, density failures, initial segment questions.
- **1956.** Spector constructs a minimal degree, showing $\mathcal{D}$ is not dense.
- **1960s–70s.** Initial-segment technology (Lachlan, Lerman, Lachlan–Lebeuf): every countable upper semilattice with least element embeds as an initial segment of $\mathcal{D}$. This yields undecidability of $\mathrm{Th}(\mathcal{D})$ (Lachlan 1968).
- **1977.** Simpson: $\mathrm{Th}(\mathcal{D},\leq_T)$ is recursively isomorphic to $\mathrm{Th}(Z_2)$, true second-order arithmetic. The theory is thus completely pinned down as a set — but the *definable relations* are not.
- **1979–81.** Failure of homogeneity: Feiner-style constructions plus Shore's work give $\mathbf{a}$ with $\mathrm{Th}(\mathcal{D}(\geq\mathbf{a}))\neq\mathrm{Th}(\mathcal{D})$; Shore (1981) shows $\mathrm{Th}(\mathcal{D}(\leq\mathbf{0}'))$ is undecidable and interprets true first-order arithmetic.
- **1986–90.** Slaman and Woodin prove: $\mathrm{Aut}(\mathcal{D})$ is countable; every automorphism is the identity on the cone above $\mathbf{0}''$; every automorphism is induced by an arithmetically definable map on reals; $\mathcal{D}$ is biinterpretable with $Z_2$ **with parameters**.
- **1999.** Shore and Slaman, *Defining the Turing jump* (Math. Res. Lett.): the map $\mathbf{a}\mapsto\mathbf{a}'$ is first-order definable in $(\mathcal{D},\leq_T)$, parameter-free, combining Slaman–Woodin coding with the relativized Posner–Robinson theorem.
- **1999–2000s.** Cooper announces a nontrivial automorphism of $\mathcal{D}$; the argument is not accepted by the community and no verified construction exists.
- **2007–present.** Shore's programme on definability of jump classes and ideals; Montalbán and others relate the analysis to computable structure theory and Martin's conjecture.

## 4. Partial Results / Verified Cases

- **Full theory identified.** $\mathrm{Th}(\mathcal{D}) \equiv_1 \mathrm{Th}(Z_2)$ (Simpson 1977); same for $\mathcal{D}$ with jump.
- **Rigidity above $\mathbf{0}''$.** Every $\pi\in\mathrm{Aut}(\mathcal{D})$ satisfies $\pi(\mathbf{x}) = \mathbf{x}$ for all $\mathbf{x}\geq\mathbf{0}''$ (Slaman–Woodin). Hence $|\mathrm{Aut}(\mathcal{D})|\leq\aleph_0$, and $\mathcal{D}(\geq \mathbf{0}'')$ is rigid and biinterpretable without parameters.
- **Jump definable.** $\{(\mathbf{a},\mathbf{b}) : \mathbf{b} = \mathbf{a}'\}$ is definable in $(\mathcal{D},\leq)$; consequently $\mathbf{0}^{(n)}$, the arithmetic degrees, the relation "$\mathbf{a}$ is arithmetic in $\mathbf{b}$", and $\mathcal{D}(\leq \mathbf{0}')$ as a set are definable (Shore–Slaman 1999).
- **Countable relations, with parameters.** Every countable degree-invariant relation is definable from parameters (Slaman–Woodin coding); hence *every* automorphism is arithmetic.
- **Homogeneity refuted.** There exist $\mathbf{a}$ (e.g. constructed by initial-segment coding of a nonstandard-looking ideal) with $\mathcal{D}(\geq\mathbf{a})\not\cong\mathcal{D}$; Shore showed $\mathrm{Th}(\mathcal{D}(\geq \mathbf a))$ can differ from $\mathrm{Th}(\mathcal{D})$, refuting Sacks' strong homogeneity conjecture.
- **Quantifier levels.** The $\exists$-theory of $(\mathcal{D},\leq,\vee)$ is decidable (finite usl embedding, Kleene–Post/Sacks); the $\forall\exists$-theory of $(\mathcal{D},\leq)$ is decidable (Lerman, via extension-of-embeddings for finite posets); the $\exists\forall\exists$-theory is undecidable.
- **Local analogues solved.** For the c.e. degrees $\mathcal{R}$: $\mathrm{Th}(\mathcal{R})\equiv$ true first-order arithmetic, and the jump classes $\mathrm{low}_n$, $\mathrm{high}_n$ ($n\geq 2$, plus $\mathrm{high}_1$) are definable (Nies–Shore–Slaman 1998). $\mathcal{R}$ is *not* known to be rigid either, but the coding technology is complete there with parameters.

## 5. Principal Obstacles

- **Parameters cannot be eliminated.** All known codings of arithmetic into $\mathcal{D}$ start from an exact pair or an independent set of parameters. Removing them requires a *definable* choice of a coding apparatus, but every candidate apparatus is only unique up to a countable ambiguity — exactly the ambiguity an automorphism could exploit.
- **The gap below $\mathbf{0}''$.** Slaman–Woodin rigidity is proved by pushing coding through the double jump; below $\mathbf{0}''$ the ideal used to code is not definable, and finite-extension/forcing constructions there are too flexible to constrain $\pi$.
- **Forcing is too generic.** Cohen and Sacks forcing over $\mathcal{D}$ produce degrees whose only structural properties are those forced generically; they cannot distinguish a degree from its automorphic image, so they yield no rigidity, only embeddings.
- **Priority arguments do not scale.** Infinite-injury machinery is calibrated to $\Sigma_3$-level requirements in $\mathcal{R}$; automorphism construction on $\mathcal{D}$ needs to control $2^{\aleph_0}$ degrees simultaneously and there is no known transfinite bookkeeping for it.
- **Descriptive-set-theoretic barrier.** Martin's conjecture (under $\mathsf{AD}$) says every degree-invariant function is, on a cone, an iterate of the jump. If true, it constrains automorphisms on a cone but says nothing off cones — and Martin's conjecture is itself open in the general case.

## 6. The Gap

Proven: biinterpretability **with parameters**, plus rigidity **on the cone above $\mathbf{0}''$**, plus definability of the jump. The general statement demands: (i) a formula $\theta(\bar x)$ that *defines* a suitable parameter tuple up to automorphism, or (ii) a direct argument that any $\pi\in\mathrm{Aut}(\mathcal{D})$ fixing all $\mathbf{x}\geq\mathbf{0}''$ also fixes each $\mathbf{a}<\mathbf{0}''$.

The exact step is: given $\pi$ trivial above $\mathbf{0}''$ and $\mathbf{a}$ arbitrary, show that the countable ideal $\mathcal{D}(\leq\mathbf{a})$ together with its coded copy of $\mathbb{N}$ recovers $A$ itself, uniformly and parameter-freely. Equivalently: strengthen Posner–Robinson-type "everything is a jump relative to something" theorems from the double-jump level to the single-degree level. Cooper's claimed automorphism would close the gap the other way; it remains unverified.

## 7. Current Research (as of June 2026)

- **Berkeley (Slaman, Woodin and students).** Continued refinement of coding: reducing the parameter count in the biinterpretability proof and analysing which ideals are definable. The stated target is biinterpretability from a *definable* parameter.
- **Cornell (Shore).** Definability of ideals, jump classes and $n$-REA degrees in $\mathcal{D}$ and $\mathcal{D}(\leq\mathbf{0}')$; surveys the programme in *The Turing degrees: an introduction* (2015).
- **Martin's conjecture line.** Lutz and Siskind, *Part 1 of Martin's conjecture for order-preserving and measure-preserving functions* (2021–2023), proved the first part of the conjecture for these restricted function classes — the strongest unconditional progress in decades, and directly relevant to constraining automorphisms on cones. *(frontier — verify current publication status)*
- **Reverse-mathematical calibration.** Work relating the strength of the Posner–Robinson theorem and of jump-definability arguments to subsystems of $Z_2$ (Shore–Slaman-style arguments formalized in $\mathsf{ATR}_0$-adjacent systems). *(frontier — verify)*
- **Status of Cooper's claim.** Still not accepted; no published refutation of a specific error, but no verification either. Treat $\mathcal{D}$ as neither known rigid nor known non-rigid.

## 8. Future Work

- Prove the **Biinterpretability Conjecture** by exhibiting a parameter-free definable coding; Slaman's suggested route is to define an $\omega$-model of $Z_2$ using the definability of the jump plus definable exact pairs.
- Settle the **local biinterpretability** question for $\mathcal{D}(\leq\mathbf{0}')$ and for $\mathcal{R}$: rigidity of $\mathcal{R}$ is a stated open problem with the same coding obstruction.
- Decide the **two-quantifier theory of $\mathcal{D}(\leq\mathbf{0}')$** — open, unlike the global case.
- Push **Martin's conjecture** past order-preserving functions; a full proof under $\mathsf{AD}$ would give that every automorphism is the identity on a cone by a purely descriptive-set-theoretic route.
- Determine whether **$\mathrm{Aut}(\mathcal{D})$ has a nontrivial element in some forcing extension** — an independence result would itself be a major outcome, since $\mathrm{Th}(\mathcal{D})$ is not absolute in obvious ways.

## 9. Key References

- **[Foundational]** S. C. Kleene and E. L. Post. *The upper semi-lattice of degrees of recursive unsolvability.* Annals of Mathematics 59 (1954), 379–407.
- **[Foundational]** C. Spector. *On degrees of recursive unsolvability.* Annals of Mathematics 64 (1956), 581–592.
- **[Foundational]** S. G. Simpson. *First-order theory of the degrees of recursive unsolvability.* Annals of Mathematics 105 (1977), 121–139.
- **[Foundational]** D. B. Posner and R. W. Robinson. *Degrees joining to $\mathbf{0}'$.* Journal of Symbolic Logic 46 (1981), 714–722.
- **[Foundational]** R. A. Shore. *The theory of the degrees below $\mathbf{0}'$.* Journal of the London Mathematical Society 24 (1981), 1–14.
- **[SOTA]** T. A. Slaman and W. H. Woodin. *Definability in the Turing degrees.* Illinois Journal of Mathematics 30 (1986), 320–334.
- **[SOTA]** R. A. Shore and T. A. Slaman. *Defining the Turing jump.* Mathematical Research Letters 6 (1999), 711–722.
- **[SOTA]** A. Nies, R. A. Shore and T. A. Slaman. *Interpretability and definability in the recursively enumerable degrees.* Proceedings of the London Mathematical Society 77 (1998), 241–291.
- **[SOTA / Recent]** P. Lutz and J. Siskind. *Part 1 of Martin's conjecture for order-preserving and measure-preserving functions.* arXiv preprint / Journal of Mathematical Logic, 2021–2023.
- **[Survey]** T. A. Slaman. *Global properties of the Turing degrees and the Turing jump.* In *Computational Prospects of Infinity*, World Scientific, 2008.
- **[Survey]** R. A. Shore. *The Turing degrees: an introduction.* In *Forcing, Iterated Ultrapowers, and Turing Degrees*, Lecture Notes Series, IMS NUS, World Scientific, 2015.
- **[Book]** R. I. Soare. *Turing Computability: Theory and Applications.* Springer, 2016.
- **[Book]** M. Lerman. *Degrees of Unsolvability: Local and Global Theory.* Springer, Perspectives in Mathematical Logic, 1983.

## 10. Worked Example / Concrete Special Case

**Goal.** Show concretely how Posner–Robinson converts a jump statement into an order statement — the engine of Shore–Slaman jump definability.

**Posner–Robinson theorem.** If $\mathbf{a}\neq\mathbf{0}$, there is $\mathbf{g}$ with
$$\mathbf{a}\vee\mathbf{g} = \mathbf{g}' = \mathbf{0}'.$$

*Construction sketch.* Fix $A\in\mathbf{a}$, $A\neq_T\emptyset$. Build $G$ by forcing with finite binary strings, using $\emptyset'$ to decide requirements, so that $G\leq_T\emptyset'$ and $A\oplus G\equiv_T \emptyset'$. Two requirement families:

- $R_e$ (jump control): at stage $2e$, with current condition $\sigma$, ask $\emptyset'$ whether $\exists\tau\supseteq\sigma$ with $\Phi_e^{\tau}(e)\!\downarrow$. If yes, extend to such $\tau$; if no, keep $\sigma$. This makes $G'\leq_T\emptyset'$.
- $S_n$ (coding $A$): at stage $2n+1$, append the block $0^{A(n)}1$ — i.e. code $A(n)$ into the length of a run of zeros. Then $A\leq_T G$ trivially would collapse the point, so instead one codes $A$ into *which* extension is taken among a pair of witnesses that only $A$ can distinguish, giving $\emptyset' \leq_T A\oplus G$ while $A\not\leq_T G$.

The output: $G$ is a "generic" set for which $A$ is exactly the extra information needed to compute $G'$.

**Why this matters.** Relativizing, for $\mathbf{a}\not\leq\mathbf{x}$ there is $\mathbf{g}\geq\mathbf{x}$ with $\mathbf{a}\vee\mathbf{g} = \mathbf{g}'$. So the *jump* of $\mathbf g$ — an operator not present in the language $\{\leq\}$ — is realized as a *join*, which is order-definable. Shore and Slaman combine this with Slaman–Woodin coding: inside a coded standard model $\mathcal{M}(\bar p)$ of arithmetic, "$\mathbf{b} = \mathbf{a}'$" becomes
$$\forall \mathbf{g}\,\big[\,\mathbf{g}\ \text{generic over the coded model and}\ \mathbf{a}\vee\mathbf{g} = \mathbf{g}'\ \text{witnessed in }\mathcal{M}(\bar p)\,\big] \Rightarrow \text{a first-order condition on } \mathbf{b},$$
and a further argument removes $\bar p$, yielding a parameter-free definition of the jump.

**Concrete instance.** Take $\mathbf{a} = \deg(K)$ where $K = \emptyset'$ — but $K\neq \mathbf{0}$, so Posner–Robinson applies to any nonzero degree, e.g. $\mathbf{a}$ minimal (Spector). Then there is $\mathbf{g}\leq\mathbf{0}'$ with $\mathbf{a}\vee\mathbf{g} = \mathbf{0}'$: a minimal degree, which has no nontrivial predecessors at all, nevertheless joins a suitable $\mathbf{g}$ up to $\mathbf{0}'$ and simultaneously $\mathbf{g}' = \mathbf{0}'$ (so $\mathbf g$ is low-jump-optimal). This single example already shows why order-theoretic data determines jump-theoretic data — and equally why an automorphism $\pi$ must permute these configurations coherently, which is precisely what the rigidity question asks about below $\mathbf{0}''$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*