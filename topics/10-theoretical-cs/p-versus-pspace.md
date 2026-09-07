---
id: 10-theoretical-cs/p-versus-pspace
title: "P versus PSPACE"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# P versus PSPACE

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/p-versus-pspace` · **Status:** open

## 1. Problem Statement / Conjecture

Is every decision problem solvable by a deterministic Turing machine in polynomial *space* also solvable in polynomial *time*?

$$\textbf{P} \stackrel{?}{=} \textbf{PSPACE}.$$

The containment $\textbf{P} \subseteq \textbf{PSPACE}$ is trivial (a machine running for $t$ steps touches at most $t$ cells). The conjecture is that the containment is strict: $\textbf{P} \subsetneq \textbf{PSPACE}$.

A complete resolution requires one of:

- **Separation.** Exhibit a language $L \in \textbf{PSPACE}$ and prove $L \notin \textbf{DTIME}(n^k)$ for every $k$. By completeness it suffices to prove that $\mathrm{TQBF}$ (true quantified Boolean formulas) has no polynomial-time algorithm.
- **Collapse.** Give a polynomial-time algorithm for $\mathrm{TQBF}$, i.e. a uniform algorithm evaluating an $n$-variable quantified formula in time $n^{O(1)}$.

A separation implies $\textbf{P} \neq \textbf{NP}$, so this problem is strictly harder than the Clay Millennium problem. A collapse would imply $\textbf{P} = \textbf{NP} = \textbf{PH} = \textbf{IP}$.

## 2. Mathematical Foundations

**Complexity classes.** For a function $s:\mathbb{N}\to\mathbb{N}$, let $\textbf{DSPACE}(s(n))$ be the languages decided by a deterministic Turing machine with a read-only input tape and a work tape using $O(s(n))$ cells. Then

$$\textbf{P}=\bigcup_{k\ge 1}\textbf{DTIME}(n^k),\qquad \textbf{PSPACE}=\bigcup_{k\ge 1}\textbf{DSPACE}(n^k).$$

**Known chain.**
$$\textbf{L}\subseteq\textbf{NL}\subseteq\textbf{P}\subseteq\textbf{NP}\subseteq\textbf{PH}\subseteq\textbf{PSPACE}\subseteq\textbf{EXP}.$$
Every inclusion from $\textbf{NL}$ to $\textbf{PSPACE}$ is open; at least one of $\textbf{P}\ne\textbf{NP}$, $\textbf{NP}\ne\textbf{PH}$, $\textbf{PH}\ne\textbf{PSPACE}$ must hold, since $\textbf{NL}\subsetneq\textbf{PSPACE}$.

**Space-bounded configuration counting.** A machine on input length $n$ with space $s(n)\ge\log n$ has at most $2^{O(s(n))}$ configurations, giving $\textbf{DSPACE}(s)\subseteq\textbf{DTIME}(2^{O(s)})$ and hence $\textbf{PSPACE}\subseteq\textbf{EXP}$.

**Savitch's theorem** (1970): $\textbf{NSPACE}(s(n))\subseteq\textbf{DSPACE}(s(n)^2)$ for $s(n)\ge\log n$, so $\textbf{NPSPACE}=\textbf{PSPACE}$. Space is therefore robust against nondeterminism, unlike time.

**Alternation** (Chandra–Kozen–Stockmeyer 1981): $\textbf{ATIME}(t)\subseteq\textbf{DSPACE}(t)\subseteq\textbf{ATIME}(t^2)$, so
$$\textbf{APTIME}=\textbf{PSPACE},\qquad \textbf{ASPACE}(\log n)=\textbf{P}.$$
Thus $\textbf{P}$ vs $\textbf{PSPACE}$ is exactly the question of whether alternating logspace equals alternating polynomial time — an unbounded-alternation game question.

**Canonical complete problem.** $\mathrm{TQBF}=\{\,\Phi = Q_1x_1\,Q_2x_2\cdots Q_nx_n\,\varphi(x_1,\dots,x_n) : \Phi \text{ true}\,\}$, $Q_i\in\{\exists,\forall\}$ and $\varphi$ a Boolean formula. $\mathrm{TQBF}$ is $\textbf{PSPACE}$-complete under logspace many-one reductions (Stockmeyer–Meyer 1973). So
$$\textbf{P}=\textbf{PSPACE}\iff \mathrm{TQBF}\in\textbf{P}.$$

**Space hierarchy theorem** (Stearns–Hartmanis–Lewis 1965): if $s_1(n)=o(s_2(n))$ and $s_2$ is space-constructible, $\textbf{DSPACE}(s_1)\subsetneq\textbf{DSPACE}(s_2)$. Time hierarchy (Hartmanis–Stearns 1965): $\textbf{DTIME}(t_1)\subsetneq\textbf{DTIME}(t_2)$ when $t_1\log t_1 = o(t_2)$.

**IP = PSPACE** (Lund–Fortnow–Karloff–Nisan and Shamir, 1992): $\textbf{PSPACE}$ equals the class with polynomial-time interactive proofs, via arithmetization of $\mathrm{TQBF}$ and Shamir's degree-reduction operator.

## 3. History & State of the Art (SOTA)

- **1965.** Hartmanis–Stearns and Stearns–Hartmanis–Lewis establish the time and space hierarchy theorems, the only unconditional separation machinery still in use.
- **1970.** Savitch proves $\textbf{NPSPACE}=\textbf{PSPACE}$.
- **1973.** Stockmeyer and Meyer show $\mathrm{TQBF}$ is $\textbf{PSPACE}$-complete and give the polynomial hierarchy; $\textbf{PSPACE}$ acquires a natural complete problem and a game semantics.
- **1975.** Baker–Gill–Solovay construct oracles $A,B$ with $\textbf{P}^A=\textbf{PSPACE}^A$ (take $A$ $\textbf{PSPACE}$-complete) and $\textbf{P}^B\neq\textbf{PSPACE}^B$: the relativization barrier.
- **1977.** Hopcroft–Paul–Valiant: $\textbf{DTIME}(t)\subseteq\textbf{DSPACE}(t/\log t)$ — space is strictly more powerful than time at matching bounds, but the gap is only logarithmic.
- **1981.** Chandra–Kozen–Stockmeyer recast the question as alternation.
- **1992.** $\textbf{IP}=\textbf{PSPACE}$: a non-relativizing technique, showing arithmetization escapes the 1975 barrier.
- **1997.** Razborov–Rudich: natural proofs cannot separate $\textbf{P}$ from $\textbf{NP}$ (hence not from $\textbf{PSPACE}$) if strong pseudorandom functions exist.
- **2009.** Aaronson–Wigderson: algebrization. Arithmetization plus relativization is still insufficient — separating $\textbf{P}$ from $\textbf{PSPACE}$ requires non-algebrizing techniques.
- **2025.** R. Williams, *Simulating time with square-root space*: $\textbf{DTIME}(t)\subseteq\textbf{DSPACE}(O(\sqrt{t\log t}))$, built on Cook–Mertz tree evaluation. Corollary via the space hierarchy: $\textbf{DSPACE}(s)\not\subseteq\textbf{DTIME}(s^{2-\varepsilon})$ — the first polynomial (rather than logarithmic) time lower bound for space-bounded computation.

## 4. Partial Results / Verified Cases

- **Fixed-degree separations.** For every fixed $k$, $\textbf{DTIME}(n^k)\subseteq\textbf{DSPACE}(n^k)\subsetneq\textbf{DSPACE}(n^{k+1})\subseteq\textbf{PSPACE}$, so $\textbf{PSPACE}\not\subseteq\textbf{DTIME}(n^k)$. The obstacle is only the union over all $k$.
- **Quadratic time lower bound (2025).** For space-constructible $s$ with $s(n)\ge\log n$ and any $\varepsilon>0$, $\textbf{DSPACE}(s)\not\subseteq\textbf{DTIME}(s^{2-\varepsilon})$ (Williams 2025).
- **Below P.** $\textbf{L}\subsetneq\textbf{PSPACE}$ and $\textbf{NL}\subsetneq\textbf{PSPACE}$, both by the space hierarchy plus Savitch. Likewise $\textbf{PSPACE}\subsetneq\textbf{EXPSPACE}$.
- **Nonuniform.** For every $k$, $\textbf{PSPACE}\not\subseteq\textbf{SIZE}(n^k)$ (counting plus a $\textbf{PSPACE}$ search for the lexicographically first hard function; cf. Kannan 1982, who proves the stronger $\Sigma_2^p\cap\Pi_2^p$ version). But whether $\textbf{PSPACE}\subseteq\textbf{P/poly}$ is open.
- **Restricted quantifier depth.** $\Sigma_k\mathrm{SAT}$, the fragment of $\mathrm{TQBF}$ with $k$ alternations, is $\Sigma_k^p$-complete; for constant $k$ these lie in $\textbf{PH}$, and no fixed level is known to escape $\textbf{P}$.
- **Restricted proof and circuit models.** Exponential lower bounds are known for Q-resolution and tree-like QBF calculi on $\mathrm{TQBF}$ families, for read-once branching programs, and for constant-depth circuits ($\mathrm{PARITY}\notin \textbf{AC}^0$, Håstad 1986). Nečiporuk's method gives $\Omega(n^2/\log^2 n)$ branching-program size for explicit functions — the best general bound, far below superpolynomial in a class-separating sense.
- **Relativized worlds.** Both $\textbf{P}^A=\textbf{PSPACE}^A$ and $\textbf{P}^B\neq\textbf{PSPACE}^B$ are realized (Baker–Gill–Solovay 1975); random oracles separate.
- **Games.** Concrete $\textbf{PSPACE}$-complete games (Generalized Geography, Go with Japanese ko rules, Sokoban, QBF-Gomoku) versus polynomial-time-solvable games (Nim, Undirected Geography) mark the empirical boundary.

## 5. Principal Obstacles

- **Relativization.** Any argument that treats the machine as a black box with an oracle proves nothing: an oracle world exists where the classes coincide (Baker–Gill–Solovay 1975). Diagonalization and simulation arguments — the tools behind the hierarchy theorems — relativize.
- **Algebrization.** The one known non-relativizing family (arithmetization, as in $\textbf{IP}=\textbf{PSPACE}$) is itself blocked. Aaronson–Wigderson (2009) construct oracles $A$ and low-degree extensions $\tilde A$ such that $\textbf{P}^{A}=\textbf{PSPACE}^{\tilde A}$, so any technique closed under algebraic extension of oracles cannot separate the classes.
- **Natural proofs.** A circuit-lower-bound route would very likely produce a property that is *constructive* and *large*; Razborov–Rudich (1997) show such a property breaks subexponentially secure pseudorandom functions, which are themselves computable in $\textbf{PSPACE}$-friendly models. The route thus contradicts widely believed cryptographic hardness.
- **Weak general lower bounds.** No superlinear time lower bound is known for any $\textbf{NP}$ problem on a general-purpose machine model; the best explicit circuit lower bound is $(3+\varepsilon)n$ (Find–Golovnev–Hirsch–Kulikov 2016). Separating $\textbf{P}$ from $\textbf{PSPACE}$ demands a *superpolynomial* bound.
- **Space simulates time too well.** $\textbf{DTIME}(t)\subseteq\textbf{DSPACE}(\sqrt{t\log t})$ shows time-to-space compression is real and quantitatively strong; the reverse — space-to-time — resists because a space-$s$ machine's $2^{\Theta(s)}$ configuration graph has no known succinct reachability certificate.
- **No fine-grained handle.** Unlike $\textbf{P}$ vs $\textbf{NP}$, there is no widely accepted hardness hypothesis (SETH-analogue) whose refutation would give $\textbf{P}=\textbf{PSPACE}$, so conditional progress is scarce.

## 6. The Gap

Proven: for each fixed $k$, some $\textbf{PSPACE}$ language is outside $\textbf{DTIME}(n^k)$, and (2025) outside $\textbf{DTIME}(s^{2-\varepsilon})$ for space $s$. Required: a *single* language in $\textbf{PSPACE}$ outside $\bigcup_k \textbf{DTIME}(n^k)$.

The obstruction is quantifier order. The hierarchy theorems produce a diagonal language depending on the bound $k$ being diagonalized against; there is no known way to diagonalize against all polynomials while staying in polynomial space, because the diagonalizing machine must simulate machines of unbounded polynomial time within a fixed polynomial space budget. Concretely, the missing step is a superpolynomial *time* lower bound for $\mathrm{TQBF}$ on multitape Turing machines (or, equivalently up to uniformity, a superpolynomial circuit lower bound for $\mathrm{TQBF}$), by a technique that neither relativizes, nor algebrizes, nor yields a natural property.

## 7. Current Research (as of June 2026)

- **Catalytic and tree-evaluation space.** Cook–Mertz's $O(\log n\cdot\log\log n)$-space tree evaluation algorithm (2024) and Williams' $\sqrt{t\log t}$ simulation (STOC 2025) drive an active program at MIT, Toronto, and DIMACS on space-efficient simulation; several groups are trying to push to $\textbf{DTIME}(t)\subseteq\textbf{DSPACE}(t^{1/2-\delta})$ or to prove it impossible. A tight version would give $\textbf{P}\ne\textbf{PSPACE}$-adjacent consequences such as $\textbf{P}\ne\textbf{PSPACE}$ only under further strengthening *(frontier — verify)*.
- **Algorithmic method.** Williams' framework (nontrivial satisfiability algorithms $\Rightarrow$ circuit lower bounds), which yielded $\textbf{NEXP}\not\subseteq\textbf{ACC}^0$, is being aimed at $\textbf{PSPACE}$-level classes; the method is non-naturalizing but so far reaches only nonuniform classes above $\textbf{NEXP}$.
- **Meta-complexity.** MCSP/MKTP-based approaches (Hirahara, Allender, Santhanam) connect learning, one-way functions, and lower bounds, and are structurally exempt from natural proofs.
- **Proof complexity for QBF.** Lower bounds for QBF calculi (Beyersdorff, Bonacina, Nordström) chart the limits of practical QBF solvers and give unconditional bounds in restricted models.
- **Barrier cartography.** Work on non-algebrizing techniques and on "ironic complexity" (Aaronson) asks which known non-barriered tools remain.

## 8. Future Work

- Prove or refute $\textbf{PSPACE}\subseteq\textbf{P/poly}$; a refutation would be the first superpolynomial lower bound against a $\textbf{PSPACE}$-complete problem.
- Settle the weaker $\textbf{PH}\ne\textbf{PSPACE}$, which follows if $\textbf{PSPACE}$-completeness cannot be matched inside $\textbf{PH}$ (since $\textbf{PH}=\textbf{PSPACE}$ forces $\textbf{PH}$ to collapse).
- Improve time-space tradeoffs: any proof that $\mathrm{SAT}\notin\textbf{TISP}(n^{1+\varepsilon},n^{o(1)})$ beyond the current $n^{2\cos(\pi/7)-o(1)}\approx n^{1.801}$ bound (Williams; Fortnow–Lipton–van Melkebeek–Viglas) tightens the picture.
- Find a natural non-algebrizing tool. $\textbf{IP}=\textbf{PSPACE}$ shows one exists at the level of interaction; the search is for its lower-bound analogue.
- Develop unconditional lower bounds in models strictly stronger than branching programs but weaker than general circuits, to break the $\Omega(n^2/\log^2 n)$ Nečiporuk ceiling.

## 9. Key References

- **[Foundational]** J. Hartmanis, R. E. Stearns. *On the Computational Complexity of Algorithms.* Transactions of the AMS 117, 1965.
- **[Foundational]** R. E. Stearns, J. Hartmanis, P. M. Lewis II. *Hierarchies of Memory Limited Computations.* IEEE Conf. on Switching Circuit Theory and Logical Design (SWAT), 1965.
- **[Foundational]** W. J. Savitch. *Relationships Between Nondeterministic and Deterministic Tape Complexities.* Journal of Computer and System Sciences 4(2), 1970.
- **[Foundational]** L. J. Stockmeyer, A. R. Meyer. *Word Problems Requiring Exponential Time.* STOC 1973.
- **[Foundational]** T. Baker, J. Gill, R. Solovay. *Relativizations of the P =? NP Question.* SIAM Journal on Computing 4(4), 1975.
- **[Foundational]** J. Hopcroft, W. Paul, L. Valiant. *On Time Versus Space.* Journal of the ACM 24(2), 1977.
- **[Foundational]** A. K. Chandra, D. C. Kozen, L. J. Stockmeyer. *Alternation.* Journal of the ACM 28(1), 1981.
- **[Foundational]** A. Shamir. *IP = PSPACE.* Journal of the ACM 39(4), 1992.
- **[Foundational]** C. Lund, L. Fortnow, H. Karloff, N. Nisan. *Algebraic Methods for Interactive Proof Systems.* Journal of the ACM 39(4), 1992.
- **[Barrier]** A. A. Razborov, S. Rudich. *Natural Proofs.* Journal of Computer and System Sciences 55(1), 1997.
- **[Barrier]** S. Aaronson, A. Wigderson. *Algebrization: A New Barrier in Complexity Theory.* ACM Transactions on Computation Theory 1(1), 2009.
- **[SOTA / Recent]** J. Cook, I. Mertz. *Tree Evaluation Is in Space $O(\log n \cdot \log\log n)$.* STOC 2024.
- **[SOTA / Recent]** R. Williams. *Simulating Time With Square-Root Space.* STOC 2025.
- **[SOTA / Recent]** R. Williams. *Nonuniform ACC Circuit Lower Bounds.* Journal of the ACM 61(1), 2014.
- **[Survey]** S. Arora, B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009.
- **[Survey]** C. H. Papadimitriou. *Computational Complexity.* Addison-Wesley, 1994.
- **[Survey]** L. Fortnow. *The Status of the P versus NP Problem.* Communications of the ACM 52(9), 2009.

## 10. Worked Example / Concrete Special Case

**Instance.** Take $n=3$ and
$$\Phi \;=\; \exists x\,\forall y\,\exists z\;\big[(x\vee y)\wedge(\neg y\vee z)\wedge(\neg x\vee\neg z)\big].$$

**Evaluation by the canonical PSPACE algorithm** (depth-first recursion over the quantifier prefix, reusing space):

- **Branch $x=1$.**
  - $y=0$: clauses become $(1)\wedge(1)\wedge(\neg z)$. Choose $z=0$: all clauses true. $\exists z$ succeeds.
  - $y=1$: clauses become $(1)\wedge(z)\wedge(\neg z)$. Both $z=0$ and $z=1$ fail. $\exists z$ fails, so $\forall y$ fails.
  - Branch $x=1$ is **false**.
- **Branch $x=0$.**
  - $y=0$: first clause $(x\vee y)=(0\vee 0)=0$. Fails for both $z$.
  - $\forall y$ fails immediately. Branch $x=0$ is **false**.

Hence $\Phi$ is **false**, so $\Phi\notin\mathrm{TQBF}$.

**Resource accounting.** The recursion tree has $2^3=8$ leaves and depth $3$. Each stack frame holds one bit (the current assignment to $x_i$) plus $O(\log n)$ bookkeeping, so total work space is $O(n\log n)$ bits beyond the read-only input — polynomial, in fact linear-ish. Running time is $\Theta(2^n\cdot|\varphi|)$, since a false $\forall$ branch may only be detected after exhausting the subtree.

**What the open problem asks.** For general $n$-variable $\Phi$ of size $m$, the algorithm above uses space $O(n\log n + m)$ and time $2^{\Theta(n)}$. $\textbf{P}=\textbf{PSPACE}$ would require an algorithm running in time $(n+m)^{O(1)}$ — i.e. one that *never* enumerates the game tree, instead computing the truth value from some polynomially sized certificate of the alternating game. No such certificate is known to exist, and none is known not to. Note the contrast with the $\exists$-only fragment: $\exists x\exists y\exists z\,\varphi$ is $\mathrm{SAT}$, still $2^{\Theta(n)}$ in the worst case but at least with an efficiently checkable witness; once $\forall$ alternates in, even *verifying* a claimed answer is $\textbf{PSPACE}$-hard, and only the interactive protocol of Shamir (1992) recovers efficient verification — using randomness and $n$ rounds of interaction rather than a static witness.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*