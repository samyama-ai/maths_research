---
id: 07-combinatorics/erdos-gallai-conjecture
title: "Erdős-Gallai Path Decomposition Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Gallai Path Decomposition Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-gallai-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Erdős–Gallai / Gallai, 1966).** Every connected simple graph $G$ on $n$ vertices admits a decomposition of its edge set into at most $\lceil n/2 \rceil$ edge-disjoint paths.

A *decomposition* is a family $\mathcal{P} = \{P_1,\dots,P_k\}$ of subgraphs whose edge sets partition $E(G)$; every edge lies in exactly one $P_i$, and each $P_i$ is a path (possibly a single edge). Vertices may be reused across paths; only edges are constrained. The quantity
$$p(G) \;=\; \min\{\,|\mathcal{P}| : \mathcal{P} \text{ is a path decomposition of } G\,\}$$
is the **path number** of $G$. The conjecture asserts $p(G) \le \lceil n/2 \rceil$ for connected $G$.

The bound is sharp: for every $n$ there are connected graphs attaining it (Section 10). A complete proof must handle all connected graphs; a disproof requires one explicit connected $G$ with $p(G) \ge \lceil n/2\rceil + 1$, which by Lovász's theorem (Section 3) must contain cycles that cannot be absorbed into paths.

*Nomenclature.* The name "Erdős–Gallai conjecture" attaches to two related decomposition problems posed in the same 1960s Hungarian circle: this path version (usually credited to Gallai, reported by Lovász 1968) and the **cycle version** — every graph on $n$ vertices decomposes into $O(n)$ cycles and edges. This page treats the path version and records the cycle version as its companion in Sections 3 and 7.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, simple, undirected, $|V|=n$, $|E|=m$. Write $d_G(v)$ for degree and
$$O(G) = \{ v \in V : d_G(v) \equiv 1 \pmod 2 \}, \qquad o(G)=|O(G)|.$$

**Parity constraint.** Fix a decomposition $\mathcal{P}$. For $v\in V$, let $e(v)$ be the number of paths of $\mathcal{P}$ having $v$ as an endpoint and $i(v)$ the number having $v$ as an internal vertex. Every path through $v$ consumes two incident edges if $v$ is internal and one if $v$ is an endpoint, so
$$d_G(v) = 2\,i(v) + e(v), \qquad\text{hence}\qquad e(v)\equiv d_G(v)\pmod 2 .$$
Each odd-degree vertex is therefore an endpoint of at least one path. Counting endpoints ($2|\mathcal{P}| = \sum_v e(v)$) yields the universal lower bound
$$p(G) \;\ge\; \frac{o(G)}{2}.$$
If every vertex has odd degree, $p(G)\ge n/2$, which is exactly the conjectured value — such graphs are the extremal family.

**Lovász's theorem (1968).** For every graph $G$ on $n$ vertices, $E(G)$ decomposes into at most $\lfloor n/2 \rfloor$ paths *and cycles*. Consequently
$$p(G) \le \frac{o(G)}{2} + \Big(\text{number of cycles used}\Big),$$
and when $o(G)=n$ the decomposition is forced to be all paths, giving $p(G)=n/2$ exactly. The proof is by induction: split a vertex of even degree $\ge 2$ into two vertices, reducing the even-degree case to the odd one.

**Path cover vs. decomposition.** Relaxing "partition" to "cover" (edges may repeat) gives the path cover number $\rho(G)\le p(G)$. Fan (2002) proved $\rho(G)\le \lceil n/2\rceil$ for all connected $G$; the conjecture is that this survives the disjointness requirement.

**Companion (cycle) conjecture (Erdős–Gallai, 1966).** Every graph on $n$ vertices decomposes into $O(n)$ cycles and edges. The Erdős–Gallai extremal theorem on paths — a graph with no path on $k+1$ vertices has at most $\tfrac{(k-1)n}{2}$ edges (Erdős–Gallai 1959) — is the classical tool bounding path lengths available inside sparse graphs.

## 3. History & State of the Art (SOTA)

- **1959.** Erdős and Gallai publish *On maximal paths and circuits of graphs*, the extremal backdrop for all later path-packing work.
- **1966/1968.** Gallai poses the $\lceil n/2\rceil$ path decomposition conjecture; it is recorded in print by Lovász in the Tihany colloquium volume together with the theorem $p_{\text{paths+cycles}}(G)\le\lfloor n/2\rfloor$.
- **1980.** Donald proves $p(G)\le \lfloor 3n/4 \rfloor$ for connected $G$ — the first general bound below $n$.
- **1998–2000.** Yan (PhD thesis) and independently Dean–Kouider push this to $p(G)\le \lfloor 2n/3 \rfloor$; Dean and Kouider also handle disconnected graphs, where the right statement replaces $n$ by a per-component count.
- **1996.** Pyber proves every connected graph is *covered* by $n/2 + O(n^{3/4})$ paths, and that graphs whose even-degree vertices form an independent set satisfy the conjecture.
- **2002/2005.** Fan proves the covering version $\rho(G)\le\lceil n/2\rceil$ and then establishes the decomposition conjecture for large classes defined by block structure (e.g. every block with maximum degree $\le 3$, or Eulerian blocks with few edges relative to vertices).
- **2017–2020.** Structural classes fall: girth $\ge 4$ (Harding–McGuinness), maximum degree $\le 5$ (Bonamy–Perrett), treewidth $\le 3$ (Botler–Sambinelli–Coelho–Lee), triangle-free planar (Botler–Jiménez–Sambinelli).
- **2021–2023.** Dense-graph and asymptotic versions (Girão–Granet–Kühn–Osthus) settle the conjecture up to $o(n)$ error for graphs of large minimum degree. In parallel, Bucić and Montgomery bring the companion cycle conjecture from $O(n\log\log n)$ (Conlon–Fox–Sudakov) to $O(n\log^{*}n)$.

**SOTA summary.** General upper bound $\lfloor 2n/3\rfloor$; conjectured $\lceil n/2\rceil$; no improvement on the $2/3$ constant for arbitrary connected graphs in over two decades.

## 4. Partial Results / Verified Cases

| Class / parameter | Result | Source |
|---|---|---|
| All graphs, paths **and** cycles allowed | $\le \lfloor n/2\rfloor$ parts | Lovász 1968 |
| All degrees odd ($o(G)=n$) | $p(G)=n/2$ exactly | Lovász 1968 |
| Even-degree vertices form an independent set | $p(G)\le\lceil n/2\rceil$ | Pyber 1996 |
| Every block has $\Delta \le 3$; Eulerian blocks with $m\le \tfrac{5}{2}n_B$ | conjecture holds | Fan 2005 |
| Girth $\ge 4$ | improved sub-$2n/3$ bounds; conjecture for subclasses | Harding–McGuinness 2017 |
| $\Delta(G)\le 5$ | conjecture holds | Bonamy–Perrett 2019 |
| Treewidth $\le 3$ (includes series–parallel, $K_4$-minor-free) | conjecture holds | Botler–Sambinelli–Coelho–Lee 2020 |
| Triangle-free planar | conjecture holds | Botler–Jiménez–Sambinelli 2019 |
| $\delta(G)\ge(1-o(1))n$, $n$ large | $\lceil n/2\rceil$ paths, asymptotically exact | Girão–Granet–Kühn–Osthus 2021 |
| Complete graphs $K_n$ | $p(K_n)=\lceil n/2\rceil$ | classical (Lucas/Walecki decompositions) |
| Trees, and any graph with $o(G)$ close to $n$ | immediate from the endpoint count | — |
| Small $n$ (exhaustive `nauty` enumeration, $n\le 10$–$11$) | no counterexample found *(frontier — verify)* | computational folklore |

Graphs of maximum degree $\le 4$ follow from Fan's block criterion plus Bonamy–Perrett; the first genuinely open bounded-degree case is $\Delta=6$.

## 5. Principal Obstacles

- **Even-degree vertices give no leverage.** The parity lower bound $o(G)/2$ is what makes the odd case trivial. When many vertices have even degree, $o(G)/2$ can be $0$ (Eulerian graphs) while $p(G)$ is still $\approx n/2$; there is no matching lower-bound mechanism, so induction has nothing to push against.
- **Cycles are the whole difficulty.** Lovász already gives $\lfloor n/2\rfloor$ *parts*; the conjecture is exactly the assertion that the cycles can be avoided. But converting a cycle into path segments costs an extra part unless the cycle is grafted onto a path at a shared vertex, and grafting is blocked when the cycle's vertices already have all their edges internally used.
- **Induction destroys connectivity.** Deleting a path or contracting typically disconnects $G$ or creates components whose budgets $\lceil n_i/2\rceil$ sum to more than $\lceil n/2\rceil$. Dean–Kouider's disconnected formulation exists precisely because the naive induction leaks $+1$ per component.
- **Local switching arguments saturate.** Fan's edge-switching method (take a minimum decomposition, reroute at a vertex to reduce the count) yields covers cleanly but stalls for decompositions: switching can re-create a cycle elsewhere, and no potential function is known that decreases monotonically.
- **No LP/flow relaxation is tight.** Path decomposition is not a matroid or flow problem; the natural LP has fractional optimum near $o(G)/2$ and huge integrality gap on Eulerian graphs. Deciding $p(G)\le k$ is NP-hard, so no efficiently checkable certificate is expected.
- **Absorption needs density.** The probabilistic/absorbing techniques that solved dense-graph versions require $\delta(G)=\Omega(n)$ to build absorbers; sparse graphs — where extremal examples live — are outside their reach.

## 6. The Gap

Proven: $p(G) \le \lfloor 2n/3\rfloor$ in general; $p(G)\le\lceil n/2\rceil$ under a structural hypothesis that either (i) controls parity ($o(G)$ large, even-degree vertices independent), (ii) bounds local complexity ($\Delta\le5$, treewidth $\le3$, girth/planarity), or (iii) forces density ($\delta \ge (1-o(1))n$).

Conjectured: $p(G)\le\lceil n/2\rceil$ for **all** connected $G$.

The gap is the constant $\tfrac{2}{3}\to\tfrac12$ for graphs of *intermediate* degree with many even-degree vertices — sparse, high-girth, non-planar graphs with $\Delta \ge 6$ and $o(G)=o(n)$. Concretely, the missing step is: given a Lovász decomposition into $\lfloor n/2\rfloor$ paths and cycles with $c>0$ cycles, exhibit a rerouting that reduces the cycle count without increasing the total. No known argument produces such a rerouting when every cycle meets the rest of the decomposition only at vertices already internal to two paths. Even the weaker target $p(G)\le(\tfrac12+\varepsilon)n$ for a fixed small $\varepsilon>0$, for all connected graphs, is open.

## 7. Current Research (as of June 2026)

- **Bounded degree ladder.** Extending Bonamy–Perrett from $\Delta\le5$ to $\Delta\le6$ is the flagship target; the difficulty is that discharging arguments lose their surplus at degree 6. Preprints claiming $\Delta \le 6$ under extra girth assumptions circulate *(frontier — verify)*.
- **Minor-closed classes.** The Campinas/Rio group (Botler, Sambinelli, Lee, Jiménez) is pushing from treewidth $\le3$ toward treewidth $\le4$ and to all planar graphs; the triangle-free planar case is done, general planar is not *(frontier — verify)*.
- **Absorption for sparse graphs.** Birmingham-school techniques (Kühn, Osthus, Granet, Girão) are being adapted to lower the density threshold below $(1-o(1))n$, aiming at $\delta \ge cn$ for a fixed $c$.
- **Companion cycle conjecture.** After Bucić–Montgomery's $O(n\log^{*}n)$, effort focuses on removing the last iterated-log factor; techniques there (robust expander decompositions) are being tested for path versions.
- **Variants.** Decompositions into paths of bounded length, into trails, and the directed analogue (Alspach–Mason-type conjectures for digraphs) are active proxies.

## 8. Future Work

- Find a potential function on path-and-cycle decompositions that strictly decreases under a local switch, converting Lovász's theorem into the conjecture.
- Prove any bound $(\tfrac12+\varepsilon)n$ with $\varepsilon<\tfrac16$ for all connected graphs — the first improvement on $2n/3$ since 2000 would be a major event.
- Settle $\Delta\le6$, then aim at $\Delta \le \Delta_0$ for all $\Delta_0$ by an argument uniform in $\Delta$.
- Prove the conjecture for all planar graphs, removing the triangle-free hypothesis.
- Develop a robust-expander framework for path decomposition mirroring the Bucić–Montgomery cycle machinery.
- Extend exhaustive verification past $n=12$ with isomorph-free generation and ILP certificates, and publish the verified range.

## 9. Key References

- **[Foundational]** P. Erdős, T. Gallai. *On maximal paths and circuits of graphs.* Acta Mathematica Academiae Scientiarum Hungaricae 10 (1959), 337–356.
- **[Foundational]** L. Lovász. *On covering of graphs.* In: Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, 1968, 231–236.
- **[Bound]** A. Donald. *An upper bound for the path number of a graph.* Journal of Graph Theory 4 (1980), 189–201.
- **[Bound]** N. Dean, M. Kouider. *Gallai's conjecture for disconnected graphs.* Discrete Mathematics 213 (2000), 43–54.
- **[Bound]** L. Yan. *Path decompositions of graphs.* PhD thesis, Arizona State University, 1998.
- **[Covering]** L. Pyber. *Covering the edges of a connected graph by paths.* Journal of Combinatorial Theory Series B 66 (1996), 152–159.
- **[Covering]** G. Fan. *Subgraph coverings and edge switchings.* Journal of Combinatorial Theory Series B 84 (2002), 54–83.
- **[SOTA]** G. Fan. *Path decompositions and Gallai's conjecture.* Journal of Combinatorial Theory Series B 93 (2005), 117–125.
- **[SOTA]** M. Bonamy, T. J. Perrett. *Gallai's path decomposition conjecture for graphs of small maximum degree.* Discrete Mathematics 342 (2019), 1293–1299.
- **[SOTA]** F. Botler, M. Sambinelli, R. S. Coelho, O. Lee. *Gallai's path decomposition conjecture for graphs with treewidth at most 3.* Journal of Graph Theory 93 (2020), 328–349.
- **[SOTA]** F. Botler, A. Jiménez, M. Sambinelli. *Gallai's path decomposition conjecture for triangle-free planar graphs.* Discrete Mathematics 342 (2019), 1403–1414.
- **[SOTA]** P. Harding, S. McGuinness. *Gallai's conjecture for graphs of girth at least four.* Journal of Graph Theory 84 (2017), 413–423.
- **[Dense]** A. Girão, B. Granet, D. Kühn, D. Osthus. *Path and cycle decompositions of dense graphs.* Journal of the London Mathematical Society 104 (2021), 1085–1134.
- **[Companion]** M. Bucić, R. Montgomery. *Towards the Erdős–Gallai cycle decomposition conjecture.* Proc. STOC 2022; Advances in Mathematics 437 (2024).
- **[Companion]** D. Conlon, J. Fox, B. Sudakov. *Cycle packing.* Random Structures & Algorithms 45 (2014), 608–626.
- **[Survey]** J. A. Bondy. *Beautiful conjectures in graph theory.* European Journal of Combinatorics 37 (2014), 4–23.

## 10. Worked Example / Concrete Special Case

**Take $G=K_5$**, $n=5$, $m=10$, every degree $4$ (even), so $o(G)=0$ and the parity bound gives nothing.

*Lower bound.* A path in $K_5$ has at most $5$ vertices, hence at most $4$ edges. Any decomposition into $k$ paths satisfies $4k \ge 10$, so $k \ge 3 = \lceil 5/2\rceil$. Generally for $K_{2t+1}$: $m=t(2t+1)$, each path has $\le 2t$ edges, so $k \ge (2t+1)/2$, i.e. $k\ge t+1=\lceil n/2\rceil$ — the complete graphs of odd order are tight instances.

*Upper bound — explicit decomposition.* Label $V=\{1,2,3,4,5\}$, $E=\{12,13,14,15,23,24,25,34,35,45\}$.

- $P_1 = 1\!-\!2\!-\!3\!-\!4\!-\!5$ uses $\{12,23,34,45\}$
- $P_2 = 2\!-\!4\!-\!1\!-\!3\!-\!5$ uses $\{24,14,13,35\}$
- $P_3 = 1\!-\!5\!-\!2$ uses $\{15,25\}$

Edge counts $4+4+2=10$ and the three sets are pairwise disjoint, so this is a decomposition; $p(K_5)=3=\lceil 5/2\rceil$.

*Why the naive route fails.* $K_5$ is Eulerian and splits into two Hamiltonian cycles $C_1=1\,2\,3\,4\,5\,1$ and $C_2=1\,3\,5\,2\,4\,1$. Cutting one edge from each cycle gives $2$ paths plus $2$ leftover edges — $4$ paths, one over budget. The decomposition above works only because the leftover edges $15$ and $25$ share vertex $5$ and can be merged into the single path $1\!-\!5\!-\!2$. This merging step, trivial here, is exactly the operation nobody knows how to guarantee in general: it is the content of Section 6's gap.

*Endpoint check.* Endpoint multiset: $P_1:\{1,5\}$, $P_2:\{2,5\}$, $P_3:\{1,2\}$. So $e(1)=e(2)=e(5)=2$, $e(3)=e(4)=0$ — all even, matching $e(v)\equiv d(v)\equiv 0 \pmod 2$, and $\sum_v e(v)=6=2\cdot3$ as required.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*