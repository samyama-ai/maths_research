---
id: 10-theoretical-cs/quantum-singular-value-transformation-optimality
title: "Quantum Singular Value Transformation Optimality"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Singular Value Transformation Optimality

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-singular-value-transformation-optimality` · **Status:** open

## 1. Problem Statement / Conjecture

Quantum singular value transformation (QSVT) — Gilyén, Su, Low and Wiebe (STOC 2019) — takes a block-encoded matrix $A$ and a bounded polynomial $p$ of degree $d$, and implements $p^{(\mathrm{SV})}(A)$ using $d$ queries to the block encoding, $O(d)$ single-qubit rotations, and one ancilla qubit. Nearly every known quantum speedup (search, amplitude estimation, Hamiltonian simulation, linear systems, phase estimation) has been rewritten in this form.

The **QSVT optimality problem** asks whether this framework is *complete and tight*. Three formally distinct claims:

- **(O1) Query optimality.** For every problem specified by a block-encoding oracle, is the minimum QSVT degree $d^\star(\varepsilon)$ equal, up to constant factors, to the true bounded-error quantum query complexity? Equivalently: is the polynomial method not merely a lower-bound technique but an *exactly achievable* upper bound in the block-encoding model?
- **(O2) Universality with constant overhead.** *Conjecture.* Every quantum algorithm making $T$ queries to a unitary oracle $U$ and $U^\dagger$ can be simulated by an interleaved QSVT/LCU circuit using $O(T)$ oracle calls and $O(1)$ ancilla qubits beyond the input register. Currently only $\mathrm{poly}(T)$-overhead or $\Theta(\log)$-ancilla versions are known in general.
- **(O3) Multivariate characterization.** For $k \ge 2$ commuting block-encoded inputs, characterize exactly which tuples of multivariate polynomials are realizable by multivariable QSP (M-QSP). The conjectured $k=1$-style characterization is *false*; no complete replacement is known.

A complete resolution of (O1) requires, for each natural oracle class, either a QSVT construction matching a proven lower bound or a problem with a provable separation between quantum query complexity and minimum achievable QSVT degree. A resolution of (O2) requires a compilation theorem or an oracle separation.

## 2. Mathematical Foundations

**Block encoding.** For $A \in \mathbb{C}^{2^s \times 2^s}$, an $(\alpha, a, \varepsilon)$-block-encoding is a unitary $U$ on $s+a$ qubits with
$$\bigl\| A - \alpha\,(\langle 0|^{\otimes a} \otimes I)\, U \,(|0\rangle^{\otimes a} \otimes I)\bigr\| \le \varepsilon .$$

**Quantum signal processing (QSP).** Let $W(x) = \begin{pmatrix} x & i\sqrt{1-x^2} \\ i\sqrt{1-x^2} & x\end{pmatrix}$ for $x\in[-1,1]$, and $\Phi=(\phi_0,\dots,\phi_d)\in\mathbb{R}^{d+1}$. Set
$$U_\Phi(x) \;=\; e^{i\phi_0 Z} \prod_{k=1}^{d} W(x)\, e^{i\phi_k Z} \;=\; \begin{pmatrix} P(x) & i Q(x)\sqrt{1-x^2} \\ i Q^*(x)\sqrt{1-x^2} & P^*(x)\end{pmatrix}.$$

**Theorem (Low–Chuang; Gilyén–Su–Low–Wiebe).** Such a $\Phi$ exists iff $P,Q \in \mathbb{C}[x]$ satisfy: $\deg P \le d$, $\deg Q \le d-1$; $P$ has parity $d \bmod 2$ and $Q$ parity $(d-1)\bmod 2$; and
$$|P(x)|^2 + (1-x^2)\,|Q(x)|^2 = 1 \quad \text{for all } x \in [-1,1].$$
The completion step (finding $Q$ from $P$) is a Fejér–Riesz factorization of $1-|P|^2$.

**Singular value transformation.** With $A = \sum_j \sigma_j |w_j\rangle\langle v_j|$ and $p$ odd,
$$p^{(\mathrm{SV})}(A) \;=\; \sum_j p(\sigma_j)\,|w_j\rangle\langle v_j|, \qquad \text{and for even } p,\ \ p^{(\mathrm{SV})}(A)=\sum_j p(\sigma_j)|v_j\rangle\langle v_j| .$$
Alternating projected phase rotations $\Pi_\phi = e^{i\phi(2\Pi - I)}$ interleaved with $U, U^\dagger$ block-encode $p^{(\mathrm{SV})}(A)$ using $d$ queries.

**Realizability constraint.** Only $p$ with $\|p\|_{[-1,1]} \le 1$ are directly implementable; subnormalization by a factor $\gamma<1$ costs $O(\gamma^{-1})$ amplitude amplification rounds. The achievable degree is therefore governed by classical approximation theory:
$$d^\star(f,\varepsilon) \;=\; \min\{\,d : \exists\, p,\ \deg p \le d,\ \|p\|_{[-1,1]}\le 1,\ \|p-f\|_{D} \le \varepsilon \,\}.$$

**Polynomial method lower bound (Beals–Buhrman–Cleve–Mosca–de Wolf, 2001).** A $T$-query quantum algorithm's acceptance probability is a real polynomial of degree $\le 2T$ in the oracle bits. Hence $Q_2(f) \ge \widetilde{\deg}(f)/2$. (O1) is the question of whether this inequality is essentially an equality once inputs are presented as block encodings.

**Benchmark degrees.** $e^{-iHt}$ to error $\varepsilon$: $d = \Theta\!\left(t + \frac{\log(1/\varepsilon)}{\log\log(1/\varepsilon)}\right)$ (Jacobi–Anger; matching lower bound from no-fast-forwarding). $\operatorname{sgn}(x)$ on $[-1,-\Delta]\cup[\Delta,1]$: $d=\Theta(\Delta^{-1}\log(1/\varepsilon))$ (Eremenko–Yuditskii). $1/x$ on $[1/\kappa,1]$: $d = \Theta(\kappa\log(1/\varepsilon))$.

## 3. History & State of the Art (SOTA)

- **2016–2017.** Low, Yoder and Chuang introduce QSP for optimal composite pulse sequences; Low–Chuang give optimal Hamiltonian simulation (*PRL* 118, 010501, 2017).
- **2018–2019.** Low–Chuang's *qubitization* (*Quantum* 3, 163) reduces simulation to a walk operator with Chebyshev structure. Gilyén, Su, Low and Wiebe unify search, simulation and matrix inversion into QSVT (STOC 2019). Haah (*Quantum* 3, 190, 2019) proves the exact algebraic characterization of realizable Laurent polynomials and gives an $O(d^3)$ exact-arithmetic decomposition.
- **2020–2021.** Chao–Ding–Gilyén–Huang–Szegedy and Dong–Meng–Whaley–Lin give numerically stable phase-factor solvers reaching machine precision for $d \sim 10^4$. Martyn–Rossi–Tan–Chuang (*PRX Quantum* 2, 040203, 2021) present the "grand unification" reduction of the standard algorithm zoo to QSVT.
- **2022–2024.** Rossi–Chuang (*Quantum* 6, 811, 2022) propose M-QSP and conjecture a multivariate characterization; Németh et al. (arXiv:2312.09072, 2023) refute the natural form of that conjecture. Motlagh–Wiebe (*PRX Quantum* 5, 020368, 2024) give *generalized* QSP, removing the parity and normalization constraints for the $\mathrm{SU}(2)$-on-$U$ setting and lowering rotation counts by a constant factor. Tang–Tian (SOSA 2024) give a short linear-algebraic proof. Low–Su (FOCS 2024) extend to non-normal matrices via quantum eigenvalue processing.
- **State of the art on optimality:** QSVT is *known* optimal for Hamiltonian simulation (additive-error, sparse-access), unstructured search, and eigenstate filtering. It is *known not* to be degree-optimal for quantum linear systems: QSVT gives $O(\kappa \log^2(\kappa/\varepsilon))$ (with variable-time amplitude amplification), while the discrete-adiabatic solver of Costa et al. (*PRX Quantum* 3, 040303, 2022) achieves the optimal $\Theta(\kappa\log(1/\varepsilon))$.

## 4. Partial Results / Verified Cases

- **$k=1$, single block encoding, $\|A\|\le 1$:** the QSP characterization is a complete, proven if-and-only-if theorem (Haah 2019; Gilyén et al. 2019). No gap exists here between realizable and achievable polynomials.
- **Hamiltonian simulation:** QSVT degree $\Theta(\alpha t + \log(1/\varepsilon)/\log\log(1/\varepsilon))$ matches the lower bound of Berry–Childs–Cleve–Kothari–Somma (STOC 2014) — optimal in *all* parameters simultaneously.
- **Amplitude amplification / search:** degree $\Theta(1/a)$ for amplitude $a$, matching BBBV; fixed-point variants (Yoder–Low–Chuang 2014) are degree-optimal to constants.
- **Eigenstate filtering:** Lin–Tong (*Quantum* 4, 361, 2020) prove their degree-$\Theta(\Delta^{-1}\log(1/\varepsilon))$ polynomial is *exactly* the minimax optimum, not merely order-optimal.
- **Ground-state energy estimation:** near-optimal in $\Delta^{-1}$ and overlap $\gamma^{-1}$ (Lin–Tong, *Quantum* 4, 372, 2020).
- **Phase-factor computation:** for $d \le \sim 10^4$ and symmetric $\Phi$, $O(d\,\mathrm{poly}\log)$ algorithms are empirically stable in double precision; provable stability is established in the "infinite QSP" regime where $\sum_k |\phi_k| < \infty$ (Dong–Lin–Ni–Wang, arXiv:2209.10162).
- **$k \ge 2$:** M-QSP is fully characterized only for degree $\le 2$ in each variable and for the commuting-Chebyshev subfamily; general $k=2$ is open.
- **Dequantization boundary:** for low-rank $A$ with sampling access, Chia–Gilyén–Li–Lin–Tang–Wang (STOC 2020) show QSVT confers only polynomial speedup — a verified case where QSVT is *not* the source of exponential advantage.

## 5. Principal Obstacles

- **No lower-bound technique for degree itself.** The polynomial method bounds *query* complexity but says nothing about whether the optimal polynomial is achievable within the QSP normalization $\|p\|_\infty \le 1$. A problem could have quantum query complexity $T$ while every degree-$T$ bounded polynomial fails, because the algorithm exploits interference *between* ancilla branches that no single-qubit signal-processing sequence reproduces.
- **Adiabatic and LCU algorithms escape the polynomial frame.** The optimal linear-systems solver uses the discrete adiabatic theorem, whose analysis is a Riemann–Lebesgue/gap-tracking argument, not an approximation-theoretic one. There is no known way to convert an adiabatic $\Theta(\kappa\log(1/\varepsilon))$ schedule into a degree-$\Theta(\kappa\log(1/\varepsilon))$ bounded polynomial. Chebyshev truncation of $1/x$ provably requires $\Omega(\kappa\log(1/\varepsilon))$ *and* subnormalization $\gamma = \Theta(1/\kappa)$, and removing that $\kappa$ costs the extra log.
- **The Fejér–Riesz completion is unstable in the natural basis.** Root-finding for $1-|P|^2$ has condition number growing exponentially in $d$ when $P$ approaches the boundary $\|P\|_\infty = 1$ — precisely the regime of optimal polynomials. Optimality claims therefore stall on a numerical-analysis obstruction, not only a combinatorial one.
- **Multivariate Fejér–Riesz fails.** For $k\ge2$ variables, a nonnegative trigonometric polynomial need not be a sum-of-squares (Motzkin-type obstruction), so the $\mathrm{SU}(2)$ completion argument that makes the $k=1$ theorem an iff has no analogue. This is the structural reason the Rossi–Chuang conjecture is false.
- **Ancilla accounting.** Interleaving QSVT with LCU for non-polynomial tasks reintroduces $\Theta(\log)$ ancillas; no compression theorem is known, blocking (O2).

## 6. The Gap

Proven: a complete characterization for one variable, and degree-optimality on a specific list of tasks (simulation, search, filtering). Conjectured: that this list is *all* tasks.

The gap is one implication: **from a $T$-query quantum algorithm to a degree-$O(T)$ bounded polynomial with $O(1)$ ancillas.** The polynomial method gives the converse (algorithm $\Rightarrow$ polynomial of degree $2T$ in oracle *bits*), but that polynomial lives in $\{0,1\}^N$-variables, not in the single spectral variable $x$ that QSP manipulates. Crossing the gap requires either (i) a *spectral* polynomial method — showing every oracle algorithm's output amplitude is a bounded univariate polynomial in the block-encoded singular values, or (ii) an explicit oracle problem where quantum query complexity is $T$ but every realizable QSP polynomial needs degree $\omega(T)$. The linear-systems $\log(1/\varepsilon)$ versus $\log^2(1/\varepsilon)$ discrepancy is the sharpest known candidate for (ii), but it is not yet a proven separation — no lower bound rules out a cleverer degree-$O(\kappa\log(1/\varepsilon))$ QSVT construction.

## 7. Current Research (as of June 2026)

- **Berkeley/LBNL (Lin Lin, and collaborators Dong, Ni, Wang, Tong):** analytic theory of phase factors — "infinite QSP", Lipschitz continuity of the $\Phi \mapsto P$ map, and provably stable $O(d\log d)$ solvers. Focus is on making optimality claims numerically realizable.
- **Alfréd Rényi Institute (Gilyén) and collaborators:** classification of QSP variants and the multivariate landscape; the 2023–2024 refutations of M-QSP conjectures, plus search for the correct replacement characterization via matrix-valued Nevanlinna–Pick interpolation. *(frontier — verify)*
- **MIT (Chuang, Martyn, Rossi):** generalized and non-unitary QSP, Laurent/infinite-dimensional lifts, and $\mathrm{SU}(N)$ signal-processing generalizations aimed at (O2).
- **Google/Sydney (Berry, Babbush, Su, Costa):** the adiabatic-versus-QSVT question for linear systems and eigenvalue problems; whether $\Theta(\kappa\log(1/\varepsilon))$ is QSVT-achievable is treated as the key test case for (O1). *(frontier — verify)*
- **Quantum eigenvalue processing (Low–Su, FOCS 2024) follow-ups:** extending optimality analysis to non-normal $A$ and to Jordan-block-degenerate spectra, where singular values and eigenvalues decouple.

## 8. Future Work

- Prove or refute a **spectral polynomial method**: every bounded-error $T$-query algorithm on block-encoded input has acceptance amplitude equal to $p(\sigma)$ for some $\|p\|_\infty\le1$, $\deg p = O(T)$.
- Settle the **linear-systems test case**: either a degree-$O(\kappa\log(1/\varepsilon))$ QSVT circuit for $A^{-1}$, or an $\Omega(\kappa\log^2(1/\varepsilon))$ degree lower bound for bounded polynomial approximations of $1/x$ under the QSP normalization.
- Develop **multivariate positivity certificates** (SOS relaxations, Schur–Agler class) to replace Fejér–Riesz and characterize M-QSP for $k=2$.
- Establish **constant-ancilla compilation** theorems, or an oracle separation showing $\Theta(\log)$ ancillas are necessary.
- Prove **backward stability** of a phase-factor algorithm at the boundary $\|P\|_\infty \to 1$, closing the gap between mathematically optimal and computable phase sequences.

## 9. Key References

- **[Foundational]** A. Gilyén, Y. Su, G. H. Low, N. Wiebe. *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics.* Proc. 51st ACM STOC, 193–204, 2019.
- **[Foundational]** G. H. Low, I. L. Chuang. *Optimal Hamiltonian simulation by quantum signal processing.* Physical Review Letters 118, 010501, 2017.
- **[Foundational]** G. H. Low, I. L. Chuang. *Hamiltonian simulation by qubitization.* Quantum 3, 163, 2019.
- **[Foundational]** J. Haah. *Product decomposition of periodic functions in quantum signal processing.* Quantum 3, 190, 2019.
- **[Foundational]** R. Beals, H. Buhrman, R. Cleve, M. Mosca, R. de Wolf. *Quantum lower bounds by polynomials.* Journal of the ACM 48(4), 778–797, 2001.
- **[Survey]** J. M. Martyn, Z. M. Rossi, A. K. Tan, I. L. Chuang. *Grand unification of quantum algorithms.* PRX Quantum 2, 040203, 2021.
- **[Survey]** E. Tang, K. Tian. *A CS guide to the quantum singular value transformation.* Proc. SIAM Symposium on Simplicity in Algorithms (SOSA), 2024.
- **[SOTA / Recent]** D. Motlagh, N. Wiebe. *Generalized quantum signal processing.* PRX Quantum 5, 020368, 2024.
- **[SOTA / Recent]** Z. M. Rossi, I. L. Chuang. *Multivariable quantum signal processing (M-QSP): prophecies of the two-headed oracle.* Quantum 6, 811, 2022.
- **[SOTA / Recent]** B. Németh, B. Kövér, B. Kulcsár, R. B. Miklós, A. Gilyén. *On variants of multivariate quantum signal processing and their characterizations.* arXiv:2312.09072, 2023.
- **[SOTA / Recent]** P. C. S. Costa, D. An, Y. R. Sanders, Y. Su, R. Babbush, D. W. Berry. *Optimal scaling quantum linear-systems solver via discrete adiabatic theorem.* PRX Quantum 3, 040303, 2022.
- **[SOTA / Recent]** G. H. Low, Y. Su. *Quantum eigenvalue processing.* Proc. 65th IEEE FOCS, 2024.
- **[SOTA / Recent]** L. Lin, Y. Tong. *Optimal polynomial based quantum eigenstate filtering with application to solving quantum linear systems.* Quantum 4, 361, 2020.
- **[SOTA / Recent]** Y. Dong, X. Meng, K. B. Whaley, L. Lin. *Efficient phase-factor evaluation in quantum signal processing.* Physical Review A 103, 042419, 2021.
- **[Foundational]** A. Eremenko, P. Yuditskii. *Uniform approximation of $\mathrm{sgn}(x)$ by polynomials and entire functions.* Journal d'Analyse Mathématique 101, 313–324, 2007.
- **[SOTA / Recent]** N.-H. Chia, A. Gilyén, T. Li, H.-H. Lin, E. Tang, C. Wang. *Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quantum machine learning.* Proc. 52nd ACM STOC, 387–400, 2020.

## 10. Worked Example / Concrete Special Case

**Task.** Amplitude amplification with known amplitude $a = 1/2$. Let $|\psi\rangle = a|\mathrm{good}\rangle + \sqrt{1-a^2}\,|\mathrm{bad}\rangle$ with $a=\sin\theta$, $\theta = \pi/6$. Goal: reach amplitude exactly $1$ on $|\mathrm{good}\rangle$.

**QSVT view.** Take $\Phi = (0,0,0,0)$, so $U_\Phi(x) = W(x)^3$. Writing $x=\cos\alpha$ gives $W(x) = e^{i\alpha X}$, hence
$$\langle 0 | W(x)^3 | 0\rangle = \cos 3\alpha = T_3(x) = 4x^3 - 3x .$$
In the amplitude variable $x = \sin\theta$ (odd parity, sine convention) this is the odd degree-3 polynomial
$$p(x) \;=\; 3x - 4x^3, \qquad p(\sin\theta) = \sin 3\theta .$$

**Evaluation.** At $x = a = 1/2$:
$$p(1/2) \;=\; 3\cdot\tfrac12 - 4\cdot\tfrac18 \;=\; \tfrac32 - \tfrac12 \;=\; 1 .$$
So a degree-3 QSVT sequence — 3 uses of the block encoding, i.e. one Grover iterate plus the initial state preparation — maps amplitude $1/2$ to amplitude $1$. Success probability is exactly $1$, with zero error.

**Realizability check.** $|p(x)|^2 + (1-x^2)|q(x)|^2 = 1$ holds with $q(x) = 4x^2-1$: indeed $(3x-4x^3)^2 + (1-x^2)(4x^2-1)^2 = 1$ identically, so $\Phi$ exists, as the QSP characterization theorem requires.

**Degree optimality.** Suppose $\deg p \le 2$ with $p$ odd, so $p(x)=cx$. The constraint $\|p\|_{[-1,1]}\le 1$ forces $|c|\le 1$, hence $p(1/2) \le 1/2 < 1$. Degree $1$ is impossible, so degree $3$ is minimal. Independently, BBBV-type adversary bounds give $\Omega(1/a) = \Omega(2)$ queries. Here the QSVT degree and the query lower bound agree to within a constant — an instance where (O1) holds.

**Where the general question bites.** Replace the target function $p \approx \operatorname{sgn}$ by $p \approx 1/x$ on $[1/\kappa,1]$. The best bounded polynomial has $\|p\|_\infty \le 1$ only after scaling by $\gamma = \Theta(1/\kappa)$, so recovering unit amplitude costs $\Theta(\kappa)$ further amplification rounds on top of degree $\Theta(\kappa\log(1/\varepsilon))$, yielding $O(\kappa\log^2(\kappa/\varepsilon))$ overall. The adiabatic solver achieves $\Theta(\kappa\log(1/\varepsilon))$. Whether some degree-$O(\kappa\log(1/\varepsilon))$ polynomial with $\gamma = \Theta(1)$ exists — the exact analogue of the clean $p(1/2)=1$ above — is the open case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*