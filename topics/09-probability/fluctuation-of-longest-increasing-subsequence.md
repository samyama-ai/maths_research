---
id: 09-probability/fluctuation-of-longest-increasing-subsequence
title: "Fluctuation of Longest Increasing Subsequence"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fluctuation of Longest Increasing Subsequence

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/fluctuation-of-longest-increasing-subsequence` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\sigma$ be uniform on the symmetric group $S_n$ and let
$$L_n(\sigma)=\max\{k:\ \exists\, i_1<\dots<i_k \text{ with } \sigma(i_1)<\dots<\sigma(i_k)\}.$$
**Ulam's problem** (1961) asks for the distribution of $L_n$. The law-of-large-numbers part, $L_n/\sqrt n\to 2$, was settled in 1977. The **fluctuation problem** — the order and limit law of $L_n-2\sqrt n$ — was resolved by Baik, Deift and Johansson (1999):
$$\frac{L_n-2\sqrt n}{n^{1/6}}\ \xrightarrow{\ d\ }\ \mathrm{TW}_{\mathrm{GUE}},$$
the Tracy–Widom $F_2$ law, with convergence of all moments.

The entry is marked **solved-recently** because the uniform case is a theorem, while the surrounding programme is open. The live questions are: (i) the exact **rate** of convergence and the full asymptotic expansion of $\mathbb{P}(L_n\le \ell)$ in powers of $n^{-1/3}$; (ii) **universality** — does the same $n^{1/6}$/$F_2$ answer hold for non-uniform permutation measures (Mallows, Ewens, conjugacy-invariant, pattern-avoiding) and for random words; (iii) the **$d\ge 3$ Bollobás–Winkler problem**, where even the fluctuation exponent is unknown. A complete resolution of (iii) means identifying $\alpha_d$ with $\mathrm{Var}\,L^{(d)}_n=n^{2\alpha_d+o(1)}$ and the limit law.

## 2. Mathematical Foundations

**RSK and Plancherel measure.** The Robinson–Schensted correspondence is a bijection $\sigma\mapsto(P,Q)$ onto pairs of standard Young tableaux of the same shape $\lambda\vdash n$, with $L_n(\sigma)=\lambda_1$. Hence
$$\mathbb{P}(\lambda)=\frac{(f^\lambda)^2}{n!},\qquad \mathbb{P}(L_n\le \ell)=\frac{1}{n!}\sum_{\lambda\vdash n,\ \lambda_1\le \ell}(f^\lambda)^2,$$
the **Plancherel measure** on $\mathbb{Y}_n$, $f^\lambda$ the hook-length count.

**Poissonization and Gessel's determinant.** Let $N\sim\mathrm{Poisson}(\lambda)$ and $L(\lambda)=L_N$. Gessel's identity (1990) gives
$$\sum_{n\ge 0}\frac{\lambda^n}{(n!)^2}\,\bigl|\{\sigma\in S_n:L_n\le \ell\}\bigr| = D_\ell(\lambda)=\det\bigl(I_{j-k}(2\sqrt\lambda)\bigr)_{j,k=0}^{\ell-1},$$
a Toeplitz determinant with symbol $e^{2\sqrt\lambda\cos\theta}$ ($I_m$ = modified Bessel). Equivalently $e^{-\lambda}D_\ell(\lambda)=\mathbb{P}(L(\lambda)\le\ell)$.

**Hammersley's process.** Equivalently, $L(\lambda)$ is the maximal number of points on an increasing (north-east) chain of a rate-1 Poisson process in $[0,\sqrt\lambda\,]^2$ — a last-passage percolation model whose interface obeys KPZ scaling: longitudinal $n$, transversal $n^{2/3}$, fluctuation $n^{1/3}$ (here $n\leftrightarrow\sqrt{\lambda}$, so $\lambda^{1/6}$).

**Limit law.** With $F_2(s)=\exp\!\left(-\int_s^\infty (x-s)q(x)^2dx\right)$, $q$ the Hastings–McLeod solution of Painlevé II $q''=sq+2q^3$, $q(s)\sim\mathrm{Ai}(s)$ at $+\infty$ (Tracy–Widom 1994). Then $\mathbb{P}\bigl((L_n-2\sqrt n)n^{-1/6}\le s\bigr)\to F_2(s)$, with $\mu_2=\int s\,dF_2\approx-1.771087$, $\mathrm{Var}(F_2)\approx 0.81320$. Hence
$$\mathbb{E}L_n = 2\sqrt n+\mu_2 n^{1/6}+o(n^{1/6}),\qquad \mathrm{Var}\,L_n\sim 0.8132\, n^{1/3}.$$

## 3. History & State of the Art (SOTA)

- **1961** — Ulam raises the problem; Monte Carlo suggests $\mathbb{E}L_n\approx c\sqrt n$.
- **1972** — Hammersley proves $L_n/\sqrt n\to c$ a.s. by subadditivity, with $\pi/2\le c\le e$, and introduces the interacting-particle picture.
- **1977** — Logan–Shepp and (independently) Vershik–Kerov prove $c=2$ by solving a variational problem for the limit shape of Plancherel-typical Young diagrams.
- **1991–1996** — Concentration era: Frieze, Bollobás–Brightwell and Talagrand's isoperimetric inequality give $L_n$ concentrated on scale $n^{1/4}$; J. H. Kim obtains exponential tail bounds. The true $n^{1/6}$ scale stays out of reach.
- **1995** — Aldous–Diaconis give a soft hydrodynamic proof of $c=2$ via Hammersley's process.
- **1999** — Baik–Deift–Johansson: Riemann–Hilbert steepest descent (Deift–Zhou) applied to the Bessel-symbol Toeplitz determinant yields $F_2$, plus moment convergence and de-Poissonization.
- **2000–2001** — Three independent routes to the edge of the Plancherel measure: Okounkov (random matrices/maps), Borodin–Okounkov–Olshanski (discrete sine and Airy kernels), Johansson (discrete orthogonal polynomial ensembles). Baik–Rains handle symmetrized versions (involutions, symmetry classes) giving $F_1$, $F_4$ and interpolating laws.
- **2015** — Romik's monograph consolidates the field.
- **2024** — Bornemann derives rigorous asymptotic expansions for the distribution and moments in powers of $n^{-1/3}$, with numerically validated coefficients.

## 4. Partial Results / Verified Cases

- **Uniform $S_n$ (fully solved).** $F_2$ limit with all moments (BDJ 1999). Multi-row extension: $(\lambda_1,\dots,\lambda_k)$ jointly converge, after $2\sqrt n+n^{1/6}\,\cdot$ scaling, to the top $k$ GUE Tracy–Widom eigenvalues / Airy point process (BOO 2000; Johansson 2001).
- **Symmetry classes (solved).** Random involutions: $L_n$ fluctuates on scale $n^{1/6}$ with $F_1$ (GOE) or $F_4$ (GSE) limits depending on the number of fixed points; Baik–Rains (2001) give the full one-parameter family, including the crossover $F^{\mathrm{GOE}}$–$F_2$ when fixed points number $\asymp\sqrt n$.
- **Poissonized model (solved).** $\mathbb{P}(L(\lambda)\le\ell)$ is exactly $e^{-\lambda}\det(I_{j-k}(2\sqrt\lambda))$ for every $\ell,\lambda$; determinantal formulas are exact, not asymptotic.
- **Small $n$ (exact).** Distributions of $L_n$ computed exactly to $n\approx 10^2$ by summing $(f^\lambda)^2$; Odlyzko–Rains computed $\mathbb{E}L_n$ for $n$ up to $10^{10}$ by Monte Carlo/patience-sorting and confirmed the $2\sqrt n+\mu_2n^{1/6}$ two-term law.
- **Non-uniform, partially solved.** Mallows measure with $q=1-\beta/n$: $L_n\asymp\sqrt n$ with a $\beta$-dependent constant (Mueller–Starr 2013); in the regime $n(1-q)\to\infty$ the order changes and limit theorems are known (Basu–Bhatnagar 2017), but Tracy–Widom fluctuations are proved only in restricted regimes. Conjugacy-invariant permutations with few long cycles: $F_2$ limit transfers (Kammoun 2018).
- **Rate of convergence.** $O(n^{-1/3+\varepsilon})$-type bounds and full expansions in $n^{-1/3}$ (Bornemann 2024); a Berry–Esseen-type optimal constant is not established.
- **Higher dimensions.** Bollobás–Winkler (1988): for the longest chain among $n$ uniform points in $[0,1]^d$, $L_n^{(d)}/n^{1/d}\to c_d$ with $c_d\uparrow e$. Fluctuations known only for $d=2$.

## 5. Principal Obstacles

- **Concentration inequalities cannot see $n^{1/6}$.** Talagrand's convex-distance and bounded-differences methods bound the fluctuation by $\sqrt{\mathbb{E}L_n}\asymp n^{1/4}$, since changing one point changes $L_n$ by at most $1$ and the certificate has size $L_n$. This is provably the ceiling for such arguments; the extra cancellation producing $n^{1/6}$ is not a Lipschitz phenomenon.
- **Subadditivity gives no second order.** Kingman-type arguments yield the constant $2$ but are insensitive to $o(\sqrt n)$ corrections.
- **Integrability is fragile.** Every proof of $F_2$ uses an exact algebraic identity — Gessel's Toeplitz determinant, the Plancherel measure's determinantal structure, or Schur-function expansions. Perturbing the measure (Mallows, Ewens, pattern-avoidance) or the geometry ($d\ge 3$) destroys the determinantal/Pfaffian structure, and no robust replacement exists.
- **No $d\ge3$ solvable model.** In $d\ge 3$ there is no analogue of RSK: the chain-length statistic is not a Schur-measure observable. Even the exponent $\alpha_d$ is conjectural, and the variational problem determining $c_d$ has no closed form.
- **Coupling/comparison arguments lose the exponent.** Sandwiching a non-uniform measure between uniform ones perturbs the mean at order $\sqrt n$, swamping the $n^{1/6}$ signal, so universality cannot be obtained by naive comparison.

## 6. The Gap

For uniform $\sigma\in S_n$ there is no gap: Section 1's statement is a theorem. The residual boundaries are:

1. **Universality gap.** Proved: $F_2$ for measures with exact determinantal structure (uniform, involutions, and near-uniform conjugacy classes). Conjectured: $F_2$ for all "sufficiently mixing" permutation measures at scale $n^{1/6}$. Missing step: a KPZ-universality theorem for last-passage percolation with general point processes — the same barrier as in the Sepp\"al\"ainen–Corwin programme.
2. **Dimension gap.** Proved: $d=2$ exact. Conjectured: $\mathrm{Var}\,L^{(d)}_n=n^{2\alpha_d+o(1)}$ with $\alpha_d<1/(2d)$ decreasing; no rigorous non-trivial upper bound below the trivial $n^{1/(2d)}$ concentration bound is known for $d\ge3$. Missing step: an integrable or hydrodynamic handle on $d$-dimensional chain growth.
3. **Expansion gap.** Bornemann's expansions supply coefficients in $n^{-1/3}$; a fully rigorous, uniform-in-$s$ error control with explicit constants for all orders is still incomplete *(frontier — verify)*.

## 7. Current Research (as of June 2026)

- **Finite-size corrections and numerics.** Bornemann (TU München) — rigorous asymptotic expansions $\mathbb{P}(L_n\le \ell)=F_2(s)+n^{-1/3}F_1^{(1)}(s)+\dots$, high-precision evaluation of Painlevé II and of expected values; extended to symmetry classes and to hard-edge analogues *(frontier — verify)*.
- **KPZ universality school.** Corwin, Hammond, Quastel, Remenik, Virág, Sarkar, Basu, Ganguly — the directed landscape and KPZ fixed point as universal scaling limits; Hammersley's process is one of the few models where convergence to the directed landscape is accessible, and papers extending $F_2$ to perturbed Hammersley models are active.
- **Non-uniform permutation measures.** Bhattacharya, Mukherjee, Bhatnagar, Kammoun, Starr — Mallows and Ewens LIS; permutons and the "LIS of a permuton-sampled permutation" question (Dubach, Borga, Maazoun) *(frontier — verify)*.
- **Pattern-avoiding permutations.** Madras, Pehlivan, Miner, Pak — $L_n$ for $\sigma$ avoiding a fixed pattern grows like $c\sqrt n$ or $\Theta(n)$ depending on the class; fluctuation laws largely open.
- **Higher dimensions and posets.** Groups in Cambridge and Tel Aviv on chain lengths in random $d$-dimensional point sets and in random graph orders.

## 8. Future Work

- Prove $F_2$ fluctuations for **Hammersley-type processes with general (non-Poisson) point measures**, the natural universality statement.
- Establish **sharp Berry–Esseen bounds**: show $\sup_s|\mathbb{P}((L_n-2\sqrt n)n^{-1/6}\le s)-F_2(s)|\asymp n^{-1/3}$ with an explicit constant.
- Obtain a **non-integrable proof** of the $1/3$ exponent for LIS — e.g. via geodesic-coalescence and multi-scale arguments — which would likely transfer to $d\ge 3$.
- Determine $c_3$ (the 3-dimensional Bollobás–Winkler constant) to provable accuracy, and prove any bound $\mathrm{Var}\,L^{(3)}_n=o(n^{1/6})$.
- Extend to **LIS in random words** over a finite alphabet at critical alphabet size $\asymp\sqrt n$, where a crossover between Gaussian and Tracy–Widom behaviour is predicted (Its–Tracy–Widom; Houdré–Litherland).

## 9. Key References

- **[Foundational]** J. M. Hammersley. *A few seedlings of research.* Proc. Sixth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1, 345–394, Univ. California Press, 1972.
- **[Foundational]** B. F. Logan and L. A. Shepp. *A variational problem for random Young tableaux.* Advances in Mathematics 26 (1977), 206–222.
- **[Foundational]** A. M. Vershik and S. V. Kerov. *Asymptotics of the Plancherel measure of the symmetric group and the limiting form of Young tableaux.* Soviet Mathematics Doklady 18 (1977), 527–531.
- **[Foundational]** I. M. Gessel. *Symmetric functions and P-recursiveness.* Journal of Combinatorial Theory Series A 53 (1990), 257–285.
- **[Foundational]** C. A. Tracy and H. Widom. *Level-spacing distributions and the Airy kernel.* Communications in Mathematical Physics 159 (1994), 151–174.
- **[SOTA]** J. Baik, P. Deift and K. Johansson. *On the distribution of the length of the longest increasing subsequence of random permutations.* Journal of the American Mathematical Society 12 (1999), 1119–1178.
- **[SOTA]** A. Borodin, A. Okounkov and G. Olshanski. *Asymptotics of Plancherel measures for symmetric groups.* Journal of the AMS 13 (2000), 481–515.
- **[SOTA]** A. Okounkov. *Random matrices and random permutations.* International Mathematics Research Notices 2000, no. 20, 1043–1095.
- **[SOTA]** K. Johansson. *Discrete orthogonal polynomial ensembles and the Plancherel measure.* Annals of Mathematics 153 (2001), 259–296.
- **[SOTA]** J. Baik and E. M. Rains. *Algebraic aspects of increasing subsequences.* Duke Mathematical Journal 109 (2001), 1–65.
- **[SOTA / Recent]** F. Bornemann. *Asymptotic expansions relating to the distribution of the length of longest increasing subsequences.* Forum of Mathematics, Sigma 12 (2024), e36.
- **[Recent]** C. Mueller and S. Starr. *The length of the longest increasing subsequence of a random Mallows permutation.* Journal of Theoretical Probability 26 (2013), 514–540.
- **[Recent]** R. Basu and N. Bhatnagar. *Limit theorems for longest monotone subsequences in random Mallows permutations.* Annales de l'Institut Henri Poincaré (B) 53 (2017), 1934–1951.
- **[Survey]** D. Aldous and P. Diaconis. *Longest increasing subsequences: from patience sorting to the Baik–Deift–Johansson theorem.* Bulletin of the AMS 36 (1999), 413–432.
- **[Survey / Book]** D. Romik. *The Surprising Mathematics of Longest Increasing Subsequences.* Cambridge University Press, 2015.
- **[Related]** B. Bollobás and P. Winkler. *The longest chain among random points in Euclidean space.* Proceedings of the AMS 103 (1988), 347–353.

## 10. Worked Example / Concrete Special Case

**Exact law at $n=3$ via RSK.** Partitions of $3$ and their standard-tableaux counts: $f^{(3)}=1$, $f^{(2,1)}=2$, $f^{(1,1,1)}=1$, and $1^2+2^2+1^2=6=3!$. Since $L_3=\lambda_1$:
$$\mathbb{P}(L_3=3)=\tfrac16,\quad \mathbb{P}(L_3=2)=\tfrac{4}{6},\quad \mathbb{P}(L_3=1)=\tfrac16 .$$
Direct check: $L=3$ only for $123$; $L=1$ only for $321$; the other four permutations ($132,213,231,312$) have $L=2$. Hence $\mathbb{E}L_3=(3+8+1)/6=2$ and $\mathrm{Var}\,L_3=1/3$. The asymptotic prediction $2\sqrt 3\approx 3.464$ is useless here — the $F_2$ regime is genuinely asymptotic.

**Toeplitz check at $\ell=1$.** Gessel's determinant with $\ell=1$ is the $1\times1$ determinant $D_1(\lambda)=I_0(2\sqrt\lambda)=\sum_{n\ge0}\lambda^n/(n!)^2$. The coefficient of $\lambda^n/(n!)^2$ is $1$, matching $|\{\sigma:L_n\le1\}|=1$ (only the reversal). For $\ell=2$, $D_2(\lambda)=I_0^2-I_1^2$, whose expansion gives $|\{L_n\le 2\}|=C_n$, the Catalan number (Erdős–Szekeres/RSK: $\lambda_1\le2$ forces at most two rows).

**Two-term law at large $n$.** For $n=10^6$:
$$\mathbb{E}L_n\approx 2\sqrt{10^6}+\mu_2 (10^6)^{1/6}=2000+(-1.771087)(10)=1982.29,$$
$$\mathrm{sd}(L_n)\approx\sqrt{0.8132}\,(10^6)^{1/6}=0.9018\times10=9.02 .$$
Monte Carlo estimates of $\mathbb{E}L_n$ (Odlyzko–Rains) agree with $1982.29$ to within the next-order $O(n^{-1/6}\cdot n^{1/6})=O(1)$ correction supplied by Bornemann's expansion. Note the scale separation: the mean is $\sim 2\times10^3$ while the fluctuation is $\sim 9$ — a relative fluctuation $n^{-1/3}$, far below the $n^{-1/4}$ that Talagrand's inequality alone can certify. That $n^{1/4}\to n^{1/6}$ improvement is exactly the content of the theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*