---
id: 07-combinatorics/bermond-thomassen-conjecture
title: "Bermond-Thomassen Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bermond-Thomassen Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bermond-thomassen-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Bermond–Thomassen, 1981).** For every integer $k \ge 1$, every digraph $D$ with minimum out-degree
$$\delta^{+}(D) \;\ge\; 2k-1$$
contains $k$ pairwise vertex-disjoint directed cycles.

Constraints and conventions:

- $D$ is a **digraph**: loops are forbidden, and at most one arc in each direction between an ordered pair. Digons (2-cycles $u \to v \to u$) are allowed and count as cycles.
- "Cycle" means **directed** cycle of length $\ge 2$; "disjoint" means vertex-disjoint (hence arc-disjoint too).
- No in-degree hypothesis is imposed. This is essential: the conjecture is a purely *out-degree* statement.

A complete proof must exhibit, for arbitrary $k$ and arbitrary $D$ with $\delta^+(D) \ge 2k-1$, $k$ disjoint cycles. A disproof requires a single digraph $D$ and integer $k$ with $\delta^+(D) \ge 2k-1$ whose maximum number of disjoint cycles is $\le k-1$.

The bound $2k-1$ is **sharp** if true: the complete digraph $\overleftrightarrow{K}_{2k-1}$ on $2k-1$ vertices has $\delta^+ = 2k-2$, and since every cycle uses $\ge 2$ vertices it holds at most $\lfloor (2k-1)/2 \rfloor = k-1$ disjoint cycles.

## 2. Mathematical Foundations

Let $D = (V,A)$ be a digraph. For $v \in V$ write $N^{+}(v) = \{u : (v,u) \in A\}$, $d^{+}(v) = |N^{+}(v)|$, and
$$\delta^{+}(D) = \min_{v \in V} d^{+}(v), \qquad \delta^{-}(D) = \min_{v \in V} d^{-}(v).$$
Let $\nu_{\circ}(D)$ denote the **cycle packing number**: the maximum size of a family of pairwise vertex-disjoint directed cycles. Define the extremal function
$$f(k) \;=\; \min\{\, d \in \mathbb{N} : \delta^{+}(D) \ge d \ \Rightarrow\ \nu_{\circ}(D) \ge k \ \text{ for all digraphs } D \,\}.$$
The conjecture is the assertion
$$f(k) = 2k-1 \quad \text{for all } k \ge 1 .$$
The lower bound $f(k) \ge 2k-1$ is witnessed by $\overleftrightarrow{K}_{2k-1}$; the content is the upper bound $f(k) \le 2k-1$.

Two elementary facts anchor the theory.

- **$k=1$ (folklore).** If $\delta^{+}(D) \ge 1$ then $D$ has a cycle: iterate $v_{i+1} \in N^{+}(v_i)$; since $V$ is finite some vertex repeats, and the segment between repetitions is a directed cycle. Hence $f(1) = 1$.
- **Greedy iteration fails.** Deleting a cycle $C$ from $D$ can drop out-degrees arbitrarily, so one cannot simply extract cycles one at a time from a $\delta^{+} \ge 2k-1$ digraph. Any proof must control the *residual* degree, which is why the natural target is $2$ per cycle rather than $1$.

Relevant auxiliary notions: the **girth** $g(D)$ (shortest cycle length); a **tournament** is an orientation of a complete graph; the **independence number** $\alpha(D)$ is that of the underlying undirected graph ($\alpha = 1$ for tournaments). A digraph is $k$-**regular** if $d^+(v) = d^-(v) = k$ for all $v$.

An important strengthening in the tournament case replaces "cycle" by "cycle of length exactly $3$", using the fact that a tournament with a cycle has a $3$-cycle (Moon's theorem on vertex-pancyclicity of strong tournaments is the standard companion result).

## 3. History & State of the Art (SOTA)

- **1981 — origin.** J.-C. Bermond and C. Thomassen posed the conjecture in their survey *Cycles in digraphs — a survey* (J. Graph Theory 5, 1–43), where it appears among the problems on disjoint cycles in digraphs.
- **1983 — existence of $f(k)$.** Thomassen (*Disjoint cycles in digraphs*, Combinatorica 3, 393–396) proved that $f(k)$ is finite, with a bound of factorial type ($f(k) \le (k+1)!$ in the form usually quoted), and settled $k=2$: $\delta^{+} \ge 3$ forces two disjoint cycles.
- **1996 — linear bound.** N. Alon (*Disjoint directed cycles*, JCTB 68, 167–178) proved $f(k) \le 64k$ by a probabilistic argument: randomly partition $V$ into parts and show that with positive probability many parts retain enough out-degree to host a cycle. This reduced the problem from "is $f$ linear?" to "what is the constant?".
- **2009 — $k=3$.** Lichiardopol, Pór and Sereni (SIAM J. Discrete Math. 23, 979–992) proved the case $k=3$ by a long structural analysis of a minimal counterexample.
- **2010–2014 — tournaments.** Bessy, Lichiardopol and Sereni proved the conjecture for tournaments with $\delta^{-} \ge 2k-1$; Bang-Jensen, Bessy and Thomassé removed the in-degree hypothesis and proved the strong form: every tournament with $\delta^{+} \ge 2k-1$ has $k$ disjoint **3-cycles**.
- **2018 — best general constant.** M. Bucić (*An improved bound for disjoint directed cycles*, Discrete Math. 341, 227–233) proved $f(k) \le 18k$, refining Alon's partitioning with a more careful degree-accounting argument.

Current status: proven for $k \le 3$ and for all $k$ in restricted classes; open for general digraphs and every $k \ge 4$. Best general upper bound $f(k) \le 18k$, versus the conjectured $2k-1$ — a multiplicative gap of about $9$.

## 4. Partial Results / Verified Cases

| Case / class | Result | Source |
|---|---|---|
| $k = 1$ | $f(1)=1$; trivial | folklore |
| $k = 2$ | $\delta^+ \ge 3 \Rightarrow$ 2 disjoint cycles | Thomassen 1983 |
| $k = 3$ | $\delta^+ \ge 5 \Rightarrow$ 3 disjoint cycles | Lichiardopol–Pór–Sereni 2009 |
| all $k$, general digraphs | $\delta^+ \ge 64k \Rightarrow k$ disjoint cycles | Alon 1996 |
| all $k$, general digraphs | $\delta^+ \ge 18k \Rightarrow k$ disjoint cycles | Bucić 2018 |
| tournaments, $\delta^- \ge 2k-1$ | conjecture holds | Bessy–Lichiardopol–Sereni 2010 |
| tournaments, $\delta^+ \ge 2k-1$ | $k$ disjoint **3-cycles** (strong form) | Bang-Jensen–Bessy–Thomassé 2014 |
| regular tournaments | $k$ disjoint 3-cycles whenever $2k-1 \le \delta^+$ | Lichiardopol 2010s |

Additional verified regimes:

- **Digraphs of small order.** If $|V(D)| \le 3k-1$ and $\delta^+ \ge 2k-1$, the counting is tight enough that the disjoint cycles can be extracted directly; the hard instances have many vertices relative to $k$.
- **Bipartite-like / digon-free restrictions.** For oriented graphs (digon-free digraphs) the girth is $\ge 3$, so $k$ disjoint cycles consume $\ge 3k$ vertices; several of the counting obstructions to the general case relax, and the conjecture is verified for further sub-families of oriented graphs with bounded independence number.
- **Prescribed lengths.** Lichiardopol proved variants forcing $k$ disjoint cycles of length exactly $q$ under out-degree conditions of the form $\delta^{+} \ge (q-1)k - 1$ in tournaments, which specialize to the $q=3$ tournament case above.

## 5. Principal Obstacles

- **No degree budget for iteration.** The natural induction "find a cycle $C$, delete it, apply the statement for $k-1$" requires that $D - V(C)$ still has $\delta^{+} \ge 2k-3$. A single vertex of $C$ can absorb up to $|V(C)|$ out-neighbours of some $v$, so deletion may drop $d^{+}(v)$ by an unbounded amount. Choosing $C$ *shortest* limits the damage to $g(D)$, not to $2$ — which is exactly the missing factor.
- **Probabilistic methods lose constants.** Alon's and Bucić's arguments split $V$ randomly and want each part to retain out-degree $\ge 1$ inside itself. Concentration inequalities (Chernoff / Lovász Local Lemma) inherently need an out-degree of order $\log$-free but constant-inflated size; a random split cannot see the *tight* extremal configuration $\overleftrightarrow{K}_{2k-1}$, so no random partition scheme is expected to reach $2k-1$.
- **Extremal examples are non-unique and unstable.** Disjoint copies of $\overleftrightarrow{K}_{2k-1}$-like blocks, blow-ups, and near-regular constructions all sit near the boundary. Stability arguments ("a digraph close to extremal has the desired packing") lack a rigidity theorem to anchor them.
- **No LP/flow duality.** For undirected graphs, Erdős–Pósa-type theorems relate cycle packing and covering. In digraphs the Erdős–Pósa property for directed cycles holds (Reed–Robertson–Seymour–Thomas) but with a huge, non-explicit function, and the corresponding fractional relaxation has an unbounded integrality gap, so packing cannot be certified via a covering dual with the precision $2k-1$ demands.
- **Minimal-counterexample analysis explodes.** The $k=3$ proof already requires an extensive case analysis on the structure of a minimal counterexample; the number of configurations grows superlinearly in $k$, giving no inductive template.

## 6. The Gap

Proven: $f(k) \le 18k$ for all $k$, and $f(k) = 2k-1$ for $k \le 3$ and inside tournaments. Conjectured: $f(k)=2k-1$ for all $k$.

The precise barrier is the **per-cycle degree cost**. Every known general argument pays $\Theta(1) \cdot k$ with a constant $\ge 18$ because it must guarantee, simultaneously for $k$ regions of the digraph, that out-degree survives localization. The conjecture asserts the cost is exactly $2$ per cycle: each extra cycle should consume only two units of out-degree. Closing the gap requires either

1. an **exchange/rotation argument** that, given $k-1$ disjoint cycles and a vertex set of high out-degree outside them, reroutes the packing to free up a $k$-th cycle while losing at most $2$ units of degree per step; or
2. a **sharp extremal characterization**: prove that any digraph with $\delta^+ \ge 2k-1$ and $\nu_\circ = k-1$ must contain a $\overleftrightarrow{K}_{2k-1}$-like block, and then contradict $\delta^+$.

Neither is available even for $k=4$, which is the smallest open case.

## 7. Current Research (as of June 2026)

- **Bounded independence number.** The most active thread extends the tournament proof to digraphs with $\alpha(D) \le 2$ or $\alpha(D) \le c$, where Ramsey-type arguments still supply many short cycles. Partial results of this type are the main recent additions to the literature *(frontier — verify)*.
- **Improving the linear constant.** Refinements of Bucić's counting — combining the random-partition step with a semi-random "nibble" or with entropy compression — are pursued at Cambridge, ETH Zürich and the Rényi Institute; a constant below $10$ would be the first substantive movement since 2018 *(frontier — verify)*.
- **Case $k=4$.** Computer-assisted analysis of minimal counterexamples with $\delta^+ = 7$, using SAT/ILP certification of local configurations, has been attempted; no complete resolution is reported *(frontier — verify)*.
- **Prescribed-length and regular variants.** Lichiardopol-style conjectures (e.g. $k$ disjoint cycles of length $\ge g$ under $\delta^+ \ge k(g-1)-1$) are studied as testbeds, since they isolate the degree-accounting question from the girth question.
- **Groups.** Bang-Jensen and collaborators (Southern Denmark), Bessy and Havet (Montpellier / Inria Sophia Antipolis), Thomassé (ENS Lyon), and Chinese groups working on cycle packing in digraphs are the recurring contributors.

## 8. Future Work

- Prove $k=4$. Even a computer-assisted proof would test whether the $k=3$ method scales.
- Prove the **asymptotic** version: $f(k) \le (2+o(1))k$. This would confirm the constant $2$ without resolving the exact bound and is regarded as the realistic next milestone.
- Establish the conjecture for **digon-free digraphs** (oriented graphs), where the extremal example $\overleftrightarrow{K}_{2k-1}$ disappears and one may hope for a stronger bound such as $\delta^+ \ge \tfrac{3}{2}k$.
- Develop a **stability theory** for cycle packing in digraphs: classify digraphs with $\delta^+ \ge 2k-1$ and $\nu_\circ$ small.
- Transfer the tournament proof: identify the exact property of tournaments (high density, $\alpha=1$, abundance of 3-cycles) that makes the $2k-1$ bound provable, and weaken it step by step.

## 9. Key References

- **[Foundational]** J.-C. Bermond, C. Thomassen. *Cycles in digraphs — a survey.* Journal of Graph Theory, 5(1):1–43, 1981.
- **[Foundational]** C. Thomassen. *Disjoint cycles in digraphs.* Combinatorica, 3(3–4):393–396, 1983.
- **[SOTA]** N. Alon. *Disjoint directed cycles.* Journal of Combinatorial Theory, Series B, 68(2):167–178, 1996.
- **[SOTA]** M. Bucić. *An improved bound for disjoint directed cycles.* Discrete Mathematics, 341(1):227–233, 2018.
- **[Partial]** N. Lichiardopol, A. Pór, J.-S. Sereni. *A step toward the Bermond–Thomassen conjecture about disjoint cycles in digraphs.* SIAM Journal on Discrete Mathematics, 23(2):979–992, 2009.
- **[Partial]** S. Bessy, N. Lichiardopol, J.-S. Sereni. *Two proofs of the Bermond–Thomassen conjecture for tournaments with bounded minimum in-degree.* Discrete Mathematics, 310(3):557–560, 2010.
- **[SOTA]** J. Bang-Jensen, S. Bessy, S. Thomassé. *Disjoint 3-cycles in tournaments: a proof of the Bermond–Thomassen conjecture for tournaments.* Journal of Graph Theory, 75(3):284–302, 2014.
- **[Survey / Book]** J. Bang-Jensen, G. Gutin. *Digraphs: Theory, Algorithms and Applications.* 2nd edition, Springer Monographs in Mathematics, 2009.
- **[Survey / Book]** J. Bang-Jensen, G. Gutin (eds.). *Classes of Directed Graphs.* Springer Monographs in Mathematics, 2018.

## 10. Worked Example / Concrete Special Case

**Sharpness for $k=2$.** Take $D = \overleftrightarrow{K}_3$ on $V=\{a,b,c\}$ with all six arcs. Then $d^{+}(v)=2$ for every $v$, so $\delta^{+}=2 = 2k-2$ with $k=2$. Two vertex-disjoint cycles would need $\ge 4$ vertices, but $|V|=3$. Hence $\nu_\circ(D)=1$ and $f(2) \ge 3 = 2k-1$. The same construction with $\overleftrightarrow{K}_{2k-1}$ gives $f(k) \ge 2k-1$ for every $k$.

**The matching upper bound $f(2) \le 3$ (Thomassen).** Let $\delta^{+}(D) \ge 3$ and suppose $\nu_\circ(D) = 1$. Pick a **shortest** cycle $C = v_1 v_2 \cdots v_\ell v_1$, so $\ell = g(D)$. Minimality gives that $C$ has no chords in the "shortcut" direction: for $i \ne j$, an arc $v_i \to v_j$ exists only if $j = i+1 \pmod \ell$ (otherwise it would create a shorter cycle). Therefore each $v_i$ sends at least $d^{+}(v_i) - 1 \ge 2$ arcs out of $V(C)$.

Now consider $D' = D - V(C)$. Since $\nu_\circ(D)=1$, $D'$ has **no** cycle, so $D'$ is acyclic and has a sink $s$ (a vertex with $d^{+}_{D'}(s)=0$). All $\ge 3$ out-neighbours of $s$ in $D$ lie on $C$; say $s \to v_i$ and $s \to v_j$ with $i \ne j$. Trace $C$ from $v_i$ forward: since $s$ also has in-neighbours forced by the counting above (some $v_p \to s$, because each $v_p$ has $\ge 2$ out-arcs leaving $C$ and $D'$ is acyclic with $s$ reachable), we obtain a cycle through $s$ and a proper arc of $C$, and a second cycle on the remaining part of $C$ — two disjoint cycles, contradiction. (The full argument in Combinatorica 3 (1983) handles the reachability bookkeeping; the sketch shows how the value $3 = 2\cdot 2 - 1$ enters: one unit of out-degree is spent on $C$ itself, and two units are needed to split the rest.)

**Illustration of the tight regime for $k=3$.** Take three disjoint copies of $\overleftrightarrow{K}_{3}$ plus a "hub" vertex $h$ joined out to three vertices in distinct copies. Here $\delta^{+}=2 < 5$, and $\nu_\circ = 3$ already — showing that low out-degree does *not* by itself obstruct packing. The extremal examples must be **globally** tight, i.e. one clique-like block of $2k-1$ vertices, which is precisely the structure a stability theorem (Section 6, route 2) would have to isolate.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*