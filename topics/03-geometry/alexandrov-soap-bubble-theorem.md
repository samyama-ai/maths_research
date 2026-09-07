---
id: 03-geometry/alexandrov-soap-bubble-theorem
title: "Alexandrov's Soap Bubble Theorem"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alexandrov's Soap Bubble Theorem

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/alexandrov-soap-bubble-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Classical statement (Alexandrov, 1958).** Let $\Sigma \subset \mathbb{R}^n$, $n \ge 3$, be a compact, connected, embedded hypersurface of class $C^2$ with constant mean curvature. Then $\Sigma$ is a round sphere, and the region it bounds is a ball.

The classical statement is a theorem, not an open problem. What remains open is the family of questions that surround it, and this page catalogs that program:

1. **Sharp stability.** If the mean curvature is only *almost* constant, is $\Sigma$ quantitatively close to a sphere, with the optimal exponent and an explicit constant? Concretely: does
$$\rho_e - \rho_i \;\le\; C\,\|H - H_0\|_{L^p(\Sigma)}^{\tau}$$
hold with $\tau = 1$ (known optimal) for all $n$ and all $p$ down to the natural threshold, where $\rho_e, \rho_i$ are the radii of the smallest circumscribed and largest inscribed concentric balls?
2. **Ambient generality.** For which Riemannian manifolds $(M,g)$ does the conclusion survive? Brendle settled warped products of a specific type; the general characterization is open.
3. **Weak, anisotropic and nonlocal versions.** Which regularity, ellipticity or kernel hypotheses can be dropped before spheres/Wulff shapes cease to be the only critical points?
4. **Capillary and free-boundary analogues** in balls, cones, wedges and slabs.

A complete resolution of (1) means: an inequality with the optimal exponent, a constant depending only on $n$ and explicitly computable a priori data, together with a matching example showing no better exponent is possible.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^n$ be a bounded domain with $\Sigma = \partial\Omega$ of class $C^2$, outward unit normal $\nu$, principal curvatures $\kappa_1,\dots,\kappa_{n-1}$, and mean curvature
$$H \;=\; \kappa_1 + \cdots + \kappa_{n-1} \;=\; \operatorname{div}_\Sigma \nu .$$
(The unit sphere $S^{n-1}$ has $H = n-1$ under this normalization.) The $k$-th mean curvature is $H_k = \binom{n-1}{k}^{-1} \sigma_k(\kappa)$, with $\sigma_k$ the elementary symmetric polynomial.

**Variational characterization.** $\Sigma$ has constant $H$ iff it is a critical point of the area functional $P(\Omega)$ under volume constraint: for a normal variation with speed $\varphi$,
$$\delta P = \int_\Sigma H\varphi\,dA, \qquad \delta |\Omega| = \int_\Sigma \varphi\,dA .$$

**Heintze–Karcher inequality.** If $H > 0$ on $\Sigma = \partial\Omega$, then
$$\int_{\Sigma} \frac{n-1}{H}\,dA \;\ge\; n\,|\Omega|,$$
with equality **iff** $\Omega$ is a ball (Heintze–Karcher 1978; Ros 1987). Alexandrov's theorem follows immediately: constant $H$ plus the divergence identity $\int_\Sigma H\,dA \cdot \tfrac{1}{H} = |\Sigma|/H$ and Minkowski's formula $\int_\Sigma H\,dA = (n-1)|\Sigma| \cdot$ … more directly, $H \equiv H_0$ gives $\frac{(n-1)|\Sigma|}{H_0} \ge n|\Omega|$, while the divergence theorem $\int_\Sigma \langle x,\nu\rangle dA = n|\Omega|$ combined with the Minkowski formula $\int_\Sigma \big(1 - \tfrac{H}{n-1}\langle x,\nu\rangle\big)dA = 0$ forces equality.

**Reilly's identity.** For $u$ solving $\Delta u = 1$ in $\Omega$, $u = 0$ on $\Sigma$:
$$\int_\Omega \big( (\Delta u)^2 - |\nabla^2 u|^2 \big)\,dx \;=\; \int_\Sigma H\, u_\nu^2 \, dA .$$
Since $(\Delta u)^2 \le n|\nabla^2 u|^2$ with equality iff $\nabla^2 u = \frac{1}{n}I$, this yields both Heintze–Karcher and, via the *P-function* $P = |\nabla u|^2 - \tfrac{2}{n}u$, the quantitative estimates of Magnanini–Poggesi.

**Moving planes.** Alexandrov's original argument: for each direction $e$ and each $t$, reflect $\Sigma \cap \{x\cdot e > t\}$ across $\{x\cdot e = t\}$; at the critical $t$ the reflected cap touches $\Sigma$ internally or orthogonally, and the interior/boundary-point Hopf lemma applied to the quasilinear elliptic mean-curvature operator forces $\Sigma$ to be symmetric about the plane. Symmetry in all directions gives a sphere. **Embeddedness is used exactly here** — it is what makes the reflected cap lie inside $\Omega$.

## 3. History & State of the Art (SOTA)

- **1853 / 1899.** Jellett and Liebmann: star-shaped, resp. convex, CMC surfaces in $\mathbb{R}^3$ are spheres.
- **1951.** Hopf: an *immersed* CMC sphere ($g=0$) in $\mathbb{R}^3$ is round, via the holomorphic Hopf differential.
- **1956–58.** Alexandrov proves the general embedded case by the reflection method, inventing what Serrin (1971) and Gidas–Ni–Nirenberg (1979) later turned into the standard moving-planes toolkit.
- **1977–78.** Reilly's integral identity; Heintze–Karcher's comparison inequality.
- **1982.** Hsiang constructs immersed non-spherical CMC hyperspheres in $\mathbb{R}^4$: Hopf's theorem does *not* generalize.
- **1986.** Wente's immersed CMC torus in $\mathbb{R}^3$ refutes Hopf's conjecture; embeddedness in Alexandrov's theorem is essential, not technical.
- **1987–91.** Ros, then Montiel–Ros: Alexandrov's theorem for $H_k$ constant, any $k$, and in space forms $\mathbb{H}^n$ and the open hemisphere.
- **2013.** Brendle proves the Heintze–Karcher inequality — hence Alexandrov rigidity — in warped products $\mathbb{R}\times_f N$ satisfying explicit curvature conditions, covering Schwarzschild and de Sitter–Schwarzschild.
- **2017–20.** The stability era: Ciraolo–Maggi, Ciraolo–Vezzoni, Delgadino–Maggi, Magnanini–Poggesi, De Rosa–Kolasiński–Santilli.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $\mathbb{R}^n$, $n\ge 3$, $C^2$ embedded, $H$ const | Sphere | Alexandrov 1958 |
| $\mathbb{R}^n$, $H_k$ const for some $k\in\{1,\dots,n-1\}$, embedded | Sphere | Ros 1987; Montiel–Ros 1991 |
| $\mathbb{H}^n$, open hemisphere $S^n_+$ | Sphere (geodesic) | Montiel–Ros 1991 |
| Warped products $\mathbb{R}\times_f N$ with $f'>0$, Ric conditions | Slice or geodesic sphere | Brendle 2013 |
| Sets of finite perimeter, distributional const. mean curvature, $\Omega$ bounded | Finite union of equal balls with disjoint interiors | Delgadino–Maggi 2019 |
| Anisotropic energy $\int F(\nu)$, $F$ uniformly convex, finite perimeter | Wulff shape (unions thereof) | De Rosa–Kolasiński–Santilli 2020 |
| Nonlocal mean curvature $H_s$, $s\in(0,1)$, bounded set | Ball | Cabré–Fall–Solà-Morales–Weth 2018; Ciraolo–Figalli–Maggi–Novaga 2018 |
| Stability, $\|H-H_0\|_{L^\infty}\le \varepsilon$, a priori $C^{2,\alpha}$ bounds | $\rho_e-\rho_i \le C\varepsilon$, **optimal exponent 1** | Ciraolo–Vezzoni 2018 |
| Stability, $L^1$/$L^2$ deficit, no uniform-obstacle bound | $\tau = 1$ for $n=2,3$; $\tau=1-\epsilon$ for $n=4$; $\tau = 2/(n-2)$ for $n\ge 5$; later improved to $\tau$ arbitrarily close to $1$ | Magnanini–Poggesi 2019, 2020 |
| Almost-CMC, no embeddedness, $H$ bounded in $L^\infty$ | $\Sigma$ is $C^1$-close to a finite union of tangent equal spheres | Ciraolo–Maggi 2017 |
| Capillary hypersurfaces in a ball, stable | Spherical cap or totally geodesic disc | Wang–Xia 2019 |

## 5. Principal Obstacles

- **Moving planes is not quantitative by nature.** The Hopf boundary lemma is a strict-inequality statement with no modulus. Turning it into an estimate (Ciraolo–Vezzoni) requires quantitative Harnack inequalities on thin reflected caps, whose constants degenerate as the touching point approaches a tangency; this is what forces a priori $C^{2,\alpha}$ bounds and non-explicit constants.
- **Integral-identity methods lose sharpness in high dimension.** The Magnanini–Poggesi route bounds $\|\nabla^2 u - \tfrac{1}{n}I\|_{L^2(\Omega)}$ and must convert this into a pointwise oscillation bound on $|\nabla u|$. The conversion uses a Sobolev/Hardy-type inequality whose exponent degrades once $n \ge 5$ — the $2/(n-2)$ loss is an artifact of the trace/interpolation step, not of the geometry.
- **The Heintze–Karcher inequality needs mean-convexity.** $H>0$ is required to define the normal-exponential comparison; for merely almost-CMC surfaces $H$ can vanish, and the cut-locus argument collapses.
- **Bubbling is a genuine phenomenon, not a defect of proof.** Delgadino–Maggi's unions of tangent balls are true minimizers of the weak problem, so any stability theorem must either exclude them by a connectedness/diameter hypothesis or accept a multi-bubble conclusion. This is why no unconditional single-sphere stability statement can exist.
- **In general ambient manifolds the statement is false.** There are Riemannian metrics on $S^n$ admitting non-umbilic embedded CMC hypersurfaces. No one knows the sharp curvature hypothesis separating rigid from non-rigid ambients; Brendle's conditions are sufficient, not necessary.
- **Anisotropic non-smooth case.** When the surface tension $F$ is only convex (crystalline Wulff shapes, faceted), the associated operator is degenerate elliptic; the strong maximum principle used by moving planes has no analogue on flat facets.

## 6. The Gap

Three precise gaps:

1. **Optimal-constant stability.** Known: exponent $\tau = 1$ under $C^{2,\alpha}$ bounds (Ciraolo–Vezzoni), and $\tau \to 1^-$ with mild bounds (Magnanini–Poggesi 2020). Missing: an inequality $\rho_e - \rho_i \le C(n)\,\|H-H_0\|_{L^{n-1}}$ with $C$ depending only on $n$ and $|\Omega|$, valid for all $n$, with $C$ explicit. The barrier is the interpolation step converting an $L^2$ Hessian deficit into an $L^\infty$ boundary estimate.
2. **Characterizing rigid ambients.** Missing: a necessary-and-sufficient curvature condition on $(M,g)$ under which every embedded CMC hypersurface is umbilic. Brendle's $f' > 0$ warped-product hypothesis is far from necessary.
3. **Crystalline anisotropy.** Missing: rigidity for $F$ merely convex with facets, where the Wulff shape is a polytope.

## 7. Current Research (as of June 2026)

- **Florence / Perth (Magnanini, Poggesi).** Integral-identity stability; recent work extends the P-function method to Serrin-type overdetermined problems in space forms and to $p$-Laplacian analogues. *(frontier — verify)* Reports of $\tau=1$ in all dimensions under only a uniform interior-sphere condition.
- **Milan / Turin (Ciraolo, Vezzoni, Roncoroni).** Quantitative moving planes; extensions to CMC hypersurfaces in cones and to Riemannian manifolds with nonnegative Ricci curvature and Euclidean volume growth.
- **Austin (Maggi and collaborators).** Geometric-measure-theoretic Alexandrov theorems, quantitative bubbling, and capillarity; the "almost-CMC $\Rightarrow$ union of spheres" program.
- **Xiamen / Freiburg (Xia, Wang, Jia, Zhang).** Heintze–Karcher inequalities for capillary hypersurfaces in half-spaces, wedges and cones, yielding Alexandrov-type theorems with contact-angle conditions. *(frontier — verify)*
- **Barcelona / Frankfurt (Cabré, Weth, Fall).** Nonlocal CMC: constant fractional mean curvature, Delaunay-type nonlocal cylinders, and the failure of Alexandrov for unbounded nonlocal sets.
- **Stanford / Columbia (Brendle and students).** Rigidity in substatic and warped-product manifolds, motivated by the Riemannian Penrose inequality.

## 8. Future Work

- Replace the Sobolev interpolation in the P-function method with a sharp trace inequality on domains satisfying only a uniform interior-sphere condition; this is the identified route to $\tau=1$ in all $n$.
- Develop a quantitative Heintze–Karcher inequality: bound $|\Omega|^{-1}\int_\Sigma \frac{n-1}{H} - n$ from below by a distance-to-ball functional. Would unify both current approaches.
- Extend Delgadino–Maggi's varifold argument to ambient manifolds, avoiding moving planes entirely — the most promising route to characterizing rigid ambients.
- Settle crystalline anisotropy via viscosity/facet-based maximum principles, or find a counterexample.
- Free-boundary and capillary rigidity in general convex cones with prescribed contact angle; the wedge case remains only partly understood.

## 9. Key References

- **[Foundational]** A. D. Alexandrov. *Uniqueness theorems for surfaces in the large, V.* Vestnik Leningrad Univ. **13** (1958), 5–8; English transl. Amer. Math. Soc. Transl. (2) **21** (1962), 412–416.
- **[Foundational]** E. Heintze, H. Karcher. *A general comparison theorem with applications to volume estimates for submanifolds.* Ann. Sci. École Norm. Sup. (4) **11** (1978), 451–470.
- **[Foundational]** R. C. Reilly. *Applications of the Hessian operator in a Riemannian manifold.* Indiana Univ. Math. J. **26** (1977), 459–472.
- **[Foundational]** A. Ros. *Compact hypersurfaces with constant higher order mean curvatures.* Rev. Mat. Iberoamericana **3** (1987), 447–453.
- **[Foundational]** H. C. Wente. *Counterexample to a conjecture of H. Hopf.* Pacific J. Math. **121** (1986), 193–243.
- **[Foundational]** W.-Y. Hsiang. *Generalized rotational hypersurfaces of constant mean curvature in the Euclidean spaces, I.* J. Differential Geom. **17** (1982), 337–356.
- **[Foundational]** J. Serrin. *A symmetry problem in potential theory.* Arch. Rational Mech. Anal. **43** (1971), 304–318.
- **[SOTA]** S. Brendle. *Constant mean curvature surfaces in warped product manifolds.* Publ. Math. IHÉS **117** (2013), 247–269.
- **[SOTA]** G. Ciraolo, L. Vezzoni. *A sharp quantitative version of Alexandrov's theorem via the method of moving planes.* J. Eur. Math. Soc. **20** (2018), 261–299.
- **[SOTA]** G. Ciraolo, F. Maggi. *On the shape of compact hypersurfaces with almost-constant mean curvature.* Comm. Pure Appl. Math. **70** (2017), 665–716.
- **[SOTA]** M. G. Delgadino, F. Maggi. *Alexandrov's theorem revisited.* Analysis & PDE **12** (2019), 1613–1642.
- **[SOTA]** R. Magnanini, G. Poggesi. *On the stability for Alexandrov's Soap Bubble theorem.* J. Anal. Math. **139** (2019), 179–205.
- **[SOTA]** R. Magnanini, G. Poggesi. *Nearly optimal stability for Serrin's problem and the soap bubble theorem.* Calc. Var. Partial Differential Equations **59** (2020), art. 35.
- **[SOTA]** A. De Rosa, S. Kolasiński, M. Santilli. *Uniqueness of critical points of the anisotropic isoperimetric problem for finite perimeter sets.* Arch. Ration. Mech. Anal. **238** (2020), 1157–1198.
- **[SOTA]** X. Cabré, M. M. Fall, J. Solà-Morales, T. Weth. *Curves and surfaces with constant nonlocal mean curvature: meeting Alexandrov and Delaunay.* J. Reine Angew. Math. **745** (2018), 253–280.
- **[SOTA]** G. Wang, C. Xia. *Uniqueness of stable capillary hypersurfaces in a ball.* Math. Ann. **374** (2019), 1845–1882.
- **[Survey]** R. Magnanini. *Alexandrov, Serrin, Weinberger, Reilly: symmetry and stability by integral identities.* Bruno Pini Math. Anal. Semin. **8** (2017), 121–141.
- **[Survey]** S. Montiel, A. Ros. *Compact hypersurfaces: the Alexandrov theorem for higher order mean curvatures.* In: Differential Geometry (Pitman Monographs 52), Longman, 1991, 279–296.

## 10. Worked Example / Concrete Special Case

**Claim to illustrate: the stability exponent $\tau = 1$ cannot be improved.**

Work in $\mathbb{R}^n$ with the normalization $H = \kappa_1+\cdots+\kappa_{n-1}$. Take a nearly spherical hypersurface written as a radial graph over $S^{n-1}$:
$$\Sigma_\varepsilon = \{\, r(\theta)\,\theta \;:\; \theta \in S^{n-1} \,\}, \qquad r(\theta) = 1 + \varepsilon\, u(\theta), \quad \|u\|_{C^2} \le 1 .$$

**Step 1 — linearize the mean curvature.** A standard computation gives
$$H(\theta) \;=\; (n-1) \;-\; \varepsilon\big( \Delta_{S^{n-1}} u + (n-1)u \big) \;+\; O(\varepsilon^2).$$

**Step 2 — choose a spherical harmonic.** Let $u = Y_\ell$ with $\Delta_{S^{n-1}} Y_\ell = -\lambda_\ell Y_\ell$, $\lambda_\ell = \ell(\ell+n-2)$. Then
$$H = (n-1) + \varepsilon\big(\lambda_\ell - (n-1)\big) Y_\ell + O(\varepsilon^2).$$
- $\ell = 0$: coefficient $-(n-1) \ne 0$ — this is a rescaling, and indeed changes $H$.
- $\ell = 1$: $\lambda_1 = n-1$, coefficient $0$ — the kernel, corresponding to translations. Consistent with rigidity.
- $\ell \ge 2$: coefficient $\lambda_\ell - (n-1) > 0$, so $H$ genuinely oscillates.

**Step 3 — take $n=3$, $\ell=2$, $u = Y_2$ normalized so $\max Y_2 = 1$, $\min Y_2 = -\tfrac12$ (e.g. $Y_2 \propto 3\cos^2\vartheta - 1$).** Then $\lambda_2 = 2\cdot 3 = 6$, $n-1 = 2$, so the coefficient is $6 - 2 = 4$ and
$$\operatorname{osc}(H) \;=\; \|H - H_0\|_{L^\infty} \text{-type deficit} \;=\; 4\varepsilon \cdot \tfrac32 + O(\varepsilon^2) \;=\; 6\varepsilon + O(\varepsilon^2).$$

**Step 4 — measure the distance to a sphere.** The concentric inscribed and circumscribed radii are $\rho_i = 1 + \varepsilon\min Y_2 = 1 - \tfrac{\varepsilon}{2}$ and $\rho_e = 1 + \varepsilon\max Y_2 = 1 + \varepsilon$, so
$$\rho_e - \rho_i \;=\; \tfrac{3}{2}\varepsilon + O(\varepsilon^2).$$

**Step 5 — conclude.**
$$\frac{\rho_e - \rho_i}{\operatorname{osc}(H)} \;=\; \frac{\tfrac32 \varepsilon}{6\varepsilon} \;=\; \frac14 + O(\varepsilon).$$
The ratio stays bounded away from $0$ and $\infty$ as $\varepsilon \to 0$. Hence no estimate $\rho_e-\rho_i \le C\,\operatorname{osc}(H)^\tau$ with $\tau > 1$ can hold, and the constant satisfies $C \ge 1/\big(\lambda_\ell-(n-1)\big)$, minimized at $\ell=2$: $C \ge 1/\big(n - (n-1)\big) = \ldots$ for $n=3$, $C \ge 1/4$. This is exactly the exponent achieved by Ciraolo–Vezzoni (2018), so their result is sharp in this family; the open part is removing the a priori $C^{2,\alpha}$ bound and making $C$ explicit in $n$.

**Sanity check on the exact sphere.** For $\Sigma = S^{n-1}$, $H \equiv n-1$, $|\Omega| = \omega_n$, $|\Sigma| = n\omega_n$, and Heintze–Karcher reads $\int_\Sigma \frac{n-1}{H} = |\Sigma| = n\omega_n = n|\Omega|$ — equality, as the rigidity statement requires.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*