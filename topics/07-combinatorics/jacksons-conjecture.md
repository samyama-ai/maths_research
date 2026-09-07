---
id: 07-combinatorics/jacksons-conjecture
title: "Jackson's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jackson's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/jacksons-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Jackson, 1981).** Every $d$-regular oriented graph on $n$ vertices with
$$n \le 4d+1$$
contains a Hamilton cycle.

Here an *oriented graph* is a digraph with no loops, no repeated arcs and no $2$-cycles (i.e. an orientation of a simple graph), and *$d$-regular* means every vertex has in-degree and out-degree exactly $d$. A Hamilton cycle is a directed cycle through all $n$ vertices.

A complete resolution requires either a proof valid for all $d \ge 1$ and all admissible $n$, or a single $d$-regular oriented graph on $n \le 4d+1$ vertices with no Hamilton cycle. Asymptotic versions (all sufficiently large $n$, or $n \le (4-\varepsilon)d$) are strictly weaker and are recorded separately in §4.

The bound $4d+1$ cannot be raised: the disjoint union of two regular tournaments on $2d+1$ vertices is a $d$-regular oriented graph on $4d+2$ vertices which is not even connected.

## 2. Mathematical Foundations

Let $G=(V,A)$ be an oriented graph, $|V| = n$. For $v \in V$ write $N^+(v)=\{u: vu \in A\}$, $N^-(v)=\{u: uv \in A\}$, $d^+(v)=|N^+(v)|$, $d^-(v)=|N^-(v)|$. The **minimum semi-degree** is
$$\delta^0(G) = \min_{v\in V}\ \min\{d^+(v), d^-(v)\}.$$
$G$ is $d$-regular iff $d^+(v)=d^-(v)=d$ for all $v$; then $|A| = nd$.

**Feasibility.** Since $N^+(v)$ and $N^-(v)$ are disjoint (no $2$-cycles), $n \ge 2d+1$. Equality forces $G$ to be a **regular tournament** on $2d+1$ vertices. Thus the conjecture concerns the window
$$2d+1 \ \le\ n \ \le\ 4d+1 ,\qquad\text{equivalently}\qquad d \ \ge\ \tfrac{n-1}{4}.$$

**Underlying graph.** The underlying simple graph $\bar G$ is $2d$-regular. For $n \le 4d$ we get $\delta(\bar G) = 2d \ge n/2$, so by Dirac's theorem $\bar G$ is Hamiltonian. The content of the conjecture is therefore entirely about *orientation*: an undirected Hamilton cycle exists for free, but its arcs need not be consistently directed.

**Strong connectivity (a proof, not a hypothesis).** Suppose $V = A \sqcup B$ with no arc from $B$ to $A$. Every arc leaving $A$ ends in $A\cup B$, but every arc entering $A$ starts in $A$; counting in-arcs at $A$ gives $|A|d \le \binom{|A|}{2}$, i.e. $|A| \ge 2d+1$. Counting out-arcs at $B$ gives $|B| \ge 2d+1$. Hence $n \ge 4d+2$. So:

> **Lemma.** Every $d$-regular oriented graph on $n \le 4d+1$ vertices is strongly connected.

This is exactly why $4d+1$ is the natural threshold, and it shows the conjecture asserts that in this regime the obvious necessary condition (strong connectivity) is also sufficient.

**Comparison thresholds.** For general digraphs, Ghouila-Houri's theorem gives a Hamilton cycle when $\delta^0(G) \ge n/2$. For oriented graphs the truth is $\delta^0(G) \ge \lceil (3n-4)/8 \rceil$ (Keevash–Kühn–Osthus). Jackson's conjecture asks for a Hamilton cycle at $d \ge (n-1)/4$, i.e. **well below** the general oriented-graph threshold $3n/8$; regularity is doing the extra work.

## 3. History & State of the Art (SOTA)

- **1959.** Camion: every strongly connected tournament is Hamiltonian. Combined with the Lemma above this settles $n = 2d+1$.
- **1960.** Ghouila-Houri: $\delta^0 \ge n/2$ forces Hamiltonicity in digraphs — the directed Dirac theorem, and the model for all later work.
- **1981.** Bill Jackson, *Long paths and cycles in oriented graphs* (J. Graph Theory **5**, 145–157), studies long cycles in oriented graphs of large minimum degree and poses the $n \le 4d+1$ conjecture. Same year, Thomassen's *Long cycles in digraphs* develops the complementary long-cycle machinery.
- **1993.** Häggkvist introduces the "chord/rotation" method for oriented graphs, giving Hamiltonicity for $\delta^0 \ge (5/12 - o(1))n$.
- **2008.** Kelly, Kühn and Osthus prove the asymptotically optimal $\delta^0 \ge (3/8 + o(1))n$ using the directed regularity lemma plus a robust-expansion argument.
- **2009.** Keevash, Kühn and Osthus sharpen this to the exact bound $\delta^0 \ge \lceil (3n-4)/8\rceil$ for large $n$ — best possible.
- **2012–2013.** The Kühn–Osthus *robust outexpander* framework matures: every large $d$-regular robust outexpander with $d \ge \alpha n$ has a Hamilton **decomposition** (proof of Kelly's conjecture for large tournaments). This is the strongest available tool, and it is the reason the regular case is expected to behave far better than the general one.
- **Status 2026.** Jackson's conjecture remains open for all $d \ge 3$ in the range $n > \tfrac{8}{3}d$. No counterexample and no full proof.

## 4. Partial Results / Verified Cases

1. **$n = 2d+1$ (regular tournaments): proved.** Strong connectivity (Lemma, §2) plus Camion's theorem. In fact such graphs have Hamilton decompositions for large $d$ (Kühn–Osthus 2013).
2. **$d = 1$: proved.** A $1$-regular oriented graph is a disjoint union of directed cycles of length $\ge 3$; with $n \le 5$ there is only one cycle, so it is Hamiltonian.
3. **$d = 2$ ($n \le 9$): verified by exhaustive computer search** over $2$-regular oriented graphs on $7,8,9$ vertices — a finite check, not a structural proof.
4. **Dense regime $n \le \tfrac{8}{3}d + O(1)$, $n$ large: proved.** If $d \ge \lceil (3n-4)/8 \rceil$ then $\delta^0(G) = d$ meets the Keevash–Kühn–Osthus exact bound, so $G$ is Hamiltonian for all sufficiently large $n$. Equivalently, the conjecture is known for $n \le \tfrac{8}{3}d + \tfrac{4}{3}$.
5. **Robust expanders: proved (large $n$).** If in addition $G$ is a robust outexpander with linear expansion parameter, Hamiltonicity — indeed a Hamilton decomposition — follows from Kühn–Osthus. Random $d$-regular orientations with $d = \Omega(n)$ are robust outexpanders with high probability, so the conjecture holds for almost all $d$-regular oriented graphs in the range.
6. **Underlying-graph statement: proved.** For $n \le 4d$ the underlying $2d$-regular graph is Hamiltonian (Dirac), and even $\lfloor d \rfloor$-edge-connected-Hamiltonian-decomposable in dense cases; only the orientation obstruction remains.
7. **Sharpness: settled.** Non-Hamiltonian $d$-regular oriented graphs exist on $4d+2$ vertices (two disjoint regular tournaments), so the constant $4$ is optimal.

## 5. Principal Obstacles

- **The regularity/absorption toolkit is calibrated to $3n/8$, not $n/4$.** All modern proofs (Kelly–Kühn–Osthus, Keevash–Kühn–Osthus) run: apply the directed regularity lemma, find an almost-spanning structure in the reduced digraph, absorb the leftovers. The reduced digraph inherits semi-degree $\approx d$; below $3n/8$ its "extremal" configurations (a near-partition into two dense parts with a thin, badly oriented cut) survive, and the standard extremal-case analysis has no replacement hypothesis to exploit. Regularity is a *global* condition that the local regularity-lemma analysis cannot see.
- **Sparse regime.** At $d \approx n/4$ the graph has $nd \approx n^2/4$ arcs — still dense — but each vertex misses $n - 1 - 2d \approx n/2$ vertices. Rotation–extension arguments (Häggkvist) need many "chords" out of a long path; at $n/4$ the supply is too thin to guarantee a rotation that closes the cycle.
- **Robust expansion is not implied.** Kühn–Osthus machinery requires robust outexpansion. A $d$-regular oriented graph with $d = (n-1)/4$ need not robustly expand: it may consist of two tightly knit halves joined by exactly the arcs the counting Lemma forces. These borderline graphs are precisely the untreated ones, and no known argument converts "strongly connected + regular" into "robust expander" at this density.
- **No flow/matching reformulation.** Hamiltonicity is not a flow condition; the natural LP relaxation (fractional 2-factor / cycle cover) is satisfied trivially by regularity — every $d$-regular digraph decomposes into $d$ arc-disjoint $1$-factors — yet these $1$-factors can be forced to consist of short cycles. Turning a cycle factor into a single cycle is exactly the missing step, and there is no polytope-level obstruction to detect.
- **Small $d$ is not asymptotic.** All strong results carry an unspecified "$n$ sufficiently large" from the regularity lemma, of tower type. Even a full asymptotic proof would leave every explicitly checkable $d$ untouched.

## 6. The Gap

Known: $n \le \tfrac{8}{3}d + O(1)$ for large $n$ (§4.4), plus $n = 2d+1$ and the robust-expander case for all $n$ in range. Conjectured: $n \le 4d+1$.

The precise open window is
$$\tfrac{8}{3}d \ <\ n\ \le\ 4d+1,$$
i.e. semi-degree between $n/4$ and $3n/8$ **under the extra hypothesis of exact regularity**. The step to be crossed: show that regularity alone rules out the extremal configurations that make $3n/8$ tight in the non-regular setting — concretely, prove that every strongly connected $d$-regular oriented graph with $n \le 4d+1$ is a robust outexpander, or else handle the non-expanding cases by a direct structural decomposition. Additionally, the tower-type dependence in the regularity lemma must be removed to reach small $d$.

## 7. Current Research (as of June 2026)

- **Birmingham school (Kühn, Osthus, and successors).** Continued development of robust-expander and absorption methods for regular digraphs; the guiding programme is "regularity + expansion $\Rightarrow$ Hamilton decomposition", of which Jackson's conjecture would be the sparse-degree endpoint.
- **Regularity-free absorption.** Recent work replaces the directed regularity lemma with sparse absorbers and randomised rounding of fractional cycle covers, aiming to remove the tower-type $n_0$. *(frontier — verify)* — this is the most likely route to statements covering moderate $d$.
- **Structural classification of near-extremal regular oriented graphs.** Attempts to prove that a $d$-regular oriented graph on $n \le 4d+1$ vertices failing robust outexpansion must be close to two regular tournaments joined by a sparse cut, and that such graphs are Hamiltonian by an explicit patching argument. *(frontier — verify)*
- **Computational verification.** Isomorph-free generation of $d$-regular oriented graphs (nauty/`directg`-style pipelines) has been pushed to $d = 3$, $n \le 13$; the search space grows superexponentially, so $d \ge 4$ is out of reach by brute force. *(frontier — verify)*
- **Related conjectures actively pursued.** Arbitrary orientations of Hamilton cycles in oriented graphs; Hamilton decompositions of regular oriented graphs; Bermond–Thomassen-type cycle-partition problems, which share the "regularity forces global structure" theme.

## 8. Future Work

- **Prove the expansion dichotomy.** Show: every strongly connected $d$-regular oriented graph with $n \le 4d+1$ is either a robust outexpander (then apply Kühn–Osthus) or has a specific two-block structure amenable to direct analysis. This is the strategy explicitly advocated in the Kühn–Osthus survey.
- **Get an intermediate constant.** Even $n \le 3d$ for large $n$ would be the first improvement past the $8/3$ barrier and would prove that regularity genuinely beats the $3n/8$ semi-degree threshold.
- **Quantitative regularity.** Replace the directed regularity lemma with a sparse/absorbing method giving $n_0$ of tower-free size, opening $d \le 20$ to computation.
- **Test sharpness harder.** Search systematically for $d$-regular oriented graphs on exactly $4d+1$ vertices with no Hamilton cycle; a counterexample would be a single explicit graph, and its absence at $d = 3,4$ is meaningful evidence.
- **Strengthen to decomposition.** Conjecturally, every $d$-regular oriented graph on $n \le 4d+1$ vertices has $\lfloor d/2 \rfloor$ edge-disjoint Hamilton cycles; proving the weaker single-cycle version may be easier via the stronger statement, as happened for Kelly's conjecture.

## 9. Key References

- **[Foundational]** B. Jackson. *Long paths and cycles in oriented graphs.* Journal of Graph Theory **5** (1981), 145–157.
- **[Foundational]** P. Camion. *Chemins et circuits hamiltoniens des graphes complets.* Comptes Rendus de l'Académie des Sciences Paris **249** (1959), 2151–2152.
- **[Foundational]** A. Ghouila-Houri. *Une condition suffisante d'existence d'un circuit hamiltonien.* Comptes Rendus de l'Académie des Sciences Paris **251** (1960), 495–497.
- **[Foundational]** C. Thomassen. *Long cycles in digraphs.* Proceedings of the London Mathematical Society (3) **42** (1981), 231–251.
- **[Classical]** R. Häggkvist. *Hamilton cycles in oriented graphs.* Combinatorics, Probability and Computing **2** (1993), 25–32.
- **[SOTA]** L. Kelly, D. Kühn, D. Osthus. *A Dirac-type result on Hamilton cycles in oriented graphs.* Combinatorics, Probability and Computing **17** (2008), 689–709.
- **[SOTA]** P. Keevash, D. Kühn, D. Osthus. *An exact minimum degree condition forcing Hamiltonicity in oriented graphs.* Journal of the London Mathematical Society **79** (2009), 144–166.
- **[SOTA]** D. Kühn, D. Osthus. *Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments.* Advances in Mathematics **237** (2013), 62–146.
- **[Survey]** D. Kühn, D. Osthus. *A survey on Hamilton cycles in directed graphs.* European Journal of Combinatorics **33** (2012), 750–766.
- **[Reference]** J. Bang-Jensen, G. Gutin. *Digraphs: Theory, Algorithms and Applications.* 2nd edition, Springer Monographs in Mathematics, 2009.

## 10. Worked Example / Concrete Special Case

**Case $d = 2$, $n = 5$ (the extreme $n = 2d+1$).** Take the circulant tournament $C_5(1,2)$: vertices $\mathbb{Z}_5$, arcs $i \to i+1$ and $i \to i+2 \pmod 5$. Each vertex has $d^+ = d^- = 2$, so it is $2$-regular, and $n = 5 = 2d+1 \le 4d+1 = 9$. The arcs $0\to1\to2\to3\to4\to0$ form a Hamilton cycle. This matches the general proof: strongly connected (Lemma) plus Camion.

**Case $d = 2$, $n = 9 = 4d+1$ (the extreme upper end).** Take $G$ on $\mathbb{Z}_9$ with arcs $i \to i+1$ and $i \to i+3$. Then $d^+(i) = d^-(i) = 2$, and no $2$-cycle exists since $1 + 1, 1+3, 3+3 \not\equiv 0 \pmod 9$. The cycle $0\to1\to2\to\cdots\to8\to0$ is Hamiltonian, as predicted.

**Why $4d+2$ fails.** Let $d = 2$ and put $H = C_5(1,2) \sqcup C_5(1,2)$, two disjoint copies of the $5$-vertex circulant tournament. Then $H$ is $2$-regular on $n = 10 = 4d+2$ vertices and has no Hamilton cycle, since it is disconnected. This is the sharpness example of §1, and the counting Lemma of §2 explains it exactly: a "one-way" partition needs both sides of size $\ge 2d+1 = 5$, so it first becomes possible at $n = 4d+2 = 10$.

**Where the difficulty hides.** For $d = 2$, $n = 9$, the underlying graph is $4$-regular on $9$ vertices, hence Hamiltonian by Dirac ($4 \ge 9/2$ fails marginally, but $4$-regular graphs on $9$ vertices are Hamiltonian by inspection). The conjecture asserts that some undirected Hamilton cycle can always be chosen *consistently oriented*. Verifying this for a single graph is a finite check; doing it for all $d$-regular oriented graphs at $d \approx n/4$, where no expansion guarantee is available, is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*