---
id: 07-combinatorics/jaegers-8-flow-conjecture
title: "Jaeger's 8-Flow Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jaeger's 8-Flow Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/jaegers-8-flow-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The statement historically called the **8-flow conjecture** — every bridgeless graph admits a nowhere-zero $8$-flow — is **no longer open**. It was proved independently by Kilpatrick (1975) and Jaeger (1979) and is now **Jaeger's 8-flow theorem**. This page tracks the conjectural program that survives it, which is what the name is used for in current literature:

- **(A) Descent below 8.** Seymour (1981) reduced $8 \to 6$. Tutte's **5-flow conjecture** (1954) — every bridgeless graph has a nowhere-zero $5$-flow — is the open endpoint and remains untouched at the value $6$ after 45 years.
- **(B) Jaeger's circular flow conjecture** (1984/1988), the connectivity-graded generalization of the 8-flow theorem: for every $p \ge 1$, every $4p$-edge-connected graph has a mod $(2p+1)$-orientation, equivalently circular flow number $\phi_c(G) \le \frac{2p+1}{p}$. This is **false in general**: Han, Li, Wu and Zhang (2018) built counterexamples for every $p \ge 3$. The cases $p = 1$ (Tutte's 3-flow conjecture with connectivity 4) and $p = 2$ remain **open**.

A complete resolution of (A) means exhibiting a nowhere-zero $5$-flow in every bridgeless graph, or a bridgeless graph with flow number $6$. A complete resolution of (B) means settling $p \in \{1,2\}$ and determining, for each $p \ge 3$, the least $f(p)$ such that $f(p)$-edge-connectivity forces a mod $(2p+1)$-orientation.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite graph, $D$ an orientation of $E$, and $A$ an abelian group. A map $f : E \to A$ is an **$A$-flow** under $D$ if Kirchhoff's law holds at every vertex:

$$\sum_{e \in \partial^{+}(v)} f(e) \;-\; \sum_{e \in \partial^{-}(v)} f(e) \;=\; 0 \qquad \text{for all } v \in V .$$

It is **nowhere-zero** if $f(e) \neq 0$ for all $e$. For an integer $k \ge 2$, a **nowhere-zero $k$-flow** is a $\mathbb{Z}$-flow with $0 < |f(e)| \le k-1$.

**Theorem (Tutte, 1954).** For $|A| = k$, $G$ has a nowhere-zero $A$-flow iff it has a nowhere-zero $k$-flow. The count is a polynomial in $k$ — the flow polynomial $F_G(k)$, the dual of the chromatic polynomial. Hence existence depends only on $|A|$, not on the group structure.

The **flow number** is $\phi(G) = \min\{k : G \text{ has a nowhere-zero } k\text{-flow}\}$; $\phi(G) < \infty$ iff $G$ is bridgeless. Duality: for a connected plane graph, $\phi(G) = \chi(G^{*})$, so the Four Colour Theorem is exactly "planar bridgeless $\Rightarrow$ 4-flow".

**Circular flows.** For real $r \ge 2$, a **circular nowhere-zero $r$-flow** is a real flow with $1 \le |f(e)| \le r-1$; $\phi_c(G) = \min\{r\}$ is attained and rational, and $\phi(G) = \lceil \phi_c(G) \rceil$ (Goddyn–Tarsi–Zhang, 1998).

**Modular orientations.** $D$ is a **mod $(2p+1)$-orientation** if
$$d^{+}_{D}(v) - d^{-}_{D}(v) \equiv 0 \pmod{2p+1} \quad \forall v \in V .$$
Equivalently $G$ carries a nowhere-zero $\mathbb{Z}_{2p+1}$-flow with all values $\equiv 1$, and equivalently $\phi_c(G) \le \frac{2p+1}{p}$.

**Jaeger's circular flow conjecture (CFC$_p$).** Every $4p$-edge-connected graph has a mod $(2p+1)$-orientation.

**Key structural input.** Nash-Williams–Tutte: $G$ has $k$ edge-disjoint spanning trees iff every partition $P$ of $V$ satisfies $\|E_G(P)\| \ge k(|P|-1)$. A $2k$-edge-connected graph has $k$ edge-disjoint spanning trees. Doubling all edges of a bridgeless $G$ yields a $4$-edge-connected graph, hence two edge-disjoint spanning trees — the engine of the 8-flow theorem.

**Theorem (Kilpatrick 1975; Jaeger 1979).** Every bridgeless $G$ has three even subgraphs $C_1,C_2,C_3$ with $E = C_1 \cup C_2 \cup C_3$; the indicator map $e \mapsto (\mathbb{1}_{C_1}(e),\mathbb{1}_{C_2}(e),\mathbb{1}_{C_3}(e))$ is a nowhere-zero $\mathbb{Z}_2^3$-flow, so $\phi(G) \le 8$.

**Theorem (Seymour 1981).** Every bridgeless $G$ has a nowhere-zero $\mathbb{Z}_2 \times \mathbb{Z}_3$-flow, so $\phi(G) \le 6$.

## 3. History & State of the Art (SOTA)

- **1949–1954.** Tutte introduces flows as the dual of colouring and states the 5-flow, 4-flow and 3-flow conjectures.
- **1975.** F. Kilpatrick's Cape Town thesis proves the 8-flow bound.
- **1979.** F. Jaeger, *Flows and generalized coloring theorems in graphs* (JCTB 26), gives the independent proof via three even subgraphs; the name attaches to him.
- **1981.** P. D. Seymour, *Nowhere-zero 6-flows* (JCTB 30, 130–135): $\phi(G) \le 6$. This is still the record for general bridgeless graphs.
- **1984/1988.** Jaeger poses the circular flow conjecture in *Nowhere-zero flow problems* (Selected Topics in Graph Theory 3), unifying the 8-flow theorem with the 3-flow conjecture as $p=1$.
- **1992.** Jaeger, Linial, Payan, Tarsi introduce **group connectivity** ($A$-connectivity), a nonhomogeneous strengthening, and conjecture every $5$-edge-connected graph is $\mathbb{Z}_3$-connected.
- **2012.** Thomassen proves the **weak 3-flow conjecture**: $8$-edge-connectivity forces a nowhere-zero $3$-flow; his method also gives $\phi_c \le \frac{2p+1}{p}$ for connectivity roughly $(2p+1)^2$ — the first finite bound for all $p$.
- **2013.** Lovász, Thomassen, Wu, Zhang sharpen this to **$6$-edge-connected $\Rightarrow$ $\mathbb{Z}_3$-connected**, and $(3p-1)$-... more precisely $6p$-edge-connectivity forces a mod $(2p+1)$-orientation.
- **2018.** Han, Li, Wu, Zhang, *Counterexamples to Jaeger's circular flow conjecture* (JCTB 131, 1–11): for each $p \ge 3$ there are $4p$-edge-connected (indeed $(4p+1)$-edge-connected for large $p$ in later refinements) graphs with no mod $(2p+1)$-orientation.

## 4. Partial Results / Verified Cases

| Class / parameter | Result |
|---|---|
| All bridgeless graphs | $\phi(G) \le 6$ (Seymour 1981); $\le 8$ (Jaeger/Kilpatrick) |
| Planar bridgeless | $\phi(G) \le 4$ (Four Colour Theorem, Appel–Haken 1977; Robertson–Sanders–Seymour–Thomas 1997) |
| Planar, girth $\ge 5$ / $4$-edge-connected planar | $\phi(G) \le 3$ (Grötzsch 1959, dually) |
| Petersen-minor-free cubic | $\phi(G) \le 4$ (Robertson–Seymour–Thomas, *Excluded minors in cubic graphs*, JCTB 138, 2019) |
| $4$-edge-connected | $\phi(G) \le 4$ (Jaeger 1979, via two edge-disjoint spanning trees) |
| $6$-edge-connected | $\mathbb{Z}_3$-connected, hence $\phi \le 3$ (Lovász–Thomassen–Wu–Zhang 2013) |
| $6p$-edge-connected | mod $(2p+1)$-orientation exists (LTWZ 2013) |
| Graphs with a Hamiltonian path, Cayley graphs on abelian/nilpotent groups, vertex-transitive graphs of certain orders | $\phi \le 4$ or $\le 3$ in many families (Alspach–Liu–Zhang; Nánásiová–Škoviera) |
| CFC$_p$, $p \ge 3$ | **False** (Han–Li–Wu–Zhang 2018) |
| CFC$_1$ (Tutte 3-flow with $\lambda \ge 4$), CFC$_2$ ($\lambda \ge 8 \Rightarrow$ mod 5) | **Open** |
| 5-flow conjecture, minimal counterexample | Must be a cyclically $6$-edge-connected cubic graph of girth $\ge 9$ (Kochol 2004–2010); verified by computation for all snarks up to $36$ vertices |

## 5. Principal Obstacles

- **The parity barrier at 6 → 5.** Seymour's proof builds a $\mathbb{Z}_2 \times \mathbb{Z}_3$-flow by a greedy expansion over a "3-edge-connected splitting" structure; $6 = 2 \cdot 3$ is exactly where the group factorizes. $5$ is prime, so no analogous product decomposition exists, and every known constructive flow proof (Jaeger's tree-packing, Seymour's induction, Kochol's superposition) is fundamentally a factorization argument.
- **Non-monotonicity of flow number under minors.** $\phi$ is minor-monotone only for contraction/deletion of specific kinds; there is no Robertson–Seymour-style excluded-minor characterization to run structure theory against, except conjecturally (Tutte's 4-flow conjecture).
- **Edge-connectivity is the wrong parameter beyond $p=2$.** The Han–Li–Wu–Zhang counterexamples show that mod $(2p+1)$-orientation is obstructed by *global* quantities — the modular deficiency accumulates over large odd-order vertex sets — that $4p$-edge-connectivity does not control. The correct invariant (a partition-type or fractional-orientation condition) is unidentified.
- **Thomassen-type induction loses a constant factor.** The contraction-and-lift induction underlying $6$-edge-connected $\Rightarrow$ $\mathbb{Z}_3$-connected needs a degree surplus to keep the hypothesis alive after contracting; pushing $6 \to 5$ or $4$ breaks the induction at the first contraction, since the reduced graph can drop below the threshold.
- **Algebraic/topological methods do not see the constraint.** Flow polynomials $F_G(5)$ can be computed but there is no known positivity certificate; Combinatorial-Nullstellensatz and Alon–Tarsi arguments give group connectivity results only for large degrees.

## 6. The Gap

- **For (A):** proven $\phi(G) \le 6$; conjectured $\phi(G) \le 5$. The gap is a single integer, but structurally it is the passage from a *composite* group ($\mathbb{Z}_2 \times \mathbb{Z}_3$, where flows can be assembled coordinate-wise) to the *simple* group $\mathbb{Z}_5$, where no coordinate decomposition exists. No proof technique currently produces a nowhere-zero flow in a group of prime order $> 3$ for a general bridgeless graph.
- **For (B):** proven $6p$-edge-connectivity suffices; disproved at $4p$ for $p \ge 3$. The gap is the interval $[4p+1, 6p-1]$ — the true threshold $f(p)$ is unknown for every $p \ge 2$, and even its asymptotic order ($\Theta(p)$ with what constant?) is open. For $p=1$ the gap is connectivity $4$ (conjectured) versus $6$ (proved).

## 7. Current Research (as of June 2026)

- **Threshold determination for modular orientations.** Groups around Hong-Jian Lai (West Virginia), Cun-Quan Zhang (West Virginia), Miaomiao Han and Jiaao Li (Nankai) are narrowing $f(p)$; the working belief is $f(p) = 4p + \Theta(1)$ is false and $f(p) \ge 4p + \Omega(p)$ *(frontier — verify)*.
- **Group connectivity.** The Jaeger–Linial–Payan–Tarsi conjecture that $5$-edge-connectivity forces $\mathbb{Z}_3$-connectivity is the main live descendant of CFC$_1$; partial results exist for graphs with bounded independence number and for line graphs.
- **Signed and bidirected graphs.** Bouchet's 6-flow conjecture for signed graphs is the analogue programme; DeVos, Rollová, Šámal and Kaiser have pushed bounds (currently $11$-flows for flow-admissible signed graphs, improving Seymour-type $12$).
- **Snark structure and computer search.** Brinkmann, Goedgebeur, Hägglund and Markström's snark catalogue is used to test 5-flow and cycle-double-cover statements exhaustively; no counterexample to the 5-flow conjecture in any generated family.
- **Matroid generalizations.** Flow conjectures for regular and near-regular matroids (Walton–Welsh; recent work by Goddyn and collaborators) are pursued as a potentially easier abstraction.

## 8. Future Work

- Find any proof of a nowhere-zero $5$-flow for a natural infinite class not covered by 4-flow results — e.g. all cubic graphs of girth $\ge 6$, or all graphs of bounded genus.
- Identify the correct connectivity-free obstruction to mod $(2p+1)$-orientations, generalizing the Han–Li–Wu–Zhang construction into a characterization.
- Prove $5$-edge-connected $\Rightarrow$ $\mathbb{Z}_3$-connected, closing one unit of the LTWZ bound; Thomassen has singled this out as the most tractable next step.
- Relate the 5-flow conjecture to the Cycle Double Cover conjecture and the Berge–Fulkerson conjecture, which are known to imply flow statements for snarks.
- Develop a flow analogue of the discharging method that certifies $F_G(5) > 0$ directly.

## 9. Key References

- **[Foundational]** W. T. Tutte. *A contribution to the theory of chromatic polynomials.* Canadian Journal of Mathematics 6 (1954), 80–91.
- **[Foundational]** F. Jaeger. *Flows and generalized coloring theorems in graphs.* Journal of Combinatorial Theory, Series B 26 (1979), 205–216.
- **[Foundational]** F. Kilpatrick. *Tutte's first colour-cycle conjecture.* PhD thesis, University of Cape Town, 1975.
- **[Foundational]** P. D. Seymour. *Nowhere-zero 6-flows.* Journal of Combinatorial Theory, Series B 30 (1981), 130–135.
- **[Foundational]** F. Jaeger. *Nowhere-zero flow problems.* In L. W. Beineke, R. J. Wilson (eds.), Selected Topics in Graph Theory 3, Academic Press, 1988, 71–95.
- **[Foundational]** F. Jaeger, N. Linial, C. Payan, M. Tarsi. *Group connectivity of graphs — a nonhomogeneous analogue of nowhere-zero flow properties.* JCTB 56 (1992), 165–182.
- **[SOTA / Recent]** C. Thomassen. *The weak 3-flow conjecture and the weak circular flow conjecture.* JCTB 102 (2012), 521–529.
- **[SOTA / Recent]** L. M. Lovász, C. Thomassen, Y. Wu, C.-Q. Zhang. *Nowhere-zero 3-flows and modulo k-orientations.* JCTB 103 (2013), 587–598.
- **[SOTA / Recent]** M. Han, J. Li, Y. Wu, C.-Q. Zhang. *Counterexamples to Jaeger's circular flow conjecture.* JCTB 131 (2018), 1–11.
- **[SOTA / Recent]** N. Robertson, P. D. Seymour, R. Thomas. *Excluded minors in cubic graphs.* JCTB 138 (2019), 219–285.
- **[Survey]** C.-Q. Zhang. *Integer Flows and Cycle Covers of Graphs.* Marcel Dekker, 1997.
- **[Survey]** C.-Q. Zhang. *Circuit Double Cover of Graphs.* Cambridge University Press, LMS Lecture Note Series 399, 2012.
- **[Survey]** L. A. Goddyn, M. Tarsi, C.-Q. Zhang. *On $(k,d)$-colorings and fractional nowhere-zero flows.* Journal of Graph Theory 28 (1998), 155–161.
- **[Survey]** R. Diestel. *Graph Theory,* 5th ed., Springer GTM 173, 2017, Chapter 6 ("Flows").

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$.** Vertices $u_0,\dots,u_4$ (outer $5$-cycle $u_i u_{i+1}$), $v_0,\dots,v_4$ (inner pentagram $v_i v_{i+2}$), spokes $u_i v_i$; indices mod $5$; $|E| = 15$.

*Step 1 — an explicit nowhere-zero $8$-flow via Jaeger's construction.* Exhibit three even subgraphs (each a disjoint union of cycles) covering $E$:

- $C_1$ = outer $5$-cycle $\cup$ inner pentagram (a $2$-factor). Covers all $10$ non-spoke edges.
- $C_2$ = the $6$-cycle $u_0 u_1 v_1 v_4 v_2 v_0 u_0$ (check: $v_1 v_4$ and $v_4 v_2$ and $v_2 v_0$ are pentagram edges). Covers spokes $u_0v_0$, $u_1v_1$.
- $C_3$ = the $2$-factor $(u_2 u_3 v_3 v_0 v_2 u_2) \sqcup (u_0 u_1 v_1 v_4 u_4 u_0)$. Covers spokes $u_2v_2$, $u_3v_3$, $u_4v_4$ (and $u_1v_1$).

Every edge lies in at least one $C_i$, so $f(e) = (\mathbb{1}_{C_1}(e), \mathbb{1}_{C_2}(e), \mathbb{1}_{C_3}(e)) \in \mathbb{Z}_2^3$ is nowhere zero, and each coordinate satisfies Kirchhoff's law mod $2$ because even subgraphs have all degrees even. Since $|\mathbb{Z}_2^3| = 8$, Tutte's theorem converts this to an integer nowhere-zero $8$-flow. Hence $\phi(P) \le 8$.

*Step 2 — the descent stops at $5$.* For a cubic graph, $\phi(G) \le 4$ iff $G$ is $3$-edge-colourable (a proper $3$-edge-colouring by $\mathbb{Z}_2^2 \setminus \{0\}$ is exactly a nowhere-zero $\mathbb{Z}_2^2$-flow, since at each vertex the three distinct nonzero elements sum to $0$). The Petersen graph is the smallest snark: it is not $3$-edge-colourable, so $\phi(P) \ge 5$. A nowhere-zero $5$-flow exists (Seymour's theorem gives $6$; direct construction gives $5$), so
$$\phi(P) = 5, \qquad \phi_c(P) = 5 .$$

*Step 3 — what this shows about the gap.* $P$ is $3$-edge-connected but not $4$-edge-connected, so it is outside the $4$-edge-connected $\Rightarrow$ $4$-flow regime, and it attains the value the 5-flow conjecture asserts is maximal. Every known potential counterexample to the 5-flow conjecture must be a snark; $P$ is the archetype, and no snark with $\phi = 6$ has ever been found. Conversely, $P$ has no mod $5$-orientation constraint issue but illustrates why edge-connectivity alone is the wrong lever: CFC$_2$ asks for $8$-edge-connectivity to force $\phi_c \le 5/2$, a hypothesis $P$ fails by a wide margin while still achieving $\phi_c = 5$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*