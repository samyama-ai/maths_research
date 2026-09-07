---
id: 10-theoretical-cs/nc-versus-p
title: "NC versus P"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NC versus P

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/nc-versus-p` · **Status:** open

## 1. Problem Statement / Conjecture

$\mathsf{NC}$ is the class of languages decided by uniform Boolean circuit families of polynomial size and polylogarithmic depth — equivalently, problems solvable in polylogarithmic parallel time on a polynomial number of processors. $\mathsf{P}$ is deterministic polynomial time. The containment $\mathsf{NC} \subseteq \mathsf{P}$ is elementary. The open question:

$$\text{Is } \mathsf{NC} = \mathsf{P}\,?$$

**Conjecture (widely believed).** $\mathsf{NC} \subsetneq \mathsf{P}$: some polynomial-time problem is *inherently sequential*, admitting no polylog-depth polynomial-size circuit family.

A resolution requires either (a) a uniform polylog-depth, poly-size circuit family for a $\mathsf{P}$-complete problem such as the Circuit Value Problem, which by closure under $\mathsf{NC}$-reductions collapses $\mathsf{NC} = \mathsf{P}$; or (b) a proof that some explicit language in $\mathsf{P}$ requires depth $\omega(\log^k n)$ for every fixed $k$ at polynomial size. Note $\mathsf{NC} \neq \mathsf{P}$ is not known to follow from $\mathsf{P} \neq \mathsf{NP}$, nor conversely.

## 2. Mathematical Foundations

**Circuits.** A Boolean circuit $C_n$ on $n$ inputs is a DAG whose nodes are inputs $x_1,\dots,x_n$, constants, and gates from a basis $B$. *Size* $|C_n|$ = number of gates; *depth* $d(C_n)$ = longest directed input–output path.

**The $\mathsf{NC}$ hierarchy.** For $i \ge 1$, $L \in \mathsf{NC}^i$ iff there is a DLOGTIME-uniform family $\{C_n\}$ over the basis $\{\wedge,\vee,\neg\}$ with fan-in $2$ such that
$$|C_n| = n^{O(1)}, \qquad d(C_n) = O(\log^i n), \qquad C_n(x) = 1 \iff x \in L .$$
$\mathsf{AC}^i$ is the same with unbounded fan-in $\wedge,\vee$. Then
$$\mathsf{NC}^i \subseteq \mathsf{AC}^i \subseteq \mathsf{NC}^{i+1}, \qquad \mathsf{NC} = \bigcup_{i\ge 1}\mathsf{NC}^i = \bigcup_{i \ge 0}\mathsf{AC}^i .$$

**Known chain.** $\mathsf{AC}^0 \subsetneq \mathsf{NC}^1 \subseteq \mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{AC}^1 \subseteq \mathsf{NC}^2 \subseteq \cdots \subseteq \mathsf{NC} \subseteq \mathsf{P}$. The inclusions $\mathsf{NC}^1 \subseteq \mathsf{L}$ and $\mathsf{NL} \subseteq \mathsf{NC}^2$ are Borodin's (1977).

**PRAM equivalence.** $L \in \mathsf{NC}^i$ iff $L$ is decided by a CRCW PRAM in time $O(\log^i n)$ using $n^{O(1)}$ processors (Stockmeyer–Vishkin). This makes "$\mathsf{NC} = \mathsf{P}$?" the formal version of "is everything feasible also efficiently parallelizable?"

**$\mathsf{P}$-completeness.** $A \le_{\mathsf{NC}^1} B$ if there is an $\mathsf{NC}^1$-computable $f$ with $x \in A \iff f(x) \in B$ (logspace reductions are also standard). $B$ is $\mathsf{P}$-complete if $B \in \mathsf{P}$ and every $A \in \mathsf{P}$ reduces to $B$. Since $\mathsf{NC}$ is closed under these reductions:
$$\exists\, B \ \mathsf{P}\text{-complete with } B \in \mathsf{NC} \iff \mathsf{NC} = \mathsf{P}.$$

**Canonical complete problem.** CVP: given an encoding of a Boolean circuit $C$ and an input $x$, decide whether $C(x)=1$. Ladner (1975) proved CVP is logspace-complete for $\mathsf{P}$.

**Karchmer–Wigderson games.** For non-constant $f:\{0,1\}^n\to\{0,1\}$, let $\mathrm{KW}_f$ be the relation where Alice holds $a \in f^{-1}(1)$, Bob holds $b \in f^{-1}(0)$, and they must output an index $i$ with $a_i \neq b_i$. Then
$$\mathrm{depth}(f) = \mathrm{CC}(\mathrm{KW}_f),$$
the deterministic communication complexity. Depth lower bounds are exactly communication lower bounds — the main formal handle on the problem.

**Barrington's theorem (1989).** $\mathsf{NC}^1$ equals the languages recognized by polynomial-length width-$5$ permutation branching programs over $S_5$, using the commutator identity: for $5$-cycles $\sigma,\tau$ with $[\sigma,\tau]=\sigma\tau\sigma^{-1}\tau^{-1}$ again a $5$-cycle.

## 3. History & State of the Art

- **1975.** Ladner: CVP is $\mathsf{P}$-complete — the fixed point of the whole theory.
- **1976.** Csanky: determinant and matrix inverse over fields of characteristic $0$ in $\mathsf{NC}^2$; the first surprising parallelization of an apparently sequential task.
- **1979.** Pippenger: simultaneous size–depth characterization; Nick Pippenger's initials give the class its name (coined by Cook).
- **1979–85.** $\mathsf{P}$-completeness catalog grows: maximum flow (Goldschlager–Shaw–Staples 1982), linear programming (Dobkin–Lipton–Reiss 1979), lexicographically-first maximal independent set, Horn-SAT, and depth-first search order (Reif 1985).
- **1984–87.** The only unconditional separations at the bottom: $\mathsf{AC}^0 \subsetneq \mathsf{NC}^1$ (Furst–Saxe–Sipser, Ajtai; optimal $\exp(\Omega(n^{1/(d-1)}))$ parity bound by Håstad's switching lemma), and $\mathsf{AC}^0[p] \subsetneq \mathsf{NC}^1$ for prime $p$ (Razborov, Smolensky).
- **1990–92.** Monotone depth lower bounds: $\Omega(\log^2 n)$ for $st$-connectivity (Karchmer–Wigderson), $\Omega(n)$ for perfect matching (Raz–Wigderson) — i.e. **monotone-$\mathsf{NC} \neq$ monotone-$\mathsf{P}$**.
- **1995.** Greenlaw–Hoover–Ruzzo's monograph lists $\sim$150 $\mathsf{P}$-complete problems.
- **1998–2014.** Formula-size frontier: Håstad's shrinkage exponent $2$ gives $n^{3-o(1)}$ formula size for Andreev's function, i.e. depth $\ge (3-o(1))\log n$; refined by Tal (2014). This is the best explicit De Morgan formula bound known and is a factor of $\log^{k}$ away from anything relevant.
- **2016–20.** Randomized $\to$ quasi-$\mathsf{NC}$ derandomization for matching (below).
- **2018–present.** KRW-conjecture program (Dinur–Meir; Mihajlin–Smal; lifting theorems) as the mainstream route to super-logarithmic depth.

## 4. Partial Results / Verified Cases

Solved *positively* — problems once thought sequential, now in $\mathsf{NC}$:

- Determinant, matrix inverse, characteristic polynomial, rank over $\mathbb{Q}$ and finite fields: $\mathsf{NC}^2$ (Csanky 1976; Berkowitz 1984 for arbitrary rings).
- Maximal independent set, maximal matching, $(\Delta+1)$-coloring: $\mathsf{NC}^2$ (Karp–Wigderson 1985; Luby 1986 — $O(\log^2 n)$ rounds).
- Integer arithmetic: addition and comparison in $\mathsf{AC}^0$; multiplication, iterated addition, division in $\mathsf{TC}^0 \subseteq \mathsf{NC}^1$ (Hesse–Allender–Barrington 2002).
- Perfect matching: $\mathsf{RNC}^2$ (Mulmuley–Vazirani–Vazirani 1987, Isolation Lemma); **quasi-$\mathsf{NC}^2$** — depth $O(\log^3 n)$, size $2^{O(\log^3 n)}$ — for bipartite graphs (Fenner–Gurjar–Thierauf 2016) and general graphs (Svensson–Tarnawski 2017); fully in $\mathsf{NC}$ for planar and bounded-genus graphs (Anari–Vazirani 2020).
- Restricted CVP: planar monotone CVP is in $\mathsf{NC}$ (Yang 1991; Delcher–Kosaraju), while planar CVP and monotone CVP remain $\mathsf{P}$-complete.
- Two-player games / regular languages / bounded-width computations: $\mathsf{NC}^1$ by Barrington.

Solved *negatively* in restricted models:

- Monotone circuits: matching needs monotone depth $\Omega(n)$ (Raz–Wigderson 1992); $st$-connectivity needs $\Omega(\log^2 n)$, separating monotone $\mathsf{NC}^1$ from monotone $\mathsf{NC}^2$ (Karchmer–Wigderson 1990).
- Constant depth: $\mathsf{AC}^0 \subsetneq \mathsf{AC}^0[p] \subsetneq \mathsf{NC}^1$ for prime $p$.
- Bounded-width / read-once branching programs, monotone span programs, and several proof-complexity analogues all give unconditional separations.

## 5. Principal Obstacles

- **No super-logarithmic depth bound for any explicit function.** For general (non-monotone) circuits, the best depth lower bound for an explicit $f$ is $(3-o(1))\log n$ from formula size $n^{3-o(1)}$ (Håstad 1998, Tal 2014). Separating $\mathsf{NC}^1$ from $\mathsf{P}$ needs $\omega(\log n)$ depth; separating $\mathsf{NC}$ from $\mathsf{P}$ needs $\omega(\log^k n)$ for all $k$. General circuit-size bounds are worse still: $(3+\tfrac{1}{86})n$ (Find–Golovnev–Hirsch–Kulikov 2016), against the $n^{O(1)}$ size that $\mathsf{NC}$ already allows.
- **Monotone methods do not lift.** Razborov's approximation method and Raz–Wigderson's monotone-depth argument exploit the absence of negations; Razborov showed matching has polynomial-size *non-monotone* circuits gap-wise, and monotone lower bounds are known not to transfer.
- **Natural proofs (Razborov–Rudich 1997).** Any lower-bound argument that is *constructive* and *large* on the property it uses would break pseudorandom function generators computable in $\mathsf{TC}^0 \subseteq \mathsf{NC}^1$. Switching-lemma and polynomial-approximation methods are natural, so they are provably blocked from reaching $\mathsf{NC}^1$ and beyond under standard hardness assumptions.
- **Relativization and algebrization** (Baker–Gill–Solovay; Aaronson–Wigderson 2009) rule out diagonalization-style arguments that treat $\mathsf{P}$ machines as black boxes.
- **Amplification traps.** Allender–Koucký (2010): a $n^{1+\varepsilon}$ size lower bound for certain self-reducible $\mathsf{NC}^1$-complete problems in $\mathsf{TC}^0$ would give super-polynomial bounds — so even tiny improvements are as hard as the full question.
- **Uniformity gives no leverage.** Unlike some space–time separations, no known diagonalization exploits DLOGTIME-uniformity to separate $\mathsf{NC}$ from $\mathsf{P}$.

## 6. The Gap

Everything proven lives in one of two boxes: (i) *restricted models* — monotone, constant-depth, bounded-width — where sequentiality is provable; (ii) *specific problems* pulled into $\mathsf{NC}$, which only shrinks the candidate set. Neither touches the general statement.

The precise missing step: exhibit an explicit $f \in \mathsf{P}$ and prove $\mathrm{CC}(\mathrm{KW}_f) = \omega(\log^k n)$ for all $k$, in a way that is not natural and does not relativize. The nearest concrete target is the **KRW conjecture** (Karchmer–Raz–Wigderson 1995): for $f:\{0,1\}^m\to\{0,1\}$ and $g:\{0,1\}^n\to\{0,1\}$,
$$\mathrm{depth}(f \diamond g) \;\approx\; \mathrm{depth}(f) + \mathrm{depth}(g),$$
where $f \diamond g$ is the block composition on $mn$ bits. Iterating $\log n / \log\log n$ times with $g$ of depth $\log\log n$ would yield a function in $\mathsf{P}$ of depth $\omega(\log n)$, hence $\mathsf{NC}^1 \neq \mathsf{P}$. That is still only the *first* level; ruling out all $\mathsf{NC}^i$ requires a genuinely new hierarchy-level argument.

## 7. Current Research (as of June 2026)

- **KRW program.** Dinur–Meir (2018) proved a composition theorem strong enough to re-derive cubic formula bounds via communication complexity. Mihajlin–Smal (2021) proposed the weaker XOR-KRW conjecture, which still implies $\mathsf{NC}^1 \neq \mathsf{P}$. Work continues at Weizmann (Meir), Technion, Steklov/St. Petersburg (Smal), and IAS.
- **Lifting theorems.** Query-to-communication lifting (Raz–McKenzie 1999; Göös–Pitassi–Watson; de Rezende–Meir–Nordström–Pitassi–Robere–Vinyals 2020) converts decision-tree bounds into monotone depth bounds and is the main engine behind recent monotone circuit and proof-complexity separations. Extending lifting past the monotone barrier is the live question. *(frontier — verify)*
- **Derandomizing matching.** Closing the quasi-$\mathsf{NC}$/$\mathsf{NC}$ gap for general perfect matching (Gurjar, Thierauf, Vazirani, Anari) — a positive result that would remove a long-standing candidate for $\mathsf{P} \setminus \mathsf{NC}$ (matching is not known $\mathsf{P}$-complete, so this does not settle the main question).
- **Fine-grained parallelism.** Conditional lower bounds on parallel depth for problems inside $\mathsf{P}$ under $\mathsf{P}$-completeness-style reductions, and depth-vs-work tradeoffs in the work-span model.
- **Meta-complexity.** MCSP and related problems used to bypass natural proofs (Hirahara, Santhanam, Oliveira); hardness magnification results occasionally claim near-threshold depth bounds. *(frontier — verify)*

## 8. Future Work

- Prove the XOR-KRW conjecture, or any composition theorem with additive depth for a non-trivial inner function of super-constant depth.
- Develop lifting gadgets that survive negations, transferring the $\Omega(n)$ monotone matching bound to general circuits.
- Find a non-natural invariant: a circuit-depth measure that is not large (holds for a sub-exponential fraction of functions), e.g. via algebraic geometry / GCT-style representation-theoretic obstructions applied to depth rather than size.
- Settle $\mathsf{NC}^1 \overset{?}{=} \mathsf{NC}^2$ or $\mathsf{NC} \overset{?}{=} \mathsf{SC}$ — either would be the first structural crack in the hierarchy.
- On the positive side: search for polylog-depth algorithms for $\mathsf{P}$-complete problems in *structured* instances (planar, bounded treewidth, bounded genus), mapping the exact frontier of parallelizability.

## 9. Key References

- **[Foundational]** Ladner, R. E. *The circuit value problem is log space complete for P.* SIGACT News 7(1), 18–20, 1975.
- **[Foundational]** Borodin, A. *On relating time and space to size and depth.* SIAM Journal on Computing 6(4), 733–744, 1977.
- **[Foundational]** Cook, S. A. *A taxonomy of problems with fast parallel algorithms.* Information and Control 64(1–3), 2–22, 1985.
- **[Foundational]** Barrington, D. A. M. *Bounded-width polynomial-size branching programs recognize exactly those languages in $NC^1$.* JCSS 38(1), 150–164, 1989.
- **[Foundational]** Csanky, L. *Fast parallel matrix inversion algorithms.* SIAM Journal on Computing 5(4), 618–623, 1976.
- **[Lower bounds]** Karchmer, M., Wigderson, A. *Monotone circuits for connectivity require super-logarithmic depth.* SIAM J. Discrete Mathematics 3(2), 255–265, 1990.
- **[Lower bounds]** Raz, R., Wigderson, A. *Monotone circuits for matching require linear depth.* Journal of the ACM 39(3), 736–744, 1992.
- **[Lower bounds]** Karchmer, M., Raz, R., Wigderson, A. *Super-logarithmic depth lower bounds via the direct sum in communication complexity.* Computational Complexity 5(3–4), 191–204, 1995.
- **[Lower bounds]** Håstad, J. *The shrinkage exponent of De Morgan formulas is 2.* SIAM Journal on Computing 27(1), 48–64, 1998.
- **[Barrier]** Razborov, A. A., Rudich, S. *Natural proofs.* Journal of Computer and System Sciences 55(1), 24–35, 1997.
- **[SOTA / Recent]** Fenner, S., Gurjar, R., Thierauf, T. *Bipartite perfect matching is in quasi-NC.* STOC 2016, 754–763.
- **[SOTA / Recent]** Svensson, O., Tarnawski, J. *The matching problem in general graphs is in quasi-NC.* FOCS 2017, 696–707.
- **[SOTA / Recent]** Anari, N., Vazirani, V. V. *Planar graph perfect matching is in NC.* Journal of the ACM 67(4), Article 21, 2020.
- **[SOTA / Recent]** Dinur, I., Meir, O. *Toward the KRW conjecture: cubic lower bounds via communication complexity.* Computational Complexity 27(3), 375–462, 2018.
- **[SOTA / Recent]** Mihajlin, I., Smal, A. *Toward better depth lower bounds: the XOR-KRW conjecture.* CCC 2021, LIPIcs vol. 200.
- **[Survey / Book]** Greenlaw, R., Hoover, H. J., Ruzzo, W. L. *Limits to Parallel Computation: P-Completeness Theory.* Oxford University Press, 1995.
- **[Survey / Book]** Vollmer, H. *Introduction to Circuit Complexity: A Uniform Approach.* Springer, 1999.
- **[Survey / Book]** Arora, S., Barak, B. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Ch. 6, 14).

## 10. Worked Example / Concrete Special Case

**The sequential chain.** Consider a "straight-line" circuit of $n$ gates where each gate feeds only the next:
$$y_0 = x_0, \qquad y_{i} = g_i(y_{i-1}, x_i) \quad (1 \le i \le n), \qquad \text{output } y_n .$$
Naively this has depth $n$. Whether it can be evaluated in depth $O(\log^k n)$ is exactly CVP restricted to a path, and the answer depends entirely on the algebra of the $g_i$.

**Case A — affine gates, in $\mathsf{NC}^1$.** Suppose each $g_i(y,x) = a_i y \oplus b_i$ over $\mathbb{F}_2$ with $a_i,b_i$ determined by $x_i$. Encode the state projectively:
$$\begin{pmatrix} y_i \\ 1\end{pmatrix} = M_i \begin{pmatrix} y_{i-1} \\ 1\end{pmatrix}, \qquad M_i = \begin{pmatrix} a_i & b_i \\ 0 & 1 \end{pmatrix} \in \mathbb{F}_2^{2\times 2}.$$
Then $y_n$ is read off from $M_n M_{n-1}\cdots M_1$. Matrix product is associative, so a balanced binary tree computes the product in $\lceil \log_2 n \rceil$ levels, each level being a constant-size $2\times 2$ multiplication over $\mathbb{F}_2$ (depth $\le 3$: four AND gates, two XOR gates in a tree). Total depth $\le 3\lceil\log_2 n\rceil + O(1)$, size $O(n)$. For $n = 2^{20} \approx 10^6$: depth $\approx 63$ instead of $10^6$ — a $16000\times$ speedup in parallel time.

**Case B — general gates, $\mathsf{P}$-complete.** Now let $g_i$ be arbitrary two-input gates and let the chain be a general DAG rather than a path. The state is no longer an element of a fixed finite monoid whose product can be precomputed obliviously; the "transfer function" of a sub-block of the circuit is an arbitrary Boolean function of its inputs, whose truth table can be exponentially large in the block's fan-in. Balanced-tree evaluation collapses because the composition of two blocks is not an $O(1)$-size object. This is precisely Ladner's CVP, and a polylog-depth algorithm for it would give $\mathsf{NC} = \mathsf{P}$.

**The dividing line.** Barrington's theorem says the associative-product trick is not a special case but the *whole* of $\mathsf{NC}^1$: any language in $\mathsf{NC}^1$ can be written as a product of $n^{O(1)}$ elements of $S_5$, each depending on one input bit. So "is CVP in $\mathsf{NC}^1$?" becomes "can $n$-step arbitrary Boolean composition be simulated by a $\text{poly}(n)$-length product over a fixed finite group?" No obstruction is known — and no construction either. That, in one sentence, is the $\mathsf{NC}$ vs $\mathsf{P}$ gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*