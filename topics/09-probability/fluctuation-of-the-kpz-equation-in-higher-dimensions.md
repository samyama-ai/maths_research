---
id: 09-probability/fluctuation-of-the-kpz-equation-in-higher-dimensions
title: "Fluctuation of the KPZ Equation in Higher Dimensions"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fluctuation of the KPZ Equation in Higher Dimensions

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/fluctuation-of-the-kpz-equation-in-higher-dimensions` · **Status:** open

## 1. Problem Statement / Conjecture

The Kardar–Parisi–Zhang (KPZ) equation in $d$ spatial dimensions is

$$\partial_t h(t,x) = \tfrac12 \Delta h + \tfrac{\lambda}{2}|\nabla h|^2 + \sqrt{\beta}\,\xi(t,x), \qquad x \in \mathbb{R}^d,$$

with $\xi$ space-time white noise. For $d = 1$ the theory is complete: $h$ is well posed via Hopf–Cole and regularity structures, and $t^{-1/3}\big(h(t,0) - \mathbb{E}h(t,0)\big)$ converges to a Tracy–Widom-type law. For $d \ge 2$ the following are open.

1. **Well-posedness at fixed coupling.** For $d\ge 2$, $\xi$ is too rough for the nonlinearity to make sense: give a nontrivial, non-Gaussian, translation-covariant construction of a solution to the mollified equation as the mollification scale $\varepsilon \to 0$ with $\lambda,\beta$ fixed, or prove none exists (triviality).
2. **Strong-coupling exponents.** Prove existence of exponents $\chi(d), z(d)$ with
$$\varepsilon^{\chi}\big(h(\varepsilon^{-z}t,\varepsilon^{-1}x)-\mathbb{E}h\big) \Rightarrow \mathfrak{h}_d,$$
a nondegenerate limit, and identify them. Conjecturally $\chi + z = 2$ (Galilean/tilt invariance) holds in all $d$; the pair is otherwise unknown for every $d \ge 2$.
3. **Upper critical dimension.** Decide whether there is $d_c < \infty$ above which $\chi = 0$ and the strong-coupling fixed point coincides with Edwards–Wilkinson (EW). Mode-coupling and some renormalization arguments predict $d_c = 4$; numerics of Marinari–Pagnani–Parisi predict $d_c = \infty$.

A complete resolution means: a construction as in (1), a limit theorem as in (2) with identified exponents, and a proof or disproof of (3).

## 2. Mathematical Foundations

**Hopf–Cole.** Setting $u = \exp(\lambda h)$ formally turns KPZ into the multiplicative stochastic heat equation (SHE)
$$\partial_t u = \tfrac12\Delta u + \lambda\sqrt{\beta}\, u\,\xi ,\qquad u(0,\cdot)\equiv 1 .$$
For $d \ge 2$, $\xi$ has parabolic Hölder regularity $-\tfrac{d}{2}-1-$, and Itô theory for $u\xi$ requires $d = 1$. One therefore mollifies: let $\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon)$, $\xi_\varepsilon = \xi * \rho_\varepsilon$ in space, and study
$$\partial_t u_\varepsilon = \tfrac12\Delta u_\varepsilon + \beta_\varepsilon\, u_\varepsilon\, \xi_\varepsilon .$$

**Scaling / disorder relevance.** The Feynman–Kac representation
$$u_\varepsilon(t,x) = \mathbb{E}_B\Big[\exp\Big(\beta_\varepsilon\!\int_0^t \xi_\varepsilon(t-s, x+B_s)\,ds - \tfrac{\beta_\varepsilon^2 t}{2}R_\varepsilon\Big)\Big]$$
identifies $u_\varepsilon$ with a continuum directed-polymer partition function, where $R_\varepsilon = \int_0^\infty p_s(0)\,(\rho_\varepsilon\!*\!\rho_\varepsilon)$-type overlap. The Brownian intersection integral $\int_0^1 p_s(0)\,ds$ diverges like $\varepsilon^{2-d}$ for $d\ge 3$ and like $\log(1/\varepsilon)$ for $d = 2$. Hence:

- $d = 1$: disorder **relevant**, $\beta_\varepsilon = \varepsilon^{1/2}\beta$ gives intermediate disorder.
- $d = 2$: disorder **marginally relevant**; the critical window is $\beta_\varepsilon^2 = \dfrac{2\pi\hat\beta^2}{\log(1/\varepsilon)}$ with critical point $\hat\beta_c = 1$.
- $d \ge 3$: disorder **irrelevant at small coupling**; $\beta_\varepsilon = \beta$ fixed, with a phase transition at $\beta_c(d) > 0$ between weak and strong disorder.

**Weak vs. strong disorder.** For $d\ge3$ the martingale $u_\varepsilon(t,0)$ (equivalently the polymer partition function $W_n$) converges a.s. to $W_\infty \ge 0$; weak disorder is $\{W_\infty > 0\}$ a.s., strong disorder is $W_\infty = 0$ a.s. There is $\beta_c(d)\in(0,\infty)$ separating them (Comets–Yoshida).

**Predicted exponents.** $h(t,0)$ fluctuates as $t^{\chi/z}$ with $\chi+z=2$. Values: $d=1$: $\chi=1/2$, $z=3/2$. EW ($\lambda=0$): $\chi=(2-d)/2$, $z=2$, so $h$ has logarithmic fluctuations in $d=2$ and is pointwise finite-variance Gaussian in $d\ge3$. Numerics for the strong-coupling fixed point give roughly $\chi \approx 0.39, z\approx 1.61$ ($d=2$) and $\chi\approx 0.31, z\approx 1.69$ ($d=3$).

## 3. History & State of the Art (SOTA)

- **1986.** Kardar, Parisi, Zhang introduce the equation; one-loop dynamic RG shows the coupling is marginal in $d=2$ and has a nontrivial fixed point above a threshold in $d>2$, with no perturbatively accessible strong-coupling fixed point.
- **1987–1995.** Forster–Nelson–Stephen-type RG and mode-coupling theory (Bouchaud–Cates, Doherty et al.) predict $d_c=4$; Lässig and others dispute it.
- **1998.** Bertini–Cancrini analyze the two-dimensional SHE with mollified noise and identify the $1/\log$ scaling of the critical window.
- **2002.** Marinari–Pagnani–Parisi simulate up to $d=6$ and report $\chi>0$ in every dimension, arguing against a finite $d_c$.
- **2014.** Hairer's regularity structures solve KPZ in $d=1$; the method is subcritical only for $d=1$ and does not extend.
- **2016–2020.** Rigorous **weak-coupling (EW) limits** in $d\ge3$ (Magnen–Unterberger; Gu–Ryzhik–Zeitouni; Dunlap–Gu–Ryzhik–Zeitouni; Comets–Cosco–Mukherjee) and in the full subcritical $d=2$ window (Caravenna–Sun–Zygouras; Chatterjee–Dunlap; Gu).
- **2023.** Caravenna, Sun and Zygouras construct the **critical 2d stochastic heat flow** at $\hat\beta_c=1$: a genuinely new, non-Gaussian, measure-valued process that is not the exponential of a Gaussian field (*Inventiones Mathematicae*). This is the first rigorous non-EW continuum object above $d=1$.
- **Present.** No rigorous statement whatsoever about strong-coupling exponents for any $d\ge2$.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $d\ge3$, $\beta<\beta_{L^2}$ fixed | $u_\varepsilon(t,x)\to$ a.s. positive limit; $\varepsilon^{1-d/2}(u_\varepsilon-1)\Rightarrow$ solution of additive SHE; $h$ has **EW** Gaussian fluctuations with $\chi=(2-d)/2$, $z=2$ | Magnen–Unterberger (2018); Gu–Ryzhik–Zeitouni (2018); Dunlap–Gu–Ryzhik–Zeitouni (2020) |
| $d\ge3$, all $\beta$ | Existence of $\beta_c(d)\in(0,\infty)$; weak/strong disorder dichotomy; $L^2$ threshold $\beta_{L^2}\le\beta_c$ and the inequality is **strict** | Comets–Yoshida (2006); Mukherjee–Shamov–Zeitouni (2016); Birkner–Sun; Berger–Lacoin (2017) |
| $d=2$, $\hat\beta<1$ (entire subcritical window) | $\log$-scaled field converges to EW; second-order CLT with explicit variance $\log\frac{1}{1-\hat\beta^2}$ | Caravenna–Sun–Zygouras (2017, 2020); Chatterjee–Dunlap (2020); Gu (2020) |
| $d=2$, $\hat\beta=1$ (critical window) | Existence, uniqueness and non-Gaussianity of the **critical 2d stochastic heat flow**; moment characterization | Caravenna–Sun–Zygouras (2023); Tsai (2024) |
| $d=2$, $\hat\beta>1$ | Nothing rigorous |  |
| Any $d$, fixed $\lambda$ | Local KPZ behavior (a quantitative local Gaussian-plus-drift structure) for a class of growth models under arbitrary scaling | Chatterjee (2023) |
| Numerics | $d=2$: $\chi\approx0.39$, $z\approx1.61$; $d=3$: $\chi\approx0.31$; $d=4,5$: $\chi>0$ small but nonzero | Marinari–Pagnani–Parisi (2002); Kelling–Ódor (2011) |

## 5. Principal Obstacles

- **Subcriticality fails.** Regularity structures / paracontrolled calculus need the nonlinearity to be a subcritical perturbation: for KPZ this is $d<2$. At $d=2$ the equation is exactly critical, at $d\ge3$ supercritical. No renormalization scheme with finitely many counterterms exists there; the theories are not merely hard to apply — they are inapplicable.
- **Hopf–Cole loses its power.** In $d=1$ Hopf–Cole plus the exact solvability of ASEP/TASEP/$q$-TASEP delivers Fredholm-determinant formulas. In $d\ge2$ the SHE is still linear, but there is no known integrable discretization: no Bethe-ansatz-solvable $d\ge2$ growth model, no Macdonald-process input, no determinantal structure.
- **Moments blow up.** The chaos expansion $u=\sum_k I_k$ has $k$-th moment governed by $k$-body Brownian intersection local times, which are infinite for $d\ge2$; the $L^2$ method controls only the weak-disorder phase and provably misses $[\beta_{L^2},\beta_c)$.
- **No superadditivity for exponents.** In $d=1$ the exponent $\chi$ can be extracted from last-passage percolation via subadditive ergodic theorems plus concentration. In $d\ge2$ the natural transversal/longitudinal exponent relation $\chi=2z-... $ is unproven even in the KPZ scaling-relation form $\chi=2\chi_{\text{trans}}-1$ except for one-sided inequalities.
- **Strong disorder is genuinely non-perturbative.** The polymer measure localizes on $O(1)$ favorable corridors; every existing tool (martingale, chaos, replica-symmetric perturbation) presumes delocalization.

## 6. The Gap

Everything proven above $d=1$ concerns a **vanishing coupling** tuned to the scale: $\beta_\varepsilon\to0$ in $d\ge3$ scaled by $\varepsilon^{(d-2)/2}$, or $\beta_\varepsilon\sim(\log\frac1\varepsilon)^{-1/2}$ in $d=2$. In those windows the limit is either Gaussian (EW) or, at $\hat\beta_c=1$ in $d=2$, the stochastic heat flow. The conjecture concerns **fixed** $\lambda,\beta$ at large $t$ — the strong-coupling fixed point, which lies at infinite distance from every window controlled so far. The precise step needed: an a-priori estimate showing that $\mathrm{Var}\,h(t,0)\asymp t^{2\chi/z}$ with $\chi>0$ for fixed coupling in $d=2$ or $d=3$, i.e. a **lower bound beating the EW/logarithmic prediction** — currently unavailable even up to constants. Equivalently, on the polymer side: prove that the free energy $\frac1n\log W_n$ has fluctuations of order $n^{\chi/z}$ with $\chi/z>0$ in the strong-disorder phase for $d\ge2$.

## 7. Current Research (as of June 2026)

- **Critical 2d SHF program.** Caravenna (Milano-Bicocca), Sun (NUS) and Zygouras (Warwick), with Tsai (Utah), study the properties of the critical stochastic heat flow: singularity of its law with respect to any Gaussian multiplicative chaos, its moment growth $\mathbb{E}[Z^k] \sim \exp(Ck^2\log k)$-type bounds, and its role as a candidate $d=2$ KPZ fixed point. *(frontier — verify: claims that the SHF's logarithm gives the $d=2$ strong-coupling KPZ field remain conjectural.)*
- **Beyond the $L^2$ threshold in $d\ge3$.** Junk (Kyushu), Cosco, Nakajima, Nakashima study the martingale limit $W_\infty$ and local limit theorems in the whole weak-disorder phase $\beta<\beta_c$, establishing that EW behavior persists past $\beta_{L^2}$ — a genuinely new region.
- **Nonlinear-fluctuation / mode-coupling rigor.** Gu (Maryland), Dunlap (Duke), Ryzhik (Stanford) push moderate-deviation and higher-order expansions for the weakly coupled equation.
- **Chatterjee's local-KPZ framework** (Stanford) aims to identify KPZ-type behavior in all $d$ without solvability, currently at the level of local structure rather than exponents.
- **High-precision GPU simulation** (Ódor, Kelling, Budapest) refines $\chi(d)$ up to $d=5$; the $d_c=4$ question remains numerically contested. *(frontier — verify.)*

## 8. Future Work

- Construct the **$d=2$ supercritical** ($\hat\beta>1$) continuum object, or show the finite-dimensional distributions degenerate.
- Prove a **variance lower bound** $\mathrm{Var}\,\log W_n \gtrsim n^{c}$, $c>0$, in the strong-disorder phase for $d=2,3$ — the smallest quantitative statement that would rule out EW behavior at strong coupling.
- Establish the **KPZ scaling relation** $\chi = 2\xi - 1$ (with $\xi$ the transversal wandering exponent) in $d\ge2$; only partial one-sided results exist, adapted from Chatterjee's and Auffinger–Damron's FPP arguments.
- Find any **integrable model in $d\ge2$** in the KPZ class, or prove a no-go theorem; this is the structural analogue of the search for higher-dimensional solvable vertex models.
- Settle $d_c$ by identifying whether $\beta_c(d)\to\infty$ fast enough that the strong-coupling fixed point merges with EW.

## 9. Key References

- **[Foundational]** M. Kardar, G. Parisi, Y.-C. Zhang. *Dynamic Scaling of Growing Interfaces.* Physical Review Letters **56**, 889–892, 1986.
- **[Foundational]** L. Bertini, N. Cancrini. *The two-dimensional stochastic heat equation: renormalizing a multiplicative noise.* Journal of Physics A **31**, 615–622, 1998.
- **[Foundational]** M. Hairer. *A theory of regularity structures.* Inventiones Mathematicae **198**, 269–504, 2014.
- **[SOTA]** F. Caravenna, R. Sun, N. Zygouras. *The critical 2d Stochastic Heat Flow.* Inventiones Mathematicae **233**, 325–460, 2023.
- **[SOTA]** F. Caravenna, R. Sun, N. Zygouras. *The two-dimensional KPZ equation in the entire subcritical regime.* Annals of Probability **48**(3), 1086–1127, 2020.
- **[SOTA]** F. Caravenna, R. Sun, N. Zygouras. *Universality in marginally relevant disordered systems.* Annals of Applied Probability **27**(5), 3050–3112, 2017.
- **[SOTA]** S. Chatterjee, A. Dunlap. *Constructing a solution of the $(2+1)$-dimensional KPZ equation.* Annals of Probability **48**(2), 1014–1055, 2020.
- **[SOTA]** A. Dunlap, Y. Gu, L. Ryzhik, O. Zeitouni. *Fluctuations of the solutions to the KPZ equation in dimensions three and higher.* Probability Theory and Related Fields **176**, 1217–1258, 2020.
- **[SOTA]** Y. Gu, L. Ryzhik, O. Zeitouni. *The Edwards–Wilkinson limit of the random heat equation in dimensions three and higher.* Communications in Mathematical Physics **363**, 351–388, 2018.
- **[SOTA]** J. Magnen, J. Unterberger. *The scaling limit of the KPZ equation in space dimension 3 and higher.* Journal of Statistical Physics **171**, 543–598, 2018.
- **[SOTA]** C. Mukherjee, A. Shamov, O. Zeitouni. *Weak and strong disorder for the stochastic heat equation and continuous directed polymers in $d\ge3$.* Electronic Communications in Probability **21**, paper 61, 2016.
- **[SOTA]** Q. Berger, H. Lacoin. *The high-temperature behavior for the directed polymer in dimension $1+2$.* Annales de l'IHP Probabilités et Statistiques **53**(1), 430–450, 2017.
- **[SOTA]** L.-C. Tsai. *Stochastic heat flow by moments.* arXiv preprint, 2024.
- **[SOTA]** S. Chatterjee. *Local KPZ behavior under arbitrary scaling limits.* Communications in Mathematical Physics **396**, 1277–1304, 2022.
- **[Numerics]** E. Marinari, A. Pagnani, G. Parisi. *Critical exponents of the KPZ equation via multi-surface coding numerical simulations.* Journal of Physics A **33**, 8181–8192, 2000.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications **1**(1), 1130001, 2012.
- **[Survey / Book]** F. Comets. *Directed Polymers in Random Environments.* Lecture Notes in Mathematics 2175, Springer, 2017.
- **[Survey]** T. Halpin-Healy, Y.-C. Zhang. *Kinetic roughening phenomena, stochastic growth, directed polymers and all that.* Physics Reports **254**, 215–414, 1995.

## 10. Worked Example / Concrete Special Case

**Why $d=2$ is exactly critical, computed on the discrete polymer.** Take simple random walk $S$ on $\mathbb{Z}^d$ and i.i.d. standard Gaussian environment $\omega(n,x)$. Define
$$W_N = \mathbb{E}_S\Big[\exp\Big(\sum_{n=1}^N \big(\beta_N\omega(n,S_n)-\tfrac{\beta_N^2}{2}\big)\Big)\Big],$$
a mean-one martingale. Its second moment is computed by replicating: with $S,S'$ independent walks,
$$\mathbb{E}[W_N^2] = \mathbb{E}_{S,S'}\Big[\exp\Big(\beta_N^2 \sum_{n=1}^N \mathbf{1}_{\{S_n=S'_n\}}\Big)\Big].$$
The difference $S-S'$ is a random walk, so $\sum_{n\le N}\mathbf 1_{\{S_n=S_n'\}}$ has mean $R_N=\sum_{n\le N} P(S_n = S'_n) \asymp \sum_{n\le N} n^{-d/2}$. Hence
$$R_N \asymp \begin{cases} \sqrt{N}, & d=1,\\ \tfrac{1}{\pi}\log N, & d=2,\\ R_\infty < \infty, & d\ge3.\end{cases}$$

Writing $\sigma^2 = e^{\beta_N^2}-1 \approx \beta_N^2$ and summing the geometric series over the number of collisions,
$$\mathbb{E}[W_N^2] \approx \sum_{k\ge0} \sigma^{2k}\, u_k(N), \qquad u_k(N)=\text{$k$-fold collision integral} \approx \frac{R_N^k}{k!}\cdot(\text{combinatorics}),$$
and the series stays bounded precisely when $\sigma^2 R_N = O(1)$. This forces the scaling of the coupling:

- $d=1$: $\beta_N^2 \sim \hat\beta^2 N^{-1/2}$ — polynomially relevant, the intermediate-disorder regime whose limit is the $d=1$ SHE.
- $d=2$: $\beta_N^2 = \dfrac{\pi\hat\beta^2}{\log N}$. Then $\sigma^2R_N\to \hat\beta^2$, and the resummation $\sum_k \hat\beta^{2k} = (1-\hat\beta^2)^{-1}$ converges iff $\hat\beta<1$. This is the origin of the critical point $\hat\beta_c=1$ and of the second-order CLT variance $\log\frac{1}{1-\hat\beta^2}$ found by Caravenna–Sun–Zygouras.
- $d\ge3$: $\beta_N=\beta$ fixed works, and $\mathbb{E}[W_\infty^2]<\infty$ iff $\beta^2 R_\infty$ is small, giving the explicit $L^2$ threshold $\beta_{L^2}$ with $e^{\beta_{L^2}^2}-1 = 1/R_\infty$ (and $R_\infty$ is the Green's function collision constant of the $d$-dimensional walk).

**Where the problem starts.** All three lines above are second-moment computations, valid only when the geometric series converges. Above $\hat\beta_c$ in $d=2$, or above $\beta_c$ in $d\ge3$, $W_N\to0$ and one wants the fluctuation exponent of $\log W_N$. The second-moment machinery gives nothing: $\mathbb{E}[W_N^2]/(\mathbb{E}W_N)^2 \to \infty$, and $\log W_N$ is not accessible by any moment of $W_N$. Predicting $\log W_N \approx -c N + N^{\chi/z}\,\Xi$ with $\chi/z \approx 0.24$ in $d=2$ is exactly the open problem of Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*