---
id: 07-combinatorics/graph-reconstruction-conjecture
title: "Graph Reconstruction Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Graph Reconstruction Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/graph-reconstruction-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple undirected graph on vertex set $V(G)$ with $|V(G)| = n$. The **deck** of $G$ is the multiset of unlabelled induced subgraphs
$$\mathcal{D}(G) = \{\!\{\, G - v \;:\; v \in V(G) \,\}\!\},$$
each element $G-v$ being called a **card**, given only up to isomorphism.

**Conjecture (Kelly 1942/1957, Ulam 1960).** Every finite simple graph $G$ with $n \ge 3$ vertices is determined up to isomorphism by $\mathcal{D}(G)$: if $H$ is a graph with $\mathcal{D}(H) = \mathcal{D}(G)$ as multisets, then $H \cong G$.

The hypothesis $n \ge 3$ is necessary: $K_2$ and $\overline{K_2}$ both have deck $\{\!\{K_1, K_1\}\!\}$. The conjecture is stated for finite simple graphs only — it is **false** for digraphs and tournaments (Stockmeyer 1977), false for infinite graphs, false for hypergraphs (Kocay), and the multiset structure is essential (the *set* of cards does not suffice).

A proof must show injectivity of the deck map $G \mapsto \mathcal{D}(G)$ on isomorphism classes for all $n \ge 3$. A disproof requires exhibiting one pair $G \not\cong H$, $n \ge 3$, with identical decks.

**Companion (Harary 1964), Edge Reconstruction Conjecture.** Every simple graph with at least $4$ edges is determined by the multiset $\{\!\{\,G - e : e \in E(G)\,\}\!\}$. Vertex reconstructibility implies edge reconstructibility for graphs with $n\ge 4$ (Greenwell).

## 2. Mathematical Foundations

A graph parameter $p$ is **reconstructible** if $\mathcal{D}(G) = \mathcal{D}(H) \Rightarrow p(G) = p(H)$; a class $\mathcal{C}$ is **recognizable** if membership in $\mathcal{C}$ is reconstructible, and **reconstructible** if additionally every $G \in \mathcal{C}$ is determined by its deck.

**Kelly's Lemma (1957).** For graphs $F$ with $|V(F)| < |V(G)| = n$, let $s(F,G)$ denote the number of subsets $S \subseteq V(G)$ with $G[S] \cong F$. Then
$$s(F,G) \;=\; \frac{1}{\,n - |V(F)|\,}\sum_{v \in V(G)} s(F, G-v),$$
since each copy of $F$ survives in exactly $n - |V(F)|$ cards. Hence **every subgraph count of a proper induced subgraph is reconstructible**. Consequences:

- Edge count: $m(G) = \dfrac{1}{n-2}\sum_{v} m(G-v)$.
- Degree sequence: $\deg(v) = m(G) - m(G-v)$, so the multiset of degrees is reconstructible along with the pairing card $\leftrightarrow$ deleted degree.
- Connectedness, the number of components, and the complement's deck: $\mathcal{D}(\overline{G}) = \{\!\{\,\overline{G-v}\,\}\!\}$, so $G$ is reconstructible iff $\overline{G}$ is.

**Nash-Williams' counting / lemma.** For a set $\mathcal{X}$ of pairwise non-isomorphic graphs on $n$ vertices, if $\mathcal{D}(G)=\mathcal{D}(H)$ then for every $F$ on $n$ vertices with $F \not\cong G$,
$$s^*(F,G) = s^*(F,H),$$
where $s^*$ counts *spanning* subgraph copies; only the count $s^*(G,G)$ vs $s^*(G,H)$ can differ. This "one unknown coefficient" structure is the source of nearly all positive results, including Lovász's and Müller's edge-reconstruction bounds via the Möbius/inclusion–exclusion identity
$$\sum_{F \supseteq \text{spanning}} (-1)^{|E(F)|-|E(G)|}\, s^*(G,F) = \pm 1 .$$

**Tutte (1979).** The Tutte polynomial $T_G(x,y)$ is reconstructible; hence so are the chromatic polynomial, the number of spanning trees, the characteristic polynomial of the adjacency matrix, and the number of Hamiltonian cycles.

## 3. History & State of the Art (SOTA)

- **1942/1957.** P. J. Kelly's thesis under Ulam proves the tree case; published as *A congruence theorem for trees*, Pacific J. Math. 7 (1957).
- **1960.** Ulam states the problem in *A Collection of Mathematical Problems*, giving it wide circulation as the "Ulam conjecture".
- **1964.** Harary formulates the edge version and the modern terminology of "reconstruction".
- **1969–1978.** Structural era: Kelly's lemma, Nash-Williams' counting theorems, Greenwell–Hemminger's results on disconnected and separable graphs. Bondy–Hemminger's survey (1977) codifies the field.
- **1972/1977.** Lovász proves edge reconstructibility for $m > \tfrac12\binom{n}{2}$; Müller improves to $2^{m-1} > n!$, i.e. $m \gtrsim \tfrac12 n\log_2 n$.
- **1977.** Stockmeyer's infinite families of non-reconstructible tournaments and digraphs kill any purely counting-based proof that ignores undirectedness.
- **1988.** Yang Yongzhi reduces the conjecture to 2-connected graphs.
- **1990.** Bollobás: almost every graph has reconstruction number 3 — three well-chosen cards suffice with probability $\to 1$.
- **1991.** Bondy's *A graph reconstructor's manual* remains the standard reference.
- **1997.** McKay verifies the conjecture computationally for all $n \le 11$.
- **2001–present.** Focus shifts to the **$k$-deck** problem (multiset of induced $k$-vertex subgraphs) and to quantitative "how many cards" questions.

## 4. Partial Results / Verified Cases

**Computational.** All graphs on $n \le 11$ vertices are reconstructible (McKay 1997, exhaustive over the $1{,}018{,}997{,}864$ graphs on 11 vertices). No counterexample is known for any $n$.

**Reconstructible classes** (all proved unconditionally):

| Class | Attribution |
|---|---|
| Trees, forests | Kelly 1957 |
| Disconnected graphs | Kelly 1957 |
| Regular graphs | folklore via Kelly's lemma |
| Separable graphs without end-vertices | Bondy 1969 |
| Unicyclic graphs, cacti | Manvel |
| Maximal planar graphs; outerplanar graphs | Fiorini, Lauri; Giles 1974 |
| Graphs with $\le 2$ vertices of degree $\ge 3$; max degree $\le 2$ | Manvel; Spinoza–West 2019 |
| Critical blocks, squares of paths, bidegreed graphs | various, see Bondy 1991 |
| Graphs $G$ with $\mathrm{diam}(G)=2$ or $\mathrm{diam}(\overline G)=2$ ... partial | Bondy–Hemminger 1977 |

**Reduction.** It suffices to prove the conjecture for 2-connected graphs (Yang 1988).

**Edge reconstruction.** True whenever $m > \tfrac12\binom{n}{2}$ (Lovász 1972); whenever $2^{m-1} > n!$ (Müller 1977), so all graphs with $m \ge \tfrac12 n\log_2 n$ are edge-reconstructible; also for all planar graphs with $\delta \ge 3$, all graphs with $\delta \ge 3$ and $m \ge 3n-5$ hold via degree-based arguments; and for all graphs on $n \le 11$ vertices.

**Reconstructible parameters.** Edge count, degree sequence, connectivity, number of components, Tutte polynomial, chromatic and characteristic polynomials, planarity, and the number of spanning trees.

**$k$-decks.** Nýdl (2001) showed that for every $\varepsilon>0$ there are infinitely many $n$ and non-isomorphic $n$-vertex graphs with the same $k$-deck for $k < \varepsilon n$ — so the deck of *small* cards is genuinely weaker. Trees on $n$ vertices are determined by their $k$-deck for $k \ge (8/9 + o(1))n$ (Groenland–Johnston–Scott–Tan) *(frontier — verify)*.

## 5. Principal Obstacles

1. **Counting saturates one degree short.** Kelly's lemma reconstructs every count $s(F,G)$ for $|V(F)| < n$; Nash-Williams' framework reduces everything to a single unknown, $s^*(G,G)$ versus $s^*(G,H)$. Every additional identity derived from the deck is a linear consequence of those already known, so pure counting provably cannot close the last step.
2. **No canonical vertex.** A proof would want to identify a distinguished vertex or edge whose deletion is recognizable. Automorphism-rich graphs (vertex-transitive, strongly regular) admit no canonical choice, and the deck gives no labelling.
3. **Stockmeyer's barrier.** Tournaments are non-reconstructible, yet all counting lemmas above hold verbatim for digraphs. Hence any successful proof must use a property of *undirected* graphs that the counting machinery does not see — no current technique isolates such a property.
4. **Density gap in the edge version.** Lovász–Müller arguments need $m = \Omega(n\log n)$; sparse graphs have too little entropy for the inclusion–exclusion sign argument to survive, and the sparse regime (where trees live) needs entirely different, ad hoc structural methods.
5. **Algebraic methods do not converge.** Spectral data (characteristic polynomial) is reconstructible but far from complete — cospectral non-isomorphic graphs are abundant, so eigenvalue methods cannot separate $G$ from $H$.
6. **Computational verification is exponential.** The number of graphs on $n$ vertices grows as $2^{\binom{n}{2}}/n!$; extending McKay's $n\le 11$ check to $n = 13$ is already out of reach by brute force.

## 6. The Gap

The precise boundary: everything expressible as a count of *proper* induced subgraphs is known (Section 2); the conjecture asks for the isomorphism class of $G$ itself, an $n$-vertex datum. Formally, given $\mathcal{D}(G)=\mathcal{D}(H)$, all the constraints derivable are
$$s^*(F,G) = s^*(F,H) \quad \text{for all } F \not\cong G,\ |V(F)| = n,$$
and the missing step is to force $s^*(G,G) = s^*(G,H)$, i.e. to show $H$ contains a spanning copy of $G$. Equivalently: **prove that no non-isomorphic pair can agree on all spanning-subgraph counts except their own.** The linear algebra of the Kelly–Nash-Williams system is rank-deficient by exactly one dimension, and no known argument supplies the missing equation without extra structural input (2-connectivity, degree bounds, density).

## 7. Current Research (as of June 2026)

- **Quantitative reconstruction ($k$-decks).** Kostochka and West (Illinois) and collaborators study the least $k$ for which the $k$-deck determines $G$ in given classes; e.g. graphs with maximum degree 2, caterpillars, and graphs of bounded treewidth. Kostochka–West (IEEE Trans. Inform. Theory, 2021) connect this to reconstruction of sequences from subsequences, tying the problem to coding theory and DNA-storage trace reconstruction.
- **Oxford/Birmingham school.** Groenland, Guggiari, Johnston, Scott and Tan have produced probabilistic and entropy-based bounds: *size reconstructibility* (the number of edges is determined by the $k$-deck for $k \ge$ roughly $\tfrac{1}{2}n$ ranges), and trees from $\Theta(n)$-sized cards.
- **Trace reconstruction crossover.** Techniques from string trace reconstruction (complex-analytic moment methods) are being imported to graph decks *(frontier — verify)*.
- **Formalization.** Partial formal verification of Kelly's lemma and the tree case in Lean/mathlib is under way *(frontier — verify)*.
- **Computation.** No published extension of McKay's $n\le 11$ verification; the bottleneck is canonical-form enumeration at $n=12$.

## 8. Future Work

- Prove the conjecture for **3-connected planar graphs** or for **vertex-transitive graphs**, the two classes where automorphism structure is strongest and counting is weakest.
- Sharpen Müller's edge-reconstruction bound from $\tfrac12 n\log_2 n$ toward the conjectured constant-density or even $m \ge 4$ threshold; Bondy explicitly proposes attacking $m = \Omega(n)$.
- Identify a property distinguishing graphs from digraphs that is visible in the deck — the only route past Stockmeyer's barrier.
- Determine the minimum $k = k(n)$ such that the $k$-deck reconstructs all $n$-vertex graphs; current knowledge places it between $\Omega(n)$ (Nýdl) and $n-1$.
- Develop an entropy/information-theoretic lower bound showing the deck carries $\ge \binom{n}{2}$ bits about $G$ in the worst case.

## 9. Key References

- **[Foundational]** P. J. Kelly. *A congruence theorem for trees.* Pacific Journal of Mathematics 7 (1957), 961–968.
- **[Foundational]** S. M. Ulam. *A Collection of Mathematical Problems.* Interscience Publishers, New York, 1960.
- **[Foundational]** F. Harary. *On the reconstruction of a graph from a collection of subgraphs.* In: Theory of Graphs and its Applications (Prague, 1964), 47–52.
- **[Foundational]** L. Lovász. *A note on the line reconstruction problem.* Journal of Combinatorial Theory, Series B 13 (1972), 309–310.
- **[Foundational]** V. Müller. *The edge reconstruction hypothesis is true for graphs with more than $n\log_2 n$ edges.* Journal of Combinatorial Theory, Series B 22 (1977), 281–283.
- **[Foundational]** P. K. Stockmeyer. *The falsity of the reconstruction conjecture for tournaments.* Journal of Graph Theory 1 (1977), 19–25.
- **[Foundational]** W. T. Tutte. *All the king's horses. A guide to reconstruction.* In: Graph Theory and Related Topics, Academic Press, 1979, 15–33.
- **[Foundational]** Yang Yongzhi. *The reconstruction conjecture is true if all 2-connected graphs are reconstructible.* Journal of Graph Theory 12 (1988), 237–243.
- **[SOTA / Recent]** B. Bollobás. *Almost every graph has reconstruction number three.* Journal of Graph Theory 14 (1990), 1–4.
- **[SOTA / Recent]** B. D. McKay. *Small graphs are reconstructible.* Australasian Journal of Combinatorics 15 (1997), 123–126.
- **[SOTA / Recent]** V. Nýdl. *Graph reconstruction from subgraphs.* Discrete Mathematics 235 (2001), 335–341.
- **[SOTA / Recent]** H. Spinoza and D. B. West. *Reconstruction from the deck of $k$-vertex induced subgraphs.* Journal of Graph Theory 90 (2019), 497–522.
- **[SOTA / Recent]** A. V. Kostochka and D. B. West. *On reconstruction of graphs from the multiset of subgraphs obtained by deleting $\ell$ vertices.* IEEE Transactions on Information Theory 67 (2021), 3278–3286.
- **[SOTA / Recent]** C. Groenland, H. Guggiari and A. Scott. *Size reconstructibility of graphs.* Journal of Graph Theory 96 (2021), 326–337.
- **[Survey]** J. A. Bondy and R. L. Hemminger. *Graph reconstruction — a survey.* Journal of Graph Theory 1 (1977), 227–268.
- **[Survey]** J. A. Bondy. *A graph reconstructor's manual.* In: Surveys in Combinatorics 1991, LMS Lecture Note Series 166, Cambridge University Press, 221–252.
- **[Survey]** C. St. J. A. Nash-Williams. *The reconstruction problem.* In: Selected Topics in Graph Theory (L. W. Beineke, R. J. Wilson, eds.), Academic Press, 1978, 205–236.

## 10. Worked Example / Concrete Special Case

**Task.** Reconstruct $G$ on $n=4$ vertices from the deck
$$\mathcal{D} = \{\!\{\, P_3,\ P_3,\ K_2 \cup K_1,\ K_2 \cup K_1 \,\}\!\},$$
where $P_3$ is the 3-vertex path (2 edges) and $K_2 \cup K_1$ is an edge plus an isolated vertex (1 edge).

**Step 1 — edge count.** By Kelly's lemma with $F = K_2$:
$$m(G) = \frac{1}{n-2}\sum_{v} m(G-v) = \frac{2+2+1+1}{4-2} = \frac{6}{2} = 3.$$

**Step 2 — degrees.** $\deg(v) = m(G) - m(G-v)$, so the two $P_3$ cards come from vertices of degree $3-2=1$ and the two $K_2\cup K_1$ cards from vertices of degree $3-1=2$. Degree sequence: $(1,1,2,2)$, consistent with $\sum \deg = 6 = 2m$.

**Step 3 — candidates.** The 4-vertex graphs with 3 edges are $P_4$ (degrees $1,2,2,1$), $K_3 \cup K_1$ (degrees $2,2,2,0$), and the star $K_{1,3}$ (degrees $3,1,1,1$). Only $P_4$ has degree sequence $(1,1,2,2)$.

**Step 4 — verify.** Label $P_4 = v_1v_2v_3v_4$. Deleting $v_1$ or $v_4$ leaves $P_3$; deleting $v_2$ or $v_3$ leaves an edge plus an isolated vertex. So $\mathcal{D}(P_4) = \mathcal{D}$. Hence $G \cong P_4$, uniquely.

**Why this is not a proof strategy in general.** Steps 1–2 used only reconstructible counts, and Step 3 succeeded because at $n=4$ the degree sequence happened to pin down the isomorphism class. For $n=6$ already there are non-isomorphic graphs with identical degree sequences and identical counts of all $5$-vertex induced subgraphs *up to the single spanning count* — the deck resolves these only through the finer multiset structure, and no general argument is known that this always suffices. Contrast the 3-vertex tournaments: the cyclic triangle $C_3^{\to}$ and the transitive triangle both yield decks of two-vertex arcs, and at larger sizes Stockmeyer's families genuinely collide — the same Steps 1–2 go through unchanged there, which is exactly why counting alone cannot finish the undirected case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*