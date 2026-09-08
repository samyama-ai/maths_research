---
id: 06-pdes/fractional-burgers-critical-regularity
title: "Global Regularity of the Fractional Burgers Equation at the Critical Exponent"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Regularity of the Fractional Burgers Equation at the Critical Exponent

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/fractional-burgers-critical-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the fractional (fractal) Burgers equation
$$\partial_t u + u\,\partial_x u + \Lambda^{\alpha} u = 0, \qquad u(x,0)=u_0(x), \quad x\in\mathbb{R}\ \text{or}\ \mathbb{T},\ t>0,$$
where $\Lambda^{\alpha}=(-\partial_x^2)^{\alpha/2}$ is the fractional Laplacian of order $\alpha\in(0,2]$. The **critical exponent** is $\alpha=1$: this is the unique value at which the scaling symmetry
$$u_\lambda(x,t)=\lambda^{\alpha-1}u(\lambda x,\lambda^{\alpha}t)$$
leaves $\|u\|_{L^\infty}$ invariant, so the $L^\infty$ maximum principle — the only globally coercive a priori bound available — is exactly scale-critical and provides no room for a perturbative argument.

**Core question.** For which combinations of dissipation order, spatial dimension, flux nonlinearity and velocity structure does the scale-critical dissipation $\Lambda^{1}$ suffice to prevent finite-time gradient blow-up (shock formation) for all smooth data?

For the scalar 1D case with quadratic flux the answer is **yes**, proved by Kiselev, Nazarov and Shterenberg (2008): every $u_0\in H^{1/2}$ (indeed $u_0 \in L^\infty$ with periodic or decaying data) yields a unique global smooth solution, real-analytic for $t>0$. What remains open is the critical-exponent problem in its natural generality:

1. **(General flux)** $\partial_t u + \partial_x f(u) + \Lambda u = 0$ with $f$ smooth, convex and superquadratic (e.g. $f(u)=u^3$): is every smooth solution global?
2. **(Nonlocal velocity)** $\partial_t\theta + \partial_x(\theta\, \mathcal{H}\theta) + \Lambda\theta = 0$ in divergence (as opposed to transport) form, and higher-dimensional analogues with a velocity field recovered from $\theta$ by an order-zero singular operator.
3. **(Supercritical range)** For $\alpha\in(0,1)$ blow-up is known; the **structure** of the singular set, the uniqueness class of entropy solutions, and the sharp regularity of entropy solutions remain open.

A complete resolution of (1) requires either a proof that $\|\partial_x u(\cdot,t)\|_{L^\infty}$ stays finite for all $t$ for all smooth data, or an explicit datum plus rigorous argument producing $\|\partial_x u(\cdot,t)\|_{L^\infty}\to\infty$ as $t\uparrow T<\infty$.

## 2. Mathematical Foundations

**Fractional Laplacian.** For $\alpha\in(0,2)$, on the Fourier side $\widehat{\Lambda^{\alpha}u}(\xi)=|\xi|^{\alpha}\hat u(\xi)$; pointwise,
$$\Lambda^{\alpha}u(x) = c_{\alpha}\,\mathrm{P.V.}\!\int_{\mathbb{R}}\frac{u(x)-u(y)}{|x-y|^{1+\alpha}}\,dy, \qquad c_\alpha=\frac{\alpha\,2^{\alpha-1}\Gamma\!\left(\frac{1+\alpha}{2}\right)}{\sqrt{\pi}\,\Gamma\!\left(1-\frac{\alpha}{2}\right)}>0.$$

**Maximum principle and Córdoba–Córdoba inequality.** For convex $\varphi$,
$$\varphi'(u)\Lambda^{\alpha}u \ \ge\ \Lambda^{\alpha}\varphi(u),$$
giving $\|u(\cdot,t)\|_{L^p}\le\|u_0\|_{L^p}$ for all $p\in[1,\infty]$ and the energy identity
$$\tfrac12\frac{d}{dt}\|u\|_{L^2}^2 = -\|\Lambda^{\alpha/2}u\|_{L^2}^2 .$$

**Scaling and criticality.** With $u_\lambda$ as above, $\|u_\lambda\|_{L^\infty}=\lambda^{\alpha-1}\|u\|_{L^\infty}$: subcritical $\alpha>1$, critical $\alpha=1$, supercritical $\alpha<1$. Correspondingly the equation is locally well-posed in $H^{s}$ for $s>\frac32-\alpha$, and $\dot H^{1/2}$ is the critical Sobolev space at $\alpha=1$.

**Modulus of continuity method (KNS).** A modulus of continuity is an increasing concave $\omega:(0,\infty)\to(0,\infty)$ with $\omega(0^+)=0$. Say $u$ *obeys* $\omega$ if $|u(x)-u(y)|<\omega(|x-y|)$ for all $x\ne y$. The family $\omega$ is preserved by the equation provided that at a hypothetical first breakdown time, with $\xi=|x-y|$,
$$\underbrace{\omega(\xi)\,\omega'(\xi)}_{\text{nonlinear steepening}} \;<\; \underbrace{D_\alpha(\xi)}_{\text{dissipation}},$$
where, from the pointwise kernel representation,
$$D_\alpha(\xi)\;\ge\; \frac{c_\alpha}{2}\!\int_0^{\xi/2}\!\frac{\omega(\xi+2\eta)+\omega(\xi-2\eta)-2\omega(\xi)}{\eta^{1+\alpha}}d\eta \;+\;\frac{c_\alpha}{2}\!\int_{\xi/2}^{\infty}\!\frac{\omega(2\eta+\xi)-\omega(2\eta-\xi)-2\omega(\xi)}{\eta^{1+\alpha}}d\eta .$$
Both sides are homogeneous of the same degree only when $\alpha=1$, which is exactly why the critical case demands a *logarithmically improved* modulus rather than a power one.

**Reference model.** The critical surface quasi-geostrophic (SQG) equation $\partial_t\theta+u\cdot\nabla\theta+\Lambda\theta=0$, $u=\nabla^{\perp}\Lambda^{-1}\theta$, shares the same criticality and is the archetype for all methods used here.

## 3. History & State of the Art (SOTA)

- **1948/1950.** Burgers introduces $u_t+uu_x=\nu u_{xx}$; the inviscid case forms shocks in finite time by characteristics.
- **2006.** Droniou and Imbert (*Arch. Ration. Mech. Anal.* 182) develop the theory of "fractal" first-order PDEs, establishing the Duhamel/regularizing framework for $\Lambda^\alpha$-dissipated conservation laws.
- **2007.** Alibaud, Droniou and Vovelle prove **shock formation for $\alpha<1$** and global smoothness for $\alpha>1$, leaving $\alpha=1$ open. Alibaud gives an entropy formulation valid across the supercritical range.
- **2007.** Kiselev, Nazarov and Volberg resolve critical SQG by the modulus-of-continuity method; Caffarelli and Vasseur independently prove it by De Giorgi iteration (*Ann. of Math.* 2010).
- **2008 — the breakthrough.** Kiselev, Nazarov, Shterenberg, *Blow up and regularity for fractal Burgers equation* (Dynamics of PDE 5): global well-posedness and analyticity at $\alpha=1$; finite-time blow-up for $0<\alpha<1$ for suitable smooth data.
- **2009.** Dong, Du and Li reprove critical global well-posedness by a nonlocal-maximum-principle/Besov argument and sharpen the blow-up statement (*Indiana Univ. Math. J.* 58).
- **2010.** Chan and Czubak extend critical regularity to the **$N$-dimensional Burgers system** with $\Lambda$ dissipation (*Ann. IHP–ANL* 27). Chan, Czubak and Silvestre prove **eventual regularization** in the slightly supercritical range. Alibaud and Andreianov show **non-uniqueness of weak (non-entropy) solutions** for $\alpha<1$.
- **2012.** Constantin and Vicol's nonlinear maximum principle gives a third, more robust proof of critical global regularity; Silvestre's Hölder estimates for drift-diffusion supply a De Giorgi–Nash route.
- **State of the art.** Critical scalar 1D and the critical multi-D vector Burgers system are settled. The critical superquadratic-flux problem, critical nonlocal-velocity divergence-form models, and the fine structure of supercritical shocks are not.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $\alpha\in(1,2]$, any $u_0\in L^2$ | Global smooth, analytic for $t>0$ | Droniou–Imbert 2006; Kiselev–Nazarov–Shterenberg 2008 |
| $\alpha=1$, $u_0\in H^{1/2}(\mathbb{R})$ or $L^\infty(\mathbb{T})$, flux $u^2/2$ | Global well-posedness + real analyticity | KNS 2008; Dong–Du–Li 2009 |
| $\alpha=1$, $N$-dimensional vector Burgers $\partial_t u+(u\cdot\nabla)u+\Lambda u=0$ | Global regularity for smooth data | Chan–Czubak 2010 |
| $\alpha\in(0,1)$ | Finite-time gradient blow-up from explicit odd, compactly-modulated data | KNS 2008; Alibaud–Droniou–Vovelle 2007 |
| $\alpha\in(0,1)$ | Global existence + uniqueness of **entropy** solutions in $L^\infty$ | Alibaud 2007; Alibaud–Imbert–Karch 2010 |
| $\alpha$ slightly $<1$ (log-supercritical $|\xi|/\log^{\beta}$) | Eventual regularity; global regularity for mild log corrections | Chan–Czubak–Silvestre 2010; Dabkowski–Kiselev–Vicol 2012 (SQG analogue) |
| $\alpha=1$, nonlocal velocity $\theta_t+(\mathcal{H}\theta)\theta_x+\Lambda\theta=0$ (transport form) | Global well-posedness | Kiselev 2011 (nonlocal maximum principles); Dong 2008 |
| $\alpha<1$, $L^\infty$ weak solutions | Non-uniqueness without entropy condition | Alibaud–Andreianov 2010 |

Asymptotics are also known: for $\alpha\in(1,2)$ solutions converge to the self-similar source solution of $\partial_t u+\Lambda^\alpha u=0$; at $\alpha=1$ the nonlinearity and dissipation balance in the long-time limit, and rarefaction-wave convergence holds for $\alpha\in(1,2)$ (Karch–Miao–Xu 2008).

## 5. Principal Obstacles

- **No supercritical coercive quantity.** Every conserved/monotone quantity ($L^p$ norms, entropy) is at best scale-invariant at $\alpha=1$. Standard energy methods produce $\frac{d}{dt}\|u\|_{\dot H^{s}}^2 \lesssim \|\partial_x u\|_{L^\infty}\|u\|_{\dot H^s}^2$ and the missing $\|\partial_x u\|_{L^\infty}$ control is precisely what is at stake — the estimate closes only through a Gronwall loop that criticality forbids.
- **Loss of the tie-breaking logarithm for general flux.** The KNS argument survives because the nonlinear term at the extremal pair is exactly $\omega\omega'$, matched against $D_1(\xi)$; the logarithmically-corrected modulus wins by a factor $\sim 1/\log(\xi/\delta)$. For $f(u)=u^3$ the steepening term becomes $\omega(\xi)^2\omega'(\xi)$, which is **not** balanced by $D_1$ under the only available bound $\|u\|_{L^\infty}\le\|u_0\|_{L^\infty}$ after rescaling: the amplitude enters at a higher power than the dissipation can absorb, and no modulus is known to be preserved.
- **Divergence versus transport form.** The Córdoba–Córdoba–Fontelos-type divergence models are not transported by a divergence-free field; the maximum principle degrades and the two-point extremal argument produces an uncontrolled term $\theta\,\partial_x\mathcal{H}\theta$ with no sign.
- **De Giorgi methods lose the constant.** Caffarelli–Vasseur/Silvestre-type Hölder estimates for $\partial_t u + b\cdot\nabla u+\Lambda u=0$ with $b\in L^\infty_t BMO_x$ give $C^\gamma$ with $\gamma$ *not* explicit and *not* stable under the nonlinear feedback $b=u$ when the flux is superquadratic; the bootstrap from $C^\gamma$ to $C^{1,\gamma}$ needs $\gamma>0$ uniform in time, which the iteration only delivers when the drift bound is critical, not supercritical.
- **Blow-up constructions are non-quantitative near $\alpha=1$.** The KNS blow-up uses a comparison functional whose gain degenerates as $\alpha\to1^-$; no candidate self-similar or nearly self-similar singular profile is known at $\alpha=1$ for any flux.

## 6. The Gap

Proven (§4): $\alpha=1$, quadratic flux, local velocity, any dimension. Claimed (§1): $\alpha=1$ for **superquadratic convex fluxes** and for **divergence-form nonlocal-velocity models**, plus a structural theory of supercritical shocks.

The precise missing step is a **scale-invariant nonlinear-versus-dissipative comparison that tolerates amplitude powers $>1$**. Concretely, one must either
- construct $\omega$ (or a nonlinear maximum principle of Constantin–Vicol type) satisfying $\;|f''|_{\infty,\,\|u_0\|_\infty}\,\omega(\xi)\,\omega'(\xi) < D_1(\xi)$ *uniformly in $\xi>0$* when $f$ is superquadratic — impossible for the KNS family, since the nonlinear side then carries an extra factor $\omega(\xi)$ that vanishes only at $\xi\to0$ while $D_1$ also degenerates linearly there; or
- exhibit a datum whose critical-flux dynamics steepens faster than the logarithmic dissipative gain, i.e. show the KNS logarithm is genuinely absent for $f(u)=u^3$.

Both alternatives require a new mechanism at the exact scaling boundary; no interpolation, smallness or perturbation of the known $\alpha=1$ result reaches them.

## 7. Current Research (as of June 2026)

- **Nonlinear maximum principles.** Extensions of Constantin–Vicol (GAFA 2012) to general fluxes and to bounded domains with the spectral or restricted fractional Laplacian, where the kernel loses translation invariance and the two-point method must be localized. *(frontier — verify)*
- **Log-supercritical thresholds.** Sharpening the Dabkowski–Kiselev–Vicol/Chan–Czubak–Silvestre programme: identifying the exact modulus of log-weakening $\Lambda/\log^\beta(2+\Lambda)$ for which regularity persists, with the conjectured threshold $\beta=1$ for Burgers-type fluxes. Groups: Duke (Kiselev), USC (Vicol at NYU/Courant), Chicago (Silvestre).
- **Entropy and singular-set theory in the supercritical range.** Alibaud, Andreianov and collaborators (Besançon, Franche-Comté) on uniqueness classes, splitting/BV structure of shocks, and numerical schemes convergent to entropy solutions for $\alpha<1$.
- **Stochastic and multiplicative-noise variants.** Regularization-by-noise for $\alpha\le1$ fractional conservation laws; whether noise restores uniqueness in the non-entropy class. *(frontier — verify)*
- **Machine-assisted search for critical blow-up profiles** for superquadratic fluxes, adapting the neural-network self-similar profile approach used for Euler-type equations. *(frontier — verify)*

## 8. Future Work

- Prove or disprove global regularity at $\alpha=1$ for $f(u)=u^{3}$; this is the single cleanest test of whether $L^\infty$-criticality or *flux*-criticality governs the problem.
- Develop a modulus-of-continuity theory in which the modulus itself evolves (a time-dependent family), removing the rigid requirement of a single stationary $\omega$.
- Establish uniform-in-$\alpha$ estimates as $\alpha\uparrow1$ that quantify the blow-up time $T_\alpha\to\infty$; a sharp rate would reveal the mechanism the critical logarithm replaces.
- Transfer critical Burgers technology to the divergence-form nonlocal model $\theta_t+\partial_x(\theta\mathcal{H}\theta)+\Lambda\theta=0$, whose inviscid version blows up by Córdoba–Córdoba–Fontelos (2005).
- Treat bounded domains and boundary layers, where even $\alpha>1$ well-posedness theory is incomplete.

## 9. Key References

- **[Foundational]** A. Kiselev, F. Nazarov, R. Shterenberg. *Blow up and regularity for fractal Burgers equation.* Dynamics of Partial Differential Equations, 5(3):211–240, 2008.
- **[Foundational]** N. Alibaud, J. Droniou, J. Vovelle. *Occurrence and non-appearance of shocks in fractal Burgers equations.* Journal of Hyperbolic Differential Equations, 4(3):479–499, 2007.
- **[Foundational]** J. Droniou, C. Imbert. *Fractal first-order partial differential equations.* Archive for Rational Mechanics and Analysis, 182(2):299–331, 2006.
- **[SOTA]** H. Dong, D. Du, D. Li. *Finite time singularities and global well-posedness for fractal Burgers equations.* Indiana University Mathematics Journal, 58(2):807–821, 2009.
- **[SOTA]** C. H. Chan, M. Czubak. *Regularity of solutions for the critical N-dimensional Burgers' equation.* Annales de l'Institut Henri Poincaré — Analyse Non Linéaire, 27(2):471–501, 2010.
- **[SOTA]** C. H. Chan, M. Czubak, L. Silvestre. *Eventual regularization of the slightly supercritical fractional Burgers equation.* Discrete and Continuous Dynamical Systems, 27(2):847–861, 2010.
- **[SOTA]** P. Constantin, V. Vicol. *Nonlinear maximum principles for dissipative linear nonlocal operators and applications.* Geometric and Functional Analysis, 22(5):1289–1321, 2012.
- **[SOTA]** N. Alibaud, B. Andreianov. *Non-uniqueness of weak solutions for the fractal Burgers equation.* Annales de l'Institut Henri Poincaré — Analyse Non Linéaire, 27(4):997–1016, 2010.
- **[SOTA]** N. Alibaud, C. Imbert, G. Karch. *Asymptotic properties of entropy solutions to fractal Burgers equation.* SIAM Journal on Mathematical Analysis, 42(1):354–376, 2010.
- **[Related]** A. Kiselev, F. Nazarov, A. Volberg. *Global well-posedness for the critical 2D dissipative quasi-geostrophic equation.* Inventiones Mathematicae, 167(3):445–453, 2007.
- **[Related]** L. Caffarelli, A. Vasseur. *Drift diffusion equations with fractional diffusion and the quasi-geostrophic equation.* Annals of Mathematics, 171(3):1903–1930, 2010.
- **[Related]** A. Córdoba, D. Córdoba, M. A. Fontelos. *Formation of singularities for a transport equation with nonlocal velocity.* Annals of Mathematics, 162(3):1377–1389, 2005.
- **[Related]** M. Dabkowski, A. Kiselev, V. Vicol. *Global well-posedness for a slightly supercritical surface quasi-geostrophic equation.* Nonlinearity, 25(5):1525–1535, 2012.
- **[Survey]** A. Kiselev. *Regularity and blow up for active scalars.* Mathematical Modelling of Natural Phenomena, 5(4):225–255, 2010.
- **[Survey]** L. Silvestre. *Hölder estimates for advection fractional-diffusion equations.* Annali della Scuola Normale Superiore di Pisa, Classe di Scienze, 11(4):843–855, 2012.

## 10. Worked Example / Concrete Special Case

**Scaling heuristic that isolates $\alpha=1$.** Take a steepening front of amplitude $A$ and width $\delta$: $u(x)\approx A\,\phi(x/\delta)$ with $\phi$ a fixed odd profile. Then

- nonlinear steepening: $|u\partial_x u| \sim A^2/\delta$;
- dissipation: $|\Lambda^\alpha u| \sim A/\delta^{\alpha}$.

Their ratio is
$$R(\delta)=\frac{A^2/\delta}{A/\delta^{\alpha}} = A\,\delta^{\alpha-1}.$$
By the maximum principle $A\le\|u_0\|_{L^\infty}$ is fixed. As $\delta\to0$:

| $\alpha$ | $R(\delta)$ as $\delta\to0$ | Outcome |
|---|---|---|
| $>1$ | $\to 0$ | dissipation wins at small scales — global regularity (subcritical) |
| $<1$ | $\to\infty$ | steepening wins — shock forms (proved by KNS 2008) |
| $=1$ | $\equiv A$ | exact tie at every scale — **critical** |

**How the tie is broken at $\alpha=1$ (KNS).** Fix $\delta>0$ and $\gamma>0$ small, and define
$$\omega(\xi)=\begin{cases}\xi-\xi^{3/2}, & 0<\xi\le\delta,\\[2pt] \omega(\delta)+\displaystyle\int_\delta^{\xi}\frac{\gamma\,ds}{s\big(4+\log(s/\delta)\big)}, & \xi>\delta.\end{cases}$$
This $\omega$ is continuous, increasing, concave, with $\omega'(0^+)=1$ and $\omega(\infty)=\infty$ (so any smooth compactly-supported $u_0$ obeys $\omega$ after the rescaling $u\mapsto\lambda u(\lambda x,t)$, which preserves the equation at $\alpha=1$).

Suppose the modulus is first violated at time $T$ at a pair $x\ne y$ with $\xi=|x-y|$, so $u(x)-u(y)=\omega(\xi)$. The transport term contributes at most $\omega(\xi)\omega'(\xi)$ to $\frac{d}{dt}\big(u(x)-u(y)\big)$, while the dissipative term contributes at most $-D_1(\xi)$ with $D_1$ as in §2. Two regimes:

- **Small $\xi\le\delta$:** $\omega(\xi)\omega'(\xi)\le \xi$, while the first integral in $D_1$ picks up the concavity defect $-\xi^{3/2}$ and gives $D_1(\xi)\gtrsim \xi^{1/2}\cdot\xi\cdot\xi^{-1}\cdot C = C\xi^{1/2}\cdot\xi^{1/2}$; choosing the exponent $3/2$ makes $D_1(\xi)\ge c\,\xi$ with $c>1$ for $\delta$ small, so the inequality is strict.
- **Large $\xi>\delta$:** $\omega'(\xi)=\dfrac{\gamma}{\xi(4+\log(\xi/\delta))}$ and $\omega(\xi)\le \delta+\gamma\log(4+\log(\xi/\delta))\cdot C$, hence
$$\omega(\xi)\omega'(\xi)\ \lesssim\ \frac{\gamma\,\omega(\xi)}{\xi\log(\xi/\delta)},$$
whereas the far-field integral gives $D_1(\xi)\gtrsim \dfrac{\omega(\xi)}{\xi}$. For $\gamma$ small enough, $\omega\omega' < D_1$ for every $\xi>\delta$.

So the strict inequality holds on $(0,\infty)$, no first breakdown time exists, and $\omega$ is preserved for all time. Since $\omega'(0^+)=1<\infty$, this yields $\|\partial_x u(\cdot,t)\|_{L^\infty}\le \omega'(0^+)=1$ uniformly in $t$ — a global Lipschitz bound, from which global smoothness and analyticity follow by standard bootstrapping.

**Where the argument dies for $f(u)=u^3$.** The steepening bound becomes $u(x)^2\,\omega'(\xi)\le \|u_0\|^2_{L^\infty}\omega'(\xi)$ in the far field, but the critical rescaling $u\mapsto\lambda u(\lambda x,\lambda t)$ no longer preserves the cubic equation ($\lambda^2 u^2 u_x$ picks up an extra $\lambda$). One cannot normalize $\|u_0\|_{L^\infty}$ to be small, so the constant multiplying $\omega\omega'$ is unbounded and no choice of $\gamma$ restores the inequality. This single lost normalization is the whole of the gap in §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*