---
id: 06-pdes/klein-gordon-small-data
title: "Klein Gordon Small Data"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Small-Data Global Existence and Asymptotics for Nonlinear Klein–Gordon Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/klein-gordon-small-data` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Consider the nonlinear Klein–Gordon (NLKG) Cauchy problem on $\mathbb{R}^{1+n}$,

$$\Box u + m^2 u = N(u, \partial u, \partial^2 u), \qquad \Box = \partial_t^2 - \Delta_x, \quad m > 0,$$

with data $(u,\partial_t u)|_{t=0} = \varepsilon(u_0,u_1)$ smooth, compactly supported (or rapidly decaying), and $N$ vanishing to order $\ge 2$ at the origin.

**Core question.** For which $n$, which nonlinearities $N$, and which classes of coupled systems does there exist $\varepsilon_0 > 0$ such that for all $\varepsilon < \varepsilon_0$ the solution is global in $t$, and what are its sharp asymptotics as $t \to \infty$ (linear scattering, or modified scattering with a logarithmic phase)?

A complete solution requires, for each configuration: (i) global existence with uniform bounds, (ii) sharp $L^\infty$ decay matching the linear rate $t^{-n/2}$, (iii) identification of the asymptotic profile, and (iv) sharpness — an example with the same structure whose solution blows up in finite time when the structural hypothesis fails.

The problem is marked **solved-recently** because its hardest flagship instance — the global nonlinear stability of Minkowski space for the Einstein–Klein–Gordon system, i.e. small-data global existence for a self-gravitating massive scalar field — was settled by LeFloch–Ma (2016) and Ionescu–Pausader (2022). Residual open cases in one space dimension and on curved backgrounds are listed in §6.

## 2. Mathematical Foundations

**Linear theory.** The free propagator has symbol $\langle\xi\rangle_m = \sqrt{|\xi|^2 + m^2}$; solutions of $\Box u + m^2 u = 0$ obey the dispersive estimate

$$\|u(t)\|_{L^\infty(\mathbb{R}^n)} \lesssim (1+|t|)^{-n/2}\,\big(\|u_0\|_{W^{k,1}} + \|u_1\|_{W^{k-1,1}}\big), \qquad k > n/2 + 1 .$$

Unlike the wave equation there is **no scaling invariance** ($m$ breaks it) and no null-cone concentration: energy propagates strictly inside the light cone, with group velocity $\xi/\langle\xi\rangle_m$ of modulus $<1$.

**Vector fields.** The Klein–Gordon equation commutes with $\partial_\alpha$, the Lorentz boosts $L_i = x_i\partial_t + t\partial_i$ and rotations $\Omega_{ij}$ — but **not** with the scaling field $S = t\partial_t + x\cdot\nabla$. Writing $Z$ for the admissible fields, Klainerman's Sobolev-type inequality in the interior cone gives

$$|u(t,x)| \lesssim (t^2-|x|^2)^{-n/4}\, t^{-n/4}\!\!\sum_{|\alpha|\le k}\|Z^\alpha u(t)\|_{L^2}, \qquad k > n/2 .$$

**Hyperboloidal foliation.** Set $\tau = \sqrt{t^2 - |x|^2}$ on $\{t > |x|\}$. In coordinates $(\tau,\underline{x})$ with $\underline{x}=x$, $t=\sqrt{\tau^2+|x|^2}$, the natural energy on hyperboloids $\mathcal{H}_\tau$ controls both $\partial u$ and $\tau t^{-1}\partial u$, and the wave operator becomes $\partial_\tau^2 + \frac{n}{\tau}\partial_\tau - \tau^{-2}\Delta_{\mathbb{H}^n}$ in the radial reduction — the basis of the LeFloch–Ma method.

**Normal forms and resonances.** For a quadratic term, the time-resonance function is
$$\Phi_{\pm\pm}(\xi,\eta) = \langle\xi\rangle_m \mp \langle\eta\rangle_m \mp \langle\xi-\eta\rangle_m .$$
Strict subadditivity of $\zeta \mapsto \sqrt{|\zeta|^2+m^2}$ for $m>0$ gives $|\Phi| \gtrsim m$ **uniformly**: quadratic Klein–Gordon interactions with a single mass are *never* time-resonant. Shatah's normal-form transformation $u \mapsto u + B(u,u)$, with $\widehat{B}(\xi)=\int \Phi^{-1}\hat u\hat u$, therefore converts quadratic into cubic nonlinearity with no loss of derivatives (at semilinear order). This is the single structural fact that makes NLKG far more tractable than the massless wave equation.

**Cubic obstruction.** Cubic terms have space-time resonant set $\{\xi=\eta=\sigma\}$, which is nonempty; the associated long-range effect produces **modified scattering** with a $\log t$ phase whenever $\int^\infty t^{-n}\,dt$ diverges, i.e. exactly at $n=1$.

## 3. History & State of the Art (SOTA)

- **1985.** Klainerman (CPAM) proves global existence for quadratic $N$ in $n=3$ by the vector-field method; Shatah (CPAM) proves the same by normal forms, extending to $n\ge 2$ for semilinear equations. The two papers define the two techniques still in use.
- **1990s.** Georgiev (1992) sharpens the decay machinery; Simon–Taflin (CMP 1993) and Ozawa–Tsutaya–Tsutsumi (Math. Z. 1996) settle the delicate $n=2$ quadratic case, where the normal form produces cubic terms decaying like $t^{-1}\cdot t^{-1}$ — borderline integrable.
- **1997.** Hörmander's lecture notes systematize the $\varepsilon$-lifespan hierarchy for quasilinear hyperbolic equations.
- **2001.** Delort (Ann. Sci. ENS) solves the quasilinear $n=1$ problem under a **null condition** on the cubic resonant coefficient, obtaining global solutions with modified scattering; an erratum (2006) corrects the multi-mass argument.
- **2004–2010.** Delort–Fang–Xue treat $n=2$ quasilinear systems with several masses; Germain–Masmoudi–Shatah introduce the space-time resonance formalism, unifying normal forms and stationary phase.
- **2016–2022.** LeFloch–Ma (CMP 2016) and Ionescu–Pausader (Annals of Math. Studies 213, 2022) prove global nonlinear stability of Minkowski space for **Einstein–Klein–Gordon**, the massive-field analogue of Christodoulou–Klainerman. Q. Wang (JDG 2020) gives an independent intrinsic-hyperboloid proof. Klainerman–Wang–Yang (CPAM 2020) settle massive Maxwell–Klein–Gordon.
- **2020s.** Attention shifts to $n=1$ with potentials and to non-generic/threshold resonances (Lindblad–Lührmann–Soffer; Germain–Pusateri).

## 4. Partial Results / Verified Cases

| Configuration | Status |
|---|---|
| $n \ge 3$, quadratic semilinear or quasilinear, single mass | Global, linear scattering (Klainerman 1985; Shatah 1985) |
| $n = 2$, quadratic, semilinear and quasilinear | Global, scattering (Simon–Taflin 1993; Ozawa–Tsutaya–Tsutsumi 1996; Delort–Fang–Xue 2004) |
| $n = 1$, cubic, null condition on the resonant coefficient | Global, modified scattering, $|u|\sim t^{-1/2}$ (Delort 2001) |
| $n = 1$, cubic $\pm u^3$ | Global with $\log t$ phase correction (Delort; Hayashi–Naumkin) |
| $n = 1$, quadratic with generic potential $V$ | Global, decay $t^{-1/2}$ (Lindblad–Lührmann–Soffer 2021; Germain–Pusateri 2022) |
| Wave–Klein–Gordon systems with null structure, $n = 3$ | Global (Katayama 2012; LeFloch–Ma 2014) |
| Einstein–Klein–Gordon, $n = 3$, asymptotically flat data | Global stability of Minkowski (LeFloch–Ma 2016; Wang 2020; Ionescu–Pausader 2022) |
| Massive Maxwell–Klein–Gordon, $n = 3$ | Global (Klainerman–Wang–Yang 2020) |
| $n = 1$, quadratic $u^2$, no null condition, no potential | Lifespan $\gtrsim \varepsilon^{-2}$ only; **open** |

## 5. Principal Obstacles

- **Loss of scaling.** The absent field $S$ removes one unit of the standard commuting algebra. Conformal-energy and scaling-based bootstrap arguments used for wave equations are simply unavailable; boosts $L_i$ grow like $t$ inside the cone, so each commutation costs a power of $t$ that must be reclaimed elsewhere.
- **Quasilinear derivative loss in normal forms.** Shatah's transformation divides by $\Phi \gtrsim m$, which is harmless semilinearly. For quasilinear $N$ containing $u\,\partial^2 u$, the multiplier $\Phi^{-1}$ carries a symbol of positive order; the resulting energy estimate loses derivatives unless a paradifferential (Bony) decomposition with a modified energy is used — Delort's technical core, and the reason $n=1$ took sixteen years after $n=3$.
- **Non-integrable cubic decay at $n = 1$.** After normal form the effective nonlinearity decays like $t^{-1}$; $\int^\infty t^{-1}dt = \infty$. No perturbative scheme closes; one must extract the resonant ODE exactly and prove that its solution has conserved modulus. Any error term merely $O(t^{-1})$ destroys the argument.
- **Mixed wave/Klein–Gordon coupling.** Massless fields decay like $t^{-1}$ along the cone and their vector-field algebra includes $S$; massive fields decay like $t^{-3/2}$ but exclude $S$. No single foliation is adapted to both — hyperboloids degenerate near the light cone, so wave components must be handled in the exterior by a separate mechanism and glued.
- **Slow decay of the metric.** In Einstein–Klein–Gordon, the ADM mass forces $g - \eta \sim r^{-1}$; the massive field propagates on a background that is never asymptotically flat fast enough for uniform-in-$t$ Fourier methods, requiring $t^{\delta}$-loss bookkeeping throughout.

## 6. The Gap

The gap between Section 4 and Section 1 is now narrow and concentrated in three places.

1. **$n=1$, quadratic, no structure.** For $\Box u + u = u^2$ on $\mathbb{R}^{1+1}$ with no potential and no null condition, no global result and no blow-up example is known; the best lower bound on the lifespan is $T_\varepsilon \gtrsim \varepsilon^{-2}$ (via one normal form). The missing step is control of the cubic resonant coefficient produced by the normal form when it fails to be purely imaginary — the precise dichotomy "purely imaginary $\Rightarrow$ global with $\log t$ phase / positive real part $\Rightarrow$ blow-up" is conjectured but unproven.
2. **Non-generic potentials and threshold resonances.** In $n=1$ with $V$ having a zero-energy resonance (the case relevant to kink stability in $\phi^4$), the required $L^1 \to L^\infty$ distorted-Fourier bounds degrade; only partial results exist.
3. **General curved backgrounds.** Small-data global existence for NLKG on a fixed non-stationary or slowly-decaying background (beyond Schwarzschild/Kerr perturbative regimes) has no general theory.

## 7. Current Research (as of June 2026)

- **Princeton / Brown (Ionescu, Pausader) and collaborators**: extending the Minkowski-stability framework to Einstein–Vlasov with massive particles and to non-compactly-supported data. *(frontier — verify)*
- **Sorbonne / Paris school (Delort, and successors)**: paradifferential normal forms with several masses and quasilinear couplings in $n=1,2$.
- **Johns Hopkins / Bonn (Lindblad, Lührmann, Soffer, Schlag)**: 1D asymptotics with variable-coefficient nonlinearities and non-generic potentials; kink asymptotic stability for $\phi^4$ remains the target application.
- **Berkeley (Ifrim, Tataru)**: "testing by wave packets" and quasilinear modified scattering, aiming at long-time (not merely global) results for general 1D dispersive models without null conditions.
- **Queen Mary / Oxford (LeFloch, Ma, Q. Wang)**: hyperboloidal-foliation refinements, applications to $f(R)$ gravity and to wave–Klein–Gordon with non-null quadratic terms.

## 8. Future Work

- Prove or disprove the conjectured dichotomy for $n=1$ quadratic NLKG by computing the sign of the effective cubic coefficient after two normal-form reductions.
- Develop a unified functional framework — likely a hybrid of wave packets and hyperboloidal energies — that handles massless and massive components without exterior/interior gluing.
- Establish asymptotic stability of the $\phi^4$ kink, the sharpest known consequence of 1D NLKG asymptotics with a threshold resonance.
- Extend small-data theory to Klein–Gordon on Kerr with a positive mass, where superradiance and the trapped null geodesics interact with the massive-field decay rate.

## 9. Key References

- **[Foundational]** S. Klainerman. *Global existence of small amplitude solutions to nonlinear Klein–Gordon equations in four space-time dimensions.* Comm. Pure Appl. Math. 38 (1985), 631–641.
- **[Foundational]** J. Shatah. *Normal forms and quadratic nonlinear Klein–Gordon equations.* Comm. Pure Appl. Math. 38 (1985), 685–696.
- **[Foundational]** L. Hörmander. *Lectures on Nonlinear Hyperbolic Differential Equations.* Mathématiques & Applications 26, Springer, 1997.
- **[Key]** J. Simon, E. Taflin. *The Cauchy problem for non-linear Klein–Gordon equations.* Comm. Math. Phys. 152 (1993), 433–478.
- **[Key]** T. Ozawa, K. Tsutaya, Y. Tsutsumi. *Global existence and asymptotic behavior of solutions for the Klein–Gordon equations with quadratic nonlinearity in two space dimensions.* Math. Z. 222 (1996), 341–362.
- **[Key]** J.-M. Delort. *Existence globale et comportement asymptotique pour l'équation de Klein–Gordon quasi-linéaire à données petites en dimension 1.* Ann. Sci. École Norm. Sup. 34 (2001), 1–61 (Erratum: 39 (2006), 335–345).
- **[Key]** J.-M. Delort, D. Fang, R. Xue. *Global existence of small solutions for quadratic quasilinear Klein–Gordon systems in two space dimensions.* J. Funct. Anal. 211 (2004), 288–323.
- **[SOTA]** P. G. LeFloch, Y. Ma. *The global nonlinear stability of Minkowski space for self-gravitating massive fields.* Comm. Math. Phys. 346 (2016), 603–665.
- **[SOTA]** A. D. Ionescu, B. Pausader. *The Einstein–Klein–Gordon Coupled System: Global Stability of the Minkowski Solution.* Annals of Mathematics Studies 213, Princeton University Press, 2022.
- **[SOTA]** Q. Wang. *An intrinsic hyperboloid approach for Einstein Klein–Gordon equations.* J. Differential Geom. 115 (2020), 27–109.
- **[SOTA]** S. Klainerman, Q. Wang, S. Yang. *Global solution for massive Maxwell–Klein–Gordon equations.* Comm. Pure Appl. Math. 73 (2020), 63–109.
- **[SOTA]** H. Lindblad, J. Lührmann, A. Soffer. *Asymptotics for 1D Klein–Gordon equations with variable coefficient quadratic nonlinearities.* Arch. Ration. Mech. Anal. 241 (2021), 1459–1527.
- **[SOTA]** P. Germain, F. Pusateri. *Quadratic Klein–Gordon equations with a potential in one dimension.* Forum of Mathematics, Pi 10 (2022), e17.
- **[Survey]** P. Germain, N. Masmoudi, J. Shatah. *Global solutions for the gravity water waves equation in dimension 3.* Ann. of Math. 175 (2012), 691–754. (Reference text for the space-time resonance method.)
- **[Survey]** P. G. LeFloch, Y. Ma. *The Hyperboloidal Foliation Method.* Series in Applied and Computational Mathematics 2, World Scientific, 2014.

## 10. Worked Example / Concrete Special Case

**Modified scattering for $\Box u + u = u^3$ in one space dimension.**

Take $\Box = \partial_t^2 - \partial_x^2$, $m=1$, data $\varepsilon(u_0,u_1)$ supported in $|x|\le 1$. Finite speed of propagation confines the solution to $|x| \le t+1$, so work in hyperbolic coordinates $\tau = \sqrt{t^2-x^2}$, $\rho = \operatorname{arctanh}(x/t)$. There $\Box = \partial_\tau^2 + \tfrac{1}{\tau}\partial_\tau - \tau^{-2}\partial_\rho^2$.

Insert the ansatz $u = \tau^{-1/2}\,\mathrm{Re}\!\left(A(\tau,\rho)\,e^{i\tau}\right)$, suggested by the linear decay rate $t^{-1/2}$.

*Step 1 — the linear part cancels to two orders.* With $A$ constant and $f = \tau^{-1/2}e^{i\tau}$:
$$f' = \big(-\tfrac12\tau^{-3/2} + i\tau^{-1/2}\big)e^{i\tau}, \qquad f'' = \big(\tfrac34\tau^{-5/2} - i\tau^{-3/2} - \tau^{-1/2}\big)e^{i\tau},$$
$$f'' + \tfrac{1}{\tau}f' + f = \big(\tfrac34 - \tfrac12\big)\tau^{-5/2}e^{i\tau} + \big(-i + i\big)\tau^{-3/2}e^{i\tau} = \tfrac14\,\tau^{-5/2}e^{i\tau}.$$
The $\tau^{-1/2}$ and $\tau^{-3/2}$ terms vanish identically; the residual is $O(\tau^{-5/2})$, which is integrable against $d\tau$ after one more power.

*Step 2 — the surviving nonlinear term.* Allowing $A=A(\tau)$, the coefficient of $\tau^{-3/2}e^{i\tau}$ on the left is $2i\,\partial_\tau A$. On the right,
$$u^3 = \tau^{-3/2}\Big(\tfrac{1}{8}\big(Ae^{i\tau} + \bar A e^{-i\tau}\big)^3\Big) = \tau^{-3/2}\Big(\tfrac38|A|^2A\,e^{i\tau} + \tfrac18 A^3 e^{3i\tau} + \text{c.c.}\Big).$$
The $e^{\pm 3i\tau}$ terms are non-resonant: integrating by parts in $\tau$ gains a factor $\tau^{-1}$ and they contribute $O(\tau^{-5/2})$. Only $\tfrac38|A|^2A$ survives.

*Step 3 — the resonant ODE.* Matching $\tau^{-3/2}e^{i\tau}$ coefficients,
$$2i\,\partial_\tau A = \tfrac38\,\tau^{-1}|A|^2 A \quad\Longrightarrow\quad \partial_\tau A = -\tfrac{3i}{16}\,\tau^{-1}|A|^2A .$$
Then $\partial_\tau |A|^2 = 2\,\mathrm{Re}(\bar A\partial_\tau A) = 0$: the modulus is exactly conserved. Hence
$$A(\tau,\rho) = A_\infty(\rho)\,\exp\!\Big(-\tfrac{3i}{16}\,|A_\infty(\rho)|^2\log\tau\Big),$$
$$u(t,x) \;\approx\; \tau^{-1/2}\,\mathrm{Re}\Big[A_\infty(\rho)\,e^{\,i\tau \,-\, \frac{3i}{16}|A_\infty(\rho)|^2\log\tau}\Big], \qquad \tau=\sqrt{t^2-x^2}.$$

*Reading the result.* The amplitude decays at the free rate $t^{-1/2}$, so the solution is global for $\varepsilon$ small (with $\|A_\infty\|_\infty = O(\varepsilon)$), but the phase carries an $O(\varepsilon^2\log t)$ correction. There is **no** asymptotic state in the free-evolution sense: $e^{-it\langle D\rangle}u(t)$ does not converge. This is *modified scattering*, and it is exactly the phenomenon that fails to appear for $n\ge 2$, where the cubic term decays like $t^{-1}\cdot t^{-n/2+1/2}$ and is integrable. Replacing $u^3$ by a general cubic $N$ changes $\tfrac{3}{16}$ into a coefficient $c(\rho)$; Delort's **null condition** is precisely the requirement that the real part of $c$ vanish, so that $|A|$ stays conserved. When $\mathrm{Re}\,c > 0$ the ODE $\partial_\tau|A|^2 = 2\,\mathrm{Re}(c)\tau^{-1}|A|^4$ blows up at $\tau \sim \exp(C/|A_\infty|^2)$ — the mechanism behind the conjectured dichotomy in §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*