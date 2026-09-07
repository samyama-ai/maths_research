---
id: 09-probability/random-energy-model-phase-transition-exact-solutions
title: "Random Energy Model Phase Transition Exact Solutions"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Energy Model Phase Transition Exact Solutions

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-energy-model-phase-transition-exact-solutions` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Derrida's Random Energy Model (REM) assigns to each of the $2^N$ spin configurations $\sigma\in\Sigma_N=\{-1,1\}^N$ an independent Gaussian energy of variance $N$. The programme is to determine **exactly**, with proof, every level of the model's thermodynamic description:

1. **Free energy (solved).** $\lim_N N^{-1}\log Z_{N,\beta}$ exists a.s. and equals an explicit function with a phase transition at $\beta_c=\sqrt{2\log 2}$.
2. **Fluctuations (solved).** The exact limit law of $\log Z_{N,\beta}-\mathbb{E}\log Z_{N,\beta}$ in each of the four regimes $\beta<\beta_c/2$, $\beta_c/2<\beta<\beta_c$, $\beta=\beta_c$, $\beta>\beta_c$.
3. **Gibbs measure (solved).** The weak limit of the ordered Gibbs weights below $\beta_c$ is Poisson–Dirichlet $\mathrm{PD}(\beta_c/\beta)$.
4. **Dynamics (partially open).** Exact ageing and metastability statements for Glauber/Metropolis dynamics at all time scales and all temperatures, including the critical window.
5. **Universality (open).** The precise class of correlated random fields whose extremes and free energy are governed by REM asymptotics ("REM universality class"), including the Fyodorov–Hiary–Keating freezing picture for $\log|\zeta(\tfrac12+it)|$.

A complete resolution means rigorous limit theorems, not physics-level replica or one-step-replica-symmetry-breaking (1RSB) computations. Items 1–3 are theorems; items 4–5 are the live open frontier, which is why the page is filed as *solved-recently* rather than *open*.

## 2. Mathematical Foundations

**Model.** Let $(X_\sigma)_{\sigma\in\Sigma_N}$ be i.i.d. standard Gaussians and set $H_N(\sigma)=-\sqrt N X_\sigma$, so $\mathbb{E}[H_N(\sigma)^2]=N$ and $\mathbb{E}[H_N(\sigma)H_N(\tau)]=N\mathbf 1_{\sigma=\tau}$. The partition function and free energy are
$$Z_{N,\beta}=\sum_{\sigma\in\Sigma_N} e^{\beta\sqrt N X_\sigma},\qquad f_N(\beta)=\frac1N\log Z_{N,\beta}.$$

**Theorem (Derrida 1981; Eisele 1983; Olivieri–Picco 1984).** Almost surely and in $L^1$,
$$f(\beta)=\lim_{N\to\infty}f_N(\beta)=\begin{cases}\log 2+\dfrac{\beta^2}{2}, & \beta\le\beta_c=\sqrt{2\log 2},\\[4pt] \beta\sqrt{2\log 2}, & \beta>\beta_c.\end{cases}$$
$f$ is $C^1$ but not $C^2$ at $\beta_c$: the transition is *third order* in Ehrenfest's classification (Eisele's title), with the entropy $s(\beta)=f-\beta f'$ vanishing identically for $\beta\ge\beta_c$ — "entropy crisis".

**Extremes.** With $n=2^N$ and
$$c_N=\sqrt{2\log 2}\,N-\frac{\log(N\log 2)+\log 4\pi}{2\sqrt{2\log 2}},$$
the point process $\sum_\sigma \delta_{\sqrt N X_\sigma-c_N}$ converges to a Poisson point process on $\mathbb{R}$ with intensity $\beta_c e^{-\beta_c y}\,dy$ (Gumbel/extremal type I). Hence
$$e^{-\beta c_N}Z_{N,\beta}\ \Longrightarrow\ \sum_i e^{\beta y_i}<\infty \quad (\beta>\beta_c),$$
a completely asymmetric $\alpha$-stable random variable with index $\alpha=\beta_c/\beta\in(0,1)$.

**Gibbs measure.** $\mu_{N,\beta}(\sigma)=e^{\beta\sqrt N X_\sigma}/Z_{N,\beta}$. For $\beta>\beta_c$ the decreasing rearrangement of $(\mu_{N,\beta}(\sigma))_\sigma$ converges to Poisson–Dirichlet $\mathrm{PD}(\alpha)$, $\alpha=\beta_c/\beta$ (Ruelle 1987). The overlap $R_{12}=N^{-1}\sum_i\sigma_i\tau_i$ under $\mu^{\otimes2}_{N,\beta}$ satisfies
$$P(q)\ \Longrightarrow\ \Big(1-\tfrac{\beta_c}{\beta}\Big)\delta_0+\tfrac{\beta_c}{\beta}\,\delta_1,$$
the canonical 1RSB order parameter, with Parisi parameter $m=\beta_c/\beta$.

**Fluctuations (Bovier–Kurkova–Löwe 2002).** Writing $\alpha=\beta_c/\beta$:
- $\beta<\beta_c/2$: $\ \sqrt{2^N e^{-\beta^2N}}\,(Z_{N,\beta}/\mathbb{E}Z_{N,\beta}-1)\Rightarrow \mathcal N(0,1)$; $\log Z_{N,\beta}$ has Gaussian fluctuations of exponentially small order.
- $\beta_c/2<\beta<\beta_c$: after centering by $N(\log 2+\beta^2/2)$ minus explicit $O(1)$ corrections, $\log Z_{N,\beta}$ converges to a completely asymmetric $\alpha$-stable law with $\alpha=\beta_c/\beta\in(1,2)$.
- $\beta=\beta_c$: an extra $-\tfrac12\log N$-type correction appears and the limit is $1$-stable.
- $\beta>\beta_c$: $\log Z_{N,\beta}-\beta c_N\Rightarrow \log\!\big(\sum_i e^{\beta y_i}\big)$, a log-$\alpha$-stable law, $\alpha<1$.

**GREM/CREM.** Derrida's generalised REM adds a hierarchy: energies indexed by a tree with $n$ levels, weights $a_1,\dots,a_n$ ($\sum a_k=1$) and branching exponents $p_1,\dots,p_n$. The free energy is the Legendre-type concave-hull recipe of Derrida–Gardner (1986), made rigorous by Bovier–Kurkova (2004), whose continuous version (CREM) depends only on the concave hull of the covariance function $A(x)=\lim N^{-1}\mathbb{E}[H(\sigma)H(\tau)]$ at overlap $x$.

## 3. History & State of the Art (SOTA)

- **1980–81.** Derrida introduces the REM as the $p\to\infty$ limit of the $p$-spin Sherrington–Kirkpatrick model (PRL 45, 79; Phys. Rev. B 24, 2613), computes $f(\beta)$ and identifies the frozen phase.
- **1983–84.** Eisele gives the first rigorous proof (CMP 90) and names the transition third order; Olivieri–Picco (CMP 96) prove existence of the thermodynamic limit and large-deviation refinements.
- **1986.** Derrida–Gardner solve the GREM.
- **1987.** Ruelle reformulates REM/GREM via Poisson cascades — the birth of *Ruelle probability cascades*, later shown by Bolthausen–Sznitman (1998) to be the unique measures invariant under the abstract cavity/Bolthausen–Sznitman coalescent, and used as the ansatz in Panchenko's proof of the Parisi ultrametricity theorem.
- **1989.** Galves–Martinez–Picco obtain first fluctuation results for REM/GREM.
- **2002.** Bovier–Kurkova–Löwe give the complete fluctuation theory in all regimes, and transfer it to $p$-spin SK models.
- **2002–03.** Ben Arous–Bovier–Gayrard prove ageing and metastability for random-hopping (trap) dynamics of the REM.
- **2012–2019.** Fyodorov–Hiary–Keating export the REM/freezing heuristic to $\log|\zeta|$ and random matrix characteristic polynomials; Arguin–Belius–Bourgade–Radziwiłł–Soundararajan prove the leading-order prediction.
- **2019.** Gayrard proves ageing for genuine Metropolis dynamics of the REM.

## 4. Partial Results / Verified Cases

| Object | Status | Parameter range |
|---|---|---|
| $f(\beta)$ | proved | all $\beta\ge0$, a.s. and in $L^1$ |
| Order of transition | proved third order | at $\beta_c=\sqrt{2\log2}\approx1.1774$ |
| CLT for $Z/\mathbb{E}Z$ | proved | $0\le\beta<\beta_c/2\approx0.5887$ |
| $\alpha$-stable fluctuations | proved | $\beta_c/2<\beta<\beta_c$, $\alpha=\beta_c/\beta\in(1,2)$ |
| Critical fluctuations | proved | $\beta=\beta_c$ (1-stable, extra $\log N$ correction) |
| Log-stable fluctuations | proved | $\beta>\beta_c$, $\alpha=\beta_c/\beta<1$ |
| Gibbs weights $\to \mathrm{PD}(\alpha)$, $P(q)$ 1RSB | proved | $\beta>\beta_c$ |
| GREM, finitely many levels | proved | any $n<\infty$, arbitrary $(a_k,p_k)$ |
| CREM | proved | any covariance $A:[0,1]\to[0,1]$, free energy via concave hull $\hat A$ |
| $p$-spin $\to$ REM | proved | $p\to\infty$ with $\beta$ fixed; low-temperature REM-like behaviour for large $p$ (Talagrand) |
| Ageing, random-hopping dynamics | proved | $\beta>\beta_c$, time scales $e^{cN}$, arcsine-law limit |
| Ageing, Metropolis dynamics | proved | $\beta>\beta_c$ (Gayrard 2019) |
| REM with external field / constrained magnetisation | proved | free energy by tilting the Gaussian tail exponent |

## 5. Principal Obstacles

- **Second-moment failure.** $\mathbb{E}Z^2/(\mathbb{E}Z)^2=1+2^{-N}(e^{\beta^2N}-1)\to1$ only for $\beta<\sqrt{\log2}=\beta_c/2$. In the whole window $\beta_c/2<\beta<\beta_c$ the naive Paley–Zygmund route dies even though the annealed free energy is still correct; truncated second moments (restricting to $X_\sigma\le \gamma\sqrt N$) are required, and this truncation is what makes fluctuations non-Gaussian and stable-law valued.
- **No concentration at the right scale.** $\log Z$ concentrates on scale $O(1)$ by Gaussian concentration, but the answer sits *at* scale $O(1)$; concentration inequalities therefore give no information about the limit law, and superconcentration/chaos arguments (Chatterjee) reach only variance orders.
- **Dynamics is not thermodynamics.** Trap-model results depend on the exact geometry of the hypercube through the transition rates; for Metropolis dynamics the jump rates couple to energy differences, destroying the exact renewal structure exploited in the random-hopping case. Critical and high-temperature time scales remain out of reach of the potential-theoretic capacity estimates.
- **Correlation kills the Poisson picture.** For log-correlated fields (branching random walk, 2D GFF, $\log|\zeta|$) the extremes form a *decorated* Poisson process with a random shift, the max centering acquires the $-\tfrac{3}{2\beta_c}\log N$ Bramson correction instead of $-\tfrac1{2\beta_c}\log N$, and the derivative martingale — not a plain stable law — appears. There is no general criterion telling which correlated fields fall on which side.

## 6. The Gap

The gap is no longer in the REM's own statics. It is:

1. **Dynamic phase diagram.** A single theorem covering all $(\beta,\text{time scale})$ pairs for Metropolis/Glauber dynamics, including $\beta\le\beta_c$ and time scales below the metastable regime, with a proved crossover line.
2. **Universality criterion.** A checkable condition on a correlated Gaussian field $(H_\sigma)$ — beyond "$A$ is concave" for the CREM — implying REM-type free energy and Poissonian extremes. Kistler's multiscale refinement of the second-moment method gives sufficient conditions but no dichotomy.
3. **Freezing beyond toy models.** Proving the full Fyodorov–Hiary–Keating prediction — the $O(1)$ limiting law of $\max_{|h|\le1}\log|\zeta(\tfrac12+i(t+h))|$ and the freezing of $\lim N^{-1}\log \sum e^{\beta H}$ for $\beta>\beta_c$ — for zeta and for characteristic polynomials of CUE.

## 7. Current Research (as of June 2026)

- **Bonn (Bovier, Kistler and students).** Multiscale second-moment method; REM-like universality classes for correlated fields; "Derrida's random energy models" as an organising survey.
- **Aix-Marseille / Bonn (Gayrard, Hartung).** Dynamic phase diagram of the REM: extension of ageing results to broader time scales and to the $p$-spin case. *(frontier — verify)*
- **Montréal / NYU / Zürich (Arguin, Bourgade, Belius).** Extremes of log-correlated fields, zeta on short intervals, subleading-order results; branching-random-walk decorations.
- **Paris/Princeton (Panchenko school).** Ruelle cascades and ultrametricity as the "GREM-ification" of general mean-field models; extensions to multi-species and vector spin models.
- **Algorithmic side.** Sampling and optimisation thresholds in REM-like landscapes (overlap gap property; Gamarnik and coauthors): the REM is the extreme case where local algorithms provably fail above $\beta_c$. *(frontier — verify)*

## 8. Future Work

- Prove a *dichotomy theorem*: for a Gaussian field with covariance profile $A$, REM behaviour holds iff $A$ is "sufficiently concave at scale $\log N$".
- Complete the dynamic phase diagram for Metropolis dynamics at $\beta<\beta_c$ and at the critical scale, likely via capacity/potential theory plus coarse-graining on the extremal states.
- Sharpen the $\beta=\beta_c$ statics: identify the full critical scaling window $\beta=\beta_c+t/\sqrt N$ interpolating between the two fluctuation regimes.
- Transfer the proved REM fluctuation theory to number-theoretic and random-matrix models to establish freezing rigorously.

## 9. Key References

- **[Foundational]** B. Derrida. *Random-Energy Model: Limit of a Family of Disordered Models.* Physical Review Letters **45**, 79–82, 1980.
- **[Foundational]** B. Derrida. *Random-energy model: An exactly solvable model of disordered systems.* Physical Review B **24**, 2613–2626, 1981.
- **[Foundational]** T. Eisele. *On a third-order phase transition.* Communications in Mathematical Physics **90**, 125–159, 1983.
- **[Foundational]** E. Olivieri, P. Picco. *On the existence of thermodynamics for the random energy model.* Communications in Mathematical Physics **96**, 125–144, 1984.
- **[Foundational]** D. Ruelle. *A mathematical reformulation of Derrida's REM and GREM.* Communications in Mathematical Physics **108**, 225–239, 1987.
- **[Foundational]** B. Derrida, E. Gardner. *Solution of the generalised random energy model.* Journal of Physics C **19**, 2253–2274, 1986.
- **[SOTA]** A. Bovier, I. Kurkova, M. Löwe. *Fluctuations of the free energy in the REM and the $p$-spin SK models.* Annals of Probability **30**, 605–651, 2002.
- **[SOTA]** A. Bovier, I. Kurkova. *Derrida's generalised random energy models I & II.* Annales de l'IHP Probabilités et Statistiques **40**, 439–480 and 481–495, 2004.
- **[SOTA]** G. Ben Arous, A. Bovier, V. Gayrard. *Glauber dynamics of the random energy model. I & II.* Communications in Mathematical Physics **235**, 379–425 and **236**, 1–54, 2003.
- **[SOTA]** V. Gayrard. *Aging in Metropolis dynamics of the REM: a proof.* Probability Theory and Related Fields **174**, 501–551, 2019.
- **[SOTA]** L.-P. Arguin, D. Belius, P. Bourgade, M. Radziwiłł, K. Soundararajan. *Maximum of the Riemann zeta function on a short interval of the critical line.* Communications on Pure and Applied Mathematics **72**, 500–535, 2019.
- **[SOTA]** Y. V. Fyodorov, G. A. Hiary, J. P. Keating. *Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function.* Physical Review Letters **108**, 170601, 2012.
- **[Survey]** A. Bovier. *Statistical Mechanics of Disordered Systems: A Mathematical Perspective.* Cambridge University Press, 2006.
- **[Survey]** N. Kistler. *Derrida's random energy models: from spin glasses to the extremes of correlated random fields.* In *Correlated Random Systems: Five Different Methods*, Lecture Notes in Mathematics 2143, Springer, 2015.
- **[Survey]** M. Talagrand. *Mean Field Models for Spin Glasses, Volumes I–II.* Springer, 2011.
- **[Survey]** S. Chatterjee. *Superconcentration and Related Topics.* Springer, 2014.
- **[Foundational]** E. Bolthausen, A.-S. Sznitman. *On Ruelle's probability cascades and an abstract cavity method.* Communications in Mathematical Physics **197**, 247–276, 1998.

## 10. Worked Example / Concrete Special Case

**Where the second moment breaks, and why the free energy still does not.**

First moment: $\mathbb{E}Z_{N,\beta}=2^N e^{\beta^2N/2}$, so by Jensen and Markov
$$\limsup_N f_N(\beta)\le \log 2+\tfrac{\beta^2}{2}\quad\text{a.s.}$$
Second moment: since the $X_\sigma$ are independent,
$$\mathbb{E}Z^2=2^N e^{2\beta^2 N}+2^N(2^N-1)e^{\beta^2N},\qquad \frac{\mathbb{E}Z^2}{(\mathbb{E}Z)^2}=2^{-N}e^{\beta^2N}+1-2^{-N}.$$
This tends to $1$ iff $\beta^2<\log 2$, i.e. $\beta<\beta_c/2\approx0.5887$. So Paley–Zygmund gives $Z\asymp\mathbb{E}Z$ only on the first half of the high-temperature phase — yet the correct answer $f=\log2+\beta^2/2$ holds up to $\beta_c\approx1.1774$, twice as far.

**Repair by truncation.** Fix $\gamma\in(\beta,\beta_c)$ and set $\tilde Z=\sum_\sigma e^{\beta\sqrt N X_\sigma}\mathbf 1_{\{X_\sigma\le\gamma\sqrt N\}}$. Since $\mathbb{P}(\exists\sigma: X_\sigma>\gamma\sqrt N)\le 2^Ne^{-\gamma^2N/2}\to0$ for $\gamma>\beta_c$… choosing $\gamma$ slightly below $\beta_c$ keeps $\tilde Z=Z$ with probability $\to1$ up to $e^{o(N)}$ corrections, while
$$\mathbb{E}\tilde Z^2\le 2^N\,\mathbb{E}\big[e^{2\beta\sqrt NX}\mathbf 1_{X\le\gamma\sqrt N}\big]+(\mathbb{E}\tilde Z)^2,\qquad \mathbb{E}\big[e^{2\beta\sqrt NX}\mathbf 1_{X\le\gamma\sqrt N}\big]\le e^{N(2\beta\gamma-\gamma^2/2)},$$
using $2\beta x-x^2/2\le 2\beta\gamma-\gamma^2/2$ for $x \le \gamma\sqrt N$ when $\gamma\le 2\beta$. The truncated ratio stays bounded whenever $\log2+\beta^2>2\beta\gamma-\gamma^2/2$, and optimising over $\gamma<\beta_c$ pushes the argument all the way to $\beta_c$: at $\beta=\beta_c^-$ the constraint becomes $\log 2 + \beta^2 > 2\beta\beta_c - \beta_c^2/2 = 2\beta\beta_c-\log2$, i.e. $(\beta-\beta_c)^2>0$, true for every $\beta<\beta_c$.

**Frozen phase, numerically.** Take $\beta=2\beta_c=2\sqrt{2\log2}\approx2.3548$. Then $f(\beta)=\beta\beta_c=2\beta_c^2=4\log 2\approx2.7726$, the entropy is $s=f-\beta f'=0$, and $\alpha=\beta_c/\beta=1/2$: the Gibbs weights converge to $\mathrm{PD}(1/2)$ and
$$P(q)=\tfrac12\delta_0+\tfrac12\delta_1 .$$
Two independent samples from the Gibbs measure coincide with probability $\to1/2$ — the measure is carried by $O(1)$ configurations. Contrast $\beta=1<\beta_c$: $f=\log2+\tfrac12\approx1.1931$, $s=\log 2\approx0.6931>0$, $P(q)\Rightarrow\delta_0$, and the measure spreads over $e^{N\log 2 (1+o(1))}$ states. Setting $f_{\text{ann}}(\beta)=\log2+\beta^2/2$ and $f_{\text{frozen}}(\beta)=\beta\beta_c$, the two branches touch tangentially at $\beta_c$ ($f_{\text{ann}}-f_{\text{frozen}}=\tfrac12(\beta-\beta_c)^2$), which is exactly the third-order character of the transition.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*