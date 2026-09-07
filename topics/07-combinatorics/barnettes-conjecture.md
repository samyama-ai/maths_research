---
id: 07-combinatorics/barnettes-conjecture
title: "Barnette's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Barnette's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/barnettes-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Barnette, 1969).** Every $3$-connected cubic planar bipartite graph is Hamiltonian.

Equivalently, in polyhedral language: the graph of every simple $3$-polytope all of whose faces have an even number of sides has a Hamiltonian cycle.

The three hypotheses — $3$-connectivity, cubicity plus planarity, and bipartiteness — are all used. A proof must produce, for every graph $G$ in the class, a cycle through all $|V(G)|$ vertices; a disproof must exhibit one such $G$ with no spanning cycle. Verified counterexamples would have to have at least $86$ vertices (Section 4), so a disproof is necessarily a large explicit construction or a non-constructive parity/obstruction argument.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite simple graph.

- $G$ is **cubic** (3-regular) if $\deg(v)=3$ for all $v\in V$.
- $G$ is **$3$-connected** if $|V|\ge 4$ and $G-S$ is connected for every $S\subseteq V$ with $|S|\le 2$.
- $G$ is **planar** if it embeds in $S^2$; by **Steinitz's theorem**, a graph is the $1$-skeleton of a convex $3$-polytope iff it is planar and $3$-connected. Whitney's theorem gives that a $3$-connected planar graph has an essentially unique embedding, so its **face set** $F$ is a graph invariant.
- $G$ is **bipartite** iff it has no odd cycle. For a planar embedding this is equivalent to every face being bounded by an even number of edges.
- A **Hamiltonian cycle** is a cycle $C\subseteq E$ with $V(C)=V$.

**Counting identity.** For cubic planar $G$ with $n=|V|$: $|E|=\tfrac{3n}{2}$ and, by Euler's formula $n-|E|+|F|=2$, $|F|=\tfrac{n}{2}+2$. Writing $f_k$ for the number of faces of size $k$,
$$\sum_k f_k = \frac{n}{2}+2, \qquad \sum_k k\,f_k = 2|E| = 3n .$$
Eliminating $n$ gives the discharging identity
$$\sum_k (k-6)\,f_k = -12 .$$
For a Barnette graph all $k$ are even and $k\ge 4$ (no multi-edges, $3$-connected), so
$$2 f_4 = 12 + \sum_{k\ge 8} (k-6) f_k \;\;\Longrightarrow\;\; f_4 \ge 6 .$$
Every member of the class therefore has at least six quadrilateral faces.

**Grinberg's condition.** If a planar graph with a Hamiltonian cycle $C$ has $f'_k$ (resp. $f''_k$) faces of size $k$ inside (resp. outside) $C$, then
$$\sum_k (k-2)\,(f'_k - f''_k) = 0 .$$
For bipartite graphs every $k$ is even, so $k-2$ is even and the identity is a congruence modulo $2$ that is automatically satisfied — Grinberg's obstruction, the engine behind almost all known non-Hamiltonian planar examples, is vacuous here. This is the structural reason the conjecture is hard.

**Tait's theorem.** A bridgeless cubic planar graph is $3$-edge-colourable (equivalent to the Four Colour Theorem), and a Hamiltonian cubic graph is $3$-edge-colourable; the converse fails, so edge colourings give no traction.

## 3. History & State of the Art (SOTA)

- **1884.** P. G. Tait conjectured every $3$-connected cubic planar graph is Hamiltonian, which would have implied the Four Colour Theorem.
- **1946.** W. T. Tutte disproved Tait with a $46$-vertex counterexample built from the "Tutte fragment".
- **1956.** Tutte proved every $4$-connected planar graph is Hamiltonian. This cannot apply here: a cubic graph has vertex connectivity at most $3$.
- **1968.** Grinberg's criterion supplies a systematic non-Hamiltonicity test — but it degenerates for bipartite planar graphs (Section 2).
- **1969.** D. W. Barnette proposed the conjecture in *Recent Progress in Combinatorics* (Tutte, ed.), listed as Conjecture 5. A companion conjecture — all $3$-connected cubic planar graphs with faces of size $\le 6$ are Hamiltonian — was settled affirmatively by Kardoš (2020, computer-assisted).
- **1975.** Goodey proved the case where all faces have size $4$ or $6$.
- **1985–2000.** Exhaustive computer searches raised the verified vertex bound from $64$ (Holton–Manvel–McKay) to $84$ (Aldred–Bau–Holton–McKay).
- **1988.** Holton and McKay showed the smallest counterexample to Tait's conjecture has $38$ vertices — evidence that non-Hamiltonian cubic $3$-connected planar graphs are abundant once bipartiteness is dropped.
- **2006.** Feder and Subi showed that if Barnette's conjecture is false, then deciding Hamiltonicity within the class is NP-complete — so either the conjecture holds or the class is computationally as hard as the general planar case.
- **2016–2020.** Alt–Payne–Schmidt–Wood proposed reduction-based strengthenings; Bagheri Gh., Feder, Fleischner and Subi obtained new partial results via facial $2$-factors.

Status as of 2026: open, widely believed true, no counterexample known and no proof strategy known to be complete.

## 4. Partial Results / Verified Cases

- **Face-size restrictions.** Goodey (1975): true if $f_k=0$ for all $k\notin\{4,6\}$. Kardoš (2020): all $3$-connected cubic planar graphs with $f_k=0$ for $k>6$ (the Barnette–Goodey setting, including fullerene graphs) are Hamiltonian — this covers the bipartite subcase $\{4,6\}$ independently.
- **Small orders.** Verified for all $n\le 64$ (Holton, Manvel, McKay 1985) and extended to $n\le 84$ (Aldred, Bau, Holton, McKay 2000). Any counterexample has $n\ge 86$ (order is even; $f_4\ge 6$).
- **Facial $2$-factors.** Bagheri Gh., Feder, Fleischner, Subi (2020) prove Hamiltonicity for Barnette graphs admitting a $2$-factor consisting of facial cycles of restricted sizes, a class strictly larger than Goodey's.
- **Equivalent strengthenings.** Kelmans (1994) and Florek (2010) show Barnette's conjecture is equivalent to formally stronger statements about Hamiltonian cycles through prescribed edges of a common face — so no loss of generality is incurred by demanding more.
- **Sharpness of each hypothesis.**
  - Drop bipartiteness: Tutte (1946), $46$ vertices; minimum $38$ (Holton–McKay 1988).
  - Drop planarity: Georges (1989) constructs $3$-connected non-Hamiltonian bicubic graphs.
  - Drop $3$-connectivity: Hamiltonicity for $2$-connected cubic bipartite planar graphs is NP-complete (Akiyama, Nishizeki, Saito 1980).

## 5. Principal Obstacles

- **Grinberg is silent.** The only general-purpose certificate of non-Hamiltonicity for planar graphs vanishes modulo $2$ on bipartite faces. There is no known replacement invariant, so even a *disproof* has no candidate obstruction to aim at; counterexample hunting is blind search.
- **Connectivity ceiling.** Tutte's $4$-connected theorem and its descendants (Thomassen's Hamiltonian-connectedness, Sanders' results on cycles through prescribed edges) all require connectivity $\ge 4$, unattainable for cubic graphs. Passing to the cyclic connectivity variant loses the induction.
- **No stable reduction.** Standard cubic-graph induction contracts a face or a $4$-cycle. Contracting a quadrilateral face of a Barnette graph typically destroys bipartiteness or $3$-connectivity, so the class is not closed under any known reduction — inductive proofs collapse at the first step.
- **Complexity barrier.** By Feder–Subi, a proof of the conjecture is a polynomial-time algorithm (output "yes" always); a disproof implies NP-completeness. Any partial method that both certifies and searches efficiently on a subclass hits this dichotomy, ruling out purely local/greedy arguments unless they extend to everything.
- **Discharging saturates.** Kardoš's success on $f_k=0$ for $k>6$ used the fact that face sizes are bounded, keeping the discharging rules finite. Barnette graphs admit arbitrarily large faces ($f_k>0$ for any even $k$), so the reducible-configuration list is not finite by the same argument.

## 6. The Gap

Proven: all $n\le 84$; all instances whose faces have size $4$ or $6$; instances with suitable facial $2$-factors. Open: instances with $n\ge 86$ containing at least one face of size $\ge 8$.

Concretely, the identity $2f_4 = 12 + \sum_{k\ge 8}(k-6) f_k$ says that large faces are paid for by extra quadrilaterals. The missing step is a mechanism that converts that surplus of $4$-faces into a spanning cycle — either a finite reducible-configuration set that survives unbounded face sizes, or a bipartite analogue of Grinberg's identity strong enough to be non-vacuous. Neither exists.

## 7. Current Research (as of June 2026)

- **Extending computer verification.** Plantri-based generation of cubic planar bipartite $3$-connected graphs coupled with SAT/ILP Hamiltonicity tests; the bottleneck is the growth of the class beyond $n\approx 90$, not the Hamiltonicity check. *(frontier — verify)* Claims of verification past $n=100$ circulate but no refereed extension of the $84$-vertex bound is confirmed.
- **Kardoš-style computer-assisted discharging.** Attempts to adapt the fullerene proof by imposing a bound on face size and letting the bound grow; each fixed bound is a genuine theorem, but the family of proofs does not obviously converge. *(frontier — verify)*
- **Reduction/strengthening programme.** Following Alt, Payne, Schmidt and Wood (2016), searching for a strengthened statement closed under a reduction operation, so that induction can run. Groups at Monash and TU Berlin have pursued variants.
- **Facial $2$-factor and transition-system methods.** Continuation of the Feder–Fleischner–Subi line, treating Hamiltonian cycles as compatible transitions in an Eulerian-type auxiliary structure.
- **Structural-complexity framing.** Studying which subclasses admit polynomial Hamiltonicity algorithms, given that unconditional NP-completeness for the class would refute the conjecture.

## 8. Future Work

- Find a bipartite-planar invariant that is a genuine (non-degenerate) obstruction to Hamiltonicity, replacing Grinberg's identity modulo $4$ or in a $\mathbb{Z}$-valued refinement.
- Prove the conjecture under a bound $k\le K$ on face size for $K=8,10,\dots$ via discharging, and look for a uniform-in-$K$ argument.
- Establish Barnette's conjecture for cyclically $5$-connected members, isolating the small-cut cases for separate treatment.
- Develop a strengthening closed under quadrilateral-face contraction, converting the class into an inductively usable one (the Alt–Payne–Schmidt–Wood strategy).
- Push exhaustive search to $n\approx 100$ with canonical-construction-path generation; a counterexample, if it exists, plausibly lies well beyond, but the data constrains conjectured cycle counts.

## 9. Key References

- **[Foundational]** D. W. Barnette. *Conjecture 5.* In W. T. Tutte (ed.), **Recent Progress in Combinatorics**, Academic Press, 1969, p. 343.
- **[Foundational]** W. T. Tutte. *On Hamiltonian circuits.* Journal of the London Mathematical Society, 21 (1946), 98–101.
- **[Foundational]** W. T. Tutte. *A theorem on planar graphs.* Transactions of the American Mathematical Society, 82 (1956), 99–116.
- **[Foundational]** E. Grinberg. *Plane homogeneous graphs of degree three without Hamiltonian circuits.* Latvian Math. Yearbook, 4 (1968), 51–58.
- **[Partial]** P. R. Goodey. *Hamiltonian circuits in polytopes with even sides.* Israel Journal of Mathematics, 22 (1975), 52–56.
- **[Computational]** D. A. Holton, B. Manvel, B. D. McKay. *Hamiltonian cycles in cubic 3-connected bipartite planar graphs.* Journal of Combinatorial Theory, Series B, 38 (1985), 279–297.
- **[Computational]** D. A. Holton, B. D. McKay. *The smallest non-Hamiltonian 3-connected cubic planar graphs have 38 vertices.* Journal of Combinatorial Theory, Series B, 45 (1988), 305–319.
- **[SOTA / Computational]** R. E. L. Aldred, S. Bau, D. A. Holton, B. D. McKay. *Nonhamiltonian 3-connected cubic planar graphs.* SIAM Journal on Discrete Mathematics, 13 (2000), 25–32.
- **[Complexity]** T. Akiyama, T. Nishizeki, N. Saito. *NP-completeness of the Hamiltonian cycle problem for bipartite graphs.* Journal of Information Processing, 3 (1980), 73–76.
- **[Complexity]** T. Feder, C. Subi. *On Barnette's conjecture.* Electronic Colloquium on Computational Complexity, Report TR06-015, 2006.
- **[Equivalences]** A. K. Kelmans. *Constructions of cubic bipartite 3-connected graphs without Hamiltonian cycles.* American Mathematical Society Translations (2), 158 (1994), 127–140.
- **[Equivalences]** J. J. Florek. *On Barnette's conjecture.* Discrete Mathematics, 310 (2010), 1531–1535.
- **[Related]** J. P. Georges. *Non-Hamiltonian bicubic graphs.* Journal of Combinatorial Theory, Series B, 46 (1989), 121–124.
- **[SOTA / Recent]** F. Kardoš. *A computer-assisted proof of the Barnette–Goodey conjecture: Not only fullerene graphs are Hamiltonian.* SIAM Journal on Discrete Mathematics, 34 (2020), 3–33.
- **[SOTA / Recent]** B. Bagheri Gh., T. Feder, H. Fleischner, C. Subi. *Hamiltonian cycles in planar cubic graphs with facial 2-factors, and a new partial solution of Barnette's Conjecture.* Journal of Graph Theory, 96 (2021), 269–288.
- **[Survey]** A. Alt, M. Payne, J. M. Schmidt, D. R. Wood. *Thoughts on Barnette's conjecture.* Australasian Journal of Combinatorics, 64 (2016), 354–365.

## 10. Worked Example / Concrete Special Case

**The hexagonal prism $Y_6 = C_6 \times K_2$.**

Vertices $u_1,\dots,u_6$ (outer hexagon), $v_1,\dots,v_6$ (inner hexagon), edges $u_iu_{i+1}$, $v_iv_{i+1}$ (indices mod $6$) and rungs $u_iv_i$. Then $n=12$, $|E|=18$, $|F|=8$: two hexagons and six squares.

*Class membership.* Cubic: each $u_i$ meets $u_{i-1},u_{i+1},v_i$. Planar and $3$-connected (a prism over a cycle of length $\ge 3$ is $3$-connected). Bipartite: colour $u_i$ by the parity of $i$, $v_i$ by the opposite parity; every edge joins opposite classes since $6$ is even.

*Counting check.* $f_4=6$, $f_6=2$, so
$$\sum_k (k-6) f_k = 6\cdot(4-6) + 2\cdot(6-6) = -12 \;\checkmark,$$
and $f_4 = 6$ meets the lower bound of Section 2 with equality, since there are no faces of size $\ge 8$.

*Hamiltonian cycle.* Take
$$C: u_1 \to u_2 \to u_3 \to u_4 \to u_5 \to u_6 \to v_6 \to v_5 \to v_4 \to v_3 \to v_2 \to v_1 \to u_1 .$$
All $12$ vertices appear once; the edges used are five outer hexagon edges, five inner hexagon edges, and the two rungs $u_6v_6$, $u_1v_1$ — $12$ edges, as required for a $12$-cycle.

*Why Grinberg gives nothing.* Take $C$ above. Inside $C$ lie the four squares $u_1u_2v_2v_1$, $u_2u_3v_3v_2$, $u_3u_4v_4v_3$, $u_4u_5v_5v_4$ — so $f'_4=4$; outside lie $f''_4=2$ squares and both hexagons split as $f'_6=0$, $f''_6=2$. Grinberg's sum:
$$(4-2)(4-2) + (6-2)(0-2) = 4 - 8 \ne 0 ?$$
The discrepancy shows the naive face count must be corrected: the inner hexagon face $v_1\dots v_6$ is bounded by $C$ on one side, and the correct partition places $f'_4=5$, $f''_4=1$, $f'_6=0$, $f''_6=2$ relative to the chosen embedding orientation, giving $2(5-1)+4(0-2)=8-8=0$ $\checkmark$. The point stands independently: every coefficient $k-2$ is even here, so the identity reduces to $0\equiv 0 \pmod 2$ and can never certify non-Hamiltonicity for a bipartite planar graph.

*Scaling up.* Replacing $C_6$ by $C_{2m}$ gives an infinite Barnette family with $f_4=2m$, $f_{2m}=2$, all Hamiltonian by the same zig-zag. Genuine difficulty starts only when the quadrilateral faces are irregularly distributed among several large faces — exactly the regime, $n\ge 86$ with some $k\ge 8$, that Section 6 identifies as untouched.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*