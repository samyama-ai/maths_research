---
id: 06-pdes/hunter-saxton-weak-solutions
title: "Hunter Saxton Weak Solutions"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hunter–Saxton Equation: Weak Solutions, Admissibility and Uniqueness

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/hunter-saxton-weak-solutions` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Hunter–Saxton (HS) equation
$$(u_t + u u_x)_x = \tfrac12 u_x^2$$
develops a singularity in finite time from every non-constant smooth initial datum: $u$ stays continuous but $u_x \to -\infty$ on a set of positive measure, and the energy density $u_x^2\,dx$ concentrates on a set of measure zero. Past that time the Cauchy problem admits **infinitely many** distributional solutions with the same data.

The problem is to select a physically meaningful class of weak solutions and prove that the Cauchy problem is well posed in it. Concretely:

1. **(Solved)** Existence of global weak solutions for $u_{0,x} \in L^2$, in both the *conservative* class (total energy $\int u_x^2 dx$ constant) and the *dissipative* class (energy nonincreasing, with maximal loss at concentration).
2. **(Solved for the two extremes)** Uniqueness and Lipschitz continuous dependence in each of those two classes.
3. **(Open)** A single admissibility criterion — stated intrinsically on the weak solution, not through a Lagrangian construction — that singles out one solution per datum, and that covers the intermediate $\alpha$-dissipative family $\alpha \in (0,1)$ in which a fixed fraction $\alpha$ of the concentrating energy is removed. Equivalently: is "maximal dissipation" in the sense of Dafermos the right selection principle, and does it determine the solution for all $u_{0,x}\in L^2$?
4. **(Open)** Transfer of these results to the parent nonlinear variational wave equation $u_{tt} - c(u)(c(u)u_x)_x = 0$, of which HS is the high-frequency asymptotic limit.

A complete resolution means: an Eulerian-side admissibility condition plus a proof of uniqueness and stability under it, for the full class of finite-energy data.

## 2. Mathematical Foundations

**Derivation.** Hunter and Saxton (1991) obtained the equation for the director field of a nematic liquid crystal, as the asymptotic equation for weakly nonlinear orientation waves. Writing $u$ for the rescaled director angle gradient, one gets the nonlocal form (real line, $\int u_x^2 dx = E_0$):
$$u_t + u u_x = \tfrac12 \int_{-\infty}^{x} u_y^2 \, dy ,$$
and on the circle, with the mean-zero normalisation $\int_{\mathbb T} u_x \,dx = 0$,
$$u_t + u u_x = \tfrac14\Big(\int_{0}^{x} - \int_{x}^{1}\Big) u_y^2\,dy .$$

**Weak solution.** $u \in L^\infty_{loc}([0,\infty); H^1_{loc})$ is a weak solution if for all $\varphi \in C_c^\infty$
$$\int_0^\infty\!\!\int_{\mathbb R} \Big( u\varphi_t + \tfrac12 u^2 \varphi_x + \tfrac12\Big(\int_{-\infty}^x u_y^2 dy\Big)\varphi \Big)\,dx\,dt + \int u_0 \varphi(\cdot,0)\,dx = 0 .$$

**Characteristics and the Riccati mechanism.** Along $\dot y = u(y,t)$ the equation reduces to
$$\frac{d}{dt}\,u_x = -\tfrac12 u_x^2 \quad\Longrightarrow\quad u_x(t) = \frac{u_{0,x}}{1 + \tfrac{t}{2}u_{0,x}},$$
so wave breaking occurs at $T^\ast = -2/\inf_x u_{0,x}$ whenever $\inf u_{0,x} < 0$. This is the exact solvability that makes HS a model case: blow-up is a pointwise Riccati blow-up, not a genuinely nonlocal effect.

**Energy measure.** Define a nonnegative Radon measure $\mu(t)$ with $\mu_{ac}(t) = u_x^2\,dx$. Conservative solutions satisfy $\mu(t)(\mathbb R) = E_0$ for all $t$ and the transport identity
$$\mu_t + (u\mu)_x = 0 \quad\text{in }\mathcal D'.$$
Dissipative solutions instead drop the singular part at the moment of concentration: $\mu(t) = u_x^2 dx$ for a.e. $t$, and $t \mapsto \mu(t)(\mathbb R)$ is nonincreasing. The $\alpha$-dissipative family keeps a fraction $1-\alpha$ of each concentrating atom.

**Lagrangian change of variables.** Setting $y(t,\xi)$ the flow map and $U = u\circ y$, $q = y_\xi$, $v = u_x\circ y \cdot y_\xi$, the HS system becomes a semilinear ODE system in a Banach space, globally solvable; solutions of the PDE are recovered by pushing forward. All existence proofs since Bressan–Constantin (2005) use this.

**Geometry.** Lenells (2007) showed the periodic HS equation is the geodesic equation of the homogeneous $\dot H^1$ right-invariant metric on $\mathrm{Diff}(\mathbb S^1)/\mathbb S^1$, and that this space is isometric to a subset of an $L^2$ sphere; geodesics are then arcs of great circles, and blow-up is the geodesics reaching the boundary of the diffeomorphism group in finite time. Khesin–Misiołek placed this in the Euler–Arnold framework.

## 3. History & State of the Art (SOTA)

- **1991.** Hunter & Saxton derive the equation (*SIAM J. Appl. Math.* 51).
- **1994.** Hunter & Zheng find bi-Hamiltonian structure, a Lax pair and complete integrability (*Physica D* 79).
- **1995.** Hunter & Zheng construct global weak solutions of both dissipative and conservative type for data with $u_{0,x}$ of bounded variation, via viscous and dispersive regularisations (*ARMA* 129, two parts).
- **2000.** Zhang & Zheng extend existence to general $u_{0,x}\in L^2$ and prove uniqueness of the dissipative solution under an Oleinik-type one-sided condition (*ARMA* 155).
- **2005.** Bressan & Constantin give the definitive Lagrangian construction: two continuous semigroups (conservative, dissipative) on $H^1$-type spaces (*SIAM J. Math. Anal.* 37).
- **2010.** Bressan, Holden & Raynaud build an explicit Lipschitz metric under which the conservative flow is a Lipschitz semigroup — optimal-transport-flavoured, since the $H^1$ distance is not preserved (*J. Math. Pures Appl.* 94).
- **2011.** Dafermos re-proves existence and uniqueness of dissipative solutions purely in Eulerian variables via generalized characteristics (*J. Hyperbolic Differ. Equ.* 8).
- **2016.** Cieślak & Jamróz show that for bounded-energy data the *maximal dissipation* criterion selects exactly the dissipative solution (*Adv. Math.* 290).
- **2018–2022.** Grunert, Nordli, Solem and collaborators develop $\alpha$-dissipative theory and convergent numerical schemes.

## 4. Partial Results / Verified Cases

- **Conservative class, $u_{0,x}\in L^2(\mathbb R)$ or periodic mean-zero:** global existence (Bressan–Constantin 2005), uniqueness among solutions satisfying the energy-transport identity with $\mu$ absolutely continuous for a.e. $t$, and Lipschitz stability in the Bressan–Holden–Raynaud metric (2010).
- **Dissipative class:** existence for all $u_{0,x}\in L^2$; uniqueness proved by Zhang–Zheng (2000) under $u_x \le 2/t$ (the sharp one-sided Oleinik bound implied by the Riccati equation), and independently by Dafermos (2011) by generalized characteristics with no BV assumption.
- **$u_{0,x}\in BV$:** the full structure of the singular set is known — energy concentrates on an at most countable family of points, and the solution is piecewise smooth away from them (Hunter–Zheng 1995).
- **$\alpha$-dissipative, $\alpha\in[0,1]$ constant:** existence and, for the two-component HS system, Lipschitz stability in a suitable metric (Grunert–Nordli 2018); genuine continuity in $\alpha$ fails at $\alpha \in (0,1)$ in general.
- **Selection principle:** maximal dissipation $=$ dissipative solution, proved for bounded energy data by Cieślak–Jamróz (2016).
- **Piecewise-linear data:** completely explicit; solutions are computable in closed form (Section 10), and numerical schemes converge to the conservative solution at observed rate $\sim h^{1/2}$ in the BHR metric (Grunert–Nordli–Solem, *BIT* 2021).

## 5. Principal Obstacles

- **Loss of the natural metric.** The $H^1$ norm is conserved but the $H^1$ *distance* between two solutions is not controlled: characteristics from different solutions cross, and Grönwall arguments fail exactly at concentration times. Any stability statement must be made in a non-Hilbertian, transport-type metric constructed after the fact.
- **The singular measure is not a function of $u$.** Two conservative solutions can agree as functions $u$ on a time interval yet carry different $\mu$. So $u$ alone is not a state variable; the natural state is the pair $(u,\mu)$, and no purely Eulerian PDE closure for $\mu$ is known that is stable under weak limits.
- **Non-uniqueness is generic, not exceptional.** Standard hyperbolic admissibility (entropy conditions, Lax shock inequalities) has no counterpart: HS is not a conservation law in $u$, there is no shock, and $u$ itself remains continuous. Kruzhkov-type $L^1$ contraction machinery has no starting point.
- **Lagrangian coordinates are not canonical.** All uniqueness proofs pass through a relabelling-invariant Lagrangian formulation; recovering uniqueness *in the Eulerian class* requires showing that every weak solution is the push-forward of a Lagrangian one, which is only known under extra regularity (BV, or one-sided Oleinik bounds).
- **$\alpha$-dissipation breaks semigroup rigidity.** For $\alpha\in(0,1)$ the "fraction of energy removed" depends on the decomposition of $\mu$ into atoms, which is not stable under limits, so the flow is not continuous with respect to data in any known metric uniformly in $\alpha$.

## 6. The Gap

Proven: two isolated, well-posed semigroups sit at the extreme points $\alpha = 0$ (conservative) and $\alpha = 1$ (dissipative), each characterised by a construction (Lagrangian variables or generalized characteristics) rather than by an intrinsic condition on the Eulerian solution.

Missing: a single admissibility condition $\mathcal A(u,\mu) \ge 0$, checkable on a distributional solution, such that (i) for every $u_{0,x}\in L^2$ exactly one solution satisfies $\mathcal A$ within each prescribed dissipation regime, and (ii) the map $u_0 \mapsto u$ is continuous in a metric independent of the construction. The concrete barrier is the concentration instant: at $t = T^\ast$ the map from data to solution loses injectivity because the atom's mass, and how much of it is returned to the absolutely continuous part, is not determined by $u(\cdot,T^\ast)$. Crossing the gap requires either (a) a variational/entropy functional whose extremisation reproduces the whole $\alpha$-family, or (b) a proof that every Eulerian weak solution with $u_x \le 2/t$ arises from a Lagrangian one, without BV.

## 7. Current Research (as of June 2026)

- **NTNU Trondheim (Grunert, Nordli, Solem; with Holden, Raynaud).** $\alpha$-dissipative solutions with $\alpha = \alpha(u)$ variable, Lipschitz metrics for the HS and two-component HS systems, and convergence proofs for finite-difference and finite-element schemes. *(frontier — verify)* Recent work claims a Lipschitz metric for the full $\alpha$-dissipative family under a bounded-variation restriction on the concentrating set (Grunert–Tandy).
- **Penn State (Bressan and collaborators).** Generic regularity of conservative solutions and uniqueness via characteristics, transferred from Camassa–Holm and the variational wave equation to HS; the aim is a "generic well-posedness" statement — well-posedness for an open dense set of data in a Baire sense.
- **Warsaw (Cieślak, Jamróz).** Maximal-dissipation selection beyond bounded energy; connections to regular Lagrangian flows in the DiPerna–Lions sense.
- **Geometric school (Lenells, Khesin, Misiołek, Modin).** HS as geodesic flow; the sphere isometry gives closed-form solutions and suggests that weak solutions correspond to geodesics continued past the cut locus — a possible intrinsic selection principle. *(frontier — verify)*
- **Integrable-systems side.** Use of the Hunter–Zheng Lax pair and inverse-scattering-type transforms to characterise post-blow-up continuation; so far only for special classes.

## 8. Future Work

- Prove or disprove: every Eulerian weak solution with $u_x(x,t) \le 2/t$ coincides with the Dafermos dissipative solution, for arbitrary $L^2$ data.
- Construct a convex functional on $(u,\mu)$ whose gradient flow / minimisation reproduces the $\alpha$-dissipative semigroup, giving a variational admissibility condition.
- Extend the BHR Lipschitz metric to $\alpha \in (0,1)$ with constants uniform in $\alpha$, or exhibit a counterexample showing this is impossible.
- Lift the HS results to the nonlinear variational wave equation $u_{tt} = c(u)(c(u)u_x)_x$, where conservative existence is known (Holden–Raynaud 2011) but uniqueness for general $c$ is open.
- Establish rates of convergence for numerical schemes in the conservative metric; current evidence is $O(h^{1/2})$ and unproved.

## 9. Key References

- **[Foundational]** J. K. Hunter, R. Saxton. *Dynamics of director fields.* SIAM Journal on Applied Mathematics 51 (1991), 1498–1521.
- **[Foundational]** J. K. Hunter, Y. Zheng. *On a completely integrable nonlinear hyperbolic variational equation.* Physica D 79 (1994), 361–386.
- **[Foundational]** J. K. Hunter, Y. Zheng. *On a nonlinear hyperbolic variational equation I: Global existence of weak solutions; II: The zero-viscosity and dispersion limits.* Archive for Rational Mechanics and Analysis 129 (1995), 305–353 and 355–383.
- **[Foundational]** P. Zhang, Y. Zheng. *Existence and uniqueness of solutions of an asymptotic equation arising from a variational wave equation with general data.* Archive for Rational Mechanics and Analysis 155 (2000), 49–83.
- **[SOTA]** A. Bressan, A. Constantin. *Global solutions of the Hunter–Saxton equation.* SIAM Journal on Mathematical Analysis 37 (2005), 996–1026.
- **[SOTA]** A. Bressan, H. Holden, X. Raynaud. *Lipschitz metric for the Hunter–Saxton equation.* Journal de Mathématiques Pures et Appliquées 94 (2010), 68–92.
- **[SOTA]** C. M. Dafermos. *Generalized characteristics and the Hunter–Saxton equation.* Journal of Hyperbolic Differential Equations 8 (2011), 159–168.
- **[SOTA]** T. Cieślak, G. Jamróz. *Maximal dissipation in Hunter–Saxton equation for bounded energy initial data.* Advances in Mathematics 290 (2016), 590–613.
- **[Recent]** K. Grunert, A. Nordli. *Existence and Lipschitz stability for $\alpha$-dissipative solutions of the two-component Hunter–Saxton system.* Journal of Hyperbolic Differential Equations 15 (2018), 559–597.
- **[Recent]** K. Grunert, A. Nordli, S. Solem. *Numerical conservative solutions of the Hunter–Saxton equation.* BIT Numerical Mathematics 61 (2021), 941–976.
- **[Structural]** J. Lenells. *The Hunter–Saxton equation describes the geodesic flow on a sphere.* Journal of Geometry and Physics 57 (2007), 2049–2064.
- **[Structural]** B. Khesin, G. Misiołek. *Euler equations on homogeneous spaces and Virasoro orbits.* Advances in Mathematics 176 (2003), 116–144.
- **[Related]** H. Holden, X. Raynaud. *Global semigroup of conservative solutions of the nonlinear variational wave equation.* Archive for Rational Mechanics and Analysis 201 (2011), 871–964.
- **[Survey]** A. Bressan. *Uniqueness of conservative solutions for nonlinear wave equations via characteristics.* Bulletin of the Brazilian Mathematical Society 47 (2016), 157–169.

## 10. Worked Example / Concrete Special Case

Take on $\mathbb R$ the piecewise-linear datum with $u_{0,x} = -\mathbf 1_{(0,1)}$:
$$u_0(x) = \begin{cases} 0, & x \le 0,\\ -x, & 0 < x < 1,\\ -1, & x \ge 1,\end{cases} \qquad E_0 = \int u_{0,x}^2\,dx = 1 .$$

**Riccati slope.** On the middle interval $u_{0,x} = -1$, so along characteristics $u_x(t) = -1/(1 - t/2) = -2/(2-t)$: blow-up at $T^\ast = 2$. Outside, $u_{0,x}=0$ stays $0$.

**Explicit solution for $0 \le t < 2$.** The left endpoint sits at $x=0$ where $u=0$, so it does not move. Put $\ell(t) = (2-t)^2/4$ and
$$u(x,t) = \begin{cases} 0, & x \le 0,\\[2pt] -\dfrac{2x}{2-t}, & 0<x<\ell(t),\\[6pt] -\dfrac{2-t}{2}, & x \ge \ell(t).\end{cases}$$
*Check.* Right endpoint: $\dot\ell = -(2-t)/2 = u(\ell,t)$ ✓. Middle: $u_t + uu_x = -\frac{2x}{(2-t)^2} + \frac{4x}{(2-t)^2} = \frac{2x}{(2-t)^2}$, while $\frac12\int_{-\infty}^x u_y^2\,dy = \frac12 \cdot \frac{4x}{(2-t)^2} = \frac{2x}{(2-t)^2}$ ✓. Right region: $u_t = \frac12$ and $\frac12\int_{\mathbb R}u_y^2 = \frac12 E_0 = \frac12$ ✓.

**Energy.** $\int u_x^2\,dx = \frac{4}{(2-t)^2}\cdot \frac{(2-t)^2}{4} = 1$ for all $t<2$: energy is conserved while the support shrinks to the point $x=0$. At $t=2$, $u(\cdot,2)\equiv 0$ and $\mu(2) = \delta_0$ — a pure atom, invisible in $u$.

**Non-uniqueness after $T^\ast$.** Two continuations from the same state:
- *Dissipative:* $u \equiv 0$ for $t \ge 2$; energy drops from $1$ to $0$ at $t=2$.
- *Conservative:* mirror the construction, $u(x,t) = \frac{2x}{t-2}$ on $0<x<(t-2)^2/4$ and $u = \frac{t-2}{2}$ to the right; energy returns to $1$ instantly.
- *$\alpha$-dissipative:* keep amplitude $\sqrt{1-\alpha}$, i.e. replace the slope by $\sqrt{1-\alpha}\,\cdot \frac{2}{t-2}$ on a correspondingly rescaled interval, giving energy $1-\alpha$.

All three are distributional solutions with identical data. This one-parameter family is the entire well-posedness problem in miniature: $u(\cdot,2)$ carries no information about which branch to take, and the selection must be made by an admissibility condition that current theory supplies only at $\alpha = 0$ and $\alpha = 1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*