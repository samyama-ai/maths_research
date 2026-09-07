---
id: 07-combinatorics/lovasz-path-removal-conjecture
title: "Lovász Path Removal Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lovász Path Removal Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/lovasz-path-removal-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Lovász, 1975).** There is a function $f:\mathbb{N}\to\mathbb{N}$ such that for every $k\ge 1$, every $f(k)$-connected finite simple graph $G$, and every pair of distinct vertices $s,t\in V(G)$, there exists an **induced** path $P$ from $s$ to $t$ in $G$ such that $G-V(P)$ is $k$-connected.

Constraints and reading:

- $G$ is finite, simple, undirected. "$m$-connected" means $|V(G)|>m$ and $G-X$ is connected for every $X\subseteq V(G)$ with $|X|<m$.
- $P$ is induced: $G[V(P)]=P$, i.e. $P$ has no chords.
- The bound $f(k)$ must depend on $k$ only — not on $|V(G)|$, the maximum degree, girth, or the choice of $s,t$.

A complete proof requires exhibiting such an $f$ (with any growth rate) together with an argument valid for all $k$. A disproof requires, for some fixed $k$, an infinite family $G_1,G_2,\dots$ with $\kappa(G_i)\to\infty$ and prescribed pairs $s_i,t_i$ such that no induced $s_i$–$t_i$ path leaves a $k$-connected remainder. The conjecture is **open for every $k\ge 3$**: not even the existence of $f(3)$ is known.

## 2. Mathematical Foundations

Let $\kappa(G)$ denote vertex connectivity. Define, for $k\ge1$,

$$
f(k)\;=\;\min\Big\{\,m\in\mathbb{N}\;:\;\forall G \text{ with } \kappa(G)\ge m,\ \forall s\neq t\in V(G),\ \exists\ \text{induced } s\text{–}t \text{ path } P \text{ with } \kappa\big(G-V(P)\big)\ge k \Big\},
$$

with $f(k)=\infty$ if no such $m$ exists. The conjecture asserts $f(k)<\infty$ for all $k$.

**Elementary constraints.**

- *Order.* $G-V(P)$ must be $k$-connected, so $|V(G)|-|V(P)|\ge k+1$. High connectivity alone does not bound $|V(P)|$, so the argument must control path length implicitly.
- *Trivial lower bound.* $f(k)\ge k+2$: deleting the interior of $P$ can destroy at most the connectivity that the removed vertices carried, and a $(k+1)$-connected $G$ may become $(k-1)$-connected.
- *Monotonicity.* $f$ is non-decreasing, since a $k$-connected remainder is $(k-1)$-connected.

**Certificate form.** A separator obstruction is a set $S\subseteq V(G)\setminus V(P)$ with $|S|<k$ such that $G-V(P)-S$ is disconnected. Thus the statement "$P$ is good" is a $\Pi_1$ condition over all $\binom{n}{<k}$ sets $S$, and a proof must simultaneously defeat exponentially many potential separators — this is the source of the difficulty (Section 5).

**Cycle form.** The edge version replaces the pair $(s,t)$ by an edge $e$ and asks for an induced cycle $C$ with $e\in E(C)$ and $\kappa(G-V(C))\ge k$. The two versions are equivalent up to an additive constant in $f$: given $e=st$, an induced $s$–$t$ path in $G-e$ avoiding chords closes to an induced cycle, and conversely.

**Base cases as theorems.**

- $k=1$, cycle form: every $3$-connected graph has, through any edge, an induced cycle $C$ with $G-V(C)$ connected — a consequence of Tutte's theory of non-separating induced cycles (peripheral cycles) developed in *How to draw a graph* (1963), refined by Thomassen and Toft (1981).
- $k=1$, path form: $f(1)=3$.
- $k=2$: $f(2)=5$ (Chen–Gould–Yu 2003).

## 3. History & State of the Art (SOTA)

- **1963.** Tutte proves that in a $3$-connected graph every edge lies on at least two peripheral (non-separating induced) cycles — the structural ancestor of the conjecture.
- **1975.** Lovász poses the removal conjecture; it circulates through his problem lists and *Combinatorial Problems and Exercises* (North-Holland, 1979), and is stated in the modern form in the literature of the 1980s–2000s.
- **1981.** Thomassen and Toft, *Non-separating induced cycles in graphs* (JCTB), show every graph with minimum degree $\ge 3$ has a non-separating induced cycle; Thomassen, *Nonseparating cycles in $k$-connected graphs* (JGT), gives cycle removals preserving connectivity in the non-induced regime.
- **2001.** Kriesell, *Induced paths in 5-connected graphs* (JGT), gives the first substantial attack at connectivity $5$.
- **2003.** Chen, Gould and Yu, *Graph connectivity after path removal* (Combinatorica), settle $k=2$: every $5$-connected graph admits, for any $s,t$, an induced $s$–$t$ path whose deletion leaves a $2$-connected graph. They also exhibit $4$-connected graphs where this fails, so $f(2)=5$ exactly.
- **2008.** Kawarabayashi, Lee, Reed and Wollan, *A weaker version of Lovász' path removal conjecture* (JCTB), prove a relaxation for all $k$: at sufficiently high connectivity one can always find an induced $s$–$t$ path whose removal leaves a graph that is $k$-connected apart from a bounded, explicitly described exceptional structure. This is the strongest general-$k$ statement known.
- **2008–present.** Adjacent progress on "connectivity-keeping" subgraphs (Fujita–Kawarabayashi, JCTB 2008) and on non-separating subgraphs in highly connected graphs, none of which closes the induced-path case for $k\ge 3$.

The data $f(1)=3$, $f(2)=5$ fit $f(k)=2k+1$; no construction is known that rules this out, and it is the standard refined guess.

## 4. Partial Results / Verified Cases

- **$k=1$: solved, $f(1)=3$.** Every $3$-connected graph and every pair $s,t$ admits an induced $s$–$t$ path with connected remainder. Sharp: $K_{2,3}$ is $2$-connected and fails (Section 10).
- **$k=2$: solved, $f(2)=5$** (Kriesell 2001; Chen–Gould–Yu 2003). Both the upper bound ($5$-connected suffices) and sharpness ($4$-connected counterexamples exist) are established.
- **$k\ge 3$: open**, including the mere finiteness of $f(3)$.
- **Cycle version, $k=1$:** every $3$-connected graph has a non-separating induced cycle through each prescribed edge (Tutte 1963; Thomassen–Toft 1981); every graph of minimum degree $\ge3$ has one somewhere.
- **Bounded-defect version, all $k$:** Kawarabayashi–Lee–Reed–Wollan (2008) establish the conjecture when the conclusion is weakened to allow a bounded exceptional set/structure, giving a finite connectivity threshold for the relaxed statement at every $k$.
- **Non-induced variant:** even dropping the induced requirement (a strictly weaker demand, since more candidate paths are admissible), no finite bound is known for $k\ge3$.
- **Lower bounds:** $f(k)\ge k+2$ trivially; $f(2)\ge5$ by explicit $4$-connected examples. No superlinear lower bound is known for any $k$.

## 5. Principal Obstacles

- **No induction on $k$.** The natural strategy — remove a path to drop from $k$ to $k-1$, then iterate — fails, because the hypothesis needed at step $k$ is connectivity $f(k)$ of the *original* graph and the removal destroys the structure ($G-V(P)$ is $k$-connected but nothing is known about *its* $s,t$ pairs or its induced paths). The known $k=1,2$ proofs are ad hoc case analyses of local separator configurations; the number of cases grows fast with $k$.
- **Path length is unbounded.** An induced $s$–$t$ path may need to be long (in a graph of large girth, all $s$–$t$ paths are long and automatically induced). Greedy or local rerouting arguments lose control: a repair that fixes one $(k-1)$-separator can create another far away, with no monotone potential function known to terminate the process.
- **Separator interaction.** Preserving $k$-connectivity means defeating all sets $S$ with $|S|\le k-1$ simultaneously. The submodular/uncrossing machinery for $k$-cuts (Menger, Tutte's tree decomposition of $2$-cuts, the Cunningham–Edmonds framework) is well behaved for $k\le 2$ but there is no comparably clean lattice of $k$-separators for $k\ge3$ once vertices are deleted rather than contracted.
- **Contraction methods do not transfer.** Kriesell-style results on contractible edges and Mader-style results on $k$-critical graphs control *edge* operations; deleting the vertex set of a path is a large, non-local operation that no known contraction/critical-subgraph reduction models.
- **Extremal counterexamples are hard to search for.** The failure of $4$-connected graphs at $k=2$ was found by hand-crafted construction; random and computer search over $6$–$8$-connected graphs is infeasible at the sizes where the phenomenon (if any) for $k=3$ would appear.
- **Minor/structure theory gives the wrong dichotomy.** Graph minor tools yield either a large clique minor or a bounded-width decomposition; neither directly produces an *induced* path with a global connectivity guarantee, which is why Kawarabayashi–Lee–Reed–Wollan land on a weakened conclusion.

## 6. The Gap

Proven: $f(1)=3$, $f(2)=5$, and, for every $k$, a finite threshold for the *approximate* statement in which $G-V(P)$ is $k$-connected up to a bounded exceptional structure. Conjectured: a finite threshold for the *exact* statement at every $k$.

The precise barrier is the removal of the exceptional structure in the 2008 theorem — equivalently, an argument that at connectivity $f(k)$ one can always reroute an induced $s$–$t$ path so as to avoid *every* $(k-1)$-separator of the remainder, not merely all but boundedly many. Concretely, the missing step is a **rerouting lemma with a monotone potential**: given an induced $s$–$t$ path $P$ and a set $S$, $|S|\le k-1$, separating $G-V(P)$, produce an induced $s$–$t$ path $P'$ with strictly smaller potential (e.g. lexicographically smaller multiset of bad separators) using only $\kappa(G)\ge f(k)$. For $k\le2$ such a lemma is available through the $2$-cut structure tree; for $k=3$ nothing plays that role.

## 7. Current Research (as of June 2026)

- **$k=3$ as the decisive test case.** Effort concentrates on proving $f(3)<\infty$, with $f(3)=7$ the target if $f(k)=2k+1$ holds. Groups in structural graph theory at NII Tokyo (Kawarabayashi and collaborators), Georgia Tech / Emory (the Yu–Gould circle), and Hamburg/Ilmenau (Kriesell) remain the main centres. *(frontier — verify)*
- **Quantitative strengthening of the 2008 weak version**, aiming to shrink the exceptional structure to size $0$ under higher connectivity; the natural intermediate statement is a bound of the form "connectivity $c\cdot k$ suffices for the remainder to be $k$-connected after deleting at most $g(k)$ extra vertices". *(frontier — verify)*
- **Non-separating subgraph analogues:** connectivity-keeping trees and paths of prescribed shape (Fujita–Kawarabayashi lineage, and later work on keeping $k$-connectivity after deleting a tree with prescribed leaves) are being used as testbeds for potential-function arguments. *(frontier — verify)*
- **Computational search** for $6$-connected counterexamples at $k=3$ over vertex-transitive and Cayley graphs; nothing reported. *(frontier — verify)*
- **Directed and hypergraph analogues** are being formulated, mainly to identify which features of undirected connectivity the conjecture really uses.

## 8. Future Work

- Prove the **cycle form for $k=3$** first: an induced cycle through a prescribed edge whose deletion leaves a $3$-connected graph. The edge version has more symmetry and a richer supply of Tutte-style peripheral cycles.
- Develop a **structure theory of $3$-separators stable under vertex deletion**, extending the Tutte/Cunningham decomposition of $2$-cuts. This is the single most-cited prerequisite.
- Settle the **non-induced version** for $k\ge3$; a positive answer there would localise the difficulty in the chord-freeness requirement.
- Determine whether $f(k)=2k+1$ by constructing $2k$-connected counterexamples generalising the $4$-connected, $k=2$ examples of Chen–Gould–Yu.
- Seek a **linear-programming or matroid relaxation** of "induced path avoiding all small separators", where duality could replace the missing rerouting lemma.
- Test the conjecture on **expanders and graphs of large girth**, where induced paths are plentiful but separators are scarce — a proof restricted to girth $\ge5$ and $k=3$ would be a genuine advance.

## 9. Key References

- **[Foundational]** Tutte, W. T. *How to draw a graph.* Proceedings of the London Mathematical Society 13 (1963), 743–767.
- **[Foundational]** Lovász, L. *Combinatorial Problems and Exercises.* North-Holland, Amsterdam, 1979.
- **[Foundational]** Thomassen, C., Toft, B. *Non-separating induced cycles in graphs.* Journal of Combinatorial Theory, Series B 31 (1981), 199–224.
- **[Foundational]** Thomassen, C. *Nonseparating cycles in $k$-connected graphs.* Journal of Graph Theory 5 (1981), 351–354.
- **[SOTA]** Chen, G., Gould, R. J., Yu, X. *Graph connectivity after path removal.* Combinatorica 23 (2003), 185–203.
- **[SOTA]** Kriesell, M. *Induced paths in 5-connected graphs.* Journal of Graph Theory 36 (2001), 52–58.
- **[SOTA / Recent]** Kawarabayashi, K., Lee, O., Reed, B., Wollan, P. *A weaker version of Lovász' path removal conjecture.* Journal of Combinatorial Theory, Series B 98 (2008), 972–979.
- **[Related]** Fujita, S., Kawarabayashi, K. *Connectivity keeping edges in graphs with large minimum degree.* Journal of Combinatorial Theory, Series B 98 (2008), 805–811.
- **[Survey]** Kriesell, M. *A survey on contractible edges in graphs of a prescribed vertex connectivity.* Graphs and Combinatorics 18 (2002), 1–30.
- **[Survey]** Bondy, J. A., Murty, U. S. R. *Graph Theory.* Springer, Graduate Texts in Mathematics 244, 2008.

## 10. Worked Example / Concrete Special Case

**(a) Sharpness at $k=1$: $f(1)>2$.** Let $G=K_{2,3}$ with parts $\{s,t\}$ and $\{a,b,c\}$. Then $\kappa(G)=2$. Every induced $s$–$t$ path has length $2$: the candidates are $sat$, $sbt$, $sct$ (any longer walk would revisit $s$ or $t$). Take $P=sat$, so $V(P)=\{s,a,t\}$ and

$$G-V(P)=G[\{b,c\}]=\overline{K_2},$$

which is disconnected. By symmetry the same holds for $P=sbt$ and $P=sct$. So no induced $s$–$t$ path leaves a connected remainder, and $2$-connectivity is insufficient: $f(1)\ge3$.

**(b) The positive case $k=1$ on the cube.** Let $G=Q_3$, the $3$-cube, $V=\{0,1\}^3$, edges between strings at Hamming distance $1$. $Q_3$ is $3$-regular and $3$-connected, so $\kappa(Q_3)=3=f(1)$. Take $s=000$, $t=111$ and

$$P:\;000\,-\,100\,-\,110\,-\,111 .$$

*Induced check.* Non-consecutive pairs: $d(000,110)=2$, $d(100,111)=2$, $d(000,111)=3$. No chords, so $P$ is induced.

*Removal.* $V(G)\setminus V(P)=\{001,010,011,101\}$ with induced edges $001\!-\!011$, $001\!-\!101$, $010\!-\!011$. The remainder is the path $101-001-011-010$: connected. So $P$ witnesses the $k=1$ statement for this pair.

*Failure of the naive greedy choice.* The shortest induced path is not always usable in general graphs; here, however, note that the alternative $000-001-011-111$ also works, leaving $100,110,010,101$ with edges $100\!-\!110$, $110\!-\!010$, $100\!-\!101$ — again connected. Both witnesses exist because $\kappa=3$; part (a) shows that at $\kappa=2$ every witness can be destroyed.

**(c) What changes at $k=2$.** Requiring $\kappa(G-V(P))\ge2$ on $Q_3$ is impossible for order reasons: $|V(Q_3)|=8$ and any induced $000$–$111$ path has $4$ vertices, leaving $4$ vertices with only $3$ edges — a tree, never $2$-connected. This is exactly why $f(2)=5>3$: the theorem of Chen–Gould–Yu needs $5$-connectivity, and its sharpness comes from $4$-connected graphs in which every induced $s$–$t$ path leaves a cut vertex behind. Generalising these two obstructions — order deficiency and residual cut sets — to $k=3$ is the content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*