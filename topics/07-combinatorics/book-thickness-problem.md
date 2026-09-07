---
id: 07-combinatorics/book-thickness-problem
title: "Book Thickness of Graphs"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Book Thickness of Graphs

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/book-thickness-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **book embedding** of a graph $G$ places all vertices on a line (the *spine*) and assigns each edge to one of $k$ half-planes (*pages*) bounded by that line, so that two edges on the same page never cross. The **book thickness** (or *pagenumber*, *stacknumber*) $\mathrm{bt}(G)$ is the least $k$ admitting such an embedding.

The problem is a cluster of questions, some settled and some open:

1. **Exact values for natural families.** Determine $\mathrm{bt}(K_{m,n})$, $\mathrm{bt}(Q_d)$ (hypercube), and $\mathrm{bt}$ of random and bounded-degree graphs. All three are open in general.
2. **Minor-closed classes (Blankenship–Oporowski).** Does every proper minor-closed class of graphs have bounded book thickness? Equivalently, is $\mathrm{bt}(G)$ bounded by a function of $t$ for all $K_t$-minor-free $G$?
3. **Beyond-planar classes.** Is the book thickness of $k$-planar graphs bounded by a function of $k$? Known for $k=1$; open for general $k$ with tight constants.
4. **Complexity.** Deciding $\mathrm{bt}(G)\le 2$ is NP-complete; no fixed-parameter or approximation algorithm with a nontrivial guarantee is known for $\mathrm{bt}(G)\le k$, $k \ge 3$.

A complete resolution of (2) means a proof or counterexample to the statement "for every $t$ there is $f(t)$ with $\mathrm{bt}(G)\le f(t)$ whenever $G$ has no $K_t$ minor." The planar case ($t=5$) is settled: the answer is exactly $4$.

## 2. Mathematical Foundations

Let $G=(V,E)$, $|V|=n$, $|E|=m$. A book embedding is a pair $(\prec, \sigma)$ where $\prec$ is a linear order on $V$ and $\sigma: E \to \{1,\dots,k\}$ is a page assignment. Two edges $uv$, $xy$ **conflict** if their endpoints interleave:
$$u \prec x \prec v \prec y \quad\text{(up to relabelling of each edge and swapping the pairs)}.$$
Validity requires $\sigma(e)\ne\sigma(f)$ whenever $e,f$ conflict. Fixing $\prec$, the conflict relation defines the **circle graph** $C_\prec(G)$, and
$$\mathrm{bt}(G) \;=\; \min_{\prec}\ \chi\bigl(C_\prec(G)\bigr).$$

**Euler-type counting bound (Bernhart–Kainen, 1979).** A $k$-page embedding with $n\ge 3$ satisfies
$$m \;\le\; k(n-3) + n, \qquad\text{hence}\qquad \mathrm{bt}(G) \;\ge\; \left\lceil \frac{m-n}{\,n-3\,}\right\rceil .$$
Each page plus the spine path is an outerplanar graph on $n$ vertices ($\le 2n-3$ edges, of which $n-1$ are spine edges), giving $m \le k(n-2)+ (n-1)$ for one-page counts; the sharpened form above follows from the outerplanarity of each page together with the spine cycle.

**Characterisations of small book thickness.**
- $\mathrm{bt}(G)=0 \iff G$ is a union of paths (a *linear forest*).
- $\mathrm{bt}(G)\le 1 \iff G$ is outerplanar.
- $\mathrm{bt}(G)\le 2 \iff G$ is *subhamiltonian planar*, i.e. a subgraph of a planar Hamiltonian graph on the same vertex set.
- $\mathrm{bt}(G)\le 3$ has no known combinatorial characterisation; it does not coincide with any minor-closed or topologically defined class.

**Complete graphs.** $\mathrm{bt}(K_n)=\lceil n/2\rceil$ for $n\ge 4$ (Bernhart–Kainen), so $\mathrm{bt}(G)\le \lceil n/2\rceil$ universally.

**Related parameters.** Book thickness is the *stack number*; the dual notion where each page must be a set of *nested* (rather than non-crossing) edges is the **queue number** $\mathrm{qn}(G)$. Both bound and are bounded by other layout parameters: $\mathrm{bt}(G) \le O(\mathrm{qn}(G)\cdot\ldots)$ relations are subtle — Dujmović–Joret–Micek–Morin–Ueckerdt–Wood (2020) showed planar graphs have $\mathrm{qn}(G)\le 49$, while Dujmović, Eppstein, Hickingbotham, Micek, Morin, Wood and coauthors established that stack number is *not* bounded by queue number (2022).

## 3. History & State of the Art (SOTA)

- **1973–1979.** Ollmann and then Bernhart & Kainen, *The book thickness of a graph* (JCTB 1979), formalise the parameter, prove $\mathrm{bt}(K_n)=\lceil n/2\rceil$, the outerplanar and subhamiltonian characterisations, and the counting bound. Kainen had earlier posed the planar question.
- **1982.** Wigderson proves that recognising subhamiltonian planar graphs is NP-complete, hence deciding $\mathrm{bt}(G)\le 2$ is NP-complete.
- **1987.** Chung, Leighton & Rosenberg, *Embedding graphs in books: a layout problem with applications to VLSI design* (SIAM J. Alg. Disc. Meth.), connect the parameter to VLSI, sorting with stacks, and fault-tolerant processor arrays.
- **1986/1989.** Yannakakis announces (STOC 1986) and publishes (*Embedding planar graphs in four pages*, JCSS 1989) that every planar graph has $\mathrm{bt}\le 4$. Whether $3$ suffices became the central open question for 30+ years.
- **1994.** Malitz proves $\mathrm{bt}(G)=O(\sqrt m)$ and $\mathrm{bt}(G)=O(\sqrt g)$ for Euler genus $g$ — both in *Journal of Algorithms*.
- **2020 (breakthrough).** Bekos, Kaufmann, Klute, Pupyrev, Raftopoulou & Ueckerdt, *Four pages are indeed necessary for planar graphs* (J. Computational Geometry 11(1)), and independently Yannakakis, *Planar graphs that need four pages* (JCTB 145, 2020), exhibit planar graphs with $\mathrm{bt}=4$. **Planar book thickness $=4$ is settled.**
- **2020s.** Focus shifts to minor-closed classes, beyond-planar graphs, and separations between stack and queue number.

## 4. Partial Results / Verified Cases

| Class | Book thickness | Source |
|---|---|---|
| Linear forests / outerplanar | $0$ / $\le 1$ | Bernhart–Kainen 1979 |
| Subhamiltonian planar (incl. planar 4-connected, series–parallel) | $\le 2$ | Bernhart–Kainen 1979 |
| Planar | exactly $4$ (upper: Yannakakis 1989; lower: 2020) | Bekos et al. 2020; Yannakakis 2020 |
| $K_n$ | $\lceil n/2\rceil$, $n\ge 4$ | Bernhart–Kainen 1979 |
| Treewidth $\le k$ | $\le k+1$, tight for $k\ge 3$ | Ganley–Heath 2001; Dujmović–Wood 2007 |
| Euler genus $g$ | $O(\sqrt g)$; toroidal $\le 7$ | Malitz 1994; Endo 1997 |
| $m$ edges (arbitrary $G$) | $O(\sqrt m)$ | Malitz 1994 |
| $1$-planar | $O(1)$ (constant $\le 4$ for optimal $1$-planar) | Bekos–Bruckdorfer–Kaufmann–Raftopoulou and successors |
| $K_{m,n}$, $n$ fixed small | exact values for $n\le 3$ | Muder–Weaver–West 1988 |

For $K_{n,n}$ the counting bound gives $\mathrm{bt}(K_{n,n}) \ge \lceil (n^2-2n)/(2n-3)\rceil \approx n/2$, while Muder, Weaver & West (1988) prove $\mathrm{bt}(K_{n,n}) \le \lceil (n+1)/2\rceil$ and conjecture equality; Enomoto, Nakamigawa & Ota (JCTB 1997) narrowed the lower-order gap but the exact value is still unknown for general $n$. Hypercube: $\mathrm{bt}(Q_d)\le d-1$ with matching values verified only for small $d$.

Computationally: SAT-based and exhaustive solvers have confirmed $\mathrm{bt}\le 3$ for all planar triangulations up to moderate size and produced the minimal $4$-page-requiring planar examples (Bekos et al. used a certified search; the published minimal instance has 156 vertices, later reduced).

## 5. Principal Obstacles

- **Double optimisation.** $\mathrm{bt}$ minimises $\chi$ of a circle graph over $n!$ spine orders. There is no useful relaxation: the inner problem (circle-graph colouring) is itself NP-hard for $\ge 4$ colours (Unger), and the outer problem has no submodular or matroidal structure to exploit.
- **No forbidden-substructure theory.** Book thickness $\le k$ is not minor-closed for $k\ge 3$ (subdividing edges can change it, and page count is not monotone under contraction), so Robertson–Seymour machinery gives no finite obstruction set. This is the main reason lower bounds are so rare.
- **Lower bounds are essentially only counting.** Nearly every published lower bound is the edge-density bound $m\le k(n-3)+n$ or a small refinement. For sparse classes (bounded degree, minor-closed) that bound is vacuous, so proving *any* superconstant lower bound requires genuinely new discharging or entropy arguments. The 2020 planar lower bound needed a bespoke, computer-assisted case analysis over $4$-page assignments of a large gadget — it does not generalise.
- **Probabilistic tools give the wrong regime.** Random-graph and expander arguments produce $\Omega(\sqrt m)$-type bounds for dense graphs but say nothing at bounded degree, where the conflict graph is sparse and colourable greedily under most orders.
- **Product structure gives layouts, not pages.** The planar product-structure theorem $G \subseteq H \boxtimes P \boxtimes K_\ell$ resolved queue number, but stacks lack the "nesting" closure that makes the strong-product argument work; stack number is provably not bounded by queue number, so the transfer fails at a proven barrier, not just a technical one.

## 6. The Gap

Proven: constant bounds for planar ($=4$), bounded genus ($O(\sqrt g)$), bounded treewidth ($\le k+1$), and $1$-planar graphs. Conjectured: a constant for every proper minor-closed class.

The precise missing step is a bound of the form $\mathrm{bt}(G) \le f(t)$ for $K_t$-minor-free $G$. By the graph-minor structure theorem, such $G$ decompose into clique-sums of graphs almost-embeddable in a surface of bounded genus, with bounded apex sets and bounded-width vortices. Each piece is handled: bounded-genus pieces by Malitz, bounded-width vortices by treewidth bounds. What is missing is a **composition lemma**: book thickness is not known to be bounded under clique-sums, apex addition, or vortex insertion, because merging two book embeddings requires reconciling two spine orders, and no known amalgamation uses only $O(1)$ extra pages. Closing the gap means either such a lemma or a family of $K_t$-minor-free graphs with unbounded pagenumber.

## 7. Current Research (as of June 2026)

- **Beyond-planar layouts.** Groups at Würzburg (Kaufmann, Wolff), Tübingen, Perugia (Di Battista, Montecchiani), and Athens (Bekos) study book thickness of $k$-planar, fan-planar, and $k$-quasi-planar graphs. Best known bounds for $k$-planar remain exponential in $k$; whether $O(k)$ pages suffice is open *(frontier — verify)*.
- **Stack vs queue separations.** Following the 2022 proof that stack number is unbounded on graphs of queue number 4 (Dujmović, Eppstein, Hickingbotham, Morin, Wood and coauthors), work continues on which layout parameters *do* bound stack number.
- **Subdivisions.** Every graph admits a $3$-page subdivision with $O(\log n)$ division vertices per edge (Enomoto–Miyauchi); the Blankenship–Oporowski question of whether $\mathrm{bt}(G)$ is bounded by a function of $\mathrm{bt}(G')$ for the single subdivision $G'$ remains a focal point, with recent negative partial evidence *(frontier — verify)*.
- **Exact computation.** SAT/ILP pipelines (Pupyrev; Klute) settle pagenumber for named families — snarks, Kneser and generalised Petersen graphs, Cayley graphs of small groups — feeding conjectures on bounded-degree lower bounds.
- **Bounded degree.** Whether cubic graphs have $\mathrm{bt}\le 2$ in general, and whether any bounded-degree family needs $\omega(1)$ pages, are both actively pursued; the $O(\sqrt m)$ bound is the only general tool.

## 8. Future Work

- Prove a **clique-sum composition lemma**: $\mathrm{bt}(G_1 \oplus_k G_2) \le \max(\mathrm{bt}(G_i)) + h(k)$. This alone would give the minor-closed conjecture together with Malitz's genus bound.
- Develop **non-counting lower-bound techniques** — entropy compression, or a discharging scheme on the circle graph — capable of beating $m \le k(n-3)+n$ on sparse instances.
- Settle $\mathrm{bt}(K_{n,n}) = \lceil (n+1)/2\rceil$ (Muder–Weaver–West conjecture); the remaining gap is lower-order and may yield to a refined interleaving argument.
- Determine whether $\mathrm{bt}(G)\le 3$ is decidable in polynomial time on planar inputs, now that $4$ is known to be necessary — this is the natural algorithmic sequel to the 2020 breakthrough.
- Establish or refute an $O(k)$ bound for $k$-planar graphs.

## 9. Key References

- **[Foundational]** F. Bernhart, P. C. Kainen. *The book thickness of a graph.* Journal of Combinatorial Theory, Series B, 27(3):320–331, 1979.
- **[Foundational]** F. R. K. Chung, F. T. Leighton, A. L. Rosenberg. *Embedding graphs in books: a layout problem with applications to VLSI design.* SIAM Journal on Algebraic and Discrete Methods, 8(1):33–58, 1987.
- **[Foundational]** M. Yannakakis. *Embedding planar graphs in four pages.* Journal of Computer and System Sciences, 38(1):36–67, 1989.
- **[SOTA / Recent]** M. A. Bekos, M. Kaufmann, F. Klute, S. Pupyrev, C. Raftopoulou, T. Ueckerdt. *Four pages are indeed necessary for planar graphs.* Journal of Computational Geometry, 11(1):332–353, 2020.
- **[SOTA / Recent]** M. Yannakakis. *Planar graphs that need four pages.* Journal of Combinatorial Theory, Series B, 145:241–263, 2020.
- **[Classical bound]** S. M. Malitz. *Genus $g$ graphs have pagenumber $O(\sqrt g)$.* Journal of Algorithms, 17(1):85–109, 1994. (Companion: *Graphs with $E$ edges have pagenumber $O(\sqrt E)$*, same volume, 71–84.)
- **[Bipartite]** D. J. Muder, M. L. Weaver, D. B. West. *Pagenumber of complete bipartite graphs.* Journal of Graph Theory, 12(4):469–489, 1988.
- **[Bipartite]** H. Enomoto, T. Nakamigawa, K. Ota. *On the pagenumber of complete bipartite graphs.* Journal of Combinatorial Theory, Series B, 71(1):111–120, 1997.
- **[Treewidth]** J. L. Ganley, L. S. Heath. *The pagenumber of $k$-trees is $O(k)$.* Discrete Applied Mathematics, 109(3):215–221, 2001.
- **[Treewidth]** V. Dujmović, D. R. Wood. *Graph treewidth and geometric thickness parameters.* Discrete & Computational Geometry, 37(4):641–670, 2007.
- **[Survey]** L. S. Heath, S. V. Pemmaraju, A. N. Trenk. *Stack and queue layouts of directed acyclic graphs.* SIAM Journal on Computing, 28(4):1510–1539, 1999.
- **[Survey]** V. Dujmović, D. R. Wood. *On linear layouts of graphs.* Discrete Mathematics and Theoretical Computer Science, 6(2):339–358, 2004.

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathrm{bt}(K_5)=3$.

*Lower bound.* Here $n=5$, $m=10$. The Bernhart–Kainen inequality $m \le k(n-3)+n$ gives $10 \le 2k+5$, so $k \ge 2.5$ and $\mathrm{bt}(K_5)\ge 3$. This holds for every spine order, since the bound is order-independent.

*Upper bound.* Fix the spine order $1 \prec 2 \prec 3 \prec 4 \prec 5$ and close it into the cycle $1\,2\,3\,4\,5$. Split the edges:

- **Cycle edges** $\{12,23,34,45,15\}$: consecutive on the spine (or the wrap-around edge $15$, which spans everything). No two of these interleave, so they all fit on **page 1**.
- **Diagonals** $\{13,24,35,14,25\}$. Compute conflicts. $13$ vs $24$: $1\prec 2\prec 3\prec 4$ interleaves — conflict. $13$ vs $25$: $1\prec2\prec3\prec5$ — conflict. $13$ vs $14$, $13$ vs $35$: share an endpoint, no conflict. Repeating for all pairs, the conflict graph on the five diagonals is the $5$-cycle
$$13 - 24 - 35 - 14 - 25 - 13,$$
the familiar pentagram. Since $\chi(C_5)=3$, three colours are needed and suffice for the diagonals; page 1 is free of conflicts with them only in part, so assign: **page 1** $=\{12,23,34,45,15,\,13\}$ — check $13$ vs cycle edges: $13$ vs $45$ disjoint intervals, $13$ vs $15$ nested, $13$ vs $23,12$ share endpoints, $13$ vs $34$ shares endpoint. No conflict. **Page 2** $=\{24,14\}$ (nested: $1\prec2\prec4\prec4$ — they share vertex $4$, no conflict). **Page 3** $=\{35,25\}$ (share vertex $5$).

All ten edges are placed on three pages with no same-page conflict, so $\mathrm{bt}(K_5)\le 3$, and with the lower bound, $\mathrm{bt}(K_5)=3=\lceil 5/2\rceil$, matching Bernhart–Kainen.

*Why this does not scale.* For $K_5$ the counting bound is tight. For a planar triangulation with $n$ vertices, $m=3n-6$ and the same inequality gives only $k \ge \lceil (2n-6)/(n-3)\rceil = 2$ — useless against the true answer $4$. That collapse is exactly the obstacle described in Section 5: on sparse graphs the only general lower-bound tool says nothing.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*