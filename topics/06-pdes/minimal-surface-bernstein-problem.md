---
id: 06-pdes/minimal-surface-bernstein-problem
title: "Minimal Surface Bernstein Problem"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Minimal Surface Bernstein Problem

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/minimal-surface-bernstein-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $u : \mathbb{R}^n \to \mathbb{R}$ be a smooth entire solution of the **minimal surface equation**

$$\operatorname{div}\!\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right) = 0 \qquad \text{on all of } \mathbb{R}^n .$$

**Bernstein problem.** Must $u$ be an affine function, $u(x) = a\cdot x + b$?

The classical question is fully resolved: **yes for $n \le 7$** (Bernstein, Fleming, De Giorgi, Almgren, Simons), **no for $n \ge 8$** (Bombieri–De Giorgi–Giusti). The problem remains *live* in its modern reformulation, the **stable Bernstein problem**:

> Is every complete, two-sided, immersed, **stable** minimal hypersurface $M^n \subset \mathbb{R}^{n+1}$ a hyperplane?

Every entire minimal graph is stable and area-minimizing, so this strictly generalizes the graph case. It is true for $n \le 5$ (2024) and false for $n \ge 8$; $n = 6, 7$ are open. A resolution requires either a proof for $n\in\{6,7\}$ or a complete stable non-planar example in $\mathbb{R}^7$ or $\mathbb{R}^8$.

## 2. Mathematical Foundations

**Graph formulation.** The graph $\Gamma_u = \{(x,u(x))\}\subset\mathbb{R}^{n+1}$ is a critical point of the area functional $\mathcal{A}(u)=\int \sqrt{1+|\nabla u|^2}\,dx$. The Euler–Lagrange equation, in nondivergence form, is

$$\sum_{i,j=1}^n \left(\delta_{ij} - \frac{u_i u_j}{1+|\nabla u|^2}\right) u_{ij} = 0 ,$$

a quasilinear uniformly elliptic equation whose ellipticity ratio degenerates like $(1+|\nabla u|^2)^{-1}$ as $|\nabla u|\to\infty$.

**Sets of finite perimeter.** For $E\subset\mathbb{R}^{n+1}$ measurable, $P(E;\Omega)=\sup\{\int_E \operatorname{div}X : X\in C_c^1(\Omega;\mathbb{R}^{n+1}), |X|\le 1\}$. $E$ is **area-minimizing** if $P(E;\Omega)\le P(F;\Omega)$ for all $F$ with $E\triangle F \Subset \Omega$. The subgraph of an entire solution is area-minimizing in $\mathbb{R}^{n+1}$ (Miranda).

**Blow-down.** If $E$ is minimizing, the rescalings $E_r = r^{-1}E$ subconverge in $L^1_{loc}$ to a **minimizing cone** $C$. Bernstein for $\mathbb{R}^n$ follows if every minimizing cone in $\mathbb{R}^n$ is a hyperplane (Fleming's reduction, plus De Giorgi's dimension-lowering: a minimizing cone in $\mathbb{R}^{n+1}$ that is a cylinder over a cone in $\mathbb{R}^n$ reduces the dimension by one).

**Stability.** For a two-sided minimal hypersurface $M^n$ with unit normal $\nu$, second variation of area under $\varphi\nu$, $\varphi \in C_c^\infty(M)$:

$$Q(\varphi,\varphi) = \int_M \left(|\nabla_M \varphi|^2 - |A|^2\varphi^2\right)d\mu \ge 0 ,$$

where $|A|^2$ is the squared norm of the second fundamental form. **Simons' inequality** on a minimal hypersurface:

$$\Delta_M |A|^2 \ge -2|A|^4 + 2\left(1+\tfrac{2}{n}\right)\big|\nabla |A|\big|^2 .$$

**Cone stability criterion.** For the cone $C$ over a closed minimal $\Sigma^{n-1}\subset S^n$, $C\setminus\{0\}$ is stable iff

$$\lambda_1\!\left(-\Delta_\Sigma - |A_\Sigma|^2\right) \ \ge\ -\frac{(n-2)^2}{4}.$$

**Simons cone.** $\mathcal{C}_{k} = \{x\in\mathbb{R}^{2k+2} : x_1^2+\cdots+x_{k+1}^2 = x_{k+2}^2+\cdots+x_{2k+2}^2\}$, the cone over the Clifford minimal hypersurface $S^k(1/\sqrt2)\times S^k(1/\sqrt2)\subset S^{2k+1}$.

## 3. History & State of the Art (SOTA)

- **1915–17** — Sergei Bernstein proves the $n=2$ case (entire minimal graphs over $\mathbb{R}^2$ are planes), via a geometric theorem on elliptic PDE.
- **1961** — Moser: Bernstein holds in every dimension **under the extra hypothesis $|\nabla u| \le C$**, by Harnack inequality applied to the derivatives.
- **1962** — Fleming reproves $n=2$ by geometric measure theory and reduces the general problem to nonexistence of singular minimizing cones.
- **1965** — De Giorgi's dimension-reduction gives $n=3$.
- **1966** — Almgren: $n=4$.
- **1968** — Simons: no stable minimal cones with isolated singularity in $\mathbb{R}^n$ for $n \le 7$, hence Bernstein for $n\le 7$; Simons also identifies $\mathcal{C}_3\subset\mathbb{R}^8$ as stable and conjectures it minimizes.
- **1969** — Bombieri, De Giorgi, Giusti prove $\mathcal{C}_3$ is area-minimizing and construct a **nonlinear entire solution on $\mathbb{R}^8$**, settling the classical problem.
- **1977** — Lawson–Osserman: in codimension $\ge 2$ the analogue fails badly; the Hopf map gives a Lipschitz, non-affine entire minimal graph $\mathbb{R}^4\to\mathbb{R}^3$.
- **1979–80** — do Carmo–Peng, Fischer-Colbrie–Schoen, Pogorelov: **stable** Bernstein for $n=2$.
- **2021–24** — Chodosh–Li ($n=3$), Chodosh–Li–Minter–Stryker ($n=4$), Mazet ($n=5$): stable Bernstein in $\mathbb{R}^4,\mathbb{R}^5,\mathbb{R}^6$.

## 4. Partial Results / Verified Cases

| Statement | Range | Author(s) |
|---|---|---|
| Entire minimal graphs are affine | $n \le 7$ | Bernstein; De Giorgi; Almgren; Simons (1968) |
| Counterexample (nonlinear entire graph) | $n = 8$, and $n\ge 8$ by cylinders | Bombieri–De Giorgi–Giusti (1969) |
| Bernstein with $|\nabla u|$ bounded | all $n$ | Moser (1961) |
| Bernstein under growth $u(x) = o(|x|)$ or one-sided bounds on $n-2$ derivatives | all $n$ | Ecker–Huisken (1990); Bombieri–Giusti (1972) |
| Stable minimal hypersurfaces in $\mathbb{R}^{n+1}$ are hyperplanes | $n=2$ | do Carmo–Peng; Fischer-Colbrie–Schoen; Pogorelov (1979–80) |
| Same, $n=3$ | $\mathbb{R}^4$ | Chodosh–Li, *Acta Math.* (2024) |
| Same, $n=4$ | $\mathbb{R}^5$ | Chodosh–Li–Minter–Stryker (2024) |
| Same, $n=5$ | $\mathbb{R}^6$ | Mazet (2024) |
| Curvature estimates $\Rightarrow$ Bernstein for stable hypersurfaces with Euclidean volume growth | $n\le 5$ | Schoen–Simon–Yau (1975) |
| Codimension $\ge 2$, $n=2$ | all codim | Osserman (1961) |
| Codimension $\ge 2$, $n=4$: **false** | Lipschitz cone solution | Lawson–Osserman (1977) |

Higher-codimension Bernstein statements survive only under strong extra hypotheses (e.g. Hildebrandt–Jost–Widman: bounded slope / image in a geodesic ball).

## 5. Principal Obstacles

- **Degenerate ellipticity.** The linearized operator has ellipticity ratio $(1+|\nabla u|^2)^{-1}$. Without a gradient bound, De Giorgi–Nash–Moser theory does not apply directly, which is exactly why Moser's proof needs $|\nabla u|\le C$ and why the general case must be routed through geometric measure theory.
- **The dimension barrier is real, not technical.** For $n\ge 8$ the answer is *no*: any method that "should work in all dimensions" is wrong. The truth hinges on the arithmetic inequality $n-1 \le (n-2)^2/4$, which first holds at $n=7$.
- **Stable, non-minimizing behavior.** In the stable Bernstein problem one loses the minimizing property, hence loses compactness of blow-downs, monotonicity-based cone reduction, and Federer dimension reduction. The Schoen–Simon–Yau curvature estimate stops at $n\le 5$ because its Simons-inequality bootstrap requires $\int |A|^{2+q}$ with $q < \sqrt{2/n}$.
- **No volume control.** Chodosh–Li's $n=3$ proof works because a stable minimal $M^3$ carries a positive-scalar-curvature-type conformal structure (via the $\mu$-bubble / Schoen–Yau slicing), forcing quadratic area growth. In $n=6,7$ there is no known substitute: a stable hypersurface may a priori have wildly growing area, and the Gauss–Bonnet/warped-$\mu$-bubble machinery has no analogue above dimension 5.
- **Singularity structure.** Even for minimizers, the singular set can be $(n-7)$-dimensional (Federer), and Simon's work gives rectifiability but not enough structure to run induction past dimension 5 in the stable setting.

## 6. The Gap

The classical graph problem has **no gap**: it is closed in every dimension. The remaining gap is precisely:

- **Stable Bernstein for $n=6$ and $n=7$** (hypersurfaces in $\mathbb{R}^7$, $\mathbb{R}^8$). The expected answer is yes, since the first stable non-planar cone $\mathcal{C}_3$ lives in $\mathbb{R}^8$ as a *hypersurface of dimension 7*, and it is not complete-and-smooth. One must rule out complete smooth stable hypersurfaces of dimension 6 and 7 with non-Euclidean volume growth.
- The concrete missing step: an *a priori* area-growth bound $\mathrm{Area}(M\cap B_R)\le C R^n$ for complete stable $M^n\subset\mathbb{R}^{n+1}$, $n=6,7$. Given such a bound, Schoen–Simon regularity plus Simons' cone classification closes the case immediately. Every proof to date ($n\le 5$) obtains that bound by a dimension-specific mechanism (Gauss–Bonnet for $n=2$; $\mu$-bubbles and Sobolev/isoperimetric inequalities on slices for $n=3,4,5$) that has no known extension.

## 7. Current Research (as of June 2026)

- **Stanford / MIT / Cambridge school** (Chodosh, Li, Minter, Stryker) continues to push the $\mu$-bubble + intrinsic-slicing method; the $n=5$ argument of Mazet (Université Gustave Eiffel) reorganizes it via a Bishop–Gromov-type comparison. Extension to $n=6$ is the stated target. *(frontier — verify)*
- **Anisotropic and free-boundary analogues.** Chodosh–Li's "Stable anisotropic minimal hypersurfaces in $\mathbb{R}^4$" transports the method to elliptic integrands, where no Simons inequality is available; the anisotropic Bernstein problem is open for $n\ge 4$ *(frontier — verify)*.
- **Finite Morse index.** Classifying complete minimal hypersurfaces in $\mathbb{R}^{n+1}$ of finite index (rather than index 0) for $3\le n \le 5$ is active; index bounds should force stability outside a compact set.
- **Bernstein-type theorems in Riemannian ambients**, notably in manifolds of nonnegative Ricci curvature, and their use in scalar-curvature rigidity (Schoen–Yau positive mass, Gromov's conjectures).
- **Explicit BDGG-type solutions.** Numerical and asymptotic work refining the expansion of the BDGG graph near the Simons cone (Davila–del Pino–Wei-style gluing) informs conjectural constructions in $\mathbb{R}^7$–$\mathbb{R}^8$ *(frontier — verify)*.

## 8. Future Work

1. Prove Euclidean volume growth for complete stable $M^6, M^7\subset\mathbb{R}^{7},\mathbb{R}^{8}$ — the single decisive step.
2. Develop a dimension-independent replacement for $\mu$-bubbles: a stable-hypersurface Sobolev inequality with constants uniform in $n$.
3. Settle the **anisotropic Bernstein problem** for general elliptic integrands where $|A|^2$-based Simons identities fail.
4. Understand which minimal cones over homogeneous $\Sigma\subset S^n$ are stable but non-minimizing; a stable non-minimizing cone would be a new phenomenon.
5. Quantify the failure: classify all entire minimal graphs on $\mathbb{R}^8$ (currently a large family constructed by symmetry, none classified).

## 9. Key References

- **[Foundational]** S. Bernstein. *Sur un théorème de géométrie et ses applications aux équations aux dérivées partielles du type elliptique.* Comm. Soc. Math. Kharkov, 1915–17.
- **[Foundational]** W. H. Fleming. *On the oriented Plateau problem.* Rend. Circ. Mat. Palermo 11 (1962), 69–90.
- **[Foundational]** E. De Giorgi. *Una estensione del teorema di Bernstein.* Ann. Scuola Norm. Sup. Pisa 19 (1965), 79–85.
- **[Foundational]** F. J. Almgren, Jr. *Some interior regularity theorems for minimal surfaces and an extension of Bernstein's theorem.* Ann. of Math. 84 (1966), 277–292.
- **[Foundational]** J. Simons. *Minimal varieties in Riemannian manifolds.* Ann. of Math. 88 (1968), 62–105.
- **[Foundational]** E. Bombieri, E. De Giorgi, E. Giusti. *Minimal cones and the Bernstein problem.* Invent. Math. 7 (1969), 243–268.
- **[Foundational]** J. Moser. *On Harnack's theorem for elliptic differential equations.* Comm. Pure Appl. Math. 14 (1961), 577–591.
- **[Foundational]** R. Schoen, L. Simon, S.-T. Yau. *Curvature estimates for minimal hypersurfaces.* Acta Math. 134 (1975), 275–288.
- **[Foundational]** D. Fischer-Colbrie, R. Schoen. *The structure of complete stable minimal surfaces in 3-manifolds of non-negative scalar curvature.* Comm. Pure Appl. Math. 33 (1980), 199–211.
- **[Foundational]** M. do Carmo, C. K. Peng. *Stable complete minimal surfaces in $\mathbb{R}^3$ are planes.* Bull. Amer. Math. Soc. 1 (1979), 903–906.
- **[Foundational]** H. B. Lawson, R. Osserman. *Non-existence, non-uniqueness and irregularity of solutions to the minimal surface system.* Acta Math. 139 (1977), 1–17.
- **[SOTA / Recent]** O. Chodosh, C. Li. *Stable minimal hypersurfaces in $\mathbb{R}^4$.* Acta Mathematica 233 (2024), 1–31.
- **[SOTA / Recent]** O. Chodosh, C. Li, P. Minter, D. Stryker. *Stable minimal hypersurfaces in $\mathbb{R}^5$.* arXiv:2401.01492, 2024.
- **[SOTA / Recent]** L. Mazet. *Stable minimal hypersurfaces in $\mathbb{R}^6$.* arXiv:2405.14676, 2024.
- **[SOTA / Recent]** K. Ecker, G. Huisken. *A Bernstein result for minimal graphs of controlled growth.* J. Differential Geom. 31 (1990), 397–400.
- **[Survey]** E. Giusti. *Minimal Surfaces and Functions of Bounded Variation.* Birkhäuser, 1984.
- **[Survey]** R. Osserman. *A Survey of Minimal Surfaces.* Dover, 1986 (orig. Van Nostrand, 1969).
- **[Survey]** T. H. Colding, W. P. Minicozzi II. *A Course in Minimal Surfaces.* AMS Graduate Studies in Mathematics 121, 2011.
- **[Survey]** L. Simon. *Lectures on Geometric Measure Theory.* Proc. Centre Math. Analysis, ANU, 1983.

## 10. Worked Example / Concrete Special Case

**Why dimension 8 and not 6: the stability of the Simons cones.**

Take $\Sigma_k = S^k(1/\sqrt2)\times S^k(1/\sqrt2) \subset S^{2k+1}$, a minimal hypersurface of $S^{2k+1}$ (the Clifford-type example), and let $\mathcal{C}_k \subset \mathbb{R}^{2k+2}$ be the cone over it — a minimal hypersurface of dimension $n = 2k+1$, smooth away from the origin.

*Step 1 — second fundamental form.* $\Sigma_k$ has principal curvatures $\pm 1$, each with multiplicity $k$ (the two factors curve oppositely inside $S^{2k+1}$), so

$$|A_{\Sigma_k}|^2 = 2k = n-1 \quad (\text{constant}).$$

*Step 2 — spectrum.* Since $|A_{\Sigma}|^2$ is constant and $\Sigma$ is closed, the bottom eigenvalue of $-\Delta_\Sigma - |A_\Sigma|^2$ is attained by constants:

$$\lambda_1 = 0 - (n-1) = -(n-1).$$

*Step 3 — apply the cone criterion.* $\mathcal{C}_k$ is stable iff $-(n-1) \ge -\frac{(n-2)^2}{4}$, i.e.

$$n - 1 \le \frac{(n-2)^2}{4}, \qquad n = 2k+1 \ \Longleftrightarrow\ 2k \le \frac{(2k-1)^2}{4} \ \Longleftrightarrow\ 4k^2 - 12k + 1 \ge 0 .$$

The roots are $k = \frac{3}{2} \pm \frac{\sqrt{8}}{2}\approx 0.086,\ 2.914$. Hence:

| $k$ | ambient | cone dim $n$ | $4k^2-12k+1$ | stable? |
|---|---|---|---|---|
| 1 | $\mathbb{R}^4$ | 3 | $-7$ | no |
| 2 | $\mathbb{R}^6$ | 5 | $-7$ | no |
| **3** | $\mathbb{R}^8$ | **7** | $+1$ | **yes** |
| 4 | $\mathbb{R}^{10}$ | 9 | $+17$ | yes |

*Step 4 — consequence.* For $n\le 7$ no singular stable cone exists (Simons' full theorem extends this computation to all minimal $\Sigma$), so the blow-down of an entire minimal graph over $\mathbb{R}^{n}$, $n\le 7$, is a hyperplane, forcing $u$ affine. At $k=3$ the inequality first turns positive by the margin $4\cdot 9-36+1 = 1$. Bombieri–De Giorgi–Giusti then show $\mathcal{C}_3$ is not merely stable but area-minimizing, and build barriers $w^{\pm}$ trapping a solution $u$ on $\mathbb{R}^8$ asymptotic to $\mathcal{C}_3$ — e.g. the rotationally symmetric family $u(x) = f(r,s)$ with $r=|(x_1,\dots,x_4)|$, $s=|(x_5,\dots,x_8)|$, odd under $r\leftrightarrow s$ and vanishing exactly on $\{r=s\}$. That $u$ is a non-affine entire solution: the Bernstein theorem fails at $n=8$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*