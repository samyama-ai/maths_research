---
id: 06-pdes/boltzmann-soft-potentials-noncutoff
title: "Global Solvability of the Boltzmann Equation Without Angular Cutoff for Soft Potentials"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Solvability of the Boltzmann Equation Without Angular Cutoff for Soft Potentials

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/boltzmann-soft-potentials-noncutoff` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the spatially inhomogeneous Boltzmann equation on $\mathbb{T}^3_x \times \mathbb{R}^3_v$ (or $\mathbb{R}^3_x \times \mathbb{R}^3_v$),

$$\partial_t f + v\cdot\nabla_x f = Q(f,f), \qquad f(0,x,v) = f_0(x,v) \ge 0,$$

with a **non-cutoff** collision kernel of inverse-power-law type: $B(|v-v_*|,\cos\theta) = |v-v_*|^{\gamma} b(\cos\theta)$, where $b(\cos\theta)\sin\theta \approx \theta^{-1-2s}$ as $\theta\to 0^+$, so that $\int_0^{\pi} b(\cos\theta)\sin^2\theta\,\theta\,d\theta<\infty$ but $\int b\,\sin\theta \,d\theta=\infty$. The **soft potential** regime is $\gamma<0$, with $\gamma > -3$ (Coulomb-like limit at $\gamma = -3$).

**Question (open).** For soft potentials, does every initial datum $f_0$ with finite mass, energy and entropy (and suitable polynomial or Gaussian decay) generate a **global-in-time, unique, smooth** solution that conserves mass, momentum and energy and converges to the Maxwellian equilibrium? Equivalently: is there no finite-time breakdown of the hydrodynamic quantities

$$\rho(t,x)=\int f\,dv,\quad E(t,x)=\int |v|^2 f\,dv,\quad H(t,x)=\int f\log f\,dv ?$$

A complete resolution requires either (i) an unconditional global existence-and-uniqueness theorem for large data in the soft-potential range $-3<\gamma<0$, $s\in(0,1)$, or (ii) a construction of a solution whose local density, energy or entropy blows up in finite time. The **very soft** sub-range $\gamma+2s<0$ — which contains all Coulomb-like interactions — is the hard core of the problem; the **moderately soft** range $\gamma+2s\ge 0$ is settled conditionally.

## 2. Mathematical Foundations

The collision operator in weak (Maxwell) form is

$$\int Q(g,f)\varphi\,dv = \int_{\mathbb{R}^3}\int_{\mathbb{R}^3}\int_{S^2} B\,g_* f\,\big(\varphi(v')-\varphi(v)\big)\,d\sigma\,dv_*\,dv,$$

with the momentum- and energy-preserving parametrization

$$v' = \frac{v+v_*}{2}+\frac{|v-v_*|}{2}\sigma,\qquad v'_*=\frac{v+v_*}{2}-\frac{|v-v_*|}{2}\sigma,\qquad \cos\theta = \tfrac{v-v_*}{|v-v_*|}\cdot\sigma .$$

For an inverse-power force $\propto r^{-(p-1)}$ in dimension $3$ one has $\gamma=\frac{p-5}{p-1}$ and $s=\frac{1}{p-1}$, so $\gamma+2s=\frac{p-3}{p-1}$; hard potentials are $p>5$, Maxwell molecules $p=5$, soft potentials $3<p<5$, and $\gamma+2s<0$ corresponds to $p<3$. Grad's angular cutoff ($b\in L^1$) is a modeling truncation with no physical basis.

**Regularization.** Without cutoff, $Q$ behaves like a velocity-fractional diffusion of order $2s$ with degenerate coefficient:

$$Q(g,f) \;\approx\; -\,C_g\,\langle v\rangle^{\gamma}\,(-\Delta_v)^{s} f \;+\; \text{lower order}, \qquad \langle v\rangle=(1+|v|^2)^{1/2},$$

and, after commuting with transport, an effective ellipticity $\langle v\rangle^{\gamma+2s}$ in the natural scaling. The Alexandre–Desvillettes–Villani–Wennberg coercivity estimate gives, for $g$ with mass bounded below and mass/energy/entropy bounded above,

$$-\int Q(g,f)\,f\,dv \;\gtrsim\; \big\|\langle v\rangle^{\gamma/2} f\big\|^2_{H^s_v} - C\big\|\langle v\rangle^{\gamma/2}f\big\|^2_{L^2_v}.$$

**Linearized theory.** Writing $f=\mu+\mu^{1/2}g$ with $\mu(v)=(2\pi)^{-3/2}e^{-|v|^2/2}$, the linearized operator $L$ satisfies the Gressman–Strain coercivity

$$\langle -Lg,g\rangle \;\gtrsim\; |g|^2_{N^{s,\gamma}},\qquad |g|^2_{N^{s,\gamma}} \simeq \big\|\langle v\rangle^{\frac{\gamma+2s}{2}}g\big\|^2_{L^2} + \iint \frac{(g(v)-g(v'))^2}{d(v,v')^{3+2s}}\,\langle v\rangle^{\gamma+2s+1}\mathbf{1}_{d\le 1}\,dv\,dv',$$

an anisotropic (Carleman/lifted-metric) fractional norm. For $\gamma+2s<0$ the weight $\langle v\rangle^{\gamma+2s}$ vanishes at infinity: **there is no spectral gap**, only degenerate dissipation.

**Scaling.** The kinetic scaling $f_r(t,x,v)=f(r^{2s}t,\;r^{1+2s}x,\;rv)$ is compatible with the local ellipticity, and the equation is *critical* for $\gamma+2s=0$: below that threshold the diffusion is subcritical relative to the drift produced by large velocities.

## 3. History & State of the Art (SOTA)

- **1963.** Grad introduces the angular cutoff to split $Q=Q_{\text{gain}}-\nu f$, enabling all early well-posedness theory; the physical singular kernel is set aside.
- **1989.** DiPerna–Lions renormalized solutions give global existence for large data (all $\gamma$), but with no uniqueness, no energy conservation, no regularity. Extended to the non-cutoff case by Alexandre–Villani (2002) as *renormalized solutions with defect measure*.
- **2000.** Alexandre–Desvillettes–Villani–Wennberg (ARMA) prove entropy-dissipation coercivity, identifying the $H^s_v$ smoothing hidden in the grazing singularity.
- **2004.** Desvillettes–Wennberg prove $C^\infty$ smoothing for the spatially homogeneous equation, moderately soft potentials.
- **2011–2012.** Two independent perturbative programs — Gressman–Strain (JAMS) and Alexandre–Morimoto–Ukai–Xu–Yang (CMP; JFA) — establish global existence, uniqueness, smoothing and exponential/polynomial relaxation for **near-Maxwellian data**, covering essentially the whole range $\gamma>-3$, $s\in(0,1)$ (Gressman–Strain under $\gamma+2s>-1$; AMUXY reaching the soft range in the whole space).
- **2016–2022.** The *conditional regularity* program (Silvestre; Imbert–Silvestre; Imbert–Mouhot–Silvestre; Golse–Imbert–Mouhot–Vasseur) imports De Giorgi–Nash–Moser and Schauder theory for kinetic integro-differential equations, reducing large-data global smoothness to a priori control of $\rho,E,H$.
- **2021.** Duan–Liu–Sakamoto–Strain (CPAM) construct global mild solutions in $L^\infty_v$-type spaces with polynomial weights; Alonso–Morimoto–Sun–Yang remove Gaussian-weight requirements.
- **2023–2024.** Guillen–Silvestre prove Villani's conjecture on monotonicity of Fisher information along Boltzmann/Landau flows, yielding the Landau–Coulomb global regularity theorem and a new a priori $L^3_v$ bound in the Boltzmann setting.

Status: **large-data global smooth solvability for soft potentials remains open**, unconditionally in every sub-range; conditionally it is closed for $\gamma+2s\ge 0$ and (frontier) for $\gamma+2s>-2$.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $\gamma>-3$, $s\in(0,1)$, near-Maxwellian data, torus | Global existence, uniqueness, $C^\infty$ smoothing, convergence to $\mu$ | Gressman–Strain 2011 ($\gamma+2s>-1$); AMUXY 2011–2012 |
| Soft potentials, whole space, Maxwellian-weighted perturbation | Global existence with time-decay $\langle t\rangle^{-\sigma}$ | AMUXY, JFA 262 (2012) |
| $-3<\gamma<0$, polynomial-weighted $L^\infty$ perturbations | Global mild solutions, no Gaussian tail assumed | Duan–Liu–Sakamoto–Strain 2021; Alonso–Morimoto–Sun–Yang 2021 |
| Moderately soft $\gamma+2s\in[0,2]$, large data | **Conditional**: if $0<m_0\le\rho\le M_0$, $E\le E_0$, $H\le H_0$ on $[0,T]$, then $f\in C^\infty$ with estimates depending only on those constants | Imbert–Silvestre, JAMS 35 (2022) |
| Very soft $\gamma+2s<0$, large data | **Conditional with extra hypothesis**: same conclusion provided additionally $\|f(t,\cdot,\cdot)\|_{L^\infty_x L^p_v}$ is bounded for some $p>\frac{3}{3+\gamma+2s}$ | Imbert–Silvestre 2022; Imbert–Mouhot–Silvestre 2020 |
| Spatially homogeneous, $\gamma\ge -2s$ | Global well-posedness and $C^\infty$ smoothing for finite mass/energy/entropy data | Desvillettes–Wennberg 2004; Alexandre–Morimoto–Ukai–Xu–Yang |
| Moderately soft, near vacuum, $\mathbb{R}^3_x$ | Nonlinear stability of vacuum, global solutions | Chaturvedi, Ann. PDE 7 (2021) |
| Landau–Coulomb (grazing limit $s\to1$, $\gamma=-3$) | Unconditional global well-posedness and smoothness | Guillen–Silvestre 2023 |

## 5. Principal Obstacles

- **No spectral gap for $\gamma+2s<0$.** The dissipation weight $\langle v\rangle^{\gamma+2s}$ decays at large $|v|$, so linearized relaxation is only polynomial or stretched-exponential. Perturbative Gronwall schemes that close on exponential damping fail; near-Maxwellian methods therefore do not extend to large data.
- **Subcritical diffusion.** Under kinetic scaling, $\gamma+2s=0$ is the critical exponent. For $\gamma+2s<0$ the fractional diffusion is weaker than the transport it must control at high velocity, so De Giorgi/Nash iteration loses its self-improving constant and cannot produce an unconditional $L^\infty$ bound from mass–energy–entropy alone.
- **Nonlocality in $v$ prevents maximum-principle barriers.** The singular kernel is genuinely nonlocal: a comparison function that dominates locally can still be beaten by the tail integral $\int (f(v')-f(v))K(v,v')\,dv'$, so pointwise barriers must be paired with sharp decay estimates for large velocities, which are themselves only conditional.
- **Missing a priori estimates.** Mass, momentum, energy and the $H$-theorem are the only known unconditional conserved/monotone quantities. They give no $L^p$ control for $p>1$, no pointwise lower bound on $\rho$, and no propagation of moments in $x$; the conditional-regularity program is bottlenecked exactly there.
- **Loss of derivatives / anisotropy.** The coercive norm $N^{s,\gamma}$ is anisotropic and non-Euclidean; commutators of $Q$ with $\langle v\rangle^k$ and with $\nabla_x$ generate terms not controlled by the same norm when $\gamma<0$, forcing weighted-space bookkeeping that degrades as $\gamma\downarrow -3$.
- **Vacuum.** If $\rho$ can touch zero, the coercivity constant in the ADVW estimate degenerates and all ellipticity is lost. Excluding vacuum for large data is itself open.

## 6. The Gap

Proven (Section 4) is a **conditional** implication:

$$\big(\rho,E,H \text{ bounded, } \rho \ge m_0>0 \text{ on } [0,T]\big) \;\Longrightarrow\; f\in C^\infty\big((0,T]\times\mathbb{T}^3\times\mathbb{R}^3\big),$$

valid for $\gamma+2s\in[0,2]$ unconditionally in the extra-integrability sense, and for $\gamma+2s<0$ only after assuming $f\in L^\infty_x L^p_v$, $p>3/(3+\gamma+2s)$.

The gap has two components:

1. **Close the hypothesis.** Show that finite initial mass/energy/entropy propagate as *bounded* $\rho, E, H$ with $\rho$ bounded below — i.e. rule out finite-time concentration or vacuum. No mechanism currently produces this.
2. **Remove the auxiliary $L^p$ assumption for $\gamma+2s<0$.** The required exponent $p>3/(3+\gamma+2s)$ blows up as $\gamma+2s\to-3$; a bound valid down to $\gamma=-3$, $s$ small, is not available from any known monotone functional.

Crossing the gap means finding a new coercive/monotone quantity — a genuinely nonlinear a priori estimate beyond the $H$-theorem — or a self-consistent bootstrap of the conditional regularity into itself.

## 7. Current Research (as of June 2026)

- **Fisher information route.** Guillen–Silvestre's proof of Villani's conjecture (monotonicity of $I(f)=\int |\nabla \sqrt{f}|^2\,dv$ along the collision flow) supplies an $H^{1/2}_v \hookrightarrow L^3_v$ bound. Since $3>3/(3+\gamma+2s)$ whenever $\gamma+2s>-2$, this closes the auxiliary $L^p$ hypothesis in Section 6(2) on that range, leaving only $-3<\gamma+2s\le-2$ *(frontier — verify the inhomogeneous, $x$-localized version)*. Groups: Chicago (Silvestre), CMAP/Paris (Imbert), Cambridge (Mouhot).
- **Kinetic De Giorgi–Nash–Moser and Schauder theory** for integro-differential equations with degenerate coefficients — Golse, Imbert, Mouhot, Vasseur, Loher — aiming at estimates uniform as $\gamma+2s\downarrow -3$.
- **Polynomial-weight perturbative theory** (Duan, Strain, Sakamoto; Alonso, Morimoto, Sun, Yang; He, Jiang) — enlarging the basin of attraction of the Maxwellian toward non-Gaussian tails, with the goal of merging with large-data conditional results.
- **Grazing-collision asymptotics.** Transferring the Landau–Coulomb theorem back to Boltzmann with $s\to 1^-$, uniformly in $s$ *(frontier — verify uniformity of constants)*.
- **Hydrodynamic limits and boundary problems** for soft potentials, where the same missing estimates obstruct rigorous Navier–Stokes limits.

## 8. Future Work

- Search for a second monotone functional beyond entropy and Fisher information — candidates include weighted relative entropies and $\Phi$-entropies adapted to $\langle v\rangle^{\gamma}$.
- Prove an unconditional lower bound $\rho\ge m_0>0$ (a "no-vacuum" theorem) for large data with confined geometry; Mouhot's Maxwellian lower bounds are conditional on the same quantities.
- Establish local $L^p_v$ propagation in the inhomogeneous setting directly from the Fisher-information estimate, including $x$-dependence.
- Construct a candidate blow-up scenario for very soft potentials (self-similar concentration in $v$) to test the sharpness of $\gamma+2s=-2$; a rigorous non-existence proof for such profiles would be equally informative.
- Extend to bounded domains with diffusive/specular boundary conditions, where soft potentials interact badly with grazing boundary trajectories.

## 9. Key References

- **[Foundational]** H. Grad. *Asymptotic theory of the Boltzmann equation, II.* In: Rarefied Gas Dynamics (J. Laurmann, ed.), Academic Press, 1963.
- **[Foundational]** R. Alexandre, L. Desvillettes, C. Villani, B. Wennberg. *Entropy dissipation and long-range interactions.* Archive for Rational Mechanics and Analysis, 152(4):327–355, 2000.
- **[Foundational]** R. J. DiPerna, P.-L. Lions. *On the Cauchy problem for Boltzmann equations: global existence and weak stability.* Annals of Mathematics, 130(2):321–366, 1989.
- **[SOTA]** P. T. Gressman, R. M. Strain. *Global classical solutions of the Boltzmann equation without angular cut-off.* Journal of the American Mathematical Society, 24(3):771–847, 2011.
- **[SOTA]** R. Alexandre, Y. Morimoto, S. Ukai, C.-J. Xu, T. Yang. *Global existence and full regularity of the Boltzmann equation without angular cutoff.* Communications in Mathematical Physics, 304(2):513–581, 2011.
- **[SOTA]** R. Alexandre, Y. Morimoto, S. Ukai, C.-J. Xu, T. Yang. *The Boltzmann equation without angular cutoff in the whole space: I, Global existence for soft potential.* Journal of Functional Analysis, 262(3):915–1010, 2012.
- **[SOTA]** C. Imbert, L. Silvestre. *Global regularity estimates for the Boltzmann equation without cut-off.* Journal of the American Mathematical Society, 35(3):625–703, 2022.
- **[SOTA]** L. Silvestre. *A new regularization mechanism for the Boltzmann equation without cut-off.* Communications in Mathematical Physics, 348(1):69–100, 2016.
- **[SOTA]** C. Imbert, C. Mouhot, L. Silvestre. *Decay estimates for large velocities in the Boltzmann equation without cutoff.* Journal de l'École polytechnique — Mathématiques, 7:143–183, 2020.
- **[SOTA]** R. Duan, S. Liu, S. Sakamoto, R. M. Strain. *Global mild solutions of the Landau and non-cutoff Boltzmann equations.* Communications on Pure and Applied Mathematics, 74(5):932–1020, 2021.
- **[Recent]** R. Alonso, Y. Morimoto, W. Sun, T. Yang. *Non-cutoff Boltzmann equation with polynomial decay perturbations.* Revista Matemática Iberoamericana, 37(1):189–292, 2021.
- **[Recent]** N. Guillen, L. Silvestre. *The Landau equation does not blow up.* arXiv:2311.09420, 2023.
- **[Recent]** S. Chaturvedi. *Stability of vacuum for the Boltzmann equation with moderately soft potentials.* Annals of PDE, 7(2), Article 15, 2021.
- **[Foundational]** L. Desvillettes, B. Wennberg. *Smoothness of the solution of the spatially homogeneous Boltzmann equation without cutoff.* Communications in Partial Differential Equations, 29(1–2):133–155, 2004.
- **[Survey]** C. Villani. *A review of mathematical topics in collisional kinetic theory.* Handbook of Mathematical Fluid Dynamics, Vol. I, North-Holland, 2002, pp. 71–305.
- **[Survey]** C. Imbert, L. Silvestre. *The weak Harnack inequality for the Boltzmann equation without cut-off.* Journal of the European Mathematical Society, 22(2):507–592, 2020.

## 10. Worked Example / Concrete Special Case

**Loss of exponential relaxation when $\gamma+2s<0$.** Take the spatially homogeneous linearized equation $\partial_t g = Lg$ in $L^2(dv)$ with $f=\mu+\mu^{1/2}g$. Set $y(t)=\|g(t)\|^2_{L^2}$ and $a=\tfrac{\gamma+2s}{2}<0$. Gressman–Strain coercivity gives

$$\tfrac{d}{dt}\,y = 2\langle Lg,g\rangle \le -2c\,\big\|\langle v\rangle^{a} g\big\|^2_{L^2}.$$

Suppose a moment bound $\big\|\langle v\rangle^{k} g(t)\big\|_{L^2}\le M$ propagates for some $k>0$. Interpolate the unweighted norm between the dissipation weight $a<0$ and the moment weight $k>0$: choose $\theta\in(0,1)$ with $0=\theta a+(1-\theta)k$, i.e.

$$\theta=\frac{k}{k+|a|}.$$

Hölder in $v$ then gives $\|g\| \le \|\langle v\rangle^{a}g\|^{\theta}\,\|\langle v\rangle^{k}g\|^{1-\theta}$, hence

$$\big\|\langle v\rangle^{a}g\big\|^2 \;\ge\; y^{1/\theta}\,M^{-2(1-\theta)/\theta},$$

and the differential inequality becomes

$$y' \le -C\,y^{1/\theta},\qquad C = 2c\,M^{-2(1-\theta)/\theta},\qquad \tfrac1\theta>1 .$$

Integrating $y' = -Cy^{1/\theta}$:

$$y(t) \;\lesssim\; \big(C(\tfrac1\theta-1)\,t\big)^{-\frac{\theta}{1-\theta}} = \big(C\,\tfrac{|a|}{k}\,t\big)^{-k/|a|},\qquad \frac{\theta}{1-\theta}=\frac{k}{|a|}=\frac{2k}{|\gamma+2s|}.$$

**Reading the computation.**
- For $\gamma+2s>0$ the weight $\langle v\rangle^{a}$ has $a>0$, no interpolation is needed, $y'\le -2cy$, and relaxation is exponential.
- For $\gamma+2s<0$ the best available rate is the **polynomial** $y(t)\lesssim t^{-2k/|\gamma+2s|}$. It can be made arbitrarily fast by propagating higher moments $k$, but never exponential, and every gain costs a moment bound whose constant $M$ degrades the prefactor $C$.
- Concretely, for $p=2.5$ ($\gamma=-\tfrac53$, $s=\tfrac23$, so $\gamma+2s=-\tfrac13$) and $k=2$, the rate is $t^{-12}$; for $\gamma+2s=-2$ and $k=2$ it is only $t^{-2}$.

This is the exact mechanism blocking large-data theory: a nonlinear Gronwall argument on the perturbation needs the linear damping to beat the quadratic term $Q(g,g)$ uniformly in time. Exponential damping does this for any small datum; polynomial damping $t^{-2k/|\gamma+2s|}$ only closes when the moment bound $M$ is itself controlled, and propagating $\langle v\rangle^{k}$ moments for large data is precisely the unconditional estimate that does not exist.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*