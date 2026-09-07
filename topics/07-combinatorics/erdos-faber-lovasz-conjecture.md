---
id: 07-combinatorics/erdos-faber-lovasz-conjecture
title: "Erdős-Faber-Lovász Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Faber-Lovász Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-faber-lovasz-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Erdős, Faber, Lovász, 1972).** Let $G_1,\dots,G_n$ be $n$ complete graphs, each on exactly $n$ vertices, such that any two of them share at most one vertex. Then the union
$$G \;=\; \bigcup_{i=1}^{n} G_i$$
has chromatic number $\chi(G) = n$.

The lower bound $\chi(G)\ge n$ is immediate ($G$ contains $K_n$). The content is the upper bound $\chi(G)\le n$: the $n$ cliques can be properly coloured with only $n$ colours, no matter how their $\binom{n}{2}$ possible one-vertex overlaps are arranged.

Equivalent hypergraph formulation: if $\mathcal{H}$ is a **linear** hypergraph (any two edges meet in at most one vertex) with $n$ edges, each of size at most $n$, then the chromatic index satisfies $\chi'(\mathcal{H}) \le n$, i.e. the edges can be partitioned into $n$ intersecting-free classes (matchings).

A complete resolution requires a proof valid for **every** $n$, or a counterexample: a configuration of $n$ pairwise-nearly-disjoint $K_n$'s whose union needs $n+1$ colours. **Status:** Kang, Kelly, Kühn, Methuku and Osthus proved the conjecture for all sufficiently large $n$ (*Annals of Mathematics*, 2023); the statement for small and moderate $n$ below their unspecified threshold $n_0$ remains formally unverified.

## 2. Mathematical Foundations

**Hypergraphs.** $\mathcal{H}=(V,E)$ with $E\subseteq 2^V$. $\mathcal{H}$ is *linear* (or *nearly disjoint*) if $|e\cap f|\le 1$ for all distinct $e,f\in E$; it is *$k$-uniform* if $|e|=k$ for all $e$. The *degree* $d(v)=|\{e\in E: v\in e\}|$, and $\Delta(\mathcal{H})=\max_v d(v)$.

**Chromatic index.** $\chi'(\mathcal{H})$ is the least $t$ with a map $c:E\to[t]$ such that $c(e)=c(f)\Rightarrow e\cap f=\emptyset$. Equivalently $\chi'(\mathcal{H})=\chi(L(\mathcal{H}))$ where $L(\mathcal{H})$ is the line graph. Trivially $\chi'(\mathcal{H})\ge\Delta(\mathcal{H})$.

**Duality.** Given cliques $G_1,\dots,G_n$ on vertex sets $V_1,\dots,V_n$, form the dual hypergraph $\mathcal{H}^*$ whose vertices are the indices $\{1,\dots,n\}$ and whose edges are $e_v=\{i: v\in V_i\}$ for each $v\in\bigcup V_i$. Near-disjointness of the cliques makes $\mathcal{H}^*$ linear with $\Delta(\mathcal{H}^*)\le n$; a proper vertex colouring of $G$ is exactly a proper edge colouring of $\mathcal{H}^*$. So EFL asserts
$$\chi'(\mathcal{H}) \;=\; \Delta(\mathcal{H}) \quad\text{whenever } \mathcal{H} \text{ is linear with } \Delta(\mathcal{H})=n \text{ and } |e|\le n .$$

**Fractional relaxation.** The fractional chromatic index $\chi'_f(\mathcal{H})$ is the LP value $\min\sum_M y_M$ over matchings $M$ with $\sum_{M\ni e}y_M\ge1$. Kahn and Seymour proved $\chi'_f(\mathcal{H})\le n$ in the EFL setting, so the gap the conjecture must close is purely integrality.

**Extremal configurations.** Tightness comes from projective planes: for $q$ a prime power, $PG(2,q)$ has $n=q^2+q+1$ points and $n$ lines, each line a $(q+1)$-clique, any two lines meeting in one point. Padding each line to size $n$ gives $\chi = n$ exactly. Near-pencils (one line of $n-1$ points plus $n-1$ lines through a common point) are the other classical tight family.

**Local structure.** Write $\Gamma(e)=\{f\in E: f\cap e\neq\emptyset\}$. In a linear hypergraph with $|e|\le n$ and $\Delta\le n$, $|\Gamma(e)|\le n(n-1)$, so greedy colouring gives only $\chi'\le n^2-n+1$; the whole difficulty is compressing $\Theta(n^2)$ to $n$.

## 3. History & State of the Art (SOTA)

- **1972.** Posed by Paul Erdős, Vance Faber and László Lovász at a party in Boulder, Colorado. Erdős repeatedly called it one of his three favourite combinatorial problems and eventually offered \$500 for a solution.
- **1972–1980s.** Erdős publicised the problem in his problem collections; early work established only quadratic or linear-with-large-constant bounds.
- **1978–1981.** Seymour proved that every EFL hypergraph contains an edge meeting many others in a controlled way; Hindman verified small cases computationally.
- **1988.** Chang and Lawler gave the clean bound $\chi(G)\le \lceil 3n/2\rceil - 2$ by a short greedy/counting argument.
- **1992.** Kahn's breakthrough: $\chi(G)\le n+o(n)$, via the Rödl nibble (semi-random method) plus concentration inequalities. This asymptotically settled the conjecture up to a lower-order term.
- **1992.** Kahn and Seymour proved the fractional version exactly: $\chi'_f\le n$.
- **2007.** Romero and Sánchez-Arroyo surveyed the state of the art and confirmed the conjecture for further structured families.
- **2019.** Faber and Harris proved the conjecture for dense regular uniform hypergraphs, and Faber formulated the "regular uniform" reduction: it suffices to treat $n$-uniform, $n$-regular linear hypergraphs on $n$ vertices with $n$ edges plus small perturbations.
- **2021 (announced) / 2023 (published).** **Dong Yeap Kang, Tom Kelly, Daniela Kühn, Abhishek Methuku, Deryk Osthus**, *A proof of the Erdős–Faber–Lovász conjecture*, *Annals of Mathematics* **198** (2023), 537–618: the conjecture holds for all sufficiently large $n$. The proof combines the nibble, iterative absorption, and a partition of edges by size into "large", "medium" and "small" regimes handled by different mechanisms.

## 4. Partial Results / Verified Cases

| Result | Statement | Source |
|---|---|---|
| Greedy | $\chi(G)\le n^2-n+1$ | folklore |
| Chang–Lawler | $\chi(G)\le \lceil 3n/2\rceil-2$ | Chang–Lawler 1988 |
| Kahn | $\chi(G)\le n+o(n)$ | Kahn 1992 |
| Fractional | $\chi'_f(\mathcal{H})\le n$ exactly | Kahn–Seymour 1992 |
| Large $n$ | $\chi(G)=n$ for all $n\ge n_0$ | Kang–Kelly–Kühn–Methuku–Osthus 2023 |

Additional verified classes:

- **Small $n$:** verified by hand/computer for $n\le 10$ (Hindman, 1981), and for further small values by later exhaustive searches over linear hypergraphs.
- **Uniform cases:** all $G_i$ meeting pairwise in exactly one vertex (the "sunflower"/projective-plane-like case) — colouring follows from a matching argument (Hall's theorem on the dual).
- **Dense regular uniform hypergraphs:** Faber and Harris (2019) proved $\chi'=\Delta$ for $k$-uniform $d$-regular linear hypergraphs when $k$ is large relative to the number of vertices.
- **Bounded intersection patterns:** if the "intersection graph" of the cliques has bounded degree, or if no vertex lies in more than $2$ cliques, the union is a graph of small clique-degeneracy and $\chi\le n$ follows greedily.
- **Linear hypergraphs of bounded codegree / girth $\ge 5$:** Vizing-type and Pippenger–Spencer results give $\chi'\le(1+o(1))\Delta$, matching EFL asymptotically.
- **List version (Faber's strengthening):** proved asymptotically, $\chi'_\ell(\mathcal{H})\le(1+o(1))n$, by Kang–Kelly–Kühn–Methuku–Osthus in companion work.

## 5. Principal Obstacles

- **No integrality slack.** The conjecture asks for the *exact* value $n$, not $n+O(1)$. Nibble/random-greedy methods inherently leave $o(n)$ uncoloured edges; converting "$n+o(n)$" to "$n$" requires absorbing every leftover edge with zero surplus colours. Standard probabilistic arguments have error terms that cannot be driven to zero.
- **Extremal rigidity.** Projective planes and near-pencils are tight, so any proof must be sensitive enough to certify $n$ rather than $n+1$ on those configurations while still handling all $2^{\Theta(n^2)}$ non-extremal ones. Purely local (degree/greedy) arguments cannot distinguish them.
- **Heterogeneous edge sizes.** Edges may have any size from $1$ to $n$. Large edges are few (at most $n$ of them) and behave like a near-perfect design; small edges are numerous and low-degree. No single random process handles both: nibble arguments need near-regularity, absorption needs structured reservoirs.
- **Failure of Vizing-type inductions.** For graphs, Vizing's theorem gives $\chi'\le\Delta+1$ by Kempe-chain recolouring. Hypergraph Kempe chains are not well defined once edges have size $\ge3$: swapping two colours along an alternating structure can create new conflicts, so the classical recolouring toolkit collapses.
- **LP–IP gap resists rounding.** Kahn–Seymour give a fractional colouring of value exactly $n$; but rounding a fractional edge colouring to an integral one generically costs $\Omega(\log \Delta)$ colours (as in fractional-vs-integral chromatic number), and there is no rounding scheme known that is lossless in general.

## 6. The Gap

Two gaps remain after 2023.

1. **The threshold $n_0$.** The Annals proof is asymptotic: it works for $n$ sufficiently large, with $n_0$ never made explicit and, given the layered nibble + iterative absorption + regularity-style concentration, astronomically large. Between the computationally verified range (roughly $n\le 12$) and $n_0$ lies an unbounded, unverified band. Closing it needs either (a) an explicit and modest $n_0$ extracted by careful bookkeeping through every concentration inequality, or (b) a genuinely different finite-case argument. This is the only obstacle to calling EFL *solved*, not *solved for large $n$*.
2. **Strengthenings still open.** Faber's list-colouring conjecture — $\chi'_\ell(\mathcal{H})=n$ exactly, not $(1+o(1))n$ — is open; so is the conjecture that for linear hypergraphs with $\Delta=n$ and unbounded edge sizes the same bound holds under weaker linearity (e.g. $|e\cap f|\le 2$, where the truth is unknown even asymptotically).

## 7. Current Research (as of June 2026)

- **Birmingham school (Kühn, Osthus) and collaborators (Kang, Kelly, Methuku).** Continued development of iterative absorption as a general tool for exact hypergraph colouring and decomposition results; the EFL proof is now a template applied to Latin-square completion and design existence problems. *(frontier — verify)*
- **Explicit thresholds.** Efforts to extract a concrete $n_0$ from the Annals argument, and to combine it with SAT/ILP verification for moderate $n$. No published explicit bound as of mid-2026. *(frontier — verify)*
- **List and online variants.** Work on $\chi'_\ell$ for linear hypergraphs, including online/greedy versions and correspondence (DP) colouring analogues.
- **Local versions.** Refinements replacing the global bound $\Delta\le n$ by a "local EFL": colouring each edge $e$ with a palette of size $\max_{v\in e} d(v)$, proved asymptotically in the Kang et al. framework.
- **Design theory interface.** Understanding which linear hypergraphs actually attain $\chi'=\Delta$ with no slack; classification of extremal examples beyond projective planes and near-pencils.

## 8. Future Work

- Extract an explicit, verifiable $n_0$; even $n_0 = 10^{100}$ would convert the result to "conditionally finite" and focus computation.
- Find a proof for all $n$ that avoids the nibble entirely — e.g. an entropy-compression / algorithmic Lovász Local Lemma argument, or a polynomial-method certificate for $\chi\le n$.
- Prove Faber's exact list version $\chi'_\ell=n$ using the absorption machinery with list-sensitive reservoirs.
- Determine the truth for $|e\cap f|\le t$ with $t\ge2$: is $\chi'\le C_t \cdot \Delta$ with $C_t\to1$?
- Develop a hypergraph Kempe-chain theory strong enough to give Vizing-type recolouring for linear hypergraphs.

## 9. Key References

- **[Foundational]** P. Erdős. *Problems and results in graph theory and combinatorial analysis.* In: Proceedings of the Fifth British Combinatorial Conference (Aberdeen, 1975), Congressus Numerantium XV, Utilitas Math., 1976, pp. 169–192.
- **[Foundational]** P. Erdős. *On the combinatorial problems which I would most like to see solved.* Combinatorica **1** (1981), 25–42.
- **[Bound]** G. J. Chang, E. L. Lawler. *Edge coloring of hypergraphs and a conjecture of Erdős, Faber, Lovász.* Combinatorica **8** (1988), 293–295.
- **[Breakthrough]** J. Kahn. *Coloring nearly-disjoint hypergraphs with $n+o(n)$ colors.* Journal of Combinatorial Theory, Series A **59** (1992), 31–39.
- **[Fractional]** J. Kahn, P. D. Seymour. *A fractional version of the Erdős–Faber–Lovász conjecture.* Combinatorica **12** (1992), 155–160.
- **[SOTA / Recent]** D. Y. Kang, T. Kelly, D. Kühn, A. Methuku, D. Osthus. *A proof of the Erdős–Faber–Lovász conjecture.* Annals of Mathematics **198** (2023), no. 2, 537–618.
- **[Recent]** V. Faber, D. G. Harris. *Edge-coloring linear hypergraphs with medium-sized edges.* Random Structures & Algorithms **55** (2019), 153–159.
- **[Survey]** D. Romero, A. Sánchez-Arroyo. *Advances on the Erdős–Faber–Lovász conjecture.* In: Combinatorics, Complexity and Chance (G. Grimmett, C. McDiarmid, eds.), Oxford University Press, 2007, pp. 285–298.
- **[Survey]** D. Y. Kang, T. Kelly, D. Kühn, A. Methuku, D. Osthus. *Graph and hypergraph colouring via nibble methods: a survey.* Proceedings of the 8th European Congress of Mathematics, EMS Press, 2023.

## 10. Worked Example / Concrete Special Case

**Case $n=3$.** Take three triangles ($K_3$'s), pairwise sharing at most one vertex, arranged in the maximally-overlapping (near-pencil-free) way:
$$V_1=\{1,2,3\},\quad V_2=\{3,4,5\},\quad V_3=\{5,6,1\}.$$
Each pair shares exactly one vertex ($V_1\cap V_2=\{3\}$, $V_2\cap V_3=\{5\}$, $V_3\cap V_1=\{1\}$), so the configuration is admissible. The union $G$ has $6$ vertices and edge set
$$\{12,23,13\}\cup\{34,45,35\}\cup\{56,61,51\},$$
i.e. the $6$-cycle $1\text{–}2\text{–}3\text{–}4\text{–}5\text{–}6\text{–}1$ plus the "inner triangle" chords $13,35,51$.

*Lower bound.* Vertices $1,3,5$ are pairwise adjacent, so $\chi(G)\ge 3$.

*Upper bound.* Colour $c(1)=a$, $c(3)=b$, $c(5)=c$. Vertex $2$ is adjacent only to $1,3$, so give it $c(2)=c$. Vertex $4$ is adjacent only to $3,5$: set $c(4)=a$. Vertex $6$ is adjacent only to $5,1$: set $c(6)=b$. Checking each clique: $V_1\mapsto\{a,c,b\}$, $V_2\mapsto\{b,a,c\}$, $V_3\mapsto\{c,b,a\}$ — all rainbow. Hence $\chi(G)=3=n$. ✔

*Dual view.* The dual hypergraph $\mathcal{H}^*$ has vertex set $\{1,2,3\}$ (one per clique) and edges $e_1=\{1,3\}$, $e_2=\{1\}$, $e_3=\{1,2\}$, $e_4=\{2\}$, $e_5=\{2,3\}$, $e_6=\{3\}$. It is linear with $\Delta=3$, and the colouring above is the edge colouring $e_1,e_4\mapsto a$; $e_3,e_6\mapsto b$; $e_2,e_5\mapsto c$ — three matchings, so $\chi'(\mathcal{H}^*)=3=\Delta$.

*Why the general case is hard.* Here $n=3$ leaves each vertex with at most $2\cdot(n-1)=4$ coloured neighbours out of $n=3$ colours, and greedy alone would need $5$. Success depended on choosing the order and reusing colours across cliques globally. For general $n$ a vertex can have up to $n(n-1)$ neighbours competing for $n$ colours — a factor-$n$ deficit that no local rule resolves, which is exactly why the Kang–Kelly–Kühn–Methuku–Osthus proof needs a global random-plus-absorption scheme.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*