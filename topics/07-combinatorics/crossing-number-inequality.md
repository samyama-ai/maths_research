---
id: 07-combinatorics/crossing-number-inequality
title: "Crossing Number Inequality"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 07-combinatorics/crossing-number-inequality
title: "Crossing Number Inequality"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Crossing Number Inequality

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/crossing-number-inequality` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Crossing Number Inequality (also known as the Crossing Lemma) is a fundamental theorem bounding the crossing number of dense graphs. While the asymptotic growth rate of the crossing number is completely resolved, the precise optimal multiplicative constant remains an open problem.

Let $G = (V, E)$ be a simple, undirected graph with $v = |V|$ vertices and $e = |E|$ edges. The crossing number $\text{cr}(G)$ is the minimum number of edge intersections in any drawing of $G$ in the plane.

The general inequality states that there exists a universal constant $c > 0$ such that, for any graph where the edge density satisfies $e \ge 4v$ (or, in some formulations, $e > 7v$), the following lower bound holds:
$$ \text{cr}(G) \ge c \cdot \frac{e^3}{v^2} $$

The **Open Problem** is to determine the exact value of the optimal crossing constant, denoted $c^*$, defined as the supremum over all constants $c$ for which the inequality strictly holds as $v \to \infty$ and $e \gg v$.

## 2. Mathematical Foundations

The problem requires rigorous definitions of graph embeddings and topological spaces.

A **drawing** of a graph $G = (V, E)$ in the plane $\mathbb{R}^2$ (or the sphere $\mathbb{S}^2$) is a mapping $\phi$ such that:
1. Each vertex $u \in V$ is mapped to a distinct point $\phi(u) \in \mathbb{R}^2$.
2. Each edge $uv \in E$ is mapped to a simple continuous curve with endpoints $\phi(u)$ and $\phi(v)$.
3. Edges do not pass through any vertex other than their endpoints.
4. Any two edges intersect in at most a finite number of points, and all such intersections are transverse (no tangencies).

A **crossing** is a point in $\mathbb{R}^2 \setminus \phi(V)$ where two edge curves intersect. The crossing number $\text{cr}(G)$ is the minimum number of such crossing points over all valid drawings $\phi$.

Euler's formula dictates that for any planar graph ($v \ge 3$), the number of edges is bounded by $e \le 3v - 6$. From this, we obtain a trivial lower bound for any simple graph by iteratively deleting one edge per crossing until the graph is planar:
$$ \text{cr}(G) \ge e - 3v + 6 > e - 3v $$

The theoretical basis for the Crossing Lemma is a probabilistic argument that amplifies this trivial linear bound into a cubic bound by considering a random induced subgraph $H \subseteq G$. If each vertex is selected independently with probability $p \in (0, 1]$, the expected number of vertices is $pv$, the expected number of edges is $p^2 e$, and the expected number of crossings in the inherited drawing is $p^4 \text{cr}(G)$. Linearity of expectation applied to the trivial bound $\text{cr}(H) > e(H) - 3v(H)$ yields:
$$ p^4 \text{cr}(G) \ge p^2 e - 3pv $$
Optimizing for $p$ establishes the foundational $c = 1/64$ lower bound, but structural limits govern the tightness of this expectation.

## 3. History & State of the Art (SOTA)

The history of the problem is defined by progressive refinements of the constant $c$:

- **1982 / 1983**: The inequality was discovered independently by Ajtai, Chvátal, Newborn, and Szemerédi (1982), and by F. Thomson Leighton (1983) for applications in VLSI design. The original proofs yielded constants of $c = 1/100$ and $c = 1/64$, respectively.
- **1997**: Pach and Tóth explicitly formalized the bounds and initiated the search for the optimal $c^*$.
- **2006**: Pach, Radoičić, Tardos, and Tóth improved the constant to $c \ge 1024 / 31827 \approx 0.0321$. They achieved this by proving stronger bounds on sparse graphs (specifically graphs where no edge crosses more than $k$ times) and substituting these tighter "trivial" bounds into the probabilistic sampling argument.
- **2013 / 2019**: Eyal Ackerman established the current SOTA lower bound of $c \ge 1/29 \approx 0.03448$ (applicable when $e \ge 6.95v$). He accomplished this by deriving exact bounds on the size of topological graphs that lack four pairwise crossing edges.
- **Upper Bounds**: It is structurally known that $c^*$ cannot exceed $\frac{8}{9\pi^2} \approx 0.09006$. This upper limit is derived by analyzing the crossing numbers of complete graphs embedded on the sphere or examining geometric random graphs.

## 4. Partial Results / Verified Cases

While the universal constant $c^*$ remains unknown, exact crossing behavior has been verified for specific geometric constraints and graph classes:

- **Rectilinear Crossing Number ($\overline{\text{cr}}(G)$)**: When edges are strictly constrained to be straight line segments, the optimal constant $\overline{c}^*$ is known to be strictly larger than the topological constant $c^*$. The best known lower bound for the rectilinear case is heavily dependent on specific computational configurations rather than purely probabilistic bounds.
- **Complete Graphs ($K_n$)**: Under the Harary-Hill Conjecture (Guy's Conjecture), the crossing number of the complete graph is hypothesized to be exactly $\frac{1}{4} \lfloor \frac{n}{2} \rfloor \lfloor \frac{n-1}{2} \rfloor \lfloor \frac{n-2}{2} \rfloor \lfloor \frac{n-3}{2} \rfloor$. Because $K_n$ represents the limit of maximum edge density, its bounds are used to cap the maximum possible value of $c^*$.
- **Complete Bipartite Graphs ($K_{m,n}$)**: Zarankiewicz's Conjecture posits the exact crossing number for complete bipartite graphs. Evaluating the Crossing Number Inequality for $K_{n,n}$ gives an effective upper bound of $c \le 1/4$ for this specific family.
- **Low-Density Thresholds**: If the condition $e \ge 4v$ is relaxed to $e \ge 3v$, the inequality still holds, but the best valid constant degrades. The $1/29$ constant is uniquely verified only for $e \ge 6.95v$.

## 5. Principal Obstacles

The main obstacle to finding the precise optimal constant $c^*$ is the "lossy" nature of the probabilistic proof method. The standard technique takes a global property (the crossing number of $G$) and estimates it via the expected crossings of a randomly sampled subgraph $H$. This sampling destroys topological context; a crossing between two edges in $H$ only provides localized information and discards the global routing constraints of the original embedding of $G$.

Furthermore, to improve the constant mathematically, researchers must establish tighter trivial bounds for sparse graphs (e.g., $k$-planar graphs). However, translating local forbidden intersection patterns (like forbidding $4$ pairwise crossing edges) into tight global edge density bounds requires classifying an enormous set of topological configurations.

Finally, the extremal graphs that asymptotically achieve the optimal constant $c^*$ are unknown. Without knowing the target topological structure of the "worst-case" dense graphs that minimize crossings, it is extraordinarily difficult to tailor a bounding technique that saturates the inequality.

## 6. The Gap

The mathematical gap lies strictly between Ackerman's lower bound of $c \ge 1/29 \approx 0.0345$ and the constructive upper bound of $c \le \frac{8}{9\pi^2} \approx 0.0901$. 

To close this gap, one must either:
1. Discover an entirely new family of graph embeddings that dramatically reduces crossings in dense networks, pulling the upper bound down toward $0.0345$.
2. Abandon the standard probabilistic sampling technique and develop a new topological invariant or algebraic method that rigorously forces more crossings globally, pushing the lower bound up toward $0.0901$.

## 7. Current Research (as of June 2026)

Research is largely bifurcated into computational optimization of small configurations and theoretical extensions of topological graph constraints:
- **Topological Graph Theory**: Institutions like the Alfréd Rényi Institute of Mathematics and groups led by János Pach and Eyal Ackerman continue to analyze local crossing limits, specifically bounding graphs with no $k$ pairwise crossing edges for $k \ge 5$.
- **Computational Approaches**: Researchers are increasingly applying Razborov's Flag Algebras and SAT solvers to bound crossing densities in specific minor-free classes *(frontier — verify)*.
- **Edge Density Refinements**: Recent preprints (e.g., Büngener et al., 2024) have explored marginal fractional improvements to the constant (such as $c \approx 1/27.48$) by highly restricting the allowable edge density ranges.

## 8. Future Work

Leading combinatorists suggest that future breakthroughs will require a departure from purely combinatorial bounds into algebraic topology. Suggested pathways include:
- **Higher-order intersection forms**: Generalizing the problem using $\mathbb{Z}_2$-intersection forms to measure algebraic crossings (where odd/even parity of crossings is tracked) rather than strict topological crossings. By the Hanani-Tutte theorem, algebraic and topological crossings are heavily linked, which may yield new bounding techniques.
- **Bisection width optimization**: Exploring the exact relationship between the crossing number and the bisection width of the graph. Improving the constants in the bisection-width inequalities could inversely force a tighter constant in the Crossing Lemma.

## 9. Key References

- **[Foundational]** Ajtai, M., Chvátal, V., Newborn, M. M., & Szemerédi, E. *Crossing-free subgraphs.* Theory and Practice of Combinatorics, 1982.
- **[Foundational]** Leighton, F. T. *Complexity Issues in VLSI: Optimal layouts for the shuffle-exchange graph and other networks.* MIT Press, 1983.
- **[SOTA]** Pach, J., Radoičić, R., Tardos, G., & Tóth, G. *Improving the Crossing Lemma by Finding More Crossings in Sparse Graphs.* Discrete & Computational Geometry, 2006.
- **[SOTA / Recent]** Ackerman, E. *On topological graphs with at most four crossings per edge.* Computational Geometry, 2019.

## 10. Worked Example / Concrete Special Case

To understand where the baseline constant $c = 1/64$ originates, we can walk through the probabilistic proof for a specific graph density.

Assume we have a dense graph $G$ with $v$ vertices and exactly $e = 10v$ edges. Let $\text{cr}(G)$ be its optimal crossing number. 

By Euler's formula, any simple planar graph on $v$ vertices has at most $3v - 6 < 3v$ edges. Therefore, any graph must satisfy the trivial linear bound:
$$ \text{cr}(G) \ge e - 3v $$

We construct a random induced subgraph $H$ by selecting each vertex of $G$ independently with probability $p = \frac{4v}{e}$. Since $e = 10v$, we use $p = \frac{4v}{10v} = \frac{2}{5}$. 

We compute the expected properties of the subgraph $H$:
- **Expected vertices:** $\mathbb{E}[v_H] = p \cdot v = \frac{2}{5}v$
- **Expected edges:** $\mathbb{E}[e_H] = p^2 \cdot e = \left(\frac{2}{5}\right)^2 (10v) = \frac{4}{25}(10v) = \frac{8}{5}v$
- **Expected crossings:** Each crossing requires all $4$ endpoints of the two intersecting edges to be selected. Thus, $\mathbb{E}[\text{cr}(H)] = p^4 \cdot \text{cr}(G) = \left(\frac{2}{5}\right)^4 \text{cr}(G) = \frac{16}{625} \text{cr}(G)$.

Because the trivial bound $\text{cr}(H) \ge e_H - 3v_H$ must hold for *any* subgraph, it also holds for their expectations:
$$ \mathbb{E}[\text{cr}(H)] \ge \mathbb{E}[e_H] - 3\mathbb{E}[v_H] $$

Substituting our expected values:
$$ \frac{16}{625} \text{cr}(G) \ge \frac{8}{5}v - 3\left(\frac{2}{5}v\right) $$
$$ \frac{16}{625} \text{cr}(G) \ge \frac{8}{5}v - \frac{6}{5}v = \frac{2}{5}v $$
$$ \text{cr}(G) \ge \frac{625}{16} \cdot \frac{2}{5} v = \frac{125}{8} v = 15.625 v $$

Now, evaluate the standard $c=1/64$ formulation of the Crossing Lemma inequality for $G$:
$$ \frac{e^3}{64v^2} = \frac{(10v)^3}{64v^2} = \frac{1000v^3}{64v^2} = \frac{125}{8}v = 15.625v $$

This demonstrates perfectly how the optimization of the probabilistic parameter $p = 4v/e$ rigorously isolates the $1/64$ constant for dense graphs, serving as the mathematical floor that modern researchers like Ackerman work to push higher.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*