---
id: 07-combinatorics/acyclic-edge-coloring-conjecture
title: "Acyclic Edge Coloring Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Acyclic Edge Coloring Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/acyclic-edge-coloring-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G$ be a finite simple graph with maximum degree $\Delta(G)$. A proper edge coloring of $G$ is **acyclic** if no cycle of $G$ receives exactly two colors. The **acyclic chromatic index** $a'(G)$ is the least number of colors in such a coloring.

**Conjecture (Fiamčík 1978; Alon, McDiarmid, Reed 1991).** Every graph $G$ satisfies
$$a'(G) \le \Delta(G) + 2 .$$

A complete proof must supply, for every simple graph, an acyclic proper edge coloring with $\Delta+2$ colors (or an efficient/existential argument establishing one). A disproof requires a single graph $G$ with $a'(G) \ge \Delta(G)+3$. The bound would be tight: $a'(K_4)=a'(K_{3,3})=5=\Delta+2$. Multigraphs are excluded — two parallel edges already force distinct colors and the analogous statement fails.

The problem is open for general graphs. The best unconditional bound is linear with a constant near $3.74$, not $1$.

## 2. Mathematical Foundations

Let $G=(V,E)$, $|V|=n$, $|E|=m$. A map $c: E \to [k]$ is **proper** if $c(e)\ne c(f)$ whenever $e\cap f \ne \emptyset$. For colors $i\ne j$ write
$$G_{ij} = \big(V,\; c^{-1}(i)\cup c^{-1}(j)\big).$$
Each $G_{ij}$ has maximum degree $\le 2$, so it is a disjoint union of paths and even cycles. Acyclicity is exactly the condition
$$\forall\, i\ne j:\quad G_{ij}\ \text{is a linear forest (acyclic)} .$$
Equivalently, $c$ is proper and no cycle of $G$ is 2-colored; the shortest possible bichromatic cycle has length $4$, so the constraint is a set of local conditions on cycles of even length $\ge 4$.

**Elementary bounds.**
$$\chi'(G)\ \le\ a'(G),\qquad \Delta \le \chi'(G)\le \Delta+1 \ \ (\text{Vizing}).$$
If $G$ is $\Delta$-regular then $a'(G)\ge \Delta+1$: a proper $\Delta$-edge coloring of a $\Delta$-regular graph partitions $E$ into $\Delta$ perfect matchings, and the union of any two perfect matchings is a disjoint union of even cycles, hence contains a bichromatic cycle.

**Counting lower bound.** Since every $G_{ij}$ is a forest on $n$ vertices, $|c^{-1}(i)|+|c^{-1}(j)|\le n-1$. Summing over all $\binom{k}{2}$ pairs with $k=a'(G)$ gives $(k-1)m \le \binom{k}{2}(n-1)$, i.e.
$$a'(G)\ \ge\ \frac{2m}{n-1} \quad\text{(so dense graphs need many colors).}$$

**Probabilistic frame.** Color each edge uniformly at random from $[k]$. For each pair of adjacent edges define a "properness" bad event, and for each cycle $C$ of even length $2\ell$ a bad event $A_C$ = "$C$ is 2-colored", with $\Pr[A_C] \le 2 k^{-(2\ell-2)}$ up to constants. The number of cycles of length $2\ell$ through a fixed edge is at most $\Delta^{2\ell-2}$, so the Lovász Local Lemma sum
$$\sum_{\ell\ge 2}\Delta^{2\ell-2}\cdot k^{-(2\ell-2)}$$
converges precisely when $k > C\Delta$ — the source of the linear-in-$\Delta$ constant that all current methods pay.

**Related invariant.** The vertex analogue, the acyclic chromatic number $a(G)$, satisfies $a(G)=O(\Delta^{4/3})$ and this is tight up to logarithmic factors (Alon, McDiarmid, Reed 1991); the edge version is conjecturally linear, which is what makes it delicate.

## 3. History & State of the Art (SOTA)

- **1978.** Fiamčík introduces the acyclic chromatic index and conjectures $a'(G)\le\Delta+2$.
- **1991.** Alon, McDiarmid and Reed, using the Lovász Local Lemma, prove $a'(G)\le 64\Delta$ — the first linear bound — and restate the conjecture.
- **1998.** Molloy and Reed sharpen the LLL analysis to $a'(G)\le 16\Delta$.
- **2001.** Alon, Sudakov and Zaks prove $a'(G)\le \Delta+2$ for graphs of girth at least $c\Delta\log\Delta$, and for almost all $\Delta$-regular graphs.
- **2002.** Alon and Zaks show that deciding $a'(G)\le 3$ is NP-complete, so no simple structural characterization is expected.
- **2012.** Ndreca, Procacci and Scoppola, via cluster-expansion / Shearer-type LLL refinements, obtain $a'(G)\le \lceil 9.62(\Delta-1)\rceil$.
- **2013.** Esperet and Parreau introduce **entropy compression** (Moser–Tardos-style algorithmic counting) for this problem: $a'(G)\le 4\Delta-4$.
- **2017.** Giotis, Kirousis, Psaromiligkos and Thilikos push the same machinery to $a'(G)\le \lceil 3.74(\Delta-1)\rceil+1$ — the current general record.
- **2017.** Cai, Perarnau, Reed and Watts obtain $a'(G)\le \lceil 3.569(\Delta-1)\rceil$ for large $\Delta$, and reduce the girth requirement for the tight bound from $c\Delta\log\Delta$ to $O(\log\Delta)$.

Progress since 2017 has been on structured classes (planar, degenerate, bounded girth) rather than on the general constant.

## 4. Partial Results / Verified Cases

- **Small maximum degree.** $\Delta\le 2$: trivial ($a'(G)\le 4$, and cycles need $3$ colors unless the length is divisible by... in fact $a'(C_n)=3$ for $n\ne 5$, $a'(C_5)=4$). $\Delta=3$: Skulrattanakulchai (2004) gives $a'(G)\le 5=\Delta+2$, with a linear-time algorithm. $\Delta=4$: Basavaraju and Chandran (2009) give $a'(G)\le 6=\Delta+2$.
- **Sparse / degenerate classes.** $2$-degenerate graphs satisfy $a'(G)\le\Delta+1$ (Basavaraju–Chandran 2009). Outerplanar and series-parallel graphs satisfy $a'(G)\le \Delta+1$ (Muthu, Narayanan, Subramanian 2006/2007).
- **Large girth.** Girth $\ge c\Delta\log\Delta$ implies $a'(G)\le\Delta+2$ (Alon–Sudakov–Zaks 2001); girth $\ge C\log\Delta$ suffices (Cai–Perarnau–Reed–Watts 2017). Girth $\ge 2\Delta\log\Delta$-type conditions also give $a'(G)=\Delta+1$ for non-regular graphs.
- **Planar graphs.** $a'(G)\le\Delta+12$ (Basavaraju, Chandran, Cohen, Havet, Müller 2011), improved to $\Delta+6$ and below under girth or triangle-distance restrictions in subsequent work; planar graphs of girth $\ge 5$ satisfy $a'(G)\le\Delta+1$ *(frontier — verify individual improvements)*.
- **Random graphs.** $a'(G_{n,p})$ and random $\Delta$-regular graphs satisfy the conjecture asymptotically almost surely.
- **Tight instances.** $a'(K_4)=a'(K_{3,3})=5$; $a'(K_n)\ge n+1$ for $n$ even, and $a'(K_n)\le n+2$ is known, showing the $+2$ slack is genuinely used.

## 5. Principal Obstacles

- **The LLL/entropy-compression constant is structural, not cosmetic.** Every probabilistic proof must simultaneously dominate bad events for bichromatic $4$-cycles, $6$-cycles, … For $2\ell$-cycles the count $\Delta^{2\ell-2}$ and the probability $k^{-(2\ell-2)}$ balance only when $k/\Delta$ exceeds a constant $>1$. Uniformly random colorings simply do not concentrate near $k=\Delta+2$; the union/LLL bound is false there, not merely unprovable. Getting to $\Delta+2$ requires a non-uniform measure or a global argument that no current framework supplies.
- **No useful discharging target.** Planar-style discharging works because Euler's formula bounds edge density. General graphs have no such reducible configuration list, and Alon–Zaks NP-completeness for $k=3$ rules out a finite forbidden-structure characterization.
- **Recoloring/augmenting-path methods break down.** Vizing-type fan and Kempe-chain arguments are the standard route to $\Delta+1$ for $\chi'$, but a Kempe swap on $G_{ij}$ can create a new bichromatic cycle in $G_{i\ell}$ elsewhere; there is no monotone potential function known that decreases under such swaps, so induction on edges stalls.
- **Density lower bound is nearly tight.** $a'(G)\ge 2m/(n-1)$ shows the conjecture is close to the extremal truth for dense graphs, leaving essentially no slack for lossy arguments.
- **Global vs. local.** A bichromatic cycle can have length $\Theta(n)$, so the constraint is not bounded-radius; local search / LLL arguments must handle unboundedly many event scales at once.

## 6. The Gap

Proven: $a'(G)\le \lceil 3.74(\Delta-1)\rceil+1$ for all graphs; $a'(G)\le\Delta+2$ when $\Delta\le 4$, when $G$ is $2$-degenerate or series-parallel, or when the girth is $\Omega(\log\Delta)$.

Conjectured: $a'(G)\le\Delta+2$ for all graphs, including graphs with many short cycles and $\Delta$ large.

The gap is a **multiplicative factor of roughly $3.74$**, and it is concentrated exactly on graphs with girth $O(1)$ and $\Delta\to\infty$ — dense neighborhoods where short even cycles are abundant. The missing step is a coloring method whose failure probability (or algorithmic termination measure) remains controllable when the number of colors is only $\Delta+2$, i.e. when each edge has just $3$ colors free after its neighbors are fixed. No known technique — LLL, entropy compression, semi-random "nibble", or algebraic Combinatorial Nullstellensatz methods — survives at that density.

## 7. Current Research (as of June 2026)

- **Refining entropy compression.** Groups at the National and Kapodistrian University of Athens (Kirousis, Giotis and coauthors) and at UFMG/Brazil (Procacci, Fialho, de Lima) continue to shave the constant using cluster-expansion criteria strictly stronger than the symmetric LLL. Gains since 2017 are fractions of a unit *(frontier — verify)*.
- **Girth reduction.** Following Cai–Perarnau–Reed–Watts, work at Waterloo/Birmingham aims to prove $a'(G)\le\Delta+2$ under a constant girth bound (e.g. girth $\ge 5$ or $\ge 7$) independent of $\Delta$ — widely seen as the most reachable major milestone.
- **Structured classes.** Chinese groups (Zhejiang Normal, Shandong) produce a steady stream of planar and sparse-graph results, driving planar bounds toward $a'(G)\le\Delta+2$ and proving $a'(G)=\Delta$ for planar graphs with large $\Delta$ and no short cycles *(frontier — verify)*.
- **List version.** The list acyclic chromatic index $a'_{\ell}(G)$ is conjectured to equal $a'(G)$-type bounds; current results give $a'_\ell(G)\le 4\Delta$-ish, and progress there tracks the non-list case.
- **Algorithmic angle.** Moser–Tardos derandomization and local-computation algorithms give near-linear-time constructions matching the $3.74\Delta$ bound; whether a $\Delta+2$ coloring, if it exists, is polynomially findable is open.

## 8. Future Work

- Prove $a'(G)\le\Delta+2$ for graphs of girth at least some absolute constant $g_0$, removing the $\Delta$-dependence entirely; this is the stated next target of the Reed school.
- Extend the $\Delta\le 4$ case-analysis to $\Delta=5,6$ via computer-assisted reducible-configuration search; a verified $\Delta=5$ proof would test whether discharging scales at all.
- Develop a non-uniform random coloring measure (weighting colorings by a cycle-avoiding Gibbs factor) so that the local-lemma criterion becomes satisfiable near $k=\Delta+2$.
- Settle the Alon–Sudakov–Zaks refinement: characterize which graphs actually need $\Delta+2$ rather than $\Delta+1$ colors.
- Improve the lower-bound side: exhibit a family with $a'(G)\ge\Delta+2$ and unbounded $\Delta$ beyond the complete/complete-bipartite examples, or prove none exists.

## 9. Key References

- **[Foundational]** N. Alon, C. J. H. McDiarmid, B. Reed. *Acyclic coloring of graphs.* Random Structures & Algorithms 2(3):277–288, 1991.
- **[Foundational]** J. Fiamčík. *The acyclic chromatic class of a graph.* Math. Slovaca 28:139–145, 1978.
- **[Foundational]** N. Alon, B. Sudakov, A. Zaks. *Acyclic edge colorings of graphs.* Journal of Graph Theory 37(3):157–167, 2001.
- **[Complexity]** N. Alon, A. Zaks. *Algorithmic aspects of acyclic edge colorings.* Algorithmica 32(4):611–614, 2002.
- **[Technique]** M. Molloy, B. Reed. *Further algorithmic aspects of the Local Lemma.* Proc. 30th ACM STOC, 524–529, 1998.
- **[SOTA]** L. Esperet, A. Parreau. *Acyclic edge-coloring using entropy compression.* European Journal of Combinatorics 34(6):1019–1027, 2013.
- **[SOTA]** I. Giotis, L. Kirousis, K. I. Psaromiligkos, D. M. Thilikos. *On the algorithmic Lovász Local Lemma and acyclic edge coloring.* / *Acyclic edge coloring through the Lovász Local Lemma.* Theoretical Computer Science 665:40–50, 2017.
- **[SOTA]** X. S. Cai, G. Perarnau, B. Reed, A. B. Watts. *Acyclic edge colourings of graphs with large girth.* Random Structures & Algorithms 50(4):511–533, 2017.
- **[SOTA]** S. Ndreca, A. Procacci, B. Scoppola. *Improved bounds on coloring of graphs.* European Journal of Combinatorics 33(4):592–609, 2012.
- **[Small $\Delta$]** S. Skulrattanakulchai. *Acyclic colorings of subcubic graphs.* Information Processing Letters 92(4):161–167, 2004.
- **[Small $\Delta$]** M. Basavaraju, L. S. Chandran. *Acyclic edge coloring of graphs with maximum degree 4.* Journal of Graph Theory 61(3):192–209, 2009.
- **[Planar]** M. Basavaraju, L. S. Chandran, N. Cohen, F. Havet, T. Müller. *Acyclic edge-coloring of planar graphs.* SIAM Journal on Discrete Mathematics 25(2):463–478, 2011.
- **[Survey]** N. Alon, J. H. Spencer. *The Probabilistic Method*, 4th ed. Wiley, 2016 (Chapter 5, Lovász Local Lemma and acyclic colorings).

## 10. Worked Example / Concrete Special Case

**Claim: $a'(K_4)=5=\Delta+2$.** Here $n=4$, $m=6$, $\Delta=3$, $\chi'(K_4)=3$.

*Lower bound.* First, $3$ colors fail: a proper $3$-edge-coloring of the $3$-regular graph $K_4$ splits $E$ into three perfect matchings $M_1,M_2,M_3$, and $M_1\cup M_2$ is a $4$-cycle — bichromatic.

Now suppose a proper acyclic coloring uses $4$ colors, with class sizes $s_1\ge s_2\ge s_3\ge s_4\ge 0$ and $\sum s_i = 6$. Each class is a matching in $K_4$, so $s_i\le 2$, and every matching of size $2$ in $K_4$ is a *perfect* matching. If two classes had size $2$ they would be two distinct perfect matchings whose union is a $4$-cycle, again bichromatic. Hence at most one class has size $2$, giving
$$\sum_i s_i \le 2+1+1+1 = 5 < 6,$$
a contradiction. So $a'(K_4)\ge 5$.

*Upper bound.* Label $V=\{1,2,3,4\}$ and color:
$$c(12)=1,\ c(34)=1,\ c(13)=2,\ c(14)=3,\ c(23)=4,\ c(24)=5.$$
Properness: at vertex $1$ the colors are $\{1,2,3\}$; at $2$, $\{1,4,5\}$; at $3$, $\{1,2,4\}$; at $4$, $\{1,3,5\}$ — all distinct. Acyclicity: only color $1$ has two edges, and $\{12,34\}$ is a perfect matching; a bichromatic cycle would need $\ge 2$ edges of each of two colors, impossible since classes $2,3,4,5$ are singletons. Hence $a'(K_4)=5$.

The same argument on $K_{3,3}$ ($\Delta=3$, $m=9$, $n=6$) gives $a'(K_{3,3})=5$. These are the canonical certificates that the conjectured bound $\Delta+2$ cannot be lowered to $\Delta+1$, and the counting bound $a'(G)\ge 2m/(n-1) = 12/3 = 4$ for $K_4$ shows how close the density obstruction already comes to the truth.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*