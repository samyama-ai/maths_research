---
id: 06-pdes/fractional-laplacian-regularity
title: "Fractional Laplacian Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fractional Laplacian Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/fractional-laplacian-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The problem concerns establishing optimal interior and boundary regularity estimates for solutions to partial differential equations (PDEs) driven by the fractional Laplacian $(-\Delta)^s$, or more broadly, non-local integro-differential operators. For a bounded domain $\Omega \subset \mathbb{R}^n$ and $s \in (0,1)$, the linear Dirichlet problem is given by:
$$
\begin{cases} 
(-\Delta)^s u = f & \text{in } \Omega, \\
u = g & \text{in } \mathbb{R}^n \setminus \Omega.
\end{cases}
$$
The core regularity questions are:
1. **Interior Regularity:** Under what assumptions on $f$, the domain $\Omega$, and the kernel of the integro-differential operator does the solution $u$ belong to Hölder spaces $C^\beta_{loc}(\Omega)$ or classical fractional Sobolev spaces $H^{\beta}_{loc}(\Omega)$?
2. **Boundary Regularity:** Because non-local operators detect exterior data globally, boundary conditions must be prescribed on $\mathbb{R}^n \setminus \Omega$. How does the solution behave as it approaches $\partial \Omega$? Specifically, can one establish that $u/d^s \in C^\alpha(\overline{\Omega})$, where $d(x) = \text{dist}(x, \partial \Omega)$, even though $u \notin C^1(\overline{\Omega})$ in general?
3. **Fully Nonlinear Regularity:** For fully nonlinear non-local operators $F(u, x) = f(x)$, does the classical Caffarelli regularity theory (e.g., $C^{1,\alpha}$ interior regularity for the fractional Isaacs equation) generalize optimally up to the boundary?

A complete resolution requires sharp Hölder and Schauder-type estimates for linear, quasi-linear, and fully nonlinear fractional operators, both in the interior and up to $\partial \Omega$, covering non-symmetric kernels and rough coefficients.

## 2. Mathematical Foundations

The fractional Laplacian is defined for a Schwartz function $u \in \mathcal{S}(\mathbb{R}^n)$ via the Fourier transform as $\mathcal{F}((-\Delta)^s u)(\xi) = |\xi|^{2s} \mathcal{F} u(\xi)$, where $s \in (0,1)$. Equivalently, it is a singular integral operator defined by a Cauchy principal value:
$$
(-\Delta)^s u(x) = C_{n,s} \text{P.V.} \int_{\mathbb{R}^n} \frac{u(x) - u(y)}{|x-y|^{n+2s}} \, dy,
$$
where the normalization constant is $C_{n,s} = \frac{s2^{2s}\Gamma(\frac{n+2s}{2})}{\pi^{n/2}\Gamma(1-s)}$.

The natural functional setting for the Dirichlet problem is the fractional Sobolev space $H^s_0(\Omega)$, which is the completion of $C^\infty_c(\Omega)$ under the Gagliardo semi-norm:
$$
[u]_{H^s(\mathbb{R}^n)}^2 = \int_{\mathbb{R}^n} \int_{\mathbb{R}^n} \frac{|u(x)-u(y)|^2}{|x-y|^{n+2s}} \, dx \, dy.
$$

A pivotal tool in modern fractional regularity theory is the **Caffarelli-Silvestre Extension** (2007). The non-local operator $(-\Delta)^s$ on $\mathbb{R}^n$ can be realized as a Dirichlet-to-Neumann operator for a local, degenerate elliptic equation in the upper half-space $\mathbb{R}^{n+1}_+ = \mathbb{R}^n \times (0, \infty)$. If $U(x, y)$ solves:
$$
\begin{cases} 
\text{div}_{x,y} \left( y^{1-2s} \nabla U \right) = 0 & \text{in } \mathbb{R}^{n+1}_+, \\
U(x,0) = u(x) & \text{on } \mathbb{R}^n,
\end{cases}
$$
then, up to a strict positive constant $c_s$, 
$$
(-\Delta)^s u(x) = -c_s \lim_{y \to 0^+} y^{1-2s} \partial_y U(x,y).
$$
This transforms non-local problems into degenerate local PDEs with an $A_2$ Muckenhoupt weight, opening the door to classical techniques like the De Giorgi-Nash-Moser iterations.

Fully nonlinear integro-differential operators are often modeled as:
$$
I u(x) = \inf_{\alpha} \sup_{\beta} \int_{\mathbb{R}^n} \delta u(x,y) K_{\alpha \beta}(x,y) \, dy
$$
where $\delta u(x,y) = u(x+y) + u(x-y) - 2u(x)$, and the kernels $K_{\alpha \beta}$ are comparable to the fractional Laplacian kernel $|y|^{-(n+2s)}$.

## 3. History & State of the Art (SOTA)

Historically, fractional operators were studied via Riesz potentials in the 1930s and emerged heavily in probability theory via Lévy processes (jump processes). The modern PDE regularity perspective underwent a revolution around 2007–2009.

- **2007:** Caffarelli and Silvestre introduced the harmonic extension problem. This structural insight allowed researchers to apply local PDE techniques to non-local operators, triggering a decade of rapid advancement.
- **2009–2011:** Caffarelli and Silvestre published a triad of foundational papers establishing interior regularity theory for fully nonlinear integro-differential equations, pushing Isaacs and Bellman-type equations to the fractional setting. They proved $C^{1,\alpha}$ estimates without relying on the extension, using instead non-local Alexandroff-Bakelman-Pucci (ABP) estimates.
- **2014:** Ros-Oton and Serra resolved the boundary regularity for the linear fractional Dirichlet problem. They proved that while $u$ only achieves $C^s(\mathbb{R}^n)$ globally, the quotient $u/d^s$ belongs to $C^\alpha(\overline{\Omega})$, initiating the concept of "weighted boundary regularity" for non-local operators.
- **2018–2022:** Progress shifted to free boundary problems (e.g., the fractional obstacle problem) and non-symmetric kernels. Figalli, Ros-Oton, and Serra characterized the singular set of the free boundary for the fractional obstacle problem.

Currently, the state-of-the-art for linear elliptic fractional PDEs is structurally complete: optimal Schauder estimates are known. The SOTA for fully nonlinear equations is well-developed in the interior, but boundary behaviors for highly anisotropic, fully non-linear Lévy measures remain actively contested.

## 4. Partial Results / Verified Cases

The regularity theory is firmly established in the following cases:

- **Interior Linear Schauder Estimates:** If $(-\Delta)^s u = f$ in $\Omega$ and $f \in C^\alpha(\Omega)$, then $u \in C^{2s+\alpha}_{loc}(\Omega)$ (provided $2s+\alpha \notin \mathbb{Z}$). 
- **Boundary Linear Regularity:** For $f \in L^\infty(\Omega)$ and a $C^{1,1}$ domain $\Omega$, the solution $u$ is generally not Lipschitz up to the boundary. Instead, $u \in C^s(\mathbb{R}^n)$. Furthermore, $u = d^s v$, where $v \in C^\alpha(\overline{\Omega})$ and $d(x)$ is the distance to $\partial \Omega$.
- **Fully Nonlinear Interior Regularity:** Solutions to fully nonlinear equations $\inf \sup L_{ab} u = 0$ (where $L_{ab}$ are linear translation-invariant integro-differential operators) satisfy $u \in C^{1,\alpha}_{loc}$ (Caffarelli-Silvestre). If the kernels are smooth enough, solutions bootstrap to classical $C^{2s+\alpha}_{loc}$.
- **Fractional Obstacle Problem:** For the problem $\min\{(-\Delta)^s u, u - \varphi\} = 0$, the free boundary $\partial \{u = \varphi\}$ decomposes into a regular part (which is a $C^{1,\alpha}$ hypersurface) and a singular set. For $s = 1/2$ (the Signorini problem), the singular set is completely classified and shown to be rectifiable.

## 5. Principal Obstacles

The fundamental bottleneck in fractional regularity theory is **non-locality**, which breaks down standard multiplier and localization techniques.

**1. Commutator Difficulties:** In classical PDE theory, one studies local behavior by multiplying the solution $u$ by a smooth cutoff function $\eta \in C^\infty_c(B_R)$. For the local Laplacian, $\Delta(u\eta) = \eta\Delta u + u\Delta \eta + 2\nabla u \cdot \nabla \eta$. This cleanly isolates derivatives. For the fractional Laplacian, the product rule yields a highly non-trivial commutator:
$$
(-\Delta)^s(u\eta) = \eta(-\Delta)^s u + u(-\Delta)^s \eta - C_{n,s} \int_{\mathbb{R}^n} \frac{(u(x)-u(y))(\eta(x)-\eta(y))}{|x-y|^{n+2s}} \, dy.
$$
The integral term involves the interaction of $u$ globally across $\mathbb{R}^n$, meaning interior regularity strongly depends on the "tails" of the function at infinity.

**2. Boundary Non-Degeneracy:** Because solutions typically decay as $d(x)^s$ near the boundary, standard Schauder estimates applied near $\partial \Omega$ degenerate. Analyzing $u/d^s$ involves tracking degenerate integral operators with singular weights, which destroys the translation invariance of the problem near the boundary.

**3. Absence of the Extension Trick:** The Caffarelli-Silvestre extension only applies to the standard fractional Laplacian (or operators with explicit spectral multipliers). For fully nonlinear equations with rough $x$-dependent kernels, or non-symmetric Lévy measures (like fractional drift-diffusion equations), the extension to $\mathbb{R}^{n+1}_+$ does not exist. One must work directly with highly singular integrals using non-local De Giorgi methods, which scale poorly when anisotropy is introduced.

## 6. The Gap

The exact boundary separating the solved instances and the general regularity conjecture lies in **boundary regularity for fully nonlinear non-local equations** and **non-translation invariant rough kernels**. 

Specifically:
- While we know $u/d^s \in C^\alpha(\overline{\Omega})$ for linear operators with regular kernels, proving sharp, global Schauder estimates $u/d^s \in C^{1+\alpha}(\overline{\Omega})$ for general fully nonlinear fractional operators $F(u, x) = f(x)$ with non-convex structure remains an open frontier.
- The parabolic theory is considerably less complete than the elliptic theory. Time-dependent fractional operators $(\partial_t + (-\Delta)^s)u = 0$ in bounded domains pose severe technical gaps regarding the initial-boundary compatibility conditions for higher-order regularity.
- Moving from $C^{1,1}$ domains to Lipschitz domains limits the application of distance-function quotients. The precise trace spaces and boundary trace behavior for $s$-harmonic functions on Lipschitz boundaries are not fully characterized for all $s \in (0,1)$.

## 7. Current Research (as of June 2026)

Active research in the mid-2020s has bifurcated into a few prominent directions:

- **Rough and Anisotropic Kernels:** Groups at UT Austin and ETH Zurich are studying operators with merely measurable bounded coefficients $K(x,y) \asymp |x-y|^{-(n+2s)}$. Establishing boundary Harnack principles for these equations without relying on scale-invariance is a major target. *(frontier — verify)*: Recent preprints claim to establish $C^\alpha$ estimates up to the boundary for operators where the kernel is not symmetric, i.e., $K(x,y) \neq K(y,x)$.
- **Variable Order Operators:** Equations where the order of the fractional derivative depends on spatial position, $(-\Delta)^{s(x)}$, are actively studied for applications in anomalous diffusion where the medium's porosity changes.
- **Fractional Free Boundaries:** The complete generic regularity of the free boundary in the obstacle problem for all $s \in (0,1)$ in high dimensions ($n \ge 4$) remains intensely studied by the schools surrounding Figalli, Ros-Oton, and Serra.
- **Connections to Fluid Dynamics:** Fractional operators appear prominently in the Surface Quasi-Geostrophic (SQG) equation. Regularity of solutions for the critically dissipative SQG is known, but the boundary behavior for SQG in bounded domains remains an active point of attack.

## 8. Future Work

Leading researchers emphasize the need to develop a robust **non-local pseudo-differential calculus** that operates efficiently on bounded domains with rough boundaries (Lipschitz or fractal). A major goal is to bypass the extension technique entirely, establishing purely integral-based proofs for fractional Krylov-Safonov and Schauder theories.

Another identified pathway is integrating fractional regularity with geometric measure theory. For example, understanding non-local minimal surfaces (fractional perimeters) completely—specifically the Bernstein problem for fractional minimal graphs in dimensions $n \ge 4$—requires new monotonicity formulas that can handle the non-local energy tail interacting with infinity.

## 9. Key References

- **[Foundational]** Caffarelli, L., & Silvestre, L. *An extension problem related to the fractional Laplacian.* Communications in Partial Differential Equations, 32(8), 2007.
- **[Foundational]** Caffarelli, L., & Silvestre, L. *Regularity theory for fully nonlinear integro-differential equations.* Communications on Pure and Applied Mathematics, 62(5), 2009.
- **[SOTA / Recent]** Ros-Oton, X., & Serra, J. *The Dirichlet problem for the fractional Laplacian: regularity up to the boundary.* Journal de Mathématiques Pures et Appliquées, 101(3), 2014.
- **[SOTA / Recent]** Figalli, A., Ros-Oton, X., & Serra, J. *Generic regularity of free boundaries for the obstacle problem.* Publications Mathématiques de l'IHÉS, 132, 2020.
- **[Survey]** Bucur, C., & Valdinoci, E. *Nonlocal Diffusion and Applications.* Lecture Notes of the Unione Matematica Italiana, Springer, 2016.

## 10. Worked Example / Concrete Special Case

Consider a specific geometric setup to illustrate boundary behavior: the one-dimensional linear problem on the interval $\Omega = (-1, 1) \subset \mathbb{R}$ with $s = 1/2$.
$$
\begin{cases}
(-\Delta)^{1/2} u(x) = 1 & x \in (-1, 1), \\
u(x) = 0 & x \in \mathbb{R} \setminus (-1, 1).
\end{cases}
$$
Classical elliptic PDEs ($\Delta u = -1$) would yield a parabola $u(x) = C(1-x^2)$, which has smooth (Lipschitz/bounded) derivatives up to $x = \pm 1$. 

For the half-Laplacian, the solution is exactly computed using properties of Riesz potentials or the Caffarelli-Silvestre extension to $\mathbb{R}^2_+$. The exact solution is:
$$
u(x) = \kappa \left( 1 - x^2 \right)_+^{1/2}
$$
where $\kappa$ is a normalizing constant and $a_+ = \max(a, 0)$.

**Regularity Analysis:**
1. **Interior:** Away from $x = \pm 1$, the function $(1-x^2)^{1/2}$ is infinitely differentiable. Thus, interior regularity is perfectly smooth: $u \in C^\infty_{loc}(-1, 1)$, corroborating the $C^{2s+\alpha}_{loc}$ interior estimates.
2. **Boundary:** As $x \to 1^-$, we can approximate $1-x^2 = (1-x)(1+x) \approx 2(1-x)$. Therefore, $u(x) \sim \kappa \sqrt{2} (1-x)^{1/2}$. 
   The derivative is $u'(x) \sim \frac{-\kappa}{\sqrt{2}} (1-x)^{-1/2}$, which approaches $-\infty$ as $x \to 1$.
   Therefore, $u \notin C^1(\overline{\Omega})$ and $u$ is not even Lipschitz. Specifically, $u \in C^{1/2}(\mathbb{R})$.
3. **The Quotient:** If we divide by the distance function to the boundary $d(x)^s = (1-|x|)^{1/2}$, we evaluate $u(x) / d(x)^{1/2}$. Near $x=1$, this quotient behaves like $\kappa \frac{(1-x^2)^{1/2}}{(1-x)^{1/2}} = \kappa (1+x)^{1/2}$. This quotient function is completely smooth (specifically $C^\infty$) up to the boundary $x=1$. 

This explicit case perfectly grounds the abstract theorem of Ros-Oton and Serra: $u \in C^s(\mathbb{R}^n)$, but $u / d^s \in C^\alpha(\overline{\Omega})$. The fractional Laplacian fundamentally alters classical boundary smoothness, exchanging it for weighted regularity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*