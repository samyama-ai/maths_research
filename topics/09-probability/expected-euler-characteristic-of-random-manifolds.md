---
id: 09-probability/expected-euler-characteristic-of-random-manifolds
title: "Expected Euler Characteristic of Random Manifolds"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Expected Euler Characteristic of Random Manifolds

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/expected-euler-characteristic-of-random-manifolds` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a compact $N$-dimensional manifold and let $f = (f_1,\dots,f_k)$ be a random smooth map $M \to \mathbb{R}^k$. Two families of random manifolds arise: the **excursion set** $A_u(f,M) = \{x \in M : f(x) \ge u\}$ (for $k=1$), and the **random submanifold** $Z = f^{-1}(0)$ of codimension $k$. The problem is to compute, or sharply estimate, the expected Euler characteristic
$$\mathbb{E}\big[\chi(A_u(f,M))\big], \qquad \mathbb{E}\big[\chi(f^{-1}(0))\big],$$
and to determine when these expectations control the actual topology.

Three distinct questions are open to different degrees:

1. **(Exact formulas.)** For which classes of random fields beyond Gaussian and Gaussian-related is there a closed-form expression for $\mathbb{E}[\chi(A_u)]$ as a finite sum of geometric invariants of $M$ times universal functions of $u$?
2. **(The Euler characteristic heuristic.)** For which fields and which thresholds $u$ is $\mathbb{E}[\chi(A_u)]$ an exponentially accurate approximation to $\mathbb{P}\{\sup_M f \ge u\}$?
3. **(Random submanifolds.)** For random real algebraic and band-limited random-wave models, determine the leading constants — and the fluctuations — of $\mathbb{E}[\chi(Z)]$ and of the individual Betti numbers $\mathbb{E}[b_i(Z)]$.

A complete resolution requires: for (1), a Kac–Rice-type identity valid without Gaussian conditioning; for (2), proof or refutation of exponential-order accuracy in the non-Gaussian and non-smooth regimes; for (3), identification of the constants, which are currently only known to exist.

## 2. Mathematical Foundations

**Setting.** Let $(M,g)$ be a compact $C^2$ Whitney-stratified $N$-manifold. Let $f$ be a centered, unit-variance Gaussian field on $M$, a.s. $C^2$, with non-degenerate joint distributions. Endow $M$ with the **induced (Riemannian) metric**
$$g_x(X,Y) := \mathbb{E}\big[(Xf)(x)\,(Yf)(x)\big], \qquad X,Y \in T_xM .$$

**Lipschitz–Killing curvatures.** For $(M,g)$ define $\mathcal{L}_0,\dots,\mathcal{L}_N$ by the tube formula: for small $\rho>0$,
$$\mathrm{Vol}_g\big(\{x : d_g(x,M)\le \rho\}\big) = \sum_{j=0}^{N} \omega_{N+\ell-j}\,\rho^{N+\ell-j}\,\mathcal{L}_j(M),$$
with $\mathcal{L}_0(M)=\chi(M)$ and $\mathcal{L}_N(M)=\mathrm{Vol}_g(M)$.

**Gaussian Kinematic Formula (GKF).** Taylor (2006), extending Adler–Taylor (2003): for $f$ as above,
$$\boxed{\ \mathbb{E}\big[\chi(A_u(f,M))\big] \;=\; \sum_{j=0}^{N} \mathcal{L}_j(M)\,\rho_j(u)\ }$$
where the **Euler characteristic densities** are
$$\rho_0(u) = \Psi(u) := \int_u^\infty \frac{e^{-t^2/2}}{\sqrt{2\pi}}\,dt, \qquad \rho_j(u) = (2\pi)^{-(j+1)/2} H_{j-1}(u)\, e^{-u^2/2},\ j\ge 1,$$
and $H_{j}$ is the Hermite polynomial ($H_{-1}(u):=e^{u^2/2}\Psi(u)$, $H_0=1$, $H_1(u)=u$, $H_2(u)=u^2-1$).

**Kac–Rice / Morse-theoretic origin.** For a Morse function, $\chi(A_u) = \sum_{x:\,\nabla f(x)=0,\ f(x)\ge u} (-1)^{\mathrm{ind}(x)}$, so
$$\mathbb{E}[\chi(A_u)] = \int_M \mathbb{E}\Big[\det(-\nabla^2 f(x))\,\mathbf{1}_{\{f(x)\ge u\}}\,\Big|\,\nabla f(x)=0\Big]\, p_{\nabla f(x)}(0)\, \mathrm{Vol}_g(dx).$$
For isotropic Gaussian fields the conditional Hessian is a shifted GOE matrix, and the inner expectation reduces to a Gaussian expectation of $\det$ of a GOE matrix — the source of the Hermite polynomials.

**Random submanifolds.** For $f$ Gaussian with values in $\mathbb{R}^k$ and $Z=f^{-1}(0)$ of even dimension $N-k$, Chern–Gauss–Bonnet plus Kac–Rice gives
$$\mathbb{E}[\chi(Z)] = \int_M \mathbb{E}\big[\,\mathrm{Pf}\text{-type functional of }\nabla^2 f \mid f(x)=0\,\big]\,p_{f(x)}(0)\,\mathrm{Vol}(dx).$$

**Euler characteristic heuristic.** With $u\to\infty$, one hopes
$$\Big|\mathbb{P}\{\textstyle\sup_M f \ge u\} - \mathbb{E}[\chi(A_u)]\Big| \le C\, e^{-\alpha u^2/2}, \qquad \alpha > 1 .$$

## 3. History & State of the Art (SOTA)

- **1945–1957.** Rice's formula for level crossings of stationary processes; Kac's counting formula for real roots.
- **1970s–1981.** Adler and Hasofer compute $\mathbb{E}[\chi]$ of excursion sets of stationary Gaussian fields on $\mathbb{R}^N$; consolidated in Adler, *The Geometry of Random Fields* (1981), which also proposes the Euler characteristic as a supremum-tail surrogate.
- **1990s.** Worsley extends the computation to $\chi^2$, $t$ and $F$ fields, driven by neuroimaging thresholding (SPM software). This makes the formula a working statistical tool.
- **2003.** Taylor and Adler prove the manifold version: $\mathbb{E}[\chi(A_u)]$ on a Riemannian manifold is a finite sum over Lipschitz–Killing curvatures.
- **2005.** Taylor, Takemura and Adler prove the heuristic is exponentially accurate for smooth Gaussian fields: the error is $O(e^{-\alpha u^2/2})$ with $\alpha>1$ explicit.
- **2006.** Taylor's Gaussian Kinematic Formula unifies all Gaussian-related cases: for $F = F(f_1,\dots,f_m)$ with $F$ a nice subset of $\mathbb{R}^m$, $\mathbb{E}[\mathcal{L}_i(M\cap f^{-1}F)]$ is a finite sum $\sum_j \binom{i+j}{j}\omega\text{-factors}\,\mathcal{L}_{i+j}(M)\,\mathcal{M}_j^{\gamma}(F)$ with Gaussian Minkowski functionals $\mathcal{M}_j^\gamma$.
- **2007–2016.** Algebraic side: Bürgisser computes average Euler characteristics of random real algebraic varieties; Podkorytov, Gayet–Welschinger and Letendre obtain $d^{N/2}$-order asymptotics for Kostlan models.
- **2009–2019.** Nazarov–Sodin, Sarnak–Wigman, Canzani–Sarnak establish laws of large numbers for numbers of nodal components and their nesting/topology types, with constants defined only implicitly.

## 4. Partial Results / Verified Cases

- **Smooth Gaussian fields on compact stratified $C^2$ manifolds, all $N$, all $u$:** GKF gives an exact, finite, closed-form answer (Adler–Taylor 2003; Taylor 2006). Extends to manifolds with boundary and corners.
- **Gaussian-related fields:** $\chi^2_k$, $t$, $F$, Hotelling $T^2$, and general $C^2$ functionals of finitely many i.i.d. Gaussian fields — exact densities $\rho_j$ computed (Worsley 1994; Taylor–Worsley 2007).
- **Heuristic accuracy:** proven for a.s. $C^2$ Gaussian fields with constant variance; error term $O(e^{-u^2(1+\alpha)/2})$ where $\alpha$ depends on the critical-radius/curvature of the associated Gaussian tube (Taylor–Takemura–Adler 2005).
- **Random spherical harmonics on $S^2$:** all quantities in the GKF are explicit for degree $\ell$; $\mathbb{E}[\chi(A_u)]$ known exactly for every $\ell$ and $u$ (Section 10).
- **Kostlan random hypersurfaces $Z_d \subset \mathbb{RP}^n$:** $\mathbb{E}[\chi(Z_d)] = \Theta(d^{n/2})$ for $n$ odd (so $\dim Z_d$ even); leading constant computed by Bürgisser (2007) and, for general codimension $r$ and general Kähler ambient, by Letendre (2016): $\mathbb{E}[\chi(Z_d)] \sim e_{n,r}\, d^{n/2}\,\mathrm{Vol}(M)$ with $e_{n,r}$ an explicit Gaussian-matrix integral. For $\dim Z_d$ odd, $\chi \equiv 0$ and the statement is vacuous.
- **Betti-number bounds:** Gayet–Welschinger prove $\mathbb{E}[b_i(Z_d)] \le c\, d^{n/2}$ and matching lower bounds of order $d^{n/2}$ for Kostlan models (2014, 2016), using barrier/quantitative-transversality plus GOE determinant estimates.
- **Nodal component counts:** Nazarov–Sodin: for random spherical harmonics of degree $\ell$, the number of nodal domains is $(c_{NS}+o(1))\,\ell^2$ in $L^1$ and a.s., with $c_{NS}>0$ existing but not evaluated.
- **Critical points:** Nicolaescu (2015) computes the expected number and index distribution of critical points of random smooth functions on compact manifolds, recovering $\mathbb{E}[\chi]$ as an alternating sum.

## 5. Principal Obstacles

- **Gaussianity is structural, not technical.** The GKF rests on two Gaussian facts: (i) $f(x)$ and $\nabla f(x)$ are independent at each point under constant variance; (ii) conditional Hessians are shifted GOE matrices with computable $\mathbb{E}[\det]$. Both fail for non-Gaussian fields, and no substitute for $\mathbb{E}[\det(\text{Hessian})]$ is known in general.
- **Euler characteristic collapses at low thresholds.** $\chi$ is an alternating sum; near $u=0$ massive cancellation makes $\mathbb{E}[\chi]$ an $O(1)$ quantity while individual $b_i$ grow polynomially. So the exact formula carries no information exactly where topology is richest.
- **Betti numbers are not Kac–Rice-computable.** $b_i$ is not a local integral of jet data; no integral-geometric formula of Kac–Rice type exists for $\mathbb{E}[b_i]$. Only sandwich bounds via Morse inequalities are available, and these are lossy by constant factors.
- **Fluctuation control.** Second-moment methods for $\chi$ and $b_i$ require four-point correlations of critical points; the associated Kac–Rice integrands are singular on the diagonal, and integrability is only established under strong non-degeneracy.
- **Implicit constants.** Nazarov–Sodin constants and the nesting/topology-type measures of Sarnak–Wigman are defined as limits of local models on $\mathbb{R}^n$ with no known closed form — even $c_{NS}$ for $S^2$ is only bracketed numerically.
- **Low regularity.** GKF requires a.s. $C^2$ sample paths; for fields with $C^{1,\alpha}$ paths (many fractional and Lévy-type models) $\chi(A_u)$ may be a.s. infinite or ill-defined.

## 6. The Gap

The exact formula (Section 4, GKF) and the general question (Section 1) diverge in three precise places.

1. **Beyond Gaussian-related fields.** GKF covers $F(f_1,\dots,f_m)$ with $f_i$ i.i.d. Gaussian. For a genuinely non-Gaussian field — e.g. shot-noise, Poisson-driven, or the modulus of a non-Gaussian ensemble — the missing step is a replacement for the identity $\mathbb{E}[\det(-\nabla^2 f)\mid \nabla f=0,\ f=u]$ as a polynomial in $u$. It is not known whether any non-Gaussian class admits a *finite* expansion in $\mathcal{L}_j(M)$.
2. **From $\chi$ to $(b_0,\dots,b_N)$.** Everything proven concerns the alternating sum. The gap is a method that separates the Morse indices, i.e. computes $\mathbb{E}[\\#\{\text{critical points of index } i,\ f\ge u\}]$ with error small enough to pin $\mathbb{E}[b_i]$ rather than bound it. Nicolaescu's index densities give $\mathbb{E}$ of critical counts, but Morse inequalities lose the sharp constants.
3. **Constants versus orders.** Random algebraic and band-limited models are known to $\Theta(d^{n/2})$ or $\Theta(\ell^n)$ order with existence of the limiting constant; evaluating that constant — or even proving it is irrational/transcendental — is entirely open.

## 7. Current Research (as of June 2026)

- **Stanford / Technion school (Taylor, Adler and collaborators).** Extensions of the GKF to non-constant-variance fields and to Gaussian fields on infinite-dimensional or shape spaces; applications to post-selection inference. *(frontier — verify)*
- **Nodal geometry (Sarnak, Wigman, Canzani, Beliaev).** Sharpening the Nazarov–Sodin framework to obtain fluctuation results for numbers of components and for topology types of nodal sets of monochromatic waves; numerical estimation of $c_{NS}$.
- **Real algebraic geometry (Gayet, Welschinger, Letendre, Lerario, Stecconi).** A "random Morse theory over $\mathbb{R}$" programme aiming at exponentially rare-event bounds for the probability that $Z_d$ contains a prescribed diffeotype, and at expected Betti numbers of intersections in general Kähler ambients.
- **Random matrices and landscape complexity (Fyodorov, Auffinger, Ben Arous, Subag).** Kac–Rice with large-deviation asymptotics of $\mathbb{E}|\det(\text{GOE}-u)|$ to count critical points of spin-glass Hamiltonians on the sphere; $\mathbb{E}[\chi]$ appears as the signed (and hence far smaller) analogue of the complexity.
- **Topological data analysis (Bobrowski, Kahle, Weinberger).** Expected Euler characteristic and Betti numbers of random Čech/Vietoris–Rips complexes and of sublevel sets of distance functions; persistent-homology versions of the Euler curve $u \mapsto \mathbb{E}[\chi(A_u)]$ as a statistical descriptor ("Euler characteristic transform").
- **Non-Gaussian Euler characteristics.** Preprints extend GKF-type expansions to elliptic/Laplace-mixtures and to fields with heavy-tailed marginals via subordination. *(frontier — verify)*

## 8. Future Work

- Prove or disprove: no non-Gaussian-related isotropic field on $S^N$ admits an exact finite Lipschitz–Killing expansion of $\mathbb{E}[\chi(A_u)]$.
- Establish a central limit theorem for $\chi(A_u(f,M_T))$ as $M_T$ grows, with explicit variance; partial results exist for Wiener-chaos expansions of nodal volumes, but the $\chi$ case needs Hessian-determinant chaos control.
- Compute $\mathbb{E}[b_i(Z)]$ to leading order (not just order of magnitude) for Kostlan and band-limited models, e.g. via a local limit for the nodal set together with a percolation-type decomposition.
- Determine $c_{NS}$ for $S^2$ to provable accuracy, or express it in terms of a percolation critical parameter, as suggested by the Bogomolny–Schmit heuristic.
- Extend the heuristic's exponential accuracy to fields with non-constant variance and to manifolds of low regularity.
- Develop a stable, finite-sample estimator of the Euler characteristic curve from sampled data and quantify its bias — the practical bottleneck in cosmological and neuroimaging use.

## 9. Key References

- **[Foundational]** R. J. Adler. *The Geometry of Random Fields.* Wiley, 1981 (SIAM Classics reprint, 2010).
- **[Foundational]** J. E. Taylor, R. J. Adler. *Euler characteristics for Gaussian fields on manifolds.* Annals of Probability 31(2):533–563, 2003.
- **[Foundational]** J. E. Taylor. *A Gaussian kinematic formula.* Annals of Probability 34(1):122–158, 2006.
- **[Foundational]** R. J. Adler, J. E. Taylor. *Random Fields and Geometry.* Springer Monographs in Mathematics, 2007.
- **[SOTA / Recent]** J. E. Taylor, A. Takemura, R. J. Adler. *Validity of the expected Euler characteristic heuristic.* Annals of Probability 33(4):1362–1396, 2005.
- **[SOTA / Recent]** K. J. Worsley. *Local maxima and the expected Euler characteristic of excursion sets of $\chi^2$, $F$ and $t$ fields.* Advances in Applied Probability 26(1):13–42, 1994.
- **[SOTA / Recent]** P. Bürgisser. *Average Euler characteristic of random real algebraic varieties.* Comptes Rendus Mathématique 345(9):507–512, 2007.
- **[SOTA / Recent]** D. Gayet, J.-Y. Welschinger. *Lower estimates for the expected Betti numbers of random real hypersurfaces.* Journal of the London Mathematical Society 90(1):105–120, 2014.
- **[SOTA / Recent]** D. Gayet, J.-Y. Welschinger. *Betti numbers of random real hypersurfaces and determinants of random symmetric matrices.* Journal of the European Mathematical Society 18(4):733–772, 2016.
- **[SOTA / Recent]** T. Letendre. *Expected volume and Euler characteristic of random submanifolds.* Journal of Functional Analysis 270(8):3047–3110, 2016.
- **[SOTA / Recent]** F. Nazarov, M. Sodin. *On the number of nodal domains of random spherical harmonics.* American Journal of Mathematics 131(5):1337–1357, 2009.
- **[SOTA / Recent]** P. Sarnak, I. Wigman. *Topologies of nodal sets of random band-limited functions.* Communications on Pure and Applied Mathematics 72(2):275–342, 2019.
- **[SOTA / Recent]** L. I. Nicolaescu. *Critical sets of random smooth functions on compact manifolds.* Asian Journal of Mathematics 19(3):391–432, 2015.
- **[Survey]** R. J. Adler, J. E. Taylor, K. J. Worsley. *Applications of Random Fields and Geometry: Foundations and Case Studies.* Springer (in preparation / preprint editions circulated since 2009).
- **[Survey]** O. Bobrowski, M. Kahle. *Topology of random geometric complexes: a survey.* Journal of Applied and Computational Topology 1:331–364, 2018.

## 10. Worked Example / Concrete Special Case

**Random spherical harmonics on $S^2$.** Let $f_\ell$ be the centered Gaussian field on the unit sphere $S^2$ with covariance $\mathbb{E}[f_\ell(x)f_\ell(y)] = P_\ell(\langle x,y\rangle)$, the Legendre polynomial of degree $\ell$ (equivalently, a uniform random unit vector in the $(2\ell+1)$-dimensional eigenspace of $\Delta_{S^2}$ with eigenvalue $-\ell(\ell+1)$). This field has unit variance and is isotropic.

**Step 1 — second spectral moment.** Differentiating the covariance twice at $x=y$ gives, for any unit tangent vector $X$,
$$\lambda := \mathbb{E}\big[(Xf_\ell)^2\big] = \frac{\ell(\ell+1)}{2}.$$
So the induced metric is $g = \lambda\, g_{\mathrm{round}}$.

**Step 2 — Lipschitz–Killing curvatures of $(S^2, g)$.**
$$\mathcal{L}_0 = \chi(S^2) = 2, \qquad \mathcal{L}_1 = 0 \ \ (\text{closed 2-manifold}), \qquad \mathcal{L}_2 = \mathrm{Vol}_g(S^2) = \lambda \cdot 4\pi = 2\pi\,\ell(\ell+1).$$

**Step 3 — apply the GKF.** With $\rho_0=\Psi$, $\rho_2(u) = (2\pi)^{-3/2}u\,e^{-u^2/2}$:
$$\mathbb{E}\big[\chi(A_u)\big] = 2\Psi(u) + 2\pi\ell(\ell+1)\cdot(2\pi)^{-3/2}u\,e^{-u^2/2} = 2\Psi(u) + \frac{\ell(\ell+1)}{\sqrt{2\pi}}\,u\,e^{-u^2/2}.$$

**Step 4 — numerical instance.** Take $\ell = 10$ (so $\ell(\ell+1)=110$) and $u=2$:
$$\mathbb{E}[\chi(A_2)] = 2(0.02275) + \frac{110}{2.5066}\cdot 2\cdot e^{-2} = 0.0455 + 43.88\cdot 2 \cdot 0.13534 \approx 11.9.$$
The excursion set above level $2$ consists, on average, of about $12$ small blobs (each contractible, so $\chi\approx b_0$). Since the heuristic error is $O(e^{-\alpha u^2/2})$ with $\alpha>1$, $\mathbb{P}\{\sup f_{10}\ge u\}$ for large $u$ is well approximated by the same expression; at $u=4$ it gives $\approx 0.0132$, an accurate tail estimate.

**Step 5 — where the formula stops being informative.** At $u=0$,
$$\mathbb{E}[\chi(A_0)] = 2\cdot\tfrac12 + 0 = 1 \quad\text{for every } \ell .$$
Yet $\chi(A_0) = b_0(A_0) - b_1(A_0)$, and by Nazarov–Sodin the number of nodal domains is $\asymp c_{NS}\,\ell^2$, so both $b_0$ and $b_1$ grow like $\ell^2$ while their difference stays exactly $1$. This single line is the whole difficulty: the exactly computable quantity is blind to the topology it is meant to describe, and recovering $\mathbb{E}[b_0]$ requires tools — percolation heuristics, local limits, quantitative transversality — entirely outside the Kac–Rice framework that produced the formula.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*