---
id: 07-combinatorics/loebl-komlos-szemeredi-conjecture
title: "Loebl-Komlós-Szemerédi Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Loebl-Komlós-Szemerédi Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/loebl-komlos-szemeredi-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Loebl–Komlós–Szemerédi, LKS).** Let $k \in \mathbb{N}$ and let $G$ be a graph on $n$ vertices. If at least $n/2$ vertices of $G$ have degree at least $k$, then $G$ contains every tree with $k$ edges as a subgraph.

The containment is as a (not necessarily induced, not necessarily spanning) subgraph: there is an injective map $\varphi: V(T) \to V(G)$ with $\varphi(u)\varphi(v) \in E(G)$ for every $uv \in E(T)$.

A complete resolution means: a proof valid for **all** $k \ge 1$ and all $n$, or a single counterexample — a graph $G$ with $|\{v : \deg_G(v) \ge k\}| \ge n/2$ and a tree $T$ with $e(T) = k$ such that $T \not\subseteq G$.

Two weakenings are standard and are the objects most theorems address:

- **Approximate LKS ($\alpha$-version).** For each $\alpha > 0$ there is $k_0$ such that for $k > k_0$: if at least $(\tfrac12 + \alpha)n$ vertices of $G$ have degree at least $(1+\alpha)k$, then every tree with $k$ edges embeds in $G$.
- **Loebl's original "$n/2$–$n/2$–$n/2$" conjecture.** The case $k = n/2$: if at least $n/2$ vertices have degree at least $n/2$, then $G$ contains every tree with at most $n/2$ edges.

**Status note.** The approximate version is a theorem (Hladký–Komlós–Piguet–Simonovits–Stein–Szemerédi, 2017), and the exact statement is a theorem for several large families (dense graphs, $k = n/2$ with $n$ large, bounded-degree trees). The exact conjecture in full generality — in particular for $k = o(n)$ with no assumption on $\Delta(T)$ — remains open.

## 2. Mathematical Foundations

Write $\deg_G(v)$ for the degree of $v$, and define the set of *large-degree* vertices
$$\mathfrak{L}_k(G) \;=\; \{\, v \in V(G) \;:\; \deg_G(v) \ge k \,\}.$$
Call $G$ an **LKS graph** for parameter $k$ if $|\mathfrak{L}_k(G)| \ge n/2$, and let
$$\mathcal{T}_k \;=\; \{\, T : T \text{ a tree}, \; e(T) = k, \; |V(T)| = k+1 \,\}.$$
LKS asserts $\mathcal{T}_k \subseteq \{\text{subgraphs of } G\}$ for every LKS graph $G$.

Both numerical parameters are best possible.

- **Degree $k$ cannot be lowered.** Let $G$ be a disjoint union of copies of $K_k$. Every vertex has degree $k-1$, and no component has $k+1$ vertices, so no $T \in \mathcal{T}_k$ embeds.
- **The fraction $1/2$ cannot be lowered.** Let $n$ be even, $k = n-1$, and
$$G \;=\; K_{n/2-1} \;\vee\; \overline{K_{n/2+1}}$$
(a clique of size $n/2-1$ joined completely to an independent set of size $n/2+1$). Clique vertices have degree $n-1 \ge k$, so $|\mathfrak{L}_k(G)| = n/2 - 1$, one short of the threshold. The independent set has size $n/2+1 > \tfrac12 n$, and a Hamilton path $P_n \in \mathcal{T}_{n-1}$ would need its $\lceil n/2 \rceil$ independent-side vertices separated by distinct clique vertices — impossible. So $P_n \not\subseteq G$.

Two extremal configurations drive the difficulty: the **clique-like** obstruction ($K_{k+1}$, in which every $T \in \mathcal{T}_k$ sits trivially) and the **bipartite-like** obstruction ($K_{k/2,\,m}$, which contains all trees whose smaller colour class fits in the small side). A proof must handle graphs that are locally a mixture of the two.

Standard machinery:

- **Szemerédi Regularity Lemma.** For $\varepsilon>0$, $M_0$, there is $M$ so that every graph admits an $\varepsilon$-regular partition $V = V_0 \cup V_1 \cup \dots \cup V_m$ with $M_0 \le m \le M$, where a pair $(V_i,V_j)$ is $\varepsilon$-regular if $|d(A,B)-d(V_i,V_j)| < \varepsilon$ for all $A \subseteq V_i, B \subseteq V_j$ with $|A| \ge \varepsilon|V_i|$, $|B|\ge \varepsilon|V_j|$.
- **Blow-up Lemma** (Komlós–Sárközy–Szemerédi, 1997): super-regular pairs behave like complete bipartite graphs for embedding bounded-degree spanning subgraphs.
- **Tree structure.** Every $T$ with $k$ edges has a *centroid* vertex $c$ whose removal leaves components of order $\le (k+1)/2$; and $T$ is bipartite, $V(T) = A \cup B$, so any embedding respects a two-colouring. A **matching-and-shadow** decomposition of $T$ into a matching plus its neighbourhood is the basic unit used in embeddings.
- Related: the **Erdős–Sós conjecture** — $e(G) > \tfrac12(k-1)n$ implies $T \subseteq G$ for all $T \in \mathcal{T}_k$ — which LKS does not imply and which does not imply LKS.

## 3. History & State of the Art (SOTA)

- **1995.** Martin Loebl's "$n/2$–$n/2$–$n/2$" conjecture is recorded in Erdős, Füredi, Loebl and Sós, *Discrepancy of trees*, where it arises from a question on tree discrepancy and Ramsey-type numbers for trees. Komlós and Szemerédi propose the general $k$ version.
- **1995.** Ajtai, Komlós and Szemerédi, *On a conjecture of Loebl*, prove the approximate form of Loebl's original case: $(\tfrac12+\alpha)n$ vertices of degree $\ge (\tfrac12+\alpha)n$ suffice for all trees with $\le n/2$ edges, $n$ large.
- **2008.** Piguet and Stein settle LKS exactly for trees of diameter at most $5$.
- **2009.** Cooley proves LKS exactly for large dense graphs: for $q>0$ there is $n_0$ with the conjecture true whenever $n \ge n_0$ and $k \ge qn$.
- **2011.** Zhao proves Loebl's original $n/2$–$n/2$–$n/2$ conjecture exactly for all sufficiently large $n$.
- **2012.** Piguet and Stein prove the approximate LKS conjecture for trees of bounded degree, using regularity plus the blow-up lemma.
- **2017.** Hladký, Komlós, Piguet, Simonovits, Stein and Szemerédi publish *The approximate Loebl–Komlós–Szemerédi conjecture I–IV* (SIAM J. Discrete Math. 31), a ~400-page series proving approximate LKS in full: no degree bound on $T$, no density assumption on $G$. The engine is a **sparse decomposition** of $G$ into regular pairs, expanders, and a "dense spots"/avoiding-set structure that works below the regularity threshold.

SOTA in one line: approximate LKS is done for large $k$; exact LKS is done for $k = \Theta(n)$ and for $k=n/2$; exact LKS for sparse $k$ is open.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $k \le 4$, small $k$ | Exact, by direct case analysis on the finitely many $T \in \mathcal{T}_k$ | folklore |
| $\operatorname{diam}(T) \le 5$ | Exact, all $k$, all $n$ | Piguet–Stein 2008 |
| $T = K_{1,k}$ (stars) | Trivial: some vertex has degree $\ge k$ | — |
| $T = P_{k+1}$ (paths) | Follows from Erdős–Gallai: $e(G) > \tfrac12(k-1)n \Rightarrow P_{k+1} \subseteq G$; LKS hypothesis gives $e(G) \ge \tfrac{kn}{4}$ per component analysis | Erdős–Gallai 1959 |
| $k \ge qn$, $n \ge n_0(q)$ | Exact | Cooley 2009 |
| $k = n/2$, $n$ large | Exact (Loebl's conjecture) | Zhao 2011 |
| $\Delta(T) \le D$, $k$ large | Approximate version | Piguet–Stein 2012 |
| All $T \in \mathcal{T}_k$, $k \ge k_0(\alpha)$ | Approximate version, $(\tfrac12+\alpha)n$ vertices of degree $(1+\alpha)k$ | HKPSSS 2017 (I–IV) |

Computationally, LKS has been checked exhaustively for all graphs on $n \le 10$ vertices and all $k \le 6$ by brute-force subgraph search; no counterexample is known for any $(G,T)$ pair ever tested. *(frontier — verify: no single published paper is the canonical source for these exhaustive checks.)*

## 5. Principal Obstacles

- **Regularity is useless when $k = o(n)$.** The regularity method gives density information only at scale $\Omega(n^2)$ edges. An LKS graph with $k$ constant has $O(n)$ edges; every regular pair has density $0$. The 2017 series had to build a *sparse decomposition* — separating $G$ into dense spots, an expanding part, and a "$\gamma$-avoiding" remainder — precisely because the standard tool vanishes.
- **Trees of unbounded degree break the blow-up lemma.** The blow-up lemma requires $\Delta(T) = O(1)$; a tree with a vertex of degree $\Theta(k)$ must be embedded into a *single* high-degree vertex of $G$, and the choice of that vertex is globally constrained. Bounded-degree LKS (Piguet–Stein 2012) is far easier for this reason.
- **Two incompatible extremal families.** Near-extremal LKS graphs are close to either disjoint $K_{k+1}$'s or unbalanced complete bipartite graphs. Stability arguments must classify all near-extremal structures; the intermediate regime (graphs that are dense in one part and sparse-expanding in another) has no clean description, and the "rough structure / finer structure" halves of the 2017 series exist only to enumerate it.
- **Approximate-to-exact loss.** Every regularity- or expander-based embedding loses a constant fraction of the host: an $\varepsilon$-fraction of vertices lands in the exceptional class $V_0$. Removing the $\alpha$ slack in *both* the count $(\tfrac12+\alpha)n$ and the degree $(1+\alpha)k$ requires an absorption or stability step that currently has no sparse analogue.
- **No LP/entropy relaxation.** Unlike Turán-type problems, tree containment is not captured by a flag-algebra or entropy-counting certificate: the conclusion is existential over $|\mathcal{T}_k| \sim k^{-5/2}\,2.9558^k$ non-isomorphic trees, all of which must embed simultaneously.

## 6. The Gap

Proven: for every $\alpha > 0$ there is $k_0(\alpha)$ such that $(\tfrac12+\alpha)n$ vertices of degree $\ge (1+\alpha)k$ force all of $\mathcal{T}_k$ when $k > k_0$.

Conjectured: $\alpha = 0$ and $k_0 = 1$.

Precisely two steps are missing.

1. **Kill the $\alpha$'s.** Convert the approximate theorem into the exact one for large $k$. This is a stability problem: assume $G$ is an LKS graph missing some $T \in \mathcal{T}_k$, deduce $G$ is $\alpha$-close to one of the two extremal configurations of Section 2, then embed by hand in each. Cooley's and Zhao's proofs do exactly this in the dense regime, where regularity supplies the closeness; the sparse regime has no such supply.
2. **Kill $k_0$.** Handle all small $k$ uniformly. Every existing proof is asymptotic, so even a full stability argument leaves an ineffective — and in the 2017 series astronomically large — threshold $k_0(\alpha)$ untouched. No finite-check reduction is known.

## 7. Current Research (as of June 2026)

- **The Chilean school (Maya Stein, Universidad de Chile, CMM).** Systematic study of degree conditions for tree embedding: minimum/maximum-degree variants (Besomi–Pavez-Signé–Stein), the Erdős–Sós conjecture for bounded-degree trees, and spanning-tree analogues with Reed. The declared goal is a unified "degree condition ⟹ tree containment" framework of which LKS and Erdős–Sós are instances.
- **Prague / Czech Academy of Sciences (Hladký, Piguet).** Continuation of the sparse-decomposition programme, with graph limits (graphons and their sparse counterparts) as the intended replacement for regularity in the $k = o(n)$ range. *(frontier — verify: an exact LKS theorem for large $k$ has been announced in talks by members of the 2017 team but no complete manuscript is public.)*
- **Erdős–Sós interface.** Ajtai, Komlós, Simonovits and Szemerédi have long announced a proof of the Erdős–Sós conjecture for large $k$; a published version would supply techniques directly transferable to exact LKS. *(frontier — verify: still unpublished as of this review.)*
- **Randomised/absorption approaches.** Absorption methods that resolved many spanning-structure problems (Hamiltonicity, $F$-factors) are being tested on tree containment; the obstacle is that LKS is non-spanning and its host has no expansion guarantee.

## 8. Future Work

- Prove **exact LKS for $k \ge k_0$** by adding a stability layer to the 2017 sparse decomposition; this is the consensus next target.
- Develop a **sparse regularity/limit theory** valid at $O(n)$ edges without bounded-degree or locality assumptions, so that the $k = o(n)$ case gets a tool comparable to Szemerédi's lemma.
- Find a **counting or algebraic certificate** for tree containment that avoids case analysis over $\mathcal{T}_k$ — for instance, a single "universal" tree-like structure whose presence implies all of $\mathcal{T}_k$.
- Settle the **bounded-diameter hierarchy**: exact LKS is known for $\operatorname{diam}(T)\le 5$; diameter $6$ and $7$ are the natural next test cases and are believed tractable.
- Establish **effective bounds**: any proof with explicit $k_0$ would open the door to a computer-assisted finish for small $k$.

## 9. Key References

- **[Foundational]** P. Erdős, Z. Füredi, M. Loebl, V. T. Sós. *Discrepancy of trees.* Studia Scientiarum Mathematicarum Hungarica, 30 (1995), 47–57.
- **[Foundational]** M. Ajtai, J. Komlós, E. Szemerédi. *On a conjecture of Loebl.* In: Graph Theory, Combinatorics, and Algorithms, Vol. 1–2 (Kalamazoo, MI, 1992), Wiley, 1995, pp. 1135–1146.
- **[Foundational]** P. Erdős, T. Gallai. *On maximal paths and circuits of graphs.* Acta Mathematica Academiae Scientiarum Hungaricae, 10 (1959), 337–356.
- **[Technique]** J. Komlós, G. N. Sárközy, E. Szemerédi. *Blow-up lemma.* Combinatorica, 17 (1997), 109–123.
- **[Partial]** D. Piguet, M. J. Stein. *Loebl–Komlós–Szemerédi conjecture for trees of diameter 5.* Electronic Journal of Combinatorics, 15 (2008), #R106.
- **[Partial]** O. Cooley. *Proof of the Loebl–Komlós–Szemerédi conjecture for large, dense graphs.* Discrete Mathematics, 309 (2009), 6190–6228.
- **[Partial]** Y. Zhao. *Proof of the $(n/2 - n/2 - n/2)$ conjecture for large $n$.* Electronic Journal of Combinatorics, 18 (2011), #P27.
- **[Partial]** D. Piguet, M. J. Stein. *An approximate version of the Loebl–Komlós–Szemerédi conjecture for trees of bounded degree.* Journal of Combinatorial Theory Series B, 102 (2012), 102–125.
- **[SOTA]** J. Hladký, J. Komlós, D. Piguet, M. Simonovits, M. J. Stein, E. Szemerédi. *The approximate Loebl–Komlós–Szemerédi conjecture I: The sparse decomposition.* SIAM Journal on Discrete Mathematics, 31 (2017), 945–982. (Parts II, III, IV in the same volume: 983–1016; 1017–1071; 1072–1148.)
- **[Announcement]** J. Hladký, D. Piguet, M. Simonovits, M. J. Stein, E. Szemerédi. *The approximate Loebl–Komlós–Szemerédi conjecture and the bandwidth theorem.* Electronic Notes in Discrete Mathematics, 34 (2009), 175–179.
- **[Related]** J. Besomi, M. Pavez-Signé, M. Stein. *Maximum and minimum degree conditions for embedding trees.* SIAM Journal on Discrete Mathematics, 33 (2019), 1521–1555.
- **[Survey]** M. Stein. *Tree containment and degree conditions.* In: Discrete Mathematics and Applications (Springer Optimization and Its Applications, vol. 165), Springer, 2020, pp. 459–486.

## 10. Worked Example / Concrete Special Case

**Claim.** LKS holds for $k = 3$: if at least $n/2$ vertices of $G$ have degree $\ge 3$, then $G$ contains every tree with $3$ edges.

$\mathcal{T}_3$ has exactly two members: the star $K_{1,3}$ and the path $P_4$.

*Star.* The hypothesis gives at least $n/2 \ge 1$ vertex of degree $\ge 3$ (for $n\ge 1$; if $n = 0$ there is nothing to prove). Any such vertex plus three neighbours is a copy of $K_{1,3}$. ∎

*Path.* Suppose $P_4 \not\subseteq G$. A connected graph containing no path on four vertices is a triangle or a star $K_{1,m}$ ($m \ge 0$): if it had two adjacent vertices each with a private neighbour, those four vertices would give $P_4$; a cycle of length $\ge 4$ contains $P_4$ directly.

Count $|\mathfrak{L}_3(G)|$ component by component. Let $C$ be a component of order $n_C$.

- $C$ a triangle: all degrees are $2 < 3$, contributing $0$ high-degree vertices out of $n_C = 3$.
- $C = K_{1,m}$ with $m \le 2$: max degree $\le 2$, contributing $0$.
- $C = K_{1,m}$ with $m \ge 3$: only the centre has degree $\ge 3$, contributing $1$ out of $n_C = m+1 \ge 4$.

So in every case the component contributes at most $n_C/4$ high-degree vertices, and summing,
$$|\mathfrak{L}_3(G)| \;\le\; \frac{n}{4} \;<\; \frac{n}{2},$$
contradicting the hypothesis (for $n > 0$). Hence $P_4 \subseteq G$. ∎

**Sharpness at $k=3$.** Let $G$ be the disjoint union of $m$ copies of $K_{1,3}$, so $n = 4m$. Exactly the $m$ centres have degree $3$, i.e. $|\mathfrak{L}_3(G)| = n/4$, and $G$ contains no $P_4$. The bound $n/4$ obtained in the proof is therefore attained, and the hypothesis cannot be weakened from $n/2$ to $n/4$.

This $k=3$ argument is a finite case check. The whole difficulty of LKS is that $|\mathcal{T}_k|$ grows like $c\,k^{-5/2}(2.9558\ldots)^k$ and the $P_4$-free classification has no analogue for general $k$ — the structure of $T$-free graphs for a *single* large tree $T$ is itself unknown.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*