---
id: 03-geometry/hsiang-lawson-conjecture
title: "Hsiang-Lawson Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hsiang-Lawson Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/hsiang-lawson-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Lawson 1970; often "Hsiang–Lawson").** Let $\Sigma \subset S^3$ be a smoothly embedded, closed, minimal surface of genus $1$ in the round unit $3$-sphere. Then $\Sigma$ is congruent, under an isometry of $S^3$, to the **Clifford torus**
$$
\mathbb{T}_{\mathrm{Cl}} \;=\; \Big\{ (x_1,x_2,x_3,x_4)\in S^3 \;:\; x_1^2+x_2^2 = x_3^2+x_4^2 = \tfrac12 \Big\} \;\cong\; \tfrac{1}{\sqrt2}S^1 \times \tfrac{1}{\sqrt2}S^1 .
$$

Three points are essential and each is sharp:

- **Embedded, not immersed.** Immersed minimal tori in $S^3$ exist in abundance — Lawson's own $\tau_{m,k}$ family and the integrable-systems tori of Pinkall–Sterling — so embeddedness is doing real work.
- **Genus exactly $1$.** Genus $0$ is settled by the Almgren–Calabi theorem (every minimal $2$-sphere in $S^3$ is a totally geodesic equator). For genus $g \ge 2$ the analogous uniqueness statement is **false as stated** and remains open in corrected form.
- **Ambient metric is the round one.** The statement fails for Berger spheres and general metrics.

A complete resolution requires showing no embedded minimal torus other than $\mathbb{T}_{\mathrm{Cl}}$ exists. **Status: proved by Simon Brendle (2012, published *Acta Mathematica* 2013).** The page is retained because the natural generalizations (higher genus, CMC analogues in other ambient spaces, quantitative/effective versions) remain open.

## 2. Mathematical Foundations

Let $S^3 \subset \mathbb{R}^4$ be the unit sphere with induced metric, and $F : \Sigma \to S^3$ an immersion of a closed surface with unit normal $\nu$ (a section of the normal bundle in $TS^3$). The **second fundamental form** is
$$
h_{ij} \;=\; \big\langle \bar\nabla_{e_i} \nu,\, e_j \big\rangle, \qquad H \;=\; g^{ij}h_{ij}, \qquad |A|^2 \;=\; g^{ik}g^{jl}h_{ij}h_{kl}.
$$
$\Sigma$ is **minimal** iff $H \equiv 0$; equivalently the coordinate functions $x_\alpha|_\Sigma$ satisfy $\Delta_\Sigma x_\alpha = -2 x_\alpha$, i.e. $\Sigma$ is a minimal submanifold precisely when its embedding is by first-eigenvalue-like harmonic coordinates.

**Gauss equation.** For a surface in $S^3$ with principal curvatures $\lambda_1,\lambda_2$,
$$
K \;=\; 1 + \lambda_1\lambda_2 \;=\; 1 + \tfrac12\big(H^2 - |A|^2\big).
$$
For minimal $\Sigma$, $\lambda_2 = -\lambda_1 =: \kappa \ge 0$, so $|A|^2 = 2\kappa^2$ and $K = 1 - \kappa^2$. Gauss–Bonnet for a torus gives
$$
\int_\Sigma \big(1-\kappa^2\big)\, d\mu \;=\; 2\pi\chi(\Sigma) \;=\; 0 \quad\Longrightarrow\quad \int_\Sigma |A|^2 \, d\mu \;=\; 2\,\mathrm{Area}(\Sigma).
$$

**Simons' identity.** On a minimal surface in $S^3$,
$$
\Delta_\Sigma |A|^2 \;=\; -2|\nabla A|^2 + 2|A|^2\big(2-|A|^2\big),
$$
which yields the Simons gap: a closed minimal surface with $|A|^2 \le 2$ has $|A|^2\equiv 0$ (equator) or $|A|^2 \equiv 2$. Chern–do Carmo–Kobayashi and Lawson identified $|A|^2\equiv 2$ with the Clifford torus. The conjecture is therefore equivalent to: *an embedded minimal torus in $S^3$ has $|A|^2$ constant.*

**Brendle's two-point function.** For $\Sigma$ minimal, embedded, with $\kappa>0$, define on $(\Sigma\times\Sigma)\setminus\mathrm{diag}$ and $\varepsilon \in (0,1]$:
$$
Z_\varepsilon(x,y) \;=\; \varepsilon\,\kappa(x)\big(1 - \langle x,y\rangle\big) \;-\; \big\langle \nu(x),\, y \big\rangle .
$$
$Z_\varepsilon \ge 0$ is a **noncollapsing** condition: it says the geodesic ball of curvature radius $\varepsilon^{-1}\kappa(x)^{-1}$ tangent to $\Sigma$ at $x$ from the inside meets $\Sigma$ only at $x$. Embeddedness plus compactness gives $Z_\varepsilon \ge 0$ for $\varepsilon$ close to $1$ after rescaling; the content of the proof is propagating this to all $\varepsilon>0$.

**Clifford torus data.** $\mathbb{T}_{\mathrm{Cl}}$ is flat, has $\kappa \equiv 1$, $|A|^2 \equiv 2$, $\mathrm{Area} = 2\pi^2$, Willmore energy $\int (1+H^2/4) = 2\pi^2$, Morse index $5$, and nullity $4$.

## 3. History & State of the Art (SOTA)

- **1966–1970.** Simons' gap theorem; Chern–do Carmo–Kobayashi classify minimal hypersurfaces of spheres with $|A|^2$ constant equal to the gap value.
- **1970.** H. Blaine Lawson Jr., *Complete minimal surfaces in $S^3$* (Ann. of Math. 92), constructs embedded minimal surfaces $\xi_{m,k}$ of every genus $g\ge 1$ and the immersed tori $\tau_{m,k}$, and poses the uniqueness question for embedded tori.
- **1971.** Hsiang–Lawson, *Minimal submanifolds of low cohomogeneity* (J. Differential Geom. 5), develops the equivariant machinery reducing symmetric cases to ODEs; the conjecture's dual attribution stems from this circle of work and from W.-Y. Hsiang's later equivariant constructions.
- **1985–1989.** Pinkall–Sterling and Hitchin classify **all** immersed minimal tori in $S^3$ via integrable systems (finite-gap/spectral-curve data), showing the immersed problem has infinite-dimensional families — none of the non-Clifford ones is embedded, but the classification does not decide embeddedness.
- **1990.** Urbano: a closed minimal surface in $S^3$ that is not totally geodesic has Morse index $\ge 5$, with equality **iff** it is the Clifford torus.
- **1995.** Ros: two-piece property and a proof of the conjecture under an antipodal-symmetry hypothesis.
- **2012/2013.** **Simon Brendle** proves the conjecture in full, using Ben Andrews' two-point maximum principle for the function $Z_\varepsilon$ above.
- **2014.** Marques–Neves prove the Willmore conjecture (min-max), giving an independent variational picture in which $\mathbb{T}_{\mathrm{Cl}}$ is the unique minimizer of $\int (1+H^2/4)$ among tori in $\mathbb{R}^3$/$S^3$.
- **2015.** Andrews–Li extend Brendle's method to classify **all embedded CMC tori** in $S^3$ (the Pinkall–Sterling conjecture): they are exactly the rotationally symmetric ones.

## 4. Partial Results / Verified Cases

Before Brendle, the conjecture was known in these concrete classes:

| Class | Result | Source |
|---|---|---|
| Genus $0$ | Every minimal $S^2 \subset S^3$ is an equator | Almgren (1966), Calabi |
| $|A|^2 \le 2$ pointwise | $\Sigma$ is equator or Clifford torus | Simons; Chern–do Carmo–Kobayashi (1970) |
| $|A|^2$ constant, genus $1$ | Clifford torus | Lawson (1969/70) |
| Index $\le 5$ | Equator ($=1$) or Clifford torus ($=5$) | Urbano (1990) |
| Antipodally invariant tori ($-\Sigma = \Sigma$) | Clifford torus | Ros (1995) |
| Invariant under a $1$-parameter isometry group (cohomogeneity one) | ODE reduction, Clifford only | Hsiang–Lawson (1971) |
| Tori with $\lambda_1 = 2$ (first-eigenvalue normalization) | Clifford torus | Montiel–Ros; El Soufi–Ilias |
| Area $\le 2\pi^2 + \delta$ | Clifford (via Willmore/min-max) | Marques–Neves (2014) |
| Embedded CMC tori, all $H \in \mathbb{R}$ | rotationally symmetric | Andrews–Li (2015) |

Brendle's theorem removes all hypotheses: **genus $1$, embedded, minimal $\Rightarrow$ Clifford**, unconditionally.

## 5. Principal Obstacles

Why the problem resisted for 42 years, and why the remaining generalizations resist now:

- **Embeddedness is not a local condition and not a differential inequality.** Every classical tool for minimal surfaces — Simons' identity, stability/index estimates, Bochner formulas — is local or integral in a single point. The hypothesis distinguishing $\mathbb{T}_{\mathrm{Cl}}$ from the immersed Lawson tori $\tau_{m,k}$ lives on $\Sigma\times\Sigma$. Any single-point maximum principle sees $\tau_{m,k}$ as an equally valid competitor.
- **Integrable-systems classification is transcendental.** Pinkall–Sterling/Hitchin give all minimal tori as spectral-curve data, but embeddedness translates into a global condition on theta functions with no known algebraic characterization. The classification is complete and yet decides nothing.
- **No a priori curvature bound.** $\int_\Sigma |A|^2 = 2\,\mathrm{Area}$ controls only the $L^2$ norm; a genus-$1$ minimal surface could a priori have $\sup |A|$ arbitrarily large with concentration, and Choi–Schoen compactness needs an area bound that is not available in advance.
- **Variational routes lose the genus.** Min-max produces a minimal surface of controlled index or width, but the genus of the limit can drop or the limit can appear with multiplicity, so a variational characterization of "the" minimal torus does not directly follow.
- **Higher genus is genuinely different.** For $g \ge 2$ the Lawson surfaces $\xi_{g,1}$, the Karcher–Pinkall–Sterling examples, and Kapouleas–Yang doublings of $\mathbb{T}_{\mathrm{Cl}}$ give several non-congruent embedded minimal surfaces of the same genus, so no uniqueness statement of the Clifford type can hold; only a conjectural least-area characterization survives.

## 6. The Gap

For genus $1$ the gap is **closed**. The step that closed it: Andrews' two-point maximum principle applied to $Z_\varepsilon$. Brendle considers
$$
\varepsilon_0 \;=\; \inf\{\varepsilon\in(0,1] : Z_\varepsilon \ge 0 \text{ on } \Sigma\times\Sigma\}.
$$
If $\varepsilon_0 > 0$, then $Z_{\varepsilon_0}$ attains an interior zero at some $(x_0,y_0)$ with $x_0 \ne y_0$. Differentiating the constraint in both variables and feeding the first-order conditions into the Codazzi and Simons identities produces a second-order inequality that the maximum principle forbids — unless $\nabla A \equiv 0$-type rigidity holds. Hence $\varepsilon_0 = 0$ is impossible too by the same rigidity, and the surviving case forces $\kappa$ constant, i.e. $|A|^2 \equiv 2$, whence Lawson's classification gives $\mathbb{T}_{\mathrm{Cl}}$.

The **remaining gaps** are the generalizations:

1. **Genus $g \ge 2$:** is the Lawson surface $\xi_{g,1}$ the embedded minimal surface of genus $g$ of least area? Is it the unique one of index $\le 2g+3$? Open.
2. Uniqueness of minimal tori in non-round metrics on $S^3$, e.g. Berger spheres and metrics of positive Ricci curvature.
3. An effective/quantitative version: if $\Sigma$ is an embedded minimal torus with $\||A|^2-2\|_{L^2}\le \delta$, how close is it to $\mathbb{T}_{\mathrm{Cl}}$ in $C^k$? No sharp stability constant is known.

## 7. Current Research (as of June 2026)

- **Higher-genus uniqueness and index.** Work in the Marques–Neves min-max school (IMPA, Princeton, Chicago) on index/genus relations and on the conjectural least-area role of $\xi_{g,1}$. Kapouleas–McGrath's gluing programme constructs new embedded minimal surfaces by desingularization and doublings, sharpening what uniqueness could even mean. *(frontier — verify)*
- **Two-point functions beyond $S^3$.** Andrews' noncollapsing method has been pushed to CMC surfaces (Andrews–Li), to free-boundary minimal surfaces in the ball (where the analogue of the conjecture is the **critical catenoid conjecture**, still open), and to ancient solutions of mean curvature flow. The critical catenoid case is the most active direct descendant. *(frontier — verify)*
- **Spectral/integrable approaches.** Continued study of spectral curves of minimal tori (Bobenko, Heller–Heller–Schmitt) now aims at explicit deformations of $\xi_{g,1}$ and at the equivariant spectral genus, giving quantitative area estimates for Lawson surfaces.
- **Willmore-type stability.** Refinements of Marques–Neves toward quantitative Willmore inequalities with explicit deficit constants.

## 8. Future Work

- Prove or refute: among closed embedded minimal surfaces of genus $g$ in $S^3$, $\xi_{g,1}$ minimizes area; equivalently, area is a strictly increasing function of genus with the known values as minima.
- Resolve the **critical catenoid conjecture**: the critical catenoid is the unique embedded free-boundary minimal annulus in $B^3$. Brendle's method is the leading candidate; the obstruction is the boundary term in the two-point argument.
- Extend noncollapsing to ambient $3$-manifolds of positive Ricci curvature, replacing $\langle x,y\rangle$ by the ambient distance function — the difficulty is the failure of the exact algebraic identities available in $S^3$.
- Develop a genuinely effective version of Brendle's argument giving an explicit $\delta$-to-$C^k$ stability modulus.
- Determine whether index $2g+3$ characterizes $\xi_{g,1}$, extending Urbano's index-$5$ theorem.

## 9. Key References

- **[Foundational]** H. B. Lawson Jr. *Complete minimal surfaces in $S^3$.* Annals of Mathematics **92** (1970), 335–374.
- **[Foundational]** W.-Y. Hsiang and H. B. Lawson Jr. *Minimal submanifolds of low cohomogeneity.* Journal of Differential Geometry **5** (1971), 1–38. [DOI](https://doi.org/10.4310/jdg/1214429775)
- **[Foundational]** J. Simons. *Minimal varieties in Riemannian manifolds.* Annals of Mathematics **88** (1968), 62–105. [DOI](https://doi.org/10.2307/1970556)
- **[Foundational]** S. S. Chern, M. do Carmo, S. Kobayashi. *Minimal submanifolds of a sphere with second fundamental form of constant length.* In *Functional Analysis and Related Fields*, Springer, 1970, 59–75. [DOI](https://doi.org/10.1007/978-3-642-48272-4_2)
- **[Foundational]** U. Pinkall and I. Sterling. *On the classification of constant mean curvature tori.* Annals of Mathematics **130** (1989), 407–451. [DOI](https://doi.org/10.2307/1971425)
- **[SOTA]** S. Brendle. *Embedded minimal tori in $S^3$ and the Lawson conjecture.* Acta Mathematica **211** (2013), 177–190.
- **[SOTA]** B. Andrews and H. Li. *Embedded constant mean curvature tori in the three-sphere.* Journal of Differential Geometry **99** (2015), 169–189. [DOI](https://doi.org/10.4310/jdg/1421415560)
- **[SOTA]** F. C. Marques and A. Neves. *Min-max theory and the Willmore conjecture.* Annals of Mathematics **179** (2014), 683–782. [DOI](https://doi.org/10.4007/annals.2014.179.2.6)
- **[Related]** F. Urbano. *Minimal surfaces with low index in the three-dimensional sphere.* Proceedings of the AMS **108** (1990), 989–992. [DOI](https://doi.org/10.2307/2047957)
- **[Related]** A. Ros. *A two-piece property for compact minimal surfaces in a three-sphere.* Indiana University Mathematics Journal **44** (1995), 841–849. [DOI](https://doi.org/10.1512/iumj.1995.44.2011)
- **[Survey]** S. Brendle. *Minimal surfaces in $S^3$: a survey of recent results.* Bulletin of Mathematical Sciences **3** (2013), 133–171. [DOI](https://doi.org/10.1007/s13373-013-0034-2)
- **[Survey]** B. Andrews. *Noncollapsing in mean-convex mean curvature flow.* Geometry & Topology **16** (2012), 1413–1418. [DOI](https://doi.org/10.2140/gt.2012.16.1413)

## 10. Worked Example / Concrete Special Case

**Verify the Clifford torus and evaluate Brendle's function on it.** Parametrize
$$
x(u,v) \;=\; \tfrac{1}{\sqrt2}\big(\cos u,\ \sin u,\ \cos v,\ \sin v\big), \qquad (u,v)\in[0,2\pi)^2 .
$$
Then $|x|=1$, $x_u = \tfrac{1}{\sqrt2}(-\sin u,\cos u,0,0)$, $x_v = \tfrac{1}{\sqrt2}(0,0,-\sin v,\cos v)$, so the induced metric is $g = \tfrac12(du^2+dv^2)$: the torus is **flat**, with area $\tfrac12\cdot(2\pi)^2 = 2\pi^2$.

A unit normal in $TS^3$ is $\nu = \tfrac{1}{\sqrt2}(\cos u,\sin u,-\cos v,-\sin v)$; check $\langle \nu,x\rangle = \tfrac12-\tfrac12 = 0$ and $\langle\nu,x_u\rangle=\langle\nu,x_v\rangle=0$. Now
$$
\nu_u = \tfrac{1}{\sqrt2}(-\sin u,\cos u,0,0) = x_u, \qquad \nu_v = -x_v .
$$
Hence $h_{uu} = \langle \nu_u, x_u\rangle = \tfrac12$, $h_{vv} = -\tfrac12$, $h_{uv}=0$. With $g^{uu}=g^{vv}=2$ the principal curvatures are $\lambda_1 = 2\cdot\tfrac12 = 1$ and $\lambda_2 = -1$. So
$$
H = \lambda_1+\lambda_2 = 0 \ (\text{minimal}), \qquad |A|^2 = 2, \qquad \kappa \equiv 1, \qquad K = 1-\kappa^2 = 0 .
$$
This matches Gauss–Bonnet: $\int_\Sigma |A|^2 = 2\cdot 2\pi^2 = 2\,\mathrm{Area}$.

**Sharpness of $\varepsilon = 1$.** Fix $x_0 = x(0,0) = \tfrac{1}{\sqrt2}(1,0,1,0)$, $\nu_0 = \tfrac{1}{\sqrt2}(1,0,-1,0)$, and let $y = x(u,v)$. Then
$$
\langle x_0,y\rangle = \tfrac{\cos u+\cos v}{2}, \qquad \langle \nu_0,y\rangle = \tfrac{\cos u-\cos v}{2},
$$
so with $\kappa \equiv 1$,
$$
Z_1(x_0,y) \;=\; \big(1-\langle x_0,y\rangle\big) - \langle \nu_0,y\rangle \;=\; 1 - \tfrac{\cos u+\cos v}{2} - \tfrac{\cos u-\cos v}{2} \;=\; 1-\cos u \;\ge\; 0 .
$$
Equality holds exactly on the circle $\{u=0\}$ — a whole one-parameter family of touching points, not just the diagonal. So the Clifford torus is $1$-noncollapsed **and sits exactly at the boundary** of the noncollapsing condition: for any $\varepsilon > 1$ one computes $Z_\varepsilon(x_0, x(0,\pi)) = \varepsilon\cdot 1\cdot(1-0) - 1 \cdot$ (sign check) and the inequality degenerates. This borderline behaviour is precisely why the equality case of the two-point maximum principle can only be the Clifford torus, and it is the geometric content of Brendle's proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*