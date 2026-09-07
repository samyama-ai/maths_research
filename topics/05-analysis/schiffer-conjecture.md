---
id: 05-analysis/schiffer-conjecture
title: "Schiffer's Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Schiffer's Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/schiffer-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ ($n \ge 2$) be a bounded domain with connected boundary $\partial\Omega$ of class $C^1$ (or Lipschitz; the boundary is then forced to be real-analytic). Suppose there exist $\alpha > 0$ and a nonconstant $u \in C^2(\overline{\Omega})$ with

$$\Delta u + \alpha u = 0 \ \text{ in } \Omega, \qquad \frac{\partial u}{\partial \nu} = 0 \ \text{ on } \partial\Omega, \qquad u = c \ \text{ (constant) on } \partial\Omega .$$

**Conjecture (Schiffer).** Then $\Omega$ is a ball.

The system is overdetermined: a Neumann eigenfunction generically has non-constant boundary trace, so the extra Dirichlet condition should force rigidity. A complete solution is either a proof of the implication for all $n \ge 2$, or the exhibition of a single non-spherical $\Omega$ (with connected boundary) admitting such a pair $(\alpha, u)$. Both the connectedness of $\partial\Omega$ and $\alpha>0$ are essential hypotheses.

## 2. Mathematical Foundations

**Normalizations.** If $c = 0$ then $u$ solves both Dirichlet and Neumann homogeneous conditions, so by Holmgren's uniqueness theorem $u \equiv 0$; hence $c \neq 0$ and one may take $c = 1$. Green's identity gives

$$\alpha \int_\Omega u \, dx = -\int_\Omega \Delta u \, dx = -\int_{\partial\Omega} \partial_\nu u \, d\sigma = 0 \implies \int_\Omega u\,dx = 0,$$

so $u$ changes sign and $\alpha$ is a nonzero Neumann eigenvalue: $\alpha \in \{\mu_1(\Omega) \le \mu_2(\Omega) \le \cdots\}$, the spectrum of $-\Delta$ with $\partial_\nu u = 0$.

**Pompeiu property.** $\Omega$ has the *Pompeiu property* if for $f \in C(\mathbb{R}^n)$,

$$\int_{\sigma(\Omega)} f \, dx = 0 \quad \text{for every rigid motion } \sigma \in M(n) \implies f \equiv 0 .$$

By Brown–Schreiber–Taylor (1973), spectral synthesis for $M(n)$-invariant subspaces shows that $\Omega$ **fails** the Pompeiu property iff the Fourier–Laplace transform $\widehat{\chi_\Omega}$ vanishes on a complex sphere $\{\zeta \in \mathbb{C}^n : \zeta\cdot\zeta = \alpha\}$ for some $\alpha>0$:

$$\widehat{\chi_\Omega}(\zeta) = \int_\Omega e^{-i \zeta \cdot x}\,dx = 0 \qquad \text{for all } \zeta \text{ with } \textstyle\sum_j \zeta_j^2 = \alpha .$$

**Equivalence (Williams, 1976/1981).** For bounded Lipschitz $\Omega$ with connected boundary, failure of the Pompeiu property is equivalent to solvability of the overdetermined system in §1; moreover $\partial\Omega$ must then be real-analytic and diffeomorphic to $S^{n-1}$. So *Schiffer's conjecture $\Leftrightarrow$ the Pompeiu conjecture: the ball is the only bounded domain with connected Lipschitz boundary failing the Pompeiu property.*

**Ball computation.** For $\Omega = B_R \subset \mathbb{R}^n$, the radial solution of $\Delta u + \alpha u = 0$ is $u(r) = r^{1-n/2} J_{n/2-1}(\sqrt{\alpha}\, r)$, and from $\frac{d}{dz}\big(z^{-\nu} J_\nu(z)\big) = -z^{-\nu}J_{\nu+1}(z)$ one gets $u'(R)=0 \iff \sqrt{\alpha}R = j_{n/2,k}$, the $k$-th positive zero of $J_{n/2}$. Consistently,

$$\widehat{\chi_{B_R}}(\xi) = (2\pi)^{n/2} R^{n/2} \frac{J_{n/2}(R|\xi|)}{|\xi|^{n/2}},$$

which vanishes on the spheres $|\xi| = j_{n/2,k}/R$. Balls are therefore genuine solutions, and Serrin-type moving-plane arguments — which settle the analogous Dirichlet problem $\Delta u = -1$, $u=0$, $\partial_\nu u = $ const (Serrin 1971; Weinberger 1971) — are the model one wishes to imitate.

## 3. History & State of the Art (SOTA)

- **1929** — D. Pompeiu poses the integral-geometric question; his original claim that every planar domain has the property is flawed.
- **1944** — L. Chakalov observes discs fail the property, via the Bessel zeros above.
- **1973** — Brown, Schreiber & Taylor give the Fourier/spectral-synthesis characterization, moving the problem into complex analysis of $\widehat{\chi_\Omega}$ on the complex quadric.
- **mid-1970s** — M. Schiffer formulates the overdetermined Neumann eigenvalue version (transmitted through Yau's problem list, Problem 80).
- **1976–1981** — S. A. Williams proves the equivalence and real-analyticity of $\partial\Omega$.
- **1980–1987** — C. A. Berenstein, and Berenstein–Yang, obtain the first-eigenvalue case and multi-eigenvalue rigidity.
- **1993–1994** — Garofalo–Segàla and Ebenfelt settle large classes of planar analytic boundaries using conformal maps and propagation of singularities in the complex Cauchy problem.
- **2023–present** — Enciso, Fernández, Ruiz & Sicbaldi construct counterexamples to the *Schiffer problem on the cylinder and on $S^2$*, showing the Euclidean statement cannot follow from purely local/curvature-free arguments.

No counterexample in $\mathbb{R}^n$ is known, and no complete proof exists in any dimension.

## 4. Partial Results / Verified Cases

- **Regularity reduction.** Any counterexample has real-analytic boundary homeomorphic to $S^{n-1}$ (Williams 1981). Corners, cusps, merely-$C^\infty$-non-analytic boundaries, and multiply-connected boundaries of a candidate are all excluded a priori.
- **First eigenvalue.** If $\alpha = \mu_1(\Omega)$, the first nonzero Neumann eigenvalue, then $\Omega$ is a ball (Berenstein 1980; further symmetry theorems by Aviles 1986). Extensions cover $\alpha$ small in a spectral-gap sense.
- **Multiple eigenvalues.** If the overdetermined system is solvable for infinitely many distinct $\alpha_k$ — equivalently $\widehat{\chi_\Omega}$ vanishes on infinitely many spheres — then $\Omega$ is a ball (Berenstein; Berenstein–Yang 1987).
- **Planar analytic classes.** For simply connected $\Omega \subset \mathbb{R}^2$ whose Riemann map $\varphi: \mathbb{D}\to\Omega$ is a polynomial, or whose boundary is a "trigonometric-polynomial" curve of low degree, only the disc occurs (Garofalo–Segàla 1993, 1994). Ebenfelt (1993, 1994) settles domains with algebraic boundary and quadrature-type domains by tracking singularities of the analytic continuation of the Cauchy problem for $\Delta u+\alpha u=0$.
- **Symmetry hypotheses.** If $\Omega$ is assumed invariant under a sufficiently large subgroup of $O(n)$, or is a domain of revolution with additional structure, the conclusion follows.
- **Non-Euclidean failure.** On the flat cylinder $S^1\times\mathbb{R}$ and on the round $S^2$, non-spherical domains with connected analytic boundary solving the Schiffer system exist (Enciso–Fernández–Ruiz–Sicbaldi, 2023).

## 5. Principal Obstacles

- **Moving planes does not apply.** Serrin's method needs the maximum principle for the linearized operator; here $u$ changes sign ($\int_\Omega u = 0$) and $\Delta + \alpha$ with $\alpha \ge \mu_1$ is not coercive, so reflections give no comparison. This is the single largest structural barrier.
- **Bifurcation gives no obstruction.** Linearizing the overdetermined problem about $B_R$ at $\alpha = (j_{n/2,k}/R)^2$ produces nontrivial kernel elements (spherical harmonics of degree $m$ satisfying a Bessel resonance condition), so the ball is *not* isolated at linear order. Only higher-order/nonlocal information can exclude nearby analytic perturbations — and the sphere/cylinder counterexamples show the analogous obstruction genuinely vanishes in curved settings.
- **Entire-function rigidity.** In the Fourier formulation one must show that $\widehat{\chi_\Omega}$, an entire function of exponential type on $\mathbb{C}^n$, cannot vanish on a whole complex quadric unless $\Omega$ is a ball. Zero sets of exponential-type functions in several variables are poorly controlled; classical Paley–Wiener theory constrains growth, not the geometry of the zero variety.
- **Loss of conformal tools above $n=2$.** The successful planar proofs use Riemann maps and analytic continuation of the Cauchy data across $\partial\Omega$; for $n \ge 3$ there is no substitute, and the Cauchy–Kovalevskaya continuation loses control of singularities.
- **No variational characterization.** Unlike Serrin's problem (which arises from a torsion-functional identity, Weinberger's $P$-function), no known integral identity or $P$-function is monotone for the Schiffer system.

## 6. The Gap

Proven: rigidity when $\alpha$ is the *lowest* nonzero Neumann eigenvalue, or when the system holds for *infinitely many* eigenvalues, or when $\partial\Omega$ lies in a restricted algebraic/conformal-polynomial class in dimension 2. Conjectured: rigidity for a *single, arbitrary* eigenvalue $\alpha = \mu_k(\Omega)$, $k$ large, in *every* dimension, for an *arbitrary* real-analytic connected boundary.

The exact barrier: for high $k$ the eigenfunction oscillates on scale $\alpha^{-1/2}$, and the nodal set meets $\partial\Omega$ in a complicated pattern; all known rigidity mechanisms (maximum principle, first-eigenvalue variational characterization, low-degree conformal expansion) are uniform-in-$k$ blind. One needs either (i) a $k$-uniform integral identity forcing $\partial\Omega$ to have constant mean curvature, or (ii) a bound on the zero variety of $\widehat{\chi_\Omega}$ ruling out an entire complex sphere.

## 7. Current Research (as of June 2026)

- **Counterexamples in curved/periodic settings.** Enciso, Fernández, Ruiz and Sicbaldi (Madrid–Granada school) built non-trivial Schiffer domains on $S^2$ and the cylinder by local bifurcation from degenerate spherical caps/bands. Ongoing work asks whether analogous constructions can survive in $\mathbb{R}^n$ under weakened hypotheses (disconnected boundary, unbounded periodic domains). *(frontier — verify)*
- **Overdetermined problems by gluing/perturbation.** Techniques from Fall–Minlend–Weth and Schlenk–Sicbaldi (nontrivial extremal/Serrin domains) are being adapted to sign-changing eigenfunctions.
- **Complex-analytic continuation.** Continuation of the line of Ebenfelt and Khavinson–Lundberg on the Cauchy problem for the Helmholtz operator and quadrature domains, aiming at all planar algebraic boundaries.
- **Claimed proofs.** A. G. Ramm has posted several claimed resolutions of the Pompeiu/Schiffer conjecture; these are not accepted by the community and gaps have been reported. *(frontier — verify)*
- **Numerics.** Shape-optimization searches over analytic boundary parametrizations minimizing the residual $\|u - \bar u\|_{L^2(\partial\Omega)}$ over Neumann eigenfunctions consistently return only the ball.

## 8. Future Work

- Establish an integral identity (a Rellich–Pohozaev variant with a $k$-independent sign) forcing constant mean curvature of $\partial\Omega$, then invoke Alexandrov's theorem.
- Determine whether the Enciso–Fernández–Ruiz–Sicbaldi mechanism has an obstruction that is genuinely Euclidean — isolating what property of $\mathbb{R}^n$ (flatness, non-compactness, scaling) kills it, which would suggest the right proof.
- Prove the two-eigenvalue case: if the system is solvable for two distinct $\alpha_1 \ne \alpha_2$, is $\Omega$ a ball? This would sharpen Berenstein–Yang from "infinitely many" to a finite condition.
- Settle $n = 2$ for all real-analytic boundaries by controlling singularity propagation for the Helmholtz Cauchy problem in $\mathbb{C}^2$.
- Study the discrete/graph and Riemannian analogues to identify which axioms the rigidity really needs.

## 9. Key References

- **[Foundational]** S. A. Williams. *A partial solution of the Pompeiu problem.* Mathematische Annalen 223 (1976), 183–190.
- **[Foundational]** S. A. Williams. *Analyticity of the boundary for Lipschitz domains without the Pompeiu property.* Indiana University Mathematics Journal 30 (1981), 357–369.
- **[Foundational]** L. Brown, B. M. Schreiber, B. A. Taylor. *Spectral synthesis and the Pompeiu problem.* Annales de l'Institut Fourier 23 (1973), 125–154.
- **[Foundational]** J. Serrin. *A symmetry problem in potential theory.* Archive for Rational Mechanics and Analysis 43 (1971), 304–318; H. F. Weinberger, *Remark on the preceding paper of Serrin*, same volume, 319–320.
- **[Partial]** C. A. Berenstein. *An inverse spectral theorem and its relation to the Pompeiu problem.* Journal d'Analyse Mathématique 37 (1980), 128–144.
- **[Partial]** C. A. Berenstein, P. C. Yang. *An inverse Neumann problem.* Journal für die reine und angewandte Mathematik 382 (1987), 1–21.
- **[Partial]** P. Aviles. *Symmetry theorems related to Pompeiu's problem.* American Journal of Mathematics 108 (1986), 1023–1036.
- **[Partial]** N. Garofalo, F. Segàla. *Univalent functions and the Pompeiu problem.* Transactions of the American Mathematical Society 346 (1994), 137–146.
- **[Partial]** P. Ebenfelt. *Propagation of singularities from singular and infinite points in certain complex-analytic Cauchy problems and an application to the Pompeiu problem.* Duke Mathematical Journal 73 (1994), 561–582.
- **[SOTA / Recent]** A. Enciso, A. J. Fernández, D. Ruiz, P. Sicbaldi. *The Schiffer problem on the cylinder and on the 2-sphere.* arXiv:2306.03449 (2023).
- **[Survey]** L. Zalcman. *A bibliographic survey of the Pompeiu problem.* In: B. Fuglede et al. (eds.), *Approximation by Solutions of Partial Differential Equations*, NATO ASI Series C 365, Kluwer, 1992, 185–194; with *Supplementary bibliography*, Contemporary Mathematics 278 (2001), 69–74.
- **[Survey]** S.-T. Yau (ed.). *Problem section*, in *Seminar on Differential Geometry*, Annals of Mathematics Studies 102, Princeton University Press, 1982 (Problem 80).

## 10. Worked Example / Concrete Special Case

**The unit disc, $n=2$, $R=1$.** Seek a radial solution of $\Delta u + \alpha u = 0$ on $\mathbb{D}$:

$$u'' + \tfrac1r u' + \alpha u = 0 \implies u(r) = J_0(\sqrt{\alpha}\, r).$$

Since $J_0' = -J_1$, the Neumann condition is $u'(1) = -\sqrt{\alpha}\,J_1(\sqrt{\alpha}) = 0$, i.e. $\sqrt{\alpha} = j_{1,k}$. Taking $k=1$, $j_{1,1} = 3.8317059\ldots$, so

$$\alpha = j_{1,1}^2 = 14.6819\ldots, \qquad u\big|_{\partial\mathbb{D}} = J_0(3.83171) = -0.402759\ldots = c \neq 0 .$$

Being radial, $u$ is automatically constant on $\partial\mathbb{D}$, so all three conditions of §1 hold. Consistency check with §2: $\int_{\mathbb{D}} u = 2\pi \int_0^1 J_0(j_{1,1}r)\,r\,dr = 2\pi\, J_1(j_{1,1})/j_{1,1} = 0$. ✓ Equivalently $\widehat{\chi_{\mathbb{D}}}(\xi) = 2\pi J_1(|\xi|)/|\xi|$ vanishes on $|\xi| = j_{1,1}$, so the disc fails the Pompeiu property: the function $f(x) = J_0(j_{1,1}|x - p|)$ has zero integral over *every* unit disc centred at distance-preserving images, yet $f \not\equiv 0$.

**Why boundary connectedness is assumed.** On an annulus $A = \{r_1 < |x| < r_2\}$ the general radial solution is $u = A J_0(\sqrt\alpha r) + B Y_0(\sqrt\alpha r)$. Imposing $u'(r_1) = u'(r_2) = 0$ and $u(r_1) = u(r_2)$ gives three equations in the three effective unknowns $(B/A,\ \alpha,\ r_2/r_1)$ — a determined system with discrete solutions. Non-spherical solutions of this relaxed problem are therefore expected, which is exactly why the conjecture requires $\partial\Omega$ connected. *(frontier — verify the explicit annular parameters numerically.)*

**What a disproof would look like.** Perturb $\partial B_1$ as $r(\theta) = 1 + \varepsilon\cos(m\theta)$. To first order in $\varepsilon$, the linearized system is solvable when $J_m(\sqrt{\alpha}) $ and the Bessel resonance $\big(\alpha - m^2\big)J_0(\sqrt\alpha) \cdot$ (mode coupling) degenerate simultaneously; such degeneracies do occur, so the ball is not linearly isolated. A counterexample requires pushing such a formal branch to a genuine analytic domain — precisely the step that succeeds on $S^2$ and the cylinder and is unresolved in $\mathbb{R}^n$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*