---
id: 10-theoretical-cs/p-versus-np-problem
title: "P versus NP Problem"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# P versus NP Problem

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/p-versus-np-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathrm{P}$ be the class of languages decided by a deterministic Turing machine in time $O(n^k)$ for some constant $k$, and $\mathrm{NP}$ the class decided by a nondeterministic Turing machine in polynomial time — equivalently, languages with polynomial-time-checkable certificates. The question:

$$\mathrm{P} \stackrel{?}{=} \mathrm{NP}.$$

The inclusion $\mathrm{P} \subseteq \mathrm{NP}$ is immediate. The open direction is whether every problem whose solutions can be *verified* quickly can also be *solved* quickly. A resolution requires either:

- a deterministic polynomial-time algorithm for one $\mathrm{NP}$-complete language (e.g. SAT), with a proof of correctness and of the polynomial time bound; or
- a proof that some language in $\mathrm{NP}$ has no deterministic $n^{O(1)}$-time algorithm — a superpolynomial lower bound for a *general* model of computation, not a restricted one.

The problem is one of the seven Clay Millennium Prize Problems (official statement by Stephen Cook, 2000). The consensus expectation is $\mathrm{P} \neq \mathrm{NP}$: in Gasarch's 2019 poll of researchers, 88% predicted $\mathrm{P} \neq \mathrm{NP}$.

## 2. Mathematical Foundations

**Model.** A multitape Turing machine $M$ over alphabet $\Sigma$. For $t : \mathbb{N} \to \mathbb{N}$, $\mathrm{DTIME}(t(n))$ is the class of $L \subseteq \Sigma^*$ decided by a deterministic $M$ halting within $O(t(n))$ steps on inputs of length $n$; $\mathrm{NTIME}(t(n))$ is the nondeterministic analogue. Then

$$\mathrm{P} = \bigcup_{k \ge 1} \mathrm{DTIME}(n^k), \qquad \mathrm{NP} = \bigcup_{k \ge 1} \mathrm{NTIME}(n^k).$$

**Certificate characterization.** $L \in \mathrm{NP}$ iff there exist a polynomial $p$ and $R \in \mathrm{P}$ with

$$x \in L \iff \exists\, y \in \Sigma^{\le p(|x|)} \ \text{such that} \ \langle x, y\rangle \in R .$$

**Reductions and completeness.** $A \le_m^p B$ if there is $f$ computable in polynomial time with $x \in A \iff f(x) \in B$. $B$ is $\mathrm{NP}$-hard if $A \le_m^p B$ for all $A \in \mathrm{NP}$, and $\mathrm{NP}$-complete if additionally $B \in \mathrm{NP}$. If any $\mathrm{NP}$-complete $B$ lies in $\mathrm{P}$, then $\mathrm{P} = \mathrm{NP}$.

**Cook–Levin Theorem (1971/1973).** SAT — satisfiability of a Boolean formula in conjunctive normal form — is $\mathrm{NP}$-complete. The proof encodes an accepting computation tableau of a nondeterministic machine as a CNF formula of size polynomial in $p(n)$, with clauses enforcing consistent cell contents, a valid start row, local transition legality (a $2\times 3$ window condition), and an accepting final row.

**Circuit form.** $\mathrm{P}/\mathrm{poly}$ is the class decided by families $\{C_n\}$ of Boolean circuits with $|C_n| \le n^{O(1)}$. Since $\mathrm{P} \subseteq \mathrm{P}/\mathrm{poly}$, proving $\mathrm{NP} \not\subseteq \mathrm{P}/\mathrm{poly}$ suffices for $\mathrm{P} \neq \mathrm{NP}$. Counting shows almost all Boolean functions on $n$ bits require circuits of size $\Theta(2^n/n)$ (Shannon 1949; Lupanov 1958), yet no explicit $\mathrm{NP}$ function is known to require superlinear size.

**Hierarchy theorems.** The deterministic time hierarchy theorem (Hartmanis–Stearns 1965) gives $\mathrm{DTIME}(t) \subsetneq \mathrm{DTIME}(t')$ when $t \log t = o(t')$ and $t'$ is time-constructible; hence $\mathrm{P} \subsetneq \mathrm{EXP}$. This yields separations only between models of the *same* type, not across determinism.

**Ladner's Theorem (1975).** If $\mathrm{P} \neq \mathrm{NP}$ then there exists $L \in \mathrm{NP} \setminus \mathrm{P}$ that is not $\mathrm{NP}$-complete (an "NP-intermediate" language), so the class does not collapse into two levels.

## 3. History & State of the Art (SOTA)

- **1956.** Gödel's letter to von Neumann asks whether a proof-search problem is solvable in $\sim Kn$ or $Kn^2$ steps — the earliest statement of the question (published Hartmanis 1989).
- **1965.** Hartmanis and Stearns found complexity theory with the time hierarchy theorem; Edmonds (1965) proposes polynomial time as the formal notion of "efficient".
- **1971.** Cook, *The complexity of theorem-proving procedures* (STOC), proves SAT complete; Levin (1973) independently gives six complete "universal search" problems.
- **1972.** Karp exhibits 21 $\mathrm{NP}$-complete problems (clique, vertex cover, Hamiltonian circuit, 3-SAT, subset sum, …), establishing the phenomenon's ubiquity. Garey and Johnson (1979) catalog several hundred.
- **1975.** Baker–Gill–Solovay: oracles $A, B$ with $\mathrm{P}^A = \mathrm{NP}^A$ and $\mathrm{P}^B \neq \mathrm{NP}^B$ — relativizing proofs cannot settle the question.
- **1980s.** Circuit lower bounds for restricted classes: Furst–Saxe–Sipser (1984) and Håstad's switching lemma (1986) give $2^{\Omega(n^{1/(d-1)})}$ bounds for $\mathrm{AC}^0$ parity; Razborov (1985) gives superpolynomial monotone circuit bounds for clique; Razborov–Smolensky (1987) handle $\mathrm{AC}^0[p]$ for prime $p$.
- **1994.** Razborov–Smolensky's success is bounded by Razborov–Rudich's **natural proofs** barrier.
- **2010.** Deolalikar's claimed proof of $\mathrm{P} \neq \mathrm{NP}$ is refuted within weeks by a public collaborative review (Immerman, Gowers, Lipton and others), primarily over the treatment of $\mathrm{XORSAT}$'s solution-space geometry.
- **2011.** Williams proves $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ via an algorithmic-method argument, the strongest unconditional non-uniform separation to date.

## 4. Partial Results / Verified Cases

- **Restricted circuit classes.** Parity $\notin \mathrm{AC}^0$: any depth-$d$ unbounded-fan-in AND/OR/NOT circuit computing $\oplus_n$ has size $2^{\Omega(n^{1/(d-1)})}$ (Håstad 1986). $\mathrm{MOD}_q \notin \mathrm{AC}^0[p]$ for distinct primes $p, q$ (Razborov 1987, Smolensky 1987). $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ (Williams 2011); strengthened to $\mathrm{NQP} \not\subseteq \mathrm{ACC}^0$ (Murray–Williams 2018).
- **Monotone circuits.** CLIQUE on $n$ vertices requires monotone circuits of size $2^{\Omega(\sqrt[4]{k})}$-type bounds (Razborov 1985; Alon–Boppana 1987). Does not transfer: Razborov (1985) showed matching, which is in $\mathrm{P}$, also needs superpolynomial monotone size.
- **General circuit size.** The best explicit lower bound for a function in $\mathrm{NP}$ over the basis $\{\wedge,\vee,\neg\}$ is $(3+1/86)n - o(n)$ (Find–Golovnev–Hirsch–Kulikov 2016), improving the long-standing $5n - o(n)$ bound of Iwama–Lachish–Morizumi–Raz over $U_2$. Still linear.
- **Time–space tradeoffs.** SAT cannot be solved by an algorithm running in time $n^{c}$ and space $n^{o(1)}$ for $c < 2\cos(\pi/7) \approx 1.8019$ (Williams 2008, building on Fortnow, Lipton, van Melkebeek, Viglas).
- **Provable separations.** $\mathrm{P} \subsetneq \mathrm{EXP}$, $\mathrm{NP} \subsetneq \mathrm{NEXP}$ (hierarchy theorems); $\mathrm{P} \ne \mathrm{NP}$ relative to a random oracle with probability 1 (Bennett–Gill 1981).
- **Tractable fragments.** Schaefer's dichotomy theorem (1978): every Boolean constraint satisfaction problem $\mathrm{SAT}(S)$ is in $\mathrm{P}$ or $\mathrm{NP}$-complete, and it is in $\mathrm{P}$ exactly when every relation in $S$ is 0-valid, 1-valid, bijunctive (2-SAT), Horn, dual-Horn, or affine. Bulatov (2017) and Zhuk (2017) extend the dichotomy to all finite domains. 2-SAT and Horn-SAT are linear-time; $k$-SAT for $k \ge 3$ is complete.
- **Parameterized islands.** Vertex cover of size $k$ is solvable in $O(1.2738^k + kn)$ time (Chen–Kanj–Xia 2010); by Courcelle's theorem, every MSO-definable property is linear-time on graphs of bounded treewidth.

## 5. Principal Obstacles

Three formal barriers rule out entire families of proof techniques.

1. **Relativization** (Baker–Gill–Solovay 1975). Diagonalization arguments that treat the machine as a black box hold relative to every oracle. Since $\mathrm{P}^A = \mathrm{NP}^A$ and $\mathrm{P}^B \neq \mathrm{NP}^B$ for suitable $A, B$, no such argument can decide the question. This kills the direct simulation/diagonalization route inherited from the hierarchy theorems.
2. **Natural proofs** (Razborov–Rudich 1994). Almost all known circuit lower bounds proceed via a property $\mathcal{C}$ of Boolean truth tables that is (i) *constructive* — decidable in time $2^{O(n)}$ in the truth table length — and (ii) *large* — holding for a $\ge 2^{-O(n)}$ fraction of all functions. If such a $\mathcal{C}$ separated $\mathrm{NP}$ from $\mathrm{P}/\mathrm{poly}$, it would break every pseudorandom function generator of subexponential hardness, contradicting the standard hardness assumptions (e.g. subexponentially hard factoring) that most of cryptography rests on. A working proof must be non-constructive or non-large.
3. **Algebrization** (Aaronson–Wigderson 2008). Interactive-proof techniques (arithmetization: $\mathrm{IP} = \mathrm{PSPACE}$, $\mathrm{MIP} = \mathrm{NEXP}$) escape relativization but respect low-degree extensions of oracles. Extending each oracle $A$ to a polynomial $\tilde{A}$ over a field, one gets $\mathrm{P}^A = \mathrm{NP}^{\tilde{A}}$-type collapses and separations, so arithmetization alone also fails.

Beyond the barriers: geometric complexity theory (Mulmuley–Sohoni) requires representation-theoretic multiplicity results that have proven far harder than anticipated — Bürgisser–Ikenmeyer–Panova (2019) showed the originally proposed *occurrence obstructions* do not exist, invalidating the program's first concrete plan. And no technique currently distinguishes an $\mathrm{NP}$-complete function from a random function in a way that survives the largeness condition.

## 6. The Gap

Proven: superpolynomial lower bounds hold for circuits that are *constant-depth*, *monotone*, or *depth-limited with modular gates*, and for the *uniform* class $\mathrm{NEXP}$ against $\mathrm{ACC}^0$. Needed: a superpolynomial lower bound for *unrestricted* fan-in-2 circuits of *arbitrary* depth against a language in $\mathrm{NP}$.

Quantitatively the gap is stark: current explicit general lower bound $\approx 3.011n$; required $n^{\omega(1)}$. Even $n^{1+\varepsilon}$ for any explicit $\mathrm{NP}$ function is open. The step to be crossed is a technique that certifies hardness of a *specific* function without giving an efficient test that a *random* function is hard — the exact combination the natural-proofs barrier forbids and that Williams' algorithmic method partially achieves (it is non-naturalizing) but only at exponential-time scales.

## 7. Current Research (as of June 2026)

- **The algorithmic method.** Williams' program: any nontrivial ($2^n/n^{\omega(1)}$-time) satisfiability algorithm for a circuit class $\mathcal{C}$ yields lower bounds against $\mathcal{C}$. Chen, Lyu, Williams, Ren and coauthors have extended it to almost-everywhere and average-case bounds, and to $\mathrm{NP}$-level (rather than $\mathrm{NEXP}$-level) hard functions in restricted settings. *(frontier — verify)*
- **Meta-complexity.** The complexity of MCSP (Minimum Circuit Size Problem) and time-bounded Kolmogorov complexity $\mathrm{K}^t$ has become the most active line: Hirahara's worst-case-to-average-case reductions for $\mathrm{NP}$ under $\mathrm{K}^t$-style measures, and Liu–Pass's equivalence between one-way functions and mild average-case hardness of $\mathrm{K}^t$. Groups: MIT (Williams), Simons Institute, NII Tokyo (Hirahara), Cornell (Pass), Oxford (Santhanam, Oliveira). *(frontier — verify)*
- **Geometric complexity theory.** Post-2019 the focus shifted from occurrence obstructions to multiplicity obstructions and to the border-rank/degeneration theory of the determinant–permanent problem (Landsberg, Ikenmeyer, Panova, Bläser).
- **Proof complexity.** Lower bounds for strong proof systems (Frege, extended Frege) as a route to $\mathrm{NP} \ne \mathrm{coNP}$; connections to bounded arithmetic and to the (in)dependence of $\mathrm{P}$ vs $\mathrm{NP}$ from weak theories.
- **Fine-grained complexity.** SETH-based conditional lower bounds (Impagliazzo–Paturi; Williams, Vassilevska Williams) map the internal structure of $\mathrm{P}$ and $\mathrm{NP}$ while unconditional bounds stall.

## 8. Future Work

- Push the algorithmic method downward: obtain a nontrivial CircuitSAT algorithm for general fan-in-2 circuits of size $cn$, which would give superlinear bounds for $\mathrm{NP}$ (Williams' explicitly stated goal).
- Prove unconditional hardness of MCSP or gap-MCSP; Kabanets–Cai (2000) and Hirahara's later work show this would have immediate consequences for lower bounds and for the natural-proofs barrier itself.
- Find a non-naturalizing hardness magnification threshold: Oliveira–Santhanam and Chen–Jin–Williams show tiny lower bounds (e.g. $n^{1+\varepsilon}$ size for a sparse variant of MCSP) would magnify into $\mathrm{NP} \not\subseteq \mathrm{P}/\mathrm{poly}$ — locating the magnification frontier just beyond current techniques.
- Complete the representation-theoretic input to GCT: positivity of Kronecker and plethysm coefficients, still open in the required generality.
- Determine the independence question: whether $\mathrm{P}$ vs $\mathrm{NP}$ is provable in fragments such as $\mathrm{PV}_1$ or $S^1_2$ (Razborov's program on the unprovability of circuit lower bounds).

## 9. Key References

- **[Foundational]** Stephen A. Cook. *The Complexity of Theorem-Proving Procedures.* Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC), 151–158, 1971.
- **[Foundational]** Leonid A. Levin. *Universal Sequential Search Problems.* Problems of Information Transmission 9(3), 265–266, 1973.
- **[Foundational]** Richard M. Karp. *Reducibility Among Combinatorial Problems.* In *Complexity of Computer Computations*, Plenum Press, 85–103, 1972.
- **[Foundational]** Michael R. Garey and David S. Johnson. *Computers and Intractability: A Guide to the Theory of NP-Completeness.* W. H. Freeman, 1979.
- **[Barrier]** Theodore Baker, John Gill, Robert Solovay. *Relativizations of the P =? NP Question.* SIAM Journal on Computing 4(4), 431–442, 1975.
- **[Barrier]** Alexander A. Razborov and Steven Rudich. *Natural Proofs.* Journal of Computer and System Sciences 55(1), 24–35, 1997 (STOC 1994).
- **[Barrier]** Scott Aaronson and Avi Wigderson. *Algebrization: A New Barrier in Complexity Theory.* ACM Transactions on Computation Theory 1(1), 2009.
- **[SOTA / Recent]** Ryan Williams. *Non-Uniform ACC Circuit Lower Bounds.* Journal of the ACM 61(1), Article 2, 2014 (CCC 2011).
- **[SOTA / Recent]** Cody D. Murray and R. Ryan Williams. *Circuit Lower Bounds for Nondeterministic Quasi-Polytime.* STOC 2018, 890–901.
- **[SOTA / Recent]** Peter Bürgisser, Christian Ikenmeyer, Greta Panova. *No Occurrence Obstructions in Geometric Complexity Theory.* Journal of the AMS 32, 163–193, 2019.
- **[SOTA / Recent]** Magnus Gausdal Find, Alexander Golovnev, Edward A. Hirsch, Alexander S. Kulikov. *A Better-Than-3n Lower Bound for the Circuit Complexity of an Explicit Function.* FOCS 2016, 89–98.
- **[Survey]** Stephen Cook. *The P versus NP Problem.* Official Clay Mathematics Institute Millennium Problem description, 2000.
- **[Survey]** Lance Fortnow. *The Status of the P versus NP Problem.* Communications of the ACM 52(9), 78–86, 2009.
- **[Survey]** Avi Wigderson. *Mathematics and Computation: A Theory Revolutionizing Technology and Science.* Princeton University Press, 2019.
- **[Survey]** Sanjeev Arora and Boaz Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009.
- **[Survey]** William Gasarch. *Guest Column: The Third P =? NP Poll.* ACM SIGACT News 50(1), 38–59, 2019.

## 10. Worked Example / Concrete Special Case

**Reducing 3-SAT to Independent Set, and why it does not help.**

Take the formula
$$\varphi = (x_1 \vee \neg x_2 \vee x_3) \wedge (\neg x_1 \vee x_2 \vee x_3) \wedge (x_1 \vee x_2 \vee \neg x_3).$$

Build a graph $G_\varphi$: one triangle per clause, its three vertices labelled by the literals; add an edge between any two vertices carrying complementary literals.

- Vertices: $\{x_1, \neg x_2, x_3\}$, $\{\neg x_1, x_2, x_3\}$, $\{x_1, x_2, \neg x_3\}$ — 9 total.
- Triangle edges: 9. Conflict edges: $x_1 \!-\! \neg x_1$ (2 pairs), $x_2 \!-\! \neg x_2$ (2 pairs), $x_3 \!-\! \neg x_3$ (2 pairs) — 6.

Claim: $\varphi$ is satisfiable iff $G_\varphi$ has an independent set of size $k = 3$ (the number of clauses). An independent set of size 3 picks exactly one vertex per triangle (triangles are cliques) and never two complementary literals (conflict edges), so setting the chosen literals true is consistent and satisfies every clause. Conversely, a satisfying assignment picks one true literal per clause.

Check: $x_1 = \mathrm{T}, x_2 = \mathrm{T}, x_3 = \mathrm{T}$ satisfies $\varphi$. The corresponding independent set is $\{x_1 \text{ (clause 1)}, x_2 \text{ (clause 2)}, x_1 \text{ (clause 3)}\}$ — pick the vertex $x_1$ in triangle 1, $x_2$ in triangle 2, $x_1$ in triangle 3. These three vertices lie in distinct triangles and no two are complementary, so they form an independent set of size 3.

The construction runs in time $O(m)$ for $m$ clauses, so $\mathrm{3\text{-}SAT} \le_m^p \mathrm{IS}$, and $\mathrm{IS} \in \mathrm{P}$ would give $\mathrm{P} = \mathrm{NP}$.

**Where the difficulty sits.** Verification is trivial: given the 3 vertices, check $\binom{3}{2} = 3$ pairs against the edge set — $O(k^2)$ time. Search is not: brute force scans $\binom{3m}{k}$ subsets, and for general $m$ the best known exact algorithm for maximum independent set runs in $O(1.1996^n)$ time (Xiao–Nagamochi 2017) — exponential. Any *proof* that no polynomial algorithm exists must lower-bound circuit size for the language $\{\langle G, k\rangle : \alpha(G) \ge k\}$. The best such bound available today is roughly $3.011 n$ gates, i.e. barely more than the number of input bits — a gap of $n^{\omega(1)}$ versus $O(n)$ that no known method narrows.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*