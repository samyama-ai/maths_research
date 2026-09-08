---
id: 07-combinatorics/brualdi-hollingsworth-conjecture
title: "Brualdi–Hollingsworth Conjecture on Rainbow Spanning Trees"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brualdi–Hollingsworth Conjecture on Rainbow Spanning Trees

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/brualdi-hollingsworth-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $n \ge 3$ and let $K_{2n}$ be properly edge-coloured with exactly $2n-1$ colours — equivalently, fix a **one-factorization** of $K_{2n}$, the colour classes being perfect matchings. A subgraph is **rainbow** (multicoloured) if no two of its edges share a colour.

**Conjecture (Brualdi–Hollingsworth, 1996).** The edge set of $K_{2n}$ can be partitioned into $n$ edge-disjoint rainbow spanning trees.

The parameters are forced: $|E(K_{2n})| = n(2n-1)$, each spanning tree has $2n-1$ edges, so $n$ trees exactly exhaust the edges, and each tree must use **every** colour exactly once. The conjecture therefore asserts a perfect decomposition, not a packing with slack.

A proof must handle every one-factorization of every $K_{2n}$ with $n \ge 3$; the case $n = 2$ is genuinely false (Section 10). A disproof requires exhibiting one one-factorization of some $K_{2n}$ admitting no such partition.

**Stronger form (Constantine, 2002).** The $n$ trees can additionally be taken pairwise isomorphic.

**Related form (Kaneko–Kano–Suzuki).** Any proper edge-colouring of $K_n$ (any number of colours) contains $\lfloor n/2 \rfloor$ edge-disjoint rainbow spanning trees.

## 2. Mathematical Foundations

Let $G = (V,E)$ with $|V| = N$. A proper edge-colouring is a map $c : E \to C$ with $c(e) \ne c(f)$ whenever $e \cap f \ne \emptyset$. When $N = 2n$ and $|C| = 2n-1 = \chi'(K_{2n})$, the colouring is **optimal** and each class
$$M_i = c^{-1}(i), \qquad |M_i| = n, \qquad \bigsqcup_{i=1}^{2n-1} M_i = E(K_{2n})$$
is a perfect matching; $\mathcal{F} = \{M_1,\dots,M_{2n-1}\}$ is a one-factorization.

A subgraph $H$ is rainbow iff $|E(H) \cap M_i| \le 1$ for all $i$. A rainbow spanning tree $T$ satisfies $|E(T)| = 2n-1$ and hence $|E(T) \cap M_i| = 1$ for every $i$: $T$ is a **transversal** of $\mathcal{F}$ that happens to be a spanning tree. The conjecture asks for a partition
$$E(K_{2n}) = \bigsqcup_{j=1}^{n} E(T_j), \quad T_j \text{ spanning trees with } |E(T_j)\cap M_i| = 1 \ \ \forall i,j,$$
i.e. an $n \times (2n-1)$ array whose rows are spanning trees and whose columns are the one-factors — a "multicoloured parallelism".

Two classical facts frame the difficulty.

- **Matroid intersection.** Rainbow spanning subgraphs of $G$ are the common independent sets of the graphic matroid $M(G)$ and the partition matroid $P_c$ with ground blocks $M_i$. By Edmonds' theorem a rainbow spanning tree exists iff for every $C' \subseteq C$ the graph $\bigcup_{i \in C'} M_i$ has at most $|C'| + $ (number of components) $-1$ … in particular a **single** rainbow spanning tree is trivial here: every star $K_{1,2n-1}$ at a vertex $v$ is rainbow, since the $2n-1$ edges at $v$ get distinct colours. All the content lies in edge-disjointness.
- **Nash-Williams–Tutte / Nash-Williams decomposition.** Uncoloured, $K_{2n}$ does decompose into exactly $n$ spanning trees, since $|E| = n(2n-1)$ and $K_{2n}$ is $n$-tree-connected. So the conjecture is a *rainbow refinement of a tight tree decomposition* — there is zero edge slack to absorb colour conflicts.

## 3. History & State of the Art (SOTA)

- **1996.** Richard Brualdi and Susan Hollingsworth, *Multicolored trees in complete graphs* (JCTB 68, 310–313), pose the conjecture and prove $K_{2n}$ ($n \ge 3$) contains **2** edge-disjoint rainbow spanning trees.
- **2000.** Krussel, Marshall and Verrall push this to **3** edge-disjoint rainbow spanning trees (Ars Combinatoria 57).
- **2002.** Constantine strengthens the conjecture to isomorphic trees and verifies small cases.
- **2006.** Akbari, Alipour, Fu and Lo (SIAM J. Discrete Math. 20) settle the *existence* form of Constantine's conjecture for infinite families of orders: explicit one-factorizations of $K_{2n}$ decomposing into $n$ isomorphic rainbow spanning trees.
- **2016.** Carraher, Hartke and Horn: every properly edge-coloured $K_n$ (arbitrary colouring) has $\lfloor n/(1000 \log n)\rfloor$ edge-disjoint rainbow spanning trees — the first bound growing with $n$.
- **2018.** Horn removes the logarithm in the one-factorized setting: $\Omega(n)$, i.e. at least $cn$ edge-disjoint rainbow spanning trees in any one-factorized $K_{2n}$, for an explicit but tiny $c > 0$.
- **2019.** Montgomery, Pokrovskiy and Sudakov prove the **asymptotic** conjecture: any properly coloured $K_n$ contains $(1/2 - o(1))n$ edge-disjoint *isomorphic* rainbow spanning trees.
- **2021.** Glock, Kühn, Montgomery and Osthus prove that for all sufficiently large $n$, every optimal edge-colouring of $K_n$ decomposes into $\lfloor n/2 \rfloor$ isomorphic rainbow spanning trees — resolving both Brualdi–Hollingsworth and Constantine for large $n$.

**SOTA summary:** true for $n$ large (non-explicit threshold $n_0$), true for $2n \le 6$, and only "3 trees out of $n$" unconditionally in the middle range.

## 4. Partial Results / Verified Cases

| Result | Guarantee | Range |
|---|---|---|
| Brualdi–Hollingsworth 1996 | 2 disjoint rainbow spanning trees | all $2n \ge 6$ |
| Krussel–Marshall–Verrall 2000 | 3 disjoint rainbow spanning trees | all $2n \ge 6$ |
| Carraher–Hartke–Horn 2016 | $\lfloor n/(1000\log n)\rfloor$ | all proper colourings of $K_n$ |
| Horn 2018 | $cn$, $c>0$ absolute | one-factorized $K_{2n}$ |
| Montgomery–Pokrovskiy–Sudakov 2019 | $(1/2-o(1))n$, isomorphic | all proper colourings of $K_n$ |
| Glock–Kühn–Montgomery–Osthus 2021 | full $n/2$, isomorphic | $n \ge n_0$, optimal colourings |

Concrete consequences:

- **$2n = 4$ ($n=2$): FALSE.** Every one-factorization of $K_4$ fails (Section 10) — this is why $n \ge 3$ is assumed.
- **$2n = 6$ ($n=3$): TRUE, all colourings.** $K_6$ has a unique one-factorization up to isomorphism and $n = 3$ trees are needed, exactly the Krussel–Marshall–Verrall bound; an explicit decomposition is given in Section 10, and its three trees are isomorphic, so Constantine holds too.
- **$2n = 8$ ($n = 4$): needs 4 trees**, one beyond the unconditional bound; $K_8$ has 6 non-isomorphic one-factorizations, and the case is settled only by direct computer search, not by any of the general theorems.
- **Structured colourings.** For the standard "starter" one-factorization $GK_{2n}$ ($\mathbb{Z}_{2n-1}$-cyclic, colour $i$ = $\{\infty i\} \cup \{\{i+k, i-k\}\}$), algebraic constructions of Akbari–Alipour–Fu–Lo give full isomorphic decompositions for infinite families of $n$.

## 5. Principal Obstacles

- **No slack.** The decomposition is exact: $n(2n-1)$ edges, $n$ trees, every colour once per tree. Probabilistic and greedy methods produce packings with $\varepsilon n^2$ leftover edges; here the leftover must be $0$. This is why Horn's linear bound gives $cn$ with $c \ll 1/2$ and cannot be tuned upward.
- **The endgame.** After removing $(1/2-\varepsilon)n$ trees, the remaining graph has average degree $\approx 2\varepsilon n$ and the surviving colour classes are near-perfectly determined: each remaining vertex must still receive a specific multiset of colours. Local switching arguments (rotate an edge out of $T_j$, into $T_k$) run out of admissible moves because both the tree constraint (acyclicity) and the transversal constraint (one edge per colour) bind simultaneously.
- **Matroid intersection does not iterate.** One rainbow spanning tree is a matroid intersection problem, solvable in polynomial time. Packing $k$ disjoint common independent sets is not a matroid intersection problem — the union of the graphic matroid with itself interacts badly with the partition matroid, and no Edmonds–Rado-type min–max characterisation is known for rainbow tree packings.
- **Adversarial colourings.** Lower-bound intuition from Latin squares (a one-factorization of $K_{2n}$ is a symmetric Latin square) means a proof must survive colourings with heavy algebraic structure, e.g. the $\mathbb{Z}_2^k$ one-factorization where many rainbow subgraphs are forced to close up into cycles — exactly the phenomenon that kills $K_4$.
- **Absorption costs a threshold.** The successful method (iterative absorption plus random greedy) reserves an absorbing structure whose existence needs $n$ large; the reserved set is polynomial in $1/\varepsilon$, so the argument gives no explicit $n_0$ and no information for $n$ in the hundreds.

## 6. The Gap

Proven: (a) $3$ trees for all $n \ge 3$; (b) all $n$ trees for $n \ge n_0$ with $n_0$ non-explicit. The gap is the **small- and medium-$n$ window** $4 \le n < n_0$, where only $3$ trees are guaranteed out of $n$.

Two distinct barriers must be crossed:

1. **Effectivise $n_0$.** Glock–Kühn–Montgomery–Osthus use iterative absorption with an unquantified reservoir; extracting an explicit $n_0$ (even $10^{10}$) would reduce the conjecture to a finite — if presently infeasible — computation and to a bridging argument.
2. **A finite-$n$ argument.** No induction from $K_{2n}$ to $K_{2n+2}$ is known: deleting two vertices from a one-factorization of $K_{2n+2}$ does not yield a one-factorization of $K_{2n}$ (it yields a near-one-factorization with $2n+1$ classes of size $n-1$ or $n$), so the natural recursion breaks at the first step.

## 7. Current Research (as of June 2026)

- **Birmingham / Warwick school (Kühn, Osthus, Glock, Montgomery).** Continued development of iterative absorption for rainbow decompositions; the same machinery resolved Ringel's conjecture and the Oberwolfach problem. Current effort targets quantitative absorption with explicit thresholds. *(frontier — verify)*
- **ETH / Zurich (Sudakov, Pokrovskiy and collaborators).** Rainbow structures in *bounded* rather than proper colourings: results for colourings where each colour appears at most $(1-\varepsilon)n/2$ times generalise the one-factorization case and are the natural next target.
- **Latin-square viewpoint.** The Brualdi–Hollingsworth problem is a symmetric analogue of the Ryser–Brualdi–Stein transversal problem; transfer of the recent full resolution of Ryser–Brualdi–Stein for large orders to the tree setting is actively pursued. *(frontier — verify)*
- **Computational.** Exhaustive/SAT-based verification for $2n = 8, 10, 12$ over all non-isomorphic one-factorizations (6 for $K_8$, 396 for $K_{10}$, 526\,915\,620 for $K_{12}$) is feasible up to $2n=10$ and reported consistent with the conjecture; $2n = 12$ is at the edge of exhaustive search. *(frontier — verify)*

## 8. Future Work

- Prove the conjecture for all $n$ by a self-contained combinatorial argument (switching, network flows, or a min–max theorem for rainbow tree packings) that avoids absorption.
- Obtain an explicit $n_0$ from the 2021 proof.
- Settle the **Kaneko–Kano–Suzuki** version: $\lfloor n/2\rfloor$ edge-disjoint rainbow spanning trees for *arbitrary* proper colourings of $K_n$, where the colour classes may be far from perfect matchings.
- Extend to $K_{2n}$ minus a one-factor, to complete multipartite graphs, and to rainbow decompositions into other spanning structures (Hamiltonian paths, near-perfect matchings).
- Find a min–max/polyhedral characterisation of maximum rainbow spanning tree packings; even the complexity of deciding whether $2$ edge-disjoint rainbow spanning trees exist in a general edge-coloured graph is not fully classified.

## 9. Key References

- **[Foundational]** R. A. Brualdi, S. Hollingsworth. *Multicolored trees in complete graphs.* Journal of Combinatorial Theory, Series B, 68(2):310–313, 1996.
- **[Foundational]** J. Krussel, S. Marshall, H. Verrall. *Spanning trees orthogonal to one-factorizations of $K_{2n}$.* Ars Combinatoria, 57:77–82, 2000.
- **[Foundational]** G. M. Constantine. *Multicolored parallelisms of isomorphic spanning trees.* Discrete Mathematics and Theoretical Computer Science, 5:121–125, 2002.
- **[Partial]** S. Akbari, A. Alipour, H.-L. Fu, Y.-H. Lo. *Multicolored parallelisms of isomorphic spanning trees.* SIAM Journal on Discrete Mathematics, 20(3):564–567, 2006.
- **[Partial]** J. Carraher, S. G. Hartke, P. Horn. *Edge-disjoint rainbow spanning trees in complete graphs.* European Journal of Combinatorics, 57:71–84, 2016.
- **[Partial]** P. Horn. *Rainbow spanning trees in complete graphs colored by one-factorizations.* Journal of Graph Theory, 87(3):333–346, 2018.
- **[SOTA]** R. Montgomery, A. Pokrovskiy, B. Sudakov. *Decompositions into spanning rainbow structures.* Proceedings of the London Mathematical Society, 119(4):899–959, 2019.
- **[SOTA]** S. Glock, D. Kühn, R. Montgomery, D. Osthus. *Decompositions into isomorphic rainbow spanning trees.* Journal of Combinatorial Theory, Series B, 146:439–484, 2021.
- **[Survey]** A. Pokrovskiy. *Rainbow subgraphs and their applications.* In *Surveys in Combinatorics 2022*, London Mathematical Society Lecture Note Series, Cambridge University Press, 2022.
- **[Background]** J. Edmonds. *Matroid intersection.* Annals of Discrete Mathematics, 4:39–49, 1979.

## 10. Worked Example / Concrete Special Case

**(a) Why $n = 2$ fails.** Take $K_4$ on $\{1,2,3,4\}$ with its unique one-factorization
$$M_1=\{12,34\},\quad M_2=\{13,24\},\quad M_3=\{14,23\}.$$
A decomposition would need two edge-disjoint spanning trees with $3$ edges each. Spanning trees of $K_4$ are stars or Hamiltonian paths. If $T_1$ is the star at $v$, its complement is a triangle on $V \setminus \{v\}$ — not a tree. So both trees are Hamiltonian paths $a\!-\!b\!-\!c\!-\!d$. But $\{ab, cd\}$ is a perfect matching, hence monochromatic: $c(ab) = c(cd)$. **No Hamiltonian path of $K_4$ is rainbow**, so no decomposition exists. This isolated failure is exactly the $n \ge 3$ hypothesis.

**(b) The first true case, $K_6$ ($n=3$).** Vertices $\mathbb{Z}_5 \cup \{\infty\}$, starter one-factorization $c_i = \{\infty i\} \cup \{\{i+1,i-1\}, \{i+2,i-2\}\}$ for $i \in \mathbb{Z}_5$:

$$c_0=\{\infty 0,\,14,\,23\},\quad c_1=\{\infty 1,\,02,\,34\},\quad c_2=\{\infty 2,\,13,\,04\},$$
$$c_3=\{\infty 3,\,24,\,01\},\quad c_4=\{\infty 4,\,03,\,12\}.$$

Take
$$T_1=\{\infty 0,\;02,\;13,\;24,\;03\},\qquad T_2=\{23,\;\infty 1,\;\infty 2,\;01,\;\infty 4\},\qquad T_3=\{14,\;34,\;04,\;\infty 3,\;12\}.$$

*Rainbow check (colour order $c_0,c_1,c_2,c_3,c_4$):* $T_1: \infty0,02,13,24,03$; $T_2: 23,\infty1,\infty2,01,\infty4$; $T_3: 14,34,04,\infty3,12$. Each hits every colour once.

*Tree check.* $T_1$: $0$ is adjacent to $\infty,2,3$; then $2\!-\!4$ and $3\!-\!1$ — all $6$ vertices, $5$ edges, acyclic. $T_2$: $\infty$ adjacent to $1,2,4$; then $1\!-\!0$, $2\!-\!3$. $T_3$: $4$ adjacent to $1,3,0$; then $3\!-\!\infty$, $1\!-\!2$.

*Disjointness.* The five $\infty$-edges appear once each; the ten $K_5$-edges $01,02,03,04,12,13,14,23,24,34$ appear once each. Total $15 = |E(K_6)|$.

*Bonus.* All three trees are the same spider: a degree-$3$ centre with legs of lengths $1, 2, 2$ (centres $0$, $\infty$, $4$ respectively). So $K_6$ also verifies **Constantine's** stronger isomorphic form.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*