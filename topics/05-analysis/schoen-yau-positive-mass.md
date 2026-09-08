---
id: 05-analysis/schoen-yau-positive-mass
title: "Schoen-Yau Positive Mass"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Schoen–Yau Positive Mass Theorem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/schoen-yau-positive-mass` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Riemannian positive mass theorem (PMT).** Let $(M^n, g)$ be a complete, asymptotically flat Riemannian manifold with nonnegative scalar curvature $R_g \ge 0$. Then the ADM mass of each end is nonnegative,
$$m_{\mathrm{ADM}}(M,g) \ge 0,$$
with equality if and only if $(M,g)$ is isometric to Euclidean space $(\mathbb{R}^n, \delta)$.

**Spacetime PMT.** Let $(M^n, g, k)$ be an asymptotically flat initial data set for the Einstein equations satisfying the dominant energy condition
$$\mu \ge |J|_g, \qquad \mu = \tfrac12\big(R_g + (\mathrm{tr}_g k)^2 - |k|_g^2\big), \quad J = \mathrm{div}_g\big(k - (\mathrm{tr}_g k)\,g\big).$$
Then the ADM energy–momentum vector $(E,P)$ is future-causal: $E \ge |P|$. Equality $E = 0$ forces the data to arise from a spacelike slice of Minkowski space.

A complete resolution requires: (i) all dimensions $n \ge 3$, (ii) no spin assumption, (iii) the rigidity/equality statement, (iv) the full spacetime version with $k \not\equiv 0$. Items (i)–(iii) are settled in the Riemannian case; parts of (iv) remain open in high dimensions without spin.

## 2. Mathematical Foundations

**Asymptotic flatness.** $(M^n,g)$ is asymptotically flat of order $q > \frac{n-2}{2}$ if outside a compact set $M$ is a finite union of ends, each diffeomorphic to $\mathbb{R}^n \setminus \overline{B_1}$, with
$$g_{ij} = \delta_{ij} + O(|x|^{-q}), \quad \partial g_{ij} = O(|x|^{-q-1}), \quad \partial^2 g_{ij} = O(|x|^{-q-2}), \qquad R_g \in L^1(M).$$

**ADM mass** (Arnowitt–Deser–Misner, 1961):
$$m_{\mathrm{ADM}} = \frac{1}{2(n-1)\omega_{n-1}} \lim_{r\to\infty} \int_{S_r} \big(\partial_i g_{ij} - \partial_j g_{ii}\big)\,\nu^j \, dA,$$
where $\omega_{n-1} = |S^{n-1}|$ and $\nu$ is the outward unit normal. Bartnik (1986) and Chruściel (1986) proved this limit exists and is a geometric invariant precisely under the above decay plus $R_g \in L^1$.

**ADM momentum.**
$$P_i = \frac{1}{(n-1)\omega_{n-1}} \lim_{r\to\infty} \int_{S_r} \big(k_{ij} - (\mathrm{tr}_g k)\,g_{ij}\big)\nu^j\, dA .$$

**Schoen–Yau minimal-hypersurface mechanism.** If $m_{\mathrm{ADM}} < 0$, one solves a Plateau problem in a large slab to produce a complete, area-minimizing, asymptotically planar hypersurface $\Sigma^{n-1} \subset M$. Stability gives, for all $\varphi \in C_c^\infty(\Sigma)$,
$$\int_\Sigma |\nabla \varphi|^2 \ge \int_\Sigma \big(|A|^2 + \mathrm{Ric}_g(\nu,\nu)\big)\varphi^2 ,$$
and the Gauss equation $2\,\mathrm{Ric}_g(\nu,\nu) = R_g - R_\Sigma + |A|^2 - H^2$ converts this into
$$\int_\Sigma |\nabla\varphi|^2 + \tfrac12 R_\Sigma \varphi^2 \ \ge\ \tfrac12\int_\Sigma \big(R_g + |A|^2\big)\varphi^2 \ \ge\ 0,$$
so $\Sigma$ carries a metric of nonnegative scalar curvature in a conformal/averaged sense. Induction on dimension plus the Gauss–Bonnet obstruction at $n=3$ ($\Sigma^2$ would be a stable minimal plane of positive genus-zero type in a negative-mass end) yields the contradiction.

**Witten's spinor identity.** On a spin manifold, for a harmonic spinor $\psi$ ($D\psi = 0$) asymptotic to a constant spinor $\psi_0$, the Lichnerowicz–Schrödinger formula $D^2 = \nabla^*\nabla + \tfrac14 R$ integrates to
$$4(n-1)\omega_{n-1}\, m_{\mathrm{ADM}} \,|\psi_0|^2 = \int_M \Big(|\nabla \psi|^2 + \tfrac14 R_g |\psi|^2\Big),$$
giving $m \ge 0$ immediately, and $\nabla\psi \equiv 0$ (parallel spinors, hence flatness) in the equality case.

## 3. History & State of the Art (SOTA)

- **1959–1962.** ADM define the Hamiltonian mass of asymptotically flat data; the physics conjecture "gravitational mass of an isolated system is nonnegative" is folklore by the 1960s.
- **1973–1978.** Geroch proposes the inverse-mean-curvature-flow route for $n=3$; Jang, Brill–Deser, Choquet-Bruhat obtain perturbative and special-symmetry cases.
- **1979.** Schoen and Yau, *On the proof of the positive mass conjecture in general relativity* (Comm. Math. Phys. 65), prove the Riemannian PMT for $n = 3$ by minimal-surface descent.
- **1981.** Schoen–Yau, *Proof of the positive mass theorem II* (Comm. Math. Phys. 79), handle the spacetime case in dimension 3 via Jang's equation. Witten gives the spinor proof (published 1981, with analytic details by Parker–Taubes 1982).
- **1979–2017.** The minimal-hypersurface argument extends to $3 \le n \le 7$; beyond $n = 7$, minimizers can have singular sets of codimension $7$, blocking the induction.
- **2017–2019.** Schoen–Yau, *Positive scalar curvature and minimal hypersurface singularities* (Surveys in Differential Geometry 24, 441–480), remove the dimension restriction for the Riemannian PMT by a regularization/slicing scheme controlling the singular set. Lohkamp announced an independent program ("skin structures") over the same period.
- **2016.** Eichmair, Lam, Lee, Schoen, *Positive mass theorem for asymptotically flat manifolds with arbitrary ends* / the earlier *The spacetime positive mass theorem in dimensions less than eight* (J. Eur. Math. Soc. 18, 2016) settles $E \ge |P|$ for $3 \le n \le 7$ using marginally outer trapped surfaces and Jang's equation.
- **2020.** Huang–Lee, *Equality in the spacetime positive mass theorem* (Comm. Math. Phys. 376), prove the rigidity statement for $E = |P|$ in dimensions $< 8$.

## 4. Partial Results / Verified Cases

| Setting | Range settled | Source |
|---|---|---|
| Riemannian PMT, $R_g \ge 0$ | $3 \le n \le 7$, all topologies | Schoen–Yau 1979 + dimensional induction |
| Riemannian PMT | all $n \ge 3$, spin | Witten 1981; Parker–Taubes 1982; Bartnik 1986 |
| Riemannian PMT | all $n \ge 3$, no spin assumption | Schoen–Yau 2017/2019 |
| Spacetime PMT $E \ge \lvert P\rvert$ | $3 \le n \le 7$ | Eichmair–Lam–Lee–Schoen 2016 |
| Spacetime PMT | all $n$, spin | Witten-type argument (Parker–Taubes; Bartnik) |
| Rigidity $E=\lvert P\rvert$ | $n < 8$ | Huang–Lee 2020 |
| Low regularity: corners along a hypersurface | $n=3$, Lipschitz metrics with matched induced metric and $H^+ \ge H^-$ | Miao 2002; Shi–Tam 2002 |
| Penrose refinement $m \ge \sqrt{A/16\pi}$ | $n = 3$, single/multiple horizons | Huisken–Ilmanen 2001; Bray 2001; Bray–Lee 2009 ($n \le 7$, spin for rigidity) |
| Hyperbolic/asymptotically AdS analogue | $n=3$, spin, and $n \le 7$ under conditions | Chruściel–Herzlich 2003; X. Wang 2001 |
| Stability: $m \to 0 \Rightarrow$ convergence | rotationally symmetric, graphical, $n=3$ classes | Lee–Sormani 2014 (intrinsic flat) |

## 5. Principal Obstacles

- **Singularities of area minimizers in $n \ge 8$.** Federer's dimension reduction bounds the singular set of a mass-minimizing hypersurface by $\mathcal{H}^{n-8}$; the Simons cone $C(S^3\times S^3)\subset \mathbb{R}^8$ is a genuinely singular minimizer. The Schoen–Yau induction needs $\Sigma$ smooth to apply the stability inequality and to iterate. The 2017 fix uses minimizers of a weighted/regularized functional and shows the singular set has codimension $\ge 3$ in the slice, enough for capacity arguments to kill it — but the machinery is delicate and independent verification has been slow.
- **Spin is a topological hypothesis.** Witten's proof is clean but requires a spin structure and a solvable Dirac equation; asymptotically flat manifolds with arbitrary ends and nontrivial $w_2$ fall outside it.
- **Jang's equation blows up.** In the spacetime case one solves $\big(g^{ij} - \frac{f^i f^j}{1+|Df|^2}\big)\big(\frac{\nabla_{ij} f}{\sqrt{1+|Df|^2}} - k_{ij}\big)=0$; solutions blow up exactly at marginally outer trapped surfaces (MOTS), and controlling the blow-up geometry is a nonlinear-elliptic problem whose regularity again degrades past $n=7$.
- **No conformal or Fourier reduction.** The ADM mass is a boundary flux, not a curvature integral; there is no local pointwise inequality to integrate, and linearizing about flat space only yields the theorem perturbatively (the second variation of mass is a positive quadratic form, but the problem is global).
- **Low regularity.** Below $C^{1,\alpha}$, the ADM integrand is not defined pointwise; distributional scalar curvature (Lee–LeFloch, Burkhardt-Guim) provides candidate formulations but the rigidity case is hard.

## 6. The Gap

The Riemannian statement of Section 1 is now proved in full generality; the residual gaps are:

1. **Verification.** The Schoen–Yau 2017 singular-slicing argument and Lohkamp's parallel program have not been fully absorbed by the community at the level of a textbook proof. *(frontier — verify)*
2. **Spacetime PMT for $n \ge 8$, non-spin.** $E \ge |P|$ is not known in general; Jang's equation inherits the singularity problem, and the reduction of the general case to the Riemannian one is not available.
3. **Rigidity in the spacetime case for $n \ge 8$.** Huang–Lee's argument uses the smooth $n<8$ theory as input.
4. **Very low regularity.** PMT for metrics that are merely $W^{1,n}_{\mathrm{loc}}$ or continuous with distributional $R \ge 0$, and the corresponding quantitative stability (a Bartnik-style "small mass $\Rightarrow$ close to $\mathbb{R}^n$" statement in a metric of convergence stronger than intrinsic-flat), is open.

## 7. Current Research (as of June 2026)

- **Stanford / Tsinghua (Schoen, Yau and collaborators):** completing and streamlining the higher-dimensional minimal-hypersurface machinery; applications to the higher-dimensional Penrose inequality.
- **Chicago / Columbia (Lohkamp; Gromov circle):** Lohkamp's "skin structure" desingularization and Gromov's $\mu$-bubble / torical-band techniques, which recover positive-scalar-curvature obstructions without regular minimizers. Gromov's *Four lectures on scalar curvature* (2019–2023) is the reference point.
- **Stony Brook / Fudan (Huang, Lee, Sormani):** stability of the PMT — quantifying "small ADM mass implies Euclidean-close" in intrinsic flat distance; the Huang–Lee–Sormani program on Bartnik mass and localized mass. *(frontier — verify)*
- **Spinorial revival (Bär, Bray, Cecchini, Zeidler):** Callias-operator and index-theoretic proofs give new bounds relating scalar curvature to distance ($\mathrm{Sc} \ge n(n-1) \Rightarrow$ width bounds), and spinorial PMT variants for manifolds with boundary.
- **Numerical relativity groups** verify $E \ge |P|$ on constructed initial data (binary black-hole punctures, Bowen–York data) as a consistency check on constraint solvers.

## 8. Future Work

- Produce a self-contained, refereed treatment of the $n \ge 8$ Riemannian case that isolates the singular-set estimates as standalone geometric-measure-theory theorems.
- Extend Jang's equation regularity theory to dimensions $\ge 8$, closing the spacetime PMT.
- Prove the Riemannian Penrose inequality $m \ge \frac12\big(A/\omega_{n-1}\big)^{\frac{n-2}{n-1}}$ for all $n$ and for multiple horizons without spin.
- Establish PMT for distributional scalar curvature (Burkhardt-Guim's $C^0$ scalar curvature via Ricci flow smoothing) including rigidity.
- Settle the Bartnik mass minimization conjecture: quasi-local minimizers should be static vacuum extensions.

## 9. Key References

- **[Foundational]** R. Schoen and S.-T. Yau. *On the proof of the positive mass conjecture in general relativity.* Communications in Mathematical Physics **65** (1979), 45–76. [DOI](https://doi.org/10.1007/bf01940959)
- **[Foundational]** R. Schoen and S.-T. Yau. *Proof of the positive mass theorem II.* Communications in Mathematical Physics **79** (1981), 231–260. [DOI](https://doi.org/10.1007/bf01942062)
- **[Foundational]** E. Witten. *A new proof of the positive energy theorem.* Communications in Mathematical Physics **80** (1981), 381–402. [DOI](https://doi.org/10.1007/bf01208277)
- **[Foundational]** T. Parker and C. H. Taubes. *On Witten's proof of the positive energy theorem.* Communications in Mathematical Physics **84** (1982), 223–238. [DOI](https://doi.org/10.1007/bf01208569)
- **[Foundational]** R. Arnowitt, S. Deser, C. W. Misner. *Coordinate invariance and energy expressions in general relativity.* Physical Review **122** (1961), 997–1006. [DOI](https://doi.org/10.1103/physrev.122.997)
- **[Foundational]** R. Bartnik. *The mass of an asymptotically flat manifold.* Communications on Pure and Applied Mathematics **39** (1986), 661–693. [DOI](https://doi.org/10.1002/cpa.3160390505)
- **[SOTA / Recent]** R. Schoen and S.-T. Yau. *Positive scalar curvature and minimal hypersurface singularities.* Surveys in Differential Geometry **24** (2019), 441–480. [DOI](https://doi.org/10.4310/sdg.2019.v24.n1.a10)
- **[SOTA / Recent]** M. Eichmair, L.-H. Huang, D. A. Lee, R. Schoen. *The spacetime positive mass theorem in dimensions less than eight.* Journal of the European Mathematical Society **18** (2016), 83–121. [DOI](https://doi.org/10.4171/jems/584)
- **[SOTA / Recent]** L.-H. Huang and D. A. Lee. *Equality in the spacetime positive mass theorem.* Communications in Mathematical Physics **376** (2020), 2379–2407. [DOI](https://doi.org/10.1007/s00220-019-03619-w)
- **[SOTA / Recent]** G. Huisken and T. Ilmanen. *The inverse mean curvature flow and the Riemannian Penrose inequality.* Journal of Differential Geometry **59** (2001), 353–437. [DOI](https://doi.org/10.4310/jdg/1090349447)
- **[SOTA / Recent]** H. L. Bray. *Proof of the Riemannian Penrose inequality using the positive mass theorem.* Journal of Differential Geometry **59** (2001), 177–267. [DOI](https://doi.org/10.4310/jdg/1090349428)
- **[Survey]** D. A. Lee. *Geometric Relativity.* Graduate Studies in Mathematics **201**, American Mathematical Society, 2019.
- **[Survey]** M. Gromov. *Four lectures on scalar curvature.* In *Perspectives in Scalar Curvature*, World Scientific, 2023. [DOI](https://doi.org/10.1142/9789811273223_0001)
- **[Survey]** P. T. Chruściel, G. J. Galloway, D. Pollack. *Mathematical general relativity: a sampler.* Bulletin of the AMS **47** (2010), 567–638. [DOI](https://doi.org/10.1090/s0273-0979-2010-01304-5)

## 10. Worked Example / Concrete Special Case

**The Schwarzschild time-symmetric slice.** On $M = \mathbb{R}^3 \setminus \{0\}$ take
$$g = u^4 \, \delta, \qquad u(x) = 1 + \frac{m}{2r}, \quad r = |x|.$$
Since $\Delta_\delta u = 0$ away from the origin, the conformal scalar-curvature formula $R_g = -8u^{-5}\Delta_\delta u$ gives $R_g \equiv 0$, so the hypothesis $R_g \ge 0$ holds.

**Compute the ADM mass.** With $g_{ij} = u^4 \delta_{ij}$,
$$\partial_i g_{ij} = \partial_j(u^4) = 4u^3 \partial_j u, \qquad \partial_j g_{ii} = 3\,\partial_j(u^4) = 12 u^3 \partial_j u,$$
so the ADM integrand is $(\partial_i g_{ij} - \partial_j g_{ii})\nu^j = -8u^3 \partial_j u \, \nu^j$. Now $\partial_j u = -\dfrac{m x_j}{2 r^3}$ and $\nu^j = x_j/r$, hence $\partial_j u\,\nu^j = -\dfrac{m}{2r^2}$ and the integrand equals $4 m u^3 / r^2$. Over $S_r$ (Euclidean area $4\pi r^2$):
$$\int_{S_r} = 16\pi m\Big(1+\frac{m}{2r}\Big)^{3} \xrightarrow[r\to\infty]{} 16\pi m, \qquad m_{\mathrm{ADM}} = \frac{1}{16\pi}\cdot 16\pi m = m .$$

**Why the hypotheses bite.** For $m > 0$ the metric is complete: $r = m/2$ is a totally geodesic minimal $2$-sphere (the horizon, area $16\pi m^2$) and the manifold has two asymptotically flat ends, each of mass $m > 0$ — consistent with PMT, and saturating the Riemannian Penrose inequality $m \ge \sqrt{A/16\pi}$.

For $m < 0$ the conformal factor $u$ vanishes at $r = |m|/2$, where $g$ degenerates. The manifold $\{r > |m|/2\}$ is **incomplete** with a naked singularity, so it is not a counterexample: completeness is exactly the hypothesis that excludes negative-mass scalar-flat metrics.

For $m = 0$, $u \equiv 1$ and $g = \delta$ — the rigidity statement realized: mass zero forces flat Euclidean space. The general rigidity proof reverses this: from $m_{\mathrm{ADM}} = 0$ one perturbs to $R_g > 0$ with $m < 0$, contradicting the theorem, then shows $\mathrm{Ric}_g \equiv 0$ and, with asymptotic flatness, $(M,g)\cong(\mathbb{R}^n,\delta)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*