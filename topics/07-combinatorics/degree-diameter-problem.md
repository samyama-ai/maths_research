---
id: 07-combinatorics/degree-diameter-problem
title: "Degree-Diameter Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Degree-Diameter Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/degree-diameter-problem` · **Status:** open

## 1. Problem Statement / Conjecture

The **Degree-Diameter Problem** is one of the most prominent optimization questions in extremal graph theory. It asks for the maximum possible number of vertices $N(d,k)$ in a simple graph $G$ having a given maximum degree $d \ge 2$ and a given diameter $k \ge 1$.

Alternatively, the problem is formulated constructively: given constraints on the degree $d$ and diameter $k$, find graphs (or infinite families of graphs) that achieve or closely approach the theoretical upper bound on the number of vertices, known as the **Moore bound**.

The fundamental question comprises three layers:
1. **The Exact Problem**: Determine the precise values of $N(d,k)$ for specific small parameters (e.g., finding the maximum number of vertices for $d=6, k=3$).
2. **The Asymptotic Problem**: Understand the growth rate of $N(d,k)$ as either the degree $d \to \infty$ for fixed diameter $k$, or as the diameter $k \to \infty$ for fixed degree $d$.
3. **The Moore Graph Conjecture**: Determine the existence of the elusive Moore graph of degree 57 and diameter 2, the only parameter set for which the existence of an optimal Moore graph remains mathematically undecided.

A complete resolution of the degree-diameter problem would require either discovering a universal algebraic method for constructing maximally dense graphs with small diameter, or proving structural theorems that definitively lower the asymptotic upper bounds for all $(d,k)$.

## 2. Mathematical Foundations

The framework of the problem rests on algebraic graph theory and extremal combinatorics. Let $G = (V,E)$ be a simple, undirected, and connected graph.
- The **distance** $d(u,v)$ between two vertices $u, v \in V$ is defined as the number of edges in the shortest path connecting them.
- The **diameter** $k$ of $G$ is the maximum distance between any two vertices in the graph: $k = \max_{u,v \in V} d(u,v)$.
- The **maximum degree** $d$ is defined as $\max_{v \in V} \deg(v)$.

For any chosen root vertex $v \in V$, the number of vertices at distance $i$ from $v$ is bounded. At distance 1, there are at most $d$ vertices. For each subsequent distance $i \ge 2$, each vertex at distance $i-1$ can connect to at most $d-1$ new vertices. Summing these capacities over all distances up to the diameter $k$ yields the **Moore bound**, denoted $M_{d,k}$:

$$ M_{d,k} = 1 + d + d(d-1) + d(d-1)^2 + \dots + d(d-1)^{k-1} $$

For $d > 2$, this geometric series evaluates to:

$$ M_{d,k} = 1 + d \frac{(d-1)^k - 1}{d-2} $$

A graph of maximum degree $d$ and diameter $k$ that has exactly $M_{d,k}$ vertices is called a **Moore graph**. In a Moore graph, the graph is strictly $d$-regular, and for every pair of vertices $u, v$, there is exactly one unique shortest path of length at most $k$ connecting them, implying the graph has a girth (length of the shortest cycle) of precisely $2k+1$.

The spectral properties of Moore graphs are tightly constrained. Let $A$ be the adjacency matrix of a $d$-regular graph $G$. We can define a sequence of orthogonal polynomials $F_i(x)$ such that the distance-$i$ adjacency matrix $A_i$ equals $F_i(A)$. Specifically:
- $F_0(x) = 1$
- $F_1(x) = x$
- $F_2(x) = x^2 - d$
- $F_{i+1}(x) = x F_i(x) - (d-1)F_{i-1}(x)$ for $i \ge 2$.

For a Moore graph of diameter $k$, the sum of all distance matrices must equal the all-ones matrix $J$:

$$ \sum_{i=0}^k F_i(A) = J $$

Because $J$ has one eigenvalue of $N(d,k)$ (associated with the all-ones eigenvector) and all other eigenvalues are 0, any other eigenvalue $\lambda$ of $A$ must be a root of the polynomial $P_k(x) = \sum_{i=0}^k F_i(x) = 0$. The roots of $P_k(x)$ dictate the eigenvalues of $A$, and their multiplicities (which must be strictly positive integers) form the core Diophantine equations that dictate whether such a graph can mathematically exist.

Because Moore graphs are virtually non-existent, modern research characterizes graphs by their **defect** $\delta$, defined as $\delta = M_{d,k} - N(d,k)$.

## 3. History & State of the Art (SOTA)

The history of the degree-diameter problem traces back to a foundational 1960 paper by Alan J. Hoffman and Robert R. Singleton. By analyzing the eigenvalues of the adjacency matrix, they completely characterized Moore graphs of diameter $k=2$, proving they can only exist for degrees $d = 2, 3, 7$, and possibly $d=57$.

For larger diameters, the breakthrough occurred in 1973. R. M. Damerell, and independently Eiichi Bannai and Tatsuro Ito, used the algebraic theory of distance-regular graphs to prove a sweeping non-existence theorem: for $k \ge 3$ and $d \ge 3$, Moore graphs strictly do not exist. This effectively closed the search for optimal graphs (defect $\delta=0$) for almost all parameter spaces.

Attention subsequently shifted to the **Bipartite Moore Bound**, where graphs are constrained to contain no odd cycles. The analogous upper bound is $M^b_{d,k} = 2 \sum_{i=0}^{k-1} (d-1)^i$. Bipartite Moore graphs correspond geometrically to generalized polygons. In a monumental result derived from the Feit-Higman theorem (1964), it is known that bipartite Moore graphs only exist for $k \in \{2, 3, 4, 6\}$ (corresponding to projective planes, generalized quadrangles, and generalized hexagons).

Today, the state of the art involves populating the "Degree-Diameter Table," a catalog of the largest known explicit graph constructions for specific pairs of $(d,k)$. The best known constructions primarily utilize group theory (Cayley graphs) and finite field geometries (polarity graphs, lifts of voltage graphs).

Asymptotically, as $d \to \infty$ for fixed $k$, the SOTA is as follows:
- For $k \in \{2, 3, 5\}$, explicit constructions based on generalized polygons yield graphs of order $\Theta(d^k)$.
- For $k \notin \{2, 3, 5\}$, the best known explicit constructions achieve only order $\Theta(d^{\lfloor (k+2)/2 \rfloor})$ or slightly better, leaving a massive gap from the theoretical $O(d^k)$ bound.

## 4. Partial Results / Verified Cases

### The Moore Graphs (Defect 0)
The only definitively known Moore graphs are:
- For $d=2$: The odd cycles $C_{2k+1}$ for any diameter $k$.
- For $k=1$: The complete graphs $K_{d+1}$ for any degree $d$.
- For $k=2, d=3$: The Petersen graph ($N=10$).
- For $k=2, d=7$: The Hoffman-Singleton graph ($N=50$).

### Bipartite Moore Graphs
Verified classes of bipartite Moore graphs include:
- $k=2$: Complete bipartite graphs $K_{d,d}$.
- $k=3$: Incidence graphs of finite projective planes, existing when $d-1$ is a prime power (e.g., the Heawood graph for $d=3, N=14$).
- $k=4$: Incidence graphs of generalized quadrangles.
- $k=6$: Incidence graphs of generalized hexagons.

### Graph Constructions with Small Defect
Finding graphs with defect $\delta = 1$ is exceptionally rare. For $k=2$, it has been proven that graphs of defect 1 can only exist for $d=2$ (the 4-cycle) and no other degrees. For $k \ge 3$, extensive work by Jørgensen, Knor, and Širáň has shown that defect 1 graphs do not exist for most known parameters, and it is strongly conjectured that none exist for any $d \ge 3$.

For defect 2, successful verifications include:
- $d=3, k=3$: $N=20$ (the modified chordal ring or Elspas graph), against a Moore bound of $M_{3,3} = 22$.
- $d=4, k=2$: $N=15$, against a Moore bound of $M_{4,2} = 17$.
- $d=5, k=2$: $N=24$, against a Moore bound of $M_{5,2} = 26$.

## 5. Principal Obstacles

The primary barrier preventing the resolution of the degree-diameter problem is the inherent tension between high vertex density and the prevention of short cycles (the girth constraint). To pack the theoretical maximum number of vertices within a radius $k$, the graph must expand like an absolute perfect tree up to depth $k$. Any cross-edges that create cycles of length $\le 2k$ prematurely collapse branches of the tree, wasting degree capacity that must otherwise be used to reach undiscovered vertices.

1. **Algebraic Rigidity and Discrete Spectra**: The spectral theory of graphs implies that if a graph's vertex count approaches the Moore bound, its adjacency matrix must possess eigenvalues that tightly mirror those of the hypothetical Moore graph. Because eigenvalues of integer matrices are algebraic integers, and their multiplicities must be rational integers, you cannot "perturb" a graph slightly to fix defects. Traditional continuous mathematics, calculus of variations, and topological approximations completely fail here because graph spectra are rigidly discrete.
2. **Symmetry vs. Short Relations**: The most powerful known lower-bound constructions rely entirely on group theory (e.g., Cayley graphs) to guarantee a uniform diameter across all vertices. However, groups naturally induce algebraic relations; the identity word in the group presentation physically corresponds to a cycle in the graph. Imposing sufficient symmetry to ensure a small overall diameter paradoxically forces the existence of short cycles (short relations), which collapses the tree-like expansion. Breaking these symmetries usually destroys the diameter guarantee.
3. **Failure of Probabilistic Methods**: Probabilistic methods (like the Erdős-Rényi random graph models or the Lovász Local Lemma), which brilliantly solve average-case scenarios and the related Cage Problem, fail to provide strong bounds for the degree-diameter problem. Random graphs can bound the *average* distance efficiently, but bounding the *maximum* distance (diameter) strictly to $k$ requires avoiding isolated long paths. Forcing the absolute strict bounds on maximum degree and exact diameter simultaneously introduces massive defect constants, rendering probabilistic graphs far inferior to algebraic ones in this specific context.

## 6. The Gap

The "Gap" represents the precise boundary between known constructions and theoretical limitations.

1. **The Asymptotic General Gap**: For a fixed diameter $k \ge 4$ (excluding $k=5$), the gap is catastrophic. The theoretical Moore bound is $O(d^k)$. The best known constructions, however, generally produce graphs of order $\Omega(d^{\lfloor (k+2)/2 \rfloor})$. Finding the "correct" exponent of $d$ is a massive open barrier. It is widely suspected that the true maximum order for general $k$ is closer to the lower bounds, meaning a new, stronger theoretical upper bound needs to be discovered that accounts for unavoidable cycle formations in dense graphs.
2. **The Exact Defect Gap**: For small fixed parameters (e.g., $d=10, k=5$), the theoretical bound is $100,000$ vertices. The largest known graph might have only $60,000$ vertices. The gap is the exact integer difference between the largest computationally verified graph and the Moore bound. Crossing this barrier requires either exhaustive computational search algorithms that scale beyond $O(d^k)$ complexity, or new families of voltage graphs over non-abelian groups.

## 7. Current Research (as of June 2026)

Active research in extremal graph theory operates on several fronts, primarily driven by institutions such as the University of Auckland, the University of Newcastle (Australia), and the Slovak University of Technology.

- **Voltage Graphs and Liftings**: The dominant methodology for finding new record-breaking large graphs is the technique of "lifting" small base graphs using voltage assignments from finite groups. Recent preprints focus on using semi-direct products and non-abelian groups (like $PSL(2, q)$) as the voltage groups, analyzed using modern SAT solvers and integer linear programming (ILP) to prune the vast search space.
- **The Search for the $d=57$ Moore Graph**: Computational mathematicians continue the hunt for the $(57,2)$ Moore graph ($3,250$ vertices). Theoretical work by Mačaj and Širáň has proven that if it exists, its automorphism group can have a size of at most 375, and likely is trivial. *(frontier — verify)* Recent efforts apply geometric deep learning and graph neural networks (GNNs) as heuristic filters to identify viable adjacency sub-matrices, though a formal existence proof or disproof remains elusive.
- **Directed and Mixed Degree-Diameter Problems**: Because the undirected problem is so rigidly stalled by the lack of Moore graphs, substantial research has shifted to the *Directed Degree-Diameter Problem* (where edges are one-way) and the *Mixed Degree-Diameter Problem* (graphs containing both directed and undirected edges), which feature different spectral constraints and allow for tighter bounds.

## 8. Future Work

Leading mathematicians and combinatorialists advocate for the following research strategies:
- **Determine the existence of the $(57,2)$ Moore graph**: Resolving this final case would permanently close the foundational chapter on diameter-2 Moore graphs inaugurated by Hoffman and Singleton in 1960.
- **Improve Asymptotics for Even Diameters**: For diameter $k=4$, the Moore bound is approximately $d^4$. The best known explicit constructions yield order $d^2$ or $d^3$. Closing this polynomial gap (ideally by proving a strictly lower upper bound for graphs lacking generalized polygon structures) is considered the next great theoretical milestone.
- **Defect $\delta$ Characterization as $d \to \infty$**: Generalize the non-existence proofs for defect 0 and defect 1. If researchers can prove that for any fixed defect $\delta$, graphs do not exist for sufficiently large $d$ and $k$, it would fundamentally reshape our understanding of the upper bounds, proving that the Moore bound is asymptotically unreachable by a growing margin.

## 9. Key References

- **[Foundational]** Hoffman, A. J., & Singleton, R. R. *On Moore graphs with diameters 2 and 3.* IBM Journal of Research and Development, 1960.
- **[Foundational]** Damerell, R. M. *On Moore graphs.* Mathematical Proceedings of the Cambridge Philosophical Society, 1973.
- **[Foundational]** Bannai, E., & Ito, T. *On finite Moore graphs.* Journal of the Faculty of Science, University of Tokyo, 1973.
- **[Survey]** Miller, M., & Širáň, J. *Moore graphs and beyond: A survey of the degree/diameter problem.* Electronic Journal of Combinatorics, 2013.
- **[SOTA / Recent]** Loz, E., & Širáň, J. *New record graphs in the degree-diameter problem.* Australasian Journal of Combinatorics, 2008.

## 10. Worked Example / Concrete Special Case

Consider the concrete problem of finding the maximum possible number of vertices for a graph with a maximum degree constraint of $d = 3$ and a strict diameter constraint of $k = 2$.

**1. Calculate the Theoretical Moore Bound:**
Using the formula for the maximum theoretical capacity, we sum the possible vertices at distance 0, 1, and 2 from a root vertex:
$$ M_{3,2} = 1 + d \sum_{i=0}^{2-1} (d-1)^i = 1 + 3 \left( (3-1)^0 + (3-1)^1 \right) $$
$$ M_{3,2} = 1 + 3(1 + 2) = 10 $$
The absolute theoretical maximum is 10 vertices.

**2. Constructing the Graph:**
To achieve exactly 10 vertices, the graph must be a Moore graph (defect 0). It must be strictly 3-regular, and every vertex must act as the root of a perfect tree of depth 2 with no overlapping edges before distance 2.
The unique solution to this Diophantine configuration is the **Petersen Graph**.

**3. Verification of the Petersen Graph:**
We can construct the Petersen graph using combinatorial sets. Let the 10 vertices be defined as the 2-element subsets of the set $\{1, 2, 3, 4, 5\}$. There are exactly $\binom{5}{2} = 10$ such vertices.
Connect two vertices with an edge if and only if their representative subsets are completely disjoint.

- **Degree Verification:** Consider the vertex $\{1,2\}$. It is disjoint from exactly three other subsets: $\{3,4\}$, $\{3,5\}$, and $\{4,5\}$. Therefore, its degree is 3. By combinatorial symmetry, every vertex in the graph has exactly degree 3.
- **Diameter Verification:** Consider the vertex $\{1,2\}$. It is directly connected to $\{3,4\}$ at distance 1. What about a non-adjacent vertex, such as $\{1,3\}$? Because they share the element `1`, they are not disjoint and thus have no direct edge. However, both $\{1,2\}$ and $\{1,3\}$ are completely disjoint from $\{4,5\}$. Thus, the path $\{1,2\} \to \{4,5\} \to \{1,3\}$ exists, creating a path of exactly length 2.
Because any two non-adjacent vertices will share exactly one element, they will always mutually be disjoint to a third subset made of the remaining two elements of the 5-element set. Therefore, no two vertices are further apart than 2 edges.

This perfectly fulfills the constraints, proving mathematically that $N(3,2) = 10$ and that the defect $\delta = 10 - 10 = 0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*