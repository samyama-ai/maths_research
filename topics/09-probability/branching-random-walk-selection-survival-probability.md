---
id: 09-probability/branching-random-walk-selection-survival-probability
title: "Survival Probability of Branching Random Walks with Selection"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Survival Probability of Branching Random Walks with Selection

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/branching-random-walk-selection-survival-probability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A branching random walk (BRW) under *selection* is a branching particle system on $\mathbb{R}$ in which particles are removed by a selection rule: either killed below a moving absorbing wall of slope $-\mu$, or culled to keep only the $N$ rightmost particles ($N$-BRW). Both rules destroy the branching property and the associated martingale structure, and both are near-critical: the system barely survives.

The problem has two coupled parts.

**(A) Near-critical survival probability (Derrida–Simon problem).** For branching Brownian motion (BBM) with binary branching at rate $1$, standard diffusion, drift $-\mu$, killed at the origin, let $Q(\mu,x)$ be the probability of eternal survival from a single particle at $x>0$. Survival is possible iff $\mu<\mu_c=\sqrt2$. Write $\mu=\sqrt{2-\epsilon}$. Determine the complete asymptotic expansion of $Q$ as $\epsilon\downarrow0$: the leading exponential rate is known, and the conjecture is that

$$Q(\epsilon,x)\;=\;C\,\epsilon^{\,\alpha}\,f(x)\,\exp\!\Big(-\frac{\sqrt2\,\pi}{\sqrt{\epsilon}}\Big)\,(1+o(1)),$$

with an explicit constant $C$, exponent $\alpha$, and shape function $f$. **Open:** everything beyond the leading exponent.

**(B) $N$-BRW persistence.** For the $N$-particle system with an extra source of death (extra killing rate, or a hard wall), quantify the survival probability and the extinction time as $N\to\infty$, including the conjectured Brunet–Derrida corrections
$$v_c-v_N=\frac{\pi^2\chi}{2(\log N+3\log\log N)^2}\,(1+o(1)).$$

A complete solution means proofs of the prefactor asymptotics in (A) and of the full second-order expansion plus fluctuation theory in (B), for general step distributions with exponential moments.

## 2. Mathematical Foundations

**BRW.** Let $\mathcal{L}$ be a point process on $\mathbb{R}$ with $\kappa(\theta)=\log\mathbb{E}\big[\sum_{u\in\mathcal{L}}e^{\theta X_u}\big]<\infty$ on a neighbourhood of some $\theta^*>0$. The BRW $(X_u)_{u\in\mathbb{T}}$ has i.i.d. copies of $\mathcal{L}$ attached to each vertex. The a.s. speed of the maximum is
$$v_c=\inf_{\theta>0}\frac{\kappa(\theta)}{\theta}=\frac{\kappa(\theta^*)}{\theta^*},\qquad \kappa'(\theta^*)\theta^*-\kappa(\theta^*)=0 .$$

**Killed BRW.** Kill every particle falling below the line $n\mapsto -\rho n$. The system survives with positive probability iff $\rho>-v_c$ (strict), dies a.s. at the critical slope $\rho=-v_c$ (Kesten 1978; Biggins–Lubachevsky–Shwartz–Weiss 1991).

**BBM normalization.** For binary BBM at rate $1$ with drift $-\mu$ killed at $0$, the survival probability $u(x)=Q(\mu,x)$ solves the stationary FKPP equation
$$\tfrac12 u''+\mu\,u'+u-u^2=0,\qquad u(0)=0,\ u(+\infty)=1 .$$
Its linearization $\mathcal{A}=\tfrac12\partial_x^2+\mu\partial_x+1$ on the strip $(0,L)$ with Dirichlet boundaries has principal eigenpair
$$\varphi_L(x)=e^{-\mu x}\sin\!\Big(\frac{\pi x}{L}\Big),\qquad \lambda(L)=1-\frac{\mu^2}{2}-\frac{\pi^2}{2L^2}=\frac{\epsilon}{2}-\frac{\pi^2}{2L^2},$$
using $\mu^2=2-\epsilon$. Criticality $\lambda=0$ fixes the **effective strip width**
$$\boxed{\;L_\epsilon=\frac{\pi}{\sqrt{\epsilon}}\;}$$
and the associated additive martingale-like functional
$$Y_t=\sum_{i}e^{\sqrt2\,x_i(t)}\sin\!\Big(\frac{\pi x_i(t)}{L}\Big)\mathbf{1}_{\{0<x_i(t)<L\}},$$
which is (to leading order) a conserved quantity of the quasi-stationary dynamics and is the correct state variable for survival.

**Selection ($N$-BRW).** At each generation, branch all $N$ particles, then keep the $N$ rightmost. The empirical cloud travels at a deterministic speed $v_N<v_c$ with $v_N\to v_c$. Matching $N\asymp\int_0^L e^{\theta^* x}\varphi_L\,dx\asymp e^{\theta^* L}$ gives $L\approx \theta^{*-1}\log N$, so the cutoff-induced speed deficit is $\Theta((\log N)^{-2})$ — the Brunet–Derrida law.

## 3. History & State of the Art (SOTA)

- **1978.** Kesten proves a.s. extinction of BBM with critical drift $\sqrt2$ and absorption, with bounds on the extinction time and on the number of particles.
- **1991.** Biggins, Lubachevsky, Shwartz, Weiss give the sharp survival/extinction criterion for BRW with a linear barrier.
- **1997.** Brunet and Derrida, studying FKPP fronts with a cutoff $1/N$, predict the $\pi^2/\log^2 N$ velocity deficit — a slow, universal correction not visible to naive perturbation theory.
- **2007–2008.** Derrida and Simon formulate the near-critical survival problem, predict $\log Q\asymp -c/\sqrt{\epsilon}$ from the FKPP boundary-layer/strip picture, and describe the quasi-stationary regime.
- **2010.** Bérard and Gouéré prove the Brunet–Derrida first-order law $v_c-v_N\sim \pi^2\chi/(2\log^2N)$ for a class of lattice BRWs with $N$-selection.
- **2011.** Gantert, Hu and Shi obtain the sharp leading-order asymptotics of $\log$(survival probability) for killed BRW as the slope approaches critical; Aïdékon and Jaffuel refine survival/extinction-generation counts; Berestycki, Berestycki and Schweinsberg establish the $Y$-threshold description of near-critical survival for BBM.
- **2013–2017.** BBS identify the genealogy under absorption as the Bolthausen–Sznitman coalescent on time scale $(\log N)^3$; Maillard (2016) proves speed and fluctuation results for $N$-BBM; Schweinsberg (2017) proves the $3\log\log N$ second-order correction for the BBM-with-absorption population model.

**SOTA summary:** leading exponential order is theorem; prefactors, and general-step-distribution second order, remain conjectural.

## 4. Partial Results / Verified Cases

- **Critical slope, general BRW:** extinction a.s. (Kesten 1978; BLSW 1991). Total progeny of the critical killed BRW has tail $\mathbb{P}(Z>n)\sim c/(n\log^2 n)$-type behaviour (Aïdékon 2010).
- **Leading exponent, $\epsilon\downarrow0$:** for BBM in the normalization above, $\log Q(\epsilon,x)=-\sqrt2\,\pi\,\epsilon^{-1/2}(1+o(1))$; the analogous statement for BRW with finite exponential moments, with the constant explicit in terms of $\theta^*$ and $\kappa''(\theta^*)$, is Gantert–Hu–Shi (2011).
- **Configuration threshold:** BBS (2011) show that near-critical BBM survives with probability tending to $1$ (resp. $0$) when the initial value of $Y$ is far above (resp. below) an explicit $L$-dependent threshold, giving matching upper/lower bounds up to constants.
- **$N$-BRW velocity:** $v_c-v_N\sim \pi^2\chi/(2\log^2N)$ proved for lattice BRWs with bounded steps and mild regularity (Bérard–Gouéré 2010); the $3\log\log N$ correction and $(\log N)^3$ genealogical time scale proved for BBM with absorption (BBS 2013; Schweinsberg 2017); speed and Lévy-type fluctuation limits for $N$-BBM (Maillard 2016).
- **Polynomial tails:** if the step law has regularly varying tail of index $\alpha$, the Brunet–Derrida universality *fails*; Bérard–Maillard (2014) determine the correct scaling and identify a non-trivial limiting jump process.
- **Solvable case:** the exponential/Poisson-cascade model of Brunet–Derrida–Mueller–Munier (2007) gives exact ancestry and confirms Bolthausen–Sznitman genealogy.

## 5. Principal Obstacles

- **Loss of branching structure.** Selection couples all particles: $N$-BRW is neither a branching process nor an exchangeable interacting particle system with a tractable generator. The many-to-one lemma and additive martingales $\sum e^{\theta X_u -n\kappa(\theta)}$, the two workhorses of BRW theory, only survive in truncated, error-accumulating form.
- **Near-critical FKPP prefactors.** The travelling-wave PDE for $Q$ is nonlinear and the relevant regime is a *singular* boundary layer: the nonlinearity $u^2$ matters only in an $O(1)$-window near the top of the strip of width $\pi/\sqrt\epsilon$, so the constant $C$ is set by matching an inner nonlinear problem to an outer linear one. No general theory delivers matching constants for such exponentially small quantities; both the linear-eigenvalue method and probabilistic first/second-moment methods lose $e^{O(1)/\sqrt{\epsilon}}$-free but still $\Theta(1)$-indeterminate factors.
- **Second moments blow up.** The functional $Y$ is nearly conserved in mean but has heavy-tailed jumps (a single particle reaching the top of the strip multiplies $Y$ by an $L^3$-scale factor), so $\mathbb{E}[Y^2]=\infty$ in the relevant regime and Paley–Zygmund arguments give bounds only up to constants.
- **Stable-law time scales.** The jump structure produces a $1$-stable (Bolthausen–Sznitman/Neveu) limit with logarithmic corrections; $1$-stable limits have no scaling-invariant centring, which is exactly the source of the $3\log\log N$ term and why proofs must control three separate scales ($O(1)$, $\log N$, $(\log N)^3$) simultaneously.
- **Non-universality.** Any argument must be robust to the failure of the $\log^{-2}N$ law under polynomial tails, so it cannot rest on soft comparison alone.

## 6. The Gap

Proven: $\log Q=-\sqrt2\pi\epsilon^{-1/2}(1+o(1))$, i.e. control of $Q$ up to factors $e^{o(\epsilon^{-1/2})}$. Conjectured: $Q=C\epsilon^{\alpha}f(x)e^{-\sqrt2\pi/\sqrt\epsilon}(1+o(1))$. The gap is the entire subexponential factor — a multiplicative window of size $e^{o(1/\sqrt\epsilon)}$, which hides any power of $\epsilon$.

Crossing it requires a *sharp* description of the rate at which the near-critical system converts a single particle into a quasi-stationary cloud of size $Y\sim L^3$: an exact renewal/one-jump decomposition for the $Y$-process with matching constants, uniformly in $\epsilon$. Equivalently, on the PDE side, an inner–outer matched expansion for the cutoff FKPP travelling wave in which the inner nonlinear correction constant is computed, not merely bounded. Existing proofs produce two-sided bounds with different constants; no method currently pins the constant on both sides.

For $N$-BRW the analogous gap is between $\Theta(\log^{-2}N)$-type theorems for restricted step laws and the conjectured full expansion $v_N=v_c-\frac{\pi^2\chi}{2}\big[(\log N+3\log\log N)^{-2}+O(\log^{-3}N)\big]$ for general laws with exponential moments.

## 7. Current Research (as of June 2026)

- **Sharp prefactors via spine and Yaglom-type methods.** Groups in Paris (LPSM/Sorbonne; Shi, Aïdékon and collaborators), Bath/Warwick, and Vienna (Maillard) push spine decompositions and Yaglom limits for critical killed BRW toward constant-level precision. *(frontier — verify)*
- **Genealogy beyond Bolthausen–Sznitman.** Refined coalescent approximations with $(\log N)^{-1}$ corrections; work connecting $N$-BRW genealogies to the Brunet–Derrida universality class in continuous state space. *(frontier — verify)*
- **Non-standard selection rules.** $L$-BBM (kill below the leading particle minus $L$), $\ell$-fitness rules, and "soft" selection with density-dependent killing; Pain's velocity results are the template, and the survival/extinction dichotomy for random $L$ is active.
- **Heavy tails and non-universality.** Extending Bérard–Maillard to intermediate tail classes (stretched exponentials), where the crossover between the $\log^{-2}N$ law and stable behaviour occurs.
- **Large deviations.** Derrida–Shi's programme on slower/faster deviations of BBM maxima under selection or coalescence, giving rate functions that encode the same $\sqrt\epsilon$ scaling.
- **Numerics.** High-precision simulation of $N$ up to $10^{12}$-equivalents via the $Y$-functional and exponential-record representations, testing the $\epsilon^\alpha$ prefactor exponent. *(frontier — verify)*

## 8. Future Work

- Develop a rigorous matched-asymptotics framework for the cutoff FKPP wave that produces two-sided constants, converting the Derrida–Simon heuristic into theorem.
- Prove a Yaglom-type limit for critical killed BRW conditioned on survival to generation $n$, uniformly as the slope approaches critical, which would supply the missing prefactor.
- Establish the $3\log\log N$ correction for lattice BRW with general steps, removing the BBM-specific Brownian-strip computations (Schweinsberg's method uses the exact BBM eigenfunctions).
- Determine the fluctuation field for the $N$-BRW front: conjecturally a Lévy-type process with $1$-stable jumps on time scale $(\log N)^3$; proved for $N$-BBM, open in the lattice case.
- Classify the universality classes of selection rules by tail index, unifying $N$-BRW, $L$-BBM and killed BRW.

## 9. Key References

- **[Foundational]** H. Kesten. *Branching Brownian motion with absorption.* Stochastic Processes and their Applications 7 (1978), 9–47.
- **[Foundational]** J. D. Biggins, B. D. Lubachevsky, A. Shwartz, A. Weiss. *A branching random walk with a barrier.* Annals of Applied Probability 1 (1991), 573–581.
- **[Foundational]** É. Brunet, B. Derrida. *Shift in the velocity of a front due to a cutoff.* Physical Review E 56 (1997), 2597–2604.
- **[Foundational]** B. Derrida, D. Simon. *The survival probability of a branching random walk in presence of an absorbing wall.* Europhysics Letters 78 (2007), 60006.
- **[Foundational]** D. Simon, B. Derrida. *Quasi-stationary regime of a branching random walk in presence of an absorbing wall.* Journal of Statistical Physics 131 (2008), 203–233.
- **[Foundational]** É. Brunet, B. Derrida, A. H. Mueller, S. Munier. *Effect of selection on ancestry: an exactly soluble case and its phenomenological generalization.* Physical Review E 76 (2007), 041104.
- **[SOTA]** J. Bérard, J.-B. Gouéré. *Brunet–Derrida behavior of branching-selection particle systems on the line.* Communications in Mathematical Physics 298 (2010), 323–342.
- **[SOTA]** N. Gantert, Y. Hu, Z. Shi. *Asymptotics for the survival probability in a killed branching random walk.* Annales de l'IHP Probabilités et Statistiques 47 (2011), 111–129.
- **[SOTA]** E. Aïdékon, B. Jaffuel. *Survival of branching random walks with absorption.* Stochastic Processes and their Applications 121 (2011), 1901–1937.
- **[SOTA]** J. Berestycki, N. Berestycki, J. Schweinsberg. *Survival of near-critical branching Brownian motion.* Journal of Statistical Physics 143 (2011), 833–854.
- **[SOTA]** J. Berestycki, N. Berestycki, J. Schweinsberg. *The genealogy of branching Brownian motion with absorption.* Annals of Probability 41 (2013), 527–618.
- **[SOTA]** J. Bérard, P. Maillard. *The limiting process of N-particle branching random walk with polynomial tails.* Electronic Journal of Probability 19 (2014), paper 22.
- **[SOTA]** P. Maillard. *Speed and fluctuations of N-particle branching Brownian motion with spatial selection.* Probability Theory and Related Fields 166 (2016), 1061–1173.
- **[SOTA]** J. Schweinsberg. *Rigorous results for a population model with selection I: evolution of the population size; II: genealogy of the population.* Electronic Journal of Probability 22 (2017).
- **[SOTA]** M. Pain. *Velocity of the $L$-branching Brownian motion.* Electronic Journal of Probability 21 (2016), paper 28.
- **[Recent]** B. Derrida, Z. Shi. *Large deviations for the branching Brownian motion in presence of selection or coalescence.* Journal of Statistical Physics 163 (2016), 1285–1311.
- **[Survey]** Z. Shi. *Branching Random Walks.* École d'Été de Probabilités de Saint-Flour XLII (2012), Lecture Notes in Mathematics 2151, Springer, 2015.

## 10. Worked Example / Concrete Special Case

**Deriving the strip width and the two matched exponents.**

Take BBM: binary branching at rate $1$, standard Brownian motion, drift $-\mu$ with $\mu^2=2-\epsilon$, absorption at $0$. Linearize the survival equation ($u$ small): $\tfrac12u''+\mu u'+u=0$. Try $u(x)=e^{-\mu x}w(x)$:
$$\tfrac12 e^{-\mu x}\big(w''-\mu^2 w\big)+\mu e^{-\mu x}\big(w'-\mu w\big)+\mu e^{-\mu x}w \;\Rightarrow\; \tfrac12 w''+\Big(1-\tfrac{\mu^2}{2}\Big)w=0 .$$
With $1-\mu^2/2=\epsilon/2$ this is $w''+\epsilon w=0$, so $w(x)=\sin(\sqrt\epsilon\,x)$. The solution is positive exactly on $(0,\pi/\sqrt\epsilon)$: the linear theory allows a quasi-stationary cloud only inside a strip of width
$$L_\epsilon=\frac{\pi}{\sqrt\epsilon},$$
and the nonlinear term $-u^2$ must cut the wave off at the top. So a lineage survives only by reaching height $\approx L_\epsilon$.

**Cost of reaching the top.** For BBM with drift $\approx-\sqrt2$ the probability that any descendant of a particle at $x=O(1)$ ever reaches level $L$ decays like $e^{-\sqrt2 L}$ (the additive-martingale/Many-to-one estimate, since $\theta^*=\sqrt2$). Hence
$$\log Q(\epsilon,x)\approx-\sqrt2\,L_\epsilon=-\frac{\sqrt2\,\pi}{\sqrt\epsilon},$$
which is exactly the Gantert–Hu–Shi leading order. Everything the conjecture asks for lives in the $(1+o(1))$ here: the polynomial factor in $\epsilon$ and the constant $C$ come from the $O(1)$-thick nonlinear layer at the top of the strip, not from this estimate.

**Matching to $N$-selection.** In the quasi-stationary strip the particle density is proportional to $e^{\sqrt2 x}\sin(\pi x/L)$, so the population is
$$N\;\asymp\;\int_0^L e^{\sqrt2 x}\sin\!\Big(\frac{\pi x}{L}\Big)dx\;\asymp\;e^{\sqrt2 L}\quad\Longrightarrow\quad L\approx\frac{\log N}{\sqrt2}.$$
The speed deficit of a front confined to a strip of width $L$ is, from $v=\sqrt{2-\epsilon}\approx\sqrt2-\epsilon/(2\sqrt2)$ with $\epsilon=\pi^2/L^2$:
$$v_c-v_N\approx\frac{\pi^2}{2\sqrt2\,L^2}=\frac{\pi^2}{2\sqrt2}\cdot\frac{2}{\log^2N}=\frac{\pi^2}{\sqrt2\,\log^2 N}.$$
Take $N=10^{6}$: $\log N\approx13.8$, giving $v_c-v_N\approx 6.98/190.6\approx0.037$, a $2.6\%$ deficit off $v_c=1.414$ — enormous for a $10^{6}$-particle system, and the reason the correction was found numerically before it was proved. Replacing $\log N$ by $\log N+3\log\log N\approx13.8+7.9=21.7$ drops the prediction to $0.0148$; the discrepancy between these two numbers at accessible $N$ is precisely what the second-order theory (proved for BBM, open for general BRW) must explain.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*