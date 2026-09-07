---
id: 10-theoretical-cs/quantum-advantage-for-shallow-circuits
title: "Quantum Advantage for Shallow Circuits"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Advantage for Shallow Circuits

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-advantage-for-shallow-circuits` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\mathsf{QNC}^0$ be the class of relation problems solvable with high probability by constant-depth quantum circuits over a fixed finite gate set of bounded arity, and let $\mathsf{NC}^0$, $\mathsf{AC}^0$, $\mathsf{AC}^0[p]$, $\mathsf{TC}^0$, $\mathsf{NC}^1$ be the corresponding classical constant-depth (and log-depth) randomized circuit classes.

**Core question.** Is there a computational task, provably and without any unproven complexity assumption, that constant-depth quantum circuits solve but constant-depth classical circuits cannot?

**Resolved fragment (2018).** Yes for bounded fan-in classical circuits: Bravyi, Gosset and König exhibited a relation problem (2D Hidden Linear Function, 2D HLF) with

$$\mathsf{QNC}^0 \not\subseteq \mathsf{NC}^0 ,$$

unconditionally, with the quantum circuit even geometrically local on a 2D grid.

**Open remainder.** The general conjecture is that the separation persists against strictly more powerful classical models:

1. $\mathsf{QNC}^0 \not\subseteq \mathsf{TC}^0$ (constant-depth threshold circuits) and $\mathsf{QNC}^0 \not\subseteq \mathsf{NC}^1$ for *non-interactive* tasks;
2. the separation survives constant-rate local stochastic noise in **2D** without a fault-tolerance overhead that destroys constant depth;
3. the separating task is *verifiable* in classical polynomial time and robust to $\Theta(1)$ error rates in the sense needed for experiments.

A complete resolution of (1) means either an unconditional lower bound for the relation against the classical class, or a $\mathsf{QNC}^0$ simulation algorithm placing all such tasks inside it. Note that pushing to unbounded depth ($\mathsf{QNC}^0 \not\subseteq \mathsf{P/poly}$) would imply $\mathsf{P} \neq \mathsf{PSPACE}$-type separations and is out of reach.

## 2. Mathematical Foundations

**Circuit classes.** A quantum circuit on $n$ qubits has depth $d$ if its gates partition into $d$ layers of pairwise disjoint supports, each gate acting on $O(1)$ qubits. $\mathsf{QNC}^0$ = families $\{C_n\}$ of polynomial size and $d = O(1)$, with output a measurement in the computational basis. Classical circuits are randomized, take independent uniform random bits as extra inputs, and must output a valid answer with probability $\ge 1-\varepsilon$ on **every** input (relation problems have many valid outputs).

**Light cones.** If a classical circuit has fan-in $\le K$ and depth $d$, each output bit depends on at most $K^d$ input bits. This is the only structural fact used against $\mathsf{NC}^0$, and it is what fails for $\mathsf{AC}^0$.

**The Hidden Linear Function problem.** Fix $A \in \mathbb{F}_2^{n \times n}$ upper triangular and $b \in \mathbb{F}_2^n$. Define the quadratic form
$$q(x) \;=\; 2\!\!\sum_{1\le i<j\le n}\!\! A_{ij}x_i x_j \;+\; \sum_{i=1}^n b_i x_i \pmod 4 ,\qquad x\in\mathbb{F}_2^n .$$
Let
$$\mathcal{L}_q=\{x\in\mathbb{F}_2^n : q(x\oplus y)=q(x)+q(y) \bmod 4 \ \ \forall y\in\mathbb{F}_2^n\},$$
a linear subspace on which $q$ restricts to a linear function. **HLF:** output any $z\in\mathbb{F}_2^n$ with
$$q(x)\;=\;2\,z^{\mathsf T}x \pmod 4 \qquad \text{for all } x\in\mathcal{L}_q .$$
**2D HLF** restricts $A$ to the adjacency matrix of a subgraph of the $\sqrt n \times \sqrt n$ grid.

**Quantum solution.** With $U_q|x\rangle = i^{q(x)}|x\rangle$ (a product of $\mathrm{CZ}$ gates for the $A_{ij}$ and $S$ gates for the $b_i$),
$$|\psi_q\rangle \;=\; H^{\otimes n} U_q H^{\otimes n} |0^n\rangle ,\qquad \langle z|\psi_q\rangle = \frac{1}{2^n}\sum_{x\in\mathbb{F}_2^n} (-1)^{z^{\mathsf T}x}\, i^{q(x)} .$$

**Theorem (Bravyi–Gosset–König 2018).** Measuring $|\psi_q\rangle$ yields a valid $z$ with probability $1$; on the grid the $\mathrm{CZ}$ layer 4-edge-colors, so depth is $\le 8$ with nearest-neighbour gates. Conversely, any randomized classical circuit of fan-in $K$ solving 2D HLF on all inputs with probability $> 7/8$ has depth $\Omega(\log n)$.

The $7/8$ threshold is the classical value of the **Mermin–Peres magic square game**: quantum strategies win with probability $1$, any local-hidden-variable strategy with probability $\le 8/9$ per constraint, and the reduction embeds $\Theta(n)$ disjoint magic-square instances into a single 2D HLF instance so that a shallow classical circuit's small light cones force independent — hence classically bounded — play.

## 3. History & State of the Art (SOTA)

- **1990.** Mermin and Peres give the magic square: a finite, perfect quantum–classical gap from commuting Pauli observables. This is the combinatorial seed of every later result.
- **2004.** Terhal and DiVincenzo show constant-depth quantum circuits already produce distributions hard to sample classically under complexity assumptions — advantage, but conditional.
- **2018.** Bravyi, Gosset, König (*Science*) give the first **unconditional** separation, $\mathsf{QNC}^0 \not\subseteq \mathsf{NC}^0$, via 2D HLF.
- **2019.** Bene Watts, Kothari, Schaeffer and Tal (STOC) break the fan-in barrier: a relation in $\mathsf{QNC}^0$ requiring $\mathsf{AC}^0$ circuits of size $\exp(n^{\Omega(1)})$, using $\mathsf{AC}^0$ correlation bounds against parity (Håstad's switching lemma machinery) rather than light cones. Le Gall (CCC 2019) gives an average-case version of the BGK separation.
- **2020.** Bravyi, Gosset, König, Tomamichel (*Nature Physics*) make the separation **noise-robust** using 3D-local circuits and a surface-code-based construction. Grier and Schaeffer (STOC 2020) show interactive (adaptive, few-round) shallow Clifford circuits beat $\mathsf{NC}^1$ and $\oplus \mathsf{L}/\mathrm{poly}$.
- **2021–2024.** Coudron–Stark–Vidick and Bene Watts–Parham extend the framework to certifiable randomness and to *sampling* rather than relation tasks; Caha, Coiteux-Roy, König obtain a "colossal" advantage where noisy 3D-local shallow quantum circuits defeat unbounded fan-in classical circuits.

**SOTA summary.** Separations are unconditional against $\mathsf{NC}^0$, $\mathsf{AC}^0$ (exponential size), and — with interaction — $\mathsf{NC}^1$. Nothing unconditional is known against $\mathsf{TC}^0$ non-interactively.

## 4. Partial Results / Verified Cases

| Classical class | Result | Reference |
|---|---|---|
| $\mathsf{NC}^0$ (fan-in $K$, depth $d$) | 2D HLF needs $d=\Omega(\log n)$ at success $>7/8$; quantum depth $\le 8$, 2D-local | BGK 2018 |
| $\mathsf{NC}^0$, average case | Advantage holds for random instances, success gap $\Theta(1)$ | Le Gall 2019 |
| $\mathsf{AC}^0$ (unbounded fan-in, depth $d$) | Relation problem needs size $\exp\big(\Omega(n^{1/d'})\big)$ | Bene Watts–Kothari–Schaeffer–Tal 2019 |
| $\mathsf{NC}^1$, $\oplus\mathsf{L}/\mathrm{poly}$ | Separation with $O(1)$ rounds of classical interaction | Grier–Schaeffer 2020 |
| $\mathsf{AC}^0$, sampling tasks | Sampling separation, not merely relational | Bene Watts–Parham 2023 |
| Noisy quantum circuits | 3D-local, constant depth, local stochastic noise below a threshold $p_0>0$ | BGKT 2020; Caha–Coiteux-Roy–König 2023 |

Concrete parameters: the BGK grid instance uses $n = m^2$ qubits with $m$ odd, embedding $\Theta(m)$ magic-square gadgets; the classical depth bound is $d \ge \frac{\log(m/2)}{\log K}$ (implied constant depending only on the $7/8$ success target). Small cases ($n \le 25$) have been simulated exactly and run on superconducting hardware.

## 5. Principal Obstacles

- **Light cones stop at fan-in.** The BGK argument is purely geometric: bounded fan-in means output $i$ ignores far-away inputs, so magic-square constraints decouple. An $\mathsf{AC}^0$ gate sees all $n$ inputs, killing the argument outright. Every step past $\mathsf{NC}^0$ needs a genuinely different lower-bound technique.
- **The classical lower-bound frontier.** Beyond $\mathsf{AC}^0$ (switching lemma) and $\mathsf{AC}^0[p]$ (Razborov–Smolensky polynomial method), no superpolynomial lower bounds are known for $\mathsf{TC}^0$ or $\mathsf{NC}^1$ against *any* explicit function. A non-interactive $\mathsf{QNC}^0 \not\subseteq \mathsf{TC}^0$ separation would be a new circuit lower bound in a regime open since the 1980s — this is a hard barrier, not a gap in effort.
- **Correlation bounds are not relation bounds.** Relation problems admit many correct outputs, so an adversarial classical circuit can adaptively pick which constraints to satisfy. Converting a distributional correlation bound into a worst-case relation bound requires the quantum task's solution set to be *rigid* (essentially unique up to a linear code), which is delicate to arrange while keeping the quantum circuit shallow.
- **Noise vs. locality.** Constant-rate noise destroys the magic-square correlations after $O(1)$ layers unless the state is encoded. Known encodings that are decodable in constant depth (single-shot surface codes) need 3D locality; a 2D noisy constant-depth separation would require a single-shot 2D code with constant-depth decoding, which conflicts with known bounds on constant-depth error suppression.
- **Classical simulation from the other side.** Bravyi–Gosset–Movassagh-type algorithms show that noisy or low-entanglement shallow circuits are sometimes classically simulable, so the separating task must live in a narrow window: shallow enough to be quantum, entangled enough to escape simulation.

## 6. The Gap

Proven: an explicit relation $R_n$ with $R_n \in \mathsf{QNC}^0$ and $R_n \notin \mathsf{NC}^0$, $R_n \notin \mathsf{AC}^0$; and with interaction, $R_n \notin \mathsf{NC}^1$.

Wanted: the same with $\mathsf{AC}^0$ replaced by $\mathsf{AC}^0[p]$, $\mathsf{TC}^0$, or $\mathsf{NC}^1$ **without** interaction; and with the quantum circuit 2D-local and noisy.

The precise step: find a $\mathsf{QNC}^0$-computable relation whose valid-output set has *low-degree rigidity* — every $\mathbb{F}_p$-polynomial of degree $\mathrm{polylog}$ agrees with a valid output on at most $2^{-n^{\Omega(1)}}$ fraction of inputs — so that Razborov–Smolensky applies to relations. For $\mathsf{TC}^0$ no candidate technique exists; the gap there is co-extensive with the general circuit lower bound barrier (natural proofs, algebrization).

## 7. Current Research (as of June 2026)

- **IBM Research / Waterloo (Bravyi, Gosset).** Noise-robust separations and matching classical simulation algorithms, mapping the exact depth/noise boundary.
- **RWTH Aachen / Amsterdam (König, Coiteux-Roy, Caha).** 3D-local noisy shallow circuits versus unbounded fan-in classical circuits; pushing towards a 2D analogue. *(frontier — verify)*
- **Simons Institute / MIT–Berkeley (Bene Watts, Parham, Grier, Schaeffer).** Sampling-task separations and relation-versus-$\mathsf{AC}^0[p]$ rigidity; the stated target is an unconditional $\mathsf{QNC}^0$ vs $\mathsf{AC}^0[2]$ separation. *(frontier — verify)*
- **Experimental.** Small-instance 2D HLF and magic-square demonstrations on superconducting and trapped-ion devices; the open engineering question is reaching the $7/8$ threshold at $n$ large enough that no shallow classical circuit could match it. *(frontier — verify)*

## 8. Future Work

1. **Relation-rigidity lemmas.** Develop a polynomial-method analogue for relations, targeting $\mathsf{AC}^0[p]$; the magic square's $\mathbb{F}_2$-linear structure is a natural but currently unhelpful fit, since parity is exactly the $\mathsf{AC}^0[2]$ blind spot.
2. **Non-locality games beyond magic square.** Use games with larger quantum–classical gaps (e.g. linear-system games over $\mathbb{Z}_d$) to strengthen the $7/8$ threshold toward $1/2 + o(1)$, buying room for stronger classical models.
3. **2D noisy separation.** Determine whether a single-shot 2D topological code with constant-depth decoder suffices; a negative answer would be a structural theorem of independent interest.
4. **Efficient verification.** Design separating tasks whose answers are checkable in near-linear classical time, closing the loop between complexity separation and experimental demonstration.
5. **Simulation side.** Sharpen classical algorithms for noisy shallow 2D circuits — an efficient simulation at any constant noise rate would show 2D noisy $\mathsf{QNC}^0$ has *no* advantage, resolving item (2) negatively.

## 9. Key References

- **[Foundational]** S. Bravyi, D. Gosset, R. König. *Quantum advantage with shallow circuits.* Science **362**(6412):308–311, 2018.
- **[Foundational]** N. D. Mermin. *Simple unified form for the major no-hidden-variables theorems.* Physical Review Letters **65**:3373–3376, 1990.
- **[Foundational]** A. Peres. *Incompatible results of quantum measurements.* Physics Letters A **151**:107–108, 1990.
- **[Foundational]** B. Terhal, D. DiVincenzo. *Adaptive quantum computation, constant-depth quantum circuits and Arthur–Merlin games.* Quantum Information and Computation **4**(2):134–145, 2004.
- **[SOTA / Recent]** A. Bene Watts, R. Kothari, L. Schaeffer, A. Tal. *Exponential separation between shallow quantum circuits and unbounded fan-in shallow classical circuits.* STOC 2019, pp. 515–526.
- **[SOTA / Recent]** S. Bravyi, D. Gosset, R. König, M. Tomamichel. *Quantum advantage with noisy shallow circuits.* Nature Physics **16**:1040–1045, 2020.
- **[SOTA / Recent]** D. Grier, L. Schaeffer. *Interactive shallow Clifford circuits: quantum advantage against NC¹ and beyond.* STOC 2020.
- **[SOTA / Recent]** F. Le Gall. *Average-case quantum advantage with shallow circuits.* CCC 2019, LIPIcs vol. 137.
- **[SOTA / Recent]** M. Coudron, J. Stark, T. Vidick. *Trading locality for time: certifiable randomness from low-depth circuits.* Communications in Mathematical Physics **382**:49–86, 2021.
- **[SOTA / Recent]** A. Bene Watts, N. Parham. *Unconditional quantum advantage for sampling with shallow circuits.* arXiv:2301.00995, 2023.
- **[SOTA / Recent]** L. Caha, X. Coiteux-Roy, R. König. *A colossal advantage: 3D-local noisy shallow quantum circuits defeat unbounded fan-in classical circuits.* arXiv:2312.09209, 2023.
- **[Survey]** A. Harrow, A. Montanaro. *Quantum computational supremacy.* Nature **549**:203–209, 2017.
- **[Survey]** J. Håstad. *Computational Limitations of Small-Depth Circuits.* MIT Press, 1987.

## 10. Worked Example / Concrete Special Case

Take $n=3$ on a path $1-2-3$: $A_{12}=A_{23}=1$, all other $A_{ij}=0$, $b=0$. Then
$$q(x) = 2(x_1x_2 + x_2x_3) \bmod 4 .$$

**Step 1 — compute $\mathcal{L}_q$.** Since $q$ is $2\times$ an $\mathbb{F}_2$ form, $q(x\oplus y)-q(x)-q(y) = 2\big(x_1y_2+y_1x_2+x_2y_3+y_2x_3\big) \bmod 4$. This vanishes for all $y$ iff the $\mathbb{F}_2$-coefficients of $y_1,y_2,y_3$ vanish:
$$x_2 = 0,\qquad x_1+x_3=0,\qquad x_2=0 \;\Longrightarrow\; \mathcal{L}_q=\{000,\,101\}.$$

**Step 2 — valid outputs.** $q(000)=0$ and $q(101)=2(0+0)=0$, so we need $2z^{\mathsf T}x \equiv 0 \bmod 4$ on $\mathcal{L}_q$, i.e. $z_1+z_3 \equiv 0 \bmod 2$. Valid set:
$$Z=\{000,\;010,\;101,\;111\}.$$

**Step 3 — the quantum circuit.** $U_q = \mathrm{CZ}_{12}\mathrm{CZ}_{23}$ (two layers, since edges $12$ and $23$ share qubit 2), sandwiched by Hadamard layers: depth 4. Amplitudes:
$$\langle z|\psi_q\rangle=\frac18\sum_{x\in\mathbb{F}_2^3}(-1)^{x_1x_2+x_2x_3+z^{\mathsf T}x}.$$
Split on $x_2$. For $x_2=0$: $\sum_{x_1,x_3}(-1)^{z_1x_1+z_3x_3}=4$ if $z_1=z_3=0$, else $0$. For $x_2=1$: $(-1)^{z_2}\sum_{x_1,x_3}(-1)^{(1+z_1)x_1+(1+z_3)x_3}=4(-1)^{z_2}$ if $z_1=z_3=1$, else $0$. Hence
$$\langle z|\psi_q\rangle=\tfrac12 \text{ for } z\in\{000,010\},\qquad \pm\tfrac12 \text{ for } z\in\{101,111\},\qquad 0 \text{ otherwise.}$$
The circuit outputs a uniformly random element of $Z$ — probability $1/4$ each, success probability $1$.

**Step 4 — why depth matters classically.** Scale the path to length $m$ and note that $z_1+z_m$ is forced by the *global* parity of the $b$-pattern along the path. A classical depth-$d$, fan-in-$K$ circuit computes each $z_i$ from $\le K^d$ inputs; if $K^d < m$, output bits at the two ends see disjoint inputs and are independent given the shared randomness, so the parity constraint fails with constant probability. On the 2D grid, BGK amplify this from one constraint to $\Theta(\sqrt n)$ independent magic-square gadgets, capping any $\mathsf{NC}^0$ circuit at success $7/8$ and forcing depth $\Omega(\log n)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*