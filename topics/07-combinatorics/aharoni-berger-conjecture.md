---
id: 07-combinatorics/aharoni-berger-conjecture
title: "Aharoni–Berger Rainbow Matching Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Aharoni–Berger Rainbow Matching Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/aharoni-berger-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Aharoni–Berger, 2009).** Let $n \ge 1$ and let $M_1, \dots, M_n$ be matchings in a bipartite multigraph, each of size $|M_i| \ge n+1$. Then there exist edges $e_1 \in M_1, \dots, e_n \in M_n$ that are pairwise disjoint, i.e. $\{e_1,\dots,e_n\}$ is a *rainbow matching* of size $n$.

Equivalently, in colouring language: if the edges of a bipartite multigraph are coloured with $n$ colours so that each colour class is a matching of size at least $n+1$, the graph contains a matching of size $n$ using each colour exactly once.

The bound $n+1$ cannot be lowered to $n$: matchings of size $n$ can fail (Section 10). Whether $n+1$ is also sufficient in **general** (non-bipartite) multigraphs is a separate, false-as-stated question — there the correct threshold is conjectured to be $n+2$ for even $n$ (Aharoni–Berger–Chudnovsky–Howard–Seymour).

A complete proof must handle all $n$ and all bipartite multigraphs (parallel edges allowed, no bound on multiplicity). A disproof requires an explicit family $M_1,\dots,M_n$ of matchings of size $n+1$ whose maximum rainbow matching has size $\le n-1$.

## 2. Mathematical Foundations

Let $G = (A \cup B, E)$ be a bipartite multigraph with parts $A, B$. A **matching** $M \subseteq E$ is a set of pairwise vertex-disjoint edges. Given a family $\mathcal{M} = (M_1,\dots,M_m)$ of matchings, a **partial rainbow matching** is a set $R \subseteq E$ together with an injection $\varphi: R \to [m]$ such that $e \in M_{\varphi(e)}$ for all $e \in R$ and $R$ is a matching. Write
$$\rho(\mathcal{M}) = \max\{|R| : R \text{ is a partial rainbow matching of } \mathcal{M}\}.$$

Define the extremal function
$$f(n) = \min\{\, s : \text{every } n \text{ matchings of size } s \text{ in a bipartite multigraph satisfy } \rho \ge n \,\}.$$
The conjecture asserts $f(n) = n+1$; trivially $f(n) \ge n+1$.

**Latin-square specialisation.** An $n \times n$ Latin square $L$ over symbol set $[n]$ corresponds to the bipartite multigraph $K_{n,n}$ with $A$ = rows, $B$ = columns, edge $rc$ coloured by $L(r,c)$. Each colour class is a perfect matching of size $n$. A rainbow matching of size $k$ is a **partial transversal** of size $k$: $k$ cells in distinct rows, distinct columns, with distinct symbols. Thus:

- **Ryser's conjecture (1967):** every Latin square of odd order $n$ has a full transversal ($k=n$).
- **Brualdi–Stein conjecture:** every Latin square of order $n$ has a partial transversal of size $n-1$.

Taking $n-1$ of the $n$ colour classes, each of size $n = (n-1)+1$, the Aharoni–Berger conjecture applied with parameter $n-1$ yields a rainbow matching of size $n-1$, i.e. Brualdi–Stein. So Aharoni–Berger is a strict generalisation (it drops the assumption that the matchings live inside a single Latin square, allows unequal vertex sets, multigraphs, and matchings of size larger than the host).

**Topological tool.** The classical machinery here is the topological connectivity of the independence complex. For a graph $H$, let $\mathcal{I}(H)$ be the complex of independent sets and $\eta(H) = \eta(\mathcal{I}(H))$ its connectivity parameter. Aharoni–Berger–Ziv's theorem states: if $H$ has a vertex partition $V_1,\dots,V_m$ with $\eta(\mathcal{I}(H)) \ge m$, then there is an independent transversal. Applied to the line graph of $G$ with $V_i = M_i$, an independent set in the line graph is exactly a matching, so lower bounds on $\eta$ of the line-graph independence complex give rainbow matchings. Meshulam-type bounds give $\eta(\mathcal{I}(L(G))) \ge \nu(G)/2$ for general graphs and $\ge 2\nu(G)/3$ in the bipartite case, where $\nu$ is the matching number.

## 3. History & State of the Art (SOTA)

- **1967:** Ryser conjectures every odd-order Latin square has a transversal; Brualdi and later Stein propose the $n-1$ partial-transversal version.
- **1998:** Drisko proves that any $2n-1$ matchings of size $n$ in $K_{n,n}$ (row-Latin rectangles) admit a rainbow matching of size $n$, and that $2n-2$ does not suffice.
- **2007:** Aharoni, Berger and Ziv develop the topological independent-systems-of-representatives method, giving $\rho \ge$ roughly $2s/3$ from bipartite matchings of size $s$.
- **2009:** Aharoni and Berger state the conjecture in *Rainbow matchings in $r$-partite $r$-graphs*, as the natural "$n$ matchings of size $n+1$" strengthening of Brualdi–Stein.
- **2015–2017:** A sequence of quantitative improvements to $f(n)$: $\lfloor 7n/4 \rfloor$ (Aharoni–Charbit–Howard), $\lfloor 5n/3 \rfloor$ (Aharoni–Kotlar–Ziv), $3n/2 + o(n)$ (Clemens–Ehrenmüller).
- **2018:** Pokrovskiy proves the **approximate conjecture**: $f(n) \le n + o(n)$.
- **2019:** Aharoni, Berger, Chudnovsky, Howard, Seymour prove the tight general-graph analogue: $3n-2$ matchings of size $n$ force a rainbow matching of size $n$, and $3n-3$ do not.
- **2023:** Munhá Correia, Pokrovskiy and Sudakov sharpen the error term to $f(n) \le n + O(\log n / \log\log n)$, with substantially shorter proofs.
- **2023–2024:** Montgomery resolves the Ryser–Brualdi–Stein conjecture for all sufficiently large $n$ (transversal of size $n-1$ always; size $n$ for large odd $n$), settling the Latin-square special case asymptotically. *(frontier — verify)*

## 4. Partial Results / Verified Cases

| Setting | Guarantee | Source |
|---|---|---|
| Bipartite, matchings of size $2n-1$ | rainbow matching of size $n$; tight | Drisko 1998; Aharoni–Berger 2009 |
| General multigraphs, size $3n-2$ | size $n$; tight | Aharoni–Berger–Chudnovsky–Howard–Seymour 2019 |
| Bipartite, size $\lfloor 7n/4\rfloor$ | size $n$ | Aharoni–Charbit–Howard 2015 |
| Bipartite, size $3n/2 + o(n)$ | size $n$ | Clemens–Ehrenmüller 2016 |
| Bipartite, size $n + o(n)$ | size $n$ | Pokrovskiy 2018 |
| Bipartite, size $n + O(\log n/\log\log n)$ | size $n$ | Munhá Correia–Pokrovskiy–Sudakov 2023 |
| Latin squares, $n$ large | partial transversal of size $n-1$ | Montgomery 2023 *(frontier — verify)* |
| Simple bipartite graphs, matchings of size $n+1$, $n \le 3$ | conjecture holds | case analysis / Drisko for $n\le 2$ |
| Matchings of size $n+1$, all $M_i$ equal or nearly equal | holds by Hall-type argument | folklore |

Also verified: the "large $n$, bounded multiplicity, properly coloured multigraph" regime of Keevash–Yepremyan, and the random setting — a uniformly random $n\times n$ Latin square has a full transversal with high probability (Kwan; Kwan–Sah–Sawhney–Simkin give large-deviation counts).

Note the small-$n$ status is weak relative to the asymptotics: $2n-1$ equals $n+1$ only for $n\le 2$, and the $n+O(\log n/\log\log n)$ bounds are effective only for large $n$. The first genuinely open instance is small: $n = 4$ or $5$ with matchings of size $n+1$ has no published proof independent of the $2n-1$ bound.

## 5. Principal Obstacles

- **Topological ceiling.** The Aharoni–Berger–Ziv method converts the problem into a lower bound on $\eta(\mathcal{I}(L(G)))$. For line graphs of bipartite graphs the best available bound is $\eta \ge 2\nu/3$, and this is *tight* for the complex — the connectivity genuinely stops at $2/3$. So topology alone cannot go below matchings of size $3n/2$; the last factor is invisible to the method.
- **Greedy/augmentation loses a factor of 2.** Greedily extending a partial rainbow matching, each chosen edge blocks at most two edges of any later matching, giving only $\rho \ge \lceil s/2 \rceil$. Augmenting-path arguments (Pokrovskiy's) recover the constant but generate long alternating structures whose analysis leaks an additive error term.
- **The additive error is structural, not cosmetic.** In Pokrovskiy-type proofs one iteratively grows a rainbow matching by rerouting through "unused" colours; the argument needs a reservoir of spare edges of size roughly $\log n/\log\log n$ to guarantee progress at every step. Removing the reservoir requires an exact, non-iterative certificate — nothing of that kind is known.
- **Multigraphs defeat absorption.** Absorption and regularity arguments assume bounded multiplicity or a dense host; the conjecture allows $n$ matchings on as few as $2(n+1)$ vertices with arbitrary parallel edges, so there is no "sparse remainder to absorb".
- **No LP/entropy relaxation is tight.** The natural fractional relaxation (fractional rainbow matchings) is solved by a Hall-type criterion and gives $n+1 \Rightarrow n$ immediately; the integrality gap is precisely the difficulty, and there is no known rounding scheme that closes it.

## 6. The Gap

Proven: $f(n) \le n + C\log n/\log\log n$ for large $n$. Conjectured: $f(n) = n+1$. The gap is the additive term $C\log n/\log\log n - 1$.

Concretely, the missing step is: given $n$ matchings of size exactly $n+1$ and a maximum rainbow matching $R$ with $|R| = n-1$ (one colour $c$ unused), produce an augmentation using $M_c$. All $n+1$ edges of $M_c$ must meet $V(R)$, a set of $2n-2$ vertices, so a counting argument forces heavy overlap; the difficulty is that the alternating structure needed to swap $R$ around this overlap can be blocked by parity obstructions of exactly the kind that make even-order Latin squares transversal-free. Current proofs buy their way past this with slack; an exact proof must exploit that the *only* obstruction at threshold $n+1$ is the even Latin square, and no known invariant isolates it.

## 7. Current Research (as of June 2026)

- **Sudakov's group (ETH Zürich)** and collaborators (Munhá Correia, Pokrovskiy at UCL) continue to drive the additive error down; the technique is iterative absorption combined with "colour-switching" augmenting walks. *(frontier — verify)*
- **Montgomery (Warwick)** and the Latin-square community have shifted attention to full transversals and to counting transversals, following the resolution of Ryser–Brualdi–Stein for large $n$; the transfer of those methods to arbitrary matching families (where no Latin structure is available) is an active question. *(frontier — verify)*
- **Aharoni, Berger, Briggs, Holzman (Technion)** pursue the topological line, extending $\eta$-bounds to rainbow odd cycles, rainbow independent sets and rainbow cycle covers, seeking a connectivity notion that beats the $2/3$ barrier.
- **Small-case computation.** Exhaustive or SAT-based verification for $n = 4,5,6$ with matchings of size $n+1$ is feasible in principle but no published certificate exists; this is a low-hanging, unclaimed contribution.

## 8. Future Work

1. **Close the additive gap.** Replace the $\log n/\log\log n$ reservoir with a stability argument: show that a family with $\rho \le n-1$ must be $o(n)$-close to a Latin square of even order, then rule that structure out directly.
2. **Even/odd dichotomy.** Formulate and prove the general-graph version ($n+2$ for even $n$, $n+1$ for odd $n$) — the parity behaviour there may reveal the right invariant for the bipartite case.
3. **New connectivity parameter.** Find a homotopy-theoretic or matroidal invariant of $\mathcal{I}(L(G))$ that exceeds $2\nu/3$ for line graphs of bipartite multigraphs.
4. **Machine-checked small cases** for $n \le 7$, giving both confidence and possible extremal-structure hints.
5. **Matroid generalisation.** Rota's basis conjecture is the matroid cousin; a common framework covering both would be a major advance.

## 9. Key References

- **[Foundational]** R. Aharoni and E. Berger. *Rainbow matchings in $r$-partite $r$-graphs.* Electronic Journal of Combinatorics 16 (2009), \#R119.
- **[Foundational]** A. A. Drisko. *Transversals in row-Latin rectangles.* Journal of Combinatorial Theory, Series A 84 (1998), 181–195.
- **[Foundational]** R. Aharoni, E. Berger and R. Ziv. *Independent systems of representatives in weighted graphs.* Combinatorica 27 (2007), 253–267.
- **[SOTA]** A. Pokrovskiy. *An approximate version of a conjecture of Aharoni and Berger.* Advances in Mathematics 333 (2018), 1197–1241.
- **[SOTA]** D. Munhá Correia, A. Pokrovskiy and B. Sudakov. *Short proofs of rainbow matchings results.* International Mathematics Research Notices, 2023.
- **[SOTA]** R. Aharoni, E. Berger, M. Chudnovsky, D. Howard and P. Seymour. *Large rainbow matchings in general graphs.* European Journal of Combinatorics 79 (2019), 222–227.
- **[Partial]** R. Aharoni, P. Charbit and D. Howard. *On a generalization of the Ryser–Brualdi–Stein conjecture.* Journal of Graph Theory 78 (2015), 143–156.
- **[Partial]** D. Clemens and J. Ehrenmüller. *An improved bound on the sizes of matchings guaranteeing a rainbow matching.* Electronic Journal of Combinatorics 23 (2016), \#P2.11.
- **[Recent]** R. Montgomery. *A proof of the Ryser–Brualdi–Stein conjecture for large even $n$.* arXiv preprint, 2023.
- **[Survey]** I. M. Wanless. *Transversals in Latin squares: a survey.* In *Surveys in Combinatorics 2011*, London Math. Soc. Lecture Note Series 392, Cambridge University Press, 2011, 403–437.
- **[Survey]** A. Gyárfás and G. N. Sárközy. *Rainbow matchings and cycle-free partial transversals of Latin squares.* Discrete Mathematics 327 (2014), 96–102.

## 10. Worked Example / Concrete Special Case

**Why size $n$ fails ($n = 2$).** Take $A = \{a_1,a_2\}$, $B = \{b_1,b_2\}$ and the Latin square of order $2$:
$$L = \begin{pmatrix} 1 & 2 \\ 2 & 1\end{pmatrix}, \qquad M_1 = \{a_1b_1,\ a_2b_2\},\qquad M_2 = \{a_1b_2,\ a_2b_1\}.$$
Both have size $2 = n$. A rainbow matching of size $2$ needs one edge from each. Check all four pairs: $\{a_1b_1, a_1b_2\}$ shares $a_1$; $\{a_1b_1, a_2b_1\}$ shares $b_1$; $\{a_2b_2, a_1b_2\}$ shares $b_2$; $\{a_2b_2, a_2b_1\}$ shares $a_2$. So $\rho = 1 < 2$, and $f(2) \ge 3 = n+1$. The same construction from any even-order Latin square gives $f(n)\ge n+1$ for all even $n$; a padding argument extends it to odd $n$.

**The case $n = 2$ of the conjecture.** Let $M_1, M_2$ be matchings of size $3$. Pick any $e = a b \in M_1$. Edges of $M_2$ meeting $e$ must use $a$ or $b$; since $M_2$ is a matching it has at most one edge at $a$ and at most one at $b$, so at most $2$ edges of $M_2$ are blocked. As $|M_2| = 3 > 2$, some $f \in M_2$ is disjoint from $e$, and $\{e,f\}$ is a rainbow matching of size $2$. $\square$

**The trivial general bound and where it stops.** Repeating this greedily: having built a rainbow matching $\{e_1,\dots,e_k\}$ with $e_i\in M_i$, the next matching $M_{k+1}$ has at most $2k$ edges blocked, so if $|M_{k+1}| \ge 2k+1$ we can extend. With all matchings of size $s = n+1$ this succeeds while $2k+1 \le n+1$, i.e. up to
$$k = \left\lceil \tfrac{n}{2} \right\rceil,$$
giving $\rho \ge \lceil n/2\rceil$ — about half the conjectured value. Drisko's theorem removes the factor $2$ at the cost of doubling $s$ (matchings of size $2n-1$); Pokrovskiy's argument removes it at cost $o(n)$; the conjecture asks for it at cost $1$.

**Latin-square instance ($n=4$).** For the cyclic Latin square $L(r,c) = r + c \bmod 4$, the four colour classes are perfect matchings of $K_{4,4}$ of size $4$. Any full transversal would require cells $(r, \sigma(r))$ with $r+\sigma(r)$ all distinct mod $4$; summing, $\sum_r r + \sum_r \sigma(r) \equiv 0+1+2+3 \equiv 2 \pmod 4$ while the left side is $2 + 2 = 4 \equiv 0$ — contradiction. So $\rho = 3 = n-1$ exactly, matching Brualdi–Stein and confirming that the conjecture's guarantee (take $n-1 = 3$ matchings of size $4$, get a rainbow matching of size $3$) is sharp here.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*