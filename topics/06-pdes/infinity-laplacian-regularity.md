---
id: 06-pdes/infinity-laplacian-regularity
title: "Infinity Laplacian Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinity Laplacian Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/infinity-laplacian-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ be open and let $u \in C(\Omega)$ be a viscosity solution of the infinity Laplace equation
$$\Delta_\infty u := \sum_{i,j=1}^n u_{x_i} u_{x_j} u_{x_i x_j} = 0 \quad \text{in } \Omega .$$
Such a $u$ is called **infinity harmonic**.

**Conjecture (interior regularity).** Every infinity harmonic function on $\Omega\subset\mathbb{R}^n$ is $C^{1,\alpha}_{\mathrm{loc}}(\Omega)$ for some $\alpha=\alpha(n)>0$.

**Sharp form.** The optimal exponent is $\alpha = 1/3$, i.e. $u \in C^{1,1/3}_{\mathrm{loc}}$, and this cannot be improved.

A complete resolution requires either (a) a proof of interior $C^1$ (and then Hölder) regularity of $Du$ valid in all dimensions $n \ge 3$, with a modulus depending only on $n$ and $\|u\|_{L^\infty}$; or (b) a counterexample: an infinity harmonic function on a ball in some $\mathbb{R}^n$ whose gradient is not continuous, or is continuous but not Hölder. Only $n=2$ is settled. Nothing beyond everywhere-differentiability is known for $n\ge 3$.

## 2. Mathematical Foundations

**The operator.** $\Delta_\infty$ is the formal limit as $p\to\infty$ of $p^{-1}|Du|^{4-p}\Delta_p u$, where $\Delta_p u = \operatorname{div}(|Du|^{p-2}Du)$. It is degenerate elliptic: writing $A(\xi)=\xi\otimes\xi$, the equation is $\operatorname{tr}\!\big(A(Du)\,D^2u\big)=0$, so the coefficient matrix has rank $1$ and vanishes identically where $Du=0$. It is not in divergence form and admits no variational structure in the usual sense.

**Viscosity solutions.** $u$ is a viscosity subsolution if for every $\varphi\in C^2$ touching $u$ from above at $x_0$ one has $\Delta_\infty\varphi(x_0)\ge 0$; supersolutions reverse the inequality. This is necessary because $u$ need not be twice differentiable (Section 10).

**Absolutely minimizing Lipschitz extensions (AMLE).** For $V\Subset\Omega$ set $\operatorname{Lip}(u,V)=\sup_{x\ne y\in V}\frac{|u(x)-u(y)|}{|x-y|}$. A function $u\in C(\Omega)$ is *absolutely minimizing* if for all $V\Subset\Omega$ and $v\in C(\overline V)$ with $v=u$ on $\partial V$,
$$\operatorname{Lip}(u,V)\le \operatorname{Lip}(v,V).$$
**Theorem (Aronsson 1967; Jensen 1993; Crandall–Evans–Gariepy 2001).** $u$ is absolutely minimizing $\iff$ $u$ is infinity harmonic $\iff$ $u$ enjoys *comparison with cones*: for every $V\Subset\Omega$, $b\in\mathbb{R}$, $a\in\mathbb{R}$, $z\notin V$, if $u(x)\le b+a|x-z|$ on $\partial V$ then the same holds in $V$.

**Existence/uniqueness.** Jensen (1993) proved that for $g\in C(\partial\Omega)$ the Dirichlet problem $\Delta_\infty u=0$ in $\Omega$, $u=g$ on $\partial\Omega$ has a unique viscosity solution; Armstrong–Smart (2010) gave a short proof via a finite-difference/comparison argument.

**Structural identities.** For $x\in\Omega$ and small $r$ define
$$S^+_r(x)=\max_{|y-x|=r}\frac{u(y)-u(x)}{r},\qquad S^-_r(x)=\max_{|y-x|=r}\frac{u(x)-u(y)}{r}.$$
Comparison with cones makes $r\mapsto S^\pm_r(x)$ nondecreasing, and $|Du(x)|=\lim_{r\to 0}S^+_r(x)=\lim_{r\to 0}S^-_r(x)$ wherever $u$ is differentiable. Infinity harmonic functions satisfy the asymptotic mean value property
$$u(x)=\tfrac12\Big(\max_{\overline B_r(x)}u+\min_{\overline B_r(x)}u\Big)+o(r^2),$$
the deterministic shadow of the **tug-of-war** game of Peres–Schramm–Sheffield–Wilson (2009), whose value function is the AMLE.

**Aronsson equations.** More generally, for a Hamiltonian $H\in C^2$, minimizers of $\|H(Du)\|_{L^\infty}$ satisfy $\mathcal{A}_H[u]=\langle D^2u\,D_\xi H(Du),D_\xi H(Du)\rangle=0$; $H(\xi)=\tfrac12|\xi|^2$ recovers $\Delta_\infty$.

## 3. History & State of the Art (SOTA)

- **1967–1968.** Gunnar Aronsson introduces absolutely minimizing extensions and derives $\Delta_\infty u=0$ as the Euler–Lagrange equation of the $L^\infty$ variational problem (*Ark. Mat.*). He produces $u(x,y)=|x|^{4/3}-|y|^{4/3}$, an explicit $C^{1,1/3}$ but non-$C^2$ solution, fixing the ceiling for any regularity theory.
- **1993.** Robert Jensen proves uniqueness of viscosity solutions of the Dirichlet problem, and the equivalence with absolute minimality (*Arch. Ration. Mech. Anal.*). This turns $\Delta_\infty$ into a well-posed PDE.
- **2001.** Crandall–Evans–Gariepy establish the cone-comparison characterization (*Calc. Var. PDE*), giving the geometric tool that all later regularity work uses.
- **2005.** Ovidiu Savin proves $C^1$ regularity in the plane (*ARMA*) by a compactness/contradiction argument exploiting planar topology of level sets.
- **2008.** Evans–Savin upgrade this to $C^{1,\alpha}$ for $n=2$ (*Calc. Var. PDE*), with a small non-explicit $\alpha$.
- **2009.** Peres–Schramm–Sheffield–Wilson give the tug-of-war probabilistic representation (*J. Amer. Math. Soc.*), extending existence/uniqueness to length spaces.
- **2011.** Evans–Smart prove everywhere differentiability of infinity harmonic functions in every dimension (*Calc. Var. PDE*), via an adjoint/vanishing-viscosity method (*ARMA*, 2011). No modulus of continuity for $Du$ is obtained.
- **2019.** Koch–Zhang–Zhou obtain asymptotically sharp Sobolev regularity for planar infinity harmonic functions (*J. Math. Pures Appl.*), quantifying the integrability of second derivatives in $n=2$.

**Status:** $n=2$ solved qualitatively ($C^{1,\alpha}$), sharp exponent unknown; $n\ge3$ open beyond differentiability.

## 4. Partial Results / Verified Cases

- **$n=2$, homogeneous:** $u\in C^{1,\alpha}_{\mathrm{loc}}$ (Evans–Savin 2008). The exponent is not explicit and is far from the conjectured $1/3$.
- **All $n\ge 2$:** $u$ is differentiable at *every* point (Evans–Smart 2011); moreover $|Du|$ is upper semicontinuous and $\lim_{r\to0}S^\pm_r=|Du|$ everywhere. Continuity of $Du$ is not obtained.
- **All $n$, blow-up rigidity:** any blow-up limit $\lim_j \frac{u(x_0+r_jx)-u(x_0)}{r_j}$ is a linear function $x\mapsto \langle Du(x_0),x\rangle$ (Crandall–Evans–Gariepy; Evans–Smart).
- **Non-vanishing gradient:** where $u\in C^2$ and $Du\ne 0$, classical Aronsson theory shows the gradient flow lines are straight segments along which $u$ is affine, giving local smoothness. In the plane this rigidity is what drives Savin's argument.
- **Small perturbations / linear data:** if $u$ is infinity harmonic in $B_1$ and $\|u-\ell\|_{L^\infty(B_1)}\le\varepsilon(n)$ for an affine $\ell$ with $|D\ell|=1$, then $u$ is $C^{1,\alpha}$ in $B_{1/2}$ — a flatness-implies-regularity statement valid in all dimensions. The obstruction is the absence of a decay/iteration mechanism to reach flatness.
- **Sobolev, $n=2$:** $|Du|^\beta\in W^{1,2}_{\mathrm{loc}}$ for suitable $\beta>2$, asymptotically sharp as $\beta\downarrow 2$ (Koch–Zhang–Zhou 2019); Savin's estimate already gives $u\in W^{2,p}$-type control only in the plane.
- **Inhomogeneous equation $\Delta_\infty u=f$:** uniqueness holds when $f>0$ or $f<0$ throughout (Lu–Wang, *Adv. Math.* 2008); Lindgren (2014) proves everywhere differentiability for continuous $f$. Uniqueness for sign-changing $f$ is itself open.
- **General Aronsson equations:** everywhere differentiability for a class of $C^2$ Hamiltonians (Wang–Yu, *Ann. IHP* 2008); planar $C^1$ for convex Hamiltonians with suitable structure.

## 5. Principal Obstacles

- **Rank-one degeneracy.** $A(Du)=Du\otimes Du$ has rank $1$: the equation controls the second derivative only in the single direction $Du/|Du|$. Krylov–Safonov Harnack, Evans–Krylov, and De Giorgi–Nash–Moser all require uniform ellipticity or a divergence structure; none applies.
- **No divergence form, no energy.** There is no Caccioppoli inequality, no $W^{1,2}$-based iteration, and no monotonicity formula. Difference quotients cannot be tested against the equation.
- **Singular set at $Du=0$.** Where the gradient vanishes the equation degenerates completely and carries no information. Aronsson's example is singular precisely on the axes $\{x=0\}\cup\{y=0\}$, where $D^2u$ blows up.
- **Failure of $p$-harmonic approximation.** Uniform-in-$p$ gradient estimates for $\Delta_p$ deteriorate like $O(1/p)$ or worse; passing $p\to\infty$ loses every quantitative constant.
- **Non-perturbative planar arguments.** Savin's $C^1$ proof uses that in $\mathbb{R}^2$ a level set separates the domain, and that "$u$ is close to a cone on a large scale" propagates by a topological connectedness argument. In $\mathbb{R}^3$ level sets do not disconnect balls and the argument has no known substitute.
- **Adjoint method yields no modulus.** Evans–Smart's differentiability proof integrates against the adjoint of the linearized operator at the viscosity level; it gives pointwise linearity of blow-ups but no rate, hence no compactness for $Du$.

## 6. The Gap

Proven: $Du$ exists at every point in every dimension, and every blow-up of $u$ is linear. Conjectured: $Du$ is continuous with a Hölder modulus.

The gap is exactly a **quantitative rate of convergence of blow-ups**. One needs a decay estimate of the form: there exist $\theta\in(0,1)$, $C$, $\alpha>0$ such that for infinity harmonic $u$ in $B_1$,
$$\inf_{\ell \text{ affine}} \|u-\ell\|_{L^\infty(B_r)} \le C r^{1+\alpha}\inf_{\ell}\|u-\ell\|_{L^\infty(B_1)} \quad \text{for all } r<\theta ,$$
uniform in $n$. Currently $\|u-\ell\|_{L^\infty(B_r)}=o(r)$ pointwise (differentiability) with no rate and no uniformity in the base point. Closing this requires either a genuinely dimension-free improvement-of-flatness iteration, or a Harnack-type inequality for the gradient of a rank-one degenerate operator — neither exists.

## 7. Current Research (as of June 2026)

- **Sharp planar exponents.** Groups around Beijing Normal University (Y. Zhou, C. Wang) and Bonn (H. Koch) continue to push planar Sobolev/Hölder estimates toward $\alpha=1/3$; the conjecture that the planar exponent equals $1/3$ remains open. *(frontier — verify)*
- **Aronsson equations for general $H$.** Regularity for $\mathcal{A}_H$ with convex, non-quadratic $H$ (Katzourakis, Leicester; Wang, Kentucky) is developed via vectorial $L^\infty$ calculus of variations; results parallel but do not exceed the $\Delta_\infty$ case.
- **Game-theoretic and discrete methods.** Tug-of-war discretizations and their $\varepsilon$-step regularity (Armstrong–Smart-style finite-difference approximations, work in the Helsinki/Jyväskylä school around Parviainen and Lindqvist) aim at estimates stable as $\varepsilon\to0$.
- **Adjoint / stochastic-control methods.** Refinements of Evans–Smart aiming at a modulus for $Du$ in $n\ge3$; no announced breakthrough. *(frontier — verify)*
- **Free-boundary and obstacle analogues** for $\Delta_\infty$ (Rossi and collaborators, Buenos Aires) and inhomogeneous problems with sign-changing $f$.

## 8. Future Work

1. **Dimension-free flatness iteration.** Find a compactness argument replacing planar topology — for instance a quantitative version of "blow-ups are linear" using the monotone quantities $S^\pm_r$ uniformly in $x$.
2. **Harnack for $|Du|$.** Prove that $\sup_{B_{1/2}}|Du| \le C\inf_{B_{1/2}}|Du|$ away from the zero set, or a suitable weak analogue; this would linearize the problem in a uniformly elliptic regime.
3. **Structure of $\{Du=0\}$.** Estimate the Hausdorff dimension of the critical set in $n\ge3$; in the plane it is known to be small. A dimension bound would allow a covering argument.
4. **Counterexample search.** Systematically look for non-$C^1$ solutions in $n\ge3$, e.g. by rotationally symmetric ansätze or by gluing Aronsson-type profiles across cones.
5. **Numerics.** High-accuracy monotone finite-difference schemes for $\Delta_\infty$ in $\mathbb{R}^3$ to test whether $C^{1,1/3}$ is the sharp ceiling.

## 9. Key References

- **[Foundational]** G. Aronsson. *Extension of functions satisfying Lipschitz conditions.* Arkiv för Matematik 6 (1967), 551–561.
- **[Foundational]** G. Aronsson. *On the partial differential equation $u_x^2u_{xx}+2u_xu_yu_{xy}+u_y^2u_{yy}=0$.* Arkiv för Matematik 7 (1968), 395–425.
- **[Foundational]** R. Jensen. *Uniqueness of Lipschitz extensions: minimizing the sup norm of the gradient.* Arch. Ration. Mech. Anal. 123 (1993), 51–74.
- **[Foundational]** M. G. Crandall, L. C. Evans, R. F. Gariepy. *Optimal Lipschitz extensions and the infinity Laplacian.* Calc. Var. PDE 13 (2001), 123–139.
- **[SOTA]** O. Savin. *$C^1$ regularity for infinity harmonic functions in two dimensions.* Arch. Ration. Mech. Anal. 176 (2005), 351–361.
- **[SOTA]** L. C. Evans, O. Savin. *$C^{1,\alpha}$ regularity for infinity harmonic functions in two dimensions.* Calc. Var. PDE 32 (2008), 325–347.
- **[SOTA]** L. C. Evans, C. K. Smart. *Everywhere differentiability of infinity harmonic functions.* Calc. Var. PDE 42 (2011), 289–299.
- **[SOTA]** L. C. Evans, C. K. Smart. *Adjoint methods for the infinity Laplacian partial differential equation.* Arch. Ration. Mech. Anal. 201 (2011), 87–113.
- **[SOTA]** Y. Peres, O. Schramm, S. Sheffield, D. B. Wilson. *Tug-of-war and the infinity Laplacian.* J. Amer. Math. Soc. 22 (2009), 167–210.
- **[SOTA]** H. Koch, Y. R.-Y. Zhang, Y. Zhou. *An asymptotic sharp Sobolev regularity for planar infinity harmonic functions.* J. Math. Pures Appl. 132 (2019), 457–482.
- **[Related]** G. Lu, P. Wang. *Inhomogeneous infinity Laplace equation.* Advances in Mathematics 217 (2008), 1838–1868.
- **[Related]** S. Armstrong, C. K. Smart. *An easy proof of Jensen's theorem on the uniqueness of infinity harmonic functions.* Calc. Var. PDE 37 (2010), 381–384.
- **[Survey]** G. Aronsson, M. G. Crandall, P. Juutinen. *A tour of the theory of absolutely minimizing functions.* Bull. Amer. Math. Soc. 41 (2004), 439–505.
- **[Survey]** P. Lindqvist. *Notes on the Infinity Laplace Equation.* SpringerBriefs in Mathematics, Springer, 2016.

## 10. Worked Example / Concrete Special Case

**Aronsson's function.** Let
$$u(x,y)=|x|^{4/3}-|y|^{4/3},\qquad (x,y)\in\mathbb{R}^2 .$$

*Derivatives off the axes.* For $x,y\ne0$,
$$u_x=\tfrac43\operatorname{sgn}(x)|x|^{1/3},\quad u_y=-\tfrac43\operatorname{sgn}(y)|y|^{1/3},\quad u_{xx}=\tfrac49|x|^{-2/3},\quad u_{yy}=-\tfrac49|y|^{-2/3},\quad u_{xy}=0 .$$

*Verification.*
$$\Delta_\infty u = u_x^2u_{xx}+2u_xu_yu_{xy}+u_y^2u_{yy}
=\tfrac{16}{9}|x|^{2/3}\cdot\tfrac49|x|^{-2/3}+0+\tfrac{16}{9}|y|^{2/3}\cdot\big(-\tfrac49|y|^{-2/3}\big)=\tfrac{64}{81}-\tfrac{64}{81}=0 .$$
The cancellation is exact and independent of $(x,y)$, so $u$ is a classical solution on $\{xy\ne0\}$; a direct check with test functions shows it is a viscosity solution across the axes.

*Regularity ceiling.* $|Du(x,y)|=\tfrac43\big(|x|^{2/3}+|y|^{2/3}\big)^{1/2}$, so $Du$ is continuous and, since $t\mapsto t^{1/3}$ is $1/3$-Hölder and no better at $0$,
$$|Du(x,0)-Du(0,0)|=\tfrac43|x|^{1/3},$$
i.e. $u\in C^{1,1/3}$ and $u\notin C^{1,\beta}$ for any $\beta>1/3$. Meanwhile $u_{xx}=\frac49|x|^{-2/3}\to\infty$ as $x\to0$, so $u\notin C^2$ and $u_{xx}\in L^p_{\mathrm{loc}}$ only for $p<3/2$.

*What this fixes.* The example shows (i) the conjectured exponent $1/3$ cannot be improved; (ii) any proof must operate at the level of viscosity solutions, since $D^2u$ genuinely blows up on a set of positive $1$-dimensional measure; (iii) the singular set coincides with $\{Du=0\}$ only partly — here $Du(0,0)=0$ while on the punctured axes $Du\ne0$ yet $D^2u$ is unbounded, so controlling $\{Du=0\}$ alone is not sufficient. Rescaling at the origin, $u_r(x,y)=r^{-4/3}u(rx,ry)=u(x,y)$: the function is self-similar of degree $4/3>1$, so its blow-up is the zero linear function, consistent with the Evans–Smart theorem and showing that linearity of blow-ups carries no rate information — exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*