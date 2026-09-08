---
id: 05-analysis/kobayashi-hyperbolicity
title: "Kobayashi Hyperbolicity"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kobayashi Hyperbolicity

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kobayashi-hyperbolicity` · **Status:** open

## 1. Problem Statement / Conjecture

A complex space $X$ is **Kobayashi hyperbolic** if the Kobayashi pseudodistance $d_X$ is an actual distance ($d_X(p,q)>0$ for $p\neq q$). The central open problem is the **Kobayashi conjecture** (Kobayashi, 1970), in two parts:

**(K1) Compact case.** A generic smooth hypersurface $X \subset \mathbb{P}^n(\mathbb{C})$ of degree $d$ is Kobayashi hyperbolic once $d$ is large enough. Demailly's expected optimal threshold is $d \ge 2n-1$.

**(K2) Complement case.** For a generic smooth hypersurface $D \subset \mathbb{P}^n$ of degree $d \ge 2n+1$, the complement $\mathbb{P}^n \setminus D$ is Kobayashi hyperbolic (and Brody-hyperbolic, even hyperbolically embedded).

A complete solution of (K1) requires: (i) hyperbolicity for **every** smooth $X$ of degree $\ge 2n-1$ outside a proper algebraic subset of the parameter space $\mathbb{P}(H^0(\mathbb{P}^n,\mathcal{O}(d)))$, with explicit control of that subset; and (ii) sharpness — an example of a non-hyperbolic smooth hypersurface of degree $2n-2$ in every dimension. A disproof would exhibit a Zariski-dense family of degree-$d$ hypersurfaces, $d$ arbitrarily large, each carrying a nonconstant entire curve.

The broader open problem is the **Green–Griffiths–Lang (GGL) conjecture**: if $X$ is a projective variety of general type, there is a proper algebraic subvariety $Y \subsetneq X$ containing the image of every nonconstant holomorphic map $f:\mathbb{C}\to X$. Lang's strengthening: $X$ is hyperbolic iff every subvariety of $X$ (including $X$) is of general type.

## 2. Mathematical Foundations

Let $\Delta=\{z\in\mathbb{C}:|z|<1\}$ with Poincaré metric $\rho$ of curvature $-1$,
$$\rho_\Delta(0,r)=\tfrac12\log\frac{1+r}{1-r},\qquad ds^2 = \frac{4\,|dz|^2}{(1-|z|^2)^2}.$$

**Kobayashi pseudodistance.** For a complex space $X$ and $p,q\in X$,
$$d_X(p,q)=\inf\sum_{i=1}^{k}\rho_\Delta(a_i,b_i),$$
the infimum over all chains of holomorphic maps $f_i:\Delta\to X$ and points $a_i,b_i\in\Delta$ with $f_1(a_1)=p$, $f_i(b_i)=f_{i+1}(a_{i+1})$, $f_k(b_k)=q$. It is the largest pseudodistance for which every holomorphic $f:\Delta\to X$ is distance-decreasing; hence every holomorphic $F:X\to Y$ satisfies $d_Y(F(x),F(x'))\le d_X(x,x')$.

**Royden's infinitesimal form.** For $\xi\in T_{X,x}$,
$$k_X(x,\xi)=\inf\{\,\lambda>0 : \exists f:\Delta\to X,\ f(0)=x,\ \lambda f'(0)=\xi \,\},$$
and $d_X$ is the integrated form of $k_X$ (Royden, 1971).

**Brody's theorem** (1978). If $X$ is *compact*, then $X$ is Kobayashi hyperbolic $\iff$ every holomorphic $f:\mathbb{C}\to X$ is constant. The proof is the Brody reparametrization lemma: given $f_n:\Delta\to X$ with $\|f_n'(0)\|\to\infty$, one produces $g:\mathbb{C}\to X$ nonconstant with $\|g'\|\le\|g'(0)\|=1$.

**Jet differentials.** Let $J_kX\to X$ be the bundle of $k$-jets of germs $(\mathbb{C},0)\to X$. The **Green–Griffiths bundle** $E^{GG}_{k,m}T^*_X$ has as sections the polynomial operators
$$P(f)=\sum_{|\alpha|=m} a_\alpha(f)\,(f')^{\alpha_1}(f'')^{\alpha_2}\cdots (f^{(k)})^{\alpha_k},\qquad \textstyle\sum_j j\,\alpha_j = m,$$
weighted-homogeneous of degree $m$. Demailly's subbundle $E_{k,m}T^*_X\subset E^{GG}_{k,m}T^*_X$ consists of operators invariant under reparametrization $t\mapsto \varphi(t)$, $\varphi(0)=0$.

**Fundamental vanishing theorem** (Green–Griffiths; Siu–Yeung; Demailly). If $A\to X$ is an ample line bundle and $P\in H^0(X, E_{k,m}T^*_X\otimes A^{-1})$, then every entire curve $f:\mathbb{C}\to X$ satisfies
$$P(f',f'',\dots,f^{(k)})\equiv 0 .$$
Hence entire curves lie in the base locus of such sections; producing enough sections forces $f$ into a proper subvariety. This is the engine behind every modern advance.

**Riemann–Roch input.** For $X\subset\mathbb{P}^n$ of degree $d$ and dimension $n-1$, $K_X=\mathcal{O}_X(d-n-1)$, so $X$ is of general type iff $d\ge n+2$. Demailly's Morse-type estimate gives $h^0(X,E_{k,m}T^*_X)\gtrsim \frac{m^{(k+1)\dim X-1}}{(k!)^{\dim X}}$ under explicit positivity, which is what forces $d$ to grow with $n$ in all effective results.

## 3. History & State of the Art (SOTA)

- **1967–70.** Kobayashi introduces the pseudodistance and poses the conjectures in *Hyperbolic Manifolds and Holomorphic Mappings* (Marcel Dekker, 1970).
- **1978.** Brody's compactness criterion converts a metric problem into a value-distribution problem.
- **1980.** Green–Griffiths propose the general-type degeneracy conjecture and introduce jet differentials.
- **1996–2004.** Explicit low-degree hyperbolic surfaces in $\mathbb{P}^3$: Shiffman–Zaidenberg (degree 8, then 6 with singular corrections), Duval's smooth hyperbolic **sextic** (2004).
- **1998.** McQuillan proves GGL for surfaces of general type with $c_1^2>c_2$, using Ahlfors currents and Diophantine approximation on foliations.
- **2000–2008.** Demailly–El Goul: very general $X\subset\mathbb{P}^3$ of degree $\ge 21$ is hyperbolic; Păun improves the technique; Diverio–Trapani (2010) give degree $\ge 593$ under a cleaner argument.
- **2010.** Diverio–Merker–Rousseau prove GGL for generic hypersurfaces in $\mathbb{P}^{n+1}$ of degree $d\ge 2^{n^5}$.
- **2015.** **Siu** proves (K1) for generic hypersurfaces of sufficiently high, non-effective degree (Invent. Math. 202), using slanted vector fields on jet spaces.
- **2016–17.** **Brotbek** gives a new, conceptually simpler proof via Wronskian jet differentials on general hypersurfaces; Brotbek–Darondeau and Deng convert it into effective bounds ($d\ge (5n)^2 n^n$ order of magnitude).
- **2018–20.** Demailly's survey records the effective bound $d \ge \big\lfloor \tfrac{n^4}{3}\,(n\log(n\log(24n)))^n \big\rfloor$ for hyperbolicity of general hypersurfaces of dimension $n$. Brotbek–Deng (GAFA 2019) settle the complement case (K2) for effective high degree.

**Status:** existence of a threshold is a theorem; the conjectured *optimal* threshold $2n-1$ is wide open in every dimension $\ge 3$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| Curves ($\dim 1$) | Smooth plane curve of degree $d\ge4$ (genus $\ge2$) is hyperbolic; complete | classical uniformization |
| Surfaces in $\mathbb{P}^3$ | Very general degree $\ge 21$ hyperbolic | Demailly–El Goul 2000 |
| Surfaces in $\mathbb{P}^3$ | Explicit smooth hyperbolic sextic exists ($d=6$) | Duval 2004 |
| Surfaces of general type | GGL holds when $c_1^2>c_2$ | McQuillan 1998 |
| $\dim n$, generic | Hyperbolic for $d\gg0$ (non-effective) | Siu 2015 |
| $\dim n$, general | Hyperbolic for $d\ge (5n)^2n^n$ (effective) | Brotbek 2017; Deng 2016 |
| $\dim n$, general | $d\ge\lfloor \tfrac{n^4}{3}(n\log(n\log 24n))^n\rfloor$ | Demailly 2020 |
| Rational curves | General $X\subset\mathbb{P}^{n+1}$, $d\ge 2n+1$, contains no rational curves | Voisin 1996; Pacienza ($d\ge 2n$, $n\ge6$) |
| Algebraic hyperbolicity | General $X$, $d\ge 2n+1$: $2g(C)-2\ge \varepsilon\deg C$ for all curves $C\subset X$ | Clemens–Ein–Voisin, Demailly |
| Complements | $\mathbb{P}^n\setminus D$ hyperbolic for general $D$ of effective high degree | Brotbek–Deng 2019; Darondeau 2016 |

Note the gap in magnitude: the conjecture asserts $2n-1$ (linear); the best theorem gives roughly $n^{n}$ (super-exponential).

## 5. Principal Obstacles

- **Genericity is essential and not removable.** The Fermat hypersurface of any degree contains lines, hence is never hyperbolic. So no argument using only $d$, $n$, and positivity of $K_X$ can work; one must exploit the geometry of the *universal family* $\mathcal{X}\subset\mathbb{P}^n\times\mathbb{P}(H^0(\mathcal{O}(d)))$.
- **Slanted vector fields cost degree.** Siu's and Brotbek's proofs differentiate in the coefficient directions of the defining equation to move jets off the degeneracy locus. The vector fields have poles of order growing with the jet order $k$, and $k$ must be at least $\dim X$; twisting them away consumes $\mathcal{O}(d)$-positivity, forcing $d\gtrsim n^n$.
- **Jet differentials are scarce in low degree.** Riemann–Roch/Morse estimates only guarantee $h^0(E_{k,m}T^*_X\otimes A^{-1})>0$ when $d$ exceeds a bound that is exponential in $n$; near $d=2n-1$, $K_X=\mathcal{O}(d-n-1)$ is barely positive and the leading Euler-characteristic term is swamped by uncontrolled $h^2$ terms.
- **No control of the base locus.** Even with sections, the vanishing theorem confines entire curves to $\bigcap \mathrm{Bs}$, and proving that intersection is empty (rather than merely proper) is a separate, largely unsolved problem — this is exactly the gap between GGL and hyperbolicity.
- **Nevanlinna theory is not yet strong enough.** The second main theorem with truncated counting functions in higher dimensions (Griffiths' conjecture) is open, so classical value-distribution arguments cannot replace jet techniques.
- **McQuillan's foliation method is dimension-bound.** Ahlfors currents plus the Miyaoka–Bogomolov index inequality for foliations work for surfaces; no analogue of the index theorem is known for $\dim\ge3$ foliations with singularities.

## 6. The Gap

Proven: for each $n$ there exists $d(n)$ — roughly $n^{n}$ — such that a general degree-$d$ hypersurface of dimension $n$ is hyperbolic. Conjectured: $d(n)=2n-1$ works. The precise missing step is a **degree-efficient production of reparametrization-invariant jet differentials with empty common base locus** in the range $2n-1\le d \le n^n$. Equivalently, two sub-gaps:

1. **GGL $\Rightarrow$ Kobayashi.** Passing from "entire curves lie in a proper $Y\subsetneq X$" to "no entire curves" requires induction on $\dim Y$, but $Y$ is uncontrolled — it need not be of general type or even reduced. Riedl–Yang's Grassmannian technique closes part of this by trading dimension for degree: GGL for general hypersurfaces in dimension $\approx 2n+1$ implies the Kobayashi conjecture in dimension $n$ *(frontier — verify the exact index shift)*.
2. **Sharpness.** No smooth non-hyperbolic hypersurface of degree $2n-2$ is known in general dimension, so even the conjectured constant is unverified.

## 7. Current Research (as of June 2026)

- **Wronskian and Fermat-type constructions** (Brotbek; Brotbek–Deng; Bérczi–Kirwan via non-reductive GIT) aim to lower the effective bound from $n^n$ toward polynomial in $n$. Bérczi–Kirwan's approach applies a proportionality/localization formula on the reparametrization group quotient to prove positivity of the Demailly–Semple tower *(frontier — verify)*.
- **Deng Ya, Brotbek, Cadorel** (Strasbourg/Toulouse/CNRS) work on hyperbolicity of bases of maximally-varying families and Viehweg–Zuo sheaves, linking (K1) to moduli-theoretic positivity.
- **Riedl–Yang and the "hyperbolicity from degeneracy" school** (Notre Dame) develop Grassmannian degeneration to reduce the Kobayashi conjecture to GGL in higher dimension.
- **Demailly's Morse-theoretic program** (posthumously continued via his 2020 survey) seeks a strong Morse inequality for the Demailly–Semple tower that yields sections for $d$ linear in $n$.
- **Arithmetic side.** Lang's conjecture (hyperbolic $\Rightarrow$ finitely many $K$-rational points) is being probed by the Lawrence–Venkatesh $p$-adic method, which gives finiteness for some families where hyperbolicity is expected.

## 8. Future Work

- Prove a **Morse inequality with no $h^2$ loss** on the Demailly–Semple tower, which would drop the degree bound to polynomial in $n$.
- Establish the **Griffiths second main theorem with truncation** for $\mathbb{P}^n$; this would give hyperbolicity by pure Nevanlinna theory.
- Construct a **non-hyperbolic smooth hypersurface of degree $2n-2$** in each dimension to confirm sharpness.
- Extend McQuillan's foliation/index argument to threefolds, i.e. find a Miyaoka-type inequality for rank-1 foliations in dimension 3.
- Settle **Kobayashi's conjecture for surfaces in $\mathbb{P}^3$ at $d=5$**, the first genuinely unknown case at the conjectured optimum.

## 9. Key References

- **[Foundational]** S. Kobayashi. *Hyperbolic Manifolds and Holomorphic Mappings.* Marcel Dekker, 1970 (2nd ed., World Scientific, 2005).
- **[Foundational]** S. Kobayashi. *Hyperbolic Complex Spaces.* Grundlehren der math. Wissenschaften 318, Springer, 1998.
- **[Foundational]** R. Brody. *Compact manifolds and hyperbolicity.* Transactions of the AMS 235 (1978), 213–219. [DOI](https://doi.org/10.2307/1998216)
- **[Foundational]** M. Green, P. Griffiths. *Two applications of algebraic geometry to entire holomorphic mappings.* In: The Chern Symposium 1979, Springer, 1980, 41–74. [DOI](https://doi.org/10.1007/978-1-4613-8109-9_4)
- **[Foundational]** J.-P. Demailly. *Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials.* Proc. Sympos. Pure Math. 62, AMS, 1997, 285–360. [DOI](https://doi.org/10.1090/pspum/062.2/1492539)
- **[Key result]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS 87 (1998), 121–174. [DOI](https://doi.org/10.1007/bf02698862)
- **[Key result]** C. Voisin. *On a conjecture of Clemens on rational curves on hypersurfaces.* Journal of Differential Geometry 44 (1996), 200–213. [DOI](https://doi.org/10.4310/jdg/1214458743)
- **[Key result]** J.-P. Demailly, J. El Goul. *Hyperbolicity of generic surfaces of high degree in projective 3-space.* American Journal of Mathematics 122 (2000), 515–546. [DOI](https://doi.org/10.1353/ajm.2000.0019)
- **[Key result]** J. Duval. *Une sextique hyperbolique dans $\mathbb{P}^3(\mathbb{C})$.* Mathematische Annalen 330 (2004), 473–476.
- **[SOTA]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae 202 (2015), 1069–1166. [DOI](https://doi.org/10.1007/s00222-015-0584-x)
- **[SOTA]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS 126 (2017), 1–34. [DOI](https://doi.org/10.1007/s10240-017-0090-3)
- **[SOTA]** D. Brotbek, Y. Deng. *Hyperbolicity of the complements of general hypersurfaces of high degree.* Geometric and Functional Analysis 29 (2019), 690–750. [DOI](https://doi.org/10.1007/s00039-019-00496-2)
- **[SOTA]** E. Riedl, D. Yang. *Applications of a Grassmannian technique to hyperbolicity, Chow equivalency, and Seshadri constants.* Journal of Algebraic Geometry 31 (2022), 1–12. [DOI](https://doi.org/10.1090/jag/786)
- **[Survey]** J.-P. Demailly. *Recent results on the Kobayashi and Green–Griffiths–Lang conjectures.* Japanese Journal of Mathematics 15 (2020), 1–120. [DOI](https://doi.org/10.1007/s11537-019-1566-3)
- **[Survey]** S. Diverio, E. Rousseau. *Hyperbolicity of Projective Varieties.* IMPA Monographs / Springer, 2016.

## 10. Worked Example / Concrete Special Case

**Dimension 1: the conjecture is a theorem, and the threshold is visible.**

Let $C\subset\mathbb{P}^2$ be a smooth plane curve of degree $d$. Genus formula:
$$g=\frac{(d-1)(d-2)}{2}.$$
So $g(1)=g(2)=0$, $g(3)=1$, $g(4)=3$, $g(5)=6$.

- $d\le 2$: $C\cong\mathbb{P}^1$. The Kobayashi pseudodistance vanishes identically, since $\mathbb{P}^1$ is covered by images of $\mathbb{C}$; any two points are joined by one disc of arbitrarily large Poincaré radius. Not hyperbolic.
- $d=3$: $C$ is an elliptic curve $\mathbb{C}/\Lambda$. The universal cover is $\mathbb{C}$, and $\exp:\mathbb{C}\to C$ is a nonconstant entire curve, so by Brody $C$ is not hyperbolic. Directly: $d_C\equiv 0$ because $d_{\mathbb{C}}\equiv0$ and the covering map is distance-decreasing and surjective.
- $d\ge 4$: $g\ge3\ge2$, so the universal cover is $\Delta$ (uniformization). Then $d_C$ is the pushforward of the Poincaré distance and is positive on distinct points: for $\pi:\Delta\to C$, one has $d_C(p,q)=\min\{\rho_\Delta(\tilde p,\tilde q)\}$ over lifts, and discreteness of $\pi^{-1}(q)$ makes this minimum positive. Equivalently, any $f:\mathbb{C}\to C$ lifts to $\tilde f:\mathbb{C}\to\Delta$, which is constant by Liouville. Hyperbolic.

For $n=2$ the conjectured threshold $2n-1=3$ would give hyperbolicity for $d\ge3$; the true answer is $d\ge4=n+2$, matching "general type". In dimension 1 general type and hyperbolicity coincide — the whole difficulty in higher dimension is that they do not.

**Why genericity cannot be dropped: the Fermat quartic surface.**

Let $X=\{x_0^4+x_1^4+x_2^4+x_3^4=0\}\subset\mathbb{P}^3$, smooth of degree $4$ (a K3, not of general type, but the mechanism is generic in degree). Fix $\zeta$ with $\zeta^4=-1$, e.g. $\zeta=e^{i\pi/4}$. Consider the line
$$L=\{(s:\zeta s: t:\zeta t)\ :\ (s:t)\in\mathbb{P}^1\}.$$
Substituting: $s^4+\zeta^4 s^4+t^4+\zeta^4 t^4 = s^4-s^4+t^4-t^4=0$. So $L\subset X$. Then $f:\mathbb{C}\to X$, $f(t)=(1:\zeta:t:\zeta t)$, is a nonconstant entire curve, and by Brody's theorem $X$ is not hyperbolic — indeed $d_X$ vanishes on $L\times L$.

The same computation works for the Fermat hypersurface of *any* degree $d$ in any $\mathbb{P}^n$ with $n\ge3$: pick $\zeta^d=-1$ and pair up coordinates. Fermat hypersurfaces of arbitrarily large degree are therefore never hyperbolic. This is why (K1) must be stated for a *general* member of the linear system, and why every proof must work on the universal family rather than on a fixed $X$ — the technical source of the slanted-vector-field method and of the super-exponential degree bounds in Section 4.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*