---
id: 07-combinatorics/meyniels-cops-and-robbers-conjecture
title: "Meyniel's Cops and Robbers Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Meyniel's Cops and Robbers Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/meyniels-cops-and-robbers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Meyniel, 1985).** There is an absolute constant $C$ such that every connected graph $G$ on $n$ vertices satisfies
$$c(G) \le C\sqrt{n},$$
where $c(G)$ is the *cop number*: the least number of cops needed to catch a robber in the Nowakowski–Winkler–Quilliot pursuit game.

A complete proof must exhibit, for every connected $n$-vertex graph, a winning strategy for $C\sqrt n$ cops (existence suffices; no algorithmic efficiency is required). A disproof must exhibit an infinite family $\{G_n\}$ with $c(G_n)/\sqrt{n} \to \infty$.

The bound is asymptotically best possible: incidence graphs of finite projective planes have $n = 2(q^2+q+1)$ vertices and cop number $q+1 = \Theta(\sqrt n)$. So the conjecture asserts that these extremal examples are the worst case up to a constant.

Two weaker statements are also open and are standard intermediate targets:

- **Soft Meyniel.** $c(G) = O(n^{1-\varepsilon})$ for some fixed $\varepsilon > 0$.
- **Meyniel for a class $\mathcal{C}$.** $c(G) = O(\sqrt n)$ for all $G \in \mathcal{C}$.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, simple, connected, with $|V| = n$. Fix $k \ge 1$ cops.

**The game.** Cops choose positions $c_1,\dots,c_k \in V$; then the robber chooses $r \in V$. Players alternate, cops first. In a cop move each cop either stays or moves along an edge; likewise the robber. Both sides see all positions (perfect information). The cops win if some cop occupies the robber's vertex after finitely many rounds. Define
$$c(G) = \min\{k : k \text{ cops have a winning strategy on } G\}.$$
The game is a finite-state reachability game on $V^k \times V \times \{\text{cop},\text{rob}\}$, hence determined, and $c(G) \le n$ trivially.

**Closed neighbourhood and domination.** $N[v] = \{v\} \cup \{u : uv \in E\}$. A vertex $u$ is a *corner* (or is dominated) if $N[u] \subseteq N[v]$ for some $v \ne u$. $G$ is *dismantlable* (cop-win ordering) if repeatedly deleting corners reduces $G$ to a single vertex.

**Theorem (Quilliot 1978; Nowakowski–Winkler 1983).** $c(G) = 1$ iff $G$ is dismantlable.

**Retract theorem (Berarducci–Intrigila 1993).** If $H$ is a retract of $G$ then $c(H) \le c(G)$, and $c(G) \le \max\{c(H),\, c_{G}(G \setminus H)\}$-type decompositions hold; in particular the cop number is monotone under retracts, but *not* under subgraphs or minors.

**Isometric path lemma (Aigner–Fromme 1984).** If $P$ is a shortest $u$–$v$ path in $G$, one cop can, after finitely many moves, guard $P$: from then on the robber entering $V(P)$ is caught immediately. This is the workhorse of every upper-bound proof.

**Girth lower bound.** Write $\delta(G)$ for minimum degree and $g(G)$ for girth. If $g(G) \ge 5$ then
$$c(G) \ge \delta(G).$$
More generally (Frankl 1987), if $g(G) \ge 8t-3$ and $\delta(G) \ge d$ then $c(G) > d^{\,t}$. Bradshaw, Hosseini, Mohar and Stacho (2023) sharpened this to
$$c(G) \ \ge\ \tfrac{1}{e}\,(\delta-1)^{\lfloor (g-1)/4 \rfloor}.$$
Since a graph with $\delta \ge d$ and girth $\ge 5$ has $n \ge d^2+1$ (Moore bound), $\delta \le \sqrt{n-1}$, so the girth-5 lower bound alone can never exceed $\sqrt n$ — consistent with Meyniel.

**Extremal family.** For a prime power $q$, the incidence graph $I_q$ of $PG(2,q)$ is $(q+1)$-regular, bipartite, of girth $6$, with $n = 2(q^2+q+1)$ and $c(I_q) = q+1 \approx \sqrt{n/2}$.

## 3. History & State of the Art (SOTA)

The game was introduced independently by Quilliot (1978 thesis) and Nowakowski–Winkler (1983), both characterising $c(G)=1$. Aigner and Fromme (1984) introduced the multi-cop version, proved the isometric-path lemma, and showed $c(G)\le 3$ for planar $G$.

Henri Meyniel stated the $O(\sqrt n)$ conjecture in a 1985 private communication to Péter Frankl; it first appears in print in Frankl's 1987 paper, which proved
$$c(G) = O\!\left(\frac{n \log\log n}{\log n}\right).$$
Chiniforooshan (2008) improved this to $O(n/\log n)$. In 2011–2012 three groups independently obtained the current record, all by variants of the same expansion/counting argument:

$$c(G) \;\le\; \frac{n}{2^{(1-o(1))\sqrt{\log_2 n}}}\, .$$

— Lu and Peng (*J. Graph Theory*, 2012), Scott and Sudakov (*SIAM J. Discrete Math.*, 2011), and Frieze, Krivelevich and Loh (*J. Graph Theory*, 2012). This is $n^{1-o(1)}$: it does not even establish soft Meyniel. No asymptotic improvement to the general bound has been published since.

Complementary hardness: deciding $c(G)\le k$ is EXPTIME-complete for $k$ part of the input (Kinnersley, 2015), and computing $c(G)$ is NP-hard, ruling out brute-force resolution.

## 4. Partial Results / Verified Cases

Meyniel's bound is known — usually with a much stronger constant-or-parameter bound — in these classes.

| Class | Bound | Source |
|---|---|---|
| Dismantlable (chordal, trees, interval) | $c=1$ | Quilliot 1978; Nowakowski–Winkler 1983 |
| Planar | $c \le 3$ | Aigner–Fromme 1984 |
| Genus $g$ surfaces | $c \le \tfrac{4g}{3}+3$ | Bowler, Erde, Lehner, Pitz 2021 (earlier $\lfloor 3g/2\rfloor+3$, Schröder 2001) |
| $H$-minor-free | $c \le$ const$(H)$ | Andreae 1986 |
| Treewidth $\mathrm{tw}$ | $c \le \tfrac{1}{2}\mathrm{tw}+1$ | Joret, Kamiński, Theis 2010 |
| Diameter 2 | $c \le 2\sqrt n - 1$ | Lu–Peng 2012 |
| Bipartite, diameter 3 | $c \le 2\sqrt n - 1$ | Lu–Peng 2012 |
| Cayley graphs of abelian groups | $c \le 0.95\sqrt n$ (asymptotically) | Frankl 1987; Bradshaw 2019 |
| Binomial random graphs $G(n,p)$, all $p=p(n)$ | $c = O(\sqrt n)$ whp | Prałat–Wormald 2015 |
| Random $d$-regular graphs, $3\le d$ | $c = O(\sqrt n)$ whp | Prałat–Wormald 2017 |
| Dense $G(n,p)$, $p \ge 2.1\log n/n$ | $c \le 160000\sqrt{n}\log n$ | Bollobás–Kun–Leader 2013 |
| Graphs with no induced long cycles / bounded genus quotients | Meyniel holds | Turcotte 2022 *(class-specific)* |

Small-order data: the minimum order of a 3-cop-win graph is $10$ (the Petersen graph); the minimum order of a 4-cop-win graph is $19$ (Turcotte–Yvon, 2021), confirmed by exhaustive computation. All graphs on $n \le 18$ vertices satisfy $c(G) \le 3 < \sqrt{18}\cdot C$ for $C=1$, so no small counterexample exists.

Random graphs also show the bound is *attained*: Łuczak–Prałat's "zigzag theorem" (2010) gives densities where $c(G(n,p)) = n^{1/2 + o(1)}$, so any proof must be tight at $\sqrt n$ for those densities.

## 5. Principal Obstacles

- **No useful monotonicity.** $c(\cdot)$ is not monotone under subgraphs, minors, or vertex deletion — deleting a vertex can raise or lower the cop number. Induction on graph structure, the standard combinatorial engine, has no safe base operation. Only retracts behave well, and general graphs have no rich supply of retracts.
- **The counting barrier at $n^{1-o(1)}$.** All record proofs are the same: place cops randomly / greedily so that each cop guards an isometric path or dominates a set, then argue the robber's free territory shrinks by a factor per round. The shrinkage per cop is only $2^{-\Theta(\sqrt{\log n})}$, because guarding a shortest path costs one cop yet removes only a $1/\mathrm{polylog}$-ish fraction of a set that can be expander-like. Pushing this to $n^{1-\varepsilon}$ needs a cop that removes a *constant power* of the vertex set — no known mechanism does this.
- **Expanders defeat local strategies.** In a graph of girth $\ge 5$ and degree $d$, a cop at distance $\ge 2$ from the robber controls at most one of the robber's $d$ neighbours. Locality gives no leverage; catching requires globally coordinated encirclement, which has no known potential-function certificate.
- **Two-sided extremality.** Projective-plane incidence graphs sit exactly at $\Theta(\sqrt n)$, so any argument must be essentially tight on them. Slack-tolerant techniques (probabilistic deletion, entropy compression) lose more than the target margin.
- **Complexity obstruction.** EXPTIME-completeness of the game means no polynomial-size "witness" of a cop strategy is expected, so proofs cannot be reduced to verifying short certificates.

## 6. The Gap

Proven: $c(G) \le n\,2^{-(1-o(1))\sqrt{\log_2 n}}$ for all $G$. Conjectured: $c(G) = O(n^{1/2})$.

The multiplicative gap is $2^{(1-o(1))\sqrt{\log_2 n}}$ versus $\sqrt n = 2^{\frac12\log_2 n}$ — a gap of $n^{1/2 - o(1)}$. Concretely, even the *qualitative* statement "$c(G) \le n^{0.999}$" is unproved.

The exact missing step: an argument showing that in a graph where the robber's escape territory is a set $S$ with $|S| = n^{\alpha}$, $\alpha > 1/2$, one additional cop can shrink $|S|$ by a factor $n^{-\Omega(1)}$ rather than $2^{-O(\sqrt{\log n})}$. Equivalently, a structural dichotomy is needed: either $G$ has a small isometric-path decomposition (few cops suffice by Aigner–Fromme), or $G$ has girth-and-degree structure forcing $\delta = O(\sqrt n)$ by the Moore bound. Nobody knows how to make this dichotomy exhaustive for graphs with many short cycles but expander-like global structure.

## 7. Current Research (as of June 2026)

- **Group-theoretic Cayley graphs.** Bradshaw, Hosseini and collaborators continue extending Meyniel to Cayley graphs of nilpotent and small-doubling groups; abelian and directed abelian cases are settled with constant $< 1$. *(frontier — verify)* Extensions to Cayley graphs of arbitrary groups with bounded generator-set size are actively circulating.
- **High-girth lower bounds.** The Bradshaw–Hosseini–Mohar–Stacho bound $c \ge \frac1e(\delta-1)^{\lfloor (g-1)/4\rfloor}$ (*J. Graph Theory*, 2023) is being pushed toward the conjectured $\delta^{\lfloor (g-1)/4 \rfloor}$ threshold, which would tie Meyniel to the Moore-bound extremal problem.
- **Random and geometric models.** Prałat's group (Toronto Metropolitan) works on random geometric graphs, random intersection graphs, and preferential-attachment models — all supporting Meyniel in-model.
- **Variants as proxies.** Zero-visibility, lazy-cop, and Cops-and-Attacking-Robbers variants are studied to isolate which game feature blocks the $\sqrt n$ bound; the lazy cop number of $G(n,1/2)$ is known to exceed $\sqrt n$, showing the "all cops move" rule is essential.
- **Computer search.** SAT/ILP-based determination of minimum-order $k$-cop-win graphs (Turcotte, Yvon) has settled $k=4$ at $n=19$; $k=5$ is open, conjectured to be $n=34$. *(frontier — verify)*

## 8. Future Work

Directions endorsed in the literature (Baird–Bonato survey; Bonato–Nowakowski book):

1. **Prove soft Meyniel first.** Any $c(G) = O(n^{1-\varepsilon})$ result would be the first genuinely new mechanism since 1987.
2. **Expander case.** Settle Meyniel for graphs with spectral gap bounded below; expanders are the presumed hard core, and Bollobás–Kun–Leader-style guarding may generalise from $G(n,p)$ to pseudo-random graphs.
3. **Girth-degree dichotomy.** Prove $c(G) = O(\sqrt n)$ for all graphs of girth $\ge 5$ using the Moore bound, then handle short cycles by contraction/retract arguments.
4. **Bounded-degree graphs.** No $o(n/\log n)$-type improvement is known even for 3-regular graphs; a clean $O(\sqrt n)$ theorem there would be a major step.
5. **Search for a counterexample.** Frankl's high-girth lower bound suggests probing generalised polygons and Ramanujan graphs for families with $c \gg \sqrt n$.

## 9. Key References

- **[Foundational]** R. Nowakowski, P. Winkler. *Vertex-to-vertex pursuit in a graph.* Discrete Mathematics 43 (1983), 235–239.
- **[Foundational]** A. Quilliot. *Jeux et points fixes sur les graphes.* Thèse de 3ème cycle, Université de Paris VI, 1978.
- **[Foundational]** M. Aigner, M. Fromme. *A game of cops and robbers.* Discrete Applied Mathematics 8 (1984), 1–12.
- **[Foundational]** P. Frankl. *Cops and robbers in graphs with large girth and Cayley graphs.* Discrete Applied Mathematics 17 (1987), 301–305.
- **[SOTA]** A. Scott, B. Sudakov. *A bound for the cops and robbers problem.* SIAM Journal on Discrete Mathematics 25 (2011), 1438–1442.
- **[SOTA]** L. Lu, X. Peng. *On Meyniel's conjecture of the cop number.* Journal of Graph Theory 71 (2012), 192–205.
- **[SOTA]** A. Frieze, M. Krivelevich, P. Loh. *Variations on cops and robbers.* Journal of Graph Theory 69 (2012), 383–402.
- **[SOTA]** E. Chiniforooshan. *A better bound for the cop number of general graphs.* Journal of Graph Theory 58 (2008), 45–48.
- **[Recent]** P. Prałat, N. Wormald. *Meyniel's conjecture holds for random graphs.* Random Structures & Algorithms 48 (2016), 396–421.
- **[Recent]** B. Bollobás, G. Kun, I. Leader. *Cops and robbers in a random graph.* Journal of Combinatorial Theory Series B 103 (2013), 226–236.
- **[Recent]** P. Bradshaw, S. A. Hosseini, B. Mohar, L. Stacho. *On the cop number of graphs of high girth.* Journal of Graph Theory 102 (2023), 15–34.
- **[Recent]** N. Bowler, J. Erde, F. Lehner, M. Pitz. *Bounding the cop number of a graph by its genus.* SIAM Journal on Discrete Mathematics 35 (2021), 2459–2489.
- **[Recent]** W. B. Kinnersley. *Cops and Robbers is EXPTIME-complete.* Journal of Combinatorial Theory Series B 111 (2015), 201–220.
- **[Survey]** W. Baird, A. Bonato. *Meyniel's conjecture on the cop number: a survey.* Journal of Combinatorics 3 (2012), 225–238.
- **[Book]** A. Bonato, R. Nowakowski. *The Game of Cops and Robbers on Graphs.* Student Mathematical Library 61, American Mathematical Society, 2011.

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$: $c(P) = 3$, and $\sqrt{10} \approx 3.16$.**

$P$ is $3$-regular, $n=10$, girth $5$, diameter $2$.

*Lower bound $c(P) \ge 3$ (Aigner–Fromme girth argument).* Suppose two cops play. Claim: the robber can always move to a vertex not adjacent to any cop, or stay safe. Let the robber sit at $v$ with $N(v) = \{x_1,x_2,x_3\}$. Consider a cop at vertex $u$ with $d(u,v) = 2$. If $u$ were adjacent to two distinct $x_i, x_j$, then $v x_i u x_j v$ is a $4$-cycle, contradicting girth $5$. So each cop at distance $2$ threatens at most one neighbour of $v$. A cop at distance $1$, say at $x_1$, threatens $v$ and at most one further $x_j$ — again girth $5$ forbids adjacency of $x_1$ to two of $\{x_2,x_3\}$ plus $v$ without creating a triangle or $4$-cycle; in $P$, $N(v)$ is independent, so $x_1$ threatens only $v$ among $\{v,x_1,x_2,x_3\}$ (and itself).

Count the safe set $\{v,x_1,x_2,x_3\}$, of size $4$. Two cops threaten at most $2$ of these $4$ vertices before the robber's move (each cop kills at most one element by the above, plus the vertex it occupies if it lies in the set). Hence at least one vertex of $N[v]$ is unthreatened, and the robber moves there. This is a perpetual escape, so $c(P) \ge 3$. Equivalently $c(P) \ge \delta(P) = 3$.

*Upper bound $c(P) \le 3$.* $P$ has diameter $2$. Place the three cops on a maximal independent-ish set: take $v$ and note $N[v]$ has $4$ vertices, leaving $6$. Concretely, place cops on the three vertices of an outer path $u_1u_2u_3$ of the 5-cycle rim. Because $\mathrm{diam}(P)=2$, after one cop move the cops can be positioned so that $N[c_1]\cup N[c_2]\cup N[c_3]$ covers $3\cdot4 = 12 \ge 10$ vertices; a direct check of the 10 vertices shows a covering triple exists (e.g. cops on $\{1,2,3\}$ of the outer 5-cycle dominate all of $P$ minus one vertex, and one further move closes it). Hence $c(P)=3$.

*What this instance shows.* At $n=10$ we have $c = 3 \approx \sqrt{10}$, matching Meyniel with $C=1$. But the Petersen graph is the *Moore graph* of degree $3$ and girth $5$: it is exactly the extremal object for the bound $\delta \le \sqrt{n-1}$. The conjecture asserts that no graph beats this ratio by more than a constant — and the whole difficulty is that current proofs give only $10 \cdot 2^{-(1-o(1))\sqrt{\log_2 10}}$-type bounds, which are vacuous at this scale and still $n^{1-o(1)}$ asymptotically.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*