---
id: 06-pdes/kolmogorov-turbulence-law
title: "Kolmogorov Turbulence Law"
topic: 06-pdes
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kolmogorov Turbulence Law

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kolmogorov-turbulence-law` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Kolmogorov's 1941 theory (K41) predicts that in the inertial range of a high-Reynolds-number incompressible fluid the statistics of velocity increments are universal and determined solely by the mean energy dissipation rate $\varepsilon$. The problem is to **derive K41 — the $4/5$ law, the $2/3$ law, and the $k^{-5/3}$ energy spectrum — as a theorem about the incompressible Navier–Stokes equations**, rather than as a physical hypothesis.

Concretely, let $u^\nu$ solve
$$\partial_t u^\nu + (u^\nu\cdot\nabla)u^\nu = -\nabla p^\nu + \nu\Delta u^\nu + f, \qquad \nabla\cdot u^\nu = 0, \qquad x \in \mathbb{T}^3,$$
and let $\langle\cdot\rangle$ denote a statistically stationary, homogeneous, isotropic ensemble average. Write $\delta u_\parallel(\ell) = \big(u(x+\ell e)-u(x)\big)\cdot e$ for the longitudinal increment. The claims are:

1. **Dissipation anomaly (zeroth law).** $\varepsilon := \lim_{\nu\to 0}\nu\langle |\nabla u^\nu|^2\rangle$ exists and is **strictly positive** and $\nu$-independent.
2. **Four-fifths law.** In the inertial range $\eta \ll \ell \ll L$, $\ \langle \delta u_\parallel(\ell)^3\rangle = -\tfrac{4}{5}\varepsilon\ell$.
3. **Two-thirds law / $-5/3$ spectrum.** $\langle \delta u_\parallel(\ell)^2\rangle = C_2\,\varepsilon^{2/3}\ell^{2/3}$ and $E(k) = C_K \varepsilon^{2/3}k^{-5/3}$, with $C_K$ a universal constant.
4. **Self-similarity.** $\langle|\delta u(\ell)|^p\rangle \sim \varepsilon^{p/3}\ell^{\zeta_p}$ with $\zeta_p = p/3$ for all $p>0$.

A complete resolution would either prove (1)–(3) from the Navier–Stokes equations under stated hypotheses, or exhibit the correct replacement. Claim (4) is **empirically false** for $p \gtrsim 4$ (intermittency); the open problem there is to derive the true $\zeta_p$.

## 2. Mathematical Foundations

**Kármán–Howarth–Monin relation.** For homogeneous solutions, with the correlation $ \Gamma(\ell)=\langle u(x)\cdot u(x+\ell)\rangle$,
$$\partial_t \Gamma(\ell) = \tfrac{1}{4}\nabla_\ell\cdot\langle |\delta u(\ell)|^2\,\delta u(\ell)\rangle + 2\nu\Delta_\ell\Gamma(\ell) + \langle f(x)\cdot u(x+\ell)\rangle .$$
Under stationarity, isotropy and incompressibility this reduces (Kolmogorov 1941; Frisch 1995, §6.2) to
$$\langle \delta u_\parallel(\ell)^3\rangle - 6\nu\,\partial_\ell \langle\delta u_\parallel(\ell)^2\rangle = -\tfrac{4}{5}\,\varepsilon\,\ell + \text{(forcing term, } O(\ell^3)\text{ for } \ell\ll L).$$
The $4/5$ law is the $\nu\to 0$, inertial-range limit of this exact identity — the only claim of K41 with a near-derivation.

**Scales.** The Kolmogorov dissipation length and velocity are
$$\eta = \Big(\frac{\nu^3}{\varepsilon}\Big)^{1/4}, \qquad u_\eta = (\nu\varepsilon)^{1/4}, \qquad \frac{L}{\eta} \sim \mathrm{Re}^{3/4},\quad \mathrm{Re}=\frac{UL}{\nu}.$$

**Onsager's criterion.** Define the local energy flux via the Duchon–Robert distribution
$$D(u) = \lim_{\epsilon\to0}\tfrac{1}{4}\int \nabla\varphi_\epsilon(\xi)\cdot \delta u(\xi)\,|\delta u(\xi)|^2\,d\xi .$$
For $u\in L^3_t B^{s}_{3,\infty}$ with $s>1/3$, $D(u)=0$ and energy is conserved (Constantin–E–Titi 1994; Duchon–Robert 2000). The K41 scaling $\delta u \sim \ell^{1/3}$ sits exactly at the critical exponent $s=1/3$ — anomalous dissipation requires $u$ to be *no smoother* than Hölder-$1/3$.

**Structure exponents.** $S_p(\ell)=\langle|\delta u(\ell)|^p\rangle \sim \ell^{\zeta_p}$. K41 asserts $\zeta_p=p/3$; the exact relation $\zeta_3=1$ (signed) holds. Convexity of $p\mapsto\zeta_p$ follows from Hölder; monotonicity from incompressibility. Refined similarity (K62) replaces $\varepsilon$ by the local average $\varepsilon_\ell$, giving $\zeta_p = p/3 - \tfrac{\mu}{18}p(p-3)$ with intermittency exponent $\mu\approx 0.25$. She–Leveque (1994) proposes
$$\zeta_p = \frac{p}{9} + 2\Big(1 - \big(\tfrac{2}{3}\big)^{p/3}\Big),$$
which matches data to $p\approx 10$.

## 3. History & State of the Art (SOTA)

- **1941.** A. N. Kolmogorov, three *Doklady* notes: the local-isotropy hypotheses, the $2/3$ law, and the exact $4/5$ law. A. M. Obukhov gives the spectral form independently the same year.
- **1945–49.** Onsager derives the $k^{-5/3}$ spectrum and, in his 1949 *Nuovo Cimento* supplement, states that Euler solutions rougher than $C^{1/3}$ can dissipate energy — the Onsager conjecture.
- **1962.** Landau's objection (fluctuations of $\varepsilon$ over the large scales cannot be universal) prompts Kolmogorov's refined similarity hypothesis (K62), lognormal $\varepsilon_\ell$.
- **1984.** Anselmet–Gagne–Hopfinger–Antonia measure $\zeta_p$ up to $p=18$; clear departure from $p/3$.
- **1994.** Constantin–E–Titi prove the "easy half" of Onsager: $B^{1/3+}_{3,\infty}$ regularity implies conservation. Eyink gives a parallel proof.
- **1994–2000.** She–Leveque multifractal model; Duchon–Robert local energy balance for weak solutions.
- **2016–2019.** Isett proves the Onsager conjecture: dissipative $C^{1/3-}_{t,x}$ Euler solutions exist (*Annals*, 2018); Buckmaster–De Lellis–Székelyhidi–Vicol construct them with prescribed energy profile (*CPAM*, 2019).
- **2019–2022.** Bedrossian, Coti Zelati, Punshon-Smith and Weber establish the $4/5$ law and dual-cascade flux laws for stochastically forced Navier–Stokes **conditional on** a quantified anomalous-dissipation hypothesis; Bedrossian–Blumenthal–Punshon-Smith prove Batchelor's $k^{-1}$ passive-scalar law unconditionally at fixed Reynolds number (*Annals of Math.*, 2022).

Measured constants: $C_K = 1.62\pm 0.17$ (Sreenivasan 1995) and normalized dissipation $\varepsilon L/U^3 \approx 0.5$ at high $R_\lambda$ (Sreenivasan 1998), both stable across experiments and DNS.

## 4. Partial Results / Verified Cases

- **Exact $4/5$ law, given hypotheses.** Under homogeneity, isotropy, stationarity and $\varepsilon>0$, the law is a theorem (Frisch 1995, Thm. 6.2). Bedrossian–Coti Zelati–Punshon-Smith–Weber (*Comm. Math. Phys.* 373, 2020) prove it for stationary martingale solutions of stochastically forced 3D Navier–Stokes assuming only a weak anomalous-dissipation condition, without assuming isotropy.
- **Onsager exponent $1/3$ is sharp.** Conservation for $B^{1/3+\delta}_{3,\infty}$; nonconservation for every exponent $<1/3$ (Isett 2018).
- **2D dual cascade.** For stochastic 2D Navier–Stokes, direct-enstrophy and inverse-energy flux laws hold under explicit conditions (BCZPSW, *Arch. Ration. Mech. Anal.* 237, 2020). Enstrophy conservation forbids a 3D-type energy anomaly in 2D — a proved structural dichotomy.
- **Upper bounds on dissipation.** The background/Doering–Constantin method yields $\varepsilon \le c\,U^3/L$ uniformly in $\nu$ for body-forced and shear flows (Doering–Foias, *J. Fluid Mech.* 467, 2002) — the K41 upper bound is rigorous; only the matching lower bound is missing.
- **Passive scalars.** Batchelor's $k^{-1}$ spectrum proved for advection by stochastic Navier–Stokes; anomalous scalar dissipation proved in Kraichnan's white-in-time model and in explicit deterministic shear/alternating-cell flows (Drivas, Elgindi, Iyer, Jeong).
- **Numerics.** DNS to $R_\lambda \approx 2300$ (Ishihara–Gotoh–Kaneda; Buaria et al.) confirm the $-5/3$ spectrum over $\sim$1.5 decades and $\zeta_3 = 1.00\pm 0.01$, with $\zeta_p<p/3$ for $p\ge 4$.

## 5. Principal Obstacles

- **No lower bound on dissipation.** Proving $\liminf_{\nu\to0}\nu\langle|\nabla u^\nu|^2\rangle > 0$ for 3D Navier–Stokes is open and is not weaker than understanding the regularity problem: it demands control of a singular limit where the only uniform bound is $\|u\|_{L^\infty_tL^2}$ plus $\sqrt{\nu}\|\nabla u\|_{L^2}$, which is exactly the scale-invariant borderline.
- **Energy estimates are the wrong topology.** Leray theory gives $u\in L^\infty_tL^2\cap L^2_t\dot H^1$; the $4/5$ law is a *third-order* statement requiring $L^3$-type increment control that no a priori estimate supplies. Fourier analysis is blocked because the nonlinearity is critical in $\dot H^{1/2}$ and the cascade is a genuinely nonperturbative transfer across all scales simultaneously.
- **Convex integration produces non-unique solutions.** The Euler solutions realizing Onsager's exponent are constructed, not selected; they form a dense wild set and none is known to be a vanishing-viscosity limit. So they certify sharpness of the exponent but say nothing about which flow nature picks.
- **Ensembles are undefined.** K41 averages over an invariant measure for 3D Navier–Stokes whose existence with the required homogeneity/isotropy and uniform-in-$\nu$ moment bounds is itself unproven; stochastic forcing supplies one, at the cost of altering the model.
- **Intermittency breaks the ansatz.** Since $\zeta_p$ is strictly concave, no single-exponent self-similar ansatz can be correct, so the very scaling structure the analysis would target is known to be wrong for $p>3$.

## 6. The Gap

Everything reduces to one implication. Section 4 gives: *if* $\varepsilon>0$ in the inviscid limit, *then* the $4/5$ law follows, and *if* the flow were smoother than $B^{1/3}_{3,\infty}$, *then* $\varepsilon=0$. Section 1 asks for $\varepsilon>0$ itself. The missing step is a **quantitative inviscid lower bound** — a proof that for some physically relevant forcing and some sequence $\nu_j\to0$, vanishing-viscosity limits of Navier–Stokes are Onsager-critical rather than smooth. Second gap: even granting the $4/5$ law, $\zeta_3=1$ does not imply $\zeta_2=2/3$; going from the third-order identity to the second-order law needs an independent argument that rules out the concavity corrections. Third: universality of $C_K$ and $C_2$ has no proof strategy at all.

## 7. Current Research (as of June 2026)

- **Stochastic-PDE school** (Bedrossian, Punshon-Smith, Coti Zelati, Weber; Maryland/Michigan/Johns Hopkins): conditional flux laws, Lagrangian chaos, Lyapunov exponents of stochastic Navier–Stokes; goal is an unconditional anomalous-dissipation theorem for a forced model. *(frontier — verify)* Work on non-Gaussian forcing and Reynolds-uniform mixing rates continues.
- **Convex integration** (De Lellis, Székelyhidi, Vicol, Buckmaster, Giri–Kwon–Novack): "intermittent" schemes producing $L^3$-critical and $L^p$-based non-uniqueness; Novack–Vicol constructed weak Euler solutions satisfying the local energy inequality at exponent $1/3$. Direction: build Euler solutions that are also vanishing-viscosity limits.
- **Anomalous dissipation for passive scalars** (Drivas, Elgindi, Colombo, Crippa, Sorella, Armstrong–Vicol): explicit divergence-free fields with anomalous scalar dissipation and total scalar mixing; Armstrong–Vicol's renormalization-group construction (2023) gives anomalous diffusion for advection–diffusion by a self-similar velocity field.
- **DNS at extreme resolution** (Kaneda/Ishihara; Sreenivasan–Buaria; Yeung): $R_\lambda>1000$ studies of extreme dissipation events indicating dissipation-range scaling that does not collapse with $\eta$ alone.
- **Wavelet/multifractal analysis** (Eyink, Chen; Ni–Xi): direct measurement of the singularity spectrum and tests of exact martingale-type refined similarity relations.

## 8. Future Work

- Prove anomalous dissipation for *one* forced 3D system — even a shell model, a Kraichnan-type velocity ensemble, or a Navier–Stokes system with degenerate noise. This is the consensus first target (Bedrossian's ICM-style program).
- Establish that some vanishing-viscosity subsequence converges to an Onsager-critical Euler solution, closing the loop between convex integration and physical selection.
- Derive $\zeta_2 = 2/3$, or its intermittency correction, from an exact hierarchy rather than a closure; candidate route is the Duchon–Robert local balance combined with monotonicity of the flux.
- Obtain rigorous inequalities constraining $\zeta_p$ — e.g. proving $\zeta_p \le p/3$ for $p>3$ from incompressibility alone would confirm that intermittency has a sign.
- Extend the 2D proof technology (where enstrophy control is available) to 3D helical or axisymmetric settings with an additional conserved quantity.

## 9. Key References

- **[Foundational]** A. N. Kolmogorov. *The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers.* Dokl. Akad. Nauk SSSR 30, 1941 (reprinted, Proc. R. Soc. Lond. A 434, 1991).
- **[Foundational]** A. N. Kolmogorov. *Dissipation of energy in the locally isotropic turbulence.* Dokl. Akad. Nauk SSSR 32, 1941.
- **[Foundational]** L. Onsager. *Statistical hydrodynamics.* Nuovo Cimento 6 (Suppl. 2), 1949.
- **[Foundational]** A. N. Kolmogorov. *A refinement of previous hypotheses concerning the local structure of turbulence…* J. Fluid Mech. 13, 1962.
- **[Survey]** U. Frisch. *Turbulence: The Legacy of A. N. Kolmogorov.* Cambridge University Press, 1995.
- **[Foundational]** P. Constantin, W. E, E. Titi. *Onsager's conjecture on the energy conservation for solutions of Euler's equation.* Comm. Math. Phys. 165, 1994.
- **[Foundational]** J. Duchon, R. Robert. *Inertial energy dissipation for weak solutions of incompressible Euler and Navier–Stokes equations.* Nonlinearity 13, 2000.
- **[SOTA]** P. Isett. *A proof of Onsager's conjecture.* Annals of Mathematics 188, 2018.
- **[SOTA]** T. Buckmaster, C. De Lellis, L. Székelyhidi Jr., V. Vicol. *Onsager's conjecture for admissible weak solutions.* Comm. Pure Appl. Math. 72, 2019.
- **[SOTA]** J. Bedrossian, M. Coti Zelati, S. Punshon-Smith, F. Weber. *A sufficient condition for the Kolmogorov 4/5 law for stationary martingale solutions to the 3D Navier–Stokes equations.* Comm. Math. Phys. 367, 2019.
- **[SOTA]** J. Bedrossian, A. Blumenthal, S. Punshon-Smith. *The Batchelor spectrum of passive scalar turbulence in stochastic fluid mechanics at fixed Reynolds number.* Comm. Pure Appl. Math. 75, 2022.
- **[SOTA]** C. Doering, C. Foias. *Energy dissipation in body-forced turbulence.* J. Fluid Mech. 467, 2002.
- **[Empirical]** F. Anselmet, Y. Gagne, E. J. Hopfinger, R. A. Antonia. *High-order velocity structure functions in turbulent shear flows.* J. Fluid Mech. 140, 1984.
- **[Empirical]** Z.-S. She, E. Leveque. *Universal scaling laws in fully developed turbulence.* Phys. Rev. Lett. 72, 1994.
- **[Empirical]** K. R. Sreenivasan. *On the universality of the Kolmogorov constant.* Phys. Fluids 7, 1995; *An update on the energy dissipation rate in isotropic turbulence.* Phys. Fluids 10, 1998.
- **[Survey]** G. L. Eyink, K. R. Sreenivasan. *Onsager and the theory of hydrodynamic turbulence.* Rev. Mod. Phys. 78, 2006.

## 10. Worked Example / Concrete Special Case

**Setting.** Air at room conditions, $\nu = 1.5\times10^{-5}\,\mathrm{m^2/s}$, in a wind tunnel with integral scale $L = 1\,\mathrm{m}$ and rms velocity $U = 1\,\mathrm{m/s}$.

**Step 1 — dissipation from the zeroth law.** Assuming $\varepsilon \approx 0.5\,U^3/L$ (Sreenivasan 1998),
$$\varepsilon \approx 0.5\ \mathrm{m^2/s^3}.$$
Note the $\nu$-independence: this is precisely the empirical content of claim (1), and precisely what is unproven.

**Step 2 — scale separation.**
$$\eta = \Big(\frac{\nu^3}{\varepsilon}\Big)^{1/4} = \Big(\frac{(1.5\times10^{-5})^3}{0.5}\Big)^{1/4} = (6.75\times10^{-15})^{1/4} \approx 2.9\times10^{-4}\ \mathrm{m}.$$
So $L/\eta \approx 3.5\times10^{3}$, giving $\sim (L/\eta)^3 \approx 4\times10^{10}$ active degrees of freedom — consistent with $\mathrm{Re}^{9/4}$ for $\mathrm{Re}=6.7\times10^4$.

**Step 3 — the $4/5$ law at $\ell = 10^{-2}\,\mathrm{m}$** (safely inertial: $\eta \ll \ell \ll L$):
$$\langle\delta u_\parallel^3\rangle = -\tfrac{4}{5}(0.5)(10^{-2}) = -4\times10^{-3}\ \mathrm{m^3/s^3}.$$
The sign is the cascade: negative skewness means energy moves to small scales.

**Step 4 — the $2/3$ law and its failure at high order.** With $C_2\approx 2.0$,
$$\langle\delta u_\parallel^2\rangle \approx 2.0\,(0.5)^{2/3}(10^{-2})^{2/3} = 2.0\times 0.63\times 0.0464 \approx 5.8\times10^{-2}\ \mathrm{m^2/s^2},$$
i.e. $\delta u_\parallel \approx 0.24\ \mathrm{m/s}$. Now compare $p=6$. K41 predicts $\zeta_6 = 2$; She–Leveque gives
$$\zeta_6 = \tfrac{6}{9} + 2\big(1-(2/3)^{2}\big) = 0.667 + 2(0.5556) = 1.778,$$
matching measurements ($\zeta_6 \approx 1.78$, Anselmet et al. 1984). Over the decade $\ell/L$ from $10^{-1}$ to $10^{-2}$, the two predictions differ by a factor $10^{2-1.778} \approx 1.7$ — small in one decade, but divergent as $\mathrm{Re}\to\infty$.

**What the example shows.** The exact identity (Step 3) is derivable from Navier–Stokes *once* Step 1 is granted; Step 4 shows that even granting Step 1, the self-similar extension of K41 is quantitatively wrong. The catalogued open problem is the conjunction: prove Step 1, then replace Step 4's ansatz with a derived $\zeta_p$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*