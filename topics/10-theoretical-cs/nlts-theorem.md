---
id: 10-theoretical-cs/nlts-theorem
title: "NLTS Theorem"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NLTS Theorem (No Low-Energy Trivial States)

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/nlts-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The **No Low-Energy Trivial States (NLTS) conjecture**, posed by Freedman and Hastings (2014), asks whether there is a family of local Hamiltonians whose *entire low-energy space* — not merely the ground space — is globally entangled, in the circuit-complexity sense.

**Statement (NLTS).** There exists a constant $\varepsilon>0$, a constant locality $k$, and an explicit family $\{H^{(n)}\}_{n\to\infty}$ of $k$-local Hamiltonians on $n$ qubits with $m=\Theta(n)$ terms, such that every state $|\psi\rangle$ with
$$\langle\psi|H^{(n)}|\psi\rangle \le e_0(H^{(n)}) + \varepsilon$$
requires quantum circuit depth $\omega(1)$ to prepare from $|0^n\rangle$ using two-qubit gates.

**Resolution.** Anshu, Breuckmann and Nirkhe (STOC 2023) proved NLTS, with the quantitative bound $\mathrm{depth} = \Omega(\log n)$, using asymptotically good quantum LDPC codes. The page status is therefore *solved-recently*: the named conjecture is a theorem, while the strengthenings it was invented to serve (quantum PCP, NLSS, polynomial-depth NLTS) remain open.

A complete proof required: (i) an explicit Hamiltonian family, (ii) a constant $\varepsilon$ independent of $n$, (iii) a lower bound holding for *all* states in the energy window, not for ground states only.

## 2. Mathematical Foundations

**Local Hamiltonian.** $H=\frac{1}{m}\sum_{i=1}^{m}H_i$ on $(\mathbb{C}^2)^{\otimes n}$, each $H_i$ acting on at most $k=O(1)$ qubits with $0\preceq H_i\preceq I$. Normalized so $\|H\|\le 1$; the energy $\langle\psi|H|\psi\rangle$ is the *fraction of violated constraints*. Write $e_0(H)=\lambda_{\min}(H)$; the Hamiltonian is **frustration-free** if $e_0=0$.

**Trivial state.** $|\psi\rangle$ is $d$-trivial if $|\psi\rangle = U|0^n\rangle$ for a circuit $U$ of two-qubit gates of depth $d$. A depth-$d$ circuit has lightcones of radius $2^d$; for $d=O(1)$ the state is a bounded-range entangled state with strictly local correlations.

**CSS codes.** For binary matrices $H_X\in\mathbb{F}_2^{m_X\times n}$, $H_Z\in\mathbb{F}_2^{m_Z\times n}$ with $H_XH_Z^{\mathsf T}=0$, the code is $\mathcal{C}=\ker H_X\cap\ker H_Z$ read in the appropriate bases, with associated Hamiltonian
$$H=\frac{1}{m_X+m_Z}\Big(\sum_{r}\tfrac{I-\prod_{j\in r}X_j}{2}+\sum_{s}\tfrac{I-\prod_{j\in s}Z_j}{2}\Big),$$
frustration-free with ground space the codespace. **qLDPC** means every check has weight $O(1)$ and every qubit is in $O(1)$ checks. **Good** means rate $k/n=\Theta(1)$ and distance $d=\Theta(n)$.

**Confinement.** The property actually used is stronger than distance: a code has *linear confinement* if any error $e$ with $|e|\le \alpha n$ and syndrome weight $|H_Ze|\le \beta n$ is equivalent, modulo stabilizers, to an error of weight $O(|H_Ze|)$. Good qLDPC codes (Panteleev–Kalachev; Leverrier–Zémor) satisfy this.

**Clustering.** For a distribution $p$ on $\{0,1\}^n$, say $p$ is *$(\alpha,\beta)$-clustered* if its support decomposes into sets pairwise separated by Hamming distance $\ge \alpha n$, each of diameter $\le\beta n$.

**Theorem (ABN 2023).** Let $\{Q_n\}$ be good qLDPC codes with linear confinement and $H^{(n)}$ their code Hamiltonians. There is $\varepsilon>0$ such that any $|\psi\rangle$ with $\langle\psi|H^{(n)}|\psi\rangle\le\varepsilon$ has circuit depth $\Omega(\log n)$.

**Proof skeleton.** (a) *Code side:* low energy forces the computational-basis measurement distribution of $|\psi\rangle$ to be well-clustered — mass sits on far-separated syndrome sectors, by confinement. (b) *Circuit side:* if $|\psi\rangle$ is $O(1)$-depth, its measurement statistics obey a martingale/lightcone concentration argument that rules out mass on two clusters at Hamming distance $\Theta(n)$ while the $X$-basis statistics simultaneously satisfy the $X$-checks. (c) Contradiction via an uncertainty-type argument playing the $X$ and $Z$ distributions against each other.

## 3. History & State of the Art

- **2013.** Aharonov, Arad, Vidick's SIGACT survey formulates the **quantum PCP (qPCP)** conjecture and isolates NLTS as its "entanglement-theoretic" necessary consequence: if qPCP holds and $\mathrm{QMA}\ne\mathrm{NP}$, NLTS Hamiltonians exist (a constant-depth low-energy state is a classical certificate whose energy is poly-time computable).
- **2013.** Hastings: commuting Hamiltonians on low-dimensional/hyperfinite geometry admit trivial low-energy states — NLTS must live on expanders.
- **2014.** Freedman and Hastings state NLTS and give the hyperfiniteness framing: the interaction complex must be *non-$k$-hyperfinite*.
- **2013.** Brandão–Harrow: for high-degree or expanding constraint graphs, *product states* approximate the ground energy well — the "no-go" that constrains which Hamiltonians can be NLTS.
- **2017.** Eldar–Harrow prove **NLETS** (no low-*error* trivial states): states within Hamming-type error $o(n)$ of the ground space are nontrivial. Weaker than NLTS since low energy $\ne$ low error.
- **2018.** Nirkhe–Vazirani–Yuen give a simpler NLETS proof via approximate low-weight check codes.
- **2021.** Anshu–Nirkhe obtain $\Omega(\log n)$ depth bounds for ground states of linear-distance qLDPC codes and for restricted low-energy regimes.
- **2022.** Panteleev–Kalachev and Leverrier–Zémor construct asymptotically good qLDPC codes — the missing ingredient.
- **2022–23.** Anshu, Breuckmann, Nirkhe prove NLTS (arXiv:2206.13228; STOC 2023, best-paper).

## 4. Partial Results / Verified Cases

- **Proved in full generality:** constant $\varepsilon$, constant locality, $\Omega(\log n)$ depth, for good qLDPC code Hamiltonians (PK / LZ / DELLM constructions), qubit degree and check weight $O(1)$.
- **NLETS:** proved 2017 for error $\epsilon n$ with $\epsilon$ constant, via hypergraph-product codes with $\Theta(\sqrt n)$ distance.
- **Ground-space-only bounds:** any code Hamiltonian with distance $d$ forces depth $\Omega(\log d)$ on exact ground states; toric code ($d=\Theta(\sqrt n)$) gives $\Omega(\log n)$.
- **Stabilizer restriction:** Coble–Coudron–Nelson–Nezhadi (TQC 2023) show local Hamiltonians with *no low-energy stabilizer states*, a different resource-restricted strengthening.
- **Where NLTS provably fails:** commuting Hamiltonians on $D$-dimensional lattices for fixed $D$; any hyperfinite interaction graph; high-temperature Gibbs states, which Bakshi–Liu–Moitra–Tang (FOCS 2024) show are unentangled and efficiently preparable above a constant temperature.
- **Depth regime:** the theorem is tight only up to $\Theta(\log n)$; no low-energy state of any explicit Hamiltonian is known to require depth $n^{\Omega(1)}$.

## 5. Principal Obstacles

The historical obstacles, and why they still bite for the successor problems:

- **Distance is not enough.** Linear distance controls the ground space only. A state can have energy $\varepsilon m$ and be at Hamming distance $\Theta(n)$ from every codeword. The fix — confinement/small-set expansion — was unavailable before good qLDPC codes.
- **Lightcone arguments alone fail.** Constant-depth circuits still generate correlations at range $2^d$; a counting or lightcone-locality argument gives no contradiction with $\varepsilon$-energy unless one also controls the *global* shape of the measurement distribution.
- **Product-state barrier.** By Brandão–Harrow, on dense or high-degree instances product states achieve near-optimal energy, so NLTS instances must be sparse *and* expanding — a narrow window.
- **Commuting case.** Hastings's coarse-graining shows that for commuting local terms on hyperfinite complexes one can always patch together locally exact states, so geometric locality is fatal.
- **For qPCP specifically:** NLTS is a *statement about states*, qPCP a statement about *hardness*. No known reduction turns circuit-depth lower bounds into QMA-hardness of gap estimation; that would need quantum locally testable codes with constant rate, distance and soundness plus a gap-amplification analogue of Dinur's proof, and quantum gap amplification is blocked by the impossibility of copying witnesses.

## 6. The Gap

For NLTS itself the gap is closed. The residual gaps are:

1. **Depth strength.** Proven: $\Omega(\log n)$. Wanted: $n^{\Omega(1)}$ or even $\Omega(n)$ depth for low-energy states. Present techniques cap out at $\log n$ because clustering arguments only certify entanglement across a single scale.
2. **NLSS.** *No Low-energy Sampleable States*: low-energy states whose measurement statistics can be sampled by a classical poly-size circuit should not exist. This is the true NP-certificate obstruction to qPCP; NLTS is strictly weaker (constant-depth $\subsetneq$ classically sampleable).
3. **qPCP.** NLTS is necessary but far from sufficient. Missing: $c^3$-qLTCs feeding a quantum gap amplification.

## 7. Current Research (as of June 2026)

- **qLTC programme.** Dinur, Lin and Vidick (FOCS 2024) construct quantum locally testable codes with constant rate, distance and soundness from expanding cubical complexes — the qPCP-facing successor to the good-qLDPC breakthrough. Groups: Weizmann, Caltech, IQC/Berkeley. *(frontier — verify)* attempts to combine $c^3$-qLTCs with an entropic gap-amplification step remain unpublished.
- **NLSS.** Partial results restrict the class of classical samplers (shallow classical circuits, matrix-product-state samplers). Full NLSS is open. *(frontier — verify)*
- **Thermal-state boundary.** High-temperature efficient Gibbs sampling results (Bakshi–Liu–Moitra–Tang; Rouzé–França–Alhambra) sharpen where NLTS-type robustness can hold, pushing toward a critical-temperature dichotomy.
- **Beyond log depth.** Work on "combinatorial NLTS" and on the low-energy spaces of quantum Tanner codes seeks polynomial depth bounds via multi-scale clustering. *(frontier — verify)*

## 8. Future Work

- Prove or refute **NLSS**; this is the explicitly stated next milestone in Anshu–Breuckmann–Nirkhe.
- Upgrade $\Omega(\log n)$ to $n^{\Omega(1)}$ depth, presumably by showing the low-energy space itself carries codewords of a hierarchy of nested codes.
- Establish a **quantum gap amplification** theorem, or prove a formal barrier to it.
- Determine whether NLTS holds for **commuting** Hamiltonians, where Hastings's results leave a gap between hyperfinite (fails) and expanding non-hyperfinite complexes.
- Physical instantiation: identify a natural many-body model — not code-derived — with an NLTS low-energy space, addressing whether "room-temperature robust entanglement" (Eldar) is achievable in a laboratory geometry.

## 9. Key References

- **[Foundational]** M. Freedman, M. Hastings. *Quantum systems on non-$k$-hyperfinite complexes: a generalization of classical statistical mechanics on expander graphs.* Quantum Information & Computation 14(1–2):144–180, 2014. arXiv:1301.1363.
- **[Foundational]** D. Aharonov, I. Arad, T. Vidick. *Guest Column: The Quantum PCP Conjecture.* ACM SIGACT News 44(2):47–79, 2013.
- **[SOTA]** A. Anshu, N. P. Breuckmann, C. Nirkhe. *NLTS Hamiltonians from Good Quantum Codes.* STOC 2023, 1090–1096. arXiv:2206.13228.
- **[SOTA]** P. Panteleev, G. Kalachev. *Asymptotically Good Quantum and Locally Testable Classical LDPC Codes.* STOC 2022, 375–388.
- **[SOTA]** A. Leverrier, G. Zémor. *Quantum Tanner Codes.* FOCS 2022, 872–883.
- **[SOTA]** I. Dinur, S. Evra, R. Livne, A. Lubotzky, S. Mozes. *Good Quantum LDPC Codes with Linear Time Decoders.* STOC 2023.
- **[Recent]** I. Dinur, T.-C. Lin, T. Vidick. *Expansion of higher-dimensional cubical complexes with application to quantum locally testable codes.* FOCS 2024.
- **[Prior art]** L. Eldar, A. Harrow. *Local Hamiltonians Whose Ground States Are Hard to Approximate.* FOCS 2017, 427–438.
- **[Prior art]** C. Nirkhe, U. Vazirani, H. Yuen. *Approximate Low-Weight Check Codes and Circuit Lower Bounds for Noisy Ground States.* ICALP 2018.
- **[Prior art]** A. Anshu, C. Nirkhe. *Circuit lower bounds for low-energy states of quantum code Hamiltonians.* ITCS 2021.
- **[Barrier]** F. Brandão, A. Harrow. *Product-state approximations to quantum ground states.* STOC 2013, 871–880.
- **[Barrier]** M. Hastings. *Trivial low energy states for commuting Hamiltonians and the quantum PCP conjecture.* Quantum Information & Computation 13(5–6):393–429, 2013.
- **[Related]** J. Coble, M. Coudron, J. Nelson, S. Nezhadi. *Local Hamiltonians with no low-energy stabilizer states.* TQC 2023.
- **[Related]** A. Bakshi, A. Liu, A. Moitra, E. Tang. *High-temperature Gibbs states are unentangled and efficiently preparable.* FOCS 2024.
- **[Background]** A. Kitaev. *Fault-tolerant quantum computation by anyons.* Annals of Physics 303(1):2–30, 2003.

## 10. Worked Example / Concrete Special Case

**Why the toric code is *not* NLTS — an explicit constant-depth low-energy state.**

Take Kitaev's toric code on an $L\times L$ torus: $n=2L^2$ qubits on edges, $m=2L^2$ checks ($L^2$ star operators $A_v=\prod_{j\ni v}X_j$, $L^2$ plaquettes $B_p=\prod_{j\in p}Z_j$), Hamiltonian $H=\frac{1}{m}\sum_v\frac{I-A_v}{2}+\frac{1}{m}\sum_p\frac{I-B_p}{2}$, $e_0=0$, code distance $L=\Theta(\sqrt n)$. Exact ground states need depth $\Omega(L)$.

Now coarse-grain. Fix a constant $b$ and tile the torus with $(L/b)^2$ blocks of size $b\times b$.

1. On each block $B$, prepare the ground state of $H_B$ = the sum of only those checks whose support lies entirely inside $B$. Each block has $O(b^2)=O(1)$ qubits, so this state is producible by a circuit of depth $O(b^2)=O(1)$.
2. Blocks are disjoint, so the global state $|\psi_b\rangle=\bigotimes_B |\phi_B\rangle$ is prepared in depth $O(1)$ — a trivial state.
3. Energy accounting. Every check inside a block is satisfied exactly. Only checks straddling a block boundary can be violated. A $b\times b$ block has $O(b)$ boundary checks, so the total number of possibly-violated checks is at most $c\cdot (L/b)^2\cdot b = cL^2/b$.
4. Energy density:
$$\langle\psi_b|H|\psi_b\rangle \;\le\; \frac{cL^2/b}{2L^2} \;=\; \frac{c}{2b}.$$

Given any target $\varepsilon>0$, choose $b=\lceil c/(2\varepsilon)\rceil$ — a constant. Then $|\psi_b\rangle$ has energy $\le\varepsilon$ and depth $O(b^2)=O(1)$. So the toric code has low-energy trivial states at every constant $\varepsilon$, for every $L$.

**The lesson.** The argument uses only that the interaction graph is *hyperfinite*: removing an $O(1/b)$ fraction of edges leaves components of size $O(1)$. Every $D$-dimensional lattice is hyperfinite, so no geometrically local model can be NLTS. Expander interaction graphs are not hyperfinite — cutting the graph into constant-size pieces costs a *constant fraction* of edges, so the boundary term above never shrinks. This is exactly Freedman and Hastings's "non-$k$-hyperfinite complexes" requirement, and exactly the property that good qLDPC codes supply, letting Anshu–Breuckmann–Nirkhe convert the failed accounting above into a genuine $\Omega(\log n)$ depth lower bound.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*