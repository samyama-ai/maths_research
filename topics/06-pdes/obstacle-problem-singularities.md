---
id: 06-pdes/obstacle-problem-singularities
title: "Obstacle Problem Singularities"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Obstacle Problem Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/obstacle-problem-singularities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For the classical obstacle problem $\Delta u = \chi_{\{u>0\}}$, $u \ge 0$, the free boundary $\partial\{u>0\}$ splits into a **regular set** (locally a real-analytic hypersurface) and a **singular set** $\Sigma$ (points where the contact set $\{u=0\}$ has vanishing density). The open problem has three linked parts.

1. **Sharp size of $\Sigma$ for generic data.** *Schaeffer's conjecture* (1974): for generic boundary data / obstacles the free boundary is a smooth manifold. Proved in $n=2$ (Schaeffer, Monneau) and in low dimensions by Figalli–Ros-Oton–Serra. Open: in every dimension $n\ge 5$, is
$$\dim_{\mathcal H}\Sigma(u_t) \le n-4 \quad \text{for a.e. } t,$$
and is the exponent $n-4$ attained?
2. **Structure of $\Sigma$ for a *fixed* solution.** Is each stratum $\Sigma_k$ locally contained in a $C^{1,1}$ (or $C^\infty$, or analytic) $k$-dimensional manifold, outside an explicitly small exceptional set? The known top-stratum result is $C^{1,1}$; the "anomalous" exceptional points are only known to have dimension $\le k-1$.
3. **Higher-order asymptotics.** At every singular point the blow-up is a unique quadratic polynomial; the open question is the sharp expansion beyond second order, and whether the degenerate ("anomalous") behaviour that blocks $C^{1,\alpha}$ regularity of $\Sigma_k$ can actually occur.

A complete resolution of (1) means: an example realising dimension $n-4$ for a positive-measure set of parameters, plus a matching upper bound in all dimensions. A disproof means a family with generically larger singular set.

## 2. Mathematical Foundations

Let $\Omega\subset\mathbb R^n$ be bounded and $g\in H^1(\Omega)$, $g \ge 0$. Minimise
$$J(v)=\int_\Omega \Big(\tfrac12|\nabla v|^2+v\Big)\,dx, \qquad v\in \mathcal K=\{v\in H^1(\Omega): v\ge 0,\ v-g\in H^1_0(\Omega)\}.$$
The minimiser $u$ is unique and satisfies the complementarity system
$$u\ge 0,\qquad \Delta u=\chi_{\{u>0\}}\ \text{ a.e. in }\Omega .$$
Optimal interior regularity is $u\in C^{1,1}_{\rm loc}$ (Frehse; Caffarelli), and this is sharp. The **free boundary** is $\Gamma=\partial\{u>0\}\cap\Omega$.

**Blow-ups.** For $x_0\in\Gamma$ set $u_r(x)=r^{-2}u(x_0+rx)$. By $C^{1,1}$ bounds the family is compact in $C^1_{\rm loc}$, and Weiss's monotonicity formula
$$W(r,u,x_0)=\frac{1}{r^{n+2}}\int_{B_r(x_0)}\big(|\nabla u|^2+2u\big)-\frac{2}{r^{n+3}}\int_{\partial B_r(x_0)}u^2,\qquad \frac{d}{dr}W \ge 0,$$
forces every blow-up limit to be $2$-homogeneous. **Caffarelli's dichotomy** (1977, 1998): every blow-up is either
- a **half-space solution** $u_0(x)=\tfrac12 (x\cdot e)_+^2$, $|e|=1$ — then $x_0$ is *regular*; or
- a **singular polynomial** $u_0=p$, where $p\ge0$ is a quadratic form with
$$\Delta p=1,\qquad p\ge 0,\qquad p(0)=0,\qquad \dim\ker p =: k \in\{0,\dots,n-1\},$$
i.e. $p(x)=\tfrac12 x^\top A x$ with $A\ge0$, $\operatorname{tr}A=1$ — then $x_0\in\Sigma_k$, the $k$-th singular stratum, and $\Sigma=\bigcup_{k=0}^{n-1}\Sigma_k$.

**Uniqueness of blow-up at singular points** follows from Monneau's monotonicity formula: for $p$ a singular quadratic,
$$M(r,u,x_0,p)=\frac{1}{r^{n+3}}\int_{\partial B_r(x_0)}(u-p)^2 \quad\text{is nondecreasing in } r .$$
Consequently $x_0\mapsto p_{x_0}$ is well defined and continuous on $\Sigma_k$, and Whitney extension plus the implicit function theorem give $\Sigma_k\subset$ countable union of $C^1$ $k$-manifolds (Caffarelli 1998).

The regular set is open in $\Gamma$, is locally a $C^{1,\alpha}$ graph (Caffarelli 1977), and is real-analytic by Kinderlehrer–Nirenberg (1977) via hodograph–Legendre transform. All the difficulty is at $\Sigma$.

## 3. History & State of the Art (SOTA)

- **1964–72.** Variational formulation by Fichera, Stampacchia, Lions–Stampacchia; $C^{1,1}$ regularity of $u$ (Frehse 1972).
- **1974–77.** Schaeffer constructs free boundaries that are not smooth and conjectures generic smoothness (Ann. SNS Pisa, 1977). Caffarelli proves the regular/singular dichotomy and $C^{1,\alpha}$ regularity of the regular set (Acta Math. 1977). Caffarelli–Rivière analyse singular points in $n=2$ (Ann. of Math. 1977).
- **1998–2003.** Caffarelli's "obstacle problem revisited": stratification and $C^1$-rectifiability of $\Sigma_k$. Weiss (1999) and Monneau (2003) supply the monotonicity formulas that make the argument robust and dimension-free. Monneau proves Schaeffer's conjecture in $n=2$.
- **2018.** Colombo–Spolaor–Velichkov prove a **logarithmic epiperimetric inequality**, upgrading $C^1$-rectifiability to a quantitative rate: $\Sigma_k$ is locally contained in a $C^{1,\log^{\varepsilon}}$ manifold, with an explicit decay $|u-p_{x_0}| = O(r^{2}|\log r|^{-\varepsilon})$.
- **2019.** Figalli–Serra: fine structure. The top stratum $\Sigma_{n-1}$ is locally contained in a **$C^{1,1}$** hypersurface; each $\Sigma_k$ is $C^{1,\alpha}$ outside a set of *anomalous points* of dimension $\le k-1$. In $n=2$ this yields that singular points are locally finite.
- **2020.** Figalli–Ros-Oton–Serra, *Generic regularity of free boundaries for the obstacle problem* (Publ. IHÉS): for the monotone family $u_t$ (obstacle/data shifted by $t$), for a.e. $t$ the singular set satisfies $\dim_{\mathcal H}\Sigma(u_t)\le n-4$, giving generic smoothness of the free boundary in dimensions $n\le 4$. This is the current SOTA on part (1).
- **2024.** Figalli–Ros-Oton–Serra extend the machinery to the **Stefan problem** (J. Amer. Math. Soc.), bounding the space–time singular set and proving generic regularity in low dimensions.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| Regular points, all $n$ | Free boundary real-analytic | Caffarelli 1977; Kinderlehrer–Nirenberg 1977 |
| $\Sigma_k$, all $n$, fixed solution | $\dim_{\mathcal H}\Sigma_k = k$; $C^1$-rectifiable | Caffarelli 1998 |
| $\Sigma_k$, all $n$ | $C^{1,\log^\varepsilon}$ rate | Colombo–Spolaor–Velichkov 2018 |
| $\Sigma_{n-1}$ | Locally in a $C^{1,1}$ manifold | Figalli–Serra 2019 |
| $\Sigma_k$, $k\le n-2$ | $C^{1,\alpha}$ off anomalous set of dim $\le k-1$ | Figalli–Serra 2019 |
| $n=2$, generic data | $\Sigma=\emptyset$ for a.e. $t$ (Schaeffer's conjecture) | Monneau 2003 |
| $n\le 4$, generic data | $\dim_{\mathcal H}\Sigma(u_t)\le n-4$; free boundary generically $C^\infty$ | Figalli–Ros-Oton–Serra 2020 |
| Signorini (thin) obstacle problem | Generic regularity of the free boundary in low dimensions | Fernández-Real–Ros-Oton 2021 |
| Stefan problem | Space–time singular set bounds; generic regularity in $n\le 3$ *(frontier — verify)* | Figalli–Ros-Oton–Serra 2024 |

For fixed (non-generic) solutions the bound $\dim\Sigma_k=k$ is **sharp**: explicit polynomial solutions realise an $(n-1)$-dimensional singular set (Section 10).

## 5. Principal Obstacles

- **No energy gap between strata below the top one.** Weiss's density at singular points varies continuously with the blow-up polynomial $p$ (it equals $\int_{B_1}p$), so there is no discrete spectrum forcing rigidity. Stratification cannot be improved by a compactness/dimension-reduction argument alone, unlike minimal surfaces where Simons' cone and the Federer reduction give a hard codimension.
- **Degenerate decay.** Near a singular point the free boundary is *not* a perturbation of a hyperplane, so the Caffarelli boundary-Harnack / flatness machinery is unavailable. The natural decay $u-p_{x_0}=o(r^2)$ is only logarithmic in general; there is no power gain, which blocks any Schauder-type bootstrap.
- **Anomalous points.** Figalli–Serra's $C^{1,\alpha}$ regularity of $\Sigma_k$ fails exactly where the third-order term in the expansion of $u-p$ degenerates. Whether such points exist is unknown; ruling them out requires unique continuation-type information for a degenerate elliptic operator with non-smooth coefficients.
- **Genericity is a measure-theoretic argument, not a structural one.** The FRS proof shows that, as $t$ increases, the "cleanest" singular strata are hit for at most a measure-zero set of $t$, using a dimension-count of $\Sigma_k$ against the monotone motion of the contact set. The count degrades in high dimension because the strata $\Sigma_k$ with $k$ close to $n-1$ contribute too much measure.
- **No comparison/monotonicity in $n\ge 3$ analogous to Monneau's planar argument**, which exploited the fact that a planar contact set has isolated topological structure.

## 6. The Gap

Proven: for a.e. $t$, $\dim_{\mathcal H}\Sigma(u_t)\le n-4$ in dimensions $n\le 4$, and unconditionally $\dim_{\mathcal H}\Sigma \le n-1$. Conjectured: the same $n-4$ bound in **all** dimensions. The missing step is quantitative control of *how fast* a singular point of stratum $\Sigma_k$ dissolves under the monotone perturbation $t\mapsto u_t$. Current arguments consume roughly one "dimension" per unit of expansion order recovered; getting from the unconditional $n-1$ to $n-4$ in general $n$ needs three extra orders of the expansion $u-p_{x_0}-q_{x_0}-\dots$, uniformly along the stratum. Equivalently: prove a **$C^{1,\alpha}$ (or $C^{1,1}$) regularity theorem for every stratum $\Sigma_k$ with no anomalous exceptional set** — that would feed directly into the FRS measure count and close the gap.

## 7. Current Research (as of June 2026)

- **ETH Zürich / Figalli's group and Barcelona (Ros-Oton, ICREA–UB; Fernández-Real, EPFL)** continue the generic-regularity programme: extending the $n-4$ bound past $n=4$, and transferring it to the thin obstacle (Signorini), parabolic Stefan, and fully nonlinear settings. *(frontier — verify)*
- **Epiperimetric inequalities.** Colombo, Spolaor (UCSD), Velichkov (Pisa) and collaborators develop log-epiperimetric inequalities for other free boundaries (one-phase Bernoulli, thin obstacle, Alt–Caffarelli), aiming at a unified variational proof of stratum regularity.
- **Sharp examples.** Construction of solutions whose singular set is generically of dimension exactly $n-4$ in some high dimension would settle optimality; no such example is known, and it is not excluded that the true generic bound is smaller. *(frontier — verify)*
- **Nonlocal analogues.** Obstacle problems for $(-\Delta)^s$ and for integro-differential operators (Caffarelli–Ros-Oton–Serra) raise the same singular-set questions with an extra parameter $s$; recent work studies whether the singular strata depend on $s$.

## 8. Future Work

- Remove the anomalous set from Figalli–Serra's theorem, or construct an anomalous point — either outcome is decisive.
- Prove a **higher-order expansion** $u(x_0+x)=p_{x_0}(x)+q_{x_0}(x)+o(|x|^{3})$ with $q_{x_0}$ varying Hölder-continuously along $\Sigma_k$; this is the direct route to the general-$n$ generic bound.
- Develop a **Federer-type dimension reduction** adapted to the continuous Weiss density; the obstruction is the lack of a discrete density spectrum.
- Extend generic regularity to non-monotone perturbations (arbitrary smooth families of obstacles), where no comparison principle orders the contact sets.
- Numerical/computer-assisted exploration of high-dimensional singular configurations, to guide the search for sharp examples.

## 9. Key References

- **[Foundational]** L. A. Caffarelli. *The regularity of free boundaries in higher dimensions.* Acta Mathematica 139 (1977), 155–184.
- **[Foundational]** L. A. Caffarelli, N. M. Rivière. *Asymptotic behaviour of free boundaries at their singular points.* Annals of Mathematics 106 (1977), 309–317.
- **[Foundational]** D. G. Schaeffer. *Some examples of singularities in a free boundary.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. (4) 4 (1977), 133–144.
- **[Foundational]** D. Kinderlehrer, L. Nirenberg. *Regularity in free boundary problems.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. (4) 4 (1977), 373–391.
- **[Foundational]** L. A. Caffarelli. *The obstacle problem revisited.* Journal of Fourier Analysis and Applications 4 (1998), 383–402.
- **[Foundational]** G. S. Weiss. *A homogeneity improvement approach to the obstacle problem.* Inventiones Mathematicae 138 (1999), 23–50.
- **[Foundational]** R. Monneau. *On the number of singularities for the obstacle problem in two dimensions.* Journal of Geometric Analysis 13 (2003), 359–389.
- **[SOTA / Recent]** M. Colombo, L. Spolaor, B. Velichkov. *A logarithmic epiperimetric inequality for the obstacle problem.* Geometric and Functional Analysis 28 (2018), 1029–1061.
- **[SOTA / Recent]** A. Figalli, J. Serra. *On the fine structure of the free boundary for the classical obstacle problem.* Inventiones Mathematicae 215 (2019), 311–366.
- **[SOTA / Recent]** A. Figalli, X. Ros-Oton, J. Serra. *Generic regularity of free boundaries for the obstacle problem.* Publications mathématiques de l'IHÉS 132 (2020), 181–292.
- **[SOTA / Recent]** A. Figalli, X. Ros-Oton, J. Serra. *The singular set in the Stefan problem.* Journal of the American Mathematical Society 37 (2024), 305–389.
- **[SOTA / Recent]** X. Fernández-Real, X. Ros-Oton. *Free boundary regularity for almost every solution to the Signorini problem.* Archive for Rational Mechanics and Analysis 240 (2021), 419–466.
- **[Survey]** A. Petrosyan, H. Shahgholian, N. Uraltseva. *Regularity of Free Boundaries in Obstacle-Type Problems.* AMS Graduate Studies in Mathematics 136, 2012.
- **[Survey]** X. Fernández-Real, X. Ros-Oton. *Regularity Theory for Elliptic PDE.* EMS Press, Zurich Lectures in Advanced Mathematics, 2022.
- **[Survey]** A. Figalli. *Regularity of interfaces in phase transitions via obstacle problems.* Proceedings of the ICM 2018, Rio de Janeiro, Vol. I, 225–247.

## 10. Worked Example / Concrete Special Case

**(a) A singular point with a one-dimensional contact set ($n=2$).** Take $p(x)=\tfrac12 x_1^2$. Then $p\ge0$, $\{p=0\}=\{x_1=0\}$ has zero Lebesgue measure, so $\Delta p = 1 = \chi_{\{p>0\}}$ a.e. Thus $p$ is a global solution and $0\in\Sigma_1$: the contact set is a line, of density $0$ in $\mathbb R^2$.

**Weiss density gap.** For any $2$-homogeneous solution $u$, integrating by parts with $\partial_\nu u = 2u$ on $\partial B_1$,
$$\int_{B_1}|\nabla u|^2 = 2\int_{\partial B_1}u^2-\int_{B_1}u \quad\Longrightarrow\quad W(1,u)=\int_{B_1}u .$$
- Singular: $\int_{B_1}\tfrac12 x_1^2\,dx=\tfrac12\int_0^1\!\!\int_0^{2\pi} r^3\cos^2\theta\,d\theta\,dr=\tfrac12\cdot\tfrac14\cdot\pi=\tfrac{\pi}{8}$.
- Regular: $u_0=\tfrac12(x_1)_+^2$ gives exactly half, $\tfrac{\pi}{16}$.

So $W_{\rm sing}=2\,W_{\rm reg}$: the singular density is strictly larger, which is why regular points cannot converge to singular ones. But within the singular class $A\mapsto \int_{B_1}\tfrac12 x^\top Ax$ varies continuously over $\{A\ge0,\ \operatorname{tr}A=1\}$ — this is the missing gap of Section 5.

**(b) Why singularities are non-generic.** Radial solutions in $\mathbb R^2$ with contact set $\overline{B_\rho}$: solve $\Delta u=1$ in $\{r>\rho\}$ with $u=|\nabla u|=0$ on $r=\rho$:
$$u_\rho(r)=\frac{r^2-\rho^2}{4}-\frac{\rho^2}{2}\log\frac{r}{\rho},\qquad r\ge\rho .$$
Check: $u_\rho'(r)=\frac r2-\frac{\rho^2}{2r}$, so $u_\rho'(\rho)=0$ and $u_\rho''+\frac1r u_\rho' = \frac12+\frac{\rho^2}{2r^2}+\frac12-\frac{\rho^2}{2r^2}=1$. For every $\rho>0$ the free boundary $\{r=\rho\}$ is a smooth circle, entirely regular. As $\rho\downarrow 0$, $u_\rho\to \tfrac{r^2}{4}=\tfrac14(x_1^2+x_2^2)$, a singular solution with $\Sigma_0=\{0\}$ (blow-up $p$ with $A=\tfrac12 I$, $\ker A = \{0\}$).

The singular configuration occurs at the single parameter value $\rho=0$: perturbing the data (raising the boundary value by $t$ shrinks or grows $\rho$ monotonically) destroys it for a.e. $t$. This is exactly the mechanism that Figalli–Ros-Oton–Serra make quantitative in dimensions $n\le 4$, and which is not yet controlled for $n\ge5$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*