---
id: 06-pdes/chapman-enskog-expansion-convergence
title: "Chapman-Enskog Expansion Convergence for Kinetic Equations"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chapman-Enskog Expansion Convergence for Kinetic Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/chapman-enskog-expansion-convergence` · **Status:** open

## 1. Problem Statement / Conjecture

The Chapman–Enskog (CE) expansion is the formal power series in the Knudsen number $\varepsilon$ that produces hydrodynamics (Euler at order $\varepsilon^0$, Navier–Stokes–Fourier at $\varepsilon^1$, Burnett at $\varepsilon^2$, super-Burnett at $\varepsilon^3$) from a kinetic equation such as Boltzmann or BGK.

**The problem.** Characterize the analytic status of this series:

1. **Divergence/convergence.** For which kinetic models, collision kernels, and classes of macroscopic data does the CE series have positive radius of convergence in $\varepsilon$? The prevailing expectation is that it is generically *divergent* (asymptotic only), even for the linearized Boltzmann equation, and that its failure is not a technical artifact.
2. **Resummation.** If divergent, does the series nonetheless determine a genuine object — an invariant *hydrodynamic manifold* of the kinetic equation, obtained by Borel summation, Padé resummation, or direct solution of the invariance equation — and on what domain of wave numbers / amplitudes does that manifold exist?
3. **Truncation.** Are the truncations beyond Navier–Stokes (Burnett, super-Burnett) well posed? Bobylev's short-wave instability says no in their standard form; the question is whether a *canonical* correction exists that is both stable and asymptotically equivalent to all orders.

A complete resolution requires, for a specified kinetic equation: (a) a proof or disproof of nonzero radius of convergence, with the exact radius in the linear case; (b) a construction of the summed hydrodynamic manifold together with a well-posedness theory for the PDE it carries; (c) an error estimate comparing kinetic solutions to that PDE on physically relevant time scales.

## 2. Mathematical Foundations

Let $f(t,x,v)\ge 0$, $x\in\mathbb{T}^d$ or $\mathbb{R}^d$, $v\in\mathbb{R}^d$, solve the scaled Boltzmann equation

$$\partial_t f + v\cdot\nabla_x f = \frac{1}{\varepsilon} Q(f,f),\qquad
Q(f,f)(v)=\int_{\mathbb{R}^d}\!\int_{S^{d-1}} B(|v-v_*|,\theta)\,\big(f'f'_*-ff_*\big)\,d\sigma\,dv_*,$$

with $\varepsilon$ the Knudsen number. $Q$ has the collision invariants $1,v,|v|^2$ and $H$-theorem $\int Q(f,f)\log f\,dv\le 0$, with equality iff $f$ is Maxwellian $M_{\rho,u,T}$.

**Macroscopic projection.** $\Pi f=(\rho,\rho u,\tfrac12\rho|u|^2+\tfrac{d}{2}\rho T)$, $\rho=\int f\,dv$, etc. Write $f=M_{\rho,u,T}(1+\varepsilon\, h)$.

**The CE ansatz.** Seek $f$ slaved to the macroscopic fields $U=(\rho,u,T)$:

$$f = F_\varepsilon[U](v),\qquad F_\varepsilon=\sum_{n\ge0}\varepsilon^n F^{(n)}[U],\quad F^{(0)}=M_U,$$

together with the expansion of the macroscopic evolution $\partial_t U=\sum_{n\ge0}\varepsilon^n \mathcal{A}^{(n)}[U]$. Substituting into the kinetic equation gives the **invariance equation**

$$\big(\partial_t + v\cdot\nabla_x\big)F_\varepsilon[U] \;\Big|_{\partial_t U = \mathcal{A}_\varepsilon[U]} \;=\; \frac{1}{\varepsilon}Q(F_\varepsilon,F_\varepsilon),$$

a functional (not merely differential) equation whose formal power-series solution is the CE series. Order by order one inverts the linearized collision operator $L_M h = 2Q(M,Mh)/M$ on $(\ker L_M)^\perp$, with spectral gap $\langle h, L_M h\rangle_M \le -\lambda\|h\|^2_M$ for hard cutoff kernels (Grad 1963).

Order $\varepsilon^0$ gives compressible Euler; order $\varepsilon^1$ gives Navier–Stokes–Fourier with

$$\sigma = -\mu\big(\nabla u + (\nabla u)^{\!\top} - \tfrac{2}{d}(\nabla\!\cdot u)I\big),\qquad q=-\kappa\nabla T,$$

$\mu,\kappa$ given by Sonine-polynomial solutions of $L_M$-inversion; order $\varepsilon^2$ gives the Burnett stress, containing terms like $\varpi_1 (\nabla\!\cdot u)^2$, $\varpi_2\,\nabla^2 T$, $\varpi_3\,\nabla T\otimes\nabla T/T$.

**Linear model problem.** Fourier transform the linearized equation at wave number $k$; the hydrodynamic modes are eigenvalues $\lambda_j(k)$ of a $k$-dependent operator. The CE series is exactly the Taylor expansion of $\lambda_j$ in $k$ (with $\varepsilon k$ the true parameter), so its radius of convergence equals the distance from $k=0$ to the nearest singularity of the hydrodynamic branch — typically a **branch point where a hydrodynamic eigenvalue collides with the kinetic (non-hydrodynamic) spectrum**.

## 3. History & State of the Art (SOTA)

- **1912–1917.** Hilbert's expansion (Hilbert, 1912) gives hydrodynamics with $\varepsilon$-dependent *initial data*; Chapman (1916) and Enskog (1917) independently produce the slaved expansion that yields $\varepsilon$-independent transport coefficients matching experiment.
- **1949–1958.** Grad's moment method and his rigorous analysis of $L_M$ (spectral gap, Fredholm alternative) put the order-by-order inversion on firm ground; Grad already warns that the series is asymptotic.
- **1979–1980.** Nishida derives the compressible Euler limit for analytic data via an abstract Cauchy–Kovalevskaya theorem; Caflisch (CPAM 1980) proves the truncated Hilbert expansion converges on the time interval where the Euler solution stays smooth.
- **1982.** Bobylev shows the linearized Burnett and super-Burnett equations are **unstable to short waves** — the $O(k^4)$ correction has the wrong sign — so CE truncations beyond Navier–Stokes are ill posed as initial-value problems. This is the single most influential structural obstruction.
- **1986.** Santos, Brey and Dufty exhibit a solvable model (BGK under uniform shear flow) where the CE series in the shear rate has **zero radius of convergence**, with the exact transport coefficients non-analytic at zero.
- **1991–2004.** The incompressible hydrodynamic limits: Bardos–Golse–Levermore program; De Masi–Esposito–Lebowitz; Bardos–Ukai; culminating in Golse–Saint-Raymond's derivation of Leray solutions of Navier–Stokes from renormalized DiPerna–Lions solutions (Invent. Math. 2004).
- **1990s–2010s.** The *invariant manifold* viewpoint (Gorban–Karlin): treat the invariance equation directly and solve it non-perturbatively. For linearized Grad systems the exact hydrodynamic manifold is computable and exists only up to a critical wave number, beyond which it ceases to be a smooth invariant manifold — an exact, computable radius of convergence.

## 4. Partial Results / Verified Cases

- **Truncated Hilbert / CE at first order, rigorous.** Caflisch (1980): compressible Euler limit with $O(\varepsilon)$ error for hard-sphere Boltzmann as long as the Euler solution is smooth. Lachowicz (1987) adds the initial layer. Guo (CPAM 2006) validates the diffusive expansion *beyond* Navier–Stokes to arbitrary finite order for the incompressible scaling with smooth data, showing the truncations are asymptotically correct even though the full series need not converge.
- **Exact linear hydrodynamics, finite-moment models.** For linearized Grad 13-moment and related closures in 1D, Karlin, Colangeli and Kröger solve the invariance equation exactly; the hydrodynamic branch exists for $|k| < k_c$ and terminates at a branch point (reported $k_c \approx 0.3033$ in the Karlin–Gorban normalization), where the CE series radius of convergence is exactly $k_c$.
- **Zero radius of convergence.** BGK in uniform shear flow (Santos–Brey–Dufty 1986): CE series in the reduced shear rate diverges for every nonzero value; the exact viscosity is a non-analytic function of shear rate.
- **Ill-posedness of truncations.** Bobylev (1982, 2006): linearized Burnett and super-Burnett have unbounded growth rates $\sim +c\,k^4$ for large $k$ for Maxwell molecules and hard spheres. Regularized variants (Jin–Slemrod 2001, via relaxation; Bobylev's hyperbolic Burnett) restore linear stability while agreeing to $O(\varepsilon^2)$.
- **Kinetic spectrum.** For linearized Boltzmann with hard cutoff kernels the five hydrodynamic eigenvalues are analytic in $k$ on a neighborhood of $0$ (Ellis–Pinsky, Nicolaenko), so the *linear* CE series has strictly positive radius of convergence in that setting — a genuine positive result, but with no known uniform lower bound as the kernel softens and the spectral gap closes.

## 5. Principal Obstacles

- **Small denominators from spectrum collision.** Order-$n$ CE coefficients involve $n$-fold inversions of $L_M$ against increasingly oscillatory data; the effective expansion parameter is $\varepsilon k / \lambda_{\text{gap}}$. When a hydrodynamic branch approaches the continuous/essential kinetic spectrum, coefficients grow factorially. There is no mechanism, analytic or entropic, forcing cancellation.
- **Non-analyticity is real, not technical.** The Santos–Brey–Dufty example shows divergence survives in exactly solvable models. So no improvement of estimates can rescue convergence in general; only a resummation theory can.
- **Soft potentials and no spectral gap.** For soft potentials and non-cutoff kernels $L_M$ has no spectral gap; inverting it loses velocity weights at every order, and the natural function spaces degrade with $n$. Standard hypocoercivity gives at best subexponential control, not the uniform-in-$n$ bounds a convergence proof needs.
- **Loss of derivatives.** Each CE order raises the spatial derivative count by one. A convergent series would require analyticity in $x$ with a uniform radius; hydrodynamic solutions generically develop shocks, so the analytic framework that makes Nishida's argument work is not available globally.
- **Nonlinearity of the invariance equation.** The exact hydrodynamic manifold is defined by a nonlinear functional equation with a quadratic term; no fixed-point formulation with a contraction on a natural Banach space is known beyond linearized or moment-truncated settings.
- **Borel summability unproven.** Even where factorial divergence is expected, nobody has established the required Gevrey-1 bounds $|F^{(n)}| \le C A^n n!$ with analyticity in a Borel sector for the Boltzmann collision operator.

## 6. The Gap

Proven: (i) the first two truncations are asymptotically valid, with rigorous error bounds, on time intervals of smooth hydrodynamic solutions; (ii) in linearized, finite-moment, or spatially one-dimensional models, the exact hydrodynamic manifold exists and the CE radius of convergence equals a computable branch-point distance; (iii) the series can have radius zero in nonlinear regimes.

Missing: a theory that, for full nonlinear Boltzmann with hard-sphere kernel, (a) proves the CE coefficients obey Gevrey-type bounds $\|F^{(n)}\|\le C A^n (n!)^{s}$ with explicit $s$, (b) constructs a summation transform mapping the series to a true invariant manifold of the kinetic flow, and (c) identifies the exact domain in $(\varepsilon, k, \|U\|)$ where that manifold exists. The barrier is that all present arguments are *finite-order* — they estimate a fixed truncation and dump the rest into a remainder controlled by kinetic energy/entropy methods, which cannot see the $n\to\infty$ structure at all.

## 7. Current Research (as of June 2026)

- **Invariant-manifold school** (ETH Zürich, Karlin and collaborators; Gorban at Leicester). Exact hydrodynamics for linearized kinetic models, Newton-iteration solution of the invariance equation instead of power series; the Newton method converges where the series diverges. Extension to nonlinear and multi-dimensional settings is the active frontier.
- **Rigorous hydrodynamic limits** (Guo and collaborators, Brown; Jang; Esposito–Marra school). Hilbert/CE expansions with boundary layers, diffuse-reflection boundaries, and Knudsen-layer matching; validation of higher-order truncations under regularity assumptions.
- **Regularized higher-order hydrodynamics.** Bobylev's hyperbolic Burnett systems and relaxation-regularized Burnett (Jin–Slemrod) remain the reference constructions; work continues on whether a *unique* stable regularization is singled out by the invariance equation. *(frontier — verify)*
- **Resurgence/Borel methods imported from ODE and hydrodynamics.** Transseries treatments of divergent series in fluid asymptotics are being applied to relaxation-type kinetic models; no Boltzmann-level result yet. *(frontier — verify)*
- **Microscopic derivations.** Long-time validity of the Boltzmann equation from hard-sphere dynamics (Deng–Hani–Ma, 2025) sharpens the meaning of "the" kinetic equation whose CE series is under study. *(frontier — verify)*

## 8. Future Work

- Prove or disprove Gevrey-1 bounds on CE coefficients for the linearized hard-sphere operator, then attempt Borel summation in $\varepsilon$.
- Compute the exact hydrodynamic manifold for the *nonlinear* one-dimensional BGK equation and locate its boundary; this is the smallest nonlinear target where the answer should be decidable.
- Determine whether the branch-point mechanism (hydrodynamic eigenvalue meeting the essential spectrum) is the *only* source of divergence in the linear theory, for general cutoff kernels.
- Establish whether stable higher-order hydrodynamics can be derived by projecting the kinetic flow onto an approximate invariant manifold, rather than truncating a series — with an a priori error estimate.
- Extend to granular gases, plasmas (Vlasov–Landau) and lattice Boltzmann, where the CE expansion is a design tool and its failure has concrete numerical consequences.

## 9. Key References

- **[Foundational]** S. Chapman and T. G. Cowling. *The Mathematical Theory of Non-uniform Gases.* 3rd ed., Cambridge University Press, 1970.
- **[Foundational]** H. Grad. *Asymptotic theory of the Boltzmann equation.* Physics of Fluids 6, 1963.
- **[Foundational]** R. E. Caflisch. *The fluid dynamic limit of the nonlinear Boltzmann equation.* Communications on Pure and Applied Mathematics 33(5), 651–666, 1980.
- **[Foundational]** A. V. Bobylev. *The Chapman–Enskog and Grad methods for solving the Boltzmann equation.* Soviet Physics Doklady 27, 29–31, 1982.
- **[Key result]** A. Santos, J. J. Brey, J. W. Dufty. *Divergence of the Chapman–Enskog expansion.* Physical Review Letters 56, 1571–1574, 1986.
- **[SOTA / Recent]** F. Golse and L. Saint-Raymond. *The Navier–Stokes limit of the Boltzmann equation for bounded collision kernels.* Inventiones Mathematicae 155, 81–161, 2004.
- **[SOTA / Recent]** Y. Guo. *Boltzmann diffusive limit beyond the Navier–Stokes approximation.* Communications on Pure and Applied Mathematics 59(5), 626–687, 2006.
- **[SOTA / Recent]** S. Jin and M. Slemrod. *Regularization of the Burnett equations via relaxation.* Journal of Statistical Physics 103, 1009–1033, 2001.
- **[SOTA / Recent]** A. V. Bobylev. *Instabilities in the Chapman–Enskog expansion and hyperbolic Burnett equations.* Journal of Statistical Physics 124, 371–399, 2006.
- **[SOTA / Recent]** I. V. Karlin, M. Colangeli, M. Kröger. *Exact linear hydrodynamics from the Boltzmann equation.* Physical Review Letters 100, 214503, 2008.
- **[Survey]** A. N. Gorban and I. Karlin. *Hilbert's 6th Problem: exact and approximate hydrodynamic manifolds for kinetic equations.* Bulletin of the American Mathematical Society 51(2), 187–246, 2014.
- **[Survey]** C. Villani. *A review of mathematical topics in collisional kinetic theory.* Handbook of Mathematical Fluid Dynamics, Vol. I, North-Holland, 2002.
- **[Book]** A. N. Gorban and I. V. Karlin. *Invariant Manifolds for Physical and Chemical Kinetics.* Lecture Notes in Physics 660, Springer, 2005.
- **[Book]** Y. Sone. *Molecular Gas Dynamics: Theory, Techniques, and Applications.* Birkhäuser, 2007.

## 10. Worked Example / Concrete Special Case

Take the minimal linear two-field model at fixed wave number $k>0$ (a caricature of one macroscopic field $f_1$ coupled to one kinetic moment $f_2$ with relaxation rate $1$, in units $\varepsilon=1$):

$$\partial_t f_1 = -ik f_2, \qquad \partial_t f_2 = -ik f_1 - f_2 .$$

**Invariance equation.** The CE ansatz slaves the fast variable: $f_2 = A(k)\,f_1$. Then $\partial_t f_1 = -ikA f_1$, and consistency with the second equation requires $A\,\partial_t f_1 = -ikf_1 - Af_1$, i.e.

$$-ikA^2 = -ik - A \quad\Longleftrightarrow\quad ik\,A^2 - A - ik = 0 .$$

**Exact solution.**

$$A_\pm(k)=\frac{1 \pm \sqrt{1-4k^2}}{2ik}.$$

The physical (hydrodynamic) branch is the one regular at $k=0$: expanding $\sqrt{1-4k^2}=1-2k^2-2k^4-\cdots$,

$$A_-(k) = \frac{2k^2+2k^4+4k^6+\cdots}{2ik} = -i\big(k + k^3 + 2k^5+\cdots\big).$$

**Reading off the Chapman–Enskog orders.** The macroscopic equation is $\partial_t f_1 = -ikA_-(k) f_1 = \lambda(k) f_1$ with

$$\lambda(k) = -k^2 - k^4 - 2k^6 - \cdots$$

- $O(k^2)$: $\lambda \approx -k^2$ — the Navier–Stokes-level diffusive term, $\partial_t f_1 = \partial_x^2 f_1$.
- $O(k^4)$: the Burnett correction $-k^4$. Note it is *stabilizing* here; in real Boltzmann the analogous coefficient has the opposite sign, which is exactly Bobylev's instability.
- The coefficients $1,1,2,5,14,\dots$ are Catalan numbers — the series is the generating function of a branch of an algebraic curve.

**Radius of convergence.** The singularity is the square-root branch point where the discriminant vanishes:

$$1-4k_c^2 = 0 \;\Longrightarrow\; k_c = \tfrac12 .$$

So the CE series converges precisely for $|k|<\tfrac12$ and diverges for $|k|>\tfrac12$; the radius is set not by any estimate on collision integrals but by a **collision of the hydrodynamic root with the second (kinetic) root**: at $k=k_c$, $A_+=A_-=1/(2ik_c)$, and for $k>k_c$ the two roots become complex conjugates so no real invariant hydrodynamic manifold exists.

**What this illustrates.** (i) The CE series is a Taylor expansion of an algebraic/analytic branch, so its convergence is a spectral question, not an estimate question. (ii) Its radius is finite and computable in solvable models. (iii) Beyond $k_c$, hydrodynamics does not merely converge slowly — the object it is expanding *ceases to exist*. The open problem is whether the same clean picture, and a summation procedure valid up to the analogous $k_c(\varepsilon)$, can be established for the full nonlinear Boltzmann equation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*