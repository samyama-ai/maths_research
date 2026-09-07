---
id: 06-pdes/helfrich-willmore-boundary-value
title: "Helfrich Willmore Boundary Value Problem"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Helfrich–Willmore Boundary Value Problem

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/helfrich-willmore-boundary-value` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Gamma \subset \mathbb{R}^3$ be a smooth closed curve (or a finite disjoint union of such curves) and let $N$ be a prescribed unit normal field along $\Gamma$. The **Helfrich–Willmore boundary value problem** asks for a surface $\Sigma$ with $\partial\Sigma = \Gamma$, attaining the prescribed tangent planes along $\Gamma$ (Dirichlet data) or a prescribed contact angle / free conormal (Navier or natural data), which is critical for the Helfrich energy

$$\mathcal{H}_{c_0}(\Sigma) \;=\; \int_\Sigma (H - c_0)^2 \, d\mu \;+\; \lambda\,\operatorname{Area}(\Sigma) \;+\; p\,\operatorname{Vol}(\Sigma),$$

where $H = \tfrac12(\kappa_1+\kappa_2)$ is the mean curvature, $c_0 \in \mathbb{R}$ the spontaneous curvature, and $\lambda, p$ are Lagrange multipliers (or prescribed constants).

**The open problem, in three linked parts.**

1. **Existence.** For $c_0 \neq 0$, does every admissible boundary datum $(\Gamma, N)$ of disk type bound a smooth Helfrich surface minimizing $\mathcal{H}_{c_0}$ in its class? For $c_0 = 0$ (Willmore case) a Douglas-type energy condition suffices; no analogue is known for $c_0\neq0$ without smallness of $|c_0|$ or an area constraint.
2. **Regularity up to the boundary.** Are minimizers/critical points smooth up to $\Gamma$, and is the boundary branch-point set empty?
3. **Sharp existence threshold.** Determine the exact condition on $(\Gamma, N, c_0, \lambda, p)$ separating existence from non-existence, in particular whether energy concentration into spheres of radius $1/|c_0|$ can be excluded.

A complete resolution requires either a proof of existence + boundary regularity under an explicit, sharp hypothesis, or an explicit boundary datum for which the infimum of $\mathcal{H}_{c_0}$ is not attained by any branched immersion.

## 2. Mathematical Foundations

Let $f: \Sigma \to \mathbb{R}^3$ be a $W^{2,2}\cap W^{1,\infty}$ immersion of a compact surface with boundary, $g = f^*\delta$ the induced metric, $A$ the second fundamental form, $\mathring{A} = A - \tfrac12 g\,\vec H$ its trace-free part, $K$ the Gauss curvature. The **Willmore energy** is $\mathcal{W}(f) = \int_\Sigma H^2 d\mu$; by Gauss–Bonnet,

$$\int_\Sigma |A|^2 d\mu = 4\mathcal{W}(f) - 2\int_\Sigma K\, d\mu, \qquad \int_\Sigma K\,d\mu = 2\pi\chi(\Sigma) - \int_{\partial\Sigma}\kappa_g\,ds .$$

$\mathcal{W}$ is invariant under the Möbius group of $\mathbb{R}^3\cup\{\infty\}$; $\mathcal{H}_{c_0}$ with $c_0\neq0$ is invariant only under rigid motions and, after rescaling $c_0 \mapsto c_0/\rho$, dilations.

**Euler–Lagrange (shape) equation.** Critical points of $\mathcal{H}_{c_0}$ satisfy the fourth-order quasilinear elliptic system

$$\Delta_g H \;+\; 2(H-c_0)\big(H^2 + c_0 H - K\big) \;-\;\lambda H \;+\; \tfrac{p}{2} \;=\; 0 \quad\text{on } \Sigma^{\circ},$$

which for $c_0=\lambda=p=0$ reduces to the **Willmore equation** $\Delta_g H + 2H(H^2-K)=0$. In divergence form (Rivière), $\Delta_g \vec H + \text{lower order} = 0$ can be rewritten as a conservation law $\operatorname{div}\big(\nabla \vec H - 3\pi_{\vec n}\nabla\vec H + \star(\nabla^\perp \vec n \wedge \vec H)\big)=0$, giving a Wente-type compensation structure.

**Boundary conditions.**
- *Dirichlet:* $f|_{\partial\Sigma} = \gamma$, $\;\mathrm{d}f(T_p\partial\Sigma)\oplus \mathbb{R}\nu = $ prescribed plane, i.e. $f$ and its normal $n$ are prescribed on $\Gamma$.
- *Navier:* $f|_{\partial\Sigma} = \gamma$, $H = 0$ (or $H = c_0$) on $\Gamma$.
- *Natural / free:* $f|_{\partial\Sigma}=\gamma$ with the variational condition $\partial_\nu H = 0$ and $\mathring{A}(\nu,\nu)=0$ along $\Gamma$; for a free boundary on a support surface $S$, $\Sigma \perp S$ and $\partial_\nu H = 0$.

**Function space and compactness.** The natural class is $W^{2,2}$ immersions with $\int|A|^2 \le \Lambda$. Along such a sequence one has Langer/Simon graph decompositions, but only *branched* conformal immersions in the limit; the energy quantization threshold is $8\pi$ for closed surfaces and $4\pi$ for boundary points ($\mathcal{W} < 4\pi$ near a boundary point excludes branching).

## 3. History & State of the Art (SOTA)

- **1965.** Willmore introduces $\int H^2$ and the conjecture $\mathcal{W}\ge 2\pi^2$ for tori.
- **1973.** Helfrich proposes $\int (H-c_0)^2 + $ area/volume terms as the bending energy of lipid bilayers; $c_0$ encodes bilayer asymmetry. Canham (1970) had used the $c_0=0$ version for red blood cells.
- **1993.** Nitsche formulates the boundary value problems (Dirichlet, Navier, free) for curvature integrals systematically and derives the natural boundary conditions.
- **1993.** Simon's direct method gives existence of closed Willmore minimizers of prescribed genus; the ambient technique (graph decomposition + Simon's monotonicity) underlies almost everything since.
- **2004.** Kuwert–Schätzle: removability of point singularities of Willmore surfaces; branch points with $\mathcal{W}<8\pi$ can be handled.
- **2007–2011.** Deckelnick–Grunau and Dall'Acqua–Fröhlich–Grunau–Schieweck settle the axisymmetric Willmore Dirichlet problem: existence for *arbitrary* symmetric Dirichlet data among surfaces of revolution.
- **2008/2014.** Rivière's conservation laws give $\varepsilon$-regularity and a weak framework for Willmore immersions with $L^2$-bounded second fundamental form.
- **2010.** Schätzle proves existence of branched Willmore immersions in $S^n$ with prescribed boundary and tangent planes under a Douglas-type condition comparing the infimum against $4\pi$.
- **2019–2020.** Eichmann obtains existence for the **Helfrich** boundary value problem in the axisymmetric setting and lower-semicontinuity results for $\mathcal{H}_{c_0}$; Mondino–Scharrer prove existence of minimizing Canham–Helfrich *spheres* under explicit energy hypotheses.

The full boundary problem for $c_0\neq0$, without symmetry and without smallness, remains open.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $c_0=0$, closed, genus $g$ | Simon (1993), Bauer–Kuwert (2003): minimizers exist for every genus |
| $c_0=0$, Dirichlet boundary in $S^n$ | Schätzle (2010): branched minimizer exists if $\inf \mathcal{W} < 4\pi$ (Douglas condition) |
| $c_0=0$, surfaces of revolution, arbitrary symmetric Dirichlet data | Dall'Acqua–Fröhlich–Grunau–Schieweck (2011): classical solutions exist; Dall'Acqua–Deckelnick–Grunau (2008) for the annular case |
| $c_0=0$, natural/Navier boundary data, axisymmetric | Bergner–Dall'Acqua–Fröhlich (2010): existence and estimates |
| One-dimensional Willmore equation (elastic curves as graphs) | Deckelnick–Grunau (2007): complete existence/uniqueness/nonuniqueness picture for symmetric Dirichlet data |
| $c_0 \neq 0$, axisymmetric BVP | Eichmann (*Calc. Var. PDE* 58, 2019): existence of an axisymmetric Helfrich minimizer for Dirichlet data, under an area/energy constraint |
| $c_0 \neq 0$, closed spheres, $\lambda,p$ constraints | Mondino–Scharrer (2020): minimizing Canham–Helfrich spheres exist when the energy is below the explicit threshold; Choksi–Veneroni (2013) for axisymmetric area+volume constrained minimizers |
| Free boundary on a support surface, small data | Alessandroni–Kuwert (2016): local minimizers exist for a free boundary Willmore problem with small prescribed area |
| Graph case with relaxation | Deckelnick–Grunau–Röger (2017): the relaxed Willmore functional for graphs with boundary conditions is minimized |
| Uniqueness | Palmer (2000): uniqueness/rigidity theorems for Willmore surfaces with fixed and free boundaries under curvature hypotheses |

## 5. Principal Obstacles

- **Loss of conformal invariance.** All quantitative Willmore machinery — Li–Yau inequality, Simon's monotonicity formula, the $8\pi$/$4\pi$ energy thresholds, inversion tricks — depends on Möbius invariance of $\int H^2$. For $c_0 \ne 0$ the cross term $-2c_0\int H\,d\mu$ scales like area under dilation and is *not* controlled by $\mathcal{H}_{c_0}$: minimizing sequences can inflate area while keeping energy bounded.
- **Failure of coercivity and lower semicontinuity.** $\int (H-c_0)^2$ does not control $\int H^2$ (expand: $\int H^2 \le 2\mathcal{H}_{c_0} + 2c_0^2 |\Sigma|$, useless without an area bound). Under varifold/weak convergence, $\mathcal{H}_{c_0}$ is only semicontinuous after accounting for multiplicity: a limit of multiplicity $m$ contributes $\int(H - c_0)^2$ but the approximants may carry $c_0$-terms with opposite orientation, so semicontinuity can fail without orientation control.
- **Concentration into $c_0$-spheres.** Spheres of radius $1/|c_0|$ have $\mathcal{H}_{c_0}=0$ (see §10). Minimizing sequences can bubble off arbitrarily many such spheres at zero energy cost, defeating the direct method unless area/volume constraints or connectedness are imposed.
- **Fourth order.** No maximum principle, no comparison surfaces, no Perron method. Regularity comes only from $\varepsilon$-regularity in $\int|A|^2$; the constants degrade at the boundary because the boundary integral $\int_\Gamma \kappa_g$ enters Gauss–Bonnet with an unfavourable sign.
- **Boundary branch points.** Schätzle's compactness yields *branched* immersions; excluding a branch point on $\Gamma$ requires the local energy below $4\pi$, exactly the quantity one cannot control for general data.

## 6. The Gap

Proven (§4) covers: (i) $c_0=0$ with a Douglas-type strict inequality $\inf\mathcal{W} < 4\pi$, allowing branch points; (ii) $c_0\ne0$ only under rotational symmetry or an a priori area/energy constraint. The general statement (§1) demands existence for **arbitrary** $(\Gamma,N)$, arbitrary $c_0$, **without** symmetry, **with** boundary regularity and no branch points.

The precise missing step is a **replacement for Möbius invariance**: a monotonicity or Li–Yau-type inequality for $\mathcal{H}_{c_0}$ that (a) bounds $\operatorname{Area}(\Sigma)$ in terms of $\mathcal{H}_{c_0}(\Sigma)$, $\operatorname{diam}(\Gamma)$ and $c_0$, and (b) gives a local energy threshold at boundary points ruling out branching. Without (a) the direct method has no compactness; without (b) even a weak limit may be branched, so "solution" is achieved only in a weaker sense than asked.

## 7. Current Research (as of June 2026)

- **Magdeburg/Regensburg school (Grunau, Eichmann, Dall'Acqua, Müller):** axisymmetric Helfrich BVPs, asymptotics of solutions as boundary data degenerate, and Willmore flow with boundary conditions as a route to existence. *(frontier — verify)* continued work on convergence of the boundary-constrained Willmore flow to critical points.
- **Freiburg/ETH/Tübingen (Kuwert, Rivière, Schätzle, Mondino, Scharrer):** varifold and branched-immersion formulations, quantization of the Helfrich energy, and the multiphase Canham–Helfrich functional (Brazda–Lussardi–Stefanelli).
- **Pisa/Naples (Pozzetta, Novaga):** Plateau–Douglas problems for the Willmore energy with planar boundary curves; confinement and area-constrained variants.
- **Applied/numerics:** isogeometric and phase-field discretizations of the Helfrich BVP for lipid membranes with edges and open patches; used to conjecture the shape of minimizers when $|c_0|\,\mathrm{diam}(\Gamma) \gg 1$. *(frontier — verify)*

## 8. Future Work

- Prove a **diameter–area–energy inequality** for $\mathcal{H}_{c_0}$ on surfaces with boundary, the analogue of Simon's monotonicity, which would immediately give compactness of minimizing sequences.
- Establish a **sharp Douglas condition** for $c_0\ne0$: identify the constant $\Theta(c_0,\Gamma)$ replacing $4\pi$ below which minimizers are unbranched and smooth up to $\Gamma$.
- Settle **non-existence**: construct $(\Gamma,N)$ and $c_0$ with $\inf\mathcal{H}_{c_0}$ not attained, presumably by exhibiting a bubbling sequence of $c_0$-spheres attached to a degenerating neck.
- Use the **Willmore/Helfrich $L^2$-gradient flow** with Dirichlet or Navier boundary data as a constructive existence proof, extending Kuwert–Schätzle's small-energy global existence to the boundary setting.
- Extend Rivière's **conservation laws** to $c_0\neq0$; the divergence structure survives with an explicit $c_0$-dependent correction, potentially restoring $\varepsilon$-regularity.

## 9. Key References

- **[Foundational]** W. Helfrich. *Elastic properties of lipid bilayers: theory and possible experiments.* Zeitschrift für Naturforschung C 28 (1973), 693–703.
- **[Foundational]** T. J. Willmore. *Note on embedded surfaces.* An. Şti. Univ. "Al. I. Cuza" Iaşi, Sect. I a Mat. 11B (1965), 493–496.
- **[Foundational]** J. C. C. Nitsche. *Boundary value problems for variational integrals involving surface curvatures.* Quarterly of Applied Mathematics 51 (1993), 363–387.
- **[Foundational]** L. Simon. *Existence of surfaces minimizing the Willmore functional.* Communications in Analysis and Geometry 1 (1993), 281–326.
- **[SOTA]** R. Schätzle. *The Willmore boundary problem.* Calculus of Variations and PDE 37 (2010), 275–302.
- **[SOTA]** S. Eichmann. *The Helfrich boundary value problem.* Calculus of Variations and PDE 58 (2019), article 34.
- **[SOTA]** A. Mondino, C. Scharrer. *Existence and regularity of spheres minimising the Canham–Helfrich energy.* Archive for Rational Mechanics and Analysis 236 (2020), 1455–1485.
- **[SOTA]** A. Dall'Acqua, S. Fröhlich, H.-Ch. Grunau, F. Schieweck. *Symmetric Willmore surfaces of revolution satisfying arbitrary Dirichlet boundary data.* Advances in Calculus of Variations 4 (2011), 1–81.
- **[SOTA]** K. Deckelnick, H.-Ch. Grunau. *Boundary value problems for the one-dimensional Willmore equation.* Calculus of Variations and PDE 30 (2007), 293–314.
- **[SOTA]** R. Alessandroni, E. Kuwert. *Local solutions to a free boundary problem for the Willmore functional.* Calculus of Variations and PDE 55 (2016), article 24.
- **[SOTA]** M. Bergner, A. Dall'Acqua, S. Fröhlich. *Symmetric Willmore surfaces of revolution satisfying natural boundary conditions.* Calculus of Variations and PDE 39 (2010), 361–378.
- **[SOTA]** R. Choksi, M. Veneroni. *Global minimizers for the doubly-constrained Helfrich energy: the axisymmetric case.* Calculus of Variations and PDE 48 (2013), 337–366.
- **[SOTA]** K. Brazda, L. Lussardi, U. Stefanelli. *Existence of varifold minimizers for the multiphase Canham–Helfrich functional.* Calculus of Variations and PDE 59 (2020), article 93.
- **[Survey]** T. Rivière. *Analysis aspects of Willmore surfaces.* Inventiones Mathematicae 174 (2008), 1–45.
- **[Survey]** E. Kuwert, R. Schätzle. *Removability of point singularities of Willmore surfaces.* Annals of Mathematics 160 (2004), 315–357.

## 10. Worked Example / Concrete Special Case

**Spherical caps over a unit circle.** Take $\Gamma = \{x^2+y^2=1, z=0\}$ and let $\Sigma_\varphi$ be a spherical cap of sphere radius $R$ meeting $\Gamma$, parametrized by the polar half-angle $\varphi\in(0,\pi)$ with $R\sin\varphi = 1$, i.e. $R = 1/\sin\varphi$. The cap is a zone of height $h = R(1-\cos\varphi)$, so

$$\operatorname{Area}(\Sigma_\varphi) = 2\pi R h = 2\pi R^2 (1-\cos\varphi).$$

The cap has constant mean curvature $H = 1/R = \sin\varphi$. With $\lambda = p = 0$,

$$\mathcal{H}_{c_0}(\Sigma_\varphi) = (H-c_0)^2\operatorname{Area} = 2\pi R^2(1-\cos\varphi)\Big(\tfrac1R - c_0\Big)^2 = 2\pi(1-\cos\varphi)\big(1 - c_0/\sin\varphi\big)^2 .$$

*Check of the Euler–Lagrange equation.* $H$ is constant so $\Delta_g H = 0$, and the residual is $2(H-c_0)(H^2+c_0H-K)$ with $K = H^2 = \sin^2\varphi$; this vanishes iff $H = c_0$ or $c_0 H = 0$. So the cap is a Helfrich critical point exactly when $\sin\varphi = c_0$ (or $c_0=0$, the classical fact that spheres are Willmore).

*Consequences.*
- **$c_0 = 0$:** $\mathcal{H}_0(\Sigma_\varphi) = 2\pi(1-\cos\varphi)$, strictly decreasing as $\varphi\downarrow 0$, with infimum $0$ attained by the flat disk ($\varphi=0$). This matches $\mathcal{W}\ge0$ with equality for planes.
- **$0 < c_0 \le 1$:** choosing $\sin\varphi = c_0$ gives $\mathcal{H}_{c_0}=0$. The BVP has an explicit zero-energy solution: the cap of radius $1/c_0$. Rescaling to a circle of radius $r$, this works iff $c_0 r \le 1$.
- **$c_0 r > 1$ (small circle, strong spontaneous curvature):** no spherical cap spanning $\Gamma$ has $H = c_0$, and $\min_\varphi 2\pi(1-\cos\varphi)(1-c_0/\sin\varphi)^2 > 0$. Here the minimizer is not a cap, and a minimizing sequence may prefer a long thin neck from $\Gamma$ up to a nearly closed sphere of radius $1/c_0$ — the neck costs Willmore energy $\to$ a positive constant while the sphere costs nothing. Whether the infimum is attained in this regime, for a general boundary curve, is precisely the open question of §1.

This one-parameter family already shows the two features that break the general theory: the energy is *not* scale-invariant (the value depends on $c_0 r$, not on $\Gamma$ alone), and there is a nontrivial zero set of $\mathcal{H}_{c_0}$ consisting of $c_0$-spheres available for bubbling.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*