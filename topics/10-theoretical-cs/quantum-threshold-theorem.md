---
id: 10-theoretical-cs/quantum-threshold-theorem
title: "Quantum Threshold Theorem"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Threshold Theorem

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-threshold-theorem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The quantum threshold theorem (quantum accuracy threshold theorem) asserts:

> There exists a constant $p_{\mathrm{th}} > 0$ such that for any noise rate $p < p_{\mathrm{th}}$ drawn from a specified noise model, any ideal quantum circuit $C$ with $N$ gate locations can be simulated by a noisy circuit $C'$ of size $O\big(N\,\mathrm{polylog}(N/\varepsilon)\big)$ whose output distribution is within total variation distance $\varepsilon$ of that of $C$.

The theorem is **proved** for a well-characterized family of noise models (independent stochastic, local stochastic, and weakly correlated local non-Markovian noise). What remains open is a cluster of quantitative and model-theoretic questions that the community collectively calls "the threshold problem":

1. **Exact threshold value.** Determine $p_{\mathrm{th}}^{\ast} = \sup\{p : \text{fault tolerance is possible at rate } p\}$ for a fixed noise model (say, circuit-level depolarizing noise with two-qubit gates). Rigorous lower bounds and rigorous upper bounds are separated by roughly **four orders of magnitude**.
2. **Model boundary.** Characterize exactly which non-Markovian / correlated noise models admit a threshold. Give a necessary *and* sufficient condition on the decay of spatial and temporal noise correlations.
3. **Overhead optimality.** Determine the minimal space overhead compatible with a threshold, and whether constant-overhead fault tolerance is achievable at the same threshold rate as concatenated schemes.

A complete resolution of (1) requires matching constructive and impossibility bounds; of (2), a correlation-decay criterion with a proof and a matching counterexample; of (3), a lower bound on overhead as a function of $p$.

## 2. Mathematical Foundations

**Circuits and locations.** A quantum circuit is a sequence of *locations* — gate, preparation, measurement, or identity (wait) — acting on qubits in $(\mathbb{C}^2)^{\otimes n}$. Let $\mathcal{L}$ be the location set, $|\mathcal{L}| = N$.

**Local stochastic noise.** A fault path is a subset $S \subseteq \mathcal{L}$ of faulty locations. Noise is *local stochastic with rate $p$* if for every $S_0 \subseteq \mathcal{L}$,
$$\Pr[\,S \supseteq S_0\,] \le p^{|S_0|},$$
with faults at locations in $S$ replaced by arbitrary (adversarial) CPTP maps on the location's support. This subsumes i.i.d. depolarizing noise, where a location fails with a Pauli error drawn uniformly:
$$\mathcal{E}_p(\rho) = (1-p)\rho + \frac{p}{3}\big(X\rho X + Y\rho Y + Z\rho Z\big).$$

**Hamiltonian (non-Markovian) noise.** System $S$ plus bath $B$ evolve under
$$H = H_S(t) + H_B + \sum_{k} H_{SB,k}, \qquad \max_k \lVert H_{SB,k}\rVert \le \eta ,$$
where $H_{SB,k}$ couples a bounded neighborhood of qubits to the bath. The relevant dimensionless parameter is $\eta\,\tau$ ($\tau$ = gate time); a threshold $\eta_0$ is claimed for $\eta\tau < \eta_0$.

**Stabilizer codes.** An $[[n,k,d]]$ code is the joint $+1$ eigenspace of an abelian subgroup $\mathcal{S} \le \mathcal{P}_n$ with $-I \notin \mathcal{S}$; $d$ is the minimum weight of a Pauli in $\mathcal{N}(\mathcal{S})\setminus \mathcal{S}$. A distance-$d$ code corrects $t = \lfloor (d-1)/2\rfloor$ arbitrary single-qubit errors.

**Concatenation recursion.** For a distance-3 code with $A$ *malignant fault pairs* per extended rectangle (exRec), the level-$L$ effective error rate obeys
$$p_L \le \frac{1}{A}\,(A p)^{2^{L}} ,$$
so $p_{\mathrm{th}} \ge 1/A$, and reaching target error $\varepsilon$ needs
$$L = \Big\lceil \log_2 \frac{\log(1/A\varepsilon)}{\log(1/Ap)} \Big\rceil = O(\log\log(1/\varepsilon)),$$
giving overhead $n^{L} = \mathrm{polylog}(1/\varepsilon)$ per qubit.

**Key structural tools.** (i) *Level reduction* and the exRec formalism of Aliferis–Gottesman–Preskill, converting a noisy level-$L$ circuit into an effectively noisy level-$(L-1)$ circuit; (ii) *transversality* — the Eastin–Knill theorem forbids a transversal universal gate set for any code detecting single-qubit errors, forcing magic-state distillation; (iii) the *topological* route, where the surface code's threshold maps to a phase transition of the random-bond Ising model on the Nishimori line.

## 3. History & State of the Art (SOTA)

- **1995–96.** Shor's 9-qubit code and Steane's $[[7,1,3]]$ code establish that quantum information is protectable at all; Shor (1996) gives the first fault-tolerant procedures.
- **1996–98.** Independent proofs of a threshold: Aharonov–Ben-Or (STOC 1997; SIAM J. Comput. 2008), Kitaev (1997), Knill–Laflamme–Zurek (*Science* 1998; *Proc. R. Soc. A* 1998). Knill–Laflamme–Zurek estimate $p_{\mathrm{th}} \sim 10^{-4}$–$10^{-3}$.
- **1997–2003.** Kitaev's toric/surface code introduces the topological approach; Dennis–Kitaev–Landahl–Preskill (2002) compute the code-capacity threshold $\approx 10.9\%$ via the random-bond Ising Nishimori point.
- **2005–06.** Rigorous, gap-free proofs with explicit constants: Aliferis–Gottesman–Preskill prove $p_{\mathrm{th}} \ge 2.73\times10^{-5}$ for local stochastic noise with the concatenated $[[7,1,3]]$ code. Terhal–Burkard and Aharonov–Kitaev–Preskill extend the theorem to non-Markovian, local-in-time Hamiltonian baths.
- **2007.** Raussendorf–Harrington obtain a $\approx 0.75\%$ numerical threshold for 3D topological (measurement-based) fault tolerance with only nearest-neighbor gates in 2D; Knill reports $\sim 3\%$ for postselection-heavy schemes with enormous overhead.
- **2004–08.** Impossibility side: Razborov shows no threshold above $1 - 1/k$ for $k$-qubit gates; Buhrman et al. and Kempe–Regev–Unger–de Wolf push the depolarizing upper bound down to $\approx 29.3\%$.
- **2014–18.** Gottesman shows constant space overhead is achievable with quantum LDPC codes; Fawzi–Grospellier–Leverrier give an efficient single-shot decoder for quantum expander codes with a threshold.
- **2024–25.** Google Quantum AI reports surface-code memory operating *below* threshold, with logical error suppressed by $\Lambda \approx 2.14$ per distance step from $d=3$ to $d=7$ (*Nature*, 2025) — the first experimental demonstration on the correct side of the threshold.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| Local stochastic, concatenated $[[7,1,3]]$ | $p_{\mathrm{th}} \ge 2.73\times 10^{-5}$ (rigorous) | Aliferis–Gottesman–Preskill 2006 |
| Local stochastic, Bacon–Shor subsystem code | $p_{\mathrm{th}} \ge 1.94\times 10^{-4}$ (rigorous) | Aliferis–Cross 2007 |
| Non-Markovian, local bath couplings | threshold in $\eta\tau$ exists | Terhal–Burkard 2005; Aharonov–Kitaev–Preskill 2006 |
| Correlated noise, power-law decay | threshold if correlation strength decays fast enough with distance | Preskill 2013 |
| 1D nearest-neighbor architecture | threshold exists (polylog overhead) | Gottesman 2000 |
| 2D nearest-neighbor, surface code | numerical $p_{\mathrm{th}} \approx 0.57\%$–$1.1\%$ (circuit-level) | Raussendorf–Harrington 2007; Fowler et al. 2012 |
| Surface code, code capacity (perfect syndromes) | $p_{\mathrm{th}} = 10.93(2)\%$ (Nishimori point) | Dennis et al. 2002; Wang–Harrington–Preskill 2003 |
| Erasure (located loss) errors, surface code | $p_{\mathrm{th}} = 50\%$ (bond percolation) | Stace–Barrett–Doherty 2009 |
| Upper bound, depolarizing, 2-qubit gates | no threshold above $\approx 29.3\%$ | Kempe–Regev–Unger–de Wolf 2008 |
| Upper bound, $k$-qubit gates | no threshold above $1 - 1/k$ | Razborov 2004 |
| Constant space overhead | achievable with qLDPC codes, threshold $>0$ | Gottesman 2014; Fawzi–Grospellier–Leverrier 2018 |

## 5. Principal Obstacles

- **Combinatorial explosion in rigorous counting.** Lower bounds come from bounding the number $A$ of malignant fault pairs in an exRec. For the Steane exRec, $A$ is in the tens of thousands; exhaustive enumeration is done by computer and is dominated by pessimistic worst-case assumptions (any fault pair that *could* cause a logical error is counted as if it does). Making the count tight requires case analysis that grows super-exponentially with code distance, so rigorous bounds stall near $10^{-4}$ while Monte Carlo says $10^{-2}$.
- **Adversarial vs. average-case gap.** Local stochastic noise allows the adversary to choose the CPTP map at faulty locations. Numerical thresholds assume Pauli (or depolarizing) noise, where the decoder can be analyzed as a classical statistical-mechanics model. There is no known reduction converting an average-case Pauli threshold into an adversarial-CPTP threshold without losing constants.
- **Non-Markovian analysis is norm-based, hence lossy.** Hamiltonian-noise proofs expand the Dyson series and bound each term by $\lVert H_{SB}\rVert$. This discards phase cancellation entirely, so a bath that is physically benign (e.g. $1/f$ dephasing with long correlation time) is treated as worst-case. No proof technique currently exploits bath spectral structure to recover a competitive constant.
- **Coherent error accumulation.** Systematic over-rotations add in amplitude, not probability: $L$ repetitions of a rotation error $\theta$ give error $\sim (L\theta)^2$ rather than $L\theta^2$. Pauli-twirling arguments convert coherent to stochastic noise only after averaging, and the twirl itself costs gates.
- **Upper bounds are simulation-based.** Impossibility proofs work by showing the noisy circuit becomes classically simulable (its output is a product of local depolarized states, or a shallow-light-cone object). These arguments need noise so strong that entanglement is destroyed outright — around $30\%$ — and provide no leverage at $1\%$.
- **Eastin–Knill barrier.** No code with a transversal universal gate set exists, so every scheme needs a distillation or code-switching gadget whose own threshold must be analyzed separately; the overall threshold is set by the worst gadget, usually the non-Clifford one.

## 6. The Gap

The proved statement is: *for local stochastic noise with $p < 2.73\times10^{-5}$ (or $1.94\times10^{-4}$ with Bacon–Shor), scalable quantum computation exists.* The impossibility statement is: *for depolarizing noise with $p > 0.293$, it does not.* Between $2\times10^{-4}$ and $0.29$ — a factor of $\sim 1500$ — the question is undecided by proof; simulation says the true value for standard 2D architectures is near $1\%$.

Crossing the gap requires one of:

- **From below:** a proof technique that tracks the *distribution* of fault configurations rather than union-bounding over malignant sets — i.e. a rigorous percolation or statistical-mechanics argument for circuit-level (not code-capacity) noise, including measurement errors and gate-induced correlations. Equivalently, a rigorous proof that the 3D random-plaquette gauge model's Nishimori-line transition controls the circuit-level surface-code threshold.
- **From above:** an impossibility argument valid at small $p$, which would have to exhibit an obstruction other than classical simulability — none is known, and many believe none exists below $\sim 10\%$.
- **For the model boundary:** a sharp correlation-decay exponent $\alpha^{\ast}$ such that bath couplings decaying as $r^{-\alpha}$ admit a threshold iff $\alpha > \alpha^{\ast}$. Preskill (2013) gives a sufficient condition; the matching counterexample is missing.

## 7. Current Research (as of June 2026)

- **qLDPC fault tolerance.** Bivariate bicycle codes (IBM, 2024) achieve $[[144,12,12]]$ with weight-6 checks and a numerical circuit-level threshold near $0.7\%$ at $\sim 1/10$ the qubit cost of the surface code. Rigorous threshold proofs for these specific families remain incomplete *(frontier — verify)*.
- **Single-shot and soundness.** Work on 3D/4D homological and quantum expander codes aims at thresholds without repeated syndrome extraction, using the confinement property of the code (Bombín; Campbell; Fawzi–Grospellier–Leverrier lineage).
- **Coherent-noise thresholds.** Analytic treatments of rotation errors via free-fermion/Majorana mappings for the repetition and surface codes, quantifying when the coherent threshold is strictly worse than the Pauli one.
- **Erasure-biased hardware.** Dual-rail superconducting and neutral-atom platforms convert most errors into detected erasures, raising thresholds toward the percolation limits (Yale, AWS, Harvard/QuEra groups).
- **Experimental below-threshold operation.** Google's $d=7$ surface-code memory and subsequent scaling; neutral-atom logical-qubit arrays (Harvard/MIT/QuEra). These are demonstrations, not proofs, but they pin the empirical threshold near $0.5$–$1\%$.
- **Institutions.** Caltech IQIM, Perimeter/IQC Waterloo, IBM Research, Google Quantum AI, Delft QuTech, Sydney, Yale, Inria Paris (Leverrier group).

## 8. Future Work

- Develop a *rigorous statistical-mechanics* proof of the circuit-level surface-code threshold, replacing malignant-set counting with a proof of the disorder-averaged free-energy cost of a homologically nontrivial defect.
- Establish tight overhead lower bounds: prove or refute that $\Omega(\log(1/\varepsilon))$ space overhead is necessary at fixed $p$ close to $p_{\mathrm{th}}$.
- Find a necessary-and-sufficient correlation condition for non-Markovian thresholds; construct an explicit bath with slowly decaying correlations that provably defeats all fault-tolerant schemes.
- Close the coherent-error question: is there a code family whose threshold under arbitrary unitary (non-Pauli) local errors matches its Pauli threshold up to constants?
- Push impossibility bounds below $10\%$ using entanglement- or magic-monotone arguments rather than classical simulability.

## 9. Key References

- **[Foundational]** P. W. Shor. *Fault-tolerant quantum computation.* Proc. 37th Annual Symposium on Foundations of Computer Science (FOCS), 1996.
- **[Foundational]** D. Aharonov, M. Ben-Or. *Fault-Tolerant Quantum Computation with Constant Error Rate.* SIAM Journal on Computing 38(4):1207–1282, 2008 (conference version STOC 1997).
- **[Foundational]** E. Knill, R. Laflamme, W. H. Zurek. *Resilient Quantum Computation.* Science 279:342–345, 1998.
- **[Foundational]** A. Yu. Kitaev. *Quantum computations: algorithms and error correction.* Russian Mathematical Surveys 52(6):1191–1249, 1997.
- **[Foundational]** A. Yu. Kitaev. *Fault-tolerant quantum computation by anyons.* Annals of Physics 303(1):2–30, 2003.
- **[SOTA]** P. Aliferis, D. Gottesman, J. Preskill. *Quantum accuracy threshold for concatenated distance-3 codes.* Quantum Information and Computation 6(2):97–165, 2006.
- **[SOTA]** P. Aliferis, A. W. Cross. *Subsystem fault tolerance with the Bacon-Shor code.* Physical Review Letters 98:220502, 2007.
- **[SOTA]** E. Dennis, A. Kitaev, A. Landahl, J. Preskill. *Topological quantum memory.* Journal of Mathematical Physics 43:4452–4505, 2002.
- **[SOTA]** R. Raussendorf, J. Harrington. *Fault-tolerant quantum computation with high threshold in two dimensions.* Physical Review Letters 98:190504, 2007.
- **[SOTA]** A. G. Fowler, M. Mariantoni, J. M. Martinis, A. N. Cleland. *Surface codes: Towards practical large-scale quantum computation.* Physical Review A 86:032324, 2012.
- **[SOTA]** D. Gottesman. *Fault-tolerant quantum computation with constant overhead.* Quantum Information and Computation 14(15–16):1338–1372, 2014.
- **[SOTA]** O. Fawzi, A. Grospellier, A. Leverrier. *Constant overhead quantum fault-tolerance with quantum expander codes.* Proc. 59th IEEE FOCS, 2018.
- **[Upper bounds]** A. A. Razborov. *An upper bound on the threshold quantum decoherence rate.* Quantum Information and Computation 4(3):222–228, 2004.
- **[Upper bounds]** J. Kempe, O. Regev, F. Unger, R. de Wolf. *Upper bounds on the noise threshold for fault-tolerant quantum computing.* Proc. ICALP, LNCS 5125, 2008.
- **[Noise models]** B. M. Terhal, G. Burkard. *Fault-tolerant quantum computation for local non-Markovian noise.* Physical Review A 71:012336, 2005.
- **[Noise models]** D. Aharonov, A. Kitaev, J. Preskill. *Fault-tolerant quantum computation with long-range correlated noise.* Physical Review Letters 96:050504, 2006.
- **[Noise models]** J. Preskill. *Sufficient condition on noise correlations for scalable quantum computing.* Quantum Information and Computation 13(3–4):181–194, 2013.
- **[Structural]** B. Eastin, E. Knill. *Restrictions on transversal encoded quantum gate sets.* Physical Review Letters 102:110502, 2009.
- **[Experimental]** Google Quantum AI and Collaborators. *Quantum error correction below the surface code threshold.* Nature 638:920–926, 2025.
- **[Survey]** D. Gottesman. *An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation.* In Quantum Information Science and Its Contributions to Mathematics, Proc. Symposia in Applied Mathematics 68, AMS, 2010.
- **[Survey]** B. M. Terhal. *Quantum error correction for quantum memories.* Reviews of Modern Physics 87:307, 2015.

## 10. Worked Example / Concrete Special Case

**Step 1 — the simplest recursion.** Take the 3-qubit repetition code $\{|000\rangle, |111\rangle\}$ against independent bit flips of rate $p$, with perfect encoding, syndrome extraction and decoding. Majority decoding fails iff two or three physical qubits flip:
$$p_L = 3p^2(1-p) + p^3 = 3p^2 - 2p^3 .$$
Solving $p_L = p$ gives the fixed points $p \in \{0, \tfrac12, 1\}$. So $p_L < p$ exactly when $p < 1/2$: the code-capacity threshold is $p_{\mathrm{th}} = 1/2$, and iterating the map drives $p_L \to 0$ doubly exponentially.

**Step 2 — where the idealization breaks.** Real syndrome extraction uses CNOTs and ancillas that are themselves noisy. Charging error rate $p$ to *every* location and letting a single fault propagate through the two CNOTs of a syndrome circuit, the recursion becomes $p_L \le A p^2$ with $A$ the number of malignant fault *pairs* in the extended rectangle. The threshold collapses from $1/2$ to $1/A$. For the concatenated Steane $[[7,1,3]]$ code with the AGP counting, $A \approx 10^4$, hence the rigorous $p_{\mathrm{th}} \gtrsim 2.73\times10^{-5}$.

**Step 3 — overhead accounting.** Take $A = 10^4$ and physical rate $p = 10^{-6}$, so $Ap = 10^{-2}$. The level-$L$ logical rate is
$$p_L \le \frac{1}{A}(Ap)^{2^L} = 10^{-4}\cdot 10^{-2\cdot 2^{L}} .$$
To run a circuit with $N = 10^{12}$ locations we need $p_L \lesssim 10^{-15}$:
$$10^{-4-2^{L+1}} \le 10^{-15} \iff 2^{L+1} \ge 11 \iff L = 3 .$$
Three levels of Steane concatenation use $7^3 = 343$ physical qubits per logical qubit (and $p_3 \le 10^{-4-16} = 10^{-20}$, comfortably sufficient). Note the doubly exponential suppression: $L=4$ would give $10^{-36}$ for $7^4 = 2401$ qubits.

**Step 4 — the gap made concrete.** Set $p = 10^{-3}$ instead. Then $Ap = 10 > 1$ and the rigorous recursion *diverges*: the proof gives nothing. Yet Monte Carlo simulation of the surface code at circuit-level depolarizing rate $10^{-3}$ shows logical error decreasing by a factor $\Lambda \approx 2$ per two units of code distance, and Google's hardware confirms this experimentally. The mathematical content of the open problem is exactly this discrepancy: the analytic recursion is loose by a factor of $\sim 10^3$ in $p$, because it union-bounds over malignant sets instead of computing the true probability that the decoder's homology class is wrong.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*