---
id: 06-pdes/chern-ricci-flow-singularities
title: "Chern Ricci Flow Singularities"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chern-Ricci Flow Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/chern-ricci-flow-singularities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Chern-Ricci flow is the parabolic evolution of a Hermitian metric on a compact complex manifold by its Chern-Ricci form,
$$\frac{\partial}{\partial t}\omega(t) = -\mathrm{Ric}(\omega(t)), \qquad \omega(0)=\omega_0 ,$$
where $\mathrm{Ric}(\omega) = -\sqrt{-1}\,\partial\bar\partial \log\det g$ is the curvature of the Chern connection on $K_M^{-1}$. On Kähler manifolds this is exactly the Kähler-Ricci flow; on non-Kähler manifolds it is a genuinely different flow, and it is defined on every compact complex manifold.

**The problem.** Classify the finite-time singularities of the Chern-Ricci flow and determine whether they realize a *non-Kähler minimal model program*. Concretely, the following are open in general.

- **(A) Geometric classification (Tosatti-Weinkove).** Let $M$ be a compact complex surface with maximal existence time $T<\infty$. If the volume does not go to zero, then $M$ contains either a $(-1)$-curve or a global spherical shell; $(M,\omega(t))$ converges in Gromov-Hausdorff distance as $t\to T$ to a compact metric space obtained by contracting finitely many curves, and the flow continues past $T$ on the contracted space (as a metric/weak solution). If the volume does go to zero, the flow collapses $M$ onto a lower-dimensional canonical model determined by the Kodaira dimension.
- **(B) Curvature blow-up.** At every finite-time singularity, $\displaystyle \limsup_{t\to T}\ \sup_M |\mathrm{Rm}(\omega(t))|_{\omega(t)}\,(T-t) \ge c>0$; more sharply, the Chern scalar curvature $s=\mathrm{tr}_\omega \mathrm{Ric}(\omega)$ is unbounded as $t\to T$.
- **(C) Higher dimensions.** Extend (A) to $\dim_{\mathbb C} M = n \ge 3$, where no classification of complex manifolds is available.

A complete solution of (A) requires, for each compact complex surface and each initial Hermitian metric, an identification of the limit space, the singularity model, and a canonical continuation. A disproof would exhibit a surface and a metric whose singularity is not modeled on a holomorphic contraction.

## 2. Mathematical Foundations

Let $(M^n,J)$ be a compact complex manifold and $\omega = \sqrt{-1}\, g_{i\bar j}\, dz^i\wedge d\bar z^j$ a Hermitian metric ($\omega$ positive, not necessarily $d$-closed). The **Chern connection** is the unique connection on $T^{1,0}M$ compatible with $g$ and $J$ with no $(0,2)$-torsion; its curvature is
$$R_{i\bar j k}^{\ \ \ \ l} = -\partial_i\partial_{\bar j} g_{k\bar m} g^{l\bar m} + \cdots,\qquad
\mathrm{Ric}(\omega)_{i\bar j} = -\partial_i\partial_{\bar j}\log\det g .$$
$\mathrm{Ric}(\omega)$ is a closed real $(1,1)$-form representing $c_1^{BC}(M) \in H^{1,1}_{BC}(M,\mathbb R)$, the **Bott-Chern cohomology** group
$$H^{1,1}_{BC}(M,\mathbb R)=\frac{\{\alpha \in A^{1,1}_{\mathbb R} : d\alpha =0\}}{\{\sqrt{-1}\partial\bar\partial \varphi : \varphi\in C^\infty(M,\mathbb R)\}} .$$
Because $\omega_0$ need not be closed, $[\omega(t)]$ does not lie in a fixed cohomology group; one instead writes $\omega(t)=\hat\omega(t)+\sqrt{-1}\partial\bar\partial\varphi$ with the reference path $\hat\omega(t)=\omega_0 - t\,\mathrm{Ric}(\omega_0)$, reducing the flow to the **parabolic complex Monge-Ampère equation**
$$\frac{\partial \varphi}{\partial t} = \log \frac{(\hat\omega(t)+\sqrt{-1}\partial\bar\partial\varphi)^n}{\omega_0^n},\qquad \varphi(0)=0 ,$$
a scalar, uniformly parabolic, fully nonlinear PDE as long as $\hat\omega(t)+\sqrt{-1}\partial\bar\partial\varphi>0$.

**Theorem (Tosatti-Weinkove, JDG 2015).** A unique maximal smooth solution exists on $[0,T)$ with
$$T=\sup\{\,t>0 : \exists\,\psi\in C^\infty(M,\mathbb R)\ \text{with}\ \omega_0 - t\,\mathrm{Ric}(\omega_0)+\sqrt{-1}\partial\bar\partial\psi>0\,\}.$$
Thus $T$ is determined by the Bott-Chern class $[\omega_0]-t\,c_1^{BC}(M)$ meeting the boundary of the cone of Bott-Chern classes containing a positive representative. Volume evolves by $\frac{d}{dt}\int_M \omega^n = -n\int_M \mathrm{Ric}(\omega)\wedge\omega^{n-1}$, a polynomial in $t$ of degree $\le n$, so the volume behavior at $T$ is a purely cohomological quantity.

Two structural facts drive all estimates: the **maximum principle** applied to $\dot\varphi$ and $\mathrm{tr}_{\omega_0}\omega$ (Aubin-Yau second-order estimate, corrected for torsion by Cherrier's trick), and the **Calabi-type third-order estimate** of Sherman-Weinkove: if $C^{-1}\omega_0 \le \omega(t)\le C\omega_0$ on a parabolic cylinder, then all higher derivatives of $\omega(t)$ are bounded there.

## 3. History & State of the Art (SOTA)

- **2010-2011.** M. Gill introduced the flow (as the parabolic Monge-Ampère equation on Hermitian manifolds) and proved: if $c_1^{BC}(M)=0$, the flow exists for all time and converges smoothly to the unique Chern-Ricci-flat metric in its class — a parabolic proof of the Hermitian Calabi-Yau theorem of Cherrier and Tosatti-Weinkove.
- **2011.** Streets and Tian independently introduced Hermitian curvature flows, including the pluriclosed flow ($\partial\bar\partial$-closed metrics), a closely related but distinct evolution with better a priori structure.
- **2013.** Tosatti and Weinkove named the Chern-Ricci flow and gave the first systematic study of complex surfaces (Compositio Math. 149), including Inoue surfaces, Hopf surfaces, and blow-ups.
- **2015.** The general existence-time theorem (JDG 99) and the collapsing analysis on non-Kähler elliptic surfaces (Math. Ann. 362).
- **2015-2020.** Extensions to Oeljeklaus-Toma manifolds (Zheng), Chern scalar curvature behavior (Gill-Smith), weak/viscosity solutions past singular times, and homogeneous solutions.
- **State of the art.** The existence time is completely understood cohomologically in all dimensions. The singularity structure is understood for every explicitly known non-Kähler surface class except Kato/class VII surfaces with $b_2>0$, and essentially nothing is proved in dimension $\ge 3$ outside homogeneous or cohomologically trivial cases.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $c_1^{BC}(M)=0$ (e.g. Calabi-Yau, some non-Kähler Calabi-Eckmann-type) | Immortal flow, smooth convergence to Chern-Ricci-flat metric, any $n$ | Gill 2011 |
| Kähler manifolds, any $n$ | Reduces to Kähler-Ricci flow; full analytic MMP for surfaces | Cao 1985; Song-Weinkove |
| Hopf surfaces $(\mathbb C^2\setminus 0)/\langle z\mapsto \lambda z\rangle$ | Explicit solution, $T<\infty$, volume $\to 0$, collapse to the elliptic fiber; $s\sim (T-t)^{-1}$ | Tosatti-Weinkove 2013/2015 |
| Inoue surfaces (class $S^0,S^\pm$) | $T=\infty$; $\tfrac1t\,\omega(t)$ converges to a nonnegative $(1,1)$-current, leafwise flat, in $C^{1+\alpha}$ potentials | Tosatti-Weinkove 2013; Angella-Tosatti |
| Non-Kähler properly elliptic surfaces ($\mathrm{kod}=1$) | Normalized flow exists for all time and collapses to the orbifold base Riemann surface, GH and locally smooth away from singular fibers | Tosatti-Weinkove, Math. Ann. 2015 |
| Blow-ups of surfaces at a point, with suitable $\omega_0$ | Flow contracts the exceptional $(-1)$-curve in finite time; metric completion is the blow-down | Tosatti-Weinkove 2013 |
| Oeljeklaus-Toma manifolds ($n\ge 2$) | Long-time existence, collapsing behavior of the normalized flow | Zheng 2017 |
| Locally homogeneous surfaces | Complete classification of the flow's behavior | Boling 2016 (pluriclosed); analogues for Chern-Ricci |
| Any $M$, uniform metric equivalence | $|\nabla^k \mathrm{Rm}|$ bounds (Calabi/Shi-type local estimate) | Sherman-Weinkove 2013 |

## 5. Principal Obstacles

- **Loss of cohomological rigidity.** In the Kähler case $[\omega(t)]=[\omega_0]-t\,c_1$ lives in $H^{1,1}(M,\mathbb R)$ and intersection numbers control volumes of *all* subvarieties. Bott-Chern classes on non-Kähler surfaces carry far less intersection theory: the positivity cone is not described by numerical criteria, so one cannot read off from $T$ which curves are being contracted.
- **Torsion terms.** With $\partial\omega \ne 0$, the evolution of $\mathrm{tr}_{\omega_0}\omega$ and of $|\mathrm{Rm}|^2$ acquires torsion terms of the same differential order as the good negative terms. Maximum-principle arguments that close in the Kähler case (Cao's estimates) only close after adding a Cherrier-type exponential correction, which costs the sharp constants needed for blow-up rates.
- **No Perelman package.** There is no known monotone entropy, no $\mathcal W$-functional, no reduced volume, and no non-collapsing theorem for the Chern-Ricci flow. Consequently one cannot rule out collapsed limits or run a blow-up/compactness argument to extract a singularity model.
- **Scalar curvature is not a Ricci trace of the Riemannian metric.** The Chern scalar curvature $s$ satisfies $\partial_t s = \Delta s + |\mathrm{Ric}|^2 + (\text{torsion})$, and the torsion terms have no sign. Zhang's Kähler-Ricci proof that scalar curvature blows up at finite-time singularities therefore does not transfer.
- **Class VII surfaces.** The Global Spherical Shell conjecture (classification of surfaces with $b_1=1$, $b_2>0$) is itself open, so any singularity classification on those surfaces would either presuppose or imply hard classification results.

## 6. The Gap

Proved: the singular *time* in all dimensions; the singular *behavior* on every surface class whose geometry is explicitly known (Kähler, $c_1^{BC}=0$, Hopf, Inoue, elliptic, one-point blow-ups). Conjectured: that for an *arbitrary* initial Hermitian metric on an arbitrary compact complex surface, the limit at $T$ is a holomorphic contraction.

The precise missing step is a **uniform scalar estimate independent of the geometry**: a bound
$$\|\varphi(t)\|_{C^0} \le C \quad\text{and}\quad \omega(t) \ge C^{-1}\,\pi^*\omega_{\text{limit}}$$
on the region where the limiting class is strictly positive, with $C$ depending only on $\omega_0$ and $T$. In the Kähler case this comes from Kołodziej-type $L^\infty$ estimates plus intersection-theoretic positivity of $[\omega_0]-T c_1$ on subvarieties. Non-Kähler, the pluripotential input exists (Cherrier, Tosatti-Weinkove, Guedj-Lu), but the *positivity input* — a Nakai-Moishezon criterion for Bott-Chern classes on a non-Kähler surface — does not. Crossing the gap means proving such a criterion, or replacing it by a curvature-based argument that identifies the collapsing locus directly from the flow.

## 7. Current Research (as of June 2026)

- **Northwestern / NYU (Tosatti, Weinkove and collaborators):** sharpening convergence on Inoue and Kato surfaces, leafwise-flat limit currents, and weak solutions across singular times.
- **Streets, Tian, Ustinovskiy and the pluriclosed-flow school:** the pluriclosed flow has a Perelman-type functional and generalized Kähler structure; results there (global existence on complex surfaces with vanishing appropriate classes, and classification of static metrics) are used as a template for what Chern-Ricci statements should look like. *(frontier — verify: recent claims of long-time existence for pluriclosed flow on all class VII surfaces.)*
- **Chinese schools (Zheng, Y. Zhang, X. Zhang, Fu):** Chern-Ricci flow on solvmanifolds, Oeljeklaus-Toma manifolds and higher-dimensional homogeneous examples; explicit collapsing rates.
- **Pluripotential input:** uniform $L^\infty$ estimates for complex Monge-Ampère equations by the Guo-Phong-Tong method, which avoid pluripotential theory and are robust to torsion — currently being applied to Hermitian and parabolic settings. *(frontier — verify: fully torsion-robust parabolic version.)*
- **Numerical/experimental:** discretized flows on explicit Hopf and Inoue quotients used to test the conjectured $(T-t)^{-1}$ curvature rate.

## 8. Future Work

1. Prove the Chern scalar curvature blows up at any finite-time singularity (the Chern analogue of Z. Zhang's theorem), which would already rule out "type III without curvature blow-up" scenarios.
2. Develop a Nakai-Moishezon-type positivity criterion in $H^{1,1}_{BC}$ for compact complex surfaces.
3. Build a compactness theory for Hermitian metrics with bounded Chern curvature and torsion — a Cheeger-Gromov theory adapted to non-symmetric connections — to extract singularity models.
4. Transport the pluriclosed flow's monotone functional to the Chern-Ricci setting, or prove no such functional exists.
5. Dimension $\ge 3$: identify a class (e.g. Vaisman manifolds, complex nilmanifolds, torus bundles) rich enough to test the contraction picture without full classification.

## 9. Key References

- **[Foundational]** M. Gill. *Convergence of the parabolic complex Monge-Ampère equation on compact Hermitian manifolds.* Communications in Analysis and Geometry 19 (2011), 277-303.
- **[Foundational]** V. Tosatti, B. Weinkove. *On the evolution of a Hermitian metric by its Chern-Ricci form.* Journal of Differential Geometry 99 (2015), 125-163.
- **[Foundational]** V. Tosatti, B. Weinkove. *The Chern-Ricci flow on complex surfaces.* Compositio Mathematica 149 (2013), 2101-2138.
- **[SOTA]** V. Tosatti, B. Weinkove. *The Chern-Ricci flow on elliptic surfaces.* Mathematische Annalen 362 (2015), 1223-1271.
- **[SOTA]** M. Sherman, B. Weinkove. *Local Calabi and curvature estimates for the Chern-Ricci flow.* New York Journal of Mathematics 19 (2013), 565-582.
- **[SOTA]** J. Streets, G. Tian. *A parabolic flow of pluriclosed metrics.* International Mathematics Research Notices 2010, no. 16, 3101-3133.
- **[SOTA]** J. Streets, G. Tian. *Hermitian curvature flow.* Journal of the European Mathematical Society 13 (2011), 601-634.
- **[SOTA]** T. Zheng. *The Chern-Ricci flow on Oeljeklaus-Toma manifolds.* Canadian Journal of Mathematics 69 (2017), 220-240.
- **[SOTA]** V. Tosatti, B. Weinkove. *On the Calabi-Yau equation on compact Hermitian manifolds.* Journal of the American Mathematical Society 23 (2010), 1187-1195.
- **[Survey]** V. Tosatti. *KAWA lecture notes on the Kähler-Ricci flow.* Annales de la Faculté des Sciences de Toulouse 27 (2018), 285-376.
- **[Survey]** J. Song, B. Weinkove. *An introduction to the Kähler-Ricci flow.* In *An Introduction to the Kähler-Ricci Flow*, Lecture Notes in Mathematics 2086, Springer, 2013.
- **[Survey]** V. Tosatti, B. Weinkove. *The Chern-Ricci flow.* Rendiconti dell'Istituto di Matematica dell'Università di Trieste, 2022 (survey article).

## 10. Worked Example / Concrete Special Case

**The standard Hopf surface.** Let $M=(\mathbb C^2\setminus\{0\})/\langle z\mapsto 2z\rangle$, diffeomorphic to $S^1\times S^3$, with $b_1=1$ and no Kähler metric. Take
$$\omega_0=\frac{\sqrt{-1}}{|z|^2}\big(dz^1\wedge d\bar z^1 + dz^2\wedge d\bar z^2\big),\qquad |z|^2=|z^1|^2+|z^2|^2,$$
which is invariant under $z\mapsto 2z$ and so descends to $M$. Then $\det g = |z|^{-4}$, hence
$$\mathrm{Ric}(\omega_0) = -\sqrt{-1}\partial\bar\partial\log|z|^{-4} = 2\sqrt{-1}\partial\bar\partial\log|z|^2 = 2(\omega_0-\beta),\qquad
\beta:=\sqrt{-1}\,\frac{\bar z_i z_j}{|z|^4}\,dz^i\wedge d\bar z^j .$$
**Ansatz.** Try $\omega(t)=\omega_0 - t\,\mathrm{Ric}(\omega_0) = (1-2t)\omega_0 + 2t\beta$. In a unitary frame adapted to the radial direction $z$, the two eigenvalues of $g(t)$ are
$$\lambda_{\text{fiber}} = \frac{(1-2t)+2t}{|z|^2}=\frac{1}{|z|^2},\qquad \lambda_{\text{base}}=\frac{1-2t}{|z|^2}.$$
So $\det g(t) = (1-2t)\,|z|^{-4}$ and
$$\mathrm{Ric}(\omega(t)) = -\sqrt{-1}\partial\bar\partial\big(\log(1-2t) - 2\log|z|^2\big) = 2\sqrt{-1}\partial\bar\partial\log|z|^2 = \mathrm{Ric}(\omega_0).$$
The Chern-Ricci form is constant along the flow, so $\partial_t\omega = -\mathrm{Ric}(\omega_0) = -\mathrm{Ric}(\omega(t))$: the ansatz is an exact solution, valid exactly on $[0,T)$ with $T=\tfrac12$, matching the cohomological formula of Section 2.

**Singularity.** As $t\to \tfrac12$:
- $\mathrm{Vol}(M,\omega(t)) = (1-2t)\,\mathrm{Vol}(M,\omega_0) \to 0$ linearly — a *collapsing* singularity.
- The fiber direction (tangent to the elliptic curves $\mathbb C^*/\langle z\sim 2z\rangle$ of the Hopf fibration) keeps length $\asymp 1$; the base $\mathbb P^1$ direction shrinks like $(1-2t)^{1/2}$. The Gromov-Hausdorff limit is the flat $2$-torus fiber.
- Chern scalar curvature: since $\mathrm{Ric}(\omega_0)$ has eigenvalues $0$ (fiber) and $2/|z|^2$ (base),
$$s(t)=\mathrm{tr}_{\omega(t)}\mathrm{Ric}(\omega(t)) = \frac{2/|z|^2}{(1-2t)/|z|^2} = \frac{2}{1-2t}=\frac{1}{T-t}.$$
This is a **type I** singularity with exactly the rate conjectured in (B), and it is contraction-free: nothing is blown down, the whole manifold collapses onto its fiber. The general conjecture asserts that every finite-time singularity is a combination of this collapsing model and the curve-contracting model seen on blow-ups — and it is exactly the absence of a compactness theory for such Hermitian collapsings (Section 5) that blocks the proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*