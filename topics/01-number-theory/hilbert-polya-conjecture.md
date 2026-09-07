---
id: 01-number-theory/hilbert-polya-conjecture
title: "Hilbert-Polya Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hilbert-Polya Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/hilbert-polya-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Hilbert-Pólya conjecture states that the non-trivial zeros of the Riemann zeta function $\zeta(s)$ correspond to the eigenvalues of a self-adjoint operator (or a related Hermitian operator) acting on a Hilbert space. Specifically, if the non-trivial zeros are parameterized as $s_n = 1/2 + i\gamma_n$, the conjecture posits that the values $\gamma_n$ form the discrete spectrum of an unbounded, self-adjoint operator $H$. Because self-adjoint operators possess purely real eigenvalues, the existence of such an operator would imply that all $\gamma_n$ are real, thereby providing a rigorous proof of the Riemann Hypothesis.

## 2. Mathematical Foundations

The Riemann zeta function is defined for $Re(s) > 1$ by the Dirichlet series and the Euler product:
$$ \zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^s}\right)^{-1} $$
It can be analytically continued to a meromorphic function on the entire complex plane with a single simple pole at $s=1$. The Riemann Hypothesis asserts that all non-trivial zeros of $\zeta(s)$ lie exactly on the critical line $Re(s) = 1/2$.

In functional analysis, a densely defined linear operator $H$ on a Hilbert space $\mathcal{H}$ is self-adjoint if it equals its own adjoint ($H = H^*$) and their domains coincide. The spectral theorem guarantees that the spectrum of a self-adjoint operator is a subset of the real numbers $\mathbb{R}$.

If there exists a self-adjoint operator $H$ such that its eigenvalue equation:
$$ H \psi_n = \gamma_n \psi_n $$
has solutions where $1/2 + i\gamma_n$ are the non-trivial zeros of $\zeta(s)$, then all $\gamma_n \in \mathbb{R}$, which forces $Re(s_n) = 1/2$.

## 3. History & State of the Art (SOTA)

The conjecture is primarily attributed to conversations between George Pólya and Edmund Landau around 1912–1914, though Pólya later indicated the core concept originated with David Hilbert. At that time, it was merely an intuitive speculation that the zeros might be eigenvalues of some matrix or integral operator.

The modern revival occurred in 1972, when Hugh Montgomery investigated the pair correlation of the zeros of the zeta function. Montgomery discovered that the zeros exhibited "mutual repulsion." Physicist Freeman Dyson noticed that Montgomery's pair correlation formula perfectly matched the pair correlation of eigenvalues of random complex Hermitian matrices in the Gaussian Unitary Ensemble (GUE) of random matrix theory (RMT).

This connection led to the Berry-Keating conjecture in 1999, which proposed that the hypothetical operator $H$ could be constructed by quantizing the classical chaotic Hamiltonian $H_{cl} = xp$ on the phase space $(x, p)$.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, the spectral interpretation has been unequivocally proven in analogous mathematical domains:

1. **Selberg Trace Formula (1956):** Atle Selberg discovered a trace formula relating the lengths of closed geodesics on compact Riemann surfaces to the eigenvalues of the Laplace-Beltrami operator on the surface. The Selberg zeta function $Z(s)$ has zeros precisely corresponding to the eigenvalues $\lambda = s(1-s)$ of the Laplacian. Because the Laplacian is a positive semi-definite self-adjoint operator, its eigenvalues are real and non-negative, proving the analogue of the Riemann Hypothesis for $Z(s)$ unconditionally.
2. **Function Fields / Weil Conjectures (1974):** The Weil conjectures, proven by Pierre Deligne, imply the analogue of the Riemann Hypothesis for curves over finite fields. The proof realizes the zeros of the associated Hasse-Weil zeta function as the eigenvalues of the Frobenius endomorphism acting on étale cohomology groups, providing a pure algebraic geometry spectral interpretation.
3. **Computational Verification:** Massive numerical computations by Andrew Odlyzko on the zeros of the Riemann zeta function (verifying up to the $10^{22}$-nd zero) confirm that the local spacing distribution of the zeros aligns extraordinarily well with GUE predictions from random matrix theory.

## 5. Principal Obstacles

The central difficulty lies in constructing the required Hilbert space and the operator $H$, and avoiding circular logic when proving its spectrum.

1. **Boundary Conditions for $H = xp$:** The Berry-Keating classical Hamiltonian $H_{cl} = xp$ possesses a continuous spectrum. Standard quantization yields the operator $\hat{H} = \frac{1}{2}(\hat{x}\hat{p} + \hat{p}\hat{x}) = -i\hbar(x \frac{d}{dx} + \frac{1}{2})$, which still has a purely continuous real spectrum. Truncating this continuous spectrum into a discrete set corresponding exactly to the Riemann zeros requires highly artificial boundary conditions that no one has successfully derived from first principles.
2. **The "Minus Sign" and Density of States:** In random matrix theory, the density of eigenvalues follows Wigner's semicircle law, while the density of Riemann zeros grows logarithmically. Alain Connes (1999) proposed a rigorous spectral interpretation where the Riemann zeros appear as an *absorption* spectrum (missing eigenvalues) rather than an emission spectrum. Connes' operator acts on the adele class space, but completing the proof requires demonstrating a highly non-trivial positivity condition.

## 6. The Gap

The exact boundary between what is known and the full solution is the lack of an unconditionally defined, naturally self-adjoint operator $H$ whose discrete spectrum mirrors $\{ \gamma \mid \zeta(1/2+i\gamma) = 0 \}$. While Connes’ construction provides a functional operator space, the final missing step is establishing the global trace formula for test functions without compact support. Proving the validity of this specific trace formula is currently mathematically equivalent to proving the Riemann Hypothesis itself.

## 7. Current Research (as of June 2026)

Active research on the Hilbert-Pólya conjecture operates across several distinct fronts:
- **Noncommutative Geometry:** Following Alain Connes, researchers are exploring the geometry of the adele class space, looking for topological or algebraic reasons that enforce the necessary positivity condition.
- **Quantum Chaos:** Physicists continue to search for a specific classical chaotic system whose periodic orbits correspond to the prime numbers, attempting to make the Berry-Keating approach mathematically rigorous.
- **PT-Symmetric Quantum Mechanics:** A newer approach championed by Carl Bender investigates non-Hermitian operators exhibiting PT-symmetry (Parity-Time reversal). These operators can have purely real spectra, offering a wider class of candidate Hamiltonians for the zeros. *(frontier — verify)*

## 8. Future Work

Leading mathematicians and physicists suggest two dominant strategies for future breakthroughs:
1. **The Field with One Element ($\mathbb{F}_1$):** Establishing a rigorous geometric theory of $\mathbb{F}_1$ could allow the Riemann zeta function to be framed as a Hasse-Weil zeta function over $\mathbb{F}_1$. This would potentially allow the spectral machinery of étale cohomology (which proved the Weil conjectures) to be ported to the integers.
2. **Physical Realizations in String Theory:** Searching for an effective Hamiltonian in condensed matter physics or string theory that naturally reduces to the $xp$ operator with the correct discrete boundary conditions arising from physical constraints rather than ad-hoc mathematical truncation.

## 9. Key References

- **[Foundational]** Montgomery, H. L. *The pair correlation of zeros of the zeta function.* Analytic Number Theory, Proc. Sympos. Pure Math., Vol. XXIV, AMS, 1973.
- **[Foundational]** Berry, M. V., and Keating, J. P. *The Riemann zeros and eigenvalue asymptotics.* SIAM Review, 1999.
- **[Foundational]** Connes, A. *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* Selecta Mathematica, 1999.
- **[SOTA / Recent]** Bender, C. M., Brody, D. C., and Müller, M. P. *Hamiltonian for the zeros of the Riemann zeta function.* Physical Review Letters, 2017.
- **[Survey]** Biane, P., Pitman, J., and Yor, M. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions.* Bulletin of the American Mathematical Society, 2001.

## 10. Worked Example / Concrete Special Case

To understand why a quantum mechanical operator is expected to relate to prime numbers, consider the structural similarity between the explicit formulas of number theory and quantum chaos. 

The Gutzwiller trace formula relates the density of states $\rho(E)$ of a quantum chaotic system to the classical periodic orbits:
$$ \rho(E) \approx \bar{\rho}(E) + \frac{1}{\pi\hbar} \sum_{p} \sum_{m=1}^{\infty} \frac{T_p}{\sqrt{|\det(M_p^m - I)|}} \cos\left( m \frac{S_p}{\hbar} - \mu_{p,m} \frac{\pi}{2} \right) $$
where $p$ indexes primitive periodic orbits, $T_p$ is the period, $S_p$ is the classical action, and $M_p$ is the monodromy matrix indicating instability.

Compare this to the Guinand-Weil explicit formula connecting the zeros $\rho = 1/2 + i\gamma$ of $\zeta(s)$ to the prime numbers:
$$ \sum_{\gamma} h(\gamma) = \frac{1}{2\pi} \int_{-\infty}^{\infty} h(r) \frac{\Gamma'}{\Gamma}\left(\frac{1}{4} + \frac{ir}{2}\right) dr - \frac{1}{2\pi} \sum_{p \text{ prime}} \sum_{m=1}^{\infty} \frac{\ln p}{p^{m/2}} \left( g(m \ln p) + g(-m \ln p) \right) + \text{const.} $$
Here, $h$ and $g$ are Fourier transform pairs. The striking mathematical alignment suggests a dictionary:
- The eigenvalues $\gamma$ correspond to the energy levels $E$.
- The primitive periodic orbits $p$ correspond to the prime numbers $p$.
- The orbit periods $T_p$ correspond to $\ln p$.
- The classical instability factor $1/\sqrt{|\det(M_p^m - I)|}$ corresponds to $1/p^{m/2}$.

If a Hamiltonian $H$ exists yielding the Riemann zeros as energy levels, its classical counterpart must have prime numbers dictating the periods of its chaotic orbits. This exact resonance is what fundamentally justifies the Hilbert-Pólya conjecture.