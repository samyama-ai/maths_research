---
id: 03-geometry/green-griffiths-conjecture
title: "Green-Griffiths Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Green-Griffiths Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/green-griffiths-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a projective algebraic variety of general type over $\mathbb{C}$ (i.e. $X$ smooth, or with mild singularities, and $K_X$ big). The **Green–Griffiths conjecture** asserts:

> There exists a proper algebraic subvariety $Y \subsetneq X$ such that every nonconstant holomorphic map $f \colon \mathbb{C} \to X$ has image contained in $Y$.

Such an $X$ is called **algebraically degenerate** for entire curves, or *pseudo–Brody hyperbolic*. The **Green–Griffiths–Lang (GGL)** form adds Lang's arithmetic half: the same $Y$ can be chosen so that for every number field $K$ over which $X$ is defined, $X(K) \setminus Y$ is finite; and $Y$ is the union of all positive-dimensional images of non-general-type subvarieties.

A complete proof must produce $Y$ for *all* varieties of general type in all dimensions. A disproof needs a single $X$ of general type carrying a Zariski-dense entire curve. Two weaker statements often conflated with the full conjecture and **not** sufficient:

1. every entire curve satisfies some algebraic differential equation (proved by Demailly, 2011);
2. algebraic degeneracy for *generic* members of a family (proved for generic hypersurfaces of high degree).

## 2. Mathematical Foundations

**General type.** $X$ smooth projective of dimension $n$ is of general type if $\mathrm{vol}(K_X) = \limsup_m \frac{n!}{m^n} h^0(X, mK_X) > 0$.

**Brody/Kobayashi.** $X$ is Brody hyperbolic if every holomorphic $f\colon\mathbb{C}\to X$ is constant; for compact $X$ this is equivalent to Kobayashi hyperbolicity (vanishing of the Kobayashi pseudodistance only on the diagonal).

**Jet bundles.** Let $J_kX \to X$ be the bundle of $k$-jets of germs $(\mathbb{C},0)\to X$, with fibre $\cong \mathbb{C}^{nk}$. The group $\mathbb{G}_k$ of $k$-jets of reparametrisations $(\mathbb{C},0)\to(\mathbb{C},0)$ acts on $J_kX$. Green and Griffiths introduced the graded bundle $E^{GG}_{k,m}T^*_X$ of **jet differentials of order $k$ and weighted degree $m$**: locally, polynomial operators
$$
P\big(f', f'', \dots, f^{(k)}\big) \;=\; \sum_{|\alpha_1| + 2|\alpha_2| + \cdots + k|\alpha_k| = m} a_{\alpha}(f)\, (f')^{\alpha_1}(f'')^{\alpha_2}\cdots (f^{(k)})^{\alpha_k},
$$
homogeneous of weight $m$ for the $\mathbb{C}^*$-action $\lambda \cdot (f',\dots,f^{(k)}) = (\lambda f', \lambda^2 f'', \dots, \lambda^k f^{(k)})$. Demailly's subbundle $E_{k,m}T^*_X \subset E^{GG}_{k,m}T^*_X$ of $\mathbb{G}_k$-invariant operators is the sheaf of sections of $\mathcal{O}_{X_k}(m)$ on the Demailly–Semple tower $X_k$.

**Fundamental vanishing theorem** (Green–Griffiths 1980; Siu–Yeung; Demailly 1997). If $A$ is an ample line bundle and $P \in H^0\!\big(X, E^{GG}_{k,m}T^*_X \otimes A^{-1}\big)$, then for every entire $f\colon\mathbb{C}\to X$,
$$
P\big(f',f'',\dots,f^{(k)}\big) \equiv 0 .
$$
Hence entire curves lie in the zero locus of the base ideal; the conjecture reduces to showing enough such $P$ exist **and** that their common zero locus is a proper subvariety.

**Demailly's Morse-inequality estimate** (2011). For $X$ of general type of dimension $n$, as $k\to\infty$,
$$
h^0\!\big(X, E^{GG}_{k,m}T^*_X \otimes \mathcal{O}(-m A)\big) \;\gtrsim\; \frac{m^{n+kn-1}}{(n+kn-1)!}\,\frac{(\log k)^n}{n!\,(k!)^n}\Big( c_1(K_X)^n - C\,\frac{\log\log k}{\log k}\Big),
$$
which is positive for $k \gg 0$. This yields the differential equation (statement 2 of §1) but gives no control on the base locus.

## 3. History & State of the Art (SOTA)

- **1970s.** Bloch (1926, revived by Ochiai 1977 and Kawamata 1980) proves that entire curves in a complex torus have Zariski closure a translate of a subtorus — the Bloch–Ochiai theorem.
- **1979/1980.** M. Green and P. Griffiths, in *Two applications of the theory of meromorphic mappings to the study of algebraic and analytic varieties* (Chern Symposium volume), formulate the conjecture and introduce jet differentials.
- **1977–1986.** Bogomolov: surfaces with $c_1^2 > c_2$ have only finitely many rational and elliptic curves; symmetric differentials as the algebraic shadow of the analytic statement.
- **1986/1997.** Lang unifies the analytic and Diophantine pictures (*Hyperbolic and Diophantine analysis*, Bull. AMS 1986).
- **1998.** McQuillan proves the conjecture for surfaces of general type with $c_1^2 > c_2$, combining Ahlfors currents, Nevanlinna theory and Riccati foliations (*Diophantine approximations and foliations*, Publ. IHÉS).
- **2010–2019.** Effective algebraic degeneracy for generic projective hypersurfaces: Diverio–Merker–Rousseau ($d \ge 2^{n^5}$), then Darondeau, Merker–Ta ($d \ge (\sqrt{n}\log n)^n$).
- **2015–2018.** Siu, then Brotbek, prove Kobayashi hyperbolicity of general hypersurfaces of sufficiently large degree; effective versions follow (Deng, Demailly, Merker–Ta).
- **2022+.** Cadorel–Deng–Yamanoi and collaborators prove GGL-type statements for varieties with large fundamental group.

The conjecture is open in every dimension $\ge 2$ for arbitrary varieties of general type.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Subvarieties of abelian/semi-abelian varieties | Full GGL: entire curves are contained in translates of subtori; general-type subvarieties are Brody hyperbolic | Bloch, Ochiai, Kawamata, Noguchi, Yamanoi |
| Surfaces with $c_1^2 > c_2$ (positive second Segre number $s_2 = c_1^2 - c_2$) | Conjecture proved | McQuillan (1998); Demailly–El Goul (2000) |
| Surfaces with $p_g \ge 2$ and irregular surfaces of maximal Albanese dimension | Proved | McQuillan; Yamanoi (2015) |
| Generic hypersurfaces $X \subset \mathbb{P}^{n+1}$ of degree $d \ge (\sqrt{n}\log n)^n$ | Algebraic degeneracy | Merker–Ta (2019), after Diverio–Merker–Rousseau (2010) |
| Generic hypersurfaces $X \subset \mathbb{P}^{n+1}$, $d \gg 0$ (e.g. $d \ge (n\log n)^n$) | Brody hyperbolic — stronger than GG | Siu (2015), Brotbek (2017), Deng, Demailly |
| Generic surfaces in $\mathbb{P}^3$ of degree $d \ge 21$ | Hyperbolic | Demailly–El Goul (2000); improved to $d\ge 18$ by Păun |
| Complete intersections of high multi-degree and high codimension | Ample cotangent bundle $\Rightarrow$ hyperbolic $\Rightarrow$ GG | Brotbek–Darondeau (2018) |
| Any $X$ of general type | Every entire curve satisfies a nonzero global algebraic differential equation | Demailly (2011) |
| Quotients of bounded symmetric domains, varieties with big $\pi_1$-representations | GGL-type degeneracy | Cadorel–Deng–Yamanoi (arXiv, 2022–) |

## 5. Principal Obstacles

- **Base locus, not existence.** Demailly's Morse inequalities give sections of $E^{GG}_{k,m}T^*_X \otimes A^{-1}$ for $k \gg 0$, but nothing bounds the common zero locus of all such sections. The gap between "some differential equation" and "a proper $Y$" is the entire difficulty.
- **Jet bundles are not positive.** $T^*_X$ is almost never ample; positivity of $\mathcal{O}_{X_k}(1)$ on the Demailly tower holds only on the complement of a "vertical" divisor, and Morse-type estimates degenerate as $k$ grows ($(k!)^{-n}$ factors).
- **Genericity is essential to current methods.** Brotbek's Wronskian-type and Siu's slanted-vector-field constructions differentiate in the parameters of a family. They collapse for a single fixed $X$, so no method covers non-generic members.
- **Foliation methods stop at dimension 2.** McQuillan's proof uses Ahlfors currents and the Miyaoka–Bogomolov index/tautological inequality on a foliated surface; in dimension $\ge 3$ Ahlfors currents give no analogue of the $c_1^2 > c_2$ dichotomy, and singularity resolution for foliations is unavailable in general.
- **The Chern-class inequality fails where it is needed.** For hypersurfaces in $\mathbb{P}^3$, $c_1^2 - c_2 < 0$ for all $d$ (see §10), so the one complete surface case never applies to the flagship examples.
- **Value distribution theory is one-dimensional.** Nevanlinna's second main theorem controls one map into one target; there is no higher-rank SMT with error terms strong enough for arbitrary general type $X$.

## 6. The Gap

Proven: (a) *existence* of jet-differential equations on any general-type $X$; (b) *proper degeneracy locus* only when either $\dim X = 2$ with $s_2 = c_1^2 - c_2 > 0$, or $X$ is generic in a family with a large positivity parameter, or $X$ sits inside a semi-abelian variety.

The general statement needs one step: **from a nonzero $P \in H^0(X, E^{GG}_{k,m}T^*_X \otimes A^{-1})$, produce enough further sections that $\bigcap_P Z(P) \neq X$.** Concretely, one wants a lower bound on $\mathrm{vol}(\mathcal{O}_{X_k}(1) - \pi_k^*A)$ *away from a proper subvariety*, or a global-generation statement for jet bundles twisted by a controlled ample factor. Demailly's "algebraic strong general type" reduction shows GGL follows if every general-type $X$ and every irreducible subvariety of every jet tower stage is again of general type in a suitable orbifold sense — that induction is exactly what is missing. Riedl–Yang (2022) sharpen the stakes: GGL for general hypersurfaces of dimension $2n$ and degree $d$ implies Brody hyperbolicity of general hypersurfaces of dimension $n$ and the same degree, so GGL is at least as hard as the Kobayashi conjecture.

## 7. Current Research (as of June 2026)

- **Grenoble/Demailly school** (Demailly's programme continued by Diverio, Trapani, Rousseau, Darondeau): holomorphic Morse inequalities on Demailly–Semple towers, orbifold and "strong general type" reformulations.
- **Brotbek–Deng–Cadorel–Yamanoi**: Wronskian ideal sheaves and Nevanlinna theory over quasi-projective bases; hyperbolicity from big fundamental-group representations (variations of Hodge structure, Higgs bundles, Simpson correspondence). *(frontier — verify: unconditional GGL for all smooth projective $X$ with big $\pi_1$-representation)*
- **Non-reductive GIT** (Bérczi, Kirwan, Oxford): localisation on the reparametrisation-group quotient aiming at polynomial degree bounds $d \gtrsim n^5$ for generic hypersurfaces. *(frontier — verify)*
- **Foliation-theoretic** (McQuillan, Pereira, and students): birational classification of foliations in dimension 3 as a route past the surface case.
- **Arithmetic side**: function-field and Vojta-style analogues, and Lang's conjecture for subvarieties of abelian varieties in characteristic $p$.

## 8. Future Work

1. Prove the conjecture for a *single* fixed (non-generic) smooth surface in $\mathbb{P}^3$ of low degree, e.g. a Fermat quintic — no such result exists.
2. Extend McQuillan's Riccati/Ahlfors machinery to threefolds by classifying rank-1 and rank-2 foliations with degenerate leaves.
3. Prove effective global generation for $E_{k,m}T^*_X \otimes A^{-1}$ with $m, k$ bounded polynomially in $n$ and $\mathrm{vol}(K_X)$.
4. Establish Demailly's "strong general type" induction, or find a general-type $X$ violating it.
5. Attack the Lang half through unlikely intersections and $o$-minimal/Pila–Wilkie counting on jet spaces.

## 9. Key References

- **[Foundational]** M. Green, P. Griffiths. *Two applications of the theory of meromorphic mappings to the study of algebraic and analytic varieties.* In: The Chern Symposium 1979, Springer, 1980, 41–74.
- **[Foundational]** S. Lang. *Hyperbolic and Diophantine analysis.* Bulletin of the American Mathematical Society 14 (1986), 159–205. [DOI](https://doi.org/10.1007/978-1-4612-2116-6_15)
- **[Foundational]** J.-P. Demailly. *Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials.* Proceedings of Symposia in Pure Mathematics 62, AMS, 1997, 285–360. [DOI](https://doi.org/10.1090/pspum/062.2/1492539)
- **[Milestone]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS 87 (1998), 121–174. [DOI](https://doi.org/10.1007/bf02698862)
- **[Milestone]** J.-P. Demailly, J. El Goul. *Hyperbolicity of generic surfaces of high degree in projective 3-space.* American Journal of Mathematics 122 (2000), 515–546. [DOI](https://doi.org/10.1353/ajm.2000.0019)
- **[SOTA]** S. Diverio, J. Merker, E. Rousseau. *Effective algebraic degeneracy.* Inventiones Mathematicae 180 (2010), 161–223. [DOI](https://doi.org/10.1007/s00222-010-0232-4)
- **[SOTA]** J.-P. Demailly. *Holomorphic Morse inequalities and the Green–Griffiths–Lang conjecture.* Pure and Applied Mathematics Quarterly 7 (2011), 1165–1207. [DOI](https://doi.org/10.4310/pamq.2011.v7.n4.a6)
- **[SOTA]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae 202 (2015), 1069–1166. [DOI](https://doi.org/10.1007/s00222-015-0584-x)
- **[SOTA]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS 126 (2017), 1–34. [DOI](https://doi.org/10.1007/s10240-017-0090-3)
- **[SOTA]** D. Brotbek, L. Darondeau. *Complete intersection varieties with ample cotangent bundles.* Inventiones Mathematicae 212 (2018), 913–940. [DOI](https://doi.org/10.1007/s00222-017-0782-9)
- **[SOTA]** J. Merker, T.-A. Ta. *Degrees $d \ge (\sqrt{n}\log n)^n$ and $d \ge (n\log n)^n$ in the conjectures of Green–Griffiths and of Kobayashi.* Acta Mathematica Vietnamica 44 (2019), 63–100.
- **[SOTA]** E. Riedl, D. Yang. *Applications of a Grassmannian technique to hyperbolicity, Chow equivalency, and Seshadri constants.* Journal of Algebraic Geometry 31 (2022), 1–12. [DOI](https://doi.org/10.1090/jag/786)
- **[Survey]** J.-P. Demailly. *Recent results on the Kobayashi and Green–Griffiths–Lang conjectures.* Japanese Journal of Mathematics 15 (2020), 1–120. [DOI](https://doi.org/10.1007/s11537-019-1566-3)
- **[Survey]** S. Diverio, E. Rousseau. *A survey on hyperbolicity of projective hypersurfaces.* IMPA Publicações Matemáticas, 2011.
- **[Related]** K. Yamanoi. *Holomorphic curves in algebraic varieties of maximal Albanese dimension.* International Journal of Mathematics 26 (2015), 1540006. [DOI](https://doi.org/10.1142/s0129167x15410062)
- **[Book]** J. Noguchi, J. Winkelmann. *Nevanlinna Theory in Several Complex Variables and Diophantine Approximation.* Grundlehren der mathematischen Wissenschaften 350, Springer, 2014. [DOI](https://doi.org/10.1007/978-4-431-54571-2)

## 10. Worked Example / Concrete Special Case

**Why McQuillan's theorem misses every surface in $\mathbb{P}^3$.**

Let $X \subset \mathbb{P}^3$ be a smooth surface of degree $d$, with hyperplane class $h = \mathcal{O}_X(1)$, $h^2 = d$. Adjunction gives
$$
K_X = \mathcal{O}_X(d-4), \qquad c_1(X) = -(d-4)h .
$$
So $X$ is of general type exactly when $d \ge 5$, and
$$
c_1^2 = (d-4)^2 h^2 = d(d-4)^2 .
$$
From the exact sequences $0 \to T_X \to T_{\mathbb{P}^3}|_X \to \mathcal{O}_X(d) \to 0$ and the Euler sequence, the total Chern class is $c(T_X) = (1+h)^4 / (1+dh)$, giving
$$
c_2 = \big(6 - 4d + d^2\big) h^2 = d\,(d^2 - 4d + 6).
$$
Check $d = 4$ (a K3): $c_1^2 = 0$, $c_2 = 4\cdot 6 = 24$ — correct.

Now form the second Segre number:
$$
s_2 = c_1^2 - c_2 = d\big[(d-4)^2 - (d^2 - 4d + 6)\big] = d\big[d^2 - 8d + 16 - d^2 + 4d - 6\big] = d\,(10 - 4d).
$$
For $d \ge 5$ (general type), $10 - 4d \le -10 < 0$, so
$$
c_1^2 - c_2 \le -5\cdot 10 = -50 < 0 \quad \text{for every smooth surface of general type in } \mathbb{P}^3 .
$$
McQuillan's hypothesis $c_1^2 > c_2$ therefore **never** holds for a smooth hypersurface surface. For $d = 5$: $c_1^2 = 5$, $c_2 = 55$, $s_2 = -50$. For $d = 6$: $c_1^2 = 24$, $c_2 = 108$, $s_2 = -84$. The deficit grows like $-4d^2$.

By contrast, a compact ball quotient $X = \mathbb{B}^2/\Gamma$ ($\Gamma$ torsion-free cocompact) satisfies the equality case of Bogomolov–Miyaoka–Yau, $c_1^2 = 3c_2$, hence $s_2 = 2c_2 > 0$: McQuillan applies (and $X$ is in fact Kobayashi hyperbolic outright, since $\mathbb{B}^2$ is Kobayashi hyperbolic and hyperbolicity descends to quotients).

**Consequence.** Every known unconditional surface technique with a numerical hypothesis is inert on quintic surfaces in $\mathbb{P}^3$. For these one only has the generic statement (Demailly–El Goul: a *very general* surface of degree $d \ge 21$ is hyperbolic) plus Demailly's non-effective differential equation. Whether a *specific* smooth quintic — say the Fermat quintic $x_0^5 + x_1^5 + x_2^5 + x_3^5 = 0$ — admits a Zariski-dense entire curve is open. It contains lines and singular rational curves (so it is not Brody hyperbolic), and Green–Griffiths predicts these algebraic curves, finite in number here, exhaust all entire curves.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*