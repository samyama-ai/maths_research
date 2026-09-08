---
id: 05-analysis/bochner-riesz-conjecture
title: "Bochner-Riesz Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bochner-Riesz Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bochner-riesz-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

For $\delta \ge 0$ define the **Bochner–Riesz multiplier operator** on $\mathbb{R}^n$ by

$$\widehat{S^{\delta} f}(\xi) \;=\; \bigl(1-|\xi|^{2}\bigr)_{+}^{\delta}\,\hat f(\xi), \qquad (t)_+ = \max(t,0).$$

Set the **critical index**

$$\delta(p) \;=\; \max\Bigl( n\Bigl|\tfrac1p-\tfrac12\Bigr| - \tfrac12,\; 0 \Bigr).$$

**Conjecture (Bochner–Riesz).** For $n \ge 2$ and $1 \le p \le \infty$, $S^{\delta}$ extends to a bounded operator on $L^{p}(\mathbb{R}^{n})$ **if and only if** $\delta > \delta(p)$ — equivalently, iff $\delta > 0$ and

$$\frac{2n}{n+1+2\delta} \;<\; p \;<\; \frac{2n}{n-1-2\delta}.$$

The "only if" direction is known (Section 4); the open content is the sufficiency for $\delta \le \frac{n-1}{2}$ in dimensions $n\ge 3$. A complete resolution must produce, for every $p$ and every $\delta>\delta(p)$, a constant $C=C(n,p,\delta)$ with $\|S^\delta f\|_{L^p}\le C\|f\|_{L^p}$; a disproof must exhibit $f \in L^p$ with $\delta > \delta(p)$ and $S^\delta f \notin L^p$.

## 2. Mathematical Foundations

**Riesz means.** For $R>0$ put $S_R^\delta f = \mathcal{F}^{-1}\bigl[(1-|\xi|^2/R^2)_+^\delta \hat f\bigr]$. By scaling, $\|S_R^\delta\|_{L^p\to L^p}=\|S^\delta\|_{L^p\to L^p}$, so uniform bounds in $R$ are equivalent to a single bound. Boundedness for $\delta>\delta(p)$ implies $S_R^\delta f \to f$ in $L^p$ as $R\to\infty$: **spherical summability** of the Fourier inversion integral.

**Kernel.** $S^\delta$ is convolution with
$$K^{\delta}(x) \;=\; \frac{\Gamma(\delta+1)}{\pi^{\delta}}\,\frac{J_{\frac n2+\delta}(2\pi|x|)}{|x|^{\frac n2+\delta}},$$
where $J_\nu$ is the Bessel function of the first kind. From $J_\nu(r)=\sqrt{2/(\pi r)}\cos\bigl(r-\tfrac{\nu\pi}{2}-\tfrac{\pi}{4}\bigr)+O(r^{-3/2})$,
$$K^{\delta}(x) \;=\; c_{n,\delta}\,\frac{\cos\bigl(2\pi|x| - \tfrac{\pi}{2}(\tfrac n2+\delta) - \tfrac\pi4\bigr)}{|x|^{\frac{n+1}{2}+\delta}} \;+\; O\bigl(|x|^{-\frac{n+3}{2}-\delta}\bigr), \qquad |x|\to\infty .$$
The decay exponent $\frac{n+1}{2}+\delta$ is the curvature gain from stationary phase on $S^{n-1}$ (nonvanishing Gaussian curvature), and it drives everything.

**Ball multiplier ($\delta=0$).** $S^0 = $ the disc multiplier $\chi_{B(0,1)}(D)$. **Fefferman (1971):** $S^0$ is unbounded on $L^p(\mathbb{R}^n)$ for every $p\ne 2$, $n\ge2$, via Besicovitch/Kakeya sets and the Y. Meyer randomization lemma.

**Related conjectures.** Write $\mathcal{E}g(x)=\int_{S^{n-1}}g(\omega)e^{2\pi i x\cdot\omega}\,d\sigma(\omega)$.
- *Restriction:* $\|\mathcal{E}g\|_{L^p(\mathbb{R}^n)}\lesssim\|g\|_{L^\infty}$ for $p>\frac{2n}{n-1}$.
- *Kakeya:* every Besicovitch set in $\mathbb{R}^n$ has Hausdorff (Minkowski) dimension $n$.

Implications: **Bochner–Riesz $\Rightarrow$ Restriction $\Rightarrow$ Kakeya** (Tao 1999; Fefferman 1970, Córdoba 1977). No converse is known in general, which is why Bochner–Riesz is the *hardest* of the three.

**Square-function formulation (Stein).** With $\Delta_j$ a dyadic decomposition of $1-|\xi|$, boundedness reduces to $L^p$ bounds for $G f=\bigl(\sum_j |S_{\Delta_j}f|^2\bigr)^{1/2}$, i.e. to a local-smoothing estimate for the wave equation after Fourier integral conjugation.

## 3. History & State of the Art (SOTA)

- **1936.** S. Bochner introduces spherical Riesz means for multiple Fourier series and proves convergence for $\delta>\frac{n-1}{2}$ (the *critical index*), where the kernel is absolutely integrable.
- **1954.** Herz determines the exact range for **radial** $f$, producing the conjectured $\delta(p)$ as the necessary threshold.
- **1970s.** Stein formulates the conjecture in its modern form and proves it in the Stein–Tomas range via $L^2$ restriction. Fefferman (1971) kills $\delta=0$. Carleson–Sjölin (1972) settle $n=2$ completely; Hörmander, Fefferman (1973) and Córdoba (1977) give alternative proofs.
- **1991.** Bourgain breaks the Stein–Tomas exponent for restriction and Kakeya, opening incremental progress in $n\ge3$.
- **2011.** Bourgain–Guth multilinear method (built on Bennett–Carbery–Tao) improves the Bochner–Riesz range in every dimension $n\ge3$.
- **2016–2019.** Guth's polynomial partitioning, extended by Guth–Hickman–Iliopoulou, pushes restriction to $p>\frac{2(3n+1)}{3n-3}$ ($n$ odd).
- **2022.** Guo–Oh–Wang–Wu–Zhang revisit Stein's square-function ("old") approach and transfer state-of-the-art restriction/decoupling input into Bochner–Riesz bounds, closing much of the historical gap between the two problems in $\mathbb{R}^3$.

## 4. Partial Results / Verified Cases

- **$n=1$:** trivial for $\delta>0$; $\delta=0$ is the Hilbert transform (M. Riesz), bounded for $1<p<\infty$.
- **$n=2$: fully proved.** Carleson–Sjölin (1972): $S^\delta$ bounded on $L^p(\mathbb{R}^2)$ for all $\delta>\delta(p)=\max(2|\tfrac1p-\tfrac12|-\tfrac12,0)$, i.e. $\frac{4}{3+2\delta}<p<\frac{4}{1-2\delta}$.
- **Necessity, all $n$:** $\delta \le \delta(p)$ fails — by the kernel computation of Section 10 for $p<\frac{2n}{n+1}$, and by Fefferman's ball-multiplier theorem plus interpolation for the full sharp range.
- **Stein–Tomas range, all $n\ge3$:** conjecture true for $p\ge\frac{2(n+1)}{n-1}$ and dually $p\le\frac{2(n+1)}{n+3}$ (Stein; Fefferman 1970). For $n=3$: $p\ge4$.
- **Above the critical index:** $\delta>\frac{n-1}{2}$ gives $K^\delta\in L^1$, so $S^\delta$ is bounded on all $L^p$, $1\le p\le\infty$ (Bochner).
- **Radial functions, all $n$:** Herz (1954) — the conjecture holds exactly as stated when $f$ is radial.
- **$L^2$-based endpoint:** $\delta=0$, $p=2$ trivially bounded; $S^\delta$ is bounded on $L^p$ for $\delta > \frac{n-1}{2}\bigl|\frac1p-\frac12\bigr|\cdot 2 - \ldots$ — quantitatively, Bourgain–Guth (2011) and Lee (2004, 2018) give explicit $\delta$-improvements below the Stein–Tomas exponent in every $n\ge3$.
- **$n=3$ (SOTA):** Guo–Oh–Wang–Wu–Zhang (2022) establish the conjecture in $\mathbb{R}^3$ for $p \ge 3+\tfrac{3}{13}\approx 3.231$, matching Hong Wang's broom-based restriction range — versus the conjectured $p>3$. *(frontier — verify the exact published exponent.)*

## 5. Principal Obstacles

- **No orthogonality at the sharp exponent.** For $p\ne2$ Plancherel is unavailable; one must control $\sim R^{(n-1)/2}$ overlapping wave packets (tubes of dimensions $R^{1/2}\times\cdots\times R^{1/2}\times R$ after rescaling the $R^{-1}$-neighbourhood of the sphere) whose interactions are exactly Kakeya-type. Any proof must implicitly solve the Kakeya conjecture, open for $n\ge4$.
- **Non-positivity of the kernel.** $K^\delta$ oscillates and is only conditionally integrable for $\delta\le\frac{n-1}{2}$; maximal-function/Calderón–Zygmund machinery, which needs positive or rapidly decaying majorants, gives nothing at the sharp index.
- **Stein–Tomas is $L^2$-based and saturated.** The $L^2$ restriction theorem is sharp for the exponent $\frac{2(n+1)}{n-1}$; extracting more requires genuinely $L^p$ information about how tubes cluster, not just $L^2$ orthogonality.
- **Multilinear-to-linear loss.** Bennett–Carbery–Tao multilinear restriction is essentially sharp, but Bourgain–Guth's descent from transverse multilinear to linear estimates loses a fixed power of $R$ that grows with $n$; the loss is not known to be removable.
- **Bochner–Riesz is strictly harder than restriction.** Tao (1999) shows BR $\Rightarrow$ restriction, but restriction estimates alone do not obviously return BR: the multiplier lives on a *neighbourhood* of the sphere with a variable-order singularity, requiring a summation over dyadic scales that costs logarithms unless a square-function bound is available.
- **Missing sharp local smoothing.** Stein's square-function conjecture, equivalent to sharp $L^p$ local smoothing for the wave equation, is proved only for $n=2$ (Guth–Wang–Zhang 2020); its $n\ge3$ analogue is open.

## 6. The Gap

The gap is the interval of exponents
$$\frac{2n}{n-1} \;<\; p \;<\; p_{\text{known}}(n),$$
where $p_{\text{known}}(n)$ is the current SOTA threshold ($p_{\text{known}}(3)\approx 3.231$ against the conjectured $3$; for large $n$, $p_{\text{known}}(n)\approx\frac{2(3n+1)}{3n-3}$ against $\frac{2n}{n-1}$ — a gap that does **not** close as $n\to\infty$). Concretely, one must prove for each $R\ge1$ and $\varepsilon>0$
$$\Bigl\| \sum_{\theta} f_\theta \Bigr\|_{L^p(\mathbb{R}^n)} \lesssim_\varepsilon R^{\varepsilon}\Bigl(\sum_\theta \|f_\theta\|_{L^p}^p\Bigr)^{1/p}, \qquad p>\tfrac{2n}{n-1},$$
for wave packets $f_\theta$ adapted to $R^{-1/2}$-caps $\theta\subset S^{n-1}$ — i.e. show that $R^{1/2}$-scale tubes pointing in $R^{(n-1)/2}$ distinct directions cannot concentrate more than the Kakeya bound permits, and do so with $L^p$ (not $L^2$) summation across dyadic annuli. The last step, dyadic summation without $\log R$ loss, is precisely Stein's square-function conjecture.

## 7. Current Research (as of June 2026)

- **Polynomial method / decoupling school** (Guth, Hickman, Iliopoulou, Zahl, Wang, R. Zhang, S. Wu, Oh, Guo — MIT, NYU, UBC, Wisconsin, Berkeley/IAS). Broom arguments and refined transversality continue to nibble at $\mathbb{R}^3$.
- **Kakeya in $\mathbb{R}^3$.** Wang–Zahl's proof of the three-dimensional Kakeya set conjecture (2025) removes the Kakeya obstruction in $n=3$ and is being tested as input to sticky/structural arguments for BR. It does **not** immediately yield BR, since BR needs the quantitative maximal-function and multi-scale forms. *(frontier — verify)*
- **Square-function revival.** The Guo–Oh–Wang–Wu–Zhang programme argues that Stein's 1970s square-function route, combined with modern decoupling, is a more efficient converter of geometric input into BR bounds than the restriction route.
- **Variable-coefficient and manifold analogues.** Bochner–Riesz for the Laplace–Beltrami operator on compact manifolds (Sogge, Seeger); known counterexamples of Bourgain and of Minicozzi–Sogge show the flat conjecture's range can fail in the variable-coefficient setting, sharpening what is special about $S^{n-1}$.
- **Maximal and a.e.-convergence forms.** The maximal Bochner–Riesz conjecture (a.e. convergence of $S_R^\delta f$) remains open even in $\mathbb{R}^2$ for $p<2$ below Tao's range.

## 8. Future Work

- Prove Stein's square-function conjecture in $\mathbb{R}^3$; by the classical reduction this gives BR *and* sharp local smoothing in three dimensions.
- Convert the Wang–Zahl Kakeya theorem into a quantitative $R^\varepsilon$ Kakeya maximal bound in $\mathbb{R}^3$, then feed it into a broad/narrow induction.
- Find a mechanism removing the fixed loss in the Bourgain–Guth multilinear-to-linear descent, which would improve all $n$ simultaneously.
- Settle the weak-type endpoint $\delta=\delta(p)$ in $\mathbb{R}^2$ (Tao, 1998, gives partial results) — a testbed for endpoint technology.
- Develop $L^p$-based (not $L^2$-based) restriction theory: Tao's proposed "bilinear-to-linear with sharp exponents" or an entirely non-inductive geometric argument.

## 9. Key References

- **[Foundational]** S. Bochner. *Summation of multiple Fourier series by spherical means.* Transactions of the American Mathematical Society, 40 (1936), 175–207. [DOI](https://doi.org/10.1090/s0002-9947-1936-1501870-1)
- **[Foundational]** C. Herz. *On the mean inversion of Fourier and Hankel transforms.* Proceedings of the National Academy of Sciences USA, 40 (1954), 996–999. [DOI](https://doi.org/10.1073/pnas.40.10.996)
- **[Foundational]** C. Fefferman. *Inequalities for strongly singular convolution operators.* Acta Mathematica, 124 (1970), 9–36. [DOI](https://doi.org/10.1007/bf02394567)
- **[Foundational]** C. Fefferman. *The multiplier problem for the ball.* Annals of Mathematics, 94 (1971), 330–336. [DOI](https://doi.org/10.2307/1970864)
- **[Foundational]** L. Carleson, P. Sjölin. *Oscillatory integrals and a multiplier problem for the disc.* Studia Mathematica, 44 (1972), 287–299. [DOI](https://doi.org/10.4064/sm-44-3-287-299)
- **[Foundational]** A. Córdoba. *The Kakeya maximal function and the spherical summation multipliers.* American Journal of Mathematics, 99 (1977), 1–22. [DOI](https://doi.org/10.2307/2374006)
- **[Foundational]** E. M. Stein. *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals.* Princeton University Press, 1993 (Chapter IX).
- **[SOTA / Recent]** J. Bourgain. *Besicovitch type maximal operators and applications to Fourier analysis.* Geometric and Functional Analysis, 1 (1991), 147–187. [DOI](https://doi.org/10.1007/bf01896376)
- **[SOTA / Recent]** T. Tao. *The Bochner–Riesz conjecture implies the restriction conjecture.* Duke Mathematical Journal, 96 (1999), 363–375. [DOI](https://doi.org/10.1215/s0012-7094-99-09610-2)
- **[SOTA / Recent]** S. Lee. *Improved bounds for Bochner–Riesz and maximal Bochner–Riesz operators.* Duke Mathematical Journal, 122 (2004), 205–232. [DOI](https://doi.org/10.1215/s0012-7094-04-12217-1)
- **[SOTA / Recent]** J. Bourgain, L. Guth. *Bounds on oscillatory integral operators based on multilinear estimates.* Geometric and Functional Analysis, 21 (2011), 1239–1295. [DOI](https://doi.org/10.1007/s00039-011-0140-9)
- **[SOTA / Recent]** L. Guth. *A restriction estimate using polynomial partitioning.* Journal of the American Mathematical Society, 29 (2016), 371–413. [DOI](https://doi.org/10.1090/jams827)
- **[SOTA / Recent]** L. Guth, J. Hickman, M. Iliopoulou. *Sharp estimates for oscillatory integral operators via polynomial partitioning.* Acta Mathematica, 223 (2019), 251–376. [DOI](https://doi.org/10.4310/acta.2019.v223.n2.a2)
- **[SOTA / Recent]** L. Guth, H. Wang, R. Zhang. *A sharp square function estimate for the cone in $\mathbb{R}^3$.* Annals of Mathematics, 192 (2020), 551–581. [DOI](https://doi.org/10.4007/annals.2020.192.2.6)
- **[SOTA / Recent]** H. Wang. *A restriction estimate in $\mathbb{R}^3$ using brooms.* Duke Mathematical Journal, 171 (2022), 1749–1822.
- **[SOTA / Recent]** S. Guo, C. Oh, H. Wang, S. Wu, R. Zhang. *The Bochner–Riesz problem: an old approach revisited.* Peking Mathematical Journal, 2022.
- **[Survey]** T. Tao. *Recent progress on the restriction conjecture.* In *Fourier Analysis and Convexity*, Birkhäuser, 2004. [DOI](https://doi.org/10.1007/978-0-8176-8172-2_10)
- **[Survey]** C. D. Sogge. *Fourier Integrals in Classical Analysis.* 2nd ed., Cambridge University Press, 2017.

## 10. Worked Example / Concrete Special Case

**Claim.** $S^\delta$ bounded on $L^p(\mathbb{R}^n)$ forces $K^\delta \in L^p(\mathbb{R}^n)$ for $p \le 2$, hence $\delta > \delta(p)$ for $p<\frac{2n}{n+1}$. This is the necessity half, done by hand.

*Step 1 — reduce to the kernel.* Let $\varphi$ be a smooth bump with $\hat\varphi = 1$ on $B(0,2)$, supported in $B(0,4)$. Then $S^\delta\varphi = K^\delta * \varphi$, and since $\widehat{S^\delta \varphi}=(1-|\xi|^2)_+^\delta = \widehat{K^\delta}$, we get $S^\delta\varphi = K^\delta$ exactly. If $\|S^\delta\|_{L^p\to L^p}=C<\infty$ then $\|K^\delta\|_{L^p} \le C\|\varphi\|_{L^p} < \infty$.

*Step 2 — integrability of the kernel.* From Section 2,
$$|K^\delta(x)| \asymp |x|^{-\frac{n+1}{2}-\delta}\bigl|\cos(2\pi|x| - \theta_{n,\delta})\bigr|, \qquad |x| \ge 1 .$$
The cosine is $\ge \tfrac12$ on a fixed proportion of each unit annulus, so
$$\int_{|x|\ge1}|K^\delta|^p \asymp \int_1^\infty r^{-p(\frac{n+1}{2}+\delta)}\,r^{n-1}\,dr,$$
which converges **iff** $p\bigl(\tfrac{n+1}{2}+\delta\bigr) > n$, i.e.
$$\delta \;>\; \frac{n}{p} - \frac{n+1}{2} \;=\; n\Bigl(\frac1p-\frac12\Bigr)-\frac12 \;=\; \delta(p).$$

*Step 3 — a number.* Take $n=3$, $p=1$. Then $\delta(1) = 3(1-\tfrac12)-\tfrac12 = 1 = \tfrac{n-1}{2}$. The kernel decays like $|x|^{-2-\delta}$; against the volume growth $r^{2}\,dr$ it is integrable iff $2+\delta>3$, i.e. $\delta>1$. So $S^{1}$ is **not** bounded on $L^1(\mathbb{R}^3)$, while $S^{\delta}$ is for every $\delta>1$ — the critical-index endpoint fails, matching Bochner's 1936 threshold.

*Step 4 — where the difficulty lies.* This argument is one-sided. It gives necessity, and for $p>2$ duality plus Fefferman's ball-multiplier theorem gives the rest of the necessity. The **sufficiency** for, say, $n=3$ and $3<p<3.23$ cannot be obtained from kernel size alone: at those exponents the kernel is in $L^p$ but the operator's boundedness depends on cancellation among $\sim R$ wave packets, which is exactly the Kakeya-type geometry that no current technique controls.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*