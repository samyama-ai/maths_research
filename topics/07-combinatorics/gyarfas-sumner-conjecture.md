---
id: 07-combinatorics/gyarfas-sumner-conjecture
title: "Gyárfás-Sumner Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gyárfás–Sumner Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/gyarfas-sumner-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Gyárfás 1975; Sumner 1981).** For every tree $T$ and every integer $k \ge 1$ there exists $N = N(T,k)$ such that every graph $G$ with no induced subgraph isomorphic to $T$ and with no clique $K_k$ satisfies $\chi(G) \le N$.

Equivalently: the class $\mathrm{Forb}(T) = \{G : T \not\le_{\mathrm{ind}} G\}$ is **$\chi$-bounded**.

Constraints and scope:
- "Induced" is essential. Every graph of large girth and large chromatic number (Erdős 1959) contains no *subgraph* $T$ of small tree-depth-like shape only in trivial cases; forbidding $T$ as a subgraph forbids nothing useful, since large-girth graphs have no short cycles but do contain all trees as subgraphs. So subgraph-containment versions are false or vacuous.
- The hypothesis that $T$ is a **forest** is necessary: if $H$ contains a cycle, then graphs of girth $> |V(H)|$ and unbounded chromatic number are $H$-free with clique number $2$. So forests (equivalently, by taking a tree containing a given forest, trees) are the only possible candidates.
- A complete proof must supply, for each tree $T$ and each $k$, a finite bound $N(T,k)$. A disproof requires a fixed tree $T$ and a sequence $(G_n)$ with $\omega(G_n) \le k$ fixed, $T \not\le_{\mathrm{ind}} G_n$, and $\chi(G_n) \to \infty$.

The case $k = 3$ (triangle-free host graphs) is already open in general.

## 2. Mathematical Foundations

Let $G = (V,E)$ be finite, simple, undirected. Write $\chi(G)$ for the chromatic number, $\omega(G)$ for the clique number, $\alpha(G)$ for the independence number.

**$\chi$-boundedness (Gyárfás).** A class $\mathcal{C}$ closed under induced subgraphs is $\chi$-bounded if there is $f : \mathbb{N} \to \mathbb{N}$ with
$$\chi(G) \le f(\omega(G)) \qquad \text{for all } G \in \mathcal{C}.$$
$f$ is a *$\chi$-binding function*. The conjecture asserts $\mathrm{Forb}(T)$ is $\chi$-bounded for every tree $T$.

**Levelling / BFS decomposition.** For $v \in V(G)$ with $G$ connected, set $L_i = \{u : d_G(u,v) = i\}$. Then
$$\chi(G) \le 2 \max_i \chi(G[L_i]),$$
since even and odd levels each induce a graph that is a disjoint union of the $G[L_i]$. This reduces many arguments to graphs of small radius, and is why *radius* of $T$ is the natural induction parameter.

**Radius and centre.** $\mathrm{rad}(T) = \min_{v} \max_{u} d_T(u,v)$. A *star* $K_{1,m}$ has radius $1$; a *broom*, *double star*, and *spider* obtained by attaching paths of length $\le 2$ to a centre have radius $2$.

**Ramsey input.** $R(s,t)$ is the least $n$ with $K_n \to (K_s, \overline{K_t})$. The star case uses: if $\alpha(G[N(v)]) < m$ and $\omega(G) < k$, then $\deg(v) < R(m,k)$.

**Polynomial $\chi$-boundedness.** $\mathcal{C}$ is polynomially $\chi$-bounded if one may take $f(\omega) = O(\omega^c)$. Esperet asked whether every $\chi$-bounded class is polynomially $\chi$-bounded; this is **false** (Briański–Davies–Walczak 2024), so even a proof of Gyárfás–Sumner need not give polynomial bounds.

**Known binding function for paths.** For the path $P_t$ on $t$ vertices, Gyárfás proved
$$\chi(G) \le (t-1)^{\omega(G)-1} \qquad \text{for all } P_t\text{-free } G.$$

## 3. History & State of the Art (SOTA)

- **1975.** Gyárfás poses the question in *On Ramsey covering-numbers* and introduces $\chi$-boundedness as an organising concept.
- **1980.** Gyárfás, Szemerédi and Tuza prove the conjecture for all **triangle-free** host graphs when $T$ has radius $2$.
- **1981.** Sumner independently states the conjecture in *Subtrees of a graph and chromatic number*.
- **1987.** Gyárfás's problem list *Problems from the world surrounding perfect graphs* fixes the modern formulation and the path bound $(t-1)^{\omega-1}$.
- **1994.** Kierstead and Penrice: the conjecture holds for **all trees of radius $\le 2$**, for all $k$. This is still the main general theorem.
- **1997.** Scott proves the **topological relaxation**: for every tree $T$, graphs with no induced *subdivision* of $T$ and bounded clique number have bounded chromatic number.
- **2004.** Kierstead and Zhu extend the result to a family of **radius-3** trees.
- **2014.** Pawlik, Kozik, Krawczyk, Lasoń, Micek, Trotter, Walczak construct triangle-free segment intersection graphs with $\chi \to \infty$, refuting Scott's general conjecture (the topological version for arbitrary graphs $H$) — but not touching the tree case.
- **2019–2023.** Chudnovsky, Scott, Seymour and coauthors push the "Induced subgraphs of graphs with large chromatic number" series into new tree families and, separately, obtain **polynomial or near-polynomial** bounds for specific small trees.
- **2020.** Scott–Seymour survey consolidates the area.

Status: proven for all trees of radius $\le 2$ and specific radius-3 families; open for a general tree of radius $3$, even with $\omega = 2$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $T = K_{1,m}$ (stars, radius 1) | $\chi \le R(m,k)$; max degree bounded | folklore (Ramsey) |
| $T = P_t$ (paths) | $\chi \le (t-1)^{\omega-1}$ | Gyárfás 1987 |
| $T$ of radius $\le 2$, triangle-free hosts | bounded $\chi$ | Gyárfás–Szemerédi–Tuza 1980 |
| **all $T$ with $\mathrm{rad}(T) \le 2$**, all $k$ | bounded $\chi$ | Kierstead–Penrice 1994 |
| a family of radius-3 trees | bounded $\chi$ | Kierstead–Zhu 2004 |
| brooms, double stars, spiders with legs of length $\le 2$ | special cases of radius $\le 2$ | — |
| induced *subdivisions* of any $T$ | bounded $\chi$ | Scott 1997 |
| $T = P_4$ | $\chi = \omega$ (cographs are perfect) | Seinsche 1974 |
| $T = P_5$ | $\chi \le \omega^{\log_2 \omega}$ (near-polynomial) | Scott–Seymour–Spirkl 2023 |
| $T$ a star forest | polynomial binding function | Scott–Seymour–Spirkl 2022 |
| $T$ a double star | polynomial binding function | Scott–Seymour–Spirkl 2023 |
| $T$ any tree, hosts with no $K_{t,t}$ subgraph | bounded degeneracy | Scott–Seymour–Spirkl, "Excluding a biclique and an induced tree" |
| tournament analogue | complete classification of "heroes" | Berger–Choromanski–Chudnovsky–Fox–Loebl–Scott–Seymour–Thomassé 2013 |

The smallest tree for which the conjecture is **open** has radius $3$: e.g. the spider obtained from $K_{1,3}$ by subdividing each edge twice is already outside the reach of the general radius-2 machinery, though some such trees fall under Kierstead–Zhu.

## 5. Principal Obstacles

- **Levelling loses radius.** The BFS reduction $\chi(G) \le 2\max_i \chi(G[L_i])$ moves the problem into a single level, but a level of a graph is not induced-$T$-free in any controlled way. Iterating radius reductions costs one radius unit per step and stalls exactly at radius $3$, where the "centre" of $T$ can no longer be pinned to a single vertex whose neighbourhood carries all the structure.
- **No local-to-global mechanism.** Radius-2 proofs find a vertex $v$ whose neighbourhood $N(v)$ has large chromatic number and then build $T$ inside $N(v) \cup N^2(v)$. For radius $3$ one needs *two* far-apart high-$\chi$ regions joined by a controlled path; existing arguments cannot guarantee that the connecting path is induced and attaches correctly to both ends.
- **Extremal constructions defeat sparsity heuristics.** Kneser graphs, shift graphs, Zykov/Mycielski graphs and the Pawlik et al. segment graphs all have $\omega = 2$ and $\chi \to \infty$ while being locally sparse. Any proof must explain why each such family contains every fixed tree as an induced subgraph — but these families are combinatorially unrelated, so no single structural invariant currently covers them.
- **Regularity and probabilistic tools give the wrong quantifiers.** Szemerédi regularity detects dense bipartite pairs, which yield *non-induced* copies; forbidding induced $T$ is not a density condition, so removal-lemma arguments do not transfer.
- **Bounds cannot be assumed polynomial.** Briański–Davies–Walczak (2024) separate $\chi$-boundedness from polynomial $\chi$-boundedness, ruling out proof strategies that implicitly aim for $f(\omega) = \mathrm{poly}(\omega)$ as a route to the general statement.
- **Subdivision is strictly easier.** Scott's 1997 theorem shows the obstruction is *metric rigidity*: allowing arbitrary edge subdivisions gives enough freedom to route paths. The conjecture asks to fix all path lengths simultaneously, and no known argument controls lengths.

## 6. The Gap

Proven: $\mathrm{rad}(T) \le 2 \Rightarrow \mathrm{Forb}(T)$ is $\chi$-bounded (Kierstead–Penrice), plus specific radius-3 families (Kierstead–Zhu), plus the subdivision-closed version for all $T$ (Scott).

Open: the inductive step
$$\mathrm{rad}(T) = r \ \text{solved} \ \Longrightarrow \ \mathrm{rad}(T) = r+1 \ \text{solved},$$
starting at $r = 2$. Concretely, one needs: given a graph $G$ with $\omega(G) < k$ and $\chi(G)$ large, and a tree $T$ with root $v$ whose branches are subtrees of radius $2$ hanging at distance $1$, locate a vertex $u \in V(G)$ and pairwise non-adjacent, pairwise "far" sets $A_1,\dots,A_d \subseteq N(u)$ each still of large chromatic number, so the branches can be embedded independently. Current techniques produce such sets with unbounded interference between the $A_i$: edges between them create unwanted chords and destroy inducedness. Closing this gap — controlling attachment between many high-$\chi$ neighbourhood pieces — is the single missing step.

## 7. Current Research (as of June 2026)

- **Oxford / Princeton / Warwick school (Scott, Seymour, Chudnovsky, Spirkl).** The "Induced subgraphs of graphs with large chromatic number" and "Polynomial bounds for chromatic number" series continue to isolate tree families and to determine which trees admit polynomial binding functions.
- **Kraków / discrete geometry group (Micek, Walczak, Krawczyk).** Continues to produce triangle-free constructions with large $\chi$ and to test them against candidate trees; their constructions are the primary source of potential counterexamples.
- **Sparse-host reductions.** Proving the conjecture under an added hypothesis (bounded twin-width, bounded VC dimension, no $K_{t,t}$ subgraph) is a growing programme; degeneracy bounds for $K_{t,t}$-free hosts are established. *(frontier — verify)* Extensions to hosts of bounded twin-width are reported but not uniformly refereed.
- **Radius-3 attack.** Several groups target the full radius-3 case as the decisive test; partial announcements for spiders with three legs of length 3 circulate. *(frontier — verify)*
- **Directed and ordered analogues.** The tournament "hero" classification and ordered-graph variants are used as tractable models for what a general proof must look like.

## 8. Future Work

- Prove the radius-$3$ case in full; leading authors regard it as the pivot for a general induction.
- Develop a "many far-apart high-$\chi$ neighbourhoods" lemma with control on cross edges — the missing combinatorial primitive of Section 6.
- Determine the exact set of trees $T$ for which $\mathrm{Forb}(T)$ is *polynomially* $\chi$-bounded; conjecturally these are close to the trees of small "spread".
- Improve the path bound $(t-1)^{\omega-1}$ toward the conjectured polynomial $O_t(\omega^{c})$ for fixed $t$.
- Transfer Scott's subdivision theorem into fixed-length statements by bounding the subdivision multiplicities needed.
- Test candidate counterexamples: verify that Kneser, shift, and segment-intersection families contain every fixed tree as an induced subgraph, ideally by a uniform argument.

## 9. Key References

- **[Foundational]** A. Gyárfás. *On Ramsey covering-numbers.* In: Infinite and Finite Sets (Colloq. Math. Soc. János Bolyai, vol. 10), North-Holland, 1975, pp. 801–816.
- **[Foundational]** D. P. Sumner. *Subtrees of a graph and chromatic number.* In: The Theory and Applications of Graphs (G. Chartrand, ed.), Wiley, 1981, pp. 557–576.
- **[Foundational]** A. Gyárfás. *Problems from the world surrounding perfect graphs.* Zastosowania Matematyki (Applicationes Mathematicae) 19 (1987), 413–441.
- **[Foundational]** A. Gyárfás, E. Szemerédi, Zs. Tuza. *Induced subtrees in graphs of large chromatic number.* Discrete Mathematics 30 (1980), 235–244.
- **[Key partial result]** H. A. Kierstead, S. G. Penrice. *Radius two trees specify $\chi$-bounded classes.* Journal of Graph Theory 18 (1994), 119–129.
- **[Key partial result]** H. A. Kierstead, Y. Zhu. *Radius three trees in graphs with large chromatic number.* SIAM Journal on Discrete Mathematics 17 (2004), 571–581.
- **[Key partial result]** A. D. Scott. *Induced trees in graphs of large chromatic number.* Journal of Graph Theory 24 (1997), 297–311.
- **[SOTA / Recent]** M. Chudnovsky, A. Scott, P. Seymour. *Induced subgraphs of graphs with large chromatic number. XII. Distant stars.* Journal of Graph Theory 92 (2019), 237–254.
- **[SOTA / Recent]** A. Scott, P. Seymour, S. Spirkl. *Polynomial bounds for chromatic number. II. Excluding a star-forest.* Journal of Graph Theory 101 (2022), 318–322.
- **[SOTA / Recent]** A. Scott, P. Seymour, S. Spirkl. *Polynomial bounds for chromatic number. IV. A near-polynomial bound for excluding the five-vertex path.* Combinatorica 43 (2023), 845–852.
- **[SOTA / Recent]** M. Briański, J. Davies, B. Walczak. *Separating polynomial $\chi$-boundedness from $\chi$-boundedness.* Combinatorica 44 (2024), 1–8.
- **[Counterexample context]** A. Pawlik, J. Kozik, T. Krawczyk, M. Lasoń, P. Micek, W. T. Trotter, B. Walczak. *Triangle-free intersection graphs of line segments with large chromatic number.* Journal of Combinatorial Theory, Series B 105 (2014), 6–10.
- **[Directed analogue]** E. Berger, K. Choromanski, M. Chudnovsky, J. Fox, M. Loebl, A. Scott, P. Seymour, S. Thomassé. *Tournaments and colouring.* Journal of Combinatorial Theory, Series B 103 (2013), 1–20.
- **[Survey]** A. Scott, P. Seymour. *A survey of $\chi$-boundedness.* Journal of Graph Theory 95 (2020), 473–504.

## 10. Worked Example / Concrete Special Case

**Case $T = K_{1,3}$ (the claw), $k = 3$ (triangle-free hosts).**

Claim: every triangle-free claw-free graph $G$ satisfies $\chi(G) \le 6$, so $N(K_{1,3},3) \le 6$.

*Step 1 — degree bound by Ramsey.* Take any $v \in V(G)$ and suppose $\deg(v) \ge R(3,3) = 6$. Colour the pairs inside $N(v)$ by adjacency. Since $|N(v)| \ge 6$, $G[N(v)]$ contains either a triangle or an independent set of size $3$.
- A triangle in $N(v)$ gives $K_4 \subseteq G$, contradicting $\omega(G) \le 2$.
- An independent set $\{a,b,c\} \subseteq N(v)$ gives the induced subgraph on $\{v,a,b,c\}$ with edges exactly $va, vb, vc$ — an induced $K_{1,3}$, contradiction.

Hence $\Delta(G) \le 5$.

*Step 2 — greedy colouring.* Any graph with $\Delta \le 5$ is $5$-degenerate, so $\chi(G) \le \Delta + 1 = 6$.

*Step 3 — the truth is smaller.* Triangle-free and claw-free forces $\alpha(G[N(v)]) \le 2$ and $\omega(G[N(v)]) = 1$, so $|N(v)| \le R(3,3)-1 = 5$ is loose: with $\omega = 2$ the neighbourhood is independent, and claw-freeness forces $|N(v)| \le 2$. So $\Delta(G) \le 2$: every connected such $G$ is a path or a cycle, giving $\chi(G) \le 3$, with equality for $G = C_5$ ($\chi(C_5) = 3$, triangle-free, claw-free).

*What this illustrates.* For radius-$1$ trees the extremal function is exact and the proof is one Ramsey application. For $T = P_4$ the answer is also exact ($\chi = \omega$, cographs being perfect). For $T = P_5$ the best known bound is already $\omega^{\log_2 \omega}$, and for a general radius-$3$ tree no finite bound is known at all — the whole difficulty lies in replacing the single vertex $v$ of Step 1 by a *configuration* of far-apart high-chromatic neighbourhoods.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*