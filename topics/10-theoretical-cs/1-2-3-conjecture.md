---
id: 10-theoretical-cs/1-2-3-conjecture
title: "1-2-3 Conjecture"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# 1-2-3 Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/1-2-3-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be a finite simple graph. Call $G$ **nice** if no connected component of $G$ is isomorphic to $K_2$ (a single edge). For an edge weighting $w:E\to\mathbb{Z}_{>0}$ define the induced vertex colour
$$\sigma_w(v)\;=\;\sum_{e\ni v} w(e).$$
The weighting is **proper** (or *vertex-colouring*, *neighbour-sum-distinguishing*) if $\sigma_w(u)\neq\sigma_w(v)$ for every edge $uv\in E$.

**1-2-3 Conjecture (Karoński, Łuczak, Thomason, 2004).** Every nice graph admits a proper edge weighting $w:E\to\{1,2,3\}$.

A component equal to $K_2$ is excluded because its two endpoints always receive the same sum. The bound $3$ is best possible: $K_3$ and $C_5$ admit no proper weighting from $\{1,2\}$ (Section 10).

**Status.** Proved by Ralph Keusch in 2023–2024. A complete proof must supply, for every nice $G$, a weighting from $\{1,2,3\}$; a disproof would exhibit one nice graph where all $3^{|E|}$ weightings fail. Several strengthenings — most notably the **list version** with arbitrary $3$-element lists — remain open, which is why this entry is tracked rather than closed.

## 2. Mathematical Foundations

**Parameter.** The *neighbour-sum-distinguishing index* (also written $s(G)$ or $\chi^e_\Sigma(G)$) is
$$\mu(G)\;=\;\min\{k\;:\;\exists\, w:E\to\{1,\dots,k\}\text{ proper}\}.$$
The conjecture reads $\mu(G)\le 3$ for all nice $G$, and Keusch's theorem establishes it.

**Difference formulation.** Fix a base weighting $w_0\equiv 1$, so $\sigma_{w_0}(v)=\deg(v)$. Writing $w=1+f$ with $f:E\to\{0,1,2\}$ gives $\sigma_w(v)=\deg(v)+\sum_{e\ni v} f(e)$. The task is to choose $f$ so that
$$\deg(u)-\deg(v)\;\neq\;\sum_{e\ni v}f(e)-\sum_{e\ni u}f(e)\qquad\text{for all }uv\in E .$$
Hence only edges joining vertices of *equal or close* degree impose real constraints; the hard core of the problem is the regular-like part of $G$.

**Subgraph / degree-constrained view.** A weighting from $\{1,2\}$ is the same as a spanning subgraph $H\subseteq G$ (the edges of weight $2$) with $\deg_G(v)+\deg_H(v)$ distinct along edges. This is the "degree-constrained subgraph" reformulation of Addario-Berry, Dalal and Reed.

**Algebraic view.** Assign a variable $x_e$ to each edge and form the *graph polynomial*
$$P_G(x)\;=\;\prod_{uv\in E}\Big(\sum_{e\ni u}x_e-\sum_{e\ni v}x_e\Big).$$
A weighting is proper iff $P_G(w)\neq 0$. By the Combinatorial Nullstellensatz (Alon, 1999), if $P_G$ has a monomial $\prod_e x_e^{d_e}$ of maximum total degree $|E|$ with nonzero coefficient and $d_e\le k-1$ for all $e$, then every assignment of $k$-element lists $L(e)$ admits a proper choice $w(e)\in L(e)$. This yields the **list 1-2-3 Conjecture**: every nice graph is $3$-*weight-choosable* (Bartnicki, Grytczuk, Niwczyk, 2009).

**Related invariants.** The *irregularity strength* $s_{\mathrm{irr}}(G)$ (Chartrand et al., 1988) demands all vertex sums be *pairwise* distinct, not just along edges; the 1-2-3 problem is its local relaxation. The *total* variant (weights on vertices and edges, lists $\{1,2\}$) is the **1-2 Conjecture** of Przybyło and Woźniak.

**Complexity.** Deciding $\mu(G)\le 2$ is NP-complete (Dudek and Wajc, 2011); by Keusch's theorem, deciding $\mu(G)\le 3$ is trivial for nice graphs.

## 3. History & State of the Art (SOTA)

- **2004.** Karoński, Łuczak and Thomason introduce the problem in *Edge weights and vertex colours* (JCTB), motivated by irregularity strength. They prove the conjecture for $3$-colourable graphs and, for graphs of large chromatic number, a version with weights from any set of $3$ real numbers under an algebraic condition; no absolute constant bound is obtained in general.
- **2007.** Addario-Berry, Dalal, McDiarmid, Reed and Thomason give the first constant: weights $\{1,\dots,30\}$ always suffice (Combinatorica).
- **2008.** Addario-Berry, Dalal and Reed improve to $16$ via degree-constrained subgraphs; Wang and Yu reach $13$.
- **2010.** Kalkowski, Karoński and Pfender prove $\mu(G)\le 5$ (JCTB) with a short, fully algorithmic greedy argument that fixes vertex sums one at a time inside a nested interval. This "Kalkowski shifting" method dominated the next decade.
- **2016.** Thomassen, Wu and Zhang link the problem to nowhere-zero flows and modulo-$k$ factors, giving flow-based proofs for structured classes.
- **2021–2022.** Przybyło proves the conjecture asymptotically and outright for graphs of large minimum degree: every graph with $\delta(G)\ge 10^{8}$ satisfies $\mu(G)\le 3$ (Combinatorica).
- **2023.** Keusch proves $\mu(G)\le 4$ for all nice graphs, and in the list setting that $4$-element lists always suffice (Combinatorica).
- **2023–2024.** Keusch, *A solution to the 1-2-3 conjecture* (arXiv, March 2023; JCTB, 2024): $\mu(G)\le 3$ for every nice graph. The proof refines the Kalkowski algorithm with a carefully controlled set of "flexible" vertices and a discharging/parity analysis, and does **not** extend to lists.

## 4. Partial Results / Verified Cases

Milestones proved before the general theorem — still the reference points for the open strengthenings:

- **$3$-colourable graphs** (in particular all bipartite and all planar-bipartite graphs): $\mu\le 3$, Karoński–Łuczak–Thomason 2004.
- **$3$-connected bipartite graphs**: $\mu\le 2$ (Lu, Yu, Zhang, 2011). More generally, characterising the graphs with $\mu(G)\le 2$ is NP-hard, so no clean classification is expected.
- **Cycles**: $\mu(C_n)=2$ iff $n\equiv 0\pmod 4$, else $3$. **Complete graphs**: $\mu(K_n)=3$ for $n\ge 3$. **Trees**: $\mu\le 2$ for nice trees other than a few small cases; $\mu(P_3)=2$.
- **Large minimum degree**: $\delta(G)\ge 10^{8}\Rightarrow\mu(G)\le 3$ (Przybyło, 2022); asymptotic versions for $d$-regular graphs with $d\to\infty$.
- **Uniform bounds pre-2023**: $30\to16\to13\to5\to4$ (2007, 2008, 2008, 2010, 2023).
- **Multiset version**: distinguishing neighbours by the *multiset* of incident weights instead of the sum is easier and was settled with $\{1,2,3\}$ well before the sum version.
- **List version**: every nice graph is $4$-weight-choosable (Keusch, 2023); $5$-element lists were known earlier via total-weight-choosability machinery. The case of $3$-element lists is **open**.
- **Computation**: exhaustive search over all small graphs (all connected nice graphs on $\le 10$ vertices) found no counterexample before the proof; such searches are now only of historical interest.

## 5. Principal Obstacles

Why the problem resisted for nearly twenty years, and why the list version still does:

- **No local certificate.** Changing one edge weight shifts two vertex sums simultaneously, so conflicts propagate along paths. There is no bounded-radius structure whose repair is guaranteed not to create a new conflict elsewhere — this kills naive local-search and discharging arguments.
- **Failure of probabilistic methods at $k=3$.** Random weightings from $\{1,2,3\}$ leave $\Theta(|E|/\sqrt{d})$ conflicting edges in a $d$-regular graph; the Lovász Local Lemma needs the conflict probability below $\approx 1/(e\cdot\text{degree of dependency})$, and for $d$-regular graphs the collision probability $\Theta(1/\sqrt{d})$ against dependency degree $\Theta(d)$ fails by a factor $\sqrt{d}$. This is exactly why the early bounds were absolute constants like $30$, obtained from entropy-compression-style or flow arguments with slack, not from $k=3$.
- **Regular graphs carry no degree signal.** For non-regular graphs the base term $\deg(u)-\deg(v)$ already separates most edges. On $d$-regular graphs the whole burden falls on the weighting, and the available "budget" of $\{1,2,3\}$ gives each vertex only $2d+1$ reachable sums while its $d$ neighbours must all be avoided — a counting margin that is linear, not exponential.
- **Kalkowski shifting is intrinsically lossy.** The greedy method processes vertices in an order and reserves for each an interval of admissible sums; with weight set $\{1,\dots,k\}$ the reservation costs one unit of slack per already-processed neighbour, which naturally bottoms out at $k=5$. Getting to $4$ and then $3$ required tracking a global pool of undecided ("flexible") edges and a parity invariant, not a better local rule.
- **Algebraic tools do not reach $3$.** The Combinatorial Nullstellensatz route needs a nonvanishing coefficient of a monomial with all exponents $\le 2$ in $P_G$. Computing coefficients of $P_G$ is $\\#P$-hard in general, and no permanent-type or sign-reversing-involution argument is known to certify nonvanishing for all graphs. This is precisely the barrier that keeps the list version open.

## 6. The Gap

The gap for the *original* statement is closed: Section 4's class-by-class results are subsumed by Keusch's theorem $\mu(G)\le 3$ for all nice $G$. What remains is the gap between the **existence** statement and its **choosability** strengthening:

$$\text{proved: } \forall G \text{ nice, } \exists\, w:E\to\{1,2,3\}\ \text{proper}
\qquad\text{open: } \forall G \text{ nice, } \forall L \text{ with } |L(e)|=3,\ \exists\, w(e)\in L(e)\ \text{proper}.$$

Keusch's argument fixes the weight *values* $1,2,3$ and exploits their arithmetic (differences $1$ and $2$, parity of partial sums) in the shifting step; with arbitrary lists $\{a_e,b_e,c_e\}$ these relations vanish. The precise missing step is either (i) a list-robust version of the flexible-vertex shifting scheme, or (ii) a proof that $P_G$ has a nonzero coefficient on some monomial with all exponents at most $2$. Neither is currently in reach. Secondary gaps: reducing Przybyło's $\delta\ge 10^8$-type thresholds in strengthened variants, and the exact characterisation of $\mu(G)\le 2$ (NP-hard, hence structural only).

## 7. Current Research (as of June 2026)

- **List 1-2-3 Conjecture.** The main open descendant. Best published bound: lists of size $4$ (Keusch, 2023). Work continues on hybrid schemes combining Nullstellensatz certificates for dense parts with shifting on sparse parts. *(frontier — verify)*
- **1-2 Conjecture (total version).** Weights on vertices and edges from $\{1,2\}$; total-weight-choosability results have driven progress here, and post-2023 work asks whether Keusch's technique transfers. *(frontier — verify)*
- **Directed, hypergraph and group-valued analogues.** Neighbour-sum distinguishing weightings with weights in $\mathbb{Z}_k$ or on oriented edges; connections to Tutte's $3$-flow conjecture via the Thomassen–Wu–Zhang framework remain the most promising structural bridge.
- **Algorithmics.** Keusch's proof is constructive and polynomial-time; explicit near-linear-time implementations and distributed/LOCAL-model versions are of active interest in the distributed-computing community. *(frontier — verify)*
- **Groups.** Kraków (Przybyło, Woźniak and collaborators, AGH), ETH Zürich (Keusch), Université Côte d'Azur (Bensmail and coauthors, who maintain the broadest survey activity on distinguishing labellings), and Chinese groups working on total weight choosability.

## 8. Future Work

- Find a *list-robust* invariant replacing the parity/interval bookkeeping in the shifting argument — the consensus route to the list conjecture.
- Develop tractable sufficient conditions for nonvanishing coefficients of the graph polynomial $P_G$ (e.g. via Alon–Tarsi orientations adapted to sum-distinguishing polynomials).
- Push minimum-degree thresholds in strengthened variants from $10^8$ down to small explicit constants, ideally by replacing the regularity/absorption machinery with a direct argument.
- Settle the complexity of recognising $\mu(G)\le 2$ on restricted classes (planar, bipartite, bounded treewidth) — currently NP-complete in general.
- Extend to *total* and *multiset* settings uniformly, aiming at a single theorem implying the 1-2, 1-2-3 and multiset conjectures.

## 9. Key References

- **[Foundational]** M. Karoński, T. Łuczak, A. Thomason. *Edge weights and vertex colours.* Journal of Combinatorial Theory, Series B, 91(1):151–157, 2004.
- **[SOTA / Solution]** R. Keusch. *A solution to the 1-2-3 conjecture.* Journal of Combinatorial Theory, Series B, 2024 (arXiv:2303.02611, 2023).
- **[SOTA]** R. Keusch. *Vertex-coloring graphs with 4-edge-weightings.* Combinatorica, 43:651–658, 2023.
- **[Key milestone]** M. Kalkowski, M. Karoński, F. Pfender. *Vertex-coloring edge-weightings: towards the 1-2-3 conjecture.* Journal of Combinatorial Theory, Series B, 100(3):347–349, 2010.
- **[Milestone]** L. Addario-Berry, K. Dalal, C. McDiarmid, B. A. Reed, A. Thomason. *Vertex-colouring edge-weightings.* Combinatorica, 27(1):1–12, 2007.
- **[Milestone]** L. Addario-Berry, K. Dalal, B. A. Reed. *Degree constrained subgraphs.* Discrete Applied Mathematics, 156(7):1168–1174, 2008.
- **[Large degree]** J. Przybyło. *The 1-2-3 Conjecture holds for graphs with large enough minimum degree.* Combinatorica, 2022.
- **[Structural]** C. Thomassen, Y. Wu, C.-Q. Zhang. *The 3-flow conjecture, factors modulo k, and the 1-2-3-conjecture.* Journal of Combinatorial Theory, Series B, 121:308–325, 2016.
- **[List version]** T. Bartnicki, J. Grytczuk, S. Niwczyk. *Weight choosability of graphs.* Journal of Graph Theory, 60(3):242–256, 2009.
- **[Complexity]** A. Dudek, D. Wajc. *On the complexity of vertex-coloring edge-weightings.* Discrete Mathematics and Theoretical Computer Science, 13(3):45–50, 2011.
- **[Two weights]** H. Lu, Q. Yu, C.-Q. Zhang. *Vertex-coloring 2-edge-weighting of graphs.* European Journal of Combinatorics, 32(1):21–27, 2011.
- **[Origin of the family]** G. Chartrand, M. S. Jacobson, J. Lehel, O. R. Oellermann, S. Ruiz, F. Saba. *Irregular networks.* Congressus Numerantium, 64:197–210, 1988.
- **[Survey]** B. Seamone. *The 1-2-3 Conjecture and related problems: a survey.* arXiv:1211.5122, 2012.
- **[Tool]** N. Alon. *Combinatorial Nullstellensatz.* Combinatorics, Probability and Computing, 8(1–2):7–29, 1999.

## 10. Worked Example / Concrete Special Case

**The 5-cycle $C_5$: two weights fail, three succeed.**

Label vertices $v_1,\dots,v_5$ cyclically and edges $e_i=v_iv_{i+1}$ (indices mod $5$), with weights $a_i=w(e_i)$. Then
$$\sigma(v_i)=a_{i-1}+a_i .$$

*Claim: no proper weighting exists with $a_i\in\{1,2\}$.* The edge $e_i=v_iv_{i+1}$ is satisfied iff
$$\sigma(v_i)\neq\sigma(v_{i+1})\iff a_{i-1}+a_i\neq a_i+a_{i+1}\iff a_{i-1}\neq a_{i+1}.$$
So a proper $\{1,2\}$-weighting is exactly a $2$-colouring of the index set $\mathbb{Z}_5$ in which every pair of indices at distance $2$ gets different colours. The "distance-$2$" graph on $\mathbb{Z}_5$ is itself a $5$-cycle ($1\!-\!3\!-\!5\!-\!2\!-\!4\!-\!1$), an odd cycle, which has chromatic number $3$. No $2$-colouring exists, hence $\mu(C_5)\ge 3$. The same computation shows $\mu(C_n)=2$ exactly when $n\equiv 0 \pmod 4$ (for $n$ odd the distance-$2$ graph is an odd cycle; for $n\equiv 2 \pmod 4$ it is two odd cycles).

*A proper $\{1,2,3\}$-weighting.* Take $(a_1,\dots,a_5)=(1,1,2,2,3)$:

| vertex | $\sigma$ | computation |
|---|---|---|
| $v_1$ | $4$ | $a_5+a_1=3+1$ |
| $v_2$ | $2$ | $a_1+a_2=1+1$ |
| $v_3$ | $3$ | $a_2+a_3=1+2$ |
| $v_4$ | $4$ | $a_3+a_4=2+2$ |
| $v_5$ | $5$ | $a_4+a_5=2+3$ |

Checking the five edges: $4\neq2$, $2\neq3$, $3\neq4$, $4\neq5$, $5\neq4$. All satisfied, so $\mu(C_5)=3$.

**$K_3$ shows tightness a second way.** With edge weights $a,b,c$ the vertex sums are $a+b$, $b+c$, $c+a$; these are pairwise distinct iff $a,b,c$ are pairwise distinct. Two weight values therefore never suffice, and $\{1,2,3\}$ gives sums $3,5,4$. Both examples confirm that the constant $3$ in the conjecture cannot be lowered, and together with Keusch's theorem they pin the extremal value exactly: $\max_{G\text{ nice}}\mu(G)=3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*