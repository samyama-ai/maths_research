---
id: 10-theoretical-cs/chvatal-toughness-conjecture
title: "Chvatal Toughness Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chvátal's Toughness Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/chvatal-toughness-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Chvátal (1973) introduced toughness as a quantitative measure of how hard a graph is to break apart, and asked whether enough toughness forces a Hamiltonian cycle.

**Conjecture (Chvátal, 1973).** There exists a finite constant $t_0$ such that every $t_0$-tough graph on at least three vertices is Hamiltonian.

Here a graph $G$ is *$t$-tough* if removing any vertex set $S$ that disconnects $G$ leaves at most $|S|/t$ components. Chvátal's own guess was $t_0 = 2$ (the "2-tough conjecture"); that specific value was disproved in 2000. The existential form is open.

A complete resolution requires either:
- a proof that some explicit finite $t_0$ suffices, with a Hamiltonicity certificate for all $t_0$-tough graphs; or
- a construction of non-Hamiltonian graphs of arbitrarily large toughness, i.e. an infinite family $G_1, G_2, \dots$ with $t(G_i) \to \infty$ and no Hamiltonian cycle.

The conjecture is a *sufficient-condition* statement: toughness $\ge 1$ is necessary for Hamiltonicity (Section 2), and the question is how far this necessary condition is from being sufficient.

## 2. Mathematical Foundations

Let $G = (V,E)$ be a finite simple graph, $c(H)$ the number of connected components of $H$, $\kappa(G)$ its vertex connectivity, $\alpha(G)$ its independence number.

**Definition (toughness).** For non-complete $G$,
$$t(G) \;=\; \min_{\substack{S \subseteq V \\ c(G-S) \ge 2}} \frac{|S|}{c(G-S)},$$
and $t(K_n) = \infty$ by convention. $G$ is *$t$-tough* if $t(G) \ge t$. A set $S$ attaining the minimum is a *tough set*.

**Basic inequalities.**
$$t(G) \le \frac{\kappa(G)}{2} \quad \text{for non-complete } G, \qquad t(G) \le \frac{n - \alpha(G)}{\alpha(G)} \ \text{ when } \alpha(G)\ge 2 .$$
The first follows by taking $S$ a minimum cut (which leaves $\ge 2$ components); the second by taking $S = V \setminus I$ for a maximum independent set $I$. Consequently $t(G) \ge 2 \Rightarrow \kappa(G) \ge 4$.

**Necessity.** If $G$ has a Hamiltonian cycle $C$ then for every $S \subseteq V$, $c(G-S) \le c(C-S) \le |S|$, so $t(G) \ge 1$. Every Hamiltonian graph is $1$-tough. The converse fails badly: infinitely many $1$-tough graphs are non-Hamiltonian, which is what motivates raising the threshold.

**Related spanning structures.** Toughness controls weaker spanning objects with sharp thresholds:
- *$k$-factors* (Enomoto–Jackson–Katerinis–Saito, 1985): if $t(G) \ge k$, $k|V|$ even and $|V| \ge k+1$, then $G$ has a $k$-factor; and for every $\varepsilon>0$ there are $(k-\varepsilon)$-tough graphs with no $k$-factor. So $2$-tough $\Rightarrow$ a $2$-factor (a spanning union of cycles) — the natural relaxation of a Hamiltonian cycle.
- *Bounded-degree spanning trees* (Win, 1989): $t(G) \ge \frac{1}{k-2}$ implies a spanning tree of maximum degree $\le k$.
- *$k$-walks* (Jackson–Wormald conjecture): every $\frac{1}{k-1}$-tough graph should have a closed spanning walk visiting each vertex at most $k$ times; a Hamiltonian cycle is a $1$-walk. Ellingham–Zha (2000) proved every $4$-tough graph has a $2$-walk.

**Computational status.** Deciding whether $t(G) \ge 1$ is NP-hard (Bauer–Hakimi–Schmeichel, 1990), so toughness is not a certificate one can verify efficiently in general — an obstacle to computer-assisted search for counterexamples.

## 3. History & State of the Art (SOTA)

- **1973.** Václav Chvátal, *Tough graphs and hamiltonian circuits* (Discrete Mathematics 5, 215–228), defines $t(G)$, proves $1$-toughness is necessary, exhibits $\tfrac{3}{2}$-tough non-Hamiltonian graphs, and conjectures a finite sufficient threshold, suggesting $t_0=2$.
- **1978–1979.** Bigalke and Jung: every $1$-tough graph with $\delta(G) \ge n/3$ is Hamiltonian — toughness combines with degree conditions.
- **1985.** Enomoto–Jackson–Katerinis–Saito settle the $k$-factor analogue exactly, showing the "toughness $\ge k$" threshold is sharp there. This made $t_0 = 2$ look plausible for $2$-factors but gave no cycle.
- **2000.** Bauer, Broersma and Veldman, *Not every 2-tough graph is Hamiltonian* (Discrete Applied Mathematics 99, 317–321): for every $\varepsilon > 0$ they construct non-Hamiltonian graphs with $t > \tfrac{9}{4} - \varepsilon$ (and non-traceable ones with $t > \tfrac{7}{4}-\varepsilon$; chordal non-Hamiltonian examples with $t > \tfrac{7}{4}-\varepsilon$). This kills $t_0 = 2$ and gives the current lower bound $t_0 \ge \tfrac{9}{4}$ if $t_0$ exists.
- **2006.** Bauer–Broersma–Schmeichel survey, *Toughness in graphs — a survey* (Graphs and Combinatorics 22, 1–35), the standard reference.
- **2014–2021.** Sharp thresholds for hereditary classes: $2K_2$-free graphs (Broersma–Patel–Pyatkin 2014: $25$-tough; Shan 2020: $3$-tough), chordal graphs (Kabela–Kaiser 2017: $10$-tough).

**SOTA summary.** No finite $t_0$ is known for general graphs. The proven interval is $\tfrac{9}{4} \le t_0 \le \infty$; nothing rules out the conjecture being false.

## 4. Partial Results / Verified Cases

The conjecture is *true with an explicit constant* on several classes:

| Class | Sufficient toughness | Best lower bound (non-Hamiltonian examples) | Source |
|---|---|---|---|
| Planar | $t > 3/2$ (then $\kappa \ge 4$, Tutte) | $3/2$ — sharp | Tutte 1956; survey 2006 |
| Split graphs | $t \ge 3/2$ | $3/2 - 1/n$ — sharp | Kratsch–Lehel–Müller 1996 |
| Chordal | $t \ge 10$ | $7/4 - \varepsilon$ | Kabela–Kaiser 2017; BBV 2000 |
| $2K_2$-free | $t \ge 3$ | $7/4$-ish | Shan 2020 |
| Claw-free | $t \ge 2$ conditional on Matthews–Sumner | — | via $t\ge 2 \Rightarrow \kappa \ge 4$ |
| $k$-factor analogue | $t \ge k$ | $k - \varepsilon$ — sharp | EJKS 1985 |
| $2$-walks | $t \ge 4$ | — | Ellingham–Zha 2000 |

Other verified regimes: graphs with $t \ge 1$ and $\delta \ge n/3$; graphs of bounded independence number ($\alpha \le 3$ classes are largely settled by the $2K_2$-free and $P_3$-family results); and all graphs on $n \le 12$ vertices, where exhaustive search finds no $2$-tough non-Hamiltonian example — the Bauer–Broersma–Veldman graphs are large.

## 5. Principal Obstacles

- **Toughness is a min over exponentially many cuts.** It is a global, NP-hard-to-verify parameter with no local structure. Standard Hamiltonicity machinery — Ore/Chvátal–Erdős degree and independence conditions, closure operations, rotation-extension arguments — all consume *local* information (degrees, neighbourhoods). A tough graph can have vertices of degree $\Theta(t)$ only, so degree-based tools give nothing.
- **The counting is too weak by a constant factor.** The workhorse argument takes a longest cycle $C$, removes a set $S$ of "attachment" vertices, and counts components of $G - S$ against $|S|$. This yields spanning objects that are *almost* cycles — $2$-factors, $2$-walks, degree-$3$ spanning trees — but the last step, merging the components of a $2$-factor into one cycle, is exactly where the toughness budget runs out. Toughness bounds component *counts*, not the connection pattern between them.
- **Extremal constructions are ratio-tuned, not rigid.** The BBV examples show the obstruction is not a parity or topological invariant but a fine numerical balance; there is no evident invariant to induct on.
- **No good certificate for large toughness.** Building candidate counterexamples of toughness $> 9/4$ requires certifying a min over cuts on large graphs; NP-hardness (Bauer–Hakimi–Schmeichel 1990) blocks brute force, so the search space above $9/4$ is essentially unexplored computationally.
- **Class-specific proofs do not transfer.** The chordal and $2K_2$-free proofs use clique-tree decompositions or bounded independence to localise the argument. Both crutches vanish in general graphs, where $\alpha$ can be $\Theta(n/t)$.

## 6. The Gap

Proven: for every fixed $k$, $t \ge k$ forces a $k$-factor, and $t \ge 4$ forces a $2$-walk; for restricted classes, explicit constants force Hamiltonicity. Conjectured: one constant works for *all* graphs.

The precise missing step is a **connectivity-to-cyclicity upgrade**: given a $2$-factor $F$ of a $t$-tough graph with $r \ge 2$ cycles, produce a $2$-factor with fewer cycles. Every known merging argument needs either two cycles joined by two independent edges in a suitable configuration, or a degree condition, and toughness alone does not supply one. Equivalently: is there a function $f$ with $t(G) \ge f(r)$ forcing a $2$-factor with $< r$ components, and is $f$ bounded? A bounded $f$ proves the conjecture; an unbounded $f$ with matching constructions refutes it.

The complementary gap is quantitative: the interval $[9/4, \infty]$ for $t_0$ has not been narrowed from either end since 2000.

## 7. Current Research (as of June 2026)

- **Forbidden-subgraph thresholds.** The most active line: determine the exact toughness threshold for $H$-free graphs. Shan and collaborators have pushed $2K_2$-free to $t \ge 3$, and extended to $(P_2 \cup P_3)$-free and $P_4$-related families; work on $R$-free classes with $\alpha \le 4$ continues *(frontier — verify)*.
- **Chordal and clique-tree methods.** Whether $10$ can be reduced toward the $7/4$ lower bound for chordal graphs (Kabela, Kaiser, Prague/Pilsen school) remains the cleanest quantitative target.
- **Spectral and pseudorandom surrogates.** Toughness bounds from eigenvalue gaps (Alon-type $t \ge \Theta(d/\lambda)$ estimates; Gu, Brouwer–Haemers line) give large-toughness families that are provably Hamiltonian, supporting the conjecture on pseudorandom graphs *(frontier — verify)*.
- **Walks and factors.** Progress on the Jackson–Wormald $k$-walk conjecture is treated as a testbed: improving $t \ge 4$ for $2$-walks would sharpen the merging technology needed for cycles.
- **Counterexample search.** Attempts to beat $9/4$ by generalising the BBV gadget; no published improvement.

## 8. Future Work

- Decide the $2$-factor merging question of Section 6 for $r = 2$: does high toughness force a $2$-factor with a single cycle when only two cycles are present?
- Reduce the chordal constant from $10$ to $7/4$, or find chordal examples above $7/4$; the class is small enough to be decisive and large enough to be informative.
- Determine the exact threshold for split graphs' natural superclasses (interval, strongly chordal), where $3/2$ is already sharp below.
- Establish or refute a *fractional* version: is every $t$-tough graph's cycle space rich enough to admit a fractional Hamiltonian cycle for bounded $t$? A fractional counterexample would strongly suggest the conjecture is false.
- Push the BBV construction: replace its fixed gadget with a family whose ratio grows, which would refute the conjecture outright.

## 9. Key References

- **[Foundational]** V. Chvátal. *Tough graphs and hamiltonian circuits.* Discrete Mathematics 5(3), 215–228, 1973.
- **[Foundational]** W. T. Tutte. *A theorem on planar graphs.* Transactions of the American Mathematical Society 82, 99–116, 1956.
- **[Key]** H. Enomoto, B. Jackson, P. Katerinis, A. Saito. *Toughness and the existence of $k$-factors.* Journal of Graph Theory 9(1), 87–95, 1985.
- **[Key]** S. Win. *On a connection between the existence of $k$-trees and the toughness of a graph.* Graphs and Combinatorics 5, 201–205, 1989.
- **[Complexity]** D. Bauer, S. L. Hakimi, E. Schmeichel. *Recognizing tough graphs is NP-hard.* Discrete Applied Mathematics 28(3), 191–195, 1990.
- **[Key]** D. Kratsch, J. Lehel, H. Müller. *Toughness, hamiltonicity and split graphs.* Discrete Mathematics 150(1–3), 231–245, 1996.
- **[Key]** G. Chen, M. S. Jacobson, A. E. Kézdy, J. Lehel. *Tough enough chordal graphs are Hamiltonian.* Networks 31(1), 29–38, 1998.
- **[Counterexample]** D. Bauer, H. J. Broersma, H. J. Veldman. *Not every 2-tough graph is Hamiltonian.* Discrete Applied Mathematics 99(1–3), 317–321, 2000.
- **[Key]** M. N. Ellingham, X. Zha. *Toughness, trees, and walks.* Journal of Graph Theory 33(3), 125–137, 2000.
- **[Survey]** D. Bauer, H. J. Broersma, E. Schmeichel. *Toughness in graphs — a survey.* Graphs and Combinatorics 22(1), 1–35, 2006.
- **[SOTA]** H. Broersma, V. Patel, A. Pyatkin. *On toughness and hamiltonicity of $2K_2$-free graphs.* Journal of Graph Theory 75(3), 244–255, 2014.
- **[Survey]** H. Broersma. *How tough is toughness?* Bulletin of the EATCS 117, 2015.
- **[SOTA]** A. Kabela, T. Kaiser. *10-tough chordal graphs are Hamiltonian.* Journal of Combinatorial Theory, Series B 122, 417–427, 2017.
- **[SOTA]** S. Shan. *Hamiltonian cycles in 3-tough $2K_2$-free graphs.* Journal of Graph Theory 94(3), 349–363, 2020.

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$: toughness $4/3$, non-Hamiltonian.**

Label the outer $5$-cycle $v_1 \dots v_5$ ($v_i \sim v_{i+1}$ mod $5$), the inner pentagram $u_1 \dots u_5$ ($u_i \sim u_{i\pm 2}$ mod $5$), and spokes $v_i \sim u_i$.

*Upper bound $t(P) \le 4/3$.* Take
$$S = \{v_1,\, v_3,\, u_4,\, u_5\}.$$
Check $S$ is independent: $v_1 \not\sim v_3$; $v_1$'s neighbours are $v_2,v_5,u_1$; $v_3$'s are $v_2,v_4,u_3$; $u_4 \sim u_1,u_2,v_4$; $u_5 \sim u_2,u_3,v_5$; and $u_4 \not\sim u_5$ since $|4-5| = 1 \ne 2$.

Now delete $S$. The surviving vertices are $\{v_2,v_4,v_5,u_1,u_2,u_3\}$ with surviving edges:
- $v_2 \sim u_2$ (its outer neighbours $v_1,v_3$ are gone), and $u_2 \sim u_4,u_5$ are gone — component $\{v_2,u_2\}$;
- $v_4 \sim v_5$ ($v_4 \sim v_3, u_4$ gone; $v_5 \sim v_1, u_5$ gone) — component $\{v_4,v_5\}$;
- $u_1 \sim u_3$ ($u_1 \sim u_4, v_1$ gone; $u_3 \sim u_5, v_3$ gone) — component $\{u_1,u_3\}$.

So $c(P - S) = 3$ and $|S|/c = 4/3$. A case check over cut sizes ($P$ is $3$-connected and vertex-transitive, and no $3$-set leaves $3$ components) gives $t(P) = 4/3$ exactly.

*Interpretation.* $P$ is $4/3$-tough, hence $1$-tough, yet has no Hamiltonian cycle (classical: $P$ is hypohamiltonian). This shows $1$-toughness is strictly weaker than Hamiltonicity and motivates raising the threshold. Chvátal's $\tfrac{3}{2}$-tough non-Hamiltonian examples push past $P$, and BBV push past $2$, reaching $\tfrac94 - \varepsilon$.

*How BBV get to $9/4$.* Their graphs are assembled from a fixed non-Hamiltonian "core" whose vertices are blown up into cliques of tuned sizes and joined to a large independent set. Non-Hamiltonicity is forced by an independent set $I$ with $|I| > $ (number of available cycle segments), while the clique sizes are chosen so that every cut $S$ satisfies $|S|/c(G-S) > \tfrac94 - \varepsilon$. Increasing the blow-up drives the ratio to $9/4$ but not past it: the core's fixed combinatorics caps the achievable ratio. Finding a core family whose cap grows without bound would refute Chvátal's conjecture; proving no such family exists would prove it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*