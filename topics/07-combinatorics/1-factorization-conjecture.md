---
id: 07-combinatorics/1-factorization-conjecture
title: "1-Factorization Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# 1-Factorization Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/1-factorization-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a $D$-regular simple graph on an even number $n$ of vertices. A **1-factorization** is a partition of $E(G)$ into $D$ perfect matchings.

**Conjecture (1-factorization conjecture).** If
$$D \;\ge\; 2\left\lceil \frac{n}{4} \right\rceil - 1,$$
then $G$ has a 1-factorization.

Explicitly, the threshold is $D \ge n/2 - 1$ when $n \equiv 0 \pmod 4$ and $D \ge n/2$ when $n \equiv 2 \pmod 4$. A complete proof must produce a 1-factorization for **every** such $G$ at **every** even $n$; a disproof needs a single $D$-regular graph meeting the degree bound whose edge set admits no such partition. The conjecture is known for all sufficiently large $n$ (Csaba–Kühn–Lo–Osthus–Treglown, 2016); it is open for small and moderate $n$, since that proof gives no usable $n_0$.

## 2. Mathematical Foundations

**Edge colouring.** A proper edge colouring assigns colours to $E(G)$ so that adjacent edges differ; $\chi'(G)$ is the least number of colours. For $D$-regular $G$ on even $n$,
$$G \text{ is 1-factorizable} \iff \chi'(G) = D \iff G \text{ is Class 1},$$
because each colour class in a $D$-colouring of a $D$-regular graph is a perfect matching.

**Vizing's theorem (1964).** For simple $G$, $\Delta(G) \le \chi'(G) \le \Delta(G)+1$. So the conjecture asserts that high-degree regular graphs of even order fall on the lower side of Vizing's dichotomy.

**Overfullness.** A subgraph $H \subseteq G$ is *overfull* if $|V(H)|$ is odd and
$$|E(H)| \;>\; \Delta(G)\left\lfloor \frac{|V(H)|}{2} \right\rfloor .$$
Overfullness forces $\chi'(G) > \Delta(G)$: each colour class meets an odd set in at most $\lfloor |V(H)|/2\rfloor$ edges. The **overfull conjecture** (Chetwynd–Hilton) says that for $\Delta(G) > n/3$ this is the only obstruction; the 1-factorization conjecture is its regular, even-order special case.

**Sharpness.** For $n \equiv 2 \pmod 4$, $K_{n/2} \,\dot\cup\, K_{n/2}$ is $(n/2-1)$-regular with two odd components, hence has no perfect matching at all. For $n \equiv 0 \pmod 4$, take $K_{n/2-1} \,\dot\cup\, H$ with $H$ any $(n/2-2)$-regular graph on $n/2+1$ vertices; both orders are odd, so again no 1-factor. Thus $2\lceil n/4\rceil - 1$ cannot be lowered.

**Easy sufficient conditions.** König's theorem gives $\chi'(G) = \Delta(G)$ for bipartite $G$, so bipartite regular graphs are always 1-factorizable, at any degree.

**Companion statement.** The same machinery settles the **Hamilton decomposition conjecture** (Nash-Williams): every $D$-regular graph on $n$ vertices with $D \ge \lfloor n/2 \rfloor$ decomposes into Hamilton cycles plus at most one perfect matching.

## 3. History & State of the Art (SOTA)

- **1847.** Kirkman's round-robin schedule: $K_{2m}$ has a 1-factorization — the $D = n-1$ case.
- **1950s–1985.** The conjecture circulated as folklore (often attributed to Dirac's circle) and was first stated in print by Chetwynd and Hilton, *Regular graphs of high degree are 1-factorizable*, Proc. LMS 1985, together with a proof for $D \ge \tfrac{6}{7}n$.
- **1989–1990.** Threshold improved to $D \ge \tfrac{1}{2}(\sqrt{7}-1)n \approx 0.8229n$, independently by Chetwynd–Hilton (Discrete Math., 1989) and Niessen–Volkmann (J. Graph Theory, 1990).
- **1997.** Perković and Reed prove the conjecture for $D \ge n/2 + \varepsilon n$ and $n$ large — the first result reaching the correct order of the threshold, using probabilistic edge-colouring and Reed-style structural decomposition.
- **2013.** Vaughan proves an asymptotic multigraph analogue.
- **2016.** Csaba, Kühn, Lo, Osthus and Treglown, *Proof of the 1-factorization and Hamilton decomposition conjectures* (Memoirs AMS 244, no. 1154; arXiv 2014) prove the exact statement for all $n \ge n_0$, via Szemerédi regularity, robust expander decompositions (Kühn–Osthus), absorption, and a separate treatment of graphs close to the two extremal configurations.

SOTA is therefore: **exact for large $n$, unquantified $n_0$, open below it.** The wider overfull conjecture remains fully open.

## 4. Partial Results / Verified Cases

- **$D = n-1$:** $K_n$, $n$ even — Kirkman, 1847.
- **$D = n-2$:** $K_n$ minus a perfect matching — classical.
- **$D \ge n-3$:** the complement has maximum degree $\le 2$ (a union of paths and cycles); explicit constructions and Plantholt's chromatic-index results for graphs with a spanning star cover these cases.
- **Bipartite regular graphs:** all degrees, by König.
- **$D \ge \tfrac{6}{7}n$:** Chetwynd–Hilton 1985.
- **$D \ge 0.8229n$:** Chetwynd–Hilton 1989; Niessen–Volkmann 1990.
- **$D \ge (1/2+\varepsilon)n$, $n \ge n_0(\varepsilon)$:** Perković–Reed 1997.
- **$D \ge 2\lceil n/4 \rceil - 1$, $n \ge n_0$:** Csaba–Kühn–Lo–Osthus–Treglown 2016.
- **Small orders:** $n \le 8$ is settled by hand (see §10 for $n=8$, $D=3$); $n = 10, 12$ are within reach of exhaustive generation with `geng`/`nauty` plus an exact edge-colouring solver, though no such enumeration appears in the refereed literature.
- **Cubic case context:** the conjecture at $n = 8$ reduces to the fact that no cubic Class-2 graph has fewer than 10 vertices.

## 5. Principal Obstacles

- **No structural characterization of Class 2.** Holyer (1981) proved deciding $\chi'(G)=3$ for cubic graphs is NP-complete, so no polynomial-checkable certificate for Class 1 is expected in general. Any proof must exploit high degree specifically, not edge-colouring theory as such.
- **Vizing fans and Kempe chains saturate.** The classical recolouring toolkit (fans, Kempe chain interchanges, critical-graph adjacency lemmas) yields bounds of the form $D \ge cn$ with $c$ bounded away from $1/2$; recolouring arguments lose control once the number of "missing colours" at a vertex is $\Theta(n)$, which is exactly the regime near $n/2$.
- **Two extremal families sit at the threshold.** Graphs near $K_{n/2}\dot\cup K_{n/2}$ (a near-disconnected pair of cliques) and graphs near the complete bipartite structure both fail generic arguments and must be handled by separate ad hoc constructions. Any uniform method has to interpolate between them.
- **Regularity-method costs.** The 2016 proof uses the Szemerédi regularity lemma inside a robust-expander decomposition; the tower-type dependence makes $n_0$ astronomical and non-explicit. Regularity is also blind to $o(n^2)$ edge sets, yet the difference between a 1-factorization and a near-1-factorization is a single perfect matching, i.e. $n/2$ edges.
- **Exactness.** Approximate decompositions (covering $(1-o(1))|E(G)|$) are comparatively easy; forcing the *last* few matchings to be perfect requires absorption structures that are fragile precisely at the sharp threshold.

## 6. The Gap

Proven: the statement for $n \ge n_0$ where $n_0$ arises from regularity and is not extracted. Claimed: all even $n$. The gap has two components.

1. **Quantitative.** Replace regularity/absorption by an argument with explicit constants, bringing $n_0$ down to a computationally checkable value (say $n_0 \le 10^2$), then close the residual finite range by exhaustive search. This is a de-asymptotization problem, not a new-idea problem — but no regularity-free proof of the $D \ge (1/2+\varepsilon)n$ case is known either.
2. **Structural.** Prove the overfull conjecture for $\Delta > n/3$, which would give the 1-factorization conjecture at all $n$ as an immediate corollary, since a regular graph of even order contains no overfull subgraph. This is strictly harder and currently has no viable attack.

## 7. Current Research (as of June 2026)

- **Birmingham/Warwick school (Kühn, Osthus, Lo, Treglown and co-authors):** continued development of robust expanders and absorption for exact decomposition problems — Hamilton decompositions, resolvable designs, hypergraph matchings. Effort is directed at new targets rather than at reducing $n_0$ for this conjecture.
- **Iterative absorption and regularity-free methods** (Glock, Joos, Kühn, Osthus and collaborators) have removed the regularity lemma from several decomposition theorems. Applying the same programme here to obtain an explicit $n_0$ is a stated but unrealized goal *(frontier — verify)*.
- **Overfull conjecture:** work by Hilton's school and by Cao, Chen, Jing, Shan and collaborators on Class-2 criteria and Goldberg–Seymour-adjacent multigraph colouring continues; the Goldberg–Seymour conjecture's resolution (Chen–Jing–Zang) has renewed interest in whether similar polyhedral/fractional arguments reach the simple-graph overfull setting *(frontier — verify)*.
- **Computational:** SAT/ILP edge-colouring pipelines over `nauty`-generated regular graphs make full verification for $n \le 14$ plausible; no published certified enumeration exists.

## 8. Future Work

- Extract an explicit $n_0$ from the Csaba–Kühn–Lo–Osthus–Treglown proof, or reprove the $D \ge (1/2+\varepsilon)n$ regime by nibble/absorption without regularity.
- Verify $10 \le n \le 16$ exhaustively with machine-checkable certificates, publishing the search.
- Prove the overfull conjecture for regular graphs of even order — a strictly stronger, cleaner statement.
- Extend to multigraphs with bounded multiplicity, sharpening Vaughan's asymptotic result.
- Seek a purely local, Vizing-fan-based proof for $D \ge (1-\varepsilon)n$ with small explicit $\varepsilon$, to test whether recolouring can in principle reach $n/2$.

## 9. Key References

- **[Foundational]** V. G. Vizing. *On an estimate of the chromatic class of a p-graph.* Diskret. Analiz 3 (1964), 25–30.
- **[Foundational]** A. G. Chetwynd, A. J. W. Hilton. *Regular graphs of high degree are 1-factorizable.* Proceedings of the London Mathematical Society (3) 50 (1985), 193–206.
- **[Foundational]** A. G. Chetwynd, A. J. W. Hilton. *1-factorizing regular graphs of high degree — an improved bound.* Discrete Mathematics 75 (1989), 103–112.
- **[Partial]** T. Niessen, L. Volkmann. *Class 1 conditions depending on the minimum degree and the number of vertices of maximum degree.* Journal of Graph Theory 14 (1990), 225–246.
- **[Partial]** L. Perković, B. Reed. *Edge coloring regular graphs of high degree.* Discrete Mathematics 165/166 (1997), 567–578.
- **[SOTA]** B. Csaba, D. Kühn, A. Lo, D. Osthus, A. Treglown. *Proof of the 1-factorization and Hamilton decomposition conjectures.* Memoirs of the American Mathematical Society 244 (2016), no. 1154.
- **[SOTA]** E. R. Vaughan. *An asymptotic version of the multigraph 1-factorization conjecture.* Journal of Graph Theory 72 (2013), 19–29.
- **[Technique]** D. Kühn, D. Osthus. *Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments.* Advances in Mathematics 237 (2013), 62–146.
- **[Complexity]** I. Holyer. *The NP-completeness of edge-colouring.* SIAM Journal on Computing 10 (1981), 718–720.
- **[Related]** M. Plantholt. *The chromatic index of graphs with a spanning star.* Journal of Graph Theory 5 (1981), 45–53.
- **[Survey]** M. Stiebitz, D. Scheide, B. Toft, L. M. Favrholdt. *Graph Edge Coloring: Vizing's Theorem and Goldberg's Conjecture.* Wiley, 2012.
- **[Survey]** W. D. Wallis. *One-Factorizations.* Kluwer Academic Publishers, 1997.

## 10. Worked Example / Concrete Special Case

**Case $n = 8$.** The threshold is $2\lceil 8/4\rceil - 1 = 3$, so the conjecture claims: *every cubic graph on 8 vertices is 1-factorizable.*

*Proof.* Let $G$ be cubic on 8 vertices and suppose $G$ is Class 2, i.e. $\chi'(G)=4$.

1. **$G$ has no bridge.** Suppose $uv$ is a bridge and $A$ is the vertex set of the component of $G-uv$ containing $u$, $|A| = k$. Degrees inside $A$ sum to $3k-1$, which must be even, so $k$ is odd. If $k=1$, $u$ has degree 1 — impossible. If $k=3$, one vertex of $A$ has 2 neighbours in $A$ and the other two have 3 each, but a simple graph on 3 vertices has maximum degree 2 — impossible. So $k \ge 5$ on both sides, forcing $|V(G)| \ge 10$. Contradiction.
2. **$G$ is bridgeless and cubic**, so by definition a Class-2 bridgeless cubic graph is a snark (allowing trivial ones). Every cubic Class-2 graph on fewer than 10 vertices would have to be one; the smallest such graph is the Petersen graph, on 10 vertices.

Hence no cubic Class-2 graph on 8 vertices exists, and every cubic $G$ on 8 vertices splits into 3 perfect matchings. $\square$

**Sharpness at $n = 8$.** Drop the degree to $D = 2 = n/2 - 2$. Take $G = C_3 \,\dot\cup\, C_5$: 2-regular, 8 vertices, and both components have odd order, so $G$ has no perfect matching whatsoever — not merely no 1-factorization. This realizes the $n \equiv 0 \pmod 4$ extremal family of §2 and shows the bound $D \ge 3$ is exactly right here.

**Explicit factorization, $D = 3$.** Let $G$ be the cube $Q_3$, vertices $\{0,1\}^3$, edges joining strings differing in one coordinate. The three matchings
$$M_i = \{\, xy : x \text{ and } y \text{ differ exactly in coordinate } i \,\}, \quad i = 1,2,3,$$
each pair up all 8 vertices ($x \mapsto x + e_i$ is a fixed-point-free involution), are pairwise disjoint, and together contain all $3\cdot 4 = 12$ edges. That is a 1-factorization, and $Q_3$ is bipartite, so König already guarantees it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*