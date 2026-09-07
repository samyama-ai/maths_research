---
id: 09-probability/fractional-brownian-motion-local-time-existence
title: "Fractional Brownian Motion Local Time Existence"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fractional Brownian Motion Local Time Existence

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/fractional-brownian-motion-local-time-existence` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $B^H = \{B^H_t, t \ge 0\}$ be a $d$-dimensional fractional Brownian motion (fBm) with Hurst index $H \in (0,1)$: $d$ independent copies of a centred Gaussian process with $\mathbb{E}[B_sB_t] = \tfrac12(s^{2H}+t^{2H}-|t-s|^{2H})$.

**Question.** For which pairs $(H,d)$ does the occupation measure
$$\mu_T(A) = \lambda_1\{ s \in [0,T] : B^H_s \in A\}, \qquad A \in \mathcal{B}(\mathbb{R}^d),$$
admit a density $L(x,T)$ with respect to Lebesgue measure on $\mathbb{R}^d$ — the **local time** — and when is that density jointly continuous in $(x,T)$ with a sharp modulus?

The folklore answer is the **dimension criterion**: local time exists (a.s., in $L^2(dP \times dx)$) iff $Hd < 1$, and fails iff $Hd > 1$. The genuinely hard part is the **critical case $Hd = 1$**, i.e. $d = 1/H$ with $1/H \in \mathbb{N}$. A complete resolution requires proving or disproving that single points are polar for $B^H$ when $Hd=1$, since non-polarity of points is equivalent (for these self-similar Gaussian fields) to the occupation measure being a.s. absolutely continuous. The critical case was settled — points are polar, no local time exists — by Dalang, Mueller and Xiao (2017). Residual open problems concern exact moduli, anisotropic and multi-parameter extensions, and renormalized self-intersection local times at criticality.

## 2. Mathematical Foundations

**fBm.** $B^{H}$ is the unique (up to scale) centred Gaussian self-similar process with stationary increments and index $H$:
$$\{B^H_{at}\}_{t\ge0} \stackrel{d}{=} \{a^H B^H_t\}_{t\ge0}, \qquad \mathbb{E}\|B^H_t - B^H_s\|^2 = d\,|t-s|^{2H}.$$
$H=\tfrac12$ recovers Brownian motion. Moving-average representation (Mandelbrot–Van Ness):
$$B^H_t = C_H \int_{-\infty}^{0}\!\big[(t-u)^{H-1/2}-(-u)^{H-1/2}\big]dW_u + C_H\!\int_0^t (t-u)^{H-1/2}dW_u .$$
For $H \ne \tfrac12$, $B^H$ is neither Markov nor a semimartingale.

**Occupation density.** $L(\cdot,T)$ is the Radon–Nikodym derivative $d\mu_T/d\lambda_d$, characterised by the occupation formula
$$\int_0^T f(B^H_s)\,ds = \int_{\mathbb{R}^d} f(x)L(x,T)\,dx \quad \text{for all bounded Borel } f.$$

**Berman's Fourier criterion** (Berman 1969, 1973; Geman–Horowitz 1980). Writing formally
$$L(x,T) = (2\pi)^{-d}\int_{\mathbb{R}^d}\int_0^T e^{-i\langle \xi,x\rangle}e^{i\langle \xi,B^H_s\rangle}\,ds\,d\xi,$$
Plancherel gives
$$\mathbb{E}\int_{\mathbb{R}^d} L(x,T)^2\,dx = (2\pi)^{-d}\int_{\mathbb{R}^d}\!\!\int_0^T\!\!\int_0^T e^{-\frac{|\xi|^2}{2}|t-s|^{2H}}ds\,dt\,d\xi = (2\pi)^{-d/2}\!\int_0^T\!\!\int_0^T \!|t-s|^{-Hd}\,ds\,dt. \tag{2.1}$$
The right side is finite iff $Hd<1$. So $Hd<1 \Rightarrow$ existence in $L^2$; $Hd \ge 1 \Rightarrow$ the second moment diverges, which by itself does **not** prove non-existence.

**Strong local nondeterminism (SLND)** (Pitt 1978). There is $\kappa = \kappa(H,d)>0$ with
$$\operatorname{Var}\big(B^{H,1}_t \mid B^{H,1}_{s_1},\dots,B^{H,1}_{s_n}\big) \ \ge\ \kappa \min_{1\le j\le n}|t-s_j|^{2H}. \tag{2.2}$$
SLND replaces the Markov property and drives all sharp moment estimates for $L$.

**Potential theory.** For $F=B^H$ on $[a,b]\subset(0,\infty)$ and compact $E\subset\mathbb{R}^d$,
$$c_1\,\mathcal{C}_{d-1/H}(E) \ \le\ \mathbb{P}\{F([a,b])\cap E \ne \emptyset\} \ \le\ c_2\,\mathcal{C}_{d-1/H}(E), \tag{2.3}$$
with $\mathcal{C}_\alpha$ the Bessel–Riesz capacity of order $\alpha$ (logarithmic when $\alpha=0$). Points have positive capacity iff $d<1/H$; the case $d=1/H$ is exactly the capacity-zero boundary where (2.3) is uninformative.

## 3. History & State of the Art (SOTA)

- **1940** — Kolmogorov introduces the "Wiener spiral" ($=$ fBm) in Hilbert space.
- **1948, 1958** — Lévy constructs Brownian local time; Trotter proves joint continuity in $(x,t)$ for $d=1$.
- **1968** — Mandelbrot and Van Ness give the moving-average representation and the name.
- **1969–1973** — Berman develops the Fourier/local-nondeterminism method, proving existence and joint continuity of local times for Gaussian processes; for one-dimensional fBm, $L(x,t)$ is jointly continuous for every $H\in(0,1)$.
- **1978** — Pitt establishes SLND (2.2) for fBm and gets existence and joint continuity for $Hd<1$ in all dimensions.
- **1980** — Geman–Horowitz survey axiomatises occupation densities.
- **1995–1997** — Talagrand's covering method gives exact Hausdorff measure of the range; Xiao obtains local and uniform Hölder conditions for $L$.
- **2002–2009** — Extensions to fractional Brownian sheets and anisotropic Gaussian fields (Xiao–Zhang; Ayache–Wu–Xiao; Baraka–Mountford–Xiao).
- **2005** — Hu–Nualart resolve existence of the *renormalized self-intersection* local time for $Hd<3/2$.
- **2017** — **Dalang, Mueller, Xiao** prove polarity of points in the critical dimension $d=1/H$ for fBm and a class of Gaussian random fields, closing the last gap in the existence dichotomy.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $d=1$, all $H\in(0,1)$ | $L(x,t)$ exists, jointly continuous, Hölder of order $<1-H$ in $x$ (Berman 1973; Xiao 1997) |
| $Hd<1$, any $d\ge1$ | Exists in $L^2$ by (2.1); jointly continuous; all moments finite (Pitt 1978) |
| $Hd>1$ | Points polar, range has zero Lebesgue measure, no occupation density (capacity criterion (2.3)) |
| $Hd=1$ (e.g. $H=\tfrac12,d=2$; $H=\tfrac13,d=3$; $H=\tfrac14,d=4$) | **Points polar** — no local time (Dalang–Mueller–Xiao 2017); classical for $H=\tfrac12$ (Kakutani) |
| $Hd<3/2$ | Renormalized self-intersection local time exists (Hu–Nualart 2005) |
| $Hd<1$, exact modulus | $\limsup_{r\to0} L(B(x,r),1)/(r^d(\log\log 1/r)^{Hd})$ finite and positive (Baraka–Mountford–Xiao 2009) |
| Fractional Brownian sheets $\prod H_j$, $\sum_j 1/H_j > d$ | Local time exists and is jointly continuous (Ayache–Wu–Xiao 2008) |
| SDEs $dX = \sigma(X)dB^H + b(X)dt$, elliptic $\sigma$, $H>1/2$, $Hd<1$ | Local time exists, is Hölder continuous (Lou–Ouyang 2017) |

## 5. Principal Obstacles

- **The second-moment method dies at criticality.** Paley–Zygmund / capacity lower bounds in (2.3) need $\mathcal{C}_{d-1/H}(\{x\})>0$. At $d=1/H$ the relevant kernel is logarithmic and capacity is zero, so both directions of the standard argument are vacuous. Divergence of (2.1) is consistent with existence of a local time that is merely $L^1$, so it proves nothing.
- **No Markov property, no Green function.** For $H\ne\tfrac12$, classical potential theory (excessive functions, Choquet capacity of the process's own semigroup, Itô–Tanaka) is unavailable. Everything must be built from Gaussian correlations, i.e. from SLND (2.2).
- **Scaling gives an exactly critical, non-summable series.** Self-similarity turns the hitting problem into a sum over dyadic scales whose terms are $\asymp 1/n$ at $Hd=1$: convergent-or-not depends on constants no soft argument controls. Dalang–Mueller–Xiao needed a delicate covering argument plus sharp small-ball/hitting estimates uniform in scale.
- **Anisotropy breaks scaling entirely.** For sheets and multifractional fields there is no single self-similarity index; sector conditions and time-inhomogeneous SLND must be established case by case.
- **Renormalization at criticality.** Self-intersection local times require subtracting divergent expectations; at $Hd=3/2$ the Wiener-chaos expansion has a logarithmically divergent second chaos, and no canonical normalization is known.

## 6. The Gap

The existence dichotomy is now complete: local time exists $\iff Hd<1$. The remaining gap is quantitative and structural:

1. **Exact uniform modulus.** Local (law of the iterated logarithm) moduli are sharp; the *uniform* modulus $\sup_x$ over $x\in\mathbb{R}^d$ is known only up to the constant, and the exact Hausdorff measure function of the level set $\{t: B^H_t=x\}$ for $d\ge2$ is open.
2. **Critical self-intersections.** Existence/renormalization at $Hd=3/2$ and beyond.
3. **Beyond Gaussian.** Transfer to solutions of rough differential equations driven by $B^H$ with $H<1/4$, where no SLND is available for the solution.

## 7. Current Research (as of June 2026)

- **Potential theory of Gaussian fields.** Dalang (EPFL), Mueller (Rochester), Xiao (Michigan State) continue the critical-dimension programme, extending polarity results to systems of stochastic heat and wave equations, where the solution behaves like an anisotropic fBm.
- **Malliavin calculus and chaos expansions.** Nualart-school work (Hu, Song, Xu) on limit theorems for additive functionals $\int_0^T f(B^H_s)ds$, with the local time appearing as the limit object; central and non-central limit theorems depend on $Hd$ crossing thresholds.
- **Rough paths and regularization by noise.** Local time and its space regularity are the key input to Catellier–Gubinelli-type results: fBm regularises ODEs precisely because $L(x,t)$ is $\rho$-irregular. Sharp $H$-dependent thresholds are being pushed. *(frontier — verify)*
- **Anisotropic and operator-scaling fields.** Existence and joint continuity criteria for operator-scaling stable and Gaussian fields, where the condition $Hd<1$ becomes $\sum_j 1/H_j > d$. *(frontier — verify)*
- **Numerical/statistical use.** Local-time estimators of $H$ from a single path, and occupation-time functionals in long-memory finance models.

## 8. Future Work

- Determine the exact Hausdorff measure function for level sets $L_x = \{t\in[0,1] : B^H_t = x\}$ when $2 \le d < 1/H$; only the dimension $1-Hd$ is known.
- Establish a Tanaka-type formula and an Itô–Tanaka calculus for $H<1/4$ in $d\ge2$, where existing divergence-integral techniques fail.
- Resolve renormalized self-intersection local time at the critical exponent $Hd=3/2$ and identify the correct centring.
- Prove a critical-dimension polarity theorem for general anisotropic Gaussian fields with only *approximate* SLND, removing the self-similarity crutch.
- Quantify the modulus of continuity in $x$ of $L(x,T)$ uniformly, with matching upper and lower constants.

## 9. Key References

- **[Foundational]** A. N. Kolmogorov. *Wienersche Spiralen und einige andere interessante Kurven im Hilbertschen Raum.* C. R. (Doklady) Acad. Sci. URSS 26 (1940), 115–118.
- **[Foundational]** B. B. Mandelbrot, J. W. Van Ness. *Fractional Brownian motions, fractional noises and applications.* SIAM Review 10 (1968), 422–437.
- **[Foundational]** S. M. Berman. *Local nondeterminism and local times of Gaussian processes.* Indiana University Mathematics Journal 23 (1973), 69–94.
- **[Foundational]** L. D. Pitt. *Local times for Gaussian vector fields.* Indiana University Mathematics Journal 27 (1978), 309–330.
- **[Survey]** D. Geman, J. Horowitz. *Occupation densities.* Annals of Probability 8 (1980), 1–67.
- **[Survey]** Y. Xiao. *Sample path properties of anisotropic Gaussian random fields.* In: A Minicourse on Stochastic Partial Differential Equations, Lecture Notes in Mathematics 1962, Springer, 2009, 145–212.
- **[Book]** M. B. Marcus, J. Rosen. *Markov Processes, Gaussian Processes, and Local Times.* Cambridge University Press, 2006.
- **[Book]** D. Nualart. *The Malliavin Calculus and Related Topics.* 2nd ed., Springer, 2006.
- **[SOTA]** R. C. Dalang, C. Mueller, Y. Xiao. *Polarity of points for Gaussian random fields.* Annals of Probability 45 (2017), 4700–4751.
- **[SOTA]** Y. Hu, D. Nualart. *Renormalized self-intersection local time for fractional Brownian motion.* Annals of Probability 33 (2005), 948–983.
- **[SOTA]** A. Ayache, D. Wu, Y. Xiao. *Joint continuity of the local times of fractional Brownian sheets.* Annales de l'IHP Probabilités et Statistiques 44 (2008), 727–748.
- **[Recent]** D. Baraka, T. Mountford, Y. Xiao. *Hölder properties of local times for fractional Brownian motions.* Metrika 69 (2009), 125–152.
- **[Recent]** M. Talagrand. *Hausdorff measure of trajectories of multiparameter fractional Brownian motion.* Annals of Probability 23 (1995), 767–775.
- **[Recent]** Y. Hu, D. Nualart, F. Xu. *Central limit theorem for an additive functional of the fractional Brownian motion.* Annals of Probability 42 (2014), 168–203.

## 10. Worked Example / Concrete Special Case

**Take $H=1/3$, $d=2$, $T=1$.** Then $Hd = 2/3 < 1$, so a local time should exist. Evaluate (2.1) explicitly.

Step 1 — Gaussian integral in $\xi$. Since $B^H_t-B^H_s \sim N(0,|t-s|^{2/3}I_2)$,
$$\int_{\mathbb{R}^2} e^{-\frac{|\xi|^2}{2}|t-s|^{2/3}}d\xi = \frac{2\pi}{|t-s|^{2/3}}.$$

Step 2 — time integral. With $\alpha = Hd = 2/3$,
$$\int_0^1\!\!\int_0^1 |t-s|^{-\alpha}\,ds\,dt = \frac{2}{(1-\alpha)(2-\alpha)} = \frac{2}{(1/3)(4/3)} = \frac{9}{2}=4.5 .$$

Step 3 — combine, using $(2\pi)^{-d}\cdot(2\pi)^{d/2} = (2\pi)^{-1}$ for $d=2$:
$$\mathbb{E}\int_{\mathbb{R}^2} L(x,1)^2\,dx = (2\pi)^{-1}\cdot \frac92 \approx 0.716 < \infty .$$
Finiteness gives $L(\cdot,1)\in L^2(\mathbb{R}^2)$ almost surely; SLND (2.2) upgrades this via the moment bound $\mathbb{E}[L(x,1)^n] \le c^n (n!)^{Hd}$ to joint continuity and Hölder exponent $<1-Hd = 1/3$ in $x$.

**Now the critical case $H=1/3$, $d=3$** (so $Hd=1$). Step 2 becomes
$$\int_0^1\!\!\int_0^1 |t-s|^{-1}ds\,dt = \infty \quad (\text{logarithmically}),$$
so the $L^2$ criterion fails. The classical capacity bound (2.3) reads $\mathbb{P}\{B^H([a,b])\ni x\} \asymp \mathcal{C}_0(\{x\})=0$ only in the *upper* direction and gives no lower bound; both existence and non-existence remained consistent with all pre-2017 estimates. Dalang–Mueller–Xiao close this by a scale-by-scale covering argument: partitioning $[a,b]$ into $2^n$ intervals and using SLND to show the expected number of intervals whose image comes within $\varepsilon$ of $x$ stays bounded while the *variance* is too large for a positive-probability hit, they conclude $\mathbb{P}\{\exists t: B^H_t = x\} = 0$. Hence the occupation measure is a.s. singular and no local time exists — the boundary $Hd=1$ belongs to the "no local time" side, exactly as for planar Brownian motion ($H=\tfrac12$, $d=2$).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*