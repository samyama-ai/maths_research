---
id: 05-analysis/fuglede-conjecture
title: "Fuglede Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fuglede Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/fuglede-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fuglede's Conjecture (also known as the Spectral Set Conjecture) posits a deep, unexpected connection between the geometry of translational tiling and the spectral theory of partial differential operators. Specifically, the conjecture states that a measurable set $\Omega \subset \mathbb{R}^d$ of finite and positive Lebesgue measure is a spectral set (meaning the Hilbert space $L^2(\Omega)$ admits an orthogonal basis of exponential functions) if and only if $\Omega$ can tile $\mathbb{R}^d$ by translations.

The conjecture asks for an exact equivalence:
1. **Spectral condition:** Does there exist a countable set of frequencies $\Lambda \subset \mathbb{R}^d$ such that the family of exponentials $\{e^{2\pi i \langle \lambda, x \rangle}\}_{\lambda \in \Lambda}$ forms an orthogonal basis for $L^2(\Omega)$?
2. **Tiling condition:** Does there exist a countable set $T \subset \mathbb{R}^d$ such that almost every $x \in \mathbb{R}^d$ belongs to exactly one translated copy $\Omega + t$ for $t \in T$?

A complete proof or disproof requires either establishing this bi-directional implication for all dimensions and classes of sets, or providing counterexamples. While general counterexamples have been found for arbitrary disjoint sets in higher dimensions ($d \ge 3$), the conjecture remains open and heavily researched in dimensions $1$ and $2$, and has been rigorously proven for restricted geometric classes, most notably all convex bodies.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^d$ be a Lebesgue-measurable set of finite and positive measure, $0 < \mu(\Omega) < \infty$. The Hilbert space $L^2(\Omega)$ is equipped with the normalized inner product:
$$ \langle f, g \rangle_{L^2(\Omega)} = \frac{1}{\mu(\Omega)} \int_{\Omega} f(x) \overline{g(x)} \, dx $$

An exponential function corresponding to a frequency $\lambda \in \mathbb{R}^d$ is given by $e_\lambda(x) = e^{2\pi i \langle \lambda, x \rangle}$. 

**Definition (Spectral Set):** A countable set $\Lambda \subset \mathbb{R}^d$ is called a *spectrum* for $\Omega$ if the system of functions $E_\Lambda = \{ e_\lambda \}_{\lambda \in \Lambda}$ forms a complete orthogonal basis for $L^2(\Omega)$. If such a $\Lambda$ exists, $\Omega$ is termed a *spectral set*. 

Orthogonality between $e_\lambda$ and $e_{\lambda'}$ (where $\lambda \neq \lambda'$) is analytically equivalent to the Fourier transform of the indicator function $\chi_\Omega$ vanishing at the difference of the frequencies:
$$ \widehat{\chi}_{\Omega}(\lambda - \lambda') = \int_{\Omega} e^{-2\pi i \langle \lambda - \lambda', x \rangle} \, dx = 0 $$
Completeness requires that for any $f \in L^2(\Omega)$, if $\langle f, e_\lambda \rangle = 0$ for all $\lambda \in \Lambda$, then $f = 0$ almost everywhere on $\Omega$.

**Definition (Translational Tiling):** A set $\Omega$ is said to *tile* $\mathbb{R}^d$ by translations if there exists a countable set $T \subset \mathbb{R}^d$ such that the translated copies $\{ \Omega + t \}_{t \in T}$ cover almost every point in $\mathbb{R}^d$ exactly once. Formally:
$$ \sum_{t \in T} \chi_{\Omega}(x - t) = 1 \quad \text{for almost every } x \in \mathbb{R}^d $$

Fuglede's motivation was rooted in operator theory. Consider the partial derivative operators $D_j = -i \frac{\partial}{\partial x_j}$ defined initially on $C_c^\infty(\Omega)$. Fuglede proved that these operators admit mutually commuting, self-adjoint extensions to densely defined operators on $L^2(\Omega)$ if and only if $\Omega$ is a spectral set.

## 3. History & State of the Art (SOTA)

The conjecture was formulated by Bent Fuglede in 1974. In his original paper, Fuglede proved the conjecture for the restrictive case where either the translation set $T$ or the frequency set $\Lambda$ forms a full-rank lattice in $\mathbb{R}^d$. For thirty years, it was widely believed to hold for all measurable sets.

The landscape was permanently altered in 2004 when Terence Tao disproved the "spectral implies tiling" direction for $d \ge 5$. Tao translated the continuous geometric problem into a discrete combinatorics problem over finite Abelian groups. He demonstrated that a spectral set that fails to tile could be constructed in the discrete group $\mathbb{Z}_3^5$, and then lifted this discrete counterexample to a geometric union of unit cubes in $\mathbb{R}^5$.

This catalyzed a wave of breakthroughs in rapid succession:
- **Matolcsi (2005)** lowered the dimension of Tao's counterexample to $d=4$.
- **Kolountzakis and Matolcsi (2006)** further reduced the failure dimension to $d=3$.
- **Farkas, Matolcsi, and Móra (2006)** definitively disproved the converse direction ("tiling implies spectral") in dimensions $d \ge 3$ using similar discrete group methodologies.

Consequently, the general Fuglede Conjecture is false in dimensions three and higher. The state-of-the-art subsequently bifurcated into two primary directives: mapping the exact boundary of failure in low dimensions ($d=1, 2$), and establishing the conjecture for rigid topological classes. In 2022, Nir Lev and Máté Matolcsi achieved a monumental milestone, completely proving both directions of the conjecture for all convex bodies across all dimensions $d \ge 1$.

## 4. Partial Results / Verified Cases

Despite the failure of the general statement for arbitrary disjoint unions of cubes in higher dimensions, the Fuglede Conjecture holds structurally in several highly significant and rigorously verified regimes:

- **Convex Bodies (All Dimensions):** Lev and Matolcsi (2022) established that any convex domain $\Omega \subset \mathbb{R}^d$ is spectral if and only if it tiles $\mathbb{R}^d$. This represents the absolute pinnacle of current affirmative results. The tiling condition severely restricts the geometry; by Minkowski's theorem, convex tilers must be specific centrally symmetric polytopes with centrally symmetric facets.
- **Lattice Scenarios:** As proven by Fuglede (1974), if $\Omega$ tiles $\mathbb{R}^d$ with a strict lattice $T = \Lambda^*$, then it is spectral with spectrum $\Lambda$. The converse also holds if the assumed spectrum is a lattice.
- **Unions of Intervals (1D):** For subsets of $\mathbb{R}$ consisting of a union of two intervals, Izabella Łaba (2001) proved the conjecture holds. For unions of three intervals, partial results by Bownik and Casazza confirm the conjecture under mild rationally-commensurable constraints.
- **Planar Domains:** The conjecture is verified for all triangles, and more broadly, for all planar convex polygons (absorbed by the Lev-Matolcsi theorem).

## 5. Principal Obstacles

The difficulty of resolving the problem in dimensions $1$ and $2$ for arbitrary disjoint measurable sets stems from the structural limitations of finite Abelian groups and the erratic behavior of the Fourier transform for heavily disconnected geometries.

**The Discrete Group Bottleneck:** Tao's continuous-to-discrete reduction relies on transferring the spectral and tiling properties from $\mathbb{R}^d$ to $\mathbb{Z}_p^d$. Finding sets that are spectral but do not tile in $\mathbb{Z}_p^d$ requires a sufficiently large dimension $d$ to allow enough combinatorial freedom. For $d=1$ and $d=2$, the groups $\mathbb{Z}_p$ and $\mathbb{Z}_p^2$ are extremely rigid. Polynomial constraints on these low-dimensional cyclic groups make it fundamentally difficult to synthesize the necessary counterexamples.

**Analytic vs. Geometric Rigidity:** The gap between the tiling condition and the spectral condition is the gap between a strict, non-overlapping geometric packing and the purely analytic distribution of zeroes of the Fourier transform $\widehat{\chi}_\Omega$. For a highly disconnected set $\Omega = \bigcup_j \Omega_j$, the Fourier transform is a complex interference pattern:
$$ \widehat{\chi}_{\Omega}(\xi) = \sum_{j} e^{-2\pi i \langle \tau_j, \xi \rangle} \widehat{\chi}_{\Omega_j}(\xi) $$
Finding an orthogonal spectrum requires locating an infinite, uniformly dense set of common zeroes in this quasi-periodic analytic function. Traditional Harmonic Analysis techniques fail to control the zeroes of these exponential sums. The crystallographic diffraction techniques introduced by Lev and Matolcsi rely heavily on the non-vanishing curvature of the boundary of convex domains, an assumption that entirely collapses for disjoint intervals.

## 6. The Gap

The defining gap that must be crossed to resolve the remaining open cases of the conjecture lies in dimension $d=1$ for non-convex sets—specifically, finite unions of intervals $\Omega = \bigcup_{j=1}^N [a_j, b_j]$.

To solve this, researchers must establish a precise rigid link between the zeroes of the exponential polynomial $\sum_{j=1}^N c_j e^{i \omega_j x}$ (which dictates the spectral condition) and the structural periodicity required for translational tiling. Current algebraic number theory can describe the structure of these zeroes, but lacks the sharpness required to enforce a global geometric tiling lattice. A resolution requires either discovering a novel analytic identity forcing these zeroes into a lattice, or executing a massively scaled computational search in highly composite cyclic groups $\mathbb{Z}_N$ to find a counterexample.

## 7. Current Research (as of June 2026)

Current research focuses heavily on Arithmetic Combinatorics and Harmonic Analysis over finite fields.
- **Discrete Fuglede on Cyclic Groups:** Researchers are intensely dissecting the conjecture on $\mathbb{Z}_N$. The behavior of polynomials with $\{0, 1\}$ coefficients evaluated at roots of unity is a primary tool. It is known that for $N = p^k q^l$ (where $p, q$ are primes), the discrete conjecture holds, but larger composite moduli remain highly active.
- **Universal Spectra Analysis:** Research is exploring whether specific tiling sets admit a "universal spectrum" (a single set $\Lambda$ that serves as a spectrum for all translations of a tiling fundamental domain).
- **Weak Tiling Constraints:** Lev and Matolcsi successfully utilized "weak tiling" (where translated sets cover the space with a uniform non-negative integer weight $w \ge 1$ instead of $w=1$) to constrain convex bodies. Generalizing weak tiling bounds to highly disconnected sets is a major frontier.
- `*(frontier — verify)*`: Advanced SAT-solvers and integer programming algorithms are currently deployed on supercomputing clusters to search for spectral-but-non-tiling subsets in $\mathbb{Z}_N$ for highly composite moduli $N > 10^7$. Finding one would instantly translate to a counterexample in $\mathbb{R}^1$.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- **Resolve the 1D Finite Interval Case:** The most critical open question is the behavior of finite unions of intervals in $\mathbb{R}$. A definitive proof for arbitrary $k$-intervals would likely unravel the fundamental arithmetic mechanism locking the spectral zeroes to tiling sets in low dimensions.
- **The $p$-adic Fuglede Conjecture:** Formulating and solving the conjecture in the local fields $\mathbb{Q}_p$, where the underlying ultra-metric geometry simplifies certain Fourier analytic obstructions, potentially offering a mirror to understand the Euclidean case.
- **Riesz Bases of Exponentials:** A more flexible, perturbation-friendly variation of the conjecture asks when $L^2(\Omega)$ admits a *Riesz basis* of exponentials. Relaxing strict orthogonality to bounded invertibility may bridge the gap and classify general measurable sets without requiring perfect translational tiling.

## 9. Key References

- **[Foundational]** Fuglede, B. *Commuting self-adjoint partial differential operators and a group theoretic problem.* Journal of Functional Analysis, 1974.
- **[Foundational]** Tao, T. *Fuglede's conjecture is false in 5 and higher dimensions.* Mathematical Research Letters, 2004.
- **[SOTA / Recent]** Lev, N., and Matolcsi, M. *The Fuglede conjecture for convex domains is true in all dimensions.* Acta Mathematica, 2022.
- **[SOTA / Recent]** Farkas, B., Matolcsi, M., and Móra, P. *On Fuglede's conjecture and the existence of universal spectra.* Journal of Fourier Analysis and Applications, 2006.
- **[Survey]** Kolountzakis, M. N. *The study of translational tiling with Fourier Analysis.* Fourier Analysis and Convexity, 2004.

## 10. Worked Example / Concrete Special Case

The simplest and most concrete mathematical instance of the Fuglede Conjecture is the one-dimensional unit interval, $\Omega = [0, 1) \subset \mathbb{R}$. 

**1. Verification of the Tiling Condition:**
It is elementary that $\Omega$ tiles $\mathbb{R}$ by translations. Let the translation set be the integers, $T = \mathbb{Z}$. The translated copies are exactly the intervals $[n, n+1)$.
$$ \sum_{n \in \mathbb{Z}} \chi_{[0,1)}(x - n) = 1 \quad \text{for all } x \in \mathbb{R} $$
Thus, almost every point in $\mathbb{R}$ is covered exactly once without overlap.

**2. Verification of the Spectral Condition:**
Fuglede's Conjecture dictates that $\Omega$ must be a spectral set. We select the spectrum $\Lambda = \mathbb{Z}$. The corresponding exponential functions are $e_n(x) = e^{2\pi i n x}$ for $n \in \mathbb{Z}$. 
To verify orthogonality in $L^2([0,1))$, we compute the inner product for $n \neq m$:
$$ \langle e_n, e_m \rangle = \int_0^1 e^{2\pi i n x} \overline{e^{2\pi i m x}} \, dx = \int_0^1 e^{2\pi i (n - m) x} \, dx $$
Evaluating this integral yields:
$$ \left[ \frac{e^{2\pi i (n - m) x}}{2\pi i (n - m)} \right]_0^1 = \frac{e^{2\pi i (n - m)} - 1}{2\pi i (n - m)} $$
Since $n-m$ is a non-zero integer, $e^{2\pi i (n - m)} = 1$, and thus:
$$ \langle e_n, e_m \rangle = \frac{1 - 1}{2\pi i (n - m)} = 0 $$
When $n = m$, the integral is trivially $\int_0^1 1 \, dx = 1$. The classical theory of Fourier series over a finite interval guarantees that $\{ e^{2\pi i n x} \}_{n \in \mathbb{Z}}$ is dense in $L^2([0,1))$. Therefore, it forms a complete orthogonal basis, and $\Omega$ is confirmed to be a spectral set.

**3. The Analytic Link (Fourier Zeroes):**
The underlying mechanism linking these two conditions is found in the Fourier transform of the indicator function $\chi_{[0,1)}$:
$$ \widehat{\chi}_{[0,1)}(\xi) = \int_0^1 e^{-2\pi i \xi x} \, dx = e^{-\pi i \xi} \frac{\sin(\pi \xi)}{\pi \xi} $$
The zeroes of this function are exactly the non-zero integers, $\xi \in \mathbb{Z} \setminus \{0\}$. The orthogonality of our basis relies precisely on the fact that the difference between any two distinct frequencies in our spectrum $\Lambda$ must land on a zero of the Fourier transform. Since $\Lambda = \mathbb{Z}$, the difference $\lambda_1 - \lambda_2 = n - m \in \mathbb{Z} \setminus \{0\}$, which matches the zeroes perfectly. This perfectly aligns the algebraic structure of the spectrum with the analytic zeroes dictated by the geometric shape of the tiling domain.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*