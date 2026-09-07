---
id: 07-combinatorics/erdos-sos-conjecture
title: "Erdős-Sós Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Sós Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-sos-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Erdős–Sós, 1963).** Let $k \ge 1$ and let $G$ be a simple graph on $n$ vertices with
$$e(G) > \frac{(k-1)n}{2}.$$
Then $G$ contains every tree $T$ with $k$ edges as a subgraph (not necessarily induced, not necessarily spanning).

Equivalently, in extremal-function language: for every tree $T$ with $k$ edges,
$$\mathrm{ex}(n, T) \le \frac{(k-1)n}{2},$$
where $\mathrm{ex}(n,T)$ is the maximum number of edges in a $T$-free graph on $n$ vertices. Equivalently again: average degree $\bar d(G) > k-1$ forces a copy of every $k$-edge tree.

A complete proof must handle **all** trees $T$ with $k$ edges and **all** host graphs $G$ simultaneously; the hypothesis is purely a global edge count, with no assumption on $\Delta(G)$, $\delta(G)$, connectivity, or $n$ versus $k$. A disproof requires exhibiting one tree $T_0$ with $k_0$ edges and one graph $G_0$ with $e(G_0) > (k_0-1)|V(G_0)|/2$ containing no copy of $T_0$.

## 2. Mathematical Foundations

Let $G=(V,E)$ be simple, $n = |V|$, $e(G)=|E|$, $\deg_G(v)$ the degree of $v$, and
$$\bar d(G) = \frac{2e(G)}{n}, \qquad \delta(G) = \min_v \deg_G(v), \qquad \Delta(G) = \max_v \deg_G(v).$$
A *tree* $T$ with $k$ edges has $k+1$ vertices. "$G$ contains $T$" means there is an injection $\varphi: V(T)\to V(G)$ with $\varphi(x)\varphi(y)\in E(G)$ for all $xy\in E(T)$.

**Sharpness.** The bound $(k-1)n/2$ cannot be lowered:

1. If $k \mid n$, let $G = \frac{n}{k}K_k$ (disjoint copies of the complete graph on $k$ vertices). Then
 $$e(G) = \frac{n}{k}\binom{k}{2} = \frac{(k-1)n}{2},$$
 and every component has $k < k+1$ vertices, so $G$ contains no $k$-edge tree. Hence $\mathrm{ex}(n,T) \ge (k-1)n/2$ for every such $T$.
2. For the star $T=K_{1,k}$, any $(k-1)$-regular graph on $n$ vertices ($(k-1)n$ even) has $\Delta = k-1 < k$ and $e = (k-1)n/2$; here the conjecture is trivially true, since $e(G) > (k-1)n/2 \Rightarrow \Delta(G)\ge k$ by pigeonhole on $\sum_v \deg(v) = 2e(G)$.

**Reference theorem it generalizes (Erdős–Gallai, 1959).** If $e(G) > \frac{(k-1)n}{2}$ then $G$ contains a path with $k$ edges. This is exactly the case $T = P_{k+1}$, and it is the only infinite family settled by a short classical argument.

**Minimum-degree relaxation.** The greedy embedding lemma gives a trivial baseline: if $\delta(G)\ge k$ then $G$ contains every $k$-edge tree (embed $T$ vertex by vertex; at each step at most $k$ vertices are used, so a free neighbour exists). The conjecture asks to replace the *minimum* degree $k$ by *average* degree $>k-1$ — a much weaker, non-local hypothesis.

**Related conjectures.**
- *Loebl–Komlós–Sós*: if at least $n/2$ vertices of $G$ have degree $\ge k$, then $G \supseteq T$ for every $k$-edge tree $T$. Median-degree version; proved for large $n$ by Hladký–Komlós–Piguet–Simonovits–Stein–Szemerédi.
- *Gyárfás tree-packing* and the *Ringel–Kotzig graceful labelling* programme: Erdős–Sós is the natural "one copy" shadow of these decomposition statements, since $K_{2k+1}$ has average degree $2k$ and any $T$-decomposition forces many copies of $T$.

## 3. History & State of the Art (SOTA)

- **1959.** Erdős and Gallai prove the path case, $\mathrm{ex}(n,P_{k+1}) \le (k-1)n/2$, in *On maximal paths and circuits of graphs*.
- **1963/64.** Erdős states the conjecture, attributing it jointly to himself and Vera T. Sós, at the Smolenice symposium (*Extremal problems in graph theory*).
- **1980s–90s.** A stream of special-case results: girth conditions, $C_4$-free hosts, small trees, spiders, restricted diameters.
- **1990s.** Ajtai, Komlós, Simonovits and Szemerédi announce a proof for all trees with $k$ edges, $k$ sufficiently large, using the Szemerédi regularity lemma plus a stability/extremal-configuration analysis. The announcement is repeatedly cited (e.g. in Komlós–Simonovits's 1996 regularity survey) but the full manuscript has never appeared in a refereed journal. **This is the central fact about the problem's status: the conjecture is widely described as "solved for large $k$" on the strength of an unpublished proof.**
- **2000s–2020s.** Two parallel programmes: (i) exact results for structured tree classes and structured hosts; (ii) approximate/degree-condition variants, notably by Havet, Reed, Stein, Wood, and by Besomi, Pavez-Signé, Stein, plus Rozhoň's local method.

Status as of 2026: **open** in the literature for all $k$ (no published complete proof for large $k$; no proof at all for general $k$).

## 4. Partial Results / Verified Cases

**By tree class.**
- **Paths** $P_{k+1}$, all $k$: Erdős–Gallai (1959).
- **Stars** $K_{1,k}$, all $k$: immediate from $\sum \deg = 2e > (k-1)n$.
- **Spiders** (trees with at most one vertex of degree $\ge 3$), all sizes: Fan and Sun (2007); later extended to spiders of larger size by Fan and collaborators.
- **Trees of diameter $\le 4$**: McLennan (2005). Diameter $\le 3$ (double brooms/caterpillars of small depth) was known earlier.
- **Brooms, caterpillars of bounded structure**: various authors; the general caterpillar case remains only partially covered.
- **All trees with $k$ edges, $k$ large**: Ajtai–Komlós–Simonovits–Szemerédi (announced, unpublished).

**By host graph class.**
- **Girth $\ge 5$ hosts**: Brandt and Dobson (1996) — the conjecture holds for every $k$-edge tree.
- **$C_4$-free hosts**: Saclé and Woźniak (1997).
- **Hosts with $n \le k+4$-type small ranges** and hosts whose complement is sparse: settled by direct counting.

**Degree-condition variants (proved, weaker or incomparable hypotheses).**
- Havet, Reed, Stein and Wood (2020): every graph with $\Delta(G) \ge k$ and $\delta(G) \ge \lfloor 2k/3\rfloor$ contains every tree with $k$ edges. This is a genuine theorem approaching the conjecture from the local side.
- Besomi, Pavez-Signé and Stein (2019, and follow-ups): maximum/minimum degree conditions for embedding trees, and an approximate version of Erdős–Sós for trees of bounded maximum degree in large host graphs.
- Rozhoň (2019): a "local" approach proving Erdős–Sós-type statements for bounded-degree trees under a local density hypothesis, avoiding the regularity lemma's tower-type bounds in part of the argument.

## 5. Principal Obstacles

- **No local structure to exploit.** The hypothesis $e(G) > (k-1)n/2$ is a single scalar. A host graph can be a disjoint union of a dense blob and a huge sparse part; the density may live entirely where the tree cannot be embedded. Any proof must first *locate* a sub-structure of min-degree roughly $k$, and extracting a subgraph with $\delta \ge k/2$ (standard) loses a factor of $2$ that is exactly the gap.
- **Extremal configurations are numerous and near-tight.** Besides $\frac{n}{k}K_k$, the near-extremal family includes complete bipartite-like graphs $K_{\lfloor (k-1)/2\rfloor, n - \lfloor(k-1)/2\rfloor}$ (which blocks trees with all vertices far from leaves in one class) plus unions and blow-ups of these. Stability arguments must rule out *all* of them simultaneously, and different trees are blocked by different extremal graphs — a star is blocked by regular graphs, a path by $K_k$-unions, a balanced double-broom by the unbalanced complete bipartite graph.
- **Regularity-lemma limits.** The AKSS strategy applies the regularity lemma, which requires $n$ enormous relative to $k$ and gives no bound for small or moderate $k$. It also cannot see the sparse regime $n = O(k)$, where the density hypothesis leaves almost no room and the embedding becomes near-spanning.
- **Trees of unbounded degree.** Absorption and randomized-embedding techniques that work for bounded-$\Delta$ trees break when $T$ has vertices of degree $\Theta(k)$: such a vertex must map to a high-degree host vertex, and there may be only a handful of these, forcing a global matching argument between the high-degree parts of $T$ and $G$.
- **No induction that preserves the density.** Deleting a leaf of $T$ reduces $k$ by one but the hypothesis $e(G) > (k-1)n/2$ does not improve correspondingly; deleting a low-degree vertex of $G$ can drop $e(G)$ below the threshold for the remaining vertex count.

## 6. The Gap

The proven territory is: (a) all $k$ but only structured trees (paths, stars, spiders, diameter $\le 4$) or structured hosts (girth $\ge 5$, $C_4$-free); (b) all trees but only under a *local* degree hypothesis ($\delta \ge \lfloor 2k/3\rfloor$ with $\Delta \ge k$, or $\delta \ge k$ trivially); (c) all trees for $k$ large, but only via an unpublished manuscript.

The precise barrier has two components:

1. **Average-to-minimum degree conversion.** Every published general technique needs a vertex-local guarantee of order $k$. From $\bar d(G) > k-1$ one can only extract a subgraph with $\delta \ge k/2$. Closing the interval $[\,k/2,\ k\,)$ — for instance, pushing Havet–Reed–Stein–Wood from $\lfloor 2k/3\rfloor$ down to $\lceil k/2\rceil$ and then removing the $\Delta \ge k$ hypothesis — would essentially settle the conjecture.
2. **Uniformity in $k$.** Even granting AKSS, the statement is open for every explicit $k$ beyond the settled classes; there is no known $k_0$ for which "all $k \ge k_0$" is verifiable, and no computational verification programme for moderate $k$ because the host graph size $n$ is unbounded.

## 7. Current Research (as of June 2026)

- **Stein's group (Universidad de Chile / CMM)** continues the systematic degree-condition programme with Besomi and Pavez-Signé: approximate Erdős–Sós for bounded-degree trees, and sharpened max/min-degree pairs. Stein's survey *Tree containment and degree conditions* (2020) is the current map of the area.
- **Regularity-free and local methods.** Rozhoň's local framework, and subsequent sparse-regularity/absorption hybrids, aim to remove the tower-type dependence on $k$ so that explicit bounds become extractable. *(frontier — verify)* Several recent arXiv preprints claim Erdős–Sós for further tree families (large-diameter brooms, trees with a bounded number of branch vertices); these should be checked individually before citation.
- **Status of the AKSS manuscript.** Portions of the Ajtai–Komlós–Simonovits–Szemerédi argument have circulated and been discussed at conferences; as of mid-2026 no complete refereed version is available. *(frontier — verify)*
- **Random and pseudorandom hosts.** Embedding all $k$-edge trees into $G(n,p)$ and into $(n,d,\lambda)$-graphs at the Erdős–Sós density threshold is an active offshoot, with resilience-type statements the target.
- **Connections to decomposition.** Work on the Gyárfás tree-packing conjecture and on approximate graceful labellings (Montgomery, Pokrovskiy, Sudakov's resolution of Ringel's conjecture for large $n$) has supplied absorption tools that some groups are retargeting at Erdős–Sós.

## 8. Future Work

- **Publish or replace AKSS.** A refereed, self-contained proof for large $k$ — ideally with an explicit $k_0$ — is the single highest-value output.
- **Drive the minimum degree to $k/2$.** Prove: $\Delta(G)\ge k$ and $\delta(G)\ge \lceil k/2 \rceil$ imply $G \supseteq T$ for all $k$-edge $T$. Combined with a density-to-degree extraction, this would close the gap.
- **Full stability classification.** Characterize all $n$-vertex graphs with $e(G) = \lfloor (k-1)n/2 \rfloor$ containing no $k$-edge tree $T$; a clean list would enable a stability-plus-extremal induction.
- **Bounded-degree case exactly.** Prove Erdős–Sós for all trees with $\Delta(T) \le C$ and all $k$, with no largeness assumption on $n$.
- **Caterpillars in full generality**, then trees of diameter $5$ — the natural next rung after McLennan.
- **Computer-assisted verification** for small $k$ (say $k \le 8$) via flag-algebra or SDP relaxations of the density bound, which would at least rule out small counterexamples.

## 9. Key References

- **[Foundational]** P. Erdős and T. Gallai. *On maximal paths and circuits of graphs.* Acta Mathematica Academiae Scientiarum Hungaricae 10 (1959), 337–356.
- **[Foundational]** P. Erdős. *Extremal problems in graph theory.* In: Theory of Graphs and its Applications (Proc. Sympos. Smolenice, 1963), Publ. House Czechoslovak Acad. Sci., Prague, 1964, 29–36.
- **[Foundational]** J. Komlós and M. Simonovits. *Szemerédi's regularity lemma and its applications in graph theory.* In: Combinatorics, Paul Erdős is Eighty, Vol. 2, Bolyai Soc. Math. Stud. 2, Budapest, 1996, 295–352. (Contains the announcement of the Ajtai–Komlós–Simonovits–Szemerédi result for large $k$.)
- **[Partial]** S. Brandt and E. Dobson. *The Erdős–Sós conjecture for graphs of girth 5.* Discrete Mathematics 150 (1996), 411–414.
- **[Partial]** J.-F. Saclé and M. Woźniak. *The Erdős–Sós conjecture for graphs without $C_4$.* Journal of Combinatorial Theory, Series B 70 (1997), 367–372.
- **[Partial]** A. McLennan. *The Erdős–Sós conjecture for trees of diameter four.* Journal of Graph Theory 49 (2005), 291–301.
- **[Partial]** G. Fan and L. Sun. *The Erdős–Sós conjecture for spiders.* Discrete Mathematics 307 (2007), 3055–3062.
- **[SOTA / Recent]** F. Havet, B. Reed, M. Stein and D. R. Wood. *A variant of the Erdős–Sós conjecture.* Journal of Graph Theory 94 (2020), 131–158.
- **[SOTA / Recent]** G. Besomi, M. Pavez-Signé and M. Stein. *Degree conditions for embedding trees.* SIAM Journal on Discrete Mathematics 33 (2019), 1521–1555.
- **[SOTA / Recent]** V. Rozhoň. *A local approach to the Erdős–Sós conjecture.* SIAM Journal on Discrete Mathematics 33 (2019), 643–664.
- **[Related]** J. Hladký, J. Komlós, D. Piguet, M. Simonovits, M. Stein and E. Szemerédi. *The approximate Loebl–Komlós–Sós conjecture, I–IV.* SIAM Journal on Discrete Mathematics 31 (2017).
- **[Survey]** M. Stein. *Tree containment and degree conditions.* In: Discrete Mathematics and Applications, Springer Optimization and Its Applications 165, Springer, 2020, 459–486.

## 10. Worked Example / Concrete Special Case

**The case $k = 3$, proved completely.**

There are exactly two trees with $3$ edges: the path $P_4$ and the star $K_{1,3}$. The conjecture claims: if $e(G) > \frac{(3-1)n}{2} = n$, then $G$ contains both.

*Star $K_{1,3}$.* From $\sum_{v} \deg_G(v) = 2e(G) > 2n$, the average degree exceeds $2$, so some vertex $v$ has $\deg_G(v) \ge 3$. Any three neighbours of $v$ give a copy of $K_{1,3}$. ∎

*Path $P_4$.* Suppose $G$ has no path with $3$ edges. Take a longest path $v_0 v_1 \dots v_\ell$ in a component $C$; if $\ell \ge 3$ we are done, so $\ell \le 2$, meaning every component of $G$ has diameter $\le 2$ and no $P_4$. A connected $P_4$-free graph is a triangle or a star: if $C$ contains a vertex $u$ with two neighbours $a,b$ and $a$ has a further neighbour $c \notin \{u,b\}$, then $b\,u\,a\,c$ is a $P_4$. So each component $C$ with $n_C$ vertices satisfies $e(C) \le n_C$ (star: $n_C - 1$; triangle: $3 = n_C$). Summing, $e(G) \le n$, contradicting $e(G) > n$. ∎

*Sharpness.* Let $n = 3m$ and $G = m K_3$. Then
$$e(G) = 3m = n = \frac{(k-1)n}{2}\Big|_{k=3},$$
and every component has $3$ vertices, so $G$ contains neither $P_4$ nor $K_{1,3}$ (both need $4$ vertices in one component). The threshold $n$ is therefore exact, and adding a single edge — say joining two triangles — creates a vertex of degree $3$ (a $K_{1,3}$) and a $P_4$ across the new edge.

*Where the difficulty starts.* At $k=3$ both arguments are local and finite. At $k = 6$ with $T$ a double broom (two adjacent centres, each with three pendant leaves), the star argument gives only $\Delta(G)\ge 6$, and the path argument gives no control on where the two centres sit. The host $K_{2,n-2}$ has $2(n-2) > \frac{5n}{2}$ edges only for $n < -\,$ (never), which is why the bipartite extremal example matters at other parameters: $K_{\lfloor (k-1)/2\rfloor,\,n-\lfloor(k-1)/2\rfloor}$ has $\approx \frac{(k-1)n}{2}$ edges and contains no tree needing $\ge \lceil (k+1)/2\rceil$ vertices on both sides. Any general proof must simultaneously defeat this bipartite obstruction and the $\frac{n}{k}K_k$ obstruction — the coexistence of two structurally unrelated extremal families is the technical heart of the problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*