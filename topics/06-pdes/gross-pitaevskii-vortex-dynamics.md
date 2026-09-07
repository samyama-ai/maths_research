---
id: 06-pdes/gross-pitaevskii-vortex-dynamics
title: "Gross Pitaevskii Vortex Dynamics"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gross–Pitaevskii Vortex Dynamics

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/gross-pitaevskii-vortex-dynamics` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Gross–Pitaevskii (GP) equation on $\mathbb{R}^d$ or a bounded domain $\Omega\subset\mathbb{R}^d$,
$$i\,\partial_t u_\varepsilon \;=\; \Delta u_\varepsilon + \frac{1}{\varepsilon^2}\,u_\varepsilon\big(1-|u_\varepsilon|^2\big),\qquad u_\varepsilon:\Omega\times[0,\infty)\to\mathbb{C},$$
where $\varepsilon>0$ is the healing length (vortex core radius). Zeros of $u_\varepsilon$ carry a quantized topological degree; as $\varepsilon\to 0$ they concentrate on points ($d=2$) or curves ($d=3$).

**The conjecture (asymptotic vortex motion law).** If the initial data are well prepared with $n$ vortices of degrees $d_j\in\mathbb{Z}\setminus\{0\}$ at distinct points $a_j^0\in\Omega$, then for all time before a collision the vortices $a_j(t)$ follow the **Kirchhoff–Onsager point-vortex system**
$$d_j\,\dot a_j(t) \;=\; \frac{1}{\pi}\,J\,\nabla_{a_j} W\big(a_1,\dots,a_n\big),\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},$$
$$W(a) \;=\; -\pi\sum_{i\neq j} d_i d_j \log|a_i-a_j| \;+\; \text{(boundary/renormalization terms)} .$$
In $d=3$, after rescaling time by $|\log\varepsilon|$, each vortex filament $\gamma(\cdot,t)$ should evolve by **binormal curvature flow** $\partial_t\gamma=\kappa\, b$.

**What a full resolution requires.** (i) A proof valid for *general finite-energy initial data*, not merely well-prepared data; (ii) a proof valid *past collision and reconnection times*, including a selection principle saying which configuration emerges after two vortices merge or two filaments reconnect; (iii) in $d=3$, a proof for arbitrary (non-nearly-parallel, non-smooth) filament configurations, including the passage through curvature blow-up. All three remain open.

## 2. Mathematical Foundations

**Energy.** The GP energy is
$$E_\varepsilon(u) \;=\; \int_\Omega \frac{|\nabla u|^2}{2} + \frac{(1-|u|^2)^2}{4\varepsilon^2}\,dx .$$
It is conserved by the flow, which is the Hamiltonian system $\partial_t u = -i\,\delta E_\varepsilon/\delta \bar u$ for the symplectic form $\omega(u,v)=\int \operatorname{Im}(u\bar v)$.

**Vorticity and Jacobian.** For $u\neq 0$ write $u=\rho e^{i\varphi}$. Define the current and the Jacobian
$$j(u) \;=\; \operatorname{Im}(\bar u\,\nabla u),\qquad Ju \;=\; \tfrac12\,\nabla\times j(u)\;=\;\det(\nabla u)\ \ (d=2).$$
The Jacobian is the natural weak vorticity: for a vortex configuration $\sum_j d_j\delta_{a_j}$ one has $Ju \rightharpoonup \pi\sum_j d_j\delta_{a_j}$ in $(C^{0,1}_c)^*$.

**Energy quantization (Bethuel–Brezis–Hélein).** For a degree-$d$ configuration in a disc of radius $R$,
$$E_\varepsilon \;=\; \pi\Big(\sum_j |d_j|\Big)\log\frac{1}{\varepsilon} \;+\; W(a) \;+\; n\gamma \;+\; o_\varepsilon(1),$$
with $\gamma$ the core energy of the standard degree-$\pm1$ profile $u=f(r)e^{\pm i\theta}$, $f$ solving $f''+f'/r-f/r^2+\varepsilon^{-2}f(1-f^2)=0$, $f(0)=0$, $f(\infty)=1$.

**Renormalized energy.** $W$ above is the Bethuel–Brezis–Hélein renormalized energy; on $\mathbb{R}^2$ with total degree zero it reduces to $-\pi\sum_{i\neq j}d_id_j\log|a_i-a_j|$.

**Kirchhoff–Onsager system.** With $H(a)=W(a)$ and symplectic weights $\pi d_j$, the motion law is the Hamiltonian flow of $W$; it conserves $W$, the total momentum $\sum d_j a_j$ and the angular impulse $\sum d_j|a_j|^2$.

**Scaling.** GP vortices move at $O(1)$ speed (dispersive/Hamiltonian scaling), in contrast to the parabolic Ginzburg–Landau flow where the correct time scale is $|\log\varepsilon|$. In $d=3$, filament self-induction carries a $\log$ divergence, so the binormal flow appears only after rescaling $t\mapsto t|\log\varepsilon|$.

**Compatibility constraint.** Finite-energy data on $\mathbb{R}^2$ forces total degree $\sum_j d_j = 0$; nonzero total degree requires infinite energy and the renormalized framework of Bethuel–Jerrard–Smets.

## 3. History & State of the Art (SOTA)

- **1961.** Gross and Pitaevskii independently derive the equation as the mean-field model for a dilute Bose–Einstein condensate.
- **1949/1867.** Onsager's point-vortex statistics and Kirchhoff's law provide the conjectured limit dynamics; Kelvin/Da Rios (1906) give the binormal flow for filaments.
- **1982.** Jones and Roberts compute the travelling-wave branch of GP in 2D and 3D numerically, identifying the vortex dipole and vortex-ring solutions.
- **1994.** Bethuel–Brezis–Hélein's monograph *Ginzburg–Landau Vortices* establishes the static $\pi|\log\varepsilon|$ expansion and the renormalized energy, the analytic backbone for all dynamic results.
- **1998.** Colliander–Jerrard (IMRN) give the first rigorous derivation of the point-vortex law for GP on the torus with well-prepared data, using the Jacobian/current framework.
- **1999.** Lin–Xin (Comm. Math. Phys.) prove the motion law on bounded domains and on $\mathbb{R}^2$, via a modulated-energy/Pohozaev argument.
- **2002.** Jerrard (Ann. SNS Pisa) derives binormal curvature flow for GP filaments in $\mathbb{R}^3$ under a priori smoothness assumptions.
- **2008.** Jerrard–Spirn (ARMA) prove the motion law with *quantitative* error rates using refined Jacobian estimates, allowing much rougher (non-well-prepared) initial data.
- **2008–2015.** Bethuel–Jerrard–Smets treat infinite-energy configurations; Jerrard–Smets establish existence of weak binormal-flow solutions through singularities (JEMS 2015) and treat inhomogeneous GP.
- **2017.** Serfaty (JAMS) derives mean-field limits for GP with $n\to\infty$ vortices, yielding the incompressible Euler equation in vorticity form.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| $d=2$, well-prepared data, $\Omega=\mathbb{T}^2$ or bounded | Kirchhoff–Onsager law holds up to first collision time $T_c$ | Colliander–Jerrard 1998 |
| $d=2$, $\mathbb{R}^2$ and bounded domains, finite energy, $\sum d_j=0$ | Motion law, modulated energy method | Lin–Xin 1999 |
| $d=2$, degrees $d_j=\pm1$, energy excess $\le C\varepsilon^{\alpha}$ | Motion law with explicit error $O(\varepsilon^{\alpha}|\log\varepsilon|^{c})$, valid on $[0,T_c)$ | Jerrard–Spirn 2008 |
| $d=2$, infinite energy, $\sum d_j \neq 0$ | Motion law in a renormalized sense | Bethuel–Jerrard–Smets 2008 |
| $d=2$, critically scaled inhomogeneity (pinning potential) | Modified law with pinning force term | Kurzke–Marzuola–Spirn 2017 |
| $d=3$, single filament, a priori $C^{1,1}$ bounds on the limit curve | Binormal curvature flow on $[0,T]$ | Jerrard 2002 |
| $d=3$, nearly parallel filaments, Ginzburg–Landau | Klein–Majda–Damodaran system rigorously derived | Contreras–Jerrard 2017 |
| $d=3$, binormal flow itself | Weak measure-valued solutions exist globally, including through corner formation | Jerrard–Smets 2015 |
| $n\to\infty$ vortices, mean field | Convergence to 2D incompressible Euler | Serfaty 2017 |
| Explicit solutions | Rotating vortex pairs, translating dipoles, vortex rings, helices | Jones–Roberts 1982; Bethuel–Orlandi–Smets 2004; Chiron 2005 |

Uniformly across these: **the constraint $t < T_c$ (first collision) is present in every 2D theorem**, and every 3D theorem assumes either near-parallelism or a priori regularity of the limit filament.

## 5. Principal Obstacles

- **Loss of energy quantization at collision.** The expansion $E_\varepsilon=\pi\sum|d_j|\,|\log\varepsilon|+W+O(1)$ degenerates when $|a_i-a_j|\to 0$: $W\to\pm\infty$ at rate $\log|a_i-a_j|$, which is comparable to the leading term once $|a_i-a_j|\sim\varepsilon^{\beta}$. All compactness arguments for the Jacobian break down exactly there.
- **No dissipation to select the outcome.** In the parabolic Ginzburg–Landau flow, energy decrease forces a unique post-collision configuration (Bethuel–Orlandi–Smets 2005). GP conserves energy, so the excess released in a $(+1,-1)$ annihilation is radiated as dispersive sound waves. Controlling that radiation requires quantitative dispersive estimates for a *variable-coefficient, non-perturbative* linearization around a vortex, which are not available.
- **Failure of perturbation theory.** The linearized operator around a vortex has an $L^2$ zero mode (translation) plus continuous spectrum reaching the origin; the modulation ansatz $u\approx \prod_j f(|x-a_j|)e^{id_j\theta_j}$ has $H^1$ error of size $|\log\varepsilon|^{-1/2}$ only, too large to close a Grönwall estimate over $O(1)$ times without the Jacobian machinery.
- **Fourier analysis is blocked by the topology.** GP has non-decaying boundary condition $|u|\to1$; the phase $\varphi$ is not globally defined, so linear dispersive estimates and Strichartz theory apply only to the modulus/hydrodynamic variables, not to the vortex data.
- **3D filaments: curvature blow-up.** Binormal flow develops corners in finite time (self-similar solutions of Gutiérrez–Rivas–Vega). Beyond that time the limit object is only a measure, and the Jerrard–Smets weak solutions are non-unique. So even the *limit equation* lacks a well-posedness theory to converge to.
- **Reconnection has no rigorous existence proof.** Numerical (Koplik–Levine 1993) and experimental evidence for GP filament reconnection is strong, but no theorem produces a solution that changes filament topology.

## 6. The Gap

Precisely: all theorems hold on $[0,T_c)$ where $T_c$ is the first collision/reconnection time of the *limit* system, with error estimates that blow up like a power of $\min_{i\neq j}|a_i(t)-a_j(t)|^{-1}$. The conjecture asserts the law on $[0,\infty)$ with a defined continuation past $T_c$. Crossing the gap requires:

1. A **uniform-in-$\varepsilon$ lower bound on vortex separation**, or an alternative: a quantitative description of the collision layer at scale $|a_i-a_j|\sim\varepsilon$.
2. An **energy-partition theorem** splitting $E_\varepsilon$ into vortex energy plus radiated sound, with a bound on the radiation rate; currently no such splitting is known to be stable under GP flow.
3. In 3D, a **selection principle for weak binormal flow** singling out the physically correct continuation past corner formation.

## 7. Current Research (as of June 2026)

- **Quantitative Jacobian and modulated-energy methods.** Continuation of the Jerrard–Spirn program, pushing error rates toward the collision scale; Serfaty-school modulated-energy techniques adapted from Coulomb-gas dynamics. *(frontier — verify)* Refinements claiming error control down to separations $\varepsilon^{1-\delta}$ have circulated as preprints.
- **Mean-field / Euler limit.** Extensions of Serfaty (2017) to $n=n(\varepsilon)\to\infty$ with mixed signs, and to the compressible/Euler–Korteweg regime.
- **Weak binormal flow and reconnection.** Groups in Paris (Sorbonne / IHÉS), Bilbao (BCAM — Vega and collaborators on self-similar and knotted binormal solutions), and Toronto (Jerrard) study post-singularity continuation.
- **Numerics.** High-order time-splitting spectral schemes (Bao and collaborators) resolve reconnection at $\varepsilon\sim10^{-3}$ and match the binormal law away from reconnection; discrepancy in the reconnection exponent $|t-t_*|^{1/2}$ prefactor remains under study. *(frontier — verify)*
- **Physics interface.** BEC experiments imaging vortex-lattice dynamics and turbulent vortex tangles give quantitative tests of the Kirchhoff law and of reconnection statistics.

## 8. Future Work

- Prove a **no-collapse** theorem: for $(+1,+1)$ configurations show separation is bounded below on $[0,T]$ uniformly in $\varepsilon$ (plausible via conservation of angular impulse plus a Lyapunov argument on $W$).
- Establish **asymptotic stability of the single vortex** in a topologically nontrivial energy space; this is the missing dispersive ingredient for radiation control.
- Derive a **dissipative effective law** capturing the radiation loss at collision (an "$\varepsilon$-regularized Kirchhoff system") and prove convergence to it.
- Prove existence of a GP solution exhibiting **filament reconnection**, even for one symmetric configuration.
- Identify a **uniqueness class for binormal flow** through corners, e.g. via the Hasimoto transform and the 1D cubic NLS with $\delta$-type data.

## 9. Key References

- **[Foundational]** F. Bethuel, H. Brezis, F. Hélein. *Ginzburg–Landau Vortices.* Birkhäuser, Progress in Nonlinear Differential Equations and Their Applications 13, 1994.
- **[Foundational]** J. E. Colliander, R. L. Jerrard. *Vortex dynamics for the Ginzburg–Landau–Schrödinger equation.* International Mathematics Research Notices, 1998, no. 7, 333–358.
- **[Foundational]** F.-H. Lin, J. X. Xin. *On the incompressible fluid limit and the vortex motion law of the nonlinear Schrödinger equation.* Communications in Mathematical Physics 200 (1999), 249–274.
- **[Foundational]** C. A. Jones, P. H. Roberts. *Motions in a Bose condensate IV: Axisymmetric solitary waves.* Journal of Physics A: Mathematical and General 15 (1982), 2599–2619.
- **[SOTA / Recent]** R. L. Jerrard, D. Spirn. *Refined Jacobian estimates and Gross–Pitaevskii vortex dynamics.* Archive for Rational Mechanics and Analysis 190 (2008), 425–475.
- **[SOTA / Recent]** R. L. Jerrard. *Vortex filament dynamics for Gross–Pitaevskii type equations.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. (5) 1 (2002), 733–768.
- **[SOTA / Recent]** R. L. Jerrard, D. Smets. *On the motion of a curve by its binormal curvature.* Journal of the European Mathematical Society 17 (2015), 1487–1515.
- **[SOTA / Recent]** F. Bethuel, R. L. Jerrard, D. Smets. *On the NLS dynamics for infinite energy vortex configurations on the plane.* Revista Matemática Iberoamericana 24 (2008), 671–702.
- **[SOTA / Recent]** S. Serfaty. *Mean field limits of the Gross–Pitaevskii and parabolic Ginzburg–Landau equations.* Journal of the American Mathematical Society 30 (2017), 713–768.
- **[SOTA / Recent]** A. Contreras, R. L. Jerrard. *Nearly parallel vortex filaments in the 3D Ginzburg–Landau equations.* Geometric and Functional Analysis 27 (2017), 1161–1230.
- **[SOTA / Recent]** M. Kurzke, J. L. Marzuola, D. Spirn. *Gross–Pitaevskii vortex motion with critically-scaled inhomogeneities.* SIAM Journal on Mathematical Analysis 49 (2017), 471–500.
- **[Survey]** F. Bethuel, P. Gravejat, J.-C. Saut. *Existence and properties of travelling waves for the Gross–Pitaevskii equation.* In *Stationary and Time Dependent Gross–Pitaevskii Equations*, Contemporary Mathematics 473, AMS, 2008, 55–103.
- **[Survey]** L. Pitaevskii, S. Stringari. *Bose–Einstein Condensation and Superfluidity.* Oxford University Press, 2016.
- **[Numerics]** W. Bao, Q. Du, Y. Zhang. *Dynamics of rotating Bose–Einstein condensates and their efficient and accurate numerical computation.* SIAM Journal on Applied Mathematics 66 (2006), 758–786.
- **[Numerics]** J. Koplik, H. Levine. *Vortex reconnection in superfluid helium.* Physical Review Letters 71 (1993), 1375–1378.

## 10. Worked Example / Concrete Special Case

**Two co-rotating vortices in $\mathbb{R}^2$.** Take $d_1=d_2=+1$ with initial positions $a_1^0=(\tfrac{D}{2},0)$, $a_2^0=(-\tfrac{D}{2},0)$, and use the renormalized energy on the plane,
$$W(a_1,a_2) \;=\; -\pi\sum_{i\neq j} d_i d_j\log|a_i-a_j| \;=\; -2\pi\log|a_1-a_2|.$$

Then $\nabla_{a_1}W = -2\pi\dfrac{a_1-a_2}{|a_1-a_2|^2}$, and the motion law $d_1\dot a_1 = \frac{1}{\pi}J\nabla_{a_1}W$ gives
$$\dot a_1 \;=\; -\frac{2}{|a_1-a_2|^{2}}\,J\,(a_1-a_2),\qquad \dot a_2 \;=\; -\frac{2}{|a_1-a_2|^{2}}\,J\,(a_2-a_1).$$

**Separation is conserved.** With $r=a_1-a_2$, $\dot r = -\frac{4}{|r|^2}Jr$, so
$$\frac{d}{dt}|r|^2 \;=\; 2\,r\cdot\dot r \;=\; -\frac{8}{|r|^{2}}\;r\cdot Jr \;=\;0,$$
since $J$ is antisymmetric. Hence $|r(t)|\equiv D$ for all time.

**Explicit trajectory.** Substituting $|r|=D$: $\dot r = -\frac{4}{D^2}Jr$, a linear rotation. Each vortex traces a circle of radius $D/2$ about the centroid $\frac{a_1+a_2}{2}=0$ with angular velocity
$$\omega \;=\; \frac{4}{D^{2}},\qquad \text{period } T \;=\; \frac{2\pi}{\omega} \;=\; \frac{\pi D^{2}}{2},$$
and orbital speed $|\dot a_j| = \omega\,\tfrac{D}{2} = 2/D$. (The sense of rotation flips with the sign convention for $J$; the physical pair co-rotates.)

**What the theorems give and where they stop.** Jerrard–Spirn (2008) show that if $u_\varepsilon^0$ has two degree-$+1$ vortices at $a_j^0$ with energy excess $E_\varepsilon(u^0_\varepsilon)-2\pi|\log\varepsilon|-W(a^0)-2\gamma \le \varepsilon^\alpha$, then
$$\sup_{t\in[0,T]}\Big|\,\pi^{-1}Ju_\varepsilon(t)-\textstyle\sum_j \delta_{a_j(t)}\Big|_{(C^{0,1}_c)^*} \;\longrightarrow\; 0$$
with $a_j(t)$ the circular orbits above, for every $T<\infty$ — here $T_c=+\infty$ because separation is conserved. This case is therefore *fully solved*.

**The unsolved variant.** Change $d_2$ to $-1$. Then $W=+2\pi\log|a_1-a_2|$ and the pair translates rigidly at speed $2/D$ perpendicular to $r$ — the Jones–Roberts dipole, again with $T_c=\infty$. But perturb the dipole so the two vortices approach: the limit ODE has $|r|\to0$ in finite time $T_c$, $W\to-\infty$, and no theorem describes $u_\varepsilon$ for $t>T_c$. Numerically the pair annihilates into an outgoing sound pulse carrying the released energy $\approx 2\pi|\log\varepsilon|$. Proving that — and identifying the emergent solution — is the open core of the problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*