---
id: 06-pdes/kuramoto-synchronization-threshold
title: "Kuramoto Synchronization Threshold"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kuramoto Synchronization Threshold

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kuramoto-synchronization-threshold` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Kuramoto model describes $N$ phase oscillators with natural frequencies $\omega_i$ drawn from a density $g$, coupled all-to-all with strength $K$. Kuramoto's 1975 self-consistency argument predicts a sharp onset of collective synchronization at

$$K_c \;=\; \frac{2}{\pi g(0)},$$

for even, unimodal $g$, with order parameter $r(K)\sim \sqrt{K-K_c}$ just above threshold. The problem has two open faces.

**(A) Continuum / PDE threshold.** For the mean-field (Kuramoto–Sakaguchi) kinetic equation, prove for *general* frequency densities $g$ — beyond analytic, unimodal, or Lorentzian cases — that the incoherent state $\rho\equiv 1/2\pi$ is nonlinearly asymptotically stable (in a suitable weak topology) for all $K<K_c$, that it is unstable for $K>K_c$, and that a stable branch of partially locked states bifurcates at exactly $K_c$ with the stated scaling. A complete solution must handle non-analytic and merely $L^1$ or measure-valued $g$, bimodal or degenerate $g$ (where $g''(0)=0$ or $g$ has flat/plateau structure), and identify the topology in which the "Landau-damped" decay of the order parameter is genuine rather than an artifact of regularity of the data.

**(B) Finite-graph global synchronization threshold.** Let $G$ be a connected graph on $n$ vertices with minimum degree $\mu n$ and identical frequencies. Determine the critical constant
$$\mu_c \;=\; \inf\{\mu : \text{every graph with } \delta(G)\ge \mu n \text{ is globally synchronizing}\},$$
where *globally synchronizing* means every stable equilibrium of $\dot\theta_i = \sum_{j\sim i}\sin(\theta_j-\theta_i)$ is the fully in-phase state. It is known that $0.6818 \le \mu_c \le 0.75$; pinning $\mu_c$ is open.

## 2. Mathematical Foundations

**Finite system.** For $\theta\in\mathbb{T}^N$,
$$\dot\theta_i \;=\; \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j-\theta_i),\qquad i=1,\dots,N.$$
The complex order parameter is
$$r e^{\mathrm{i}\psi} \;=\; \frac1N\sum_{j=1}^N e^{\mathrm{i}\theta_j},$$
which rewrites the dynamics in mean-field form $\dot\theta_i=\omega_i+Kr\sin(\psi-\theta_i)$.

**Kinetic limit.** As $N\to\infty$ the empirical measure converges (Neunzert/Dobrushin-type stability, made quantitative in Wasserstein distance by Carrillo–Choi–Ha–Kang–Kim) to a solution of the Kuramoto–Sakaguchi equation on $\mathbb{T}\times\mathbb{R}$:
$$\partial_t \rho(\theta,\omega,t) + \partial_\theta\!\big[ v[\rho](\theta,\omega,t)\,\rho \big] \;=\; D\,\partial_\theta^2\rho, \qquad v[\rho] = \omega + K r \sin(\psi-\theta),$$
$$r(t)e^{\mathrm{i}\psi(t)} = \int_{\mathbb{R}}\int_{\mathbb{T}} e^{\mathrm{i}\theta}\rho(\theta,\omega,t)\,d\theta\, g(\omega)\,d\omega .$$
For $D=0$ this is a Vlasov-type transport equation with a nonlocal, order-one force; for $D>0$ it is a nonlinear Fokker–Planck equation with a smoothing term.

**Linearization at incoherence.** Writing $\rho = \frac{1}{2\pi}+\varepsilon\,\eta$, the first Fourier mode $\eta_1(\omega,t)$ obeys
$$\partial_t \eta_1 = -(\mathrm{i}\omega + D)\eta_1 + \frac{K}{2}\int_{\mathbb{R}} \eta_1(\omega',t)\,g(\omega')\,d\omega'.$$
The eigenvalue relation is
$$\frac{K}{2}\int_{\mathbb{R}} \frac{g(\omega)}{\lambda + D + \mathrm{i}\omega}\,d\omega \;=\; 1, \qquad \operatorname{Re}\lambda>0 .$$
Taking $\lambda\to 0^+$ and $D=0$ with the Plemelj formula gives $\frac{K}{2}\big(\pi g(0) - \mathrm{i}\,\mathrm{p.v.}\!\int \tfrac{g(\omega)}{\omega}d\omega\big)=1$; for even $g$ the principal value vanishes and $K_c = 2/(\pi g(0))$.

The essential spectrum of the linearized operator is the imaginary axis (multiplication by $-\mathrm{i}\omega$), so for $K<K_c$ there is **no spectral gap**: decay of $r(t)$ is a phase-mixing (Landau damping) phenomenon, not exponential semigroup decay. Chiba's resolution uses **generalized spectral theory in rigged Hilbert spaces** $X\subset H\subset X'$, where the resolvent of the multiplication operator continues analytically across $\mathrm{i}\mathbb{R}$ as an operator into $X'$, producing *generalized eigenvalues* (resonance poles) that cross into the right half-plane exactly at $K=K_c$.

**Self-consistency for locked states.** A stationary partially locked state has oscillators with $|\omega|\le Kr$ locked at $\theta=\arcsin(\omega/Kr)$ and the rest drifting with density $\propto 1/|\omega - Kr\sin\theta|$; this yields
$$r \;=\; Kr\int_{-\pi/2}^{\pi/2}\cos^2\theta\; g(Kr\sin\theta)\,d\theta .$$

## 3. History & State of the Art (SOTA)

- **1975** — Kuramoto, at the Kyoto international symposium, introduces the model and the self-consistency computation giving $K_c=2/(\pi g(0))$; expanded in his 1984 monograph.
- **1988** — Sakaguchi adds white noise, giving $K_c = 2/\big(\pi \,\tilde g_D(0)\big)$ effects; for Lorentzian $g$ of width $\gamma$, $K_c = 2(D+\gamma)$.
- **1994** — Crawford's centre-manifold/amplitude expansions expose the singular $D\to 0$ limit: the cubic coefficient blows up like $D^{-1}$, so the noiseless bifurcation is *not* a regular normal-form problem.
- **2000** — Strogatz's *Physica D* review frames the stability of incoherence below $K_c$ as an explicit open problem, noting the continuous-spectrum obstruction identified by Strogatz–Mirollo–Matthews (1992), who showed $r(t)$ decays like a Landau-damped mode.
- **2007** — Mirollo–Strogatz compute the spectrum of the partially locked state, showing it also lacks a gap.
- **2008** — Ott–Antonsen find an invariant manifold on which the Lorentzian case reduces to a scalar ODE $\dot r = (\tfrac{K}{2}-\gamma) r - \tfrac{K}{2}r^3$; exact but non-generic.
- **2015–2016** — Chiba proves the Kuramoto bifurcation conjecture (existence, stability and $\sqrt{K-K_c}$ scaling of the branch) for even unimodal analytic-class $g$; Dietert proves nonlinear stability of incoherence below threshold and the bifurcation for $g$ in a Sobolev/Fourier-weighted class; Fernandez–Gérard-Varet–Giacomin prove Landau damping for analytic perturbations.
- **2012–2022** — Graph-theoretic branch: Taylor shows $\mu\ge 0.9395$ suffices; Ling–Xu–Bandeira improve to $0.7929$; Lu–Steinerberger to $0.7889$; Kassabov–Strogatz–Townsend to $0.75$. Townsend–Stillman–Strogatz construct non-synchronizing graphs with $\mu = 0.6818$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| Lorentzian $g$, any $K$ | Exact: $K_c=2\gamma$, $r=\sqrt{1-K_c/K}$; global dynamics reduce to 1 ODE | Kuramoto (1975); Ott–Antonsen (2008) |
| $D>0$ (noise), any $g\in L^1$ | Spectral gap restored; linear and nonlinear stability of incoherence for $K<K_c(D)$; smooth bifurcation | Sakaguchi (1988); Bertini–Giacomin–Pakdaman (2010) |
| $g$ even, unimodal, in Chiba's rigged-space class | Full bifurcation theorem: stable partially locked branch for $0<K-K_c\ll1$, $r\sim c\sqrt{K-K_c}$ | Chiba (2015) |
| $g$ with $\hat g$ decaying, Sobolev-type class | Nonlinear asymptotic stability of incoherence for all $K<K_c$; order parameter $\to 0$ | Dietert (2016) |
| Analytic perturbations, analytic $g$ | Landau damping with exponential decay rate | Fernandez–Gérard-Varet–Giacomin (2016) |
| Identical frequencies, complete graph, $N$ finite | Global synchronization from all but a measure-zero set | Watanabe–Strogatz; Benedetto–Caglioti–Montemagno (2015) |
| $\mathrm{supp}\,g$ compact of width $W$, finite $N$ | Complete phase-locking for $K > CW$ with explicit $C$ | Chopra–Spong (2009); Ha–Kim–Ryoo (2016) |
| Graph, $\delta(G)\ge 0.75\,n$ | Globally synchronizing | Kassabov–Strogatz–Townsend (2021) |
| Erdős–Rényi $G(n,p)$, $p \gg n^{-1/3}$ (roughly) | Globally synchronizing w.h.p. | Kassabov–Strogatz–Townsend (2022) |
| $\delta(G) = 0.6818\,n$ | Counterexample: stable twisted state exists | Townsend–Stillman–Strogatz (2020) |

## 5. Principal Obstacles

- **No spectral gap.** The linearized operator at incoherence is $-\mathrm{i}\omega\,\cdot$ plus a rank-one perturbation; its essential spectrum fills $\mathrm{i}\mathbb{R}$. Standard semigroup/centre-manifold reduction, which needs a gap between critical and stable spectrum, does not apply. The decay of $r(t)$ comes from destructive interference of a continuum of neutral modes.
- **Regularity is consumed by phase mixing.** As in Vlasov–Landau damping, the perturbation $\eta(\theta,\omega,t)$ develops oscillations in $\omega$ of frequency $\sim t$; only weak moments decay. Nonlinear closure therefore requires either analyticity (Mouhot–Villani-style echo control) or a Fourier-weight norm — leaving $g$ merely continuous or $L^1$ out of reach.
- **Singular bifurcation as $D\to0$.** Crawford's expansion coefficients diverge like $1/D$, so the vanishing-noise limit is not uniform; the noiseless branch cannot be obtained by continuation from the parabolic problem.
- **Non-unimodal $g$.** For bimodal $g$ the eigenvalue relation admits a pair of complex roots crossing simultaneously; the onset can be a Hopf/standing-wave bifurcation, and no rigged-space analysis covers the codimension-two organizing centre.
- **Graph case: nonconvex landscape.** Ruling out stable non-in-phase equilibria means excluding all spurious local minima of $-\sum_{i\sim j}\cos(\theta_i-\theta_j)$. Current proofs use spectral/Grothendieck-type relaxations of the Hessian condition, which are lossy: the relaxation is provably not tight below $\mu\approx 0.75$, while explicit counterexamples stop at $0.6818$.

## 6. The Gap

Three precise gaps separate what is proven from the general statement.

1. **Regularity gap (PDE).** Proven: nonlinear stability below $K_c$ for $g$ and data in analytic or Fourier-weighted Sobolev classes. Wanted: the same for $g\in L^1$, or data that is a general probability measure. The missing step is a nonlinear Landau-damping estimate that does not require exponentially decaying Fourier weights to control the plasma-echo cascade.
2. **Shape gap.** Proven: even, unimodal $g$. Wanted: degenerate ($g''(0)=0$, plateau) and multimodal $g$, where the bifurcation may be transcritical, subcritical, or oscillatory rather than the supercritical pitchfork with $r\sim\sqrt{K-K_c}$.
3. **Constant gap (graphs).** $\mu_c \in [0.6818,\,0.75]$. Closing it requires either a graph construction with a stable twisted state above density $0.6818n$, or a Hessian-positivity argument that beats the current spectral relaxation.

## 7. Current Research (as of June 2026)

- **Rigged-space / generalized spectral programs** (Chiba and collaborators, Kyushu; Dietert, Imperial College London) extending resonance-pole methods to bimodal and noise-perturbed $g$, and to Kuramoto–Sakaguchi with phase lag $\alpha$.
- **Kinetic-theory school** (Giacomin, Gérard-Varet, Fernandez, Paris; Carrillo, Oxford; Ha, Seoul National University) pushing Landau-damping techniques toward Gevrey and finite-regularity classes, importing tools from the Vlasov–Poisson damping literature.
- **Optimization / random-graph school** (Strogatz, Townsend, Kassabov at Cornell; Bandeira and Abdalla at ETH Zürich) using expansion and Grothendieck-type certificates; expander-based global synchronization results are the most active line. *(frontier — verify)* Refinements pushing the sufficient density below $0.75n$ under added spectral hypotheses circulate as preprints but are not yet consolidated.
- **Higher-order and network-coupled variants** (simplicial Kuramoto, adaptive coupling) where the threshold can become explosive/first-order; rigorous PDE treatment is nascent. *(frontier — verify)*

## 8. Future Work

- Prove Landau damping for the Kuramoto equation in finite Sobolev regularity, exploiting the fact that the interaction kernel is a single Fourier mode (much weaker than the Coulomb kernel) — widely viewed as the most tractable next step.
- Classify onset for bimodal $g$: establish rigorously the coexistence of standing-wave and locked branches at the codimension-two point.
- Obtain a uniform-in-$D$ bifurcation theory bridging Sakaguchi's noisy threshold and Chiba's noiseless one.
- Settle $\mu_c$; a natural conjecture from numerics is that the true value is near the counterexample bound $0.6818$ rather than $0.75$.
- Quantify $N^{-1/2}$ fluctuation corrections to $K_c$ for finite $N$ and reconcile with the finite-size scaling exponents observed numerically.

## 9. Key References

- **[Foundational]** Y. Kuramoto. *Self-entrainment of a population of coupled non-linear oscillators.* In: International Symposium on Mathematical Problems in Theoretical Physics, Lecture Notes in Physics 39, Springer, 1975, pp. 420–422.
- **[Foundational]** Y. Kuramoto. *Chemical Oscillations, Waves, and Turbulence.* Springer, 1984.
- **[Survey]** S. H. Strogatz. *From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators.* Physica D 143 (2000), 1–20.
- **[Foundational]** J. D. Crawford. *Amplitude expansions for instabilities in populations of globally-coupled oscillators.* Journal of Statistical Physics 74 (1994), 1047–1084.
- **[Foundational]** H. Sakaguchi. *Cooperative phenomena in coupled oscillator systems under external fields.* Progress of Theoretical Physics 79 (1988), 39–46.
- **[SOTA]** H. Chiba. *A proof of the Kuramoto conjecture for a bifurcation structure of the infinite-dimensional Kuramoto model.* Ergodic Theory and Dynamical Systems 35 (2015), 762–834.
- **[SOTA]** H. Dietert. *Stability and bifurcation for the Kuramoto model.* Journal de Mathématiques Pures et Appliquées 105 (2016), 451–489.
- **[SOTA]** B. Fernandez, D. Gérard-Varet, G. Giacomin. *Landau damping in the Kuramoto model.* Annales Henri Poincaré 17 (2016), 1793–1823.
- **[Survey]** H. Dietert, B. Fernandez. *The mathematics of asymptotic stability in the Kuramoto model.* Proceedings of the Royal Society A 474 (2018), 20180467.
- **[Foundational]** R. E. Mirollo, S. H. Strogatz. *The spectrum of the partially locked state for the Kuramoto model.* Journal of Nonlinear Science 17 (2007), 309–347.
- **[Foundational]** E. Ott, T. M. Antonsen. *Low dimensional behavior of large systems of globally coupled oscillators.* Chaos 18 (2008), 037113.
- **[Survey]** F. Dörfler, F. Bullo. *Synchronization in complex networks of phase oscillators: A survey.* Automatica 50 (2014), 1539–1564.
- **[SOTA]** J. A. Carrillo, Y.-P. Choi, S.-Y. Ha, M.-J. Kang, Y. Kim. *Contractivity of transport distances for the kinetic Kuramoto equation.* Journal of Statistical Physics 156 (2014), 395–415.
- **[SOTA]** S. Ling, R. Xu, A. S. Bandeira. *On the landscape of synchronization networks: a perspective from nonconvex optimization.* SIAM Journal on Optimization 29 (2019), 1879–1907.
- **[SOTA]** J. Lu, S. Steinerberger. *Synchronization of Kuramoto oscillators in dense networks.* Nonlinearity 33 (2020), 5905–5918.
- **[SOTA]** M. Kassabov, S. H. Strogatz, A. Townsend. *Sufficiently dense Kuramoto networks are globally synchronizing.* Chaos 31 (2021), 073135.
- **[SOTA]** A. Townsend, M. Stillman, S. H. Strogatz. *Dense networks that do not synchronize and sparse ones that do.* Chaos 30 (2020), 083142.
- **[SOTA]** M. Kassabov, S. H. Strogatz, A. Townsend. *A global synchronization theorem for oscillators on a random graph.* Chaos 32 (2022), 093119.
- **[SOTA]** L. Bertini, G. Giacomin, K. Pakdaman. *Dynamical aspects of mean field plane rotators and the Kuramoto model.* Journal of Statistical Physics 138 (2010), 270–290.

## 10. Worked Example / Concrete Special Case

**Lorentzian frequencies, $D=0$.** Take
$$g(\omega) = \frac{\gamma}{\pi(\omega^2+\gamma^2)},\qquad g(0)=\frac{1}{\pi\gamma}.$$

*Step 1 — linear threshold.* The eigenvalue relation with $D=0$ is $\frac{K}{2}\int_{\mathbb{R}}\frac{g(\omega)}{\lambda+\mathrm{i}\omega}d\omega=1$. Closing the contour in the lower half $\omega$-plane picks up the pole $\omega=-\mathrm{i}\gamma$, giving $\int \frac{g}{\lambda+\mathrm{i}\omega}d\omega = \frac{1}{\lambda+\gamma}$ for $\operatorname{Re}\lambda>0$. Hence
$$\frac{K}{2(\lambda+\gamma)}=1 \;\Longrightarrow\; \lambda = \frac{K}{2}-\gamma .$$
So incoherence is linearly unstable iff $K>2\gamma$, i.e.
$$K_c = 2\gamma = \frac{2}{\pi g(0)},$$
matching Kuramoto's formula.

*Step 2 — branch of locked states.* Insert $g$ into the self-consistency equation with $x=Kr$:
$$1 = K\int_{-\pi/2}^{\pi/2}\cos^2\theta \cdot \frac{\gamma}{\pi\,(x^2\sin^2\theta+\gamma^2)}\,d\theta .$$
Writing $\cos^2\theta = 1-\sin^2\theta$ and using $\int_{-\pi/2}^{\pi/2}\frac{d\theta}{x^2\sin^2\theta+\gamma^2} = \frac{\pi}{\gamma\sqrt{x^2+\gamma^2}}$, one obtains after evaluation
$$1 = \frac{K}{\gamma+\sqrt{x^2+\gamma^2}} \quad\Longrightarrow\quad \sqrt{K^2r^2+\gamma^2} = K-\gamma .$$
Squaring: $K^2r^2 = K^2-2K\gamma$, so
$$\boxed{\,r = \sqrt{1-\frac{2\gamma}{K}} = \sqrt{1-\frac{K_c}{K}}\,},\qquad K>K_c,$$
and near onset $r \simeq \frac{1}{\sqrt{2}\,\gamma^{1/2}}\sqrt{K-K_c}\cdot\frac{1}{\sqrt{2}}$, i.e. $r=O(\sqrt{K-K_c})$ — the predicted square-root pitchfork.

*Step 3 — where the difficulty hides.* For $K<K_c$ the formula $\lambda=\frac{K}{2}-\gamma$ has $\operatorname{Re}\lambda<0$, yet $\lambda$ is *not* an eigenvalue of the linearized operator: it lies outside the spectrum, which is exactly $\mathrm{i}\mathbb{R}$. It is a **resonance pole** obtained by analytic continuation of $\int g/(\lambda+\mathrm{i}\omega)\,d\omega$ across the imaginary axis — possible here only because the Lorentzian extends analytically. The observable $r(t)$ decays like $e^{(K/2-\gamma)t}$ while $\|\eta(t)\|_{L^2}$ does not decay at all. Replace the Lorentzian by a compactly supported $C^\infty$ bump and the continuation may fail to exist; recovering decay of $r(t)$ then demands the nonlinear phase-mixing machinery of Sections 5–6. That substitution is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*