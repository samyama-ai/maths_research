---
id: 03-geometry/kollar-local-fundamental-group-conjecture
title: "Kollar's Conjecture on Local Fundamental Groups"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kollár's Conjecture on Local Fundamental Groups

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/kollar-local-fundamental-group-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(X,x)$ be a germ of a normal complex singularity of dimension $n$. Its **link** $L(X,x) = X \cap S^{2N-1}_\epsilon(x)$ (for a local embedding $X \subset \mathbb{C}^N$ and $0 < \epsilon \ll 1$) is a compact $(2n-1)$-manifold whose homeomorphism type is independent of the choices. Kollár's programme asks: **which groups occur as $\pi_1$ of a link, once the singularity is constrained by the Minimal Model Program?**

Without constraints there is no restriction: Kollár (2013) showed every finitely presented group is $\pi_1(L(X,x))$ for some normal $3$-fold singularity. The conjecture is that log terminal and log canonical conditions collapse this to a tiny class.

**Conjecture (Kollár).** Let $(X,\Delta;x)$ be an $n$-dimensional germ.

* **(A) klt case.** If $(X,\Delta)$ is Kawamata log terminal, the local fundamental group $\pi_1^{\mathrm{loc}}(X,x) := \pi_1\big(L(X,x) \setminus \mathrm{Sing}\big) = \pi_1\big(X^{\mathrm{reg}} \cap U_x\big)$ is **finite**. *(Proved: Braun 2021.)*
* **(B) lc case, open.** If $(X,\Delta)$ is log canonical, then $\pi_1^{\mathrm{loc}}(X,x)$ is **virtually solvable**: it contains a normal solvable subgroup of index at most $c(n)$, of derived length and rank bounded by functions of $n$ alone.
* **(C) effective/Jordan refinement, open in general.** The finite groups in (A) are of bounded Jordan type *and* bounded order once the minimal log discrepancy is bounded away from $0$: there is $N(n,\varepsilon)$ with $|\pi_1^{\mathrm{loc}}(X,x)| \le N(n,\varepsilon)$ whenever $\mathrm{mld}(X,\Delta;x) \ge \varepsilon$.

A full resolution requires proving (B) with explicit bounds, or exhibiting an lc germ whose local fundamental group has no solvable subgroup of finite index; and settling (C) uniformly in dimension.

## 2. Mathematical Foundations

**Discrepancies.** For a normal pair $(X,\Delta)$ with $K_X + \Delta$ $\mathbb{Q}$-Cartier and a proper birational $f : Y \to X$,
$$K_Y = f^*(K_X+\Delta) + \sum_{E} a(E;X,\Delta)\, E .$$
$(X,\Delta)$ is **klt** if $a(E;X,\Delta) > -1$ for all exceptional $E$ and $\lfloor \Delta \rfloor = 0$; **log canonical (lc)** if $a(E;X,\Delta) \ge -1$ for all $E$. The **minimal log discrepancy** is
$$\mathrm{mld}(X,\Delta;x) = \inf_{\,\mathrm{center}_X E = \{x\}} \big(a(E;X,\Delta) + 1\big) \in [0,n].$$

**Local groups.** Set $U_x$ a contractible analytic neighbourhood. Three groups are compared:
$$\pi_1^{\mathrm{loc}}(X,x)=\pi_1\big(U_x \cap X^{\mathrm{reg}}\big), \qquad \widehat{\pi}_1^{\,\mathrm{loc}} = \pi_1^{\text{ét}}\big(U_x\cap X^{\mathrm{reg}}\big), \qquad \pi_1\big(L(X,x)\big),$$
with surjections $\pi_1^{\mathrm{loc}} \twoheadrightarrow \pi_1(L(X,x))$ (killing local monodromies along $\mathrm{Sing}$) and $\pi_1^{\mathrm{loc}} \to \widehat{\pi}_1^{\,\mathrm{loc}}$ dense. For a boundary $\Delta = \sum (1 - \tfrac{1}{m_i}) D_i$ one uses the **orbifold** version $\pi_1^{\mathrm{orb}}(X^{\mathrm{snc}},\Delta)$, quotienting by $m_i$-th powers of meridians of $D_i$.

**Cone model.** If $Y$ is Fano-type projective with $L$ ample and $K_Y \sim_{\mathbb{Q}} -r L$, the affine cone $C_a(Y,L) = \mathrm{Spec}\bigoplus_{m\ge0} H^0(Y, mL)$ has exceptional discrepancy $a(E) = r - 1$: klt iff $r>0$, lc iff $r \ge 0$. Its link is the unit circle bundle $L^{-1}|_{S^1}$ over $Y$, giving the central extension
$$1 \to \mathbb{Z}/\!\deg \to \pi_1(L) \to \pi_1^{\mathrm{orb}}(Y) \to 1 .$$

**Key input theorems.** (i) *Finiteness of $\widehat{\pi}_1^{\,\mathrm{loc}}$ for klt* (Xu 2014). (ii) *Boundedness of index-one covers and the theory of quasi-étale covers* (Greb–Kebekus–Peternell 2016). (iii) *Braun's theorem:* for klt $(X,\Delta;x)$, $\pi_1^{\mathrm{loc}}$ is finite. (iv) *Jordan property* (Braun–Filipazzi–Moraga–Svaldi 2022): there is $c(n)$ so that $\pi_1^{\mathrm{loc}}$ of an $n$-dimensional klt germ has a normal abelian subgroup of index $\le c(n)$.

## 3. History & State of the Art (SOTA)

* **1961.** Mumford: the link of a normal surface singularity is a graph manifold; $\pi_1(L)=1$ forces smoothness.
* **1968.** Brieskorn: $2$-dimensional klt = quotient singularity $\mathbb{C}^2/G$, $G \subset GL(2,\mathbb{C})$ finite — so (A) holds in dimension $2$ with $\pi_1^{\mathrm{loc}} = G$.
* **1993–2011.** Kollár's Shafarevich-map circle of ideas, and his construction (arXiv 2011; *Surveys in Differential Geometry* 18, 2013) that **every** finitely presented group is a link group of a normal $3$-fold singularity. This is the sharp contrast that makes (A),(B) meaningful, and where the conjectures were formulated.
* **2014.** Xu: $\widehat{\pi}_1^{\,\mathrm{loc}}$ of a klt germ is finite (via boundedness of complements and termination-free MMP arguments).
* **2016–2017.** Greb–Kebekus–Peternell; Tian–Xu: global and quasi-étale versions; finiteness of $\pi_1$ for klt Fano-type spaces.
* **2021.** **Braun** (*Invent. Math.* 226): $\pi_1^{\mathrm{loc}}$ of a klt singularity is finite — part (A) is a theorem, in all dimensions.
* **2022.** Braun–Filipazzi–Moraga–Svaldi (*Geom. Topol.* 26): Jordan property with dimensional constant $c(n)$; structural results toward (B) in low dimension.

The state of the art: (A) closed; (B) open in dimension $\ge 3$ in general; (C) open, tied to the ACC/boundedness conjectures for mlds.

## 4. Partial Results / Verified Cases

* **Dimension 2, klt.** $\pi_1^{\mathrm{loc}} \cong G \subset GL(2,\mathbb{C})$ finite (Brieskorn 1968); the Jordan constant is $c(2)=60$ (finite subgroups of $PGL_2(\mathbb{C})$: cyclic, dihedral, $A_4$, $S_4$, $A_5$).
* **Dimension 2, lc.** Complete classification (Kawamata; Kollár–Shepherd-Barron; see Kollár–Mori 1998, §4.1): quotient, simple elliptic, cusp, and $\mathbb{Z}/2$-quotients thereof. Links are $S^1$-bundles over elliptic curves ($\pi_1$ virtually nilpotent, integral Heisenberg type) or torus bundles over $S^1$ with hyperbolic monodromy ($\pi_1 \cong \mathbb{Z}^2 \rtimes_A \mathbb{Z}$, solvable, not virtually nilpotent). **(B) holds in dimension 2 with $c(2)$ explicit.**
* **All dimensions, klt.** Finiteness (Braun 2021) and the Jordan property (BFMS 2022).
* **Toric and $T$-varieties.** $\pi_1^{\mathrm{loc}}$ of an affine toric germ $U_\sigma$ is $N/\langle \sigma \cap N\rangle$-computable, always finite abelian; lc non-klt toric germs give explicitly abelian-by-finite groups.
* **Cones.** For $C_a(Y,L)$ klt, finiteness reduces to $\pi_1^{\mathrm{orb}}$ of a log Fano pair — known by Braun and by Tian–Xu (2017).
* **Positive characteristic.** For a strongly $F$-regular local ring $(R,\mathfrak{m})$, Carvajal-Rojas–Schwede–Tucker (2018) prove $\pi_1^{\text{ét}}(\mathrm{Spec}\,R \setminus \mathfrak{m})$ is finite with the explicit bound $|\pi_1^{\text{ét}}| \le 1/s(R)$, $s(R)$ the $F$-signature; extended by Bhatt–Carvajal-Rojas–Graf–Schwede–Tucker (2019).

## 5. Principal Obstacles

* **No local Hodge theory.** The classical route to restricting $\pi_1$ (Hodge structures, harmonic maps, Shafarevich maps) needs a compact Kähler space. Links are odd-dimensional, non-Kähler, and only have a mixed Hodge structure on cohomology with no direct control on the group.
* **Non-finitely generated $\pi_1$ in the non-lc regime.** Kollár's realization theorem shows no purely topological argument can work: the input must be the discrepancy inequality itself, so every proof has to pass through birational geometry.
* **Infinite towers of quasi-étale covers.** For klt, Braun's proof bounds the tower using boundedness of complements plus a "Galois-invariant" MMP; in the lc case the index-one cover need not be klt, complements may fail to be bounded, and the tower has genuinely infinite groups ($\mathbb{Z}^{2k}$-type), so no finiteness statement survives to be bootstrapped.
* **Solvability is not birationally local.** The expected solvable quotient of an lc link group comes from the dual complex $\mathcal{DR}(X,x)$ (a $\le (n-1)$-dimensional CW complex, a quotient of a sphere by Kollár–Xu). Controlling $\pi_1(\mathcal{DR})$ requires knowing the homeomorphism type of dual complexes of lc pairs, itself open above dimension $3$.
* **mld pathologies.** Part (C) needs ACC for mlds and boundedness of $\varepsilon$-lc germs; both are open in dimension $\ge 4$.

## 6. The Gap

Proven: the klt case in all dimensions, and the full lc case only in dimension $2$ (plus toric/cone families in all dimensions). Missing: for an $n \ge 3$ lc germ, a mechanism producing a finite-index solvable subgroup of $\pi_1^{\mathrm{loc}}$. Concretely, the single step to be crossed is:

> Given an lc germ $(X,\Delta;x)$ with a dlt modification $f : Y \to X$ and reduced exceptional divisor $E = \lfloor \Delta_Y \rfloor$, show that $\pi_1(L(X,x))$ is an extension of $\pi_1$ of the dual complex $\mathcal{DR}(E)$ — known to be a quotient of $S^{k}$, hence with controlled (crystallographic) $\pi_1$ — by a group governed by the klt strata, to which Braun's finiteness applies.

The obstruction is that the extension is not known to split, and the strata monodromy acting on $H_1$ of the $\mathbb{Z}^{2k}$-parts is only known to be quasi-unipotent up to finite index in dimension $\le 3$.

## 7. Current Research (as of June 2026)

* **Braun, Filipazzi, Moraga, Svaldi** and collaborators (Freiburg, EPFL, UCLA/Utah, Milano) continue the boundedness-of-complements approach; the effective Jordan constant $c(n)$ and the lc case are their stated targets. *(frontier — verify)* Recent work of Braun–Greb–Langlois–Moraga on reductive quotients of klt singularities gives structure theorems for klt germs with large automorphism groups.
* **K-stability school** (Li, Liu, Xu, Zhuang): local volumes $\widehat{\mathrm{vol}}(x,X)$ satisfy $|\pi_1^{\mathrm{loc}}| \le n^n/\widehat{\mathrm{vol}}(x,X)$ for klt germs — a quantitative form of (C) whenever local volume is bounded below. Effective lower bounds on $\widehat{\mathrm{vol}}$ in terms of mld are the current bottleneck.
* **Mixed and positive characteristic**: $F$-signature and perfectoid methods extending CST-type bounds to lc/log terminal singularities in char $p>0$ and to arithmetic families.
* **Topology of links**: computation of dual complexes of lc degenerations, connecting to non-archimedean/Berkovich skeleta.

## 8. Future Work

1. Prove (B) in dimension $3$ using the classification of dlt $3$-fold singularities and Kollár–Xu's result that $\mathcal{DR}$ of an lc $3$-fold is $S^1$, $S^2$, or a quotient of $S^2$.
2. Make Braun's proof effective: extract $N(n,\varepsilon)$ from boundedness of $\varepsilon$-lc complements.
3. Determine the sharp Jordan constant $c(3)$ for klt $3$-folds; $c(2)=60$ is the only known sharp value.
4. Prove a local Bieberbach theorem: an lc link group has a finite-index subgroup that is the fundamental group of an infra-solvmanifold.
5. Transfer to char $p$: is $\pi_1^{\text{ét},\mathrm{tame}}$ of a klt (not necessarily $F$-regular) germ finite?

## 9. Key References

- **[Foundational]** D. Mumford. *The topology of normal singularities of an algebraic surface and a criterion for simplicity.* Publ. Math. IHÉS 9 (1961), 5–22. [DOI](https://doi.org/10.1007/bf02698717)
- **[Foundational]** E. Brieskorn. *Rationale Singularitäten komplexer Flächen.* Inventiones Mathematicae 4 (1968), 336–358.
- **[Foundational]** J. Kollár. *Shafarevich maps and plurigenera of algebraic varieties.* Inventiones Mathematicae 113 (1993), 177–215. [DOI](https://doi.org/10.1007/bf01244307)
- **[Foundational]** J. Kollár, S. Mori. *Birational Geometry of Algebraic Varieties.* Cambridge Tracts in Mathematics 134, Cambridge University Press, 1998.
- **[Survey]** J. Kollár. *Links of complex analytic singularities.* Surveys in Differential Geometry 18 (2013), 157–193. [DOI](https://doi.org/10.4310/sdg.2013.v18.n1.a4)
- **[Survey]** J. Kollár. *Singularities of the Minimal Model Program.* Cambridge Tracts in Mathematics 200, Cambridge University Press, 2013.
- **[SOTA]** C. Xu. *Finiteness of algebraic fundamental groups.* Compositio Mathematica 150 (2014), 409–414. [DOI](https://doi.org/10.1112/s0010437x13007562)
- **[SOTA]** D. Greb, S. Kebekus, T. Peternell. *Étale fundamental groups of Kawamata log terminal spaces, flat sheaves, and quotients of abelian varieties.* Duke Mathematical Journal 165 (2016), 1965–2004. [DOI](https://doi.org/10.1215/00127094-3450859)
- **[SOTA]** G. Tian, C. Xu. *Finiteness of fundamental groups.* Compositio Mathematica 153 (2017), 257–273. [DOI](https://doi.org/10.1112/s0010437x16007867)
- **[SOTA]** J. Carvajal-Rojas, K. Schwede, K. Tucker. *Fundamental groups of $F$-regular singularities via $F$-signature.* Annales Scientifiques de l'ENS 51 (2018), 993–1016. [DOI](https://doi.org/10.24033/asens.2370)
- **[SOTA / Recent]** L. Braun. *The local fundamental group of a Kawamata log terminal singularity is finite.* Inventiones Mathematicae 226 (2021), 845–896. [DOI](https://doi.org/10.1007/s00222-021-01062-0)
- **[SOTA / Recent]** L. Braun, S. Filipazzi, J. Moraga, R. Svaldi. *The Jordan property for local fundamental groups.* Geometry & Topology 26 (2022), 3819–3872. [DOI](https://doi.org/10.2140/gt.2022.26.283)

## 10. Worked Example / Concrete Special Case

**The klt/lc boundary for cones over curves.** Take $Y$ a smooth projective curve, $L$ ample of degree $d$, $X = C_a(Y,L)$ with vertex $x$. Write $K_Y \sim_{\mathbb{Q}} -rL$, so $r = -\deg K_Y/d = (2-2g)/d$. Blowing up the vertex gives $f: Y_{\mathrm{tot}} \to X$ with exceptional divisor $E \cong Y$ and
$$a(E;X) = r-1 = \frac{2-2g}{d} - 1 .$$

* **$g=0$, $L=\mathcal{O}(d)$:** $r = 2/d > 0$, $a(E) = 2/d - 1 > -1$, so $X$ is klt. Indeed $X = \mathbb{C}^2/\mu_d$ with $\mu_d$ acting by $\tfrac{1}{d}(1,1)$; the link is the lens space $L(d,1)$ and
$$\pi_1^{\mathrm{loc}}(X,x) \cong \mathbb{Z}/d,$$
finite — as (A) predicts. Its Jordan index is $1$; the full Jordan bound $60$ in dimension $2$ is attained by the binary icosahedral group $2I$ of order $120$ acting on $\mathbb{C}^2$ (the $E_8$ singularity), where the maximal normal abelian subgroup is the centre $\mathbb{Z}/2$, index $60$.
* **$g=1$ (elliptic $E$), $\deg L = d$:** $r = 0$, $a(E)=-1$, so $X$ is lc but **not** klt — a simple elliptic singularity. The link is the circle bundle of Euler number $-d$ over the torus, with
$$\pi_1(L) = \langle a,b,c \mid [a,c]=[b,c]=1,\ [a,b]=c^{d}\rangle,$$
a discrete Heisenberg-type group: infinite, torsion-free, nilpotent of class $2$. Finiteness fails exactly at $a(E) = -1$, and the group is (virtually) solvable — the content of (B).
* **Cusp singularity (still lc, dimension 2):** the link is a torus bundle $T^2 \to M \to S^1$ with monodromy $A \in SL_2(\mathbb{Z})$, $|\mathrm{tr}\,A| > 2$, so
$$\pi_1(L) \cong \mathbb{Z}^2 \rtimes_A \mathbb{Z},$$
solvable of derived length $2$ but **not** virtually nilpotent. This is why (B) must be stated with "solvable" and not "nilpotent", and it pins the expected shape of the answer: lc link groups should be fundamental groups of infra-solvmanifolds, up to the finite klt part supplied by Braun's theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*