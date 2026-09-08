---
id: 06-pdes/boltzmann-equation-large-data
title: "Boltzmann Equation Large Data"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boltzmann Equation Large Data

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/boltzmann-equation-large-data` · **Status:** open

## 1. Problem Statement / Conjecture

For the spatially inhomogeneous Boltzmann equation on $\mathbb{R}^3_x \times \mathbb{R}^3_v$ (or on $\mathbb{T}^3_x$, or a bounded domain with physical boundary conditions), decide whether arbitrary large initial data of finite mass, energy and entropy generate a **unique global-in-time solution that conserves energy and is smooth for $t>0$**.

Concretely, three linked questions, all open:

1. **Global existence of strong solutions.** Does every $f_0 \ge 0$ with
$$\int\!\!\int f_0\,(1+|v|^2+|\log f_0|)\,dv\,dx < \infty$$
launch a global solution in a class strong enough that the equation holds pointwise (or in the a.e.-Duhamel sense), rather than only in DiPerna–Lions renormalized form?
2. **Uniqueness / non-breakdown.** Are DiPerna–Lions renormalized solutions unique? Equivalently, does a large-data solution avoid finite-time breakdown of the hydrodynamic fields (density $\rho$, temperature $T$)?
3. **Energy conservation.** Renormalized solutions are only known to satisfy $\int\!\!\int f|v|^2 \le \int\!\!\int f_0|v|^2$. Is equality forced?

A complete resolution is either a proof of global well-posedness for large data, or an example — a genuine large-data initial datum whose solution loses uniqueness, loses energy, or blows up (concentration of $\rho$, vanishing of $T$, or unbounded moments in finite time).

## 2. Mathematical Foundations

The unknown is a density $f(t,x,v)\ge 0$ solving
$$\partial_t f + v\cdot\nabla_x f = Q(f,f),$$
with the bilinear collision operator
$$Q(g,f)(v) = \int_{\mathbb{R}^3}\int_{S^2} B(v-v_*,\sigma)\,\big[g(v'_*)f(v') - g(v_*)f(v)\big]\,d\sigma\,dv_*,$$
$$v' = \frac{v+v_*}{2} + \frac{|v-v_*|}{2}\sigma, \qquad v'_* = \frac{v+v_*}{2} - \frac{|v-v_*|}{2}\sigma,$$
so that $v'+v'_* = v+v_*$ and $|v'|^2+|v'_*|^2 = |v|^2+|v_*|^2$. The kernel factorizes for inverse-power interactions as
$$B(z,\sigma) = |z|^{\gamma}\, b(\cos\theta), \qquad \cos\theta = \tfrac{z}{|z|}\cdot\sigma,$$
with $\gamma \in (-3,1]$: hard spheres $\gamma=1$, hard potentials $\gamma>0$, Maxwell molecules $\gamma=0$, soft potentials $\gamma<0$. Without Grad's angular cutoff, $b(\cos\theta)\sim \theta^{-2-2s}$ as $\theta\to0$ with $s\in(0,1)$, and the singularity is non-integrable: $\int b\,d\sigma = +\infty$. The operator then behaves like a fractional diffusion of order $2s$ in $v$ (Alexandre–Desvillettes–Villani–Wennberg coercivity).

**Conservation and entropy.** For $\varphi \in \{1, v, |v|^2\}$, $\int Q(f,f)\varphi\,dv = 0$, so mass, momentum and energy are formally conserved. Boltzmann's $H$-theorem gives
$$\frac{d}{dt}\int\!\!\int f\log f\,dv\,dx = -\int D(f)\,dx \le 0,\qquad D(f)=-\int Q(f,f)\log f\,dv \ge 0,$$
and $D(f)=0$ iff $f$ is a local Maxwellian $M_{\rho,u,T}(v) = \rho(2\pi T)^{-3/2}e^{-|v-u|^2/2T}$.

**The a priori set.** For large data, the *only* known coercive controls are: $\|f\|_{L^1}$, energy, the entropy $H(f)$, the space-time entropy dissipation $\int_0^\infty\!\!\int D(f)\,dx\,dt$, plus dispersive/averaging gains. These are all at the level of $L^1$ or $L\log L$ — subcritical relative to the quadratic nonlinearity $Q(f,f)$, which requires roughly $f \in L^\infty_v L^1$-type bounds to be defined.

**Scaling.** The equation with $\gamma$-homogeneous kernel is invariant under
$$f_\lambda(t,x,v) = \lambda^{a} f(\lambda^{b}t,\lambda^{c}x,v),$$
for suitable exponents; unlike Navier–Stokes there is no single critical Sobolev space, but the collision term scales as $\lambda \cdot$mass, so *no* smallness is supplied by the conserved quantities.

**Renormalization.** DiPerna–Lions consider $\beta(f)$ with $\beta'(f) = (1+f)^{-1}$, giving
$$\partial_t \beta(f) + v\cdot\nabla_x\beta(f) = \frac{Q^+(f,f)-Q^-(f,f)}{1+f},$$
whose right-hand side is in $L^1_{loc}$ under the a priori bounds. Velocity averaging (Golse–Lions–Perthame–Sentis) supplies the compactness of $\int f\varphi(v)dv$ needed to pass to the limit.

## 3. History & State of the Art (SOTA)

- **1872**: Boltzmann introduces the equation and the $H$-theorem.
- **1933**: Carleman gives the first global existence result — spatially homogeneous, radially symmetric hard spheres.
- **1963–72**: Grad's cutoff and linearized theory; Arkeryd's systematic $L^1$ theory of the spatially homogeneous equation.
- **1974–80**: Ukai constructs global solutions near a global Maxwellian in $\mathbb{T}^3$ (and Nishida–Imai, Shizuta, Caflisch for soft potentials).
- **1984**: Illner–Shinbrot: global solutions near vacuum in $\mathbb{R}^3$ for small, dispersing data.
- **1989**: **DiPerna–Lions** (*Annals of Mathematics*) prove global existence of renormalized solutions for arbitrary large data with finite mass, energy, entropy and $\int f|x|^2$. Uniqueness, energy conservation and regularity are left open and remain open.
- **2002–04**: Golse–Saint-Raymond derive the incompressible Navier–Stokes limit from renormalized solutions (*Invent. Math.* 2004) — the strongest structural use of large-data solutions to date.
- **2003–11**: Guo's nonlinear energy method extends near-Maxwellian theory to Vlasov–Maxwell–Boltzmann and to bounded domains; Gressman–Strain and Alexandre–Morimoto–Ukai–Xu–Yang independently solve the non-cutoff perturbative problem.
- **2016–22**: **Imbert–Silvestre** develop a De Giorgi–Nash–Moser / kinetic-Schauder theory giving *conditional* regularity: solutions with bounded hydrodynamic fields are $C^\infty$ for $t>0$. This is the current frontier.

## 4. Partial Results / Verified Cases

- **Spatially homogeneous ($f=f(t,v)$), all data.** Global existence and uniqueness for hard potentials with cutoff (Arkeryd 1972; Mischler–Wennberg 1999 for uniqueness in $L^1_2$); moment propagation (Povzner, Elmroth, Bobylev), $L^\infty$ and Gaussian-tail bounds, and eventual regularization. Non-cutoff homogeneous case: global well-posedness for $\gamma+2s\ge 0$ known.
- **Near global Maxwellian.** $f = M + \sqrt{M}g$, $\|g\|_{H^N_{x,v}}\ll1$ on $\mathbb{T}^3$: global existence, uniqueness, $C^\infty$ smoothness, exponential decay $e^{-\lambda t}$ (hard potentials) or stretched-exponential (soft), all $\gamma\in(-3,1]$, with and without cutoff (Ukai 1974; Guo 2003–06; Gressman–Strain, *JAMS* 2011; AMUXY 2012). Bounded domains with diffuse reflection: Guo, *ARMA* 2010.
- **Near vacuum.** Small data in $\mathbb{R}^3$ dispersing: Illner–Shinbrot 1984 (cutoff, $\gamma\ge0$); Chaturvedi (*Ann. PDE* 2021) for moderately soft non-cutoff potentials.
- **One space dimension in $x$ / slab geometry.** Cercignani, Arkeryd–Nouri: strong solutions for the slab under structural hypotheses.
- **Conditional regularity, all data.** If a solution satisfies $0<\rho_0\le\rho(t,x)$, $\rho \le \rho_1$, $T\le T_1$, $\int f|v|^2$ locally bounded, and $\gamma+2s\in[0,2]$, then $f\in C^\infty((0,T]\times\mathbb{R}^3\times\mathbb{R}^3)$ with quantitative estimates (Imbert–Silvestre, *JAMS* 2022; Imbert–Mouhot–Silvestre for $L^\infty$).
- **Hydrodynamic limits.** From renormalized solutions to Leray solutions of incompressible Navier–Stokes (Golse–Saint-Raymond 2004, 2009) — Leray-level regularity, not more.
- **Cercignani's conjecture** ($D(f)\ge \lambda H(f|M)$): false in general (Bobylev–Cercignani), true up to $\varepsilon$-loss $D(f)\gtrsim H(f|M)^{1+\varepsilon}$ (Villani, *CMP* 2003), giving almost-exponential relaxation.

## 5. Principal Obstacles

- **Supercritical a priori bounds.** Mass + energy + entropy control $f$ only in $L\log L$. $Q(f,f)$ is quadratic and requires an $L^1_v$-in-$v$ bound *pointwise in $x$*; nothing in the conserved set forbids $\rho(t,x)\to\infty$ or $T(t,x)\to0$ on a set of measure zero. This is a genuine scaling gap, not a technical one.
- **No maximum principle for the nonlinear problem.** $f\ge0$ is preserved, but there is no comparison principle giving upper bounds, because $Q^+(f,f)$ is quadratic in $f$.
- **Loss of coercivity when $\rho\to0$ or $T\to0$.** The collision operator's ellipticity constant degenerates like $\rho\,T^{\,\cdot}$; the Imbert–Silvestre machinery collapses exactly at vacuum and at zero temperature, which is precisely where a hypothetical singularity would sit.
- **Renormalization destroys the nonlinearity.** DiPerna–Lions solutions satisfy an equation for $\beta(f)$ only; one cannot multiply by $f$ or by $v$-weights to derive further estimates, which is why uniqueness and energy conservation are inaccessible.
- **Transport vs. collisions.** Free streaming $v\cdot\nabla_x$ is hyperbolic and regularizes nothing in $x$; the collision operator regularizes only in $v$ (order $2s$, and not at all with cutoff). Regularity in $x$ must be bootstrapped by hypoellipticity (Hörmander commutator $[\partial_t+v\cdot\nabla_x, \nabla_v] = -\nabla_x$), which requires the $v$-gain to be uniform — again failing near vacuum.
- **Velocity averaging is too weak.** It gives compactness, hence existence, but only fractional-derivative gains ($H^{1/2}_x$ for the averages) that cannot close a quadratic estimate.

## 6. The Gap

Everything proven for large data lives at the level of *weak/renormalized* solutions; everything proven at the level of *strong* solutions requires either a perturbative smallness, a symmetry reduction ($x$-independence), or an assumed pointwise bound on $(\rho, u, T)$.

The precise missing step: **derive the hydrodynamic bounds**
$$0 < \rho_0 \le \rho(t,x), \qquad \rho(t,x)\le \rho_1, \qquad T(t,x)\le T_1$$
*from the conserved quantities alone*, for at least one class of large data. Imbert–Silvestre have shown these bounds are sufficient for full regularity; nobody knows how to produce them. Equivalently, rule out (or exhibit) finite-time concentration of mass or collapse of temperature. This is the exact analogue of the Navier–Stokes gap between Leray solutions and the Ladyzhenskaya–Prodi–Serrin criterion.

## 7. Current Research (as of June 2026)

- **Conditional-regularity program** (Imbert, Silvestre, Mouhot, Guillen; Paris–Chicago–Cambridge). Extending the De Giorgi/Schauder theory to the full range $\gamma+2s<0$ (very soft potentials) and to boundary-value problems. Recent work on kinetic Schauder estimates and on the local well-posedness theory of the non-cutoff equation in $L^\infty$-based weighted spaces. *(frontier — verify)* Attempts to close the loop by proving a lower bound on $T$ from entropy dissipation remain unpublished.
- **Convex-integration non-uniqueness.** Following its success for Euler and Navier–Stokes, several groups are probing whether renormalized Boltzmann solutions admit non-uniqueness constructions; the obstruction is that $f\ge0$ and $H$-decay are rigid constraints. *(frontier — verify)*
- **Large-data close to hydrodynamics.** Constructing solutions near a local Maxwellian whose fluid fields solve compressible Euler/Navier–Stokes (Guo–Jang–Jiang; Guo–Xiao), transferring the fluid problem's difficulty into kinetic theory.
- **Boundary effects.** Regularity and decay in non-convex domains, where singularities propagate along grazing characteristics (Guo, Kim, Tonon, Trescases).
- **Quantitative derivation.** Extending Lanford's short-time validity (Bodineau–Gallagher–Saint-Raymond–Simonella) toward long-time and fluctuation results — relevant because a large-data blow-up would contradict the particle picture.

## 8. Future Work

- Prove a *conditional* criterion in the reverse direction: a Serrin-type integrability condition on $\rho$ alone (e.g. $\rho\in L^p_tL^q_x$) sufficient for regularity, weakening the current $L^\infty$ hypothesis.
- Establish energy conservation for renormalized solutions under an extra moment bound $\int f|v|^{2+\delta}$ — Lions and Villani both single this out as the most likely first crack.
- Settle uniqueness of renormalized solutions in the spatially homogeneous *plus* small-$x$-perturbation regime as a stepping stone.
- Build a self-similar or concentration ansatz to test whether blow-up is even conceivable; Villani's survey conjectures none exists for hard spheres.
- Exploit entropy dissipation quantitatively (Desvillettes–Villani, *Invent. Math.* 2005) to force convergence to a global Maxwellian *without* assuming a priori smoothness — currently their result is conditional on uniform-in-time Sobolev bounds.

## 9. Key References

- **[Foundational]** R. J. DiPerna, P.-L. Lions. *On the Cauchy problem for Boltzmann equations: global existence and weak stability.* Annals of Mathematics 130 (1989), 321–366. [DOI](https://doi.org/10.2307/1971423)
- **[Foundational]** S. Ukai. *On the existence of global solutions of mixed problem for non-linear Boltzmann equation.* Proc. Japan Acad. 50 (1974), 179–184. [DOI](https://doi.org/10.3792/pja/1195519027)
- **[Foundational]** R. Illner, M. Shinbrot. *The Boltzmann equation: global existence for a rare gas in an infinite vacuum.* Communications in Mathematical Physics 95 (1984), 217–226. [DOI](https://doi.org/10.1007/bf01468142)
- **[Foundational]** C. Cercignani, R. Illner, M. Pulvirenti. *The Mathematical Theory of Dilute Gases.* Springer, Applied Mathematical Sciences 106, 1994. [DOI](https://doi.org/10.1007/978-1-4419-8524-8)
- **[SOTA / Recent]** C. Imbert, L. Silvestre. *Global regularity estimates for the Boltzmann equation without cut-off.* Journal of the AMS 35 (2022), 625–703. [DOI](https://doi.org/10.1090/jams/986)
- **[SOTA / Recent]** C. Imbert, C. Mouhot, L. Silvestre. *Decay estimates for large velocities in the Boltzmann equation without cutoff.* Journal de l'École polytechnique 7 (2020), 143–183. [DOI](https://doi.org/10.5802/jep.113)
- **[SOTA / Recent]** P. T. Gressman, R. M. Strain. *Global classical solutions of the Boltzmann equation without angular cut-off.* Journal of the AMS 24 (2011), 771–847. [DOI](https://doi.org/10.1090/s0894-0347-2011-00697-8)
- **[SOTA / Recent]** Y. Guo. *Decay and continuity of the Boltzmann equation in bounded domains.* Archive for Rational Mechanics and Analysis 197 (2010), 713–809. [DOI](https://doi.org/10.1007/s00205-009-0285-y)
- **[SOTA / Recent]** F. Golse, L. Saint-Raymond. *The Navier–Stokes limit of the Boltzmann equation for bounded collision kernels.* Inventiones Mathematicae 155 (2004), 81–161. [DOI](https://doi.org/10.1007/s00222-003-0316-5)
- **[SOTA / Recent]** L. Desvillettes, C. Villani. *On the trend to global equilibrium for spatially inhomogeneous kinetic systems: the Boltzmann equation.* Inventiones Mathematicae 159 (2005), 245–316. [DOI](https://doi.org/10.1007/s00222-004-0389-9)
- **[SOTA / Recent]** S. Chaturvedi. *Stability of vacuum for the Boltzmann equation with moderately soft potentials.* Annals of PDE 7 (2021), article 15. [DOI](https://doi.org/10.1007/s40818-021-00103-4)
- **[Survey]** C. Villani. *A review of mathematical topics in collisional kinetic theory.* Handbook of Mathematical Fluid Dynamics, Vol. I, North-Holland, 2002, 71–305. [DOI](https://doi.org/10.1016/s1874-5792(02)80004-0)
- **[Survey]** C. Imbert, L. Silvestre. *Regularity for the Boltzmann equation conditional to macroscopic bounds.* EMS Surveys in Mathematical Sciences 7 (2020), 117–172. [DOI](https://doi.org/10.4171/emss/37)
- **[Survey]** C. Mouhot. *De Giorgi–Nash–Moser and Hörmander theories: new interplays.* Proceedings of the ICM 2018, Vol. III, 2467–2493. [DOI](https://doi.org/10.1142/9789813272880_0146)

## 10. Worked Example / Concrete Special Case

**Maxwell molecules, spatially homogeneous — where the large-data problem *is* solved, and why removing $x$-dependence is the whole difficulty.**

Take $\gamma=0$ with cutoff, $B=b(\cos\theta)$, $\int_{S^2}b\,d\sigma = 1$, and $f=f(t,v)$ with $\int f\,dv=1$, $\int v f\,dv=0$, $\int|v|^2f\,dv=3$. Bobylev's identity turns the collision operator into a closed convolution on the Fourier side. With $\hat f(\xi)=\int f(v)e^{-i v\cdot\xi}dv$,
$$\partial_t \hat f(\xi) = \int_{S^2} b\!\left(\tfrac{\xi}{|\xi|}\!\cdot\!\sigma\right)\Big[\hat f(\xi^+)\hat f(\xi^-) - \hat f(0)\hat f(\xi)\Big]d\sigma,\qquad \xi^{\pm}=\tfrac{\xi \pm |\xi|\sigma}{2}.$$
Note $|\xi^+|^2+|\xi^-|^2=|\xi|^2$. Define the Toscani distance
$$d_2(f,g) = \sup_{\xi\neq0} \frac{|\hat f(\xi)-\hat g(\xi)|}{|\xi|^2}.$$
Let $M$ be the Maxwellian with the same mass, momentum, energy, so $\hat M$ solves the same equation as a steady state. Subtracting and writing $h = \hat f - \hat M$:
$$\partial_t h(\xi) = \int_{S^2} b\big[h(\xi^+)\hat f(\xi^-) + \hat M(\xi^+)h(\xi^-)\big]d\sigma - h(\xi).$$
Using $|\hat f|\le1$, $|\hat M|\le1$ and $|h(\eta)|\le d_2 |\eta|^2$,
$$|\partial_t h(\xi)| + |h(\xi)| \le d_2(t)\int_{S^2} b\,\big(|\xi^+|^2+|\xi^-|^2\big)d\sigma = d_2(t)\,|\xi|^2 .$$
Dividing by $|\xi|^2$ and taking the sup gives $\frac{d}{dt}d_2 \le -d_2 + d_2 = 0$ — a contraction bound; refining the estimate with the exact angular average $\int b\,(\cos^4(\theta/2)+\sin^4(\theta/2))\,d\sigma = 1-\kappa$, $\kappa>0$, yields
$$d_2(f(t),M) \le e^{-\kappa t}\, d_2(f_0,M).$$
**Consequences.** $d_2$ is a metric, so this is simultaneously *uniqueness* and *exponential relaxation* — for arbitrarily large data, no smallness at all. Combined with Povzner moment estimates ($\int f|v|^{2k}$ propagates and becomes bounded for $t\ge t_0$) one gets full regularity.

**Why this collapses with $x$-dependence.** The Bobylev identity needs $Q$ acting alone; adding $v\cdot\nabla_x f$ makes the Fourier variables $(\xi,k)$ couple through the transport term $k\cdot\nabla_\xi \hat f$, a first-order transport in $\xi$ that transfers information from low to high $|\xi|$ with no damping. The quantity $\sup_\xi |h|/|\xi|^2$ is then not monotone, and no substitute Lyapunov functional is known. The homogeneous case is solved because it has a *closed, contractive* structure; the inhomogeneous large-data case has none — the entire content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*