---
id: 06-pdes/kraichnan-spectrum-2d
title: "Kraichnan Spectrum 2D"
topic: 06-pdes
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Kraichnan Spectrum for Two-Dimensional Turbulence

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kraichnan-spectrum-2d` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Kraichnan (1967) predicted that forced, statistically stationary two-dimensional Navier–Stokes turbulence splits into two inertial ranges with distinct power-law energy spectra: an **inverse energy cascade** with $E(k)\sim \epsilon^{2/3}k^{-5/3}$ at scales larger than the forcing scale, and a **direct enstrophy cascade** with $E(k)\sim \eta^{2/3}k^{-3}$ at smaller scales.

**Conjecture.** Let $u$ solve the 2D Navier–Stokes equations on $\mathbb{T}^2$, driven by a body force concentrated at wavenumber $k_f$ and damped at large scales by linear friction $\alpha$. In the joint limit $\nu\to 0$, $\alpha\to 0$ with energy injection rate $\epsilon$ and enstrophy injection rate $\eta = k_f^2\epsilon$ held fixed, the stationary energy spectrum satisfies
$$E(k) \;\simeq\; C_\epsilon\,\epsilon^{2/3}k^{-5/3}\quad (k\ll k_f),\qquad E(k)\;\simeq\;C_\eta\,\eta^{2/3}k^{-3}\quad (k\gg k_f),$$
with $C_\epsilon, C_\eta$ universal, and the corresponding constant-flux laws $\Pi_E(k)=-\epsilon$ for $k<k_f$, $\Pi_Z(k)=+\eta$ for $k>k_f$.

A complete resolution requires: (i) existence of the stationary measures and the limits above, (ii) proof of the two flux laws from the equations rather than from closure assumptions, (iii) determination of whether the $k^{-3}$ law is exact or carries Kraichnan's (1971) logarithmic correction, and (iv) a proof or disproof of universality of $C_\epsilon,C_\eta$. A disproof would exhibit a forcing class satisfying the hypotheses for which the exponents differ (e.g. the steeper, coherent-vortex-dominated spectra seen in some simulations).

## 2. Mathematical Foundations

Work in vorticity form on $\mathbb{T}^2$, $\omega=\partial_1 u_2-\partial_2 u_1$:
$$\partial_t\omega + u\cdot\nabla\omega \;=\; \nu\Delta\omega \;-\;\alpha\omega\;+\;f,\qquad u=\nabla^\perp\Delta^{-1}\omega,\qquad \nabla\cdot u=0 .$$
The nonlinearity $u\cdot\nabla\omega$ is a null form for both quadratic invariants: for $\nu=\alpha=f=0$,
$$E=\tfrac12\int|u|^2\,dx,\qquad Z=\tfrac12\int\omega^2\,dx$$
are conserved, together with all Casimirs $\int F(\omega)\,dx$. In Fourier variables $E=\int_0^\infty E(k)\,dk$ and $Z=\int_0^\infty k^2E(k)\,dk$.

**Fjørtoft constraint.** Conservation of $E$ and $Z$ under a triadic transfer from $k_f$ to $k_1<k_f<k_2$ forces the energy fractions
$$\frac{\delta E_1}{\delta E_2}=\frac{k_2^2-k_f^2}{k_f^2-k_1^2},$$
so energy moves preferentially to low $k$ and enstrophy to high $k$ (Fjørtoft 1953). This is the rigorous kinematic seed of the dual cascade; it does **not** by itself give a direction or a rate.

**Dimensional closure.** Assuming a $k$-local, constant-flux range depending only on $\epsilon$ (units $L^2T^{-3}$) or $\eta$ (units $T^{-3}$) gives $E(k)=C_\epsilon\epsilon^{2/3}k^{-5/3}$ and $E(k)=C_\eta\eta^{2/3}k^{-3}$. Because $k^{-3}$ makes the enstrophy integral log-divergent, the enstrophy range is only marginally local; Kraichnan (1971) resummed the nonlocal shear straining to obtain
$$E(k)=C'\,\eta^{2/3}k^{-3}\bigl[\ln(k/k_f)\bigr]^{-1/3}.$$

**Exact flux laws.** The 2D analogues of Kolmogorov's $4/5$ law, derived from the Kármán–Howarth–Monin relation for the stationary state, are for the longitudinal structure function $S_3^L(r)=\langle(\delta_r u_L)^3\rangle$:
$$S_3^L(r)=\tfrac{3}{2}\,\epsilon\, r\ \ (r\gg \ell_f),\qquad S_3^L(r)=\tfrac{1}{8}\,\eta\, r^3\ \ (r\ll \ell_f),$$
together with the mixed vorticity flux law $\langle \delta_r u_L\,(\delta_r\omega)^2\rangle=-2\eta r$ (Eyink 1996; Bernard 1999). Note the **positive** sign of $S_3^L$ in the inverse range, opposite to 3D.

**Anomalous dissipation.** The direct cascade requires an enstrophy dissipation anomaly, $\lim_{\nu\to0}\nu\|\nabla\omega\|_{L^2}^2=\eta>0$, i.e. an Onsager-type singularity in $\omega$. The known 2D Onsager threshold: for $u\in L^3_tB^{\sigma}_{3,\infty}$ with $\sigma>1/3$ energy is conserved (Constantin–E–Titi 1994), and vorticity-based criteria (Eyink 2001) show enstrophy conservation holds unless $\omega$ fails a corresponding $B^{0}_{3,\infty}$-type bound.

## 3. History & State of the Art (SOTA)

- **1953** — Fjørtoft: the dual-invariant transfer constraint.
- **1967** — R. H. Kraichnan, *Inertial ranges in two-dimensional turbulence* (Phys. Fluids 10, 1417): the two-range prediction.
- **1968–69** — C. Leith (Phys. Fluids 11, 671) and G. K. Batchelor (Phys. Fluids Suppl. II, 233) derive the $k^{-3}$ enstrophy range independently; hence "Kraichnan–Batchelor–Leith" (KBL) theory.
- **1971** — Kraichnan, JFM 47, 525: test-field-model resummation yielding the $[\ln]^{-1/3}$ correction; recognition that $k^{-3}$ is marginal.
- **1980s–90s** — Nastrom & Gage (1984) atmospheric spectra; Lindborg (1999, JFM 388) tests the 2D structure-function laws on aircraft data.
- **1996–2000** — Eyink (Physica D 91, 97) proves rigorous consequences of vorticity conservation; Bernard (PRE 60, 6184) and Nam–Ott–Antonsen–Guzdar (PRL 84, 5134) show friction steepens the direct-cascade exponent above $3$.
- **2000s** — Direct numerical simulation confirms both ranges: Boffetta (JFM 589, 2007) measures $C_\epsilon\approx 5.8$–$6.0$ in the inverse range; Boffetta & Musacchio (PRE 82, 016307, 2010) resolve both cascades simultaneously at $32768^2$.
- **2020s** — Bedrossian, Coti Zelati, Punshon-Smith & Weber (ARMA, 2022) give the first *sufficient conditions*, verifiable in principle, under which the dual flux laws hold for stochastically forced 2D Navier–Stokes.

## 4. Partial Results / Verified Cases

- **Rigorous, unconditional.** Global well-posedness and unique stationary measure for 2D stochastic Navier–Stokes with degenerate noise (Hairer–Mattingly, Ann. Math. 164, 2006). Existence of the stationary state is therefore not an issue — only its spectrum is.
- **Rigorous, conditional.** Bedrossian–Coti Zelati–Punshon-Smith–Weber (2022): if the stationary measures satisfy a weak anomalous-dissipation hypothesis plus a mild uniform regularity bound, then $\Pi_E\to-\epsilon$ below $k_f$ and $\Pi_Z\to+\eta$ above $k_f$ in a suitable averaged sense — a *bona fide* derivation of the two constant-flux ranges, though not of the spectral exponents.
- **No-go for the direct cascade with smooth forcing.** Constantin & Ramos (CMP 275, 2007) prove that for damped–driven 2D Navier–Stokes on $\mathbb{R}^2$ with forcing in $H^1$, enstrophy dissipation vanishes as $\nu\to0$: the enstrophy anomaly needed for $k^{-3}$ cannot occur under those hypotheses. The conjecture must therefore be posed with $k_f$ scaling with $\nu$, or with rough forcing.
- **Statistical-estimate bounds.** Foias, Jolly, Manley & Rosa (J. Stat. Phys. 108, 591, 2002) derive rigorous inequalities on ensemble-averaged 2D spectra consistent with KBL, locating the dissipation wavenumber at $k_\eta\sim(\eta/\nu^3)^{1/6}$ (Kraichnan scale) with matching upper and lower bounds under a "cascade" assumption.
- **Numerics.** The $-5/3$ inverse range is measured to within $\pm 0.03$ over $\gtrsim 2$ decades with $C_\epsilon\approx 6$ (Boffetta 2007; Boffetta–Musacchio 2010); the inverse-cascade statistics are close to Gaussian and non-intermittent, confirmed by structure functions up to order 8. The $\tfrac32\epsilon r$ law is verified directly.
- **Passive-scalar analogue solved.** Bedrossian, Blumenthal & Punshon-Smith (CPAM 75, 2022) *prove* the Batchelor $k^{-1}$ spectrum for a passive scalar in a stochastic velocity field at fixed Reynolds number — the first rigorous turbulence power law of this family.
- **Experiments.** Soap films and electromagnetically forced stratified layers reproduce both ranges (Rutgers 1998; Kellay & Goldburg, Rep. Prog. Phys. 65, 2002).

## 5. Principal Obstacles

- **The direct cascade is only marginally local.** With $E(k)\propto k^{-3}$, the strain at wavenumber $k$ has equal contributions from every octave below it. All local-cascade arguments — Kolmogorov-style similarity, shell models, Fourier localization estimates — lose their small parameter. Nonlocal shear straining is exactly what produces the log correction, and no rigorous method controls it.
- **Enstrophy dissipation anomaly is nearly forbidden.** $\omega\in L^\infty$ is propagated by 2D Euler (Yudovich), and Constantin–Ramos rules out the anomaly under natural forcing hypotheses. The conjecture lives in a narrow window where a $\nu$-dependent forcing scale sustains an anomaly that the smooth theory excludes; no construction realizes this window rigorously.
- **Coherent vortices break self-similarity.** Long-lived vortices formed at the forcing scale carry $\omega\sim$ const cores whose spectral signature is $k^{-4}$ locally; sweeping by them is nonlocal in $k$ but local in $x$. Dritschel, Scott, Macaskill, Gottwald & Tran (PRL 101, 094501, 2008) argue for a vortex-population scaling in which the enstrophy-range exponent is not universal.
- **Friction contaminates the exponent.** With linear drag $\alpha$, the direct-cascade slope becomes $-(3+\xi)$ with $\xi$ increasing in $\alpha/\eta^{1/3}$ (Bernard 1999; Nam et al. 2000). Any laboratory or numerical realization has $\alpha>0$, so the "clean" $k^{-3}$ is an extrapolated, never directly measured, limit.
- **Condensation.** The inverse cascade in a finite box terminates in a spectral condensate at $k\sim L^{-1}$ (Chertkov, Connaughton, Kolokolov & Lebedev, PRL 99, 084501, 2007), which feeds back on the inertial range and forbids taking $\alpha\to0$ first.

## 6. The Gap

Between Section 4 and Section 1 lie two distinct steps.

1. **From flux to spectrum.** The conditional theorems deliver *constant flux* ($\Pi_E=-\epsilon$, $\Pi_Z=\eta$). Converting a flux law into a spectral exponent requires an additional locality/scale-invariance input that is proved nowhere; in 3D the same gap separates the $4/5$ law from $k^{-5/3}$. In 2D the gap is worse, because in the enstrophy range locality is *known to fail marginally*.
2. **Producing the anomaly.** No forcing family is known for which one can prove $\liminf_{\nu\to0}\nu\|\nabla\omega\|^2>0$ while satisfying the hypotheses of the flux theorems. Constantin–Ramos shows the naive choices fail. The precise barrier: exhibit stationary measures $\mu_\nu$ for the forced 2D equations with $\|\omega\|_{B^{0}_{3,\infty}}$ uniformly *just* failing the Eyink-type conservation criterion.

Even granting both, universality of $C_\epsilon$ and the presence or absence of the $[\ln(k/k_f)]^{-1/3}$ factor remain open at the level of numerics: no simulation has the decade count to distinguish $k^{-3}$ from $k^{-3}(\ln k)^{-1/3}$.

## 7. Current Research (as of June 2026)

- **Stochastic-PDE school** (Bedrossian, Punshon-Smith, Coti Zelati, Weber; Northwestern / Maryland / EPFL / GSSI). Programme: use Lyapunov-exponent and Malliavin-calculus machinery — the same that proved the Batchelor spectrum — to attack the 2D velocity field itself. Effort is concentrated on the *inverse* cascade, where non-intermittency makes Gaussian-like closures plausible. *(frontier — verify)*
- **Onsager-type flexibility.** Convex integration has produced non-conservative 2D Euler solutions with vorticity in $L^p$ (Buckmaster–De Lellis–Székelyhidi lineage; Giri–Radu 2023 for the 3D Onsager endpoint). Whether such solutions can be exhibited as $\nu\to0$ limits of *forced stationary* 2D flows — the object the conjecture concerns — is the live question. *(frontier — verify)*
- **Ultra-high-resolution DNS** on GPU clusters, targeting three clean decades in the enstrophy range to test the log correction; groups at Torino (Boffetta, Musacchio), St Andrews (Dritschel, Scott), and KTH (Lindborg).
- **Oceanic/atmospheric validation**: submesoscale-permitting models and altimetry continue to test whether observed $k^{-3}$-to-$k^{-5/3}$ transitions are KBL or a distinct wave–vortex decomposition (Bühler, Callies, Ferrari).
- **Wave-turbulence rigor**: Deng–Hani's derivation of the wave kinetic equation raises the prospect of a first-principles kinetic derivation for weakly nonlinear 2D systems, though 2D Navier–Stokes is strongly nonlinear and not directly covered.

## 8. Future Work

- Formulate a $\nu$-dependent forcing scaling $k_f(\nu)$ for which the enstrophy anomaly can be proved, evading Constantin–Ramos.
- Prove locality of the enstrophy flux up to the expected logarithm, e.g. bounding the nonlocal contribution to $\Pi_Z(k)$ by $O(\log^{-1})$ relative to the local one.
- Establish a rigorous lower bound $E(k)\gtrsim \eta^{2/3}k^{-3-\delta}$ and upper bound $E(k)\lesssim \eta^{2/3}k^{-3+\delta}$ in an averaged (Foias-style) sense with explicit $\delta\to0$.
- Settle whether $C_\epsilon$ depends on the forcing correlation structure by systematic DNS with $\delta$-correlated versus deterministic forcing.
- Extend the Batchelor-spectrum proof technique from the passive scalar to the active vorticity field at fixed Reynolds number.

## 9. Key References

- **[Foundational]** R. H. Kraichnan. *Inertial ranges in two-dimensional turbulence.* Physics of Fluids **10**, 1417–1423, 1967.
- **[Foundational]** G. K. Batchelor. *Computation of the energy spectrum in homogeneous two-dimensional turbulence.* Physics of Fluids **12**, Suppl. II, 233–239, 1969.
- **[Foundational]** C. E. Leith. *Diffusion approximation for two-dimensional turbulence.* Physics of Fluids **11**, 671–673, 1968.
- **[Foundational]** R. H. Kraichnan. *Inertial-range transfer in two- and three-dimensional turbulence.* Journal of Fluid Mechanics **47**, 525–535, 1971.
- **[Theory]** G. L. Eyink. *Exact results on stationary turbulence in 2D: consequences of vorticity conservation.* Physica D **91**, 97–142, 1996.
- **[Theory]** D. Bernard. *Three-point velocity correlation functions in two-dimensional forced turbulence.* Physical Review E **60**, 6184–6187, 1999.
- **[Rigorous]** P. Constantin, W. E, E. S. Titi. *Onsager's conjecture on the energy conservation for solutions of Euler's equation.* Communications in Mathematical Physics **165**, 207–209, 1994.
- **[Rigorous]** P. Constantin, F. Ramos. *Inviscid limit for damped and driven incompressible Navier–Stokes equations in $\mathbb{R}^2$.* Communications in Mathematical Physics **275**, 529–551, 2007.
- **[Rigorous]** C. Foias, M. S. Jolly, O. P. Manley, R. Rosa. *Statistical estimates for the Navier–Stokes equations and the Kraichnan theory of 2-D fully developed turbulence.* Journal of Statistical Physics **108**, 591–645, 2002.
- **[SOTA / Recent]** J. Bedrossian, M. Coti Zelati, S. Punshon-Smith, F. Weber. *Sufficient conditions for dual cascade flux laws in the stochastic 2d Navier–Stokes equations.* Archive for Rational Mechanics and Analysis **244**, 1–58, 2022.
- **[SOTA / Recent]** J. Bedrossian, A. Blumenthal, S. Punshon-Smith. *The Batchelor spectrum of passive scalar turbulence in stochastic fluid mechanics at fixed Reynolds number.* Communications on Pure and Applied Mathematics **75**, 1237–1291, 2022.
- **[Numerics]** G. Boffetta. *Energy and enstrophy fluxes in the double cascade of two-dimensional turbulence.* Journal of Fluid Mechanics **589**, 253–260, 2007.
- **[Numerics]** G. Boffetta, S. Musacchio. *Evidence for the double cascade scenario in two-dimensional turbulence.* Physical Review E **82**, 016307, 2010.
- **[Numerics]** D. G. Dritschel, R. K. Scott, C. Macaskill, G. A. Gottwald, C. V. Tran. *Unifying scaling theory for vortex dynamics in two-dimensional turbulence.* Physical Review Letters **101**, 094501, 2008.
- **[Survey]** G. Boffetta, R. E. Ecke. *Two-dimensional turbulence.* Annual Review of Fluid Mechanics **44**, 427–451, 2012.
- **[Survey]** P. Tabeling. *Two-dimensional turbulence: a physicist approach.* Physics Reports **362**, 1–62, 2002.
- **[Book]** C. Foias, O. Manley, R. Rosa, R. Temam. *Navier–Stokes Equations and Turbulence.* Cambridge University Press, 2001.

## 10. Worked Example / Concrete Special Case

**Fjørtoft's bound made numerical, and the spectrum it implies.**

Take forcing at $k_f = 100$ (box $2\pi$, so $\ell_f\approx 0.063$), injecting $\epsilon = 1$ and hence $\eta = k_f^2\epsilon = 10^4$. Suppose energy leaves the forcing shell only via two triads, to $k_1=10$ and $k_2=1000$. Conservation of $E$ and $Z$ gives
$$\delta E_1+\delta E_2 = \epsilon,\qquad k_1^2\delta E_1 + k_2^2\delta E_2 = k_f^2\epsilon .$$
Solving:
$$\delta E_1 = \epsilon\,\frac{k_2^2-k_f^2}{k_2^2-k_1^2}=\frac{10^6-10^4}{10^6-10^2}\approx 0.990,\qquad \delta E_2\approx 0.010 .$$
So $99\%$ of the energy goes *down* in $k$, while the enstrophy fractions are $k_1^2\delta E_1/\eta \approx 0.0099$ and $k_2^2\delta E_2/\eta\approx 0.990$ — $99\%$ of enstrophy goes *up*. This is the dual cascade in one line of arithmetic.

**Consequences for the spectrum.** In the enstrophy range set $E(k)=C_\eta\eta^{2/3}k^{-3}$ with $C_\eta\approx 1.4$. The eddy turnover time is scale-independent:
$$\tau(k)=\bigl[k^3E(k)\bigr]^{-1/2}=C_\eta^{-1/2}\eta^{-1/3}\approx 0.85\times 10^{-4/3}\approx 0.039 .$$
Every scale in the direct cascade turns over at the same rate $\eta^{1/3}=21.5\,\mathrm{s^{-1}}$ — the hallmark of a constant-strain, non-local range, and the reason the enstrophy flux is $\eta$ at all $k>k_f$.

**Where the marginality bites.** The enstrophy content between $k_f$ and $K$ is
$$\int_{k_f}^{K}k^2E(k)\,dk = C_\eta\eta^{2/3}\ln(K/k_f),$$
which diverges logarithmically. With Kraichnan's correction $E(k)=C'\eta^{2/3}k^{-3}[\ln(k/k_f)]^{-1/3}$ the integral becomes $\tfrac32 C'\eta^{2/3}[\ln(K/k_f)]^{2/3}$ — still divergent, but the local strain is now finite per octave, restoring self-consistency.

**Detectability.** Over three decades, $K/k_f=10^3$, the correction factor $[\ln 10^3]^{-1/3}=6.91^{-1/3}=0.524$ versus $[\ln 10]^{-1/3}=0.744$ at one decade: the log term steepens the *apparent* slope by only
$$\Delta = \frac{\ln(0.744/0.524)}{\ln 10^{2}} = \frac{0.350}{4.605}\approx 0.076 .$$
An effective exponent of $-3.08$ against $-3.00$ — within the scatter of the best $32768^2$ simulations. This is precisely why the problem is *empirically supported* but not settled: the discriminating signal is a $2.5\%$ change in slope over three decades that no experiment or DNS has yet resolved.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*