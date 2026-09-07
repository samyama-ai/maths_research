---
id: 03-geometry/mnop-conjecture
title: "MNOP Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# MNOP Conjecture (Gromov–Witten/Donaldson–Thomas Correspondence)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/mnop-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $X$ be a nonsingular projective 3-fold over $\mathbb{C}$ and $\beta \in H_2(X,\mathbb{Z})$ a curve class. Two virtual counts of curves in class $\beta$ exist:

- **Gromov–Witten (GW):** integrals over the moduli of stable maps $\overline{M}_{g}(X,\beta)$, assembled into a genus series in a variable $u$.
- **Donaldson–Thomas (DT):** integrals over the Hilbert scheme $I_n(X,\beta)$ of ideal sheaves of 1-dimensional subschemes with $[Z]=\beta$, $\chi(\mathcal{O}_Z)=n$, assembled into a series in $q$.

Maulik, Nekrasov, Okounkov and Pandharipande (2006) conjectured three linked statements.

**(C1) Degree-0 evaluation.** $Z_{\mathrm{DT}}(X;q)_0 = M(-q)^{\int_X c_3(T_X\otimes K_X)}$, with $M(q)=\prod_{n\ge1}(1-q^n)^{-n}$ the MacMahon function.

**(C2) Rationality.** The reduced series $Z'_{\mathrm{DT}}(X;q)_\beta = Z_{\mathrm{DT}}(X;q)_\beta / Z_{\mathrm{DT}}(X;q)_0$ is the Laurent expansion of a rational function of $q$, invariant under $q \leftrightarrow 1/q$.

**(C3) GW/DT correspondence.** After the change of variables $-q=e^{iu}$,
$$(-iu)^{d_\beta}\, Z'_{\mathrm{GW}}(X;u)_\beta \;=\; (-q)^{-d_\beta/2}\, Z'_{\mathrm{DT}}(X;q)_\beta , \qquad d_\beta=\int_\beta c_1(T_X).$$

A complete proof must establish (C2) — needed even to make (C3) meaningful, since the substitution $-q=e^{iu}$ requires analytic continuation — and (C3) for **all** nonsingular projective 3-folds and all $\beta$, together with the descendent-insertion refinement of MNOP II. A disproof would exhibit a 3-fold and class $\beta$ with $Z'_{\mathrm{DT}}$ irrational, or matching failing at some genus.

## 2. Mathematical Foundations

**GW side.** $\overline{M}_g(X,\beta)$ carries a virtual class of dimension $d_\beta = \int_\beta c_1(T_X)$ (Li–Tian, Behrend–Fantechi). For $\beta \ne 0$ and $d_\beta=0$ (e.g. Calabi–Yau) the invariant is the number $N_{g,\beta}=\int_{[\overline{M}_g(X,\beta)]^{\mathrm{vir}}} 1$. The connected potential and the reduced partition function are
$$F_{\mathrm{GW}}(u,v)=\sum_{g\ge0}\sum_{\beta\ne0} N_{g,\beta}\,u^{2g-2}v^\beta,\qquad
Z'_{\mathrm{GW}}(X;u)_\beta=\big[\exp F_{\mathrm{GW}}\big]_{v^\beta}.$$

**DT side.** $I_n(X,\beta)=\{\,I\subset\mathcal{O}_X : [Z]=\beta,\ \chi(\mathcal{O}_Z)=n\,\}$ is the Hilbert scheme, viewed as a moduli of rank-1 torsion-free sheaves with trivial determinant. Its deformation theory in the derived category gives a symmetric perfect obstruction theory of virtual dimension $\int_\beta c_1(T_X)$; for $d_\beta=0$ one sets
$$Z_{\mathrm{DT}}(X;q)_\beta=\sum_{n\in\mathbb{Z}} \Big(\int_{[I_n(X,\beta)]^{\mathrm{vir}}}1\Big)q^n .$$
Behrend's theorem identifies this with the weighted Euler characteristic $\sum_n q^n\,e(I_n(X,\beta),\nu)$ for the constructible function $\nu$.

**Descendents.** For $\gamma\in H^*(X)$, DT descendents use $\mathrm{ch}_{k+2}(\mathcal{F})$ of the universal sheaf; GW descendents use $\psi$-classes. MNOP II conjectures a **universal**, $X$-independent, $\mathbb{Q}[i,u]$-linear transformation matching the two descendent bases after $-q=e^{iu}$.

**Stable pairs.** Pandharipande–Thomas replace ideal sheaves by pairs $(F,s)$, $F$ pure 1-dimensional, $\mathrm{coker}(s)$ 0-dimensional, giving $Z_{\mathrm{PT}}$. The DT/PT conjecture $Z'_{\mathrm{DT}}=Z_{\mathrm{PT}}$ makes $Z_{\mathrm{PT}}$ the technically preferred model, since the degree-0 factor is absent by construction.

**Toric localization.** For toric $X$, the $T=(\mathbb{C}^*)^3$-fixed loci of $I_n(X,\beta)$ are finite, given by monomial ideals; the vertex contribution is the equivariant 3d-partition series $W(\lambda,\mu,\nu)$, and $Z_{\mathrm{DT}}$ is a sum over "vertex/edge" configurations — the DT counterpart of the topological vertex.

## 3. History & State of the Art (SOTA)

- **2003–2006.** Motivated by the topological vertex of Aganagic–Klemm–Mariño–Vafa and by Nekrasov's instanton partition functions, MNOP write the two *Compositio Mathematica* papers (I: 142 (2006) 1263–1285; II: 1286–1304) stating (C1)–(C3), the equivariant version for toric $X$, and the descendent correspondence.
- **2006–2009.** (C1) proved independently by J. Li, Behrend–Fantechi, and Levine–Pandharipande. Okounkov–Pandharipande prove the local-curve case via the GW/Hilbert/Sym triangle.
- **2009–2011.** Pandharipande–Thomas introduce stable pairs; Toda and Bridgeland prove DT/PT via Hall-algebra wall-crossing. Maulik–Oblomkov–Okounkov–Pandharipande prove the full equivariant GW/DT correspondence for **toric** 3-folds (*Invent. Math.* 186 (2011) 435–479).
- **2013–2017.** Pandharipande–Pixton prove rationality of descendent series for local curves and toric 3-folds, then GW/PT for the **quintic** and, more generally, for complete intersections in products of projective spaces (*JAMS* 30 (2017) 389–449; *Geom. Topol.* 18 (2014)).
- **2019–present.** Oblomkov–Okounkov–Pandharipande derive the descendent correspondence from vertex operators / the stable envelope formalism; K-theoretic and cohomological refinements (Nekrasov–Okounkov, Okounkov's Park City lectures) become the active frontier.

## 4. Partial Results / Verified Cases

| Case | Statement proved | Reference |
|---|---|---|
| $\beta=0$, all projective 3-folds | (C1) MacMahon formula | Li 2006; Behrend–Fantechi 2008; Levine–Pandharipande 2009 |
| Toric nonsingular 3-folds, all $\beta$, equivariant, primary insertions | (C2)+(C3) | MOOP, *Invent. Math.* 2011 |
| Local curves $N\to C$ ($N$ rank 2), equivariant | full GW/DT/Hilbert triangle | Okounkov–Pandharipande; Bryan–Pandharipande |
| Complete intersections in products of $\mathbb{P}^n$, e.g. the quintic $\subset\mathbb{P}^4$ | GW/PT for primary fields | Pandharipande–Pixton 2017 |
| All projective 3-folds, $\beta$ irreducible | rationality + correspondence | Pandharipande–Pixton, "GW/P descendent correspondence for toric 3-folds" methods; Pandharipande–Thomas 2009 (irreducible classes, BPS) |
| CY 3-folds, primary invariants | DT $=$ PT (wall-crossing) | Toda 2010; Bridgeland 2011 |
| $K3\times E$, abelian 3-folds, local surfaces | verified in families via Igusa/Jacobi form structure | Oberdieck–Pandharipande and successors |

Computationally, the conjecture is checked to high order in $q$ and $u$ for local $\mathbb{P}^2$, local $\mathbb{P}^1\times\mathbb{P}^1$, the resolved conifold, and the quintic through genus $\approx 50$ via the topological-vertex and BCOV computations.

## 5. Principal Obstacles

- **No common moduli space.** Stable maps and ideal sheaves are parametrized by unrelated spaces with unrelated obstruction theories; there is no known geometric correspondence inducing the identity — only equalities of numbers after resummation.
- **Degeneration alone is insufficient.** Both theories satisfy degeneration formulas, but the GW and DT relative theories match only if the correspondence already holds for the relative geometries, so induction needs a base case with enough rigidity. This is exactly what fails for a general projective 3-fold: it need not degenerate into toric or local-curve pieces.
- **Localization is unavailable off toric.** MOOP's proof is a torus-equivariant argument on vertex/edge data. A general $X$ has no torus action, so the entire computational engine (3d partitions, equivariant vertex, stable envelopes) disappears.
- **Rationality is not formal.** $Z'_{\mathrm{DT}}$ is an infinite series with no a-priori finiteness; only wall-crossing (available for CY3 or with strong stability structures) or explicit vertex computation currently produce rationality. For general $X$ the Behrend function and its identities are not controlled well enough.
- **Genus growth.** The change of variables $-q=e^{iu}$ mixes all genera at once. Any finite-genus GW result gives only a finite-order statement about $Z'_{\mathrm{DT}}$; conversely, DT results do not localize in $g$.

## 6. The Gap

Proved: the toric case (all $\beta$, equivariantly, with descendents), the local-curve case, and complete intersections in products of projective spaces. Open: an arbitrary nonsingular projective 3-fold — in particular one that is neither toric, nor a complete intersection of the treated form, nor deformable to such. The exact missing step is a **degeneration/cobordism argument that reduces an arbitrary $(X,\beta)$ to the known geometries while preserving both theories' relative invariants**, or, alternatively, a proof of (C2) for general $X$ via a wall-crossing formalism valid outside the Calabi–Yau (symmetric-obstruction) setting. Even the singular/Deligne–Mumford-stack version and the full descendent matrix for non-toric $X$ remain unestablished.

## 7. Current Research (as of June 2026)

- **Vertex-operator derivation.** Oblomkov–Okounkov–Pandharipande express the GW/PT descendent correspondence through explicit vertex operators, aiming at a formula with no toric input. Groups: ETH Zürich, Columbia, MIT.
- **Log/orbifold GW and log DT.** Maulik–Ranganathan and collaborators build a logarithmic DT theory whose degeneration behaviour is functorial, targeting the reduction step of Section 6. *(frontier — verify)*
- **Universal curve counts.** Pardon's framework for defining Gopakumar–Vafa-type invariants for symplectic Calabi–Yau 3-folds offers a route to integrality independent of algebraicity. *(frontier — verify)*
- **K-theoretic and refined correspondences.** Okounkov's school studies $K$-theoretic DT with Nekrasov's "membrane index", conjecturally matching refined topological strings; the cohomological limit recovers MNOP.
- **Cohomological DT / Joyce–Safronov and motivic lifts.** Attempts to upgrade (C2) to a statement about vanishing cycles that is manifestly rational.

## 8. Future Work

1. Prove rationality (C2) for all projective 3-folds — likely the highest-leverage single step, since (C3) then becomes an identity of rational functions checkable genus by genus.
2. Develop a degeneration formalism (logarithmic or expanded) in which every projective 3-fold degenerates to pieces with torus actions.
3. Extend the descendent correspondence matrix beyond toric targets; the matrix is conjecturally universal, so a single proof of universality would transport all toric results.
4. Prove the GW/DT correspondence for singular targets and orbifolds, aligning it with the crepant resolution conjecture.
5. Deduce integrality (Gopakumar–Vafa/BPS) statements directly from the DT side.

## 9. Key References

- **[Foundational]** D. Maulik, N. Nekrasov, A. Okounkov, R. Pandharipande. *Gromov–Witten theory and Donaldson–Thomas theory, I.* Compositio Mathematica 142 (2006), 1263–1285.
- **[Foundational]** D. Maulik, N. Nekrasov, A. Okounkov, R. Pandharipande. *Gromov–Witten theory and Donaldson–Thomas theory, II.* Compositio Mathematica 142 (2006), 1286–1304.
- **[SOTA]** D. Maulik, A. Oblomkov, A. Okounkov, R. Pandharipande. *Gromov–Witten/Donaldson–Thomas correspondence for toric 3-folds.* Inventiones Mathematicae 186 (2011), 435–479.
- **[SOTA]** R. Pandharipande, A. Pixton. *Gromov–Witten/Pairs correspondence for the quintic 3-fold.* Journal of the AMS 30 (2017), 389–449.
- **[SOTA]** R. Pandharipande, R. P. Thomas. *Curve counting via stable pairs in the derived category.* Inventiones Mathematicae 178 (2009), 407–447.
- **[Structural]** T. Bridgeland. *Hall algebras and curve-counting invariants.* Journal of the AMS 24 (2011), 969–998.
- **[Structural]** Y. Toda. *Curve counting theories via stable objects I: DT/PT correspondence.* Journal of the AMS 23 (2010), 1119–1157.
- **[Degree 0]** J. Li. *Zero dimensional Donaldson–Thomas invariants of threefolds.* Geometry & Topology 10 (2006), 2117–2171.
- **[Degree 0]** K. Behrend, B. Fantechi. *Symmetric obstruction theories and Hilbert schemes of points on threefolds.* Algebra & Number Theory 2 (2008), 313–345.
- **[Survey]** R. Pandharipande, R. P. Thomas. *13/2 ways of counting curves.* In *Moduli Spaces*, LMS Lecture Note Series 411, Cambridge University Press, 2014.
- **[Survey]** A. Okounkov. *Lectures on K-theoretic computations in enumerative geometry.* In *Geometry of Moduli Spaces and Representation Theory*, IAS/Park City Math. Series 24, AMS, 2017.

## 10. Worked Example / Concrete Special Case

**The resolved conifold, degree 1.** Let $X=\mathcal{O}_{\mathbb{P}^1}(-1)\oplus\mathcal{O}_{\mathbb{P}^1}(-1)\to\mathbb{P}^1$, a toric Calabi–Yau 3-fold, and $\beta=[\mathbb{P}^1]$. Since $K_X$ is trivial, $d_\beta=\int_\beta c_1(T_X)=0$, so the prefactor $(-iu)^{d_\beta}=1$.

*GW side.* The only curves in class $\beta$ are multiple covers of the rigid $(-1,-1)$ curve. The Faber–Pandharipande multiple-cover computation gives $N_{g,1}=\frac{|B_{2g}|}{2g\,(2g-2)!}$ for $g\ge 2$, $N_{0,1}=1$, $N_{1,1}=1/12$, and the resummation
$$Z'_{\mathrm{GW}}(X;u)_{\beta}=\sum_{g\ge0}N_{g,1}u^{2g-2}=\frac{1}{\big(2\sin(u/2)\big)^{2}}
= u^{-2}+\tfrac{1}{12}+\tfrac{u^{2}}{240}+\cdots .$$

*DT side.* Subschemes with $[Z]=\beta$ are the fibre $\mathbb{P}^1$ plus embedded/floating points; the reduced series is computed by the topological vertex (or by localization on $I_n$) to be
$$Z'_{\mathrm{DT}}(X;q)_{\beta}=\frac{q}{(1+q)^{2}},$$
a rational function, manifestly invariant under $q\mapsto 1/q$ — confirming (C2) here.

*Matching.* Put $-q=e^{iu}$, i.e. $q=-e^{iu}$. Then
$$\frac{q}{(1+q)^{2}}=\frac{-e^{iu}}{(1-e^{iu})^{2}} .$$
Meanwhile $\big(2\sin(u/2)\big)^{2}=\big(-i(e^{iu/2}-e^{-iu/2})\big)^{2}=-e^{-iu}(e^{iu}-1)^{2}$, so
$$\frac{1}{(2\sin(u/2))^{2}}=\frac{-e^{iu}}{(e^{iu}-1)^{2}}=\frac{q}{(1+q)^{2}} .$$
The two sides agree exactly, and since $d_\beta=0$ the normalization $(-q)^{-d_\beta/2}$ is trivial. Expanding the DT side in $q$ gives $q-2q^2+3q^3-\cdots$, i.e. virtual counts $\pm n$ on $I_n(X,\beta)$; expanding after substitution reproduces $1,\ 1/12,\ 1/240,\dots$, the genus-$0,1,2$ GW numbers. This one class already exhibits all three ingredients: MacMahon-normalized reduction, rationality with $q\leftrightarrow 1/q$ symmetry, and the trigonometric change of variables.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*