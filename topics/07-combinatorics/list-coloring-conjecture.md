---
id: 07-combinatorics/list-coloring-conjecture
title: "List Coloring Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# List Coloring Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/list-coloring-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Give every edge $e$ of a multigraph $G$ a private list $L(e)$ of allowed colors. An **$L$-edge-coloring** picks $c(e) \in L(e)$ for each edge so that adjacent edges get different colors. The **list chromatic index** $\chi'_\ell(G)$ is the least $k$ such that $G$ is $L$-edge-colorable for *every* assignment of lists of size $k$.

**Conjecture (List Coloring Conjecture, LCC).** For every (multi)graph $G$,
$$\chi'_\ell(G) = \chi'(G),$$
where $\chi'(G)$ is the ordinary chromatic index.

One inequality is free: taking all lists equal to $\{1,\dots,k\}$ gives $\chi'_\ell(G) \ge \chi'(G)$. The content is $\chi'_\ell(G) \le \chi'(G)$: *no* adversarial choice of lists of size $\chi'(G)$ can defeat the edges. A proof must handle all multigraphs (loops are irrelevant; parallel edges are not); a disproof needs one multigraph and one explicit list assignment of size $\chi'(G)$ with no system of distinct representatives respecting adjacency.

The conjecture is striking because the vertex analogue is false by an unbounded margin: $\chi(K_{m,m}) = 2$ while $\chi_\ell(K_{m,m}) = (1+o(1))\log_2 m$ (Erdős–Rubin–Taylor, 1979). LCC asserts that line graphs are exactly the place where the list gap collapses.

## 2. Mathematical Foundations

**List coloring.** For a graph $H$ and $L: V(H) \to 2^{\mathbb{N}}$, $H$ is *$L$-colorable* if there is $c$ with $c(v) \in L(v)$ and $c(u) \neq c(v)$ for $uv \in E(H)$. Then
$$\chi_\ell(H) = \min\{k : H \text{ is } L\text{-colorable for all } L \text{ with } |L(v)| \ge k\ \forall v\}.$$
The edge version is the vertex version of the line graph: $\chi'_\ell(G) = \chi_\ell(L(G))$, and $\chi'(G) = \chi(L(G))$. LCC is thus: *line graphs of multigraphs are chromatic-choosable*, $\chi_\ell = \chi$.

**Classical edge-coloring bounds.** Vizing–Gupta: for simple $G$, $\Delta \le \chi' \le \Delta+1$; for multigraphs with maximum edge multiplicity $\mu$, $\chi' \le \Delta + \mu$. Shannon: $\chi' \le \lfloor 3\Delta/2 \rfloor$. König: $\chi' = \Delta$ for bipartite multigraphs. Under LCC each bound should hold verbatim for $\chi'_\ell$; even $\chi'_\ell \le \Delta+1$ for simple graphs is **open**.

**Kernel method.** In a digraph $D$, a set $S \subseteq V$ is a *kernel* if $S$ is independent and every $v \notin S$ has an out-neighbor in $S$; $D$ is *kernel-perfect* if every induced subdigraph has a kernel. Bondy–Boppana–Siegel: if $D$ is a kernel-perfect orientation of $H$ and $|L(v)| \ge d^+_D(v)+1$ for all $v$, then $H$ is $L$-colorable. Galvin's proof of the bipartite case orients $L(G)$ using a proper $\Delta$-edge-coloring (a Latin-square structure) so that out-degrees are $\le \Delta-1$ and every induced subdigraph is kernel-perfect via the stable-matching theorem.

**Algebraic method.** The graph polynomial is $f_H(x) = \prod_{uv \in E(H),\, u<v} (x_u - x_v)$. Alon's Combinatorial Nullstellensatz: if the coefficient of $\prod_v x_v^{d_v}$ in $f_H$ is nonzero and $|L(v)| \ge d_v + 1$, then $H$ is $L$-colorable. Alon–Tarsi: if $D$ is an orientation of $H$ with $\mathrm{EE}(D) \neq \mathrm{EO}(D)$ (numbers of even/odd Eulerian spanning subdigraphs), then $\chi_\ell(H) \le \max_v d^+_D(v) + 1$.

**Asymptotic tool.** Kahn's semi-random ("nibble") method plus the Lovász Local Lemma yields $\chi'_\ell(G) = (1+o(1))\Delta(G)$ for simple $G$.

## 3. History & State of the Art (SOTA)

- **1976.** Vizing introduces list coloring (*Vertex colorings with given colors*, Metody Diskret. Analiz 29) and poses the edge conjecture; Erdős–Rubin–Taylor (1979) independently develop choosability and pose the Dinitz problem's ancestor.
- **1979.** Jeff Dinitz asks: given an $n \times n$ array with a list of $n$ symbols per cell, can one always fill it so rows and columns are rainbow? This is LCC for $K_{n,n}$.
- **1985.** Bollobás–Harris prove $\chi'_\ell \le 1.8\Delta$ for large $\Delta$; Bollobás–Hind later push to $7\Delta/4$. Häggkvist popularizes the name "List Coloring Conjecture" and attributes it also to Gupta, Albertson–Collins, and Bollobás–Harris.
- **1992.** Alon–Tarsi's orientation theorem gives the first algebraic handle; it implies every $d$-regular bipartite graph is $d$-edge-choosable.
- **1995.** **Galvin** proves LCC for all bipartite multigraphs: $\chi'_\ell = \Delta$, settling the Dinitz problem.
- **1996.** **Kahn** proves $\chi'_\ell(G) \le (1+o(1))\Delta$ — LCC holds asymptotically.
- **1997.** Borodin–Kostochka–Woodall extend the kernel method to multigraphs (Shannon-type bound $\chi'_\ell \le \lfloor 3\Delta/2 \rfloor$) and settle planar graphs with $\Delta \ge 12$. Häggkvist–Janssen sharpen the error term to $\Delta + O(\Delta^{2/3}\sqrt{\log \Delta})$ and prove $\chi'_\ell(K_n) \le n$.
- **2000.** Molloy–Reed reduce the error to $\Delta + O(\Delta^{1/2}\,\mathrm{polylog}\,\Delta)$.
- **2014.** Schauz proves LCC for $K_{p+1}$, $p$ prime, via the Combinatorial Nullstellensatz.

SOTA in one line: LCC is true asymptotically, true for bipartite multigraphs, true for planar graphs of large degree, and open in every regime where the additive constant matters.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Bipartite multigraphs (all $\Delta$) | $\chi'_\ell = \Delta$ | Galvin 1995 |
| All simple graphs, asymptotically | $\chi'_\ell \le \Delta + O(\Delta^{1/2}\mathrm{polylog}\,\Delta)$ | Kahn 1996; Molloy–Reed 2000 |
| All multigraphs | $\chi'_\ell \le \lfloor 3\Delta/2 \rfloor$ (Shannon-tight) | Borodin–Kostochka–Woodall 1997 |
| Planar, $\Delta \ge 12$ | $\chi'_\ell = \Delta$ | Borodin–Kostochka–Woodall 1997 (after Borodin 1990, $\Delta \ge 14$) |
| Planar, $\Delta \ge 8$ | $\chi'_\ell \le \Delta+1$ | Bonamy 2015 |
| Planar $\Delta$-regular, class 1 | $\chi'_\ell = \Delta$ | Ellingham–Goddyn 1996 |
| $\Delta \le 4$ | $\chi'_\ell \le 5$ (LCC for class-1 $\Delta = 4$ still open) | Juvan–Mohar–Škrekovski 1999 |
| $K_{p+1}$, $p$ prime | $\chi'_\ell = p = \chi'$ | Schauz 2014 |
| $K_n$, all $n$ | $\chi'_\ell \le n$ (tight only for $n$ odd) | Häggkvist–Janssen 1997 |
| Line-perfect multigraphs (no odd cycle of length $\ge 5$ in $L(G)$) | $\chi'_\ell = \chi'$ | Peterson–Woodall 1999 |

Consequence of Ellingham–Goddyn plus the Four Color Theorem: every bridgeless cubic planar graph is $3$-edge-choosable.

## 5. Principal Obstacles

- **The kernel method needs bipartite-like orientations.** Galvin's argument requires an orientation of $L(G)$ with all out-degrees $\le \chi'-1$ that is kernel-perfect. Kernel-perfectness follows from Gale–Shapley stability only because a proper edge coloring of a *bipartite* graph is a Latin square: the "row order" and "column order" agree on every clique of $L(G)$. In a non-bipartite graph the triangle-cliques of $L(G)$ (edges meeting at a vertex of odd multiplicity structure) can be oriented cyclically, and a directed triangle has no kernel. No known orientation scheme repairs this in general.
- **The nibble loses a lower-order term.** Kahn's semi-random method colors a constant fraction of edges per round and controls list sizes with concentration inequalities. The error accumulated over $\Theta(\log \Delta)$ rounds is $\Omega(\sqrt{\Delta})$ — inherent to martingale deviation bounds, not an artifact. LCC needs error $O(1)$, so probabilistic methods cannot reach it even in principle without a fundamentally different, deterministic endgame.
- **Algebraic methods choke on coefficient computation.** Alon–Tarsi requires $\mathrm{EE}(D) \neq \mathrm{EO}(D)$ for a specific orientation of $L(G)$; computing this signed count is $\\#P$-hard in general, and Schauz's success for $K_{p+1}$ depends on a modular miracle (working over $\mathbb{F}_p$, where a determinant identity forces the coefficient to be $\not\equiv 0$). No analogue is known when $\Delta+1$ is composite.
- **Class 1 vs class 2 is itself hard.** Deciding $\chi'(G) \in \{\Delta, \Delta+1\}$ is NP-complete (Holyer 1981). LCC asserts equality with an invariant that is NP-hard to compute, so any proof must be structural rather than case-analytic on the value of $\chi'$.
- **No stability/extremal handle.** For chromatic-choosability results one usually exploits near-extremal structure; line graphs of multigraphs form a rich, non-degenerate family with no known "almost-tight instances only" reduction.

## 6. The Gap

Proven: $\chi'_\ell \le \chi'$ when $G$ is bipartite (all $\Delta$), or when $\Delta$ is large enough relative to structure (planar $\Delta \ge 12$), or asymptotically with an additive $\Theta(\sqrt{\Delta}\,\mathrm{polylog})$ slack. Conjectured: exact equality for every multigraph.

The gap is exactly the **additive lower-order term**. Concretely, three benchmark statements sit strictly between Section 4 and Section 1 and are all open:

1. $\chi'_\ell(G) \le \Delta+1$ for every simple graph (list Vizing).
2. $\chi'_\ell(G) \le \Delta+\mu$ for every multigraph (list Vizing–Gupta).
3. $\chi'_\ell(K_{2n}) = 2n-1$ (list version of a $1$-factorization of the complete graph of even order) — even $K_6$ requires $\chi'_\ell = 5$, unproved by any general method.

Crossing the gap means producing, for an arbitrary $G$ with a fixed proper $\chi'$-edge-coloring, either (i) a kernel-perfect orientation of $L(G)$ with out-degrees $\le \chi'-1$, or (ii) a nonvanishing Alon–Tarsi coefficient, or (iii) a deterministic completion step that absorbs the nibble's $\sqrt{\Delta}$ residue.

## 7. Current Research (as of June 2026)

- **Algebraic/Nullstellensatz school** (Schauz; Cariolaro and collaborators; groups in Ulm, Padua): extending the prime-degree argument for $K_{p+1}$ to $K_{2n}$ and to near-complete graphs. The obstruction is computing permanent-like coefficients modulo composite numbers. *(frontier — verify)* Reported partial extensions to $K_{n}$ for $n$ with a single small prime factor remain preprint-level.
- **Probabilistic/entropy compression school** (Molloy; Reed; Kang, Kelly, Postle and coauthors): refined nibble analyses and "local" versions of LCC, e.g. proving $\chi'_\ell \le \Delta+O(1)$ for graphs of large girth or bounded local density. Postle's group has driven local-list-coloring machinery for Reed-type conjectures; transporting it to edges is active.
- **Sparse/topological classes** (Bonamy, Cohen, Havet and the Bordeaux/Sophia school): discharging proofs lowering the planar threshold; the target is planar $\Delta \ge 9$ with $\chi'_\ell = \Delta$ *(frontier — verify)*, and LCC for graphs of bounded genus or bounded maximum average degree.
- **Total-coloring analogue**: the List Total Coloring Conjecture $\chi''_\ell = \chi''$ is pursued jointly, since the kernel and discharging arguments transfer with an extra color class.
- **Computer-assisted search for counterexamples**: exhaustive checks over small multigraphs and structured list assignments (SAT/ILP encodings) have found none; the smallest untested interesting case remains $K_6$ with adversarial $5$-lists at scale $\binom{15}{\,}$ list families, handled only by symmetry reduction.

## 8. Future Work

- **Find the right orientation.** Häggkvist and Woodall have both suggested that the correct target is a *fractional* or *weighted* kernel condition, replacing kernel-perfectness by a fixed-point/LP-duality statement valid on non-bipartite line graphs.
- **Reduce to $\chi' = \Delta$ multigraphs.** A structural reduction of the class-2 case to the class-1 case, in the spirit of Goldberg–Seymour (now a theorem, Chen–Jing–Zang 2019), would let the fractional chromatic index carry the argument; the list analogue of Goldberg–Seymour is a natural intermediate target.
- **Prove list Vizing.** Even $\chi'_\ell \le \Delta+1$ for simple graphs would be a landmark; a Vizing-fan-recoloring argument that works with lists is the most-attempted route and repeatedly fails because fan recoloring permutes colors globally, which lists forbid.
- **Nullstellensatz coefficient theory.** Develop tools to certify nonvanishing Alon–Tarsi coefficients for line graphs without explicit computation, e.g. via representation theory of $S_n$ acting on $1$-factorizations.

## 9. Key References

- **[Foundational]** V. G. Vizing. *Vertex colorings with given colors* (Russian). Metody Diskret. Analiz. 29 (1976), 3–10.
- **[Foundational]** P. Erdős, A. L. Rubin, H. Taylor. *Choosability in graphs.* Congressus Numerantium 26 (1979), 125–157.
- **[Foundational]** N. Alon, M. Tarsi. *Colorings and orientations of graphs.* Combinatorica 12 (1992), 125–134.
- **[Breakthrough]** F. Galvin. *The list chromatic index of a bipartite multigraph.* Journal of Combinatorial Theory, Series B 63 (1995), 153–158.
- **[Breakthrough]** J. Kahn. *Asymptotically good list-colorings.* Journal of Combinatorial Theory, Series A 73 (1996), 1–59.
- **[SOTA]** O. V. Borodin, A. V. Kostochka, D. R. Woodall. *List edge and list total colourings of multigraphs.* Journal of Combinatorial Theory, Series B 71 (1997), 184–204.
- **[SOTA]** R. Häggkvist, J. Janssen. *New bounds on the list-chromatic index of the complete graph and other simple graphs.* Combinatorics, Probability and Computing 6 (1997), 295–313.
- **[SOTA]** M. Molloy, B. Reed. *Near-optimal list colourings.* Random Structures & Algorithms 17 (2000), 376–402.
- **[SOTA]** U. Schauz. *Proof of the list edge coloring conjecture for complete graphs of prime degree.* Electronic Journal of Combinatorics 21(3) (2014), \#P3.43.
- **[Recent]** M. Bonamy. *Planar graphs with maximum degree $\Delta \ge 8$ are $(\Delta+1)$-edge-choosable.* SIAM Journal on Discrete Mathematics 29(3) (2015), 1735–1763.
- **[Special classes]** M. N. Ellingham, L. Goddyn. *List edge colourings of some 1-factorizable multigraphs.* Combinatorica 16 (1996), 343–352.
- **[Special classes]** M. Juvan, B. Mohar, R. Škrekovski. *Graphs of degree 4 are 5-edge-choosable.* Journal of Graph Theory 32 (1999), 250–264.
- **[Survey]** D. R. Woodall. *List colourings of graphs.* In: Surveys in Combinatorics 2001, LMS Lecture Note Series 288, Cambridge University Press, 269–301.
- **[Book]** T. R. Jensen, B. Toft. *Graph Coloring Problems.* Wiley, 1995 (Problem 12.20).
- **[Book]** M. Molloy, B. Reed. *Graph Colouring and the Probabilistic Method.* Springer, 2002.

## 10. Worked Example / Concrete Special Case

**Dinitz problem, $n = 3$.** Take $K_{3,3}$ with parts $R = \{r_1,r_2,r_3\}$ (rows) and $C = \{c_1,c_2,c_3\}$ (columns); the $9$ edges are the cells of a $3 \times 3$ array. Here $\chi'(K_{3,3}) = \Delta = 3$, so LCC demands $\chi'_\ell = 3$: any $3$-element list per cell admits a filling with all rows and all columns rainbow. Adversarial lists drawn from $\{1,\dots,5\}$:

$$
L=\begin{pmatrix}
\{1,2,3\} & \{1,2,4\} & \{1,3,4\}\\
\{2,3,5\} & \{1,4,5\} & \{2,4,5\}\\
\{1,2,5\} & \{2,3,5\} & \{3,4,5\}
\end{pmatrix}
$$

Greedy row-by-row fails: choosing $1,2,3$ in row 1 and $2,3,5$ forced-ish in row 2 can strand cell $(3,3)$. Galvin's orientation solves it deterministically. Fix the reference Latin square $\sigma(i,j) = i+j \bmod 3 \in \{0,1,2\}$. Orient the line graph $L(K_{3,3})$: for two cells in the same **row**, point from the smaller $\sigma$-value to the larger; for two cells in the same **column**, point from the larger $\sigma$-value to the smaller. Each cell $(i,j)$ then has out-degree
$$d^+(i,j) = \\#\{\text{same-row cells with larger } \sigma\} + \\#\{\text{same-column cells with smaller } \sigma\} = (2-\sigma) + \sigma = 2,$$
since within a row the three $\sigma$-values are exactly $\{0,1,2\}$, and likewise within a column. So $d^+ \equiv 2 = |L| - 1$ everywhere.

Every induced subdigraph is kernel-perfect: an induced sub-array's kernel is obtained by running Gale–Shapley stable matching where rows rank cells by increasing $\sigma$ and columns by decreasing $\sigma$; a stable matching is precisely an independent dominating set in this orientation. By Bondy–Boppana–Siegel, $K_{3,3}$ is $L$-colorable. Executing it on the table above gives

$$
c=\begin{pmatrix}
3 & 2 & 1\\
2 & 5 & 4\\
1 & 3 & 5
\end{pmatrix},
$$
with $c(i,j) \in L(i,j)$ in all nine cells and every row and column rainbow.

**Where the argument dies.** Replace $K_{3,3}$ by $K_4$ (also $\chi' = 3$). The line graph $L(K_4)$ is the octahedron $K_{2,2,2}$, whose triangles correspond to the three edges at a common vertex. There is no "row order/column order" split: any attempt to orient the triangles consistently produces a directed $3$-cycle, which has no kernel, so Galvin's method gives nothing. LCC for $K_4$ is nonetheless true — it is the case $p = 3$ of Schauz's theorem, proved by showing the coefficient of $\prod_e x_e^{2}$ in the graph polynomial of $K_{2,2,2}$ is nonzero modulo $3$. That two unrelated methods are needed for two graphs with the same $\Delta$ and the same $\chi'$ is the honest measure of how far the general conjecture is from reach.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*