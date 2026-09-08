---
id: 05-analysis/griffiths-positivity-conjecture
title: "Griffiths Positivity Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Griffiths Positivity Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/griffiths-positivity-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a compact complex manifold and $E \to X$ a holomorphic vector bundle of rank $r$. Two notions of positivity compete:

- **Algebraic:** $E$ is *ample* (Hartshorne) if the tautological line bundle $\mathcal{O}_{\mathbb{P}(E)}(1)$ on the projectivized bundle of hyperplanes is ample.
- **Differential-geometric:** $E$ is *Griffiths positive* if it carries a smooth Hermitian metric $h$ whose Chern curvature $\Theta_{E,h}$ is positive in the Griffiths sense (definition in §2).

**Conjecture (Griffiths, 1969).** $E$ is ample $\iff$ $E$ is Griffiths positive.

The implication ($\Leftarrow$) is a theorem. The open direction is

$$E \text{ ample} \;\Longrightarrow\; \exists\, h \text{ smooth Hermitian with } \Theta_{E,h} >_{\mathrm{Gr}} 0 .$$

A complete proof must, given an ample $E$, *construct* (or prove existence of) such an $h$ on an arbitrary projective manifold $X$ of arbitrary dimension and arbitrary rank $r \ge 2$. A disproof requires an ample bundle admitting no Griffiths-positive metric — necessarily $\dim X \ge 2$, $r \ge 2$.

A companion statement, also due to Griffiths and also open in general, is the **Chern-form positivity conjecture**: if $(E,h)$ is Griffiths positive then for every Schur polynomial $P$ of weighted degree $k$, the differential form $P(c_1(E,h),\dots,c_k(E,h))$ is a positive $(k,k)$-form pointwise, not merely a positive cohomology class.

## 2. Mathematical Foundations

Let $(E,h)$ be Hermitian holomorphic, $\nabla = \nabla^{1,0} + \bar\partial$ the Chern connection, and
$$\Theta_{E,h} = \nabla^2 \in C^\infty\big(X, \Lambda^{1,1}T_X^* \otimes \mathrm{End}(E)\big).$$
In local holomorphic coordinates $(z_1,\dots,z_n)$ on $X$ and a local frame $(e_1,\dots,e_r)$ of $E$,
$$\Theta_{E,h} = \sum_{j,k,\lambda,\mu} c_{jk\lambda\mu}\, dz_j \wedge d\bar z_k \otimes e_\lambda^* \otimes e_\mu, \qquad
c_{jk\lambda\mu} = \overline{c_{kj\mu\lambda}} .$$
Set the associated Hermitian form on $T_X \otimes E$:
$$\widetilde\Theta(u,u) \;=\; \sum_{j,k,\lambda,\mu} c_{jk\lambda\mu}\, u_{j\lambda}\,\overline{u_{k\mu}}, \qquad u = \sum u_{j\lambda}\, \tfrac{\partial}{\partial z_j}\otimes e_\lambda .$$

- **Griffiths positive** ($\Theta >_{\mathrm{Gr}} 0$): $\widetilde\Theta(u,u) > 0$ for all nonzero *decomposable* tensors $u = \xi \otimes s$, $\xi \in T_{X,x}\setminus\{0\}$, $s \in E_x\setminus\{0\}$, i.e. $\sum c_{jk\lambda\mu}\xi_j\bar\xi_k s_\lambda \bar s_\mu > 0$.
- **Nakano positive** ($\Theta >_{\mathrm{Nak}} 0$): $\widetilde\Theta(u,u) > 0$ for *all* nonzero $u \in T_{X,x}\otimes E_x$.
- **Dual Nakano positive**: $(E^*,h^*)$ is Nakano negative.

Hence $\text{Nakano} \Rightarrow \text{Griffiths} \Rightarrow \text{ample}$, and for $r=1$ all three coincide with $\Theta > 0$, i.e. with positivity of $c_1$ by Kodaira's embedding theorem.

The easy direction of the conjecture: if $\Theta_{E,h}>_{\mathrm{Gr}}0$, then the induced metric on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ has curvature
$$\Theta_{\mathcal{O}(1)}\big|_{(x,[s])} = \pi^*\omega_{\mathrm{FS-fibre}} + \frac{\widetilde\Theta(\,\cdot\otimes s,\,\cdot\otimes s)}{|s|_h^2} > 0,$$
so $\mathcal{O}(1)$ is positive and $E$ is ample. The converse fails to be reversible because ampleness only gives a metric on $\mathcal{O}(1)$ of a *general* shape, not one that is fibrewise Fubini–Study, and the fibrewise-FS condition is exactly what encodes "curvature of a metric on $E$".

Key structural theorems used throughout:

- **Demailly–Skoda (1980).** $\Theta_{E,h}>_{\mathrm{Gr}}0 \Rightarrow E \otimes \det E$ is Nakano positive; likewise $\ge_{\mathrm{Gr}}0 \Rightarrow \ge_{\mathrm{Nak}}0$.
- **Nakano vanishing.** $E >_{\mathrm{Nak}} 0 \Rightarrow H^q(X, K_X \otimes E) = 0$ for $q \ge 1$.
- **Fulton–Lazarsfeld (1983).** For $E$ ample and $P$ a Schur polynomial of degree $k \le \dim X$, $\int_Z P(c(E)) > 0$ for all $k$-dimensional subvarieties $Z$ — the *numerical* shadow of Griffiths' Chern-form conjecture.

## 3. History & State of the Art (SOTA)

Griffiths introduced the pointwise curvature notion and posed the conjecture in his 1969 Kodaira-volume paper *Hermitian differential geometry, Chern classes, and positive vector bundles*, motivated by the wish to prove Chern-class positivity for ample bundles by pointwise curvature computations. Nakano's stronger condition dates to 1955.

Milestones:

| Year | Result |
|---|---|
| 1955–65 | Nakano positivity, Kodaira embedding: case $r=1$ settled |
| 1969 | Griffiths states the conjecture; proves Griffiths $\Rightarrow$ ample |
| 1973 | Umemura: ample bundles on compact Riemann surfaces are Griffiths positive (partial, low rank/genus) |
| 1980 | Demailly–Skoda: $E$ Griffiths $\ge 0 \Rightarrow E\otimes\det E$ Nakano $\ge 0$ |
| 1983 | Fulton–Lazarsfeld: numerical positivity of Schur polynomials for ample $E$ (algebraic, not curvature) |
| 1990 | Campana–Flenner: complete proof of the conjecture for all curves |
| 2009 | Berndtsson: Nakano positivity of direct images $\pi_*(K_{X/Y}\otimes L)$ — first large new supply of Nakano-positive bundles |
| 2012–22 | Guler, Diverio, Finski, Ross–Toma: Chern/Segre/Schur *form* positivity progress |
| 2020 | Demailly: Hermitian–Yang–Mills / geometric-flow strategy for the full conjecture |

Ampleness is by contrast completely characterized algebraically (Hartshorne, Lazarsfeld's *Positivity II*), so the conjecture is precisely the assertion that an algebraic condition has an analytic realization.

## 4. Partial Results / Verified Cases

- **Rank $r = 1$, all dimensions.** Kodaira: ample $\iff$ $c_1$ representable by a positive form. Griffiths = Nakano = ample.
- **$\dim_{\mathbb{C}} X = 1$ (all compact Riemann surfaces, all ranks, all genera).** Campana–Flenner, *Math. Ann.* 287 (1990): every ample bundle on a smooth projective curve admits a Griffiths-positive metric; earlier partial cases by Umemura (1973). This is the only unconditional dimension.
- **Direct sums and pullbacks.** $\bigoplus_i L_i$ with $L_i$ ample line bundles is Griffiths positive (product metric); Griffiths positivity is stable under quotients, tensor products, symmetric and exterior powers, and pullback by immersions.
- **Homogeneous bundles on rational homogeneous spaces $G/P$.** Ample homogeneous bundles carry $G$-invariant metrics whose curvature is computable by root data and is Griffiths positive; e.g. $T_{\mathbb{P}^n}$ (Fubini–Study), $\mathcal{O}(1)^{\oplus r}$, ample bundles on Grassmannians.
- **Twisted statements.** For $E$ ample, $E \otimes \det E \otimes A$ is known Nakano-positive in many settings; by Demailly–Skoda any Griffiths-positive $E$ gives Nakano-positive $E\otimes \det E$, so "Griffiths $\Rightarrow$ Nakano" holds after a determinant twist.
- **Direct images.** Berndtsson (2009): if $\pi:X\to Y$ is a smooth fibration and $L$ is (semi)positive, $\pi_*(K_{X/Y}\otimes L)$ is Nakano semipositive — hence Griffiths semipositive; Mourougane–Takayama extended this to singular settings.
- **Chern-form conjecture, partial.** Guler (2012): Segre forms $s_k(E,h)$ of a Griffiths-positive bundle are positive $(k,k)$-forms. Diverio (2016) reproved and extended this via a Kobayashi–Lübke type inequality. Finski (2022) and Ross–Toma (2021–23) established positivity/Hodge–Riemann-type statements for general Schur forms of Griffiths-positive bundles, essentially settling the *form* version for Schur polynomials.

## 5. Principal Obstacles

- **No canonical metric to start from.** Ampleness gives a positive metric on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$; recovering a metric on $E$ requires that metric to be *fibrewise Fubini–Study*. Averaging or fibre-integrating a general positive metric destroys positivity of the transverse (base) directions: the second fundamental form of the averaging contributes a negative term of the same order.
- **Ampleness is asymptotic, Griffiths positivity is pointwise.** $E$ ample means $S^m E$ is globally generated for $m \gg 0$; the natural metric $h_m$ induced from $S^mE \hookrightarrow \mathcal{O}^{N}$ (or from $H^0$) is Griffiths *semi*positive at best, and the $m$-th root operation $h_m^{1/m}$ produces curvature terms whose error does not vanish as $m\to\infty$ in the non-decomposable directions. This is the exact point where the standard "Kodaira via Bergman kernels" argument for $r=1$ breaks.
- **Non-convexity of the Griffiths cone.** The set of Griffiths-positive curvature tensors is a cone defined by positivity on the Segre variety of decomposable tensors, not by positivity of a Hermitian form. It is not preserved by the natural elliptic regularizations; heat-flow/Hermitian–Yang–Mills methods preserve Nakano-type conditions much more readily than Griffiths ones, and Nakano positivity is *strictly stronger* — it genuinely fails for $T_{\mathbb{P}^n}$, so no flow whose invariant cone is Nakano can prove the conjecture.
- **No vanishing theorem to leverage.** Griffiths positivity alone does not imply Nakano vanishing (only after a $\det E$ twist), so cohomological methods that made $r=1$ tractable have no direct analogue.
- **Curves are special.** The proof on curves uses the classification of ample bundles via the Harder–Narasimhan filtration and the fact that $\Lambda^{1,1}$ is one-dimensional, so Griffiths and Nakano conditions collapse to a single scalar inequality. Both facts fail for $\dim X \ge 2$.

## 6. The Gap

Proven: $r=1$ (any $X$); any $r$ with $\dim X = 1$; homogeneous and split cases; semipositive versions from direct images; the Chern/Schur *form* consequences assuming a Griffiths-positive metric exists.

Missing: a single construction producing a Griffiths-positive metric from ampleness when $\dim X \ge 2$ and $r \ge 2$. Concretely, no example is known — not even one — of an ample rank-2 bundle on an algebraic surface for which Griffiths positivity is verified by a method that does not reduce to a homogeneous/split/curve situation. The precise step to cross: convert the positive metric on $\mathcal{O}_{\mathbb{P}(E^*)}(1)$ into a fibrewise-FS positive metric, i.e. solve a fibrewise "Fubini–Study approximation" problem with base-direction curvature control, or run a geometric flow on the space of Hermitian metrics on $E$ whose invariant set is exactly the Griffiths cone.

## 7. Current Research (as of June 2026)

- **Hermitian–Yang–Mills / flow approach.** Demailly (2020, *Matemática Contemporânea* / arXiv:2002.02677) proposed evolving metrics by a modified HYM-type equation designed to reach Griffiths positivity; the invariance of the Griffiths cone under the flow remains unproven. Groups in Grenoble/Institut Fourier and Paris continue this line. *(frontier — verify)*
- **Approximation and $L^2$ characterizations.** Naumann, *An approach to Griffiths' conjecture* (arXiv:1901.09227), reformulates the problem via curvature of $L^2$-metrics on spaces of sections. Deng–Ning–Wang–Zhou and Hosono–Inayama give converses to Hörmander/Ohsawa–Takegoshi estimates characterizing Nakano and dual-Nakano positivity by $L^2$-extension properties, opening the possibility of an analogous $L^2$ characterization of Griffiths positivity. *(frontier — verify)*
- **Schur-form positivity.** Finski, Ross–Toma, and collaborators continue to push pointwise positivity and Hodge–Riemann bilinear relations for characteristic forms, now for broader positivity classes (dual Nakano, $m$-positivity). This settles Griffiths' *second* conjecture in much generality while leaving the metric-existence conjecture untouched.
- **Singular/adjoint variants.** Extension of Berndtsson-type positivity to direct images with singular Hermitian metrics (Păun–Takayama, Hacon–Popa–Schnell circle) supplies Griffiths-semipositive objects and motivates a "singular Griffiths positivity" version of the conjecture.

## 8. Future Work

- Settle the first open case: $X$ a smooth projective surface, $E$ ample of rank 2 — e.g. bundles arising as extensions $0\to \mathcal{O}(A) \to E \to \mathcal{O}(B)\to 0$ on $\mathbb{P}^2$ with $A,B$ ample, where the extension class obstructs the split metric.
- Identify a flow or variational functional on $\mathrm{Herm}(E)$ with the Griffiths cone as its invariant/attracting set; Demailly's proposal is the template.
- Find an $L^2$-extension characterization of Griffiths positivity parallel to the known Nakano and dual-Nakano characterizations, then verify it directly for ample bundles.
- Test the conjecture numerically: discretize the curvature condition on toric or homogeneous-fibred surfaces and search for obstructions in the space of ample rank-2 bundles.
- Clarify the exact relationship among ample, Griffiths, dual Nakano and $\det$-twisted Nakano positivity; a counterexample separating ample from Griffiths would be as valuable as a proof.

## 9. Key References

- **[Foundational]** P. A. Griffiths. *Hermitian differential geometry, Chern classes, and positive vector bundles.* In: Global Analysis (Papers in Honor of K. Kodaira), Princeton University Press, 1969, pp. 185–251.
- **[Foundational]** S. Nakano. *On complex analytic vector bundles.* Journal of the Mathematical Society of Japan 7 (1955), 1–12. [DOI](https://doi.org/10.2969/jmsj/00710001)
- **[Foundational]** J.-P. Demailly, H. Skoda. *Relations entre les notions de positivités de P. A. Griffiths et de S. Nakano pour les fibrés vectoriels.* Séminaire P. Lelong–H. Skoda 1978/79, Lecture Notes in Mathematics 822, Springer, 1980, pp. 304–309.
- **[Partial result]** H. Umemura. *Some results in the theory of vector bundles.* Nagoya Mathematical Journal 52 (1973), 97–128. [DOI](https://doi.org/10.1017/s0027763000015919)
- **[Partial result]** F. Campana, H. Flenner. *A characterization of ample vector bundles on a curve.* Mathematische Annalen 287 (1990), 571–575. [DOI](https://doi.org/10.1007/bf01446914)
- **[Foundational]** W. Fulton, R. Lazarsfeld. *Positive polynomials for ample vector bundles.* Annals of Mathematics 118 (1983), 35–60. [DOI](https://doi.org/10.2307/2006953)
- **[SOTA]** B. Berndtsson. *Curvature of vector bundles associated to holomorphic fibrations.* Annals of Mathematics 169 (2009), 531–560. [DOI](https://doi.org/10.4007/annals.2009.169.531)
- **[SOTA]** J.-P. Demailly. *Hermitian–Yang–Mills approach to the conjecture of Griffiths on the positivity of ample vector bundles.* arXiv:2002.02677 (2020).
- **[SOTA]** D. Guler. *On Segre forms of positive vector bundles.* Canadian Mathematical Bulletin 55 (2012), 108–113. [DOI](https://doi.org/10.4153/cmb-2011-100-6)
- **[SOTA]** S. Diverio. *Segre forms and Kobayashi–Lübke inequality.* Mathematische Zeitschrift 283 (2016), 1033–1047. [DOI](https://doi.org/10.1007/s00209-016-1632-y)
- **[SOTA]** S. Finski. *On characteristic forms of positive vector bundles, mixed discriminants and pushforward identities.* arXiv:2108.13070 (2021). [DOI](https://doi.org/10.1112/jlms.12605)
- **[SOTA]** J. Ross, M. Toma. *Hodge–Riemann relations for Schur classes in the linear and Kähler cases.* arXiv:2104.03718 (2021). [DOI](https://doi.org/10.1093/imrn/rnac208)
- **[SOTA]** M. Naumann. *An approach to Griffiths' conjecture.* arXiv:1901.09227 (2019).
- **[Survey / Book]** R. Lazarsfeld. *Positivity in Algebraic Geometry II: Positivity for Vector Bundles, and Multiplier Ideals.* Ergebnisse der Mathematik 49, Springer, 2004.
- **[Survey / Book]** S. Kobayashi. *Differential Geometry of Complex Vector Bundles.* Publications of the Mathematical Society of Japan 15, Princeton University Press, 1987.
- **[Survey / Book]** J.-P. Demailly. *Complex Analytic and Differential Geometry.* OpenContent book, Institut Fourier (continuously updated).

## 10. Worked Example / Concrete Special Case

**$E = T_{\mathbb{P}^n}$ with the Fubini–Study metric: Griffiths positive, Nakano degenerate.**

Normalize the Fubini–Study metric so that its curvature tensor at a point $x$, with $T_{\mathbb{P}^n,x}$ identified with $\mathbb{C}^n$ carrying the standard Hermitian product $\langle\cdot,\cdot\rangle$, is
$$\widetilde\Theta(\xi\otimes s,\ \eta\otimes t) \;=\; \langle \xi,\eta\rangle\,\langle s,t\rangle \;+\; \langle \xi,t\rangle\,\langle s,\eta\rangle .$$

*Griffiths positivity.* For a decomposable tensor $u=\xi\otimes s$ with $\xi,s\neq0$:
$$\widetilde\Theta(u,u) \;=\; |\xi|^2|s|^2 + |\langle \xi,s\rangle|^2 \;\ge\; |\xi|^2|s|^2 \;>\;0 .$$
So $T_{\mathbb{P}^n}$ is Griffiths positive, consistent with its ampleness (Mori). For $n=1$, $T_{\mathbb{P}^1}=\mathcal{O}(2)$ and the expression is $2|\xi|^2|s|^2>0$ — the line-bundle case.

*Nakano failure for $n\ge2$.* Let $e_1,e_2$ be orthonormal in $\mathbb{C}^n$ and take the non-decomposable tensor
$$u \;=\; e_1\otimes e_2 \;-\; e_2\otimes e_1 \;\in\; T_{\mathbb{P}^n,x}\otimes T_{\mathbb{P}^n,x}, \qquad u \neq 0 .$$
Expanding bilinearly with $\xi_1=e_1,s_1=e_2$ (coefficient $+1$) and $\xi_2=e_2,s_2=e_1$ (coefficient $-1$):

- First term $\sum_{i,j}\epsilon_i\bar\epsilon_j\langle \xi_i,\xi_j\rangle\langle s_i,s_j\rangle$: diagonal contributions $1\cdot 1 + 1\cdot 1 = 2$; off-diagonal contributions vanish since $\langle e_1,e_2\rangle=0$. Total $=2$.
- Second term $\sum_{i,j}\epsilon_i\bar\epsilon_j\langle \xi_i,s_j\rangle\langle s_i,\xi_j\rangle$: diagonal contributions are $|\langle e_1,e_2\rangle|^2 = 0$ twice; off-diagonal $(i,j)=(1,2)$ gives $(+1)(-1)\langle e_1,e_1\rangle\langle e_2,e_2\rangle=-1$, and $(2,1)$ gives $-1$. Total $=-2$.

Hence $\widetilde\Theta(u,u) = 2 - 2 = 0$: the Nakano form degenerates on the antisymmetric tensor $u$, so $(T_{\mathbb{P}^n},h_{FS})$ is **not** Nakano positive for $n\ge2$.

*What the example shows.* Griffiths positivity is strictly weaker than Nakano positivity, and any strategy that manufactures metrics inside the Nakano cone cannot settle the conjecture, since ample bundles need not sit there. Consistently with Demailly–Skoda, the twist $T_{\mathbb{P}^n}\otimes \det T_{\mathbb{P}^n} = T_{\mathbb{P}^n}\otimes\mathcal{O}(n+1)$ *is* Nakano positive: the twist adds $(n+1)\,\omega_{FS}\otimes \mathrm{Id}$, i.e. $+(n+1)|u|^2$ to the quadratic form, turning the $0$ above into $(n+1)\cdot 2>0$. This is the smallest complete instance of both the phenomenon and the repair mechanism at the heart of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*