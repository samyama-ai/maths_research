---
id: 09-probability/maximal-inequality-for-fractional-martingales
title: "Maximal Inequality for Fractional Martingales"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Maximal Inequality for Fractional Martingales

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/maximal-inequality-for-fractional-martingales` · **Status:** open

## 1. Problem Statement / Conjecture

Let $M=(M_t)_{t\ge 0}$ be a continuous local martingale with $M_0=0$ and quadratic variation $\langle M\rangle$. For $\alpha\in(-\tfrac12,\tfrac12)$ define the **fractional martingale** (Hu–Nualart–Song, 2009)

$$M^{\alpha}_t \;=\; \int_0^t (t-s)^{\alpha}\,dM_s ,\qquad t\ge 0 .$$

This is *not* a martingale for $\alpha\neq0$: the integrand depends on the terminal time $t$, so $M^\alpha$ is a Volterra process, and neither Doob's $L^p$ maximal inequality nor the Burkholder–Davis–Gundy (BDG) inequality applies to $\sup_{t\le T}|M^\alpha_t|$.

**Conjecture A (regular regime, $0<\alpha<\tfrac12$).** For every $p>0$ there is $C_{p,\alpha}<\infty$, depending only on $p$ and $\alpha$, with

$$\mathbb{E}\Big[\sup_{0\le t\le T}\big|M^{\alpha}_t\big|^{p}\Big]\;\le\; C_{p,\alpha}\,\mathbb{E}\Big[\langle M\rangle_T^{\,p(\alpha+\frac12)}\Big] \qquad\text{for all } T>0 .$$

**Conjecture B (singular regime, $-\tfrac12<\alpha<0$).** With the kernel-weighted bracket $A_T^{\alpha}:=\int_0^T (T-s)^{2\alpha}\,d\langle M\rangle_s$, for every $p>0$ there is $C_{p,\alpha}$ with

$$\mathbb{E}\Big[\sup_{0\le t\le T}\big|M^{\alpha}_t\big|^{p}\Big]\;\le\; C_{p,\alpha}\,\mathbb{E}\big[(A^{\alpha}_T)^{p/2}\big].$$

A complete solution means: prove both inequalities on the stated parameter ranges with the stated dependence of the constant, or exhibit a continuous local martingale $M$, an exponent $p$, and an $\alpha$ for which the ratio of the two sides is unbounded. A *sharp* solution would also settle the two-sided (BDG-type) version, i.e. whether a matching lower bound $c_{p,\alpha}\mathbb{E}[\,\cdot\,]\le \mathbb{E}[\sup_t|M^\alpha_t|^p]$ holds.

## 2. Mathematical Foundations

**Fractional Brownian motion (fBm).** $B^H$ is the centred Gaussian process with
$$\mathbb{E}[B^H_tB^H_s]=\tfrac12\big(t^{2H}+s^{2H}-|t-s|^{2H}\big),\qquad H\in(0,1),$$
introduced in the moving-average form by Mandelbrot and Van Ness (1968). It is $H$-self-similar with stationary increments and is a semimartingale only for $H=\tfrac12$.

**Volterra representation.** On $[0,T]$ one has $B^H_t=\int_0^t K_H(t,s)\,dW_s$ for a Brownian motion $W$ and an explicit kernel $K_H$ (Decreusefond–Üstünel 1999; Alòs–Mazet–Nualart 2001). The kernel $(t-s)^{\alpha}$ used above is the leading singular/smoothing part of $K_H$ with $H=\alpha+\tfrac12$.

**Characterization theorem (Hu–Nualart–Song 2009).** If $M$ is a continuous local martingale with $M_0=0$, $\alpha\in(-\tfrac12,\tfrac12)$, and $M^\alpha$ is defined as above, then
$$\langle M\rangle_t=t \ \ \forall t \iff \tfrac{1}{c_\alpha}M^{\alpha} \text{ is a fBm with } H=\alpha+\tfrac12 ,$$
where $c_\alpha^2 = 1/(2\alpha+1)$ normalizes the variance. This is the fractional analogue of Lévy's characterization of Brownian motion, and it is the reason $M^\alpha$ is the canonical "fractional martingale".

**Second-moment scaling.** For fixed $t$, $u\mapsto N^{(t)}_u:=\int_0^u (t-s)^\alpha dM_s$ *is* a martingale on $[0,t]$ with $\langle N^{(t)}\rangle_u=\int_0^u (t-s)^{2\alpha}d\langle M\rangle_s$. Hence classical BDG gives, for each **fixed** $t$ and $p>0$,
$$\mathbb{E}\big|M^{\alpha}_t\big|^{p}\;\le\;c_p\,\mathbb{E}\Big[\Big(\int_0^t (t-s)^{2\alpha}\,d\langle M\rangle_s\Big)^{p/2}\Big]. \tag{2.1}$$
When $\langle M\rangle_s=s$ this equals $c_p\,(2\alpha+1)^{-p/2}\,t^{p(\alpha+1/2)}$. The whole difficulty is exchanging "for each fixed $t$" with "uniformly in $t$", since the family $\{N^{(t)}\}_{t\le T}$ is an uncountable family of *different* martingales indexed by their own terminal time.

**Chaining tool.** The standard substitute is the Garsia–Rodemich–Rumsey (GRR) lemma (1970): if $\Psi$ is a Young function and $p$ a modulus,
$$\Psi\!\left(\frac{|f(t)-f(s)|}{4p(|t-s|)}\right)\le \frac{4B}{|t-s|^2},\qquad B=\int_0^T\!\!\int_0^T \Psi\!\left(\frac{|f(u)-f(v)|}{p(|u-v|)}\right)du\,dv .$$
With $\Psi(x)=x^p$ and $p(x)=x^{\gamma}$ this converts $L^p$ increment bounds into a sup bound, at the cost of requiring $p\gamma>1$.

## 3. History & State of the Art (SOTA)

- **1968.** Mandelbrot–Van Ness give fBm its moving-average kernel; the kernel $(t-s)^{H-1/2}$ appears.
- **1970–72.** GRR lemma; BDG inequalities (Burkholder–Davis–Gundy 1972) fix the martingale template: $\mathbb{E}[\sup_{t\le T}|M_t|^p]\asymp_p \mathbb{E}[\langle M\rangle_T^{p/2}]$ for all $p>0$.
- **1980.** Lenglart–Lépingle–Pratelli unify domination inequalities; Lenglart domination becomes the standard route to weak-type bounds for non-martingale processes dominated by increasing processes.
- **1999.** Novikov–Valkeila establish maximal inequalities for fBm itself (Gaussian case, $\langle M\rangle_t=t$), including two-sided moment bounds for $\sup_{t\le T}|B^H_t|$.
- **1999–2001.** Decreusefond–Üstünel, Alòs–Mazet–Nualart build stochastic calculus for Volterra-kernel Gaussian processes; the transfer principle $B^H=K_H\!\cdot\! W$ becomes routine.
- **2009.** Hu, Nualart and Song, *Fractional martingales and characterization of the fractional Brownian motion* (Ann. Probab. 37(6), 2404–2430), introduce $M^\alpha$, prove the Lévy-type characterization, and prove a maximal inequality of the form of Conjecture A **under a restriction on $p$** — an $L^p$-chaining/GRR argument that needs the exponent large enough relative to $\alpha$ (roughly $p\alpha>1$). They explicitly note the restriction is an artifact of the method.
- **2008–present.** Mishura's monograph and subsequent Volterra-process literature record the inequality with the same restriction; no unrestricted version has appeared.

**SOTA summary:** Conjecture A is a theorem for $\alpha\in(0,\tfrac12)$ and large $p$; it is open for small $p$ (in particular $p=1$ and $p=2$ when $\alpha$ is small). Conjecture B is open for all $p$ except in Gaussian or explicitly time-changed cases.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $\alpha=0$ (ordinary martingale) | **Proved**, all $p>0$ — BDG (1972), constants sharp in order. |
| $\langle M\rangle_t=t$ (i.e. $M^\alpha=c_\alpha B^H$) | **Proved**, all $p>0$, both directions, by Gaussian concentration / Fernique and Novikov–Valkeila (1999). |
| $\alpha\in(0,\tfrac12)$, $p$ large (roughly $p>1/\alpha$) | **Proved** — Hu–Nualart–Song (2009), via GRR chaining on $L^p$ increments. |
| Fixed time $t$, any $\alpha\in(-\frac12,\frac12)$, any $p>0$ | **Proved** — inequality (2.1), direct BDG on $N^{(t)}$. |
| $\langle M\rangle$ absolutely continuous with $c^{-1}\le d\langle M\rangle_s/ds\le c$ | **Proved** — kernel comparison reduces to the Gaussian/deterministic-clock case up to $c^{p(\alpha+1/2)}$. |
| Discrete-time analogue $\sum_{k\le n}(n-k)^{\alpha}\xi_k$, $\xi_k$ bounded martingale differences | **Proved** for $p\ge 2$ by Rosenthal + summation by parts. |
| $\alpha\in(-\frac12,0)$, Conjecture A's RHS $\langle M\rangle_T^{p(\alpha+1/2)}$ | **False** — see §10. |

## 5. Principal Obstacles

- **No martingale structure in $t$.** $M^\alpha$ is not a semimartingale in its own filtration for $\alpha\ne0$ (it is fBm with $H\ne\frac12$ in the model case). Doob's inequality, optional stopping and Lenglart domination all need an adapted supermartingale or a dominating increasing process; $|M^\alpha|^p$ has neither.
- **Time-change fails.** The Dambis–Dubins–Schwarz theorem removes $\langle M\rangle$ from ordinary BDG. Here the kernel $(t-s)^\alpha$ is written in *calendar* time while the bracket lives in *intrinsic* time; substituting $t=\tau_u$ turns the kernel into $(\tau_u-\tau_v)^\alpha$, a random, non-Markovian object, and destroys the self-similarity that makes the constant $\alpha$-only.
- **Chaining loses small $p$.** GRR and Kolmogorov-type criteria convert increment moments into sup bounds only when the moment exponent beats the Hölder exponent ($p\alpha>1$ here). For $p$ small the chaining sum diverges. The usual repair — good-$\lambda$ inequalities, which for martingales let one descend from $p\ge2$ to all $p>0$ — needs a stopping-time argument comparing $M^\alpha$ before and after a stopping time. The kernel makes $M^\alpha_t$ depend on the *whole* past with a $t$-dependent weight, so $M^\alpha_{t}-M^\alpha_{\tau}$ is not a fractional martingale of the shifted increments; the good-$\lambda$ splitting is unavailable.
- **Singular kernel, $\alpha<0$.** The weight $(t-s)^{\alpha}$ blows up at the diagonal. Any bracket that concentrates its mass just below $t$ inflates $M^\alpha_t$ without inflating $\langle M\rangle_T$ (§10). So the correct right-hand side must itself be kernel-weighted, and $A^\alpha_T$ is not adapted-increasing in $T$ — it is not even monotone — which again blocks domination arguments.
- **Rough-path machinery does not help.** Sewing/rough-path estimates control iterated integrals of a *given* rough path with known $p$-variation; here the roughness is the unknown being estimated, and the driver $M$ has random, possibly degenerate clock.

## 6. The Gap

Everything proven either (i) fixes $t$, (ii) fixes the clock $\langle M\rangle_t=t$, or (iii) buys uniformity in $t$ by paying a large moment exponent. The general statement asks for all three simultaneously: uniform in $t$, arbitrary random clock, arbitrary $p>0$.

Precisely, the missing step is a **stopping-time decomposition for Volterra integrals**: a way to write, for a stopping time $\tau\le t$,
$$M^\alpha_t \;=\; \underbrace{\int_0^{\tau}(t-s)^\alpha dM_s}_{\text{"past", depends on }t} \;+\; \int_\tau^t (t-s)^\alpha dM_s$$
with the first term controlled by $\mathcal{F}_\tau$-measurable data uniformly in $t\ge\tau$. Without it, no good-$\lambda$ or Lenglart argument closes, and $p\alpha>1$ remains the frontier for Conjecture A. For Conjecture B the gap is larger: even a restricted-$p$ version with the weighted bracket $A^\alpha_T$ on the right is not in the literature.

## 7. Current Research (as of June 2026)

- **Volterra/rough-volatility community.** Rough-volatility models use $\int_0^t(t-s)^{H-1/2}\sigma_s dW_s$ with $H\approx0.1$, i.e. exactly the singular regime $\alpha<0$ with random clock. Moment and maximal bounds needed for numerical-scheme error analysis are the practical driver for Conjecture B. *(frontier — verify)*
- **Sharp-constant programme.** Following the Marinelli–Röckner survey of BDG proofs, there is interest in reproving BDG by methods (Itô-calculus-free, domination-based) that might survive the Volterra perturbation. *(frontier — verify)*
- **Groups.** The Kansas/Barcelona/Beijing Malliavin-calculus circle around Hu, Nualart and Song remains the natural home of the problem; Volterra-Gaussian analysis groups in Kyiv (Mishura) and rough-path groups in Berlin/Oxford supply the $\alpha<0$ motivation.
- No preprint claiming the unrestricted inequality has been verified as of this review.

## 8. Future Work

1. **Interpolation downward in $p$.** Prove the $p=1$ case for $\alpha\in(0,\frac12)$ directly (weak-type $(1,1)$ for the Volterra maximal operator), then interpolate with the known large-$p$ case; this would give all $p\ge1$ at once.
2. **Deterministic maximal-operator route.** Bound the sublinear operator $f\mapsto \sup_t|\int_0^t (t-s)^\alpha f(s)ds|$ on weighted $L^p$ and transfer via the Burkholder decomposition; Muckenhoupt-type $A_p$ conditions on $d\langle M\rangle$ are the natural hypothesis.
3. **Discrete-to-continuum.** Establish the inequality for dyadic fractional martingale transforms with constants independent of the mesh, then pass to the limit — the classical Burkholder route.
4. **Counterexample hunt for small $p$.** For $\alpha$ close to $0^+$ and $p<1$, search among brackets alternating between near-zero and burst regimes; a failure here would show $p\alpha>1$ is not an artifact.
5. **Two-sided version.** Determine whether $\mathbb{E}[\sup_t|M^\alpha_t|^p]\gtrsim \mathbb{E}[(A^\alpha_T)^{p/2}]$ holds; this is unknown even for $\alpha>0$.

## 9. Key References

- **[Foundational]** B. B. Mandelbrot and J. W. Van Ness. *Fractional Brownian motions, fractional noises and applications.* SIAM Review 10(4), 422–437, 1968.
- **[Foundational]** D. L. Burkholder, B. J. Davis and R. F. Gundy. *Integral inequalities for convex functions of operators on martingales.* Proc. Sixth Berkeley Symposium on Mathematical Statistics and Probability, Vol. II, 223–240, Univ. California Press, 1972.
- **[Foundational]** A. M. Garsia, E. Rodemich and H. Rumsey Jr. *A real variable lemma and the continuity of paths of some Gaussian processes.* Indiana University Mathematics Journal 20, 565–578, 1970/71.
- **[Core]** Y. Hu, D. Nualart and J. Song. *Fractional martingales and characterization of the fractional Brownian motion.* Annals of Probability 37(6), 2404–2430, 2009.
- **[SOTA / Recent]** C. Marinelli and M. Röckner. *On the maximal inequalities of Burkholder, Davis and Gundy.* Expositiones Mathematicae 34(1), 1–26, 2016.
- **[Related]** A. A. Novikov and E. Valkeila. *On some maximal inequalities for fractional Brownian motions.* Statistics & Probability Letters 44(1), 47–54, 1999.
- **[Related]** E. Alòs, O. Mazet and D. Nualart. *Stochastic calculus with respect to Gaussian processes.* Annals of Probability 29(2), 766–801, 2001.
- **[Related]** L. Decreusefond and A. S. Üstünel. *Stochastic analysis of the fractional Brownian motion.* Potential Analysis 10, 177–214, 1999.
- **[Related]** E. Lenglart, D. Lépingle and M. Pratelli. *Présentation unifiée de certaines inégalités de la théorie des martingales.* Séminaire de Probabilités XIV, Lecture Notes in Mathematics 784, 26–48, Springer, 1980.
- **[Survey / Book]** Yu. Mishura. *Stochastic Calculus for Fractional Brownian Motion and Related Processes.* Lecture Notes in Mathematics 1929, Springer, 2008.
- **[Book]** D. Nualart. *The Malliavin Calculus and Related Topics.* 2nd ed., Springer, 2006.
- **[Book]** D. Revuz and M. Yor. *Continuous Martingales and Brownian Motion.* 3rd ed., Springer, 1999.

## 10. Worked Example / Concrete Special Case

**(a) The Gaussian benchmark.** Take $M=W$, so $\langle M\rangle_t=t$. Then $M^\alpha_t=\int_0^t(t-s)^\alpha dW_s$ is Gaussian with
$$\operatorname{Var}(M^\alpha_t)=\int_0^t (t-s)^{2\alpha}ds=\frac{t^{2\alpha+1}}{2\alpha+1},$$
so $M^\alpha=c_\alpha B^{H}$ with $H=\alpha+\frac12$, $c_\alpha=(2\alpha+1)^{-1/2}$. By self-similarity and Fernique's theorem, $\mathbb{E}[\sup_{t\le T}|M^\alpha_t|^p]=\kappa_{p,\alpha}T^{p(\alpha+1/2)}$ with $\kappa_{p,\alpha}<\infty$ for every $p>0$. Since $\langle M\rangle_T^{p(\alpha+1/2)}=T^{p(\alpha+1/2)}$, Conjecture A holds here with $C_{p,\alpha}=\kappa_{p,\alpha}$, **for all $p>0$** — no restriction. This is why the restriction $p\alpha>1$ is believed to be an artifact of the chaining proof.

**(b) Why the right-hand side must change when $\alpha<0$.** Fix $T=1$, $\varepsilon\in(0,1)$, and let
$$dM_s=\varepsilon^{-1/2}\,\mathbf{1}_{[1-\varepsilon,\,1]}(s)\,dW_s,\qquad\text{so}\qquad \langle M\rangle_1=\varepsilon^{-1}\!\!\int_{1-\varepsilon}^{1}\!\!ds=1 .$$
The bracket is pinned at $1$ for every $\varepsilon$. Now
$$\operatorname{Var}\big(M^{\alpha}_1\big)=\varepsilon^{-1}\int_{1-\varepsilon}^{1}(1-s)^{2\alpha}ds=\varepsilon^{-1}\int_0^{\varepsilon}u^{2\alpha}du=\frac{\varepsilon^{2\alpha}}{2\alpha+1}.$$
For $\alpha<0$ this diverges as $\varepsilon\downarrow0$, hence for any $p>0$,
$$\frac{\mathbb{E}[\sup_{t\le1}|M^\alpha_t|^p]}{\mathbb{E}[\langle M\rangle_1^{p(\alpha+1/2)}]}\;\ge\;\frac{\mathbb{E}|M^\alpha_1|^p}{1}\;=\;\gamma_p\Big(\frac{\varepsilon^{2\alpha}}{2\alpha+1}\Big)^{p/2}\;\xrightarrow[\varepsilon\to0]{}\;\infty,$$
where $\gamma_p=\mathbb{E}|Z|^p$, $Z\sim N(0,1)$. So Conjecture A's form is **false** for every $\alpha\in(-\frac12,0)$ — the clock, not just its total mass, matters. Note the weighted bracket tracks it correctly: $A^\alpha_1=\varepsilon^{2\alpha}/(2\alpha+1)$, so the ratio in Conjecture B stays at $\gamma_p$ in this example.

**(c) The same computation for $\alpha>0$.** Here $\varepsilon^{2\alpha}\to0$: concentrating the bracket near the terminal time *reduces* $M^\alpha_1$, because the smoothing kernel vanishes on the diagonal. This is the structural reason the regular regime is tractable and the singular regime is not.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*