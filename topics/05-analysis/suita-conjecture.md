---
id: 05-analysis/suita-conjecture
title: "Suita Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Suita Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/suita-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Suita Conjecture, originally formulated by Nobuyuki Suita in 1998, proposes a fundamental potential-theoretic inequality that relates two crucial, domain-dependent invariants on an open Riemann surface: the logarithmic capacity (or Suita metric) and the Bergman kernel. 

Let $\Omega$ be an open Riemann surface that admits a Green's function $G_\Omega(z, \zeta)$ (i.e., a hyperbolic Riemann surface). For any local coordinate $z$ in a neighborhood of a point $z_0 \in \Omega$, the logarithmic capacity (associated to the Green's function) is defined as:
$$ c_\beta(z_0) = \exp \left( \lim_{z \to z_0} \Big( G_\Omega(z_0, z) + \log |z - z_0| \Big) \right) $$

Let $K_\Omega(z, w)$ be the Bergman kernel of $\Omega$, which represents the reproducing kernel of the Hilbert space of square-integrable holomorphic $(1,0)$-forms on $\Omega$. The restriction of the Bergman kernel to the diagonal, $K_\Omega(z, z)$, transforms as a conformal metric.

The Suita Conjecture states that for any $z \in \Omega$, the following precise inequality holds:
$$ c_\beta(z)^2 \le \pi K_\Omega(z, z) $$
Furthermore, the conjecture asserts a rigid equality condition: the equality $c_\beta(z)^2 = \pi K_\Omega(z, z)$ holds for some (and hence all) $z \in \Omega$ if and only if the Riemann surface $\Omega$ is conformally equivalent to the unit disk $\mathbb{D} \subset \mathbb{C}$ less a (possibly empty) polar set. 

This conjecture represents a deep bridge between the potential theory of Riemann surfaces (governing capacities and Green's functions) and the $L^2$-analytic theory of holomorphic functions (governing the Bergman space).

## 2. Mathematical Foundations

To formalize the Suita Conjecture, one must integrate concepts from classical potential theory and functional analysis on complex manifolds.

**The Bergman Space and Kernel:**
Let $\Omega$ be an open Riemann surface. The Bergman space $A^2(\Omega)$ is the Hilbert space of holomorphic $(1,0)$-forms $\alpha = f(z) dz$ on $\Omega$ such that:
$$ \|\alpha\|^2 = i \int_\Omega \alpha \wedge \bar{\alpha} = 2 \int_\Omega |f(z)|^2 \, dx \, dy < \infty $$
where $z = x + iy$ is a local holomorphic coordinate. Since point evaluation is a bounded linear functional on $A^2(\Omega)$, the Riesz Representation Theorem guarantees the existence of a unique reproducing kernel, the Bergman kernel $K_\Omega(z, w) \, dz \otimes d\bar{w}$. On the diagonal $z = w$, we can write $K_\Omega(z) = K_\Omega(z, z)$, which is strictly positive if $\Omega$ admits non-trivial $L^2$ holomorphic forms. In a local coordinate system, it is given by:
$$ K_\Omega(z) = \sup \left\{ |f(z)|^2 : f(z)dz \in A^2(\Omega), \, \int_\Omega |f(\zeta)|^2 d\lambda(\zeta) \le 1 \right\} $$

**Green's Function and Logarithmic Capacity:**
The Green's function $G_\Omega(z, \zeta)$ for the Laplacian on a Riemann surface $\Omega$ is defined by the following properties:
1. $G_\Omega(z, \zeta)$ is harmonic in $z \in \Omega \setminus \{\zeta\}$.
2. $G_\Omega(z, \zeta) > 0$.
3. Near the singularity $\zeta$, $G_\Omega(z, \zeta) = -\log |z - \zeta| + u(z, \zeta)$, where $u(z, \zeta)$ is a harmonic function of $z$ near $\zeta$.
4. $G_\Omega(z, \zeta) = 0$ for $z \in \partial\Omega$ (if the boundary is sufficiently regular).

The constant term of the regular part evaluated at the singularity yields the Suita metric:
$$ c_\beta(\zeta) = \exp(u(\zeta, \zeta)) = \exp \left( \lim_{z \to \zeta} (G_\Omega(z, \zeta) + \log |z - \zeta|) \right) $$
Under conformal mappings, $c_\beta(z)|dz|$ transforms as an invariant metric, exactly as $\sqrt{K_\Omega(z)}|dz|$ does, making the ratio $c_\beta(z)^2 / K_\Omega(z)$ a well-defined global conformal invariant of the surface $\Omega$.

**Ohsawa-Takegoshi $L^2$ Extension Theorem:**
The most critical mathematical foundation for resolving the conjecture is the Ohsawa-Takegoshi extension theorem, which states that any square-integrable holomorphic function on a complex submanifold can be extended to the entire ambient manifold with a controlled $L^2$ norm. The Suita Conjecture is essentially equivalent to proving an *optimal-constant* version of this theorem for extending from a single point (a 0-dimensional manifold) to the 1-dimensional Riemann surface $\Omega$.

## 3. History & State of the Art (SOTA)

**Formulation and Early Bounds:**
Nobuyuki Suita posed the conjecture in his 1998 paper "Capacities and kernels on Riemann surfaces," building on the observation that the inequality is an identity for the unit disk. The connection between the conjecture and the Ohsawa-Takegoshi extension theorem was realized almost immediately. In the same year, Takeo Ohsawa proved a weaker version of the conjecture, establishing that $c_\beta(z)^2 \le C \pi K_\Omega(z)$ for a universal constant $C = 750$. 

**Iterative Improvements (1998–2012):**
The race to prove the conjecture transformed into a quest to optimize the constant $C$ in the Ohsawa-Takegoshi extension theorem. 
- B.-Y. Chen (2002) reduced the constant to $C \approx 34$.
- Z. Błocki (2012) further reduced the constant to $C = 2$ using a highly refined solution to the weighted $\bar{\partial}$-equation.

**The Resolution (2012–2015):**
The Suita Conjecture was fully resolved in a series of dramatic breakthroughs:
1. **Planar Domains:** In 2013, Zbigniew Błocki published a proof of the Suita conjecture for bounded pseudoconvex domains in $\mathbb{C}$. Błocki utilized advanced pluripotential theory, specifically examining the limit behavior of the pluricomplex Green function.
2. **General Riemann Surfaces:** Independent of Błocki, Qi'an Guan and Xiangyu Zhou (2012 preprints, published in *Annals of Mathematics* in 2015) solved the Suita Conjecture in full generality for all open Riemann surfaces. Their method involved inventing a completely novel, optimal $L^2$ extension theorem. By introducing a new weight function class in the Hörmander $L^2$ estimates for the $\bar{\partial}$-operator, they achieved the sharp constant $C = 1$.
3. **The Equality Condition:** In a subsequent 2015 paper, Guan and Zhou completely characterized the equality condition, proving that equality holds if and only if the Riemann surface is conformally equivalent to $\mathbb{D} \setminus E$, where $E$ is a set of zero logarithmic capacity (a polar set).

## 4. Partial Results / Verified Cases

Prior to its complete resolution, the Suita Conjecture was verified in several specific regimes:

- **Simply Connected Domains:** For the unit disk $\mathbb{D}$, direct computation shows $c_\beta(0) = 1$ and $K_{\mathbb{D}}(0) = 1/\pi$, yielding $1 \le \pi(1/\pi)$, which is a perfect equality. By the Riemann Mapping Theorem, this extends to all simply connected planar domains.
- **Annuli:** Suita initially verified the conjecture for standard annuli $A_r = \{ z \in \mathbb{C} : r < |z| < 1 \}$. The Bergman kernel and Green's function for annuli can be written explicitly in terms of Weierstrass elliptic functions and theta functions, allowing for direct, albeit tedious, verification of the inequality.
- **Tori with Punctures:** Verified analytically by various authors using the explicit forms of Green's functions on abelian varieties.
- **Planar Domains:** Błocki (2013) solved the case where $\Omega \subset \mathbb{C}$ is a bounded domain, bridging the 1D conjecture to pluripotential theory in higher dimensions.

## 5. Principal Obstacles

Before 2012, the Suita Conjecture remained intractable because the primary analytic tool—Hörmander’s $L^2$ method for solving the $\bar{\partial}$-equation—was historically "lossy". 

To prove $c_\beta(z)^2 \le \pi K_\Omega(z)$, one must construct a holomorphic function $f \in A^2(\Omega)$ such that $f(z_0) = 1$ and its $L^2$ norm is precisely bounded above by $\pi / c_\beta(z_0)^2$. The standard procedure involves taking a smooth cutoff function $\chi$ near $z_0$, setting the approximate solution to $u = \chi \cdot 1$, and then correcting this to a true holomorphic function by solving $\bar{\partial} v = \bar{\partial} u$ with $L^2$ estimates.

The obstacle was the standard Bochner-Kodaira-Nakano identity and Hörmander's weighted inequalities. These methods inherently involved applying Cauchy-Schwarz inequalities and integrating over weight functions (typically of the form $e^{-\phi}$ where $\phi$ relates to the Green's function). Traditional choices of weights and standard differential geometric estimates inevitably produced an extraneous constant multiplier $C > 1$ in the final $L^2$ norm bound of $v$. Bypassing this required a structural departure from standard Kähler metric weighting.

## 6. The Gap

The exact boundary that needed to be crossed was the discovery of an *optimal-constant* Ohsawa-Takegoshi extension theorem. The gap was not conceptual—mathematicians knew since 1998 that an optimal extension theorem would immediately imply the Suita Conjecture. The gap was purely analytic: finding the magical combination of weight functions and metrics in the $\bar{\partial}$ complex that would yield no loss of constants.

Guan and Zhou crossed this gap by proving the following optimal extension theorem: 
Let $\Omega$ be a Stein manifold of dimension $n$, and let $H$ be a closed complex submanifold. For a specific class of plurisubharmonic weights $\varphi$, any holomorphic function $f$ on $H$ can be extended to $F$ on $\Omega$ such that:
$$ \int_\Omega |F|^2 e^{-\varphi} dV_\Omega \le \frac{\pi}{\inf \Delta \psi} \int_H |f|^2 e^{-\varphi} dV_H $$
By carefully choosing $\varphi$ as a highly specialized non-linear transformation of the Green's function $G_\Omega(z, z_0)$, Guan and Zhou forced the constant in the inequality to drop exactly to 1, bridging the final gap to the Suita Conjecture.

## 7. Current Research (as of June 2026)

With the Suita Conjecture firmly solved, the field of $L^2$ extension theorems and pluripotential theory has pivoted toward multidimensional analogs and generalizations. 

- **Higher-Dimensional Suita Conjectures:** Researchers are actively investigating higher-dimensional analogs, relating the Bergman kernel of a Stein manifold to the pluricomplex Green function. Błocki, Zwonek, and others have formulated multi-dimensional variants of the Suita inequality.
- **Jet Extension Theorems:** Current research involves finding optimal $L^2$ extension bounds for higher-order derivatives (jet bundles). *Guan, Zhou, and their collaborators are exploring optimal extensions with prescribed jets at isolated points, which translates to fine asymptotic expansions of the Bergman kernel.* 
- **Vector Bundles and Nakano Positivity:** Extending the optimal Ohsawa-Takegoshi theorem from trivial line bundles to holomorphic vector bundles possessing various curvature positivities (like Nakano or Griffiths positivity). *(frontier — verify)* Active preprints from groups at the Chinese Academy of Sciences and various European institutions are attempting to nail down the precise curvature tensor conditions required to maintain the sharp constant $C=1$ for sections of vector bundles.
- **Links to Kähler-Einstein Metrics:** The sharp constants derived from the Suita machinery are currently being used to bound Ricci curvatures and analyze the boundary behavior of Kähler-Einstein metrics on pseudoconvex domains.

## 8. Future Work

Leading complex analysts point to several open pathways stemming from the resolution of the Suita Conjecture:
1. **The Multi-dimensional Equality Condition:** While the optimal extension theorem is known in higher dimensions, characterizing the exact geometric constraints required for the multi-dimensional Suita inequality to become an equality remains an open and fiercely challenging problem. It is conjectured to heavily restrict the manifold to be biholomorphic to the complex unit ball $\mathbb{B}^n$.
2. **Foliations and Levi-flat Manifolds:** Applying optimal $L^2$ extension techniques to complex foliations, specifically investigating how the Suita metric behaves along the leaves of a Levi-flat foliation.
3. **Analytic Torsion:** Linking the sharp constants found in the Bergman kernel estimates directly to analytic torsion and Ray-Singer metrics on Riemann surfaces, providing a purely analytic proof of certain arithmetic intersection inequalities.

## 9. Key References

- **[Foundational]** Suita, N. *Capacities and kernels on Riemann surfaces.* Archiv der Mathematik, 1998.
- **[Foundational]** Ohsawa, T. *On the extension of $L^2$ holomorphic functions. V. Effects of generalization.* Nagoya Mathematical Journal, 1998.
- **[SOTA / Recent]** Błocki, Z. *Suita conjecture and the Ohsawa-Takegoshi extension theorem.* Inventiones Mathematicae, 2013. [DOI](https://doi.org/10.1007/s00222-012-0423-2)
- **[SOTA / Recent]** Guan, Q., and Zhou, X. *A solution of an $L^2$ extension problem with an optimal estimate and applications.* Annals of Mathematics, 2015. [DOI](https://doi.org/10.4007/annals.2015.181.3.6)
- **[SOTA / Recent]** Guan, Q., and Zhou, X. *Optimal constant in an $L^2$ extension problem and a proof of a conjecture of Ohsawa.* Journal de Mathématiques Pures et Appliquées, 2015. [DOI](https://doi.org/10.1007/s11425-014-4946-4)
- **[Survey]** Ohsawa, T. *$L^2$ Approaches in Several Complex Variables.* Springer Monographs in Mathematics, Springer, 2015.

## 10. Worked Example / Concrete Special Case

To ground the Suita Conjecture, we can walk through the explicit calculation for the simplest non-trivial open Riemann surface: the unit disk $\mathbb{D} = \{ z \in \mathbb{C} : |z| < 1 \}$.

**1. Calculating the Logarithmic Capacity:**
The Green's function for the unit disk with a pole at $\zeta \in \mathbb{D}$ is given explicitly by the logarithm of the Möbius transformation mapping the disk to itself:
$$ G_{\mathbb{D}}(z, \zeta) = -\log \left| \frac{z - \zeta}{1 - \bar{\zeta}z} \right| $$
We want to find the capacity at the origin, $z_0 = 0$. The Green's function with a pole at $0$ is simply:
$$ G_{\mathbb{D}}(z, 0) = -\log |z| $$
By the definition of the Suita metric (logarithmic capacity):
$$ c_\beta(0) = \exp \left( \lim_{z \to 0} \Big( G_{\mathbb{D}}(z, 0) + \log |z - 0| \Big) \right) $$
Substituting our Green's function:
$$ c_\beta(0) = \exp \left( \lim_{z \to 0} \Big( -\log |z| + \log |z| \Big) \right) = \exp(0) = 1 $$

**2. Calculating the Bergman Kernel:**
The Bergman space $A^2(\mathbb{D})$ has an orthonormal basis given by $e_n(z) = \sqrt{\frac{n+1}{\pi}} z^n$ for $n \ge 0$.
The Bergman kernel can be expressed as the infinite sum of this orthonormal basis:
$$ K_{\mathbb{D}}(z, w) = \sum_{n=0}^\infty e_n(z) \overline{e_n(w)} = \sum_{n=0}^\infty \frac{n+1}{\pi} z^n \bar{w}^n $$
This is a standard geometric series derivative, which evaluates to:
$$ K_{\mathbb{D}}(z, w) = \frac{1}{\pi (1 - z\bar{w})^2} $$
Restricting the kernel to the diagonal at the origin $z = w = 0$:
$$ K_{\mathbb{D}}(0, 0) = \frac{1}{\pi (1 - 0)^2} = \frac{1}{\pi} $$

**3. Verifying the Suita Inequality:**
The Suita Conjecture demands that $c_\beta(0)^2 \le \pi K_{\mathbb{D}}(0, 0)$. 
Plugging in our computed values:
$$ 1^2 \le \pi \left( \frac{1}{\pi} \right) \implies 1 \le 1 $$
The inequality holds, and in fact, it is a strict equality. As proven by Guan and Zhou, this strict equality $c_\beta(z)^2 = \pi K_{\Omega}(z, z)$ is a characterizing feature of the unit disk (up to the removal of polar sets), perfectly aligning with the rigidity statement of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*