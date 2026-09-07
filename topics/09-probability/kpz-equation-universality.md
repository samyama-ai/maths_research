---
id: 09-probability/kpz-equation-universality
title: "KPZ Equation Universality"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# KPZ Equation Universality

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/kpz-equation-universality` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Kardar–Parisi–Zhang (KPZ) universality conjecture asserts that a large class of randomly growing interfaces — driven by local, non-conservative dynamics with a smoothing term, a slope-dependent growth nonlinearity, and rapidly decorrelating noise — share a single scaling limit that depends on almost none of the microscopic details.

Two nested claims:

**(A) Weak universality (KPZ equation as crossover).** For a microscopic growth model with weak asymmetry of strength $\varepsilon^{1/2}$, the rescaled height function
$$h_\varepsilon(t,x) \;=\; \varepsilon^{1/2}\Big( h\big(\varepsilon^{-2}t,\ \varepsilon^{-1}x\big) - C_\varepsilon t \Big)$$
converges in distribution to the Hopf–Cole solution of the one-dimensional KPZ equation, for suitable centering constants $C_\varepsilon$.

**(B) Strong universality (KPZ fixed point).** For the same class *without* tuning the asymmetry to zero, under the $1{:}2{:}3$ scaling
$$\mathfrak{h}_\epsilon(t,x) \;=\; \epsilon^{1/2}\Big( h\big(\epsilon^{-3/2}t,\ \epsilon^{-1}x\big) - c_\infty \epsilon^{-3/2} t \Big),$$
the limit as $\epsilon\to 0$ is the **KPZ fixed point** $\mathfrak{h}(t,x)$, a Markov process on upper semicontinuous functions, independent of the model and of the initial-data class beyond its own scaling limit. In particular fluctuations grow like $t^{1/3}$, correlations decorrelate on scale $t^{2/3}$, and one-point laws are Tracy–Widom GUE (curved/narrow-wedge data), Tracy–Widom GOE (flat data), or Baik–Rains (stationary data).

A complete resolution requires: (i) a model-independent characterization of the KPZ fixed point's domain of attraction, and (ii) proofs of convergence for models outside the integrable (exactly solvable) family — non-determinantal, non-Bethe-solvable dynamics. Both remain open. In dimension $d \ge 2$, even the values of the exponents are conjectural.

## 2. Mathematical Foundations

**The equation.** For $h:\mathbb{R}_+\times\mathbb{R}\to\mathbb{R}$,
$$\partial_t h \;=\; \nu\,\partial_x^2 h \;+\; \tfrac{\lambda}{2}\,(\partial_x h)^2 \;+\; \sqrt{D}\,\xi,$$
with $\xi$ space-time white noise: a centered Gaussian generalized field with $\mathbb{E}[\xi(t,x)\xi(s,y)]=\delta(t-s)\delta(x-y)$. Standard normalization: $\nu=\tfrac12$, $\lambda=D=1$.

**Ill-posedness.** Solutions are locally Brownian in $x$, so $\partial_x h$ is a distribution of regularity $C^{-1/2-}$ and $(\partial_x h)^2$ has no canonical meaning. The equation is *subcritical* in the regularity-structures sense (nonlinearity is a finite-order perturbation), but not classically well-posed.

**Hopf–Cole solution.** Set $Z=\exp(h)$. Formally $Z$ solves the multiplicative stochastic heat equation (SHE)
$$\partial_t Z \;=\; \tfrac12 \partial_x^2 Z \;+\; Z\,\xi ,$$
interpreted in the Itô/Walsh sense. For nonnegative, nonzero initial data, $Z(t,x)>0$ almost surely (Mueller's strong positivity, 1991), so $h := \log Z$ is well defined. This is the reference notion of solution.

**Renormalization.** Mollifying the noise, $\xi_\delta = \xi * \rho_\delta$, the solutions $h_\delta$ of the equation with the counterterm $-C_\delta$, $C_\delta \sim c\,\delta^{-1}$, converge to the Hopf–Cole solution. Regularity structures (Hairer) and paracontrolled distributions (Gubinelli–Imkeller–Perkowski) both produce this limit intrinsically.

**Energy solutions.** For stationary-type data, Gonçalves–Jara define solutions via a martingale problem where the nonlinear term is the $L^2$ limit
$$\mathcal{A}_t(\varphi)=\lim_{\kappa\to0}\int_0^t\!\!\int \big(\partial_x h_\kappa(s,x)\big)^2 \partial_x\varphi(x)\,dx\,ds$$
with an Itô-trick energy estimate; Gubinelli–Perkowski proved uniqueness in this class.

**Invariances.** (i) *Stationarity*: two-sided Brownian motion (plus arbitrary height shift) is invariant. (ii) *Galilean tilt*: $h(t,x)\mapsto h(t,x+\lambda v t)-vx-\tfrac{\lambda}{2}v^2 t$ preserves the law. (iii) *$1{:}2{:}3$ scaling*: $h_\epsilon(t,x)=\epsilon^{1/2}h(\epsilon^{-3/2}t,\epsilon^{-1}x)+\tfrac{t}{2}\epsilon^{-3/2}\cdot(\cdot)$ maps KPZ to KPZ with $\nu\to\epsilon^{1/2}\nu$ — the equation is *not* scale invariant; it is a crossover between the Edwards–Wilkinson fixed point ($\epsilon\to\infty$) and the KPZ fixed point ($\epsilon\to0$).

**Directed landscape.** The space-time scaling limit of last-passage percolation, $\mathcal{L}(x,s;y,t)$, is a random continuous function satisfying the metric composition law
$$\mathcal{L}(x,s;y,t)=\max_{z}\big\{\mathcal{L}(x,s;z,r)+\mathcal{L}(z,r;y,t)\big\},$$
with $\mathcal{L}(x,0;y,1)+ (y-x)^2$ having Airy-sheet marginals. The KPZ fixed point is recovered by $\mathfrak{h}(t,y)=\sup_x\{\mathfrak{h}_0(x)+\mathcal{L}(x,0;y,t)\}$.

## 3. History & State of the Art

- **1986** — Kardar, Parisi, Zhang propose the equation and, via a one-loop dynamic RG plus the fluctuation–dissipation relation in $d=1$, predict $\chi=1/2$, $z=3/2$.
- **1997** — Bertini–Giacomin prove that weakly asymmetric simple exclusion (WASEP) height functions converge to the Hopf–Cole solution: the first rigorous weak-universality theorem.
- **1999–2002** — Baik–Deift–Johansson (longest increasing subsequence) and Johansson (corner growth) establish Tracy–Widom GUE fluctuations with $t^{1/3}$ scale for integrable models; Prähofer–Spohn identify the Airy$_2$ process as the spatial limit of PNG.
- **2009–2011** — Tracy–Widom solve ASEP with step initial data via Bethe ansatz; Amir–Corwin–Quastel (CPAM 2011) and, non-rigorously, Sasamoto–Spohn and Calabrese–Le Doussal–Rosso derive the exact one-point distribution of the narrow-wedge KPZ equation — the "crossover distribution" interpolating Gaussian ($t\to0$) and Tracy–Widom GUE ($t\to\infty$).
- **2013–2014** — Hairer's *Solving the KPZ equation* (Annals) and *A theory of regularity structures* (Invent. Math., Fields Medal 2014) give a pathwise solution theory; Gubinelli–Imkeller–Perkowski give the paracontrolled alternative.
- **2021–2023** — Matetski–Quastel–Remenik construct the KPZ fixed point (Acta Math. 2021); Dauvergne–Ortmann–Virág construct the directed landscape (Acta Math. 2022); Quastel–Sarkar (JAMS 2023) prove convergence of a family of exclusion processes *and* of the KPZ equation itself to the KPZ fixed point; Virág gives an independent route via the heat/landscape correspondence.
- **2023** — Caravenna–Sun–Zygouras construct the *critical 2d stochastic heat flow*, the first nontrivial object in the marginal dimension $d=2$.

## 4. Partial Results / Verified Cases

**Weak universality (A) — proven for:**
- WASEP with asymmetry $\varepsilon^{1/2}$ (Bertini–Giacomin 1997).
- A class of continuous growth models $\partial_t h=\partial_x^2 h + \varepsilon^{1/2}F(\partial_x h)+\xi$ with $F$ polynomial or of suitable growth, for *any* $F$ with nonzero second-order Taylor coefficient (Hairer–Quastel, *Forum Math. Pi* 2018) — the limit is KPZ with an effective $\lambda$ given by a Gaussian average of $F''$.
- Directed polymers in the intermediate-disorder regime $\beta_\varepsilon=\beta\varepsilon^{1/4}$ in $d=1$ (Alberts–Khanin–Quastel, *Ann. Probab.* 2014): partition functions converge to the SHE.
- Stationary/nonequilibrium energy solutions for a broad family of conservative particle systems with a nonlinear flux (Gonçalves–Jara, ARMA 2014; uniqueness: Gubinelli–Perkowski, JAMS 2018) — this covers non-integrable dynamics.

**Strong universality (B) — proven for:**
- TASEP and a one-parameter family of exclusion processes, all initial data (Matetski–Quastel–Remenik 2021; Quastel–Sarkar 2023).
- The KPZ equation itself: $\epsilon^{1/2}h(\epsilon^{-3/2}t,\epsilon^{-1}x)\to \mathfrak{h}$ (Quastel–Sarkar 2023; Virág 2020).
- Exponential and geometric last-passage percolation, the log-gamma and O'Connell–Yor polymers, the six-vertex/stochastic higher-spin family — all via exact formulas.
- One-point Tracy–Widom limits for ASEP (Tracy–Widom 2009), and for the colored ASEP / stochastic six-vertex model (Aggarwal–Corwin–Hegde, 2024) *(frontier — verify)*.

**Dimension.** All of the above is $d=1$. For $d\ge 3$ and small $\beta$, the SHE has a Gaussian (Edwards–Wilkinson) limit (Magnen–Unterberger 2018; Dunlap–Gu–Ryzhik–Zeitouni, CMP 2020) — i.e. KPZ behavior does *not* occur in the weak-disorder phase. In $d=2$ with $\beta_\varepsilon = \hat\beta\sqrt{2\pi/\log \varepsilon^{-1}}$, the critical stochastic heat flow exists and is non-Gaussian (Caravenna–Sun–Zygouras, Invent. Math. 2023).

## 5. Principal Obstacles

- **Integrability is the only known engine for $t^{1/3}$.** Every proof of Tracy–Widom limits routes through a determinantal structure, a Bethe-ansatz eigenfunction expansion, or a Macdonald/Yang–Baxter symmetry. Generic ASEP-like models with, say, three-site interaction or non-nearest-neighbor jumps have none of these; there is no known a-priori estimate giving even $t^{1/3+o(1)}$ upper *and* lower bounds for such models.
- **No comparison/monotonicity principle at the fluctuation scale.** Coupling arguments give hydrodynamic limits ($t^{1}$ order) but do not transfer $1/3$-order information between models.
- **Regularity structures do not scale.** Hairer's theory is *local in the small-scale parameter*: it renormalizes ultraviolet divergences and gives well-posedness, but its estimates degrade as $\epsilon\to 0$ in the $1{:}2{:}3$ scaling, which is a large-scale (infrared) problem. The strong-coupling fixed point is inaccessible to the same machinery.
- **RG is non-perturbative.** The one-loop RG flow for KPZ has no accessible fixed point in $d=1$; in $d\ge2$ the coupling is relevant and the strong-coupling fixed point lies outside any $\epsilon$-expansion. The upper critical dimension of KPZ is itself disputed (numerics say none finite; some mode-coupling arguments say $d_c=4$).
- **Tightness for general initial data.** Even in integrable cases, controlling the height profile as a *process* (not one point) requires Airy line-ensemble Brownian-Gibbs resampling, which again exists only for integrable models.

## 6. The Gap

Proven: convergence to the KPZ equation for models with a *tunable weak asymmetry* and a smoothing/martingale structure; convergence to the KPZ fixed point for models with *exact solvability*.

Missing: a bridge that does not use either tuning or exact formulas. Concretely, the outstanding step is an a-priori tightness estimate of the form
$$c\,t^{1/3} \;\le\; \big\|\,h(t,0)-\mathbb{E}h(t,0)\,\big\|_{L^2} \;\le\; C\,t^{1/3}$$
for a non-integrable asymmetric growth model, together with a *characterization theorem* — a set of properties (Markov, $1{:}2{:}3$ scale invariance, Brownian stationarity for the increment process, the variational/metric composition law) that pins down the KPZ fixed point uniquely. With such a characterization, universality would reduce to verifying soft properties model by model. No such uniqueness theorem is known.

## 7. Current Research (as of June 2026)

- **Characterization programs.** Efforts to axiomatize the directed landscape by its metric composition law plus Airy marginals, extending Aggarwal–Huang-type strong characterizations of the Airy line ensemble via Brownian-Gibbs uniqueness *(frontier — verify)*. Groups: Columbia (Corwin), Toronto (Quastel, Virág, Dauvergne), Berkeley/Chicago.
- **Non-integrable models.** Perturbative stability of TASEP under small non-integrable modifications; renormalization-group-with-rigor approaches (Bonn: Hairer's former group; Paris-Dauphine; Milan). No unconditional $t^{1/3}$ result yet.
- **Higher dimensions.** Structure of the 2d critical stochastic heat flow: moments, multiplicativity, and whether it is the weak-disorder-critical limit of 2d directed polymers uniquely (Caravenna–Sun–Zygouras and collaborators).
- **KPZ with boundaries and on the half-line**, and stationary measures on segments (Barraquand–Le Doussal; Corwin–Knizel, showing the stationary measure of KPZ on $[0,L]$ is a Markov-type "continuous dual Hahn" process).
- **Large deviations.** Tail exponents $\exp(-c s^{3/2})$ (lower) and $\exp(-c s^{3})$ (upper) for the narrow-wedge KPZ equation, and the weak-noise/Freidlin–Wentzell regime (Lin–Tsai; Krajenbrink–Le Doussal).

## 8. Future Work

- Prove a uniqueness theorem for the KPZ fixed point from scaling invariance + Markov property + one-point marginals; this is the strategy most explicitly advocated by Quastel and Remenik.
- Develop coupling or hydrodynamic-plus-fluctuation techniques that transport $t^{1/3}$ bounds from an integrable model to a nearby non-integrable one (an "integrable probability perturbation theory").
- Build a rigorous, non-perturbative RG for the $1{:}2{:}3$ scaling limit — i.e. an infrared counterpart to regularity structures.
- Settle whether a strong-coupling phase and a nontrivial fixed point exist for $d=2,3$ with strong disorder, and whether $d_c<\infty$.
- Extend universality to multi-species/colored systems and to KPZ on general graphs and manifolds.

## 9. Key References

- **[Foundational]** M. Kardar, G. Parisi, Y.-C. Zhang. *Dynamic Scaling of Growing Interfaces.* Physical Review Letters 56 (1986), 889–892.
- **[Foundational]** L. Bertini, G. Giacomin. *Stochastic Burgers and KPZ equations from particle systems.* Communications in Mathematical Physics 183 (1997), 571–607.
- **[Foundational]** M. Hairer. *Solving the KPZ equation.* Annals of Mathematics 178 (2013), 559–664.
- **[Foundational]** M. Hairer. *A theory of regularity structures.* Inventiones Mathematicae 198 (2014), 269–504.
- **[Foundational]** G. Amir, I. Corwin, J. Quastel. *Probability distribution of the free energy of the continuum directed random polymer in 1+1 dimensions.* Communications on Pure and Applied Mathematics 64 (2011), 466–537.
- **[SOTA]** K. Matetski, J. Quastel, D. Remenik. *The KPZ fixed point.* Acta Mathematica 227 (2021), 115–203.
- **[SOTA]** D. Dauvergne, J. Ortmann, B. Virág. *The directed landscape.* Acta Mathematica 229 (2022), 201–285.
- **[SOTA]** J. Quastel, S. Sarkar. *Convergence of exclusion processes and the KPZ equation to the KPZ fixed point.* Journal of the American Mathematical Society 36 (2023), 251–289.
- **[SOTA]** M. Hairer, J. Quastel. *A class of growth models rescaling to KPZ.* Forum of Mathematics, Pi 6 (2018), e3.
- **[SOTA]** M. Gubinelli, N. Perkowski. *Energy solutions of KPZ are unique.* Journal of the American Mathematical Society 31 (2018), 427–471.
- **[SOTA]** F. Caravenna, R. Sun, N. Zygouras. *The critical 2d Stochastic Heat Flow.* Inventiones Mathematicae 233 (2023), 325–460.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications 1 (2012), 1130001.
- **[Survey]** J. Quastel, H. Spohn. *The one-dimensional KPZ equation and its universality class.* Journal of Statistical Physics 160 (2015), 965–984.
- **[Book]** T. Alberts, K. Khanin, J. Quastel. *The intermediate disorder regime for directed polymers in dimension $1+1$.* Annals of Probability 42 (2014), 1212–1256.

## 10. Worked Example / Concrete Special Case

**Deriving $\chi=1/2$, $z=3/2$ from two exact symmetries.**

Postulate a scaling limit with exponents $\chi$ (height) and $z$ (dynamic): $h(t,x)\approx b^{-\chi} h(b^z t, b x)$ in law, so that $\mathrm{Var}\,h(t,0)\sim t^{2\chi/z}$ and correlations decorrelate on $x\sim t^{1/z}$.

*Step 1 — Galilean invariance fixes one relation.* The tilt map $h(t,x)\mapsto h(t,x+\lambda v t)-vx-\tfrac{\lambda}{2}v^2 t$ leaves the law invariant for every $v\in\mathbb{R}$. Under the rescaling $x\to bx,\ t\to b^z t,\ h\to b^{\chi}h$, the slope $v$ transforms as $v\to b^{\chi-1}v$, while consistency of the term $\lambda v t$ with $x$ requires $b^{\chi-1}\cdot b^{z} = b^{1}$, i.e.
$$\chi + z = 2.$$
Equivalently: $\lambda$ must be non-renormalized, which is the standard statement of the KPZ Ward identity.

*Step 2 — Brownian stationarity fixes $\chi$ in $d=1$.* Take $h_0$ a two-sided standard Brownian motion. Funaki–Quastel (2015) proved this measure (modulo height shift) is invariant for the KPZ equation with $\nu=\tfrac12,\lambda=D=1$. Hence for all $t$,
$$\mathrm{Var}\big(h(t,x)-h(t,0)\big)=|x| .$$
So spatial fluctuations grow like $|x|^{1/2}$: $\chi=\tfrac12$. With Step 1, $z=\tfrac32$, and
$$\mathrm{Var}\,h(t,0)\;\sim\; t^{2\chi/z}=t^{2/3},\qquad \text{fluctuation scale } t^{1/3}.$$
Contrast: dropping the nonlinearity gives the Edwards–Wilkinson equation with $\chi=(2-d)/2$, $z=2$, so fluctuations $\sim t^{(2-d)/4}$ — in $d=1$, $t^{1/4}$, not $t^{1/3}$. The $1/4\to1/3$ jump is precisely what universality asserts is model-independent.

*Step 3 — the exact one-point law (narrow wedge).* Let $Z$ solve the SHE with $Z(0,\cdot)=\delta_0$ and $h=\log Z$. Amir–Corwin–Quastel prove that with $t$-scale $\sigma_t = (t/2)^{1/3}$,
$$\Upsilon_t \;:=\; \frac{h(t,0)+\frac{t}{24}+\frac{1}{2}\log(2\pi t)}{\sigma_t}$$
has an explicit Fredholm-determinant distribution, and
$$\Upsilon_t \;\xrightarrow[t\to\infty]{d}\; \mathrm{TW}_{\mathrm{GUE}},\qquad \mathbb{E}[\mathrm{TW}_{\mathrm{GUE}}]\approx -1.7711,\ \ \mathrm{Var}\approx 0.8132 .$$
As $t\to 0$, $\Upsilon_t$ is asymptotically Gaussian. So the KPZ equation is a *crossover*: Edwards–Wilkinson at short time, KPZ fixed point at long time.

**What the example does not give.** Steps 1–2 are exact for the KPZ equation and for a handful of models with explicit Brownian-type stationary measures (TASEP: product Bernoulli; O'Connell–Yor: explicit). For a growth model without an explicit invariant measure, neither the Galilean identity nor $\chi=1/2$ can currently be established — that is exactly the gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*