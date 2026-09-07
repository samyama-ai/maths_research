---
id: 07-combinatorics/erdos-nesetril-conjecture
title: "Erdős-Nešetřil Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Nešetřil Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-nesetril-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A *strong edge colouring* of a simple graph $G$ is an assignment of colours to $E(G)$ such that every colour class is an **induced matching**: any two edges receiving the same colour are neither adjacent nor joined by a third edge. The least number of colours is the *strong chromatic index* $\chi'_s(G)$.

**Conjecture (Erdős–Nešetřil, 1985).** For every graph $G$ with maximum degree $\Delta$,
$$
\chi'_s(G) \;\le\;
\begin{cases}
\dfrac{5}{4}\Delta^2, & \Delta \text{ even},\\[2mm]
\dfrac{5\Delta^2 - 2\Delta + 1}{4}, & \Delta \text{ odd}.
\end{cases}
$$

The bounds are attained (Section 10), so the conjecture asserts an exact extremal result, not merely an asymptotic one. A complete proof requires the inequality for **all** graphs with the stated $\Delta$; a disproof requires a single graph $G$ with $\Delta(G)=\Delta$ and $\chi'_s(G)$ exceeding the bound. The weaker asymptotic form, $\chi'_s(G) \le (\tfrac54 + o(1))\Delta^2$, is itself open and is the target of essentially all current work.

## 2. Mathematical Foundations

Let $G=(V,E)$ be simple, $\Delta = \Delta(G) = \max_{v} \deg(v)$.

**Reformulation via graph powers.** Let $L(G)$ be the line graph and $L(G)^2$ its square (edges joined when at distance $\le 2$). Then
$$
\chi'_s(G) \;=\; \chi\bigl(L(G)^2\bigr),
$$
so strong edge colouring is ordinary vertex colouring of a graph whose vertices are the edges of $G$. For $e=uv$, the number of edges conflicting with $e$ is at most
$$
\deg(u)+\deg(v)-2 + \sum_{w \in N(u)\setminus\{v\}}(\deg(w)-1) + \sum_{w\in N(v)\setminus\{u\}}(\deg(w)-1) \;\le\; 2\Delta^2-2\Delta,
$$
so $\Delta(L(G)^2) \le 2\Delta^2-2\Delta$ and greedy colouring gives the **trivial bound**
$$
\chi'_s(G) \;\le\; 2\Delta^2 - 2\Delta + 1 ,
$$
noted by Faudree, Gyárfás, Schelp and Tuza (1990). The conjecture asks to improve the leading constant from $2$ to $5/4$.

**Strong clique number.** A *strong clique* is a set of pairwise conflicting edges, i.e. a clique of $L(G)^2$; write $\omega'_s(G)=\omega(L(G)^2)$. Chung, Gyárfás, Trotter and Tuza (1990) proved the exact extremal statement
$$
\omega'_s(G) \;\le\;
\begin{cases}
\tfrac54\Delta^2 & \Delta\text{ even},\\
\tfrac14(5\Delta^2-2\Delta+1) & \Delta\text{ odd},
\end{cases}
$$
equivalently: a graph with maximum degree $\Delta$ in which no two edges span an induced $2K_2$ has at most that many edges. The Erdős–Nešetřil conjecture is exactly the assertion that this clique bound is also a **chromatic** bound, i.e. that $L(G)^2$ is "perfect enough" at the extremal value.

**Probabilistic apparatus.** Upper bounds beyond $2\Delta^2$ use the Lovász Local Lemma in its asymmetric form: if each bad event $A_i$ has $\Pr[A_i]\le p$ and depends on at most $d$ others with $ep(d+1)\le 1$, then $\Pr[\bigcap \overline{A_i}]>0$. Modern improvements use *local sparsity*: for a vertex $x$ of $L(G)^2$ let
$$
\text{(local density)}\quad \frac{e\bigl(N(x)\bigr)}{\binom{\deg x}{2}} ,
$$
and colour graphs where every neighbourhood induces at most $(1-\sigma)\binom{d}{2}$ edges with roughly $\bigl(1-c\,\sigma\bigr)\Delta/\ln(1/\ldots)$-type savings.

## 3. History & State of the Art (SOTA)

- **1985.** Erdős and Nešetřil pose the problem at a seminar in Prague, first asking whether $\chi'_s$ is bounded by $O(\Delta^2)$ and then proposing the exact constant $5/4$ after constructing the $C_5$ blow-up. Recorded in Erdős, *Problems and results in combinatorial analysis and graph theory* (Discrete Math. 72, 1988) and in the problem list of *Irregularities of Partitions* (Springer, 1989).
- **1990.** Faudree, Gyárfás, Schelp, Tuza record the greedy bound $2\Delta^2-2\Delta+1$ and formulate the bipartite variant $\chi'_s \le \Delta^2$.
- **1990.** Chung–Gyárfás–Trotter–Tuza settle the clique/extremal-edge version exactly.
- **1997.** Molloy and Reed give the first improvement of the leading constant: $\chi'_s(G)\le 1.998\Delta^2$ for $\Delta$ sufficiently large, via the Local Lemma applied to a partial random colouring plus a "wasted-pair" counting argument.
- **2018.** Bruhn and Joos: $\chi'_s(G)\le 1.93\Delta^2$ for large $\Delta$.
- **2018–2022.** Bonamy, Perrett and Postle: $1.835\Delta^2$ for large $\Delta$, using colouring of graphs with sparse neighbourhoods.
- **2021–2022.** Hurley, de Joannis de Verclos and Kang: $\chi'_s(G)\le 1.772\Delta^2$ for large $\Delta$ — the current record — from an improved local-density colouring procedure.

Small-$\Delta$ history runs in parallel: $\Delta=3$ was settled by Andersen (1992) and independently by Horák, Qing and Trotter (1993); $\Delta=4$ has been pushed from $23$ to $22$ (Cranston, 2006) to $21$ (Huang, Santana, Yu, 2018) against a conjectured $20$.

## 4. Partial Results / Verified Cases

| Case | Conjectured | Known | Reference |
|---|---|---|---|
| $\Delta = 2$ | $5$ | $5$ (tight on $C_5$) | elementary |
| $\Delta = 3$ | $10$ | $10$ — **proved** | Andersen 1992; Horák–Qing–Trotter 1993 |
| $\Delta = 4$ | $20$ | $\le 21$ | Huang–Santana–Yu 2018 |
| $\Delta$ large | $1.25\Delta^2$ | $\le 1.772\Delta^2$ | Hurley–de Joannis de Verclos–Kang 2022 |
| any $\Delta$ | — | $\le 2\Delta^2-2\Delta+1$ | Faudree et al. 1990 |

Further verified classes:

- **Clique version.** $\omega'_s(G)$ meets the conjectured bound exactly for all $\Delta$ (Chung–Gyárfás–Trotter–Tuza 1990). So no *local* counterexample exists.
- **$C_4$-free graphs.** $\chi'_s(G) = O(\Delta^2/\log \Delta)$ (Mahdian, 2000), far below $\tfrac54\Delta^2$; more generally graphs of girth $\ge 5$ and bounded-density neighbourhoods beat the conjecture asymptotically.
- **Subcubic planar multigraphs.** $\chi'_s \le 9$, confirming the Faudree–Gyárfás–Schelp–Tuza refinement (Kostochka, Li, Ruksasakchai, Santana, Wang, Yu, 2016).
- **Chordless / structurally sparse families.** Graphs with no induced cycle of length $\ge 4$, $K_4$-minor-free graphs, and bounded-treewidth graphs all satisfy stronger linear- or $\Delta^2$-free bounds.
- **Bipartite $G$ with parts of degree $\le \Delta_1,\Delta_2$**: the Brualdi–Quinn Massey conjecture $\chi'_s\le \Delta_1\Delta_2$ is verified for $\Delta_1 \le 2$ and for several sparse subfamilies; it implies the $\Delta^2$ bipartite bound, itself below $\tfrac54\Delta^2$.

## 5. Principal Obstacles

- **The gap is a constant, not an exponent.** Every known technique loses a constant factor; the target is a specific constant $5/4$, so no "soft" argument suffices. Improvements from $1.998$ to $1.772$ took 25 years and each step needed a new colouring procedure.
- **Local Lemma saturation.** LLL-based arguments need each edge to have many *repeated* colours in its conflict neighbourhood. In the extremal $C_5$ blow-up, the conflict graph $L(G)^2$ is a **clique** of size $\tfrac54\Delta^2$ — zero local sparsity, no slack for the probabilistic argument. The very configuration that forces the bound is the one where randomisation gives nothing.
- **Clique number $\ne$ chromatic number.** $L(G)^2$ is not perfect and is not known to be $\chi$-bounded with the right constant. Proving $\chi \le \omega$ for this family would suffice, but no structural theory (perfect graph, claw-free, quasi-line) applies: $L(G)^2$ can contain odd holes and induced $K_{1,3}$'s.
- **Discharging does not scale.** The $\Delta=3$ and $\Delta=4$ proofs are long reducible-configuration/discharging arguments whose case count grows superpolynomially in $\Delta$; they give no template for general $\Delta$.
- **Two-regime tension.** Graphs with locally dense neighbourhoods (near $C_5$ blow-ups) and locally sparse ones need opposite methods; current papers interpolate with a density parameter but the interpolation is lossy exactly at the extremal density.

## 6. The Gap

Proven asymptotically: $\chi'_s \le 1.772\,\Delta^2$ for $\Delta$ large. Conjectured: $1.25\,\Delta^2$. The gap is the constant interval $(1.25, 1.772]$ — a factor of about $1.42$.

Precisely, the missing step is: **show that every graph $G$ with $\Delta(G)=\Delta$ whose conflict graph $L(G)^2$ has clique number close to $\tfrac54\Delta^2$ is (near-)structurally a blow-up of $C_5$, and colour the remaining, locally sparse graphs by density-based methods.** Both halves are partly available — the extremal characterisation of $\omega'_s$ (Chung et al.) and the sparse-neighbourhood colouring (Bonamy–Perrett–Postle; Hurley et al.) — but no *stability* theorem links them: it is unknown whether $\omega'_s(G) \ge (1.25-\varepsilon)\Delta^2$ forces $C_5$-blow-up-like structure with $\varepsilon$ independent of $\Delta$. For finite $\Delta$ the gap is a single integer at $\Delta=4$: $20$ versus $21$.

## 7. Current Research (as of June 2026)

- **Local-density colouring.** The Hurley–de Joannis de Verclos–Kang framework (occupancy method plus hard-core model entropy) is the active engine; further constant improvements are expected to come from sharpening the occupancy-fraction analysis rather than new combinatorics. *(frontier — verify)* Reported refinements below $1.75\Delta^2$ circulate as preprints.
- **Small cases.** Groups around G. Yu (William & Mary) and M. Santana continue the $\Delta = 4$ attack; a claimed reduction from $21$ to $20$ would settle the first open exact case. *(frontier — verify)*
- **Strong clique stability.** Work by Cames van Batenburg, Kang and collaborators on strong cliques in graph classes (claw-free, $C_4$-free, bounded local density) targets exactly the structural half of Section 6.
- **List and correspondence versions.** Whether the strong list chromatic index obeys the same bound is open even asymptotically; techniques transfer from list colouring of squares.
- **Bipartite and planar refinements.** The Brualdi–Quinn Massey conjecture and planar variants (girth conditions, $\Delta$-dependent constants) are the most-published subfields, with contributions from groups in Bordeaux (Montassier, Raspaud), Prague, and China (Wang, Chen).

## 8. Future Work

- Prove a **stability theorem**: $\omega'_s(G) \ge (\tfrac54-\varepsilon)\Delta^2 \Rightarrow G$ contains a large $C_5$-blow-up-like structure; then use it as the base case of an induction.
- Settle $\Delta=4$ at $20$, and identify whether a computer-assisted discharging scheme can be made uniform in $\Delta$.
- Attack the **fractional** relaxation $\chi'_{s,f}(G) \le \tfrac54\Delta^2$; a fractional proof would be the first evidence that $5/4$ (rather than some intermediate constant) is the true colouring threshold.
- Determine whether the conjectured bound holds for **bipartite** graphs with the sharper $\Delta^2$ constant, which would isolate odd-cycle structure as the sole source of the extra $\tfrac14\Delta^2$.
- Push occupancy/entropy methods to handle the mixed regime where a graph is locally dense on part of its edge set and sparse elsewhere.

## 9. Key References

- **[Foundational]** P. Erdős. *Problems and results in combinatorial analysis and graph theory.* Discrete Mathematics **72** (1988), 81–92.
- **[Foundational]** F. R. K. Chung, A. Gyárfás, W. T. Trotter, Zs. Tuza. *The maximum number of edges in $2K_2$-free graphs of bounded degree.* Discrete Mathematics **81** (1990), 129–135.
- **[Foundational]** R. J. Faudree, A. Gyárfás, R. H. Schelp, Zs. Tuza. *The strong chromatic index of graphs.* Ars Combinatoria **29B** (1990), 205–211.
- **[Partial results]** L. D. Andersen. *The strong chromatic index of a cubic graph is at most 10.* Discrete Mathematics **108** (1992), 231–252.
- **[Partial results]** P. Horák, H. Qing, W. T. Trotter. *Induced matchings in cubic graphs.* Journal of Graph Theory **17** (1993), 151–160.
- **[SOTA lineage]** M. Molloy, B. Reed. *A bound on the strong chromatic index of a graph.* Journal of Combinatorial Theory Series B **69** (1997), 103–109.
- **[SOTA lineage]** H. Bruhn, F. Joos. *A stronger bound for the strong chromatic index.* Combinatorics, Probability and Computing **27** (2018), 21–43.
- **[SOTA lineage]** M. Bonamy, T. Perrett, L. Postle. *Colouring graphs with sparse neighbourhoods: bounds and applications.* Journal of Combinatorial Theory Series B **155** (2022), 130–164.
- **[SOTA / Recent]** E. Hurley, R. de Joannis de Verclos, R. J. Kang. *An improved procedure for colouring graphs of bounded local density.* Advances in Combinatorics (2022); preliminary version in Proc. SODA 2021.
- **[Small cases]** D. W. Cranston. *Strong edge-coloring of graphs with maximum degree 4 using 22 colors.* Discrete Mathematics **306** (2006), 2772–2778.
- **[Small cases]** M. Huang, M. Santana, G. Yu. *Strong chromatic index of graphs with maximum degree four.* Electronic Journal of Combinatorics **25**(3) (2018), \#P3.31.
- **[Planar]** A. V. Kostochka, X. Li, W. Ruksasakchai, M. Santana, T. Wang, G. Yu. *Strong chromatic index of subcubic planar multigraphs.* European Journal of Combinatorics **51** (2016), 380–397.
- **[Sparse]** M. Mahdian. *The strong chromatic index of $C_4$-free graphs.* Random Structures & Algorithms **17** (2000), 357–375.
- **[Survey]** T. R. Jensen, B. Toft. *Graph Coloring Problems.* Wiley-Interscience, 1995 (Problem 12.3, strong chromatic index).

## 10. Worked Example / Concrete Special Case

**The extremal $C_5$ blow-up at $\Delta = 4$.** Take $C_5$ with vertex classes $V_1,\dots,V_5$, each $|V_i| = 2$, and join every vertex of $V_i$ to every vertex of $V_{i+1}$ (indices mod 5). Call this $G = C_5[\overline{K_2}]$.

- **Degrees.** A vertex in $V_i$ has neighbours exactly $V_{i-1}\cup V_{i+1}$, so $\deg = 2+2 = 4$; hence $\Delta = 4$.
- **Edge count.** $|E| = \sum_{i=1}^{5}|V_i||V_{i+1}| = 5\cdot(2\cdot 2) = 20$.
- **All 20 edges pairwise conflict.** Let $e$ join $V_i,V_{i+1}$ and $f$ join $V_j,V_{j+1}$.
  - If $j=i$: $e,f$ lie between the same two classes; either they share an endpoint, or their endpoints $u\in V_i, v'\in V_{i+1}$ are adjacent — conflict.
  - If $j=i+1$: they meet class $V_{i+1}$; either they share a vertex or the two distinct vertices of $V_{i+1}$ are joined through $V_{i+2}$… more directly, the endpoint of $e$ in $V_i$ and the endpoint of $f$ in $V_{i+1}$ are adjacent — conflict.
  - If $j=i+2$: $e$ meets $V_{i+1}$, $f$ meets $V_{i+2}$, and $V_{i+1}$–$V_{i+2}$ is a complete join, so an edge connects them — conflict.
  Since indices run mod $5$, these three cases cover all pairs. So $L(G)^2 = K_{20}$.
- **Consequence.** No two edges can share a colour: $\chi'_s(G) = |E| = 20 = \tfrac54\cdot 4^2$.

So the conjecture is **tight** at $\Delta = 4$, and the general construction $C_5[\overline{K_{\Delta/2}}]$ gives $5(\Delta/2)^2 = \tfrac54\Delta^2$ for every even $\Delta$ (for $\Delta=2$ this is $C_5$ itself with $\chi'_s = 5$). Matching constructions for odd $\Delta$ give $\tfrac14(5\Delta^2-2\Delta+1)$; these are the extremal $2K_2$-free graphs of Chung–Gyárfás–Trotter–Tuza and are not plain blow-ups of $C_5$, which is why the odd formula differs.

Contrast this with what is proved: for $\Delta=4$ the best theorem is $\chi'_s \le 21$ (Huang–Santana–Yu 2018) and the greedy bound is $2\cdot16-8+1 = 25$. The whole difficulty of the conjecture is compressed into that single unit — showing no $\Delta = 4$ graph needs a $21$st colour.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*