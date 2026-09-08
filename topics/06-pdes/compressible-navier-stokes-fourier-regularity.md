---
id: 06-pdes/compressible-navier-stokes-fourier-regularity
title: "Compressible Navier-Stokes-Fourier Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Compressible Navier-Stokes-Fourier Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/compressible-navier-stokes-fourier-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the full Navier–Stokes–Fourier (NSF) system for a viscous, compressible, heat-conducting Newtonian fluid on $\Omega \subseteq \mathbb{R}^3$ (torus $\mathbb{T}^3$, or a bounded domain with no-slip and insulated walls). Given smooth initial data $(\rho_0, u_0, \theta_0)$ with $\rho_0, \theta_0$ bounded above and bounded away from zero:

**Regularity problem.** Does the unique local classical solution extend to all $t \in [0,\infty)$, or can $\rho$, $\theta$, or $\nabla u$ become unbounded in finite time?

**Weak-solution problem.** Does the full NSF system (with Fourier's law $q = -\kappa\nabla\theta$, $\kappa$ constant, and constant viscosities) admit *global* weak solutions in 3D satisfying the energy equality, and are such solutions unique in the class where they exist?

A complete resolution requires either (i) an a priori estimate closing global regularity for a physically standard constitutive class ($p = R\rho\theta$, $\mu,\lambda,\kappa$ constant, $2\mu + 3\lambda \ge 0$), or (ii) an explicit construction of data whose solution loses regularity while $\rho$ stays bounded away from vacuum, or (iii) a global existence theory for weak solutions of the full system under Fourier's law without the artificial growth hypotheses currently needed.

The problem is *not* fully open in the crude form "can smooth data blow up": for the barotropic system, finite-time blowup from smooth data has been constructed (Merle–Raphaël–Rodnianski–Szeftel, 2022). The open content is the regularity theory away from vacuum and density concentration, and the entire weak theory for the temperature equation.

## 2. Mathematical Foundations

Unknowns: density $\rho(t,x)\ge 0$, velocity $u(t,x)\in\mathbb{R}^3$, absolute temperature $\theta(t,x) > 0$.

$$\partial_t \rho + \operatorname{div}(\rho u) = 0,$$
$$\partial_t(\rho u) + \operatorname{div}(\rho u\otimes u) + \nabla p(\rho,\theta) = \operatorname{div}\mathbb{S}(\nabla u),$$
$$\partial_t\!\big(\rho e\big) + \operatorname{div}(\rho e\, u) + \operatorname{div} q = \mathbb{S}:\nabla u - p\,\operatorname{div} u .$$

Newtonian stress and Fourier flux:
$$\mathbb{S}(\nabla u) = \mu\Big(\nabla u + \nabla^{T}u - \tfrac{2}{3}\operatorname{div}u\, \mathbb{I}\Big) + \eta\,\operatorname{div}u\,\mathbb{I},\qquad q = -\kappa\nabla\theta,$$
with $\mu>0$, $\eta\ge 0$, $\kappa>0$. For a perfect gas $p = R\rho\theta$, $e = c_v\theta$, $c_v = R/(\gamma-1)$.

**Entropy.** With $s = c_v\log\theta - R\log\rho$ the system yields
$$\partial_t(\rho s) + \operatorname{div}(\rho s u) + \operatorname{div}\!\Big(\frac{q}{\theta}\Big) = \frac{1}{\theta}\Big(\mathbb{S}:\nabla u - \frac{q\cdot\nabla\theta}{\theta}\Big) \ \ge 0 .$$
Feireisl's *weak (variational) solution* replaces the internal-energy equation by this entropy **inequality** plus the total-energy balance
$$\frac{d}{dt}\int_\Omega \Big(\tfrac12\rho|u|^2 + \rho e\Big)\,dx = 0 .$$

**Barotropic reduction.** Setting $p = a\rho^\gamma$ decouples temperature and gives the isentropic system, on which most structural progress rests.

**Effective viscous flux.** $F := (2\mu+\eta)\operatorname{div}u - (p - \bar p)$ satisfies $\Delta F = \operatorname{div}\big(\rho \dot u\big)$, $\dot u = \partial_t u + u\cdot\nabla u$. Lions' *compensated-compactness identity*
$$\lim_{n}\int \big(p(\rho_n) - (2\mu+\eta)\operatorname{div}u_n\big)\rho_n\,\varphi = \int \big(\overline{p(\rho)} - (2\mu+\eta)\operatorname{div}u\big)\rho\,\varphi$$
plus renormalized continuity (DiPerna–Lions) is the engine of the weak theory. Two-dimensional and one-dimensional analogues, Lagrangian mass coordinates in 1D, and Bresch–Desjardins entropy for $\mu = \mu(\rho)$ are the other standard structures.

**Scaling.** The barotropic system is invariant under $\rho_\lambda = \rho(\lambda^2 t,\lambda x)$, $u_\lambda = \lambda u(\lambda^2 t,\lambda x)$ only if $p$ is rescaled; the *critical* spaces of Danchin are $\dot B^{3/p}_{p,1}\times \dot B^{3/p-1}_{p,1}$, and unlike incompressible Navier–Stokes the equation is **not** scaling invariant — pressure breaks the scaling, which is why no clean supercriticality statement exists.

## 3. History & State of the Art (SOTA)

- **1959–1962.** Serrin proves uniqueness for classical compressible flows; Nash establishes local existence.
- **1968–1977.** Kanel', Kazhikhov and Shelukhin settle the 1D problem: global classical solutions for the full NSF system with $\rho_0>0$, arbitrary large data.
- **1976–1982.** Solonnikov, Valli, Matsumura–Nishida: local strong solutions in Sobolev classes; global existence for data close to a constant equilibrium $(\bar\rho, 0, \bar\theta)$ in $H^3(\mathbb{R}^3)$ with exponential/algebraic decay.
- **1993–1998.** P.-L. Lions constructs global weak solutions for the barotropic system for $\gamma \ge 9/5$ in 3D, via the effective viscous flux and renormalized transport.
- **2001.** Feireisl, Novotný and Petzeltová extend this to $\gamma > 3/2$ using oscillation defect measures.
- **2004.** Feireisl builds global variational solutions for the *full* NSF system — but only for constitutive laws with $\kappa(\theta)\sim \theta^3$ (radiation) and $\mu(\theta)$ growing, not for constant $\kappa$.
- **1995, 1998.** Hoff constructs global weak solutions with discontinuous data; Xin shows solutions with compactly supported initial density and finite entropy cannot stay smooth.
- **2012.** Huang, Li and Xin: global classical solutions of the 3D barotropic system for *small energy but possibly large oscillations*, allowing vacuum.
- **2018.** Bresch and Jabin (Annals) remove monotonicity of $p$ and handle anisotropic stress by a new commutator/compactness method.
- **2022.** Merle, Raphaël, Rodnianski and Szeftel construct smooth, finite-energy data for the *barotropic* compressible Navier–Stokes system in $d = 2,3$ whose solution implodes in finite time (self-similar, density blows up), for a discrete set of admissible $\gamma$-related exponents. This is the first genuine blowup theorem for compressible Navier–Stokes.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| **1D, full NSF, $\rho_0 \ge c > 0$** | Global unique classical solutions, arbitrary large data (Kazhikhov–Shelukhin 1977); temperature-dependent $\kappa(\theta)\sim\theta^b$, $b>0$ handled by Jenssen–Karper (2010). |
| **1D with vacuum** | Global weak solutions for $p=a\rho^\gamma$, $\gamma>1$ (Hoff, Serre); regularity degenerates at the vacuum interface. |
| **3D, small data** | Matsumura–Nishida (1980, 1983): global classical solutions for $\|(\rho_0-\bar\rho,u_0,\theta_0-\bar\theta)\|_{H^3}$ small; Danchin (2000, *Invent. Math.*) in critical Besov spaces $\dot B^{3/2}_{2,1}$; extended to $\dot B^{3/p}_{p,1}$, $p<6$, by Charve–Danchin and Chen–Miao–Zhang. |
| **3D, large oscillation** | Huang–Li–Xin (2012, *CPAM*): global classical solution when $E_0 = \int(\tfrac12\rho_0|u_0|^2 + G(\rho_0))$ is small, with $\|\rho_0\|_{L^\infty}$ arbitrary. |
| **Barotropic weak solutions** | $\gamma>3/2$ in 3D, $\gamma>1$ in 2D (Feireisl–Novotný–Petzeltová 2001); degenerate viscosity $\mu(\rho)=\rho$ (Vasseur–Yu 2016, *Invent. Math.*; Li–Xin). |
| **Symmetry classes** | Spherically/cylindrically symmetric large-data global existence away from the origin. |
| **Blowup criteria** | Sun–Wang–Zhang (2011): $\limsup_{t\to T}\|\rho\|_{L^\infty}<\infty \Rightarrow$ no blowup at $T$ (barotropic, $\eta$ range condition). Huang–Li–Xin (2011): Beale–Kato–Majda-type criterion in $\|\mathbb{D}(u)\|_{L^1_tL^\infty}$. |
| **Blowup existence** | MRRS (2022): finite-time implosion, barotropic, $d=2,3$, smooth data. Xin (1998), Xin–Yan (2013): blowup for compactly supported density. |

## 5. Principal Obstacles

- **No pointwise density control in 3D.** In 1D, Lagrangian mass coordinates give an ODE along particle paths yielding two-sided bounds on the specific volume. In 3D, the analogous relation for $\log\rho$ involves the effective viscous flux $F$, which the energy estimate only places in $L^2_tH^1_x \hookrightarrow L^2_t\mathrm{BMO}$ — logarithmically short of $L^1_tL^\infty$. This single logarithm is the gap.
- **Vacuum destroys parabolicity.** Where $\rho\to 0$ the momentum equation loses its time derivative; $\dot u$ is not controlled, uniqueness arguments fail, and Xin's theorem shows genuine loss of regularity.
- **The temperature equation has an $L^1$ source.** $\mathbb{S}:\nabla u \in L^1$ only. Fourier's law with constant $\kappa$ gives $\theta \in L^2_tH^1$, which does not control $\theta$ in $L^\infty$; DiPerna–Lions renormalization is unavailable for $\theta$ because the source is not sign-definite after subtracting $p\,\mathrm{div}\,u$. This is why Feireisl's theory must impose $\kappa \sim \theta^3$.
- **Coupling breaks compactness.** With $p = R\rho\theta$, weak convergence of $\rho_n\theta_n$ requires strong convergence of *one* factor; the effective-flux identity produces compactness for $\rho$ only when $p$ depends on $\rho$ alone.
- **No scaling symmetry.** Pressure is not scale invariant, so there is no "critical/supercritical" dichotomy to guide a small-data-to-large-data bootstrap, and MRRS's self-similar profiles are constructed for the *inviscid* Euler equation with viscosity treated perturbatively — the method does not see the non-vacuum regime at all.

## 6. The Gap

Two precise boundaries:

1. **Regularity.** Proven: no blowup if $\|\rho\|_{L^\infty_{t,x}}$ stays finite (Sun–Wang–Zhang). Needed: an a priori bound on $\|\rho\|_{L^\infty}$, equivalently on $\int_0^T \|F\|_{L^\infty}\,dt$ where $F = (2\mu+\eta)\operatorname{div}u - p$. Current estimates give $F\in L^2_tH^1$; closing the loop requires upgrading a BMO bound to $L^\infty$ or replacing it with a logarithmic Gronwall argument that the nonlinear pressure defeats. MRRS's blowup does have $\|\rho\|_{L^\infty}\to\infty$, so it is consistent with — and does not resolve — the non-vacuum conjecture.

2. **Weak theory.** Proven: global variational solutions for $\kappa(\theta)\sim\theta^3$, $\mu(\theta)\sim(1+\theta)$. Needed: the same for constant $\kappa,\mu$ and $p = R\rho\theta$. The missing step is an a priori bound placing $\theta$ in a space where $\rho\theta$ converges weakly to the right limit — no known estimate yields $\theta\in L^\infty_tL^q$ with $q$ large enough.

## 7. Current Research (as of June 2026)

- **Feireisl, Novotný and collaborators (Prague, Toulon)** continue the weak/dissipative-solution program: measure-valued and dissipative solutions, weak–strong uniqueness in the class of finite-energy weak solutions, and semiflow selection.
- **Convex integration for compressible flows.** Chiodaroli, De Lellis and Kreml (2015) proved non-uniqueness of admissible weak solutions for isentropic Euler; Feireisl and coauthors have extended ill-posedness constructions toward the viscous setting. Consensus direction: the *weak* theory for full NSF may be non-unique even if global existence holds. *(frontier — verify)*
- **Post-implosion analysis.** Extending MRRS to the full NSF system with heat conduction, and determining whether the implosion is stable, are active. Reported extensions to non-radial data and to wider exponent ranges circulate as preprints. *(frontier — verify)*
- **Critical-regularity well-posedness.** Danchin, Haspot, Xu and collaborators push hybrid Besov frameworks and low-Mach-number limits; vacuum in critical spaces remains open.
- **Degenerate viscosity.** The Bresch–Desjardins entropy line (Vasseur, Yu, Li, Xin) continues, now aimed at $\mu(\rho)=\rho^\alpha$ for $\alpha$ ranges beyond $\alpha=1$.

## 8. Future Work

- Prove or disprove: for $\rho_0 \ge c > 0$ smooth on $\mathbb{T}^3$, the classical solution is global. Xin has repeatedly identified this as the sharp formulation.
- Replace the BMO-to-$L^\infty$ gap with a logarithmically improved Gronwall estimate for $\log\rho$ along particle trajectories.
- Construct global weak solutions to full NSF with constant $\kappa$, or produce a compactness obstruction showing none exist in that class.
- Determine whether MRRS implosion profiles exist for the heat-conducting system, where $\theta$ diffusion may regularize the self-similar core.
- Adapt convex integration to produce non-unique *viscous* compressible flows, which would settle the uniqueness half negatively.

## 9. Key References

- **[Foundational]** A. V. Kazhikhov, V. V. Shelukhin. *Unique global solution with respect to time of initial-boundary value problems for one-dimensional equations of a viscous gas.* Journal of Applied Mathematics and Mechanics (PMM) 41(2), 1977. [DOI](https://doi.org/10.1016/0021-8928(77)90011-9)
- **[Foundational]** A. Matsumura, T. Nishida. *The initial value problem for the equations of motion of viscous and heat-conductive gases.* Journal of Mathematics of Kyoto University 20(1), 1980. [DOI](https://doi.org/10.1215/kjm/1250522322)
- **[Foundational]** P.-L. Lions. *Mathematical Topics in Fluid Mechanics, Vol. 2: Compressible Models.* Oxford University Press, 1998.
- **[Foundational]** E. Feireisl, A. Novotný, H. Petzeltová. *On the existence of globally defined weak solutions to the Navier–Stokes equations.* Journal of Mathematical Fluid Mechanics 3, 2001. [DOI](https://doi.org/10.1007/pl00000976)
- **[Foundational]** Z. Xin. *Blowup of smooth solutions to the compressible Navier–Stokes equation with compact density.* Communications on Pure and Applied Mathematics 51, 1998. [DOI](https://doi.org/10.1002/(sici)1097-0312(199803)51:3<229::aid-cpa1>3.0.co;2-c)
- **[Foundational]** R. Danchin. *Global existence in critical spaces for compressible Navier–Stokes equations.* Inventiones Mathematicae 141, 2000. [DOI](https://doi.org/10.1007/s002220000078)
- **[SOTA / Recent]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On the implosion of a compressible fluid II: singularity formation.* Annals of Mathematics 196(2), 2022. [DOI](https://doi.org/10.4007/annals.2022.196.2.4)
- **[SOTA / Recent]** D. Bresch, P.-E. Jabin. *Global existence of weak solutions for compressible Navier–Stokes equations: thermodynamically unstable pressure and anisotropic viscous stress tensor.* Annals of Mathematics 188(2), 2018. [DOI](https://doi.org/10.4007/annals.2018.188.2.4)
- **[SOTA / Recent]** A. Vasseur, C. Yu. *Existence of global weak solutions for 3D degenerate compressible Navier–Stokes equations.* Inventiones Mathematicae 206, 2016. [DOI](https://doi.org/10.1007/s00222-016-0666-4)
- **[SOTA / Recent]** X. Huang, J. Li, Z. Xin. *Global well-posedness of classical solutions with large oscillations and vacuum to the three-dimensional isentropic compressible Navier–Stokes equations.* Communications on Pure and Applied Mathematics 65, 2012. [DOI](https://doi.org/10.1002/cpa.21382)
- **[Survey]** E. Feireisl, A. Novotný. *Singular Limits in Thermodynamics of Viscous Fluids.* Birkhäuser, 2nd ed., 2017.
- **[Survey]** A. Novotný, I. Straškraba. *Introduction to the Mathematical Theory of Compressible Flow.* Oxford University Press, 2004. [DOI](https://doi.org/10.1093/oso/9780198530848.001.0001)

## 10. Worked Example / Concrete Special Case

**Why 1D closes and 3D does not.** Take the 1D barotropic system in Lagrangian mass coordinate $y$, with specific volume $v = 1/\rho$, isothermal pressure $p = R/v$:
$$v_t = u_y,\qquad u_t + \Big(\frac{R}{v}\Big)_y = \mu\Big(\frac{u_y}{v}\Big)_y .$$

Since $v_t = u_y$, we have $u_y/v = v_t/v = (\log v)_t$. Substituting,
$$u_t + \Big(\frac{R}{v}\Big)_y = \mu\,(\log v)_{ty}.$$
Integrate in $y$ from $0$ to $y$ and set $Y(y,t) := \int_0^y u(z,t)\,dz$:
$$\mu\,(\log v)_t = \frac{R}{v} + Y_t + c(t).$$
Integrating in $t$ and exponentiating gives Kazhikhov's representation
$$v(y,t) = D(y,t)\Big[v_0(y) + \frac{R}{\mu}\int_0^t D(y,s)^{-1}\,ds\Big],\qquad D = \exp\Big(\frac{Y(y,t)-Y(y,0)}{\mu} + \tfrac1\mu\!\int_0^t c\Big).$$

The basic energy estimate gives $\|u(t)\|_{L^2}^2 \le E_0$, hence by Cauchy–Schwarz $|Y(y,t)| \le \sqrt{|\Omega|\,E_0}$ uniformly. Therefore $D$ and $D^{-1}$ are bounded by explicit constants $e^{\pm C(E_0)/\mu}$, and the bracket is bounded below by $\min v_0 > 0$ and above by $\max v_0 + (R/\mu)T e^{C/\mu}$. Conclusion:
$$0 < c(T,E_0,\mu) \le v(y,t) \le C(T,E_0,\mu) \quad\Longleftrightarrow\quad 0 < \underline{\rho} \le \rho \le \overline{\rho}.$$
No vacuum, no concentration; higher regularity then bootstraps and the solution is global.

**The 3D failure.** The same computation in 3D produces, along particle paths $\dot X = u$,
$$(2\mu+\eta)\,\frac{D}{Dt}\log\rho = -\,p(\rho) + F,\qquad F = (2\mu+\eta)\operatorname{div}u - p,$$
so that
$$\log\rho(X(t),t) = \log\rho_0 + \frac{1}{2\mu+\eta}\int_0^t \big(F - p\big)\,ds .$$
The pressure term has a good sign (it damps growth). But $F$ solves $\Delta F = \operatorname{div}(\rho\dot u)$, and the only universal bound available is $\|\nabla F\|_{L^2_{t,x}} \lesssim \|\sqrt{\rho}\,\dot u\|_{L^2_{t,x}} \lesssim E_0$. In three dimensions $H^1 \not\hookrightarrow L^\infty$: $F$ lies in BMO, and $\int_0^T\|F\|_{L^\infty}dt$ can only be bounded by $\int_0^T \|F\|_{BMO}\log(e + \|\rho\|_{L^\infty})\,dt$. The resulting Gronwall inequality is
$$\log\overline{\rho}(t) \lesssim 1 + \int_0^t \|F\|_{BMO}\,\log\big(e+\overline{\rho}(s)\big)\,ds,$$
which is *doubly exponential* and does not close without an extra smallness assumption — precisely the assumption Huang–Li–Xin impose ($E_0$ small). Closing this logarithm for arbitrary $E_0$, with $\rho_0$ bounded away from zero, is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*