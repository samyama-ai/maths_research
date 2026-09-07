---
id: 06-pdes/landau-lifshitz-gilbert-blow-up
title: "Landau Lifshitz Gilbert Blow Up"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Finite-Time Blow-Up for the Landau–Lifshitz–Gilbert Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/landau-lifshitz-gilbert-blow-up` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $u : \mathbb{R}^d \times [0,T) \to \mathbb{S}^2 \subset \mathbb{R}^3$ solve the Landau–Lifshitz–Gilbert (LLG) equation

$$\partial_t u \;=\; \alpha_1\, u \times \Delta u \;-\; \alpha_2\, u \times (u \times \Delta u), \qquad |u| = 1,$$

with damping $\alpha_2 > 0$ and precession $\alpha_1 \in \mathbb{R}$. The problem is to decide, for each $d$ and each parameter pair $(\alpha_1,\alpha_2)$, whether smooth finite-energy initial data $u_0$ exist for which the solution loses regularity in finite time, i.e. $\limsup_{t \to T^-}\|\nabla u(t)\|_{L^\infty} = \infty$ for some $T < \infty$.

The sharp open case is the **energy-critical dimension $d = 2$ with both terms present** ($\alpha_1 \neq 0$, $\alpha_2 > 0$):

> **Conjecture.** For every $\alpha_1 \neq 0$, $\alpha_2 > 0$ there exist smooth, compactly-supported-gradient data $u_0 : \mathbb{R}^2 \to \mathbb{S}^2$ whose LLG solution blows up in finite time by concentrating a nontrivial harmonic map (a "bubble") at a point, with concentration rate $\lambda(t) \to 0$ as $t \to T^-$.

A complete resolution requires either (i) a construction of such data together with the blow-up rate and the bubble profile, or (ii) a proof of global regularity for all smooth finite-energy data when $\alpha_1\alpha_2 \neq 0$ in $d=2$ — which would separate LLG sharply from both of its endpoint limits.

## 2. Mathematical Foundations

**Gilbert form.** With effective field $H_{\mathrm{eff}} = \Delta u$ (exchange only), the physical form is
$$\partial_t u = -\gamma\, u \times H_{\mathrm{eff}} + \alpha\, u \times \partial_t u,\qquad \alpha>0 .$$
Taking $u\times$ and using $|u|=1$ converts this to the Landau–Lifshitz form above with $\alpha_1 = \gamma/(1+\alpha^2)$, $\alpha_2 = \alpha\gamma/(1+\alpha^2)$.

**Dissipative form.** Since $-u \times (u \times X) = X - (u\cdot X)u$ and $u\cdot\Delta u = -|\nabla u|^2$ on the sphere,
$$\partial_t u \;=\; \alpha_2\big(\Delta u + |\nabla u|^2 u\big) \;+\; \alpha_1\, u \times \Delta u .$$
The bracket is the tension field $\tau(u)$ of the map into $\mathbb{S}^2$. Thus LLG interpolates between the **harmonic map heat flow** ($\alpha_1 = 0$) and the **Schrödinger map flow** ($\alpha_2 = 0$).

**Energy.** $E(u) = \tfrac12 \int_{\mathbb{R}^d} |\nabla u|^2\,dx$ satisfies
$$\frac{d}{dt}E(u(t)) \;=\; -\alpha_2 \int_{\mathbb{R}^d} \big|\Delta u + |\nabla u|^2u\big|^2\,dx \;\le\; 0,$$
the precession term being energy-neutral ($\int \nabla u\cdot\nabla(u\times\Delta u)=0$).

**Scaling and criticality.** $u_\lambda(x,t) = u(\lambda x, \lambda^2 t)$ solves LLG whenever $u$ does, and $E(u_\lambda) = \lambda^{2-d}E(u)$. Hence $d=2$ is energy-critical, $d\ge 3$ energy-supercritical. The critical Sobolev space is $\dot H^{d/2}$.

**Harmonic maps and equivariance.** Steady states of the heat part are harmonic maps $\tau(u)=0$. In $m$-equivariant coordinates $(r,\theta)$,
$$u(r,\theta,t) = \big(\sin\phi\,\cos(m\theta+\psi),\ \sin\phi\,\sin(m\theta+\psi),\ \cos\phi\big),\qquad \phi=\phi(r,t),\ \psi=\psi(r,t),$$
LLG reduces to a coupled system for $(\phi,\psi)$; when $\alpha_1=0$ one may take $\psi\equiv 0$. The explicit harmonic maps are
$$Q_m(r) = 2\arctan(r^m), \qquad E(Q_m) = 4\pi m,$$
each generating a scaling family $Q_m(r/\lambda)$ and a dilation zero mode $\Lambda Q_m = r\partial_r Q_m$.

**Bubbling theorem (Struwe-type).** In $d=2$ there is $\varepsilon_0>0$ such that if $\sup_{x}E(u_0; B_1(x)) < \varepsilon_0$ then the solution stays smooth for a time depending only on the local energy; energy concentration below $\varepsilon_0$ is impossible, so blow-up must quantize at least $4\pi$ of energy.

## 3. History & State of the Art (SOTA)

- **1935.** Landau and Lifshitz introduce the gyromagnetic equation with damping for ferromagnetic domain structure.
- **1955/2004.** Gilbert reformulates the damping term; the two forms are algebraically equivalent (published in full in IEEE Trans. Magn., 2004).
- **1985.** Struwe: global weak solutions of the 2D harmonic map heat flow, smooth off finitely many points, with bubbling at singular times.
- **1989–1992.** Coron–Ghidaglia produce finite-time blow-up for harmonic map heat flow in $d\ge 3$; Chang–Ding–Ye do so in $d=2$ for equivariant data on the disc — the first proof that the critical-dimension flow is not globally regular.
- **1992–1993.** Alouges–Soyeur prove global existence of weak LLG solutions ($\alpha_2>0$) and non-uniqueness; Guo–Hong prove 2D partial regularity for LLG.
- **2004–2007.** Harpes establishes uniqueness and bubbling for the 2D LLG flow; Melcher gives partial regularity in $d=3$. **Ding–Wang (2007)** construct the first genuine LLG finite-time singularities, in $d=3,4$.
- **2010–2013.** Gustafson–Nakanishi–Tsai give a unified $m$-equivariant analysis of heat flow, LLG and Schrödinger maps on $\mathbb{R}^2$; Rodnianski–Sterbenz and Merle–Raphaël–Rodnianski, and independently Perelman, construct blow-up for the $m=1$ Schrödinger map; Raphaël–Schweyer construct *stable* blow-up for the $m=1$ harmonic map heat flow.
- **2020s.** Inner–outer gluing methods (Dávila–del Pino–Wei and successors) produce blow-up with prescribed rates for the heat flow and are being pushed toward $\alpha_1\neq 0$.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $d=1$, any $\alpha_1,\alpha_2$ | Global smooth solutions for smooth data (Zhou–Guo; see Guo–Ding, *Landau–Lifshitz Equations*). No blow-up. |
| $d=2$, small energy $E(u_0)<\varepsilon_0$ | Global smooth, $u(t)\to$ constant. |
| $d=2$, $\alpha_1=0$ (heat flow), $m$-equivariant, $m=1$ | **Blow-up proven** (Chang–Ding–Ye 1992); stable rate $\lambda(t)\sim \kappa\,(T-t)/|\log(T-t)|^2$ (Raphaël–Schweyer 2013). |
| $d=2$, $\alpha_2=0$ (Schrödinger map), $m=1$ | **Blow-up proven** (Merle–Raphaël–Rodnianski 2013; Perelman 2014). |
| $d=2$, $\alpha_1\alpha_2\ne0$, $m$-equivariant, $m\ge 3$ | **No blow-up**: harmonic maps $Q_m$ are asymptotically stable, solutions near $Q_m$ are global (Gustafson–Nakanishi–Tsai 2010). |
| $d=2$, $\alpha_1\alpha_2\ne0$, $m=2$ | Global for data near $Q_2$, but $\lambda(t)$ may oscillate without limit; no blow-up construction. |
| $d=2$, $\alpha_1\alpha_2\ne0$, $m=1$ | **Open.** |
| $d=3,4$, $\alpha_2>0$ | **Blow-up proven** for suitable equivariant data on the ball (Ding–Wang, IMRN 2007). |
| $d\ge 3$, small $\|\nabla u_0\|_{\mathrm{BMO}}$ (or small critical norm) | Global smooth (Melcher 2012; Bejenaru–Ionescu–Kenig–Tataru 2011 for $\alpha_2=0$). |
| $d\ge 2$, $\alpha_2>0$, general data | Global weak solutions exist; partially regular with singular set of parabolic Hausdorff dimension $\le d-2$. |

## 5. Principal Obstacles

- **Loss of variational structure.** For $\alpha_1=0$ the flow is the $L^2$-gradient flow of $E$, so monotonicity formulas (Struwe's local energy inequality, backward-heat-kernel monotonicity) drive the blow-up analysis. Adding $\alpha_1 u\times\Delta u$ keeps $E$ decreasing but destroys the gradient-flow structure: there is no known local monotone quantity adapted to the mixed operator, so blow-up cannot be forced by energy comparison alone.
- **Loss of the maximum principle and of comparison.** The Chang–Ding–Ye argument uses a scalar parabolic comparison for $\phi(r,t)$ under equivariance. With $\alpha_1\neq 0$ the reduction produces a *coupled* system for $(\phi,\psi)$ with a first-order coupling; no comparison principle survives.
- **Non-self-adjoint linearization.** Linearizing at $Q_m/\lambda$ gives $\mathcal{L}_{\alpha} = (\alpha_2 + i\alpha_1)\mathcal{L}$ where $\mathcal{L}=-\Delta+V$ is the (self-adjoint) heat-flow linearization written in the gauge-covariant complex form. The rotated spectral sector mixes dissipative and dispersive decay: parabolic energy estimates lose the smoothing exponent, and dispersive/Strichartz estimates lose the pointwise damping.
- **The $m=1$ logarithm.** $\Lambda Q_1 = 2r/(1+r^2)$ is *not* in $L^2(\mathbb{R}^2)$: $\|\Lambda Q_1\|^2_{L^2(r<R)} \sim 8\pi\log R$. Modulation for the scaling parameter is therefore only logarithmically coercive, forcing sharp (rather than soft) construction of an approximate profile to many orders — the technical core of Raphaël–Schweyer and of MRR — and these two constructions use *different* mechanisms (dissipative vs. dispersive tail radiation) that have not been merged.
- **Non-uniqueness of weak solutions.** Alouges–Soyeur's non-uniqueness means any "weak-solution blow-up" statement is ambiguous; one must work with strong solutions, losing global-in-time compactness tools.

## 6. The Gap

Proven: blow-up at the two endpoints $\alpha_1=0$ and $\alpha_2=0$ in $d=2$ with $m=1$; blow-up for $\alpha_2>0$ in $d=3,4$; no blow-up near $Q_m$ for $m\ge3$ in $d=2$ for all $(\alpha_1,\alpha_2)$.

Missing: a construction valid for the *interior* of the parameter segment $\alpha_1\alpha_2\neq 0$ at $d=2$, $m=1$. Concretely, one must produce a modulation law for $\lambda(t) \in \mathbb{R}_{>0}$ and a phase $\gamma(t)$ solving the coupled system
$$(\alpha_2 - i\alpha_1)^{-1}\Big(\frac{\dot\lambda}{\lambda} + i\dot\gamma\Big)\,\|\Lambda Q_1\|^2_{L^2(r<\lambda^{-1})} \;=\; -\,\mathcal{F}[\varepsilon,\lambda],$$
where $\varepsilon$ is the radiation remainder and $\mathcal{F}$ its flux, and show the resulting $\lambda(t)$ reaches $0$ at finite $T$ rather than oscillating or converging to a positive limit. The rotation $(\alpha_2-i\alpha_1)^{-1}$ couples $\dot\lambda$ to $\dot\gamma$; the open question is whether this coupling can pump energy back out of the core and *prevent* concentration. No proof in either direction is known.

## 7. Current Research (as of June 2026)

- **Inner–outer gluing.** The Dávila–del Pino–Wei parabolic gluing scheme has been adapted to complex-coefficient parabolic operators; several groups report blow-up constructions for LLG in $d=2$, $m=1$ for small $|\alpha_1|/\alpha_2$ *(frontier — verify)*, notably work of Wei, Zhang and Zhou on finite-time singularity formation for LLG in dimension two. Whether the constructions extend to all $\alpha_1/\alpha_2$ is unresolved.
- **Equivariant dynamics beyond $m=1$.** Continuation of Gustafson–Nakanishi–Tsai: classifying the $m=2$ borderline, where $\lambda(t)$ can oscillate eternally, and asking whether $\alpha_1\ne0$ regularizes or destabilizes.
- **Full micromagnetic energy.** Adding anisotropy, Zeeman and stray-field terms (Melcher, Kružík–Prohl school) changes the criticality balance; blow-up under an applied field and skyrmion collapse are studied both analytically and numerically.
- **Numerics.** Structure-preserving (projection / tangent-plane) finite-element schemes are used to probe borderline data; simulations of $m=1$ data with $E$ slightly above $4\pi$ are consistent with concentration for moderate $\alpha_1$ *(frontier — verify)*.

## 8. Future Work

1. Build an approximate self-similar-modulated profile for the rotated operator $(\alpha_2+i\alpha_1)\mathcal{L}$ to sufficient order, transporting Raphaël–Schweyer's tail computation into the complex-coefficient setting.
2. Find a substitute for Struwe's local energy monotonicity valid for $\alpha_1\neq0$ — for example a monotone quantity for the modified Hamiltonian $E + \alpha_1\alpha_2^{-1}\,(\text{helicity-type correction})$.
3. Determine whether blow-up, if it occurs, is stable or of finite codimension, and whether the rate is quantized (heat-flow-like $|\log(T-t)|^{-2}$) or continuous (Schrödinger-like).
4. Settle $d\ge5$ for $\alpha_2>0$, and decide whether the Ding–Wang singularities are Type I or Type II.
5. Prove or disprove uniqueness of energy-class weak LLG solutions in $d=2$ below the first singular time.

## 9. Key References

- **[Foundational]** L. D. Landau, E. M. Lifshitz. *On the theory of the dispersion of magnetic permeability in ferromagnetic bodies.* Phys. Z. Sowjetunion 8 (1935), 153–169.
- **[Foundational]** T. L. Gilbert. *A phenomenological theory of damping in ferromagnetic materials.* IEEE Transactions on Magnetics 40 (2004), 3443–3449.
- **[Foundational]** M. Struwe. *On the evolution of harmonic mappings of Riemannian surfaces.* Commentarii Mathematici Helvetici 60 (1985), 558–581.
- **[Foundational]** K.-C. Chang, W.-Y. Ding, R. Ye. *Finite-time blow-up of the heat flow of harmonic maps from surfaces.* Journal of Differential Geometry 36 (1992), 507–515.
- **[Foundational]** J.-M. Coron, J.-M. Ghidaglia. *Explosion en temps fini pour le flot des applications harmoniques.* C. R. Acad. Sci. Paris Sér. I 308 (1989), 339–344.
- **[Foundational]** F. Alouges, A. Soyeur. *On global weak solutions for Landau–Lifshitz equations: existence and nonuniqueness.* Nonlinear Analysis 18 (1992), 1071–1084.
- **[Foundational]** B. Guo, M.-C. Hong. *The Landau–Lifshitz equation of the ferromagnetic spin chain and harmonic maps.* Calculus of Variations and PDE 1 (1993), 311–334.
- **[SOTA]** S. Ding, C. Wang. *Finite time singularity of the Landau–Lifshitz–Gilbert equation.* International Mathematics Research Notices 2007, rnm012.
- **[SOTA]** S. Gustafson, K. Nakanishi, T.-P. Tsai. *Asymptotic stability, concentration, and oscillation in harmonic map heat-flow, Landau–Lifshitz, and Schrödinger maps on $\mathbb{R}^2$.* Communications in Mathematical Physics 300 (2010), 205–242.
- **[SOTA]** P. Raphaël, R. Schweyer. *Stable blowup dynamics for the 1-corotational energy critical harmonic heat flow.* Communications on Pure and Applied Mathematics 66 (2013), 414–480.
- **[SOTA]** F. Merle, P. Raphaël, I. Rodnianski. *Blowup dynamics for smooth data equivariant solutions to the critical Schrödinger map problem.* Inventiones Mathematicae 193 (2013), 249–365.
- **[SOTA]** G. Perelman. *Blow up dynamics for equivariant critical Schrödinger maps.* Communications in Mathematical Physics 330 (2014), 69–105.
- **[SOTA]** C. Melcher. *Global solvability of the Cauchy problem for the Landau–Lifshitz–Gilbert equation in higher dimensions.* Indiana University Mathematics Journal 61 (2012), 1175–1200.
- **[SOTA]** I. Bejenaru, A. Ionescu, C. Kenig, D. Tataru. *Global Schrödinger maps in dimensions $d\ge2$: small data in the critical Sobolev spaces.* Annals of Mathematics 173 (2011), 1443–1506.
- **[SOTA]** C. Harpes. *Uniqueness and bubbling of the 2-dimensional Landau–Lifshitz flow.* Calculus of Variations and PDE 20 (2004), 213–229.
- **[Survey]** M. Kružík, A. Prohl. *Recent developments in the modeling, analysis, and numerics of ferromagnetism.* SIAM Review 48 (2006), 439–483.
- **[Survey/Book]** B. Guo, S. Ding. *Landau–Lifshitz Equations.* World Scientific, Frontiers of Research with the Chinese Academy of Sciences, 2008.

## 10. Worked Example / Concrete Special Case

**Setting.** $d=2$, $1$-equivariant data, $u_0$ close to the harmonic map $Q(r) = 2\arctan r$, $E(Q)=4\pi$. Write $u(t)\approx Q_{\lambda(t),\gamma(t)}$, the bubble rescaled by $\lambda(t)$ and rotated by $\gamma(t)$ about the $z$-axis.

**Step 1 — the zero mode.** Differentiating $Q(r/\lambda)$ in $\lambda$ at $\lambda=1$ gives $-\Lambda Q$ with
$$\Lambda Q(r) = r\,\partial_r Q = \frac{2r}{1+r^2}.$$
Its $L^2(\mathbb{R}^2)$ norm on $r<R$ is
$$\int_0^R \frac{4r^2}{(1+r^2)^2}\,2\pi r\,dr \;=\; 8\pi\log R + O(1),$$
so $\Lambda Q \notin L^2(\mathbb{R}^2)$: the scaling mode is only logarithmically normalizable. Contrast $m\ge2$, where $\Lambda Q_m = 2m r^m/(1+r^{2m})$ satisfies $\int_0^\infty \frac{4m^2 r^{2m}}{(1+r^{2m})^2}\,r\,dr < \infty$. This single computation explains the $m\ge3$ stability theorem of Gustafson–Nakanishi–Tsai and the log corrections at $m=1$.

**Step 2 — modulation.** Plugging $u \approx Q_{\lambda,\gamma}$ into LLG and projecting onto $\Lambda Q$ gives, at leading order,
$$\Big(\frac{\dot\lambda}{\lambda} + i\dot\gamma\Big)\,\big(8\pi\log(1/\lambda)\big) \;=\; -(\alpha_2 + i\alpha_1)\,\Phi(\lambda),$$
with $\Phi(\lambda)>0$ the energy flux carried by the radiation matched to the bubble at scale $r\sim\sqrt{T-t}$.

**Step 3 — pure heat flow ($\alpha_1=0$).** Matched asymptotics (van den Berg–Hulshof–King) give $\Phi(\lambda)\sim c\,\lambda^{-1}|\log\lambda|^{-1}$ after the outer matching, and the modulation law reduces to
$$\dot\lambda \;\approx\; -\,\frac{c}{|\log\lambda|^{2}} \;\Longrightarrow\; \lambda\,|\log\lambda|^{2} \approx c\,(T-t) \;\Longrightarrow\; \lambda(t)\sim \kappa\,\frac{T-t}{|\log(T-t)|^{2}},$$
which is exactly the stable rate proved by Raphaël–Schweyer. Since $\lambda(T)=0$, $|\nabla u|$ blows up and precisely $4\pi$ of energy concentrates.

**Step 4 — where the general case breaks.** For $\alpha_1\neq 0$, Step 2 gives
$$\frac{\dot\lambda}{\lambda} = -\alpha_2\,\frac{\Phi(\lambda)}{8\pi\log(1/\lambda)},\qquad \dot\gamma = -\alpha_1\,\frac{\Phi(\lambda)}{8\pi\log(1/\lambda)} .$$
Formally $\dot\lambda<0$ still, so concentration is expected. But $\Phi$ now depends on the *rotating* radiation field, which solves a Schrödinger-type equation with damping in the outer region; its sign and magnitude are no longer determined by the energy identity alone. If the rotating tail returns energy to the core at order $\Phi$, the law degenerates and $\lambda$ may stall. Closing this estimate — showing $\Phi(\lambda)\gtrsim \lambda^{-1}|\log\lambda|^{-1}$ uniformly in $\alpha_1/\alpha_2$ — is exactly the open step of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*