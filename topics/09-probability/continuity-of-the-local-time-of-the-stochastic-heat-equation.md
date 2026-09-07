---
id: 09-probability/continuity-of-the-local-time-of-the-stochastic-heat-equation
title: "Continuity of the Local Time of the Stochastic Heat Equation"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Continuity of the Local Time of the Stochastic Heat Equation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/continuity-of-the-local-time-of-the-stochastic-heat-equation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $u=(u_1,\dots,u_d)$ solve the system of stochastic heat equations on $\mathbb{R}_+\times\mathbb{R}$,
$$\partial_t u_i(t,x)=\partial_x^2 u_i(t,x)+\sum_{j=1}^d \sigma_{ij}\big(u(t,x)\big)\,\dot W_j(t,x),\qquad u(0,\cdot)\equiv 0,$$
with $\dot W_1,\dots,\dot W_d$ independent space–time white noises and $\sigma:\mathbb{R}^d\to\mathbb{R}^{d\times d}$ Lipschitz, bounded, and uniformly elliptic ($\inf_z \det\sigma(z)\sigma(z)^{\!\top}>0$).

Define the space–time occupation measure of a rectangle $Q=[t_1,t_2]\times[x_1,x_2]$ by $\mu_Q(A)=\mathrm{Leb}\{(t,x)\in Q:\ u(t,x)\in A\}$, $A\in\mathcal{B}(\mathbb{R}^d)$. The **local time** is the density $L(y,Q)=\frac{d\mu_Q}{dy}(y)$, when it exists.

**Conjecture.** For every such $\sigma$:

1. $\mu_Q\ll \mathrm{Leb}_{\mathbb{R}^d}$ a.s. for all $Q$ if and only if $d\le 5$;
2. for $d\le 5$ there is a version of $(y,Q)\mapsto L(y,Q)$ that is jointly continuous in $y$ and in the endpoints of $Q$;
3. this version is a.s. Hölder continuous in $y$ of every order $\gamma<\tfrac12\big(1-\tfrac{d}{6}\big)$, and this exponent is sharp.

A complete solution proves or disproves all three, uniformly over the stated class of $\sigma$ (not merely for $\sigma\equiv\text{const}$), and settles the critical dimension $d=6$.

## 2. Mathematical Foundations

**Mild solution.** With $p_r(x)=(4\pi r)^{-1/2}e^{-x^2/4r}$, the Walsh solution is
$$u_i(t,x)=\sum_j\int_0^t\!\!\int_{\mathbb{R}} p_{t-s}(x-z)\,\sigma_{ij}(u(s,z))\,W_j(ds\,dz),$$
which exists, is unique, and satisfies $\sup_{Q}\mathbb{E}|u(t,x)|^p<\infty$ for all $p$ (Walsh, 1986). Its Hölder indices are $H_1=\tfrac14$ in $t$ and $H_2=\tfrac12$ in $x$; the natural metric is parabolic,
$$\Delta\big((t,x),(t',x')\big)=|t-t'|^{1/4}+|x-x'|^{1/2},$$
and $(\mathbb{R}_+\times\mathbb{R},\Delta)$ has "index" $Q^\ast=\sum_j H_j^{-1}=4+2=6$.

**Berman's criterion.** For a random field $v$ on a parameter set $T\subset\mathbb{R}^N$, $L(\cdot,T)\in L^2(dy)$ a.s. as soon as
$$\int_T\!\!\int_T \mathbb{E}\Big[\big|\det \mathrm{Cov}\big(v(s),v(t)\big)\big|^{-1/2}\Big]\,ds\,dt<\infty$$
in the Gaussian case (Berman 1969; Geman–Horowitz 1980). Joint continuity follows from moment bounds
$$\mathbb{E}\big[|L(y,Q)-L(y',Q)|^{n}\big]\le C_n\,|y-y'|^{n\gamma}$$
plus Kolmogorov's continuity theorem, and these require $n$-point density bounds
$$p_{u(t_1,x_1),\dots,u(t_n,x_n)}(y_1,\dots,y_n)\le C\prod_{k=1}^n \Delta\big(z_k,\{z_1,\dots,z_{k-1}\}\big)^{-d}. \tag{$\star$}$$

**Strong local nondeterminism (LND).** The field is strongly LND on $Q$ if there is $c>0$ with
$$\mathrm{Var}\big(u_1(z)\mid u_1(z^1),\dots,u_1(z^n)\big)\ \ge\ c\,\min_{1\le k\le n}\Delta(z,z^k)^2 .$$
For $\sigma\equiv I$ (additive noise) the coordinates are independent centred Gaussian fields with
$$\mathbb{E}\big[(u_1(t,x)-u_1(t',x'))^2\big]\asymp |t-t'|^{1/2}+|x-x'| ,$$
strong LND holds, and $(\star)$ is a Gaussian computation. For general $\sigma$, $u$ is not Gaussian; $(\star)$ must come from Malliavin calculus — Bally–Pardoux (1998) gives smooth densities, Chen–Hu–Nualart (2021) gives strict positivity and Gaussian-type upper bounds for $d=1$.

## 3. History & State of the Art (SOTA)

- **1969–1980.** Berman's Fourier-analytic criterion and the Geman–Horowitz survey establish the template: LND $\Rightarrow$ existence $\Rightarrow$ joint continuity $\Rightarrow$ Hölder exponent.
- **1978.** Pitt proves LND for Gaussian vector fields and points out $d<Q^\ast$ as the existence threshold.
- **1986.** Walsh's Saint-Flour notes construct the solution field and its Hölder regularity, making the parabolic metric $\Delta$ available.
- **2002.** Mueller–Tribe study hitting properties of the random string (SHE with additive noise), identifying $d=6$ as the critical dimension for point-hitting.
- **2007.** Dalang–Khoshnevisan–Nualart (ALEA) settle hitting probabilities for **additive** noise systems: points are polar iff $d\ge6$, with Bessel–Riesz capacity/Hausdorff-measure two-sided bounds.
- **2009.** Dalang–Khoshnevisan–Nualart (PTRF) extend to **multiplicative** noise via Malliavin calculus: non-polarity for $d<6$, polarity for $d>6$, $d=6$ left open.
- **2009.** Hu–Nualart use Brownian local time inside a Feynman–Kac representation for SHE driven by fractional noise with $H<1/2$ — the first place local time enters SHE theory structurally.
- **2011–2017.** Xiao's LND machinery for anisotropic Gaussian fields; Dalang–Mueller–Xiao (2017) sharpen polarity of points for Gaussian random fields with parabolic scaling.

**SOTA summary:** the Gaussian ($\sigma$ constant) case is essentially complete; the nonlinear case has hitting-probability analogues but no continuity theorem for $L$ beyond $d=1$-type arguments.

## 4. Partial Results / Verified Cases

- **Additive noise, all $d\le5$.** $u$ is Gaussian, strongly LND w.r.t. $\Delta$; Berman's criterion gives $L(\cdot,Q)\in L^2(dy)$, and $(\star)$ yields a jointly continuous version with Hölder exponent $\gamma<\frac12(1-d/6)$ in $y$. For $d\ge6$ the occupation measure is a.s. singular and no local time exists.
- **Fixed time slice, $d=1$.** For any $t>0$, $x\mapsto u(t,x)$ is a Gaussian process with $\mathbb{E}[(u(t,x)-u(t,x'))^2]\asymp|x-x'|$; the spatial local time exists, is jointly continuous, and is Hölder$(\gamma)$ for all $\gamma<1/2$ — a Ray–Knight-type regularity matching Brownian motion.
- **Nonlinear $\sigma$, $d=1$.** Bally–Pardoux (1998) smoothness plus the two-sided density bounds of Chen–Hu–Nualart (2021) give existence and joint continuity of the space–time local time; the Hölder exponent obtained is not proved sharp.
- **Nonlinear $\sigma$, hitting-probability surrogate, $d\ne6$.** Dalang–Khoshnevisan–Nualart (2009): $\mathbb{P}\{u(Q)\cap\{y\}\ne\emptyset\}>0$ for $d<6$, $=0$ for $d>6$. Positivity of hitting is weaker than absolute continuity of $\mu_Q$, but it fixes the same critical dimension.
- **Colored noise in spatial dimension $k\ge2$.** For noise with Riesz covariance $|x|^{-\beta}$, $0<\beta<2\wedge k$, the additive-noise field has indices $H_1=\frac{2-\beta}{4}$, $H_2=\frac{2-\beta}{2}$ and $Q^\ast=\frac{4}{2-\beta}+\frac{2k}{2-\beta}$; the Gaussian theory transfers verbatim, giving existence and continuity for $d<Q^\ast$.

## 5. Principal Obstacles

- **Loss of Gaussianity.** Berman's method runs on characteristic functions $\mathbb{E}\exp(i\sum\xi_k\cdot u(z_k))$, which factor explicitly only for Gaussian fields. For $\sigma$ non-constant no closed form exists, and the $n$-fold Fourier integrals cannot be bounded term by term.
- **No LND substitute.** Strong LND is a statement about conditional variances of a Gaussian field. The Malliavin-matrix analogue — a lower bound on $\det\gamma_{u(z)}$ conditionally on $n$ nearby values, uniform in $n$ and in the configuration — is not available. Existing Malliavin bounds degrade as $n$ grows, so the constant in $(\star)$ blows up with the number of points.
- **Moment order versus dimension.** Joint continuity in $y$ needs $\mathbb{E}|L(y,Q)-L(y',Q)|^n$ for $n>d/\gamma$, i.e. arbitrarily high $n$ as $d\to6^-$. Malliavin density estimates are typically proved for small $n$ and lose a factor per point, so the reachable $(d,\gamma)$ region shrinks exactly where the problem is interesting.
- **Criticality at $d=6$.** At $d=Q^\ast$ the relevant integrals diverge logarithmically. Deciding $d=6$ requires a gauge-function refinement (a $\log$-corrected capacity), of the type unavailable even in the Gaussian case for parabolic anisotropy.
- **Time–space anisotropy.** Standard local-time theory is cleanest for isotropic or product-type fields. The metric $|t-t'|^{1/4}+|x-x'|^{1/2}$ forces anisotropic Hausdorff measures, and sector conditions used to compare $\Delta$-balls with Euclidean ones are lossy.

## 6. The Gap

Proven: existence, joint continuity and Hölder regularity of $L$ for **additive** noise in all $d\le5$, with sharp exponent; and the same for **nonlinear** $\sigma$ when $d=1$.

Conjectured: the identical statement for nonlinear $\sigma$ in $2\le d\le5$, plus sharpness of $\gamma$ and the classification of $d=6$.

The exact missing step is the uniform-in-$n$ joint density bound $(\star)$ for the non-Gaussian solution, equivalently a Malliavin-calculus replacement for strong local nondeterminism:
$$\det \mathrm{Cov}\Big(u(z)\ \Big|\ u(z^1),\dots,u(z^n)\Big)\ \gtrsim\ \min_k \Delta(z,z^k)^{2d}\quad\text{a.s., with constants free of }n .$$
Every other ingredient (Berman's criterion, Kolmogorov's theorem, the anisotropic Hausdorff bookkeeping) is already in place.

## 7. Current Research (as of June 2026)

- **Malliavin-calculus school (Dalang, Khoshnevisan, Nualart, Chen, Song).** Pushing two-sided Gaussian density bounds from $d=1$ to systems, aiming to convert them into $(\star)$. Le Chen and collaborators' moment formulas for the parabolic Anderson model are the main new input. *(frontier — verify)*
- **Anisotropic Gaussian-field school (Xiao, Wu, Lee).** Refining LND with gauge functions to attack the critical case $d=Q^\ast$ for additive noise, as a rehearsal for $d=6$. *(frontier — verify)*
- **Regularity-structures / paracontrolled approaches (Hairer school, Berlin–Bonn–Warwick).** Local times of singular SPDEs (KPZ-type, $\Phi^4_3$) via reconstruction; so far continuity results for occupation densities of the KPZ height function are announced rather than published. *(frontier — verify)*
- **Rough-noise SHE.** Local times of SHE driven by fractional noise with $H<1/2$, continuing the Hu–Nualart programme; the noise roughness changes $Q^\ast$ and gives a one-parameter family of test cases.

## 8. Future Work

1. Prove a conditional-Malliavin LND inequality with constants independent of the number of conditioning points; this alone closes $2\le d\le5$.
2. Settle $d=6$ for additive noise first, using a logarithmic gauge $\varphi(r)=r^{6}\log\log(1/r)$ in the anisotropic Hausdorff measure.
3. Establish sharpness of $\gamma<\frac12(1-d/6)$ via a lower bound on the modulus of $L$ in $y$ (a Chung-type law of the iterated logarithm for $L$).
4. Develop intersection local times of two independent SHE solutions; the associated critical dimension should be $d<12$ and the Gaussian case is already tractable.
5. Transfer results to colored noise in spatial dimension $k\ge2$ and to the hyperbolic analogue (stochastic wave equation), where $H_1=H_2=1/2$ and $Q^\ast=4$.

## 9. Key References

- **[Foundational]** J. B. Walsh. *An Introduction to Stochastic Partial Differential Equations.* École d'Été de Probabilités de Saint-Flour XIV, Lecture Notes in Mathematics 1180, Springer, 1986.
- **[Foundational]** S. M. Berman. *Local times and sample function properties of stationary Gaussian processes.* Transactions of the American Mathematical Society 137 (1969), 277–299.
- **[Survey]** D. Geman, J. Horowitz. *Occupation densities.* The Annals of Probability 8 (1980), 1–67.
- **[Foundational]** L. D. Pitt. *Local times for Gaussian vector fields.* Indiana University Mathematics Journal 27 (1978), 309–330.
- **[Foundational]** C. Mueller, R. Tribe. *Hitting properties of a random string.* Electronic Journal of Probability 7 (2002), paper no. 10.
- **[SOTA]** R. C. Dalang, D. Khoshnevisan, E. Nualart. *Hitting probabilities for systems of non-linear stochastic heat equations with additive noise.* ALEA, Latin American Journal of Probability and Mathematical Statistics 3 (2007), 231–271.
- **[SOTA]** R. C. Dalang, D. Khoshnevisan, E. Nualart. *Hitting probabilities for systems of non-linear stochastic heat equations with multiplicative noise.* Probability Theory and Related Fields 144 (2009), 371–427.
- **[SOTA]** R. C. Dalang, C. Mueller, Y. Xiao. *Polarity of points for Gaussian random fields.* The Annals of Probability 45 (2017), 4700–4751.
- **[Foundational]** V. Bally, E. Pardoux. *Malliavin calculus for white noise driven parabolic SPDEs.* Potential Analysis 9 (1998), 27–64.
- **[SOTA]** L. Chen, Y. Hu, D. Nualart. *Regularity and Strict Positivity of Densities for the Nonlinear Stochastic Heat Equation.* Memoirs of the American Mathematical Society, 2021.
- **[Related]** Y. Hu, D. Nualart. *Stochastic heat equation driven by fractional noise and local time.* Probability Theory and Related Fields 143 (2009), 285–328.
- **[Survey]** M. B. Marcus, J. Rosen. *Markov Processes, Gaussian Processes, and Local Times.* Cambridge Studies in Advanced Mathematics 100, Cambridge University Press, 2006.
- **[Survey]** Y. Xiao. *Sample path properties of anisotropic Gaussian random fields.* In: A Minicourse on Stochastic Partial Differential Equations, Lecture Notes in Mathematics 1962, Springer, 2009, 145–212.
- **[Survey]** D. Khoshnevisan. *Analysis of Stochastic Partial Differential Equations.* CBMS Regional Conference Series in Mathematics 119, American Mathematical Society, 2014.

## 10. Worked Example / Concrete Special Case

**Additive noise, $d=1$, fixed time slice.** Take $\partial_t u=\partial_x^2u+\dot W$ on $\mathbb{R}$, $u(0,\cdot)=0$. Then
$$u(t,x)=\int_0^t\!\!\int_\mathbb{R} p_{t-s}(x-z)\,W(ds\,dz),\qquad p_r(x)=(4\pi r)^{-1/2}e^{-x^2/4r}.$$

Fix $t$ and put $h=x-x'$. By the Walsh isometry and Plancherel,
$$\int_\mathbb{R}\big(p_r(x-z)-p_r(x'-z)\big)^2dz=2\big(p_{2r}(0)-p_{2r}(h)\big)=\frac{2}{\sqrt{8\pi r}}\Big(1-e^{-h^2/8r}\Big),$$
so
$$\sigma^2(h):=\mathbb{E}\big[(u(t,x)-u(t,x'))^2\big]=\int_0^t \frac{2}{\sqrt{8\pi r}}\Big(1-e^{-h^2/8r}\Big)dr .$$
Substituting $r=h^2v/8$ gives $\sigma^2(h)=\frac{|h|}{4\sqrt\pi}\int_0^{8t/h^2}v^{-1/2}\big(1-e^{-1/v}\big)dv$, and since $\int_0^\infty v^{-1/2}(1-e^{-1/v})dv=\int_0^\infty w^{-3/2}(1-e^{-w})dw=-\Gamma(-\tfrac12)=2\sqrt\pi$,
$$\sigma^2(h)\ \nearrow\ \frac{|h|}{2}\qquad (t\to\infty),\qquad \sigma^2(h)\le \frac{|h|}{2}\ \text{ for all }t.$$
Thus $u(t,\cdot)$ is, up to the factor $1/\sqrt2$, Brownian in space; there are also constants $c_1,c_2>0$ with $c_1|h|\le\sigma^2(h)\le c_2|h|$ for $|h|\le 1$, $t\ge1$.

**Existence of the spatial local time.** Berman's criterion on $I=[0,1]$ requires
$$\int_0^1\!\!\int_0^1 \big(\sigma^2(x-x')\big)^{-1/2}dx\,dx'\ \le\ c_1^{-1/2}\int_0^1\!\!\int_0^1 |x-x'|^{-1/2}dx\,dx'=\tfrac{8}{3}c_1^{-1/2}<\infty,$$
so $L(\cdot,I)$ exists and lies in $L^2(dy)$ a.s.

**Continuity.** Strong LND of Brownian-type Gaussian processes gives, for $n\in\mathbb{N}$ and $\gamma<1/2$,
$$\mathbb{E}\big[|L(y,I)-L(y',I)|^{n}\big]\le C_{n,\gamma}|y-y'|^{n\gamma},$$
and Kolmogorov's theorem yields a version of $y\mapsto L(y,I)$ that is Hölder$(\gamma)$ for every $\gamma<1/2$ — the exponent predicted by Section 1 with the one-parameter index $Q^\ast=2$ and $d=1$: $\frac12(1-\frac12)$ replaced by $\frac{1}{2}(2-1)/1$ in the fixed-time normalisation.

**Where it breaks.** Replace $\dot W$ by $\sigma(u)\dot W$ with $\sigma$ non-constant. The quantity $\sigma^2(h)$ is no longer deterministic, the increment $u(t,x)-u(t,x')$ is not Gaussian, and the bound $\big(\sigma^2(h)\big)^{-1/2}\le c_1^{-1/2}|h|^{-1/2}$ must be replaced by $\mathbb{E}\big[|\det\mathrm{Cov}|^{-1/2}\big]$-type estimates obtainable only from the Malliavin matrix. In $d=1$ these exist (Chen–Hu–Nualart 2021); for $2\le d\le5$, with $n$ points, they do not — which is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*