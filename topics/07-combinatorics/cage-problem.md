---
id: 07-combinatorics/cage-problem
title: "Cage Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cage Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/cage-problem` · **Status:** open

## 1. Problem Statement / Conjecture

A **$(k,g)$-graph** is a finite simple graph that is $k$-regular (every vertex has degree exactly $k$) and has girth exactly $g$ (the shortest cycle has length $g$). For $k \ge 2$ and $g \ge 3$ such graphs exist (Erdős–Sachs, 1963). A **$(k,g)$-cage** is a $(k,g)$-graph with the minimum possible number of vertices; that minimum is written $n(k,g)$.

**The cage problem.** Determine $n(k,g)$ for all $k \ge 3$, $g \ge 5$, and construct the extremal graphs.

Two sharper questions carry most of the research weight:

1. **Exact values.** Compute $n(k,g)$ for specific small pairs. The smallest unresolved cubic case is $n(3,13)$, currently pinned only to $202 \le n(3,13) \le 272$.
2. **Asymptotics.** The Moore bound gives $n(k,g) \ge (k-1)^{(1+o(1))g/2}$ for fixed $k$. No construction is known achieving $(k-1)^{(1+o(1))g/2}$; the best general constructions give roughly $(k-1)^{(1+o(1))\cdot 3g/4}$. Is the true growth exponent $g/2$ or $3g/4$ (or something between)?

A complete resolution of (1) for a given pair means an explicit graph together with a proof — computational or structural — that no smaller $(k,g)$-graph exists. A resolution of (2) means matching upper and lower bounds on $\log n(k,g)/g$ as $g \to \infty$ with $k$ fixed.

## 2. Mathematical Foundations

**Moore bound.** Fix a vertex $v$ in a $k$-regular graph of girth $g$ and expand the breadth-first tree. For odd $g = 2r+1$, the balls of radius $r$ around $v$ contain no repeats, so
$$n(k,g) \ \ge\ M(k,g) \ =\ 1 + k\sum_{i=0}^{r-1}(k-1)^{i}.$$
For even $g = 2r$, expand from an edge $uv$:
$$n(k,g) \ \ge\ M(k,g) \ =\ 2\sum_{i=0}^{r-1}(k-1)^{i}.$$
A graph meeting the bound is a **Moore graph** (odd $g$) or a **generalized polygon incidence graph** (even $g$). The **excess** is $e(k,g) = n(k,g) - M(k,g)$.

**Classification of the extremal case.**
- *Hoffman–Singleton (1960):* a $k$-regular Moore graph of girth $5$ exists only for $k \in \{2,3,7,57\}$. Cases $k=3$ (Petersen, $10$ vertices) and $k=7$ (Hoffman–Singleton graph, $50$ vertices) exist; **$k=57$, $n=3250$, remains open**.
- *Damerell (1973), Bannai–Ito (1973):* for $k \ge 3$ there are no Moore graphs of odd girth $g \ge 7$.
- *Feit–Higman (1964):* generalized $m$-gons with both parameters $>1$ exist only for $m \in \{3,4,6,8\}$ (and degenerately $12$). Hence Moore-bound-attaining $k$-regular graphs of even girth exist only for $g \in \{6,8,12\}$, and there only when $k-1$ is a prime power, via incidence graphs of $PG(2,q)$, $W(q)$, and split Cayley hexagons $H(q)$.

So the bound is attained on a finite, fully classified list; everywhere else the problem is about controlling excess.

**Upper bounds.** Erdős–Sachs (1963) gave the first general existence bound by a deletion/rewiring argument. Sauer (1967) sharpened it to
$$n(k,g) < 2(k-2)^{g-2}\ (g \text{ odd}), \qquad n(k,g) < 4(k-2)^{g-3}\ (g \text{ even}),$$
for $k \ge 4$. The best general algebraic bound is Lazebnik–Ustimenko–Woldar (1997):
$$n(k,g)\ \le\ 2kq^{\frac{3}{4}g - a}, \qquad a = \tfrac{1}{4}\{16,\,{11},\,{7},\,{3}\}\ \text{for } g \equiv 0,1,2,3 \pmod 4,$$
where $q$ is the smallest odd prime power $\ge k-1$. This gives the $3g/4$ exponent, built from the $CD(n,q)$ graphs of Lazebnik–Ustimenko–Woldar (1995), which are $q$-regular, of girth $\ge n+5$, and are the densest known infinite families of high girth.

**Structural facts.** Cages are $2$-connected; every $(k,g)$-cage is $3$-connected (Jiang–Mubayi 1998), and $(k,g)$-cages with $g \ge 10$ are $4$-connected (Marcote–Balbuena–Pelayo–Fàbrega 2005). It is conjectured (Fu–Huang–Rodger 1997) that every $(k,g)$-cage is $k$-connected. Monotonicity in degree, $n(k,g) < n(k+1,g)$ for $g \ge 3$, is known.

## 3. History & State of the Art (SOTA)

- **1947.** Tutte introduces cages while studying cubic graphs of large girth ("A family of cubical graphs"), identifying the $(3,g)$-cages for $g \le 8$; the Tutte–Coxeter graph of order $30$ is the $(3,8)$-cage.
- **1960–1973.** The extremal theory closes: Hoffman–Singleton, Feit–Higman, Damerell, Bannai–Ito. After this, no Moore graph problem remains except degree $57$, girth $5$.
- **1963–1967.** Erdős–Sachs existence; Sauer's exponential upper bounds. These remain the best *general* bounds of purely combinatorial type.
- **1964–1982.** Sporadic cages found and verified: Robertson's $(4,5)$-cage on $19$ vertices; the $(5,5)$-cage on $30$; O'Keefe–Wong establish $n(3,10)=70$, $n(6,5)=40$, $n(7,5)=50$. Wong's 1982 survey consolidates the era.
- **1995–1998.** Computer search matures. Brinkmann–McKay–Saager prove $n(3,9)=58$; McKay–Myrvold–Nadon's backtracking finds the $(3,13)$ graph on $272$ vertices and settles $n(3,11)=112$ (Balaban's 11-cage).
- **1995–1997.** Lazebnik–Ustimenko–Woldar algebraic constructions give the current asymptotic ceiling $\approx q^{3g/4}$.
- **2011.** Exoo–McKay–Myrvold–Nadon publish the full computational determination of the $(3,11)$ and $(4,7)$ cages: $n(4,7)=67$.
- **2008–present.** Exoo–Jajcay's *Dynamic Cage Survey* (Electron. J. Combin., DS16) is the live record of best known upper bounds; most improvements since 2000 are voltage-graph / Cayley-graph lifts that shave a few vertices off a record graph rather than close a case.

## 4. Partial Results / Verified Cases

**Cubic cages, all known values.**

| $g$ | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|
| $n(3,g)$ | 4 | 6 | 10 | 14 | 24 | 30 | 58 | 70 | 112 | 126 |

Graphs: $K_4$, $K_{3,3}$, Petersen, Heawood, McGee, Tutte–Coxeter, Brinkmann–McKay–Saager's $9$-cage (18 non-isomorphic ones), Balaban 10-cage, Balaban 11-cage (unique), Tutte 12-cage (unique; minimality by Benson 1966).

**Beyond degree 3, all known values:** $n(4,5)=19$, $n(4,6)=26$, $n(4,7)=67$, $n(4,8)=80$, $n(4,12)=728$; $n(5,5)=30$, $n(5,6)=42$, $n(5,8)=170$, $n(5,12)=2730$; $n(6,5)=40$, $n(6,6)=62$; $n(7,5)=50$, $n(7,6)=90$. For $g \in \{6,8,12\}$ and $k-1 = q$ a prime power, $n(k,g)=M(k,g)$ exactly, by the incidence graphs of $PG(2,q)$, $W(q)$, $H(q)$.

**Excess results.** For $k \ge 3$ and girth $5$ with $k \notin \{3,7,57\}$, excess $\ge 2$; more generally the "Moore graphs with small excess" theory (Biggs, Bannai–Ito) rules out excess $1$ for $k \ge 3$, and eigenvalue-integrality arguments kill many small excesses.

**Open small cases.** $n(3,13) \in [202,272]$; $n(3,14) \in [258, 384]$; $n(4,9) \in [275, 275]$? — no: $n(4,9)$ is bounded $[159,275]$ *(frontier — verify current survey record)*. $n(5,7) \in [152, 2730 \text{-range}]$, best known upper $170$-class constructions; $n(7,7), n(6,7)$ open. Existence of the $(57,5)$ Moore graph on $3250$ vertices is open, though it is known such a graph would have trivial automorphism group on most orbits (Mačaj–Širáň: $|\mathrm{Aut}| \le 375$).

## 5. Principal Obstacles

- **The counting bound is nearly free and nearly tight-looking, but unusable beyond the classified cases.** The Moore bound uses only local tree expansion. Improving it requires global information about how the "leaves" of the BFS tree join up, and no general algebraic invariant controls that once the spectral characterization (Moore graphs, generalized polygons) is exhausted.
- **Spectral methods stop working off the extremal locus.** For Moore graphs the adjacency matrix satisfies a polynomial equation $p(A)=J$, forcing integrality of eigenvalue multiplicities — the engine behind Hoffman–Singleton and Feit–Higman. With excess $e \ge 2$ that identity degenerates into an inequality and the integrality obstruction evaporates.
- **Algebraic constructions carry an intrinsic $3/4$ loss.** $CD(n,q)$ and the LUW graphs are defined by explicit polynomial equations over $\mathbb{F}_q$; the girth is forced by a "cascading" system of coordinates, and each unit of girth costs about $3/4$ of a dimension rather than $1/2$. No known algebraic family — including Ramanujan graphs (Lubotzky–Phillips–Sarnak, Margulis), which give girth $\ge \frac{4}{3}\log_{k-1} n$ — reaches the $g/2$ exponent. Random regular graphs are useless: they have girth $O(1)$.
- **Search space explodes.** Exhaustive backtracking scales roughly like the number of partial extensions of a BFS tree; the $(3,11)$ determination ($112$ vertices) already needed years of specialized isomorph-free generation. $(3,13)$ has $\ge 202$ vertices and an estimated search cost several orders of magnitude larger.
- **No lower-bound technique below the Moore bound plus small additive terms.** Almost every improved lower bound is a case analysis on the excess vertices' neighborhood structure; these arguments do not compose or generalize in $g$.

## 6. The Gap

Two gaps, of different character.

**Exact-value gap.** For $(3,13)$ the true value lies in $[202,272]$ — a factor of $1.35$. Closing it needs either (a) a construction below $272$, or (b) a lower bound argument or exhaustive search past $202$. Neither is a new idea in principle; both are blocked by combinatorial explosion. The general boundary: cases are solvable when $M(k,g)$ is attained (algebra decides) or when $n(k,g) \lesssim 120$ (computation decides). Between roughly $120$ and $3250$ vertices, nothing works.

**Asymptotic gap.** Known:
$$(k-1)^{g/2 - 1} \ \lesssim\ n(k,g)\ \lesssim\ q^{3g/4}.$$
The step that must be crossed is producing a $k$-regular graph family of girth $g$ and order $(k-1)^{(1/2+\varepsilon)g}$ for some $\varepsilon < 1/4$ — or proving the Moore bound can be improved by a factor exponential in $g$. Even the special case $g=6$ *(Turán-type: $\mathrm{ex}(n;C_4)$)* is tight, so the loss must be concentrated at large $g$, and no mechanism explaining where is known.

## 7. Current Research (as of June 2026)

- **Voltage graphs and lifts.** Exoo, Jajcay, and collaborators (Slovak/Indiana school) construct record graphs as regular lifts of small base graphs with voltage assignments in $\mathbb{Z}_n$ or non-abelian groups, letting a computer search run over group elements rather than vertices. Most upper-bound records for $k=3,4$ and $g \in \{13,\dots,18\}$ come from this. *(frontier — verify current DS16 revision for the live table.)*
- **Biregular cages and bipartite cages.** Balbuena and coauthors (UPC Barcelona) study $(\{r,m\};g)$-cages and bipartite cages $n_b(k,g)$, where incidence-geometry deletions give sharper constructions.
- **Degree-57 Moore graph.** Mačaj–Širáň-style automorphism restrictions and SAT/ILP attacks continue; the graph is neither constructed nor excluded. *(frontier — verify.)*
- **Girth-Ramsey and constructive-density interplay.** Connections to the degenerate Turán problem $\mathrm{ex}(n; C_4,\dots,C_{g-1})$ and to LDPC code design (girth $\leftrightarrow$ absence of short cycles in Tanner graphs) keep the asymptotic question active outside pure combinatorics.
- **Isomorph-free exhaustive generation.** McKay's `genreg`/`nauty` toolchain plus canonical-augmentation pruning remains the only route to exact values; parallelization has not yet reached $(3,13)$.

## 8. Future Work

- **Attack $n(3,13)$ directly.** Improve the lower bound from $202$ toward $230$–$250$ by structural analysis of the excess subgraph, then close by search. Exoo has repeatedly identified this as the natural next exact value.
- **Find a construction beating exponent $3/4$.** Candidate sources: incidence structures of higher-rank buildings, coset graphs of groups of Lie type over local rings, and Cayley graphs of nilpotent groups with prescribed relator length.
- **Prove or refute the $k$-connectivity conjecture** (Fu–Huang–Rodger). A positive proof would give a genuinely new structural lever on excess vertices.
- **Excess theory beyond $e=1$.** Extend spectral obstructions to excess $2$ and $3$ for odd girth, which would immediately settle several small open cases.
- **Certified search.** Produce machine-checkable certificates (e.g., in Lean or via DRAT proofs from SAT encodings) for existing exact values, then push the method to $(3,13)$.

## 9. Key References

- **[Foundational]** W. T. Tutte. *A family of cubical graphs.* Proceedings of the Cambridge Philosophical Society **43** (1947), 459–474.
- **[Foundational]** P. Erdős, H. Sachs. *Reguläre Graphen gegebener Taillenweite mit minimaler Knotenzahl.* Wiss. Z. Martin-Luther-Univ. Halle-Wittenberg Math.-Natur. Reihe **12** (1963), 251–257.
- **[Foundational]** A. J. Hoffman, R. R. Singleton. *On Moore graphs with diameters 2 and 3.* IBM Journal of Research and Development **4** (1960), 497–504.
- **[Foundational]** W. Feit, G. Higman. *The nonexistence of certain generalized polygons.* Journal of Algebra **1** (1964), 114–131.
- **[Foundational]** R. M. Damerell. *On Moore graphs.* Proceedings of the Cambridge Philosophical Society **74** (1973), 227–236.
- **[Foundational]** E. Bannai, T. Ito. *On finite Moore graphs.* Journal of the Faculty of Science, University of Tokyo, Sect. IA **20** (1973), 191–208.
- **[Foundational]** N. Sauer. *Extremaleigenschaften regulärer Graphen gegebener Taillenweite, I and II.* Österreich. Akad. Wiss. Math.-Natur. Kl. S.-B. II **176** (1967), 27–43.
- **[SOTA]** F. Lazebnik, V. A. Ustimenko, A. J. Woldar. *A new series of dense graphs of high girth.* Bulletin of the American Mathematical Society **32** (1995), 73–79.
- **[SOTA]** F. Lazebnik, V. A. Ustimenko, A. J. Woldar. *New upper bounds on the order of cages.* Electronic Journal of Combinatorics **4**(2) (1997), \#R13.
- **[SOTA]** G. Brinkmann, B. D. McKay, C. Saager. *The smallest cubic graphs of girth nine.* Combinatorics, Probability and Computing **4** (1995), 317–329.
- **[SOTA]** G. Exoo, B. D. McKay, W. Myrvold, J. Nadon. *Computational determination of $(3,11)$ and $(4,7)$ cages.* Journal of Combinatorial Mathematics and Combinatorial Computing **77** (2011), 151–164.
- **[SOTA]** T. Jiang, D. Mubayi. *Connectivity and separating sets of cages.* Journal of Graph Theory **29** (1998), 35–44.
- **[Survey]** G. Exoo, R. Jajcay. *Dynamic cage survey.* Electronic Journal of Combinatorics, Dynamic Survey DS16 (2008; revised editions through 2013).
- **[Survey]** P. K. Wong. *Cages — a survey.* Journal of Graph Theory **6** (1982), 1–22.
- **[Book]** N. Biggs. *Algebraic Graph Theory*, 2nd edition. Cambridge University Press, 1993.
- **[Book]** A. E. Brouwer, A. M. Cohen, A. Neumaier. *Distance-Regular Graphs.* Springer-Verlag, 1989.

## 10. Worked Example / Concrete Special Case

**Claim.** $n(3,5) = 10$, attained uniquely by the Petersen graph.

*Lower bound.* Take $k=3$, $g=5=2\cdot 2+1$, so $r=2$:
$$M(3,5) = 1 + 3\big((3-1)^0 + (3-1)^1\big) = 1 + 3(1+2) = 10.$$
Concretely: pick a vertex $v$. It has $3$ neighbours $u_1,u_2,u_3$. Each $u_i$ has $2$ further neighbours. No two of these $6$ second-neighbours coincide (that would give a $4$-cycle) and none is adjacent to $v$ (that would give a triangle), and none equals another $u_j$ (a triangle again). So $1+3+6 = 10$ distinct vertices, hence $n(3,5)\ge 10$.

*Upper bound and closure.* With exactly $10$ vertices, every second-neighbour $w$ has one edge used (to its $u_i$) and needs $2$ more. It cannot attach to $v$, to any $u_j$ (that would create a $4$-cycle through $v$), nor to the other second-neighbour under the same $u_i$ (a triangle). So the $6$ outer vertices form a $2$-regular graph on themselves with all edges between different $u_i$-blocks: this is forced to be a $6$-cycle alternating blocks, and the resulting graph is the Petersen graph. Uniqueness follows because every choice above was forced up to relabelling.

**Contrast: girth 7 fails the bound.** For $k=3$, $g=7$, $r=3$:
$$M(3,7) = 1 + 3(1 + 2 + 4) = 22,$$
but the actual cage is the McGee graph on $24$ vertices, excess $e = 2$. Damerell's theorem says the deficit is unavoidable for every cubic girth $\ge 7$; but it says nothing about *how large* the excess must be. That single missing quantitative statement — a lower bound on $e(k,g)$ that grows — is the heart of the cage problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*