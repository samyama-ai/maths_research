---
id: 06-pdes/hot-spots-conjecture
title: "Hot Spots Conjecture"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hot Spots Conjecture

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/hot-spots-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ be a bounded connected domain with (say) Lipschitz boundary, and let $u$ solve the heat equation with insulated (Neumann) boundary:
$$\partial_t u = \Delta u \ \text{ in } \Omega\times(0,\infty), \qquad \partial_\nu u = 0 \ \text{ on } \partial\Omega\times(0,\infty), \qquad u(\cdot,0)=u_0 \in L^2(\Omega).$$

**Conjecture (Rauch, 1974).** For generic initial data, the point of maximal temperature ("hot spot") migrates to the boundary: $\operatorname{dist}(\arg\max_x u(\cdot,t),\partial\Omega)\to 0$ as $t\to\infty$.

Since $u(\cdot,t)=\bar u_0+e^{-\mu_2 t}\,c_2\varphi_2+O(e^{-\mu_3 t})$, where $\mu_2$ is the first nonzero Neumann eigenvalue, the conjecture reduces (when $\mu_2$ is simple and $c_2\ne 0$) to a statement about the **second Neumann eigenfunction**:

**Conjecture (eigenfunction form).** If $\varphi_2$ satisfies $\Delta\varphi_2 + \mu_2\varphi_2 = 0$ in $\Omega$, $\partial_\nu\varphi_2 = 0$ on $\partial\Omega$, then
$$\max_{\overline\Omega}\varphi_2 = \max_{\partial\Omega}\varphi_2 \quad\text{and}\quad \min_{\overline\Omega}\varphi_2 = \min_{\partial\Omega}\varphi_2 ,$$
i.e. $\varphi_2$ attains its extrema only on $\partial\Omega$ (**weak form**: attains them also on $\partial\Omega$; **strong form**: has no interior critical point at all).

The conjecture is **false in general** (Burdzy–Werner 1999, multiply connected planar domains) and **true** in several broad classes. The live problem is:

> **Open problem.** Does the hot spots conjecture hold for every bounded **convex** domain in $\mathbb{R}^n$, $n\ge 2$? More weakly, for every simply connected planar domain?

A complete resolution means either a proof for all convex (resp. simply connected) domains, or an explicit counterexample with a rigorous, computer-assisted-or-not verification that $\varphi_2$ has an interior extremum.

## 2. Mathematical Foundations

**Neumann spectrum.** On a bounded Lipschitz $\Omega$, the form $a(u,v)=\int_\Omega \nabla u\cdot\nabla v$ on $H^1(\Omega)$ has compact resolvent; the spectrum is discrete,
$$0=\mu_1<\mu_2\le\mu_3\le\cdots\to\infty,$$
with $\varphi_1$ constant and
$$\mu_2=\min\Big\{\tfrac{\int_\Omega|\nabla v|^2}{\int_\Omega v^2}\ :\ v\in H^1(\Omega)\setminus\{0\},\ \int_\Omega v=0\Big\}.$$
Courant's nodal theorem gives $\varphi_2$ exactly two nodal domains.

**Heat semigroup.** $u(\cdot,t)=e^{t\Delta_N}u_0=\sum_{k\ge1}e^{-\mu_k t}\langle u_0,\varphi_k\rangle\varphi_k$ with $\|\varphi_k\|_{L^2}=1$. Hence the asymptotic reduction in §1.

**Probabilistic form.** The Neumann heat semigroup is the transition semigroup of **reflecting Brownian motion** (RBM) $X_t$ in $\overline\Omega$, solving the Skorokhod problem
$$dX_t=dB_t+\nu(X_t)\,dL_t,$$
with $L$ the boundary local time. Then $u(x,t)=\mathbb{E}^x[u_0(X_t)]$, and the conjecture says the RBM started far inside spends comparatively more time near the "hot" end of the domain. **Mirror/scaling couplings** of two RBMs $(X,Y)$ are the main probabilistic tool: if the coupling can be run so that $\varphi_2(X_t)-\varphi_2(Y_t)$ has a sign, monotonicity of $\varphi_2$ along a direction follows.

**Related quantities.** For convex $\Omega$ with diameter $d$ and inradius $\rho$, Payne–Weinberger gives $\mu_2\ge \pi^2/d^2$, sharp in the thin-limit. On thin convex domains $\varphi_2$ is close to the 1-D Neumann mode $\cos(\pi s/d)$ along the long axis — the heuristic behind the conjecture.

**Lip domain.** A planar domain that is the region between graphs of two Lipschitz-1 functions; equivalently, bounded by two graphs of slope $\le 1$ in rotated coordinates. Lip domains are simply connected but need not be convex.

## 3. History & State of the Art (SOTA)

- **1974** — Jeffrey Rauch states the conjecture in a lecture at a Tulane PDE conference; it circulates as folklore for two decades.
- **1999** — Bañuelos and Burdzy (*J. Funct. Anal.* 164) give the first systematic treatment: proofs for obtuse triangles, certain "lip-like" and symmetric planar domains, plus the coupling framework.
- **1999** — Burdzy and Werner (*Ann. of Math.* 149) construct a **planar domain with two holes** where $\varphi_2$ has a strict interior maximum: the conjecture is false in general.
- **2000** — Jerison and Nadirashvili (*J. Amer. Math. Soc.* 13) prove the conjecture for planar convex domains with **two orthogonal axes of symmetry**.
- **2004** — Atar and Burdzy (*J. Amer. Math. Soc.* 17) prove it for all planar **lip domains** using a mirror-coupling/synchronous-coupling argument.
- **2005** — Burdzy (*Duke Math. J.* 129) sharpens the counterexample to a domain with **one hole** (not simply connected).
- **2020** — Judge and Mondal (*Ann. of Math.* 191) prove the conjecture, in strong form, for **all Euclidean triangles**: $\mu_2$ is simple and $\varphi_2$ has no interior critical point. (Erratum/correction published 2022.)
- **2021** — Kleefeld gives high-accuracy numerics indicating failure for certain non-convex, non-simply-connected planar domains, and validates the triangle results.

Status today: true for triangles, lip domains, doubly symmetric convex planar domains, thin/long convex domains; false for some multiply connected planar domains; **open for general convex domains in the plane and in all dimensions $n\ge3$, and for general simply connected planar domains.**

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Obtuse triangles (angle $\ge \pi/2$) | Weak + strong form | Bañuelos–Burdzy 1999; Siudeja 2015 |
| **All triangles** in $\mathbb{R}^2$ | $\mu_2$ simple; $\varphi_2$ has no interior critical point; extrema at two vertices | Judge–Mondal 2020 |
| Planar **lip domains** (boundary slopes $\le1$) | Weak form; $\varphi_2$ monotone along the diagonal direction | Atar–Burdzy 2004 |
| Planar convex domains with **two orthogonal symmetry axes** | Weak form; $\varphi_2$ monotone in one coordinate | Jerison–Nadirashvili 2000 |
| Convex $\Omega\subset\mathbb{R}^n$ with diameter/inradius ratio large ("thin") | Extrema within $O(\text{inradius})$ of the boundary/tips | Steinerberger 2020 |
| Convex planar domains, one axis of symmetry (with additional hypotheses) | Weak form under a Neumann-line/symmetry condition | Miyamoto 2009–2013; Pascu 2002 |
| Product domains, balls, rectangles, spherical sectors | Explicit eigenfunctions, extrema on $\partial\Omega$ | Classical separation of variables |
| Domains with 2 holes (Burdzy–Werner), 1 hole (Burdzy) | **Counterexamples**: interior maximum | Burdzy–Werner 1999; Burdzy 2005 |
| Non-convex simply connected numerical candidates | No verified counterexample known | Kleefeld 2021 |

For the ball $B^n$: $\varphi_2 = f(r)\,\frac{x_i}{r}$ with $f(r)=r^{1-n/2}J_{n/2}(kr)$, $k$ the first positive zero of $J'_{n/2}$; extrema at antipodal boundary points. For the square $(0,1)^2$: $\mu_2=\pi^2$ is **double**, eigenspace spanned by $\cos\pi x,\cos\pi y$ — extrema still on $\partial\Omega$ for every element of the eigenspace, but simplicity fails, showing the generic-data caveat is needed.

## 5. Principal Obstacles

- **No maximum principle for $\varphi_2$.** The equation $\Delta\varphi_2=-\mu_2\varphi_2$ has the wrong sign for elliptic maximum-principle arguments; the extremum location is a *global* spectral fact, not a local one.
- **Failure of the derivative trick.** For the first Dirichlet eigenfunction, log-concavity (Brascamp–Lieb) forces a unique interior maximum. The natural analogue here would be a convexity/monotonicity property of $\partial_e\varphi_2$, but $\partial_e\varphi_2$ solves the *Dirichlet-on-part-of-the-boundary* problem with a boundary term $\propto$ the curvature of $\partial\Omega$, which has no sign in general and is a measure at corners.
- **Coupling arguments break at non-convexity and at obtuse corners.** Mirror coupling of RBMs works when the reflecting boundary is "in the right direction relative to the mirror"; this is exactly the lip/convex-symmetric hypothesis. For general convex bodies in $n\ge3$ no coupling has been shown to preserve the required order.
- **Topology genuinely matters.** Burdzy–Werner's counterexample localizes eigenfunction mass in thin necks around a hole; nothing in the standard PDE toolkit distinguishes "simply connected" from "multiply connected" at the level of $\varphi_2$, so any proof must use topology essentially.
- **Degeneracy of $\mu_2$.** For symmetric domains $\mu_2$ can be multiple (square, disk, equilateral triangle), so statements must hold for the whole eigenspace; perturbation/continuity arguments in a family of domains lose analyticity at crossings. Judge–Mondal had to prove simplicity of $\mu_2$ for triangles as a separate, hard step.
- **Numerics cannot close it.** An interior maximum in a candidate convex domain would be a tiny quantity; certifying it needs validated eigenvalue enclosures plus rigorous $C^1$ bounds on the eigenfunction, currently done only in special polygonal settings.

## 6. The Gap

Proven cases share one of two structural crutches: (i) an explicit **ordering direction** (lip condition, symmetry axis, triangle's altitude foliation) along which $\varphi_2$ can be shown monotone, or (ii) an **explicit eigenfunction**. A general convex body in $\mathbb{R}^2$ has neither a canonical monotonicity direction nor symmetry; convex bodies in $\mathbb{R}^n$ additionally lack the planar tools (conformal maps, nodal-line-is-a-curve arguments, two-dimensional coupling geometry) used in every planar proof.

Concretely, the missing step is: **for a convex $\Omega$, show that the nodal set of $\varphi_2$ is a hypersurface meeting $\partial\Omega$ transversally and that $\varphi_2$ has no critical point in the open domain** — equivalently, that the level sets of $\varphi_2$ foliate each nodal domain without closed leaves. Judge–Mondal achieve exactly this for triangles by a deformation argument through the space of triangles, which has 2 parameters and explicit degenerations (thin triangles, right triangles). The space of convex bodies is infinite-dimensional with no analogous compactification with explicitly solvable extremes.

## 7. Current Research (as of June 2026)

- **Deformation/continuity methods beyond triangles.** Extension of the Judge–Mondal machinery (variational vector fields, counting interior critical points as a homotopy invariant) to convex polygons with $\ge4$ vertices — quadrilaterals are the first target *(frontier — verify)*.
- **Probabilistic couplings.** Continued work in the Burdzy school (Washington) on scaling and mirror couplings for RBM in convex bodies, and on quantitative "hot spots up to an inradius" statements.
- **Rigorous computer-assisted spectral analysis.** Validated finite-element / method-of-particular-solutions enclosures for $\mu_2,\mu_3$ and $\nabla\varphi_2$ on polygons, extending Kleefeld's and Siudeja-type computations to certify absence of interior critical points on families of convex polygons.
- **Discrete and graph analogues.** Hot spots for the Neumann Laplacian on quantum graphs and for graph Laplacians (Rohleder and coauthors), where counterexamples are easier to construct and clarify what convexity buys.
- **Quantitative/robust versions.** Steinerberger-style bounds locating extrema within $C\cdot\text{inradius}$ of $\partial\Omega$ for convex domains in all dimensions, sharpening the constant $C$.

## 8. Future Work

1. **Prove the conjecture for convex polygons** by induction on the number of vertices, using the triangle case as a base and a deformation that merges vertices.
2. **Find a coupling that survives $n\ge3$**: identify a geometric condition on convex bodies (e.g. a "lip condition in every 2-plane") under which mirror coupling of RBM preserves order.
3. **Settle the simply connected planar case**: either extend lip-domain results to all simply connected domains via conformal mapping (the Neumann problem transforms with a conformal weight $|f'|^2$, so the question becomes a weighted eigenvalue problem on the disk), or build a simply connected counterexample by thinning necks without adding a hole.
4. **Establish simplicity of $\mu_2$** for general convex domains — currently open and a prerequisite for a clean statement.
5. **Certified numerics at scale**: sweep large families of convex polygons with rigorous enclosures to either find a counterexample or produce strong evidence and, ideally, a proof template.

## 9. Key References

- **[Foundational]** J. Rauch. *Five problems: an introduction to the qualitative theory of partial differential equations.* In: Partial Differential Equations and Related Topics, Lecture Notes in Mathematics 446, Springer, 1975, pp. 355–369. (Original statement of the hot spots problem.)
- **[Foundational]** R. Bañuelos, K. Burdzy. *On the "hot spots" conjecture of J. Rauch.* Journal of Functional Analysis 164 (1999), 1–33.
- **[Counterexample]** K. Burdzy, W. Werner. *A counterexample to the "hot spots" conjecture.* Annals of Mathematics 149 (1999), 309–317.
- **[Counterexample]** K. Burdzy. *The hot spots problem in planar domains with one hole.* Duke Mathematical Journal 129 (2005), 481–502.
- **[SOTA]** C. Judge, S. Mondal. *Euclidean triangles have no hot spots.* Annals of Mathematics 191 (2020), 167–211. (Correction: Annals of Mathematics 195 (2022), 337–362.)
- **[SOTA]** R. Atar, K. Burdzy. *On Neumann eigenfunctions in lip domains.* Journal of the American Mathematical Society 17 (2004), 243–265.
- **[Structural]** D. Jerison, N. Nadirashvili. *The "hot spots" conjecture for domains with two axes of symmetry.* Journal of the American Mathematical Society 13 (2000), 741–772.
- **[Structural]** R. D. Bass, K. Burdzy. *Fiber Brownian motion and the "hot spots" problem.* Duke Mathematical Journal 105 (2000), 25–58.
- **[Quantitative]** S. Steinerberger. *Hot spots in convex domains are in the tips (up to an inradius).* Communications in Partial Differential Equations 45 (2020), 641–654.
- **[Computational]** A. Kleefeld. *The hot spots conjecture can be false: some numerical examples.* Advances in Computational Mathematics 47 (2021), article 85.
- **[Related classes]** B. Siudeja. *Hot spots of weakly symmetric convex planar domains.* Journal of Mathematical Analysis and Applications 400 (2013), 98–103.
- **[Survey]** K. Burdzy. *The hot spots problem: attempts to solve a $\$1000$ problem.* Lecture notes / expository article, University of Washington. See also the Polymath 7 project pages on the hot spots conjecture.

## 10. Worked Example / Concrete Special Case

**Rectangle.** Let $\Omega=(0,a)\times(0,b)$ with $a>b>0$. Separation of variables gives the Neumann eigenfunctions
$$\varphi_{m,n}(x,y)=\cos\!\Big(\frac{m\pi x}{a}\Big)\cos\!\Big(\frac{n\pi y}{b}\Big),\qquad \mu_{m,n}=\pi^2\Big(\frac{m^2}{a^2}+\frac{n^2}{b^2}\Big),\ m,n\ge0 .$$
The smallest nonzero eigenvalue is $\mu_2=\pi^2/a^2$ (taking $m=1,n=0$), simple because $a>b$. So
$$\varphi_2(x,y)=\cos(\pi x/a),$$
with $\max=1$ at $x=0$ and $\min=-1$ at $x=a$: both on $\partial\Omega$, and $\nabla\varphi_2=(-\tfrac{\pi}{a}\sin(\pi x/a),0)$ vanishes only where $x\in\{0,a\}$, i.e. on the boundary. The strong form holds.

Heat-equation check: take $u_0(x,y)=\cos(\pi x/a)+\tfrac12\cos(2\pi x/a)$. Then
$$u(x,y,t)=e^{-\pi^2 t/a^2}\cos(\pi x/a)+\tfrac12 e^{-4\pi^2 t/a^2}\cos(2\pi x/a).$$
Setting $\partial_x u=0$: $\sin(\pi x/a)\big[1+2e^{-3\pi^2t/a^2}\cos(\pi x/a)\big]=0$. For $t> \frac{a^2}{3\pi^2}\ln 2$ the bracket is positive, so the only critical points are $x\in\{0,a\}$: the hot spot sits at $x=0$ for all large $t$. For small $t$ the bracket can vanish at $\cos(\pi x/a)=-\tfrac12 e^{3\pi^2 t/a^2}$, giving a genuine interior critical point — illustrating that the conjecture is asymptotic in $t$, not valid at every time.

**Contrast (why the square is excluded).** For $a=b$, $\mu_2=\pi^2/a^2$ has multiplicity 2, eigenspace $\operatorname{span}\{\cos(\pi x/a),\cos(\pi y/a)\}$. Every element $\alpha\cos(\pi x/a)+\beta\cos(\pi y/a)$ still attains its extrema at corners, but the eigenfunction is no longer determined by $\Omega$; this degeneracy is the mechanism that makes perturbation arguments in families of domains fail, and it is precisely what Judge–Mondal had to rule out (by proving $\mu_2$ simple) for non-equilateral triangles.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*