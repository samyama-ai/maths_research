---
id: 06-pdes/helmholtz-high-frequency-resolvent
title: "High Frequency Helmholtz Resolvent Estimates"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# High Frequency Helmholtz Resolvent Estimates

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/helmholtz-high-frequency-resolvent` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $R(k)$ be the outgoing resolvent of a self-adjoint Helmholtz operator at frequency $k>0$ — for the free exterior problem, $R(k) = (-\Delta - k^2)^{-1}$ with the Sommerfeld radiation condition. The central question is:

> **Given the geometry (obstacle shape, boundary condition, coefficient regularity), what is the sharp rate of growth of $\|\chi R(k)\chi\|_{L^2 \to L^2}$ as $k \to \infty$, for $\chi \in C_c^\infty(\mathbb{R}^d)$?**

Three sub-problems are open in distinct regimes.

1. **Rough coefficients.** For the variable-coefficient operator $-\nabla\cdot(A\nabla\,\cdot) - k^2 n$ with $A \in L^\infty(\mathbb{R}^d;\mathbb{R}^{d\times d}_{\mathrm{sym}})$ uniformly elliptic and $n \in L^\infty$ bounded below, is there *any* a priori bound $\|\chi R(k)\chi\| \le F(k)$ with $F$ locally bounded? No such bound is known below $C^{0,1}$ regularity of $A$.
2. **Sharpness of the exponential.** For smooth trapping geometries the universal upper bound is $\|\chi R(k)\chi\| \le e^{Ck}$. Characterise geometrically the exact exponential rate, and decide whether the exponential is attained for *nonpenetrable* (Dirichlet/Neumann) obstacles as it is for penetrable ones.
3. **Generic frequencies.** Is the resolvent polynomially bounded for all $k$ outside a set of *finite* (rather than merely small) measure, and can the exceptional set be described spectrally?

A complete resolution of any sub-problem requires either a proof valid for the whole stated class, or an explicit geometry/coefficient realising the claimed lower bound with matching $k$-dependence.

## 2. Mathematical Foundations

Let $\Omega_- \subset \mathbb{R}^d$ ($d \ge 2$) be a bounded Lipschitz obstacle, $\Omega_+ = \mathbb{R}^d \setminus \overline{\Omega_-}$. The **exterior Dirichlet Helmholtz problem** is: given $f$, find $u$ with
$$\Delta u + k^2 u = -f \ \text{in } \Omega_+, \qquad u = 0 \ \text{on } \partial\Omega_-, \qquad \lim_{r\to\infty} r^{\frac{d-1}{2}}\!\left(\partial_r u - i k u\right) = 0 .$$
Write $R(k)f = u$. By the limiting absorption principle $R(k) = \lim_{\varepsilon \downarrow 0}(-\Delta - (k+i\varepsilon)^2)^{-1}$, and $\chi R(k)\chi$ continues meromorphically from $\{\operatorname{Im} k > 0\}$ to $\mathbb{C}$ ($d$ odd) or the logarithmic cover ($d$ even); poles are **resonances**.

**Semiclassical form.** Put $h = k^{-1}$, $P = -h^2\Delta$. Then $\chi R(k)\chi = h^{2}\,\chi(P - 1 - i0)^{-1}\chi$, and a bound $\|\chi R(k)\chi\|_{L^2\to L^2} \le C k^{-1}$ is equivalent to the semiclassical estimate $\|\chi (P-1-i0)^{-1}\chi\| \le C h^{-1}$.

**Trapping.** Let $\Phi_t$ denote the generalised bicharacteristic flow of $P$ on $T^*\Omega_+$ (Melrose–Sjöstrand, allowing glancing and reflection). The **trapped set** is
$$K = \{(x,\xi) \in S^*\Omega_+ : \Phi_t(x,\xi) \not\to \infty \ \text{as } t \to \pm\infty\}.$$
The geometry is **nontrapping** if $K = \emptyset$. The three canonical regimes:

$$\|\chi R(k)\chi\|_{L^2\to L^2} \;\lesssim\;
\begin{cases}
k^{-1}, & K = \emptyset \quad \text{(nontrapping)},\\[2pt]
k^{-1}\log k, & K \ \text{hyperbolic, thin (pressure } P(1/2)<0),\\[2pt]
e^{Ck}, & \text{general smooth geometry}.
\end{cases}$$

The lower barrier is universal: $\|\chi R(k)\chi\| \ge c\,k^{-1}$ for all geometries, since the free resolvent already saturates $k^{-1}$.

**Quasimode–resonance duality.** If there exist $u_j$, $\|u_j\|=1$, supported in a fixed compact set, with $\|(\Delta + k_j^2)u_j\| \le \varepsilon(k_j)$, then $\|\chi R(k)\chi\| \gtrsim \varepsilon(k)^{-1}$ for $k$ in intervals near $k_j$ (Tang–Zworski, Stefanov). Exponentially accurate quasimodes therefore force exponentially large resolvents.

**Variable coefficients.** For $\mathcal{L}u = \nabla\cdot(A\nabla u) + k^2 n u$, the Morawetz/Rellich multiplier $\overline{x\cdot\nabla u} + \alpha \bar u$ yields $\|\chi R(k)\chi\|\lesssim k^{-1}$ under the *nontrapping-by-monotonicity* conditions
$$x\cdot\nabla n(x) \le 0, \qquad \partial_r\!\left(r\,\text{-radial part of } A\right) \preceq 0 \ \text{(matrix sense)},$$
holding a.e. — no smoothness required beyond $A \in C^{0,1}$ for the well-posedness theory.

## 3. History & State of the Art (SOTA)

- **1962–1975.** Morawetz introduced the multiplier identities giving local energy decay for star-shaped obstacles; Morawetz–Ludwig (1968) and Morawetz–Ralston–Strauss (1977) extended this to nontrapping obstacles.
- **1975.** Vainberg linked local energy decay, resonance-free strips, and short-wave asymptotics, establishing $O(k^{-1})$ in the nontrapping case (with Melrose–Sjöstrand propagation of singularities, 1978, supplying the glancing analysis).
- **1998.** Burq proved the universal exponential bound $\|\chi R(k)\chi\|\le e^{Ck}$ for *any* smooth obstacle with no geometric hypothesis, via Carleman estimates and unique continuation — the single most important structural result.
- **2002.** Cardoso–Vodev generalised the exponential bound to a broad class of infinite-volume manifolds and exteriors of large balls.
- **1999–2004.** Popov–Vodev, and Cardoso–Popov–Vodev, constructed transmission problems with resonances at exponentially small distance from the real axis, showing the $e^{Ck}$ bound is **sharp** for penetrable obstacles.
- **2009.** Nonnenmacher–Zworski proved the fractal-uncertainty-free pressure criterion $P(1/2)<0 \Rightarrow$ resonance-free strip $\Rightarrow \|\chi R\chi\|\lesssim k^{-1}\log k$; Christianson had earlier obtained the same for a single hyperbolic orbit, Burq–Guillarmou–Hassell for hyperbolic trapped sets with applications to Strichartz estimates.
- **2012.** Datchev–Vasy's *gluing* technique reduced the global estimate to a black-box estimate near $K$ plus a nontrapping estimate away from it, making the $\log$-loss regime modular.
- **2014–2020.** Spence, Baskin–Spence–Wunsch, Graham–Pembery–Spence, and Galkowski–Spence–Wunsch made all constants **wavenumber- and geometry-explicit**, driven by numerical analysis of the Helmholtz FEM/BEM where the resolvent norm is exactly the stability constant.
- **2021.** Lafontaine–Spence–Wunsch: even with strong (elliptic, stable) trapping, for all $k$ outside a set of arbitrarily small measure, the resolvent is polynomially bounded.

## 4. Partial Results / Verified Cases

| Class | Bound | Source |
|---|---|---|
| Star-shaped Lipschitz obstacle, Dirichlet | $\|\chi R\chi\| \le C\,\mathrm{diam}(\Omega_-)\,k^{-1}$, explicit $C$ | Morawetz; Chandler-Wilde–Monk (2008) |
| Smooth nontrapping obstacle, $d\ge 2$, Dirichlet/Neumann/impedance | $\lesssim k^{-1}$, sharp | Vainberg (1975); Melrose–Sjöstrand |
| Nontrapping, explicit constant | $\|\chi R\chi\|\le C k^{-1}$ with $C$ expressed via the maximal escape time on $\operatorname{supp}\chi$ | Galkowski–Spence–Wunsch (2020) |
| Hyperbolic trapped set, $P(1/2)<0$ | $\lesssim k^{-1}\log k$; includes several convex obstacles satisfying Ikawa's condition | Nonnenmacher–Zworski (2009) |
| One hyperbolic closed geodesic | $\lesssim k^{-1}\log k$, sharp | Christianson (2007); Burq–Guillarmou–Hassell (2010) |
| $A \in C^{0,1}$, $n\in L^\infty$, radial monotonicity | $\lesssim k^{-1}$ | Graham–Pembery–Spence (2019) |
| Any smooth compactly supported perturbation | $\le e^{Ck}$ | Burq (1998); Cardoso–Vodev (2002) |
| Penetrable trapping obstacle (e.g. ball with $n>1$ inside) | $\ge e^{ck}$ along a sequence $k_j\to\infty$ | Popov–Vodev (1999); Cardoso–Popov–Vodev (2004) |
| Strong (elliptic) trapping, $k \notin J$, $|J|<\varepsilon$ | polynomial in $k$ | Lafontaine–Spence–Wunsch (2021) |
| $d=1$, any $L^\infty$ coefficients | $\lesssim k^{-1}$ | elementary ODE/transfer-matrix argument |

## 5. Principal Obstacles

- **Unique continuation fails below Lipschitz.** Burq's $e^{Ck}$ bound rests on Carleman estimates, which need $A \in C^{0,1}$ (or Hölder with structure). Pliś-type counterexamples give elliptic operators with Hölder coefficients admitting compactly supported nontrivial solutions, so no Carleman route exists for $A\in L^\infty$ — and no substitute is known. This is the reason sub-problem 1 is completely open.
- **No propagation of singularities without smoothness.** The nontrapping $k^{-1}$ estimate is proved by microlocal propagation along bicharacteristics; for $L^\infty$ coefficients the Hamilton flow is not even defined, so "nontrapping" has no intrinsic meaning. Multiplier (Morawetz) methods survive, but they only ever certify *star-shaped-like* monotone geometries, not general nontrapping ones.
- **Multipliers cannot see trapping.** Rellich/Morawetz identities produce a positive-definite bulk term only under sign conditions; there is no known multiplier producing a $\log k$ loss, so the hyperbolic-trapping results are inaccessible to real-variable methods and require full semiclassical machinery.
- **Interpolating between $\log$ and exponential is unmapped.** Between thin hyperbolic trapping ($k^{-1}\log k$) and stable elliptic trapping ($e^{ck}$) lie mixed and parabolic trapped sets where no general theorem exists; the pressure condition $P(1/2)<0$ is a scalar summary that discards essential geometry.
- **Lower bounds are hard to produce.** Quasimode constructions need a stable invariant structure (elliptic island, total internal reflection). For Dirichlet obstacles with trapping but no such island, neither an improved upper bound nor a matching lower bound is available.

## 6. The Gap

The proven ceiling and the conjectural truth diverge at three explicit points.

1. **Regularity threshold.** Proven: $A\in C^{0,1}\Rightarrow \|\chi R\chi\|\le e^{Ck}$. Unknown: $A\in C^{0,\alpha}$ for $\alpha<1$, or $A\in L^\infty$. The crossing step is a unique-continuation or Carleman inequality — or a counterexample — at sub-Lipschitz regularity.
2. **Obstacle trapping.** Proven: $e^{Ck}$ upper, $e^{ck}$ lower for *penetrable* media. Unknown: whether any impenetrable obstacle in $\mathbb{R}^d$ forces exponential growth. The crossing step is either an exponentially accurate quasimode for a Dirichlet geometry, or a proof that boundary-trapped rays always leak at a polynomial rate.
3. **Generic frequency sets.** Proven: exceptional set of arbitrarily small measure. Unknown: finite measure, or a description of the exceptional set as a neighbourhood of resonance real parts with quantitative width.

## 7. Current Research (as of June 2026)

- **Bath / UCL / Northwestern axis** (Spence, Galkowski, Wunsch, Lafontaine): wavenumber-explicit constants feeding numerical analysis. The line "does the $hp$-FEM with PML truncation suffer from the pollution effect?" is settled negatively for nontrapping media, with the resolvent bound as the sole analytic input. *(frontier — verify)* Extensions to $L^\infty$ media using only Morawetz identities and no unique continuation are under active development.
- **Semiclassical school** (Zworski, Dyatlov, Datchev, Christianson): fractal uncertainty principles now give resonance-free strips in cases where the pressure condition fails, notably for hyperbolic surfaces and open quantum maps; transferring these gains to Euclidean obstacle scattering is the stated target.
- **Random/UQ Helmholtz** (Graham, Pembery, Sloan): resolvent bounds uniform over random coefficient fields, where realisations are only $L^\infty$ almost surely — this is the applied driver of sub-problem 1.
- **Transmission and metamaterials** (Vodev, Moiola, Cassier): sharp resonance widths for penetrable obstacles with contrast, including sign-changing coefficients where ellipticity itself degenerates.

## 8. Future Work

- Prove a **Morawetz-only** nontrapping theorem: identify the largest class of $L^\infty$ coefficients for which a $k^{-1}$ bound follows from a multiplier identity, without Carleman estimates.
- Establish or refute a **Dirichlet exponential lower bound** by constructing quasimodes concentrated on a stable trapped ray in an obstacle exterior (elliptic cavity candidates are numerically suggestive but not proved).
- Replace the pressure condition by a **fractal-uncertainty criterion** for Euclidean obstacle trapped sets, targeting $k^{-1}\log k$ under weaker thinness hypotheses.
- Quantify the exceptional set in the "most frequencies" theorem: show $|J\cap[k,2k]|\to 0$ with an explicit rate tied to resonance counting.
- Develop **$k$-explicit bounds in $H^1$ and $L^\infty$ norms**, not just $L^2$, since finite-element error analysis needs the former and scattering asymptotics the latter.

## 9. Key References

- **[Foundational]** C. S. Morawetz. *Decay for solutions of the exterior problem for the wave equation.* Communications on Pure and Applied Mathematics 28 (1975), 229–264.
- **[Foundational]** B. R. Vainberg. *On the short wave asymptotic behaviour of solutions of stationary problems and the asymptotic behaviour as $t\to\infty$ of solutions of non-stationary problems.* Russian Mathematical Surveys 30 (1975), 1–58.
- **[Foundational]** R. B. Melrose, J. Sjöstrand. *Singularities of boundary value problems I.* Communications on Pure and Applied Mathematics 31 (1978), 593–617.
- **[Foundational]** N. Burq. *Décroissance de l'énergie locale de l'équation des ondes pour le problème extérieur et absence de résonance au voisinage du réel.* Acta Mathematica 180 (1998), 1–29.
- **[SOTA]** F. Cardoso, G. Vodev. *Uniform estimates of the resolvent of the Laplace–Beltrami operator on infinite volume Riemannian manifolds II.* Annales Henri Poincaré 3 (2002), 673–691.
- **[SOTA]** S. Nonnenmacher, M. Zworski. *Quantum decay rates in chaotic scattering.* Acta Mathematica 203 (2009), 149–233.
- **[SOTA]** N. Burq, C. Guillarmou, A. Hassell. *Strichartz estimates without loss on manifolds with hyperbolic trapped geodesics.* Geometric and Functional Analysis 20 (2010), 627–656.
- **[SOTA]** K. Datchev, A. Vasy. *Gluing semiclassical resolvent estimates via propagation of singularities.* International Mathematics Research Notices 2012, 5409–5443.
- **[SOTA]** D. Baskin, E. A. Spence, J. Wunsch. *Sharp high-frequency estimates for the Helmholtz equation and applications to boundary integral equations.* SIAM Journal on Mathematical Analysis 48 (2016), 229–267.
- **[SOTA]** I. G. Graham, O. R. Pembery, E. A. Spence. *The Helmholtz equation in heterogeneous media: a priori bounds, well-posedness, and resonances.* Journal of Differential Equations 266 (2019), 2869–2923.
- **[SOTA]** J. Galkowski, E. A. Spence, J. Wunsch. *Optimal constants in nontrapping resolvent estimates and applications in numerical analysis.* Pure and Applied Analysis 2 (2020), 157–202.
- **[SOTA]** D. Lafontaine, E. A. Spence, J. Wunsch. *For most frequencies, strong trapping has a weak effect in frequency-domain scattering.* Communications on Pure and Applied Mathematics 74 (2021), 2025–2063.
- **[Lower bounds]** G. Popov, G. Vodev. *Resonances near the real axis for transparent obstacles.* Communications in Mathematical Physics 207 (1999), 411–438.
- **[Survey]** E. A. Spence. *Wavenumber-explicit bounds in time-harmonic acoustic scattering.* SIAM Journal on Mathematical Analysis 46 (2014), 2987–3024.
- **[Survey]** M. Zworski. *Semiclassical Analysis.* Graduate Studies in Mathematics 138, American Mathematical Society, 2012.

## 10. Worked Example / Concrete Special Case

**Claim.** Let $\Omega_-\subset\mathbb{R}^d$ be star-shaped with respect to $0$, and let $u$ solve $\Delta u + k^2 u = -f$ in $\Omega_+$, $u=0$ on $\partial\Omega_-$, outgoing, with $f$ supported in $B_R$. Then $k\|u\|_{L^2(\Omega_+\cap B_R)} \le C R\,\|f\|_{L^2}$, i.e. $\|\chi R(k)\chi\|\lesssim R\,k^{-1}$.

**Derivation (Rellich–Morawetz multiplier).** Test the equation against $\mathcal{M}u := x\cdot\nabla \bar u + \tfrac{d-1}{2}\bar u$ and take real parts. Two exact identities drive everything. For any $v \in H^2$,
$$2\operatorname{Re}\big(\Delta v,\; x\cdot\nabla v\big) = \nabla\cdot\Big( 2\operatorname{Re}\big[(x\cdot\nabla \bar v)\nabla v\big] - x|\nabla v|^2 \Big) + (d-2)|\nabla v|^2,$$
$$2\operatorname{Re}\big(k^2 v,\; x\cdot\nabla \bar v\big) = \nabla\cdot\big(k^2 x |v|^2\big) - d\,k^2|v|^2 .$$
Adding $(d-1)\operatorname{Re}\big((\Delta v + k^2 v)\bar v\big)$ cancels the unwanted $(d-2)|\nabla v|^2$ and $-d k^2|v|^2$ terms against $-(d-1)|\nabla v|^2 + (d-1)k^2|v|^2$, leaving on $B_R\cap\Omega_+$
$$2\operatorname{Re}\!\int (\Delta u + k^2u)\,\overline{\mathcal{M}u} \;=\; \int_{\partial(B_R\cap\Omega_+)}\!\!\Big[2\operatorname{Re}\big((x\cdot\nabla\bar u)\partial_\nu u\big) - (x\cdot\nu)\big(|\nabla u|^2 - k^2|u|^2\big) + (d-1)\operatorname{Re}(\bar u\,\partial_\nu u)\Big].$$

**Boundary contributions.**
- On $\partial\Omega_-$: since $u=0$ there, $\nabla u = (\partial_\nu u)\nu$, and the bracket collapses to $-(x\cdot\nu)|\partial_\nu u|^2$. With the outward normal of $\Omega_+$ pointing *into* $\Omega_-$, star-shapedness gives $x\cdot\nu \le 0$ on that surface, so this term has a **favourable sign** and can be discarded.
- On $\partial B_R$: $x\cdot\nu = R$, and the outgoing condition plus a standard Rellich argument bounds these terms by $C R \|f\|\,(\|\nabla u\| + k\|u\|)$ with no loss in $k$.

**Conclusion.** The left-hand side is $-2\operatorname{Re}\int f\,\overline{\mathcal{M}u}$, bounded by $2\|f\|\big(R\|\nabla u\| + \tfrac{d-1}{2}\|u\|\big)$. Combining with the elementary identity $\|\nabla u\|^2 - k^2\|u\|^2 = \operatorname{Re}\int f\bar u$ and absorbing, one obtains
$$\|\nabla u\|_{L^2(B_R\cap\Omega_+)}^2 + k^2\|u\|^2_{L^2(B_R\cap\Omega_+)} \;\le\; C\,R^2\,\|f\|^2_{L^2},$$
so $\|u\| \le C R k^{-1}\|f\|$, sharp in $k$.

**Where it breaks.** The only geometric input was the pointwise sign $x\cdot\nu \le 0$. Deform $\Omega_-$ into a non-star-shaped but still nontrapping shape — a smooth crescent whose boundary has $x\cdot\nu>0$ somewhere — and the boundary term loses its sign; the identity gives nothing. The $k^{-1}$ bound remains true, but only via Melrose–Sjöstrand propagation, which needs $C^\infty$ boundary. That gap between "sign-condition geometries provable with $L^\infty$ data" and "nontrapping geometries provable only with smooth data" is exactly sub-problem 1 of Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*