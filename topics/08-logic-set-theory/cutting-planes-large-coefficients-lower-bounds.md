---
id: 08-logic-set-theory/cutting-planes-large-coefficients-lower-bounds
title: "Proof Complexity Lower Bounds for Cutting Planes with Large Coefficients"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Proof Complexity Lower Bounds for Cutting Planes with Large Coefficients

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/cutting-planes-large-coefficients-lower-bounds` · **Status:** open

## 1. Problem Statement / Conjecture

Cutting Planes (CP) is a refutation system for unsatisfiable CNFs that reasons with integer linear inequalities over $\{0,1\}^n$. When the coefficients appearing in a proof are bounded by $\mathrm{poly}(n)$ the system is called CP$^*$; unrestricted CP allows coefficients of exponential (or larger) magnitude.

**Open problem.** Prove superpolynomial length lower bounds for unrestricted Cutting Planes on an explicit family of constant-width CNFs whose hardness does *not* reduce to a monotone circuit or monotone-real-circuit lower bound.

Concretely, the three benchmark statements are:

1. **(Constant width)** There is a constant $k$ and an explicit family $F_n$ of $k$-CNFs on $n$ variables such that every CP refutation of $F_n$ has length $2^{n^{\Omega(1)}}$. Every known CP lower bound needs either clause width $\Theta(\log n)$ or a lifted/interpolation structure.
2. **(Non-interpolation method)** Prove any superpolynomial CP lower bound by a technique that does not factor through communication complexity of a search problem. All current proofs go through real communication protocols.
3. **(Strength)** Prove $2^{\Omega(n)}$ lower bounds, and lower bounds for CP augmented with the natural extensions (Stabbing Planes, branch-and-cut with variable-disjunction branching), where essentially nothing is known.

A complete solution to (1) is an explicit family plus a proof; a disproof would be a polynomial-size CP refutation scheme for the candidate families (random CNFs, Tseitin-like formulas), which would itself be a major result.

## 2. Mathematical Foundations

**Encoding.** A clause $\bigvee_{i \in P} x_i \vee \bigvee_{j \in N} \neg x_j$ becomes the inequality
$$\sum_{i \in P} x_i + \sum_{j \in N} (1 - x_j) \;\ge\; 1 .$$
Axioms $x_i \ge 0$, $-x_i \ge -1$ are available for all $i$.

**Rules.** From $\sum_i a_i x_i \ge b$ and $\sum_i c_i x_i \ge d$ with $a,c \in \mathbb{Z}^n$, $\lambda,\mu \in \mathbb{Z}_{\ge 0}$:
$$\text{(addition)}\quad \sum_i (\lambda a_i + \mu c_i)\,x_i \;\ge\; \lambda b + \mu d,$$
$$\text{(division / Chvátal–Gomory cut)}\quad \frac{\sum_i a_i x_i \ge b}{\sum_i (a_i/c)\,x_i \ge \lceil b/c \rceil}\qquad c \mid a_i \ \ \forall i,\; c \ge 1 .$$
A **refutation** derives $0 \ge 1$. **Length** is the number of lines; **size** counts bits, so coefficient magnitude matters. Buss and Clote (1996) showed coefficients can be normalized without blowing up length beyond a controlled factor, so length and size lower bounds are closely related but not identical.

**Semantic CP** replaces the two rules by: from $I_1, I_2$ infer any $I_3$ with $\{0,1\}^n \cap I_1 \cap I_2 \subseteq I_3$. Filmus, Hrubeš and Lauria (2016) proved semantic CP is *strictly* stronger than syntactic CP (an exponential separation), and semantic CP is not known to be automatable or even to have polynomial-time verifiable lines — all robust lower bound methods target the semantic system anyway.

**Chvátal rank.** For a polytope $P$, the closure $P' = \bigcap_{c \in \mathbb{Z}^n} \{x : c^\top x \ge \lceil \min_{P} c^\top x \rceil\}$; the rank is the least $r$ with $P^{(r)} \cap \{0,1\}^n = P_I$. Rank and length are incomparable measures; the open problem concerns length.

**Interpolation.** For a split CNF $A(\vec p, \vec q) \wedge B(\vec p, \vec r)$ with $\vec p$ occurring positively only in $A$, Pudlák (1997) showed a CP refutation of length $L$ yields a **monotone real circuit** of size $\mathrm{poly}(L)$ separating $\{\vec p : A(\vec p, \cdot) \text{ sat}\}$ from $\{\vec p : B(\vec p, \cdot)\text{ sat}\}$. Combined with Pudlák's $2^{\Omega(n^{1/3}/\log n)}$-type lower bound for monotone real circuits computing clique/colouring, this gives exponential CP lower bounds — but only for formulas of interpolation shape.

**Real communication.** The modern route (Krajíček 1998; Göös–Pitassi 2018; Fleming–Pankratov–Pitassi–Robere) converts a length-$L$ CP refutation of $F$ into a randomized/real dag-like communication protocol for the falsified-clause search problem $\mathrm{Search}(F)$ of cost $O(\log L)$ under any variable partition. Lower bounds on the protocol cost then bound $L$ from below.

## 3. History & State of the Art (SOTA)

- **1958–1973.** Gomory introduces cutting planes for integer programming; Chvátal formalizes the closure and rank.
- **1987.** Cook, Coullard and Turán define CP as a propositional proof system, show it $p$-simulates resolution, and give **polynomial-size** CP refutations of the pigeonhole principle $\mathrm{PHP}^{n+1}_n$ — which is exponentially hard for resolution. This established CP as genuinely stronger.
- **1994.** Impagliazzo, Pitassi and Urquhart prove exponential lower bounds for **tree-like** CP via a rank/effective-interpolation argument.
- **1997.** Bonet, Pitassi and Raz give exponential lower bounds for **CP$^*$** (polynomially bounded coefficients) via monotone interpolation over Boolean circuits. Independently Krajíček develops the general interpolation framework in bounded arithmetic.
- **1997.** Pudlák breaks the coefficient restriction: monotone **real** circuit lower bounds give exponential lower bounds for **unrestricted** CP on the clique–colouring pair. This remains the template for every unrestricted-CP lower bound proved by interpolation.
- **2016.** Filmus–Hrubeš–Lauria separate semantic from syntactic CP.
- **2017.** Two independent breakthroughs remove the interpolation shape requirement: Hrubeš–Pudlák (*Random formulas, monotone circuits, and interpolation*) and Fleming–Pankratov–Pitassi–Robere (*Random $\Theta(\log n)$-CNFs are hard for cutting planes*), the latter giving $\exp(n^{\varepsilon})$ lower bounds for random CNFs of width $\Theta(\log n)$, for semantic CP.
- **2018–2021.** Garg–Göös–Kamath–Sokolov derive monotone circuit lower bounds *from* resolution via lifting, unifying the two directions. Beame et al. introduce Stabbing Planes; Fleming, Göös, Impagliazzo, Pitassi, Robere, Tan and Wigderson analyse the power and limits of branch-and-cut.
- **2020.** Dadush and Tiwari show that Tseitin formulas — long a candidate hard family — admit quasi-polynomial-size CP refutations, eliminating the most natural constant-width candidate.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| Tree-like CP, unrestricted coefficients | $2^{n^{\Omega(1)}}$ for $\mathrm{PHP}$-like and interpolation pairs | Impagliazzo–Pitassi–Urquhart 1994 |
| CP$^*$ (coefficients $\le \mathrm{poly}(n)$), dag-like | $2^{n^{\Omega(1)}}$ for clique–colouring | Bonet–Pitassi–Raz 1997 |
| Unrestricted CP, interpolation-shaped formulas | $2^{\Omega(n^{1/3}/\log n)}$ for the clique–colouring pair, via monotone real circuits | Pudlák 1997 |
| Unrestricted **semantic** CP, width $\Theta(\log n)$ | $\exp(n^{\varepsilon})$ for random $\Theta(\log n)$-CNFs at appropriate density | Fleming–Pankratov–Pitassi–Robere, FOCS 2017 / JACM |
| Unrestricted CP, lifted search problems | $\exp(n^{\Omega(1)})$ for $\mathrm{Search}(F) \circ g^n$ with suitable gadget $g$ (index gadget of width $\Theta(\log n)$) | Göös–Pitassi 2018; Garg–Göös–Kamath–Sokolov 2018 |
| Chvátal rank | $\Omega(n)$ rank lower bounds for many $0/1$ polytopes (e.g. via protection/permutation arguments) | Chvátal–Cook–Hartmann 1989 |
| Constant width $k = O(1)$, dag-like, unrestricted coefficients | **No superpolynomial lower bound known** | — |

Positive (upper bound) side: $\mathrm{PHP}^{n+1}_n$, weak PHP, and Tseitin formulas all have polynomial or quasi-polynomial CP refutations, so none can serve as the hard family.

## 5. Principal Obstacles

- **The $\Theta(\log n)$ width barrier.** All communication-based arguments lift a Boolean search problem through a gadget $g$ whose input length must be $\Omega(\log n)$ for the simulation theorem to hold. Each lifted variable block becomes $\Theta(\log n)$ literals, so the resulting CNF has width $\Theta(\log n)$. No lifting theorem with an $O(1)$-size gadget is known for dag-like real communication.
- **Real-valued communication.** A CP line $\sum a_i x_i \ge b$ splits under a partition into $a^{(1)\top} x^{(1)} \ge b - a^{(2)\top}x^{(2)}$; with unbounded coefficients the exchanged quantity is an arbitrary real/large integer, so only *real* communication (Krajíček's model, one bit per comparison of two privately computed reals) can simulate it. Real communication kills every counting/rank/discrepancy argument that relies on Boolean fooling sets: a single comparison can transmit unboundedly much information about magnitudes.
- **No combinatorial method.** Unlike resolution (width–size, Ben-Sasson–Wigderson) or Nullstellensatz/Sums-of-Squares (degree and pseudo-expectations), CP has no known progress measure. Chvátal rank does not lower-bound length: formulas of rank $\Omega(n)$ can have polynomial-length refutations.
- **Semantic strength.** Any technique must survive the semantic rule, where a line is an arbitrary consequence of two predecessors. This rules out syntactic/normal-form induction and any argument tracking coefficient growth.
- **Candidate exhaustion.** The formulas combinatorialists would try first — PHP, weak PHP, Tseitin, subset-sum with small numbers — are all *easy* for CP, because CP's division rule performs counting and parity-style reasoning cheaply.

## 6. The Gap

Proven: exponential lower bounds when $\mathrm{Search}(F)$ has high dag-like real communication complexity, which today requires either (a) an explicit interpolation split reducing to monotone real circuits, or (b) width $\Theta(\log n)$ arising from lifting or random $\Theta(\log n)$-CNFs.

Wanted: the same bound for width-$O(1)$ formulas with no split.

The exact missing step is a **lifting theorem for real dag-like communication with constant-size gadgets**, or a genuinely different measure. Equivalently: show that some constant-width CNF has search problem with $\mathrm{poly}(n)$ real dag-like communication complexity lower bound $\omega(\log n)$ without gadget composition. The gap is not quantitative slack in an existing bound — it is a structural requirement of the only known simulation.

## 7. Current Research (as of June 2026)

- **Lifting with small gadgets.** Groups at Simons/Toronto (Pitassi, Robere), IAS/Prague (Pudlák, Hrubeš) and Copenhagen (Nordström's group) pursue lifting theorems with $O(1)$-bit or sub-logarithmic gadgets; partial results exist for deterministic Boolean lifting but not for real dag-like protocols. *(frontier — verify)*
- **Stabbing Planes and branch-and-cut.** Lower bounds for Stabbing Planes with large coefficients, and the exact relation between Stabbing Planes size and CP length, are actively studied; the SP-to-CP translation is quasi-polynomial and known to be tight in restricted regimes. *(frontier — verify)*
- **Monotone circuit transfer.** Following Garg–Göös–Kamath–Sokolov, several groups treat monotone circuit lower bounds and CP lower bounds as one problem, seeking monotone-real-circuit lower bounds for functions with constant-width certificate structure.
- **Weak systems above CP.** Attempts to lower-bound $\mathrm{CP}$ + counting axioms, or $\mathrm{TC}^0$-Frege, motivate CP as the last frontier before Frege lower bounds. No non-trivial lower bound is known for $\mathrm{AC}^0[p]$-Frege or $\mathrm{TC}^0$-Frege, and CP with large coefficients is regarded as the accessible sub-case.
- **SAT-solving side.** Pseudo-Boolean solvers (RoundingSat, Sat4j) empirically probe which families need large coefficients; hardness observations there feed candidate hard families back to theory.

## 8. Future Work

- Identify a constant-width candidate not killed by CP's counting power: proposals include random constant-width CNFs at density just above the satisfiability threshold, binary-encoded PHP, and Tseitin over $\mathbb{Z}_p$ with $p$ large relative to degree.
- Develop a *rank-like* progress measure that is monotone under the semantic rule; candidates are pseudo-distributions supported on $\{0,1\}^n$ that survive Chvátal–Gomory rounding.
- Prove lower bounds for real dag-like communication directly, e.g. via topological or measure-theoretic arguments on threshold functions rather than counting rectangles.
- Settle whether CP with unbounded coefficients $p$-simulates CP$^*$ with only polynomial length overhead when the underlying formula has constant width.
- Extend Filmus–Hrubeš–Lauria to show semantic CP is exponentially separated from syntactic CP on *natural* families, clarifying which system the barriers actually apply to.

## 9. Key References

- **[Foundational]** W. Cook, C. R. Coullard, G. Turán. *On the complexity of cutting-plane proofs.* Discrete Applied Mathematics 18(1), 25–38, 1987.
- **[Foundational]** V. Chvátal. *Edmonds polytopes and a hierarchy of combinatorial problems.* Discrete Mathematics 4(4), 305–337, 1973.
- **[Foundational]** P. Pudlák. *Lower bounds for resolution and cutting plane proofs and monotone computations.* Journal of Symbolic Logic 62(3), 981–998, 1997.
- **[Foundational]** J. Krajíček. *Interpolation theorems, lower bounds for proof systems, and independence results for bounded arithmetic.* Journal of Symbolic Logic 62(2), 457–486, 1997.
- **[Foundational]** M. L. Bonet, T. Pitassi, R. Raz. *Lower bounds for cutting planes proofs with small coefficients.* Journal of Symbolic Logic 62(3), 708–728, 1997.
- **[Foundational]** R. Impagliazzo, T. Pitassi, A. Urquhart. *Upper and lower bounds for tree-like cutting planes proofs.* LICS 1994, 220–228.
- **[SOTA / Recent]** N. Fleming, D. Pankratov, T. Pitassi, R. Robere. *Random $\Theta(\log n)$-CNFs are hard for cutting planes.* FOCS 2017; Journal of the ACM, 2022.
- **[SOTA / Recent]** P. Hrubeš, P. Pudlák. *Random formulas, monotone circuits, and interpolation.* FOCS 2017, 121–131.
- **[SOTA / Recent]** A. Garg, M. Göös, P. Kamath, D. Sokolov. *Monotone circuit lower bounds from resolution.* STOC 2018, 902–911.
- **[SOTA / Recent]** M. Göös, T. Pitassi. *Communication lower bounds via critical block sensitivity.* SIAM Journal on Computing 47(5), 2018.
- **[SOTA / Recent]** Y. Filmus, P. Hrubeš, M. Lauria. *Semantic versus syntactic cutting planes.* STACS 2016.
- **[SOTA / Recent]** D. Dadush, S. Tiwari. *On the complexity of branching proofs.* CCC 2020.
- **[SOTA / Recent]** P. Beame, N. Fleming, R. Impagliazzo, A. Kolokolova, D. Pankratov, T. Pitassi, R. Robere. *Stabbing planes.* ITCS 2018.
- **[Survey]** J. Krajíček. *Proof Complexity.* Cambridge University Press, Encyclopedia of Mathematics and its Applications 170, 2019.
- **[Survey]** S. Buss, P. Clote. *Cutting planes, connectivity, and threshold logic.* Archive for Mathematical Logic 35(1), 33–62, 1996.

## 10. Worked Example / Concrete Special Case

**Why division (and coefficient size) is the whole story.** Take $n = 2$ and the system
$$I_1:\; 2x_1 + 2x_2 \ge 1, \qquad I_2:\; -2x_1 - 2x_2 \ge -1, \qquad x_1,x_2 \in \{0,1\}.$$
Over the reals this is *feasible*: $x = (\tfrac14,\tfrac14)$ satisfies both. So no non-negative linear combination alone yields $0 \ge 1$ — the addition rule is provably insufficient.

Apply division by $c = 2$ to each:
$$\frac{2x_1+2x_2 \ge 1}{x_1 + x_2 \ge \lceil 1/2 \rceil = 1}, \qquad \frac{-2x_1-2x_2 \ge -1}{-x_1 - x_2 \ge \lceil -1/2 \rceil = 0}.$$
Adding the two conclusions with $\lambda = \mu = 1$:
$$0 \ge 1 .$$
A four-line refutation of Chvátal rank $1$, entirely driven by the rounding $\lceil 1/2 \rceil = 1$.

**Scaling to large coefficients.** Replace $2$ by $M = 2^n$ and take
$$\sum_{i=1}^{n} M x_i \ge 1, \qquad -\sum_{i=1}^n M x_i \ge -(M-1).$$
Division by $M$ gives $\sum_i x_i \ge 1$ and $-\sum_i x_i \ge \lceil -(M-1)/M \rceil = 0$, again contradictory in $4$ lines. The same reasoning expressed with coefficients bounded by $\mathrm{poly}(n)$ requires simulating the binary magnitude $M$ across many lines; this coefficient gap is exactly what Bonet–Pitassi–Raz exploit for CP$^*$ and exactly what defeats every attempt to extend their Boolean monotone-circuit extraction to unrestricted CP.

**Where the barrier bites.** Under a partition $x^{(1)} \mid x^{(2)}$, verifying the line $\sum_i M x_i \ge 1$ requires the two players to compare $M \cdot |x^{(1)}|$ against $1 - M\cdot|x^{(2)}|$ — numbers of $\Theta(n)$ bits. In Krajíček's real communication model this is one round; in the Boolean model it costs $\Theta(n)$ bits. Any lower bound method that charges Boolean bits therefore proves nothing about unrestricted CP, and the only surviving model — real dag-like communication — currently admits lower bounds only for lifted, $\Theta(\log n)$-width search problems. That is the gap of Section 6, in miniature.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*