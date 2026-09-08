---
id: 03-geometry/beilinson-conjectures
title: "Beilinson Conjectures"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Beilinson Conjectures

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/beilinson-conjectures` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective variety over $\mathbb{Q}$ of dimension $d$, and fix $0 \le i \le 2d$ and an integer $n$. Attached to the motive $h^i(X)$ is an $L$-function $L(h^i(X), s)$, defined by an Euler product over primes $p$,
$$L(h^i(X),s) = \prod_p \det\!\big(1 - \mathrm{Frob}_p\, p^{-s} \mid H^i_{\text{ét}}(X_{\overline{\mathbb{Q}}}, \mathbb{Q}_\ell)^{I_p}\big)^{-1},$$
convergent for $\mathrm{Re}(s) > \frac{i}{2}+1$ and conjecturally continued meromorphically to $\mathbb{C}$.

Beilinson conjectures that the leading Taylor coefficient of $L(h^i(X),s)$ at every integer point is computed by a **regulator determinant** on algebraic $K$-theory. Precisely, in the *non-critical* range $n > \frac{i}{2}+1$:

1. **(Rank)** $\dim_{\mathbb{Q}} H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}}, \mathbb{Q}(n)) = \operatorname{ord}_{s=i+1-n} L(h^i(X),s)$, and this dimension is finite.
2. **(Regulator isomorphism)** The Beilinson regulator induces an isomorphism of real vector spaces
$$r_{\mathcal{D}} \otimes \mathbb{R}:\; H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}}, \mathbb{Q}(n)) \otimes_{\mathbb{Q}} \mathbb{R} \;\xrightarrow{\ \sim\ }\; H^{i+1}_{\mathcal{D}}(X_{/\mathbb{R}}, \mathbb{R}(n)).$$
3. **(Special value)** The determinant of $r_{\mathcal{D}}$, computed against the $\mathbb{Q}$-structure on the source given by motivic cohomology and on the target given by Betti–de Rham rational structures, satisfies
$$\det(r_{\mathcal{D}}) \cdot \mathbb{Q}^\times \;=\; L^*(h^i(X), i+1-n)\cdot \mathbb{Q}^\times ,$$
where $L^*$ denotes the leading nonzero Taylor coefficient.

At the *near-central* point $n = \frac{i}{2}+1$ ($i$ even) the source must be enlarged by the $\mathbb{Q}$-span of algebraic cycle classes (a Néron–Severi type correction); at the central point the statement degenerates into the Beilinson–Bloch height conjecture, generalising Birch–Swinnerton-Dyer.

A complete proof requires establishing (1)–(3) for all $X$, $i$, $n$; a disproof requires one variety where the rational number $\det(r_\mathcal{D})/L^*$ is provably irrational or where the rank fails.

## 2. Mathematical Foundations

**Motivic cohomology.** Beilinson defines, via Adams eigenspaces of Quillen $K$-theory,
$$H^j_{\mathcal{M}}(X, \mathbb{Q}(n)) := K_{2n-j}(X)^{(n)}_{\mathbb{Q}},$$
identified by Bloch's higher Chow groups: $H^j_{\mathcal{M}}(X,\mathbb{Q}(n)) \cong \mathrm{CH}^n(X, 2n-j)_{\mathbb{Q}}$. Low-weight cases: $H^1_{\mathcal{M}}(X,\mathbb{Q}(1)) = \mathcal{O}(X)^\times \otimes \mathbb{Q}$, $H^2_{\mathcal{M}}(X,\mathbb{Q}(1)) = \mathrm{Pic}(X)_{\mathbb{Q}}$.

**Integral part.** For a regular proper flat model $\mathcal{X}/\mathbb{Z}$, set
$$H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}},\mathbb{Q}(n)) := \mathrm{Im}\big(H^{i+1}_{\mathcal{M}}(\mathcal{X},\mathbb{Q}(n)) \to H^{i+1}_{\mathcal{M}}(X,\mathbb{Q}(n))\big).$$
Model-independence of this image is itself part of the conjectural package; Scholl (2000) gave an intrinsic characterisation by local conditions when no good model is available.

**Deligne–Beilinson cohomology.** For a complex manifold $X(\mathbb{C})$, $H^\bullet_{\mathcal{D}}(X,\mathbb{R}(n))$ is hypercohomology of
$$\mathbb{R}(n)_{\mathcal{D}}:\quad \mathbb{R}(n) \longrightarrow \mathcal{O}_X \longrightarrow \Omega^1_X \longrightarrow \cdots \longrightarrow \Omega^{n-1}_X ,$$
with $\mathbb{R}(n)=(2\pi i)^n\mathbb{R}$; for $X$ over $\mathbb{R}$ one takes the subspace fixed by the composite of complex conjugation on coefficients and on points. Deligne's computation of $\Gamma$-factors gives
$$\dim_{\mathbb{R}} H^{i+1}_{\mathcal{D}}(X_{/\mathbb{R}},\mathbb{R}(n)) = \operatorname{ord}_{s=i+1-n} L(h^i(X),s) \quad (n > \tfrac{i}{2}+1),$$
so part (1) of the conjecture is equivalent to $r_{\mathcal{D}}$ being surjective and injective modulo torsion.

**The regulator.** $r_{\mathcal{D}}$ is the Chern character from $K$-theory to Deligne cohomology, realised concretely by explicit currents: for $n=2$, $i=1$ the map on $K_2$ of a curve is Bloch's
$$\{f,g\} \;\longmapsto\; \Big[\gamma \mapsto \int_\gamma \log|f|\, d\arg g - \log|g|\, d\arg f\Big] \in H^1(X(\mathbb{C}),\mathbb{R})^-.$$
Burgos Gil (2002) proved that this Beilinson regulator agrees, up to an explicit factor of $2$, with the Borel regulator on $K_\bullet$ of number rings.

**Refinement.** Bloch–Kato (1990) sharpen "$\cdot\,\mathbb{Q}^\times$" to an exact equality of Tamagawa measures, pinning the rational number; Fontaine–Perrin-Riou recast this as the equivariant Tamagawa number conjecture.

## 3. History & State of the Art (SOTA)

- **1839–1930s.** Dirichlet's class number formula: $\operatorname{ord}_{s=0}\zeta_F(s)=r_1+r_2-1$ with leading coefficient the unit regulator. This is Beilinson's conjecture for $X=\operatorname{Spec} F$, $i=0$, $n=1$.
- **1974–1977.** Borel computes $K_{2n-1}(\mathcal{O}_F)\otimes\mathbb{Q}$ and relates its regulator covolume to $\zeta_F^*(1-n)$ up to $\mathbb{Q}^\times$ — the first higher case.
- **1977–1980.** Bloch's Irvine lectures on $K_2$ of elliptic curves; Deligne's Corvallis conjecture on *critical* values as periods (1979) supplies the complementary picture.
- **1984.** Beilinson, *Higher regulators and values of $L$-functions*, unifies Dirichlet, Borel, Deligne and BSD in one framework.
- **1986–1990.** Beilinson proves the modular curve case; Deninger handles Hecke $L$-series of imaginary quadratic fields; Bloch–Grayson compute $K_2$ regulators of elliptic curves numerically.
- **1988–1994.** Rapoport–Schappacher–Schneider volume and Nekovář's *Motives* survey stabilise the formulation.
- **1990–2004.** Bloch–Kato Tamagawa refinement; Kato's Euler system yields deep partial results for modular forms.
- **2000s–2020s.** Numerical verification programme (Dokchitser–de Jeu–Zagier; Brunault; de Jeu) and Mahler-measure identities; higher regulators of Shimura varieties (Kings, Lemma, Cauchi).

Status: the conjecture is a theorem only for restricted classes; no general case beyond $\dim \le 2$ mixed Tate/modular situations is known.

## 4. Partial Results / Verified Cases

| Class | Result | Author, year |
|---|---|---|
| $X=\operatorname{Spec}\mathcal{O}_F$, all $n\ge 2$ | Conjecture true up to $\mathbb{Q}^\times$ | Borel 1977 |
| $\zeta_F(2)$, all number fields | Dilogarithm formula | Bloch, Zagier, Suslin |
| Modular curves $X_1(N)$, $i=1$, $n=2$ | Proved | Beilinson 1986; Schappacher–Scholl 1991 |
| CM elliptic curves / Hecke characters of imaginary quadratic fields | Proved for $n\ge 2$ | Deninger 1989, 1990 |
| Dirichlet motives $\mathbb{Q}(\chi)$, all $n$ | Bloch–Kato form proved (up to $p=2$) | Huber–Kings 2003 |
| Hilbert modular surfaces, $n=2$ | Proved | Kings 1998 |
| Modular forms, weight $k\ge 2$, non-critical $n$ | One inclusion via Beilinson–Kato Euler system | Kato 2004 |
| Products of modular curves | Integral elements constructed; rank inequality | Scholl 2000 |
| Hyperelliptic curves, $K_2$, genus $\le 3$ | Numerically verified to $\sim$25 digits | Dokchitser–de Jeu–Zagier 2006 |
| Elliptic curves over $\mathbb{Q}$, $K_2$, conductor $\le \sim 5000$ | Numerical agreement | Bloch–Grayson 1986; Brunault |
| Siegel threefolds, $\mathrm{GSp}_4$, $n$ near-central | Non-vanishing of regulator classes | Lemma 2017 |

Uniformly, proofs exist where **explicit motivic elements** are available: cyclotomic/Beilinson elements, Siegel units, Eisenstein symbols, polylogarithm sheaves.

## 5. Principal Obstacles

- **No supply of motivic classes.** For a general variety, no method constructs elements of $H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}},\mathbb{Q}(n))$. Every proved case rides on a modular/automorphic source of units or Eisenstein classes. For, say, a generic quintic threefold there is not one known nonzero class.
- **Finiteness is open.** $\dim H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}},\mathbb{Q}(n)) < \infty$ is unproved in general (it is essentially Bass' finite generation conjecture for $K$-theory of regular $\mathbb{Z}$-schemes). Even $K_2$ of an elliptic surface over $\mathbb{Z}$ resists.
- **Upper bounds need Euler systems.** Bounding motivic cohomology from above requires controlling Selmer groups; Euler systems exist only in the few settings (cyclotomic, Kato, Heegner) with norm-compatible geometric families. There is no construction machine.
- **Transcendence.** Statement (3) asserts the *ratio* of two transcendental numbers is rational. Analytic and Diophantine techniques give no leverage: for $\zeta(3)$ alone, irrationality is Apéry's, and nothing beyond is known. So numerical checks can never be upgraded to proof by analysis.
- **$L$-functions are conjectural.** For most $X$ the meromorphic continuation of $L(h^i(X),s)$ past $\mathrm{Re}(s)>\frac{i}{2}+1$ is unknown, so the right-hand side does not yet exist — this forces the automorphic detour and explains why Langlands-modular cases are the only ones settled.
- **Model dependence.** Defining the integral subspace requires regular proper models; resolution of singularities in mixed characteristic is not available in general.

## 6. The Gap

Proved cases occupy the region where the motive is *automorphic and of small rank*: $h^0$ of number fields, $h^1$ of modular curves and CM elliptic curves, and their Tate twists. The general statement quantifies over all smooth projective $X/\mathbb{Q}$, all $i$, all $n$.

The exact missing step is a **two-sided rank computation**: a construction functor producing $\ge \operatorname{ord}_{s=i+1-n}L$ independent motivic classes for arbitrary $X$, matched by an Euler-system bound showing no more exist. Currently only sporadic constructions on one side and Kato-type bounds in one family on the other are available. Bridging requires either (a) a general theory of motivic $L$-values from the conjectural motivic $t$-structure on $\mathrm{DM}(\mathbb{Q})$ — which itself needs the standard conjectures — or (b) a functorial transfer moving proved automorphic cases along Langlands functoriality to all motives, which needs full potential automorphy in every rank and weight.

## 7. Current Research (as of June 2026)

- **Higher regulators of Shimura varieties.** Kings (Regensburg), Lemma (Paris), Cauchi, Rodrigues Jacinto: motivic Eisenstein classes and Siegel units for $\mathrm{GSp}_4$, $\mathrm{GU}(2,1)$, aiming at $n$ near-central. Non-vanishing at the boundary is the recurring technical core.
- **Euler systems programme.** Loeffler–Zerbes (UCL/Heidelberg) and collaborators: Lefschetz-type and Rankin–Eisenstein classes give Bloch–Kato bounds for $\mathrm{GSp}_4$ and $\mathrm{GL}_2\times\mathrm{GL}_2$ motives; these feed the upper-bound half of Beilinson's rank prediction. *(frontier — verify: extensions to higher-rank groups announced in preprint form.)*
- **Mahler measures.** Brunault, Zudilin, Rogers: identities $m(P) = c\cdot L'(E,0)$ are instances of Beilinson for $K_2$ of curves; many remain conjectural and numerically verified only.
- **$p$-adic analogues.** Syntomic regulators and rigid-syntomic Beilinson conjectures (Besser, Bannai, Nekovář–Nizioł); progress here is faster because $p$-adic $L$-functions are constructible.
- **Motivic homotopy input.** Use of $\mathbb{A}^1$-homotopy and Milnor–Witt refinements to control the integral part. *(frontier — verify.)*
- **Numerics.** PARI/Magma and de Jeu's algorithms verify new curve and surface families to high precision; useful as falsification tests, never as proof.

## 8. Future Work

- Prove finite-dimensionality of $H^{i+1}_{\mathcal{M}}(X_{\mathbb{Z}},\mathbb{Q}(n))$ for surfaces over $\mathbb{Z}$ — the first genuinely new rank input in decades.
- Extend Scholl's intrinsic definition of the integral part to all $X$, removing dependence on regular models.
- Construct Eisenstein/polylogarithm classes for unitary and orthogonal Shimura varieties, then push to non-cohomological weights.
- Prove Beilinson for $h^2$ of a K3 surface with large Picard rank, where cycle-class corrections at the near-central point can be computed explicitly.
- Attack the transcendence side: any unconditional statement that a specific regulator/$L$-value ratio is rational would be a first.

## 9. Key References

- **[Foundational]** A. A. Beilinson. *Higher regulators and values of $L$-functions.* Itogi Nauki i Tekhniki, Sovremennye Problemy Matematiki 24 (1984), 181–238; English transl. J. Soviet Math. 30 (1985), 2036–2070. [DOI](https://doi.org/10.1007/bf02105861)
- **[Foundational]** A. Borel. *Cohomologie de $SL_n$ et valeurs de fonctions zêta aux points entiers.* Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 4 (1977), 613–636.
- **[Foundational]** P. Deligne. *Valeurs de fonctions $L$ et périodes d'intégrales.* Proc. Sympos. Pure Math. 33.2, AMS, 1979, 313–346. [DOI](https://doi.org/10.1090/pspum/033.2/546622)
- **[Foundational]** S. Bloch, K. Kato. *$L$-functions and Tamagawa numbers of motives.* The Grothendieck Festschrift, Vol. I, Progr. Math. 86, Birkhäuser, 1990, 333–400.
- **[Survey]** M. Rapoport, N. Schappacher, P. Schneider (eds.). *Beilinson's Conjectures on Special Values of $L$-Functions.* Perspectives in Mathematics 4, Academic Press, 1988 (incl. P. Schneider, *Introduction to the Beilinson conjectures*).
- **[Survey]** J. Nekovář. *Beilinson's conjectures.* In: Motives, Proc. Sympos. Pure Math. 55.1, AMS, 1994, 537–570.
- **[Survey]** J. I. Burgos Gil. *The Regulators of Beilinson and Borel.* CRM Monograph Series 15, AMS, 2002. [DOI](https://doi.org/10.1090/crmm/015)
- **[Partial]** A. Beilinson. *Higher regulators of modular curves.* Contemp. Math. 55 (1986), 1–34. [DOI](https://doi.org/10.1090/conm/055.1/862627)
- **[Partial]** C. Deninger. *Higher regulators and Hecke $L$-series of imaginary quadratic fields I.* Invent. Math. 96 (1989), 1–69; *II*, Ann. of Math. 132 (1990), 131–158. [DOI](https://doi.org/10.2307/1971502)
- **[Partial]** G. Kings. *Higher regulators, Hilbert modular surfaces, and special values of $L$-functions.* Duke Math. J. 92 (1998), 61–127. [DOI](https://doi.org/10.1215/s0012-7094-98-09202-x)
- **[Partial]** A. Huber, G. Kings. *Bloch–Kato conjecture and Main Conjecture of Iwasawa theory for Dirichlet characters.* Duke Math. J. 119 (2003), 393–464. [DOI](https://doi.org/10.1215/s0012-7094-03-11931-6)
- **[Partial]** K. Kato. *$p$-adic Hodge theory and values of zeta functions of modular forms.* Astérisque 295 (2004), 117–290.
- **[Structural]** A. J. Scholl. *Integral elements in $K$-theory and products of modular curves.* NATO Sci. Ser. C 548, Kluwer, 2000, 467–489. [DOI](https://doi.org/10.1007/978-94-011-4098-0_17)
- **[Computational]** S. Bloch, D. Grayson. *$K_2$ and $L$-functions of elliptic curves: computer calculations.* Contemp. Math. 55 (1986), 79–88.
- **[SOTA / Recent]** T. Dokchitser, R. de Jeu, D. Zagier. *Numerical verification of Beilinson's conjecture for $K_2$ of hyperelliptic curves.* Compositio Math. 142 (2006), 339–373.
- **[SOTA / Recent]** F. Brunault, W. Zudilin. *Many Variations of Mahler Measures: A Lasting Symphony.* Aust. Math. Soc. Lecture Series 28, Cambridge University Press, 2020.

## 10. Worked Example / Concrete Special Case

Take $X = \operatorname{Spec}\mathbb{Q}$, so $d=0$, $i=0$, $h^0(X)$ has $L$-function $\zeta(s)$. Fix $n=3$ (non-critical: $n > \frac{i}{2}+1 = 1$). The conjecture predicts a statement about $s = i+1-n = -2$.

**Analytic side.** $\zeta(s)$ has a simple trivial zero at $s=-2$, so $\operatorname{ord}_{s=-2}\zeta(s) = 1$. From the functional equation
$$\zeta(s) = 2^s\pi^{s-1}\sin\!\big(\tfrac{\pi s}{2}\big)\Gamma(1-s)\zeta(1-s),$$
differentiating at $s=-2$ (where $\sin(\pi s/2)$ vanishes) gives the exact leading coefficient
$$\zeta'(-2) = -\frac{\zeta(3)}{4\pi^{2}}.$$

**Motivic side.** $H^{1}_{\mathcal{M}}(\operatorname{Spec}\mathbb{Z},\mathbb{Q}(3)) = K_5(\mathbb{Z})\otimes\mathbb{Q}$. Borel's theorem gives $\operatorname{rank} K_{2n-1}(\mathbb{Z}) = 1$ for $n$ odd $\ge 3$ and $0$ for $n$ even; here $\operatorname{rank} K_5(\mathbb{Z}) = 1$. (In fact $K_5(\mathbb{Z})\cong\mathbb{Z}$.) Rank prediction (1) holds: $1 = 1$. Cross-check at $n=2$: $\zeta(-1) = -\tfrac1{12}\neq 0$ so the order is $0$, and indeed $K_3(\mathbb{Z})\otimes\mathbb{Q}=0$.

**Target.** For $\operatorname{Spec}\mathbb{Q}$ one has $H^1_{\mathcal{D}}(\operatorname{Spec}\mathbb{R},\mathbb{R}(n)) = \mathbb{R}(n-1)^{c=\mathrm{id}}$, which is $\mathbb{R}$ for $n$ odd and $0$ for $n$ even. For $n=3$ it is one-dimensional, matching the source.

**Regulator.** Let $\xi$ generate $K_5(\mathbb{Z})$ modulo torsion. Borel's theorem states $R_3 := r_{\mathcal{D}}(\xi)$ satisfies
$$\zeta(3) = q\cdot R_3 \quad\text{for some } q\in\mathbb{Q}^\times,$$
and Burgos Gil (2002) fixes the normalisation between Borel's and Beilinson's regulators (a factor $2$ per degree). Combining with the functional-equation identity,
$$\zeta'(-2) = -\frac{q\,R_3}{4\pi^{2}} \;\in\; \mathbb{Q}^\times\cdot \pi^{-2} \det(r_{\mathcal{D}}).$$
The factor $\pi^{-2} = (2\pi i)^{-2}$ up to $\mathbb{Q}^\times$ is exactly the discrepancy between the Betti and de Rham rational structures on $H^1_{\mathcal{D}}$ that enters $\det(r_{\mathcal{D}})$ in statement (3). So the conjecture is verified in this case — and one sees the whole mechanism: a $K$-theory class of rank matching a trivial zero, a transcendental regulator, and a period power tracking the twist.

The next case up, $X$ an elliptic curve over $\mathbb{Q}$ with $i=1$, $n=2$, replaces $K_5(\mathbb{Z})$ by $K_2(\mathcal{E})$ and $R_3$ by Bloch's integral $\int_\gamma \log|f|\,d\arg g - \log|g|\,d\arg f$; that case is proved only for CM and modular-parametrised situations, and verified numerically otherwise.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*