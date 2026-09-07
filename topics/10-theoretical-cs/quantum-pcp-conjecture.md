---
id: 10-theoretical-cs/quantum-pcp-conjecture
title: "Quantum PCP Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum PCP Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-pcp-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The classical PCP theorem (Arora–Safra; Arora–Lund–Motwani–Sudan–Szegedy, 1998) says that approximating MAX-3SAT to within a constant factor is NP-hard. The **quantum PCP conjecture (qPCP)** is the assertion that the same phenomenon holds for the quantum analogue of constraint satisfaction, the **local Hamiltonian problem**.

**Conjecture (constraint-satisfaction form).** There exist constants $k \in \mathbb{N}$ and $\alpha > 0$ such that the following promise problem is QMA-hard: given a $k$-local Hamiltonian $H = \frac{1}{m}\sum_{i=1}^{m} H_i$ on $n$ qubits with $0 \preceq H_i \preceq I$, decide whether $\lambda_{\min}(H) = 0$ or $\lambda_{\min}(H) \ge \alpha$.

Equivalently: **QMA-hardness survives at constant promise gap** (constant *relative* error), where Kitaev's original hardness holds only at gap $1/\mathrm{poly}(n)$.

A proof would exhibit a gap-amplification or quantum-proof-composition procedure mapping any QMA instance to a constant-gap one in polynomial time. A disproof would give a polynomial-time (or $\mathsf{NP}$-verifiable) algorithm estimating $\lambda_{\min}(H)$ to within $\alpha m$ for all local Hamiltonians, collapsing the constant-gap problem to $\mathsf{NP}$ (or below) unless $\mathsf{QMA} = \mathsf{NP}$.

## 2. Mathematical Foundations

**Local Hamiltonians.** Fix Hilbert space $\mathcal{H} = (\mathbb{C}^{d})^{\otimes n}$. A term $H_i$ is *$k$-local* if it acts nontrivially on at most $k$ qudits. The instance is a *quantum CSP*; the *ground energy* is
$$\lambda_{\min}(H) = \min_{\|\psi\|=1} \langle \psi | H | \psi \rangle = \min_{\rho \succeq 0,\ \mathrm{tr}\rho = 1} \mathrm{tr}(H\rho).$$
The *unsatisfied fraction* of a state is $\varepsilon(\psi) = \langle\psi|H|\psi\rangle$ under the normalization $H = \frac1m\sum_i H_i$, $0\preceq H_i \preceq I$.

**Kitaev's theorem.** $k$-LOCAL-HAMILTONIAN with $k\ge 2$ and promise gap $b - a \ge 1/\mathrm{poly}(n)$ is QMA-complete (Kitaev 1999; $k=2$ by Kempe–Kitaev–Regev 2006). The circuit-to-Hamiltonian map sends a verifier circuit $U_T\cdots U_1$ to the *history state*
$$|\eta\rangle = \frac{1}{\sqrt{T+1}}\sum_{t=0}^{T} U_t\cdots U_1|\xi\rangle \otimes |t\rangle_{\text{clock}},$$
with $H = H_{\text{in}} + H_{\text{out}} + H_{\text{prop}}$, $H_{\text{prop}} = \sum_t \frac12\big(|t\rangle\langle t| + |t{+}1\rangle\langle t{+}1| - U_{t+1}\otimes|t{+}1\rangle\langle t| - U_{t+1}^\dagger\otimes|t\rangle\langle t{+}1|\big)$. The $1/T$ weight of each clock step is exactly why the gap is only $\Omega(1/T^{3})$ after normalization.

**qPCP, proof-verification form.** $\mathsf{QMA} = \mathsf{QPCP}[\log n, O(1)]$: every $L\in\mathsf{QMA}$ has a verifier reading $O(1)$ qubits of a polynomial-size quantum proof (chosen using $O(\log n)$ random bits), with completeness $\ge 2/3$ and soundness $\le 1/3$. This is equivalent to the constraint form above.

**NLTS (no low-energy trivial states).** A family $\{H_n\}$ of $k$-local Hamiltonians on bounded-degree interaction graphs is **NLTS** with parameter $\varepsilon>0$ if there is no family of states $|\psi_n\rangle$ with
$$\langle\psi_n|H_n|\psi_n\rangle \le \lambda_{\min}(H_n) + \varepsilon m, \qquad |\psi_n\rangle = V_n|0^n\rangle,\ \mathrm{depth}(V_n) = O(1).$$
**Lemma (Freedman–Hastings 2014).** qPCP $\Rightarrow$ NLTS, unless $\mathsf{QMA}\subseteq\mathsf{NP}$: constant-depth states admit polynomial-size classical descriptions of all local marginals, so their energies are $\mathsf{NP}$-certifiable.

**Mean-field / product-state benchmark.** $\lambda_{\min}^{\mathrm{prod}}(H) = \min_{\rho_1\otimes\cdots\otimes\rho_n}\mathrm{tr}(H\rho)$ is an $\mathsf{NP}$ quantity. Any theorem showing $\lambda_{\min}^{\mathrm{prod}} - \lambda_{\min} = o(m)$ for a class of Hamiltonians is a *no-go* for qPCP on that class.

## 3. History & State of the Art (SOTA)

- **1999.** Kitaev proves LOCAL-HAMILTONIAN is QMA-complete with inverse-polynomial gap — the quantum Cook–Levin theorem.
- **2006–2009.** Aharonov–Naveh and Aharonov–Arad–Landau–Vazirani frame the constant-gap question; the *detectability lemma* (AALV 2009) yields a quantum analogue of Dinur's gap amplification step — the gap improves by a constant factor, but locality and degree grow, so the amplification cannot be iterated. No quantum alphabet/degree reduction is known.
- **2013.** Aharonov, Arad and Vidick publish the canonical survey, fixing the modern formulations and the map of no-go results.
- **2014.** Freedman–Hastings isolate **NLTS** as the minimal structural consequence of qPCP.
- **2018–2020.** The *games* variant is settled in the affirmative and far beyond: Natarajan–Vidick prove $\mathsf{NEEXP}\subseteq\mathsf{MIP}^*$ via quantum low-degree testing, and Ji–Natarajan–Vidick–Wright–Yuen prove $\mathsf{MIP}^*=\mathsf{RE}$. This gives a "quantum games PCP" but *not* the Hamiltonian (qPCP) statement, because entangled-prover soundness does not bound the ground energy of a bounded-size system.
- **2022–2023.** **Anshu, Breuckmann and Nirkhe prove the NLTS theorem**, using good quantum LDPC codes (Panteleev–Kalachev 2022) as the Hamiltonian family. This removes the main structural obstruction to qPCP.
- **2024–2026.** Attention moves to *quantum locally testable codes* (qLTC) with constant soundness, rate and distance — widely viewed as the missing combinatorial object for a qPCP proof — and to sharpening no-go algorithms.

## 4. Partial Results / Verified Cases

**Proved (positive direction).**
- **NLTS theorem** (Anshu–Breuckmann–Nirkhe, STOC 2023): explicit families of $O(1)$-local, bounded-degree Hamiltonians from $[[n, \Theta(n), \Theta(n)]]$ qLDPC codes, with $\varepsilon$ a fixed constant. Circuits of depth $o(\log n)$ cannot reach energy density $\le \varepsilon$.
- **NLETS** (Eldar–Harrow, FOCS 2017): a weaker "no low-error trivial states" family, proved before NLTS.
- **NLSS** (no low-energy *stabilizer* states) established for qLDPC-based families, ruling out a further natural class of $\mathsf{NP}$ witnesses *(frontier — verify)*.
- **Games PCP:** $\mathsf{MIP}^*=\mathsf{RE}$ (JNVWY 2020) — a complete PCP-style theorem for entangled multiprover interactive proofs.
- **Gap amplification, one step:** detectability-lemma amplification (AALV 2009) raises gap $\alpha \to c\alpha$ at the cost of increased locality.

**Proved (no-go direction — classes where constant-gap approximation is easy).**
- **Dense instances:** 2-local Hamiltonians on graphs with $\Omega(n^2)$ edges admit a PTAS via product states (Gharibian–Kempe 2012; Brandão–Harrow 2016).
- **High degree:** for 2-local $H$ on a $D$-regular graph, $\lambda_{\min}^{\mathrm{prod}} - \lambda_{\min} = O(m\,d^{3}/D^{1/3})$ (Brandão–Harrow 2016), so no qPCP-hard family can have degree growing with $n$ at fixed locality.
- **Bounded-degree planar / low-threshold-rank graphs:** product states are near-optimal; PTAS exists (Brandão–Harrow 2016; Bansal–Bravyi–Terhal 2009 for planar quantum Ising).
- **2-local, low-degree:** Arad (2011) gives a poly-time approximation to within relative error $O(D^{-1/3})$-type factors, ruling out qPCP for 2-local Hamiltonians at $k=2$ unless the constants are re-tuned.
- **Commuting Hamiltonians:** 2-local commuting is in $\mathsf{NP}$ (Bravyi–Vyalyi 2003); 3-local commuting on qubits and 4-local on a plane are in $\mathsf{NP}$ (Aharonov–Eldar 2011; Schuch 2011). Hastings (2013) shows commuting Hamiltonians with topological-order-free structure have trivial low-energy states.
- **qLDPC-code Hamiltonians:** a polynomial-time constant-relative-error energy estimator exists for the very code families used to prove NLTS *(frontier — verify; Anshu–Breuckmann–Tang, 2024)*, showing NLTS alone is far from sufficient.

## 5. Principal Obstacles

- **No quantum alphabet/degree reduction.** Dinur's classical proof alternates (i) degree reduction by expanderization, (ii) gap amplification by graph powering, (iii) alphabet reduction by proof composition. Steps (i) and (iii) require *copying* the assignment onto many locations. The no-cloning theorem forbids the direct quantum analogue; the detectability lemma supplies only (ii).
- **No local-to-global correction of quantum witnesses.** Classical PCP soundness rests on local testability of encodings (Hadamard, low-degree, Reed–Muller). The quantum analogue — a **qLTC with constant rate, distance and soundness** — is not known to exist. Chain-complex constructions that give good qLDPC codes have soundness decaying with $n$.
- **Entanglement is bounded by the same locality that defines the problem.** Brandão–Harrow's monogamy/de Finetti argument shows that on high-degree or low-threshold-rank interaction graphs the ground state is *mean-field*: entanglement must be spread thinly, and the product-state energy is within $o(m)$. Any hard family therefore lives in a narrow window: bounded degree, high girth-like expansion, non-commuting terms.
- **Robust entanglement vs. thermal stability.** Freedman–Hastings' intuition — hard instances need entanglement robust to constant energy density — collides with results that at any constant temperature many local models have efficiently describable Gibbs states.
- **Proof composition needs a quantum "assignment tester."** Composing a QMA verifier inside another requires simulating a quantum verifier on a quantum witness with $O(1)$ queries; no candidate quantum PCP of proximity is known.

## 6. The Gap

Proven: (a) hardness at gap $1/\mathrm{poly}(n)$; (b) NLTS — no *constant-depth-circuit* witness at constant energy density; (c) constant-gap PCP for *interactive games with entangled provers*.

Conjectured: hardness at gap $\Omega(1)$ for a *single bounded-size* Hamiltonian.

The precise missing step is a **gap-amplification-preserving encoding**: a map $H \mapsto H'$, poly-time computable, with $H'$ $O(1)$-local on a bounded-degree graph, such that $\lambda_{\min}(H)=0 \Rightarrow \lambda_{\min}(H')=0$ and $\lambda_{\min}(H)\ge \delta \Rightarrow \lambda_{\min}(H') \ge \alpha$ for a fixed $\alpha$ independent of $\delta$. Equivalently, on the coding side: a family of $[[n,k,d]]$ **quantum locally testable codes with $k,d = \Theta(n)$, $O(1)$ locality and $\Omega(1)$ soundness**, plus a way to *compute* inside such codes. NLTS supplies only the "hard witness exists" half; it says nothing about hardness of *deciding*, as the qLDPC no-go result illustrates.

## 7. Current Research (as of June 2026)

- **qLTC program.** High-dimensional expanders and cubical/sheaf complexes are the leading route; Dinur–Lin–Vidick (FOCS 2024) construct qLTCs with improved soundness–distance trade-offs from expanding cubical complexes, still short of the $c^3$ regime *(frontier — verify)*. Groups: Weizmann (Dinur), Caltech/Weizmann (Vidick), TU Delft/Munich (Breuckmann), Bordeaux (Leverrier, Zémor).
- **Sharpening the no-go frontier.** Anshu, Breuckmann and collaborators push polynomial-time energy estimators to broader qLDPC and expander-based families, mapping out which structures *cannot* witness qPCP *(frontier — verify)*.
- **NLTS strengthenings.** Beyond constant depth: ruling out $\mathrm{polylog}$-depth, stabilizer, matrix-product and neural-network witnesses; each closes another candidate $\mathsf{NP}$ witness class.
- **Games-to-Hamiltonians transfer.** Attempts to compile $\mathsf{MIP}^*$ soundness into single-system Hamiltonian hardness (via cryptographic compilation, Kalai–Lombardi–Vaikuntanathan-style) yield *computational* rather than information-theoretic hardness; whether this can give qPCP-like statements under $\mathsf{LWE}$ is actively debated.
- **Physics side.** Consequences for the quantum PCP-vs-thermalization question: qPCP would imply local Hamiltonians whose low-temperature physics is computationally intractable to describe, tension with ETH-based expectations.

## 8. Future Work

1. **Construct $c^3$-qLTCs** (constant rate, distance, soundness). Widely regarded (Aharonov–Eldar; Dinur) as necessary, plausibly close to sufficient, for a qPCP proof.
2. **Develop a quantum proof-composition theorem** — a quantum PCP of proximity, likely via self-testing ideas imported from the $\mathsf{MIP}^*$ line.
3. **Prove or refute qPCP for commuting Hamiltonians** (the "commuting qPCP" conjecture), where no-cloning is less of an obstruction and the problem is combinatorial/homological.
4. **Push no-gos to their limit.** Determine whether every bounded-degree $k$-local family with $k \le 3$ admits a constant-relative-error classical estimator; a positive answer would force any hard family to $k\ge 4$.
5. **Quantify the amplification barrier.** Prove that detectability-lemma amplification provably cannot be iterated without degree blow-up — a formal barrier theorem, analogous to relativization/natural proofs.

## 9. Key References

- **[Foundational]** A. Yu. Kitaev, A. H. Shen, M. N. Vyalyi. *Classical and Quantum Computation.* Graduate Studies in Mathematics 47, American Mathematical Society, 2002.
- **[Foundational]** S. Arora, S. Safra. *Probabilistic Checking of Proofs: A New Characterization of NP.* Journal of the ACM 45(1):70–122, 1998.
- **[Foundational]** I. Dinur. *The PCP Theorem by Gap Amplification.* Journal of the ACM 54(3):12, 2007.
- **[Survey]** D. Aharonov, I. Arad, T. Vidick. *Guest Column: The Quantum PCP Conjecture.* ACM SIGACT News 44(2):47–79, 2013.
- **[Foundational]** D. Aharonov, I. Arad, Z. Landau, U. Vazirani. *The Detectability Lemma and Quantum Gap Amplification.* STOC 2009, pp. 417–426.
- **[Structural]** M. H. Freedman, M. B. Hastings. *Quantum Systems on Non-$k$-Hyperfinite Complexes: A Generalization of Classical Statistical Mechanics on Expander Graphs.* Quantum Information & Computation 14(1–2):144–180, 2014.
- **[SOTA]** A. Anshu, N. P. Breuckmann, C. Nirkhe. *NLTS Hamiltonians from Good Quantum Codes.* STOC 2023, pp. 1090–1096.
- **[SOTA]** P. Panteleev, G. Kalachev. *Asymptotically Good Quantum and Locally Testable Classical LDPC Codes.* STOC 2022, pp. 375–388.
- **[No-go]** F. G. S. L. Brandão, A. W. Harrow. *Product-State Approximations to Quantum States.* Communications in Mathematical Physics 342(1):47–80, 2016.
- **[No-go]** S. Bravyi, M. Vyalyi. *Commutative Version of the Local Hamiltonian Problem and Common Eigenspace Problem.* Quantum Information & Computation 5(3):187–215, 2005.
- **[Related]** Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen. *MIP\* = RE.* Communications of the ACM 64(11):131–138, 2021.
- **[Related]** L. Eldar, A. W. Harrow. *Local Hamiltonians Whose Ground States Are Hard to Approximate.* FOCS 2017, pp. 427–438.
- **[Codes]** D. Aharonov, L. Eldar. *Quantum Locally Testable Codes.* SIAM Journal on Computing 44(5):1230–1262, 2015.

## 10. Worked Example / Concrete Special Case

**Instance.** Three qubits on a triangle, antiferromagnetic Heisenberg terms:
$$H = \frac{1}{3}\sum_{1\le i<j\le 3} \vec S_i\cdot \vec S_j, \qquad \vec S = \tfrac12(\sigma^x,\sigma^y,\sigma^z).$$

**Exact ground energy.** Using $\sum_{i<j}\vec S_i\cdot\vec S_j = \tfrac12\big(S_{\text{tot}}^2 - \sum_i \vec S_i^2\big) = \tfrac12\big(S_{\text{tot}}^2 - \tfrac94\big)$, and $S_{\text{tot}}^2 \in \{\tfrac{15}{4}\ (S=\tfrac32),\ \tfrac34\ (S=\tfrac12)\}$, the minimum is at $S=\tfrac12$:
$$\sum_{i<j}\vec S_i\cdot\vec S_j = \tfrac12\big(\tfrac34-\tfrac94\big) = -\tfrac34 \quad\Longrightarrow\quad \lambda_{\min}(H) = -\tfrac14 .$$
The minimizer is a two-dimensional entangled doublet, e.g. $|\psi\rangle = \tfrac{1}{\sqrt2}(|01\rangle-|10\rangle)\otimes|0\rangle$ symmetrized — genuinely non-product.

**Best product state.** For $\rho = \rho_1\otimes\rho_2\otimes\rho_3$, $\langle \vec S_i\cdot\vec S_j\rangle = \tfrac14 \hat n_i\cdot\hat n_j$ with $|\hat n_i|\le 1$. Minimizing $\sum_{i<j}\hat n_i\cdot\hat n_j$ over unit vectors gives the coplanar $120^\circ$ configuration, $\hat n_i\cdot\hat n_j = -\tfrac12$:
$$\lambda_{\min}^{\mathrm{prod}}(H) = \tfrac13\cdot 3\cdot\tfrac14\cdot\left(-\tfrac12\right) = -\tfrac18 .$$

**Reading.** The relative advantage of entanglement is
$$\frac{\lambda_{\min}^{\mathrm{prod}} - \lambda_{\min}}{\|H\|_{\text{norm}}} = -\tfrac18 - \left(-\tfrac14\right) = \tfrac18,$$
a *constant* energy-density gap between the $\mathsf{NP}$-checkable mean-field value and the true ground energy. qPCP asserts that families with such a constant gap exist *and* that closing it is QMA-hard. The counterweight is Brandão–Harrow: extend this triangle to a $D$-regular frustrated graph and the gap shrinks like $O(D^{-1/3})$, so the mean-field certificate becomes accurate. Any proof of qPCP must therefore build a bounded-degree family in which local frustration of this triangle type persists at constant density across $n$ qubits *and* resists both product-state and constant-depth-circuit certification — exactly what good qLDPC codes achieve for the NLTS half of the statement, and what qLTCs would need to achieve for the hardness half.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*