---
id: 07-combinatorics/antimagic-labeling-conjecture
title: "Antimagic Labeling Conjecture (Hartsfield–Ringel)"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Antimagic Labeling Conjecture (Hartsfield–Ringel)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/antimagic-labeling-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be a finite simple graph with $m=|E|$ edges. An **antimagic labeling** of $G$ is a bijection $f:E\to\{1,2,\dots,m\}$ such that the induced vertex weights
$$w_f(v)\;=\;\sum_{e\ni v} f(e)$$
are pairwise distinct over all $v\in V$. A graph admitting such a labeling is **antimagic**.

**Conjecture (Hartsfield–Ringel, 1990).** Every connected graph on at least three vertices is antimagic.

Equivalently: the only connected exception is $K_2$. The excluded cases are forced — $K_1$ has no edges and $K_2$ has the single labeling $f(e)=1$, giving both endpoints weight $1$.

A complete resolution requires either (a) a construction or existence proof covering all connected $G\neq K_2$, or (b) an explicit connected counterexample $G$ together with a proof that no bijection $E\to\{1,\dots,m\}$ separates all vertex weights. Note that the conjecture is not monotone in edges: adding edges can destroy a labeling, so no "add edges to a known antimagic subgraph" reduction is available.

## 2. Mathematical Foundations

Fix $G$ with $n=|V|$, $m=|E|$, degree sequence $d(v)$, minimum degree $\delta$, maximum degree $\Delta$.

**Weight range.** For a vertex of degree $d$,
$$\binom{d+1}{2}\;=\;1+2+\cdots+d\;\le\;w_f(v)\;\le\;\sum_{i=0}^{d-1}(m-i)\;=\;dm-\binom{d}{2}.$$
Hence vertices of equal degree $d$ compete for $dm-\binom{d}{2}-\binom{d+1}{2}+1 = d(m-d)+1$ weight values. Counting gives a *necessary* feasibility condition: if $n_d$ vertices have degree $d$, then $n_d \le d(m-d)+1$. For connected graphs this is never violated except at $K_2$ — the conjecture asserts the obvious counting bound is also sufficient.

**Total weight identity.**
$$\sum_{v\in V} w_f(v)\;=\;\sum_{e\in E} 2f(e)\;=\;m(m+1),$$
an invariant independent of $f$, which constrains any prospective weight multiset.

**Relation to magic labelings.** A *magic* labeling demands all $w_f(v)$ equal; antimagic is the exact opposite extremal condition. Both sit inside the general labeling framework surveyed in Gallian's dynamic survey.

**Algebraic tool: Combinatorial Nullstellensatz (Alon, 1999).** Encode a labeling by variables $x_e$ and consider
$$P(x)\;=\;\prod_{\{u,v\}\subseteq V}\Big(\sum_{e\ni u}x_e-\sum_{e\ni v}x_e\Big).$$
An antimagic labeling exists if $P$ is nonzero at some point of $\{1,\dots,m\}^E$ with distinct coordinates. Hefetz's approach bounds $\deg P=\binom{n}{2}$ and extracts a nonvanishing monomial coefficient; the method works when $G$ has strong regular substructure (e.g. a $K_3$-factor).

**Probabilistic/flow tool.** Alon–Kaplan–Lev–Roditty–Yuster split $E$ into a spanning structure plus a random-greedy remainder; distinctness is enforced by pigeonhole on intervals of length $\Theta(m/n)$, which requires $\delta$ large enough that each vertex's weight window is wide.

**Variants.** $(a,b)$-antimagic (labels from an arithmetic progression), *shifted antimagic* (labels $\{k+1,\dots,k+m\}$), *local antimagic* (only adjacent weights must differ), and **antimagic orientations** of digraphs, where $w_f(v)=\sum_{e\ \text{in}} f(e)-\sum_{e\ \text{out}} f(e)$.

## 3. History & State of the Art (SOTA)

- **1990.** Nora Hartsfield and Gerhard Ringel state the conjecture in *Pearls in Graph Theory*, together with the stronger claim that every tree other than $K_2$ is antimagic. They verify paths, cycles, wheels and complete graphs $K_n$, $n\ge 3$.
- **2004.** First general theorem: Alon, Kaplan, Lev, Roditty and Yuster prove every graph on $n$ vertices with $\delta \ge c\log n$ is antimagic, and every graph with $\Delta \ge n-2$ is antimagic. This established the "dense" regime.
- **2005.** Hefetz applies the Combinatorial Nullstellensatz: any graph on $3k$ vertices with a $K_3$-factor is antimagic.
- **2009–2016.** The regular case falls in stages: Cranston (bipartite regular, $k\ge2$), Cranston–Liang–Zhu (odd $k\ge3$), then independently Bérczi–Bernáth–Vizer and Chang–Liang–Pan–Zhu for even $k$. Conclusion: **every regular graph of degree $\ge 2$ is antimagic**.
- **2013.** Yilma extends the large-maximum-degree range to $\Delta \ge n-3$ (with $n\ge9$).
- **2016.** Eccles proves the strongest density result to date: there is an absolute constant $c_0$ such that every graph with average degree at least $c_0$ and no isolated vertex or isolated edge is antimagic. This removes the $\log n$ dependence entirely — the open territory is now exactly the *sparse* regime.

## 4. Partial Results / Verified Cases

Classes proven antimagic:

- **Dense graphs.** $\delta \ge c\log n$ (AKLRY 2004); average degree $\ge c_0$, $c_0$ an absolute constant, with the constant in Eccles' proof astronomically large (Eccles 2016).
- **Large maximum degree.** $\Delta \ge n-2$ (AKLRY 2004); $\Delta \ge n-3$, $n\ge 9$ (Yilma 2013).
- **All $k$-regular graphs, $k\ge 2$** (Cranston 2009; Cranston–Liang–Zhu 2015; Bérczi–Bernáth–Vizer 2015; Chang–Liang–Pan–Zhu 2016). Note $k=1$ is $K_2$, the genuine exception.
- **Complete graphs $K_n$ ($n\ge3$), complete bipartite $K_{p,q}$ except $K_{1,1}$, complete multipartite graphs**, wheels, fans, paths $P_n$ ($n\ge3$), cycles $C_n$.
- **Graphs with a $K_3$-factor** on $3k$ vertices (Hefetz 2005).
- **Cartesian products.** Grids $P_m\square P_n$, prisms $C_m\square K_2$, toroidal grids $C_m\square C_n$ (Wang 2005; Cheng 2007, 2008); $G\square H$ antimagic whenever both factors are regular of degree $\ge1$ and not both $K_2$.
- **Trees, partially.** Every tree with **at most one vertex of degree 2** is antimagic (Kaplan–Lev–Roditty 2009, via zero-sum partitions of abelian groups; a gap in the original argument was repaired by Liang–Wong–Zhu 2014). Caterpillars are antimagic (Lozano–Mora–Seara 2019); spiders (trees with one branch vertex) are antimagic (Shang).
- **Small orders.** Exhaustive search confirms all connected graphs of small order ($n\le 9$ in reported computations) are antimagic; no counterexample has ever been exhibited.

## 5. Principal Obstacles

- **Sparse graphs defeat counting.** Every successful density argument gives each vertex a weight window of width $\Theta(d(v)\cdot m/n)$ and applies pigeonhole/greedy allocation. When $d(v)=1$ or $2$ for most vertices, windows are narrow and heavily overlapping; the union bound in the probabilistic method exceeds 1.
- **Degree-2 vertices are the sharp obstruction in trees.** For a degree-1 vertex the weight is a single label, so leaves are separated automatically by injectivity of $f$. Degree-2 vertices produce weights $f(e)+f(e')$ — sums from a Sidon-type problem. Avoiding coincidences among many such sums requires the label set to behave like a $B_2$ set, which $\{1,\dots,m\}$ emphatically is not.
- **Nullstellensatz degree blow-up.** $\deg P = \binom{n}{2}$ grows quadratically while the label alphabet has size $m$, which is only linear in $n$ for sparse graphs. The Nullstellensatz hypothesis $\deg P < \sum(|S_e|-1)$ fails outright once $m \ll n^2$.
- **No monotonicity, no minimal counterexample.** Antimagicness is not closed under edge addition, edge deletion, subgraphs, or minors. Standard induction and extremal "minimal counterexample" machinery therefore has no handle.
- **No local certificate.** Distinctness of weights is a global constraint on $\binom{n}{2}$ pairs; local repair moves (swapping two labels) change four weights at once and can create new collisions, so local-search arguments do not terminate provably.

## 6. The Gap

Everything proven lives in one of two regimes: (i) **high density** — average degree above an absolute constant $c_0$, or $\Delta$ within 3 of $n$; (ii) **high symmetry** — regularity, $K_3$-factors, product structure, or trees with almost no degree-2 vertices.

The gap is the complement: **connected graphs of bounded average degree that are not regular and lack a rigid symmetric decomposition.** The canonical hard instance is a tree with many degree-2 vertices — e.g. a long subdivided star, or any subdivision of a graph. Here $m=n-1$, the label set is barely larger than the vertex set, and roughly $n$ vertex weights must be pairwise distinct pairwise-sums drawn from $\{1,\dots,n-1\}$.

Concretely, the step to cross: prove that for a tree $T$ with $k$ vertices of degree 2 one can choose the labeling so all $\binom{k}{2}$ pairwise sum-collisions are simultaneously avoided, without any density slack. No current technique produces such a simultaneous avoidance for unbounded $k$.

## 7. Current Research (as of June 2026)

- **Sparse and tree cases.** Groups around Zhu (Zhejiang Normal), Wong (Taiwan), and Spanish combinatorics groups (Lozano, Mora, Seara) push structured tree families — caterpillars, spiders, bounded-diameter trees, trees with bounded number of degree-2 vertices. Extending caterpillar results to *lobsters* and to trees of bounded degree is the active frontier *(frontier — verify)*.
- **Lowering Eccles' constant.** Explicit values of $c_0$ from the 2016 proof are enormous; work on entropy-compression and semi-random ("nibble") allocation aims to bring $c_0$ into single or double digits *(frontier — verify)*.
- **Antimagic orientations.** The Hefetz–Mütze–Schwartz program (every connected graph admits an antimagic orientation) is pursued via flow and Eulerian-orientation arguments; the directed version is often easier because negative contributions widen weight windows.
- **Local and shifted antimagic.** The *local antimagic chromatic number* $\chi_{la}(G)$ has become a substantial subfield, with the Local Antimagic Chromatic Number Conjecture ($\chi_{la}(G)=\chi(G)$ for suitable $G$) generating a steady stream of papers.
- **Computation.** SAT/ILP encodings and constraint solvers are used to certify antimagicness for structured families and to search for counterexamples among sparse graphs; none found.

## 8. Future Work

1. **Settle trees.** A proof for all trees $\neq K_2$ would be the decisive advance; the Hartsfield–Ringel tree conjecture is regarded as morally equivalent in difficulty to the general case.
2. **Bridge to $\delta\ge 2$ or $\delta \ge 3$.** Prove antimagicness for all connected graphs of minimum degree 2 or 3; this would combine with the regular results into a near-complete picture.
3. **Reduce to a spanning-tree-plus-remainder framework.** Every connected graph has a spanning tree; a robust theorem "if $T$ is antimagic and $G\supseteq T$ then $G$ is antimagic under condition $X$" would collapse the general case, but no such $X$ is known.
4. **Sidon-set methods.** Import additive combinatorics: choose the labeling so that degree-2 weights land in a prescribed Sidon-like structure.
5. **Explicit small $c_0$.** Bringing Eccles' constant below, say, 10 would leave only a genuinely sparse residue.
6. **Counterexample search.** Systematic sparse-graph search with symmetry breaking, targeting graphs with many equal-degree vertices of degree 2.

## 9. Key References

- **[Foundational]** N. Hartsfield and G. Ringel. *Pearls in Graph Theory: A Comprehensive Introduction.* Academic Press, 1990 (revised Dover edition, 2003).
- **[Foundational]** N. Alon, G. Kaplan, A. Lev, Y. Roditty, R. Yuster. *Dense graphs are antimagic.* Journal of Graph Theory, 47(4):297–309, 2004.
- **[Foundational]** N. Alon. *Combinatorial Nullstellensatz.* Combinatorics, Probability and Computing, 8(1–2):7–29, 1999.
- **[SOTA / Recent]** T. Eccles. *Graphs of large linear size are antimagic.* Journal of Graph Theory, 81(3):236–261, 2016.
- **[SOTA / Recent]** D. W. Cranston. *Regular bipartite graphs are antimagic.* Journal of Graph Theory, 60(3):173–182, 2009.
- **[SOTA / Recent]** D. W. Cranston, Y.-C. Liang, X. Zhu. *Regular graphs of odd degree are antimagic.* Journal of Graph Theory, 80(1):28–33, 2015.
- **[SOTA / Recent]** K. Bérczi, A. Bernáth, M. Vizer. *Regular graphs are antimagic.* Electronic Journal of Combinatorics, 22(3):\#P3.34, 2015.
- **[SOTA / Recent]** F. Chang, Y.-C. Liang, Z. Pan, X. Zhu. *Antimagic labeling of regular graphs.* Journal of Graph Theory, 82(4):339–349, 2016.
- **[SOTA / Recent]** D. Hefetz. *Anti-magic graphs via the Combinatorial NullStellenSatz.* Journal of Graph Theory, 50(4):263–272, 2005.
- **[SOTA / Recent]** G. Kaplan, A. Lev, Y. Roditty. *On zero-sum partitions and anti-magic trees.* Discrete Mathematics, 309(8):2010–2014, 2009.
- **[SOTA / Recent]** Y.-C. Liang, T.-L. Wong, X. Zhu. *Anti-magic labeling of trees.* Discrete Mathematics, 331:9–14, 2014.
- **[SOTA / Recent]** Z. Yilma. *Antimagic properties of graphs with large maximum degree.* Journal of Graph Theory, 72(4):367–373, 2013.
- **[SOTA / Recent]** D. Hefetz, T. Mütze, J. Schwartz. *On antimagic directed graphs.* Journal of Graph Theory, 64(3):219–232, 2010.
- **[SOTA / Recent]** A. Lozano, M. Mora, C. Seara. *Antimagic labelings of caterpillars.* Applied Mathematics and Computation, 347:734–740, 2019.
- **[Survey]** J. A. Gallian. *A Dynamic Survey of Graph Labeling.* Electronic Journal of Combinatorics, Dynamic Survey DS6 (updated annually).

## 10. Worked Example / Concrete Special Case

**(a) Why $K_2$ fails.** $m=1$, so $f(e)=1$ is forced and $w_f(u)=w_f(v)=1$. Not antimagic.

**(b) The path $P_4$.** Vertices $v_1v_2v_3v_4$, edges $e_1=v_1v_2$, $e_2=v_2v_3$, $e_3=v_3v_4$, labels $\{1,2,3\}$. Weights:
$$w(v_1)=f(e_1),\quad w(v_2)=f(e_1)+f(e_2),\quad w(v_3)=f(e_2)+f(e_3),\quad w(v_4)=f(e_3).$$

| $(f(e_1),f(e_2),f(e_3))$ | $w(v_1),w(v_2),w(v_3),w(v_4)$ | distinct? |
|---|---|---|
| $(1,2,3)$ | $1,3,5,3$ | no ($v_2=v_3$) |
| $(2,1,3)$ | $2,3,4,3$ | no |
| $(2,3,1)$ | $2,5,4,1$ | **yes** |

So $P_4$ is antimagic via $f(e_1)=2,\ f(e_2)=3,\ f(e_3)=1$. Check the invariant: $2+5+4+1=12=m(m+1)=3\cdot4$. ✓

**(c) The two degree-2 vertices are exactly the difficulty.** The leaves $v_1,v_4$ carry single labels, automatically distinct. The only collisions possible are $w(v_2)=w(v_3)$, i.e. $f(e_1)=f(e_3)$ — impossible — or a leaf equalling an internal vertex. In $P_4$ this is easy; in $P_n$ there are $n-2$ interior vertices whose weights are $f(e_{i-1})+f(e_i)$, a sequence of $n-2$ consecutive pairwise sums that must all differ. The standard fix for $P_n$ labels edges alternately from the low and high ends, forcing the interior weights to split into an increasing and a decreasing run.

**(d) The counting bound is tight nowhere but at $K_2$.** For $P_4$: the two degree-1 vertices need $n_1=2 \le 1\cdot(3-1)+1=3$ ✓, the two degree-2 vertices need $n_2=2\le 2\cdot(3-2)+1=3$ ✓. For $K_2$: $n_1=2 > 1\cdot(1-1)+1=1$ ✗ — the unique connected graph where the necessary condition fails. The conjecture is precisely the claim that this single counting failure is the whole story.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*