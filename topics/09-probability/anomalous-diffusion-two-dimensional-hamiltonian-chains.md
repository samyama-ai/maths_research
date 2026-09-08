---
id: 09-probability/anomalous-diffusion-two-dimensional-hamiltonian-chains
title: "Anomalous Diffusion Exponent for the Two-Dimensional Anharmonic Chain"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Anomalous Diffusion Exponent for the Two-Dimensional Anharmonic Chain

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/anomalous-diffusion-two-dimensional-hamiltonian-chains` · **Status:** open

## 1. Problem Statement / Conjecture

Consider a momentum-conserving anharmonic crystal on $\mathbb{Z}^2$ in thermal equilibrium at temperature $T>0$ and zero pressure. Energy is a locally conserved quantity; let $\mathcal{E}(x,t)$ denote the energy field and let

$$
S_{\mathrm{ee}}(x,t)=\big\langle \mathcal{E}(x,t)\,\mathcal{E}(0,0)\big\rangle^{c}_{T}
$$

be its equilibrium space–time correlation, with $c$ denoting the truncated (connected) correlation. Define the mean-square spread of the energy pulse
$$
\sigma^2(t)=\frac{\sum_{x\in\mathbb{Z}^2}|x|^2\,S_{\mathrm{ee}}(x,t)}{\sum_{x\in\mathbb{Z}^2}S_{\mathrm{ee}}(x,t)},
$$
after subtracting the ballistic sound peaks.

**Conjecture (marginal superdiffusion in $d=2$).** For a generic non-integrable, momentum-conserving anharmonic potential in two dimensions, energy transport is superdiffusive but only marginally so:
$$
\sigma^2(t)\;\asymp\; t\,(\ln t)^{\gamma},\qquad \gamma>0,
$$
equivalently the Green–Kubo integrand decays as $C_{JJ}(t)\sim t^{-1}(\ln t)^{\gamma-1}$ and the finite-size conductivity of a chain of linear size $N$ diverges as $\kappa(N)\sim(\ln N)^{\gamma}$.

**The open exponent.** The value of $\gamma$ is not known. One-loop mode-coupling gives $\gamma=1$ ($\kappa\sim\ln N$); the self-consistent closure of the same theory gives $\gamma=\tfrac12$ ($\kappa\sim\sqrt{\ln N}$). A complete solution must (i) prove that $\kappa(N)\to\infty$ (no Fourier law) for a genuine Hamiltonian model, (ii) prove the upper bound $\sigma^2(t)=O(t^{1+\epsilon})$ excluding a power-law anomaly, and (iii) determine $\gamma$.

## 2. Mathematical Foundations

**Model.** Particles labelled by $x\in\Lambda_N=(\mathbb{Z}/N\mathbb{Z})^2$ with displacement $q_x\in\mathbb{R}^n$ and momentum $p_x\in\mathbb{R}^n$, Hamiltonian
$$
H=\sum_{x\in\Lambda_N}\frac{|p_x|^2}{2m}+\sum_{\langle x,y\rangle}V(q_x-q_y),\qquad
V(r)=\tfrac12 |r|^2+\tfrac{\lambda_3}{3}|r|^3+\tfrac{\lambda_4}{4}|r|^4 .
$$
Dynamics $\dot q_x=p_x/m$, $\dot p_x=-\partial_{q_x}H$ conserves total energy, total momentum $\sum_x p_x$, and total stretch. Gibbs states $\propto e^{-\beta(H-\text{pressure terms})}$ are the relevant invariant measures.

**Green–Kubo.** With local energy $e_x$ and energy currents $j_{x,x+\hat{e}_i}$ satisfying $\frac{d}{dt}e_x=-\sum_i\big(j_{x,x+\hat e_i}-j_{x-\hat e_i,x}\big)$, define $J_i=\sum_x j_{x,x+\hat e_i}$ and
$$
\kappa=\frac{1}{k_BT^2}\lim_{\tau\to\infty}\lim_{N\to\infty}\frac{1}{N^2}\int_0^{\tau} \big\langle J_1(t)J_1(0)\big\rangle_T\,dt .
$$
Anomalous transport means this limit is $+\infty$; the divergence rate defines the exponent through $\kappa(N)\sim N^{\alpha}$ or $\sim(\ln N)^{\gamma}$.

**Nonlinear fluctuating hydrodynamics (NLFH).** Linearising the Euler equations for the conserved fields $\vec u=(\text{stretch},\text{momentum},\text{energy})$ and diagonalising gives normal modes $\phi_\sigma$ with velocities $\{0,\pm c\}$ ($c$ = sound speed). Each mode obeys
$$
\partial_t\phi_\sigma+\partial_x\!\big(v_\sigma\phi_\sigma+\langle\phi,G^\sigma\phi\rangle\big)=D_\sigma\Delta\phi_\sigma+\text{noise},
$$
with $G^\sigma$ the second-order expansion of the currents. In $d=1$ the quadratic term is relevant and drives the heat mode to Lévy-$5/3$ scaling, $\sigma^2(t)\sim t^{4/3}$, $z=3/2$ (Spohn 2014; van Beijeren 2012). In $d=2$ the nonlinearity is **marginal**: power counting for the one-loop memory kernel gives
$$
C_{JJ}(t)\;\propto\;\int_{\mathbb{R}^2}\!\frac{d^2k}{(2\pi)^2}\,e^{-2D k^2 t}\;\propto\;\frac{1}{t},
$$
whose time integral diverges logarithmically — the same marginality as $2$-dimensional long-time tails in fluids (Alder–Wainwright / Ernst–Hauge–van Leeuwen).

**Self-consistent closure.** Replacing the bare $Dk^2$ by a memory-dressed damping $\Gamma(k,t)$ and demanding consistency yields instead $C_{JJ}(t)\sim (t\sqrt{\ln t})^{-1}$, hence $\kappa(N)\sim\sqrt{\ln N}$ — the $\gamma=\tfrac12$ scenario (Lepri–Livi–Politi; Delfini et al.).

## 3. History & State of the Art (SOTA)

- **1955–1970.** Fermi–Pasta–Ulam–Tsingou numerics open the question of whether Hamiltonian lattices obey Fourier's law at all.
- **1970s.** Alder–Wainwright long-time tails and the mode-coupling analysis of Ernst, Hauge and van Leeuwen establish the $t^{-d/2}$ decay of current correlations, predicting divergence of transport coefficients in $d\le 2$.
- **2000.** Lippi and Livi simulate 2d FPU-type lattices and report $\kappa$ consistent with a logarithmic divergence in system size (J. Stat. Phys. 100, 1147).
- **2002.** Narayan and Ramaswamy derive $d$-dependent exponents from fluctuating hydrodynamics, giving $t^{-d/(1+d)}$ ($d=1$: $t^{-1/2}$) and marginal behaviour in $d=2$ (PRL 89, 200601).
- **2003, 2008.** Reviews by Lepri–Livi–Politi (Phys. Rep. 377) and Dhar (Adv. Phys. 57) codify the $\kappa\sim\ln N$ expectation in $d=2$.
- **2006–2016.** Rigorous branch: Basile–Bernardin–Olla add momentum-conserving noise and *prove* $\kappa\sim\sqrt{N}$ in $d=1$, $\kappa\sim\ln N$ in $d=2$ for the harmonic-plus-noise chain (PRL 96, 204303). Jara–Komorowski–Olla and Bernardin–Gonçalves–Jara then establish $3/4$-fractional superdiffusion scaling limits in $d=1$.
- **2012.** Wang, Hu and Li give large-scale 2d simulations supporting $\kappa\propto\ln N$ over three decades (PRE 86, 040101(R)).
- **2014–2016.** Spohn's NLFH gives the sharp $d=1$ picture (KPZ sound peaks, Lévy-$5/3$ heat peak); the $d=2$ case remains at the level of marginal power counting.

Current status: a logarithmic law is the consensus, but no derivation from a deterministic Hamiltonian is rigorous, and the numerics do not separate $\ln N$ from $\sqrt{\ln N}$.

## 4. Partial Results / Verified Cases

- **Harmonic chain + energy–momentum-conserving noise, $d=2$:** proven $\kappa(N)\asymp\ln N$, i.e. $\gamma=1$ (Basile–Bernardin–Olla 2006; Basile–Olla–Spohn, ARMA 195 (2010) 171). Kinetic (phonon Boltzmann) limits make the divergence explicit.
- **$d=1$ stochastic chains:** $\kappa\sim N^{1/2}$ for the noisy harmonic chain; energy superdiffuses as a $3/4$-stable process, $\sigma^2(t)\sim t^{4/3}$ (Jara–Komorowski–Olla, CMP 339 (2015) 407; Bernardin–Gonçalves–Jara, ARMA 220 (2016) 505).
- **$d\ge 3$ stochastic chains:** $\kappa<\infty$ — Fourier's law holds, current correlations are integrable ($t^{-d/2}$, $d/2>1$).
- **Momentum non-conserving cases:** with an on-site pinning potential $\tfrac{\nu}{2}|q_x|^2$, normal diffusion holds in all $d\ge1$ for stochastic models; numerically $\kappa<\infty$ for pinned 2d lattices at all $T$.
- **Integrable exceptions:** 2d harmonic crystals without noise are ballistic, $\sigma^2(t)\sim t^2$ — showing anharmonicity is essential to the conjecture.
- **Numerics:** 2d FPU-$\beta$, Lennard-Jones and $\phi^4$-free scalar models for $N$ up to $\sim 2^{12}$ per side, $T\in[0.1,1]$, all consistent with $\kappa=a+b\ln N$; effective power-law fits give $\alpha_{\mathrm{eff}}\lesssim 0.05$ and drifting downward with $N$.

## 5. Principal Obstacles

- **Marginality kills every scaling argument.** In $d=1$ the nonlinearity is strictly relevant, so a renormalisation-group or NLFH fixed point exists (KPZ, Lévy-$5/3$). In $d=2$ the coupling is exactly marginal, so the answer sits in the *logarithmic corrections*, which are exactly what one-loop power counting cannot fix. Distinguishing $\gamma=1$ from $\gamma=\tfrac12$ requires resumming the full series, not a fixed point.
- **No mixing input for deterministic dynamics.** All rigorous results add a stochastic exchange noise precisely because deterministic Hamiltonian lattices offer no proof of ergodicity or of decay of correlations in the Gibbs state. Even the qualitative statement $\kappa=\infty$ is open for a single Hamiltonian anharmonic 2d model.
- **Green–Kubo is not known to be well-posed.** The double limit $\lim_{\tau}\lim_{N}$ has no proof of existence for anharmonic lattices; one cannot even guarantee $C_{JJ}(t)$ is eventually monotone.
- **Noise changes the answer's mechanism.** The stochastic models are effectively *harmonic plus scattering*, where the log comes from a phonon-Boltzmann collision rate $W(k)\propto|k|^2$. Genuine anharmonic three-phonon scattering has a different low-$k$ rate, and there is no transfer theorem.
- **Numerical resolution is exponentially bad.** Deciding $\gamma$ needs to resolve $\sqrt{\ln N}$ against $\ln N$; a factor-2 change in the ratio requires $N$ to change by a factor $e^{4}\approx 55$ per decade of discrimination, i.e. lattices of $10^{8}$–$10^{10}$ sites plus $t\sim N$ integration.
- **Boundary and finite-size artefacts.** In 2d, the sound peaks and the heat peak overlap for far longer than in 1d, contaminating $\sigma^2(t)$ with ballistic weight.

## 6. The Gap

Proven: marginal logarithmic divergence with $\gamma=1$, for the *harmonic* chain in $d=2$ perturbed by a conservative noise. Conjectured: the same marginal class, with an unknown $\gamma$, for *deterministic anharmonic* Hamiltonian dynamics.

Two distinct steps are missing.

1. **Removing the noise.** One must show that the anharmonic terms $\lambda_3,\lambda_4\ne 0$ generate enough phonon scattering to reproduce the noise-induced kernel, uniformly in $N$ — i.e. a rigorous kinetic (phonon Boltzmann) limit for a deterministic anharmonic crystal. Nothing of the sort is known beyond formal weak-coupling expansions.
2. **Fixing the logarithm's power.** Even granting NLFH as a valid effective theory, no argument selects between the bare one-loop ($\gamma=1$) and self-consistent ($\gamma=\tfrac12$) closures. The gap is a controlled resummation of the marginal coupling — the analogue of computing the logarithmic correction at the upper critical dimension, but for a nonequilibrium transport kernel with three coupled modes.

## 7. Current Research (as of June 2026)

- **Rigorous stochastic lattices** (Olla and collaborators, CEREMADE Paris–Dauphine; Bernardin, Rennes; Komorowski, Lublin/IMPAN; Jara, IMPA). Focus: superdiffusive scaling limits and fractional Laplacian generators; extending $d=1$ results to $d=2$ marginal kernels and to weakly anharmonic perturbations of the noisy chain. *(frontier — verify)* Reports of an $\ln$-corrected hydrodynamic limit for 2d noisy chains with a cubic perturbation.
- **NLFH and mode-coupling** (Spohn, TU München; Mendl; Lepri–Livi–Politi, ISC-CNR Florence). Focus: two-loop and self-consistent kernels in $d=2$; whether the sound modes carry a 2d analogue of KPZ.
- **Large-scale simulation** (Li, Hu and collaborators; Dhar and Kundu, ICTS Bengaluru). GPU lattices with $N\ge 2^{14}$ per side, direct measurement of $S_{\mathrm{ee}}(x,t)$ rather than $\kappa(N)$, to reduce boundary artefacts.
- **Kinetic-theory route.** Rigorous phonon Boltzmann limits for weakly anharmonic crystals (Lukkarinen–Spohn programme) applied at $d=2$; the low-$k$ behaviour of the collision operator is the key unknown.

## 8. Future Work

- Prove $\kappa(N)\to\infty$ for *any* deterministic momentum-conserving anharmonic lattice in $d=2$ — a qualitative result would already be a breakthrough.
- Establish an upper bound $\sigma^2(t)\le C t\,(\ln t)^{C'}$ to exclude power-law superdiffusion; the $d=1$ techniques (Varadhan-type resolvent bounds) are the natural starting point.
- Compute the two-loop correction to the $d=2$ NLFH memory kernel and check whether it renormalises $\gamma$ away from $1$.
- Add weak anharmonicity to the Basile–Bernardin–Olla model as a perturbation and track whether $\gamma$ is stable.
- Design a numerical observable whose leading behaviour is $\gamma$ itself — for example the logarithmic derivative $d\ln\kappa/d\ln\ln N$ — instead of fitting $\kappa(N)$.
- Test the $d=2$ prediction in physically realisable systems (suspended graphene, 2d colloidal crystals), where a $\ln$ law is experimentally reported.

## 9. Key References

- **[Foundational]** S. Lepri, R. Livi, A. Politi. *Thermal conduction in classical low-dimensional lattices.* Physics Reports **377** (2003) 1–80.
- **[Foundational]** A. Lippi, R. Livi. *Heat conduction in two-dimensional nonlinear lattices.* Journal of Statistical Physics **100** (2000) 1147–1172.
- **[Foundational]** O. Narayan, S. Ramaswamy. *Anomalous heat conduction in one-dimensional momentum-conserving systems.* Physical Review Letters **89** (2002) 200601.
- **[Rigorous]** G. Basile, C. Bernardin, S. Olla. *Momentum conserving model with anomalous thermal conductivity in low dimensional systems.* Physical Review Letters **96** (2006) 204303.
- **[Rigorous]** G. Basile, S. Olla, H. Spohn. *Energy transport in stochastically perturbed lattice dynamics.* Archive for Rational Mechanics and Analysis **195** (2010) 171–203.
- **[Rigorous]** M. Jara, T. Komorowski, S. Olla. *Superdiffusion of energy in a chain of harmonic oscillators with noise.* Communications in Mathematical Physics **339** (2015) 407–453.
- **[Rigorous]** C. Bernardin, P. Gonçalves, M. Jara. *3/4-fractional superdiffusion in a system of harmonic oscillators perturbed by a conservative noise.* Archive for Rational Mechanics and Analysis **220** (2016) 505–542.
- **[SOTA / Theory]** H. Spohn. *Nonlinear fluctuating hydrodynamics for anharmonic chains.* Journal of Statistical Physics **154** (2014) 1191–1227.
- **[SOTA / Theory]** H. van Beijeren. *Exact results for anomalous transport in one-dimensional Hamiltonian systems.* Physical Review Letters **108** (2012) 180601.
- **[SOTA / Numerics]** L. Wang, B. Hu, B. Li. *Logarithmic divergent thermal conductivity in two-dimensional nonlinear lattices.* Physical Review E **86** (2012) 040101(R).
- **[Theory]** L. Delfini, S. Lepri, R. Livi, A. Politi. *Self-consistent mode-coupling approach to one-dimensional heat transport.* Physical Review E **73** (2006) 060201(R).
- **[Survey]** A. Dhar. *Heat transport in low-dimensional systems.* Advances in Physics **57** (2008) 457–537.
- **[Survey]** S. Lepri (ed.). *Thermal Transport in Low Dimensions: From Statistical Physics to Nanoscale Heat Transfer.* Lecture Notes in Physics **921**, Springer, 2016.
- **[Related]** K. Saito, A. Dhar. *Heat conduction in a three dimensional anharmonic crystal.* Physical Review Letters **104** (2010) 040601.

## 10. Worked Example / Concrete Special Case

**The solvable 2d case: harmonic crystal with momentum-conserving noise.**

Take scalar displacements $q_x\in\mathbb{R}$, $x\in\mathbb{Z}^2$, with
$$
H=\sum_x\Big(\tfrac12 p_x^2+\tfrac12\sum_{i=1,2}(q_{x+\hat e_i}-q_x)^2\Big),
$$
and add a stochastic exchange that randomly rotates momentum triples on plaquettes at rate $\gamma$, conserving $\sum p_x$ and $\sum p_x^2$.

*Step 1 — dispersion.* Fourier transform, $k\in[-\pi,\pi]^2$:
$$
\omega(k)=2\sqrt{\sin^2(k_1/2)+\sin^2(k_2/2)}\;\xrightarrow[k\to0]{}\;|k| .
$$
Group velocity $\nabla\omega(k)\to k/|k|$, of modulus $1$ at small $k$.

*Step 2 — scattering rate.* The noise gives a phonon Boltzmann equation for the Wigner distribution $W(k,t)$ with relaxation rate vanishing quadratically at long wavelength:
$$
\tau(k)^{-1}\;=\;\gamma\,c_0\,|k|^{2}\;+\;O(|k|^{4}),
$$
because momentum conservation forbids scattering of the $k\to0$ mode.

*Step 3 — Green–Kubo in relaxation-time form.*
$$
\kappa \;=\; \frac{1}{k_BT}\int_{[-\pi,\pi]^2}\frac{d^2k}{(2\pi)^2}\;\big|\partial_{k_1}\omega(k)\big|^{2}\,\tau(k)
\;\approx\;\frac{1}{k_BT}\int_{2\pi/N}^{\Lambda}\frac{2\pi k\,dk}{(2\pi)^2}\;\frac{1/2}{\gamma c_0 k^{2}} .
$$

*Step 4 — the logarithm.* The radial integral is $\int dk/k$:
$$
\kappa(N)\;=\;\frac{1}{8\pi\gamma c_0 k_BT}\,\ln\!\Big(\frac{\Lambda N}{2\pi}\Big)+O(1)\;\sim\;\frac{\ln N}{8\pi\gamma c_0 k_BT}.
$$
The infrared cutoff is the smallest wavenumber a box of side $N$ supports; the divergence is exactly logarithmic, so $\gamma_{\text{exponent}}=1$ here. Equivalently $C_{JJ}(t)\sim (4\pi\gamma c_0 t)^{-1}$ and $\sigma^2(t)\sim t\ln t$.

*Why this does not settle the conjecture.* The calculation uses two facts special to the noisy harmonic model: the phonon spectrum is exactly $\omega(k)$ for all times, and the collision rate is exactly $\propto|k|^2$ with no feedback. For a genuine anharmonic crystal, three-phonon processes make $\tau(k)$ itself depend on the dressed damping. Substituting the self-consistent ansatz $\tau(k)^{-1}\propto |k|^{2}\,\kappa$ and requiring $\kappa\propto\int_{1/N} dk\,k^{-1}\kappa^{-1}$ gives $\kappa^{2}\propto\ln N$, i.e. $\kappa\sim\sqrt{\ln N}$ and $\gamma=\tfrac12$. The two closures differ only in whether the damping is bare or dressed — and no one knows which is correct.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*