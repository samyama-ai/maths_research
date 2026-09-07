---
id: 07-combinatorics/gyarfas-tree-packing-conjecture
title: "Gyárfás' Tree Packing Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gyárfás' Tree Packing Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/gyarfas-tree-packing-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Gyárfás 1976; Gyárfás–Lehel).** Let $T_1, T_2, \dots, T_n$ be trees with $|V(T_i)| = i$ for every $i$. Then $T_1, \dots, T_n$ pack into the complete graph $K_n$: there exist injections $\varphi_i : V(T_i) \to V(K_n)$ such that the edge sets $\varphi_i(E(T_i))$ are pairwise disjoint subsets of $E(K_n)$.

The packing, if it exists, is necessarily **perfect** (a decomposition of $K_n$): the trees carry
$$\sum_{i=1}^{n} (i-1) \;=\; \binom{n}{2} \;=\; |E(K_n)|$$
edges in total, so every edge of $K_n$ is used exactly once. The statement is thus equivalent to: *every* such sequence of trees decomposes $K_n$, with no room for slack anywhere.

A complete proof must produce (or prove the existence of) such embeddings for **all** $n$ and **all** choices of the trees, including adversarial ones (e.g. all $T_i$ stars, or a mixture of stars and paths of the worst kind). A disproof requires exhibiting one $n$ and one sequence $(T_i)_{i \le n}$ admitting no packing. The conjecture is currently open in general and proved in several substantial regimes (Section 4), hence *partially-solved*.

## 2. Mathematical Foundations

**Packing.** Graphs $G_1,\dots,G_k$ on at most $n$ vertices *pack into* a host $H$ on $n$ vertices if there are injective maps $\varphi_i : V(G_i)\to V(H)$ with $\varphi_i(E(G_i)) \subseteq E(H)$ and $\varphi_i(E(G_i)) \cap \varphi_j(E(G_j)) = \emptyset$ for $i\neq j$. Equivalently, $H$ contains edge-disjoint copies of all $G_i$. A packing is *perfect* when $\sum_i e(G_i) = e(H)$, i.e. it is a decomposition $E(H)=\bigsqcup_i \varphi_i(E(G_i))$.

**Trees.** $T_i$ is connected and acyclic, so $e(T_i)=i-1$ and $\sum_{i=1}^n e(T_i)=\binom n2$. Write $\Delta(T)$ for the maximum degree, $L(T)$ for the number of leaves, and $d(T)$ for the degeneracy ($d(T)=1$ for any tree with an edge).

**Degree feasibility.** For a vertex $v \in V(K_n)$ the packing must satisfy
$$\sum_{i=1}^{n} \deg_{T_i}\big(\varphi_i^{-1}(v)\big) \;=\; n-1 ,$$
where $\deg_{T_i}(\cdot)=0$ if $v \notin \varphi_i(V(T_i))$. Summing over $v$ recovers the edge count; the *local* constraint is what makes greedy strategies fail, since $\Delta(T_n)$ may be as large as $n-1$.

**Two extremal instances.** If $T_n=K_{1,n-1}$ (star) then its centre $c$ has all $n-1$ incident edges consumed, so $T_1,\dots,T_{n-1}$ must perfectly pack $K_n - c \cong K_{n-1}$: the conjecture is self-reducing on star-heavy sequences. If instead $T_n=P_n$ (path), a Hamilton path is used and $K_n$ minus a Hamilton path is still near-regular.

**Related statements.**
- *Ringel's conjecture (1963).* Every tree $T$ with $m$ edges decomposes $K_{2m+1}$ into $2m+1$ copies of $T$. Proved for large $m$ by Montgomery, Pokrovskiy and Sudakov (2021).
- *Graceful tree conjecture (Ringel–Kotzig).* A graceful labelling of $T$ yields a cyclic decomposition of $K_{2m+1}$, implying Ringel's conjecture for that tree.
- *Gyárfás–Lehel bipartite/ordered variants* and the "$n+1$ host" relaxation used in Section 4.

**Main tools.** Absorption; the regularity method (Szemerédi's regularity lemma with a *blow-up lemma for approximate decompositions*); random greedy / nibble processes; Rödl-style iterative packing; and rainbow-matching / Latin-square arguments transplanted from the Ringel line of work.

## 3. History & State of the Art (SOTA)

- **1976.** Gyárfás and Lehel state and study the conjecture in *Packing trees of different order into $K_n$* (Colloq. Math. Soc. János Bolyai 18, Keszthely 1976), proving it when every $T_i$ is a star or a path, and other structured families.
- **1978–1983.** Independent formulations and small-case work (Zaks–Liu decomposition results; Fishburn's analysis of odd/even tree packings). The conjecture is verified for $n \le 9$.
- **1983.** Bollobás, *Some remarks on packing trees*: the $\lfloor n/\sqrt{2}\rfloor$ smallest trees always pack into $K_n$ — the first unconditional "positive fraction" result, by a simple counting/greedy argument.
- **1981–1987.** Hobbs; Hobbs, Bourgeois and Kasiraj: the two (and, under conditions, three) largest trees pack into $K_n$.
- **2013.** Balogh and Palmer: the $\Theta(n^{1/4})$ *largest* trees pack — attacking the hard end of the sequence rather than the easy end.
- **2016.** Böttcher, Hladký, Piguet and Taraz: an approximate version for bounded-degree trees, using regularity.
- **2019.** Joos, Kim, Kühn and Osthus: the conjecture holds **exactly** for bounded-degree trees and all sufficiently large $n$ — the single largest advance, built on the Kim–Kühn–Osthus–Tyomkyn blow-up lemma for approximate decompositions plus absorption.
- **2021.** Montgomery, Pokrovskiy and Sudakov prove Ringel's conjecture for large trees, establishing that the "one tree, many copies" analogue is fully tractable.
- **Since.** Effort has shifted to removing the bounded-degree hypothesis (degeneracy + many leaves; near-linear maximum degree; quasirandom hosts).

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $n \le 9$ | Full verification of all tree sequences | Fishburn (1983) / early enumeration |
| All $T_i$ stars or paths | Conjecture holds | Gyárfás–Lehel (1976) |
| $T_n, T_{n-1}$ (and $T_{n-2}$, restricted) | Pack into $K_n$ | Hobbs (1981); Hobbs–Bourgeois–Kasiraj (1987) |
| $T_1,\dots,T_{\lfloor n/\sqrt2\rfloor}$ | Pack into $K_n$ | Bollobás (1983) |
| $T_{n-k},\dots,T_n$ with $k=\tfrac1{10}n^{1/4}$ | Pack into $K_{n+1}$ | Balogh–Palmer (2013) |
| $\Delta(T_i)\le D$, $|V(T_i)|\le(1-\varepsilon)n$ | Pack into $K_{(1+\varepsilon)n}$ | Böttcher–Hladký–Piguet–Taraz (2016) |
| $\Delta(T_i)\le D$ fixed, $n\ge n_0(D)$ | **Conjecture true** (exact, perfect packing of $K_n$) | Joos–Kim–Kühn–Osthus (2019) |
| Bounded degeneracy $+\;\Omega(n)$ leaves | Perfect packing into $K_n$ for large $n$ | Allen–Böttcher–Clemens–Taraz (2019 preprint) |
| Minor-closed families, separable families | Approximate packings into $K_n$ | Messuti–Rödl–Schacht (2016); Ferber–Lee–Mousset (2017) |
| $\Delta \le cn/\log n$, near-spanning trees | Approximate packing (random/complete hosts) | Ferber–Samotij (2019) |

So the conjecture is settled asymptotically whenever the degree profile is controlled: bounded $\Delta$, or bounded degeneracy with a linear number of leaves. It is open as soon as some $T_i$ carries a vertex of degree $\omega(1)$ without compensating leaf structure — most starkly, sequences containing many stars.

## 5. Principal Obstacles

- **No slack.** The packing is forced to be perfect. Every regularity/absorption method leaves an $o(n^2)$ leftover of edges; converting an approximate packing into an exact one requires an absorbing structure that can swallow an arbitrary residue. Joos–Kim–Kühn–Osthus supply such a structure only under $\Delta(T_i)\le D$, because the absorber's capacity is measured in bounded-degree embeddings.
- **Blow-up lemma degree ceiling.** The blow-up lemma for approximate decompositions (Kim–Kühn–Osthus–Tyomkyn) embeds spanning bounded-degree graphs into super-regular pairs. Its error terms degrade like $\Delta$ and break entirely at $\Delta = n^{\Omega(1)}$: a vertex of degree $\Theta(n)$ must consume a constant fraction of one host vertex's edges, which no local randomised embedding can schedule.
- **Stars destroy quasirandomness.** After embedding $K_{1,n-1}$ the host is $K_{n-1}$ plus an isolated-ish vertex — the leftover is not pseudorandom in any uniform sense, and repeated star removal produces a rigid, deterministic recursion rather than a random-like process where nibble arguments apply.
- **Simultaneous global constraints.** Unlike Ringel's conjecture (one tree, all copies isomorphic, symmetry available from cyclic/algebraic labellings), here $n$ *different* trees must be scheduled at once. Latin-square and rainbow-matching tricks that power the Ringel proof lose their symmetry.
- **Small trees are not free.** The many tiny trees $T_1,\dots,T_{\sqrt n}$ have few edges but still occupy vertices; counting arguments (Bollobás) exhaust exactly when the cumulative edge demand reaches $\sim n^2/4$.

## 6. The Gap

Proven: the conjecture for all sequences with $\max_i \Delta(T_i) \le D$ for a constant $D$ and $n \ge n_0(D)$; plus prefixes/suffixes of unrestricted sequences of length $\Theta(n)$ and $\Theta(n^{1/4})$ respectively.

Wanted: unrestricted $\Delta$, up to $\Delta(T_n)=n-1$.

The precise barrier is **an exact packing method insensitive to maximum degree**. Concretely, three steps are missing:

1. An embedding lemma that places a tree with $\Delta = \Theta(n)$ into a near-complete host while retaining pseudorandomness of the leftover — high-degree vertices must be embedded *first* and globally, not by local randomisation.
2. An absorber whose reservoir tolerates high-degree residual edges, so that $o(n^2)$ leftover edges can be redistributed when the remaining trees are stars.
3. Control of the interaction: a proof must handle sequences that mix bounded-degree trees (where current tools work) with stars (where the recursion of Section 2 works) — no framework currently spans both regimes at once.

## 7. Current Research (as of June 2026)

- **Birmingham / Warwick / Heidelberg (Kühn, Osthus, Joos, Kim, Montgomery).** Extending approximate-decomposition blow-up machinery to trees of degree $n^{o(1)}$, and to host graphs that are only quasirandom. *(frontier — verify)* Announced progress raising the admissible degree bound from $O(1)$ to $n^{c}$ for small $c$.
- **LSE / FU Berlin / Hamburg (Allen, Böttcher, Clemens, Taraz).** The degeneracy-plus-leaves route: replacing $\Delta \le D$ with $d(T)\le D$ and $L(T)\ge \alpha n$, then trying to weaken the leaf hypothesis toward $L(T) \ge n^{1-o(1)}$.
- **Oxford / ETH (Pokrovskiy, Sudakov, Keevash, Staden).** Transporting Ringel-conjecture technology — random greedy tree embeddings with rainbow structure, and Ringel's conjecture in quasirandom hosts — to the multi-tree setting.
- **Star-heavy exact analysis.** The recursion "if $T_n$ is a star, delete its centre" gives a clean induction; work is ongoing on hybrid sequences where a bounded number of stars appear at arbitrary positions. *(frontier — verify)*
- **Computation.** Exhaustive verification remains limited by the super-exponential number of sequences ($\prod_i t_i$, where $t_i$ counts trees on $i$ vertices); SAT/ILP formulations have been used for spot checks at moderate $n$ rather than complete ranges. *(frontier — verify)*

## 8. Future Work

- Prove the conjecture for $\Delta(T_i) \le n^{1-\varepsilon}$; then close the last gap for star-like trees using the deletion recursion.
- Develop an absorption framework in which the absorber is itself a tree sequence, making the residue "self-similar" to the problem.
- Settle the weaker Gyárfás–Lehel variant with host $K_{n+1}$ (one spare vertex) in full generality — the slack of $n$ extra edges might be enough for existing nibble arguments.
- Classify which *pairs* of trees $(T_i,T_j)$ are hardest to co-embed, producing a local obstruction theory; absence of local obstructions plus a compactness/entropy argument would be a genuinely new route.
- Pursue an entropy or flow formulation: count packings via a fractional relaxation (a doubly stochastic assignment of tree-edges to host-edges) and prove integrality via an entropy-concentration argument.

## 9. Key References

- **[Foundational]** A. Gyárfás, J. Lehel. *Packing trees of different order into $K_n$.* Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely 1976), Colloq. Math. Soc. János Bolyai 18, North-Holland, 1978, 463–469.
- **[Foundational]** B. Bollobás. *Some remarks on packing trees.* Discrete Mathematics 46 (1983), 203–204.
- **[Foundational]** P. C. Fishburn. *Packing graphs with odd and even trees.* Journal of Graph Theory 7 (1983), 369–383.
- **[Foundational]** A. M. Hobbs, B. A. Bourgeois, J. Kasiraj. *Packing trees in complete graphs.* Discrete Mathematics 67 (1987), 27–42.
- **[Partial]** J. Balogh, C. Palmer. *On the tree packing conjecture.* SIAM Journal on Discrete Mathematics 27 (2013), 1995–2006.
- **[Partial]** J. Böttcher, J. Hladký, D. Piguet, A. Taraz. *An approximate version of the tree packing conjecture.* Israel Journal of Mathematics 211 (2016), 191–221.
- **[SOTA]** F. Joos, J. Kim, D. Kühn, D. Osthus. *Optimal packings of bounded degree trees.* Journal of the European Mathematical Society 21 (2019), 3573–3647.
- **[SOTA / Tools]** J. Kim, D. Kühn, D. Osthus, M. Tyomkyn. *A blow-up lemma for approximate decompositions.* Transactions of the American Mathematical Society 371 (2019), 4655–4742.
- **[SOTA / Related]** R. Montgomery, A. Pokrovskiy, B. Sudakov. *A proof of Ringel's conjecture.* Geometric and Functional Analysis 31 (2021), 663–720.
- **[Related]** S. Messuti, V. Rödl, M. Schacht. *Packing minor-closed families of graphs into complete graphs.* Journal of Combinatorial Theory Series B 119 (2016), 245–265.
- **[Related]** A. Ferber, C. Lee, F. Mousset. *Packing spanning graphs from separable families.* Israel Journal of Mathematics 219 (2017), 959–982.
- **[Related]** A. Ferber, W. Samotij. *Packing trees of unbounded degrees in random graphs.* Journal of the London Mathematical Society 99 (2019), 653–677.
- **[Preprint]** P. Allen, J. Böttcher, D. Clemens, A. Taraz. *Perfectly packing graphs with bounded degeneracy and many leaves.* arXiv:1906.11558, 2019.
- **[Survey]** R. Yuster. *Combinatorial and computational aspects of graph packing and graph decomposition.* Computer Science Review 1 (2007), 12–26.

## 10. Worked Example / Concrete Special Case

**Case $n=5$.** $K_5$ on $V=\{1,2,3,4,5\}$ has $\binom52=10$ edges. The trees must satisfy $e(T_1)+\cdots+e(T_5)=0+1+2+3+4=10$, so the packing is a decomposition. Take the hardest-looking mixture: $T_5=P_5$ (path), $T_4=K_{1,3}$ (star), $T_3=P_3$, $T_2=K_2$.

Embed:

| Tree | Edges | Image in $K_5$ |
|---|---|---|
| $T_5=P_5$ | $4$ | $12,\;23,\;34,\;45$ |
| $T_4=K_{1,3}$ | $3$ | $13,\;14,\;15$ (centre $1$) |
| $T_3=P_3$ | $2$ | $42,\;25$ (centre $2$) |
| $T_2=K_2$ | $1$ | $35$ |
| $T_1$ | $0$ | any vertex |

The ten images are $\{12,13,14,15,23,24,25,34,35,45\}$ — exactly $E(K_5)$, each once. Degree check at vertex $1$: $\deg_{P_5}=1$, $\deg_{K_{1,3}}=3$, $\deg_{P_3}=0$, $\deg_{K_2}=0$, total $4=n-1$. ✓

**The star recursion.** Now take $n=5$ with $T_5=K_{1,4}$. Its centre, say $5$, absorbs all four edges at $5$. The remaining trees $T_1,\dots,T_4$ must decompose $K_5-5 \cong K_4$, which has $6=0+1+2+3$ edges. With $T_4=P_4$, $T_3=P_3$, $T_2=K_2$ on $\{1,2,3,4\}$: $P_4 = 1\!-\!2\!-\!3\!-\!4$ uses $12,23,34$; $P_3 = 1\!-\!3\!-\!?$ uses $13$ and $3$'s remaining neighbour is exhausted, so instead take $P_3 = 2\!-\!4\!-\!1$ using $24,41$; then $T_2=13$. Union: $\{12,23,34,24,14,13\}=E(K_4)$. ✓

This illustrates both the mechanism (Section 2's self-reduction: an all-star sequence reduces $K_n \to K_{n-1} \to \cdots$, so the all-star case is trivially true by induction) and the difficulty: adversarial sequences interleave stars with wide, bushy trees, and no known argument handles that interleaving. Section 4's theorems cover the case where the star $K_{1,4}$ above is replaced by any $T_5$ with $\Delta \le D$; the open territory begins precisely when both a high-degree tree and a non-star bushy tree appear in the same sequence with $n$ large.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*