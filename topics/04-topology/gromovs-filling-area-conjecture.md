---
id: 04-topology/gromovs-filling-area-conjecture
title: "Gromov's Filling Area Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gromov's Filling Area Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/gromovs-filling-area-conjecture` · **Status:** solved-recently

**Status note.** The catalog status records recent *resolution of the main sub-cases* — genus $0$ (Gromov, 1983), genus $1$ and all hyperelliptic fillings (Bangert–Croke–Ivanov–Katz, 2005), the Möbius band (equivalent to Pu's inequality), and the Finsler disc with Holmes–Thompson area (Ivanov, 2011). The conjecture in full generality, over fillings of arbitrary genus, is **open**.

## 1. Problem Statement / Conjecture

Let $S^1_{2\pi}$ denote the circle of total length $2\pi$ with its intrinsic (arclength) metric, so that $d_{S^1}(x,y)\le\pi$ for all $x,y$.

A compact Riemannian surface $(M,g)$ with $\partial M \cong S^1$ is an **isometric filling** of $S^1_{2\pi}$ if the boundary, with the metric induced by the *ambient* distance of $M$, is isometric to $S^1_{2\pi}$:
$$d_M(x,y) \;=\; d_{S^1}(x,y)\qquad \text{for all } x,y\in\partial M .$$
Note this is a strong condition: no shortcut through the interior is allowed.

**Conjecture (Gromov, 1983).** Every orientable isometric filling $(M,g)$ of $S^1_{2\pi}$ satisfies
$$\operatorname{area}(M,g)\;\ge\;2\pi,$$
with equality for the round hemisphere $S^2_+ \subset S^2(1)$.

Equivalently, $\operatorname{FillArea}(S^1_{2\pi}) = 2\pi$, where the filling area is the infimum of areas over all such fillings. A complete proof must handle fillings of **every genus** $h\ge 0$ and every smooth (or Lipschitz) metric; a disproof requires an orientable filling of area $<2\pi$.

## 2. Mathematical Foundations

**Filling volume.** For a closed $n$-manifold $(N,d)$, Gromov defines
$$\operatorname{FillVol}(N,d)=\inf\{\operatorname{vol}(M,g)\;:\;\partial M=N,\ d_M|_{N\times N}=d\},$$
the infimum over compact $(n{+}1)$-manifolds $M$ filling $N$ isometrically. Gromov proved $\operatorname{FillVol}$ is finite and, via the Kuratowski embedding $N\hookrightarrow L^\infty(N)$, that it can be computed by fillings inside $L^\infty(N)$. The conjecture is the single unresolved sharp value in the lowest nontrivial case $N=S^1$.

**Filling radius.** $\operatorname{FillRad}(N)=\inf\{\varepsilon: N \text{ bounds in its } \varepsilon\text{-neighbourhood in } L^\infty(N)\}$; for $S^1_{2\pi}$, $\operatorname{FillRad}=\pi/3$. Gromov's chain of inequalities
$$\operatorname{sys}_1 \;\le\; C_n \operatorname{FillRad} \;\le\; C_n' \operatorname{vol}^{1/n}$$
places the problem at the origin of systolic geometry.

**The extremal candidate.** On the unit hemisphere, boundary points at equator-arclength $s\le\pi$ are joined by the equatorial great-circle arc, which is a minimizing geodesic of $S^2_+$; hence $d_{S^2_+}=d_{S^1}$ on the equator and $\operatorname{area}(S^2_+)=2\pi$.

**Pu's inequality (1952).** Every Riemannian metric $g$ on $\mathbb{RP}^2$ satisfies
$$\operatorname{sys}(g)^2 \;\le\; \frac{\pi}{2}\,\operatorname{area}(g),$$
with equality exactly for constant curvature. Doubling a Möbius-band filling along its boundary and quotienting produces a metric on $\mathbb{RP}^2$; this makes the nonorientable genus-$1$ case of the filling problem equivalent to Pu.

**Finsler version.** For a Finsler metric $F$ on $M$, the **Holmes–Thompson area** is
$$\operatorname{area}_{HT}(M,F)=\frac{1}{\pi}\operatorname{vol}\big(\{(x,p)\in T^*M: F^*_x(p)\le 1\}\big),$$
normalized so that Riemannian metrics recover the usual area. Gromov's conjecture has a Finsler analogue with the same constant $2\pi$.

## 3. History & State of the Art (SOTA)

- **1952.** Besicovitch proves the "two problems of Loewner" lemma: a Riemannian metric on the square $[0,1]^2$ in which opposite sides are at distance $\ge 1$ has area $\ge 1$. Pu proves the $\mathbb{RP}^2$ systolic inequality the same year. These are the two seeds of the subject.
- **1983.** Gromov, *Filling Riemannian manifolds* (J. Differential Geom. 18, 1–147), introduces filling volume, filling radius, and states the Filling Area Conjecture. In the same paper he settles the **genus-$0$** case (fillings by a disc) and observes the equivalence of the Möbius-band case with Pu's inequality.
- **2001.** S. Ivanov gives a new, more conceptual proof of the disc case by a convexity/geodesic-flow argument that generalizes beyond the Riemannian setting.
- **2005.** Bangert, Croke, Ivanov and Katz prove the conjecture for **genus-$1$ orientable fillings**, by reducing to *ovalless real hyperelliptic surfaces* and applying a Pu-type argument to the quotient. Their method covers hyperelliptic fillings of any genus.
- **2011.** Ivanov proves the **Finsler disc** case with Holmes–Thompson area, and (with Burago) develops the minimality of flat/projective Finsler metrics that underlies it.
- **2018–2022.** Cossarini's discretization of surface metrics ("square-celled surfaces", weighted curve systems) and Cossarini–Sabourau's work on minimal-area Finsler discs whose geodesics are minimizing recast the problem as an integral-geometric / combinatorial optimization. *(frontier — verify)*

No counterexample of any genus is known; no filling of area $<2\pi$ has been produced even numerically.

## 4. Partial Results / Verified Cases

| Class of filling | Result | Source |
|---|---|---|
| Genus $0$ (disc), Riemannian | $\operatorname{area}\ge 2\pi$, sharp | Gromov 1983 |
| Genus $1$, orientable, Riemannian | $\operatorname{area}\ge 2\pi$, sharp | BCIK 2005 |
| Hyperelliptic fillings, any genus $h\ge 1$ | $\operatorname{area}\ge 2\pi$ | BCIK 2005 |
| Möbius band (nonorientable, genus 1) | equivalent to Pu; holds | Pu 1952 / Gromov 1983 |
| Finsler disc, Holmes–Thompson area | $\operatorname{area}_{HT}\ge 2\pi$ | Ivanov 2011 |
| Fillings by a disc in $L^\infty(S^1)$ | attained; hemisphere extremal | Gromov 1983 |
| Finsler discs all of whose geodesics minimize | sharp bound via integral geometry | Cossarini–Sabourau *(frontier — verify)* |

The equality case is rigid: in genus $\le 1$, area $=2\pi$ forces isometry with the round hemisphere.

## 5. Principal Obstacles

- **Topology is unbounded.** The genus $h$ of the filling is not constrained by the boundary. Every proof to date fixes a topological type and exploits it; there is no argument uniform in $h$. A priori a very high-genus surface could be "efficient" at realizing the required boundary distances with little area.
- **Hyperellipticity fails for $h\ge 2$.** The BCIK proof passes to a $\mathbb{Z}/2$ quotient and applies a Pu/Loewner-type inequality there. For $h\ge 3$ the generic Riemann surface is not hyperelliptic, so the involution needed to build the quotient simply does not exist.
- **No conformal handle.** Loewner- and Pu-type inequalities come from uniformization plus averaging over a conformal group action; the boundary-distance constraint is not conformally natural, and for higher genus the Jacobian/Abel–Jacobi machinery (Gromov's stable systolic inequalities) loses sharpness by uncontrolled constants.
- **Non-locality of the constraint.** $d_M(x,y)=d_{S^1}(x,y)$ is a statement about *global* minimizers, not a pointwise curvature or first-order condition. Calculus-of-variations arguments have no usable Euler–Lagrange equation; the constraint set is not smooth.
- **Compactness failure.** Minimizing sequences of metrics can degenerate (long thin tubes, collapsing handles). Gromov–Hausdorff limits leave the category of Riemannian surfaces, and the limit object's "area" is not automatically lower semicontinuous in a usable way.
- **Besicovitch-type cutting is lossy.** Cutting a high-genus filling into discs to apply Besicovitch's lemma destroys the distance condition on the cuts; the recovered constant is strictly below $2\pi$.

## 6. The Gap

Proven: $\operatorname{area}\ge 2\pi$ for genus $0$, genus $1$, and hyperelliptic fillings of any genus; and for Finsler discs. Conjectured: the same bound for **orientable fillings of genus $h\ge 2$ that admit no hyperelliptic involution**.

The precise missing step is a genus-independent mechanism converting the boundary condition $d_M|_{\partial M}=d_{S^1}$ into an area lower bound. Concretely, one needs either

1. a *reduction* showing any minimizing filling may be taken of genus $\le 1$ (or hyperelliptic) — i.e. that handles never help; or
2. an *integral-geometric identity* (a Crofton-type formula) bounding area below by the total length of a family of boundary-to-boundary minimizing geodesics, valid for all topologies.

Even a proof of $\operatorname{area}\ge 2\pi - \varepsilon$ uniform in genus, for some explicit $\varepsilon>0$, would be a major advance; currently no unconditional bound close to $2\pi$ is known for unrestricted genus.

## 7. Current Research (as of June 2026)

- **Integral geometry / Finsler route.** The Finsler formulation with Holmes–Thompson area is more flexible than the Riemannian one: Crofton formulas convert area into a measure on the space of geodesics. Ivanov's disc theorem is proved this way, and the programme is to extend it to positive genus. Groups at St. Petersburg (Ivanov), Paris-Est/Créteil (Sabourau), and Bar-Ilan (Katz) drive this line.
- **Discretization.** Cossarini's square-celled surfaces reduce filling area to a combinatorial minimization over weighted curve systems, making finite-genus cases computer-checkable in principle. *(frontier — verify)*
- **Minimal surfaces / calibration.** Attempts to calibrate the hemisphere by a differential form pulled back from $L^\infty(S^1)$, in the spirit of Burago–Ivanov's proof of minimality of flat metrics in the class of Finsler metrics.
- **Metric-geometry limits.** Sormani-style intrinsic-flat convergence is used to control degenerating minimizing sequences and to make "the infimum is attained" precise in a weak category. *(frontier — verify)*
- **Systolic side.** Sharper stable systolic and Loewner-type inequalities on higher-genus surfaces (Katz–Sabourau and successors) feed back into the higher-genus filling problem.

## 8. Future Work

- Prove a **handle-reduction theorem**: show that surgery on a handle of a filling does not increase area while preserving the boundary distance condition. This would collapse the general case to genus $\le 1$.
- Settle **genus $2$**, where all Riemann surfaces *are* hyperelliptic as conformal structures but the BCIK argument requires compatibility with the metric and the boundary — the first genuinely new case.
- Establish a **Crofton inequality for Finsler surfaces of positive genus** with the sharp constant $\pi$, which would give the Finsler (hence Riemannian) conjecture in full.
- Resolve the **Finsler nonorientable case**, where it is expected that the constant differs from $2\pi$; understanding this asymmetry would clarify what orientability contributes.
- Determine $\operatorname{FillVol}(S^n_{\mathrm{can}})$ for $n\ge 2$ — even the conjectural extremal (the hemisphere $S^{n+1}_+$) is unproven and the value is unknown.

## 9. Key References

- **[Foundational]** M. Gromov. *Filling Riemannian manifolds.* Journal of Differential Geometry, 18(1):1–147, 1983. [DOI](https://doi.org/10.4310/jdg/1214509283)
- **[Foundational]** P. M. Pu. *Some inequalities in certain nonholonomic systems.* Pacific Journal of Mathematics, 2(1):55–71, 1952.
- **[Foundational]** A. S. Besicovitch. *On two problems of Loewner.* Journal of the London Mathematical Society, 27:141–144, 1952. [DOI](https://doi.org/10.1112/jlms/s1-27.2.141)
- **[SOTA]** V. Bangert, C. Croke, S. Ivanov, M. Katz. *Filling area conjecture and ovalless real hyperelliptic surfaces.* Geometric and Functional Analysis (GAFA), 15(3):577–597, 2005. [DOI](https://doi.org/10.1007/s00039-005-0517-8)
- **[SOTA]** S. Ivanov. *Filling minimality of Finslerian 2-discs.* Proceedings of the Steklov Institute of Mathematics, 273:176–190, 2011. [DOI](https://doi.org/10.1134/s0081543811040079)
- **[SOTA]** V. Bangert, C. Croke, S. Ivanov, M. Katz. *Boundary case of equality in optimal Loewner-type inequalities.* Transactions of the American Mathematical Society, 359(1):1–17, 2007. [DOI](https://doi.org/10.1090/s0002-9947-06-03836-0)
- **[Related]** D. Burago, S. Ivanov. *Riemannian tori without conjugate points are flat.* Geometric and Functional Analysis, 4(3):259–269, 1994. [DOI](https://doi.org/10.1007/bf01896241)
- **[Survey]** M. Katz. *Systolic Geometry and Topology.* Mathematical Surveys and Monographs 137, American Mathematical Society, 2007.
- **[Survey]** C. Croke, M. Katz. *Universal volume bounds in Riemannian manifolds.* Surveys in Differential Geometry VIII, International Press, 2003, pp. 109–137. [DOI](https://doi.org/10.4310/sdg.2003.v8.n1.a4)
- **[Survey]** M. Gromov. *Systoles and intersystolic inequalities.* Actes de la Table Ronde de Géométrie Différentielle (Luminy, 1992), Séminaires et Congrès 1, Société Mathématique de France, 1996, pp. 291–362.

## 10. Worked Example / Concrete Special Case

**Round spherical caps: only the hemisphere qualifies.**

Take the sphere $S^2(R)$ of radius $R$ and the cap $C_{R,\theta}$ of colatitude $\theta\in(0,\pi)$ about the north pole. Its boundary circle has length $2\pi R\sin\theta$; requiring this to equal $2\pi$ forces
$$R\sin\theta = 1 \quad\Longrightarrow\quad R\ge 1 .$$

*Area.* $\operatorname{area}(C_{R,\theta}) = 2\pi R^2(1-\cos\theta)$.

*Boundary distances.* Two boundary points separated by longitude angle $\varphi\in[0,\pi]$ are at boundary arclength $s = R\varphi\sin\theta = \varphi$. Their intrinsic distance in the cap is realized by the great-circle arc $R\gamma$, where the spherical law of cosines gives
$$\sin\tfrac{\gamma}{2} = \sin\theta\,\sin\tfrac{\varphi}{2}.$$
So the filling condition $R\gamma = \varphi$ reads
$$\sin\!\Big(\frac{\varphi}{2R}\Big) = \frac{1}{R}\,\sin\frac{\varphi}{2}\qquad\text{for all }\varphi\in[0,\pi].$$
For $R>1$ the left side is $\frac{\varphi}{2R}-\frac{\varphi^3}{48R^3}+\cdots$ and the right is $\frac{\varphi}{2R}-\frac{\varphi^3}{48R}+\cdots$; the cubic terms differ, and $R\gamma<\varphi$ strictly. So **every cap with $R>1$ takes a shortcut through the interior and is not an isometric filling.** Only $R=1$, $\theta=\pi/2$ survives:
$$\operatorname{area}(C_{1,\pi/2}) = 2\pi\cdot 1^2\cdot(1-0) = 2\pi .$$

*Why the constraint is essential.* The flat disc bounded by a circle of circumference $2\pi$ has radius $1$ and area $\pi<2\pi$ — but antipodal boundary points sit at distance $2$, not $\pi$. Likewise, letting $R\to\infty$ above gives
$$2\pi R^2\Big(1-\sqrt{1-R^{-2}}\Big)\;\longrightarrow\;\pi,$$
the flat disc again, along a family of *non*-fillings. The conjecture asserts that no genuine isometric filling — of any genus — can reach down toward $\pi$; $2\pi$ is the floor.

*Nonorientable check.* Double a Möbius-band filling $M$ across $\partial M$ and quotient by the deck involution: one obtains a metric on $\mathbb{RP}^2$ with systole $\ge\pi$ and area $2\operatorname{area}(M)$. Pu's inequality $\operatorname{sys}^2\le\frac{\pi}{2}\operatorname{area}$ then gives $\pi^2 \le \frac{\pi}{2}\cdot 2\operatorname{area}(M)$, i.e. $\operatorname{area}(M)\ge\pi$ — the sharp Möbius-band bound, attained by the hemisphere's antipodal-quotient model.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*