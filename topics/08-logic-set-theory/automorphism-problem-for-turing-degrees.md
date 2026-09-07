---
id: 08-logic-set-theory/automorphism-problem-for-turing-degrees
title: "Automorphism Problem for Turing Degrees"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Automorphism Problem for Turing Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/automorphism-problem-for-turing-degrees` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{D} = (\mathcal{D}, \leq_T, \vee)$ be the upper semilattice of Turing degrees: equivalence classes of subsets of $\mathbb{N}$ under mutual Turing reducibility, ordered by relative computability.

**Question (Automorphism Problem).** Is $\mathrm{Aut}(\mathcal{D})$ trivial? That is, is every order-automorphism $\pi : \mathcal{D} \to \mathcal{D}$ the identity?

**Rigidity Conjecture.** $\mathcal{D}$ is rigid: $\mathrm{Aut}(\mathcal{D}) = \{\mathrm{id}\}$.

A complete resolution means either (a) a proof that $\pi(\mathbf{a}) = \mathbf{a}$ for all $\pi \in \mathrm{Aut}(\mathcal{D})$ and all $\mathbf{a} \in \mathcal{D}$, or (b) an explicit construction, verifiable in $\mathrm{ZFC}$, of a degree $\mathbf{a}$ and an automorphism $\pi$ with $\pi(\mathbf{a}) \neq \mathbf{a}$. Note that $\pi$ is required only to preserve $\leq_T$; preservation of $\vee$ is automatic (least upper bounds are order-definable), and preservation of the jump $\mathbf{a} \mapsto \mathbf{a}'$ is a theorem, not an assumption (Shore–Slaman 1999).

The parallel questions for the local structures $\mathcal{D}(\leq \mathbf{0}')$ (degrees below the halting problem) and $\mathcal{R}$ (computably enumerable degrees) are also open.

## 2. Mathematical Foundations

**Degrees.** For $A, B \subseteq \mathbb{N}$, write $A \leq_T B$ if $A$ is computable from an oracle for $B$. Then $\equiv_T$ is $\leq_T \cap \geq_T$, $\mathcal{D} = 2^{\mathbb{N}}/\!\equiv_T$, and $\deg(A) \vee \deg(B) = \deg(A \oplus B)$ where $A \oplus B = \{2n : n \in A\} \cup \{2n+1 : n \in B\}$. The structure has least element $\mathbf{0} = \deg(\emptyset)$, cardinality $2^{\aleph_0}$, every element has countably many predecessors, and every countable subset has an upper bound.

**Jump.** $A' = \{e : \Phi_e^A(e)\!\downarrow\}$; $\mathbf{a}' = \deg(A')$ is well defined, $\mathbf{a} <_T \mathbf{a}'$, and $\mathbf{a} \leq_T \mathbf{b} \Rightarrow \mathbf{a}' \leq_T \mathbf{b}'$. Iterates: $\mathbf{0}^{(n)}$.

**Cones and Martin measure.** The cone above $\mathbf{a}$ is $\mathcal{D}(\geq \mathbf{a}) = \{\mathbf{b} : \mathbf{b} \geq_T \mathbf{a}\}$. Under $\mathrm{AD}$, and for Borel sets in $\mathrm{ZFC}$ (Martin), every degree-invariant set contains or is disjoint from a cone; "on a cone" is the natural almost-everywhere quantifier here.

**Coding and interpretability.** Slaman and Woodin showed how to code arbitrary countable relations into $\mathcal{D}$ by finitely many parameters: for each countable $\mathcal{M} = (M, R)$ there are parameters $\bar{p}$ such that $\mathcal{M}$ is isomorphic to a structure first-order definable in $\mathcal{D}$ from $\bar{p}$. Combined with Simpson's interpretation of arithmetic, this yields
$$\mathrm{Th}(\mathcal{D}) \equiv_1 \mathrm{Th}(\mathcal{Z}_2),$$
i.e. the first-order theory of $\mathcal{D}$ is recursively isomorphic to true second-order arithmetic (Simpson 1977; Nerode–Shore 1980).

**Biinterpretability Conjecture (Slaman–Woodin).** $\mathcal{D}$ is biinterpretable with $\mathcal{Z}_2$ with parameters: there are parameters $\bar{p}$ and a definable copy $\mathcal{N}_{\bar{p}} \cong (\mathbb{N}, +, \times)$ inside $\mathcal{D}$ such that the relation
$$\{(\mathbf{x}, i) : i \in \mathcal{N}_{\bar{p}} \text{ codes a set } X \text{ with } \deg(X) = \mathbf{x}\}$$
is definable in $\mathcal{D}$ from $\bar{p}$. **Key implication:** biinterpretability with parameters $\Rightarrow$ $\mathcal{D}$ is rigid, and moreover a relation on $\mathcal{D}$ is definable iff it is degree-invariant and definable in $\mathcal{Z}_2$.

## 3. History & State of the Art (SOTA)

- **1944–1954.** Post and Kleene–Post initiate the study of $\mathcal{D}$ as an algebraic object; Kleene–Post produce incomparable degrees below $\mathbf{0}'$ by finite-extension forcing.
- **1963/1966.** Sacks, *Degrees of Unsolvability*, sets the global programme; the homogeneity and automorphism questions are explicitly circulated (Sacks' problem list asks whether $\mathcal{D} \cong \mathcal{D}(\geq \mathbf{a})$ for all $\mathbf{a}$).
- **1977.** Simpson: $\mathrm{Th}(\mathcal{D})$ is recursively isomorphic to $\mathrm{Th}(\mathcal{Z}_2)$ — the structure is maximally complicated, which is evidence *for* rigidity (a rich structure has little room for symmetry).
- **1977.** Jockusch–Solovay: any automorphism commuting with the jump is the identity on the cone above $\mathbf{0}^{(4)}$; hence jump-preserving automorphisms are highly constrained.
- **1980.** Nerode–Shore: homogeneity fails ($\mathcal{D} \not\cong \mathcal{D}(\geq \mathbf{a})$ for suitable $\mathbf{a}$), and $\mathrm{Aut}(\mathcal{D})$ acts trivially on a cone if it acts trivially on a sufficiently definable set.
- **1981.** Jockusch–Posner: automorphism bases — the minimal degrees, and various other small classes, determine any automorphism.
- **1986.** Slaman–Woodin: the coding theorem; $|\mathrm{Aut}(\mathcal{D})| \leq \aleph_0$, every automorphism is arithmetically definable, and every automorphism is the identity on the cone above $\mathbf{0}''$.
- **1997–2001.** Cooper announces a nontrivial automorphism of $\mathcal{D}$ (and of $\mathcal{R}$). The construction has never been accepted by the community; no refereed proof exists and the consensus is that it is not established.
- **1999.** Shore–Slaman: the Turing jump is first-order definable in $\mathcal{D}$, using the Slaman–Woodin coding plus the Kumabe–Slaman theorem on degree-invariant functions. Consequence: every automorphism preserves the jump, so Jockusch–Solovay applies unconditionally.

**SOTA summary.** Rigidity holds "above $\mathbf{0}''$"; the automorphism group is countable, arithmetic, and jump-preserving; full rigidity is equivalent (modulo the Slaman–Woodin programme) to the Biinterpretability Conjecture.

## 4. Partial Results / Verified Cases

| Result | Statement | Source |
|---|---|---|
| Cone rigidity | Every $\pi \in \mathrm{Aut}(\mathcal{D})$ satisfies $\pi(\mathbf{a}) = \mathbf{a}$ for all $\mathbf{a} \geq_T \mathbf{0}''$ | Slaman–Woodin 1986 |
| Countability | $|\mathrm{Aut}(\mathcal{D})| \leq \aleph_0$; each $\pi$ has an arithmetic presentation | Slaman–Woodin 1986 |
| Jump preservation | $\pi(\mathbf{a}') = \pi(\mathbf{a})'$; $\pi(\mathbf{0}^{(n)}) = \mathbf{0}^{(n)}$ | Shore–Slaman 1999 |
| Jump-preserving case | Jump-preserving automorphisms fix the cone above $\mathbf{0}^{(4)}$ | Jockusch–Solovay 1977 |
| Automorphism bases | $\pi$ determined by its action on the minimal degrees; also by $\mathcal{D}(\leq \mathbf{0}')$-type bases | Jockusch–Posner 1981 |
| Definable classes fixed | Every definable degree is fixed: $\mathbf{0}$, $\mathbf{0}^{(n)}$, $\mathbf{0}^{(\alpha)}$ for recursive $\alpha$ (via jump definability + Spector) | Shore–Slaman 1999 |
| Local structures | Biinterpretability with parameters holds for $\mathcal{R}$ *up to* the definability of the relevant coding; jump classes $\mathrm{low}_n$, $\mathrm{high}_n$ are definable in $\mathcal{R}$ | Nies–Shore–Slaman 1998 |
| Countable substructures | Every countable upper semilattice with least element embeds in $\mathcal{D}$ preserving $\vee$; so no local finite configuration can obstruct symmetry | Sacks 1963 |

The unsettled region is therefore exactly $\mathcal{D} \setminus \mathcal{D}(\geq \mathbf{0}'')$ — a set of size $2^{\aleph_0}$ that includes all of $\mathcal{D}(\leq \mathbf{0}')$ and all minimal degrees.

## 5. Principal Obstacles

- **Coding needs parameters that are too high.** The Slaman–Woodin coding of a model of arithmetic into $\mathcal{D}$ requires parameters whose join computes $\mathbf{0}''$-like information. Below $\mathbf{0}''$ one cannot in general recover, from the order alone, a copy of $\mathbb{N}$ together with the "$\mathbf{x}$ is the degree of the set coded by $i$" relation. Removing the parameters is exactly the Biinterpretability Conjecture.
- **No definable point below $\mathbf{0}'$ is known.** Every rigidity argument so far bootstraps from definable anchors ($\mathbf{0}$, the jump). Below $\mathbf{0}'$ there is no known individually definable degree other than $\mathbf{0}$, so there is nothing to anchor an induction on.
- **Forcing constructions are symmetric by design.** Minimal degrees, exact pairs, and initial-segment embeddings are all built by Spector/Sacks forcing with perfect trees; these constructions are homogeneous and produce configurations that look alike from inside the order. Techniques that build structure cannot simultaneously certify that no relabelling of what was built is order-preserving.
- **Initial-segment richness cuts against definability.** Every countable upper semilattice is an initial segment of $\mathcal{D}$ (Lachlan–Lerman, Lerman). A local isomorphism-invariant cannot distinguish two copies of the same initial segment placed at different points.
- **Priority/tree-of-strategies methods are inherently local.** Finite-injury and $0'''$-priority arguments settle facts within a fixed cone or within $\mathcal{R}$; they give no leverage on a global symmetry of a size-$2^{\aleph_0}$ structure.
- **Failed disproof attempts are informative.** Cooper's announced nontrivial automorphism would have to be arithmetic (Slaman–Woodin) and jump-preserving (Shore–Slaman) and fix everything above $\mathbf{0}''$ — an extremely narrow target that no accepted construction has hit.

## 6. The Gap

Proven: $\pi \upharpoonright \mathcal{D}(\geq \mathbf{0}'') = \mathrm{id}$, $\pi$ jump-preserving, $\mathrm{Aut}(\mathcal{D})$ countable and arithmetic.

Wanted: $\pi \upharpoonright \mathcal{D} = \mathrm{id}$.

The gap is a single step: **eliminate the parameters from the Slaman–Woodin coding.** Formally, one must show that there is a first-order formula $\varphi(\mathbf{x}, i)$ — without parameters, or with parameters that are themselves definable — expressing that $\mathbf{x}$ is the degree of the set with index $i$ in a definable copy of $\mathbb{N}$. Equivalently: show that for every $\mathbf{a} \not\geq_T \mathbf{0}''$, some order-theoretic configuration around $\mathbf{a}$ determines a real representative of $\mathbf{a}$ up to $\equiv_T$. Given that, $\pi$ fixes every degree because it fixes the coded reals pointwise. Conversely, a nontrivial automorphism refutes biinterpretability with parameters and shows some degree-invariant arithmetic relation is undefinable in $\mathcal{D}$.

## 7. Current Research (as of June 2026)

- **Berkeley (Slaman) and Cornell/Chicago (Shore, and students).** Continued development of the Slaman–Woodin definability programme; the long-awaited monograph *Definability in Degree Structures* remains the reference manuscript. Focus: pushing cone rigidity below $\mathbf{0}''$ by refining the coding with pseudo-jump and Posner–Robinson techniques. *(frontier — verify)*
- **Martin's Conjecture interface.** Work on degree-invariant functions (Kumabe–Slaman, Steel, Slaman–Steel; more recently Marks, Monin–Patey, Lutz) treats the "on a cone" behaviour of order-preserving maps. A proof of Martin's Conjecture for Borel order-preserving functions would classify all uniformly degree-invariant self-maps of $\mathcal{D}$ and directly constrain $\mathrm{Aut}(\mathcal{D})$ under determinacy hypotheses. *(frontier — verify)*
- **Local structures.** Definability in $\mathcal{R}$ and $\mathcal{D}(\leq \mathbf{0}')$ (Nies–Shore–Slaman line, continued by Shore's students and the Singapore/NUS group around Yu and Wu): whether $\mathcal{R}$ has a nontrivial automorphism remains open and is regarded as possibly easier or possibly harder than the global problem.
- **Descriptive set theory of $\mathcal{D}$.** Treating $\mathrm{Aut}(\mathcal{D})$ as a definable group and asking for a $\Sigma^1_1$ or Borel bound on its complexity; also whether $\mathrm{Aut}(\mathcal{D})$ can be shown trivial in $L$ or under $\mathrm{AD}^{L(\mathbb{R})}$ but not in $\mathrm{ZFC}$ — no independence result is known, and most researchers expect none.

## 8. Future Work

- **Prove biinterpretability with parameters, then eliminate parameters.** Slaman's stated route: strengthen the coding so that the parameters can be chosen from a definable class, then quantify them away.
- **Find one definable degree strictly between $\mathbf{0}$ and $\mathbf{0}'$**, or prove none exists. Either outcome reshapes the problem.
- **Extend cone rigidity to $\mathbf{0}'$.** Replace uses of $\mathbf{0}''$ in the coding with $\mathbf{0}'$-level approximations (pseudo-jump inversion, Posner–Robinson at the $\Delta^0_2$ level).
- **Settle Martin's Conjecture** for Borel functions; its part-I statement (every non-increasing-on-a-cone function is constant on a cone) would rule out large families of candidate automorphisms.
- **Automorphism bases with definable closure.** Sharpen Jockusch–Posner: find an automorphism base each of whose members is definable from a definable set of parameters.
- **Machine-checked audit of announced counterexamples.** Formalising the Slaman–Woodin constraints (arithmetic, jump-preserving, fixing the cone above $\mathbf{0}''$) gives a checklist against which any future nontriviality claim can be tested quickly.

## 9. Key References

- **[Foundational]** G. E. Sacks. *Degrees of Unsolvability.* Annals of Mathematics Studies 55, Princeton University Press, 1963 (2nd ed. 1966).
- **[Foundational]** S. G. Simpson. *First-order theory of the degrees of recursive unsolvability.* Annals of Mathematics 105 (1977), 121–139.
- **[Foundational]** C. G. Jockusch, Jr. and R. M. Solovay. *Fixed points of jump preserving automorphisms of degrees.* Journal of Symbolic Logic 42 (1977), 782–785.
- **[Foundational]** A. Nerode and R. A. Shore. *Reducibility orderings: theories, definability and automorphisms.* Annals of Mathematical Logic 18 (1980), 61–89.
- **[Foundational]** C. G. Jockusch, Jr. and D. B. Posner. *Automorphism bases for degrees of unsolvability.* Israel Journal of Mathematics 40 (1981), 150–164.
- **[Key]** T. A. Slaman and W. H. Woodin. *Definability in the Turing degrees.* Illinois Journal of Mathematics 30 (1986), 320–334.
- **[SOTA]** R. A. Shore and T. A. Slaman. *Defining the Turing jump.* Mathematical Research Letters 6 (1999), 711–722.
- **[SOTA]** A. Nies, R. A. Shore and T. A. Slaman. *Interpretability and definability in the recursively enumerable degrees.* Proceedings of the London Mathematical Society (3) 77 (1998), 241–291.
- **[SOTA]** T. A. Slaman. *Global properties of the Turing degrees and the Turing jump.* In *Computational Prospects of Infinity, Part I: Tutorials*, Lecture Notes Series, IMS, NUS, vol. 14, World Scientific, 2008, 83–101.
- **[Survey]** R. A. Shore. *Degree structures: local and global investigations.* Bulletin of Symbolic Logic 12 (2006), 369–389.
- **[Survey]** P. Odifreddi. *Classical Recursion Theory, Volume II.* Studies in Logic and the Foundations of Mathematics 143, North-Holland, 1999.
- **[Reference]** M. Lerman. *Degrees of Unsolvability: Local and Global Theory.* Perspectives in Mathematical Logic, Springer, 1983.
- **[Disputed]** S. B. Cooper. *The Turing universe is not rigid.* Unpublished preprint, University of Leeds, 1997. (Announced nontrivial automorphism; never accepted or published in refereed form.)

## 10. Worked Example / Concrete Special Case

**Claim.** Let $\pi \in \mathrm{Aut}(\mathcal{D})$. Then $\pi$ fixes $\mathbf{0}$, fixes every $\mathbf{0}^{(n)}$, maps minimal degrees to minimal degrees, and is completely determined by its restriction to the minimal degrees.

*Step 1 — $\pi(\mathbf{0}) = \mathbf{0}$.* $\mathbf{0}$ is the unique degree satisfying the parameter-free formula $\varphi_0(\mathbf{x}) \equiv \forall \mathbf{y}\,(\mathbf{x} \leq \mathbf{y})$. Order-automorphisms preserve definable elements, so $\pi(\mathbf{0}) = \mathbf{0}$.

*Step 2 — $\pi(\mathbf{0}^{(n)}) = \mathbf{0}^{(n)}$.* Shore–Slaman (1999) give a formula $\psi(\mathbf{x}, \mathbf{y})$ with $\mathcal{D} \models \psi(\mathbf{x}, \mathbf{y}) \iff \mathbf{y} = \mathbf{x}'$. Hence $\pi(\mathbf{x}') = \pi(\mathbf{x})'$. By Step 1 and induction, $\pi(\mathbf{0}^{(n)}) = \pi(\mathbf{0})^{(n)} = \mathbf{0}^{(n)}$.

*Step 3 — minimality is order-theoretic.* $\mathbf{m}$ is minimal iff
$$\mathcal{D} \models \mathbf{m} \neq \mathbf{0} \ \wedge\ \forall \mathbf{x}\,(\mathbf{x} \leq \mathbf{m} \rightarrow \mathbf{x} = \mathbf{0} \vee \mathbf{x} = \mathbf{m}).$$
This uses only $\leq$, so $\pi$ permutes the set $\mathcal{M}$ of minimal degrees. Such degrees exist by Spector's 1956 perfect-tree forcing: build a sequence of computable perfect trees $T_0 \supseteq T_1 \supseteq \cdots$, where $T_{n+1}$ either forces $\Phi_n^G$ to be partial, or forces it computable, or makes $T_{n+1}$ *$e$-splitting* so that $G$ is computable from $\Phi_n^G$; the unique $G \in \bigcap_n [T_n]$ then has minimal degree.

*Step 4 — determination.* Every degree $\mathbf{a} \geq_T \mathbf{0}''$ is the join $\mathbf{m}_1 \vee \mathbf{m}_2$ of two minimal degrees (Posner; see Odifreddi, Vol. II). Since $\pi$ preserves joins ($\vee$ is the order-theoretic least upper bound), $\pi(\mathbf{a}) = \pi(\mathbf{m}_1) \vee \pi(\mathbf{m}_2)$. Jockusch–Posner (1981) upgrade this: $\mathcal{M}$ is an *automorphism base*, so $\pi \upharpoonright \mathcal{M} = \mathrm{id}$ forces $\pi = \mathrm{id}$ on all of $\mathcal{D}$.

*What is missing.* Take two minimal degrees $\mathbf{m}_1 = \deg(G_1)$ and $\mathbf{m}_2 = \deg(G_2)$ built by Spector forcing over different generic paths. Every finite (indeed every countable) order-theoretic configuration realised around $\mathbf{m}_1$ is realised around $\mathbf{m}_2$: both have initial segment $\{\mathbf{0}, \mathbf{m}_i\}$, both are cappable, both sit below cones isomorphic to $\mathcal{D}$. Nothing in the currently available toolkit distinguishes them by an order-theoretic formula. The Biinterpretability Conjecture asserts that the Slaman–Woodin coding, run with the right parameters, recovers $G_1$ and $G_2$ themselves from the order — and hence separates them. That single unproved step is the whole problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*