---
id: 10-theoretical-cs/graph-isomorphism-complexity
title: "Graph Isomorphism Complexity"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Graph Isomorphism Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/graph-isomorphism-complexity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Given two finite simple graphs $G$ and $H$ on $n$ vertices, decide whether there is a bijection $\varphi: V(G) \to V(H)$ with $\{u,v\} \in E(G) \iff \{\varphi(u),\varphi(v)\} \in E(H)$. The decision problem is $\mathsf{GI}$.

The open question: **what is the exact complexity of $\mathsf{GI}$?** Concretely:

1. Is $\mathsf{GI} \in \mathsf{P}$? No polynomial-time algorithm is known.
2. Is $\mathsf{GI}$ $\mathsf{NP}$-complete? Believed no; it is not, unless the polynomial hierarchy collapses to $\Sigma_2^p$.
3. Is $\mathsf{GI}$ $\mathsf{NP}$-intermediate in the sense of Ladner, i.e. neither in $\mathsf{P}$ nor $\mathsf{NP}$-complete?

The status is *partially-solved*: Babai (2016) gave a quasipolynomial algorithm running in time $\exp\big((\log n)^{O(1)}\big)$, which rules out the problem being hard in any conventional sense but leaves the $\mathsf{P}$ question open. A complete resolution means either a polynomial-time algorithm (equivalently, polynomial-time *canonical labelling*), or a proof of hardness under a credible complexity assumption.

## 2. Mathematical Foundations

**Automorphism group.** $\mathrm{Aut}(G) \le \mathrm{Sym}(V)$ is the stabiliser of $E(G)$ under the induced action on $\binom{V}{2}$. If $G \cong H$, the set of isomorphisms is a coset $\varphi\,\mathrm{Aut}(G)$, so isomorphism testing, automorphism-group computation and canonical form computation are polynomial-time equivalent for graphs.

**Canonical form.** A map $\mathrm{Can}$ with $\mathrm{Can}(G) \cong G$ and $\mathrm{Can}(G)=\mathrm{Can}(H) \iff G \cong H$. Canonisation solves $\mathsf{GI}$; the converse reduction is Babai–Luks (1983) via individualisation-refinement.

**Color refinement (1-WL).** Start with $\chi^0(v)=1$ and iterate
$$\chi^{i+1}(v) = \Big(\chi^i(v),\ \{\!\{\chi^i(u) : u \in N(v)\}\!\}\Big),$$
where $\{\!\{\cdot\}\!\}$ is a multiset. The partition stabilises in $\le n$ rounds. If the stable color multisets of $G$ and $H$ differ, $G \not\cong H$.

**$k$-dimensional Weisfeiler–Leman ($k$-WL).** Colors $k$-tuples $\bar v \in V^k$ by their atomic type, then iterates
$$\chi^{i+1}(\bar v) = \Big(\chi^i(\bar v),\ \{\!\{\big(\chi^i(\bar v[1/w]),\dots,\chi^i(\bar v[k/w])\big) : w \in V\}\!\}\Big).$$
The **WL-dimension** of $G$ is the least $k$ such that $k$-WL distinguishes $G$ from every non-isomorphic $H$. By Immerman–Lander (1990), $k$-WL is exactly as expressive as the logic $C^{k+1}_{\infty\omega}$ ($(k+1)$-variable first-order logic with counting quantifiers). $k$-WL runs in time $n^{O(k)}$.

**Group-theoretic setting.** Luks's method reduces $\mathsf{GI}$ on structures to *string isomorphism*: given $G \le \mathrm{Sym}(\Omega)$ by generators and strings $\mathfrak{x},\mathfrak{y}:\Omega \to \Sigma$, decide whether $\mathrm{Iso}_G(\mathfrak{x},\mathfrak{y}) = \{\sigma \in G : \mathfrak{x}^\sigma = \mathfrak{y}\} \neq \emptyset$. Divide-and-conquer along an imprimitivity system works whenever the primitive quotients are small; the barrier is primitive groups of large order, classified by Cameron's theorem as (essentially) *Johnson groups* $A_m^{(k)}$ acting on $\binom{[m]}{k}$ up to bounded-index extensions.

**Complexity placement.**
$$\mathsf{GI} \in \mathsf{NP} \cap \mathsf{coAM}, \qquad \mathsf{GI} \in \mathsf{SPP} \subseteq \mathsf{PP},$$
and $\mathsf{GI}$ is *low* for $\mathsf{PP}$ and for $\Sigma_2^p$ (Schöning 1988; Arvind–Kurur 2006). Hence if $\mathsf{GI}$ were $\mathsf{NP}$-complete, $\mathsf{PH} = \Sigma_2^p$ (Boppana–Håstad–Zachos 1987).

## 3. History & State of the Art (SOTA)

- **1970s.** The problem is singled out in Karp's 1972 list as one of the few natural problems neither known in $\mathsf{P}$ nor $\mathsf{NP}$-complete. Weisfeiler and Leman introduce the refinement method (1968).
- **1979–1983.** Babai gives a Las Vegas polynomial algorithm for graphs of bounded color class size; Babai–Erdős–Selkow (1980) give linear-average-time canonisation for random graphs. Zemlyachenko–Korneenko–Tyshkevich reduce the general worst case to $\exp\big(O(\sqrt{n \log n})\big)$ (1982) — the moderately exponential bound that stood for 33 years.
- **1982.** Luks: isomorphism of graphs of bounded degree $d$ in time $n^{O(d)}$, the origin of the group-theoretic method.
- **1987–1992.** Complexity-theoretic evidence against hardness (Goldwasser–Micali–Rackoff zero-knowledge protocol; Boppana–Håstad–Zachos; Schöning lowness). Cai–Fürer–Immerman (1992) prove $\Omega(n)$-dimensional WL is needed in the worst case.
- **2015–2017.** Babai announces and publishes a $\exp\big((\log n)^{O(1)}\big)$ algorithm (STOC 2016). Helfgott finds a gap in the *split-or-Johnson* routine in January 2017; Babai repairs it within days, and Helfgott's Bourbaki exposition (2017) independently verifies the argument. The published exponent is $O((\log n)^3)$ after the fix.
- **2018–2023.** Grohe–Neuen–Schweitzer improve bounded-degree testing to $n^{O((\log d)^{c})}$, breaking Luks's $n^{O(d)}$. Neuen and Wiebking extend quasipolynomial techniques to excluded topological subgraphs and to hypergraphs.

**Practice.** `nauty`/`Traces` (McKay–Piperno 2014) and `bliss` solve almost all graphs with thousands of vertices in milliseconds; the only hard instances are engineered (CFI graphs, Miyazaki graphs, strongly regular graphs, Hadamard-design incidence graphs).

## 4. Partial Results / Verified Cases

Polynomial time (in many cases linear or canonical) is known for:

| Class | Bound | Source |
|---|---|---|
| Trees | $O(n)$ | Aho–Hopcroft–Ullman (1974) |
| Planar graphs | $O(n)$ | Hopcroft–Wong (1974); Datta et al. put it in $\mathsf{L}$ (2009) |
| Bounded genus $g$ | $O(n)$, constant depends on $g$ | Miller (1980); Kawarabayashi (2015) |
| Bounded degree $d$ | $n^{O(d)}$, improved to $n^{O((\log d)^c)}$ | Luks (1982); Grohe–Neuen–Schweitzer (2023) |
| Bounded treewidth $k$ | $2^{O(k^5\log k)} n^{O(1)}$ (FPT) | Lokshtanov–Pilipczuk–Pilipczuk–Saurabh (2017) |
| Bounded eigenvalue multiplicity | $n^{O(1)}$ | Babai–Grigoryev–Mount (1982) |
| Bounded rank width / clique width | FPT, canonical | Grohe–Neuen (2023) |
| Graphs excluding a fixed minor or topological subgraph | $n^{O(1)}$ / FPT | Grohe (2017); Grohe–Marx; Neuen (2022) |
| Interval, permutation, circular-arc graphs | $O(n+m)$ | Lueker–Booth (1979) and successors |
| Random $G(n,1/2)$ | $O(n)$ average, w.h.p. | Babai–Erdős–Selkow (1980) |
| Strongly regular graphs | $\exp\big(\tilde O(n^{1/3})\big)$ | Babai–Chen–Sun–Teng–Wilmes (2013); Spielman (1996) |
| Tournaments | $n^{O(\log n)}$ | Babai–Luks (1983) |
| Groups of order $n$ (isomorphism) | $n^{O(\log n)}$ | Tarjan; Miller (1978) |

General case: $\exp\big(O((\log n)^3)\big)$ (Babai 2016). WL-dimension is bounded by a constant on every class listed above except bounded degree; e.g. planar graphs have WL-dimension $\le 3$ (Kiefer–Ponomarenko–Schweitzer 2019).

## 5. Principal Obstacles

- **Combinatorial refinement provably fails.** Cai–Fürer–Immerman construct graphs $X_k$ with $O(k)$ vertices that $k$-WL cannot distinguish, so *any* fixed-dimension counting refinement is defeated. This kills the entire class of "individualise a bounded number of vertices, then refine" algorithms as a route to $\mathsf{P}$.
- **Group theory is the bottleneck at Johnson groups.** In Luks's framework the recursion is cheap unless a primitive quotient has order $n^{\Theta(\log n)}$. By Cameron's classification these are the Johnson/Cameron groups. Babai's *split-or-Johnson* and *local certificates* machinery handles them, but at the cost of a $(\log n)^{O(1)}$ recursion depth that is intrinsic: each level either shrinks the domain by a $\log$ factor or extracts a Johnson structure, never by a constant factor.
- **Coherent configurations resist.** The hardest instances (strongly regular graphs, Steiner systems, Latin-square graphs) are *primitive coherent configurations* of rank $3$ where local structure carries no information. Progress here relies on delicate spectral and design-theoretic arguments (Chen–Sun–Teng, Babai–Wilmes) that give $\exp(n^{\epsilon})$, not $n^{O(1)}$.
- **No logic captures $\mathsf{PTIME}$.** Grohe's programme derives polynomial canonisation from definability in fixed-point logic with counting (FPC). On general graphs FPC fails (CFI again), and no candidate logic capturing $\mathsf{PTIME}$ on all structures is known — a Gurevich-conjecture-level obstruction.
- **No hardness route.** Standard reductions cannot make $\mathsf{GI}$ $\mathsf{NP}$-hard without collapsing $\mathsf{PH}$; and $\mathsf{GI}$ is not known to be hard for any class above $\mathsf{DET}$, so lower-bound techniques have essentially no target.

## 6. The Gap

The proven upper bound is $\exp\big(O((\log n)^3)\big)$; the target is $n^{O(1)} = \exp\big(O(\log n)\big)$. The gap is the *recursion depth* of the group-theoretic divide-and-conquer.

Precisely: Babai's algorithm reduces string isomorphism on a domain of size $n$ to instances of size $n/\mathrm{polylog}(n)$ (via local certificates plus split-or-Johnson), yielding depth $\Theta(\log n / \log\log n)$ and multiplicative cost $\mathrm{polylog}(n)$ per level. A polynomial algorithm requires either

- reduction to domain size $n^{1-\epsilon}$ (constant multiplicative shrink factor), or
- a per-level cost that telescopes rather than multiplies, or
- an entirely different handle on rank-3 primitive coherent configurations and Johnson schemes.

No known technique produces a constant-factor domain reduction; the $\log$-factor is forced by the combinatorics of Johnson group actions on $\binom{[m]}{k}$.

## 7. Current Research (as of June 2026)

- **RWTH Aachen (Grohe, Neuen, and collaborators).** Canonisation for structurally restricted classes: bounded rank width, excluded topological subgraphs, and the *"isomorphism is FPT parameterised by Hadwiger number"* programme. Grohe–Neuen's survey (2021) is the standard entry point.
- **Chicago / Babai school.** Refinement of local certificates; the open target is a $\exp\big(O((\log n)^2)\big)$ or $\exp(\tilde O(\log n))$ bound. *(frontier — verify)*
- **Coherent configurations.** Ongoing work by Ponomarenko, Kiefer, Chen, Sun and Wilmes on classifying primitive coherent configurations of small rank and bounding their WL-dimension; the target result is $n^{O(1)}$ for all strongly regular graphs.
- **WL-dimension as a graph parameter.** Kiefer's programme computing exact WL-dimension for structural classes; connected to expressivity limits of message-passing graph neural networks (Morris et al. 2019, Xu et al. 2019), which are exactly 1-WL-bounded — a large applied literature now depends on these bounds.
- **Quantum and fine-grained angles.** No quantum speedup is known beyond generic search; $\mathsf{GI}$ is a hidden-subgroup problem for $S_n$, and the standard coset-state approach is known to need highly entangled measurements (Hallgren–Moore–Rötteler–Russell–Sen 2010) — widely read as evidence against a quantum polynomial algorithm.

## 8. Future Work

- **Push the exponent.** Reduce $\exp((\log n)^3)$ toward $\exp((\log n)^{1+o(1)})$ by improving the split-or-Johnson step; a constant-factor domain reduction would immediately give $n^{O(1)}$.
- **Settle strongly regular graphs.** These are the canonical hard family; a polynomial algorithm there would remove the main empirical obstruction.
- **Bounded-degree in polynomial time.** Grohe–Neuen–Schweitzer's $n^{O((\log d)^c)}$ suggests $n^{O(1)}$ for all $d$ may be within reach; this would be the first unbounded-parameter class conquered.
- **Descriptive complexity.** Find a logic capturing $\mathsf{PTIME}$ on graph classes strictly beyond minor-closed, or prove a sharp non-capture theorem.
- **Structural complexity.** Determine whether $\mathsf{GI}$ has a Ladner-style intermediate status, or is complete for some natural class (candidate: $\mathsf{GI}$-completeness of ring/group isomorphism variants).

## 9. Key References

- **[Foundational]** L. Babai. *Graph Isomorphism in Quasipolynomial Time.* Proc. 48th ACM Symposium on Theory of Computing (STOC), pp. 684–697, 2016. arXiv:1512.03547.
- **[Foundational]** E. M. Luks. *Isomorphism of Graphs of Bounded Valence Can Be Tested in Polynomial Time.* Journal of Computer and System Sciences 25(1):42–65, 1982.
- **[Foundational]** J.-Y. Cai, M. Fürer, N. Immerman. *An Optimal Lower Bound on the Number of Variables for Graph Identification.* Combinatorica 12(4):389–410, 1992.
- **[Foundational]** L. Babai, E. M. Luks. *Canonical Labeling of Graphs.* Proc. 15th ACM Symposium on Theory of Computing (STOC), pp. 171–183, 1983.
- **[Foundational]** R. Boppana, J. Håstad, S. Zachos. *Does co-NP Have Short Interactive Proofs?* Information Processing Letters 25(2):127–132, 1987.
- **[Foundational]** U. Schöning. *Graph Isomorphism is in the Low Hierarchy.* Journal of Computer and System Sciences 37(3):312–323, 1988.
- **[Foundational]** L. Babai, P. Erdős, S. M. Selkow. *Random Graph Isomorphism.* SIAM Journal on Computing 9(3):628–635, 1980.
- **[SOTA / Recent]** M. Grohe, D. Neuen, P. Schweitzer. *A Faster Isomorphism Test for Graphs of Small Degree.* SIAM Journal on Computing 52(6), 2023 (conference version FOCS 2018).
- **[SOTA / Recent]** D. Neuen. *Isomorphism Testing for Graphs Excluding Small Topological Subgraphs.* Proc. ACM–SIAM Symposium on Discrete Algorithms (SODA), 2022.
- **[SOTA / Recent]** D. Lokshtanov, M. Pilipczuk, M. Pilipczuk, S. Saurabh. *Fixed-Parameter Tractable Canonization and Isomorphism Test for Graphs of Bounded Treewidth.* SIAM Journal on Computing 46(1):161–189, 2017.
- **[SOTA / Recent]** S. Kiefer, I. Ponomarenko, P. Schweitzer. *The Weisfeiler–Leman Dimension of Planar Graphs Is at Most 3.* Journal of the ACM 66(6), 2019.
- **[Survey]** M. Grohe, D. Neuen. *Recent Advances on the Graph Isomorphism Problem.* In *Surveys in Combinatorics 2021*, London Mathematical Society Lecture Note Series 470, Cambridge University Press, 2021.
- **[Survey]** H. A. Helfgott. *Isomorphismes de graphes en temps quasi-polynomial (d'après Babai et Luks, Weisfeiler–Leman…).* Séminaire Bourbaki, Exp. 1125, Astérisque 407, 2019.
- **[Survey]** M. Grohe. *Descriptive Complexity, Canonisation, and Definable Graph Structure Theory.* Lecture Notes in Logic 47, Cambridge University Press, 2017.
- **[Practice]** B. D. McKay, A. Piperno. *Practical Graph Isomorphism, II.* Journal of Symbolic Computation 60:94–112, 2014.

## 10. Worked Example / Concrete Special Case

**Color refinement fails on regular graphs.** Let $G = C_6$ (6-cycle) and $H = C_3 \sqcup C_3$ (two triangles). Both have $n=6$, $m=6$, and every vertex has degree 2.

*1-WL trace.* Initially $\chi^0 \equiv 1$ on both. Then
$$\chi^1(v) = (1, \{\!\{1,1\}\!\}) \quad \text{for every } v \in V(G) \cup V(H).$$
The partition is already stable — one class of size 6 in each graph — so the stable color multisets are identical: $\{\!\{c\}\!\}^6$. **1-WL cannot distinguish $G$ from $H$**, yet $G \not\cong H$ ($G$ is connected, $H$ is not).

*2-WL succeeds.* 2-WL colors ordered pairs. Count, for each pair $(u,v)$ with $u \sim v$, the number of common neighbours $|N(u)\cap N(v)|$, which 2-WL records:

- In $H$: every edge $(u,v)$ lies in a triangle, so $|N(u)\cap N(v)| = 1$.
- In $G = C_6$: no triangles, so $|N(u)\cap N(v)| = 0$ for every edge.

The multiset of pair-colors after one 2-WL round therefore differs: $H$ produces 6 ordered "edge" pairs with common-neighbour count 1, $G$ produces 6 with count 0. Hence 2-WL separates them; the WL-dimension of $C_6$ against this family is 2.

*Why this does not solve the problem.* The Cai–Fürer–Immerman construction iterates exactly this trick against every fixed $k$. From a connected 3-regular base graph $B$ with $\Theta(k)$ vertices and treewidth $\ge k$, replace each vertex by a gadget encoding the parity-check space $\{x \in \mathbb{F}_2^3 : x_1+x_2+x_3 = 0\}$, and build $X(B)$ and its *twisted* copy $\tilde X(B)$ by flipping the parity on one edge. Then

$$X(B) \not\cong \tilde X(B), \qquad \text{yet } k\text{-WL}\big(X(B)\big) = k\text{-WL}\big(\tilde X(B)\big),$$

with $|V(X(B))| = O(k)$. So the refinement dimension needed grows linearly in $n$, and the $n^{O(k)}$ running time of $k$-WL becomes $n^{\Omega(n)}$ — worse than brute force. This single family is the reason $\mathsf{GI}$ needs the group-theoretic machinery of Section 2, and why the honest upper bound remains $\exp\big(O((\log n)^3)\big)$ rather than $n^{O(1)}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*