---
id: 05-analysis/kahler-ricci-flow-blowup
title: "Kahler-Ricci Flow Blowup"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kähler–Ricci Flow Blowup

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kahler-ricci-flow-blowup` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $X$ be a compact Kähler manifold of complex dimension $n$ and let $\omega(t)$ solve the (unnormalized) Kähler–Ricci flow
$$\frac{\partial}{\partial t}\omega(t) = -\mathrm{Ric}(\omega(t)), \qquad \omega(0)=\omega_0 .$$
The flow exists on a maximal interval $[0,T)$ with
$$T = \sup\{\, t>0 \;:\; [\omega_0] - t\,c_1(X) \in \mathcal{K}_X \,\},$$
where $\mathcal{K}_X$ is the Kähler cone (Tian–Zhang). When $T<\infty$ the curvature blows up. **The problem is to describe that blowup completely.** Three linked claims:

1. **(Scalar curvature)** The scalar curvature $R(\omega(t))$ stays uniformly bounded on $X\times[0,T)$ whenever the limiting class $\alpha_T=[\omega_0]-Tc_1(X)$ is semi-ample (Song–Tian). More generally: does $\sup_X R$ control the singularity?
2. **(Blowup model)** For any sequence $(x_i,t_i)$ with $t_i\to T$ and $Q_i=|\mathrm{Rm}|(x_i,t_i)\to\infty$, the parabolic rescalings $Q_i\,\omega(t_i+Q_i^{-1}s)$ subconverge to a complete ancient solution. Is that limit always a **shrinking gradient Kähler–Ricci soliton** (possibly singular)? Is the singularity always of Type I, i.e. $\sup_X|\mathrm{Rm}|(t)\le C/(T-t)$?
3. **(Geometry–algebra match)** Does $(X,\omega(t))$ converge in Gromov–Hausdorff sense as $t\to T$ to a compact metric space homeomorphic to a normal projective variety $X_T$, with the flow continuing past $T$ through the divisorial contraction or flip predicted by the Minimal Model Program (Song–Tian analytic MMP)?

A complete resolution proves or refutes each of (1)–(3) for all $(X,\omega_0)$ with $T<\infty$, in all dimensions $n\ge 2$.

## 2. Mathematical Foundations

**Potential reduction.** Fix $\chi\in -c_1(X)$ and set $\hat\omega_t=\omega_0+t\chi$, a Kähler form for $t\in[0,T)$. Writing $\omega(t)=\hat\omega_t+ i\partial\bar\partial\varphi$, the flow is the parabolic complex Monge–Ampère equation
$$\frac{\partial\varphi}{\partial t}=\log\frac{(\hat\omega_t+i\partial\bar\partial\varphi)^n}{\Omega},\qquad \varphi(0)=0,\qquad i\partial\bar\partial\log\Omega=\chi .$$
Since the flow is determined by a scalar PDE, the cohomological class $[\omega(t)]=[\omega_0]-tc_1(X)$ is *linear in $t$* — this is what makes the singular time computable from algebraic geometry alone.

**Curvature quantities.** With $g_{i\bar j}$ the metric, $R_{i\bar j}=-\partial_i\partial_{\bar j}\log\det g$, and $R=g^{i\bar j}R_{i\bar j}$, the volume form satisfies
$$\frac{\partial}{\partial t}\omega^n = -R\,\omega^n,\qquad \Big(\frac{\partial}{\partial t}-\Delta\Big)R = |\mathrm{Ric}|^2 \ge \frac{R^2}{n}.$$
The maximum principle then forces $\sup_X R(t)\ge -n/(t-T^*)$ for the blowup time $T^*$ of $R$; conversely a bound $R\le C$ does *not* immediately bound $|\mathrm{Rm}|$.

**Singularity types.** A finite-time singularity is **Type I** if $\sup_X|\mathrm{Rm}|(\cdot,t)\le C(T-t)^{-1}$, and **Type II** otherwise.

**Shrinking soliton.** A complete Kähler metric $g$ with $f\in C^\infty$ satisfying
$$R_{i\bar j}+\nabla_i\nabla_{\bar j}f=\lambda g_{i\bar j},\quad \nabla_i\nabla_j f=0,\quad \lambda>0,$$
generates a self-similar solution $\omega(t)=(1-2\lambda t)\,\phi_t^*\omega$, the conjectural universal model for the blowup.

**Analytic MMP data.** $\alpha_T=[\omega_0]-Tc_1(X)$ is nef and lies on $\partial\mathcal{K}_X$. Its **null locus** is $\mathrm{Null}(\alpha_T)=\bigcup\{V \subset X : \int_V\alpha_T^{\dim V}=0\}$. Collins–Tosatti proved $\mathrm{Null}(\alpha_T)=E_{nK}(\alpha_T)$, the non-Kähler locus. If $\alpha_T=c_1(L)$ with $L$ semi-ample, the map $\Phi_{|mL|}:X\to X_T$ contracts exactly $\mathrm{Null}(\alpha_T)$.

**Perelman's functionals.** $\mathcal{W}(g,f,\tau)=\int_X\big[\tau(R+|\nabla f|^2)+f-2n\big](4\pi\tau)^{-n}e^{-f}dV$ is monotone; $\nu$-entropy noncollapsing gives $\mathrm{Vol}(B_r)\ge \kappa r^{2n}$ at scales $r\le\sqrt{T}$ where curvature is controlled.

## 3. History & State of the Art

- **1985.** H.-D. Cao proves long-time existence and convergence when $c_1(X)<0$ or $c_1(X)=0$, re-deriving Yau's theorem by parabolic methods.
- **2006.** Tian–Zhang establish the maximal-time formula $T=\sup\{t:[\omega_0]-tc_1(X)>0\}$, making $T$ purely cohomological.
- **2007–2012.** Song–Tian propose the **analytic MMP**: KRF should implement the steps of the MMP with scaling, flowing through divisorial contractions and flips, and converging to canonical (Kähler–Einstein) metrics on minimal models. Established for elliptic surfaces and Iitaka fibrations (JAMS 2012).
- **2009.** Z. Zhang bounds $R$ uniformly for infinite-time flows on minimal models of general type.
- **2013–2015.** Song–Weinkove prove KRF contracts exceptional divisors with normal bundle $\mathcal{O}(-1)$ and restarts on the contracted manifold; Collins–Tosatti identify the singularity set with $\mathrm{Null}(\alpha_T)$, giving $C^\infty_{loc}$ convergence on $X\setminus\mathrm{Null}(\alpha_T)$.
- **2017.** Song–Tian construct weak KRF through singularities as a global solution on a sequence of birational models, unique in a suitable class.
- **2018–2020.** Bamler ("Convergence of Ricci flows with bounded scalar curvature," *Annals*) and Chen–Wang (*JDG*) settle the **Hamilton–Tian conjecture**: for Fano $X$, the normalized flow subconverges in Gromov–Hausdorff sense to a $\mathbb{Q}$-Fano variety carrying a singular Kähler–Ricci soliton, singular set of real codimension $\ge 4$.
- **2023–2024.** Guo–Phong–Tong ($L^\infty$ estimates for complex Monge–Ampère, *Annals* 2023) and Guo–Phong–Song–Sturm (diameter estimates, *CPAM* 2024) give class-uniform diameter and Green's-function bounds along the flow, independent of curvature.

## 4. Partial Results / Verified Cases

- **Fano case, $n$ arbitrary.** Hamilton–Tian conjecture: fully proved (Chen–Wang; Bamler; Chen–Sun–Wang). Rescaled limits are shrinking solitons on $\mathbb{Q}$-Fano varieties.
- **Type I singularities, any dimension.** Enders–Müller–Topping: the rescaled flow at a Type I singular point converges to a *nontrivial* gradient shrinking soliton. So claim (2) is settled *given* Type I.
- **Complex dimension $n=2$.** Complete picture: finite-time singularities on Kähler surfaces are either global extinction, collapse to a curve/point via a fibration, or contraction of finitely many disjoint $(-1)$-curves — the latter handled by Song–Weinkove, with the flow continuing on the blown-down surface.
- **Semi-ample $\alpha_T$ with $\dim X_T = n$ (birational contraction).** $R$ bounded and Gromov–Hausdorff convergence to the metric completion of $X_T\setminus \mathrm{Sing}$ is known in the divisorial cases treated by Song–Tian and Song–Weinkove.
- **Explicit models.** Feldman–Ilmanen–Knopf: $U(n)$-invariant shrinking solitons on $\mathcal{O}(-k)\to\mathbb{P}^{n-1}$ for $1\le k\le n-1$; these are the expected Type I blowup limits at divisorial contractions. Koiso's soliton on $\mathrm{Bl}_p\mathbb{P}^2$ models extinction there.
- **Projective bundles / Hirzebruch surfaces.** Song–Székelyhidi–Weinkove: on $\mathbb{P}(\mathcal{O}\oplus\mathcal{O}(-1)^{\oplus k})$ the flow either collapses fibers or contracts the zero section, exactly as MMP predicts.
- **Negative data.** Máximo produced four-dimensional Kähler Ricci flows on $\mathrm{Bl}_0\mathbb{C}^2$ that are **Type II**, so Type I is *not* universal; Appleton analyzed the associated Eguchi–Hanson bubbling.

## 5. Principal Obstacles

- **Scalar curvature does not control $|\mathrm{Rm}|$.** In Kähler geometry $R=g^{i\bar j}R_{i\bar j}$ is a trace of the Ricci form only; the "holomorphic sectional" directions can degenerate while $R$ stays bounded. Bamler's theory yields codimension-4 regularity *given* $R\le C$, but Stolarski's Ricci flows with bounded scalar curvature and unbounded $|\mathrm{Rm}|$ (higher dimension, non-Kähler) show no purely local argument can close the gap *(frontier — verify for the Kähler category)*.
- **No a priori $C^0$ bound on $\varphi$ at collapsing classes.** When $\alpha_T^n=0$ the reference volume vanishes; Yau/Kołodziej-type estimates degenerate, and the Monge–Ampère equation loses uniform ellipticity in every direction simultaneously.
- **Type II blowups are non-self-similar.** For Type II one must extract a *steady* or ancient non-soliton limit at a second, faster scale; there is no compactness theory forcing the limit to be a soliton, and Máximo/Appleton examples show genuine bubbling with Ricci-flat ALE ($\mathrm{Eguchi–Hanson}$) fibres.
- **Flips have no metric model.** Divisorial contractions are metrically "collapse a divisor"; flips change the manifold in codimension $\ge 2$ with no continuous family of Kähler metrics, so even the *statement* of continuation past a flip requires weak (pluripotential) solutions whose uniqueness is unproved in general.
- **Non-projective Kähler $X$.** The MMP itself is conjectural outside the projective category, so claim (3) has no algebraic target variety to converge to.

## 6. The Gap

Proven: (i) Type I $\Rightarrow$ soliton blowup limit; (ii) $R$ bounded $\Rightarrow$ codimension-4 structure and Gromov–Hausdorff limits; (iii) full descriptions for $n=2$, for Fano, and for divisorial contractions of $\mathcal{O}(-1)$-divisors.

Unproven: the implication $T<\infty \Rightarrow \sup_{X\times[0,T)}R<\infty$ for a general Kähler class, and the exclusion (or classification) of Type II finite-time singularities on *compact* Kähler manifolds. The precise missing step is a **uniform lower bound on the volume ratio / Perelman entropy at the singular scale in a degenerating Kähler class** — equivalently, a non-collapsing estimate that survives when $\alpha_T$ has zero volume on a subvariety. Every current proof of $R\le C$ uses semi-ampleness of $\alpha_T$ to import a smooth model metric from $X_T$; when $\alpha_T$ is merely nef and big with non-semi-ample structure (or nef with $\alpha_T^n=0$), no such model exists.

## 7. Current Research (as of June 2026)

- **Bamler's $\mathbb{F}$-convergence programme** (Berkeley) — metric-flow compactness without curvature bounds; being adapted to the Kähler setting to obtain singular-time limits as $\mathbb{RCD}$-type spaces *(frontier — verify)*.
- **Guo–Phong–Song–Sturm** (Rutgers/Columbia) — non-perturbative $L^\infty$, diameter and Green's-function estimates for degenerate Monge–Ampère equations, aiming to bound $\mathrm{diam}(X,\omega(t))$ and the Sobolev constant at $T$ using only cohomological data.
- **Song's "Riemannian geometry of Kähler–Einstein currents"** — identifying the metric completion of the flow limit with the algebraic model $X_T$, now extended toward flips.
- **Tosatti–Collins–Guenancia** — regularity and singularity sets for degenerate Kähler–Einstein metrics on singular varieties, supplying the target geometry of the continuation.
- **Chen–Wang–Sun school** — soliton degenerations and the connection to $K$-stability/$\mathbb{H}$-invariants for the limiting model.
- **U(2)- and torus-invariant analysis** (Appleton, Máximo, Isenberg–Knopf–Šešum) — constructing further Type II Kähler examples to delimit any general theorem.

## 8. Future Work

- Prove $R\le C$ on $[0,T)$ for all nef and big $\alpha_T$; the semi-ample case is the natural first target using the Base-Point-Free theorem.
- Classify complete shrinking Kähler–Ricci solitons with quadratic curvature decay in $n=2,3$; a classification plus Enders–Müller–Topping would close the Type I case.
- Develop a *soliton-plus-bubble* decomposition for Type II Kähler singularities, treating Eguchi–Hanson bubbles as the codimension-4 defect predicted by Bamler's theory.
- Formulate weak KRF through flips as a viscosity/pluripotential flow and prove uniqueness in the class of Song–Tian solutions.
- Extend the analytic MMP beyond projective $X$, or produce a compact non-projective Kähler counterexample to (3).

## 9. Key References

- **[Foundational]** H.-D. Cao. *Deformation of Kähler metrics to Kähler–Einstein metrics on compact Kähler manifolds.* Inventiones Mathematicae 81 (1985), 359–372.
- **[Foundational]** G. Tian, Z. Zhang. *On the Kähler–Ricci flow on projective manifolds of general type.* Chinese Annals of Mathematics Ser. B 27 (2006), 179–192. [DOI](https://doi.org/10.1007/s11401-005-0533-x)
- **[Foundational]** M. Feldman, T. Ilmanen, D. Knopf. *Rotationally symmetric shrinking and expanding gradient Kähler–Ricci solitons.* Journal of Differential Geometry 65 (2003), 169–209. [DOI](https://doi.org/10.4310/jdg/1090511686)
- **[SOTA]** R. Bamler. *Convergence of Ricci flows with bounded scalar curvature.* Annals of Mathematics 188 (2018), 753–831. [DOI](https://doi.org/10.4007/annals.2018.188.3.2)
- **[SOTA]** X.-X. Chen, B. Wang. *Space of Ricci flows (II) — Part B: Weak compactness of the flows.* Journal of Differential Geometry 116 (2020), 1–123. [DOI](https://doi.org/10.4310/jdg/1599271253)
- **[SOTA]** J. Song, G. Tian. *The Kähler–Ricci flow through singularities.* Inventiones Mathematicae 207 (2017), 519–595. [DOI](https://doi.org/10.1007/s00222-016-0674-4)
- **[SOTA]** J. Song, B. Weinkove. *Contracting exceptional divisors by the Kähler–Ricci flow.* Duke Mathematical Journal 162 (2013), 367–415. [DOI](https://doi.org/10.1215/00127094-1962881)
- **[SOTA]** T. Collins, V. Tosatti. *Kähler currents and null loci.* Inventiones Mathematicae 202 (2015), 1167–1198. [DOI](https://doi.org/10.1007/s00222-015-0585-9)
- **[SOTA]** B. Guo, D. H. Phong, F. Tong. *On $L^\infty$ estimates for complex Monge–Ampère equations.* Annals of Mathematics 198 (2023), 393–418. [DOI](https://doi.org/10.4007/annals.2023.198.1.4)
- **[SOTA]** B. Guo, D. H. Phong, J. Song, J. Sturm. *Diameter estimates in Kähler geometry.* Communications on Pure and Applied Mathematics 77 (2024), 3520–3556. [DOI](https://doi.org/10.1002/cpa.22196)
- **[SOTA]** J. Enders, R. Müller, P. Topping. *On type-I singularities in Ricci flow.* Communications in Analysis and Geometry 19 (2011), 905–922.
- **[SOTA]** D. Máximo. *On the blow-up of four-dimensional Ricci flow singularities.* Journal für die reine und angewandte Mathematik 692 (2014), 153–171.
- **[Survey]** J. Song, B. Weinkove. *An introduction to the Kähler–Ricci flow.* In: *An Introduction to the Kähler–Ricci Flow*, Lecture Notes in Mathematics 2086, Springer, 2013. [DOI](https://doi.org/10.1007/978-3-319-00819-6_3)
- **[Survey]** V. Tosatti. *KAWA lecture notes on the Kähler–Ricci flow.* Annales de la Faculté des Sciences de Toulouse 27 (2018), 285–376. [DOI](https://doi.org/10.5802/afst.1571)
- **[Survey]** N. Sesum, G. Tian. *Bounding scalar curvature and diameter along the Kähler–Ricci flow (after Perelman).* Journal of the Institute of Mathematics of Jussieu 7 (2008), 575–587. [DOI](https://doi.org/10.1017/s1474748008000133)

## 10. Worked Example: $X=\mathrm{Bl}_p\mathbb{P}^2$

Let $\pi:X\to\mathbb{P}^2$ be the blowup at one point, $H=\pi^*c_1(\mathcal{O}(1))$, $E$ the exceptional $(-1)$-curve. Intersection numbers: $H^2=1$, $H\cdot E=0$, $E^2=-1$. Then $c_1(X)=3H-E$, and $aH-bE$ is Kähler iff $a>b>0$.

Take $[\omega_0]=aH-bE$ with $a>b>0$. Then
$$[\omega(t)]=(a-3t)H-(b-t)E .$$
Kähler positivity requires $b-t>0$ and $(a-3t)-(b-t)>0$, so
$$T=\min\Big\{\,b,\ \tfrac{a-b}{2}\,\Big\}.$$
The volume is $\mathrm{Vol}(t)=(a-3t)^2-(b-t)^2$. Three regimes:

**(i) $a>3b$, so $T=b$.** At $t\to T$: $[\omega(T)]=(a-3b)H$, nef and big with $\mathrm{Vol}(T)=(a-3b)^2>0$, and $\mathrm{Null}(\alpha_T)=E$ since $\alpha_T\cdot E=0$. The flow shrinks $E$ to a point while converging smoothly on $X\setminus E$; Song–Weinkove show Gromov–Hausdorff convergence to $\mathbb{P}^2$ with a smooth restart. Concretely with $a=4,b=1$: $T=1$, $\mathrm{Vol}$ drops from $15$ to $1$. **Expected blowup model:** rescale by $(T-t)^{-1}$; the conjectural limit is the FIK shrinker on $\mathcal{O}(-1)\to\mathbb{P}^1$ — *unproved*, and Máximo's examples show a Type II alternative is not excluded a priori.

**(ii) $a<3b$, so $T=(a-b)/2$.** Then $a-3T=b-T=(3b-a)/2$, i.e. $\alpha_T=\tfrac{3b-a}{2}(H-E)$ with $(H-E)^2=0$: the class is nef but degenerate. $H-E$ is the fiber class of the ruling $X=\mathbb{F}_1\to\mathbb{P}^1$, so the flow **collapses the $\mathbb{P}^1$-fibers**, $\mathrm{Vol}(T)=0$, diameter stays bounded, and the limit is $\mathbb{P}^1$ with a metric of the Song–Tian generalized-Kähler–Einstein type. Example $a=2,b=1$: $T=1/2$.

**(iii) $a=3b$ (e.g. $[\omega_0]=3H-E=c_1(X)$).** Then $T=b=(a-b)/2$ and $[\omega(t)]=(1-t/b)(aH-bE)\to 0$: **finite-time extinction**, the whole manifold shrinks to a point. Rescaling by $(T-t)^{-1}$ gives the normalized flow on the Fano surface $X$. Since $\mathrm{Aut}(X)$ is non-reductive, $X$ admits **no** Kähler–Einstein metric (Matsushima), but it carries Koiso's shrinking Kähler–Ricci soliton, and the rescaled flow converges to it — the Fano instance of the Hamilton–Tian conjecture, here a theorem (Tian–Zhu; Chen–Sun–Wang).

Regime (iii) is fully solved, (ii) is solved, and (i) is solved at the level of Gromov–Hausdorff geometry but **open at the level of the rescaled blowup limit** — the smallest concrete instance of the general problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*