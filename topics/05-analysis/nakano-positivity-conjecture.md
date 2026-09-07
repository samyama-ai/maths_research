---
id: 05-analysis/nakano-positivity-conjecture
title: "Nakano Positivity Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nakano Positivity Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/nakano-positivity-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a compact complex manifold of dimension $n$ and $E \to X$ a holomorphic vector bundle of rank $r$ that is **ample** in the sense of Hartshorne (i.e. $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ is an ample line bundle on the projectivized bundle).

**Conjecture (Nakano positivity form; Griffiths 1969, Demailly–Skoda 1980).**
If $E$ is ample, then $E \otimes \det E$ carries a smooth Hermitian metric whose Chern curvature is **Nakano positive**.

Two companion statements are part of the same problem cluster:

- **(G) Griffiths' conjecture.** $E$ ample $\Rightarrow$ $E$ admits a Griffiths positive metric.
- **(S) Strong form.** $E$ ample $\Rightarrow$ $S^k E \otimes \det E$ is Nakano positive for every $k \ge 0$.

Note that ampleness does **not** imply Nakano positivity of $E$ itself: $T_{\mathbb{P}^n}$ for $n \ge 2$ is ample but admits no Nakano positive metric (Section 10). The twist by $\det E$ is exactly what makes the statement plausible. By the Demailly–Skoda theorem, (G) $\Rightarrow$ the conjecture, and (G) $\Leftarrow$ the conjecture would follow if Nakano positivity of $E \otimes \det E$ could be untwisted; the two are known to be equivalent for $r=1$ and open in general.

A complete solution requires either (i) constructing, for every ample $E$, a metric $h$ on $E \otimes \det E$ with $\theta_{h} > 0$ in the Nakano sense, or (ii) exhibiting an ample $E$ for which no such metric exists — which by Nakano's vanishing theorem could in principle be done by a cohomological obstruction.

## 2. Mathematical Foundations

Let $(E,h)$ be a Hermitian holomorphic vector bundle with Chern connection $\nabla = \nabla^{1,0} + \bar\partial$ and curvature
$$\Theta_{E,h} \;=\; \nabla^2 \;=\; \sum_{1\le j,k\le n}\ \sum_{1\le\alpha,\beta\le r} \Theta_{j\bar k\alpha\bar\beta}\, dz_j \wedge d\bar z_k \otimes e_\alpha^* \otimes \overline{e_\beta^*},$$
with $\Theta_{j\bar k\alpha\bar\beta} = -\partial_j\partial_{\bar k} h_{\alpha\bar\beta} + \sum_{\gamma,\delta} h^{\gamma\bar\delta}\,\partial_j h_{\alpha\bar\delta}\,\partial_{\bar k} h_{\gamma\bar\beta}$ (Hermitian symmetry: $\overline{\Theta_{j\bar k\alpha\bar\beta}} = \Theta_{k\bar j\beta\bar\alpha}$). The associated Hermitian form on $T_X \otimes E$ is
$$\theta(u,u) \;=\; \sum_{j,k,\alpha,\beta} \Theta_{j\bar k\alpha\bar\beta}\, u^{j\alpha}\,\overline{u^{k\beta}}, \qquad u = \sum u^{j\alpha}\,\partial_j \otimes e_\alpha .$$

**Definitions.**
- $(E,h)$ is **Griffiths positive** if $\theta(\xi\otimes v,\xi\otimes v) > 0$ for all $\xi \in T_X\setminus\{0\}$, $v \in E\setminus\{0\}$ — positivity on **decomposable** tensors only.
- $(E,h)$ is **Nakano positive** if $\theta(u,u) > 0$ for all $u \in T_X\otimes E$, $u \ne 0$ — positivity on **all** tensors.
- $(E,h)$ is **dual Nakano positive** if $(E^*,h^*)$ is Nakano negative.

Hence Nakano $\Rightarrow$ Griffiths $\Rightarrow$ ample, and for $r=1$ all three coincide with $\Theta > 0$ (Kodaira). The first implication is strict: the obstruction is the cone of non-decomposable tensors in $T_X\otimes E$, of dimension $nr$ versus the $(n+r-1)$-dimensional decomposable cone.

**Nakano vanishing theorem.** If $(E,h)$ is Nakano positive on compact $X$, then
$$H^{q}\!\left(X, K_X \otimes E\right) = 0 \quad \text{for all } q \ge 1 .$$
**Griffiths/Le Potier vanishing.** If $E$ is Griffiths positive (or ample), $H^{q}(X, K_X\otimes E) = 0$ for $q\ge 1$ as well, but the stronger consequences of Nakano positivity — e.g. vanishing for $K_X\otimes S^kE$-type twists and the Demailly–Nadel machinery — are not available from Griffiths positivity alone.

**Demailly–Skoda theorem (1980).** If $(E,h)$ is Griffiths (semi)positive, then $(E\otimes\det E,\, h\otimes\det h)$ is Nakano (semi)positive. Explicitly, the curvature of the twist is
$$\widetilde\Theta_{j\bar k\alpha\bar\beta} \;=\; \Theta_{j\bar k\alpha\bar\beta} \;+\; \delta_{\alpha\beta}\sum_{\gamma}\Theta_{j\bar k\gamma\bar\gamma},$$
and the trace term dominates the non-decomposable directions.

## 3. History & State of the Art (SOTA)

- **1955.** Nakano introduces the strong curvature positivity notion and proves the vanishing theorem (*J. Math. Soc. Japan* 7).
- **1969.** Griffiths, in the Kodaira volume, introduces the weaker (decomposable) notion, proves ampleness of Griffiths positive bundles, and asks the converse. This is the origin of the problem.
- **1973.** Umemura proves ample $\Rightarrow$ Griffiths positive on compact Riemann surfaces.
- **1980.** Demailly and Skoda prove the twist theorem, converting (G) into the Nakano statement above.
- **1990.** Campana–Flenner give a second, cleaner proof of the curve case via a characterization of ample bundles on curves.
- **2007–2009.** Mourougane–Takayama and Berndtsson prove Nakano positivity for *direct image* bundles $f_*(K_{X/Y}\otimes L)$ with $L$ positively curved — the first large natural family where Nakano (not merely Griffiths) positivity is verified.
- **2013.** Liu–Sun–Yang extend Demailly–Skoda: $E$ Griffiths positive $\Rightarrow$ $S^kE\otimes\det E$ Nakano positive, plus associated vanishing theorems.
- **2020–2021.** Demailly proposes a nonlinear Hermitian–Yang–Mills-type system whose solvability would imply (G); Pingali and Naumann analyze the system in low rank.
- **2022–2023.** Deng–Ning–Wang–Zhou characterize Nakano and dual Nakano positivity by $L^p$-estimates for $\bar\partial$ / optimal $L^2$-extension, giving a functional-analytic reformulation independent of curvature computations.

No counterexample to any of (G), the conjecture, or (S) is known; no proof beyond $\dim X = 1$ or $r=1$ is known.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $r = 1$ (line bundles) | **Proved**; Nakano = Griffiths = $\Theta>0$ | Kodaira 1954 |
| $\dim_{\mathbb C} X = 1$, all $r$ | **Proved**: ample $\Rightarrow$ Griffiths positive, hence $E\otimes\det E$ Nakano positive | Umemura 1973; Campana–Flenner 1990 |
| $E$ Griffiths positive (any $X$, any $r$) | **Proved**: $E\otimes\det E$ and $S^kE\otimes\det E$ Nakano positive | Demailly–Skoda 1980; Liu–Sun–Yang 2013 |
| $E$ globally generated | Quotient metric from $\mathcal{O}^{\oplus N}$ is Griffiths semipositive; $E\otimes L$ Griffiths positive for $L$ positive | standard, Demailly CADG Ch. VII |
| $E = f_*(K_{X/Y}\otimes L)$, $L$ semipositive, $f$ smooth projective | **Proved** Nakano semipositive | Berndtsson 2009; Mourougane–Takayama 2007 |
| Direct sums $\bigoplus_i L_i$ with $L_i$ ample | **Proved** (Nakano positive directly) | elementary |
| Demailly's HYM system, rank $2$ over curves | Solvable; consistent with (G) | Pingali 2021 |
| Chern-class consequences (Fulton–Lazarsfeld positivity of Schur polynomials) | **Proved** for ample $E$; hence no numerical obstruction | Fulton–Lazarsfeld 1983 |

The last row is important negative evidence for a counterexample: every Chern-number inequality forced by Griffiths positivity is already known to hold for ample bundles.

## 5. Principal Obstacles

- **The decomposable/non-decomposable gap is a genuinely non-convex condition.** Griffiths positivity is positivity of a biquadratic form on a variety of rank-one tensors; Nakano positivity is positivity of a Hermitian matrix of size $nr$. Passing between them is the vector-bundle analogue of separating positive semidefinite from sum-of-squares biquadratic forms, a problem known to be NP-hard in the algebraic setting. There is no local pointwise algebraic implication.
- **Ampleness is a cohomological/asymptotic condition; positivity is pointwise.** Ampleness gives a positive metric on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$, i.e. a metric on $\mathcal{O}(1)$ whose curvature is positive on the total space of $\mathbb{P}(E^*)$. Pushing this down to a metric on $E$ requires a fibrewise averaging (a Finsler-to-Hermitian convexification). Every known averaging — the $L^2$/Bergman average over fibres — loses positivity in the horizontal-vertical mixed terms, precisely the terms that control non-decomposable tensors.
- **No PDE with a well-behaved existence theory.** Hermitian–Yang–Mills solves a trace equation and yields no pointwise curvature sign. Demailly's proposed system is a fully nonlinear, non-concave determinant-type system on $\mathrm{Herm}(E)$; the standard Evans–Krylov / continuity-method toolkit does not apply because the operator is neither elliptic-concave nor of Monge–Ampère type in the matrix variable.
- **Vanishing theorems cannot detect the difference in known examples.** The only proven obstruction to Nakano positivity is $H^q(X,K_X\otimes E)\ne 0$; after twisting by $\det E$, ampleness forces all such groups to vanish (Griffiths vanishing). So the natural source of counterexamples is closed off.
- **Curves are misleading.** In $\dim X = 1$ there are no non-decomposable tensors issues of the same severity ($n=1$ makes $T_X\otimes E$ automatically "decomposable"), so Nakano $=$ Griffiths there. The curve proofs use the classification of ample bundles on curves and do not survive to surfaces.

## 6. The Gap

Proven: (a) $\dim X = 1$ or $r=1$; (b) the implication Griffiths positive $\Rightarrow$ $E\otimes\det E$ Nakano positive (Demailly–Skoda), for *any* $X$, $r$.

Missing: the single step
$$E \text{ ample} \;\Longrightarrow\; E \text{ admits a Griffiths positive metric} \quad (\dim X \ge 2,\ r \ge 2),$$
or a direct construction of a Nakano positive metric on $E\otimes\det E$ bypassing Griffiths. Concretely, the gap is the construction of a Hermitian metric on $E$ from a positive metric $e^{-\varphi}$ on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ such that the resulting fibrewise-quadratic form has positive curvature on rank-one tensors. The unknown quantity is quantitative: no method currently controls the second fundamental form of the fibration $\mathbb{P}(E^*)\to X$ well enough to keep the Griffiths sign after averaging. Even the smallest open case — $X$ a smooth projective surface, $r = 2$, $E$ ample — is unresolved.

## 7. Current Research (as of June 2026)

- **Demailly's HYM programme.** Demailly (Institut Fourier, before 2022) reduced (G) to solvability of a coupled system whose solutions produce Griffiths positive metrics; the analytic existence theory remains open. Pingali (IISc Bangalore) established solvability in restricted rank/base settings. Continuation of this line is the most explicit PDE route. *(frontier — verify current status of higher-rank cases)*
- **$L^2$-characterizations of positivity.** Deng–Ning–Wang–Zhou (Sichuan / AMSS Beijing) characterize Nakano and dual Nakano positivity via $L^p$-estimates and optimal $L^2$-extension, allowing singular metrics; this converts the conjecture into a statement about solvability of $\bar\partial$ with prescribed constants.
- **Singular Hermitian metrics.** Hosono, Inayama, Raufi and collaborators study Nakano positivity for singular metrics, where curvature need not be a well-defined current; partial vanishing theorems of Demailly–Nadel–Nakano type exist (Inayama 2022).
- **Bergman-kernel / semiclassical asymptotics.** Finski and others use asymptotics of orthogonal Bergman kernels and Ohsawa–Takegoshi extension with sharp constants to characterize positivity of $E$ through $S^kE\otimes L^{\otimes k}$ as $k\to\infty$; an asymptotic version of Griffiths positivity is within reach, but the finite-$k$ statement is not. *(frontier — verify)*
- **Direct-image geometry.** Berndtsson-type complex Brunn–Minkowski methods continue to be the main engine for *proving* Nakano positivity in families; extending them to arbitrary ample bundles by realizing $E$ as a direct image is an active but unfinished strategy.

## 8. Future Work

- Solve the surface, rank-2 case: classify ample rank-2 bundles on $\mathbb{P}^2$ (e.g. $T_{\mathbb{P}^2}$, twisted null-correlation-type bundles) and construct Griffiths positive metrics case by case.
- Develop an existence theory for Demailly's nonlinear system: identify a concavity substitute or a variational formulation (a functional whose critical points are Griffiths positive metrics).
- Search for obstructions beyond vanishing theorems: e.g. sharper Chern-form (not Chern-number) inequalities valid for Griffiths positive metrics but not implied by ampleness, extending Fulton–Lazarsfeld to the level of forms (Pingali's representability results).
- Settle the untwisting question: does Nakano positivity of $E\otimes\det E$ imply Griffiths positivity of $E$? A positive answer makes the two conjectures literally equivalent.
- Use $L^2$-characterizations to attack the conjecture through Hörmander estimates with optimal constants on $\mathbb{P}(E^*)$.

## 9. Key References

- **[Foundational]** S. Nakano. *On complex analytic vector bundles.* J. Math. Soc. Japan **7** (1955), 1–12.
- **[Foundational]** P. A. Griffiths. *Hermitian differential geometry, Chern classes, and positive vector bundles.* In: Global Analysis (Papers in Honor of K. Kodaira), Princeton Univ. Press, 1969, 185–251.
- **[Foundational]** J.-P. Demailly, H. Skoda. *Relations entre les notions de positivités de P. A. Griffiths et de S. Nakano pour les fibrés vectoriels.* Séminaire P. Lelong–H. Skoda (Analyse), Lecture Notes in Math. **822**, Springer, 1980, 304–309.
- **[Partial result]** H. Umemura. *Some results in the theory of vector bundles.* Nagoya Math. J. **52** (1973), 97–128.
- **[Partial result]** F. Campana, H. Flenner. *A characterization of ample vector bundles on a curve.* Math. Ann. **287** (1990), 571–575.
- **[Structural]** W. Fulton, R. Lazarsfeld. *Positive polynomials for ample vector bundles.* Ann. of Math. **118** (1983), 35–60.
- **[SOTA]** B. Berndtsson. *Curvature of vector bundles associated to holomorphic fibrations.* Ann. of Math. **169** (2009), 531–560.
- **[SOTA]** C. Mourougane, S. Takayama. *Hodge metrics and positivity of direct images.* J. Reine Angew. Math. **606** (2007), 167–178.
- **[SOTA]** K. Liu, X. Sun, X. Yang. *Positivity and vanishing theorems for ample vector bundles.* J. Algebraic Geom. **22** (2013), 303–331.
- **[SOTA]** J.-P. Demailly. *Hermitian–Yang–Mills approach to the conjecture of Griffiths on the positivity of ample vector bundles.* Sbornik: Mathematics **212** (2021), 305–318.
- **[SOTA]** V. P. Pingali. *A note on Demailly's approach towards a conjecture of Griffiths.* C. R. Math. Acad. Sci. Paris **359** (2021), 501–503.
- **[SOTA]** F. Deng, J. Ning, Z. Wang, X. Zhou. *Positivity of holomorphic vector bundles in terms of $L^p$-estimates for $\bar\partial$.* Math. Ann. **385** (2023), 575–607.
- **[Recent]** T. Inayama. *Nakano positivity of singular Hermitian metrics and vanishing theorems of Demailly–Nadel–Nakano type.* Algebraic Geometry (Foundation Compositio), 2022.
- **[Survey/Book]** J.-P. Demailly. *Complex Analytic and Differential Geometry.* OpenContent book, Institut Fourier (Chapters VII, X).
- **[Book]** S. Kobayashi. *Differential Geometry of Complex Vector Bundles.* Princeton University Press / Iwanami Shoten, 1987.

## 10. Worked Example / Concrete Special Case

**$E = T_{\mathbb{P}^n}$ with the Fubini–Study metric.** Fix $x\in\mathbb{P}^n$ and normal coordinates in which $\omega_{FS}(x) = \sqrt{-1}\sum_j dz_j\wedge d\bar z_j$. The curvature of $T_{\mathbb{P}^n}$ at $x$ is
$$\Theta_{j\bar k\alpha\bar\beta} \;=\; \delta_{jk}\delta_{\alpha\beta} \;+\; \delta_{j\beta}\delta_{k\alpha}, \qquad 1\le j,k,\alpha,\beta\le n .$$

*Griffiths positivity.* For $u = \xi\otimes v$, i.e. $u^{j\alpha} = \xi^j v^\alpha$:
$$\theta(u,u) = |\xi|^2|v|^2 + \Big|\textstyle\sum_j \xi^j \overline{v^j}\Big|^2 \;\ge\; |\xi|^2|v|^2 \;>\; 0 .$$
So $T_{\mathbb{P}^n}$ is Griffiths positive.

*Failure of Nakano positivity.* Identify $u$ with the matrix $U = (u^{j\alpha})$. Then
$$\theta(u,u) \;=\; \|U\|^2 + \sum_{j,\alpha} u^{j\alpha}\overline{u^{\alpha j}} \;=\; \|U\|^2 + \operatorname{tr}\!\big(U\,\overline{U}\big).$$
Take $n \ge 2$ and $U$ antisymmetric, $u^{j\alpha} = -u^{\alpha j}$, e.g. $U = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$ padded with zeros. Then $\operatorname{tr}(U\overline{U}) = \sum_{j,\alpha} u^{j\alpha}\overline{u^{\alpha j}} = -\sum_{j,\alpha}|u^{j\alpha}|^2 = -\|U\|^2$, so $\theta(u,u) = 0$ with $u \ne 0$. The Fubini–Study metric is Nakano semipositive but not positive.

*This is not an artifact of the metric.* Since $\Omega^{n}_{\mathbb{P}^n}\otimes T_{\mathbb{P}^n}\cong\Omega^{n-1}_{\mathbb{P}^n}$,
$$H^{n-1}\big(\mathbb{P}^n, K_{\mathbb{P}^n}\otimes T_{\mathbb{P}^n}\big) \cong H^{n-1}\big(\mathbb{P}^n,\Omega^{n-1}_{\mathbb{P}^n}\big) \cong \mathbb{C} \neq 0,$$
so by Nakano's vanishing theorem **no** metric on $T_{\mathbb{P}^n}$ ($n\ge 2$) is Nakano positive, even though $T_{\mathbb{P}^n}$ is ample.

*The twist repairs it.* $\det T_{\mathbb{P}^n} = \mathcal{O}(n+1)$ has induced curvature $(n+1)\delta_{jk}$ at $x$, so for $E\otimes\det E$:
$$\widetilde\theta(u,u) = \|U\|^2 + \operatorname{tr}(U\overline U) + (n+1)\|U\|^2 \;\ge\; (n+2)\|U\|^2 - \|U\|^2 = (n+1)\|U\|^2 > 0,$$
using $|\operatorname{tr}(U\overline U)| \le \|U\|^2$ (Cauchy–Schwarz). So $T_{\mathbb{P}^n}\otimes\mathcal{O}(n+1)$ is Nakano positive, exactly as Demailly–Skoda predicts.

The conjecture asserts this last computation is universal. The obstruction to proving it is that for a general ample $E$ we have no Griffiths positive metric to start from — the input $\Theta_{j\bar k\alpha\bar\beta} = \delta_{jk}\delta_{\alpha\beta}+\delta_{j\beta}\delta_{k\alpha}$, available here by homogeneity, has no substitute.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*