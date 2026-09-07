---
id: 09-probability/parisi-formula-for-spin-glasses
title: "Parisi Formula for Spin Glasses"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Parisi Formula for Spin Glasses

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/parisi-formula-for-spin-glasses` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Sherrington–Kirkpatrick (SK) model is a random Hamiltonian on the hypercube $\Sigma_N=\{-1,+1\}^N$. Parisi's 1979–80 replica-symmetry-breaking ansatz predicted an exact variational formula for the limiting free energy

$$F(\beta)=\lim_{N\to\infty}\frac1N\,\mathbb{E}\log\sum_{\sigma\in\Sigma_N}e^{-\beta H_N(\sigma)} .$$

**Claim (Parisi formula).** $F=\inf_{\zeta}\mathcal{P}(\zeta)$, where $\zeta$ ranges over probability measures on $[0,1]$ (the *functional order parameter*, the limiting law of the overlap between two replicas) and $\mathcal{P}$ is the Parisi functional defined in §2.

The formula was derived by a non-rigorous replica trick involving an analytic continuation to $n\to0$ replicas and a limit of $n\times n$ matrices with $n<1$. A complete resolution requires: (i) proof that the limit exists; (ii) a matching upper bound $F\le\inf_\zeta\mathcal{P}(\zeta)$; (iii) a matching lower bound. All three are now theorems for mixed $p$-spin models with Ising or spherical spins (Guerra 2003; Talagrand 2006; Panchenko 2014). The **open** part of the problem is everything beyond that perimeter: non-convex vector/multi-species models, the Potts and general vector spin classes in full generality, quantitative rates, explicit determination of the minimizing $\zeta$, and — the deepest question — whether any Parisi-type description holds for the finite-dimensional Edwards–Anderson model.

## 2. Mathematical Foundations

**Hamiltonian.** For a mixture function $\xi(t)=\sum_{p\ge2}\beta_p^2 t^p$ with $\sum_p 2^p\beta_p^2<\infty$, let $H_N$ be the centered Gaussian field on $\Sigma_N$ with

$$\mathbb{E}\,H_N(\sigma^1)H_N(\sigma^2)=N\,\xi(R_{12}),\qquad R_{12}=\frac1N\sum_{i=1}^N\sigma^1_i\sigma^2_i,$$

realized as $H_N(\sigma)=\sum_{p\ge2}\frac{\beta_p}{N^{(p-1)/2}}\sum_{i_1,\dots,i_p}g_{i_1\cdots i_p}\sigma_{i_1}\cdots\sigma_{i_p}$ with i.i.d. standard Gaussians $g$. The SK model is $\xi(t)=\beta^2t^2/2$. With external field $h$, the free energy is

$$F_N=\frac1N\,\mathbb{E}\log\sum_{\sigma}\exp\Big(H_N(\sigma)+h\sum_i\sigma_i\Big).$$

**Parisi functional.** For a probability measure $\zeta$ on $[0,1]$ write $\zeta(t)=\zeta([0,t])$ for its distribution function. Let $f_\zeta:[0,1]\times\mathbb{R}\to\mathbb{R}$ solve the **Parisi PDE**

$$\partial_t f_\zeta(t,x)=-\frac{\xi''(t)}{2}\Big(\partial_x^2 f_\zeta(t,x)+\zeta(t)\,\big(\partial_x f_\zeta(t,x)\big)^2\Big),\qquad f_\zeta(1,x)=\log\cosh x .$$

Then

$$\mathcal{P}(\zeta)=\log 2+f_\zeta(0,h)-\frac12\int_0^1 \zeta(t)\,t\,\xi''(t)\,dt .$$

**Theorem (Parisi formula; Guerra, Talagrand, Panchenko).** $\lim_{N\to\infty}F_N=\inf_\zeta\mathcal{P}(\zeta)$.

Structural inputs:

- **Superadditivity** (Guerra–Toninelli 2002): $NF_N$ is superadditive by Gaussian interpolation, so the limit exists.
- **Guerra's RSB bound** (2003): interpolation against a Ruelle probability cascade gives $F_N\le\mathcal{P}(\zeta)$ for every $\zeta$, for all $N$.
- **Ghirlanda–Guerra identities**: self-averaging of the Hamiltonian forces the overlap array to satisfy an infinite family of distributional identities.
- **Ultrametricity** (Panchenko 2013): under GG identities, the support of the limiting overlap array is a.s. ultrametric, $R_{13}\ge\min(R_{12},R_{23})$; combined with the Dovbysh–Sudakov representation this identifies the limiting Gibbs measure as a Ruelle cascade, yielding the lower bound.
- **Convexity** (Auffinger–Chen 2015): $\zeta\mapsto\mathcal{P}(\zeta)$ is strictly convex in $\zeta$, so the minimizer (*Parisi measure*) is unique. Jagannath–Tobasco (2015) recast $\mathcal{P}$ as a dynamic-programming/stochastic-control value.

## 3. History & State of the Art (SOTA)

- **1975.** Sherrington and Kirkpatrick propose the model and the replica-symmetric solution; it gives negative entropy at low temperature — manifestly wrong.
- **1978.** de Almeida and Thouless locate the instability line of the RS solution.
- **1979–80.** Parisi introduces hierarchical replica symmetry breaking and the functional order parameter; Mézard–Parisi–Virasoro (1987) develop the physical picture: pure states, ultrametric organization, non-self-averaging overlaps.
- **2002.** Guerra–Toninelli prove existence of the limit.
- **2003.** Guerra proves $\mathcal{P}$ is an upper bound for all $\zeta$ — the first rigorous appearance of the exact formula. Aizenman–Sims–Starr give the "extended variational principle" and the cavity/ROSt framework.
- **2006.** Talagrand proves the matching lower bound for even mixed $p$-spin models (Annals of Mathematics), and separately the Crisanti–Sommers formula for spherical spins.
- **2013–14.** Panchenko proves the ultrametricity conjecture and then the Parisi formula for **general** mixtures (odd $p$ allowed) via the GG identities.
- **2013–17.** Chen extends to spherical mixed models with odd terms; Auffinger–Chen prove uniqueness of the Parisi measure and the zero-temperature Parisi formula for the ground-state energy.
- **2015–22.** Panchenko treats multi-species SK with convex covariance and the Potts spin glass; Bates–Sohn handle multi-species spherical models and simultaneous symmetry breaking.
- **2019–24.** Hamilton–Jacobi reformulation (Mourrat and coauthors) reframes the formula as a variational solution to an infinite-dimensional HJ equation, and produces new upper bounds for **non-convex** vector models.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| Ising mixed $p$-spin, $\xi$ even, $h\in\mathbb{R}$ | Proved (Talagrand 2006) |
| Ising mixed $p$-spin, general $\xi$ (odd $p$ allowed) | Proved (Panchenko 2014) |
| Spherical mixed $p$-spin (Crisanti–Sommers) | Proved (Talagrand 2006; Chen 2013 for odd $p$) |
| Zero temperature: $\lim N^{-1}\max_\sigma H_N$ | Proved (Auffinger–Chen 2017) |
| SK at high temperature $\beta\le1$, $h=0$ | Replica-symmetric: $F=\log2+\beta^2/4$; CLT for $\log Z_N$ (Aizenman–Lebowitz–Ruelle 1987) |
| Multi-species SK, **convex** covariance | Proved (Panchenko 2015) |
| Multi-species spherical, incl. non-convex regimes | Proved (Bates–Sohn 2022) |
| Potts / vector spins, convex case | Proved (Panchenko 2018; Panchenko vector spin glasses) |
| Multi-species Ising, non-convex covariance | Upper bound only (Chen–Mourrat 2024) — **open** |
| Edwards–Anderson on $\mathbb{Z}^d$, $d\ge2$ | Entirely open |

Numerically, the SK ground-state energy is $-0.763166\ldots$ (Parisi constant), matched by Monte Carlo, extremal optimization, and truncated $k$-step RSB; full RSB ($k\to\infty$) is required — $1$-step RSB gives $-0.7652$, off in the fourth digit.

## 5. Principal Obstacles

- **The replica trick is not a proof technique.** $\mathbb{E}Z^n$ for integer $n$ does not determine the $n\to0$ analytic continuation; no rigorous argument recovers the hierarchical matrix ansatz from moments. Every proof to date bypasses replicas entirely.
- **Second-moment methods die at the AT line.** $\mathbb{E}Z_N^2/(\mathbb{E}Z_N)^2$ stays bounded only for $\beta<1$, $h=0$. Below that, $\log Z_N$ concentrates but its mean is dominated by rare, non-Gaussian overlap structure.
- **Lower bounds need the Gibbs measure, not just its free energy.** Guerra's interpolation is one-sided: convexity of $t\mapsto\xi(t)$ along the interpolation path gives $\le$ but never $\ge$. Recovering $\ge$ requires proving that the asymptotic Gibbs measure *is* a Ruelle cascade — that is, ultrametricity — which is a statement about an infinite exchangeable array, not about a single scalar.
- **Non-convexity breaks interpolation.** For vector/multi-species models the covariance is a function of an overlap *matrix*; Guerra interpolation needs the analogue of $\xi$ to be convex on the relevant matrix set. When it is not (e.g. bipartite SK with a negative species coupling), the interpolation error term changes sign and the Parisi bound is not even known to be an upper bound in the classical form.
- **No local structure.** In finite dimensions there is no cavity field with i.i.d. Gaussian statistics, no exchangeability, hence no Ghirlanda–Guerra identities and no ultrametricity. Newman–Stein's metastate analysis shows that even formulating the correct conjecture for $\mathbb{Z}^d$ is delicate.
- **Quantitative control is weak.** $|F_N-F|$ is known to be $O(N^{-1/4})$-ish at best in general; interpolation gives no rate at the critical temperature, where superconcentration phenomena (Chatterjee) suppress variance below the Gaussian scale.

## 6. The Gap

For scalar Ising and spherical mixed $p$-spin models there is **no gap**: §4 covers §1 completely. The gap lives one step outward.

1. **Non-convex covariances.** For vector spin glasses with a general covariance $\xi:\mathbb{R}^{\kappa\times\kappa}\to\mathbb{R}$ that is not convex on the overlap-matrix cone, only an upper bound is known (in Hamilton–Jacobi form). The missing step is a *matching lower bound*: a synchronization/ultrametricity theorem for matrix-valued overlaps without convexity. Panchenko's synchronization mechanism currently needs convexity to certify that the overlap matrix is a monotone function of a single scalar.
2. **Explicit Parisi measures.** The minimizer $\zeta_\star$ is unique and characterized by a first-order condition, but is not known in closed form for any $\beta>1$; even whether $\zeta_\star$ has full support on an interval (full RSB) for SK at all $\beta>1$, $h=0$, is not fully settled rigorously.
3. **Short range.** Whether $\mathbb{Z}^d$ spin glasses exhibit RSB or the two-state droplet picture (Fisher–Huse) remains the central physical dichotomy, untouched by mean-field technology.

## 7. Current Research (as of June 2026)

- **Hamilton–Jacobi programme.** Mourrat and collaborators recast $F_N$ as an approximate solution of an HJ equation on the space of measures; the Parisi formula becomes a Hopf–Lax representation. This yields free-energy upper bounds for non-convex vector models (Chen–Mourrat) and a variational formula that is *not* obviously equal to Parisi's when convexity fails — the discrepancy is itself an active object of study. *(frontier — verify)*
- **Algorithmic Parisi.** Montanari's approximate-message-passing algorithm achieves energy $\mathrm{ALG}=\int_0^1\sqrt{\xi''(t)}\,dt$-type values, provably optimal among "overlap-gap-free" classes; Huang–Sellke prove branching-OGP obstructions matching the Parisi threshold. Groups: Stanford, MIT, Berkeley, NYU.
- **Multi-species and deep networks.** Bates–Sohn, Subag, and others push spherical multi-species results toward Ising; motivation includes deep Boltzmann machines and layered inference models.
- **Fluctuations.** CLTs for $\log Z_N$ inside the RSB phase remain largely open; partial results exist at $1$-RSB and for spherical models (Baik–Lee for the spherical SK). *(frontier — verify)*
- **Institutions.** Northwestern (Auffinger), Chicago (W.-K. Chen at Minnesota; Panchenko at Toronto), Courant, ENS/Paris (Mourrat, Bolthausen school in Zurich).

## 8. Future Work

- Prove a lower bound matching the HJ upper bound for non-convex vector models, or exhibit a model where the classical Parisi expression is strictly wrong — the sharper of the two outcomes.
- Establish synchronization of matrix overlaps without convexity, likely via a matrix-valued Ghirlanda–Guerra identity.
- Obtain quantitative rates $|F_N - F|=O(N^{-\alpha})$ uniform in $\beta$, including at criticality.
- Determine regularity of $\zeta_\star$ (Auffinger–Chen conjecture that $\zeta_\star$ has a density on its support in the SK model at low $T$).
- Transfer any fragment of ultrametricity to diluted models on sparse graphs (Talagrand's and Coja-Oghlan's programme), then to $\mathbb{Z}^d$.

## 9. Key References

- **[Foundational]** D. Sherrington, S. Kirkpatrick. *Solvable Model of a Spin-Glass.* Physical Review Letters 35, 1792–1796, 1975.
- **[Foundational]** G. Parisi. *Infinite Number of Order Parameters for Spin-Glasses.* Physical Review Letters 43, 1754–1756, 1979.
- **[Foundational]** G. Parisi. *A sequence of approximated solutions to the S-K model for spin glasses.* Journal of Physics A 13, L115, 1980.
- **[Foundational]** M. Mézard, G. Parisi, M. A. Virasoro. *Spin Glass Theory and Beyond.* World Scientific, 1987.
- **[Key]** F. Guerra, F. L. Toninelli. *The thermodynamic limit in mean field spin glass models.* Communications in Mathematical Physics 230, 71–79, 2002.
- **[Key]** F. Guerra. *Broken replica symmetry bounds in the mean field spin glass model.* Communications in Mathematical Physics 233, 1–12, 2003.
- **[Key]** M. Aizenman, R. Sims, S. L. Starr. *Extended variational principle for the Sherrington–Kirkpatrick spin-glass model.* Physical Review B 68, 214403, 2003.
- **[Key]** M. Talagrand. *The Parisi formula.* Annals of Mathematics 163, 221–263, 2006.
- **[Key]** M. Talagrand. *Free energy of the spherical mean field model.* Probability Theory and Related Fields 134, 339–382, 2006.
- **[Key]** D. Panchenko. *The Parisi ultrametricity conjecture.* Annals of Mathematics 177, 383–393, 2013.
- **[Key]** D. Panchenko. *The Parisi formula for mixed $p$-spin models.* Annals of Probability 42, 946–958, 2014.
- **[SOTA]** A. Auffinger, W.-K. Chen. *The Parisi formula has a unique minimizer.* Communications in Mathematical Physics 335, 1429–1444, 2015.
- **[SOTA]** A. Auffinger, W.-K. Chen. *Parisi formula for the ground state energy in the mixed $p$-spin model.* Annals of Probability 45, 4617–4631, 2017.
- **[SOTA]** W.-K. Chen. *The Aizenman–Sims–Starr scheme and Parisi formula for mixed $p$-spin spherical models.* Electronic Journal of Probability 18, no. 94, 2013.
- **[SOTA]** D. Panchenko. *The free energy in a multi-species Sherrington–Kirkpatrick model.* Annals of Probability 43, 3494–3513, 2015.
- **[SOTA]** D. Panchenko. *Free energy in the Potts spin glass.* Annals of Probability 46, 829–864, 2018.
- **[SOTA]** E. Bates, Y. Sohn. *Crisanti–Sommers formula and simultaneous symmetry breaking in multi-species spherical spin glasses.* Communications in Mathematical Physics 394, 1101–1152, 2022.
- **[SOTA]** A. Jagannath, I. Tobasco. *A dynamic programming approach to the Parisi functional.* Proceedings of the American Mathematical Society 143, 3135–3145, 2015.
- **[SOTA]** J.-C. Mourrat. *Hamilton–Jacobi equations for mean-field disordered systems.* Annales Henri Lebesgue 4, 453–484, 2021.
- **[Survey]** D. Panchenko. *The Sherrington–Kirkpatrick Model.* Springer Monographs in Mathematics, 2013.
- **[Survey]** M. Talagrand. *Mean Field Models for Spin Glasses, Volumes I & II.* Springer, 2011.
- **[Context]** M. Aizenman, J. L. Lebowitz, D. Ruelle. *Some rigorous results on the Sherrington–Kirkpatrick spin glass model.* Communications in Mathematical Physics 112, 3–20, 1987.

## 10. Worked Example / Concrete Special Case

**SK model, no external field, replica-symmetric trial measure.** Take $\xi(t)=\beta^2t^2/2$ (so $\xi''(t)=\beta^2$, $\xi'(1)=\beta^2$) and $h=0$. Try the one-atom measure $\zeta=\delta_q$, whose distribution function is $\zeta(t)=\mathbf{1}\{t\ge q\}$.

*Step 1 — solve the PDE on $[q,1]$.* Here $\zeta(t)=1$, so the equation is $\partial_t f=-\tfrac{\beta^2}{2}(\partial_x^2f+(\partial_xf)^2)$. The Hopf–Cole substitution $u=e^{f}$ linearizes it: $\partial_t u=-\tfrac{\beta^2}{2}\partial_x^2u$, a backward heat equation with total variance $\int_q^1\beta^2\,dt=\beta^2(1-q)$. With $u(1,x)=\cosh x$ and $\mathbb{E}\cosh(x+\sigma z)=\cosh(x)e^{\sigma^2/2}$,

$$u(q,x)=\cosh(x)\,e^{\beta^2(1-q)/2},\qquad f(q,x)=\log\cosh x+\tfrac{\beta^2}{2}(1-q).$$

*Step 2 — solve on $[0,q]$.* Here $\zeta(t)=0$ and the equation is the linear backward heat equation with variance $\beta^2 q$, so $f(0,0)=\mathbb{E}\big[\log\cosh(\beta\sqrt{q}\,z)\big]+\tfrac{\beta^2}{2}(1-q)$, $z\sim N(0,1)$.

*Step 3 — the penalty term.*

$$\frac12\int_0^1\zeta(t)\,t\,\xi''(t)\,dt=\frac{\beta^2}{2}\int_q^1 t\,dt=\frac{\beta^2}{4}(1-q^2).$$

*Step 4 — assemble.*

$$\mathcal{P}(\delta_q)=\log2+\mathbb{E}\log\cosh(\beta\sqrt{q}\,z)+\frac{\beta^2}{2}(1-q)-\frac{\beta^2}{4}(1-q^2)=\log2+\mathbb{E}\log\cosh(\beta\sqrt q\,z)+\frac{\beta^2}{4}(1-q)^2,$$

the classical replica-symmetric expression.

*Step 5 — optimize.* Stationarity gives the SK self-consistency equation $q=\mathbb{E}\tanh^2(\beta\sqrt q\,z)$. For $\beta\le1$ the only root is $q=0$, and

$$F(\beta)=\mathcal{P}(\delta_0)=\log2+\frac{\beta^2}{4},$$

which matches the annealed bound $\frac1N\log\mathbb{E}Z_N$ exactly and is confirmed by the second-moment method: $\mathbb{E}Z_N^2/(\mathbb{E}Z_N)^2$ stays bounded iff $\beta<1$.

For $\beta>1$ a nonzero root appears, but $\delta_q$ is no longer the minimizer: the de Almeida–Thouless stability condition $\beta^2\mathbb{E}\,\mathrm{sech}^4(\beta\sqrt q z)\le1$ fails, and the infimum is attained at a measure $\zeta_\star$ with infinitely many atoms — full replica symmetry breaking. This is precisely the regime where $\inf_\zeta\mathcal{P}(\zeta)$ has no closed form and where Talagrand's and Panchenko's theorems supply the only rigorous identification of $F(\beta)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*