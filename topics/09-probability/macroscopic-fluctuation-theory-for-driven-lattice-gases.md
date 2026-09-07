---
id: 09-probability/macroscopic-fluctuation-theory-for-driven-lattice-gases
title: "Macroscopic Fluctuation Theory for Driven Lattice Gases"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Macroscopic Fluctuation Theory for Driven Lattice Gases

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/macroscopic-fluctuation-theory-for-driven-lattice-gases` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Macroscopic fluctuation theory (MFT) is a proposed closed variational description of large deviations in diffusive interacting particle systems out of equilibrium. The problem is to establish it as a theorem, at the level of generality in which it is used.

Let $\eta_t$ be a conservative lattice gas on $\Lambda_N = (\mathbb{Z}/N\mathbb{Z})^d$ or on a domain $\Lambda \subset \mathbb{R}^d$ discretized at scale $1/N$, driven out of equilibrium by boundary reservoirs at densities $b(\cdot)$ and/or by an external field $E$. Under diffusive rescaling $t \mapsto N^2 t$, the empirical density $\pi^N_t(dx) = N^{-d}\sum_i \eta_t(i)\delta_{i/N}(dx)$ is conjectured to satisfy a large deviation principle with speed $N^d$ and rate functional determined by only two macroscopic transport coefficients, the diffusivity $D(\rho)$ (a $d\times d$ matrix) and the mobility $\sigma(\rho)$.

**Conjecture (MFT).** For a broad class of driven lattice gases with a single conserved quantity:

1. **(Dynamical LDP)** $\mathbb{P}[\pi^N_\cdot \approx \rho_\cdot] \asymp \exp(-N^d I_{[0,T]}(\rho))$ with the explicit functional of Section 2.
2. **(Static LDP / quasipotential)** The stationary measures $\mu_N$ satisfy $\mu_N[\pi^N \approx \rho] \asymp \exp(-N^d V(\rho))$, where $V$ is the quasipotential $V(\rho)=\inf\{I_{(-\infty,0]}(\hat\rho): \hat\rho(0)=\rho,\ \hat\rho(-\infty)=\bar\rho\}$, and $V$ is the unique (viscosity) solution of the associated infinite-dimensional Hamilton–Jacobi equation.
3. **(Current LDP)** The time-averaged empirical current obeys an LDP whose rate function is the contraction of $I$, with the Gallavotti–Cohen symmetry built in.

A complete resolution requires proving (1)–(3) for models where $D$ and $\sigma$ are not both constant and where no explicit invariant measure or duality is available, together with well-posedness of the Hamilton–Jacobi equation for $V$.

## 2. Mathematical Foundations

**Hydrodynamic scaling.** The law of large numbers is the quasilinear parabolic equation
$$\partial_t \rho = \nabla\!\cdot\!\big(D(\rho)\nabla\rho - \sigma(\rho)E\big), \qquad \rho|_{\partial\Lambda}=b .$$
The coefficients satisfy the local Einstein (fluctuation–dissipation) relation
$$D(\rho) = \sigma(\rho)\, f''_{\mathrm{eq}}(\rho),$$
with $f_{\mathrm{eq}}$ the equilibrium free-energy density. In Green–Kubo form, $\sigma(\rho)$ is the variance of the time-integrated current in the equilibrium system at density $\rho$.

**Dynamical rate functional.** Write the fluctuating hydrodynamics
$$\partial_t\rho = \nabla\!\cdot\!\big(D(\rho)\nabla\rho - \sigma(\rho)E\big) + \nabla\!\cdot\!\big(\sqrt{\sigma(\rho)/N^{d}}\, \xi\big),$$
$\xi$ a space–time white noise. The Freidlin–Wentzell functional is
$$I_{[0,T]}(\rho) \;=\; \frac{1}{2}\int_0^T\!\! dt \;\big\langle\, j - J(\rho)\,,\; \sigma(\rho)^{-1}\big(j-J(\rho)\big)\big\rangle,$$
where $J(\rho) = -D(\rho)\nabla\rho + \sigma(\rho)E$ and $j$ is the unique current with $\partial_t\rho + \nabla\!\cdot j = 0$. Equivalently, in $H^{-1}$-type variational form,
$$I_{[0,T]}(\rho)=\sup_{H}\Big\{\int_0^T\!\!\langle \partial_t\rho, H\rangle - \langle J(\rho),\nabla H\rangle - \tfrac12\langle \sigma(\rho)\nabla H,\nabla H\rangle \,dt\Big\},$$
the supremum over $H \in C^{1,2}_0$.

**Hamilton–Jacobi equation for the quasipotential.**
$$\Big\langle \nabla \frac{\delta V}{\delta \rho},\; \sigma(\rho)\,\nabla\frac{\delta V}{\delta\rho}\Big\rangle \;-\; 2\Big\langle \frac{\delta V}{\delta \rho},\; \nabla\!\cdot\! J(\rho)\Big\rangle \;=\; 0 .$$
MFT asserts $V$ is the relevant solution and that the adjoint ("time-reversed") hydrodynamics is $\partial_t\rho = \nabla\!\cdot(D\nabla\rho - \sigma E) - 2\nabla\!\cdot(\sigma(\rho)\nabla \tfrac{\delta V}{\delta\rho})$. In equilibrium ($E=0$, $b$ constant) $V$ reduces to the local free energy $\int_\Lambda [f(\rho)-f(\bar\rho)-f'(\bar\rho)(\rho-\bar\rho)]dx$; out of equilibrium $V$ is generically **nonlocal**, which is the theory's signature prediction.

**Current LDP and additivity.** For the time-averaged current $j$ in $d=1$, the additivity principle of Bodineau–Derrida gives
$$\mathcal{F}(j)=\min_{\rho(\cdot)}\int_0^1 \frac{\big(j + D(\rho)\rho'\big)^2}{2\sigma(\rho)}\,dx,$$
valid only when the optimal profile is time-independent.

## 3. History & State of the Art (SOTA)

- **1989.** Kipnis, Olla, Varadhan prove the dynamical LDP for the symmetric simple exclusion process (SSEP), the first rigorous instance of the functional above (CPAM 42).
- **1995–1999.** Extensions to mean-zero asymmetric attractive processes (Benois–Kipnis–Landim), zero-range and Ginzburg–Landau dynamics; systematized in Kipnis–Landim's monograph.
- **1998.** Derrida–Lebowitz compute the exact current large deviation function for ASEP by Bethe ansatz, exhibiting the Gallavotti–Cohen symmetry.
- **2001.** Derrida–Lebowitz–Speer obtain the exact nonlocal free-energy functional of the boundary-driven SSEP via matrix product ansatz.
- **2001–2002.** Bertini, De Sole, Gabrielli, Jona-Lasinio, Landim formulate MFT (PRL 87, 040601; JSP 107, 635) and rederive DLS from the Hamilton–Jacobi equation.
- **2004–2005.** Bodineau–Derrida: additivity principle and its breakdown; dynamical phase transition to time-dependent optimal profiles.
- **2009.** Bertini–Landim–Mourragui: rigorous dynamical LDP for the boundary-driven weakly asymmetric exclusion process (Ann. Probab. 37).
- **2015.** The Rev. Mod. Phys. review consolidates the theory.
- **2016–2024.** Rigorous quasipotential results, $\Gamma$-convergence/gradient-flow reformulations (Mielke–Peletier–Renger), and exact-solution cross-checks from integrable probability.

## 4. Partial Results / Verified Cases

Rigorously established:

- **SSEP, $d\ge1$, periodic or boundary-driven:** full dynamical LDP with matching upper and lower bounds (Kipnis–Olla–Varadhan 1989; Bertini–Landim–Mourragui 2009 for the driven case). Here $D\equiv 1$, $\sigma(\rho)=\rho(1-\rho)$.
- **Weakly asymmetric exclusion, field $E=O(1/N)$ at the lattice scale:** LDP proven; strong asymmetry $E=O(1)$ is not covered.
- **Zero-range and misanthrope processes with Lipschitz, monotone jump rates:** hydrodynamics and LDP under attractiveness/gradient conditions.
- **Gradient models** (where the microscopic current is a discrete gradient) with $\sigma$ smooth and strictly positive on $(0,1)$: the replacement/superexponential lemmas close, so both bounds hold.
- **Quasipotential:** exact for boundary-driven SSEP (DLS 2001) and for the KMP energy-transport model in $d=1$; Farfan–Landim–Mourragui and Bertini et al. verify the Hamilton–Jacobi characterization in these cases.
- **Static LDP:** proven for boundary-driven SSEP; the rate function is the DLS functional, confirming nonlocality.
- **Additivity principle:** proven to give the true current LDF in $d=1$ when $\sigma''(\rho)\le 0$ with $D$ constant (SSEP: $\sigma''=-2$). It is known to **fail** for KMP ($\sigma(\rho)=\rho^2$, $\sigma''=2>0$) at large current deviations, where travelling-wave optimal profiles take over.

Not established in general: non-gradient models (e.g. general lattice gases where $D(\rho)$ is defined only by a variational Green–Kubo formula), $d\ge2$ with $E=O(1)$, and models with degenerate $\sigma$ (kinetically constrained gases, facilitated exclusion).

## 5. Principal Obstacles

- **Non-gradient models.** $D(\rho)$ exists only as a Varadhan-type variational formula; there is no microscopic identity expressing the current as a gradient. Varadhan's non-gradient method yields the hydrodynamic limit but the LDP requires uniform-in-$\rho$ control of the fluctuation–dissipation decomposition and of the spectral gap, which is not available.
- **Superexponential replacement.** The upper bound needs local-equilibrium replacement with error $o(e^{-CN^d})$. Existing proofs use the entropy/Dirichlet-form estimate plus the two-blocks lemma, which is tight only when the reference measure is product and reversible — false for driven systems.
- **Density of regular paths.** The matching lower bound requires that any $\rho$ with $I(\rho)<\infty$ be approximable in the $I$-topology by smooth paths with strictly positive density bounded away from $0,1$, obtained by perturbing with $H\in C^{1,2}$. This is a $\Gamma$-density statement that is open whenever $\sigma$ vanishes at the boundary of the density range and $D$ is nonconstant.
- **Strong drive.** For $E=O(1)$ the correct scaling is hyperbolic; solutions of the conservation law are non-unique (entropy solutions), the rate function is only lower semicontinuous with non-matching bounds (Varadhan's ASEP problem), and diffusive MFT does not apply.
- **Hamilton–Jacobi in infinite dimensions.** No general uniqueness/viscosity theory for the functional equation above; comparison principles for gradients in $H^{-1}$ with degenerate $\sigma$ are missing, so "the" quasipotential is not known to be well-defined.

## 6. The Gap

Proven: models that are simultaneously (a) gradient, (b) attractive or with product reversible reference measure, (c) diffusively scaled with $E=O(1/N)$, (d) $\sigma$ smooth. Conjectured: all diffusive conservative dynamics with well-defined $(D,\sigma)$.

The precise missing step is a superexponential local-equilibrium estimate at speed $N^d$ for non-gradient, non-reversible dynamics, combined with a $\Gamma$-density theorem for paths of finite $I$. Separately, even given the dynamical LDP, deducing the static LDP requires proving that the quasipotential defined by the infimum coincides with the unique viscosity solution of the Hamilton–Jacobi equation — currently verified only where an exact solution exists.

## 7. Current Research (as of June 2026)

- **Rome/IMPA/Leiden school** (Bertini, Landim, Jona-Lasinio's successors, Gabrielli): quasipotential regularity, boundary-driven models with several conserved quantities.
- **Gradient-flow/GENERIC reformulations** (Mielke, Peletier, Renger; Berlin–Eindhoven): MFT functionals as $\Gamma$-limits of microscopic relative-entropy functionals, giving a route to the lower bound without path-density arguments. *(frontier — verify)*
- **Weak-solution/kinetic approaches to non-gradient LDPs** (Quastel-school, Jara, Menezes): stochastic Burgers/KPZ scaling and energy solutions used to control the crossover regime $E \sim N^{-\gamma}$, $\gamma\in(0,1)$. *(frontier — verify)*
- **Integrable-probability cross-validation:** exact current cumulants for ASEP/KPZ fixed point used to test MFT predictions in the weakly asymmetric limit.
- **Dynamical phase transitions:** rigorous confirmation of the Bodineau–Derrida symmetry-breaking transition in KMP-type models, and of travelling-wave optimal profiles.

## 8. Future Work

- Prove the dynamical LDP for one genuinely non-gradient model (e.g. lattice gases with energy exchange, or the Kawasaki dynamics of the Ising lattice gas above $T_c$).
- Develop a viscosity-solution theory for the Hamilton–Jacobi equation on the space of densities, with a comparison principle valid for degenerate $\sigma$.
- Extend MFT to systems with several conserved fields (mass, momentum, energy) where $\sigma$ is a matrix and Onsager symmetry must be proven, not assumed.
- Classify dynamical phase transitions in the current LDF by convexity properties of $\sigma$ and $D$.
- Establish MFT for long-range/anomalous models where the limit is fractional and the diffusive ansatz fails.

## 9. Key References

- **[Foundational]** C. Kipnis, S. Olla, S. R. S. Varadhan. *Hydrodynamics and large deviation for simple exclusion processes.* Communications on Pure and Applied Mathematics 42 (1989), 115–137.
- **[Foundational]** C. Kipnis, C. Landim. *Scaling Limits of Interacting Particle Systems.* Grundlehren der mathematischen Wissenschaften 320, Springer, 1999.
- **[Foundational]** L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim. *Fluctuations in stationary nonequilibrium states of irreversible processes.* Physical Review Letters 87 (2001), 040601.
- **[Foundational]** L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim. *Macroscopic fluctuation theory for stationary non-equilibrium states.* Journal of Statistical Physics 107 (2002), 635–675.
- **[Survey]** L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim. *Macroscopic fluctuation theory.* Reviews of Modern Physics 87 (2015), 593–636.
- **[Foundational]** B. Derrida, J. L. Lebowitz. *Exact large deviation function in the asymmetric exclusion process.* Physical Review Letters 80 (1998), 209–213.
- **[Foundational]** B. Derrida, J. L. Lebowitz, E. R. Speer. *Free energy functional for nonequilibrium systems: an exact result.* Physical Review Letters 87 (2001), 150601.
- **[SOTA]** T. Bodineau, B. Derrida. *Current fluctuations in nonequilibrium diffusive systems: an additivity principle.* Physical Review Letters 92 (2004), 180601.
- **[SOTA]** L. Bertini, C. Landim, M. Mourragui. *Dynamical large deviations for the boundary driven weakly asymmetric exclusion process.* Annals of Probability 37 (2009), 2357–2403.
- **[SOTA]** L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim. *Non equilibrium current fluctuations in stochastic lattice gases.* Journal of Statistical Physics 123 (2006), 237–276.
- **[Survey]** B. Derrida. *Non-equilibrium steady states: fluctuations and large deviations of the density and of the current.* Journal of Statistical Mechanics: Theory and Experiment (2007), P07023.
- **[Related]** L. Bertini, G. Giacomin. *Stochastic Burgers and KPZ equations from particle systems.* Communications in Mathematical Physics 183 (1997), 571–607.

## 10. Worked Example / Concrete Special Case

**Boundary-driven SSEP on $\{1,\dots,N-1\}$, reservoirs $\rho_0=1$ at the left, $\rho_1=0$ at the right.** Macroscopic domain $\Lambda=(0,1)$, coefficients $D(\rho)=1$, $\sigma(\rho)=\rho(1-\rho)$, field $E=0$.

*Step 1 — stationary profile.* The hydrodynamic equation $\partial_t\rho=\partial_x^2\rho$ with $\rho(0)=1,\rho(1)=0$ has the stationary solution
$$\bar\rho(x)=1-x .$$

*Step 2 — mean current.* $J=-\partial_x\bar\rho = 1$ (in macroscopic units; microscopically the current is $\sim 1/N$).

*Step 3 — Gaussian current fluctuations from the additivity principle.* Expanding $\mathcal{F}(j)$ around $j=J$ with $\rho$ frozen at $\bar\rho$,
$$\mathrm{Var}(j)\;=\;\int_0^1\sigma(\bar\rho(x))\,dx\;=\;\int_0^1 x(1-x)\,dx\;=\;\tfrac16 .$$
So the time-averaged current over a window $T$ has $\mathcal{F}(j)\approx \tfrac{3}{1}(j-1)^2 = 3(j-1)^2$ to leading order, i.e. fluctuations of size $\sqrt{1/(6T N^{d})}$. Because $\sigma''=-2<0$, the additivity principle is exact here: the optimal profile stays time-independent for all $j$, and $\mathcal{F}$ is the true rate function.

*Step 4 — the nonlocal quasipotential.* For general reservoir densities $\rho_0>\rho_1$, solving the Hamilton–Jacobi equation reproduces the Derrida–Lebowitz–Speer functional
$$V(\rho)=\int_0^1\!\Big[\rho\log\frac{\rho}{F}+(1-\rho)\log\frac{1-\rho}{1-F}+\log\frac{F'}{\rho_1-\rho_0}\Big]dx,$$
where the auxiliary field $F$ solves
$$\frac{F''}{F'}=\frac{(\rho-F)(F')}{F(1-F)},\qquad F(0)=\rho_0,\;F(1)=\rho_1 .$$
$F$ depends on $\rho$ over the whole interval: $V$ is not an integral of a local function of $\rho(x)$. This is the concrete signature of nonequilibrium — at $\rho_0=\rho_1=\bar\rho$ one gets $F\equiv\bar\rho$ and $V$ collapses to the local Bernoulli relative entropy $\int_0^1[\rho\log\frac{\rho}{\bar\rho}+(1-\rho)\log\frac{1-\rho}{1-\bar\rho}]dx$.

*Step 5 — what is and is not proven here.* Steps 1–4 are theorems for SSEP: the dynamical LDP (Kipnis–Olla–Varadhan), the static LDP with $V$ as above (Derrida–Lebowitz–Speer; Bertini et al.), and the current LDF. Replace $\sigma(\rho)=\rho(1-\rho)$ by the mobility of a non-gradient lattice gas, and every step above becomes conjectural: even $D(\rho)$ is then only a variational object, and the superexponential replacement lemma underpinning Step 1's large deviation upper bound has no known proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*