---
id: 06-pdes/logarithmic-schrodinger-dispersive-estimates
title: "Logarithmic Schrodinger Equation Dispersive Estimates"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Logarithmic Schrödinger Equation Dispersive Estimates

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/logarithmic-schrodinger-dispersive-estimates` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the logarithmic Schrödinger equation (logNLS) on $\mathbb{R}^d$,

$$i\partial_t u + \tfrac{1}{2}\Delta u = \lambda\, u \ln|u|^2, \qquad u(0,\cdot)=u_0,$$

with $\lambda\in\mathbb{R}\setminus\{0\}$ ($\lambda>0$ defocusing, $\lambda<0$ focusing).

**The problem.** Establish sharp pointwise dispersive decay for the defocusing case, and a sharp dispersion/non-dispersion dichotomy in the focusing case. Concretely:

1. **(Sharp $L^\infty$ decay.)** Prove that for all $u_0$ in the energy space with $xu_0\in L^2$ and $\lambda>0$,
 $$\|u(t)\|_{L^\infty(\mathbb{R}^d)} \;\lesssim\; \big(t\sqrt{\ln t}\big)^{-d/2},\qquad t\to\infty,$$
 i.e. dispersion strictly *faster* than the linear rate $t^{-d/2}$ by the factor $(\ln t)^{-d/4}$, together with a matching lower bound for non-trivial data.
2. **(Uniform-in-data / $L^1\to L^\infty$ form.)** Determine whether the decay is uniform over bounded sets of data, and whether a genuine dispersive (kernel) estimate or Strichartz-type space-time estimate adapted to the rescaled variable holds.
3. **(Asymptotic completeness.)** Show that the phase of $u$ admits a complete long-time expansion (a modified-scattering statement) matching the known universal behaviour of $|u|$.
4. **(Focusing dichotomy.)** For $\lambda<0$, classify which data disperse and which remain trapped in the Gausson/breather regime.

A complete solution proves the upper and lower bounds in (1) for all $d\ge1$ and all non-trivial energy-space data, or exhibits data violating them.

## 2. Mathematical Foundations

**Energy space.** The nonlinearity $z\mapsto z\ln|z|^2$ is continuous but not locally Lipschitz at $z=0$, and $\ln|u|^2$ is not integrable against $|u|^2$ for general $H^1$ data. The natural space is
$$W:=\Big\{u\in H^1(\mathbb{R}^d)\;:\; |u|^2\big|\ln|u|^2\big|\in L^1(\mathbb{R}^d)\Big\},$$
an Orlicz-type space with $A(s)=-s^2\ln s^2$ near $0$. Conserved quantities:
$$M(u)=\|u\|_{L^2}^2,\qquad E(u)=\tfrac12\|\nabla u\|_{L^2}^2+\lambda\!\int_{\mathbb{R}^d}\!|u|^2\big(\ln|u|^2-1\big)\,dx .$$

**Uniqueness mechanism.** For all $z_1,z_2\in\mathbb{C}$,
$$\big|\,\mathrm{Im}\big[(z_1\ln|z_1|^2-z_2\ln|z_2|^2)\,\overline{(z_1-z_2)}\big]\big|\le 2\,|z_1-z_2|^2 ,$$
which yields $L^2$ uniqueness by Grönwall despite the failure of Lipschitz continuity (Cazenave–Haraux 1980).

**No scaling, no small data.** logNLS has no scaling invariance, but for $\mu>0$,
$$u \text{ solves} \;\Longrightarrow\; w:=\mu\,e^{-i\lambda t\ln\mu^2}u \text{ solves.}$$
Hence amplitude is a gauge symmetry: there is **no small-data regime**, and the nonlinearity is never a perturbation of the free flow.

**Exact Gaussian solutions.** The Gaussian ansatz is preserved. With $\tau$ solving
$$\ddot\tau=\frac{4\lambda}{\tau},\qquad \tau(0)=1,\ \dot\tau(0)=0,$$
(a dimension-independent ODE), one gets explicit solutions with $|u(t,x)|=\tau(t)^{-d/2}\exp\!\big(-|x|^2/(2\tau(t)^2)\big)$ up to normalisation. For $\lambda>0$, $\tau(t)\sim 2t\sqrt{2\lambda\ln t}$; for $\lambda<0$, $\tau$ is periodic — a **breather**, and the stationary choice gives the **Gausson**
$$\phi(x)=e^{\frac{d}{2}}\,e^{-\lambda|x|^2 }\ \ (\lambda<0,\ \text{up to normalisation}),\qquad -\tfrac12\Delta\phi+\lambda\phi\ln|\phi|^2 = \omega\phi .$$

**Rescaled unknown.** Setting
$$u(t,x)=\frac{1}{\tau(t)^{d/2}}\,v\!\left(t,\frac{x}{\tau(t)}\right)\exp\!\left(i\frac{\dot\tau(t)}{2\tau(t)}|x|^2\right),$$
$v$ solves a logNLS with a confining harmonic term whose coefficient decays, and $\|v(t)\|_{H^1}+\||y|v(t)\|_{L^2}$ stays bounded. This is the engine of all known decay results.

## 3. History & State of the Art (SOTA)

- **1976.** Bialynicki-Birula and Mycielski introduce logNLS as the unique nonlinear wave mechanics preserving separability of non-interacting subsystems; they discover the Gausson.
- **1980–1983.** Cazenave and Haraux build the well-posedness theory in $W$ using nonlinear semigroups; Cazenave proves orbital stability of the Gausson.
- **1987.** Blanchard–Stubbe–Vázquez place Gausson stability in the general variational framework for solitary waves.
- **2014.** d'Avenia–Montefusco–Squassina give a modern variational treatment (Orlicz setting, existence and multiplicity of stationary states).
- **2018 (key).** Carles and Gallagher (*Duke Math. J.*) prove **universal dynamics** for $\lambda>0$: for every non-trivial $u_0$ in the energy space with finite variance, the rescaled density converges,
 $$\tau(t)^{d}\,\big|u\big(t,\tau(t)\,y\big)\big|^2 \;\longrightarrow\; \frac{\|u_0\|_{L^2}^2}{\pi^{d/2}}\,e^{-|y|^2}\quad\text{in }L^1(\mathbb{R}^d),$$
 with $\tau(t)\sim 2t\sqrt{2\lambda\ln t}$. The limit profile is **independent of the initial datum** — no analogue exists for power nonlinearities.
- **2019.** Bao–Carles–Su–Tang give regularised finite-difference and time-splitting schemes with error estimates, making the $\sqrt{\ln t}$ rate numerically accessible.
- **2020–2022.** Ferriere obtains quantitative convergence in Wasserstein distance and treats the focusing breather/superposition regime; Carles–Ferriere handle quadratic potentials; Carles' EMS survey consolidates the isothermal-fluid analogy.

## 4. Partial Results / Verified Cases

- **Global well-posedness:** all $d\ge1$, both signs of $\lambda$, data in $W$ (Cazenave–Haraux 1980; Cazenave 1983); uniqueness holds already in $L^2$.
- **Exact Gaussian data, all $d\ge1$:** the decay $\|u(t)\|_{L^\infty}=\tau(t)^{-d/2}\sim c_d (t\sqrt{\ln t})^{-d/2}$ is proved *exactly*, upper and lower bound, by ODE analysis.
- **General finite-variance data, $\lambda>0$, all $d\ge1$:** $L^1$-convergence of the rescaled density to the universal Gaussian (Carles–Gallagher 2018). Consequently, for $2\le p< \frac{2d}{d-2}$ (all $p<\infty$ if $d\le2$),
 $$\|u(t)\|_{L^p}\;\lesssim\;\tau(t)^{-d\left(\frac12-\frac1p\right)}\sim\big(t\sqrt{\ln t}\big)^{-d\left(\frac12-\frac1p\right)},$$
 via Gagliardo–Nirenberg applied to the rescaled unknown $v$, whose $H^1$ norm is bounded. Matching **lower** bounds in $L^p$, $p>2$, follow from the $L^1$ convergence plus mass conservation.
- **Rates:** Ferriere (2021) upgrades the convergence to a quantitative rate in Wasserstein-2 distance, and obtains the semiclassical/isothermal-Euler limit.
- **Focusing, $\lambda<0$:** the Gausson is orbitally stable in $W$ (Cazenave 1983; Blanchard–Stubbe–Vázquez 1987; Ardila 2016) — dispersion **fails** for an open set of data; breathers (periodic $\tau$) give explicit non-dispersing, non-stationary solutions (Ferriere 2020).
- **Variants:** logNLS with a harmonic potential is completely solved in the Gaussian sector (Carles–Ferriere 2021).

## 5. Principal Obstacles

- **No small-data / no perturbative regime.** The amplitude gauge symmetry means the nonlinearity cannot be treated as a perturbation at any size. Duhamel + Strichartz, the standard route to dispersive estimates, has no entry point.
- **Non-Lipschitz nonlinearity.** $z\ln|z|^2$ fails to be $C^1$ at $z=0$; contraction-mapping and standard bootstrap arguments break, and the flow is only continuous, not smooth, on $W$. Regularising ($\ln(\varepsilon+|u|^2)$) destroys the exact Gaussian algebra.
- **Loss of $L^\infty$ control.** The known results are $L^1$/$L^2$-based: they control the density, not its supremum. Passing from $L^1$ convergence of $\tau^d|u(t,\tau y)|^2$ to $L^\infty$ requires uniform higher regularity of the rescaled solution $v$, which is not conserved — the rescaled equation carries a slowly decaying harmonic term $\frac{\ddot\tau\tau}{2}|y|^2$ and a $\ln\tau$ phase forcing.
- **Phase is uncontrolled.** Carles–Gallagher control $|u|$ but the phase acquires an unbounded $\lambda\ln\tau^{-d}$ drift; no weighted-space vector field commutes cleanly with $u\ln|u|^2$ (the Galilean operator $J=x+it\nabla$ does not annihilate the nonlinearity's log).
- **Non-uniformity in the data.** The convergence to the universal profile is *not* known to be uniform on bounded sets of $W$, so no kernel-type $L^1\to L^\infty$ statement can currently be formulated, let alone proved.

## 6. The Gap

Proved: $\tau(t)\sim 2t\sqrt{2\lambda\ln t}$ and $L^1$-convergence of the rescaled density, hence sharp $L^p$ decay for $p$ strictly below the $H^1$-critical exponent. Conjectured: the endpoint $p=\infty$,
$$\big(t\sqrt{\ln t}\big)^{d/2}\|u(t)\|_{L^\infty}\;\longrightarrow\;\frac{\|u_0\|_{L^2}}{\pi^{d/4}}\ \text{(or at least stays bounded)} .$$
The missing step is a **uniform-in-time higher-regularity bound for the rescaled unknown**: control of $\|v(t)\|_{H^s}$, $s>d/2$, or of $\|\Delta v\|_{L^2}$, under the rescaled logNLS. The obstruction is that the log nonlinearity is not $H^s$-tame: $\|\,f\ln|f|^2\|_{H^s}$ cannot be bounded by $\|f\|_{H^s}$ times a function of $\|f\|_{L^\infty}$ without lower bounds on $|f|$, and $v$ has Gaussian-thin tails where $\ln|v|^2\sim-|y|^2$ diverges.

## 7. Current Research (as of June 2026)

- **Montpellier / Rennes (Carles and collaborators).** Rescaled-variable methods, logNLS with potentials, and the isothermal-fluid (Madelung) reformulation, where $\lambda\ln\rho$ is exactly an isothermal pressure. Programme: transfer compressible-Euler decay technology to logNLS.
- **Ferriere and the Wasserstein school.** Optimal-transport metrics as a substitute for $L^\infty$ control; sharpening rates in $W_2$ and pushing toward $W_\infty$. *(frontier — verify)* Reported extensions to infinite-variance data with slowly decaying tails.
- **Numerical analysis (Bao, Su, Tang and collaborators).** Regularised and Lie/Strang splitting schemes with $\varepsilon$-uniform error bounds; high-resolution computations that confirm the $(\ln t)^{-d/4}$ correction in $L^\infty$ well beyond the range where proofs exist.
- **Variational/stationary side.** Orlicz-space critical point theory for logNLS on domains, graphs and with magnetic fields (Squassina and collaborators), and stability thresholds for excited Gaussons.
- **Focusing dichotomy.** *(frontier — verify)* Attempts to prove that all data with energy below the Gausson level and negative-definite virial disperse, mirroring the Kenig–Merle roadmap; the absence of scaling invariance blocks the concentration-compactness step.

## 8. Future Work

- Prove uniform $H^s$ bounds ($s>d/2$) for the rescaled unknown; this alone would close the $L^\infty$ endpoint.
- Develop Strichartz-type estimates in the *rescaled* time variable $s=\int^t \tau(\sigma)^{-2}d\sigma$, in which the logNLS becomes autonomous-like.
- Obtain the second-order asymptotic expansion (phase correction), giving a genuine modified-scattering theory and asymptotic completeness.
- Extend beyond finite variance: characterise the class of $u_0$ for which $\tau$-rescaling is still the right normalisation.
- Settle the focusing case: build a virial/concentration argument that survives the loss of scaling invariance.
- Exploit the isothermal-Euler limit to import large-time decay results for compressible flows.

## 9. Key References

- **[Foundational]** I. Bialynicki-Birula, J. Mycielski. *Nonlinear wave mechanics.* Annals of Physics **100** (1976), 62–93.
- **[Foundational]** T. Cazenave, A. Haraux. *Équations d'évolution avec non linéarité logarithmique.* Annales de la Faculté des Sciences de Toulouse Math. (5) **2** (1980), 21–51.
- **[Foundational]** T. Cazenave. *Stable solutions of the logarithmic Schrödinger equation.* Nonlinear Analysis TMA **7** (1983), 1127–1140.
- **[Foundational]** P. Blanchard, J. Stubbe, L. Vázquez. *On the stability of solitary waves for classical scalar fields.* Annales de l'IHP, Physique Théorique **47** (1987), 309–336.
- **[SOTA]** R. Carles, I. Gallagher. *Universal dynamics for the defocusing logarithmic Schrödinger equation.* Duke Mathematical Journal **167** (2018), no. 9, 1761–1801.
- **[SOTA]** G. Ferriere. *Convergence rate in Wasserstein distance and semiclassical limit for the defocusing logarithmic Schrödinger equation.* Analysis & PDE **14** (2021), 617–666.
- **[SOTA]** G. Ferriere. *The focusing logarithmic Schrödinger equation: analysis of breathers and nonlinear superposition.* Discrete and Continuous Dynamical Systems **40** (2020), 6247–6274.
- **[SOTA]** R. Carles, G. Ferriere. *Logarithmic Schrödinger equation with quadratic potential.* Nonlinearity **34** (2021), 8283–8310.
- **[Numerics]** W. Bao, R. Carles, C. Su, Q. Tang. *Error estimates of a regularized finite difference method for the logarithmic Schrödinger equation.* SIAM Journal on Numerical Analysis **57** (2019), 657–680.
- **[Variational]** P. d'Avenia, E. Montefusco, M. Squassina. *On the logarithmic Schrödinger equation.* Communications in Contemporary Mathematics **16** (2014), 1350032.
- **[Stability]** A. H. Ardila. *Orbital stability of Gausson solutions to logarithmic Schrödinger equations.* Electronic Journal of Differential Equations, 2016.
- **[Survey]** R. Carles. *Logarithmic Schrödinger equation and isothermal fluids.* EMS Surveys in Mathematical Sciences **9** (2022), 99–134.
- **[Book]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes 10, AMS, 2003.

## 10. Worked Example / Concrete Special Case

**Exact Gaussian solution and the $\sqrt{\ln t}$ rate, $\lambda>0$, any $d\ge1$.**

Take $u_0(x)=e^{-|x|^2/2}$ and seek
$$u(t,x)=\frac{1}{\tau(t)^{d/2}}\exp\!\Big(i\phi(t)+i\frac{\dot\tau(t)}{2\tau(t)}|x|^2-\frac{|x|^2}{2\tau(t)^2}\Big).$$

Insert into $i\partial_t u+\frac12\Delta u=\lambda u\ln|u|^2$. Matching the coefficients of $|x|^2$ gives the **Ermakov-type ODE**
$$\ddot\tau=\frac{4\lambda}{\tau},\qquad \tau(0)=1,\ \dot\tau(0)=0,$$
and matching the $x$-independent terms fixes $\dot\phi=-\frac{d}{2}\frac{\dot\tau}{\tau}\cdot 0 - \lambda\big(d\ln\tau^{-1}\big)+\ldots$, i.e. $\phi$ is determined by a quadrature in $\tau$. Note the ODE is **independent of $d$** — a purely logarithmic feature.

Multiply by $\dot\tau$ and integrate:
$$\frac{d}{dt}\Big(\frac{\dot\tau^2}{2}\Big)=4\lambda\frac{\dot\tau}{\tau}=\frac{d}{dt}\big(4\lambda\ln\tau\big) \quad\Longrightarrow\quad \dot\tau^2=8\lambda\ln\tau .$$

Since $\lambda>0$ and $\ddot\tau(0)=4\lambda>0$, $\tau$ increases and $\dot\tau=2\sqrt{2\lambda\ln\tau}\to\infty$. Writing $\tau=t\,\sigma(t)$ with $\sigma$ slowly varying, $\ln\tau=\ln t(1+o(1))$, so $\dot\tau\sim 2\sqrt{2\lambda\ln t}$ and integrating,
$$\boxed{\ \tau(t)\sim 2t\sqrt{2\lambda\ln t}\ },\qquad t\to\infty.$$

Therefore
$$\|u(t)\|_{L^\infty}=\tau(t)^{-d/2}\sim\big(2\sqrt{2\lambda}\big)^{-d/2}\,\big(t\sqrt{\ln t}\big)^{-d/2},$$
strictly faster than the free Schrödinger rate $t^{-d/2}$ by $(\ln t)^{-d/4}$. Rescaling, $\tau^d|u(t,\tau y)|^2=e^{-|y|^2}$ exactly — the universal profile, here visible with no analysis at all.

**Contrast, $\lambda<0$.** Then $\dot\tau^2=8\lambda\ln\tau=-8|\lambda|\ln\tau$ forces $\tau\le 1$, and $\tau$ oscillates periodically between $\tau_{\min}=e^{-\dot\tau_{\max}^2/(8|\lambda|)}$-type turning points: the solution is a breather, $\|u(t)\|_{L^\infty}=\tau(t)^{-d/2}$ never decays, and $\tau\equiv1$ (achieved by choosing the Gausson amplitude) gives the stationary Gausson. **This is the entire difficulty of item (4) in Section 1 in one line: the sign of $\lambda$ flips the ODE from escape to libration, and no known argument controls which of the two behaviours a general non-Gaussian focusing datum selects.**

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*