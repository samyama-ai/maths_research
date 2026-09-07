---
id: 10-theoretical-cs/learning-with-errors-complexity
title: "Learning with Errors Complexity"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Learning with Errors Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/learning-with-errors-complexity` · **Status:** open

## 1. Problem Statement / Conjecture

Learning with Errors (LWE) asks one to recover a secret $\mathbf{s} \in \mathbb{Z}_q^n$ from noisy linear equations $\langle \mathbf{a}_i, \mathbf{s}\rangle + e_i \bmod q$ with $\mathbf{a}_i$ uniform and $e_i$ small. The open problem is to pin down its true computational complexity. Four sharp questions:

1. **Best algorithm.** With $q = \mathrm{poly}(n)$, Gaussian noise of width $\alpha q = \Theta(\sqrt{n})$, and $m = O(n)$ samples, does any algorithm run in time $2^{o(n)}$? Nothing below $2^{\Theta(n)}$ is known; nothing rules $2^{o(n)}$ out.
2. **Tightness of the attack curve.** Is the primal/dual lattice-reduction cost $2^{\Theta(\beta)}$ at BKZ block size $\beta$ essentially optimal, and can that optimality be proven in any restricted algorithmic model?
3. **Reduction quality.** Can the worst-case-to-average-case reduction from $\mathrm{GapSVP}_\gamma$ / $\mathrm{SIVP}_\gamma$ with $\gamma = \tilde{O}(n/\alpha)$ be made *classical, polynomial-modulus, and dimension-preserving*? Regev's is quantum; the classical versions pay an exponential modulus or a dimension blow-up.
4. **Quantum separation.** Is there a quantum algorithm beating the best classical one by more than Grover-type square-root factors on subroutines?

A resolution of (1) means a proven $2^{o(n)}$ algorithm in the cryptographic regime, or an unconditional lower bound in a strong model (statistical query, sum-of-squares, low-degree polynomial). A resolution of (3) means the reduction stated above with no loss.

## 2. Mathematical Foundations

**Distribution.** Fix dimension $n$, modulus $q = q(n)$, error distribution $\chi$ on $\mathbb{Z}$. For $\mathbf{s} \in \mathbb{Z}_q^n$, the LWE distribution $A_{\mathbf{s},\chi}$ on $\mathbb{Z}_q^n \times \mathbb{Z}_q$ outputs
$$(\mathbf{a}, b),\qquad \mathbf{a} \leftarrow U(\mathbb{Z}_q^n),\; e \leftarrow \chi,\; b = \langle \mathbf{a},\mathbf{s}\rangle + e \bmod q .$$

**Search-LWE$_{n,q,\chi,m}$:** given $m$ samples from $A_{\mathbf{s},\chi}$, output $\mathbf{s}$.
**Decision-LWE:** distinguish $m$ such samples (with $\mathbf{s}\leftarrow U(\mathbb{Z}_q^n)$) from $m$ uniform samples on $\mathbb{Z}_q^n\times\mathbb{Z}_q$ with non-negligible advantage.

In matrix form, with $A \in \mathbb{Z}_q^{m\times n}$ and $\mathbf{b} = A\mathbf{s} + \mathbf{e} \bmod q$, LWE is bounded-distance decoding (BDD) on the $q$-ary lattice
$$\Lambda_q(A) = \{ \mathbf{y} \in \mathbb{Z}^m : \mathbf{y} \equiv A\mathbf{s} \!\!\pmod q,\ \exists\,\mathbf{s} \in \mathbb{Z}_q^n \},\qquad \det \Lambda_q(A) = q^{\,m-n}\ \text{(generic $A$)},$$
whose companion is the SIS lattice $\Lambda_q^\perp(A) = \{\mathbf{y} \in \mathbb{Z}^m : A^{\top}\mathbf{y} \equiv \mathbf{0} \bmod q\}$.

**Noise.** Standard choice is the discrete Gaussian $D_{\mathbb{Z},\sigma}$, $\Pr[x] \propto e^{-\pi x^2/\sigma^2}$, with $\sigma = \alpha q$. The hard regime needs $\alpha q \ge 2\sqrt{n}$, i.e. noise above the smoothing parameter
$$\eta_\varepsilon(\Lambda) = \min\{ s>0 : \rho_{1/s}(\Lambda^*\setminus\{\mathbf 0\}) \le \varepsilon \},\qquad \rho_s(\mathbf{x}) = e^{-\pi\|\mathbf{x}\|^2/s^2}.$$

**Lattice problems.** For approximation factor $\gamma(n)$: $\mathrm{GapSVP}_\gamma$ decides $\lambda_1(\Lambda) \le 1$ versus $\lambda_1(\Lambda) > \gamma$; $\mathrm{SIVP}_\gamma$ finds $n$ independent vectors of length $\le \gamma\,\lambda_n(\Lambda)$.

**Theorem (Regev 2005).** For $q \le 2^{\mathrm{poly}(n)}$ and $\alpha q \ge 2\sqrt{n}$, there is a *quantum* polynomial-time reduction from worst-case $\mathrm{SIVP}_{\tilde{O}(n/\alpha)}$ and $\mathrm{GapSVP}_{\tilde{O}(n/\alpha)}$ to average-case search-LWE$_{n,q,\Psi_\alpha}$.

**Theorem (Regev 2005, search-to-decision).** For prime $q = \mathrm{poly}(n)$, search-LWE and decision-LWE are polynomially equivalent, via a hybrid that guesses each coordinate $s_j \in \mathbb{Z}_q$ and tests with a shifted distinguisher.

**Theorem (Peikert 2009; Brakerski–Langlois–Peikert–Regev–Stehlé 2013).** There is a *classical* reduction from $\mathrm{GapSVP}_{\tilde{O}(n/\alpha)}$ to LWE with exponential modulus $q \ge 2^{n/2}$ (Peikert), or with polynomial modulus at the cost of a dimension blow-up $n \mapsto n\log q$ (BLPRS modulus–dimension tradeoff).

**Structured variants.** Ring-LWE replaces $\mathbb{Z}_q^n$ by $R_q = \mathbb{Z}[x]/(\Phi_m(x),q)$; Module-LWE interpolates via rank-$d$ modules over $R_q$. Reductions from approximate-SVP on ideal (LPR 2010) and module (Langlois–Stehlé 2015) lattices are known.

## 3. History & State of the Art (SOTA)

- **1993 — Blum, Furst, Kearns, Lipton** pose learning parity with noise (LPN), the $q=2$ ancestor.
- **2003 — Blum, Kalai, Wasserman (BKW)** give a $2^{O(n/\log n)}$ algorithm for LPN by iterated sample collision; it later transfers to LWE.
- **2005 — Regev** defines LWE and proves the quantum worst-case reduction and search-to-decision equivalence (STOC 2005; JACM 2009).
- **2009 — Peikert** gives the first classical reduction, with exponential modulus.
- **2010 — Lyubashevsky, Peikert, Regev** introduce Ring-LWE, making LWE cryptography practical.
- **2011 — Arora, Ge** solve LWE in subexponential time when noise is very small, by linearizing an error-annihilating polynomial.
- **2013 — BLPRS** get the classical reduction at polynomial modulus with dimension loss.
- **2015–2016 — cryptanalytic baseline.** Albrecht–Player–Scott give the concrete-hardness survey; Alkim–Ducas–Pöppelmann–Schwabe introduce the "core-SVP" cost model; Becker–Ducas–Gama–Laarhoven give sieving at $2^{0.292\beta+o(\beta)}$ time (quantum variants near $2^{0.265\beta}$).
- **2016–2017 — ideal-lattice weakness.** Cramer–Ducas–Peikert–Regev and Cramer–Ducas–Wesolowski solve Ideal-SVP to $2^{\tilde{O}(\sqrt{n})}$ factors in quantum polynomial time.
- **2023 — Ducas, Pulles** show the independence heuristics behind several claimed dual-attack gains are self-contradictory, retracting part of the SOTA estimate.
- **2024 — quantum claim retracted.** Chen's claimed polynomial-time quantum algorithm for LWE was withdrawn within days after a bug was found.
- **2024 — standardization.** NIST publishes FIPS 203 (ML-KEM) and FIPS 204 (ML-DSA), both resting on Module-LWE.

## 4. Partial Results / Verified Cases

- **Small noise is easy (Arora–Ge).** If the error takes at most $d$ values, search-LWE is solvable in time $n^{O(d)}$ by linearization. For $\alpha q = n^{\epsilon}$ with $\epsilon<1/2$ this gives $2^{\tilde{O}(n^{2\epsilon})}$ — subexponential. So the threshold $\alpha q \gtrsim \sqrt{n}$ is real, not a proof artifact.
- **Unbounded samples: $2^{O(n/\log n)}$.** BKW adapted to LWE (Albrecht–Cid–Faugère–Fitzpatrick–Perret 2015) achieves $2^{O(n/\log n)}$ time for $q=\mathrm{poly}(n)$, but needs subexponentially many samples — never available in cryptographic instances.
- **Bounded samples ($m = O(n)$): $2^{\Theta(n)}$.** Best known is BKZ with sieving; no $2^{o(n)}$ algorithm for any constant in the exponent.
- **Exponential modulus.** For $q \ge 2^{n/2}$, Peikert's classical reduction from $\mathrm{GapSVP}_{\tilde O(n/\alpha)}$ applies.
- **Small/sparse secrets.** Binary secrets in dimension $n$ are roughly as hard as uniform secrets in dimension $n/\log q$; sparse secrets of Hamming weight $h \ll n$ admit hybrid meet-in-the-middle speedups (Howgrave-Graham; Albrecht 2017).
- **Restricted-model lower bounds.** Noisy parity, hence LWE, requires $2^{\Omega(n)}$ statistical queries in Kearns' SQ model; low-degree-polynomial and sum-of-squares lower bounds hold for related planted problems.
- **Structured cases.** Ideal-SVP $\to$ Ring-LWE and Module-SVP $\to$ Module-LWE are theorems; but Ideal-SVP itself is quantum-subexponential at $2^{\tilde O(\sqrt n)}$ factors, so the ring starting point is strictly weaker than general SVP.

## 5. Principal Obstacles

- **No unconditional hardness technique.** Proving LWE hard implies $\mathsf{P} \ne \mathsf{NP}$. The only realistic goal is reduction from a believed-hard problem; circuit lower bound barriers (relativization, natural proofs, algebrization) block everything else.
- **The reduction's source problem cannot be NP-hard.** $\mathrm{GapSVP}_\gamma$ is NP-hard only for $\gamma = n^{O(1/\log\log n)}$; for $\gamma \ge \sqrt{n}$ it lies in $\mathsf{NP}\cap\mathsf{coNP}$ (Aharonov–Regev 2005). LWE's reduction needs $\gamma = \tilde O(n/\alpha) \gg \sqrt n$, so the worst-case guarantee comes from a provably-not-NP-hard problem unless PH collapses.
- **The quantum step is essential, not cosmetic.** Regev converts a BDD oracle into discrete Gaussian samples using a quantum Fourier transform over lattice cosets — it holds a superposition over cosets that no known classical procedure simulates at polynomial modulus without dimension loss.
- **Lattice reduction resists analysis.** BKZ's output quality is described by the Geometric Series Assumption and simulators, not theorems. Provable BKZ bounds are far weaker than observed behaviour, so even the *upper* bound $2^{0.292\beta}$ is heuristic; "is the attack optimal?" cannot yet be stated in proven quantities.
- **Dual-attack foundations are unstable.** Ducas–Pulles (2023) showed the heuristics behind several claimed improvements are mutually contradictory, so the cost estimate itself keeps moving.
- **Algebraic structure cuts both ways.** Ring structure enables faster arithmetic *and* specialized attacks, so unstructured-LWE intuition does not transfer to the deployed structured variants.

## 6. The Gap

Proven: (a) LWE is at least as hard as worst-case $\mathrm{SIVP}_{\tilde O(n/\alpha)}$ under a quantum reduction; (b) with $\mathrm{poly}(n)$ samples the best known algorithm costs $2^{\Theta(n)}$; (c) with $2^{\Theta(n/\log n)}$ samples, BKW costs $2^{\Theta(n/\log n)}$; (d) with $\alpha q \ll \sqrt n$ it is subexponential.

Unproven: there is **no lower bound in any general model**, and **no upper bound below $2^{\Theta(n)}$** in the cryptographic sample regime. The gap between "nothing known below $2^{0.292\beta}$" and "nothing proved above $\mathrm{poly}(n)$" spans the whole complexity landscape. The concrete steps to cross are: (i) a classical, polynomial-modulus, dimension-preserving worst-case reduction; (ii) a proof that sieving-BKZ is optimal within some natural algorithmic class; (iii) an algorithm exploiting the $q$-ary structure of $\Lambda_q(A)$ — which BKZ treats as a generic lattice — to reach $2^{o(n)}$ with $O(n)$ samples.

## 7. Current Research (as of June 2026)

- **Concrete-hardness estimation.** The Lattice Estimator (Albrecht et al.) is the reference tool; work continues reconciling primal-uSVP, dual, and hybrid costs after the Ducas–Pulles correction. *(frontier — verify)* Recent preprints replace contradictory dual-attack heuristics with contradiction-free models.
- **Sieving and memory.** CWI (Ducas), Leiden, and Bochum groups study whether $2^{0.292\beta}$ time / $2^{0.208\beta}$ memory can be beaten, and whether memory-bounded cost models shift NIST security categories.
- **Quantum algorithms.** After the 2024 retraction, work continues on Gaussian-state and dihedral-hidden-subgroup framings, and on whether quantum advantage for LWE is confined to Grover square roots. *(frontier — verify)*
- **Structured-lattice separations.** Whether Module-LWE at rank $\ge 2$ inherits ideal-lattice weaknesses; consensus is no, proof absent.
- **FHE secrets.** Sparse/ternary secrets in CKKS/BGV/TFHE drive hybrid dual meet-in-the-middle attack research and periodic parameter revisions.
- **Average-case complexity.** Placing LWE in fine-grained frameworks and deriving low-degree / sum-of-squares lower bounds.

## 8. Future Work

- A classical worst-case reduction at $q = \mathrm{poly}(n)$ with no dimension loss — Peikert's stated open problem since 2009.
- Unconditional $2^{\Omega(n)}$ lower bounds in a model that actually captures BKZ-style algorithms.
- Replace the Geometric Series Assumption with a theorem; a rigorous BKZ output-quality analysis would make NIST parameter estimates provable rather than simulated.
- Settle whether $\alpha q = \Theta(\sqrt n)$ is a sharp threshold: is there an algorithm at $\alpha q = n^{1/2-o(1)}$ beating Arora–Ge?
- Determine whether decision-Ring-LWE over non-cyclotomic or non-prime-splitting rings admits attacks, sharpening ring-choice guidance.

## 9. Key References

- **[Foundational]** Oded Regev. *On lattices, learning with errors, random linear codes, and cryptography.* STOC 2005; Journal of the ACM 56(6), 2009.
- **[Foundational]** Avrim Blum, Adam Kalai, Hal Wasserman. *Noise-tolerant learning, the parity problem, and the statistical query model.* Journal of the ACM 50(4), 2003.
- **[Foundational]** Chris Peikert. *Public-key cryptosystems from the worst-case shortest vector problem.* STOC 2009.
- **[Foundational]** Vadim Lyubashevsky, Chris Peikert, Oded Regev. *On ideal lattices and learning with errors over rings.* EUROCRYPT 2010; Journal of the ACM 60(6), 2013.
- **[Theory]** Zvika Brakerski, Adeline Langlois, Chris Peikert, Oded Regev, Damien Stehlé. *Classical hardness of learning with errors.* STOC 2013.
- **[Theory]** Sanjeev Arora, Rong Ge. *New algorithms for learning in presence of errors.* ICALP 2011.
- **[Theory]** Dorit Aharonov, Oded Regev. *Lattice problems in NP ∩ coNP.* Journal of the ACM 52(5), 2005.
- **[Theory]** Adeline Langlois, Damien Stehlé. *Worst-case to average-case reductions for module lattices.* Designs, Codes and Cryptography 75(3), 2015.
- **[SOTA / Recent]** Anja Becker, Léo Ducas, Nicolas Gama, Thijs Laarhoven. *New directions in nearest neighbor searching with applications to lattice sieving.* SODA 2016.
- **[SOTA / Recent]** Léo Ducas, Ludo Pulles. *Does the dual-sieve attack on Learning with Errors even work?* CRYPTO 2023.
- **[SOTA / Recent]** Ronald Cramer, Léo Ducas, Chris Peikert, Oded Regev. *Recovering short generators of principal ideals in cyclotomic rings.* EUROCRYPT 2016.
- **[SOTA / Recent]** Erdem Alkim, Léo Ducas, Thomas Pöppelmann, Peter Schwabe. *Post-quantum key exchange — a New Hope.* USENIX Security 2016.
- **[Survey]** Martin R. Albrecht, Rachel Player, Sam Scott. *On the concrete hardness of Learning with Errors.* Journal of Mathematical Cryptology 9(3), 2015.
- **[Survey]** Chris Peikert. *A decade of lattice cryptography.* Foundations and Trends in Theoretical Computer Science 10(4), 2016.
- **[Survey]** Daniele Micciancio, Oded Regev. *Lattice-based cryptography.* In *Post-Quantum Cryptography*, Springer, 2009.
- **[Standard]** NIST. *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard.* 2024.

## 10. Worked Example / Concrete Special Case

Take $n=2$, $q=17$, secret $\mathbf{s}=(4,12)^\top$, errors $e_i \in \{-1,0,1\}$. Note $2^{-1}=9$ and $5^{-1}=7$ in $\mathbb{Z}_{17}$.

| $i$ | $\mathbf{a}_i$ | $\langle \mathbf{a}_i,\mathbf{s}\rangle \bmod 17$ | $e_i$ | $b_i$ |
|---|---|---|---|---|
| 1 | $(3,1)$ | $12+12=24\equiv 7$ | $+1$ | $8$ |
| 2 | $(5,0)$ | $20\equiv 3$ | $-1$ | $2$ |
| 3 | $(1,2)$ | $4+24=28\equiv 11$ | $0$ | $11$ |
| 4 | $(2,4)$ | $8+48=56\equiv 5$ | $+1$ | $6$ |

**Elimination.** Sample 2 forces $5s_1 \in \{1,2,3\}$, so $s_1 \in \{7\cdot1, 7\cdot2, 7\cdot3\} = \{7,14,4\}$.

- $s_1=7$: sample 1 gives $21+s_2 \equiv 4+s_2 \in \{7,8,9\}$, so $s_2\in\{3,4,5\}$. Sample 3 gives $7+2s_2\in\{10,11,12\}$, so $2s_2\in\{3,4,5\}$ and $s_2\in\{10,2,11\}$. Intersection empty — branch dies.
- $s_1=4$: sample 1 gives $s_2\in\{12,13,14\}$; sample 3 gives $2s_2\in\{6,7,8\}$, i.e. $s_2\in\{3,12,4\}$. Intersection $\{12\}$. Sample 4 checks: $8+48\equiv5$, $|6-5|=1$. ✓
- $s_1=14$: sample 1 gives $s_2\in\{16,0,1\}$; sample 3 gives $2s_2\in\{13,14,15\}$, i.e. $s_2\in\{15,7,16\}$. Intersection $\{16\}$; sample 4 gives $28+64=92\equiv7$, $|6-7|=1$, so $(14,16)$ **also survives**.

Four samples are not enough. Add sample 5: $\mathbf{a}_5=(1,1)$, $e_5=0$, $b_5=16$. Then $(4,12)$ gives $16$ ✓, while $(14,16)$ gives $30\equiv13$, an error of $3$ — rejected. The secret is now unique.

**Lattice view.** With $A$ the $5\times2$ matrix of the $\mathbf{a}_i$, the lattice $\Lambda_q(A)\subset\mathbb{Z}^5$ has $\det = 17^{3}=4913$, and the Gaussian heuristic predicts
$$\lambda_1 \approx \sqrt{\tfrac{5}{2\pi e}}\cdot 4913^{1/5} \approx 0.541 \times 5.47 \approx 2.96 .$$
The target $A\mathbf{s}$ sits at distance $\|\mathbf{e}\| = \sqrt{1+1+0+1+0} = \sqrt3 \approx 1.73 < \lambda_1/2 \cdot 2$, so the BDD instance is uniquely decodable and reduction finds it.

**The hard regime.** Scale to ML-KEM-768: $q=3329$, $\sigma\approx1.2$, effective dimension $768$ (rank 3 over a degree-256 ring). The primal attack needs BKZ block size $\beta\approx 620$, costing about $2^{0.292\cdot620}\approx 2^{181}$ core-SVP operations. Nothing known pushes this below exponential, and nothing proves it cannot fall to $\mathrm{poly}(n)$. That gap is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*