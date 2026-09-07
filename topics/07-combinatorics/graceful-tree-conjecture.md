---
id: 07-combinatorics/graceful-tree-conjecture
title: "Graceful Tree Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Graceful Tree Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/graceful-tree-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Ringel–Kotzig, "Graceful Tree Conjecture").** Every finite tree admits a graceful labeling.

Concretely: let $T$ be a tree with $q$ edges and $q+1$ vertices. The claim is that there exists a bijection
$$f : V(T) \longrightarrow \{0,1,\dots,q\}$$
such that the induced edge map
$$f^{*}(uv) = |f(u) - f(v)|$$
is a bijection $E(T) \to \{1,2,\dots,q\}$.

A proof must produce such an $f$ for **every** tree, of every order and every shape — not merely for a family closed under some construction. A disproof requires exhibiting one explicit tree $T$ together with a certificate that no bijection $f$ works; since the search space for $n$ vertices has size $n!$ and gracefulness is decidable, a counterexample is in principle finitely checkable, and for a fixed small tree an exhaustive search is a valid certificate.

The conjecture is false for general graphs (e.g. $K_n$ is graceful only for $n \le 4$, and $C_n$ is graceful iff $n \equiv 0,3 \pmod 4$), so "tree" is essential.

## 2. Mathematical Foundations

Let $G=(V,E)$ with $|E|=q$.

**Definitions.**
- A **$\beta$-valuation (graceful labeling)** is an injection $f: V \to \{0,\dots,q\}$ with $\{|f(u)-f(v)| : uv \in E\} = \{1,\dots,q\}$. For a tree, $|V| = q+1$, so $f$ is forced to be a bijection onto $\{0,\dots,q\}$.
- An **$\alpha$-labeling** is a graceful labeling for which there exists a **boundary value** $\lambda$ with
$$\min\{f(u),f(v)\} \le \lambda < \max\{f(u),f(v)\} \qquad \text{for every } uv \in E .$$
Equivalently $f$ certifies bipartiteness: $\{v : f(v)\le\lambda\}$ and $\{v: f(v)>\lambda\}$ are the two colour classes.
- A **$\rho$-labeling** is an injection $f : V \to \{0,1,\dots,2q\}$ such that the induced *circular* lengths $\min\{|f(u)-f(v)|,\; 2q+1-|f(u)-f(v)|\}$ realise each of $1,\dots,q$ exactly once. Graceful $\Rightarrow$ $\rho$.

**Rosa's decomposition theorem (1967).** For a graph $G$ with $q$ edges, $K_{2q+1}$ has a cyclic $G$-decomposition **iff** $G$ has a $\rho$-labeling. In particular, if $G$ is graceful then the $2q+1$ rotations $v \mapsto f(v)+i \pmod{2q+1}$ of $G$ inside $\mathbb{Z}_{2q+1}$ tile $K_{2q+1}$ exactly.

**Consequence for trees.** Since a tree $T$ with $n$ edges has $n+1$ vertices and $K_{2n+1}$ has $n(2n+1)$ edges $= (2n+1)\cdot n$, gracefulness of $T$ implies **Ringel's conjecture** for $T$: $K_{2n+1}$ decomposes into $2n+1$ edge-disjoint copies of $T$. So the Graceful Tree Conjecture is strictly stronger than Ringel's conjecture.

**Consequence of $\alpha$.** If $G$ has an $\alpha$-labeling with $q$ edges, then $K_{2qk+1}$ has a cyclic $G$-decomposition for every $k\ge 1$, and $G$ decomposes $K_{q,q}$ and every $K_{qk,qk}$ (Rosa; Kotzig). Trees of diameter $\ge 6$ need not have $\alpha$-labelings, so $\alpha$ is genuinely stronger than gracefulness.

**Counting constraint.** Summing edge labels gives $\sum_{uv\in E}|f(u)-f(v)| = \binom{q+1}{2}$, and modulo $2$,
$$\sum_{uv \in E} \big(f(u)+f(v)\big) \equiv \binom{q+1}{2} \pmod 2 ,$$
i.e. $\sum_{v} \deg(v) f(v) \equiv \binom{q+1}{2} \pmod 2$. This parity identity is the standard obstruction that kills gracefulness for cycles $C_n$ with $n \equiv 1,2 \pmod 4$; it imposes **no** obstruction on trees, which is part of why the conjecture is believed.

## 3. History & State of the Art (SOTA)

- **1963.** Ringel poses the decomposition problem: does every tree with $n$ edges decompose $K_{2n+1}$? (Problem 25, Smolenice symposium.)
- **1966/67.** Rosa introduces $\alpha$-, $\beta$-, $\rho$- and $\sigma$-valuations and proves the decomposition equivalence. He proves caterpillars have $\alpha$-labelings.
- **1972.** Golomb coins the term "graceful"; Kotzig popularises the tree conjecture and conjectures almost all trees are graceful.
- **1979–1982.** Bermond surveys the area and raises the still-open sub-case of **lobsters**. Huang–Kotzig–Rosa settle trees with at most four leaves.
- **1998.** Aldred and McKay verify all trees on $\le 27$ vertices by computer.
- **2001.** Hrnčiar and Haviar settle all trees of diameter $5$.
- **2010.** Fang's hybrid (constraint-propagation + randomised) search verifies all trees on $\le 35$ vertices.
- **2020.** Adamaszek, Allen, Grosu and Hladký prove an approximate version for bounded-degree trees.
- **2021.** Montgomery, Pokrovskiy and Sudakov prove **Ringel's conjecture** for all sufficiently large $n$ — the strongest structural corollary of gracefulness now holds unconditionally, without proving gracefulness itself.

State of the art: the conjecture is verified up to $35$ vertices, proved for many named families, and its main *consequence* is a theorem, but no general labeling method exists.

## 4. Partial Results / Verified Cases

Proven classes (selection):

| Class | Result |
|---|---|
| Paths, stars, complete binary trees | Graceful (elementary; $\alpha$-labelings) |
| **Caterpillars** (removing leaves gives a path) | $\alpha$-labeling, Rosa 1967 |
| Trees of **diameter $\le 5$** | Graceful; Hrnčiar–Haviar 2001 (diameter $\le 4$ earlier) |
| Trees with **at most 4 leaves** | Huang–Kotzig–Rosa 1982 |
| **Spiders** with $\le 4$ legs, and spiders with legs of $\le 5$ distinct lengths | Bahls–Lake–Wertheim 2010 |
| **Symmetrical trees** (rooted, all leaves at equal depth, isomorphic branches) | Bermond–Sotteau |
| Olive trees, banana trees, firecrackers, spiders of specific leg profiles | Numerous; catalogued in Gallian's Dynamic Survey |
| **All trees on $n \le 27$ vertices** | Aldred–McKay 1998, exhaustive |
| **All trees on $n \le 35$ vertices** | Fang 2010, exhaustive search (approx. $10^{10}$ trees on 35 vertices) |

**Relaxations proved.**
- *Range-relaxed:* every tree on $n$ vertices has an injective labeling into $\{0,\dots,\binom{n}{2}\}$ with distinct edge differences (Van Bussel 2002); the target is to shrink the range to $n-1$.
- *Near-graceful, asymptotic:* for every $\varepsilon>0$ and $n$ large, every $n$-vertex tree of maximum degree $O(n/\log n)$ has an injective labeling into $\{0,\dots,(1+\varepsilon)n\}$ with all edge differences distinct (Adamaszek–Allen–Grosu–Hladký 2020).
- *Ringel's conjecture:* true for all trees with $n$ edges, $n$ large (Montgomery–Pokrovskiy–Sudakov 2021), via absorption and random greedy embedding — this does **not** yield labelings.

**Open sub-cases.** Lobsters (removing leaves gives a caterpillar) — Bermond's problem, still open in general. Trees of diameter $6$ in full generality. Trees with $5$ leaves in full generality.

## 5. Principal Obstacles

- **No local-to-global induction.** Every natural induction (delete a leaf, contract an edge, split at a centroid) changes $q$, hence changes the entire label alphabet $\{0,\dots,q\}$. A graceful labeling of $T-v$ has labels $\{0,\dots,q-1\}$ and there is no canonical way to insert a new label and re-derive a bijection on differences. The conjecture has no known self-reducible structure.
- **Rigid global constraint.** Gracefulness is a *perfect difference system*: $q$ edges must realise $q$ prescribed differences with zero slack. Probabilistic and greedy arguments, which excel when a constant fraction of slack is allowed, break down exactly at slack $0$. This is why the Adamaszek et al. result needs $(1+\varepsilon)n$ labels and cannot be pushed to $\varepsilon = 0$.
- **Absorption cannot be exact.** The Montgomery–Pokrovskiy–Sudakov machinery for Ringel's conjecture embeds copies of $T$ one at a time and absorbs leftovers; it never produces a single cyclic $\mathbb{Z}_{2n+1}$-invariant decomposition, which is what a labeling corresponds to. Their decompositions are not cyclic, so the equivalence in Section 2 gives nothing back.
- **Algebraic/Fourier methods have no handle.** Difference-set techniques (Sidon sets, character sums) control *how many* differences occur, not *which multiset of differences is realisable on a prescribed tree shape*. The tree's incidence structure is not captured by any known character-theoretic transform.
- **High-degree vertices.** A vertex of degree $d$ with label $a$ forces $d$ distinct differences from $a$; extremal trees with many high-degree vertices defeat the flow/matching relaxations (the natural bipartite matching between vertex pairs and differences is not integral).
- **Search complexity.** Exhaustive verification grows as (number of trees on $n$ vertices) $\times$ backtracking cost; the number of unlabeled trees on $n$ vertices grows like $C\,\alpha^{n} n^{-5/2}$ with $\alpha \approx 2.9558$, making $n \approx 40$ the practical wall.

## 6. The Gap

The proven region is: (i) all trees with $n \le 35$ vertices; (ii) trees constrained in *diameter* ($\le 5$), *number of leaves* ($\le 4$), or *symmetry*; (iii) approximate labelings with $\varepsilon n$ spare labels; (iv) the decomposition consequence, non-cyclically.

The general statement needs a labeling for trees of unbounded diameter **and** unbounded leaf count simultaneously — precisely where every existing constructive scheme (which fixes a spine and zig-zags labels along it) loses control. The single missing step is a mechanism that converts an approximate perfect difference system on a tree, with $\varepsilon n$ slack, into an exact one — i.e. a "de-slacking" or rounding step for difference systems. Equivalently: strengthen Montgomery–Pokrovskiy–Sudakov from an arbitrary decomposition of $K_{2n+1}$ to a **cyclic** ($\mathbb{Z}_{2n+1}$-rotational) one.

## 7. Current Research (as of June 2026)

- **Absorption / regularity school** (Montgomery, Pokrovskiy, Sudakov, Keevash, Staden, and groups at Warwick, ETH Zürich, Birmingham, UCL): pushing tree-decomposition results toward cyclic and near-optimal-host versions, and toward decompositions of $K_n$ for $n$ not of the form $2q+1$. *(frontier — verify)* Work on rotational/cyclic strengthenings of Ringel is reported but no cyclic analogue covering all trees is established.
- **Constructive labeling school** (Slovak/Czech tradition following Rosa, Hrnčiar, Haviar; Indian groups on lobsters and spiders): incremental extension of the diameter hierarchy to diameter $6$ and structured lobster families.
- **Computational school**: SAT/CP encodings and GPU-accelerated backtracking aiming to push exhaustive verification past $n = 35$. *(frontier — verify)* Claims of verification beyond 37 vertices circulate but require independent replication.
- **Relaxation school**: sharpening range-relaxed and near-graceful bounds — reducing the Adamaszek et al. label range from $(1+\varepsilon)n$ toward $n + O(1)$ and removing the maximum-degree restriction.
- **Equivalent reformulations**: Broersma–Hoede's reformulation via "strongly graceful" orientations and Eulerian-type conditions continues to be used as an alternative attack surface.

## 8. Future Work

1. **Cyclic absorption.** Develop an absorption method that preserves a group action, so leftover edges are absorbed $\mathbb{Z}_{2n+1}$-equivariantly. This would upgrade Ringel to gracefulness for large $n$ and, with the $n \le 35$ verification, potentially close the conjecture modulo a mid-range gap.
2. **Remove the degree hypothesis** in the near-graceful theorem, then attack $\varepsilon \to 0$ via a rounding or local-swap argument on the $\varepsilon n$ unused labels.
3. **Diameter induction.** Extend Hrnčiar–Haviar to diameter $6$; a uniform method for all diameters would be the first genuinely inductive scheme.
4. **Lobsters.** Bermond's problem is the natural next family and a testbed for any general technique.
5. **Complexity framing.** Determine the complexity of deciding gracefulness for general graphs (NP-complete for graphs) and whether a polynomial-time labeling *algorithm* for trees exists — a constructive algorithm would prove the conjecture.
6. **Counterexample search.** Targeted search among extremal shapes (many degree-3 branch vertices, large diameter) rather than exhaustive enumeration.

## 9. Key References

- **[Foundational]** A. Rosa. *On certain valuations of the vertices of a graph.* In *Theory of Graphs (Internat. Sympos., Rome, 1966)*, Gordon and Breach / Dunod, 1967, pp. 349–355.
- **[Foundational]** G. Ringel. *Problem 25.* In *Theory of Graphs and its Applications (Smolenice, 1963)*, Publ. House Czechoslovak Acad. Sci., Prague, 1964, p. 162.
- **[Foundational]** A. Kotzig. *On certain vertex-valuations of finite graphs.* Utilitas Mathematica 4 (1973), 261–290.
- **[SOTA / Recent]** R. Montgomery, A. Pokrovskiy, B. Sudakov. *A proof of Ringel's conjecture.* Geometric and Functional Analysis 31 (2021), 663–720.
- **[SOTA / Recent]** A. Adamaszek, P. Allen, C. Grosu, J. Hladký. *Almost all trees are almost graceful.* Random Structures & Algorithms 56 (2020), 948–987.
- **[Partial results]** P. Hrnčiar, A. Haviar. *All trees of diameter five are graceful.* Discrete Mathematics 233 (2001), 133–150.
- **[Partial results]** C. Huang, A. Kotzig, A. Rosa. *Further results on tree labellings.* Utilitas Mathematica 21 (1982), 31–48.
- **[Partial results]** P. Bahls, S. Lake, A. Wertheim. *Gracefulness of families of spiders.* Involve 3 (2010), 241–247.
- **[Computational]** R. E. L. Aldred, B. D. McKay. *Graceful and harmonious labellings of trees.* Bulletin of the Institute of Combinatorics and its Applications 23 (1998), 69–72.
- **[Computational]** W. Fang. *A computational approach to the graceful tree conjecture.* arXiv:1003.3045, 2010.
- **[Relaxation]** F. Van Bussel. *Relaxed graceful labellings of trees.* Electronic Journal of Combinatorics 9 (2002), \#R4.
- **[Reformulation]** H. J. Broersma, C. Hoede. *Another equivalent of the graceful tree conjecture.* Ars Combinatoria 51 (1999), 183–192.
- **[Survey]** J. A. Gallian. *A Dynamic Survey of Graph Labeling.* Electronic Journal of Combinatorics, Dynamic Survey DS6 (updated annually).
- **[Survey]** M. Edwards, L. Howard. *A survey of graceful trees.* Atlantic Electronic Journal of Mathematics 1 (2006), 5–30.
- **[Survey]** J.-C. Bermond. *Graceful graphs, radio antennae and French windmills.* In *Graph Theory and Combinatorics*, Pitman, London, 1979, pp. 18–37.

## 10. Worked Example / Concrete Special Case

**The tree.** Let $T$ be the caterpillar with spine $s_1 s_2 s_3$, two leaves $x,y$ attached to $s_1$, one leaf $z$ on $s_2$, one leaf $w$ on $s_3$. Then $|V(T)| = 7$, $q = |E(T)| = 6$, and labels must be a bijection $V \to \{0,\dots,6\}$ with edge differences $\{1,\dots,6\}$.

**Rosa's zig-zag construction.** Maintain a low counter $a$ (starting $0$) and a high counter $b$ (starting $q=6$). Label $s_1 = 0$; assign its unlabeled neighbours the largest unused high labels; move to the next spine vertex and assign its unlabeled neighbours the smallest unused low labels; alternate.

- $f(s_1) = 0$.
- Neighbours of $s_1$: $f(x)=6$, $f(y)=5$, $f(s_2)=4$. Edge labels $6,5,4$.
- Neighbours of $s_2 = 4$ still unlabeled: $f(z)=1$, $f(s_3)=2$. Edge labels $|4-1|=3$, $|4-2|=2$.
- Neighbour of $s_3=2$: $f(w)=3$. Edge label $|2-3|=1$.

**Verification.**

$$f = \{s_1{\mapsto}0,\; z{\mapsto}1,\; s_3{\mapsto}2,\; w{\mapsto}3,\; s_2{\mapsto}4,\; y{\mapsto}5,\; x{\mapsto}6\}$$

Vertex labels $=\{0,1,2,3,4,5,6\}$, all distinct. Edge labels:
$$\{6,\,5,\,4,\,3,\,2,\,1\} = \{1,\dots,6\}. \checkmark$$

**It is even an $\alpha$-labeling.** The bipartition classes are $A=\{s_1,s_3,z\}$ with labels $\{0,2,1\}$ and $B=\{x,y,s_2,w\}$ with labels $\{6,5,4,3\}$. Taking $\lambda = 2$ we have $\max_{A} f = 2 < 3 = \min_{B} f$, so every edge straddles $\lambda$.

**Decomposition payoff.** By Rosa's theorem, the $13$ translates $v \mapsto f(v)+i \pmod{13}$, $i = 0,\dots,12$, give $13$ edge-disjoint copies of $T$ covering all $\binom{13}{2}=78 = 13\cdot 6$ edges of $K_{13}$. Because the labeling is an $\alpha$-labeling, $T$ additionally decomposes $K_{12k,12k}$ and $K_{12k+1}$ for every $k \ge 1$.

**Where the difficulty starts.** The zig-zag works because deleting the leaves of a caterpillar leaves a *path*, so the label alphabet can be consumed monotonically from both ends. For a lobster — delete the leaves and a caterpillar remains — the spine branches, two branches compete for the same low labels, and no ordering of the branch vertices is known to make the two counters meet exactly. That single failure of the alphabet-consumption argument is the elementary face of the obstacle described in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*