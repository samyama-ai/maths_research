---
id: 10-theoretical-cs/bpp-versus-p
title: "BPP versus P"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# BPP versus P

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/bpp-versus-p` · **Status:** open

## 1. Problem Statement / Conjecture

Is every decision problem solvable in polynomial time by a randomized algorithm with two-sided bounded error also solvable in deterministic polynomial time? Formally, does $\mathsf{BPP} = \mathsf{P}$?

$\mathsf{P} \subseteq \mathsf{BPP}$ is immediate (ignore the coins). The open direction is $\mathsf{BPP} \subseteq \mathsf{P}$.

- A **proof** requires a deterministic polynomial-time simulation of every bounded-error probabilistic polynomial-time machine — equivalently (by standard arguments), a polynomial-time computable pseudorandom generator or hitting-set generator fooling all polynomial-size circuits.
- A **disproof** requires exhibiting a language $L \in \mathsf{BPP} \setminus \mathsf{P}$. This is strictly harder than it looks: $\mathsf{BPP} \neq \mathsf{P}$ implies $\mathsf{P} \neq \mathsf{PSPACE}$, so a disproof would settle a long-standing separation.

The community consensus is that $\mathsf{BPP} = \mathsf{P}$, i.e. randomness does not buy polynomial-time power. The status is **open**, but conditionally settled under plausible circuit lower bounds.

## 2. Mathematical Foundations

**Probabilistic Turing machines.** A PTM $M$ has, on input $x$ with $|x|=n$, access to a random string $r \in \{0,1\}^{p(n)}$ for a polynomial $p$. Define $L \in \mathsf{BPP}$ iff there is a polynomial-time $M$ and polynomial $p$ with

$$x \in L \implies \Pr_{r \sim U_{p(n)}}[M(x,r)=1] \geq \tfrac{2}{3}, \qquad x \notin L \implies \Pr_{r}[M(x,r)=1] \leq \tfrac{1}{3}.$$

**Error amplification.** By Chernoff, running $k$ independent trials and taking the majority reduces error to $2^{-\Omega(k)}$; the constants $2/3, 1/3$ may be replaced by $\tfrac12 + n^{-c}$ and $1 - 2^{-n^c}$ respectively without changing the class. Related classes: $\mathsf{RP}$ (one-sided error), $\mathsf{ZPP} = \mathsf{RP} \cap \mathsf{coRP}$ (zero error, expected polynomial time).

**Pseudorandom generators.** $G = \{G_n : \{0,1\}^{s(n)} \to \{0,1\}^{n}\}$ is a PRG fooling size-$m$ circuits with error $\varepsilon$ if for every circuit $C$ of size $m$ on $n$ inputs,

$$\Big| \Pr_{y \sim U_{s(n)}}[C(G_n(y))=1] - \Pr_{z \sim U_n}[C(z)=1] \Big| \leq \varepsilon .$$

If such a $G$ is computable in time $2^{O(s(n))}$ with $s(n) = O(\log n)$, $m = n$, $\varepsilon = 1/10$, then enumerating all $2^{s(n)} = \mathrm{poly}(n)$ seeds and taking the majority derandomizes any BPP machine: $\mathsf{BPP} = \mathsf{P}$.

**Hardness measure.** For $f : \{0,1\}^n \to \{0,1\}$, the *average-case hardness* $H(f)$ is the largest $m$ such that every circuit $C$ of size $m$ satisfies $\Pr_x[C(x)=f(x)] \le \tfrac12 + \tfrac1m$. The Nisan–Wigderson construction converts a function of hardness $H$ into a PRG with seed length $s = O(\log^2 n / \log H)$ using a combinatorial design $S_1,\dots,S_n \subseteq [s]$ with $|S_i| = \ell$ and $|S_i \cap S_j| \le \log n$:

$$\mathrm{NW}^f(y) = f(y|_{S_1}),\, f(y|_{S_2}),\, \dots,\, f(y|_{S_n}).$$

**Main conditional theorem (Impagliazzo–Wigderson 1997).** If there exists $f \in \mathsf{E} = \mathsf{DTIME}(2^{O(n)})$ and $\delta>0$ such that every circuit computing $f_n$ has size $\ge 2^{\delta n}$ for all large $n$, then $\mathsf{P} = \mathsf{BPP}$. The proof combines worst-case-to-average-case hardness amplification (Yao's XOR lemma, derandomized) with the NW generator.

**Structural facts.**
$$\mathsf{BPP} \subseteq \mathsf{P/poly} \quad (\text{Adleman 1978}), \qquad \mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p \quad (\text{Sipser–Gács–Lautemann 1983}).$$
$\mathsf{BPP}$ is closed under complement and union, is low for itself ($\mathsf{BPP}^{\mathsf{BPP}} = \mathsf{BPP}$), and has **no known complete problem** and no known time hierarchy theorem, since it is a *semantic* class (the promise on the acceptance probability is not syntactically checkable).

## 3. History & State of the Art (SOTA)

- **1977.** John Gill defines $\mathsf{BPP}$, $\mathsf{RP}$, $\mathsf{ZPP}$ and their basic closure properties.
- **1977–1980.** Solovay–Strassen and Miller–Rabin primality tests, and Schwartz–Zippel identity testing, make randomness look genuinely powerful: several natural problems had randomized but no deterministic polynomial-time algorithm.
- **1978.** Adleman: $\mathsf{BPP} \subseteq \mathsf{P/poly}$ — randomness can be replaced by nonuniform advice.
- **1982–1984.** Yao, then Blum–Micali, introduce the cryptographic hardness-to-pseudorandomness paradigm; Yao shows subexponentially strong one-way functions put $\mathsf{BPP}$ in subexponential deterministic time.
- **1983.** Sipser, Gács, Lautemann: $\mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$, so $\mathsf{BPP}$ collapses if $\mathsf{PH}$ does.
- **1994.** Nisan–Wigderson: hardness against *circuits* (not one-way functions) suffices; PRGs from any hard function in $\mathsf{E}$.
- **1997.** Impagliazzo–Wigderson: full high-end derandomization $\mathsf{E} \not\subseteq \mathsf{SIZE}(2^{o(n)}) \Rightarrow \mathsf{P} = \mathsf{BPP}$. This is the SOTA framing: the question becomes a circuit lower bound question.
- **2001–2004.** Impagliazzo–Wigderson (uniform assumption): either $\mathsf{BPP} = \mathsf{EXP}$ or $\mathsf{BPP}$ has subexponential deterministic simulations infinitely often on average. Kabanets–Impagliazzo: derandomization is *necessary*, not just sufficient — derandomizing polynomial identity testing implies $\mathsf{NEXP} \not\subseteq \mathsf{P/poly}$ or that the permanent has no polynomial-size arithmetic circuits.
- **2020–2023.** Doron–Moshkovitz–Oh–Zuckerman and Chen–Tell obtain *near-optimal* derandomization: under appropriate hardness, $\mathsf{BPTIME}(T) \subseteq \mathsf{DTIME}(T^{1+\varepsilon})$, removing the polynomial blow-up of NW-style arguments.

## 4. Partial Results / Verified Cases

- **Specific problems derandomized.** Primality: AKS (2004) gives a deterministic $\tilde{O}(\log^{7.5} n)$ algorithm, replacing Solovay–Strassen/Miller–Rabin. Undirected $s$–$t$ connectivity: Reingold (2008) puts $\mathsf{USTCON}$ in $\mathsf{L}$, giving $\mathsf{SL} = \mathsf{L}$. Polynomial factoring over $\mathbb{F}_q$ in fixed characteristic, and several approximate counting problems, have deterministic analogues.
- **Bounded-depth circuits.** Nisan (1991): explicit PRG fooling depth-$d$ size-$m$ circuits with seed $O(\log^{2d+6} m)$; hence $\mathsf{BP}\cdot\mathsf{AC}^0 \subseteq$ quasipolynomial-time deterministic. Extensions cover $\mathsf{AC}^0[\oplus]$ and low-degree $\mathbb{F}_2$ polynomials.
- **Space-bounded randomness.** Nisan (1992): PRG for $\mathsf{BPL}$ with seed $O(\log^2 n)$. Saks–Zhou (1999): $\mathsf{BPSPACE}(S) \subseteq \mathsf{DSPACE}(S^{3/2})$, so $\mathsf{BPL} \subseteq \mathsf{DSPACE}(\log^{1.5} n)$; improved constant-factor and pseudodistribution refinements by Hoza and co-authors (2019–2021). $\mathsf{BPL} = \mathsf{L}$ remains open, but is the closest analogue where unconditional progress exists.
- **Restricted identity testing.** Deterministic polynomial-time PIT is known for read-once oblivious ABPs (quasipolynomial), depth-3 circuits with bounded top fan-in (Dvir–Shpilka, Kayal–Saxena), and sparse polynomials — but not for general arithmetic circuits.
- **Weak unconditional simulations.** $\mathsf{BPP} \subseteq \Sigma_2^p \cap \Pi_2^p$ and $\mathsf{BPP} \subseteq \mathsf{P/poly}$ hold unconditionally; $\mathsf{MA} \subseteq \mathsf{S}_2^p$ (Russell–Sundaram, Canetti).

## 5. Principal Obstacles

- **Equivalence to circuit lower bounds.** Impagliazzo–Wigderson reduces $\mathsf{P}=\mathsf{BPP}$ to $\mathsf{E} \not\subseteq \mathsf{SIZE}(2^{o(n)})$. No superlinear lower bound is known for general circuits on any explicit function: the best is $(3+\tfrac{1}{86})n - o(n)$ (Find–Golovnev–Hirsch–Kulikov 2016). We are exponentially far from what is needed.
- **Kabanets–Impagliazzo converse.** Derandomization is not merely *aided* by lower bounds; it *implies* them. So any proof of $\mathsf{P}=\mathsf{BPP}$ must, en route, prove $\mathsf{NEXP} \not\subseteq \mathsf{P/poly}$ or an arithmetic lower bound on the permanent. There is no "cheap" route.
- **Natural proofs.** Razborov–Rudich: a combinatorial-property-based lower bound argument that is constructive and large cannot separate $\mathsf{P/poly}$ from $\mathsf{NP}$ if strong pseudorandom functions exist. The very hardness assumptions used to derandomize block the standard techniques for proving them.
- **Relativization and algebrization.** Baker–Gill–Solovay-style oracles separate $\mathsf{P}$ from $\mathsf{BPP}$ relative to a random oracle in some formulations, and Aaronson–Wigderson's algebrization barrier rules out algebraic-degree extensions of diagonalization for the relevant lower bounds.
- **Semantic class pathology.** $\mathsf{BPP}$ has no complete problem and no known hierarchy theorem, so one cannot pick a canonical hardest language and derandomize it; every derandomization argument must be uniform in the machine.
- **Amplification loses too much.** Classical NW-based arguments incur polynomial overhead ($T \mapsto T^{c}$), and worst-case-to-average-case amplification within $\mathsf{NP}$ is itself blocked by known barriers (Bogdanov–Trevisan).

## 6. The Gap

Proven: $\mathsf{P} = \mathsf{BPP}$ *conditional* on $\mathsf{E} \not\subseteq \mathsf{SIZE}(2^{o(n)})$ (or on weaker uniform variants, giving subexponential/infinitely-often simulations). Unconditional derandomization exists only for restricted models: constant depth, logspace, structured arithmetic circuits, and isolated problems like primality.

The missing step is a single unconditional statement: **exhibit an explicit function in $\mathsf{E}$ (or in $\mathsf{EXP}$, or in $\mathsf{NEXP}$) requiring circuits of size $2^{\Omega(n)}$**, or, alternatively, construct a polynomial-time hitting-set generator for general polynomial-size circuits by other means. Every known route to the second passes through the first. The gap is therefore not a technical lemma but the entire unsolved theory of general Boolean circuit lower bounds — currently stuck between $3n$ and $2^{\Omega(n)}$.

## 7. Current Research (as of June 2026)

- **Non-black-box and instance-wise derandomization.** Chen and Tell (FOCS 2021) bypass the classical PRG framework: instead of fooling all circuits, they derandomize a specific computation using its own structure, obtaining $\mathsf{BPTIME}(T) \subseteq \mathsf{DTIME}(T^{1+\varepsilon})$ from *uniform* hardness assumptions about $\mathsf{DTIME}(2^{kn})$. This is the most active line; groups at Simons/UC Berkeley, Tel Aviv (Tell), and Tsinghua IIIS (Chen) drive it.
- **Superfast derandomization of proof systems.** Chen–Tell (STOC 2023) and follow-ups derandomize $\mathsf{AM}$ and interactive protocols with near-linear overhead under nondeterministic hardness. *(frontier — verify)*
- **Derandomization ↔ refutation / meta-complexity.** Connections between derandomization, MCSP, and time-bounded Kolmogorov complexity (Hirahara, Liu–Pass, Ren) are reframing hardness-vs-randomness in terms of the complexity of compressibility. *(frontier — verify)*
- **Space-bounded derandomization.** The $\mathsf{BPL}$ vs $\mathsf{L}$ programme (Hoza, Pyne, Umans, Cohen–Doron–Renard–Sberlo–Ta-Shma) uses weighted pseudorandom generators and spectral techniques; several recent results push toward $\mathsf{BPL} \subseteq \mathsf{DSPACE}(\log^{1+\varepsilon} n)$ for restricted branching programs. *(frontier — verify)*
- **Arithmetic PIT.** Bootstrapping results (Agrawal–Ghosh–Saxena 2019) show that even mildly nontrivial deterministic PIT for constant-variate low-degree circuits implies quasipolynomial-time PIT in general — a rare "sharp threshold" phenomenon.

## 8. Future Work

- Prove $\mathsf{NEXP} \not\subseteq \mathsf{P/poly}$, or extend Williams' algorithmic method (which gave $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$) to larger circuit classes; Williams explicitly frames faster-than-brute-force satisfiability algorithms as the lever.
- Obtain unconditional deterministic polynomial-time PIT for depth-4 or read-$k$ arithmetic circuits, which by bootstrapping would cascade upward.
- Settle $\mathsf{BPL} = \mathsf{L}$ as a proving ground for the time-bounded question.
- Develop the non-black-box paradigm further, aiming at derandomization from assumptions that provably evade natural proofs.
- Goldreich's programme: study the structural consequences of $\mathsf{P}=\mathsf{BPP}$ (on cryptography, property testing, sublinear algorithms) to identify which consequences might be independently refutable, giving a route to disproof.

## 9. Key References

- **[Foundational]** John Gill. *Computational Complexity of Probabilistic Turing Machines.* SIAM Journal on Computing 6(4), 1977.
- **[Foundational]** Leonard Adleman. *Two Theorems on Random Polynomial Time.* FOCS, 1978.
- **[Foundational]** Clemens Lautemann. *BPP and the Polynomial Hierarchy.* Information Processing Letters 17(4), 1983.
- **[Foundational]** Noam Nisan, Avi Wigderson. *Hardness vs Randomness.* Journal of Computer and System Sciences 49(2), 1994.
- **[Foundational]** Russell Impagliazzo, Avi Wigderson. *P = BPP if E Requires Exponential Circuits: Derandomizing the XOR Lemma.* STOC, 1997.
- **[Foundational]** Russell Impagliazzo, Avi Wigderson. *Randomness vs Time: Derandomization under a Uniform Assumption.* Journal of Computer and System Sciences 63(4), 2001.
- **[Foundational]** Valentine Kabanets, Russell Impagliazzo. *Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds.* Computational Complexity 13(1–2), 2004.
- **[Foundational]** Alexander Razborov, Steven Rudich. *Natural Proofs.* Journal of Computer and System Sciences 55(1), 1997.
- **[SOTA / Recent]** Lijie Chen, Roei Tell. *Hardness vs Randomness, Revisited: Uniform, Non-Black-Box, and Instance-Wise.* FOCS, 2021.
- **[SOTA / Recent]** Dean Doron, Dana Moshkovitz, Justin Oh, David Zuckerman. *Nearly Optimal Pseudorandomness from Hardness.* Journal of the ACM 69(6), 2022 (FOCS 2020).
- **[SOTA / Recent]** Ryan Williams. *Nonuniform ACC Circuit Lower Bounds.* Journal of the ACM 61(1), 2014.
- **[SOTA / Recent]** Manindra Agrawal, Neeraj Kayal, Nitin Saxena. *PRIMES is in P.* Annals of Mathematics 160(2), 2004.
- **[SOTA / Recent]** Omer Reingold. *Undirected Connectivity in Log-Space.* Journal of the ACM 55(4), 2008.
- **[Survey]** Salil Vadhan. *Pseudorandomness.* Foundations and Trends in Theoretical Computer Science 7(1–3), 2012.
- **[Survey]** Oded Goldreich. *In a World of P=BPP.* In *Studies in Complexity and Cryptography*, LNCS 6650, Springer, 2011.
- **[Survey]** Sanjeev Arora, Boaz Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapters 7, 20).

## 10. Worked Example / Concrete Special Case

**Bipartite perfect matching via the Tutte/Edmonds matrix** — a textbook $\mathsf{RP}$ algorithm whose derandomization is exactly the PIT problem.

Let $G$ be bipartite with parts $\{u_1,u_2,u_3\}$, $\{v_1,v_2,v_3\}$ and edges $u_1v_1, u_1v_2, u_2v_2, u_2v_3, u_3v_1$. Form the symbolic matrix $A$ with $A_{ij} = x_{ij}$ if $u_iv_j \in E$, else $0$:

$$A = \begin{pmatrix} x_{11} & x_{12} & 0 \\ 0 & x_{22} & x_{23} \\ x_{31} & 0 & 0 \end{pmatrix}, \qquad \det A = x_{31}\,(x_{12}x_{23} - 0\cdot x_{22}) = x_{31}x_{12}x_{23}.$$

Each monomial of $\det A$ corresponds to a perfect matching, so (Edmonds' theorem) $G$ has a perfect matching iff $\det A \not\equiv 0$. Here the single monomial $x_{31}x_{12}x_{23}$ certifies the matching $\{u_3v_1, u_1v_2, u_2v_3\}$.

**The randomized test.** Expanding $\det A$ symbolically costs up to $n!$ terms. Instead pick a prime $q$ and sample $a_{ij} \in \mathbb{F}_q$ uniformly, then evaluate $\det A(a)$ by Gaussian elimination in $O(n^3)$ field operations. By Schwartz–Zippel, since $\deg \det A = n$,

$$\Pr_{a \sim \mathbb{F}_q^{\,n^2}}\big[\det A(a) = 0 \mid \det A \not\equiv 0\big] \le \frac{n}{q}.$$

With $n=3$ and $q=101$ the false-negative probability is at most $3/101 < 0.03$; taking $q > 2n$ and repeating $k$ times gives error $2^{-\Omega(k)}$. Concretely, sampling $x_{11}=4, x_{12}=7, x_{22}=9, x_{23}=5, x_{31}=2$ over $\mathbb{F}_{101}$ gives $\det A = 2\cdot 7\cdot 5 = 70 \neq 0$: matching confirmed. Only the $3/101$ fraction of assignments with $x_{31}x_{12}x_{23} \equiv 0 \pmod{101}$ — those with one of the three variables zero — would mislead.

**Why this is the crux.** No deterministic polynomial-time algorithm is known for the general problem "is a given arithmetic circuit identically zero?", and by Kabanets–Impagliazzo any such algorithm would imply circuit lower bounds we cannot currently prove. (Bipartite matching itself *does* have a deterministic polynomial algorithm — Hopcroft–Karp — so this instance illustrates the phenomenon rather than witnessing $\mathsf{BPP} \neq \mathsf{P}$.) The general question $\mathsf{BPP} = \mathsf{P}$ asks whether every such lucky-sample argument can be replaced by a polynomially small, deterministically constructible set of test points.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*