---
id: 06-pdes/kuramoto-sivashinsky-attractor
title: "Kuramoto Sivashinsky Attractor"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kuramoto–Sivashinsky Attractor: Extensivity of the Global Attractor

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kuramoto-sivashinsky-attractor` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Kuramoto–Sivashinsky (KS) equation on the periodic interval $[0,L]$,

$$u_t + u_{xxxx} + u_{xx} + u u_x = 0, \qquad x \in \mathbb{T}_L = \mathbb{R}/L\mathbb{Z},\quad t>0,$$

with mean-zero initial data. The equation has a compact global attractor $\mathcal{A}_L \subset \dot{L}^2(\mathbb{T}_L)$. The problem is to determine the **exact scaling in $L$** of two quantities:

1. **(Amplitude / turbulence conjecture)** The attractor's size in $L^2$:
$$\limsup_{t\to\infty}\|u(\cdot,t)\|_{L^2(\mathbb{T}_L)} \;\overset{?}{\lesssim}\; L^{1/2},$$
equivalently, the spatial root-mean-square amplitude $L^{-1/2}\|u\|_{L^2}$ stays bounded uniformly in $L$. This is the statement that KS turbulence is **extensive**: energy is proportional to system size, with an $L$-independent energy density.

2. **(Dimension conjecture)** The fractal (and Hausdorff) dimension of the attractor:
$$\dim_f \mathcal{A}_L \;\overset{?}{\asymp}\; L,$$
i.e. $c_1 L \le \dim_f\mathcal{A}_L \le c_2 L$ for absolute constants $0<c_1\le c_2$, matching the number of linearly unstable Fourier modes.

A complete resolution means proving both upper bounds ($O(L^{1/2})$ for the norm, $O(L)$ for the dimension) with constants independent of $L$ and of the initial data, or exhibiting a family of solutions violating them. Both statements are supported by extensive numerics and by physical (extensive-chaos) heuristics; neither is proven.

A closely related open problem: **global well-posedness of the 2D KS equation** $u_t + \Delta^2 u + \Delta u + \tfrac12|\nabla u|^2 = 0$ on $\mathbb{T}^2$, where even existence of a global attractor is unknown for general data.

## 2. Mathematical Foundations

**Derivative form.** Setting $u = \phi_x$ gives the "integrated" KS equation $\phi_t + \phi_{xxxx} + \phi_{xx} + \tfrac12\phi_x^2 = 0$, a model for flame-front position and for thin-film flow down an inclined plane.

**Scaling.** Under $x \mapsto Lx/2\pi$, $t\mapsto (L/2\pi)^4 t$, $u \mapsto (2\pi/L) u$, KS on $[0,L]$ maps to $u_t + u_{xxxx} + \nu u_{xx} + uu_x=0$ on $[0,2\pi]$ with $\nu = (L/2\pi)^2$. Thus large domain $\equiv$ small viscosity-like parameter; $L$ is the only parameter.

**Linear spectrum.** For $u = \sum_{k\in\frac{2\pi}{L}\mathbb{Z}} \hat u_k e^{ikx}$, the linearization about $u\equiv0$ has growth rate
$$\sigma(k) = k^2 - k^4,$$
so modes with $0<|k|<1$ grow, the most unstable wavenumber is $k_\ast = 1/\sqrt2$ (rate $1/4$), and $|k|>1$ modes are strongly damped. The number of unstable modes is $\lfloor L/2\pi \rfloor$, growing linearly in $L$ — the source of the $\dim\mathcal{A}_L \asymp L$ heuristic.

**Energy identity.** Since $\int u^2 u_x\,dx = 0$, the nonlinearity is conservative and
$$\frac{d}{dt}\tfrac12\|u\|_{L^2}^2 = \|u_x\|_{L^2}^2 - \|u_{xx}\|_{L^2}^2 .$$
The RHS is negative for all Fourier content at $|k|>1$, but is not sign-definite: energy is pumped at large scales and dissipated at small scales, and only the nonlinearity transfers it. This is the entire difficulty.

**Background-flow (Lyapunov) method.** Write $u = v + \Phi$ for a fixed "background" profile $\Phi(x)$. Then
$$\frac{d}{dt}\tfrac12\|v\|^2 = -\|v_{xx}\|^2 + \|v_x\|^2 - \int \Phi' \tfrac{v^2}{2} + \text{(linear in }v)\,,$$
and one seeks $\Phi$ with $\Phi' \ge$ some threshold making the quadratic form coercive. Nicolaenko–Scheurer–Temam used $\Phi$ built from the solution's own structure in the odd (Galilean-symmetric) subspace; later work used more delicate multiscale choices.

**Attractor and dimension.** $\mathcal{A}_L = \bigcap_{t\ge0} S(t)\,\mathcal{B}$ where $S(t)$ is the semigroup and $\mathcal{B}$ an absorbing ball. Upper bounds on $\dim_f\mathcal{A}_L$ come from the Constantin–Foias–Temam trace formula: if the sum of the first $m$ global Lyapunov exponents, $q_m = \limsup \sup_{u\in\mathcal{A}}\frac1t\int_0^t \mathrm{Tr}\,(P_m\,DF(u)\,P_m)$, is negative, then $\dim_f\mathcal{A}\le m$. Bounding $\mathrm{Tr}$ requires a Lieb–Thirring inequality plus control of $\|u\|_{L^2}$ — so the dimension bound is downstream of the amplitude bound.

**Inertial manifold.** KS admits an inertial manifold $\mathcal{M}$ (finite-dimensional, exponentially attracting, Lipschitz, containing $\mathcal{A}$) via the spectral-gap condition for $\partial_x^4$ — proven by Foias–Nicolaenko–Sell–Temam (1988). Its dimension bounds $\dim\mathcal{A}$ from above but is currently super-linear in $L$.

## 3. History & State of the Art (SOTA)

- **1976–1977.** Kuramoto (with Tsuzuki) derived the equation for phase turbulence in reaction–diffusion systems; Sivashinsky derived it independently for hydrodynamic flame-front instability.
- **1985.** Nicolaenko, Scheurer, Temam: first global bound, for odd solutions, $\limsup\|u\|_{L^2} \lesssim L^{5/2}$, and existence of the attractor with $\dim_f \lesssim L^{2.5}$.
- **1988.** Foias, Nicolaenko, Sell, Temam: inertial manifolds for KS; reduction to a finite-dimensional ODE system.
- **1992–1993.** Il'yashenko removed the odd-symmetry restriction ($L^2$-bound $\lesssim L^{2}$ in a suitable normalization); Collet–Eckmann–Epstein–Stubbe obtained $\limsup\|u\|_{L^2} \lesssim L^{8/5}$ for general periodic data and proved analyticity of solutions on the attractor with a uniform strip width.
- **1994.** Goodman gave a short energy proof recovering $L^{5/2}$ with the background-flow trick, making the method transparent. Temam–Wang: $\dim_f\mathcal{A}_L = O(L^{1.64})$ in the general (non-odd) case.
- **2006.** Bronski–Gambill: $\limsup\|u\|_{L^2}\lesssim L^{3/2}$ via an optimized background profile — the best power-law bound by pure Lyapunov-function methods.
- **2005–2015.** Giacomelli–Otto proved $o(L^{3/2})$, breaking the power barrier; Otto (2009) and Goldman–Josien–Otto (2015) obtained near-optimal (logarithmic-loss) bounds for the closely related **inhomogeneous Burgers** model and for weaker/averaged norms of KS.
- **2018–2024.** Ambrose–Mazzucato: analyticity radii and 2D KS on thin domains and with anisotropic scaling; Feng–Mazzucato and Coti Zelati–Dolce–Feng–Mazzucato: global existence for 2D KS with advection by a shear flow (enhanced dissipation).

**Numerical SOTA.** Direct simulation robustly shows $L^{-1/2}\|u\|_{L^2}\to$ const $\approx 1.2$ and Lyapunov-dimension density $\dim/L \approx 0.07$–$0.09$ as $L\to\infty$, with a spatial correlation length independent of $L$ — the empirical case for extensivity.

## 4. Partial Results / Verified Cases

- **Odd subspace, all $L$:** $\limsup\|u\|_{L^2}\lesssim L^{5/2}$ (Nicolaenko–Scheurer–Temam 1985; Goodman 1994).
- **General periodic data, all $L$:** $\limsup\|u\|_{L^2}\lesssim L^{3/2}$ (Bronski–Gambill 2006), improved to $o(L^{3/2})$ with a quantitative logarithmic gain (Giacomelli–Otto 2005; Goldman–Josien–Otto 2015). Conjectured exponent $1/2$; proven exponent $3/2$ — a gap of $L$.
- **Attractor dimension:** $\dim_f\mathcal{A}_L = O(L^{1.64})$ (Temam–Wang 1994) and $O(L^{1.5+})$ following from the sharpened norm bounds. Lower bound $\dim\mathcal{A}_L \ge c L$ from counting unstable eigenvalues of $\sigma(k)=k^2-k^4$ at the fixed point $u\equiv 0$ (dimension of its unstable manifold $= 2\lfloor L/2\pi\rfloor$ minus symmetry directions).
- **Small $L$ (rigorous, complete):** for $L<2\pi$ the zero solution is globally asymptotically stable and $\mathcal{A}_L=\{0\}$; the first bifurcation is at $L=2\pi$. For $L$ up to roughly $13$, the bifurcation diagram (steady states, travelling waves, first period-doubling cascades) is known essentially completely by rigorous computer-assisted continuation.
- **Computer-assisted proofs:** existence and stability of specific periodic orbits and heteroclinic connections at $L\approx 38.5$ (Cvitanović and collaborators; Zgliczyński–Mischaikow-type rigorous interval-arithmetic proofs for the Galerkin truncation with rigorous tail estimates).
- **Anisotropic / stabilized 2D cases:** global existence for 2D KS on thin domains, with growing shear advection, or with the destabilizing term restricted to one direction.

## 5. Principal Obstacles

- **No conserved sign structure.** The nonlinearity $uu_x$ is $L^2$-orthogonal to $u$, so it contributes nothing to the energy identity — yet the entire conjecture is that it is exactly what saturates the linear instability by transferring energy to $|k|>1$. Any proof must extract a *quantitative* transfer estimate from a term that is invisible in the energy budget.
- **Background-flow saturation.** Lyapunov/background methods bound $\|u\|$ by the size of the profile $\Phi$ needed for coercivity; the best admissible $\Phi$ has $\|\Phi\|_{L^2}\sim L^{3/2}$. Bronski–Gambill showed this is *optimal for the method*: no choice of $\Phi$ in that framework yields $L^{1/2}$. The obstruction is that coercivity is demanded pointwise in time, whereas the true mechanism is time-averaged.
- **Galilean invariance and mean drift.** KS is invariant under $u\mapsto u+c$, $x \mapsto x-ct$; the mean-zero constraint is preserved but "local means" over subintervals drift, so localized versions of the energy estimate lose control.
- **No maximum principle, no comparison.** Fourth-order operator: no positivity, no Harnack, so parabolic regularity arguments used for Navier–Stokes-type scalar models are unavailable.
- **Dimension bounds inherit the norm gap.** The Lieb–Thirring trace estimate produces $\dim_f \lesssim L\cdot(L^{-1/2}\|u\|_{L^2})^{\alpha}$-type expressions; with $\|u\|\lesssim L^{3/2}$ the bound degrades to $L^{1.5}$–$L^{1.64}$. Even a sharp $L^{1/2}$ amplitude bound would give $\dim \lesssim L$ only with a further sharp Lieb–Thirring constant.
- **2D:** the analogue of the 1D "$\|u\|_{L^\infty}$ controls everything" scaling fails; global existence is open even without asking about attractors.

## 6. The Gap

Proven: $\limsup_t\|u\|_{L^2} \le C L^{3/2-\epsilon(L)}$ with $\epsilon(L)\to 0$ logarithmically. Conjectured: $\le C L^{1/2}$. The gap is a full factor of $L$ in the norm, and roughly $L^{0.5}$–$L^{0.64}$ in the attractor dimension.

The precise missing step: a rigorous, $L$-uniform statement that the nonlinear flux
$$\Pi(k_0) = \Big\langle \sum_{|k|>k_0} \overline{\hat u_k}\,\widehat{(uu_x)}_k \Big\rangle$$
transports the large-scale energy input $\langle\|u_x\|^2\rangle$ into the dissipation range at a rate matching the linear pumping, *on average in time* rather than instantaneously. Equivalently: a coercive functional adapted to space–time averages replacing the pointwise-in-time background profile. Otto's program achieves exactly this for the inhomogeneous Burgers surrogate $u_t + uu_x = f$ with $f$ concentrated at large scales; the missing piece is handling the genuine feedback in which $f$ is $-(\partial_x^4+\partial_x^2)u$ determined by $u$ itself.

## 7. Current Research (as of June 2026)

- **Otto school (Leipzig, MPI MiS).** Continuation of the "shocks and entropy" program: KS solutions on the attractor look like arrays of sawtooth shocks; the aim is a rigorous shock-counting argument giving amplitude $O(L^{1/2})$. Refinements of Goldman–Josien–Otto to the full KS feedback are the live target *(frontier — verify)*.
- **Mazzucato, Ambrose and collaborators (Penn State, Drexel).** 2D KS: global existence under advection, anisotropic dissipation, thin domains; analyticity radii and their $L$-dependence.
- **Bronski, Gambill and dynamical-systems groups (Illinois).** Sharper Lyapunov functionals and variational lower bounds on what any background-flow method can give.
- **Cvitanović-style periodic-orbit theory (Georgia Tech, Warwick, Kraków).** Rigorous computer-assisted classification of unstable periodic orbits at moderate $L$ ($L\lesssim 100$) and cycle-expansion computation of attractor measures and dimensions; interval-arithmetic proofs (Zgliczyński, Wilczak) of orbits and connections.
- **Data-driven / learned reduced models.** Neural-network and Koopman approximations of the KS inertial manifold, used to estimate its minimal dimension numerically; these are heuristic but sharpen conjectures about $\dim\mathcal{A}_L/L$ *(frontier — verify)*.
- **Control and stabilization.** Feedback stabilization of KS with boundary/interior control, and KS with additive noise (stochastic KS invariant measures, extensivity of the measure).

## 8. Future Work

- Prove a **time-averaged flux inequality** for KS by transplanting Otto's inhomogeneous-Burgers machinery, treating $-(\partial_x^4+\partial_x^2)u$ as a controlled forcing via a bootstrap on the dissipation.
- Establish the **sawtooth/shock structure** of attractor states rigorously: show that on $\mathcal{A}_L$, $u$ is $O(1)$-close in $L^1$ to a piecewise-linear profile with $O(L)$ shocks of $O(1)$ height. This immediately gives $\|u\|_{L^2}\sim L^{1/2}$.
- Obtain a **linear-in-$L$ inertial manifold dimension**, closing the gap between $O(L^{1.64})$ and $\Theta(L)$; this would also confirm extensivity of the dimension.
- Prove **existence of an invariant SRB-type measure** for KS at large $L$ and extensivity of its Kolmogorov–Sinai entropy density.
- Settle **2D global well-posedness** for $\mathbb{T}^2$ KS with general mean-zero data, or find finite-time blowup.
- Rigorous **lower bound $\dim_f\mathcal{A}_L \ge cL$ with an explicit constant** approaching numerics ($\approx0.07L$), via volume expansion along a hyperbolic periodic orbit rather than around $u\equiv0$.

## 9. Key References

- **[Foundational]** Y. Kuramoto, T. Tsuzuki. *Persistent Propagation of Concentration Waves in Dissipative Media Far from Thermal Equilibrium.* Progress of Theoretical Physics 55(2), 356–369, 1976.
- **[Foundational]** G. I. Sivashinsky. *Nonlinear analysis of hydrodynamic instability in laminar flames — I. Derivation of basic equations.* Acta Astronautica 4, 1177–1206, 1977.
- **[Foundational]** B. Nicolaenko, B. Scheurer, R. Temam. *Some global dynamical properties of the Kuramoto–Sivashinsky equations: nonlinear stability and attractors.* Physica D 16(2), 155–183, 1985.
- **[Foundational]** C. Foias, B. Nicolaenko, G. R. Sell, R. Temam. *Inertial manifolds for the Kuramoto–Sivashinsky equation and an estimate of their lowest dimension.* Journal de Mathématiques Pures et Appliquées 67, 197–226, 1988.
- **[Structural]** P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe. *A global attracting set for the Kuramoto–Sivashinsky equation.* Communications in Mathematical Physics 152, 203–214, 1993.
- **[Structural]** P. Collet, J.-P. Eckmann, H. Epstein, J. Stubbe. *Analyticity for the Kuramoto–Sivashinsky equation.* Physica D 67, 321–326, 1993.
- **[Method]** J. Goodman. *Stability of the Kuramoto–Sivashinsky and related systems.* Communications on Pure and Applied Mathematics 47(3), 293–306, 1994.
- **[Dimension]** R. Temam, X. Wang. *Estimates on the lowest dimension of inertial manifolds for the Kuramoto–Sivashinsky equation in the general case.* Differential and Integral Equations 7(3–4), 1095–1108, 1994.
- **[SOTA]** J. C. Bronski, T. N. Gambill. *Uncertainty estimates and $L_2$ bounds for the Kuramoto–Sivashinsky equation.* Nonlinearity 19(9), 2023–2039, 2006.
- **[SOTA]** L. Giacomelli, F. Otto. *New bounds for the Kuramoto–Sivashinsky equation.* Communications on Pure and Applied Mathematics 58(3), 297–318, 2005.
- **[SOTA]** F. Otto. *Optimal bounds on the Kuramoto–Sivashinsky equation.* Journal of Functional Analysis 257(7), 2188–2245, 2009.
- **[SOTA]** M. Goldman, M. Josien, F. Otto. *New bounds for the inhomogeneous Burgers and the Kuramoto–Sivashinsky equations.* Communications in Partial Differential Equations 40(12), 2237–2265, 2015.
- **[Recent]** D. M. Ambrose, A. L. Mazzucato. *Global solutions of the two-dimensional Kuramoto–Sivashinsky equation with a linearly growing mode in each direction.* Journal of Nonlinear Science 31, 96, 2021.
- **[Recent]** Y. Feng, A. L. Mazzucato. *Global existence for the two-dimensional Kuramoto–Sivashinsky equation with advection.* Communications in Partial Differential Equations 47(2), 279–306, 2022.
- **[Computational]** F. Christiansen, P. Cvitanović, V. Putkaradze. *Spatiotemporal chaos in terms of unstable recurrent patterns.* Nonlinearity 10(1), 55–70, 1997.
- **[Computational]** P. Cvitanović, R. L. Davidchack, E. Siminos. *On the state space geometry of the Kuramoto–Sivashinsky flow in a periodic domain.* SIAM Journal on Applied Dynamical Systems 9(1), 1–33, 2010.
- **[Survey / Book]** R. Temam. *Infinite-Dimensional Dynamical Systems in Mechanics and Physics.* 2nd ed., Springer Applied Mathematical Sciences 68, 1997.
- **[Survey / Book]** J. C. Robinson. *Infinite-Dimensional Dynamical Systems.* Cambridge University Press, 2001.

## 10. Worked Example / Concrete Special Case

**Goal.** Show two things by hand: (a) the attractor is trivial for $L<2\pi$; (b) the background-flow method really produces a super-extensive power of $L$, exhibiting the gap.

**(a) $L<2\pi \Rightarrow \mathcal{A}_L=\{0\}$.** For mean-zero $u$ on $\mathbb{T}_L$, Fourier modes satisfy $|k| \ge 2\pi/L =: k_{\min}$. The energy identity gives
$$\frac{d}{dt}\tfrac12\|u\|^2 = \sum_k (k^2-k^4)|\hat u_k|^2 L \le -\big(k_{\min}^4-k_{\min}^2\big)\|u\|^2 .$$
If $L<2\pi$ then $k_{\min}>1$, so $\lambda := k_{\min}^4-k_{\min}^2>0$ and $\|u(t)\|^2 \le e^{-2\lambda t}\|u(0)\|^2$. Every solution decays to $0$ exponentially; the attractor is the single point $0$. At $L=2\pi$ exactly, $k_{\min}=1$ and $\sigma(k_{\min})=0$ — the bifurcation point, where the first nontrivial steady branch emerges.

**Numerical check of the growth rate.** At $L=8$: $k_{\min}=2\pi/8=0.7854$, $\sigma = 0.6169 - 0.3805 = +0.2364 > 0$. The zero state is unstable, one unstable pair of modes ($k=\pm k_{\min}$; the next, $k=2k_{\min}=1.571>1$, has $\sigma=-3.62$). The attractor here is a nontrivial small set (a circle of steady states modulo translation), consistent with $\lfloor L/2\pi\rfloor = 1$ unstable mode.

**(b) Where $L^{3/2}$ comes from.** Take $u = v + \Phi$ with $\Phi$ mean-zero and fixed. Substituting and using $\int v^2 v_x =0$:
$$\frac{d}{dt}\tfrac12\|v\|^2 = -\|v_{xx}\|^2 + \|v_x\|^2 - \int \Phi'\frac{v^2}{2}\,dx - \int v\,\big(\Phi''''+\Phi''+\Phi\Phi'\big)dx .$$
Interpolation gives $\|v_x\|^2 \le \tfrac12\|v_{xx}\|^2 + \tfrac12\|v\|^2$, so the quadratic part is bounded by
$$-\tfrac12\|v_{xx}\|^2 - \int\Big(\frac{\Phi'-1}{2}\Big)v^2\,dx .$$
Coercivity therefore needs $\Phi' \gtrsim 1$ on most of $\mathbb{T}_L$ — but $\Phi$ is periodic, so $\int\Phi'=0$: $\Phi'$ must be $\approx +1$ on a large fraction and compensate with steep negative "shock" jumps, whose contribution the $\|v_{xx}\|^2$ term must absorb. Optimizing the number $N$ of jumps: with $N$ shocks the ramps have length $L/N$ and $\|\Phi\|_{L^2}^2 \sim L\cdot (L/N)^2$, while absorbing each jump costs a fixed budget from $\|v_{xx}\|^2$, forcing $N \lesssim L^{?}$. Bronski–Gambill's optimization yields the best admissible $\|\Phi\|_{L^2} \sim L^{3/2}$, hence
$$\limsup_{t\to\infty}\|u\|_{L^2} \le \|v\|_\infty^{\text{bound}} + \|\Phi\|_{L^2} = O(L^{3/2}).$$
The conjectured truth requires $\|\Phi\|_{L^2}\sim L^{1/2}$, i.e. $\Phi$ a sawtooth with $\Theta(L)$ shocks of $O(1)$ height and $O(1)$ ramp length — exactly what simulations show the solution itself to be. Such a $\Phi$ is *not admissible* in the pointwise-in-time argument, because the $\Theta(L)$ shocks overwhelm the $\|v_{xx}\|^2$ budget. That single failure, and its repair by time-averaging, is the content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*