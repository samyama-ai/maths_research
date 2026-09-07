---
id: 07-combinatorics/hajos-conjecture
title: "Hajós Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hajós Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hajos-conjecture` · **Status:** solved-recently (refuted in general; cases $k=5,6$ open)

## 1. Problem Statement / Conjecture

Hajós (1961) conjectured:

> For every integer $k \ge 1$, every graph $G$ with $\chi(G) \ge k$ contains a subdivision of the complete graph $K_k$ as a subgraph.

Equivalently: $G \supseteq TK_{\chi(G)}$ for every graph $G$, where $TK_r$ denotes any graph obtained from $K_r$ by replacing edges with internally disjoint paths. Contrapositive form for fixed $k$: every $TK_k$-free graph is $(k-1)$-colourable.

Catalog status note: the conjecture is **false as stated**. Catlin (1979) constructed counterexamples for every $k \ge 7$, and Erdős–Fajtlowicz (1981) showed almost every graph is a counterexample. The residual open problem is the two-case statement:

> **(H5)** Every graph with no $K_5$-subdivision is $4$-colourable. **(H6)** Every graph with no $K_6$-subdivision is $5$-colourable.

A complete resolution of the remaining problem requires either a proof of (H5) and (H6), or an explicit graph $G$ with $\chi(G)\ge 5$ (resp. $\ge 6$) and no $TK_5$ (resp. $TK_6$) subgraph.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, simple, undirected. $\chi(G)$ is the least $k$ with a proper colouring $c:V\to[k]$, $\omega(G)$ the clique number, $\alpha(G)$ the independence number, $d(G)=2|E|/|V|$ the average degree.

**Subdivision (topological minor).** $H$ is a *topological minor* of $G$, written $H \preceq_t G$, if there is an injection $\varphi: V(H)\to V(G)$ (the *branch vertices*) and a family $\{P_{uv} : uv\in E(H)\}$ of paths in $G$, internally disjoint from each other and from $\varphi(V(H))$, with $P_{uv}$ joining $\varphi(u)$ to $\varphi(v)$. Write $TK_r$ for a subdivision of $K_r$; it has $r$ branch vertices and $\binom r2$ paths.

**Hierarchy.** Topological minor $\Rightarrow$ minor, so Hajós implies Hadwiger's conjecture ($\chi(G)\ge k \Rightarrow K_k \preceq_m G$) for each $k$; the two are equivalent for $k\le 4$ and Hajós is strictly stronger for $k\ge 5$.

**Extremal threshold.** Define $\sigma(G)=\max\{r : TK_r \subseteq G\}$. Mader's problem, solved by Bollobás–Thomason (1998) and Komlós–Szemerédi (1996): there is $c>0$ with
$$d(G) \ge c\,r^{2} \;\Longrightarrow\; TK_r \subseteq G ,$$
and $c r^2$ is optimal up to the constant (random graphs $G(n,p)$ with $p$ tuned show $d = \Theta(r^2)$ is needed).

**Degeneracy bound from colouring.** If $\chi(G)\ge k$, some subgraph $G'$ is $k$-critical, hence $\delta(G')\ge k-1$ and $d(G')\ge k-1$. Combining with the threshold gives only
$$\chi(G)\ge k \;\Longrightarrow\; \sigma(G) \;\ge\; c'\sqrt{k}. \tag{2.1}$$
This linear-versus-quadratic mismatch is the structural heart of the problem.

**Erdős–Fajtlowicz parameter.**
$$H(n) \;=\; \max_{|V(G)|=n} \frac{\chi(G)}{\sigma(G)} .$$
Hajós asserts $H(n)\le 1$. Fox, Lee and Sudakov (2013) proved $H(n)=\Theta\!\left(\sqrt{n}/\log n\right)$, so the conjecture fails by the largest possible margin.

## 3. History & State of the Art (SOTA)

- **1943.** Hadwiger states the minor version.
- **1952.** Dirac proves the $k=4$ case of both conjectures: every $4$-chromatic graph contains a $TK_4$.
- **1961.** György Hajós states the subdivision strengthening (Halle-Wittenberg proceedings), motivated by his construction of $k$-critical graphs (the *Hajós join*).
- **1979.** Catlin refutes the conjecture for all $k\ge 7$ using blow-ups $C_5[K_r]$ of the $5$-cycle.
- **1981.** Erdős and Fajtlowicz: for $G\sim G(n,1/2)$, $\chi = (1+o(1))\,n/(2\log_2 n)$ while $\sigma(G)=(1+o(1))\,2\sqrt n$ (Bollobás–Catlin, 1981). Hence almost all graphs are counterexamples — the counterexamples are typical, not exotic.
- **1993.** Robertson–Seymour–Thomas prove Hadwiger for $k=6$; the corresponding Hajós cases stay open.
- **2005–2007.** Thomassen shows counterexamples persist under strong side conditions (large girth is *not* one of them) and proves Hajós for line graphs.
- **2006.** Yu and Zickfeld reduce (H5) to $4$-connected graphs.
- **2013.** Fox–Lee–Sudakov settle the Erdős–Fajtlowicz quantitative question, $H(n)=\Theta(\sqrt n/\log n)$.
- **2020.** He, Wang and Yu prove the Kelmans–Seymour conjecture: every $5$-connected non-planar graph contains a $TK_5$ — the strongest structural handle currently available on (H5).

## 4. Partial Results / Verified Cases

- **$k\le 3$:** trivial. $\chi\ge 2$ forces an edge; $\chi\ge 3$ forces an odd cycle, which contains $TK_3$.
- **$k=4$:** true (Dirac 1952). $TK_4$-free graphs have treewidth $\le 2$ (series–parallel), hence are $3$-degenerate-by-$2$ and $3$-colourable.
- **$k=5$ (H5), restricted:** true for $4$-connected graphs would suffice (Yu–Zickfeld 2006); true for graphs containing no $K_4^-$-configuration obstruction (Ma–Yu); every $5$-connected non-planar graph contains $TK_5$ (He–Wang–Yu 2020), so a minimal counterexample to (H5) has connectivity exactly $4$ or is planar (planar graphs are $4$-colourable, so planarity is excluded).
- **$k \ge 7$:** false. Catlin's family $C_5[K_r]$ (each vertex of $C_5$ blown up to a clique $K_r$, adjacent blocks joined completely) has $\alpha=2$, $n=5r$, $\chi=\lceil 5r/2\rceil$, and $\sigma$ too small.
- **Large girth:** Kühn and Osthus (2002) proved that graphs of girth at least a fixed constant and minimum degree $\ge r$ contain $TK_{r+1}$; combined with criticality this gives Hajós for all graphs of large girth, all $k$.
- **Line graphs:** true for all $k$ (Thomassen 2007).
- **Random graphs:** false with probability $1-o(1)$ for $G(n,1/2)$ (Erdős–Fajtlowicz 1981).
- **Small cases computationally:** all graphs on $n\le 10$ vertices are consistent with (H5) and (H6); Catlin's smallest counterexample $C_5[K_3]$ has $n=15$.

## 5. Principal Obstacles

- **Quadratic vs. linear degree.** Forcing $TK_k$ needs average degree $\Theta(k^2)$ (Bollobás–Thomason; Komlós–Szemerédi), while $\chi\ge k$ delivers only $\delta \ge k-1$ in a critical subgraph. Every purely density-based argument therefore stalls at $(2.1)$, giving $TK_{\Theta(\sqrt k)}$ — quadratically short. No colouring hypothesis is known to boost density beyond criticality.
- **Extremal counterexamples have $\alpha = 2$.** Catlin's graphs and dense random graphs both use many vertices with small independence number to inflate $\chi$ without creating room for internally disjoint paths. Subdivisions consume *vertices*, not just edges: a $TK_k$ needs at least $k$ vertices of degree $\ge k-1$ plus internal vertices for every non-adjacent branch pair. Chromatic number is insensitive to this budget.
- **Minor techniques do not transfer.** The Robertson–Seymour–Thomas proof of Hadwiger for $k=6$ uses the structure theorem for $K_6$-minor-free graphs (apex over planar). No comparable structure theorem exists for $TK_5$- or $TK_6$-free graphs: subdivision-closed classes are not minor-closed, so graph-minors machinery (well-quasi-ordering, tree decompositions of excluded-minor classes) is unavailable.
- **(H5) is at least as hard as the Four Colour Theorem.** (H5) $\Rightarrow$ Hadwiger for $k=5$ $\Rightarrow$ 4CT (Wagner's equivalence). Any proof must contain a proof of 4CT, so no short combinatorial argument is expected.
- **Probabilistic/algebraic methods give the wrong direction.** Random constructions and the Lovász theta-function bound both *produce* counterexamples for large $k$; they say nothing about the small-$k$ regime where the vertex budget is tight.

## 6. The Gap

Proved: $\chi \ge k \Rightarrow TK_{c\sqrt k}$, plus exact results for $k\le 4$ and refutation for $k\ge 7$. Conjectured (residual): $k \in \{5,6\}$.

The precise boundary for (H5): by Yu–Zickfeld, a minimum counterexample $G$ to (H5) is $4$-connected, non-planar (else 4CT applies), and $5$-critical. By He–Wang–Yu, $G$ is not $5$-connected. So the entire open case lives in **exactly $4$-connected, non-planar, $5$-chromatic, $TK_5$-free graphs**. The missing step is a structure theorem describing how $4$-cuts can be used to build $TK_5$-free graphs, together with a colouring argument that glues $4$-colourings across such cuts — the analogue of the RST apex-planar decomposition, which is not known to exist here.

For (H6) the gap is wider: no reduction to a bounded connectivity class is known, and even the implication (H6) $\Rightarrow$ Hadwiger $k=6$ (a theorem needing the full RST machinery) shows any proof must subsume that argument.

## 7. Current Research (as of June 2026)

- **Georgia Tech school (Yu and collaborators).** Continuation of the Kelmans–Seymour programme: extending $TK_5$-existence results from $5$-connected to $4$-connected graphs with prescribed local structure, aiming directly at (H5). *(frontier — verify)*
- **Extremal/probabilistic side (Sudakov, Lee, and coauthors).** Refinements of $H(n)=\Theta(\sqrt n/\log n)$ to the list-chromatic and fractional analogues, and to clique subdivisions in $H$-free hosts.
- **Sparse-host results (Birmingham: Kühn, Osthus, and successors).** Girth, expansion and $K_{s,s}$-freeness as substitutes for the missing density; the general theme is "any hypothesis that kills dense pseudo-random blow-ups restores Hajós".
- **Variants that survive.** The *fractional*, *list*, and *odd-$K_k$-subdivision* versions are under active study; the odd-subdivision analogue is closely tied to Geelen–Gerards–Reed–Seymour–Vetta odd-minor theory.
- **Computer search.** Exhaustive generation (nauty/geng-based) has not produced a $5$-chromatic $TK_5$-free graph in the feasible range; searches are limited by the cost of testing $TK_5$-containment (polynomial, via Robertson–Seymour, but with impractical constants for exhaustive sweeps). *(frontier — verify)*

## 8. Future Work

- Build a decomposition theorem for $4$-connected $TK_5$-free graphs analogous to the apex-planar description of $K_6$-minor-free graphs; this is the pathway Yu and Zickfeld's reduction points to.
- Determine the truth of (H6) modulo (H5): is there a reduction of $k=6$ to $k=5$ analogous to the Hadwiger induction?
- Sharpen $(2.1)$: find any hypothesis $P$ such that $\chi \ge k$ and $P$ force $TK_{\Omega(k)}$, then check whether $P$ holds for $5$-critical graphs.
- Seymour's suggested reframing: study which *classes* satisfy Hajós, replacing the false universal statement by a classification — line graphs, large-girth graphs and (conjecturally) graphs of bounded independence-ratio complement.
- Compute the exact minimum order of a counterexample for each $k \ge 7$; only $k=7$ is bracketed ($\le 15$ from Catlin).

## 9. Key References

- **[Foundational]** G. A. Dirac. *A property of 4-chromatic graphs and some remarks on critical graphs.* Journal of the London Mathematical Society 27 (1952), 85–92.
- **[Foundational]** G. Hajós. *Über eine Konstruktion nicht $n$-färbbarer Graphen.* Wissenschaftliche Zeitschrift der Martin-Luther-Universität Halle-Wittenberg, Math.-Naturwiss. Reihe 10 (1961), 116–117.
- **[Refutation]** P. A. Catlin. *Hajós' graph-coloring conjecture: variations and counterexamples.* Journal of Combinatorial Theory, Series B 26 (1979), 268–274.
- **[Refutation]** P. Erdős and S. Fajtlowicz. *On the conjecture of Hajós.* Combinatorica 1 (1981), 141–143.
- **[Foundational]** B. Bollobás and P. A. Catlin. *Topological cliques of random graphs.* Journal of Combinatorial Theory, Series B 30 (1981), 224–227.
- **[Extremal]** J. Komlós and E. Szemerédi. *Topological cliques in graphs II.* Combinatorics, Probability and Computing 5 (1996), 79–90.
- **[Extremal]** B. Bollobás and A. Thomason. *Proof of a conjecture of Mader, Erdős and Hajnal on topological complete subgraphs.* European Journal of Combinatorics 19 (1998), 883–887.
- **[SOTA]** J. Fox, C. Lee and B. Sudakov. *Chromatic number, clique subdivisions, and the conjectures of Hajós and Erdős–Fajtlowicz.* Combinatorica 33 (2013), 421–431.
- **[SOTA]** X. Yu and F. Zickfeld. *Reducing Hajós' 4-coloring conjecture to 4-connected graphs.* Journal of Combinatorial Theory, Series B 96 (2006), 482–492.
- **[SOTA]** D. He, Y. Wang and X. Yu. *The Kelmans–Seymour conjecture I–IV.* Journal of Combinatorial Theory, Series B 144 (2020).
- **[Structural]** C. Thomassen. *Some remarks on Hajós' conjecture.* Journal of Combinatorial Theory, Series B 93 (2005), 95–105.
- **[Structural]** C. Thomassen. *Hajós' conjecture for line graphs.* Journal of Combinatorial Theory, Series B 97 (2007), 156–157.
- **[Structural]** D. Kühn and D. Osthus. *Topological minors in graphs of large girth.* Journal of Combinatorial Theory, Series B 86 (2002), 364–380.
- **[Related]** N. Robertson, P. Seymour and R. Thomas. *Hadwiger's conjecture for $K_6$-free graphs.* Combinatorica 13 (1993), 279–361.
- **[Survey]** P. Seymour. *Hadwiger's conjecture.* In: J. F. Nash Jr. and M. Th. Rassias (eds.), *Open Problems in Mathematics*, Springer, 2016, 417–437.
- **[Textbook]** R. Diestel. *Graph Theory*, 5th edition. Springer GTM 173, 2017 (Ch. 7).

## 10. Worked Example / Concrete Special Case

**(a) The true case $k=4$.** Claim: $TK_4$-free $\Rightarrow$ $3$-colourable. Induct on $|V|$. If $G$ has a vertex $v$ of degree $\le 2$, colour $G-v$ and extend. Otherwise $\delta(G)\ge 3$. A classical lemma (Dirac 1964) states every graph with $n$ vertices and at least $2n-2$ edges contains a $TK_4$; more simply, a $2$-connected graph with $\delta \ge 3$ contains a cycle $C$ with a path joining two non-adjacent vertices of $C$ plus a further chord-path — yielding four branch vertices and six internally disjoint paths, i.e. a $TK_4$. So $TK_4$-free graphs are $2$-degenerate, hence $3$-colourable. This matches Hajós at $k=4$ exactly.

**(b) Catlin's counterexample $G = C_5[K_3]$.** Vertices: $V = \{v_{i,j} : i\in\mathbb Z_5,\ j\in\{1,2,3\}\}$, so $n=15$. Edges: $v_{i,j}\sim v_{i,j'}$ for $j\ne j'$ (inside each block), and $v_{i,j}\sim v_{i+1,j'}$ for all $j,j'$ (between consecutive blocks).

- *Degrees.* $\deg(v_{i,j}) = 2 + 3 + 3 = 8$; $|E| = 15\cdot 8/2 = 60$.
- *Independence number.* Two vertices are non-adjacent iff their blocks are non-consecutive; three blocks of $C_5$ cannot be pairwise non-consecutive, so $\alpha(G)=2$.
- *Chromatic number.* Each colour class has size $\le \alpha = 2$, so $\chi \ge \lceil 15/2\rceil = 8$. The pairing $\{v_{i,j}, v_{i+2,j}\}$ for suitable indices gives $7$ classes of size $2$ and one singleton, so $\chi(G)=8$. ($\omega(G)=6$, from two consecutive blocks.)
- *The vertex budget.* Suppose $TK_8 \subseteq G$ with branch set $B$, $|B|=8$. Only $15-8=7$ vertices remain as path interiors, and distinct non-adjacent branch pairs need disjoint interiors, so
$$e(G[B]) \;\ge\; \binom{8}{2} - 7 \;=\; 21 .$$
Writing $b_i = |B \cap \text{block } i|$ with $\sum b_i = 8$, we get $e(G[B]) = \sum_i \binom{b_i}{2} + \sum_i b_i b_{i+1}$. The maximum over all distributions is attained at $(b_1,\dots,b_5)=(3,3,2,0,0)$: $\;(3+3+1) + (9+6+0+0+0) = 22$. Catlin's case analysis rules out the few distributions with $e(G[B]) \ge 21$, since the surviving configurations cannot supply the required disjoint interiors for all $\binom82 - e(G[B]) \le 7$ missing pairs while keeping branch degrees at $7$.

Hence $\chi(G)=8$ but $\sigma(G)\le 7$: Hajós fails at $k=8$, and the same blow-up family $C_5[K_r]$ extends the failure to every $k\ge 7$. The slack in the count ($22$ versus $21$) shows how narrowly the construction works — which is exactly why the same idea has never been pushed down to $k=5$ or $k=6$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*