---
id: 09-probability/bak-sneppen-model-critical-exponents
title: "Critical Exponents of the Bak-Sneppen Model"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Critical Exponents of the Bak-Sneppen Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/bak-sneppen-model-critical-exponents` · **Status:** open

## 1. Problem Statement / Conjecture

The Bak–Sneppen (BS) model is a Markov process on fitness configurations $x \in [0,1]^{\mathbb{Z}_N^d}$ in which, at each step, the site of minimal fitness and its nearest neighbours are assigned fresh independent $\mathrm{Unif}[0,1]$ values. Simulation shows that the process self-organizes: the empirical fitness distribution converges to something supported on $[f_c,1]$ with a numerically sharp threshold $f_c \approx 0.6670$ in $d=1$, and avalanche statistics obey power laws.

**The open problem.** Prove, rigorously and for the model as defined (no modification, no annealed approximation):

1. The threshold $f_c(d)$ exists, is strictly interior to $(0,1)$, and — for $d=1$ — determine it, or prove it is not algebraic / has no closed form.
2. The avalanche size distribution satisfies $P(s) \sim s^{-\tau}$ with a well-defined exponent $\tau$, and $\tau(1) \approx 1.073$.
3. The avalanche dimension $D$, correlation exponent $\nu$, and dynamical exponent $z$ exist and satisfy the scaling relations of Paczuski–Maslov–Bak, in particular $\tau_{\text{first}} = 2 - d/D$.
4. The upper critical dimension is $d_c = 4$: for $d \ge 4$ the exponents take the mean-field values $\tau = 3/2$, $f_c = 1/2$, $D = 4$.

A complete solution requires existence of the limits (not just tightness of finite-$N$ empirical measures), identification of the exponents as real numbers, and proof of the scaling relations as theorems rather than as consequences of an assumed scaling ansatz. A disproof would exhibit, e.g., logarithmic corrections destroying pure power-law behaviour in $d=1$, or non-existence of a sharp threshold.

## 2. Mathematical Foundations

**The process.** Fix $d \ge 1$, $N \in \mathbb{N}$, and the torus $\Lambda = (\mathbb{Z}/N\mathbb{Z})^d$. The state is $X(t) = (X_i(t))_{i \in \Lambda} \in [0,1]^\Lambda$, with $X(0)$ i.i.d. $\mathrm{Unif}[0,1]$. One step:

$$m(t) = \arg\min_{i \in \Lambda} X_i(t), \qquad X_j(t+1) = \begin{cases} U_j(t) & \|j - m(t)\|_1 \le 1,\\ X_j(t) & \text{otherwise,}\end{cases}$$

with $\{U_j(t)\}$ i.i.d. $\mathrm{Unif}[0,1]$, independent of the past. In $d=1$ exactly three sites are refreshed. The chain is Harris ergodic on $[0,1]^\Lambda$; write $\mu_N$ for its stationary law and $\rho_N$ for the one-site marginal of $\mu_N$.

**Threshold.** Define
$$f_c := \lim_{N\to\infty} \operatorname*{ess\,inf} \mathrm{supp}\,\rho_N \quad \text{(conjecturally } \rho_N \Rightarrow \mathrm{Unif}[f_c,1]\text{)}.$$

**Avalanches.** For $f \in (0,1)$, an *$f$-avalanche* started from a configuration whose minimum is just below $f$ is the run
$$S_f = \min\{t \ge 1 : \min_i X_i(t) > f\},$$
i.e. the number of updates until all fitnesses exceed $f$. The *avalanche critical value* is
$$p_c := \sup\{f : \mathbb{E}[S_f] < \infty \text{ on } \mathbb{Z}^d\}.$$

**Conjectured scaling.** At $f = f_c$,
$$P(S_{f_c} = s) \sim s^{-\tau}, \qquad \mathbb{E}[S_f] \sim (f_c - f)^{-\gamma}, \qquad s_{\max}(f) \sim (f_c-f)^{-1/\sigma},$$
and if $r$ is the spatial diameter of the avalanche cluster, $s \sim r^{D}$ with $D$ the *avalanche dimension*, $\xi \sim (f_c-f)^{-\nu}$, $t \sim r^{z}$. The standard relations (Paczuski, Maslov & Bak 1996) are
$$\tfrac{1}{\sigma} = \nu D, \qquad \gamma = \nu D\,(2-\tau), \qquad \tau_{\text{first}} = 2 - \frac{d}{D}, \qquad \tau_{\text{all}} = \frac{d}{D},$$
the last pair governing first-return and all-return times of the activity to a fixed site, and implying $\tau_{\text{first}} + \tau_{\text{all}} = 2$.

**Gap equation.** With $G(t) = \max_{s \le t} \min_i X_i(s)$ (the running maximum of the minimum),
$$\frac{dG}{dt} = \frac{1 - G(t)}{N^d\,\mathbb{E}[S_{G(t)}]},$$
which is the exact bookkeeping identity underlying the claim that the model drives itself to $f_c$ without parameter tuning ("self-organized criticality").

**Numerics ($d=1$).** $f_c = 0.66702(3)$ (Grassberger 1995), $\tau = 1.073(3)$, $D = 2.43(1)$, $\gamma \approx 2.7$, $\tau_{\text{all}} \approx 0.42$. In $d=2$, $f_c \approx 0.3286$, $\tau \approx 1.245$. Mean field: $f_c = 1/2$, $\tau = 3/2$, $D = 4$, $\gamma = 1$.

## 3. History & State of the Art (SOTA)

- **1993.** Bak and Sneppen introduce the model (*Phys. Rev. Lett.* **71**, 4083) as a caricature of punctuated equilibrium in evolution: a system with no tuning parameter that nevertheless sits at a critical point.
- **1994–1996.** de Boer, Derrida, Flyvbjerg, Jackson and Wettig solve the *random-neighbour* variant exactly, getting $f_c = 1/2$, $\tau = 3/2$. Maslov, Paczuski and Bak connect avalanche statistics to $1/f$ noise. Paczuski, Maslov and Bak (*Phys. Rev. E* **53**, 414) give the general avalanche/scaling framework and the relations above, extending it to depinning interfaces.
- **1995.** Grassberger's high-precision simulations fix $f_c = 0.66702(3)$ in $d=1$ and $\tau \approx 1.07$.
- **1996.** Boettcher and Paczuski obtain exact spatio-temporal correlation results for a solvable BS-type ("$M$-site") variant.
- **1998.** Marsili, De Los Rios and Maslov perform an expansion around the mean-field solution, arguing $d_c = 4$.
- **2001–2006.** The rigorous era begins: Barbay and Kenyon (SODA 2001) analyse the discrete BS model; Meester and Znamenski prove non-triviality and identify the limit behaviour (*Ann. Probab.* **31**, 2003); Gillett, Meester and Nuyens obtain explicit numerical bounds on avalanche critical values; Bandt (2005) relates a discrete BS variant to the classical contact process.
- **2012–present.** Meester and Sarkar prove genuine self-organized criticality for a *modified* BS model; work continues on complete-graph, tree and mean-field versions, where exact answers are reachable.

**SOTA summary.** Not one of the exponents $\tau, D, \nu, z$ in $d = 1,2,3$ is known rigorously, and $f_c(1)$ is known only to a few decimals numerically, with rigorous bounds far weaker.

## 4. Partial Results / Verified Cases

- **Mean-field / random-neighbour model (exactly solved).** Replace "nearest neighbours" by $M-1$ uniformly chosen sites. de Boer et al. (1994, 1995) show $f_c = 1/(M-1)$-type thresholds; for $M=2$, $f_c = 1/2$, $\tau = 3/2$, $\gamma = 1$, via a random-walk representation (Section 10). These are theorems modulo the annealed independence assumption, which is exact in the $N \to \infty$ random-neighbour limit.
- **Non-triviality.** Meester and Znamenski (*J. Stat. Phys.* **109**, 2002) prove for the discrete BS model that the threshold is bounded away from the trivial values, i.e. $0 < f_c < 1$.
- **Existence and identification of the limit.** Meester and Znamenski (*Ann. Probab.* **31**, 2003) prove convergence of the finite-$N$ stationary one-site marginals and identify the self-organized threshold with the avalanche critical value $p_c$ — a rigorous version of the folklore statement "the model tunes itself to $p_c$".
- **Explicit bounds.** Gillett, Meester and Nuyens (*Markov Process. Related Fields* **12**, 2006) obtain rigorous numerical upper and lower bounds on the avalanche critical values for the BS model on $\mathbb{Z}$ and on the complete graph; these bracket, but do not pin down, $0.667$.
- **Discrete/contact-process link.** Barbay and Kenyon (2001) and Bandt (2005) establish exact combinatorial and conjugacy results for the discrete-fitness BS model, transporting some contact-process technology.
- **Modified models.** Meester and Sarkar (*J. Stat. Phys.* **149**, 2012) prove self-organized criticality — convergence of the driving parameter to the critical point of an associated percolation-type model — for a modified BS dynamics.
- **Computational verification.** Exponents in $d = 1,2$ are reproduced across independent codes to $2$–$3$ significant figures over $10^{9}$–$10^{11}$ updates (Grassberger 1995; Garcia & Dickman 2004).

## 5. Principal Obstacles

- **No monotonicity, no coupling.** The dynamics is driven by a *global* extremal rule: the site updated depends on the entire configuration. Standard attractive-particle-system machinery (basic coupling, the contact-process comparison, FKG) requires local, monotone updating and fails here. Two configurations ordered coordinatewise do not stay ordered.
- **Non-Markovian activity.** The set of "active" sites (fitness $< f$) is not itself a Markov chain: whether an update creates activity depends on the global minimum's location relative to previously refreshed sites, producing long-range temporal memory and $1/f$ correlations.
- **No conserved quantity, no Abelian structure.** Unlike the abelian sandpile, BS has no group structure, no burning bijection and no matrix-tree formula; the stationary measure has no known product or determinantal representation, even in $d=1$.
- **Absence of an exact renormalization scheme.** Real-space RG for BS is uncontrolled: the coarse-grained rule is not of the same form as the microscopic rule. There is no field-theoretic action for BS derived from first principles comparable to the Reggeon field theory of directed percolation, so $\epsilon$-expansion below $d_c=4$ is heuristic.
- **The scaling ansatz is an assumption.** All exponent relations of Section 2 are consequences of a postulated single-scale form $P(s,f) = s^{-\tau}g(s(f_c-f)^{1/\sigma})$. Nothing rigorous establishes even the existence of a power law, let alone the collapse.
- **Exponent value is anomalous.** $\tau(1) = 1.073$ is barely above $1$, so $\mathbb{E}[S]$ diverges only logarithmically slowly in cutoff; finite-size corrections are strong and numerics cannot decide between $\tau = 1.073$ and, say, $\tau = 1$ with a logarithmic correction.

## 6. The Gap

Proven: existence of the stationary law for finite $N$; existence of the $N\to\infty$ marginal limit; equality of the self-organized threshold with $p_c$; strict non-triviality $0 < p_c < 1$; crude explicit bounds; full solution of the annealed/random-neighbour caricature.

Not proven, at any dimension $d \ge 1$: (i) that $\mathbb{E}[S_f]$ diverges as a *power* of $f_c - f$; (ii) that $P(S_{f_c} = s)$ is regularly varying, i.e. that $\tau$ exists at all; (iii) any numerical value of $f_c(1)$ beyond weak bounds; (iv) any of $\tau, D, \nu, z$; (v) that $d_c = 4$.

The precise barrier is the step from *"the process converges to a threshold"* to *"the process at that threshold has regularly varying avalanche statistics"*. This is the analogue of proving that critical percolation clusters have power-law size distribution — but without percolation's independence, monotonicity, or duality. A plausible minimal target: prove $\liminf s^{\tau'}P(S_{f_c}=s) > 0$ for some explicit $\tau' > 1$, i.e. a rigorous one-sided power bound.

## 7. Current Research (as of June 2026)

- **Rigorous probability on tractable geometries.** Complete graphs, star graphs, trees and one-dimensional discrete-fitness versions remain the main arena where theorems are provable; Dutch (VU Amsterdam / Leiden, in the Meester tradition), Israeli and US groups (Ben-Ari, Roitershtein and coauthors on "species survival" chains) continue extracting exact thresholds and mixing rates for these. *(frontier — verify)*
- **Contact-process comparison.** Sharpening the Bandt-type conjugacy so that sharpness-of-phase-transition tools (Duminil-Copin–Raoufi–Tassion randomized-algorithm method) can be imported to BS-type extremal dynamics. This is the most concrete route to a rigorous $f_c$ with sharp behaviour. *(frontier — verify)*
- **High-precision numerics.** Multi-billion-update simulations with improved finite-size scaling collapse aimed at distinguishing $\tau = 1.073$ from $\tau = 1$ plus logarithmic corrections, and at settling $d_c = 4$ by direct simulation in $d = 3,4,5$. *(frontier — verify)*
- **Extremal-dynamics universality.** Whether BS, invasion percolation and interface depinning share a universality class remains a working hypothesis; recent work maps BS avalanches onto records/extremes processes and onto quenched Edwards–Wilkinson depinning.
- **Non-equilibrium field theory.** Attempts to write an effective action for extremal dynamics (functional RG for depinning, adapted) to justify $d_c = 4$. *(frontier — verify)*

## 8. Future Work

- **Prove regular variation of $S_{f_c}$.** Even a two-sided bound $c_1 s^{-a} \le P(S=s) \le c_2 s^{-b}$ with $1 < b \le a$ would be the first rigorous statement of criticality in the original model.
- **Sharpen $p_c$ bounds.** Improve the Gillett–Meester–Nuyens interval by finite-window renormalization to bracket $0.667$ within $\pm 0.01$; this is a computer-assisted-proof-shaped problem.
- **Establish $d_c = 4$.** A lace-expansion or comparison argument for the high-dimensional model, where mean-field behaviour should be provable, in analogy with high-$d$ percolation (Hara–Slade).
- **Identify the correct solvable deformation.** Find a BS variant that (a) is exactly solvable and (b) is provably in the same universality class as BS, so that exponents transfer.
- **Rule out or confirm log corrections.** Because $\tau(1)-1 \approx 0.073$ is small, a rigorous or high-precision argument distinguishing genuine anomalous exponent from marginal behaviour would settle a long-standing numerical ambiguity.

## 9. Key References

- **[Foundational]** P. Bak and K. Sneppen. *Punctuated equilibrium and criticality in a simple model of evolution.* Physical Review Letters **71**(24), 4083–4086, 1993.
- **[Foundational]** J. de Boer, B. Derrida, H. Flyvbjerg, A. D. Jackson and T. Wettig. *Simple model of self-organized biological evolution.* Physical Review Letters **73**(6), 906–909, 1994.
- **[Foundational]** M. Paczuski, S. Maslov and P. Bak. *Avalanche dynamics in evolution, growth, and depinning models.* Physical Review E **53**(1), 414–443, 1996.
- **[SOTA / Recent]** P. Grassberger. *The Bak–Sneppen model for punctuated evolution.* Physics Letters A **200**(3–4), 277–282, 1995.
- **[SOTA / Recent]** R. Meester and D. Znamenski. *Limit behavior of the Bak–Sneppen evolution model.* The Annals of Probability **31**(4), 1986–2002, 2003.
- **[SOTA / Recent]** R. Meester and D. Znamenski. *Non-triviality of a discrete Bak–Sneppen evolution model.* Journal of Statistical Physics **109**(5–6), 987–1004, 2002.
- **[SOTA / Recent]** J. Barbay and C. Kenyon. *On the discrete Bak–Sneppen model of self-organized criticality.* Proceedings of the 12th ACM–SIAM Symposium on Discrete Algorithms (SODA), 928–933, 2001.
- **[SOTA / Recent]** R. Meester and A. Sarkar. *Rigorous self-organised criticality in a modified Bak–Sneppen model.* Journal of Statistical Physics **149**(5), 964–968, 2012.
- **[SOTA / Recent]** M. Marsili, P. De Los Rios and S. Maslov. *Expansion around the mean-field solution of the Bak–Sneppen model.* Physical Review Letters **80**(7), 1457–1460, 1998.
- **[SOTA / Recent]** C. Bandt. *The discrete evolution model of Bak and Sneppen is conjugate to the classical contact process.* Journal of Statistical Physics **120**(3–4), 685–693, 2005.
- **[Survey]** H. J. Jensen. *Self-Organized Criticality: Emergent Complex Behavior in Physical and Biological Systems.* Cambridge University Press, 1998.
- **[Survey]** R. Dickman, M. A. Muñoz, A. Vespignani and S. Zapperi. *Paths to self-organized criticality.* Brazilian Journal of Physics **30**(1), 27–41, 2000.
- **[Survey]** P. Bak. *How Nature Works: The Science of Self-Organized Criticality.* Copernicus/Springer, 1996.

## 10. Worked Example / Concrete Special Case

**The random-neighbour ($M=2$) model, solved exactly.** At each step, delete the global minimum and one *uniformly chosen* other site, and give both fresh $\mathrm{Unif}[0,1]$ values. As $N \to \infty$, the non-minimal fitnesses become i.i.d. with common law $\rho$, so the count of *active* sites (fitness $< f$) is a Markov chain.

Let $n_t$ be the number of sites with fitness $< f$. One update removes the minimum (always active, so $-1$) and replaces two sites by uniforms, each landing below $f$ with probability $f$ independently. Hence

$$n_{t+1} - n_t = -1 + B, \qquad B \sim \mathrm{Bin}(2,f), \qquad \mathbb{E}[n_{t+1}-n_t] = 2f - 1.$$

The avalanche is the excursion of $n_t$ from $1$ back to $0$. The drift vanishes exactly at

$$\boxed{f_c = \tfrac12}$$

so the walk is subcritical for $f < 1/2$ and supercritical for $f > 1/2$: this is the mean-field threshold, and the gap equation drives $G(t) \uparrow 1/2$.

**Mean avalanche size.** For $f < 1/2$ the walk has drift $-(1-2f)$; by Wald's identity applied to the first passage to $0$ from $1$,
$$\mathbb{E}[S_f] = \frac{1}{1-2f} \quad \Longrightarrow \quad \gamma = 1 .$$

**Avalanche exponent.** At $f = f_c = 1/2$ the increments are
$$P(-1) = \tfrac14, \quad P(0) = \tfrac12, \quad P(+1) = \tfrac14,$$
a lazy simple random walk with zero mean and finite variance. The avalanche length is its first return time $T$ to $0$. Stripping the lazy steps, $T$ is a geometric sum of first-return times of an unbiased $\pm1$ walk, for which
$$P(T_{\pm} = 2n) = \frac{1}{2n-1}\binom{2n}{n}2^{-2n} \;\sim\; \frac{1}{2\sqrt{\pi}}\,n^{-3/2},$$
using Stirling. Laziness rescales time by a constant factor and does not change the tail exponent, so
$$P(S = s) \sim C\, s^{-3/2}, \qquad \tau_{\mathrm{MF}} = \tfrac32 ,$$
consistent with $\gamma = \nu D(2-\tau) = 1$ once $\nu D = 2$, i.e. $1/\sigma = 2$ and $D = 4$ at $d = d_c = 4$ with $\nu = 1/2$.

**What breaks in $d = 1$.** The same bookkeeping fails because the two refreshed neighbours are *spatially adjacent* to the minimum, so freshly created active sites are correlated with the existing active cluster: activity is confined to a growing contiguous region rather than spread uniformly. The counting process $n_t$ is no longer Markov, the increments are not i.i.d., and the random-walk argument collapses. Numerically this shifts $f_c$ from $0.5$ to $0.667$ and $\tau$ from $3/2$ to $1.073$ — a drop that no controlled perturbation of the above computation has yet reproduced. Proving that $1.073\ldots$ is the exponent, or that any exponent exists, is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*