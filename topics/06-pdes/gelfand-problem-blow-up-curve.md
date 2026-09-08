---
id: 06-pdes/gelfand-problem-blow-up-curve
title: "Gelfand Problem Blow-Up Curve"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gelfand Problem Blow-Up Curve

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/gelfand-problem-blow-up-curve` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The **Gelfand Problem** (historically identified as the Liouville-Bratu-Gelfand problem) models nonlinear thermal ignition, combustion, and aspects of differential geometry. Formulated on a bounded, smooth domain $\Omega \subset \mathbb{R}^n$, it asks for the solutions to the nonlinear elliptic boundary value problem:
$$
\begin{cases}
-\Delta u = \lambda e^u & \text{in } \Omega \\
u = 0 & \text{on } \partial\Omega
\end{cases}
$$
where $\lambda > 0$ is a real parameter, known as the Frank-Kamenetskii parameter.

The **Blow-Up Curve** (or bifurcation diagram) is the topological space of solutions defined by the one-dimensional curve $\mathcal{C} = \{ (\lambda, \|u\|_\infty) \mid u \text{ is a classical solution} \} \subset \mathbb{R}^+ \times \mathbb{R}^+$. 

**The Core Conjecture:** 
While the precise geometric structure of $\mathcal{C}$ is completely classified when $\Omega$ is a perfect sphere (the unit ball $B_1$), its structure on arbitrary domains remains one of the most prominent open questions in nonlinear PDE theory. Specifically, the conjecture asserts that for generic convex domains in dimensions $3 \le n \le 9$, the infinite spiraling (infinitely many turning points) observed in the radial case unfolds into a finite number of turning points; alternatively, some hypothesize that the infinite sequence of folds remains robust under small perturbations. A complete proof requires establishing the exact number of solutions for a given $\lambda$, verifying non-degeneracy at the turning points, and classifying the spatial blow-up profiles of the solutions as they traverse the upper branches of $\mathcal{C}$.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^n$ ($n \ge 1$) be a bounded domain with boundary $\partial\Omega$ of class $C^2$. We seek classical solutions $u \in C^2(\Omega) \cap C(\overline{\Omega})$ or weak solutions $u \in H_0^1(\Omega) \cap L^\infty(\Omega)$. 

The problem is governed by the energy functional $J_\lambda : H_0^1(\Omega) \to \mathbb{R} \cup \{+\infty\}$, defined as:
$$
J_\lambda(u) = \frac{1}{2} \int_\Omega |\nabla u|^2 \, dx - \lambda \int_\Omega e^u \, dx
$$

The mathematical structure relies heavily on the existence of a critical parameter $\lambda^* \in (0, \infty)$, defined as:
$$
\lambda^* = \sup \{ \lambda > 0 \mid \text{there exists a classical solution to } -\Delta u = \lambda e^u \}
$$

By the Implicit Function Theorem and the strong maximum principle, the following foundational axioms are established:
1.  **Minimal Branch:** For every $\lambda \in (0, \lambda^*)$, there exists a unique minimal solution $u_\lambda$, which is classically stable. Stability here means the principal eigenvalue $\mu_1(u_\lambda)$ of the linearized operator $L_u = -\Delta - \lambda e^u$ is strictly positive.
2.  **Extremal Solution:** As $\lambda \nearrow \lambda^*$, the minimal solutions $u_\lambda$ monotonically converge to an extremal solution $u^*$. 
3.  **Turning Points:** A point on the curve $\mathcal{C}$ where the tangent is vertical (i.e., $d\lambda = 0$) is a turning point. At such a point, the linearized operator $L_u$ has a zero eigenvalue ($\mu_1 = 0$), and the Morse index of the solution changes.

The "blow-up" behavior studies the asymptotic limits of families of solutions $u_k$ associated with parameters $\lambda_k$. We say a sequence of solutions blows up if $\|u_k\|_\infty \to \infty$. 

## 3. History & State of the Art (SOTA)

The history of the problem is rich and spans over a century:
-   **Liouville (1853):** Solved the equation in the entire two-dimensional space $\mathbb{R}^2$, providing exact classification of solutions.
-   **Bratu (1914):** Explicitly solved the 1D case, revealing a single turning point.
-   **Gelfand (1959):** Formulated the problem in the context of thermal combustion, sparking modern mathematical interest.
-   **Joseph & Lundgren (1973):** Delivered the foundational breakthrough by completely classifying the radial solutions for the unit ball $\Omega = B_1$.

**The Joseph-Lundgren Classification (Radial Case):**
When $\Omega = B_1$, the problem reduces to the ODE $-u'' - \frac{n-1}{r} u' = \lambda e^u$. The blow-up curve $\mathcal{C}$ exhibits striking dimension-dependent phase transitions:
-   **$1 \le n \le 2$:** The curve $\mathcal{C}$ has exactly one turning point at $\lambda = \lambda^*$. The upper branch extends to $\lambda = 0$ monotonically, and solutions concentrate at the origin as $\lambda \to 0$.
-   **$3 \le n \le 9$:** The curve $\mathcal{C}$ exhibits infinitely many turning points. It spirals inward around a singular limit $\lambda_s = 2(n-2)$, which corresponds to the singular solution $u_s(r) = -2 \log r$.
-   **$n \ge 10$:** The curve $\mathcal{C}$ is strictly monotone increasing and contains no turning points. The extremal solution $u^*$ is precisely the singular solution $u_s(r)$ and $\lambda^* = 2(n-2)$.

**State of the Art (SOTA):**
For $n=2$, the SOTA is highly advanced. Due to connections with the Liouville equation and conformal geometry, it is established (Nagasaki & Suzuki, 1990) that blow-up solutions on arbitrary 2D domains exhibit quantized mass concentration, $ \lambda \int_\Omega e^{u_k} \to 8\pi m $ for some integer $m \ge 1$, blowing up at exactly $m$ interior points.
For $n \ge 3$, the SOTA is far less complete. Recent efforts focus on utilizing Lyapunov-Schmidt reduction to construct multi-peak solutions, proving that for non-convex domains or domains with holes, secondary bifurcations branch off the main curve. However, the exact structure of $\mathcal{C}$ for generic smooth convex domains in $3 \le n \le 9$ remains deeply unresolved.

## 4. Partial Results / Verified Cases

The conjecture is resolved only under strict symmetric or topological constraints:

1.  **Strictly Radial Domains:** For $\Omega = B_R(0)$, the exact structure (including the $3 \le n \le 9$ spiral) is completely verified. 
2.  **Two-Dimensional Convex Domains:** It has been rigorously proven that for any smooth, strictly convex domain in $n=2$, the blow-up curve has exactly one turning point, mirroring the radial case. The level sets of the solutions are strictly convex.
3.  **Annular Domains ($3 \le n \le 9$):** When $\Omega = \{ x \in \mathbb{R}^n \mid a < |x| < b \}$, symmetry-breaking bifurcations are proven to exist. The radial solution curve spirals, but non-radial solution branches bifurcate from the radial curve, leading to a highly complex, interconnected web of solutions.
4.  **Extremal Regularity:** It is proven that the extremal solution $u^*$ is universally smooth ($u^* \in L^\infty$) for $1 \le n \le 9$ on *any* bounded domain, while it can be singular for $n \ge 10$ (Brezis & Vázquez, 1997).

## 5. Principal Obstacles

Why do modern mathematical techniques fail to classify the general curve for $n \ge 3$?

-   **Failure of Trudinger-Moser in Higher Dimensions:** In $n=2$, the exponential growth $e^u$ is critically bounded by the Trudinger-Moser inequality, granting weak compactness. For $n \ge 3$, the nonlinearity $e^u$ is highly supercritical relative to the Sobolev embedding $H_0^1(\Omega) \hookrightarrow L^p(\Omega)$ for $p = \frac{2n}{n-2}$. Standard variational methods (like verifying the Palais-Smale condition) fail globally, making topological degree theory extraordinarily difficult to apply.
-   **Spectral Degeneracy & Morse Index:** At every turning point, the linearized operator $L_u$ becomes degenerate. In the radial case, ODE phase-plane methods easily track the Morse index. Without radial symmetry, predicting the spectrum of $-\Delta - \lambda e^u$ as $\|u\|_\infty \to \infty$ requires highly refined asymptotic estimates of Green's functions, which depend heavily on arbitrary boundary geometry.
-   **Singular Perturbation Collapse:** Attempting to construct solutions near the singular limit $\lambda_s = 2(n-2)$ via perturbation theory involves matching inner (blow-up profile) and outer (boundary condition) expansions. For $3 \le n \le 9$, the linear operator evaluated at the singular solution possesses complex eigenvalues. This induces oscillatory boundary layers that are notoriously unstable under non-radial domain perturbations.

## 6. The Gap

The precise mathematical gap lies between **topological degree counting** and the **exact multiplicity of solutions**. 
Currently, it is possible to prove that as $\lambda \to 0$ or as solutions blow up, the Leray-Schauder degree of the solutions can be computed. However, degree theory only provides an algebraic sum of solutions (e.g., $N_{\text{stable}} - N_{\text{unstable}} = \text{const}$).
To fully resolve the conjecture for convex domains in $3 \le n \le 9$, one must bridge the gap between knowing *that solutions exist* and proving the *non-degeneracy* of those solutions. The barrier is proving that the kernel of $L_u = -\Delta - \lambda e^u$ is exactly one-dimensional at folding points and empty elsewhere. Proving this would preclude the solution curve from fraying into multiple disjoint branches or exhibiting pitchfork bifurcations on arbitrary convex domains.

## 7. Current Research (as of June 2026)

Current investigations are proceeding along several distinct fronts:
-   **Rigorous Computation:** Computer-assisted proofs (using interval arithmetic and fixed-point theorems in Banach spaces) are being deployed to track the global continuation of the bifurcation curve on specific deformations of the ball, such as precise ellipsoids.
-   **Non-local Operators:** There is a surge of interest in the fractional Gelfand problem $(-\Delta)^s u = \lambda e^u$. Researchers are investigating how the non-local parameter $s \in (0, 1)$ smooths out the infinite oscillations observed in integer dimensions.
-   **Geometric Blow-up Profiling:** *(frontier — verify)* Recent preprints claim that for generic perturbations of the domain boundary in $n=3$, the infinite spiraling is a structurally unstable phenomenon, collapsing into a finite (though arbitrarily large) number of folds. This relies on advanced refined blow-up asymptotics and the precise geometry of the Robin function.

## 8. Future Work

Leading researchers suggest the following pathways to crack the general domains problem:
1.  **Refined Morse Theory:** Develop a localized Morse theory capable of handling supercritical non-compactness, specifically tailored to track the Morse index of solutions along the bifurcation branch without relying on radial ODE reductions.
2.  **Domain Variations:** Utilize shape optimization techniques (Hadamard variations) to study the differential of the turning points with respect to the domain boundary $\partial\Omega$. If the turning points are isolated and structurally stable, one could define a homotopy from the unit ball to any strictly convex domain.
3.  **Yamabe Connections:** Exploit analogies between the critical Gelfand equation and the Yamabe problem on manifolds with boundary, mapping the blow-up behavior of $e^u$ to the concentration of scalar curvature.

## 9. Key References

-   **[Foundational]** Joseph, D. D., & Lundgren, T. S. *Quasilinear Dirichlet problems driven by positive sources*. Archive for Rational Mechanics and Analysis, 49(4), 241-269, 1973. [DOI](https://doi.org/10.1007/bf00250508)
-   **[Foundational]** Gelfand, I. M. *Some problems in the theory of quasilinear equations*. Uspekhi Matematicheskikh Nauk, 14(2), 87-158, 1959.
-   **[Foundational]** Brezis, H., & Vázquez, J. L. *Blow-up solutions of some nonlinear elliptic problems*. Revista Matemática de la Universidad Complutense de Madrid, 10(2), 443-469, 1997.
-   **[SOTA / Recent]** Miyamoto, Y. *Classification of bifurcation diagrams for elliptic equations with exponential growth in a ball*. Annali di Matematica Pura ed Applicata, 194, 931-952, 2015. [DOI](https://doi.org/10.1007/s10231-014-0404-8)
-   **[Survey]** Dupaigne, L. *Stable Solutions of Elliptic Partial Differential Equations*. Chapman and Hall/CRC, 2011. [DOI](https://doi.org/10.1201/b10802)

## 10. Worked Example / Concrete Special Case

To ground the abstract geometry of the blow-up curve, consider the **1D Gelfand Problem** on the interval $\Omega = (-1, 1)$:
$$
-u'' = \lambda e^u, \quad u(-1) = u(1) = 0
$$
By symmetry, the maximum occurs at the origin. Let $M = u(0) = \|u\|_\infty$.
Multiplying the equation by $u'$ and integrating yields the conservation of energy:
$$
-\frac{1}{2}(u')^2 = \lambda e^u + C
$$
At $x = 0$, we have $u = M$ and $u' = 0$, giving $C = -\lambda e^M$. Thus:
$$
\frac{du}{dx} = -\sqrt{2\lambda(e^M - e^u)} \quad \text{for } x > 0
$$
Integrating this separable ODE from $x=0$ to $x=1$ gives the exact relationship between the parameter $\lambda$ and the maximum amplitude $M$:
$$
\int_0^M \frac{du}{\sqrt{e^M - e^u}} = \sqrt{2\lambda}
$$
By making the substitution $v = e^{(u-M)}$, this integral can be evaluated analytically in terms of elementary functions, leading to:
$$
\lambda(M) = 2 e^{-M} \left( \text{arctanh}\sqrt{1 - e^{-M}} \right)^2
$$
**Analysis of the Curve:**
-   As $M \to 0$ (small solutions), $\lambda \to 0$.
-   As $M \to \infty$ (blow-up), the asymptotic behavior is $\lambda(M) \approx 2 M^2 e^{-M} \to 0$.
-   By differentiating $\lambda(M)$ with respect to $M$, we find exactly one root. The curve has a unique maximum (turning point) at $M^* \approx 1.1868$, corresponding to the critical parameter $\lambda^* \approx 0.8785$. 

This explicit relation geometrically maps out a perfect "C-shaped" (or single-fold) blow-up curve in the $(\lambda, M)$ plane, definitively verifying the Joseph-Lundgren classification for $n=1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*