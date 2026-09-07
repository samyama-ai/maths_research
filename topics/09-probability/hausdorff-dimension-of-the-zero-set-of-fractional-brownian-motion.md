---
id: 09-probability/hausdorff-dimension-of-the-zero-set-of-fractional-brownian-motion
title: "Hausdorff Dimension of the Zero Set of Fractional Brownian Motion"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hausdorff Dimension of the Zero Set of Fractional Brownian Motion

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/hausdorff-dimension-of-the-zero-set-of-fractional-brownian-motion` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $B^H = \{B^H(t) : t \in \mathbb{R}^N\}$ be an $(N,d)$-fractional Brownian field: $d$ independent copies of a centred real Gaussian field with Hurst index $H \in (0,1)$. The **zero set** (level set at $0$) is
$$
Z = (B^H)^{-1}(0) = \{ t \in \mathbb{R}^N : B^H(t) = 0 \}.
$$

The core claim, now established, is:

> **Theorem (dimension of the zero set).** If $N > Hd$, then almost surely on the event $\{Z \cap (0,\infty)^N \neq \emptyset\}$,
> $$\dim_{\mathrm H} Z = \dim_{\mathrm P} Z = N - Hd .$$
> If $N \le Hd$, then $Z \cap (0,\infty)^N = \emptyset$ a.s. (points are polar), including the **critical case** $N = Hd$.

For $N=d=1$ this reads $\dim_{\mathrm H}\{t>0 : B^H(t)=0\} = 1-H$, recovering $1/2$ for standard Brownian motion.

What remains open — the live content of this entry — is the *refinement* layer: the exact Hausdorff and packing **measure** (gauge function) of $Z$ for $H \ne 1/2$; **uniform** (simultaneous-in-level, simultaneous-in-subset) dimension results; and the corresponding statements for anisotropic, multifractional, and SPDE-driven relatives where the isotropic scaling argument breaks. A complete resolution of the refinement layer means: exhibit $\varphi$ with $0 < \varphi\text{-}m(Z) < \infty$ a.s., and prove the sharp constant-order two-sided bounds.

## 2. Mathematical Foundations

**Fractional Brownian motion.** $B^H_0$ is the real centred Gaussian field on $\mathbb{R}^N$ with $B^H_0(0)=0$ and
$$
\mathbb{E}\big[B^H_0(s)B^H_0(t)\big] = \tfrac12\big(\|s\|^{2H} + \|t\|^{2H} - \|s-t\|^{2H}\big),
\qquad H\in(0,1).
$$
Hence $\mathbb{E}[(B^H_0(s)-B^H_0(t))^2] = \|s-t\|^{2H}$: the field is **isotropic**, has stationary increments, and is self-similar of index $H$, i.e. $B^H_0(c\,\cdot) \stackrel{d}{=} c^H B^H_0(\cdot)$. The vector field is $B^H = (B^H_1,\dots,B^H_d)$ with i.i.d. coordinates. For $N=1$, Mandelbrot–Van Ness give the moving-average representation
$$
B^H_0(t) = \frac{1}{\Gamma(H+\tfrac12)}\int_{\mathbb{R}} \Big[(t-u)_+^{H-1/2} - (-u)_+^{H-1/2}\Big]\,dW(u).
$$

**Hausdorff measure and dimension.** For a gauge $\varphi:(0,\delta)\to(0,\infty)$ increasing with $\varphi(0+)=0$,
$$
\varphi\text{-}m(E) = \lim_{\varepsilon\downarrow0}\ \inf\Big\{\textstyle\sum_i \varphi(2r_i) : E \subset \bigcup_i B(x_i,r_i),\ r_i<\varepsilon\Big\},
$$
and $\dim_{\mathrm H} E = \inf\{\alpha : \ \alpha\text{-}m(E)=0\}$ with $\varphi(r)=r^\alpha$.

**Frostman's lemma / energy method.** If a Borel probability measure $\mu$ on $E$ satisfies $\mathcal{E}_\alpha(\mu)=\iint \|s-t\|^{-\alpha}\,d\mu(s)\,d\mu(t)<\infty$, then $\dim_{\mathrm H} E \ge \alpha$.

**Local nondeterminism (LND).** Berman's local $\phi$-nondeterminism, in the strong form of Pitt: there is $c>0$ such that for all $t,t^1,\dots,t^n$,
$$
\operatorname{Var}\big(B^H_0(t)\ \big|\ B^H_0(t^1),\dots,B^H_0(t^n)\big) \ \ge\ c\ \min_{1\le j\le n}\|t-t^j\|^{2H}.
$$
Pitt (1978) proved this for fBm on $\mathbb{R}^N$ for every $H\in(0,1)$. LND is the engine: it replaces the Markov property, which fBm lacks for $H\ne 1/2$.

**Local times.** When $N > Hd$, $B^H$ has a local time $L(x,T)$ satisfying the occupation-density formula
$$
\int_T f(B^H(t))\,dt = \int_{\mathbb{R}^d} f(x)\,L(x,T)\,dx \qquad \text{for all Borel } f\ge0,
$$
jointly continuous in $(x,T)$, and $x \mapsto L(x,\cdot)$ is a measure carried by the level set $(B^H)^{-1}(x)$. LND yields the Hölder regularity of $T\mapsto L(0,T)$, which supplies exactly the Frostman measure needed for the lower bound.

**Hitting probabilities.** For a compact $F \subset \mathbb{R}^d$, LND plus Gaussian small-ball estimates give the capacity/Hausdorff-measure sandwich
$$
c_1\,\mathcal{H}_{d - N/H}(F) \ \le\ \mathbb{P}\big\{B^H(T) \cap F \neq \emptyset\big\} \ \le\ c_2\,\mathcal{C}_{d - N/H}(F),
$$
with $\mathcal{C}_\beta$ the Bessel–Riesz capacity; polarity of points is the case $F=\{0\}$, $d \ge N/H$.

## 3. History & State of the Art (SOTA)

- **1930s–1960s.** Lévy computed the Brownian zero set: for $N=d=1$, $H=1/2$, it is a closed set of Lebesgue measure zero, perfect, of dimension $1/2$. Taylor and Wendel (1966) obtained the *exact* Hausdorff measure of the zero set of a stable process, giving for Brownian motion the gauge $\varphi(r)=r^{1/2}(\log\log 1/r)^{1/2}$, with $\varphi\text{-}m(Z)$ a constant multiple of the local time.
- **1968.** Mandelbrot and Van Ness formalise fBm and its self-similarity, opening the $H\ne1/2$ regime where no Markov or martingale structure survives.
- **1973–1978.** Berman introduces local nondeterminism for local times; Pitt extends it to Gaussian vector fields and proves joint continuity of the local times of $(N,d)$-fBm when $N > Hd$.
- **1985.** Kahane, *Some Random Series of Functions* (Ch. 18), gives the dimension formula $\dim_{\mathrm H}(B^H)^{-1}(x) = N-Hd$ for $N>Hd$ and establishes the image/graph dimensions $\min(d, N/H)$ and $\min(N/H, N+(1-H)d)$.
- **1987.** Monrad and Pitt prove uniform dimension results for images of fBm via LND.
- **1995–1998.** Talagrand supplies the sharp small-ball/LND technology: exact Hausdorff measure of the trajectories (1995), and polarity of points in the critical case $N=Hd$ together with multiple-point results (1998). This closes the last gap in the dichotomy stated in §1.
- **1996–2009.** Xiao develops packing measure and packing dimension for fBm paths, exact-measure results for graphs, and — with Ayache and Wu — the anisotropic theory (fractional Brownian sheets) where the dimension of a level set becomes a sum over coordinate Hurst indices rather than a single scaling exponent.

The dimension question is therefore **solved**; the SOTA frontier is the exact gauge and its uniformity.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $N=d=1$, $H=1/2$ | $\dim_{\mathrm H} Z=1/2$; exact gauge $r^{1/2}(\log\log 1/r)^{1/2}$, $\varphi\text{-}m(Z) = c\,L(0,\cdot)$ | Taylor–Wendel 1966 |
| $N=d=1$, any $H$ | $\dim_{\mathrm H} Z = \dim_{\mathrm P} Z = 1-H$ | Kahane 1985 |
| $N > Hd$, any $N,d,H$ | $\dim_{\mathrm H}(B^H)^{-1}(x) = N-Hd$ a.s. for fixed $x$; jointly continuous local times | Pitt 1978; Kahane 1985 |
| $N < Hd$ | $Z\cap(0,\infty)^N=\emptyset$ a.s. (points polar) | Kahane 1985 |
| $N = Hd$ (critical) | points polar; $Z$ empty | Talagrand 1998 |
| Hitting of general targets | capacity/measure sandwich with index $d-N/H$ | Xiao 2009 survey |
| Anisotropic sheets $\prod$-type covariance, $H=(H_1,\dots,H_N)$ | $\dim_{\mathrm H} Z = \min_{1\le k\le N}\big\{\sum_{j=1}^{N} H_k/H_j - H_k d\big\}$ on the non-polar range | Ayache–Xiao 2005; Wu–Xiao 2007 |
| Graph, $N=d=1$ | $\dim_{\mathrm H}\mathrm{Gr}(B^H)=2-H$, with exact gauge known | Xiao 1997 |

Also verified: $\dim_{\mathrm P} Z = \dim_{\mathrm H} Z$ for isotropic fBm (no dimension gap), and $Z$ is a.s. a perfect, Lebesgue-null, uncountable closed set when $N=d=1$.

## 5. Principal Obstacles

- **No Markov property, no martingales.** For $H \ne 1/2$ increments are correlated at all lags, so excursion theory, Itô's decomposition, Tanaka's formula and the Ray–Knight theorems — all of which give the Brownian zero set for free — are unavailable. LND is a quantitative substitute but yields constants, not identities: it produces bounds $c_1 \le \liminf \le \limsup \le c_2$ where the exact-measure problem needs a limit.
- **Second-moment estimates degrade at the gauge scale.** Dimension is a first-moment/second-moment competition and is robust to constants. An exact Hausdorff measure requires the sharp $\log\log$ correction, i.e. a law of the iterated logarithm for the local time $L(0,\cdot)$ that is *uniform over all small intervals*. LND gives the required upper LIL, but the matching lower bound needs near-independence of the field over a sparse family of scales, and the long-range dependence of fBm for $H>1/2$ obstructs the standard Borel–Cantelli decoupling.
- **Uniformity in the level.** Fixed-$x$ statements hold for every $x$ a.s. with an exceptional null set depending on $x$; upgrading to "a.s., for all $x$ simultaneously" requires control of $\sup_x$ over an uncountable family, and the natural entropy bound loses exactly the factor needed at the critical exponent.
- **Anisotropy destroys single-index scaling.** For fractional Brownian sheets the field is not self-similar under a single dilation; the covering argument must run in a metric $\rho(s,t)=\sum_j|s_j-t_j|^{H_j}$, in which balls are boxes with $N$ distinct aspect ratios, and standard density theorems for Hausdorff measure fail.
- **Critical-case fragility.** At $N=Hd$ polarity is proved but the argument (Talagrand's sharp small-ball estimate) is tight; the analogous critical statements for non-Gaussian or non-LND fields have no known route.

## 6. The Gap

Proven: the value $N-Hd$ and the polar/non-polar dichotomy, for all $H\in(0,1)$, $N,d\ge1$, isotropic case.

Not proven, for $H \ne 1/2$ and $N=d=1$: that
$$
\varphi(r) = r^{1-H}\,(\log\log 1/r)^{H}
$$
is the exact gauge, i.e. $0 < \varphi\text{-}m(Z) < \infty$ a.s. with $\varphi\text{-}m(Z)$ proportional to the local time $L(0,\cdot)$. The exponent $H$ on the iterated logarithm is the value forced by Taylor–Wendel at $H=1/2$ and by the LIL for the local time; two-sided bounds of the correct *form* follow from LND, but the identification of the limit does not. *(frontier — verify)*

The precise missing step: a **uniform lower LIL** for the local time,
$$
\liminf_{r\downarrow0}\ \sup_{t\in Z\cap I}\ \frac{L(0,[t,t+r])}{r^{1-H}(\log\log 1/r)^{H}} \ \in (0,\infty)\quad\text{a.s.},
$$
which requires decoupling the fBm field across a geometric sequence of scales without the independent-increments property.

## 7. Current Research (as of June 2026)

- **Michigan State (Xiao and collaborators)** continue the anisotropic-field programme: exact measure functions for level sets of fractional Brownian sheets and of solutions to systems of linear SPDEs, using sectorial LND. Recent effort targets packing measure of level sets, where even the correct gauge form is unsettled. *(frontier — verify)*
- **SPDE level sets.** The zero set of the solution to the stochastic heat equation with additive space-time white noise behaves locally like fBm with $H=1/4$ in time and $H=1/2$ in space; groups at EPFL, Utah and Wisconsin study the resulting anisotropic zero set, whose dimension is predicted by the $\rho$-metric formula. *(frontier — verify)*
- **Multifractional and variable-index fields.** When $H=H(t)$ varies, the zero set has a *multifractal* dimension spectrum: $\dim_{\mathrm H}(Z\cap I) = 1-\sup_{t\in I}H(t)$ is expected, with the localisation argument sensitive to the regularity of $H(\cdot)$.
- **Rough-path / Malliavin routes.** Malliavin-calculus density bounds for $B^H(t)$ conditioned on finitely many values are being used to re-derive LND with explicit constants, in the hope of tracking constants all the way to the gauge.

## 8. Future Work

- Transfer Talagrand's sharp small-ball estimate for fBm into a *uniform-over-scales* form; this is the identified bottleneck for the exact gauge.
- Prove or refute uniform Hausdorff dimension for level sets: a.s. simultaneously for all $x$ in the range, $\dim_{\mathrm H}(B^H)^{-1}(x) = N-Hd$, in the spirit of Monrad–Pitt's uniform result for images.
- Settle the exact **packing** measure gauge of $Z$; for Brownian motion the packing gauge involves $(\log|\log r|)^{-1}$ rather than a power, and no fBm analogue is known.
- Extend the polarity dichotomy to fields with only *sectorial* LND, where the critical case is entirely open.
- Develop excursion theory for fBm at the level of the zero set — e.g. a $\sigma$-finite excursion measure whose existence would immediately give the exact gauge, as it does for $H=1/2$.

## 9. Key References

- **[Foundational]** Mandelbrot, B. B. and Van Ness, J. W. *Fractional Brownian motions, fractional noises and applications.* SIAM Review 10 (1968), 422–437.
- **[Foundational]** Taylor, S. J. and Wendel, J. G. *The exact Hausdorff measure of the zero set of a stable process.* Z. Wahrscheinlichkeitstheorie verw. Gebiete 6 (1966), 170–180.
- **[Foundational]** Berman, S. M. *Local nondeterminism and local times of Gaussian processes.* Indiana University Mathematics Journal 23 (1973), 69–94.
- **[Foundational]** Pitt, L. D. *Local times for Gaussian vector fields.* Indiana University Mathematics Journal 27 (1978), 309–330.
- **[Foundational]** Kahane, J.-P. *Some Random Series of Functions*, 2nd ed. Cambridge University Press, 1985 (Chapter 18).
- **[Foundational]** Adler, R. J. *The Geometry of Random Fields.* Wiley, 1981.
- **[SOTA]** Talagrand, M. *Hausdorff measure of trajectories of multiparameter fractional Brownian motion.* Annals of Probability 23 (1995), 767–775.
- **[SOTA]** Talagrand, M. *Multiple points of trajectories of multiparameter fractional Brownian motion.* Probability Theory and Related Fields 112 (1998), 545–563.
- **[SOTA]** Xiao, Y. *Hausdorff measure of the graph of fractional Brownian motion.* Mathematical Proceedings of the Cambridge Philosophical Society 122 (1997), 565–576.
- **[SOTA]** Xiao, Y. *Packing measure of the sample paths of fractional Brownian motion.* Transactions of the American Mathematical Society 348 (1996), 3193–3213.
- **[SOTA]** Ayache, A. and Xiao, Y. *Asymptotic properties and Hausdorff dimensions of fractional Brownian sheets.* Journal of Fourier Analysis and Applications 11 (2005), 407–439.
- **[SOTA]** Monrad, D. and Pitt, L. D. *Local nondeterminism and Hausdorff dimension.* In: Seminar on Stochastic Processes 1986, Progress in Probability 13, Birkhäuser, 1987, 163–189.
- **[Survey]** Xiao, Y. *Sample path properties of anisotropic Gaussian random fields.* In: A Minicourse on Stochastic Partial Differential Equations, Lecture Notes in Mathematics 1962, Springer, 2009, 145–212.
- **[Survey]** Khoshnevisan, D. *Multiparameter Processes: An Introduction to Random Fields.* Springer, 2002.
- **[Survey]** Falconer, K. *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. Wiley, 2014.

## 10. Worked Example / Concrete Special Case

Take $N=d=1$, $H=1/4$, and $Z = \{t\in[1,2] : B^{1/4}(t)=0\}$. Claim: $\dim_{\mathrm H} Z = 1-H = 3/4$ a.s. on $\{Z\neq\emptyset\}$.

**Upper bound (first moment / box counting).** Partition $[1,2]$ into $n=\delta^{-1}$ intervals $I_j$ of length $\delta$. Over $I_j$ the field has modulus of continuity $\delta^{H}=\delta^{1/4}$, and $B^{1/4}(t_j)$ is Gaussian with variance in $[1,2]$. So
$$
\mathbb{P}\{Z\cap I_j\neq\emptyset\}\ \asymp\ \mathbb{P}\{|B^{1/4}(t_j)| \le c\,\delta^{H}\}\ \asymp\ \delta^{H}=\delta^{1/4}.
$$
Let $M_\delta$ count the intervals meeting $Z$. Then
$$
\mathbb{E}[M_\delta]\ \asymp\ \delta^{-1}\cdot\delta^{1/4}=\delta^{-3/4}.
$$
For $\alpha>3/4$, $\mathbb{E}\big[\sum_j \delta^{\alpha}\mathbf 1\{Z\cap I_j\ne\emptyset\}\big]\asymp \delta^{\alpha-3/4}\to0$, so $\alpha\text{-}m(Z)=0$ a.s. and $\dim_{\mathrm H}Z\le 3/4$. (This also gives upper box dimension $3/4$.)

**Lower bound (local time as Frostman measure).** Since $N=1>Hd=1/4$, the local time $L(0,\cdot)$ exists, is jointly continuous, and is a nonzero measure $\mu$ carried by $Z$ with positive probability. LND gives the moment bound, for every $\gamma<1-H=3/4$ and small $r$,
$$
\mathbb{E}\big[L(0,[t,t+r])\big] \ \asymp\ r^{1-H}=r^{3/4},
\qquad
\mathbb{E}\big[L(0,[t,t+r])^k\big] \ \le\ C^k (k!)^{H} r^{k(1-H)} .
$$
Hence $\mu([t,t+r]) \le C_\omega\, r^{\gamma}$ uniformly, and the energy
$$
\mathcal{E}_\gamma(\mu)=\iint_{Z\times Z}|s-t|^{-\gamma}\,d\mu(s)\,d\mu(t)
= \int_Z\!\Big(\gamma\!\int_0^\infty \!u^{\gamma-1}\mu\big(B(t,u^{-1})\big)\,du\Big)d\mu(t)
$$
converges whenever $\gamma < 3/4$, because $\mu(B(t,r))\lesssim r^{\gamma'}$ with $\gamma<\gamma'<3/4$. Frostman's lemma then gives $\dim_{\mathrm H}Z\ge \gamma$ for every $\gamma<3/4$, so $\dim_{\mathrm H}Z\ge3/4$.

**Conclusion and where it stops.** $\dim_{\mathrm H}Z=3/4$. But the argument only shows
$$
0 < \liminf_{r\to0}\frac{L(0,[t,t+r])}{r^{3/4}(\log\log 1/r)^{1/4}} \quad\text{and}\quad \limsup < \infty
$$
with unmatched constants; it does not identify $\varphi\text{-}m(Z)$ for $\varphi(r)=r^{3/4}(\log\log 1/r)^{1/4}$. That identification — routine at $H=1/2$ via excursion theory — is precisely the open refinement of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*