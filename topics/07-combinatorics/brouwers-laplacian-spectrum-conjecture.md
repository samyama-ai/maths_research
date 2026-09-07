---
id: 07-combinatorics/brouwers-laplacian-spectrum-conjecture
title: "Brouwer's Laplacian Spectrum Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brouwer's Laplacian Spectrum Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/brouwers-laplacian-spectrum-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple graph with $n$ vertices and $m$ edges, and let
$$\mu_1(G) \ge \mu_2(G) \ge \cdots \ge \mu_n(G) = 0$$
be the eigenvalues of its Laplacian matrix. Write $S_k(G) = \sum_{i=1}^{k}\mu_i(G)$ for the sum of the $k$ largest Laplacian eigenvalues.

**Conjecture (Brouwer, c. 2008).** For every simple graph $G$ and every $k$ with $1 \le k \le n$,
$$S_k(G) \;\le\; m + \binom{k+1}{2}.$$

A complete proof must establish the inequality for all $n$, all $m$, and all $k$ simultaneously; a disproof requires one explicit graph and one index $k$ with $S_k(G) > m + \binom{k+1}{2}$. The bound is attained — it is not merely an asymptotic claim — so any proof must be tight against an infinite family of extremal graphs (Section 10).

## 2. Mathematical Foundations

For $G=(V,E)$ with $|V|=n$, let $A$ be the adjacency matrix and $D = \mathrm{diag}(d_1,\dots,d_n)$ the diagonal degree matrix. The **Laplacian** is
$$L(G) = D - A, \qquad x^{\mathsf T} L x = \sum_{uv \in E} (x_u - x_v)^2 \ \ge 0 ,$$
so $L$ is positive semidefinite, $\mu_n = 0$ with eigenvector $\mathbf{1}$, and $\operatorname{tr} L = \sum_i \mu_i = 2m$. The multiplicity of $0$ equals the number of connected components; $\mu_{n-1}$ is the algebraic connectivity.

Two standard facts frame the problem:

- **Trace/Ky Fan characterization.** $S_k(G) = \max \{ \operatorname{tr}(X^{\mathsf T} L X) : X \in \mathbb{R}^{n\times k},\, X^{\mathsf T}X = I_k \}$, i.e. $S_k$ is the Ky Fan $k$-norm of $L$. It is therefore a *convex* function of $L$, hence subadditive over edge sets: $S_k(G_1 \cup G_2) \le S_k(G_1) + S_k(G_2)$ on a common vertex set.
- **Interlacing / edge addition.** Adding an edge increases each $\mu_i$ weakly and increases $\sum_i \mu_i$ by exactly $2$; deleting an edge $e$ gives $\mu_i(G) \ge \mu_i(G-e) \ge \mu_{i+1}(G)$.

Two elementary upper bounds already dispose of most parameter ranges:
$$S_k(G) \le 2m \quad\text{(trace)}, \qquad S_k(G) \le kn \quad\text{(since } \mu_1 \le n\text{)} .$$
The first proves the conjecture whenever $m \le \binom{k+1}{2}$, i.e. $k \gtrsim \sqrt{2m}$; the second whenever $kn - \binom{k+1}{2} \le m$, i.e. roughly $k \lesssim m/n$. The open window is therefore
$$\tfrac{m}{n} \;\lesssim\; k \;\lesssim\; \sqrt{2m},$$
which is nonempty precisely for sparse and moderately dense graphs at intermediate $k$.

**Related conjecture (Grone–Merris–Bai).** Let $d^{*}_j = |\{i : d_i \ge j\}|$ be the conjugate degree sequence. Then
$$S_k(G) \le \sum_{j=1}^{k} d^{*}_j \qquad (1 \le k \le n),$$
conjectured by Grone and Merris (1994) and proved by Bai (2011). Since $\sum_{j\ge 1} d^{*}_j = 2m$, the GMB bound implies Brouwer's bound whenever $\sum_{j=1}^k d^*_j \le m + \binom{k+1}{2}$, but this fails for many sparse graphs; neither inequality dominates the other in general.

**Closure under disjoint union.** If $G = G_1 \sqcup G_2$ then $S_k(G) = \max_{k_1+k_2=k} \big(S_{k_1}(G_1)+S_{k_2}(G_2)\big)$, and $\binom{k_1+1}{2}+\binom{k_2+1}{2}\le\binom{k+1}{2}$. Hence the conjecture may be assumed for connected graphs without loss of generality.

## 3. History & State of the Art (SOTA)

The inequality was posed by **Andries E. Brouwer** around 2008 as a proposed strengthening/companion of the then-open Grone–Merris conjecture, circulated on his web pages and stated in print in Brouwer and Haemers, *Spectra of Graphs* (Springer, 2012). Brouwer reported computational verification for all graphs on at most $10$ vertices.

Milestones:

- **1990–1994.** Grone, Merris and Sunder develop the majorization framework for Laplacian spectra; Grone and Merris state the conjugate-degree conjecture.
- **2010.** Haemers, Mohammadian and Tayfeh-Rezaie prove the case $k=2$ for all graphs and the full conjecture for trees, via the sharper tree bound $S_k(T) \le m + 2k-1$.
- **2010.** Mayank's Eindhoven master's thesis (supervised in the Brouwer–Haemers circle) settles split graphs and confirms the exhaustive check for $n \le 10$.
- **2011.** Bai proves the Grone–Merris conjecture (now the Grone–Merris–Bai theorem), removing one route of attack by showing GMB is *not* strong enough to imply Brouwer.
- **2012–2016.** Du–Zhou (unicyclic, bicyclic), Wang–Huang–Liu, Rocha–Trevisan, and Ganie–Alghamdi–Pirzada extend the verified families and push the range of admissible $k$.
- **2018–present.** X. Chen and coauthors obtain the best current improvements on the "large $k$" side; no general proof and no counterexample has appeared.

## 4. Partial Results / Verified Cases

**By index $k$.**
- $k=1$: $\mu_1 \le n \le m+1$ for connected $G$ (and the disjoint-union reduction handles the rest). Equality iff $G$ is a star $K_{1,n-1}$ plus isolated vertices.
- $k=2$: proved for all graphs (Haemers–Mohammadian–Tayfeh-Rezaie, 2010).
- $k = n-1$ and $k=n$: trivial, since $S_{n-1}=S_n=2m$ and $m \le \binom{n}{2} \le \binom{k+1}{2}$ for these $k$.
- $k \ge \sqrt{2m}$ (roughly) and $k \le m/n$ (roughly): trivial from the two bounds in Section 2.

**By graph class.**
- **Trees:** $S_k(T) \le (n-1) + 2k-1$, which is $\le m+\binom{k+1}{2}$ for all $k\ge1$.
- **Unicyclic and bicyclic graphs** (Du–Zhou, 2012).
- **Split graphs** and **threshold graphs**, where the Grone–Merris–Bai bound is tight and implies the Brouwer bound.
- **Regular graphs of small degree** and various degree-constrained families in the 2012–2016 literature.
- **Graphs with few edges relative to $n$**, e.g. $m \le n$ type regimes covered by the trivial bounds.

**Computationally.** Exhaustively verified for all graphs on $n \le 10$ vertices (Brouwer; Mayank), and by sampling for larger random and structured families. *(frontier — verify: claims of exhaustive checks beyond $n=11$ have circulated but no published exhaustive census beyond $n=10$ is confirmed.)*

## 5. Principal Obstacles

- **The bound is exactly tight on an infinite family.** Complete split graphs $K_k \vee \overline{K_{n-k}}$ achieve equality for every $k$ (Section 10). Any argument with slack — averaging, trace bounds, crude interlacing — cannot work; the proof must be exact at the extremal locus.
- **Convexity points the wrong way.** $S_k$ is convex in $L$, so edge-deletion/induction arguments give $S_k(G) \le S_k(G-e) + S_k(K_2\text{-edge})$, losing $2$ per edge exactly where the target loses $1$. Standard "delete an edge and induct" schemes therefore accumulate error linearly in $m$.
- **Majorization is not enough.** The Grone–Merris–Bai theorem is the strongest general majorization statement known, and it is provably weaker than Brouwer's bound for sparse graphs (e.g. long paths and trees with many degree-2 vertices), so the conjugate-degree machinery cannot be pushed to close the gap.
- **No eigenvector localization.** Proving $k=2$ already required a delicate case analysis on the structure of the top two eigenvectors; for general $k$ there is no known combinatorial certificate describing the optimal $k$-dimensional invariant subspace, so the Ky Fan variational formula is hard to exploit.
- **Spectral methods lack a combinatorial dual.** Unlike the Grone–Merris setting, there is no known interpretation of $m + \binom{k+1}{2}$ as counting a combinatorial object, so no bijective or polyhedral (e.g. matroid/Schur-Horn) proof strategy has taken hold.

## 6. The Gap

Everything is known outside the window $m/n \lesssim k \lesssim \sqrt{2m}$, and inside it only for structurally restricted classes (trees, unicyclic, bicyclic, split, $n\le 10$). The unresolved core is:

> Graphs of intermediate density — average degree $\bar d = 2m/n$ growing with $n$ but $\bar d = o(n)$ — at indices $k$ comparable to $\bar d$ up to $\sqrt{m}$, with no bounded cyclomatic number and no degree-sequence structure forcing GMB tightness.

Concretely, the missing step is a bound of the form $S_k(G) \le S_k(H) + f(k)$ for a suitable structural decomposition $G \to H$ in which $f(k) = k$ rather than $2k$ — that is, an edge-removal or vertex-splitting operation whose spectral cost matches the $\binom{k+1}{2}$ increment rather than the trace increment $2m$. No such operation is known.

## 7. Current Research (as of June 2026)

- **Sharpened $k$-ranges.** Following X. Chen's 2018 improvements, several groups (Guangxi University; Kashmir/King Abdulaziz group of Pirzada, Ganie and coauthors) continue to enlarge the interval of $k$ for which the bound is unconditional, typically by combining $\mu_1 \le \max_{uv\in E}(d_u+d_v)$ with clique-number and cyclomatic-number constraints.
- **Trevisan school (UFRGS, Porto Alegre).** Algorithmic diagonalization of tree and cograph Laplacians (the "Jacobs–Trevisan algorithm") is being extended to graphs of bounded treewidth, aiming at Brouwer's bound for such classes. *(frontier — verify)*
- **Signless Laplacian analogue.** Ashraf, Omidi and Tayfeh-Rezaie proposed the $Q = D+A$ version, $\sum_{i\le k} q_i \le m + \binom{k+1}{2}$; its status and its interaction with the Laplacian version remain an active thread.
- **Eigenvalue distribution.** Work on $m_G[n-k,n]$ — the number of Laplacian eigenvalues in an interval, in terms of domination number, matching number and diameter (Ahanjideh, Akbari, van Dam, Fakharan and successors) — supplies counting tools that could bound $S_k$ from above by localizing the spectrum.
- **Computer search.** Randomized and SDP-guided searches for near-tight graphs continue to return only equality (never violation), which is the main empirical evidence for the conjecture.

## 8. Future Work

- Identify the complete equality family. Conjecturally the extremal graphs at index $k$ are exactly the "$k$-th complete split-like" graphs; a classification would pin down what a proof must preserve.
- Develop an interlacing scheme with cost $1$ per deleted edge (rather than $2$) by deleting edges in a matching or a star, exploiting that $S_k$ is insensitive to edges spanned by the bottom eigenspace.
- Prove the conjecture for cographs and for graphs of bounded treewidth, then attempt a minor-monotone or decomposition-based induction.
- Attack the regime $k \asymp \bar d$ directly via a Schur–Horn / majorization polytope argument, seeking a doubly stochastic transfer between the Laplacian spectrum and the degree sequence that respects the $\binom{k+1}{2}$ term.
- Settle $k=3$ in full generality — the natural next case after Haemers–Mohammadian–Tayfeh-Rezaie, and a plausible test bed for any new technique.

## 9. Key References

- **[Foundational]** A. E. Brouwer and W. H. Haemers. *Spectra of Graphs.* Springer, Universitext, 2012. (Statement of the conjecture and background on Laplacian spectra.)
- **[Foundational]** R. Grone, R. Merris and V. S. Sunder. *The Laplacian spectrum of a graph.* SIAM Journal on Matrix Analysis and Applications 11 (1990), 218–238.
- **[Foundational]** R. Grone and R. Merris. *The Laplacian spectrum of a graph II.* SIAM Journal on Discrete Mathematics 7 (1994), 221–229.
- **[Key partial result]** W. H. Haemers, A. Mohammadian and B. Tayfeh-Rezaie. *On the sum of Laplacian eigenvalues of graphs.* Linear Algebra and its Applications 432 (2010), 2214–2221.
- **[Key theorem]** H. Bai. *The Grone–Merris conjecture.* Transactions of the American Mathematical Society 363 (2011), 4463–4474.
- **[SOTA / Recent]** Z. Du and B. Zhou. *Upper bounds for the sum of Laplacian eigenvalues of graphs.* Linear Algebra and its Applications 436 (2012), 3672–3683.
- **[SOTA / Recent]** S. Wang, Y. Huang and B. Liu. *On a conjecture for the sum of Laplacian eigenvalues.* Mathematical and Computer Modelling 56 (2012), 60–68.
- **[SOTA / Recent]** H. A. Ganie, A. M. Alghamdi and S. Pirzada. *On the sum of the Laplacian eigenvalues of a graph and Brouwer's conjecture.* Linear Algebra and its Applications 501 (2016), 376–389.
- **[SOTA / Recent]** X. Chen. *Improved results on Brouwer's conjecture for sum of the Laplacian eigenvalues of a graph.* Linear Algebra and its Applications 557 (2018), 327–338.
- **[Related]** F. Ashraf, G. R. Omidi and B. Tayfeh-Rezaie. *On the sum of signless Laplacian eigenvalues of a graph.* Linear Algebra and its Applications 438 (2013), 4539–4546.
- **[Survey]** J. Rocha and V. Trevisan. *Bounding the sum of the largest Laplacian eigenvalues of graphs.* Discrete Applied Mathematics 170 (2014), 95–103.

## 10. Worked Example / Concrete Special Case

**The extremal family: complete split graphs.** Let $CS_{n,k} = K_k \vee \overline{K_{n-k}}$: a clique on $k$ vertices joined completely to an independent set of size $n-k$. Its edge count is
$$m = \binom{k}{2} + k(n-k).$$
Using the join rule — for $G_1 \vee G_2$ with $|G_i| = n_i$, the Laplacian spectrum is $\{0\} \cup \{n\} \cup \{n_2 + \mu_i(G_1)\} \cup \{n_1 + \mu_j(G_2)\}$ over the nonzero-indexed eigenvalues — we get
$$\operatorname{spec} L(CS_{n,k}) = \big\{\, n^{(k)},\; k^{(n-k-1)},\; 0 \,\big\}.$$
Check the trace: $kn + k(n-k-1) = 2kn - k^2 - k = k(k-1) + 2k(n-k) = 2m$. ✓

Now evaluate both sides at index $k$:
$$S_k = kn, \qquad m + \binom{k+1}{2} = \frac{k(k-1)}{2} + kn - k^2 + \frac{k(k+1)}{2} = kn .$$
**Equality holds for every $n$ and every $k$.** This is why no lossy argument can prove the conjecture.

**A numerical instance.** Take $n=6$, $k=2$: $G = K_2 \vee \overline{K_4}$, the "book" $B_4$, with $m = 1 + 8 = 9$. Spectrum $\{6,6,2,2,2,0\}$ (sum $=18=2m$ ✓).

| $k$ | $S_k(G)$ | $m+\binom{k+1}{2}$ | slack |
|---|---|---|---|
| 1 | 6 | 10 | 4 |
| 2 | 12 | 12 | **0** |
| 3 | 14 | 15 | 1 |
| 4 | 16 | 19 | 3 |
| 5 | 18 | 24 | 6 |

**A second tight point.** Add one edge inside the independent set: $G' = K_2 \vee (K_2 \cup \overline{K_2})$, so $m=10$. The join rule gives $\operatorname{spec} L(G') = \{6,6,4,2,2,0\}$ (sum $=20=2m$ ✓). Then $S_3(G') = 16$ and $m + \binom{4}{2} = 10+6 = 16$ — equality again, now at $k=3$. Perturbing an extremal graph moves the tight index but does not create slack, which is the local phenomenon any inductive proof has to survive.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*