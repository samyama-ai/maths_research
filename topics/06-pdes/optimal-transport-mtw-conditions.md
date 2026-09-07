---
id: 06-pdes/optimal-transport-mtw-conditions
title: "Optimal Transport MTW Conditions"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Transport MTW Conditions

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/optimal-transport-mtw-conditions` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Ma–Trudinger–Wang (MTW) tensor is a fourth-order differential invariant of a transport cost $c(x,y)$ whose sign controls regularity of optimal maps. Loeper proved the condition is *necessary*: if it fails at one point, smooth positive densities exist whose optimal map is discontinuous. It is also *sufficient* under convexity hypotheses. The open problem is therefore not "is MTW the right condition" but the two questions it leaves:

**(Q1) Classification.** Characterize the pairs $(M,c)$ — in particular Riemannian manifolds $(M,g)$ with $c=d_g^2/2$ — satisfying $\mathrm{A3w}$ (MTW $\ge 0$) or $\mathrm{A3s}$ (MTW $>0$). Nonnegative sectional curvature is necessary but not sufficient (Kim, 2008). No intrinsic geometric characterization is known.

**(Q2) Loeper–Villani conjecture.** If $(M,g)$ is compact and satisfies $\mathrm{A3s}$, then every tangent injectivity domain $I(x)\subset T_xM$ is (uniformly) convex.

A complete resolution of (Q1) means a checkable geometric criterion equivalent to $\mathrm{A3w}$; of (Q2), a proof in all dimensions or a counterexample manifold with $\mathrm{A3s}$ and a nonconvex injectivity domain.

## 2. Mathematical Foundations

Let $\Omega,\Omega'\subset\mathbb R^n$ be bounded domains, $c\in C^4(\overline\Omega\times\overline{\Omega'})$, and $\mu=f\,dx$, $\nu=g\,dy$ probability measures. Monge's problem seeks $T_\\\\#\mu=\nu$ minimizing $\int c(x,T(x))\,d\mu$. Under

- **(A1)** for each $x$, $y\mapsto D_xc(x,y)$ is injective (twist),
- **(A2)** $\det\big(c_{i,j}\big)\neq 0$, where $c_{i,j}=\partial^2c/\partial x^i\partial y^j$,

the optimal map is $T(x)=c\text{-}\exp_x(Du(x))$ for a $c$-convex potential $u$ solving the Monge–Ampère type equation
$$\det\!\big(D^2u(x)-D^2_{xx}c(x,T(x))\big)=\big|\det c_{i,j}\big|\,\frac{f(x)}{g(T(x))}.$$

Write $c^{i,j}$ for the inverse of $c_{i,j}$ and $c_{ij,k}=\partial^3 c/\partial x^i\partial x^j\partial y^k$. The **MTW tensor** is
$$\mathfrak S_c(x,y)(\xi,\eta)=\big(c_{ij,rs}-c_{ij,p}\,c^{p,q}\,c_{q,rs}\big)\,c^{r,k}c^{s,l}\,\xi^i\xi^j\eta^k\eta^l ,$$
summation implied, with the sign fixed so that on a Riemannian manifold with $c=d^2/2$ one has, on the diagonal and for $\xi\perp\eta$,
$$\mathfrak S_c(x,x)(\xi,\eta)=\tfrac{4}{3}\,\mathrm{Sec}_x(\xi\wedge\eta)\,|\xi|^2|\eta|^2 .$$

- **(A3w)** $\mathfrak S_c(x,y)(\xi,\eta)\ge 0$ whenever $\textstyle\sum_{i,k}c_{i,k}\,\xi^i\eta^k=0$.
- **(A3s)** $\mathfrak S_c(x,y)(\xi,\eta)\ge K|\xi|^2|\eta|^2$ for some $K>0$ under the same orthogonality.

**Kim–McCann reformulation.** On $M\times N$ the symmetric bilinear form
$$h=-\tfrac12\begin{pmatrix}0 & c_{i,j}\\ c_{i,j}^{\,\top} & 0\end{pmatrix}$$
is a pseudo-Riemannian metric of signature $(n,n)$; $\mathrm{A3w}$ is exactly nonnegativity of its sectional curvature on null planes spanned by $\xi\oplus0$ and $0\oplus\eta$. This makes MTW manifestly invariant under diffeomorphisms of $M$ and $N$ separately.

**Loeper's synthetic form (DASM).** $\mathrm{A3w}$ is equivalent to: for every $x$ and every $c$-segment $t\mapsto y_t$ (a segment in the $D_xc$ coordinates), the function $t\mapsto -c(x',y_t)+c(x,y_t)$ satisfies the maximum principle
$$-c(x',y_t)+c(x,y_t)\le\max\{-c(x',y_0)+c(x,y_0),\,-c(x',y_1)+c(x,y_1)\}.$$
Equivalently, the $c$-subdifferential of any $c$-convex function is $c$-convex — a statement with no derivatives in it, which is why it survives as the "right" condition.

**Regularity theorem (Ma–Trudinger–Wang; Trudinger–Wang; Loeper).** Under (A1),(A2),(A3s), $c$-convexity of $\Omega,\Omega'$, and $0<\lambda\le f,g\le\Lambda$: $u\in C^{1,\alpha}$ with $\alpha=\alpha(n)$; if additionally $f,g\in C^\beta$ then $u\in C^{2,\beta}$ and $T$ is a diffeomorphism when $f,g$ are smooth.

## 3. History & State of the Art (SOTA)

- **1991–1996.** Brenier's polar factorization; Caffarelli's interior regularity for $c=|x-y|^2/2$ requires convexity of the target and fails without it. Wang's reflector-antenna work ($c=-\log|x-y|$) is the first non-quadratic regularity theory.
- **2005.** Ma, Trudinger and Wang isolate $\mathfrak S_c$ and prove interior $C^3$ regularity under $\mathrm{A3s}$ (ARMA 177).
- **2009.** Loeper (Acta Math. 202) proves $\mathrm{A3w}$ is *necessary* — failure at one point yields smooth positive densities with a discontinuous optimal map — establishes the DASM equivalence, and gives the $C^{1,\alpha}$ estimate with $\alpha=1/(4n-1)$ under $\mathrm{A3s}$. Trudinger–Wang give global $C^{2,\alpha}$ under $\mathrm{A3w}$ plus strong $c$-convexity.
- **2009–2011.** Loeper (ARMA 199, 2011) verifies $\mathrm{A3s}$ for the round sphere with $c=d^2/2$, with $\mathfrak S_c\ge\tfrac23|\xi|^2|\eta|^2$ in the standard normalization. Loeper–Villani (Duke Math. J. 151, 2010) prove regularity in the nonfocal case and formulate the convexity conjecture.
- **2010–2013.** Kim–McCann's pseudo-Riemannian picture (JEMS 12, 2010); Delanoë–Ge for space forms; Figalli–Rifford–Villani's necessary-and-sufficient conditions on manifolds; Figalli–Kim–McCann prove $\mathrm{A3w}$ and continuity of optimal maps on multiple products of round spheres (JEMS 15, 2013), and $C^{1,\alpha}$ regularity under $\mathrm{A3w}$ alone (ARMA 209, 2013).
- **2014–2020.** De Philippis–Figalli survey the field (BAMS 51, 2014). Guillen–Kitagawa (CPAM 70, 2017) extend the MTW machinery to generated Jacobian equations, covering near-field geometric optics where $c$ is replaced by a generating function.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $c=\|x-y\|^2/2$ on $\mathbb R^n$ | $\mathfrak S_c\equiv0$: $\mathrm{A3w}$ holds degenerately, $\mathrm{A3s}$ fails. Regularity is Caffarelli's, needing target convexity. |
| Round sphere $S^n$, $c=d^2/2$ | $\mathrm{A3s}$ holds, all $n\ge2$ (Loeper 2011; Kim–McCann). |
| Space forms of constant curvature $\ge0$; $\mathbb{RP}^n$ | $\mathrm{A3s}$ / $\mathrm{A3w}$ verified (Delanoë–Ge 2010; Kim–McCann). |
| $\mathbb{CP}^n$, $\mathbb{HP}^n$ | $\mathrm{A3w}$ via Riemannian submersion from Lie groups (Kim–McCann, Crelle 664, 2012). |
| Products $S^{n_1}\times\cdots\times S^{n_k}$ | $\mathrm{A3w}$ (not $\mathrm{A3s}$: mixed planes are degenerate); optimal maps continuous (Figalli–Kim–McCann 2013). |
| $C^4$-perturbations of $S^2$ | $\mathrm{A3s}$ and convex injectivity domains persist; optimal maps continuous (Figalli–Rifford, CPAM 2010; Figalli–Rifford–Villani, *Nearly round spheres look convex*, Amer. J. Math. 134, 2012). |
| Surfaces, $n=2$ | $\mathrm{A3s}$ + a nonfocality/geometric hypothesis $\Rightarrow$ convex injectivity domains: Loeper–Villani conjecture proved in dimension 2 (Figalli–Rifford–Villani, Calc. Var. PDE 39, 2010). |
| Nonfocal manifolds, any $n$ | $\mathrm{A3s}$ $\Rightarrow$ regularity (Loeper–Villani, Duke 2010). |
| Costs on $\mathbb R^n$ | $\mathrm{A3s}$ verified for $c=\sqrt{1+\|x-y\|^2}$ and $c=-\sqrt{1-\|x-y\|^2}$; $\mathrm{A3w}$ for $c=-\log\|x-y\|$; power costs $\pm\|x-y\|^p$ satisfy $\mathrm{A3s}$ only for restricted $p$ and on domains obeying extra geometric restrictions (MTW 2005, §4). |
| Negative sectional curvature anywhere | $\mathrm{A3w}$ fails; discontinuous optimal maps exist (Loeper 2009). |
| $\mathrm{Sec}>0$ but $\mathrm{A3w}$ false | Explicit examples exist (Kim, IMRN 2008). |

Under $\mathrm{A3w}$ alone with $c$-convex support, Figalli–Kim–McCann give $u\in C^{1,\alpha}$ and injectivity of $T$; $C^2$ regularity generally fails without $\mathrm{A3s}$.

## 5. Principal Obstacles

- **The tensor is a global object in disguise.** $\mathfrak S_c(x,y)$ involves fourth derivatives of $d^2$ at pairs $(x,y)$ that may be far apart, i.e. Jacobi-field data along a whole minimizing geodesic. Curvature bounds are pointwise; MTW is not implied by any pointwise curvature condition. This is exactly why Kim's positively curved counterexamples exist.
- **Cut locus nonsmoothness.** $d^2$ is only Lipschitz across the cut locus, so $\mathfrak S_c$ is not classically defined there — the analysis must be done in a nonsmooth/viscosity framework, and the cut locus is precisely where the interesting degeneracies live. Villani calls this the central technical obstruction.
- **Failure of perturbation.** $\mathrm{A3s}$ is an open condition in $C^4$, but $\mathrm{A3w}$ is closed and typically *degenerate* (products of spheres, flat space). Perturbative arguments give no information at degenerate null planes, and second-order estimates blow up as $K\to0$.
- **No maximum principle at fourth order.** The Monge–Ampère type equation is degenerate elliptic in $D^2u$; the MTW term enters only when one differentiates the equation twice, so the standard Pogorelov/Caffarelli toolkit — which works for the quadratic cost because $\mathfrak S_c\equiv0$ kills the offending term — has no substitute when $\mathfrak S_c$ changes sign.
- **Convexity is not variational.** Injectivity domains $I(x)$ are described by the cut-time function, which is only semiconcave; there is no known energy or curvature flow whose monotonicity forces $I(x)$ convex, so (Q2) resists all soft arguments.

## 6. The Gap

Proved: $\mathrm{A3w}$ is necessary and, with $c$-convexity of the supports, sufficient for continuity. Verified on a finite list of highly symmetric spaces (spheres, projective spaces, their products, small perturbations of $S^2$).

Not proved:
1. **Any intrinsic criterion.** Every verification above is a hand computation exploiting symmetry (Jacobi fields with constant curvature, submersion identities). There is no theorem of the form "$\mathrm{A3w}$ $\iff$ [condition on $\mathrm{Sec}$, injectivity radius, focal structure]". The gap is between a finite list of examples and a classification.
2. **$\mathrm{A3s}\Rightarrow$ convexity of $I(x)$** is known only for $n=2$ and in the nonfocal case; dimension $\ge3$ with focal points is fully open. Since convexity of $I(x)$ is a *hypothesis* in every manifold regularity theorem, closing this gap would make $\mathrm{A3s}$ alone sufficient.
3. **Sharp exponents.** The $C^{1,\alpha}$ exponent under $\mathrm{A3s}$ is $\alpha\ge1/(4n-1)$ (Loeper), improved to $1/(2n-1)$ for the quadratic-like case; the optimal $\alpha$ as a function of $n$ and the density regularity is unknown.

## 7. Current Research (as of June 2026)

- **Generated Jacobian equations.** Guillen–Kitagawa's extension of the MTW condition to generating functions (near-field reflector/refractor design) is the most active line; the analogue of (Q1) there — which optical configurations satisfy generated-A3w — is open and application-driven.
- **Synthetic and metric-measure formulations.** Attempts to express $\mathrm{A3w}$ via the DASM maximum principle on non-smooth spaces (Alexandrov spaces, $\mathrm{RCD}$ spaces), aiming at stability under Gromov–Hausdorff limits. *(frontier — verify)*
- **Groups and homogeneous spaces.** Extending Kim–McCann's submersion technique to general compact symmetric spaces and to sub-Riemannian settings (Heisenberg group), where the cut locus is generically nonsmooth. *(frontier — verify)*
- **Numerics.** Machine-assisted evaluation of $\mathfrak S_c$ along geodesic families, used to search for $\mathrm{Sec}>0$ manifolds violating $\mathrm{A3w}$ and to test the Loeper–Villani conjecture in dimension $3$. *(frontier — verify)*
- Groups: ETH Zürich (Figalli), Toronto (McCann), ANU/Wollongong (Trudinger, Wang, Kitagawa's collaborators), Michigan State (Kitagawa), Nice/Grenoble (Rifford), Lyon (Villani's school).

## 8. Future Work

- Prove or refute Loeper–Villani in dimension $3$; Figalli–Rifford–Villani suggest attacking it through the "extended" MTW condition on the whole tangent injectivity domain rather than pointwise.
- Find a curvature-plus-focal-structure criterion sufficient for $\mathrm{A3w}$, e.g. for manifolds with $\mathrm{Sec}\ge\delta>0$ and injectivity radius close to the Bonnet–Myers bound.
- Determine whether $\mathrm{A3w}$ is closed under Riemannian products in general (known for spheres, open in general) and under quotients by isometric group actions.
- Establish sharp Hölder exponents and $W^{2,p}$ estimates under $\mathrm{A3w}$ only, in the spirit of De Philippis–Figalli's $W^{2,1+\varepsilon}$ theory for the classical Monge–Ampère equation.
- Develop a stability theory: does $\mathrm{A3w}$ pass to Gromov–Hausdorff limits of manifolds with uniform bounds?

## 9. Key References

- **[Foundational]** X.-N. Ma, N. S. Trudinger, X.-J. Wang. *Regularity of potential functions of the optimal transportation problem.* Archive for Rational Mechanics and Analysis 177 (2005), 151–183.
- **[Foundational]** G. Loeper. *On the regularity of solutions of optimal transportation problems.* Acta Mathematica 202 (2009), 241–283.
- **[Foundational]** L. A. Caffarelli. *The regularity of mappings with a convex potential.* Journal of the AMS 5 (1992), 99–104.
- **[Structural]** Y.-H. Kim, R. J. McCann. *Continuity, curvature, and the general covariance of optimal transportation.* Journal of the European Mathematical Society 12 (2010), 1009–1040.
- **[Counterexample]** Y.-H. Kim. *Counterexamples to continuity of optimal transportation on positively curved Riemannian manifolds.* International Mathematics Research Notices 2008, art. rnn120.
- **[SOTA]** G. Loeper, C. Villani. *Regularity of optimal transport in curved geometry: the nonfocal case.* Duke Mathematical Journal 151 (2010), 431–485.
- **[SOTA]** A. Figalli, L. Rifford, C. Villani. *Nearly round spheres look convex.* American Journal of Mathematics 134 (2012), 109–139.
- **[SOTA]** A. Figalli, Y.-H. Kim, R. J. McCann. *Regularity of optimal transport maps on multiple products of spheres.* Journal of the European Mathematical Society 15 (2013), 1131–1166.
- **[SOTA]** A. Figalli, Y.-H. Kim, R. J. McCann. *Hölder continuity and injectivity of optimal maps.* Archive for Rational Mechanics and Analysis 209 (2013), 747–795.
- **[SOTA]** N. Guillen, J. Kitagawa. *Pointwise estimates and regularity in geometric optics and other generated Jacobian equations.* Communications on Pure and Applied Mathematics 70 (2017), 1146–1220.
- **[Survey]** G. De Philippis, A. Figalli. *The Monge–Ampère equation and its link to optimal transportation.* Bulletin of the AMS 51 (2014), 527–580.
- **[Survey/Book]** C. Villani. *Optimal Transport: Old and New.* Grundlehren der mathematischen Wissenschaften 338, Springer, 2009 (Chapter 12).
- **[Book]** A. Figalli. *The Monge–Ampère Equation and Its Applications.* Zurich Lectures in Advanced Mathematics, EMS, 2017.

## 10. Worked Example / Concrete Special Case

**Translation-invariant costs.** Take $c(x,y)=h(x-y)$ on $\mathbb R^n$ with $h$ smooth and $D^2h>0$. Then $c_{i,j}=-\partial_{ij}h$, $c^{i,j}=-(D^2h)^{-1}_{ij}$, and $c_{ij,k}=-\partial_{ijk}h$, $c_{ij,rs}=\partial_{ijrs}h$. Substituting into $\mathfrak S_c$ and writing $\bar\eta=(D^2h)^{-1}\eta$:
$$\mathfrak S_c(\xi,\eta)=-D^4h(\xi,\xi,\bar\eta,\bar\eta)+3\,D^3h(\xi,\xi,\cdot)\,(D^2h)^{-1}\,D^3h(\bar\eta,\bar\eta,\cdot).$$

**Case 1: quadratic cost.** $h(z)=\tfrac12|z|^2$. Then $D^3h=0$ and $D^4h=0$, so
$$\mathfrak S_c\equiv 0 .$$
$\mathrm{A3w}$ holds, with equality on every null plane; $\mathrm{A3s}$ fails everywhere. This is the exact reason Caffarelli's theory needs convexity of the target as a separate hypothesis: the MTW term contributes nothing, so all the geometric information must come from the domain. Removing convexity — Caffarelli's two-half-ball target — produces a discontinuous optimal map even though $\mathrm{A3w}$ holds.

**Case 2: the sphere near the diagonal.** For $(M,g)$ with $c=d_g^2/2$, expand at $y=x$ using Jacobi fields. For unit $\xi\perp\eta$,
$$\mathfrak S_c(x,x)(\xi,\eta)=\tfrac43\,\mathrm{Sec}_x(\xi\wedge\eta).$$
Two consequences follow immediately:

- If $\mathrm{Sec}_x(\xi\wedge\eta)<0$ for some plane, $\mathrm{A3w}$ fails, so by Loeper's necessity theorem there are $C^\infty$ densities bounded above and below on $M$ whose optimal map is not continuous. Hyperbolic space and any negatively curved compact surface are therefore excluded.
- On $S^n$ with $\mathrm{Sec}\equiv1$, the diagonal value is $\tfrac43>0$. Loeper's theorem upgrades this to the *global, off-diagonal* bound $\mathfrak S_c(x,y)(\xi,\eta)\ge\tfrac23|\xi|^2|\eta|^2$ for all $y$ outside the cut locus of $x$ — a statement that the pointwise diagonal computation alone cannot give, and precisely the step that has never been carried out for a general manifold.

**Case 3: a degenerate product.** On $S^2\times S^2$ take $\xi=(\xi_1,0)$ tangent to the first factor and $\eta=(0,\eta_2)$ tangent to the second. The cost splits, $c=c_1\oplus c_2$, so all mixed derivatives vanish and $\mathfrak S_c(\xi,\eta)=0$. Hence $S^2\times S^2$ satisfies $\mathrm{A3w}$ but never $\mathrm{A3s}$ — the case Figalli–Kim–McCann had to handle by an argument that does not use any strict positivity, and the model for why the degenerate condition is the hard one.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*