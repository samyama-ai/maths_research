---
id: 06-pdes/chemotaxis-navier-stokes-regularity
title: "Global Well-posedness of the Chemotaxis–Navier–Stokes System in Three Dimensions"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Well-posedness of the Chemotaxis–Navier–Stokes System in Three Dimensions

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/chemotaxis-navier-stokes-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Tuval–Goldstein model of oxytactic bacteria suspended in an incompressible fluid, on a bounded smooth domain $\Omega \subset \mathbb{R}^3$:

$$
\begin{cases}
n_t + u\cdot\nabla n = \Delta n - \nabla\!\cdot\!\big(n\,\chi(c)\nabla c\big), \\[2pt]
c_t + u\cdot\nabla c = \Delta c - n f(c), \\[2pt]
u_t + \kappa\,(u\cdot\nabla)u = \Delta u - \nabla P + n\nabla\phi, \qquad \nabla\cdot u = 0 .
\end{cases}
$$

**Question.** For $\kappa = 1$ (full Navier–Stokes), $\chi \equiv 1$, $f(c)=c$, and arbitrary smooth initial data $(n_0 \ge 0,\, c_0 \ge 0,\, u_0)$ of arbitrary size, does the system possess a **global-in-time classical solution**, unique in a natural class, which remains bounded and converges to the homogeneous steady state $\big(\overline{n_0},\,0,\,0\big)$ as $t\to\infty$?

A complete resolution requires either (i) a proof of global existence, uniqueness and boundedness of smooth solutions for all large data; or (ii) an explicit initial datum for which the solution's $L^\infty$ norm blows up in finite time, or a proof of non-uniqueness in the energy class. The problem is listed as **partially-solved**: global *weak* solutions exist for all data, and global *classical* solutions are known under smallness, dimensional reduction, or structural modification — but large-data 3D classical well-posedness is open, and remains open even for the Stokes simplification $\kappa=0$.

## 2. Mathematical Foundations

**Unknowns.** $n(x,t)\ge 0$ is the bacterial density, $c(x,t)\ge0$ the oxygen concentration, $u(x,t)\in\mathbb{R}^3$ the fluid velocity, $P$ the pressure. The gravitational potential $\phi \in C^{1+\beta}(\bar\Omega)$ models buoyancy: cells are denser than water, so their excess mass forces the fluid.

**Boundary and initial conditions.** No-flux for cells, no-flux for oxygen, no-slip for the fluid:
$$
\big(\nabla n - n\chi(c)\nabla c\big)\cdot\nu = 0,\qquad \partial_\nu c = 0, \qquad u = 0 \quad \text{on } \partial\Omega\times(0,\infty).
$$

**Structural hypotheses.** $\chi \in C^2([0,\infty))$ positive, $f\in C^1([0,\infty))$ with $f(0)=0$, $f>0$ on $(0,\infty)$. The prototype is $\chi\equiv \chi_0>0$, $f(c)=c$.

**Two exact conservation/decay laws.**
$$
\frac{d}{dt}\int_\Omega n = 0 \quad\Rightarrow\quad \|n(\cdot,t)\|_{L^1} = \|n_0\|_{L^1}, \qquad\qquad
\|c(\cdot,t)\|_{L^\infty} \le \|c_0\|_{L^\infty},
$$
the second by the maximum principle, since $-nf(c)\le 0$. Unlike the classical Keller–Segel system, oxygen is *consumed*, not produced; there is no zeroth-order production term to amplify aggregation.

**Quasi-energy functional (Winkler).** For $\chi\equiv1$, $f(c)=c$ and $\Omega$ convex,
$$
\mathcal{F}(t) = \int_\Omega n\ln n \;+\; 2\int_\Omega |\nabla \sqrt{c}\,|^2 \;+\; K\int_\Omega |u|^2
$$
satisfies a differential inequality of the form
$$
\frac{d}{dt}\mathcal{F} + \int_\Omega \frac{|\nabla n|^2}{n} + \int_\Omega c\,\big|D^2\ln c\big|^2 + \int_\Omega |\nabla u|^2 \;\le\; C\big(1+\mathcal{F}\big),
$$
supplying the a priori bounds $n\in L^\infty_{loc}(L\log L)$, $\nabla\sqrt{n}\in L^2_{loc}(L^2)$, $u \in L^\infty_{loc}(L^2)\cap L^2_{loc}(H^1)$. In 2D these bounds are *supercritical* for the drift term and close the argument; in 3D they are strictly *subcritical*.

**Scaling.** The parabolic scaling $n_\lambda = \lambda^2 n(\lambda x,\lambda^2 t)$, $c_\lambda = c(\lambda x,\lambda^2 t)$, $u_\lambda = \lambda u(\lambda x,\lambda^2 t)$ leaves the chemotaxis and Navier–Stokes operators invariant. The invariant norm for $n$ is $L^{d/2}$: mass ($L^1$) is critical in $d=2$ and subcritical in $d=3$, where $L^{3/2}$ control is needed. The buoyancy force $n\nabla\phi$ scales as $\lambda^2$ while the Navier–Stokes momentum balance demands $\lambda^3$, so the fluid coupling is *subcritical* — the difficulty is the taxis nonlinearity, not the fluid.

## 3. History & State of the Art (SOTA)

- **2005.** Tuval, Cisneros, Dombrowski, Wolgemuth, Kessler and Goldstein (PNAS) derive the model from experiments on *Bacillus subtilis* suspensions near contact lines, observing bioconvection plumes.
- **2010.** Lorz (M3AS) constructs local solutions and 2D global weak solutions. Duan, Lorz and Markowich (Comm. PDE) prove global existence in $\mathbb{R}^3$ for small data, or for large data with vanishing $\phi$. Di Francesco, Lorz and Markowich treat nonlinear diffusion $\Delta n^m$.
- **2011.** Liu and Lorz (Ann. IHP) obtain global weak solutions for the 3D chemotaxis–**Stokes** case under structural conditions on $\chi, f$.
- **2012.** Winkler (Comm. PDE) proves global classical bounded solutions in 2D for the Navier–Stokes case and global weak solutions in 3D for the Stokes case ($\kappa=0$), with $\Omega$ convex. This is the reference result of the field.
- **2014.** Winkler (ARMA) proves 2D stabilization: $(n,c,u)\to(\overline{n_0},0,0)$ in $L^\infty$ exponentially. Zhang and Zheng (SIAM J. Math. Anal.) obtain 2D global well-posedness with general chemotactic sensitivity.
- **2016–2017.** Winkler (Ann. IHP) constructs global weak solutions for the full 3D **Navier**–Stokes system; in TAMS (2017) he proves that 3D chemotaxis–Stokes weak solutions become smooth after some finite time $T_0$ and stabilize — an "eventual regularity" theorem analogous to Leray's.
- **2016–2026.** Extensive work on modified models: nonlinear (porous-medium) diffusion, saturated sensitivity, rotational (matrix-valued) fluxes, logistic sources, and singular sensitivity. Large-data 3D classical well-posedness of the original model is untouched.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $d=2$, $\kappa=1$, large data | global classical, bounded, exponential stabilization | Winkler 2012, 2014 |
| $d=3$, $\kappa=0$ (Stokes), large data | global **weak** solutions, $\Omega$ convex | Winkler 2012; Liu–Lorz 2011 |
| $d=3$, $\kappa=1$, large data | global weak solutions | Winkler 2016 |
| $d=3$, $\kappa=0$, large data | eventual smoothness: $\exists\,T_0$ with solution smooth on $\Omega\times(T_0,\infty)$ | Winkler 2017 (TAMS) |
| $d=3$, $u\equiv0$, $\|c_0\|_{L^\infty}\le \frac{1}{6(d+1)\|\chi\|_{L^\infty}}$ | global classical bounded | Tao 2011 (JMAA) |
| $d=3$, $u\equiv0$, large data | global weak + eventual smoothness | Tao–Winkler 2012 (JDE) |
| $d=3$, $\kappa=1$, small $\|n_0\|_{L^{3/2}}$, $\|c_0\|_{L^\infty}$, $\|u_0\|_{L^3}$ | global classical, matrix-valued sensitivity | Cao–Lankeit 2016 (Calc. Var.) |
| $\mathbb{R}^3$, small data in critical Besov/Sobolev spaces | global classical, temporal decay | Duan–Lorz–Markowich 2010; Chae–Kang–Lee 2014 |
| $d=3$, diffusion $\Delta n^m$ with $m>\tfrac{7}{6}$ (Stokes), $m > \tfrac{9}{8}$ variants | global bounded weak/strong solutions | Winkler 2015 (Calc. Var.), Tao–Winkler |
| $d=3$, saturated sensitivity $|S(n)|\le C(1+n)^{-\alpha}$, $\alpha>0$ | global bounded classical | Winkler, JMFM 2018 |
| Regularity criteria | $n \in L^\infty_t L^{3/2+\varepsilon}_x$ or $\|\nabla c\|_{L^\infty}$ bounded $\Rightarrow$ smoothness | Chae–Kang–Lee 2013 (DCDS) |

## 5. Principal Obstacles

- **Supercriticality of the drift.** The a priori bounds available for all data are $L^1$ mass, $L\log L$ entropy, and $\|c\|_{L^\infty}$. In $d=3$ the taxis term $\nabla\cdot(n\nabla c)$ requires $n$ controlled in $L^{3/2}$ *uniformly in time*; entropy gives only $L\log L\hookrightarrow$ nothing better than $L^1$-type control after $t$-integration. The gap is exactly one scaling power.
- **Failure of Moser–Trudinger.** The 2D proof closes because $\int n\ln n$ and $\|\nabla\sqrt{n}\|_{L^2}$ combine through the 2D Moser–Trudinger / Gagliardo–Nirenberg inequality $\|v\|_{L^4}^4 \le C\|\nabla v\|_{L^2}^2\|v\|_{L^2}^2$ with $v=\sqrt n$. In 3D the corresponding exponent is $\|v\|_{L^{10/3}}^{10/3}$, and the resulting Grönwall inequality is superlinear: it yields only local-in-time bounds.
- **Boundary terms.** On a bounded domain, the entropy computation produces $\int_{\partial\Omega}|\nabla c|^2 \partial_\nu|\nabla c|$-type traces controlled only when $\partial\Omega$ is convex ($\partial_\nu|\nabla c|^2\le0$). Non-convex domains are open even in 2D for some formulations.
- **No known monotone quantity at the critical scale.** Unlike Navier–Stokes, where $L^2$ energy is the exact scaling-critical deficit, here two competing nonlinearities (taxis, advection) share dissipation; no Lyapunov functional dominating $\|n\|_{L^{3/2}}$ has been found.
- **Weak solutions are not known to be unique.** The 3D weak solutions of Winkler (2016) are of "generalized/supersolution" type; energy-inequality uniqueness fails for the same reason as in Leray–Hopf theory, compounded by the low regularity of $n$.

## 6. The Gap

Everything proven falls on one side of a single threshold: a time-uniform bound on $\|n(\cdot,t)\|_{L^{p}}$ for some $p>3/2$, or equivalently $\|\nabla c(\cdot,t)\|_{L^{q}}$ for some $q>3$. Given such a bound, Moser iteration plus maximal Sobolev regularity for the Stokes operator upgrades the solution to $C^{2,1}$ and continuation is immediate (Chae–Kang–Lee criterion). Every large-data 3D theorem to date obtains either (a) $L^{3/2}$ *locally in time*, (b) $L^{p}$ *after* an unquantified waiting time $T_0$ (eventual smoothness), or (c) $L^p$ globally under smallness or after weakening the taxis nonlinearity. The missing step is a **global-in-time, large-data, scaling-critical estimate for $n$ in $L^{3/2}$ with a quantitative continuation criterion at $t=0^+$** — or a construction showing that the consumption structure $-nc$, though damping, cannot prevent a self-similar concentration of $n$ along a shrinking plume.

## 7. Current Research (as of June 2026)

- **The Winkler school (Paderborn)** and collaborators (Lankeit, Tao, Wang) continue the programme of identifying minimal structural weakenings — nonlinear diffusion exponents, saturation thresholds, rotational fluxes — that restore global boundedness, mapping the boundary of the blow-up region.
- **Eventual-regularity refinements.** Attempts to quantify $T_0$ in Winkler's TAMS theorem in terms of $\|n_0\|_{L\log L}$, and to extend eventual smoothness from Stokes to Navier–Stokes. *(frontier — verify)*
- **Critical-space Cauchy theory.** Groups working in $\mathbb{R}^3$ (Chae–Kang–Lee lineage, and Besov-space analysts) pursue well-posedness in scaling-invariant spaces $\dot B^{-2+3/p}_{p,\infty}$ for $n$ paired with $\dot B^{-1+3/q}_{q,\infty}$ for $u$, seeking the analogue of Koch–Tataru theory.
- **Mixing and suppression of blow-up.** Following Kiselev–Ryzhik and Kiselev–Xu, the question of whether ambient or self-generated fluid advection can *suppress* chemotactic concentration in 3D is active; results exist for prescribed relaxation-enhancing flows, not for the self-consistent buoyancy coupling. *(frontier — verify)*
- **Numerics.** Structure-preserving (positivity- and mass-preserving) finite-volume and IMEX schemes are used to probe plume formation; no computation to date exhibits credible finite-time blow-up in the consumption model, which is taken as weak evidence for global regularity.

## 8. Future Work

1. **Prove or refute a Serrin-type criterion at the endpoint** $n \in L^\infty_t L^{3/2}_x$, closing the "eventual" to "global" gap.
2. **Partial regularity theory.** Develop a Caffarelli–Kohn–Nirenberg analogue: bound the parabolic Hausdorff dimension of the singular set of 3D weak solutions. No such theorem exists for the chemotaxis–fluid coupling.
3. **Uniqueness of weak solutions** in the class where the entropy inequality holds, or a Ladyzhenskaya–Prodi–Serrin condition covering both $n$ and $u$.
4. **Blow-up constructions.** Adapt the self-similar and modulation techniques used for supercritical Keller–Segel to the consumption model, testing whether $\|c\|_{L^\infty}$ decay genuinely obstructs concentration.
5. **Sharp smallness thresholds.** Determine the optimal constant in Tao's condition $\|c_0\|_{L^\infty}\le \frac{1}{6(d+1)\|\chi\|_\infty}$ and whether it is a genuine transition or an artifact of the method.

## 9. Key References

- **[Foundational]** I. Tuval, L. Cisneros, C. Dombrowski, C. W. Wolgemuth, J. O. Kessler, R. E. Goldstein. *Bacterial swimming and oxygen transport near contact lines.* Proc. Natl. Acad. Sci. USA 102 (2005), 2277–2282.
- **[Foundational]** A. Lorz. *Coupled chemotaxis fluid model.* Math. Models Methods Appl. Sci. 20 (2010), 987–1004.
- **[Foundational]** R. Duan, A. Lorz, P. Markowich. *Global solutions to the coupled chemotaxis-fluid equations.* Comm. Partial Differential Equations 35 (2010), 1635–1673.
- **[Foundational]** J.-G. Liu, A. Lorz. *A coupled chemotaxis-fluid model: global existence.* Ann. Inst. H. Poincaré Anal. Non Linéaire 28 (2011), 643–652.
- **[SOTA]** M. Winkler. *Global large-data solutions in a chemotaxis-(Navier–)Stokes system modeling cellular swimming in fluid drops.* Comm. Partial Differential Equations 37 (2012), 319–351.
- **[SOTA]** M. Winkler. *Stabilization in a two-dimensional chemotaxis-Navier–Stokes system.* Arch. Ration. Mech. Anal. 211 (2014), 455–487.
- **[SOTA]** M. Winkler. *Global weak solutions in a three-dimensional chemotaxis–Navier–Stokes system.* Ann. Inst. H. Poincaré Anal. Non Linéaire 33 (2016), 1329–1352.
- **[SOTA]** M. Winkler. *How far do chemotaxis-driven forces influence regularity in the Navier–Stokes system?* Trans. Amer. Math. Soc. 369 (2017), 3067–3125.
- **[SOTA]** Y. Tao, M. Winkler. *Eventual smoothness and stabilization of large-data solutions in a three-dimensional chemotaxis system with consumption of oxygen.* J. Differential Equations 252 (2012), 2520–2543.
- **[SOTA]** Y. Tao. *Boundedness in a chemotaxis model with oxygen consumption by bacteria.* J. Math. Anal. Appl. 381 (2011), 521–529.
- **[SOTA]** X. Cao, J. Lankeit. *Global classical small-data solutions for a three-dimensional chemotaxis Navier–Stokes system involving matrix-valued sensitivities.* Calc. Var. Partial Differential Equations 55 (2016), art. 107.
- **[SOTA]** D. Chae, K. Kang, J. Lee. *Existence of smooth solutions to coupled chemotaxis-fluid equations.* Discrete Contin. Dyn. Syst. 33 (2013), 2271–2297.
- **[SOTA]** D. Chae, K. Kang, J. Lee. *Global existence and temporal decay in Keller–Segel models coupled to fluid equations.* Comm. Partial Differential Equations 39 (2014), 1205–1235.
- **[SOTA]** Q. Zhang, Y. Zheng. *Global well-posedness for the two-dimensional incompressible chemotaxis–Navier–Stokes equations.* SIAM J. Math. Anal. 46 (2014), 3078–3105.
- **[Survey]** N. Bellomo, A. Bellouquid, Y. Tao, M. Winkler. *Toward a mathematical theory of Keller–Segel models of pattern formation in biological tissues.* Math. Models Methods Appl. Sci. 25 (2015), 1663–1763.
- **[Survey]** J. Lankeit, M. Winkler. *Facing low regularity in chemotaxis systems.* Jahresber. Dtsch. Math.-Ver. 122 (2020), 35–64.

## 10. Worked Example / Concrete Special Case

**The $L^p$ estimate and exactly where 3D fails.** Take $\chi\equiv1$, $f(c)=c$, and test the $n$-equation with $p\,n^{p-1}$, $p>1$. Using $\nabla\cdot u = 0$ and $u|_{\partial\Omega}=0$ to kill the advection term:
$$
\frac{d}{dt}\int_\Omega n^p = -p(p-1)\int_\Omega n^{p-2}|\nabla n|^2 + p(p-1)\int_\Omega n^{p-1}\nabla n\cdot\nabla c .
$$
Since $p(p-1)n^{p-1}\nabla n = (p-1)\nabla(n^p)$, integrating by parts and using $\partial_\nu c=0$:
$$
\frac{d}{dt}\int_\Omega n^p + \frac{4(p-1)}{p}\int_\Omega \big|\nabla n^{p/2}\big|^2 = -(p-1)\int_\Omega n^p\,\Delta c .
$$
Now substitute $\Delta c = c_t + u\cdot\nabla c + nc$:
$$
\frac{d}{dt}\int_\Omega n^p + \frac{4(p-1)}{p}\int_\Omega \big|\nabla n^{p/2}\big|^2 + (p-1)\underbrace{\int_\Omega n^{p+1}c}_{\ \ge 0} = -(p-1)\int_\Omega n^p\,(c_t + u\cdot\nabla c).
$$
The consumption term has a **favorable sign** — this is the structural advantage over classical Keller–Segel, where the corresponding term is $+\int n^{p+1}$ and drives blow-up.

*Why smallness works.* If $\|c_0\|_{L^\infty}$ is small, one couples this with a functional of the form $\int n^p c^{\,\theta}$; the cross terms are dominated by the two dissipation terms provided $\|c_0\|_{L^\infty}\le \frac{1}{6(d+1)}$ (Tao 2011). Then $\|n\|_{L^p}$ is bounded for every $p$, Moser iteration gives $\|n\|_{L^\infty}$, and the solution is classical and global.

*Why large data fails in 3D.* For arbitrary $c_0$ the term $\int n^p c_t$ must be absorbed. The only unconditional bound on $c_t$ comes from the entropy dissipation $\int_0^T\!\!\int c|D^2\ln c|^2 < \infty$, which controls $\nabla c$ in $L^{10/3}_{x,t}$ at best. Estimating $\int n^p |\nabla c|$-type terms by Gagliardo–Nirenberg with $v = n^{p/2}$:
$$
\int_\Omega v^{2}\,|\nabla c| \le \|v\|_{L^{4}}^{2}\|\nabla c\|_{L^2}, \qquad
\|v\|_{L^4}^2 \le C\|\nabla v\|_{L^2}^{a}\|v\|_{L^{2/p}}^{1-a}, \quad a = \frac{3}{4}\cdot\frac{?}{}
$$
In $d=2$ the exponent is $a=1$ with a **linear** appearance of $\|\nabla v\|_{L^2}^2$, absorbable by the dissipation; the argument closes and yields Winkler's 2D theorem. In $d=3$ the same interpolation forces $a = \tfrac{3}{2}\cdot\frac{p-1}{\,\cdot\,} > 1$ in the relevant range, producing $\|\nabla v\|_{L^2}^{2\sigma}$ with $\sigma>1$: Young's inequality then leaves a residual power $\big(\int n^p\big)^{\gamma}$, $\gamma>1$, and Grönwall gives only
$$
\int_\Omega n^p(\cdot,t) \le \Big[\big(\textstyle\int_\Omega n_0^p\big)^{1-\gamma} - C(\gamma-1)t\Big]^{\frac{1}{1-\gamma}},
$$
a bound that blows up at the finite time $T^* = \frac{(\int n_0^p)^{1-\gamma}}{C(\gamma-1)}$. This $T^*$ is an artifact of the method, not a proven singularity — but no technique currently removes it for large data. That single superlinear exponent is *the gap* of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*