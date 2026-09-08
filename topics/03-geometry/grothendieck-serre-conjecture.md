---
id: 03-geometry/grothendieck-serre-conjecture
title: "Grothendieck-Serre Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Grothendieck-Serre Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/grothendieck-serre-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $R$ be a regular local ring with fraction field $K = \operatorname{Frac}(R)$, and let $G$ be a reductive group scheme over $R$ (affine, smooth, with connected reductive geometric fibers — the fibers need not be split or even quasi-split). The conjecture asserts:

> A principal $G$-bundle (a $G$-torsor) over $\operatorname{Spec} R$ that is trivial over the generic point is trivial.

Equivalently, in étale (equivalently fppf, since $G$ is smooth) non-abelian cohomology, the restriction map
$$H^1_{\text{ét}}(R,\,G) \longrightarrow H^1_{\text{ét}}(K,\,G)$$
has trivial kernel. A proof must handle arbitrary regular local $R$ (equal or mixed characteristic, ramified or not) and arbitrary reductive $R$-group schemes. A disproof requires an explicit $R$, $G$, and a nontrivial $G$-torsor $E \to \operatorname{Spec} R$ with $E(K) \neq \emptyset$.

Both hypotheses are sharp: dropping regularity of $R$ or reductivity of $G$ produces counterexamples (Section 10, Section 4).

## 2. Mathematical Foundations

**Torsors.** For a flat affine group scheme $G$ over a base $S$, a $G$-torsor is an $S$-scheme $E$ with an action $G \times_S E \to E$ such that $E \to S$ is faithfully flat, locally of finite presentation, and $G \times_S E \xrightarrow{\ (g,e)\,\mapsto\,(ge,e)\ } E \times_S E$ is an isomorphism. Isomorphism classes are classified by the pointed set $H^1_{\text{fppf}}(S,G)$; smoothness of $G$ gives $H^1_{\text{fppf}}(S,G) = H^1_{\text{ét}}(S,G)$ (Grothendieck).

**Reductive group schemes** (SGA3, Exp. XIX): $G \to S$ affine, smooth, finitely presented, with all geometric fibers $G_{\bar{s}}$ connected reductive. Each such $G$ is an inner twist of a quasi-split form, and is classified by a root datum plus a class in $H^1(S, \operatorname{Aut}(G_0))$.

**Local statement.** Writing $\mathfrak{m}$ for the maximal ideal, $k = R/\mathfrak{m}$, and $d = \dim R$, regularity means $\dim_k \mathfrak{m}/\mathfrak{m}^2 = d$. The conjecture is the injectivity-on-the-neutral-class statement
$$\ker\!\left[ H^1_{\text{ét}}(R,G) \to H^1_{\text{ét}}(K,G) \right] = \{*\}.$$

**Standard reductions and inputs.**
- *Purity/limit reduction:* by Noetherian approximation, one may take $R$ essentially of finite type over a field or over a Dedekind ring; the equicharacteristic case reduces to $R = \mathcal{O}_{X,x}$ for $X$ smooth affine over an infinite field $k$.
- *Nisnevich/Quillen patching:* a torsor over $\mathbb{A}^1_R$ trivial along a section and over $\mathbb{A}^1_{R}[1/f]$ can be glued from local data; this converts the problem into an extension problem for bundles on relative curves.
- *Geometric presentation lemma* (Ojanguren–Panin, after Quillen and Gabber): given $x \in X$ smooth affine over $k$ and a divisor $Z \ni x$, there is, after localizing, a smooth morphism $\pi: X \to \mathbb{A}^{d-1}_k$ of relative dimension one such that $\pi|_Z$ is finite and $Z$ meets the fiber through $x$ in a well-controlled way. This produces "nice triples" $(\mathcal{X} \to U, f, \Delta)$ used to move the locus of nontriviality off the closed point.
- *Abelian shadows:* for $G = \mathbb{G}_m$ the statement is $\operatorname{Pic}(R)=0$, true since regular local rings are UFDs (Auslander–Buchsbaum). For $G = \mathrm{PGL}_n$ it contains the Auslander–Goldman injectivity $\operatorname{Br}(R) \hookrightarrow \operatorname{Br}(K)$.

## 3. History & State of the Art (SOTA)

- **1958.** Serre, *Espaces fibrés algébriques* (Séminaire Chevalley), raises the question for $G$ defined over a field; Grothendieck, *Torsion homologique et sections rationnelles* (same seminar), formulates the general version. Grothendieck restates it in *Le groupe de Brauer II* (1968) after proving the $\mathrm{PGL}_n$ shadow.
- **1960s–80s.** Verified for tori and for $\dim R \le 1$: Colliot-Thélène–Sansuc (flasque resolutions, 1987) settle all $R$-tori; Nisnevich (1984) settles semilocal Dedekind $R$ under isotropy/quasi-splitness hypotheses.
- **1992.** Colliot-Thélène–Ojanguren prove the conjecture for $G$ *constant* (extended from an infinite base field $k$) and $R$ geometrically regular local over $k$ — the first high-dimensional case, via Quillen's patching plus a geometric presentation.
- **2015.** Panin–Stavrova–Vavilov prove the isotropic case over regular local $k$-algebras; Fedorov–Panin (Publ. IHÉS) prove the full equicharacteristic case for $R$ containing an **infinite** field.
- **2020.** Panin removes the infinitude assumption: the conjecture is a **theorem for every regular local ring containing a field**.
- **2022.** Mixed characteristic breaks open: Guo settles all semilocal Dedekind rings (no isotropy hypothesis); Česnavičius proves the **unramified quasi-split** case in mixed characteristic; Fedorov gives further unramified cases and generalizations to non-constant/semilocal settings.
- **State of the art (2026).** Equicharacteristic: solved. Mixed characteristic: solved when $R$ is unramified and $G$ quasi-split (or after further hypotheses), plus $\dim R \le 1$ unconditionally. **Ramified mixed characteristic with non-quasi-split $G$ remains open.**

## 4. Partial Results / Verified Cases

| Case | Hypotheses | Status / Author |
|---|---|---|
| $G$ a torus | any regular local $R$ | Proved — Colliot-Thélène–Sansuc (1987) |
| $G = \mathbb{G}_m$ | any regular local $R$ | $\operatorname{Pic}(R)=0$, Auslander–Buchsbaum |
| $G=\mathrm{PGL}_n$ | regular local $R$ | Auslander–Goldman (1960), Grothendieck (1968) |
| $\dim R = 1$ | semilocal Dedekind, any reductive $G$ | Proved — Nisnevich (1984, partial); Guo (2022, full) |
| $G$ constant over $k$, $R \supseteq k$ infinite field | $R$ geometrically regular | Colliot-Thélène–Ojanguren (1992) |
| $G$ isotropic | $R$ regular local containing a field | Panin–Stavrova–Vavilov (2015) |
| any reductive $G$ | $R$ regular local containing an **infinite** field | Fedorov–Panin (2015) |
| any reductive $G$ | $R$ regular local containing **any** field | Panin (2020) — equicharacteristic complete |
| $G$ quasi-split | $R$ **unramified** regular local, mixed char. | Česnavičius (2022) |
| $G$ with a specified reductive model over the base DVR | unramified mixed char., further hypotheses | Fedorov (2022) |
| **Not true in general** | $R$ non-regular, or $G$ non-reductive | Counterexamples (Section 10) |

Ranges: for $R$ essentially smooth over a field the result holds in every dimension $d \ge 0$. In mixed characteristic the unconditional range is $d \le 1$; $d \ge 2$ needs unramifiedness plus quasi-splitness.

## 5. Principal Obstacles

- **No geometric presentation lemma over a DVR base.** The equicharacteristic proofs rest on fibering $\operatorname{Spec} R$ (or a smooth model $X/k$) into a relative curve over $\mathbb{A}^{d-1}$ with the "bad" divisor finite over the base. Over $\mathbb{Z}_p$ or a ramified DVR, the closed fiber is not a hypersurface one can move: Gabber-style presentation requires a large residue field or an infinite base field to choose generic projections. The residue field is typically finite, and the mixed-characteristic analogue is only known in the unramified case (Česnavičius's version uses Popescu approximation plus a delicate Bertini argument over $\mathbb{Z}_p$).
- **Ramification destroys smoothness of the model.** If $R$ is ramified over $\mathbb{Z}_p$ (say $p \in \mathfrak{m}^2$), $\operatorname{Spec} R$ is not smooth over any DVR, so the relative-curve machinery, affine Grassmannian uniformization, and Beauville–Laszlo gluing all lose their base.
- **Non-quasi-split forms.** Reduction to a quasi-split inner form requires understanding the twisting class in $H^1(R, \operatorname{Aut} G)$, which is itself a torsor problem — circular in mixed characteristic. Tools like the Bruhat–Tits building and Steinberg's theorem need field hypotheses that do not hold for $\operatorname{Frac}$ of a higher-dimensional ring.
- **Failure of purity for exotic groups.** Even for $\mathrm{Spin}$ and exceptional groups, the needed purity statements ($H^1(R,G) \to \prod_{\text{ht }1} H^1(R_\mathfrak{p},G)$ injective) are theorems only where the conjecture itself is known.
- **No cohomological dimension bound.** Étale cohomological methods control $H^1$ with abelian coefficients; for non-abelian $G$ there is no exact sequence to push the class down to a $\dim \le 1$ situation.

## 6. The Gap

Proven (Section 4) covers: all $R$ containing a field, all $R$ of dimension $\le 1$, and $R$ unramified with $G$ quasi-split. The general statement (Section 1) additionally demands:

1. **$R$ ramified of mixed characteristic, $\dim R \ge 2$** — completely open, even for $G = \mathrm{SL}_1(D)$ or $\mathrm{Spin}(q)$;
2. **$R$ unramified, $\dim R \ge 2$, $G$ not quasi-split** — open outside the cases where the inner twisting class can be trivialized.

The precise missing step: a *presentation/moving lemma over a mixed-characteristic base* — given $\operatorname{Spec} R$ with $R$ regular local of mixed characteristic and a closed subscheme $Z$ containing the non-triviality locus of a torsor $E$, produce an elementary fibration $\mathcal{X} \to U$ with $\dim U = \dim R - 1$ such that $Z \to U$ is finite and $E|_{\mathcal{X}}$ extends to a torsor over a projective compactification. Everything downstream (Quillen patching, Fedorov–Panin's "nice triple" induction, Česnavičius's descent) is known to work once such a fibration exists.

## 7. Current Research (as of June 2026)

- **Česnavičius's school (Paris-Saclay/Orsay).** Extending the quasi-split unramified proof to ramified bases via Prüfer/valuation-ring techniques and purity for torsors over non-Noetherian bases. Related: torsors over Prüfer rings, $v$-sheaf and prismatic reformulations. *(frontier — verify)*
- **Guo and collaborators.** After the semilocal Dedekind theorem, work on *constant* reductive group schemes in mixed characteristic and on Nisnevich-type purity; preprints on "Grothendieck–Serre for constant reductive group schemes" circulate. *(frontier — verify)*
- **Fedorov (Pittsburgh) and Panin (Steklov, St. Petersburg).** Generalizations beyond reductive: to group schemes with toral/parabolic structure, to non-local semilocal regular domains, and to versions with several generic points.
- **Affine Grassmannian / Beauville–Laszlo methods.** Uniformizing $G$-bundles on relative curves over $\mathbb{Z}_p$, connected to work on the Fargues–Fontaine curve and $\mathbb{B}_{\mathrm{dR}}^+$-Grassmannians; the hope is that $p$-adic geometry supplies the missing moving lemma.
- **Bass–Quillen circle.** The parallel conjecture (every finitely generated projective $R[x_1,\dots,x_n]$-module extended from $R$) shares techniques and is still open for general regular $R$; progress transfers in both directions.

## 8. Future Work

- Prove a Gabber-type presentation lemma for regular local rings of mixed characteristic with possibly finite residue field; this is the single highest-value target.
- Combine Popescu's smoothing theorem with prismatic/perfectoid descent to remove the unramifiedness assumption.
- Prove purity for $H^1(-,G)$ over regular rings independently of the conjecture (Česnavičius's problem list), which would allow a codimension induction.
- Handle non-quasi-split inner forms by developing a mixed-characteristic analogue of the Bruhat–Tits/isotropy arguments of Panin–Stavrova–Vavilov.
- Extend to non-reductive but *pseudo-reductive* groups, and to semilocal regular domains with several maximal ideals, delimiting exactly where the statement fails.

## 9. Key References

- **[Foundational]** J.-P. Serre. *Espaces fibrés algébriques.* Séminaire C. Chevalley, 2ᵉ année, Exp. 1, ENS, 1958.
- **[Foundational]** A. Grothendieck. *Torsion homologique et sections rationnelles.* Séminaire C. Chevalley, 2ᵉ année, Exp. 5, ENS, 1958.
- **[Foundational]** A. Grothendieck. *Le groupe de Brauer II: théorie cohomologique.* In *Dix exposés sur la cohomologie des schémas*, North-Holland, 1968.
- **[Foundational]** M. Auslander, O. Goldman. *The Brauer group of a commutative ring.* Trans. Amer. Math. Soc. 97 (1960), 367–409. [DOI](https://doi.org/10.1090/s0002-9947-1960-0121392-6)
- **[Partial]** Y. Nisnevich. *Espaces homogènes principaux rationnellement triviaux et arithmétique des schémas en groupes réductifs sur les anneaux de Dedekind.* C. R. Acad. Sci. Paris Sér. I 299 (1984), 5–8.
- **[Partial]** J.-L. Colliot-Thélène, J.-J. Sansuc. *Principal homogeneous spaces under flasque tori: applications.* J. Algebra 106 (1987), 148–205. [DOI](https://doi.org/10.1016/0021-8693(87)90026-3)
- **[Partial]** J.-L. Colliot-Thélène, M. Ojanguren. *Espaces principaux homogènes localement triviaux.* Publ. Math. IHÉS 75 (1992), 97–122. [DOI](https://doi.org/10.1007/bf02699492)
- **[SOTA]** R. Fedorov, I. Panin. *A proof of the Grothendieck–Serre conjecture on principal bundles over regular local rings containing infinite fields.* Publ. Math. IHÉS 122 (2015), 169–193. [DOI](https://doi.org/10.1007/s10240-015-0075-z)
- **[SOTA]** I. Panin, A. Stavrova, N. Vavilov. *On Grothendieck–Serre's conjecture concerning principal $G$-bundles over reductive group schemes: I.* Compositio Math. 151 (2015), 535–567. [DOI](https://doi.org/10.1070/im8452)
- **[SOTA]** I. Panin. *Proof of the Grothendieck–Serre conjecture on principal bundles over regular local rings containing a finite field.* Izvestiya: Mathematics 84 (2020), 780–795. [DOI](https://doi.org/10.1070/im8982)
- **[SOTA]** K. Česnavičius. *Grothendieck–Serre in the quasi-split unramified case.* Forum of Mathematics, Pi 10 (2022), e9. [DOI](https://doi.org/10.1017/fmp.2022.5)
- **[SOTA]** N. Guo. *The Grothendieck–Serre conjecture over semilocal Dedekind rings.* Transformation Groups 27 (2022), 897–917.
- **[SOTA]** R. Fedorov. *On the Grothendieck–Serre conjecture about principal bundles and its generalizations.* Algebra & Number Theory 16 (2022), 447–465. [DOI](https://doi.org/10.2140/ant.2022.16.447)
- **[Survey]** I. Panin. *On Grothendieck–Serre conjecture concerning principal bundles.* Proc. International Congress of Mathematicians, Rio de Janeiro 2018, Vol. II, 201–221, World Scientific, 2018. [DOI](https://doi.org/10.1142/9789813272880_0051)
- **[Survey]** K. Česnavičius. *Problems about torsors over regular rings.* Acta Mathematica Vietnamica 47 (2022), 39–107. [DOI](https://doi.org/10.1007/s40306-022-00477-y)
- **[Background]** M. Demazure, A. Grothendieck (eds.). *Schémas en groupes (SGA 3), Tome III.* Lecture Notes in Math. 153, Springer, 1970.

## 10. Worked Example / Concrete Special Case

**(a) The abelian case $G = \mathbb{G}_m$.** Here $H^1_{\text{ét}}(R,\mathbb{G}_m) = \operatorname{Pic}(R)$. If $R$ is regular local, it is a UFD (Auslander–Buchsbaum), so every height-one prime is principal and $\operatorname{Pic}(R) = 0$. The conjecture holds trivially — the kernel is the whole (trivial) group.

**(b) Regularity is necessary.** Take $k$ a field and the cuspidal cubic
$$A = k[x,y]/(y^2 - x^3), \qquad \nu: A \hookrightarrow \tilde{A} = k[t], \quad x \mapsto t^2,\ y \mapsto t^3 .$$
The conductor is $\mathfrak{c} = (t^2) \subset k[t]$, and the conductor square gives the exact sequence
$$1 \to A^\times \to \tilde{A}^\times \times (A/\mathfrak{c})^\times \to (\tilde{A}/\mathfrak{c})^\times \to \operatorname{Pic}(A) \to \operatorname{Pic}(\tilde{A}) = 0 .$$
Since $\tilde{A}^\times = k^\times$, $(A/\mathfrak{c})^\times = k^\times$, and $(\tilde{A}/\mathfrak{c})^\times = (k[t]/t^2)^\times \cong k^\times \times (k,+)$, we get
$$\operatorname{Pic}(A) \cong (k,+) \neq 0 .$$
But $\operatorname{Frac}(A) = k(t)$ is a field, so $\operatorname{Pic}(\operatorname{Frac} A) = 0$: every one of these line bundles is generically trivial. The map $H^1(A,\mathbb{G}_m) \to H^1(K,\mathbb{G}_m)$ has kernel $(k,+)$. The singular point $(x,y)$ is exactly where regularity fails — the conjecture's hypothesis cannot be weakened.

**(c) A nonabelian instance: $R = \mathbb{Z}_p$, $G = \mathrm{PGL}_n$.** Torsors are classified by Azumaya $R$-algebras of degree $n$ modulo isomorphism, $H^1_{\text{ét}}(R,\mathrm{PGL}_n) \cong \{\text{Azumaya } R\text{-algebras of degree } n\}/\cong$, with the trivial class $M_n(R)$. Suppose $\mathcal{A}$ is Azumaya over $\mathbb{Z}_p$ with $\mathcal{A} \otimes_{\mathbb{Z}_p} \mathbb{Q}_p \cong M_n(\mathbb{Q}_p)$. Reduce mod $p$: $\bar{\mathcal{A}} = \mathcal{A}/p\mathcal{A}$ is a central simple $\mathbb{F}_p$-algebra of degree $n$. By Wedderburn's theorem ("every finite division ring is a field"), $\operatorname{Br}(\mathbb{F}_p) = 0$, so $\bar{\mathcal{A}} \cong M_n(\mathbb{F}_p)$. Choosing an $\mathbb{F}_p$-isomorphism and lifting the resulting splitting idempotents along the henselian surjection $\mathbb{Z}_p \to \mathbb{F}_p$ (idempotents lift over henselian local rings), one obtains $\mathcal{A} \cong M_n(\mathbb{Z}_p)$. The torsor is trivial, confirming the conjecture in this case.

Contrast: the quaternion algebra $\mathcal{A} = \left(\frac{u,\,p}{\mathbb{Z}_p}\right)$ with $u$ a non-square unit is *not* Azumaya over $\mathbb{Z}_p$ (its discriminant involves $p$), and its generic fiber is the division algebra over $\mathbb{Q}_p$ with invariant $\tfrac12 \in \operatorname{Br}(\mathbb{Q}_p) \cong \mathbb{Q}/\mathbb{Z}$ — nontrivial over $K$, so it is not a counterexample but rather illustrates that $H^1(K,G)$ is genuinely larger than $H^1(R,G)$; the conjecture only forbids nontrivial classes from *dying* generically.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*