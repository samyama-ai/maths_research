---
id: 10-theoretical-cs/ringel-conjecture
title: "Ringel Conjecture"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ringel Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/ringel-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Ringel's conjecture (1963).** Let $T$ be any tree with $n$ edges. Then the complete graph $K_{2n+1}$ on $2n+1$ vertices decomposes into $2n+1$ edge-disjoint copies of $T$.

The edge count is exact, not approximate:
$$e(K_{2n+1}) = \binom{2n+1}{2} = n(2n+1) = (2n+1)\cdot e(T),$$
so a decomposition uses every edge of $K_{2n+1}$ exactly once. There is no slack — this is a *perfect* packing problem, and any proof must place the last edge as carefully as the first.

A complete resolution requires, for **every** $n \ge 1$ and **every** tree $T$ on $n$ edges, an explicit family $\{T_1,\dots,T_{2n+1}\}$ of subgraphs of $K_{2n+1}$, each isomorphic to $T$, with $E(T_i)\cap E(T_j)=\emptyset$ for $i\ne j$ and $\bigcup_i E(T_i)=E(K_{2n+1})$. A disproof requires one tree $T$ for which no such family exists.

**Status.** Montgomery, Pokrovskiy and Sudakov (GAFA, 2021) proved the conjecture for all $n \ge n_0$, with $n_0$ an unspecified large absolute constant; Keevash and Staden proved it independently by a different route. The conjecture is therefore **solved asymptotically but not for all $n$**: no explicit $n_0$ has been extracted, and the range $n$ small-to-$n_0$ rests on separate structural and computational results. The stronger *graceful tree conjecture* of Ringel–Kotzig, which implies Ringel's conjecture in the strong cyclic form, remains fully open.

## 2. Mathematical Foundations

**Decomposition.** For graphs $H,G$, an *$H$-decomposition* of $G$ is a set $\mathcal{D}=\{H_1,\dots,H_k\}$ of subgraphs of $G$, each isomorphic to $H$, such that $\{E(H_i)\}$ partitions $E(G)$. Necessarily $k=e(G)/e(H)$.

**Graceful labeling.** A labeling $f: V(T)\to\{0,1,\dots,n\}$ of a tree $T$ with $n$ edges is *graceful* if $f$ is injective and the induced edge labeling
$$f^\ast(uv) = |f(u)-f(v)|$$
is a bijection $E(T)\to\{1,2,\dots,n\}$.

**Cyclic decompositions.** Identify $V(K_{2n+1})$ with $\mathbb{Z}_{2n+1}$. For $d \in \{1,\dots,n\}$ the *difference class*
$$D_d = \{\,\{x,y\}\subseteq \mathbb{Z}_{2n+1} : y-x \equiv \pm d \pmod{2n+1}\,\}$$
has $|D_d| = 2n+1$, and $E(K_{2n+1}) = \bigsqcup_{d=1}^{n} D_d$. A copy $T_0 \subseteq K_{2n+1}$ hitting each $D_d$ exactly once is a *perfect difference family* representative, and its rotations $T_i = T_0 + i$ (all vertex labels shifted by $i$ mod $2n+1$) give a decomposition.

**Rosa's theorem (1967).** A tree $T$ with $n$ edges admits a graceful labeling **iff** $K_{2n+1}$ has a *cyclic* $T$-decomposition. Proof sketch: embed $T$ into $\mathbb{Z}_{2n+1}$ via $f$; since $0 \le f(u),f(v)\le n$, we have $|f(u)-f(v)| \le n$, so the mod-$(2n+1)$ difference of an edge equals its graceful label, and gracefulness means each difference class is hit once.

**Graceful tree conjecture (Ringel–Kotzig).** Every tree is graceful. This implies Ringel's conjecture; the converse fails, since Ringel's conjecture allows non-cyclic decompositions.

**$\alpha$-labeling.** A graceful labeling is an *$\alpha$-labeling* if there is $k$ with $\min(f(u),f(v)) \le k < \max(f(u),f(v))$ for every edge $uv$; equivalently $f$ witnesses bipartiteness with the two sides in intervals $[0,k]$ and $[k+1,n]$. $\alpha$-labelings yield decompositions of $K_{2nt+1}$ for all $t\ge 1$, not just $t=1$.

## 3. History & State of the Art (SOTA)

- **1963/64.** Ringel poses the problem as Problem 25 at the Smolenice symposium.
- **1966/67.** Rosa introduces $\beta$-valuations (later "graceful labelings") and $\alpha$-labelings, proves the equivalence above, and settles caterpillars.
- **1970s–2000s.** A long accumulation of labeled tree classes (Gallian's dynamic survey DS6 tracks hundreds of results), plus exhaustive computer searches for gracefulness of small trees.
- **2014.** Drmota and Lladó: almost every tree with $m$ edges decomposes $K_{2m+2}$ — a *typical-tree* result, not all trees.
- **2016.** Böttcher, Hladký, Piguet and Taraz prove an approximate version of the related Gyárfás–Lehel tree packing conjecture via the regularity/blow-up machinery, establishing that bounded-degree trees pack almost perfectly.
- **2019.** Joos, Kim, Kühn and Osthus prove Ringel's conjecture exactly for all trees of **bounded maximum degree** and large $n$, using a blow-up lemma for approximate decompositions (Kim–Kühn–Osthus–Tyomkyn).
- **2020.** Almost all trees are "almost graceful" (Adamaszek, Allen, Grosu, Hladký).
- **2021 (SOTA).** Montgomery, Pokrovskiy, Sudakov, *A proof of Ringel's conjecture*, GAFA 31: true for all trees with $n$ edges, $n$ sufficiently large — no degree restriction. Independently, Keevash and Staden prove the tree packing conjecture in quasirandom host graphs, which yields Ringel for large $n$.

## 4. Partial Results / Verified Cases

| Class / range | Result |
|---|---|
| Caterpillars (deleting leaves gives a path) | Graceful; cyclic decomposition (Rosa, 1967) |
| Paths $P_{n+1}$, stars $K_{1,n}$, complete binary trees, symmetric trees | Graceful, explicit labelings |
| Spiders with at most 4 legs; olive trees; firecrackers; banana trees | Graceful (Gallian DS6 catalogue) |
| Trees with $\le 4$ leaves, diameter $\le 5$ | Graceful |
| All trees with at most 27 vertices | Verified graceful by exhaustive search (Aldred–McKay, 1998) |
| All trees with at most 35 vertices | Verified graceful by computation (Fang, 2010) |
| Bounded-degree trees, $\Delta(T)\le \Delta$ fixed, $n\ge n_0(\Delta)$ | Ringel proved exactly (Joos–Kim–Kühn–Osthus, 2019) |
| Almost every tree on $m$ edges | Decomposes $K_{2m+2}$ (Drmota–Lladó, 2014) |
| **All trees, $n \ge n_0$ absolute** | **Ringel proved (Montgomery–Pokrovskiy–Sudakov, 2021; Keevash–Staden)** |
| Lobsters (deleting leaves gives a caterpillar) | Bermond's conjecture that all are graceful — open |

## 5. Principal Obstacles

- **No slack.** Approximate decomposition leaves an $\varepsilon\binom{n}{2}$-edge remainder that is an arbitrary, structurally uncontrolled graph. Regularity-based embedding cannot see it; absorption must be designed to swallow exactly it.
- **Unbounded degree defeats the blow-up lemma.** The Kim–Kühn–Osthus–Tyomkyn blow-up lemma for approximate decompositions requires $\Delta(T) = O(1)$ (or $n^{o(1)}$). A tree may have a vertex of degree $n$; a star's copy must consume nearly a full vertex neighbourhood, so degree-sequence bookkeeping in the host becomes global rather than local.
- **Gracefulness is not the right invariant for all trees, and is itself unproven.** Rosa's equivalence funnels the problem into an arithmetic labeling question with no known algebraic obstruction and no known construction — brute force is superexponential ($n!$-scale search over labelings), and no polynomial certificate structure is known.
- **The last few copies.** Once $\ge (1-\varepsilon)$ of $K_{2n+1}$ is used, the leftover host graph is sparse and irregular; standard random greedy / nibble analyses lose concentration exactly there.
- **Non-effective constants.** The 2021 proofs stack absorption, random partitioning and iterative embedding; each step contributes an unquantified tower-type or at least astronomically large constant, so $n_0$ is not extractable in usable form.

## 6. The Gap

Two distinct gaps remain.

1. **The small-$n$ gap.** Proven: all trees with $n \ge n_0$; and all trees with $\le 34$ edges via computational gracefulness. Unproven: trees with $35 \le n < n_0$, where $n_0$ is unspecified and almost certainly enormous. Closing this needs either an effective version of the MPS/Keevash–Staden argument (extracting a concrete $n_0$) or a proof of the graceful tree conjecture. Neither is in reach: the absorption steps are non-constructive in their dependence on regularity parameters.
2. **The structural gap.** Ringel's conjecture is now a theorem for large $n$, but the *cyclic* strengthening — that a decomposition can always be realised by the rotation group $\mathbb{Z}_{2n+1}$ — is exactly the graceful tree conjecture and remains open for **all** $n$ beyond the computational range. The MPS decomposition is not cyclic; it is built by embedding, not by a labeling. No known reduction upgrades a general decomposition to a cyclic one.

## 7. Current Research (as of June 2026)

- **Effective bounds.** Work on quantifying $n_0$ in the Montgomery–Pokrovskiy–Sudakov framework, in parallel with the general programme of de-regularising absorption arguments (Oxford, Warwick, ETH Zürich, Birmingham). *(frontier — verify)*
- **Graceful tree conjecture via structural decompositions.** Attacks combining $\alpha$-labelings of subtrees with amalgamation; and probabilistic constructions extending Adamaszek–Allen–Grosu–Hladký's "almost graceful" result toward exact gracefulness for typical trees. *(frontier — verify)*
- **Host-graph generalisations.** Keevash–Staden's quasirandom framework invites the question: for which densities $p$ does $G(n,p)$ admit a $T$-decomposition for all trees $T$ of the right size? Partial answers exist for bounded degree.
- **Algorithmic angle (TCS).** Given $T$, output a decomposition of $K_{2n+1}$ in polynomial time. Cyclic decompositions are trivially constructive once a graceful labeling is known; the existence proofs for large $n$ are not algorithmic. Complexity of deciding gracefulness for a general *graph* is NP-complete; for trees the decision problem is conjecturally trivial (always yes) but no polynomial-time labeling algorithm is known.
- **Computational search.** Extension of exhaustive verification past 35 vertices is limited by the $\Theta(n!)$ label space; SAT/CP encodings with symmetry breaking are the current tool of choice. *(frontier — verify)*

## 8. Future Work

- Extract an explicit $n_0$ from the 2021 proof, even if astronomically large, to make the statement "Ringel's conjecture is true for $n\ge n_0$" a finite reduction rather than an asymptotic one.
- Prove the graceful tree conjecture for lobsters (Bermond) — the natural next class after caterpillars, and the standard testbed.
- Develop absorption techniques tolerant of unbounded degree in *general* decomposition problems (Oberwolfach-type, Gyárfás–Lehel tree packing).
- Settle the Gyárfás–Lehel conjecture exactly: trees $T_1,\dots,T_n$ with $e(T_i)=i-1$ pack into $K_n$. Known approximately for bounded degree.
- Find a polynomial-time algorithm producing graceful labelings for structured tree families, or an obstruction showing none exists.

## 9. Key References

- **[Foundational]** G. Ringel. *Problem 25*, in **Theory of Graphs and its Applications** (Proc. Symposium Smolenice 1963), Publ. House Czechoslovak Acad. Sci., Prague, 1964, p. 162.
- **[Foundational]** A. Rosa. *On certain valuations of the vertices of a graph.* In **Theory of Graphs** (Internat. Sympos. Rome 1966), Gordon and Breach, 1967, pp. 349–355.
- **[SOTA]** R. Montgomery, A. Pokrovskiy, B. Sudakov. *A proof of Ringel's conjecture.* **Geometric and Functional Analysis (GAFA)** 31 (2021), 663–720.
- **[SOTA]** P. Keevash, K. Staden. *Ringel's tree packing conjecture in quasirandom graphs.* arXiv:2004.09947; **Journal of the European Mathematical Society**.
- **[SOTA]** F. Joos, J. Kim, D. Kühn, D. Osthus. *Optimal packings of bounded degree trees.* **Journal of the European Mathematical Society** 21 (2019), 3573–3647.
- **[Recent]** J. Böttcher, J. Hladký, D. Piguet, A. Taraz. *An approximate version of the tree packing conjecture.* **Israel Journal of Mathematics** 211 (2016), 391–446.
- **[Recent]** J. Kim, D. Kühn, D. Osthus, M. Tyomkyn. *A blow-up lemma for approximate decompositions.* **Transactions of the AMS** 371 (2019), 4655–4742.
- **[Recent]** M. Drmota, A. Lladó. *Almost every tree with $m$ edges decomposes $K_{2m+2}$.* **Combinatorics, Probability and Computing** 23 (2014), 50–65.
- **[Recent]** M. Adamaszek, P. Allen, C. Grosu, J. Hladký. *Almost all trees are almost graceful.* **Random Structures & Algorithms** 56 (2020), 892–938.
- **[Computational]** R. E. L. Aldred, B. D. McKay. *Graceful and harmonious labellings of trees.* **Bulletin of the ICA** 23 (1998), 69–72.
- **[Computational]** W. Fang. *A computational approach to the graceful tree conjecture.* arXiv:1003.3045, 2010.
- **[Survey]** J. A. Gallian. *A dynamic survey of graph labeling.* **Electronic Journal of Combinatorics**, Dynamic Survey DS6 (updated annually).
- **[Foundational, related]** A. Gyárfás, J. Lehel. *Packing trees of different order into $K_n$.* Colloq. Math. Soc. János Bolyai 18, 1978, pp. 463–469.

## 10. Worked Example / Concrete Special Case

Take $n=3$, so $T$ has 3 edges and the host is $K_7$, with $e(K_7)=21=7\cdot 3$. Take $T = P_4$, the path on 4 vertices.

**Step 1 — graceful labeling.** Label the path in the order $0 - 3 - 1 - 2$. Vertex labels $\{0,3,1,2\}=\{0,1,2,3\}$: injective. Edge labels:
$$|0-3| = 3,\qquad |3-1| = 2,\qquad |1-2| = 1.$$
These are exactly $\{1,2,3\}$, so the labeling is graceful.

**Step 2 — seed copy in $\mathbb{Z}_7$.** Set $T_0$ to be the path $0-3-1-2$ inside $K_7$ with $V=\mathbb{Z}_7$. Its edges $\{0,3\},\{3,1\},\{1,2\}$ lie in difference classes $D_3, D_2, D_1$ respectively — one edge per class.

**Step 3 — rotate.** For $i=0,\dots,6$ let $T_i = T_0+i$, i.e. the path $i - (i{+}3) - (i{+}1) - (i{+}2)$ mod 7:

| $i$ | path | edges |
|---|---|---|
| 0 | $0{-}3{-}1{-}2$ | 03, 13, 12 |
| 1 | $1{-}4{-}2{-}3$ | 14, 24, 23 |
| 2 | $2{-}5{-}3{-}4$ | 25, 35, 34 |
| 3 | $3{-}6{-}4{-}5$ | 36, 46, 45 |
| 4 | $4{-}0{-}5{-}6$ | 04, 05, 56 |
| 5 | $5{-}1{-}6{-}0$ | 15, 16, 06 |
| 6 | $6{-}2{-}0{-}1$ | 26, 02, 01 |

**Step 4 — check.** The 21 listed edges are $01,02,03,04,05,06,12,13,14,15,16,23,24,25,26,34,35,36,45,46,56$ — all $\binom{7}{2}=21$ edges of $K_7$, each once. So $K_7$ decomposes into 7 copies of $P_4$.

**Why this is the easy case.** Every edge fell into place because gracefulness converted a global packing constraint into a local arithmetic one: hit each of the $n$ difference classes exactly once, then let the cyclic group $\mathbb{Z}_{2n+1}$ do the rest. For a general tree of unbounded degree and large $n$, no such labeling is known to exist, and the 2021 proof abandons the group action entirely — building the $2n+1$ copies one at a time by randomised embedding with a reserved absorbing structure that mops up the final $\varepsilon$-fraction of edges.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*