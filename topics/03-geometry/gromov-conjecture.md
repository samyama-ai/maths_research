---
id: 03-geometry/gromov-conjecture
title: "Gromov Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gromov Conjecture (Filling Area Conjecture)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/gromov-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Gromov's **Filling Area Conjecture** (FAC), posed in *Filling Riemannian manifolds* (1983), asserts that the round hemisphere is the least-area orientable filling of a circle.

Let $C_L$ be the circle of total length $L$ with its intrinsic (arclength) metric. A **filling** of $C_L$ is a compact orientable surface $M$ with $\partial M \cong C_L$, carrying a Riemannian metric such that the induced intrinsic distance on $M$ restricted to the boundary is **at least** the circle distance:
$$d_M(x,y)\;\ge\;d_{C_L}(x,y)\qquad \forall\, x,y\in\partial M .$$
(Since a path along $\partial M$ realizes $d_{C_L}$, this forces equality: the boundary is isometrically embedded.)

**Conjecture (Gromov, 1983).** For every orientable filling $M$ of $C_L$, of any genus $g \ge 0$,
$$\operatorname{Area}(M)\;\ge\;\frac{L^{2}}{2\pi},$$
with equality for the round hemisphere of radius $L/2\pi$.

A proof must handle **all genera simultaneously**; a disproof requires a single orientable filling with $\operatorname{Area} < L^2/2\pi$. Orientability is essential: the Möbius band admits fillings of area $< L^2/2\pi$ (the projective plane minus a small disc), so the nonorientable statement is false. Normalizing $L = 2\pi$, the claim is $\operatorname{Area}(M) \ge 2\pi$.

*(Note: "Gromov conjecture" also labels his Betti-number and scalar-curvature conjectures; this page treats the filling area statement, the one canonically attached to the name in metric geometry.)*

## 2. Mathematical Foundations

**Filling volume.** For a closed Riemannian manifold $(N^n, g)$ with induced distance $d_N$, Gromov defines
$$\operatorname{FillVol}(N^n,g)\;=\;\inf\Big\{\operatorname{Vol}(M^{n+1},h)\;:\;\partial M = N,\;\; d_M\big|_{N\times N}\ \ge\ d_N\Big\}.$$
The FAC is the assertion
$$\operatorname{FillVol}(S^1, \text{can}_{L})\;=\;\frac{L^2}{2\pi},$$
restricted to **orientable** $M$. Gromov proved that the infimum may be taken over surfaces with $M$ homeomorphic to a fixed topological type only after bounding genus, which is exactly where the difficulty lies.

**Pu's inequality (1952).** For every Riemannian metric $g$ on the real projective plane $\mathbb{RP}^2$,
$$\operatorname{Area}(g)\;\ge\;\frac{2}{\pi}\,\operatorname{sys}(g)^2,$$
where $\operatorname{sys}(g)$ is the least length of a noncontractible loop; equality holds precisely for metrics of constant curvature. For the round $\mathbb{RP}^2$ of curvature $1$: $\operatorname{sys}=\pi$, $\operatorname{Area}=2\pi=\frac{2}{\pi}\pi^2$.

**Filling radius.** $\operatorname{FillRad}(N)$ is the smallest $r$ such that the Kuratowski embedding $N \hookrightarrow L^\infty(N)$, $x \mapsto d_N(x,\cdot)$, bounds in its $r$-neighbourhood. Gromov's chain of inequalities $\operatorname{sys} \le 6\operatorname{FillRad}$, $\operatorname{FillRad}^n \lesssim_n \operatorname{FillVol}$ ties FAC to the systolic universe, but with non-sharp constants.

**Finsler variant.** Replacing Riemannian area by the **Holmes–Thompson area** $\operatorname{area}_{HT}(M)=\frac{1}{\pi}\operatorname{vol}(B^*M)$ (symplectic volume of the unit codisc bundle) gives the Finsler FAC, with the same conjectural constant $\frac{1}{2\pi}$; it implies the Riemannian statement is at least consistent with a larger competitor class.

## 3. History & State of the Art (SOTA)

- **1952.** P. M. Pu proves the sharp systolic inequality for $\mathbb{RP}^2$ (Pacific J. Math.), later recognized as the genus-$0$ case of FAC.
- **1983.** Gromov, *Filling Riemannian manifolds* (J. Differential Geom. **18**, 1–147), introduces filling radius, filling volume, and states the FAC. He proves it for genus $0$ (via Pu) and establishes non-sharp bounds $\operatorname{Area} \ge c\,L^2$ with $c>0$ for arbitrary genus, plus $\operatorname{FillVol}(S^n)\ge c_n$ in all dimensions.
- **1991.** Croke proves boundary-rigidity results for simple metrics on discs (J. Differential Geom. **33**), the "local" cousin of the filling problem.
- **2005.** Bangert, Croke, Ivanov, Katz settle **genus 1** (GAFA **15**, 577–597), by relating hyperelliptic fillings to ovalless real hyperelliptic surfaces and reducing to Pu's inequality on the quotient.
- **2010.** Burago–Ivanov prove filling-volume minimality of metrics $C^2$-close to flat (Ann. of Math. **171**), giving a genuinely higher-dimensional, local version.
- **2011.** Ivanov proves the **Finsler** filling-minimality of the 2-disc with Holmes–Thompson area.
- **2018–2023.** Cossarini's discretization (square-celled surfaces) and Cossarini–Sabourau's theorem on Finsler discs with minimizing geodesics (JEMS) push the combinatorial/integral-geometric approach.

No counterexample or improvement to the sharp constant in higher genus has appeared in over forty years.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| Genus $0$ (disc fillings), Riemannian | **Proved**, sharp | Gromov 1983 via Pu 1952 |
| Genus $1$, orientable | **Proved**, sharp | Bangert–Croke–Ivanov–Katz 2005 |
| Genus $\ge 2$ | **Open** | — |
| Hyperelliptic fillings (via quotient argument) | Proved in the cases where the involution descends as in genus 1 | BCIK 2005 |
| Finsler, genus $0$, Holmes–Thompson area | **Proved**, sharp constant $\tfrac{1}{2\pi}$ | Ivanov 2011 (also Ivanov 2001) |
| Finsler discs all of whose geodesics are minimizing | **Proved** | Cossarini–Sabourau, JEMS 2023 |
| Metrics $C^2$-close to a flat metric on $D^n$, $n\ge 2$ | **Proved** (filling minimality + boundary rigidity) | Burago–Ivanov 2010 |
| Simple metrics on $D^2$ (boundary rigidity) | **Proved** | Pestov–Uhlmann 2005 |
| Arbitrary genus, non-sharp constant $\operatorname{Area}\ge cL^2$ | **Proved** for some $c < \tfrac{1}{2\pi}$ | Gromov 1983 |
| Nonorientable fillings with the same constant | **False** | Möbius band in $\mathbb{RP}^2$ |

## 5. Principal Obstacles

- **No genus control.** Cutting a high-genus filling along short curves to reduce genus does not preserve the boundary distance condition: surgery can create shortcuts $d_M(x,y) < d_{C_L}(x,y)$. Every known sharp argument (Pu, BCIK) uses a global conformal/involutive structure that exists only for $g \le 1$.
- **Conformal methods stall.** Pu's proof integrates over the $\mathrm{SO}(3)$-orbit of a conformal uniformization of $\mathbb{RP}^2$ and uses Cauchy–Schwarz. For $g\ge 2$ the uniformizing hyperbolic metric has no transitive symmetry group to average over, so the averaging step that produces the constant $2/\pi$ has no analogue.
- **Minimizers may not exist or may be singular.** The infimum in $\operatorname{FillVol}$ is over a non-compact class of metrics; limits are only length spaces, not Riemannian surfaces. Geometric measure theory gives compactness for integral currents in $L^\infty$, but the boundary-distance constraint is not a mass-minimization constraint, so regularity theory does not apply directly.
- **Coarse tools lose the constant.** Filling radius, isoperimetric-type inequalities, and Besicovitch/cube-slicing arguments all produce inequalities of the form $\operatorname{Area}\ge cL^2$ with $c$ far below $1/(2\pi)\approx 0.1592$; each step (co-area, covering, Vitali) is lossy by a definite factor.
- **Non-positivity of the functional.** The problem is a min–max over pairs of boundary points, so the constraint set $\{d_M \ge d_{C_L}\}$ is defined by uncountably many nonsmooth inequalities; first-variation calculus at a candidate minimizer produces measures supported on geodesic families rather than a PDE.

## 6. The Gap

Proven: $g=0$ and $g=1$ with the sharp constant; all $g$ with a non-sharp constant. Conjectured: all $g\ge 2$ with constant $\frac{1}{2\pi}$.

The precise missing step is a mechanism converting a **genus-$g$ orientable filling** into either (i) a metric on $\mathbb{RP}^2$ with systole $\ge L/2$ and no area loss (the genus-$\le 1$ route: glue antipodal boundary points, use Pu), or (ii) a filling of smaller genus with area not larger. For $g\ge 2$, the antipodal gluing of $M$ produces a closed nonorientable surface of higher genus where the sharp Pu constant fails — the systolic ratio of $\mathbb{RP}^2$ is not attained on higher-genus nonorientable surfaces, and their optimal systolic constants are themselves unknown. Equivalently: **FAC in genus $g$ is at least as hard as a sharp systolic inequality on a nonorientable surface of genus $2g+1$**, which is open for every $g \ge 2$.

## 7. Current Research (as of June 2026)

- **Discretization.** Cossarini's *square-celled surfaces* encode Finsler metrics with a combinatorial "curve-crossing" area, turning FAC into a statement about minimal-area filling of a cyclic word by a surface of curves. Active at Université Paris-Est Créteil / IMPA circles. *(frontier — verify current status of the genus-$\ge2$ discrete case.)*
- **Integral geometry / symplectic methods.** Ivanov and Burago's technique — comparing $\operatorname{vol}(B^*M)$ against a calibration built from the geodesic flow — is the only method that has yielded sharp constants outside genus $\le 1$; extending the calibration past the "minimizing geodesics" hypothesis of Cossarini–Sabourau is the main technical target.
- **Boundary rigidity in higher dimensions.** Stefanov–Uhlmann–Vasy's local and global boundary rigidity results for foliated manifolds (Ann. of Math., 2021) feed the higher-dimensional filling volume programme; whether $\operatorname{FillVol}(S^n)=\tfrac12\operatorname{Vol}(S^{n+1})$ remains open for $n\ge 2$.
- **Systolic geometry of nonorientable surfaces.** Sharp systolic constants for $N_k$, $k\ge 3$, studied by Katz–Sabourau and successors, are the direct obstruction identified in §6.

## 8. Future Work

- Prove the Finsler FAC for discs *without* the minimizing-geodesic hypothesis; by Ivanov's framework this would then be attacked genus-by-genus with the same calibration.
- Establish a **genus-reduction lemma**: any orientable filling of $C_L$ of genus $g\ge 1$ admits a genus-$(g-1)$ filling of no greater area. Gromov has repeatedly flagged this as the natural but elusive statement.
- Develop compactness for the filling class in the Gromov–Hausdorff / intrinsic flat topology (Sormani–Wenger currents) and prove regularity of the limit, so that a variational argument becomes admissible.
- Settle the higher-dimensional filling volume of $S^n$, or find a counterexample; a failure in high dimension would sharply constrain what proof techniques can work in dimension 2.
- Search computationally for low-area high-genus fillings using discrete (square-celled or PL) models — a numerical counterexample would settle the conjecture negatively.

## 9. Key References

- **[Foundational]** M. Gromov. *Filling Riemannian manifolds.* Journal of Differential Geometry **18** (1983), 1–147. [DOI](https://doi.org/10.4310/jdg/1214509283)
- **[Foundational]** P. M. Pu. *Some inequalities in certain nonorientable Riemannian manifolds.* Pacific Journal of Mathematics **2** (1952), 55–71. [DOI](https://doi.org/10.2140/pjm.1952.2.55)
- **[SOTA]** V. Bangert, C. Croke, S. Ivanov, M. Katz. *Filling area conjecture and ovalless real hyperelliptic surfaces.* Geometric and Functional Analysis (GAFA) **15** (2005), 577–597. [DOI](https://doi.org/10.1007/s00039-005-0517-8)
- **[SOTA]** S. Ivanov. *Filling minimality of Finslerian 2-discs.* Proceedings of the Steklov Institute of Mathematics **273** (2011), 176–190. [DOI](https://doi.org/10.1134/s0081543811040079)
- **[SOTA]** D. Burago, S. Ivanov. *Boundary rigidity and filling volume minimality of metrics close to a flat one.* Annals of Mathematics **171** (2010), 1183–1211. [DOI](https://doi.org/10.4007/annals.2010.171.1183)
- **[SOTA / Recent]** M. Cossarini, S. Sabourau. *Minimal area of Finsler disks with minimizing geodesics.* Journal of the European Mathematical Society, 2023. [DOI](https://doi.org/10.4171/jems/1339)
- **[Related]** C. Croke. *Rigidity and the distance between boundary points.* Journal of Differential Geometry **33** (1991), 445–464. [DOI](https://doi.org/10.4310/jdg/1214446326)
- **[Related]** P. Stefanov, G. Uhlmann, A. Vasy. *Local and global boundary rigidity and the geodesic X-ray transform in the normal gauge.* Annals of Mathematics **194** (2021), 1–95. [DOI](https://doi.org/10.4007/annals.2021.194.1.1)
- **[Survey]** M. Katz. *Systolic Geometry and Topology.* Mathematical Surveys and Monographs **137**, American Mathematical Society, 2007.
- **[Survey]** M. Gromov. *Metric Structures for Riemannian and Non-Riemannian Spaces.* Birkhäuser, 2007 (with appendices by M. Katz, P. Pansu, S. Semmes). [DOI](https://doi.org/10.1007/978-0-8176-4583-0)
- **[Survey]** L. Guth. *Notes on Gromov's systolic estimate.* Geometriae Dedicata **123** (2006), 113–129. [DOI](https://doi.org/10.1007/s10711-006-9111-y)

## 10. Worked Example / Concrete Special Case

**Normalize $L = 2\pi$.** The model filling is the unit hemisphere $H \subset S^2$: $\partial H$ is the equator of length $2\pi$, $\operatorname{Area}(H)=2\pi$, and antipodal equator points satisfy $d_H(x,-x)=\pi = d_{C_{2\pi}}(x,-x)$ — the boundary is isometrically embedded.

**Why the flat disc is not a competitor.** The Euclidean disc $D$ of radius $1$ has $\partial D$ of length $2\pi$ and area $\pi < 2\pi$, but for antipodal boundary points $d_D(x,-x)=2 < \pi$. The constraint $d_M \ge d_{C_L}$ fails, so $D$ is not a filling. This is the entire content of the conjecture: shortcutting through the interior is forbidden.

**Proof of the genus-0 case.** Let $M$ be a filling disc of $C_{2\pi}$. Glue each boundary point $x$ to its antipode $-x$ (the point at circle-distance $\pi$). The quotient $\bar M = M/\!\sim$ is a closed surface with
$$\chi(\bar M) = \chi(M) - \tfrac12\chi(S^1)\cdot 0 = 1 - 1 = 0 \quad\text{(cells: } \bar M \cong \mathbb{RP}^2\text{)},$$
concretely: a disc with antipodal boundary identification is $\mathbb{RP}^2$. Give $\bar M$ the quotient length metric.

*Systole bound.* Let $\gamma$ be a noncontractible loop in $\bar M$. Its lift to $M$ is a path from some $x \in \partial M$ to $-x$, so
$$\operatorname{length}(\gamma)\;\ge\;d_M(x,-x)\;\ge\;d_{C_{2\pi}}(x,-x)\;=\;\pi .$$
Hence $\operatorname{sys}(\bar M) \ge \pi$.

*Apply Pu.* $\operatorname{Area}(M) = \operatorname{Area}(\bar M) \ge \frac{2}{\pi}\operatorname{sys}(\bar M)^2 \ge \frac{2}{\pi}\pi^2 = 2\pi = \frac{L^2}{2\pi}.$

Equality forces equality in Pu, i.e. $\bar M$ has constant curvature $1$, so $M$ is the round hemisphere. **For genus $g \ge 1$ the same gluing yields a nonorientable surface of genus $2g+1$, where no sharp systolic inequality of Pu type is known** — this is precisely the gap of §6, closed only for $g=1$ by the hyperelliptic argument of Bangert–Croke–Ivanov–Katz.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*