---
id: 04-topology/turaev-surface-words-conjecture
title: "Turaev Surface Words Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Turaev Surface Words Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/turaev-surface-words-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Every connected link diagram $D$ in $S^2$ determines a closed orientable **Turaev surface** $\Sigma_D \subset S^3$, which is a Heegaard surface for $S^3$ on which $D$ becomes an alternating diagram. The combinatorics of $\Sigma_D$ — equivalently, of the induced Heegaard diagram — is encoded by a finite list of cyclic words in which every letter occurs exactly twice: the **Turaev surface words** of $D$.

**The conjecture (realization problem).** Give an intrinsic, finitely checkable characterization of which such word systems arise. Concretely, Armond, Druivenga and Kindred (2015) formulated the claim that the evident local conditions — each crossing letter occurring exactly twice, the induced ribbon-graph duality between the two states, and the induced closed $3$-manifold being $S^3$ — are not merely necessary but **sufficient**:

> **Conjecture.** A system of double-occurrence cyclic words $W$ is a Turaev surface word system if and only if $W$ satisfies conditions (N1)–(N3) of §2.

A complete solution requires either (a) an algorithm plus proof reconstructing a spherical link diagram $D$ from any $W$ satisfying (N1)–(N3), or (b) an explicit $W$ satisfying (N1)–(N3) that is provably not realized by any $D \subset S^2$.

## 2. Mathematical Foundations

Let $D \subset S^2$ be a connected link diagram with crossing set $C(D)$, $|C(D)| = n$. At each crossing apply the Kauffman $A$-smoothing or $B$-smoothing:

$$\text{$A$: } \;\;\times \;\longmapsto\; )( \qquad\qquad \text{$B$: } \;\;\times \;\longmapsto\; \asymp$$

Let $s_A(D)$ and $s_B(D)$ be the all-$A$ and all-$B$ states, with $|s_A|$ and $|s_B|$ circles.

**Turaev surface.** Embed $D$'s projection in $S^2 \times \{0\} \subset S^3$. The saddle cobordism from $s_A$ (at height $+1$) to $s_B$ (at height $-1$), with $|s_A| + |s_B|$ discs capping the ends, is a closed orientable surface

$$\Sigma_D, \qquad g(\Sigma_D) \;=\; g_T(D) \;=\; \frac{2 + n - |s_A| - |s_B|}{2}.$$

Turaev's inequality $|s_A| + |s_B| \le n + 2$ gives $g_T(D) \ge 0$, with equality iff $D$ is alternating. The **Turaev genus** of a link is $g_T(L) = \min_D g_T(D)$.

**Heegaard structure.** $\Sigma_D$ splits $S^3$ into two handlebodies $H_A, H_B$; the $s_A$-circles bound compressing discs in $H_A$ and the $s_B$-circles bound compressing discs in $H_B$. Thus $(\Sigma_D; s_A, s_B)$ is a Heegaard diagram of $S^3$ of genus $g_T(D)$, and $D$ sits on $\Sigma_D$ as an alternating diagram.

**Ribbon graph / word encoding.** Let $\mathbb{G}_A(D)$ be the ribbon graph with vertex set $s_A$, edge set $C(D)$, and cyclic edge-orders read off $\Sigma_D$. Reading each $A$-circle gives a cyclic word $w_i$ in the alphabet $C(D)$; put $W_A(D) = \{w_1,\dots,w_{|s_A|}\}$. Faces of $\mathbb{G}_A$ correspond to $s_B$-circles, so

$$\chi(\Sigma_D) \;=\; |s_A| - n + |s_B| \;=\; 2 - 2g_T(D).$$

**Necessary conditions.**
- **(N1) Double occurrence.** Each letter of $C(D)$ occurs exactly twice in $W$ (counting both occurrences in one word).
- **(N2) Ribbon-graph consistency.** $W$ defines a connected orientable ribbon graph $\mathbb{G}$; its face words $W^{*}$ (the dual ribbon graph $\mathbb{G}^{*}$) are the $B$-state words, and $\Sigma$ is the ribbon surface of $\mathbb{G}$.
- **(N3) $S^3$-condition.** Gluing handlebodies to $\Sigma$ along the vertex circles of $\mathbb{G}$ on one side and the face circles on the other yields $S^3$.

## 3. History & State of the Art (SOTA)

- **1987.** Turaev introduces the surface in *A simple proof of the Murasugi and Kauffman theorems on alternating links*, using $|s_A| + |s_B| \le n+2$ to prove the crossing-number and span conjectures for alternating links.
- **2001.** Bollobás–Riordan define the ribbon graph polynomial, supplying the combinatorial language.
- **2007–2008.** Champanerkar–Kofman–Stoltzfus and Dasbach–Futer–Kalfagianni–Lin–Stoltzfus show the Jones polynomial is a specialization of the Bollobás–Riordan polynomial of $\mathbb{G}_A(D)$, making the ribbon graph — not just its genus — the object of interest.
- **2008–2011.** Turaev genus is shown to bound homological width: $\mathrm{w}_{Kh}(L) \le g_T(L) + 2$ (Champanerkar–Kofman–Stoltzfus), $\mathrm{w}_{HFK}(K) \le g_T(K)+1$ (Lowrance); Dasbach–Lowrance bound the signature.
- **2015.** Armond–Druivenga–Kindred describe the Heegaard diagram of $\Sigma_D$ explicitly, define Turaev surface words, and pose the realization conjecture. This is the reference statement of the problem.
- **2018.** Seungwon Kim characterizes link diagrams of Turaev genus one; Kim–Lowrance relate Turaev genus to alternating decompositions.

**SOTA:** the conjecture is open in both directions. No counterexample is known, and no general reconstruction algorithm exists beyond low genus.

## 4. Partial Results / Verified Cases

- **Genus $0$ (complete).** If $g(\Sigma) = 0$, then $\mathbb{G}$ is a planar ribbon graph, $\Sigma = S^2$ is the unique genus-$0$ Heegaard surface of $S^3$, and $W$ is realized by the unique alternating diagram whose all-$A$ state is $\mathbb{G}$. This is the classical Turaev-genus-zero criterion: connected $D$ has $g_T(D) = 0$ iff $D$ is alternating.
- **Genus $1$.** Kim's classification of Turaev genus one diagrams (via the alternating decomposition of the diagram into alternating tangles glued along a cycle of "non-alternating" edges) gives a structural normal form; realization for genus-$1$ word systems is verified in this framework for the diagrams arising from that decomposition.
- **Adequate diagrams.** For $A$-adequate and $B$-adequate diagrams ($\mathbb{G}_A$ and $\mathbb{G}_B$ loopless) Abe's theorem $g_T(K) = c(K) - \operatorname{span}\langle K\rangle$ (for adequate $K$) pins the genus exactly, and the word system is recoverable from the state graphs.
- **Small crossing number.** Exhaustive checks over all connected diagrams with $n \le 12$ crossings (via knot tables plus diagram enumeration) find no word system satisfying (N1)–(N3) that fails to be realized. *(computational; ranges reported in the ribbon-graph literature.)*
- **Trivial direction.** (N1)–(N3) are proven necessary — this is exactly the content of the ADK Heegaard-diagram description.

## 5. Principal Obstacles

- **Non-locality of planarity.** (N1)–(N2) are purely local/combinatorial and can be checked in $O(n)$ time. Realization by a diagram in $S^2$ is a global condition. The classical analogue — Gauss code realizability — needed genuinely global criteria (Lovász/Dehn/Rosenstiehl interlacement conditions); no interlacement-style criterion is known for state words.
- **Waldhausen gives no rigidity.** Every genus-$g$ Heegaard splitting of $S^3$ is standard, so knowing $\Sigma$ *is* a Heegaard surface of $S^3$ supplies no residual invariant. The obstruction, if any, lives in the position of the curve system, not the splitting.
- **(N3) is not effectively checkable.** Deciding whether a Heegaard diagram presents $S^3$ is $3$-sphere recognition — decidable, but with no known polynomial algorithm and no combinatorial normal form on words. So even the hypothesis of the conjecture resists finite certification.
- **Loss of the diagram under partial duality.** Partial duality (Chmutov, Moffatt) acts transitively enough on ribbon graphs that the class of realizable $\mathbb{G}_A$ is not closed under natural operations; ribbon-graph invariants (Bollobás–Riordan polynomial, genus, duality) are blind to the distinction.
- **No obstruction theory.** Turaev genus itself is hard to compute: $g_T$ is not known to be algorithmically computable in general, and the only strong lower bounds come from homological width, which is far too coarse to detect a single unrealizable word.

## 6. The Gap

Proven: (N1)–(N3) hold for every Turaev surface word system, and they suffice in genus $0$ and in the structured genus-$1$ families.

Missing: a **reconstruction map**. Given $W$ satisfying (N1)–(N3), one has an alternating link diagram $D_W$ on the abstract surface $\Sigma$, and $\Sigma$ bounds handlebodies making $S^3$. What is not known is whether the pair $(\Sigma, D_W)$ can always be isotoped so that $\Sigma$ is the *Turaev* surface of the image of $D_W$ under the projection $\Sigma \to S^2$ — i.e. whether the saddle-cobordism structure can be recovered. The gap is exactly the step from "$\Sigma$ is a Heegaard surface carrying an alternating diagram" to "$\Sigma$ arises from a spherical diagram by the $s_A \to s_B$ cobordism".

## 7. Current Research (as of June 2026)

- **Alternating-decomposition school** (Kim, Lowrance, Vassar/Bard College): pushing the genus-one normal form to genus two, where the decomposition graph is no longer a cycle. *(frontier — verify)*
- **Kindred's geometric programme**: state surfaces, checkerboard/plumbing techniques and a geometric proof of the flyping theorem give tools for isotoping alternating diagrams on surfaces; adapting them to the reconstruction step is the most direct attack. *(frontier — verify)*
- **Ribbon-graph combinatorics** (Ellis-Monaghan, Moffatt, and collaborators): partial duality and twisted duality as a group action on word systems, seeking an orbit invariant distinguishing realizable from non-realizable. *(frontier — verify)*
- **Computational enumeration**: exhaustive generation of orientable ribbon graphs with $n \le 14$ edges and $S^3$-recognition on the resulting Heegaard diagrams (Regina/SnapPy pipelines) as a counterexample search. *(frontier — verify)*

## 8. Future Work

1. **Find an interlacement criterion.** Replace (N3) by a Lovász-style condition on the interlacement graph of $W$, making the characterization checkable in polynomial time.
2. **Prove genus $2$.** With Kim's genus-one result, genus $2$ would establish a pattern strong enough to attempt induction on $g_T$ via destabilization of the Heegaard splitting.
3. **Counterexample search at high genus.** Realizable $\mathbb{G}_A$ are conjecturally sparse among all ribbon graphs with $n$ edges as $g \to n/2$; a counting argument comparing the two growth rates could give a non-constructive disproof.
4. **Relate to Turaev genus computability.** A positive answer yields a certificate for "$g_T(L) \le g$", potentially placing Turaev-genus bounding in $\mathbf{NP}$.

## 9. Key References

- **[Foundational]** V. G. Turaev. *A simple proof of the Murasugi and Kauffman theorems on alternating links.* L'Enseignement Mathématique (2) **33** (1987), 203–225.
- **[Foundational]** B. Bollobás, O. Riordan. *A polynomial invariant of graphs on orientable surfaces.* Proc. London Math. Soc. **83** (2001), 513–531. [DOI](https://doi.org/10.1112/plms/83.3.513)
- **[Foundational]** O. Dasbach, D. Futer, E. Kalfagianni, X.-S. Lin, N. Stoltzfus. *The Jones polynomial and graphs on surfaces.* J. Combin. Theory Ser. B **98** (2008), 384–399. [DOI](https://doi.org/10.1016/j.jctb.2007.08.003)
- **[Problem source]** C. Armond, N. Druivenga, T. Kindred. *Heegaard diagrams corresponding to Turaev surfaces.* Journal of Knot Theory and Its Ramifications **24** (2015), no. 4, 1550019. [DOI](https://doi.org/10.1142/s0218216515500261)
- **[SOTA / Recent]** S. Kim. *Link diagrams with low Turaev genus.* Proc. Amer. Math. Soc. **146** (2018), 875–890. [DOI](https://doi.org/10.1090/proc/13723)
- **[SOTA / Recent]** S. Kim, A. Lowrance. *Turaev genus and alternating decompositions.* Algebr. Geom. Topol. **18** (2018), 1665–1682. [DOI](https://doi.org/10.2140/agt.2017.17.793)
- **[SOTA / Recent]** A. Champanerkar, I. Kofman, N. Stoltzfus. *Graphs on surfaces and Khovanov homology.* Algebr. Geom. Topol. **7** (2007), 1531–1540. [DOI](https://doi.org/10.2140/agt.2007.7.1531)
- **[SOTA / Recent]** A. Lowrance. *On knot Floer width and Turaev genus.* Algebr. Geom. Topol. **8** (2008), 1141–1162. [DOI](https://doi.org/10.2140/agt.2008.8.1141)
- **[SOTA / Recent]** T. Abe. *The Turaev genus of an adequate knot.* Topology and its Applications **156** (2009), 2704–2712. [DOI](https://doi.org/10.1016/j.topol.2009.07.020)
- **[SOTA / Recent]** O. Dasbach, A. Lowrance. *Turaev genus, knot signature, and the knot homology concordance invariants.* Proc. Amer. Math. Soc. **139** (2011), 2631–2645. [DOI](https://doi.org/10.1090/s0002-9939-2010-10698-6)
- **[Survey]** A. Champanerkar, I. Kofman. *A survey on the Turaev genus of knots.* Acta Mathematica Vietnamica **39** (2014), 497–514. [DOI](https://doi.org/10.1007/s40306-014-0083-y)
- **[Survey]** J. Ellis-Monaghan, I. Moffatt. *Graphs on Surfaces: Dualities, Polynomials, and Knots.* SpringerBriefs in Mathematics, Springer, 2013. [DOI](https://doi.org/10.5860/choice.51-3890)

## 10. Worked Example / Concrete Special Case

**(a) A realizable word system: the standard trefoil.** Take $D$ = closure of the braid $\sigma_1^3$, $n = 3$, crossings labelled $1,2,3$. The all-$A$ state has two circles — an outer and an inner one, each passing through all three crossings — so

$$W_A \;=\; \{\,(1\,2\,3),\;(1\,3\,2)\,\}, \qquad |s_A| = 2.$$

$\mathbb{G}_A$ is the theta graph $\Theta_3$: two vertices, three parallel edges. Its faces are the three bigons, so $|s_B| = 3$. Then

$$\chi = 2 - 3 + 3 = 2 \;\Rightarrow\; g(\Sigma_D)=0, \qquad g_T(D) = \tfrac{2 + 3 - 2 - 3}{2} = 0,$$

consistent with $D$ alternating. Conditions (N1)–(N3) hold trivially, and reconstruction is immediate: $\Theta_3 \subset S^2$ is the all-$A$ state graph of exactly one alternating diagram, the trefoil.

**(b) A word satisfying (N1)–(N2) but not (N3).** Take the single cyclic word

$$W \;=\; \{\,(1\,2\,1\,2)\,\}, \qquad n = 2.$$

Each letter occurs twice, so (N1) holds. The ribbon graph $\mathbb{G}$ has one vertex and two interleaved loops; it is orientable and connected, with $V = 1$, $E = 2$, and one face, so

$$\chi = 1 - 2 + 1 = 0 \;\Rightarrow\; \Sigma = T^2, \quad g = 1,$$

and (N2) holds. If $W$ were realized by a diagram $D$, then $n = 2$, $|s_A| = 1$, $|s_B| = 1$, giving $g_T(D) = (2 + 2 - 1 - 1)/2 = 1$.

But enumerate all connected $2$-crossing diagrams in $S^2$. The shadow is either two circles crossing twice (Hopf shadow, $(|s_A|,|s_B|) = (2,2)$) or one circle with two self-crossings. The latter has Gauss code $1122$ (the code $1212$ is the classical non-planar Gauss code), giving $(3,1)$ or $(2,2)$ depending on curl handedness. In every case $|s_A| + |s_B| = 4 = n + 2$ and $g_T(D) = 0$. So no diagram realizes $W$.

Condition (N3) detects this directly: on $T^2$ the vertex curve $\alpha$ and the face curve $\beta$ meet in the two edge-bands, so $|\alpha \cap \beta| = 2$. A genus-one Heegaard splitting yields $S^3$ only when the two curves meet once; with two intersections the glued manifold is $S^1 \times S^2$ or a lens space, never $S^3$.

The conjecture asserts that this pattern is complete: (N3) is the *only* further obstruction. Whether some larger word system slips past all three conditions and still fails to come from a spherical diagram is exactly what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*