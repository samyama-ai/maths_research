---
id: 07-combinatorics/erdos-rothschild-problem
title: "Erdős-Rothschild Problem"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Rothschild Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-rothschild-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fix integers $r \ge 2$ (number of colours) and $k \ge 3$ (clique order). For a graph $G$ on $n$ vertices, let
$$c_{k,r}(G) = \\#\{\chi : E(G) \to [r] \;:\; \text{no } K_k \subseteq G \text{ is monochromatic under } \chi\},$$
counting **all** $r$-colourings of $E(G)$, not necessarily proper, in which no copy of $K_k$ receives a single colour. Define
$$F(n,k,r) = \max_{|V(G)|=n} c_{k,r}(G).$$

**The problem (Erdős–Rothschild, 1974).** Determine $F(n,k,r)$ and the extremal graphs attaining it.

Every $K_k$-free graph $G$ admits all $r^{e(G)}$ colourings, so
$$F(n,k,r) \ \ge\ r^{\mathrm{ex}(n,K_k)} = r^{e(T_{k-1}(n))},$$
where $\mathrm{ex}(n,K_k)$ is the Turán number and $T_{k-1}(n)$ the balanced complete $(k-1)$-partite graph. **Erdős and Rothschild conjectured that equality holds for $r = 2$** (and Erdős later for $r=3$), i.e. that colour-counting does not reward putting cliques back into the host graph.

A complete solution for a pair $(k,r)$ means: an exact formula for $F(n,k,r)$ valid for all large $n$, together with the full list of extremal graphs. A disproof of the "Turán is extremal" form means exhibiting $G$ with $c_{k,r}(G) > r^{\mathrm{ex}(n,K_k)}$ — which is known to happen for all $r \ge 4$.

## 2. Mathematical Foundations

**Turán's theorem.** $\mathrm{ex}(n,K_k) = e(T_{k-1}(n)) = \left(1-\tfrac{1}{k-1}\right)\tfrac{n^2}{2} + O(1)$, with $T_{k-1}(n)$ the unique extremal graph.

**Colour patterns.** The asymptotics of $F(n,k,r)$ are controlled by an entropy-style optimisation. A *pattern* on $m$ parts is a pair $(\,\mathbf{a},\,\Phi\,)$ where $\mathbf{a}=(a_1,\dots,a_m)$, $a_i \ge 0$, $\sum a_i = 1$ gives part densities, and $\Phi = (\Phi_1,\dots,\Phi_r)$ assigns to each colour $s$ a graph $\Phi_s$ on vertex set $[m]$ (possibly with loops) that is $K_k$-free in the *blow-up* sense: the blow-up of $\Phi_s$ must contain no $K_k$. Colour $s$ is admissible on the pair $\{i,j\}$ iff $ij \in \Phi_s$. Writing $c_{ij} = \\#\{s : ij \in \Phi_s\}$, the number of colourings of the corresponding host is
$$\prod_{i<j} c_{ij}^{\,a_i a_j n^2}\cdot \prod_i c_{ii}^{\,a_i^2 n^2/2},$$
so one is led to
$$F(n,k,r) = 2^{(\kappa_{k,r}+o(1))\,n^2/2}, \qquad
\kappa_{k,r} \;=\; \max_{m,\mathbf{a},\Phi}\ \Big( \sum_{i<j} 2 a_i a_j \log_2 c_{ij} + \sum_i a_i^2 \log_2 c_{ii}\Big).$$
For $k=3$ each $\Phi_s$ must be triangle-free and loopless with no two adjacent looped vertices; the clean sub-case is $\Phi_s$ = complete bipartite graph induced by a bipartition of $[m]$.

**Baseline.** Taking $m=k-1$, $\mathbf{a}$ balanced and every colour allowed everywhere gives $\kappa_{k,r} \ge \left(1-\tfrac1{k-1}\right)\log_2 r$, i.e. the Turán bound $r^{\mathrm{ex}(n,K_k)}$.

**Tools.** The proofs rest on: (i) Szemerédi's regularity lemma plus the removal lemma, or (ii) the hypergraph container method, which shows that all $K_k$-free subgraphs of $K_n$ lie in few "almost-Turán" containers, and (iii) stability arguments of Erdős–Simonovits type upgrading approximate structure to exact structure.

## 3. History & State of the Art (SOTA)

- **1974.** Erdős and Rothschild pose the question (recorded in Erdős's problem papers, e.g. *Some new applications of probability methods to combinatorial analysis and graph theory*, 1974). Conjecture: $F(n,3,2)=2^{\lfloor n^2/4\rfloor}$.
- **1996.** Yuster proves the case $k=3$, $r=2$ for all $n \ge 6$: the Turán graph $T_2(n)$ is the unique extremal graph.
- **2004.** Alon, Balogh, Keevash and Sudakov prove the conjecture for **all $k \ge 3$ and $r \in \{2,3\}$**, $n$ large: $F(n,k,r) = r^{\mathrm{ex}(n,K_k)}$ with $T_{k-1}(n)$ the unique optimum. In the same paper they show the conjecture **fails for every $r \ge 4$**: $F(n,3,4) \ge 2^{(1/2+c)n^2}$ for some $c>0$, beating $4^{n^2/4}$.
- **2012.** Pikhurko and Yilma determine two exact non-Turán cases: $F(n,3,4)$ is attained by $T_4(n)$ and $F(n,4,4)$ by $T_9(n)$, for large $n$.
- **2017–2023.** Pikhurko, Staden and Yilma reduce the general problem to the finite-dimensional optimisation of Section 2 and prove an *exact stability* transfer: if the optimisation has a unique, "stable" optimum, the extremal graphs for large $n$ are exactly the corresponding complete multipartite blow-ups.
- **2019–.** Botler, Corsten, Dankovics, Frankl, Hàn, Jiménez and Skokan settle $k=3$, $r \in \{5,6\}$ for large $n$, again with complete multipartite extremal graphs whose number of parts exceeds $k-1$.
- **Variants.** Analogues are now standard for forbidden monochromatic: paths/matchings (Hoppen–Kohayakawa–Lefmann), general graphs $H$ (Lefmann–Person–Schacht), Boolean-lattice and set-system versions (Hoppen–Lefmann–Odermann; Das–Glebov–Sudakov–Tran), rainbow-free and Gallai-type constraints, and sum-free colourings of $[n]$ / abelian groups (Liu–Sharifzadeh–Staden).

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $k=3$, $r=2$ | $F = 2^{\lfloor n^2/4 \rfloor}$, extremal $T_2(n)$, all $n\ge 6$ | Yuster 1996 |
| all $k\ge3$, $r=2,3$ | $F = r^{\mathrm{ex}(n,K_k)}$, unique extremal $T_{k-1}(n)$, $n \ge n_0(k)$ | Alon–Balogh–Keevash–Sudakov 2004 |
| $r \ge 4$, $k = 3$ | Turán bound is **false**: $F(n,3,r) \ge 2^{(1/2+c)n^2}$ | ABKS 2004 |
| $k=3$, $r=4$ | extremal graph $T_4(n)$, $n$ large; $F = 2^{(\log_2 324/16 + o(1))n^2}$ | Pikhurko–Yilma 2012 |
| $k=4$, $r=4$ | extremal graph $T_9(n)$, $n$ large | Pikhurko–Yilma 2012 |
| $k=3$, $r=5,6$ | exact, extremal graphs complete multipartite with more than $2$ parts | Botler–Corsten–Dankovics–Frankl–Hàn–Jiménez–Skokan 2019+ |
| general $(k,r)$ | asymptotic reduction to the finite optimisation; exact answer whenever that optimisation has a stable unique optimum | Pikhurko–Staden–Yilma 2017; Pikhurko–Staden 2023 |
| monochromatic-$H$ variants | asymptotics for all $H$ with $\chi(H)\ge3$ and $r=2,3$ | Lefmann–Person–Schacht 2010s |

Small $n$ outside the "large $n$" regime is checked only by direct computation; the $r=2$, $k=3$ case is the only one verified down to a concrete threshold ($n \ge 6$).

## 5. Principal Obstacles

- **The optimisation is not solved.** Even asymptotically, $\kappa_{k,r}$ is the value of a maximisation over an unbounded number of parts $m$, all $r$-tuples of blow-up-$K_k$-free pattern graphs, and all density vectors. There is no a priori bound on $m$ for general $(k,r)$, and no convexity: the objective $\sum 2a_ia_j\log_2 c_{ij}$ is a non-concave polynomial-in-logs, so local optima abound and numerical search gives lower bounds only.
- **No entropy/product bound is tight.** Shearer/Kruskal–Katona style entropy bounds on the number of colourings lose a constant in the exponent precisely when $r \ge 4$, where the extra colours are "spent" on more parts rather than more edges.
- **Regularity gives only $n \ge \mathrm{tower}$.** All exact results proceed via regularity or containers plus stability, so thresholds $n_0(k,r)$ are astronomically large or unspecified. This is why no case beyond $k=3, r=2$ has an explicit $n_0$.
- **Stability can fail.** The Pikhurko–Staden transfer requires the optimal pattern to be *strictly* optimal and locally rigid. When several patterns tie asymptotically — expected for large $r$ where near-balanced allocations of $r\cdot(\text{pairs per colour})$ incidences over $\binom m2$ pairs are numerous — no exact result follows.
- **Counting vs. structure.** Unlike Turán problems, a single dense monochromatic-free colouring family can compensate for the loss of $\Theta(n^2)$ edges; local moves that improve a graph's edge count can decrease its colouring count, so no monotone extremal invariant is available.

## 6. The Gap

Proven: $r \le 3$ (all $k$), and the sporadic exact points $(k,r) \in \{(3,4),(4,4),(3,5),(3,6)\}$. Unknown: essentially everything else, starting with $(k,r) = (3,7)$ and $(4,5)$.

The precise missing step has two layers:

1. **Solve the pattern optimisation.** Show that the maximum in $\kappa_{k,r}$ is attained on a bounded number of parts $m \le m_0(k,r)$ — even a computable bound would make each $(k,r)$ a finite (if large) computation — and identify the maximiser.
2. **Bridge asymptotic to exact.** Verify the strict-optimality hypothesis of the stability theorem for the identified maximiser. Currently this is done ad hoc, case by case, and there is no general criterion guaranteeing it.

A structural conjecture that would close the gap: for every $k,r$ and large $n$ the extremal graph is *complete multipartite* (with possibly unbalanced parts). This is proved only in the settled cases.

## 7. Current Research (as of June 2026)

- **Warwick / Oxford / Illinois school** (Pikhurko, Staden, Balogh and coauthors): pushing the container-plus-stability machinery to general $(k,r)$ and to unbalanced multipartite optima; also to "few monochromatic copies" relaxations where $\le t$ monochromatic $K_k$'s are permitted.
- **São Paulo / LSE group** (Hàn, Jiménez, Skokan, Botler and coauthors): explicit optimisation for $k=3$ and $r=7,8$, where the candidate optima come from bipartition systems on $8$ or more parts *(frontier — verify)*.
- **Arithmetic analogues**: maximum number of sum-free or solution-free $r$-colourings of $[n]$ and of abelian groups (Liu, Sharifzadeh, Staden and successors), where container methods for arithmetic structures replace graph regularity.
- **Hypergraph Erdős–Rothschild**: colourings of $K_n^{(3)}$ avoiding monochromatic tetrahedra remain open even for $r=2$, obstructed by the unresolved Turán density $\pi(K_4^{(3)})$.
- **Algorithmic/computational**: semidefinite (flag algebra) relaxations of the pattern optimisation, used to certify upper bounds on $\kappa_{3,r}$ for small $r$ *(frontier — verify)*.

## 8. Future Work

- Prove a general bound $m \le m_0(k,r)$ on the number of parts in an optimal pattern, reducing each case to a finite search.
- Establish the "extremal graphs are complete multipartite" conjecture for all $(k,r)$, independently of solving the optimisation.
- Determine the growth of $\kappa_{3,r}$ as $r\to\infty$: is $\kappa_{3,r} = \log_2 r - \Theta(1)$, and what is the optimal number of parts as a function of $r$?
- Replace regularity by containers throughout to obtain explicit, ideally polynomial, thresholds $n_0(k,r)$.
- Extend exact results to forbidden monochromatic $H$ with $\chi(H)=2$, where the Turán number is $o(n^2)$ and the whole framework must be rebuilt.

## 9. Key References

- **[Foundational]** P. Erdős. *Some new applications of probability methods to combinatorial analysis and graph theory.* Proc. 5th Southeastern Conf. on Combinatorics, Graph Theory and Computing, Congressus Numerantium, 1974. (Statement of the Erdős–Rothschild question.)
- **[Foundational]** R. Yuster. *The number of edge colorings with no monochromatic triangle.* Journal of Graph Theory 21 (1996), 441–452.
- **[Foundational]** N. Alon, J. Balogh, P. Keevash, B. Sudakov. *The number of edge colorings with no monochromatic cliques.* Journal of the London Mathematical Society 70 (2004), 273–288.
- **[SOTA]** O. Pikhurko, Z. B. Yilma. *The maximum number of $K_3$-free and $K_4$-free edge 4-colourings.* Journal of the London Mathematical Society 85 (2012), 593–615.
- **[SOTA]** O. Pikhurko, K. Staden, Z. B. Yilma. *The Erdős–Rothschild problem on edge-colourings with forbidden monochromatic cliques.* Mathematical Proceedings of the Cambridge Philosophical Society 163 (2017), 341–356.
- **[SOTA]** O. Pikhurko, K. Staden. *Stability for the Erdős–Rothschild problem.* Forum of Mathematics, Sigma 11 (2023), e23.
- **[SOTA]** F. Botler, J. Corsten, A. Dankovics, N. Frankl, H. Hàn, A. Jiménez, J. Skokan. *Maximum number of triangle-free edge colourings with five and six colours.* Acta Mathematica Universitatis Comenianae 88 (2019), 495–499 (extended abstract; full version in journal form).
- **[Related]** H. Lefmann, Y. Person, M. Schacht. *A structural result for hypergraphs with many restricted edge colorings.* Journal of Combinatorics 1 (2010), 441–475.
- **[Related]** H. Liu, M. Sharifzadeh, K. Staden. *On the maximum number of integer colourings with forbidden monochromatic sums.* Electronic Journal of Combinatorics 28 (2021), \#P1.59.
- **[Survey]** J. Balogh, R. Morris, W. Samotij. *The method of hypergraph containers.* Proc. International Congress of Mathematicians 2018, Vol. IV, 3059–3092.

## 10. Worked Example / Concrete Special Case

**Why four colours break the Turán bound ($k=3$, $r=4$).**

*Turán candidate.* $G = T_2(n) = K_{n/2,n/2}$ is triangle-free, so every one of its $4^{n^2/4}$ colourings is admissible:
$$4^{n^2/4} = 2^{n^2/2} = 2^{0.5\,n^2}.$$

*Better candidate.* Let $G = T_4(n)$, the complete $4$-partite graph with parts $V_1,\dots,V_4$ of size $n/4$; it contains many triangles, so not all colourings survive. Build admissible colourings from a *pattern*: to each colour $s \in \{1,2,3,4\}$ assign a bipartition of $\{1,2,3,4\}$ and allow colour $s$ only on pairs crossing that bipartition. Any colour class is then contained in a blow-up of a bipartite graph, hence triangle-free, hence no monochromatic $K_3$ appears.

Take the three perfect bipartitions
$$P_1 = 12|34,\quad P_2=13|24,\quad P_3=14|23,$$
each of which crosses exactly $4$ of the $\binom42 = 6$ part-pairs. Assign $P_1,P_2,P_3$ to colours $1,2,3$ and reuse $P_1$ for colour $4$. Counting, for each part-pair $\{i,j\}$, how many colours are admissible:

| pair | $\{1,2\}$ | $\{3,4\}$ | $\{1,3\}$ | $\{2,4\}$ | $\{1,4\}$ | $\{2,3\}$ |
|---|---|---|---|---|---|---|
| colours $c_{ij}$ | 2 | 2 | 3 | 3 | 3 | 3 |

(The pairs inside a block of $P_1$, namely $\{1,2\}$ and $\{3,4\}$, lose colours $1$ and $4$; the other four pairs lose exactly one colour each.) Total incidences check: $4 \times 4 = 16 = 2+2+3+3+3+3$. Each part-pair spans $(n/4)^2 = n^2/16$ edges, so the number of colourings obtained is
$$\prod_{i<j} c_{ij}^{\,n^2/16} = \left(2^2\cdot 3^4\right)^{n^2/16} = 324^{\,n^2/16} = 2^{(\log_2 324)\,n^2/16} = 2^{8.340\,n^2/16} = 2^{0.5212\,n^2}.$$

Since $0.5212 > 0.5$, for large $n$
$$c_{3,4}(T_4(n)) \ \ge\ 2^{0.521\,n^2} \ >\ 2^{0.5\,n^2} \ =\ 4^{\mathrm{ex}(n,K_3)},$$
disproving the Turán form of the conjecture at $r=4$. Pikhurko and Yilma showed this construction is optimal: $F(n,3,4) = 324^{(1+o(1))n^2/16}$ with $T_4(n)$ the unique extremal graph for large $n$.

*Contrast at $r=3$.* Repeating the count with three colours and the three bipartitions $P_1,P_2,P_3$ gives $c_{ij}=2$ for every pair, hence $2^{6n^2/16}=2^{0.375\,n^2}$, whereas $T_2(n)$ gives $3^{n^2/4}=2^{0.396\,n^2}$. The Turán graph wins — matching the Alon–Balogh–Keevash–Sudakov theorem, and showing the crossover sits exactly between $r=3$ and $r=4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*