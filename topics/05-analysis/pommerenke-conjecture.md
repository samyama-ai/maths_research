---
id: 05-analysis/pommerenke-conjecture
title: "Pommerenke Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pommerenke Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/pommerenke-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture concerns the **universal integral means spectrum** of conformal maps, the function introduced and systematically studied by Christian Pommerenke.

For $f$ holomorphic and univalent (injective) on the unit disc $\mathbb{D}=\{|z|<1\}$ and $t\in\mathbb{R}$, set

$$\beta_f(t)\;=\;\limsup_{r\to 1^-}\;\frac{\log \int_0^{2\pi}\bigl|f'(re^{i\theta})\bigr|^{t}\,d\theta}{\log\frac{1}{1-r}},$$

and let $B(t)=\sup\{\beta_f(t): f \text{ univalent and bounded on }\mathbb{D}\}$.

**Conjecture.** For all real $t$,

$$B(t)\;=\;\begin{cases}\dfrac{t^{2}}{4}, & |t|\le 2,\\[2mm] |t|-1, & |t|\ge 2.\end{cases}$$

Equivalently: no bounded conformal map beats the "Gaussian/snowflake" rate $t^2/4$ in the range $|t|\le2$, while for $|t|\ge2$ the extremal behaviour is that of a boundary with an isolated inward/outward spike.

A complete solution requires either (i) a proof of the upper bound $\beta_f(t)\le t^2/4$ for every bounded univalent $f$ and every $|t|\le 2$, together with matching examples, or (ii) a single conformal map (or family) with $\beta_f(t_0)>t_0^2/4$ for some $|t_0|\le2$. Two special values carry their own names: $B(-2)=1$ is **Brennan's conjecture**, and $B(1)=\tfrac14$ is the **Carleson–Jones conjecture** on coefficients of univalent functions.

## 2. Mathematical Foundations

**Univalent classes.** $S=\{f\text{ univalent on }\mathbb{D}: f(0)=0,\,f'(0)=1\}$; $\Sigma$ is the class of univalent $g(z)=z+b_0+\sum_{n\ge1}b_nz^{-n}$ on $|z|>1$. The Koebe function $k(z)=z(1-z)^{-2}$ is extremal for many growth problems in $S$.

**Distortion and Bloch bound.** For $f\in S$, Koebe distortion gives $\frac{1-r}{(1+r)^3}\le|f'(z)|\le\frac{1+r}{(1-r)^3}$, $|z|=r$. Consequently $g=\log f'$ satisfies the Bloch estimate

$$\|g\|_{\mathcal{B}}=\sup_{z\in\mathbb{D}}(1-|z|^2)\,|g'(z)|=\sup_z (1-|z|^2)\Bigl|\frac{f''(z)}{f'(z)}\Bigr|\;\le\;6,$$

with $\le 4$ for bounded univalent $f$. So the problem is a question about the *exponential moments of a Bloch function*.

**Multifractal formalism.** $B$ is convex, $B(0)=0$, and $B$ is the Legendre-type transform of the harmonic-measure multifractal spectrum $f(\alpha)$ of the boundary. Makarov's dimension theorem — $\dim_H\omega=1$ for harmonic measure on any simply connected domain boundary — corresponds to $B'(0)=0$ and $B''(0)$ finite.

**Gaussian heuristic.** If $\log|f'(re^{i\theta})|$ behaved as a centred Gaussian field of variance $\sigma^2\log\frac{1}{1-r}$, then $\int |f'|^t\,d\theta \approx (1-r)^{-t^2\sigma^2/2}$, giving $\beta_f(t)=\tfrac{t^2\sigma^2}{2}$. The conjecture asserts the universal **asymptotic variance** of Bloch functions with $\|g\|_{\mathcal B}\le1$ is $\Sigma^2=1$, whence $t^2/4$ after normalisation.

**Related spectra.** $B_S(t)=\sup_{f\in S}\beta_f(t)$ for the (unbounded) class $S$ satisfies $B_S(t)\ge 3t-1$ from $k$, since $|k'(z)|=|1+z|/|1-z|^3$ and $\int_0^{2\pi}|1-re^{i\theta}|^{-3t}d\theta\asymp(1-r)^{1-3t}$ for $t>1/3$.

## 3. History & State of the Art

- **1965–1975.** Pommerenke studies means of $|f'|$ and coefficient growth; *Univalent Functions* (1975) formalises the integral means problem and the spectrum $\beta_f(t)$.
- **1976.** Feng and MacGregor prove Koebe is extremal in $S$ for large $t$: $B_S(t)=3t-1$ for $t\ge 2/5$, and give matching results for starlike and close-to-convex classes.
- **1978.** Brennan poses the integrability conjecture for $|\varphi'|^p$, $\varphi$ mapping a simply connected domain onto $\mathbb{D}$, for $4/3<p<4$ — the value $B(-2)=1$.
- **1985.** Makarov's distortion theorem and law of the iterated logarithm establish $\dim_H\omega=1$ and yield $B(t)=\tfrac{t^2}{4}+O(t^3)$ as $t\to0$; this is the source of the constant $1/4$.
- **1992.** Carleson and Jones link coefficients of $\Sigma$, harmonic measure and $B(1)$, and give numerical evidence for $B(1)=1/4$ (equivalently $b_n=O(n^{-3/4+\varepsilon})$).
- **1996.** Kraetzer's numerical experiments on Julia-set and snowflake maps support the full formula $B(t)=t^2/4$ on $|t|\le2$; the closed form above is often called Kraetzer's conjecture.
- **2005–2010.** Hedenmalm–Shimorin's Bergman-space/area methods give the best general upper bounds; Beliaev–Smirnov's random conformal snowflakes give the best lower bounds and are shown to compute $B$ in a limiting sense.
- **2015–2019.** Ivrii's work on Makarov's principle shows $\Sigma^2<1$ strictly for the relevant Bloch class, ruling out equality in some extremal-problem formulations (e.g. quasicircles of dimension exactly $1+k^2$).

## 4. Partial Results / Verified Cases

- **$|t|\ge 2$ (unbounded class).** For $t\ge2$ the value $|t|-1$ is known to be a lower bound; single-corner and spiral maps realise $\max(0,|t|-1)$.
- **Class $S$, $t\ge 2/5$.** $B_S(t)=3t-1$ exactly (Feng–MacGregor 1976): Koebe is extremal.
- **Small $t$.** $B(t)=\tfrac{t^2}{4}+O(|t|^3)$ (Makarov). The conjecture is thus correct to second order at $t=0$.
- **$t=1$.** Best published bounds are of the form $0.23\lesssim B(1)\le 0.46$: the lower bound from Beliaev–Smirnov random snowflakes, the upper bound from Hedenmalm–Shimorin. The conjectured value is $0.25$.
- **$t=-2$ (Brennan).** Integrability $\int_\Omega|\varphi'|^p\,dA<\infty$ is proved for $p$ in an interval strictly larger than the trivial one, currently up to about $p<3.42$ (Hedenmalm–Shimorin), against the conjectured $p<4$.
- **Special families.** Verified for starlike, close-to-convex, and spirallike functions; for lacunary-series and Julia-set examples (Kayumov, Binder); for maps onto domains bounded by piecewise-analytic curves, where $\beta_f(t)=\max(0,\lambda t-1)$ is computed exactly from corner exponents; and for $k$-quasicircles in the small-$k$ regime, where $B(t)\le \Sigma^2 k^2 t^2/4$-type bounds hold with $\Sigma^2<1$ (Ivrii).

## 5. Principal Obstacles

- **No exact model.** $\log f'$ is a Bloch function, but not a Gaussian field. The heuristic that predicts $t^2/4$ has no rigorous transfer: Bloch functions can have heavy, non-Gaussian tails on the "bad" sets that dominate high moments.
- **Extremals are fractal, not classical.** Every classical extremal candidate (Koebe, wedges, spirals) gives only $\max(0,|t|-1)$ near $t=1$, far below $t^2/4$. The true extremals are believed to be genuinely multifractal boundaries with no closed form, so variational calculus over an explicit family cannot close the gap.
- **Loss of sharp constants in area methods.** Bergman-space/Bergman-kernel arguments (Hedenmalm–Shimorin) convert the problem into a positivity question for a quadratic form; the passage from the form to $\beta_f$ dissipates constants, producing $0.46$ where $0.25$ is needed.
- **Non-compactness of the sup.** $B(t)$ is a supremum over an infinite-dimensional, non-compact family; it is not known to be attained, so one cannot argue by studying "the" extremal map.
- **Fourier analysis fails.** Boundary values of $f'$ need not be in any $L^p$ with $p>0$ uniformly, and the boundary curve may have no rectifiability; standard Littlewood–Paley or singular-integral machinery does not see the multifractal structure that governs $\beta_f$.

## 6. The Gap

Proven: the correct *order* near $t=0$ ($ct^2\le B(t)\le Ct^2$) and the correct value to second order; the exact spectrum for $S$ for $t\ge 2/5$; the conjecture for structured subclasses. Conjectured: the exact constant $1/4$ across the whole range $|t|\le 2$, and the transition point $|t|=2$.

The precise missing step is the identification of the **universal asymptotic variance**

$$\Sigma^2=\limsup_{\|g\|_{\mathcal B}\le1}\;\limsup_{r\to1^-}\frac{1}{2\pi\log\frac{1}{1-r}}\int_0^{2\pi}|g(re^{i\theta})|^2\,d\theta,$$

restricted to $g=\log f'$ with $f$ univalent. Proving $\Sigma^2$ takes exactly the value predicted by the Gaussian model, and then upgrading a second-moment statement to control of all exponential moments $\int e^{t\,\mathrm{Re}\,g}$, is the barrier. Ivrii's strict inequality $\Sigma^2<1$ for general Bloch functions shows the two normalisations do not coincide and that the univalence constraint must be used, not just the Bloch bound.

## 7. Current Research (as of June 2026)

- **Bergman-space / Hilbert-space methods.** Successors to Hedenmalm–Shimorin: sharpened positivity certificates and weighted-kernel inequalities aimed at pushing Brennan's range past $p=3.5$. Groups at KTH Stockholm and Helsinki.
- **Random conformal geometry.** Coupling the problem with SLE, Liouville quantum gravity, and Gaussian multiplicative chaos, where the analogue of $B(t)$ is exactly quadratic; the open question is whether SLE-type boundaries approach the universal supremum. Active at Geneva, Cambridge, Toronto (Beliaev, Smirnov, Ivrii and collaborators).
- **Computer-assisted lower bounds.** Optimisation over random conformal snowflakes with many parameters, giving certified lower bounds for $B(1)$; incremental improvements toward $0.25$ are reported. *(frontier — verify)*
- **Bloch-variance program.** Sharp bounds for asymptotic variance of Bloch and univalent-Bloch functions, with implications for the dimension of $k$-quasicircles, $\dim\le 1+\Sigma^2k^2$. *(frontier — verify)*
- **Dynamical models.** Integral means spectra of Julia sets and Fuchsian/Kleinian limit sets used as testbeds where thermodynamic formalism computes $\beta$ exactly.

## 8. Future Work

- Establish sharp *exponential* moment bounds for $\log f'$ from univalence, not just Bloch bounds — the missing analytic upgrade.
- Prove the conjecture at the single value $t=1$; by convexity plus Makarov's expansion this would strongly constrain the whole range.
- Show $B$ is attained, or construct a compactification of the extremal problem, permitting Euler–Lagrange analysis of an extremal boundary.
- Determine whether $B$ is real-analytic on $(-2,2)$ and whether the phase transition at $|t|=2$ is exactly first-order in the multifractal sense.
- Settle Brennan's conjecture, which is the endpoint $t=-2$ and has independent applications to the integrability of derivatives of Riemann maps and to elliptic PDE on rough domains.

## 9. Key References

- **[Foundational]** Ch. Pommerenke. *Univalent Functions.* Vandenhoeck & Ruprecht, Göttingen, 1975.
- **[Foundational]** Ch. Pommerenke. *Boundary Behaviour of Conformal Maps.* Grundlehren der mathematischen Wissenschaften 299, Springer, 1992. [DOI](https://doi.org/10.1007/978-3-662-02770-7)
- **[Foundational]** N. G. Makarov. *On the distortion of boundary sets under conformal mappings.* Proceedings of the London Mathematical Society (3) **51** (1985), 369–384. [DOI](https://doi.org/10.1112/plms/s3-51.2.369)
- **[Foundational]** J. Feng, T. H. MacGregor. *Estimates on integral means of the derivatives of univalent functions.* Journal d'Analyse Mathématique **29** (1976), 203–231. [DOI](https://doi.org/10.1007/bf02789979)
- **[Foundational]** J. E. Brennan. *The integrability of the derivative in conformal mapping.* Journal of the London Mathematical Society (2) **18** (1978), 261–272. [DOI](https://doi.org/10.1112/jlms/s2-18.2.261)
- **[SOTA / Recent]** L. Carleson, P. W. Jones. *On coefficient problems for univalent functions and conformal dimension.* Duke Mathematical Journal **66** (1992), 169–206. [DOI](https://doi.org/10.1215/s0012-7094-92-06605-1)
- **[SOTA / Recent]** P. Kraetzer. *Experimental bounds for the universal integral means spectrum of conformal maps.* Complex Variables, Theory and Application **31** (1996), 305–309. [DOI](https://doi.org/10.1080/17476939608814969)
- **[SOTA / Recent]** H. Hedenmalm, S. Shimorin. *Weighted Bergman spaces and the integral means spectrum of conformal mappings.* Duke Mathematical Journal **127** (2005), 341–393. [DOI](https://doi.org/10.1215/s0012-7094-04-12725-3)
- **[SOTA / Recent]** D. Beliaev, S. Smirnov. *Random conformal snowflakes.* Annals of Mathematics **172** (2010), 597–615. [DOI](https://doi.org/10.4007/annals.2010.172.597)
- **[SOTA / Recent]** O. Ivrii. *On Makarov's principle in conformal mapping.* International Mathematics Research Notices, 2019.
- **[Survey]** N. G. Makarov. *Fine structure of harmonic measure.* St. Petersburg Mathematical Journal **10** (1999), 217–268.
- **[Survey]** C. J. Bishop, Y. Peres. *Fractals in Probability and Analysis.* Cambridge University Press, 2017.

## 10. Worked Example / Concrete Special Case

**A single boundary corner.** Fix $0<\alpha<1$ and let $f_\alpha(z)=(1-z)^{\alpha}$, univalent and bounded on $\mathbb{D}$, mapping onto a domain whose boundary has one corner of interior opening $\alpha\pi$ at $0$. Then

$$f_\alpha'(z)=-\alpha(1-z)^{\alpha-1},\qquad |f_\alpha'(re^{i\theta})|^{t}=\alpha^{t}\,|1-re^{i\theta}|^{-t(1-\alpha)} .$$

Using $|1-re^{i\theta}|\asymp (1-r)+|\theta|$ for $|\theta|\le\pi$, with $s=t(1-\alpha)$,

$$\int_0^{2\pi}|f_\alpha'(re^{i\theta})|^{t}d\theta \;\asymp\; \int_0^{\pi}\bigl((1-r)+\theta\bigr)^{-s}\,d\theta\;\asymp\;\begin{cases}(1-r)^{1-s}, & s>1,\\ \log\frac{1}{1-r}, & s=1,\\ O(1), & s<1.\end{cases}$$

Hence

$$\beta_{f_\alpha}(t)=\max\{0,\;t(1-\alpha)-1\}.$$

Letting $\alpha\downarrow0$ (an outward slit) gives $\sup_\alpha \beta_{f_\alpha}(t)=\max\{0,t-1\}$, which is exactly the conjectured value of $B(t)$ for $t\ge2$ — the corner family is extremal there.

**Why the hard range is different.** At $t=1$ this family gives only $\beta=0$, while the conjecture asserts $B(1)=\tfrac14$. So a bounded conformal map with $\int_0^{2\pi}|f'(re^{i\theta})|\,d\theta \asymp (1-r)^{-1/4}$ (the length of the image of the circle $|z|=r$ blowing up at rate $1/4$) cannot have finitely many corners: it must have boundary distortion on *every* scale. This is what snowflake constructions supply — a self-similar boundary in which $\log|f'|$ accumulates roughly independent increments across $\log\frac{1}{1-r}$ dyadic scales, so that $\log|f'|$ is approximately Gaussian with variance proportional to $\log\frac{1}{1-r}$, and

$$\int_0^{2\pi}|f'|^{t}d\theta\;\approx\;\exp\Bigl(\tfrac{t^2}{2}\cdot\tfrac{1}{2}\log\tfrac{1}{1-r}\Bigr)=(1-r)^{-t^2/4}.$$

The best rigorous snowflakes reach about $(1-r)^{-0.23}$ at $t=1$; the best proven upper bound is about $(1-r)^{-0.46}$. Closing that interval to the single value $1/4$ is the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*