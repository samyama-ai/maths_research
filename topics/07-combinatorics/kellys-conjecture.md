---
id: 07-combinatorics/kellys-conjecture
title: "Kelly's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kelly's Conjecture (Hamilton Decompositions of Regular Tournaments)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/kellys-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Kelly, 1968).** Every regular tournament on $n$ vertices can be decomposed into $(n-1)/2$ arc-disjoint Hamilton cycles.

A *tournament* is an orientation of the complete graph $K_n$: for every pair $u \neq v$ exactly one of the arcs $uv$, $vu$ is present. It is *regular* if every vertex has out-degree and in-degree equal to $(n-1)/2$, which forces $n$ to be odd. A *Hamilton cycle* is a directed cycle visiting every vertex exactly once; a *decomposition* is a partition of the arc set into such cycles.

The count is exactly tight: a regular tournament has $\binom{n}{2} = n(n-1)/2$ arcs and each Hamilton cycle uses $n$ arcs, so a decomposition must consist of precisely $(n-1)/2$ cycles and must leave no arc uncovered. There is no slack; the conjecture asserts a perfect packing, not an approximate one.

**Status.** Proved by Kühn and Osthus (2013) for all sufficiently large $n$. It remains open for small $n$ in the sense that the proof gives an ineffective threshold $n_0$; the conjecture as stated for *all* odd $n$ is not fully certified, though no counterexample exists and all small cases checked satisfy it.

**What a complete resolution requires.** Either (i) an argument valid for every odd $n$ (e.g. an explicit $n_0$ plus exhaustive verification below it), or (ii) a counterexample: a regular tournament whose arc set admits no partition into Hamilton cycles.

## 2. Mathematical Foundations

Let $G = (V,A)$ be a digraph on $n$ vertices, $N^+(v) = \{u : vu \in A\}$, $N^-(v) = \{u : uv \in A\}$, $d^\pm(v) = |N^\pm(v)|$. $G$ is $D$-regular if $d^+(v)=d^-(v)=D$ for all $v$.

**Tournaments.** $T$ is a tournament iff for all $u \ne v$, $\mathbf{1}[uv \in A] + \mathbf{1}[vu \in A] = 1$. Regularity gives
$$d^+(v) = d^-(v) = \frac{n-1}{2}, \qquad n \equiv 1 \pmod 2 .$$

**Decomposition.** A Hamilton decomposition is a family $\mathcal{H} = \{H_1,\dots,H_k\}$ of Hamilton cycles with
$$A(T) = \bigsqcup_{i=1}^{k} A(H_i), \qquad k = \frac{|A(T)|}{n} = \frac{n-1}{2}.$$

**Robust outexpansion** (the structural notion that carries the proof). For $0 < \nu \le \tau < 1$ and $S \subseteq V$, the $\nu$-robust outneighbourhood is
$$RN^+_{\nu}(S) \;=\; \{\, v \in V : |N^-(v) \cap S| \ge \nu n \,\}.$$
$G$ is a **robust $(\nu,\tau)$-outexpander** if
$$|RN^+_{\nu}(S)| \ \ge\ |S| + \nu n \qquad \text{for every } S \text{ with } \tau n \le |S| \le (1-\tau)n .$$
Robustness means expansion survives the deletion of a sparse digraph: removing $o(n)$ arcs at each vertex preserves the property with slightly weaker parameters. This is what allows Hamilton cycles to be extracted one after another without destroying the structure of the remainder.

**Key fact.** Every regular tournament on $n$ vertices is a robust $(\nu,\tau)$-outexpander for suitable constants $0 < \nu \ll \tau \ll 1$. Sketch: for $|S| \ge \tau n$, all but at most $O(1/\nu)$ vertices receive at least $\nu n$ arcs from $S$, because $\sum_{v}|N^-(v)\cap S| = e(S, V) \ge \binom{|S|}{2}$-type counting forces most in-degrees from $S$ to be linear.

**Main theorem used.** *(Kühn–Osthus 2013)* For every $\alpha > 0$ there exist $\nu, \tau, n_0$ such that every $D$-regular robust $(\nu,\tau)$-outexpander on $n \ge n_0$ vertices with $D$ linear in $n$ has a Hamilton decomposition. Applying this to $D = (n-1)/2$ yields Kelly's conjecture for large $n$.

**Related exact result.** The complete digraph $K^*_n$ (both arcs on every pair) has a Hamilton decomposition iff $n \notin \{4,6\}$ (Tillson, 1980) — a sharp reminder that small cases can genuinely fail in decomposition problems.

## 3. History & State of the Art (SOTA)

- **1968.** The conjecture is recorded as a problem of **P. Kelly** in J. W. Moon's monograph *Topics on Tournaments*. Motivation: a regular tournament models a round-robin schedule with balanced wins; the conjecture asks whether the schedule splits into balanced cyclic "rounds".
- **1970s.** Camion's theorem (every strongly connected tournament is Hamiltonian, 1959) and Moon's theorem (every strong tournament is vertex-pancyclic, 1966) give one Hamilton cycle for free but say nothing about disjointness.
- **1980.** Tillson decomposes $K^*_{2m}$ for $2m \ge 8$, establishing the "undirected-analogue" toolkit but not the tournament case.
- **1982.** **Thomassen** obtains the first infinite family of arc-disjoint Hamilton cycles in every regular tournament, a bound of order $n^{1/2}$ up to constants — far from the required $(n-1)/2$.
- **2010.** **Kühn, Osthus, Treglown** prove that every sufficiently large regular tournament contains at least $(1/8 - o(1))n$ arc-disjoint Hamilton cycles: the first result with the *correct order of magnitude*, i.e. a constant fraction of the optimum.
- **2012.** Approximate versions: every large regular tournament contains $(1/2 - o(1))n$ arc-disjoint Hamilton cycles, so all but a $o(1)$-fraction of the arcs can be covered. The remaining sparse "leftover" is the entire difficulty.
- **2013.** **Kühn and Osthus**, *Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments* (Advances in Mathematics 237, 62–146), prove the conjecture for all $n \ge n_0$, and in the far more general setting of regular robust outexpanders.
- **2014–2016.** The robust-expander machinery is exported: Hamilton decompositions of dense regular digraphs and graphs (Kühn–Osthus, JCTB 2014), and the proof of the 1-factorization conjecture and the Hamilton decomposition conjecture for dense graphs (Csaba, Kühn, Lo, Osthus, Treglown, Memoirs AMS, 2016).

**SOTA summary.** True for $n \ge n_0$ with $n_0$ ineffective (Szemerédi-regularity-based); true for all verified small cases; no explicit threshold known.

## 4. Partial Results / Verified Cases

| Class / range | Result |
|---|---|
| $n \ge n_0$, all regular tournaments | Full Hamilton decomposition (Kühn–Osthus 2013) |
| $D$-regular robust $(\nu,\tau)$-outexpanders, $D = \Theta(n)$, $n$ large | Full decomposition (same theorem) |
| Circulant (rotational) tournaments $C_n(1,2,\dots,\tfrac{n-1}{2})$, all odd $n$ | Explicit decomposition by jump classes; each jump $j$ with $\gcd(j,n)=1$ gives one Hamilton cycle, and jumps with $\gcd(j,n)=d>1$ are recombined |
| $n \in \{3,5,7,9\}$ | Exhaustive: $1, 1, 3, 15$ non-isomorphic regular tournaments respectively; all decompose |
| $n = 11$ | $1223$ non-isomorphic regular tournaments; computationally checked |
| Arbitrary regular tournaments, any $n$ | $\Omega(n^{1/2})$ arc-disjoint Hamilton cycles (Thomassen 1982) |
| Large regular tournaments | $\ge (1/8-o(1))n$ cycles (Kühn–Osthus–Treglown 2010); $(1/2-o(1))n$ in approximate form |
| Counting | The number of Hamilton decompositions of a regular tournament is $n^{(1+o(1))n^2/2}$ (Ferber–Long–Sudakov 2018) |

Near-regular tournaments (even $n$, degrees $n/2$ and $n/2-1$) admit the analogous statement: a decomposition into $n/2$ arc-disjoint Hamilton *paths*, also settled for large $n$ by the same machinery.

## 5. Principal Obstacles

- **No slack at the end.** Greedy/absorption arguments cover $(1-o(1))$ of the arcs easily. The obstruction is the *leftover* digraph $R$ of maximum degree $o(n)$: sparse digraphs are not expanders, are not robustly Hamiltonian, and generic extremal tools give nothing about them. Every partial result before 2013 stopped exactly here.
- **Regularity lemma cost.** The proof partitions $V$ via Szemerédi's regularity lemma for digraphs, then routes leftovers through a "robustly decomposable" reservoir digraph built in advance. The tower-type bound in the regularity lemma makes $n_0$ astronomical and non-explicit.
- **Parity/counting rigidity.** Because $|A(T)| = n \cdot \frac{n-1}{2}$ exactly, any local imbalance is fatal: one uncovered arc means no decomposition. Probabilistic arguments naturally produce near-perfect, not perfect, packings.
- **Failure of algebraic constructions.** Circulant tournaments decompose by group-theoretic jump arguments, but the overwhelming majority of regular tournaments (asymptotically almost all are asymmetric with trivial automorphism group) have no such symmetry.
- **Small cases are not tame.** Tillson's exceptions $K^*_4, K^*_6$ show that decomposition problems of this shape can have sporadic failures, so a soft argument covering all $n$ is unlikely to exist.

## 6. The Gap

Proved: the statement for $n \ge n_0$, plus explicit verification for $n \le 11$. Asserted: the statement for every odd $n$.

The gap is the interval $11 < n < n_0$. Two things are missing:

1. **An effective threshold.** Replacing the regularity lemma by a regularity-free absorption or expander-mixing argument would give an explicit $n_0$ — the current one is not merely large but not written down.
2. **A computationally reachable $n_0$.** The number of regular tournaments grows super-exponentially ($1223$ at $n=11$, then billions), so exhaustive verification is feasible only up to roughly $n \le 15$. Closing the gap by computation alone would need $n_0 \le 15$, which is far beyond any foreseeable quantitative improvement.

## 7. Current Research (as of June 2026)

- **Regularity-free proofs.** The main programme is to re-derive Hamilton decompositions of robust outexpanders using absorption and switching techniques only, targeting an explicit $n_0$ of size $2^{\mathrm{poly}(1/\alpha)}$ rather than a tower. *(frontier — verify)*
- **Lowering the degree threshold.** Extending decomposition results from linear-degree robust outexpanders to degrees $n^{1-\epsilon}$, or to sparse pseudorandom digraphs; this would also cover random regular tournament-like models. *(frontier — verify)*
- **Counting and typical structure.** Following Ferber–Long–Sudakov, work on the distribution of decompositions and on random greedy decomposition algorithms in digraphs.
- **Bipartite and Nash-Williams-type analogues.** Jackson-style conjectures on regular bipartite tournaments and packings of Hamilton cycles in regular oriented graphs of degree just above $3n/8$.
- **Groups.** Birmingham (Kühn, Osthus, Lo, and collaborators) remains the centre of the robust-expander programme; related activity at ETH Zürich, Oxford, IBS Korea, and Warwick.

## 8. Future Work

- Derive an explicit $n_0$ by replacing regularity with a hypergraph-matching or iterative-absorption framework.
- Find a *self-contained* proof for tournaments specifically, exploiting the complete-graph underlying structure (every pair is adjacent) rather than treating tournaments as generic expanders.
- Settle exact-degree analogues: what is the minimum semi-degree forcing a Hamilton decomposition in a regular oriented graph? The conjectured threshold is $3n/8$, matching the Keevash–Kühn–Osthus Hamiltonicity threshold.
- Develop practical algorithms: a polynomial-time algorithm that outputs a decomposition of any regular tournament, currently unavailable below $n_0$.
- Randomised verification: certify decomposability for random regular tournaments on moderate $n$ (say $n \le 10^3$) by SAT/flow-based methods, giving empirical support across the gap.

## 9. Key References

- **[Foundational]** J. W. Moon. *Topics on Tournaments.* Holt, Rinehart and Winston, New York, 1968. (Where Kelly's conjecture is recorded.)
- **[Foundational]** C. Thomassen. *Edge-disjoint Hamiltonian paths and cycles in tournaments.* Proceedings of the London Mathematical Society (3) 45 (1982), 151–168.
- **[Foundational]** T. W. Tillson. *A Hamiltonian decomposition of $K^*_{2m}$, $2m \ge 8$.* Journal of Combinatorial Theory Series B 29 (1980), 68–74.
- **[SOTA]** D. Kühn and D. Osthus. *Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments.* Advances in Mathematics 237 (2013), 62–146.
- **[SOTA]** D. Kühn, D. Osthus and A. Treglown. *Hamilton decompositions of regular tournaments.* Proceedings of the London Mathematical Society (3) 101 (2010), 303–335.
- **[SOTA]** D. Kühn and D. Osthus. *Hamilton decompositions of regular expanders: applications.* Journal of Combinatorial Theory Series B 104 (2014), 1–27.
- **[SOTA]** B. Csaba, D. Kühn, A. Lo, D. Osthus and A. Treglown. *Proof of the 1-factorization and Hamilton decomposition conjectures.* Memoirs of the American Mathematical Society 244 (2016), no. 1154.
- **[Recent]** A. Ferber, E. Long and B. Sudakov. *Counting Hamilton decompositions of oriented graphs.* International Mathematics Research Notices, 2018.
- **[Survey]** D. Kühn and D. Osthus. *A survey on Hamilton cycles in directed graphs.* European Journal of Combinatorics 33 (2012), 750–766.
- **[Survey]** J. Bang-Jensen and G. Gutin. *Digraphs: Theory, Algorithms and Applications.* 2nd edition, Springer, 2009.

## 10. Worked Example / Concrete Special Case

**Case $n = 5$.** Up to isomorphism there is exactly one regular tournament on $5$ vertices: the circulant $T_5 = C_5(1,2)$ on $V = \mathbb{Z}_5$, with arcs $i \to i+1$ and $i \to i+2 \pmod 5$. Each vertex has $d^+ = d^- = 2$, and $|A| = 10$. A decomposition must use $\frac{5-1}{2} = 2$ Hamilton cycles of $5$ arcs each.

Split by jump length:
$$H_1 : 0 \to 1 \to 2 \to 3 \to 4 \to 0 \quad (\text{all jumps } +1),$$
$$H_2 : 0 \to 2 \to 4 \to 1 \to 3 \to 0 \quad (\text{all jumps } +2).$$
$H_1$ is Hamilton since $\gcd(1,5)=1$; $H_2$ is Hamilton since $\gcd(2,5)=1$. Their arc sets are disjoint (different jump classes) and together contain all $10$ arcs. Decomposition verified.

**Case $n = 7$, circulant $C_7(1,2,3)$.** Jumps $1,2,3$ all satisfy $\gcd(j,7)=1$, so each jump class is itself a Hamilton cycle; e.g. the jump-$3$ cycle is
$$0 \to 3 \to 6 \to 2 \to 5 \to 1 \to 4 \to 0 .$$
Three cycles, $3 \cdot 7 = 21 = \binom{7}{2}$ arcs. Decomposition verified.

**Why this is not the general argument.** The jump trick needs $\gcd(j,n)=1$ for every $j \le (n-1)/2$, i.e. $n$ prime, *and* it needs the tournament to be circulant. At $n=9$ the jump-$3$ class of $C_9(1,2,3,4)$ splits into three triangles, not a Hamilton cycle, and must be recombined with another class; and $14$ of the $15$ regular tournaments on $9$ vertices are not circulant at all. Beyond $n=11$ almost every regular tournament has trivial automorphism group, and the only known route is the robust-expander machinery of Section 2.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*