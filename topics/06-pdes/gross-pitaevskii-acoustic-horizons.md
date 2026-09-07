---
id: 06-pdes/gross-pitaevskii-acoustic-horizons
title: "Gross Pitaevskii Acoustic Horizons"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gross–Pitaevskii Acoustic Horizons

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/gross-pitaevskii-acoustic-horizons` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Gross–Pitaevskii (GP) equation for a dilute Bose gas with an external potential $V$ and repulsive coupling $g>0$. A **stationary transonic flow** is a solution $\psi_0(x)e^{-i\mu t/\hbar}$ whose Madelung velocity field $v=\nabla S/m$ crosses the local sound speed $c=\sqrt{g\rho/m}$ transversally at a point $x_h$ (the **acoustic horizon**), with $|v|<c$ upstream and $|v|>c$ downstream.

Two coupled open questions:

**(A) Dynamical existence and stability.** For which potentials $V$ and chemical potentials $\mu$ do such transonic stationary solutions exist in $d=1,2,3$, and are they *nonlinearly stable* — i.e. does an initial datum $\psi_0 + \varepsilon$ with $\|\varepsilon\|_{H^1}$ small remain, for all $t>0$, within $O(\varepsilon)$ of the orbit $\{e^{i\theta}\psi_0(\cdot-y)\}$ modulo the emitted radiation? The supersonic region carries **negative-energy Bogoliubov modes**, so the standard Lyapunov argument (energy minimisation at fixed mass) is unavailable, and the linearised generator is non-self-adjoint in the energy norm.

**(B) Rigorous Hawking effect with dispersion.** Let $\kappa=\partial_x(c-v)|_{x_h}$ be the surface gravity and $\xi=\hbar/(mc_h)$ the healing length at the horizon. Prove that the stationary scattering matrix of the Bogoliubov–de Gennes (BdG) operator on this background produces, in a suitable vacuum state, a flux of quanta whose spectrum is Planckian at $T_H=\hbar\kappa/2\pi k_B$, with an *explicit* error bound in the dispersive parameter $\varepsilon_{\rm disp}=\kappa\xi/c_h$:
$$\left|\,n(\omega) - \frac{1}{e^{2\pi\omega/\kappa}-1}\,\right| \le C(\omega)\,\varepsilon_{\rm disp}^{\,p},\qquad p>0 ,$$
uniformly for $\omega$ below the group-velocity cutoff $\omega_{\max}$. A complete solution to (B) states the class of profiles $(\rho,v)$ admitted, the quantum state (initial vacuum vs. Hadamard-type condition), the exponent $p$, and whether $C(\omega)$ blows up as $\omega\to0$.

Disproof of (B) would mean exhibiting an admissible profile with $\varepsilon_{\rm disp}\to0$ whose flux does not converge to Planckian.

## 2. Mathematical Foundations

The GP equation on $\mathbb{R}^d$:
$$i\hbar\,\partial_t\psi=-\frac{\hbar^{2}}{2m}\Delta\psi+V(x)\psi+g|\psi|^{2}\psi ,\qquad |\psi|^2\to\rho_\infty \text{ as } |x|\to\infty .$$
The natural phase space is the **Zhidkov / finite-energy space** $\mathcal{E}=\{\psi:\nabla\psi\in L^2,\ |\psi|^2-\rho_\infty\in L^2\}$ with energy
$$E(\psi)=\int \frac{\hbar^2}{2m}|\nabla\psi|^{2}+V(|\psi|^2-\rho_\infty)+\frac{g}{2}\big(|\psi|^{2}-\rho_\infty\big)^{2}\,dx .$$

**Madelung transform.** With $\psi=\sqrt{\rho}\,e^{iS/\hbar}$, $v=\nabla S/m$, GP is equivalent (where $\rho>0$) to
$$\partial_t\rho+\nabla\!\cdot(\rho v)=0,\qquad m\,\partial_t v+\nabla\!\left(\tfrac{m}{2}|v|^{2}+g\rho+V+Q[\rho]\right)=0,\qquad Q[\rho]=-\frac{\hbar^{2}}{2m}\frac{\Delta\sqrt{\rho}}{\sqrt{\rho}} .$$
$Q$ is the **quantum pressure**; dropping it gives isentropic Euler with sound speed $c=\sqrt{g\rho/m}$.

**Acoustic metric (Unruh 1981).** Linearising the hydrodynamic system about $(\rho_0,v_0)$ and writing $\delta S=\hbar\,\theta$, one obtains, to leading order in $\xi$,
$$\partial_\mu\!\left(\sqrt{-g}\,g^{\mu\nu}\partial_\nu\theta\right)=0,\qquad
g_{\mu\nu}=\frac{\rho_0}{c}\begin{pmatrix}-(c^{2}-|v_0|^{2}) & -v_0^{\!\top}\\[2pt] -v_0 & \mathbb{I}_d\end{pmatrix}.$$
The hypersurface $|v_0|=c$ is a Killing horizon of the vector field $\partial_t$; near it $g$ is Painlevé–Gullstrand-like, and $\kappa=\partial_n(c-|v_0|)|_{x_h}$ is the surface gravity.

**Bogoliubov–de Gennes system.** Exactly (no gradient expansion), fluctuations $\psi=\psi_0(1+\phi)$ obey a $2\times2$ non-self-adjoint system whose homogeneous-background dispersion relation is
$$\big(\omega-v_0k\big)^{2}=c^{2}k^{2}+\frac{\hbar^{2}k^{4}}{4m^{2}} ,$$
i.e. **superluminal (anomalous) dispersion**: group velocity $\to\infty$ as $k\to\infty$. Hence the "horizon" is not a causal barrier for short wavelengths; the acoustic-metric description holds only for $k\xi\ll1$. The BdG operator is self-adjoint for the indefinite Krein product $\langle(u,w),(u,w)\rangle=\int(|u|^2-|w|^2)$; the supersonic region supports modes of negative Krein norm ("negative-energy" modes), which is exactly the mechanism converting vacuum fluctuations into a correlated pair flux.

**Stationary scattering.** For a $1$D profile asymptotically homogeneous on both sides, fixing $\omega\in(0,\omega_{\max})$ gives four propagating channels: $u$ and $v$ (upstream), and downstream the pair $u^{\rm out}$, plus the negative-norm partner $\tilde u$. The $S$-matrix $S(\omega)$ is pseudo-unitary, $S^\dagger\eta S=\eta$ with $\eta=\mathrm{diag}(1,1,-1)$, and the emitted occupation number is $n(\omega)=|S_{u\tilde u}(\omega)|^{2}$.

## 3. History & State of the Art (SOTA)

- **1981.** Unruh shows that sound in a transonic fluid obeys the wave equation on a black-hole metric, and predicts thermal phonon emission at $T_H=\hbar\kappa/2\pi k_B$ (*Phys. Rev. Lett.* **46**, 1351).
- **1995.** Unruh, and independently Jacobson, note the **trans-Planckian problem**: the derivation appeals to arbitrarily short wavelengths. Lattice/dispersive models suggest robustness but no proof.
- **2000–2001.** Garay, Anglin, Cirac, Zoller propose BECs as the concrete realisation and analyse stability of sonic horizons in ring and de Laval geometries. Barceló–Liberati–Visser formalise "analogue gravity from BECs".
- **2009–2012.** Exact BdG scattering solved for piecewise-homogeneous 1D flows (Recati–Pavloff–Carusotto; Macher–Parentani; Larré–Recati–Carusotto–Pavloff), giving analytic $S(\omega)$ for "waterfall", "delta-peak" and "flat-profile" configurations. Deviations from thermality are $O(\varepsilon_{\rm disp})$ numerically.
- **2010–2016.** Density–density correlation function shown to carry the Hawking signal as an off-diagonal "tongue" (Balbinot–Fabbri–Fagnocchi–Carusotto–Recati, 2008; Carusotto et al., 2008), which becomes the experimental observable.
- **2016–2021.** Steinhauer reports correlated Hawking pairs in a BEC; Muñoz de Nova et al. (2019) report $T_H\approx0.35$ nK with thermal spectrum; Kolobov et al. (2021) study stationarity and horizon-region dynamics.
- **PDE side.** Global well-posedness in $\mathcal{E}$ (Zhidkov, $d=1$; Gérard, $d=2,3$ and $d=4$), Gravejat's nonexistence of supersonic travelling waves, Mariş's existence theorem for subsonic travelling waves in $d\ge3$, and Béthuel–Gravejat–Smets' stability of the black soliton form the rigorous backbone — but none of these treat flows with a horizon.

## 4. Partial Results / Verified Cases

- **Cauchy theory.** GP is globally well-posed in the energy space $\mathcal{E}$ for $d=1$ (Zhidkov 2001), $d=2,3$ (Gérard, *Ann. IHP* 2006) and $d=4$ (Gérard 2008, small energy). This covers all transonic backgrounds as *data*.
- **Explicit 1D transonic stationary solutions.** For step and $\delta$-potentials, the full family is known in closed form: the "waterfall" ($\rho$ monotone, one horizon), the "delta-peak" and the "flat-profile" configuration, parameterised by the upstream Mach number $M_-\in(0,1)$ and the downstream $M_+>1$ (Larré–Recati–Carusotto–Pavloff, *PRA* **85**, 013621, 2012). These are genuine solutions of the full GP ODE including the quantum pressure.
- **Exact $S$-matrix and near-thermality.** For piecewise-homogeneous 1D profiles, $S(\omega)$ is computed by matching the four roots of the quartic dispersion relation. Thermality with $T_H=\hbar\kappa/2\pi k_B$ is recovered numerically and asymptotically for $\varepsilon_{\rm disp}=\kappa\xi/c_h\lesssim0.1$; deviations grow to $O(1)$ for $\varepsilon_{\rm disp}\gtrsim1$ (Macher–Parentani, *PRA* **80**, 043601, 2009; Coutant–Parentani, *PRD* **89**, 084042, 2014). This is a controlled expansion, not a theorem with explicit constants.
- **Linear (spectral) stability.** For the 1D waterfall and flat-profile families, absence of complex-frequency BdG eigenvalues is verified numerically over the whole parameter range; the ring/de Laval geometries of Garay et al. exhibit genuine **dynamical instabilities** ("black-hole lasers") when a second, white-hole horizon closes the cavity — proved to be a discrete set of unstable modes in the idealised two-step model (Coutant–Parentani, *PRD* **81**, 084042, 2010).
- **Relativistic reference case.** Without dispersion, Hawking's result is a theorem: Fredenhagen–Haag (*CMP* **127**, 1990) derive the thermal flux from the short-distance (Hadamard) structure of the state on a collapsing spacetime; Gérard's microlocal framework (EMS, 2019) makes the construction of the relevant Hadamard states rigorous.
- **Travelling-wave theory** (adjacent, fully rigorous): no finite-energy travelling wave exists for speed $\mathfrak{c}>\sqrt{2}c$ (Gravejat 2004); solutions exist for all $\mathfrak{c}\in(0,\sqrt2 c)$ in $d\ge3$ (Mariş, *Annals of Math.* **178**, 2013); the transonic limit is governed by KP-I (Béthuel–Gravejat–Saut; Chiron–Mariş).

## 5. Principal Obstacles

1. **Indefinite energy.** The conserved GP energy is not coercive around a transonic profile: the supersonic region hosts negative-Krein-norm modes with real frequencies. Grillakis–Shatah–Strauss theory requires a finite-dimensional negative subspace; here the negative cone is infinite-dimensional and embedded in continuous spectrum.
2. **Non-self-adjoint, non-elliptic operator.** The BdG generator $JL$ on a flow with turning point is neither self-adjoint nor sectorial; resolvent estimates near the horizon degenerate because the symbol has a triple root at $(\omega,k)=(0,0)$ where $\omega-v_0k$ meets $\pm ck$.
3. **Failure of geometric optics at the horizon.** WKB is what produces $T_H$, but its validity condition $|\partial_x k|\ll k^2$ fails precisely in the region $|x-x_h|\lesssim\xi/\varepsilon_{\rm disp}^{1/3}$ — the "dispersive turning region", where the mode conversion between positive- and negative-norm branches actually happens. Uniform Airy-type normal forms exist formally but no error bound uniform in $\omega\to0$ has been proved.
4. **No Hadamard condition for dispersive fields.** In relativistic QFT the state is fixed by a microlocal wavefront-set condition. The quartic BdG dispersion relation has no Lorentzian light cone, so the standard Hadamard/microlocal machinery (Duistermaat–Hörmander propagation of singularities) does not apply and there is no accepted substitute characterisation of "vacuum".
5. **Infrared divergence.** In $1$D the emitted flux has $n(\omega)\sim\kappa/2\pi\omega$ as $\omega\to0$; the total particle number diverges logarithmically, so any stability statement must be modulo a slowly growing zero-mode/phase drift, which obstructs a clean orbital-stability formulation.
6. **Backreaction.** Emission depletes the condensate; the coupled GP + BdG system is a genuine nonlinear problem in which the horizon itself moves. No rigorous framework controls the drift of $x_h(t)$.

## 6. The Gap

Proven: (i) the background solutions exist explicitly in 1D for piecewise-constant potentials; (ii) the exact linear scattering coefficients are computable for those profiles; (iii) thermality holds *in the strictly dispersionless limit* $\xi\to0$ at the formal level, and rigorously in the relativistic analogue.

Missing: a theorem of the form "for all profiles in class $\mathcal{C}^k$ with $\varepsilon_{\rm disp}<\varepsilon_0$, the BdG $S$-matrix satisfies $n(\omega)=(e^{2\pi\omega/\kappa}-1)^{-1}+O(\varepsilon_{\rm disp}^{p})$". The precise missing step is a **uniform-in-$\omega$ connection formula across the dispersive turning region**: a rigorous matched asymptotic (exact WKB / Stokes-graph) analysis of the fourth-order ODE
$$\Big(\tfrac{\hbar^2}{4m^2}\partial_x^4 - \partial_x\big(c(x)^2-v(x)^2\big)\partial_x+\dots\Big)\phi=0$$
near a point where $c^2-v^2$ vanishes simply. On the nonlinear side, the gap is the absence of any coercive functional or virial/Morawetz estimate adapted to a flow with a sonic point.

## 7. Current Research (as of June 2026)

- **Exact WKB / resurgence for the quartic BdG symbol.** Applying Voros–Écalle exact-WKB and Stokes-graph methods to the fourth-order horizon ODE, aiming at rigorous connection matrices. Groups in Nice/Angers (Chiron, Mariş-adjacent PDE analysts) and mathematical-physics groups in Trento and Paris-Saclay. *(frontier — verify)*
- **Trento (Carusotto, Recati) and Nice/Orsay (Pavloff, Larré).** Correlation-function observables, backreaction, and analogue rotating (draining-vortex) horizons in 2D polariton and atomic condensates.
- **Bogoliubov–de Gennes spectral theory.** Krein-space Kato-type perturbation results for transonic backgrounds; conditions ruling out complex eigenvalues (black-hole-laser instability thresholds) in single-horizon geometries. *(frontier — verify)*
- **Analogue-gravity experiment.** Technion (Steinhauer) and Nottingham (Weinfurtner) on stationarity, greybody factors and subcritical flows; superfluid-helium and polariton platforms extend the parameter range of $\varepsilon_{\rm disp}$.
- **Microlocal analysis beyond Lorentzian cones.** Attempts to define a Hadamard-type state condition for dispersive/non-relativistic field operators, drawing on Gérard–Wrochna techniques. *(frontier — verify)*

## 8. Future Work

- Prove existence of smooth transonic stationary GP solutions for a *class* of potentials (not just step/$\delta$) via a shooting/centre-manifold argument at the sonic point, where the reduced ODE has a saddle-node structure.
- Establish linear (spectral) stability for the 1D waterfall family: show $\sigma(JL)\subset\mathbb{R}$ using Krein-signature counting plus absence of embedded eigenvalues.
- Obtain the first rigorous $O(\varepsilon_{\rm disp}^{p})$ thermality bound for an analytic profile with a single simple sonic point, with $p$ explicit ($p=1$ conjectured, possibly $p=2$ for symmetric profiles).
- Quantify greybody factors: prove $n(\omega)=\Gamma(\omega)(e^{2\pi\omega/\kappa}-1)^{-1}$ with $\Gamma$ the transmission coefficient of the associated effective potential.
- Nonlinear stability modulo emitted radiation, using an indefinite virial functional and modulation of $(x_h,\theta)$; expect a statement with slow logarithmic growth from the IR sector.
- Extend to 2D/3D draining-vortex flows, where ergoregion + horizon coexist and superradiance replaces (or supplements) Hawking emission.

## 9. Key References

- **[Foundational]** W. G. Unruh. *Experimental Black-Hole Evaporation?* Physical Review Letters **46**, 1351–1353, 1981.
- **[Foundational]** L. J. Garay, J. R. Anglin, J. I. Cirac, P. Zoller. *Sonic Analog of Gravitational Black Holes in Bose–Einstein Condensates.* Physical Review Letters **85**, 4643, 2000.
- **[Foundational]** C. Barceló, S. Liberati, M. Visser. *Analogue gravity from Bose–Einstein condensates.* Classical and Quantum Gravity **18**, 1137, 2001.
- **[Survey]** C. Barceló, S. Liberati, M. Visser. *Analogue Gravity.* Living Reviews in Relativity **14**:3, 2011.
- **[SOTA]** J. Macher, R. Parentani. *Black-hole radiation in Bose–Einstein condensates.* Physical Review A **80**, 043601, 2009.
- **[SOTA]** P.-É. Larré, A. Recati, I. Carusotto, N. Pavloff. *Quantum fluctuations around black hole horizons in Bose–Einstein condensates.* Physical Review A **85**, 013621, 2012.
- **[SOTA]** A. Coutant, R. Parentani. *Hawking radiation with dispersion: the broadened horizon paradigm.* Physical Review D **90**, 121501(R), 2014.
- **[PDE]** P. Gérard. *The Cauchy problem for the Gross–Pitaevskii equation.* Annales de l'IHP — Analyse Non Linéaire **23**, 765–779, 2006.
- **[PDE]** M. Mariş. *Traveling waves for nonlinear Schrödinger equations with nonzero conditions at infinity.* Annals of Mathematics **178**, 107–182, 2013.
- **[PDE]** F. Béthuel, P. Gravejat, D. Smets. *Asymptotic stability in the energy space for dark solitons of the Gross–Pitaevskii equation.* Annales Scientifiques de l'ENS **48**, 1327–1381, 2015.
- **[Rigorous Hawking, relativistic]** K. Fredenhagen, R. Haag. *On the derivation of Hawking radiation associated with the formation of a black hole.* Communications in Mathematical Physics **127**, 273–284, 1990.
- **[Book]** C. Gérard. *Microlocal Analysis of Quantum Fields on Curved Spacetimes.* EMS Publishing House, 2019.
- **[Experiment]** J. R. Muñoz de Nova, K. Golubkov, V. I. Kolobov, J. Steinhauer. *Observation of thermal Hawking radiation and its temperature in an analogue black hole.* Nature **569**, 688–691, 2019.

## 10. Worked Example / Concrete Special Case

**A smooth 1D transonic profile with an explicit surface gravity.** Work in 1D, stationary, and *inverse-engineer* the potential. Continuity gives $\rho v=J$ constant. Fix
$$\rho(x)=\rho_h\big(1-\epsilon\tanh(x/\sigma)\big),\qquad 0<\epsilon<1 ,$$
so $\rho$ decreases with $x$ and $v=J/\rho$ increases. Then $c(x)=\sqrt{g\rho/m}$ and the sonic condition $c=v$ at $x=0$ forces
$$J^{2}=\frac{g\rho_h^{3}}{m}\quad\Longleftrightarrow\quad J=\rho_h c_h,\qquad c_h=\sqrt{g\rho_h/m}.$$
The potential is then read off from the stationary Bernoulli equation,
$$V(x)=\mu-\frac{mJ^{2}}{2\rho^{2}}-g\rho+\frac{\hbar^{2}}{2m}\frac{(\sqrt{\rho})''}{\sqrt{\rho}} ,$$
which is smooth, bounded, and asymptotically constant on each side. So $(\rho,v,V)$ is an exact GP stationary transonic solution — quantum pressure included, not approximated.

**Surface gravity.** With $c=c_h\sqrt{\rho/\rho_h}$ and $v=c_h\rho_h/\rho$,
$$\partial_x(c-v)\big|_{0}=c_h\left(\frac{\rho'(0)}{2\rho_h}+\frac{\rho'(0)}{\rho_h}\right)=\frac{3c_h\rho'(0)}{2\rho_h},\qquad \rho'(0)=-\frac{\epsilon\rho_h}{\sigma},$$
hence
$$\kappa=\frac{3\epsilon c_h}{2\sigma},\qquad T_H=\frac{\hbar\kappa}{2\pi k_B}=\frac{3\epsilon\hbar c_h}{4\pi k_B\sigma}.$$

**Numbers.** Take $c_h=1.5$ mm/s, $\xi=\hbar/(mc_h)=0.5\ \mu$m, $\sigma=5\ \mu$m, $\epsilon=0.3$:
$$\kappa=\frac{3(0.3)(1.5\times10^{-3})}{2(5\times10^{-6})}=135\ \text{s}^{-1},\qquad
T_H=\frac{(1.055\times10^{-34})(135)}{2\pi(1.381\times10^{-23})}\approx1.6\times10^{-10}\ \text{K}\approx0.16\ \text{nK},$$
the same order as the $0.35$ nK reported by Muñoz de Nova et al. (2019). The dispersive parameter is
$$\varepsilon_{\rm disp}=\frac{\kappa\xi}{c_h}=\frac{3\epsilon\xi}{2\sigma}=\frac{3(0.3)(0.5)}{2(5)}=0.045 ,$$
so the hydrodynamic (acoustic-metric) description is marginally justified, and numerics on such profiles give spectra thermal to a few percent.

**Where the proof breaks.** Fluctuations $\phi=e^{-i\omega t}u(x)$ satisfy a fourth-order ODE whose symbol is $(\omega-v(x)k)^2-c(x)^2k^2-\hbar^2k^4/4m^2$. For $x<0$ the quartic has two real roots (subsonic); for $x>0$ it has four (supersonic), and the two extra roots — one of which carries **negative Krein norm** — are born at a turning point at $x\approx0$ where $k$ scales like $(\kappa m/\hbar)^{1/3}$, i.e. $k\xi\sim\varepsilon_{\rm disp}^{1/3}\approx0.36$. The WKB condition $|\partial_xk|\ll k^2$ fails exactly there. The thermal factor $e^{-2\pi\omega/\kappa}$ arises from the $\log$-singularity of the phase at the horizon in the *dispersionless* problem; making that statement uniform in $\omega$ for the quartic symbol, with an error $O(\varepsilon_{\rm disp}^p)$, is the open step described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*