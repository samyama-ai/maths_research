---
id: 07-combinatorics/dinitz-conjecture
title: "Dinitz Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dinitz Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/dinitz-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Dinitz Conjecture (now a theorem) is a foundational result in combinatorics concerning the filling of square arrays under restrictive local constraints. It states that for any $n \times n$ array, if every cell $(i, j)$ is equipped with a set (or "list") $S(i,j)$ of size $n$, it is always possible to select exactly one element from each set $S(i,j)$ to place in the cell $(i, j)$ such that no element is repeated in any row or column. 

In the language of graph theory, the conjecture posits that the list chromatic index of the complete bipartite graph $K_{n,n}$ is exactly equal to its maximum degree $n$. Formally, if $\chi_l'(G)$ denotes the list chromatic index of a graph $G$, the statement is:
$$ \chi_l'(K_{n,n}) = n $$

A complete proof was provided by Fred Galvin in 1994, who verified a more generalized statement: for any bipartite multigraph $G$, the list chromatic index equals the standard chromatic index, $\chi_l'(G) = \chi'(G)$.

## 2. Mathematical Foundations

The problem rests upon the frameworks of graph coloring and choosability. Let $G = (V, E)$ be a finite multigraph. 

- **Edge Coloring and Chromatic Index:** An edge coloring is an assignment of labels (colors) to the edges of $G$ such that no two adjacent edges share the same color. The minimum number of colors required for a valid edge coloring is the chromatic index, denoted $\chi'(G)$.
- **List Edge Coloring (Choosability):** Let $L: E \to 2^{\mathbb{N}}$ be an assignment of lists of available colors to each edge. A proper $L$-coloring is an edge coloring $c$ such that $c(e) \in L(e)$ for all $e \in E$, and $c(e) \neq c(f)$ for any adjacent edges $e$ and $f$.
- **List Chromatic Index:** The list chromatic index, $\chi_l'(G)$ (also called the edge-choosability index), is the smallest integer $k$ such that $G$ admits a proper $L$-coloring for *every* list assignment $L$ where $|L(e)| \ge k$ for all $e \in E$.
- **Line Graph $L(G)$:** The problem of edge coloring a graph $G$ is structurally isomorphic to vertex coloring its line graph $L(G)$, where vertices of $L(G)$ represent edges of $G$, and edges in $L(G)$ connect vertices whose corresponding edges in $G$ are incident. For $G = K_{n,n}$, the line graph $L(K_{n,n})$ is known as the Rook's graph $R_n$.
- **Kőnig's Line Coloring Theorem:** A classical result stating that for any bipartite multigraph $G$, the chromatic index equals the maximum degree: $\chi'(G) = \Delta(G)$. Thus, for $K_{n,n}$, $\chi'(K_{n,n}) = n$.

The Dinitz conjecture essentially asserts that local restrictions (arbitrary lists) do not inflate the number of required colors beyond the global minimum required for standard edge coloring in complete bipartite graphs.

## 3. History & State of the Art (SOTA)

The problem was formulated by Jeff Dinitz in 1979 at the 10th Southeastern Conference on Combinatorics, Graph Theory, and Computing. It was conceived as a generalization of Latin squares; a standard $n \times n$ Latin square is simply a valid list coloring where every cell has the identical list $L = \{1, 2, \dots, n\}$. Dinitz questioned whether the structural rigidity of Latin squares survived when the uniform lists were replaced by arbitrary heterogenous lists of the same size.

Independently around the same time, V. G. Vizing (1976) and Erdős, Rubin, and Taylor (1979) laid the foundations for list coloring and choosability. Vizing proposed the vastly more general List Edge Coloring Conjecture (LECC), which states that $\chi_l'(G) = \chi'(G)$ for *all* multigraphs. The Dinitz conjecture thus represented the most high-profile test case for the LECC.

For 15 years, the problem resisted all attempts. Early SOTA bounds were established by Roland Häggkvist in 1989, who proved $\chi_l'(K_{n,n}) \le c n$ for some constant $c > 1$. The introduction of the Polynomial Method by Noga Alon and Michael Tarsi in 1992 created a new algebraic vector of attack, allowing Jeannette Janssen (1993) to bound the Dinitz problem at $\chi_l'(K_{n,n}) \le n+1$.

The complete resolution came suddenly in 1994 from Fred Galvin. Abandoning the algebraic polynomial methods, Galvin utilized the Gale-Shapley Stable Marriage Theorem, demonstrating that directed line graphs of bipartite multigraphs possess kernel-perfect orientations, proving $\chi_l'(G) = \chi'(G) = \Delta(G)$ for all bipartite multigraphs.

## 4. Partial Results / Verified Cases

Prior to Galvin's sweeping proof, several critical partial cases were verified:
- **Small Values of $n$:** Computational verifications easily handled $n \le 4$. For $n=2$ and $n=3$, algebraic reductions and brute-force 1-factorizations confirmed the conjecture early on.
- **Asymptotic Convergence:** Using the probabilistic "nibble" method, Jeff Kahn (1996) verified the asymptotic form of the broader List Edge Coloring Conjecture, proving that for any multigraph $G$, $\chi_l'(G) \le (1+o(1))\chi'(G)$ as $\Delta(G) \to \infty$. 
- **The $n+1$ Bound:** Janssen (1993) proved $\chi_l'(K_{n,n}) \le n+1$ by embedding the Rook's graph polynomial into a larger algebraic space to avoid coefficient vanishing.
- **Prime Dimensional Arrays:** Before Galvin, Alon and Tarsi utilized algebraic geometry to prove that if $n=p$ (a prime number), a slightly restricted version of the conjecture held true based on the non-vanishing of polynomials over finite fields $\mathbb{F}_p$.

## 5. Principal Obstacles

The problem remained unsolved for over a decade because both classical graph coloring reductions and advanced algebraic techniques encountered hard theoretical limits:

1. **Failure of Vertex Choosability Bounds:** The line graph $L(K_{n,n})$ requires $n$ colors, but general vertex list coloring behaves pathologically compared to standard coloring. There exist bipartite graphs (which are 2-colorable in the standard sense) that require arbitrarily large lists to be list-colorable (e.g., $\chi_l(K_{m, 2^m}) = m+1$). Because $L(K_{n,n})$ contains massive complete bipartite subgraphs, standard vertex choosability bounds fail catastrophically, predicting required list sizes of $O(n \log n)$ rather than $n$.
2. **Algebraic Cancellation in the Polynomial Method:** The Alon-Tarsi theorem detects choosability by analyzing the graph polynomial $P_G = \prod_{uv \in E} (x_u - x_v)$. For a graph to be $k$-choosable, a specific coefficient in $P_G$ must be non-zero. This coefficient measures the difference between the number of even and odd Eulerian orientations of the graph. Because $L(K_{n,n})$ is highly symmetric, the even and odd orientations perfectly cancel each other out for the target degree $n-1$. This exact algebraic cancellation yielded a coefficient of $0$, rendering the Polynomial Method completely blind to the exact $n$-choosability of the graph and artificially halting progress at $n+1$.

## 6. The Gap

Because Galvin's proof entirely resolves the Dinitz conjecture for bipartite multigraphs, the modern "gap" in this domain is the leap from bipartite graphs to the generalized List Edge Coloring Conjecture (LECC): $\chi_l'(G) = \chi'(G)$ for *all* multigraphs. 

Galvin's proof elegantly crosses the bipartite threshold by defining Gale-Shapley preferences between the two partitions (Rows and Columns). However, for non-bipartite graphs containing odd cycles, it is impossible to globally partition the vertices into "proposers" and "receivers." The stable matching orientations generate directed cycles without kernels when forced onto non-bipartite line graphs. Crossing this gap requires an entirely new mathematical apparatus that does not rely on stable matchings.

## 7. Current Research (as of June 2026)

Research stemming from the Dinitz conjecture heavily revolves around modern generalizations of choosability:
- **Paintability (Online List Coloring):** Introduced by Schauz, online list coloring forces the graph to be colored dynamically as lists are revealed one element at a time. The Dinitz array has been proven to be $n$-paintable, demonstrating that Galvin's stable matching structures are robust even against adversarial temporal dynamics.
- **DP-Coloring (Correspondence Coloring):** Introduced by Dvořák and Postle, DP-coloring is a severe generalization of list coloring where the "names" of the colors in the lists can permute along the edges, breaking global color identification. Researchers are currently investigating the DP-chromatic index of generalized complete graphs. *(frontier — verify: whether exact DP-chromatic index for arbitrary bipartite line graphs strictly equals $\Delta$ is still under intense bounds testing).*
- **Total List Coloring Conjecture:** Researchers are attempting to fuse Galvin's bipartite edge methods with vertex choosability bounds to prove that the total list chromatic number $\chi_{l}''(G) = \chi''(G)$.

## 8. Future Work

Leading algebraic combinatorialists suggest the following pathways:
- **Nullstellensatz Extensions:** Developing asymmetric non-vanishing conditions for the Combinatorial Nullstellensatz that can detect choosability even when symmetric coefficients cancel, potentially bridging the gap to the LECC.
- **Planar Graph Edge Choosability:** Proving the LECC specifically for planar graphs with maximum degree $\Delta \ge 5$, isolating the structural topological properties from the purely combinatorial ones.
- **Algorithmic Complexity of DP-Coloring:** Since Galvin's Gale-Shapley reduction yields a polynomial-time algorithm ($O(V^2)$) to actually find the Dinitz coloring, mapping the computational complexity boundary of extending these kernel-perfect orientations into correspondence coloring regimes remains a major target.

## 9. Key References

- **[Foundational]** Erdős, P., Rubin, A. L., & Taylor, H. *Choosability in graphs*. Congressus Numerantium, 1979. 
- **[Foundational]** Dinitz, J. H. *Problem posed at the 10th Southeastern Conference on Combinatorics, Graph Theory, and Computing*. 1979.
- **[SOTA / Recent]** Galvin, F. *The list chromatic index of a bipartite multigraph*. Journal of Combinatorial Theory, Series B, 1995.
- **[SOTA / Recent]** Kahn, J. *Asymptotically good list-colorings*. Journal of Combinatorial Theory, Series A, 1996.
- **[Survey]** Alon, N. *Restricted colorings of graphs*. Surveys in Combinatorics, 1993.
- **[SOTA / Recent]** Janssen, J. C. M. *The Dinitz problem solved for rectangles*. Bulletin of the American Mathematical Society, 1993.
- **[Survey]** Schauz, U. *Mr. Paint and Mrs. Fault: Elements of Epistemic Graph Theory*. The Electronic Journal of Combinatorics, 2009.

## 10. Worked Example / Concrete Special Case

Consider the $2 \times 2$ Dinitz problem. We operate on $G = K_{2,2}$ with vertex partitions $X = \{x_1, x_2\}$ (rows) and $Y = \{y_1, y_2\}$ (columns). The edges are $E = \{e_{11}, e_{12}, e_{21}, e_{22}\}$.
We establish a baseline proper edge coloring $c: E \to \{1, 2\}$ mapping:
- $c(e_{11}) = 1$, $c(e_{12}) = 2$
- $c(e_{21}) = 2$, $c(e_{22}) = 1$

Galvin's method requires orienting the line graph $L(K_{2,2})$ based on $c$ to create a digraph $D$. 
**Orientation Rule:** For adjacent edges sharing a vertex $v$: if $v \in X$, direct the edge with the *larger* color to the edge with the *smaller* color. If $v \in Y$, direct from *smaller* to *larger*.

Let's calculate the directed edges:
- At $x_1 \in X$: Edges are $e_{11}, e_{12}$. Since $c(e_{12}) > c(e_{11})$, direct $e_{12} \to e_{11}$.
- At $x_2 \in X$: Edges are $e_{21}, e_{22}$. Since $c(e_{21}) > c(e_{22})$, direct $e_{21} \to e_{22}$.
- At $y_1 \in Y$: Edges are $e_{11}, e_{21}$. Since $c(e_{11}) < c(e_{21})$, direct $e_{11} \to e_{21}$.
- At $y_2 \in Y$: Edges are $e_{12}, e_{22}$. Since $c(e_{22}) < c(e_{12})$, direct $e_{22} \to e_{12}$.

The resulting digraph $D$ forms a directed cycle: $e_{12} \to e_{11} \to e_{21} \to e_{22} \to e_{12}$.
Crucially, the maximum out-degree of any vertex in $D$ is $1$. 

Assume an adversary provides arbitrary lists of size 2, for instance:
$L(e_{11})=\{a,b\}$, $L(e_{12})=\{b,c\}$, $L(e_{21})=\{a,c\}$, $L(e_{22})=\{b,c\}$.

We extract an independent set (kernel) for the color $b$. The subgraph of edges containing $b$ in their lists is $S_b = \{e_{11}, e_{12}, e_{22}\}$. The induced edges on $S_b$ from $D$ are $e_{12} \to e_{11}$ and $e_{22} \to e_{12}$. 
A kernel is an independent set $K$ where all external vertices in the subgraph point into $K$. For $S_b$, the unique kernel is $K_b = \{e_{11}, e_{22}\}$ (since $e_{12}$ points to $e_{11} \in K_b$, and $e_{11}, e_{22}$ are independent).

We safely assign color $b$ to $K_b$: $c_l(e_{11}) = b$, $c_l(e_{22}) = b$.
The remaining uncolored edges $e_{12}$ and $e_{21}$ have colors $c$ and $a$ left in their lists, respectively. We assign $c_l(e_{12}) = c$ and $c_l(e_{21}) = a$. The array is successfully and properly colored, demonstrating the mechanics of Galvin's stable-matching kernel perfect orientation on the line graph.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*