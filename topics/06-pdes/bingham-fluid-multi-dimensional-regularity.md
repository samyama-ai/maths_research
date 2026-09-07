---
id: 06-pdes/bingham-fluid-multi-dimensional-regularity
title: "Bingham Fluid Multi-Dimensional Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bingham Fluid Multi-Dimensional Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/bingham-fluid-multi-dimensional-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

A Bingham fluid is an incompressible viscoplastic medium that behaves as a rigid body where the stress deviator stays below a yield threshold $\tau_*>0$ and as a Newtonian fluid of viscosity $\mu>0$ above it. Its motion is not a PDE in the classical sense but an evolutionary **variational inequality** with a non-differentiable, positively 1-homogeneous dissipation term $\tau_*\int|\mathbb{D}(u)|$.

**The problem.** Let $\Omega\subset\mathbb{R}^n$ be a bounded domain with smooth boundary, $n=3$, and let $u$ be a Duvaut–Lions weak solution of the unsteady Bingham system with smooth data. Decide:

1. **(Regularity)** Is $u$ locally $C^{1,\alpha}$ in space, and is the stress deviator $\mathbb{S}$ continuous, up to a set of measure zero — globally in time, without smallness assumptions?
2. **(Uniqueness)** Is the weak solution unique in $n=3$?
3. **(Free boundary)** Is the *rigid zone* $\mathcal{R}(t)=\{x:\mathbb{D}(u)(x,t)=0\}$ a set with locally finite perimeter, and is its boundary — the yield surface — rectifiable/smooth away from a small singular set?

A complete resolution proves or disproves each in $n=3$ (and $n\ge 4$) for the inertial system. Even for the **stationary** and **quasi-static** ($u\cdot\nabla u$ dropped) problems, statements (1) and (3) are open in $n=3$ beyond the partial results of Section 4. Item (1) is strictly harder than the corresponding Navier–Stokes question in one respect and easier in another: the extra $\tau_*$ term supplies $L^1$ control of $\mathbb{D}(u)$ but destroys ellipticity of the leading operator where $\mathbb{D}(u)=0$.

## 2. Mathematical Foundations

**Constitutive law.** Write $\mathbb{D}(u)=\tfrac12(\nabla u+\nabla u^{\mathsf T})$, and let $\mathbb{T}=-p\,\mathbb{I}+\mathbb{S}$ be the Cauchy stress with $\operatorname{tr}\mathbb{S}=0$. The Bingham–von Mises law is the multivalued relation

$$
\mathbb{S}=2\mu\,\mathbb{D}(u)+\tau_*\frac{\mathbb{D}(u)}{|\mathbb{D}(u)|}\ \ \text{if }\mathbb{D}(u)\neq0,
\qquad
|\mathbb{S}|\le\tau_*\ \ \text{if }\mathbb{D}(u)=0,
$$

with $|A|=(A:A)^{1/2}$. Equivalently $\mathbb{S}\in 2\mu\mathbb{D}(u)+\tau_*\,\partial|\cdot|(\mathbb{D}(u))$, where $\partial$ is the convex subdifferential.

**Balance laws.** On $\Omega\times(0,T)$,
$$
\partial_t u+(u\cdot\nabla)u=\operatorname{div}\mathbb{S}-\nabla p+f,\qquad \operatorname{div}u=0,\qquad u|_{\partial\Omega}=0,\ u(\cdot,0)=u_0 .
$$

**Variational inequality (Duvaut–Lions).** Set $V=\{v\in W^{1,2}_0(\Omega;\mathbb{R}^n):\operatorname{div}v=0\}$, $H=\overline{V}^{L^2}$, and
$$
a(u,v)=2\mu\!\int_\Omega \mathbb{D}(u):\mathbb{D}(v)\,dx,\qquad
j(v)=\tau_*\!\int_\Omega|\mathbb{D}(v)|\,dx .
$$
$j$ is convex, Lipschitz on $V$, but **not** Gâteaux differentiable at $v$ with $\mathbb{D}(v)$ vanishing on a positive-measure set. A weak solution is $u\in L^\infty(0,T;H)\cap L^2(0,T;V)$ with, for all $v\in V$ and a.e. $t$,
$$
\langle\partial_t u,v-u\rangle+b(u,u,v-u)+a(u,v-u)+j(v)-j(u)\ \ge\ \langle f,v-u\rangle,
\tag{VI}
$$
$b(u,v,w)=\int_\Omega (u\cdot\nabla)v\cdot w$.

**Stationary case as convex minimisation.** With inertia dropped, (VI) is the Euler–Lagrange inequality of
$$
\min_{v\in V}\ J(v)=\mu\!\int_\Omega|\mathbb{D}(v)|^2dx+\tau_*\!\int_\Omega|\mathbb{D}(v)|\,dx-\int_\Omega f\!\cdot\! v\,dx,
$$
a functional of **linear growth in the $\tau_*$ term and quadratic in the $\mu$ term**. Its natural relaxed space is $BD(\Omega)$, functions of bounded deformation, where $\mathbb{D}(v)$ is a matrix-valued Radon measure and $J$ must be relaxed with a boundary term $\tau_*\int_{\partial\Omega}|v\odot\nu|\,d\mathcal{H}^{n-1}$ accounting for boundary slip. Key structural facts used throughout:

- **Korn's inequality:** $\|\nabla v\|_{L^2}\le C\|\mathbb{D}(v)\|_{L^2}$ for $v\in W^{1,2}_0$; it **fails** for $p=1$, so $BD\not\subset BV$.
- **Duality / safe-load:** the dual problem is $\max\{-\tfrac1{4\mu}\|\mathbb{S}-\Pi_{\tau_*}\mathbb{S}\|^2\}$ over divergence-compatible stresses; the multiplier $\lambda=\mathbb{S}-2\mu\mathbb{D}(u)$ satisfies $|\lambda|\le\tau_*$ a.e. and is **unique** even when $u$ is not.
- **Mosolov–Miasnikov:** for antiplane shear in a cross-section $\omega\subset\mathbb{R}^2$, the flow/no-flow threshold is a purely geometric quantity, $\tau_*/G$ compared with $\sup_{A\subset\omega}|A|/\mathcal{H}^1(\partial A\cap\omega)$ — a Cheeger-type constant.

## 3. History & State of the Art (SOTA)

- **1922.** E. C. Bingham introduces the yield-stress model in *Fluidity and Plasticity*.
- **1947–1958.** Oldroyd and Prager give the tensorial von Mises form used above.
- **1965.** Mosolov and Miasnikov solve the antiplane pipe-flow problem variationally, identifying rigid cores and the geometric stagnation criterion.
- **1972/1976.** Duvaut and Lions establish existence of weak solutions to (VI) for $n=2,3$ and uniqueness for $n=2$ — still the baseline well-posedness theory.
- **1981.** Glowinski, Lions and Trémolières give the augmented-Lagrangian/Uzawa numerics (ALG2), still the standard exact-law solver.
- **1996–2000.** Fuchs, Grotowski, Reuling, then Fuchs and Seregin, obtain the first genuine interior regularity: $C^{1,\alpha}$ in $n=2$ and partial regularity in $n=3$ for the quasi-static problem, via $BD$-relaxation and blow-up.
- **2002–2005.** Shelukhin shows Bingham flow is the rigorous limit of regularised (Herschel–Bulkley/bi-viscosity) fluids; Málek–Růžička–Shelukhin treat steady Herschel–Bulkley flows.
- **2005–2015.** Regularisation-versus-exact-law numerics debated (Frigaard–Nouar); Balmforth–Frigaard–Ovarlez survey establishes the yield-surface question as the central analytic gap.

## 4. Partial Results / Verified Cases

- **Existence, all $n\le 3$, all data.** Duvaut–Lions (1976): $u\in L^\infty_tH\cap L^2_tV$ for the unsteady inertial problem; the stationary problem has a unique $\mathbb{D}(u)$ and unique multiplier $\lambda$ in every dimension.
- **Uniqueness, $n=2$.** Global-in-time uniqueness for (VI) with $L^2$ data (Duvaut–Lions). In $n=3$ uniqueness holds only in the Ladyzhenskaya–Prodi–Serrin class or for small data / short time.
- **Interior regularity, $n=2$.** Fuchs–Seregin (Math. Z. 233, 2000): for the quasi-static Bingham variational inequality in $n=2$, $u\in C^{1,\alpha}_{loc}$ and $\mathbb{S}\in C^{0,\alpha}_{loc}$; the rigid zone is closed with $u$ locally rigid there.
- **Partial regularity, $n=3$.** Same paper: $u\in C^{1,\alpha}(\Omega_0)$ for an open $\Omega_0\subset\Omega$ with $\mathcal{H}^{n-2+\varepsilon}$-small singular set for the quasi-static problem; **no** result for the inertial 3D problem.
- **Higher integrability.** $u\in W^{2,2}_{loc}$ and $\mathbb{S}\in W^{1,2}_{loc}$ in $n=2,3$ for stationary flows with $f\in L^2$; the difference quotient argument survives the non-smooth term because $|\cdot|$ is convex.
- **Exactly solvable geometries.** Plane Poiseuille (Section 10), circular pipe (Buckingham–Reiner formula, $1921$), Couette between rotating cylinders, antiplane flow in a strip: here the yield surface is an analytic hypersurface and $u\in C^{1,1}\setminus C^2$.
- **Regularised approximations.** For Herschel–Bulkley with $p>1$ and $\tau_*>0$ mollified as $\tau_*|\mathbb{D}|/\sqrt{|\mathbb{D}|^2+\varepsilon^2}$, $C^{1,\alpha}$ holds for each $\varepsilon>0$, but the estimates degenerate as $\varepsilon\to0$.
- **Stagnation criteria.** Mosolov–Miasnikov: exact geometric thresholds for total rigidity in antiplane pipe flow, verified for polygons, ellipses, eccentric annuli.

## 5. Principal Obstacles

- **Loss of ellipticity on the rigid set.** Where $\mathbb{D}(u)=0$ the operator degenerates from uniformly elliptic to a differential *inclusion*. De Giorgi–Nash–Moser and Caffarelli-type $W^{2,p}$ theory need a nondegenerate ellipticity ratio; here the ratio is unbounded on a set of possibly positive measure.
- **$BD$ is not $BV$.** The natural relaxation space for the linear-growth term has no Korn inequality at exponent $1$. One cannot pass from control of $\mathbb{D}(u)$ to control of $\nabla u$, so standard truncation, Lipschitz-truncation and covering arguments used for power-law fluids (Frehse–Málek–Steinhauer, Diening–Růžička–Wolf) do not transfer.
- **Non-differentiable functional blocks Euler–Lagrange.** The equation is only an inequality; test functions must lie in a convex cone, so the usual "differentiate the equation, test with $\partial_k u$" bootstrap yields only one-sided information.
- **The multiplier $\lambda$ is undetermined on the rigid zone.** $\lambda$ is unique as an $L^\infty$ function, but its *fine* structure — trace on $\partial\mathcal{R}$, continuity — is not controlled; the yield surface is exactly the level set $\{|\lambda|=\tau_*\}$ of a merely $L^\infty$ field, and level sets of $L^\infty$ functions carry no geometry.
- **Inertia in 3D.** Adding $(u\cdot\nabla)u$ reintroduces the full supercriticality of Navier–Stokes: the energy inequality gives $u\in L^\infty_tL^2\cap L^2_tW^{1,2}$, scaling-critical only in $n=2$. The extra $\tau_*$ dissipation gives $\int_0^T\!\!\int|\mathbb{D}(u)|$, which is *weaker* than the $L^2$ term and does not close the scaling gap.
- **No comparison principle / no maximum principle** for the vector-valued inclusion, so free-boundary techniques from the obstacle problem (where $C^{1,1}$ and Caffarelli's regularity of the free boundary hold) have no scalar analogue.

## 6. The Gap

Proven: $C^{1,\alpha}_{loc}$ in $n=2$ for the quasi-static inequality; partial regularity with a small singular set in $n=3$ quasi-static; existence with no regularity in $n=3$ inertial.

Missing, in one line: **an $\varepsilon$-regularity theorem with a scaling-invariant excess that survives the degenerate set.** Concretely, one needs a decay estimate of the form
$$
\fint_{B_r}|\mathbb{D}(u)-(\mathbb{D}(u))_{B_r}|^2 \le C\Big(\frac{r}{R}\Big)^{2\alpha}\fint_{B_R}|\mathbb{D}(u)-(\mathbb{D}(u))_{B_R}|^2 + C r^{2\beta}
$$
valid *uniformly across the yield surface*, where the blow-up limit may be a rigid motion. Existing 2D proofs use the $n=2$ Sobolev embedding $W^{1,2}\hookrightarrow BMO$-type gains and a $BD$-compactness argument that loses a full dimension in $n\ge3$. Crossing the gap requires either (a) proving the singular set is $\mathcal{H}^{n-1}$-negligible rather than merely of empty interior, or (b) proving $\lambda\in C^0$, which upgrades $\{|\lambda|=\tau_*\}$ to a closed set and makes free-boundary methods applicable. Neither implication is currently available in either direction.

## 7. Current Research (as of June 2026)

- **Prague school (Málek, Bulíček, and collaborators, Charles University).** Implicit constitutive theory: treat the Bingham law as a maximal monotone graph $G(\mathbb{D},\mathbb{S})=0$ and prove existence/regularity uniformly across the family, including activated Euler and stress-power-law fluids. Yields uniform-in-$\tau_*$ estimates but not interior $C^{1,\alpha}$ in 3D.
- **Regularity school (successors of Fuchs–Seregin; Saarbrücken, St. Petersburg).** Pushing partial regularity in $n=3$ towards Hausdorff-dimension bounds on the singular set of the quasi-static problem. *(frontier — verify)* Claims of $\dim_{\mathcal H}\mathrm{Sing}\le n-2$ for the quasi-static case circulate in preprint form.
- **Free-boundary/geometric-measure approach.** Treating $\partial\mathcal{R}$ with Cheeger-set and total-variation-flow machinery, exploiting the Mosolov–Miasnikov equivalence between rigidity and Cheeger constants; strongest results remain antiplane ($n=2$ cross-section).
- **Numerics as evidence.** High-accuracy augmented-Lagrangian and adaptive FEM computations (Frigaard, Saramito, Roquet) resolve yield surfaces to mesh scale and consistently show piecewise-smooth surfaces with isolated corners — evidence for, not proof of, rectifiability.
- **Asymptotics $\tau_*\to\infty$ / $\tau_*\to0$.** Rigorous $\Gamma$-convergence of the Bingham functional to perfect plasticity and to Stokes, respectively.

## 8. Future Work

- Prove or disprove **continuity of the multiplier $\lambda$** in $n=3$. This is the smallest self-contained target and would immediately give a closed rigid zone.
- Develop a **Korn-type substitute in $BD$** — e.g. a Lipschitz-truncation lemma adapted to symmetric gradients of linear growth — to import power-law-fluid machinery.
- Establish **$\varepsilon$-regularity for the inertial 3D problem** in the Caffarelli–Kohn–Nirenberg style, using the $\tau_*$ term as extra dissipation; the natural conjecture is a singular set of parabolic Hausdorff dimension $\le1$, as for Navier–Stokes.
- Settle **uniqueness in 3D for the quasi-static problem**, where inertia is absent and the obstruction is purely the degeneracy.
- Prove **rectifiability of $\partial\mathcal{R}$** with a density estimate; the obstacle-problem analogy suggests $C^{1,\alpha}$ away from a lower-dimensional singular set.

## 9. Key References

- **[Foundational]** E. C. Bingham. *Fluidity and Plasticity.* McGraw-Hill, 1922.
- **[Foundational]** P. P. Mosolov, V. P. Miasnikov. *Variational methods in the theory of the fluidity of a viscous-plastic medium.* Journal of Applied Mathematics and Mechanics (PMM), 29(3):545–577, 1965.
- **[Foundational]** G. Duvaut, J.-L. Lions. *Inequalities in Mechanics and Physics.* Grundlehren der mathematischen Wissenschaften 219, Springer, 1976. (French original: *Les inéquations en mécanique et en physique*, Dunod, 1972.)
- **[Foundational]** R. Glowinski, J.-L. Lions, R. Trémolières. *Numerical Analysis of Variational Inequalities.* North-Holland, 1981.
- **[SOTA]** M. Fuchs, G. Seregin. *Regularity results for the quasi-static Bingham variational inequality in dimensions two and three.* Mathematische Zeitschrift, 233:569–592, 2000.
- **[SOTA]** M. Fuchs, J. F. Grotowski, J. Reuling. *On variational models for quasi-static Bingham fluids.* Mathematical Methods in the Applied Sciences, 19:991–1015, 1996.
- **[SOTA]** M. Fuchs, G. Seregin. *Variational Methods for Problems from Plasticity Theory and for Generalized Newtonian Fluids.* Lecture Notes in Mathematics 1749, Springer, 2000.
- **[SOTA]** V. V. Shelukhin. *Bingham viscoplastic as a limit of non-Newtonian fluids.* Journal of Mathematical Fluid Mechanics, 4:109–127, 2002.
- **[SOTA]** J. Málek, M. Růžička, V. V. Shelukhin. *Herschel–Bulkley fluids: existence and regularity of steady flows.* Mathematical Models and Methods in Applied Sciences, 15:1845–1861, 2005.
- **[Related]** J. Frehse, J. Málek, M. Steinhauer. *On analysis of steady flows of fluids with shear-dependent viscosity based on the Lipschitz truncation method.* SIAM Journal on Mathematical Analysis, 34:1064–1083, 2003.
- **[Survey]** N. J. Balmforth, I. A. Frigaard, G. Ovarlez. *Yielding to stress: recent developments in viscoplastic fluid mechanics.* Annual Review of Fluid Mechanics, 46:121–146, 2014.
- **[Survey]** R. R. Huilgol. *Fluid Mechanics of Viscoplasticity.* Springer, 2015.
- **[Survey]** I. A. Frigaard, C. Nouar. *On the usage of viscosity regularisation methods for visco-plastic fluid flow computation.* Journal of Non-Newtonian Fluid Mechanics, 127:1–26, 2005.

## 10. Worked Example / Concrete Special Case

**Plane Poiseuille flow of a Bingham fluid.** Take $\Omega=\mathbb{R}\times(-h,h)$, steady, unidirectional: $u=(u(x_2),0)$, constant pressure gradient $\partial_1 p=-G<0$. Then $\mathbb{D}(u)$ has only the off-diagonal entry $\tfrac12u'(x_2)$, inertia vanishes identically, and momentum balance reduces to $\mathbb{S}_{12}'(x_2)=-G$, so
$$
\mathbb{S}_{12}(x_2)=-G\,x_2 ,
$$
using symmetry $\mathbb{S}_{12}(0)=0$. Write $y_0=\tau_*/G$.

*Rigid core.* $|\mathbb{S}_{12}|\le\tau_*$ exactly when $|x_2|\le y_0$. There $u'=0$: the fluid moves as an unsheared **plug**.

*Yielded layers.* For $y_0<x_2<h$ we have $u'<0$, so the law gives $\mu u'-\tau_*=-Gx_2$, i.e. $u'(x_2)=(\tau_*-Gx_2)/\mu$. Integrating with $u(h)=0$:
$$
u(x_2)=\frac{G}{2\mu}\,(h^2-x_2^2)-\frac{\tau_*}{\mu}\,(h-x_2),\qquad y_0\le x_2\le h,
$$
and by symmetry on $-h\le x_2\le -y_0$. Matching at $x_2=y_0$ with $\tau_*=Gy_0$ gives the plug speed
$$
u_p=\frac{G}{2\mu}\,(h-y_0)^2 .
$$

*Consequences.*
- If $G\le\tau_*/h$ then $y_0\ge h$: the whole channel is rigid and $u\equiv0$. This is the 1D instance of the Mosolov–Miasnikov stagnation criterion.
- $u'$ is continuous and piecewise linear, hence $u\in C^{1,1}$; but $u''=-G/\mu$ for $|x_2|>y_0$ and $u''=0$ for $|x_2|<y_0$, so $u''$ jumps by $G/\mu$ across $x_2=\pm y_0$. **$u\notin C^2$**, and $C^{1,1}$ is optimal. Any conjectured general regularity statement must therefore stop at $C^{1,\alpha}$/$C^{1,1}$ — $C^2$ is false already in the simplest geometry.
- Flow rate: $Q=\int_{-h}^{h}u=\frac{2Gh^3}{3\mu}\Big(1-\tfrac32\tfrac{y_0}{h}+\tfrac12\tfrac{y_0^3}{h^3}\Big)$, the plane analogue of the Buckingham–Reiner formula, vanishing to third order as $y_0\to h$.

The yield surface here is the pair of hyperplanes $\{x_2=\pm y_0\}$ — flat, analytic, and determined by an explicit formula. The open problem of Section 1 asks whether anything of this structure survives in a general 3D domain, where $\mathbb{S}$ is only known to be an $L^2$ tensor field and $\{|\mathbb{S}|=\tau_*\}$ is a level set with no a priori geometry.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*