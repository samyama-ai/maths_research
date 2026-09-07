---
id: 09-probability/multi-type-contact-process-stationary-measure
title: "Stationary Measure for the Multi-Type Contact Process"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Stationary Measure for the Multi-Type Contact Process

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/multi-type-contact-process-stationary-measure` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fix $d \ge 1$ and $k \ge 2$ types. The multi-type contact process on $\mathbb{Z}^d$ is the Markov process $\xi_t : \mathbb{Z}^d \to \{0,1,\dots,k\}$ in which a site of type $i \ge 1$ dies at rate $1$ and an empty site is colonised by each neighbouring type-$i$ site at rate $\lambda_i$. The problem is to classify the **extremal stationary (invariant) distributions** of this process, and in particular:

- **Symmetric (neutral) case $\lambda_1 = \dots = \lambda_k = \lambda > \lambda_c(d)$.** Does there exist a translation-invariant stationary measure $\nu$ with $\nu(\xi(0)=i) > 0$ for at least two types $i$ (*coexistence*)? The standing conjecture is the **voter-model dichotomy**: coexistence fails for $d = 1, 2$ (the system *clusters*, and every translation-invariant stationary measure is a mixture of $\delta_{\emptyset}$ and the one-type upper invariant measures $\bar\nu_i$), and coexistence holds for $d \ge 3$, where a one-parameter family $\{\nu_\alpha\}_{\alpha \in [0,1]}$ of extremal translation-invariant stationary measures exists, indexed by the type-1 density.
- **Asymmetric case $\lambda_1 > \lambda_2$.** Conjecture (*"the stronger type wins"*): if $\lambda_1 > \lambda_c(d)$, then $\xi_t$ started from any initial configuration converges to a mixture of $\delta_\emptyset$ and $\bar\nu_1$; no stationary measure charges type 2.

A complete solution means: for every $d$, $k$, and rate vector $(\lambda_i)$, an exhaustive description of the set $\mathcal{I}$ of stationary measures together with a complete convergence theorem identifying the limit law from every initial configuration.

## 2. Mathematical Foundations

**State space and generator.** Let $X = \{0,1,\dots,k\}^{\mathbb{Z}^d}$ with the product topology; $X$ is compact and the process is Feller. For $\xi \in X$, $x \in \mathbb{Z}^d$, $i \in \{0,\dots,k\}$, write $\xi^{x,i}$ for the configuration equal to $\xi$ off $x$ with $\xi^{x,i}(x) = i$. The generator acts on cylinder functions $f$ by

$$
\mathcal{L}f(\xi) \;=\; \sum_{x \in \mathbb{Z}^d} \Big[ \mathbf{1}_{\{\xi(x)\neq 0\}}\big(f(\xi^{x,0}) - f(\xi)\big) \;+\; \mathbf{1}_{\{\xi(x)= 0\}} \sum_{i=1}^{k} \lambda_i n_i(x,\xi)\,\big(f(\xi^{x,i}) - f(\xi)\big) \Big],
$$

where $n_i(x,\xi) = \\#\{y : \|y-x\|_1 = 1,\ \xi(y) = i\}$. A probability measure $\nu$ on $X$ is stationary iff $\int \mathcal{L}f \, d\nu = 0$ for all cylinder $f$; $\mathcal{I}$ denotes the (compact, convex) set of such $\nu$, $\mathcal{I}_e$ its extreme points, and $\mathcal{S}$ the translation-invariant measures.

**Reduction to the one-type process.** The *shadow* $\eta_t(x) = \mathbf{1}_{\{\xi_t(x) \neq 0\}}$ is, in the symmetric case $\lambda_i \equiv \lambda$, exactly the basic contact process with parameter $\lambda$. Its critical value $\lambda_c(d)$ satisfies $\lambda_c(1) \approx 1.6494$ and $1/(2d) \le \lambda_c(d)\,$ with $2d\lambda_c(d) \to 1$; by Bezuidenhout–Grimmett the critical process dies out, so for $\lambda > \lambda_c$ the upper invariant measure $\bar\nu$ (limit from all-occupied) is nontrivial and, by Harris duality plus the complete convergence theorem, $\mathcal{I}_e = \{\delta_\emptyset, \bar\nu\}$ for the one-type process.

**Neutral case as a voter model on a random medium.** For $\lambda_i \equiv \lambda$, condition on the shadow $\eta_\cdot$: the types are assigned by a genealogical rule in which each occupied site inherits its type from the site that gave birth to it. Types therefore evolve by a *voter-like* mechanism carried on the space-time backbone of the contact process, and the natural dual object is a system of **coalescing ancestral lineages** $\{A_t^x\}$ on the contact-process backbone. Coexistence is equivalent to *non-coalescence*: writing $\tau_{x,y}$ for the coalescence time of the lineages started at $x,y$ (given both survive),

$$
\text{coexistence} \iff \mathbb{P}\big(\tau_{x,y} = \infty \mid \text{both lineages survive}\big) > 0 .
$$

For the ordinary voter model the corresponding lineages are independent random walks, and $\mathbb{P}(\text{no coalescence}) > 0$ iff the walk is transient, i.e. $d \ge 3$ (Holley–Liggett). The conjecture asserts that the contact-process backbone does not change this dichotomy.

**Interface (one dimension).** For $d=1$, $k=2$ with the *heaviside* start $\xi_0(x) = 1$ for $x \le 0$, $=2$ for $x>0$, define
$$
r_t = \sup\{x : \xi_t(x) = 1\}, \qquad l_t = \inf\{x : \xi_t(x) = 2\}, \qquad I_t = [l_t, r_t],
$$
the *interface*. Tightness of $|I_t|$ is the key structural statement in $d=1$.

## 3. History & State of the Art (SOTA)

- **1974–1990.** Harris introduces the contact process; Liggett's *Interacting Particle Systems* (1985) develops duality and the classification $\mathcal{I}_e = \{\delta_\emptyset, \bar\nu\}$ for one type. Bezuidenhout and Grimmett (*Ann. Probab.* 18, 1990) prove the critical process dies out, closing the last gap in the one-type phase diagram.
- **1991.** Durrett and Møller (*Probab. Theory Related Fields* 88) prove a complete convergence theorem for a two-species competition model, the first multi-type result of this shape.
- **1992.** Neuhauser, *Ergodic theorems for the multitype contact process* (*PTRF* 91, 467–506), is the foundational paper: she proves the *stronger type wins* theorem for $\lambda_1 > \lambda_2$ with $\lambda_1 > \lambda_c$, and analyses the neutral case, establishing clustering in $d \le 2$ from translation-invariant initial laws and coexistence in $d \ge 3$ under a large-$\lambda$ (or supercritical-percolation-of-the-backbone) hypothesis.
- **1997–2009.** Durrett and Neuhauser (*Ann. Appl. Probab.* 7, 1997) obtain coexistence for competition models with fast stirring via reaction–diffusion limits. Chan, Durrett and Lanchier (*Ann. Appl. Probab.* 19, 2009) show coexistence for a multitype contact process with seasons, where the neutral degeneracy is broken by time-varying rates.
- **2010–2016.** Valesin (*Electron. J. Probab.* 15, 2010) analyses extinction and the interface on $\mathbb{Z}$; Andjel, Mountford, Pimentel and Valesin (*Bernoulli* 16, 2010) prove **tightness of the one-dimensional interface**, a long-standing question; Mountford and Valesin obtain a functional CLT for the interface (ALEA, 2016).
- **Present.** The neutral $d \ge 3$ coexistence problem for *all* $\lambda > \lambda_c$, and the full description of $\mathcal{I}_e$ in $d \ge 3$, remain open.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $k$ types, $\lambda_1 > \lambda_i$ for $i\ge2$, $\lambda_1 > \lambda_c(d)$, any $d$ | **Solved** (Neuhauser 1992): weaker types die out; $\mathcal{I}_e = \{\delta_\emptyset,\bar\nu_1\}$. |
| $\lambda_i \equiv \lambda \le \lambda_c(d)$ | **Solved**: $\mathcal{I} = \{\delta_\emptyset\}$ (Bezuidenhout–Grimmett). |
| $d = 1$, neutral, translation-invariant start | **Solved**: clustering; no coexisting translation-invariant stationary measure. |
| $d = 2$, neutral | **Solved** (Neuhauser 1992): clustering from translation-invariant product starts. |
| $d \ge 3$, neutral, $\lambda$ large | **Proved**: a one-parameter family of coexisting stationary measures exists. |
| $d \ge 3$, neutral, $\lambda_c < \lambda < \infty$ general | **Open**. |
| $d = 1$, heaviside start | Interface $|I_t|$ is **tight** in $t$ (Andjel–Mountford–Pimentel–Valesin 2010); FCLT for $r_t$ with diffusive scaling (Mountford–Valesin 2016). |
| Fast-stirring / rapid-mixing perturbations, $d \ge 2$ | Coexistence via reaction–diffusion PDE limits (Durrett–Neuhauser 1997; Cox–Durrett–Perkins 2013). |
| Non-neutral with seasonality or spatial heterogeneity | Coexistence proved in explicit parameter windows (Chan–Durrett–Lanchier 2009). |
| Homogeneous trees $\mathbb{T}_d$, neutral | Coexistence (backbone is transient), analogous to $d\ge3$. |

## 5. Principal Obstacles

- **Loss of attractiveness.** With $k \ge 2$ types the natural partial order on $\{0,\dots,k\}$ is not preserved: increasing type-1 mass decreases type-2 mass. Coupling and monotonicity — the engines behind the one-type theory (existence of $\bar\nu$, monotone limits, correlation inequalities) — are unavailable.
- **No self-duality.** The one-type contact process is self-dual, which yields the complete convergence theorem. The multi-type process has only a *conditional* duality with coalescing lineages on a random backbone, and the backbone is not independent of the lineages.
- **Correlated, non-Markov lineages.** Ancestral lineages of the neutral process are random walks *constrained to a supercritical oriented-percolation cluster*. They are not Markov on $\mathbb{Z}^d$, are mutually dependent through the shared environment, and their transience/recurrence in $d = 3$ near $\lambda_c$ is not accessible by Fourier or Green-function methods.
- **Near-criticality.** For $\lambda \downarrow \lambda_c$ the backbone becomes sparse and long-range correlated; large-$\lambda$ arguments (Peierls contours, block constructions with high-density blocks) break down precisely where the answer is most delicate. No renormalisation scheme is known that preserves the neutral symmetry while pushing $\lambda$ down to $\lambda_c$.
- **Degenerate neutral fixed point.** Mean-field and reaction–diffusion approximations produce a *line* of fixed points (Section 10), so hydrodynamic/PDE methods that succeed for strictly competitive systems give no information in the neutral case.

## 6. The Gap

Proven: (i) the full asymmetric case, (ii) clustering in $d \le 2$, (iii) coexistence in $d \ge 3$ **for $\lambda$ large**. Conjectured: coexistence in $d \ge 3$ for **every** $\lambda > \lambda_c(d)$, with $\mathcal{I}_e \cap \mathcal{S} = \{\nu_\alpha : \alpha \in [0,1]\}$.

The precise missing step is a **transience statement for a single ancestral lineage in the supercritical contact-process backbone at all $\lambda > \lambda_c$, uniform enough to give non-coalescence of two lineages in $d \ge 3$**. Equivalently: show that the Green function of the pair-difference lineage process on the backbone is finite for all supercritical $\lambda$ when $d\ge3$. Existing proofs supply this only when the backbone density is close to $1$, where block constructions turn the lineage into a perturbation of simple random walk.

## 7. Current Research (as of June 2026)

- **Ancestral-lineage random walks in random environment.** Continuing programme (Birkner, Černý, Depperschmidt and collaborators) on directed random walks in the oriented-percolation cluster, proving CLTs and quenched invariance principles; extending these to *pairs* of lineages is the natural route to the $d \ge 3$ coexistence theorem. *(frontier — verify)*
- **Interface geometry.** Brazilian and Swiss schools (IMPA, UFRJ, IME-USP, EPFL; Valesin, Mountford, Pimentel and coauthors) push the one-dimensional interface results toward $d = 2$, where a tight interface would give an independent proof of clustering with quantitative cluster-size exponents.
- **Voter-model perturbation theory.** Cox–Durrett–Perkins machinery is being applied to weakly asymmetric multi-type contact processes, $\lambda_2 = \lambda_1(1 - \varepsilon)$, to determine the crossover scale $\varepsilon \sim L^{-\theta}$ at which "the stronger wins" and neutral clustering compete. *(frontier — verify)*
- **Multi-type processes on random graphs and trees** (Galton–Watson trees, configuration model), where transience of lineages is generic and coexistence is expected to be the rule; and multi-type processes with mutation, which admit nontrivial stationary measures with all types present.

## 8. Future Work

1. Prove non-coalescence of two backbone lineages for all $\lambda > \lambda_c(d)$, $d \ge 3$ — the decisive open step.
2. Establish a **complete convergence theorem** in the neutral $d \ge 3$ case: identify the limit from arbitrary (non-translation-invariant) starts as a mixture of $\delta_\emptyset$ and $\{\nu_\alpha\}$.
3. Determine clustering exponents in $d=1,2$: is the typical cluster diameter at time $t$ of order $t^{1/2}$ ($d=1$) and $t^{1/2}$ up to logarithms ($d=2$), matching the voter model?
4. Settle the critical dimension: is $d=2$ genuinely marginal, with coexistence recovered on $\mathbb{Z}^2$ under long-range ($\alpha$-stable) birth kernels?
5. Prove that at $\lambda = \lambda_c$ all multi-type stationary measures are $\delta_\emptyset$ in every dimension.

## 9. Key References

- **[Foundational]** C. Neuhauser. *Ergodic theorems for the multitype contact process.* Probability Theory and Related Fields, 91:467–506, 1992.
- **[Foundational]** T. M. Liggett. *Interacting Particle Systems.* Springer, Grundlehren 276, 1985.
- **[Foundational]** T. M. Liggett. *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes.* Springer, Grundlehren 324, 1999.
- **[Foundational]** C. Bezuidenhout and G. Grimmett. *The critical contact process dies out.* Annals of Probability, 18(4):1462–1482, 1990.
- **[Foundational]** R. Durrett and A. M. Møller. *Complete convergence theorem for a competition model.* Probability Theory and Related Fields, 88:121–136, 1991.
- **[SOTA / Recent]** E. Andjel, T. Mountford, L. P. R. Pimentel and D. Valesin. *Tightness for the interface of the one-dimensional contact process.* Bernoulli, 16(4):909–925, 2010.
- **[SOTA / Recent]** D. Valesin. *Multitype contact process on $\mathbb{Z}$: extinction and interface.* Electronic Journal of Probability, 15:2220–2260, 2010.
- **[SOTA / Recent]** T. Mountford and D. Valesin. *Functional central limit theorem for the interface of the symmetric multitype contact process.* ALEA, Latin American Journal of Probability and Mathematical Statistics, 13:481–519, 2016.
- **[SOTA / Recent]** N. Lanchier and C. Neuhauser. *Stochastic spatial models of host–pathogen and host–mutualist interactions I.* Annals of Applied Probability, 16(1):448–474, 2006.
- **[SOTA / Recent]** Y. Chan, R. Durrett and N. Lanchier. *Coexistence for a multitype contact process with seasons.* Annals of Applied Probability, 19(5):1921–1943, 2009.
- **[Survey]** R. Durrett and C. Neuhauser. *Coexistence results for some competition models.* Annals of Applied Probability, 7(1):10–45, 1997.
- **[Survey]** J. T. Cox, R. Durrett and E. A. Perkins. *Voter model perturbations and reaction diffusion equations.* Astérisque 349, Société Mathématique de France, 2013.
- **[Survey]** R. Durrett. *Ten Lectures on Particle Systems.* In: Lectures on Probability Theory (Saint-Flour XXIII), Lecture Notes in Math. 1608, Springer, 1995.

## 10. Worked Example / Concrete Special Case

**Mean-field limit and the degeneracy of neutrality.** Replace $\mathbb{Z}^d$ by the complete graph on $N$ sites with birth rate $\lambda/N$ per ordered pair. Let $u_i$ be the density of type $i$, $u_0 = 1 - u_1 - u_2$. The law of large numbers gives

$$
\dot u_1 = \lambda u_1 (1 - u_1 - u_2) - u_1, \qquad \dot u_2 = \lambda u_2 (1 - u_1 - u_2) - u_2 .
$$

Let $s = u_1 + u_2$ (total occupancy). Adding, $\dot s = \lambda s(1-s) - s$, whose stable fixed point for $\lambda > 1$ is $s^* = 1 - 1/\lambda$ — the mean-field analogue of $\bar\nu$. For the ratio $p = u_1/s$,

$$
\dot p = \frac{\dot u_1 s - u_1 \dot s}{s^2} = \frac{\big(\lambda u_1 u_0 - u_1\big)s - u_1\big(\lambda s u_0 - s\big)}{s^2} = 0 .
$$

**The type ratio is a conserved quantity.** The ODE therefore has an entire *line* of fixed points $\{(u_1,u_2) : u_1 + u_2 = s^*,\ u_i \ge 0\}$, one for each $p \in [0,1]$: neutral competition is non-hyperbolic, and no linear stability analysis decides anything. This is exactly why PDE and perturbative methods give no leverage in Section 5.

**Finite $N$: the fluctuation decides.** At finite $N$ the conserved quantity becomes a martingale. Conditioning on $s \approx s^*$, $p_t$ is a bounded martingale with quadratic variation rate $\approx c\, p(1-p)/(N s^*)$ — a Wright–Fisher diffusion. Hence $p_t \to \{0,1\}$ a.s., and the fixation time is $O(N)$: **on any finite mean-field system coexistence fails**, and the stationary law charges only one type (or $\emptyset$).

**Interpretation on $\mathbb{Z}^d$.** The same martingale is present: on $\mathbb{Z}^d$ the type ratio measured through the dual lineages is a martingale whose quadratic variation accumulates at rate proportional to the *coalescence rate* of two lineages. In $d = 1,2$ the lineages, being recurrent-like on the backbone, coalesce a.s.; the martingale accumulates infinite variation and fixates locally — clustering. In $d \ge 3$ transience should make the total accumulated variation finite, so $p_t$ converges to a genuinely random limit in $(0,1)$ with positive probability — coexistence, and a stationary measure $\nu_\alpha$ for each $\alpha$. Converting "should" into a theorem for all $\lambda > \lambda_c$ is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*