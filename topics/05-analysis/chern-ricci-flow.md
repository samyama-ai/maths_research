---
id: 05-analysis/chern-ricci-flow
title: "Chern-Ricci Flow"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chern-Ricci Flow

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/chern-ricci-flow` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $X$ be a compact complex manifold of complex dimension $n$ and $\omega_0$ a Hermitian metric (a positive $(1,1)$-form, **not** assumed closed). The **Chern-Ricci flow** is

$$\frac{\partial}{\partial t}\omega(t) \;=\; -\,\mathrm{Ric}(\omega(t)),\qquad \omega(0)=\omega_0,$$

where $\mathrm{Ric}(\omega) = -\sqrt{-1}\,\partial\bar\partial \log\det g$ is the Chern-Ricci form of the Chern connection. When $\omega_0$ is Kähler this is exactly the Kähler-Ricci flow.

The central open problem: **does the Chern-Ricci flow carry out a birational classification of non-Kähler complex manifolds, in the way the Kähler-Ricci flow carries out the analytic Minimal Model Program?**

Concretely, the guiding conjecture of Tosatti–Weinkove for complex **surfaces** states: starting from any Hermitian metric $\omega_0$ on a compact complex surface $X$, the flow either exists for all time, or reaches a maximal time $T<\infty$ at which the metrics converge in $C^\infty_{loc}$ outside a finite set of $(-1)$-curves which are contracted, so the flow can be restarted on the blow-down; after finitely many such surgeries the flow exists for all time on a minimal model, and the rescaled flow $\omega(t)/t$ (or $e^{-t}\omega(t)$) converges in the Gromov-Hausdorff sense to a canonical limit — a point, a circle, a Riemann orbifold surface, or a Kähler-Einstein metric — determined by the Kodaira dimension and the class of the surface.

A complete resolution requires: (i) proving the singularity/surgery statement without extra symmetry or curvature hypotheses; (ii) identifying all long-time limits, including for **class VII** surfaces with $b_2>0$, where the flow is proposed as an analytic route to the global spherical shell conjecture; (iii) generalizing to $n\ge 3$, where even the correct statement is not agreed upon.

## 2. Mathematical Foundations

**Chern connection.** On a Hermitian manifold $(X,J,g)$ with $g_{i\bar j}$, the Chern connection $\nabla$ is the unique connection with $\nabla J=0$, $\nabla g=0$ and $(0,1)$-part equal to $\bar\partial$. Its curvature is
$$R_{i\bar j k}{}^{\ell} = -\partial_i\partial_{\bar j} g_{k\bar m}\,g^{\ell\bar m} + g^{\ell \bar m}g^{p\bar q}\,\partial_i g_{k\bar q}\,\partial_{\bar j} g_{p \bar m},$$
and the **first Chern-Ricci curvature** is the trace $R_{i\bar j}=g^{k\bar\ell}R_{i\bar j k \bar\ell}$, giving the closed real $(1,1)$-form
$$\mathrm{Ric}(\omega) = \sqrt{-1}\,R_{i\bar j}\,dz^i\wedge d\bar z^j = -\sqrt{-1}\,\partial\bar\partial\log\det(g_{k\bar\ell}).$$
It represents $c_1^{BC}(X)$, the first **Bott-Chern class**, living in
$$H^{1,1}_{BC}(X,\mathbb{R}) = \frac{\{\alpha \in A^{1,1}(X,\mathbb{R}) : d\alpha = 0\}}{\{\sqrt{-1}\partial\bar\partial\psi : \psi \in C^\infty(X,\mathbb{R})\}}.$$
Non-Kähler manifolds have three inequivalent Ricci traces (first, second, third Chern-Ricci); the flow uses the first, which is $\partial\bar\partial$-exact up to Bott-Chern class and hence gives a *scalar* reduction.

**Parabolic Monge-Ampère reduction.** Write $\hat\omega_t = \omega_0 - t\,\mathrm{Ric}(\omega_0)$. Since $\mathrm{Ric}$ changes within a Bott-Chern class by $\sqrt{-1}\partial\bar\partial$ of a function, solutions take the form $\omega(t)=\hat\omega_t + \sqrt{-1}\partial\bar\partial\varphi$ with
$$\frac{\partial \varphi}{\partial t} = \log\frac{(\hat\omega_t + \sqrt{-1}\partial\bar\partial\varphi)^n}{\omega_0^n},\qquad \varphi(0)=0,\qquad \hat\omega_t + \sqrt{-1}\partial\bar\partial\varphi>0 .$$
This is a scalar parabolic complex Monge-Ampère equation on a Hermitian manifold — no torsion terms appear in the equation itself, which is the essential reason the flow is tractable.

**Maximal existence time (Tosatti–Weinkove, JDG 2015).** A unique smooth solution exists on $[0,T)$ with
$$T = \sup\{\,t\ge 0 \;:\; \exists\,\psi\in C^\infty(X,\mathbb{R}) \text{ with } \omega_0 - t\,\mathrm{Ric}(\omega_0) + \sqrt{-1}\partial\bar\partial\psi > 0\,\}.$$
This is the exact Hermitian analogue of the Tian–Zhang criterion $T=\sup\{t : [\omega_0]-t c_1(X)>0\}$ for the Kähler-Ricci flow, but note $T$ is *not* a purely cohomological quantity in general, since the positive cone in $H^{1,1}_{BC}$ need not behave as in the Kähler case.

**Normalizations.** For $K_X$ "positive" one uses $\partial_t\omega = -\mathrm{Ric}(\omega)-\omega$; for collapsing problems, $\partial_t\omega=-\mathrm{Ric}(\omega)$ with rescaling $\tilde\omega = \omega(t)/t$ or $(T-t)^{-1}\omega(t)$.

## 3. History & State of the Art (SOTA)

- **1985.** H.-D. Cao proves convergence of the Kähler-Ricci flow on manifolds with $c_1=0$ and $c_1<0$, giving a parabolic proof of Yau's theorem.
- **2011.** M. Gill introduces the flow $\partial_t\omega=-\mathrm{Ric}(\omega)$ on **Hermitian** manifolds with $c_1^{BC}(X)=0$ and proves long-time existence and convergence to a Chern-Ricci-flat metric — the parabolic counterpart of the Tosatti–Weinkove solution of the Calabi-Yau equation on Hermitian manifolds.
- **2013–2015.** Tosatti and Weinkove name the flow, establish the maximal existence time formula, prove the Kähler-Einstein convergence results, and launch the surface classification programme (Compositio 149 (2013); JDG 99 (2015)).
- **2013.** Sherman–Weinkove prove local Calabi-type third-order and curvature estimates, giving $C^\infty_{loc}$ convergence away from singular sets from a *local* uniform equivalence of metrics.
- **2015–2016.** Tosatti–Weinkove–Yang settle the collapsing behaviour on non-Kähler elliptic surfaces (Math. Ann. 2015); Fang–Tosatti–Weinkove–Zheng settle Inoue surfaces (J. Funct. Anal. 2016) — the flow collapses to a circle.
- **2017–present.** Weak/viscosity solutions past singularities (Nie; Tô), Oeljeklaus-Toma manifolds and homogeneous examples (Zheng and coauthors), and comparisons with Streets–Tian's pluriclosed flow, which preserves the SKT condition but is a genuinely different (non-scalar) flow.

Present state: the flow is completely understood on all compact complex surfaces of Kodaira dimension $\ge 0$ **modulo** the general singularity-formation conjecture, and largely open on class VII surfaces and in dimension $\ge 3$.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $\omega_0$ Kähler | Flow = Kähler-Ricci flow; MMP with scaling known in dim 2, largely known in higher dim (Song–Tian) |
| $c_1^{BC}(X)=0$, any $n$ | Gill (2011): $T=\infty$; $\omega(t)\to\omega_\infty$ Chern-Ricci-flat, smoothly |
| $X$ Kähler with $c_1(X)<0$, $\omega_0$ arbitrary Hermitian | Tosatti–Weinkove (2015): normalized flow converges smoothly to the Kähler-Einstein metric |
| $K_X$ nef in the Bott-Chern sense | $T=\infty$; the flow does not develop finite-time singularities |
| Hopf surfaces $(\mathbb{C}^2\setminus\{0\})/\langle z\mapsto \lambda z\rangle$ | Explicit solution, $T<\infty$, Gromov-Hausdorff limit is a circle (§10) |
| Inoue surfaces (class VII, $b_2=0$) | Fang–Tosatti–Weinkove–Zheng (2016): $T=\infty$, $\omega(t)/t$ collapses; GH limit a circle |
| Non-Kähler properly elliptic and Kodaira surfaces | Tosatti–Weinkove–Yang (2015): $\omega(t)/t \to$ pullback of the orbifold Kähler-Einstein metric on the base curve; GH convergence to the base |
| Complex surfaces, weak solutions | Nie (2017), Tô (2018): weak (viscosity/pluripotential) solutions exist past $T$ and are smooth off the singular set |
| Non-Kähler blow-ups, symmetric initial data | Tosatti–Weinkove (2013): flow contracts the exceptional $(-1)$-curve in finite time and continues on the blow-down |
| Any $n$, local estimates | Sherman–Weinkove (2013): $C^{1,1}$/curvature bounds from local metric equivalence, with no global input |

## 5. Principal Obstacles

- **No maximum principle for torsion.** In the Kähler case, $d\omega=0$ makes $\Delta \mathrm{tr}_{\hat\omega}\omega$ computations closed. Here the torsion $T^k_{ij}=g^{k\bar\ell}(\partial_i g_{j\bar\ell}-\partial_j g_{i\bar\ell})$ appears in every commutation identity, and $|T|$ is not controlled by the flow: the standard Aubin–Yau second-order estimate produces uncontrolled first-derivative-of-torsion terms.
- **Cohomology is too weak.** $H^{1,1}_{BC}$ is not a ring with a well-behaved intersection form on non-Kähler surfaces; $\int_X\omega^n$ can vanish in the limit without a cohomological reason. So the Kähler-Ricci flow strategy of "read the singularity from the class $[\omega_0]-Tc_1$" has no direct substitute.
- **No Riemannian Ricci flow tools.** The Chern-Ricci flow is not the Riemannian Ricci flow of any metric; Perelman's $\mathcal{W}$-entropy, monotonicity, non-collapsing, and Hamilton–Ivey pinching are unavailable. Scalar curvature bounds along the flow are only known in special cases.
- **No uniform $C^0$ estimate.** In the Kähler-Ricci flow, $\varphi$ is bounded on $[0,T)$ by Kolodziej-type pluripotential theory using the fixed cohomology class. On Hermitian manifolds the Monge-Ampère mass $\int(\hat\omega_t+\sqrt{-1}\partial\bar\partial\varphi)^n$ is not a topological invariant, so the $L^\infty$ bound for $\varphi$ near $T$ fails to follow from Bott-Chern data alone.
- **Class VII rigidity.** For surfaces with $b_2>0$ (Inoue-Hirzebruch, Kato surfaces), no explicit metric is known adapted to the flow, and there is no known geometric object the flow could converge to that would produce a spherical shell.

## 6. The Gap

The proven region is: (a) all cases where the flow exists for all time and a **model limit is already available** ($c_1^{BC}=0$, $c_1<0$, elliptic fibrations, Inoue, Hopf); (b) finite-time contractions under **explicit symmetry or torsion assumptions**.

The missing step is a **uniform, hypothesis-free scalar estimate near a finite-time singularity**: a bound
$$\|\varphi(t)\|_{L^\infty(X)} \le C \quad\text{and}\quad C^{-1}\hat\omega_t \le \omega(t)\le C\hat\omega_t \ \text{ on } X\setminus E$$
for $t\in[0,T)$, where $E$ is the (conjecturally analytic) singular set, with $C$ independent of $t$ and not requiring $\sqrt{-1}\partial\bar\partial\omega_0=0$ or a torus symmetry. Given such a bound, Sherman–Weinkove local estimates upgrade it to $C^\infty_{loc}$ convergence off $E$, and Nie/Tô weak solutions supply the restart. Everything in §1 for surfaces follows. The barrier is that all existing routes to this bound consume either the closedness of $\omega_0$ or an explicit ansatz.

## 7. Current Research (as of June 2026)

- **Northwestern / Columbia school (Tosatti, Weinkove and students).** Extending the surface programme to precise singularity structure, and to $(n-1)$-plurisubharmonic and Gauduchon settings via Monge-Ampère equations for $(n-1,n-1)$-forms.
- **Pluripotential methods for Hermitian Monge-Ampère flows.** Guedj, Lu, Tô and collaborators push regularizing properties of degenerate complex Monge-Ampère flows on Hermitian manifolds; the target is a Kolodziej-type $L^\infty$ estimate uniform in $t$ that would close the gap of §6. *(frontier — verify)*
- **Homogeneous and solvmanifold test cases.** Zheng, Kawamura and coauthors compute the flow on Oeljeklaus-Toma manifolds, Vaisman manifolds, and complex Lie groups, giving a growing list of long-time limits that any general theorem must reproduce.
- **Comparison with pluriclosed flow.** Streets–Tian's pluriclosed flow, with its generalized Kähler and Bismut-flat rigidity theorems, is being used to predict what the Chern-Ricci flow should do on class VII surfaces; recent Bismut-flat classification results suggest a Chern-Ricci analogue on Hopf surfaces. *(frontier — verify)*
- **Higher-dimensional statements.** Which non-Kähler "MMP" the flow should implement in $n\ge 3$ is unsettled — candidates involve contracting subvarieties on which $\int\omega^{\dim}$ tends to $0$ rather than cohomological criteria.

## 8. Future Work

1. **Uniform $C^0$ bound.** Prove $\sup_{[0,T)}\|\varphi\|_{L^\infty}<\infty$ under the assumption that the limiting Bott-Chern class is "big" in a suitable Hermitian sense.
2. **Torsion control.** Find a quantity, monotone or almost-monotone along the flow, that dominates $|T|_{\omega(t)}$ — the analogue of Perelman's scalar curvature bound for the Kähler-Ricci flow.
3. **Surgery formalism.** Define Chern-Ricci flow with surgery on surfaces and prove that only finitely many surgeries occur, matching the finiteness of $(-1)$-curves.
4. **Class VII.** Determine the long-time behaviour on a Kato surface; a proof that the rescaled flow converges to a leafwise-flat structure would bear directly on the global spherical shell conjecture.
5. **Higher dimension.** Formulate and test the correct conjecture for $n=3$ on Calabi-Eckmann and twistor-type manifolds.

## 9. Key References

- **[Foundational]** H.-D. Cao. *Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds.* Inventiones Mathematicae 81 (1985), 359-372.
- **[Foundational]** M. Gill. *Convergence of the parabolic complex Monge-Ampère equation on compact Hermitian manifolds.* Communications in Analysis and Geometry 19 (2011), 277-303. [DOI](https://doi.org/10.4310/cag.2011.v19.n2.a2)
- **[Foundational]** V. Tosatti, B. Weinkove. *On the evolution of a Hermitian metric by its Chern-Ricci form.* Journal of Differential Geometry 99 (2015), 125-157.
- **[Foundational]** V. Tosatti, B. Weinkove. *The Chern-Ricci flow on complex surfaces.* Compositio Mathematica 149 (2013), 2101-2138. [DOI](https://doi.org/10.1112/s0010437x13007471)
- **[SOTA / Recent]** M. Sherman, B. Weinkove. *Local Calabi and curvature estimates for the Chern-Ricci flow.* New York Journal of Mathematics 19 (2013), 565-582.
- **[SOTA / Recent]** V. Tosatti, B. Weinkove, X. Yang. *Collapsing of the Chern-Ricci flow on elliptic surfaces.* Mathematische Annalen 362 (2015), 1223-1271. [DOI](https://doi.org/10.1007/s00208-014-1160-1)
- **[SOTA / Recent]** S. Fang, V. Tosatti, B. Weinkove, T. Zheng. *Inoue surfaces and the Chern-Ricci flow.* Journal of Functional Analysis 271 (2016), 3162-3185. [DOI](https://doi.org/10.1016/j.jfa.2016.08.013)
- **[SOTA / Recent]** X. Nie. *Weak solutions of the Chern-Ricci flow on compact complex surfaces.* Mathematical Research Letters 24 (2017), 1819-1844. [DOI](https://doi.org/10.4310/mrl.2017.v24.n6.a13)
- **[SOTA / Recent]** T. D. Tô. *Regularizing properties of complex Monge-Ampère flows II: Hermitian manifolds.* Mathematische Annalen 372 (2018), 699-741. [DOI](https://doi.org/10.1007/s00208-017-1574-7)
- **[Related flow]** J. Streets, G. Tian. *Hermitian curvature flow.* Journal of the European Mathematical Society 13 (2011), 601-634.
- **[Survey]** V. Tosatti, B. Weinkove. *The Chern-Ricci flow.* Rendiconti dell'Istituto di Matematica dell'Università di Trieste 54 (2022).
- **[Survey]** J. Song, B. Weinkove. *An introduction to the Kähler-Ricci flow.* In *An Introduction to the Kähler-Ricci Flow*, Lecture Notes in Mathematics 2086, Springer, 2013. [DOI](https://doi.org/10.1007/978-3-319-00819-6_3)

## 10. Worked Example / Concrete Special Case

**The Hopf surface.** Let $X = (\mathbb{C}^2\setminus\{0\})/\langle z\mapsto 2z\rangle$, diffeomorphic to $S^1\times S^3$. It carries no Kähler metric ($b_1=1$), so the Kähler-Ricci flow does not apply. Take the Boothby metric
$$\omega_0 = \sqrt{-1}\,\frac{\delta_{jk}}{|z|^2}\,dz^j\wedge d\bar z^k, \qquad |z|^2=|z^1|^2+|z^2|^2,$$
which is $\langle z\mapsto 2z\rangle$-invariant, hence descends to $X$.

*Step 1 — Chern-Ricci form.* $\det g_0 = |z|^{-4}$, so
$$\mathrm{Ric}(\omega_0) = -\sqrt{-1}\partial\bar\partial\log|z|^{-4} = 2\sqrt{-1}\,\partial\bar\partial\log|z|^2 = 2\sqrt{-1}\Big(\frac{\delta_{jk}}{|z|^2}-\frac{\bar z_j z_k}{|z|^4}\Big)dz^j\wedge d\bar z^k .$$
This is $2\,\pi^*\omega_{FS}$ for the Hopf map $\pi:X\to\mathbb{P}^1$; it is semi-positive with kernel the Hopf fibre direction.

*Step 2 — Ansatz.* Set $\omega(t)=\omega_0 - t\,\mathrm{Ric}(\omega_0)$, i.e.
$$g(t)_{j\bar k} = \frac{1-2t}{|z|^2}\delta_{jk} + \frac{2t}{|z|^4}\bar z_j z_k .$$

*Step 3 — Determinant.* The matrix is $a\,\delta_{jk} + b\,\bar z_j z_k$ with $a=(1-2t)/|z|^2$, $b=2t/|z|^4$. Eigenvalues are $a+b|z|^2 = 1/|z|^2$ (radial/Hopf direction) and $a=(1-2t)/|z|^2$ (base direction). Hence
$$\det g(t) = \frac{1-2t}{|z|^4} = (1-2t)\det g_0 .$$

*Step 4 — Verification.* $\log\det g(t) = \log\det g_0 + \log(1-2t)$ differs from $\log\det g_0$ by a function of $t$ only, so $\mathrm{Ric}(\omega(t))=\mathrm{Ric}(\omega_0)$ and $\partial_t\omega(t) = -\mathrm{Ric}(\omega_0)=-\mathrm{Ric}(\omega(t))$. The ansatz is the solution.

*Step 5 — Singularity.* Positivity fails exactly when $1-2t\le 0$, so
$$T = \tfrac12 .$$
As $t\uparrow \tfrac12$, the base $\mathbb{P}^1$ directions shrink like $(1-2t)$ while the Hopf fibre keeps length of order $1$; the total volume $\int_X\omega(t)^2 \sim (1-2t)$ tends to $0$. The diameter stays bounded and $(X,\omega(t))$ converges in the Gromov-Hausdorff sense to a **circle**, of length equal to that of the Hopf fibre in $\omega_0$ (namely $\log 2$ up to normalization).

*What it illustrates.* The Hopf surface has $c_1^{BC}\ne 0$ and $K_X$ not nef, yet the singularity at $T=1/2$ is *not* a contraction of a curve: it is a global collapse to a lower-dimensional object with no algebro-geometric contraction underneath. This is exactly the phenomenon absent from the Kähler-Ricci flow / MMP dictionary, and the reason the surface conjecture of §1 must include circle and orbifold limits alongside curve contractions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*