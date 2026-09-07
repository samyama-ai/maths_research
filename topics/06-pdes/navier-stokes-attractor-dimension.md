---
id: 06-pdes/navier-stokes-attractor-dimension
title: "Navier Stokes Attractor Dimension"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Navier–Stokes Attractor Dimension

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/navier-stokes-attractor-dimension` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For the 2D incompressible Navier–Stokes equations with time-independent forcing on a bounded domain or torus, the semigroup has a compact global attractor $\mathcal{A}$ of finite fractal dimension. The problem is to determine the **sharp growth rate of $\dim \mathcal{A}$ as the forcing amplitude (Grashof number $G$) tends to infinity**, and to match it against the physical count of turbulent degrees of freedom.

Three concrete questions:

1. **(Log correction.)** Is the Constantin–Foias–Temam bound $d_F(\mathcal{A}) \le c\,G^{2/3}(1+\log G)^{1/3}$ sharp, or does the logarithm come off, giving $d_F(\mathcal{A}) \asymp G^{2/3}$ for the periodic case?
2. **(Boundary case.)** Under no-slip (Dirichlet) boundary conditions the best upper bound is $c\,G$ while the best lower bound is $c\,G^{2/3}$. Which exponent is correct?
3. **(3D.)** Does the 3D system possess a finite-dimensional global attractor at all, and does its dimension obey the Landau–Lifshitz count $\sim Re^{9/4}$?

A complete resolution of (1) or (2) requires either a construction of forces realising the upper exponent, or an improved trace estimate. Resolution of (3) is at least as hard as the 3D global regularity problem.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^n$ ($n=2,3$) be $\mathbb{T}^n = [0,L]^n$ or a bounded domain. Consider

$$\partial_t u + (u\cdot\nabla)u - \nu \Delta u + \nabla p = f, \qquad \nabla\cdot u = 0, \qquad u(0)=u_0 .$$

Set $H = \{u \in L^2(\Omega)^n : \nabla\cdot u=0,\ u\cdot n|_{\partial\Omega}=0\}$ (mean-zero in the periodic case), $V = H \cap H^1_0$, $P$ the Leray projector, $A = -P\Delta$ the Stokes operator with eigenvalues $0<\lambda_1\le\lambda_2\le\cdots$, and $B(u,v)=P(u\cdot\nabla v)$. The functional form is

$$\frac{du}{dt} + \nu A u + B(u,u) = Pf .$$

**Grashof number.** With $\kappa_0 = \lambda_1^{1/2}$,
$$G = \frac{\|Pf\|_{L^2}}{\nu^2 \kappa_0^{2}} \quad (n=2), \qquad G = \frac{\|Pf\|_{L^2}}{\nu^2 \kappa_0^{3/2}} \quad (n=3).$$

**Global attractor.** For $n=2$ the solution semigroup $S(t)$ on $H$ is well defined and possesses a unique compact invariant set $\mathcal{A}=\bigcap_{t\ge0}\overline{\bigcup_{s\ge t}S(s)\mathcal{B}}$ attracting all bounded sets. Its Hausdorff and fractal dimensions satisfy $d_H(\mathcal{A})\le d_F(\mathcal{A})$.

**Dimension mechanism (Constantin–Foias–Temam).** Linearise: $\partial_t U = -\nu A U - B(u,U)-B(U,u) =: \mathcal{L}(u)U$. Let
$$q_m = \limsup_{T\to\infty}\ \sup_{u_0\in\mathcal{A}}\ \frac1T\int_0^T \operatorname{Tr}\big(\mathcal{L}(u(s))\circ Q_m(s)\big)\,ds,$$
with $Q_m$ the orthogonal projection onto the first $m$ directions of the linearised flow. If $q_m<0$ then $d_H(\mathcal{A})<m$, and the Kaplan–Yorke-type interpolation of Constantin–Foias–Temam bounds $d_F$ by the same $m$.

For an orthonormal family $\{\varphi_j\}_{j\le m}\subset V$ with $\rho=\sum_j|\varphi_j|^2$, the **Lieb–Thirring inequality for orthonormal systems** gives, in 2D,
$$\int_\Omega \rho^2\,dx \ \le\ c_{LT}\sum_{j=1}^m \|\nabla\varphi_j\|_{L^2}^2 ,$$
which converts $\operatorname{Tr}(\mathcal{L}Q_m) \le -\nu\sum_j\|\nabla\varphi_j\|^2 + \int \rho\,|\nabla u|$ into a closed inequality. Combining with the enstrophy balance $\nu\langle \|\Delta u\|^2\rangle \le \|f\|\,\langle\|\nabla u\|^2\rangle^{1/2}$ on $\mathcal{A}$ yields the $G^{2/3}$ scale.

**Kraichnan length.** With $\eta$ the mean enstrophy dissipation rate, $\ell_d = (\nu^3/\eta)^{1/6}$; the physical prediction is $\dim\mathcal{A}\asymp (L/\ell_d)^2$.

## 3. History & State of the Art (SOTA)

- **1967** — Foias and Prodi prove that 2D Navier–Stokes flows are determined by finitely many Fourier modes: the first quantitative statement that turbulence is finite-dimensional.
- **1985** — Constantin and Foias (*CPAM* 38) introduce global Lyapunov exponents and the Kaplan–Yorke formula for the 2D attractor; Constantin–Foias–Temam (*Memoirs AMS* 314) give $d_H(\mathcal{A}) \le c\,G$ and, on the torus, $c\,G^{2/3}(1+\log G)^{1/3}$.
- **1988** — Constantin–Foias–Temam (*Physica D* 30) recast the bound as $d \le c\,(L/\ell_d)^2(1+\log(L/\ell_d))^{1/3}$, matching Kraichnan's count up to the logarithm. Ghidaglia–Marion–Temam supply the Lieb–Thirring constants used.
- **1993** — V. X. Liu (*CMP* 158) constructs forces on $\mathbb{T}^2$ with $d_H(\mathcal{A}) \ge c\,G^{2/3}$, closing the exponent gap in the periodic case.
- **1997** — Ziane (*Physica D* 105) obtains bounds optimal in the domain aspect ratio for elongated and thin domains.
- **2000s** — Chepyzhov–Vishik develop trajectory attractors for the 3D system, where uniqueness fails; Cheskidov–Foias analyse the 3D weak global attractor.
- **2010s–2020s** — Ilyin, Laptev, Loss and Zelik sharpen the Lieb–Thirring constants, producing explicit (not merely $O(1)$) constants in the $G^{2/3}$ bound, and transfer the machinery to damped Euler–Bardina regularisations in 2D and 3D, where matching upper and lower bounds are available.

## 4. Partial Results / Verified Cases

| Setting | Upper bound | Lower bound | Status |
|---|---|---|---|
| $\mathbb{T}^2$, general $f\in H$ | $c\,G^{2/3}(1+\log G)^{1/3}$ (CFT 1988) | $c\,G^{2/3}$ (Liu 1993) | exponent matched; log open |
| Bounded $\Omega\subset\mathbb{R}^2$, no-slip | $c\,G$ (Temam 1988) | $c\,G^{2/3}$ | exponent **open** |
| $\mathbb{T}^2$, free/stress-free, elongated $L_1\gg L_2$ | aspect-ratio-optimal $c\,G$-type (Ziane 1997) | matching family | solved in aspect ratio |
| 2D sphere $\mathbb{S}^2$ | $c\,G$; $c\,G^{2/3}$ for special forces (Ilyin) | $c\,G^{2/3}$ | partially matched |
| 2D damped Euler–Bardina | $c\,\alpha^{-1}$-type sharp | matching | **solved** (Ilyin–Zelik) |
| 3D damped Euler–Bardina | sharp two-sided (Ilyin–Kostianko–Zelik 2022) | matching | **solved** |
| 3D Navier–Stokes | conditional on regularity only | none | **open** |
| Determining modes/nodes, 2D | $c\,G$ (Jones–Titi 1993) | — | best known |

Also verified: for $G$ below the first bifurcation threshold, $\mathcal{A}$ is a single stationary point and $\dim\mathcal{A}=0$; for the Kolmogorov flow this holds up to the Meshalkin–Sinai Reynolds threshold.

## 5. Principal Obstacles

- **Trace estimates are one-sided.** The Lieb–Thirring route bounds $\operatorname{Tr}(\mathcal{L}Q_m)$ using only the enstrophy $\langle\|\nabla u\|^2\rangle$ on $\mathcal{A}$. Any information about the *geometry* of $\mathcal{A}$ — which directions are actually expanding — is discarded. Recovering the missing $(1+\log G)^{1/3}$ requires a trace estimate sensitive to the spatial intermittency of $|\nabla u|$, which no current inequality supplies.
- **Boundary layers.** Under no-slip conditions the enstrophy balance $\nu\|\Delta u\|^2 \le \|f\|\|\nabla u\|$ fails: the pressure term $\int (\nabla p)\cdot \Delta u$ does not vanish on $\partial\Omega$, and the resulting boundary integral scales like $\nu^{-1}$, costing a full power of $G$. This is precisely the $G$ versus $G^{2/3}$ gap.
- **Lower bounds are local.** Every known lower bound counts unstable eigenvalues of the linearisation about an *explicit* stationary solution (Kolmogorov flow, shear flows). Since a laminar solution of amplitude $\lambda$ has an unstable subspace of dimension controlled by $\lambda/\nu$ and by the forcing wavenumber, the construction is a spectral count, not a description of the attractor. There is no technique to bound $\dim\mathcal{A}$ from below by a genuinely turbulent, non-stationary object.
- **3D non-uniqueness.** Without global well-posedness there is no semigroup, so the standard volume-contraction argument has no phase space to act on. Trajectory and weak attractors exist but the Lyapunov exponent apparatus does not apply to them.

## 6. The Gap

- **Periodic 2D:** proven $c_1 G^{2/3} \le d_F(\mathcal{A}) \le c_2 G^{2/3}(1+\log G)^{1/3}$. Open step: either an example family with $d_F \gtrsim G^{2/3}(\log G)^{1/3}$, or a trace inequality that removes the logarithm. The logarithm enters through an interpolation $\|\nabla u\|_{L^\infty}\lesssim \|\Delta u\|(1+\log(\cdot))^{1/2}$ used to control $\int\rho|\nabla u|$; removing it means bounding this term without a Brezis–Gallouët-type loss.
- **No-slip 2D:** the missing step is an enstrophy-type balance on the attractor valid up to the boundary, or a boundary-adapted Lieb–Thirring inequality whose constant does not degenerate as $\nu\to0$.
- **3D:** the gap coincides with the Clay Millennium problem — no finite-dimensional attractor is available until uniqueness of Leray–Hopf solutions is settled.

## 7. Current Research (as of June 2026)

- **Sharp-constant programme (Ilyin, Kostianko, Zelik; Laptev).** Explicit constants in the Lieb–Thirring inequalities for orthonormal families with magnetic and rotational terms, pushed into attractor bounds for Navier–Stokes on the torus and the sphere and for Euler–Bardina regularisations. The 3D Bardina results give matching two-sided bounds and serve as a proxy for what the true 3D answer might look like. *(frontier — verify)*
- **Alpha-models and interpolation.** Navier–Stokes-$\alpha$, Leray-$\alpha$ and Bardina models admit attractors whose dimension is computed sharply; a live question is whether these bounds converge to the Navier–Stokes value as $\alpha\to0$. *(frontier — verify)*
- **Determining modes/nodes.** Refinements of Jones–Titi towards a $G^{2/3}$ count of determining modes, which would align the data-assimilation picture with the attractor dimension.
- **Stochastic forcing.** Random attractors for 2D stochastic Navier–Stokes: dimension bounds in terms of the noise covariance trace, and lower bounds from unstable manifolds of random fixed points.
- **Groups.** Keldysh Institute / HSE Moscow (Ilyin, Zelik, Chepyzhov), Lancaster/Surrey (Kostianko, Zelik), Texas A&M and Weizmann (Titi and collaborators), Indiana (Temam school), Chicago/UIC (Cheskidov).

## 8. Future Work

- Construct a forcing family on $\mathbb{T}^2$ realising a logarithmic correction, or prove a $\log$-free trace estimate using the Bernstein-type localisation of $\rho$.
- Develop a Lieb–Thirring inequality adapted to Dirichlet boundary layers, with a constant uniform in $\nu$, to settle the no-slip exponent.
- Move beyond stationary-solution spectral counts for lower bounds: bound $\dim\mathcal{A}$ below via the entropy of an invariant measure or via a horseshoe construction near a heteroclinic cycle.
- Compute attractor dimension numerically for Kolmogorov flow at $G$ spanning several decades and fit the exponent; existing computations of Lyapunov spectra are limited to modest $G$.
- Transfer the sharp 3D Bardina bounds to the hyperviscous 3D Navier–Stokes system and track the exponent as the hyperviscosity power decreases to $1$.

## 9. Key References

- **[Foundational]** C. Foias, G. Prodi. *Sur le comportement global des solutions non-stationnaires des équations de Navier–Stokes en dimension 2.* Rend. Sem. Mat. Univ. Padova 39, 1967.
- **[Foundational]** P. Constantin, C. Foias. *Global Lyapunov exponents, Kaplan–Yorke formulas and the dimension of the attractors for 2D Navier–Stokes equations.* Comm. Pure Appl. Math. 38, 1985.
- **[Foundational]** P. Constantin, C. Foias, R. Temam. *Attractors representing turbulent flows.* Memoirs of the American Mathematical Society 314, 1985.
- **[Foundational]** P. Constantin, C. Foias, R. Temam. *On the dimension of the attractors in two-dimensional turbulence.* Physica D 30, 1988.
- **[SOTA]** V. X. Liu. *A sharp lower bound for the Hausdorff dimension of the global attractors of the 2D Navier–Stokes equations.* Comm. Math. Phys. 158, 1993.
- **[SOTA]** M. Ziane. *Optimal bounds on the dimension of the attractor of the Navier–Stokes equations.* Physica D 105, 1997.
- **[SOTA]** D. A. Jones, E. S. Titi. *Upper bounds on the number of determining modes, nodes, and volume elements for the Navier–Stokes equations.* Indiana Univ. Math. J. 42, 1993.
- **[SOTA / Recent]** A. Ilyin, A. Kostianko, S. Zelik. *Sharp upper and lower bounds of the attractor dimension for 3D damped Euler–Bardina equations.* Physica D 432, 2022.
- **[Survey]** R. Temam. *Infinite-Dimensional Dynamical Systems in Mechanics and Physics.* 2nd ed., Springer Applied Mathematical Sciences 68, 1997.
- **[Survey]** C. Foias, O. Manley, R. Rosa, R. Temam. *Navier–Stokes Equations and Turbulence.* Cambridge University Press, 2001.
- **[Survey]** V. V. Chepyzhov, M. I. Vishik. *Attractors for Equations of Mathematical Physics.* AMS Colloquium Publications 49, 2002.
- **[Survey]** C. R. Doering, J. D. Gibbon. *Applied Analysis of the Navier–Stokes Equations.* Cambridge University Press, 1995.

## 10. Worked Example / Concrete Special Case

**Kolmogorov flow on $\mathbb{T}^2=[0,2\pi]^2$.** Take
$$f(x,y) = \nu\lambda\kappa^2\,\sin(\kappa y)\,e_1, \qquad \kappa\in\mathbb{N},\ \lambda>0 .$$

*Stationary solution.* $u^* = \lambda\sin(\kappa y)\,e_1$ solves the steady equation exactly: $(u^*\cdot\nabla)u^* = \lambda\sin(\kappa y)\partial_x u^* = 0$, and $-\nu\Delta u^* = \nu\lambda\kappa^2\sin(\kappa y)e_1 = f$, with $p\equiv0$. So $u^*\in\mathcal{A}$ for every $\lambda$.

*Grashof number.* $\kappa_0=\lambda_1^{1/2}=1$ and
$$\|f\|_{L^2}^2 = \nu^2\lambda^2\kappa^4\!\!\int_0^{2\pi}\!\!\int_0^{2\pi}\!\sin^2(\kappa y)\,dx\,dy = 2\pi^2\nu^2\lambda^2\kappa^4 ,$$
hence $\|f\|_{L^2} = \sqrt2\,\pi\,\nu\lambda\kappa^2$ and
$$G = \frac{\|f\|_{L^2}}{\nu^2\kappa_0^2} = \frac{\sqrt2\,\pi\,\lambda\kappa^2}{\nu}.$$

*Instability count.* Write the perturbation in stream-function form $\psi = e^{i\alpha x}\sum_{k\in\mathbb{Z}} c_k e^{ik\kappa y}$. The linearisation about $u^*$ couples only neighbours $k\to k\pm1$, producing a Jacobi (tridiagonal) eigenvalue problem. Meshalkin and Sinai (1961) solved it by continued fractions: the flow is linearly stable for
$$R := \frac{\lambda}{\nu\kappa} < \sqrt{2},$$
and for $R>\sqrt2$ an unstable eigenvalue exists for each integer $x$-wavenumber $\alpha$ with $0<|\alpha|<\kappa$.

*Consequences.*
- For $R<\sqrt2$ — i.e. $G < \sqrt2\pi\cdot\sqrt2\,\kappa^3 = 2\pi\kappa^3$ — the origin of the local dynamics is stable; for $\kappa=1$ one gets $\dim\mathcal{A}=0$ below $G\approx 6.28$ in this normalisation.
- For $R$ a fixed multiple of $\sqrt2$, the number of unstable $\alpha$-modes is $2(\kappa-1)$, so $\dim W^u(u^*)\ge 2\kappa-2$. With $\lambda=\sqrt2\nu\kappa$ this gives $G = 2\pi\kappa^3$ and therefore
$$\dim\mathcal{A} \ \ge\ 2\kappa-2 \ \asymp\ G^{1/3}.$$
- Liu's theorem improves this to $c\,G^{2/3}$ by taking the amplitude $\lambda/\nu$ far above threshold (so that the unstable band widens in *both* wavenumber directions) while simultaneously sending $\kappa\to\infty$, and by controlling the full Jacobi matrix rather than a single band.

The example shows both sides of the difficulty: the upper bound $c\,G^{2/3}(1+\log G)^{1/3}$ is a global energy/enstrophy statement, while every lower bound available is a finite-dimensional eigenvalue count around one explicit laminar solution. The residual $(1+\log G)^{1/3}$ lies exactly in the space between these two very different kinds of argument.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*