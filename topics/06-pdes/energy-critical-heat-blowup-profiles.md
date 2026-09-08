---
id: 06-pdes/energy-critical-heat-blowup-profiles
title: "Uniqueness of Blow-up Profiles for the Energy-Critical Heat Equation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Uniqueness of Blow-up Profiles for the Energy-Critical Heat Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/energy-critical-heat-blowup-profiles` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the energy-critical semilinear heat equation (critical Fujita equation) on $\mathbb{R}^n$, $n \ge 3$:

$$\partial_t u = \Delta u + |u|^{p-1}u, \qquad p = p_S := \frac{n+2}{n-2}, \qquad u(0,\cdot) = u_0 \in \dot H^1(\mathbb{R}^n).$$

Let $u$ be a solution with maximal existence time $T < \infty$ that blows up in **type II** fashion, i.e.

$$\limsup_{t \to T} (T-t)^{\frac{1}{p-1}}\|u(t)\|_{L^\infty} = \limsup_{t\to T}(T-t)^{\frac{n-2}{4}}\|u(t)\|_{L^\infty} = +\infty .$$

**Conjecture (uniqueness / rigidity of blow-up profiles).** For every such solution there exist an integer $k \ge 1$, a regular asymptotic profile $u^* \in \dot H^1$, points $x_j(t) \to x_j^*$, signs $\iota_j \in \{\pm 1\}$ and scales $\lambda_j(t) \to 0$ with $\lambda_1 \ll \lambda_2 \ll \cdots \ll \lambda_k$, such that

$$u(t,\cdot) \;=\; u^* \;+\; \sum_{j=1}^{k} \frac{\iota_j}{\lambda_j(t)^{\frac{n-2}{2}}}\, W\!\Big(\frac{\cdot - x_j(t)}{\lambda_j(t)}\Big) \;+\; o_{\dot H^1}(1), \qquad t \to T,$$

where $W$ is the Aubin–Talenti bubble; and moreover the admissible scaling laws $\lambda_j(t)$ form a **discrete (quantized) family**, determined in each dimension by an explicit list of rates. A complete resolution requires (i) proving the bubble decomposition for *all* type II solutions (soliton resolution along the continuous time limit, not merely along subsequences), and (ii) classifying the possible rates $\lambda_j(t)$, showing no continuum of rates exists. A disproof would exhibit a type II solution with non-bubbling concentration, or a one-parameter continuum of blow-up rates in a fixed dimension.

## 2. Mathematical Foundations

**Scaling and invariants.** The equation is invariant under $u_\lambda(t,x) = \lambda^{\frac{2}{p-1}}u(\lambda^2 t, \lambda x)$, and for $p=p_S$ the exponent is $\frac{2}{p-1} = \frac{n-2}{2}$, so $\|\nabla u_\lambda\|_{L^2} = \|\nabla u\|_{L^2}$: the Dirichlet energy is scale-invariant. The energy

$$E(u) = \frac12\int_{\mathbb{R}^n}|\nabla u|^2 - \frac{1}{p+1}\int_{\mathbb{R}^n}|u|^{p+1}, \qquad \frac{d}{dt}E(u(t)) = -\int_{\mathbb{R}^n}|\partial_t u|^2 \le 0 ,$$

is a Lyapunov functional.

**Ground state.** Steady states of finite energy are the Aubin–Talenti bubbles, extremals of the Sobolev inequality:

$$W(y) = \Big(1+\frac{|y|^2}{n(n-2)}\Big)^{-\frac{n-2}{2}}, \qquad \Delta W + W^{p_S} = 0, \qquad E(W) = \frac1n\|\nabla W\|_{L^2}^2 = \frac1n S^{n/2},$$

with $S$ the best Sobolev constant. Bubbles are non-$L^2$ for $n \le 4$ and carry the quantum of energy that appears in Struwe's global compactness decomposition.

**Linearized operator.** With $\mathcal{L}\varepsilon = -\Delta\varepsilon - p_S W^{p_S-1}\varepsilon$ acting on $\dot H^1(\mathbb{R}^n)$, the spectrum has one negative eigenvalue and kernel spanned by the symmetry modes

$$\Lambda W := \frac{n-2}{2}W + y\cdot\nabla W \quad(\text{scaling}), \qquad \partial_{y_i}W \quad (\text{translations}).$$

Since $W(y) \sim c_n|y|^{-(n-2)}$, one has $\Lambda W(y) \sim -\frac{n-2}{2}c_n|y|^{-(n-2)}$, hence

$$\int_{|y|\le R}|\Lambda W|^2\,dy \;\asymp\; \begin{cases} R, & n=3,\\ \log R, & n=4,\\ O(1), & n\ge 5.\end{cases}$$

This trichotomy governs the modulation law and is the structural source of the dimensional dependence of the blow-up rates.

**Type I vs type II.** Type I means $\|u(t)\|_{L^\infty} \lesssim (T-t)^{-\frac{n-2}{4}}$ (ODE rate); type II is its negation. Under type II with a single bubble, $\|u(t)\|_\infty \sim \lambda(t)^{-\frac{n-2}{2}}$, so type II is equivalent to $\lambda(t) \ll (T-t)^{1/2}$: the concentration scale is asymptotically smaller than the parabolic scale.

## 3. History & State of the Art (SOTA)

- **1966–1985.** Fujita's blow-up theory; Giga–Kohn (*CPAM* 1985, 1987, 1989) prove that for $p < p_S$ all blow-up is type I and asymptotically self-similar. The critical case $p=p_S$ is excluded by their arguments.
- **1984.** Struwe's global compactness theorem gives the bubble-decomposition template for critical elliptic problems and Palais–Smale sequences; it is the elliptic backbone of the conjectured profile decomposition.
- **2000.** Filippas–Herrero–Velázquez perform formal matched asymptotics for radial sign-changing solutions at $p=p_S$ and predict a **discrete family** of type II rates in dimensions $3\le n \le 6$, e.g. $\lambda(t)\sim (T-t)^{k}$ type laws with $k$ integer-indexed, plus log corrections in $n=4$.
- **2012.** Schweyer gives the first rigorous type II construction at $p=p_S$: $n=4$, radial, with
  $$\lambda(t) = c(1+o(1))\,\frac{T-t}{|\log(T-t)|^{2}},\qquad \|u(t)\|_{L^\infty}\sim \lambda(t)^{-1},$$
  stable in a codimension-one sense within the radial class.
- **2017–2020.** Collot–Merle–Raphaël prove a **rigidity theorem in large dimensions**: for $n \ge 7$, solutions starting near the ground state manifold in $\dot H^1\cap L^\infty$ either dissipate, blow up in type I (ODE) fashion, or converge to a rescaled bubble — no type II blow-up occurs near $W$. Their JAMS paper constructs strongly anisotropic non-radial type II blow-up at isolated points, showing the profile geometry can be far from spherically symmetric.
- **2019–2020.** del Pino–Musso–Wei and Cortázar–del Pino–Musso construct type II solutions in $n=5$ (finite time, $\lambda(t)\sim (T-t)^{2}$) and infinite-time bubbling in $n=3$ with rate governed by the Green's function of the domain; Harada constructs a *second, faster* type II rate in $n=5$, confirming that rates are non-unique but appear quantized.
- **2020–2024.** Sharp quantitative stability of Struwe's decomposition (Figalli–Glaudo; Deng–Sun–Wei) supplies the quantitative tool needed to upgrade subsequential bubbling to genuine soliton resolution.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n\ge 7$, data near $W$ in $\dot H^1\cap L^\infty$ | Full trichotomy; **no type II** near the ground state | Collot–Merle–Raphaël 2017 |
| $n=4$, radial | Existence of type II with $\lambda\sim (T-t)|\log(T-t)|^{-2}$; stable in the radial class | Schweyer 2012 |
| $n=5$, radial | Type II with $\lambda(t)\sim(T-t)^2$; also a higher-speed rate | del Pino–Musso–Wei 2019; Harada 2020 |
| $n=3$, bounded domain, Dirichlet | Infinite-time bubbling, $\lambda(t)\sim e^{-?}$ / $t^{-1}$-type laws determined by Green's function; profile uniquely tied to a critical point of the Robin function | Cortázar–del Pino–Musso 2020 |
| $n\ge 5$, non-radial | Anisotropic type II blow-up at isolated points | Collot–Merle–Raphaël 2020 |
| $n=4,5,6$, sign-changing | Tower-of-bubbles ($k\ge 2$) constructions with prescribed relative rates | del Pino–Musso–Wei–Zhou; Filippas–Herrero–Velázquez (formal) |
| Elliptic side, $3\le n\le 5$, any $k$ | Struwe decomposition is *linearly* stable: $\mathrm{dist}(u,\mathcal{M}_k)\lesssim \|\Delta u + u^{p}\|_{H^{-1}}$ | Figalli–Glaudo 2020 |
| Elliptic side, $n\ge 6$ | Sharp non-linear rate with $\log$ loss at $n=6$ | Deng–Sun–Wei 2021 |

Uniqueness of the profile is thus **proved** in the perturbative regime near a single bubble in $n\ge 7$ (trivially: none exists) and in the constructed families where the rate is prescribed a priori. It is **not** proved for arbitrary type II data in $3\le n\le 6$.

## 5. Principal Obstacles

- **No monotonicity for the scale.** Giga–Kohn's self-similar-variable argument uses the local energy and a Liouville theorem valid for $p<p_S$. At $p=p_S$ the rescaled energy is scale-invariant, so it gives no information about $\lambda(t)$; the standard blow-up-limit machinery degenerates.
- **Non-$L^2$ kernel.** For $n\le 4$ the scaling mode $\Lambda W$ fails to be square-integrable (log-divergent at $n=4$, linearly divergent at $n=3$). The modulation equation for $\lambda$ must be extracted by cutting off at the parabolic scale $R \sim \sqrt{T-t}/\lambda$, which couples inner and outer problems and produces logarithmic, non-algebraic laws that are not stable under crude perturbation theory.
- **Slow decay of the bubble tail.** $W \sim c_n|y|^{-(n-2)}$ decays slowly for small $n$; the tail interacts with the far field over the whole parabolic region, so the error terms are not localized and Duhamel estimates lose smallness.
- **Continuous-time vs subsequential convergence.** Compactness plus energy monotonicity gives bubbling *along subsequences* $t_m\to T$. Excluding an oscillating family of distinct limits requires a Łojasiewicz–Simon type inequality at the multi-bubble configuration, which fails naively because the multi-bubble manifold is non-compact (scales degenerate) and the linearization has an almost-kernel.
- **Bubble–bubble interaction.** For towers, the interaction is of order $(\lambda_j/\lambda_{j+1})^{\frac{n-2}{2}}$ and competes with the self-interaction; sign, dimension, and relative rate all change which term dominates, so no single perturbative scheme covers all $k$ and all $n$.

## 6. The Gap

Proven: (a) rigidity near a *single* bubble for $n\ge 7$; (b) existence of specific rates in $n=3,4,5$; (c) sharp quantitative stability of the *elliptic* Struwe decomposition. Conjectured: rigidity for *arbitrary* type II data in $3\le n\le 6$ and for multi-bubble configurations in every dimension.

The exact missing step is a **parabolic Łojasiewicz–Simon inequality at multi-bubble configurations with degenerating scales**: an estimate of the form

$$\mathrm{dist}_{\dot H^1}\big(u,\mathcal{M}_k\big)^{1+\theta} \;\lesssim\; \big|E(u) - E(u^*) - k\,E(W)\big|$$

uniform as $\lambda_1/\lambda_2 \to 0$, together with a proof that the resulting modulation ODE system for $(\lambda_1,\dots,\lambda_k)$ admits only the quantized solution branches. Deng–Sun–Wei supply the *static* version of the left-hand side; converting it into a dynamical statement that pins down $\lambda(t)$ up to the discrete list is the open crossing.

## 7. Current Research (as of June 2026)

- **Soliton resolution for the radial critical heat flow.** Work in the tradition of Jendrej–Lawrie (wave maps) transported to the parabolic setting: continuous-in-time bubble decomposition for radial finite-energy solutions in low dimensions, via collision analysis and virial/localized-energy monotonicity. *(frontier — verify)*
- **Quantitative Struwe stability as a dynamical tool.** Groups around Wei (UBC/CUHK), Sun (Chinese Academy of Sciences), Figalli and Glaudo (ETH) are pushing the sharp elliptic estimates into parabolic convergence-rate theorems, including $n=6$ with logarithmic loss.
- **Inner–outer gluing.** del Pino, Musso, Wei and collaborators continue to use the gluing scheme to produce prescribed rates, sign-changing towers, and non-radial multi-point blow-up, mapping out the *lower* bound on how many profiles exist.
- **Rigidity in high dimensions.** Collot, Merle, Raphaël and students work on removing the $L^\infty$ proximity assumption and extending the trichotomy to $n=5,6$.
- **Numerics.** Adaptive-mesh and rescaling-based simulations in $n=3,4,5$ are used to test the Filippas–Herrero–Velázquez rate list and to look for unlisted rates; no counterexample rate has been reported. *(frontier — verify)*

## 8. Future Work

1. Prove a no-return/no-collision lemma preventing two bubbles with comparable scales from oscillating indefinitely; this would upgrade subsequential to full convergence.
2. Establish the parabolic Łojasiewicz inequality at $k$-bubble towers with explicit $\theta = \theta(n,k)$.
3. Classify solutions of the modulation ODE system derived from matched asymptotics and show its bounded orbits form a discrete set — i.e. prove the quantization of rates from a dynamical-systems angle.
4. Settle the borderline dimension $n=6$ ($p_S=2$), where the bubble tail $|y|^{-4}$ and the nonlinearity $u^2$ both sit at the threshold of the gluing estimates.
5. Transfer the results to the Yamabe flow and harmonic map heat flow, where the same $\Lambda W \notin L^2$ obstruction produces the $(T-t)|\log(T-t)|^{-2}$ law.

## 9. Key References

- **[Foundational]** T. Aubin. *Problèmes isopérimétriques et espaces de Sobolev.* J. Differential Geometry 11 (1976), 573–598.
- **[Foundational]** G. Talenti. *Best constant in Sobolev inequality.* Ann. Mat. Pura Appl. 110 (1976), 353–372.
- **[Foundational]** M. Struwe. *A global compactness result for elliptic boundary value problems involving limiting nonlinearities.* Math. Z. 187 (1984), 511–517.
- **[Foundational]** Y. Giga, R. V. Kohn. *Asymptotically self-similar blow-up of semilinear heat equations.* Comm. Pure Appl. Math. 38 (1985), 297–319.
- **[Foundational]** S. Filippas, M. A. Herrero, J. J. L. Velázquez. *Fast blow-up mechanisms for sign-changing solutions of a semilinear parabolic equation with critical nonlinearity.* Proc. Roy. Soc. London Ser. A 456 (2000), 2957–2982.
- **[SOTA]** R. Schweyer. *Type II blow-up for the four dimensional energy critical semi linear heat equation.* J. Funct. Anal. 263 (2012), 3922–3983.
- **[SOTA]** C. Collot, F. Merle, P. Raphaël. *Dynamics near the ground state for the energy critical nonlinear heat equation in large dimensions.* Comm. Math. Phys. 352 (2017), 215–285.
- **[SOTA]** C. Collot, F. Merle, P. Raphaël. *Strongly anisotropic type II blow up at isolated points.* J. Amer. Math. Soc. 33 (2020), 527–607.
- **[SOTA]** M. del Pino, M. Musso, J. Wei. *Type II blow-up in the 5-dimensional energy critical heat equation.* Acta Math. Sin. (Engl. Ser.) 35 (2019), 1027–1042.
- **[SOTA]** C. Cortázar, M. del Pino, M. Musso. *Green's function and infinite-time bubbling in the critical nonlinear heat equation.* J. Eur. Math. Soc. 22 (2020), 283–344.
- **[SOTA]** J. Harada. *A higher speed type II blowup for the five dimensional energy critical heat equation.* Ann. Inst. H. Poincaré C Anal. Non Linéaire 37 (2020), 309–341.
- **[SOTA]** A. Figalli, F. Glaudo. *On the sharp stability of critical points of the Sobolev inequality.* Arch. Ration. Mech. Anal. 237 (2020), 201–258.
- **[SOTA]** B. Deng, L. Sun, J. Wei. *Sharp quantitative estimates of Struwe's decomposition.* Preprint, arXiv:2103.15360 (2021).
- **[Structure]** H. Matano, F. Merle. *Classification of type I and type II behaviors for a supercritical nonlinear heat equation.* J. Funct. Anal. 256 (2009), 992–1064.
- **[Survey]** P. Quittner, P. Souplet. *Superlinear Parabolic Problems: Blow-up, Global Existence and Steady States.* 2nd ed., Birkhäuser, 2019.

## 10. Worked Example / Concrete Special Case

**Why the rate law changes with $n$: the $L^2$-norm of the scaling mode.**

Take $n=4$, so $p_S = 3$ and

$$W(y) = \Big(1+\frac{|y|^2}{8}\Big)^{-1}, \qquad \Delta W + W^3 = 0 \ \text{ on } \mathbb{R}^4 .$$

Compute the scaling mode $\Lambda W = W + y\cdot\nabla W$ with $r=|y|$:

$$\partial_r W = -\frac{r/4}{(1+r^2/8)^2}, \qquad \Lambda W = \frac{1}{1+\frac{r^2}{8}} - \frac{\frac{r^2}{4}}{\big(1+\frac{r^2}{8}\big)^{2}} = \frac{1-\frac{r^2}{8}}{\big(1+\frac{r^2}{8}\big)^{2}} \;\xrightarrow[r\to\infty]{}\; -\frac{8}{r^{2}} .$$

Hence, with $|S^3| = 2\pi^2$,

$$\int_{|y|\le R}|\Lambda W|^2\,dy \;=\; 2\pi^2\!\!\int^{R}\!\frac{64}{r^{4}}\,r^{3}\,dr + O(1) \;=\; 128\pi^{2}\log R + O(1).$$

The scaling mode is **not** in $L^2(\mathbb{R}^4)$; the divergence is logarithmic. Repeating the computation in general dimension with $\Lambda W \sim -\frac{n-2}{2}c_n r^{-(n-2)}$ gives $\int_{|y|\le R}|\Lambda W|^2 \asymp \int^R r^{4-2n}r^{n-1}dr = \int^R r^{3-n}dr$, i.e. $R$ for $n=3$, $\log R$ for $n=4$, and $O(1)$ for $n\ge 5$.

**Consequence.** In the self-similar frame the modulation equation for $\lambda(t)$ is obtained by projecting the equation on $\Lambda W$, truncated at the parabolic cut-off $R = \sqrt{T-t}/\lambda(t)$, since beyond that radius the bubble no longer describes the solution. The projection carries the weight $\int_{|y|\le R}|\Lambda W|^2$:

- $n \ge 5$: the weight is a finite constant, the modulation law is a clean autonomous ODE, and the rates come out as pure powers — matching $\lambda(t)\sim (T-t)^{2}$ in $n=5$ (del Pino–Musso–Wei) and the discrete higher-speed branches (Harada).
- $n = 4$: the weight is $\log R \approx \tfrac12|\log(T-t)|$ when $\lambda$ is nearly linear in $T-t$. The extra $|\log(T-t)|$ in the denominator of the flux balance produces exactly the observed law
  $$\lambda(t) = c\,\frac{T-t}{|\log(T-t)|^{2}}, \qquad \|u(t)\|_{L^\infty}\sim c^{-1}\frac{|\log(T-t)|^{2}}{T-t} \gg (T-t)^{-1/2},$$
  confirming this solution is type II (the type I rate at $n=4$ is $(T-t)^{-\frac{n-2}{4}} = (T-t)^{-1/2}$).
- $n = 3$: the weight diverges like $R$, the inner problem is dominated by the far field, and no finite-time single-bubble law survives on $\mathbb{R}^3$; on a bounded domain the scale is instead slaved to the Green's function / Robin function of the domain, giving *infinite-time* bubbling.

The example shows the mechanism precisely: the uniqueness question is not about the shape of the profile — that is always $W$ — but about whether the truncated projection identity forces $\lambda(t)$ onto a discrete list of solutions. Only the *existence* of points on that list has been proved; the *absence* of any other point has not.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*