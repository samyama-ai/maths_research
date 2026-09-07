---
id: 07-combinatorics/lovasz-conjecture-hamiltonian
title: "Lovász Conjecture on Hamiltonian Paths"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lovász Conjecture on Hamiltonian Paths

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/lovasz-conjecture-hamiltonian` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Lovász, 1970).** Every finite connected vertex-transitive graph contains a Hamiltonian path — a path passing through every vertex exactly once.

Lovász in fact posed the problem in the negative direction, asking for a construction of a finite connected vertex-transitive graph with no Hamiltonian path. None has been found in 56 years, and the statement is now universally quoted as a conjecture.

Two strengthenings circulate alongside it:

- **(Cycle form.)** Every finite connected vertex-transitive graph on $n \ge 3$ vertices has a Hamiltonian cycle, except for the four known exceptions listed in §4.
- **(Cayley form.)** Every connected Cayley graph on a finite group of order $\ge 3$ has a Hamiltonian cycle.

A disproof requires exhibiting a single finite connected vertex-transitive graph $X$ with no spanning path (for the cycle forms, an infinite family, or a fifth sporadic exception). A proof requires the statement for all $n$, with no restriction on valency, order, or the structure of $\operatorname{Aut}(X)$.

## 2. Mathematical Foundations

Let $X=(V,E)$ be a finite simple graph and $\operatorname{Aut}(X)$ its automorphism group. $X$ is **vertex-transitive** if $\operatorname{Aut}(X)$ acts transitively on $V$: for all $u,v \in V$ there is $g \in \operatorname{Aut}(X)$ with $g(u)=v$. Vertex-transitivity forces regularity, $\deg(v)=d$ for all $v$, and $|V| \mid |\operatorname{Aut}(X)|$.

A **Cayley graph** $\operatorname{Cay}(G,S)$ for a finite group $G$ and $S \subseteq G \setminus \{1\}$ with $S = S^{-1}$ has vertex set $G$ and edges $\{g, gs\}$ for $g\in G$, $s \in S$. It is connected iff $\langle S\rangle = G$, and is vertex-transitive because $G$ acts regularly on itself by left multiplication. By **Sabidussi's theorem**, $X$ is a Cayley graph iff $\operatorname{Aut}(X)$ contains a subgroup acting regularly on $V$. Vertex-transitive graphs strictly contain Cayley graphs: the Petersen graph is vertex-transitive with $\operatorname{Aut} \cong S_5$, which has no regular subgroup of order $10$.

A **Hamiltonian path** is a sequence $v_1,\dots,v_n$ with $\{v_i,v_{i+1}\}\in E$ and $\{v_i\} = V$; a **Hamiltonian cycle** adds $\{v_n,v_1\}\in E$. In $\operatorname{Cay}(G,S)$ a Hamiltonian cycle is exactly a sequence $s_1,\dots,s_n \in S$ with
$$\prod_{i=1}^{n} s_i = 1, \qquad \text{all partial products } \prod_{i=1}^{k} s_i \ (1\le k \le n) \text{ distinct},$$
so the conjecture becomes a purely group-theoretic statement about *Hamiltonian sequences* in $G$.

The standard structural tool is **quotienting**: if $N \trianglelefteq G$, then $\operatorname{Cay}(G,S)$ maps onto $\operatorname{Cay}(G/N, SN/N)$, and one attempts to lift a Hamiltonian cycle of the quotient through the fibres. For general vertex-transitive $X$ with $K \le \operatorname{Aut}(X)$ semiregular, the quotient $X/K$ is defined on $K$-orbits; the fibres are then blocks of imprimitivity, and lifting requires the **Alspach lifting lemma**: a Hamiltonian cycle in $X/K$ whose lift contains a cycle traversing the fibres coherently yields a Hamiltonian cycle in $X$.

Two ancillary invariants: the **circumference** $c(X)$ (longest cycle length), and Babai's bound
$$c(X) \ \ge\ \sqrt{3n} \qquad \text{for every connected vertex-transitive } X \text{ on } n \text{ vertices.}$$

## 3. History & State of the Art (SOTA)

- **1969/1970.** Lovász posed the problem (Problem 11) at the Calgary conference on combinatorial structures; published in *Combinatorial Structures and Their Applications*, Gordon and Breach, 1970.
- **1970s–80s.** The directed analogue is settled negatively: Rankin's earlier work on $\{a,b\}$-generated groups and Witte's analysis show Cayley *digraphs* need not be Hamiltonian, so any proof must use edge-reversal.
- **1979.** Babai gives the first general circumference bound $c(X)\ge\sqrt{3n}$ — still the shape of the best unconditional bound for four decades.
- **1981.** Chen and Quimpo settle abelian groups: every connected Cayley graph on an abelian group of order $\ge 3$ and valency $\ge 2$ is Hamiltonian (indeed Hamiltonian-connected or Hamiltonian-laceable).
- **1983–2009.** Marušič, Alspach, Kutnar and collaborators push the "order with few prime factors" programme via quotient/lifting arguments.
- **2007–2012.** Glover–Marušič and successors settle cubic Cayley graphs on $(2,s,3)$-generated groups: a Hamiltonian path always exists, and a Hamiltonian cycle in most congruence classes.
- **2014.** Christofides, Hladký and Máthé prove the dense case: there is $c>0$ such that for large $n$, every connected vertex-transitive graph of valency $\ge cn$ is Hamiltonian.
- **2020s.** DeVos improves Babai's exponent to $c(X)=\Omega(n^{3/5})$ *(frontier — verify)*.

Competing beliefs are on record. Thomassen conjectures only finitely many connected vertex-transitive graphs are non-Hamiltonian (so the four known exceptions are all). Babai conjectures the opposite extreme: there is $\varepsilon>0$ and infinitely many vertex-transitive graphs with $c(X)<(1-\varepsilon)n$.

## 4. Partial Results / Verified Cases

**Exceptions to the cycle form.** Exactly four connected vertex-transitive graphs on $\ge 3$ vertices are known with no Hamiltonian cycle: the Petersen graph ($n=10$), the Coxeter graph ($n=28$), and the two graphs obtained from them by replacing each vertex with a triangle ($n=30$, $n=84$). ($K_2$ is a fifth if $n=2$ is admitted.) All four have Hamiltonian paths, and none is a Cayley graph — consistent with the Cayley form.

**Solved classes.**

- **Order.** Hamiltonicity holds for connected vertex-transitive graphs of order $p$, $2p$, $3p$, $4p$, $5p$, $6p$, $10p$, $p^2$, $p^3$, $2p^2$ for $p$ prime (Marušič; Alspach; Kutnar–Marušič; Kutnar–Šparl), with the Petersen graph ($n=2\cdot 5$) and Coxeter graph ($n=4\cdot 7$) as the only exceptions in those ranges.
- **Cayley, few prime factors.** Kutnar–Marušič–D. W. Morris–J. Morris–Šparl (2012): every connected Cayley graph of order $kp$, $kp^2$ or $kp^3$ with $k\le 31$ (and various orders $pqr$) has a Hamiltonian cycle.
- **Group structure.** Abelian groups (Chen–Quimpo 1981); groups with cyclic commutator subgroup of prime-power order (Keating–Witte 1985); $p$-groups — even the digraph case (Witte 1986); dihedral groups, and $\operatorname{Cay}(G,S)$ whenever $|G|$ has at most three prime factors counted with multiplicity, in many configurations.
- **Valency.** Cubic Cayley graphs of $(2,s,3)$-generated groups: Hamiltonian path always; Hamiltonian cycle for $s \equiv 0 \pmod 4$ and for $s$ odd (Glover–Marušič 2007; Glover–Kutnar–Marušič 2009; Glover–Kutnar–Malnič–Marušič 2012).
- **Dense valency.** $d \ge cn$, $n$ large (Christofides–Hladký–Máthé 2014).
- **Computation.** Exhaustive machine search over all connected vertex-transitive graphs of order $n \le 47$ (and all Cayley graphs in comparable ranges) finds no further non-Hamiltonian example and no vertex-transitive graph without a Hamiltonian path.

## 5. Principal Obstacles

- **No global invariant obstructs Hamiltonicity.** Toughness, connectivity ($\kappa = d$ for connected vertex-transitive graphs by Mader/Watkins), and expansion are all favourable; there is no counting or parity invariant whose vanishing would certify a Hamiltonian path, so extremal and probabilistic methods give circumference lower bounds, not spanning structures.
- **Quotient/lifting stalls on primitive actions.** The one method that works — descend to $X/K$, lift — requires a nontrivial block system. Vertex-transitive graphs whose automorphism group acts *primitively* (e.g. many graphs on $p$ or $p^2$ vertices in general position, or graphs with $\operatorname{Aut}$ almost simple) admit no proper quotient, and every proof in §4 breaks down.
- **Sporadic exceptions rule out clean induction.** Petersen and Coxeter show any induction on order or valency must carry exceptional cases through, and truncation shows exceptions propagate to larger orders. No known induction is robust to this.
- **The digraph analogue is false.** Since directed Cayley graphs can fail to be Hamiltonian, any successful argument must genuinely use $S=S^{-1}$, ruling out all purely word-combinatorial arguments on generating sequences.
- **Regularity/absorption methods need density.** The Christofides–Hladký–Máthé proof uses the regularity method plus a structural decomposition valid only for $d = \Omega(n)$; sparse vertex-transitive graphs (cubic Cayley graphs of large simple groups) fall entirely outside it.
- **Circumference gap.** Even the weak question is open: no proof gives $c(X) \ge \varepsilon n$ for all vertex-transitive $X$. The gap between $\Omega(n^{3/5})$ and $n$ is the honest measure of ignorance.

## 6. The Gap

Proven: Hamiltonian cycles/paths for graphs with a usable imprimitivity structure (orders with few prime factors, abelian or nilpotent-like groups, cubic $(2,s,3)$ groups), plus the dense regime $d=\Omega(n)$. Conjectured: all $n$, all valencies, all automorphism groups.

The exact barrier is **sparse plus primitive**: a connected vertex-transitive graph of bounded valency whose automorphism group acts primitively (equivalently, has no proper semiregular quotient usable for lifting), on an order with many prime factors. Cubic Cayley graphs of nonabelian finite simple groups sit precisely there. Crossing the gap means producing a spanning-path construction that does not consume a block system — a method with no current prototype. Weakening the target, the first meaningful milestone is $c(X)\ge \varepsilon n$ for a fixed $\varepsilon>0$, which would refute Babai's counter-conjecture and is itself wide open.

## 7. Current Research (as of June 2026)

- **Ljubljana/Primorska school (Marušič, Kutnar, Šparl, Malnič).** Continues the order-classification programme, extending the $kp^m$ families and analysing vertex-transitive graphs whose quotient is a Cayley graph on a small group.
- **Morris school (D. W. Morris, J. Morris, Lethbridge).** Systematically extends the "few prime factors" ceiling for Cayley graphs and maintains a running catalogue of settled orders; recent work targets Cayley graphs on solvable groups of order $2^a p$.
- **Circumference programme.** After DeVos's $\Omega(n^{3/5})$ improvement *(frontier — verify)*, several groups are attacking the exponent via cycle-space and rotation arguments adapted to transitive actions; no linear bound has been announced.
- **Regularity/absorption extensions.** Attempts to lower the density threshold in Christofides–Hladký–Máthé below $d = \Omega(n)$, e.g. to $d = n^{1-\delta}$, using sparse regularity and the expansion guaranteed by transitivity *(frontier — verify)*.
- **Computer search.** Enumeration of vertex-transitive graphs (Holt–Royle census, $n \le 47$ and beyond) continues to test for a fifth exception; nothing new has appeared.

## 8. Future Work

- Prove $c(X) \ge \varepsilon n$ for all connected vertex-transitive $X$ — the consensus next target, since it separates Thomassen's and Babai's positions.
- Settle cubic Cayley graphs of nonabelian finite simple groups, the canonical sparse-primitive test case; a positive answer would validate a genuinely new technique.
- Complete the $(2,s,3)$ programme in the remaining congruence classes ($s \equiv 2 \pmod 4$), where only a Hamiltonian path is currently guaranteed.
- Push absorption/regularity to sub-linear valency, closing the range $n^{3/5} \ll d \ll n$.
- Decide whether the four exceptions are all: prove that a non-Hamiltonian connected vertex-transitive graph must be a truncation of a smaller one.

## 9. Key References

- **[Foundational]** L. Lovász. *Problem 11*, in **Combinatorial Structures and Their Applications** (Proc. Calgary Internat. Conf., 1969), Gordon and Breach, New York, 1970, pp. 243–246.
- **[Foundational]** L. Babai. *Long cycles in vertex-transitive graphs.* **Journal of Graph Theory** 3 (1979), 301–304.
- **[Foundational]** C. C. Chen, N. F. Quimpo. *On strongly Hamiltonian abelian group graphs.* In **Combinatorial Mathematics VIII**, Lecture Notes in Mathematics 884, Springer, 1981, 23–34.
- **[Foundational]** D. Witte. *Cayley digraphs of prime-power order are Hamiltonian.* **Journal of Combinatorial Theory, Series B** 40 (1986), 107–112.
- **[Structural]** B. Alspach. *Lifting Hamilton cycles of quotient graphs.* **Discrete Mathematics** 78 (1989), 25–36.
- **[Structural]** D. Marušič. *Hamiltonian circuits in Cayley graphs.* **Discrete Mathematics** 46 (1983), 49–54.
- **[SOTA]** H. Glover, D. Marušič. *Hamiltonicity of cubic Cayley graphs.* **Journal of the European Mathematical Society** 9 (2007), 775–787.
- **[SOTA]** H. Glover, K. Kutnar, D. Marušič. *Hamiltonian cycles in cubic Cayley graphs: the $\langle 2,4k,3\rangle$ case.* **Journal of Algebraic Combinatorics** 30 (2009), 447–475.
- **[SOTA]** K. Kutnar, D. Marušič, D. W. Morris, J. Morris, P. Šparl. *Hamiltonian cycles in Cayley graphs whose order has few prime factors.* **Ars Mathematica Contemporanea** 5 (2012), 27–71.
- **[SOTA]** D. Christofides, J. Hladký, A. Máthé. *Hamilton cycles in dense vertex-transitive graphs.* **Journal of Combinatorial Theory, Series B** 109 (2014), 34–72.
- **[Survey]** D. Witte, J. A. Gallian. *A survey: Hamiltonian cycles in Cayley graphs.* **Discrete Mathematics** 51 (1984), 293–304.
- **[Survey]** S. J. Curran, J. A. Gallian. *Hamiltonian cycles and paths in Cayley graphs and digraphs — a survey.* **Discrete Mathematics** 156 (1996), 1–18.
- **[Survey]** K. Kutnar, D. Marušič. *Hamilton cycles and paths in vertex-transitive graphs — current directions.* **Discrete Mathematics** 309 (2009), 5491–5500.

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$: vertex-transitive, no Hamiltonian cycle, but a Hamiltonian path.**

Vertices $u_0,\dots,u_4$ (outer $5$-cycle, $u_i \sim u_{i+1}$), $v_0,\dots,v_4$ (inner pentagram, $v_i \sim v_{i\pm2}$), spokes $u_i \sim v_i$; indices mod $5$. $P$ is cubic, $n=10$, $\operatorname{Aut}(P)\cong S_5$ acts transitively on vertices.

*No Hamiltonian cycle.* Let $H$ be one, using $k$ spokes. Contracting the outer cycle and inner pentagram separately shows $k$ is even, so $k\in\{0,2,4\}$.

- $k=0$: $H$ lies inside the two disjoint $5$-cycles — not spanning.
- $k=2$: $H$ decomposes into a Hamiltonian path of the outer $C_5$ from $u_i$ to $u_j$, a Hamiltonian path of the inner pentagram from $v_i$ to $v_j$, and the two spokes. A Hamiltonian path of a $5$-cycle omits exactly one edge, so its ends are adjacent: $j \equiv i\pm1$. In the pentagram, adjacency means $j \equiv i\pm2$. Both cannot hold mod $5$.
- $k=4$: say spoke $u_0v_0$ is omitted. Then $u_0$ uses both outer edges $u_4u_0,u_0u_1$; each other $u_i$ uses its spoke plus exactly one outer edge, giving $ (2+4)/2 = 3$ outer edges. Since $u_1$ and $u_4$ are already saturated, the third is $u_2u_3$. Symmetrically the inner edges are $v_0v_2, v_0v_3, v_1v_4$. Now follow: $u_4 u_0 u_1 \to v_1 \to v_4 \to u_4$, a closed $5$-cycle on $\{u_4,u_0,u_1,v_1,v_4\}$ — a proper subcycle, contradiction.

Hence $c(P)=9 < 10$.

*A Hamiltonian path.* Take
$$u_0 \to u_1 \to u_2 \to u_3 \to u_4 \to v_4 \to v_1 \to v_3 \to v_0 \to v_2 .$$
Every consecutive pair is an edge: the $u$-steps are outer-cycle edges, $u_4v_4$ is a spoke, and $v_4v_1$ ($4+2\equiv1$), $v_1v_3$, $v_3v_0$ ($3+2\equiv0$), $v_0v_2$ are pentagram edges. All ten vertices appear once.

$P$ is therefore an exception to the cycle form and an instance of the path form. Note $P$ is *not* a Cayley graph: $S_5$ has no subgroup of order $10$ acting regularly on the $10$ vertices (its only order-$10$ subgroups are the dihedral point stabilisers' complements, which fix a $2$-subset and hence are not regular here). This is exactly why the Cayley form has no known exceptions while the vertex-transitive cycle form has four.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*