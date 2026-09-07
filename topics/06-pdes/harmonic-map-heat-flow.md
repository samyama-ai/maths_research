---
id: 06-pdes/harmonic-map-heat-flow
title: "Harmonic Map Heat Flow"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Harmonic Map Heat Flow

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/harmonic-map-heat-flow` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M^n,g)$ and $(N^k,h)$ be smooth compact Riemannian manifolds, $N$ isometrically embedded in $\mathbb{R}^L$ by Nash. The harmonic map heat flow is the $L^2$-gradient flow of the Dirichlet energy
$$E(u)=\tfrac12\int_M |\nabla u|^2\,d\mu_g ,\qquad u:M\to N .$$
Given $u_0\in C^\infty(M,N)$, solve
$$\partial_t u=\tau(u):=\Delta_g u+A(u)(\nabla u,\nabla u),\qquad u(\cdot,0)=u_0,$$
where $A$ is the second fundamental form of $N\subset\mathbb{R}^L$.

The open problem is the **global structure theory** of this flow, in three linked parts.

- **(P1) Singularity formation.** For which $(M,N,u_0)$ does the smooth solution blow up in finite time, and at what rate? In particular: is finite-time blow-up generic in $\dim M\ge 3$, and does it occur for *some* smooth data whenever $N$ carries a non-constant harmonic sphere?
- **(P2) Uniqueness / selection.** Weak solutions in the energy class $H^1$ with $E$ non-increasing (Struwe class) are known to be non-unique in dimension $2$ once the energy inequality is relaxed, and no uniqueness class is known for $n\ge 3$. Identify the correct selection principle.
- **(P3) Asymptotics and bubbling.** Does every global flow converge (not merely subconverge along a sequence $t_j\to\infty$) to a harmonic map plus a finite bubble tree, with no energy lost in the necks?

A complete resolution means: a proof or counterexample for each of (P1)–(P3), with the singular set characterized up to a set of parabolic Hausdorff dimension $0$.

## 2. Mathematical Foundations

**Tension field.** In local coordinates $y^\alpha$ on $N$ with Christoffel symbols $\Gamma^\alpha_{\beta\gamma}$,
$$\tau(u)^\alpha=\Delta_g u^\alpha+g^{ij}\Gamma^{\alpha}_{\beta\gamma}(u)\,\partial_i u^\beta\partial_j u^\gamma .$$
Critical points $\tau(u)=0$ are **harmonic maps**. The flow satisfies the energy identity
$$E(u(T_2))+\int_{T_1}^{T_2}\!\!\int_M |\partial_t u|^2 = E(u(T_1)).$$

**Scaling.** The equation is invariant under $u_\lambda(x,t)=u(\lambda x,\lambda^2 t)$, under which $\int|\nabla u|^2$ scales like $\lambda^{2-n}$: the flow is **energy-critical in $n=2$** and supercritical for $n\ge3$.

**Bochner formula.** With $\mathrm{Rm}^N\le 0$,
$$\left(\partial_t-\Delta\right)|\nabla u|^2=-2|\nabla^2u|^2-2\langle \mathrm{Rm}^N(\partial_iu,\partial_ju)\partial_ju,\partial_iu\rangle+2\,\mathrm{Ric}^M(\nabla u,\nabla u),$$
so nonpositive target curvature makes the reaction term favorable — the source of Eells–Sampson.

**Monotonicity (Struwe 1988).** With backward heat kernel $G_{(x_0,t_0)}$,
$$\Phi(t)=(t_0-t)\int_M |\nabla u|^2 G_{(x_0,t_0)}\,\eta^2\,d\mu$$
is almost monotone; combined with an $\varepsilon$-regularity theorem
$$\sup_{P_r}|\nabla u|\le C/r \quad\text{whenever}\quad r^{2-n}\!\!\int_{P_{2r}}|\nabla u|^2<\varepsilon_0,$$
this yields partial regularity.

**Blow-up limits.** Rescaling at a singular point $(x_0,T)$ by $\lambda_j\to0$ produces either a nonconstant **harmonic sphere** $\omega:S^2\to N$ (in $n=2$) or a **quasi-harmonic sphere** / self-shrinker $u:\mathbb{R}^n\to N$ solving $\tau(u)+\tfrac12 x\cdot\nabla u=0$ with finite weighted energy (in $n\ge3$).

**Bubble tree.** At a singular time $T$, one expects
$$E(u(T^-))=E(u(T))+\sum_{i=1}^{m}E(\omega_i),$$
the **energy identity**, plus **no-neck**: the images $u(t)$ converge in $C^0$ so the body map and bubbles join continuously.

## 3. History & State of the Art

- **1964.** Eells and Sampson introduce the flow to produce harmonic maps in a homotopy class; they prove global existence and smooth convergence when $\mathrm{sec}^N\le 0$ — the origin of geometric heat flows and a direct ancestor of Ricci flow.
- **1975–85.** Hamilton's boundary-value extension; Hildebrandt–Kaul–Widman's small-image regularity.
- **1985.** Struwe: for $\dim M=2$, a global weak solution exists, unique in the class of non-increasing energy, smooth away from finitely many space-time points; blow-up points carry harmonic spheres.
- **1988–89.** Struwe (higher dimensions) and Chen–Struwe: global weak solutions with singular set of parabolic Hausdorff dimension $\le n-2$.
- **1989–92.** Coron–Ghidaglia produce finite-time blow-up for $n\ge3$; Chang–Ding–Ye produce the first blow-up in the critical dimension $n=2$, for equivariant maps $D^2\to S^2$.
- **1995–97.** Freire proves uniqueness in the energy class for $n=2$; Ding–Tian and Qing–Tian establish energy identity and no-neck for approximate harmonic maps from surfaces.
- **2002–04.** Topping ("reverse bubbling") and Bertsch–Dal Passo–van der Hout construct non-unique weak solutions in $n=2$ that gain energy; Topping's *Annals* paper gives quantization and asymptotic control for almost-harmonic maps.
- **2013–2020.** Raphaël–Schweyer give a stable blow-up rate for $1$-corotational flow; Dávila–del Pino–Wei construct blow-up for the $2$D flow into $S^2$ by inner–outer gluing, with prescribed points and rates.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $\mathrm{sec}^N\le0$, any $n$ | Global smooth existence; $u(t)\to$ harmonic map (Eells–Sampson 1964). |
| $u_0(M)\subset$ geodesic ball of radius $<\pi/(2\sqrt{\kappa})$, $\mathrm{sec}^N\le\kappa$ | Global smooth existence, convex-ball barrier (Hildebrandt–Kaul–Widman). |
| $n=2$, any $N$ | Global weak solution, at most finitely many singularities, unique in energy class (Struwe 1985; Freire 1995). |
| $n=2$, $\pi_2(N)=0$ | No finite-time singularity; flow is smooth for all time and converges to a harmonic map in the homotopy class of $u_0$. |
| $n=2$, $E(u_0)<\varepsilon_0$ or $E(u_0)<$ least harmonic-sphere energy | Global smoothness. |
| $n=2$, $M=D^2$, $N=S^2$, equivariant degree $\ge1$, boundary data forcing degree | Finite-time blow-up (Chang–Ding–Ye 1992); rate $\lambda(t)\sim \kappa(T-t)/|\log(T-t)|^2$ for corotational index $k=1$ (Raphaël–Schweyer 2013), $\lambda(t)\sim c(T-t)^{k/(k-1)}$-type laws for $k\ge2$. |
| $n\ge3$, symmetric data | Finite-time blow-up (Coron–Ghidaglia 1989); explicit example $u_0(x)=x/|x|$-type for $M=B^3$, $N=S^3$. |
| $n\ge3$, general | Global weak (Chen–Struwe) solution; $\dim_{\mathcal P}\Sigma\le n-2$; $\Sigma$ closed. |
| $\|\nabla u_0\|_{L^n}$ or $\|u_0\|_{\mathrm{BMO}}$ small | Local well-posedness and uniqueness for rough data (Koch–Lamm 2012; C. Wang 2011). |
| $n=2$, global flows | Energy identity and no-neck at finite singular times (Ding–Tian 1995; Qing–Tian 1997); asymptotic quantization at $t\to\infty$ under curvature/analyticity conditions (Topping 2004). |

## 5. Principal Obstacles

- **Supercriticality for $n\ge3$.** No conserved or monotone quantity controls the critical norm $\|\nabla u\|_{L^n}$. Struwe's monotonicity gives only $r^{2-n}\int|\nabla u|^2$, which is scale-invariant but not coercive enough for uniqueness; parabolic Schauder theory needs $L^\infty$ control of $\nabla u$ that no a priori estimate supplies.
- **Quasi-harmonic spheres are not classified.** Blow-up limits in $n\ge3$ are self-shrinkers on $\mathbb{R}^n$ with Gaussian-weighted energy. Lin–Wang showed there is no nonconstant quasi-harmonic sphere with image in a hemisphere, but no general classification exists, so one cannot rule out singularity models by geometry of $N$ alone.
- **Loss of the conformal structure.** In $n=2$ the analysis leans on conformal invariance of $E$, Wente-type compensated compactness, and Rivière's antisymmetric-potential trick. Both mechanisms vanish for $n\ge3$; Rivière's counterexample of everywhere-discontinuous weakly harmonic maps into $S^2$ shows the weak-solution class is genuinely wild without an energy monotonicity constraint.
- **Non-uniqueness is real, not technical.** Topping's reverse bubbling shows a bubble can be *reattached*, producing weak solutions with jumping energy. So (P2) is not a regularity problem but a question of which extra condition (energy decay, monotonicity, Struwe class, entropy) picks the geometric flow.
- **Neck analysis at infinite time.** Energy identity as $t\to\infty$ requires uniform control over necks of unbounded length; without a Łojasiewicz–Simon inequality (which needs analyticity of $N$ and a nondegenerate limit) the flow can in principle oscillate among distinct harmonic maps.

## 6. The Gap

Proven: dimension $2$ is essentially complete (existence, finite singular set, energy identity, no-neck, uniqueness in Struwe class), and dimension $\ge3$ has weak solutions with $\dim_{\mathcal P}\Sigma\le n-2$ plus isolated symmetric blow-up examples.

Not proven, and the exact barriers:

1. **From $\dim_{\mathcal P}\Sigma\le n-2$ to $\le n-4$ (or rectifiability).** This requires ruling out or classifying quasi-harmonic spheres in $\mathbb{R}^n$ — an entire-solution Liouville theorem that is currently out of reach without symmetry.
2. **From "some symmetric data blow up" to "generic data blow up."** Existing constructions are equivariant or gluing-based with hand-built profiles; no variational or degree-theoretic criterion converts topology of $N$ into blow-up for open sets of data in $n\ge3$.
3. **From uniqueness in $n=2$ to a selection principle in $n\ge3$.** Freire's proof uses the Hardy-space/BMO duality specific to two dimensions; there is no substitute in higher dimension, and no example is known distinguishing candidate classes.

## 7. Current Research (as of June 2026)

- **Gluing methods.** The inner–outer parabolic gluing scheme of Dávila, del Pino and Wei is being pushed to non-symmetric data, multi-bubble configurations, and to $n\ge3$ where the profile is a scaled harmonic $S^2\hookrightarrow N$; groups at UBC, Bath and the Chinese Academy of Sciences are active. Reported extensions to prescribed *bubble-tree* blow-up in $n=2$ with continuum-many rates remain to be fully refereed *(frontier — verify)*.
- **Sharp blow-up rates and stability.** Following Raphaël–Schweyer, modulation analysis is being used to decide whether the $k=1$ log-rate is the only stable one and whether $k\ge2$ rates are unstable of finite codimension.
- **Rough-data well-posedness.** Continuation of Koch–Lamm and C. Wang: critical-space theory in $\mathrm{BMO}^{-1}$-type and Besov spaces, aimed at an ill-posedness/uniqueness dichotomy in $n=3$.
- **Free-boundary and nonlocal analogues.** Half-harmonic and fractional harmonic map flows (Sire–Wei–Zheng and collaborators) serve as testbeds where the critical dimension is $1$ and computations are explicit.
- **Łojasiewicz–Simon at infinite time.** Work extending Topping's quantization toward unconditional convergence of global flows on surfaces, and toward convergence rates for flows into analytic targets.

## 8. Future Work

- Prove a **Liouville theorem for quasi-harmonic spheres** into a general compact $N$ under an energy bound; this alone would improve the singular-set bound in $n\ge3$.
- Develop a **parabolic Federer dimension-reduction** for the harmonic map flow paralleling the elliptic theory of Simon and of Lin, to obtain rectifiability of $\Sigma$.
- Identify an **entropy** (Colding–Minicozzi style, from the Struwe monotone quantity) whose monotonicity is strict enough to force uniqueness of the flow past singularities.
- Construct **non-symmetric finite-time blow-up in $n=3$** by gluing, deciding whether the low-dimensional intuition ($\pi_2(N)\ne0$ forces blow-up) survives supercriticality.
- Settle whether every global $2$D flow converges as $t\to\infty$ **without** assuming analyticity of $N$.

## 9. Key References

- **[Foundational]** J. Eells and J. H. Sampson. *Harmonic mappings of Riemannian manifolds.* American Journal of Mathematics 86 (1964), 109–160.
- **[Foundational]** M. Struwe. *On the evolution of harmonic mappings of Riemannian surfaces.* Commentarii Mathematici Helvetici 60 (1985), 558–581.
- **[Foundational]** M. Struwe. *On the evolution of harmonic maps in higher dimensions.* Journal of Differential Geometry 28 (1988), 485–502.
- **[Foundational]** Y. Chen and M. Struwe. *Existence and partial regularity results for the heat flow for harmonic maps.* Mathematische Zeitschrift 201 (1989), 83–103.
- **[Blow-up]** J.-M. Coron and J.-M. Ghidaglia. *Explosion en temps fini pour le flot des applications harmoniques.* C. R. Acad. Sci. Paris Sér. I 308 (1989), 339–344.
- **[Blow-up]** K.-C. Chang, W.-Y. Ding and R. Ye. *Finite-time blow-up of the heat flow of harmonic maps from surfaces.* Journal of Differential Geometry 36 (1992), 507–515.
- **[Bubbling]** W. Ding and G. Tian. *Energy identity for a class of approximate harmonic maps from surfaces.* Communications in Analysis and Geometry 3 (1995), 543–554.
- **[Bubbling]** J. Qing and G. Tian. *On the removability of necks in the harmonic map flow.* Communications on Pure and Applied Mathematics 50 (1997), 295–310.
- **[Uniqueness]** A. Freire. *Uniqueness for the harmonic map flow in two dimensions.* Calculus of Variations and PDE 3 (1995), 95–105.
- **[Non-uniqueness]** P. Topping. *Reverse bubbling and nonuniqueness in the harmonic map flow.* International Mathematics Research Notices 2002, no. 10, 505–520.
- **[Non-uniqueness]** M. Bertsch, R. Dal Passo and R. van der Hout. *Nonuniqueness for the heat flow of harmonic maps on the disk.* Archive for Rational Mechanics and Analysis 161 (2002), 93–112.
- **[SOTA]** P. Topping. *Repulsion and quantization in almost-harmonic maps, and asymptotics of the harmonic map flow.* Annals of Mathematics 159 (2004), 465–534.
- **[SOTA]** P. Raphaël and R. Schweyer. *Stable blowup dynamics for the 1-corotational energy critical harmonic heat flow.* Communications on Pure and Applied Mathematics 66 (2013), 414–480.
- **[SOTA]** J. Dávila, M. del Pino and J. Wei. *Singularity formation for the two-dimensional harmonic map flow into $S^2$.* Inventiones Mathematicae 219 (2020), 345–466.
- **[Rates]** S. Angenent, J. Hulshof and H. Matano. *The radius of vanishing bubbles in equivariant harmonic map flow from $D^2$ to $S^2$.* SIAM Journal on Mathematical Analysis 41 (2009), 1121–1137.
- **[Rough data]** H. Koch and T. Lamm. *Geometric flows with rough initial data.* Asian Journal of Mathematics 16 (2012), 209–235.
- **[Rough data]** C. Wang. *Well-posedness for the heat flow of harmonic maps and the liquid crystal flow with rough initial data.* Archive for Rational Mechanics and Analysis 200 (2011), 1–19.
- **[Elliptic counterpart]** T. Rivière. *Everywhere discontinuous harmonic maps into spheres.* Acta Mathematica 175 (1995), 197–226.
- **[Survey / Book]** F. Lin and C. Wang. *The Analysis of Harmonic Maps and Their Heat Flows.* World Scientific, 2008.
- **[Survey / Book]** F. Hélein. *Harmonic Maps, Conservation Laws and Moving Frames.* 2nd ed., Cambridge University Press, 2002.

## 10. Worked Example / Concrete Special Case

**Corotational flow $D^2\to S^2$.** Write $x=re^{i\theta}\in D^2$ and use the ansatz
$$u(r,\theta,t)=\big(\sin\varphi(r,t)\cos\theta,\ \sin\varphi(r,t)\sin\theta,\ \cos\varphi(r,t)\big)\in S^2 .$$
Substituting into $\partial_t u=\Delta u+|\nabla u|^2u$ reduces the system to a scalar equation:
$$\varphi_t=\varphi_{rr}+\frac{\varphi_r}{r}-\frac{\sin 2\varphi}{2r^2},\qquad \varphi(0,t)=0 .$$

**Energy.** For this ansatz
$$E(u)=\pi\int_0^1\Big(\varphi_r^2+\frac{\sin^2\varphi}{r^2}\Big)r\,dr .$$
Complete the square (Bogomolny trick):
$$E(u)=\pi\int_0^1\Big(\varphi_r-\frac{\sin\varphi}{r}\Big)^2 r\,dr+2\pi\int_0^1 \sin\varphi\,\varphi_r\,dr .$$
The last term equals $2\pi\big[-\cos\varphi\big]_0^1$, a topological quantity. If $\varphi$ runs from $0$ to $\pi$ the second term is $4\pi$, so
$$E(u)\ \ge\ 4\pi,$$
with equality exactly when $\varphi_r=\sin\varphi/r$, i.e. $\varphi(r)=2\arctan(r/\lambda)$ — the degree-one harmonic sphere, of energy exactly $4\pi$, at any scale $\lambda>0$. **The scale is a free parameter: this is the noncompact family that drives blow-up.**

**Blow-up.** Impose the boundary condition $\varphi(1,t)=\varphi_1$ with $\pi<\varphi_1<\ldots$, and take $\varphi(r,0)$ monotone with $\varphi(r,0)>\pi$ somewhere. Chang–Ding–Ye show that the maximum principle forces $\varphi(r,t)$ to keep exceeding $\pi$ at interior points while the energy budget forbids a smooth degree-shifting limit; hence there is $T<\infty$ with $\sup_r|\varphi_r(r,t)|\to\infty$ as $t\to T$. Near $T$ the solution looks like the bubble
$$\varphi(r,t)\approx 2\arctan\!\big(r/\lambda(t)\big)+\text{(smooth body map)},$$
and by Raphaël–Schweyer, for the stable regime,
$$\lambda(t)=\kappa(u_0)\,\frac{T-t}{|\log(T-t)|^2}\,\big(1+o(1)\big),\qquad t\to T^- .$$
Energy is quantized: $E(u(T^-))-E(u(T))=4\pi$, exactly one bubble.

**What is open even here.** For non-corotational perturbations of this very datum it is not known whether the same $4\pi$ single-bubble scenario is stable in the full (non-symmetric) topology; and the analogous construction in $M=B^3$ has no known energy-quantization statement, because the blow-up limit is a quasi-harmonic sphere, not a harmonic sphere.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*