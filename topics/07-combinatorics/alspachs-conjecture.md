---
id: 07-combinatorics/alspachs-conjecture
title: "Alspach's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alspach's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/alspachs-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Alspach's conjecture asks when a complete graph can be cut into edge-disjoint cycles of arbitrarily prescribed lengths.

**Conjecture (Alspach, 1981).** Let $n \geq 3$ and let $m_1, m_2, \dots, m_t$ be integers with $3 \le m_i \le n$ for all $i$. Then:

- if $n$ is odd, $K_n$ admits a decomposition into cycles of lengths $m_1,\dots,m_t$ if and only if $\sum_{i=1}^{t} m_i = \binom{n}{2}$;
- if $n$ is even, $K_n - I$ (the complete graph minus a perfect matching $I$) admits such a decomposition if and only if $\sum_{i=1}^{t} m_i = \frac{n(n-2)}{2}$.

The "only if" direction is trivial: a cycle decomposition partitions the edge set, so the lengths must sum to the edge count, and no cycle in a simple graph on $n$ vertices is shorter than $3$ or longer than $n$. The content is that these obvious conditions are **sufficient** — no arithmetic, parity, or divisibility obstruction beyond edge counting exists.

A complete proof must produce, for every admissible list $(n; m_1,\dots,m_t)$, an explicit or existentially guaranteed decomposition. A disproof requires one admissible list with no decomposition. **The conjecture is now a theorem** (Bryant, Horsley & Pettersson, 2014), so the page records a solved problem together with its still-open generalisations.

## 2. Mathematical Foundations

Let $G = (V,E)$ be a finite simple graph. A **cycle** $C_m$ is a connected $2$-regular subgraph on $m \ge 3$ vertices. A **decomposition** of $G$ is a set $\{H_1,\dots,H_t\}$ of subgraphs with
$$E(G) = \bigsqcup_{i=1}^{t} E(H_i),$$
a disjoint union. If each $H_i \cong C_{m_i}$ we call it an $(m_1,\dots,m_t)$-**cycle decomposition**.

**Degree/parity constraint.** Every cycle contributes an even degree at each vertex it meets, so a graph with a cycle decomposition is necessarily even (all degrees even) — equivalently, Eulerian on each component. For $K_n$, $\deg(v) = n-1$, which is even exactly when $n$ is odd. For even $n$ one removes a $1$-factor $I$, leaving the $(n-2)$-regular graph $K_n - I$. This is why the conjecture splits into two cases. Veblen's theorem gives the converse for unspecified lengths: an even graph decomposes into cycles.

**Edge counts.**
$$|E(K_n)| = \frac{n(n-1)}{2}, \qquad |E(K_n - I)| = \frac{n(n-2)}{2}\ \ (n \text{ even}).$$

**Admissible list.** Call $(m_1,\dots,m_t)$ *admissible for $n$* if
$$3 \le m_i \le n \ \forall i \quad\text{and}\quad \sum_i m_i = \begin{cases} n(n-1)/2, & n \text{ odd},\\ n(n-2)/2, & n \text{ even}.\end{cases}$$

**Uniform case.** When $m_1 = \dots = m_t = m$, an $m$-cycle system of $K_n$ exists iff $n$ is odd, $m \le n$, and $m \mid \binom{n}{2}$ (resp. $n$ even, $m \mid \frac{n(n-2)}{2}$). Special cases: $m=3$ gives Steiner triple systems, existing iff $n \equiv 1, 3 \pmod 6$ (Kirkman, 1847); $m=n$ with $n$ odd gives Walecki's Hamilton decomposition of $K_n$ into $\frac{n-1}{2}$ Hamilton cycles.

**Standard toolkit.** Cyclic/rotational constructions using base blocks and difference sets in $\mathbb{Z}_n$; a cycle $(a_0,\dots,a_{m-1})$ generates the differences $\pm(a_{j+1}-a_j) \bmod n$, and covering each difference class once yields a decomposition of $K_n$. Other tools: $1$-factorisations, Latin squares, group divisible designs, and edge-colouring theorems (Vizing, Hall's theorem for systems of distinct representatives).

## 3. History & State of the Art (SOTA)

- **1847.** Kirkman constructs Steiner triple systems: the $m=3$ uniform case.
- **1890s.** Walecki's construction: $K_n$ ($n$ odd) decomposes into Hamilton cycles; $K_n - I$ ($n$ even) likewise.
- **1965–1966.** Kotzig and Rosa give cyclic constructions for $m$-cycle systems in congruence classes, notably Rosa's work on $(4k+2)$-gon decompositions.
- **1981.** Brian Alspach poses the general problem as Problem 3 in the "Research Problems" section of *Discrete Mathematics* 36 (1981), p. 333.
- **1989.** Hoffman, Lindner & Rodger reduce odd cycle systems to finitely many cases per congruence class.
- **2001.** Alspach & Gavlas settle the uniform case for all even $m$.
- **2002.** Šajna settles the uniform case for all odd $m$ (Cycle decompositions III). Together these give the full uniform-length theorem.
- **2003.** Alspach, Gavlas, Šajna & Vanden Eynden settle the directed uniform analogue for $K_n^{*}$.
- **2009–2010.** Bryant & Horsley handle decompositions into long cycles, then give an asymptotic solution valid for all sufficiently large $n$.
- **2014.** Bryant, Horsley & Pettersson prove the conjecture in full: *Cycle decompositions V*, Proc. London Math. Soc. **108** (2014), 1153–1192.

## 4. Partial Results / Verified Cases

Milestones along the route to the full theorem, each a genuine special class:

| Class | Result | Source |
|---|---|---|
| $m_i = 3$ for all $i$ | $n \equiv 1,3 \pmod 6$ | Kirkman 1847 |
| $m_i = n$ for all $i$ (Hamilton) | all $n \ge 3$ | Walecki, 1890s |
| $m_i = m$ uniform, $m$ even | all admissible $(n,m)$ | Alspach & Gavlas 2001 |
| $m_i = m$ uniform, $m$ odd | all admissible $(n,m)$ | Šajna 2002 |
| all $m_i$ large (long cycles) | admissible lists with all lengths above a linear threshold | Bryant & Horsley 2009 |
| all $n$ sufficiently large | asymptotic solution | Bryant & Horsley 2010 |
| $n \le 14$ and other small cases | exhaustive computation | Bryant & Horsley 2010 and earlier surveys |
| short even lengths | decompositions into cycles of bounded even length in general graphs | Horsley 2012 |
| **all admissible lists, all $n$** | **theorem** | **Bryant, Horsley & Pettersson 2014** |

Adjacent solved analogues: Tarsi (1983) proved the corresponding path-decomposition statement for complete multigraphs; the uniform directed case is closed (2003).

## 5. Principal Obstacles

The difficulty that kept the problem open for 33 years was **non-uniformity**, and it defeated each standard technique:

- **Algebraic constructions break.** Cyclic and rotational designs use base blocks whose orbits under $\mathbb{Z}_n$ produce many cycles *of the same length*. A list like $(3,3,4,5,\dots,n,n)$ with all lengths distinct has no group action to exploit; difference methods give no leverage.
- **Recursive/design-theoretic constructions break.** Group divisible designs and Wilson-type recursions build large decompositions from small ingredient designs, but they impose divisibility on the parts. Arbitrary length lists do not respect any modular structure, so the recursion has no closed family to induct on.
- **The parameter space is $2$-dimensional and unbounded.** For fixed $n$ the number of admissible lists is the number of partitions of $\binom{n}{2}$ into parts in $[3,n]$ — superpolynomial. No induction on $n$ alone can control it; one needs induction on the *multiset*, and removing one cycle from a decomposition can destroy the evenness that makes the residual graph decomposable at all.
- **Probabilistic and absorption methods fail at the exact edge count.** Random greedy / nibble arguments leave an uncontrolled remainder; here the decomposition must be perfect (zero leftover edges), so approximate methods must be paired with an exact completion step that was unavailable for mixed lengths.
- **Small cases resist.** Even the asymptotic result left a finite but computationally intractable window of $n$ where brute force is hopeless.

The 2014 proof succeeded by inducting on a much more general statement — decompositions of complete graphs *with a hole* / complete multipartite-type ambient graphs into cycles of arbitrary lengths — so that removing a cycle stays inside the induction class. This "strengthen the statement to make induction possible" move is the crux.

## 6. The Gap

For the original conjecture there is no remaining gap: the necessary counting conditions are sufficient, for all $n$ and all admissible lists. The frontier has moved to the generalisations, where the gap is real:

- **Complete multigraphs $\lambda K_n$.** Decomposing $\lambda K_n$ (each edge of multiplicity $\lambda$) into cycles of arbitrary specified lengths $3 \le m_i \le n$ with $\sum m_i = \lambda\binom{n}{2}$. Resolved for large families of $(\lambda, n)$ (Bryant, Horsley, Maenhaut & Smith, 2011) but not in complete generality.
- **Directed version.** Decomposing $K_n^{*}$ (both arcs on each pair) into directed cycles of arbitrary lengths $2 \le m_i \le n$. Only the uniform case is closed.
- **Complete multipartite graphs.** $K_{n_1,\dots,n_k}$ into cycles of arbitrary lengths — necessary conditions are known but sufficiency is open in general.
- **Fixed number of vertices used per cycle / packing versions**, and hypergraph analogues (tight-cycle decompositions of $K_n^{(3)}$), remain wide open.

## 7. Current Research (as of June 2026)

- **Monash University (Daniel Horsley) and University of Queensland (Darryn Bryant)** remain the centres of gravity, extending the 2014 machinery to multigraphs, graphs with holes, and packing/covering formulations.
- **University of Ottawa (Mateja Šajna)** continues work on directed and mixed cycle decompositions, and on Honeymoon Oberwolfach-type variants.
- **Absorption-based design theory** (following Keevash's and the Glock–Kühn–Lo–Osthus school's proofs of the existence conjecture for designs and of decompositions of quasirandom graphs) is being applied to arbitrary-length cycle decompositions of dense graphs beyond complete graphs — a plausible route to the multipartite case. *(frontier — verify)*
- **Reported progress on complete multipartite analogues of Alspach's conjecture** in recent preprints, extending known results on $K_{n_1,\dots,n_k}$ with equal parts. *(frontier — verify)*
- Computational design search (SAT/ILP and orderly generation) is used for small ingredient designs feeding recursive constructions.

## 8. Future Work

- **Unify the multigraph case.** Close the remaining $(\lambda,n)$ gaps left by the 2011 multigraph paper, ideally by porting the "hole" induction of *Cycle decompositions V*.
- **Directed arbitrary lengths.** Extend Alspach–Gavlas–Šajna–Vanden Eynden from uniform to arbitrary directed cycle lengths; the parity obstructions differ, since $2$-cycles are permitted.
- **General host graphs.** Characterise which even graphs $G$ decompose into cycles of arbitrary prescribed lengths; Horsley's short-even-cycle results suggest a density threshold statement.
- **Effective/algorithmic proofs.** The 2014 proof is existential in places; a polynomial-time algorithm constructing a decomposition from an admissible list is not known in general and would be of independent interest.
- **Hypergraph analogues.** Decompositions of $K_n^{(k)}$ into tight or loose cycles of prescribed lengths, where even the uniform case is largely open.

## 9. Key References

- **[Foundational]** B. Alspach. *Research Problems, Problem 3.* Discrete Mathematics **36** (1981), 333.
- **[Foundational]** T. P. Kirkman. *On a problem in combinations.* Cambridge and Dublin Mathematical Journal **2** (1847), 191–204.
- **[Partial]** B. Alspach and H. Gavlas. *Cycle decompositions of $K_n$ and $K_n - I$.* Journal of Combinatorial Theory, Series B **81** (2001), 77–99.
- **[Partial]** M. Šajna. *Cycle decompositions III: complete graphs and fixed length cycles.* Journal of Combinatorial Designs **10** (2002), 27–78.
- **[Partial]** B. Alspach, H. Gavlas, M. Šajna and H. Vanden Eynden. *Cycle decompositions IV: complete directed graphs and fixed length directed cycles.* Journal of Combinatorial Theory, Series A **103** (2003), 165–208.
- **[Partial]** D. Bryant and D. Horsley. *Decompositions of complete graphs into long cycles.* Bulletin of the London Mathematical Society **41** (2009), 927–934.
- **[Partial]** D. Bryant and D. Horsley. *An asymptotic solution to the cycle decomposition problem for complete graphs.* Journal of Combinatorial Theory, Series A **117** (2010), 1258–1284.
- **[SOTA / Solution]** D. Bryant, D. Horsley and W. Pettersson. *Cycle decompositions V: complete graphs into cycles of arbitrary lengths.* Proceedings of the London Mathematical Society **108** (2014), 1153–1192.
- **[Related]** D. Bryant, D. Horsley, B. Maenhaut and B. R. Smith. *Cycle decompositions of complete multigraphs.* Journal of Combinatorial Designs **19** (2011), 42–69.
- **[Related]** M. Tarsi. *Decomposition of a complete multigraph into simple paths: nonbalanced handcuffed designs.* Journal of Combinatorial Theory, Series A **34** (1983), 60–70.
- **[Related]** D. G. Hoffman, C. C. Lindner and C. A. Rodger. *On the construction of odd cycle systems.* Journal of Graph Theory **13** (1989), 417–426.
- **[Survey]** D. Bryant. *Cycle decompositions of complete graphs.* In *Surveys in Combinatorics 2007*, London Mathematical Society Lecture Note Series **346**, Cambridge University Press, 2007, 67–97.
- **[Survey]** D. Bryant and C. A. Rodger. *Cycle decompositions.* In *Handbook of Combinatorial Designs*, 2nd edition (C. J. Colbourn and J. H. Dinitz, eds.), Chapman & Hall/CRC, 2007, 373–382.

## 10. Worked Example / Concrete Special Case

**Instance: $n = 6$, lengths $(3,4,5)$.**

Since $n$ is even, the host graph is $K_6 - I$ with $V = \{0,1,2,3,4,5\}$ and $I = \{03, 14, 25\}$. Then
$$|E(K_6 - I)| = \frac{6 \cdot 4}{2} = 12 = 3 + 4 + 5,$$
and each length lies in $[3,6]$, so the list is admissible. Every vertex has degree $4$, which is even — the parity test passes.

The 12 edges are
$$\{01,02,04,05,\;12,13,15,\;23,24,\;34,35,\;45\}.$$

Build the decomposition greedily, longest-constraint-first:

1. **Triangle** $C_3 = (0,1,2)$ uses $01, 12, 02$.
   Remaining (9 edges): $04,05,13,15,23,24,34,35,45$.
2. **4-cycle** $C_4 = (3,4,5,1)$ uses $34, 45, 51, 13$. Note $(1,3,2,4)$ would fail — the edge $14$ lies in the removed matching $I$.
   Remaining (5 edges): $04,05,23,24,35$.
3. **Residual degrees**: $\deg(0)=2$ (via $04,05$), $\deg(2)=2$ ($23,24$), $\deg(3)=2$ ($23,35$), $\deg(4)=2$ ($04,24$), $\deg(5)=2$ ($05,35$), $\deg(1)=0$. The residue is $2$-regular on five vertices and connected, hence a single **5-cycle**: $(0,4,2,3,5)$.

Check: $\{01,12,02\} \sqcup \{34,45,15,13\} \sqcup \{04,42,23,35,50\}$ is exactly the 12-edge set, each edge once. The conjecture asserts that this kind of ad hoc success is never accidental: for *every* $n$ and every admissible list, a decomposition exists. For $n=6$ one can check all admissible partitions of $12$ into parts from $\{3,4,5,6\}$ — $(3,3,3,3)$, $(3,3,6)$, $(3,4,5)$, $(4,4,4)$, $(3,3,3,3)$, $(6,6)$, $(4,3,5)$, $(5,4,3)$, $(6,3,3)$, $(4,4,4)$ — and each is realisable, with $(6,6)$ being Walecki's Hamilton decomposition of $K_6 - I$ into two $6$-cycles.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*