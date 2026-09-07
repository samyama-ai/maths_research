---
id: 03-geometry/griffiths-conjecture
title: "Griffiths Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Griffiths Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/griffiths-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a compact complex manifold and $E \to X$ a holomorphic vector bundle of rank $r$. Recall that $E$ is **ample** in the sense of Hartshorne if the tautological line bundle $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ on the projectivized bundle of lines is ample.

**Conjecture (Griffiths, 1969).** $E$ is ample if and only if $E$ carries a smooth Hermitian metric $h$ whose Chern curvature $\Theta_{E,h}$ is **Griffiths positive**.

One direction is elementary: Griffiths positivity implies ampleness, because a Griffiths-positive metric on $E$ induces a positively curved metric on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$, and Kodaira's theorem applies. The open content is the converse:

> If $E$ is ample, does there exist $h$ with $\Theta_{E,h} >_{\mathrm{Gr}} 0$?

A complete solution requires either (i) a construction, for every ample $E$ on every compact complex (or at least projective) manifold, of a metric with pointwise Griffiths-positive curvature, or (ii) an explicit ample bundle admitting no such metric. Note that ampleness is a cohomological/algebraic condition invariant under twist and pullback, while Griffiths positivity is a pointwise differential-geometric condition on a tensor: the conjecture asserts these coincide.

A second statement also called the Griffiths conjecture — that all Schur polynomials in the Chern **forms** of a Griffiths-positive bundle are positive $(p,p)$-forms — is discussed in §4 and §7; it is a refinement of the Fulton–Lazarsfeld cohomological positivity theorem.

## 2. Mathematical Foundations

Let $(E,h)$ be a Hermitian holomorphic bundle on $X$, $\dim_{\mathbb C} X = n$, $\operatorname{rk} E = r$. The Chern connection $\nabla = \nabla^{1,0} + \bar\partial$ is the unique $h$-unitary connection with $(0,1)$-part $\bar\partial$. Its curvature $\Theta_{E,h} = \nabla^2 \in C^\infty(X, \Lambda^{1,1}T^*_X \otimes \operatorname{End} E)$ is, in local holomorphic coordinates $(z_1,\dots,z_n)$ and a local frame $(e_1,\dots,e_r)$,

$$\Theta_{E,h} \;=\; \sum_{1\le j,k\le n}\;\sum_{1\le \alpha,\beta\le r} \Theta_{j\bar k\alpha\bar\beta}\, dz_j \wedge d\bar z_k \otimes e^*_\alpha \otimes e_\beta ,
\qquad \Theta_{j\bar k \alpha\bar\beta} = -\frac{\partial^2 h_{\alpha\bar\beta}}{\partial z_j \partial \bar z_k} + \sum_{\gamma,\delta} h^{\gamma\bar\delta}\frac{\partial h_{\alpha\bar\delta}}{\partial z_j}\frac{\partial h_{\gamma\bar\beta}}{\partial \bar z_k}.$$

The curvature defines a Hermitian form $\tilde\Theta$ on $T_X \otimes E$:
$$\tilde\Theta(\tau,\tau) \;=\; \sum_{j,k,\alpha,\beta} \Theta_{j\bar k\alpha\bar\beta}\, \tau^{j\alpha}\overline{\tau^{k\beta}}, \qquad \tau = \sum \tau^{j\alpha}\, \partial/\partial z_j \otimes e_\alpha .$$

* **Griffiths positive**, $\Theta >_{\mathrm{Gr}} 0$: $\tilde\Theta(\tau,\tau)>0$ for all nonzero **decomposable** $\tau = v\otimes\xi$, i.e. $\sum \Theta_{j\bar k\alpha\bar\beta} v^j\bar v^k \xi^\alpha\bar\xi^\beta > 0$ for all $0\ne v\in T_{X,x}$, $0\ne \xi\in E_x$.
* **Nakano positive**, $\Theta >_{\mathrm{Nak}} 0$: $\tilde\Theta(\tau,\tau)>0$ for **all** nonzero $\tau \in T_{X,x}\otimes E_x$.
* **Dual Nakano positive**: $\Theta_{E^*,h^*} <_{\mathrm{Nak}} 0$.

Hence $\text{Nakano} \Rightarrow \text{Griffiths} \Rightarrow \text{ample}$, and for $r=1$ all three coincide with $c_1(E)>0$ (Kodaira). For $r\ge 2$ Griffiths $\not\Rightarrow$ Nakano (see §10).

Two structural theorems anchor the subject:

* **Demailly–Skoda (1980).** If $\Theta_{E,h} >_{\mathrm{Gr}} 0$ then $E \otimes \det E$ is Nakano positive. So the gap between the two positivities is bounded by one determinant twist.
* **Fulton–Lazarsfeld (1983).** If $E$ is ample, then for every Schur polynomial $s_\lambda$ of weight $p\le n$, $\int_X s_\lambda(c(E))\wedge \alpha > 0$ for effective cycle classes; i.e. all *cohomology* Schur classes are numerically positive. Griffiths' finer question asks whether $s_\lambda(\Theta_{E,h})$ is a positive **form** when $h$ is Griffiths positive.

## 3. History & State of the Art (SOTA)

Phillip Griffiths raised the question in *Hermitian differential geometry, Chern classes, and positive vector bundles* (in *Global Analysis: Papers in Honor of K. Kodaira*, Princeton Univ. Press, 1969), where the metric notion of positivity now bearing his name was introduced alongside Nakano's earlier notion (Nakano, 1955). Hartshorne's algebraic theory of ample bundles (*Ample vector bundles*, Publ. IHÉS 29, 1966) supplied the other half of the comparison.

Milestones:

* 1973: Umemura established metric positivity results for ample bundles on curves.
* 1980: Demailly–Skoda prove Griffiths $\Rightarrow$ $E\otimes\det E$ Nakano positive.
* 1983: Fulton–Lazarsfeld settle the cohomological positivity of Schur polynomials for ample $E$ (Ann. of Math. 118).
* 1990: Campana–Flenner prove the conjecture for $\dim X = 1$ (Math. Ann. 287): on a compact Riemann surface, $E$ ample $\iff$ $E$ admits a Griffiths-positive metric.
* 2009: Berndtsson's Nakano positivity of direct images (Ann. of Math. 169) supplies a large supply of genuinely Nakano-positive bundles and a new mechanism for producing curvature positivity.
* 2020–21: Demailly proposes a Hermitian–Yang–Mills scheme on flag bundles reducing the conjecture to solvability of a nonlinear elliptic system; Naumann and others analyze it.
* 2021–2024: the *Schur-form* variant is resolved affirmatively in significant generality (see §4, §7).

State of the art: the conjecture is **open for every $\dim X \ge 2$ and every rank $r \ge 2$**, with no counterexample candidate and no general construction.

## 4. Partial Results / Verified Cases

* **Line bundles ($r=1$), any $n$:** true; it is exactly the Kodaira embedding theorem.
* **Curves ($n=1$), any rank $r$:** proved. Campana–Flenner (1990) construct Griffiths-positive metrics on ample bundles over compact Riemann surfaces, building on Narasimhan–Seshadri/Donaldson theory and Umemura's earlier work. On a curve, ample $\Leftrightarrow$ every quotient has positive degree, and stable-bundle deformation arguments apply.
* **Direct-image bundles:** if $p: \mathcal{X} \to X$ is a smooth fibration with relative canonical $K_{\mathcal{X}/X}$ and $L$ a positively curved line bundle, then $p_*(K_{\mathcal{X}/X}\otimes L)$ is Nakano semipositive (Berndtsson 2009), hence Griffiths semipositive; Mourougane–Takayama give algebraic analogues.
* **Twists:** if $E$ is ample and globally generated, $E$ carries a Griffiths semipositive metric (pull back the Fubini–Study metric under $X\to \mathrm{Gr}$); positivity of the twist $E\otimes A$ for $A$ a sufficiently positive line bundle then follows. Ample $E$ becomes Griffiths positive after tensoring with a suitable ample line bundle — this is the elementary "$\varepsilon$-room" case.
* **Homogeneous/equivariant bundles:** for $X = G/P$ and $E$ homogeneous, invariant metrics are finite-dimensional objects and the equivalence can be checked directly (e.g. $T_{\mathbb{P}^n}$, $\mathcal{O}(a)\oplus\mathcal{O}(b)$ with $a,b>0$, Schwarzenberger/null-correlation twists).
* **Schur-form variant:** Guler (Canad. Math. Bull. 55, 2012) proved that all Segre forms of a Griffiths-positive bundle are positive; Diverio (Math. Z. 2016) refined the picture; more recently the full positivity of Schur forms $s_\lambda(\Theta_{E,h})$ for Griffiths-positive $E$ has been established *(frontier — verify)* by Finski and independently in the work of Ross–Toma.

## 5. Principal Obstacles

* **No canonical metric to construct.** Ampleness gives sections of $\mathcal{O}_{\mathbb{P}(E^*)}(k)$, hence metrics on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ with positive curvature; but a positively curved metric on the tautological line bundle descends to a Griffiths-positive metric on $E$ **only if it is fiberwise a Hermitian (quadratic) metric**. Bergman-type constructions from sections produce metrics that are fiberwise homogeneous of the right degree but *not* quadratic, i.e. Finsler rather than Hermitian. Converting Finsler positivity to Hermitian positivity is the central unresolved step.
* **Failure of averaging.** Griffiths positivity is not convex in $h$ in an obvious way, and the natural averaging/geodesic operations in the space of metrics ($h_t = h_0^{1-t}h_1^t$ along Mabuchi-type geodesics) preserve only weaker curvature conditions.
* **Non-linearity and lack of an elliptic equation.** Unlike the Hermitian–Yang–Mills equation, whose solvability is governed by slope stability (Donaldson–Uhlenbeck–Yau), Griffiths positivity is an open pointwise inequality with no associated variational functional whose critical points automatically satisfy it. Demailly's flag-bundle HYM system is an attempt to supply one; its a priori estimates are not known.
* **Rank–dimension interaction.** For $n\ge 2$ the curvature tensor has $n^2r^2$ components constrained only on the Segre cone of decomposable tensors, a non-convex algebraic variety; positivity there is not a semidefinite condition and standard convexity/SDP machinery does not apply.
* **Deformation invariance fails.** Ampleness is open and deformation-stable; Griffiths positivity is also open, but there is no known compactness result letting one pass to limits of "almost Griffiths-positive" metrics.

## 6. The Gap

Proven: $\text{Griffiths} \Rightarrow \text{ample}$ (all $n,r$); $\text{ample} \Rightarrow \text{Griffiths}$ for $r=1$ and for $n=1$; ample $\Rightarrow$ Griffiths positive *after* twisting by an ample line bundle.

Missing: for $n\ge 2$, $r\ge 2$, an untwisted construction. Concretely, the gap is the implication

$$\Big\{\ \mathcal{O}_{\mathbb{P}(E^*)}(1) \text{ carries } \varphi \text{ with } i\partial\bar\partial\varphi>0 \ \Big\} \;\Longrightarrow\; \Big\{\ \exists\ \varphi \text{ as above that is fiberwise a Hermitian norm } \Big\}.$$

Equivalently: does the space of positively curved *Finsler* metrics on $E$ retract onto (or nonempty-intersect) the space of positively curved *Hermitian* metrics? Every known approach either loses fiberwise quadraticity (Bergman kernels, $L^2$-extension) or loses strict positivity (symmetrization, Demailly–Skoda-type twists).

## 7. Current Research (as of June 2026)

* **Demailly's HYM programme.** Demailly, *Hermitian–Yang–Mills approach to the conjecture of Griffiths on the positivity of ample vector bundles* (2020–21), lifts the problem to the flag bundle $\mathrm{Fl}(E)\to X$ and seeks a family of HYM-type equations whose solutions descend to Griffiths-positive metrics; existence hinges on a priori estimates for a degenerate elliptic system. Active in Grenoble/IF and among his former students.
* **Naumann's analysis** of the associated nonlinear system, clarifying the obstruction terms and establishing solvability in low rank / special geometry *(frontier — verify)*.
* **Schur- and Segre-form positivity.** Finski's $L^2$/Bergman methods and Ross–Toma's Hodge–Riemann bilinear relations for Schur classes of ample bundles have essentially closed the "positivity of Chern forms" version of Griffiths' question and generate new pointwise inequalities usable as necessary conditions on a hypothetical Griffiths metric *(frontier — verify)*.
* **Berndtsson-school complex Brunn–Minkowski methods** (Berndtsson, Păun, Lempert, Hosono–Inayama) producing Nakano/dual-Nakano positivity from plurisubharmonic variation; Inayama's dual-Nakano results give the sharpest known bridges between the positivity notions.
* **Vector-bundle Monge–Ampère equations** (Pingali, IISc Bangalore) as a substitute canonical equation whose solutions are candidate Griffiths-positive metrics.

## 8. Future Work

* Solve the conjecture on surfaces ($n=2$) for rank $2$: the smallest genuinely open case, where the Segre cone is a quadric and explicit curvature algebra is tractable.
* Symmetrization: find an operator taking a positively curved Finsler metric to a Hermitian one preserving strict positivity — e.g. via fiberwise Bergman kernels of $\mathcal{O}(k)$ restricted to fibers, controlling the error in $k^{-1}$.
* Remove the twist in Demailly–Skoda: decide whether ample $\Rightarrow$ $E\otimes\det E$ Nakano positive, an intermediate statement strictly weaker than the conjecture but currently also open.
* Search for counterexamples among bundles with large discriminant on surfaces of general type, using Kobayashi–Lübke-type inequalities as pointwise obstructions.
* Extend the curve proof: understand which Narasimhan–Seshadri-type deformation argument can survive in higher dimension, where stability is only a numerical, not a pointwise, condition.

## 9. Key References

- **[Foundational]** P. A. Griffiths. *Hermitian differential geometry, Chern classes, and positive vector bundles.* In *Global Analysis: Papers in Honor of K. Kodaira*, Princeton University Press, 1969, pp. 185–251.
- **[Foundational]** R. Hartshorne. *Ample vector bundles.* Publications Mathématiques de l'IHÉS 29 (1966), 63–94.
- **[Foundational]** S. Nakano. *On complex analytic vector bundles.* Journal of the Mathematical Society of Japan 7 (1955), 1–12.
- **[Foundational]** J.-P. Demailly, H. Skoda. *Relations entre les notions de positivité de P. A. Griffiths et de S. Nakano pour les fibrés vectoriels.* Séminaire P. Lelong–H. Skoda 1978/79, Lecture Notes in Math. 822, Springer, 1980, 304–309.
- **[Key partial result]** F. Campana, H. Flenner. *A characterization of ample vector bundles on a curve.* Mathematische Annalen 287 (1990), 571–575.
- **[Key partial result]** W. Fulton, R. Lazarsfeld. *Positive polynomials for ample vector bundles.* Annals of Mathematics 118 (1983), 35–60.
- **[SOTA / Recent]** B. Berndtsson. *Curvature of vector bundles associated to holomorphic fibrations.* Annals of Mathematics 169 (2009), 531–560.
- **[SOTA / Recent]** J.-P. Demailly. *Hermitian–Yang–Mills approach to the conjecture of Griffiths on the positivity of ample vector bundles.* Sbornik: Mathematics 212 (2021).
- **[SOTA / Recent]** D. Guler. *On Segre forms of positive vector bundles.* Canadian Mathematical Bulletin 55 (2012), 108–113.
- **[SOTA / Recent]** S. Diverio. *Segre forms and Kobayashi–Lübke inequality.* Mathematische Zeitschrift 283 (2016), 1033–1047.
- **[SOTA / Recent]** V. P. Pingali. *Representability of Chern–Weil forms.* Mathematische Zeitschrift 288 (2018), 629–641.
- **[Survey]** R. Lazarsfeld. *Positivity in Algebraic Geometry II: Positivity for Vector Bundles, and Multiplier Ideals.* Ergebnisse der Mathematik 49, Springer, 2004 (Chapter 6).
- **[Survey]** J.-P. Demailly. *Complex Analytic and Differential Geometry.* Open-access book manuscript, Institut Fourier (Chapter VII).

## 10. Worked Example / Concrete Special Case

**$E = T_{\mathbb{P}^n}$ with the Fubini–Study metric: Griffiths positive, not Nakano positive.**

Take $X=\mathbb{P}^n$ with the FS metric $\omega_{FS}$, and $E = T_{\mathbb{P}^n}$, which is ample (Mori). Fix $x_0=[1:0:\cdots:0]$ and normal coordinates $(z_1,\dots,z_n)$ at $x_0$ with $h_{j\bar k}(x_0)=\delta_{jk}$. A classical computation (from the Euler sequence $0\to\mathcal{O}\to\mathcal{O}(1)^{n+1}\to T_{\mathbb{P}^n}\to 0$) gives, at $x_0$, curvature components

$$\Theta_{j\bar k\alpha\bar\beta} \;=\; \delta_{jk}\delta_{\alpha\beta} \;+\; \delta_{j\beta}\delta_{k\alpha}, \qquad 1\le j,k,\alpha,\beta\le n .$$

*Griffiths test.* For $\tau = v\otimes\xi$ decomposable,
$$\tilde\Theta(v\otimes\xi,v\otimes\xi) = \sum_{j,k,\alpha,\beta}(\delta_{jk}\delta_{\alpha\beta}+\delta_{j\beta}\delta_{k\alpha}) v^j\bar v^k\xi^\alpha\bar\xi^\beta = |v|^2|\xi|^2 + \Big|\sum_j v^j\bar\xi^{\,j}\Big|^2 \;\ge\; |v|^2|\xi|^2 > 0 .$$
So $T_{\mathbb{P}^n}$ is Griffiths positive, consistent with the conjecture.

*Nakano test.* Let $n\ge 2$ and take the antisymmetric tensor $\tau$ with matrix $\tau^{j\alpha}$ satisfying $\tau^{j\alpha}=-\tau^{\alpha j}$, e.g. $\tau = \partial_1\otimes e_2 - \partial_2\otimes e_1$. Then
$$\tilde\Theta(\tau,\tau)=\sum_{j,\alpha}|\tau^{j\alpha}|^2 + \sum_{j,\alpha}\tau^{j\alpha}\overline{\tau^{\alpha j}} = \|\tau\|^2 - \|\tau\|^2 = 0 .$$
Hence the FS metric is Nakano semipositive but **not** Nakano positive; in fact $T_{\mathbb{P}^n}$ admits no Nakano-positive metric for $n\ge2$ (by Nakano vanishing it would force $H^{n-1,n}$-type vanishing violated by $H^{n-1}(\mathbb{P}^n,\Omega^{n-1}\otimes\ldots)$ considerations).

*What the example shows.* Ampleness cannot be equivalent to Nakano positivity — the strongest curvature notion is too strong. Griffiths positivity is the exact candidate: it is weak enough to be satisfied here and, by Demailly–Skoda, strong enough that $T_{\mathbb{P}^n}\otimes\det T_{\mathbb{P}^n} = T_{\mathbb{P}^n}(n+1)$ is Nakano positive. The conjecture asks whether the pattern seen in this homogeneous example — where the invariant metric is handed to us by symmetry — persists when no symmetry is available to produce the metric.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*