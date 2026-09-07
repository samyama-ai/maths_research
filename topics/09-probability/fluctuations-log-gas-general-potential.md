---
id: 09-probability/fluctuations-log-gas-general-potential
title: "Empirical Measure Fluctuations for Log-Gases with General Potentials"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Empirical Measure Fluctuations for Log-Gases with General Potentials

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/fluctuations-log-gas-general-potential` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\beta>0$ and let $V:\mathbb R\to\mathbb R$ be a confining potential. The one-dimensional log-gas (β-ensemble) is the exchangeable probability measure on $\mathbb R^N$

$$d\mathbb P_N^{V,\beta}(x_1,\dots,x_N)=\frac{1}{Z_N^{V,\beta}}\prod_{i<j}|x_i-x_j|^{\beta}\,e^{-\frac{\beta N}{2}\sum_{i=1}^N V(x_i)}\,dx .$$

Write $\hat\mu_N=\frac1N\sum_i\delta_{x_i}$ and let $\mu_V$ be the equilibrium measure. The **fluctuation functional** is

$$\mathrm{Fluct}_N(f)=\sum_{i=1}^N f(x_i)-N\int f\,d\mu_V .$$

**Problem.** Determine, for the widest possible class of potentials $V$ and test functions $f$, the limit law of $\mathrm{Fluct}_N(f)$: identify the deterministic mean $m_V(f)$, the variance $\sigma_V^2(f)$, the rate of convergence, and the range of scales on which the law is Gaussian.

The precise open statement: **for every $\beta>0$, is $\mathrm{Fluct}_N(f)$ asymptotically Gaussian (possibly after subtracting an explicit oscillatory or discrete random correction) for all potentials $V$ that are merely $C^k$ with $k$ small and possibly *critical* — vanishing density in the bulk, higher-order edge exponents, or hard walls — and for all $f$ of low regularity ($f\in H^{1/2}$, or $f$ Lipschitz but not $C^1$)?** A complete solution gives: (i) necessary and sufficient conditions on $(V,f,\beta)$ for a Gaussian limit; (ii) the exact non-Gaussian law when it fails; (iii) mesoscopic versions valid down to scale $N^{-1+\varepsilon}$ for every $\varepsilon>0$. A disproof of Gaussianity in a given regime must exhibit the alternative limit law.

## 2. Mathematical Foundations

**Equilibrium measure.** For $V$ continuous with $\liminf_{|x|\to\infty}\big(V(x)-2\log|x|\big)>-\infty$, the energy functional

$$\mathcal E_V(\mu)=\iint \log\frac{1}{|x-y|}\,d\mu(x)d\mu(y)+\int V\,d\mu$$

has a unique minimizer $\mu_V$ among probability measures, with compact support $\Sigma$ and Euler–Lagrange conditions

$$2\int\log|x-y|\,d\mu_V(y)-V(x)=\ell_V \ \ \text{on } \Sigma,\qquad \le \ell_V \ \text{ on } \mathbb R .$$

$\hat\mu_N\to\mu_V$ almost surely, with a large-deviation principle at speed $N^2$ and rate $\frac{\beta}{2}(\mathcal E_V-\mathcal E_V(\mu_V))$ (Ben Arous–Guionnet 1997).

**Regularity classes.** $V$ analytic is *one-cut regular* if $\Sigma=[a,b]$ and $d\mu_V=\frac{1}{2\pi}S(x)\sqrt{(b-x)(x-a)}\,dx$ with $S>0$ on $[a,b]$ and strict inequality off $\Sigma$; *multi-cut regular* if $\Sigma=\bigcup_{h=0}^{g}[a_h,b_h]$ with the same local behaviour. *Critical* cases: $S$ vanishes in the interior (Painlevé II / higher-order kernels), $S$ vanishes at an endpoint (edge exponent $(b-x)^{2k+1/2}$), or two cuts merge.

**Master operator.** The linearized loop equation is governed by the finite Hilbert transform
$$\Xi_V[\phi](x)=\mathrm{p.v.}\!\int\frac{\phi(x)-\phi(y)}{x-y}\,d\mu_V(y),$$
and the CLT reduces to solving $\Xi_V[\phi]=f$ with controlled regularity — the key technical object in Bekerman–Figalli–Guionnet and Bekerman–Leblé–Serfaty.

**One-cut CLT.** Normalize $\Sigma=[-1,1]$ and expand $f(\cos\theta)=\sum_{k\ge0}c_k\cos(k\theta)$. Then, for one-cut regular $V$ and smooth $f$,

$$\mathrm{Fluct}_N(f)\ \xrightarrow{d}\ \mathcal N\big(m_V(f),\,\sigma^2(f)\big),\qquad \sigma^2(f)=\frac{1}{2\beta}\sum_{k\ge1}k\,c_k^2=\frac{1}{\beta}\|f\|^2_{H^{1/2}(\mu_{\mathrm{eq}})},$$

with **no normalization by $\sqrt N$** — the variance is $O(1)$, the signature of long-range rigidity. The mean splits as $m_V(f)=\big(\tfrac{2}{\beta}-1\big)\mathcal A(f)+\mathcal B_V(f)$: a "β-anomaly" $\mathcal A$ supported at the endpoints of $\Sigma$, plus a potential-dependent term $\mathcal B_V$ built from $S$ and $V''$. The variance is universal in $V$ (depends only on $\Sigma$); only the mean sees $V$.

**Multi-cut.** With $g+1$ cuts, the filling fractions $\mathbf n=(N_h)$ (number of points per cut) fluctuate as a $\mathbb Z^g$-valued random vector whose law converges to a discrete Gaussian; $\mathrm{Fluct}_N(f)$ is then a sum of a Gaussian and an $N$-dependent quasi-periodic term expressed by Siegel theta functions — the limit **does not exist** without subsequences.

## 3. History & State of the Art (SOTA)

- **1970s–90s (physics).** Dyson's Coulomb-gas heuristics; Ambjørn–Makeenko and the topological-recursion school derive $1/N$ expansions of matrix-model free energies non-rigorously.
- **1998.** Johansson, *On fluctuations of eigenvalues of random Hermitian matrices* (Duke Math. J.) — the first rigorous CLT: one-cut, $V$ polynomial (later analytic), all $\beta>0$, no $\sqrt N$ normalization. Method: loop equations plus a change of variables.
- **2011.** Pastur–Shcherbina's monograph consolidates CLTs for Hermitian and β models with analytic one-cut potentials.
- **2012–2013.** Borot–Guionnet obtain full asymptotic $1/N$ expansions of $Z_N$ and of correlators in the one-cut and multi-cut analytic regimes; Shcherbina identifies the oscillatory multi-cut fluctuations.
- **2014.** Bourgade–Erdős–Yau prove bulk and edge universality plus optimal rigidity $|x_i-\gamma_i|\lesssim N^{-1+\varepsilon}\hat i^{-1/3}$ for general β-ensembles with analytic convex-type $V$, supplying the a priori input for later CLTs.
- **2015.** Bekerman–Figalli–Guionnet build approximate transport maps between β-ensembles, transferring local statistics across potentials.
- **2018.** Bekerman–Leblé–Serfaty prove the one-cut CLT for **non-analytic** $V$ (roughly $C^p$, $p\ge 30$ in the original statement) using the electric/energy method of Serfaty's Coulomb-gas program — the current benchmark for generality in $V$.
- **2019–2021.** Lambert–Ledoux–Webb give quantitative normal approximation (Stein's method, explicit rates $O(N^{-1/2+\varepsilon})$ classes) ; Claeys–Fahs–Lambert–Webb determine global rigidity, $\max_x|\mathrm{Fluct}_N(\mathbf 1_{(-\infty,x]})|\sim \sqrt{\tfrac{2}{\beta}}\log N$ up to $\sqrt{\log\log}$ corrections.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $V$ analytic, one-cut regular, $f$ analytic, all $\beta>0$ | **Proved** (Johansson 1998; Borot–Guionnet 2013 with full $1/N$ expansion) |
| $V\in C^p$ ($p$ large finite), one-cut regular, $f\in C^{p'}$, all $\beta>0$ | **Proved** (Bekerman–Leblé–Serfaty 2018) |
| $V$ analytic, multi-cut ($g\ge1$) | **Proved with oscillation**: limit along subsequences of $N\alpha_h \bmod 1$; Gaussian $+$ theta-function correction (Shcherbina 2013; Borot–Guionnet, multi-cut) |
| $\beta=2$, $V$ analytic, $f$ with Fisher–Hartwig jump/root singularities | **Proved** via Riemann–Hilbert steepest descent (Deift–Its–Krasovsky; Charlier 2019) |
| Mesoscopic scales $f_N(x)=f\big((x-E)/\eta\big)$, $N^{-1}\ll\eta\ll1$, $E$ in the bulk | **Proved** for analytic/smooth $V$, all $\beta$ (Bekerman–Lodhia 2018; Lambert) |
| Quantitative rates | $d_{\mathrm{W}}$ or Kolmogorov distance $O(N^{-1/2+\varepsilon})$ for smooth $f$, one-cut (Lambert–Ledoux–Webb 2019) |
| Global maximum / $\log$-correlated structure | $\beta=2$ analytic one-cut: full second-order rigidity (Claeys–Fahs–Lambert–Webb 2021) |
| $\beta=2$ hard edge, Laguerre/Jacobi weights | **Proved** (classical orthogonal-polynomial asymptotics) |
| Higher-dimensional Coulomb ($d=2$, $\beta$ general) | CLT proved for $C^4$ potentials (Leblé–Serfaty 2018), variance $\frac{1}{2\pi\beta}\|\nabla f\|_{L^2}^2$ |

## 5. Principal Obstacles

- **Loss of analyticity kills Riemann–Hilbert.** The sharpest results ($\beta=2$, singular $f$, critical $V$) come from steepest descent for orthogonal polynomials, which needs an analytic weight and has **no known $\beta\ne2$ analogue** (no determinantal structure, no integrable kernel).
- **Loop equations need a priori rigidity.** Dyson–Schwinger hierarchies close only after inverting $\Xi_V$; the inversion loses $\sim 1/2$ to $2$ derivatives per iteration, so bootstrapping to $O(1)$ precision consumes many derivatives of $V$ and $f$. The $C^{30}$-type hypotheses in Bekerman–Leblé–Serfaty are artifacts of this loss, but no argument recovers the natural $C^{2}$/$H^{1/2}$ thresholds.
- **$\Xi_V$ degenerates at critical points.** When $S$ vanishes in the bulk or the edge exponent leaves $1/2$, $\Xi_V^{-1}$ is unbounded on the relevant spaces; the fluctuation problem couples to Painlevé transcendents rather than to a Gaussian field.
- **Multi-cut arithmetic.** Filling fractions are integers; their law depends on $N\int_{\Sigma_h}d\mu_V \bmod 1$, an equidistribution problem. No method converts this into a limit theorem valid for all $N$ — only along subsequences.
- **Low-regularity $f$ is genuinely borderline.** $\sigma^2(f)=\frac1\beta\|f\|^2_{H^{1/2}}$ diverges for indicators, so $\mathrm{Fluct}_N$ is a log-correlated field, not a random distribution in any Sobolev space of positive index; standard tightness arguments fail exactly at the interesting scale.
- **Energy/transport methods are lossy at the edge.** Serfaty-type electric-field renormalization controls bulk energy well but the boundary terms carrying the $(\tfrac2\beta-1)$ anomaly demand separate, potential-specific analysis.

## 6. The Gap

Proved: one-cut, $V$ smooth-enough (finite but large number of derivatives), $f$ smooth, Gaussian, $O(1)$ variance. General statement: arbitrary confining $V$, arbitrary $f\in H^{1/2}$, all $\beta$. The gap has four separable components:

1. **Regularity gap:** from $V\in C^{p}$, $p\gg1$ down to $V\in C^{2}$ or $V$ merely convex; and from $f\in C^{p'}$ down to $f\in H^{1/2}$.
2. **Criticality gap:** no CLT for any $\beta\ne2$ at a critical potential (interior zero of the density, non-generic edge exponent, cut merging). The expected answer is a Gaussian plus a Painlevé-II-type random correction; nothing is proved.
3. **Multi-cut gap:** proving convergence along the full sequence $N\to\infty$ after an explicit deterministic recentering, rather than along subsequences.
4. **Scale gap:** mesoscopic CLT at scales $\eta=N^{-1+\varepsilon}$ with $\varepsilon\to0$, and matching to the local (sine/Airy) regime.

Crossing (2) is the sharpest single step: it requires a $\beta$-general substitute for the Riemann–Hilbert analysis, likely a Dyson-Brownian-motion or transport argument that stays valid when $\Xi_V$ degenerates.

## 7. Current Research (as of June 2026)

- **Serfaty's Coulomb/Riesz-gas program** (Courant, IHÉS): CLTs for $\log$- and Riesz gases in all dimensions, non-smooth potentials, and the hydrodynamic limit of the associated gradient flows. The $d\ge2$ CLT for $C^4$ potentials is the template being pushed toward critical and non-convex settings.
- **Guionnet, Borot, Bekerman and collaborators** (ENS Lyon, MIT, CNRS): transport-map and loop-equation methods; extension of $1/N$ expansions to non-analytic and multi-cut potentials.
- **Lambert, Webb, Claeys, Charlier** (KTH/Zürich, Aalto, UCLouvain): log-correlated-field structure, Fisher–Hartwig asymptotics, moderate deviations, and Stein-method rates; recent activity on the maximum of $\log|\det(M-x)|$ for $\beta\ne2$ *(frontier — verify)*.
- **Bourgade, Erdős, Yau, Schröder** (NYU, IST Austria, Courant): Dyson Brownian motion as a universality mechanism at the mesoscopic scale; homogenization estimates that could deliver optimal-regularity CLTs *(frontier — verify)*.
- **Numerics:** tridiagonal Dumitriu–Edelman sampling and Metropolis-adjusted Langevin for $N\sim 10^5$–$10^6$ confirm the $\big(\tfrac2\beta-1\big)$ anomaly and multi-cut oscillations to two or three digits.

## 8. Future Work

- Replace the derivative-counting bootstrap by a fixed-point argument for $\Xi_V^{-1}$ in weighted Hölder or Besov scales, targeting $V\in C^{2+\alpha}$.
- Develop a $\beta$-general Riemann–Hilbert surrogate: stochastic-Airy/stochastic-Bessel operator perturbation theory near critical potentials.
- Prove a functional CLT: convergence of $x\mapsto \mathrm{Fluct}_N(\mathbf 1_{(-\infty,x]})$ to a log-correlated Gaussian field, with a Gaussian multiplicative chaos statement for $e^{\gamma\,\mathrm{Fluct}_N}$ at $\beta\ne2$.
- Handle weakly confining potentials ($V(x)-2\log|x|\to$ const), where $\mu_V$ has unbounded support and heavy-tailed corrections appear.
- Extend to constrained ensembles (hard walls, external charges) and to discrete β-ensembles, where the CLT acquires a lattice-dependent variance.

## 9. Key References

- **[Foundational]** K. Johansson. *On fluctuations of eigenvalues of random Hermitian matrices.* Duke Mathematical Journal, 91(1):151–204, 1998.
- **[Foundational]** G. Ben Arous, A. Guionnet. *Large deviations for Wigner's law and Voiculescu's non-commutative entropy.* Probability Theory and Related Fields, 108:517–542, 1997.
- **[Foundational]** L. Pastur, M. Shcherbina. *Eigenvalue Distribution of Large Random Matrices.* Mathematical Surveys and Monographs 171, AMS, 2011.
- **[SOTA]** F. Bekerman, T. Leblé, S. Serfaty. *CLT for fluctuations of β-ensembles with general potential.* Electronic Journal of Probability, 23, paper 115, 2018.
- **[SOTA]** G. Borot, A. Guionnet. *Asymptotic expansion of β matrix models in the one-cut regime.* Communications in Mathematical Physics, 317:447–483, 2013.
- **[SOTA]** M. Shcherbina. *Fluctuations of linear eigenvalue statistics of β matrix models in the multi-cut regime.* Journal of Statistical Physics, 151:1004–1034, 2013.
- **[SOTA]** P. Bourgade, L. Erdős, H.-T. Yau. *Universality of general β-ensembles.* Duke Mathematical Journal, 163(6):1127–1190, 2014.
- **[SOTA]** F. Bekerman, A. Figalli, A. Guionnet. *Transport maps for β-matrix models and universality.* Communications in Mathematical Physics, 338:589–619, 2015.
- **[SOTA]** G. Lambert, M. Ledoux, C. Webb. *Quantitative normal approximation of linear statistics of β-ensembles.* Annals of Probability, 47(5):2619–2685, 2019.
- **[SOTA]** T. Leblé, S. Serfaty. *Fluctuations of two-dimensional Coulomb gases.* Geometric and Functional Analysis, 28:443–508, 2018.
- **[SOTA]** T. Claeys, B. Fahs, G. Lambert, C. Webb. *How much can the eigenvalues of a random Hermitian matrix fluctuate?* Duke Mathematical Journal, 170(9):2085–2235, 2021.
- **[Survey]** S. Serfaty. *Systems of points with Coulomb interactions.* Proceedings of the ICM 2018, Vol. 1, 935–977.
- **[Survey]** A. Guionnet. *Asymptotics of Random Matrices and Related Models: The Uses of Dyson–Schwinger Equations.* CBMS Regional Conference Series 130, AMS, 2019.
- **[Tools]** I. Dumitriu, A. Edelman. *Matrix models for beta ensembles.* Journal of Mathematical Physics, 43(11):5830–5847, 2002.

## 10. Worked Example / Concrete Special Case

Take $V(x)=2x^2$. The equilibrium measure is the semicircle on $[-1,1]$: $d\mu_V=\frac{2}{\pi}\sqrt{1-x^2}\,dx$ (check the Euler–Lagrange identity $\int\log|x-y|\,d\mu_V(y)=x^2-\tfrac12-\log 2$ on $[-1,1]$). Take $f(x)=x^2$, so $\int f\,d\mu_V=\tfrac14$.

**Prediction from the CLT.** With $x=\cos\theta$, $f(\cos\theta)=\tfrac12+\tfrac12\cos2\theta$, so $c_0=c_2=\tfrac12$ and all other $c_k=0$. Hence

$$\sigma^2(f)=\frac{1}{2\beta}\sum_{k\ge1}k\,c_k^2=\frac{1}{2\beta}\cdot 2\cdot\frac14=\frac{1}{4\beta}.$$

**Exact finite-$N$ check.** Dumitriu–Edelman: the tridiagonal matrix $H_N$ with independent diagonal $a_i\sim\mathcal N(0,2)$ and sub-diagonal $b_k=\chi_{\beta(N-k)}/\sqrt2$ has eigenvalue density $\propto\prod|\lambda_i-\lambda_j|^\beta e^{-\sum\lambda_i^2/2}$. Setting $\lambda_i=\sqrt{2\beta N}\,x_i$ reproduces $\mathbb P_N^{V,\beta}$ with $V=2x^2$, and $\sum_i x_i^2=\mathrm{Tr}(H_N^2)/(2\beta N)$ where $\mathrm{Tr}(H_N^2)=\sum_i a_i^2+2\sum_k b_k^2$. Since $\mathbb E[a_i^2]=2$, $\mathrm{Var}(a_i^2)=8$, $b_k^2=\tfrac12\chi^2_{\beta(N-k)}$ with mean $\tfrac{\beta(N-k)}{2}$ and variance $\tfrac{\beta(N-k)}{2}$:

$$\mathbb E[\mathrm{Tr}H_N^2]=2N+\frac{\beta N(N-1)}{2},\qquad \mathrm{Var}[\mathrm{Tr}H_N^2]=8N+\beta N(N-1).$$

Therefore

$$\mathbb E\big[\mathrm{Fluct}_N(f)\big]=\frac{2N+\tfrac{\beta N(N-1)}{2}}{2\beta N}-\frac{N}{4}=\frac{1}{\beta}-\frac14 ,\qquad \mathrm{Var}\big[\mathrm{Fluct}_N(f)\big]=\frac{8N+\beta N(N-1)}{4\beta^2N^2}=\frac{1}{4\beta}+\frac{8-\beta}{4\beta^2 N}.$$

Both are $O(1)$: no $\sqrt N$ normalization, matching $\sigma^2(f)=\tfrac1{4\beta}$ exactly, with an $O(1/N)$ correction. The mean $\tfrac1\beta-\tfrac14$ carries the $\beta$-anomaly: it is $\tfrac14$ at $\beta=2$ (GUE), $\tfrac34$ at $\beta=1$, $-\tfrac18$ at $\beta=8$.

**Where the difficulty enters.** Everything above used the exact tridiagonal model, available only for $V$ quadratic. For $V(x)=x^4/4-x^2$ with a double well deep enough to split the support into two intervals, $\mathrm{Fluct}_N(f)$ acquires a term depending on $N\int_{\Sigma_0}d\mu_V \bmod 1$ and no longer converges; for $V$ tuned so that the density vanishes at $x=0$ like $x^2$, the variance formula above ceases to hold and the limit law is unknown for every $\beta\ne 2$. These are exactly the cases in the Gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*