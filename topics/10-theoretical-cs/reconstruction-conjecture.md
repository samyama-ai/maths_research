---
id: 10-theoretical-cs/reconstruction-conjecture
title: "Reconstruction Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Reconstruction Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/reconstruction-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple undirected graph with vertex set $V(G)$, $|V(G)| = n$. For $v \in V(G)$ write $G - v$ for the induced subgraph on $V(G) \setminus \{v\}$. The **deck** of $G$ is the multiset of isomorphism classes
$$\mathcal{D}(G) = \{\!\{\, [G-v] \;:\; v \in V(G) \,\}\!\},$$
whose elements are called **cards**. Two graphs $G, H$ are **hypomorphic** if $\mathcal{D}(G) = \mathcal{D}(H)$ as multisets.

> **Reconstruction Conjecture (Kelly 1942/1957; Ulam 1960).** If $G$ and $H$ are finite simple graphs with $n \ge 3$ vertices and $\mathcal{D}(G) = \mathcal{D}(H)$, then $G \cong H$.

Equivalently: every finite simple graph on at least three vertices is determined up to isomorphism by its multiset of one-vertex-deleted induced subgraphs. Note the cards are *unlabelled* — this is what makes the problem hard; labelled reconstruction is trivial for $n \ge 3$.

A **proof** must show hypomorphism implies isomorphism for all $n \ge 3$. A **disproof** requires exhibiting a single pair $G \not\cong H$ on $n \ge 3$ vertices with identical decks. The hypothesis $n \ge 3$ is necessary: $K_2$ and $\overline{K_2}$ both have deck $\{\!\{K_1, K_1\}\!\}$.

A parameter or class is **reconstructible** if it takes the same value on all hypomorphic graphs; a class $\mathcal{C}$ is **recognizable** if $G \in \mathcal{C}$ and $\mathcal{D}(H) = \mathcal{D}(G)$ force $H \in \mathcal{C}$.

## 2. Mathematical Foundations

**Kelly's Counting Lemma (Kelly 1957).** For graphs $F, G$ let $s(F,G)$ denote the number of subsets $S \subseteq V(G)$ with $G[S] \cong F$. If $|V(F)| < |V(G)| = n$, then each such $S$ survives in exactly $n - |V(F)|$ cards, so
$$\sum_{v \in V(G)} s(F, G-v) = \bigl(n - |V(F)|\bigr)\, s(F,G),
\qquad\text{hence}\qquad
s(F,G) = \frac{1}{n - |V(F)|}\sum_{v \in V(G)} s(F, G-v).$$
Thus **every count of proper induced subgraphs is reconstructible**. Taking $F = K_2$ gives the edge count
$$m(G) = \frac{1}{n-2}\sum_{i=1}^{n} m(G - v_i),$$
and then the degree of the vertex deleted to make card $G-v_i$ is $d(v_i) = m(G) - m(G-v_i)$, so the **degree sequence** is reconstructible. The same lemma reconstructs the number of triangles, the characteristic polynomial (Tutte 1979), the chromatic polynomial, the Tutte polynomial, the number of spanning trees, connectedness, and the number of components.

**Kelly's Lemma for non-induced counts.** Writing $\mathrm{sub}(F,G)$ for the number of (not necessarily induced) copies of $F$, the same double count applies, and by inclusion–exclusion over the lattice of induced supergraphs the two families determine each other.

**Nash-Williams / Lovász counting.** For **edge reconstruction** (deck $\{\!\{G-e : e \in E(G)\}\!\}$, Harary's 1964 conjecture) the key identity is Lovász's:
$$\sum_{X \subseteq E(G)} (-1)^{|X|}\,[\,G - X \cong H\,] \quad\text{relations}$$
formalized as: if $G \not\cong H$ have the same edge deck with $m$ edges, then
$$2^{m-1} \le |\mathrm{Aut}(G)| \cdot \text{(orbit count)} \le n!,$$
Müller's condition. Explicitly, **Müller's theorem (1977):** if $2^{m-1} > n!$, i.e. roughly $m > n\log_2 n$, then $G$ is edge reconstructible. Lovász (1972) had the weaker $m > \binom{n}{2}/2$, improved by Nash-Williams (1978) to $m > \frac{1}{2}\binom{n}{2} - \frac{n}{2} + 1$ type bounds.

**Reconstruction number.** $\mathrm{rn}(G)$ is the least $k$ such that no graph $H \not\cong G$ shares $k$ cards with $G$ in the appropriate multiset sense; $\mathrm{rn}(G) = 3$ for almost all $G$ (Bollobás 1990).

**$\ell$-deck.** $\mathcal{D}_\ell(G)$ is the multiset of induced subgraphs on $\ell$ vertices. Kelly's lemma shows $\mathcal{D}_{n-1}$ determines $\mathcal{D}_\ell$ for all $\ell < n$, so reconstruction from small $\ell$ is strictly harder.

## 3. History & State of the Art (SOTA)

- **1942:** P. J. Kelly's PhD thesis under S. M. Ulam at Wisconsin poses the question and settles trees.
- **1957:** Kelly publishes *A congruence theorem for trees* (Pacific J. Math.), containing the counting lemma and the tree case.
- **1960:** Ulam states the problem in *A Collection of Mathematical Problems*, giving it wide circulation; "Ulam's conjecture" becomes standard usage.
- **1964:** Harary formulates the edge-reconstruction conjecture and coins "reconstruction".
- **1969:** Fisher gives a counterexample for countably infinite graphs, killing any hope of a general set-theoretic argument.
- **1972–1978:** Lovász, Müller and Nash-Williams establish the density thresholds for edge reconstruction — the strongest general-purpose counting results known.
- **1977:** Stockmeyer's infinite families of non-reconstructible tournaments and digraphs show the conjecture is false for directed graphs; Kocay later gives hypergraph counterexamples.
- **1990:** Bollobás proves almost every graph has reconstruction number 3 — three well-chosen cards suffice with probability $\to 1$.
- **1991:** Bondy's *A graph reconstructor's manual* becomes the canonical survey.
- **1997:** McKay's exhaustive computation verifies the conjecture for all graphs on $n \le 11$ vertices.
- **2019–2021:** Renewed activity on $\ell$-deck reconstruction (Spinoza–West; Kostochka–West; Groenland–Guggiari–Scott on size reconstructibility), driven partly by connections to trace reconstruction in information theory.

No approach has produced an unconditional proof for any dense unstructured class, and no counterexample search has come close to a candidate.

## 4. Partial Results / Verified Cases

**Computationally verified:** all simple graphs with $n \le 11$ vertices (McKay, 1997), covering $1{,}018{,}997{,}864$ graphs; extended by later independent recomputations and reconstruction-number databases through $n = 13$ for restricted families *(frontier — verify for the full range)*.

**Proven classes (all reconstructible):**
- Trees and forests (Kelly 1957).
- Disconnected graphs (Kelly 1957) — connectedness is recognizable and each component is smaller than $G$.
- Regular graphs (immediate: degree sequence + $\binom{n}{2}$-style counting; $G$ is determined by any single card plus the degree).
- Separable graphs with no end-vertices (Bondy).
- Maximal planar graphs (Fiorini–Lauri), outerplanar graphs (Giles 1974).
- Unicyclic graphs, cacti, and graphs with a cut vertex.
- Unit interval graphs (von Rimscha), critical blocks, squares of trees.
- Graphs with $n$ vertices and $m > n\log_2 n$ edges — **edge**-reconstructible (Müller 1977).
- Almost all graphs, in the $G(n,1/2)$ sense: reconstruction number $3$ with probability $1 - o(1)$ (Bollobás 1990).

**Reconstructible parameters:** $n$, $m$, degree sequence, connectivity status, number of components, characteristic polynomial, chromatic and Tutte polynomials, number of spanning trees, planarity (for $n$ large), and all induced-subgraph counts on $< n$ vertices.

**Known false in adjacent settings:** digraphs and tournaments (Stockmeyer 1977), hypergraphs (Kocay 1987), infinite graphs (Fisher 1969), and the $\ell$-deck for $\ell$ below roughly $\sqrt{n}$ — non-reconstructible pairs exist (Spinoza–West).

## 5. Principal Obstacles

- **Counting saturates.** Kelly's lemma reconstructs every *proper* subgraph count, but the one quantity that would finish the proof — $s(G,G) = 1$, i.e. whether $H$ contains a copy of $G$ — is exactly the case $|V(F)| = n$ where the denominator $n - |V(F)|$ vanishes. Every counting argument stops one step short by construction. This is the sharpest statement of the barrier.
- **Nash-Williams' lattice method plateaus.** The Lovász/Müller machinery works because $2^{m-1}$ beats $n!$ only when $m$ is large. For sparse graphs ($m = O(n)$) the inequality reverses, and the same technique gives nothing for vertex reconstruction at all, because there are only $n$ cards rather than $m$.
- **No local-to-global algebra.** The deck is a multiset of *isomorphism classes* — the labelling information is destroyed. Recovering a consistent labelling across cards is essentially a graph-isomorphism-hard alignment problem (Mansfield 1982: deciding whether a multiset is a legitimate deck is GI-hard; Kratsch–Hemaspaandra 1994 place reconstruction variants precisely relative to GI). So there is no polynomial certificate to exploit structurally.
- **Failure in every relaxation.** Digraphs, hypergraphs and infinite graphs all admit counterexamples, so any proof must use a property special to finite *undirected* graphs — symmetry of adjacency plus finiteness. No known technique isolates exactly that property; arguments general enough to be robust are general enough to prove the false statements.
- **The hard instances are the featureless ones.** Bollobás shows random graphs are easy. The plausible adversary is a highly regular, high-automorphism graph (strongly regular, vertex-transitive), where all cards are identical and carry minimal information — but for those the automorphism group itself pins the graph down. No one has found a class simultaneously card-poor and structure-poor, which is weak evidence the conjecture is true.

## 6. The Gap

Section 4 gives reconstruction for graphs that are sparse-and-structured (trees, disconnected, planar, unicyclic) or dense-and-random (Bollobás), plus edge reconstruction above $m > n\log_2 n$. The uncovered region is: **connected, 2-connected, non-regular graphs of intermediate density $\Theta(n)$ to $\Theta(n \log n)$ edges, with no forbidden-subgraph structure and small automorphism group but not generic.**

The precise missing step is a bridge from *all proper induced subgraph counts* to *the isomorphism type*. Formally: given $\mathcal{D}(G)$, Kelly's lemma yields the vector $\bigl(s(F,G)\bigr)_{|V(F)| < n}$; one must show this vector, together with $n$, determines $G$. Equivalently, that no two non-isomorphic $n$-vertex graphs have identical induced-subgraph profiles on all $\le n-1$ vertices. Every known route to that statement either (a) requires knowing one card's embedding into $G$, which the deck does not supply, or (b) requires a counting identity whose coefficient degenerates at $|V(F)| = n$.

## 7. Current Research (as of June 2026)

- **$\ell$-deck reconstruction.** Kostochka and West (Illinois) and coauthors ask for the least $\ell$ such that $\mathcal{D}_\ell(G)$ determines $G$ for a class. Known: trees on $n$ vertices are reconstructible from $\mathcal{D}_\ell$ for $\ell \ge (1+o(1))\sqrt{n\log n}$-type thresholds; graphs of maximum degree $k$ from $\mathcal{D}_\ell$ with $\ell$ polynomial in $k$ and $\log n$. *(frontier — verify constants)*
- **Size reconstruction from small decks.** Groenland, Guggiari and Scott proved the number of edges is determined by $\mathcal{D}_\ell$ for $\ell \ge c\sqrt{n\log n}$ (JGT, 2021), tightening Kelly-type counting well below $n-1$.
- **Information-theoretic transfer.** Cross-pollination with *trace reconstruction* (reconstructing a string from random subsequences) has imported concentration and complex-analytic tools; groups at Oxford, Cambridge, Illinois and the Rényi Institute pursue this.
- **Algorithmic/complexity angle.** Refinements of the Kratsch–Hemaspaandra placement of legitimate-deck and preimage-counting problems relative to GI, informed by Babai's quasipolynomial isomorphism algorithm.
- **Structural sub-classes.** Ongoing work on reconstructibility of chordal graphs, claw-free graphs, and graphs of bounded treewidth. *(frontier — verify)*

## 8. Future Work

- Push the edge-reconstruction density threshold below $m > n \log_2 n$ toward the conjectured $m > n$; Nash-Williams explicitly flagged closing the sparse gap as the natural next target.
- Prove reconstructibility for **2-connected planar graphs** in full, extending the maximal-planar and outerplanar results, as a test of whether topological structure suffices.
- Determine the exact threshold $\ell(n)$ for reconstruction of *all* graphs from the $\ell$-deck; the gap between the $\Omega(\sqrt{n})$ lower bound and known upper bounds is wide.
- Bondy's suggested route: find a reconstructible invariant that is *complete* (separates all isomorphism classes on $n$ vertices) — the counting lemma delivers many invariants but none complete.
- Settle Harary's **set reconstruction conjecture** (deck taken as a set, discarding multiplicities) for $n \ge 4$; a proof there would sharply constrain the multiset case.
- Explore whether spectral or algebraic-geometric encodings of the deck (e.g. as a point in a moduli space of subgraph densities) can be shown to have degree-one fibres.

## 9. Key References

- **[Foundational]** P. J. Kelly. *A congruence theorem for trees.* Pacific Journal of Mathematics, 7 (1957), 961–968.
- **[Foundational]** S. M. Ulam. *A Collection of Mathematical Problems.* Interscience Publishers, New York, 1960.
- **[Foundational]** F. Harary. *On the reconstruction of a graph from a collection of subgraphs.* In *Theory of Graphs and its Applications* (M. Fiedler, ed.), Academic Press, 1964, 47–52.
- **[Foundational]** L. Lovász. *A note on the line reconstruction problem.* Journal of Combinatorial Theory, Series B, 13 (1972), 309–310.
- **[Foundational]** V. Müller. *The edge reconstruction hypothesis is true for graphs with more than $n\log_2 n$ edges.* Journal of Combinatorial Theory, Series B, 22 (1977), 281–283.
- **[Counterexamples]** P. K. Stockmeyer. *The falsity of the reconstruction conjecture for tournaments.* Journal of Graph Theory, 1 (1977), 19–25.
- **[Counterexamples]** J. Fisher. *A counterexample to the countable version of a conjecture of Ulam.* Journal of Combinatorial Theory, 7 (1969), 364–365.
- **[SOTA]** B. Bollobás. *Almost every graph has reconstruction number three.* Journal of Graph Theory, 14 (1990), 1–4.
- **[SOTA]** B. D. McKay. *Small graphs are reconstructible.* Australasian Journal of Combinatorics, 15 (1997), 123–126.
- **[SOTA / Recent]** C. Groenland, H. Guggiari, A. Scott. *Size reconstructibility of graphs.* Journal of Graph Theory, 96 (2021), 326–337.
- **[SOTA / Recent]** A. V. Kostochka, D. B. West. *On reconstruction of graphs from the multiset of subgraphs obtained by deleting $\ell$ vertices.* IEEE Transactions on Information Theory, 67 (2021), 3278–3286.
- **[SOTA / Recent]** H. Spinoza, D. B. West. *Reconstruction from the deck of $k$-vertex induced subgraphs.* Journal of Graph Theory, 90 (2019), 497–522.
- **[Complexity]** D. Kratsch, L. A. Hemachandra. *On the complexity of graph reconstruction.* Mathematical Systems Theory, 27 (1994), 257–273.
- **[Complexity]** A. Mansfield. *The relationship between the computational complexities of the legitimate deck and isomorphism problems.* Quarterly Journal of Mathematics, 33 (1982), 345–347.
- **[Survey]** J. A. Bondy. *A graph reconstructor's manual.* In *Surveys in Combinatorics 1991*, London Math. Soc. Lecture Note Series 166, Cambridge University Press, 1991, 221–252.
- **[Survey]** C. St. J. A. Nash-Williams. *The reconstruction problem.* In *Selected Topics in Graph Theory* (L. W. Beineke, R. J. Wilson, eds.), Academic Press, 1978, 205–236.
- **[Survey]** J. A. Bondy, R. L. Hemminger. *Graph reconstruction — a survey.* Journal of Graph Theory, 1 (1977), 227–268.

## 10. Worked Example / Concrete Special Case

**Task.** Reconstruct the unique $G$ on $n = 4$ vertices with deck
$$\mathcal{D}(G) = \{\!\{\; P_3,\;\; P_3,\;\; K_2 \cup K_1,\;\; K_2 \cup K_1 \;\}\!\}.$$

**Step 1 — edge count by Kelly's lemma.** Card edge counts are $2, 2, 1, 1$. With $n = 4$:
$$m(G) = \frac{1}{n-2}\sum_i m(G - v_i) = \frac{2+2+1+1}{2} = 3.$$

**Step 2 — degree sequence.** $d(v_i) = m(G) - m(G-v_i)$, giving
$$d = (3-2,\; 3-2,\; 3-1,\; 3-1) = (1, 1, 2, 2),$$
which sums to $6 = 2m$, consistent.

**Step 3 — connectedness.** Every card is checked against the reconstructible component count; more directly, on $4$ vertices with $3$ edges and degree sequence $(1,1,2,2)$ the candidates are $P_4$ (path) and $K_3 \cup K_1$ (degrees $(2,2,2,0)$ — excluded) and the triangle-with-pendant "paw" (degrees $(1,2,2,3)$ — excluded). So $G \cong P_4$.

**Step 4 — verify.** Label $P_4 = a - b - c - d$. Deleting $a$ leaves $b-c-d \cong P_3$; deleting $d$ leaves $a-b-c \cong P_3$; deleting $b$ leaves $\{a\} \cup \{c-d\} \cong K_2 \cup K_1$; deleting $c$ leaves $\{a-b\} \cup \{d\} \cong K_2 \cup K_1$. The deck matches exactly.

**Step 5 — why $n \ge 3$ is required.** For $n = 2$, both $K_2$ and $\overline{K_2}$ have deck $\{\!\{K_1, K_1\}\!\}$; Kelly's lemma degenerates because $n - 2 = 0$ and the edge-count formula divides by zero. This single degeneracy is the miniature form of the barrier in Section 6: the counting identity always loses exactly one dimension of information, and at $n = 2$ that is all the information there is.

**Step 6 — where the method stops.** Applying Kelly's lemma to $F = K_3$ here gives $s(K_3, G) = \frac{1}{4-3}\sum_i s(K_3, G-v_i) = 0$, correctly recovering "triangle-free". But no choice of $F$ with $|V(F)| = 4$ is usable, since the coefficient $\frac{1}{n - |V(F)|}$ is undefined — for $n = 4$ the deduction had to be finished by an exhaustive case check over the $11$ graphs on four vertices. For general $n$ that case check is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*