---
id: 10-theoretical-cs/branching-program-size-lower-bounds
title: "Barrington-Style Bounded-Width Branching Programs for NC1"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Barrington-Style Bounded-Width Branching Programs for NC1

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/branching-program-size-lower-bounds` · **Status:** open

## 1. Problem Statement / Conjecture

Barrington's theorem (1986/1989) collapsed a widely believed separation: width-$5$ polynomial-length branching programs recognize **exactly** $\mathsf{NC}^1$. This turned every $\mathsf{NC}^1$ lower bound question into a question about *lengths of bounded-width programs*, and every $\mathsf{L}$ vs. $\mathsf{NC}^1$ question into a question about *sizes of unbounded-width programs*. Both remain open. The catalog entry tracks the cluster of open statements:

- **(A) Superpolynomial size.** Exhibit an explicit family $f_n \in \mathsf{P}$ (or even $\mathsf{NP}$) with branching program size $\mathrm{BP}(f_n) = n^{\omega(1)}$. This would give $\mathsf{P} \not\subseteq \mathsf{L}/\mathrm{poly}$. Best known bound for any explicit $f$: $\Theta(n^2/\log^2 n)$, Nechiporuk (1966).
- **(B) Superpolynomial length at bounded width.** Show some $f_n \in \mathsf{P}$ has no polynomial-length width-$5$ program, i.e. $f_n \notin \mathsf{NC}^1$. Best known length lower bound for width $O(1)$: $n \cdot \omega(1)$, barely superlinear.
- **(C) The width-$3$ question.** Do polynomial-length width-$3$ branching programs compute $\mathrm{MAJ}_n$? Equivalently (in the permutation case) does the solvable group $S_3$ suffice where $S_5$ does?

A complete resolution of (A) or (B) means an explicit function, a proof of the lower bound, and — since these are non-relativizing, non-naturalizable targets — a technique surviving the known barriers (Section 5).

## 2. Mathematical Foundations

**Branching program.** A *branching program* (BP) over variables $x_1,\dots,x_n$ is a directed acyclic graph with one source, sinks labeled $\{0,1\}$, and every internal node labeled by some $x_i$ with two outgoing edges labeled $0$ and $1$. On input $a \in \{0,1\}^n$ the computation follows the edge labeled $a_i$ out of each $x_i$-node; $f(a)$ is the reached sink label. Size $\mathrm{BP}(f)$ = number of nodes.

**Layered / bounded width.** A BP is *layered* of width $w$ and length $\ell$ if nodes are partitioned into layers $V_0,\dots,V_\ell$ with $|V_t| \le w$ and edges only from $V_{t-1}$ to $V_t$. Then $\mathrm{BP}(f) \le w(\ell+1)$ and the machine model is a nonuniform read-many space-$\log w$ device.

**Permutation program over a group $G$.** A length-$\ell$ program is a list of instructions $\langle i_t, g_t^0, g_t^1 \rangle_{t=1}^{\ell}$ with $i_t \in [n]$, $g_t^b \in G$. Its yield is
$$ P(a) \;=\; \prod_{t=1}^{\ell} g_t^{a_{i_t}} \in G .$$
$P$ *$\sigma$-computes* $f$ if $P(a) = \sigma \neq e$ when $f(a)=1$ and $P(a)=e$ when $f(a)=0$.

**Key algebraic fact.** In $S_5$ every $5$-cycle is a commutator of two $5$-cycles: for $5$-cycles $\sigma,\tau$ chosen suitably,
$$ [\sigma,\tau] = \sigma\tau\sigma^{-1}\tau^{-1} \text{ is again a } 5\text{-cycle},$$
because $A_5$ is simple, hence perfect ($[A_5,A_5]=A_5$). This is exactly what solvable groups lack: if $G$ is solvable, iterated commutators die.

**Theorem (Barrington 1989).** For every $f \in \mathsf{NC}^1$ of formula depth $d$ there is a width-$5$ permutation program of length $\le 4^{d}$ that $\sigma$-computes $f$ for any $5$-cycle $\sigma$; conversely every polynomial-length width-$5$ program is in $\mathsf{NC}^1$. Hence
$$ \mathsf{BWBP} \;=\; \mathsf{NC}^1 .$$

**Theorem (Barrington–Thérien 1988).** Programs of polynomial length over a fixed finite monoid $M$ recognize $\mathsf{NC}^1$ iff $M$ contains a nonsolvable group; over solvable groups they recognize exactly $\mathsf{ACC}^0$ languages of the corresponding moduli.

**Nechiporuk's measure.** For disjoint blocks $Y_1,\dots,Y_k$ of variables let $s_j(f)$ be the number of distinct subfunctions of $f$ obtained by fixing all variables outside $Y_j$. Then
$$ \mathrm{BP}(f) \;=\; \Omega\!\left(\sum_{j=1}^{k} \frac{\log s_j(f)}{\log \log s_j(f)}\right).$$

**Containments.** $\mathsf{NC}^1 \subseteq \mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{SAC}^1 \subseteq \mathsf{NC}^2$, with the nonuniform forms $\mathsf{NC}^1 \subseteq \mathsf{L}/\mathrm{poly} = $ poly-size BPs. No separation in this chain is known.

## 3. History & State of the Art (SOTA)

- **1966.** Nechiporuk introduces the subfunction-counting method, obtaining $\Omega(n^2/\log^2 n)$ for branching programs (and $\Omega(n^2/\log n)$ for formulas) on the element-distinctness-type function. Still the record for general BPs, 60 years later.
- **1979–1984.** Masek formalizes branching programs as a nonuniform space model; Pudlák and Žák prove exponential bounds for *read-once* programs.
- **1986/1989.** Barrington proves $\mathsf{BWBP} = \mathsf{NC}^1$ (STOC 1986; JCSS 38, 150–164, 1989), refuting the folklore conjecture that bounded width forces near-regular languages.
- **1988–1990.** Barrington–Thérien (JACM) and Barrington–Straubing–Thérien complete the algebraic classification: nonsolvable $\Rightarrow \mathsf{NC}^1$, solvable $\Rightarrow \mathsf{ACC}^0$.
- **1989.** Cai–Lipton give subquadratic simulations of circuits by branching programs, showing Nechiporuk-type bounds cannot be pushed past $n^2$ by the same route.
- **1993.** Borodin–Razborov–Smolensky: $2^{\Omega(n/4^k)}$ for syntactic read-$k$-times programs.
- **1995.** Barrington–Straubing prove superlinear ($\Omega(n\log n)$-type) length bounds for bounded-width programs in restricted regimes; Chandra–Furst–Lipton's multiparty communication method already gave $n\cdot\omega(1)$ for width $O(1)$.
- **1999–2003.** Ajtai's nonlinear time bound for general (oblivious-free) BPs, extended by Beame–Saks–Sun–Vee (JACM 2003) to $T = \Omega\!\big(n\sqrt{\log(n/S)/\log\log(n/S)}\big)$ time–space tradeoffs for element distinctness and quadratic forms.
- **2010s.** Derandomization side advances fast: Nisan's generator, Braverman–Rao–Raz–Yehudayoff and Impagliazzo–Meka–Zuckerman for read-once and small-width programs.
- **2024–2025.** Cook–Mertz's catalytic-style tree-evaluation algorithm in space $O(\log n \cdot \log\log n)$, and Williams' $\mathsf{TIME}[t] \subseteq \mathsf{SPACE}[\sqrt{t\log t}]$, destroy the leading candidate program for separating $\mathsf{NC}^1$ from $\mathsf{L}$.

## 4. Partial Results / Verified Cases

- **General BPs, explicit function.** $\mathrm{BP}(\mathrm{ED}_n) = \Omega(n^2/\log^2 n)$ where $\mathrm{ED}$ is element distinctness on $n/\log n$ blocks of $\log n$ bits (Nechiporuk). Matching $O(n^2/\log^2 n)$ upper bounds exist for such functions, so the method is *saturated*.
- **Read-once (BP1).** Exponential: $2^{\Omega(n)}$ for explicit functions (Žák, Wegener, Ajtai et al.); clique-only functions give $2^{\Omega(\sqrt n)}$.
- **Read-$k$, syntactic.** $2^{\Omega(n/4^k)}$ (Borodin–Razborov–Smolensky 1993); useful only for $k = o(\log n)$.
- **Oblivious, linear length.** Explicit $2^{\Omega(n)}$ bounds for oblivious BPs of length $kn$ with $k$ constant (Alon–Maass; Babai–Nisan–Szegedy via multiparty communication).
- **Width $\le 4$.** Barrington's theorem is tight in the sense that width $5$ suffices; width $4$ also captures $\mathsf{NC}^1$ using non-permutation instructions over $S_4$-based monoids with the standard padding trick.
- **Solvable width.** Programs over $S_3$, $\mathbb{Z}_q$, or any solvable group of polynomial length compute exactly $\mathsf{ACC}^0$-type classes — a genuine *upper* bound restricting width-$3$ permutation programs.
- **Bounded width, superlinear length.** $\Omega(n \log n / \log\log n)$-type length bounds for width-$w$ programs computing $\mathrm{MAJ}_n$ via $\log$-party communication complexity; these degrade to nothing once width exceeds $2^{(\log n)^{\Omega(1)}}$.
- **Time–space.** Any BP for element distinctness with space $S = n^{o(1)}$ needs time $\Omega(n\sqrt{\log n/\log\log n})$ (BSSV 2003).

## 5. Principal Obstacles

- **Nechiporuk saturation.** The measure $\sum_j \log s_j/\log\log s_j$ is bounded by $O(n^2/\log^2 n)$ for *every* $f$, since $\sum_j |Y_j| = n$ and $\log s_j \le 2^{|Y_j|}$ optimizes at block size $\approx \log n$. No refinement of subfunction counting can exceed $n^2$; Cai–Lipton's simulations show why.
- **Read-many destroys combinatorial structure.** All exponential bounds (read-once, read-$k$, oblivious) rely on a *syntactic* budget on repetitions to fix a variable-partition and invoke communication complexity. A general BP re-reads adaptively; there is no partition to fix, and the rectangle/discrepancy machinery has nothing to bite on.
- **Multiparty barrier.** Bounded-width length bounds route through $k$-party number-on-forehead complexity with $k \approx \log n$ players. Best known NOF lower bounds are $n/2^{\Theta(\sqrt{\log n})}$-scale and provably cannot yield superpolynomial BP length; pushing past $k = \log n$ players is itself a famous open problem.
- **Algebraic degeneracy at width 5.** Barrington's construction shows $\mathsf{NC}^1$-hardness is a statement about *nonsolvability*, not about width. Any technique that only exploits the finite state set (small width) must fail, since $5$ states already suffice for all of $\mathsf{NC}^1$.
- **Natural proofs and relativization.** Poly-size BPs contain $\mathsf{NC}^1 \supseteq$ pseudorandom function candidates under standard assumptions, so a largeness-and-constructivity proof strategy runs into Razborov–Rudich. Algebrization (Aaronson–Wigderson) blocks the diagonalization routes.
- **Collapse of the candidate hard function.** Tree Evaluation $\mathrm{FT}_h^d$ was proposed by Cook–McKenzie–Wehr–Braverman–Santhanam as a function in $\mathsf{P}$ plausibly outside $\mathsf{L}$. Cook–Mertz (2024) put it in space $O(\log n \log\log n)$, removing the best-motivated target.

## 6. The Gap

Proven: $\Theta(n^2/\log^2 n)$ for general BPs, exponential bounds under syntactic read restrictions, and $n\cdot\omega(1)$ at constant width. Wanted: $n^{\omega(1)}$ with **no** restriction on reads. The precise missing step is a complexity measure that is (i) subadditive along BP layers or nodes, (ii) not bounded by $O(n^2)$ for all functions, and (iii) large on an explicit $f$. Every known measure fails at least one of (i)–(iii): rank/discrepancy measures need a fixed partition (fails (i) without read restrictions), subfunction counting fails (ii), and approximate-degree or polynomial-method measures fail (iii) because BPs of polynomial size compute functions of full degree.

For the bounded-width statement (B) the gap is sharper: one needs a length lower bound of $n^{1+\Omega(1)}$ at width $5$ that does not pass through $\log n$-party communication. Even $n^{1.01}$ at width $5$ would be a breakthrough.

## 7. Current Research (as of June 2026)

- **Catalytic and space-efficient algorithms.** Cook–Mertz's technique (Toronto/Charles University lineage — Buhrman, Koucký, Loff, Speelman) is being pushed to other candidate hard problems; the emerging view is that $\mathsf{P}$ vs. $\mathsf{L}$ candidates are far scarcer than believed. Williams' $\sqrt{t\log t}$-space simulation (2025) suggests further *upper* bound surprises before lower bounds. *(frontier — verify)*
- **Lifting theorems.** Göös–Pitassi–Watson-style query-to-communication lifting is being adapted to semantic read-once and small-width models (Chattopadhyay, Koucký, Loff, Mukhopadhyay). Extension to unrestricted BPs remains blocked by the partition problem.
- **Algebraic/monoid programs.** Continued work on programs over solvable monoids, aiming at $\mathrm{MAJ} \notin \mathsf{ACC}^0$ — equivalent, via Barrington–Thérien, to width-$3$ permutation programs failing for majority.
- **Meta-complexity and satisfiability algorithms.** The Williams paradigm (nontrivial SAT algorithm $\Rightarrow$ lower bound) has been instantiated for branching-program-SAT; current algorithms handle size $n^{2-o(1)}$ or width-$o(\log n)$, short of the threshold that would give $\mathsf{ENP} \not\subseteq \mathsf{L}/\mathrm{poly}$. *(frontier — verify)*
- **Pseudorandomness for ROBPs.** Ongoing improvements to seed length for width-$w$ read-once programs (Meka, Chattopadhyay, Hoza, Pyne, Vadhan) — the derandomization side keeps outpacing the lower-bound side.

## 8. Future Work

- Find a hard-function candidate to replace Tree Evaluation, robust to catalytic space tricks; iterated group products in $A_5$ and word problems over nonsolvable groups are the natural remaining candidates.
- Develop a *semantic* read-once framework strong enough to handle non-syntactic repetitions, then bootstrap to read-$O(\log n)$; Cook–Edmonds–Medabalimi–Pitassi identified this as the concrete next rung.
- Break the $\log n$-player barrier in number-on-forehead complexity, which would immediately yield superpolynomial length bounds at constant width.
- Prove $\mathrm{MAJ}_n \notin \mathsf{ACC}^0$, settling the width-$3$ question through the Barrington–Thérien classification.
- Design a BP-SAT algorithm running in $2^{n}/n^{\omega(1)}$ for size-$n^{2}$ programs, closing the meta-algorithmic route.

## 9. Key References

- **[Foundational]** D. A. Barrington. *Bounded-Width Polynomial-Size Branching Programs Recognize Exactly Those Languages in $\mathrm{NC}^1$.* Journal of Computer and System Sciences 38(1):150–164, 1989 (STOC 1986).
- **[Foundational]** È. I. Nechiporuk. *On a Boolean Function.* Soviet Mathematics Doklady 7:999–1000, 1966.
- **[Foundational]** D. A. Barrington, D. Thérien. *Finite Monoids and the Fine Structure of $\mathrm{NC}^1$.* Journal of the ACM 35(4):941–952, 1988.
- **[Foundational]** A. Borodin, A. A. Razborov, R. Smolensky. *On Lower Bounds for Read-$k$-Times Branching Programs.* Computational Complexity 3:1–18, 1993.
- **[SOTA]** P. Beame, M. Saks, X. Sun, E. Vee. *Time-Space Trade-off Lower Bounds for Randomized Computation of Decision Problems.* Journal of the ACM 50(2):154–195, 2003.
- **[SOTA]** M. Ajtai. *A Non-linear Time Lower Bound for Boolean Branching Programs.* FOCS 1999, 60–70.
- **[SOTA]** D. A. Barrington, H. Straubing. *Superlinear Lower Bounds for Bounded-Width Branching Programs.* Journal of Computer and System Sciences 50(3):374–381, 1995.
- **[SOTA / Recent]** J. Cook, I. Mertz. *Tree Evaluation Is in Space $O(\log n \cdot \log\log n)$.* STOC 2024.
- **[SOTA / Recent]** R. R. Williams. *Simulating Time with Square-Root Space.* STOC 2025.
- **[Recent]** S. Cook, J. Edmonds, V. Medabalimi, T. Pitassi. *Lower Bounds for Nondeterministic Semantic Read-Once Branching Programs.* ICALP 2016.
- **[Survey]** I. Wegener. *Branching Programs and Binary Decision Diagrams: Theory and Applications.* SIAM Monographs on Discrete Mathematics and Applications, 2000.
- **[Survey]** S. Jukna. *Boolean Function Complexity: Advances and Frontiers.* Springer, 2012 (Chapters 14–16).
- **[Survey]** A. A. Razborov. *Lower Bounds for Deterministic and Nondeterministic Branching Programs.* Fundamentals of Computation Theory (FCT), LNCS 529, 47–60, 1991.
- **[Context]** J.-Y. Cai, R. J. Lipton. *Subquadratic Simulations of Circuits by Branching Programs.* FOCS 1989, 568–573.
- **[Context]** A. K. Chandra, M. L. Furst, R. J. Lipton. *Multi-party Protocols.* STOC 1983, 94–99.

## 10. Worked Example / Concrete Special Case

**Barrington's AND gadget in $S_5$, computed explicitly.**

Take $\sigma = (1\,2\,3\,4\,5)$ and $\tau = (1\,3\,5\,4\,2)$, both $5$-cycles. Compute the commutator $\gamma = \sigma\tau\sigma^{-1}\tau^{-1}$ (rightmost permutation applied first):

| $x$ | $\tau^{-1}$ | $\sigma^{-1}$ | $\tau$ | $\sigma$ | $\gamma(x)$ |
|---|---|---|---|---|---|
| 1 | 2 | 1 | 3 | 4 | 4 |
| 2 | 4 | 3 | 5 | 1 | 1 |
| 3 | 1 | 5 | 4 | 5 | 5 |
| 4 | 5 | 4 | 2 | 3 | 3 |
| 5 | 3 | 2 | 1 | 2 | 2 |

So $\gamma = (1\,4\,3\,5\,2)$ — again a $5$-cycle, and in particular $\gamma \neq e$.

**Why this proves the theorem's inductive step.** Suppose $P_1$ $\sigma$-computes $g$ with length $\ell_1$ and $P_2$ $\tau$-computes $h$ with length $\ell_2$. Form
$$ P \;=\; P_1 \cdot P_2 \cdot P_1^{-1} \cdot P_2^{-1},$$
where $P_1^{-1}$ is $P_1$ with instructions reversed and inverted (so it $\sigma^{-1}$-computes $g$). Then:

- $g=h=1$: yield $= \sigma\tau\sigma^{-1}\tau^{-1} = \gamma \ne e$.
- $g=1, h=0$: yield $= \sigma \cdot e \cdot \sigma^{-1} \cdot e = e$.
- $g=0, h=1$: yield $= e \cdot \tau \cdot e \cdot \tau^{-1} = e$.
- $g=h=0$: yield $= e$.

Hence $P$ $\gamma$-computes $g \wedge h$ with length $\ell = 2(\ell_1+\ell_2)$. Negation is free (relabel the output cycle: $P' = P \cdot \gamma^{-1}$ swaps the roles of $e$ and $\gamma$), and conjugation by any $\pi \in S_5$ converts a $\gamma$-computing program into a $\pi\gamma\pi^{-1}$-computing one at no length cost, since all $5$-cycles are conjugate.

**Length accounting.** A single variable $x_i$ is $\sigma$-computed by the length-$1$ program $\langle i, e, \sigma\rangle$. Unfolding the recursion $L(d) = 4L(d-1)$, a depth-$d$ formula yields length $L(d) \le 4^{d}$. For $\mathsf{NC}^1$ with $d = c\log_2 n$ this gives length $n^{2c}$ — polynomial, with width exactly $5$.

**The contrast that makes the problem open.** The construction shows $\mathrm{MAJ}_n$ (depth $O(\log n)$ by AKS sorting networks) has a width-$5$ program of polynomial length. Meanwhile the best *lower* bound we can prove against width-$5$ programs of any explicit function is barely $n\log n$-scale, and against unrestricted-width programs it is $n^2/\log^2 n$ — a gap of $n^{O(1)}$ versus $2^{\Theta(n)}$ (the counting bound, which shows almost all functions need size $\Omega(2^n/n)$). Every hard function we can name sits inside the tiny proven window; the counting argument guarantees the hard ones exist but names none.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*