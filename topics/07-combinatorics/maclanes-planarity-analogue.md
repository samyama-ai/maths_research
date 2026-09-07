---
id: 07-combinatorics/maclanes-planarity-analogue
title: "MacLane's Planarity Criterion Analogue"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# MacLane's Planarity Criterion Analogue

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/maclanes-planarity-analogue` · **Status:** open

## 1. Problem Statement / Conjecture

MacLane's 1937 criterion says a finite graph is planar exactly when its cycle space has a basis in which every edge lies in at most two basis cycles (a *2-basis*). The problem is to find the correct analogue for higher-genus surfaces.

Define the **MacLane deficiency** $\mu(G)$: the least $k$ such that $Z(G)$ has a basis $B = F \cup H$ with $|H| = k$ and every edge of $G$ in at most two members of $F$. MacLane's theorem is $\mu(G) = 0 \iff G$ planar.

**Central question.** Is $\mu(G)$ equal to the Euler genus $\bar\gamma(G)$ for every finite connected graph $G$? The inequality $\mu(G) \le \bar\gamma(G)$ is a theorem (Section 4). Open is the converse, in two strengths:

- **(Strong form)** $\mu(G) = \bar\gamma(G)$ for all finite connected $G$.
- **(Weak form)** There is a function $f$ with $\bar\gamma(G) \le f(\mu(G))$ — i.e. bounded deficiency forces bounded genus.

A complete resolution is either a proof of the strong form, or an explicit family $G_1, G_2, \dots$ with $\mu(G_i)$ bounded and $\bar\gamma(G_i) \to \infty$ (which refutes both forms), or a proof of the weak form with an explicit $f$ plus a counterexample to equality. Related open variants: the same question for orientable genus, and the matroid version (a purely binary-matroid criterion for "planarity" beyond genus $0$).

## 2. Mathematical Foundations

Let $G = (V,E)$ be finite, connected, $n = |V|$, $m = |E|$. The **cycle space** $Z(G) \le \mathbb{F}_2^E$ is the set of edge sets with all degrees even, with
$$\dim Z(G) = m - n + 1 =: \beta(G).$$

A family $F \subseteq Z(G)$ is **sparse** if $|\{C \in F : e \in C\}| \le 2$ for every $e \in E$.

**Theorem (MacLane 1937).** $G$ is planar $\iff$ $Z(G)$ has a sparse basis.

**Surfaces.** For a closed surface $S$, the Euler genus is $\bar\gamma(S) = 2 - \chi(S)$, so $\bar\gamma = 2g$ for the orientable genus-$g$ surface and $\bar\gamma = k$ for the connected sum of $k$ projective planes. For a **cellular** embedding of $G$ in $S$ (every face an open disc) with $f$ faces, Euler's formula reads
$$n - m + f = 2 - \bar\gamma(S).$$

**Homology.** For a cellular embedding, let $\mathcal{F}$ be the set of facial walks, viewed in $\mathbb{F}_2^E$. Each edge has exactly two sides, so each edge lies in at most two distinct facial walks — $\mathcal{F}$ is sparse. The span $\langle \mathcal{F}\rangle$ is the group of $\mathbb{F}_2$-boundaries, and
$$Z(G)/\langle \mathcal{F}\rangle \;\cong\; H_1(S;\mathbb{F}_2), \qquad \dim H_1(S;\mathbb{F}_2) = \bar\gamma(S).$$
Equivalently $\dim\langle\mathcal{F}\rangle = f - 1 = \beta(G) - \bar\gamma(S)$; the single relation is $\sum_{W \in \mathcal{F}} W = 0$.

**Consequence.** $\mu(G) \le \bar\gamma(G)$: take a minimum-genus embedding (cellular by Youngs 1963), keep $f-1$ independent facial walks as the sparse part $F$, and complete with $\bar\gamma$ cycles representing an $\mathbb{F}_2$-homology basis of $S$.

**Counting bound.** If $B = F \cup H$ witnesses $\mu(G) = k$ and $G$ is $2$-connected with girth $g_0$, then $F \cup \{\sum F\}$ covers every edge at most twice, giving $(\beta(G) - k + 1)\,g_0 \le 2m$, i.e.
$$k \;\ge\; \beta(G) + 1 - \frac{2m}{g_0}.$$
This is the exact MacLane-side shadow of the Euler-formula genus bound $\bar\gamma(G) \ge \beta(G)+1-2m/g_0$.

## 3. History & State of the Art (SOTA)

- **1932.** Whitney characterizes planarity by existence of a combinatorial dual (*Non-separable and planar graphs*, Trans. AMS).
- **1937.** Saunders MacLane, *A combinatorial condition for planar graphs* (Fund. Math. 28), gives the 2-basis criterion — the first characterization purely internal to the cycle space, with no dual graph and no forbidden subgraph.
- **1963.** Youngs proves minimum-genus embeddings are cellular, which is what makes the homological upper bound $\mu \le \bar\gamma$ valid.
- **1974.** Hopcroft–Tarjan give linear-time planarity testing; a 2-basis is extractable from the resulting embedding.
- **1981–2018.** Forbidden-minor route: Archdeacon determines the 35 minor-minimal obstructions for the projective plane; the torus list is still unknown, with 17,535 obstructions found by Myrvold–Woodcock (2018). Robertson–Seymour guarantee finiteness but give no usable certificate.
- **1989/1999.** Thomassen: computing genus is NP-complete. Mohar: for each fixed surface, embeddability is linear-time decidable. So a fixed-$g$ MacLane analogue is not blocked by complexity, but a uniform one would be.
- **2006–2009.** Bruhn–Stein prove MacLane's criterion for locally finite infinite graphs using Diestel's topological cycle space; Bruhn–Diestel (*MacLane's theorem for arbitrary surfaces*, JCTB 2009) push sparse-generating-set methods to embeddings in arbitrary surfaces *(frontier — verify exact statement)*.
- **Ongoing.** The cycle-basis survey of Kavitha et al. (2009) records that no genus analogue of MacLane's criterion is known.

## 4. Partial Results / Verified Cases

- **$k = 0$:** solved completely. $\mu(G) = 0 \iff \bar\gamma(G) = 0$ (MacLane 1937), testable in $O(n)$ time.
- **Upper bound, all $G$:** $\mu(G) \le \bar\gamma(G)$ for every finite connected graph, via the homology computation of Section 2 plus Youngs' cellularity theorem.
- **Small graphs:** equality $\mu = \bar\gamma$ is verified for $K_5, K_6, K_{3,3}, K_{3,4}$, the Petersen graph, and all graphs on $\le 10$ vertices by exhaustive search over sparse families *(frontier — verify)*. $\mu(K_5) = \mu(K_{3,3}) = 1$ (Section 10).
- **Girth-forced classes:** whenever the counting bound of Section 2 is tight — e.g. $K_{3,3}$, $K_{3,4}$, complete bipartite $K_{m,n}$ at the Ringel bound, and cages meeting the Euler bound — the lower bound on $\mu$ matches $\bar\gamma$, so equality holds by sandwiching.
- **Graphs with a closed 2-cell embedding of Euler genus $g$:** all facial walks are cycles and each edge lies in exactly two, so the sparse part is a genuine cycle double cover and $\mu \le g$ with an explicit witness. By Alspach–Goddyn–Zhang, this covers all graphs with no Petersen minor.
- **Infinite graphs:** MacLane's criterion holds verbatim for locally finite graphs with the topological cycle space (Bruhn–Stein 2006) and fails for graphs with a vertex of infinite degree.
- **Additivity checks:** genus is additive over blocks (Battle–Harary–Kodama–Youngs 1962), and $\mu$ is additive over blocks by direct-sum decomposition of $Z(G)$, so the conjecture reduces to $2$-connected graphs.

## 5. Principal Obstacles

- **Sparse ≠ facial.** A sparse family of $\beta - k$ independent cycles carries no rotation system. To turn it into an embedding one must order the faces around each vertex consistently; for $k=0$ the ordering is forced (MacLane's proof uses Whitney's dual and $3$-connected uniqueness), but for $k \ge 1$ the local rotations are underdetermined. There is no known local-to-global gluing lemma.
- **Orientability is invisible to $\mathbb{F}_2$.** Cycle space over $\mathbb{F}_2$ cannot distinguish the torus from the Klein bottle, so at best $\mu$ can capture Euler genus, never orientable genus. Any orientable analogue must move to $\mathbb{Z}$-coefficients or signed rotation systems, where "at most two" has no clean meaning.
- **Non-cellular slack.** A sparse family can be homologically efficient while the corresponding "faces" are not discs. Certifying disc-ness is precisely what the Strong Embedding Conjecture asserts and nobody can prove.
- **No minor-monotonicity.** $\bar\gamma$ is minor-monotone; $\mu$ is not obviously so, because contracting an edge can merge cycles and destroy sparseness. This blocks the entire Robertson–Seymour toolkit — one cannot argue by excluded minors about $\mu$.
- **Complexity tension.** Genus is NP-complete (Thomassen 1989). If $\mu = \bar\gamma$, then deciding $\mu \le k$ is NP-hard, so no polynomial certificate-checking form of the criterion can exist uniformly in $k$ unless P = NP. Any proof must therefore be non-algorithmic, which rules out the constructive style of MacLane's original argument.

## 6. The Gap

Proven: $0 \le \mu(G) \le \bar\gamma(G)$, with equality at $\mu = 0$. Missing: any lower bound on $\bar\gamma$ in terms of $\mu$ beyond the trivial $\bar\gamma \ge 1$ when $\mu \ge 1$.

The precise step is a **realization theorem**: given a sparse independent family $F \subset Z(G)$ with $|F| = \beta(G) - k$, produce an embedding of $G$ in a surface of Euler genus $\le h(k)$. For $k = 0$ this is MacLane's construction of the dual. For $k \ge 1$ the obstruction is that $F$ need not extend to a cycle double cover, and even when it does, the double cover need not be a *circular* (closed 2-cell) embedding. Concretely: the gap between $\mu$ and $\bar\gamma$ is exactly the gap between "$\mathbb{F}_2$-homologically genus $k$" and "topologically genus $k$", and no example separating them is known in either direction.

## 7. Current Research (as of June 2026)

- **Topological cycle space school** (Diestel, Bruhn, Stein, and successors at Hamburg): extending MacLane-type criteria from the plane to arbitrary surfaces for infinite graphs; the finite higher-genus case is the acknowledged residue.
- **Cycle double covers and circular embeddings** (Goddyn, Zhang, Máčajová, Škoviera): the Strong Embedding Conjecture is the natural sufficient condition making sparse families facial. Progress on small-genus circular embeddings of snarks feeds directly into $\mu$ vs $\bar\gamma$ *(frontier — verify)*.
- **Computational search** for a separating example, i.e. a graph with $\mu < \bar\gamma$, using SAT/ILP over sparse basis families on cubic graphs of genus $2$–$3$ *(frontier — verify)*.
- **Matroid reformulation** (Oxley school): asking for a binary-matroid invariant $\mu(M)$ agreeing with Euler genus on graphic matroids, which would explain why minor-monotonicity fails.
- **Homology-of-embeddings** approaches using $\mathbb{Z}$-coefficients and Edmonds rotation systems to attack the orientable variant.

## 8. Future Work

- Settle the **weak form** first: prove $\bar\gamma \le f(\mu)$ for cubic graphs, where cycle double covers are best understood.
- Prove or refute $\mu(G) = 1 \Rightarrow \bar\gamma(G) = 1$, i.e. a MacLane criterion for the projective plane. This is the smallest genuinely open case and is checkable against Archdeacon's 35 obstructions.
- Develop a **rotation-system completion lemma**: conditions on a sparse family guaranteeing a consistent local ordering at each vertex.
- Formulate the criterion for **binary matroids** and test whether minor-monotonicity is recovered there.
- Search systematically for $\mu < \bar\gamma$ among graphs with no cycle double cover of small genus — snarks are the natural candidates.
- Extend Bruhn–Stein to graphs with infinite-degree vertices under an end-compactification hypothesis.

## 9. Key References

- **[Foundational]** MacLane, S. *A combinatorial condition for planar graphs.* Fundamenta Mathematicae 28 (1937), 22–32.
- **[Foundational]** Whitney, H. *Non-separable and planar graphs.* Transactions of the AMS 34 (1932), 339–362.
- **[Foundational]** Youngs, J. W. T. *Minimal imbeddings and the genus of a graph.* Journal of Mathematics and Mechanics 12 (1963), 303–315.
- **[Foundational]** Battle, J., Harary, F., Kodama, Y., Youngs, J. W. T. *Additivity of the genus of a graph.* Bulletin of the AMS 68 (1962), 565–568.
- **[SOTA / Recent]** Bruhn, H., Stein, M. *MacLane's planarity criterion for locally finite graphs.* Journal of Combinatorial Theory Series B 96 (2006), 225–239.
- **[SOTA / Recent]** Bruhn, H., Diestel, R. *MacLane's theorem for arbitrary surfaces.* Journal of Combinatorial Theory Series B 99 (2009), 275–286.
- **[SOTA / Recent]** Myrvold, W., Woodcock, J. *A large set of torus obstructions and how they were discovered.* Electronic Journal of Combinatorics 25(1) (2018), #P1.16.
- **[SOTA / Recent]** Alspach, B., Goddyn, L., Zhang, C.-Q. *Graphs with the circuit cover property.* Transactions of the AMS 344 (1994), 131–154.
- **[Complexity]** Thomassen, C. *The graph genus problem is NP-complete.* Journal of Algorithms 10 (1989), 568–576.
- **[Complexity]** Mohar, B. *A linear time algorithm for embedding graphs in an arbitrary surface.* SIAM Journal on Discrete Mathematics 12 (1999), 6–26.
- **[Complexity]** Hopcroft, J., Tarjan, R. *Efficient planarity testing.* Journal of the ACM 21 (1974), 549–568.
- **[Survey]** Kavitha, T., Liebchen, C., Mehlhorn, K., Michail, D., Rizzi, R., Ueckerdt, T., Zweig, K. *Cycle bases in graphs: characterization, algorithms, complexity, and applications.* Computer Science Review 3 (2009), 199–243.
- **[Survey]** Mohar, B., Thomassen, C. *Graphs on Surfaces.* Johns Hopkins University Press, 2001.
- **[Survey]** Zhang, C.-Q. *Circuit Double Cover of Graphs.* Cambridge University Press, 2012.
- **[Survey]** Archdeacon, D. *A Kuratowski theorem for the projective plane.* Journal of Graph Theory 5 (1981), 243–246.
- **[Reference]** Oxley, J. *Matroid Theory*, 2nd ed. Oxford University Press, 2011.
- **[Reference]** Diestel, R. *Graph Theory*, 5th ed. Springer GTM 173, 2017.

## 10. Worked Example / Concrete Special Case

Take $G = K_{3,3}$ with parts $\{a_1,a_2,a_3\}$, $\{b_1,b_2,b_3\}$. Here $n=6$, $m=9$, girth $g_0=4$, and
$$\beta(G) = 9 - 6 + 1 = 4.$$

**Step 1 — no 2-basis (MacLane's counting).** Suppose $B$ is a sparse basis, $|B| = 4$. Since $G$ is $2$-connected, every edge lies in at least one member of $B$, so $B \cup \{\textstyle\sum B\}$ covers each edge exactly twice: $5$ cycles, each of length $\ge 4$, total edge-multiplicity $2m = 18$. But $5 \cdot 4 = 20 > 18$. Contradiction, so $\mu(K_{3,3}) \ge 1$ and $K_{3,3}$ is not planar.

**Step 2 — deficiency exactly one.** Put
$$C_1 = a_1b_1a_2b_2,\quad C_2 = a_2b_2a_3b_3,\quad C_3 = a_1b_1a_3b_3 .$$
Edge $a_1b_1$ lies in $C_1, C_3$; $a_2b_2$ in $C_1, C_2$; $a_3b_3$ in $C_2, C_3$; every other edge lies in exactly one. So $F = \{C_1,C_2,C_3\}$ is sparse and independent. Their sum is the hexagon
$$C_1 + C_2 + C_3 = a_1b_2a_3b_1a_2b_3a_1 ,$$
and $F \cup \{C_1+C_2+C_3\}$ covers each of the $9$ edges exactly twice: $3\cdot 4 + 6 = 18 = 2m$. These four closed walks are the facial walks of an embedding with
$$\chi = n - m + f = 6 - 9 + 4 = 1,$$
i.e. an embedding in the projective plane, $\bar\gamma = 1$.

**Step 3 — completing to a basis.** Add $C_4 = a_1b_1a_2b_3$. The span of $F$ has $8$ elements: $0$, the three $4$-cycles $C_i$, three $6$-element sums $C_i + C_j$, and the hexagon. $C_4$ is a $4$-cycle distinct from $C_1, C_2, C_3$, so $C_4 \notin \langle F \rangle$ and $B = F \cup \{C_4\}$ is a basis of $Z(K_{3,3})$ with sparse part of size $3 = \beta - 1$.

Hence $\mu(K_{3,3}) \le 1$, and with Step 1, $\mu(K_{3,3}) = 1 = \bar\gamma(K_{3,3})$.

**Where the general problem bites.** Step 2 worked because the sparse family happened to close up into a double cover whose faces are discs. Given only an abstract sparse family $F$ with $|F| = \beta - 1$, nothing forces $\sum F$ to be a single cycle rather than a disjoint union of cycles, and nothing forces the resulting face set to admit a consistent rotation at each vertex. Supplying that step, for every graph and every $k$, is the whole open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*