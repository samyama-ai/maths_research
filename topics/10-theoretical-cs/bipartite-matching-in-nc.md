---
id: 10-theoretical-cs/bipartite-matching-in-nc
title: "Bipartite Matching in NC"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bipartite Matching in NC

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/bipartite-matching-in-nc` · **Status:** open

## 1. Problem Statement / Conjecture

**Question.** Is the bipartite perfect matching problem in $\mathsf{NC}$?

Given a bipartite graph $G = (U \sqcup V, E)$ with $|U| = |V| = n$, decide whether $G$ has a perfect matching, and — in the search version — output one. A positive answer requires a deterministic parallel algorithm running in time $\log^{O(1)} n$ on $n^{O(1)}$ processors (PRAM), equivalently a uniform Boolean circuit family of depth $\log^{O(1)} n$ and polynomial size.

The problem is open in both the **search** and the **decision** form. It is *not* open whether matching is efficiently parallelizable with randomness: matching is in $\mathsf{RNC}$ (Karp–Upfal–Wigderson 1986; Mulmuley–Vazirani–Vazirani 1987). The conjecture that most researchers hold is $\mathsf{RNC} = \mathsf{NC}$ restricted to this instance:

> **Conjecture.** Bipartite perfect matching (search version) is in $\mathsf{NC}^2$.

A complete resolution is either (a) a deterministic $\log^{O(1)} n$-depth, $n^{O(1)}$-size circuit family solving it, or (b) an unconditional lower bound separating it from $\mathsf{NC}$ — which, since the problem is in $\mathsf{P}$, would separate $\mathsf{NC}$ from $\mathsf{P}$ and is far beyond current technique.

## 2. Mathematical Foundations

**Complexity classes.** $\mathsf{NC}^k$ = languages decided by uniform Boolean circuits of depth $O(\log^k n)$ and size $n^{O(1)}$; $\mathsf{NC} = \bigcup_k \mathsf{NC}^k$. $\mathsf{RNC}$ allows randomness with one-sided error. **Quasi-$\mathsf{NC}^k$** relaxes size to $2^{\log^{O(1)} n}$ while keeping depth $O(\log^k n)$.

**Algebraic handle.** For bipartite $G$ with parts $\{u_1,\dots,u_n\}, \{v_1,\dots,v_n\}$, the *Edmonds matrix* is
$$A(x)_{ij} = \begin{cases} x_{ij} & (u_i,v_j) \in E,\\ 0 & \text{otherwise},\end{cases}$$
with indeterminates $x_{ij}$. Then
$$\det A(x) = \sum_{\sigma \in \mathfrak{S}_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} A(x)_{i\sigma(i)},$$
and each nonzero term corresponds to a perfect matching. Since the monomials are distinct, no cancellation occurs, so $G$ has a perfect matching iff $\det A(x) \not\equiv 0$ (Edmonds 1967; Lovász 1979). Determinants of $n \times n$ matrices are computable in $\mathsf{NC}^2$ (Csanky 1976; Berkowitz 1984), so the only obstruction is evaluating a formal polynomial identity.

**Isolation.** Substituting random values gives $\mathsf{RNC}$ decision by Schwartz–Zippel. For search, MVV assign integer weights $w: E \to \{1,\dots,W\}$ and set $A_{ij} = 2^{w(u_i,v_j)}$. Write $\det A = 2^{w^\ast} \cdot c$ with $c$ odd, where $w^\ast$ is the minimum weight of a perfect matching, *provided the minimum-weight perfect matching $M$ is unique*. Then, for each edge $e = (u_i, v_j)$,
$$e \in M \iff \frac{\det A^{(ij)} \cdot 2^{w(e)}}{2^{w^\ast}} \ \text{ is odd},$$
where $A^{(ij)}$ deletes row $i$ and column $j$. All $n^2$ minors are computable in parallel in $\mathsf{NC}^2$ (matrix inversion / adjugate), so **search reduces to isolation**.

**Isolation Lemma (Mulmuley–Vazirani–Vazirani 1987).** For any set family $\mathcal{F} \subseteq 2^{E}$ with $|E| = m$, if $w(e)$ is drawn uniformly and independently from $\{1,\dots,2m\}$, then
$$\Pr_w[\ \exists\ \text{unique minimum-weight } S \in \mathcal{F}\ ] \ \ge\ 1/2 .$$

**Polytope reformulation.** The perfect matching polytope of a bipartite graph is
$$PM(G) = \Big\{ x \in \mathbb{R}^E_{\ge 0} \ :\ \textstyle\sum_{e \ni u} x_e = 1 \ \ \forall u \in U \sqcup V \Big\},$$
integral by Birkhoff–von Neumann. Isolating a matching means choosing $w$ so that $\min_{x \in PM(G)} \langle w, x\rangle$ is attained at a unique vertex. Equivalently, in the *cycle-space* formulation: $w$ isolates iff every cycle $C$ in $G$ has nonzero *circulation*
$$\operatorname{circ}_w(C) = \sum_{e \in C^+} w(e) - \sum_{e \in C^-} w(e) \neq 0,$$
where $C^\pm$ alternate around $C$. This is the object FGT attack.

## 3. History & State of the Art (SOTA)

- **1965–1967.** Edmonds gives the blossom algorithm and the determinant characterization; sequential polynomial time is settled.
- **1979.** Lovász: randomized decision via determinant evaluation, placing bipartite matching decision in $\mathsf{RNC}^2$.
- **1985.** Cook's taxonomy of parallel problems lists matching as the flagship $\mathsf{RNC}$-but-not-known-$\mathsf{NC}$ problem. *Lexicographically first* maximal matching is $\mathsf{P}$-complete (Cook), which is a warning against greedy approaches — but does not obstruct general matching.
- **1986.** Karp, Upfal, Wigderson: perfect matching *search* in $\mathsf{RNC}$, via a nonconstructive but parallel reduction.
- **1987.** MVV: the Isolation Lemma; search in $\mathsf{RNC}^2$ using $O(\log n)$ random bits per edge and only matrix inversion.
- **1995.** Chari, Rohatgi, Srinivasan reduce the randomness to $O(\log^2 n)$ bits total for isolation, still not $O(\log n)$.
- **2016 (breakthrough).** Fenner, Gurjar, Thierauf: **bipartite perfect matching is in quasi-$\mathsf{NC}^2$** — depth $O(\log^2 n)$, size $n^{O(\log^2 n)}$ — by a deterministic $O(\log^2 n)$-round construction of weight functions killing all small circulations.
- **2017.** Svensson and Tarnawski extend to **general (non-bipartite) graphs in quasi-$\mathsf{NC}$**. Goldwasser and Grossman give a *pseudo-deterministic* $\mathsf{RNC}$ algorithm: randomized, but outputs the same canonical matching with high probability.
- **2018–2020.** Anari and Vazirani: **planar perfect matching in $\mathsf{NC}$** (search), resolving a question open since 1985; and a general reduction showing search is $\mathsf{NC}$-equivalent to decision for matching.

**SOTA summary.** Best deterministic parallel bound: quasi-$\mathsf{NC}^2$. Best $\mathsf{NC}$ results: restricted graph classes. No hardness result rules out $\mathsf{NC}$.

## 4. Partial Results / Verified Cases

Bipartite (or general) matching is known in $\mathsf{NC}$ for:

- **Planar bipartite graphs.** Miller–Naor (1995) via planar flow; Datta, Kulkarni, Roy (2010) give a deterministic isolating weight function of $O(\log n)$ bits using face-cycle circulations, putting the problem in $\mathsf{SPL} \subseteq \mathsf{NC}^2$.
- **General planar graphs.** Anari–Vazirani (JACM 2020) — search version, the strongest topological case known.
- **One-crossing-minor-free graphs** (excluding $K_5$, $K_{3,3}$, $K_6$-minus-an-edge, or the Vámos-type single-crossing minors): Eppstein–Vazirani (2021). Earlier, $K_{3,3}$-free and $K_5$-free bipartite graphs: Arora, Gurjar, Tewari (STACS 2016).
- **Polynomially bounded permanent.** If $\operatorname{perm}(A) = n^{O(1)}$, i.e. the number of perfect matchings is polynomial, matching is in $\mathsf{NC}^2$ (Grigoriev–Karpinski 1987; Agrawal, Hoang, Thierauf 2007). More generally Anari–Vazirani: $\mathsf{NC}$ whenever the number of perfect matchings is $n^{O(1)}$.
- **Unique perfect matching / small-degree structure.** Kozen, Vazirani, Vazirani (1985): testing uniqueness and finding the matching when unique is in $\mathsf{NC}$; also comparability and interval graphs. Hoang, Mahajan, Thierauf (2006) place bipartite unique matching in $\mathsf{SPL}$-type classes.
- **Chordal and strongly chordal graphs.** Dahlhaus–Karpinski (1998).
- **Dense graphs**, e.g. minimum degree $\ge n/2$ (Dirac-type): a perfect matching can be built greedily in $\mathsf{NC}$.
- **Matroid generalizations.** Linear matroid intersection is in quasi-$\mathsf{NC}$ (Gurjar–Thierauf 2017); polytopes with totally unimodular faces admit quasi-$\mathsf{NC}$ isolation (Gurjar, Thierauf, Vishnoi 2018).
- **Parameter range.** FGT achieves depth $O(\log^2 n)$ with $n^{O(\log^2 n)}$ processors — polynomial only for graphs where the relevant cycle space has $\log^{O(1)}$-bounded "rank growth".

## 5. Principal Obstacles

- **Isolation is the whole problem, and it is information-theoretically tight in the wrong direction.** MVV needs $\Theta(m \log m)$ random bits naively. Any $\mathsf{NC}$ isolating scheme must produce, deterministically, a weight function with $O(\log n)$-bit weights (weights must fit in the determinant's bit budget) that kills all $2^{\Omega(n)}$ potential ties. Counting arguments show a *single* small-range weight function cannot work for all graphs; one needs a polynomial-size family plus a parallel way to select the good member — and verifying "did I isolate?" is itself only known via the determinant, which gives a test but not a search.
- **The FGT recursion loses a $\log$ factor per round.** FGT build $w_1, w_2, \dots$ where $w_i$ kills all cycles of circulation-support up to $2^i$ in the graph of tight edges. Each round multiplies the number of candidate weight functions by $n^{O(1)}$ and there are $\Theta(\log n)$ rounds, giving $n^{O(\log n)}$ — and $n^{O(\log^2 n)}$ with the bookkeeping. Collapsing the recursion to $O(1)$ rounds, or reusing randomness across rounds, is the open technical step. No known pseudorandom generator fools the "min-weight-matching-is-unique" predicate, which is not a small-depth circuit predicate in any usable sense.
- **Derandomization tools do not apply.** The predicate "$\det A \ne 0$ over $\mathbb{Z}$" is polynomial identity testing for a *determinantal* polynomial; unconditional PIT derandomization would give circuit lower bounds (Kabanets–Impagliazzo), so a black-box route is blocked. Bipartite matching is a special, highly structured PIT instance, but no one has exploited the structure enough to escape.
- **No canonical matching.** $\mathsf{NC}$ algorithms typically need a canonical object computable locally. The lexicographically-first matching is $\mathsf{P}$-complete, so the natural canonicalization is unusable; Goldwasser–Grossman's pseudo-deterministic result shows a canonical matching exists computably *with* randomness, but not without.
- **Topological methods do not scale.** Planar cases use the face lattice: the cycle space has an $O(n)$ basis of faces with a consistent orientation, so circulations can be forced nonzero by a short, explicit weight assignment. In genus-$g$ or minor-free-but-not-planar graphs the basis loses this locality; for general bipartite graphs the cycle space has no bounded-complexity generating set to attack.

## 6. The Gap

Proven: quasi-$\mathsf{NC}^2$, i.e. depth $O(\log^2 n)$ with $n^{O(\log^2 n)}$ size. Wanted: the same depth with $n^{O(1)}$ size. The entire gap is the **size of the isolating weight family**.

Precisely: does there exist a deterministically, $\mathsf{NC}$-computable family $W = \{w_1,\dots,w_{n^{O(1)}}\}$ of weight functions $E \to \{1,\dots,n^{O(1)}\}$ such that for every bipartite $G$ on $n$ vertices with a perfect matching, some $w_i \in W$ isolates a unique minimum-weight perfect matching? Existence of such $W$ follows from the probabilistic method with $|W| = O(n)$ — the obstruction is *explicitness*, plus a parallel selection rule. FGT prove the analogous statement with $|W| = n^{O(\log^2 n)}$. Shrinking the round count of the FGT recursion from $\Theta(\log n)$ to $O(1)$, or replacing the fresh weight function at each round with a re-used seed, would close the gap.

## 7. Current Research (as of June 2026)

- **Lattice and polytope isolation.** Gurjar, Thierauf, Vishnoi's programme — isolate a vertex of a $0/1$ polytope whose faces are totally unimodular — is the leading structural abstraction. Active at IIT Bombay (Gurjar), Ulm (Thierauf), EPFL (Svensson).
- **Matching-covered graph theory.** The tight-cut decomposition and Lovász's ear-decomposition theory are being revisited as a source of a canonical, $\mathsf{NC}$-computable object; work at Waterloo and IIT Kanpur. *(frontier — verify)*
- **Bounded genus and low-treewidth bridges.** Extending Anari–Vazirani planarity to genus $g = O(\log n)$ and to $H$-minor-free classes. Partial results for bounded genus exist; a full $\mathsf{NC}$ algorithm for all bounded-genus graphs is claimed in preprint form. *(frontier — verify)*
- **Pseudo-deterministic complexity.** Goldwasser–Grossman's line, developed further by Grossman, Holden and others, asks for randomized $\mathsf{NC}$ algorithms with canonical output; some see this as the last stop before full derandomization.
- **Lower bounds.** Monotone and bounded-depth circuit lower bounds for matching (Raz–Wigderson's $\Omega(n)$ monotone depth bound, 1992) are strong but do not touch $\mathsf{NC}$, since matching algorithms use non-monotone determinant computation essentially.

## 8. Future Work

- Reduce the FGT recursion depth: find weight functions that kill *all* circulation lengths simultaneously via a single algebraic object (e.g. a Reed–Solomon-type or lattice-based construction) rather than iteratively.
- Prove an $\mathsf{NC}$ reduction from bipartite matching to a linear-algebraic problem whose PIT instance is known-explicitly derandomizable (e.g. read-once oblivious ABPs, non-commutative ABPs).
- Settle the *decision* version separately — no known argument shows decision is as hard as search for the derandomization question, though Anari–Vazirani show $\mathsf{NC}$ equivalence.
- Prove or refute: bipartite matching is in $\mathsf{quasi\text{-}NC}^1$, or in $\mathsf{DET}$-relative deterministic logspace-uniform classes.
- Extend isolation to general $0/1$ polytopes with polynomial-size extended formulations, which would cover matching, matroid intersection, and flow simultaneously.

## 9. Key References

- **[Foundational]** Jack Edmonds. *Systems of distinct representatives and linear algebra.* Journal of Research of the National Bureau of Standards 71B, 1967.
- **[Foundational]** László Lovász. *On determinants, matchings, and random algorithms.* Fundamentals of Computation Theory (FCT), Akademie-Verlag, 1979.
- **[Foundational]** Richard M. Karp, Eli Upfal, Avi Wigderson. *Constructing a perfect matching is in random NC.* Combinatorica 6(1):35–48, 1986.
- **[Foundational]** Ketan Mulmuley, Umesh V. Vazirani, Vijay V. Vazirani. *Matching is as easy as matrix inversion.* Combinatorica 7(1):105–113, 1987.
- **[Foundational]** Stephen A. Cook. *A taxonomy of problems with fast parallel algorithms.* Information and Control 64(1–3):2–22, 1985.
- **[SOTA]** Stephen Fenner, Rohit Gurjar, Thomas Thierauf. *Bipartite perfect matching is in quasi-NC.* STOC 2016, pp. 754–763; SIAM Journal on Computing 50(3), 2021.
- **[SOTA]** Ola Svensson, Jakub Tarnawski. *The matching problem in general graphs is in quasi-NC.* FOCS 2017, pp. 696–707.
- **[SOTA]** Nima Anari, Vijay V. Vazirani. *Planar graph perfect matching is in NC.* Journal of the ACM 67(4), Article 21, 2020 (FOCS 2018).
- **[SOTA]** Nima Anari, Vijay V. Vazirani. *Matching is as easy as the decision problem, in the NC model.* ITCS 2020.
- **[Recent]** Shafi Goldwasser, Ofer Grossman. *Bipartite perfect matching in pseudo-deterministic NC.* ICALP 2017.
- **[Recent]** Rohit Gurjar, Thomas Thierauf, Nisheeth K. Vishnoi. *Isolating a vertex via lattices: polytopes with totally unimodular faces.* ICALP 2018; SIAM Journal on Computing 51(2), 2022.
- **[Recent]** David Eppstein, Vijay V. Vazirani. *NC algorithms for computing a perfect matching and a maximum flow in one-crossing-minor-free graphs.* SIAM Journal on Computing 50(3), 2021.
- **[Partial]** Samir Datta, Raghav Kulkarni, Sambuddha Roy. *Deterministically isolating a perfect matching in bipartite planar graphs.* Theory of Computing Systems 47(3):737–757, 2010.
- **[Partial]** Dima Grigoriev, Marek Karpinski. *The matching problem for bipartite graphs with polynomially bounded permanents is in NC.* FOCS 1987, pp. 166–172.
- **[Partial]** Suresh Chari, Pankaj Rohatgi, Aravind Srinivasan. *Randomness-optimal unique element isolation with applications to perfect matching and related problems.* SIAM Journal on Computing 24(5):1036–1050, 1995.
- **[Lower bound]** Ran Raz, Avi Wigderson. *Monotone circuits for matching require linear depth.* Journal of the ACM 39(3):736–744, 1992.
- **[Survey]** László Lovász, Michael D. Plummer. *Matching Theory.* North-Holland / AMS Chelsea, 1986 (2009 reprint).
- **[Survey]** Vijay V. Vazirani. *A Theory of Alternating Paths and Blossoms, from the Perspective of Minimum Length.* Mathematics of Operations Research 49(1), 2024.

## 10. Worked Example / Concrete Special Case

Take $G = C_4$: parts $U = \{u_1,u_2\}$, $V = \{v_1,v_2\}$, all four edges present. There are exactly two perfect matchings,
$$M_1 = \{u_1v_1,\ u_2v_2\}, \qquad M_2 = \{u_1v_2,\ u_2v_1\}.$$

**Why plain determinants fail.** With unit weights, $A = \begin{pmatrix}1&1\\1&1\end{pmatrix}$ and $\det A = 0$ — the two matchings have opposite sign and cancel. This is exactly the tie that isolation must break.

**Apply MVV weights.** Set $w(u_1v_1)=1,\ w(u_1v_2)=2,\ w(u_2v_1)=4,\ w(u_2v_2)=8$, and $A_{ij} = 2^{w(u_iv_j)}$:
$$A = \begin{pmatrix} 2 & 4 \\ 16 & 256\end{pmatrix}, \qquad \det A = 2\cdot 256 - 4\cdot 16 = 512 - 64 = 448 = 2^6 \cdot 7 .$$
Weights: $w(M_1) = 1+8 = 9$, $w(M_2) = 2+4 = 6$. The minimum is unique, $w^\ast = 6$, and indeed $448 / 2^6 = 7$ is **odd** — the parity test certifies isolation.

**Extract the matching in parallel.** For each edge, compute the $1\times 1$ minor and test $\det A^{(ij)} \cdot 2^{w(u_iv_j)} / 2^{w^\ast}$:

| edge $(i,j)$ | $\det A^{(ij)}$ | $2^{w(e)}$ | quotient / $2^{6}$ | parity | in $M$? |
|---|---|---|---|---|---|
| $(1,1)$ | $256 = 2^8$ | $2^1$ | $2^{9}/2^{6} = 8$ | even | no |
| $(1,2)$ | $16 = 2^4$ | $2^2$ | $2^{6}/2^{6} = 1$ | odd | **yes** |
| $(2,1)$ | $4 = 2^2$ | $2^4$ | $2^{6}/2^{6} = 1$ | odd | **yes** |
| $(2,2)$ | $2 = 2^1$ | $2^8$ | $2^{9}/2^{6} = 8$ | even | no |

All four tests are independent, so the matching $M_2 = \{u_1v_2, u_2v_1\}$ is read off in one parallel round after an $\mathsf{NC}^2$ determinant computation.

**Where the difficulty lives.** $C_4$ has a single cycle, and the weight function works because its circulation is nonzero:
$$\operatorname{circ}_w(C_4) = w(u_1v_1) - w(u_2v_1) + w(u_2v_2) - w(u_1v_2) = 1 - 4 + 8 - 2 = 3 \ne 0 .$$
Isolation for a general bipartite graph means choosing one $w$ with small values making **every** cycle's circulation nonzero. A graph on $n$ vertices has up to $2^{\Theta(n \log n)}$ cycles; a random $w$ from $\{1,\dots,2m\}$ succeeds with probability $\ge 1/2$, but no explicit $w$ (or polynomial-size list of candidate $w$'s) is known. FGT construct such a list of size $n^{O(\log^2 n)}$ by handling cycles of increasing length in $\Theta(\log n)$ rounds. Shrinking that list to $n^{O(1)}$ is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*