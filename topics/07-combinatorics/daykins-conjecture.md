---
id: 07-combinatorics/daykins-conjecture
title: "Daykin's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Daykin's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/daykins-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Daykin's Conjecture, originally posed in 1976 for simple graphs, asserts that any edge-coloring of a complete graph which is sufficiently "locally bounded" must contain a properly colored Hamilton cycle. An edge-coloring is locally bounded if no single color appears too frequently at any given vertex. While the original graph-theoretic statement has been fully resolved, the conjecture has fundamentally evolved into the **Hypergraph Daykin's Conjecture**, which remains a major open problem in extremal combinatorics.

The modern, open formulation of the conjecture states:
For every integer $k \ge 3$, there exists a positive constant $\mu_k > 0$ such that, for sufficiently large $n$, every edge-coloring of the complete $k$-uniform hypergraph $K_n^{(k)}$ with maximum monochromatic codegree at most $\mu_k n$ contains a properly colored tight Hamilton cycle.

A complete proof of this conjecture requires either demonstrating the existence of such a constant $\mu_k$ via probabilistic or absorbing methods, or providing a family of counterexamples showing that bounded monochromatic codegrees are insufficient to force a properly colored tight cycle in $k$-uniform hypergraphs. 

## 2. Mathematical Foundations

Let $K_n^{(k)}$ denote the complete $k$-uniform hypergraph on $n$ vertices, where the edge set $E(K_n^{(k)})$ consists of all $k$-element subsets of the vertex set $V$. 

An **edge-coloring** is a function $c: E(K_n^{(k)}) \to \mathbb{N}$. 
To generalize the concept of "local boundedness" from graphs to hypergraphs, we define the monochromatic $\ell$-degree. For any subset of vertices $S \subset V$ with $|S| = \ell$ and any color $j \in \mathbb{N}$, the $\ell$-degree of $S$ in color $j$ is the number of edges containing $S$ that are colored $j$:
$$ d_S^c(j) = \left| \{ e \in E(K_n^{(k)}) : S \subset e \text{ and } c(e) = j \} \right| $$
The maximum monochromatic $\ell$-degree of the coloring $c$ is then defined as:
$$ \Delta_\ell(c) = \max_{|S|=\ell} \max_{j \in \mathbb{N}} d_S^c(j) $$

A **cycle** in a $k$-uniform hypergraph is defined by a cyclic ordering of the vertices, $v_0, v_1, \dots, v_{n-1}$. The structure of the cycle depends on how consecutive edges overlap. 
- In a **loose cycle**, adjacent edges intersect at exactly one vertex.
- In a **tight cycle**, every set of $k$ consecutive vertices forms an edge. Formally, the edge set of a tight cycle is $\{e_i\}_{i=0}^{n-1}$ where $e_i = \{v_i, v_{i+1}, \dots, v_{i+k-1}\}$ (with indices taken modulo $n$). 

A hypergraph cycle is **properly colored** if any two adjacent edges in the cycle receive distinct colors. For a tight cycle, this means $c(e_i) \neq c(e_{i+1})$ for all $i$. 

The open conjecture formally posits:
$$ \exists \mu_k > 0 \text{ such that for } n \gg 1, \text{ if } \Delta_{k-1}(c) \le \mu_k n, \text{ then } K_n^{(k)} \text{ contains a properly colored tight Hamilton cycle.} $$

## 3. History & State of the Art (SOTA)

David E. Daykin presented the original conjecture for $k=2$ (graphs) at the British Combinatorial Conference in 1976. He conjectured that there exists a $\mu > 0$ such that any edge-coloring of $K_n$ with maximum monochromatic vertex degree $\Delta_1(c) \le \mu n$ contains a properly colored Hamilton cycle.

The problem was resolved almost immediately for graphs. In 1976, B. Bollobás and P. Erdős, and independently C.C. Chen and D.E. Daykin, proved the conjecture, establishing that $\mu = 1/69$ and $\mu = 1/17$ suffice, respectively. In 1979, Shearer improved this bound to $\mu = 1/7$. The asymptotic threshold for the graph case was definitively established in 2016 by Albert Lo, who proved that the conjecture holds for any $\mu < 1/2$ as $n \to \infty$, which is optimal.

With the graph case settled, the SOTA shifted to hypergraphs. In 2017, Dudek, Frieze, and Ruciński investigated properly colored and rainbow cycles in hypergraphs. They successfully established bounds for *loose* properly colored Hamilton cycles. However, the *tight* cycle case was identified as fundamentally more difficult due to the dense overlapping edge structure, elevating the Hypergraph Daykin's Conjecture to a premier open problem in extremal combinatorics.

## 4. Partial Results / Verified Cases

- **Graphs ($k=2$):** Fully resolved. The optimal bound is $\mu < 1/2$. The result has also been extended to Dirac-type host graphs: if a graph $G$ has minimum degree $\delta(G) \ge n/2$, any locally $\mu n$-bounded coloring of $G$ contains a properly colored Hamilton cycle.
- **Loose Hypergraph Cycles:** The conjecture holds for $1$-overlapping (loose) Hamilton cycles in $k$-uniform hypergraphs. If $\Delta_1(c) \le \mu n^{k-1}$ for a sufficiently small $\mu$, a properly colored loose Hamilton cycle is guaranteed to exist.
- **Rainbow Hypergraph Cycles:** A cycle is "rainbow" if *all* edges have distinct colors. While Daykin's local boundedness condition is insufficient for rainbow cycles, verified cases exist if the coloring is globally bounded (each color appears at most $O(n^{k-1})$ times total) or if the host hypergraph is randomly generated with high edge probabilities. 

## 5. Principal Obstacles

The primary barrier to resolving the tight hypergraph conjecture is the failure of the **Absorbing Method**, a standard probabilistic technique used to prove the existence of spanning structures (like Hamilton cycles) in dense graphs.

In the graph case ($k=2$), researchers construct an "absorbing path" $P$ with the property that for any small set of leftover vertices $X$, there exists an alternative properly colored path $P^*$ spanning $V(P) \cup X$ with the same endpoints. Because edges in a graph path intersect at exactly one vertex, local modifications can be made independently. If a color conflict arises when absorbing a vertex $x$, the local boundedness ($\Delta_1(c) \le \mu n$) guarantees there is ample geometric flexibility to choose an alternative edge without cascading color conflicts.

For tight hypergraphs ($k \ge 3$), adjacent edges share $k-1$ vertices. Suppose we have a properly colored tight path and we wish to insert a leftover vertex $x$ into the sequence. Inserting $x$ requires replacing one existing edge with several new, heavily overlapping edges. Because the overlap is $k-1$, the color constraints propagate linearly. The color of the newly formed edge $e_{i}$ restricts $e_{i+1}$, which in turn restricts $e_{i+2}$, creating a rigid "domino effect". A generic absorbing gadget for tight cycles requires modifying the path over a long, highly correlated segment. Probabilistically guaranteeing the existence of such a rigid, multi-colored absorber in *any* $\mu n$-bounded coloring has proven mathematically intractable with current techniques.

## 6. The Gap

The exact boundary of what is proven lies between $1$-overlapping cycles (loose) and $(k-1)$-overlapping cycles (tight). When the overlap is small, edges behave pseudo-independently, and standard applications of the Rödl Nibble and local absorbers succeed. The gap is the mathematical step required to build properly colored absorbers that can tolerate $(k-1)$-overlapping color dependencies. Closing this gap likely requires an entirely new framework for "colored hypergraph regularity" combined with a novel iterative absorption lemma designed specifically for highly overlapping rigid structures.

## 7. Current Research (as of June 2026)

Active research is concentrated within probabilistic combinatorics and extremal hypergraph theory groups, notably those originating from the Birmingham school (Kühn, Osthus, and their descendants) and the ETH Zurich group. 

Current strategies attempt to bypass the rigid absorber problem by using **Iterative Absorption**, a technique that repeatedly absorbs leftover vertices into smaller and smaller reservoirs until the remaining vertices can be covered by a deterministic brute-force structure. 

*Frontier — verify:* Recent preprint claims suggest that by utilizing a colored version of the Hypergraph Regularity Lemma, researchers can construct properly colored tight absorbers under highly restrictive global color conditions, potentially yielding a lower bound of $\mu_k = \Omega(1/n)$ for the tight cycle case. However, the existence of a constant $\mu_k > 0$ independent of $n$ remains unverified.

## 8. Future Work

Leading mathematicians have outlined several open pathways to attack the conjecture:
- **Solve the $k=3$ Baseline:** Establish the conjecture for $3$-uniform hypergraphs. Proving that $\Delta_2(c) \le \mu_3 n$ guarantees a properly colored tight Hamilton cycle in $K_n^{(3)}$ would break the methodological bottleneck.
- **Determine the Asymptotic Threshold:** If the conjecture is true, determine the optimal constant $\mu_k$. Is it related to $1/k$ or $1/k!$, analogous to Lo's $1/2$ for graphs?
- **Resilience and Robustness:** Investigate resilience versions of the problem. If an adversary deletes a small positive fraction of edges from $K_n^{(k)}$, under what monochromatic codegree bounds does the remaining structure still host a properly colored tight Hamilton cycle?

## 9. Key References

- **[Foundational]** B. Bollobás, P. Erdős. *Alternating Hamiltonian cycles.* Israel Journal of Mathematics, 1976.
- **[Foundational]** C.C. Chen, D.E. Daykin. *Graphs with Hamiltonian cycles having adjacent lines different colors.* Journal of Combinatorial Theory, Series B, 1976.
- **[SOTA / Recent]** A. Lo. *Properly colored Hamiltonian cycles in edge-colored complete graphs.* Combinatorica, 2016.
- **[SOTA / Recent]** A. Dudek, A. Frieze, A. Ruciński. *Rainbow and properly colored copies of graphs and hypergraphs.* Journal of Graph Theory, 2017.
- **[Survey]** J. Bang-Jensen, G. Gutin. *Alternating cycles and paths in edge-colored multigraphs: A survey.* Discrete Mathematics, 1997.

## 10. Worked Example / Concrete Special Case

To ground the abstract difficulty of tight hypergraphs, consider the mechanical difference of inserting a vertex into a cycle for $k=2$ (graphs) versus $k=3$ (hypergraphs).

**The Solved Graph Case ($k=2$):**
Suppose we have a properly colored Hamilton cycle in $K_n$. A segment of the cycle is $v_1 - v_2 - v_3$, with edges $e_1 = \{v_1, v_2\}$ and $e_2 = \{v_2, v_3\}$. Proper coloring dictates $c(e_1) \neq c(e_2)$.
We wish to insert a new vertex $x$ between $v_1$ and $v_2$. The new segment becomes $v_1 - x - v_2 - v_3$. 
The old edge $e_1$ is replaced by two new edges: $f_1 = \{v_1, x\}$ and $f_2 = \{x, v_2\}$. 
To maintain a proper coloring, we need:
1. $c(\text{previous edge}) \neq c(f_1)$
2. $c(f_1) \neq c(f_2)$
3. $c(f_2) \neq c(e_2)$

Because $f_1$ and $f_2$ share only vertex $x$, their color dependencies are isolated. Bounded vertex degrees ($\Delta_1(c) \le \mu n$) ensure we can easily find a vertex $x$ where the colors of $f_1$ and $f_2$ avoid the finite list of forbidden colors at the boundary.

**The Open Hypergraph Case ($k=3$):**
Consider a properly colored tight cycle in $K_n^{(3)}$. A segment is defined by vertices $v_1, v_2, v_3, v_4$, generating two adjacent edges: $E_1 = \{v_1, v_2, v_3\}$ and $E_2 = \{v_2, v_3, v_4\}$. Proper coloring dictates $c(E_1) \neq c(E_2)$.
We wish to insert vertex $x$ between $v_2$ and $v_3$. The new vertex sequence is $v_1, v_2, x, v_3, v_4$.
The old edges $E_1, E_2$ (which shared the pair $\{v_2, v_3\}$) are destroyed. We must form three entirely new overlapping edges:
- $F_1 = \{v_1, v_2, x\}$
- $F_2 = \{v_2, x, v_3\}$
- $F_3 = \{x, v_3, v_4\}$

To maintain a proper coloring, we now require:
1. $c(\{v_0, v_1, v_2\}) \neq c(F_1)$
2. $c(F_1) \neq c(F_2)$
3. $c(F_2) \neq c(F_3)$
4. $c(F_3) \neq c(\{v_3, v_4, v_5\})$

Notice the extreme rigidity: $F_1$ and $F_2$ share the pair $\{v_2, x\}$, and $F_2$ and $F_3$ share $\{x, v_3\}$. The bounded codegree condition ($\Delta_2(c) \le \mu n$) means that for the specific pair $\{v_2, x\}$, there are at most $\mu n$ edges of any given color. However, picking $x$ simultaneously fixes $F_1, F_2,$ and $F_3$. We cannot independently adjust the color of $F_2$ without also changing the geometry of $F_1$ and $F_3$. This geometric entanglement means the local bounds $\mu n$ are no longer robust enough to guarantee an available color pathway, representing the precise mathematical gap stalling Daykin's Conjecture for hypergraphs.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*