---
id: 10-theoretical-cs/np-versus-bqp
title: "NP versus BQP"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NP versus BQP

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/np-versus-bqp` · **Status:** open

## 1. Problem Statement / Conjecture

Is $\mathsf{NP} \subseteq \mathsf{BQP}$? Equivalently: can a quantum computer solve $\mathsf{NP}$-complete problems (e.g. 3-SAT) in polynomial time with bounded error?

The conjectured answer is **no**: $\mathsf{NP} \not\subseteq \mathsf{BQP}$, and moreover the two classes are incomparable, $\mathsf{BQP} \not\subseteq \mathsf{NP}$ as well.

A complete resolution requires either:

- **(a)** a bounded-error quantum polynomial-time algorithm for one $\mathsf{NP}$-complete language, or
- **(b)** a proof that no such algorithm exists.

Direction (b) implies $\mathsf{P} \neq \mathsf{NP}$ (since $\mathsf{P} \subseteq \mathsf{BQP}$), so it is strictly harder than the Millennium Prize problem. Direction (a) would not immediately settle $\mathsf{P}$ vs $\mathsf{NP}$, but would overturn post-quantum cryptography wholesale. Neither direction is achievable by any known relativizing or algebrizing technique.

## 2. Mathematical Foundations

**Quantum circuits.** A state on $n$ qubits is a unit vector in $\mathbb{C}^{2^n}$, $|\psi\rangle = \sum_{x \in \{0,1\}^n} \alpha_x |x\rangle$ with $\sum_x |\alpha_x|^2 = 1$. Gates are unitaries $U \in \mathrm{U}(2^n)$ acting on $O(1)$ qubits; measurement in the computational basis yields $x$ with probability $|\alpha_x|^2$.

**Definition ($\mathsf{BQP}$, Bernstein–Vazirani 1997).** $L \in \mathsf{BQP}$ iff there is a polynomial-time classical Turing machine outputting, on input $1^n$, a circuit $C_n$ over a fixed finite universal gate set with $|C_n| = \mathrm{poly}(n)$, such that for all $x \in \{0,1\}^n$,
$$\Pr[C_n(x) = [\,x \in L\,]] \ \geq\ 2/3 .$$
The constant $2/3$ is arbitrary in $(1/2, 1)$ by Chernoff amplification. The Solovay–Kitaev theorem makes the class independent of the universal gate set.

**Definition ($\mathsf{NP}$).** $L \in \mathsf{NP}$ iff there is a polynomial-time relation $R$ and $c$ with $x \in L \iff \exists w \in \{0,1\}^{|x|^c} : R(x,w)=1$.

**Known containments.**
$$\mathsf{P} \subseteq \mathsf{BPP} \subseteq \mathsf{BQP} \subseteq \mathsf{AWPP} \subseteq \mathsf{PP} \subseteq \mathsf{P}^{\\#\mathsf{P}} \subseteq \mathsf{PSPACE},$$
with $\mathsf{BQP} \subseteq \mathsf{PP}$ due to Adleman–DeMarrais–Huang (1997) and $\mathsf{BQP} \subseteq \mathsf{AWPP}$ to Fortnow–Rogers (1999). Also $\mathsf{NP} \subseteq \mathsf{PP}$, so both classes sit inside $\mathsf{PP}$ and no counting argument separates them.

**Self-lowness.** $\mathsf{BQP}^{\mathsf{BQP}} = \mathsf{BQP}$ (Bernstein–Vazirani), because bounded-error subroutines can be amplified and run coherently. Consequently
$$\mathsf{NP} \subseteq \mathsf{BQP} \implies \mathsf{PH} \subseteq \mathsf{BQP} \subseteq \mathsf{PP},$$
by induction on the levels $\Sigma_k^p \subseteq \mathsf{NP}^{\Sigma_{k-1}^p}$. So a quantum algorithm for SAT collapses the entire polynomial hierarchy into $\mathsf{PP}$ — a strong but not formally contradictory consequence.

**Query model.** For $f : \{0,1\}^N \to \{0,1\}$, the oracle unitary is $O_x : |i\rangle|b\rangle \mapsto |i\rangle|b \oplus x_i\rangle$. A $T$-query algorithm computes $U_T O_x U_{T-1} \cdots O_x U_0 |0\rangle$. Write $Q_2(f)$ for the bounded-error quantum query complexity. Two lower-bound engines: the **polynomial method** ($Q_2(f) \geq \deg_{1/3}(f)/2$, Beals–Buhrman–Cleve–Mosca–de Wolf 2001) and the **adversary method** (Ambainis 2002).

## 3. History & State of the Art (SOTA)

- **1993–97.** Bernstein and Vazirani define $\mathsf{BQP}$ and give the first superpolynomial black-box separation from $\mathsf{BPP}$ (recursive Fourier sampling).
- **1994/97.** Shor factors integers and computes discrete logarithms in $\mathsf{BQP}$ — problems in $\mathsf{NP} \cap \mathsf{coNP}$ believed outside $\mathsf{P}$. This established that $\mathsf{BQP}$ beats $\mathsf{BPP}$ on *structured* problems and set off speculation about $\mathsf{NP} \subseteq \mathsf{BQP}$.
- **1996.** Grover: unstructured search over $N$ items in $O(\sqrt{N})$ queries.
- **1997.** Bennett, Bernstein, Brassard and Vazirani prove the matching $\Omega(\sqrt{N})$ lower bound via a hybrid argument, giving an oracle $A$ with $\mathsf{NP}^A \not\subseteq \mathsf{BQP}^A$. This remains the central formal evidence against $\mathsf{NP} \subseteq \mathsf{BQP}$.
- **2004–07.** Aaronson–Shi ($\Omega(N^{1/3})$ for collision), Ambainis (element distinctness $\Theta(N^{2/3})$), Hallgren (Pell's equation in $\mathsf{BQP}$).
- **2009.** Aaronson–Wigderson: the *algebrization* barrier. Any resolution of $\mathsf{NP}$ vs $\mathsf{BQP}$ must be non-algebrizing.
- **2010–19.** Aaronson poses $\mathsf{BQP}$ vs $\mathsf{PH}$; Raz and Tal resolve it with the Forrelation-based oracle $A$ satisfying $\mathsf{BQP}^A \not\subseteq \mathsf{PH}^A$, hence $\mathsf{BQP}^A \not\subseteq \mathsf{NP}^A$. Together with BBBV, both non-containments hold relative to oracles.
- **2022.** Yamakawa–Zhandry: an $\mathsf{NP}$ *search* problem, defined relative to a random oracle plus a linear code, solvable in quantum polynomial time but classically hard — quantum advantage with verifiable answers and no algebraic structure.

## 4. Partial Results / Verified Cases

**Proven quantum speedups relevant to $\mathsf{NP}$ (all exponential-time, none polynomial):**

| Problem | Classical best | Quantum |
|---|---|---|
| Unstructured search, $N=2^n$ | $\Theta(N)$ | $\Theta(\sqrt N)$ (Grover; BBBV tight) |
| $k$-SAT, brute force | $2^n$ | $2^{n/2}$ |
| Backtracking / DPLL, tree size $T$ | $T$ | $\tilde O(\sqrt{T\,n})$ (Montanaro 2018) |
| TSP, degree-3 graphs | $O(1.657^n)$ | $O(1.301^n)$ (Moylett–Linden–Montanaro 2017) |
| Set cover / TSP by DP | $O^*(2^n)$ | $O^*(1.728^n)$ (Ambainis et al., SODA 2019) |
| Element distinctness | $\Theta(N)$ | $\Theta(N^{2/3})$ (Ambainis 2007) |

**Proven in $\mathsf{BQP}$, not $\mathsf{NP}$-hard:** factoring, discrete log, Pell's equation and principal ideal (Hallgren 2007), abelian hidden subgroup, dihedral HSP in $2^{O(\sqrt{\log N})}$ (Kuperberg 2005). $\mathsf{NP}$-completeness of these is ruled out unless $\mathsf{NP} = \mathsf{coNP}$ for the $\mathsf{NP}\cap\mathsf{coNP}$ ones.

**Oracle-relative resolutions.** $\exists A: \mathsf{NP}^A \not\subseteq \mathsf{BQP}^A$ (BBBV 1997), and relative to a *random* oracle this holds with probability 1. $\exists A: \mathsf{BQP}^A \not\subseteq \mathsf{PH}^A \supseteq \mathsf{NP}^A$ (Raz–Tal 2019). Also $\exists A: \mathsf{BQP}^A \subseteq \mathsf{P}^A$ trivially for $A = \emptyset$-like collapses under $\mathsf{PSPACE}$ oracles, showing the question is not settled by relativization in either direction.

## 5. Principal Obstacles

- **Relativization.** BBBV and Raz–Tal give oracles on both sides; any relativizing proof technique — diagonalization, simulation, standard query arguments — is provably insufficient.
- **Algebrization.** Aaronson–Wigderson extend the barrier to techniques that survive low-degree extension of the oracle, killing arithmetization-based approaches (the tool that gave $\mathsf{IP}=\mathsf{PSPACE}$).
- **Lower bounds require $\mathsf{P} \neq \mathsf{NP}$.** Proving $\mathsf{NP} \not\subseteq \mathsf{BQP}$ subsumes $\mathsf{P} \neq \mathsf{NP}$, so it inherits natural proofs (Razborov–Rudich) on top of the two barriers above.
- **No structural collapse to exploit.** $\mathsf{NP} \subseteq \mathsf{BQP}$ yields only $\mathsf{PH} \subseteq \mathsf{PP}$, which is not known to be false. Compare $\mathsf{NP} \subseteq \mathsf{BPP} \Rightarrow \mathsf{PH} = \Sigma_2^p$ — for $\mathsf{BQP}$ there is no analogous absurdity, because $\mathsf{BQP}$ has no known complete problem and is not known to have polynomial-size advice-based collapse structure.
- **Query lower bounds do not lift.** The $\sqrt{N}$ barrier is black-box. A SAT instance is not an opaque oracle: its clause structure is visible, and quantum algorithms could in principle exploit it, exactly as Shor exploits the group structure of $\mathbb{Z}_N^*$. No technique converts a query bound into a circuit bound.
- **Absence of a structural theory.** Aaronson–Ambainis (2014) formalize "quantum speedups need structure" as a conjecture about influences of bounded low-degree polynomials; it is itself open, so it cannot be used as a lemma.

## 6. The Gap

Proven: for the *unstructured* Boolean-hypercube search problem, $\Theta(\sqrt N)$ queries are necessary and sufficient, so $\mathsf{NP}^A \not\subseteq \mathsf{BQP}^A$ for generic $A$.

Wanted: the same conclusion for the *explicitly presented* language 3-SAT, where the verifier is a circuit given in the input rather than an oracle.

The gap is exactly the step from black-box to white-box. Every $\mathsf{NP}$ problem has a succinct description of its verifier; the quantum algorithm may read that description. Bridging requires a non-relativizing, non-algebrizing, non-naturalizing argument that succinct verifiers give no quantum leverage — precisely the kind of argument absent from all of complexity theory. Symmetrically, closing $\mathsf{BQP} \not\subseteq \mathsf{NP}$ requires showing some concrete $\mathsf{BQP}$ language has no short classical certificate, which would separate $\mathsf{BQP}$ from $\mathsf{NP}$ unconditionally and hence imply $\mathsf{P} \neq \mathsf{PSPACE}$-scale separations.

## 7. Current Research (as of June 2026)

- **Structure conjectures.** The Aaronson–Ambainis conjecture ($\text{Var}[p] \le \varepsilon \Rightarrow$ some variable has influence $\ge \mathrm{poly}(\varepsilon/\deg)$) remains the main program for formalizing "no speedup without structure"; partial results exist for low-degree and symmetric cases. *(frontier — verify)*
- **Structure-free advantage.** Follow-ups to Yamakawa–Zhandry seek to derandomize the oracle into a concrete hash function, which would give verifiable quantum advantage on an $\mathsf{NP}$ search problem in the standard model. Groups at NTT, Princeton and Weizmann are active. *(frontier — verify)*
- **Lattices.** Yilei Chen's April 2024 preprint claimed a polynomial-time quantum algorithm for variants of LWE with small modulus/noise ratio; a bug was identified within days by Ducas, van Woerden and Chen himself, and the main claim was withdrawn. Repair attempts and the surrounding "complex Gaussian filtering" toolkit continue to be studied. *(frontier — verify)*
- **Quantum walks and backtracking.** Sharper $\tilde O(\sqrt{T})$-style bounds for branch-and-bound and DPLL, plus tree-size estimation (Ambainis–Kokainis), give constant-factor-in-the-exponent improvements only; no candidate breaks $2^{cn}$ for $c$ near $0$.
- **Fine-grained quantum complexity.** Quantum analogues of SETH: whether $\mathsf{QSETH}$ (quantum Strong Exponential Time Hypothesis, Buhrman–Patro–Speelman) holds, i.e. $k$-SAT needs $2^{n/2}$ quantum time. This is the operative working hypothesis in post-quantum parameter selection.

## 8. Future Work

- Prove the Aaronson–Ambainis conjecture, giving $\mathsf{BQP}^A \subseteq \mathsf{PH}^A$-style statements for *all* random-oracle-like settings and a rigorous "structure is necessary" theorem.
- Find non-algebrizing techniques; candidates are geometric complexity theory and proof-complexity-based lower bounds, neither yet adapted to quantum classes.
- Identify an $\mathsf{NP}$-intermediate problem with hidden structure (beyond hidden subgroup) admitting quantum polynomial time — the only realistic route to surprise.
- Settle whether $\mathsf{BQP} \subseteq \mathsf{NP}$-relative-to-real-instances by finding a $\mathsf{BQP}$ problem with no classical certificate under standard assumptions.
- Refine $\mathsf{QSETH}$ into a usable hardness hypothesis with reductions, so cryptographic parameters rest on a stated conjecture rather than folklore.

## 9. Key References

- **[Foundational]** E. Bernstein, U. Vazirani. *Quantum Complexity Theory.* SIAM Journal on Computing 26(5):1411–1473, 1997.
- **[Foundational]** C. Bennett, E. Bernstein, G. Brassard, U. Vazirani. *Strengths and Weaknesses of Quantum Computing.* SIAM Journal on Computing 26(5):1510–1523, 1997.
- **[Foundational]** L. Grover. *A Fast Quantum Mechanical Algorithm for Database Search.* STOC 1996, pp. 212–219.
- **[Foundational]** P. Shor. *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.* SIAM Journal on Computing 26(5):1484–1509, 1997.
- **[Foundational]** L. Adleman, J. DeMarrais, M.-D. Huang. *Quantum Computability.* SIAM Journal on Computing 26(5):1524–1540, 1997.
- **[Foundational]** L. Fortnow, J. Rogers. *Complexity Limitations on Quantum Computation.* Journal of Computer and System Sciences 59(2):240–252, 1999.
- **[Technique]** R. Beals, H. Buhrman, R. Cleve, M. Mosca, R. de Wolf. *Quantum Lower Bounds by Polynomials.* Journal of the ACM 48(4):778–797, 2001.
- **[Technique]** A. Ambainis. *Quantum Lower Bounds by Quantum Arguments.* Journal of Computer and System Sciences 64(4):750–767, 2002.
- **[Barrier]** S. Aaronson, A. Wigderson. *Algebrization: A New Barrier in Complexity Theory.* ACM Transactions on Computation Theory 1(1), 2009.
- **[SOTA / Recent]** R. Raz, A. Tal. *Oracle Separation of BQP and PH.* STOC 2019, pp. 13–23; Journal of the ACM 69(4), 2022.
- **[SOTA / Recent]** T. Yamakawa, M. Zhandry. *Verifiable Quantum Advantage without Structure.* FOCS 2022; Journal of the ACM, 2024.
- **[SOTA / Recent]** A. Ambainis, K. Balodis, J. Iraids, M. Kokainis, K. Prūsis, J. Vihrovs. *Quantum Speedups for Exponential-Time Dynamic Programming Algorithms.* SODA 2019, pp. 1783–1793.
- **[SOTA / Recent]** A. Montanaro. *Quantum Walk Speedup of Backtracking Algorithms.* Theory of Computing 14(15):1–24, 2018.
- **[Survey]** S. Aaronson, A. Ambainis. *The Need for Structure in Quantum Speedups.* Theory of Computing 10(6):133–166, 2014.
- **[Survey]** S. Aaronson. *BQP and the Polynomial Hierarchy.* STOC 2010, pp. 141–150.
- **[Textbook]** M. Nielsen, I. Chuang. *Quantum Computation and Quantum Information.* Cambridge University Press, 10th Anniversary Edition, 2010.
- **[Textbook]** S. Arora, B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapter 10).

## 10. Worked Example / Concrete Special Case

**Grover on $N=4$: exact search in one query.** Let $f:\{0,1,2,3\}\to\{0,1\}$ with $f(x)=1$ iff $x=3$. Start from the uniform superposition
$$|s\rangle = \tfrac12\big(|0\rangle+|1\rangle+|2\rangle+|3\rangle\big).$$

*Oracle step.* $O_f|x\rangle = (-1)^{f(x)}|x\rangle$ gives amplitudes $(\tfrac12,\tfrac12,\tfrac12,-\tfrac12)$.

*Diffusion step.* $D = 2|s\rangle\langle s| - I$ maps $\alpha_x \mapsto 2\bar{\alpha} - \alpha_x$ where $\bar\alpha$ is the mean. Here $\bar\alpha = \tfrac{1}{4}(\tfrac12+\tfrac12+\tfrac12-\tfrac12) = \tfrac14$. So
$$\alpha_0,\alpha_1,\alpha_2 \mapsto 2\cdot\tfrac14 - \tfrac12 = 0, \qquad \alpha_3 \mapsto 2\cdot\tfrac14 - (-\tfrac12) = 1.$$

The state is exactly $|3\rangle$: **one query**, success probability $1$, versus $2.25$ expected classical queries. In general the optimal iteration count is $\lfloor \tfrac{\pi}{4}\sqrt N \rfloor$; for $N=4$ that is $\lfloor 1.57 \rfloor = 1$.

**Why this does not give $\mathsf{NP} \subseteq \mathsf{BQP}$.** Take 3-SAT on $n$ variables, $N = 2^n$ assignments. Grover finds a satisfying assignment in $\Theta(2^{n/2})$ evaluations — still exponential. The BBBV hybrid argument shows this is optimal in the black box. Sketch: run the $T$-query algorithm on the all-zero input, and let $q_{x} = \sum_{t=1}^{T} |\alpha_{x,t}|^2$ be the total query magnitude on index $x$ over all steps. Since each step's amplitudes are normalized, $\sum_{x=1}^{N} q_x \le T$, so some $x^\star$ has $q_{x^\star} \le T/N$. Flipping the oracle at $x^\star$ changes the final state by Euclidean distance at most $2\sqrt{T \cdot q_{x^\star}} \le 2T/\sqrt N$. For the algorithm to distinguish the two inputs with constant bias, this must be $\Omega(1)$, hence
$$T = \Omega(\sqrt N) = \Omega(2^{n/2}).$$

The gap of Section 6 is now visible in one line: the argument treats the SAT formula as an oracle. A real 3-SAT instance is a $\mathrm{poly}(n)$-bit string that the algorithm can read, and no known technique rules out a quantum algorithm that exploits that description — just as Shor exploits the description of $N$ rather than querying a black-box factoring oracle.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*