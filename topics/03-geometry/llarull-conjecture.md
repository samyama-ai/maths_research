---
id: 03-geometry/llarull-conjecture
title: "Llarull Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Llarull Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/llarull-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The round sphere should be *extremal* for scalar curvature: one cannot make a sphere both bigger and more positively curved.

**Llarull rigidity (statement).** Let $(M^n,g)$ be a closed connected oriented Riemannian $n$-manifold, $n\ge 2$, and let
$$f:(M^n,g)\longrightarrow (S^n,g_0)$$
be a smooth map to the unit round sphere with $\deg f\neq 0$. Assume

1. $f$ is $1$-Lipschitz (distance non-increasing), i.e. $|df(v)|\le |v|$ for all $v\in TM$; and
2. $\mathrm{Scal}_g \ge n(n-1) = \mathrm{Scal}_{g_0}$.

Then $f$ is a Riemannian isometry (in particular $\deg f=\pm 1$ and $g$ is the round metric).

Llarull proved this in 1998 **under the additional hypothesis that $M$ is spin**. The "Llarull conjecture" as tracked in the literature is the removal of that hypothesis, posed by Gromov, together with its sharpening:

- **(L1) Non-spin case.** The conclusion holds for every closed oriented $M^n$, with no spin assumption.
- **(L2) Area-extremality (Gromov).** Hypothesis (1) may be weakened to *area non-increasing*, $\|\Lambda^2 df\|\le 1$, in **all** dimensions (Llarull settled $n$ even).

A complete resolution means a proof valid for all $n$ and all oriented $M$, or a counterexample: an oriented $M^n$ with $\mathrm{Scal}_g\ge n(n-1)$ and a non-isometric $1$-Lipschitz (resp. area non-increasing) map of nonzero degree to $S^n$.

## 2. Mathematical Foundations

**Singular values.** At $p\in M$ diagonalise $df_p$ by singular values $\lambda_1\ge\cdots\ge\lambda_n\ge 0$. Then $f$ is $1$-Lipschitz iff $\lambda_1\le 1$; area non-increasing iff $\lambda_i\lambda_j\le 1$ for all $i<j$. The second condition is strictly weaker (e.g. $\lambda_1=10$, $\lambda_2=\cdots=\lambda_n=0$).

**Spin geometry.** If $M$ is spin, let $\mathbb{S}\to M$ be the complex spinor bundle with Clifford multiplication $c$ and Dirac operator $D=\sum_i c(e_i)\nabla_{e_i}$. For a Hermitian bundle $E\to M$ with metric connection, the twisted Dirac operator $D_E$ on $\mathbb{S}\otimes E$ satisfies the **Schrödinger–Lichnerowicz formula**
$$D_E^2=\nabla^*\nabla+\frac{\mathrm{Scal}_g}{4}+\mathcal{R}^E,\qquad
\mathcal{R}^E=\tfrac12\sum_{i<j}c(e_i)c(e_j)\otimes R^E(e_i,e_j).$$

**Llarull's twist.** Take $E=f^*\mathbb{S}(S^n)$, the pullback of the spinor bundle of the round sphere. Its curvature is Clifford-algebraic,
$$R^{E}(X,Y)=-\tfrac14\, c(f_*X)\,c(f_*Y),$$
and a pointwise linear-algebra estimate gives the sharp bound
$$\big\langle \mathcal{R}^E\sigma,\sigma\big\rangle \;\ge\; -\frac12\Big(\sum_{i<j}\lambda_i\lambda_j\Big)|\sigma|^2 \;\ge\; -\frac{n(n-1)}{4}|\sigma|^2,$$
the last step using $\lambda_i\lambda_j\le 1$ and $\\#\{i<j\}=\binom n2$. Combined with $\mathrm{Scal}_g\ge n(n-1)$,
$$D_E^2\;\ge\;\nabla^*\nabla\;\ge\;0 .$$

**Index obstruction.** For $n$ even, $\mathbb{S}(S^n)=\mathbb{S}^+\oplus\mathbb{S}^-$ and Atiyah–Singer gives
$$\mathrm{ind}\,D_E^+=\int_M \hat A(M)\,\mathrm{ch}\big(f^*\mathbb{S}(S^n)\big)=(-1)^{n/2}\,2^{n/2}\deg f\neq 0,$$
since only the top Chern character term survives. For $n$ odd one applies the even case to $M\times S^1\to S^n\times S^1$ or uses a suspension/$\mathbb{Z}_2$-index. A nonzero index forces a nonzero kernel element $\sigma$; then $\nabla\sigma=0$, all inequalities are equalities, hence $\lambda_1=\cdots=\lambda_n=1$ and $\mathrm{Scal}_g\equiv n(n-1)$, so $f$ is a local isometry and (by degree/completeness) an isometry.

**Why $n$ even is easier for (L2).** With the $\pm$ splitting, $\mathcal{R}^E$ is estimated on $2$-forms directly, and only the products $\lambda_i\lambda_j$ enter; for $n$ odd the spinor module of $S^n$ is irreducible, the $S^1$-suspension introduces a flat direction with singular value $1$, and the resulting bound needs $\lambda_i\le 1$ individually.

## 3. History & State of the Art (SOTA)

- **1963.** Lichnerowicz: $\mathrm{Scal}>0$ on a closed spin manifold kills $\hat A$; the birth of Dirac-operator scalar curvature geometry.
- **1980–83.** Gromov–Lawson: the Dirac operator with twists proves non-existence and *comparison* statements (enlargeable manifolds admit no $\mathrm{Scal}>0$). The estimate is not sharp.
- **1998.** Marcelo Llarull, *Sharp estimates and the Dirac operator* (Math. Ann. 310): the sharp constant. Theorem: spin $M^n$, $1$-Lipschitz $f\to S^n$ of nonzero degree, $\mathrm{Scal}\ge n(n-1)$ $\Rightarrow$ isometry; and for $n$ even, "$1$-Lipschitz" can be relaxed to "area non-increasing".
- **2002.** Goette–Semmelmann: the same scheme for targets that are compact symmetric spaces with non-negative curvature operator and $\chi\neq0$; area-extremality proved there for even-dimensional targets.
- **2018–19.** Gromov's *Four Lectures on Scalar Curvature* isolates the non-spin case and the odd-dimensional area-extremality case as the principal open problems, and reformulates them in terms of "extremal/rigid" metrics.
- **2020–24.** Two new engines mature: (i) **$\mu$-bubbles** (weighted/prescribed-mean-curvature slicing, after Gromov and Schoen–Yau), which are spin-free; (ii) **Dirac with boundary/comparison** (Cecchini–Zeidler long-neck and mean-curvature comparison). Wang–Xie–Yu proved Gromov's dihedral extremality/rigidity conjectures for cubes by a Dirac method on manifolds with corners; Brendle proved scalar-curvature rigidity of convex polytopes; Brendle–Hirsch–Johne proved a spin-free generalisation of Geroch's conjecture in dimensions $\le 7$ using a spectral-torical slicing.
- **2023–25.** The non-spin Llarull statement is established in dimensions $n\le 7$ by slicing arguments in the Brendle–Hirsch–Johne family *(frontier — verify)*, leaving $n\ge 8$ (regularity of minimising hypersurfaces) and the odd-dimensional area version open.

## 4. Partial Results / Verified Cases

| Case | Hypothesis on $f$ | Status |
|---|---|---|
| $n=2$, any orientable surface | area = distance non-increasing | Proved, elementary (Gauss–Bonnet; see §10) |
| $n=3$ | $1$-Lipschitz | Proved — every closed orientable $3$-manifold is parallelizable, hence spin, so Llarull 1998 applies unconditionally |
| all $n\ge2$, $M$ **spin** | $1$-Lipschitz | Proved (Llarull 1998) |
| $n$ even, $M$ **spin** | area non-increasing | Proved (Llarull 1998) |
| $n$ odd, $M$ spin | area non-increasing | **Open** |
| $4\le n\le 7$, non-spin | $1$-Lipschitz | Proved by slicing/$\mu$-bubble methods *(frontier — verify)* |
| $n\ge 8$, non-spin | $1$-Lipschitz | **Open** |
| Target a compact symmetric space, $\chi\neq0$, non-negative curvature operator, even dimension | area non-increasing | Proved (Goette–Semmelmann 2002) |
| Spherical caps / bands with mean-curvature boundary condition | $1$-Lipschitz | Proved in dimension 3 ($\mu$-bubbles, Hu–Liu–Shi) and via Dirac comparison (Cecchini–Zeidler) |
| Polytopal/dihedral analogues (cubes, convex polytopes) | — | Proved (Wang–Xie–Yu; Brendle) |
| $L^\infty$ / low-regularity metrics, punctured spheres | $1$-Lipschitz | Partial: rigidity survives under $C^0$-limits and removable punctures in the spin case |

Also proved: the "$\mathrm{Scal}\ge n(n-1)$ and $g\ge g_0$ on $S^n$ implies $g=g_0$" special case (take $f=\mathrm{id}$), which is the form most often quoted.

## 5. Principal Obstacles

- **The Dirac operator needs a spin structure.** For non-spin $M$ (first possible at $n=4$, e.g. $\mathbb{CP}^2$) there is no spinor bundle, hence no Schrödinger–Lichnerowicz identity and no index. $\mathrm{spin}^c$ Dirac operators exist but carry an extra $\frac12 c(F_L)$ term of indefinite sign that destroys the sharp constant. Seiberg–Witten theory gives scalar curvature bounds only in dimension 4 and in the wrong (non-sharp, symplectic) direction.
- **Slicing loses the degree.** The minimal-hypersurface/$\mu$-bubble descent replaces $M^n$ by a hypersurface $\Sigma^{n-1}$ with a *conformally modified* scalar curvature bound. The induced map $\Sigma\to S^{n-1}$ need not be $1$-Lipschitz after the conformal change, and the constant $n(n-1)\to(n-1)(n-2)$ is not automatically preserved — the loss is exactly where sharpness lives. Warped $\mu$-bubbles fix the constant only for band-type ($T^{n-1}\times[0,1]$) geometries, and $S^n$ is not a band.
- **Regularity in dimension $\ge 8$.** Area-minimising hypersurfaces develop singular sets of codimension $7$; the Schoen–Yau and Lohkamp desingularisation programs are technically formidable and not yet accepted as complete input for a sharp rigidity statement.
- **Odd-dimensional area case.** With only $\lambda_i\lambda_j\le1$ available, the eigenvalue estimate for $\mathcal{R}^E$ fails when a single $\lambda_1$ is large; the even-dimensional argument survives because the chirality splitting lets the estimate be run on $\Lambda^2$ alone. No substitute bundle for odd $n$ is known that both has a nonzero index pairing with $\deg f$ and a curvature term controlled by $2$-forms.
- **Rigidity, not just the inequality.** Even where the inequality is provable, upgrading to "$f$ is an isometry" requires an equality analysis (parallel spinors, or a foliation by totally geodesic slices) that slicing methods deliver only after a delicate second variation argument.

## 6. The Gap

Everything proved lives in one of two regimes: **$M$ spin** (Dirac, all $n$, sharp) or **$n\le 7$** (slicing, spin-free). The general statement of §1 needs the union to be closed, so the open boundary is exactly:

1. **Non-spin, $n\ge 8$.** Needed: either a spin-free sharp comparison principle for $S^n$, or a resolution of minimal-hypersurface singularities in dimension $\ge 8$ strong enough to preserve *sharp constants and equality cases*. Passing to a finite cover does not help — spin is not attainable by covers in general — nor does $M\times T^k$, which changes the degree pairing.
2. **Area non-increasing, $n$ odd.** Needed: a twisting bundle $E\to M$ with $\mathrm{ind}\,D_E\neq 0$ tied to $\deg f$ whose curvature term obeys $\mathcal{R}^E\ge-\frac12\sum_{i<j}\lambda_i\lambda_j$ without using $\lambda_i\le1$. The $S^1$-suspension trick, which handles the Lipschitz case for odd $n$, adds a factor with singular value $1$ and therefore reintroduces the linear constraint.

## 7. Current Research (as of June 2026)

- **Spin-free sharp comparison.** Brendle (Stanford), Hirsch (IAS/Duke), Johne, and Chao Li (NYU) develop weighted slicing ("spectral torical" and $\mu$-bubble) methods that reach $n\le 7$ for a growing list of Gromov's extremality conjectures. Extending the Llarull case to $n\ge 8$ is the stated target *(frontier — verify)*.
- **Index theory on singular/corner spaces.** Wang, Xie and Yu (Texas A&M) push Dirac methods onto manifolds with corners and polyhedral boundary; the same technology is being applied to spherical caps and to $C^0$/$L^\infty$ metrics.
- **Dirac comparison with boundary.** Cecchini (Regensburg/Fordham) and Zeidler (Münster) refine long-neck and mean-curvature comparison principles; these give quantitative, non-rigid versions of Llarull with explicit deficits.
- **Low regularity and synthetic scalar curvature.** Groups in Vienna (Kunzinger, Sämann) and Fields/Toronto study whether Llarull rigidity holds for $C^0$ metrics or $\mathrm{RCD}$-type spaces, where the equality analysis must be re-founded.
- **Singularity removal.** Lohkamp's smoothing program and Schoen–Yau's induction remain the two routes to $n\ge8$; neither is regarded as settled by the community *(frontier — verify)*.

## 8. Future Work

- Find a **spin-free replacement for the index**: a degree-detecting invariant (e.g. from Gromov's "enlargeability with sharp constants", or a Cheeger–Gromov style spectral flow) that survives on non-spin manifolds.
- Prove the **odd-dimensional area case** by identifying a bundle over $S^n$ ($n$ odd) with the right Chern character; Goette–Semmelmann's symmetric-space framework is the natural place to look.
- Develop a **stability/quantitative Llarull theorem**: if $\mathrm{Scal}_g\ge n(n-1)-\varepsilon$ and $f$ is $(1+\varepsilon)$-Lipschitz, is $g$ Gromov–Hausdorff close to $g_0$? Partial answers exist only in dimension 3.
- Settle the **regularity theory for area-minimising hypersurfaces in dimension $\ge 8$** in a form that preserves equality cases, which would simultaneously close several Gromov conjectures.
- Extend to **targets other than $S^n$** with positive scalar curvature but not symmetric — currently no sharp result is known.

## 9. Key References

- **[Foundational]** Marcelo Llarull. *Sharp estimates and the Dirac operator.* Mathematische Annalen 310 (1998), 55–71. [DOI](https://doi.org/10.1007/s002080050136)
- **[Foundational]** André Lichnerowicz. *Spineurs harmoniques.* C. R. Acad. Sci. Paris 257 (1963), 7–9.
- **[Foundational]** Mikhael Gromov, H. Blaine Lawson Jr. *Positive scalar curvature and the Dirac operator on complete Riemannian manifolds.* Publications Mathématiques de l'IHÉS 58 (1983), 83–196. [DOI](https://doi.org/10.1007/bf02953774)
- **[Foundational]** H. Blaine Lawson Jr., Marie-Louise Michelsohn. *Spin Geometry.* Princeton University Press, 1989.
- **[SOTA / Recent]** Sebastian Goette, Uwe Semmelmann. *Scalar curvature estimates for compact symmetric spaces.* Differential Geometry and its Applications 16 (2002), 65–78. [DOI](https://doi.org/10.1016/s0926-2245(01)00068-7)
- **[SOTA / Recent]** Simon Brendle, Sven Hirsch, Florian Johne. *A generalization of Geroch's conjecture.* Communications on Pure and Applied Mathematics 77 (2024), 441–456.
- **[SOTA / Recent]** Simon Brendle. *Scalar curvature rigidity of convex polytopes.* Inventiones Mathematicae 235 (2024), 669–708. [DOI](https://doi.org/10.1007/s00222-023-01229-x)
- **[SOTA / Recent]** Simone Cecchini, Rudolf Zeidler. *Scalar and mean curvature comparison via the Dirac operator.* Geometry & Topology 28 (2024), 1167–1212. [DOI](https://doi.org/10.2140/gt.2024.28.1167)
- **[SOTA / Recent]** Jinmin Wang, Zhizhang Xie, Guoliang Yu. *On Gromov's dihedral extremality and rigidity conjectures.* Preprint, arXiv:2112.01510, 2021.
- **[SOTA / Recent]** Richard Schoen, Shing-Tung Yau. *Positive scalar curvature and minimal hypersurface singularities.* Preprint, arXiv:1704.05490, 2017.
- **[Survey]** Mikhael Gromov. *Four Lectures on Scalar Curvature.* In: Perspectives in Scalar Curvature, Vol. 1, World Scientific, 2023; preprint arXiv:1908.10612. [DOI](https://doi.org/10.1142/9789811273223_0001)
- **[Survey]** Simon Brendle. *Rigidity phenomena involving scalar curvature.* Surveys in Differential Geometry 17 (2012), 179–202. [DOI](https://doi.org/10.4310/sdg.2012.v17.n1.a4)

## 10. Worked Example / Concrete Special Case

**(a) The rescaled sphere — sharpness check.** Let $g=r^2 g_0$ on $S^n$ and $f=\mathrm{id}$. Then every singular value is $\lambda_i=1/r$, so $f$ is $1$-Lipschitz iff $r\ge 1$; and $\mathrm{Scal}_g=n(n-1)/r^2\ge n(n-1)$ iff $r\le1$. The two hypotheses meet only at $r=1$. This shows the constant $n(n-1)$ cannot be improved and that the two conditions pull in opposite directions — the content of the theorem is that no non-round metric can evade the collision.

**(b) Full proof in dimension 2.** Let $(S^2,g)$ have Gauss curvature $K\ge1$ (i.e. $\mathrm{Scal}=2K\ge2=n(n-1)$), and let $f:(S^2,g)\to(S^2,g_0)$ be area non-increasing with $\deg f=d\neq 0$.

*Step 1 (degree bounds area).* Since $|\det df|\le1$ pointwise,
$$4\pi|d|=\Big|\int_{S^2} f^*\,dA_{g_0}\Big|\le\int_{S^2}|\det df|\,dA_g\le \mathrm{Area}(S^2,g).$$

*Step 2 (Gauss–Bonnet caps area).* $\displaystyle \int_{S^2}K\,dA_g=2\pi\chi(S^2)=4\pi$, and $K\ge1$ gives
$$\mathrm{Area}(S^2,g)\le\int_{S^2}K\,dA_g=4\pi.$$

*Step 3 (squeeze).* Combining, $4\pi|d|\le \mathrm{Area}(S^2,g)\le4\pi$, so $|d|=1$ and $\mathrm{Area}(S^2,g)=4\pi$.

*Step 4 (equality analysis).* Equality in Step 2 forces $K\equiv1$, hence $g=g_0$ up to isometry. Equality in Step 1 forces $|\det df|\equiv1$, so $f$ is a local diffeomorphism preserving area; on a closed surface with $|d|=1$ it is a diffeomorphism, and an area-preserving $1$-area-non-increasing map between unit spheres has $\lambda_1\lambda_2=1$ with $\lambda_1\lambda_2\le1$ attained everywhere, forcing $\lambda_1=\lambda_2=1$. Hence $f$ is an isometry. $\square$

This is the Llarull conclusion with the Dirac machinery replaced by Gauss–Bonnet. In dimension $\ge3$ no such topological integral formula for $\mathrm{Scal}$ exists — $\int\mathrm{Scal}\,dV$ is not a topological invariant — which is precisely why the index-theoretic (or slicing) argument is needed, and why the non-spin case is hard.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*