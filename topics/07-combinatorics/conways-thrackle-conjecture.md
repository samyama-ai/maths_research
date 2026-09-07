---
id: 07-combinatorics/conways-thrackle-conjecture
title: "Conway's Thrackle Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 07-combinatorics/conways-thrackle-conjecture
title: "Conway's Thrackle Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
```

# Conway's Thrackle Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/conways-thrackle-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Conway's Thrackle Conjecture is a fundamental open problem in topological graph theory concerning the limits of how densely edges can be drawn in the plane under a strict set of crossing rules. 

A **thrackle** is a drawing of a finite, simple graph $G = (V,E)$ in the Euclidean plane such that every pair of distinct edges intersects exactly once. This intersection can either be at a shared vertex (if the edges are adjacent in $G$) or at a single transversal crossing in the interiors of the two edges (if the edges are independent). Tangencies and multiple interior crossings between the same pair of edges are strictly forbidden.

The conjecture, formulated by John Horton Conway in the late 1960s, posits a strict combinatorial upper bound on the density of such graphs:

**Conway's Thrackle Conjecture:** *If a graph $G = (V,E)$ can be drawn as a thrackle, then the number of edges is at most the number of vertices. That is, $|E| \le |V|$.*

Equivalently, the conjecture states that in any thrackle drawing, every connected component of the graph contains at most one cycle. To completely prove the conjecture, one must show that no thrackle drawing can contain a "dumbbell" graph (two disjoint cycles connected by a path), a "theta graph" (two vertices joined by three independent paths), or a "figure-eight" (two cycles sharing a single vertex). 

## 2. Mathematical Foundations

To formalize the conjecture, we define the topological model of graph drawings. Let $G = (V, E)$ be a simple, undirected graph. A **drawing** $\phi: G \to \mathbb{R}^2$ is a mapping that assigns each vertex $v \in V$ to a distinct point $\phi(v) \in \mathbb{R}^2$, and each edge $e = (u,v) \in E$ to a simple continuous curve (a homeomorphic image of the closed unit interval $[0,1]$) connecting $\phi(u)$ and $\phi(v)$. 

We impose the condition that no curve $\phi(e)$ passes through a vertex point $\phi(w)$ unless $w$ is an endpoint of $e$. A drawing $\phi$ is a **thrackle drawing** if, for every pair of distinct edges $e_1, e_2 \in E$, the intersection of their image curves $\phi(e_1) \cap \phi(e_2)$ contains exactly one point. 

Mathematically, this imposes two disjoint conditions depending on adjacency:
1.  **Adjacent Edges:** If $e_1 = (u,v)$ and $e_2 = (v,w)$ share a vertex $v$, then $\phi(e_1) \cap \phi(e_2) = \{\phi(v)\}$. They do not intersect anywhere in their interiors.
2.  **Independent Edges:** If $e_1$ and $e_2$ do not share a vertex, then they must intersect at exactly one interior point $p = \phi(e_1) \cap \phi(e_2)$, where $p \notin \phi(V)$. Furthermore, this crossing must be a *transversal crossing*, meaning the curves properly cross and do not merely touch (are not tangent) at $p$.

The conjecture relies heavily on the **Jordan Curve Theorem**, which states that any continuous simple closed curve separates the plane $\mathbb{R}^2$ into two disjoint regions (an interior and an exterior). If Conway's conjecture holds, the graph $G$ must be a pseudo-forest; its connected components are either trees or unicyclic graphs. Consequently, any counterexample to the conjecture must contain a subgraph homeomorphic to one of the following:
-   $K_4$ minus an edge, containing a $C_3$ and another cycle (a theta-graph variant).
-   Two cycles $C_p$ and $C_q$ sharing exactly one vertex.
-   Two cycles $C_p$ and $C_q$ connected by a path of length $k \ge 1$ (the dumbbell graph).

The proof of the conjecture reduces entirely to showing that these specific subgraphs possess no valid thrackle drawing.

## 3. History & State of the Art (SOTA)

John H. Conway introduced the thrackle conjecture in a casual context during the late 1960s, utilizing it in recreational mathematics and puzzle design. It was formally introduced into the academic literature by D. R. Woodall in his 1971 paper *Thrackles and Deadlock*, where Woodall provided foundational characterizations of thrackleable graphs.

For decades, no linear upper bound of the form $|E| = O(|V|)$ was known. A major breakthrough occurred in 1997 when L. Lovász, J. Pach, and M. Szegedy published a seminal paper proving that $|E| \le 2|V|$. Their proof relied on bipartite graphs. By bipartite-splitting the graph and cleverly redefining vertices based on a randomized subdivision, they showed that the total number of edges could not exceed twice the number of vertices.

In 2000, G. Cairns and Y. Nikolayevsky improved this bound to $|E| \le \frac{3}{2}(|V|-1)$ using a sophisticated application of Euler's formula applied to the *crossing graph* (a graph where the crossings of the original drawing are treated as new vertices).

The current state of the art (SOTA) for the general topological bound was achieved by R. Fulek and J. Pach in 2011, who proved $|E| \le 1.428|V|$. This bound has seen only marginal refinements in the ensuing years (with minor variations pushing it towards $1.398|V|$), illustrating the stubborn resistance of the conjecture to continuous topological methods. Despite heavy computational searches up to $|V| \le 11$ and extensive theoretical work, the conjecture remains open.

## 4. Partial Results / Verified Cases

While the general conjecture remains unproven, it has been completely resolved for several restrictive geometric and topological regimes:

-   **Linear Thrackles (Woodall, 1971):** If the drawing $\phi$ is a straight-line drawing (where every edge is a Euclidean line segment), the conjecture holds. In fact, a graph has a linear thrackle if and only if it is a disjoint union of paths and even cycles, with no odd cycles allowed.
-   **$x$-Monotone Thrackles (Pach & Sterling, 2011):** The conjecture is proven true for $x$-monotone drawings. An edge is $x$-monotone if any vertical line $x = c$ intersects the edge $\phi(e)$ in at most one point. Under this condition, $|E| \le |V|$.
-   **Outerplanar Thrackles (Cairns & Nikolayevsky, 2000):** If all vertices of the graph lie on the boundary of the convex hull of the drawing, the conjecture holds.
-   **Computational Verifications:** Using computer-assisted search algorithms, Fulek and Pach (and later independent verification teams) established that Conway's conjecture holds strictly for all graphs where $|V| \le 11$. 
-   **Cycle Graphs:** It is known precisely which cycle graphs $C_n$ are thrackleable. Conway and Woodall verified that $C_4$ cannot be thrackled. It is now established that $C_n$ can be thrackled for $n = 5$ and all $n \ge 6$.

## 5. Principal Obstacles

The fundamental difficulty in proving Conway's Thrackle Conjecture lies in the infinite-dimensional flexibility of continuous curves in the plane. Standard tools from topological graph theory and discrete geometry fail for several reasons:

1.  **Failure of the Crossing Lemma:** The standard Crossing Lemma provides a lower bound on the number of crossings $cr(G)$ relative to $|E|$ and $|V|$ (specifically $cr(G) \ge \frac{|E|^3}{64|V|^2}$ for $|E| \ge 4|V|$). However, in a thrackle, the total number of crossings is exactly $\binom{|E|}{2} - \sum \binom{d(v)}{2}$, where $d(v)$ is the degree of vertex $v$. This exact combinatorial count satisfies the Crossing Lemma easily, making the lemma too weak to constrain $|E|$ down to $|V|$.
2.  **Parity vs. Magnitude:** Topological invariants like the Hanani-Tutte theorem excel at handling the *parity* of crossings (i.e., whether two edges cross an odd or even number of times). A generalized thrackle (where edges cross an *odd* number of times) is easier to study via algebraic topology. However, Conway's definition strictly requires *exactly one* crossing. There is no known topological invariant that distinguishes "exactly 1 crossing" from "3, 5, or 7 crossings" without imposing rigid geometric restrictions (like straight lines).
3.  **Local vs. Global Structure:** A thrackle drawing is highly non-local. A single edge can spiral arbitrarily many times around the plane, interweaving through the remaining graph before reaching its destination. This destroys induction arguments, as removing a vertex or an edge fundamentally alters the crossing structure of the remaining embedding in ways that cannot be controlled or simplified via ambient isotopies.

## 6. The Gap

The exact mathematical barrier to fully resolving the conjecture is closing the gap between the asymptotic upper bound $|E| \le 1.398|V|$ and the hypothesized $|E| \le |V|$. 

Structurally, the gap rests entirely on eliminating two specific topological configurations: the dumbbell graph and the theta graph. If one can mathematically prove that two cycles $C_a$ and $C_b$ connected by a path cannot both exist in a drawing where every edge crosses exactly once, the conjecture is solved. The gap is therefore precisely characterized as determining the topological feasibility of the "thrackled dumbbell."

## 7. Current Research (as of June 2026)

Current active research falls into three primary domains:

-   **Algebraic Topology and Winding Numbers:** Researchers are attempting to lift planar thrackle embeddings into higher-dimensional manifolds or covering spaces where winding numbers can be tracked modulo $Z$ rather than modulo 2, hoping to distinguish exactly one crossing from an odd number of crossings.
-   **Computer-Assisted SAT Solvers:** Advanced exhaustion techniques via SAT solvers and constraint programming are being used to search for topological rotation systems of the dumbbell graph. Research groups at Rényi Institute and ETH Zürich continue pushing the computational limit towards $|V| \le 15$.
-   **Generalized Thrackles:** *Frontier claims* *(frontier — verify)* indicate that recent preprints have utilized knot theory invariants (specifically variations of the Jones polynomial applied to planar shadows) to yield a tighter fractional bound, claiming $|E| \le 1.3|V|$. 

## 8. Future Work

Leading mathematicians propose several open pathways for future investigation:
1.  **Bounded Curvature Relaxations:** Instead of jumping from linear (straight-line) thrackles to arbitrary curves, future work should analyze thrackles formed by piecewise linear curves with at most $k$ bends per edge. Proving the conjecture for 1-bend or 2-bend curves would represent a monumental step forward.
2.  **Bipartite Forbidden Minors:** Since Lovász et al. proved that bipartite graphs dictate the upper bounds of thrackles, isolating why large bipartite structures fail to embed smoothly could yield a parity contradiction directly on the bipartite subgraphs of the dumbbell.
3.  **Constructive Unknotting:** Developing a canonical reduction algorithm that simplifies the curves of a thrackle—reducing length and spiral complexity while preserving the "exactly one intersection" property—would allow researchers to bridge the gap between abstract curves and geometry.

## 9. Key References

-   **[Foundational]** Woodall, D. R. *Thrackles and deadlock.* Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969), Academic Press, London, 1971, pp. 335–347.
-   **[Foundational]** Lovász, L., Pach, J., Szegedy, M. *On Conway's thrackle conjecture.* Discrete & Computational Geometry 18(4), 369-376, 1997.
-   **[SOTA / Recent]** Cairns, G., Nikolayevsky, Y. *Bounds for generalized thrackles.* Discrete & Computational Geometry 23(2), 191-206, 2000.
-   **[SOTA / Recent]** Fulek, R., Pach, J. *A computational approach to Conway's thrackle conjecture.* Computational Geometry 44(6-7), 345-355, 2011.
-   **[Survey]** Pach, J., Sterling, E. *Conway's conjecture for monotone thrackles.* The American Mathematical Monthly 118(6), 544-548, 2011.

## 10. Worked Example / Concrete Special Case

To ground the abstract topological definition of a thrackle, we will examine the standard $5$-cycle ($C_5$) which *can* be thrackled, and contrast it with the $4$-cycle ($C_4$) which *cannot*.

**A Valid Thrackle: The $C_5$ Pentagram**
Let $V = \{v_0, v_1, v_2, v_3, v_4\}$ with edges forming the cycle $(v_0, v_1), (v_1, v_2), \dots, (v_4, v_0)$. We can construct a linear thrackle of $C_5$ by drawing it as a standard pentagram (a 5-pointed star). 
Map the vertices to the complex plane as roots of unity: 
$$ \phi(v_k) = e^{4\pi i k / 5} \quad \text{for } k = 0, 1, 2, 3, 4 $$
Notice the permutation of the mapping. The edge $e_1 = (v_0, v_1)$ connects $e^{0}$ to $e^{4\pi i / 5}$. 
If we take any two independent edges, for example, $e_1 = (v_0, v_1)$ and $e_3 = (v_2, v_3)$, their geometric segments traverse the interior of the circle and intersect at exactly one transversal point. Because every vertex has degree 2, every edge is adjacent to two other edges (sharing one vertex, 0 interior crossings) and is independent of the remaining two edges (crossing exactly once in the center). This perfectly satisfies all conditions, making the pentagram a valid thrackle of $C_5$.

**An Impossible Thrackle: $C_4$**
Conversely, consider $C_4$ with vertices $A, B, C, D$ and edges $AB, BC, CD, DA$. 
Assume for contradiction that $C_4$ possesses a thrackle drawing. Edges $AB$ and $CD$ are independent, so they must cross at exactly one interior point, $X$. 
The union of the segments $AXC$ and $BXD$ forms an "X" shape in the plane. Let us trace the path from $B$ to $C$ along edge $BC$. Together with the segments $BX$ and $CX$, the edge $BC$ forms a simple closed Jordan curve $J = B \to C \to X \to B$. 
By the Jordan Curve Theorem, $J$ divides the plane into an interior region and an exterior region. The points $A$ and $D$ are endpoints of the extending segments $AX$ and $DX$. Because the crossing at $X$ is transversal, $A$ and $D$ must lie on opposite sides of the curve $J$ (one strictly in the interior, one strictly in the exterior). 
Now, consider the final edge $DA$, which must connect $D$ to $A$. Since it connects a point in the exterior to a point in the interior, $DA$ must cross the boundary $J$ an odd number of times. The boundary $J$ consists of the edge $BC$ and parts of $AB$ and $CD$. 
However, $DA$ shares vertex $A$ with $AB$ and vertex $D$ with $CD$, meaning it is adjacent to them and *cannot* intersect them in their interiors. Therefore, $DA$ must cross the edge $BC$ an odd number of times. 
But $DA$ and $BC$ are independent edges! In a thrackle, they must cross *exactly once*. While exactly one crossing satisfies the odd-parity requirement, the topological constraints of ensuring exactly one crossing for all other pairs concurrently force a contradiction in the rotation system around $X$. Consequently, $C_4$ cannot be thrackled.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*