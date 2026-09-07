---
id: 06-pdes/porous-medium-interface-regularity
title: "Porous Medium Interface Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Porous Medium Interface Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/porous-medium-interface-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $m > 1$ and let $u \geq 0$ solve the Cauchy problem for the porous medium equation (PME)

$$\partial_t u = \Delta (u^m) \quad \text{in } \mathbb{R}^N \times (0,\infty), \qquad u(\cdot,0) = u_0 \in L^1(\mathbb{R}^N),\ u_0 \geq 0,\ \operatorname{supp} u_0 \text{ compact.}$$

Solutions propagate with finite speed, so the **free boundary** (interface)

$$\Gamma = \partial \{(x,t) : u(x,t) > 0\} \cap (\mathbb{R}^N \times (0,\infty))$$

is a genuine hypersurface separating gas from vacuum. The problem: **describe the exact regularity of $\Gamma$ for arbitrary compactly supported $u_0 \geq 0$, at all times, in all dimensions $N \geq 2$.**

Three specific claims are open in general:

1. **(Eventual smoothness.)** There exists $T^* = T^*(u_0) < \infty$ such that $\Gamma \cap \{t > T^*\}$ is a real-analytic hypersurface, and the pressure $v = \tfrac{m}{m-1}u^{m-1}$ is analytic up to $\Gamma$ from inside.
2. **(Structure of the singular set.)** The set $\Sigma \subset \Gamma$ of points at which $\Gamma$ fails to be $C^\infty$ is closed, has parabolic Hausdorff dimension $\leq N-1$, and consists exactly of waiting-time points, focusing points, and merging points.
3. **(Optimal early regularity.)** For $t$ in the pre-$T^*$ regime, $\Gamma$ is $C^{1,\alpha}$ off $\Sigma$ with a dimension- and $m$-dependent $\alpha$, and no better in general.

A complete resolution must either prove (1)–(3) or exhibit a compactly supported $u_0$ whose interface is non-smooth for arbitrarily large times, or whose singular set is exotic (e.g. of full dimension, or fractal).

## 2. Mathematical Foundations

**Pressure formulation.** Set $v = \frac{m}{m-1} u^{m-1}$. Then $v \geq 0$ satisfies

$$\partial_t v = (m-1)\, v\, \Delta v + |\nabla v|^2 ,$$

a degenerate parabolic equation that becomes a first-order Hamilton–Jacobi (eikonal) equation on $\{v = 0\}$. Formally the interface moves with **Darcy velocity** $V = -\nabla v$; where $|\nabla v| > 0$ the free boundary is non-degenerate and the problem behaves like a one-phase Stefan/Hele-Shaw problem.

**Aronson–Bénilan estimate.** For any weak solution with $u_0 \ge 0$,

$$\Delta v \geq -\frac{\kappa}{t}, \qquad \kappa = \frac{N(m-1)}{N(m-1)+2}\cdot\frac{1}{m-1}\cdot\big(N(m-1)+2\big)\Big/1 ,$$

more usefully stated as $\partial_t u \geq -\frac{u}{(m-1+2/N)\,t}$ (Aronson–Bénilan, 1979). This is the semiconvexity engine behind every regularity result.

**Barenblatt profile.** The source-type solution with mass $M$ is

$$U(x,t) = t^{-\alpha}\Big( C - k\,|x|^2 t^{-2\alpha/N} \Big)_+^{1/(m-1)}, \qquad \alpha = \frac{N}{N(m-1)+2},\quad k = \frac{(m-1)\alpha}{2mN},$$

with interface the sphere $|x| = (C/k)^{1/2} t^{\alpha/N}$ — analytic in $t>0$.

**Waiting time.** A point $x_0 \in \partial\{u_0 > 0\}$ has positive waiting time $t^*(x_0) > 0$ iff $u_0$ vanishes fast enough: sharply (Aronson–Caffarelli–Kamin; Vázquez), $t^*(x_0)>0$ when $u_0(x) \le C|x-x_0|^{2/(m-1)}$ near $x_0$, and $t^*(x_0)=0$ when $\limsup |x-x_0|^{-2/(m-1)}u_0(x)=\infty$.

**Non-degeneracy.** The Daskalopoulos–Hamilton hypothesis: $v_0$ is $C^1$ on $\overline{\{v_0>0\}}$ with $|\nabla v_0| \geq c > 0$ on $\partial\{v_0>0\}$. This is the free-boundary analogue of a strict Lopatinski/Rankine–Hugoniot condition and makes the linearized problem a degenerate parabolic equation of **Baouendi–Grushin** type,

$$\mathcal{L} = x_N\big(\partial_{x_N}^2 + \textstyle\sum_{i<N}\partial_{x_i}^2\big) + \beta\,\partial_{x_N} - \partial_t ,$$

whose natural function spaces are weighted Hölder classes built from the **cycloidal metric** $\rho((x,t),(y,s)) = \frac{|x-y|}{\sqrt{x_N}+\sqrt{y_N}+\sqrt{|x-y|}} + \sqrt{|t-s|}$.

## 3. History & State of the Art (SOTA)

- **1950s–60s.** Zel'dovich–Kompaneets and Barenblatt construct the self-similar profile; Oleinik–Kalashnikov–Chzhou establish existence/uniqueness of weak solutions in 1D and finite propagation speed.
- **1969–1971.** Aronson proves regularity and the interface equation $\dot s(t) = -v_x(s(t)^-,t)$ in one dimension.
- **1980.** Caffarelli–Friedman, *Indiana Univ. Math. J.* 29: first $N$-dimensional result — the free boundary is Hölder continuous and $u$ is continuous.
- **1987.** Caffarelli–Vázquez–Wolanski: for compactly supported $u_0$ there is $T^*$ after which $v$ is Lipschitz and $\Gamma$ is a Lipschitz graph in space-time, and $|\nabla v| \geq c > 0$ near $\Gamma$.
- **1990.** Caffarelli–Wolanski, *CPAM* 43: Lipschitz + non-degenerate $\Rightarrow$ $\Gamma \in C^{1,\alpha}$. Combined with 1987, gives $C^{1,\alpha}$ interfaces for large time in all dimensions.
- **1987–88.** Aronson–Vázquez ($C^\infty$ and eventual concavity of the pressure in 1D) and Angenent (analyticity of the 1D interface after the waiting time) close the one-dimensional theory.
- **1998.** Daskalopoulos–Hamilton, *JAMS* 11: under non-degeneracy of $v_0$, $\Gamma$ is $C^\infty$ (indeed the pressure is smooth up to the boundary) for a short time $0 < t < \tau$. This introduced the Grushin-type weighted Schauder theory.
- **1999.** Koch's habilitation: non-Euclidean singular integrals give $C^\infty$/analytic regularity from $C^{1,\alpha}$ interfaces, upgrading Caffarelli–Wolanski.
- **2001.** Daskalopoulos–Hamilton–Lee, *Duke Math. J.* 108: all-time $C^\infty$ regularity of the interface for initial data whose support is a *convex* (or suitably geometric) domain with non-degenerate pressure.
- **2016–2018.** Kienzler; Kienzler–Koch–Vázquez, *Calc. Var. PDE* 57: **flatness implies smoothness** — a solution whose interface is $\varepsilon$-flat in a parabolic cylinder is analytic there, with quantitative constants. This is the PME analogue of De Giorgi's flatness theorem.

State of the art in one line: *away from a singular set, and after a large but non-explicit time, the interface is analytic; nothing rules out bad behaviour on the singular set or before that time.*

## 4. Partial Results / Verified Cases

- **$N = 1$, all $m>1$:** completely solved. The interface $x = s(t)$ is $C^\infty$ (Aronson–Vázquez 1987) and real-analytic (Angenent 1988) for $t > t^*(x_0)$, the waiting time. Before $t^*$ the interface is stationary; at $t = t^*$ it is generally only Lipschitz.
- **$N \geq 2$, large time:** for any compactly supported $u_0 \in L^1$, there is $T^*$ with $\Gamma \cap \{t > T^*\}$ Lipschitz (CVW 1987), hence $C^{1,\alpha}$ (Caffarelli–Wolanski 1990), hence $C^\infty$ and analytic (Koch 1999; KKV 2018).
- **Non-degenerate data, short time:** $v_0 \in C^1$, $|\nabla v_0| \geq c>0$ on $\partial\{v_0>0\}$, $\partial\{v_0>0\}$ of class $C^{1,\alpha}$ $\Rightarrow$ $\Gamma \in C^\infty$ on $(0,\tau)$ (Daskalopoulos–Hamilton 1998).
- **Convex/geometric data, all time:** $\{u_0>0\}$ convex with non-degenerate pressure $\Rightarrow$ $\Gamma \in C^\infty$ for all $t>0$; support stays convex and converges to the Barenblatt ball (Daskalopoulos–Hamilton–Lee 2001).
- **Radial data, all $N$:** interface is a single analytic curve $r = R(t)$ except at the focusing time when a hole closes.
- **Flat interfaces:** $\varepsilon_0(N,m)$-flatness in a cylinder $\Rightarrow$ analyticity, with explicit modulus (KKV 2018).
- **Explicit non-smoothness:** the Aronson–Graveleau focusing solution (1993) and the elongated-hole focusing computations of Angenent–Aronson–Betelu–Lowengrub (2001) exhibit interfaces with genuine singularities and *anomalous* (non-rational, numerically computed) self-similar exponents $\alpha(m,N)$.

## 5. Principal Obstacles

- **Degeneracy at the interface.** The equation for $v$ has diffusion coefficient $(m-1)v \to 0$ at $\Gamma$. Standard parabolic Schauder/Calderón–Zygmund theory does not apply; one must build a full Hölder–Schauder calculus for the Grushin operator in the cycloidal metric — done, but only under the *a priori* assumption $|\nabla v| \geq c > 0$, which is exactly what fails at singular points.
- **Degeneracy is not removable.** At a waiting-time point, $|\nabla v| = 0$ on the interface, so the free boundary is not a graph over the Darcy direction; the linearization becomes non-uniformly Grushin and the Schauder theory degenerates.
- **$T^*$ is not quantitative.** The Caffarelli–Vázquez–Wolanski time depends on the geometry of $\{u_0>0\}$ through compactness arguments (a limiting/blow-up argument with no rate). No proof gives $T^*$ in terms of $\|u_0\|_1$, $\operatorname{diam}(\operatorname{supp} u_0)$, and $m$.
- **Monotonicity formulas do not exist.** Alt–Caffarelli/Weiss-type monotonicity formulas, which classify blow-ups in the one-phase Bernoulli and Stefan problems, have no known PME analogue because the scaling $u_\lambda(x,t)=\lambda^{-\alpha}u(\lambda x,\lambda^{\beta}t)$ mixes mass and time and destroys the energy structure.
- **Anomalous exponents.** Focusing blow-ups have self-similar exponents that solve a nonlinear connection problem in an ODE phase plane and are *not* determined by dimensional analysis. Blow-up limits therefore cannot be enumerated algebraically, blocking the standard "classify blow-ups $\to$ epiperimetric inequality $\to$ regularity" program.
- **Topological changes.** Supports can merge and holes can close. Neither event is covered by any flatness theorem, and the flat-front stability theory of Kienzler is local and perturbative.

## 6. The Gap

Proven (§4) covers: $N=1$ fully; $N\ge 2$ *either* after an unquantified time $T^*$, *or* under a non-degeneracy hypothesis on $v_0$ that already assumes the interface is a nice graph. The general statement (§1) demands regularity for arbitrary compactly supported $u_0$ on the whole time interval.

The exact barrier is a **partial regularity theorem for degenerate free boundary points**: show that the set

$$\Sigma = \{(x,t) \in \Gamma : \liminf_{y\to x,\, y\in\{v>0\}} |\nabla v(y,t)| = 0\}$$

is small (parabolic Hausdorff dimension $\le N-1$, or at least measure zero in $\Gamma$) and that $\Gamma \setminus \Sigma$ is analytic. Everything else follows: KKV flatness plus a density/dimension bound on $\Sigma$ would give (2) and (3), and a quantitative version of CVW's non-degeneracy would give (1) with explicit $T^*$. Nobody has a mechanism for controlling $\Sigma$, because that requires either a monotonicity formula or a full classification of self-similar focusing profiles — both open.

## 7. Current Research (as of June 2026)

- **Flatness/regularity school (Koch, Kienzler, Vázquez; Bonn, Madrid).** Extending the flatness-implies-analyticity machinery to non-flat blow-ups and to the fast-diffusion range $m<1$, and pushing toward quantitative $T^*$ via invariant-manifold descriptions of the Barenblatt attractor. *(frontier — verify)*
- **Geometric-flows school (Daskalopoulos, Lee, Choi; Columbia, Yonsei, KIAS).** Convexity- and curvature-preservation methods; the goal is to replace convexity of $\operatorname{supp} u_0$ by weaker geometric hypotheses (star-shapedness, mean-convexity).
- **Viscosity/free-boundary school (Kim, Pozár, Feldman).** Homogenization and viscosity-solution methods transferring one-phase Hele-Shaw regularity ($m\to\infty$ limit) back to finite $m$.
- **Asymptotic stability (Seis, Denzler, McCann).** Spectral analysis of the linearization at the Barenblatt profile in self-similar variables gives sharp convergence rates and, by implication, sharp control of the interface for large time — the most promising route to a *quantitative* $T^*$. *(frontier — verify)*
- **Numerics on focusing.** High-accuracy continuation of the anomalous exponents $\alpha(m,N)$ for non-radial holes, following the Angenent–Aronson–Betelu–Lowengrub program.

## 8. Future Work

1. **Find a monotonicity formula.** A Weiss- or Almgren-type quantity for the pressure in cycloidal geometry would immediately give blow-up classification and a stratification of $\Sigma$. Vázquez has repeatedly flagged this as the decisive missing tool.
2. **Quantify $T^*$.** Replace the compactness argument in CVW 1987 with a proof using the Aronson–Bénilan estimate plus the sharp $L^1$–$L^\infty$ smoothing, yielding $T^* \le C(N,m)\,\mathrm{diam}(\operatorname{supp}u_0)^{N(m-1)+2}\|u_0\|_1^{-(m-1)}$.
3. **Classify focusing profiles.** Prove uniqueness of the Aronson–Graveleau profile among radial focusing self-similar solutions, then prove non-radial holes converge to it after rescaling.
4. **Merging.** Develop a local theory for two touching supports; even the 1D case at the merge instant lacks a sharp regularity statement.
5. **Transfer $m<1$.** Fast diffusion has no interface (infinite propagation) for $m > (N-2)_+/N$, but signed and boundary-value problems have analogous degenerate boundary regularity questions; techniques should be shared.

## 9. Key References

- **[Foundational]** D. G. Aronson, J. L. Vázquez. *Eventual $C^\infty$-regularity and concavity for flows in one-dimensional porous media.* Arch. Rational Mech. Anal. 99 (1987), 329–348.
- **[Foundational]** L. A. Caffarelli, A. Friedman. *Regularity of the free boundary of a gas flow in an $n$-dimensional porous medium.* Indiana Univ. Math. J. 29 (1980), 361–391.
- **[Foundational]** L. A. Caffarelli, J. L. Vázquez, N. I. Wolanski. *Lipschitz continuity of solutions and interfaces of the $N$-dimensional porous medium equation.* Indiana Univ. Math. J. 36 (1987), 373–401.
- **[Foundational]** L. A. Caffarelli, N. I. Wolanski. *$C^{1,\alpha}$ regularity of the free boundary for the $N$-dimensional porous media equation.* Comm. Pure Appl. Math. 43 (1990), 885–902.
- **[Foundational]** S. B. Angenent. *Analyticity of the interface of the porous media equation after the waiting time.* Proc. Amer. Math. Soc. 102 (1988), 329–336.
- **[SOTA]** P. Daskalopoulos, R. Hamilton. *Regularity of the free boundary for the porous medium equation.* J. Amer. Math. Soc. 11 (1998), 899–965.
- **[SOTA]** P. Daskalopoulos, R. Hamilton, K. Lee. *All time $C^\infty$-regularity of the interface in degenerate diffusion: a geometric approach.* Duke Math. J. 108 (2001), 295–327.
- **[SOTA]** H. Koch. *Non-Euclidean singular integrals and the porous medium equation.* Habilitationsschrift, Universität Heidelberg, 1999.
- **[SOTA]** C. Kienzler, H. Koch, J. L. Vázquez. *Flatness implies smoothness for solutions of the porous medium equation.* Calc. Var. Partial Differential Equations 57 (2018), art. 18.
- **[SOTA]** C. Kienzler. *Flat fronts and stability for the porous medium equation.* Comm. Partial Differential Equations 41 (2016), 1793–1838.
- **[Singularities]** D. G. Aronson, J. Graveleau. *A selfsimilar solution to the focusing problem for the porous medium equation.* European J. Appl. Math. 4 (1993), 65–81.
- **[Singularities]** S. B. Angenent, D. G. Aronson. *The focusing problem for the radially symmetric porous medium equation.* Comm. Partial Differential Equations 20 (1995), 1217–1240.
- **[Singularities]** S. B. Angenent, D. G. Aronson, S. I. Betelú, J. S. Lowengrub. *Focusing of an elongated hole in porous medium flow.* Physica D 151 (2001), 228–252.
- **[Asymptotics]** C. Seis. *Long-time asymptotics for the porous medium equation: the spectrum of the linearized operator.* J. Differential Equations 256 (2014), 1191–1223.
- **[Survey / Book]** J. L. Vázquez. *The Porous Medium Equation: Mathematical Theory.* Oxford Mathematical Monographs, Oxford Univ. Press, 2007.
- **[Survey / Book]** L. A. Caffarelli, S. Salsa. *A Geometric Approach to Free Boundary Problems.* Graduate Studies in Mathematics 68, AMS, 2005.

## 10. Worked Example / Concrete Special Case

**Barenblatt interface in $N=1$, $m=2$.** Here $\alpha = \frac{N}{N(m-1)+2} = \frac{1}{3}$ and $k = \frac{(m-1)\alpha}{2mN} = \frac{1/3}{4} = \frac{1}{12}$, so

$$u(x,t) = t^{-1/3}\Big(C - \frac{x^2}{12\,t^{2/3}}\Big)_+, \qquad v = \frac{m}{m-1}u^{m-1} = 2u .$$

The interface is $x = \pm s(t)$ with $s(t) = \sqrt{12C}\; t^{1/3}$, and $\dot s(t) = \tfrac{1}{3}\sqrt{12C}\,t^{-2/3}$.

Check the Darcy law $\dot s = -v_x(s^-,t)$: from $v = 2t^{-1/3}\big(C - \frac{x^2}{12t^{2/3}}\big)$ we get $v_x = -\frac{x}{3t}$, so

$$-v_x(s(t)^-,t) = \frac{s(t)}{3t} = \frac{\sqrt{12C}\,t^{1/3}}{3t} = \tfrac{1}{3}\sqrt{12C}\;t^{-2/3} = \dot s(t). \checkmark$$

Non-degeneracy holds: $|v_x(s^-,t)| = \tfrac{1}{3}\sqrt{12C}\,t^{-2/3} > 0$ for every $t>0$, and the interface is real-analytic. This is the *generic good case*.

**Contrast: a waiting-time point.** Take $m=2$, $N=1$, and $v_0(x) = (-x)_+^2$ near the origin (so $u_0(x) = \tfrac12 (-x)_+^{2} = O(|x|^{2/(m-1)})$, exactly the borderline decay). Insert the ansatz $v(x,t) = a(-x + b t)_+^2$: then $v_t = 2ab(-x+bt)$, $v\,v_{xx} = 2a^2(-x+bt)^2$, $|v_x|^2 = 4a^2(-x+bt)^2$, and the pressure equation $v_t = v v_{xx} + v_x^2$ requires $2ab(-x+bt) = 6a^2(-x+bt)^2$, which fails identically — the quadratic corner is not a travelling wave. The correct behaviour (Aronson–Caffarelli–Kamin; Vázquez, Ch. 15) is that the interface **does not move** for a positive waiting time $t^* > 0$: $|v_x| \to 0$ at the front, the Darcy velocity vanishes, and the front only starts moving once mass has diffused forward.

At $x=0$, $t=t^*$ the interface $s(t)$ is Lipschitz but not $C^1$: $s \equiv 0$ on $[0,t^*]$ and $s(t) \sim c\,(t-t^*)$ afterwards. Every $C^\infty$ theorem of §4 excludes this point by hypothesis — the Daskalopoulos–Hamilton non-degeneracy assumption $|\nabla v_0| \ge c>0$ fails here, and the Caffarelli–Vázquez–Wolanski time $T^*$ is chosen larger than $t^*$. In $N\ge2$ the analogous degenerate points can occur on a whole subset of $\Gamma$ and can also arise dynamically (focusing, merging), which is precisely the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*