---
id: 06-pdes/perona-malik-well-posedness
title: "Perona Malik Well Posedness"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Perona–Malik Well-Posedness

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/perona-malik-well-posedness` · **Status:** open

## 1. Problem Statement / Conjecture

The Perona–Malik equation is the forward–backward quasilinear diffusion

$$
u_t \;=\; \operatorname{div}\!\big(g(|\nabla u|^2)\,\nabla u\big),
\qquad g(s) = \frac{1}{1+s/K^2},
$$

on a bounded domain $\Omega\subset\mathbb{R}^n$ with homogeneous Neumann boundary conditions and initial datum $u_0$. It was introduced as an edge-preserving image smoother: diffusion is strong where $|\nabla u|\ll K$ and suppressed where $|\nabla u|\gg K$.

**The open problem.** Identify a solution concept and a class of initial data for which the Cauchy–Neumann problem is *well posed* — existence, uniqueness, and continuous dependence on $u_0$ — or prove that no such concept exists for generic data.

Concretely, three questions remain open:

1. **(Existence)** For $u_0 \in C^\infty(\bar\Omega)$ with $\|\nabla u_0\|_\infty > K$ somewhere, does a global weak solution exist in dimension $n \ge 2$?
2. **(Uniqueness)** In $n=1$, existence of infinitely many Lipschitz weak solutions is known for a large class of data. Is there a selection principle (entropy, variational, or limit-of-schemes) that singles out exactly one?
3. **(Convergence of schemes)** Does the standard explicit finite-difference discretization converge, as the mesh $h\to 0$, to a solution of the PDE — and if so, of which PDE?

A complete resolution must specify the function space, the notion of solution (distributional, Young-measure, gradient-flow, or measure-valued), and prove the three well-posedness properties, or exhibit a rigorous obstruction.

## 2. Mathematical Foundations

Write the flux in one space dimension. With $\phi(p) = p\,g(p^2)$ and $K=1$,

$$
\phi(p) = \frac{p}{1+p^2}, \qquad \phi'(p) = \frac{1-p^2}{(1+p^2)^2},
$$

so the 1D equation $u_t = \big(\phi(u_x)\big)_x = \phi'(u_x)\,u_{xx}$ is

- **forward parabolic** on the *subcritical* region $\{|u_x| < 1\}$, where $\phi' > 0$;
- **backward parabolic** on the *supercritical* region $\{|u_x| > 1\}$, where $\phi' < 0$.

The set $\{|u_x| = 1\}$ is the *singular set*. Backward parabolicity makes the problem ill posed in the sense of Hadamard: linearizing about a linear profile $u = ax$ with $|a| > 1$, the Fourier mode $e^{ikx}$ grows like $e^{|\phi'(a)|k^2 t}$, unbounded in $k$.

**Variational structure.** The equation is the formal $L^2$ gradient flow of

$$
E[u] = \tfrac{1}{2}\int_\Omega W(|\nabla u|)\,dx, \qquad W(p) = \log(1+p^2),
$$

a non-convex, sublinearly growing energy. Because $W$ has an affine-in-$p$ growth deficit and $W''(p) = \phi'(p)$ changes sign, $E$ is not lower semicontinuous on $W^{1,1}$; its relaxation is $E^{**}[u] = 0$ for the convexified integrand $W^{**} \equiv 0$ ($W$ is concave for $p>1$ and $\inf W'' <0$; the convex envelope of $W$ on $[0,\infty)$ is identically $W(0)=0$ since $W$ is bounded above by an affine function with slope $0$ in the limit). Consequently the minimizing-movement scheme has no classical limit and minimizing sequences oscillate — the analytic root of the "staircasing" seen numerically.

**Young-measure formulation.** A parametrized measure $\nu = (\nu_{x,t})$ on $\mathbb{R}$ with barycenter constraints is a *Young-measure solution* if $u_t = \partial_x \langle \nu_{x,t}, \phi\rangle$ and $u_x = \langle \nu_{x,t}, \mathrm{id}\rangle$ in $\mathcal{D}'$. This relaxes the pointwise flux to an averaged flux and restores existence at the price of massive non-uniqueness.

**Regularized comparison.** The Catté–Lions–Morel–Coll model replaces $|\nabla u|$ by $|\nabla (G_\sigma * u)|$ for a Gaussian $G_\sigma$; the resulting problem is well posed for every $\sigma>0$, but all known estimates degenerate as $\sigma\to 0$.

## 3. History & State of the Art (SOTA)

- **1990.** Pietro Perona and Jitendra Malik propose the model in *IEEE Trans. PAMI*, observing empirically that the discretized scheme is stable despite formal ill-posedness.
- **1983.** Klaus Höllig had already shown, for a cubic-type forward–backward heat equation, existence of a continuum of weak solutions with the same data — the template for later PM non-uniqueness proofs.
- **1992.** Catté–Lions–Morel–Coll prove existence/uniqueness for the Gaussian-regularized model, the standard "fix".
- **1994–1997.** Plotnikov constructs Young-measure solutions by viscosity limits; Kichenassamy formulates the "Perona–Malik paradox": no reasonable distributional solution can exist for smooth supercritical data, so the discrete scheme cannot be approximating the PDE in the naive sense.
- **1998.** Kawohl and Kutev establish comparison and maximum principles and local classical existence/uniqueness for data with $\|u_0'\|_\infty < 1$ (fully subcritical), plus non-existence of global classical solutions once the gradient exceeds threshold.
- **2001.** Esedoḡlu analyzes the *semi-discrete* PM scheme, showing it is well posed and that its solutions converge, on the discrete level, to piecewise-constant "staircase" profiles — explaining the empirical stability without resolving the continuum limit.
- **2006–2011.** K. Zhang, and independently Ghisi–Gobbino, produce infinitely many Lipschitz weak solutions in 1D, and construct classes of local *classical* solutions with genuinely supercritical regions.
- **2008.** Bellettini–Novaga–Paolini–Tornese, and Bellettini–Fusco, study $\Gamma$-limits of singularly perturbed PM functionals and the convergence of discrete schemes.

Status as of 2026: existence is understood only in weak/relaxed senses; uniqueness fails in every setting where existence has been proved; $n \ge 2$ is essentially untouched.

## 4. Partial Results / Verified Cases

- **Subcritical data, any $n$.** If $\|\nabla u_0\|_{L^\infty} < K$, the equation is uniformly parabolic on the relevant range and admits a unique local classical solution; Kawohl–Kutev (1998) prove in $n=1$ that the constraint $\|u_x(\cdot,t)\|_\infty < K$ propagates, giving global classical well-posedness.
- **$n=1$, non-uniqueness.** Zhang (*Calc. Var. PDE* 26, 2006) constructs infinitely many Lipschitz weak solutions with $u(\cdot,0)=u_0$ for a dense set of smooth $u_0$ having supercritical intervals, using convex-integration / differential-inclusion methods (Müller–Šverák type).
- **$n=1$, classical solutions with supercritical regions.** Ghisi–Gobbino (*Trans. AMS* 361, 2009) exhibit a class of local classical solutions where $\{|u_x|>K\}$ is nonempty, so the transition region need not be instantaneously singular.
- **$n=1$, gradient estimates.** Ghisi–Gobbino (*Math. Ann.* 337, 2007) obtain estimates on $\|u_x\|$ for the singularly perturbed problem $u_t=(\phi(u_x))_x + \varepsilon u_{xxt}$, uniform in $\varepsilon$ on the subcritical part.
- **Young-measure solutions.** Plotnikov (1994) and Taheri–Tang–Zhang (*J. Math. Anal. Appl.* 2005) prove global existence of Young-measure solutions in 1D for $u_0 \in W^{1,\infty}$, along with instability: the measures generically split onto the two branches $\{\phi'>0\}$ and $\{\phi'<0\}$.
- **Regularized models.** Catté–Lions–Morel–Coll: unique global smooth solution for every $\sigma>0$, all $n\ge 1$. Barenblatt–Bertsch–Dal Passo–Ughi (*SIAM J. Math. Anal.* 24, 1993): well-posedness for the pseudoparabolic regularization $u_t = (\phi(u_x))_x + \varepsilon u_{xxt}$.
- **Discrete schemes.** Esedoḡlu (*CPAM* 54, 2001): the semi-discrete scheme with fixed mesh $h>0$ has a unique solution, and staircase states are stable; Bellettini–Novaga–Paolini–Tornese (*JDE* 245, 2008) identify limits of discrete schemes under mesh–time coupling.

## 5. Principal Obstacles

- **No a priori gradient bound.** Energy $E[u]$ is bounded but controls only $\int \log(1+|\nabla u|^2)$, which does not embed into any $L^p$ space of gradients with $p\ge1$ compactly; minimizing sequences can concentrate gradient on null sets. Standard parabolic $L^p$ or De Giorgi–Nash–Moser theory needs uniform ellipticity, which fails by construction.
- **Loss of compactness in the flux.** Even with $u^\varepsilon \to u$ uniformly, $\phi(u^\varepsilon_x) \rightharpoonup \bar\phi \ne \phi(u_x)$ because $\phi$ is non-monotone. Div–curl / compensated compactness (Murat–Tartar) requires the flux to be monotone or the Young measure to be a Dirac mass; neither holds here, and the two-branch structure of $\phi^{-1}$ leaves the barycenter under-determined.
- **Backward parabolicity destroys uniqueness by design.** Convex integration (Zhang; after Müller–Šverák, Dacorogna–Marcellini) exploits the non-rank-one-convexity of the associated differential inclusion to insert arbitrarily many oscillating solutions. Any well-posedness theory must therefore *forbid* these solutions by a selection criterion, and no criterion is known that is both natural and sufficient — entropy conditions of hyperbolic type have no obvious analogue for a second-order operator.
- **Dimension $\ge 2$.** In 1D, $u_x$ is a scalar and the transition set is codimension 1; in $n\ge2$ the direction of $\nabla u$ matters, the operator is anisotropic (parabolic along level sets, possibly backward in the gradient direction), and no comparison principle or Young-measure existence result is available.
- **Scheme–PDE mismatch.** The discrete scheme is stable but its limit as $h\to 0$ depends on the coupling between $h$ and the time step $\tau$; there is no proof that any coupling produces a solution of the continuum PDE, so numerics cannot be used to certify a solution concept.

## 6. The Gap

Proved: (a) classical well-posedness for strictly subcritical data; (b) existence of relaxed (Young-measure / Lipschitz weak) solutions in $n=1$; (c) uniqueness *fails* for those relaxed classes; (d) well-posedness of every known regularization at fixed regularization parameter.

Wanted: a solution concept $\mathcal{S}$ that (i) contains the classical solutions of (a), (ii) admits a global existence proof for supercritical data, and (iii) is *uniquely* determined. The precise missing step is a **compactness-plus-selection theorem**: a uniform-in-$\varepsilon$ estimate on $\phi(u_x^\varepsilon)$ strong enough to pass to the limit in the flux, together with a criterion (an entropy inequality, a maximal-monotone-graph reformulation, or a $\Gamma$-limit characterization) that eliminates the convex-integration solutions. Equivalently: show that the singular limit $\sigma\to0$ of the Catté–Lions–Morel–Coll model, or $\varepsilon\to0$ of the pseudoparabolic model, exists and is independent of the regularization. Regularization-independence is exactly what is unproved — and there is evidence from numerics that different regularizations select different limits, which would make the answer "no well-posed limit exists".

## 7. Current Research (as of June 2026)

- **Forward–backward parabolic equations as maximal monotone graphs.** Smarrazzo, Tesei and collaborators pursue measure-valued and entropy formulations for $u_t = (\phi(u))_{xx}$-type equations, seeking uniqueness via a two-phase (Radon-measure) representation. Extending this to the gradient-dependent PM operator is active. *(frontier — verify)*
- **Nonlocal replacements.** Guidotti's nonlocal PM variants (e.g. replacing $|\nabla u|$ by a fractional or Hilbert-transform-mediated quantity) are provably well posed while retaining edge enhancement; the research question is whether they converge to a canonical PM limit.
- **Convex integration inventory.** Groups working on differential inclusions (following Müller–Šverák, De Lellis–Székelyhidi) are mapping exactly *how large* the non-uniqueness set is — whether the wild solutions are non-generic in a Baire or measure sense, which would motivate a selection principle. *(frontier — verify)*
- **Numerical analysis of the $h,\tau \to 0$ double limit.** Bellettini–Novaga–Paolini and successors compute regimes where staircase width scales with $h$; the conjecture that the limit is a *total-variation-like* flow rather than PM itself is being tested. *(frontier — verify)*
- **$n\ge2$ existence.** No group has announced a Young-measure existence result in two dimensions; this remains the cleanest open target.

## 8. Future Work

1. Prove or disprove **regularization independence**: compare $\lim_{\sigma\to0}$ (spatial mollification) and $\lim_{\varepsilon\to0}$ (pseudoparabolic) for a single supercritical datum; a single explicit example where they differ settles the ill-posedness question negatively and definitively.
2. Construct a **Young-measure solution in $n=2$** for radially symmetric data, where the anisotropy collapses to a scalar problem.
3. Identify an **entropy/selection criterion**: seek a family of functionals $\eta(u_x)$ with $\partial_t \eta(u_x) \le \partial_x(\cdot)$ satisfied by regularized limits but violated by convex-integration solutions.
4. Characterize the **$\Gamma$-limit** of $E_\varepsilon[u]=\int W(|u_x|) + \varepsilon^2 |u_{xx}|^2$ and its gradient flow (Bellettini–Fusco programme) in dimension $\ge 2$.
5. Determine whether the discrete PM scheme's limit is the **total variation flow**, which would explain staircasing as the correct continuum behaviour rather than a numerical artifact.

## 9. Key References

- **[Foundational]** P. Perona, J. Malik. *Scale-Space and Edge Detection Using Anisotropic Diffusion.* IEEE Transactions on Pattern Analysis and Machine Intelligence, 12(7):629–639, 1990.
- **[Foundational]** K. Höllig. *Existence of Infinitely Many Solutions for a Forward Backward Heat Equation.* Transactions of the American Mathematical Society, 278:299–316, 1983.
- **[Foundational]** F. Catté, P.-L. Lions, J.-M. Morel, T. Coll. *Image Selective Smoothing and Edge Detection by Nonlinear Diffusion.* SIAM Journal on Numerical Analysis, 29(1):182–193, 1992.
- **[Foundational]** S. Kichenassamy. *The Perona–Malik Paradox.* SIAM Journal on Applied Mathematics, 57(5):1328–1342, 1997.
- **[Theory]** B. Kawohl, N. Kutev. *Maximum and Comparison Principle for One-Dimensional Anisotropic Diffusion.* Mathematische Annalen, 311:107–123, 1998.
- **[Theory]** G. I. Barenblatt, M. Bertsch, R. Dal Passo, M. Ughi. *A Degenerate Pseudoparabolic Regularization of a Nonlinear Forward-Backward Heat Equation Arising in the Theory of Heat and Mass Exchange in Stably Stratified Turbulent Shear Flow.* SIAM Journal on Mathematical Analysis, 24(6):1414–1439, 1993.
- **[SOTA / Recent]** S. Esedoḡlu. *An Analysis of the Perona–Malik Scheme.* Communications on Pure and Applied Mathematics, 54(12):1442–1487, 2001.
- **[SOTA / Recent]** K. Zhang. *Existence of Infinitely Many Solutions for the One-Dimensional Perona–Malik Model.* Calculus of Variations and Partial Differential Equations, 26:171–199, 2006.
- **[SOTA / Recent]** M. Ghisi, M. Gobbino. *Gradient Estimates for the Perona–Malik Equation.* Mathematische Annalen, 337:557–590, 2007.
- **[SOTA / Recent]** M. Ghisi, M. Gobbino. *A Class of Local Classical Solutions for the One-Dimensional Perona–Malik Equation.* Transactions of the American Mathematical Society, 361:6429–6446, 2009.
- **[SOTA / Recent]** G. Bellettini, M. Novaga, M. Paolini, C. Tornese. *Convergence of Discrete Schemes for the Perona–Malik Equation.* Journal of Differential Equations, 245(4):892–924, 2008.
- **[SOTA / Recent]** A. Taheri, Q. Tang, K. Zhang. *Young Measure Solutions and Instability of the One-Dimensional Perona–Malik Equation.* Journal of Mathematical Analysis and Applications, 308(2):467–490, 2005.
- **[Survey]** J. Weickert. *Anisotropic Diffusion in Image Processing.* B. G. Teubner, Stuttgart, 1998.
- **[Survey]** P. Guidotti. *Anisotropic Diffusions of Image Processing from Perona–Malik On.* Advanced Studies in Pure Mathematics, Vol. 67, Mathematical Society of Japan, 2015.

## 10. Worked Example / Concrete Special Case

Take $n=1$, $K=1$, $\Omega=(0,2\pi)$, $\phi(p)=p/(1+p^2)$.

**Step 1 — linear profiles are stationary.** For $u(x,t)=ax$, $u_{xx}=0$, so $u_t=\phi'(a)u_{xx}=0$. Every affine profile solves the equation exactly, for any slope $a$.

**Step 2 — linearize.** Set $u = ax + \delta\, v(x,t)$ and keep first order:
$$
v_t = \phi'(a)\,v_{xx}, \qquad \phi'(a)=\frac{1-a^2}{(1+a^2)^2}.
$$
With $v = e^{\lambda t}\sin(kx)$: $\lambda = -\phi'(a)k^2$.

**Step 3 — the two regimes, numerically.**

| slope $a$ | $\phi'(a)$ | $\lambda$ at $k=10$ | $\lambda$ at $k=100$ |
|---|---|---|---|
| $0.5$ (subcritical) | $+0.480$ | $-48.0$ | $-4800$ |
| $2$ (supercritical) | $-0.120$ | $+12.0$ | $+1200$ |
| $5$ (supercritical) | $-0.0355$ | $+3.55$ | $+355$ |

For $a=2$ the perturbation grows like $e^{0.12k^2 t}$. Fix any time $T>0$ and any $\delta>0$: choosing $k$ large makes $\|u(\cdot,T)-ax\|_\infty$ order one while $\|u(\cdot,0)-ax\|_\infty = \delta$. Continuous dependence on the initial datum therefore fails in every $C^m$ norm — this is the Hadamard instability at the heart of the problem.

**Step 4 — what the discrete scheme does instead.** On a grid $x_j = jh$ with $U_j \approx u(x_j)$ and the standard scheme
$$
\dot U_j = \frac{1}{h}\Big[\phi\Big(\tfrac{U_{j+1}-U_j}{h}\Big)-\phi\Big(\tfrac{U_j-U_{j-1}}{h}\Big)\Big],
$$
the admissible wavenumbers satisfy $k \le \pi/h$, so the growth rate is capped at $\approx 4|\phi'(a)|/h^2$: finite, hence the ODE system is well posed for each fixed $h$ (Esedoḡlu, 2001). Moreover a discrete "staircase" — $U_j$ constant on blocks with single-cell jumps of height $H$ — has each interior difference quotient either $0$ or $H/h$. If $H/h \gg 1$ then $\phi(H/h)\approx h/H \to 0$, so $\dot U_j = O(h/H \cdot h^{-1}) = O(1/H)$: the staircase is nearly stationary and the scheme freezes there.

**Step 5 — the gap made visible.** As $h\to0$ the jump-to-mesh ratio $H/h\to\infty$ and the limit object is a jump discontinuity of size $H$, not a function with $|u_x|$ finite. The limiting flux is $0$ across each jump, so the naive limit satisfies $u_t = 0$ — no diffusion at all — while the subcritical parts continue to diffuse. Whether this piecewise-frozen object is *the* solution, and whether a different regularization (Gaussian mollification with $\sigma = \sigma(h)$) selects a different one, is exactly the open question of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*