---
id: 07-combinatorics/conway-99-graph-problem
title: "Conway's 99-Graph Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Conway's 99-Graph Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/conway-99-graph-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Does there exist an undirected simple graph $G$ on $99$ vertices such that

1. every edge lies in exactly one triangle, and
2. every non-adjacent pair of vertices lies in exactly one 4-cycle whose diagonals are that pair (equivalently, has exactly two common neighbours)?

Conway offered US\$1,000 for a construction or a nonexistence proof (one of his "Five \$1,000 Problems", 2014/2017). A complete resolution is either an explicit graph (a $99\times 99$ adjacency matrix, checkable in $O(n^3)$ time) or a proof that no such graph exists.

As shown in §2, conditions (1)–(2) force $G$ to be a strongly regular graph with parameters
$$(n,k,\lambda,\mu) = (99,14,1,2).$$
So the problem is: **does $\mathrm{srg}(99,14,1,2)$ exist?**

## 2. Mathematical Foundations

**Definition.** A graph $G$ on $n$ vertices is *strongly regular* with parameters $(n,k,\lambda,\mu)$ if it is $k$-regular, adjacent vertices have exactly $\lambda$ common neighbours, and non-adjacent distinct vertices have exactly $\mu$ common neighbours. Equivalently, the adjacency matrix $A$ satisfies
$$A^2 = kI + \lambda A + \mu (J - I - A),$$
with $J$ the all-ones matrix.

**Forcing the parameters.** Condition (1) says $\lambda = 1$; condition (2) says $\mu = 2$. Regularity is not assumed but follows: counting from a fixed vertex $u$ of degree $k_u$, standard double counting with $\lambda=1,\mu=2$ forces $k_u$ constant. The standard identity
$$k(k-\lambda-1) = (n-k-1)\mu$$
gives $k(k-2) = 2(n-k-1)$, i.e.
$$n = \tfrac{1}{2}\left(k^{2}+2\right).$$

**Eigenvalues.** The non-principal eigenvalues are the roots of $x^{2}-(\lambda-\mu)x-(k-\mu)=0$, here $x^{2}+x-12=0$, so
$$r = 3,\qquad s = -4 .$$
Multiplicities are
$$f,g=\frac12\left[(n-1)\mp\frac{2k+(n-1)(\lambda-\mu)}{\sqrt{(\lambda-\mu)^2+4(k-\mu)}}\right] = \frac12\left[98 \mp \frac{28-98}{7}\right],$$
giving spectrum
$$14^{1},\quad 3^{54},\quad (-4)^{44},\qquad 1+54+44=99 .$$

**The $\lambda=1,\mu=2$ family.** Rationality requires $4k-7=t^{2}$ for an odd integer $t$, so $k=(t^{2}+7)/4$ and $n=(t^2+7)^2/32$. Integrality of $f,g$ requires $t \mid \bigl(2k-(n-1)\bigr)$; substituting gives $t \mid (t^{2}+7)(t^{2}-9)/32$, hence $t \mid 63$. The five admissible values $t\in\{3,7,9,21,63\}$ yield exactly
$$(9,4,1,2),\ (99,14,1,2),\ (243,22,1,2),\ (6273,112,1,2),\ (494019,994,1,2).$$

**Geometric reformulation.** Since $\lambda=1$, the triangles partition $E(G)$: there are $99\cdot 14/2 = 693$ edges and $99\cdot 7/3 = 231$ triangles, and $231\cdot 3 = 693$. So $G$ is the collinearity graph of a partial linear space with $99$ points and $231$ lines of size $3$, each point on $7$ lines, any two points on at most one line, and any two non-collinear points joined by exactly two "paths of length two". The neighbourhood of every vertex is $7K_2$: $G$ is *locally a perfect matching*.

**Bounds satisfied.** Absolute bound: $n \le f(f+3)/2 = 54\cdot 57/2 = 1539$. Krein conditions hold. Hoffman (ratio) bound on independence: $\alpha(G)\le n(-s)/(k-s)=99\cdot 4/18=22$, hence $\chi(G)\ge 99/22 = 4.5$, so $\chi(G)\ge 5$. Cliques have size $\le 1-k/s = 4.5$, so $\omega(G)=3$.

## 3. History & State of the Art (SOTA)

- The parameter set $(99,14,1,2)$ appears in the earliest feasibility tables for strongly regular graphs compiled in the 1970s–80s (Brouwer–van Lint, 1984); it has survived every general feasibility test since.
- Berlekamp, van Lint and Seidel (1973) constructed $\mathrm{srg}(243,22,1,2)$ as the coset graph of the shortened perfect ternary Golay code, showing the family is not empty beyond the trivial $\mathrm{srg}(9,4,1,2)$ (the $3\times3$ rook's graph, $=$ Paley graph of order $9$). At least one further non-isomorphic $\mathrm{srg}(243,22,1,2)$ is known (Delsarte–Goethals type construction).
- Neumaier (1979) proved that for fixed smallest eigenvalue $-m$, strongly regular graphs are Steiner graphs, Latin-square graphs, conference graphs, or belong to a finite "sporadic" list with $\mu$ bounded. With $m=4$, $(99,14,1,2)$ sits in the sporadic bounded class: finiteness is known, exclusion is not.
- Conway publicised the case $n=99$ with a \$1,000 prize (2014; update 2017), giving it its popular name.
- Automorphism-based attacks: Makhnev and Minakova (2004) analysed possible automorphisms of strongly regular graphs with $\lambda=1,\mu=2$; Behbahani and Lam (2011) applied orbit-matrix methods to strongly regular graphs with non-trivial automorphisms of prime order, further constraining the $(99,14,1,2)$ case. The consensus reading is that any such graph has a very small — probably trivial — automorphism group, which is exactly the regime where classification methods have no leverage.
- No exhaustive computer search has been completed. The status in Brouwer's online parameter tables remains "?".

## 4. Partial Results / Verified Cases

Within the family $\lambda=1$, $\mu=2$ (the only five feasible parameter sets, §2):

| $t$ | Parameters | Status |
|---|---|---|
| 3 | $(9,4,1,2)$ | **Exists**, unique: $K_3\times K_3$ (rook's/Paley graph) |
| 7 | $(99,14,1,2)$ | **Open** — this problem |
| 9 | $(243,22,1,2)$ | **Exists**, $\ge 2$ non-isomorphic (Berlekamp–van Lint–Seidel; ternary Golay coset graph) |
| 21 | $(6273,112,1,2)$ | Open |
| 63 | $(494019,994,1,2)$ | Open |

Verified partial results for $n=99$:

- **All standard feasibility conditions pass**: integrality of multiplicities $(54,44)$, Krein conditions, absolute bound, Neumaier's $\mu$-bound $\mu \le m^{3}(2m-3)=320$.
- **No rank-3 example.** Rank-3 permutation groups are classified using CFSG (Foulser, Kallaher, Liebeck, Liebeck–Saxl); $(99,14,1,2)$ does not occur. Hence no such graph has a rank-3 automorphism group.
- **No Steiner or Latin-square realisation.** $s=-4$ with $\mu=2$ excludes the two infinite Neumaier families outright.
- **Automorphism restrictions.** Prime-order automorphism analyses (Makhnev–Minakova 2004; Behbahani–Lam 2011) eliminate most candidate symmetry types; surviving cases are of very small order. *(exact surviving prime list — verify against original Russian sources)*
- **Local structure is fully determined**: every vertex link is $7K_2$; the graph has $231$ triangles forming a partial Steiner triple system on $99$ points; diameter $2$, girth $3$, and $\alpha \le 22$, $\omega = 3$.

## 5. Principal Obstacles

- **Spectral methods are exhausted.** Every linear-algebraic feasibility test (integrality, Krein, absolute, Neumaier bounds) is passed. Eigenvalue techniques cannot distinguish a feasible parameter set from a realisable one; there is no analogue of the Bruck–Ryser–Chowla theorem in this range.
- **No algebraic scaffolding.** Existing constructions of $\lambda=1,\mu=2$ graphs come from coding theory over $\mathbb{F}_3$ ($9=3^2$, $243=3^5$). But $99=9\cdot 11$ is not a prime power, so coset-graph, quadratic-residue, and generalised-quadrangle constructions have no natural home. The two known members of the family are $3$-power sized; $99$ is the arithmetic outlier.
- **Likely trivial automorphism group.** Group-theoretic search — the workhorse for constructing sporadic strongly regular graphs — requires an assumed symmetry. Since prime-order automorphisms are largely excluded, any example must be found essentially "by hand" among asymmetric graphs, where orbit-matrix reduction gives no compression.
- **Search space size.** A brute-force isomorph-free enumeration of $693$-edge locally-$7K_2$ graphs on $99$ labelled vertices is far beyond current backtracking capacity. Comparable completed refutations — Azarija and Marc's proofs that $\mathrm{srg}(75,32,10,16)$ and $\mathrm{srg}(95,40,12,20)$ do not exist — exploited large $\mu$ and rigid local decompositions to prune; with $\mu = 2$ the constraint propagation is weak and each partial extension branches widely.
- **Sparse counting constraints.** With $\mu=2$, the design-theoretic identities give very little: the associated partial linear space is far from a Steiner triple system, so no divisibility or Fisher-type inequality bites.

## 6. The Gap

Proven: the parameter set is feasible by every known necessary condition; the local structure, spectrum, triangle decomposition, and symmetry restrictions are all pinned down. Unproven: whether the $231$ triangles can be assembled globally.

The gap is precisely the step from *local consistency* to *global realisability*. Concretely: given a partial partial-linear-space on $99$ points with lines of size $3$, seven through each point, no known invariant obstructs completing it so that every non-collinear pair has exactly two connecting paths. Closing the gap requires either
- a new nonexistence certificate — a counting, coding-theoretic, or semidefinite-programming argument sensitive to $n=99$ but not to $n=243$; or
- an exhaustive isomorph-free search with a pruning invariant strong enough to make the $99$-vertex tree finite in practice.

## 7. Current Research (as of June 2026)

- **Exhaustive search with SAT/CP solvers.** Encoding the adjacency matrix as $\binom{99}{2}=4851$ Boolean variables plus $\lambda/\mu$ cardinality constraints, combined with symmetry breaking, is the most actively pursued route; partial runs report no contradiction and no example. *(frontier — verify)*
- **Semidefinite / Lasserre relaxations.** Higher-order Terwilliger-algebra and Lasserre-hierarchy bounds have refuted other borderline parameter sets; applying level-3 or level-4 relaxations to $(99,14,1,2)$ is under investigation at the interface of Delft/Tilburg-style SDP combinatorics. *(frontier — verify)*
- **Algebraic combinatorics groups** at Eindhoven (Brouwer's tables), Ghent (van Maldeghem, incidence geometry), and the Ural school (Makhnev and collaborators, automorphism analysis of srg's) continue to log incremental constraints.
- **Descendants and substructures.** Studying the induced subgraph on the $84$ vertices at distance $2$ from a fixed vertex — a graph on $84$ vertices with strong local regularity — as a smaller certificate target.

## 8. Future Work

- Search for a *sub-configuration obstruction*: a small forbidden local pattern forced by $n=99$ but avoidable at $n=243$; this is the only route likely to yield a human-readable nonexistence proof.
- Extend Neumaier-type classification for $s=-4$, $\mu=2$ to a complete determination of the sporadic list — the family is provably finite, so a full enumeration is in principle achievable.
- Attack the sibling open cases $(6273,112,1,2)$ and $(494019,994,1,2)$; a construction there might reveal an algebraic recipe adaptable to $99$.
- Build a verified, formally checked exhaustive search (Coq/Lean-certified pruning), following the model of formally verified combinatorial nonexistence results.
- Investigate whether $99 = 9\cdot 11$ admits a construction over the ring $\mathbb{Z}_9$ or a $\mathbb{F}_3$-structure twisted by an $11$-fold cover.

## 9. Key References

- **[Foundational]** E. R. Berlekamp, J. H. van Lint, J. J. Seidel. *A strongly regular graph derived from the perfect ternary Golay code.* In: A Survey of Combinatorial Theory (J. N. Srivastava, ed.), North-Holland, 1973, pp. 25–30.
- **[Foundational]** A. Neumaier. *Strongly regular graphs with smallest eigenvalue $-m$.* Archiv der Mathematik 33 (1979), 392–400.
- **[Foundational]** A. E. Brouwer, J. H. van Lint. *Strongly regular graphs and partial geometries.* In: Enumeration and Design (Waterloo, 1982), Academic Press, 1984, pp. 85–122.
- **[Foundational]** A. E. Brouwer, A. M. Cohen, A. Neumaier. *Distance-Regular Graphs.* Springer-Verlag, 1989.
- **[Problem source]** J. H. Conway. *Five \$1,000 Problems (Update 2017).* Online Encyclopedia of Integer Sequences, 2017.
- **[SOTA / Recent]** A. E. Brouwer, H. Van Maldeghem. *Strongly Regular Graphs.* Encyclopedia of Mathematics and its Applications 182, Cambridge University Press, 2022.
- **[SOTA / Recent]** M. Behbahani, C. Lam. *Strongly regular graphs with non-trivial automorphisms.* Discrete Mathematics 311 (2011), 132–144.
- **[SOTA / Recent]** J. Azarija, T. Marc. *There is no (95,40,12,20) strongly regular graph.* Journal of Combinatorial Designs 26 (2018), 127–134.
- **[SOTA / Recent]** A. A. Makhnev, I. M. Minakova. *On automorphisms of strongly regular graphs with $\lambda=1$, $\mu=2$.* Discrete Mathematics and Applications 14 (2004), 201–210.
- **[Related]** H. A. Wilbrink, A. E. Brouwer. *A (57,14,1)-strongly regular graph does not exist.* Indagationes Mathematicae, 1983, 117–121.
- **[Survey]** P. J. Cameron. *Strongly regular graphs.* In: Topics in Algebraic Graph Theory (L. W. Beineke, R. J. Wilson, eds.), Cambridge University Press, 2004.
- **[Tables]** A. E. Brouwer. *Parameters of strongly regular graphs* (online tables), Technische Universiteit Eindhoven, continuously updated.

## 10. Worked Example / Concrete Special Case

**The $n=9$ case, solved in full.** Take $t=3$: $k=(9+7)/4=4$, $n=(16+2)/2=9$. Let the vertices be $\mathbb{Z}_3\times\mathbb{Z}_3$ and join two points if they share a coordinate ($3\times3$ rook's graph).

- Degree: $2+2=4$ ✓.
- $\lambda$: adjacent $(0,0)\sim(0,1)$ share only $(0,2)$, so $\lambda=1$ ✓. The triangles are the $3$ rows and $3$ columns — $6$ triangles covering all $9\cdot4/2=18$ edges, $6\cdot3=18$ ✓.
- $\mu$: non-adjacent $(0,0),(1,1)$ have common neighbours $(0,1)$ and $(1,0)$ — exactly $2$ ✓.
- Spectrum: $r,s$ solve $x^2+x-2=0$, giving $r=1$, $s=-2$; multiplicities $\frac12[8 \mp (8-8)/3] = 4,4$. Spectrum $4^1,1^4,(-2)^4$.

**Why $99$ is the next unresolved rung.** Run the same arithmetic for each admissible $t$:

$$t=3:\ (9,4,1,2)\quad t=5:\ k=8,\ n=33,\ \frac{2k-(n-1)}{t}=\frac{16-32}{5}\notin\mathbb{Z}\ \Rightarrow\ \text{infeasible}$$
$$t=7:\ k=14,\ n=99,\ \frac{28-98}{7}=-10\in\mathbb{Z}\ \Rightarrow\ \text{feasible, spectrum } 14^1 3^{54}(-4)^{44}$$
$$t=9:\ k=22,\ n=243,\ \frac{44-242}{9}=-22 \in\mathbb{Z}\ \Rightarrow\ \text{feasible, and realised by the ternary Golay coset graph}$$

**Local picture at $n=99$.** Fix a vertex $u$. Its $14$ neighbours form $7K_2$: seven disjoint edges $\{a_i,b_i\}$, each giving a triangle $\{u,a_i,b_i\}$. Each $a_i$ has $14-2=12$ neighbours outside $\{u\}\cup N(u)$, so the multiset of edges from $N(u)$ to the $99-15=84$ far vertices has size $14\cdot 12 = 168$. Since $\mu=2$, every far vertex receives exactly $2$ such edges: $84\cdot 2 = 168$ ✓. The count closes perfectly — which is exactly the difficulty. Every local balance equation is satisfiable, and the obstruction, if any, lives only in the global assembly of all $231$ triangles.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*