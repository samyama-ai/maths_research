---
id: 07-combinatorics/borodin-kostochka-conjecture
title: "Borodin–Kostochka Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borodin–Kostochka Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/borodin-kostochka-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Borodin–Kostochka, 1977).** Every simple finite graph $G$ with maximum degree $\Delta(G) \ge 9$ and clique number $\omega(G) \le \Delta(G) - 1$ satisfies
$$\chi(G) \le \Delta(G) - 1 .$$

Equivalently: for $\Delta \ge 9$, $\chi(G) = \Delta(G)$ forces $G$ to contain $K_{\Delta}$ as a subgraph. Equivalently again, every graph satisfies
$$\chi(G) \le \max\{\omega(G),\ \Delta(G)-1\} \quad \text{whenever } \Delta(G) \ge 9 .$$

Constraints: $G$ is finite, simple (no loops or parallel edges), undirected. The bound $\Delta \ge 9$ cannot be lowered — $C_5 \boxtimes K_3$ has $\Delta = 8$, $\omega = 6$, $\chi = 8$ (Section 10).

A complete proof must handle all graphs with $9 \le \Delta < 10^{14}$ (the range above which the statement is a theorem of Reed). A disproof requires a single graph with $\Delta \ge 9$, no $K_\Delta$, and $\chi = \Delta$; by Brooks' theorem $\chi \le \Delta$ always holds here, so $\chi = \Delta$ is the only possible failure mode.

## 2. Mathematical Foundations

Let $G = (V,E)$, $n = |V|$. Write $N(v)$ for the neighborhood of $v$, $d(v) = |N(v)|$, $\Delta(G) = \max_v d(v)$, $\delta(G) = \min_v d(v)$. A *proper $k$-colouring* is $c : V \to [k]$ with $c(u) \neq c(v)$ for all $uv \in E$; $\chi(G)$ is the least such $k$. The clique number $\omega(G)$ is the largest $t$ with $K_t \subseteq G$; the independence number is $\alpha(G)$.

Baseline bounds:
$$\omega(G) \le \chi(G), \qquad \chi(G) \ge \frac{n}{\alpha(G)}, \qquad \chi(G) \le \Delta(G)+1 .$$

**Theorem (Brooks, 1941).** If $G$ is connected and is neither a complete graph nor an odd cycle, then $\chi(G) \le \Delta(G)$.

The Borodin–Kostochka conjecture is the natural "second step" past Brooks: it asserts that for $\Delta \ge 9$ the only obstruction to $\Delta - 1$ colours is the trivial one, a $K_\Delta$.

**Criticality.** $G$ is *$k$-critical* if $\chi(G) = k$ and $\chi(H) < k$ for every proper subgraph $H$. Every $k$-critical graph has $\delta \ge k-1$. A minimal counterexample to the conjecture is a $\Delta$-critical graph with $\delta \ge \Delta - 1$, so all but a bounded set of vertices have degree exactly $\Delta$ — the graph is nearly regular. This is the standard entry point for every known partial result.

**Relevant products.** The strong product $G \boxtimes H$ has vertex set $V(G) \times V(H)$, with $(g,h) \sim (g',h')$ iff ($g = g'$ or $gg' \in E(G)$) and ($h = h'$ or $hh' \in E(H)$), excluding equality. Then
$$\Delta(G \boxtimes H) = \Delta(G)\Delta(H) + \Delta(G) + \Delta(H), \qquad \omega(G\boxtimes H) = \omega(G)\,\omega(H).$$

**Related conjecture (Reed, 1998).** $\chi(G) \le \left\lceil \tfrac{\Delta(G) + 1 + \omega(G)}{2} \right\rceil$. Reed's conjecture and Borodin–Kostochka are independent statements, but the same probabilistic and structural machinery attacks both.

## 3. History & State of the Art (SOTA)

- **1977.** O. V. Borodin and A. V. Kostochka, studying bounds on $\chi$ in terms of degree and density, state the conjecture and record the $\Delta = 8$ obstruction $C_5 \boxtimes K_3$ that fixes the threshold at $9$.
- **1980s.** Kostochka, and independently Mozhan, verify the conjecture for large maximum degree; Mozhan's argument is usually quoted as covering $\Delta \ge 31$ *(reported in the secondary literature; the primary sources are in Russian, in Metody Diskretnogo Analiza)*.
- **1999.** B. Reed proves the conjecture for all $\Delta \ge 10^{14}$ using the probabilistic method (sparse/dense vertex decomposition plus the Lovász Local Lemma). This remains the only unconditional large-$\Delta$ result with a fully published English proof.
- **2011–2016.** L. Rabern and D. Cranston develop a systematic structural attack (independent-set transversals, "dense neighbourhood" lemmas, Kempe-chain and Mozhan-partition arguments), resolving several natural graph classes and reducing the general conjecture to statements that look strictly weaker.
- **State of the art (2026).** The conjecture is open for every fixed $\Delta$ in $9 \le \Delta \le 10^{14}$, and no counterexample is known for any $\Delta \ge 9$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\Delta \ge 10^{14}$ | Conjecture true | Reed 1999 |
| $\Delta \ge 31$ (as reported) | Conjecture true | Mozhan 1983; Kostochka 1980 |
| Claw-free graphs ($K_{1,3}$-free), $\Delta \ge 9$ | Conjecture true | Cranston–Rabern 2013 |
| Line graphs of (multi)graphs, $\Delta \ge 9$ | Conjecture true | Rabern 2011 |
| $\Delta \ge 13$ and $\omega \le \Delta - 4$ | $\chi \le \Delta-1$; i.e. $\chi = \Delta$ forces $\omega \ge \Delta-3$ | Cranston–Rabern 2015 |
| Graphs with dense neighbourhoods (every $v$ has $e(N(v))$ close to $\binom{d(v)}{2}$) | $\chi \le \Delta - 1$ | Rabern 2014 |
| Girth $\ge 5$, $\Delta$ large | True; in fact $\chi = O(\Delta/\log\Delta)$ | Johansson; Molloy 2019 |
| Planar graphs, $\Delta \ge 9$ | Trivially true: $\chi \le 4 \le \Delta-1$ | Appel–Haken |
| $K_{1,3}$-free and $(K_5-e)$-free | $\chi \le \max\{\omega,\Delta-1\}$ | Dhurandhar 1982 |
| $\Delta \le 8$ | **False in general** — $C_5\boxtimes K_3$ ($\Delta=8$, $\omega=6$, $\chi=8$) | Borodin–Kostochka 1977 |

Cranston and Rabern additionally proved that several formally weaker statements (e.g. the conjecture restricted to graphs with $\omega \ge \Delta - 3$, or to vertex-critical graphs of a restricted shape) are *equivalent* to the full conjecture — so the residual difficulty is concentrated in a narrow band of near-extremal graphs.

## 5. Principal Obstacles

- **No slack in the counting.** A minimal counterexample $G$ has $\delta(G) \ge \Delta - 1$ and $\chi(G) = \Delta$, so it is essentially $\Delta$-regular with an almost-perfect fractional structure. Discharging and greedy arguments, which need a low-degree vertex or a sparse neighbourhood, have nothing to consume.
- **Probabilistic methods have a hard floor.** Reed's proof partitions vertices into sparse and dense parts and applies the Local Lemma; concentration inequalities (Talagrand, Azuma) need error terms of order $\sqrt{\Delta \log \Delta}$ to be $o(1)$ relative to $\Delta$. That forces $\Delta$ astronomically large. The gap $9 \le \Delta \le 10^{14}$ is not a matter of optimising constants — the method has no content at $\Delta = 9$.
- **The extremal examples are near-misses.** $C_5 \boxtimes K_3$ fails only at $\Delta = 8$, and $C_5\boxtimes K_r$ for $r \ne 3$ satisfies the bound with slack $\Theta(r)$. Any correct proof must be sensitive enough to reject $\Delta=8$ while accepting $\Delta=9$, ruling out any purely asymptotic or purely averaging argument.
- **Kempe chains stall.** Mozhan-style partition arguments split $V$ into parts inducing graphs of small degree and recolour along Kempe chains. When $\omega$ is close to $\Delta$, the dense parts are large cliques whose Kempe chains are rigid: swaps propagate globally and the potential function used to prove termination degrades exactly in the regime $\omega \in \{\Delta-3,\dots,\Delta-1\}$.
- **No good certificate for $\chi = \Delta$.** Deciding $k$-colourability is NP-hard, and there is no known polynomial obstruction (fractional, semidefinite, or homomorphism-based) that separates "$\chi = \Delta$, no $K_\Delta$" from "$\chi \le \Delta-1$", so exhaustive computational verification at $\Delta = 9$ is infeasible: candidate critical graphs are $9$-regular with unbounded order.

## 6. The Gap

Proven: the conjecture for $\Delta \ge 10^{14}$ (all graphs), and for every $\Delta \ge 9$ under a structural hypothesis — claw-free, line graph, dense neighbourhoods — or for $\Delta \ge 13$ with $\omega \le \Delta - 4$.

Unproven: the case $9 \le \Delta \le 10^{14}$ for graphs that are simultaneously (i) not claw-free, and (ii) have $\omega \in \{\Delta-3, \Delta-2, \Delta-1\}$ when $\Delta \ge 13$, or arbitrary $\omega \le \Delta-1$ when $9 \le \Delta \le 12$.

The precise step needed: show that a $\Delta$-critical graph with $\Delta \ge 9$, $\delta \ge \Delta-1$ and $\omega \ge \Delta-3$ must contain $K_\Delta$. By Cranston–Rabern this single implication (for $\Delta \ge 13$) is equivalent to the full conjecture in that range; the small cases $\Delta \in \{9,10,11,12\}$ additionally require pushing the "big cliques" theorem below its current $\Delta \ge 13$ threshold.

## 7. Current Research (as of June 2026)

- **Structural reduction school (Cranston, Rabern; Virginia Commonwealth Univ. and collaborators).** Continued refinement of independent-set transversal and "hitting all maximum cliques" lemmas, aiming to lower the $\Delta \ge 13$ threshold of the big-cliques theorem to $\Delta \ge 9$. *(frontier — verify)*
- **Illinois/Novosibirsk criticality school (Kostochka and coauthors).** Sharp lower bounds on the number of edges in $k$-critical graphs (Kostochka–Yancey theory) applied to $\Delta$-critical graphs with $\delta = \Delta-1$, to force local clique structure. *(frontier — verify)*
- **Local/entropy colouring methods.** Post-Molloy techniques for graphs with locally sparse neighbourhoods (local occupancy, hard-core model / Davies–de Joannis de Verclos–Kang–Pirot) give $\chi \le \Delta-1$ whenever any vertex neighbourhood misses enough edges; the open regime is exactly the locally dense one. *(frontier — verify)*
- **Computational search.** SAT/ILP-based searches for $9$-regular $9$-critical $K_9$-free graphs on small vertex counts have found nothing; no exhaustive certificate exists because the order is unbounded. *(frontier — verify)*

## 8. Future Work

1. **Lower the clique threshold.** Prove that $\chi = \Delta \ge 9$ implies $\omega \ge \Delta - 3$ (currently known for $\Delta \ge 13$), then attack $\omega \in \{\Delta-3,\dots,\Delta-1\}$ directly by clique-overlap analysis.
2. **Understand near-extremal structure.** Classify graphs with $\Delta \ge 9$, $\chi = \Delta - 1$, $\omega$ small: are they all "$C_5$-like" blow-ups? A structure theorem here would isolate the true obstruction.
3. **Replace concentration with local arguments.** Develop a local-lemma-free version of Reed's sparse/dense decomposition with additive error $O(1)$ rather than $O(\sqrt{\Delta\log\Delta})$.
4. **Fractional and list analogues.** Determine whether the list-colouring version ($\chi_\ell \le \Delta - 1$ for $\Delta \ge 9$, no $K_\Delta$) is true; a counterexample there would explain why colour-shuffling arguments stall.
5. **Interaction with Reed's conjecture.** Both conjectures are tight on the same examples; a joint proof of the "$\chi \le \max\{\omega, \Delta-1\}$ for $\Delta \ge 9$" and $\chi \le \lceil(\Delta+1+\omega)/2\rceil$ bounds may be easier than either alone.

## 9. Key References

- **[Foundational]** O. V. Borodin and A. V. Kostochka. *On an upper bound of a graph's chromatic number, depending on the graph's degree and density.* Journal of Combinatorial Theory, Series B, 23(2–3):247–250, 1977.
- **[Foundational]** R. L. Brooks. *On colouring the nodes of a network.* Mathematical Proceedings of the Cambridge Philosophical Society, 37(2):194–197, 1941.
- **[SOTA]** B. Reed. *A strengthening of Brooks' theorem.* Journal of Combinatorial Theory, Series B, 76(2):136–149, 1999.
- **[SOTA]** D. W. Cranston and L. Rabern. *Coloring claw-free graphs with $\Delta-1$ colors.* SIAM Journal on Discrete Mathematics, 27(1):534–549, 2013.
- **[SOTA]** D. W. Cranston and L. Rabern. *Graphs with $\chi = \Delta$ have big cliques.* SIAM Journal on Discrete Mathematics, 29(4):1792–1814, 2015.
- **[SOTA]** L. Rabern. *A strengthening of Brooks' Theorem for line graphs.* Electronic Journal of Combinatorics, 18(1):\#P145, 2011.
- **[SOTA]** L. Rabern. *Coloring graphs with dense neighborhoods.* Journal of Graph Theory, 76(4):323–340, 2014.
- **[Recent]** D. W. Cranston and L. Rabern. *Conjectures equivalent to the Borodin–Kostochka conjecture that appear weaker.* Electronic Journal of Combinatorics, 23(2):\#P2.19, 2016.
- **[Related]** A. V. Kostochka, L. Rabern, and M. Stiebitz. *Graphs with chromatic number close to maximum degree.* Discrete Mathematics, 312(6):1273–1281, 2012.
- **[Related]** S. A. Dhurandhar. *Improvement on Brooks' chromatic bound for a class of graphs.* Discrete Mathematics, 42(1):51–56, 1982.
- **[Survey / Book]** M. Molloy and B. Reed. *Graph Colouring and the Probabilistic Method.* Springer, Algorithms and Combinatorics 23, 2002.
- **[Survey / Book]** T. R. Jensen and B. Toft. *Graph Coloring Problems.* Wiley-Interscience, 1995. (Problem 4.8.)

## 10. Worked Example / Concrete Special Case

**The sharpness example $G = C_5 \boxtimes K_3$.**

Take $C_5$ with vertices $u_0,\dots,u_4$ ($u_i \sim u_{i\pm1 \bmod 5}$) and replace each $u_i$ by a triangle $B_i = \{v_i^1,v_i^2,v_i^3\}$, making all $9$ edges between $B_i$ and $B_{i+1}$ present. So $n = 15$.

*Degree.* A vertex $v_i^a$ is adjacent to the other $2$ vertices of $B_i$ and all $3+3$ vertices of $B_{i-1}\cup B_{i+1}$:
$$d(v_i^a) = 2 + 6 = 8 \quad\Rightarrow\quad \Delta(G) = 8 .$$

*Clique number.* $B_i \cup B_{i+1}$ is a $K_6$. No larger clique exists: three blobs $B_i,B_j,B_k$ can never be pairwise adjacent in $C_5$, and any clique meets at most two consecutive blobs. Hence $\omega(G) = 6 = \Delta - 2 \le \Delta - 1$.

*Independence number.* Two vertices are non-adjacent iff they lie in blobs at distance $2$ on $C_5$. Since $C_5$ has no independent set of size $3$, $\alpha(G) = 2$.

*Chromatic number.* Lower bound:
$$\chi(G) \ \ge\ \frac{n}{\alpha(G)} \ = \ \frac{15}{2} \ = \ 7.5 \ \Rightarrow\ \chi(G) \ge 8 .$$
Upper bound: $G$ is connected, not complete ($v_0^1 \not\sim v_2^1$), not an odd cycle, so Brooks gives $\chi(G) \le \Delta(G) = 8$. Therefore
$$\chi(G) = 8 = \Delta(G), \qquad \omega(G) = 6 < 7 = \Delta(G)-1 .$$

So $G$ violates "$\chi \le \Delta-1$ when $\omega \le \Delta-1$" at $\Delta = 8$, which is exactly why the conjecture is stated for $\Delta \ge 9$.

**Why the family stops there.** For general $r$, $G_r = C_5 \boxtimes K_r$ has $n = 5r$, $\alpha = 2$, $\Delta = 3r-1$, $\omega = 2r$, and $\chi(G_r) = \lceil 5r/2 \rceil$. The conjecture's conclusion $\chi \le \Delta - 1 = 3r-2$ fails iff $\lceil 5r/2\rceil > 3r-2$, i.e. iff $r \le 3$; and the hypothesis $\omega \le \Delta-1$ requires $2r \le 3r-2$, i.e. $r \ge 2$. For $r = 2$: $\Delta = 5$, $\omega = 4 = \Delta-1$, $\chi = 5 = \Delta$ — consistent with $\chi \le \max\{\omega,\Delta-1\}$? No: $\max\{4,4\}=4 < 5$, so $G_2$ (the $5$-regular Clebsch-like graph $C_5\boxtimes K_2$) is a second small counterexample, at $\Delta = 5$. For $r = 4$: $\Delta = 11$, $\omega = 8$, $\chi = 10 = \Delta - 1$ — tight but consistent. Beyond $r=3$ the slack $3r-2-\lceil 5r/2\rceil = \Theta(r/2)$ grows, so this construction produces no counterexample for any $\Delta \ge 9$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*