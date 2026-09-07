---
id: 03-geometry/generalized-calabi-conjecture
title: "Generalized Calabi Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Generalized Calabi Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/generalized-calabi-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Calabi's original conjecture (1954) asks: on a compact Kähler manifold $(X,\omega)$, is every representative of the first Chern class $c_1(X)$ the Ricci form of a unique Kähler metric in $[\omega]$? Yau proved this in 1976–78. The **generalized Calabi conjecture** is the surviving family of prescribed-volume/prescribed-Ricci problems obtained by dropping each of Yau's hypotheses in turn:

- **(G1) Non-Kähler (Gauduchon) case.** Given a compact complex manifold $X^n$ with a Hermitian metric and a smooth volume form $e^F\Omega$, does there exist a Gauduchon metric (i.e. $\partial\bar\partial\,\omega^{n-1}=0$) with that volume form? *Resolved affirmatively (Székelyhidi–Tosatti–Weinkove, 2017).*
- **(G2) Symplectic / almost-complex case (Donaldson, 2006).** Let $(M^4,\omega)$ be a compact symplectic 4-manifold with compatible almost-complex structure $J$, and let $\sigma$ be a volume form with $\int_M\sigma=\int_M\omega^2$. Does there exist a symplectic form $\tilde\omega$, cohomologous to $\omega$, taming $J$, with $\tilde\omega^2=\sigma$? **Open.**
- **(G3) Degenerate/singular case.** Does the Calabi problem remain solvable when $[\omega]$ is only nef or big (not Kähler), when $X$ is a normal variety with klt singularities, or when the right-hand side is merely $L^p$ or a measure? *Largely resolved; sharp regularity and diameter control still open.*
- **(G4) Complete non-compact case.** Which complete non-compact Kähler manifolds admit Ricci-flat metrics with prescribed volume form and prescribed asymptotics? **Open in general.**

A complete resolution of the generalized conjecture means: for each class, either an existence-and-uniqueness theorem with sharp regularity, or an explicit obstruction (a stability condition, a cohomological positivity failure, or a counterexample).

## 2. Mathematical Foundations

Let $X$ be a compact complex manifold of complex dimension $n$, $\omega$ a Hermitian $(1,1)$-form, in local coordinates $\omega = \sqrt{-1}\,g_{i\bar j}\,dz^i\wedge d\bar z^{\,j}$ with $(g_{i\bar j})$ positive definite Hermitian.

**Ricci form.** For $\omega$ Kähler, $\mathrm{Ric}(\omega) = -\sqrt{-1}\,\partial\bar\partial \log\det(g_{i\bar j})$, a closed real $(1,1)$-form with $[\mathrm{Ric}(\omega)] = 2\pi c_1(X)$.

**Calabi's problem as a Monge–Ampère equation.** Given $R\in 2\pi c_1(X)$, write $R - \mathrm{Ric}(\omega) = \sqrt{-1}\partial\bar\partial F$ by the $\partial\bar\partial$-lemma. Seeking $\tilde\omega = \omega + \sqrt{-1}\partial\bar\partial\varphi > 0$ with $\mathrm{Ric}(\tilde\omega)=R$ is equivalent to

$$(\omega + \sqrt{-1}\,\partial\bar\partial\varphi)^n = e^{F+c}\,\omega^n, \qquad \sup_X\varphi = 0,$$

with the normalization constant $c$ forced by $\int_X e^{F+c}\omega^n = \int_X\omega^n = [\omega]^n$. This is a fully nonlinear, second-order, degenerate-elliptic scalar PDE; the linearization at $\varphi$ is $\Delta_{\tilde\omega}$, so ellipticity holds exactly on the space of $\omega$-plurisubharmonic potentials $\mathrm{PSH}(X,\omega)$.

**Yau's theorem (1978).** For $\omega$ Kähler and $F\in C^\infty$, a unique smooth solution exists; the core is the a priori estimate $\|\varphi\|_{C^0}\le C(n,\omega,\|e^F\|_{L^{p}})$ for $p>1$, followed by $C^2$ and Calabi's third-order $S = |\nabla \tilde g|^2_{\tilde g}$ estimate, then Evans–Krylov/Schauder bootstrap.

**Gauduchon setting (G1).** Drop $d\omega=0$. A Gauduchon metric satisfies $\partial\bar\partial(\omega^{n-1})=0$; every conformal class on a compact complex $n$-fold contains one, unique up to scale (Gauduchon, 1977). The relevant equation, in the form used by Székelyhidi–Tosatti–Weinkove, is
$$\big(\omega_0^{\,n-1} + \tfrac{n-1}{2}\sqrt{-1}(\partial\bar\partial u\wedge\omega_0^{\,n-2}\ \text{terms})\big)^{\frac{n}{n-1}} = e^{F+b}\,\omega_0^{\,n},$$
i.e. a Monge–Ampère equation for $(n-1)$-plurisubharmonic functions (Fu–Wang–Wu form). No $\partial\bar\partial$-lemma is available, so the cohomological bookkeeping of the Kähler case disappears.

**Symplectic setting (G2).** With $J$ almost-complex and $\omega$ symplectic and $J$-compatible, write $\tilde\omega = \omega + d\alpha$ and split $\tilde\omega = \tilde\omega^{1,1} + (\tilde\omega^{2,0}+\tilde\omega^{0,2})$. The Calabi–Yau equation $\tilde\omega^2 = \sigma$ is elliptic in the $(1,1)$-part but the $(0,2)$-part is only controlled by $N_J$ (the Nijenhuis tensor); when $J$ is integrable, $\tilde\omega^{0,2}=0$ and the equation reduces to (2.1).

**Degenerate setting (G3).** For $[\theta]$ big and nef, one solves $(\theta + \sqrt{-1}\partial\bar\partial\varphi)^n = \mu$ in the Bedford–Taylor / non-pluripolar sense, with $\mu$ a positive measure of total mass $\mathrm{vol}([\theta])$ and finite energy.

## 3. History & State of the Art (SOTA)

- **1954–57.** Calabi announces the conjecture at the ICM and proves uniqueness (Calabi 1957); existence is reduced to the Monge–Ampère equation.
- **1976–78.** Yau proves existence for compact Kähler $X$ (CPAM 1978); Aubin independently settles the $c_1(X)<0$ Kähler–Einstein case, as does Yau. Corollaries: Ricci-flat Kähler (Calabi–Yau) metrics on $c_1=0$ manifolds, the Miyaoka–Yau inequality $c_1^2\le 3c_2$, and Bogomolov-type decomposition results.
- **1980–90.** Cheng–Yau and Tian–Yau extend to complete non-compact manifolds (quasi-projective, ALE, asymptotically conical).
- **1998.** Kołodziej proves $L^\infty$ bounds by pluripotential theory for $L^p$ ($p>1$) right-hand sides, decoupling the estimate from Yau's Moser iteration.
- **2009–10.** Eyssidieux–Guedj–Zeriahi solve singular Kähler–Einstein equations on klt varieties; Boucksom–Eyssidieux–Guedj–Zeriahi build Monge–Ampère theory in big classes.
- **2010.** Tosatti–Weinkove solve the Monge–Ampère equation on compact Hermitian manifolds (fixed $\omega$, prescribed volume form), removing the Kähler condition in the "fixed-metric" direction.
- **2015.** Chen–Donaldson–Sun prove the Yau–Tian–Donaldson conjecture for Fano manifolds: Kähler–Einstein $\iff$ K-polystability — the $c_1>0$ half of Calabi's program.
- **2017.** Székelyhidi–Tosatti–Weinkove prove the **Gauduchon conjecture** (G1) in all dimensions.
- **2021–24.** Chen–Cheng resolve cscK existence given properness of the Mabuchi functional; Guo–Phong–Tong give PDE-based (non-pluripotential) sharp $L^\infty$ estimates; Guo–Phong–Song–Sturm obtain uniform diameter and Green's function bounds.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| Compact Kähler, $[\omega]$ Kähler, $F\in C^\infty$, all $n$ | **Solved** (Yau 1978) |
| $c_1(X)<0$ and $c_1(X)=0$, Kähler–Einstein | **Solved** (Aubin, Yau 1978) |
| $c_1(X)>0$, Fano | **Solved conditionally**: K-polystability criterion (Chen–Donaldson–Sun 2015) |
| RHS in $L^p$, $p>1$; also RHS a measure of finite energy | **Solved** (Kołodziej 1998; Guedj–Zeriahi 2007) |
| $[\theta]$ nef and big, klt pairs, normal projective varieties | **Solved** in weak sense (EGZ 2009; BEGZ 2010) |
| Compact Hermitian, fixed metric, all $n$ | **Solved** (Tosatti–Weinkove 2010) |
| Gauduchon metric with prescribed volume form, all $n$ | **Solved** (Székelyhidi–Tosatti–Weinkove 2017) |
| Symplectic CY equation, $n=2$, $J$ integrable | **Solved** (reduces to Yau) |
| Symplectic CY equation, $M^4$ a $T^2$-bundle over $T^2$, $T^2$-invariant data | **Solved** (Weinkove; Fine; Tosatti–Weinkove 2011 for $T^2$-invariant $\sigma$) |
| Symplectic CY, general $(M^4,J)$ non-integrable | **Open** — a priori $C^0$ bound on the potential is the missing input |
| Complete non-compact: ALE, asymptotically conical, quasi-projective with ample $K_X$ | **Solved** (Cheng–Yau 1980; Tian–Yau 1990; Conlon–Hein 2013+) |
| Complete non-compact, general asymptotics | **Open** |
| Fu–Yau / Strominger system on non-Kähler CY 3-folds | **Solved** in the Goldstein–Prokushkin fibration case (Fu–Yau 2008); open in general |

## 5. Principal Obstacles

- **Loss of the $\partial\bar\partial$-lemma.** Outside the Kähler class, $[\mathrm{Ric}]$ carries no cohomological meaning and the ansatz $\tilde\omega=\omega+\sqrt{-1}\partial\bar\partial\varphi$ is not preserved. Non-Kähler problems must be posed for $(n-1)$-forms or with torsion terms, which destroys the concavity structure Evans–Krylov requires.
- **Failure of the maximum principle in the almost-complex case (G2).** Donaldson's equation is a system: the $(0,2)$-part $\tilde\omega^{0,2}$ is coupled to the $(1,1)$-part through $N_J$. Applying $\Delta$ to $\sup\varphi$ produces $N_J\ast\nabla\varphi$ terms with no sign, so Yau's $C^0$ estimate has no analogue. Donaldson's programme explicitly conjectures the $C^0$ bound and shows all higher estimates follow from it (Donaldson 2006; Tosatti–Weinkove–Yau 2008).
- **Degeneration of ellipticity in big/nef classes.** When $[\theta]^n>0$ but $\theta$ is not positive, $\tilde\omega$ degenerates along the non-Kähler locus; $C^2$ estimates blow up there and one only gets smoothness on a Zariski-open set. Whether the metric completion has bounded diameter or how singularities look metrically is not settled in general.
- **Nonlinear coupling in the Fano case.** For $c_1>0$ the equation becomes $(\omega+\sqrt{-1}\partial\bar\partial\varphi)^n = e^{F-\varphi}\omega^n$ with the *wrong* sign in $\varphi$; the maximum principle no longer bounds $\varphi$, and existence becomes an infinite-dimensional GIT/stability question rather than pure PDE.
- **No uniqueness mechanism off the Kähler cone.** Calabi's uniqueness proof uses integration by parts against $d\omega=0$. In the Gauduchon and symplectic settings, uniqueness of the solution is unknown.

## 6. The Gap

Precisely: Yau's method needs (i) a closed reference form so that potentials are scalar functions, and (ii) a concave, elliptic operator $\varphi\mapsto\log\det(g_{i\bar j}+\varphi_{i\bar j})$. Sections 4's positive results all restore one of these. The remaining gap is the class of problems where **neither** holds:

- **(G2) The $C^0$ estimate.** Donaldson's conjecture states: for $\tilde\omega$ solving $\tilde\omega^2=\sigma$ on $(M^4,J)$, $\|\varphi\|_{C^0}\le C(M,J,\omega,\sigma)$ with $C$ independent of the solution. This single a priori bound is equivalent (given TWY 2008's higher-order chain) to the full symplectic Calabi conjecture. No known technique produces it without integrability of $J$.
- **(G3) Sharp regularity.** Bridging weak (pluripotential) solutions in big classes to metric-space statements — bounded diameter, Gromov–Hausdorff limits identified with the algebraic singular model — remains partial despite Guo–Phong–Song–Sturm's diameter bounds.
- **(G4) Asymptotics.** No classification of admissible ends for complete Ricci-flat Kähler metrics.

## 7. Current Research (as of June 2026)

- **PDE-first $L^\infty$ estimates.** The Guo–Phong–Tong auxiliary-Monge–Ampère technique (Annals 2023) replaced pluripotential theory with a comparison-function argument, and has been pushed to Hermitian, parabolic, and $(n-1)$-form equations. Groups: Columbia (Phong), Rutgers, Northwestern (Tosatti, Weinkove). *(frontier — verify)* extensions to fully non-integrable settings are being attempted.
- **Symplectic Calabi–Yau.** Continued work on $T^2$-invariant and torus-fibred cases, and on Taubes' related "$SW\Rightarrow$Gr" circle of ideas linking $J$-holomorphic curve counts to the equation.
- **Non-Kähler Calabi–Yau and the Strominger system.** Fu–Yau equation generalizations, anomaly flow (Phong–Picard–Zhang), and hypersymplectic structures (Donaldson's hypersymplectic flow programme, Fine–Yao).
- **Stability side.** Post-CDS refinements: valuative stability, delta-invariants (Fujita–Odaka), and K-moduli constructions of Fano varieties; extension of YTD to cscK and extremal metrics after Chen–Cheng.
- **Metric geometry of degenerations.** Non-archimedean pluripotential theory (Boucksom–Jonsson) describing collapsing Calabi–Yau families and the SYZ picture.

## 8. Future Work

- Prove or disprove the $C^0$ estimate for the symplectic Calabi–Yau equation on $(M^4,J)$; a counterexample would need a family of solutions with unbounded potential but bounded volume form, plausibly on a non-Kähler symplectic 4-manifold with $b_1$ odd.
- Establish uniqueness for the Gauduchon prescribed-volume problem (STW's theorem gives existence only).
- Extend the Guo–Phong–Tong estimate machinery to the Nijenhuis-torsion setting, where the auxiliary equation currently has no analogue.
- Complete the classification of complete Ricci-flat Kähler metrics with Euclidean volume growth (Conlon–Hein programme) and connect it to the affine-variety side.
- Prove a YTD-type criterion for the existence of Kähler–Einstein metrics on singular Fano varieties in full generality, and identify the metric structure of the singularities.

## 9. Key References

- **[Foundational]** E. Calabi. *On Kähler manifolds with vanishing canonical class.* In *Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz*, Princeton University Press, 1957, pp. 78–89.
- **[Foundational]** S.-T. Yau. *On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I.* Communications on Pure and Applied Mathematics 31 (1978), 339–411.
- **[Foundational]** T. Aubin. *Équations du type Monge–Ampère sur les variétés kählériennes compactes.* Bulletin des Sciences Mathématiques 102 (1978), 63–95.
- **[Foundational]** S. Kołodziej. *The complex Monge–Ampère equation.* Acta Mathematica 180 (1998), 69–117.
- **[SOTA]** G. Székelyhidi, V. Tosatti, B. Weinkove. *Gauduchon metrics with prescribed volume form.* Acta Mathematica 219 (2017), 181–211.
- **[SOTA]** V. Tosatti, B. Weinkove. *The complex Monge–Ampère equation on compact Hermitian manifolds.* Journal of the AMS 23 (2010), 1187–1195.
- **[SOTA]** X.-X. Chen, S. Donaldson, S. Sun. *Kähler–Einstein metrics on Fano manifolds, I, II, III.* Journal of the AMS 28 (2015), 183–197, 199–234, 235–278.
- **[SOTA]** B. Guo, D. H. Phong, F. Tong. *On $L^\infty$ estimates for complex Monge–Ampère equations.* Annals of Mathematics 198 (2023), 393–418.
- **[SOTA]** X.-X. Chen, J. Cheng. *On the constant scalar curvature Kähler metrics (I), (II).* Journal of the AMS 34 (2021), 909–936, 937–1009.
- **[Key problem source]** S. K. Donaldson. *Two-forms on four-manifolds and elliptic equations.* In *Inspired by S. S. Chern*, Nankai Tracts in Mathematics 11, World Scientific, 2006, pp. 153–172.
- **[Partial results, G2]** V. Tosatti, B. Weinkove, S.-T. Yau. *Taming symplectic forms and the Calabi–Yau equation.* Proceedings of the London Mathematical Society 97 (2008), 401–424.
- **[Singular case]** P. Eyssidieux, V. Guedj, A. Zeriahi. *Singular Kähler–Einstein metrics.* Journal of the AMS 22 (2009), 607–639.
- **[Big classes]** S. Boucksom, P. Eyssidieux, V. Guedj, A. Zeriahi. *Monge–Ampère equations in big cohomology classes.* Acta Mathematica 205 (2010), 199–262.
- **[Non-compact]** G. Tian, S.-T. Yau. *Complete Kähler manifolds with zero Ricci curvature, I.* Journal of the AMS 3 (1990), 579–609.
- **[Non-Kähler CY]** J.-X. Fu, S.-T. Yau. *The theory of superstring with flux on non-Kähler manifolds and the complex Monge–Ampère equation.* Journal of Differential Geometry 78 (2008), 369–428.
- **[Survey]** D. H. Phong, J. Song, J. Sturm. *Complex Monge–Ampère equations.* Surveys in Differential Geometry 17 (2012), 327–411.
- **[Survey/Book]** V. Guedj, A. Zeriahi. *Degenerate Complex Monge–Ampère Equations.* EMS Tracts in Mathematics 26, 2017.
- **[Book]** G. Székelyhidi. *An Introduction to Extremal Kähler Metrics.* Graduate Studies in Mathematics 152, AMS, 2014.

## 10. Worked Example / Concrete Special Case

**Case A: $n=1$, exact solution.** Let $X = \mathbb{C}/\Lambda$ be an elliptic curve with flat metric $\omega = \sqrt{-1}\,dz\wedge d\bar z$, total area $A=\int_X\omega$. Here $\det(g_{i\bar j})$ is the single entry, and the Monge–Ampère equation collapses to the linear one:
$$\omega + \sqrt{-1}\partial\bar\partial\varphi = e^{F+c}\,\omega \iff \Delta\varphi = e^{F+c}-1,$$
with $\Delta$ the flat Laplacian (normalized so $\sqrt{-1}\partial\bar\partial\varphi = \tfrac12\Delta\varphi\cdot\omega$ up to constant). Solvability is exactly the Fredholm condition $\int_X (e^{F+c}-1)\,\omega = 0$, i.e.
$$e^{c} = \frac{A}{\int_X e^{F}\omega},$$
and the solution is unique up to an additive constant, fixed by $\sup\varphi=0$. Concretely, with $\Lambda = \mathbb{Z}+\mathbb{Z}i$, $A=1$, and $F(z)=\cos(2\pi x)$ where $z=x+iy$: expand $e^{\cos 2\pi x} = \sum_{k\in\mathbb{Z}} I_k(1)e^{2\pi i kx}$ (modified Bessel), so $e^{-c}=I_0(1)\approx 1.26607$, and
$$\varphi(x) = -\frac{1}{4\pi^2 I_0(1)}\sum_{k\neq 0}\frac{I_k(1)}{k^{2}}\,e^{2\pi i k x} + \text{const},$$
which converges absolutely since $I_k(1)$ decays like $1/(2^k k!)$. Every Fourier mode is invertible because the equation is linear — this is why $n=1$ is not representative.

**Case B: $n=2$, where the nonlinearity bites.** On $X=\mathbb{C}^2/\Lambda$ with $\omega=\sqrt{-1}\sum_{j=1}^2 dz^j\wedge d\bar z^{\,j}$, expand $\varphi=\varepsilon\psi + O(\varepsilon^2)$ and $F=\varepsilon f$. Using $(\omega+\sqrt{-1}\partial\bar\partial\varphi)^2 = \omega^2(1 + \Delta\varphi + \det(\varphi_{i\bar j})\cdot 2/\!\det g)$ one gets
$$\underbrace{\Delta\psi = f - \bar f}_{\text{order }\varepsilon}, \qquad \underbrace{\Delta\psi_2 = \tfrac12 f^2 - 2\det(\psi_{i\bar j}) - \text{const}}_{\text{order }\varepsilon^2},$$
where $\bar f$ is the mean of $f$. The quadratic term $\det(\psi_{i\bar j}) = \psi_{1\bar1}\psi_{2\bar2}-|\psi_{1\bar2}|^2$ is precisely the real Monge–Ampère nonlinearity; each order is solvable because the source has zero mean (Stokes), and the implicit function theorem gives openness of the set of solvable $F$ along the continuity path $(\omega+\sqrt{-1}\partial\bar\partial\varphi_t)^n = e^{tF+c_t}\omega^n$, $t\in[0,1]$. **Closedness** — not openness — is the whole content of Yau's theorem: one must bound $\|\varphi_t\|_{C^{2,\alpha}}$ uniformly in $t$, starting from $\|\varphi_t\|_{C^0}\le C$.

**Where (G2) breaks.** Repeat Case B on the same $T^4$ but with a non-integrable $J$ (say a small perturbation $J_\epsilon$ with $N_{J_\epsilon}\neq 0$) and unknown $\tilde\omega = \omega+d\alpha$. The order-$\varepsilon$ equation acquires the extra term $\langle N_J, \nabla\alpha\rangle$ which is first-order and not self-adjoint; the maximum principle applied to $\sup\alpha$ picks up an unsigned gradient term, and the uniform $C^0$ bound is lost. Tosatti–Weinkove proved the $T^2$-invariant version of this problem by exploiting the extra symmetry to kill the offending term — exactly the reduction that is unavailable in general.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*