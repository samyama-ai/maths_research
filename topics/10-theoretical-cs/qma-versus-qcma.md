---
id: 10-theoretical-cs/qma-versus-qcma
title: "QMA versus QCMA"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# QMA versus QCMA

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/qma-versus-qcma` · **Status:** open

## 1. Problem Statement / Conjecture

Two quantum analogues of $\mathsf{NP}$ differ only in the *type of proof* the prover sends.

- $\mathsf{QMA}$: a polynomial-time quantum verifier receives a quantum state $|\psi\rangle$ on $\mathrm{poly}(n)$ qubits.
- $\mathsf{QCMA}$ (also written $\mathsf{MQA}$): the same verifier receives a *classical* string $w \in \{0,1\}^{\mathrm{poly}(n)}$.

**Question.** Is $\mathsf{QCMA} = \mathsf{QMA}$?

Trivially $\mathsf{QCMA} \subseteq \mathsf{QMA}$ (a classical witness is a computational-basis state). The conjecture, first posed explicitly by Aharonov and Naveh (2002), is that the inclusion is **strict**: quantum proofs are strictly more powerful than classical proofs of the same length for quantum verifiers.

A resolution requires either (i) a proof that every $\mathsf{QMA}$ language admits a polynomial-length classical witness verifiable by a $\mathsf{BQP}$ machine, or (ii) an unconditional separation — which would imply $\mathsf{P} \neq \mathsf{PSPACE}$, since $\mathsf{QCMA} \subseteq \mathsf{QMA} \subseteq \mathsf{PP} \subseteq \mathsf{PSPACE}$ and $\mathsf{P}=\mathsf{PSPACE}$ collapses both. Hence the realistic targets are *relativized* separations and *conditional* results.

## 2. Mathematical Foundations

**Definition (QMA).** $L = (L_{\text{yes}}, L_{\text{no}}) \in \mathsf{QMA}(c,s)$ if there is a uniform family of polynomial-size quantum circuits $\{V_n\}$ acting on $m(n)$ witness qubits and $k(n)$ ancillas such that, writing the accept projector $\Pi_{\mathrm{acc}} = V_x^\dagger (|1\rangle\langle 1|_{\text{out}} \otimes I) V_x$,

$$
x \in L_{\text{yes}} \;\Rightarrow\; \exists\, \rho \ \text{ on } \mathbb{C}^{2^{m}}:\quad \operatorname{Tr}\!\big[\Pi_{\mathrm{acc}}\,(\rho \otimes |0^k\rangle\langle 0^k|)\big] \ge c,
$$
$$
x \in L_{\text{no}} \;\Rightarrow\; \forall\, \rho:\quad \operatorname{Tr}\!\big[\Pi_{\mathrm{acc}}\,(\rho \otimes |0^k\rangle\langle 0^k|)\big] \le s .
$$

By convexity the optimal $\rho$ may be taken pure, so the acceptance probability is the largest eigenvalue of the operator $Q_x = \operatorname{Tr}_{\text{anc}}\big[(I\otimes\langle 0^k|)\Pi_{\mathrm{acc}}(I\otimes|0^k\rangle)\big]$:

$$
\max_{|\psi\rangle} \langle \psi | Q_x | \psi\rangle = \lambda_{\max}(Q_x).
$$

**Definition (QCMA).** Identical, except the witness is restricted to $\rho = |w\rangle\langle w|$ for $w \in \{0,1\}^{m}$, so the quantity of interest is $\max_{w}\langle w|Q_x|w\rangle$, i.e. the largest *diagonal entry* of $Q_x$ in the computational basis rather than its largest eigenvalue. The whole question is whether that basis-restricted optimum can be made to track $\lambda_{\max}$ up to a constant gap.

**Amplification.** $\mathsf{QMA}(c,s) = \mathsf{QMA}(1-2^{-p}, 2^{-p})$ for any polynomial $p$ whenever $c - s \ge 1/\mathrm{poly}$, by the Marriott–Watrous in-place amplification, which uses no extra witness copies. The same holds for $\mathsf{QCMA}$, where naive repetition also works since classical witnesses can be copied.

**Known relations.**
$$
\mathsf{MA} \subseteq \mathsf{QCMA} \subseteq \mathsf{QMA} \subseteq \mathsf{PP} \subseteq \mathsf{PSPACE},\qquad \mathsf{BQP}\subseteq\mathsf{QCMA}.
$$
$\mathsf{QMA}\subseteq\mathsf{PP}$ is due to Kitaev–Watrous and Vyalyi. Also $\mathsf{QMA}/\mathrm{qpoly} \subseteq \mathsf{PSPACE}/\mathrm{poly}$ (Aaronson 2006).

**Complete problems.** $\mathsf{QMA}$: the $k$-Local Hamiltonian problem for $k \ge 2$ (Kitaev; Kempe–Kitaev–Regev), i.e. decide whether $\lambda_{\min}(H) \le a$ or $\ge b$ with $b-a \ge 1/\mathrm{poly}$ for $H = \sum_i H_i$ with each $H_i$ acting on $k$ qubits. $\mathsf{QCMA}$: identifying a nontrivial complete problem is itself hard; known ones include the two problems of Wocjan–Janzing–Beth (2003) and ground-space connectivity (GSCON) for commuting local Hamiltonians (Gosset–Mehta–Vidick 2017).

## 3. History & State of the Art (SOTA)

- **2000.** Watrous defines Group Non-Membership and places it in $\mathsf{QMA}$ using a quantum witness (a subgroup superposition), giving the first natural problem with a quantum-only proof.
- **2002.** Aharonov and Naveh introduce $\mathsf{QCMA}$ and pose $\mathsf{QMA}$ vs $\mathsf{QCMA}$ as the central "is a quantum proof more than a classical proof?" question.
- **2005.** Marriott–Watrous strong amplification removes the naive obstacle that quantum witnesses cannot be cloned.
- **2007.** Aaronson and Kuperberg give a **quantum oracle separation**: there is a unitary oracle $U$ with $\mathsf{QMA}^U \neq \mathsf{QCMA}^U$.
- **2012.** Jordan–Kobayashi–Nagaj–Nishimura show $\mathsf{QCMA}$ has perfect completeness ($\mathsf{QCMA} = \mathsf{QCMA}_1$); the analogous statement for $\mathsf{QMA}$ remains open.
- **2016.** Grilo–Kerenidis–Sikora show $\mathsf{QMA}$ equals $\mathsf{QMA}$ with **subset-state** witnesses $|S\rangle = |S|^{-1/2}\sum_{x\in S}|x\rangle$, reducing the gap to "can a subset be described classically enough?"
- **2018.** Fefferman–Kimmel strengthen the oracle model: separation relative to an **in-place permutation oracle** (a classical-ish, non-standard access model).
- **2023.** Natarajan–Nirkhe give a **distributional/classical-oracle** separation (a randomized classical oracle in a distribution-testing access model), the closest to a standard classical oracle separation.
- **2024.** Li–Liu–Pelecanos–Yamakawa separate $\mathsf{QMA}$ and $\mathsf{QCMA}$ relative to a *classically-accessible classical* oracle, closing much of the remaining gap to the standard model.

No unrelativized progress in either direction.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| Quantum oracle $U$ | $\mathsf{QMA}^U \neq \mathsf{QCMA}^U$ (Aaronson–Kuperberg 2007) |
| In-place permutation oracle | Separation (Fefferman–Kimmel 2018) |
| Distribution-testing / randomized classical oracle | Separation (Natarajan–Nirkhe 2023) |
| Classically-accessible classical oracle | Separation (Li–Liu–Pelecanos–Yamakawa 2024) |
| Standard classical oracle $A$ | **Open** |
| Witness structure | $\mathsf{QMA}$ = $\mathsf{QMA}$ with subset-state witnesses (Grilo–Kerenidis–Sikora 2016) |
| Error profile | $\mathsf{QCMA}=\mathsf{QCMA}_1$ (Jordan et al. 2012); $\mathsf{QMA}$ vs $\mathsf{QMA}_1$ open |
| Witness length $m = O(\log n)$ | Collapses: both equal $\mathsf{BQP}$ (a $O(\log n)$-qubit witness can be found by exhaustive tomography-free search over an $\varepsilon$-net of size $2^{\mathrm{poly}(n)}$? — no; instead, for $m=O(\log n)$, $\lambda_{\max}(Q_x)$ is estimable in $\mathsf{BQP}$ up to $1/\mathrm{poly}$ by phase estimation on a $\mathrm{poly}(n)$-dimensional space, giving $\mathsf{QMA}[O(\log n)]=\mathsf{BQP}=\mathsf{QCMA}[O(\log n)]$) |
| Stoquastic Hamiltonians | $\mathsf{StoqMA}\subseteq\mathsf{AM}$ (Bravyi–Terhal 2009): for this class the quantum witness is replaceable by a classical interactive proof |
| Commuting local Hamiltonians, GSCON | $\mathsf{QCMA}$-complete (Gosset–Mehta–Vidick 2017) — a natural problem on the classical side of the fence |

## 5. Principal Obstacles

- **No cloning is not the obstacle.** The intuitive advantage of a quantum witness — it cannot be copied — is neutralized by Marriott–Watrous amplification. So the separation must come from *information content*, not from fragility.
- **Counting arguments do not bind.** A quantum witness on $m$ qubits lives in a continuum, but any verifier with $1/\mathrm{poly}$ gap can only distinguish states up to an $\varepsilon$-net of size $2^{O(m\log(1/\varepsilon))}$. Naive dimension counting therefore *fails to separate*: the number of "effectively distinct" witnesses is $2^{\mathrm{poly}(m)}$, only polynomially more bits than a classical witness of length $\mathrm{poly}(m)$ — which is exactly why many people expect the classes might be equal.
- **Subset-state reduction.** After Grilo–Kerenidis–Sikora, an adequate witness is always $|S\rangle$ for some $S\subseteq\{0,1\}^m$. Proving $\mathsf{QMA}=\mathsf{QCMA}$ needs a classical description of a *good* $S$ of polynomial length; proving separation needs to show no such succinct description exists — a statement about the descriptive complexity of exponentially large sets, for which no lower-bound technique currently applies.
- **Relativization/oracle-model friction.** Every known separation uses a nonstandard oracle interface (unitary oracles, in-place permutations, sampling access). The standard-classical-oracle case fails because a classical oracle $A$ can be queried in superposition *and* described in pieces by the classical prover, and the adversary/polynomial methods do not currently give the required "hidden set is not succinctly describable" lower bound.
- **Non-relativizing collapse.** A proof of equality would almost certainly need to be non-relativizing (it must survive the known oracle separations only if those oracles are outside the standard model), pushing it toward algebrization-resistant, Hamiltonian-structural arguments — techniques that do not exist for $\mathsf{QMA}$.

## 6. The Gap

Proven: separation holds when the verifier's access to the hard object is *restricted* (quantum oracle, in-place permutation, sampling/distributional access, classically-accessible oracle). The general statement needs either

1. a **standard classical oracle** $A$ with $\mathsf{QMA}^A \neq \mathsf{QCMA}^A$ — the Aaronson–Kuperberg open problem, still open in 2026 despite 2023–2024 near-misses; or
2. an unrelativized argument, which forces $\mathsf{P}\neq\mathsf{PSPACE}$.

The exact missing step in direction (1): given a random exponential-size structure (e.g. a random subgroup, or a hidden subset $S$), show that *no* $\mathrm{poly}(n)$-bit classical hint, combined with $\mathrm{poly}(n)$ quantum queries to $A$, lets the verifier certify membership — while the state $|S\rangle$ does. Current adversary bounds break because a classical hint can encode a random $\mathrm{poly}(n)$-size sample from $S$, which suffices for all known candidate hard instances.

## 7. Current Research (as of June 2026)

- **Closing the oracle gap.** Follow-ups to Natarajan–Nirkhe and Li–Liu–Pelecanos–Yamakawa aim to convert classically-accessible-oracle separations into standard classical oracle separations; the technical target is a "distributional-to-standard" lifting theorem. *(frontier — verify)*
- **Structured witness classes.** Extending Grilo–Kerenidis–Sikora: which subclasses of subset states (e.g. those with $\mathsf{poly}$-size classical circuits deciding membership in $S$) suffice for $\mathsf{QMA}$? Equality would follow if all do.
- **Hamiltonian-side attacks.** Ground-state connectivity variants and commuting/stoquastic restrictions, where the classical-witness boundary is sharp (Gharibian–Sikora; Gosset–Mehta–Vidick).
- **Pseudorandomness.** Pseudorandom-state constructions are used to argue that "quantum witnesses that look classical" cannot be efficiently recognized, feeding candidate separations. *(frontier — verify)*
- **Groups.** Berkeley/Simons, IBM/MIT (Nirkhe, Natarajan), Maryland (Fefferman), CWI/QuSoft, and the Kyoto/NTT quantum complexity groups (Nishimura, Yamakawa).

## 8. Future Work

- Prove or refute: for every $\mathsf{QMA}$ verifier there is an optimal subset state $|S\rangle$ with $S$ decided by a $\mathrm{poly}(n)$-size classical circuit.
- Construct a standard classical oracle separation using an in-place-to-standard simulation, or prove such a simulation is impossible.
- Settle $\mathsf{QMA} \overset{?}{=} \mathsf{QMA}_1$, whose techniques are close to the $\mathsf{QCMA}$ perfect-completeness proof.
- Find a natural (non-oracle) candidate problem in $\mathsf{QMA}\setminus\mathsf{QCMA}$ beyond Group Non-Membership, which has been in $\mathsf{QCMA}$-adjacent territory ever since $\mathsf{GNM}\in\mathsf{NP}$ relative to a group-order oracle.
- Study $\mathsf{QCMA}$ hardness of approximation (a $\mathsf{QCMA}$-analogue of the quantum PCP conjecture).

## 9. Key References

- **[Foundational]** Dorit Aharonov, Tomer Naveh. *Quantum NP — A Survey.* arXiv:quant-ph/0210077, 2002.
- **[Foundational]** John Watrous. *Succinct Quantum Proofs for Properties of Finite Groups.* FOCS 2000.
- **[Foundational]** A. Yu. Kitaev, A. H. Shen, M. N. Vyalyi. *Classical and Quantum Computation.* AMS Graduate Studies in Mathematics 47, 2002.
- **[Foundational]** Chris Marriott, John Watrous. *Quantum Arthur–Merlin Games.* Computational Complexity 14(2), 2005.
- **[Key separation]** Scott Aaronson, Greg Kuperberg. *Quantum versus Classical Proofs and Advice.* Theory of Computing 3, 2007.
- **[SOTA]** Bill Fefferman, Shelby Kimmel. *Quantum vs. Classical Proofs and Subset Verification.* MFCS 2018.
- **[SOTA]** Anand Natarajan, Chinmay Nirkhe. *A Distribution Testing Oracle Separation between QMA and QCMA.* CCC 2023.
- **[SOTA]** Xingjian Li, Qipeng Liu, Angelos Pelecanos, Takashi Yamakawa. *Classical vs Quantum Advice and Proofs under Classically-Accessible Oracle.* ITCS 2024.
- **[Structural]** Alex B. Grilo, Iordanis Kerenidis, Jamie Sikora. *QMA with Subset State Witnesses.* Chicago Journal of Theoretical Computer Science, 2016.
- **[Structural]** Stephen P. Jordan, Hirotada Kobayashi, Daniel Nagaj, Harumichi Nishimura. *Achieving Perfect Completeness in Classical-Witness Quantum Merlin–Arthur Proof Systems.* Quantum Information and Computation 12, 2012.
- **[Structural]** David Gosset, Jenish C. Mehta, Thomas Vidick. *QCMA Hardness of Ground Space Connectivity for Commuting Hamiltonians.* Quantum 1:16, 2017.
- **[Structural]** Sergey Bravyi, Barbara Terhal. *Complexity of Stoquastic Frustration-Free Hamiltonians.* SIAM Journal on Computing 39(4), 2009.
- **[Survey]** Sevag Gharibian, Yichen Huang, Zeph Landau, Seung Woo Shin. *Quantum Hamiltonian Complexity.* Foundations and Trends in Theoretical Computer Science 10(3), 2015.

## 10. Worked Example / Concrete Special Case

**Group Non-Membership (Watrous 2000).** Input: a black-box group $G$ with unique encodings, generators $g_1,\dots,g_k$ of a subgroup $H \le G$, and an element $y \in G$. Decide whether $y \notin H$.

*Quantum witness.* The prover sends
$$
|H\rangle \;=\; \frac{1}{\sqrt{|H|}} \sum_{h \in H} |h\rangle .
$$
Note $|H|$ may be exponential, so $|H\rangle$ has no obvious short classical description.

*Verifier.* Apply the controlled left-multiplication $U_y : |b\rangle|g\rangle \mapsto |b\rangle |y^b g\rangle$ with the control qubit in $|+\rangle$, then Hadamard the control and measure:

$$
|+\rangle|H\rangle \;\xrightarrow{U_y}\; \tfrac{1}{\sqrt2}\big(|0\rangle|H\rangle + |1\rangle|yH\rangle\big)
\;\xrightarrow{\ H\ }\; \tfrac12 |0\rangle\big(|H\rangle+|yH\rangle\big) + \tfrac12 |1\rangle\big(|H\rangle-|yH\rangle\big).
$$

Since $H$ and $yH$ are cosets, $\langle H | yH\rangle = 1$ if $y \in H$ and $0$ otherwise. So

$$
\Pr[\text{measure } 1] = \tfrac{1}{2}\big(1 - |\langle H|yH\rangle|^2\big) = \begin{cases} 1/2, & y \notin H,\\ 0, & y \in H.\end{cases}
$$

A cheating prover cannot fake this: any state $|\phi\rangle$ passing the extra "$H$-invariance" test $|\phi\rangle \approx |h\phi\rangle$ for random $h\in H$ must be close to a superposition supported on cosets of $H$, and for $y \in H$ every such state is invariant under multiplication by $y$, forcing acceptance probability $\approx 0$. Completeness $1/2$, soundness $\approx 0$; amplify by repetition (or Marriott–Watrous).

*Where the open problem lives.* Replace $|H\rangle$ by a classical string $w$ of length $\mathrm{poly}(\log|G|)$. What could $w$ be? A list of $\mathrm{poly}$ many elements of $H$ does not certify non-membership; the order $|H|$ does (with a $\mathsf{QCMA}$ protocol using order-finding-type checks), which is precisely why Group Non-Membership is **not** a proven witness of separation. The general question — whether the analogous "quantum-only" certificate for an arbitrary $\mathsf{QMA}$ problem always admits such a classical surrogate — is exactly $\mathsf{QMA}$ vs $\mathsf{QCMA}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*