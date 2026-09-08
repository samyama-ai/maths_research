---
id: 03-geometry/hodge-conjecture
title: "Hodge Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hodge Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/hodge-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective variety over $\mathbb{C}$ (equivalently, a compact complex manifold embedded in some $\mathbb{P}^N$). Every rational cohomology class of type $(k,k)$ is a $\mathbb{Q}$-linear combination of the fundamental classes of algebraic subvarieties of codimension $k$.

Formally, the cycle class map
$$\mathrm{cl}_k \colon \mathrm{CH}^k(X)\otimes\mathbb{Q}\;\longrightarrow\; \mathrm{Hdg}^k(X):=H^{2k}(X,\mathbb{Q})\cap H^{k,k}(X)$$
is **surjective** for all $k\ge 0$.

Constraints and scope:
- **Projective is essential.** The statement is false for general compact Kähler manifolds (Voisin 2002), so no proof can be purely transcendental.
- **$\mathbb{Q}$-coefficients are essential.** The integral form ($\mathrm{cl}_k\colon \mathrm{CH}^k(X)\to H^{2k}(X,\mathbb{Z})\cap H^{k,k}$ surjective) is false (Atiyah–Hirzebruch 1962; Kollár 1992).
- A **complete proof** must produce, for each Hodge class $\alpha$, subvarieties $Z_i\subset X$ of codimension $k$ and $n_i\in\mathbb{Q}$ with $\alpha=\sum n_i[Z_i]$. A **disproof** requires an explicit smooth projective $X$ and $\alpha\in\mathrm{Hdg}^k(X)$ outside the image of $\mathrm{cl}_k$.

One of the seven Clay Millennium Problems (Deligne 2006).

## 2. Mathematical Foundations

**Hodge decomposition.** For $X$ compact Kähler of dimension $n$, harmonic theory gives
$$H^m(X,\mathbb{C})\;=\;\bigoplus_{p+q=m}H^{p,q}(X),\qquad \overline{H^{p,q}}=H^{q,p},\qquad H^{p,q}(X)\cong H^q(X,\Omega_X^p).$$
Setting $F^pH^m=\bigoplus_{p'\ge p}H^{p',m-p'}$ gives a decreasing Hodge filtration; $(H^m(X,\mathbb{Q}),F^\bullet)$ is a pure $\mathbb{Q}$-Hodge structure of weight $m$.

**Hodge classes.** $\mathrm{Hdg}^k(X)=H^{2k}(X,\mathbb{Q})\cap H^{k,k}(X)$. Equivalently, $\alpha$ is Hodge iff the associated map $\mathbb{Q}(-k)\to H^{2k}(X,\mathbb{Q})$ is a morphism of Hodge structures; iff $\alpha$ is fixed by the Mumford–Tate group $\mathrm{MT}(H^{2k})$ up to the Tate twist.

**Cycle classes.** An irreducible closed subvariety $Z\subset X$ of codimension $k$ has a class $[Z]\in H^{2k}(X,\mathbb{Z})$ (Poincaré dual of the homology class of a resolution). Since $Z$ carries a $(k,k)$-form representative, $[Z]\in\mathrm{Hdg}^k(X)$: the conjecture asserts the converse.

**Structural inputs the problem leans on.**
- *Lefschetz $(1,1)$*: $\mathrm{cl}_1$ is surjective onto $\mathrm{Hdg}^1(X)$, even integrally. Proof: the exponential sequence $0\to\mathbb{Z}\to\mathcal{O}_X\xrightarrow{\exp}\mathcal{O}_X^*\to0$ gives $\mathrm{Pic}(X)\xrightarrow{c_1}H^2(X,\mathbb{Z})\to H^2(X,\mathcal{O}_X)=H^{0,2}$, and a class is $(1,1)$ exactly when it dies in $H^{0,2}$.
- *Hard Lefschetz*: for $L=\cup\,[H]$ the hyperplane class, $L^{n-m}\colon H^m(X,\mathbb{Q})\xrightarrow{\ \sim\ }H^{2n-m}(X,\mathbb{Q})$.
- *Hodge–Riemann bilinear relations*, giving polarizations and finiteness of the relevant arithmetic groups.
- *Deligne's semisimplicity / global invariant cycle theorem*, used in almost every degeneration argument.

**Variants.** The *variational* Hodge conjecture (Grothendieck): a flat deformation of an algebraic class staying Hodge stays algebraic. The *general* Hodge conjecture on coniveau filtrations, corrected by Grothendieck (1969). The *absolute Hodge* conjecture (Deligne): Hodge classes are absolutely Hodge — weaker, still open in general, known for abelian varieties (Deligne 1982).

## 3. History & State of the Art (SOTA)

- **1924.** Lefschetz proves the $(1,1)$ theorem in *L'analysis situs et la géométrie algébrique*; the case $k=1$ has been settled ever since.
- **1950.** W. V. D. Hodge states the conjecture in his ICM plenary address, Cambridge MA, "The topological invariants of algebraic varieties", including the integral form and the (false) general conjecture on coniveau.
- **1962.** Atiyah–Hirzebruch produce torsion classes in $H^{2k}(X,\mathbb{Z})$ that are Hodge but not algebraic, via differentials in the Atiyah–Hirzebruch spectral sequence — the integral statement dies.
- **1969.** Grothendieck: "Hodge's general conjecture is false for trivial reasons", and gives the corrected coniveau formulation.
- **1977–79.** Zucker proves the conjecture for cubic fourfolds; Shioda settles large families of Fermat varieties.
- **1992.** Kollár's Trento example: a very general degree-$d$ hypersurface $X\subset\mathbb{P}^4$ with $d$ divisible by a suitable prime power has a non-algebraic *non-torsion* integral Hodge class.
- **1995.** Cattani–Deligne–Kaplan: the locus of Hodge classes in a family is a countable union of algebraic subvarieties — the strongest unconditional evidence, since it is a prediction of the conjecture.
- **1997–2006.** Totaro reinterprets Atiyah–Hirzebruch via complex cobordism; Soulé–Voisin and Voisin sharpen integral counterexamples (uniruled and Calabi–Yau threefolds).
- **2002.** Voisin: a complex torus of dimension 4 with no nonzero subtori carries a non-algebraic Hodge class — the Kähler extension is false.
- **2019–2023.** Buskin proves every rational Hodge isometry between two K3 surfaces is algebraic; Markman settles Weil classes on abelian fourfolds of Weil type with discriminant $1$.

No general approach has changed the landscape for $k\ge2$ since Hodge stated it.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $k=1$ and (by hard Lefschetz) $k=n-1$, any $X$ | Proved, integrally for $k=1$ (Lefschetz 1924) |
| $\dim X\le 3$ | Proved: only $k=0,1,2,3$ occur, all covered |
| $X$ with $H^{2k}$ spanned by algebraic classes: $\mathbb{P}^n$, Grassmannians, flag varieties, smooth toric varieties, $H^\bullet$-cellular varieties | Proved trivially |
| Cubic fourfolds $X_3\subset\mathbb{P}^5$ | Zucker (1977) |
| Fermat varieties $X_d^n\subset\mathbb{P}^{n+1}$ for $d\le 20$ and many $(n,d)$ with $d$ prime or $d\le 4$ | Shioda (1979), Ran, Aoki–Shioda |
| Abelian varieties of dimension $\le 3$; simple abelian varieties of prime dimension | Tate, Tankeev, Ribet: $\mathrm{Hdg}^\bullet$ generated by divisor classes |
| Abelian varieties of dimension $4$ and $5$ | Moonen–Zarhin (1999): all Hodge classes are divisor-generated *except* Weil classes; conjecture reduced to these |
| Weil classes on abelian fourfolds with CM by $\mathbb{Q}(\sqrt{-3})$ | Schoen (1988) |
| Weil classes on abelian fourfolds of Weil type with discriminant $1$ | Markman (2023) |
| Products $S_1\times S_2$ of K3 surfaces, Hodge isometry classes | Buskin (2019); Huybrechts, Markman refinements |
| Uniruled/rationally connected fourfolds, $K3^{[n]}$-type hyper-Kähler varieties in low degree | Conte–Murre, Charles–Markman: many families |
| $\dim X=4$, general | **Open** — the first genuinely open dimension |

## 5. Principal Obstacles

- **No construction machine.** Only three sources of algebraic classes exist: Lefschetz $(1,1)$ (i.e. line bundles), Chern classes of coherent sheaves, and pushforward along correspondences. All three ultimately reduce to divisors on some auxiliary variety. There is no known mechanism to manufacture a codimension-$2$ cycle from cohomological data alone.
- **Sheaf-theoretic route blocked in degree $\ge 4$.** The $(1,1)$ proof works because $H^2(X,\mathcal{O}_X)$ receives an exact-sequence obstruction. For $k\ge2$ there is no exponential sequence: the analogous statement would need a "$K$-theory exponential", and the Atiyah–Hirzebruch differentials show any such map cannot be surjective integrally. Rationalising kills the torsion obstruction but leaves no replacement construction.
- **Hodge classes do not deform.** The Hodge locus is a countable union of proper subvarieties (CDK 1995), so a class on a special member typically has no counterpart on nearby members. Deformation/degeneration arguments — the workhorse for divisors — therefore cannot spread algebraicity across a family.
- **Chow groups are enormous.** Mumford (1968): if $H^{2,0}(S)\ne0$ then $\mathrm{CH}_0(S)$ is infinite-dimensional. So $\mathrm{CH}^k(X)\otimes\mathbb{Q}$ is not a finite-dimensional object that a linear-algebra or moduli argument can enumerate; the kernel of $\mathrm{cl}_k$ is wildly non-representable.
- **The transcendental method is provably insufficient.** Voisin's Weil-type complex torus satisfies every Hodge-theoretic hypothesis in sight and still fails. Hence any proof must use projectivity — an ample class — in an essential, non-formal way. Nobody knows what that use looks like beyond hard Lefschetz.
- **Motivic reformulations are equivalent, not easier.** Grothendieck's standard conjectures ($B$, $D$) and absolute Hodge are all open and mutually entangled; assuming any one does not unlock the others.

## 6. The Gap

Everything proved lives in two regimes: (i) $k\in\{1,n-1\}$, where divisors suffice; (ii) varieties whose Hodge structures are so constrained (CM abelian varieties, Fermat, K3-type, cellular) that $\mathrm{Hdg}^k$ is *forced* to be divisor-generated or is matched with an explicit correspondence.

The gap is the first case where neither holds: a Hodge class $\alpha\in\mathrm{Hdg}^2(X)$ on a fourfold whose Mumford–Tate group is large enough that $\alpha$ is not in $\mathbb{Q}[\mathrm{Hdg}^1(X)]$, and whose Hodge structure is not of a recognised motivic shape. The required step is a **construction principle**: given $\alpha$ Hodge, produce a coherent sheaf $\mathcal{F}$ on $X$ (or a correspondence from a known variety) with $\mathrm{ch}_2(\mathcal{F})$ matching $\alpha$ modulo divisor terms. Equivalently, prove that the Hodge locus of $\alpha$ in a versal deformation — which CDK show is algebraic — is the locus where a cycle exists. No technique converts "the locus is algebraic" into "a cycle exists there".

## 7. Current Research (as of June 2026)

- **Abelian fourfolds of Weil type.** After Markman's discriminant-$1$ theorem (JEMS 2023), the arbitrary-discriminant case is the sharpest concrete target; work by Markman, O'Grady and van Geemen's school uses hyper-Kähler moduli (generalized Kummer varieties, intermediate Jacobians) to realise Weil classes as cycle classes. Extensions to discriminant $\ne1$ are being circulated *(frontier — verify)*.
- **Hodge loci and o-minimality.** Baldi–Klingler–Ullmo (*Invent. Math.* 2024) prove the atypical Hodge locus is algebraic, using Pila–Wilkie definability. Groups at Paris (Klingler, Ullmo/IHES), Toronto and Milano are pushing toward a Zilber–Pink picture of where Hodge classes concentrate.
- **Hyper-Kähler geometry.** Markman, Charles, Huybrechts, Voisin: Hodge classes on $K3^{[n]}$-type and OG10 varieties, Kuga–Satake constructions, and the Beauville–Voisin conjectural filtration.
- **Derived/noncommutative approaches.** Kuznetsov components of cubic fourfolds and Gushel–Mukai fourfolds as a substitute "K3 motive"; Bayer–Macrì stability conditions to construct sheaves with prescribed Chern characters.
- **$p$-adic and arithmetic transfer.** Work relating Hodge to Tate via integral $p$-adic Hodge theory and prismatic cohomology (Bhatt–Scholze school) — mostly indirect for now *(frontier — verify)*.
- **Integral refinements.** Voisin, Colliot-Thélène, Benoist, Ottem: for which classes of varieties (rationally connected threefolds, real varieties) does the integral Hodge conjecture hold, and what does its failure measure about rationality.

## 8. Future Work

- **Attack the variational conjecture first.** Grothendieck's version is a statement about deformations of *known* cycles and is strictly weaker; Bloch's semiregularity and Deligne's $p$-adic approaches (Bloch–Esnault–Kerz, 2013–2018) give partial deformation results that could be pushed to characteristic $0$ families.
- **Finish abelian varieties.** Moonen–Zarhin reduce dimensions $4,5$ to Weil classes; a uniform construction of Weil-class cycles for all CM fields and all discriminants would be the first "new class of cycles" since Schoen.
- **Find a codimension-$2$ exponential.** Formulate an obstruction theory on $K_0(X)$ or on Deligne cohomology $H^4_{\mathcal{D}}(X,\mathbb{Z}(2))$ whose vanishing characterises algebraicity — Voisin has repeatedly flagged this as the missing structural ingredient.
- **Use projectivity essentially.** Since the Kähler statement is false, isolate a positivity input (Hodge-index style, or from the ample cone) that discriminates Voisin's torus from projective fourfolds, and build a proof around it.
- **Test for counterexamples.** Systematically search families with large Mumford–Tate groups (Voisin's programme) for Hodge classes with no plausible cycle; a single such example would resolve the problem negatively.

## 9. Key References

- **[Foundational]** W. V. D. Hodge. *The topological invariants of algebraic varieties.* Proceedings of the International Congress of Mathematicians (Cambridge, MA, 1950), vol. 1, AMS, 1952, 182–192.
- **[Foundational]** S. Lefschetz. *L'analysis situs et la géométrie algébrique.* Gauthier-Villars, Paris, 1924. [DOI](https://doi.org/10.1090/s0002-9904-1925-04116-6)
- **[Foundational]** M. F. Atiyah, F. Hirzebruch. *Analytic cycles on complex manifolds.* Topology 1 (1962), 25–45. [DOI](https://doi.org/10.1016/0040-9383(62)90094-0)
- **[Foundational]** A. Grothendieck. *Hodge's general conjecture is false for trivial reasons.* Topology 8 (1969), 299–303. [DOI](https://doi.org/10.1016/0040-9383(69)90016-0)
- **[Foundational]** D. Mumford. *Rational equivalence of 0-cycles on surfaces.* J. Math. Kyoto Univ. 9 (1968), 195–204. [DOI](https://doi.org/10.1215/kjm/1250523940)
- **[SOTA / Recent]** E. Cattani, P. Deligne, A. Kaplan. *On the locus of Hodge classes.* J. Amer. Math. Soc. 8 (1995), 483–506. [DOI](https://doi.org/10.1090/s0894-0347-1995-1273413-2)
- **[SOTA / Recent]** C. Voisin. *A counterexample to the Hodge conjecture extended to Kähler varieties.* Int. Math. Res. Not. 2002, no. 20, 1057–1075.
- **[SOTA / Recent]** B. Moonen, Yu. Zarhin. *Hodge classes on abelian varieties of low dimension.* Math. Ann. 315 (1999), 711–733. [DOI](https://doi.org/10.1007/s002080050333)
- **[SOTA / Recent]** C. Schoen. *Hodge classes on self-products of a variety with an automorphism.* Compositio Math. 65 (1988), 3–32.
- **[SOTA / Recent]** N. Buskin. *Every rational Hodge isometry between two K3 surfaces is algebraic.* J. reine angew. Math. (Crelle) 755 (2019), 127–150.
- **[SOTA / Recent]** E. Markman. *The monodromy of generalized Kummer varieties and algebraic cycles on their intermediate Jacobians.* J. Eur. Math. Soc. 25 (2023), 231–321. [DOI](https://doi.org/10.4171/jems/1199)
- **[SOTA / Recent]** G. Baldi, B. Klingler, E. Ullmo. *On the distribution of the Hodge locus.* Invent. Math. 235 (2024), 441–487. [DOI](https://doi.org/10.1007/s00222-023-01226-0)
- **[SOTA / Recent]** B. Totaro. *Torsion algebraic cycles and complex cobordism.* J. Amer. Math. Soc. 10 (1997), 467–493. [DOI](https://doi.org/10.1090/s0894-0347-97-00232-4)
- **[SOTA / Recent]** C. Soulé, C. Voisin. *Torsion cohomology classes and algebraic cycles on complex projective manifolds.* Adv. Math. 198 (2005), 107–127. [DOI](https://doi.org/10.1016/j.aim.2004.10.022)
- **[Classical special case]** S. Zucker. *The Hodge conjecture for cubic fourfolds.* Compositio Math. 34 (1977), 199–209.
- **[Classical special case]** T. Shioda. *The Hodge conjecture for Fermat varieties.* Math. Ann. 245 (1979), 175–184. [DOI](https://doi.org/10.1007/bf01428804)
- **[Survey]** P. Deligne. *The Hodge conjecture.* In: The Millennium Prize Problems, Clay Mathematics Institute / AMS, 2006, 45–53.
- **[Survey]** J. D. Lewis. *A Survey of the Hodge Conjecture*, 2nd ed. CRM Monograph Series 10, AMS, 1999.
- **[Survey / Textbook]** C. Voisin. *Hodge Theory and Complex Algebraic Geometry I, II.* Cambridge Studies in Advanced Mathematics 76, 77, CUP, 2002–2003.
- **[Survey]** A. Weil. *Abelian varieties and the Hodge ring.* Collected Papers, vol. III, Springer, 1979, 421–429. [DOI](https://doi.org/10.1007/978-1-4757-1705-1_123)

## 10. Worked Example / Concrete Special Case

**(a) The case that works: $k=1$ on an abelian surface.**

Let $A=\mathbb{C}^2/\Lambda$ be an abelian surface, so $H^1(A,\mathbb{Z})\cong\Lambda^\vee\cong\mathbb{Z}^4$ and $H^2(A,\mathbb{Z})\cong\wedge^2\Lambda^\vee\cong\mathbb{Z}^6$. With $h^{2,0}=h^{0,2}=1$, $h^{1,1}=4$, a class $\alpha\in H^2(A,\mathbb{Z})$ is Hodge iff its $(2,0)$-part vanishes, i.e. iff the alternating form $E_\alpha\colon\Lambda\times\Lambda\to\mathbb{Z}$ satisfies the **Riemann relation**
$$E_\alpha(ix,iy)=E_\alpha(x,y).$$
The exponential sequence gives $H^1(A,\mathcal{O}^*)\xrightarrow{c_1}H^2(A,\mathbb{Z})\to H^2(A,\mathcal{O}_A)=H^{0,2}$, and $\alpha\mapsto 0$ in $H^{0,2}$ precisely under that relation. So $\alpha=c_1(L)$ for a line bundle $L$, and $c_1(L)=[D]$ for a divisor $D$ (difference of two effective divisors after twisting by an ample class). Every Hodge class here is algebraic — **integrally**. Note what did the work: an exact sequence of sheaves in which $\mathcal{O}_A^*$ appears.

**(b) The case that fails to yield: Weil classes on an abelian fourfold.**

Let $K=\mathbb{Q}(\sqrt{-d})$ be imaginary quadratic and let $A$ be a $4$-dimensional abelian variety with an action $K\hookrightarrow\mathrm{End}(A)\otimes\mathbb{Q}$ such that $H^1(A,\mathbb{Q})$ is a $K$-vector space $V$ of dimension $4$, and the two eigenvalue-multiplicities of $K$ acting on $H^{1,0}$ are equal: $(2,2)$. Such $A$ is *of Weil type*. Then
$$W:=\wedge^4_K V\;\subset\;\wedge^4_{\mathbb{Q}}V=H^4(A,\mathbb{Q})$$
is a $K$-line, i.e. $\dim_{\mathbb{Q}}W=2$, and the balanced signature $(2,2)$ forces $W\subset H^{2,2}(A)$. So $W\subset\mathrm{Hdg}^2(A)$.

Now count. The divisor-generated part of $\mathrm{Hdg}^2$ is the image of $\mathrm{Sym}^2\mathrm{Hdg}^1(A)\to H^4(A,\mathbb{Q})$. For a *general* member of the Weil family, $\mathrm{Hdg}^1(A)$ is spanned by a single polarization class $\theta$, so the divisor-generated subspace of $\mathrm{Hdg}^2$ is the line $\mathbb{Q}\theta^2$. Weil's computation shows $W\cap\mathbb{Q}\theta^2=0$ for suitable choices, hence
$$\dim_\mathbb{Q}\bigl(\mathrm{Hdg}^2(A)\big/\mathbb{Q}[\mathrm{Hdg}^1(A)]\bigr)\;\ge\;2 .$$
These two dimensions are exactly the classes with no divisor-theoretic source. Moonen–Zarhin (1999) prove these are the *only* exceptional Hodge classes for $\dim A\le5$. Schoen (1988) constructed the cycles when $K=\mathbb{Q}(\sqrt{-3})$ and Markman (2023) when the Hermitian form has discriminant $1$; for general $(K,\text{discriminant})$ nobody can write down a surface $Z\subset A$ with $[Z]$ spanning $W$.

**(c) Why the two cases differ.** In (a) the class is $c_1$ of a sheaf produced by a sheaf sequence. In (b) any cycle would have to come from a correspondence with an auxiliary variety, and Voisin's Kähler counterexample is built from exactly this configuration — a $4$-dimensional Weil-type complex *torus* with no subtori, where the identical Hodge class exists and is provably not algebraic. The only difference between Voisin's torus and $A$ is projectivity. That single hypothesis is what a proof must exploit, and no one knows how.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*