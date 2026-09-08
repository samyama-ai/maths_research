---
id: 08-logic-set-theory/basis-problem-uncountable-graphs
title: "Todorcevic's Conjecture on Basis for Uncountable Graphs"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Todorcevic's Conjecture on Basis for Uncountable Graphs

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/basis-problem-uncountable-graphs` · **Status:** open

## 1. Problem Statement / Conjecture

The **basis problem for uncountable graphs** asks for a small, explicitly described family $\mathcal{B}$ of graphs such that every uncountable graph contains a member of $\mathcal{B}$ as a subgraph on an uncountable vertex set. Todorcevic's programme (ICM 1998) proposes that under strong forcing axioms such bases exist and are canonical.

The sharpest and most-cited instance is **Todorcevic's Axiom (TA)**, also called the **Open Coloring Axiom (OCA)** and referred to in the Banach-space and operator-algebra literature as *Todorcevic's Conjecture*:

> **(OCA / TA).** Let $X$ be a separable metrizable space and let $[X]^2 = K_0 \cup K_1$ be a partition with $K_0$ open in the square topology on $[X]^2$. Then either
> 1. there is an uncountable $Y \subseteq X$ with $[Y]^2 \subseteq K_0$, or
> 2. $X = \bigcup_{n<\omega} X_n$ with $[X_n]^2 \subseteq K_1$ for every $n$.

Read as a basis statement: **the class of open graphs on separable metric spaces that are not $\sigma$-decomposable into independent sets has the one-element basis $\{K_{\aleph_1}\}$.**

Two open components remain:

- **(C1) Cardinal-arithmetic component.** Does OCA imply $2^{\aleph_0} = \aleph_2$? Open since 1989.
- **(C2) Basis component.** Is there a consistent, canonical basis of small cardinality for the class of *all* graphs on $\omega_1$ (no definability hypothesis) under the quasi-order of embeddability, in analogy with the five-element basis for uncountable linear orders?

A complete solution of (C1) means a ZFC proof from OCA that $\mathfrak{c} = \aleph_2$, or a model of OCA $+\ \mathfrak{c} > \aleph_2$. A solution of (C2) means either exhibiting such a basis under some forcing axiom, or a ZFC construction of $2^{\aleph_1}$ pairwise incomparable graphs closed under the relevant reductions that provably blocks every candidate basis.

## 2. Mathematical Foundations

**Graphs and embeddability.** A graph is a pair $G = (V, E)$ with $E \subseteq [V]^2$. For graphs $G, H$ write $G \sqsubseteq H$ ("$G$ embeds in $H$") if there is an injection $e : V_G \to V_H$ with $\{x,y\} \in E_G \iff \{e(x),e(y)\}\in E_H$. Let
$$\mathcal{G}_{\aleph_1} = \{\,G : |V_G| = \aleph_1\,\},$$
a quasi-order under $\sqsubseteq$. A set $\mathcal{B} \subseteq \mathcal{G}_{\aleph_1}$ is a **basis** if $\forall G \in \mathcal{G}_{\aleph_1}\ \exists B \in \mathcal{B}\ (B \sqsubseteq G)$.

**Partition notation.** $\kappa \to (\lambda,\mu)^2$ means every $c : [\kappa]^2 \to 2$ admits either a $0$-homogeneous set of type $\lambda$ or a $1$-homogeneous set of type $\mu$. Relevant facts:

- **Sierpiński (1933):** $\omega_1 \not\to (\omega_1)^2_2$.
- **Dushnik–Miller:** $\omega_1 \to (\omega_1, \omega)^2$; **Erdős–Rado:** $\omega_1 \to (\omega_1, \omega+1)^2$, and $\omega_1 \to (\omega_1,\omega+2)^2$ fails under CH.
- **Todorcevic (1987):** $\omega_1 \not\to [\omega_1]^2_{\omega_1}$ in ZFC — there is $c:[\omega_1]^2\to\omega_1$ taking all $\aleph_1$ colours on every uncountable square.

The last result is the fundamental obstruction: it shows the *unrestricted* class $\mathcal{G}_{\aleph_1}$ is far too rich for a naive basis, and forces the problem to be posed either for definable/topologically restricted graphs (OCA) or modulo a coarser reduction.

**Open graphs.** Give $X$ a separable metrizable topology; $[X]^2$ carries the quotient of $X^2 \setminus \Delta$. A graph $K_0 \subseteq [X]^2$ is *open* iff for all $\{x,y\}\in K_0$ there are open $U \ni x$, $V \ni y$ with $U \otimes V := \{\{u,v\}: u\in U, v \in V, u \neq v\} \subseteq K_0$. A set $Y$ is $K_0$-*homogeneous* (a clique) if $[Y]^2\subseteq K_0$; $X$ is $\sigma$-*independent* if it is a countable union of $K_1$-homogeneous sets.

**Variants.**
- $\mathrm{OCA}_{[T]}$: as stated above (Todorcevic 1989).
- $\mathrm{OCA}_{\mathrm{ARS}}$ (Abraham–Rubin–Shelah 1985): every partition $[X]^2 = K_0 \cup K_1$ with $K_0$ open and $X$ of size $\aleph_1$ admits a decomposition $X = \bigcup_{n} X_n$ into $\aleph_1$-many pieces each homogeneous for one colour, in a strengthened form. The two axioms are not known to be equivalent and are *not* known to be jointly derivable from a single simple axiom other than PFA.
- $\mathrm{OCA}_\infty$: a Ramsey-style strengthening used in rigidity arguments (Farah).

**Canonical hard example.** For an uncountable $X \subseteq \mathbb{R}$ and a well-ordering $\lhd$ of $X$ of type $\omega_1$, the **Sierpiński graph** is
$$S(X,\lhd) = \{\,\{x,y\} \in [X]^2 : (x < y \leftrightarrow y \lhd x)\,\}.$$

## 3. History & State of the Art (SOTA)

- **1933.** Sierpiński's colouring kills $\omega_1 \to (\omega_1)^2_2$, so no basis argument can proceed by pure partition calculus.
- **1968–81.** Galvin's open partition theorem for Polish spaces (perfect-set version) — published account in Blass, *A partition theorem for perfect sets*, Proc. AMS 82 (1981).
- **1985.** Abraham, Rubin and Shelah isolate $\mathrm{OCA}_{\mathrm{ARS}}$ and prove its consistency with $\mathfrak{c} = \aleph_2$, in the course of analysing $\aleph_1$-dense real order types.
- **1987.** Todorcevic, *Partitioning pairs of countable ordinals* (Acta Math. 159): walks on ordinals, $\omega_1 \not\to [\omega_1]^2_{\omega_1}$.
- **1989.** Todorcevic, *Partition Problems in Topology*: OCA is stated and proved consistent from PFA; first applications, including $\mathfrak{b} = \aleph_2$ under OCA.
- **1993.** Veličković: OCA implies every automorphism of $\mathcal{P}(\omega)/\mathrm{fin}$ is trivial. Feng: OCA holds outright (in ZFC) for analytic graphs.
- **1998.** Todorcevic's ICM address *Basis problems in combinatorial set theory* frames the general programme: bases for uncountable linear orders, trees, graphs, and directed graphs.
- **2002.** Moore: $\mathrm{OCA}_{\mathrm{ARS}} + \mathrm{OCA}_{[T]} \Rightarrow \mathfrak{c} = \aleph_2$.
- **2006.** Moore proves the five-element basis theorem for uncountable linear orders from BPFA — the flagship success of the programme, and the template the graph case has not yet matched.
- **2011.** Farah: all automorphisms of the Calkin algebra are inner under OCA-type hypotheses; Martínez-Ranero: Aronszajn lines are well-quasi-ordered under PFA.

## 4. Partial Results / Verified Cases

| Class / hypothesis | Status |
|---|---|
| Analytic ($\boldsymbol{\Sigma}^1_1$) open graphs on Polish spaces | **Theorem of ZFC** (Feng 1993); OCA for all sets of reals follows from AD$^{L(\mathbb{R})}$ / large cardinals |
| Open graphs on Polish $X$, perfect-clique version | **Theorem** (Galvin; Blass 1981) |
| $|X| = \aleph_1$, open graph, $\mathrm{OCA}_{\mathrm{ARS}}$ | **Consistent with** $\mathfrak{c}=\aleph_2$ (Abraham–Rubin–Shelah 1985) |
| Full $\mathrm{OCA}_{[T]}$, arbitrary separable metric $X$ | **Consistent**, from PFA (Todorcevic 1989) |
| $\mathfrak{b}$ under OCA | $\mathfrak{b} = \aleph_2$ (Todorcevic 1989) |
| $\mathfrak{c}$ under $\mathrm{OCA}_{\mathrm{ARS}}+\mathrm{OCA}_{[T]}$ | $\mathfrak{c} = \aleph_2$ (Moore 2002) |
| Uncountable **linear orders**, BPFA | Five-element basis $\{\,\omega_1,\ \omega_1^*,\ C,\ B,\ B^*\,\}$, $C \subseteq \mathbb{R}$ of size $\aleph_1$, $B$ Countryman (Moore 2006) |
| Aronszajn lines, PFA | Well-quasi-ordered (Martínez-Ranero 2011) |
| Transitive relations on $\omega_1$, PFA | Finite basis (Todorcevic, Proc. LMS 73 (1996)) |
| Arbitrary graphs on $\omega_1$ under CH | **No small basis**: $2^{\aleph_1}$ pairwise $\sqsubseteq$-incomparable graphs |

## 5. Principal Obstacles

- **Sierpiński-type rigidity in ZFC.** $\omega_1 \not\to [\omega_1]^2_{\omega_1}$ produces graphs on $\omega_1$ whose every uncountable restriction reproduces the whole colouring pattern. Any basis for unrestricted $\mathcal{G}_{\aleph_1}$ must contain continuum-many (or more) mutually incomparable such objects. This is why the topological/definability restriction in OCA is not cosmetic — it is the only known way to defeat walks-on-ordinals constructions.
- **Openness is used destructively in the proof.** Todorcevic's PFA proof of OCA builds a $\sigma$-closed$*$ccc forcing that generically shoots an uncountable clique; the ccc verification uses a $\Delta$-system plus a *neighbourhood* argument that requires $K_0$ to be open. For a Borel or arbitrary $K_0$ the analogous poset collapses $\omega_1$ or fails ccc.
- **No absoluteness handle above $\boldsymbol{\Sigma}^1_1$.** Feng's ZFC result for analytic graphs uses Shoenfield absoluteness and a Cantor-scheme construction of a perfect clique. Beyond $\boldsymbol{\Sigma}^1_1$ the clique is not $\Sigma^1_2$-definable, so absoluteness gives nothing and one must add large cardinals.
- **The $\mathfrak{c} = \aleph_2$ barrier.** All known consequences of OCA on cardinal characteristics ($\mathfrak{b}=\mathfrak{a}=\aleph_2$, etc.) are proved by applying OCA to a *fixed* $\sigma$-directed structure of size $\aleph_1$ or $\aleph_2$; none reaches an arbitrary set of reals of size $\aleph_3$. There is no known coding of a set of size $\aleph_3$ into an open graph whose clique/decomposition dichotomy yields a contradiction.
- **Ramsey degree unknown.** For a putative graph basis one needs a canonical-Ramsey theorem at $\omega_1$ ("every uncountable graph restricted to an uncountable set becomes one of finitely many canonical forms"). No such theorem is known even consistently.

## 6. The Gap

Section 4 gives a basis for open graphs (one element, $K_{\aleph_1}$, modulo $\sigma$-independence) under PFA, and for uncountable *linear orders* (five elements) under BPFA. Section 1 asks for the same for arbitrary uncountable graphs.

The precise gap has two edges.

1. **Definability edge.** Between $\boldsymbol{\Sigma}^1_1$-open (ZFC theorem) and arbitrary (needs PFA); and between *open* $K_0$ and *Borel* or *arbitrary* $K_0$, where the axiom is outright false — Sierpiński's graph, whose colour classes are Borel-in-a-parameter given a well-order, has neither an uncountable clique nor a $\sigma$-independent decomposition. So the general basis question must be reformulated, not merely strengthened.
2. **Cardinal edge.** OCA fixes $\mathfrak{b}$ at $\aleph_2$ but not $\mathfrak{c}$. Closing (C1) requires either a new application of the open-graph dichotomy to a structure of size $\aleph_3$, or a forcing iteration preserving OCA while blowing up $\mathfrak{c}$ — the latter is obstructed because all known OCA-preserving iterations are proper of length $\omega_2$ over a model of CH.

## 7. Current Research (as of June 2026)

- **Toronto / Paris (Todorcevic and collaborators).** Continued development of walks on ordinals and $\rho$-functions as the source of counterexamples; extension of basis theory from linear orders to trees and directed graphs.
- **York University / Copenhagen (Farah, Vignati, McKenney).** $\mathrm{OCA}_\infty$ and "OCA lifting theorems" for quotient structures — the main engine behind rigidity of $\mathcal{P}(\omega)/\mathrm{fin}$, the Calkin algebra, and coronas. Farah's *Combinatorial Set Theory of C\*-algebras* (Springer, 2019) is the reference text.
- **Cornell / Rutgers (Moore, and successors).** Structural analysis of Aronszajn trees and lines; the wqo programme as the strongest available surrogate for a basis.
- **Descriptive-set-theoretic side.** Open-graph dichotomies for $\sigma$-ideals and for Borel graphs (Kechris–Solecki–Todorcevic $G_0$-dichotomy lineage), with active work on whether $G_0$-style dichotomies admit $\omega_1$-analogues. *(frontier — verify)*
- **Status of (C1).** Still open; no announced solution as of mid-2026. *(frontier — verify)*

## 8. Future Work

- Find an open graph on a separable metric space of size $\aleph_3$ whose OCA-dichotomy forces a contradiction — the most direct route to $\mathfrak{c}=\aleph_2$ from OCA alone.
- Determine whether $\mathrm{OCA}_{[T]} \Rightarrow \mathrm{OCA}_{\mathrm{ARS}}$; a positive answer settles (C1) via Moore's 2002 theorem.
- Replace $\sqsubseteq$-basis by a *wqo* statement: is the class of uncountable graphs omitting $K_{\aleph_1}$ and $\overline{K_{\aleph_1}}$ well-quasi-ordered under PFA? This is the graph analogue of Martínez-Ranero's Aronszajn-line theorem.
- Classify Sierpiński graphs $S(X,\lhd)$ up to $\sqsubseteq$ under PFA: are there finitely many, or $2^{\aleph_1}$?
- Push $\mathrm{OCA}_\infty$-type axioms to graphs on $\omega_1$ that are open in a *Suslin* rather than metric topology.

## 9. Key References

- **[Foundational]** W. Sierpiński. *Sur un problème de la théorie des relations.* Ann. Scuola Norm. Sup. Pisa (2) 2, 1933.
- **[Foundational]** U. Abraham, M. Rubin, S. Shelah. *On the consistency of some partition theorems for continuous colorings, and the structure of $\aleph_1$-dense real order types.* Annals of Pure and Applied Logic 29, 1985, 123–206.
- **[Foundational]** S. Todorcevic. *Partitioning pairs of countable ordinals.* Acta Mathematica 159, 1987, 261–294.
- **[Foundational]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics 84, American Mathematical Society, 1989.
- **[Foundational]** A. Blass. *A partition theorem for perfect sets.* Proceedings of the AMS 82, 1981, 271–277.
- **[SOTA]** Q. Feng. *Homogeneity for open partitions of pairs of reals.* Transactions of the AMS 339, 1993, 659–684.
- **[SOTA]** B. Veličković. *OCA and automorphisms of $\mathcal{P}(\omega)/\mathrm{fin}$.* Topology and its Applications 49, 1993, 1–13.
- **[SOTA]** J. T. Moore. *Open colorings, the continuum and the second uncountable cardinal.* Proceedings of the AMS 130, 2002, 2753–2759.
- **[SOTA]** J. T. Moore. *A five element basis for the uncountable linear orders.* Annals of Mathematics 163, 2006, 669–688.
- **[SOTA]** C. Martínez-Ranero. *Well-quasi-ordering Aronszajn lines.* Fundamenta Mathematicae 213, 2011, 197–211.
- **[SOTA]** I. Farah. *All automorphisms of the Calkin algebra are inner.* Annals of Mathematics 173, 2011, 619–661.
- **[Survey]** S. Todorcevic. *Basis problems in combinatorial set theory.* Documenta Mathematica, Extra Volume ICM 1998, Vol. II, 43–52.
- **[Survey]** S. Todorcevic. *Walks on Ordinals and Their Characteristics.* Progress in Mathematics 263, Birkhäuser, 2007.
- **[Survey]** S. Argyros, S. Todorcevic. *Ramsey Methods in Analysis.* Advanced Courses in Mathematics CRM Barcelona, Birkhäuser, 2005.
- **[Survey]** I. Farah. *Combinatorial Set Theory of C\*-algebras.* Springer Monographs in Mathematics, 2019.

## 10. Worked Example / Concrete Special Case

**Claim.** The Sierpiński graph is a graph on an uncountable separable metric space with *no* uncountable clique and *no* $\sigma$-independent decomposition. Hence OCA's openness hypothesis cannot be dropped, and no basis of the form $\{K_{\aleph_1}\}$ works for general graphs.

**Construction.** Let $X \subseteq \mathbb{R}$ with $|X| = \aleph_1$, and let $\lhd$ be a well-ordering of $X$ of order type $\omega_1$; write $X = \{x_\alpha : \alpha < \omega_1\}$ with $x_\alpha \lhd x_\beta \iff \alpha < \beta$. Set
$$E = \bigl\{\{x_\alpha,x_\beta\} : \alpha<\beta \text{ and } x_\beta < x_\alpha \bigr\},$$
i.e. edges are exactly the pairs on which $\lhd$ and the real order $<$ disagree.

**Step 1 — no uncountable clique.** Suppose $Y \subseteq X$ is uncountable with $[Y]^2 \subseteq E$. Enumerate $Y$ in $\lhd$-increasing order as $\langle y_\xi : \xi<\omega_1\rangle$. For $\xi<\eta$ we get $\{y_\xi,y_\eta\}\in E$, so $y_\eta < y_\xi$. Thus $\langle y_\xi\rangle_{\xi<\omega_1}$ is a strictly $<$-decreasing $\omega_1$-sequence of reals. Pick a rational $q_\xi \in (y_{\xi+1}, y_\xi)$; the map $\xi \mapsto q_\xi$ is injective on $\omega_1$ into $\mathbb{Q}$. Contradiction.

**Step 2 — no uncountable independent set.** Suppose $[Z]^2 \cap E = \emptyset$ with $Z$ uncountable. Then $\lhd$ and $<$ agree on $Z$, so $(Z,<)$ is well-ordered of type $\omega_1$. The same rational-interleaving argument (choose $q_\xi \in (z_\xi, z_{\xi+1}) \cap \mathbb{Q}$) injects $\omega_1$ into $\mathbb{Q}$. Contradiction.

**Step 3 — no $\sigma$-independent decomposition.** If $X = \bigcup_{n<\omega} X_n$ with each $X_n$ independent, then some $X_n$ is uncountable (a countable union of countable sets has size $\le \aleph_0 < \aleph_1$), contradicting Step 2.

**Step 4 — why OCA is not violated.** $E$ is not open in $[X]^2$: take $\{x_\alpha, x_\beta\} \in E$ with $\alpha < \beta$, $x_\beta < x_\alpha$. Any basic neighbourhood $U \otimes V$ with $x_\beta \in U$, $x_\alpha \in V$ contains pairs $\{u,v\}$ with $u,v \in X$ and $u \lhd v$ arbitrary — the $\lhd$-order is nowhere continuous relative to the Euclidean topology, so no neighbourhood of the pair stays inside $E$. Concretely, if $X$ is dense in an interval, every $U$ meets $X$ in $\aleph_1$ points, and only countably many of them lie $\lhd$-below $x_\alpha$; so $U \otimes V \not\subseteq E$.

**Consequence.** The dichotomy of Section 1 is exactly calibrated: it holds for open $E$ under PFA (and in ZFC for analytic $E$ by Feng), and fails for the $\lhd$-definable $E$ above. Any basis theorem for *all* uncountable graphs must therefore admit $2^{\aleph_1}$-many Sierpiński graphs $S(X,\lhd)$ as basis candidates, or coarsen the reduction $\sqsubseteq$. Deciding which of these is possible is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*