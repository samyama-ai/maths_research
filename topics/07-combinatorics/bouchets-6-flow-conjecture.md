---
id: 07-combinatorics/bouchets-6-flow-conjecture
title: "Bouchet's 6-Flow Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bouchet's 6-Flow Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bouchets-6-flow-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Bouchet, 1983).** Every bidirected graph that admits a nowhere-zero integer flow admits a nowhere-zero $6$-flow.

Equivalently, in signed-graph language: if a signed graph $(G,\sigma)$ is *flow-admissible* (it has at least one nowhere-zero integer flow), then its flow number satisfies $\Phi(G,\sigma) \le 6$.

Constraints and scope:

- $G$ may have multiple edges and loops; $\sigma: E(G)\to\{+1,-1\}$ is arbitrary.
- Flow-admissibility is a genuine hypothesis, not a technicality: unlike ordinary graphs, a bridgeless signed graph can fail to carry any nowhere-zero flow only in restricted ways, and single unbalanced circuits fail outright (Section 10).
- A proof must produce, for every flow-admissible $(G,\sigma)$, an orientation and an integer flow $f$ with $1\le |f(e)|\le 5$ for all $e$. A disproof requires one flow-admissible signed graph with $\Phi \ge 7$.

The bound $6$ is sharp: signed graphs with flow number exactly $6$ exist (Bouchet gave a signed Petersen graph), so the conjecture, if true, is best possible. Setting $\sigma\equiv +1$ recovers Seymour's 6-flow theorem, so Bouchet's conjecture is a strict generalization of a hard theorem.

## 2. Mathematical Foundations

**Bidirected graphs.** A bidirected graph is a graph $G$ together with an assignment $\tau$ giving each half-edge $(e,v)$ ($v$ an endpoint of $e$) a sign $\tau(e,v)\in\{+1,-1\}$. Reading $\tau(e,v)=+1$ as "$e$ points into $v$", an edge is *directed* if its two half-edges disagree, *extraverted* if both are $-1$, *introverted* if both are $+1$.

**Signed graphs.** Put $\sigma(e) := -\tau(e,u)\tau(e,v)$ for $e=uv$. Then $\sigma:E\to\{\pm1\}$ is a signature, and $\tau$ is called an *orientation* of $(G,\sigma)$. Every signature admits $2^{|E|}$ orientations; directed edges are exactly the positive ones.

**Flows.** For an orientation $\tau$, a map $f:E(G)\to\mathbb{Z}$ is a flow if it satisfies conservation at every vertex:
$$\sum_{e \ni v} \tau(e,v)\, f(e) = 0 \qquad \text{for all } v\in V(G),$$
loops at $v$ contributing both half-edges. $f$ is a *nowhere-zero $k$-flow* if $0<|f(e)|\le k-1$ for all $e$. The *flow number* is
$$\Phi(G,\sigma) = \min\{\,k : (G,\sigma)\text{ has a nowhere-zero }k\text{-flow}\,\}, \qquad \min\emptyset = \infty .$$
Reversing $\tau$ at all half-edges incident to $v$ and negating nothing else is a symmetry; so is switching.

**Switching.** For $X\subseteq V$, the switch $\sigma^X(e) = \sigma(e)\cdot(-1)^{|e\cap X|}$ preserves $\Phi$ and the cycle signs. A circuit $C$ is *balanced* if $\prod_{e\in C}\sigma(e)=+1$; $(G,\sigma)$ is balanced if all circuits are. Balanced signed graphs switch to $\sigma\equiv+1$, so $\Phi$ then equals the ordinary Tutte flow number.

**Signed circuits.** The circuits of the signed graphic (even-cycle/frame) matroid are: balanced circuits; and *barbells* — two edge-disjoint unbalanced circuits joined by a path, possibly of length $0$ (a *figure eight*). Signed circuits are the minimal supports of flows; a barbell carries flow $\pm 1$ on the two circuits and $\pm 2$ on the connecting path.

**Flow admissibility (Bouchet).** A connected signed graph is flow-admissible iff every edge lies in a signed circuit; equivalently, iff $(G,\sigma)$ is not balanced-with-a-bridge in the sense that no bridge $e$ has a balanced component in $G-e$, and $G$ is not a single unbalanced circuit or an unbalanced graph with a bridge separating off a balanced side.

**Failure of group flows.** For ordinary graphs Tutte's theorem gives: a nowhere-zero $k$-flow exists iff a nowhere-zero $\Gamma$-flow exists for any abelian $\Gamma$ with $|\Gamma|=k$. **This equivalence is false for signed graphs.** Beck and Zaslavsky (2006) showed the nowhere-zero flow counting function of a signed graph is a quasipolynomial in $k$ with period $2$, not a polynomial — the parity obstruction is intrinsic.

## 3. History & State of the Art (SOTA)

- **1982.** Zaslavsky formalizes signed graphs and their matroids (*Discrete Appl. Math.* 4).
- **1983.** Bouchet introduces nowhere-zero flows on bidirected graphs, characterizes flow-admissibility, states the conjecture, and proves a nowhere-zero **216-flow**.
- **1987.** Khelladi proves a nowhere-zero **18-flow** for $4$-edge-connected signed graphs.
- **1987.** Zýka's thesis (KAM Series, Charles University) improves the general bound to **30**.
- **2005.** Xu and Zhang prove $\Phi \le 6$ for **$6$-edge-connected** flow-admissible signed graphs — the conjecture holds under high connectivity.
- **2013.** DeVos proves the general bound **12**, the best unconditional bound to date.
- **2011–2018.** Circular flow theory for signed graphs (Raspaud–Zhu), regular and cubic cases (Máčajová–Škoviera, Schubert–Steffen), eulerian case (Máčajová–Škoviera), and few-negative-edge cases (Rollová–Schubert–Steffen).

**SOTA summary.** General bound $12$ (DeVos). Bound $6$ under $6$-edge-connectivity (Xu–Zhang) and for several structural classes. Gap between $6$ and $12$ open for over a decade.

## 4. Partial Results / Verified Cases

| Class / hypothesis | Best bound | Source |
|---|---|---|
| All flow-admissible signed graphs | $\Phi\le 12$ | DeVos 2013 |
| All flow-admissible signed graphs | $\Phi\le 30$ | Zýka 1987 |
| All flow-admissible signed graphs | $\Phi\le 216$ | Bouchet 1983 |
| $4$-edge-connected | $\Phi\le 18$ | Khelladi 1987 |
| $6$-edge-connected | $\Phi\le 6$ ✔ | Xu–Zhang 2005 |
| $6$-edge-connected, flow-admissible | $\Phi\le 3$ under extra parity conditions | Wu–Ye–Zang–Zhang 2014 |
| Balanced signed graphs (bridgeless) | $\Phi\le 6$ ✔ | Seymour 1981 |
| Exactly two negative edges | $\Phi\le 6$ ✔ | Rollová–Schubert–Steffen 2018 |
| Signed eulerian graphs | $\Phi$ determined exactly | Máčajová–Škoviera 2017 |
| Cubic / regular signed graphs | $\Phi\le 6$ for large families | Máčajová–Škoviera 2015; Schubert–Steffen 2015 |

Sharpness: $\Phi=6$ is attained (signed Petersen graph); Máčajová–Škoviera and Schubert–Steffen exhibit further families with $\Phi=5$ or $6$, ruling out any improvement of the conjectured constant.

## 5. Principal Obstacles

- **Group flows do not transfer.** Seymour's 6-flow proof for ordinary graphs works by finding a $\mathbb{Z}_2$-flow and a $\mathbb{Z}_3$-flow and lifting, using Tutte's group/integer equivalence. That equivalence **fails** for signed graphs: a nowhere-zero $\mathbb{Z}_6$-flow on $(G,\sigma)$ need not lift to an integer $6$-flow, because the sign structure obstructs choosing consistent representatives. The entire modular toolkit is therefore unavailable.
- **Parity/quasipolynomiality.** Beck–Zaslavsky's period-$2$ quasipolynomial shows even $k$ and odd $k$ behave differently. Any inductive scheme must track a parity invariant that has no counterpart in the unsigned theory.
- **Minor-closure fails.** The class of flow-admissible signed graphs is not closed under edge contraction in the way ordinary flow theory needs (contracting a negative edge changes the signature only up to switching, and can destroy admissibility). Standard minor-minimal-counterexample reductions break.
- **Splitting and connectivity.** Xu–Zhang's proof consumes $6$-edge-connectivity to run a splitting/nowhere-zero-flow argument; there is no known signed analogue of Nash-Williams/Jaeger $2$-edge-connectivity-to-orientation machinery that survives down to $2$-edge-connected signed graphs.
- **No signed Seymour decomposition.** Ordinary $6$-flows follow from a decomposition into a spanning tree plus circuits found greedily. In signed graphs, the analogous building blocks are barbells, which force flow value $2$ on their handles; nesting barbells multiplies the required flow values rather than adding them, producing the exponential losses that give $12$, $30$, $216$.

## 6. The Gap

Proven unconditionally: $\Phi \le 12$. Conjectured: $\Phi \le 6$. Proven at $\Phi\le 6$ only when $\lambda(G)\ge 6$ or under strong structural restrictions (two negative edges, eulerian, specific regular families).

The exact barrier is a **factor-of-two loss** in the barbell handle. Every known general argument decomposes the signed graph into signed circuits; balanced circuits contribute flow values in $\{\pm1\}$, but barbells contribute $\pm 2$ on their handles. Combining $r$ such structures multiplicatively gives $2^r$-type bounds; DeVos's argument reduces this to a single doubling on top of a $6$-flow, yielding $12$. Closing the gap means finding a decomposition in which barbell handles are shared or cancelled, so that the doubling happens **once globally** rather than once per structure — or, alternatively, a signed analogue of Tutte's group-flow theorem valid for $k=6$, which would let Seymour's $\mathbb{Z}_2\times\mathbb{Z}_3$ argument run verbatim.

Bridging the connectivity gap is the second front: extending Xu–Zhang from $\lambda\ge6$ down to $\lambda\ge2$ (with flow-admissibility) would settle the conjecture.

## 7. Current Research (as of June 2026)

- **Low-negativeness hierarchy.** After the two-negative-edge case (Rollová–Schubert–Steffen 2018), groups in Bratislava (Máčajová, Škoviera) and Paderborn (Steffen and students) push toward signed graphs with three or four negative edges, and toward bounding $\Phi$ by a function of the *negativeness* $\varepsilon(G,\sigma)$, the minimum number of negative edges over all switchings. *(frontier — verify)*
- **Circular flow number.** Raspaud–Zhu's circular flow number $\Phi_c$ for signed graphs is studied as a real-valued relaxation; results bounding $\Phi_c$ for signed cubic and signed $(2t)$-regular graphs feed back into integer bounds via $\Phi = \lceil \Phi_c \rceil$.
- **Modulo orientations.** The Lovász–Thomassen–Wu–Zhang modulo-$k$-orientation technique, which gave $6$-edge-connected $\Rightarrow$ nowhere-zero $3$-flow for ordinary graphs, is being adapted to signed graphs (Wu–Ye–Zang–Zhang and successors) to reduce the connectivity threshold below $6$.
- **Matroid and integer-programming views.** The even-cycle matroid perspective and lattice-point counting (Beck–Zaslavsky style Ehrhart quasipolynomials) are used to search computationally for signed graphs with $\Phi\ge7$; no such example has been found. *(frontier — verify)*
- **Computational verification.** Exhaustive checks over small signed cubic and small connected signed graphs report $\Phi\le6$ throughout. *(frontier — verify)*

## 8. Future Work

- Prove $\Phi\le 6$ for $4$-edge-connected signed graphs, closing the Khelladi ($18$) → Xu–Zhang ($6$) connectivity gap step by step.
- Improve DeVos's $12$ to $10$ or $8$ by refining the barbell handle accounting; even a bound of $9$ would be the first sub-$10$ general result.
- Develop a correct signed analogue of Tutte's group-flow theorem, or classify precisely when a nowhere-zero $\mathbb{Z}_6$-flow lifts to an integer $6$-flow.
- Settle Bouchet's conjecture for all signed cubic graphs; Máčajová–Škoviera identify this as the natural test case, since cubic graphs are extremal for ordinary flow conjectures.
- Characterize all signed graphs with $\Phi=6$; a finite or structured list would strongly support the conjecture and may suggest the proof method.
- Establish $\Phi \le g(\varepsilon)$ with $g(\varepsilon)=6$ for all $\varepsilon$, via induction on negativeness.

## 9. Key References

- **[Foundational]** A. Bouchet. *Nowhere-zero integral flows on a bidirected graph.* Journal of Combinatorial Theory, Series B, 34(3):279–292, 1983.
- **[Foundational]** T. Zaslavsky. *Signed graphs.* Discrete Applied Mathematics, 4(1):47–74, 1982.
- **[Foundational]** P. D. Seymour. *Nowhere-zero 6-flows.* Journal of Combinatorial Theory, Series B, 30(2):130–135, 1981.
- **[Milestone]** A. Khelladi. *Nowhere-zero integral chains and flows in bidirected graphs.* Journal of Combinatorial Theory, Series B, 43(1):95–115, 1987.
- **[Milestone]** O. Zýka. *Nowhere-zero 30-flow on bidirected graphs.* KAM Series 87-26, Charles University, Prague, 1987.
- **[Milestone]** R. Xu and C.-Q. Zhang. *On flows in bidirected graphs.* Discrete Mathematics, 299(1–3):335–343, 2005.
- **[SOTA]** M. DeVos. *Flows on bidirected graphs.* arXiv:1310.8406, 2013.
- **[SOTA / Recent]** E. Rollová, M. Schubert, E. Steffen. *Signed graphs with two negative edges.* The Electronic Journal of Combinatorics, 25(1):#P1.9, 2018.
- **[SOTA / Recent]** Y. Wu, D. Ye, W. Zang, C.-Q. Zhang. *Nowhere-zero 3-flow in signed graphs.* SIAM Journal on Discrete Mathematics, 28(3):1628–1637, 2014.
- **[Recent]** E. Máčajová and M. Škoviera. *Remarks on nowhere-zero flows in signed cubic graphs.* Discrete Mathematics, 338(5):809–815, 2015.
- **[Recent]** E. Máčajová and M. Škoviera. *Nowhere-zero flows on signed eulerian graphs.* SIAM Journal on Discrete Mathematics, 31(3):1937–1952, 2017.
- **[Recent]** M. Schubert and E. Steffen. *Nowhere-zero flows on signed regular graphs.* European Journal of Combinatorics, 48:34–47, 2015.
- **[Structure]** A. Raspaud and X. Zhu. *Circular flow on signed graphs.* Journal of Combinatorial Theory, Series B, 101(6):464–479, 2011.
- **[Counting]** M. Beck and T. Zaslavsky. *The number of nowhere-zero flows on graphs and signed graphs.* Journal of Combinatorial Theory, Series B, 96(6):901–918, 2006.
- **[Survey]** C.-Q. Zhang. *Circuit Double Cover of Graphs.* London Mathematical Society Lecture Note Series 399, Cambridge University Press, 2012.
- **[Survey]** T. Zaslavsky. *A Mathematical Bibliography of Signed and Gain Graphs and Allied Areas.* Electronic Journal of Combinatorics, Dynamic Survey DS8 (updated editions).

## 10. Worked Example / Concrete Special Case

**(a) An unbalanced circuit is not flow-admissible.** Let $C$ be the triangle $u\!-\!a\!-\!b\!-\!u$ with $\sigma(ua)=\sigma(ab)=+1$ and $\sigma(bu)=-1$. The circuit is unbalanced ($\prod\sigma = -1$). Orient by traversing $u\to a\to b$: the positive edges become directed, and the negative edge $bu$ must have both half-edges of equal sign, say $\tau(bu,b)=\tau(bu,u)=+1$ (both heads). Conservation reads

- at $a$: $\;+f(ua)-f(ab)=0$,
- at $u$: $\;-f(ua)+f(bu)=0$,
- at $b$: $\;+f(ab)+f(bu)=0$.

The first two give $f(ua)=f(ab)=f(bu)=:t$, and the third gives $2t=0$, so $t=0$. No nowhere-zero flow exists — the unbalanced circuit has an "excess of $2$" that cannot be absorbed.

**(b) A barbell has flow number exactly $3$.** Let $B$ consist of two disjoint unbalanced triangles $C_1$ (through $u$) and $C_2$ (through $v$), joined by the positive edge $uv$. Orient $C_1$ as above so that, with flow $1$ on all three of its edges, conservation holds at its two non-attachment vertices and leaves an excess of $+2$ at $u$. Orient $C_2$ with the reversed traversal, so flow $1$ on its edges leaves an excess of $-2$ at $v$. Now set $f(uv)=2$ with $uv$ directed $u\to v$, contributing $-2$ at $u$ (tail) and $+2$ at $v$ (head). Then

$$\text{at } u:\; (+2) + (-2) = 0, \qquad \text{at } v:\; (-2) + (+2) = 0,$$

and all other vertices were already balanced. So $f$ takes values in $\{1,2\}$: a nowhere-zero $3$-flow, hence $\Phi(B)\le 3$.

$\Phi(B)\ge 3$: a nowhere-zero $2$-flow would force $|f(e)|=1$ on every edge. Vertex $u$ has degree $3$, so $\sum_{e\ni u}\tau(e,u)f(e)$ is a sum of three terms each $\pm1$, hence odd, hence nonzero. Therefore $\Phi(B)=3$.

**Why this is the crux.** The value $2$ on the handle $uv$ is forced by the unbalance of $C_1$ and $C_2$. In a large signed graph, many barbells overlap, and every naive combination of their flows multiplies handle values. Controlling this multiplication down to a global maximum of $5$ is exactly the content of Bouchet's conjecture; the best current control (DeVos) leaves the maximum at $11$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*