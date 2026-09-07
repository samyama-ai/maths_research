---
id: 07-combinatorics/colin-de-verdiere-conjecture
title: "Colin de Verdière Parameter Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Colin de Verdière Parameter Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/colin-de-verdiere-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Colin de Verdière Parameter Conjecture postulates a profound and direct relationship between a continuous algebraic-geometric graph invariant and a discrete topological coloring property. Specifically, it conjectures that for any finite, simple, undirected graph $G$, the chromatic number $\chi(G)$ is strictly bounded from above by the Colin de Verdière spectral parameter $\mu(G)$ plus one:

$$ \chi(G) \le \mu(G) + 1 $$

A complete proof of this conjecture would establish a master theorem in algebraic graph theory, subsuming the Four Color Theorem as a special case and implying the famously unresolved Hadwiger's Conjecture. A valid proof requires either a topological structural characterization for all levels of $\mu(G)$ combined with discrete coloring theorems, or a direct algebraic method for extracting proper colorings from the eigenvectors of the defining matrices. A disproof requires the construction of a graph—likely highly symmetric and critically dense—whose chromatic number strictly exceeds $\mu(G) + 1$.

## 2. Mathematical Foundations

Let $G = (V,E)$ be a finite, simple, undirected graph with $n$ vertices. The Colin de Verdière parameter $\mu(G)$ is defined as the maximum corank (the dimension of the kernel, $\dim(\ker M)$) over all real symmetric $n \times n$ matrices $M = (M_{i,j})$ that satisfy the following three rigorous conditions:

1. **Adjacency Support:** The off-diagonal entries respect the edges of the graph such that for all $i \neq j$:
   - $M_{i,j} < 0$ if $\{i,j\} \in E$
   - $M_{i,j} = 0$ if $\{i,j\} \notin E$
   (The diagonal entries $M_{i,i}$ are entirely unconstrained).

2. **Spectral Signature:** The matrix $M$ possesses exactly one strictly negative eigenvalue, and its algebraic multiplicity is exactly $1$.

3. **Strong Arnold Property (SAP):** The matrix $M$ must represent a regular point (a transversal intersection) within the manifold of matrices satisfying the adjacency constraints. Equivalently, if $X = (X_{i,j})$ is any real symmetric $n \times n$ matrix satisfying:
   - $M X = 0$
   - $X_{i,j} = 0$ whenever $i=j$ or $\{i,j\} \in E$
   then $X$ must be the zero matrix ($X = \mathbf{0}$). 

In differential geometry terms, SAP ensures that the tangent space to the manifold of matrices with the same rank as $M$ intersects the space of matrices respecting the graph's non-edges only at the origin. 

Crucially, these conditions ensure that $\mu(G)$ is minor-monotone. If $H$ is a graph minor of $G$ (obtained by deleting edges/vertices or contracting edges), then:
$$ \mu(H) \le \mu(G) $$
The conjecture states that the minimum number of colors $\chi(G)$ required to color the vertices such that no two adjacent vertices share a color is bounded by this maximum corank plus one.

## 3. History & State of the Art (SOTA)

Yves Colin de Verdière introduced the parameter $\mu(G)$ in his 1990 paper, *Sur un nouvel invariant des graphes et un critère de planarité*. His motivation originated from differential geometry and continuous mathematics—specifically, bounding the multiplicity of the second eigenvalue of Schrödinger operators of the form $-\Delta + V$ on Riemannian surfaces. By discretizing the surface into a graph and the operator into a generalized Laplacian matrix, he isolated $\mu(G)$.

Colin de Verdière achieved a massive breakthrough by proving that $\mu(G) \le 3$ if and only if $G$ is a planar graph. Given the Four Color Theorem (proven by Appel and Haken in 1976), this meant that for $\mu(G) \le 3$, the chromatic number was bounded by $\chi(G) \le 4 \le \mu(G) + 1$. 

Simultaneously, it was trivially verifiable that for complete graphs $K_n$, the parameter is $\mu(K_n) = n - 1$, leading to $\chi(K_n) = \mu(K_n) + 1$. Observing this perfect alignment across trees, planar graphs, and complete graphs, Colin de Verdière generalized the bound to $\chi(G) \le \mu(G) + 1$ for all graphs.

The state of the art primarily rests on connecting $\mu(G)$ to Hadwiger's Conjecture. The Hadwiger number $h(G)$ is the size of the largest complete graph minor in $G$. It is a proven theorem that $h(G) - 1 \le \mu(G)$. Therefore, if Colin de Verdière's conjecture holds ($\chi(G) \le \mu(G) + 1$), it provides an analytical pathway to Hadwiger's Conjecture ($\chi(G) \le h(G)$). Currently, general bounds on $\chi(G)$ using $\mu(G)$ remain as elusive as Hadwiger's, with SOTA progress limited to minor-free structural classifications for specific low dimensions.

## 4. Partial Results / Verified Cases

The conjecture has been rigorously verified for specific, low-dimensional structural classes of graphs where $\mu(G) \le 4$. Because $\mu(G)$ characterizes specific topological embeddings, the verifications rely on classical graph coloring theorems:

- **$\mu(G) \le 1$:** The graph $G$ is a linear forest (a collection of disjoint paths). Paths are trivially bipartite, so $\chi(G) \le 2 \le \mu(G) + 1$.
- **$\mu(G) \le 2$:** The graph $G$ is outerplanar. Outerplanar graphs always contain a vertex of degree at most $2$, making them structurally 3-colorable via basic degeneracy bounds. Thus, $\chi(G) \le 3 \le \mu(G) + 1$.
- **$\mu(G) \le 3$:** The graph $G$ is planar. By the Four Color Theorem, planar graphs are 4-colorable, satisfying $\chi(G) \le 4 \le \mu(G) + 1$.
- **$\mu(G) \le 4$:** The graph $G$ is linklessly embeddable in $\mathbb{R}^3$. Robertson, Seymour, and Thomas (1993) proved this structural equivalence, showing these graphs exclude the Petersen family as minors. Because linklessly embeddable graphs are known to be 5-colorable, the conjecture holds: $\chi(G) \le 5 \le \mu(G) + 1$.
- **Complete Graphs:** For the complete graph $K_n$, the invariant is exactly $\mu(K_n) = n - 1$. The chromatic number is $\chi(K_n) = n$. The bound holds with perfect equality: $n \le (n-1) + 1$.
- **Chordal Graphs:** For chordal graphs, the chromatic number equals the Hadwiger number ($\chi(G) = h(G)$). Since it is unconditionally proven that $h(G) - 1 \le \mu(G)$, it immediately follows that $\chi(G) \le \mu(G) + 1$ holds for all chordal graphs.

## 5. Principal Obstacles

The enduring difficulty of the conjecture stems from a fundamental mismatch between the analytical tools used to optimize $\mu(G)$ and the discrete combinatorial techniques required for graph coloring.

1. **Non-linearity and Fragility of the Strong Arnold Property (SAP):** 
SAP is a transversality condition ensuring the matrix $M$ is a non-degenerate, regular point in an algebraic variety. Standard discrete proof techniques for coloring—such as deleting a vertex, contracting an edge, or identifying non-adjacent vertices—act as discontinuous perturbations on the matrix $M$. These operations routinely destroy the SAP, causing the matrix to fall out of the regular manifold and the kernel dimension (the corank) to collapse unpredictably. 
2. **Spectral Insensitivity to Independent Sets:**
Standard spectral bounds for the chromatic number, such as Hoffman's bound ($\chi(G) \ge 1 - \frac{\lambda_{\max}}{\lambda_{\min}}$), rely on the extreme eigenvalues which directly correlate with the size of independent sets. The Colin de Verdière invariant, conversely, relies on the *multiplicity of the zero eigenvalue* (corank). Corank measures global topological embedding complexity rather than local colorability. There is no known mathematical machinery to extract a discrete proper coloring from the continuous eigenvectors of a high-dimensional null space.
3. **The Shadow of Hadwiger's Conjecture:**
Because $\chi(G) \le \mu(G) + 1$ acts as a spectral relaxation of Hadwiger's Conjecture ($\chi(G) \le h(G)$), proving it requires overcoming the same structural bottlenecks. For instance, any proof must somehow naturally handle the existence of small counter-examples to the false Hajós conjecture, distinguishing between graph minors and topological minors without relying strictly on physical embeddings.

## 6. The Gap

The precise mathematical barrier lies at $\mu(G) = 5$. 

For $\mu(G) \in \{1, 2, 3, 4\}$, the conjecture was solved by translating the algebraic bound into a physical topological embedding property (paths, outerplanarity, planarity in $\mathbb{R}^2$, and linkless embeddings in $\mathbb{R}^3$), and subsequently applying discrete coloring theorems to those topologies. 

However, for $\mu(G) \ge 5$, this translation pipeline breaks down entirely. The geometric analog for $\mu(G) = 5$ is not a simple knotless embedding in $\mathbb{R}^4$. We currently lack a forbidden-minor structural characterization for $\mu(G) = 5$. Without knowing what $\mu(G) \le 5$ actually means in terms of graph structure or forbidden minors, it is currently impossible to leverage standard combinatorial tools to prove $\chi(G) \le 6$ for this class. To cross the gap, researchers must either identify the topological nature of higher $\mu(G)$ values or bypass topology entirely with a purely algebraic proof.

## 7. Current Research (as of June 2026)

Active research surrounding the conjecture is heavily balkanized into algebraic and topological camps:

- **Algebraic Graph Theory (Matrix Relaxations):** Researchers are studying relaxations of $\mu(G)$ that are easier to manipulate. The invariant $\nu(G)$ removes the negative eigenvalue constraint, while $\xi(G)$ requires the matrix to be positive semi-definite while retaining SAP. By framing these variants within the Lovász $\theta$-function and semi-definite programming (SDP) hierarchies, groups at Georgia Tech and CWI Amsterdam aim to sandwich $\mu(G)$ and relate it strictly to fractional chromatic numbers.
- **Topological Graph Theory (Higher Dimensions):** Building on the work of Robertson, Seymour, and Thomas, topological graph theorists are attempting to classify the forbidden minor families for $\mu(G) \le 5$ and $\mu(G) \le 6$. They are investigating "knotless" embeddings and generalized spatial graph theory, aiming to find the exact combinatorial obstructions that prevent $K_7$ from having $\mu \le 5$.
- *(frontier — verify)* Recent preprints from researchers working on algorithmic graph theory suggest that for dense random graphs (e.g., Erdős–Rényi $G(n,p)$), continuous SDP-based bounds for the Hadwiger number strictly dominate $\mu(G)$. This suggests that $\mu(G)$ may be an excessively loose bound for dense graphs, implying the conjecture is likely true asymptotically, pushing the search for counterexamples toward sparse, highly-symmetric critical graphs (such as generalized Kneser graphs or Cayley graphs of specific sporadic groups).

## 8. Future Work

Leading mathematicians have outlined several open pathways and fallback strategies to tackle the conjecture:

1. **Fractional Relaxations:** Before proving $\chi(G) \le \mu(G) + 1$, a logical stepping stone is to prove the bound for the fractional chromatic number: $\chi_f(G) \le \mu(G) + 1$. Because $\chi_f(G)$ is the solution to a linear program, it might interface more cleanly with the algebraic null-space constraints of the matrix $M$ than integer colorings.
2. **Intermediate / Asymptotic Bounds:** Given the extreme difficulty of Hadwiger's conjecture, proving a constant-factor bound like $\chi(G) \le c \cdot \mu(G)$ for some $c > 1$ would be a major breakthrough. Utilizing recent advances in minor-closed structure theorems (which yield $O(h \log h)$ limits for Hadwiger), future work could attempt to adapt these to prove $\chi(G) = O(\mu(G) \log \mu(G))$.
3. **Spectral Coloring Algorithms:** A promising algorithmic strategy is to develop a projection technique that maps the coordinates of the $\mu(G)$-dimensional null space of $M$ to the surface of a hypersphere, akin to the Goemans-Williamson max-cut algorithm. If the eigenvectors can be partitioned geometrically, it could yield a deterministic $(\mu(G)+1)$-coloring.
4. **Computational Counterexamples:** Develop parallelized algorithms to rigorously test the Strong Arnold Property on massively large highly symmetric graphs, specifically searching for a counterexample where $\mu(G)$ is artificially suppressed below $\chi(G) - 1$.

## 9. Key References

- **[Foundational]** Colin de Verdière, Y. *Sur un nouvel invariant des graphes et un critère de planarité.* Journal of Combinatorial Theory, Series B, 1990.
- **[Foundational]** Robertson, N., Seymour, P., and Thomas, R. *Linkless embeddings of graphs in 3-space.* Bulletin of the American Mathematical Society, 1993.
- **[Survey]** van der Holst, H., Lovász, L., and Schrijver, A. *The Colin de Verdière graph parameter.* Graph Theory and Computational Biology (Balatonlelle, 1996), Bolyai Society Mathematical Studies, 1999.
- **[SOTA / Recent]** Kotlov, A., Lovász, L., and Vempala, S. *The Colin de Verdiere number and sphere representations of a graph.* Combinatorica, 1997.
- **[SOTA / Recent]** Norin, S., and Song, J. *A new bound for Hadwiger's conjecture.* Journal of Combinatorial Theory, Series B, 2020. 

## 10. Worked Example / Concrete Special Case

To ground the abstract definition of the conjecture, consider the complete graph $G = K_4$. We will manually construct a matrix $M$ to compute the invariant $\mu(K_4)$ and verify the conjecture $\chi(K_4) \le \mu(K_4) + 1$.

Let the number of vertices $n = 4$. We construct a $4 \times 4$ real symmetric matrix $M$ satisfying the adjacency constraints. For every edge $\{i,j\}$, we require $M_{i,j} < 0$. Let all off-diagonal entries be $-1$. To ensure the matrix has exactly one negative eigenvalue, we set the unconstrained diagonal entries to $-1$ as well.

$$
M = \begin{pmatrix}
-1 & -1 & -1 & -1 \\
-1 & -1 & -1 & -1 \\
-1 & -1 & -1 & -1 \\
-1 & -1 & -1 & -1
\end{pmatrix}
$$

Let us verify the three conditions:
1. **Adjacency:** $K_4$ has edges between all distinct pairs of vertices. For all $i \neq j$, $M_{i,j} = -1 < 0$. There are no non-edges. Condition met.
2. **Spectral Signature:** The matrix $M$ is the all-negative-ones matrix ($-J_{4 \times 4}$). The eigenvalues of $M$ are $-4$ (with algebraic multiplicity $1$, corresponding to the all-ones eigenvector $\mathbf{1}$) and $0$ (with algebraic multiplicity $3$). The matrix has exactly one negative eigenvalue. Condition met.
3. **Strong Arnold Property:** Let $X$ be a $4 \times 4$ symmetric matrix such that $M X = 0$, $X_{i,i} = 0$, and $X_{i,j} = 0$ for all edges $\{i,j\}$. Because $K_4$ is a complete graph, $\{i,j\} \in E$ for all $i \neq j$. Therefore, every single entry of $X$ is constrained to be $0$ either by the diagonal rule or the edge rule. Thus $X$ is trivially the zero matrix $\mathbf{0}$. The SAP holds.

The Colin de Verdière parameter $\mu(K_4)$ is the maximum corank of any such matrix $M$. The corank of our matrix $M$ is the algebraic multiplicity of the eigenvalue $0$, which is $3$. Therefore, $\mu(K_4) \ge 3$. (Using advanced properties, it is proven that $\mu(K_n) = n-1$, so $\mu(K_4) = 3$).

Now we verify the conjecture. The chromatic number of $K_4$ is exactly $4$, since every vertex is connected to every other vertex and requires a distinct color.
$$ \chi(K_4) = 4 $$
$$ \mu(K_4) + 1 = 3 + 1 = 4 $$
Substituting these into the conjecture yields:
$$ 4 \le 4 $$
The conjecture holds perfectly. This worked instance highlights how the matrix $M$ translates the maximum dense subgraph into a high-dimensional kernel while maintaining transversality.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*