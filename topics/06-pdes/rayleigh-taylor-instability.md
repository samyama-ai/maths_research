---
id: 06-pdes/rayleigh-taylor-instability
title: "Rayleigh-Taylor Instability"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rayleigh-Taylor Instability

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/rayleigh-taylor-instability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two immiscible incompressible fluids of constant densities $\rho^+$ (above) and $\rho^-$ (below) occupy adjacent regions separated by a free interface, under gravity $-g e_n$. When $\rho^+ > \rho^-$ — heavy over light — the flat interface is linearly unstable: the *Rayleigh–Taylor (RT) instability*. The open problems are:

1. **(Ill-posedness vs. selection.)** Without surface tension, the two-phase incompressible Euler system with $\rho^+>\rho^-$ is ill-posed in every Sobolev class. What is the correct notion of solution past the onset of instability, and is it unique in any physically meaningful sense? Convex integration produces a continuum of admissible weak solutions; is there a selection principle (vanishing viscosity, vanishing surface tension, maximal dissipation) that picks exactly one?

2. **(The $\alpha$-problem.)** For a statistically self-similar turbulent RT mixing layer between miscible fluids at Atwood number $A=(\rho^+-\rho^-)/(\rho^++\rho^-)$, the bubble-front penetration obeys $h(t)\simeq \alpha A g t^2$. Prove that a self-similar quadratic growth law holds for solutions of the Navier–Stokes or Euler equations, and determine $\alpha$ — or prove that $\alpha$ is not universal and identify what it depends on.

A complete resolution of (1) means: a well-posedness or non-uniqueness theorem for the selected class, valid for all $t>0$ and all $A\in(0,1]$. A complete resolution of (2) means a theorem bounding $\limsup_{t\to\infty} h(t)/(Agt^2)$ from above and below by explicit constants derived from the PDE, not from experiment.

## 2. Mathematical Foundations

Let $\Omega\subset\mathbb{R}^n$ ($n=2,3$) be split by a moving interface $\Gamma(t)$ into $\Omega^\pm(t)$. The **two-phase incompressible Euler system** is
$$\rho\big(\partial_t u + (u\cdot\nabla)u\big) + \nabla p = -\rho g e_n,\qquad \nabla\cdot u = 0 \quad\text{in }\Omega^\pm(t),$$
with $\rho=\rho^\pm$ in $\Omega^\pm$, kinematic condition $V_\Gamma = u\cdot \nu$, and dynamic condition
$$\llbracket p \rrbracket \;=\; \sigma_s\,\kappa \quad\text{on }\Gamma(t),$$
where $\llbracket\cdot\rrbracket$ is the jump, $\kappa$ the mean curvature, $\sigma_s\ge 0$ the surface tension, and $\nu$ the unit normal pointing into $\Omega^+$.

**Taylor sign condition.** Local well-posedness for $\sigma_s=0$ hinges on
$$-\,\llbracket \partial_\nu p\rrbracket \;\ge\; c_0 > 0 \quad\text{on }\Gamma(t).$$
Its failure is exactly the Rayleigh–Taylor condition. For a flat interface at rest, $-\llbracket\partial_\nu p\rrbracket = g(\rho^- - \rho^+)$, negative precisely when heavy sits over light.

**Linear dispersion relation.** Linearizing about the flat interface $\{x_n=0\}$ in an infinite domain with irrotational perturbations $\propto e^{i k\cdot x' + \lambda t}$, $k=|k|$:
$$\boxed{\;\lambda^2 \;=\; \frac{g k(\rho^+-\rho^-) - \sigma_s k^3}{\rho^++\rho^-}\;}$$
For $\sigma_s=0$ this gives $\lambda = \sqrt{A g k}$ — unbounded growth as $k\to\infty$, so the linearized operator generates no semigroup on any Sobolev space; this is the analytic root of the ill-posedness. For $\sigma_s>0$ the band of unstable modes is finite: $k < k_c := \sqrt{g(\rho^+-\rho^-)/\sigma_s}$.

**Viscous case.** With viscosities $\mu^\pm$ the growth rate solves a quartic characteristic equation (Chandrasekhar, 1961, Ch. X); viscosity damps but does not remove instability when $\sigma_s=0$, giving a most-unstable wavelength $\lambda_m \sim (\mu^2/(A\rho g))^{1/3}$-type scaling.

**Weak formulation.** For the density-transport form, $\rho\in L^\infty$ solves $\partial_t\rho + u\cdot\nabla\rho=0$ with $\partial_t(\rho u)+\nabla\cdot(\rho u\otimes u)+\nabla p = -\rho g e_n$ in $\mathcal{D}'$; admissible weak solutions satisfy the energy inequality $\frac{d}{dt}\int (\tfrac12\rho|u|^2 + \rho g x_n)\,dx \le 0$.

## 3. History & State of the Art (SOTA)

- **1883** — Lord Rayleigh, *Investigation of the character of the equilibrium of an incompressible heavy fluid of variable density*, Proc. London Math. Soc.: linear normal-mode analysis of stratified fluid.
- **1950** — G. I. Taylor, Proc. Roy. Soc. A 201: the accelerated-interface version, $g\mapsto$ acceleration; companion experiments by Lewis (1950) confirm exponential then nonlinear bubble/spike development.
- **1961** — Chandrasekhar's *Hydrodynamic and Hydromagnetic Stability* codifies the viscous, magnetic and rotating cases.
- **1988** — D. Ebin proves ill-posedness of the two-phase Euler problem in the RT-unstable regime.
- **1997/1999** — S. Wu shows the Taylor sign condition holds *automatically* for irrotational water waves (vacuum above), so the classical water-wave problem is never RT-unstable; local well-posedness follows in 2D and 3D.
- **2007** — Coutand–Shkoller and, independently, Cheng–Coutand–Shkoller: well-posedness of the two-phase problem *with* surface tension, no sign condition needed; and ill-posedness without it.
- **2003–2011** — Y. Guo and H. J. Hwang establish nonlinear instability (bootstrap from linear growth) for the inviscid problem; Guo–Tice develop the "variational/normal-mode" method giving sharp linear-to-nonlinear transfer for viscous free-boundary problems.
- **2011–2021** — Convex integration reaches RT: Székelyhidi's vortex-sheet construction is adapted by Gebhard, Kolumbán and Székelyhidi to build infinitely many admissible weak solutions with a mixing zone growing like $t^2$.
- **Computation.** The $\alpha$-group collaboration (Dimonte et al., Phys. Fluids 16, 2004) ran seven independent codes on a common initial condition and obtained $\alpha_b\approx 0.025\pm 0.003$, against experimental $\alpha_b\approx0.05$–$0.07$; the discrepancy remains unexplained and is initial-condition sensitive.

## 4. Partial Results / Verified Cases

- **Surface tension $\sigma_s>0$, any $A\in(0,1)$, $n=2,3$:** local-in-time well-posedness in $H^s$, $s$ large, for the two-phase Euler and Navier–Stokes free-boundary problems (Coutand–Shkoller 2007; Cheng–Coutand–Shkoller 2008; Shatah–Zeng 2011). RT instability is then a genuine finite-band phenomenon, unstable only for $k<k_c$.
- **Taylor sign condition satisfied ($\rho^+<\rho^-$ or vacuum above):** local well-posedness without surface tension — Wu (1997 for $n=2$, 1999 for $n=3$), Lannes (2005), Lindblad (2005) for the rotational one-phase case.
- **Ill-posedness, $\sigma_s=0$, $\rho^+>\rho^-$:** no continuous dependence in any $H^s$ (Ebin 1988; Cheng–Coutand–Shkoller 2008). Solved negatively.
- **Nonlinear instability from linear instability:** proven for the inviscid incompressible stratified problem (Hwang–Guo, ARMA 167 (2003)), for viscous incompressible fluids (Jiang–Jiang–Ni), and for compressible viscous flow.
- **Magnetic stabilization:** for the incompressible MHD free-boundary problem with a horizontal field $B_0$, the flat interface is *stable* iff $|B_0|^2$ exceeds an explicit threshold depending on $g\llbracket\rho\rrbracket$ and the domain height (Wang–Tice; Jiang–Jiang). Sharp in the linear and, in bounded slabs, nonlinear regime.
- **Surface-tension threshold in slabs:** for the viscous two-layer problem in a horizontally periodic slab of period $L$, there is a critical $\sigma_c(L)$ such that $\sigma_s>\sigma_c$ gives global existence with exponential decay and $\sigma_s<\sigma_c$ gives instability (Wang–Tice–Kim, ARMA 212 (2014)).
- **Muskat / porous-media analogue:** the incompressible porous medium equation with heavy-over-light is ill-posed, and Otto (1999, 2001) and Székelyhidi (2012) characterize the relaxed/mixing solution; Córdoba–Gancedo give the RT sign condition for the Muskat problem. This is the one setting where the "mixing zone" is rigorously identified as the unique solution of a relaxed variational problem.
- **Non-uniqueness:** Gebhard–Kolumbán–Székelyhidi (ARMA 241 (2021)) construct, for flat unstable initial data, infinitely many admissible weak solutions whose mixing zone has thickness $c\,A g t^2$ with an explicit admissible range of $c$.

## 5. Principal Obstacles

- **Loss of derivatives is structural, not technical.** $\lambda\sim\sqrt{Agk}$ means the linearized evolution gains half a derivative per unit time in the wrong direction. Energy estimates fail at every order; no paradifferential symmetrization repairs it, because the principal symbol of the interface operator is $-Agk$ rather than $+\sigma_s k^3$. This is why Wu-type arguments, which exploit the *positivity* of $-\partial_\nu p$, cannot be transplanted.
- **Vanishing surface tension is singular.** Existence times from $\sigma_s>0$ theory shrink like $\sigma_s^{1/2}$ or worse in the unstable case, so no compactness argument yields a $\sigma_s\to 0$ limit. The instability's most-unstable wavelength $\lambda_m\to0$ as $\sigma_s\to0$, so energy concentrates at unresolved scales.
- **Convex integration gives too much.** The $h$-principle produces a residual set of admissible weak solutions rather than one; the standard admissibility criterion (energy inequality) does not distinguish them. Strengthened criteria (local energy, maximal dissipation, entropy) are not known to be well-defined or selective for this system.
- **The mixing zone is not a graph.** Past the bubble–spike stage the interface loses regularity and topology (droplet pinch-off, reconnection). Every rigorous free-boundary framework assumes a graph or a $C^{1,\alpha}$ hypersurface; there is no PDE-level definition of the mixing-zone boundary $h(t)$ that is both intrinsic and stable.
- **Self-similarity is not enforced by scaling.** The Euler system with gravity has a scaling $x\to\ell x$, $t\to \ell^{1/2}t$ consistent with $h\sim t^2$, but it is not a symmetry that constrains the constant $\alpha$; $\alpha$ depends on the initial spectrum, and no rigorous bound separates the "memory" of initial data from the asymptotic law.

## 6. The Gap

Proved: (i) ill-posedness with $\sigma_s=0$, $\rho^+>\rho^-$; (ii) well-posedness with $\sigma_s>0$ on $[0,T(\sigma_s)]$; (iii) existence of *many* admissible weak solutions with $t^2$ mixing zones; (iv) linear-to-nonlinear instability transfer on the exponential-growth window.

Not proved: any statement valid on the timescale where $h(t)$ becomes comparable to the domain, for a *canonically selected* solution. The precise missing step is a compactness or selection theorem: show that the family $\{u^{\sigma_s}\}$ (or $\{u^{\nu}\}$ from vanishing viscosity) converges as $\sigma_s\to0$ to a single measure-valued or subsolution-type limit, and that this limit — not the convex-integration zoo — is the physical one. Equivalently: identify a coercive relaxed functional whose unique minimizer is the mixing zone, as Otto did for porous media, but for inertial (Euler/Navier–Stokes) dynamics where the relaxation is genuinely non-convex in the velocity.

## 7. Current Research (as of June 2026)

- **Convex integration and subsolutions.** Groups around Székelyhidi (Leipzig/MPI MiS), Kolumbán, and Gebhard continue to sharpen the admissible range of mixing-zone speeds, aiming to show the *maximal* subsolution speed matches the buoyancy-drag prediction. *(frontier — verify)*
- **Free-boundary MHD stabilization.** Jiang Fei and Jiang Song (Fuzhou), Y. Wang and I. Tice (CMU) extend sharp stability thresholds to nonhomogeneous and viscoelastic media, including elasticity-driven stabilization where the shear modulus plays the role of $\sigma_s$.
- **Vanishing surface tension.** Continued efforts to obtain $\sigma_s$-uniform estimates on $O(\sigma_s^{0})$ timescales for *stable-sign* data, as a stepping stone to the unstable case.
- **Data-driven / rigorous-numerics hybrids.** High-resolution DNS at $Re\sim10^4$ with controlled initial spectra to test whether $\alpha$ is initial-condition-determined (Livermore, Los Alamos, Cambridge DAMTP). Current consensus: $\alpha_b$ is *not* universal for arbitrary initial perturbation spectra; it is asymptotically universal only for sufficiently steep short-wavelength spectra. *(frontier — verify)*
- **Relaxation/homogenization for inertial mixing.** Attempts to build an Otto-style gradient-flow relaxation for the Boussinesq system rather than the porous-medium system.

## 8. Future Work

- Prove a **selection theorem**: vanishing viscosity for the 3D two-phase Navier–Stokes with $\sigma_s\to0$ jointly, giving a unique measure-valued solution with a well-defined mixing zone.
- Establish **two-sided bounds** $c_1 \le h(t)/(Agt^2)\le c_2$ for admissible weak solutions with generic initial data, with $c_2$ from a subsolution/energy argument and $c_1$ from an instability bootstrap.
- **Sharpen the surface-tension threshold** $\sigma_c(L)$ to the fully nonlinear 3D setting with unbounded domains.
- Extend **Guo–Tice normal-mode machinery** to compressible, multi-mode and stratified-background settings with non-constant $\rho(x_n)$, where the eigenvalue problem is a Sturm–Liouville operator rather than an algebraic relation.
- Settle whether **maximal dissipation** (Dafermos) is well-posed as a selection criterion for the two-phase Euler system.

## 9. Key References

- **[Foundational]** Lord Rayleigh. *Investigation of the character of the equilibrium of an incompressible heavy fluid of variable density.* Proc. London Math. Soc. **14**, 170–177, 1883.
- **[Foundational]** G. I. Taylor. *The instability of liquid surfaces when accelerated in a direction perpendicular to their planes. I.* Proc. Roy. Soc. London A **201**, 192–196, 1950.
- **[Foundational]** S. Chandrasekhar. *Hydrodynamic and Hydromagnetic Stability.* Oxford University Press, 1961 (Dover reprint 1981), Chapter X.
- **[Foundational]** D. G. Ebin. *Ill-posedness of the Rayleigh–Taylor and Helmholtz problems for incompressible fluids.* Comm. Partial Differential Equations **13**(10), 1265–1295, 1988.
- **[Foundational]** S. Wu. *Well-posedness in Sobolev spaces of the full water wave problem in 2-D.* Invent. Math. **130**, 39–72, 1997; and *…in 3-D.* J. Amer. Math. Soc. **12**, 445–495, 1999.
- **[SOTA]** D. Coutand, S. Shkoller. *Well-posedness of the free-surface incompressible Euler equations with or without surface tension.* J. Amer. Math. Soc. **20**(3), 829–930, 2007.
- **[SOTA]** C. H. A. Cheng, D. Coutand, S. Shkoller. *On the motion of vortex sheets with surface tension in three-dimensional Euler equations with vorticity.* Comm. Pure Appl. Math. **61**(12), 1715–1752, 2008.
- **[SOTA]** H. J. Hwang, Y. Guo. *On the dynamical Rayleigh–Taylor instability.* Arch. Ration. Mech. Anal. **167**, 235–253, 2003.
- **[SOTA]** Y. Guo, I. Tice. *Linear Rayleigh–Taylor instability for viscous, compressible fluids.* SIAM J. Math. Anal. **42**(4), 1688–1720, 2010.
- **[SOTA]** Y. Wang, I. Tice, C. Kim. *The viscous surface-internal wave problem: global well-posedness and decay.* Arch. Ration. Mech. Anal. **212**, 1–92, 2014.
- **[SOTA / Recent]** B. Gebhard, J. J. Kolumbán, L. Székelyhidi Jr. *A new approach to the Rayleigh–Taylor instability.* Arch. Ration. Mech. Anal. **241**, 1243–1280, 2021.
- **[SOTA]** F. Otto. *Evolution of microstructure in unstable porous media flow: a relaxational approach.* Comm. Pure Appl. Math. **52**(7), 873–915, 1999.
- **[Computational]** G. Dimonte et al. *A comparative study of the turbulent Rayleigh–Taylor instability using high-resolution three-dimensional numerical simulations: The Alpha-Group collaboration.* Phys. Fluids **16**(5), 1668–1693, 2004.
- **[Survey]** D. H. Sharp. *An overview of Rayleigh–Taylor instability.* Physica D **12**, 3–18, 1984.
- **[Survey]** Y. Zhou. *Rayleigh–Taylor and Richtmyer–Meshkov instability induced flow, turbulence, and mixing.* Physics Reports **720–722** and **723–725**, 2017.
- **[Survey]** D. Lannes. *The Water Waves Problem: Mathematical Analysis and Asymptotics.* AMS Mathematical Surveys and Monographs **188**, 2013.

## 10. Worked Example / Concrete Special Case

**Two-layer irrotational inviscid fluid with surface tension, $n=2$.** Take $\Omega^-=\{y<0\}$ with density $\rho^-$, $\Omega^+=\{y>0\}$ with $\rho^+>\rho^-$, gravity $-g e_y$, surface tension $\sigma_s$. Write the interface as $y=\eta(x,t)$ and velocity potentials $\phi^\pm$ with $\Delta\phi^\pm=0$, decaying as $y\to\mp\infty$.

Seek $\eta=\hat\eta\,e^{ikx+\lambda t}$, $\phi^-=Ae^{ky}e^{ikx+\lambda t}$, $\phi^+=Be^{-ky}e^{ikx+\lambda t}$ with $k>0$.

*Kinematic conditions* $\partial_t\eta=\partial_y\phi^\pm|_{y=0}$ give
$$\lambda\hat\eta = kA,\qquad \lambda\hat\eta = -kB \;\Longrightarrow\; A=\lambda\hat\eta/k,\; B=-\lambda\hat\eta/k.$$

*Dynamic condition.* Linearized Bernoulli gives $p^\pm|_{\Gamma}=-\rho^\pm(\partial_t\phi^\pm + g\eta)$, and $\llbracket p\rrbracket=\sigma_s\kappa=-\sigma_s\partial_x^2\eta=\sigma_s k^2\hat\eta$. Hence
$$-\rho^+(\lambda B + g\hat\eta) + \rho^-(\lambda A + g\hat\eta) = \sigma_s k^2\hat\eta.$$
Substituting $A,B$:
$$\frac{\lambda^2\hat\eta}{k}(\rho^++\rho^-) - g\hat\eta(\rho^+-\rho^-) = \sigma_s k^2\hat\eta,$$
$$\lambda^2 = \frac{g k(\rho^+-\rho^-)-\sigma_s k^3}{\rho^++\rho^-}.$$

**Numbers (water over air).** $\rho^+=1000$, $\rho^-=1.2\ \mathrm{kg\,m^{-3}}$, $g=9.81\ \mathrm{m\,s^{-2}}$, $\sigma_s=0.0728\ \mathrm{N\,m^{-1}}$.

- Cutoff: $k_c=\sqrt{g\Delta\rho/\sigma_s}=\sqrt{9800/0.0728}\approx 367\ \mathrm{m^{-1}}$, i.e. $\lambda_c=2\pi/k_c\approx 1.7\ \mathrm{cm}$. Ripples shorter than $1.7$ cm are stabilized — this is why a $1$ cm-wide inverted glass of water does not empty.
- Most unstable mode: $\frac{d}{dk}(gk\Delta\rho-\sigma_sk^3)=0\Rightarrow k_m=k_c/\sqrt3\approx 212\ \mathrm{m^{-1}}$, wavelength $\approx 3.0$ cm.
- Growth rate: $\lambda_{\max}^2 = k_m(g\Delta\rho-\sigma_sk_m^2)/(\rho^++\rho^-) = 212\,(9800-3266)/1001.2\approx 1.38\times10^3\ \mathrm{s^{-2}}$, so $\lambda_{\max}\approx 37\ \mathrm{s^{-1}}$: an e-folding time of $27$ ms.

**Where the open problem enters.** Set $\sigma_s=0$. Then $\lambda(k)=\sqrt{Agk}$ with $A\approx 0.9976$, and $\sup_k \lambda(k)=\infty$. For initial data $\eta_0$ with Fourier coefficients $\hat\eta_0(k)=e^{-\sqrt{k}}$ (analytic-type decay, in every $H^s$), the linear solution at time $t$ has $\hat\eta(k,t)=e^{-\sqrt k}\cosh(\sqrt{Agk}\,t)$, which for any $t>0$ fails to lie in $L^2$ once $\sqrt{Ag}\,t>1$. No continuous dependence holds in any $H^s$; the initial-value problem is ill-posed, and the linear analysis above tells us nothing about $h(t)$ beyond $t\approx 27$ ms. What replaces it — a mixing zone $h(t)=\alpha Agt^2$ with $\alpha$ determined by the PDE, or a genuinely non-unique family — is exactly the open question of Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*