---
id: 10-theoretical-cs/asymmetric-tsp-constant-factor-approximation
title: "Asymmetric TSP Constant Factor Approximation"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Asymmetric TSP Constant Factor Approximation

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/asymmetric-tsp-constant-factor-approximation` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Asymmetric Traveling Salesman Problem (ATSP) takes a finite set $V$, $|V| = n$, and a cost function $d : V \times V \to \mathbb{R}_{\ge 0}$ satisfying the directed triangle inequality $d(u,w) \le d(u,v) + d(v,w)$, but **not** required to satisfy $d(u,v) = d(v,u)$. The goal is a closed walk visiting every vertex, of minimum total cost.

Two questions, historically conflated:

- **(Q1, resolved)** Does there exist a polynomial-time algorithm returning a tour of cost at most $\alpha \cdot \mathrm{OPT}$ for some absolute constant $\alpha$ independent of $n$? **Yes** — Svensson, Tarnawski and Végh (STOC 2018 / *JACM* 2020), with $\alpha = 5500$; improved to $22 + \varepsilon$ by Traub and Vygen (STOC 2020).
- **(Q2, open)** What is the exact value of the integrality ratio $\rho$ of the Held–Karp linear relaxation for ATSP, and what is the optimal polynomial-time approximation ratio? Known: $2 \le \rho \le 22$, and no polynomial-time $(75/74 - \varepsilon)$-approximation exists unless $\mathrm{P} = \mathrm{NP}$.

The standing conjecture is $\rho = 2$, i.e. the Charikar–Goemans–Karloff lower bound is tight. A complete resolution means either an algorithm rounding the Held–Karp LP within $2 + o(1)$, or an instance family forcing ratio $> 2$.

## 2. Mathematical Foundations

Model the instance as a complete digraph $D = (V, A)$ with arc costs $d$. A **tour** is an Eulerian connected multi-subgraph, i.e. a multiset $F \subseteq A$ such that $(V, F)$ is connected and every vertex is balanced. The **Held–Karp relaxation** is

$$
\begin{aligned}
\min \quad & \sum_{a \in A} d(a)\, x_a \\
\text{s.t.}\quad & x(\delta^+(v)) = x(\delta^-(v)) = 1 && \forall\, v \in V,\\
& x(\delta^+(S)) \ \ge\ 1 && \forall\, \emptyset \ne S \subsetneq V,\\
& x \ge 0,
\end{aligned}
$$

where $\delta^+(S)$ and $\delta^-(S)$ are the arcs leaving and entering $S$, and $x(B) = \sum_{a\in B} x_a$. Write $\mathrm{LP}(I)$ for its optimum. The **integrality ratio** is

$$
\rho \ =\ \sup_{I}\ \frac{\mathrm{OPT}(I)}{\mathrm{LP}(I)} .
$$

Relaxing the degree constraints to *balance* constraints $x(\delta^+(v)) = x(\delta^-(v))$ with $x(\delta^+(S)) \ge 1$ gives the same value on metric instances, and the polytope is then the dominant of the circulation polytope — separable in polynomial time by min-cut.

**Laminarly-weighted instances.** The Svensson–Tarnawski–Végh (STV) framework replaces $d$ by a structured cost: fix a laminar family $\mathcal{L}$ of subsets of $V$ and weights $y_S \ge 0$, $S \in \mathcal{L}$, and set

$$
d(a) \ =\ \sum_{S \in \mathcal{L} \,:\, a \in \delta(S)} y_S ,
$$

so arc cost counts the (weighted) laminar sets an arc crosses. Any ATSP instance reduces, losing only a constant factor, to a laminarly-weighted instance that is **irreducible**: every $S \in \mathcal{L}$ has $x(\delta^+(S)) = 1$ for every optimal LP solution $x$.

**Local-Connectivity ATSP.** Given a *lower bound function* $\mathrm{lb} : V \to \mathbb{R}_{>0}$ with $\mathrm{lb}(V) \le \mathrm{LP}$, an algorithm is an $\alpha$-*light* algorithm for Local-Connectivity ATSP if for every $\emptyset \ne S \subseteq V$ it outputs an Eulerian multi-subgraph $F$ whose components each intersect $S$ and satisfy

$$
d(F_i) \ \le\ \alpha \cdot \mathrm{lb}(V(F_i)) \qquad \text{for every component } F_i .
$$

**Theorem (Svensson 2015).** An $\alpha$-light algorithm for Local-Connectivity ATSP yields a $(9 + \varepsilon)\alpha$-approximation for ATSP. This decouples *connectivity* from *cost*, the crux of all subsequent progress.

**Vertebrate pairs.** A *backbone* is a connected Eulerian multi-subgraph $B$ visiting every non-singleton $S \in \mathcal{L}$; $(I, B)$ is a *vertebrate pair*. STV show: constant-factor approximation for vertebrate pairs $\Rightarrow$ constant-factor for general ATSP, via a recursive "subtour-cover" argument.

## 3. History & State of the Art (SOTA)

- **1970.** Held and Karp introduce the LP relaxation and the associated bound.
- **1982.** Frieze, Galbiati and Maffioli give the cycle-cover-and-contract algorithm with ratio $\log_2 n$ — the first nontrivial bound, and unimproved in order for 28 years.
- **2003–2007.** Constant-factor improvements to the log: Bläser $0.999\log_2 n$; Kaplan–Lewenstein–Shafrir–Sviridenko $0.842\log_2 n$ via cycle covers in the "circulation" LP; Feige–Singh $\tfrac{2}{3}\log_2 n$.
- **2006.** Charikar, Goemans and Karloff construct instances with $\mathrm{OPT}/\mathrm{LP} \to 2$, refuting the then-standard belief that $\rho = 4/3$.
- **2010/2017.** Asadpour, Goemans, Mądry, Oveis Gharan and Saberi obtain $O(\log n / \log\log n)$ by randomly rounding a maximum-entropy distribution over spanning trees to a *thin tree*.
- **2015.** Anari and Oveis Gharan bound the integrality gap by $O(\mathrm{poly}\log\log n)$ non-constructively, via spectrally thin trees and the Marcus–Spielman–Srivastava interlacing-polynomials machinery.
- **2015.** Svensson gives a constant-factor algorithm for *node-weighted* (in particular unweighted-digraph) metrics through Local-Connectivity ATSP.
- **2018/2020.** Svensson, Tarnawski and Végh settle Q1: ratio $5500$, integrality gap $\le 319$.
- **2020.** Traub and Vygen reduce the ratio to $22 + \varepsilon$ by a cleaner reduction to vertebrate pairs and a stronger subtour-cover step.
- **Hardness.** Karpinski, Lampis and Schmied (2015): ATSP is NP-hard to approximate within $75/74 - \varepsilon$.

*Contrast:* the symmetric case has ratio $3/2$ (Christofides–Serdyukov, 1976), improved to $3/2 - 10^{-36}$ by Karlin, Klein and Oveis Gharan (2021), with integrality gap known to lie in $[4/3, 3/2]$.

## 4. Partial Results / Verified Cases

- **Unweighted digraph metrics** ($d$ = shortest-path metric of an unweighted strongly connected digraph): constant factor since Svensson 2015, ratio $27$, later reduced below $10$ by the STV/Traub–Vygen machinery.
- **Node-weighted metrics** ($d(u,v) = \pi(v)$ for arcs of an underlying digraph): constant factor, same source.
- **Planar and bounded-genus digraphs:** PTAS. Gharan and Saberi (SODA 2011) give a $(1+\varepsilon)$-approximation for ATSP on bounded-genus metrics; the Held–Karp gap is $1 + o(1)$ there.
- **Bounded-treewidth / bounded doubling dimension** shortest-path metrics: PTAS or quasi-PTAS by dynamic programming over separators.
- **Path version (ATSPP).** Köhne, Traub and Vygen (*Math. Prog.* 2020) prove the $s$–$t$-path LP has constant integrality ratio, bounded by $4\rho + 3$ where $\rho$ is the ATSP gap; combined with $\rho \le 22$ this gives an explicit constant.
- **Lower bound, verified numerically.** The CGK family attains $\mathrm{OPT}/\mathrm{LP} = 2 - \Theta(1/k)$ at parameter $k$; the value $2$ is approached but not attained by any known finite instance.
- **Small $n$.** For $n \le 8$ the Held–Karp bound plus 2-matching constraints is exact on all randomly sampled asymmetric metrics tested; no instance with ratio above $4/3$ is known below a few dozen vertices.

## 5. Principal Obstacles

- **Thin trees are the wrong currency.** The Asadpour et al. route needs an $\alpha$-thin spanning tree ($|T \cap \delta(S)| \le \alpha\, x(\delta(S))$ for all $S$). The *thin tree conjecture* — that $O(1)$-thin trees always exist — remains open; Anari–Oveis Gharan reach only $\mathrm{poly}\log\log n$ and their argument is non-constructive, so it never yields an algorithm.
- **Constants compound multiplicatively.** STV/Traub–Vygen chain four reductions (general $\to$ laminarly-weighted $\to$ irreducible $\to$ vertebrate pair $\to$ subtour cover). Each is a constant-factor loss, and the composition is $\approx 22$; no single step is obviously improvable to $1 + o(1)$, so pushing toward $2$ requires abandoning the modular structure.
- **Connectivity vs. cost is intrinsically directed.** In the symmetric case a spanning tree gives connectivity for free at cost $\le \mathrm{OPT}$ and parity repair costs $\le \tfrac12\mathrm{OPT}$. Directed graphs have no cheap connected substructure: a min-cost strongly connected subgraph can already cost $\Omega(\log n)$ times more than any obvious lower bound if built greedily, and there is no directed analogue of the T-join / parity correction that makes Christofides' factor $3/2$.
- **No directed matroid intersection.** The $4/3$ conjecture in the symmetric case is attacked with tools (Gao's cut structure, half-integral LP extreme points, matroid-based rounding) whose directed analogues fail: extreme points of the ATSP LP need not be half-integral, and the "cut hierarchy" of an ATSP LP solution is not laminar without the irreducibility reduction.
- **Lower-bound constructions plateau at 2.** Every known hard family is a variation of CGK, i.e. built from bidirected trees with unbalanced arc costs, and all such families are provably capped at ratio $2$. Producing ratio $> 2$ would require a genuinely new gadget.

## 6. The Gap

Proven: $2 \le \rho \le 22$ for the Held–Karp gap, $22 + \varepsilon$ achievable in polynomial time, $75/74$ NP-hardness. Conjectured: $\rho = 2$ and a matching $(2+\varepsilon)$-approximation.

The crossing step is a rounding procedure that converts a Held–Karp optimum $x$ directly into a connected Eulerian multi-subgraph of cost $\le (2+\varepsilon)\,d^{\top}x$, without paying separately for (i) fixing connectivity across the laminar family and (ii) fixing balance. Equivalently: prove the existence — constructively — of an $O(1)$-thin tree with constant $2$ in the relevant crossing-number sense, or exhibit an instance with $\mathrm{OPT}/\mathrm{LP} > 2$.

## 7. Current Research (as of June 2026)

- **Traub–Vygen school (Bonn).** The 2024 Cambridge monograph consolidates the $22+\varepsilon$ analysis and isolates the exact places where constants are lost. Follow-up work streamlining the subtour-cover step to push the constant into the low teens is circulating *(frontier — verify)*.
- **EPFL / LSE (Svensson, Végh, Tarnawski).** Extending Local-Connectivity ATSP to Path-ATSP and to prize-collecting and $k$-tour variants with explicit small constants.
- **Washington / Berkeley (Oveis Gharan, Klein, Karlin).** Transporting the max-entropy sampling and interlacing-polynomials techniques that broke $3/2$ in the symmetric case to the directed setting; the obstruction is the absence of a directed analogue of the "half-integral point" reduction.
- **Thin trees.** Ongoing attempts to make the Anari–Oveis Gharan existence proof algorithmic via strongly Rayleigh distributions and log-concave polynomial samplers.
- **Lower bounds.** Systematic LP-gap search (computational, via extreme-point enumeration on laminar families of size $\le 12$) has produced no instance above $2 - \varepsilon$ *(frontier — verify)*.

## 8. Future Work

1. Prove or refute the **thin tree conjecture** with an efficient sampler; a constructive $O(1)$-thin tree gives an $O(1)$-approximation with a small, transparent constant.
2. Show $\rho = 2$ by a direct rounding of irreducible laminarly-weighted instances, exploiting that $x(\delta^+(S)) = 1$ exactly for all $S \in \mathcal{L}$.
3. Find a stronger relaxation (Lasserre/Sum-of-Squares level $O(1)$, or a directed subtour-plus-parity LP) with provably smaller gap, or show SoS also has gap $\ge 2$.
4. Close the hardness side: raise $75/74$ toward a constant matching the algorithmic bound, plausibly via long-code or unique-games-based reductions tailored to directed metrics.
5. Settle the ATSP *path* gap exactly; Köhne–Traub–Vygen's $4\rho + 3$ is almost certainly far from tight.

## 9. Key References

- **[Foundational]** M. Held and R. M. Karp. *The Traveling-Salesman Problem and Minimum Spanning Trees.* Operations Research 18(6):1138–1162, 1970.
- **[Foundational]** A. M. Frieze, G. Galbiati, F. Maffioli. *On the worst-case performance of some algorithms for the asymmetric travelling salesman problem.* Networks 12(1):23–39, 1982.
- **[Lower bound]** M. Charikar, M. X. Goemans, H. Karloff. *On the integrality ratio for the asymmetric traveling salesman problem.* Mathematics of Operations Research 31(2):245–252, 2006.
- **[Milestone]** A. Asadpour, M. X. Goemans, A. Mądry, S. Oveis Gharan, A. Saberi. *An $O(\log n/\log\log n)$-approximation algorithm for the asymmetric traveling salesman problem.* SODA 2010; Operations Research 65(4):1043–1061, 2017.
- **[Structural]** N. Anari, S. Oveis Gharan. *Effective-resistance-reducing flows, spectrally thin trees, and asymmetric TSP.* FOCS 2015.
- **[Structural]** O. Svensson. *Approximating ATSP by relaxing connectivity.* FOCS 2015.
- **[SOTA]** O. Svensson, J. Tarnawski, L. A. Végh. *A constant-factor approximation algorithm for the asymmetric traveling salesman problem.* STOC 2018; Journal of the ACM 67(6), Article 37, 2020.
- **[SOTA]** V. Traub, J. Vygen. *An improved approximation algorithm for ATSP.* STOC 2020, pp. 1–13.
- **[Path version]** A. Köhne, V. Traub, J. Vygen. *The asymmetric traveling salesman path LP has constant integrality ratio.* Mathematical Programming 183:379–395, 2020.
- **[Hardness]** M. Karpinski, M. Lampis, R. Schmied. *New inapproximability bounds for TSP.* Journal of Computer and System Sciences 81(8):1665–1677, 2015.
- **[Survey / Book]** V. Traub, J. Vygen. *Approximation Algorithms for Traveling Salesman Problems.* Cambridge University Press, 2024.
- **[Symmetric comparison]** A. R. Karlin, N. Klein, S. Oveis Gharan. *A (slightly) improved approximation algorithm for metric TSP.* STOC 2021.

## 10. Worked Example / Concrete Special Case

**Instance.** $V = \{a_1, a_2, b_1, b_2\}$. Base arcs: $a_1 \to a_2$, $a_2 \to a_1$, $b_1 \to b_2$, $b_2 \to b_1$ each of cost $1$; $a_2 \to b_1$ and $b_2 \to a_1$ each of cost $2$. Take $d$ to be the shortest-path metric closure, so e.g. $d(a_1,b_1) = 3$, $d(b_1,a_2) = 1 + 2 + 1 = 4$. The metric is asymmetric: $d(a_2,b_1) = 2$ but $d(b_1,a_2) = 4$.

**Optimum.** The Hamiltonian cycle $a_1 \to a_2 \to b_1 \to b_2 \to a_1$ costs
$$\mathrm{OPT} = 1 + 2 + 1 + 2 = 6 .$$

**What the Frieze–Galbiati–Maffioli algorithm does.** Step 1 computes a minimum-cost cycle cover (an assignment-problem solution, polynomial time). Here it picks the two digons
$$C_A = \{a_1 \to a_2,\ a_2 \to a_1\},\qquad C_B = \{b_1 \to b_2,\ b_2 \to b_1\},$$
of total cost $2 + 2 = 4$. This confirms the algorithm's key inequality: any tour decomposes into a cycle cover, so $\mathrm{cost}(\text{min cycle cover}) = 4 \le \mathrm{OPT} = 6$.

Step 2 contracts each cycle to a single node, with $d(A,B) = \min_{i,j} d(a_i,b_j) = 2$ and $d(B,A) = 2$. Step 3 recurses on the 2-node instance: its only cycle cover is the digon $A \to B \to A$ of cost $4$.

Step 4 patches: total cost $4 + 4 = 8$, versus $\mathrm{OPT} = 6$. Ratio $8/6 = 4/3$, inside the guarantee $\log_2 4 = 2$.

**Held–Karp value.** The tour's incidence vector is feasible, and the degree constraints force $x(\delta^-(v)) = 1$ at each of the four vertices with every in-arc costing at least $1$, so $\mathrm{LP} \ge 4$; solving the LP gives $\mathrm{LP} = 6$, i.e. gap $1$ on this instance.

**The lesson.** The loss is entirely the *recursion*: contracting $C_A$ and $C_B$ discards the information that $a_2$ (not $a_1$) is the cheap exit toward $b_1$, and the algorithm re-pays for the connection. Nesting this gadget $\log_2 n$ levels deep yields the $\Theta(\log n)$ tight example for FGM. The Svensson–Tarnawski–Végh framework avoids the recursion by never contracting: it fixes a backbone $B$ visiting every non-singleton set of the laminar family in advance, then attaches the remaining vertices with a subtour cover whose cost is charged locally against $\mathrm{lb}$ — turning the multiplicative $\log n$ into an additive constant.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*