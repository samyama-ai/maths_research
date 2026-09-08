---
id: 06-pdes/compressible-navier-stokes-vacuum
title: "Compressible Navier-Stokes Vacuum"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Well-Posedness of the Compressible Navier–Stokes Equations with Vacuum

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/compressible-navier-stokes-vacuum` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the barotropic (isentropic) compressible Navier–Stokes system on $\mathbb{R}^3$ or a bounded domain $\Omega \subset \mathbb{R}^3$, for density $\rho \ge 0$ and velocity $u$:

$$\partial_t \rho + \operatorname{div}(\rho u) = 0, \qquad \partial_t(\rho u) + \operatorname{div}(\rho u \otimes u) + \nabla P(\rho) = \mu \Delta u + (\mu + \lambda)\nabla \operatorname{div} u.$$

**The problem.** Given initial data $(\rho_0, u_0)$ with $\rho_0 \ge 0$ allowed to vanish on a set of positive measure (*vacuum*), decide whether:

1. **(Regularity)** Smooth solutions with vacuum exist globally in time, or whether finite-time singularity formation is generic; and
2. **(Weak–strong / uniqueness)** whether the Lions–Feireisl finite-energy weak solutions, which do exist globally, are unique and coincide with the strong solution while the latter exists.

A complete resolution means either a global-in-time existence theorem for classical solutions with general large data containing vacuum, or an explicit example of finite-time blow-up of a classical solution from smooth, finite-energy, vacuum-containing data — together with a uniqueness theory for the weak class in dimension $3$.

The problem is **partially solved**: global weak solutions exist for $\gamma > 3/2$ (Lions–Feireisl); global classical solutions exist for small-energy large-oscillation data with vacuum (Huang–Li–Xin); and finite-time blow-up is proved for classical solutions with *compactly supported* density (Xin). The general large-data smooth-with-vacuum case is open.

## 2. Mathematical Foundations

**Pressure law.** $P(\rho) = A\rho^\gamma$, $A>0$, $\gamma > 1$ (isentropic); $\gamma = 1$ is the isothermal case. Viscosities satisfy the physical (Lamé) condition
$$\mu > 0, \qquad \lambda + \tfrac{2}{3}\mu \ge 0 .$$

**Energy law.** Smooth solutions satisfy
$$\frac{d}{dt}\int \Big( \tfrac12 \rho|u|^2 + \frac{A}{\gamma-1}\rho^\gamma \Big)\,dx + \int \big( \mu|\nabla u|^2 + (\mu+\lambda)(\operatorname{div}u)^2 \big)\,dx = 0 .$$
The natural energy space is $\rho \in L^\infty_t L^\gamma_x$, $\sqrt{\rho}\,u \in L^\infty_t L^2_x$, $\nabla u \in L^2_{t,x}$. On vacuum $\{\rho = 0\}$ the momentum equation degenerates: it gives no information about $u$, so $u$ is not determined pointwise and the system loses its parabolic-hyperbolic structure.

**Effective viscous flux.** Set
$$F := (2\mu + \lambda)\operatorname{div} u - P(\rho) + \bar P, \qquad \omega := \nabla \times u .$$
Then $\Delta F = \operatorname{div}(\rho \dot u)$ and $\mu \Delta \omega = \nabla \times (\rho \dot u)$, where $\dot u = \partial_t u + u\cdot\nabla u$ is the material derivative. $F$ is the central object: it is more regular than $\operatorname{div} u$ and drives both the Lions compactness theory and the Hoff theory of discontinuous solutions.

**Weak continuity of the pressure (Lions).** For $\gamma$ large enough, the quantity
$$\int \big( P(\rho)\,\rho - (2\mu+\lambda)\rho\operatorname{div}u \big)\,dx$$
is weakly sequentially continuous along solution sequences. Combined with the renormalized-continuity theory of DiPerna–Lions, this yields $\overline{\rho \log \rho} = \rho\log\rho$ and hence strong convergence $\rho_n \to \rho$ in $L^1$.

**Physical vacuum.** At a free boundary $\Gamma(t) = \partial\{\rho > 0\}$, the *physical vacuum* condition is
$$0 < \big| \nabla \big( c^2 \big) \big| < \infty \quad \text{on } \Gamma(t), \qquad c^2 = \frac{\partial P}{\partial \rho} = A\gamma \rho^{\gamma-1},$$
i.e. $\rho \sim \mathrm{dist}(x,\Gamma)^{1/(\gamma-1)}$. This makes the linearized operator degenerate-hyperbolic of Keldysh type; standard energy methods fail and weighted (Lagrangian) spaces are required.

**Degenerate viscosity.** For shallow-water-type models $\mu(\rho) = \rho^\alpha$, $\lambda(\rho)$ chosen so the Bresch–Desjardins (BD) relation $\lambda(\rho) = 2(\rho\mu'(\rho) - \mu(\rho))$ holds, one gains the *BD entropy*
$$\frac{d}{dt}\int \Big( \tfrac12 \rho\,|u + \nabla\varphi(\rho)|^2 + \frac{A}{\gamma-1}\rho^\gamma\Big) dx + A\gamma\!\int \rho^{\gamma-2}\mu'(\rho)|\nabla\rho|^2 dx + \dots = 0, \quad \varphi'(\rho) = \mu'(\rho)/\rho,$$
giving $\nabla \sqrt{\rho}\in L^\infty_t L^2_x$ — extra density regularity unavailable in the constant-viscosity case.

## 3. History & State of the Art (SOTA)

- **1968–1980.** Nash and Serrin establish local well-posedness away from vacuum; Kanel and Kazhikhov–Shelukhin prove global existence in 1D for data bounded away from vacuum.
- **1980.** Matsumura and Nishida prove global existence of small perturbations of a constant state $\bar\rho > 0$ in $H^3$ — no vacuum.
- **1993–1998.** Lions constructs global finite-energy weak solutions for $\gamma \ge 9/5$ in 3D, allowing vacuum, via the effective viscous flux and renormalized continuity.
- **1995.** Vaigant–Kazhikhov obtain global strong solutions in 2D for large data with density-dependent bulk viscosity $\lambda(\rho) = \rho^\beta$, $\beta > 3$.
- **1995.** Hoff builds global solutions with discontinuous data in multiple dimensions, exploiting $F$ and $\omega$.
- **1998.** Xin proves finite-time blow-up of any smooth solution on $\mathbb{R}^n$ whose initial density is compactly supported (with finite total energy and appropriate decay) — a genuine obstruction to global smoothness with vacuum.
- **2001.** Feireisl–Novotný–Petzeltová extend the weak theory to $\gamma > 3/2$ (the current threshold in 3D).
- **2004.** Cho–Choe–Kim prove local existence of strong solutions with vacuum under the *compatibility condition* $-\mu\Delta u_0 - (\mu+\lambda)\nabla\operatorname{div}u_0 + \nabla P(\rho_0) = \sqrt{\rho_0}\,g$ for some $g \in L^2$.
- **2012.** Huang–Li–Xin: global classical solutions in 3D for *small energy but possibly large oscillations*, with vacuum states permitted, including compactly supported density.
- **2016.** Vasseur–Yu prove global weak solutions for 3D degenerate viscosity $\mu(\rho)=\rho$; Li–Xin (2015) obtain the general $\rho^\alpha$ case.
- **2019–2022.** Li–Xin extend global classical existence to 2D and to a wide class of 3D data; Merle–Raphaël–Rodnianski–Szeftel construct imploding self-similar compressible solutions.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| 3D, $\gamma > 3/2$, large data, vacuum allowed | Global finite-energy weak solutions exist (uniqueness open) | Feireisl–Novotný–Petzeltová 2001 |
| 3D, $\gamma \ge 9/5$ | Original Lions construction | Lions 1998 |
| 3D, small initial energy $E_0 \le \varepsilon(\mu,\lambda,\gamma,\bar\rho)$, $\|\rho_0\|_\infty$ arbitrary | Global classical solution with vacuum; $\|\rho\|_\infty$ bounded uniformly in $t$; $\|\nabla u\|_{L^2} \to 0$ | Huang–Li–Xin 2012 |
| 2D, Cauchy problem, general large data, $\rho_0 \ge 0$ compactly supported or decaying | Global classical solutions for $\gamma>1$ | Li–Xin, *Ann. PDE* 2019 |
| 2D, $\lambda(\rho)=\rho^\beta$, $\beta>3$ (later relaxed to $\beta>4/3$) | Global strong solutions, arbitrary data | Vaigant–Kazhikhov 1995; Huang–Li 2016 |
| 1D, $\mu$ constant, free boundary with vacuum | Global well-posedness, interface regularity | Luo–Xin–Yang 2000 |
| Degenerate $\mu(\rho)=\rho^\alpha$, $1/2<\alpha<1$ (Li–Xin), $\alpha = 1$ (Vasseur–Yu) | Global weak solutions in 3D with vacuum | Li–Xin 2015; Vasseur–Yu 2016 |
| Compactly supported $\rho_0$, classical solution, $\mathbb{R}^n$ | **Blow-up in finite time** | Xin 1998; Xin–Yan 2013 |
| Finite-energy classical solutions on $\mathbb{R}^3$ with $\rho_0$ decaying | Non-existence for a broad class | Li–Wang–Xin, *ARMA* 2019 |
| Physical vacuum free boundary, 1D and 3D symmetric | Local well-posedness in weighted spaces | Coutand–Shkoller 2012; Jang–Masmoudi 2015 (Euler); Zeng, Luo–Zeng (NS) |

## 5. Principal Obstacles

- **Loss of ellipticity at vacuum.** Where $\rho = 0$ the momentum equation carries no time derivative of $u$; the standard parabolic smoothing $u \in L^2_t H^2$ cannot be closed because the coefficient of $\dot u$ vanishes. Energy estimates measure only $\sqrt{\rho}\,\dot u$, so no control of $u$ on the vacuum set is available.
- **No maximum principle for the density.** $\rho$ satisfies $D_t \rho = -\rho\operatorname{div}u$, so $\rho$ stays bounded only if $\int_0^T \|\operatorname{div}u\|_\infty dt < \infty$; $\operatorname{div} u$ is at best in $L^2_t \mathrm{BMO}$, and the logarithmic gap is exactly the Beale–Kato–Majda-type criterion (Sun–Wang–Zhang: blow-up iff $\|\rho\|_{L^\infty}$ blows up).
- **Failure of the Lions flux argument for $\gamma \le 3/2$.** Strong convergence of $\rho_n$ needs $P(\rho) \in L^p$ with $p>1$; the a priori integrability $\rho \in L^{\gamma + 2\gamma/n}$ falls to $L^1$ near $\gamma = 3/2$ in 3D, so oscillations in the pressure cannot be excluded. The physically important monatomic case $\gamma = 5/3$ is inside the range, but $\gamma = 1$ (isothermal) is not.
- **Uniqueness of weak solutions.** No weak–strong uniqueness with vacuum in full generality; convex-integration constructions (De Lellis–Székelyhidi type, adapted by Chiodaroli, Feireisl, Kreml) produce infinitely many bounded-energy weak solutions for the compressible Euler and Navier–Stokes–Fourier systems, showing the weak class is too large.
- **Blow-up vs. small data.** Xin's blow-up result and Huang–Li–Xin's global existence are compatible only because the latter's smallness is on $E_0$; nobody knows the true threshold, and no mechanism (vorticity-type, self-similar, or otherwise) has been identified for singularity formation from generic large vacuum data.
- **Degenerate viscosity.** With $\mu(\rho)=\rho^\alpha$ the BD entropy gives $\nabla\sqrt{\rho}\in L^2$ but the momentum flux $\rho^\alpha \nabla u$ is not controlled where $\rho \to 0$; compactness of $\sqrt{\rho}u$ requires delicate renormalization (Vasseur–Yu's truncation of the momentum).

## 6. The Gap

The proven statements are: (a) weak solutions exist globally for $\gamma>3/2$ but may be non-unique; (b) classical solutions exist globally when $E_0$ is small; (c) classical solutions blow up when $\rho_0$ is compactly supported *and* the solution is required to be classical with finite energy on all of $\mathbb{R}^n$.

The gap is the **large-data, non-compactly-supported, vacuum-containing regime in 3D**. Concretely, the missing step is a bound
$$\int_0^T \|\operatorname{div}u(t)\|_{L^\infty}\,dt \le C(T, E_0, \|\rho_0\|_{L^\infty})$$
that does *not* require $E_0$ small. All known routes to it use the effective flux $F$ and Zlotnik-type ODE arguments whose constants degenerate as $E_0$ grows, because the nonlinear term $\int \rho |\dot u|^2$ can only be absorbed under a smallness condition. On the weak side, the gap is a selection principle (entropy/admissibility criterion) strong enough to defeat convex integration.

## 7. Current Research (as of June 2026)

- **Li–Xin school (CUHK / Chinese Academy of Sciences).** Extending the 2D large-data global classical theory to 3D axisymmetric and to $\gamma$ near $1$; sharpening the non-existence results of Li–Wang–Xin for finite-energy classical solutions on $\mathbb{R}^3$.
- **Bresch–Vasseur–Yu (Grenoble / UT Austin).** *Entropy-weak solutions* for general nonlinear density-dependent viscosities, published in *JEMS* 2022; ongoing work on the $\kappa$-entropy and its use for the constant-viscosity limit. *(frontier — verify: whether the BD framework can be perturbed to $\mu(\rho) \to \text{const}$.)*
- **Free-boundary/physical-vacuum groups (Luo, Zeng, Jang, Coutand–Shkoller).** Global-in-time expanding solutions and stability of self-similar expanding profiles for degenerate viscosity; sharp regularity of the vacuum interface.
- **Self-similar implosion.** Merle–Raphaël–Rodnianski–Szeftel's imploding solutions for compressible Euler and Navier–Stokes (2022) supply a singularity mechanism at $\rho \to \infty$; adapting it to a *vacuum* singularity is actively pursued. *(frontier — verify.)*
- **Non-uniqueness by convex integration.** Chiodaroli–Feireisl–Kreml and successors continue to enlarge the class of non-unique weak solutions; whether vacuum is essential to those constructions is an open thread. *(frontier — verify.)*
- **Numerical/structure-preserving.** Well-balanced and asymptotic-preserving schemes that keep $\rho \ge 0$ exactly are used to probe candidate blow-up scenarios; no computational evidence of large-data smooth blow-up with vacuum has been reported.

## 8. Future Work

- Prove or disprove a **blow-up criterion in terms of $\rho$ alone** for general data: currently Sun–Wang–Zhang give $\lim_{t\to T^*}\|\rho\|_{L^\infty} = \infty$ as the only obstruction when $\lambda < 7\mu$; removing that restriction is a concrete target.
- Lower the Lions–Feireisl threshold below $\gamma = 3/2$, ideally to $\gamma > 1$, by finding a substitute for the pressure integrability gain.
- Establish **weak–strong uniqueness with vacuum** in 3D, or exhibit a genuinely non-unique pair with vacuum initial data.
- Interpolate between degenerate ($\mu = \rho^\alpha$) and constant viscosity: quantify the BD entropy's degeneration as $\alpha \to 0$.
- Settle whether the physical-vacuum interface for compressible Navier–Stokes remains regular globally in 1D radial/3D symmetric settings, or develops a cusp.

## 9. Key References

- **[Foundational]** P.-L. Lions. *Mathematical Topics in Fluid Mechanics, Volume 2: Compressible Models.* Oxford Lecture Series in Mathematics and its Applications, Oxford University Press, 1998.
- **[Foundational]** E. Feireisl, A. Novotný, H. Petzeltová. *On the existence of globally defined weak solutions to the Navier–Stokes equations.* Journal of Mathematical Fluid Mechanics, 3(4):358–392, 2001. [DOI](https://doi.org/10.1007/pl00000976)
- **[Foundational]** Z. Xin. *Blowup of smooth solutions to the compressible Navier–Stokes system with compact density.* Communications on Pure and Applied Mathematics, 51(3):229–240, 1998. [DOI](https://doi.org/10.1002/(sici)1097-0312(199803)51:3<229::aid-cpa1>3.0.co;2-c)
- **[Foundational]** V. A. Vaigant, A. V. Kazhikhov. *On the existence of global solutions to two-dimensional Navier–Stokes equations of a compressible viscous fluid.* Siberian Mathematical Journal, 36(6):1108–1141, 1995. [DOI](https://doi.org/10.1007/bf02106835)
- **[Foundational]** D. Hoff. *Global solutions of the Navier–Stokes equations for multidimensional compressible flow with discontinuous initial data.* Journal of Differential Equations, 120(1):215–254, 1995. [DOI](https://doi.org/10.1006/jdeq.1995.1111)
- **[Foundational]** Y. Cho, H. J. Choe, H. Kim. *Unique solvability of the initial boundary value problems for compressible viscous fluids.* Journal de Mathématiques Pures et Appliquées, 83(2):243–275, 2004. [DOI](https://doi.org/10.1016/j.matpur.2003.11.004)
- **[SOTA / Recent]** X. Huang, J. Li, Z. Xin. *Global well-posedness of classical solutions with large oscillations and vacuum to the three-dimensional isentropic compressible Navier–Stokes equations.* Communications on Pure and Applied Mathematics, 65(4):549–585, 2012. [DOI](https://doi.org/10.1002/cpa.21382)
- **[SOTA / Recent]** J. Li, Z. Xin. *Global well-posedness and large time asymptotic behavior of classical solutions to the compressible Navier–Stokes equations with vacuum.* Annals of PDE, 5:7, 2019. [DOI](https://doi.org/10.1007/s40818-019-0064-5)
- **[SOTA / Recent]** A. Vasseur, C. Yu. *Existence of global weak solutions for 3D degenerate compressible Navier–Stokes equations.* Inventiones Mathematicae, 206(3):935–974, 2016. [DOI](https://doi.org/10.1007/s00222-016-0666-4)
- **[SOTA / Recent]** D. Bresch, A. Vasseur, C. Yu. *Global existence of entropy-weak solutions to the compressible Navier–Stokes equations with non-linear density dependent viscosities.* Journal of the European Mathematical Society, 24(5):1791–1837, 2022.
- **[SOTA / Recent]** J. Li, Z. Wang, Z. Xin. *Non-existence of classical solutions with finite energy to the Cauchy problem of the compressible Navier–Stokes equations.* Archive for Rational Mechanics and Analysis, 232(2):557–590, 2019. [DOI](https://doi.org/10.1007/s00205-018-1328-z)
- **[SOTA / Recent]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On the implosion of a compressible fluid I: Smooth self-similar inviscid profiles.* Annals of Mathematics, 196(2):567–778, 2022. [DOI](https://doi.org/10.4007/annals.2022.196.2.3)
- **[Foundational]** D. Bresch, B. Desjardins. *Existence of global weak solutions for a 2D viscous shallow water equations and convergence to the quasi-geostrophic model.* Communications in Mathematical Physics, 238(1–2):211–223, 2003. [DOI](https://doi.org/10.1007/s00220-003-0859-8)
- **[Survey]** E. Feireisl. *Dynamics of Viscous Compressible Fluids.* Oxford Lecture Series in Mathematics and its Applications 26, Oxford University Press, 2004. [DOI](https://doi.org/10.1093/acprof:oso/9780198528388.001.0001)
- **[Survey]** A. Novotný, I. Straškraba. *Introduction to the Mathematical Theory of Compressible Flow.* Oxford University Press, 2004. [DOI](https://doi.org/10.1093/oso/9780198530848.001.0001)

## 10. Worked Example / Concrete Special Case

**An exact free-boundary solution with vacuum (1D, isothermal).** Take $n=1$, $P(\rho)=A\rho$ ($\gamma=1$), constant viscosity $\mu>0$, and look for a self-similarly expanding gas occupying $\Omega(t) = (-X(t), X(t))$, vacuum outside, with the stress-free boundary condition
$$\big(\mu u_x - P(\rho)\big)\Big|_{x = \pm X(t)} = 0 .$$

*Ansatz:* $u(x,t) = a(t)\,x$, $\rho(x,t) = r(t)$ for $|x| < X(t)$, with $\dot X = a X$.

**Continuity.** $\rho_t + (\rho u)_x = \dot r + r\,a = 0 \Rightarrow \dot r = -a r$.

**Momentum.** $u$ is linear so $u_{xx} = 0$; $\rho$ is constant in $x$ so $P_x = 0$. What remains is
$$\rho\,(u_t + u u_x) = r\,(\dot a\,x + a^2 x) = 0 \quad \Longrightarrow \quad \dot a + a^2 = 0 .$$

With $a(0) = a_0 > 0$ this integrates to
$$a(t) = \frac{a_0}{1 + a_0 t}, \qquad r(t) = \frac{r_0}{1+a_0 t}, \qquad X(t) = X_0 (1 + a_0 t).$$

**Boundary condition.** $\mu u_x - P = \mu a(t) - A r(t) = \dfrac{\mu a_0 - A r_0}{1+a_0 t}$. This vanishes for all $t \ge 0$ exactly when
$$\boxed{\;\mu a_0 = A r_0\;}$$
so choosing $a_0 = A r_0/\mu$ gives a **global-in-time exact classical solution** of compressible Navier–Stokes with a genuine vacuum exterior.

**What it illustrates.**
- Mass is conserved: $2 X(t)\, r(t) = 2X_0 r_0$ for all $t$.
- The density decays like $t^{-1}$ and the solution stays smooth forever — global existence with vacuum is *not* impossible; the difficulty is generic data, not vacuum per se.
- The density is discontinuous at the interface: $\rho \to r(t) > 0$ from inside, $0$ outside. So this is *not* physical vacuum ($|\nabla c^2| = \infty$ at $\Gamma$ in the distributional sense). Replacing the profile by $\rho \sim \mathrm{dist}(x,\Gamma)^{1/(\gamma-1)}$ destroys the linear-velocity ansatz and reintroduces the degenerate weighted analysis of Section 2.
- Perturbing the ansatz breaks it immediately: with $u = a(t)x + v$, the term $\rho\, v_t$ has a coefficient $r(t)\to 0$, so control of $v$ in $L^\infty$ costs a factor $1/r(t) \sim t$ — the exact mechanism by which vacuum destroys uniform estimates.
- Xin's theorem does not contradict this: his blow-up hypothesis requires the density to be compactly supported *in the whole space with the solution classical on $\mathbb{R}$* (so $u$ defined and smooth on the vacuum region too), whereas here the problem is posed as a free-boundary problem on $\Omega(t)$ only.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*