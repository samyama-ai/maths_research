---
id: 07-combinatorics/bunkbed-conjecture
title: "Bunkbed Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bunkbed Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bunkbed-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be a finite graph and $T\subseteq V$ a set of *transversal* vertices. The **bunkbed graph** $G_T$ is built from two disjoint copies of $G$ — the *lower bunk* $\{(v,0)\}$ and the *upper bunk* $\{(v,1)\}$ — joined by a vertical *post* $\{(v,0),(v,1)\}$ for each $v\in T$. Run Bernoulli bond percolation: copy edges $(e,0)$ and $(e,1)$ are open with the same probability $p_e$, independently; the post at $v$ is open with probability $q_v$, independently.

**Conjecture (Kasteleyn, c. 1985).** For all $u,v\in V$,
$$\Pr\big[(u,0)\leftrightarrow (v,0)\big]\;\ge\;\Pr\big[(u,0)\leftrightarrow (v,1)\big].$$
Informally: in a random bunkbed, a fixed vertex is at least as likely to be connected to a target *on its own bunk* as to the mirror image of that target on the other bunk. The intuition is that any path to $(v,1)$ must cross an odd number of posts, and post-crossings are "costly".

**Resolution.** The conjecture is **false**. Gladkov, Pak and Zimin (2024) exhibit an explicit finite graph and probability assignment for which the inequality fails strictly. A complete disproof requires only a single such triple $(G,T,\{p_e,q_v\})$ together with a certified evaluation of both connection probabilities; a proof of the surviving restricted versions (e.g. planar $G$, or $p_e\equiv 1/2$) remains open.

## 2. Mathematical Foundations

Write $\Omega=\{0,1\}^{E(G_T)}$ with product measure $\mathbb P_{p,q}$. For $\omega\in\Omega$ let $\{x\leftrightarrow y\}$ denote the event that $x,y$ lie in the same open cluster. Define
$$\Delta_{u,v}(G,T)\;=\;\Pr\big[(u,0)\leftrightarrow(v,0)\big]-\Pr\big[(u,0)\leftrightarrow(v,1)\big].$$
The conjecture asserts $\Delta_{u,v}\ge 0$ always.

**Parity structure.** Assign to each vertical post the "level flip" map. A path from $(u,0)$ to $(v,\varepsilon)$ in $G_T$ projects to a walk in $G$; the number of posts used has parity $\varepsilon$. This $\mathbb Z/2$ grading is the entire source of the conjecture's plausibility, and also the reason it has no obvious monotonicity proof.

**Reflection symmetry.** The involution $\sigma_S$ that reflects the levels of all vertices in a set $S\subseteq V$ with $\partial S\cap T=\emptyset$ is a measure-preserving automorphism of $\mathbb P_{p,q}$. When $G$ is such that enough such involutions exist (e.g. $G$ a complete graph with symmetric parameters), reflection arguments give $\Delta\ge0$ directly.

**Polynomial form.** With all $p_e=p$, $q_v=q$, both terms are polynomials in $p,q$ with integer coefficients:
$$\Delta_{u,v}(p,q)=\sum_{k,\ell} c_{k\ell}\,p^k q^\ell,\qquad c_{k\ell}\in\mathbb Z,$$
counting (with signs, via inclusion–exclusion over open subgraphs) configurations connecting $u$ to $v$ on the same versus opposite bunk. Disproof therefore reduces to an exact rational computation in a finite polynomial ring.

**Standard tools available.** Harris–FKG (positive correlation of increasing events), the BK inequality for disjoint occurrence, and the van den Berg–Kahn inequality
$$\Pr[u\leftrightarrow v \text{ and } x\leftrightarrow y]\;\ge\;\Pr[u\leftrightarrow v]\,\Pr[x\leftrightarrow y]\ \text{fails in general},$$
its correct form being the Harris bound; none of these is signed correctly to yield $\Delta\ge 0$.

**Hypergraph generalisation.** For a $3$-uniform hypergraph $H$ one takes the same two-copy construction with hyperedges opened independently in each copy; connectivity means connectivity of the induced hypergraph. The conjecture has an evident analogue here, and it is this analogue that broke first.

## 3. History & State of the Art (SOTA)

- **c. 1985 — Origin.** Pieter Kasteleyn formulated the statement in the context of percolation-theoretic correlation inequalities for statistical mechanics; it circulated orally and was recorded in print by van den Berg and Kahn in their 1998–2001 work on connection-event correlations.
- **1998–2003 — Häggström.** Olle Häggström popularised the problem, proved continuous ("bunkbed on wheels"/complete-graph) variants and formulated the strong, coupling-based version: that one can couple so that $\{(u,0)\leftrightarrow(v,1)\}\subseteq\{(u,0)\leftrightarrow(v,0)\}$ pointwise after a measure-preserving map.
- **2011 — Linusson.** Proof for outerplanar graphs and for graphs whose transversal set is small or structured; introduced systematic local-move (path-switching) methods.
- **2016–2019 — Symmetric classes.** de Buyer settled complete graphs at $p=1/2$; van Hintum and Lammers settled the complete graph with general symmetric parameters; Rudzinski and Smyth gave equivalent poset formulations plus exhaustive computer checks on small graphs.
- **2023 — Hutchcroft, Kent, Nizić-Nikolac.** The conjecture holds in the $p\uparrow 1$ limit for every fixed finite graph: $\Delta_{u,v}(p)\ge 0$ for $p$ sufficiently close to $1$. This was the strongest general-graph result ever obtained.
- **2023 — Gladkov.** The *strong* (coupling) bunkbed conjecture is false, removing the most natural proof strategy.
- **2024 — Hollom.** The $3$-uniform hypergraph analogue is false: an explicit small hypergraph counterexample. This showed the conjecture is "not robust to generalisation".
- **2024 — Gladkov, Pak, Zimin.** *The bunkbed conjecture is false* (arXiv:2410.02545). Hollom's hypergraph is converted into an ordinary graph counterexample with $7222$ vertices and $14442$ edges, with a rigorous exact-arithmetic verification that $\Delta_{u,v}<0$; the reported deficit is of order $10^{-4341}$.

## 4. Partial Results / Verified Cases

The conjecture is **proved** in the following settings; all remain valid theorems.

- **Complete graphs $K_n$**, all $p_e=p$, all $q_v=q$, arbitrary $n$ (van Hintum–Lammers 2019); earlier the case $p=1/2$ (de Buyer 2016).
- **Complete bipartite graphs $K_{m,n}$** and related highly symmetric classes (Richthammer 2022).
- **Outerplanar graphs**, and graphs where $|T|\le 2$ or where the transversal set separates simply (Linusson 2011).
- **Trees, cycles, and series-parallel graphs**, where explicit path decomposition gives $\Delta\ge0$ by term-by-term comparison.
- **$p\to 1$ regime:** for every fixed finite $G,T$ there is $p_0(G)<1$ with $\Delta_{u,v}(p)\ge0$ for $p\in[p_0,1]$ (Hutchcroft–Kent–Nizić-Nikolac 2023). Also trivially true in the $p\to0$ regime by leading-order path counting: shortest same-bunk paths beat shortest cross-bunk paths.
- **Exhaustive computation** over all graphs on at most nine vertices with all transversal choices, at symbolic $p$ (Rudzinski–Smyth 2016) — no counterexample.
- **Wheels and complete graphs minus a matching**, and the case $u=v$ (trivial: $\Delta_{u,u}\ge 0$ since $\Pr[(u,0)\leftrightarrow(u,0)]=1$).

## 5. Principal Obstacles

Why the conjecture resisted for forty years, and why its falsity was hard to detect:

- **No monotone coupling.** The natural strategy — construct a measure-preserving injection from cross-bunk configurations into same-bunk ones — is provably impossible: Gladkov (2023) refuted the strong form. Any correct proof of a restricted case must be non-constructive or averaging-based.
- **Correlation inequalities are the wrong sign.** FKG and BK compare *increasing* events; $\{(u,0)\leftrightarrow(v,0)\}$ and $\{(u,0)\leftrightarrow(v,1)\}$ are both increasing and are positively correlated, which gives no information about their *difference*.
- **Parity cancellation.** The polynomial $\Delta_{u,v}(p,q)$ has massively cancelling signed coefficients. Its true minimum is exponentially small in $|V|$ — the known deficit $10^{-4341}$ on $7222$ vertices means floating-point search is hopeless and any random or heuristic search on small graphs returns "true".
- **Small cases are misleading.** Every graph on $\le 9$ vertices satisfies the inequality, and all natural symmetric families satisfy it. Local path-switching arguments succeed exactly on graphs of small treewidth or high symmetry and give no purchase in the middle range.
- **Asymptotic methods only reach the edges of parameter space.** The $p\uparrow 1$ proof uses a perturbative expansion around the full configuration; the expansion's error terms blow up away from $p=1$, and no interpolation to moderate $p$ exists.

## 6. The Gap

The original gap — between symmetric/small verified classes and general graphs — has been closed *negatively*. The remaining boundary is now:

1. **Planar graphs.** No planar counterexample is known; the Gladkov–Pak–Zimin graph is non-planar, and Hollom's hypergraph loses planarity when expanded into a graph. Whether $\Delta_{u,v}\ge0$ for all planar $G$ is the central surviving open question.
2. **Uniform parameters.** The counterexample uses a non-uniform assignment (including edges of probability essentially $1$ used to simulate contractions). Whether the conjecture fails when all $p_e=p$ for a fixed $p$, and in particular at $p=1/2$, is open — continuity gives failure on some open parameter set, but not with all coordinates equal. *(frontier — verify)*
3. **Minimum counterexample size.** The gap between $9$ vertices (verified true) and $7222$ (false) is more than three orders of magnitude.

## 7. Current Research (as of June 2026)

- **Planar bunkbed.** The most active line, pursued at Caltech (Hutchcroft's probability group) and UCLA (Pak's combinatorics group), asks whether planarity plus the Jordan curve theorem forces the parity heuristic to be correct. Partial progress exists for planar graphs with all transversals on the outer face — a direct extension of Linusson's outerplanar theorem. *(frontier — verify)*
- **Minimising counterexamples.** Computer-assisted searches aim to shrink the $7222$-vertex example by replacing Hollom's gadget with smaller hypergraph counterexamples and by tightening the hypergraph-to-graph translation. *(frontier — verify)*
- **Quantitative bounds.** Determining $\min_{G,T,u,v,p}\Delta_{u,v}$ as a function of $|V|$: is the deficit necessarily exponentially small, i.e. is the conjecture "true up to $e^{-cn}$"?
- **Related inequalities.** Renewed attention to the van den Berg–Kahn conjectures on connection-event correlations, several of which were believed to follow the same intuition and are now viewed with suspicion.

## 8. Future Work

- Prove or disprove the **planar case**; a proof would explain why every hand-drawn instance obeys the inequality.
- Settle the **uniform-$p$** version, especially $p=1/2$, where combinatorial bijection methods are strongest.
- Develop a **structural criterion** — a minor-closed or treewidth-based condition — separating graphs satisfying the inequality from those that do not. It is not known whether the class of bunkbed-satisfying graphs is minor-closed.
- Extend to **infinite lattices**: does $\Delta\ge0$ hold on $\mathbb Z^d\times K_2$ with $T=V$? The counterexample does not embed as a subgraph in a way that preserves the sign.
- Re-examine other percolation folklore conjectures whose only support is parity intuition plus small-case verification.

## 9. Key References

- **[Foundational]** J. van den Berg and J. Kahn. *A correlation inequality for connection events in percolation.* Annals of Probability, 29(1):123–126, 2001.
- **[Foundational]** O. Häggström. *Probability on bunkbed graphs.* Proceedings of FPSAC 2003 (Formal Power Series and Algebraic Combinatorics), Linköping, 2003.
- **[Partial]** S. Linusson. *On percolation and the bunkbed conjecture.* Combinatorics, Probability and Computing, 20(1):103–117, 2011.
- **[Partial]** P. de Buyer. *A proof of the bunkbed conjecture for the complete graph at $p=1/2$.* Preprint, 2016.
- **[Partial]** P. van Hintum and P. Lammers. *The bunkbed conjecture on the complete graph.* European Journal of Combinatorics, 76:175–177, 2019.
- **[Partial]** N. Rudzinski and C. Smyth. *Equivalent formulations of the bunk bed conjecture.* The North Carolina Journal of Mathematics and Statistics, 2:23–28, 2016.
- **[Partial]** T. Richthammer. *Bunkbed conjecture for complete bipartite graphs and related classes of graphs.* Preprint, 2022.
- **[SOTA]** T. Hutchcroft, A. Kent and P. Nizić-Nikolac. *The bunkbed conjecture holds in the $p\uparrow1$ limit.* Combinatorics, Probability and Computing, 32(3):363–369, 2023.
- **[SOTA]** N. Gladkov. *A strong bunkbed conjecture is false.* Preprint, 2023.
- **[SOTA]** L. Hollom. *The bunkbed conjecture is not robust to generalisation.* Preprint, 2024.
- **[SOTA / Resolution]** N. Gladkov, I. Pak and A. Zimin. *The bunkbed conjecture is false.* arXiv:2410.02545, 2024.
- **[Survey]** G. Grimmett. *Percolation.* 2nd edition, Grundlehren der mathematischen Wissenschaften 321, Springer, 1999. (Background on FKG, BK, and connection events.)

## 10. Worked Example / Concrete Special Case

Take $G$ to be the single edge $\{u,v\}$ with $T=\{u,v\}$. The bunkbed $G_T$ is a $4$-cycle: horizontal edges $e_0=\{(u,0),(v,0)\}$ and $e_1=\{(u,1),(v,1)\}$, each open with probability $p$; posts $f_u=\{(u,0),(u,1)\}$ and $f_v=\{(v,0),(v,1)\}$, each open with probability $q$.

**Same bunk.** $(u,0)\leftrightarrow(v,0)$ iff $e_0$ is open, or the three-edge route $f_u,e_1,f_v$ is open. These two routes are edge-disjoint and independent, so
$$\Pr[(u,0)\leftrightarrow(v,0)]=1-(1-p)\big(1-pq^2\big)=p+pq^2-p^2q^2.$$

**Opposite bunk.** $(u,0)\leftrightarrow(v,1)$ iff $A=\{f_u,e_1 \text{ open}\}$ or $B=\{e_0,f_v \text{ open}\}$. Here $\Pr[A]=\Pr[B]=pq$ and $A\cap B$ is the all-open event of the four distinct edges, so $\Pr[A\cap B]=p^2q^2$ and
$$\Pr[(u,0)\leftrightarrow(v,1)]=2pq-p^2q^2.$$

**Difference.**
$$\Delta_{u,v}(p,q)=\big(p+pq^2-p^2q^2\big)-\big(2pq-p^2q^2\big)=p\big(1-2q+q^2\big)=p(1-q)^2\;\ge\;0,$$
with equality exactly when $p=0$ or $q=1$. The equality case is instructive: when all posts are certainly open, the two bunks are identified and the conjecture is tight. It is precisely by engineering many near-tight local gadgets and combining them so that the residual signs cancel adversarially that Gladkov–Pak–Zimin drive $\Delta$ below zero — on a graph with $7222$ vertices, and only by about $10^{-4341}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*