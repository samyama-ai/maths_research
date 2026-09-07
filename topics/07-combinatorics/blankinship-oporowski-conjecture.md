---
id: 07-combinatorics/blankinship-oporowski-conjecture
title: "Blankinship-Oporowski Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Blankinship–Oporowski Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/blankinship-oporowski-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture asks whether the *stack-number* (book thickness) of a graph is controlled by the stack-number of its shallow subdivisions.

For a graph $G$ and integer $d \ge 0$, let $G^{(d)}$ denote the $d$-subdivision of $G$: the graph obtained by replacing every edge of $G$ by a path with exactly $d$ internal ("division") vertices. Write $\mathrm{sn}(G)$ for the stack-number.

**Conjecture (Blankinship–Oporowski, 1999).** For all integers $k \ge 1$ and $d \ge 0$ there exists $c = c(k,d)$ such that for every graph $G$,
$$\mathrm{sn}\big(G^{(d)}\big) \le k \;\Longrightarrow\; \mathrm{sn}(G) \le c .$$
The case $d = 1$ is the headline statement: *stack-number is bounded by a function of the stack-number of the $1$-subdivision.*

A proof requires exhibiting such a function $c(k,d)$ (equivalently, a procedure converting a $k$-stack layout of $G^{(d)}$ into a bounded-stack layout of $G$). A disproof requires a family $(G_n)$ with $\mathrm{sn}(G_n^{(d)}) \le k$ for fixed $k,d$ but $\mathrm{sn}(G_n) \to \infty$.

The hypothesis that $d$ is **bounded** is essential: if the number of division vertices per edge may grow with $G$, the statement is false, since every graph has *some* subdivision with stack-number at most $3$ (Atneosen 1968; Bernhart–Kainen 1979).

## 2. Mathematical Foundations

**Stack layouts.** A $k$-*stack layout* of a graph $G = (V,E)$ is a pair $(\prec, \phi)$ where $\prec$ is a linear order on $V$ and $\phi : E \to \{1,\dots,k\}$ assigns each edge a *page*, such that no two edges on a common page *cross*: there are no $v \prec x \prec w \prec y$ with $vw, xy \in E$ and $\phi(vw) = \phi(xy)$. The stack-number is
$$\mathrm{sn}(G) = \min\{k : G \text{ has a } k\text{-stack layout}\}.$$
Equivalently, $\mathrm{sn}(G) \le k$ iff $G$ embeds in a $k$-page book with vertices on the spine and each edge drawn inside one page without crossings.

**Basic classifications** (Bernhart–Kainen 1979):
- $\mathrm{sn}(G) \le 1 \iff G$ is outerplanar;
- $\mathrm{sn}(G) \le 2 \iff G$ is *subhamiltonian planar* (a spanning subgraph of a planar Hamiltonian graph);
- $\mathrm{sn}(G) \le 3$ has **no** known characterization by forbidden substructures, and recognizing $\mathrm{sn}(G)\le 3$ is NP-hard (Chung–Leighton–Rosenberg 1987, via Hamiltonicity of maximal planar graphs, Wigderson).

**Density bound.** For $n \ge 3$, a graph with a $k$-stack layout on $n$ vertices has at most
$$|E| \le n + k(n-3)$$
edges (the spine order supplies $\le n$ "consecutive'' edges; each page is outerplanar relative to that order).

**Extremal values.** $\mathrm{sn}(K_n) = \lceil n/2 \rceil$; planar graphs satisfy $\mathrm{sn} \le 4$ (Yannakakis 1989) and this is tight (Yannakakis 2020; Bekos–Kaufmann–Klute–Pupyrev–Raftopoulou–Ueckerdt 2020); $\mathrm{sn}(G) = O(\sqrt{|E|})$ (Malitz 1994); $k$-trees have $\mathrm{sn} = O(k)$ (Ganley–Heath 2001).

**Subdivision operator.** $G^{(d)}$ has $|V| + d|E|$ vertices and $(d+1)|E|$ edges. Subdivision preserves the topological-minor order: $H$ is a topological minor of $G$ iff $H^{(d)}$-type structures persist, and in particular planarity, outerplanarity and genus are subdivision-invariant. Stack-number is **not** subdivision-invariant: it can only decrease or stay equal in a useful sense, and it drops to $\le 3$ under sufficiently deep subdivision.

## 3. History & State of the Art (SOTA)

- **1968–1979.** Atneosen's thesis establishes that every finite graph embeds in a $3$-book after subdivision; Bernhart and Kainen formalize book thickness and prove the $k \le 2$ characterizations, and observe that unbounded subdivision trivializes the parameter.
- **1989–1999.** Yannakakis proves planar graphs need at most $4$ pages. Enomoto and Miyauchi show every graph embeds in a $3$-page book with $O(m \log n)$ *spine crossings* (equivalently division vertices in total), and Enomoto–Miyauchi–Ota prove matching $\Omega(n\log n)$ lower bounds for $K_n$. This quantifies the trade-off "pages vs. division vertices'' that the conjecture is about.
- **1999.** Blankinship and Oporowski (Louisiana State University), studying book drawings of subdivisions of $K_n$ and $K_{n,n}$, formulate the conjecture in a departmental technical report; it is developed further in Blankinship's 2003 LSU doctoral thesis *Book Embeddings of Graphs*.
- **2004–2005.** Dujmović and Wood, in *Stacks, queues and tracks*, popularize the conjecture, prove the analogous quantitative results for queue and track layouts, and show that every graph $G$ has a $3$-stack subdivision with $O(\log \mathrm{sn}(G))$ division vertices per edge — i.e. logarithmically many division vertices already suffice to reach $3$ pages. This is the sharpest known "converse'' evidence and pins the conjecture's difficulty at the constant-$d$ regime.
- **2022–2024.** Renewed activity on stack-number after Dujmović–Eppstein–Hickingbotham–Micek–Morin–Wood separate stack-number from queue-number (Combinatorica 2022), and Eppstein–Hickingbotham–Merker–Norin–Seweryn–Wood construct $3$-dimensional graph products with unbounded stack-number. Both use subdivision-like and product-like constructions, and both are widely seen as the toolkits most likely to settle the conjecture — in the negative.

The conjecture remains **open for every pair $(k,d)$ with $k \ge 3$ and $d \ge 1$.**

## 4. Partial Results / Verified Cases

- **$k = 1$, all $d$.** $\mathrm{sn}(G^{(d)}) \le 1$ means $G^{(d)}$ is outerplanar. Outerplanarity is characterized by the forbidden *topological* minors $K_4$ and $K_{2,3}$, hence is subdivision-invariant, so $G$ is outerplanar and $\mathrm{sn}(G) = 1$. Thus $c(1,d) = 1$.
- **$k = 2$, all $d$.** $\mathrm{sn}(G^{(d)}) \le 2$ forces $G^{(d)}$ planar, hence $G$ planar, hence $\mathrm{sn}(G) \le 4$ by Yannakakis. Thus $c(2,d) \le 4$, and by the four-page-necessary results this constant cannot be improved below $4$ in general form. This is the only nontrivial confirmed case.
- **Complete and complete bipartite graphs.** Blankinship and Oporowski's original analysis of $d$-subdivisions of $K_n$ and $K_{n,n}$ shows that for each fixed $d$ the stack-number of $K_n^{(d)}$ grows without bound in $n$ — exactly the behaviour the conjecture predicts for the densest graphs *(frontier — verify the exact growth rate; the thesis gives bounds of the form $n^{\Theta(1/(d+1))}$)*.
- **Bounded-degeneracy / bounded-treewidth hosts.** If $G$ belongs to a class where stack-number is already bounded (planar graphs, $k$-trees, bounded-genus graphs via Malitz's $O(\sqrt g)$ bound, proper minor-closed classes via Blankenship–Oporowski-type product structure), the implication holds vacuously; these classes give no information about the general case.
- **Unbounded $d$ is genuinely different.** Every graph has a $3$-stack subdivision (Atneosen), and with only $O(\log \mathrm{sn}(G))$ division vertices per edge (Dujmović–Wood 2005). So any proof must exploit $d = O(1)$ quantitatively, not qualitatively.

## 5. Principal Obstacles

1. **Counting dies immediately.** The density bound gives $(d+1)m \le (n + dm) + k(n+dm-3)$, i.e. $m\,(1 - kd - d\,k) \lesssim (k+1)n$. Already for $d = 1$, $k = 1$ the coefficient of $m$ is non-positive and the inequality is vacuous: subdivision dilutes density below every threshold a $k$-page bound can detect. Every extremal/Turán-style argument that proves lower bounds on $\mathrm{sn}$ (Malitz, Bernhart–Kainen) is therefore useless on $G^{(d)}$.
2. **No structural characterization at $k \ge 3$.** The $k \le 2$ cases were settled purely because $\mathrm{sn} \le 2$ coincides with a *topological* (subdivision-invariant) property. From $k = 3$ onwards, stack-number is not minor-monotone, not topological-minor-monotone, and NP-hard to recognize; there is no forbidden-structure list to transfer from $G^{(d)}$ back to $G$.
3. **Lost adjacency information.** In a stack layout of $G^{(d)}$, an edge $uv$ of $G$ becomes a path whose division vertices may be scattered arbitrarily along the spine and across pages. Recovering a page assignment for $uv$ means contracting a path that may cross the whole layout; no known contraction lemma bounds the resulting crossing structure by a function of $k$ and $d$.
4. **The logarithmic construction is nearly optimal.** Since $O(\log \mathrm{sn})$ division vertices per edge already buy $3$ pages, any proof must show that the gap between $d = O(1)$ and $d = \Theta(\log \mathrm{sn}(G))$ is a genuine complexity jump — a $\log$-sized gap that current lower-bound machinery (spine-crossing counts of order $n \log n$) is too coarse to see.
5. **Successful separations point the other way.** The techniques that recently produced *negative* results (stack-number vs. queue-number; products with unbounded stack-number) rely on probabilistic/Ramsey-type colouring arguments that produce huge graphs with small layouts — precisely the shape of a counterexample.

## 6. The Gap

Proven: $c(k,d)$ exists for $k \le 2$ and every $d$, by transferring a topological property. Conjectured: existence for all $k \ge 3$, $d \ge 1$.

The missing step is a **path-contraction lemma for stack layouts**: given a $k$-stack layout of $G^{(d)}$, produce a vertex order and page assignment of $G$ with $O_{k,d}(1)$ pages. Equivalently, one must show that "$G$ has a $k$-page layout after inserting $d$ break-points per edge'' already implies a bounded-page layout without break-points. No invariant is currently known that (i) is bounded on $k$-stack graphs, (ii) is preserved under contracting subdivided paths, and (iii) bounds stack-number. Conversely, a disproof needs graphs of arbitrarily large stack-number whose $1$-subdivisions embed in a fixed number of pages — for which no candidate family has been verified.

## 7. Current Research (as of June 2026)

- **Monash / Wood's group** (Wood, Hickingbotham, Distel) continue subdivision- and product-structure work; the conjecture appears on Wood's standing open-problem lists and in graph-product-structure surveys.
- **Separation programme** *(frontier — verify)*: attempts to adapt the Combinatorica 2022 stack-vs-queue separation, which builds graphs with small queue-number and large stack-number, to build graphs whose $1$-subdivisions have small stack-number. The obstruction is that the known constructions control queue-number, and no analogous "subdivision-robust'' lower-bound certificate for stack-number is known.
- **Ottawa / Ottawa–Wrocław (Dujmović, Morin, Micek)**: quantitative layouts of subdivisions, spine-crossing lower bounds, and layered/product decompositions.
- **Beyond-planar graphs community** (Bekos, Kaufmann, Pupyrev, Ueckerdt): exact page numbers for structured families, plus SAT-based computation of stack-numbers of small subdivisions — the natural source of a small counterexample if one exists.
- **Computational search** *(frontier — verify)*: no published exhaustive verification of $\mathrm{sn}(G^{(1)}) \le 3 \Rightarrow \mathrm{sn}(G) \le c$ over a nontrivial graph range is available; SAT encodings of book embeddings scale to a few dozen vertices, and $G^{(1)}$ of a graph with $m$ edges has $n+m$ vertices, which caps searches near $n \le 10$.

## 8. Future Work

- Prove the case $k = 3$, $d = 1$: characterize which $3$-page layouts of $1$-subdivisions arise, exploiting that $3$-page graphs have $\le 4n-9$ edges and bounded "local'' structure.
- Find a subdivision-stable lower-bound certificate for stack-number (an analogue of the Enomoto–Miyauchi–Ota spine-crossing count, but sensitive at $d = O(1)$).
- Settle the weaker "bounded-degree'' version: does $\mathrm{sn}(G^{(1)}) \le k$ and $\Delta(G) \le \Delta$ imply $\mathrm{sn}(G) \le c(k,\Delta)$?
- Determine the exact growth of $\mathrm{sn}(K_n^{(d)})$ for fixed $d$; a tight bound would calibrate any general function $c(k,d)$.
- Run SAT/ILP searches over $1$-subdivisions of small graphs with stack-number $\ge 5$, seeking a $3$-page layout — a single hit disproves the conjecture.

## 9. Key References

- **[Foundational]** F. Bernhart and P. C. Kainen. *The book thickness of a graph.* Journal of Combinatorial Theory, Series B, 27(3):320–331, 1979.
- **[Foundational]** G. H. Atneosen. *On the embeddability of compacta in $n$-books: intrinsic and extrinsic properties.* PhD thesis, Michigan State University, 1968.
- **[Origin]** R. Blankinship. *Book Embeddings of Graphs.* PhD thesis, Louisiana State University, 2003. (Advisor: B. Oporowski; conjecture first stated in a 1999 LSU Department of Mathematics technical report with Oporowski on drawing subdivisions of complete and complete bipartite graphs on books.)
- **[SOTA / Survey]** V. Dujmović and D. R. Wood. *Stacks, queues and tracks: layouts of graph subdivisions.* Discrete Mathematics and Theoretical Computer Science, 7:155–202, 2005.
- **[SOTA]** V. Dujmović and D. R. Wood. *On linear layouts of graphs.* Discrete Mathematics and Theoretical Computer Science, 6:339–358, 2004.
- **[SOTA / Recent]** V. Dujmović, D. Eppstein, R. Hickingbotham, P. Micek, P. Morin, D. R. Wood. *Stack-number is not bounded by queue-number.* Combinatorica, 42:151–164, 2022.
- **[SOTA / Recent]** D. Eppstein, R. Hickingbotham, L. Merker, S. Norin, M. T. Seweryn, D. R. Wood. *Three-dimensional graph products with unbounded stack-number.* Discrete & Computational Geometry, 2024.
- **[Foundational]** M. Yannakakis. *Embedding planar graphs in four pages.* Journal of Computer and System Sciences, 38(1):36–67, 1989; and *Planar graphs that need four pages*, Journal of Combinatorial Theory, Series B, 145:241–263, 2020.
- **[SOTA]** M. A. Bekos, M. Kaufmann, F. Klute, S. Pupyrev, C. Raftopoulou, T. Ueckerdt. *Four pages are indeed necessary for planar graphs.* Journal of Computational Geometry, 11(1):332–353, 2020.
- **[Foundational]** H. Enomoto and M. S. Miyauchi. *Embedding graphs into a three page book with $O(m\log n)$ crossings of edges over the spine.* SIAM Journal on Discrete Mathematics, 12(3):337–341, 1999.
- **[Foundational]** H. Enomoto, M. S. Miyauchi, K. Ota. *Lower bounds for the number of edge-crossings over the spine in a topological book embedding of a graph.* Discrete Applied Mathematics, 92(2–3):149–155, 1999.
- **[Related]** S. M. Malitz. *Graphs with $E$ edges have pagenumber $O(\sqrt{E})$.* Journal of Algorithms, 17(1):71–84, 1994.
- **[Related]** J. L. Ganley and L. S. Heath. *The pagenumber of $k$-trees is $O(k)$.* Discrete Applied Mathematics, 109(3):215–221, 2001.

## 10. Worked Example / Concrete Special Case

**Goal: prove $c(2,d) \le 4$ for every $d$, and see exactly where the argument stops at $k = 3$.**

Let $G$ be any graph with $\mathrm{sn}(G^{(d)}) \le 2$.

1. By Bernhart–Kainen, $\mathrm{sn}(H) \le 2$ implies $H$ is planar (indeed subhamiltonian). So $G^{(d)}$ is planar.
2. Planarity is invariant under subdividing and suppressing degree-$2$ vertices (Kuratowski: the forbidden objects $K_5, K_{3,3}$ are forbidden *topological* minors). Suppressing all $d|E(G)|$ division vertices recovers $G$, so $G$ is planar.
3. Yannakakis: every planar graph has a $4$-page book embedding. Hence $\mathrm{sn}(G) \le 4$. $\square$

**Tightness.** Take $G_0$ to be one of the planar graphs of Yannakakis (2020) / Bekos et al. (2020) with $\mathrm{sn}(G_0) = 4$. If $\mathrm{sn}(G_0^{(1)}) \le 2$ — plausible, since subdividing every edge of a planar graph makes it bipartite and greatly relaxes the Hamiltonicity requirement — then the jump $2 \mapsto 4$ is realized and $c(2,1) = 4$ exactly.

**Why counting cannot replace step 2.** Suppose we try to bound $m = |E(G)|$ from $\mathrm{sn}(G^{(1)}) \le 1$ using the density bound $|E| \le N + k(N-3)$ with $N = n + m$, $k = 1$:
$$2m \;\le\; (n+m) + \big((n+m)-3\big) \;=\; 2n + 2m - 3,$$
which reduces to $0 \le 2n - 3$: always true, no information. The same computation for general $k, d$ gives
$$(d+1)m \le (k+1)(n + dm) - 3k \iff m\big[(d+1) - (k+1)d\big] \le (k+1)n - 3k,$$
and the bracket $1 - kd$ is $\le 0$ as soon as $kd \ge 1$. So for every $k \ge 1, d \ge 1$ the inequality is vacuous: $G$ may have arbitrarily many edges relative to $n$ while $G^{(d)}$ stays sparse enough for $k$ pages.

**Where $k = 3$ breaks.** Repeating step 1 with $k = 3$ yields only "$G^{(d)}$ has a $3$-page layout'' — a property with no forbidden-topological-minor characterization, not preserved under suppressing degree-$2$ vertices in any known way. Concretely, $\mathrm{sn}(K_6) = 3$ and $\mathrm{sn}(K_{12}) = 6$; the conjecture demands that $\mathrm{sn}(K_{12}^{(1)})$ be bounded away from $3$ by an absolute rule, yet the only available lower bound for spine crossings ($\Omega(n\log n)$ total for $K_n$, i.e. $O(\log n / n)$ per edge on average) is far too weak to forbid one division vertex per edge. That quantitative gap — $\Theta(1)$ versus $\Theta(\log n)$ division vertices per edge — is the whole content of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*