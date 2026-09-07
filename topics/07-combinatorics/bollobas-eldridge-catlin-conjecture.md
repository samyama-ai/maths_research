---
id: 07-combinatorics/bollobas-eldridge-catlin-conjecture
title: "Bollobás-Eldridge-Catlin Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bollobás-Eldridge-Catlin Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bollobas-eldridge-catlin-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Two graphs $G_1, G_2$ on the same vertex set $V$ with $|V| = n$ **pack** if they can be placed edge-disjointly in $K_n$: there is a bijection $\sigma: V(G_1) \to V(G_2)$ with $\sigma(E(G_1)) \cap E(G_2) = \emptyset$.

**Conjecture (Bollobás–Eldridge 1978; Catlin 1974).** Let $G_1, G_2$ be graphs on $n$ vertices with maximum degrees $\Delta_1 = \Delta(G_1)$, $\Delta_2 = \Delta(G_2)$. If
$$(\Delta_1 + 1)(\Delta_2 + 1) \le n + 1,$$
then $G_1$ and $G_2$ pack.

A complete proof must produce such a $\sigma$ for every admissible pair; a disproof needs one pair satisfying the degree inequality with no packing. The bound is sharp: $n+1$ cannot be replaced by $n+2$.

**Status note.** The conjecture is settled for $\Delta_1 \le 3$ (the last case for large $n$), for bipartite host structures, and for $d$-degenerate graphs of large maximum degree. The `solved-recently` label tracks a claimed asymptotic resolution for all $\Delta$ and all sufficiently large $n$ circulating in preprint form; it is **not** confirmed in the journal literature of record, and the general statement should still be treated as open by default. See §7.

## 2. Mathematical Foundations

Let $G$ be simple, $V(G)$ its vertex set, $\delta(G)$ its minimum degree, $\overline{G}$ its complement.

**Packing–embedding duality.** $G_1$ and $G_2$ pack on $n$ vertices $\iff$ $G_1 \subseteq \overline{G_2}$ up to relabelling. Setting $H = G_1$, $G = \overline{G_2}$, and using $\delta(G) = n - 1 - \Delta_2$, the conjecture becomes an **embedding / spanning-subgraph** statement:

> If $\Delta(H) = \Delta$, $|V(H)| = |V(G)| = n$, and
> $$\delta(G) \;\ge\; n - \frac{n+1}{\Delta+1},$$
> then $H \subseteq G$.

**Counting heuristic.** $e(G_1) \le n\Delta_1/2$, $e(G_2) \le n\Delta_2/2$, so $e(G_1)+e(G_2) \le \binom{n}{2}$ already fails to be implied by the hypothesis for large $\Delta_i$; the obstruction is structural, not merely a count.

**Sharpness.** Take $H = \frac{n}{\Delta+1} K_{\Delta+1}$ (a clique factor). Then $H \subseteq G$ is exactly a $K_{\Delta+1}$-factor, and the **Hajnal–Szemerédi theorem** (1970) says $\delta(G) \ge \left(1 - \frac{1}{k}\right)n$ forces a $K_k$-factor when $k \mid n$, with extremal examples showing $\delta = \left(1-\frac1k\right)n - 1$ can fail. Translating back, $(\Delta_1+1)(\Delta_2+1) \le n$ suffices in this case. The conjecture asserts the extra unit of slack, $n+1$, holds for *all* $H$ of maximum degree $\Delta$ — so BEC is a strict strengthening of Hajnal–Szemerédi.

**Baseline theorem (Sauer–Spencer 1978).** If
$$2\,\Delta_1 \Delta_2 < n,$$
then $G_1$ and $G_2$ pack. This is weaker than BEC roughly by a factor of $2$ in $\Delta_1\Delta_2$ and is proved by a short "move the worst vertex" exchange argument on bijections minimising the number of conflicting edges.

**Degeneracy.** $G$ is $d$-degenerate if every subgraph has a vertex of degree $\le d$; trees are $1$-degenerate, planar graphs $5$-degenerate. Degeneracy allows greedy embedding orders unavailable for general bounded-degree graphs.

## 3. History & State of the Art (SOTA)

- **1974–76.** P. A. Catlin, in *Subgraph isomorphisms, transversals and embeddings* (JCTB, 1974) and his 1976 Ohio State thesis, formulated the degree condition while strengthening Hajnal–Szemerédi-type colouring/embedding results.
- **1978.** B. Bollobás and S. E. Eldridge, *Packings of graphs and applications to computational complexity* (JCTB), stated the conjecture in its packing form, proved the case $\min\{\Delta_1,\Delta_2\} \le 1$, and gave the sharpness examples ruling out $n+2$.
- **1978.** N. Sauer and J. Spencer, *Edge disjoint placement of graphs* (JCTB), proved the $2\Delta_1\Delta_2 < n$ criterion, the workhorse bound for three decades.
- **1993.** M. Aigner and S. Brandt settled $\Delta_1 = 2$ exactly: every $H$ with $\Delta(H) \le 2$ embeds in any $G$ with $\delta(G) \ge \frac{2n-1}{3}$.
- **1996.** N. Alon and E. Fischer gave an approximate $\Delta = 2$ result via the regularity lemma (*2-factors in dense graphs*), introducing regularity/blow-up machinery into the problem.
- **2003.** B. Csaba, A. Shokoufandeh and E. Szemerédi proved the case $\Delta_1 = 3$ for all sufficiently large $n$ (Combinatorica), by regularity + blow-up + extremal-case analysis.
- **2005–08.** Bollobás, Kostochka and Nakprasit proved BEC for $d$-degenerate $G_1$ whose maximum degree is large relative to $d$; Kaul and Kostochka characterised the extremal pairs for Sauer–Spencer, and subsequent work of Kaul–Kostochka–Yu pushed the packing threshold above $\Delta_1\Delta_2 < n/2$ under structural side conditions.
- **2007.** Csaba proved the conjecture for bipartite $G_1$ (CPC).

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\min\{\Delta_1,\Delta_2\} \le 1$ | Full conjecture; reduces to a (near-)perfect matching in $\overline{G_2}$ | Bollobás–Eldridge 1978 |
| $\Delta_1 = 2$, all $n$ | Full conjecture: $\delta(G) \ge \frac{2n-1}{3} \Rightarrow H \subseteq G$ | Aigner–Brandt 1993 |
| $\Delta_1 = 2$, $n$ large, $o(n)$ error | Approximate version by regularity | Alon–Fischer 1996 |
| $\Delta_1 = 3$, $n \ge n_0$ | Full conjecture | Csaba–Shokoufandeh–Szemerédi 2003 |
| $G_1$ bipartite | Full conjecture | Csaba 2007 |
| $G_1$ $d$-degenerate, $\Delta_1$ large vs. $d$ | Full conjecture | Bollobás–Kostochka–Nakprasit 2005/2008 |
| $H = K_{\Delta+1}$-factor, $(\Delta+1)\mid n$ | Follows from $\delta(G) \ge (1-\frac{1}{\Delta+1})n$ | Hajnal–Szemerédi 1970 |
| All $\Delta_1,\Delta_2$ with $2\Delta_1\Delta_2 < n$ | Weaker packing bound | Sauer–Spencer 1978 |
| Small $n$ (exhaustive search) | Verified computationally for $n \le 11$–$12$ over all pairs meeting the bound | folklore / independent checks |

## 5. Principal Obstacles

- **The window is one unit wide.** Between the Hajnal–Szemerédi-implied threshold $(\Delta_1+1)(\Delta_2+1) \le n$ and BEC's $\le n+1$ there is no room for error terms. Every regularity-based method loses $\varepsilon n$ in the minimum degree and therefore cannot reach an exactly tight bound without a separate extremal analysis.
- **Sauer–Spencer exchange arguments saturate.** Minimising conflicting edges over bijections improves while a "bad" vertex exists, but the potential function stalls exactly at $2\Delta_1\Delta_2 \approx n$; the deficit is a factor of $2$, not an $\varepsilon$.
- **No degeneracy to exploit.** Bounded maximum degree does not bound degeneracy usefully: $H$ may be a disjoint union of $K_{\Delta+1}$'s, forcing a factor-type argument, or an expander, forcing a spread/absorption argument. No single embedding order handles both.
- **Extremal configurations proliferate with $\Delta$.** For $\Delta = 3$ the extremal cases (near-clique-factors, near-bipartite hosts) were enumerable by hand; the number of near-extremal structures grows with $\Delta$, and the stability analysis has not been made uniform in $\Delta$.
- **$\Delta$ growing with $n$.** For $\Delta_1 \asymp \sqrt{n}$ both graphs are dense in the relevant sense; regularity gives no leverage on $H$, and randomised/absorption embeddings need spread hypotheses that clique factors violate.

## 6. The Gap

Proven: $\Delta_1 \le 3$ (with $n$ large for $\Delta_1 = 3$); $G_1$ bipartite; $G_1$ degenerate with large $\Delta_1$; and the whole range $2\Delta_1\Delta_2 < n$.

Missing: the regime $\Delta_1 \ge 4$ with
$$\tfrac{n}{2} \;\lesssim\; \Delta_1\Delta_2 \;\le\; \tfrac{n+1}{\Delta_1\Delta_2^{-1}} \quad\text{more precisely}\quad n \ge 2\Delta_1\Delta_2 \ \text{fails but}\ (\Delta_1+1)(\Delta_2+1) \le n+1 \ \text{holds},$$
i.e. roughly a factor-$2$ band in $\Delta_1\Delta_2$, uniformly in $\Delta_1$ and including $\Delta_1$ growing with $n$. The concrete step needed: a stability theorem saying that a pair $(G_1, G_2)$ meeting the degree bound but admitting no packing must be within $o(n)$ edits of one of a bounded list of extremal configurations, **with the list and the error term uniform in $\Delta$**. All existing proofs fix $\Delta$ before choosing $n_0$.

## 7. Current Research (as of June 2026)

- **Claimed asymptotic resolution.** Preprints asserting BEC for all $\Delta$ and all $n \ge n_0(\Delta)$, combining absorption with regularity-free iterative embedding, have circulated since the mid-2020s; none has completed journal refereeing. *(frontier — verify)*
- **Absorption for spanning bounded-degree subgraphs.** The Montgomery-style absorber and spread-measure/Kahn–Kalai-adjacent techniques developed for spanning trees and $F$-factors are being adapted; the difficulty is that clique-factor targets are not spread. *(frontier — verify)*
- **Removing largeness from $\Delta_1 = 3$.** Making the Csaba–Shokoufandeh–Szemerédi proof effective, i.e. an explicit $n_0$ or a regularity-free argument.
- **Ore-type and list variants.** Kierstead–Kostochka's Ore-type Hajnal–Szemerédi theorem suggests a degree-sum analogue $d(u)+d(v)$ replacing $\Delta$; the correct BEC analogue is open.
- **Groups.** Combinatorics groups at Illinois (Kostochka school), Szeged/Budapest (Szemerédi school, Csaba), Illinois Tech (Kaul), and Birmingham/Oxford extremal-graph groups are the main contributors.

## 8. Future Work

- Prove a $\Delta$-uniform stability theorem: no-packing pairs near the threshold are near clique-factor or near-bipartite configurations.
- Settle $\Delta_1 = 4$ unconditionally — the smallest case where the extremal list is not fully classified.
- Establish BEC for $\Delta_1 = \Theta(n^{\alpha})$, $0 < \alpha < 1/2$, where neither regularity nor greedy methods apply.
- Prove the natural list/rainbow strengthening: packing $k \ge 3$ graphs with $\prod_i (\Delta_i + 1) \le n + 1$-type conditions (largely open even for $k = 3$).
- Develop an algorithmic version: is the packing, when it exists under the BEC bound, findable in polynomial time?

## 9. Key References

- **[Foundational]** B. Bollobás, S. E. Eldridge. *Packings of graphs and applications to computational complexity.* Journal of Combinatorial Theory, Series B **25** (1978), 105–124.
- **[Foundational]** P. A. Catlin. *Subgraph isomorphisms, transversals and embeddings.* Journal of Combinatorial Theory, Series B **17** (1974), 251–265.
- **[Foundational]** N. Sauer, J. Spencer. *Edge disjoint placement of graphs.* Journal of Combinatorial Theory, Series B **25** (1978), 295–302.
- **[Foundational]** A. Hajnal, E. Szemerédi. *Proof of a conjecture of P. Erdős.* In *Combinatorial Theory and Its Applications II*, North-Holland, 1970, 601–623.
- **[Partial]** M. Aigner, S. Brandt. *Embedding arbitrary graphs of maximum degree two.* Journal of the London Mathematical Society **48** (1993), 39–51.
- **[Partial]** N. Alon, E. Fischer. *2-factors in dense graphs.* Discrete Mathematics **152** (1996), 13–23.
- **[SOTA]** B. Csaba, A. Shokoufandeh, E. Szemerédi. *Proof of a conjecture of Bollobás and Eldridge for graphs of maximum degree three.* Combinatorica **23** (2003), 35–72.
- **[SOTA]** B. Csaba. *On the Bollobás–Eldridge conjecture for bipartite graphs.* Combinatorics, Probability and Computing **16** (2007), 661–691.
- **[SOTA]** B. Bollobás, A. Kostochka, K. Nakprasit. *Packing $d$-degenerate graphs.* Journal of Combinatorial Theory, Series B **98** (2008), 85–94.
- **[SOTA]** H. Kaul, A. Kostochka. *Extremal graphs for a graph packing theorem of Sauer and Spencer.* Combinatorics, Probability and Computing **16** (2007), 409–416.
- **[Survey]** H. P. Yap. *Packing of graphs — a survey.* Discrete Mathematics **72** (1988), 395–404.
- **[Survey]** H. A. Kierstead, A. V. Kostochka. *A short proof of the Hajnal–Szemerédi theorem on equitable colouring.* Combinatorics, Probability and Computing **17** (2008), 265–270.

## 10. Worked Example / Concrete Special Case

**(a) Complete proof of the case $\Delta_1 = 1$.** Suppose $\Delta_1 = 1$, so $G_1$ is a matching with $m \le \lfloor n/2 \rfloor$ edges. The hypothesis $(1+1)(\Delta_2+1) \le n+1$ gives $\Delta_2 \le \frac{n-1}{2}$. Set $G = \overline{G_2}$; then
$$\delta(G) \;\ge\; n - 1 - \Delta_2 \;\ge\; n - 1 - \frac{n-1}{2} = \frac{n-1}{2}.$$
If $n$ is even, $\delta(G) \ge \lceil (n-1)/2 \rceil = n/2$, so by Dirac's theorem $G$ is Hamiltonian and contains a perfect matching, hence contains $G_1$. If $n$ is odd, $\delta(G) \ge (n-1)/2$ and $G$ is connected (any two vertices share a neighbour since $2\cdot\frac{n-1}{2} = n-1 > n-2$); a graph on odd $n$ with $\delta \ge (n-1)/2$ has a matching of size $(n-1)/2 \ge m$. Either way $G_1 \subseteq \overline{G_2}$, so they pack. $\square$

**(b) A tight instance with $\Delta_1 = \Delta_2 = 2$, $n = 9$.** Here $(\Delta_1+1)(\Delta_2+1) = 9 \le n+1 = 10$, so BEC predicts a packing. Note Sauer–Spencer does **not** apply: $2\Delta_1\Delta_2 = 8 < 9$ — it barely does here, but at $n = 8$ it would fail while BEC still asserts packing.

Take $G_1 = 3K_3$ on parts $A = \{1,2,3\}$, $B = \{4,5,6\}$, $C = \{7,8,9\}$. Then
$$\overline{G_1} = K_{3,3,3}.$$
- If $G_2 = C_9$: the cycle $1\,4\,7\,2\,5\,8\,3\,6\,9\,1$ has every consecutive pair in different parts, so $C_9 \subseteq K_{3,3,3}$ — packing found.
- If $G_2 = 3K_3$ as well: pick the transversal triangles $\{1,4,7\}, \{2,5,8\}, \{3,6,9\}$, all edges crossing parts, so $3K_3 \subseteq K_{3,3,3}$ — packing found. Explicitly, the two triangle systems are edge-disjoint in $K_9$: $G_1$ uses only within-part pairs, $G_2$ only cross-part pairs.
- Any $G_2$ with $\Delta_2 \le 2$ is a disjoint union of paths and cycles on $9$ vertices; a greedy embedding into $K_{3,3,3}$ that never reuses a part for two consecutive vertices succeeds because each part has $3 = 9/3$ vertices, matching the Hajnal–Szemerédi equitable bound.

**(c) Where the margin lives.** At $n = 8$, $\Delta_1 = \Delta_2 = 2$: $(3)(3) = 9 > n+1 = 9$? No — $9 \le 9$, so BEC still applies, while $2\Delta_1\Delta_2 = 8 = n$ makes Sauer–Spencer fail by exactly one. Take $G_1 = G_2 = 2K_3 \cup 2K_1$. Then $\overline{G_1}$ is $K_{3,3}$ joined completely to two extra vertices, which contains $2K_3$ (one triangle using a cross pair plus an extra vertex, twice). This one-unit band — $2\Delta_1\Delta_2 \ge n$ but $(\Delta_1+1)(\Delta_2+1) \le n+1$ — is precisely the region described in §6 that remains unproven for $\Delta_1 \ge 4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*