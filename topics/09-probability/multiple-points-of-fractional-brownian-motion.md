---
id: 09-probability/multiple-points-of-fractional-brownian-motion
title: "Multiple Points of Fractional Brownian Motion"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Multiple Points of Fractional Brownian Motion

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/multiple-points-of-fractional-brownian-motion` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $B^H = \{B^H(t): t \in \mathbb{R}^N_+\}$ be an $(N,d)$-fractional Brownian motion of Hurst index $H \in (0,1)$: a centered Gaussian random field with values in $\mathbb{R}^d$ whose $d$ coordinates are i.i.d. copies of a real-valued field with covariance $\tfrac12(\|s\|^{2H}+\|t\|^{2H}-\|s-t\|^{2H})$. A point $x \in \mathbb{R}^d$ is a **$k$-multiple point** if there exist distinct $t_1,\dots,t_k$ with $B^H(t_1)=\dots=B^H(t_k)=x$.

The core questions are:

1. **Existence.** For which triples $(N,d,H)$ and integers $k \ge 2$ does $B^H$ have $k$-multiple points a.s.?
2. **Critical case.** What happens on the boundary surface $dH(k-1) = kN$, where dimension counting gives no answer?
3. **Size.** What are the exact Hausdorff and packing measure functions (not just dimensions) of the multiple-point set $M_k \subset \mathbb{R}^d$ and of its time-preimage?
4. **Anisotropy.** The same questions for fields with distinct Hurst indices $(H_1,\dots,H_N)$ per time coordinate, where the natural metric is non-Euclidean.

Item (1) off the critical surface and the dimension part of (3) are settled. Items (2) for anisotropic fields, (3) in full, and (4) are open. A complete resolution must give a necessary-and-sufficient criterion covering the critical boundary and an exact gauge function.

## 2. Mathematical Foundations

**The field.** For $H\in(0,1)$, real fBm $X_H$ on $\mathbb{R}^N_+$ is the centered Gaussian field with
$$\mathbb{E}\big[X_H(s)X_H(t)\big] = \tfrac{1}{2}\left(\|s\|^{2H} + \|t\|^{2H} - \|s-t\|^{2H}\right), \qquad \mathbb{E}\big[(X_H(s)-X_H(t))^2\big] = \|s-t\|^{2H}.$$
$B^H = (X_H^1,\dots,X_H^d)$ with independent coordinates. It is self-similar, $B^H(a\,\cdot) \overset{d}{=} a^H B^H(\cdot)$, and for $N=1$ has stationary increments; for $H=1/2$, $N=1$ it is Brownian motion.

**Strong local nondeterminism (SLND).** Pitt (1978) proved that for every compact $T$ away from the origin there is $c>0$ with
$$\operatorname{Var}\big(X_H(t) \mid X_H(s_1),\dots,X_H(s_n)\big) \ \ge\ c \min_{1\le j\le n} \|t-s_j\|^{2H}.$$
SLND replaces the Markov property, which fBm lacks for $H\ne 1/2$, and is the engine behind every sharp result below.

**Dimension counting.** $\dim_H B^H([0,1]^N) = \min\{d, N/H\}$ a.s. Treating $k$ independent images as sets of codimension $d - N/H$, an intersection is nonempty when the codimensions sum to less than $d$:
$$k\left(d - \frac{N}{H}\right) < d \iff \boxed{\,dH(k-1) < kN\,} \iff H < \frac{kN}{(k-1)d}.$$
For $N=1,k=2$ this is $H < 2/d$; for $H=1/2$ it returns $k(d-2)<d$, i.e. double points iff $d\le 3$, triple points iff $d\le 2$.

**Local times and capacity.** Existence is made rigorous by second-moment arguments on the intersection local time. For independent copies $X,Y$,
$$\alpha = \int_0^1\!\!\int_0^1 \delta_0\big(X(s)-Y(t)\big)\,ds\,dt, \qquad \mathbb{E}[\alpha] = (2\pi)^{-d/2}\!\int_0^1\!\!\int_0^1 \big(s^{2H}+t^{2H}\big)^{-d/2} ds\,dt,$$
finite exactly when $dH < 2N$ (for $N=1$: $dH<2$). Nonexistence uses the Fitzsimmons–Salisbury capacity formalism for multiparameter processes: $\{x\}$ is polar for the $k$-fold field iff a Bessel–Riesz capacity of the singleton vanishes in the relevant index.

**Dimension of the multiple set.** When $dH(k-1)<kN$,
$$\dim_H M_k = \min\left\{d,\ \frac{kN}{H} - (k-1)d\right\}, \qquad \dim_H\{(t_1,\dots,t_k): B^H(t_i)\ \text{all equal}\} = kN - (k-1)dH .$$

## 3. History & State of the Art (SOTA)

- **1950–1957.** Dvoretzky, Erdős and Kakutani prove Brownian paths have double points in $d\le 3$ and none in $d\ge 4$; with Taylor (1957) they show triple points exist in the plane but not in $\mathbb{R}^3$. This fixes the $H=1/2$, $N=1$ row of the table and identifies the critical dimension $d=4$, $k=2$ as negative.
- **1968.** Mandelbrot and Van Ness introduce fBm as a stochastic-integral model, making $H$ a free parameter and turning "which $d$" into "which $(d,H)$".
- **1978–1980.** Pitt establishes SLND for fBm; Geman and Horowitz's occupation-density survey supplies the local-time machinery.
- **1985.** Kahane's *Some Random Series of Functions* collects the Gaussian-field methods (energy, capacity, Fourier) that give the sufficient half of the criterion for general $H$.
- **1987–2005.** Rosen constructs planar fBm self-intersection local time; Hu and Nualart give the sharp renormalization threshold.
- **1998.** Talagrand settles the **critical case** $dH(k-1)=kN$ for multiparameter fBm: there are no $k$-multiple points on the boundary surface. The proof uses sharp small-ball and hitting estimates rather than a Markovian argument.
- **2009–2017.** Xiao's minicourse systematizes anisotropic fields; Dalang, Khoshnevisan, Nualart, Wu and Xiao prove the critical Brownian sheet has no double points (2012); Dalang, Mueller and Xiao give general polarity-of-points criteria (2017).

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $dH(k-1) < kN$ (subcritical), all $N\ge1$, $H\in(0,1)$ | **Solved:** $k$-multiple points exist a.s.; $M_k$ has positive Lebesgue measure iff $kN/H - (k-1)d > d$. |
| $dH(k-1) > kN$ (supercritical) | **Solved:** no $k$-multiple points a.s. |
| $dH(k-1) = kN$ (critical), isotropic fBm | **Solved** (Talagrand 1998): no $k$-multiple points. |
| $N=1$, $H=1/2$ | **Solved** classically: double points iff $d\le3$, $k$-multiple iff $k(d-2)<d$. |
| $N=1$, $d=3$, $k=2$ | Double points iff $H<2/3$; $\dim_H M_2 = 4/H^{-1}$-form: $2/H-3$, e.g. $1$ at $H=1/2$. |
| $N=1$, $d=2$ | Double points for every $H\in(0,1)$ since $H<1=2N/d$ fails only at $H=1$; $M_2$ has positive area when $H<1/2$. |
| Renormalized self-intersection local time, $N=1$ | Exists in $L^2$ iff $H < 3/(2d)$ (Hu–Nualart 2005); a CLT holds at and above threshold with suitable normalization. |
| Brownian sheet, $N=2$, critical $d=8$ for $k=2$ | **Solved** (DKNWX 2012): no double points. |
| Exact Hausdorff measure of $M_k$ | Known only for $H=1/2$ and low-dimensional cases; open in general. |
| Anisotropic $(H_1,\dots,H_N)$ | Subcritical/supercritical criteria known in terms of $\sum_j 1/H_j$; **critical case open**. |

## 5. Principal Obstacles

- **No Markov property.** For $H \ne 1/2$ fBm is neither Markov nor a semimartingale. The Dvoretzky–Erdős–Kakutani proofs, and the whole potential-theoretic apparatus based on transition densities and hitting probabilities of Markov processes, do not transfer. SLND is a substitute, but only supplies two-sided estimates up to constants, which is exactly the precision lost at criticality.
- **Criticality is a $\log$-divergence.** On $dH(k-1)=kN$, the second moment of the approximating intersection local time diverges logarithmically. Both the first-moment (Borel–Cantelli) and second-moment (Paley–Zygmund) routes fail simultaneously; deciding the boundary requires a multi-scale argument with constants tracked across all scales, which is what makes Talagrand's proof hard and non-generalizable by inspection.
- **Non-Euclidean metric under anisotropy.** With distinct $H_j$ the canonical metric $\rho(s,t) = \sum_j |s_j-t_j|^{H_j}$ is not comparable to any norm; covering arguments need parallelepipeds of $N$ different aspect ratios, and the standard covering/net inequalities lose polynomial factors — again fatal at criticality.
- **Exact gauge functions need sharp limsup behavior.** Hausdorff *measure* (as opposed to dimension) is governed by the limsup fluctuations of the occupation measure of small balls, i.e. by law-of-the-iterated-logarithm-type results for the multiple-point local time. For $k \ge 2$ these are $k$-fold integrals with non-independent components, and the standard Erdős–Taylor decomposition into independent blocks fails.
- **Fourier analysis loses the constant.** The natural spectral computation gives energy integrals $\int |\xi|^{-\gamma}\,d\mu(\xi)$ whose convergence characterizes only the strict inequality; the boundary case is invisible to it.

## 6. The Gap

Proven: a full trichotomy for *isotropic* fBm in terms of the single number $dH(k-1) - kN$, plus dimension formulas for $M_k$. The general statement in Section 1 additionally demands (i) the same trichotomy when $H$ is replaced by a vector $(H_1,\dots,H_N)$, with the critical surface $\sum_j H_j^{-1} = kd/(k-1)$ decided in either direction, and (ii) exact measure functions, conjecturally of the form $\varphi(r) = r^{\dim_H M_k}(\log\log 1/r)^{\theta}$ with $\theta$ depending on $(N,d,H,k)$.

The precise step to be crossed: an anisotropic analogue of Talagrand's critical-case small-ball estimate — a bound on $\mathbb{P}\{\inf_{t\in I} \|B^H(t)-x\| \le \varepsilon\}$ that is sharp up to a constant *uniformly over rectangles $I$ of all admissible aspect ratios*, not merely over cubes. Every known proof of the isotropic critical case uses scaling invariance of the cube family, which anisotropy destroys.

## 7. Current Research (as of June 2026)

- **Anisotropic Gaussian fields (Michigan State / EPFL / Utah lineage).** The Xiao school continues to push hitting-probability and polarity criteria for fields satisfying sectorial or strong local nondeterminism, aiming at the critical surface for $(H_1,\dots,H_N)$ *(frontier — verify)*.
- **SPDE-driven fields.** Solutions of stochastic heat and wave equations behave locally like anisotropic fBm ($H=1/4$ in time, $1/2$ in space for the heat equation with space–time white noise). Multiple-point questions for these solution fields are an active transfer target of the Dalang–Khoshnevisan–Nualart program.
- **Malliavin-calculus routes to local times.** Renormalized $k$-fold self-intersection local times of fBm, their chaos expansions, and limit theorems above the $L^2$ threshold; Markowsky-type results on derivatives of intersection local time.
- **Exact measure functions.** Attempts to obtain LIL-type limsup laws for multiple-point local times, which would upgrade dimension results to exact Hausdorff/packing measures *(frontier — verify)*.

## 8. Future Work

- Prove or disprove the critical case for anisotropic fBm; a single decisive example ($N=2$, $H_1\ne H_2$) would set the direction.
- Establish exact Hausdorff and packing measure functions for $M_k$ in the subcritical regime, starting with $N=1$, $d=3$, $k=2$.
- Extend the trichotomy to fBm on non-Euclidean parameter spaces (spheres, fractals) where $\|s-t\|^{2H}$ must be replaced by a metric of negative type.
- Quantify the multifractal spectrum of the multiple-point set: dimensions of $\{x : \text{multiplicity} = k\}$ for all $k$ simultaneously, including $k=\infty$ points in the plane.
- Transfer the criterion to solutions of nonlinear SPDEs, where the Gaussian structure is only approximate.

## 9. Key References

- **[Foundational]** B. B. Mandelbrot and J. W. Van Ness. *Fractional Brownian motions, fractional noises and applications.* SIAM Review 10 (1968), 422–437.
- **[Foundational]** A. Dvoretzky, P. Erdős and S. Kakutani. *Double points of paths of Brownian motion in $n$-space.* Acta Sci. Math. (Szeged) 12 (1950), 75–81.
- **[Foundational]** A. Dvoretzky, P. Erdős, S. Kakutani and S. J. Taylor. *Triple points of Brownian paths in 3-space.* Proc. Cambridge Philos. Soc. 53 (1957), 856–862.
- **[Foundational]** L. D. Pitt. *Local times for Gaussian vector fields.* Indiana University Mathematics Journal 27 (1978), 309–330.
- **[Foundational]** D. Geman and J. Horowitz. *Occupation densities.* Annals of Probability 8 (1980), 1–67.
- **[SOTA]** M. Talagrand. *Multiple points of trajectories of multiparameter fractional Brownian motion.* Probability Theory and Related Fields 112 (1998), 545–563.
- **[SOTA]** R. C. Dalang, D. Khoshnevisan, E. Nualart, D. Wu and Y. Xiao. *Critical Brownian sheet does not have double points.* Annals of Probability 40 (2012), 1829–1859.
- **[SOTA]** R. C. Dalang, C. Mueller and Y. Xiao. *Polarity of points for Gaussian random fields.* Annals of Probability 45 (2017), 4700–4751.
- **[SOTA]** Y. Hu and D. Nualart. *Renormalized self-intersection local time for fractional Brownian motion.* Annals of Probability 33 (2005), 948–983.
- **[Related]** J. Rosen. *The intersection local time of fractional Brownian motion in the plane.* Journal of Multivariate Analysis 23 (1987), 37–46.
- **[Related]** P. J. Fitzsimmons and T. S. Salisbury. *Capacity and energy for multiparameter Markov processes.* Annales de l'IHP Probabilités et Statistiques 25 (1989), 325–350.
- **[Survey]** Y. Xiao. *Sample path properties of anisotropic Gaussian random fields.* In: A Minicourse on Stochastic Partial Differential Equations, Lecture Notes in Mathematics 1962, Springer, 2009, 145–212.
- **[Survey]** D. Khoshnevisan. *Multiparameter Processes: An Introduction to Random Fields.* Springer Monographs in Mathematics, 2002.
- **[Survey]** J.-P. Kahane. *Some Random Series of Functions*, 2nd edition. Cambridge University Press, 1985.

## 10. Worked Example / Concrete Special Case

**Setting.** $N=1$, $d=3$, $k=2$: does one-parameter fBm $B^H$ in $\mathbb{R}^3$ hit itself?

**Step 1 — the criterion.** $dH(k-1)<kN$ reads $3H < 2$, i.e. $H < 2/3$. Predicted: double points for $H<2/3$, none for $H \ge 2/3$.

**Step 2 — first moment.** Take $X, Y$ independent copies of $B^H$ (a legitimate local model for $B^H$ restricted to two disjoint time intervals, since fBm's dependence across separated intervals is bounded by SLND). Then $X(s)-Y(t)$ is centered Gaussian in $\mathbb{R}^3$ with covariance $(s^{2H}+t^{2H})I_3$, so with $\delta_0$ approximated by $p_\varepsilon$,
$$\mathbb{E}[\alpha] = (2\pi)^{-3/2}\int_0^1\!\!\int_0^1 \big(s^{2H}+t^{2H}\big)^{-3/2}\,ds\,dt .$$
Substitute $s = r u$, $t = r v$ with $r=\max(s,t)$: the integrand scales as $r^{-3H}$ and the measure as $r\,dr$, giving $\int_0^1 r^{1-3H}\,dr$, finite iff $3H<2$. At $H=1/2$ this is $\int_0^1 r^{-1/2}dr = 2 < \infty$.

**Step 3 — second moment.** Using SLND, $\operatorname{Var}(X(s_2)\mid X(s_1)) \ge c|s_2-s_1|^{2H}$, so
$$\mathbb{E}[\alpha^2] \le C \int_{[0,1]^4} \big(|s_1-s_2| \vee |t_1-t_2|\big)^{-3H}\,(s_1^{2H}+t_1^{2H})^{-3/2} \,ds\,dt < \infty \quad\text{iff } 3H<2 .$$
Paley–Zygmund then gives $\mathbb{P}\{\alpha>0\} \ge (\mathbb{E}\alpha)^2/\mathbb{E}[\alpha^2] > 0$, and a zero–one law upgrades this to a.s. existence of double points.

**Step 4 — dimension.** $\dim_H M_2 = \min\{3,\ 2/H - 3\}$. At $H=1/2$: $\dim_H M_2 = 1$, recovering the classical value for Brownian double points in $\mathbb{R}^3$. At $H=0.6$: $2/0.6-3 = 1/3$. The dimension shrinks to $0$ as $H \uparrow 2/3$.

**Step 5 — the boundary.** At $H=2/3$ exactly, $\int_0^1 r^{1-3H}dr = \int_0^1 r^{-1}dr = \infty$: logarithmic divergence, so neither moment method decides. Talagrand's critical-case theorem supplies the answer — **no** double points at $H=2/3$ — mirroring the absence of Brownian double points in $\mathbb{R}^4$ ($H=1/2$, $d=4$, where $dH(k-1)=2=kN$). Replacing the time index by $(t_1,t_2)\in\mathbb{R}^2_+$ with distinct Hurst exponents in each coordinate reproduces the same log-divergence, and there the boundary case remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*