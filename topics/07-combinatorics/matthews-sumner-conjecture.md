---
id: 07-combinatorics/matthews-sumner-conjecture
title: "Matthews-Sumner Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Matthews-Sumner Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/matthews-sumner-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Matthews–Sumner, 1984).** Every $4$-connected claw-free graph is Hamiltonian.

Here a finite simple graph $G$ is *claw-free* if it has no induced subgraph isomorphic to $K_{1,3}$ (the *claw*), and *$4$-connected* if $|V(G)| \ge 5$ and $G - S$ is connected for every $S \subseteq V(G)$ with $|S| \le 3$. *Hamiltonian* means $G$ contains a spanning cycle.

A complete proof must establish the statement for all such $G$, of every order. A disproof requires one $4$-connected claw-free graph with no Hamilton cycle. The hypothesis is sharp in connectivity: infinitely many $3$-connected claw-free non-Hamiltonian graphs exist (Matthews–Sumner 1984), so the conjecture cannot be weakened to $\kappa(G) \ge 3$. It is also known that no finite-degree or finite-order reduction is available — the conjecture is open for $4$-connected claw-free graphs of arbitrarily large maximum degree, and equally open for the $4$-regular-ish subclass of line graphs of cubic graphs.

## 2. Mathematical Foundations

**Line graphs.** For $H$ with $E(H) \ne \emptyset$, the line graph $L(H)$ has $V(L(H)) = E(H)$, with $e \sim f$ iff $e \cap f \ne \emptyset$. Every line graph is claw-free; the converse fails (e.g. $K_{1,3}$-free graphs like $C_5^2$-type constructions), but claw-free graphs are exactly the graphs whose neighbourhoods have independence number $\alpha(N_G(v)) \le 2$:
$$G \text{ claw-free} \iff \forall v \in V(G):\ \alpha\big(G[N_G(v)]\big) \le 2 .$$

**Dominating closed trails.** A closed trail $T$ in $H$ (closed walk with no repeated edge) is *dominating* (a DCT) if every edge of $H$ has at least one endvertex on $V(T)$.

**Theorem (Harary–Nash-Williams, 1965).** For a graph $H$ with at least three edges, $L(H)$ is Hamiltonian $\iff$ $H$ has a dominating closed trail.

**Essential edge connectivity.** An edge cut $F \subseteq E(H)$ is *essential* if $H - F$ has at least two components containing an edge. $H$ is *essentially $k$-edge-connected* if no essential cut has fewer than $k$ edges. For $H$ with $\delta(H)\ge 3$,
$$\kappa\big(L(H)\big) \ge 4 \iff H \text{ is essentially } 4\text{-edge-connected}.$$

**Ryjáček closure.** A vertex $v$ is *locally connected* if $G[N_G(v)]$ is connected. The *local completion* at $v$ replaces $G[N_G(v)]$ by a clique. The *closure* $\mathrm{cl}(G)$ is obtained by iterating local completion at locally connected vertices until none remain.

**Theorem (Ryjáček, 1997).** For claw-free $G$: (i) $\mathrm{cl}(G)$ is uniquely determined; (ii) $\mathrm{cl}(G)$ is the line graph of a triangle-free graph; (iii) $\kappa(\mathrm{cl}(G)) \ge \kappa(G)$; (iv) $G$ is Hamiltonian $\iff$ $\mathrm{cl}(G)$ is Hamiltonian.

**Consequent equivalences.** By (iii)–(iv), Matthews–Sumner is equivalent to **Thomassen's Conjecture (1986)**: *every $4$-connected line graph is Hamiltonian*; and by Harary–Nash-Williams to: *every essentially $4$-edge-connected graph with $\delta \ge 3$ has a dominating closed trail*. Fleischner–Jackson (1989) reduce the last statement to cyclically $4$-edge-connected cubic graphs. Ryjáček–Vrána (2011) further show equivalence with the formally stronger *every $4$-connected claw-free graph is $1$-Hamilton-connected* (remains Hamilton-connected after subdividing any one edge).

## 3. History & State of the Art (SOTA)

- **1984.** M. M. Matthews and D. P. Sumner, studying Hamiltonicity of $K_{1,3}$-free graphs, prove that every $2$-connected claw-free graph with $\Delta(G) \le 4$ is Hamiltonian and that every $2$-connected claw-free $G$ has a cycle of length $\ge \min\{|V(G)|, 2\delta+4\}$; they pose the $4$-connected conjecture.
- **1986.** Thomassen independently conjectures the line-graph form.
- **1989.** Fleischner and Jackson tie the problem to cyclically $4$-edge-connected cubic graphs, linking it to the circuit-cover/dominating-cycle circle of problems (Ash–Jackson, Fleischner's dominating-cycle conjecture).
- **1991.** Zhan: every $7$-connected line graph is Hamilton-connected — hence every $7$-connected claw-free graph is Hamiltonian (via closure). Independently obtained by Zhan and by Győri–Plummer-type arguments.
- **1997.** Ryjáček's closure reduces the general claw-free case to line graphs of triangle-free graphs; the survey of Faudree–Flandrin–Ryjáček consolidates the area.
- **2005.** Chudnovsky–Seymour's structure theorem for claw-free graphs gives a global decomposition, but has not yielded Hamiltonicity.
- **2006.** Lai, Shao, Wu, Zhou: every $3$-connected, essentially $11$-connected line graph is Hamiltonian.
- **2012.** Kaiser–Vrána: every $5$-connected line graph with minimum degree $\ge 6$ is Hamilton-connected; hence every $5$-connected claw-free graph with $\delta \ge 6$ is Hamiltonian. This remains the best connectivity reduction, and $5$ has not been lowered to $4$ in the fifteen years since.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\kappa \ge 7$, claw-free | Hamiltonian (indeed Hamilton-connected) | Zhan 1991 |
| $\kappa \ge 5$, claw-free, $\delta \ge 6$ | Hamilton-connected | Kaiser–Vrána 2012 |
| $4$-connected claw-free, hourglass-free ($\Gamma_0$ = two triangles sharing one vertex) | Hamilton-connected | Kaiser, Li, Ryjáček, Xiong 2005 |
| $4$-connected planar claw-free | Hamiltonian (special case of Tutte 1956) | Tutte 1956 |
| $4$-connected $L(H)$ with $H$ planar | Hamiltonian | Lai–Shao–Zhan-type arguments |
| $3$-connected, essentially $11$-connected line graphs | Hamiltonian | Lai, Shao, Wu, Zhou 2006 |
| $2$-connected claw-free, $\Delta \le 4$ | Hamiltonian | Matthews–Sumner 1984 |
| $3$-connected $\{K_{1,3},Z_7\}$-free, order $\ge 21$ ($Z_i$: triangle with a pendant $P_i$) | Hamilton-connected | Ryjáček–Vrána 2021 |
| $4$-connected claw-free | has a $2$-factor with at most $6$ components; has spanning subgraph structure results | Broersma–Kriesell–Ryjáček 2001 |
| Cubic bridgeless $H$ | a $2$-factor meeting all $3$- and $4$-cuts exists (partial step toward DCT) | Kaiser–Škrekovski 2008 |

Computationally, no counterexample appears among $4$-connected claw-free graphs of small order; exhaustive generation of cyclically $4$-edge-connected cubic graphs up to $\sim 30$ vertices confirms all have dominating closed trails *(frontier — verify: published tables cover snark catalogues rather than a dedicated DCT census)*.

## 5. Principal Obstacles

- **No local certificate for Hamiltonicity.** Hamiltonicity is NP-complete even for $3$-connected cubic planar graphs; the conjecture asserts that $4$-connectivity plus claw-freeness makes it trivially true, so any proof must be an existence argument, not a check. There is no known polynomial certificate to aim a structural induction at.
- **The closure destroys nothing but simplifies nothing enough.** Ryjáček's closure reduces to line graphs of triangle-free graphs, i.e. to DCTs in essentially $4$-edge-connected graphs. But an essentially $4$-edge-connected graph can have arbitrarily many degree-$3$ vertices, and the DCT must dominate *every* edge, including those in sparse regions where the trail has no room to manoeuvre.
- **Extremal/degree methods saturate.** Ore-, Chvátal–Erdős- and closure-type conditions all impose degree or independence-number bounds; a $4$-connected claw-free graph may have $\delta = 4$ and independence number $\Theta(n)$, outside every such window. Kaiser–Vrána's proof consumes $\delta \ge 6$ exactly to run a "stable-set / edge-cut" counting argument that collapses at $\delta = 4,5$.
- **Structure theorem is too coarse.** Chudnovsky–Seymour decompose claw-free graphs into line graphs, circular interval graphs, and thickenings of a bounded list of basic classes glued along strips. Hamiltonicity is not preserved or easily recombined across strip-gluings: a Hamilton cycle in the pieces need not concatenate, and the number of strip crossings is not controlled by $4$-connectivity.
- **Reduction to cubic graphs meets snark-like resistance.** After Fleischner–Jackson, the hard instances are cyclically $4$-edge-connected cubic graphs — precisely the family where cycle double covers, Fulkerson's conjecture and dominating-cycle problems all remain open. Techniques that succeed there (Kaiser–Škrekovski's $2$-factor arguments, Thomassen-style contractibility) produce $2$-factors, not connected trails; converting a $2$-factor into a single closed trail is the same "connectivity of the cycle space selection" obstacle that blocks the CDC conjecture.

## 6. The Gap

Proved: Hamiltonicity for $\kappa \ge 5$ with $\delta \ge 6$ (and unconditionally for $\kappa \ge 7$). Conjectured: $\kappa \ge 4$, no degree hypothesis. The gap is the interval
$$\kappa(G) = 4, \quad \text{or} \quad \kappa(G)\in\{5,6\} \text{ with } \delta(G) \le 5 .$$
In line-graph language: for essentially $4$-edge-connected $H$ with $\delta(H) = 3$, produce a dominating closed trail. Kaiser–Vrána's argument builds the trail from a system of edge-cuts and needs enough "spare" edges at each vertex of the trail; at $\delta = 3$ every vertex is tight, and every local repair step can fail. The precise missing step is a *connectivity-preserving augmentation*: given a dominating even subgraph (a $2$-factor-like object obtainable at $\delta = 3$), merge its components into one closed trail using only the four independent paths guaranteed by essential $4$-edge-connectivity. No known lemma performs this merge without an extra degree or cut-density assumption.

## 7. Current Research (as of June 2026)

- **Pilsen school (Ryjáček, Vrána, and coauthors, University of West Bohemia).** Refinements of closure operations — multigraph closures, $M$-closures, and closures preserving Hamilton-connectedness — plus systematic classification of forbidden pairs $\{K_{1,3}, X\}$ forcing Hamiltonicity in $3$-connected graphs. The current frontier of that programme is $Z_i$-free classes with $i$ growing.
- **Kaiser–Vrána line.** Attempts to remove the $\delta \ge 6$ hypothesis from the $5$-connected theorem via improved edge-cut/stable-set trade-offs *(frontier — verify)*.
- **Chinese school (Lai, Xiong, Shao, and collaborators).** Essential-connectivity thresholds for $3$-connected line graphs, pushing the "essentially $k$-connected" constant below $11$, and supereulerian-graph techniques (collapsible-graph reductions of Catlin) applied to DCT existence.
- **Cubic-graph reformulation.** Groups working on cycle double covers and dominating cycles (Kaiser, Škrekovski, Mácajová, Škoviera) treat the cyclically $4$-edge-connected cubic case as a testbed; flow- and nowhere-zero-flow reformulations of DCT existence are being explored.
- **Computational search.** Generation of cyclically $4$-edge-connected cubic graphs (via `genreg`/`snarkhunter`-style tools) with automated DCT testing, aiming either at a counterexample or at structural hypotheses *(frontier — verify: no published exhaustive DCT census beyond ~32 vertices is confirmed)*.

## 8. Future Work

- **Attack the equivalent $1$-Hamilton-connectedness form.** Ryjáček–Vrána showed it is equivalent but formally stronger-looking; the extra subdivided edge sometimes gives an induction handle unavailable to the plain statement.
- **Interpolate between $2$-factors and trails.** Prove that every essentially $4$-edge-connected cubic graph has a dominating even subgraph with at most $k$ components for an absolute $k$, then attack the merge. Even $k = 2$ unconditionally would be new.
- **Use Chudnovsky–Seymour constructively.** Develop a Hamiltonicity-preserving calculus for strip structures, so that $4$-connectivity of the whole forces enough crossings at each gluing.
- **Sharpen Catlin's reduction method.** Collapsible-graph contraction gives supereulerian conclusions under $4$-edge-connectivity; extending it to *essential* $4$-edge-connectivity with degree-$3$ vertices is a concrete, self-contained subproblem.
- **Look for a counterexample where none is expected.** The Fleischner–Jackson reduction makes the search space explicit; a snark-like cubic graph with no DCT would settle the problem negatively and simultaneously break Thomassen's conjecture.

## 9. Key References

- **[Foundational]** M. M. Matthews, D. P. Sumner. *Hamiltonian results in $K_{1,3}$-free graphs.* Journal of Graph Theory 8 (1984), 139–146.
- **[Foundational]** F. Harary, C. St. J. A. Nash-Williams. *On eulerian and hamiltonian graphs and line graphs.* Canadian Mathematical Bulletin 8 (1965), 701–709.
- **[Foundational]** C. Thomassen. *Reflections on graph theory.* Journal of Graph Theory 10 (1986), 309–324.
- **[Foundational]** W. T. Tutte. *A theorem on planar graphs.* Transactions of the American Mathematical Society 82 (1956), 99–116.
- **[Key technique]** Z. Ryjáček. *On a closure concept in claw-free graphs.* Journal of Combinatorial Theory, Series B 70 (1997), 217–224.
- **[Reduction]** H. Fleischner, B. Jackson. *A note concerning some conjectures on cyclically 4-edge-connected 3-regular graphs.* Annals of Discrete Mathematics 41 (1989), 171–177.
- **[SOTA]** T. Kaiser, P. Vrána. *Hamilton cycles in 5-connected line graphs.* European Journal of Combinatorics 33 (2012), 924–947.
- **[SOTA]** S. Zhan. *On hamiltonian line graphs and connectivity.* Discrete Mathematics 89 (1991), 89–95.
- **[SOTA]** H.-J. Lai, Y. Shao, H. Wu, J. Zhou. *Every 3-connected, essentially 11-connected line graph is hamiltonian.* Journal of Combinatorial Theory, Series B 96 (2006), 571–576.
- **[SOTA]** T. Kaiser, M.-C. Li, Z. Ryjáček, L. Xiong. *Hourglasses and Hamilton cycles in 4-connected claw-free graphs.* Journal of Graph Theory 48 (2005), 267–276.
- **[SOTA]** Z. Ryjáček, P. Vrána. *Line graphs of multigraphs and Hamilton-connectedness of claw-free graphs.* Journal of Graph Theory 66 (2011), 152–173.
- **[Related]** H. J. Broersma, M. Kriesell, Z. Ryjáček. *On factors of 4-connected claw-free graphs.* Journal of Graph Theory 37 (2001), 125–136.
- **[Related]** T. Kaiser, R. Škrekovski. *Cycles intersecting edge-cuts of prescribed sizes.* SIAM Journal on Discrete Mathematics 22 (2008), 861–874.
- **[Survey]** R. Faudree, E. Flandrin, Z. Ryjáček. *Claw-free graphs — a survey.* Discrete Mathematics 164 (1997), 87–147.
- **[Survey]** M. Chudnovsky, P. Seymour. *The structure of claw-free graphs.* In *Surveys in Combinatorics 2005*, London Math. Soc. Lecture Note Series 327, Cambridge University Press, 2005, 153–171.

## 10. Worked Example / Concrete Special Case

**Instance: $G = L(P)$, $P$ the Petersen graph.** Label $P$ with outer cycle $o_1\cdots o_5$, inner pentagram $i_1,\dots,i_5$ where $i_j \sim i_{j+2}$ (indices mod $5$), and spokes $o_j i_j$. Then $|E(P)| = 15$, so $G$ has $15$ vertices; $G$ is $4$-regular, claw-free, and since $P$ is cyclically $5$-edge-connected and cubic, $P$ is essentially $4$-edge-connected, giving $\kappa(G) \ge 4$. So $G$ is a legitimate instance of the conjecture.

**Step 1 — find a dominating closed trail in $P$.** $P$ is hypohamiltonian, so $P - o_1$ has a Hamilton cycle. Explicitly:
$$C:\quad o_2 - o_3 - o_4 - o_5 - i_5 - i_3 - i_1 - i_4 - i_2 - o_2 .$$
All nine edges are genuine edges of $P$ ($o_5i_5$ and $i_2o_2$ are spokes; $i_5i_3, i_3i_1, i_1i_4, i_4i_2$ are pentagram edges). $C$ covers every vertex except $o_1$, and the three edges at $o_1$ each have their other end on $C$. Hence $C$ is a DCT.

**Step 2 — account for the six edges off $C$.** $E(P) \setminus E(C) = \{o_1o_2,\ o_1o_5,\ o_1i_1,\ o_3i_3,\ o_4i_4,\ i_2i_5\}$; $9 + 6 = 15$. ✓

**Step 3 — lift to a Hamilton cycle of $L(P)$.** Traverse $C$; at each vertex, insert the off-trail edges incident there, each inserted exactly once (chord $i_2i_5$ at $i_5$; spokes at their outer end):
$$
\begin{aligned}
&(o_2o_3),\ (o_3i_3),\ (o_3o_4),\ (o_4i_4),\ (o_4o_5),\ (o_1o_5),\ (o_5i_5),\ (i_2i_5),\\
&(i_5i_3),\ (i_3i_1),\ (o_1i_1),\ (i_1i_4),\ (i_4i_2),\ (i_2o_2),\ (o_1o_2) \ \longrightarrow\ (o_2o_3).
\end{aligned}
$$
Consecutive pairs share an endvertex in $P$ (e.g. $(o_5i_5)$ and $(i_2i_5)$ share $i_5$; $(o_1o_2)$ and $(o_2o_3)$ share $o_2$), so each pair is an edge of $L(P)$; all $15$ vertices appear once. This is a Hamilton cycle. ✓

**What this shows and does not show.** The conjecture holds here, and the proof is entirely mechanical *once a DCT is exhibited*. The general problem is exactly Step 1: for an arbitrary essentially $4$-edge-connected cubic graph $H$ there is no known method to produce a dominating closed trail. For $P$ we exploited hypohamiltonicity — a coincidence of one graph, not a theorem about the class. Dropping to $\kappa = 3$ also breaks the conclusion: line graphs of $3$-edge-connected graphs without a DCT are $3$-connected, claw-free and non-Hamiltonian, and infinitely many exist (Matthews–Sumner 1984), which is why $4$ is the conjectured threshold.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*