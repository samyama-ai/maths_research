---
id: 07-combinatorics/firefighting-on-trees
title: "Firefighting on Trees"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Firefighting on Trees

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/firefighting-on-trees` · **Status:** open

## 1. Problem Statement / Conjecture

A fire breaks out at the root $r$ of a finite tree $T$. In each round a defender permanently protects one not-yet-burnt vertex, then the fire spreads from every burnt vertex to all unprotected neighbours. The process stops when the fire cannot spread. The objective is to maximise the number of vertices that never burn.

The open problems clustered under **Firefighting on Trees** are:

1. **Exact complexity of restricted tree classes.** Firefighter is NP-hard on trees of maximum degree $3$; the complete classification of tree classes on which it is polynomial-time solvable (by degree, pathwidth, number of leaves, level-width) is unresolved.
2. **Approximability of RMFC on trees.** For Resource Minimization for Fire Containment (RMFC) — find the smallest budget $b$ of protections per round that contains the fire — the known hardness is a factor $2$ and the known algorithm is an unspecified $O(1)$-factor. Closing this gap is open.
3. **Exact-algorithm barrier.** Firefighter on trees admits a $2^{O(\sqrt{n}\log n)}$-time exact algorithm. Whether the $\sqrt{n}$ exponent is optimal under the Exponential Time Hypothesis (ETH) is open.
4. **Optimal surviving-rate constant for trees.** Every tree has surviving rate $> 1/6$; the extremal constant is unknown.

A resolution of (2) means matching approximation and inapproximability constants for RMFC on trees under $\mathrm{P} \neq \mathrm{NP}$; of (3), an ETH lower bound of $2^{\Omega(\sqrt n)}$ or a $2^{O(n^{1/2-\epsilon})}$ algorithm.

## 2. Mathematical Foundations

Let $T=(V,E)$ be a tree rooted at $r$, $|V|=n$. Write $L_i \subseteq V$ for the set of vertices at distance $i$ from $r$, $L_{\le i} = \bigcup_{j\le i} L_j$, $P_v$ for the vertex set of the $r$–$v$ path excluding $r$, and $T_v$ for the subtree rooted at $v$.

**Reformulation (MacGillivray–Wang).** On a tree, a strategy is fully described by the set $D \subseteq V\setminus\{r\}$ of protected vertices, and $D$ is feasible iff

$$|D \cap L_{\le i}| \le i \quad \forall i \ge 1, \qquad |D \cap P_v| \le 1 \quad \forall v \in V .$$

The first family is the *budget* constraint (a vertex at level $i$ can only be protected in rounds $1,\dots,i$, since the fire reaches $L_i$ at time $i$); the second says $D$ is an antichain in the ancestor order (protecting below an already-protected vertex is wasted). The saved set is $\bigcup_{v\in D} T_v$, so Firefighter on trees is

$$\text{maximise } \sum_{v \in D} |T_v| \quad \text{subject to the two constraint families.}$$

**Natural LP relaxation.** With $w_v = |T_v|$ and $x \in [0,1]^{V\setminus\{r\}}$:

$$\max \sum_v w_v x_v \quad \text{s.t.} \quad \sum_{u \in P_v} x_u \le 1 \ \ \forall v \in \mathcal{L}(T), \qquad \sum_{u \in L_{\le i}} x_u \le i \ \ \forall i, \qquad x \ge 0,$$

where $\mathcal{L}(T)$ is the leaf set. Randomised rounding of this LP gives a $(1-1/e)$-approximation (Cai–Verbin–Yang, 2008). The integrality gap is bounded away from $1$, which is why a PTAS required techniques "beyond integrality gaps".

**RMFC on trees.** Given $T$ of height $h$, find

$$b^\ast(T) = \min\Big\{ b \in \mathbb{Z}_{>0} : \exists D \text{ with } |D \cap L_{\le i}| \le b\,i \ \forall i,\ \ D \text{ hits every } r\text{–leaf path} \Big\}.$$

Containment on a tree is equivalent to $D$ being a *root–leaf cut*, so RMFC is a cut problem with a time-indexed knapsack-type budget.

**Surviving rate.** For $v \in V$ let $\mathrm{sn}(G,v)$ be the number of vertices saved by an optimal strategy when the fire starts at $v$. Then

$$\rho(G) = \frac{1}{n^2}\sum_{v \in V} \mathrm{sn}(G,v),$$

the expected fraction saved for a uniformly random outbreak vertex.

## 3. History & State of the Art (SOTA)

- **1995.** Hartnell introduces the firefighter game at the 25th Manitoba Conference, framing it as a dynamic variant of domination.
- **2000.** Hartnell and Li prove that the greedy strategy — always protect the endangered vertex of largest subtree weight — saves at least $\tfrac12$ of the optimum on trees, and that $\tfrac12$ is asymptotically tight.
- **2003.** MacGillivray and Wang give the integer-programming formulation above and polynomial algorithms for restricted trees.
- **2007.** Finbow, King, MacGillivray and Rizzi prove NP-completeness for trees of maximum degree $3$, and polynomial solvability for graphs of maximum degree $3$ when the fire starts at a degree-$2$ vertex. This is the sharpest known complexity dichotomy by degree.
- **2008.** Cai, Verbin and Yang give the $(1-1/e)$ LP-rounding approximation, an FPT algorithm for "save $\ge k$ vertices", and a $2^{O(\sqrt n \log n)}$ exact algorithm.
- **2010.** Chalermsook and Chuzhoy give an $O(\log^\ast n)$-approximation for RMFC on trees and matching-style hardness results; Anshelevich, Chakrabarty, Hate and Swamy recast firefighting as "cuts over time".
- **2017–2019.** Adjiashvili, Baggio and Zenklusen give a **PTAS** for Firefighter on trees and the first **$O(1)$-approximation** for RMFC on trees, using enumeration of "high-value" levels combined with a strengthened LP. This is the current SOTA.

## 4. Partial Results / Verified Cases

- **Polynomial classes.** Trees in which every vertex has at most one child with a non-trivial subtree (caterpillars and generalisations); trees of bounded *level width* $\max_i |L_i|$; graphs of maximum degree $3$ with outbreak at a degree-$2$ vertex (Finbow–King–MacGillivray–Rizzi, 2007). Interval graphs, permutation graphs and split graphs are NP-hard, so tractability is genuinely tree-specific (Fomin–Heggernes–van Leeuwen, 2016).
- **Hard cases.** NP-complete for trees of max degree $3$; NP-complete for $b \ge 2$ firefighters per round on trees of degree $\le b+3$ (Bazgan–Chopin–Ries, 2013).
- **Approximation.** PTAS for Firefighter on trees: for every $\epsilon>0$ a $(1-\epsilon)$-approximation in time $n^{O(1/\epsilon)}$ (Adjiashvili–Baggio–Zenklusen). $O(1)$-approximation for RMFC on trees; $\Theta(\log^\ast n)$ was the prior bound.
- **Parameterized.** FPT in the number $k$ of saved vertices on trees; no polynomial kernel unless $\mathrm{NP} \subseteq \mathrm{coNP}/\mathrm{poly}$ (Bazgan–Chopin–Cygan–Fellows–Fomin–van Leeuwen, 2014). Structural hardness for pathwidth-type parameters (Chlebíková–Chopin, 2014).
- **Exact.** $2^{O(\sqrt{n}\log n)}$ time, versus the trivial $n^{O(h)}$; the subexponential regime is confirmed only for trees, not general graphs.
- **Surviving rate.** $\rho(T) > 1/6$ for every tree $T$ (Cai–Wang, 2009).

## 5. Principal Obstacles

- **LP integrality gap.** The natural relaxation of §2 has a gap bounded away from $1$, so no rounding of it alone can give a PTAS. The gap is created by instances where the fractional solution spreads budget thinly across many levels while any integral solution must commit early. ABZ circumvent this by enumerating the $O(1/\epsilon)$ levels carrying most of the value, but the enumeration is what forces $n^{O(1/\epsilon)}$ rather than $f(\epsilon)\cdot \mathrm{poly}(n)$ — an EPTAS remains out of reach.
- **Budget constraints are non-laminar in time.** The prefix constraints $|D\cap L_{\le i}|\le i$ couple all levels, so standard dynamic programming over subtrees must carry the entire vector of remaining budgets — a state space of size $n^{\Theta(h)}$. Tree-decomposition machinery does not help: the parameter that matters is height, not width.
- **Cut duality fails.** RMFC is a min-cut problem with a time-staged budget; the "cuts over time" LP has no integral max-flow dual, so combinatorial flow techniques give no matching lower bound.
- **Hardness constructions are coarse.** Existing reductions produce a factor-$2$ threshold for RMFC (distinguishing $b^\ast=1$ from $b^\ast \ge 2$ is NP-hard) but no gap amplification is known, because the tree structure that makes the problem approximable also destroys the recursive self-composition needed for PCP-style amplification.

## 6. The Gap

- **Approximation gap for RMFC on trees:** proven inapproximability factor $2$ versus an algorithm with an unquantified constant $C > 2$. Closing this requires either a $(2+\epsilon)$-approximation or a hardness construction with amplifiable budget levels.
- **Complexity classification gap:** NP-hardness is known at maximum degree $3$ and polynomiality at maximum degree $3$ with a degree-$2$ outbreak vertex. No parameter is known that separates these two regimes structurally.
- **Exact-algorithm gap:** $2^{O(\sqrt n \log n)}$ upper bound versus only a $2^{\Omega(\text{poly}\log n)}$-style ETH lower bound; the $\log n$ factor and the $\sqrt n$ exponent are both unmatched.
- **Surviving rate gap:** proven $\rho(T) > 1/6$ versus no known tree family attaining a value near $1/6$; the true extremal constant lies somewhere in $(1/6, 1)$.

## 7. Current Research (as of June 2026)

- **Zenklusen's group (ETH Zürich)** continues the LP-strengthening programme behind the tree PTAS, aiming at an EPTAS and at pinning the RMFC constant. *(frontier — verify)*
- **Parameterized-complexity groups (Bergen, Warsaw, Paris-Dauphine)** work on kernelization barriers and on parameters interpolating between height and level width.
- **Temporal-graph and epidemic-control communities** reuse the tree formulation as the core subproblem for vaccination and containment models on networks with spreading dynamics; several recent preprints study firefighting on random recursive trees and on Galton–Watson trees, where the interest is the survival threshold as a function of the offspring distribution. *(frontier — verify)*
- **Infinite-tree variants** (containment on the infinite $d$-ary tree with $b$ firefighters per round) are studied for their connection to branching processes and percolation.

## 8. Future Work

- Convert the ABZ level-enumeration into a *sparsification* argument to obtain an EPTAS with running time $f(\epsilon)\cdot n^{O(1)}$.
- Design a gap-amplification gadget for RMFC on trees: composing height-$h$ instances multiplicatively, the way set-cover instances compose, would push the factor-$2$ hardness towards the algorithmic constant.
- Prove an ETH-based $2^{\Omega(\sqrt n)}$ lower bound; the natural route is a planar-style reduction preserving the $\sqrt n$ separator behaviour of the level structure.
- Settle the extremal surviving-rate constant for trees, and determine whether the extremal family is a complete binary tree or a spider.
- Extend the tree PTAS to bounded-treewidth graphs, where even a constant-factor approximation is currently unknown.

## 9. Key References

- **[Foundational]** B. L. Hartnell. *Firefighter! An application of domination.* 25th Manitoba Conference on Combinatorial Mathematics and Computing, University of Manitoba, 1995.
- **[Foundational]** B. L. Hartnell, Q. Li. *Firefighting on trees: how bad is the greedy algorithm?* Congressus Numerantium 145 (2000), 187–192.
- **[Foundational]** G. MacGillivray, P. Wang. *On the firefighter problem.* Journal of Combinatorial Mathematics and Combinatorial Computing 47 (2003), 83–96.
- **[Complexity]** S. Finbow, A. King, G. MacGillivray, R. Rizzi. *The firefighter problem for graphs of maximum degree three.* Discrete Mathematics 307 (2007), 2094–2105.
- **[Approximation]** L. Cai, E. Verbin, L. Yang. *Firefighting on trees: $(1-1/e)$-approximation, fixed parameter tractability and a subexponential algorithm.* ISAAC 2008, LNCS 5369, 258–269.
- **[SOTA]** D. Adjiashvili, A. Baggio, R. Zenklusen. *Firefighting on trees beyond integrality gaps.* ACM Transactions on Algorithms 15(2), 2019 (preliminary version: SODA 2017).
- **[SOTA]** P. Chalermsook, J. Chuzhoy. *Resource minimization for fire containment.* SODA 2010, 1334–1349.
- **[Related]** E. Anshelevich, D. Chakrabarty, A. Hate, C. Swamy. *Approximability of the firefighter problem: computing cuts over time.* Algorithmica 62 (2012), 520–536.
- **[Parameterized]** C. Bazgan, M. Chopin, M. Cygan, M. R. Fellows, F. V. Fomin, E. J. van Leeuwen. *Parameterized complexity of firefighting.* Journal of Computer and System Sciences 80 (2014), 1285–1297.
- **[Related]** C. Bazgan, M. Chopin, B. Ries. *The firefighter problem with more than one firefighter on trees.* Discrete Applied Mathematics 161 (2013), 899–908.
- **[Related]** L. Cai, W. Wang. *The surviving rate of a graph for the firefighter problem.* SIAM Journal on Discrete Mathematics 23 (2009), 1814–1826.
- **[Related]** F. V. Fomin, P. Heggernes, E. J. van Leeuwen. *The firefighter problem on graph classes.* Theoretical Computer Science 613 (2016), 38–50.
- **[Survey]** S. Finbow, G. MacGillivray. *The firefighter problem: a survey of results, directions and questions.* Australasian Journal of Combinatorics 43 (2009), 57–77.

## 10. Worked Example / Concrete Special Case

**Greedy is not optimal.** Build a tree $T$ on $n=16$ vertices, rooted at $r$ (the outbreak vertex):

- $r$ has children $u$ and $v$;
- $u$ has two leaf children $u_1,u_2$ — so $|T_u| = 3$;
- $v$ has one child $w$; $w$ has ten leaf children $w_1,\dots,w_{10}$ — so $|T_v| = 12$, $|T_w| = 11$.

*Greedy (largest endangered subtree first).* Round 1: the endangered vertices are $u$ and $v$; greedy protects $v$, saving $T_v$ (12 vertices). The fire spreads to $u$. Round 2: the endangered vertices are $u_1,u_2$; protecting either saves 1. Fire burns the other. Burnt: $r,u$, and one leaf — 3 vertices. **Saved: 13.**

*Optimal.* Round 1: protect $u$, saving only $3$ vertices now; fire spreads to $v$. Round 2: $w$ is endangered and still unburnt, so protect $w$, saving $|T_w| = 11$. Burnt: $r,v$ — 2 vertices. **Saved: 14.**

Check with the §2 reformulation: $D_{\text{greedy}} = \{v, u_1\}$ has $|D \cap L_{\le 1}| = 1 \le 1$, $|D \cap L_{\le 2}| = 2 \le 2$, and is an antichain; value $12+1 = 13$. $D_{\text{opt}} = \{u, w\}$ satisfies the same constraints with value $3+11 = 14$. So $\mathrm{greedy}/\mathrm{opt} = 13/14$.

Iterating this gadget — replacing each deep leaf block by a scaled copy — drives the ratio to $1/2$, which is exactly the Hartnell–Li bound. The LP of §2 assigns $x_u = x_v = 1/2$ in round 1 and fractionally hedges, obtaining value strictly above $14$; the loss on rounding is the elementary form of the integrality gap that the ABZ PTAS had to work around.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*