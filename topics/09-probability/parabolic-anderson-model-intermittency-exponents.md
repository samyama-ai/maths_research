---
id: 09-probability/parabolic-anderson-model-intermittency-exponents
title: "Parabolic Anderson Model Intermittency Exponents"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Parabolic Anderson Model Intermittency Exponents

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/parabolic-anderson-model-intermittency-exponents` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The parabolic Anderson model (PAM) is the linear heat equation with a random multiplicative potential,
$$\partial_t u(t,x) = \kappa \Delta u(t,x) + \xi(x)\, u(t,x), \qquad u(0,\cdot)=\delta_0 \text{ or } \mathbf 1,$$
on $\mathbb Z^d$ (discrete Laplacian) or $\mathbb R^d$, with $\xi$ a random field. Solutions are *intermittent*: mass concentrates on a sparse, thin set of high-potential islands, and moments of different orders grow at different exponential rates.

The quantitative content is carried by the **Lyapunov exponents**
$$\lambda_p \;=\; \lim_{t\to\infty}\frac1t \log \mathbb E\big[u(t,0)^p\big] \quad (p>0), \qquad
\lambda_0 \;=\; \lim_{t\to\infty}\frac1t \log u(t,0) \ \ \text{($\xi$-a.s., quenched)} .$$

**Open problem (three linked parts).**

1. **Existence and exact values.** For which potential classes, dimensions $d$, and diffusivities $\kappa$ do all $\lambda_p$ exist, and what are their *closed forms* as functions of $(\kappa,d,p)$?
2. **Full intermittency.** Prove that $p\mapsto \lambda_p/p$ is strictly increasing on $(0,\infty)$ — the analytic definition of intermittency — for all $\kappa>0$ in the physically relevant classes, rather than only for small $\kappa$ or large $p$.
3. **Quenched exponent and the intermittency gap.** Identify $\lambda_0$ exactly, and the second-order (subexponential) corrections that determine the size and number of the intermittent islands.

A complete solution supplies, for a given potential class, a variational formula for each $\lambda_p$ that is evaluated (not merely stated), plus a proof of strict convexity of $p\mapsto\lambda_p$ at every $\kappa>0$.

## 2. Mathematical Foundations

**Feynman–Kac representation.** With $(X_s)$ the continuous-time simple random walk on $\mathbb Z^d$ with generator $\kappa\Delta$,
$$u(t,x)=\mathbb E_x\Big[\exp\Big(\int_0^t \xi(X_s)\,ds\Big)\Big].$$
Moments become many-body problems: for $p\in\mathbb N$ and $\xi$ Gaussian with covariance $\gamma(x-y)$,
$$\mathbb E\big[u(t,0)^p\big]=\mathbb E_{0}^{\otimes p}\Big[\exp\Big(\tfrac12\sum_{j,k=1}^p\int_0^t\!\!\int_0^t \gamma\big(X^j_s-X^k_r\big)\,ds\,dr\Big)\Big],$$
so the exponents are governed by **self-intersection local times** of $p$ independent walks.

**Space–time white noise (SHE).** In $d=1$,
$$\partial_t u=\tfrac12\partial_x^2u+\lambda\, u\,\dot W(t,x),\qquad u(0,\cdot)\equiv1,$$
in the Itô sense; here $\gamma$ is $\delta$ in space and *white in time*, so intersection local times replace double time integrals.

**Analytic vs. geometric intermittency.** By Hölder, $p\mapsto\lambda_p/p$ is non-decreasing. *Full intermittency* means strict monotonicity; it forces $\mathbb E[u^p]$ to be dominated by rare high peaks. **Geometric intermittency** — concentration of $\sum_x u(t,x)$ on $o(1)$-density islands — was shown by Gärtner–König–Molchanov (2007) to follow from the two-point asymptotics.

**Variational structure.** For i.i.d. potentials with cumulant generating function $H(s)=\log\mathbb E[e^{s\xi(0)}]$, the annealed rate is driven by the large-deviation problem
$$\frac1t\log\mathbb E[u(t,0)]\ \approx\ \sup_{g\in \ell^2(\mathbb Z^d),\,\|g\|_2=1}\Big\{\text{(potential gain)}-\kappa\,\mathcal E(g)\Big\},\qquad \mathcal E(g)=\tfrac12\!\!\sum_{|x-y|=1}\!\!(g(x)-g(y))^2 ,$$
whose continuum limit is the **Gross–Pitaevskii-type** functional $\int(\kappa|\nabla g|^2 + \cdots)$. The quenched exponent is the top of the spectrum of the **Anderson Hamiltonian** $\mathcal H=\kappa\Delta+\xi$ restricted to boxes of size $\sim t^{\alpha}$:
$$\lambda_0=\lim_{t\to\infty}\frac1t\,\lambda_{\max}\big(\mathcal H|_{B_{L(t)}}\big) \quad(\text{when finite}).$$
In $d=2,3$ with white-noise $\xi$ the operator $\mathcal H$ needs renormalization; it is constructed via **paracontrolled distributions / regularity structures** (Hairer 2014).

## 3. History & State of the Art (SOTA)

- **1958.** Anderson's localization paper motivates the spectral picture.
- **1990.** Gärtner–Molchanov, *Parabolic problems for the Anderson model I* (Comm. Math. Phys.), formulate the model probabilistically and prove annealed asymptotics for i.i.d. potentials.
- **1994.** Carmona–Molchanov, Memoirs AMS 518, establish the intermittency framework, existence of $\lambda_p$ for white-noise potential, and $\lambda_0<0$ (complete localization) in $d=1,2$ for every $\kappa$.
- **1995.** Bertini–Cancrini compute *exactly* the moment Lyapunov exponents of the $1{+}1$-dimensional SHE: $\lambda_p=p(p^2-1)\lambda^4/24$ for $u_0\equiv1$.
- **1998.** Gärtner–Molchanov II (Comm. Math. Phys.): almost-sure (quenched) asymptotics and localization.
- **2006.** van der Hofstad–König–Mörters (Comm. Math. Phys.) isolate **four universality classes** for i.i.d. potentials (double-exponential, Weibull-type, Pareto-type/heavy tails, bounded-from-above), each with its own exponent scaling.
- **2009.** König–Lacoin–Mörters–Sidorova, *A two cities theorem* (Ann. Probab.): for Pareto tails the total mass concentrates on **exactly two** sites at typical large times.
- **2014–2016.** Hairer's regularity structures make the PAM well-posed in $d=2,3$ with white noise; X. Chen (Ann. IHP 2015) obtains the **precise quenched exponent** for the $1{+}1$ SHE.
- **2016.** König's monograph consolidates the field.

## 4. Partial Results / Verified Cases

| Setting | What is known | Source |
|---|---|---|
| SHE on $\mathbb R$, space–time white noise, $u_0\equiv1$ | **All** annealed exponents exactly: $\lambda_p=\frac{p(p^2-1)}{24}\lambda^4$; full intermittency for all $p>1$ | Bertini–Cancrini (1995) |
| Same, quenched | $\lambda_0$ exists, is strictly negative, and scales as $-c\,\lambda^{4/3}$ with $c$ given by an explicit variational constant | X. Chen (2015) |
| Lattice, white-noise (i.i.d. Gaussian-type) potential, $d=1,2$ | $\lambda_0<0$ for all $\kappa>0$; $\lambda_0\asymp-\kappa\log^2(1/\kappa)$ order in $d=1$ as $\kappa\downarrow0$ | Carmona–Molchanov (1994); Cranston–Mountford–Shiga (2002) |
| Double-exponential potential, all $d$ | Annealed and quenched first-order asymptotics; island size $O(1)$ (a "$\rho$-dependent" scale); geometric intermittency proven | Gärtner–König–Molchanov (2000, 2007) |
| Pareto / heavy tails, $d\ge1$ | Complete localization on one or two sites; exponents $t^{1/(\alpha-1)}$-type scaling | König–Lacoin–Mörters–Sidorova (2009); Ortgiese–Roberts (2016) |
| Bounded-above potentials (e.g. Bernoulli) | Quenched asymptotics with $\log$-corrections from Dirichlet eigenvalues of large clear regions | Biskup–König (2001) |
| Gaussian potential, general covariance, Skorokhod regime | Moment asymptotics $\log\mathbb E[u^p]\sim C p^{\theta} t^{\beta}$ with explicit $\theta,\beta$ from Gaussian chaos | X. Chen (2014, 2017) |
| Nonlinear SPDEs $\partial_t u=\frac12 u''+\sigma(u)\dot W$ | Weak intermittency ($\lambda_2>0$, $\lambda_0$ finite) under Lipschitz + linear-growth $\sigma$ | Foondun–Khoshnevisan (2009) |

## 5. Principal Obstacles

- **Non-commutativity of the two limits.** $\lambda_0$ needs $t\to\infty$ *before* averaging; moment methods (Feynman–Kac + Gaussian chaos) compute only $\lambda_p$, and $\lambda_p/p\to\lambda_0$ as $p\downarrow0$ fails without uniform control of the $p\to0$ limit. No general interchange theorem exists.
- **Variational formulas that cannot be evaluated.** Beyond the double-exponential class the limiting functional is a nonconvex Gross–Pitaevskii problem; existence of maximizers is known, but their value (the constant in the exponent) is not computable in closed form for $d\ge2$.
- **Intersection local times are supercritical.** For $\gamma=\delta$ in $d\ge2$, the $p$-body exponent involves mutual intersection local times of Brownian motions that are almost surely infinite; renormalization changes the model (Skorokhod vs. Stratonovich) and the two conventions give different exponents.
- **Strict convexity is a rare-event statement.** Proving $\lambda_{p+1}/(p+1)>\lambda_p/p$ requires showing the optimal $p$-body configuration genuinely clusters more than the $(p{+}1)$-body one; second-moment/Paley–Zygmund arguments give only non-strict comparisons.
- **Spectral input is unavailable.** $\lambda_0$ is a top-of-spectrum problem for $\kappa\Delta+\xi$ on growing boxes; sharp eigenvalue tails for rough $\xi$ in $d\ge2$ (post-renormalization) are only partially developed.
- **Moderate $\kappa$.** Almost every sharp result is perturbative in $\kappa\downarrow0$ (strong disorder) or $\kappa\to\infty$; the crossover regime has no small parameter.

## 6. The Gap

Proven: exact $\lambda_p$ for $p\in\mathbb N$ in the exactly-solvable $1{+}1$ white-noise case, and first-order asymptotics (leading term only, often as $t\to\infty$ with $\kappa$ fixed but constant unidentified) inside the four universality classes on $\mathbb Z^d$.

Not proven, and the precise boundary:

1. **Non-integer $p$, and $p\downarrow0$.** The interpolation between $\lambda_p$ ($p\ge1$) and $\lambda_0$ is missing; the $p\to0$ asymptotic of $\lambda_p/p$ is conjectured to reproduce $\lambda_0$ but no proof exists outside $d=1$ white noise.
2. **Second-order terms.** The constants controlling island diameter $\ell(t)$ and island count $N(t)$ are known only in the double-exponential and Pareto classes.
3. **$d\ge2$ renormalized PAM.** With white noise in $d=2,3$, no Lyapunov exponent (annealed or quenched) has been computed; only well-posedness and qualitative localization of $\kappa\Delta+\xi$ are established.
4. **Strict monotonicity for all $\kappa$.** The step needed is a *quantitative* clustering inequality for $p$ interacting Brownian paths that is uniform in $\kappa$.

## 7. Current Research (as of June 2026)

- **Singular-SPDE school (Hairer, Labbé, Chouk, van Zuijlen, Dumaz; Imperial/Warwick, Paris-Saclay, Bonn).** Spectral asymptotics for the renormalized Anderson Hamiltonian in $d=2,3$; the eigenvalue tail is the missing input for $\lambda_0$. *(frontier — verify: exponent-level results in $d=3$ remain preprint-stage.)*
- **Moment/chaos school (X. Chen, Hu, Nualart, Khoshnevisan; Tennessee, Kansas, Utah).** Exact moment exponents for fractional and rough noises, including Hurst parameters below the standard threshold, and Skorokhod-vs-Stratonovich comparison.
- **Lattice localization school (König, Mörters, Sidorova, Ortgiese; Leipzig/WIAS, Köln, Bath).** Refined "few cities" theorems, ageing of the localization site, and the PAM with time-dependent or branching-particle potentials.
- **KPZ-adjacent exact solvability (Corwin, Borodin, Le Doussal, Ghosal).** Replica/Bethe-ansatz derivations of full moment sequences for the SHE with general initial data; upper-tail large deviations of $\log u$ at rate $t^{1/3}$ *(frontier — verify uniformity claims).*

## 8. Future Work

- Prove an **interchange theorem** giving $\lambda_0=\lim_{p\downarrow0}\lambda_p/p$ under a checkable concentration hypothesis; this would transfer all annealed results to the quenched side.
- Develop **eigenvalue-tail estimates** for the renormalized $\kappa\Delta+\xi$ in $d=2,3$ sharp enough to feed a Borel–Cantelli argument for $\lambda_0$.
- Establish **strict convexity of $p\mapsto\lambda_p$** by a rearrangement / Brascamp–Lieb inequality on intersection local times, valid at all $\kappa$.
- Push the **island geometry** program (number, diameter, spacing, ageing) beyond the double-exponential and Pareto classes to Weibull tails.
- Extend to **time-dependent potentials** $\xi(t,x)$ with general space–time covariance, where even the existence of $\lambda_p$ is open for critically rough noise.

## 9. Key References

- **[Foundational]** R. Carmona, S. A. Molchanov. *Parabolic Anderson Problem and Intermittency.* Memoirs of the American Mathematical Society 518, AMS, 1994.
- **[Foundational]** J. Gärtner, S. A. Molchanov. *Parabolic problems for the Anderson model I. Intermittency and related topics.* Communications in Mathematical Physics 132, 1990.
- **[Foundational]** J. Gärtner, S. A. Molchanov. *Parabolic problems for the Anderson model II. Second-order asymptotics and structure of high peaks.* Probability Theory and Related Fields 111, 1998.
- **[Foundational]** L. Bertini, N. Cancrini. *The stochastic heat equation: Feynman–Kac formula and intermittence.* Journal of Statistical Physics 78, 1995.
- **[SOTA]** X. Chen. *Precise intermittency for the parabolic Anderson equation with an $(1+1)$-dimensional time–space white noise.* Annales de l'Institut Henri Poincaré (B) 51, 2015.
- **[SOTA]** R. van der Hofstad, W. König, P. Mörters. *The universality classes in the parabolic Anderson model.* Communications in Mathematical Physics 267, 2006.
- **[SOTA]** W. König, H. Lacoin, P. Mörters, N. Sidorova. *A two cities theorem for the parabolic Anderson model.* Annals of Probability 37, 2009.
- **[SOTA]** M. Hairer. *A theory of regularity structures.* Inventiones Mathematicae 198, 2014.
- **[SOTA]** M. Foondun, D. Khoshnevisan. *Intermittence and nonlinear parabolic stochastic partial differential equations.* Electronic Journal of Probability 14, 2009.
- **[Survey]** W. König. *The Parabolic Anderson Model: Random Walk in Random Potential.* Birkhäuser (Pathways in Mathematics), 2016.
- **[Survey]** J. Gärtner, W. König. *The parabolic Anderson model.* In: Interacting Stochastic Systems, Springer, 2005.
- **[Survey]** X. Chen. *Random Walk Intersections: Large Deviations and Related Topics.* Mathematical Surveys and Monographs 157, AMS, 2010.
- **[Related]** M. Cranston, T. S. Mountford, T. Shiga. *Lyapunov exponents for the parabolic Anderson model.* Acta Mathematica Universitatis Comenianae 71, 2002.
- **[Related]** M. Biskup, W. König. *Long-time tails in the parabolic Anderson model with bounded potential.* Annals of Probability 29, 2001.
- **[Related]** M. Ortgiese, M. I. Roberts. *Intermittency for branching random walk in Pareto environment.* Annals of Probability 44, 2016.

## 10. Worked Example / Concrete Special Case

**Second moment of the $1{+}1$-dimensional stochastic heat equation.** Take
$$\partial_t u=\tfrac12 \partial_x^2 u+\lambda\,u\,\dot W,\qquad u(0,\cdot)\equiv1 .$$

*Step 1 — moment duality.* Itô's formula plus the Wiener chaos expansion gives, for two independent standard Brownian motions $B^1,B^2$ started at $0$,
$$\mathbb E\big[u(t,x)^2\big]=\mathbb E\Big[\exp\Big(\lambda^2 L_t^0(B^1-B^2)\Big)\Big],$$
where $L^0_t$ is Brownian local time at the origin (the delta covariance in space contracts to a local time; whiteness in time removes the double time integral).

*Step 2 — reduce to one Brownian motion.* $B^1-B^2\stackrel{d}{=}\sqrt2\,B$. Local time scales as $L^0_t(cB)=c^{-1}L^0_t(B)$, so
$$\lambda^2 L^0_t(B^1-B^2)\ \stackrel{d}{=}\ \frac{\lambda^2}{\sqrt2}\,L^0_t(B).$$

*Step 3 — evaluate.* $L^0_t(B)\stackrel{d}{=}|B_t|$ (Lévy), hence for $\theta>0$,
$$\mathbb E\big[e^{\theta L_t^0}\big]=\mathbb E\big[e^{\theta|B_t|}\big]=e^{\theta^2t/2}\big(1+o(1)\big)\cdot 2\Phi(\theta\sqrt t),$$
so $\frac1t\log\mathbb E[e^{\theta L_t^0}]\to\theta^2/2$. With $\theta=\lambda^2/\sqrt2$:
$$\boxed{\ \lambda_2=\frac{1}{2}\cdot\frac{\lambda^4}{2}=\frac{\lambda^4}{4}\ }$$

*Step 4 — check against the general formula.* Bertini–Cancrini give $\lambda_p=p(p^2-1)\lambda^4/24$; at $p=2$ this is $2\cdot3\cdot\lambda^4/24=\lambda^4/4$. ✓

*Step 5 — read off intermittency.* $\lambda_p/p=(p^2-1)\lambda^4/24$ is strictly increasing in $p$, so this case is fully intermittent, with the ratio $\mathbb E[u^2]/(\mathbb E[u])^2=e^{\lambda^4t/4}$ blowing up: typical values of $u$ are far below its mean. Meanwhile $\lambda_0<0$ (Chen 2015): almost every realization decays exponentially while every moment grows. That contrast — $\lambda_0<0<\lambda_1<\lambda_2/2<\cdots$ — *is* intermittency, and reproducing this complete ladder of exponents in $d\ge2$, or for non-white potentials, is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*