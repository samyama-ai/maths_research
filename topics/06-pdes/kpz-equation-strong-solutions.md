---
id: 06-pdes/kpz-equation-strong-solutions
title: "KPZ Equation Strong Solutions"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# KPZ Equation Strong Solutions

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kpz-equation-strong-solutions` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Kardar–Parisi–Zhang (KPZ) equation for a height field $h(t,x)$, $t>0$, $x\in\mathbb{R}$ or $\mathbb{T}=\mathbb{R}/\mathbb{Z}$, is

$$\partial_t h \;=\; \tfrac12\,\partial_x^2 h \;+\; \tfrac{\lambda}{2}\,(\partial_x h)^2 \;+\; \xi,$$

where $\xi$ is space–time white noise: the centered Gaussian field with $\mathbb{E}[\xi(t,x)\xi(s,y)]=\delta(t-s)\delta(x-y)$.

**The problem.** The equation is *analytically ill-posed as written*: solutions of the linear part have spatial Hölder regularity $\tfrac12^-$, so $\partial_x h$ is a distribution of regularity $-\tfrac12^-$ and $(\partial_x h)^2$ has no canonical meaning. The task is to give an intrinsic, mollifier-independent notion of solution — a **strong solution theory** — such that:

1. **(Existence/uniqueness)** For initial data in a natural class there is a unique solution, continuous in time with values in $\mathcal{C}^{\alpha}$, $\alpha<\tfrac12$.
2. **(Renormalized approximation)** For any smooth mollifier $\rho$ with $\xi_\varepsilon=\xi*\rho_\varepsilon$, the classical solutions $h_\varepsilon$ of
$$\partial_t h_\varepsilon=\tfrac12\partial_x^2h_\varepsilon+\tfrac{\lambda}{2}\big((\partial_x h_\varepsilon)^2-C_\varepsilon\big)+\xi_\varepsilon$$
converge in probability to $h$ for a suitable divergent sequence $C_\varepsilon\to\infty$, with the limit independent of $\rho$ up to a finite shift.
3. **(Stability/universality)** The solution map is continuous in the driving data, so that discrete growth models and weakly asymmetric particle systems converge to it.

A complete resolution answers this in every space dimension $d$ and for the natural generalisations (non-quadratic nonlinearity, non-Gaussian or coloured noise, systems). In $d=1$ the answer is now a theorem. In $d\ge2$ it is not: there the equation is critical ($d=2$) or supercritical ($d\ge3$), and it is expected — but not proven — that no nontrivial local strong solution theory exists at the critical coupling scale.

## 2. Mathematical Foundations

**Scaling and subcriticality.** Under $h_\delta(t,x)=\delta^{-\chi}h(\delta^{-z}t,\delta^{-1}x)$ with $z=2$, white noise scales with exponent $\tfrac{2-d}{2}$; in $d=1$ the nonlinearity $(\partial_x h)^2$ carries a positive power of $\delta$ relative to the linear terms, so the equation is **locally subcritical**. In $d=2$ the nonlinearity is exactly marginal; in $d\ge3$ it is supercritical (irrelevant at small scales, relevant at large ones).

**Cole–Hopf.** Formally $Z=e^{\lambda h}$ solves the multiplicative stochastic heat equation (SHE)

$$\partial_t Z=\tfrac12\partial_x^2Z+\lambda\,Z\,\xi ,$$

interpreted in the Itô sense, which is well-posed in $d=1$ by Walsh theory; positivity of $Z$ for positive initial data (Mueller's strong maximum principle) makes $h:=\lambda^{-1}\log Z$ well defined. This is the **Cole–Hopf solution** (Bertini–Giacomin 1997). It is a definition, not a solution theory: it says nothing about which approximations converge to it, and it does not survive perturbation of the nonlinearity.

**Hölder–Besov spaces.** For $\alpha<0$, $\mathcal{C}^\alpha=B^\alpha_{\infty,\infty}$ is the space of distributions $u$ with $\|\Delta_j u\|_{L^\infty}\lesssim 2^{-j\alpha}$ for the Littlewood–Paley blocks $\Delta_j$. Bony's paraproduct decomposes $fg=f\prec g+f\circ g+f\succ g$; the resonant term $f\circ g$ converges only when the regularities satisfy $\alpha+\beta>0$ — precisely the condition that fails for $\partial_xh\circ\partial_xh$ with $\alpha=\beta=-\tfrac12^-$.

**Regularity structures.** A regularity structure $\mathscr{T}=(A,T,G)$ with $A\subset\mathbb{R}$ locally finite, $T=\bigoplus_{\alpha\in A}T_\alpha$, and a structure group $G$; a *model* $(\Pi,\Gamma)$ assigns to each symbol a concrete distribution obeying analytic bounds. The **reconstruction theorem** states: for $\gamma>0$ and $f\in\mathcal{D}^\gamma$ there is a unique $\mathcal{R}f\in\mathcal{C}^{\min A}$ with $|\langle \mathcal{R}f-\Pi_xf(x),\varphi^\lambda_x\rangle|\lesssim\lambda^\gamma$. For KPZ the relevant symbols are $\Xi$, $\mathcal{I}'(\Xi)$, $\mathcal{I}'(\Xi)^2$, $\mathcal{I}'(\mathcal{I}'(\Xi)^2)$, and the renormalisation group acts by subtracting the divergent expectations of the last two.

**Energy solutions.** For the stationary Burgers form $u=\partial_xh$,
$$\partial_tu=\tfrac12\partial_x^2u+\tfrac{\lambda}{2}\partial_x(u^2)+\partial_x\xi,$$
with $u(t,\cdot)$ spatial white noise, one defines the quadratic term by the Itô-trick bound
$$\mathbb{E}\Big[\sup_{t\le T}\Big|\int_0^t \partial_x(u_s^2)(\varphi)\,ds\Big|^2\Big]\lesssim T\|\varphi\|^2_{H^{1}} ,$$
valid uniformly in mollification, plus the reversibility condition that $\hat u_t=u_{T-t}$ solves the same equation with $\lambda\mapsto-\lambda$.

## 3. History & State of the Art

- **1986.** Kardar, Parisi and Zhang propose the equation as the universal continuum model for randomly growing interfaces, predicting the exponents $\chi=1/2$, $z=3/2$ in $d=1$ and a roughening transition in $d\ge3$.
- **1997.** Bertini and Giacomin derive the Cole–Hopf solution as the scaling limit of the weakly asymmetric simple exclusion process (WASEP), giving the first rigorous meaning to the equation.
- **2010–2011.** Exact solvability: Amir, Corwin and Quastel obtain the one-point distribution of the narrow-wedge solution and its crossover to Tracy–Widom GUE, confirming $\chi=1/2$, $z=3/2$.
- **2013.** Hairer, *Solving the KPZ equation* (Annals of Mathematics 178), builds the first intrinsic pathwise solution theory using rough-path/Wild-expansion methods; the renormalized approximations converge to Cole–Hopf.
- **2014.** Hairer, *A theory of regularity structures* (Inventiones 198) generalises this to a broad class of singular SPDEs; Fields Medal 2014.
- **2015.** Gubinelli, Imkeller and Perkowski introduce paracontrolled distributions (Forum of Mathematics Pi 3), an alternative Fourier-analytic route.
- **2018.** Gubinelli and Perkowski prove uniqueness of energy solutions (JAMS 31), completing the probabilistic-weak route and unlocking convergence proofs for many non-perturbative particle systems.
- **2019–2021.** The black-box algebraic/analytic machinery is completed: Bruned–Hairer–Zambotti (renormalisation group), Chandra–Hairer (BPHZ convergence), Bruned–Chandra–Chevyrev–Hairer (renormalised equations).
- **2021–2023.** Structure above KPZ: Matetski–Quastel–Remenik construct the **KPZ fixed point** (Acta Math. 227, 2021); Dauvergne–Ortmann–Virág construct the **directed landscape** (Acta Math. 229, 2022); Quastel–Sarkar prove convergence of exclusion processes and of the KPZ equation itself to the fixed point (JAMS 36, 2023).
- **$d=2$.** Caravenna–Sun–Zygouras establish the entire subcritical regime and then construct the **critical 2D stochastic heat flow** (Inventiones, 2024), a genuinely new object that is *not* a function-valued solution.

## 4. Partial Results / Verified Cases

- **$d=1$, quadratic nonlinearity, space–time white noise: fully solved.** Global-in-time existence and uniqueness on $\mathbb{T}$ and on $\mathbb{R}$; initial data in $\mathcal{C}^\alpha$, $\alpha>0$, and narrow-wedge data $h_0=\delta_0$-type via Cole–Hopf. Counterterm $C_\varepsilon=c_\rho\varepsilon^{-1}+\tilde c_\rho+o(1)$, linear divergence, mollifier-dependent constant.
- **Approximation classes proven to converge to KPZ in $d=1$:** WASEP and a wide family of weakly asymmetric conservative particle systems (Gonçalves–Jara, ARMA 212, 2014, via energy solutions); a class of continuous microscopic growth models with general polynomial nonlinearity $\sum_{k\le p} a_k(\partial_x h)^k$ (Hairer–Quastel, Forum Math. Pi 6, 2018), where only the even coefficients contribute in the limit and the effective coupling is $\lambda_{\text{eff}}=\sum_k a_{2k}\,(2k-1)!!\,\sigma^{2k-2}$; discretisations and lattice approximations (Hairer–Matetski).
- **Coloured / smoothed noise, $d=1$:** well-posedness holds a fortiori and the $\varepsilon\to0$ limit matches white-noise KPZ after the same renormalisation.
- **$d=2$, subcritical coupling $\hat\lambda_\varepsilon=\hat\beta\sqrt{2\pi/\log(1/\varepsilon)}$ with $\hat\beta<1$:** Caravenna–Sun–Zygouras (Ann. Probab. 48, 2020) and Chatterjee–Dunlap (Ann. Probab. 48, 2020) show Gaussian (Edwards–Wilkinson) fluctuations with explicit variance $\hat\beta^2/(1-\hat\beta^2)$; Gu, and Dunlap–Gu–Ryzhik–Zeitouni give the corresponding $d\ge3$ small-coupling results.
- **$d=2$, critical $\hat\beta=1$ window:** the *stochastic heat flow* exists as a random measure-valued flow (Caravenna–Sun–Zygouras, Invent. Math. 2024), proven not to be the exponential of a Gaussian field. No KPZ height function.
- **$d\ge3$, weak coupling below a threshold:** the SHE has an $L^2$ limit and the height field has Gaussian fluctuations (Magnen–Unterberger; Dunlap–Gu–Ryzhik–Zeitouni, PTRF 176, 2020).

## 5. Principal Obstacles

- **Failure of Bony's resonant estimate.** $\partial_xh\circ\partial_xh$ requires $\alpha+\beta>0$ with $\alpha=\beta=-\tfrac12^-$: the product is not merely hard to estimate, it is genuinely undefined without extra data (the second-order model / paracontrolled ansatz). Nothing in classical Schauder or energy-method PDE supplies that data.
- **Loss of the maximum principle.** The renormalisation subtracts an infinite constant from a *positive* quantity, so comparison and $L^\infty$ arguments break; a priori bounds must come from Cole–Hopf positivity or from stationarity, neither of which survives perturbation of the nonlinearity.
- **$d=2$ marginality.** The analogue of $C_\varepsilon$ diverges only logarithmically, so a *multiplicative* rather than additive renormalisation is forced; the local subcriticality hypothesis underlying regularity structures and paracontrolled calculus fails outright, and the renormalisation series has no small parameter.
- **$d\ge3$ supercriticality.** The nonlinearity is irrelevant at small scales but relevant at large ones; local theories give nothing globally, and the strong-coupling phase is inaccessible: even the existence of the conjectured roughening transition in $d=3$ is unproven.
- **Non-Gaussian / anisotropic settings.** Without Gaussianity, Wiener-chaos and hypercontractivity bounds — the engine of every convergence proof for models — are unavailable; for the anisotropic KPZ equation in $d=2$ the nonlinearity has a sign structure that cancels at leading order, and the predicted $\sqrt{\log\log t}$ behaviour is out of reach.

## 6. The Gap

In $d=1$ there is no gap: the problem in Section 1 is a theorem. The frontier has moved to three sharply stated boundaries.

- **Between subcritical and critical in $d=2$.** Proven: Gaussian limits for $\hat\beta<1$; a measure-valued flow at $\hat\beta=1$. Missing: any object playing the role of $h$ at criticality, and a proof that no such height field exists — the expected statement is that the critical 2D KPZ equation admits *no* nontrivial function-valued strong solution.
- **Between weak and strong coupling in $d\ge3$.** Proven: Gaussian fluctuations for $\lambda<\lambda_c$. Missing: existence of $\lambda_c<\infty$ as a genuine phase transition point with non-Gaussian behaviour above it.
- **Between "the equation" and "the class".** In $d=1$ the fixed-point convergence (Quastel–Sarkar) is proven for KPZ and for exclusion; missing is a universality theorem covering non-integrable models with no exact solvability and no stationary measure known in closed form.

## 7. Current Research (as of June 2026)

- **Regularity structures at scale.** Chandra, Hairer, and collaborators (Imperial College London, EPFL) continue extending the BPHZ black box to systems with gauge symmetry and to non-Gaussian noises; the analytic BPHZ theorem (Chandra–Hairer) is the operative tool.
- **Energy solutions and non-integrable models.** Gubinelli, Perkowski (Bonn, FU Berlin), Gonçalves, Jara (Lisbon, IMPA) push the martingale-problem approach to systems without product-form invariant measures.
- **Critical 2D.** Caravenna, Sun, Zygouras (Milan, NUS, Warwick) study the fine structure of the stochastic heat flow — its multifractal spectrum, its non-Gaussianity, its scaling limits. *(frontier — verify)* Claims of a full characterisation of the critical flow's law and of a matching non-existence result for the 2D height field circulate as preprints.
- **KPZ fixed point universality.** Quastel, Remenik, Matetski, Virág, Dauvergne: extending convergence to the directed landscape beyond integrable models; Virág's "heat and the landscape" programme.
- **Global well-posedness for generalised nonlinearities.** Work on $\partial_th=\partial_x^2h+F(\partial_xh)+\xi$ with non-quadratic $F$: local theory is standard, global theory is open because Cole–Hopf fails.

## 8. Future Work

- Prove a **non-existence theorem** for critical 2D KPZ: no separable-noise renormalisation produces a nontrivial $\mathcal{C}^{0^-}$-valued solution.
- Establish the **strong-coupling transition in $d=3$**, e.g. by a rigorous renormalisation-group analysis of the polymer free energy.
- Remove the **Gaussian-chaos crutch**: convergence proofs for microscopic models driven by heavy-tailed or dependent randomness.
- **Global-in-time bounds without Cole–Hopf**, via stationarity or coercivity, to handle general $F$.
- Turn the **KPZ fixed point** into a genuine attractor statement: a domain-of-attraction theorem quantifying which growth models converge and at what rate.

## 9. Key References

- **[Foundational]** M. Kardar, G. Parisi, Y.-C. Zhang. *Dynamic Scaling of Growing Interfaces.* Physical Review Letters 56, 889–892, 1986.
- **[Foundational]** L. Bertini, G. Giacomin. *Stochastic Burgers and KPZ equations from particle systems.* Communications in Mathematical Physics 183, 571–607, 1997.
- **[Foundational]** M. Hairer. *Solving the KPZ equation.* Annals of Mathematics 178(2), 559–664, 2013.
- **[Foundational]** M. Hairer. *A theory of regularity structures.* Inventiones Mathematicae 198(2), 269–504, 2014.
- **[SOTA]** M. Gubinelli, P. Imkeller, N. Perkowski. *Paracontrolled distributions and singular PDEs.* Forum of Mathematics, Pi 3, e6, 2015.
- **[SOTA]** M. Gubinelli, N. Perkowski. *Energy solutions of KPZ are unique.* Journal of the AMS 31(2), 427–471, 2018.
- **[SOTA]** M. Hairer, J. Quastel. *A class of growth models rescaling to KPZ.* Forum of Mathematics, Pi 6, e3, 2018.
- **[SOTA]** K. Matetski, J. Quastel, D. Remenik. *The KPZ fixed point.* Acta Mathematica 227(1), 115–203, 2021.
- **[SOTA]** D. Dauvergne, J. Ortmann, B. Virág. *The directed landscape.* Acta Mathematica 229(2), 201–285, 2022.
- **[SOTA]** F. Caravenna, R. Sun, N. Zygouras. *The critical 2d Stochastic Heat Flow.* Inventiones Mathematicae, 2024.
- **[SOTA]** J. Quastel, S. Sarkar. *Convergence of exclusion processes and the KPZ equation to the KPZ fixed point.* Journal of the AMS 36, 251–289, 2023.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications 1(1), 1130001, 2012.
- **[Survey]** M. Gubinelli, N. Perkowski. *KPZ reloaded.* Communications in Mathematical Physics 349, 165–269, 2017.
- **[Book]** M. Hairer. *An Introduction to Stochastic PDEs.* Lecture notes, 2009 (arXiv:0907.4178).

## 10. Worked Example / Concrete Special Case

**Computing the counterterm $C_\varepsilon$ on the torus.** Take $\lambda=1$ and the *linear* (Edwards–Wilkinson) equation on $\mathbb{T}$, $\partial_tX=\tfrac12\partial_x^2X+\xi$, which supplies the leading behaviour of $(\partial_xh_\varepsilon)^2$.

Expand in Fourier modes $k=2\pi n$, $n\in\mathbb{Z}$. Each nonzero mode is a complex Ornstein–Uhlenbeck process,
$$d\hat X_k=-\tfrac{k^2}{2}\hat X_k\,dt+d\hat\beta_k,\qquad \mathbb{E}|\hat X_k|^2=\frac{1}{k^2}\ \ \text{in stationarity}.$$

Mollify: $X_\varepsilon=X*\rho_\varepsilon$, so $\widehat{X_\varepsilon}(k)=\hat\rho(\varepsilon k)\hat X_k$. Then

$$\mathbb{E}\big[(\partial_xX_\varepsilon)^2\big]=\sum_{n\neq0}k^2|\hat\rho(\varepsilon k)|^2\,\mathbb{E}|\hat X_k|^2=\sum_{n\neq0}|\hat\rho(2\pi\varepsilon n)|^2 .$$

Replace the sum by an integral ($u=2\pi\varepsilon n$, spacing $2\pi\varepsilon$):

$$\sum_{n\neq0}|\hat\rho(2\pi\varepsilon n)|^2=\frac{1}{2\pi\varepsilon}\int_{\mathbb{R}}|\hat\rho(u)|^2\,du+O(1)=\frac{c_\rho}{\varepsilon}+O(1),\qquad c_\rho=\frac{1}{2\pi}\|\hat\rho\|_{L^2}^2 .$$

Three conclusions, all visible in this one line:

1. **The divergence is $\varepsilon^{-1}$ and the constant $c_\rho$ depends on the mollifier.** Hence $C_\varepsilon=c_\rho\varepsilon^{-1}+\tilde c_\rho$ and the limit is mollifier-independent only after a finite shift $h\mapsto h-\tilde c_\rho t$ — exactly the statement in Section 1(2).
2. **Only a constant needs subtracting.** The divergent part is deterministic and $x$-independent because the noise is stationary; this is what makes the additive renormalisation sufficient in $d=1$, and it is a consequence of subcriticality: the Wick-ordered product $(\partial_xX_\varepsilon)^2-C_\varepsilon$ lives in the second Wiener chaos and converges in $\mathcal{C}^{-1^-}$.
3. **The same computation in $d=2$ gives $\log(1/\varepsilon)$.** There $\mathbb{E}|\hat X_k|^2=|k|^{-2}$ but the mode sum is two-dimensional: $\sum_{k}|\hat\rho(\varepsilon k)|^2\asymp\varepsilon^{-2}$ while the Wick constant for the SHE nonlinearity behaves like $\int_{1}^{1/\varepsilon}\frac{dr}{r}=\log(1/\varepsilon)$. A logarithm cannot be absorbed by shifting $h$; it must be absorbed into the coupling, forcing $\hat\lambda_\varepsilon\sim\hat\beta\sqrt{2\pi/\log(1/\varepsilon)}$ — the critical window of Caravenna–Sun–Zygouras, and the precise point at which the $d=1$ theory stops working.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*