---
id: 10-theoretical-cs/quantum-state-tomography-complexity
title: "Quantum State Tomography Complexity"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum State Tomography Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-state-tomography-complexity` · **Status:** open

## 1. Problem Statement / Conjecture

Given $N$ identical copies of an unknown $d$-dimensional mixed quantum state $\rho$, determine the minimum $N$ — and the minimum *computation time* — needed to output a classical description $\hat\rho$ with $\|\hat\rho - \rho\|_1 \le \varepsilon$ with probability $\ge 2/3$.

The unrestricted sample complexity is settled at $\Theta(d^2/\varepsilon^2)$. What remains open is the complexity landscape once the measurement device is constrained, which is the regime every physical experiment lives in. The principal open questions:

1. **Bounded quantum memory.** Let $N(d,\varepsilon,k)$ be the optimal copy complexity for a learner holding at most $k$ qubits of quantum memory between measurements (so it can entangle at most $\lfloor k/\log d\rfloor$ copies at a time). Conjecturally $N \asymp d^3/(\varepsilon^2 \cdot 2^{\Theta(k)})$ interpolating between $d^3/\varepsilon^2$ ($k=0$) and $d^2/\varepsilon^2$ ($k = \Omega(N\log d)$). No matching bounds are known for intermediate $k$.
2. **Infidelity tomography.** Close the $\log(d/\varepsilon)$ gap between the $O\!\big(\tfrac{dr}{\varepsilon}\log\tfrac{d}{\varepsilon}\big)$ upper bound and the $\Omega(dr/\varepsilon)$ lower bound for rank-$r$ states under infidelity loss.
3. **Shadow tomography.** Close the gap between $O(\varepsilon^{-4}\log^2 M \log d)$ and $\Omega(\varepsilon^{-2}\min\{\log M, d^2\})$ copies for estimating $\mathrm{tr}(E_i\rho)$ for $M$ known observables.
4. **Computational efficiency.** Is there a tomography procedure achieving $O(d^2/\varepsilon^2)$ copies in time $\tilde O(d^2/\varepsilon^2)$, i.e. near-linear in the output size?

A complete resolution means matching upper and lower bounds (up to constants) for each of (1)–(3) and an algorithm or barrier for (4).

## 2. Mathematical Foundations

A **state** is $\rho \in \mathbb{C}^{d\times d}$, $\rho = \rho^\dagger \succeq 0$, $\mathrm{tr}\,\rho = 1$. A **POVM** is a family $\{E_x\}_{x\in\mathcal{X}}$ with $E_x \succeq 0$, $\sum_x E_x = I$; Born's rule gives $\Pr[x] = \mathrm{tr}(E_x\rho)$.

Loss functions: trace distance $\|\sigma-\rho\|_1 = \mathrm{tr}\,|\sigma-\rho|$, and infidelity $1 - F(\rho,\sigma)$ with $F = \big(\mathrm{tr}\sqrt{\sqrt{\rho}\,\sigma\sqrt{\rho}}\big)^2$. Fuchs–van de Graaf relates them:
$$1-F \;\le\; \tfrac12\|\rho-\sigma\|_1 \;\le\; \sqrt{1-F}.$$
The square-root makes infidelity the strictly harder loss at scale $\varepsilon$, which is why its optimal rate is $d^2/\varepsilon$ rather than $d^2/\varepsilon^2$.

**Measurement classes.** *Entangled (collective):* one POVM on $\rho^{\otimes N} \in (\mathbb{C}^d)^{\otimes N}$. *Incoherent (single-copy):* measure copies one at a time, possibly adapting the $t$-th POVM to outcomes $x_1,\dots,x_{t-1}$. *$k$-qubit-memory:* the learner's state space is $\mathbb{C}^{2^k}\otimes(\text{classical})$, refreshed by one incoming copy per round.

**Schur–Weyl duality** is the engine for optimal collective schemes. Under the commuting actions of $U(d)$ and $S_N$,
$$(\mathbb{C}^d)^{\otimes N} \;\cong\; \bigoplus_{\lambda \vdash N,\ \ell(\lambda)\le d} \mathcal{Q}_\lambda^d \otimes \mathcal{P}_\lambda ,$$
where $\mathcal{Q}^d_\lambda$ is the irrep of $U(d)$ and $\mathcal{P}_\lambda$ of $S_N$ with Young diagram $\lambda$. Since $\rho^{\otimes N}$ commutes with $S_N$, the **weak Schur sampling** measurement $\{\Pi_\lambda\}$ is sufficient for the spectrum, and $\hat\lambda/N$ concentrates on the spectrum of $\rho$ (Keyl–Werner). Estimating eigenvectors uses the $\mathcal{Q}_\lambda^d$ register; the resulting **Keyl estimator** yields $\hat\rho$.

**Lower bound machinery.** For collective measurements one uses a Bayesian/packing argument with Haar-random unitary conjugates of a fixed spectrum plus Holevo-type information bounds; $\Omega(d^2/\varepsilon^2)$ follows because $\rho$ has $d^2-1$ real parameters each learnable to precision $\varepsilon/d$. For incoherent measurements the sharp tool is a **martingale / likelihood-ratio** analysis: write the learner's transcript likelihood under $\rho_U = \frac{1}{d}(I + \varepsilon\, U G U^\dagger)$ for a random Gaussian-Hermitian $G$, and bound
$$\mathbb{E}_U\!\left[\prod_{t=1}^{N}\frac{\mathrm{tr}(E_{x_t}\rho_U)}{\mathrm{tr}(E_{x_t} I/d)}\right]$$
by a Gaussian-integral / Weingarten calculation. The extra factor $d$ over the collective bound arises because a single-copy POVM element $E$ with $\mathrm{tr}\,E = 1$ can only extract $O(1/d)$ of the available signal per copy.

## 3. History & State of the Art (SOTA)

- **1957–1989.** Fano's density-matrix reconstruction; Vogel–Risken introduce optical homodyne tomography, realized by Smithey et al. (1993).
- **1990s–2000s.** Maximum-likelihood tomography (Hradil 1997); Keyl–Werner (2001) give the spectrum estimator from Schur sampling. Experimental tomography of 8 trapped-ion qubits (Häffner et al., 2005) needed $\sim 10^5$ measurement settings — making the complexity question urgent.
- **2010.** Gross, Liu, Flammia, Becker, Eisert: compressed-sensing tomography, $O(rd\,\mathrm{polylog}\,d)$ Pauli settings for rank-$r$ states.
- **2016.** Two independent papers settle the collective-measurement rate: Haah–Harrow–Ji–Liu–Wu give $O(\frac{d^2}{\varepsilon^2}\log\frac{d}{\varepsilon})$ for trace distance with a memory-efficient scheme, and O'Donnell–Wright give the tight $\Theta(d^2/\varepsilon^2)$ via Schur–Weyl/RSK analysis. Matching lower bound $\Omega(d^2/\varepsilon^2)$.
- **2018.** Aaronson introduces **shadow tomography**: $\tilde O(\varepsilon^{-4}\log^4 M\log d)$ copies for $M$ observables — exponentially fewer than full tomography in $M$.
- **2020.** Huang–Kueng–Preskill's **classical shadows**: $O(\varepsilon^{-2}\log M \cdot \max_i \|E_i\|^2_{\text{shadow}})$ single-copy measurements, practical and now standard in experiments.
- **2021–2023.** Chen–Cotler–Huang–Li prove exponential separations for memory-bounded learners. Chen–Huang–Li–Liu–Sellke and independent work establish the tight incoherent rate $\Theta(d^3/\varepsilon^2)$ and prove **adaptivity does not help** for trace-distance tomography. Bădescu–O'Donnell reduce shadow tomography to $O(\varepsilon^{-4}\log^2 M\log d)$.

## 4. Partial Results / Verified Cases

| Setting | Bound | Status |
|---|---|---|
| Collective, trace distance, general $\rho$ | $\Theta(d^2/\varepsilon^2)$ | **Solved** (O'Donnell–Wright 2016; lower bound Haah et al. 2017) |
| Collective, trace distance, rank $\le r$ | $\Theta(rd/\varepsilon^2)$ | Solved |
| Collective, infidelity, rank $\le r$ | $O(\frac{rd}{\varepsilon}\log\frac{d}{\varepsilon})$ vs. $\Omega(rd/\varepsilon)$ | Open log gap |
| Incoherent nonadaptive & adaptive, trace distance | $\Theta(d^3/\varepsilon^2)$ | **Solved** (2022–23) |
| Pure states ($r=1$), collective | $\Theta(d/\varepsilon)$ infidelity | Solved |
| State *certification* ($\rho = \sigma_0$ vs. $\varepsilon$-far), incoherent | $\Theta(d^{3/2}/\varepsilon^2)$ | Solved |
| Certification, collective | $\Theta(d/\varepsilon^2)$ | Solved |
| Purity testing with $k$-qubit memory | $2^{\Omega(n-k)}$ copies, $d=2^n$ | Solved (Chen–Cotler–Huang–Li 2021) |
| Matrix product states, bond dimension $D$, $n$ qubits | $\mathrm{poly}(n,D,1/\varepsilon)$ | Solved (Cramer et al. 2010; Lanyon et al. 2017 for 14 ions) |
| Stabilizer states / low Clifford-rank | $O(n)$ copies, $\mathrm{poly}(n)$ time | Solved (Montanaro 2017) |
| Shadow tomography of $M$ observables | $O(\varepsilon^{-4}\log^2 M\log d)$ / $\Omega(\varepsilon^{-2}\min\{\log M,d^2\})$ | Open |

Numerically, full tomography is routine to $d = 2^{6}$–$2^{8}$; the 8-qubit W-state reconstruction (Häffner et al. 2005) and 14-qubit MPS tomography (Lanyon et al. 2017) mark the experimental frontier for exact and structured tomography respectively.

## 5. Principal Obstacles

- **Representation theory does not interpolate.** The optimal collective analysis lives entirely inside $\bigoplus_\lambda \mathcal{Q}_\lambda\otimes\mathcal{P}_\lambda$ and needs *all* $N$ copies to be permutation-symmetric. With $k$-qubit memory the learner processes copies in blocks, and the state is symmetric only within blocks; the decomposition of $(\mathbb{C}^d)^{\otimes b}$ into blocks of size $b$ loses exactly the cross-block $S_N$ structure the concentration argument uses. There is no known "partially symmetric" Schur–Weyl calculus with the right error terms.
- **Lower bounds are per-model, not compositional.** The incoherent $\Omega(d^3/\varepsilon^2)$ proof bounds a likelihood martingale where each increment contributes $O(\varepsilon^2/d^{?})$ signal — an argument that requires the post-measurement state to be *classical*. With $k$ qubits retained, the transcript is a quantum–classical hybrid and the martingale is no longer adapted to a classical filtration.
- **The $\varepsilon^{-4}$ in shadow tomography is an artifact of the median-of-means/threshold search primitive** (quantum OR / gentle measurement), not obviously of the task. Gentle measurement composition loses $\varepsilon^2$ per "damage budget" accounting, and no technique currently avoids paying it twice.
- **Time vs. copies.** Even optimal-copy schemes require implementing the quantum Schur transform on $N\log d$ qubits; while this is $\mathrm{poly}$-time (Bacon–Chuang–Harrow), the classical post-processing (Keyl estimator, projections onto the PSD cone) is $\omega(d^2)$, and no near-linear-time optimal estimator is known.
- **Non-i.i.d. and noise.** SPAM (state-preparation-and-measurement) errors mean the observed POVM is itself unknown; self-consistent (gauge) tomography has no complexity theory at all.

## 6. The Gap

For (1): proven endpoints $k=0 \Rightarrow \Theta(d^3/\varepsilon^2)$ and $k = \Omega(N\log d) \Rightarrow \Theta(d^2/\varepsilon^2)$. Unproven: any tight bound for $1 \le k \le n$ with $d=2^n$. The missing step is a lower-bound technique that tracks the *quantum* information in a $k$-qubit register across rounds — a quantum analogue of the classical communication/branching-program hybrid arguments — plus a matching algorithm that uses block-wise Schur sampling on $2^{k/n}$-copy blocks.

For (2): the $\log(d/\varepsilon)$ excess comes from a union bound over eigenvector directions in the Keyl estimator's error analysis; removing it requires a direct concentration bound on $F(\rho,\hat\rho)$ rather than on individual spectral data.

For (3): $\varepsilon^{-4}$ vs. $\varepsilon^{-2}$, and $\log^2 M$ vs. $\log M$. Even the *sign* of the truth is unclear — no lower bound rules out $O(\varepsilon^{-2}\log M \log d)$.

## 7. Current Research (as of June 2026)

- **Memory-bounded interpolation.** Groups at Caltech/Berkeley (Huang, Chen, Cotler, Li, Preskill) and MIT continue the "learning with vs. without quantum memory" program; partial interpolations of the form $\tilde\Theta(d^3/(\varepsilon^2 2^{k}))$ for restricted algorithm classes have been announced *(frontier — verify)*.
- **Tomography under structure.** Learning shallow circuits, Gibbs states, and bounded-depth output distributions with $\mathrm{poly}(n)$ copies; Hamiltonian learning at Heisenberg-limited scaling $O(1/\varepsilon)$ in total evolution time.
- **Classical shadows beyond Cliffords.** Fermionic and matchgate shadows, locally-scrambled ensembles, and shadows robust to gate noise; derandomized and biased-basis variants.
- **Online / adaptive settings.** Regret-minimization formulations of shadow tomography (Aaronson–Chen–Hazan–Kale–Nayak) and mistake-bounded online learning of states.
- **Certification and property testing** as a cheaper substitute for tomography — testing purity, entanglement, and closeness to a stabilizer state with $o(d^2)$ copies.

## 8. Future Work

- Develop a **quantum hybrid argument** for $k$-qubit-memory learners, treating the memory register as a bounded-capacity quantum channel and applying continuity of the Holevo quantity.
- Seek a **matching algorithm** using $b$-copy blockwise Schur sampling and prove its rate is $d^2 \cdot d^{1/b}/\varepsilon^2$-like, which would pin the interpolation.
- Replace gentle-measurement bookkeeping in shadow tomography with a **one-shot compression** argument (quantum information-theoretic, à la convex-split / position-based decoding) to attack $\varepsilon^{-4}$.
- Establish **time–copy tradeoff lower bounds**: is there a cryptographic obstruction to $\tilde O(d^2)$-time optimal tomography?
- Extend the complexity theory to **SPAM-robust, gauge-invariant** tomography, where the true parameter is an equivalence class, not a point.

## 9. Key References

- **[Foundational]** M. Keyl, R. F. Werner. *Estimating the spectrum of a density operator.* Physical Review A 64, 052311, 2001.
- **[Foundational]** D. Gross, Y.-K. Liu, S. T. Flammia, S. Becker, J. Eisert. *Quantum state tomography via compressed sensing.* Physical Review Letters 105, 150401, 2010.
- **[Foundational]** R. O'Donnell, J. Wright. *Efficient quantum tomography.* STOC 2016, pp. 899–912.
- **[Foundational]** J. Haah, A. W. Harrow, Z. Ji, X. Wu, N. Yu. *Sample-optimal tomography of quantum states.* IEEE Transactions on Information Theory 63(9), 5628–5641, 2017 (STOC 2016).
- **[SOTA / Recent]** S. Aaronson. *Shadow tomography of quantum states.* STOC 2018, pp. 325–338; SIAM Journal on Computing 49(5), 2020.
- **[SOTA / Recent]** H.-Y. Huang, R. Kueng, J. Preskill. *Predicting many properties of a quantum system from very few measurements.* Nature Physics 16, 1050–1057, 2020.
- **[SOTA / Recent]** C. Bădescu, R. O'Donnell. *Improved quantum data analysis.* STOC 2021, pp. 1398–1411.
- **[SOTA / Recent]** S. Chen, J. Cotler, H.-Y. Huang, J. Li. *Exponential separations between learning with and without quantum memory.* FOCS 2021, pp. 574–585.
- **[SOTA / Recent]** S. Chen, B. Huang, J. Li, A. Liu, M. Sellke. *When does adaptivity help for quantum state learning?* FOCS 2023.
- **[SOTA / Recent]** H. Yuen. *An improved sample complexity lower bound for (fidelity) quantum state tomography.* Quantum 7, 890, 2023.
- **[Survey]** M. Cramer, M. B. Plenio, S. T. Flammia, R. Somma, D. Gross, S. D. Bartlett, O. Landon-Cardinal, D. Poulin, Y.-K. Liu. *Efficient quantum state tomography.* Nature Communications 1, 149, 2010.
- **[Survey]** M. A. Nielsen, I. L. Chuang. *Quantum Computation and Quantum Information.* Cambridge University Press, 10th anniversary edition, 2010 (Ch. 8–9).
- **[Survey]** A. Anshu, S. Arunachalam. *A survey on the complexity of learning quantum states.* Nature Reviews Physics 6, 59–69, 2024.

## 10. Worked Example / Concrete Special Case

**One qubit, $d=2$, incoherent Pauli tomography.** Write $\rho = \tfrac12(I + r_x X + r_y Y + r_z Z)$ with Bloch vector $r$, $\|r\|_2 \le 1$. Note $\|\rho - \sigma\|_1 = \|r_\rho - r_\sigma\|_2$.

Split $N$ copies into three groups of $N/3$ and measure $X$, $Y$, $Z$ respectively. Measuring $Z$ on $\rho$ gives $\pm1$ with $\Pr[\pm] = (1\pm r_z)/2$, so the outcome $b$ satisfies $\mathbb{E}[b] = r_z$, $\mathrm{Var}(b) = 1-r_z^2$. The empirical mean $\hat r_z$ over $N/3$ shots has
$$\mathrm{Var}(\hat r_z) = \frac{3(1-r_z^2)}{N}, \qquad \mathbb{E}\|\hat r - r\|_2^2 = \frac{3}{N}\sum_{i}(1-r_i^2) = \frac{3(3-\|r\|^2)}{N} \le \frac{9}{N}.$$
To force $\|\hat\rho-\rho\|_1 = \|\hat r - r\|_2 \le \varepsilon$ with constant probability, Chebyshev needs $9/N \lesssim \varepsilon^2$, i.e.
$$N = \Theta(1/\varepsilon^2)\quad\text{with constant } \approx 27 \text{ for } \tfrac13 \text{ failure at } \|r\|=0 .$$

Now compare the three regimes at $d=2$: incoherent optimum $\Theta(d^3/\varepsilon^2) = 8/\varepsilon^2$; collective optimum $\Theta(d^2/\varepsilon^2) = 4/\varepsilon^2$. At $d=2$ the ratio is only $2$, so Pauli tomography looks near-optimal. The point of the open problem is what happens on $n$ qubits, $d = 2^n$: the same naive scheme costs $3^n/\varepsilon^2 = d^{1.585}/\varepsilon^2$ *settings* but $\Theta(d^3/\varepsilon^2) = 8^n/\varepsilon^2$ copies, whereas a collective scheme needs $4^n/\varepsilon^2$. At $n=10$ that is $2^{30} \approx 10^9$ copies versus $2^{20}\approx10^6$ — a factor $1024$, which is precisely the factor $d$ that bounded quantum memory is conjectured to buy back exponentially in $k$, and which nobody has yet quantified for $0 < k < n$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*