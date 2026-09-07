---
id: 07-combinatorics/hadwiger-conjecture
title: "Hadwiger Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hadwiger Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hadwiger-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Hadwiger, 1943).** For every integer $t \ge 1$, every graph $G$ with chromatic number $\chi(G) \ge t$ contains $K_t$ as a minor.

Equivalently, in contrapositive form: every $K_t$-minor-free graph is $(t-1)$-colorable. Writing $h(G)$ for the **Hadwiger number** — the largest $t$ such that $K_t$ is a minor of $G$ — the claim is
$$\chi(G) \le h(G) \qquad \text{for every finite simple graph } G.$$

Graphs are finite, simple, undirected. A **proof** requires establishing the implication for all $t$; a **disproof** requires exhibiting a single graph $G$ with $\chi(G) > h(G)$, or a nonconstructive argument that one exists (e.g. a counting argument over random graphs — which is known *not* to work, see §4).

The conjecture is a vast generalization of the Four Color Theorem: the case $t=5$ implies it, and is implied by it.

## 2. Mathematical Foundations

**Minors.** $H$ is a *minor* of $G$, written $H \preceq G$, if $H$ can be obtained from a subgraph of $G$ by contracting edges. Equivalently, there is a **minor model**: a family $\{B_v\}_{v \in V(H)}$ of pairwise disjoint vertex sets $B_v \subseteq V(G)$ (the *branch sets*), each inducing a connected subgraph, such that for every $uv \in E(H)$ there is an edge of $G$ between $B_u$ and $B_v$. Thus $K_t \preceq G$ iff there exist $t$ disjoint connected subgraphs of $G$, pairwise joined by at least one edge.

**Chromatic number.** $\chi(G) = \min\{k : \exists\, c: V(G)\to[k],\ c(u)\neq c(v)\ \forall uv\in E(G)\}$. **Degeneracy** $d(G) = \max_{H \subseteq G} \delta(H)$ satisfies the greedy bound $\chi(G) \le d(G) + 1$.

**Extremal function for minors.** Define
$$c(t) \;=\; \inf\{\,c : e(G) \ge c\,|V(G)| \implies K_t \preceq G \,\}.$$
Any $K_t$-minor-free graph is $\lfloor 2c(t)\rfloor$-degenerate, hence $\chi \le 2c(t)+1$. Mader (1968) proved $c(t) = t-2$ for $t \le 7$, giving the *linear* bound $\chi(G)\le 2(t-2)+1$ in that range and conjecturing linearity in general. This fails:
$$c(t) \;=\; (\alpha + o(1))\, t\sqrt{\log t}, \qquad \alpha = 0.638\ldots$$
(Kostochka 1984 and Thomason 1984 for the order of magnitude; Thomason 2001 for the exact constant, $\alpha = 0.63817\ldots$ defined via an optimization involving $\lambda$ with $\lambda\log\lambda = 1$). The lower bound comes from random graphs $G(n,p)$, which are $K_t$-minor-free yet have average degree $\Theta(t\sqrt{\log t})$.

Hence the **degeneracy barrier**: purely density-based arguments cannot give better than
$$\chi(G) \le O\!\left(t\sqrt{\log t}\right) \quad \text{for } K_t\text{-minor-free } G,$$
a $\sqrt{\log t}$ factor away from Hadwiger's $t-1$.

**Clique-sums.** $G$ is a *$k$-clique-sum* of $G_1,G_2$ if $G = (G_1\cup G_2)$ where $G_1\cap G_2$ is a clique on $\le k$ vertices, with edges of that clique optionally deleted. Coloring is well-behaved: $\chi(G)=\max(\chi(G_1),\chi(G_2))$, and $K_t$-minor-freeness is preserved for $k \le t-1$ in the relevant structure theorems. This is the engine behind all exactly-solved cases.

## 3. History & State of the Art (SOTA)

- **1937.** Wagner characterizes $K_5$-minor-free graphs by a clique-sum decomposition into planar pieces and the Wagner graph $V_8$, and shows Hadwiger's $t=5$ case is *equivalent* to the Four Color Conjecture.
- **1943.** Hadwiger states the conjecture in *Über eine Klassifikation der Streckenkomplexe*, proving $t \le 4$.
- **1952.** Dirac independently proves $t=4$ and characterizes the extremal graphs.
- **1968.** Mader determines $c(t)=t-2$ for $t\le 7$ and conjectures linear extremal growth.
- **1976/1997.** Four Color Theorem (Appel–Haken; Robertson–Sanders–Seymour–Thomas) settles $t=5$.
- **1980.** Bollobás–Catlin–Erdős: the conjecture holds for almost every graph — $h(G(n,1/2)) = (1+o(1))\, n/\sqrt{\log_2 n}$, matching $\chi$ asymptotically.
- **1984.** Kostochka and Thomason independently kill Mader's linear hope: $c(t)=\Theta(t\sqrt{\log t})$. This yields the long-standing bound $\chi \le O(t\sqrt{\log t})$.
- **1993.** Robertson–Seymour–Thomas prove $t=6$ (every $K_6$-minor-free graph is 5-colorable), reducing to the Four Color Theorem via an "apex" structure theorem. This remains the largest case resolved.
- **2019–2023.** Norin–Postle–Song break the degeneracy barrier: $\chi = O(t(\log t)^{\beta})$ for any $\beta > 1/4$.
- **2021–2025.** Delcourt–Postle reduce the linear form of the conjecture to coloring small graphs and obtain $\chi = O(t\log\log t)$ — the current SOTA.

## 4. Partial Results / Verified Cases

| Case / class | Result |
|---|---|
| $t \le 3$ | Trivial ($K_3$-minor-free = forest, 2-colorable) |
| $t = 4$ | Hadwiger 1943, Dirac 1952 — series-parallel structure |
| $t = 5$ | Wagner 1937 + Four Color Theorem 1976 |
| $t = 6$ | Robertson–Seymour–Thomas 1993 (uses 4CT) |
| $t = 7$ | **Open.** Kawarabayashi–Toft 2005: every 7-chromatic graph has a $K_7$ or $K_{4,4}$ minor |
| $t=7,8$ bounds | Albar–Gonçalves 2018: $K_7$-minor-free $\Rightarrow$ 8-colorable; $K_8$-minor-free $\Rightarrow$ 10-colorable |
| General $t$ | $\chi = O(t\log\log t)$ (Delcourt–Postle) |
| Fractional relaxation | $\chi_f(G) \le 2h(G)$ (Reed–Seymour 1998) |
| Random graphs | True for $G(n,1/2)$ a.a.s. (Bollobás–Catlin–Erdős 1980) |
| Line graphs | True (Reed–Seymour 2004); quasi-line graphs (Chudnovsky–Fradkin 2008) |
| Perfect graphs | True (follows from $\chi=\omega$) |
| $\alpha(G)=2$ | $h(G)\ge \lceil n/2\rceil$ needed; proved by Plummer–Stiebitz–Toft 2003 for graphs with no induced $C_4$; Blasiak 2007 for $n$ divisible by 3 |
| Proper minor-closed, bounded genus | True (Euler-formula degeneracy arguments) |
| **List version** | **FALSE** — Barát–Joret–Wood 2011: $K_{3t+2}$-minor-free graphs with list chromatic number $\ge 4t$ |

## 5. Principal Obstacles

- **The degeneracy barrier.** Every classical proof for $K_t$-minor-free graphs proceeds by finding a low-degree vertex and coloring greedily. Kostochka's random-graph construction shows the best possible such bound is $\Theta(t\sqrt{\log t})$, so *no* argument that only sees edge density can reach $t-1$. Breaking it (Norin–Postle–Song) required density-increment arguments that recursively pass to small dense subgraphs — winning only $(\log t)^{1/4}$-type factors, not the full $\sqrt{\log t}$.
- **No structure theorem in the right regime.** The Robertson–Seymour graph minor structure theorem describes $K_t$-minor-free graphs as clique-sums of graphs almost-embeddable in surfaces with apex vertices and vortices. The number of apices is a function $f(t)$ that is astronomically larger than $t$, so each apex costs a color and the bound is useless. The $t\le 6$ proofs work precisely because the structure is *explicit* and apex-count small.
- **Extremal examples are not understood.** Graphs with $\chi(G) = h(G)$ (tight instances) include $C_5[K_t]$-type constructions and are poorly classified. Without knowing the shape of extremal graphs, induction has no target.
- **Failure of local/probabilistic coloring.** Entropy compression and nibble methods need bounded local density or triangle-sparseness; $K_t$-minor-free graphs can contain arbitrarily large cliques of size $t-1$, defeating local arguments.
- **List coloring counterexample.** Barát–Joret–Wood show the natural list-coloring strengthening is false, ruling out the entire toolkit of list-coloring/Combinatorial-Nullstellensatz-style proofs, which have been the source of most modern coloring breakthroughs.

## 6. The Gap

Proven: $\chi(G)\le h(G)$ for $h(G)\le 6$, and $\chi(G) = O(h(G)\log\log h(G))$ in general. Conjectured: $\chi(G)\le h(G)-$nothing, for all $h$.

Two distinct gaps:

1. **The multiplicative gap.** Removing the $\log\log t$ factor would prove **Linear Hadwiger** ($\chi \le Ct$), itself a major open problem. Delcourt–Postle reduce this to: *every $K_t$-minor-free graph on $O(t)$ vertices is $O(t)$-colorable* — a finite-flavored statement per $t$, but still unbounded in $t$.
2. **The constant gap.** Even $\chi \le Ct$ with $C=1.0001$ does not give Hadwiger. The step from linear to *exactly* $t-1$ appears to require a structural characterization of tight examples, of a kind currently available only for $t\le 6$.

The next concrete milestone is $t=7$: proving every $K_7$-minor-free graph is 6-colorable. Kawarabayashi–Toft reduces it to handling graphs with a $K_{4,4}$ minor but no $K_7$ minor; the missing ingredient is a Wagner-type decomposition for $K_7$, which does not exist (Jørgensen's conjecture on 6-connected $K_6$-minor-free graphs — every such graph is apex — is itself open and is a prerequisite-flavored problem).

## 7. Current Research (as of June 2026)

- **Density-increment / small-graph reduction** (Postle, Delcourt, Waterloo/Illinois). The $O(t\log\log t)$ bound of Delcourt–Postle, announced for *J. Amer. Math. Soc.*, is the active frontier; effort is on removing $\log\log t$ entirely. *(frontier — verify publication details)*
- **Norin–Song–Postle school** (McGill, Georgia Tech): refining $K_t$-minor extraction from graphs of average degree slightly above $t$, using rooted-minor and "well-linked set" machinery.
- **Odd Hadwiger** (Gerards–Seymour conjecture: $\chi(G)\le t$ if $G$ has no odd $K_{t+1}$ minor). Steiner and collaborators (ETH Zürich) have pushed bounds to $O(t\log\log t)$ matching the ordinary case *(frontier — verify)*, and proved several relaxations for $\alpha(G)=2$.
- **Independence number 2** (Seymour, Chudnovsky, Bosse): the case $\alpha(G)=2$ reduces to showing every graph on $n$ vertices whose complement is triangle-free has a $K_{\lceil n/2\rceil}$ minor — a Ramsey-flavored statement, partially resolved.
- **Clustered and fractional relaxations** (Wood, Dvořák, Norin): "every $K_t$-minor-free graph is $(t-1)$-colorable with bounded monochromatic components" — proved in strong forms and viewed as evidence.

## 8. Future Work

- Prove **Linear Hadwiger**: $\chi(G)\le Ct$. Seymour identifies this as the realistic next target; it needs a bounded-apex structure theorem or a new density-increment fixed point.
- Settle **$t=7$**, ideally without appealing to a computer-assisted 4CT, and settle **Jørgensen's conjecture** on 6-connected $K_6$-minor-free graphs.
- Classify **tight examples**: graphs with $\chi = h$. A structural classification for $\alpha(G)=2$ would already be a substantial advance.
- Determine whether the conjecture holds for graphs of **bounded independence number** for all fixed $\alpha$, generalizing the $\alpha=2$ programme.
- Explore whether the list-coloring counterexample generalizes to a **counterexample for ordinary coloring at large $t$** — a minority view (raised by Wood and others) that Hadwiger may be false for large $t$.

## 9. Key References

- **[Foundational]** H. Hadwiger. *Über eine Klassifikation der Streckenkomplexe.* Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich **88** (1943), 133–142.
- **[Foundational]** K. Wagner. *Über eine Eigenschaft der ebenen Komplexe.* Mathematische Annalen **114** (1937), 570–590.
- **[Foundational]** G. A. Dirac. *A property of 4-chromatic graphs and some remarks on critical graphs.* Journal of the London Mathematical Society **27** (1952), 85–92.
- **[Foundational]** W. Mader. *Homomorphiesätze für Graphen.* Mathematische Annalen **178** (1968), 154–168.
- **[Milestone]** N. Robertson, P. Seymour, R. Thomas. *Hadwiger's conjecture for $K_6$-free graphs.* Combinatorica **13** (1993), 279–361.
- **[Bounds]** A. V. Kostochka. *Lower bound of the Hadwiger number of graphs by their average degree.* Combinatorica **4** (1984), 307–316.
- **[Bounds]** A. Thomason. *An extremal function for contractions of graphs.* Mathematical Proceedings of the Cambridge Philosophical Society **95** (1984), 261–265.
- **[Bounds]** A. Thomason. *The extremal function for complete minors.* Journal of Combinatorial Theory Series B **81** (2001), 318–338.
- **[SOTA]** S. Norin, L. Postle, Z.-X. Song. *Breaking the degeneracy barrier for coloring graphs with no $K_t$ minor.* Advances in Mathematics **422** (2023), 109020.
- **[SOTA]** M. Delcourt, L. Postle. *Reducing linear Hadwiger's conjecture to coloring small graphs.* arXiv:2108.01633 (2021); Journal of the American Mathematical Society (2025).
- **[Relaxation]** B. Reed, P. Seymour. *Fractional colouring and Hadwiger's conjecture.* Journal of Combinatorial Theory Series B **74** (1998), 147–152.
- **[Negative]** J. Barát, G. Joret, D. R. Wood. *Disproof of the list Hadwiger conjecture.* Electronic Journal of Combinatorics **18** (2011), #P232.
- **[Partial]** K. Kawarabayashi, B. Toft. *Any 7-chromatic graph has $K_7$ or $K_{4,4}$ as a minor.* Combinatorica **25** (2005), 327–353.
- **[Partial]** B. Albar, D. Gonçalves. *On triangles in $K_r$-minor free graphs.* Journal of Graph Theory **88** (2018), 154–173.
- **[Random]** B. Bollobás, P. A. Catlin, P. Erdős. *Hadwiger's conjecture is true for almost every graph.* European Journal of Combinatorics **1** (1980), 195–199.
- **[Survey]** P. Seymour. *Hadwiger's conjecture.* In *Open Problems in Mathematics* (J. F. Nash Jr., M. Th. Rassias, eds.), Springer, 2016, 417–437.
- **[Survey/Book]** T. R. Jensen, B. Toft. *Graph Coloring Problems.* Wiley-Interscience, 1995.

## 10. Worked Example / Concrete Special Case

**(a) The case $t=4$, in full.** Claim: every $K_4$-minor-free graph $G$ satisfies $\chi(G)\le 3$.

Induct on $|V(G)|$. If $G$ is disconnected or has a cut vertex, color each block separately and permute colors to agree on the cut vertex. So assume $G$ is 2-connected with $n\ge 4$. A 2-connected $K_4$-minor-free graph has a 2-vertex cut $\{x,y\}$: otherwise $G$ is 3-connected, and every 3-connected graph on $\ge 4$ vertices contains $K_4$ as a minor (take any vertex $v$ and three internally disjoint paths from $v$ to a vertex $u$, guaranteed by Menger; contract them). Given the cut $\{x,y\}$, write $G = G_1 \cup G_2$ with $V(G_1)\cap V(G_2)=\{x,y\}$. Add the edge $xy$ to each $G_i$ if absent: the resulting $G_i^+$ is still $K_4$-minor-free, because a path through the other side realizes the edge $xy$ as a contraction. By induction each $G_i^+$ is 3-colorable, and in each coloring $x,y$ get *distinct* colors (they are adjacent). Permute colors of $G_2^+$ to match $G_1^+$ on $\{x,y\}$; the union is a proper 3-coloring of $G$. $\square$

Sharpness: $K_3$ has $\chi = h = 3$. Any series-parallel graph, e.g. the "ladder" $K_4$ minus an edge, has $h=3$ and $\chi=3$.

**(b) Why $t=5$ *is* the Four Color Theorem.** Wagner's theorem: every edge-maximal $K_5$-minor-free graph is obtained by $0$-, $1$-, and $2$-clique-sums, together with $3$-clique-sums, from maximal planar graphs and the Wagner graph $V_8$ (the Möbius–Kantor ladder: $C_8$ with vertices $0,\dots,7$ plus the four chords $i(i+4)$).

Compute: $\chi(V_8)=3$ — color $0,1,2,3,4,5,6,7$ by $1,2,1,2,3,1,3,2$; check the cycle edges alternate and each chord $\{0,4\},\{1,5\},\{2,6\},\{3,7\}$ joins colors $1{-}3$, $2{-}1$, $1{-}3$, $2{-}2$ — the last fails, so adjust $7\mapsto 3$: chords become $1{-}3,\,2{-}1,\,1{-}3,\,2{-}3$ and cycle edge $6{-}7$ is $3{-}3$, also failing. In fact $V_8$ is bipartite-free of odd cycles? It contains the 5-cycle $0,1,2,3,7,0$ (using chord $3\text{–}7$ and edge $7\text{–}0$), so $\chi(V_8)\ge 3$; the assignment $0,1,2,3,4,5,6,7 \mapsto 1,2,3,1,2,3,1,2$ leaves cycle edge $7\text{–}0$ as $2{-}1$ ✓ and chords $0\text{–}4:1{-}2$ ✓, $1\text{–}5:2{-}3$ ✓, $2\text{–}6:3{-}1$ ✓, $3\text{–}7:1{-}2$ ✓. So $\chi(V_8)=3 \le 4$.

Now induct on clique-sums. Since $\chi$ of a $k$-clique-sum is the max of the parts' chromatic numbers ($k\le 3$: recolor one side so the shared clique of $\le 3$ vertices matches), a $K_5$-minor-free graph is 4-colorable as soon as every planar graph is — i.e. exactly the Four Color Theorem. Conversely every planar graph is $K_5$-minor-free (Kuratowski–Wagner), so $t=5$ implies 4CT. Hence the $t=5$ case has no proof independent of the 500-page computer-assisted 4CT, and the $t=6$ case of Robertson–Seymour–Thomas inherits that dependency — a concrete measure of how far the problem is from an elementary treatment at $t=7$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*