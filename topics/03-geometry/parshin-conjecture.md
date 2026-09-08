---
id: 03-geometry/parshin-conjecture
title: "Parshin Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Parshin Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/parshin-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Parshin, 1978).** Let $X$ be a smooth projective variety over a finite field $\mathbb{F}_q$. Then the higher algebraic $K$-groups of $X$ are torsion:
$$K_i(X)\otimes_{\mathbb{Z}}\mathbb{Q}=0 \qquad \text{for all } i\ge 1 .$$

Equivalently (via the Adams eigenspace decomposition, Section 2), all higher Chow groups vanish rationally:
$$\mathrm{CH}^n(X,i)\otimes\mathbb{Q}=0\qquad\text{for all }n\ge 0,\ i\ge 1 .$$

The only rational $K$-theory allowed is $K_0(X)\otimes\mathbb{Q}$, which the conjecture predicts is the (finite-dimensional) space of cycles modulo rational equivalence.

**Assumptions that matter.** *Smooth* and *projective* are both essential: $K_1(\mathbb{A}^1_{\mathbb{F}_q}\setminus\{0\})\supseteq \mathbb{Z}$ (the class of $t$) is already non-torsion, so the conjecture fails for open varieties, and singular varieties carry non-torsion $K$-theory coming from their nilpotents/non-normality.

**What counts as a resolution.** A proof must produce, for every smooth projective $X/\mathbb{F}_q$ and every $i\ge 1$, a demonstration that each class in $K_i(X)$ is killed by a nonzero integer. A disproof requires one smooth projective $X/\mathbb{F}_q$ and one $i\ge1$ with a $K$-class of infinite order — equivalently a nonzero element of $H^j_{\mathcal M}(X,\mathbb{Q}(n))$ with $j\neq 2n$.

## 2. Mathematical Foundations

**$K$-theory and weights.** For $X$ a quasi-projective scheme over a field, Quillen's $K$-groups $K_i(X)=\pi_i\,\Omega BQ\mathcal{P}(X)$ carry Adams operations $\psi^k$, and rationally decompose into eigenspaces
$$K_i(X)_{\mathbb{Q}}=\bigoplus_{n\ge 0} K_i(X)^{(n)}_{\mathbb{Q}},\qquad \psi^k=k^n \text{ on } K_i(X)^{(n)}_{\mathbb{Q}} .$$
By Bloch's theorem relating higher Chow groups to $K$-theory (Bloch 1986; Landsburg, Levine),
$$K_i(X)^{(n)}_{\mathbb{Q}}\cong \mathrm{CH}^n(X,i)_{\mathbb{Q}}\cong H^{2n-i}_{\mathcal M}(X,\mathbb{Q}(n)),$$
for $X$ smooth. So Parshin's conjecture is exactly the statement that motivic cohomology of a smooth projective $X/\mathbb{F}_q$ is concentrated in the diagonal degree:
$$H^{j}_{\mathcal M}(X,\mathbb{Q}(n))=0\quad\text{for } j\neq 2n,\qquad H^{2n}_{\mathcal M}(X,\mathbb{Q}(n))=\mathrm{CH}^n(X)_{\mathbb{Q}} .$$

**Bloch's cycle complex.** $z^n(X,\bullet)$ has $z^n(X,i)$ = the free abelian group on codimension-$n$ subvarieties of $X\times\Delta^i$ meeting all faces properly, $\Delta^i=\mathrm{Spec}\,k[t_0,\dots,t_i]/(\sum t_j-1)$; $\mathrm{CH}^n(X,i)=H_i(z^n(X,\bullet))$.

**Input conjectures.**
- **Tate conjecture $T(X,n)$:** for $\ell\neq \mathrm{char}\,\mathbb{F}_q$, the cycle map $\mathrm{CH}^n(X)\otimes\mathbb{Q}_\ell\to H^{2n}_{\text{ét}}(X_{\overline{\mathbb{F}}_q},\mathbb{Q}_\ell(n))^{\mathrm{Frob}}$ is surjective; equivalently $\mathrm{ord}_{s=n}Z(X,q^{-s})=-\operatorname{rank}\mathrm{CH}^n(X)$ under semisimplicity.
- **Beilinson conjecture $B(X)$:** over $\overline{\mathbb{F}}_p$, rational and numerical equivalence agree, $\mathrm{CH}^n(X)_{\mathbb{Q}}\xrightarrow{\ \sim\ }\mathrm{CH}^n_{\mathrm{num}}(X)_{\mathbb{Q}}$.

**Key structural theorem (Geisser 1998).** Over all smooth projective varieties over finite fields, Parshin's conjecture $\iff$ Tate conjecture $+$ Beilinson conjecture. Precisely: $T$ and $B$ in dimensions $\le d$ imply Parshin's conjecture in dimensions $\le d$, and conversely Parshin implies $B$ and the order-of-vanishing form of $T$.

**Finiteness.** Quillen's finite generation conjecture ($K_i(X)$ finitely generated for $X$ regular of finite type over $\mathbb{Z}$) plus Parshin's conjecture is equivalent to: $K_i(X)$ is *finite* for all $i\ge1$, $X$ smooth projective over $\mathbb{F}_q$.

## 3. History & State of the Art (SOTA)

- **1972.** Quillen computes $K_i(\mathbb{F}_q)$: $K_0=\mathbb{Z}$, $K_{2m-1}(\mathbb{F}_q)=\mathbb{Z}/(q^m-1)$, $K_{2m}(\mathbb{F}_q)=0$ for $m\ge1$. This is the conjecture in dimension $0$ and the model for the general statement.
- **1977.** Harder's computation of the cohomology of $S$-arithmetic groups over function fields yields finiteness of $K_i$ for smooth projective **curves** over $\mathbb{F}_q$, $i\ge1$.
- **1978.** Parshin states the conjecture in his ICM-era work on abelian coverings of arithmetic schemes; it is the characteristic-$p$ half of the vanishing picture later embedded by Beilinson into the general conjectural framework for motivic cohomology (the "Beilinson–Parshin conjecture", often stated over $\overline{\mathbb{F}}_p$).
- **1984.** Soulé proves vanishing of $K_i(X)^{(n)}_{\mathbb{Q}}$ in low weights ($n\le 2$) for arbitrary smooth projective $X/\mathbb{F}_q$, and relates the conjecture to zeta-function orders of vanishing.
- **1998.** Geisser establishes the equivalence with Tate $+$ Beilinson, moving the problem entirely into the theory of algebraic cycles.
- **2000–2001.** Geisser–Levine describe motivic cohomology of fields and smooth schemes in characteristic $p$ with $\mathbb{Z}/p^r$ coefficients via logarithmic de Rham–Witt sheaves, controlling the $p$-primary part.
- **2003.** Kahn proves the agreement of rational and numerical equivalence for classes of varieties of abelian type over finite fields, feeding Geisser's criterion.
- **2008.** Geisser ("Parshin's conjecture revisited") reformulates the conjecture in terms of higher Chow groups of *affine* schemes and shows it implies finite generation statements for all schemes of finite type over $\mathbb{F}_p$.

Status: open in every dimension $\ge 2$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\dim X=0$ | $K_i(\mathbb{F}_q)$ finite for $i\ge1$; explicit $\mathbb{Z}/(q^m-1)$ | Quillen 1972 |
| $\dim X=1$ (smooth projective curves) | $K_i(X)$ finite for all $i\ge1$ | Harder 1977 |
| Weights $n\le 2$, all $\dim X$ | $K_i(X)^{(n)}_{\mathbb{Q}}=0$, $i\ge1$ | Soulé 1984 |
| Weights $n>\dim X$ | $H^j_{\mathcal M}(X,\mathbb{Q}(n))=0$ for $j>n+\dim X$ and $j\le n$ in the relevant range; combined with Soulé this closes the extreme weights | standard vanishing + Soulé duality |
| Cellular / linear varieties: $\mathbb{P}^d$, Grassmannians, flag varieties $G/P$ for split $G$, smooth projective toric varieties | $K_i(X)\cong K_i(\mathbb{F}_q)^{\oplus r}$, $r=$ number of cells; torsion for $i\ge1$ | projective-bundle / cellular decomposition |
| Severi–Brauer varieties, quadrics, products of the above | $K_*$ built from $K_*$ of finite-dimensional $\mathbb{F}_q$-algebras (finite fields by Wedderburn) — torsion in degrees $\ge1$ | Quillen 1973 |
| Abelian varieties and products of elliptic curves over $\mathbb{F}_q$ | Tate conjecture known (Tate 1966; Zarhin in char $p$); rational $=$ numerical known for products of elliptic curves (Spiess 1999) and for classes of abelian type (Kahn 2003) — Geisser's criterion then delivers Parshin in the corresponding motivic subcategory | Spiess 1999, Kahn 2003, Geisser 1998 |
| $p$-primary part, any $X$ | $K_i(X;\mathbb{Z}_p)$ controlled by logarithmic de Rham–Witt cohomology; the $p$-part of the conjecture is essentially understood | Geisser–Levine 2000 |

**Not known:** any single smooth projective *surface* of general type over $\mathbb{F}_q$ outside abelian/Kummer/cellular families; e.g. a generic smooth quintic surface in $\mathbb{P}^3_{\mathbb{F}_q}$.

## 5. Principal Obstacles

- **No construction of non-torsion-free cycles from geometry.** Proving $K_i(X)_{\mathbb{Q}}=0$ means proving *every* higher cycle is rationally trivial. There is no known machine that produces null-homotopies of cycles in $z^n(X,\bullet)$ beyond the moving lemma, which gives properness of intersections but no vanishing.
- **Regulators are unavailable.** Over $\mathbb{C}$ or a number field, Beilinson regulators to Deligne cohomology detect and constrain $K_i$. Over $\mathbb{F}_q$ every archimedean invariant is absent, and the $\ell$-adic Chern classes land in $H^{j}_{\text{ét}}(X,\mathbb{Q}_\ell(n))$, which vanishes in the relevant degrees for continuous cohomology of a scheme over a finite field — the target of the natural detection map is zero, so étale methods give *no lower bound obstruction* and equally no proof of vanishing.
- **Weight-monodromy is trivial here but useless.** The Weil conjectures pin down $H^*_{\text{ét}}$ completely; the failure point is not cohomology of $X$ but the *surjectivity* of the cycle map (Tate) and *injectivity* of rational-to-numerical (Beilinson) — both of which are known to be inaccessible to cohomological input alone.
- **Equivalence to Tate.** Geisser's theorem converts the problem into two of the hardest open conjectures on algebraic cycles. Any proof of Parshin's conjecture in dimension $\ge2$ proves the Tate conjecture in that dimension; this is a strong obstruction-to-easy-proof.
- **Motivic $t$-structure is conjectural.** The clean formulation "motivic cohomology is concentrated in degree $2n$" is exactly the statement that $DM(\mathbb{F}_q)_{\mathbb{Q}}$ restricted to pure motives is semisimple with vanishing higher $\mathrm{Ext}$; there is no unconditional construction of the abelian category of mixed motives to run this argument inside.
- **Induction on dimension breaks.** De Jong alterations reduce many statements to smooth projective covers, but the conjecture is not known to descend along alterations in a way that lowers dimension without reintroducing open or singular pieces.

## 6. The Gap

Proven: dimensions $0$ and $1$; weights $n\le 2$ and the dual extreme weights in all dimensions; the entire conjecture for varieties whose Chow motive is a sum of Tate motives, and for abelian-type classes where Tate $+$ Beilinson are known.

Conjectured: everything else — in particular weight $n=3$ on a threefold, or $\mathrm{CH}^2(S,1)_{\mathbb{Q}}=0$ for a general surface $S/\mathbb{F}_q$.

The precise missing step is: **for a smooth projective $X/\mathbb{F}_q$ of dimension $d\ge2$ whose motive is not of abelian type, prove that $\mathrm{CH}^n_{\mathrm{hom}}(X)_{\mathbb{Q}}=0$ (Beilinson) and that the $\ell$-adic cycle map hits all Frobenius-invariants (Tate).** Everything else in Geisser's chain is unconditional. No technique currently converts arithmetic information about $\mathrm{Frob}_q$ into the algebraicity of a Tate class.

## 7. Current Research (as of June 2026)

- **Weil-étale cohomology.** Geisser and Morin construct Weil-étale cohomology groups whose finiteness and Euler-characteristic properties are equivalent to, or implied by, Parshin's conjecture; the programme aims to derive special-value formulas for $\zeta(X,s)$ conditionally on it. Active in Japan (Geisser, Rikkyo) and France (Morin, Bordeaux).
- **Prismatic and syntomic methods.** Bhatt–Morrow–Scholze-style $p$-adic techniques and topological cyclic homology give complete control of $K(X;\mathbb{Z}_p)$ in characteristic $p$ (via Geisser–Levine and $TC$), which is why the $p$-part is not the bottleneck; the $\ell\neq p$ part remains untouched by these tools. *(frontier — verify for specific new preprints)*
- **Motives of abelian type.** Extensions of Kahn's method to Kimura-finite motives and to varieties with finite-dimensional Chow motives, seeking to enlarge the class where rational $=$ numerical is unconditional (schools around Kahn in Paris, and finite-dimensionality work following Kimura and O'Sullivan). *(frontier — verify)*
- **Tate conjecture for surfaces.** Progress on K3 and related surfaces over finite fields (Nygaard–Ogus; Charles; Madapusi Pera; Kim–Madapusi Pera in characteristic $2$) supplies new families where the Tate half is settled; the Beilinson half for these surfaces is the remaining input.

## 8. Future Work

- Prove the Beilinson conjecture (rational $=$ numerical over $\overline{\mathbb{F}}_p$) for a single class of surfaces of general type — Geisser has repeatedly identified this as the smallest genuinely new case.
- Develop a descent statement for higher Chow groups along de Jong alterations strong enough to run an induction on $\dim X$.
- Use Geisser's affine reformulation: Parshin's conjecture is equivalent to a vanishing statement for higher Chow groups of affine schemes over $\mathbb{F}_p$, potentially amenable to $\mathbb{A}^1$-homotopy-theoretic or cdh-descent arguments.
- Extract unconditional consequences from the Weil-étale picture to test the conjecture numerically against $\zeta$-function orders of vanishing for explicit varieties.

## 9. Key References

- **[Foundational]** A. N. Parshin. *Abelian coverings of arithmetic schemes.* Soviet Math. Doklady **19** (1978), 1438–1442 (Dokl. Akad. Nauk SSSR **243** (1978), 855–858).
- **[Foundational]** D. Quillen. *On the cohomology and K-theory of the general linear groups over a finite field.* Annals of Mathematics **96** (1972), 552–586. [DOI](https://doi.org/10.2307/1970825)
- **[Foundational]** D. Quillen. *Higher algebraic K-theory I.* Lecture Notes in Mathematics **341**, Springer, 1973, 85–147.
- **[Foundational]** G. Harder. *Die Kohomologie $S$-arithmetischer Gruppen über Funktionenkörpern.* Inventiones Mathematicae **42** (1977), 135–175.
- **[Foundational]** S. Bloch. *Algebraic cycles and higher K-theory.* Advances in Mathematics **61** (1986), 267–304. [DOI](https://doi.org/10.1016/0001-8708(86)90081-2)
- **[SOTA]** C. Soulé. *Groupes de Chow et K-théorie de variétés sur un corps fini.* Mathematische Annalen **268** (1984), 317–345.
- **[SOTA]** T. Geisser. *Tate's conjecture, algebraic cycles and rational K-theory in characteristic p.* K-Theory **13** (1998), 109–122. [DOI](https://doi.org/10.1023/a:1007709804443)
- **[SOTA]** T. Geisser, M. Levine. *The K-theory of fields in characteristic p.* Inventiones Mathematicae **139** (2000), 459–493.
- **[SOTA]** B. Kahn. *Équivalences rationnelle et numérique sur certaines variétés de type abélien sur un corps fini.* Annales Scientifiques de l'ÉNS (4) **36** (2003), 977–1002. [DOI](https://doi.org/10.1016/j.ansens.2003.02.002)
- **[SOTA]** M. Spiess. *Proof of the Tate conjecture for products of elliptic curves over finite fields.* Mathematische Annalen **314** (1999), 285–290. [DOI](https://doi.org/10.1007/s002080050295)
- **[Survey]** T. Geisser. *Parshin's conjecture revisited.* In: *K-Theory and Noncommutative Geometry*, EMS Series of Congress Reports, 2008, 413–425.
- **[Survey]** B. Kahn. *Algebraic K-theory, algebraic cycles and arithmetic geometry.* In: *Handbook of K-Theory*, Springer, 2005, 351–428. [DOI](https://doi.org/10.1007/978-3-540-27855-9_9)
- **[Survey]** J. Tate. *Conjectures on algebraic cycles in $\ell$-adic cohomology.* Proceedings of Symposia in Pure Mathematics **55** (1994), 71–83. [DOI](https://doi.org/10.1090/pspum/055.1/1265523)
- **[Reference]** C. Weibel. *The K-book: An Introduction to Algebraic K-theory.* Graduate Studies in Mathematics **145**, AMS, 2013.

## 10. Worked Example / Concrete Special Case

**Goal:** verify Parshin's conjecture for $X=\mathbb{P}^1_{\mathbb{F}_q}$ in weight $n=2$, degree $j=3$, i.e. show $H^3_{\mathcal M}(\mathbb{P}^1,\mathbb{Q}(2))=0$ — and see that the integral group is *nonzero but finite*, which is exactly what the conjecture asserts.

**Step 1 — projective bundle formula.** For motivic cohomology of $\mathbb{P}^1$ over any field $k$:
$$H^{j}_{\mathcal M}(\mathbb{P}^1,\mathbb{Z}(n))\cong H^{j}_{\mathcal M}(k,\mathbb{Z}(n))\ \oplus\ H^{j-2}_{\mathcal M}(k,\mathbb{Z}(n-1)).$$
With $j=3,n=2$:
$$H^{3}_{\mathcal M}(\mathbb{P}^1,\mathbb{Z}(2))\cong H^{3}_{\mathcal M}(k,\mathbb{Z}(2))\ \oplus\ H^{1}_{\mathcal M}(k,\mathbb{Z}(1)).$$

**Step 2 — motivic cohomology of a point.** For a field $k$, $H^j_{\mathcal M}(k,\mathbb{Z}(n))=0$ for $j>n$, so $H^3_{\mathcal M}(k,\mathbb{Z}(2))=0$. And $H^1_{\mathcal M}(k,\mathbb{Z}(1))=k^{\times}$.

**Step 3 — specialise.** For $k=\mathbb{F}_q$:
$$H^{3}_{\mathcal M}(\mathbb{P}^1_{\mathbb{F}_q},\mathbb{Z}(2))\cong \mathbb{F}_q^{\times}\cong \mathbb{Z}/(q-1),$$
finite of order $q-1$. Tensoring with $\mathbb{Q}$ gives $0$. Equivalently $K_1(\mathbb{P}^1)^{(2)}_{\mathbb{Q}}=0$.

**Step 4 — cross-check by Gersten/Milnor.** The same group is $H^1(\mathbb{P}^1,\mathcal{K}_2)$, the cokernel of the tame symbol
$$K_2\big(\mathbb{F}_q(t)\big)\ \xrightarrow{\ \partial=(\partial_x)\ }\ \bigoplus_{x\in(\mathbb{P}^1)^{(1)}} k(x)^{\times}.$$
Milnor's exact sequence with $K_2(\mathbb{F}_q)=0$ (Steinberg/Quillen: $K_2$ of a finite field vanishes) gives $K_2(\mathbb{F}_q(t))\cong\bigoplus_{\pi\ \text{monic irred.}}k(\pi)^{\times}$, so $\partial$ is onto the affine components. Weil reciprocity $\prod_x N_{k(x)/\mathbb{F}_q}(\partial_x f)=1$ shows the image is contained in the kernel of the total norm $N:\bigoplus_x k(x)^{\times}\to\mathbb{F}_q^{\times}$, and equality holds. Hence
$$H^1(\mathbb{P}^1,\mathcal{K}_2)\cong \operatorname{coker}\partial\cong \mathbb{F}_q^{\times}=\mathbb{Z}/(q-1),$$
matching Step 3.

**Numerical instance.** $q=5$: $H^3_{\mathcal M}(\mathbb{P}^1_{\mathbb{F}_5},\mathbb{Z}(2))\cong\mathbb{Z}/4$. Every class is killed by $4$; nothing survives rationally.

**Why this is only a toy.** $\mathbb{P}^1$ is cellular, so $K_i(\mathbb{P}^1)\cong K_i(\mathbb{F}_q)^{\oplus 2}$ is torsion in all degrees $i\ge1$ for free. For an elliptic curve $E/\mathbb{F}_q$ the analogue $H^3_{\mathcal M}(E,\mathbb{Z}(2))=H^1(E,\mathcal{K}_2)$ has no cellular shortcut, and its finiteness rests on Harder's cohomological computation. For a surface $S/\mathbb{F}_q$ the corresponding group $\mathrm{CH}^2(S,1)$ has no known finiteness proof at all — that is where the conjecture starts.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*