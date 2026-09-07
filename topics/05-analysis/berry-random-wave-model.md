---
id: 05-analysis/berry-random-wave-model
title: "Berry Random Wave Model"
topic: 05-analysis
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Berry Random Wave Model

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/berry-random-wave-model` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Let $(M,g)$ be a compact Riemannian manifold of dimension $n$ whose geodesic flow is chaotic (ergodic, ideally Anosov). Let $\{\varphi_j\}$ be an $L^2$-orthonormal basis of Laplace eigenfunctions,
$$-\Delta_g \varphi_j = \lambda_j \varphi_j, \qquad \lambda_1 \le \lambda_2 \le \cdots \to \infty .$$

**Berry's Random Wave Conjecture (RWC).** In the high-energy limit $\lambda_j \to \infty$, a typical $\varphi_j$ behaves locally like a *monochromatic isotropic Gaussian random field*. Precisely: fix $x_0 \in M$, work in geodesic normal coordinates, and rescale
$$\varphi_j^{x_0}(y) \;:=\; \varphi_j\!\left(\exp_{x_0}\!\big(y/\sqrt{\lambda_j}\big)\right), \qquad y \in \mathbb{R}^n .$$
Then along a density-one subsequence $\varphi_j^{x_0}$ converges — in distribution with respect to the randomness of $x_0$ (or of $j$), in $C^\infty_{\mathrm{loc}}(\mathbb{R}^n)$ — to the stationary Gaussian field $\Phi$ on $\mathbb{R}^n$ with covariance
$$\mathbb{E}\big[\Phi(y)\Phi(y')\big] \;=\; \int_{S^{n-1}} e^{i\langle \xi,\, y-y'\rangle}\, d\sigma(\xi) \;=\; c_n \frac{J_{(n-2)/2}(|y-y'|)}{|y-y'|^{(n-2)/2}} .$$

A complete resolution requires either a proof of this local weak-$*$ convergence for a natural class of chaotic $(M,g)$, or a counterexample: a chaotic manifold and a density-one family whose local scaling limits are provably non-Gaussian. Weaker, still-open corollaries include the predicted asymptotics for nodal volume, nodal domain count, and value distribution of $\varphi_j$.

## 2. Mathematical Foundations

**The limit field.** $\Phi$ is the centred Gaussian field on $\mathbb{R}^n$ with spectral measure the uniform measure $\sigma$ on the unit sphere; equivalently $\Delta \Phi + \Phi = 0$ almost surely. In $n=2$,
$$K(y,y') = J_0(|y-y'|), \qquad K(0)=1,\quad \partial_{y_i}\partial_{y_j} K\big|_{y=y'} = \tfrac12 \delta_{ij}.$$
$\Phi$ is stationary, isotropic, ergodic under translations, and real-analytic.

**Quantum ergodicity (QE) — the proven shadow.** Shnirelman–Zelditch–Colin de Verdière: if the geodesic flow is ergodic there is a density-one subsequence with
$$\int_M a\,|\varphi_{j_k}|^2\,d\mathrm{vol} \;\longrightarrow\; \frac{1}{\mathrm{vol}(M)}\int_M a\,d\mathrm{vol}, \qquad a \in C(M).$$
QE controls the *first* microlocal moment; RWC is a statement about *all* joint moments of $(\varphi_j, \nabla\varphi_j, \nabla^2\varphi_j,\dots)$ at scale $\lambda_j^{-1/2}$, i.e. about Gaussianity, not just equidistribution.

**Kac–Rice / nodal predictions.** For $\Phi$ in $n=2$, the expected nodal length per unit area for an eigenfunction of eigenvalue $\lambda$ is
$$\mathcal{H}^1\text{-density} \;=\; \frac{\sqrt{\lambda}}{2\sqrt{2}} ,$$
and Nazarov–Sodin give a *nodal domain constant* $c_{\mathrm{NS}}>0$ with
$$\frac{\\#\{\text{nodal domains}\}}{\lambda} \;\longrightarrow\; c_{\mathrm{NS}}\cdot \frac{\mathrm{vol}(M)}{4\pi}\ \ (\text{predicted}).$$
Berry further predicted $L^p$ and sup-norm behaviour $\|\varphi_j\|_\infty \asymp \sqrt{\log \lambda_j}$ and Gaussian value distribution $|\{x: \varphi_j(x) > t\}| \to \mathrm{vol}(M)\,\mathbb{P}(N(0,1)>t)$.

**Berry cancellation.** For the boundary-corrected model Berry (2002) predicted that the nodal-length variance is suppressed by a full power of $\lambda$: $\mathrm{Var} \sim c\,\lambda \log \lambda$ instead of the naive $\lambda^{3/2}$ — a cancellation of the leading Wiener chaos, later confirmed rigorously in arithmetic settings.

## 3. History & State of the Art (SOTA)

- **1977.** Michael Berry, *Regular and irregular semiclassical wavefunctions* (J. Phys. A), introduces the model as a semiclassical heuristic: a chaotic eigenstate is a superposition of plane waves of fixed wavenumber with random phases and isotropic directions.
- **1992.** Hejhal–Rackner test the model numerically against Maass forms on $\mathrm{PSL}(2,\mathbb{Z})\backslash\mathbb{H}$ — value distributions match Gaussian to high accuracy.
- **2002.** Bogomolny–Schmit map nodal domains of the random wave onto critical bond percolation, predicting $c_{\mathrm{NS}} \approx 0.0624$ and the full nodal-domain size distribution.
- **2002.** Berry computes nodal-line statistics with perimeter corrections and finds the variance cancellation.
- **2009–2016.** Nazarov–Sodin prove existence and positivity of the nodal domain constant for random spherical harmonics and, in general, for translation-invariant Gaussian fields — the model's own predictions become theorems, independent of any eigenfunction.
- **2013–2016.** Arithmetic random waves (toral eigenfunctions with random Gaussian coefficients): Krishnapur–Kurlberg–Wigman compute nodal-length variance and confirm Berry cancellation; Marinucci–Peccati–Rossi–Wigman show the limiting law is *non-Gaussian* (second chaos), i.e. arithmetic structure breaks universality at the fluctuation level.
- **2014.** Bourgain proves a partial de-randomization: individual toral eigenfunctions with sufficiently equidistributed lattice-point sets inherit random-wave nodal-length asymptotics.
- **2018–2020.** Abert–Bergeron–Le Masson prove a Benjamini–Schramm/"random wave" statement for eigenfunctions on sequences of hyperbolic surfaces with injectivity radius $\to\infty$. Canzani–Hanin establish $C^\infty$ scaling asymptotics for the spectral projector and local universality for zeros/critical points of *Gaussian monochromatic waves* on any manifold.
- **2019–2022.** Ingremeau–Rivera: rigorous lower bound on the Bogomolny–Schmit constant; and a proof that Lagrangian states evolved by an Anosov flow converge to random waves.

## 4. Partial Results / Verified Cases

- **Random models (fully solved).** For the Gaussian ensemble itself — random spherical harmonics on $S^2$, arithmetic random waves on $\mathbb{T}^2$, Riemannian random waves on any $(M^n,g)$ — the nodal volume $\mathbb{E}[\mathcal{H}^{n-1}] = c_n\sqrt{\lambda}\,\mathrm{vol}(M)$, the nodal-domain law $\\#/\lambda \to c_{\mathrm{NS}}\,\mathrm{vol}/(4\pi)$ with $c_{\mathrm{NS}}>0$ (Nazarov–Sodin, *Amer. J. Math.* 2009; *ZhMFAG* 2016), and local $C^\infty$ universality (Canzani–Hanin 2020) are theorems. These verify the model's *internal* consistency, not the conjecture.
- **Torus $\mathbb{T}^2$, $n=2$.** Nodal-length variance $\mathrm{Var} \sim \frac{c\,\lambda}{\mathcal{N}^2}\ (\mathcal N = $ number of lattice points on the circle of radius $\sqrt\lambda$), confirming Berry cancellation; limit law non-Gaussian (MPRW, *GAFA* 2016). Buckley–Wigman: nodal-domain counts for arithmetic random waves.
- **Deterministic eigenfunctions, torus.** Bourgain (*Israel J. Math.* 2014): for eigenvalues whose lattice points equidistribute, individual eigenfunctions satisfy $\int_{\mathbb{T}^2}\varphi^4 \to 3(\int \varphi^2)^2$ — the Gaussian fourth moment.
- **Large-genus / large injectivity radius hyperbolic surfaces.** Abert–Bergeron–Le Masson (2018): eigenfunctions on a Benjamini–Schramm convergent sequence of hyperbolic surfaces converge to the hyperbolic random wave in the appropriate averaged sense — a genuine RWC theorem, but with the *sequence of surfaces* varying, not a single fixed $M$.
- **Anosov dynamics, Lagrangian initial data.** Ingremeau–Rivera (2022): for a fixed Anosov manifold, quasimodes obtained by long-time propagation of a Lagrangian state converge in law to the Berry field. This is the strongest single-manifold result and covers a *specific construction*, not a basis of eigenfunctions.
- **Quantum unique ergodicity, arithmetic case.** Lindenstrauss (*Ann. of Math.* 2006) and Soundararajan for the full modular surface: the first-moment part of the picture is unconditional for Hecke–Maass forms; Gaussian moments are known only under GRH-type or holomorphic analogues.

## 5. Principal Obstacles

- **No mechanism produces randomness for a fixed operator.** $-\Delta_g$ on a fixed $M$ is deterministic; the conjecture asserts an emergent statistical law over a density-one subsequence. Every proof technique (QE, entropy bounds, trace formulas) accesses only *averages over the spectrum in a window*, which control low moments but never rule out rigid, non-Gaussian correlations in the remaining eigenfunctions.
- **Higher moments need long-time dynamics.** Controlling the $k$-th moment of $\varphi_j$ at scale $\lambda^{-1/2}$ requires the semiclassical propagator up to Ehrenfest time $\sim \frac{1}{2\Lambda}\log\lambda$ and beyond. Beyond Ehrenfest time the Egorov approximation loses control; the exponential proliferation of geodesic loops is exactly the regime where the model must be validated, and no known parametrix survives it.
- **Arithmetic obstructions are real.** MPRW's non-Gaussian nodal-length limit on $\mathbb{T}^2$ proves that "random wave" universality genuinely fails at the level of fluctuations for integrable/arithmetic backgrounds. So the conjecture cannot be a soft consequence of any dimension-count or general-position argument.
- **Nodal-domain counting is not a local functional.** $\\#$ of components is unstable under $C^\infty_{\mathrm{loc}}$ perturbation: a small change can merge or split domains across the whole manifold. Nazarov–Sodin's integral-geometric sandwich needs *stationarity and ergodicity* of the limit field — properties one cannot assume when the "field" is a single eigenfunction.
- **Percolation heuristic lacks a rigorous frame.** The Bogomolny–Schmit correspondence requires an RSW-type box-crossing theory for a field with slowly decaying, sign-changing correlations $J_0(r) \sim \sqrt{2/\pi r}\cos(r - \pi/4)$; standard FKG/quasi-independence tools (Beffara–Gayet, Rivera–Vanneuville) demand faster decay than $r^{-1/2}$.

## 6. The Gap

Proven: (i) everything about the Gaussian ensemble itself; (ii) first-moment equidistribution (QE/QUE) for real eigenfunctions; (iii) fourth-moment Gaussianity on $\mathbb{T}^2$ under equidistribution of lattice points; (iv) full RWC when either the *manifold* varies (Benjamini–Schramm) or the *state* is a propagated Lagrangian rather than an eigenfunction.

Missing: a single fixed compact chaotic $(M,g)$ — say a hyperbolic surface or the Bunimovich stadium — together with a density-one subsequence of *genuine* eigenfunctions whose $k$-th local moments converge to the Gaussian values for some $k \ge 3$. The precise barrier is the passage from *one* microlocal average (QE) to *joint* microlocal averages at separated points, which requires controlling
$$\sum_{|\lambda_j - \lambda| \le 1} \varphi_j(x_1)\cdots\varphi_j(x_k)$$
with $|x_i - x_l| \sim \lambda^{-1/2}$, i.e. off-diagonal terms in the $k$-point trace formula — currently intractable past $k=2$.

## 7. Current Research (as of June 2026)

- **Large-genus random surfaces.** Weil–Petersson random hyperbolic surfaces (Mirzakhani–Petri; Wu–Xue; Lipnowski–Wright) combined with Abert–Bergeron–Le Masson give RWC statements with high probability as genus $\to\infty$; extending to nodal-domain counts is active. *(frontier — verify)*
- **Quantitative QE and higher moments.** Groups around Le Masson, Sahlsten, Dyatlov and Jin are pushing delocalisation and fractal-uncertainty methods toward third and fourth moments on fixed Anosov surfaces. *(frontier — verify)*
- **Nodal-domain constants.** Numerical and rigorous refinements of $c_{\mathrm{NS}}$ (Nastasescu; Konrad; Beliaev–Kereta; Priya) show the Bogomolny–Schmit percolation value $0.0624$ is *not* exact; improved two-sided bounds via Ingremeau–Rivera's method are being sharpened.
- **Percolation for smooth fields.** Muirhead, Rivera, Vanneuville, Severo: sharp phase transition and RSW for planar Gaussian fields with $\alpha$-decay; the Bessel kernel case remains the target.
- **Arithmetic random waves beyond $n=2$.** Nodal-volume variance and non-universality on $\mathbb{T}^3$ and higher (Cammarota, Benatar, Maffucci, Rossi).

## 8. Future Work

- Prove a **third-moment theorem** on a fixed hyperbolic surface: $\mathbb{E}_{x}\big[\varphi_j(x)^3\big] \to 0$ at scale $\lambda^{-1/2}$ with a quantitative rate.
- Establish **RSW box-crossing** for $J_0$-correlated planar fields, which would upgrade Nazarov–Sodin positivity to sharp nodal-domain fluctuation results.
- Identify the correct **error term** in the Bogomolny–Schmit prediction — is $c_{\mathrm{NS}}$ expressible in closed form at all, or is it a genuinely non-algebraic constant?
- Determine whether RWC holds for **Hecke–Maass forms** given full arithmetic QUE, or whether Hecke relations impose visible non-Gaussianity (Sarnak's question on higher moments of $|\varphi|^2$).
- Sharpen $L^\infty$: prove $\|\varphi_j\|_\infty = O(\lambda^{\epsilon})$ on negatively curved manifolds, far from the predicted $\sqrt{\log\lambda}$; current best is the Bérard $\sqrt{\lambda}/\sqrt{\log\lambda}$ improvement.

## 9. Key References

- **[Foundational]** M. V. Berry. *Regular and irregular semiclassical wavefunctions.* Journal of Physics A: Mathematical and General, 10(12):2083–2091, 1977.
- **[Foundational]** M. V. Berry. *Statistics of nodal lines and points in chaotic quantum billiards: perimeter corrections, fluctuations, curvature.* Journal of Physics A, 35(13):3025–3038, 2002.
- **[Foundational]** E. Bogomolny, C. Schmit. *Percolation model for nodal domains of chaotic wave functions.* Physical Review Letters, 88:114102, 2002.
- **[Foundational]** F. Nazarov, M. Sodin. *On the number of nodal domains of random spherical harmonics.* American Journal of Mathematics, 131(5):1337–1357, 2009.
- **[SOTA]** F. Nazarov, M. Sodin. *Asymptotic laws for the spatial distribution and the number of connected components of zero sets of Gaussian random functions.* Journal of Mathematical Physics, Analysis, Geometry, 12(3):205–278, 2016.
- **[SOTA]** M. Krishnapur, P. Kurlberg, I. Wigman. *Nodal length fluctuations for arithmetic random waves.* Annals of Mathematics, 177(2):699–737, 2013.
- **[SOTA]** D. Marinucci, G. Peccati, M. Rossi, I. Wigman. *Non-universality of nodal length distribution for arithmetic random waves.* Geometric and Functional Analysis, 26(3):926–960, 2016.
- **[SOTA]** J. Bourgain. *On toral eigenfunctions and the random wave model.* Israel Journal of Mathematics, 201(2):611–630, 2014.
- **[SOTA]** M. Abert, N. Bergeron, E. Le Masson. *Eigenfunctions and random waves in the Benjamini–Schramm limit.* Preprint, arXiv:1810.05601, 2018.
- **[SOTA]** Y. Canzani, B. Hanin. *Local universality for zeros and critical points of monochromatic random waves.* Communications in Mathematical Physics, 378:1677–1712, 2020.
- **[SOTA]** M. Ingremeau, A. Rivera. *A lower bound for the Bogomolny–Schmit constant for random monochromatic plane waves.* Mathematical Research Letters, 26(4):1179–1186, 2019.
- **[SOTA]** M. Ingremeau, A. Rivera. *How Lagrangian states evolve into random waves.* Journal de l'École polytechnique — Mathématiques, 9:177–215, 2022.
- **[Related]** E. Lindenstrauss. *Invariant measures and arithmetic quantum unique ergodicity.* Annals of Mathematics, 163(1):165–219, 2006.
- **[Numerics]** D. Hejhal, B. Rackner. *On the topography of Maass waveforms for PSL(2,Z).* Experimental Mathematics, 1(4):275–305, 1992.
- **[Survey]** I. Wigman. *On the nodal structures of random fields — a decade of results.* Journal of Applied and Computational Topology, 2023.
- **[Survey]** S. Zelditch. *Eigenfunctions of the Laplacian on a Riemannian Manifold.* CBMS Regional Conference Series in Mathematics 125, American Mathematical Society, 2017.

## 10. Worked Example / Concrete Special Case

**Expected nodal length of the planar Berry wave, and the prediction it makes.**

Take $n=2$, $\lambda = 1$. The Berry field $\Phi$ on $\mathbb{R}^2$ has covariance $K(r) = J_0(r)$ with $J_0(r) = 1 - \frac{r^2}{4} + \frac{r^4}{64} - \cdots$. Hence

$$\mathrm{Var}\,\Phi(0) = K(0) = 1, \qquad \mathrm{Var}\,\partial_i\Phi(0) = -\partial_i^2 K\big|_{0} = \tfrac12,$$

and $\partial_1\Phi(0), \partial_2\Phi(0), \Phi(0)$ are mutually independent (isotropy kills the cross terms; stationarity gives $\mathbb{E}[\Phi\,\partial_i\Phi]=0$).

Apply the Kac–Rice formula for the expected $1$-dimensional Hausdorff measure of $\Phi^{-1}(0)$ in a domain $D$:
$$\mathbb{E}\,\mathcal{H}^1\!\left(\Phi^{-1}(0)\cap D\right) \;=\; |D| \cdot p_{\Phi(0)}(0)\cdot \mathbb{E}\big[\,|\nabla \Phi(0)|\,\big].$$

- $p_{\Phi(0)}(0) = \frac{1}{\sqrt{2\pi}}$.
- $|\nabla\Phi(0)|$ is Rayleigh with scale $\sigma = 1/\sqrt2$, so $\mathbb{E}|\nabla\Phi(0)| = \sigma\sqrt{\pi/2} = \frac{1}{\sqrt2}\sqrt{\pi/2} = \frac{\sqrt{\pi}}{2}$.

Therefore the nodal length density is
$$\frac{1}{\sqrt{2\pi}}\cdot\frac{\sqrt{\pi}}{2} \;=\; \frac{1}{2\sqrt2} \approx 0.35355 .$$

Rescaling to eigenvalue $\lambda$ (i.e. $\Phi(\sqrt{\lambda}\,y)$) multiplies lengths by $\sqrt{\lambda}$:
$$\boxed{\ \mathbb{E}\,\mathcal{H}^1(\Phi^{-1}(0)\cap D) = \frac{\sqrt{\lambda}}{2\sqrt2}\,|D| \ }$$

**What the conjecture asserts.** For a chaotic surface $M$ of area $A$, RWC predicts that a density-one subsequence of eigenfunctions satisfies
$$\mathcal{H}^1\!\left(\varphi_j^{-1}(0)\right) \;\sim\; \frac{A}{2\sqrt2}\,\sqrt{\lambda_j}.$$

**Status of that prediction.** Only two-sided bounds of the right order are known unconditionally: Donnelly–Fefferman gives $c\sqrt\lambda \le \mathcal{H}^1(\varphi^{-1}(0)) \le C\sqrt\lambda$ for real-analytic metrics, and Logunov (*Ann. of Math.* 2018) gives $\mathcal H^{n-1} \ge c\sqrt\lambda$ plus a polynomial upper bound $\lambda^{\alpha}$ in the smooth case. The *constant* $\frac{1}{2\sqrt2}$ is not known for a single eigenfunction on a single chaotic manifold. This numerical gap — between "order $\sqrt\lambda$" and "exactly $\frac{A}{2\sqrt2}\sqrt\lambda$" — is the concrete form of the gap described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*