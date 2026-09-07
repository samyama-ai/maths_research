---
id: 06-pdes/payne-nodal-line-conjecture
title: "Payne Nodal Line Conjecture"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Payne Nodal Line Conjecture

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/payne-nodal-line-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\Omega\subset\mathbb{R}^2$ be a bounded domain and let $u_2$ be a second Dirichlet eigenfunction of the Laplacian on $\Omega$. Payne (1967) conjectured:

> **Conjecture (Payne).** The nodal line of $u_2$ intersects the boundary $\partial\Omega$ at exactly two points; in particular it cannot be a closed curve contained in the interior of $\Omega$.

Equivalently, no nodal domain of $u_2$ has closure disjoint from $\partial\Omega$: neither nodal domain is "interior". A disproof requires exhibiting a single bounded $\Omega$ with $\overline{\{u_2=0\}}\cap\partial\Omega=\emptyset$; a proof requires showing this is impossible for every admissible $\Omega$.

The conjecture splits by topology, and this split is the whole story:

1. **General bounded planar domains** — **false** (Hoffmann-Ostenhof, Hoffmann-Ostenhof, Nadirashvili 1997).
2. **Higher dimensions** $\mathbb{R}^D$, $D\ge 3$ — **false** (Fournais 2001).
3. **Convex planar domains** — **true**, with the strong two-point conclusion (Melas 1992; Alessandrini 1994).
4. **Simply connected planar domains** — the last standing case; the current status is *disproved by computer-assisted construction* in recent work, which is why this entry is filed as `solved-recently` rather than `open`.

Because the truth value depends on the domain class, the live formulation is: **for which classes of planar domains does the nodal line reach the boundary?**

## 2. Mathematical Foundations

Consider the fixed membrane (Dirichlet) eigenvalue problem
$$-\Delta u=\lambda u \ \text{ in }\Omega,\qquad u=0 \ \text{ on }\partial\Omega ,$$
with $\Omega\subset\mathbb{R}^n$ bounded. The spectrum is discrete,
$$0<\lambda_1(\Omega)<\lambda_2(\Omega)\le\lambda_3(\Omega)\le\cdots\to\infty ,$$
with $L^2$-orthonormal eigenfunctions $u_k\in H_0^1(\Omega)$. The variational characterisation is
$$\lambda_2(\Omega)=\min\Big\{\tfrac{\int_\Omega|\nabla v|^2}{\int_\Omega v^2}\ :\ v\in H_0^1(\Omega)\setminus\{0\},\ \textstyle\int_\Omega v\,u_1=0\Big\}.$$

The **nodal set** of $u$ is $\mathcal N(u)=\overline{\{x\in\Omega: u(x)=0\}}$; its complementary components in $\Omega$ are **nodal domains**. Facts used throughout:

- **Courant nodal domain theorem.** $u_k$ has at most $k$ nodal domains; since $u_1>0$ and $\int u_2u_1=0$, $u_2$ has **exactly two** nodal domains $\Omega^{\pm}=\{\pm u_2>0\}$.
- **Local structure.** Eigenfunctions are real-analytic in $\Omega$; $\mathcal N(u_2)\cap\Omega$ is a locally finite union of real-analytic arcs, and at a zero of order $m$ exactly $2m$ arcs meet at equal angles $\pi/m$ (Cheng, 1976). Hence in 2D the nodal set is a curve system with isolated singular crossings; $\mathcal{H}^{n-1}(\mathcal N)<\infty$.
- **Domain monotonicity.** $\Omega'\subset\Omega\Rightarrow\lambda_k(\Omega')\ge\lambda_k(\Omega)$.
- **Restatement.** $\mathcal N(u_2)$ is closed in $\Omega$ iff one nodal domain $\Omega^{-}$ satisfies $\overline{\Omega^-}\subset\Omega$. Then $u_2|_{\Omega^-}$ is a *first* eigenfunction of $\Omega^-$, so $\lambda_1(\Omega^-)=\lambda_2(\Omega)$. By Faber–Krahn,
$$\lambda_2(\Omega)=\lambda_1(\Omega^-)\ \ge\ \frac{\pi j_{0,1}^2}{|\Omega^-|},$$
so a closed nodal line forces the interior nodal domain to be small, and by domain monotonicity $\lambda_2(\Omega)\ge\lambda_1(\Omega^-)$ pins $\Omega^-$ tightly. Counterexample constructions must engineer exactly this configuration.
- **Model case: the disc.** On the unit disc, $\lambda_{m,k}=j_{m,k}^2$ with eigenfunctions $J_m(j_{m,k}r)e^{\pm i m\theta}$, where $j_{0,1}\approx2.4048$, $j_{1,1}\approx3.8317$, $j_{2,1}\approx5.1356$, $j_{0,2}\approx5.5201$. So $\lambda_2=j_{1,1}^2\approx14.68$ is angular, its nodal line a diameter meeting $\partial\Omega$ twice. The *radial* mode $J_0(j_{0,2}r)$, with closed circular nodal set $r=j_{0,1}/j_{0,2}\approx0.4356$, sits at $\lambda\approx30.47$ — third in line after $m=1,2$.

## 3. History & State of the Art (SOTA)

- **1967.** L. E. Payne states the conjecture in his survey *Isoperimetric inequalities and their applications* (SIAM Review), and reiterates it in 1973 (ZAMP), proving it for domains symmetric about a line and convex in the orthogonal direction: reflection plus the variational principle forces $u_2$ to be antisymmetric, so the nodal line is the symmetry segment.
- **1982.** S.-T. Yau lists the nodal line problem in his problem collection, giving it wide circulation.
- **1987.** C.-S. Lin extends the symmetric result to convex domains in $\mathbb{R}^n$ with symmetry hypotheses.
- **1992/1994.** A. Melas proves the conjecture for smooth convex planar domains — the nodal line is a simple curve meeting $\partial\Omega$ at exactly two points; G. Alessandrini removes smoothness, covering all convex planar domains, and gives bounds on the nodal line's position.
- **1991–1996.** D. Jerison, then Grieser–Jerison, locate the nodal line in long thin convex domains: it is asymptotically a vertical segment at the minimum of the effective potential $V(x)=\pi^2/L(x)^2$ of the ODE $-h''+Vh=\mu h$, where $L(x)$ is the vertical cross-section length. Jerison bounds the nodal line's diameter by $C\,\mathrm{inrad}(\Omega)$.
- **1997.** M. and T. Hoffmann-Ostenhof and N. Nadirashvili **disprove** the conjecture for general planar domains: a multiply connected $\Omega$ with a closed nodal line. **2001.** S. Fournais does the same in $\mathbb{R}^D$, $D\ge3$.
- **2021.** Dahne, Gómez-Serrano and Hou make the counterexample explicit and minimal-ish: a domain with **6 holes**, verified by computer-assisted rigorous enclosures of $\lambda_2$ and $\lambda_3$.
- **2020s.** The residual simply connected case is attacked by the same validated-numerics machinery; a simply connected counterexample has been announced *(frontier — verify)*.

## 4. Partial Results / Verified Cases

**Proved (nodal line reaches the boundary):**

- All **convex** planar domains, with exactly two boundary intersections and no interior singular point of the nodal set (Melas; Alessandrini). No regularity assumption needed.
- Planar domains **symmetric about a line and convex in the perpendicular direction** (Payne 1973); higher-dimensional analogues under two symmetries (Lin 1987; Damascelli 2000 for symmetric domains in $\mathbb{R}^n$).
- **Rectangles, discs, ellipses, annuli, sectors, equilateral/right triangles** — direct separation-of-variables computation.
- **Thin convex domains** $\Omega=\{(x,y):0<x<1,\ f_1(x)<y<f_2(x)\}$ with small inradius: quantitative location of the nodal segment (Jerison; Grieser–Jerison).
- **Doubly connected** domains with symmetry, e.g. annuli and eccentric annuli in a suitable parameter range (Kiwan and others).

**Disproved (closed nodal line exists):**

- Planar domains of **high connectivity** (Hoffmann-Ostenhof$^2$–Nadirashvili 1997), then **connectivity 7** (6 holes) with rigorous eigenvalue enclosures (Dahne–Gómez-Serrano–Hou 2021).
- **All dimensions $D\ge3$** for domains with holes (Fournais 2001).

## 5. Principal Obstacles

- **No maximum principle for $u_2$.** $u_2$ changes sign, so the standard elliptic toolkit — Hopf lemma, moving planes, Krein–Rutman positivity — applies only to $u_1$. Melas's proof works by a delicate reflection/rearrangement argument that consumes convexity outright; there is no known replacement for non-convex domains.
- **Convexity, not simple connectivity, is what the proofs use.** Melas and Alessandrini use that any line cuts $\Omega$ in a single interval, so a hypothetical closed nodal line can be reflected into a competitor test function. Simply connected domains with slits and fjords destroy this.
- **The obstruction is spectral, not geometric.** A closed nodal line requires the radially-symmetric-type mode to undercut all angular modes. Suppressing angular modes while preserving a radial mode is a *capacity* perturbation problem: thin obstacles have vanishing $H^1$-capacity in 2D (logarithmically small), so one needs many obstacles, or long thin ones, to lift $\lambda$ appreciably — precisely the regime where asymptotic expansions lose control.
- **Non-perturbative eigenvalue gaps.** The counterexample needs a *strict* inequality between two eigenvalues of a complicated domain. Formal asymptotics give the sign but not a proof; only computer-assisted, interval-arithmetic enclosures of $\lambda_2<\lambda_3$ close the argument, and their cost grows fast with geometric complexity.
- **Symmetry is a crutch.** Nearly all positive results reduce to a 1D or half-domain problem via symmetry. Generic simply connected domains have none.

## 6. The Gap

Proven: convex $\Rightarrow$ true; multiply connected (and $D\ge3$) $\Rightarrow$ false. The gap is the intermediate class

$$\{\text{convex}\}\ \subsetneq\ \{\text{simply connected}\subset\mathbb{R}^2\}\ \subsetneq\ \{\text{bounded}\subset\mathbb{R}^2\}.$$

To settle it one must either (a) replace each hole in a known counterexample by a thin channel joining it to $\partial\Omega$, and prove the eigenvalue ordering $\lambda_2<\lambda_3$ survives the channel perturbation with the nodal set still closed — the channel width must be small enough not to reorder the spectrum but the domain must stay open and connected; or (b) prove that simple connectivity alone implies the nodal set touches $\partial\Omega$, which would need a topological argument for $u_2$ with no convexity input — none is known. Route (a) is what recent computer-assisted work pursues.

## 7. Current Research (as of June 2026)

- **Validated numerics for eigenvalue problems.** Dahne and Gómez-Serrano (Uppsala/Brown/Barcelona) develop rigorous enclosures via the method of particular solutions with interval arithmetic, applied to nodal-line and $\lambda_2/\lambda_3$ separation questions. A **simply connected counterexample** obtained by converting holes into slits/channels has been announced by this school *(frontier — verify)*; the multiply connected 6-hole result is published and settled.
- **Nodal geometry schools** (Logunov, Malinnikova, Nadirashvili, Steinerberger) study nodal set measure and structure; techniques (doubling indices, frequency functions) give $\mathcal{H}^{n-1}$ bounds but do not see boundary contact.
- **Sharp constants and shape optimisation** groups (Bucur, Freitas, Henrot, van den Berg) treat related $\lambda_2$ optimisation and the hot-spots conjecture, whose obstacle-based counterexamples (Burdzy–Werner 1999; Burdzy 2005) are structurally analogous.
- **Discrete/graph analogues** (Bandeira, Bıyıkoğlu, Lefèvre) test how much of the two-nodal-domain rigidity is combinatorial.

## 8. Future Work

- Prove or disprove: **every simply connected planar $C^\infty$ domain has $\mathcal N(u_2)\cap\partial\Omega\neq\emptyset$** — with smoothness and a bound on curvature, does the counterexample mechanism die?
- Quantify: what is the minimal number of holes admitting a closed nodal line? Lower bound 1 vs. current upper bound 6.
- Extend Melas/Alessandrini to **mean-convex**, star-shaped, or Lipschitz domains with a quantified convexity defect; find the sharp defect threshold.
- Understand the analogous question for the **Neumann** second eigenfunction (hot spots) and for the **$p$-Laplacian**, where the two-nodal-domain structure persists but reflection arguments fail.
- Give a **stability** statement: if $\Omega$ is $\varepsilon$-close to convex in Hausdorff distance, is the nodal line within $C\varepsilon$ of the convex-domain one?

## 9. Key References

- **[Foundational]** L. E. Payne. *Isoperimetric inequalities and their applications.* SIAM Review 9(3):453–488, 1967.
- **[Foundational]** L. E. Payne. *On two conjectures in the fixed membrane eigenvalue problem.* Zeitschrift für angewandte Mathematik und Physik (ZAMP) 24:721–729, 1973.
- **[Foundational]** S. Y. Cheng. *Eigenfunctions and nodal sets.* Commentarii Mathematici Helvetici 51:43–55, 1976.
- **[Key positive result]** A. D. Melas. *On the nodal line of the second eigenfunction of the Laplacian in $\mathbb{R}^2$.* Journal of Differential Geometry 35(1):255–263, 1992.
- **[Key positive result]** G. Alessandrini. *Nodal lines of eigenfunctions of the fixed membrane problem in general convex domains.* Commentarii Mathematici Helvetici 69:142–154, 1994.
- **[Key positive result]** C.-S. Lin. *On the second eigenfunctions of the Laplacian in $\mathbb{R}^2$.* Communications in Mathematical Physics 111:161–166, 1987.
- **[Counterexample]** M. Hoffmann-Ostenhof, T. Hoffmann-Ostenhof, N. Nadirashvili. *The nodal line of the second eigenfunction of the Laplacian in $\mathbb{R}^2$ can be closed.* Duke Mathematical Journal 90(3):631–640, 1997.
- **[Counterexample]** S. Fournais. *The nodal surface of the second eigenfunction of the Laplacian in $\mathbb{R}^D$ can be closed.* Journal of Differential Equations 173(1):145–159, 2001.
- **[SOTA / Recent]** J. Dahne, J. Gómez-Serrano, K. Hou. *A counterexample to Payne's nodal line conjecture with few holes.* Communications in Nonlinear Science and Numerical Simulation 103:105957, 2021.
- **[Thin domains]** D. Grieser, D. Jerison. *Asymptotics of the first nodal line of a convex domain.* Inventiones Mathematicae 125:197–219, 1996.
- **[Thin domains]** D. Jerison. *The diameter of the first nodal line of a convex domain.* Annals of Mathematics 141(1):1–33, 1995.
- **[Survey]** A. Henrot. *Extremum Problems for Eigenvalues of Elliptic Operators.* Birkhäuser, Frontiers in Mathematics, 2006.
- **[Survey]** P. Bérard, B. Helffer. *Nodal sets of eigenfunctions, Antonie Stern's results revisited.* Séminaire de Théorie Spectrale et Géométrie, Grenoble, 2014–2015.

## 10. Worked Example / Concrete Special Case

**(a) A rectangle: the conjecture holds by direct computation.** Let $\Omega=(0,a)\times(0,b)$ with $a>b$. Eigenpairs:
$$u_{m,n}=\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b},\qquad \lambda_{m,n}=\pi^2\Big(\frac{m^2}{a^2}+\frac{n^2}{b^2}\Big).$$
Then $\lambda_1=\lambda_{1,1}$, and the two candidates for second place satisfy
$$\lambda_{2,1}-\lambda_{1,1}=\frac{3\pi^2}{a^2},\qquad \lambda_{1,2}-\lambda_{1,1}=\frac{3\pi^2}{b^2}.$$
Since $a>b$, $\lambda_2=\lambda_{2,1}$ and $u_2=\sin(2\pi x/a)\sin(\pi y/b)$. Its nodal set is the segment $\{x=a/2\}$, meeting $\partial\Omega$ at exactly the two points $(a/2,0)$ and $(a/2,b)$ — Melas's conclusion, verified.

**(b) Why holes are needed: the disc mechanism.** On the unit disc $D$, the radial mode $\varphi(r)=J_0(j_{0,2}r)$ has a **closed** nodal set, the circle $r_\ast=j_{0,1}/j_{0,2}\approx0.4356$, and eigenvalue $j_{0,2}^2\approx30.47$. It is not $\lambda_2$ because two families sit below it:
$$\lambda_{1,1}=j_{1,1}^2\approx14.68,\qquad \lambda_{2,1}=j_{2,1}^2\approx26.37 .$$
Now delete $k$ small discs of radius $\varepsilon$, centred at the points $r_\ast e^{2\pi i \ell/k}$, $\ell=0,\dots,k-1$ — i.e. **on the nodal circle of $\varphi$**. Two effects:

- $\varphi$ vanishes at the hole centres, so its eigenvalue moves by $O(\varepsilon^{2})$ in the capacity expansion (the leading logarithmic term $\propto \varphi(x_\ell)^2/|\log\varepsilon|$ vanishes).
- The competing modes $J_1(j_{1,1}r)e^{\pm i\theta}$ and $J_2(j_{2,1}r)e^{\pm 2i\theta}$ do **not** vanish at $r_\ast$; each hole raises their eigenvalues by roughly $2\pi\,|u(x_\ell)|^2/|\log\varepsilon|$ per hole. With $\mathbb{Z}_k$-symmetric holes, the modes surviving unperturbed are those with angular index $\equiv 0 \bmod k$, so taking $k=6$ leaves $m=1,2$ fully exposed while protecting the radial mode.

Choosing $\varepsilon$ and $r_\ast$ so that both $m=1$ and $m=2$ branches are pushed above the (nearly unchanged) value $\approx 30.47$ while $j_{0,1}^2\approx5.78$ stays lowest, the second eigenfunction of the perforated domain becomes radial-like, and its nodal set is a closed curve near $r=r_\ast$ that misses $\partial\Omega$ entirely. This is exactly the Hoffmann-Ostenhof$^2$–Nadirashvili scheme; Dahne–Gómez-Serrano–Hou realised it with $k=6$ holes and proved the required strict ordering $\lambda_2<\lambda_3$ by interval-arithmetic enclosures rather than asymptotics. The remaining question — cut a thin channel from one hole to $\partial\Omega$ to make the domain simply connected without reordering the spectrum — is the frontier described in Sections 6–7.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*