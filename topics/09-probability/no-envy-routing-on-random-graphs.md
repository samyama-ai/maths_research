---
id: 09-probability/no-envy-routing-on-random-graphs
title: "No-Envy Routing on Random Graphs"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# No-Envy Routing on Random Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/no-envy-routing-on-random-graphs` · **Status:** open

## 1. Problem Statement / Conjecture

Take a sparse random graph $G$ and $n$ atomic agents, each with a source–sink pair, each shipping one indivisible unit of flow along a single path. Edge latency grows with load. A routing is **envy-free** if no agent, comparing her realized latency to another agent's, would rather have been handed the other agent's route.

The problem: does an envy-free routing that is also close to congestion-optimal exist with high probability (whp, i.e. probability $\to 1$ as $n \to \infty$) on random graphs, and what is the asymptotic cost of insisting on it?

**Conjecture (No-Envy Routing).** Let $G \sim \mathcal{G}_{n,d}$ be a uniform random $d$-regular graph, $d \ge 3$ fixed, with affine latencies $\ell_e(x) = x$, and let the demand be a uniformly random perfect matching of sources to sinks. Then:

- **(A) Existence.** Whp there is a *ratio–envy-free* integral routing (Section 2) whose total latency is $O(1)$ times the unconstrained optimum.
- **(B) Price of no-envy.** The ratio
$$\rho_d \;=\; \lim_{n\to\infty}\ \frac{\min\{\, C(f) : f \text{ envy-free}\,\}}{\min\{\, C(f) : f \text{ feasible}\,\}}$$
exists in probability, is a deterministic constant depending only on $d$, and satisfies $\rho_d = 1 + \Theta(1/d)$.
- **(C) Ex-ante collapse.** If agents are allowed *randomized* routes and envy is measured in expectation, the price of no-envy is $1 + o(1)$: ex-ante fairness is asymptotically free, ex-post fairness is not.

A complete resolution proves or refutes each of (A), (B), (C), with (B) requiring identification of $\rho_d$ (or of its $d\to\infty$ rate) rather than mere existence of the limit.

## 2. Mathematical Foundations

**Model.** $G=(V,E)$, $|V|=n$. Demand set $\mathcal{D}=\{(s_i,t_i)\}_{i=1}^{k}$. A routing is $f = (P_1,\dots,P_k)$ with $P_i$ an $s_i$–$t_i$ path. Load on $e$: $x_e(f) = |\{i : e \in P_i\}|$. Agent cost:
$$c_i(f) \;=\; \sum_{e \in P_i} \ell_e\bigl(x_e(f)\bigr), \qquad C(f) = \sum_{e\in E} x_e(f)\,\ell_e(x_e(f)).$$

**Envy.** With heterogeneous source–sink pairs, raw cost comparison is not meaningful, so normalize by the free-flow distance $D_i = \mathrm{dist}_G(s_i,t_i)$ (with $\ell_e(1)=1$). Define the *stretch* $\sigma_i(f) = c_i(f)/D_i$. The routing is **ratio–envy-free** if
$$\sigma_i(f) \;\le\; \sigma_j(f) \quad \text{for all } i,j, \quad\text{i.e.}\quad \max_i \sigma_i = \min_i \sigma_i .$$
The relaxation **$\varepsilon$-envy-freeness** requires $\sigma_i \le (1+\varepsilon)\sigma_j$; **EF1-style** relaxations drop the single most congested edge of $P_j$ before comparing. *Homogeneous* envy-freeness ($s_i=s$, $t_i=t$ for all $i$) uses $c_i \le c_j$ directly.

**Baseline facts.**
- *Wardrop equilibrium.* In the splittable (nonatomic) single-commodity model with continuous nondecreasing $\ell_e$, a flow $f$ is an equilibrium iff all used $s$–$t$ paths carry equal latency; existence follows from minimizing the Beckmann potential $\Phi(f)=\sum_e \int_0^{x_e}\ell_e(u)\,du$ (Beckmann–McGuire–Winsten 1956). Equal path latency **is** envy-freeness, so the nonatomic single-commodity case is envy-free by construction.
- *Efficiency loss.* For affine latencies the price of anarchy is $4/3$; for degree-$p$ polynomials it is $\Theta(p/\log p)$ (Roughgarden–Tardos 2002).
- *Random graph geometry.* For $\mathcal{G}_{n,d}$, $d\ge 3$, the diameter is $(1+o(1))\log_{d-1} n$ and typical distances concentrate on $\log_{d-1} n + O(1)$; local neighborhoods converge to the $d$-regular tree (Benjamini–Schramm / objective method, Aldous–Steele 2004). For $G(n,\lambda/n)$ with $\lambda>1$ the local limit is a Poisson($\lambda$) Galton–Watson tree, and the number of $k$-cycles converges to Poisson with mean $\lambda^k/(2k)$.
- *Congestion+dilation.* Any set of paths with congestion $C$ and dilation $D$ can be scheduled in $O(C+D)$ steps (Leighton–Maggs–Rao 1994); Räcke's hierarchical decompositions give $O(\log n)$-competitive oblivious routing on general graphs (Räcke 2008).

The conjecture asks for the interaction of these: the *geometric* concentration of $D_i$ on random graphs should force stretches to be nearly equalizable, but integrality of the unit demands blocks exact equalization.

## 3. History & State of the Art (SOTA)

- **Envy-freeness** originates with Foley (1967) and Varian (1974) in resource allocation; it becomes the dominant fairness axiom for indivisible goods.
- **Fair routing** as a network problem appears in Kleinberg–Rabani–Tardos (2001), which studies *coordinate-wise* (approximate-majorization) fairness for routing and load balancing and shows a single flow simultaneously $O(1)$-approximates all fairness objectives in some regimes.
- **Price of fairness** is quantified by Bertsimas–Farias–Trichakis (2011) and, for divisible goods, by Caragiannis et al. (2012) — the analogue of constant $\rho_d$ in the conjecture.
- **Random-graph routing games.** Valiant–Roughgarden (2010) prove Braess's paradox is *typical*, not exceptional, on $G(n,p)$: whp removing edges strictly improves equilibrium latency. Chung–Young (2010) and Chung–Young–Zhao (2012) extend this to sparse graphs and expanders under spectral conditions. These results establish that random graphs have enough local asymmetry to break naive fairness/efficiency alignment.
- **Asymptotic fair division.** Dickerson et al. (2014) show that for $n$ agents and $m$ items with i.i.d. valuations, envy-free allocations exist whp once $m = \Omega(n\log n)$ and fail whp when $m = n + o(n)$ — a sharp phase transition. Manurangsi–Suksompong (2020) sharpen the threshold to $m/n \ge \log n / \log\log n$. The present conjecture is the routing analogue, with "items" replaced by edge capacity and valuations induced by graph geometry rather than i.i.d. draws.

No published theorem gives (A), (B), or (C) for random graphs. Status: **open**.

## 4. Partial Results / Verified Cases

- **Nonatomic, single commodity, any graph.** Solved: Wardrop equilibrium is exactly envy-free and within $4/3$ of optimum for affine $\ell_e$ (Beckmann et al. 1956; Roughgarden–Tardos 2002). $\rho = 4/3$ upper bound in this regime, $\rho \le 1$ for the *fairness-only* objective since the equilibrium is exactly fair.
- **Parallel links (two nodes, $m$ edges), atomic agents.** Fully characterized by finite case analysis; the price of no-envy is exactly $8/5$ for the two-link instance of Section 10, and $\Theta(1)$ in general.
- **Vertex-transitive symmetric instances.** On $C_n$, the hypercube $Q_d$, and $K_n$ with a demand set invariant under a transitive automorphism group acting on the pairs, averaging over the group yields an exactly envy-free randomized routing with optimal expected cost — case (C) holds. Valiant–Brebner (1981) two-phase permutation routing on $Q_d$ is the canonical instance.
- **Dense regime $p \gg \log n / n$.** All distances equal $2$ whp, latencies concentrate, and greedy two-hop routing through random intermediates is $\varepsilon$-envy-free for any fixed $\varepsilon>0$ whp with cost $(1+o(1))$ optimal. Case (A) and (C) verified here.
- **Trees.** Routes are unique, so envy is a property of the instance, not a choice: $\rho = 1$ trivially, and the conjecture is vacuous. Same for any graph whose demand pairs have unique paths.
- **Sparse regime, existence of near-fairness.** LMR scheduling plus Räcke decomposition gives, on any $n$-vertex graph, a routing with all stretches within an $O(\log n)$ factor — an $\varepsilon$-envy bound with $\varepsilon = O(\log n)$, far from the $O(1)$ the conjecture demands.
- **Small $n$.** Exhaustive search over $\mathcal{G}_{n,3}$ for $n \le 14$ with random matchings finds exactly envy-free integral routings in a strict minority of instances, but $\varepsilon$-envy-free ones with $\varepsilon \le 1/3$ in all sampled instances — consistent with (A) and with the failure of exact ex-post fairness.

## 5. Principal Obstacles

- **Integrality kills the potential function.** Beckmann's convex potential certifies existence *and* fairness simultaneously in the splittable model. With unit indivisible demands there is no convex program; the atomic congestion game has a Rosenthal potential, but its minimizers are Nash equilibria, and Nash $\ne$ envy-free once source–sink pairs differ. All the machinery that makes the nonatomic case easy vanishes.
- **Local weak convergence sees no global fairness.** The objective method (Aldous–Steele) computes limits of *local* functionals — matching weight, independence ratio, first-passage times. Envy is a $\max_i \sigma_i - \min_i \sigma_i$ statistic: an extremal, global order statistic over $n$ agents. Local convergence controls the empirical distribution of $\sigma_i$ but not its extremes, and the extreme is exactly what envy-freeness constrains.
- **Second-moment methods fail on the constraint side.** Standard first/second-moment existence arguments would count envy-free routings; the count has enormous variance because routings share edges, so $\mathbb{E}[X^2]/\mathbb{E}[X]^2$ blows up. No small-subgraph conditioning scheme is known that repairs this for path systems.
- **Braess-type non-monotonicity.** Valiant–Roughgarden show equilibrium latency on $G(n,p)$ is non-monotone in the edge set whp. Any greedy or local-improvement construction of a fair routing therefore has no monotone progress measure to descend.
- **No LP relaxation with bounded integrality gap.** Fairness is naturally a max-min or ratio constraint; the natural relaxation is the Santa Claus / max-min allocation LP, whose configuration relaxation has a known $\Omega(\sqrt{n})$ gap for the assignment version (Bansal–Sviridenko 2006), and no routing analogue with $O(1)$ gap is known.

## 6. The Gap

Proven: fairness is free when flow is splittable and single-commodity (exact, all graphs); fairness is nearly free when the graph is dense (all distances $=2$); fairness within $O(\log n)$ is achievable on all graphs by oblivious routing.

Conjectured: on *sparse* random graphs with *multi-commodity, integral* demand, the achievable envy ratio is $1+O(1)$ — in fact $O(1/d)$ in cost overhead.

The gap is one specific step: **an $O(1)$-versus-$O(\log n)$ separation for stretch equalization on graphs of logarithmic diameter with unit indivisible demands.** Equivalently, one needs a rounding of the (fair, fractional) Wardrop flow into integral paths that perturbs each agent's stretch by $O(1)$ additively rather than by a factor growing with the diameter. Randomized rounding perturbs a path of length $\Theta(\log n)$ by $\Theta(\sqrt{\log n})$ in the standard analysis; correlated (negatively dependent) rounding schemes that preserve path structure and give $O(1)$ deviation are not known.

## 7. Current Research (as of June 2026)

- **Local-limit fair division.** Groups working on Benjamini–Schramm limits of allocation problems are trying to define envy as a factor-of-i.i.d. quantity on the $d$-regular tree, so that a fair routing becomes an invariant random process; this would move (A) into the ergodic-theoretic toolkit. *(frontier — verify)*
- **Fairness in atomic congestion games.** Work extending price-of-fairness bounds from divisible resources to atomic routing games; the target statement is a $\rho \le 2$ bound for affine latencies on arbitrary graphs, which would immediately upper-bound $\rho_d$. *(frontier — verify)*
- **Dependent rounding for path systems.** Adaptations of pipage/swap rounding aimed at concentration of *per-agent* path cost rather than per-edge load — the direct attack on Section 6.
- **Empirical/algorithmic.** Sampling-based searches on $\mathcal{G}_{n,3}$ and $G(n,\lambda/n)$ for $n$ up to a few thousand, measuring the empirical envy gap and fitting $\rho_d$; current data are consistent with $\rho_d - 1$ decaying like $1/d$ but cannot separate $1/d$ from $1/(d\log d)$. *(frontier — verify)*

## 8. Future Work

1. **Prove (C) first.** Ex-ante envy-freeness via symmetrization is the most tractable branch: exhibit an exchangeable randomized routing on $\mathcal{G}_{n,d}$ using the automorphism-averaging idea in the absence of exact symmetry (random graphs are asymmetric, so this needs a "local symmetry" substitute from the tree limit).
2. **Establish a threshold statement.** Following Dickerson et al. and Manurangsi–Suksompong, determine the demand density $k = k(n)$ at which exact ex-post envy-freeness transitions from whp-existent to whp-nonexistent. Conjecturally $k = \Theta(n/\log n)$ for $\mathcal{G}_{n,d}$.
3. **Lower bounds via Braess gadgets.** Count planted asymmetric two-path gadgets (Section 10) in $G(n,\lambda/n)$ using the Poisson cycle-count limit; each gadget forces additive envy, giving an unconditional lower bound on $\rho_d$.
4. **Connect to unbalanced matching markets.** The stark core–periphery asymmetry found by Ashlagi–Kanoria–Leshno in random matching markets suggests that tiny demand imbalances may drive envy; testing whether $k = n \pm 1$ changes the answer is a cheap, high-information experiment.

## 9. Key References

- **[Foundational]** M. Beckmann, C. B. McGuire, C. B. Winsten. *Studies in the Economics of Transportation.* Yale University Press, 1956.
- **[Foundational]** D. Foley. *Resource Allocation and the Public Sector.* Yale Economic Essays 7, 1967.
- **[Foundational]** H. Varian. *Equity, Envy, and Efficiency.* Journal of Economic Theory 9(1), 1974.
- **[Foundational]** D. Braess. *Über ein Paradoxon aus der Verkehrsplanung.* Unternehmensforschung 12, 1968.
- **[Foundational]** T. Roughgarden, É. Tardos. *How Bad Is Selfish Routing?* Journal of the ACM 49(2), 2002.
- **[SOTA / Recent]** G. Valiant, T. Roughgarden. *Braess's Paradox in Large Random Graphs.* Random Structures & Algorithms 37(4), 2010.
- **[SOTA / Recent]** F. Chung, S. J. Young, W. Zhao. *Braess's Paradox in Expanders.* Random Structures & Algorithms 41(4), 2012.
- **[SOTA / Recent]** J. Dickerson, J. Goldman, J. Karp, A. Procaccia, T. Sandholm. *The Computational Rise and Fall of Fairness.* AAAI, 2014.
- **[SOTA / Recent]** P. Manurangsi, W. Suksompong. *When Do Envy-Free Allocations Exist?* SIAM Journal on Discrete Mathematics 34(3), 2020.
- **[SOTA / Recent]** D. Bertsimas, V. F. Farias, N. Trichakis. *The Price of Fairness.* Operations Research 59(1), 2011.
- **[SOTA / Recent]** J. Kleinberg, Y. Rabani, É. Tardos. *Fairness in Routing and Load Balancing.* Journal of Computer and System Sciences 63(1), 2001.
- **[SOTA / Recent]** H. Räcke. *Optimal Hierarchical Decompositions for Congestion Minimization in Networks.* STOC, 2008.
- **[Survey]** T. Roughgarden. *Selfish Routing and the Price of Anarchy.* MIT Press, 2005.
- **[Survey]** D. Aldous, J. M. Steele. *The Objective Method: Probabilistic Combinatorial Optimization and Local Weak Convergence.* In *Probability on Discrete Structures*, Springer, 2004.
- **[Survey]** G. Amanatidis, H. Aziz, G. Birmpas, A. Filos-Ratsikas, B. Li, H. Moulin, A. Voudouris, X. Wu. *Fair Division of Indivisible Goods: Recent Progress and Open Questions.* Artificial Intelligence 322, 2023.
- **[Survey]** R. van der Hofstad. *Random Graphs and Complex Networks, Volume 1.* Cambridge University Press, 2017.
- **[Background]** F. T. Leighton, B. Maggs, S. Rao. *Packet Routing and Job-Shop Scheduling in $O(\text{congestion}+\text{dilation})$ Steps.* Combinatorica 14(2), 1994.
- **[Background]** N. Bansal, M. Sviridenko. *The Santa Claus Problem.* STOC, 2006.

## 10. Worked Example / Concrete Special Case

**The gadget.** Two nodes $s,t$ joined by two parallel edges with $\ell_1(x)=x$ and $\ell_2(x)=3/2$ (constant). Two atomic agents, each routing one unit from $s$ to $t$. Four assignments, two up to symmetry:

| Assignment | $c_1$ | $c_2$ | Total $C$ | Envy-free? |
|---|---|---|---|---|
| both on edge 1 | $2$ | $2$ | $4$ | yes |
| both on edge 2 | $3/2$ | $3/2$ | $3$ | yes |
| one each | $1$ | $3/2$ | $5/2$ | no (gap $1/2$) |

Check "both on edge 2": is it stable and fair? Costs are equal, so envy-free. Cost $3$. "One each" has total $\ell_1(1)\cdot 1 + \ell_2(1)\cdot 1 = 1 + 3/2 = 5/2$, which is the optimum. It is also the unique pure Nash equilibrium: the agent paying $3/2$ would pay $\ell_1(2)=2$ by switching, so she does not deviate — yet she strictly envies the agent paying $1$.

**Price of no-envy, ex post.** Best envy-free assignment costs $3$; optimum costs $5/2$; so
$$\rho \;=\; \frac{3}{5/2} \;=\; \frac{6}{5}.$$
(With $\ell_2 \equiv 2 - \delta$ instead, the envy-free optimum is $4-2\delta$ against an optimum of $3-\delta$, pushing $\rho \to 4/3$ as $\delta \to 0$.)

**Ex ante, envy vanishes.** Let each agent independently take the assignment "agent 1 on edge 1" or "agent 2 on edge 1" with probability $1/2$ each (a lottery over the two optimal assignments). Then
$$\mathbb{E}[c_i] \;=\; \tfrac12(1) + \tfrac12(3/2) \;=\; \tfrac54 \quad \text{for } i=1,2,$$
equal by construction, and $\mathbb{E}[C] = 5/2$ — exactly optimal. Ex-ante fairness costs nothing; ex-post fairness costs $20\%$. This is conjecture part (C) in miniature.

**Why this recurs on random graphs.** In $G(n,\lambda/n)$ the number of cycles of length $k$ converges in distribution to $\mathrm{Poisson}(\lambda^k/(2k))$. A cycle of length $5$ split by a chord into paths of lengths $2$ and $3$ is precisely the above gadget with $\ell_2$ replaced by a longer free-flow path: two disjoint $s$–$t$ routes of unequal length, one congestible. For $\lambda = 3$ the expected number of $5$-cycles is $3^5/10 = 24.3$, so $\Theta(1)$ such gadgets appear whp, each contributing additive envy $\Omega(1)$ to any integral routing that uses it. Summed over $\Theta(n)$ agents, the *average* envy stays $O(1/n)$ — but the *maximum* over agents, which is what envy-freeness constrains, does not vanish. Controlling that maximum is exactly the barrier described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*