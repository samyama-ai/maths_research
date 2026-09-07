---
id: 03-geometry/oka-grauert-principle
title: "Oka-Grauert Principle"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Oka-Grauert Principle

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/oka-grauert-principle` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Oka–Grauert principle is the heuristic that **on a Stein space, problems of a cohomological or homotopy-theoretic nature that admit continuous solutions admit holomorphic solutions**, and that the holomorphic and continuous solution sets have the same weak homotopy type.

Formally, let $X$ be a Stein manifold (or reduced Stein space) and $Y$ a complex manifold. Say the pair $(X,Y)$ satisfies the **basic Oka property** if every continuous map $f_0 \colon X \to Y$ is homotopic to a holomorphic map, and the **parametric Oka property** if the inclusion
$$\mathcal{O}(X,Y) \hookrightarrow \mathcal{C}(X,Y)$$
is a weak homotopy equivalence. The central open problem is:

> **Characterize the complex manifolds $Y$ (the *Oka manifolds*) for which the parametric Oka property, with approximation on holomorphically convex compacts and interpolation on closed complex subvarieties, holds for **every** Stein source $X$ — and decide whether this class coincides with Gromov's geometrically defined class of **elliptic** manifolds.**

A complete resolution requires either (i) a proof that every Oka manifold admits a dominating spray, or (ii) a Stein counterexample, together with a workable intrinsic (local, deformation-stable) criterion for the Oka property. Secondary open components: whether the Oka property is invariant under holomorphic deformations, under blow-ups and proper modifications, and whether it passes to total spaces of holomorphic fiber bundles with Oka fiber and Oka base.

## 2. Mathematical Foundations

**Stein manifolds.** $X$ is Stein if it is holomorphically convex, holomorphically separable, and $\mathcal{O}(X)$ gives local coordinates. Equivalently (Cartan's Theorem B) $H^q(X,\mathcal{F}) = 0$ for every coherent analytic sheaf $\mathcal{F}$ and $q \ge 1$. Every Stein $X^n$ embeds properly in $\mathbb{C}^N$, $N = \lfloor 3n/2 \rfloor + 1$ (Eliashberg–Gromov, Schürmann).

**Oka–Grauert for bundles.** For a complex Lie group $G$ and a Stein base $X$, the natural map from the set of isomorphism classes of holomorphic principal $G$-bundles to that of topological ones,
$$H^1(X,\mathcal{O}(G)) \longrightarrow H^1(X,\mathcal{C}(G)),$$
is a bijection (Grauert 1958).

**Sprays and ellipticity (Gromov 1989).** A **dominating spray** on $Y$ is a holomorphic vector bundle $p\colon E \to Y$ with a holomorphic map $s\colon E \to Y$ such that for every $y \in Y$,
$$s|_{E_y}(0_y) = y, \qquad ds|_{E_y}(0_y)\colon E_y \longrightarrow T_yY \ \text{ is surjective.}$$
$Y$ is **elliptic** if such a spray exists; **subelliptic** if there are finitely many sprays $s_j\colon E_j \to Y$ with
$$\sum_{j} ds_j|_{(E_j)_y}(0_y)\,(E_j)_y = T_yY \quad \text{for all } y \in Y .$$

**Oka property.** $Y$ is an **Oka manifold** if for every $n$, every convex compact $K \subset \mathbb{C}^n$ and open $U \supset K$, every holomorphic $f\colon U \to Y$ can be approximated uniformly on $K$ by entire maps $\mathbb{C}^n \to Y$ (the **convex approximation property**, CAP). Forstnerič's theorem: CAP $\iff$ all parametric Oka properties with approximation and jet interpolation, for all Stein sources, all stratified fiber bundles.

**Implications known:**
$$\text{homogeneous} \;\Rightarrow\; \text{elliptic} \;\Rightarrow\; \text{subelliptic} \;\Rightarrow\; \text{Oka} \;\Longleftrightarrow\; \text{CAP}.$$
The converse of the second and third arrows is the open frontier (the third fails without the Stein hypothesis, see §4).

## 3. History & State of the Art (SOTA)

- **1939.** Kiyoshi Oka solves the second Cousin problem on domains of holomorphy: a holomorphic line bundle is holomorphically trivial iff it is topologically trivial. This is the seed statement.
- **1957–58.** Hans Grauert, in three *Mathematische Annalen* papers, proves the principle for principal bundles with complex Lie structure group and for sections of fiber bundles with homogeneous fiber over Stein bases, including the parametric form.
- **1962–66.** Ramspott, Forster–Ramspott recast Grauert's proof sheaf-theoretically ("Oka pairs", analytische Modulgarben).
- **1989.** Gromov's *Oka's principle for holomorphic sections of elliptic bundles* (JAMS) replaces the group action by a dominating spray — the decisive generalization, moving from homogeneity to a soft flexibility condition.
- **2000–2006.** Forstnerič and Prezelj fill in the details of Gromov's arguments, extend to subelliptic submersions, and prove the **CAP theorem**: Runge approximation on convex sets implies the full Oka property (*Annals of Mathematics* 163, 2006). This makes "Oka" a checkable property of $Y$ alone.
- **2003–2010.** Lárusson builds a model-category framework in which Stein manifolds are cofibrant and Oka manifolds fibrant, making the principle a statement about fibrant replacement.
- **2012.** Ivarsson–Kutzschebauch solve Gromov's Vaserstein problem: a null-homotopic holomorphic $f\colon X \to SL_n(\mathbb{C})$ on Stein $X$ factors as a finite product of holomorphic elementary (unipotent) matrices.
- **2020–2024.** Kusakabe proves **localization** and **elliptic characterization** theorems, shows complements of compact holomorphically (polynomially) convex sets in $\mathbb{C}^n$, $n\ge 2$, are Oka, and constructs Oka manifolds that are not elliptic.

## 4. Partial Results / Verified Cases

Established classes of Oka manifolds:

- **Complex homogeneous spaces** $G/H$, $G$ a complex Lie group — Grauert 1958. Includes $\mathbb{C}^n$, $\mathbb{C}^*$, all complex tori, $\mathbb{P}^n$, Grassmannians, flag manifolds, $SL_n(\mathbb{C})$, quadrics.
- **Elliptic manifolds**: any $Y$ carrying finitely many complete holomorphic vector fields spanning $T_yY$ at each point (e.g. **flexible** affine varieties); in particular $\mathbb{C}^n \setminus A$ for an algebraic subvariety $A$ of codimension $\ge 2$.
- **Subelliptic**: complements $\mathbb{P}^n \setminus A$, $\operatorname{codim} A \ge 2$; smooth quasi-affine algebraically elliptic varieties.
- **Dimension 1**: an open Riemann surface is Oka $\iff$ elliptic $\iff$ it is one of $\mathbb{P}^1$, $\mathbb{C}$, $\mathbb{C}^*$, a torus, or non-hyperbolic in the relevant sense — the compact Oka surfaces are exactly $\mathbb{P}^1$ and tori (genus $g \ge 2$ is Kobayashi hyperbolic, hence not Oka).
- **Surfaces (complex dim 2)**: compact Oka surfaces are classified into a short list in the Kodaira dimension $\le 0$ range; $\kappa(Y) = 2$ never Oka.
- **Bundle-theoretic cases fully proved**: sections of stratified holomorphic fiber bundles and of subelliptic submersions over Stein bases; $H^1(X,\mathcal{O}(G)) \cong H^1(X,\mathcal{C}(G))$ for all complex Lie $G$ and all Stein spaces $X$, including with parameters and with interpolation on subvarieties.
- **Negative side**: Kobayashi hyperbolic manifolds are never Oka; Oka manifolds are dominable by $\mathbb{C}^n$ and have no nonconstant negatively curved metrics.
- **Converse fails outside Stein**: Kusakabe (Proc. AMS 149, 2021) exhibits Oka manifolds — complements of suitable countable sets — that carry no dominating spray, so "Oka $\Rightarrow$ elliptic" is false in general; it remains open for Stein manifolds.

## 5. Principal Obstacles

- **No local-to-global handle on ellipticity.** CAP is verified by gluing entire maps; sprays are global objects built from complete vector fields. There is no known procedure converting a family of local approximations into a globally defined dominating spray, because the spray must be a submersion along the *entire* zero section simultaneously.
- **Failure of $\bar\partial$-methods at the target.** Hörmander $L^2$ estimates and Cartan's Theorem B live on the Stein *source*. When the target $Y$ is nonlinear and non-Stein, there is no sheaf of solutions to which vanishing theorems apply; one must instead do a Cartan-pair induction with nonlinear splitting, whose convergence needs a spray to linearize.
- **Curvature/hyperbolicity dichotomy is not exhaustive.** Non-hyperbolicity does not imply Oka; the intermediate zone (e.g. general $K3$ surfaces, complements of generic curves in $\mathbb{P}^2$) is invisible to both Nevanlinna theory and spray constructions.
- **Deformation instability is unresolved.** No known argument makes CAP semicontinuous in a family, so limits and degenerations of Oka manifolds cannot be controlled.
- **Algebraic vs analytic gap.** Algebraic ellipticity (Gromov) implies analytic ellipticity, but no converse is known and no invariant separates them; techniques from affine algebraic geometry (Andersén–Lempert theory, flexibility) stop at quasi-affine varieties.

## 6. The Gap

Proven: $\text{elliptic} \Rightarrow \text{subelliptic} \Rightarrow \text{CAP} \Leftrightarrow \text{full parametric Oka principle}$, plus a complete theory for homogeneous fibers over Stein bases. The gap is the reverse implication restricted to Stein targets:

> Does every Stein Oka manifold $Y$ admit a dominating spray $s\colon E \to Y$?

Concretely, one must upgrade an approximation statement — every holomorphic map from a neighbourhood of a convex compact $K \subset \mathbb{C}^n$ into $Y$ is approximable by entire maps — into a single holomorphic submersion $E \to Y$ from a vector bundle. The two ends differ in quantifier structure (families of germs vs one global object) and in regularity (approximation vs infinitesimal surjectivity). Kusakabe's elliptic characterization narrows this to a condition on **local dominating sprays over Stein neighbourhoods**; assembling them globally is the remaining step.

## 7. Current Research (as of June 2026)

- **Kusakabe's localization program** (Osaka/Kyoto): the Oka property is local on the target in a precise sense, yielding that complements of compact holomorphically convex sets in Oka Stein manifolds are Oka. Extensions to complements of unbounded closed sets are being pursued *(frontier — verify)*.
- **Forstnerič (Ljubljana) and Lárusson (Adelaide)**: parametric Oka principle in the model-category setting; Oka theory for manifolds with boundary, for minimal surfaces and directed holomorphic curves.
- **Kutzschebauch, Schott, Ivarsson (Bern/Uppsala)**: algebraic Oka theory, Gromov–Vaserstein factorizations, algebraic ellipticity of flexible varieties and of complements in homogeneous spaces.
- **Arzhantsev–Flenner–Kaliman–Zaidenberg school**: flexibility of affine varieties as the algebraic shadow of ellipticity; new flexible families among Fano and horospherical varieties.
- **Classification of compact Oka surfaces** and the status of $K3$ and Enriques surfaces remain a specific target of current preprints *(frontier — verify)*.

## 8. Future Work

- Settle "Oka $\Rightarrow$ elliptic" for Stein manifolds; a natural test case is a Stein Oka manifold constructed by Andersén–Lempert surgery with no obvious complete vector fields.
- Prove or refute deformation invariance: if $\pi\colon \mathcal{Y}\to \Delta$ is a holomorphic family with $\mathcal{Y}_t$ Oka for $t \ne 0$, is $\mathcal{Y}_0$ Oka?
- Decide whether the Oka property ascends and descends along blow-ups with smooth centres and along proper modifications.
- Determine whether the total space of a holomorphic fiber bundle with Oka base and Oka fiber is Oka.
- Develop an Oka theory for singular targets and for complex spaces with quotient singularities.
- Reconcile algebraic and analytic ellipticity: find an invariant, or prove they agree for smooth affine varieties.

## 9. Key References

- **[Foundational]** K. Oka. *Sur les fonctions analytiques de plusieurs variables, III: Deuxième problème de Cousin.* Journal of Science of the Hiroshima University, Series A, 9 (1939), 7–19.
- **[Foundational]** H. Grauert. *Holomorphe Funktionen mit Werten in komplexen Lieschen Gruppen.* Mathematische Annalen 133 (1957), 450–472.
- **[Foundational]** H. Grauert. *Analytische Faserungen über holomorph-vollständigen Räumen.* Mathematische Annalen 135 (1958), 263–273.
- **[Foundational]** M. Gromov. *Oka's principle for holomorphic sections of elliptic bundles.* Journal of the American Mathematical Society 2 (1989), 851–897.
- **[SOTA]** F. Forstnerič. *Runge approximation on convex sets implies the Oka property.* Annals of Mathematics 163 (2006), 689–707.
- **[SOTA]** F. Forstnerič. *The Oka principle for sections of subelliptic submersions.* Mathematische Zeitschrift 241 (2002), 527–551.
- **[SOTA]** B. Ivarsson, F. Kutzschebauch. *Holomorphic factorization of mappings into $SL_n(\mathbb{C})$.* Annals of Mathematics 175 (2012), 45–69.
- **[SOTA / Recent]** Y. Kusakabe. *Elliptic characterization and localization of Oka manifolds.* Indiana University Mathematics Journal 70 (2021), 1039–1054.
- **[SOTA / Recent]** Y. Kusakabe. *Oka complements of countable sets and nonelliptic Oka manifolds.* Proceedings of the American Mathematical Society 149 (2021), 1233–1238.
- **[Survey]** F. Forstnerič, F. Lárusson. *Survey of Oka theory.* New York Journal of Mathematics 17a (2011), 11–38.
- **[Book]** F. Forstnerič. *Stein Manifolds and Holomorphic Mappings: The Homotopy Principle in Complex Analysis.* Springer, Ergebnisse der Mathematik, 2nd edition, 2017.
- **[Book]** L. Hörmander. *An Introduction to Complex Analysis in Several Variables.* North-Holland, 3rd edition, 1990.

## 10. Worked Example / Concrete Special Case

**(a) A dominating spray on $Y=\mathbb{C}^2\setminus\{0\}$.** Take the $\mathfrak{sl}_2(\mathbb{C})$ basis
$$A_1=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad A_2=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad A_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
and define the trivial-bundle spray $s\colon Y\times\mathbb{C}^3 \to Y$,
$$s(z,\xi)=\exp\!\big(\xi_1A_1+\xi_2A_2+\xi_3A_3\big)\,z .$$
Then $s(z,0)=z$ and the differential at $\xi=0$ sends the basis to the induced vector fields
$$V_1(z)=(z_2,0),\qquad V_2(z)=(0,z_1),\qquad V_3(z)=(z_1,-z_2).$$
Check surjectivity onto $T_z\mathbb{C}^2=\mathbb{C}^2$ for every $z\ne 0$:

| case | spanning pair | span |
|---|---|---|
| $z_1\ne0,\ z_2\ne0$ | $V_1=(z_2,0),\ V_2=(0,z_1)$ | $\mathbb{C}^2$ |
| $z_2=0,\ z_1\ne0$ | $V_3=(z_1,0),\ V_2=(0,z_1)$ | $\mathbb{C}^2$ |
| $z_1=0,\ z_2\ne0$ | $V_1=(z_2,0),\ V_3=(0,-z_2)$ | $\mathbb{C}^2$ |

So $s$ is a dominating spray, $Y$ is elliptic, hence Oka. Consequence: for **any** Stein manifold $X$, every continuous nowhere-vanishing map $X\to\mathbb{C}^2\setminus\{0\}$ is homotopic to a holomorphic one, i.e. any topological pair of "coprime" functions can be deformed to holomorphic $f,g\in\mathcal{O}(X)$ with $\{f=0\}\cap\{g=0\}=\emptyset$.

**(b) Oka's original case, computed.** For $X$ Stein, the exponential sheaf sequence
$$0 \to \mathbb{Z} \to \mathcal{O}_X \xrightarrow{\ e^{2\pi i \cdot}\ } \mathcal{O}_X^* \to 0$$
gives the long exact sequence
$$H^1(X,\mathcal{O}_X) \to H^1(X,\mathcal{O}_X^*) \to H^2(X,\mathbb{Z}) \to H^2(X,\mathcal{O}_X).$$
Cartan's Theorem B kills the outer terms, so $H^1(X,\mathcal{O}_X^*)\cong H^2(X,\mathbb{Z})$: **holomorphic line bundles on a Stein manifold are classified by their topological Chern class.** Concretely, on an open Riemann surface $X$ one has $H^2(X,\mathbb{Z})=0$, so every holomorphic line bundle is trivial; equivalently every divisor $D=\sum n_j p_j$ (locally finite) is the divisor of a global $f\in\mathcal{O}(X)$ — Weierstrass' theorem recovered as the simplest instance of the Oka–Grauert principle.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*