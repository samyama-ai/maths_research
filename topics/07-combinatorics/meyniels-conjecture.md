---
id: 07-combinatorics/meyniels-conjecture
title: "Meyniel's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Meyniel's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/meyniels-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Meyniel's Conjecture is the central unsolved problem in the study of the "Cops and Robbers" game on graphs. The game is a vertex-pursuit game played on a finite, connected, undirected graph where a set of cops attempts to capture a single robber. 

The **cop number**, denoted as $c(G)$, is defined as the minimum number of cops required to guarantee the capture of the robber on a graph $G$, regardless of how optimally the robber plays. 

**Meyniel's Conjecture (1985):** There exists an absolute constant $C > 0$ such that for every connected graph $G$ on $n$ vertices, the cop number satisfies:
$$c(G) \le C \sqrt{n}$$

Alternatively stated, the maximum possible cop number for a connected graph on $n$ vertices is $O(\sqrt{n})$. A proof of this conjecture requires demonstrating a universal strategy or structural decomposition that allows $O(\sqrt{n})$ cops to trap a robber on any arbitrary $n$-vertex connected topology, while a disproof requires constructing a family of graphs where the cop number grows strictly faster than $O(\sqrt{n})$.

## 2. Mathematical Foundations

Let $G = (V,E)$ be a finite, simple, undirected, and connected graph. The Cops and Robbers game is a perfect-information, zero-sum, sequential game played between a team of $k$ cops, denoted $C_1, C_2, \dots, C_k$, and a single robber $R$.

**Rules of the Game:**
1. **Initialization:** The $k$ cops choose their starting vertices $c_1^{(0)}, \dots, c_k^{(0)} \in V$. Multiple cops may occupy the same vertex. The robber then, with full knowledge of the cops' positions, chooses a starting vertex $r^{(0)} \in V$.
2. **Transitions:** Play alternates in discrete time steps $t \ge 1$. First, the cops move to vertices $c_i^{(t)} \in N[c_i^{(t-1)}]$ for each $i \in \{1, \dots, k\}$, where $N[v] = N(v) \cup \{v\}$ denotes the closed neighborhood of a vertex $v$. This means a cop can move to an adjacent vertex or remain stationary. After the cops move, the robber moves to a vertex $r^{(t)} \in N[r^{(t-1)}]$.
3. **Termination:** The cops win if, at any step $t \ge 0$, at least one cop occupies the same vertex as the robber ($c_i^{(t)} = r^{(t)}$ for some $i$). The robber wins if they can infinitely evade capture.

**The Cop Number:**
Because the game is played on a finite graph with perfect information, by Zermelo's Theorem, either the cops or the robber must have a winning strategy. The cop number $c(G)$ is the minimum integer $k$ such that $k$ cops have a winning strategy. We denote the maximum cop number over all connected graphs on $n$ vertices as:
$$c(n) = \max \{ c(G) \mid |V(G)| = n, \, G \text{ is connected} \}$$
Meyniel's Conjecture precisely asserts that $c(n) = O(\sqrt{n})$.

## 3. History & State of the Art (SOTA)

The game of Cops and Robbers was independently introduced by Quilliot (1978) and Nowakowski and Winkler (1983). The problem of finding a general upper bound on the cop number quickly became an area of interest. In 1985, Henri Meyniel mentioned his $\sqrt{n}$ conjecture to Peter Frankl, who subsequently published it in his seminal 1987 paper, *Cops and robbers in graphs with large girth and Cayley graphs*. 

In the same 1987 paper, Frankl provided the first non-trivial upper bound for the cop number of general graphs, showing $c(n) = O(n \frac{\log \log n}{\log n})$. This logarithmic saving remained the state of the art for over two decades until Chiniforooshan (2008) improved it to $O(n / \log n)$.

A major breakthrough occurred around 2011–2012 when three independent groups of researchers—Lu and Peng; Scott and Sudakov; and Frieze, Krivelevich, and Loh—published papers that broke the logarithmic barrier. Despite using slightly different probabilistic and deterministic variations of structural decomposition, all three groups established bounds of the form:
$$c(n) \le n 2^{- (1 + o(1)) \sqrt{\log_2 n}}$$
Often referred to informally as the $n^{1-o(1)}$ bound, this remains the absolute State of the Art (SOTA) for general upper bounds on the cop number.

## 4. Partial Results / Verified Cases

While the general conjecture remains wide open, it has been verified for several important structural classes and parameter regimes:

- **Planar and Bounded Genus Graphs:** Aigner and Fromme (1984) famously proved that planar graphs have $c(G) \le 3$. This was generalized by Schröder (2001), who showed that for graphs of genus $g$, $c(G) \le \frac{3}{2}g + 3$. Bowler et al. later improved the linear coefficient. These bounds are $O(1)$ with respect to $n$, satisfying the conjecture trivially.
- **Excluded Minors:** Andreae (1986) proved that for any fixed graph $H$, the class of graphs avoiding $H$ as a minor has a cop number bounded by a constant $c_H$ depending only on $H$. 
- **Random Graphs:** The conjecture has been shown to hold for Erdős–Rényi random graphs. Prałat and Wormald (2012) proved that for $G(n,p)$ across all regimes of $p = p(n)$, the cop number is asymptotically almost surely bounded by $O(\sqrt{n \log n})$. Bollobás, Kun, and Leader (2013) refined this, proving that for dense random graphs, the cop number is concentrated and strictly confirms Meyniel's conjecture.
- **Graphs of High Girth:** If a graph $G$ has girth $g \ge 5$, it is known that $c(G) \ge \delta(G)$, where $\delta$ is the minimum degree. This structural relationship was pivotal in generating the $\Omega(\sqrt{n})$ lower bounds that show Meyniel's conjecture is tight. 
- **Chordal and Outerplanar Graphs:** It is proven that chordal graphs require at most $O(1)$ cops, while strongly chordal and outerplanar graphs have $c(G) \le 2$.

## 5. Principal Obstacles

The primary barrier to resolving Meyniel's conjecture is the inherent limitation of current mathematically formalized "pursuit strategies". All state-of-the-art upper bounds rely on a localized geometric strategy where a subset of cops "guards" a shortest path or a dominating set. 

When a cop guards a shortest path $P$, the robber is forbidden from stepping onto $P$ without being immediately intercepted. By guarding multiple paths iteratively, the cops partition and shrink the robber's accessible territory. The efficiency of this strategy depends entirely on the **Moore bound**:
- If the graph has **short cycles (low girth)**, the cops can dominate large neighborhoods efficiently.
- If the graph has **no short cycles (high girth)**, the neighborhoods grow exponentially, meaning the shortest paths are extremely long, allowing cops to eliminate large swaths of the graph by guarding a single path.

The worst-case scenario occurs precisely in the middle: when the graph has a mixture of dense, localized clusters that prevent paths from being long, but lacks the global connectivity to allow a small number of cops to dominate the entire structure. Optimizing the trade-off between these two extremes is what yields the $n 2^{-c\sqrt{\log n}}$ bound. 

Breaking past this exponential barrier requires a global topological or algebraic invariant capable of describing the whole graph's connectivity profile simultaneously. Standard tools—like spectral graph theory, traditional Fourier analysis on Boolean cubes, or homology—have failed to map usefully onto the discrete, adversarial dynamics of the Cops and Robbers game.

## 6. The Gap

The mathematical gap to fully resolving the problem is immense. We currently stand at an upper bound of $n e^{-O(\sqrt{\log n})}$. The conjecture claims an upper bound of $O(n^{1/2})$. 

Currently, it is not even known whether there exists some constant $\epsilon > 0$ such that $c(n) = O(n^{1-\epsilon})$. Bridging the gap from a sub-exponential improvement over $n$ to a polynomial improvement $n^{1-\epsilon}$ is the immediate, and currently insurmountable, hurdle. 

## 7. Current Research (as of June 2026)

Active research on Meyniel's Conjecture is highly diversified across probabilistic combinatorics and theoretical computer science. 
- **The Diameter 2 Bottleneck:** A major current sub-goal is proving the conjecture for graphs of diameter 2. It is widely suspected among researchers that if Meyniel's conjecture is false, a counterexample is most likely to be found among diameter-2 graphs with highly asymmetric expansion properties.
- **Fractional Cop Number:** Researchers have introduced a linear-programming relaxation of the game, known as the fractional cop number, where cops and robbers can split their mass across vertices. This has yielded new insights, though translating fractional bounds back to integral bounds remains lossy.
- **Computational Verification:** SAT-solvers and deep reinforcement learning *(frontier — verify)* are actively being used by groups in structural graph theory to compute exact cop numbers of graphs up to $n \approx 100$, searching for anomalous families that exhibit rapid growth in $c(G)$. 

## 8. Future Work

Leading combinatorists suggest the following open pathways:
1. **Prove the $O(n^{1-\epsilon})$ Bound:** Find any structural decomposition that guarantees saving a polynomial factor of cops over the trivial $n$ bound.
2. **Resolve the Diameter 2 Case:** Establish whether $c(G) = O(\sqrt{n})$ for all graphs with diameter 2. If this is false, Meyniel's conjecture falls. If true, the structural techniques developed would likely revolutionize the general case.
3. **Algebraic Graph Theory:** Attempt to bound the cop number directly using eigenvalues of the adjacency or Laplacian matrices, aiming to show that graphs lacking strong spectral expansion are easier for cops to control, while expanders can be handled by random walks.

## 9. Key References

- **[Foundational]** Frankl, P. *Cops and robbers in graphs with large girth and Cayley graphs.* Discrete Applied Mathematics, 1987.
- **[Foundational]** Aigner, M., and Fromme, M. *A game of cops and robbers.* Discrete Applied Mathematics, 1984.
- **[SOTA / Recent]** Lu, L., and Peng, X. *On Meyniel's conjecture of the cop number.* Journal of Graph Theory, 2012.
- **[SOTA / Recent]** Scott, A., and Sudakov, B. *A bound for the cops and robbers problem.* SIAM Journal on Discrete Mathematics, 2011.
- **[SOTA / Recent]** Frieze, A., Krivelevich, M., and Loh, P. *Variations on cops and robbers.* Journal of Combinatorial Theory, Series B, 2012.
- **[Survey]** Baird, W., and Bonato, A. *Meyniel's conjecture on the cop number: a survey.* Journal of Combinatorics, 2012.
- **[Survey]** Bonato, A., and Nowakowski, R. J. *The Game of Cops and Robbers on Graphs.* American Mathematical Society (Student Mathematical Library), 2011.

## 10. Worked Example / Concrete Special Case

To understand why Meyniel's conjecture proposes an $O(\sqrt{n})$ bound, it is instructive to examine the deterministic lower bound. We will construct a family of graphs where $c(G) = \Omega(\sqrt{n})$ using the incidence graphs of finite projective planes.

**The Geometric Construct:**
Let $q$ be a prime power, and let $PG(2, q)$ be the projective plane of order $q$. This plane consists of $q^2 + q + 1$ points and $q^2 + q + 1$ lines. 
We construct the incidence graph $G = (V,E)$ where the vertex set $V$ is the union of the points and the lines. An edge exists between a point-vertex and a line-vertex if and only if the point lies on the line. 
- The total number of vertices is $n = 2(q^2 + q + 1)$.
- Because every point lies on $q+1$ lines and every line contains $q+1$ points, $G$ is a $(q+1)$-regular bipartite graph.
- Two distinct points define exactly one line, meaning there are no cycles of length 4. Thus, the girth of $G$ is 6.

**Calculating the Cop Number:**
A foundational theorem by Aigner and Fromme (1984) states that for any graph $G$ with girth $g \ge 5$, the cop number is strictly bounded below by the minimum degree of the graph: $c(G) \ge \delta(G)$. 

To see why, suppose we play with $k = \delta - 1$ cops. The cops occupy a set of vertices $C$. The robber $R$ chooses a vertex $r$ with at least $\delta$ neighbors $v_1, \dots, v_\delta$. When the cops move to a new set of vertices $C'$, the robber must move to a neighbor $v_i$. For the cops to capture the robber on the next turn, every neighbor $v_i$ must be adjacent to (or occupied by) some cop in $C'$. 
However, because the graph has no 3-cycles or 4-cycles (as girth $\ge 5$), no single cop in $C'$ can be adjacent to more than one neighbor of $r$. Therefore, $k$ cops can threaten at most $k$ neighbors of $r$. Since $k < \delta$, there is always at least one "safe" neighbor for the robber to move to, allowing them to evade capture indefinitely.

Applying this to our incidence graph $G$:
$$c(G) \ge \delta(G) = q + 1$$
We can express this bound in terms of $n$. Since $n = 2(q^2 + q + 1)$, we have $q^2 < n/2$, which implies $q+1 > \sqrt{n/2}$. 
Therefore:
$$c(G) \ge \sqrt{\frac{n}{2}}$$
This specific geometric configuration strictly proves the existence of a family of graphs where the cop number scales as $\Omega(\sqrt{n})$, establishing the theoretical floor that mathematically justifies Meyniel's upper-bound Conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*