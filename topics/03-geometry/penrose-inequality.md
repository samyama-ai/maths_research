---
id: 03-geometry/penrose-inequality
title: "Penrose Inequality"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Penrose Inequality

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/penrose-inequality` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Penrose's 1973 heuristic argument says: if cosmic censorship holds, a spacetime containing a black hole of horizon area $A$ must have total ADM mass $m$ satisfying

$$m \;\ge\; \sqrt{\frac{A}{16\pi}}.$$

The precise mathematical conjecture (**spacetime Penrose inequality**, still open): let $(M^3,g,k)$ be an asymptotically flat initial data set for the Einstein equations satisfying the dominant energy condition, with ADM mass $m$, and let $\Sigma \subset M$ be the outermost future or past marginally outer trapped surface (MOTS, an *apparent horizon*) with area $|\Sigma|$. Then $m \ge \sqrt{|\Sigma|/16\pi}$, with equality if and only if the data embeds in the Schwarzschild spacetime.

The **Riemannian** case $k \equiv 0$ (time-symmetric data, where the horizon is a minimal surface and the dominant energy condition reduces to nonnegative scalar curvature $R\ge 0$) is a **theorem**: Huisken–Ilmanen (2001) for a single horizon component, Bray (2001) in full generality. The general $k\ne 0$ case, the higher-dimensional case $n\ge 8$, the null (light-cone) version, and the asymptotically hyperbolic version remain open.

A complete resolution means: a proof of the inequality for general $(M,g,k)$ with the rigidity statement, or a counterexample — which, by Penrose's reasoning, would signal a failure of weak cosmic censorship.

## 2. Mathematical Foundations

**Initial data.** A triple $(M^n, g, k)$ with $g$ Riemannian, $k$ a symmetric 2-tensor (second fundamental form of $M$ in a spacetime). The constraint equations define energy and momentum densities
$$16\pi\mu = R_g + (\mathrm{tr}_g k)^2 - |k|_g^2, \qquad 8\pi J = \mathrm{div}_g\!\left(k - (\mathrm{tr}_g k)\,g\right).$$
The **dominant energy condition** (DEC) is $\mu \ge |J|_g$.

**Asymptotic flatness.** $M \setminus K \cong \mathbb{R}^n\setminus \bar B$ with $g_{ij} = \delta_{ij} + O(|x|^{-p})$, $p > (n-2)/2$, $R_g \in L^1$, $k = O(|x|^{-p-1})$. The **ADM mass** is
$$m = \frac{1}{2(n-1)\omega_{n-1}}\lim_{r\to\infty}\int_{S_r}\left(\partial_j g_{ij} - \partial_i g_{jj}\right)\nu^i \, dA,$$
with $\omega_{n-1} = |S^{n-1}|$; for $n=3$ the prefactor is $1/16\pi$.

**Horizons.** With outward normal $\nu$ and mean curvature $H$, the null expansions are $\theta_\pm = H \pm \mathrm{tr}_\Sigma k$. A **MOTS** has $\theta_+ = 0$; when $k=0$ this is $H=0$, a minimal surface. The **outermost** horizon is the boundary of the region that cannot be seen from infinity; it is smooth, embedded, and (for $n=3$, by Meeks–Simon–Yau / Huisken–Ilmanen regularity) has components of spherical topology.

**Riemannian Penrose inequality (theorem, $3\le n\le 7$).** If $R_g\ge 0$ and $\Sigma$ is the outermost minimal surface,
$$m \;\ge\; \frac{1}{2}\left(\frac{|\Sigma|}{\omega_{n-1}}\right)^{\frac{n-2}{n-1}},$$
equality iff $(M,g)$ is the Riemannian Schwarzschild manifold $\left(\mathbb{R}^n\setminus\{0\},\ (1+\tfrac{m}{2|x|^{n-2}})^{\frac{4}{n-2}}\delta\right)$.

**Hawking mass and inverse mean curvature flow (IMCF).** For a surface $\Sigma^2\subset M^3$,
$$m_H(\Sigma) = \sqrt{\frac{|\Sigma|}{16\pi}}\left(1 - \frac{1}{16\pi}\int_\Sigma H^2\, dA\right).$$
Along a family $\partial_t x = \nu/H$, the Geroch monotonicity computation gives, for connected $\Sigma_t$ with $R\ge 0$,
$$\frac{d}{dt} m_H(\Sigma_t) \;\ge\; \sqrt{\frac{|\Sigma_t|}{16\pi}}\cdot\frac{1}{16\pi}\int_{\Sigma_t}\left(2|\nabla \log H|^2 + R + |\mathring{A}|^2\right) \ge 0,$$
using Gauss–Bonnet and $\chi(\Sigma_t)\le 2$. Since $m_H(\Sigma_0)=\sqrt{|\Sigma_0|/16\pi}$ for a minimal surface and $m_H\to m$ at infinity, the inequality follows — provided the flow exists.

**Positive mass theorem.** The $A\to 0$ limit: $m\ge 0$ with equality iff $(M,g,k)$ is a slice of Minkowski space (Schoen–Yau 1979/1981; Witten 1981).

## 3. History & State of the Art (SOTA)

- **1973**: Penrose proposes the inequality in *Naked singularities* (Ann. NY Acad. Sci.) as a falsifiable test of weak cosmic censorship — a violation would produce a spacetime whose Bondi mass decreases below the Schwarzschild bound.
- **1973**: Geroch shows the Hawking mass is monotone under smooth IMCF in $R\ge 0$ manifolds. Jang–Wald (1977) note this yields the Riemannian inequality *if* the flow stays smooth.
- **1990s**: Smooth IMCF is known to develop singularities; the program stalls.
- **1997/2001**: Huisken and Ilmanen introduce the **weak (level-set) formulation** of IMCF, with jumps replacing singularities, and prove the inequality with $|\Sigma|$ the area of the *largest single component* of the horizon (JDG 59 (2001) 353–437).
- **1999/2001**: Bray proves the full inequality (all components) via a **conformal flow of metrics** $g_t = u_t^4 g$ preserving $R\ge 0$, non-increasing horizon area, and non-increasing mass, converging to Schwarzschild (JDG 59 (2001) 177–267).
- **2009**: Bray–Lee extend Bray's method to $3\le n\le 7$; rigidity requires spin in their argument (Duke Math. J. 148 (2009)).
- **2010**: Lam gives a short proof for asymptotically flat **graphs** in $\mathbb{R}^{n+1}$ in all dimensions, using the divergence structure of the scalar curvature of a graph.
- **2010s–2020s**: Nonlinear potential theory ($p$-harmonic and harmonic-level-set methods) gives new proofs; spacetime harmonic functions (Bray–Kazaras–Khuri–Stern) attack the $k\ne0$ case.
- The **spacetime** case remains open in every dimension.

## 4. Partial Results / Verified Cases

| Setting | Status | Source |
|---|---|---|
| $n=3$, $k=0$, single horizon component | Proved | Huisken–Ilmanen 2001 |
| $n=3$, $k=0$, arbitrarily many components | Proved | Bray 2001 |
| $4 \le n \le 7$, $k=0$ | Proved | Bray–Lee 2009 |
| $n\ge 8$, $k=0$ | Open (minimal-hypersurface singularities) | — |
| Asymptotically flat graphs over $\mathbb{R}^n$, all $n$ | Proved | Lam 2010; Huang–Wu 2013 (hypersurfaces in $\mathbb{R}^{n+1}$) |
| $k=0$ with charge, single component (Reissner–Nordström form $m\ge \sqrt{A/16\pi} + q^2\sqrt{\pi/A}$) | Proved | Jang 1979; Disconzi–Khuri 2012 |
| Charged, multiple components | **False** as stated | Weinstein–Yamada 2005 |
| Null (light-cone) Penrose inequality, special foliations | Proved in cases | Sauter 2008; Alexakis 2015; Roesch–Scheuer 2021 |
| Spherically symmetric spacetime data ($k\ne0$) | Proved | Malec–Mars–Simon 2002; Hayward 1994 |
| Asymptotically hyperbolic, graphical / conformally flat classes | Proved | Dahl–Gicquaud–Sakovich 2013; de Lima–Girão 2016 |
| Generalized-trapped-surface version (Bray–Khuri) | Counterexample | Carrasco–Mars 2010 |
| Second-order perturbations of Schwarzschild data | Proved | Alaee–Lesourd–Yau 2021 *(frontier — verify)* |

## 5. Principal Obstacles

- **Both proofs of the Riemannian case are intrinsically time-symmetric.** IMCF monotonicity uses $R\ge 0$ pointwise via Gauss–Bonnet; with $k\ne0$ the DEC only bounds $R \ge |k|^2-(\mathrm{tr}k)^2 + 2|J|$, which has no sign. Bray's conformal flow likewise preserves $R\ge0$, not the constraint pair.
- **Jang's equation** is the standard device for reducing $k\ne0$ to $k=0$: solving $\left(g^{ij}-\frac{f^if^j}{1+|\nabla f|^2}\right)\left(\frac{\nabla_{ij}f}{\sqrt{1+|\nabla f|^2}}-k_{ij}\right)=0$ gives a metric with $R\ge 0$ up to a divergence term — but the graph *blows up* precisely at apparent horizons, producing cylindrical ends and **losing control of the horizon area** and of the ADM mass identification. This is the single largest technical barrier.
- **Topology/connectivity.** Gauss–Bonnet caps $\chi(\Sigma_t)\le 2$ only for connected surfaces; jumps in weak IMCF can merge components, which is why Huisken–Ilmanen only recover the largest component.
- **$n\ge 8$:** area-minimizing hypersurfaces (needed to define the outermost horizon and to run Bray–Lee's argument) can be singular, and the Schoen–Yau minimal-surface machinery for $R\ge0$ fails without the recent (still delicate) singularity-handling results.
- **Rigidity in high dimensions** currently needs a spin assumption in the Bray–Lee argument.
- **The choice of surface is subtle.** Carrasco–Mars (2010) show that replacing "outermost MOTS" by "outermost generalized trapped surface" makes the inequality false — so the conjecture is not robust to reformulation, and any proof must use the MOTS condition sharply.

## 6. The Gap

Proven: $R_g \ge 0$, $k=0$, $3\le n\le 7$, minimal-surface horizon. Conjectured: $\mu \ge |J|$, $k\ne0$, MOTS horizon, all $n$.

The exact missing step is a **quasi-local mass monotone along a flow that starts at a MOTS**. For a MOTS, $H = -\mathrm{tr}_\Sigma k \ne 0$, so $m_H(\Sigma) = \sqrt{|\Sigma|/16\pi}\,(1-\frac{1}{16\pi}\int H^2) < \sqrt{|\Sigma|/16\pi}$ in general: the Hawking mass **undershoots** the target at $t=0$, and no known substitute (Bartnik, Brown–York, Wang–Yau, Bray–Khuri's generalized Jang mass) is simultaneously (i) $\ge \sqrt{|\Sigma|/16\pi}$ on a MOTS, (ii) monotone under DEC, and (iii) asymptotic to the ADM mass. Producing such a functional — or a global flow of data sets converging to Schwarzschild through the constraint set — is the crossing point.

## 7. Current Research (as of June 2026)

- **Spacetime harmonic functions.** Bray–Kazaras–Khuri–Stern's level-set technique (used for the spacetime positive mass theorem and mass–capacity estimates) is being pushed toward the Penrose bound; the obstruction is controlling the horizon term in the Stern-type integral identity. Groups at Duke, Stony Brook, and Columbia. *(frontier — verify)*
- **Nonlinear potential theory.** Agostiniani–Mantegazza–Mazzieri–Oronzio give an IMCF-free proof of the $n=3$ Riemannian inequality via monotonicity along level sets of the harmonic/$p$-harmonic potential (Invent. Math. 2022 / CMP 2022); extensions to $n \ge 8$ and to charged and hyperbolic settings are active.
- **Generalized Jang equation.** Bray–Khuri's program (Jang equation coupled to IMCF or to a conformal flow) continues; Han–Khuri and collaborators handle axisymmetric and asymptotically-cylindrical cases.
- **Null Penrose inequality.** Roesch–Scheuer and Alexakis develop foliations of null cones (shear-free / "cross-sections of foliation") along which a null Hawking mass is monotone; the general asymptotically-flat null cone remains open.
- **Angular momentum and charge.** Conjectured $m \ge \sqrt{\frac{A}{16\pi} + \frac{\pi (2J)^2}{A}}$ (Kerr form) — proved only in axisymmetric, maximal, special classes (Dain, Khuri, Weinstein).
- **Asymptotically hyperbolic Penrose inequality**, relevant to AdS/CFT and to the Bondi mass; open beyond graphical/conformally-flat classes.

## 8. Future Work

- Construct a quasi-local mass satisfying (i)–(iii) of §6; Bartnik mass is the natural candidate but is not computable, and Mantoulidis–Schoen's constructions show its horizon behavior is delicate.
- Extend Bray's conformal flow to a flow through the **constraint manifold** rather than through scalar-curvature-nonnegative metrics.
- Remove the spin hypothesis and reach $n\ge 8$ using Schoen–Yau's and Lohkamp's approaches to singular minimal hypersurfaces.
- Settle the null Penrose inequality on general asymptotically flat null cones — arguably the closest to Penrose's original physical argument.
- Sharpen the charged/multi-component picture: identify the correct inequality that survives the Weinstein–Yamada counterexample.

## 9. Key References

- **[Foundational]** R. Penrose. *Naked singularities.* Annals of the New York Academy of Sciences 224 (1973), 125–134.
- **[Foundational]** R. Geroch. *Energy extraction.* Annals of the New York Academy of Sciences 224 (1973), 108–117.
- **[Foundational]** P. S. Jang, R. M. Wald. *The positive energy conjecture and the cosmic censor hypothesis.* J. Math. Phys. 18 (1977), 41–44. [DOI](https://doi.org/10.1063/1.523134)
- **[Foundational]** G. Huisken, T. Ilmanen. *The inverse mean curvature flow and the Riemannian Penrose inequality.* Journal of Differential Geometry 59 (2001), 353–437. [DOI](https://doi.org/10.4310/jdg/1090349447)
- **[Foundational]** H. L. Bray. *Proof of the Riemannian Penrose inequality using the positive mass theorem.* Journal of Differential Geometry 59 (2001), 177–267. [DOI](https://doi.org/10.4310/jdg/1090349428)
- **[SOTA]** H. L. Bray, D. A. Lee. *On the Riemannian Penrose inequality in dimensions less than eight.* Duke Mathematical Journal 148 (2009), 81–106. [DOI](https://doi.org/10.1215/00127094-2009-020)
- **[SOTA]** M.-K. G. Lam. *The Graph Cases of the Riemannian Positive Mass and Penrose Inequalities in All Dimensions.* PhD thesis, Duke University, 2011 (arXiv:1010.4256).
- **[SOTA]** V. Agostiniani, L. Mazzieri, F. Oronzio. *A Green's function proof of the positive mass theorem.* Communications in Mathematical Physics 405 (2024); and V. Agostiniani, C. Mantegazza, L. Mazzieri, F. Oronzio, *Riemannian Penrose inequality via nonlinear potential theory* (arXiv:1905.05830). [DOI](https://doi.org/10.1007/s00220-024-04941-8)
- **[SOTA]** H. L. Bray, D. Kazaras, M. Khuri, D. Stern. *Harmonic functions and the mass of 3-dimensional asymptotically flat Riemannian manifolds.* Journal of Geometric Analysis 32 (2022), 184. [DOI](https://doi.org/10.1007/s12220-022-00924-0)
- **[Counterexample]** G. Weinstein, S. Yamada. *On a Penrose inequality with charge.* Communications in Mathematical Physics 257 (2005), 703–723. [DOI](https://doi.org/10.1007/s00220-005-1355-0)
- **[Counterexample]** A. Carrasco, M. Mars. *A counter-example to a recent version of the Penrose conjecture.* Classical and Quantum Gravity 27 (2010), 062001.
- **[Survey]** H. L. Bray, P. T. Chruściel. *The Penrose inequality.* In *The Einstein Equations and the Large Scale Behavior of Gravitational Fields*, Birkhäuser, 2004, 39–70.
- **[Survey]** M. Mars. *Present status of the Penrose inequality.* Classical and Quantum Gravity 26 (2009), 193001. [DOI](https://doi.org/10.1088/0264-9381/26/19/193001)
- **[Book]** D. A. Lee. *Geometric Relativity.* Graduate Studies in Mathematics 201, AMS, 2019.

## 10. Worked Example / Concrete Special Case

**Equality case: the Schwarzschild time slice.** Take $M = \mathbb{R}^3\setminus\{0\}$ with
$$g = \left(1+\frac{m}{2r}\right)^{4}\delta, \qquad m>0 .$$
This metric is scalar-flat ($R_g=0$) because $u = 1+\frac{m}{2r}$ is harmonic on $\mathbb{R}^3\setminus\{0\}$ and $R_{u^4\delta} = -8u^{-5}\Delta_\delta u = 0$. It is asymptotically flat with ADM mass exactly $m$ (read off from $g_{ij}=(1+\frac{2m}{r}+\dots)\delta_{ij}$).

*Horizon.* The areal radius of the coordinate sphere $\{r = \rho\}$ is $s(\rho) = \rho\left(1+\frac{m}{2\rho}\right)^2$, so
$$|\{r=\rho\}| = 4\pi \rho^2\left(1+\frac{m}{2\rho}\right)^{4}.$$
Minimizing: $\frac{d}{d\rho}\left[\rho\left(1+\frac{m}{2\rho}\right)^2\right] = \left(1+\frac{m}{2\rho}\right)\left(1-\frac{m}{2\rho}\right) = 0 \Rightarrow \rho = m/2$. The sphere $r=m/2$ is minimal (it is the fixed-point set of the isometric inversion $r\mapsto m^2/4r$), with
$$A = 4\pi\left(\frac{m}{2}\right)^2\!\left(1+1\right)^4 = 16\pi m^2 .$$
Hence $\sqrt{A/16\pi} = m$: **equality holds**, and the inequality is sharp.

*Monotonicity check.* In area-radius coordinate $s$, the metric is $g = (1-2m/s)^{-1}ds^2 + s^2 g_{S^2}$ and the coordinate sphere of radius $s$ has $H = \frac{2}{s}\sqrt{1-\frac{2m}{s}}$. Then
$$\frac{1}{16\pi}\int_{\Sigma_s} H^2\,dA = \frac{4\pi s^2}{16\pi}\cdot\frac{4}{s^2}\left(1-\frac{2m}{s}\right) = 1-\frac{2m}{s},$$
so
$$m_H(\Sigma_s) = \frac{s}{2}\left(1-\left(1-\frac{2m}{s}\right)\right) = m \quad \text{for all } s\ge 2m .$$
The Hawking mass is *constant* along the IMCF in Schwarzschild — the flow is exactly at the equality case of Geroch monotonicity, where $R=0$, $\mathring A = 0$ (spheres are umbilic) and $H$ is constant on each leaf. Starting from the horizon $s=2m$ where $m_H = \sqrt{A/16\pi} = m$, and ending at $s\to\infty$ where $m_H \to m_{ADM}$, this reproduces the inequality with no slack.

*Where the spacetime case breaks.* Boost the slice: take a non-time-symmetric slice of the same Schwarzschild spacetime, so $k \ne 0$. The outermost MOTS $\Sigma$ satisfies $H = -\mathrm{tr}_\Sigma k \ne 0$, hence
$$m_H(\Sigma) = \sqrt{\frac{|\Sigma|}{16\pi}}\left(1 - \frac{1}{16\pi}\int_\Sigma H^2\right) < \sqrt{\frac{|\Sigma|}{16\pi}} ,$$
and IMCF started at $\Sigma$ can only certify $m \ge m_H(\Sigma)$, strictly weaker than the conjecture. That deficit — quantified but not yet closed — is the content of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*