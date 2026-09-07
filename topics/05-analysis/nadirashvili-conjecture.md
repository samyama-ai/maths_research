---
id: 05-analysis/nadirashvili-conjecture
title: "Nadirashvili's Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nadirashvili's Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/nadirashvili-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Nadirashvili's conjecture asserts a **uniform, dimension-only lower bound on the size of the zero set of a harmonic function that vanishes at a point**.

> **Conjecture (Nadirashvili, 1997).** For every $n \ge 2$ there is $c(n) > 0$ such that every non-constant harmonic function $u : \mathbb{R}^n \to \mathbb{R}$ with $u(0) = 0$ satisfies
> $$\mathcal{H}^{n-1}\big(\{u = 0\} \cap B_1(0)\big) \;\ge\; c(n).$$

The point is that $c$ depends on **nothing but $n$** — not on the degree, the doubling index, or the oscillation of $u$. The statement is scale-invariant in the sense that no normalization of $\|u\|_\infty$ is allowed.

**Status of the page.** The statement above was proved by Aleksandr Logunov (*Annals of Mathematics*, 2018). What this entry tracks is the conjecture in the form that is **still open**, and which is what "Nadirashvili's conjecture" now denotes in the literature:

* **(N1) Variable-coefficient form.** Does the same uniform bound hold for solutions of $\operatorname{div}(A(x)\nabla u) = 0$ with $A$ uniformly elliptic and merely Lipschitz (or Hölder, or measurable)? A proof must produce $c = c(n,\Lambda)$ depending only on dimension and the ellipticity/regularity constants of $A$.
* **(N2) Sharp constant.** Determine the optimal $c(n)$. The natural guess is $c(n) = \omega_{n-1} := |B_1^{n-1}|$, attained only by linear functions.
* **(N3) The companion upper bound (Yau's conjecture).** For a closed smooth Riemannian $(M^n,g)$ and $\Delta_g \varphi_\lambda + \lambda \varphi_\lambda = 0$, prove $\mathcal{H}^{n-1}(\{\varphi_\lambda = 0\}) \le C(M,g)\sqrt{\lambda}$.

A resolution of (N1) means a proof or an explicit counterexample family with nodal measure tending to $0$; of (N3), matching $\sqrt{\lambda}$ upper and lower bounds for smooth metrics.

## 2. Mathematical Foundations

**Nodal set.** For $u$ continuous, $Z(u) = \{x : u(x)=0\}$. If $\Delta u = 0$ and $u \not\equiv 0$, then $Z(u)$ is a real-analytic hypersurface away from the critical set $\Sigma = Z(u) \cap \{\nabla u = 0\}$, and $\dim_{\mathcal H}\Sigma \le n-2$. Hence $\mathcal{H}^{n-1}\llcorner Z(u)$ is the natural measure.

**Doubling index / frequency.** For $u$ harmonic in $B_{2r}(x)$ set
$$N(x,r) \;=\; \frac{r \int_{B_r(x)} |\nabla u|^2}{\int_{\partial B_r(x)} u^2}, \qquad
\mathcal{N}(x,r) \;=\; \log_2 \frac{\sup_{B_{2r}(x)} |u|}{\sup_{B_r(x)} |u|}.$$
Almheim–Frederick–Garofalo–Lin monotonicity: $r \mapsto N(x,r)$ is non-decreasing for harmonic $u$, and almost monotone ($e^{Cr}N(x,r)$ monotone) for $\operatorname{div}(A\nabla u)=0$ with $A$ Lipschitz (Garofalo–Lin, 1986). $N$ and $\mathcal N$ are comparable up to $C(n)$, and $N(0,0^+) = k$ equals the vanishing order.

**Model local behaviour.** If $u$ vanishes to order $k$ at $0$, then $u = P_k + O(|x|^{k+1})$ with $P_k$ a nonzero harmonic homogeneous polynomial of degree $k$; $Z(P_k)$ is a cone over a hypersurface in $S^{n-1}$. In $n=2$, $P_k = \operatorname{Re}(c\,z^k)$ up to rotation, so $Z(P_k)$ is exactly $2k$ equiangular rays.

**Standard two-sided comparison (Donnelly–Fefferman regime).** If the doubling index satisfies $\mathcal N(x,r) \le N$ on $B_1$, then
$$c(n)\,\big(\text{something like } 1\big) \;\le\; \mathcal{H}^{n-1}(Z(u)\cap B_{1/2}) \;\le\; C(n)\,N .$$
The upper bound $\le C(n)N$ is classical (integral-geometric projection plus Crofton); the lower bound *without* an upper bound on $N$ is exactly Nadirashvili's difficulty: a large frequency could in principle hide almost all nodal area outside the ball.

**Simplex/Remez inequality (Logunov's engine).** For $u$ harmonic in $B_1$ with doubling index $N$ and $E \subset B_{1/2}$,
$$\sup_{B_{1/2}} |u| \;\le\; \Big(\frac{C|B_{1/2}|}{|E|}\Big)^{CN} \sup_E |u|,$$
a quantitative unique-continuation statement that lets one convert "small nodal set" into "$u$ nearly of one sign", contradicting the mean value property $u(0)=0$.

## 3. History & State of the Art (SOTA)

* **1978.** Brüning: $\mathcal{H}^1(Z(\varphi_\lambda)) \ge c\sqrt{\lambda}$ on surfaces — the $n=2$ case of the eigenfunction lower bound.
* **1988.** Donnelly–Fefferman: for **real-analytic** $(M,g)$, $c\sqrt\lambda \le \mathcal{H}^{n-1}(Z(\varphi_\lambda)) \le C\sqrt\lambda$ in all dimensions. Yau's conjecture is settled in the analytic category.
* **1989.** Hardt–Simon: for smooth metrics, only the exponential upper bound $\mathcal{H}^{n-1} \le C\lambda^{C\sqrt\lambda}$.
* **1997.** Nadirashvili, *Geometry of nodal sets and multiplicity of eigenvalues*, states the harmonic-function conjecture as the local, scale-free core of the eigenfunction lower bound.
* **1992–2011.** Partial smooth-category lower bounds: Dong ($n=2$, $\mathcal{H}^1 \le C\lambda^{3/4}$); Colding–Minicozzi and Sogge–Zelditch, $\mathcal{H}^{n-1} \ge c\lambda^{(3-n)/4}$; Mangoubi refinements.
* **2016–2018.** Logunov proves Nadirashvili's conjecture and, as a corollary, the lower bound $\mathcal{H}^{n-1}(Z(\varphi_\lambda)) \ge c\sqrt\lambda$ in Yau's conjecture, all $n$, smooth metrics; in a companion paper he proves the first **polynomial** upper bound $\mathcal{H}^{n-1} \le C\lambda^{\alpha(n)}$ with $\alpha(n) > 1/2$ depending only on $n$.
* **2018.** Logunov–Malinnikova sharpen the $2$- and $3$-dimensional upper bounds below Dong's exponent.
* **2018–present.** No proof of the sharp $\sqrt\lambda$ upper bound; no extension of the lower bound to non-smooth coefficients with constants independent of the coefficient modulus of continuity; no sharp $c(n)$ for $n \ge 3$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n = 2$, harmonic | Proved, with **sharp** constant $c(2) = 2$ (see §10) | elementary; Brüning 1978 for eigenfunctions |
| All $n$, harmonic / smooth metrics | Proved: $c(n)>0$ exists | Logunov 2018 |
| Real-analytic metrics, all $n$ | Two-sided $c\sqrt\lambda \le \mathcal H^{n-1} \le C\sqrt\lambda$ | Donnelly–Fefferman 1988 |
| Bounded doubling index $\mathcal N \le N$ | $\mathcal{H}^{n-1}(Z \cap B_{1/2}) \asymp_{n} 1$ to $C N$; both bounds classical | Hardt–Simon; Han–Lin |
| $\operatorname{div}(A\nabla u)=0$, $A$ Lipschitz | Nodal set is $(n-1)$-rectifiable with **upper** Minkowski bound $C(n,\Lambda,N)$; effective critical-set estimates $\dim \Sigma \le n-2$ | Naber–Valtorta 2017 |
| Yau upper bound, $n=2$ | $\mathcal{H}^1(Z(\varphi_\lambda)) \le C\lambda^{3/4}$, improved to $C\lambda^{3/4-\beta}$ for some $\beta>0$ | Dong 1992; Logunov–Malinnikova 2018 |
| Yau upper bound, all $n$ | $\mathcal{H}^{n-1} \le C\lambda^{\alpha(n)}$, $\alpha(n)>1/2$ | Logunov 2018 |

## 5. Principal Obstacles

* **No compactness in the frequency.** The family of harmonic functions with $u(0)=0$ is not precompact modulo scaling: doubling indices are unbounded. Any argument using a normal-families limit loses exactly the case that matters.
* **Frequency can concentrate.** Near a point the local doubling index can be huge while being $O(1)$ on most of the ball. Logunov's proof is a **combinatorial subdivision** of a cube into $A^n$ subcubes plus a "hyperplane lemma" controlling how many children can inherit a comparable index. Both steps use the *exact* monotonicity of $N$ and the harmonic Remez inequality. With Lipschitz $A(x)$, monotonicity is only almost-monotone with a multiplicative error $e^{Cr}$; the subdivision iterates $\sim \log(1/r)$ times, and the accumulated errors are not yet shown to be summable at the required rate.
* **No Remez inequality for rough coefficients with the right constants.** The quantitative unique continuation $\sup_{B}|u| \le (C/|E|)^{CN}\sup_E|u|$ is proved for harmonic functions via harmonic measure and analytic continuation of $u$ into $\mathbb{C}^n$. For measurable $A$, solutions are only $C^{0,\alpha}$ and no complexification exists; Landis-type unique continuation is available but with constants degenerating in the modulus of continuity of $A$.
* **Upper bound (N3): the wrong integral-geometric input.** All known upper bounds pass through Crofton's formula plus a count of zeros on lines, which costs a factor of the doubling index $N \sim \sqrt\lambda$ *per direction*, giving $\lambda^{1/2 + \epsilon}$ at best; recovering the sharp $\sqrt\lambda$ needs cancellation across directions that no current tool supplies.
* **Sharp constant (N2).** The Logunov argument is by contradiction with a small parameter produced by an iteration; it yields $c(n)$ that is not effective — not even a decidable numeric value — so it says nothing about $\omega_{n-1}$.

## 6. The Gap

Proven: existence of $c(n)>0$ for the *constant-coefficient Laplacian* (equivalently, smooth metrics, by freezing coefficients and rescaling).

Open, and the precise barrier:

1. **From smooth to Lipschitz/measurable $A$.** Concretely, one needs: a hyperplane/subdivision lemma for the almost-monotone frequency of $\operatorname{div}(A\nabla u)$ in which the number of "high-index" child cubes is bounded by $C(n)A^{n-1}$ *uniformly in scale*, together with a Remez inequality with exponent $CN$ and constants depending only on $(n,\Lambda,\|A\|_{\mathrm{Lip}})$. Neither exists.
2. **From $\lambda^{\alpha}$, $\alpha>1/2$, to $\lambda^{1/2}$.** The gap is the loss $\alpha(n)-\tfrac12 > 0$ produced by Logunov's cube counting; closing it requires an upper bound on nodal measure that is *linear* in the doubling index at every scale, not merely polynomially controlled.
3. **From non-effective to sharp.** Extract an explicit $c(n)$ and prove rigidity: equality iff $u$ is linear.

## 7. Current Research (as of June 2026)

* **Rough-coefficient nodal geometry.** Groups around Naber and Valtorta (Northwestern; Milan) push quantitative stratification and Minkowski estimates for critical sets of $\operatorname{div}(A\nabla u)=0$; the lower-bound direction with Lipschitz $A$ is the announced target. *(frontier — verify)*
* **Harmonic-measure / Remez methods.** Logunov, Malinnikova and collaborators continue the combinatorial programme; the survey *Review of Yau's conjecture on zero sets of Laplace eigenfunctions* remains the reference blueprint and lists the Lipschitz-coefficient extension as Problem 1.
* **Two-dimensional sharp upper bounds.** Work by Logunov, Malinnikova, Nadirashvili and Nazarov on Dirichlet eigenfunctions in planar domains aims at $\lambda^{3/4}$-type bounds being sharp or improvable for specific boundary geometry. *(frontier — verify)*
* **Uniform rectifiability route.** Tolsa, Puliatti and coauthors (Barcelona) study nodal/singular sets of elliptic measures with Dini or Hölder coefficients; a Remez inequality in that category would be immediately relevant. *(frontier — verify)*
* **Numerics.** Direct computation is of limited value: any attempted counterexample must have unbounded doubling index, so finite-degree harmonic polynomials always satisfy the bound with room to spare.

## 8. Future Work

* Prove a **scale-uniform hyperplane lemma** for almost-monotone frequencies; this single ingredient would transfer Logunov's proof to Lipschitz coefficients essentially verbatim.
* Develop a **Remez-type inequality for $A$-harmonic functions** replacing complexification by $A$-harmonic measure and Carleman estimates with explicit constant dependence.
* Attack (N2) in $n=3$: classify harmonic homogeneous $P_k$ minimizing $\mathcal{H}^2(Z(P_k)\cap B_1)$ per degree; show the minimum is increasing in $k$ with $k=1$ the global minimum.
* For (N3), search for an averaged Crofton estimate: bound $\int_{S^{n-1}} \\#\{Z(u) \cap \ell_\theta\}\,d\theta$ by $C\sqrt\lambda$ directly, exploiting that high-multiplicity directions form a small set.
* Test the boundary of the phenomenon: construct uniformly elliptic **measurable** $A$ in $n \ge 3$ and $A$-harmonic $u$ with $u(0)=0$ and nodal measure in $B_1$ arbitrarily small — a counterexample here would sharply localize the regularity threshold.

## 9. Key References

- **[Foundational]** N. Nadirashvili. *Geometry of nodal sets and multiplicity of eigenvalues.* Current Developments in Mathematics 1997, International Press, 1999, pp. 231–235.
- **[Foundational]** H. Donnelly, C. Fefferman. *Nodal sets of eigenfunctions on Riemannian manifolds.* Inventiones Mathematicae 93 (1988), 161–183.
- **[Foundational]** R. Hardt, L. Simon. *Nodal sets for solutions of elliptic equations.* Journal of Differential Geometry 30 (1989), 505–522.
- **[Foundational]** N. Garofalo, F.-H. Lin. *Monotonicity properties of variational integrals, $A_p$ weights and unique continuation.* Indiana University Mathematics Journal 35 (1986), 245–268.
- **[SOTA]** A. Logunov. *Nodal sets of Laplace eigenfunctions: proof of Nadirashvili's conjecture and of the lower bound in Yau's conjecture.* Annals of Mathematics 187 (2018), no. 1, 241–262.
- **[SOTA]** A. Logunov. *Nodal sets of Laplace eigenfunctions: polynomial upper estimates of the Hausdorff measure.* Annals of Mathematics 187 (2018), no. 1, 221–239.
- **[SOTA]** A. Logunov, E. Malinnikova. *Nodal sets of Laplace eigenfunctions: estimates of the Hausdorff measure in dimensions two and three.* In *50 Years with Hardy Spaces*, Operator Theory: Advances and Applications 261, Birkhäuser, 2018, pp. 333–344.
- **[SOTA]** A. Naber, D. Valtorta. *Volume estimates on the critical sets of solutions to elliptic PDEs.* Communications on Pure and Applied Mathematics 70 (2017), 1835–1897.
- **[Related]** T. H. Colding, W. P. Minicozzi II. *Lower bounds for nodal sets of eigenfunctions.* Communications in Mathematical Physics 306 (2011), 777–784.
- **[Related]** R.-T. Dong. *Nodal sets of eigenfunctions on Riemann surfaces.* Journal of Differential Geometry 36 (1992), 493–506.
- **[Survey]** A. Logunov, E. Malinnikova. *Review of Yau's conjecture on zero sets of Laplace eigenfunctions.* Current Developments in Mathematics 2018, International Press, 2020.
- **[Survey]** Q. Han, F.-H. Lin. *Nodal Sets of Solutions of Elliptic Differential Equations.* Book manuscript, 2007 (widely circulated lecture notes).

## 10. Worked Example / Concrete Special Case

**The case $n = 2$, with the sharp constant.**

Let $u$ be harmonic and non-constant on $\mathbb{R}^2 \cong \mathbb{C}$ with $u(0)=0$. Write $u = \operatorname{Re} f$ for an entire $f$ with $f(0)=0$, and let $k \ge 1$ be the order of vanishing of $f'$ plus one, i.e. $f(z) = c z^k(1+O(z))$, $c \ne 0$.

*Local structure.* Near $0$, $u(z) = |c|\,r^k\cos(k\theta + \arg c) + O(r^{k+1})$. The zero set of the leading term is the union of $2k$ rays at angles $\theta_j = \frac{1}{k}\big(\tfrac{\pi}{2} - \arg c + j\pi\big)$, $j=0,\dots,2k-1$. Because these are simple zeros of $\cos$, the implicit function theorem applies on $\{r>0\}$ and $Z(u)$ near $0$ is exactly $2k$ real-analytic arcs meeting at $0$ at equal angles $\pi/k$.

*Global continuation.* $Z(u)$ has no endpoints in $\mathbb{R}^2$: at every point either $\nabla u \ne 0$ (so $Z(u)$ is locally a curve) or $u$ vanishes to some order $m$ (so $2m$ arcs meet). So each of the $2k$ arcs leaving $0$ can be continued until it leaves $B_1$ — it cannot terminate inside, and if it returns to a previously visited point it bounds a bounded domain $\Omega$ with $u|_{\partial\Omega}=0$, forcing $u \equiv 0$ on $\Omega$ by the maximum principle, hence $u\equiv0$ by analyticity. Contradiction.

*Measure count.* Each arc runs from $0$ to $\partial B_1$, so has length $\ge 1$. There are $2k$ of them, pairwise disjoint except at $0$:
$$\mathcal{H}^1\big(Z(u)\cap B_1\big) \;\ge\; 2k \;\ge\; 2 .$$

*Sharpness.* $u(x,y)=x$ gives $Z(u)\cap B_1 = \{0\}\times(-1,1)$, of length exactly $2$. So $c(2)=2$, attained precisely by linear functions ($k=1$ and both arcs are radii, forcing straightness).

*Why $n\ge 3$ is not the same argument.* The step "each arc has length $\ge 1$" uses that a $1$-dimensional nodal component through the centre must reach the boundary. In $\mathbb{R}^n$ the nodal set is a hypersurface, and while it still cannot terminate inside $B_1$, a hypersurface through $0$ reaching $\partial B_1$ has $\mathcal{H}^{n-1}$-measure bounded below only if it is not allowed to be a thin "spike". Ruling out spikes is precisely a quantitative unique-continuation problem, and is what Logunov's Remez inequality supplies — and what remains unavailable once the Laplacian is replaced by $\operatorname{div}(A(x)\nabla\cdot)$ with rough $A$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*