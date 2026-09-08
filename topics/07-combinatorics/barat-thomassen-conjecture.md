---
id: 07-combinatorics/barat-thomassen-conjecture
title: "Barát–Thomassen Tree Decomposition Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Barát–Thomassen Tree Decomposition Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/barat-thomassen-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Barát–Thomassen, 2006).** For every tree $T$ there exists a natural number $k_T$ such that every $k_T$-edge-connected graph $G$ with $|E(G)| \equiv 0 \pmod{|E(T)|}$ has a **$T$-decomposition**: a partition of $E(G)$ into edge sets, each inducing a subgraph isomorphic to $T$.

Two conditions are clearly necessary. Divisibility of $|E(G)|$ by $|E(T)|$ is forced by counting. Some connectivity requirement is forced by examples: the claw $K_{1,3}$ has $3$ edges but no decomposition into paths of length $3$, and arbitrarily large trees of size divisible by $3$ share this defect. The content of the conjecture is that a **single** finite edge-connectivity threshold, depending on $T$ alone and not on $G$, removes every obstruction.

A complete proof must supply $k_T$ for all trees; a disproof must exhibit a tree $T$ and, for every $k$, a $k$-edge-connected graph of size divisible by $|E(T)|$ with no $T$-decomposition. The existential form was **settled affirmatively** by Bensmail, Harutyunyan, Le, Merker and Thomassé (JCTB 2017). What remains open is quantitative: the growth rate of the optimal $k_T$, and the conjectured replacement of edge-connectivity by a minimum-degree condition.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite multigraph. For $X\subseteq V$ write $\partial_G(X)$ for the edge cut between $X$ and $V\setminus X$. $G$ is **$k$-edge-connected** if $|\partial_G(X)|\ge k$ for every $\emptyset \ne X \subsetneq V$.

An **$H$-decomposition** of $G$ is a family $\{H_1,\dots,H_t\}$ of subgraphs with
$$E(G)=\bigsqcup_{i=1}^{t} E(H_i), \qquad H_i \cong H \ \ \text{for all } i,$$
so necessarily $t=|E(G)|/|E(H)|$.

Fix a tree $T$ with $|E(T)|=k$. Define
$$k_T := \min\{\,m \in \mathbb{N} : \text{every } m\text{-edge-connected } G \text{ with } k \mid |E(G)| \text{ has a } T\text{-decomposition}\,\}.$$
The conjecture asserts $k_T < \infty$.

**Orientation machinery.** An orientation $D$ of $G$ is a **mod-$p$ orientation** if
$$d_D^+(v) - d_D^-(v) \equiv 0 \pmod p \qquad \text{for all } v\in V.$$
Since $d^+(v)+d^-(v)=d(v)$, this gives $2d^+(v)\equiv d(v) \pmod p$. For $p=3$, mod-$3$ orientations exist iff $G$ has a nowhere-zero $3$-flow (Tutte). The key enabling theorem is Thomassen's **weak $3$-flow theorem**: every $8$-edge-connected graph has a nowhere-zero $3$-flow (JCTB 2012), improved to **$6$-edge-connected** by Lovász, Thomassen, Wu and Zhang (JCTB 2013), who proved more generally that every $(3p-3)$-edge-connected graph ($p$ odd) has a mod-$p$ orientation.

**Fractional relaxation.** A $T$-decomposition is an integral solution to the set-partition system
$$\sum_{\substack{C \in \mathcal{C}_T(G) \\ e \in E(C)}} x_C = 1 \quad (e \in E(G)), \qquad x_C \in \{0,1\},$$
where $\mathcal{C}_T(G)$ is the set of copies of $T$ in $G$. High edge-connectivity makes the fractional relaxation easy; the difficulty is rounding.

**Degree version.** Bensmail, Harutyunyan, Le and Thomassé conjecture a constant $c$, independent of $T$, such that every $c$-edge-connected graph $G$ with $\delta(G)\ge |E(T)|$ and $|E(T)| \mid |E(G)|$ has a $T$-decomposition. The degree hypothesis is necessary: a vertex of degree $1$ in $G$ can be covered only by a leaf edge of a copy of $T$, and repeated low-degree vertices create local parity obstructions.

## 3. History & State of the Art (SOTA)

- **2006.** János Barát and Carsten Thomassen state the conjecture in *Claw-decompositions and Tutte-orientations* (J. Graph Theory 52, 135–146). Their motivation is the case $T=K_{1,3}$, which they tie directly to Tutte-orientations and hence to Tutte's $3$-flow conjecture; they show that claw decompositions of planar graphs with all degrees divisible by $3$ are governed by the same orientation questions.
- **2008.** Thomassen proves the conjecture for paths of length $3$ (J. Graph Theory 58, 286–292) and studies path decompositions of highly connected graphs (Abh. Math. Semin. Univ. Hambg. 78).
- **2012–2013.** Thomassen's weak $3$-flow theorem and the Lovász–Thomassen–Wu–Zhang modulo-$p$ orientation theorem supply the flow-theoretic engine. Thomassen then settles **all paths** (*Decomposing graphs into paths of fixed length*, Combinatorica 33 (2013), 97–123) and **all bistars** (JCTB 103 (2013), 504–508).
- **2017 — resolution.** Bensmail, Harutyunyan, Le, Merker and Thomassé, *A proof of the Barát–Thomassen conjecture*, JCTB 124, 39–55: $k_T<\infty$ for every tree $T$. The proof reduces general graphs to a bipartite-like "$T$-friendly" setting through random-orientation and fractional-decomposition arguments, then rounds using high edge-connectivity.
- **2017–2019 — quantitative phase.** Botler, Mota, Oshiro and Wakabayashi prove that $24k$-edge-connectivity suffices for paths with $k$ edges (JCTB 122, 508–542). Bensmail, Harutyunyan, Le and Thomassé (Combinatorica 39 (2019), 239–263) replace the growing connectivity by an **absolute constant**: $24$-edge-connected graphs with $\delta(G)\ge 2k$ and $k \mid |E(G)|$ decompose into paths of length $k$.

Status: existential statement **proved**; optimal thresholds **open**.

## 4. Partial Results / Verified Cases

| Class of $T$ | Result | Source |
|---|---|---|
| $T=P_3$ (path, $2$ edges) | $k_T=1$: every connected graph with an even number of edges decomposes | classical (Section 10) |
| $T=P_4$ (path, $3$ edges) | finite threshold established | Thomassen 2008 |
| $T=K_{1,3}$ (claw) | reduces to mod-$3$ orientations; $6$-edge-connectivity suffices for graphs with all degrees divisible by $3$ | Barát–Thomassen 2006; LTWZ 2013 |
| stars $K_{1,k}$ | finite threshold, via modulo-$k$ orientations | Thomassen 2012–2013 |
| paths $P_{k+1}$, all $k$ | $24k$-edge-connected suffices | Botler–Mota–Oshiro–Wakabayashi 2017 |
| paths, degree version | $24$-edge-connected plus $\delta \ge 2k$ suffices | Bensmail–Harutyunyan–Le–Thomassé 2019 |
| paths of length $5$ | explicit small-constant thresholds | Botler–Mota–Oshiro–Wakabayashi, Discrete Appl. Math. 245 (2018), 128–138 |
| bistars (two adjacent centres) | finite threshold | Thomassen 2013 |
| all trees, homomorphic copies | explicit linear-in-$|E(T)|$ edge-connectivity | Merker, *Decomposing highly edge-connected graphs into homomorphic copies of a fixed tree*, JCTB 122 (2017) |
| all trees, isomorphic copies | $k_T<\infty$, bound non-explicit | Bensmail–Harutyunyan–Le–Merker–Thomassé 2017 |

Regular and prescribed-girth host graphs have separate, sharper treatments in the Botler–Mota–Oshiro–Wakabayashi line of work.

## 5. Principal Obstacles

- **Non-explicit constants.** The 2017 proof runs through a chain of reductions (random orientations, fractional decomposition, absorption of a remainder), each of which loses control of the constant. The resulting $k_T$ is a tower-type or otherwise unspecified function of $|E(T)|$; no step in the argument is tight.
- **Orientation methods do not extend past stars and paths.** For $T=K_{1,k}$, decomposition is *equivalent* to an out-degree condition, so flow theory applies directly. For a tree of diameter $\ge 3$, no single vertex "owns" a copy of $T$, and there is no local certificate that an orientation can encode.
- **Rounding the fractional solution.** High edge-connectivity yields a fractional $T$-decomposition easily, but converting it to an integral one requires an absorber: a sparse subgraph that can swallow any small remainder. Absorbers for trees of large diameter must be built globally, and their existence is where the connectivity constant explodes.
- **Parity and residue obstructions are non-local.** Local degree conditions can be satisfied everywhere while a global residue obstruction survives — the same phenomenon that makes the $3$-flow conjecture hard. Any proof of a *small* $k_T$ for claws would essentially resolve Tutte's $3$-flow conjecture for the relevant class, so improvements below $6$ in the claw case are as hard as a famous open problem.
- **Regularity/absorption methods (Keevash, Glock–Kühn–Lo–Osthus) need near-completeness.** They deliver $F$-designs in dense hosts; sparse $k$-edge-connected graphs fall entirely outside their hypotheses.

## 6. The Gap

Proved: $k_T$ exists for every tree, with explicit linear bounds only for paths, stars, bistars and homomorphic copies. Conjectured but unproved:

1. **Linear bound.** Is $k_T = O(|E(T)|)$ — indeed, does $ck$-edge-connectivity suffice for all trees with $k$ edges, with $c$ absolute?
2. **Degree version.** Is there an absolute constant $c$ such that $c$-edge-connectivity together with $\delta(G)\ge |E(T)|$ suffices? Known for paths ($c=24$, $\delta\ge 2k$); open for every tree of diameter $\ge 3$ that is not a bistar.
3. **Sharp small cases.** The optimal $k_T$ is unknown even for $T=K_{1,3}$ and $T=P_4$.

The missing technical step is an absorption structure for arbitrary trees whose size is controlled by $|E(T)|$ rather than by the recursion depth of the reduction.

## 7. Current Research (as of June 2026)

- **Explicit-constant programme.** Groups at Université Côte d'Azur (Bensmail), ENS Lyon (Thomassé), DTU (Merker, following Thomassen's school) and São Paulo (Botler, Mota, Wakabayashi) continue to push explicit thresholds from paths to trees of bounded diameter. Diameter-$4$ trees are the current frontier *(frontier — verify)*.
- **Degree-version extensions.** Attempts to transfer the Combinatorica 2019 minimum-degree technique from paths to spiders (trees with one branch vertex) are reported in preprint form *(frontier — verify)*.
- **Flow-theoretic input.** Any improvement of the $(3p-3)$-edge-connectivity bound for mod-$p$ orientations would immediately sharpen the star cases.
- **Algorithmic angle.** Deciding $T$-decomposability is NP-complete for $|E(T)|\ge 3$ (Dor–Tarsi); constructive versions of the Barát–Thomassen proof that run in polynomial time on $k_T$-edge-connected inputs are of active interest.

## 8. Future Work

- Prove $k_T \le c\,|E(T)|$ for all trees; Merker's homomorphic-copy theorem suggests the linear regime is the right one and that the loss is in converting homomorphic images to embedded copies.
- Settle the degree version for spiders, then for trees of bounded diameter, then in general.
- Determine the exact $k_{K_{1,3}}$ conditional on Tutte's $3$-flow conjecture, isolating which part of the difficulty is flow-theoretic.
- Extend beyond trees: characterise the connected graphs $H$ (necessarily with extra degree divisibility hypotheses) for which a finite $k_H$ exists.
- Develop absorbers for sparse hosts, transferable to related sparse-design problems.

## 9. Key References

- **[Foundational]** J. Barát, C. Thomassen. *Claw-decompositions and Tutte-orientations.* Journal of Graph Theory 52(2), 135–146, 2006.
- **[Foundational]** C. Thomassen. *Decompositions of highly connected graphs into paths of length 3.* Journal of Graph Theory 58(4), 286–292, 2008.
- **[Key tool]** C. Thomassen. *The weak 3-flow conjecture and the weak circular flow conjecture.* Journal of Combinatorial Theory Series B 102(2), 521–529, 2012.
- **[Key tool]** L. M. Lovász, C. Thomassen, Y. Wu, C.-Q. Zhang. *Nowhere-zero 3-flows and modulo k-orientations.* Journal of Combinatorial Theory Series B 103(5), 587–598, 2013.
- **[Milestone]** C. Thomassen. *Decomposing graphs into paths of fixed length.* Combinatorica 33(1), 97–123, 2013.
- **[Milestone]** C. Thomassen. *Decomposing a graph into bistars.* Journal of Combinatorial Theory Series B 103(4), 504–508, 2013.
- **[SOTA]** J. Bensmail, A. Harutyunyan, T.-N. Le, M. Merker, S. Thomassé. *A proof of the Barát–Thomassen conjecture.* Journal of Combinatorial Theory Series B 124, 39–55, 2017.
- **[SOTA]** F. Botler, G. O. Mota, M. T. I. Oshiro, Y. Wakabayashi. *Decomposing highly edge-connected graphs into paths of any given length.* Journal of Combinatorial Theory Series B 122, 508–542, 2017.
- **[SOTA]** J. Bensmail, A. Harutyunyan, T.-N. Le, S. Thomassé. *Edge-partitioning a graph into paths: beyond the Barát–Thomassen conjecture.* Combinatorica 39(2), 239–263, 2019.
- **[SOTA]** M. Merker. *Decomposing highly edge-connected graphs into homomorphic copies of a fixed tree.* Journal of Combinatorial Theory Series B 122, 91–108, 2017.
- **[Complexity]** D. Dor, M. Tarsi. *Graph decomposition is NP-complete: a complete proof of Holyer's conjecture.* SIAM Journal on Computing 26(4), 1166–1187, 1997.
- **[Survey]** R. Diestel. *Graph Theory.* 5th edition, Springer GTM 173, 2017. (Chapters on connectivity and flows.)

## 10. Worked Example / Concrete Special Case

**Case $T=P_3$ (path with two edges): $k_T=1$.**

*Claim.* Every connected graph $G$ with $|E(G)|$ even decomposes into paths of length $2$.

*Proof when all degrees are even.* $G$ is Eulerian, so it has a closed Euler tour $e_1 e_2 \cdots e_m$ with $m=|E(G)|$ even. Pair consecutive edges:
$$\{e_1,e_2\},\ \{e_3,e_4\},\ \dots,\ \{e_{m-1},e_m\}.$$
Consecutive tour edges share a vertex and are distinct, so each pair spans a copy of $P_3$. The pairs partition $E(G)$. $\square$

*Example.* $G=K_5$: $|E|=10$, all degrees $4$. An Euler tour is
$$12,\,23,\,34,\,45,\,51,\,13,\,35,\,52,\,24,\,41,$$
giving the five paths $2\!-\!1\!-\!3$ wait — pairing gives $1\text{-}2\text{-}3$, $3\text{-}4\text{-}5$, $5\text{-}1\text{-}3$, $3\text{-}5\text{-}2$, $2\text{-}4\text{-}1$. Five edge-disjoint copies of $P_3$ covering all $10$ edges.

*Odd degrees.* The odd-degree vertices come in an even number $2s$; pair them and add $s$ auxiliary edges to make the graph Eulerian, run the argument, then delete auxiliary edges and repair locally. The point is that **no** connectivity beyond $1$ is needed.

**Contrast: $T=P_4$ (three edges).** Divisibility alone fails. $K_{1,3}$ has $3$ edges but its maximum path has length $2$, so no $P_4$-decomposition exists. $K_{1,3}$ is only $1$-edge-connected, which is exactly the loophole $k_T$ must close.

**Case $T=K_{1,3}$: the orientation reduction.** Suppose every degree of $G$ is divisible by $3$ and $G$ has a mod-$3$ orientation $D$. Then $2d^+(v)\equiv d(v)\equiv 0 \pmod 3$, so $3 \mid d^+(v)$ for every $v$. Partition the out-edges at each $v$ arbitrarily into groups of three; each group is a claw centred at $v$, and every edge lies in exactly one group (the one at its tail). Hence $G$ has a claw decomposition. By Lovász–Thomassen–Wu–Zhang, $6$-edge-connectivity guarantees the required orientation, so
$$G \text{ } 6\text{-edge-connected},\ 3 \mid d(v)\ \forall v \ \Longrightarrow\ G \text{ has a } K_{1,3}\text{-decomposition}.$$
This is the cleanest instance of the conjecture, and it also shows why the general case is hard: for any tree of diameter $\ge 3$ no analogous vertex-local certificate exists.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*