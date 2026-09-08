---
id: 08-logic-set-theory/automorphism-groups-of-countable-models-pa
title: "The Hartmanis–Stearns Style Problem for Nonstandard Models: Kaye's Question"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Hartmanis–Stearns Style Problem for Nonstandard Models: Kaye's Question

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/automorphism-groups-of-countable-models-pa` · **Status:** open

## 1. Problem Statement / Conjecture

The catalog title records the *shape* of the question, not a literal complexity-theoretic claim: as in Hartmanis–Stearns, one asks whether a coarse invariant of an object (there, the time complexity of a real number's expansion; here, the bare group-theoretic structure of a model's symmetries) already pins down the object itself. The mathematical content is **Kaye's reconstruction question** for models of Peano arithmetic, listed as an open problem in Kossak–Schmerl, *The Structure of Models of Peano Arithmetic* (2006), Ch. 6.

**Question (Kaye).** Let $M$ and $N$ be countable recursively saturated models of $\mathrm{PA}$. If
$$\mathrm{Aut}(M) \cong \mathrm{Aut}(N)$$
as **abstract groups** (no continuity assumed), must $M \cong N$?

A complete positive solution is a proof that the isomorphism type of a countable recursively saturated $M \models \mathrm{PA}$ is recoverable from the abstract group $\mathrm{Aut}(M)$. A complete negative solution is an explicit pair $M \not\cong N$ with $\mathrm{Aut}(M) \cong \mathrm{Aut}(N)$ — equivalently, two distinct Scott-set/theory pairs realized by models with abstractly isomorphic symmetry groups.

Two standing constraints make the question sharp. First, $\mathrm{Aut}(M)$ is a Polish group, and the *topological* group is known to be far more informative than the abstract one. Second, countable recursively saturated models are classified by two invariants (Section 2), so the question is exactly: **are $\mathrm{Th}(M)$ and $\mathrm{SSy}(M)$ definable from the group law alone?**

## 2. Mathematical Foundations

**Models and saturation.** $\mathrm{PA}$ is first-order Peano arithmetic in $\mathcal{L}_A=\{+,\cdot,<,0,1\}$. A model $M\models \mathrm{PA}$ is *recursively saturated* if every recursive type $p(x,\bar a)$ over a finite parameter tuple $\bar a \in M$ that is finitely satisfiable in $M$ is realized in $M$.

**Standard system.** Coding finite sets by the Ackermann/Gödel $\beta$-function, put
$$\mathrm{SSy}(M) \;=\; \bigl\{\, \{n\in\mathbb{N} : M\models n \in_{\mathrm{Ack}} a\,\} \;:\; a\in M \,\bigr\} \subseteq \mathcal{P}(\mathbb{N}).$$
For $M$ recursively saturated (indeed for any nonstandard $M \models \mathrm{PA}$), $\mathrm{SSy}(M)$ is a **Scott set**: closed under Turing reducibility and join, and satisfying weak König's lemma (every infinite binary tree in the set has a branch in the set). Necessarily $\mathrm{Th}(M) \in \mathrm{SSy}(M)$.

**Classification (Wilmers; Smoryński back-and-forth).** For countable recursively saturated $M,N \models \mathrm{PA}$,
$$M \cong N \iff \mathrm{Th}(M)=\mathrm{Th}(N) \ \text{ and } \ \mathrm{SSy}(M)=\mathrm{SSy}(N).$$
Conversely every pair $(T,S)$ with $T$ a completion of $\mathrm{PA}$, $S$ a countable Scott set, $T\in S$, is realized. There are $2^{\aleph_0}$ countable Scott sets, hence $2^{\aleph_0}$ such models.

**Arithmetic saturation.** $M$ is *arithmetically saturated* if it is recursively saturated and $\mathrm{SSy}(M)$ is closed under the Turing jump: $X\in \mathrm{SSy}(M) \Rightarrow X'\in \mathrm{SSy}(M)$.

**The group.** $\mathrm{Aut}(M)$ carries the topology of pointwise convergence; basic open sets are cosets of pointwise stabilizers
$$G_{(\bar a)}=\{g\in \mathrm{Aut}(M) : g(a_i)=a_i \ \forall i\},\qquad \bar a \in M^{<\omega},$$
making it a Polish group, closed in $\mathrm{Sym}(M)\cong \mathrm{Sym}(\omega)$, with $|\mathrm{Aut}(M)|=2^{\aleph_0}$ for $M$ nonstandard recursively saturated. Definable elements are fixed by every $g$; the *gap* of $a$ is $\{b : \exists\,\mathcal{L}_A\text{-definable Skolem } f,\ b< f(a) \text{ and } a<f(b)\}$, and gaps are the natural units on which automorphisms act.

**Small index property (SIP).** $\mathrm{Aut}(M)$ has SIP if every subgroup of index $<2^{\aleph_0}$ is open. SIP converts an abstract isomorphism $\mathrm{Aut}(M)\cong\mathrm{Aut}(N)$ into a homeomorphism, since openness would then be group-theoretically definable.

## 3. History & State of the Art (SOTA)

- **1980–82.** Wilmers (*Minimally saturated models*, 1980) and Smoryński (*Back-and-forth inside a recursively saturated model of arithmetic*, 1982) establish the $(\mathrm{Th},\mathrm{SSy})$ classification and the back-and-forth machinery for building automorphisms.
- **1991.** Kaye's monograph *Models of Peano Arithmetic* codifies the framework. Kaye, Kossak and Kotlarski (**KKK**), *Automorphisms of recursively saturated models of arithmetic* (APAL 55), give the first systematic group-theoretic analysis: every countable recursively saturated $M$ has an automorphism moving every undefinable element ("maximal automorphisms"), and open subgroups, gaps and interstices are tied to saturation strength. The reconstruction question is posed in this circle.
- **1993.** Kossak, Kotlarski and Schmerl (APAL 65) analyze maximal subgroups of $\mathrm{Aut}(M)$, isolating which maximal *open* subgroups are stabilizers — the key device for reading saturation off the group.
- **1995.** Kossak and Schmerl, *The automorphism group of an arithmetically saturated model of Peano arithmetic* (J. London Math. Soc. 52): for countable **arithmetically saturated** models, the abstract group determines the model. Companion paper *Arithmetically saturated models of arithmetic* (NDJFL 36) develops the internal theory.
- **2002.** Schmerl, *Automorphism groups of models of Peano arithmetic* (JSL 67), extends the analysis of which models can share automorphism groups.
- **2006.** Kossak–Schmerl's book states the general question as open; it remains open as of 2026. Parallel reconstruction technology (Lascar's small index work, 1991; Hodges–Hodkinson–Lascar–Shelah 1993) applies to $\omega$-categorical and $\omega$-stable settings that models of $\mathrm{PA}$ fall outside.

## 4. Partial Results / Verified Cases

- **Arithmetically saturated countable models (fully settled).** If $M,N$ are countable arithmetically saturated models of $\mathrm{PA}$ and $\mathrm{Aut}(M)\cong \mathrm{Aut}(N)$, then $M\cong N$ (Kossak–Schmerl 1995). The proof recovers $\mathrm{Th}(M)$ and $\mathrm{SSy}(M)$ from the group.
- **Mixed pairs.** Arithmetic saturation is itself a group-theoretic invariant of $\mathrm{Aut}(M)$ (via the KKK / KKS analysis of maximal open subgroups and moving gaps). Hence if $M$ is arithmetically saturated and $N$ is recursively but not arithmetically saturated, $\mathrm{Aut}(M)\not\cong\mathrm{Aut}(N)$. The open zone is therefore confined to pairs where **neither** model is arithmetically saturated.
- **Topological version.** If the isomorphism is a homeomorphism (equivalently, respects pointwise stabilizers of finite tuples), reconstruction goes through by back-and-forth: open subgroups recover the orbit structure, hence $\mathrm{SSy}$ and $\mathrm{Th}$, hence $M$.
- **Cardinality/structure invariants.** $|\mathrm{Aut}(M)|=2^{\aleph_0}$ for all nonstandard recursively saturated $M$, so cardinality separates nothing; the standard model has $\mathrm{Aut}(\mathbb{N})=1$, and $\mathbb{N}$ is trivially distinguished.

## 5. Principal Obstacles

- **No SIP theorem.** Every known reconstruction success (Ahlbrandt–Ziegler for $\omega$-categorical structures, Hodges–Hodkinson–Lascar–Shelah for the random graph and $\omega$-stable $\omega$-categorical cases) starts from a small index property proof. For $\mathrm{Aut}(M)$, $M\models\mathrm{PA}$ recursively saturated but not arithmetically saturated, SIP is **not known**; without it an abstract isomorphism may in principle scramble the topology.
- **$\mathrm{PA}$ is not $\omega$-categorical and has the independence property.** Orbits of finite tuples are not finite in number; there are $2^{\aleph_0}$ types over $\emptyset$. Standard stability-theoretic tools (finite rank, forking calculus over a countable type space) simply do not apply.
- **Coding is one-way.** Saturation strength is easy to read off the group ($\mathrm{SSy}$ closed under jump ⟺ a group-theoretic property), but recovering a Scott set that is *not* jump-closed requires uniform coding of arbitrary sets in $\mathrm{SSy}(M)$ by group-theoretic configurations. The known codings (via gaps and interstices) consume exactly one jump, which is why the arithmetically saturated case falls and the general case does not.
- **No candidate counterexample machinery.** Producing $M\not\cong N$ with isomorphic groups would need two Scott sets that are "group-theoretically indistinguishable". No forcing or Scott-set-construction technique is known that controls $\mathrm{Aut}$ up to abstract isomorphism while varying $\mathrm{SSy}$.

## 6. The Gap

Proven: the map $M\mapsto \mathrm{Aut}(M)$ is injective (up to isomorphism) on countable **arithmetically saturated** models, and injective on all countable recursively saturated models if one keeps the **topology**. The general statement: injectivity on all countable recursively saturated models with the topology forgotten.

The precise missing step is a single implication:
$$\text{[abstract iso } \mathrm{Aut}(M)\cong\mathrm{Aut}(N)] \;\Longrightarrow\; \text{[the iso maps some/each } G_{(\bar a)} \text{ to an open subgroup]}.$$
This is exactly SIP (or any weaker automatic-continuity statement) for $\mathrm{Aut}(M)$ in the non-arithmetically-saturated range, plus a coding of a general Scott set — one that does not require the jump — by group-theoretic data invariant under abstract isomorphism.

## 7. Current Research (as of June 2026)

- **Automatic continuity / Polish group program.** Work on ample generics, Bergman property and automatic continuity for non-oligomorphic closed subgroups of $\mathrm{Sym}(\omega)$ is the most plausible route; $\mathrm{Aut}(M)$ for $M\models\mathrm{PA}$ is a standard test case in that literature. *(frontier — verify)*
- **Interstice and interstitial gap structure.** Continuing analysis (Kossak, Schmerl and collaborators; Bielefeld/CUNY/Warsaw circles) of the lattice of open subgroups and of maximal automorphisms, aimed at group-theoretic definitions of $\mathrm{SSy}$-fragments below the jump. *(frontier — verify)*
- **Enayat-style unified constructions.** Enayat's uniform account of automorphisms of models of arithmetic and set theory (APAL 2007) supplies fixed-point-set techniques that may yield new invariants of the abstract group.
- **Descriptive-set-theoretic complexity.** Treating $M\mapsto \mathrm{Aut}(M)$ as a Borel reduction problem on the standard Borel space of countable Scott sets, to determine whether abstract-isomorphism of these groups is a smooth equivalence relation. *(frontier — verify)*

## 8. Future Work

1. **Prove SIP for $\mathrm{Aut}(M)$, $M$ countable recursively saturated.** This alone settles the question positively, by reduction to the known topological case.
2. **Jump-free coding.** Find a group-theoretic formula $\varphi$ such that $X\in\mathrm{SSy}(M)$ iff the configuration $\varphi(X)$ is realized in $\mathrm{Aut}(M)$, using only $X$ and not $X'$.
3. **Attack the negative side.** Build a family of countable Scott sets, all consisting of low sets, whose models have pairwise-isomorphic automorphism groups; even one nontrivial pair would refute reconstruction.
4. **Transfer to set theory.** Test the analogous question for countable recursively saturated models of $\mathrm{ZF}$, where Enayat's methods give a different supply of automorphisms.
5. **Classify $\mathrm{Aut}(M)$ up to elementary equivalence** as a group; a first-order group-theoretic sentence separating two models would be a strong partial result.

## 9. Key References

- **[Foundational]** R. Kaye. *Models of Peano Arithmetic.* Oxford Logic Guides 15, Oxford University Press, 1991.
- **[Foundational]** R. Kaye, R. Kossak, H. Kotlarski. *Automorphisms of recursively saturated models of arithmetic.* Annals of Pure and Applied Logic 55 (1991), 67–99.
- **[Foundational]** G. Wilmers. *Minimally saturated models.* In *Model Theory of Algebra and Arithmetic*, Lecture Notes in Mathematics 834, Springer, 1980, 370–380.
- **[Foundational]** C. Smoryński. *Back-and-forth inside a recursively saturated model of arithmetic.* In *Logic Colloquium '80*, North-Holland, 1982.
- **[SOTA]** R. Kossak, J. H. Schmerl. *The automorphism group of an arithmetically saturated model of Peano arithmetic.* Journal of the London Mathematical Society 52 (1995), 235–244.
- **[SOTA]** R. Kossak, H. Kotlarski, J. H. Schmerl. *On maximal subgroups of the automorphism group of a countable recursively saturated model of PA.* Annals of Pure and Applied Logic 65 (1993), 125–148.
- **[SOTA]** J. H. Schmerl. *Automorphism groups of models of Peano arithmetic.* Journal of Symbolic Logic 67 (2002), 1249–1264.
- **[SOTA]** R. Kossak, J. H. Schmerl. *Arithmetically saturated models of arithmetic.* Notre Dame Journal of Formal Logic 36 (1995), 531–546.
- **[SOTA]** A. Enayat. *Automorphisms of models of arithmetic: a unified view.* Annals of Pure and Applied Logic 145 (2007), 16–36.
- **[Survey]** R. Kossak, J. H. Schmerl. *The Structure of Models of Peano Arithmetic.* Oxford Logic Guides 50, Oxford University Press, 2006.
- **[Survey]** R. Kossak. *Four problems concerning recursively saturated models of arithmetic.* Notre Dame Journal of Formal Logic 36 (1995), 519–530.
- **[Context]** D. Lascar. *Autour de la propriété du petit indice.* Proceedings of the London Mathematical Society 62 (1991), 25–53.
- **[Context]** W. Hodges, I. Hodkinson, D. Lascar, S. Shelah. *The small index property for $\omega$-stable $\omega$-categorical structures and for the random graph.* Journal of the London Mathematical Society 48 (1993), 204–218.
- **[Context]** J. Hartmanis, R. E. Stearns. *On the computational complexity of algorithms.* Transactions of the American Mathematical Society 117 (1965), 285–306.

## 10. Worked Example / Concrete Special Case

**Setup.** Fix a completion $T$ of $\mathrm{PA}$. By the Gödel–Rosser theorem $T$ is not recursive, so no recursively saturated model has $\mathrm{SSy}(M)=\mathrm{REC}$; every admissible Scott set contains $T$. By the **low basis theorem** (Jockusch–Soare), the $\Pi^0_1$ class of completions of $\mathrm{PA}$ has a member $T_0$ with $T_0' \equiv_T \emptyset'$ — a *low* completion.

**Step 1: an arithmetically saturated model.** Let $S_{\mathrm{ar}}=\{X\subseteq\mathbb{N}: X \text{ arithmetical}\}$. It is a Scott set, contains $T_0$ (since $T_0\le_T \emptyset'$), and is jump-closed: $X$ arithmetical $\Rightarrow X'$ arithmetical. So the model $M_{\mathrm{ar}}$ with $\mathrm{Th}=T_0$, $\mathrm{SSy}=S_{\mathrm{ar}}$ is countable and **arithmetically saturated**.

**Step 2: a merely recursively saturated model.** Build a countable Scott set $S_{\mathrm{low}}$ all of whose members are low, with $T_0\in S_{\mathrm{low}}$ (iterate the low basis theorem $\omega$ times, taking joins; joins of low sets are low). Since $\emptyset'$ is not low, $T_0' \equiv_T \emptyset' \notin S_{\mathrm{low}}$: not jump-closed. Let $M_{\mathrm{low}}$ have $\mathrm{Th}=T_0$, $\mathrm{SSy}=S_{\mathrm{low}}$.

**Step 3: what is decided.** $\mathrm{SSy}(M_{\mathrm{ar}})\ne \mathrm{SSy}(M_{\mathrm{low}})$, so $M_{\mathrm{ar}}\not\cong M_{\mathrm{low}}$ by the Wilmers classification (equal theories, different standard systems). And indeed $\mathrm{Aut}(M_{\mathrm{ar}})\not\cong \mathrm{Aut}(M_{\mathrm{low}})$: arithmetic saturation is detectable in the abstract group (Section 4), so the groups are separated *without* any appeal to continuity. This is the settled part of the question.

**Step 4: what is not decided.** Repeat Step 2 twice with different generic choices, getting low Scott sets $S_1\neq S_2$ with $T_0\in S_1\cap S_2$, and models $M_1,M_2$. Then $M_1\not\cong M_2$. Both are recursively saturated, neither arithmetically saturated, so the KKK/Kossak–Schmerl invariant is blind here. Every known argument separating $\mathrm{Aut}(M_1)$ from $\mathrm{Aut}(M_2)$ passes through a stabilizer $G_{(a)}$ and so needs the topology: given an abstract isomorphism $\Phi:\mathrm{Aut}(M_1)\to\mathrm{Aut}(M_2)$, nothing currently forces $\Phi(G_{(a)})$ to be open in $\mathrm{Aut}(M_2)$. That single missing implication — index $<2^{\aleph_0}$ $\Rightarrow$ open — is the whole of Kaye's question in this instance.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*