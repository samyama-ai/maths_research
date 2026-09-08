---
id: 06-pdes/cahn-hilliard-droplet-formation
title: "Cahn Hilliard Droplet Formation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cahn–Hilliard Droplet Formation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/cahn-hilliard-droplet-formation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Cahn–Hilliard equation models phase separation in a binary mixture. Starting from a nearly uniform off-critical mixture (mean concentration close to one pure phase), solutions are observed to form a dilute population of nearly spherical droplets of the minority phase, which then coarsen: droplets shrink and disappear while the surviving ones grow, with mean radius $\bar R(t)\sim t^{1/3}$.

**The problem.** Give a rigorous derivation, from the Cahn–Hilliard PDE alone, of:

1. **(Droplet formation)** For off-critical initial data with small noise, solutions leave the metastable neighbourhood of the constant state and enter, on a well-defined time scale, a configuration that is $O(\varepsilon)$-close in a quantified sense to a finite union of disjoint balls of radii $\ge R_*$ (the critical nucleation radius), with a quantified statistical law for the number and size distribution of these droplets.
2. **(Droplet dynamics)** That the subsequent evolution is governed, to leading order in the volume fraction $\phi\to 0$, by the Lifshitz–Slyozov–Wagner (LSW) mean-field system.
3. **(Coarsening law)** That $\bar R(t)\sim t^{1/3}$, i.e. energy $E(t)\sim t^{-1/3}$, holds as a genuine two-sided asymptotic, not merely as a time-averaged upper bound.

A complete solution must prove all three for the PDE (not for a postulated droplet model), in dimension $d=2,3$, uniformly in $\varepsilon$, and must resolve the selection problem for the LSW self-similar profile: which of the one-parameter family of self-similar solutions is attained, and from which initial data. A disproof would exhibit initial data (or a generic class) for which the coarsening exponent differs from $1/3$, or for which the droplet ansatz fails.

## 2. Mathematical Foundations

Let $\Omega\subset\mathbb R^d$ be a bounded domain with Lipschitz boundary, or the torus $\mathbb T^d$. The **Cahn–Hilliard equation** with interfacial width $\varepsilon>0$ is

$$\partial_t u = \Delta \mu,\qquad \mu = -\varepsilon^2\Delta u + W'(u)\quad\text{in }\Omega\times(0,\infty),$$

with $\partial_\nu u=\partial_\nu\mu=0$ on $\partial\Omega$. Here $u$ is the (rescaled) concentration difference and $W$ is a double-well potential, canonically $W(u)=\tfrac14(1-u^2)^2$, with wells at $u=\pm1$.

Mass is conserved, $\frac{d}{dt}\fint_\Omega u=0$, and the Ginzburg–Landau energy

$$E_\varepsilon(u)=\int_\Omega \Big(\tfrac{\varepsilon}{2}|\nabla u|^2 + \tfrac1\varepsilon W(u)\Big)\,dx$$

decays: $\frac{d}{dt}E_\varepsilon(u)= -\varepsilon^{-1}\!\int_\Omega|\nabla\mu_\varepsilon|^2$ in the scaling $\mu_\varepsilon=-\varepsilon\Delta u+\varepsilon^{-1}W'(u)$. The equation is the $H^{-1}$ gradient flow of $E_\varepsilon$.

**Sharp-interface limit.** By Modica–Mortola, $E_\varepsilon \xrightarrow{\ \Gamma\ } \sigma\,\mathrm{Per}(\{u=1\})$ in $L^1$, with surface tension

$$\sigma=\int_{-1}^{1}\sqrt{2W(s)}\,ds=\tfrac{2\sqrt2}{3}.$$

The formal limit dynamics is the **Mullins–Sekerka (Hele-Shaw) free boundary problem**: for interface $\Gamma(t)=\partial\Omega^+(t)$,

$$\Delta v=0 \text{ in }\Omega\setminus\Gamma,\qquad v=\sigma\kappa \text{ on }\Gamma \ \ (\text{Gibbs–Thomson}),\qquad V=\tfrac12[\partial_\nu v]_\Gamma ,$$

with $\kappa$ the mean curvature and $V$ the normal velocity; this flow conserves volume and decreases area.

**Dilute droplet (LSW) regime.** Let the minority phase occupy volume fraction $\phi\ll1$ as $N$ balls of radii $R_i$. Screening is weak, and Mullins–Sekerka reduces to the mean-field system ($d=3$)

$$\dot R_i = \frac{1}{R_i}\Big(\frac{1}{R_*(t)}-\frac{1}{R_i}\Big),\qquad \frac{1}{R_*(t)}=\frac{\sum_i R_i}{\sum_i R_i^2},$$

with $\sum_i R_i^3$ conserved. Passing $N\to\infty$ gives the LSW kinetic equation for the number density $f(R,t)$,

$$\partial_t f + \partial_R\big(\dot R\,f\big)=0 .$$

LSW admits a one-parameter family of self-similar solutions with $\bar R(t)\sim t^{1/3}$; the classical Wagner profile is only one member (Niethammer–Pego).

**Nucleation.** For a spatially uniform off-critical state $\bar u$ with $|\bar u|$ inside the metastable region ($W''(\bar u)>0$ but $\bar u$ not a well), the constant state is a local but not global minimiser of $E_\varepsilon$ under the mass constraint; escape requires crossing a saddle whose critical point is a single droplet of radius $R_*$ — the **critical nucleus**.

## 3. History & State of the Art (SOTA)

- **1958.** Cahn and Hilliard introduce the free energy and the diffusion equation for a nonuniform binary system (*J. Chem. Phys.* 28).
- **1961.** Lifshitz–Slyozov and Wagner independently derive the mean-field ripening theory giving $\bar R\sim t^{1/3}$.
- **1986.** Elliott and Zheng Songmu establish global existence, uniqueness and regularity for the Cahn–Hilliard equation.
- **1989.** Pego gives the formal asymptotic derivation of Mullins–Sekerka as the $\varepsilon\to0$ limit.
- **1993–1994.** Bates and Fife analyse nucleation and the dynamics of the metastable escape; Alikakos, Bates and Chen prove convergence of Cahn–Hilliard to Mullins–Sekerka on the time interval of classical existence of the limit flow.
- **1996.** X. Chen proves a global-in-time weak (varifold/BV) convergence to a weak Mullins–Sekerka flow, allowing topological changes.
- **1998–2000.** Maier-Paape and Wanner rigorously justify spinodal decomposition — the linear-instability mechanism for *critical* mixtures — in $d\le3$.
- **2002.** Kohn and Otto introduce the interpolation/dissipation method giving the time-averaged upper bound $E(t)\gtrsim^{-1} t^{-1/3}$ in the critical case, without any droplet ansatz.
- **2005–2007.** Conti–Niethammer–Otto, and Otto–Rump–Slepčev, extend upper bounds to off-critical (droplet) mixtures, obtaining $t^{-1/3}$ for the Cahn–Hilliard/Mullins–Sekerka dynamics and rigorous rates for the droplet model itself.
- **1999–2001.** Niethammer and Otto make the screening length and the dilute limit rigorous for a static/quasi-static Ostwald ripening model; Niethammer–Pego show the LSW self-similar attractor is *not* unique and depends on the tail of the initial size distribution.

## 4. Partial Results / Verified Cases

- **Well-posedness.** Global existence, uniqueness, smoothness and a global attractor for $W$ polynomial of degree $4$, any $d\le3$ (Elliott–Zheng 1986; Temam). Logarithmic (Flory–Huggins) potentials handled by Elliott–Luckhaus.
- **Sharp-interface limit, smooth regime.** Alikakos–Bates–Chen (1994): if the Mullins–Sekerka problem has a smooth solution on $[0,T]$ with interface $\Gamma(t)$, then Cahn–Hilliard solutions with well-prepared data converge to it, with $O(\varepsilon)$ error in $L^\infty$. Valid all $d\ge2$.
- **Global weak limit.** X. Chen (1996): convergence to a weak (varifold) Mullins–Sekerka solution for all time, $d=2,3$, no smoothness assumed — but with no exclusion of surface-measure loss.
- **Single droplet / few droplets.** Alikakos–Fusco: exponentially slow motion and precise ODE reduction for $N$ well-separated small spheres in the dilute limit; the Gibbs–Thomson law is recovered with rigorous error bounds. Small-amplitude radially symmetric droplet solutions and their stability are fully classified.
- **Nucleation.** Bates–Fife (1993) prove existence of the critical-nucleus saddle point and characterise its instability index for $\bar u$ in the metastable band; combined with stochastic Cahn–Hilliard, Cassandro–Orlandi–Presutti–type large-deviation results give Arrhenius escape rates in $d=1$.
- **Coarsening upper bounds.** Kohn–Otto (2002): for critical mixtures,
  $$\frac1T\int_0^T E(t)\,dt \ \gtrsim\ T^{-1/3}\quad\text{for }T\gg1,$$
  i.e. coarsening cannot be *faster* than $t^{1/3}$, in a time-averaged sense, $d=2,3$. Conti–Niethammer–Otto (2006) extend to off-critical volume fraction $\phi$, with $\phi$-dependent crossover between $t^{1/3}$ and the $\phi$-dependent nucleation-dominated regime. Otto–Rump–Slepčev (2006) prove matching rigorous upper bounds directly for the droplet model.
- **LSW rigour.** Niethammer–Otto: rigorous derivation of the screening length $\ell\sim \bar R\,\phi^{-1/2}$ and of mean-field corrections to $O(\phi^{1/2})$ for the quasi-static problem. Niethammer–Pego: complete characterisation of domains of attraction of LSW self-similar profiles in terms of the regular variation of the initial distribution near its largest radius.
- **1D.** Complete: Bates–Xun classify slow motion of $N$-layer metastable states with $O(e^{-c/\varepsilon})$ velocities; coarsening in $d=1$ is logarithmic in time, not $t^{1/3}$, and is fully understood.

## 5. Principal Obstacles

- **No lower bound on coarsening.** All rigorous rate results are one-sided. There exist initial data (e.g. a periodic array of identical droplets) that do not coarsen at all; hence any $t^{1/3}$ *lower* bound must be conditional on a genericity or statistical hypothesis that nobody has formulated in a provable way. The Kohn–Otto interpolation inequality is intrinsically one-directional: it converts dissipation into a rate ceiling, and has no dual.
- **Loss of surface area in the weak limit.** Chen's global convergence permits the limiting varifold to carry hidden multiplicity or vanishing droplets; excluding this — an equipartition/no-collapse statement — is exactly the technical gap that blocks upgrading the weak limit to a droplet description.
- **Uncontrolled topological changes.** Mullins–Sekerka loses classical solvability at pinch-off and merging. Neither viscosity-solution theory (the flow is non-local, non-monotone, so there is no comparison principle) nor De Giorgi minimising-movement schemes are known to give uniqueness past a singularity.
- **Non-uniqueness of the LSW attractor.** Even granting the mean-field reduction, the self-similar profile is not selected: Niethammer–Pego show the exponent $1/3$ is universal but the shape is not, and the limit is unstable with respect to perturbations of the initial tail. So "the" $t^{1/3}$ law cannot be a statement about a unique attractor.
- **Nucleation is exponentially small.** Escape from metastability has rate $\exp(-\Delta E/\varepsilon^{d-1}\!\cdot\!\text{noise}^{-1})$; deterministic PDE methods cannot see it, and the required Eyring–Kramers asymptotics for the $H^{-1}$-gradient flow with conservation constraint are only known in $d=1$ and for finite-dimensional reductions.
- **Screening.** In $d=3$ the Green's function decays like $1/r$, so droplet interactions are long-range and only marginally summable; the mean-field closure is valid only after a subtle renormalisation whose error terms are $O(\phi^{1/2})$ — not small enough to close a rigorous $t\to\infty$ argument in which $\phi$ is fixed.

## 6. The Gap

Proven: (i) $\varepsilon\to0$ convergence to Mullins–Sekerka, either smooth on a finite time interval or weak globally; (ii) one-sided, time-averaged $t^{-1/3}$ energy bounds; (iii) full analysis of the LSW ODE/kinetic system *once it is assumed*.

Wanted: a bridge from (i) to (iii) that is uniform in time and in $\varepsilon$, plus a matching lower bound in (ii).

The precise missing step is a **quantitative rigidity/structure theorem**: show that a Cahn–Hilliard state whose energy is close to $\sigma\cdot$(perimeter of a union of balls) and whose dissipation is small over a long interval must in fact *be* a union of nearly spherical, well-separated droplets, with radii evolving by the Gibbs–Thomson ODE up to $O(\phi^{1/2})$ errors — and that this structure is propagated forward through droplet extinction events. Nothing in current technology propagates the droplet ansatz across the extinction of a droplet, which is precisely where coarsening happens.

## 7. Current Research (as of June 2026)

- **Quantitative sharp-interface limits.** The relative-entropy / relative-energy method of Fischer, Laux, Simon and Hensel gives weak–strong uniqueness and $O(\varepsilon)$ error estimates for Mullins–Sekerka-type flows, and is the leading candidate for extending Alikakos–Bates–Chen past singularities. Groups: Vienna (Fischer, IST Austria), Bonn/Leipzig (Laux, Otto's former school), Warwick.
- **De Giorgi / BV-solution frameworks.** Global-in-time BV solutions to Mullins–Sekerka with an energy-dissipation inequality, and uniqueness conditional on a calibration — a direct analogue of Laux's work for mean curvature flow. *(frontier — verify)*
- **Stochastic nucleation.** Sharp Eyring–Kramers asymptotics for the conservative stochastic Cahn–Hilliard/Cahn–Hilliard–Cook equation in $d=2$, via potential theory (Bovier–den Hollander programme) combined with the Da Prato–Debussche regularisation. *(frontier — verify)*
- **Coarsening lower bounds.** Attempts to prove statistical $t^{1/3}$ lower bounds for random initial data, using concentration and a "no accidental symmetry" argument. No published unconditional result.
- **Numerics.** Large-scale spectral and adaptive-FEM simulations with energy-stable convex-splitting schemes (Eyre, Shen–Yang) routinely confirm $\bar R\sim t^{1/3}$ over $3$–$4$ decades in $d=3$, and confirm the $\phi$-dependent crossover predicted by Conti–Niethammer–Otto.

## 8. Future Work

- Prove a **two-sided** coarsening law for a genericity class of initial data — e.g. for random data with a nondegenerate droplet size distribution, in the dilute limit $\phi\to0$ with $\phi$ fixed as $t\to\infty$.
- Extend the relative-entropy method to **multiple droplets with extinctions**, treating extinction as a controlled singularity rather than a breakdown time.
- Rigorously derive the LSW kinetic equation from Mullins–Sekerka with quantitative $O(\phi^{1/2})$ error, uniformly on $[0,\infty)$ after self-similar rescaling.
- Combine deterministic droplet dynamics with **thermal noise** to obtain a selection principle for the LSW self-similar profile — Otto's suggestion that noise regularises the Niethammer–Pego non-uniqueness.
- Settle whether the Cahn–Hilliard energy itself (not its time average) satisfies $E(t)\le C t^{-1/3}$ pointwise for large $t$.

## 9. Key References

- **[Foundational]** J. W. Cahn and J. E. Hilliard. *Free Energy of a Nonuniform System. I. Interfacial Free Energy.* Journal of Chemical Physics **28**, 258–267, 1958. [DOI](https://doi.org/10.1063/1.1744102)
- **[Foundational]** I. M. Lifshitz and V. V. Slyozov. *The kinetics of precipitation from supersaturated solid solutions.* Journal of Physics and Chemistry of Solids **19**, 35–50, 1961. [DOI](https://doi.org/10.1016/0022-3697(61)90054-3)
- **[Foundational]** C. M. Elliott and Zheng Songmu. *On the Cahn–Hilliard equation.* Archive for Rational Mechanics and Analysis **96**, 339–357, 1986.
- **[Foundational]** R. L. Pego. *Front migration in the nonlinear Cahn–Hilliard equation.* Proceedings of the Royal Society of London A **422**, 261–278, 1989. [DOI](https://doi.org/10.1098/rspa.1989.0027)
- **[Foundational]** L. Modica. *The gradient theory of phase transitions and the minimal interface criterion.* Archive for Rational Mechanics and Analysis **98**, 123–142, 1987. [DOI](https://doi.org/10.1007/bf00251230)
- **[SOTA]** N. D. Alikakos, P. W. Bates and X. Chen. *Convergence of the Cahn–Hilliard equation to the Hele-Shaw model.* Archive for Rational Mechanics and Analysis **128**, 165–205, 1994. [DOI](https://doi.org/10.1007/bf00375025)
- **[SOTA]** X. Chen. *Global asymptotic limit of solutions of the Cahn–Hilliard equation.* Journal of Differential Geometry **44**, 262–311, 1996. [DOI](https://doi.org/10.4310/jdg/1214458973)
- **[SOTA]** P. W. Bates and P. C. Fife. *The dynamics of nucleation for the Cahn–Hilliard equation.* SIAM Journal on Applied Mathematics **53**, 990–1008, 1993. [DOI](https://doi.org/10.1137/0153049)
- **[SOTA]** R. V. Kohn and F. Otto. *Upper bounds on coarsening rates.* Communications in Mathematical Physics **229**, 375–395, 2002.
- **[SOTA]** S. Conti, B. Niethammer and F. Otto. *Coarsening rates in off-critical mixtures.* SIAM Journal on Mathematical Analysis **37**, 1732–1741, 2006. [DOI](https://doi.org/10.1137/040620059)
- **[SOTA]** F. Otto, T. Rump and D. Slepčev. *Coarsening rates for a droplet model: rigorous upper bounds.* SIAM Journal on Mathematical Analysis **38**, 503–529, 2006. [DOI](https://doi.org/10.1137/050630192)
- **[SOTA]** B. Niethammer and R. L. Pego. *Non-self-similar behavior in the LSW theory of Ostwald ripening.* Journal of Statistical Physics **95**, 867–902, 1999. [DOI](https://doi.org/10.1023/a:1004546215920)
- **[SOTA]** B. Niethammer and F. Otto. *Ostwald ripening: the screening length revisited.* Calculus of Variations and PDE **13**, 33–68, 2001. [DOI](https://doi.org/10.1007/pl00009923)
- **[SOTA]** S. Maier-Paape and T. Wanner. *Spinodal decomposition for the Cahn–Hilliard equation in higher dimensions.* Archive for Rational Mechanics and Analysis **151**, 187–219, 2000. [DOI](https://doi.org/10.1007/s002050050196)
- **[SOTA]** J. Fischer, S. Hensel, T. Laux and T. M. Simon. *The local structure of the energy landscape in multiphase mean curvature flow: weak–strong uniqueness and stability of evolutions.* (relative-entropy method; see also Fischer–Hensel, ARMA 2020.)
- **[Survey]** A. Novick-Cohen. *The Cahn–Hilliard equation.* In *Handbook of Differential Equations: Evolutionary Equations*, Vol. 4, Elsevier, 2008.
- **[Survey]** A. Miranville. *The Cahn–Hilliard Equation: Recent Advances and Applications.* CBMS-NSF Regional Conference Series in Applied Mathematics **95**, SIAM, 2019.

## 10. Worked Example / Concrete Special Case

**Critical nucleus and the $t^{1/3}$ law in $d=3$.**

Take $\Omega=\mathbb T^3$, $W(u)=\frac14(1-u^2)^2$, so $\sigma=2\sqrt2/3$. Fix a supersaturated background $u\equiv \bar u = 1-\delta$ near the $+1$ well but with the $-1$ phase energetically favoured by a bulk driving force $\Delta f>0$ proportional to $\delta$.

*Step 1 — energy of a single droplet.* In the sharp-interface limit, a ball $B_R$ of the minority phase has excess energy

$$\mathcal E(R)=4\pi R^2\sigma-\tfrac43\pi R^3\,\Delta f .$$

*Step 2 — critical radius.* $\mathcal E'(R)=8\pi R\sigma-4\pi R^2\Delta f=0$ gives

$$R_*=\frac{2\sigma}{\Delta f},\qquad \mathcal E(R_*)=\frac{16\pi\sigma^3}{3\,\Delta f^2}.$$

With $\sigma=2\sqrt2/3\approx0.9428$ and $\Delta f=0.1$: $R_*\approx 18.9$ (in units of $\varepsilon$) and the barrier is $\mathcal E(R_*)\approx 16\pi(0.838)/(3\cdot 0.01)\approx 1.40\times10^{3}$. Since $\mathcal E''(R_*)=-8\pi\sigma<0$, $R_*$ is a **saddle**: droplets with $R<R_*$ shrink, $R>R_*$ grow. This is the rigorous content of Bates–Fife.

*Step 3 — droplet ODE.* For $N$ well-separated droplets in the dilute limit, Gibbs–Thomson plus quasi-static diffusion gives (after nondimensionalising $\sigma\mapsto1$)

$$\dot R_i=\frac{1}{R_i}\Big(\frac1{R_*(t)}-\frac1{R_i}\Big),\qquad \frac{d}{dt}\sum_i R_i^3=0 .$$

*Step 4 — the exponent.* Try $\bar R(t)=(\alpha t)^{1/3}$. Then $\bar R^2\dot{\bar R}=\alpha/3$ is constant, matching the right-hand side $\big(R_*^{-1}-R^{-1}\big)$ being $O(1/\bar R)$ times $\bar R$… concretely, the balance $\dot R\sim 1/R^2$ integrates to $R^3\sim 3t$. Mass conservation $N\bar R^3=\text{const}$ then forces $N(t)\sim t^{-1}$: droplet number decays like $1/t$, and total interfacial energy

$$E(t)\sim \sigma N\bar R^2\sim t^{-1}\cdot t^{2/3}= t^{-1/3},$$

which is exactly the exponent that Kohn–Otto bound from one side.

*Step 5 — where the proof breaks.* Steps 3–4 assume the configuration *is* a set of separated balls at every time. The extinction event $R_i(t_i)\to0$ is a topological change: at $t=t_i$, Mullins–Sekerka loses classical solvability, and no known argument re-establishes the droplet ansatz for $t>t_i$ from the PDE. Since $N(t)\sim t^{-1}$ means infinitely many extinctions on $[1,\infty)$, the ansatz must survive infinitely many such events — and that propagation is precisely the open problem of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*