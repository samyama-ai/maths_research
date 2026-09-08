---
id: 07-combinatorics/brualdi-ryser-stein-conjecture
title: "Brualdi–Ryser–Stein Conjecture on Latin Square Transversals"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brualdi–Ryser–Stein Conjecture on Latin Square Transversals

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/brualdi-ryser-stein-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $L$ be a Latin square of order $n$: an $n \times n$ array over symbol set $[n]=\{1,\dots,n\}$ in which every symbol occurs exactly once in each row and each column. A **partial transversal of size $k$** is a set of $k$ cells, no two sharing a row, a column, or a symbol. A **transversal** is a partial transversal of size $n$.

Three linked claims travel under one name:

- **(R) Ryser (1967).** Every Latin square of odd order $n$ has a transversal.
- **(B) Brualdi (1970s).** Every Latin square of order $n$ has a partial transversal of size $n-1$.
- **(S) Stein (1975).** Every $n \times n$ array filled with $n$ symbols, each occurring exactly $n$ times (an *equi-$n$-square*), has a partial transversal of size $n-1$.

(R) is sharp: the Cayley table of $\mathbb{Z}_{2m}$ has no transversal, so odd order is required. (B) is sharp for even $n$ by the same example. **(S) is false** (Pokrovskiy–Sudakov 2019). A complete resolution requires either a proof of (R) and (B) for *all* $n$, or a counterexample Latin square of odd order with no transversal, or of any order with maximum partial transversal $\le n-2$.

## 2. Mathematical Foundations

Identify $L$ with its set of $n^2$ triples
$$T(L) = \{(r,c,s) \in [n]^3 : L(r,c) = s\},$$
which is a set of $n^2$ triples meeting each *line* (each pair of coordinates fixed in two of the three axes) exactly once — equivalently, a **1-factorisation datum**. A partial transversal is a subset of $T(L)$ that is *rainbow* in all three coordinates.

**Graph reformulation.** Let $G_L$ be the tripartite 3-uniform hypergraph on $R \sqcup C \sqcup S$ with edges $T(L)$. A transversal is a perfect matching of $G_L$. Equivalently: colour the edges of $K_{n,n}$ (rows vs. columns) with $n$ colours, colour class $s$ being the perfect matching $\{rc : L(r,c)=s\}$; a transversal is a **rainbow perfect matching** of this properly $n$-edge-coloured $K_{n,n}$.

**Algebraic case.** For a group $G$ of order $n$ with Cayley table $L(x,y)=xy$, a transversal is a **complete mapping**: a bijection $\theta:G\to G$ such that $x \mapsto x\theta(x)$ is also a bijection. Existence is governed by the Hall–Paige criterion.

**Delta lemma / parity obstruction.** For $L = $ Cayley table of $\mathbb{Z}_n$ and a permutation $\sigma$ giving cells $(i,\sigma(i))$,
$$\sum_{i \in \mathbb{Z}_n} \bigl(i + \sigma(i)\bigr) = 2\binom{n}{2} = n(n-1) \pmod n,$$
while a rainbow set forces $\sum_{s\in\mathbb{Z}_n} s = n(n-1)/2 \pmod n$. For even $n$ these differ by $n/2 \not\equiv 0$, so no transversal exists.

**Counting.** Let $T(n)$ be the minimum number of transversals over Latin squares of odd order $n$. Taranenko (2015) proved the upper bound $\bigl((1+o(1))\,n/e^2\bigr)^n$ on the number of transversals of any order-$n$ Latin square; Glebov–Luria (2016) matched it asymptotically for the maximum.

## 3. History & State of the Art (SOTA)

- **1782.** Euler's work on Graeco-Latin squares: an orthogonal mate is a decomposition of $L$ into $n$ disjoint transversals.
- **1955.** Hall and Paige conjecture that a finite group has a complete mapping iff its Sylow 2-subgroup is trivial or non-cyclic.
- **1967.** Ryser states (R) in *Neuere Probleme der Kombinatorik*, together with the parity theorem that the number of transversals of an order-$n$ Latin square is congruent to $n \bmod 2$ for $n$ odd (proved for even $n$ by Balasubramanian, 1990: the count is even).
- **1969–1978, lower bounds on the largest partial transversal $\tau(L)$.** Koksma: $\tau \ge \lceil 2(n-1)/3 \rceil$. Drake (1977): $\tau \ge 3n/4$. Brouwer–de Vries–Wieringa (1978) and independently Woolbright (1978): $\tau \ge n - \sqrt{n}$.
- **1982.** Shor: $\tau \ge n - 5.53\log^2 n$ — a jump from polynomial to polylogarithmic deficiency. An error in the analysis was repaired by Hatami and Shor (2008), giving $\tau \ge n - 11.053\log^2 n$.
- **2019.** Pokrovskiy and Sudakov **disprove Stein's conjecture (S)**: equi-$n$-squares exist whose largest partial transversal has size $n - \Omega(\log n)$.
- **2022.** Keevash, Pokrovskiy, Sudakov, Yepremyan: $\tau \ge n - O(\log n/\log\log n)$, the first improvement past $\log^2$.
- **2023–2025.** Montgomery announces and circulates a proof of (R) and (B) for all sufficiently large $n$ *(frontier — verify)*.
- **Computation.** McKay, McLeod and Wanless (2006) enumerated transversal counts of all Latin squares of order $n \le 9$, confirming (R) and (B) in that range.

## 4. Partial Results / Verified Cases

- **All $n \le 9$:** exhaustive computation confirms every Latin square of order $\le 9$ has a partial transversal of size $n-1$, and every odd-order one has a transversal (McKay–McLeod–Wanless 2006; earlier work of Parker, Wallis).
- **Group-based Latin squares, all orders:** the Hall–Paige conjecture was proved by Wilcox, Evans and Bray (final case completed 2009, using the classification of finite simple groups). Every group of odd order has trivial Sylow 2-subgroup, hence a complete mapping, hence a transversal. So (R) holds for all Cayley tables.
- **Deficiency bound, all $n$:** $\tau(L) \ge n - O(\log n / \log\log n)$ unconditionally (Keevash–Pokrovskiy–Sudakov–Yepremyan 2022).
- **Almost all Latin squares:** Kwan (2020) showed a uniformly random Latin square of order $n$ has a transversal with probability $1-o(1)$; Eberhard, Manners and Mrazović (2019+) obtained asymptotics for the number of complete mappings of large groups, and Kwan–Sah–Sawhney–Simkin sharpened the random-square count.
- **Large $n$:** Montgomery's argument gives a transversal for odd $n \ge n_0$ and a partial transversal of size $n-1$ for all $n \ge n_0$, with $n_0$ not made explicit *(frontier — verify)*.
- **Structured families:** Latin squares that are $\varepsilon$-close to a group table, squares of order $n$ containing a $\lceil n/2 \rceil$-sized "generic" substructure, and Latin squares with bounded row-cycle structure admit direct arguments.

## 5. Principal Obstacles

- **No local certificate.** Transversal existence is a global perfect-matching condition on a 3-partite 3-uniform hypergraph. Such hypergraph matching problems are NP-hard in general, and the Latin condition is exactly the "line-regularity" that defeats generic Hall-type criteria — there is no known deficiency version of Hall's theorem for 3-uniform hypergraphs.
- **Parity is real but not decisive.** The $\mathbb{Z}_{2m}$ obstruction shows even-order failure is genuine, so any proof of (R) must consume the hypothesis "$n$ odd". Almost all counting and absorption techniques are parity-blind, so they can at best prove (B)-type deficiency bounds, never (R).
- **Randomised absorption plateaus.** The Rödl nibble plus absorption produces an almost-perfect rainbow matching missing $o(n)$ cells; converting to *exactly* $n$ or $n-1$ requires an absorber robust to arbitrary leftover symbol multisets. The KPSY bound $n - O(\log n/\log\log n)$ is precisely where the entropy of the leftover set stops shrinking under known switching arguments.
- **Stein's failure removes the natural generalisation.** The Pokrovskiy–Sudakov counterexample shows that the Latin condition, not merely symbol-frequency regularity, is essential. Any proof must exploit column-regularity, so purely "each symbol appears $n$ times" arguments — the setting in which most flexible probabilistic tools live — are provably insufficient.
- **Algebraic methods do not extend.** Hall–Paige is proved via CFSG and character theory on groups; a general Latin square is a quasigroup with no associativity, no subgroup lattice, and no representation theory to invoke.
- **Ineffective thresholds.** Large-$n$ proofs use regularity/absorption with tower-type or unspecified constants, leaving the mid-range $10 \le n \le n_0$ untouched and beyond exhaustive search (the number of order-11 Latin squares exceeds $10^{{26}}$).

## 6. The Gap

Proven: (i) the deficiency bound $n - O(\log n/\log\log n)$ for every $n$; (ii) full (R) and (B) for $n\le 9$; (iii) full (R) for Cayley tables of all groups; (iv) (R) and (B) for $n \ge n_0$ under Montgomery's argument.

Missing: closing the interval $9 < n < n_0$ with an *effective* argument, and (independently) a proof of (B) that removes the last $O(\log n/\log\log n)$ symbols by a method with explicit constants. The precise barrier is the **final-deficiency step**: given a rainbow matching of size $n - k$ with $k$ small, produce an augmenting structure of bounded length that increases the size by one. All current augmentation arguments need $k = \Omega(\log n/\log\log n)$ spare symbols to guarantee a switching path exists; at $k = O(1)$ the switching digraph can be shown to have no short cycle in adversarial instances, and the Stein counterexample shows no purely counting-based fix can work.

## 7. Current Research (as of June 2026)

- **Montgomery (Birmingham)** — large-$n$ resolution of (R) and (B) via a hierarchical absorption scheme combining rainbow-matching switchings with a distributive absorber; verification and simplification of the argument is ongoing *(frontier — verify)*.
- **Pokrovskiy (UCL), Sudakov (ETH Zürich), Keevash (Oxford), Yepremyan (Emory)** — extremal rainbow structures: rainbow Hamilton cycles, rainbow spanning trees, and the "many disjoint transversals" problem (does every odd-order Latin square have $n - o(n)$ disjoint transversals?).
- **Kwan (IST Austria), Sah, Sawhney, Simkin** — entropy and random-greedy methods for random Latin squares; counting transversals to within $e^{O(n)}$.
- **Wanless, Best, Hendrey, Wood (Monash)** — transversals in general Latin arrays and row-Latin arrays; computational classification of transversal-free structures.
- **Eberhard, Manners, Mrazović (Durham/Oxford/Zagreb)** — analytic number theory methods (circle method over groups) for counting complete mappings, extended toward quasigroups.
- **Effective versions.** A stated goal is an explicit $n_0$, or an SAT/SMT-assisted verification of (B) for $10 \le n \le 12$ using symmetry-reduced isotopy class representatives.

## 8. Future Work

- Extract an explicit $n_0$ from the large-$n$ proof and attack the residual range by computer search over main classes.
- Prove the **disjoint-transversal strengthening**: every Latin square of odd order decomposes a $(1-o(1))$-fraction of its cells into transversals. This would recover Ryser and connect to Euler's orthogonal-mate problem.
- Find a parity-sensitive invariant — a $\mathbb{Z}_2$-valued or Alon-style *Combinatorial Nullstellensatz* argument — that proves (R) for odd $n$ directly without absorption. Alon's polynomial method resolves related "rainbow" statements for prime $n$ and is the most promising algebraic route.
- Determine the truth of the corrected Stein-type statement: is $\tau \ge n - \Theta(\log n)$ tight for equi-$n$-squares?
- Extend Hall–Paige-style structure theory from groups to quasigroups with bounded associativity defect.

## 9. Key References

- **[Foundational]** H. J. Ryser. *Neuere Probleme der Kombinatorik.* In: Vorträge über Kombinatorik, Oberwolfach, Mathematisches Forschungsinstitut Oberwolfach, 1967, pp. 69–91.
- **[Foundational]** S. K. Stein. *Transversals of Latin squares and their generalizations.* Pacific Journal of Mathematics, 59(2):567–575, 1975.
- **[Foundational]** M. Hall and L. J. Paige. *Complete mappings of finite groups.* Pacific Journal of Mathematics, 5(4):541–549, 1955.
- **[Classical bound]** A. E. Brouwer, A. J. de Vries, R. M. A. Wieringa. *A lower bound for the length of partial transversals in a Latin square.* Nieuw Archief voor Wiskunde, 24(3):330–332, 1978.
- **[Classical bound]** D. E. Woolbright. *An $n \times n$ Latin square has a transversal with at least $n-\sqrt{n}$ distinct symbols.* Journal of Combinatorial Theory, Series A, 24(2):235–237, 1978.
- **[Classical bound]** P. W. Shor. *A lower bound for the length of a partial transversal in a Latin square.* Journal of Combinatorial Theory, Series A, 33(1):1–8, 1982.
- **[Correction]** P. Hatami and P. W. Shor. *A lower bound for the length of a partial transversal in a Latin square.* Journal of Combinatorial Theory, Series A, 115(7):1103–1113, 2008.
- **[SOTA]** P. Keevash, A. Pokrovskiy, B. Sudakov, L. Yepremyan. *New bounds for Ryser's conjecture and related problems.* Transactions of the American Mathematical Society, Series B, 9:288–321, 2022.
- **[SOTA]** A. Pokrovskiy and B. Sudakov. *A counterexample to Stein's Equi-$n$-square Conjecture.* Proceedings of the American Mathematical Society, 147(6):2281–2287, 2019.
- **[SOTA]** M. Kwan. *Almost all Steiner triple systems have perfect matchings.* Proceedings of the London Mathematical Society, 121(6):1468–1495, 2020. (Companion methods applied to Latin transversals.)
- **[Algebraic]** J. N. Bray, S. M. Wilcox, A. B. Evans. *The Hall–Paige conjecture, and synchronization for affine and diagonal groups* (and predecessors: S. M. Wilcox, *Reduction of the Hall–Paige conjecture to sporadic simple groups*, Journal of Algebra, 321(5):1407–1428, 2009).
- **[Computation]** B. D. McKay, J. C. McLeod, I. M. Wanless. *The number of transversals in a Latin square.* Designs, Codes and Cryptography, 40(3):269–284, 2006.
- **[Counting]** A. Taranenko. *Upper bounds on the numbers of 1-factors and 1-factorizations of hypergraphs.* Journal of Combinatorial Designs, 24(9):413–431, 2016.
- **[Survey]** I. M. Wanless. *Transversals in Latin squares: a survey.* In: Surveys in Combinatorics 2011, London Mathematical Society Lecture Note Series 392, Cambridge University Press, 2011, pp. 403–437.
- **[Frontier]** R. Montgomery. *A solution to Ryser's conjecture.* arXiv preprint, 2023 *(frontier — verify)*.

## 10. Worked Example / Concrete Special Case

Take $n=4$ and $L(i,j) = i+j \bmod 4$ on $\{0,1,2,3\}$:

$$
L = \begin{pmatrix}
0 & 1 & 2 & 3\\
1 & 2 & 3 & 0\\
2 & 3 & 0 & 1\\
3 & 0 & 1 & 2
\end{pmatrix}
$$

**No transversal.** A transversal picks cells $(i,\sigma(i))$ for a permutation $\sigma$ of $\{0,1,2,3\}$, with symbols $i+\sigma(i)$ all distinct. Summing the symbols mod 4 two ways:
$$\sum_{i} \bigl(i+\sigma(i)\bigr) \equiv 2(0+1+2+3) = 12 \equiv 0 \pmod 4,$$
$$\sum_{s \in \{0,1,2,3\}} s = 6 \equiv 2 \pmod 4.$$
Since $0 \ne 2$, no such $\sigma$ exists. This is the general even-order obstruction, and is why Ryser's conjecture is restricted to odd $n$.

**A partial transversal of size $n-1=3$.** Take cells $(0,0)$, $(1,1)$, $(2,3)$: rows $0,1,2$ distinct, columns $0,1,3$ distinct, symbols $0,2,1$ distinct. So Brualdi's bound is attained and is sharp here.

**Contrast at $n=3$ (odd).** For $L(i,j)=i+j \bmod 3$, take $\sigma = \mathrm{id}$: cells $(0,0),(1,1),(2,2)$ give symbols $0,2,1$ — all distinct. A transversal exists, consistent with (R). The parity computation now reads $2\cdot 3 = 6 \equiv 0$ and $0+1+2=3\equiv 0 \pmod 3$: the obstruction vanishes exactly because $n$ is odd.

**Why (S) fails but (B) may not.** Replace the Latin condition by "each symbol appears $n$ times". For $n=4$, fill the first two rows entirely with symbols $\{0,1\}$ (eight cells, four each) and the last two rows with $\{2,3\}$. Any partial transversal uses at most 2 cells from rows $\{0,1\}$ (only two symbols available) and at most 2 from rows $\{2,3\}$, so the bound $n-1=3$ is met but the argument is fragile; Pokrovskiy and Sudakov iterate this block idea at scale $\log n$ to push the maximum down to $n-\Omega(\log n)$. Latin squares cannot be blocked this way — column-regularity forbids a symbol from being confined to few rows — which isolates precisely the hypothesis any proof of (B) must use.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*