---
id: 07-combinatorics/berge-fulkerson-conjecture
title: "Berge-Fulkerson Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Berge-Fulkerson Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/berge-fulkerson-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Berge–Fulkerson).** Every bridgeless cubic graph $G$ admits a list of six perfect matchings $M_1,\dots,M_6$ (repetitions allowed) such that every edge of $G$ belongs to exactly two of them.

Such a list is a *Fulkerson cover*, and $G$ is said to have a *Berge–Fulkerson colouring*. Graphs are finite, may have parallel edges, and "bridgeless" means 2-edge-connected (a cubic graph with a bridge has an edge in no perfect matching, so the hypothesis is necessary).

A proof must produce, for every bridgeless cubic graph, the six matchings — or an algorithmic/structural argument establishing their existence. A disproof requires exhibiting one bridgeless cubic graph, necessarily a snark, with no such family. Counting is forced: $\sum_i |M_i| = 6 \cdot |V|/2 = 3|V| = 2|E|$, so the multiplicity 2 is the only value consistent with six matchings.

## 2. Mathematical Foundations

Let $G=(V,E)$ be cubic, $|V|=n$, $|E|=3n/2$. A **perfect matching** $M \subseteq E$ satisfies $|M \cap \delta(v)| = 1$ for all $v$, where $\delta(v)$ is the edge set at $v$. Writing $\chi^M \in \{0,1\}^E$ for the incidence vector, the conjecture asks for $M_1,\dots,M_6$ with

$$\sum_{i=1}^{6} \chi^{M_i} = 2 \cdot \mathbf{1}_E .$$

**Fractional version (true).** By Edmonds' perfect matching polytope theorem, $x \in \mathbb{R}^E_{\ge 0}$ lies in the perfect matching polytope $\mathrm{PM}(G)$ iff $x(\delta(v))=1$ for all $v$ and $x(\delta(S)) \ge 1$ for all odd $S \subseteq V$. For bridgeless cubic $G$, $x = \tfrac13 \mathbf{1}_E$ satisfies both (odd cuts in a bridgeless cubic graph have size $\ge 3$), so

$$\tfrac{1}{3}\mathbf{1}_E \in \mathrm{PM}(G).$$

Hence $\mathbf{1}_E$ is a nonnegative rational combination of perfect matchings; clearing denominators, there is $k \ge 1$ and $3k$ perfect matchings covering each edge exactly $k$ times. Seymour (1979) established this and the associated $r$-graph framework. **Berge–Fulkerson asserts $k=2$ always works.**

**Reduction to snarks.** If $G$ is 3-edge-colourable, i.e. $E = N_1 \sqcup N_2 \sqcup N_3$ with each $N_j$ perfect, then $(N_1,N_1,N_2,N_2,N_3,N_3)$ is a Fulkerson cover. So only *snarks* — bridgeless cubic graphs with chromatic index 4, usually required cyclically 4-edge-connected with girth $\ge 5$ to exclude trivial cases — matter.

**Structure of a cover.** In any Fulkerson cover the complement $\overline{M_i} = E \setminus M_i$ is a 2-factor, and $\sum_i \chi^{\overline{M_i}} = 4\cdot\mathbf{1}_E$: the six 2-factors form a *quadruple cover* by cycles. Also $M_i \cap M_j$ for $i \ne j$ is an independent-edge set, and $M_1 \cup M_2 \cup \dots$ gives $E$; in particular $M_1 \cup M_2 \cup M_3$ need not be all of $E$, and the complement $E \setminus (M_1\cup M_2 \cup M_3) = M_4 \cap M_5 \cap M_6$-type relations constrain intersection patterns.

**Related statements.**
- **Berge's conjecture:** the edges of any bridgeless cubic graph are covered by 5 perfect matchings. Mazzuoccolo (2011) proved Berge $\Leftrightarrow$ Berge–Fulkerson.
- **Fan–Raspaud (1994):** there exist perfect matchings with $M_1\cap M_2 \cap M_3 = \emptyset$ — implied by Berge–Fulkerson, still open.
- **Petersen colouring conjecture (Jaeger):** every bridgeless cubic $G$ has $\varphi: E(G) \to E(P)$ ($P$ = Petersen graph) mapping each $\delta(v)$ onto some $\delta(u)$. This implies Berge–Fulkerson, since $P$ itself has a Fulkerson cover and pullbacks of its matchings work.
- **Excessive index** $\chi'_e(G)$: the least number of perfect matchings whose union is $E$. Berge–Fulkerson $\Rightarrow \chi'_e(G) \le 5$ for bridgeless cubic $G$.
- **Short cycle covers:** Fan–Raspaud showed Berge–Fulkerson implies every bridgeless graph has a cycle cover of total length $\le \tfrac{7}{5}|E|$.

## 3. History & State of the Art (SOTA)

Claude Berge circulated the 5-matching covering statement in the late 1960s (unpublished lecture notes). D. R. Fulkerson stated the 6-matching, multiplicity-2 form in *Blocking and anti-blocking pairs of polyhedra* (Math. Programming, 1971), where it appears as a natural integrality question for the blocker of the perfect matching polytope: the fractional statement is a theorem, and Fulkerson asked whether the specific integral rounding with $k=2$ holds.

Seymour (1979) put the problem in the general $r$-graph setting and proved the fractional/multi-cover version, plus the conjecture for planar cubic graphs (where it follows from the Four Colour Theorem via 3-edge-colourability). Jaeger (1985, 1988) introduced Petersen colourings, giving a strictly stronger conjecture. Fan and Raspaud (1994) extracted the weaker intersection-free formulation and connected the conjecture to short cycle covers. Máčajová and Škoviera (2005) recast it as a Fano-plane colouring problem. Mazzuoccolo (2011) proved the equivalence of the Berge and Fulkerson forms, closing a long-standing question about the relation between "5 covering" and "6 with multiplicity 2".

SOTA is split three ways: (i) *approximation* — how much of $E$ a few perfect matchings can cover; (ii) *special classes* — explicit covers for named snark families; (iii) *computation* — exhaustive verification for small snarks. No general structural approach is known.

## 4. Partial Results / Verified Cases

- **3-edge-colourable cubic graphs (Class 1):** trivially true, each colour class doubled. Includes all planar bridgeless cubic graphs (Four Colour Theorem) and all bridgeless cubic graphs with a Hamiltonian cycle on an even number of vertices.
- **Computational verification:** all snarks with at most $36$ vertices satisfy the conjecture — Brinkmann, Goedgebeur, Hägglund and Markström (JCTB 2013), which also generated the complete snark catalogue to $n=36$ and checked several equivalent formulations.
- **Named families:** explicit Fulkerson covers exist for the Petersen graph, the flower snarks $J_{2k+1}$, the Blanuša families, the Goldberg snarks, and all snarks with a Petersen colouring (Hägglund–Steffen, Ars Math. Contemp. 2014).
- **Low oddness:** Hao, Niu, Wang, C.-Q. Zhang and T. Zhang (Discrete Math. 2009) proved Berge–Fulkerson colourability for cubic graphs of oddness $2$, i.e. having a 2-factor with exactly two odd circuits; further oddness-based classes appear in Steffen (JGT 2015).
- **Coverage bounds (approximate versions):** Kaiser, Král' and Norine (2006) proved two perfect matchings of a bridgeless cubic graph can be chosen covering at least $\tfrac{3}{5}|E|$ edges, and that some choice of three covers at least $\tfrac{27}{35}|E|$ — versus the $|E|$ that Berge would give with five.
- **Lower-bound side:** Esperet and Mazzuoccolo (JGT 2014) exhibited an infinite family of bridgeless cubic graphs whose edge set cannot be covered by four perfect matchings, so the number $5$ in Berge's form cannot be lowered.
- **Cycle-cover consequence, unconditional:** Kaiser, Král', Lidický, Nejedlý and Šámal (SIAM J. Discrete Math. 2010) proved every bridgeless cubic graph has a cycle cover of length $\le \tfrac{34}{21}|E| \approx 1.619|E|$, still short of the $\tfrac{7}{5}|E|$ that Berge–Fulkerson would deliver.

## 5. Principal Obstacles

- **No induction that preserves the class.** Standard reductions on snarks (contracting a cyclic 4-cut, removing a vertex, reducing a 5-cycle) destroy either cubicity or bridgelessness, and a Fulkerson cover of a reduced graph does not lift: the six matchings must agree in *multiplicity pattern* across the cut, and there are many incompatible patterns on a $4$-cut. Snarks resist minimal-counterexample arguments because no useful "smallest snark" structure theory exists.
- **Polyhedral methods stop at the fractional statement.** Edmonds' theorem gives $\tfrac13\mathbf{1} \in \mathrm{PM}(G)$ immediately, but the perfect matching polytope has exponentially many facets and vertices; nothing in linear programming forces a rational point with denominator $2$ to be an average of exactly six vertices. Carathéodory-type bounds give $|E|+1$ matchings, not six.
- **Integrality gap is real, not an artefact.** Petersen-like obstructions show $\chi'_e$ can genuinely be $5$ (Esperet–Mazzuoccolo), so any proof must be tight; there is no slack to absorb errors, and probabilistic/greedy arguments lose a constant fraction of edges — the $\tfrac35$ and $\tfrac{27}{35}$ bounds are the limit of the "pick matchings covering much" strategy.
- **Flow and homomorphism techniques do not reach it.** Nowhere-zero-flow machinery handles cycle covers and 3-flows but a Fulkerson cover is not expressible as a flow condition; the natural encoding, Petersen colouring, is a strictly harder open conjecture.
- **Algebraic certificates are absent.** Unlike Tutte-type theorems there is no known polynomial identity, matroid, or eigenvalue quantity whose vanishing certifies a Fulkerson cover, so no algebraic obstruction can be ruled out globally.
- **Search space explosion.** Verification is exponential: a snark on $n$ vertices can have exponentially many perfect matchings, and choosing 6 with an exact multiplicity constraint is a covering-design search; this is why exhaustive checks stall around $n=36$.

## 6. The Gap

Proven: the fractional relaxation ($\exists k$: $3k$ matchings covering each edge $k$ times), the case $k=1$ for Class 1 graphs, low-oddness classes, named families, and all snarks to $36$ vertices. Conjectured: $k = 2$ for **every** bridgeless cubic graph.

The precise missing step is an *integral rounding of the perfect matching polytope at denominator 2*: converting the certificate $\tfrac13\mathbf{1}_E \in \mathrm{PM}(G)$ into a representation as an average of six vertices of $\mathrm{PM}(G)$, uniformly over all snarks. Equivalently, closing the gap from "three matchings cover $\ge \tfrac{27}{35}|E|$" and "four matchings can fail" to "five matchings always suffice". A second, equally acceptable route is a structure theorem for snarks strong enough to support induction across cyclic 4- and 5-cuts with a bounded set of boundary patterns.

## 7. Current Research (as of June 2026)

- **Approximate covering ratios.** Groups around Grenoble (Esperet), Modena (Mazzuoccolo) and Prague (Král', Šámal) continue pushing the fraction of $E$ covered by 2, 3 or 4 perfect matchings, and the associated normal/strong-edge-colouring parameters. Any bound of the form "four matchings cover $\ge (1-\varepsilon)|E|$ with a controlled remainder" would be a major step. *(frontier — verify)*
- **Petersen colourings and normal colourings.** Máčajová, Škoviera and coauthors (Bratislava) study normal 5-edge-colourings and normal 6-edge-colourings, a chain of statements between Berge–Fulkerson and the Petersen colouring conjecture.
- **Oddness and resistance parameters.** Steffen's programme relates oddness, resistance $r(G)$ (edges to delete for Class 1) and cover length; extending Berge–Fulkerson from oddness 2 to oddness 4 is an actively attacked target. *(frontier — verify)*
- **Computational extension.** Goedgebeur's snark generation code (Ghent) has been extended past $n=36$ for restricted girth/connectivity classes; no counterexample has surfaced. *(frontier — verify)*
- **SAT/ILP certificates.** Encoding the six-matching condition into SAT with symmetry breaking is used to test candidate hard instances (Loupekine, permutation and superposition snarks) quickly.

## 8. Future Work

- Prove Fan–Raspaud in full first: it is the weakest nontrivial consequence and a proof would validate the "choose matchings with controlled intersections" method.
- Establish $\chi'_e(G) \le 5$ for cyclically 5-edge-connected snarks of bounded oddness, then remove the oddness bound.
- Develop a cut-pattern calculus: classify the possible restrictions of a Fulkerson cover to a $k$-edge-cut for $k \le 6$, and prove a gluing lemma — the missing ingredient for induction.
- Improve the unconditional shortest cycle cover bound below $\tfrac{34}{21}|E|$ toward $\tfrac{7}{5}|E|$; the conjectured value is the natural stopping point and progress there tracks progress on the conjecture.
- Search for a counterexample among high-oddness superposition snarks, where the number of perfect matchings is small relative to $|E|$.

## 9. Key References

- **[Foundational]** D. R. Fulkerson. *Blocking and anti-blocking pairs of polyhedra.* Mathematical Programming 1 (1971), 168–194.
- **[Foundational]** P. D. Seymour. *On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte.* Proceedings of the London Mathematical Society (3) 38 (1979), 423–460.
- **[Foundational]** F. Jaeger. *Nowhere-zero flow problems.* In: Selected Topics in Graph Theory 3, Academic Press, 1988, 71–95.
- **[Key]** G. Fan, A. Raspaud. *Fulkerson's Conjecture and Circuit Covers.* Journal of Combinatorial Theory, Series B 61 (1994), 133–138.
- **[Key]** E. Máčajová, M. Škoviera. *Fano colourings of cubic graphs and the Fulkerson conjecture.* Theoretical Computer Science 349 (2005), 112–120.
- **[Key]** T. Kaiser, D. Král', S. Norine. *Unions of perfect matchings in cubic graphs.* In: Topics in Discrete Mathematics, Algorithms and Combinatorics 26, Springer, 2006, 225–230.
- **[Key]** G. Mazzuoccolo. *The equivalence of two conjectures of Berge and Fulkerson.* Journal of Graph Theory 68 (2011), 125–128.
- **[SOTA / Recent]** L. Esperet, G. Mazzuoccolo. *On cubic bridgeless graphs whose edge-set cannot be covered by four perfect matchings.* Journal of Graph Theory 77 (2014), 144–157.
- **[SOTA / Recent]** G. Brinkmann, J. Goedgebeur, J. Hägglund, K. Markström. *Generation and properties of snarks.* Journal of Combinatorial Theory, Series B 103 (2013), 468–488.
- **[SOTA / Recent]** J. Hägglund, E. Steffen. *Petersen colorings and some families of snarks.* Ars Mathematica Contemporanea 7 (2014), 161–173.
- **[SOTA / Recent]** E. Steffen. *1-factor and cycle covers of cubic graphs.* Journal of Graph Theory 78 (2015), 195–206.
- **[Partial]** R. Hao, J. Niu, X. Wang, C.-Q. Zhang, T. Zhang. *A note on Berge–Fulkerson coloring.* Discrete Mathematics 309 (2009), 4235–4240.
- **[Related bound]** T. Kaiser, D. Král', B. Lidický, P. Nejedlý, R. Šámal. *Short cycle covers of graphs with minimum degree three.* SIAM Journal on Discrete Mathematics 24 (2010), 330–355.
- **[Survey / Book]** C.-Q. Zhang. *Circuit Double Cover of Graphs.* London Mathematical Society Lecture Note Series 399, Cambridge University Press, 2012.

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$ — the smallest snark, and a tight instance.**

Label the outer 5-cycle $o_0,\dots,o_4$ (edges $o_i o_{i+1}$), the inner pentagram $u_0,\dots,u_4$ (edges $u_i u_{i+2}$), and spokes $s_i = o_i u_i$; indices mod 5. Then $|V|=10$, $|E|=15$. $P$ is not 3-edge-colourable, so the trivial construction fails.

Take the six matchings:

$$M_\infty = \{s_0,s_1,s_2,s_3,s_4\},$$
$$M_i = \{\, s_i,\; o_{i+1}o_{i+2},\; o_{i+3}o_{i+4},\; u_{i+1}u_{i+3},\; u_{i+2}u_{i+4} \,\}, \quad i=0,\dots,4.$$

*Each is perfect.* $M_\infty$ covers all 10 vertices once. For $M_i$: the spoke covers $o_i,u_i$; the two outer edges cover $o_{i+1},o_{i+2},o_{i+3},o_{i+4}$; the two inner edges cover $u_{i+1},u_{i+3}$ and $u_{i+2},u_{i+4}$. Both inner edges are legal since the index differences are $2$. Total $2+4+4=10$ vertices, disjointly.

*Each edge is covered exactly twice.*

| edge type | in which matchings | count |
|---|---|---|
| spoke $s_j$ | $M_\infty$ and $M_j$ | 2 |
| outer $o_j o_{j+1}$ | $M_{j-1}$ (as $o_{i+1}o_{i+2}$) and $M_{j+2}$ (as $o_{i+3}o_{i+4}$) | 2 |
| inner $u_j u_{j+2}$ | $M_{j-1}$ (as $u_{i+1}u_{i+3}$) and $M_{j-2}$ (as $u_{i+2}u_{i+4}$) | 2 |

Check on $o_0 o_1$: it appears in $M_4$ (there $o_{i+1}o_{i+2} = o_0 o_1$) and in $M_3$ (there $o_{i+3}o_{i+4} = o_1 o_0$) — twice. Check on $u_0 u_2$: in $M_4$ ($u_{i+1}u_{i+3} = u_0 u_2$) and in $M_3$ ($u_{i+2}u_{i+4} = u_0 u_2$) — twice.

Global count: $6 \times 5 = 30 = 2 \times 15$. ✔

These are in fact *all* the perfect matchings of $P$ — it has exactly six, matching the six decompositions of $P$ into two disjoint 5-cycles (each $\overline{M}$ is such a 2-factor). So the Petersen graph has a Fulkerson cover with no freedom at all: the conjecture holds there with equality in the strongest sense. Its excessive index is $\chi'_e(P) = 5$ (any four of the six matchings miss an edge), confirming that the bound $5$ in Berge's form cannot be improved and explaining why $P$ is the universal target of the Petersen colouring conjecture, which would imply Berge–Fulkerson for every bridgeless cubic graph by pulling these six matchings back along $\varphi: E(G) \to E(P)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*