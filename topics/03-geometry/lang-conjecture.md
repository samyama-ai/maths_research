---
id: 03-geometry/lang-conjecture
title: "Lang Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lang Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/lang-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Serge Lang proposed a family of linked conjectures asserting that **negative curvature governs the scarcity of both entire holomorphic curves and rational points**. The catalog entry tracks the three coupled statements.

**(L1) Bombieri–Lang (arithmetic).** Let $X$ be a smooth projective variety of general type over a number field $K$. Then $X(K)$ is not Zariski dense in $X$.

**(L2) Green–Griffiths–Lang (analytic).** Let $X$ be a smooth complex projective variety of general type. There exists a proper closed algebraic subset $\mathrm{Exc}(X) \subsetneq X$ containing the image of *every* nonconstant holomorphic map $f:\mathbb{C}\to X$.

**(L3) Lang's hyperbolicity dictionary.** For a smooth projective $X$ over a number field $K$ with a fixed embedding $K\hookrightarrow\mathbb{C}$, the following are equivalent:
1. $X_{\mathbb{C}}$ is Kobayashi hyperbolic;
2. every irreducible subvariety of $X_{\mathbb{C}}$ (including $X$) is of general type — "$X$ is algebraically hyperbolic" in Lang's sense;
3. $X(L)$ is finite for every finite extension $L/K$.

A complete proof must establish these for *all* varieties of general type in all dimensions $n \ge 2$; a disproof requires one general-type $X/K$ with $X(K)$ Zariski dense (for L1), or one general-type $X$ admitting a Zariski-dense entire curve (for L2). The dimension-1 case of (L1) and (L3) is Faltings' theorem (Mordell's conjecture) and is fully proved.

## 2. Mathematical Foundations

**General type.** For $X$ smooth projective of dimension $n$ with canonical bundle $K_X = \det \Omega^1_X$, the Kodaira dimension is
$$\kappa(X)=\limsup_{m\to\infty}\frac{\log \dim H^0(X, mK_X)}{\log m}\in\{-\infty,0,1,\dots,n\}.$$
$X$ is of **general type** iff $\kappa(X)=n$, equivalently $h^0(X,mK_X)\sim c\,m^n$ with $c>0$, equivalently $K_X$ is big.

**Kobayashi pseudo-distance.** For $p,q\in X$, $d_X(p,q)$ is the infimum of $\sum_i \rho_{\mathbb{D}}(a_i,b_i)$ over chains of holomorphic discs $f_i:\mathbb{D}\to X$ with $f_i(a_i),f_i(b_i)$ linking $p$ to $q$; $\rho_{\mathbb{D}}$ is the Poincaré distance. $X$ is **Kobayashi hyperbolic** if $d_X$ is a genuine distance. By **Brody's theorem**, for $X$ compact this is equivalent to the nonexistence of a nonconstant holomorphic $f:\mathbb{C}\to X$.

**Jets and the Green–Griffiths bundle.** Let $J_kX\to X$ be the bundle of $k$-jets of germs $(\mathbb{C},0)\to X$ and $E_{k,m}\Omega^1_X$ the sheaf of jet differentials of order $k$ and weight $m$: locally, polynomials $P(f',f'',\dots,f^{(k)})$ that are homogeneous of weight $m$ under $f(t)\mapsto f(\lambda t)$. The **fundamental vanishing theorem** (Green–Griffiths, Demailly, Siu–Yeung) states: if $P\in H^0\big(X, E_{k,m}\Omega^1_X\otimes A^{-1}\big)$ with $A$ ample, then every entire curve $f:\mathbb{C}\to X$ satisfies
$$P\big(f',f'',\dots,f^{(k)}\big)\equiv 0 .$$
Entire curves are therefore confined to the base locus of such sections. Demailly's strategy is to prove that this space of sections is nonzero for $k\gg 0$ by holomorphic Morse inequalities, then to intersect base loci.

**Algebraic hyperbolicity (Demailly).** $X$ with ample $\mathcal{O}(1)$ is *algebraically hyperbolic* if there is $\varepsilon>0$ with
$$2g(\tilde{C})-2 \ \ge\ \varepsilon\,\deg C$$
for every irreducible curve $C\subset X$ with normalization $\tilde C$. Kobayashi hyperbolic $\Rightarrow$ algebraically hyperbolic.

**Vojta's dictionary.** Nevanlinna's second main theorem, $m_f(D,r)+N^{(1)}_f(D,r)\le_{\mathrm{exc}} T_{f,K_X^{-1}}(r)+\epsilon T_f(r)$, is the analytic mirror of the conjectural height inequality
$$h_{K_X}(P)+h_D(P)\ \le\ d(P)+\epsilon\, h_A(P)+O(1)$$
for $P\in X(\overline{\mathbb{Q}})$ outside a proper subvariety, where $d$ is the logarithmic discriminant. (L1) is the special case $D=0$, $[K(P):K]$ bounded.

## 3. History & State of the Art (SOTA)

- **1922:** Mordell conjectures finiteness of rational points on curves of genus $\ge 2$.
- **1970–74:** Lang, "Integral points on curves" and *Higher dimensional Diophantine problems* (Bull. AMS 80, 1974), formulates the higher-dimensional analogue and the link to hyperbolicity; Bombieri independently proposes the surface case in a 1980 lecture — hence "Bombieri–Lang".
- **1977:** Bogomolov proves that a surface with $c_1^2>c_2$ has finitely many rational and elliptic curves; the first structural evidence for (L2).
- **1979–80:** Green–Griffiths introduce jet differentials and state the degeneracy conjecture.
- **1986:** Lang's survey *Hyperbolic and Diophantine analysis* (Bull. AMS 14) fixes the modern statement of the dictionary (L3).
- **1983:** Faltings proves Mordell — case $n=1$ of (L1)/(L3).
- **1991–94:** Faltings proves the Mordell–Lang conjecture for subvarieties of abelian varieties; Vojta (1996) extends to semiabelian varieties.
- **1998:** McQuillan proves the Green–Griffiths conjecture for surfaces with $c_1^2>c_2$ using Ahlfors currents and Riccati foliations.
- **2010–2019:** Effective algebraic degeneracy for generic hypersurfaces (Diverio–Merker–Rousseau), Siu's proof of the Kobayashi conjecture for generic high-degree hypersurfaces, Brotbek's Wronskian construction, and Brotbek–Deng for complements.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Curves, $g\ge 2$ | $X(K)$ finite — full (L1),(L3) | Faltings 1983 |
| $X\subset A$, $A$ abelian, $X$ not containing a translated abelian subvariety | $X(K)$ finite | Faltings 1991, 1994 |
| $X\subset G$ semiabelian, integral points | Degeneracy proved | Vojta 1996 |
| $\Omega^1_X$ ample and globally generated | $X(K)$ finite | Moriwaki 1995 |
| Surfaces with $c_1^2>c_2$ | Green–Griffiths holds | McQuillan 1998 |
| Very general surface $S_d\subset\mathbb{P}^3$, $d\ge 21$ | Kobayashi hyperbolic | Demailly–El Goul 2000 |
| Generic hypersurface $X_d\subset\mathbb{P}^{n+1}$, $d\ge 2^{n^5}$ | Entire curves algebraically degenerate | Diverio–Merker–Rousseau 2010 |
| General $X_d\subset\mathbb{P}^{n+1}$, $d\ge (n+1)^{n+2}$ (Brotbek), $d\ge \tfrac{n^4}{3}(n\log(n\log 24n))^n$ (Demailly) | Kobayashi hyperbolic | Brotbek 2017; Demailly 2020 |
| Complements $\mathbb{P}^n\setminus X_d$, $d\gg n$ | Hyperbolic, hyperbolically embedded | Brotbek–Deng 2019 |
| Varieties with maximal-variation families / large fundamental group, $\Omega^1$ big | Pseudo-hyperbolicity | Brunebarbe, Cadorel–Deng–Yamanoi |
| Hypersurfaces in abelian varieties over $\mathbb{Q}$ | Finiteness of integral points | Lawrence–Sawin 2020 |

Conditional results are equally load-bearing: Caporaso–Harris–Mazur (1997) show Bombieri–Lang implies a **uniform** bound $N(g,K)$ on $\\#X(K)$ for all curves of genus $g$ over $K$ — widely viewed as a stress test of (L1).

## 5. Principal Obstacles

- **Jet differentials exist but their base loci are opaque.** Demailly's Morse-inequality method produces sections of $E_{k,m}\Omega^1_X\otimes A^{-1}$ only for $d$ or $k$ enormous, and gives no control on where they vanish. Proving *algebraic degeneracy* requires intersecting base loci of many sections; nothing forces that intersection to be a proper subvariety.
- **Positivity is only generic.** For a *general* hypersurface one can degenerate to a special member (Siu's slanted vector fields, Brotbek's Wronskians) and use genericity. For a *specific* variety over $\mathbb{Q}$ the deformation argument is unavailable.
- **Bogomolov's inequality $c_1^2>c_2$ fails for the natural test cases** (see §10), so McQuillan's surface theorem covers none of the hypersurfaces in $\mathbb{P}^3$.
- **No arithmetic analogue of the Ahlfors current.** McQuillan's proof converts an entire curve into a closed positive current and then to a foliation; there is no known object playing this role for an infinite set of rational points, so (L2) does not transfer to (L1).
- **Vojta's height inequality is not accessible by descent.** Faltings' method (Vojta's proof of Mordell via Arakelov geometry / product embeddings) exploits the group law of $A$; general-type varieties have no group structure and no analogue of the Mordell–Weil finite-generation input.
- **The exceptional locus is not functorially defined.** $\mathrm{Exc}(X)$ is conjecturally the same for the analytic and arithmetic problems, but no construction of it exists, so the statement has no inductive handle on dimension.

## 6. The Gap

Proven: (i) $n=1$; (ii) subvarieties of (semi)abelian varieties, where a group law supplies the geometry of numbers; (iii) *generic* members of families with $d$ exponentially large in $n$; (iv) surfaces satisfying a Chern-number inequality that no complete intersection in $\mathbb{P}^3$ satisfies.

Missing: any statement about a **single explicitly given** variety of general type of dimension $\ge 2$ that is not embedded in an abelian variety. Concretely, it is unknown whether the Fermat quintic surface $x^5+y^5+z^5+w^5=0$ has Zariski-dense rational points over some number field, and unknown whether some general-type surface in $\mathbb{P}^3$ carries a Zariski-dense entire curve. The step to be crossed is the passage from *existence* of a nonzero jet differential to *effective control of its base locus* for arbitrary (non-generic) $X$, together with a mechanism converting analytic degeneracy into arithmetic degeneracy.

## 7. Current Research (as of June 2026)

- **Hodge-theoretic Diophantine geometry.** The Lawrence–Venkatesh $p$-adic period-map method proves non-density of rational points for families with large monodromy; extensions to hypersurfaces of large degree and to Shimura-type settings are the most active arithmetic route to (L1). *(frontier — verify)* claims of Lang-type degeneracy for new classes of complete intersections via variational Hodge theory appear in 2025–26 preprints.
- **Effective hyperbolicity.** Groups around Demailly's school (Grenoble), Brotbek (Strasbourg), Deng (Chinese Academy of Sciences), Cadorel, Rousseau (Brest/IRL) push degree bounds toward the conjecturally optimal $d\ge 2n+1$ for hypersurfaces in $\mathbb{P}^{n+1}$; Riedl–Yang's Grassmannian technique reduces the Kobayashi conjecture in dimension $n$ to a statement in dimension $2n$-ish, giving polynomial rather than exponential targets.
- **Nonabelian Hodge / representation-theoretic hyperbolicity.** Brunebarbe, Cadorel–Deng–Yamanoi prove pseudo-Kobayashi hyperbolicity for varieties admitting big representations of $\pi_1$ — the largest non-generic class currently reachable.
- **Uniformity and counting.** Explicit verification programs (Mordell–Weil sieve, quadratic Chabauty, Balakrishnan–Dogra–Müller–Tuitman–Vonk) test the Caporaso–Harris–Mazur uniformity predictions on curves and surfaces.
- **Model theory.** Function-field analogues (Hrushovski's proof of Mordell–Lang in positive characteristic) remain a source of structural analogies.

## 8. Future Work

1. Prove Green–Griffiths–Lang for **all** surfaces of general type, dropping $c_1^2>c_2$ — the consensus next milestone; requires handling the foliation case when $c_1^2\le c_2$.
2. Establish an arithmetic analogue of the fundamental vanishing theorem: a height inequality forced by a global jet differential (Vojta's program).
3. Construct $\mathrm{Exc}(X)$ intrinsically, e.g. as the non-ample locus of some positivity invariant of $\Omega^1_X$, and prove its expected functoriality under dominant maps.
4. Extend Lawrence–Venkatesh beyond families with big monodromy — in particular to varieties with no natural period map.
5. Settle the **Lang exceptional set conjecture** for a single explicit surface, e.g. a smooth quintic in $\mathbb{P}^3$ over $\mathbb{Q}$.

## 9. Key References

- **[Foundational]** S. Lang. *Higher dimensional Diophantine problems.* Bulletin of the AMS 80 (1974), 779–787. [DOI](https://doi.org/10.1090/s0002-9904-1974-13516-0)
- **[Foundational]** S. Lang. *Hyperbolic and Diophantine analysis.* Bulletin of the AMS (N.S.) 14 (1986), 159–205. [DOI](https://doi.org/10.1007/978-1-4612-2116-6_15)
- **[Foundational]** M. Green, P. Griffiths. *Two applications of algebraic geometry to entire holomorphic mappings.* In: The Chern Symposium 1979, Springer, 1980, 41–74. [DOI](https://doi.org/10.1007/978-1-4613-8109-9_4)
- **[Foundational]** G. Faltings. *Diophantine approximation on abelian varieties.* Annals of Mathematics 133 (1991), 549–576.
- **[Foundational]** G. Faltings. *The general case of S. Lang's conjecture.* In: Barsotti Symposium in Algebraic Geometry, Academic Press, 1994, 175–182.
- **[SOTA]** P. Vojta. *Integral points on subvarieties of semiabelian varieties, I.* Inventiones Mathematicae 126 (1996), 133–181. [DOI](https://doi.org/10.1007/s002220050092)
- **[SOTA]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS 87 (1998), 121–174. [DOI](https://doi.org/10.1007/bf02698862)
- **[SOTA]** J.-P. Demailly, J. El Goul. *Hyperbolicity of generic surfaces of high degree in projective 3-space.* American Journal of Mathematics 122 (2000), 515–546. [DOI](https://doi.org/10.1353/ajm.2000.0019)
- **[SOTA]** S. Diverio, J. Merker, E. Rousseau. *Effective algebraic degeneracy.* Inventiones Mathematicae 180 (2010), 161–223. [DOI](https://doi.org/10.1007/s00222-010-0232-4)
- **[SOTA]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae 202 (2015), 1069–1166. [DOI](https://doi.org/10.1007/s00222-015-0584-x)
- **[SOTA]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS 126 (2017), 1–34. [DOI](https://doi.org/10.1007/s10240-017-0090-3)
- **[SOTA]** D. Brotbek, Y. Deng. *Hyperbolicity of the complements of general hypersurfaces of high degree.* Geometric and Functional Analysis 29 (2019), 690–750. [DOI](https://doi.org/10.1007/s00039-019-00496-2)
- **[SOTA]** B. Lawrence, A. Venkatesh. *Diophantine problems and $p$-adic period mappings.* Inventiones Mathematicae 221 (2020), 893–999. [DOI](https://doi.org/10.1007/s00222-020-00966-7)
- **[SOTA]** E. Riedl, D. Yang. *Applications of a Grassmannian technique to hyperbolicity, Chow equivalency, and Seshadri constants.* Journal of Algebraic Geometry 31 (2022), 1–12. [DOI](https://doi.org/10.1090/jag/786)
- **[Related]** L. Caporaso, J. Harris, B. Mazur. *Uniformity of rational points.* Journal of the AMS 10 (1997), 1–35. [DOI](https://doi.org/10.1090/s0894-0347-97-00195-1)
- **[Related]** A. Moriwaki. *Remarks on rational points of varieties whose cotangent bundles are generated by global sections.* Mathematical Research Letters 2 (1995), 113–118. [DOI](https://doi.org/10.4310/mrl.1995.v2.n1.a10)
- **[Survey]** S. Lang. *Number Theory III: Diophantine Geometry.* Encyclopaedia of Mathematical Sciences 60, Springer, 1991.
- **[Survey]** J.-P. Demailly. *Recent results on the Kobayashi and Green–Griffiths–Lang conjectures.* Japanese Journal of Mathematics 15 (2020), 1–120. [DOI](https://doi.org/10.1007/s11537-019-1566-3)
- **[Survey]** A. Javanpeykar. *The Lang–Vojta conjectures on projective pseudo-hyperbolic varieties.* In: Arithmetic Geometry of Logarithmic Pairs and Hyperbolicity of Moduli Spaces, CRM Short Courses, Springer, 2020. [DOI](https://doi.org/10.1007/978-3-030-49864-1_3)

## 10. Worked Example / Concrete Special Case

**Setting.** Let $S_d\subset\mathbb{P}^3$ be a smooth surface of degree $d$. Adjunction gives $K_{S_d}=\mathcal{O}_{S_d}(d-4)$, so
- $d\le 3$: $\kappa=-\infty$ (del Pezzo);
- $d=4$: $K$ trivial, K3 surface, $\kappa=0$;
- $d\ge 5$: $K_{S_d}$ ample, $S_d$ **of general type** — Lang predicts non-density of rational points and degenerate entire curves.

**Step 1: the exceptional set is genuinely nonempty.** The Fermat quintic $F_5:\;x^5+y^5+z^5+w^5=0$ contains lines. Fix $\zeta,\eta$ with $\zeta^5=\eta^5=-1$; the line
$$L_{\zeta,\eta}=\{x+\zeta y=0,\ z+\eta w=0\}$$
lies in $F_5$, since $x^5+y^5=(-\zeta y)^5+y^5=(-\zeta^5+1)y^5=0$ and likewise for $(z,w)$. Grouping the four coordinates into pairs in $3$ ways and choosing $(\zeta,\eta)$ in $5\times 5$ ways gives $3d^2=75$ lines. For $\zeta=\eta=-1$ the line is defined over $\mathbb{Q}$: $\{x=y,\ z=w\}\cong\mathbb{P}^1$, which has **infinitely many rational points**. So $F_5(\mathbb{Q})$ is infinite, and Lang's conjecture asserts only that
$$\overline{F_5(\mathbb{Q})\setminus \textstyle\bigcup_i L_i}^{\,\mathrm{Zar}}\neq F_5 ,$$
i.e. all but finitely many rational points lie on the $75$ lines (plus possibly finitely many other rational/elliptic curves). This is **open**.

**Step 2: why McQuillan's theorem does not apply.** For $S_d\subset\mathbb{P}^3$, with $H=\mathcal{O}(1)|_{S_d}$ and $H^2=d$:
$$c_1^2 = K_{S_d}^2=(d-4)^2H^2=d(d-4)^2,\qquad c_2=e(S_d)=d\big(d^2-4d+6\big).$$
Then
$$c_1^2-c_2 = d\big[(d-4)^2-(d^2-4d+6)\big]=d\big[d^2-8d+16-d^2+4d-6\big]=d\,(10-4d).$$
This is positive only for $d<2.5$, i.e. never for a general-type surface. For $d=5$: $c_1^2=5$, $c_2=55$, $c_1^2-c_2=-50$. Bogomolov's and McQuillan's hypothesis fails for **every** smooth surface in $\mathbb{P}^3$ — a one-line computation that explains why the most successful surface theorem is silent on the most classical examples.

**Step 3: what is known for $F_5$.** Nothing unconditional. The degree bounds of §4 apply to *very general* surfaces with $d\ge 21$ (Demailly–El Goul); $F_5$ is neither general nor of degree $\ge 21$. Algebraic hyperbolicity also fails outright, since the $75$ lines have $2g-2=-2<0$. Hence $F_5$ is not Kobayashi hyperbolic, and only the *pseudo*-hyperbolic statement (L2) is in play. Contrast $d=4$: a K3 surface has $\kappa=0$ and can have dense rational points (e.g. $x^4+y^4=z^4+w^4$, dense over $\mathbb{Q}$), confirming that the general-type hypothesis in §1 is not removable.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*