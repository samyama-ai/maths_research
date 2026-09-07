---
id: 10-theoretical-cs/linear-time-maximum-flow
title: "Linear Time Maximum Flow"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Linear Time Maximum Flow

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/linear-time-maximum-flow` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Given a directed graph $G=(V,E)$ with $|V|=n$, $|E|=m$, integer capacities $u:E\to\{1,\dots,U\}$, and terminals $s,t\in V$, compute a maximum $s$–$t$ flow exactly.

**The question.** Is there an algorithm running in time $O(m\,\mathrm{polylog}(n\,U))$ — or, in the strongest form, $O(m)$ — on the word RAM with $O(\log(nU))$-bit words?

Status is `solved-recently` for the *almost*-linear form: Chen, Kyng, Liu, Peng, Probst Gutenberg and Sachdeva (FOCS 2022) gave an $m^{1+o(1)}\log U$-time algorithm for min-cost flow, hence for max flow. What remains open is the gap between $m^{1+o(1)}$ and $O(m\,\mathrm{polylog})$: the $m^{o(1)}$ factor is subpolynomial but superpolylogarithmic, of the form $\exp(O(\log^{c} m))$ for some $c<1$ coming from recursively built dynamic low-stretch trees. A complete resolution is either (a) an algorithm with a genuinely polylogarithmic overhead, or (b) a lower bound separating exact max flow from $O(m\,\mathrm{polylog})$ in a model that captures all known techniques.

## 2. Mathematical Foundations

Let $B\in\mathbb{R}^{E\times V}$ be the edge–vertex incidence matrix, $B_{e,v}=+1$ if $e$ enters $v$, $-1$ if it leaves. A flow is $f\in\mathbb{R}^E$. Max flow is the linear program

$$\max_{f\in\mathbb{R}^E} \; F \quad\text{s.t.}\quad B^{\top} f = F\,(\mathbb{1}_t-\mathbb{1}_s),\qquad 0\le f_e\le u_e .$$

**Duality (max-flow min-cut).** $\max F = \min_{S:\,s\in S,\ t\notin S} \sum_{e\in E(S,\bar S)} u_e$. Integrality of the polytope (total unimodularity of $B$) makes the optimum integral for integral $u$.

**Min-cost flow generalisation.** With costs $c\in\mathbb{Z}^E$ and demands $d\in\mathbb{Z}^V$, $\sum_v d_v=0$:
$$\min_{B^{\top}f=d,\;\ell\le f\le u} c^{\top} f .$$
Max flow is the special case with an added arc $t\to s$ of cost $-1$ and capacity $\infty$.

**The $\ell_1$ interior-point framework.** The modern algorithm replaces the $\ell_2$ (electrical) Newton step by an $\ell_1$ one. Minimising the barrier potential
$$\Phi(f)=20m\log\big(c^{\top}f - F^{*}\big)+\sum_{e\in E}\Big[(u_e-f_e)^{-\alpha}+(f_e-\ell_e)^{-\alpha}\Big],\qquad \alpha=\tfrac{1}{1000\log mU},$$
each step requires an *undirected minimum-ratio cycle*: with $g=\nabla\Phi(f)$ and lengths $L=\mathrm{diag}(\ell)$ built from second derivatives,
$$\min_{\Delta\in\mathbb{R}^E,\ B^{\top}\Delta=0}\ \frac{g^{\top}\Delta}{\lVert L\Delta\rVert_1}.$$
Solving this to within an $m^{o(1)}$ multiplicative factor suffices; $\widetilde O(m)$ steps then reach optimality, and exactness follows by rounding to a vertex once the duality gap is below $1/(nU)^{O(1)}$.

**The data-structure core.** The approximate minimiser is realised as a *tree cycle*: maintain a collection of $m^{o(1)}$ spanning trees with average stretch $m^{o(1)}$ under edge-weight updates, so that for some tree $T$ and off-tree edge $e$, the fundamental cycle $\Delta = \mathbb{1}_e - P_T(e)$ achieves ratio within $m^{o(1)}$ of optimal. Detection and update use link–cut trees (Sleator–Tarjan, 1983) over a hierarchy of $\Theta(\log m)$ levels of vertex/edge sparsification, each level costing $m^{o(1)}$ — the product of level costs is exactly where the $\exp(O(\log^{c}m))$ factor is born.

## 3. History & State of the Art (SOTA)

- **1956** — Ford and Fulkerson define the problem and prove max-flow min-cut.
- **1970/1972** — Dinitz's blocking-flow algorithm ($O(n^2m)$, $O(m\sqrt m)$ unit capacities); Edmonds–Karp $O(m^2n)$ and the first strongly polynomial bounds.
- **1988** — Goldberg–Tarjan push–relabel, $O(nm\log(n^2/m))$.
- **1998** — Goldberg–Rao, $O(m\min(m^{1/2},n^{2/3})\log(n^2/m)\log U)$: the last purely combinatorial improvement, and the origin of the phrase "flow decomposition barrier" ($\Theta(mn)$, the size of a path decomposition).
- **2011** — Christiano–Kelner–Mądry–Spielman–Teng: electrical flows give $\tilde O(mn^{1/3}\varepsilon^{-11/3})$ approximate undirected flow. Continuous optimisation enters.
- **2013–2016** — Sherman; Kelner–Lee–Orecchia–Sidford: $(1+\varepsilon)$-approximate undirected max flow in $m^{1+o(1)}\varepsilon^{-2}$, then $O(m\,\mathrm{polylog}\,n\cdot\varepsilon^{-2})$ (Peng, 2016). Mądry: exact $\tilde O(m^{10/7}U^{1/7})$ for unit capacities.
- **2020** — Kathuria–Liu–Sidford and Liu–Sidford: $m^{4/3+o(1)}U^{1/3}$. van den Brand et al.: $\tilde O(m^{3/2-1/328}\log U)$ for general capacities.
- **2022** — **Chen, Kyng, Liu, Peng, Probst Gutenberg, Sachdeva**: min-cost flow (hence max flow, bipartite matching, negative-weight shortest paths) in $m^{1+o(1)}\log U$. FOCS 2022 best paper.
- **2023** — van den Brand, Chen, Kyng, Liu, Peng, Probst Gutenberg, Sachdeva, Sidford: deterministic $m^{1+o(1)}$, removing the oblivious-adversary assumption.
- **2024** — Chen, Kyng, Liu, Meierhans, Probst Gutenberg: incremental min-cost flow in $m^{1+o(1)}$ total time.

## 4. Partial Results / Verified Cases

True $O(m\,\mathrm{polylog})$ or better is proven in these regimes:

| Class | Bound | Source |
|---|---|---|
| Directed planar $s$–$t$ max flow | $O(n\log n)$ | Borradaile–Klein 2009 |
| Undirected planar min cut | $O(n\log\log n)$ | Italiano–Nussbaum–Sankowski–Wulff-Nilsen 2011 |
| Undirected $(1+\varepsilon)$-approximate | $O(m\,\mathrm{polylog}(n)\,\varepsilon^{-2})$ | Peng 2016 |
| Dense graphs, $m=\Theta(n^2)$ | $\tilde O(n^2)=\tilde O(m)$ | van den Brand et al. 2021 |
| Negative-weight SSSP (a flow-adjacent dual) | $O(m\log^{8}(n)\log W)$ | Bernstein–Nanongkai–Wulff-Nilsen 2022 |
| Series-parallel / bounded-treewidth $k$ | $O(k^{O(1)} n)$ | dynamic programming, folklore |
| Trees, $st$-paths, $U=1$ with $n$ paths | $O(m)$ | trivial |

Strongly polynomial: Orlin's $O(nm)$ (2013) is still the best strongly polynomial bound — the $m^{1+o(1)}$ result depends on $\log U$ and is *not* strongly polynomial.

## 5. Principal Obstacles

- **The subpolynomial factor is structural, not cosmetic.** The $m^{o(1)}$ term arises from $\Theta(\log m)$ nested levels of dynamic sparsification, each contributing an $m^{o(1)}$ or $\log^{O(1)}$ factor *multiplicatively*; a product of $\log m$ polylogarithmic factors is $\log^{\Theta(\log m)}m = \exp(\Theta(\log m\log\log m))$, already superpolylogarithmic. Flattening the recursion requires a dynamic low-stretch spanning tree with $\mathrm{polylog}$ stretch *and* $\mathrm{polylog}$ amortised update time under adaptive adversaries — currently unknown even statically for the fully dynamic setting.
- **$\widetilde{O}(m)$ IPM iterations, each nontrivial.** The $\ell_1$-IPM needs $\widetilde\Theta(m)$ steps, so the per-step budget is $m^{o(1)}$ — there is no slack. Reducing the iteration count to $\mathrm{polylog}$ would need a self-concordant barrier of complexity $\mathrm{polylog}$ for the flow polytope; Nesterov–Nemirovski theory lower-bounds barrier parameter by the number of facets' geometry, and $\sqrt m$ is the standard limit ($\sqrt n$-type barriers give $\tilde O(\sqrt m)$ iterations but $\tilde\Omega(m)$ work per iteration via Laplacian solves plus maintenance).
- **Combinatorial methods are stuck at the flow decomposition barrier.** Augmenting-path and blocking-flow schemes manipulate paths; a maximum flow can require $\Theta(m)$ paths of length $\Theta(n)$, so any algorithm that explicitly routes paths pays $\Omega(mn)$. Goldberg–Rao circumvent it only partially via binary length functions.
- **Exactness requires bit precision.** Continuous methods produce a fractional near-optimal flow; recovering an integral optimum needs $\Omega(\log(nU))$ bits of accuracy, forcing the $\log U$ dependence and blocking strong polynomiality.
- **No lower bounds beyond $\Omega(m)$.** There is no unconditional superlinear lower bound, and fine-grained hardness (SETH, 3SUM, APSP) has produced no reduction to exact max flow, so the problem is barrier-free from below as well as unresolved from above.

## 6. The Gap

Proven: $m^{1+o(1)}\log U$, with $m^{o(1)}=\exp(O(\log^{c}m))$, $c<1$. Sought: $O(m\,\mathrm{polylog}(nU))$.

The exact step to cross: replace the $\Theta(\log m)$-level recursive hierarchy of dynamic vertex/edge sparsifiers by a **single-level** dynamic data structure that maintains, under $\widetilde O(m)$ adaptive edge-weight updates, a spanning-tree collection of stretch $\mathrm{polylog}(n)$ with $\mathrm{polylog}(n)$ amortised time per update and per min-ratio-cycle query. Equivalently: an $\ell_1$ oracle with $\mathrm{polylog}$ approximation and $\mathrm{polylog}$ update cost. Every known construction loses an $m^{o(1)}$ factor at each level; no technique is known for composing $\log m$ levels with only additive loss.

## 7. Current Research (as of June 2026)

- **ETH Zürich (Kyng group), Stanford (Sidford), Berkeley/CMU (Peng, Sachdeva at UCSD, Probst Gutenberg)** — the group behind the 2022–2024 results — is pushing on *dynamic* and *incremental* versions and on shrinking the $m^{o(1)}$ factor. *(frontier — verify)* Reports of $O(m\log^{O(1)}n)$ for min-cost flow on restricted capacity ranges circulate as preprints; none is peer-reviewed as of mid-2026.
- **Deterministic and adaptive data structures.** The 2023 derandomisation opened the way to composing flow subroutines inside other algorithms without independence assumptions; work continues on deterministic expander decompositions with polylog quality.
- **Strongly polynomial almost-linear flow.** Removing the $\log U$ dependence — an $m^{1+o(1)}$ strongly polynomial min-cost flow — is an explicitly stated open problem of the FOCS 2022 paper.
- **Simplification programmes.** Several groups are producing "textbook" versions of the $\ell_1$-IPM, aiming to replace the heaviest sparsifier machinery with $\ell_1$-oblivious routings.
- **Lower bounds.** Attempts to prove $\omega(m)$ lower bounds in restricted models (combinatorial/oracle models, cut-toggling algorithms) are active but have not reached the general model.

## 8. Future Work

1. Build a dynamic low-stretch spanning tree with polylog stretch and polylog update time against adaptive adversaries — the single highest-value subproblem.
2. Design a barrier for the flow polytope with $\mathrm{polylog}$ iteration complexity, or prove none exists.
3. Extend $m^{1+o(1)}$ to fully dynamic flow (edge insertions *and* deletions) with $m^{o(1)}$ amortised time.
4. Obtain a strongly polynomial $m^{1+o(1)}$ min-cost flow algorithm.
5. Push practical implementations: the current algorithms have constants and $m^{o(1)}$ factors that make them slower than push–relabel on all realistic $m$.
6. Settle whether *exact* max flow is strictly harder than $(1+\varepsilon)$-approximate undirected max flow, which is already $O(m\,\mathrm{polylog})$.

## 9. Key References

- **[Foundational]** L. R. Ford Jr., D. R. Fulkerson. *Maximal Flow Through a Network.* Canadian Journal of Mathematics 8, 399–404, 1956.
- **[Foundational]** J. Edmonds, R. M. Karp. *Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems.* Journal of the ACM 19(2), 248–264, 1972.
- **[Foundational]** A. V. Goldberg, R. E. Tarjan. *A New Approach to the Maximum-Flow Problem.* Journal of the ACM 35(4), 921–940, 1988.
- **[Foundational]** A. V. Goldberg, S. Rao. *Beyond the Flow Decomposition Barrier.* Journal of the ACM 45(5), 783–797, 1998.
- **[SOTA]** L. Chen, R. Kyng, Y. P. Liu, R. Peng, M. Probst Gutenberg, S. Sachdeva. *Maximum Flow and Minimum-Cost Flow in Almost-Linear Time.* FOCS 2022, 612–623. arXiv:2203.00671.
- **[SOTA]** J. van den Brand, L. Chen, R. Kyng, Y. P. Liu, R. Peng, M. Probst Gutenberg, S. Sachdeva, A. Sidford. *A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow.* FOCS 2023.
- **[Recent]** L. Chen, R. Kyng, Y. P. Liu, S. Meierhans, M. Probst Gutenberg. *Almost-Linear Time Algorithms for Incremental Graphs: Minimum-Cost Flow and More.* FOCS 2024.
- **[Recent]** A. Bernstein, D. Nanongkai, C. Wulff-Nilsen. *Negative-Weight Single-Source Shortest Paths in Near-Linear Time.* FOCS 2022.
- **[Recent]** J. van den Brand, Y. T. Lee, Y. P. Liu, T. Saranurak, A. Sidford, Z. Song, D. Wang. *Minimum Cost Flows, MDPs, and $\ell_1$-Regression in Nearly Linear Time for Dense Instances.* STOC 2021.
- **[Prior art]** A. Mądry. *Computing Maximum Flow with Augmenting Electrical Flows.* FOCS 2016, 593–602.
- **[Prior art]** T. Kathuria, Y. P. Liu, A. Sidford. *Unit Capacity Maxflow in Almost $O(m^{4/3})$ Time.* FOCS 2020.
- **[Prior art]** P. Christiano, J. A. Kelner, A. Mądry, D. A. Spielman, S.-H. Teng. *Electrical Flows, Laplacian Systems, and Faster Approximation of Maximum Flow in Undirected Graphs.* STOC 2011, 273–282.
- **[Prior art]** R. Peng. *Approximate Undirected Maximum Flows in $O(m\,\mathrm{polylog}(n))$ Time.* SODA 2016, 1862–1867.
- **[Prior art]** G. Borradaile, P. Klein. *An $O(n\log n)$ Algorithm for Maximum $st$-Flow in a Directed Planar Graph.* Journal of the ACM 56(2), 2009.
- **[Prior art]** J. B. Orlin. *Max Flows in $O(nm)$ Time, or Better.* STOC 2013, 765–774.
- **[Tooling]** D. D. Sleator, R. E. Tarjan. *A Data Structure for Dynamic Trees.* Journal of Computer and System Sciences 26(3), 362–391, 1983.
- **[Survey/Book]** R. K. Ahuja, T. L. Magnanti, J. B. Orlin. *Network Flows: Theory, Algorithms, and Applications.* Prentice Hall, 1993.

## 10. Worked Example / Concrete Special Case

**The diamond instance — why capacity scaling matters.** Take $V=\{s,a,b,t\}$ and
$$u(s\!\to\! a)=u(s\!\to\! b)=u(a\!\to\! t)=u(b\!\to\! t)=C,\qquad u(a\!\to\! b)=1 .$$
Here $m=5$, $n=4$. Max flow is $2C$: send $C$ along $s\to a\to t$ and $C$ along $s\to b\to t$; the min cut $\{s\}$ has capacity $2C$.

*Ford–Fulkerson with adversarial path choice.* Choose $s\to a\to b\to t$ first: it augments by $1$ (bottleneck is the middle edge). The residual now has $b\to a$ with capacity 1; choose $s\to b\to a\to t$, augmenting by $1$ again and restoring $a\to b$. Repeating alternately gives $2C$ augmentations, each of value $1$ — running time $\Theta(mC)=\Theta(m\,2^{\log C})$, exponential in the input bit-length. This is the pseudo-polynomial failure that all later work must avoid; BFS ordering (Edmonds–Karp) fixes *this* instance but not the general $\Theta(mn)$ barrier.

*The min-ratio cycle view.* Start from the feasible flow $f=(C\!-\!1,\,C\!-\!1,\,C\!-\!1,\,C\!-\!1,\,0)$ on edges $(sa,sb,at,bt,ab)$, of value $2C-2$. Add the return arc $t\to s$ of cost $-1$; the gradient of the barrier is dominated by that arc. The undirected cycle $\Delta$ routing one unit along $s\to a\to t\to s$ has $g^{\top}\Delta \approx -1$ and $\lVert L\Delta\rVert_1 = \ell_{sa}+\ell_{at}+\ell_{ts}$; with residual capacities $1$ on $sa,at$ the lengths are $\ell\approx 1$, giving ratio $\approx -1/3$. The cycle through $a\to b$ has residual capacity $1$ but adds a fourth edge, ratio $\approx -1/4$. The IPM picks the better ratio, scales the step by the barrier's safety factor, and converges in $\widetilde O(m)=\widetilde O(5)$ steps *independent of $C$* — only $\log C$ enters, through the required precision. Rounding the final fractional flow to the nearest vertex of the flow polytope yields the integral optimum $2C$.

The example isolates the two live difficulties in miniature: the number of steps is $\widetilde\Theta(m)$, not $\mathrm{polylog}$, and finding the best ratio cycle on a general graph — not on five edges — is what costs $m^{o(1)}$ per step.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*