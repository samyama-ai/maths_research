---
id: 07-combinatorics/burning-number-conjecture
title: "Burning Number Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Burning Number Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/burning-number-conjecture` · **Status:** partially-solved (asymptotic form proved; exact form open)

## 1. Problem Statement / Conjecture

Graph burning is a discrete round-based model of contagion. Let $G$ be a finite simple **connected** graph on $n$ vertices. In round $1$ a player chooses a vertex $x_1$ and sets it on fire. In each subsequent round $i \ge 2$, first every vertex adjacent to a burnt vertex becomes burnt, then the player chooses a new *source* $x_i$ and burns it. The process ends when every vertex is burnt. The **burning number** $b(G)$ is the least number of rounds needed.

**Conjecture (Bonato–Janssen–Roshanbin, 2014).** For every connected graph $G$ on $n$ vertices,
$$b(G) \;\le\; \lceil \sqrt{n}\,\rceil .$$

The bound is tight: $b(P_n) = b(C_n) = \lceil\sqrt n\rceil$ for the path and cycle. A complete resolution requires either a proof valid for *all* $n$ and all connected $G$, or a single connected counterexample $G$ with $b(G) \ge \lceil\sqrt n\rceil + 1$. Connectivity is essential — the disjoint union of $n/2$ edges has burning number $n/2$.

## 2. Mathematical Foundations

Write $N_r[v] = \{u \in V(G) : d(u,v) \le r\}$ for the closed ball of radius $r$ in the graph metric $d$.

**Covering characterisation.** $b(G) \le k$ if and only if there is a sequence $(x_1,\dots,x_k)$ of vertices, called a *burning sequence*, with
$$\bigcup_{i=1}^{k} N_{k-i}[x_i] \;=\; V(G).$$
Source $x_i$ has been burning for $k-i$ rounds at termination, so it covers a ball of radius $k-i$. Thus $b(G)$ is the minimum $k$ for which $G$ admits a cover by balls of radii $k-1, k-2, \dots, 1, 0$. Equivalently it is a *distance-domination* problem with a prescribed, decreasing radius profile.

**Elementary consequences.**
- A ball of radius $r$ in a graph of maximum degree $\Delta \ge 3$ has at most $1 + \Delta\frac{(\Delta-1)^r - 1}{\Delta-2}$ vertices; in a path it has at most $2r+1$ vertices. Counting over the profile gives, for $G = P_n$,
$$n \;\le\; \sum_{i=0}^{k-1}(2i+1) \;=\; k^2 \quad\Longrightarrow\quad b(P_n) \ge \lceil\sqrt n\rceil,$$
and an explicit sequence attains it, so $b(P_n)=\lceil\sqrt n\rceil$.
- $b(G) \le \operatorname{rad}(G) + 1$, since a single centre burns $G$ in $\operatorname{rad}(G)+1$ rounds.
- **Spanning-tree reduction.** If $H$ is a spanning subgraph of $G$ then $b(G) \le b(H)$, because distances only shrink in $G$. Hence
$$b(G) \;=\; \min\{\,b(T) : T \text{ a spanning tree of } G\,\},$$
and the conjecture for all connected graphs is equivalent to the conjecture for all **trees**.
- $b(G) \le \lceil \sqrt n \rceil$ holds trivially for every graph containing a Hamiltonian path, since such a graph has $P_n$ as a spanning subgraph.

**Complexity.** Deciding $b(G) \le k$ is NP-complete, even for trees of maximum degree three, spider graphs, and disjoint unions of paths (Bessy–Bonato–Janssen–Rautenbach–Roshanbin, 2017).

## 3. History & State of the Art (SOTA)

The parameter was introduced by Anthony Bonato, Jeannette Janssen and Elham Roshanbin at WAW 2014 ("Burning a graph as a model of social contagion"), with the journal version *How to burn a graph* (Internet Mathematics, 2016). There they proved the general bound
$$b(G) \le 2\lceil\sqrt n\rceil - 1,$$
verified $b(P_n)=\lceil\sqrt n\rceil$, and posed the conjecture.

Progress on the leading constant $c$ in $b(G) \le c\sqrt n\,(1+o(1))$:

| Year | Authors | Bound | $c$ |
|---|---|---|---|
| 2016 | Bonato–Janssen–Roshanbin | $2\lceil\sqrt n\rceil-1$ | $2$ |
| 2016 | Land–Lu | $\frac{\sqrt6}{2}\sqrt n$ | $1.2247$ |
| 2023 | Bastide–Bonamy–Bonato–Charbit–Kamali–Pierron–Rabie | $\lceil\sqrt{4n/3}\rceil+1$ | $1.1547$ |
| 2024 | Norin–Turcotte | $(1+o(1))\sqrt n$ | $1$ |

Norin and Turcotte (*The burning number conjecture holds asymptotically*, J. Combin. Theory Ser. B 168, 2024) settled the asymptotic form: for every $\varepsilon>0$ there is $n_0$ such that every connected graph on $n \ge n_0$ vertices satisfies $b(G) \le (1+\varepsilon)\sqrt n$. Their argument works on trees, splitting into a "many long paths" case handled by a path-forest packing and a "bushy" case where balls grow fast, and uses a careful iterative decomposition rather than a single global counting bound.

Alongside the extremal question, an algorithmic literature developed: a $3$-approximation for general graphs and a $2$-approximation for trees (Bonato–Kamali, 2019), FPT algorithms in structural parameters (Kare–Reddy, 2019), and heuristics based on farthest-first traversal (García-Díaz et al., 2022).

## 4. Partial Results / Verified Cases

The conjecture $b(G)\le\lceil\sqrt n\rceil$ is **proved** in the following settings.

- **Paths and cycles:** $b(P_n)=b(C_n)=\lceil\sqrt n\rceil$ (Bonato–Janssen–Roshanbin, 2016) — the extremal cases.
- **Any graph with a Hamiltonian path**, by the spanning-subgraph monotonicity above. This covers hypercubes $Q_d$, complete graphs, complete bipartite $K_{m,m}$, and $m\times n$ grids.
- **Spiders** (trees with exactly one vertex of degree $\ge 3$): $b \le \lceil\sqrt n\rceil$ (Bonato–Lidbetter, 2019; sharp characterisation by Tan–Teh, 2020).
- **Path forests** (disjoint unions of paths, in the natural forest version of the problem): tight bounds by Tan and Teh (Appl. Math. Comput. 385, 2020), completing partial results of Bonato–Lidbetter.
- **Double spiders and caterpillars:** subsequent work of Tan and Teh extends the tight bounds to trees with two branch vertices and to caterpillar-like families.
- **Small radius:** if $\operatorname{rad}(G)\le r$ then $b(G)\le r+1$, so the conjecture holds whenever $n \ge r^2 + 2r + 1$, i.e. $n \ge (r+1)^2$. In particular every graph of diameter $2$ on $n \ge 9$ vertices satisfies $b(G)\le 3\le\lceil\sqrt n\rceil$.
- **Dense and random graphs:** for $G(n,p)$ with $p$ constant, $b(G)=2$ or $3$ asymptotically almost surely (Mitsche–Prałat–Roshanbin, 2017); graph products are treated in Mitsche–Prałat–Roshanbin (2018).
- **All large $n$ up to $(1+\varepsilon)$:** the Norin–Turcotte theorem, i.e. the conjecture holds up to a multiplicative $1+o(1)$ factor.
- **Small orders:** exhaustive computation confirms the bound for all connected graphs of small order (all $n \le 10$ are routinely checkable by brute force over burning sequences of length $\le \lceil\sqrt n\rceil$).

## 5. Principal Obstacles

- **Counting is exactly tight, with no slack.** The radius profile $k-1,\dots,0$ covers at most $\sum_{i<k}(2i+1)=k^2$ vertices in a path. So on the extremal family, every ball must be *perfectly packed*. Any argument that loses even a constant factor in ball sizes — which every straightforward greedy or LP-rounding argument does — yields $c>1$ and cannot reach $\lceil\sqrt n\rceil$.
- **Overlap control.** The natural strategy places sources along long paths, but in a tree with many branch vertices the balls overlap in ways that depend on the global metric. Bounding overlaps by local structure (degrees, girth) is what forces the constants $\sqrt{6}/2$ and $\sqrt{4/3}$.
- **No exchange/uncrossing tool.** Unlike matchings or flows, burning sequences have no known local-exchange lemma turning an arbitrary optimal sequence into a canonical one, so induction on subtrees does not compose: an optimal burning of a subtree can force a bad radius profile on the rest.
- **NP-hardness on trees** rules out a clean structural characterisation of $b(T)$; any proof must be an existence argument, not an algorithmic one.
- **The $o(1)$ in the asymptotic theorem is not effective enough.** Norin–Turcotte give $(1+\varepsilon)\sqrt n$ for $n \ge n_0(\varepsilon)$, but $\varepsilon\sqrt n$ dwarfs the additive gap $\lceil\sqrt n\rceil-\sqrt n < 1$ that the conjecture allows. Driving $\varepsilon$ to zero requires closing a *sub-constant* gap, a regime their decomposition does not reach.

## 6. The Gap

Proven: $b(G)\le(1+o(1))\sqrt n$ for all connected $G$, and $b(G)\le\lceil\sqrt n\rceil$ exactly for spiders, path forests, Hamiltonian-path graphs and small-radius graphs. Conjectured: $b(G)\le\lceil\sqrt n\rceil$ for all $n$ and all connected $G$.

The exact boundary: current methods produce a bound of the form $\sqrt n + f(n)$ with $f(n)\to\infty$ (implicitly $f(n)=\varepsilon\sqrt n$), while the conjecture demands $f(n) < 1$. Two distinct sub-gaps remain:

1. **Asymptotic-to-exact.** Show $b(G)\le\sqrt n + O(1)$, then $b(G)\le\lceil\sqrt n\rceil$ for all $n \ge n_0$. This requires a near-perfect ball-packing argument on trees, with total overlap $O(\sqrt n)$ vertices rather than $\Theta(n)$.
2. **Small cases.** Even granted the large-$n$ statement, verifying all $n < n_0$ is infeasible by brute force because $n_0$ from the current proof is astronomically large and the decision problem is NP-hard.

## 7. Current Research (as of June 2026)

- **Sharpening Norin–Turcotte.** Groups at McGill (Norin, Turcotte) and in the French combinatorics community (Bastide, Bonamy, Pierron, Rabie) are working on making the error term additive, aiming at $b(G)\le\sqrt n+O(1)$ or $\sqrt{n}+O(n^{1/4})$ for trees. *(frontier — verify)*
- **Structural restrictions.** Extensions of the tight results from spiders and double spiders to trees with a bounded number of branch vertices or bounded number of leaves; this is the most active exact-bound direction (Tan, Teh, and coauthors). *(frontier — verify)*
- **Minimum-degree and expansion hypotheses.** Graphs with larger minimum degree or positive expansion have fast-growing balls, and several works establish $b(G) = O(n^{1/3})$-type bounds or the full conjecture under such hypotheses. *(frontier — verify)*
- **Algorithmic and inapproximability side.** Improved approximation ratios for trees and interval graphs, parameterized complexity in treewidth/distance-to-cluster, and hardness of approximation for general graphs (García-Díaz et al.; Kare–Reddy lineage).
- **Variants** attracting attention: burning with multiple sources per round, edge burning, burning in directed and temporal graphs, and the *burning game* between an arsonist and a firefighter.

## 8. Future Work

- Prove a **path-forest packing lemma** with additive loss: every tree on $n$ vertices contains a spanning path forest whose burning cost exceeds $\sqrt n$ by $O(1)$ rather than by a constant factor. Bonato and Lidbetter identified this reduction as the natural route.
- Develop an **exchange argument** for burning sequences enabling induction on branch vertices, so that the spider and double-spider proofs bootstrap to arbitrary trees.
- Establish the conjecture under **min-degree $\ge 3$** or bounded-degree hypotheses, isolating the hard case as trees close to paths.
- Search computationally for counterexamples among trees with $n$ just above a perfect square $k^2$, where the constraint is tightest; a counterexample, if one exists, is most likely at $n = k^2+1$.
- Determine whether the general problem is **fixed-parameter tractable in $b(G)$** — currently open and relevant since the conjecture bounds $b$ by $\lceil\sqrt n\rceil$.

## 9. Key References

- **[Foundational]** Anthony Bonato, Jeannette Janssen, Elham Roshanbin. *How to burn a graph.* Internet Mathematics 12(1–2), 85–100, 2016.
- **[Foundational]** Anthony Bonato, Jeannette Janssen, Elham Roshanbin. *Burning a graph as a model of social contagion.* Proc. WAW 2014, LNCS 8882, Springer, 13–22, 2014.
- **[SOTA / Recent]** Sergey Norin, Jérémie Turcotte. *The burning number conjecture holds asymptotically.* Journal of Combinatorial Theory, Series B 168, 208–227, 2024.
- **[SOTA / Recent]** Paul Bastide, Marthe Bonamy, Anthony Bonato, Pierre Charbit, Shahin Kamali, Théo Pierron, Mikaël Rabie. *Improved pyrotechnics: Closer to the burning number conjecture.* Electronic Journal of Combinatorics 30(4), #P4.2, 2023.
- **[Bound]** Max Land, Linyuan Lu. *An upper bound on the burning number of graphs.* Proc. WAW 2016, LNCS 10088, Springer, 1–8, 2016.
- **[Hardness]** Stéphane Bessy, Anthony Bonato, Jeannette Janssen, Dieter Rautenbach, Elham Roshanbin. *Burning a graph is hard.* Discrete Applied Mathematics 232, 73–87, 2017.
- **[Special classes]** Anthony Bonato, Thomas Lidbetter. *Bounds on the burning numbers of spiders and path-forests.* Theoretical Computer Science 794, 12–19, 2019.
- **[Special classes]** Ta Sheng Tan, Wen Chean Teh. *Graph burning: Tight bounds on the burning numbers of path forests and spiders.* Applied Mathematics and Computation 385, 125447, 2020.
- **[Random / products]** Dieter Mitsche, Paweł Prałat, Elham Roshanbin. *Burning graphs: a probabilistic perspective.* Graphs and Combinatorics 33, 449–471, 2017.
- **[Products]** Dieter Mitsche, Paweł Prałat, Elham Roshanbin. *Burning number of graph products.* Theoretical Computer Science 746, 124–135, 2018.
- **[Algorithms]** Anthony Bonato, Shahin Kamali. *Approximation algorithms for graph burning.* Proc. TAMC 2019, LNCS 11436, Springer, 74–92, 2019.
- **[Algorithms]** Anjeneya Swami Kare, I. Vinod Reddy. *Parameterized algorithms for graph burning problem.* Proc. IWOCA 2019, LNCS 11638, Springer, 304–314, 2019.
- **[Survey]** Anthony Bonato. *A survey of graph burning.* Contributions to Discrete Mathematics 16(1), 185–197, 2021.

## 10. Worked Example / Concrete Special Case

**Claim.** $b(P_9)=3=\lceil\sqrt 9\rceil$, and no shorter sequence exists.

Label the path $v_1 - v_2 - \cdots - v_9$.

*Upper bound.* Take the burning sequence $(x_1,x_2,x_3) = (v_2, v_5, v_8)$ — wait, order matters for radii, so check the cover condition with $k=3$: $x_1$ ends with radius $2$, $x_2$ with radius $1$, $x_3$ with radius $0$. Choose $x_1=v_3$, $x_2=v_7$, $x_3=v_9$:
$$N_2[v_3]=\{v_1,\dots,v_5\},\quad N_1[v_7]=\{v_6,v_7,v_8\},\quad N_0[v_9]=\{v_9\}.$$
The union is $\{v_1,\dots,v_9\}=V$, so $b(P_9)\le 3$. Round by round: R1 burns $v_3$; R2 spreads to $v_2,v_4$ and lights $v_7$; R3 spreads to $v_1,v_5,v_6,v_8$ and lights $v_9$. All nine burnt after round 3.

*Lower bound.* With $k=2$ the radii are $1$ and $0$, covering at most $|N_1[x_1]|+|N_0[x_2]| \le 3+1 = 4 < 9$. So $b(P_9)\ge 3$, giving equality.

*Why this is the extremal shape.* The same count with general $k$ gives $\sum_{i=0}^{k-1}(2i+1)=k^2 \ge n$, so $b(P_n)\ge\lceil\sqrt n\rceil$, and for $n=k^2$ the balls tile $P_n$ exactly with zero overlap: sources at positions $1\cdot? $ — concretely for $n=9$, $k=3$, place radius-$2$, radius-$1$, radius-$0$ balls at $v_3,v_7,v_9$ covering $5+3+1=9$ vertices with no waste.

**Contrast with a tree.** Take the spider $S$ with centre $c$ and three legs of length $3$, so $n=10$ and $\lceil\sqrt{10}\rceil=4$. Burning $c$ first gives radius $3$ at termination if $k=4$, and $N_3[c]=V(S)$, so in fact $b(S)\le \operatorname{rad}(S)+1=4$; a finer check shows $b(S)=4$ since $k=3$ covers at most $|N_2[x_1]|+|N_1[x_2]|+1$, and the largest radius-$2$ ball ($N_2[c]$, size $7$) plus a radius-$1$ ball (size $\le 3$) plus one vertex can cover $10$ only if the three balls are disjoint — but the leaves at distance $3$ from $c$ lie in three different legs, and one radius-$1$ ball plus one vertex reaches at most two of them. Hence $b(S)=4=\lceil\sqrt{10}\rceil$: the conjecture is tight here too, illustrating that branching, not just length, can force the bound.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*