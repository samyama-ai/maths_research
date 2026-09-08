---
id: 10-theoretical-cs/densest-k-subgraph-approximation
title: "Hardness of Approximating Densest k-Subgraph"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hardness of Approximating Densest k-Subgraph

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/densest-k-subgraph-approximation` · **Status:** open

## 1. Problem Statement / Conjecture

**Densest $k$-Subgraph (DkS).** Given an undirected graph $G=(V,E)$ with $|V|=n$ and an integer $k\le n$, find $S\subseteq V$ with $|S|=k$ maximizing the number of induced edges $e(S)=|E(G[S])|$.

The open problem is to determine the exact polynomial-time approximability of DkS. The best known algorithm achieves ratio $O(n^{1/4+\varepsilon})$ (Bhaskara–Charikar–Chlamtáč–Feige–Vijayaraghavan, 2010); the best known NP/ETH-based hardness is $n^{1/(\log\log n)^{c}}$ for some constant $c>0$ (Manurangsi, 2017). Neither bound is believed tight.

**Conjecture (polynomial hardness).** There exists $\delta>0$ such that no polynomial-time algorithm approximates DkS within $n^{\delta}$, unless $\mathrm{NP}\subseteq\mathrm{BPTIME}(n^{\mathrm{polylog}\,n})$ or a comparable collapse occurs. A stronger form, consistent with all current evidence, asserts hardness at ratio $n^{1/4-o(1)}$, matching the algorithm.

A complete resolution requires either (i) a polynomial-time $n^{1/4-\Omega(1)}$-approximation, or (ii) a reduction from a standard complexity assumption (P $\ne$ NP, ETH, Gap-ETH, SSE, or planted clique) producing a gap of $n^{\Omega(1)}$.

## 2. Mathematical Foundations

For $S\subseteq V$ define the **density** and **average degree**
$$
d(S)=\frac{e(S)}{\binom{|S|}{2}},\qquad \bar{d}(S)=\frac{2e(S)}{|S|},\qquad \mathrm{OPT}_k(G)=\max_{|S|=k} e(S).
$$
An algorithm is an $\rho$-approximation if it outputs $S$, $|S|=k$, with $e(S)\ge \mathrm{OPT}_k(G)/\rho$.

**Unconstrained relaxation.** $\max_{S\ne\emptyset}\bar d(S)/2$ is solvable exactly in polynomial time by maximum flow (Goldberg, 1984) and $2$-approximated by iterative min-degree peeling (Charikar, 2000). The cardinality constraint $|S|=k$ is exactly what destroys this: the objective $e(S)$ is supermodular, and maximizing a supermodular function under a cardinality constraint is not covered by any known tractable framework.

**Standard LP/SDP relaxation.** With $x_i\in[0,1]$ for vertices and $y_{ij}$ for edges:
$$
\max \sum_{ij\in E} y_{ij}\quad \text{s.t.}\quad \sum_i x_i = k,\ \ y_{ij}\le x_i,\ y_{ij}\le x_j,\ \ \sum_{j} y_{ij} \le k\,x_i .
$$
This LP has integrality gap $\Theta(n/k)$; $\Omega(n^{\Omega(1)})$ rounds of the Sherali–Adams and Lasserre hierarchies still have gap $n^{\Omega(1)}$ (Bhaskara–Charikar–Guruswami–Vijayaraghavan–Zhou, 2012).

**Log-density.** For a graph $H$ on $m$ vertices with average degree $D$, its log-density is $\log_m D$. The distinguishing problem $\mathsf{D}(n,k,\alpha,\beta)$ asks to separate $G\sim G(n,p)$ with $p=n^{\alpha-1}$ (average degree $n^{\alpha}$) from the same distribution with a $k=n^{\beta}$-vertex subgraph of average degree $n^{\beta\alpha'}$ planted. The **log-density threshold** states: planted structure is detectable by counting-based (small-subgraph) certificates iff its log-density $\alpha'$ exceeds the ambient log-density $\alpha$. Below that threshold, no known certificate exists. Optimizing the resulting gap over $\alpha,\beta$ yields exactly $n^{1/4}$ — the algorithmic frontier.

**Related problems.** Densest At-Least-$k$-Subgraph (DalkS) admits a $2$-approximation (Andersen–Chellapilla 2009; Khuller–Saha 2009). Densest At-Most-$k$-Subgraph is equivalent to DkS up to a factor $4$. Maximum Balanced Biclique, Smallest $m$-Edge Subgraph and Label Cover all sit at the same log-density threshold.

## 3. History & State of the Art (SOTA)

- **1984–1993.** Goldberg solves the unconstrained problem by flow. Kortsarz and Peleg (FOCS 1993) give the first nontrivial ratio $O(n^{0.3885})$.
- **2001.** Feige, Kortsarz and Peleg (*Algorithmica* 29:410–421) give $O(n^{1/3-\varepsilon})$ with $\varepsilon\approx 1/60$, combining a greedy walk, a semidefinite step, and case analysis on $k$. This stood for nine years.
- **2006.** Khot (*SICOMP* 36(4)) rules out a PTAS under the assumption that NP has no randomized subexponential algorithms — the first hardness beyond APX for DkS.
- **2010.** Bhaskara, Charikar, Chlamtáč, Feige and Vijayaraghavan (STOC 2010) achieve $O(n^{1/4+\varepsilon})$ in time $n^{O(1/\varepsilon)}$, via the log-density framework: identify a tree-like "witness" subgraph whose expected count separates planted from ambient density.
- **2012.** Matching $n^{1/4}$ integrality gaps for $\Omega(n)$-round LP/SDP hierarchies (BCGVZ, SODA 2012).
- **2017.** Manurangsi (STOC 2017) proves $n^{1/(\log\log n)^{c}}$-hardness under ETH via birthday repetition on a Label-Cover-like PCP — almost polynomial, but not polynomial. Braverman, Ko, Rubinstein and Weinstein (SODA 2017) obtain the same ratio for the perfect-completeness variant.
- **2023.** Jones, Potechin, Rajendran and Xu (STOC 2023) prove degree-$d$ Sum-of-Squares lower bounds for DkS on random graphs, extending the hierarchy barrier to the strongest known convex-programming family.

Current status: algorithm $n^{1/4+\varepsilon}$; hardness $n^{1/(\log\log n)^{c}}$. The gap between them is the open problem.

## 4. Partial Results / Verified Cases

- **$k=\Omega(n)$ with $|E|=\Omega(n^{2})$:** PTAS via dense-instance sampling (Arora, Karger, Karpinski, *JCSS* 58, 1999).
- **$k = n^{1-o(1)}$:** trivial random sampling gives ratio $O(n/k)=n^{o(1)}$.
- **$k=O(\log n / \log\log n)$:** exhaustive search in quasi-polynomial time $n^{O(k)}$; exact.
- **Cographs and $P_4$-sparse graphs:** exact polynomial-time dynamic programming (Corneil & Perl, 1984).
- **Bounded treewidth $t$:** exact in $n^{O(1)}\cdot 2^{O(t)}\cdot k^{O(1)}$ by standard DP over a tree decomposition.
- **Bounded degeneracy / arboricity $d$:** $O(d)$-approximation by peeling; constant-factor for planar graphs.
- **Unconstrained density ($k$ free):** exactly solvable (Goldberg 1984); $(1+\varepsilon)$ in near-linear time (Chekuri–Quanrud–Torres, SODA 2022).
- **DalkS (size $\ge k$):** factor $2$, and $2$ is optimal under the Small Set Expansion hypothesis (Manurangsi, *Algorithms* 11(1), 2018).
- **Hardness verified:** no PTAS under randomized ETH (Khot 2006); $n^{1/(\log\log n)^{c}}$ under ETH (Manurangsi 2017); $n^{1/4}$ gaps for $\Omega(n)$-round Lasserre and for low-degree SoS on random instances.
- **NP-hardness** holds already on bipartite graphs of maximum degree $3$ and on chordal graphs.

## 5. Principal Obstacles

- **No gap-preserving reduction with polynomial loss.** DkS is a *maximization with a hard cardinality constraint*; standard PCP-based reductions (from Label Cover, from Max-3SAT) blow up instance size polynomially while producing only a constant or quasi-polylogarithmic gap. Birthday repetition — the only technique that has produced almost-polynomial gaps — inherently costs $n^{\Theta(\log n)}$ blowup, which caps the achievable ratio at $n^{1/\mathrm{polyloglog}\,n}$ under ETH. Getting $n^{\Omega(1)}$ needs a PCP with subexponential-size *and* strongly sublinear soundness, which no known construction provides.
- **Convex hierarchies are exhausted.** Sherali–Adams, Lasserre and SoS all exhibit $n^{1/4}$ gaps at $n^{\Omega(1)}$ rounds. Any improved algorithm must be non-relaxation-based.
- **Small-subgraph counting saturates at log-density.** Every known algorithm certifies density via counts of constant-size witnesses. In $G(n,n^{\alpha-1})$ a subgraph $H$ with $v$ vertices, $e$ edges has expected count $n^{v}p^{e}=n^{v-e(1-\alpha)}$; witnesses that are informative exist only above the log-density threshold, and the threshold optimizes to exactly $n^{1/4}$.
- **Average-case assumptions are non-standard.** Polynomial hardness is known only from planted-clique-type or random-$k$-AND hypotheses (Alon–Arora–Manokaran–Moshkovitz–Weinstein, 2011), which are not implied by P $\ne$ NP and remain unfalsifiable by current tools.
- **No unique-games route.** Unlike Max-Cut or Vertex Cover, DkS has no known UGC-based tight hardness; the Small Set Expansion hypothesis yields tightness for DalkS but not DkS.

## 6. The Gap

Proven lower bound: ratio $n^{1/(\log\log n)^{c}}=n^{o(1)}$ under ETH. Proven upper bound: $n^{1/4+\varepsilon}$. The missing step is a hardness amplification that converts a quasi-polylogarithmic gap into a polynomial one *without* superpolynomial instance blowup. Equivalently: a PCP for Label Cover with alphabet size $n^{\Omega(1)}$, soundness $n^{-\Omega(1)}$, and proof length $n^{O(1)}$ — the "polynomial-gap projection PCP" that would also settle Smallest $m$-Edge Subgraph and Balanced Biclique. Conversely, breaking $n^{1/4}$ algorithmically requires a certificate for planted density *below* the log-density threshold, which no spectral, counting, or SoS method currently supplies.

## 7. Current Research (as of June 2026)

- **Low-degree polynomial and SoS barriers.** Following Jones–Potechin–Rajendran–Xu (2023), groups at Chicago, CMU and Berkeley are mapping the precise degree/ratio trade-off for DkS on planted-dense-subgraph distributions, aiming at a "low-degree conjecture" statement matching $n^{1/4}$. *(frontier — verify)*
- **Log-density as a unifying threshold.** Chlamtáč, Manurangsi, Moshkovitz and Vijayaraghavan (SODA 2017) placed Label Cover at the same threshold; work continues on transferring hardness *between* threshold problems rather than from NP-hardness. Groups: Ben-Gurion (Chlamtáč), Google Research (Manurangsi), Northwestern.
- **Parameterized inapproximability.** Under Gap-ETH, no FPT algorithm parameterized by $k$ approximates DkS within any constant; extending this to $k^{\Omega(1)}$ ratios in FPT time is active. *(frontier — verify)*
- **Practical/heuristic side.** Lanciano–Miyauchi–Fazzone–Bonchi (*ACM Computing Surveys*, 2024) survey the algorithm-engineering literature; ILP and local-search solvers routinely handle $n\sim10^{5}$ on real networks despite worst-case hardness.

## 8. Future Work

1. Construct a projection PCP with polynomial alphabet and polynomial length — the single step that would give $n^{\Omega(1)}$ hardness for DkS, Balanced Biclique and Smallest $m$-Edge Subgraph simultaneously.
2. Formalize and defend a clean average-case hypothesis (planted dense subgraph at log-density $\alpha$) as a first-class assumption, then derive tight $n^{1/4}$ hardness from it.
3. Prove unconditional low-degree/SoS lower bounds at ratio $n^{1/4-o(1)}$ for *all* degrees $n^{\Omega(1)}$, closing the convex-programming route.
4. Attack the algorithmic side: find a certificate exploiting global spectral structure rather than local subgraph counts, targeting $n^{1/4-\Omega(1)}$.
5. Settle the parameterized version: is there an $f(k)\cdot n^{O(1)}$-time $O(1)$-approximation?

## 9. Key References

- **[Foundational]** A. V. Goldberg. *Finding a Maximum Density Subgraph.* Technical Report UCB/CSD-84-171, UC Berkeley, 1984.
- **[Foundational]** G. Kortsarz, D. Peleg. *On Choosing a Dense Subgraph.* FOCS 1993, 692–701.
- **[Foundational]** U. Feige, G. Kortsarz, D. Peleg. *The Dense k-Subgraph Problem.* Algorithmica 29(3):410–421, 2001.
- **[Foundational]** M. Charikar. *Greedy Approximation Algorithms for Finding Dense Components in a Graph.* APPROX 2000, LNCS 1913, 84–95.
- **[SOTA]** A. Bhaskara, M. Charikar, E. Chlamtáč, U. Feige, A. Vijayaraghavan. *Detecting High Log-Densities — an $O(n^{1/4})$ Approximation for Densest k-Subgraph.* STOC 2010, 201–210.
- **[SOTA]** A. Bhaskara, M. Charikar, V. Guruswami, A. Vijayaraghavan, Y. Zhou. *Polynomial Integrality Gaps for Strong SDP Relaxations of Densest k-Subgraph.* SODA 2012, 388–405.
- **[Hardness]** S. Khot. *Ruling Out PTAS for Graph Min-Bisection, Dense k-Subgraph, and Bipartite Clique.* SIAM Journal on Computing 36(4):1025–1071, 2006.
- **[Hardness]** P. Manurangsi. *Almost-Polynomial Ratio ETH-Hardness of Approximating Densest k-Subgraph.* STOC 2017, 954–961.
- **[Hardness]** M. Braverman, Y. K. Ko, A. Rubinstein, O. Weinstein. *ETH Hardness for Densest-k-Subgraph with Perfect Completeness.* SODA 2017, 1326–1341.
- **[Hardness]** N. Alon, S. Arora, R. Manokaran, D. Moshkovitz, O. Weinstein. *Inapproximability of Densest κ-Subgraph from Average Case Hardness.* Manuscript, 2011.
- **[Recent]** C. Jones, A. Potechin, G. Rajendran, J. Xu. *Sum-of-Squares Lower Bounds for Densest k-Subgraph.* STOC 2023, 84–95.
- **[Recent]** E. Chlamtáč, P. Manurangsi, D. Moshkovitz, A. Vijayaraghavan. *Approximation Algorithms for Label Cover and The Log-Density Threshold.* SODA 2017, 900–919.
- **[Related]** P. Manurangsi. *Inapproximability of Maximum Biclique Problems, Minimum k-Cut and Densest At-Least-k-Subgraph from the Small Set Expansion Hypothesis.* Algorithms 11(1):10, 2018.
- **[Related]** S. Khuller, B. Saha. *On Finding Dense Subgraphs.* ICALP 2009, LNCS 5555, 597–608.
- **[Related]** S. Arora, D. Karger, M. Karpinski. *Polynomial Time Approximation Schemes for Dense Instances of NP-Hard Problems.* Journal of Computer and System Sciences 58(1):193–210, 1999.
- **[Survey]** T. Lanciano, A. Miyauchi, A. Fazzone, F. Bonchi. *A Survey on the Densest Subgraph Problem and Its Variants.* ACM Computing Surveys 56(8), 2024.

## 10. Worked Example / Concrete Special Case

**The $n^{1/4}$ hard instance, instantiated.** Take $n=10^{8}$, $p=10^{-4}=n^{-1/2}$, so ambient log-density $\alpha=1/2$ and average degree $np=10^{4}=n^{1/2}$. Set $k=10^{4}=n^{1/2}$.

*Null case.* In $G\sim G(n,p)$, any fixed $k$-set has expected internal average degree
$$
kp = 10^{4}\cdot10^{-4}=1,
$$
and a union bound over $\binom{n}{k}$ sets gives $\mathrm{OPT}_k(G)=O(k\log n)$ edges w.h.p. — average degree $O(\log n)$.

*Planted case.* Overwrite a random $k$-set with a graph of average degree $D=10^{2}=n^{1/4}$, i.e. $e(S)=kD/2=5\times10^{5}$ edges. Its log-density is
$$
\log_k D=\frac{\tfrac14\log n}{\tfrac12\log n}=\tfrac12=\alpha,
$$
exactly the ambient log-density.

*Why no local certificate works.* For a fixed subgraph $H$ with $v$ vertices and $e$ edges, its expected number of copies in the ambient graph is
$$
\mathbb{E}[\\#H]\;\approx\;n^{v}p^{e}=n^{\,v-e/2},
$$
which is $\gg 1$ whenever $e<2v$ — every $H$ of average degree below $4$ already saturates the ambient graph, so counting such copies cannot localize the plant. Conversely $H$ with $e\ge 2v$ has expected count $\le 1$ ambiently, but the planted set of size $n^{1/2}$ and degree $n^{1/4}$ also contains only $\approx k^{v}(D/k)^{e}=n^{v/2-e/4}$ copies, which is $<1$ once $e>2v$. The two counts cross precisely at the threshold: no constant-size witness separates the cases.

*The gap.* An algorithm restricted to such certificates returns a set with $\Theta(k\log n)$ edges while $\mathrm{OPT}_k=5\times10^{5}$, giving ratio
$$
\frac{n^{1/4}}{O(\log n)} = \tilde\Theta(n^{1/4}) \approx 100/\log n .
$$
Raising the plant to degree $n^{1/4+\delta}$ pushes its log-density above $\alpha$ and the BCCFV witness-counting algorithm finds it. Lowering it below $n^{1/4}$ leaves it undetectable but also uninteresting. This single instance family is simultaneously the tight case for the best algorithm, the source of the $n^{1/4}$ Lasserre and SoS integrality gaps, and the conjectured — but unproven — true hardness threshold.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*