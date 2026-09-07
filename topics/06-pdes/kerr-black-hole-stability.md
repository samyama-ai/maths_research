---
id: 06-pdes/kerr-black-hole-stability
title: "Kerr Black Hole Stability"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kerr Black Hole Stability

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kerr-black-hole-stability` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Nonlinear stability of the Kerr family).** Let $(\mathcal{M}, g_{a,m})$ be a subextremal Kerr spacetime, $|a| < m$. Let $(\Sigma_0, \bar g, k)$ be an asymptotically flat vacuum initial data set that is sufficiently close, in a suitable weighted Sobolev norm, to Kerr data with parameters $(a_0, m_0)$. Then the maximal globally hyperbolic development of the data possesses a complete future null infinity $\mathcal{I}^+$, and the domain of outer communication (the exterior of the black hole region) converges, as $t \to \infty$, to a member $(\mathcal{M}, g_{a_f, m_f})$ of the Kerr family with final parameters $(a_f, m_f)$ near $(a_0, m_0)$.

A complete proof must be *global in time*, handle the *full subextremal range* $|a| < m$, allow *general* (non-symmetric, non-polarized) perturbations, and identify the final parameters dynamically — the limiting $(a_f,m_f)$ is not known in advance and the "target" of the convergence must be constructed along with the solution. Disproof would mean exhibiting arbitrarily small vacuum perturbations whose development fails to settle to Kerr (e.g. by growth of a linear or nonlinear mode, or by trapping-driven amplification).

**Status.** The conjecture is a *theorem for $|a_0|/m_0$ sufficiently small* (Klainerman–Szeftel with Giorgi and Shen, 2021–2023). The full subextremal range remains open, as does the extremal case $|a|=m$, where the Aretakis instability shows the statement must be modified.

## 2. Mathematical Foundations

The Einstein vacuum equations for a Lorentzian $4$-manifold $(\mathcal{M},g)$ are
$$\mathrm{Ric}(g) = 0,$$
a quasilinear system that, in wave (harmonic) gauge $\Box_g x^\mu = 0$, becomes
$$g^{\alpha\beta}\partial_\alpha\partial_\beta g_{\mu\nu} = N_{\mu\nu}(g, \partial g).$$
Diffeomorphism invariance means there is no canonical gauge; gauge choice is part of the problem.

**Kerr metric** in Boyer–Lindquist coordinates $(t,r,\theta,\varphi)$:
$$g_{a,m} = -\Big(1-\frac{2mr}{\rho^2}\Big)dt^2 - \frac{4amr\sin^2\theta}{\rho^2}\,dt\,d\varphi + \frac{\rho^2}{\Delta}dr^2 + \rho^2 d\theta^2 + \frac{(r^2+a^2)^2-a^2\Delta\sin^2\theta}{\rho^2}\sin^2\theta\, d\varphi^2,$$
with $\rho^2 = r^2 + a^2\cos^2\theta$, $\Delta = r^2 - 2mr + a^2$. For $|a|<m$, $\Delta$ has roots $r_\pm = m \pm \sqrt{m^2-a^2}$; $r = r_+$ is the event horizon, a Killing horizon for
$$K = \partial_t + \omega_+ \partial_\varphi, \qquad \omega_+ = \frac{a}{2mr_+}.$$
The **ergoregion** is $\{ r_+ < r < m + \sqrt{m^2 - a^2\cos^2\theta}\}$, where $g(\partial_t,\partial_t) > 0$: the stationary Killing field is spacelike, so the conserved energy associated with $\partial_t$ is **not positive definite**. This is *superradiance*.

Kerr is of Petrov type D and admits a Killing–Yano tensor and the Carter constant, so the geodesic flow and the wave equation separate. Writing $\psi = e^{-i\omega t + i\mathfrak{m}\varphi} S_{\ell \mathfrak{m}}(\theta) \frac{u(r)}{\sqrt{r^2+a^2}}$ with oblate spheroidal harmonics $S_{\ell\mathfrak{m}}$, the scalar wave equation $\Box_g\psi = 0$ becomes the radial ODE
$$\frac{d^2u}{dr_*^2} + \big(\omega^2 - V_{a,m,\omega,\mathfrak m,\ell}(r)\big)u = 0, \qquad \frac{dr_*}{dr} = \frac{r^2+a^2}{\Delta},$$
with $V \to 0$ at $r_*\to+\infty$ and $V \to \omega^2 - (\omega - \mathfrak m\omega_+)^2$ at the horizon $r_*\to-\infty$. Superradiant frequencies are those with $\omega(\omega - \mathfrak m\omega_+) < 0$.

**Linearized gravity** is governed by the **Teukolsky equations** for the extreme Weyl curvature components $\alpha = W(e_4,e_a,e_4,e_b)$, $\underline\alpha$ (spin $s = \pm 2$), which are gauge-invariant. Schematically,
$$\Box_{a,m}^{[s]}\psi^{[s]} + \text{(first-order terms)} = 0,$$
and via a **Chandrasekhar transformation** $\Psi = \Delta^{2}\big(\tfrac{r^2+a^2}{\Delta}\partial_r\big)^{2}\big(\Delta^{?}\alpha\big)$ (a second-order differential operator in $r$) one obtains a **generalized Regge–Wheeler equation**
$$\Box_{a,m}\Psi - \frac{4}{r^2}\Psi = \mathcal{N}[\Psi] + \text{(error, } O(a)\text{)},$$
which does admit a positive-definite energy structure modulo the ergoregion.

## 3. History & State of the Art (SOTA)

- **1963** — Kerr writes the metric (*Phys. Rev. Lett.* 11, 237).
- **1957** — Regge–Wheeler perturbation analysis of Schwarzschild; **1970** — Zerilli; **1973** — Teukolsky derives the separable master equations on Kerr.
- **1989** — Whiting proves **mode stability**: no exponentially growing separated solution on subextremal Kerr. Purely spectral; gives no decay rate.
- **2000s** — Vector-field/Morawetz methods for wave equations on black hole backgrounds (Blue–Soffer, Dafermos–Rodnianski, Andersson–Blue, Tataru–Tohaneanu). The **redshift vector field** (Dafermos–Rodnianski) controls the horizon.
- **2016** — Dafermos–Rodnianski–Shlapentokh-Rothman prove boundedness and decay for $\Box_g\psi=0$ on the **full subextremal range** $|a|<m$ (*Annals of Math.* 183).
- **2018** — Hintz–Vasy prove nonlinear stability of **Kerr–de Sitter** for small $|a|$ (*Acta Math.* 220), using microlocal/Fredholm methods where the cosmological constant gives exponential decay.
- **2019** — Dafermos–Holzegel–Rodnianski: linear stability of Schwarzschild (*Acta Math.* 222).
- **2021** — Häfner–Hintz–Vasy: linear stability of slowly rotating Kerr (*Invent. Math.* 223); Andersson–Bäckdahl–Blue–Ma give an independent linear stability proof.
- **2021–2023** — **Klainerman–Szeftel**, with **Giorgi** and **Shen**: nonlinear stability of Kerr for $|a_0|/m_0 \ll 1$. Announced in Klainerman–Szeftel, *Kerr stability for small angular momentum* (Pure Appl. Math. Q. 19, 2023), completed by the GCM construction papers and Giorgi–Klainerman–Szeftel's wave-estimate paper.
- **2021** — Dafermos–Holzegel–Rodnianski–Taylor: nonlinear stability of the **Schwarzschild** family (with a codimension-3 teleological gauge normalization).

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| Minkowski, $a=m=0$ | Full nonlinear stability | Christodoulou–Klainerman 1993 |
| $\Box_g\psi=0$, $|a|<m$ | Boundedness + integrated local decay + Price-law tails | Dafermos–Rodnianski–Shlapentokh-Rothman 2016 |
| Teukolsky $s=\pm2$, $|a| \ll m$ | Boundedness and decay | Dafermos–Holzegel–Rodnianski 2019; Ma 2020 |
| Teukolsky $s=\pm2$, **full** $|a|<m$ | Boundedness and decay (frequency-space analysis) | Shlapentokh-Rothman–Teixeira da Costa 2023 |
| Mode stability, $|a|<m$ | No growing modes; quantitative version | Whiting 1989; Shlapentokh-Rothman 2015 |
| Linear gravity, $|a|\ll m$ | Linear stability with final-parameter identification | Häfner–Hintz–Vasy 2021; Andersson–Bäckdahl–Blue–Ma 2019 |
| Schwarzschild, polarized axisymmetry | Nonlinear stability | Klainerman–Szeftel 2020 (Ann. Math. Studies 210) |
| Schwarzschild family, general perturbations | Nonlinear stability | Dafermos–Holzegel–Rodnianski–Taylor 2021 |
| **Kerr, $|a_0|/m_0 \ll 1$, general perturbations** | **Nonlinear stability** | Klainerman–Szeftel + Giorgi + Shen, 2021–2023 |
| Kerr–de Sitter, $\Lambda>0$, $|a| \ll m$ | Nonlinear stability | Hintz–Vasy 2018 |
| Extremal Kerr $|a|=m$ | **Instability**: transversal derivatives of $\psi$ do not decay on $\mathcal{H}^+$ | Aretakis 2011–2015 |

## 5. Principal Obstacles

- **Superradiance.** In the ergoregion $\partial_t$ is spacelike, so the $T$-energy is indefinite and the standard energy estimate is lost. One must combine $\partial_t$, $\partial_\varphi$, and the redshift field $Y$, and prove that superradiant frequencies are *not trapped* — a frequency-space statement with no known pure physical-space proof at large $|a|$.
- **Trapping.** Null geodesics orbit near the photon sphere ($r=3m$ in Schwarzschild), forcing a loss of derivatives in any integrated local-energy-decay (Morawetz) estimate. On Kerr the trapped set is $r$-dependent on the conserved quantities $(\omega,\mathfrak m,$ Carter$)$, so trapping is *not* localized to a single hypersurface in physical space. This is why the general-$a$ arguments live in frequency space and cannot be run in a nonlinear (non-separable) setting.
- **Slow decay / no spectral gap.** With $\Lambda = 0$, decay is polynomial ($|\psi| \sim \tau^{-3}$ Price tails), not exponential. Hintz–Vasy's Kerr–de Sitter method exploits a spectral gap that is simply absent here; the zero-energy resonance must be handled by hand.
- **Gauge and the moving target.** The final $(a_f, m_f)$ is only known at $t=\infty$. A gauge normalized on the initial data drifts; the solution must be renormalized *teleologically* (from the future). Klainerman–Szeftel's answer is **GCM (general covariant modulated) spheres and hypersurfaces**, where certain geometric quantities ($\kappa$, $\underline\kappa$, $\mu$) are prescribed exactly; Dafermos–Holzegel–Rodnianski–Taylor use a codimension-3 modulation with a continuity/degree argument.
- **Loss of algebraic structure at large $a$.** The Chandrasekhar-transformed Teukolsky system has errors of size $O(a)$ that are treated perturbatively. At $|a| \sim m$ these are not small, and the coupling to the gauge-dependent Ricci coefficients is no longer controlled by any known positive-definite energy in physical space.
- **No small-data structure.** The Einstein equations have quadratic null-form-like but not fully null structure in the black hole setting; the nonlinearity feeds back through the slowly-decaying $\ell=0,1$ modes that encode mass and angular momentum.

## 6. The Gap

Section 4 stops at $|a_0|/m_0 \ll 1$ nonlinearly, and at $|a|<m$ *linearly for a decoupled scalar or Teukolsky equation*. The gap has two components:

1. **From linear to nonlinear at large $a$.** Shlapentokh-Rothman–Teixeira da Costa's decay estimates for the Teukolsky equation in the full subextremal range are proved by a frequency-space (Fourier-in-$t$, spheroidal-in-$\theta$) decomposition, which requires the *exact* Kerr background. A nonlinear proof needs physical-space, quasilinear-robust estimates that survive when the metric is only approximately Kerr.
2. **From the Teukolsky quantity to the full metric.** Even linearly, control of $\alpha, \underline\alpha$ must be upgraded to control of all Ricci coefficients and metric components; for $|a|\ll m$ this is done by transport equations along a GCM foliation, and every step uses $a/m$ as a smallness parameter to absorb the non-integrable rotation terms.

The precise barrier: **an integrated local energy decay estimate for the linearized Einstein equations on Kerr, valid for all $|a|<m$, proved by physical-space vector-field multipliers/commutators that are stable under perturbation of the background metric.**

## 7. Current Research (as of June 2026)

- **Princeton (Klainerman, Szeftel — Paris, Giorgi — NYU, Shen).** Extending the GCM machinery beyond small $a$; simplification and streamlining of the ~1000-page proof; treating Kerr–Newman. *(frontier — verify)*
- **Cambridge / Princeton (Dafermos, Holzegel — Münster, Rodnianski, Taylor, Shlapentokh-Rothman — Toronto).** Pushing the full-subextremal-range Teukolsky estimates toward nonlinear applicability; the announced program on the **interior** (strong cosmic censorship) is closely coupled.
- **Microlocal school (Hintz — ETH, Vasy — Stanford, Häfner — Grenoble).** Resolution/b-calculus and "global" Fredholm methods; Hintz's work on gluing, on the black hole merger and extremal limits. *(frontier — verify)*
- **Extremal and near-extremal.** Aretakis-type instabilities, Gajic–Luk on the extremal Reissner–Nordström interior, and the question of what the correct *stability statement* is at $|a|=m$.
- **Numerics.** Quasinormal-mode spectra of Kerr at $a/m \to 1$ (Casals, Zimmerman, Hussain–Zimmerman) supporting mode stability up to extremality; ringdown fits to LIGO/Virgo/KAGRA data as empirical support.

## 8. Future Work

1. **Physical-space trapping estimates for all $|a|<m$** — the consensus prerequisite for full nonlinear stability. Candidate tools: hidden symmetry operators built from the Killing–Yano tensor (Andersson–Blue), second-order symmetry operators as commutators.
2. **Uniform-in-$a$ constants.** Existing $|a|\ll m$ arguments degenerate as $a \to m$; a proof with constants uniform up to extremality would simultaneously clarify the extremal case.
3. **Extremal Kerr.** Formulate and prove a modified stability statement compatible with the Aretakis conservation law on $\mathcal{H}^+$.
4. **Optimal decay and late-time tails.** Rigorous Price-law asymptotics for the nonlinear problem (Angelopoulos–Aretakis–Gajic have this for scalar fields).
5. **Beyond vacuum.** Einstein–Maxwell (Kerr–Newman), Einstein–Klein–Gordon (where superradiant bound states are expected to *destabilize* Kerr for suitable masses), and $\Lambda<0$.
6. **Interior.** Combine exterior stability with the $C^0$-formulation of strong cosmic censorship.

## 9. Key References

- **[Foundational]** R. P. Kerr. *Gravitational field of a spinning mass as an example of algebraically special metrics.* Physical Review Letters 11, 237–238, 1963.
- **[Foundational]** S. A. Teukolsky. *Perturbations of a rotating black hole. I.* Astrophysical Journal 185, 635–647, 1973.
- **[Foundational]** B. F. Whiting. *Mode stability of the Kerr black hole.* Journal of Mathematical Physics 30, 1301–1305, 1989.
- **[Foundational]** D. Christodoulou, S. Klainerman. *The Global Nonlinear Stability of the Minkowski Space.* Princeton University Press, 1993.
- **[SOTA]** M. Dafermos, I. Rodnianski, Y. Shlapentokh-Rothman. *Decay for solutions of the wave equation on Kerr exterior spacetimes III: the full subextremal case $|a|<M$.* Annals of Mathematics 183(3), 787–913, 2016.
- **[SOTA]** M. Dafermos, G. Holzegel, I. Rodnianski. *The linear stability of the Schwarzschild solution to gravitational perturbations.* Acta Mathematica 222, 1–214, 2019.
- **[SOTA]** P. Hintz, A. Vasy. *The global non-linear stability of the Kerr–de Sitter family of black holes.* Acta Mathematica 220, 1–206, 2018.
- **[SOTA]** D. Häfner, P. Hintz, A. Vasy. *Linear stability of slowly rotating Kerr black holes.* Inventiones Mathematicae 223, 1227–1406, 2021.
- **[SOTA]** S. Klainerman, J. Szeftel. *Global Nonlinear Stability of Schwarzschild Spacetime under Polarized Perturbations.* Annals of Mathematics Studies 210, Princeton University Press, 2020.
- **[SOTA]** S. Klainerman, J. Szeftel. *Kerr stability for small angular momentum.* Pure and Applied Mathematics Quarterly 19(3), 2023.
- **[SOTA]** E. Giorgi, S. Klainerman, J. Szeftel. *Wave equations estimates and the nonlinear stability of slowly rotating Kerr black holes.* arXiv:2205.14808, 2022.
- **[SOTA]** M. Dafermos, G. Holzegel, I. Rodnianski, M. Taylor. *The non-linear stability of the Schwarzschild family of black holes.* arXiv:2104.08222, 2021.
- **[SOTA]** Y. Shlapentokh-Rothman, R. Teixeira da Costa. *Boundedness and decay for the Teukolsky equation on Kerr in the full subextremal range $|a|<M$.* arXiv:2007.07211, 2020.
- **[Survey]** M. Dafermos, I. Rodnianski. *Lectures on black holes and linear waves.* Clay Mathematics Proceedings 17, 97–205, 2013.
- **[Survey]** S. Klainerman, J. Szeftel. *Brief introduction to the nonlinear stability of Kerr.* Pure and Applied Mathematics Quarterly, 2024.
- **[Related]** S. Aretakis. *Horizon instability of extremal black holes.* Advances in Theoretical and Mathematical Physics 19(3), 507–530, 2015.

## 10. Worked Example / Concrete Special Case

**Axisymmetric waves on Kerr: where superradiance disappears and trapping survives.**

Take $\Box_g\psi = 0$ on Kerr and restrict to axisymmetric data, $\partial_\varphi\psi = 0$ (i.e. azimuthal number $\mathfrak m = 0$). The conserved $T$-energy current is $J^\mu = T^{\mu\nu}[\psi]\,T_\nu$ with $T = \partial_t$.

*Step 1 — energy positivity.* On the horizon $r=r_+$, the normal is $K = T + \omega_+\partial_\varphi$. The flux through $\mathcal{H}^+$ is
$$\int_{\mathcal H^+} T_{\mu\nu}T^\mu K^\nu = \int_{\mathcal H^+} \big|K\psi\big|^2 - \omega_+ \int_{\mathcal H^+} (K\psi)(\partial_\varphi \psi).$$
With $\partial_\varphi\psi = 0$ this is $\int |K\psi|^2 \ge 0$: the energy flowing into the black hole is nonnegative, so
$$E[\psi](\Sigma_\tau) \le E[\psi](\Sigma_0).$$
No superradiance. In frequency terms $\omega(\omega - \mathfrak m\omega_+) = \omega^2 > 0$ for all $\omega \ne 0$. **This is why $\mathfrak m = 0$ (and, more generally, $|a|\ll m$ so that $\omega_+ = a/(2mr_+)$ is tiny) is the tractable regime.**

*Step 2 — the surviving difficulty.* Take $a = 0$ for the explicit potential. With $\psi = e^{-i\omega t}Y_{\ell 0}(\theta)\,u(r)/r$, $r_* = r + 2m\log(\tfrac{r}{2m}-1)$,
$$u'' + \big(\omega^2 - V_\ell(r)\big)u = 0, \qquad V_\ell(r) = \Big(1-\frac{2m}{r}\Big)\Big(\frac{\ell(\ell+1)}{r^2} + \frac{2m}{r^3}\Big).$$
Then
$$V_\ell'(r) = \frac{2}{r^4}\Big[\ell(\ell+1)\big(3m - r\big) + m\Big(4 - \frac{9m}{r}\Big)\cdot\ldots\Big],$$
and to leading order in large $\ell$, $V_\ell'(r) = 0$ at $r = 3m$ — the **photon sphere**. Setting $\ell=1$, $m=1$: $V_1(3) = (1/3)(2/9 + 2/27) = 8/81 \approx 0.0988$, while $V_1(2.5)\approx 0.0960$ and $V_1(4) \approx 0.0781$. So $V$ has an interior maximum at $r\approx 3m$.

*Step 3 — why this blocks a clean Morawetz estimate.* A multiplier $X = f(r_*)\partial_{r_*}$ yields the identity
$$\int \Big( f'|u'|^2 - \tfrac12 f''' |u|^2 - f V' |u|^2\Big)dr_* = \text{boundary terms}.$$
Positivity of the $|u|^2$ coefficient needs $fV' < 0$, forcing $f$ to change sign at the critical point of $V$, i.e. $f(3m)=0$ — so the $|u'|^2$ term degenerates there. Any integrated local energy decay estimate must therefore lose derivatives at $r=3m$:
$$\int_0^\infty\!\!\int_{r\ge r_+} \chi(r)\big(|\partial\psi|^2 + |\psi|^2\big) \lesssim E[\psi](\Sigma_0), \quad \chi(3m) = 0,$$
recovered only by commuting with $\partial_t$ (or with the Carter operator on Kerr).

*Step 4 — the Kerr obstruction.* For $a \ne 0$ the analogue of $r = 3m$ is a *frequency-dependent* radius $r_{\mathrm{trap}}(\omega, \mathfrak m, \lambda_{\ell\mathfrak m})$, ranging over an interval of $r$ as the parameters vary, and superradiant modes ($0 < \omega < \mathfrak m \omega_+$) contribute negative horizon flux of size $\omega(\omega-\mathfrak m\omega_+)|u|^2$. The whole difficulty of the full subextremal range is proving that these two bad sets — the trapped frequencies and the superradiant frequencies — are **disjoint**, which is known in frequency space (Dafermos–Rodnianski–Shlapentokh-Rothman) but not by any perturbation-stable physical-space argument.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*