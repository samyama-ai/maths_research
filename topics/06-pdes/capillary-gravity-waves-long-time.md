---
id: 06-pdes/capillary-gravity-waves-long-time
title: "Global Existence for the Two-Dimensional Water Wave Equation with Surface Tension and Vorticity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Existence for the Two-Dimensional Water Wave Equation with Surface Tension and Vorticity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/capillary-gravity-waves-long-time` · **Status:** open

## 1. Problem Statement / Conjecture

Consider a two-dimensional incompressible, inviscid fluid of infinite depth occupying a region $\Omega(t)\subset\mathbb{R}^2$ below a free interface $\Sigma(t)$, subject to gravity $g>0$ and surface tension $\sigma>0$, with **nonzero vorticity** $\omega=\mathrm{curl}\,v$.

**Conjecture (global existence and modified scattering).** For $\sigma>0$, $g>0$ and constant vorticity $\omega\equiv\gamma\neq 0$, there is $N$ large and $\varepsilon_0>0$ such that every initial interface/velocity pair with
$$\|\eta_0\|_{H^{N+1/2}}+\|\psi_0\|_{\dot H^{N}}+\||x|\partial_x(\eta_0,\psi_0)\|_{L^2}\ \le\ \varepsilon\ <\ \varepsilon_0$$
and satisfying the Rayleigh–Taylor and chord-arc conditions launches a unique solution that is **global in time**, remains of size $O(\varepsilon)$ in the energy norm, decays as $\|\partial_x\eta(t)\|_{L^\infty}\lesssim \varepsilon\,\langle t\rangle^{-1/2}$, and scatters in a modified (logarithmically or phase-corrected) sense.

A complete resolution requires either (i) a proof of the above, or (ii) a construction of small, smooth, decaying data whose solution loses regularity, has $\|\partial_x \eta\|_{L^\infty}$ growing, or ceases to exist in finite time. Two weaker, still-open milestones are: an **almost-global** bound $T_\varepsilon \ge \exp(c/\varepsilon)$, and a **quartic** lifespan $T_\varepsilon\gtrsim\varepsilon^{-3}$. The irrotational case $\gamma=0$ with **both** $g>0$ and $\sigma>0$ in 2D is already open; the vorticity adds a second layer of difficulty.

## 2. Mathematical Foundations

Let $\Sigma(t)=\{(x,\eta(t,x)):x\in\mathbb{R}\}$, $\Omega(t)=\{y<\eta(t,x)\}$. The free-boundary Euler system is
$$\partial_t v+(v\cdot\nabla)v=-\nabla p-g e_2,\qquad \nabla\cdot v=0\ \text{ in }\Omega(t),$$
$$p\big|_{\Sigma(t)}=-\sigma\,\kappa,\qquad \kappa=\partial_x\!\left(\frac{\partial_x\eta}{\sqrt{1+(\partial_x\eta)^2}}\right),\qquad \partial_t+v\cdot\nabla \text{ tangent to } \bigcup_t\Sigma(t).$$

**Irrotational reduction (Zakharov–Craig–Sulem).** If $\omega\equiv 0$, set $\psi(t,x)=\phi(t,x,\eta(t,x))$ with $v=\nabla\phi$. With the Dirichlet–Neumann operator $G(\eta)\psi=\sqrt{1+(\partial_x\eta)^2}\,\partial_n\phi|_\Sigma$,
$$\partial_t\eta=G(\eta)\psi,\qquad
\partial_t\psi=-g\eta+\sigma\kappa-\tfrac12(\partial_x\psi)^2+\frac{(G(\eta)\psi+\partial_x\eta\,\partial_x\psi)^2}{2(1+(\partial_x\eta)^2)} .$$
This is Hamiltonian with $H=\frac12\int \psi G(\eta)\psi\,dx+\frac{g}{2}\int\eta^2dx+\sigma\int(\sqrt{1+(\partial_x\eta)^2}-1)dx$ and Darboux pair $(\eta,\psi)$.

**Constant vorticity.** For $\omega\equiv\gamma$, write $v=\gamma(-y,0)+\nabla\phi$; the system remains a two-unknown evolution in $(\eta,\psi)$, with extra quadratic transport-type terms proportional to $\gamma$ (Constantin–Ivanov–Prodanov; Wahlén's Hamiltonian formulation). The linearized dispersion relation at infinite depth becomes
$$\omega_\pm(\xi)=-\frac{\gamma}{2}\,\mathrm{sgn}(\xi)\ \pm\ \sqrt{\,g|\xi|+\sigma|\xi|^3+\tfrac{\gamma^2}{4}\,},$$
degenerating to the irrotational gravity–capillary relation $\omega(\xi)=\sqrt{g|\xi|+\sigma|\xi|^3}$ when $\gamma=0$.

**Local theory hypotheses.** Local well-posedness with $\sigma>0$ does *not* require the Rayleigh–Taylor sign condition $-\partial_n p>0$ (surface tension regularizes the interface at order $3/2$), but it does require a chord–arc/non-self-intersection condition. With $\sigma=0$ the Taylor sign condition is essential (Wu).

**Decay and normal forms.** Linear solutions of $\partial_t u = -i\Lambda u$, $\Lambda=\omega(D)$, decay like $t^{-1/2}$ in 2D when $\omega''\neq0$. The quadratic nonlinearity is *not* integrable against $t^{-1/2}$, so global existence requires normal-form or space-time-resonance removal of the quadratic terms, controlled by the resonance sets
$$\mathcal{R}=\{(\xi,\eta):\ \omega(\xi)=\omega(\eta)+\omega(\xi-\eta)\},\qquad \mathcal{R}_{st}=\mathcal{R}\cap\{\nabla_\eta[\omega(\eta)+\omega(\xi-\eta)]=0\}.$$

## 3. History & State of the Art (SOTA)

- **1968.** Zakharov identifies the Hamiltonian structure of the irrotational water wave problem.
- **1997/1999.** S. Wu proves local well-posedness for 2D and 3D gravity water waves in Sobolev spaces without smallness (Invent. Math.).
- **2005.** Ambrose–Masmoudi prove local well-posedness for 2D water waves **with surface tension** and the zero-surface-tension limit; Lindblad handles free-boundary Euler with vorticity (Ann. of Math.).
- **2007.** Coutand–Shkoller prove local well-posedness for free-surface Euler with vorticity, with and without surface tension (J. Amer. Math. Soc.); Shatah–Zeng give geometric a priori estimates (CPAM 2008).
- **2009–2011.** Wu: almost-global existence ($\exp(c/\varepsilon)$) for 2D gravity waves; global existence for 3D gravity waves. Germain–Masmoudi–Shatah: global 3D gravity waves via space-time resonances (Ann. of Math. 2012).
- **2015.** Ionescu–Pusateri and Alazard–Delort independently prove **global existence with modified scattering for 2D gravity waves** ($\sigma=0$, irrotational).
- **2015–2018.** Germain–Masmoudi–Shatah: global existence for 3D **capillary** waves ($g=0$). Ionescu–Pusateri: global regularity for 2D water waves with surface tension in the pure-capillary regime ($g=0$). Deng–Ionescu–Pausader–Pusateri: global existence for the full 3D **gravity–capillary** system (Acta Math. 2017).
- **2017–2019.** Ifrim–Tataru: holomorphic-coordinate method; cubic lifespan $\varepsilon^{-2}$ for 2D capillary waves and for 2D gravity waves with **constant vorticity**.
- **2020s.** Berti–Delort (periodic gravity–capillary almost-global with parameter excision); Berti–Feola–Pusateri (Birkhoff normal form, periodic gravity waves); Berti–Maspero–Murgante (paradifferential Birkhoff normal form, constant vorticity).

**SOTA on the exact problem stated in §1:** the best unconditional lifespan for 2D gravity–capillary waves with constant vorticity is **cubic**, $T_\varepsilon\gtrsim\varepsilon^{-2}$. No almost-global or global result is known.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| 2D, $\sigma=0$, $\gamma=0$, infinite depth | Global, modified scattering | Ionescu–Pusateri (2015); Alazard–Delort (2015) |
| 2D, $g=0$, $\sigma>0$, $\gamma=0$ (pure capillary) | Global regularity, modified scattering | Ionescu–Pusateri (Mem. AMS, 2018) |
| 3D, $g>0,\sigma>0$, $\gamma=0$ | Global | Deng–Ionescu–Pausader–Pusateri (2017) |
| 3D, $g>0,\sigma=0$ / $g=0,\sigma>0$ | Global | Wu (2011); Germain–Masmoudi–Shatah (2012, 2015) |
| 2D, $\sigma>0$, $\gamma=0$ or $\gamma$ const. | $T_\varepsilon\gtrsim\varepsilon^{-2}$ (cubic lifespan) | Ifrim–Tataru (ARMA 2017; Anal. PDE 2019) |
| 2D periodic, $g,\sigma>0$, $\gamma=0$ | Almost-global $T\gtrsim\varepsilon^{-N}$ for $\sigma$ outside a null set of parameters | Berti–Delort (2018) |
| 2D, $\sigma=0$, $\gamma$ const., periodic | Almost-global / long-time Birkhoff normal form | Berti–Maspero–Murgante (2023–24) *(frontier — verify)* |
| 2D, point vortices below interface | Long-time existence, $\varepsilon^{-2}$-type bounds | Su (CMP 2020) |
| Any $\sigma\ge0$, general vorticity | Local well-posedness only | Lindblad (2005); Coutand–Shkoller (2007); Zhang–Zhang (2008) |

Numerically, Wilton-ripple bifurcation branches and the $2\!:\!1$ resonance have been computed to high accuracy (Wilton 1915; Vanden-Broeck; Akers–Nicholls), and time-dependent simulations show recurrent energy exchange between $k$ and $2k$ modes rather than blow-up — empirical support for the conjecture but not proof.

## 5. Principal Obstacles

1. **Quadratic resonances are nonempty (Wilton ripples).** For $\omega(k)=\sqrt{gk+\sigma k^3}$ the 2:1 resonance $\omega(2k)=2\omega(k)$ has a genuine solution at $k_\ast=\sqrt{g/(2\sigma)}$ (§10). The normal-form transformation removing the quadratic terms therefore has a **vanishing denominator** on a nonempty set — the mechanism that made pure-gravity ($\sigma=0$) and pure-capillary ($g=0$) 2D problems tractable is unavailable. In 3D the resonance set is lower-dimensional and transversality recovers integrability; in 2D there is no room to spend.
2. **Loss of derivatives in the normal form.** The water wave nonlinearity is quasilinear: naive normal forms lose $1/2$ (gravity) or $3/2$ (capillary) derivatives. Combining resonance-set analysis with a paradifferential/holomorphic framework that avoids derivative loss is delicate, and the two techniques have different natural function spaces.
3. **Vorticity destroys the closed two-unknown structure.** For general $\omega$, the interface evolution is coupled to a transported bulk vorticity field with no dispersive decay; the Zakharov Hamiltonian structure is lost. Constant vorticity preserves closure but breaks the $\xi\mapsto-\xi$ symmetry of the dispersion relation (the $-\tfrac\gamma2\mathrm{sgn}(\xi)$ term), enlarging the resonance set and destroying the parity cancellations used in the irrotational proofs.
4. **Degenerate group velocity.** $\omega''$ vanishes at $|\xi|=\xi_c$ where $\partial_\xi^2\sqrt{g\xi+\sigma\xi^3}=0$, so the stationary-phase $t^{-1/2}$ decay degenerates to $t^{-1/3}$ near a frequency — insufficient to close a bootstrap on its own.
5. **No conserved quantity controls high frequencies.** Energy conservation gives $H^{3/2}$-level control only; all higher Sobolev norms are propagated by a Gronwall argument whose exponent is the very quantity being bounded.

## 6. The Gap

Proven: **cubic** lifespan $T_\varepsilon\gtrsim\varepsilon^{-2}$ via a single normal-form/modified-energy step that removes the quadratic terms *away from* the resonant set and absorbs the resonant contribution into an energy correction bounded on the cubic time scale. Claimed: $T_\varepsilon=\infty$.

The exact missing step is the **treatment of the resonant quadratic interaction at $k_\ast=\sqrt{g/2\sigma}$ on time scales beyond $\varepsilon^{-2}$.** One must show that the $(k_\ast,k_\ast)\to 2k_\ast$ interaction either (a) is genuinely null — the symbol of the resonant quadratic term vanishes on $\mathcal{R}_{st}$, as happened for 2D gravity waves — or (b) drives only a bounded, phase-type correction (an integrable ODE system on the resonant manifold) rather than secular growth. Neither is established. With $\gamma\neq0$, one must additionally decide whether the $\gamma$-shifted resonance set stays a finite union of transverse curves or acquires tangencies. **No known computation of the resonant symbol at $k_\ast$ for $g,\sigma>0$ has been shown to vanish.**

## 7. Current Research (as of June 2026)

- **Paradifferential Birkhoff normal forms** (Berti, Feola, Maspero, Murgante, Pusateri; SISSA / Sapienza / Zürich): iterated normal forms preserving Hamiltonian structure and avoiding derivative loss, so far in the **periodic** setting, yielding $T\gtrsim\varepsilon^{-N}$ for generic $(g,\sigma)$ outside measure-zero sets. Extending to the line and to $\gamma\neq0$ is the active frontier *(frontier — verify)*.
- **Holomorphic coordinates** (Ifrim, Tataru, Hunter, Harrop-Griffiths; Berkeley / UCSB): exact algebraic structure of the 2D problem; quartic-lifespan and modified-scattering statements for constant vorticity in the presence of surface tension are the announced targets *(frontier — verify)*.
- **Space-time resonances / $Z$-norm method** (Ionescu, Pusateri, Deng, Pausader; Princeton / Toronto): pushing the 3D gravity–capillary machinery down to 2D by exploiting the finiteness of the resonant frequency set.
- **Vorticity beyond constant** (Coutand, Shkoller, Zhang, Su, Wang): long-time behavior with point vortices and with compactly supported vorticity; the coupling of a non-dispersive vorticity field to a dispersive interface is largely unexplored.
- **Numerics/validation**: high-order boundary-integral and conformal-mapping simulations to test whether resonant energy exchange near $k_\ast$ is bounded or secular.

## 8. Future Work

1. Compute the resonant quadratic symbol at $k_\ast=\sqrt{g/2\sigma}$ explicitly (holomorphic coordinates make this a finite algebraic computation) and determine whether it vanishes.
2. Prove a **quartic** lifespan $T_\varepsilon\gtrsim\varepsilon^{-3}$ for 2D gravity–capillary with $\gamma=0$ — the natural next milestone, requiring two normal-form steps.
3. Transfer the periodic Birkhoff-normal-form technology to $\mathbb{R}$, where small divisors are replaced by resonance-set geometry.
4. Construct, or rule out, small-data solutions with growing Sobolev norms near the Wilton frequency (a weak-turbulence-style growth mechanism).
5. Establish local well-posedness uniform in $\sigma\to0$ **with** vorticity, to interpolate between the solved $\sigma=0$ and $g=0$ endpoints.

## 9. Key References

- **[Foundational]** V. E. Zakharov. *Stability of periodic waves of finite amplitude on the surface of a deep fluid.* J. Appl. Mech. Tech. Phys. 9 (1968), 190–194.
- **[Foundational]** S. Wu. *Well-posedness in Sobolev spaces of the full water wave problem in 2-D.* Invent. Math. 130 (1997), 39–72.
- **[Foundational]** D. M. Ambrose, N. Masmoudi. *The zero surface tension limit of two-dimensional water waves.* Comm. Pure Appl. Math. 58 (2005), 1287–1315.
- **[Foundational]** H. Lindblad. *Well-posedness for the motion of an incompressible liquid with free surface boundary.* Ann. of Math. 162 (2005), 109–194.
- **[Foundational]** D. Coutand, S. Shkoller. *Well-posedness of the free-surface incompressible Euler equations with or without surface tension.* J. Amer. Math. Soc. 20 (2007), 829–930.
- **[SOTA]** A. D. Ionescu, F. Pusateri. *Global solutions for the gravity water waves system in 2d.* Invent. Math. 199 (2015), 653–804.
- **[SOTA]** T. Alazard, J.-M. Delort. *Global solutions and asymptotic behavior for two dimensional gravity water waves.* Ann. Sci. Éc. Norm. Supér. 48 (2015), 1149–1238.
- **[SOTA]** A. D. Ionescu, F. Pusateri. *Global regularity for 2D water waves with surface tension.* Memoirs of the AMS 256, no. 1227 (2018).
- **[SOTA]** Y. Deng, A. D. Ionescu, B. Pausader, F. Pusateri. *Global solutions of the gravity-capillary water-wave system in three dimensions.* Acta Math. 219 (2017), 213–402.
- **[SOTA]** M. Ifrim, D. Tataru. *The lifespan of small data solutions in two dimensional capillary water waves.* Arch. Ration. Mech. Anal. 225 (2017), 1279–1346.
- **[SOTA]** M. Ifrim, D. Tataru. *Two dimensional gravity water waves with constant vorticity: I. Cubic lifespan.* Anal. PDE 12 (2019), 903–967.
- **[SOTA]** M. Berti, J.-M. Delort. *Almost Global Solutions of Capillary-Gravity Water Waves Equations on the Circle.* Lecture Notes of the Unione Matematica Italiana 24, Springer, 2018.
- **[SOTA]** M. Berti, R. Feola, F. Pusateri. *Birkhoff normal form and long time existence for periodic gravity water waves.* Comm. Pure Appl. Math. 76 (2023), 1416–1494.
- **[Survey]** W. Craig, C. Sulem. *Numerical simulation of gravity waves.* J. Comput. Phys. 108 (1993), 73–83. (Origin of the Craig–Sulem formulation.)
- **[Survey]** D. Lannes. *The Water Waves Problem: Mathematical Analysis and Asymptotics.* Mathematical Surveys and Monographs 188, AMS, 2013.
- **[Classical]** J. R. Wilton. *On ripples.* Philos. Mag. 29 (1915), 688–700.

## 10. Worked Example / Concrete Special Case

**The Wilton resonance that blocks the normal form.** Take irrotational infinite-depth gravity–capillary waves, $\omega(k)=\sqrt{gk+\sigma k^3}$ for $k>0$. Seek a $2\!:\!1$ collinear three-wave resonance $\omega(2k)=2\omega(k)$:
$$2gk+8\sigma k^3=4\big(gk+\sigma k^3\big)\ \Longrightarrow\ 4\sigma k^3=2gk\ \Longrightarrow\ \boxed{k_\ast=\sqrt{\tfrac{g}{2\sigma}}}.$$
For clean water, $g=981\ \mathrm{cm/s^2}$ and $\sigma/\rho=74\ \mathrm{cm^3/s^2}$:
$$k_\ast=\sqrt{981/148}=2.58\ \mathrm{cm^{-1}},\qquad \lambda_\ast=2\pi/k_\ast=2.43\ \mathrm{cm}.$$
This is exactly Wilton's 1915 ripple wavelength, observed experimentally.

**Why it obstructs.** Writing the system as $\partial_t u+i\Lambda u=Q(u,u)+O(u^3)$ with $\Lambda=\omega(D)$, the normal-form change of variables $u\mapsto u+B(u,u)$ that removes $Q$ has multiplier
$$b(\xi,\eta)=\frac{q(\xi,\eta)}{i\big[\omega(\xi)-\omega(\eta)-\omega(\xi-\eta)\big]}.$$
At $(\xi,\eta)=(2k_\ast,k_\ast)$ the bracket vanishes. Moreover this point is a **space-time** resonance: $\partial_\eta[\omega(\eta)+\omega(\xi-\eta)]=\omega'(k_\ast)-\omega'(k_\ast)=0$ automatically, so the phase is stationary in $\eta$ too and no integration by parts in frequency recovers decay. Unless $q(2k_\ast,k_\ast)=0$, $b$ is unbounded and the transformation is illegal.

**Contrast with the solved endpoints.** For $\sigma=0$, $\omega(k)=\sqrt{gk}$: $\sqrt{2k}=2\sqrt{k}$ forces $\sqrt2=2$, false — no resonance. For $g=0$, $\omega(k)=\sqrt{\sigma}k^{3/2}$: $2^{3/2}=2$, false — no resonance. **Both solved cases are exactly the cases where $k_\ast$ escapes to $0$ or $\infty$.** The open problem lives precisely where $0<k_\ast<\infty$.

**Effect of vorticity.** With $\omega_+(k)=-\frac\gamma2+\sqrt{gk+\sigma k^3+\frac{\gamma^2}4}$ ($k>0$), the condition $\omega_+(2k)=2\omega_+(k)$ becomes
$$\sqrt{2gk+8\sigma k^3+\tfrac{\gamma^2}{4}}+\tfrac{\gamma}{2}=2\sqrt{gk+\sigma k^3+\tfrac{\gamma^2}{4}},$$
which for small $\gamma$ perturbs $k_\ast$ to $k_\ast(\gamma)=k_\ast+\tfrac{\gamma}{4}\,\partial\!$-correction $+O(\gamma^2)$ and, because $\omega_+(-k)\neq-\omega_+(k)$, admits **additional** counter-propagating resonant branches absent when $\gamma=0$. Removing the quadratic terms therefore fails on a strictly larger set — the precise reason the constant-vorticity case is not merely a perturbation of the irrotational one.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*