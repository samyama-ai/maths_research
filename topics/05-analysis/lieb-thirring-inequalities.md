---
id: 05-analysis/lieb-thirring-inequalities
title: "Lieb-Thirring Inequalities"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lieb-Thirring Inequalities

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/lieb-thirring-inequalities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For a real potential $V$ on $\mathbb{R}^d$ let $-\Delta + V$ act in $L^2(\mathbb{R}^d)$ and let $\lambda_1 \le \lambda_2 \le \dots < 0$ be its negative eigenvalues. The Lieb–Thirring inequality asserts

$$\sum_j |\lambda_j|^{\gamma} \;\le\; L_{\gamma,d} \int_{\mathbb{R}^d} V_-(x)^{\gamma + d/2}\,dx, \qquad V_- = \max(-V,0).$$

The inequality holds (with finite $L_{\gamma,d}$) exactly for $\gamma \ge 1/2$ when $d=1$, $\gamma > 0$ when $d = 2$, and $\gamma \ge 0$ when $d \ge 3$. **The open problem is the value of the sharp constant $L_{\gamma,d}$**, defined as the smallest admissible constant.

Two explicit candidates exist. The *semiclassical* constant, obtained by letting $V \to V(\varepsilon x)$ and applying Weyl asymptotics,

$$L^{\mathrm{sc}}_{\gamma,d} \;=\; (4\pi)^{-d/2}\,\frac{\Gamma(\gamma+1)}{\Gamma\!\big(\gamma+1+\tfrac d2\big)},$$

and the *one-bound-state* constant

$$L^{1}_{\gamma,d} \;=\; \sup_{V \ne 0}\ \frac{|\lambda_1(V)|^{\gamma}}{\int V_-^{\gamma+d/2}}.$$

Both are lower bounds: $L_{\gamma,d} \ge \max\{L^{1}_{\gamma,d}, L^{\mathrm{sc}}_{\gamma,d}\}$. The **Lieb–Thirring conjecture** (1976) is that equality holds,

$$L_{\gamma,d} \stackrel{?}{=} \max\{L^{1}_{\gamma,d},\, L^{\mathrm{sc}}_{\gamma,d}\},$$

with the most-cited instance $L_{1,3} = L^{\mathrm{sc}}_{1,3} = \tfrac{2}{15\pi^2}$, the constant governing the kinetic-energy bound used in the proof of stability of matter. A resolution requires either a proof of the matching upper bound or an explicit trial potential (or family of orthonormal functions in the dual formulation) exceeding the candidate ratio.

## 2. Mathematical Foundations

**Operator setting.** $-\Delta + V$ is defined as the form sum on $H^1(\mathbb{R}^d)$ with $V_- \in L^{\gamma + d/2}$; the negative spectrum is discrete and the Birman–Schwinger principle gives

$$\\#\{j : \lambda_j \le -e\} \;=\; \\#\{\mu \ge 1 \text{ eigenvalues of } K_e\}, \qquad K_e = V_-^{1/2}(-\Delta+e)^{-1}V_-^{1/2},$$

so that $\sum_j |\lambda_j|^\gamma = \gamma\int_0^\infty e^{\gamma-1}\,\\#\{\lambda_j \le -e\}\,de$.

**Semiclassics.** The phase-space heuristic replaces the counting function by
$$(2\pi)^{-d}\big|\{(x,\xi) : |\xi|^2 + V(x) \le -e\}\big|,$$
whose $\gamma$-moment integrates to $L^{\mathrm{sc}}_{\gamma,d}\int V_-^{\gamma+d/2}$. Hence $L^{\mathrm{sc}}$ is exactly the constant of the Weyl limit $\sum|\lambda_j(hV)|^\gamma h^{d} \to L^{\mathrm{sc}}_{\gamma,d}\int V_-^{\gamma+d/2}$ as $h\to0$.

**Dual (kinetic-energy) form.** For $\gamma = 1$ the inequality is equivalent by Legendre duality to: for any orthonormal $u_1,\dots,u_N \in H^1(\mathbb{R}^d)$ with density $\rho(x) = \sum_j |u_j(x)|^2$,

$$\sum_{j=1}^N \int |\nabla u_j|^2 \;\ge\; K_d \int_{\mathbb{R}^d} \rho(x)^{1+2/d}\,dx, \qquad K_d = \frac{2}{d}\Big(\frac{d}{(d+2)L_{1,d}}\Big)^{2/d}.$$

The conjecture $L_{1,3}=L^{\mathrm{sc}}_{1,3}$ is equivalent to $K_3 = \tfrac{3}{5}(6\pi^2)^{2/3}$, the Thomas–Fermi constant. For $N=1$ this reduces to Gagliardo–Nirenberg–Sobolev, so the conjecture says the Pauli-principle constant is exactly the free-electron-gas one.

**Boundary cases.** $\gamma = 0$, $d\ge3$ is the Cwikel–Lieb–Rozenblum bound $N(V) \le C_d\int V_-^{d/2}$; $\gamma=1/2$, $d=1$ is the critical endpoint, where the failure at $\gamma<1/2$ is shown by $V = -\alpha\delta$-type wells (any weak well binds).

## 3. History & State of the Art (SOTA)

- **1975–76.** Lieb and Thirring introduce the inequality to give a short proof of stability of matter, and conjecture the sharp constant. They prove the $d=1$, $\gamma=3/2$ case with $L_{3/2,1}=L^{\mathrm{sc}}_{3/2,1}=3/16$.
- **1978.** Aizenman and Lieb show $\gamma \mapsto L_{\gamma,d}/L^{\mathrm{sc}}_{\gamma,d}$ is non-increasing; sharpness at one $\gamma_0$ propagates to all $\gamma\ge\gamma_0$.
- **1978.** Glaser, Grosse and Martin compute $L^1_{\gamma,d}$ regimes where $L^1 > L^{\mathrm{sc}}$, fixing the "max" shape of the conjecture.
- **1990.** Helffer and Robert show $L_{\gamma,d} > L^{\mathrm{sc}}_{\gamma,d}$ for all $\gamma < 1$ in every dimension, ruling out purely semiclassical sharpness below $\gamma=1$.
- **1998.** Hundertmark, Lieb and Thomas prove the sharp endpoint $L_{1/2,1} = 1/2 = 2L^{\mathrm{sc}}_{1/2,1}$, attained by a single delta well.
- **2000.** Laptev and Weidl prove $L_{\gamma,d}=L^{\mathrm{sc}}_{\gamma,d}$ for **all $\gamma\ge3/2$ and all $d$**, by a matrix-valued one-dimensional inequality lifted dimension by dimension.
- **2008–2021.** Quantitative upper bounds for $\gamma=1$: Dolbeault–Laptev–Loss give constants via the Laptev–Weidl route; Frank, Hundertmark, Jex and Nam (2021) reduce the ratio to $L_{1,3} \le 1.456\,L^{\mathrm{sc}}_{1,3}$.
- **2021.** Frank, Gontier and Lewin construct trial states showing that the "max" form of the conjecture fails in some dimension/exponent ranges above $\gamma=1$ *(frontier — verify exact range)*, so the conjecture survives only in restricted regimes such as $\gamma=1$, $d=3$ and $1/2\le\gamma<3/2$, $d=1$.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $\gamma \ge 3/2$, all $d\ge1$ | **Solved**: $L_{\gamma,d}=L^{\mathrm{sc}}_{\gamma,d}$ (Laptev–Weidl 2000; $d=1$ by Lieb–Thirring 1976) |
| $\gamma = 1/2$, $d=1$ | **Solved**: $L_{1/2,1}=1/2=L^1_{1/2,1}$ (Hundertmark–Lieb–Thomas 1998) |
| $\gamma < 1$, all $d$ | Semiclassical value **excluded**: $L_{\gamma,d}>L^{\mathrm{sc}}_{\gamma,d}$ (Helffer–Robert 1990) |
| $\gamma = 1$, $d = 3$ | Open; best known $L_{1,3}\le 1.456\,L^{\mathrm{sc}}_{1,3}$ (Frank–Hundertmark–Jex–Nam 2021) |
| $1/2<\gamma<3/2$, $d=1$ | Open; conjectured $L_{\gamma,1}=L^1_{\gamma,1}$ up to the crossing point $\gamma=3/2$ |
| $\gamma=0$, $d\ge3$ (CLR) | Inequality holds; sharp constant open, known bounds within a factor $\approx 1.5$–$2$ of $L^{\mathrm{sc}}_{0,d}$ for large $d$ |
| Matrix/operator-valued $V$ | Sharp for $\gamma\ge3/2$ (Laptev–Weidl), the engine of the dimensional lifting |
| $\gamma \ge 1/2$, $d=1$, single-well $V$ | Sharpness known within the one-bound-state class by explicit ODE analysis |

## 5. Principal Obstacles

- **No known extremiser.** For $\gamma=1$, $d\ge2$ the optimising sequence is expected to be a many-bound-state configuration with no closed form; unlike Sobolev-type problems there is no conformal symmetry forcing a radial soliton, and concentration-compactness only yields dichotomy between the two candidate limits without excluding intermediate configurations.
- **Birman–Schwinger loses sharpness.** Estimating $\operatorname{Tr}K_e^p$ with $p$ chosen for integrability overshoots at the phase-space level; the Hilbert–Schmidt or Cwikel-type bounds have constants that are themselves not sharp, and no rearrangement inequality is known to close the gap.
- **Dimensional lifting stops at $3/2$.** The Laptev–Weidl argument needs the one-dimensional matrix inequality to hold with the *semiclassical* constant, true only for $\gamma\ge3/2$. Below that threshold the one-dimensional problem is itself non-semiclassical, and the induction fails at its base.
- **Non-commutativity of the many-body problem.** The dual form is a constrained optimisation over infinitely many orthonormal functions; the orthogonality constraint is not preserved by any known symmetrisation, so standard rearrangement (Pólya–Szegő) is unavailable.
- **The interpolation is one-sided.** Aizenman–Lieb monotonicity pushes information upward in $\gamma$, never downward, so the solved region $\gamma \ge 3/2$ gives no leverage at $\gamma=1$.

## 6. The Gap

Proven: $L_{\gamma,d} = L^{\mathrm{sc}}_{\gamma,d}$ for $\gamma\ge3/2$; $L_{1/2,1}=L^1_{1/2,1}$. Conjectured but open: the entire strip $1/2 < \gamma < 3/2$ in $d=1$, and $0\le\gamma<3/2$ in $d\ge2$, most sharply the single value $L_{1,3}$. The residual gap at $\gamma=1$, $d=3$ is the factor $1.456$: the exact step needed is an upper bound on $\operatorname{Tr}(-\Delta+V)_-$ that reproduces the phase-space volume without the loss incurred by decomposing the Birman–Schwinger kernel into low- and high-energy pieces. Equivalently, one must show no configuration of orthonormal functions beats the free-gas density in $\int|\nabla u_j|^2 / \int\rho^{5/3}$ — a statement about many-body interference for which no variational mechanism is currently known.

## 7. Current Research (as of June 2026)

- **Sharp-constant analysis via NLS for orthonormal systems.** Frank, Gontier and Lewin's programme translates the dual inequality into an infinite-component nonlinear Schrödinger problem and studies bifurcation from the single-soliton branch; this is what produced the counterexamples to the naive "max" form *(frontier — verify exact exponent ranges)*.
- **Improved Cwikel-type estimates.** Frank–Hundertmark–Jex–Nam's method, combining a Rumin-type argument with a careful splitting, is the current best route to constants; refinements aiming below $1.4\,L^{\mathrm{sc}}$ are active *(frontier — verify)*.
- **Extensions**: Lieb–Thirring inequalities with Hardy or magnetic terms, on domains and manifolds, for fractional and Jacobi operators, and for non-self-adjoint (complex $V$) operators, where even the correct exponent range is disputed.
- **Groups.** Caltech/LMU (Frank), KTH (Laptev), Ceremade–Paris Dauphine (Dolbeault, Lewin), Stuttgart (Weidl), Aalborg/Illinois (Hundertmark).

## 8. Future Work

- Prove sharpness for $d=1$, $1/2<\gamma<3/2$ within the one-bound-state class by a full ODE/inverse-scattering analysis; the trace formulas of Buslaev–Faddeev–Zakharov give exact identities at $\gamma=3/2$ that may deform.
- Determine the precise set of $(\gamma,d)$ where $L_{\gamma,d} > \max\{L^1,L^{\mathrm{sc}}\}$, replacing the conjecture with a corrected three-regime picture.
- Attack $L_{1,3}$ numerically: rigorous computer-assisted optimisation over finite orthonormal families to lower-bound $L_{1,3}/L^{\mathrm{sc}}_{1,3}$ and test whether $1$ is really optimal.
- Sharpen the CLR constant $L_{0,d}$ for large $d$, where the semiclassical ratio is conjectured to tend to $1$.

## 9. Key References

- **[Foundational]** E. H. Lieb, W. E. Thirring. *Bound for the kinetic energy of fermions which proves the stability of matter.* Physical Review Letters 35, 1975. [DOI](https://doi.org/10.1103/physrevlett.35.1116)
- **[Foundational]** E. H. Lieb, W. E. Thirring. *Inequalities for the moments of the eigenvalues of the Schrödinger Hamiltonian and their relation to Sobolev inequalities.* In *Studies in Mathematical Physics: Essays in Honor of Valentine Bargmann*, Princeton University Press, 1976.
- **[Foundational]** M. Aizenman, E. H. Lieb. *On semiclassical bounds for eigenvalues of Schrödinger operators.* Physics Letters A 66, 1978.
- **[Key result]** D. Hundertmark, E. H. Lieb, L. E. Thomas. *A sharp bound for an eigenvalue moment of the one-dimensional Schrödinger operator.* Advances in Theoretical and Mathematical Physics 2, 1998. [DOI](https://doi.org/10.4310/atmp.1998.v2.n4.a2)
- **[Key result]** A. Laptev, T. Weidl. *Sharp Lieb–Thirring inequalities in high dimensions.* Acta Mathematica 184, 2000. [DOI](https://doi.org/10.1007/bf02392782)
- **[Key result]** B. Helffer, D. Robert. *Riesz means of bounded states and semi-classical limit connected with a Lieb–Thirring conjecture.* Asymptotic Analysis 3, 1990.
- **[SOTA / Recent]** R. L. Frank, D. Hundertmark, M. Jex, P. T. Nam. *The Lieb–Thirring inequality revisited.* Journal of the European Mathematical Society 23, 2021. [DOI](https://doi.org/10.4171/jems/1062)
- **[SOTA / Recent]** R. L. Frank, D. Gontier, M. Lewin. *The nonlinear Schrödinger equation for orthonormal functions II: application to Lieb–Thirring inequalities.* Communications in Mathematical Physics 384, 2021. [DOI](https://doi.org/10.1007/s00220-021-04039-5)
- **[SOTA / Recent]** J. Dolbeault, A. Laptev, M. Loss. *Lieb–Thirring inequalities with improved constants.* Journal of the European Mathematical Society 10, 2008.
- **[Survey / Book]** R. L. Frank, A. Laptev, T. Weidl. *Schrödinger Operators: Eigenvalues and Lieb–Thirring Inequalities.* Cambridge Studies in Advanced Mathematics 200, Cambridge University Press, 2022.
- **[Survey]** R. L. Frank. *The Lieb–Thirring inequalities: Recent results and open problems.* In *Nine Mathematical Challenges*, Proceedings of Symposia in Pure Mathematics 104, AMS, 2021. [DOI](https://doi.org/10.1090/pspum/104/01877)

## 10. Worked Example / Concrete Special Case

**The sharp endpoint $\gamma=1/2$, $d=1$, via a single delta well.**

Take $V = -\alpha\delta_0$ on $\mathbb{R}$, $\alpha>0$ (a limit of narrow square wells). The operator $-\frac{d^2}{dx^2}-\alpha\delta_0$ has exactly one negative eigenvalue: matching $u(x)=e^{-\kappa|x|}$ across $0$ gives the jump condition $-2\kappa = -\alpha$, so $\kappa = \alpha/2$ and

$$\lambda_1 = -\kappa^2 = -\frac{\alpha^2}{4}, \qquad |\lambda_1|^{1/2} = \frac{\alpha}{2}.$$

The right side at $\gamma=1/2$, $d=1$ has exponent $\gamma+d/2 = 1$, so $\int V_-^{1} = \alpha$ exactly (this is why the delta is admissible: only the first moment enters). The ratio is

$$\frac{\sum_j |\lambda_j|^{1/2}}{\int V_-} = \frac{\alpha/2}{\alpha} = \frac12,$$

independent of $\alpha$. Hundertmark–Lieb–Thomas prove this is the maximum over all $V$, so $L_{1/2,1}=1/2$.

**Comparison with semiclassics.** Here
$$L^{\mathrm{sc}}_{1/2,1} = (4\pi)^{-1/2}\frac{\Gamma(3/2)}{\Gamma(2)} = \frac{1}{2\sqrt\pi}\cdot\frac{\sqrt\pi}{2} = \frac14 .$$
So $L_{1/2,1} = 2\,L^{\mathrm{sc}}_{1/2,1}$: the single bound state beats phase space by exactly a factor $2$. This is the clean instance of the $L^1 > L^{\mathrm{sc}}$ regime.

**Contrast at $\gamma=3/2$.** Repeating with the same delta well gives $|\lambda_1|^{3/2}=\alpha^3/8$, while $\int V_-^{2}=+\infty$ for a delta; regularising by a square well of depth $D$ and width $L$ with $DL=\alpha$ fixed and $L\to0$ makes $\int V_-^2 = D^2 L = \alpha^2/L \to \infty$. The ratio tends to $0$, so narrow wells are far from optimal at $\gamma=3/2$ — consistent with $L_{3/2,1}=L^{\mathrm{sc}}_{3/2,1}=3/16$, where wide slowly-varying wells (many bound states) are the optimisers. The open middle range $1/2<\gamma<3/2$ is precisely where these two competing mechanisms have not been separated.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*