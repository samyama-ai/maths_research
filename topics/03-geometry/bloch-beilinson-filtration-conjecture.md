---
id: 03-geometry/bloch-beilinson-filtration-conjecture
title: "Bloch-Beilinson Filtration Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bloch-Beilinson Filtration Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bloch-beilinson-filtration-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

For every smooth projective variety $X$ over a field $k$, the rational Chow groups $CH^j(X)_{\mathbb Q} = CH^j(X)\otimes\mathbb Q$ are expected to carry a canonical finite descending filtration
$$CH^j(X)_{\mathbb Q}=F^0 \supseteq F^1 \supseteq F^2 \supseteq \cdots \supseteq F^{j} \supseteq F^{j+1}=0$$
whose graded pieces are controlled by cohomology: $\mathrm{Gr}_F^\nu CH^j(X)_{\mathbb Q}$ should depend only on the degree-$(2j-\nu)$ cohomology of $X$, so that the "motivic" part of a Chow group is separated from its transcendental, infinite-dimensional part.

**Conjecture (Bloch–Beilinson).** There is a filtration $F^\bullet$ on $CH^\bullet(-)_{\mathbb Q}$, functorial for the category of smooth projective $k$-varieties, satisfying axioms (BB1)–(BB5) of §2. A complete solution means: construct such a filtration unconditionally (or prove no such filtration exists). Constructions satisfying (BB1)–(BB4) are known; the open content is (BB5), the vanishing $F^{j+1}CH^j(X)_{\mathbb Q}=0$, together with canonicity.

## 2. Mathematical Foundations

Let $X$ be smooth projective over $k$ of dimension $d$, and fix a Weil cohomology $H^\bullet$ (Betti for $k\subseteq\mathbb C$). A correspondence is a class $\Gamma\in CH^{d+j-i}(X\times Y)_{\mathbb Q}$, acting by $\Gamma_*(z)=p_{Y*}(\Gamma\cdot p_X^*z)$ on $CH^i(X)_{\mathbb Q}\to CH^{j}(Y)_{\mathbb Q}$. Write $[\Gamma]=\sum_{p+q=2(d+j-i)}[\Gamma]^{p,q}$ for the Künneth decomposition of its cohomology class in $\bigoplus_p H^p(X)\otimes H^{q}(Y)$.

**Axioms.**
- **(BB1)** $F^0CH^j(X)_{\mathbb Q}=CH^j(X)_{\mathbb Q}$ and $F^1CH^j(X)_{\mathbb Q}=CH^j_{\hom}(X)_{\mathbb Q}$, the kernel of the cycle class map $cl: CH^j(X)_{\mathbb Q}\to H^{2j}(X)$.
- **(BB2)** $F^r CH^i(X)_{\mathbb Q}\cdot F^s CH^j(X)_{\mathbb Q}\subseteq F^{r+s}CH^{i+j}(X)_{\mathbb Q}$ for the intersection product.
- **(BB3)** $F^\bullet$ is stable under $f^*$ and $f_*$, hence under all correspondences: $\Gamma_*F^\nu\subseteq F^\nu$.
- **(BB4)** The induced map $\Gamma_*:\mathrm{Gr}^\nu_F CH^i(X)_{\mathbb Q}\to \mathrm{Gr}^\nu_F CH^{j}(Y)_{\mathbb Q}$ vanishes whenever the Künneth component $[\Gamma]^{2d-2i+\nu,\,2j-\nu}$ vanishes. (Equivalently: $\mathrm{Gr}^\nu_F CH^j$ is a functor of the motive $h^{2j-\nu}$.)
- **(BB5)** $F^{j+1}CH^j(X)_{\mathbb Q}=0$.

**Conjectural origin.** Beilinson derives $F^\bullet$ from a conjectural abelian category $\mathcal{MM}_k$ of mixed motives with a spectral sequence
$$E_2^{p,q}=\mathrm{Ext}^p_{\mathcal{MM}_k}\big(\mathbf 1,\,h^{q}(X)(j)\big)\Longrightarrow CH^j(X)_{\mathbb Q},\qquad p+q=2j,$$
$F^\bullet$ being the induced filtration. Degeneration plus the Beilinson–Soulé vanishing $\mathrm{Ext}^p=0$ for $p<0$ gives (BB5). Then
$$\mathrm{Gr}^\nu_F CH^j(X)_{\mathbb Q}\;\cong\;\mathrm{Ext}^\nu_{\mathcal{MM}_k}\big(\mathbf 1, h^{2j-\nu}(X)(j)\big).$$
In particular $\mathrm{Gr}^0_F CH^j$ is the image of $cl$ (algebraic classes) and $\mathrm{Gr}^1_F CH^j$ should be the image of the Abel–Jacobi map, $\mathrm{Ext}^1$ in the category of $1$-motives / mixed Hodge structures.

**Murre's reformulation.** $X$ admits a *Chow–Künneth decomposition* if $\Delta_X=\sum_{i=0}^{2d}\pi_i$ in $CH^d(X\times X)_{\mathbb Q}$ with $\pi_i$ orthogonal idempotents and $[\pi_i]=$ the Künneth projector onto $H^i(X)$. Murre's conjectures add: $\pi_i$ acts as $0$ on $CH^j(X)_{\mathbb Q}$ for $i<j$ and $i>2j$; the filtration
$$F^\nu CH^j(X)_{\mathbb Q}:=\ker \pi_{2j}\cap\cdots\cap\ker\pi_{2j-\nu+1}$$
is independent of the chosen $\pi_i$. Jannsen (1994) proved: **Murre's conjectures hold for all smooth projective $X$ $\iff$ a Bloch–Beilinson filtration exists**, and the filtration is then unique.

## 3. History & State of the Art (SOTA)

- **1968–1976.** Mumford shows $CH_0$ of a surface with $p_g>0$ is "infinite-dimensional"; Roitman extends this. Bloch (1976) analyses $CH_0$ of abelian varieties. These results say Chow groups are *not* cohomological, forcing any comparison to be filtered rather than direct.
- **1980.** Bloch's *Lectures on Algebraic Cycles* formulates the conjecture that for a surface, $F^2CH^2 = T(X)$ (the Albanese kernel) is governed by $H^{2,0}$ — the surface case of the general filtration.
- **1987.** Beilinson, in *Height pairing between algebraic cycles*, states the conjectural filtration as a consequence of the existence of $\mathcal{MM}_k$ with the Ext-spectral sequence, together with the conjecture that for $k=\overline{\mathbb Q}$ one has $F^2=0$ (Beilinson–Bloch conjecture: Abel–Jacobi is injective on $CH^j_{\hom}(X)_{\mathbb Q}$ over number fields).
- **1990–1993.** Murre gives the correspondence-theoretic reformulation and proves Chow–Künneth for surfaces.
- **1992–1994.** Jannsen proves semisimplicity of numerical motives, then the equivalence "Murre $\Leftrightarrow$ Bloch–Beilinson".
- **1996–2005.** Unconditional *candidate* filtrations satisfying (BB1)–(BB4) built by S. Saito (via cycle-theoretic descending induction) and by Green–Griffiths / Lewis; all conjecturally coincide, all lack (BB5). Kimura and O'Sullivan introduce finite-dimensionality of motives, which yields nilpotence of homologically trivial correspondences and hence (BB5) for the relevant class.

## 4. Partial Results / Verified Cases

- **Curves ($d=1$):** trivially true; $F^1CH^1=\mathrm{Pic}^0\otimes\mathbb Q$, $F^2=0$ since Abel–Jacobi is an isomorphism.
- **Surfaces:** Murre (1990) constructs Chow–Künneth for every smooth projective surface, giving $F^\bullet$ with $F^3CH^2=0$; but (BB5) in the form "$p_g=0\Rightarrow F^2CH^2=0$" is Bloch's conjecture, still open in general — known for surfaces not of general type (Bloch–Kas–Lieberman, 1976), for Godeaux, Barlow (Barlow 1985), Catanese and Kimura-finite examples, and for various families via Voisin's degeneration/spread techniques.
- **Abelian varieties $A$ of dimension $d$:** Beauville's Fourier transform gives $CH^p(A)_{\mathbb Q}=\bigoplus_s CH^p_{(s)}(A)_{\mathbb Q}$ with $n^*x=n^{2p-s}x$; Deninger–Murre give the corresponding Chow–Künneth decomposition, also in families. Beauville proved $CH^p_{(s)}=0$ for $s<p-d$ and $s>p$; the full axiom (BB5) reduces to Beauville's vanishing conjecture $CH^p_{(s)}=0$ for $s<0$, which is a theorem for $p=0,1$ and for $0$-cycles $p=d$ (Beauville 1983: $CH^d(A)_{\mathbb Q}=\bigoplus_{s=0}^{d}CH^d_{(s)}$).
- **Chow–Künneth is known for:** varieties with a cellular decomposition (flag varieties, toric), complete intersections in projective space, uniruled threefolds (del Angel–Müller-Stach), products of the above, and — by Vial — varieties whose cohomology has small niveau (e.g. threefolds and fourfolds of low coniveau), including many rationally connected varieties.
- **Kimura-finite motives:** for $X$ dominated by products of curves, homologically trivial correspondences are nilpotent, and Kimura's theorem yields a filtration satisfying (BB1)–(BB5) *relative to* the finite-dimensionality input.
- **Function-field/arithmetic corollaries:** over $k=\overline{\mathbb F}_p$, the expected consequence $CH^j_{\hom}(X)_{\mathbb Q}=0$ is known only in isolated cases (e.g. via Kimura-finiteness for products of curves).

## 5. Principal Obstacles

- **No motivic $t$-structure.** The abelian category $\mathcal{MM}_k$ producing the Ext-spectral sequence does not exist unconditionally. Voevodsky's triangulated $DM_{\mathrm{gm}}(k)$ is available, but a $t$-structure on it is equivalent to the standard conjectures plus more; Ayoub's conservativity conjecture is the current gateway and is itself open.
- **Chow groups are not finitely generated.** By Mumford's theorem $F^2CH^2(S)_{\mathbb Q}$ is infinite-dimensional when $p_g(S)>0$, so no cohomological or Hodge-theoretic invariant of finite type can detect $F^\nu$ directly; Hodge-theoretic tools (Abel–Jacobi, normal functions, Deligne cohomology) only see $\mathrm{Gr}^0$ and $\mathrm{Gr}^1$ and are provably blind past $\nu=2$ (Green–Griffiths' higher Abel–Jacobi maps require formal-neighbourhood arguments with no proven convergence).
- **Idempotent lifting.** Producing $\pi_i\in CH^d(X\times X)_{\mathbb Q}$ lifting Künneth projectors requires (a) algebraicity of the Künneth components — the standard conjecture $C(X)$ — and (b) lifting idempotents along the kernel of $CH^d(X\times X)_{\mathbb Q}\to H^{2d}(X\times X)$, which is nil only if homologically trivial self-correspondences are nilpotent (Kimura–O'Sullivan). Both are open for a general $X$ of dimension $\ge 3$.
- **Vanishing (BB5) is equivalent to hard cycle conjectures.** For surfaces with $p_g=0$ it is Bloch's conjecture; over $\overline{\mathbb Q}$ it contains the Beilinson–Bloch injectivity of Abel–Jacobi, which implies (for instance) finiteness statements about Griffiths groups no current method reaches.

## 6. The Gap

Unconditional constructions (S. Saito 1996; Green–Griffiths; Lewis) yield filtrations satisfying (BB1)–(BB4). What is missing is exactly two implications:

1. **Separatedness/vanishing:** $\bigcap_\nu F^\nu=0$, sharpened to $F^{j+1}CH^j(X)_{\mathbb Q}=0$. In Murre's language: proving $\pi_i$ kills $CH^j$ for $i<j$, i.e. the motive $h^i(X)$ contributes nothing to codimension-$j$ cycles when $i<j$.
2. **Canonicity:** independence of the filtration from the chosen Chow–Künneth projectors — proved by Jannsen *conditionally* on the conjectures holding for all varieties simultaneously, so it cannot be extracted variety-by-variety.

Concretely: the smallest unresolved instance is a complex surface $S$ with $p_g=0$ and $\pi_1$ infinite non-trivial, where $F^2CH^2(S)_{\mathbb Q}=0$ is unknown; and the smallest arithmetic instance is $F^2CH^2(X_{\overline{\mathbb Q}})_{\mathbb Q}=0$ for a general surface over $\overline{\mathbb Q}$.

## 7. Current Research (as of June 2026)

- **Multiplicative Chow–Künneth decompositions.** Shen–Vial's Fourier decomposition for hyper-Kähler fourfolds of $K3^{[2]}$-type, extended by Fu, Laterveer, Vial and Bülles to many hyper-Kähler and Calabi–Yau families; these produce filtrations satisfying (BB1)–(BB4) that are *split* and multiplicative, refining the Beauville–Voisin conjecture on the subring generated by divisors.
- **Generalized Franchetta conjecture.** Fu–Laterveer–Vial (2019 onward) prove Franchetta-type statements for universal families over moduli of K3s and hyper-Kähler varieties; these are BB-consequences verified without the full filtration. *(frontier — verify: extensions to O'Grady-type tenfolds and to higher-degree tautological classes.)*
- **Motivic $t$-structures and conservativity.** Ayoub's programme (conservativity of Betti realization on $DM_{\mathrm{gm}}$) and Bondarko's weight structures are the principal route to Beilinson's derivation; partial conservativity results in dimension $\le 2$ and for abelian-type motives. *(frontier — verify.)*
- **Finite-dimensionality.** Ongoing work (Kimura, Vial, Laterveer) enlarging the class of Kimura-finite motives beyond varieties dominated by products of curves; each enlargement mechanically buys (BB5) for that class.
- **Groups/institutions:** Vial (Bielefeld), Laterveer (Strasbourg), Fu (Nice/IMJ), Voisin (CNRS/IMJ-PRG), Ayoub (Zürich), Murre school (Leiden), Lewis (Alberta), Bondarko (St Petersburg).

## 8. Future Work

- Prove Kimura finite-dimensionality for a single surface of general type with $p_g=0$ not dominated by a product of curves — this would break the current structural ceiling.
- Establish the standard conjecture $C(X)$ (algebraicity of Künneth projectors) for new classes; over $\overline{\mathbb F}_p$ it is implied by the Tate conjecture, making $p$-adic and crystalline methods a viable route.
- Construct the motivic $t$-structure on $DM_{\mathrm{gm}}(k)_{\mathbb Q}$ for $k$ a number field, at least on the abelian-type subcategory, and check the Ext-spectral sequence degenerates.
- Develop the Green–Griffiths higher Abel–Jacobi invariants into invariants with proven functoriality that detect $\mathrm{Gr}^2_F$, which would give the first cohomological handle beyond $\nu=1$.
- Test (BB5) numerically on explicit families (Godeaux-type, fake projective planes) via Voisin's spread/decomposition-of-the-diagonal method.

## 9. Key References

- **[Foundational]** S. Bloch. *Lectures on Algebraic Cycles.* Duke University Mathematics Series IV, 1980; 2nd ed., Cambridge University Press, 2010.
- **[Foundational]** A. Beilinson. *Height pairing between algebraic cycles.* In: K-theory, Arithmetic and Geometry, Lecture Notes in Mathematics 1289, Springer, 1987, pp. 1–26.
- **[Foundational]** D. Mumford. *Rational equivalence of $0$-cycles on surfaces.* J. Math. Kyoto Univ. 9 (1968), 195–204.
- **[Foundational]** J. P. Murre. *On a conjectural filtration on the Chow groups of an algebraic variety, I & II.* Indagationes Mathematicae 4 (1993), 177–188 and 189–201.
- **[Foundational]** U. Jannsen. *Motivic sheaves and filtrations on Chow groups.* In: Motives, Proc. Sympos. Pure Math. 55, Part 1, AMS, 1994, pp. 245–302.
- **[Foundational]** U. Jannsen. *Motives, numerical equivalence, and semi-simplicity.* Inventiones Mathematicae 107 (1992), 447–452.
- **[Foundational]** A. Beauville. *Sur l'anneau de Chow d'une variété abélienne.* Mathematische Annalen 273 (1986), 647–651.
- **[Foundational]** C. Deninger, J. Murre. *Motivic decomposition of abelian schemes and the Fourier transform.* J. reine angew. Math. 422 (1991), 201–219.
- **[SOTA / Recent]** S.-I. Kimura. *Chow groups are finite dimensional, in some sense.* Mathematische Annalen 331 (2005), 173–201.
- **[SOTA / Recent]** S. Saito. *Motives and filtrations on Chow groups.* Inventiones Mathematicae 125 (1996), 149–196.
- **[SOTA / Recent]** M. Green, P. Griffiths. *On the Tangent Space to the Space of Algebraic Cycles on a Smooth Algebraic Variety.* Annals of Mathematics Studies 157, Princeton University Press, 2005.
- **[SOTA / Recent]** M. Shen, C. Vial. *The Fourier Transform for Certain HyperKähler Fourfolds.* Memoirs of the AMS 240, no. 1139, 2016.
- **[SOTA / Recent]** L. Fu, R. Laterveer, C. Vial. *The generalized Franchetta conjecture for some hyper-Kähler varieties.* Journal de Mathématiques Pures et Appliquées 130 (2019), 1–35.
- **[SOTA / Recent]** C. Vial. *Niveau and coniveau filtrations on cohomology groups and Chow groups.* Proceedings of the London Mathematical Society 106 (2013), 410–444.
- **[Survey]** Y. André. *Une introduction aux motifs (motifs purs, motifs mixtes, périodes).* Panoramas et Synthèses 17, Société Mathématique de France, 2004.
- **[Survey]** J. Murre, J. Nagel, C. Peters. *Lectures on the Theory of Pure Motives.* University Lecture Series 61, AMS, 2013.
- **[Survey]** C. Voisin. *Chow Rings, Decomposition of the Diagonal, and the Topology of Families.* Annals of Mathematics Studies 187, Princeton University Press, 2014.

## 10. Worked Example / Concrete Special Case

**Zero-cycles on an abelian surface $A$ over $\mathbb C$ ($d=2$, $j=2$).**

For $n\in\mathbb Z$ let $[n]:A\to A$ be multiplication by $n$. Beauville's decomposition is the eigenspace decomposition of $[n]^*$:
$$CH^2(A)_{\mathbb Q}=\bigoplus_{s=0}^{2}CH^2_{(s)}(A)_{\mathbb Q},\qquad CH^2_{(s)}=\{x:\ [n]^*x=n^{4-s}x\ \ \forall n\in\mathbb Z\}.$$
Set $F^\nu CH^2:=\bigoplus_{s\ge\nu}CH^2_{(s)}$. Then:

- **$\nu=0$:** $\mathrm{Gr}^0 = CH^2_{(0)}=\mathbb Q\cdot[0_A]$. Check the eigenvalue: $[n]^{-1}(0_A)=A[n]$ has $n^4$ points, all algebraically equivalent to $0_A$, and rationally equivalent after $\otimes\mathbb Q$ by Bloch's argument, so $[n]^*[0_A]=n^{4}[0_A]$, i.e. $s=0$. This is the image of the cycle class map: $\mathrm{Gr}^0\cong \mathrm{im}(cl)=\mathbb Q$ via $\deg$. Consistent with (BB1).
- **$\nu=1$:** $\mathrm{Gr}^1 = CH^2_{(1)}$, and the Albanese map $\mathrm{alb}:CH^2_{\hom}(A)_{\mathbb Q}\to A(\mathbb C)\otimes\mathbb Q$ restricts to an isomorphism on $CH^2_{(1)}$. For $a\in A(\mathbb C)$ the cycle $z_a := [a]-[0_A]$ has $\mathrm{alb}(z_a)=a$; its $s=1$ component is the eigencomponent with $[n]^*$-eigenvalue $n^3$. This is exactly the $\mathrm{Ext}^1$-piece: $\mathrm{Ext}^1_{\mathrm{MHS}}(\mathbb Q, H^3(A,\mathbb Q)(2))\cong A(\mathbb C)\otimes\mathbb Q$ — a functor of $h^{2j-\nu}=h^{3}(A)$, as (BB4) demands.
- **$\nu=2$:** $\mathrm{Gr}^2=CH^2_{(2)}=T(A)_{\mathbb Q}$, the Albanese kernel, a functor of $h^2(A)$. Since $p_g(A)=h^{2,0}=1>0$, Mumford's theorem gives $T(A)_{\mathbb Q}$ infinite-dimensional: it is not parametrized by any algebraic variety. This is why the filtration cannot terminate at $\nu=1$.
- **$\nu=3$:** $F^3CH^2(A)_{\mathbb Q}=0$, i.e. no eigenvalue $n^{4-s}$ with $s\ge 3$ occurs. This is Beauville's theorem (1983) for $0$-cycles on abelian varieties, and it is precisely axiom (BB5) verified in this case.

**Contrast with the open case.** Replace $A$ by an Enriques surface $S$ (so $p_g=0$, $q=0$). Murre's construction still gives $F^\bullet$ with $F^3CH^2(S)_{\mathbb Q}=0$, and here $\mathrm{Gr}^2$ should be a functor of $h^2_{tr}(S)$, which has $h^{2,0}=0$; Bloch's conjecture predicts $F^2CH^2(S)_{\mathbb Q}=0$, hence $CH^2(S)_{\mathbb Q}=\mathbb Q$. For Enriques surfaces this is a theorem (Bloch–Kas–Lieberman, since $S$ is not of general type), but for a surface of general type with $p_g=0$ and no known Kimura-finiteness, the same three-line argument stops at "$\mathrm{Gr}^2$ is a functor of a motive with zero $(2,0)$-part" — and there is currently no way to conclude that this functor vanishes. That single step is the Bloch–Beilinson gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*