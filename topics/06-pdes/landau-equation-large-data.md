---
id: 06-pdes/landau-equation-large-data
title: "Landau Equation Large Data"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Landau Equation Large Data

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/landau-equation-large-data` · **Status:** open

## 1. Problem Statement / Conjecture

The Landau equation is the grazing-collision limit of the Boltzmann equation and the standard kinetic model of a dilute plasma. The open problem is **global well-posedness for large data**, in particular in the physically relevant Coulomb case $\gamma=-3$.

**Conjecture (large-data global regularity).** Let $f_0 \ge 0$ on $\mathbb{T}^3_x \times \mathbb{R}^3_v$ (or $\mathbb{R}^3_x\times\mathbb{R}^3_v$) have finite mass, energy and entropy, and suitable decay in $v$. Then the spatially inhomogeneous Landau equation with Coulomb potential
$$\partial_t f + v\cdot\nabla_x f = Q_L(f,f)$$
admits a unique global-in-time solution that is smooth for $t>0$, with no finite-time blow-up of $\|f(t)\|_{L^\infty}$.

A complete resolution requires either (i) a proof of global existence, uniqueness and smoothness under such hypotheses without smallness, closeness to a Maxwellian, or a priori bounds that are themselves unproven; or (ii) a counterexample exhibiting a solution whose $L^\infty$ norm (or a hydrodynamic-type quantity) blows up in finite time from admissible data.

The **space-homogeneous** version of this problem (data depending on $v$ only) was open for four decades and was resolved affirmatively by Guillen–Silvestre in 2023 via monotonicity of the Fisher information. The inhomogeneous problem — the one physicists actually pose — remains open, and is the primary content of this entry.

## 2. Mathematical Foundations

Let $f(t,x,v)\ge0$ be the phase-space density. The Landau collision operator is
$$Q_L(f,f)(v)=\nabla_v\cdot\left(\int_{\mathbb{R}^3} a(v-v_*)\big[f(v_*)\nabla_v f(v)-f(v)\nabla_{v_*}f(v_*)\big]\,dv_*\right),$$
with the projection-type kernel
$$a_{ij}(z)=|z|^{\gamma+2}\left(\delta_{ij}-\frac{z_iz_j}{|z|^2}\right),\qquad \gamma\in[-3,1].$$
Cases: $\gamma>0$ **hard potentials**, $\gamma=0$ **Maxwell molecules**, $-2\le\gamma<0$ **moderately soft**, $-3\le\gamma<-2$ **very soft**, and $\gamma=-3$ **Coulomb**, the case derived by Landau (1936).

In divergence-free (non-conservative) form,
$$Q_L(f,f)=\bar a_{ij}[f]\,\partial_{ij}f - \bar c[f]\,f,\qquad
\bar a_{ij}[f]=a_{ij}*f,\quad \bar c[f]=\partial_{ij}a_{ij}*f = c_\gamma\,|v|^{\gamma}*f,$$
where for $\gamma=-3$ one has $\partial_{ij}a_{ij}(z) = -8\pi\,\delta_0(z)$ in $\mathbb{R}^3$, so $\bar c[f]=8\pi f$ and the equation becomes the **semilinear** problem
$$\partial_t f + v\cdot\nabla_x f=\bar a_{ij}[f]\partial_{ij}f + 8\pi f^2 .$$
This is the crux: the diffusion $\bar a[f]$ (order $-1$ smoothing in $v$, gain of $|v|^{\gamma+2}=|v|^{-1}$ weight) competes against a **quadratic reaction term** $8\pi f^2$ of exactly critical strength — the Coulomb case sits at the borderline where scaling gives no margin.

Conserved quantities: mass, momentum, energy; the Boltzmann entropy $H(f)=\iint f\log f$ is nonincreasing with dissipation
$$D(f)=\frac12\iint f f_* \,a_{ij}(v-v_*)\left(\frac{\partial_i f}{f}-\frac{\partial_{i*}f_*}{f_*}\right)\left(\frac{\partial_j f}{f}-\frac{\partial_{j*}f_*}{f_*}\right)\ge 0 .$$
The **Fisher information** is $I(f)=\int \frac{|\nabla f|^2}{f}\,dv$. Guillen–Silvestre proved $\frac{d}{dt}I(f(t))\le0$ along homogeneous Landau flows for all $\gamma\in[-3,1]$, giving $\|f(t)\|_{L^\infty}$ control via the Sobolev-type bound $\|f\|_{L^\infty}\lesssim I(f)^{3/4}\|f\|_{L^1}^{1/4}$-type interpolation.

Scaling: for $\gamma=-3$ the homogeneous equation is invariant under $f_\lambda(t,v)=\lambda^{2}f(\lambda^{?}t,\lambda v)$ families that leave $L^{3/2}_v$ critical; $L^p$ with $p>3/2$ is subcritical, $L^1\cap L\log L$ is supercritical. Weak solutions in the sense of Villani (H-solutions) exist globally for all $\gamma$; uniqueness and regularity are the missing pieces.

## 3. History & State of the Art (SOTA)

- **1936.** Landau derives the equation as the grazing-collision limit of Boltzmann for Coulomb interactions.
- **1998.** Villani constructs global **H-solutions** for the homogeneous equation with very soft potentials including Coulomb, using entropy-dissipation as the only compactness; uniqueness and regularity left open.
- **2000.** Desvillettes–Villani prove global smoothness, uniqueness, moment propagation and exponential $H$-theorem convergence for **hard potentials** $\gamma\in(0,1]$, homogeneous.
- **2002.** Guo proves global existence near Maxwellian in a periodic box for the full inhomogeneous equation, all $\gamma\ge-3$ — the perturbative benchmark.
- **2015–2019.** Conditional/partial regularity era: Desvillettes' entropy-dissipation estimates; Silvestre's $L^\infty$ bound conditional on hydrodynamic quantities; Golse–Imbert–Mouhot–Vasseur's De Giorgi–Nash–Moser Harnack inequality for kinetic Fokker–Planck with rough coefficients; Golse–Gualdani–Imbert–Vasseur show the singular time set of homogeneous Coulomb solutions has Hausdorff dimension $\le 1/2$.
- **2018–2022.** Cameron–Silvestre–Snelson: global a priori $L^\infty$ and Schauder estimates for the inhomogeneous equation with moderately soft potentials $\gamma\in[-2,0)$, conditional on bounded mass, energy and entropy densities. Henderson–Snelson–Tarfulea: local well-posedness and continuation criteria for rough, slowly decaying data.
- **2023.** **Guillen–Silvestre**: the homogeneous Landau equation *does not blow up* for any $\gamma\in[-3,1]$; the Fisher information is monotone decreasing. This closes the homogeneous large-data problem.
- **2024–2026.** Effort transfers to the inhomogeneous case, where Fisher information is not known to be monotone because of the transport term $v\cdot\nabla_x f$.

## 4. Partial Results / Verified Cases

| Setting | Range | Status |
|---|---|---|
| Homogeneous, hard potentials | $\gamma\in(0,1]$ | Solved (Desvillettes–Villani 2000) |
| Homogeneous, Maxwell molecules | $\gamma=0$ | Solved; explicit moment ODEs (Villani) |
| Homogeneous, all soft incl. Coulomb | $\gamma\in[-3,0)$ | Solved: no blow-up, Guillen–Silvestre 2023 |
| Homogeneous Coulomb, radial/isotropic | $\gamma=-3$ | Earlier: global bounds by Gualdani–Guillen (2016, 2019) via $A_p$ weights and barriers |
| Homogeneous Coulomb, higher integrability | $f\in L^\infty_t L^{p}$, $p>3/2$ | Uniqueness (Fournier; Chern–Gualdani) |
| Inhomogeneous, near Maxwellian, torus | all $\gamma\ge-3$, small perturbation | Solved (Guo 2002; Duan–Liu–Sakamoto–Strain 2021 for mild solutions in $L^\infty_v L^2_x$-type spaces) |
| Inhomogeneous, conditional | $\gamma\in[-2,0)$, bounded mass/energy/entropy densities | Global smoothness (Cameron–Silvestre–Snelson 2018; Henderson–Snelson) |
| Inhomogeneous, general large data | $\gamma\in[-3,-2)$, incl. Coulomb | **Open** |
| Renormalized-type weak solutions | inhomogeneous | Existence known (Alexandre–Villani, Lions-type framework); uniqueness open |
| Approximate self-similar blow-up | isotropic Landau model | Ruled out for a class of profiles (Bedrossian–Gualdani–Snelson 2022) |

## 5. Principal Obstacles

- **Criticality of the reaction term.** For $\gamma=-3$ the equation is $\partial_t f = \bar a[f]:\nabla^2 f + 8\pi f^2$. Parabolic regularization from $\bar a[f]$ and the quadratic source are on exactly the same scaling footing; standard De Giorgi/Moser iteration produces a nonlinear Grönwall inequality that closes only under an a priori bound one does not have.
- **Degeneracy of the diffusion matrix.** $\bar a[f]$ has an eigenvalue $\sim |v|^{\gamma+2}$ that vanishes as $|v|\to\infty$ for $\gamma<-2$, and the ellipticity ratio $\Lambda/\lambda$ degenerates unless the mass density is bounded below — so uniform Harnack constants require lower mass bounds that must themselves be propagated.
- **Transport breaks the Fisher-information monotonicity.** The Guillen–Silvestre proof rests on a delicate pointwise inequality for the collision integrand that yields $\frac{d}{dt}I \le 0$ in $v$ alone. Adding $v\cdot\nabla_x f$ contributes $-\int \frac{2\nabla_v f\cdot\nabla_x f}{f}\cdot$(terms) with no sign, and there is no known kinetic analogue of the monotone quantity.
- **Entropy is supercritical.** The only unconditional a priori bounds — mass, energy, entropy — are strictly below the scaling-critical regularity threshold for $\gamma<-2$. This is the same "supercritical a priori estimate" wall as Navier–Stokes.
- **No maximum principle in $x$.** Local mass can concentrate along characteristics; unlike the homogeneous case, no comparison principle prevents vacuum formation, and vacuum destroys the ellipticity of $\bar a[f]$.

## 6. The Gap

Proven: (a) homogeneous Coulomb has no blow-up; (b) inhomogeneous Coulomb has no blow-up **provided** the hydrodynamic fields
$$\rho(t,x)=\int f\,dv,\quad E(t,x)=\int |v|^2 f\,dv,\quad H(t,x)=\int f\log f\,dv$$
remain bounded above (and $\rho$ bounded below) uniformly on the time interval.

The general statement requires exactly this: **propagating pointwise-in-$x$ bounds on $\rho, E, H$ from finite total mass/energy/entropy**, or an alternative coercive quantity that survives free transport. Equivalently: find a Lyapunov functional $\mathcal{F}[f]$ with (i) $\frac{d}{dt}\mathcal{F}\le 0$ along the full kinetic flow, and (ii) $\mathcal{F}$ subcritical, i.e. controlling $\|f\|_{L^\infty}$ or a critical Lebesgue norm. The homogeneous answer is $\mathcal{F}=I(f)$; no inhomogeneous candidate is known. That single step is the gap.

## 7. Current Research (as of June 2026)

- **Kinetic Fisher information.** Attempts to build a transport-compatible modification of $I(f)$ — e.g. hypocoercive twists $\int \frac{|\nabla_v f + \alpha t \nabla_x f|^2}{f}$ — are the most direct heir to Guillen–Silvestre. No global monotonicity has been established. *(frontier — verify)*
- **Conditional-to-unconditional programme** (Silvestre, Snelson, Imbert, Mouhot, and collaborators at Chicago, UCF, Cambridge, ENS/Polytechnique): pushing conditional regularity from $\gamma\in[-2,0)$ down to $\gamma=-3$, and attacking lower mass bounds via kinetic Harnack.
- **Partial regularity.** Extending the Golse–Gualdani–Imbert–Vasseur dimension-$1/2$ singular-set bound to the inhomogeneous setting, a Caffarelli–Kohn–Nirenberg analogue for kinetic equations. *(frontier — verify)*
- **Blow-up search.** Numerical and analytic construction of self-similar or approximately self-similar concentrating profiles for the isotropic Landau model and for the true Coulomb operator; Bedrossian–Gualdani–Snelson-type non-existence results narrow but do not close the space of candidates.
- **Coupled Vlasov–Poisson–Landau.** Large-data theory including the self-consistent field is strictly harder; only near-equilibrium results exist.

## 8. Future Work

1. **Find the kinetic Lyapunov functional.** Identify a quantity monotone under $\partial_t + v\cdot\nabla_x$ *and* under $Q_L$; the Fisher information's convexity structure under the Landau flow suggests looking at entropy-type functionals on the whole phase space with $t$-dependent weights.
2. **Lower mass bounds without smallness.** Prove $\rho(t,x)\ge c(t)>0$ from finite entropy alone, which would restore uniform ellipticity of $\bar a[f]$.
3. **Improve the a priori class.** Any unconditional bound in $L^\infty_t L^{p}_{x,v}$ with $p$ above the critical exponent would immediately close the problem via existing conditional theory.
4. **Construct or exclude blow-up** for the isotropic scalar model $\partial_t u = u\,\Delta u + \alpha u^2$ as a proving ground; the sign and size of $\alpha$ determine blow-up and mirror the Coulomb borderline.
5. **Grazing-collision consistency.** Transfer techniques between Boltzmann-without-cutoff (Imbert–Silvestre regularity theory) and Landau, since both share the same conditional-estimate architecture.

## 9. Key References

- **[Foundational]** L. D. Landau. *Die kinetische Gleichung für den Fall Coulombscher Wechselwirkung.* Phys. Z. Sowjet. **10**, 154 (1936).
- **[Foundational]** C. Villani. *On a new class of weak solutions to the spatially homogeneous Boltzmann and Landau equations.* Archive for Rational Mechanics and Analysis **143** (1998), 273–307.
- **[Foundational]** L. Desvillettes, C. Villani. *On the spatially homogeneous Landau equation for hard potentials, Parts I & II.* Communications in PDE **25** (2000).
- **[Foundational]** Y. Guo. *The Landau equation in a periodic box.* Communications in Mathematical Physics **231** (2002), 391–434.
- **[SOTA]** N. Guillen, L. Silvestre. *The Landau equation does not blow up.* arXiv:2311.09420 (2023).
- **[SOTA]** L. Silvestre. *Upper bounds for parabolic equations and the Landau equation.* Journal of Differential Equations **262** (2017), 3034–3055.
- **[SOTA]** S. Cameron, L. Silvestre, S. Snelson. *Global a priori estimates for the inhomogeneous Landau equation with moderately soft potentials.* Annales de l'IHP – Analyse Non Linéaire **35** (2018), 625–642.
- **[SOTA]** F. Golse, C. Imbert, C. Mouhot, A. Vasseur. *Harnack inequality for kinetic Fokker–Planck equations with rough coefficients and application to the Landau equation.* Annali della Scuola Normale Superiore di Pisa **19** (2019), 253–295.
- **[SOTA]** F. Golse, M. P. Gualdani, C. Imbert, A. Vasseur. *Partial regularity in time for the space-homogeneous Landau equation with Coulomb potential.* Annales de l'IHP – Analyse Non Linéaire **39** (2022), 1575–1611.
- **[SOTA]** M. P. Gualdani, N. Guillen. *Estimates for radial solutions of the homogeneous Landau equation with Coulomb potential.* Analysis & PDE **9** (2016), 1772–1809.
- **[SOTA]** J. Bedrossian, M. P. Gualdani, S. Snelson. *Non-existence of some approximately self-similar singularities for the Landau, Vlasov–Poisson–Landau, and Boltzmann equations.* Transactions of the AMS **375** (2022), 2187–2216.
- **[SOTA]** R. Duan, S. Liu, S. Sakamoto, R. M. Strain. *Global mild solutions of the Landau and non-cutoff Boltzmann equations.* Communications on Pure and Applied Mathematics **74** (2021), 932–1020.
- **[Survey]** C. Villani. *A review of mathematical topics in collisional kinetic theory.* Handbook of Mathematical Fluid Dynamics, Vol. I, North-Holland, 2002, 71–305.
- **[Survey]** L. Desvillettes. *Entropy dissipation estimates for the Landau equation in the Coulomb case and applications.* Journal of Functional Analysis **269** (2015), 1359–1403.

## 10. Worked Example / Concrete Special Case

**Maxwell molecules, homogeneous, isotropic: an exactly solvable moment.** Take $d=3$, $\gamma=0$, so $a_{ij}(z)=|z|^2\delta_{ij}-z_iz_j$ and $b_i(z)=\partial_j a_{ij}(z)=2z_i-4z_i=-2z_i$. Weak form: for a test function $\varphi$,
$$\frac{d}{dt}\!\int\! f\varphi=\frac12\iint f f_*\Big[a_{ij}(z)\big(\partial_{ij}\varphi+\partial_{ij}\varphi_*\big)+2b_i(z)\big(\partial_i\varphi-\partial_i\varphi_*\big)\Big],\quad z=v-v_*.$$

*Energy check.* With $\varphi=|v|^2$: $\partial_{ij}\varphi=2\delta_{ij}$, so $a_{ij}(4\delta_{ij})=4\,\mathrm{tr}\,a=8|z|^2$, while $2b_i(2v_i-2v_{*i})=-8|z|^2$. Sum zero: energy $M_2=\int|v|^2f$ is conserved. ✓

*Fourth moment.* Let $M_4=\int |v|^4 f$, with $f$ normalized to mass $1$, mean zero, and isotropic (so $\int f v_iv_j=\tfrac{M_2}{3}\delta_{ij}$; isotropy is propagated). With $\varphi=|v|^4$: $\partial_i\varphi=4|v|^2v_i$, $\partial_{ij}\varphi=4|v|^2\delta_{ij}+8v_iv_j$, hence
$$a_{ij}(z)\partial_{ij}\varphi(v)=16|v|^2|z|^2-8(z\cdot v)^2 .$$
Using the $v\leftrightarrow v_*$ symmetry the whole integrand reduces to twice
$$16|v|^2|z|^2-8(z\cdot v)^2-16|v|^2(z\cdot v),$$
so $\dot M_4=\iint ff_*\big[\cdots\big]$. Term by term, with $\int f_*v_*=0$:
- $16\iint ff_*|v|^2(|v|^2-2v\cdot v_*+|v_*|^2)=16(M_4+M_2^2)$,
- $-8\iint ff_*(|v|^2-v\cdot v_*)^2=-8\big(M_4+\tfrac13 M_2^2\big)$,
- $-16\iint ff_*|v|^2(|v|^2-v\cdot v_*)=-16M_4$.

Adding:
$$\boxed{\;\frac{dM_4}{dt}=-8M_4+\frac{40}{3}M_2^2\;}$$
a closed linear ODE, so
$$M_4(t)=\tfrac53 M_2^2+\Big(M_4(0)-\tfrac53M_2^2\Big)e^{-8t}.$$
The fixed point $M_4=\tfrac53M_2^2$ is exactly the Maxwellian value ($M_2=3T$, $M_4=15T^2$). Moments are bounded for all time with no smallness assumption.

**Why this collapses for Coulomb.** Repeating the computation with $\gamma=-3$ gives $a_{ij}(z)=|z|^{-1}(\delta_{ij}-\hat z_i\hat z_j)$; the moment hierarchy no longer closes, the kernel is singular at $z=0$ so near-collisions dominate, and the drift term becomes $\bar c[f]=8\pi f$, turning the moment identity into an inequality whose right-hand side involves $\int f^2|v|^k$ — a quantity not controlled by moments. That failure of closure at $\gamma=-3$ is the elementary shadow of the obstacle in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*