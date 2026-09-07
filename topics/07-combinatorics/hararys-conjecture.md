---
id: 07-combinatorics/hararys-conjecture
title: "Harary's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Harary's Conjecture (Edge Reconstruction Conjecture)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hararys-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple undirected graph with edge set $E(G)$, $|E(G)| = m$. The **edge deck** of $G$ is the multiset of isomorphism classes
$$\mathcal{D}_e(G) = \{\!\{\, G - e \;:\; e \in E(G) \,\}\!\},$$
one card per edge, cards taken up to isomorphism (so the labelling of $G$ is forgotten).

**Conjecture (Harary, 1964).** Every finite simple graph with at least $4$ edges is *edge reconstructible*: if $G$ and $H$ are simple graphs with $m \ge 4$ edges and $\mathcal{D}_e(G) = \mathcal{D}_e(H)$ as multisets, then $G \cong H$.

Conventions and constraints:

- **Simple** is essential: the conjecture is false for multigraphs and for digraphs.
- **Finite** is essential: it fails for infinite graphs.
- Isolated vertices carry no edges and are conventionally discarded; equivalently one restricts to graphs with no isolated vertices, since $n$ is not recoverable from $\mathcal{D}_e(G)$ otherwise.
- The bound $m \ge 4$ is sharp: $K_3$ and $K_{1,3}$ have identical edge decks (Section 10).

A **proof** must show that the map $G \mapsto \mathcal{D}_e(G)$ is injective on isomorphism classes of simple graphs with $m\ge 4$. A **disproof** requires one pair $G \not\cong H$, both simple, with equal edge decks — a *hypomorphic* pair.

## 2. Mathematical Foundations

Write $s(F,G)$ for the number of subgraphs of $G$ isomorphic to $F$ (spanning the same vertex set is not required; $F$ ranges over graphs without isolated vertices), and $e(F)$ for its edge count. A parameter $p(G)$ is **edge-reconstructible** if it is determined by $\mathcal{D}_e(G)$.

**Kelly's Lemma (edge form).** For any $F$ with $e(F) < m$,
$$\sum_{i=1}^{m} s(F, G_i) \;=\; \bigl(m - e(F)\bigr)\, s(F,G), \qquad \mathcal{D}_e(G) = \{\!\{G_1,\dots,G_m\}\!\}.$$
Each copy of $F$ in $G$ survives in exactly $m - e(F)$ cards. Hence **every subgraph count $s(F,G)$ with $e(F) < m$ is edge-reconstructible**, and so are $m$, the degree sequence, the number of triangles, the chromatic polynomial's low-order data, and connectivity. The whole conjecture reduces to recovering the single missing number $s(G,G)=1$ — that is, deciding $F = G$ at $e(F)=m$.

**Lovász's counting bound (1972).** If
$$m > \tfrac{1}{2}\binom{n}{2} = \frac{n(n-1)}{4},$$
then $G$ is edge reconstructible. Proof idea: for a hypomorphic pair, an inclusion–exclusion over the $2^m$ subgraphs of $G$ forces $2^{m-1}$ to be at most the number of subgraphs of $K_n$ with $\ge$ half the edges, a contradiction.

**Müller's bound (1977).** If
$$2^{\,m-1} > n!,$$
then $G$ is edge reconstructible. Since $n! < n^n$, this holds whenever $m > n\log_2 n + 1$. The argument (Nash-Williams' lemma) compares $2^{m-1}$ — a lower bound on the number of distinguishable "sub-multisets" — with $n!/|\operatorname{Aut}(G)| \le n!$, the number of labelled copies of $G$ on $[n]$.

**Greenwell's implication (1971).** Vertex reconstructibility $\Rightarrow$ edge reconstructibility for $m \ge 4$. So Harary's conjecture is *weaker* than the Kelly–Ulam reconstruction conjecture, and any class settled for vertex decks is settled here.

## 3. History & State of the Art (SOTA)

- **1942/1957.** Ulam and Kelly pose vertex reconstruction; Kelly proves it for trees and establishes Kelly's Lemma.
- **1964.** Frank Harary, at the Prague symposium *Theory of Graphs and its Applications*, formulates the edge-deck version and asks whether $m\ge 4$ suffices — the conjecture now carrying his name.
- **1971.** Greenwell shows edge reconstruction is implied by vertex reconstruction, fixing the logical hierarchy.
- **1972.** Lovász's two-page note gives the first density bound $m > n(n-1)/4$.
- **1977.** Müller sharpens this to $2^{m-1} > n!$, i.e. roughly $m \gtrsim n\log_2 n$ — still the governing general bound in 2026. It implies **almost all graphs** (in $G(n,1/2)$) are edge reconstructible, since $m \sim n^2/4 \gg n\log_2 n$ whp.
- **1978.** Nash-Williams' survey chapter systematises the counting method.
- **1987–1991.** Structural era: Godsil–Krasikov–Roditty extend to $k$-edge-deleted decks; Krasikov–Roditty develop balance equations; Ellingham–Pyber prove bidegreed graphs, and Ellingham–Pyber–Yu claw-free graphs, are edge reconstructible.
- **1997.** McKay verifies vertex reconstruction for all graphs on $n \le 11$ vertices; via Greenwell this certifies edge reconstruction there too.
- **1991–present.** No improvement to the *order* of Müller's bound has been published. Bondy's "reconstructor's manual" remains the standard reference frame.

## 4. Partial Results / Verified Cases

Edge reconstruction is **proved** for:

| Class / regime | Source |
|---|---|
| $m > n(n-1)/4$ | Lovász 1972 |
| $2^{m-1} > n!$ (so $m > n\log_2 n + 1$) | Müller 1977 |
| All graphs with $n \le 11$ vertices (computational) | McKay 1997 (via Greenwell) |
| Trees with $m\ge4$, disconnected graphs, regular graphs | Kelly 1957 + Greenwell 1971 |
| Bidegreed graphs (exactly two distinct degrees) | Ellingham–Pyber 1988 |
| Claw-free graphs ($K_{1,3}$-free) | Ellingham–Pyber–Yu 1991 |
| Graphs with $\ge 3$ vertices of maximum degree $n-1$ | Standard counting corollary |
| Almost all graphs (probability $\to 1$ in $G(n,1/2)$) | Müller 1977 |
| Every parameter $s(F,G)$ with $e(F)<m$; degree sequence, $m$, connectivity, triangle count | Kelly's Lemma |

**Counterexamples outside the hypotheses.** Digraphs: infinite families of non-edge-reconstructible pairs exist (Stockmeyer's tournament constructions for vertex decks propagate). Multigraphs and infinite graphs: false (Fisher's infinite counterexample). Hypergraphs: false in general. These delimit exactly how much of the simple-finite hypothesis is load-bearing.

## 5. Principal Obstacles

- **Counting saturates.** Kelly's Lemma delivers *all* $s(F,G)$ for $e(F)<m$ and nothing at $e(F)=m$. The single unknown is precisely the answer. Every purely enumerative refinement — Lovász's, Müller's, Krasikov–Roditty's balance equations — is an inequality between $2^{m-1}$ and $n!/|\operatorname{Aut}(G)|$, and such inequalities are useless in the sparse regime $m = O(n)$ where $n!$ dominates. This is a hard ceiling, not a technical gap: the method has no term sensitive to sparse structure.
- **The sparse regime is where the difficulty lives.** Dense graphs are done. Sparse graphs of large girth with trivial automorphism group and no forced local structure — the natural adversary — are exactly the ones with $m \approx cn$, far below $n\log_2 n$.
- **No algebraic invariant is known to separate hypomorphs.** Spectral data does not suffice: cospectral non-isomorphic graphs abound, and the characteristic polynomial is edge-reconstructible without settling the problem.
- **Automorphism groups cut the wrong way.** Müller's bound improves to $2^{m-1} > n!/|\operatorname{Aut}(G)|$, so *symmetric* graphs are easier. The hard cases are asymmetric, and almost all sparse graphs are asymmetric.
- **Category-level failure of the statement.** Because the conjecture is false for digraphs, multigraphs, infinite graphs, and hypergraphs, any proof must use a property of finite simple graphs not shared by those categories. This kills every proof strategy that is functorial or purely combinatorial-species-theoretic, and explains why no "soft" argument has ever worked.

## 6. The Gap

Proved: edge reconstructibility whenever $m$ exceeds roughly $n\log_2 n$, plus scattered structural classes. Conjectured: $m \ge 4$.

The gap is the interval
$$4 \;\le\; m \;\lesssim\; n\log_2 n,$$
i.e. all sparse graphs. In counting terms, one must replace the inequality
$$2^{\,m-1} \;>\; \frac{n!}{|\operatorname{Aut}(G)|}$$
by an argument that survives when $2^{m-1}$ is *exponentially smaller* than $n!$ — a factor of $n^{\Theta(n)}$ deficit at $m = \Theta(n)$. Equivalently: find a family of edge-reconstructible invariants that are **not** of the form $s(F,\cdot)$ with $e(F)<m$, or prove that hypomorphic sparse pairs force a rigid local structure that can be excluded directly.

## 7. Current Research (as of June 2026)

- **Structural/local approach.** Extend the Ellingham–Pyber–Yu line: prove edge reconstruction for classes defined by forbidden induced subgraphs or bounded degeneracy. Bounded-treewidth and $H$-minor-free classes are the natural next targets, with progress reported for graphs of bounded degree and large girth *(frontier — verify)*.
- **Algebraic / representation-theoretic.** Reformulate the deck map as a linear operator between permutation modules of $S_n$ and study its kernel — the "reconstruction matrix" viewpoint developed from Godsil–Krasikov–Roditty and Kocay's identities. Injectivity of the $m$-th level operator on the relevant $S_n$-isotypic components is equivalent to the conjecture.
- **Computational search.** Extending McKay-style exhaustive canonical-form searches beyond $n = 13$ for hypomorphic pairs; the search space grows super-exponentially and no pair has been found *(frontier — verify)*.
- **Groups active.** Combinatorics groups working on reconstruction include those at Vanderbilt (Ellingham), the Australian National University / `nauty` ecosystem (McKay), the Alfréd Rényi Institute (Pyber's school), and the University of Malta reconstruction group (Lauri, Scapellato), which maintains the modern survey literature.

## 8. Future Work

1. **Break $n\log_2 n$.** Any bound of the form $m > cn$ for a constant $c$ would be the first order-of-magnitude advance since 1977 and would reduce the problem to bounded average degree.
2. **Sparse-graph invariants.** Construct edge-reconstructible invariants sensitive to $m = \Theta(n)$ structure — cycle-space or homology-flavoured data rather than subgraph counts.
3. **Isolate the finite-simple hypothesis.** Identify the exact property distinguishing simple graphs from the digraph/multigraph counterexamples, then build a proof around it; this is Bondy's stated programme criterion for a "legitimate" attack.
4. **Complete the class atlas.** Perfect graphs, planar graphs, and graphs of bounded genus remain open for edge reconstruction (planar *vertex* reconstruction is also open) and would be high-value scalps.
5. **Formalisation.** Machine-checked versions of Kelly's Lemma, Lovász's and Müller's bounds would give a verified foundation for computational case analyses.

## 9. Key References

- **[Foundational]** F. Harary. *On the reconstruction of a graph from a collection of subgraphs.* In: Theory of Graphs and its Applications (Proc. Sympos. Smolenice 1963), Publ. House Czechoslovak Acad. Sci., Prague, 1964, pp. 47–52.
- **[Foundational]** P. J. Kelly. *A congruence theorem for trees.* Pacific Journal of Mathematics 7 (1957), 961–968.
- **[Foundational]** L. Lovász. *A note on the line reconstruction problem.* Journal of Combinatorial Theory, Series B 13 (1972), 309–310.
- **[Key bound]** V. Müller. *The edge reconstruction hypothesis is true for graphs with more than $n\log_2 n$ edges.* Journal of Combinatorial Theory, Series B 22 (1977), 281–283.
- **[Structural]** D. L. Greenwell. *Reconstructing graphs.* Proceedings of the American Mathematical Society 30 (1971), 431–433.
- **[SOTA]** M. N. Ellingham, L. Pyber. *Bidegreed graphs are edge reconstructible.* Journal of Graph Theory 12 (1988), 405–412.
- **[SOTA]** M. N. Ellingham, L. Pyber, X. Yu. *Claw-free graphs are edge reconstructible.* Journal of Graph Theory 15 (1991), 445–451.
- **[SOTA]** C. D. Godsil, I. Krasikov, Y. Roditty. *Reconstructing graphs from their $k$-edge deleted subgraphs.* Journal of Combinatorial Theory, Series B 43 (1987), 360–363.
- **[Computational]** B. D. McKay. *Small graphs are reconstructible.* Australasian Journal of Combinatorics 15 (1997), 123–126.
- **[Survey]** J. A. Bondy. *A graph reconstructor's manual.* In: Surveys in Combinatorics 1991, London Math. Soc. Lecture Note Series 166, Cambridge University Press, 1991, pp. 221–252.
- **[Survey]** J. A. Bondy, R. L. Hemminger. *Graph reconstruction — a survey.* Journal of Graph Theory 1 (1977), 227–268.
- **[Survey]** C. St. J. A. Nash-Williams. *The reconstruction problem.* In: Selected Topics in Graph Theory (L. W. Beineke, R. J. Wilson, eds.), Academic Press, 1978, pp. 205–236.
- **[Book]** J. Lauri, R. Scapellato. *Topics in Graph Automorphisms and Reconstruction*, 2nd ed. Cambridge University Press, 2016.

## 10. Worked Example / Concrete Special Case

**(a) Why $m \ge 4$ is sharp.** Take $G = K_3$ (triangle, $m=3$) and $H = K_{1,3}$ (star, $m=3$). Deleting any edge of $K_3$ leaves a path $P_3$ on two edges. Deleting any edge of $K_{1,3}$ leaves $P_3$ plus an isolated vertex, which the convention discards. So
$$\mathcal{D}_e(K_3) = \{\!\{P_3,P_3,P_3\}\!\} = \mathcal{D}_e(K_{1,3}), \qquad K_3 \not\cong K_{1,3}.$$
Hence $m=3$ genuinely fails, and $m\ge4$ is the correct threshold.

**(b) All 4-vertex graphs are edge reconstructible, by Lovász.** With $n=4$, Lovász's condition reads $m > n(n-1)/4 = 3$, i.e. $m\ge4$ — exactly Harary's hypothesis. So the conjecture is a *theorem* for $n=4$ with no case checking.

**(c) Reconstructing $C_4$ from its deck by counting.** Let $\mathcal{D}_e = \{\!\{P_4,P_4,P_4,P_4\}\!\}$, four copies of the 3-edge path.

1. $m = |\mathcal{D}_e| = 4$.
2. Degree sequence: each card $P_4$ has degrees $(1,2,2,1)$, total degree sum $6$ per card. Summing over the deck and applying Kelly's Lemma with $F = K_2$: $s(K_2,G) = m = 4$ and each vertex loses degree once per incident edge. The multiset of degrees is forced to $(2,2,2,2)$ — a $2$-regular graph on $4$ vertices.
3. Triangle count: take $F = K_3$, $e(F)=3 < 4$. Cards contain $0$ triangles, so $s(K_3,G) = \frac{1}{4-3}\sum_i s(K_3,G_i) = 0$.
4. The only $2$-regular simple graph on $4$ vertices is $C_4$; it is triangle-free, consistent. Therefore $G \cong C_4$. $\blacksquare$

The same script fails to close in general because step 4 — "the invariants determined so far pin down a unique graph" — has no proof beyond the sparse-regime gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*