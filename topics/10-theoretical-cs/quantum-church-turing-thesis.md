---
id: 10-theoretical-cs/quantum-church-turing-thesis
title: "Quantum Church-Turing Thesis"
topic: 10-theoretical-cs
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Church-Turing Thesis

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-church-turing-thesis` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The **Quantum Church–Turing Thesis (QCTT)**, in its strong (efficiency-preserving) form, asserts:

> Every finite physical system, evolving for a finite time under the laws of physics, can be simulated to any fixed accuracy $\varepsilon$ by a universal quantum computer using resources (qubits, gate count, time) polynomial in the system's size, its evolution time, and $1/\varepsilon$.

Equivalently: the complexity class of problems efficiently solvable by *any* physically realizable device equals $\mathsf{BQP}$.

Two weaker/stronger variants must be separated:

- **Weak (computability) form.** Any physically computable function is Turing-computable. Quantum mechanics adds no *uncomputable* power.
- **Strong (complexity) form.** Any physically computable function is computable in $\mathsf{BQP}$, i.e. polynomial-time quantum.

The thesis is not a theorem: it quantifies over "the laws of physics," which are not axiomatized. A *proof* would require fixing a complete physical theory $T$ (currently unavailable — quantum gravity is missing) and showing that $T$'s dynamics admits a $\mathrm{poly}$-size quantum circuit approximation. A *disproof* requires exhibiting a physical process, consistent with experimentally validated physics, that either (a) computes a Turing-uncomputable function, or (b) solves a problem believed outside $\mathsf{BQP}$ (e.g. an $\mathsf{NP}$-complete or $\mathsf{PSPACE}$-complete problem) in polynomial physical resources — with "resources" accounted honestly, including energy, precision and spacetime volume.

**Status:** *empirically-supported*. No experiment contradicts it; large fragments (local Hamiltonians, lattice gauge theory, topological QFT) are proven simulable in $\mathsf{BQP}$; but no fragment covering all of known physics has been established.

## 2. Mathematical Foundations

**Quantum Turing machine (QTM).** A QTM is a tuple $M=(\Sigma,Q,\delta)$ with transition amplitude function $\delta: Q\times\Sigma \to \widetilde{\mathbb{C}}^{\,Q\times\Sigma\times\{L,R\}}$, where $\widetilde{\mathbb{C}}$ denotes efficiently computable complex numbers (real and imaginary parts computable to $2^{-k}$ in time $\mathrm{poly}(k)$). $M$ is *well-formed* iff its induced time-evolution operator on the configuration Hilbert space is unitary. Bernstein–Vazirani give local conditions on $\delta$ equivalent to unitarity, and construct a universal QTM.

**Quantum circuits.** States live in $\mathcal{H}=(\mathbb{C}^2)^{\otimes n}$; a circuit is $U = U_T\cdots U_1$ with each $U_t$ acting nontrivially on $O(1)$ qubits. Define
$$\mathsf{BQP} = \bigcup_{c} \mathsf{BQTIME}(n^c),$$
where $L\in\mathsf{BQP}$ iff there is a uniform family $\{C_x\}$ of size $\mathrm{poly}(|x|)$ with $\Pr[\text{accept}]\ge 2/3$ for $x\in L$ and $\le 1/3$ otherwise. Known: $\mathsf{BPP}\subseteq\mathsf{BQP}\subseteq\mathsf{PP}\subseteq\mathsf{PSPACE}$.

**Equivalence theorems.**
- *(Yao 1993)* QTMs and uniform quantum circuit families simulate each other with polynomial overhead.
- *(Solovay–Kitaev)* Any universal finite gate set $\mathcal{G}$ closed under inverse generates a dense subgroup of $SU(2^k)$, and any $U$ is approximated to error $\varepsilon$ by $O(\log^{c}(1/\varepsilon))$ gates, $c\approx 2$ (Dawson–Nielsen 2006). Hence $\mathsf{BQP}$ is gate-set independent.
- *(Adiabatic equivalence)* Adiabatic quantum computation with $\mathrm{poly}$-bounded inverse spectral gap is polynomially equivalent to $\mathsf{BQP}$ (Aharonov–van Dam–Kempe–Landau–Lloyd–Regev 2007).

**The simulation problem.** Given a $k$-local Hamiltonian $H=\sum_{j=1}^{m} H_j$ on $n$ qubits, $\|H_j\|\le 1$, produce a circuit $\widetilde U$ with
$$\big\| e^{-iHt} - \widetilde U \big\| \le \varepsilon .$$
First-order Trotter: $\big\|e^{-i(A+B)t}-(e^{-iAt/r}e^{-iBt/r})^r\big\| \le \frac{t^2\|[A,B]\|}{2r}$. Optimal known scaling for $d$-dimensional lattice Hamiltonians is $O\!\big(nt\,\mathrm{polylog}(nt/\varepsilon)\big)$ gates (Haah–Hastings–Kothari–Low), matching the Lieb–Robinson-derived lower bound $\Omega(nt)$ up to logs. Sparse-Hamiltonian qubitization achieves query complexity $O\!\big(\tau + \log(1/\varepsilon)/\log\log(1/\varepsilon)\big)$ with $\tau = t\,\|H\|_{\max}\,d$ (Low–Chuang 2019), which is optimal in $t$ (no-fast-forwarding theorem, Berry–Ahokas–Cleve–Sanders 2007).

## 3. History & State of the Art

- **1980–82.** Benioff constructs Hamiltonian models of Turing machines. Feynman (*Int. J. Theor. Phys.* 1982) observes that classical simulation of quantum many-body dynamics appears exponentially costly and proposes a "universal quantum simulator."
- **1985.** Deutsch states the **Church–Turing principle**: "Every finitely realizable physical system can be perfectly simulated by a universal model computing machine operating by finite means," and defines the universal quantum computer.
- **1993–97.** Bernstein–Vazirani formalize QTMs, define $\mathsf{BQP}$, prove universality; Yao proves QTM/circuit equivalence; Adleman–DeMarrais–Huang show amplitude set $\{0,\pm\frac35,\pm\frac45,\pm1\}$ suffices.
- **1996.** Lloyd shows local Hamiltonian dynamics is efficiently simulable — the first substantive evidence for the strong form.
- **2002–2012.** Freedman–Kitaev–Wang: simulation of topological quantum field theories is in $\mathsf{BQP}$ (and Jones-polynomial approximation is $\mathsf{BQP}$-complete, Aharonov–Jones–Landau). Jordan–Lee–Preskill (*Science* 2012): scattering amplitudes in $\phi^4$ scalar field theory computable in $\mathsf{BQP}$, including at strong coupling.
- **2015–2021.** Post-Trotter methods (LCU, qubitization, QSP) give near-optimal simulation. Cubitt–Pérez-García–Wolf show the *spectral gap* of a translation-invariant 2D lattice is undecidable — an uncomputability result about an asymptotic (infinite-volume) property, not about finite-time dynamics, so it does not refute QCTT.
- **2019–2024.** Random-circuit sampling (Arute et al., *Nature* 2019) and Gaussian boson sampling (Zhong et al., *Science* 2020) provide experimental evidence for the *converse* direction (quantum beats classical); several claims were later eroded by improved tensor-network spoofing (Pan–Chen–Zhang, *PRL* 2022).

## 4. Partial Results / Verified Cases

Proven in $\mathsf{BQP}$ (strong form holds) for:

1. **$k$-local Hamiltonians**, $k=O(1)$, $m=\mathrm{poly}(n)$ terms: gate cost $\widetilde O(m^2 t^2/\varepsilon)$ (Lloyd 1996), improved to $\widetilde O(nt)$ for $D$-dimensional lattices with finite-range interactions, $D\le 3$ (Haah et al. 2021).
2. **Sparse Hamiltonians** with row-sparsity $d=\mathrm{poly}(n)$ and efficiently computable entries: optimal $O(\tau+\log(1/\varepsilon))$ queries.
3. **Bosonic/fermionic lattice models**: Jordan–Wigner or Bravyi–Kitaev encodings give $O(n)$ overhead per fermionic mode.
4. **Scalar quantum field theory** $\phi^4$ in $d=1,2,3$ spatial dimensions, massive, with lattice cutoff: polynomial in particle number, energy and $1/\varepsilon$ (Jordan–Lee–Preskill 2012); scattering is $\mathsf{BQP}$-complete in $d=1$ (2018).
5. **Topological QFT** (Chern–Simons/Witten invariants at roots of unity) — $\mathsf{BQP}$-complete.
6. **Lattice gauge theories** with compact gauge group and finite truncation of the local Hilbert space: $\mathsf{BQP}$ for $U(1)$, $SU(2)$, $SU(3)$ at fixed cutoff.
7. **Continuous-variable / Gaussian dynamics**: efficiently simulable classically (Bartlett–Sanders–Braunstein–Nemoto), a fortiori in $\mathsf{BQP}$.
8. **Open-system dynamics**: Markovian Lindblad evolution with $\mathrm{poly}(n)$ local jump operators simulable in $\mathrm{poly}$ time (Kliesch et al. 2011).

Non-relativistic quantum mechanics with bounded energy and bounded particle number is therefore fully covered.

## 5. Principal Obstacles

- **No axiomatization of "physics."** The thesis quantifies over a theory that does not yet exist in complete form. Any proof is conditional on an unknown $T$; hence the problem is not formally decidable as stated.
- **Quantum gravity.** No accepted Hamiltonian formulation. Holographic bounds ($S \le A/4G$, Bekenstein) suggest finite-dimensional Hilbert spaces per region — supportive of QCTT — but AdS/CFT bulk reconstruction has known complexity obstructions (Bouland–Fefferman–Vazirani: the "wormhole growth paradox" suggests bulk-boundary dictionary computation may be $\mathsf{PSPACE}$-hard).
- **Continuum and unbounded precision.** Field theories have infinite-dimensional local Hilbert spaces; every simulation result requires a *truncation*, and error bounds are proven only in regimes where truncation error is controlled. Strongly coupled, massless, or chiral theories (chiral fermion doubling; the sign problem's quantum analogue) lack such control.
- **Analytic techniques fail on nonperturbative regimes.** Lieb–Robinson bounds give locality only for finite-range bounded-norm lattice Hamiltonians; they break for relativistic fields with unbounded operators and for long-range $1/r^\alpha$ couplings with $\alpha \le D$.
- **Exotic-but-not-excluded physics.** Abrams–Lloyd (1998) show that *any* nonlinearity in the Schrödinger equation lets one solve $\mathsf{NP}$-complete and even $\\#\mathsf{P}$ problems in polynomial time. Closed timelike curves give $\mathsf{PSPACE}$ (Aaronson–Watrous). Malament–Hogarth spacetimes permit hypercomputation (Etesi–Németi 2002). Each is consistent with *some* mathematically coherent physics; ruling them out requires physical, not mathematical, input.
- **Resource accounting.** Proposed violations usually hide exponential cost in precision, energy density, or measurement duration. There is no agreed formal cost model for "physical resources," so counterexample claims cannot be adjudicated purely mathematically.

## 6. The Gap

Section 4 establishes: *finite-dimensional, bounded-norm, geometrically local (or sparse) Hamiltonian dynamics for polynomial time is in $\mathsf{BQP}$.* Section 1 demands: *all physical processes.* The gap has three components.

1. **From bounded to unbounded operators.** Extend simulation theorems from $\|H\|\le\mathrm{poly}(n)$ to relativistic field Hamiltonians with unbounded spectrum and continuum limits, with error bounds uniform in the cutoff. This is the mathematically sharpest and most tractable piece.
2. **From fixed background to dynamical geometry.** A $\mathsf{BQP}$ simulation theorem for any candidate quantum-gravity dynamics. Currently no formulation is complete enough to state the theorem.
3. **From "consistent theory" to "our world."** Excluding nonlinear QM, CTCs, and hypercomputational spacetimes is an empirical program. Aharonov–Vazirani frame the converse: if QCTT holds, then quantum mechanics for large systems is not efficiently *falsifiable* by a classical experimenter, unless one uses interactive proofs — motivating the $\mathsf{MIP}^*=\mathsf{RE}$ line and single-prover verification protocols (Mahadev 2018).

## 7. Current Research (as of June 2026)

- **Quantum simulation of gauge theories.** Groups at Maryland/JQI (Zohar, Gorshkov), Innsbruck (Zoller, Blatt), Fermilab/IQuS Seattle (Savage), and MIT (Preskill collaborators at Caltech IQIM) push rigorous resource bounds for $SU(2)$/$SU(3)$ with controlled truncation error. Several 2025–26 preprints claim uniform-in-cutoff error bounds for $1{+}1$D QCD *(frontier — verify)*.
- **Complexity of holography.** Bouland–Fefferman–Vazirani and Susskind-school work on whether the AdS/CFT dictionary is efficiently computable; "python's lunch" and pseudorandomness-based obstructions.
- **Verification of quantum advantage.** Mahadev-style classical verification of $\mathsf{BQP}$ under LWE; efficient certified randomness protocols (JPMorgan/Quantinuum 2025 demonstration).
- **Analog-to-digital reduction.** Formal statements that analog quantum simulators (cold atoms, Rydberg arrays) with realistic noise are contained in $\mathsf{BQP}$ — needed because analog devices are the most common candidate "extra-$\mathsf{BQP}$" machines.
- **Classical spoofing.** Tensor-network and Pauli-path simulators repeatedly narrowing claimed advantage, relevant to the empirical support base.

## 8. Future Work

- Prove a **cutoff-uniform simulation theorem** for interacting QFT: gate count $\mathrm{poly}(E, t, 1/\varepsilon)$ independent of lattice spacing, for $\phi^4_{3+1}$ and Yang–Mills with mass gap.
- Establish **$\mathsf{BQP}$-hardness** of scattering in $3{+}1$D, closing the completeness picture.
- Develop a **formal resource model** for physical computation (energy $\times$ time $\times$ spacetime volume $\times$ precision) under which the thesis is a precise mathematical statement, as urged by Aaronson.
- Derive QCTT **as a consequence** of holographic entropy bounds: if any region of radius $R$ carries $\le \pi R^2/(\ell_P^2 \ln 2)$ qubits, the finite-dimensionality premise of Section 4 is automatic.
- Sharpen **experimental exclusion** of Schrödinger nonlinearity; current bounds on the Weinberg nonlinearity parameter are $\sim 10^{-21}$ in fractional energy shift, which already makes Abrams–Lloyd speedups require impractical precision — quantify this trade-off rigorously.

## 9. Key References

- **[Foundational]** R. P. Feynman. *Simulating Physics with Computers.* International Journal of Theoretical Physics **21**(6/7), 467–488, 1982.
- **[Foundational]** D. Deutsch. *Quantum theory, the Church–Turing principle and the universal quantum computer.* Proceedings of the Royal Society of London A **400**, 97–117, 1985.
- **[Foundational]** E. Bernstein, U. Vazirani. *Quantum Complexity Theory.* SIAM Journal on Computing **26**(5), 1411–1473, 1997 (STOC 1993).
- **[Foundational]** A. C.-C. Yao. *Quantum Circuit Complexity.* Proceedings of the 34th FOCS, 352–361, 1993.
- **[Foundational]** S. Lloyd. *Universal Quantum Simulators.* Science **273**, 1073–1078, 1996.
- **[SOTA]** J. Haah, M. Hastings, R. Kothari, G. H. Low. *Quantum Algorithm for Simulating Real Time Evolution of Lattice Hamiltonians.* SIAM Journal on Computing **52**(6), FOCS 2018 special issue, 2021.
- **[SOTA]** G. H. Low, I. L. Chuang. *Hamiltonian Simulation by Qubitization.* Quantum **3**, 163, 2019.
- **[SOTA]** S. P. Jordan, K. S. M. Lee, J. Preskill. *Quantum Algorithms for Quantum Field Theories.* Science **336**, 1130–1133, 2012.
- **[SOTA]** M. Freedman, A. Kitaev, Z. Wang. *Simulation of Topological Field Theories by Quantum Computers.* Communications in Mathematical Physics **227**, 587–603, 2002.
- **[SOTA]** D. Aharonov, W. van Dam, J. Kempe, Z. Landau, S. Lloyd, O. Regev. *Adiabatic Quantum Computation is Equivalent to Standard Quantum Computation.* SIAM Journal on Computing **37**(1), 166–194, 2007.
- **[SOTA]** U. Mahadev. *Classical Verification of Quantum Computations.* Proceedings of the 59th FOCS, 259–267, 2018.
- **[Counterexample analysis]** D. S. Abrams, S. Lloyd. *Nonlinear Quantum Mechanics Implies Polynomial-Time Solution for NP-Complete and \\#P Problems.* Physical Review Letters **81**, 3992, 1998.
- **[Counterexample analysis]** G. Etesi, I. Németi. *Non-Turing Computations via Malament–Hogarth Space-Times.* International Journal of Theoretical Physics **41**, 341–370, 2002.
- **[Survey]** S. Aaronson. *NP-complete Problems and Physical Reality.* ACM SIGACT News **36**(1), 30–52, 2005.
- **[Survey]** D. Aharonov, U. Vazirani. *Is Quantum Mechanics Falsifiable? A Computational Perspective on the Foundations of Quantum Mechanics.* In *Computability: Turing, Gödel, Church, and Beyond* (Copeland, Posy, Shagrir, eds.), MIT Press, 2013.
- **[Survey]** A. W. Harrow, A. Montanaro. *Quantum Computational Supremacy.* Nature **549**, 203–209, 2017.
- **[Related]** T. Cubitt, D. Pérez-García, M. M. Wolf. *Undecidability of the Spectral Gap.* Nature **528**, 207–211, 2015.

## 10. Worked Example / Concrete Special Case

**Task.** Simulate the 1D transverse-field Ising chain on $n$ spins,
$$H = A + B, \qquad A = -J\sum_{i=1}^{n-1} Z_i Z_{i+1}, \qquad B = -h\sum_{i=1}^{n} X_i,$$
for time $t$ to accuracy $\varepsilon$ — a concrete instance of the Section 4 statement.

**Step 1: commutator norm.** $[Z_iZ_{i+1}, X_j]=0$ unless $j\in\{i,i+1\}$, and for those, $\|[Z_iZ_{i+1},X_j]\|=2$. There are $2(n-1)$ nonvanishing pairs, so
$$\|[A,B]\| \le Jh\cdot 2(n-1)\cdot 2 = 4Jh(n-1).$$

**Step 2: Trotter number.** Requiring $\dfrac{t^2\|[A,B]\|}{2r}\le\varepsilon$ gives
$$r \;\ge\; \frac{2Jh(n-1)t^2}{\varepsilon}.$$

**Step 3: gates per step.** $e^{-iAt/r}$ is $n-1$ two-qubit $ZZ$ rotations (each = CNOT, $R_z$, CNOT: 3 gates); $e^{-iBt/r}$ is $n$ single-qubit $R_x$ gates. Total per step: $4n-3$ gates.

**Step 4: numbers.** Take $n=100$, $J=h=1$, $t=10$, $\varepsilon=10^{-3}$:
$$r \ge \frac{2\cdot 99\cdot 100}{10^{-3}} \approx 1.98\times 10^{7}, \qquad \text{gates} \approx 397\cdot r \approx 7.9\times 10^{9}.$$

**Step 5: contrast with the state of the art.** Haah–Hastings–Kothari–Low give $O\!\big(nt\,\mathrm{polylog}(nt/\varepsilon)\big)$: with $nt = 10^3$ and logarithmic factors of order $10^2$, roughly $10^5$ gates — five orders of magnitude better, and provably near-optimal since Lieb–Robinson forces $\Omega(nt)$.

**Step 6: what this does and does not show.** The circuit is polynomial in $n$, $t$, $1/\varepsilon$: QCTT holds for this system, *exactly and constructively*. Now perturb the model: replace $Z_iZ_{i+1}$ by a $1/|i-j|$ long-range coupling, or take the continuum limit $a\to 0$ of the chain toward a free-fermion field theory. In the first case $\|H\|$ grows like $n\log n$ and the Lieb–Robinson cone opens logarithmically — bounds still work but degrade. In the second, the local Hilbert space stays 2-dimensional but the number of sites needed for fixed physical volume diverges as $1/a$, and the error analysis must be redone uniformly in $a$. That last step — uniform-in-cutoff control — is exactly the mathematical gap of Section 6(1), visible already in this two-line Hamiltonian.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*