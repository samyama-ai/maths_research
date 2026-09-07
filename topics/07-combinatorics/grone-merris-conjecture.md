---
id: 07-combinatorics/grone-merris-conjecture
title: "Grone-Merris Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Grone-Merris Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/grone-merris-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple graph on $n$ vertices with degree sequence $d_1 \ge d_2 \ge \dots \ge d_n$, and let $L(G) = D(G) - A(G)$ be its Laplacian matrix with eigenvalues $\mu_1 \ge \mu_2 \ge \dots \ge \mu_n = 0$. Define the **conjugate degree sequence** $d^* = (d_1^*, \dots, d_n^*)$ by

$$d_k^* \;=\; \\#\{\, i : d_i \ge k \,\}.$$

**Grone–Merris Conjecture (1994).** The Laplacian spectrum is majorized by the conjugate degree sequence:

$$\sum_{i=1}^{k} \mu_i \;\le\; \sum_{i=1}^{k} d_i^{*} \qquad \text{for every } k = 1,\dots,n .$$

Because $\sum_{i=1}^n \mu_i = \operatorname{tr} L = \sum_i d_i = \sum_k d_k^* = 2|E(G)|$, the case $k=n$ holds with equality, so the statement is exactly the majorization $\Lambda(G) \preceq d^*(G)$ in the dominance order on partitions of $2|E(G)|$.

A complete resolution requires either a proof valid for all simple graphs and all $k$, or a single explicit graph and index $k$ violating the inequality. The conjecture was **proved in full by Hua Bai (2011)** and is now the *Grone–Merris–Bai theorem*; the page is retained because the natural higher-dimensional and signless analogues remain open.

## 2. Mathematical Foundations

**Laplacian.** For $G=(V,E)$, $|V|=n$, $L(G)=D-A$ with $D=\operatorname{diag}(d_1,\dots,d_n)$. $L$ is positive semidefinite, $L\mathbf{1}=0$, and its quadratic form is
$$x^{\mathsf T} L x \;=\; \sum_{\{u,v\}\in E} (x_u - x_v)^2 .$$
The multiplicity of $0$ equals the number of connected components; $\mu_{n-1}$ is the algebraic connectivity (Fiedler value).

**Majorization.** For real vectors $a,b$ with equal total sum, $a \preceq b$ iff $\sum_{i\le k} a_{[i]} \le \sum_{i\le k} b_{[i]}$ for all $k$, where $[\cdot]$ denotes decreasing rearrangement. The Schur–Horn theorem gives $\operatorname{diag}(L) \preceq \Lambda(L)$, i.e. $d \preceq \Lambda(G)$. Grone–Merris asserts the complementary upper bound $\Lambda(G) \preceq d^*$, and since $d \preceq d^*$ always holds for a degree sequence, the three sequences interleave in dominance:
$$d \;\preceq\; \Lambda(G) \;\preceq\; d^{*}.$$

**Variational form.** By Ky Fan's maximum principle,
$$\sum_{i=1}^{k}\mu_i \;=\; \max\Big\{ \operatorname{tr}(U^{\mathsf T} L U) : U \in \mathbb{R}^{n\times k},\, U^{\mathsf T}U = I_k \Big\} \;=\; \lambda_{\max}\!\big(L^{[k]}\big),$$
where $L^{[k]}$ is the $k$-th additive compound (the induced operator on $\bigwedge^{k}\mathbb{R}^n$). This reformulation — bounding the top eigenvalue of an exterior power — is the technical arena of every serious attack.

**Threshold graphs.** A graph is *threshold* (equivalently degree-maximal, shifted, or $\{P_4,C_4,2K_2\}$-free) if it is built from a single vertex by repeatedly adding an isolated vertex or a dominating vertex. Merris (1994) proved threshold graphs are Laplacian integral with $\Lambda(G)=d^*(G)$ exactly. Threshold graphs are the extremal objects: they realize equality for all $k$ simultaneously, and they are precisely the graphs with a given degree sequence maximal in dominance order.

**Simplicial framing.** A graph is a $1$-dimensional simplicial complex; $d^*_k$ counts vertices in the $k$-th "shifted layer". Duval–Reiner (2002) recast the conjecture as a statement about the combinatorial Laplacian $L_{i}=\partial_{i+1}\partial_{i+1}^{\mathsf T}+\partial_i^{\mathsf T}\partial_i$ of a complex, with shifted complexes playing the role of threshold graphs.

## 3. History & State of the Art (SOTA)

- **1990.** Grone, Merris and Sunder, *The Laplacian spectrum of a graph* (SIAM J. Matrix Anal. Appl. 11), establish the basic inequalities $\mu_1 \le n$ and $\mu_i \ge d_i - i + 2$-type bounds, and $d \preceq \Lambda(G)$.
- **1994.** Grone and Merris, *The Laplacian spectrum of a graph II* (SIAM J. Discrete Math. 7, 221–229), state the conjecture $\Lambda(G)\preceq d^*(G)$, motivated by the exact equality they observed for degree-maximal graphs.
- **1994.** Merris, *Degree maximal graphs are Laplacian integral*, proves the equality case, identifying threshold graphs as the conjectured extremals.
- **2002.** Duval and Reiner, *Shifted simplicial complexes are Laplacian integral* (Trans. AMS 354), generalize the equality phenomenon to shifted complexes and prove a **weakened Grone–Merris inequality with a multiplicative constant**, plus a conjectural higher-dimensional version.
- **2005–2006.** Tamon Stephen, *On the Grone–Merris conjecture*, proves the inequality for small $k$ (notably $k=2$) by a direct combinatorial-variational argument, and reports extensive computational checks.
- **2011.** **Hua Bai**, *The Grone–Merris conjecture* (Trans. Amer. Math. Soc. 363, 4463–4474; arXiv:0911.2727), proves the conjecture in full generality for graphs.
- **After 2011.** Attention shifts to (i) **Brouwer's conjecture** $\sum_{i\le k}\mu_i \le |E| + \binom{k+1}{2}$, which is *incomparable* to Grone–Merris and still open; (ii) the Duval–Reiner higher-dimensional conjecture; (iii) signless-Laplacian, distance-Laplacian and normalized analogues.

## 4. Partial Results / Verified Cases

Milestones proved before Bai's theorem, each still the cleanest argument in its range:

- **$k=1$, all graphs.** $\mu_1 \le |V(H)|$ where $H$ is $G$ minus isolated vertices, and $|V(H)| = d_1^*$. Refinements: $\mu_1 \le \max\{d_u+d_v : uv\in E\}$ (Anderson–Morley) and $\mu_1 \le \max\{d_u + m_u\}$ (Merris).
- **$k=n-1$ and $k=n$.** Trivial from $\mu_n=0$ and the trace identity.
- **$k=2$.** Stephen (2006), unconditional.
- **Threshold / degree-maximal graphs (equality).** Merris (1994): $\Lambda = d^*$ exactly. These include complete graphs $K_n$ ($\Lambda=(n^{n-1},0)$, $d^*=(n,\dots,n,0)$), stars $K_{1,n-1}$, complete split graphs, and all graphs obtained by dominating/isolated vertex additions.
- **Laplacian-integral families.** Shifted simplicial complexes (Duval–Reiner 2002) in the $1$-dimensional case reduce to threshold graphs; the theorem there is exact.
- **Weak version with a constant.** Duval–Reiner proved $\sum_{i\le k}\mu_i \le C\sum_{i\le k}d^*_i$ for an absolute constant, for graphs and shifted-complex-adjacent settings.
- **Computational verification.** Exhaustive checks on all graphs up to $n \le 10$ vertices (over $10^7$ graphs) and randomized checks well beyond reported in the Stephen and Bai literature; no violation ever found.
- **Full theorem (2011).** Bai: the inequality holds for every simple graph and every $k$, with equality for all $k$ iff $G$ is threshold.

## 5. Principal Obstacles

The difficulty that stalled the problem for 17 years is that the two sides live in different categories and no single monotone connects them.

- **Eigenvalue sums are not combinatorially local.** $\sum_{i\le k}\mu_i = \lambda_{\max}(L^{[k]})$ involves $\binom{n}{k}$-dimensional exterior powers. Interlacing (Cauchy, Haemers' quotient interlacing) controls single eigenvalues under vertex deletion but degrades additively across $k$ terms, so induction on $n$ loses exactly the slack needed.
- **Edge-deletion induction fails.** Removing an edge decreases the right side by at most $1$ but can decrease $\sum_{i\le k}\mu_i$ by less (or the reverse), because $L(G)-L(G-e)$ is a rank-one PSD matrix whose top-$k$ eigenvalue contribution is not bounded by the change in $d^*$.
- **Shifting/compression is not spectrally monotone in an obvious way.** The combinatorial extremal principle (threshold graphs maximize in dominance) suggests Kruskal–Katona-style compression, but standard shifting operations do not visibly increase $\sum_{i\le k}\mu_i$ term by term; proving the needed monotonicity is itself as hard as the conjecture.
- **Trace/moment methods are too coarse.** Bounding $\sum_{i\le k}\mu_i$ via $\operatorname{tr}L^p$ or Chebyshev-type inequalities gives constants strictly worse than $1$ — exactly the Duval–Reiner weak form — and no moment method distinguishes threshold graphs from near-threshold ones.
- **Equality is fragile.** The extremal family is large and the inequality is tight for whole ranges of $k$ on many non-threshold graphs (e.g. any graph where $\mu_{k+1}=\dots=\mu_n=0$ forces equality at $k$), so no strict-inequality "margin" is available to absorb error terms.

Bai's resolution circumvents these by an induction on the structure of the graph relative to a vertex of maximum degree, combined with a Duval–Reiner style reduction to a statement about the top eigenvalue of the exterior power, in which the induction hypothesis is applied to a *smaller* combinatorial object rather than to $G$ minus an edge.

## 6. The Gap

For graphs, there is no gap: Bai closed it. The remaining boundary is dimensional and structural.

- **Higher dimensions (open).** Duval and Reiner conjecture that for a $d$-dimensional simplicial complex $K$, the spectrum of the $i$-th combinatorial Laplacian is majorized by the conjugate of the appropriate degree sequence of $i$-faces, with equality iff $K$ is shifted. Bai's induction is genuinely $1$-dimensional: it uses the fact that a vertex link in a graph is an independent set, which has no analogue for $i \ge 1$.
- **Brouwer's conjecture (open).** $\sum_{i\le k}\mu_i \le |E(G)| + \binom{k+1}{2}$ is neither implied by nor implies Grone–Merris–Bai; it is known for $k=1,2$, for trees (Haemers–Mohammadian–Tayfeh-Rezaie 2010), for split and threshold graphs, and for $k \ge n-2$, but open in general.
- **Signless Laplacian (open).** For $Q = D + A$ the analogous majorization $\Lambda(Q) \preceq d^* + (\text{correction})$ has no proven form; $Q$ lacks the incidence-decomposition $L=\partial\partial^{\mathsf T}$ over $\mathbb{R}$ with signed orientation that Bai's argument uses.

## 7. Current Research (as of June 2026)

- **Higher-dimensional Grone–Merris.** Work in the Minnesota/Duval–Reiner tradition on Laplacians of shifted and near-shifted complexes; the $2$-dimensional case is the active target, with partial results for complexes whose $1$-skeleton is threshold. *(frontier — verify)*
- **Brouwer's conjecture.** The most active descendant problem. Progress by the Brazilian spectral graph theory school (de Abreu, Oliveira, Trevisan) on trees, unicyclic and bicyclic graphs, and by Tilburg/Eindhoven (Haemers and co-authors) on split graphs and regularity constraints. Recent preprints extend it to graphs with bounded clique number and to $k$ near $n$. *(frontier — verify)*
- **Sharpened Grone–Merris.** Quantitative stability: if $\sum_{i\le k}\mu_i$ is close to $\sum_{i\le k}d_i^*$ for all $k$, is $G$ close to threshold in edit distance? Open, with only qualitative statements available. *(frontier — verify)*
- **Analogues.** Distance-Laplacian majorization (Aouchiche–Hansen framework), normalized Laplacian versions, and Laplacian energy $LE(G)=\sum|\mu_i - 2m/n|$ bounds derived from Bai's theorem.
- **Algorithmic/verification.** Continued use of `nauty`/`SageMath` sweeps to test proposed higher-dimensional and signless variants on small complexes.

## 8. Future Work

- Adapt Bai's induction to simplicial complexes by finding the right replacement for "the link of a maximum-degree vertex", possibly via algebraic shifting (Kalai) which preserves Betti numbers and is known to send complexes to shifted ones.
- Look for a *unified* inequality specializing to both Grone–Merris–Bai and Brouwer, e.g. a majorization by a sequence interpolating between $d^*$ and $(|E|+\binom{k+1}{2})$-type increments; Haemers has repeatedly raised this.
- Develop a compression proof: show directly that a suitable shifting operation weakly increases every partial eigenvalue sum. Such a proof would be shorter than Bai's and would likely dimension-lift.
- Characterize *partial* equality: for which $(G,k)$ does $\sum_{i\le k}\mu_i = \sum_{i\le k}d_i^*$ hold at a single $k$ without $G$ being threshold? A full answer would give the stability version.
- Test the signless analogue systematically and settle whether any majorization statement is even true for $Q=D+A$.

## 9. Key References

- **[Foundational]** R. Grone, R. Merris, V. S. Sunder. *The Laplacian spectrum of a graph.* SIAM Journal on Matrix Analysis and Applications 11(2), 218–238, 1990.
- **[Foundational]** R. Grone, R. Merris. *The Laplacian spectrum of a graph II.* SIAM Journal on Discrete Mathematics 7(2), 221–229, 1994. (Original statement of the conjecture.)
- **[Foundational]** R. Merris. *Degree maximal graphs are Laplacian integral.* Linear Algebra and its Applications 199, 381–389, 1994.
- **[SOTA]** H. Bai. *The Grone–Merris conjecture.* Transactions of the American Mathematical Society 363(9), 4463–4474, 2011. (arXiv:0911.2727)
- **[Key partial]** A. M. Duval, V. Reiner. *Shifted simplicial complexes are Laplacian integral.* Transactions of the American Mathematical Society 354(11), 4313–4344, 2002.
- **[Key partial]** T. Stephen. *On the Grone–Merris conjecture.* Discrete Mathematics and Theoretical Computer Science, Proceedings (FPSAC/Formal Power Series and Algebraic Combinatorics), 2005/2006.
- **[Related open problem]** W. H. Haemers, A. Mohammadian, B. Tayfeh-Rezaie. *On the sum of Laplacian eigenvalues of graphs.* Linear Algebra and its Applications 432(9), 2214–2221, 2010.
- **[Related]** A. E. Brouwer, W. H. Haemers. *A lower bound for the Laplacian eigenvalues of a graph — proof of a conjecture by Guo.* Linear Algebra and its Applications 429(8–9), 2131–2135, 2008.
- **[Survey]** R. Merris. *Laplacian matrices of graphs: a survey.* Linear Algebra and its Applications 197–198, 143–176, 1994.
- **[Survey / Book]** A. E. Brouwer, W. H. Haemers. *Spectra of Graphs.* Universitext, Springer, 2012.
- **[Survey]** N. M. M. de Abreu. *Old and new results on algebraic connectivity of graphs.* Linear Algebra and its Applications 423(1), 53–73, 2007.

## 10. Worked Example / Concrete Special Case

**Case A — the path $P_4$ (non-threshold, strict inequality).** Vertices $1\!-\!2\!-\!3\!-\!4$, $m=3$ edges. Degrees $d=(2,2,1,1)$, so
$$d_1^*=\\#\{i: d_i\ge 1\}=4,\quad d_2^*=\\#\{i:d_i\ge 2\}=2,\quad d_3^*=d_4^*=0,$$
giving $d^*=(4,2,0,0)$ with $\sum d^*_k = 6 = 2m$. ✓

Laplacian eigenvalues of $P_n$ are $2-2\cos(k\pi/n)$, $k=0,\dots,n-1$; for $n=4$:
$$\Lambda(P_4)=\big(2+\sqrt2,\;2,\;2-\sqrt2,\;0\big)\approx(3.414,\,2,\,0.586,\,0).$$

Partial sums:

| $k$ | $\sum_{i\le k}\mu_i$ | $\sum_{i\le k}d_i^*$ | status |
|---|---|---|---|
| 1 | $3.414$ | $4$ | strict |
| 2 | $5.414$ | $6$ | strict |
| 3 | $6$ | $6$ | equality |
| 4 | $6$ | $6$ | equality (trace) |

Equality at $k=3$ is forced by $\mu_4=0$, not by structure — illustrating the "fragile equality" obstacle of Section 5: $P_4$ is the minimal forbidden subgraph for threshold graphs, yet still meets the bound exactly at $k=3$.

**Case B — the star $K_{1,3}$ (threshold, full equality).** Degrees $d=(3,1,1,1)$, so $d^*=(4,1,1,0)$. The Laplacian spectrum of $K_{1,n-1}$ is $(n,1^{n-2},0)$, i.e. $\Lambda(K_{1,3})=(4,1,1,0)$. Every partial sum matches: $4=4$, $5=5$, $6=6$, $6=6$. This is Merris's equality theorem in the smallest nontrivial instance: $K_{1,3}$ is built by adding a dominating vertex to $\overline{K_3}$, hence threshold, hence Laplacian integral with $\Lambda = d^*$.

Comparing A and B: both graphs have $m=3$ and $n=4$, but $P_4$'s degree sequence $(2,2,1,1)$ is strictly below $(3,1,1,1)$ in dominance, and correspondingly its spectrum sits strictly inside the bound at $k=1,2$. The conjecture asserts this is universal — the threshold graph with a dominating degree sequence is always the spectral ceiling.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*