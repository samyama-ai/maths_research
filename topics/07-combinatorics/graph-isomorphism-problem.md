---
id: 07-combinatorics/graph-isomorphism-problem
title: "Graph Isomorphism Problem"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Graph Isomorphism Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/graph-isomorphism-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Given two finite simple graphs $G$ and $H$ on $n$ vertices, decide whether there is a bijection $\varphi: V(G) \to V(H)$ with $\{u,v\} \in E(G) \iff \{\varphi(u),\varphi(v)\} \in E(H)$.

The open question is not decidability — brute force over $n!$ bijections settles it — but complexity:

- **Main open problem (GI in P?).** Is there a deterministic algorithm deciding graph isomorphism in time $n^{O(1)}$?
- **Complementary open problem.** Is GI NP-complete? Widely believed no, and known to imply $\Sigma_2^p = \Pi_2^p$ (collapse of the polynomial hierarchy to its second level).

The current record is Babai's quasipolynomial bound $n^{O(\log^2 n)} = 2^{O((\log n)^3)}$. A complete resolution means either a polynomial-time algorithm (with proof of correctness and termination) or a superpolynomial lower bound in a general model — the latter being far out of reach, since it would separate P from a class containing GI.

A stronger target is **canonisation**: compute a function $\mathrm{Can}(G)$ with $\mathrm{Can}(G) = \mathrm{Can}(H) \iff G \cong H$. Polynomial canonisation implies polynomial isomorphism testing; the converse is open.

## 2. Mathematical Foundations

**Automorphism group.** $\mathrm{Aut}(G) \le \mathrm{Sym}(V)$ is the stabiliser of $E(G)$ under the induced action on $\binom{V}{2}$. If $G \cong H$ then the set of isomorphisms is a coset $\varphi\,\mathrm{Aut}(G)$, so isomorphism testing and automorphism-group computation are polynomial-time equivalent (search-to-decision reduction, Mathon 1979).

**Adjacency formulation.** With adjacency matrices $A_G, A_H \in \{0,1\}^{n\times n}$,
$$G \cong H \iff \exists P \in \Pi_n : P A_G P^{\mathsf T} = A_H,$$
where $\Pi_n$ is the set of $n \times n$ permutation matrices. Relaxing $\Pi_n$ to doubly stochastic matrices gives the *fractional* relaxation, which is necessary but not sufficient.

**Weisfeiler–Leman (WL) refinement.** The $1$-dimensional (colour refinement) algorithm iterates
$$\chi^{t+1}(v) = \big(\chi^{t}(v), \{\!\{ \chi^{t}(u) : u \in N(v) \}\!\}\big),$$
to a stable partition. The $k$-dimensional version colours $k$-tuples $\bar v \in V^k$ by
$$\chi^{t+1}(\bar v)=\Big(\chi^t(\bar v),\ \{\!\{\,(\chi^t(\bar v[1/w]),\dots,\chi^t(\bar v[k/w]))\ :\ w\in V\,\}\!\}\Big),$$
running in time $n^{O(k)}$. The **WL-dimension** of $G$ is the least $k$ with $k$-WL identifying $G$ among all graphs. Immerman–Lander: $k$-WL equivalence coincides with equivalence in the logic $C^{k+1}_{\infty\omega}$ ($(k{+}1)$-variable first-order logic with counting quantifiers).

**Group-theoretic model.** Luks's framework reduces isomorphism to *string isomorphism*: given $\Gamma \le \mathrm{Sym}(\Omega)$ by generators and $x,y: \Omega \to \Sigma$, decide whether $x^{\gamma} = y$ for some $\gamma \in \Gamma$. Algorithms recurse along the orbit/block structure of $\Gamma$, using polynomial-time permutation-group machinery (Sims's stabiliser chains, Schreier–Sims). The bottleneck is the *primitive* case, controlled by the classification of finite simple groups via Cameron's theorem: a large primitive group is (up to Cameron structure) $\mathrm{Alt}(m)^{(d)} \le \Gamma \le S_m \wr S_d$ acting on $k$-subsets.

**Complexity placement.** $\mathrm{GI} \in \mathrm{NP} \cap \mathrm{coAM}$, so GI is NP-complete only if PH collapses to $\Sigma_2^p$ (Boppana–Håstad–Zachos 1987, via Goldwasser–Sipser set lower bound on the Goldreich–Micali–Wigderson interactive proof for non-isomorphism). GI is not known to be in coNP unconditionally, is low for $\mathrm{PP}$ and for $\Sigma_2^p$ (Köbler–Schöning–Torán), and is not known to be P-hard.

## 3. History & State of the Art (SOTA)

- **1950s–60s.** Formulated in chemical documentation (Morgan's algorithm, 1965) and in Ulam's reconstruction circle; recognised as a computational problem early in the NP-completeness era.
- **1979.** Garey and Johnson list GI as one of the few natural problems in NP neither known to be in P nor NP-complete — its "NP-intermediate" status becomes canonical.
- **1980–1983.** Babai's $n^{O(\log n)}$ bound for graphs of bounded colour class size; Furst–Hopcroft–Luks polynomial permutation-group algorithms; **Luks (1982)**: isomorphism of graphs of bounded degree $d$ in $n^{O(d)}$.
- **1983.** Babai–Luks canonical labelling; combined with Zemlyachenko's degree reduction gives the general bound $\exp\big(O(\sqrt{n\log n})\big)$, which stood for 32 years.
- **1992.** Cai–Fürer–Immerman construct graphs on $O(k)$ vertices not distinguished by $k$-WL, killing the hope that bounded-dimension WL suffices.
- **2015–2017.** **Babai** announces and proves $\exp\big((\log n)^{O(1)}\big)$. Helfgott finds an error in the timing analysis (Jan 2017); Babai repairs it within days, yielding $\exp\big(O((\log n)^3)\big)$; the STOC 2016 paper and Helfgott's Bourbaki exposé (2017) are the reference accounts. The result also gives quasipolynomial canonical forms.
- **2014–present.** Practical solvers — **nauty/Traces** (McKay & Piperno), **bliss**, **saucy**, **conauto** — handle most graphs with $10^5$–$10^7$ vertices in seconds; benchmark suites are dominated by hand-built hard families.

## 4. Partial Results / Verified Cases

Polynomial-time (often linear or near-linear) for:

- **Trees**: $O(n)$ (Aho–Hopcroft–Ullman 1974); **planar graphs**: $O(n)$ (Hopcroft–Wong 1974).
- **Bounded genus** $g$: polynomial (Filotti–Mayer; Miller 1980), and FPT in $g$ (Kawarabayashi 2015).
- **Bounded degree** $d$: $n^{O(d)}$ (Luks 1982); improved to $n^{O(d/\log d)}$ (Babai–Luks style, Grohe–Neuen–Schweitzer 2018).
- **Bounded treewidth** $k$: $2^{k\,\mathrm{polylog}(k)}\,n^{O(1)}$ (Lokshtanov–Pilipczuk–Pilipczuk–Saurabh 2017); bounded **rank width** and **clique width**: FPT (Grohe–Schweitzer 2015).
- **Excluded minor** / excluded topological subgraph: polynomial (Ponomarenko 1988) and FPT (Grohe–Marx 2015; Grohe–Neuen–Schweitzer–Wiebking 2020).
- **Bounded eigenvalue multiplicity** $m$: $n^{O(m)}$ (Babai–Grigoryev–Mount 1982).
- **Interval graphs** (Lueker–Booth 1979), **permutation graphs**, **circular-arc graphs**, **graphs of bounded colour class size**, **strongly regular graphs**: $n^{O(\log n)}$ time (Spielman 1996; refined by Babai 2015).
- **Random graphs** $G(n,1/2)$: canonical form in $O(n^2)$ time whp — degree sequence plus one refinement round distinguishes vertices (Babai–Erdős–Selkow 1980).
- **WL-dimension bounds**: planar graphs have WL-dimension $\le 3$ (Kiefer–Ponomarenko–Schweitzer 2019); graphs with excluded minor $K_k$ have WL-dimension bounded by a function of $k$ (Grohe 2017).

GI-complete (equivalent to the general case): isomorphism of hypergraphs, bipartite graphs, regular graphs, chordal graphs, and self-complementary graphs; also finite-automata and semigroup isomorphism.

## 5. Principal Obstacles

- **Combinatorial refinement provably fails.** CFI graphs give, for each $k$, non-isomorphic $G,H$ on $O(k)$ vertices with $k$-WL$(G) = k$-WL$(H)$. Since $k$-WL costs $n^{O(k)}$, no fixed-dimension refinement is a decision procedure. Equivalently, there is no logic capturing PTIME on all graphs via counting logics — a direct obstacle in descriptive complexity.
- **Individualisation–refinement has exponential worst case.** Every practical solver individualises vertices then refines. Neuen–Schweitzer (2018) construct graph families forcing $2^{\Omega(n)}$ search-tree nodes for all standard IR solvers with any pruning by refinement, so the engineering line cannot reach P by itself.
- **Group theory bottleneck.** Luks-style recursion is polynomial except when the primitive quotient is a large alternating group acting on $k$-subsets ("Johnson group" case). Babai's Split-or-Johnson and Local Certificates machinery handles this at the cost of a $(\log n)^{O(1)}$ multiplicative recursion depth. Removing that factor would need either a polynomial-depth recursion (no known route) or a fundamentally non-group-theoretic idea.
- **Algebraic relaxations are too weak.** Doubly stochastic / Lasserre / Sherali–Adams relaxations at level $k$ are dominated by $k$-WL (Atserias–Maneva; Grohe–Otto), so they inherit the CFI barrier. Sum-of-squares of degree $\Theta(n)$ is needed on CFI-like instances (O'Donnell–Wright–Wu–Zhou 2014).
- **No lower-bound technology.** Proving GI $\notin$ P is beyond current techniques (natural proofs / relativisation barriers), and GI is not known even to be P-hard, so hardness intuition is thin in both directions.

## 6. The Gap

Section 4 gives polynomial algorithms for structurally restricted classes and a quasipolynomial algorithm in general. The gap is exactly the factor $(\log n)^{O(1)}$ in the exponent of Babai's bound.

Concretely, Babai's algorithm recurses with multiplicative cost $q(n) = n^{O(\log n)}$ per level over $O(\log n)$ levels, arising from the Local Certificates routine's handling of Johnson-type primitive groups on $\binom{[m]}{k}$. Closing the gap requires one of:

1. A recursion for string isomorphism under $\mathrm{Alt}(m)$-type groups with *constant* branching per level, i.e. $\mathrm{poly}(n)$ total; or
2. A polynomially computable complete invariant not based on WL — necessarily one immune to the CFI construction, hence not expressible in bounded-variable counting logic; or
3. A proof that isomorphism of *strongly regular graphs*, or of Steiner systems, admits polynomial-time testing — currently at $n^{O(\log n)}$ and widely regarded as the hardest structured core.

## 7. Current Research (as of June 2026)

- **Group-theoretic algorithms.** Groups around Babai (Chicago), Wiebking, Neuen (RWTH Aachen/Bonn), Schweitzer (Kaiserslautern) refine the quasipolynomial framework toward *canonisation with hypergraph and Steiner-system primitives*, and toward FPT results parameterised by minors, degree, and Euler genus.
- **WL-dimension and descriptive complexity.** Kiefer, Ponomarenko, Grohe: exact WL-dimension of minor-closed classes; the Grohe programme proving that CPT (Choiceless Polynomial Time with counting) or rank logic captures PTIME on restricted classes. Dawar–Grädel and coauthors showed rank logic does *not* capture PTIME (2019), redirecting effort to CPT.
- **Group isomorphism.** The $n^{\Theta(\log n)}$ barrier for isomorphism of groups of order $n$ given by Cayley table remains; recent work by Sun, Grochow–Qiao gives polynomial algorithms for broad classes of $p$-groups. *(frontier — verify)*
- **Practical solvers.** Successor versions of Traces and new SAT/CP-hybrid canonisers; benchmark families from Neuen–Schweitzer remain the discriminating tests.
- **Quantum and spectral.** No quantum speedup is known; the hidden-subgroup approach over $S_n$ is obstructed by Moore–Russell–Schulman's result that coset-state measurements require highly entangled multi-register measurements.

## 8. Future Work

- Push the exponent from $(\log n)^3$ to $(\log n)^{1+o(1)}$ by improving Split-or-Johnson, a step Babai has flagged as the natural next milestone.
- Settle strongly regular graph isomorphism in polynomial time; Spielman's $n^{O(n^{1/3}\log n)}$-era techniques plus modern coherent-configuration theory are the main tools.
- Determine whether polynomial canonisation is equivalent to polynomial isomorphism testing.
- Find a logic capturing PTIME (Gurevich's conjecture is that none exists); a proof either way reshapes the CFI barrier.
- Prove or refute that GI is in coNP unconditionally, or derandomise the AM protocol for non-isomorphism under plausible hardness assumptions (Klivans–van Melkebeek gives conditional derandomisation).

## 9. Key References

- **[Foundational]** Luks, E. M. *Isomorphism of graphs of bounded valence can be tested in polynomial time.* Journal of Computer and System Sciences 25(1), 42–65, 1982.
- **[Foundational]** Babai, L.; Luks, E. M. *Canonical labeling of graphs.* Proceedings of the 15th ACM Symposium on Theory of Computing (STOC), 171–183, 1983.
- **[Foundational]** Cai, J.-Y.; Fürer, M.; Immerman, N. *An optimal lower bound on the number of variables for graph identification.* Combinatorica 12(4), 389–410, 1992.
- **[SOTA]** Babai, L. *Graph isomorphism in quasipolynomial time.* Proceedings of the 48th ACM Symposium on Theory of Computing (STOC), 684–697, 2016. arXiv:1512.03547.
- **[SOTA]** Helfgott, H. A.; Bajpai, J.; Dona, D. *Graph isomorphisms in quasi-polynomial time.* Séminaire Bourbaki, Exposé 1125, 2017. arXiv:1710.04574.
- **[SOTA]** Grohe, M.; Neuen, D.; Schweitzer, P. *A faster isomorphism test for graphs of small degree.* SIAM Journal on Computing 52(6), 2023 (FOCS 2018).
- **[SOTA]** Neuen, D.; Schweitzer, P. *An exponential lower bound for individualization-refinement algorithms for graph isomorphism.* STOC 2018, 138–150.
- **[Survey]** Grohe, M.; Schweitzer, P. *The graph isomorphism problem.* Communications of the ACM 63(11), 128–134, 2020.
- **[Survey]** Grohe, M. *Descriptive Complexity, Canonisation, and Definable Graph Structure Theory.* Cambridge University Press (Lecture Notes in Logic 47), 2017.
- **[Book]** Köbler, J.; Schöning, U.; Torán, J. *The Graph Isomorphism Problem: Its Structural Complexity.* Birkhäuser, 1993.
- **[Practical]** McKay, B. D.; Piperno, A. *Practical graph isomorphism, II.* Journal of Symbolic Computation 60, 94–112, 2014.
- **[Complexity]** Boppana, R.; Håstad, J.; Zachos, S. *Does co-NP have short interactive proofs?* Information Processing Letters 25(2), 127–132, 1987.

## 10. Worked Example / Concrete Special Case

**Why colour refinement fails on regular graphs.** Let $G = C_6$ (6-cycle) and $H = C_3 \sqcup C_3$ (two disjoint triangles). Both are 2-regular on 6 vertices.

1-WL: every vertex starts with colour $c_0$. Then $\chi^1(v) = (c_0, \{\!\{c_0,c_0\}\!\})$ for all $v$ in both graphs. The partition is already stable, so 1-WL returns identical colour multisets $\{\!\{c_1^{\,6}\}\!\}$ — it cannot separate them, though $C_6$ is connected and $H$ is not.

2-WL separates them. Colour pairs by $\chi^0(u,v) \in \{\textsf{eq}, \textsf{adj}, \textsf{non}\}$. For an adjacent pair $(u,v)$ in $H$, the unique third vertex $w$ of its triangle satisfies $(u,w)$ adjacent and $(w,v)$ adjacent, so the multiset over $w$ contains $(\textsf{adj},\textsf{adj})$ once. In $C_6$ no $w$ is adjacent to both endpoints of an edge, so that pair never appears. Hence $\chi^1$ differs after one round: 2-WL certifies $C_6 \not\cong C_3\sqcup C_3$.

**Counting the automorphisms.** $\mathrm{Aut}(C_6) = D_6$, of order $12$. $\mathrm{Aut}(C_3 \sqcup C_3) = D_3 \wr S_2$, of order $6^2 \cdot 2 = 72$. Different orders confirm non-isomorphism independently.

**The CFI escalation.** Cai–Fürer–Immerman replace each vertex of a degree-3 expander $X$ on $k$ vertices by a gadget of 4 inner vertices encoding the parity of a $\mathbb{F}_2$-vector; each edge becomes a pair of "wires". Twisting exactly one edge flips global parity, producing $G_X \not\cong \tilde G_X$ on $n = O(k)$ vertices. Because the expander has treewidth $\Omega(k)$, a $k$-tuple of pebbles cannot cut the graph, and Duplicator wins the $(k{+}1)$-pebble bijective game: $k$-WL$(G_X) = k$-WL$(\tilde G_X)$. Setting $k = \Theta(n)$ shows the WL hierarchy needs linear dimension in the worst case, i.e. $n^{\Theta(n)}$ time — the exact reason the combinatorial route alone cannot deliver a polynomial algorithm.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*