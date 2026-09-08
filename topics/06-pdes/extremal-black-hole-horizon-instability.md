---
id: 06-pdes/extremal-black-hole-horizon-instability
title: "Sharp Decay Rates for Nonlinear Wave Equations on Extremal Black Hole Backgrounds"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sharp Decay Rates for Nonlinear Wave Equations on Extremal Black Hole Backgrounds

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/extremal-black-hole-horizon-instability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(\mathcal{M}, g)$ be an extremal black hole exterior — extremal Reissner–Nordström ($|Q| = M$) or extremal Kerr ($|a| = M$) — and let $\psi$ solve a nonlinear wave equation
$$\Box_g \psi = N(\psi, \partial\psi), \qquad N = O(|\psi|^2 + |\partial\psi|^2),$$
with smooth, suitably small data on a spacelike-null hypersurface crossing the future event horizon $\mathcal{H}^+$.

**The problem.** Determine the *sharp* late-time asymptotics of $\psi$ and of its transversal derivatives $\partial_r^k\psi$ along $\mathcal{H}^+$, in the exterior $r > M$, and along null infinity $\mathcal{I}^+$; and decide whether the **Aretakis instability** — the linear phenomenon that $\partial_r^2\psi|_{\mathcal{H}^+}$ grows linearly in advanced time $v$ while $\psi$ itself decays only like $v^{-1}$ — survives the nonlinearity, is amplified into finite-time blow-up, or is suppressed.

A complete resolution requires: (i) a proof of global existence (or a sharp blow-up criterion) for a nondegenerate class of nonlinearities; (ii) two-sided asymptotics $\psi|_{\mathcal{H}^+} = c\, v^{-p}(1+o(1))$ with $c$ determined explicitly by the data; (iii) the analogous statement for the coupled Einstein equations, where "$\psi$" is a gravitational perturbation. Items (i)–(ii) are open for essentially all genuinely nonlinear $N$; the linear case ($N \equiv 0$) is largely settled and is described in §4.

## 2. Mathematical Foundations

**Extremal Reissner–Nordström.** In ingoing Eddington–Finkelstein coordinates $(v, r, \theta, \varphi)$,
$$g = -D(r)\,dv^2 + 2\,dv\,dr + r^2 \gamma_{S^2}, \qquad D(r) = \left(1 - \frac{M}{r}\right)^{2}.$$
The horizon is $\mathcal{H}^+ = \{r = M\}$. Extremality means $D$ has a **double** root: the surface gravity
$$\kappa = \tfrac{1}{2} D'(r_+) = 0,$$
so $\mathcal{H}^+$ is a degenerate Killing horizon and the *red-shift effect* — the exponential damping mechanism $\int_{\mathcal H^+} \kappa |\partial_r\psi|^2$ that drives all subextremal decay proofs — vanishes identically.

**Wave operator and decomposition.** With $\phi = r\psi$ and spherical harmonic projection $\psi = \sum_{\ell,m}\psi_{\ell m}(v,r)Y_{\ell m}$, the equation $\Box_g\psi = 0$ becomes, in double-null coordinates $(u,v)$ with $r_* = \int D^{-1}dr$,
$$\partial_u\partial_v \phi_\ell + D(r)\left(\frac{\ell(\ell+1)}{r^2} + \frac{D'(r)}{r}\right)\phi_\ell = 0.$$

**Aretakis conservation law.** For $\ell = 0$, restricting $\Box_g\psi = 0$ to $r=M$ gives $\partial_v\big(\partial_r(r\psi)|_{\mathcal{H}^+}\big) = 0$, so
$$H_0[\psi] \;:=\; \big(\partial_r\psi + \tfrac{1}{M}\psi\big)\Big|_{\mathcal{H}^+}$$
is **conserved along every generator** of $\mathcal{H}^+$. For each $\ell$ there is a conserved $H_\ell[\psi]$ built from $\partial_r^{\ell+1}(r\psi)|_{\mathcal{H}^+}$ (Aretakis 2011, 2012). Conservation is incompatible with decay of the nondegenerate energy, and forces
$$\partial_r^{\,\ell+2}\psi\big|_{\mathcal{H}^+}(v) \sim c_\ell\, H_\ell[\psi]\, v \quad (v\to\infty), \qquad \partial_r^{\,\ell+k}\psi \sim v^{k-1}.$$

**Newman–Penrose constant.** Along $\mathcal{I}^+$ the analogous quantity is $I_0[\psi] = \lim_{r\to\infty} r^2\partial_v(r\psi)$, conserved for $\ell=0$ on any asymptotically flat background. On extremal Reissner–Nordström, $H_0$ and $I_0$ are linked by an exact "horizon hair" relation (Angelopoulos–Aretakis–Gajic 2018): $H_0$ is measurable from the $u^{-2}$ coefficient of the radiation field at $\mathcal I^+$.

**Nonlinear setting.** For $\Box_g\psi = N$, the horizon computation gives instead
$$\partial_v H_0[\psi](v) = -\,\big(r\,N\big)\big|_{\mathcal{H}^+}(v),$$
so $H_0$ is only *almost* conserved. The whole problem is whether the source term is integrable in $v$ (instability persists with a shifted constant), non-integrable (amplification, possible blow-up), or sign-definite and damping.

## 3. History & State of the Art (SOTA)

- **1990s–2009.** Price's law heuristics and rigorous subextremal decay: Dafermos–Rodnianski establish the red-shift vector field and the $r^p$-hierarchy, giving $|\psi| \lesssim \tau^{-1}$ then $\tau^{-3/2}$ uniformly up to and including $\mathcal{H}^+$ for Schwarzschild and subextremal Reissner–Nordström and slowly rotating Kerr.
- **2011–2012.** Aretakis discovers the conservation law and the instability, first for extremal Reissner–Nordström (*Comm. Math. Phys.* 2011; *Ann. Henri Poincaré* 2011), then for extremal Kerr (2012, published 2015). This is the first proof that a stationary black hole exterior is *unstable* in a nondegenerate norm.
- **2012–2013.** Lucietti–Reall show the same mechanism for gravitational (Teukolsky $s=-2$) perturbations of extremal Kerr; Bizoń–Friedrich give closed-form $\ell=0$ solutions on extremal Reissner–Nordström confirming $v^{-1}$ horizon decay; Murata–Reall–Tanahashi perform the first fully nonlinear numerical evolution (Einstein–Maxwell–scalar).
- **2016.** Casals–Gralla–Zimmerman compute the extremal-Kerr transient growth and its observational signature.
- **2018–2021.** Angelopoulos–Aretakis–Gajic obtain **sharp** late-time asymptotics for the *linear* wave equation on extremal Reissner–Nordström — the SOTA benchmark that the nonlinear problem must reproduce.
- **2022–2024.** Apetroaie proves the instability for the coupled linearised Einstein–Maxwell system on extremal Reissner–Nordström; Kehle–Unger construct extremal black holes by gravitational collapse, disproving the third law of black hole thermodynamics and making extremal dynamics physically reachable.

## 4. Partial Results / Verified Cases

**Linear, extremal Reissner–Nordström, $\ell = 0$ (solved).** For generic compactly supported data ($H_0 \neq 0$), Angelopoulos–Aretakis–Gajic prove two-sided asymptotics:
$$\psi\big|_{\mathcal{H}^+} = 2H_0\, v^{-1} + O(v^{-2}\log v), \qquad \psi(\tau, r) = c(r)\,\tau^{-2}(1+o(1))\ \ (r>M), \qquad r\psi\big|_{\mathcal{I}^+} \sim c'\,u^{-1},$$
with $c, c'$ proportional to $H_0$. Compare subextremal Reissner–Nordström, where the same data give $\tau^{-3}$ interior and $u^{-2}$ at $\mathcal{I}^+$: **extremality costs exactly one power of $\tau$.** In the non-generic case $H_0 = 0$ the rates improve to $v^{-2}$, $\tau^{-3}$.

**Linear, all $\ell$.** Instability $|\partial_r^{\ell+2}\psi|\to\infty$ linearly in $v$ holds for every $\ell\ge0$ on extremal Reissner–Nordström (Aretakis 2011–2012); sharp asymptotics for $\ell \ge 1$ are known in the axisymmetric/spherically-reduced settings.

**Extremal Kerr, $|a|=M$.** Aretakis constants exist for axisymmetric solutions ($m=0$ modes); the instability is proven there. Casals–Gralla–Zimmerman extend to $m\neq0$ Teukolsky modes with spin $s$: transversal derivatives grow like $v^{-\frac12 + |s|}$-type rates off-axis. Full nonaxisymmetric decay on extremal Kerr remains open.

**Gravitational/electromagnetic perturbations.** Apetroaie (2022–2023) proves that gauge-invariant quantities of the linearised Einstein–Maxwell system on extremal Reissner–Nordström obey conservation laws on $\mathcal{H}^+$ and hence exhibit the Aretakis instability for all $\ell\ge 2$.

**Interior.** Gajic (2017) proves linear waves extend continuously with $H^1_{loc}$ regularity past the Cauchy horizon of extremal Reissner–Nordström — strictly better than subextremal — and Gajic–Luk (2019) show $C^2$ extendibility, in contrast with subextremal blue-shift instability.

**Nonlinear.** Only: (a) Aretakis (2013) shows that for $\Box_g\psi = c\,(\partial_v\psi)^2$-type nonlinearities the conservation law degenerates into a Riccati ODE along $\mathcal{H}^+$, giving finite-time blow-up of $\partial_r^2\psi$ for a class of data; (b) Murata–Reall–Tanahashi (2013) numerically evolve the full Einstein–Maxwell–scalar system: the instability persists on the horizon when the black hole stays extremal, but generic infalling matter drives it subextremal, after which the growth shuts off exponentially.

## 5. Principal Obstacles

- **No red-shift.** Every quantitative decay proof for subextremal horizons uses Dafermos–Rodnianski's red-shift vector field $N$ with $\mathcal{K}^N \gtrsim \kappa\, |\partial\psi|^2$ on $\mathcal{H}^+$. At $\kappa = 0$ this bulk term vanishes and no nondegenerate energy is controlled; the degenerate energy alone does not close a Morawetz/$r^p$ hierarchy up to the horizon.
- **Trapping meets the horizon.** As $|a|\to M$ or $|Q|\to M$, the photon sphere merges with $\mathcal{H}^+$. Trapped null geodesics with $r=M$ force an unavoidable derivative loss in any integrated local energy decay estimate *at the horizon itself*, where one also needs boundedness.
- **The conservation law is an obstruction, not a technicality.** $H_0[\psi] \neq 0$ is stable under perturbation of data, so no choice of norm removes it; any sharp result must be an asymptotic *identity*, not an inequality.
- **Nonlinear transport along $\mathcal{H}^+$ is critical.** The source $\partial_v H_0 = -(rN)|_{\mathcal{H}^+}$ decays like $v^{-2}$ for quadratic $N$ (since $\psi\sim v^{-1}$) — borderline integrable. Constants and signs of the nonlinearity therefore decide the outcome, so soft, structure-blind arguments cannot work; null conditions on Minkowski have no known extremal analogue.
- **Coupling to the geometry.** In Einstein evolution the extremality condition $|Q|=M$ is not preserved by generic perturbation: the problem is a free-boundary one, where the horizon may leave the extremal class dynamically.

## 6. The Gap

Proven: sharp two-sided asymptotics for $\Box_g\psi = 0$ on a *fixed* extremal Reissner–Nordström background, plus linear instability for extremal Kerr and for linearised Einstein–Maxwell.

Required: the same for $N \not\equiv 0$. The precise missing step is a **stable, sharp analysis of the horizon transport equation coupled to exterior decay**: one needs $\psi|_{\mathcal H^+}(v) = 2H_\infty v^{-1}(1+o(1))$ with $H_\infty = H_0 + \int_0^\infty (rN)\,dv$ shown to converge, together with a matching argument controlling $N$ in terms of the very asymptotics being derived. Because the source sits exactly at the $v^{-2}$ integrability threshold, the bootstrap is critical: no current method converts the linear $v^{-1}$ rate into a self-improving nonlinear estimate without an extra logarithmic loss, and no method rules out that the loss is real.

## 7. Current Research (as of June 2026)

- **Princeton / Cambridge / Imperial school** (Aretakis, Dafermos, Gajic, Angelopoulos, Apetroaie): pushing sharp asymptotics from linear to semilinear models, and to nonaxisymmetric extremal Kerr. *(frontier — verify)* Extensions of the $H_0$-machinery to quasilinear scalar models are circulating in preprint form.
- **Extremal formation.** Kehle–Unger's construction of exactly extremal black holes from regular collapse (and their "extremal black hole formation as a critical phenomenon", 2024) makes the extremal dynamics a genuine endpoint problem rather than a measure-zero curiosity. Current work asks whether the Aretakis hair is *created* by the collapse.
- **Interior/strong cosmic censorship.** Van de Moortel, Gajic–Luk: charged scalar fields and near-extremal interiors; the extremal Cauchy horizon's improved regularity is a candidate counterexample regime for $C^2$-formulations of strong cosmic censorship.
- **Numerics.** Spectral and characteristic codes (Reall's group; Casals and collaborators) probing whether the linear-in-$v$ growth of $\partial_r^2\psi$ becomes superlinear or blows up under self-gravitation. *(frontier — verify)*
- **Holography.** Extremal near-horizon $AdS_2$ throats and the connection of $H_\ell$ to conserved charges of the $AdS_2$ conformal symmetry.

## 8. Future Work

1. Prove or disprove global existence for $\Box_g\psi = (\partial_v\psi)^2$ on extremal Reissner–Nordström for all small data, identifying the sharp smallness threshold.
2. Establish a *nonlinear Aretakis constant*: a modified, renormalised $H_0$ that is exactly conserved (or monotone) for a structured nonlinearity — an extremal analogue of the null condition.
3. Extend AAG asymptotics to nonaxisymmetric extremal Kerr, where no conservation law is known for $m \neq 0$.
4. Settle the full nonlinear stability/instability of extremal Reissner–Nordström as a solution of the Einstein–Maxwell system, in the spirit of the Dafermos–Holzegel–Rodnianski–Taylor Schwarzschild proof.
5. Determine the observational signature: convert $\psi|_{\mathcal H^+}\sim 2H_0v^{-1}$ into a statement about the ringdown tail at $\mathcal I^+$ for near-extremal astrophysical black holes.

## 9. Key References

- **[Foundational]** S. Aretakis. *Stability and Instability of Extreme Reissner–Nordström Black Hole Spacetimes for Linear Scalar Perturbations I.* Communications in Mathematical Physics 307 (2011), 17–63.
- **[Foundational]** S. Aretakis. *Stability and Instability of Extreme Reissner–Nordström Black Hole Spacetimes for Linear Scalar Perturbations II.* Annales Henri Poincaré 12 (2011), 1491–1538.
- **[Foundational]** S. Aretakis. *Horizon Instability of Extremal Black Holes.* Advances in Theoretical and Mathematical Physics 19 (2015), 507–530.
- **[Foundational]** M. Dafermos, I. Rodnianski. *Lectures on Black Holes and Linear Waves.* Clay Mathematics Proceedings, vol. 17, AMS, 2013.
- **[SOTA / Recent]** Y. Angelopoulos, S. Aretakis, D. Gajic. *Late-time asymptotics for the wave equation on extremal Reissner–Nordström backgrounds.* Advances in Mathematics 375 (2020), 107363.
- **[SOTA / Recent]** Y. Angelopoulos, S. Aretakis, D. Gajic. *Horizon hair of extremal black holes and measurements at null infinity.* Physical Review Letters 121 (2018), 131102.
- **[SOTA / Recent]** M. A. Apetroaie. *Instability of gravitational and electromagnetic perturbations of extremal Reissner–Nordström spacetime.* Annals of PDE 10 (2024), article 6.
- **[SOTA / Recent]** C. Kehle, R. Unger. *Gravitational collapse to extremal black holes and the third law of black hole thermodynamics.* Journal of the European Mathematical Society, 2024 (arXiv:2211.15742).
- **[SOTA / Recent]** D. Gajic, J. Luk. *The interior of extremal black holes with initially regular Cauchy data.* Analysis & PDE 12 (2019), 1445–1497.
- **[Related]** J. Lucietti, H. S. Reall. *Gravitational instability of an extreme Kerr black hole.* Physical Review D 86 (2012), 104030.
- **[Related]** K. Murata, H. S. Reall, N. Tanahashi. *What happens at the horizon(s) of an extreme black hole?* Classical and Quantum Gravity 30 (2013), 235007.
- **[Related]** P. Bizoń, H. Friedrich. *A remark about wave equations on the extreme Reissner–Nordström black hole.* Classical and Quantum Gravity 30 (2013), 065001.
- **[Related]** M. Casals, S. E. Gralla, P. Zimmerman. *Horizon instability of extremal Kerr.* Physical Review D 94 (2016), 064003.
- **[Survey]** S. Aretakis. *Dynamics of Extremal Black Holes.* SpringerBriefs in Mathematical Physics, vol. 33, Springer, 2018.

## 10. Worked Example / Concrete Special Case

**Setup.** Take extremal Reissner–Nordström with $M = 1$, so $D(r) = (1-1/r)^2$ and $\mathcal{H}^+=\{r=1\}$. Consider spherically symmetric $\psi = \psi(v,r)$ and set $\phi = r\psi$. The wave equation $\Box_g\psi=0$ in $(v,r)$ coordinates reads
$$2\,\partial_v\partial_r \phi + \partial_r\!\big(D(r)\,\partial_r\phi\big) - \frac{D'(r)}{r}\,\phi = 0 .$$

**Step 1 — the conservation law.** Evaluate at $r=1$. Since $D(1)=0$ and $D'(1)=0$, the last two terms drop, leaving
$$\partial_v\big(\partial_r\phi\big)\big|_{r=1} = 0 \quad\Longrightarrow\quad H_0 := \partial_r\phi|_{\mathcal H^+} = \big(\psi + \partial_r\psi\big)|_{r=1}\ \text{ is constant in } v.$$
For data $\psi|_{v=0} = \varepsilon\,\chi(r)$ with $\chi$ a bump supported in $[1, 2]$ and $\chi(1)=1,\ \chi'(1)=0$, we get $H_0 = \varepsilon \neq 0$: **the instability is generic**, not tuned.

**Step 2 — linear growth of the second derivative.** Differentiate the equation once in $r$ and restrict to $r=1$, using $D''(1) = 2$:
$$2\,\partial_v\partial_r^2\phi\big|_{r=1} + D''(1)\,\partial_r\phi\big|_{r=1} - \big(D''(1)\big)\phi\big|_{r=1}\cdot 0 = 0 \;\Longrightarrow\; \partial_v \partial_r^2\phi\big|_{\mathcal H^+} = -H_0 .$$
Integrating: $\partial_r^2\phi|_{\mathcal H^+}(v) = \partial_r^2\phi|_{v=0} - H_0\,v$. With $H_0 = \varepsilon$ this is unbounded growth at rate $\varepsilon$ per unit advanced time, even though $\psi$ itself is bounded and in fact decays like $2H_0 v^{-1}$ (AAG). Higher derivatives inherit $\partial_r^{2+k}\phi \sim v^{1+k}$.

**Step 3 — what the nonlinearity does.** Now take $\Box_g\psi = \lambda(\partial_v\psi)^2$. Step 1 becomes
$$\partial_v H_0(v) = -\lambda\, r\,(\partial_v\psi)^2\big|_{r=1} = -\lambda\,\big(\partial_v\phi|_{\mathcal H^+}\big)^2 .$$
If the linear rate $\psi|_{\mathcal H^+}\sim 2H_0 v^{-1}$ persists, then $\partial_v\phi|_{\mathcal H^+}\sim -2H_0 v^{-2}$ and
$$\partial_v H_0 \sim -4\lambda H_0^2\, v^{-4},$$
which **is** integrable, giving a finite limit $H_\infty = H_0 - \tfrac{4}{3}\lambda H_0^2 v_0^{-3}+\dots$ — the instability survives with a shifted constant. Replace the nonlinearity by $\lambda(\partial_r\psi)^2$, however, and the transversal derivative enters: $\partial_r\psi|_{\mathcal H^+}\to H_0 \neq 0$, so $\partial_v H_0 \sim -\lambda H_0^2$, a **Riccati equation** whose solution $H_0(v) = H_0(0)/(1+\lambda H_0(0)v)$ either decays to zero or blows up in finite $v$ depending on $\operatorname{sign}(\lambda H_0(0))$.

This one-line dichotomy is the entire difficulty in miniature: the answer depends on *which* derivative the nonlinearity sees at the degenerate horizon, and no soft argument fixes that. Making the heuristic rigorous — controlling the error terms in the exterior well enough to justify substituting the linear asymptotics into the horizon transport equation — is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*