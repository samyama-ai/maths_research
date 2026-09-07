---
id: 10-theoretical-cs/nc1-versus-p
title: "NC1 versus P"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NC1 versus P

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/nc1-versus-p` · **Status:** open

## 1. Problem Statement / Conjecture

$\mathsf{NC}^1$ is the class of languages decided by Boolean circuit families of fan-in-2 gates, polynomial size and $O(\log n)$ depth. $\mathsf{P}$ is the class decided in deterministic polynomial time. The containment $\mathsf{NC}^1 \subseteq \mathsf{P}$ is immediate (evaluate the circuit gate by gate).

**Conjecture.** $\mathsf{NC}^1 \neq \mathsf{P}$ — i.e. some polynomial-time-decidable language admits no polynomial-size logarithmic-depth circuit family. Equivalently (by the depth/formula correspondence, §2), some language in $\mathsf{P}$ requires Boolean formulas of superpolynomial size.

A complete resolution requires either:

- **(Separation)** an explicit language $L \in \mathsf{P}$ together with a proof that every circuit family of depth $O(\log n)$ deciding $L$ has superpolynomial size; or
- **(Collapse)** a uniform $O(\log n)$-depth polynomial-size circuit family for a $\mathsf{P}$-complete problem (e.g. the Circuit Value Problem), which would give $\mathsf{NC}^1 = \mathsf{L} = \mathsf{NL} = \mathsf{P}$.

The question is the "fast parallel computation" question: is every efficiently sequentially computable problem also efficiently parallelizable to logarithmic depth?

## 2. Mathematical Foundations

**Circuits.** A Boolean circuit $C$ on $n$ inputs is a DAG whose sources are labelled $x_1,\dots,x_n,\neg x_1,\dots,\neg x_n$ or constants, internal nodes are $\wedge,\vee$ of fan-in 2, with one sink. $\mathrm{size}(C)$ = number of gates, $\mathrm{depth}(C)$ = longest source-sink path.

$$\mathsf{NC}^k = \{L : \exists\, (C_n)_{n\ge 1},\ \mathrm{size}(C_n) = n^{O(1)},\ \mathrm{depth}(C_n) = O(\log^k n)\},\qquad \mathsf{NC} = \bigcup_k \mathsf{NC}^k .$$

$\mathsf{AC}^k$ is the same with unbounded fan-in $\wedge,\vee$. Uniformity (typically $\mathsf{DLOGTIME}$- or logspace-uniform) is required for the question to be about $\mathsf{P}$ rather than $\mathsf{P}/\mathrm{poly}$; the non-uniform version $\mathsf{NC}^1/\mathrm{poly}$ vs. $\mathsf{P}$ is also open and formally stronger.

**Formulas.** A formula is a circuit whose DAG is a tree. For $f:\{0,1\}^n\to\{0,1\}$ let $L(f)$ be the minimum de Morgan formula size (leaves) and $D(f)$ the minimum depth. Spira's theorem gives the balancing equivalence

$$D(f) \le O(\log L(f)), \qquad L(f) \le 2^{D(f)},$$

so $\mathsf{NC}^1$ = languages with polynomial-size formulas. Hence $\mathsf{NC}^1 \ne \mathsf{P}$ iff some $f_n \in \mathsf{P}$ has $L(f_n) = n^{\omega(1)}$.

**Branching programs.** A width-$w$ branching program of length $\ell$ is a sequence of instructions $\langle i_t, \sigma_t^0, \sigma_t^1\rangle_{t\le \ell}$ with $\sigma_t^b$ maps $[w]\to[w]$; the program computes the composition $\prod_{t} \sigma_t^{x_{i_t}}$. **Barrington's theorem** (1989): a language is in (non-uniform) $\mathsf{NC}^1$ iff it is computed by width-5 permutation branching programs of polynomial length. The key algebraic fact is that $S_5$ is non-solvable: there exist 5-cycles whose commutator is a 5-cycle.

**Known chain.**
$$\mathsf{NC}^1 \subseteq \mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{LOGCFL} \subseteq \mathsf{AC}^1 \subseteq \mathsf{NC}^2 \subseteq \cdots \subseteq \mathsf{NC} \subseteq \mathsf{P}.$$
Every inclusion here is open; $\mathsf{NC}^1 = \mathsf{P}$ would collapse all of them.

**Karchmer–Wigderson games.** For $f$ with $f^{-1}(0)=A$, $f^{-1}(1)=B$, define the relation $\mathrm{KW}_f \subseteq A\times B\times[n]$: given $a\in A$, $b\in B$, Alice and Bob must output $i$ with $a_i\ne b_i$. Then
$$D(f) = \mathrm{CC}(\mathrm{KW}_f),$$
the deterministic communication complexity. Separating $\mathsf{NC}^1$ from $\mathsf{P}$ is exactly: exhibit $f\in\mathsf{P}$ with $\mathrm{CC}(\mathrm{KW}_f) = \omega(\log n)$.

**KRW conjecture.** For $f:\{0,1\}^m\to\{0,1\}$, $g:\{0,1\}^n\to\{0,1\}$, the block composition $f \diamond g:\{0,1\}^{m\times n}\to\{0,1\}$ is $f(g(X_1),\dots,g(X_m))$. Conjecture (Karchmer–Raz–Wigderson 1995):
$$D(f\diamond g) \;\approx\; D(f) + D(g) \quad\text{(up to additive lower-order terms)}.$$
Iterating with $g$ a random-ish function on $O(\log n)$ bits yields an explicit $f \in \mathsf{P}$ with $D(f) = \omega(\log n)$, hence $\mathsf{P} \not\subseteq \mathsf{NC}^1$.

## 3. History & State of the Art

- **1975** — Ladner proves the Circuit Value Problem is $\mathsf{P}$-complete under logspace reductions, giving the class its canonical hard problem.
- **1977** — Borodin formalizes the parallel-computation thesis (space $\leftrightarrow$ parallel time), showing $\mathsf{NSPACE}(s) \subseteq \mathsf{DEPTH}(s^2)$; this places $\mathsf{NL}\subseteq \mathsf{NC}^2$ and frames $\mathsf{NC}$ vs $\mathsf{P}$.
- **1979** — Pippenger and Cook isolate $\mathsf{NC}$ ("Nick's Class"); Cook's 1985 taxonomy catalogues $\mathsf{P}$-complete problems as the presumed obstructions to parallelization.
- **1987–89** — Barrington's width-5 characterization; extended by Barrington–Thérien to a program-over-monoids theory where solvable monoids give $\mathsf{ACC}^0$ and non-solvable groups give $\mathsf{NC}^1$.
- **1990** — Karchmer–Wigderson reformulate depth as communication and prove monotone depth $\Theta(\log^2 n)$ for $st$-connectivity, giving $\mathsf{mNC}^1 \subsetneq \mathsf{mNC}^2$.
- **1995** — KRW propose the composition approach as a concrete route to $\mathsf{P}\not\subseteq\mathsf{NC}^1$.
- **1998** — Håstad's shrinkage exponent $\Gamma = 2$ under random restrictions yields $L(\mathrm{Andreev}) \ge n^{3-o(1)}$, the record for de Morgan formulas.
- **2014** — Tal sharpens this to $\Omega(n^3/\log^2 n)$.
- **2018–2023** — Dinur–Meir, Gavinsky–Meir–Weinstein–Wigderson and Meir prove KRW-type composition theorems in restricted settings (universal relation, $g$ = XOR, "strong composition").

**SOTA.** No superlinear-in-depth lower bound is known for any explicit $f\in\mathsf{P}$ in the general (non-monotone, unrestricted) model. The best explicit de Morgan depth bound is $(3-o(1))\log_2 n$; the best general-basis formula bound is Nečiporuk's $\Omega(n^2/\log n)$ (1966). Both are polynomially far from the required $n^{\omega(1)}$.

## 4. Partial Results / Verified Cases

- **Monotone model (fully solved).** Raz–McKenzie (1999) prove the monotone $\mathsf{NC}$ hierarchy is infinite and $\mathsf{mNC} \subsetneq \mathsf{mP}$; in particular $\mathsf{mNC}^1 \subsetneq \mathsf{mP}$. Karchmer–Wigderson give $\Omega(\log^2 n)$ monotone depth for $st$-CONN.
- **Bounded-depth restrictions.** $\mathsf{AC}^0 \subsetneq \mathsf{NC}^1$ (PARITY, Furst–Saxe–Sipser, Håstad); $\mathsf{ACC}^0[p] \subsetneq \mathsf{NC}^1$ for prime $p$ (Razborov, Smolensky). $\mathsf{NEXP}\not\subseteq \mathsf{ACC}^0$ (Williams 2011).
- **Bounded width / algebraic restrictions.** Width-$w$ *solvable*-group branching programs compute only $\mathsf{ACC}^0$, hence not $\mathsf{NC}^1$-complete problems — a full separation inside the program-over-monoid model.
- **Formula-size lower bounds for explicit $f\in\mathsf{P}$.** Andreev's function: $\Omega(n^3/\log^2 n)$ (Tal 2014). Element distinctness: $\Omega(n^2/\log n)$ over the full binary basis (Nečiporuk).
- **Diagonalization-reachable separations.** $\mathsf{NC}^1 \subsetneq \mathsf{PSPACE}$ (via $\mathsf{L}\subsetneq\mathsf{PSPACE}$, space hierarchy). $\mathsf{NC}^1 \ne \mathsf{MAJ}\text{-}\mathsf{SPACE}$-type classes by counting.
- **Relativized worlds.** Wilson (1985) constructs oracles $A$ with $\mathsf{NC}^{1,A} = \mathsf{P}^A$ and oracles with the $\mathsf{NC}^A$ hierarchy infinite.
- **Small $n$.** Exhaustive circuit search verifies optimal depth only for $n \le 5$-ish input functions (Knuth, *TAOCP* 7.1.2), far below any asymptotic statement.

## 5. Principal Obstacles

- **Natural proofs.** Razborov–Rudich (1997): a *natural* (constructive + large) combinatorial property that separates $\mathsf{NC}^1$ from $\mathsf{P}$ would break pseudorandom generators computable in $\mathsf{NC}^1$. Since PRGs based on factoring/discrete log are believed to lie in $\mathsf{NC}^1$ (in fact in $\mathsf{TC}^0$), essentially all known random-restriction and approximation methods are barred from extending to the general basis.
- **Shrinkage saturates.** Random restrictions give $\mathbb{E}[L(f\!\restriction_\rho)] \lesssim p^{\Gamma} L(f)$ with $\Gamma = 2$ for de Morgan formulas, and $\Gamma=2$ is *tight*. This caps the method at $n^{3}$-type bounds: no restriction-based argument can reach superpolynomial size.
- **General basis is restriction-immune.** Over the full binary basis, $\oplus$ gates survive restrictions, so shrinkage fails entirely; Nečiporuk's counting-of-subfunctions method provably cannot exceed $n^2/\log n$.
- **Composition loses information.** The direct-sum intuition behind KRW fails to be provable because Alice/Bob in $\mathrm{KW}_{f\diamond g}$ can interleave protocols across blocks. Lifting theorems (Raz–McKenzie, Göös–Pitassi–Watson, Chattopadhyay et al.) convert query lower bounds to communication ones only for structured "gadget" inner functions with large enough gadget size — not for arbitrary $g$.
- **Monotone methods do not transfer.** Every known super-logarithmic depth bound uses monotonicity crucially (via monotone KW games on minterms/maxterms); negations destroy the combinatorial structure, and $\mathsf{mP}\subsetneq \mathsf{mNC}$ results say nothing about the non-monotone classes.
- **Relativization/algebrization.** Wilson's oracles rule out purely simulation-based arguments; Aaronson–Wigderson's algebrization barrier blocks arithmetization-only proofs.

## 6. The Gap

Proven (§4): superpolynomial-size lower bounds only in the *monotone* or *bounded-depth/solvable-algebra* models; in the general model, formula-size bounds of at most $n^{3-o(1)}$, equivalently depth $(3-o(1))\log_2 n$.

Required (§1): depth $\omega(\log n)$, equivalently formula size $n^{\omega(1)}$, for some explicit $f\in\mathsf{P}$.

The gap is the passage from a *fixed polynomial* to a *superpolynomial* formula-size bound. The single cleanest crossing point is the KRW conjecture: it is known that if
$$D(f \diamond g)\;\ge\; D(f) + D(g) - o(D(f)+D(g))$$
holds for all $f$ and for $g$ chosen as a hard function on $O(\log n)$ bits, then iterating $\Theta(\log n/\log\log n)$ times produces $f^{\diamond k} \in \mathsf{P}$ with depth $\Omega(\log^2 n/\log\log n)$, resolving the problem. What is missing is a composition theorem for *arbitrary* outer $f$ and *arbitrary* inner $g$, rather than for the universal relation, for $g=\oplus$, or for lifting-friendly gadgets.

## 7. Current Research (as of June 2026)

- **KRW program.** The dominant line: Dinur–Meir (2018) proved $D(f\diamond \oplus)\ge D(f)+D(\oplus)-O(1)$-type statements via "structure vs. pseudorandomness" on KW games; Meir's *strong composition* framework (2023) upgrades the XOR case and identifies what must change to handle random inner functions. Groups at Weizmann (Meir, Tal), IAS/Princeton (Wigderson), Toronto (Pitassi), and Simons-affiliated researchers drive this. *(frontier — verify)* Reports of composition theorems for a broad class of inner functions with $O(\log n)$ input length remain unverified at the time of writing.
- **Lifting theorems.** Query-to-communication lifting with small gadgets (inner product, sink, majority) is being pushed toward constant-size gadgets — a necessary step for KRW, since the inner function must have logarithmic input length.
- **Algebraic/monoid approaches.** Program-over-algebra and the "$\mathsf{NC}^1 = \mathsf{TC}^0$?" sub-question; work on multiparty and semigroup analogues of Barrington's theorem.
- **Fine-grained parallelism.** Rather than the asymptotic separation, conditional hardness of specific $\mathsf{P}$-complete problems (linear programming, lexicographically-first maximal independent set, Horn satisfiability) under $\mathsf{NC}$-reductions continues to accumulate.
- **Proof-complexity connections.** Lower bounds for Frege systems in bounded depth mirror $\mathsf{NC}^1$ questions (Frege proofs of polynomial size correspond to $\mathsf{NC}^1$-Frege); progress on $\mathsf{AC}^0[p]$-Frege is watched as a proxy.

## 8. Future Work

- Prove KRW for $g$ a random function on $O(\log n)$ bits and arbitrary $f$ — Wigderson and Meir both name this as the concrete milestone.
- Develop *non-natural* lower-bound techniques: constructions exploiting uniformity or algorithmic-method arguments à la Williams, which evade Razborov–Rudich by being non-constructive or by targeting non-large properties.
- Break the $\Gamma = 2$ shrinkage barrier by combining restrictions with a second, non-restriction resource (e.g. quantum/approximate-degree measures, which have already given $n^{3-o(1)}$ *average-case* bounds).
- Settle intermediate separations first: $\mathsf{NC}^1 \ne \mathsf{L}$, $\mathsf{L}\ne\mathsf{P}$, or $\mathsf{TC}^0 \ne \mathsf{NC}^1$ — each is strictly easier and would supply the first non-relativizing technique.
- Search for a "hardness magnification" threshold: show that a modest formula-size bound ($n^{1+\varepsilon}$) for a specific sparse problem already implies $\mathsf{NC}^1\ne\mathsf{P}$.

## 9. Key References

- **[Foundational]** Richard E. Ladner. *The circuit value problem is log space complete for P.* ACM SIGACT News 7(1), 1975.
- **[Foundational]** Allan Borodin. *On relating time and space to size and depth.* SIAM Journal on Computing 6(4), 1977.
- **[Foundational]** David A. Mix Barrington. *Bounded-width polynomial-size branching programs recognize exactly those languages in $NC^1$.* Journal of Computer and System Sciences 38(1), 1989.
- **[Foundational]** Mauricio Karchmer, Avi Wigderson. *Monotone circuits for connectivity require super-logarithmic depth.* SIAM Journal on Discrete Mathematics 3(2), 1990.
- **[Foundational]** Mauricio Karchmer, Ran Raz, Avi Wigderson. *Super-logarithmic depth lower bounds via the direct sum in communication complexity.* Computational Complexity 5, 1995.
- **[SOTA]** Johan Håstad. *The shrinkage exponent of de Morgan formulas is 2.* SIAM Journal on Computing 27(1), 1998.
- **[SOTA]** Avishay Tal. *Shrinkage of De Morgan formulae by spectral sensitivity.* Proc. 55th IEEE FOCS, 2014.
- **[SOTA]** Ran Raz, Pierre McKenzie. *Separation of the monotone NC hierarchy.* Combinatorica 19(3), 1999.
- **[SOTA / Recent]** Irit Dinur, Or Meir. *Toward the KRW composition conjecture: cubic formula lower bounds via communication complexity.* Computational Complexity 27, 2018.
- **[SOTA / Recent]** Or Meir. *Toward better depth lower bounds: strong composition of XOR and a random function.* Proc. 38th Computational Complexity Conference (CCC), 2023.
- **[Barrier]** Alexander A. Razborov, Steven Rudich. *Natural proofs.* Journal of Computer and System Sciences 55(1), 1997.
- **[Survey]** Raymond Greenlaw, H. James Hoover, Walter L. Ruzzo. *Limits to Parallel Computation: P-Completeness Theory.* Oxford University Press, 1995.
- **[Survey]** Stephen A. Cook. *A taxonomy of problems with fast parallel algorithms.* Information and Control 64(1–3), 1985.
- **[Textbook]** Stasys Jukna. *Boolean Function Complexity: Advances and Frontiers.* Springer, 2012.

## 10. Worked Example / Concrete Special Case

**Barrington's construction for $\mathsf{AND}$ of two bits, width 5.**

Fix the 5-cycles
$$\alpha = (1\,2\,3\,4\,5), \qquad \beta = (1\,3\,5\,4\,2).$$
Their commutator is
$$\gamma = \alpha\beta\alpha^{-1}\beta^{-1} = (1\,4\,3\,5\,2),$$
verified pointwise (composing right-to-left): $1\mapsto 2\mapsto 1\mapsto 3\mapsto 4$; $4\mapsto5\mapsto4\mapsto2\mapsto3$; $3\mapsto1\mapsto5\mapsto4\mapsto5$; $5\mapsto3\mapsto2\mapsto1\mapsto2$; $2\mapsto4\mapsto3\mapsto5\mapsto1$. So $\gamma$ is again a 5-cycle — the non-solvability of $S_5$ made explicit.

Say a program $P$ **$\sigma$-computes** $h$ if $\prod_t \sigma_t^{x} = \sigma$ when $h(x)=1$ and $=\mathrm{id}$ when $h(x)=0$. Suppose $P_1$ $\alpha$-computes $x_1$ (length 1: output $\alpha$ if $x_1=1$, else $\mathrm{id}$) and $P_2$ $\beta$-computes $x_2$. Concatenate
$$P \;=\; P_1 \cdot P_2 \cdot P_1^{-1} \cdot P_2^{-1},$$
of length 4. If $x_1\wedge x_2 = 1$ the product is $\alpha\beta\alpha^{-1}\beta^{-1} = \gamma$; if either bit is 0 the corresponding factors are $\mathrm{id}$ and the remaining pair cancels, giving $\mathrm{id}$. So $P$ $\gamma$-computes $x_1\wedge x_2$ in width 5, length 4.

**Scaling.** A depth-$d$ formula becomes a width-5 program of length $\le 4^{d}$ by recursing on this identity (conjugation converts between output cycles at no length cost; $\neg$ costs a single relabelling). With $d = c\log_2 n$ the length is $4^{c\log_2 n} = n^{2c}$ — polynomial. Conversely a width-5 program of length $\ell$ balances into depth $O(\log \ell)$.

**What the separation would mean here.** $\mathsf{NC}^1 = \mathsf{P}$ is equivalent to: the Circuit Value Problem on $n$-gate circuits is decided by width-5 permutation branching programs of length $n^{O(1)}$. CVP asks, given a circuit description and input, for the output bit — a computation that appears inherently sequential, since gate $i$'s value can depend on gate $i-1$'s. The conjecture $\mathsf{NC}^1\ne\mathsf{P}$ says no polynomial-length constant-width "straight-line" product in $S_5$ can unwind that dependency chain. Nothing currently proved excludes it: the best lower bound for CVP restricted to formulas is $\Omega(n^2/\log n)$, five orders of quantifier away from superpolynomial.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*