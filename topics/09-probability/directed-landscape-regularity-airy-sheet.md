---
id: 09-probability/directed-landscape-regularity-airy-sheet
title: "Fluctuations of the Airy Sheet and Directed Landscape Regularity"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fluctuations of the Airy Sheet and Directed Landscape Regularity

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/directed-landscape-regularity-airy-sheet` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The **directed landscape** $\mathcal{L}$ is the scaling limit of last passage percolation and the conjectured universal space-time metric of the Kardar–Parisi–Zhang (KPZ) class. Its one-time marginal is the **Airy sheet** $\mathcal{S}$. Dauvergne–Ortmann–Virág (2022) proved $\mathcal{L}$ exists, is unique in law, and admits a continuous version that is Hölder-$(1/2)^-$ in the two spatial arguments and Hölder-$(1/3)^-$ in time. The open problem is to sharpen "$^-$" to exact statements:

1. **Exact spatial modulus.** Determine the a.s. constant $c$ in
$$\limsup_{\varepsilon \downarrow 0}\ \sup_{\substack{|y-y'|\le \varepsilon \\ y,y'\in[0,1]}} \frac{|\mathcal{S}(0,y)-\mathcal{S}(0,y')|}{\sqrt{\varepsilon\log(1/\varepsilon)}} = c \quad\text{a.s.},$$
and the analogous constant for the two-parameter sheet $(x,y)\mapsto \mathcal{S}(x,y)$, where the supremum over $x$ is expected to inflate the exponent of the logarithm.
2. **Exact temporal modulus.** Determine the a.s. sharp $\varphi$ with $\limsup_{\varepsilon\to0}\sup_{|t-t'|\le\varepsilon}|\mathcal{L}(0,t;0,1+t')|/\varphi(\varepsilon)\in(0,\infty)$, conjecturally $\varphi(\varepsilon)=\varepsilon^{1/3}(\log 1/\varepsilon)^{2/3}$.
3. **Exceptional-set geometry.** Compute the Hausdorff dimension of every set of space-time points at which the local modulus is atypically large, and of the sets carrying $k$ disjoint geodesics.

A complete solution means a proof of the exact constants and dimensions, not merely matching upper and lower bounds up to logarithms.

## 2. Mathematical Foundations

**Parameter space.** Let $\mathbb{R}^4_{\uparrow}=\{(x,s;y,t): s<t\}$. The directed landscape is a random continuous function $\mathcal{L}:\mathbb{R}^4_\uparrow\to\mathbb{R}$ satisfying:

* **Independent increments.** For disjoint time intervals, the restrictions of $\mathcal{L}$ are independent.
* **Metric composition (reverse triangle equality).**
$$\mathcal{L}(x,s;y,t)=\max_{z\in\mathbb{R}}\big(\mathcal{L}(x,s;z,r)+\mathcal{L}(z,r;y,t)\big),\qquad s<r<t.$$
* **Airy sheet marginals.** $\mathcal{L}(x,0;y,1)\overset{d}{=}\mathcal{S}(x,y)$, and by $1{:}2{:}3$ scaling
$$\mathcal{L}(x,s;y,s+t)\overset{d}{=}t^{1/3}\,\mathcal{S}\!\left(\frac{x}{t^{2/3}},\frac{y}{t^{2/3}}\right).$$

**Airy sheet.** $\mathcal{S}$ is characterized by: (i) $\mathcal{S}(x,y)=\mathcal{S}(0,y-x)$ in law as a process in $y$ for each fixed $x$; (ii) $y\mapsto\mathcal{S}(0,y)+y^2$ is the **Airy$_2$ process** $\mathcal{A}$ of Prähofer–Spohn, the top line of the Airy line ensemble, a stationary determinantal process with extended Airy kernel and one-point marginal $\mathcal{A}(y)\sim \mathrm{TW}_{\mathrm{GUE}}$:
$$\mathbb{P}(\mathcal{A}(0)\le s)=F_2(s)=\det(I-K_{\mathrm{Ai}})_{L^2(s,\infty)};$$
(iii) a monotonicity/shift-invariance condition fixing the joint law (DOV, Thm. 1.1).

**Brownian Gibbs property.** The Airy line ensemble $\{\mathcal{A}_i\}_{i\ge1}$, $\mathcal{A}_i(y)=\mathcal{L}_i(y)-y^2$ suitably normalized, is non-intersecting and, conditionally on the data outside a box, its lines are Brownian bridges of diffusivity $2$ conditioned not to cross (Corwin–Hammond 2014). This yields **Brownian absolute continuity**: on any compact interval, $\mathcal{A}(y)-\mathcal{A}(0)$ has a law mutually absolutely continuous with respect to Brownian motion of rate $2$, with $L^p$ Radon–Nikodym derivative for all $p<\infty$ (Hammond 2022).

**Geodesics.** For $(x,s;y,t)$ there a.s. exists a unique maximizing path $\pi$ with
$$\mathcal{L}(x,s;y,t)=\inf_{k}\inf_{s=t_0<\dots<t_k=t}\sum_{i=1}^{k}\mathcal{L}(\pi(t_{i-1}),t_{i-1};\pi(t_i),t_i),$$
and $\pi$ is Hölder-$(2/3)^-$ with a.s. $3/2$-variation (Dauvergne–Sarkar–Virág 2021).

**Difference profile.** $\mathcal{D}(y)=\mathcal{S}(1,y)-\mathcal{S}(-1,y)$ is a.s. non-decreasing; its Stieltjes measure $d\mathcal{D}$ is singular, supported on a random set of Hausdorff dimension $1/2$ (Basu–Ganguly–Hammond 2021).

## 3. History & State of the Art (SOTA)

* **2002.** Prähofer–Spohn introduce the Airy$_2$ process as the PNG droplet limit; local Brownian behaviour conjectured.
* **2005.** Johansson proves the Airy$_2$ process has a continuous version and $\arg\max$ uniqueness.
* **2014.** Corwin–Hammond construct the Airy line ensemble and prove the Brownian Gibbs property — the analytic engine for all later regularity work.
* **2018–2021.** Matetski–Quastel–Remenik construct the **KPZ fixed point** as a Markov process via exact Fredholm-determinant transition kernels (Acta Math. 2021).
* **2022.** Dauvergne–Ortmann–Virág construct the **directed landscape** from Brownian last passage percolation, prove uniqueness of the Airy sheet, and establish the $(1/2)^-$ / $(1/3)^-$ Hölder exponents with a metric-composition-based chaining argument.
* **2021–2023.** Sharp geodesic regularity ($3/2$-variation), fractal difference-profile results, disjoint-geodesic dimensions, and universality: Quastel–Sarkar (JAMS 2023) prove convergence of a class of exclusion processes to the KPZ fixed point; Virág and X. Wu prove convergence of the KPZ equation to the directed landscape.

SOTA is thus: existence, uniqueness, universality for several models, and *open* exponents up to logarithmic corrections; exact constants known only for one-parameter marginals in restricted regimes.

## 4. Partial Results / Verified Cases

| Object | Result | Source |
|---|---|---|
| $\mathcal{L}$ on compacts | Hölder $(1/2)^-$ in $x,y$; $(1/3)^-$ in $t$ | DOV 2022 |
| $\mathcal{A}$ on a compact interval | Absolutely continuous w.r.t. rate-2 Brownian motion; $L^p$ density for all $p<\infty$ | Hammond 2022 |
| Fixed $x$, one-parameter $y\mapsto\mathcal{S}(x,y)$ | Exact Lévy-type local modulus $\sqrt{4\varepsilon\log(1/\varepsilon)}$ inherited from Brownian motion on compacts | Corwin–Hammond 2014 + Hammond 2022 |
| KPZ fixed point, arbitrary initial data | $h(t,\cdot)$ locally absolutely continuous w.r.t. Brownian motion | Sarkar–Virág 2021 |
| Geodesics | $3/2$-variation exactly; Hölder $(2/3)^-$ sharp | Dauvergne–Sarkar–Virág 2021 |
| Difference profile $\mathcal{D}$ | $\mathrm{supp}(d\mathcal{D})$ has dimension $1/2$; local comparison to Brownian local time | Basu–Ganguly–Hammond 2021; Ganguly–Hegde 2023 |
| $k$ disjoint geodesics, $k=2,3$ | Endpoint-pair sets have Hausdorff dimension $4-k^2$ | Bates–Ganguly–Hammond 2022 |
| Tails | $\mathbb{P}(\mathcal{S}(0,0)>s)=e^{-\frac{4}{3}s^{3/2}(1+o(1))}$, $\mathbb{P}(\mathcal{S}(0,0)<-s)=e^{-\frac{1}{12}s^{3}(1+o(1))}$ | Tracy–Widom 1994; Ramírez–Rider–Virág |

## 5. Principal Obstacles

* **No exact formula for the two-parameter sheet.** Determinantal formulas exist for $y\mapsto\mathcal{S}(x_0,y)$ at a *single* $x_0$; the joint law in $x$ is only characterized abstractly by DOV's uniqueness theorem. Integrable methods (Fredholm determinants, Bethe ansatz) therefore cannot compute two-parameter modulus constants.
* **Brownian Gibbs is one-dimensional.** The Gibbs resampling property acts on lines indexed by $y$ at a fixed starting point. There is no known Gibbs-type resampling in the $x$ variable, so the powerful comparison-to-Brownian machinery does not extend to the sheet.
* **Radon–Nikodym derivatives are not uniformly integrable in the exceptional-set regime.** Brownian comparison loses events of probability $e^{-c\lambda^{3}}$ or smaller; extreme local oscillations, precisely those governing sharp constants and Hausdorff dimensions, live in that regime.
* **Temporal direction lacks a martingale/Markov handle at fixed space.** $t\mapsto\mathcal{L}(0,0;0,t)$ is neither Markov nor a semimartingale; metric composition gives only a supremum bound $\mathcal{L}(0,0;0,t+\varepsilon)\ge \max_z(\mathcal{L}(0,0;z,t)+\mathcal{L}(z,t;0,t+\varepsilon))$, producing the exponent $1/3$ but no matching lower bound with a constant.
* **Chaining is lossy.** The $(1/2)^-$ and $(1/3)^-$ exponents come from Kolmogorov-type chaining over dyadic grids; the union bound over $\sim\varepsilon^{-1}$ boxes costs exactly the logarithmic factor whose power is at issue.

## 6. The Gap

Proven: two-sided moment bounds of the form $\mathbb{P}(|\mathcal{S}(x,y)-\mathcal{S}(x,y')|>\lambda|y-y'|^{1/2})\le Ce^{-c\lambda^{3/2}}$, giving Hölder exponents $1/2^-$, $1/3^-$, $2/3^-$. Wanted: the *equality*
$$\limsup_{\varepsilon\downarrow 0}\ \sup_{|y-y'|\le\varepsilon}\frac{|\mathcal{S}(0,y)-\mathcal{S}(0,y')|}{\sqrt{\varepsilon\log(1/\varepsilon)}}=2\quad\text{a.s.}$$
(the Brownian-rate-$2$ Lévy constant) and its two-parameter analogue. The precise missing step is a **second-moment / correlation decay estimate for the sheet across the $x$ direction**: one must show that near-extremal oscillations at $(x,y)$ and $(x',y)$ decorrelate fast enough as $|x-x'|$ grows to run a Paley–Zygmund lower bound. Equivalently, a Brownian-Gibbs-like resampling in $x$, or an exact formula for $(\mathcal{S}(x,y),\mathcal{S}(x',y'))$, would close the gap.

## 7. Current Research (as of June 2026)

* **Toronto / Virág–Dauvergne school.** Wiener-density estimates for the Airy line ensemble give sharp Radon–Nikodym control against Brownian motion, pushing toward exact spatial constants *(frontier — verify)*.
* **Berkeley / Bangalore (Ganguly, Basu, Hegde, Hammond).** Fractal geometry programme: geodesic local time, exceptional-endpoint dimension spectra, space-time difference profiles.
* **Columbia / Toronto (Corwin, Hammond, Zhang).** Coupling and colouring arguments for multi-point sheet laws; shift-invariance identities of Borodin–Gorin–Wheeler used to extract joint distributions.
* **Universality frontier.** Extension of directed-landscape convergence beyond exactly solvable models (general LPP weight distributions) remains open and is the main obstacle to viewing the modulus problem as a statement about physical KPZ interfaces *(frontier — verify)*.
* **Half-space and multi-species landscapes.** Construction of a half-space directed landscape and of coloured/multi-species analogues, whose regularity is expected to match the full-space case.

## 8. Future Work

1. Establish a **resampling property in the $x$ variable** — an "Airy sheet Gibbs property" — perhaps via the Airy sheet's construction as a limit of Brownian melons under RSK.
2. Prove **exact temporal modulus** $\varepsilon^{1/3}(\log 1/\varepsilon)^{2/3}$ by combining the $e^{-c\lambda^{3}}$ lower-tail exponent with a decorrelation estimate for time increments.
3. Compute the **multifractal spectrum**: for $\alpha\in(0,1/2)$, the dimension of $\{y: \limsup |\mathcal{S}(0,y+\varepsilon)-\mathcal{S}(0,y)|/\varepsilon^{\alpha}>0\}$, expected to be $1-2\alpha$ style but unproven for the sheet.
4. Determine whether $\mathcal{L}$ is a **black noise** in Tsirelson's sense, which would rule out any Wiener-chaos representation and explain the failure of perturbative methods.
5. Extend all sharp results to the **KPZ equation at finite temperature**, where crossover kernels replace the Airy kernel.

## 9. Key References

- **[Foundational]** M. Prähofer, H. Spohn. *Scale invariance of the PNG droplet and the Airy process.* Journal of Statistical Physics 108 (2002), 1071–1106.
- **[Foundational]** C. Tracy, H. Widom. *Level-spacing distributions and the Airy kernel.* Communications in Mathematical Physics 159 (1994), 151–174.
- **[Foundational]** I. Corwin, A. Hammond. *Brownian Gibbs property for Airy line ensembles.* Inventiones Mathematicae 195 (2014), 441–508.
- **[Foundational]** D. Dauvergne, J. Ortmann, B. Virág. *The directed landscape.* Acta Mathematica 229 (2022), 201–285.
- **[SOTA / Recent]** K. Matetski, J. Quastel, D. Remenik. *The KPZ fixed point.* Acta Mathematica 227 (2021), 115–203.
- **[SOTA / Recent]** A. Hammond. *Brownian regularity for the Airy line ensemble, and multi-polymer watermelons in Brownian last passage percolation.* Memoirs of the American Mathematical Society, 2022.
- **[SOTA / Recent]** D. Dauvergne, S. Sarkar, B. Virág. *Three-halves variation of geodesics in the directed landscape.* Annals of Probability 49 (2021), 3006–3054.
- **[SOTA / Recent]** R. Basu, S. Ganguly, A. Hammond. *Fractal geometry of Airy$_2$ processes coupled via the Airy sheet.* Annals of Probability 49 (2021), 485–505.
- **[SOTA / Recent]** E. Bates, S. Ganguly, A. Hammond. *Hausdorff dimensions for shared endpoints of disjoint geodesics in the directed landscape.* Electronic Journal of Probability 27 (2022).
- **[SOTA / Recent]** S. Ganguly, M. Hegde. *Local and global comparisons of the Airy difference profile to Brownian local time.* Annales de l'Institut Henri Poincaré (B) 59 (2023).
- **[SOTA / Recent]** S. Sarkar, B. Virág. *Brownian absolute continuity of the KPZ fixed point with arbitrary initial condition.* Annals of Probability 49 (2021), 1718–1737.
- **[SOTA / Recent]** J. Quastel, S. Sarkar. *Convergence of exclusion processes and the KPZ equation to the KPZ fixed point.* Journal of the American Mathematical Society 36 (2023), 251–289.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universal fluctuations.* Random Matrices: Theory and Applications 1 (2012).
- **[Survey]** S. Ganguly. *Random metric geometries on the plane and Kardar–Parisi–Zhang universality.* Notices of the American Mathematical Society 69 (2022), 26–35.

## 10. Worked Example / Concrete Special Case

**Goal.** Show the one-parameter upper bound $\mathcal{S}(0,\cdot)$ is Hölder-$\alpha$ for every $\alpha<1/2$ on $[0,1]$, and see exactly where the logarithm resists sharpening.

Write $\mathcal{A}(y)=\mathcal{S}(0,y)+y^2$. Fix the compact interval $[0,1]$. By Hammond's comparison, the law of $B(y):=\mathcal{A}(y)-\mathcal{A}(0)$ on $C[0,1]$ satisfies $\mathbb{P}_{\mathcal{A}}(E)\le C\,\mathbb{P}_{W}(E)^{1-1/p}$ for a rate-$2$ Brownian motion $W$ and any $p<\infty$; take $p=2$, so
$$\mathbb{P}_{\mathcal{A}}(E)\le C\,\mathbb{P}_W(E)^{1/2}.$$

Let $E_{j,k}=\{|B(k2^{-j})-B((k-1)2^{-j})|>\lambda\, 2^{-j/2}\}$. For rate-$2$ Brownian motion, $\mathbb{P}_W(E_{j,k})\le 2e^{-\lambda^2/4}$. Hence $\mathbb{P}_{\mathcal{A}}(E_{j,k})\le C'e^{-\lambda^2/8}$.

Choose $\lambda=\lambda_j=\sqrt{8(1+\delta)j\log 2}$. Then $\mathbb{P}_{\mathcal{A}}(E_{j,k})\le C'2^{-(1+\delta)j}$ and a union bound over the $2^j$ intervals at level $j$ gives
$$\mathbb{P}_{\mathcal{A}}\Big(\bigcup_{k\le 2^j}E_{j,k}\Big)\le C'2^{-\delta j},$$
summable in $j$. Borel–Cantelli: a.s. for large $j$, every dyadic increment at scale $2^{-j}$ is at most $\sqrt{8(1+\delta)\log 2}\;\sqrt{j}\,2^{-j/2}$. Standard chaining (summing the geometric series $\sum_{j\ge J}\sqrt{j}\,2^{-j/2}$) upgrades this to
$$|\mathcal{A}(y)-\mathcal{A}(y')|\le C_\delta\,|y-y'|^{1/2}\sqrt{\log(1/|y-y'|)}\quad\text{for }|y-y'|\text{ small},$$
so $\mathcal{S}(0,\cdot)=\mathcal{A}(\cdot)-(\cdot)^2$ is Hölder-$\alpha$ for all $\alpha<1/2$.

**Where sharpness is lost.** The constant obtained is $C_\delta\ge\sqrt{8\log 2}\approx 2.35$, whereas Lévy's theorem for rate-$2$ Brownian motion gives the exact value $2$. Two losses occur: (i) the exponent $1/2$ from $p=2$ in the Radon–Nikodym bound halves the Gaussian exponent ($e^{-\lambda^2/4}\to e^{-\lambda^2/8}$); (ii) the union bound ignores correlations between adjacent increments. Letting $p\to\infty$ recovers exponent $e^{-\lambda^2/4(1-1/p)}$ and hence the constant $2$ *for the one-parameter marginal*. For the **two-parameter sheet** step (i) has no analogue at all — there is no Brownian comparison in $x$ — so even the correct power of $\log(1/\varepsilon)$ in $\sup_{x,|y-y'|\le\varepsilon}|\mathcal{S}(x,y)-\mathcal{S}(x,y')|$ is unknown. That is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*