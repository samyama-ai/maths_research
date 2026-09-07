---
id: 03-geometry/kobayashi-conjecture
title: "Kobayashi Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kobayashi Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/kobayashi-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Kobayashi, 1970).** Let $n \geq 3$. A *generic* smooth hypersurface $X \subset \mathbb{P}^n(\mathbb{C})$ of degree $d \geq 2n-1$ is Kobayashi hyperbolic.

**Complement version.** For a generic smooth hypersurface $X \subset \mathbb{P}^n$ of degree $d \geq 2n+1$, the complement $\mathbb{P}^n \setminus X$ is Kobayashi hyperbolic (and hyperbolically embedded).

Here "generic" means: outside a proper Zariski-closed subset of the parameter space $\mathbb{P}(H^0(\mathbb{P}^n, \mathcal{O}(d))) = \mathbb{P}^{N_d}$, $N_d = \binom{n+d}{d} - 1$. Genericity is essential — the Fermat hypersurface of every degree contains lines (Section 10).

A complete proof must produce, for each $n$, the sharp threshold $d_n = 2n-1$ together with a Zariski-open dense locus of hyperbolic members. A disproof would exhibit a degree $d \geq 2n-1$ and a Zariski-dense family of degree-$d$ hypersurfaces each carrying a nonconstant entire curve.

## 2. Mathematical Foundations

**Kobayashi pseudodistance.** For a complex manifold $X$, let $\mathbb{D}$ be the unit disc with Poincaré distance $\rho$. Define $d_X(p,q)$ as the infimum of $\sum_{i=1}^k \rho(a_i,b_i)$ over all chains of holomorphic maps $f_i : \mathbb{D} \to X$ with $f_1(a_1)=p$, $f_i(b_i)=f_{i+1}(a_{i+1})$, $f_k(b_k)=q$. The infinitesimal form is the Royden–Kobayashi pseudometric
$$k_X(x;\xi) = \inf\{\, \lambda > 0 : \exists f:\mathbb{D}\to X,\ f(0)=x,\ \lambda f'(0)=\xi \,\}.$$
$X$ is **Kobayashi hyperbolic** if $d_X$ is a genuine distance, equivalently (for $X$ compact) if $k_X > 0$ on $T_X \setminus \{0\}$.

**Brody's theorem (1978).** A compact complex manifold $X$ is hyperbolic if and only if every holomorphic map $f : \mathbb{C} \to X$ is constant. This converts an analytic-metric statement into a statement about entire curves, and is the form used in all modern work.

**Jet differentials (Green–Griffiths, Demailly).** Let $J_k X \to X$ be the bundle of $k$-jets of germs $f:(\mathbb{C},0)\to X$. A *jet differential of order $k$ and weight $m$* is a section of $E_{k,m}^{GG} T_X^*$, locally a polynomial
$$P\big(f', f'', \dots, f^{(k)}\big) = \sum_{|\alpha_1| + 2|\alpha_2| + \dots + k|\alpha_k| = m} a_{\alpha}(f)\, (f')^{\alpha_1}(f'')^{\alpha_2}\cdots (f^{(k)})^{\alpha_k}.$$
Demailly's subbundle $E_{k,m}T_X^* \subset E_{k,m}^{GG}T_X^*$ of *invariant* jet differentials is invariant under reparametrization of the source.

**Fundamental vanishing theorem (Green–Griffiths; Demailly; Siu–Yeung).** If $P \in H^0\big(X, E_{k,m}T_X^* \otimes A^{-1}\big)$ with $A$ ample, then every entire curve $f:\mathbb{C}\to X$ satisfies $P(j_k f) \equiv 0$. Hence enough independent such $P$ force $f$ into the base locus of the sections, giving *algebraic degeneracy*.

**Adjunction data.** For $X_d \subset \mathbb{P}^n$ smooth of degree $d$: $K_X = \mathcal{O}_X(d-n-1)$, so $X$ is of general type iff $d \geq n+2$. Hyperbolicity requires general type on every subvariety, but general type is far from sufficient.

**Lines and the sharp bound.** The Fano scheme of lines $F(X_d)$ has expected dimension $2(n-1) - (d+1) = 2n - 3 - d$; a generic $X_d$ contains lines exactly when $d \leq 2n-3$. Voisin's theorem below removes all rational curves at $d \geq 2n-1$, which is why $2n-1$ is the conjectured threshold. For $n=3$: quartics are K3 surfaces, swept by elliptic curves, so nonhyperbolic; the generic quintic is the first candidate.

## 3. History & State of the Art (SOTA)

- **1970** — Kobayashi poses the problem in *Hyperbolic Manifolds and Holomorphic Mappings*; restated with the explicit degree bounds in his 1998 Grundlehren volume and in the 1970s–80s literature.
- **1978** — Brody's reparametrization lemma makes the compact case purely a question about entire curves.
- **1980** — Green–Griffiths introduce jet differentials and the algebraic-degeneracy strategy.
- **1996** — Voisin: a generic $X_d \subset \mathbb{P}^n$ with $d \geq 2n-1$ contains no rational curves (Clemens' conjecture range), confirming the *algebraic* shadow of the conjecture at the conjectured threshold.
- **1996** — Siu–Yeung: $\mathbb{P}^2 \setminus C$ is hyperbolic for generic $C$ of degree $d \geq d_0$ with $d_0$ astronomically large (order $10^{13}$); first complement result.
- **1997–2000** — Demailly's jet-differential machinery; Demailly–El Goul prove hyperbolicity of generic surfaces in $\mathbb{P}^3$ of degree $d \geq 21$.
- **2008** — Păun improves the surface bound to $d \geq 18$ using vector fields on the universal family.
- **2010** — Diverio–Merker–Rousseau: entire curves in a generic $X_d \subset \mathbb{P}^n$ are algebraically degenerate for $d \geq 2^{n^5}$.
- **2015** — Siu proves hyperbolicity of generic hypersurfaces of sufficiently high (effective but enormous) degree, using slanted vector fields and Wronskians.
- **2017** — Brotbek gives a substantially cleaner proof via Wronskian jet differentials on Fermat-type deformations, for $d \gg n$ (initially non-effective).
- **2019–2020** — Brotbek–Deng handle the complement conjecture for general hypersurfaces of high degree; Deng and Demailly extract effective bounds. Demailly's survey records $d \geq \big\lfloor (en)^{2n+2}/5 \big\rfloor$ for hyperbolicity of general $X_d \subset \mathbb{P}^n$.

**Current SOTA:** the conjecture is *true for $d$ large*, with the best general effective threshold exponential in $n$; the sharp bound $2n-1$ is open in every dimension $n \geq 3$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$ (curves in $\mathbb{P}^2$) | Smooth $C_d$ hyperbolic $\iff$ genus $\tfrac{(d-1)(d-2)}{2} \geq 2 \iff d \geq 4$; every member, not just generic | classical |
| Surfaces in $\mathbb{P}^3$ | Generic $X_d$ hyperbolic for $d \geq 18$ (conjectured: $d\ge 5$) | Păun 2008 (after Demailly–El Goul $d \geq 21$) |
| Surfaces of general type | Entire curves algebraically degenerate if $c_1^2 > c_2$ | Bogomolov; McQuillan 1998 |
| All $n$, algebraic degeneracy | Generic $X_d$, $d \geq 2^{n^5}$ | Diverio–Merker–Rousseau 2010 |
| All $n$, full hyperbolicity | Generic $X_d$ for $d \geq d(n)$, $d(n)$ effective, $\approx (en)^{2n+2}/5$ | Siu 2015; Brotbek 2017; Demailly 2020 |
| Complements | $\mathbb{P}^n \setminus X_d$ hyperbolic for general $X_d$ of high degree (effective) | Brotbek–Deng 2019 |
| Complements, $n=2$ | Generic plane curve of degree $d \geq 15$ has hyperbolic complement (conjectured $d\ge5$) | Darondeau 2016 |
| Rational curves | No rational curves on generic $X_d$, $d \geq 2n-1$ — sharp | Voisin 1996 |
| Explicit examples | Hyperbolic surfaces in $\mathbb{P}^3$ of degree as low as $6$ (Duval), and explicit families in low degree | Shiffman–Zaidenberg; Duval |
| Reduction | If entire curves on generic $X_d \subset \mathbb{P}^{2n-1}$ are algebraically degenerate, generic $X_d \subset \mathbb{P}^n$ is hyperbolic | Riedl–Yang 2022 |

## 5. Principal Obstacles

- **Negativity of $T_X$ fails.** $T_X$ for $X_d \subset \mathbb{P}^n$ is never negative in the naive sense; hyperbolicity must be extracted from higher-order jet bundles, where positivity is only *asymptotic* in the jet order $k$ and weight $m$.
- **Riemann–Roch gives existence, not location.** Demailly's holomorphic Morse inequalities produce sections of $E_{k,m}T_X^*\otimes\mathcal{O}(-\delta m)$ only once $d$ exceeds a threshold driven by an alternating Euler-characteristic estimate; the error terms are of size comparable to the main term, forcing exponential-in-$n$ degrees.
- **The base locus problem.** Vanishing theorems give algebraic degeneracy: $f(\mathbb{C})$ lies in a subvariety $Y \subsetneq X$. Passing from degeneracy to hyperbolicity requires controlling *every* $Y$, and the induction on dimension re-opens the whole problem with no control on $\deg Y$.
- **Slanted vector fields cost degree.** Siu's and Păun's method differentiates jet differentials along vector fields on the universal family $\mathcal{X} \subset \mathbb{P}^n \times \mathbb{P}^{N_d}$ with poles of order growing linearly in the jet order; killing the pole order forces $d$ to grow at least like $n^2$ per differentiation step, and $k \approx n$ steps are needed.
- **No lower bound tools.** There is no known method to *certify* that a specific quintic surface admits no entire curve; the transcendental object (an entire map) is not detected by any finite algebraic obstruction.
- **Genericity is unavoidable but slippery.** The bad locus is a countable-union-of-subvarieties phenomenon a priori; showing it is Zariski-closed (rather than merely of measure zero) requires care, and metric-geometry arguments (Ahlfors–Schwarz, Nevanlinna second main theorem) degrade exactly at the target degrees.

## 6. The Gap

Proven: hyperbolicity for $d \gtrsim (en)^{2n+2}/5$; for $n=3$, $d \geq 18$. Conjectured: $d \geq 2n-1$; for $n=3$, $d \geq 5$.

The gap is quantitative in every dimension and qualitative in method. Concretely, the missing step is a *sharp* positivity statement: production of enough sections of $E_{k,m}T_{X}^* \otimes \mathcal{O}_X(-1)$ on a generic $X_d$ with $d = 2n-1$ and $k$ of order $n$ — the Morse-inequality count currently goes negative there. The known reductions sharpen the target: by Riedl–Yang, proving Green–Griffiths algebraic degeneracy for generic hypersurfaces of degree $d$ in $\mathbb{P}^{2n-1}$ delivers full hyperbolicity in $\mathbb{P}^n$ at the same degree. So the effective content of the conjecture reduces to *degeneracy at degree $2n-1$ in ambient dimension $2n-1$*, currently far out of reach.

## 7. Current Research (as of June 2026)

- **Wronskian / Brotbek-style constructions.** Explicit jet differentials built from Wronskians of the defining equations, deformed to Fermat-type models. Groups around Brotbek (Strasbourg/IRMA) and Deng (Sorbonne/CNRS) continue to push effectivity downward. *(frontier — verify current record bounds)*
- **Effective Nevanlinna theory.** Second Main Theorem with truncated counting functions for maps into $\mathbb{P}^n$ omitting hypersurfaces (Ru, Vojta-style), aimed at the complement conjecture with sharp $2n+1$.
- **Foliation-theoretic methods.** McQuillan's Diophantine approximation on foliated surfaces, extended to higher dimension via Ahlfors currents; obstruction is the classification of foliations with non-negative canonical class.
- **Orbifold and logarithmic pairs.** Campana's orbifold framework recasts both versions of the conjecture as a single statement about pairs $(\mathbb{P}^n, \tfrac{c}{d}X)$; interpolation in $c$ is being used to transfer bounds between the compact and complement cases.
- **Hyperbolicity of moduli and Viehweg–Zuo sheaves.** Techniques from Popa–Schnell and Deng's work on Viehweg hyperbolicity feeding back into jet-differential positivity.
- **Explicit low-degree examples.** Ongoing search for hyperbolic surfaces in $\mathbb{P}^3$ of degree $5$; degree $6$ examples are known (Duval), degree $5$ remains unresolved even for a single explicit surface. *(frontier — verify)*

## 8. Future Work

1. Prove Green–Griffiths algebraic degeneracy at degree $d = 2n-1$ and combine with Riedl–Yang to obtain the sharp Kobayashi bound.
2. Sharpen Demailly's holomorphic Morse inequalities on the Semple tower — replace the asymptotic $k \to \infty$ regime by an exact count at $k = n$.
3. Produce one explicit hyperbolic quintic surface in $\mathbb{P}^3$; this would fix the sharpness of $2n-1$ at $n=3$ in the strongest concrete sense.
4. Develop degeneration/specialization arguments that transfer hyperbolicity across the parameter space $\mathbb{P}^{N_d}$ without degree loss.
5. Settle the complement conjecture at $d = 2n+1$ for $n=2$ (degree $5$ plane curves), where the current bound is $15$.

## 9. Key References

- **[Foundational]** S. Kobayashi. *Hyperbolic Manifolds and Holomorphic Mappings.* Marcel Dekker, New York, 1970.
- **[Foundational]** S. Kobayashi. *Hyperbolic Complex Spaces.* Grundlehren der mathematischen Wissenschaften 318, Springer, 1998.
- **[Foundational]** R. Brody. *Compact manifolds and hyperbolicity.* Transactions of the American Mathematical Society 235 (1978), 213–219.
- **[Foundational]** M. Green, P. Griffiths. *Two applications of algebraic geometry to entire holomorphic mappings.* In: The Chern Symposium 1979, Springer, 1980, 41–74.
- **[Foundational]** J.-P. Demailly. *Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials.* Proceedings of Symposia in Pure Mathematics 62.2, AMS, 1997, 285–360.
- **[Key]** C. Voisin. *On a conjecture of Clemens on rational curves on hypersurfaces.* Journal of Differential Geometry 44 (1996), 200–213.
- **[Key]** Y.-T. Siu, S.-K. Yeung. *Hyperbolicity of the complement of a generic smooth curve of high degree in the complex projective plane.* Inventiones Mathematicae 124 (1996), 573–618.
- **[Key]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS 87 (1998), 121–174.
- **[Key]** J.-P. Demailly, J. El Goul. *Hyperbolicity of generic surfaces of high degree in projective 3-space.* American Journal of Mathematics 122 (2000), 515–546.
- **[Key]** M. Păun. *Vector fields on the total space of hypersurfaces in the projective space and hyperbolicity.* Mathematische Annalen 340 (2008), 875–892.
- **[Key]** S. Diverio, J. Merker, E. Rousseau. *Effective algebraic degeneracy.* Inventiones Mathematicae 180 (2010), 161–223.
- **[SOTA]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae 202 (2015), 1069–1166.
- **[SOTA]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS 126 (2017), 1–34.
- **[SOTA]** D. Brotbek, Y. Deng. *Hyperbolicity of the complements of general hypersurfaces of high degree.* Geometric and Functional Analysis 29 (2019), 690–750.
- **[SOTA]** E. Riedl, D. Yang. *Applications of a Grassmannian technique to hyperbolicity, Chow equivalency, and Seshadri constants.* Journal of Algebraic Geometry 31 (2022).
- **[Survey]** J.-P. Demailly. *Recent results on the Kobayashi and Green–Griffiths–Lang conjectures.* Japanese Journal of Mathematics 15 (2020), 1–120.
- **[Survey]** S. Diverio, E. Rousseau. *A Survey on Hyperbolicity of Projective Hypersurfaces.* Publicações Matemáticas do IMPA, 2011.

## 10. Worked Example / Concrete Special Case

**Why "generic" cannot be dropped: the Fermat quintic in $\mathbb{P}^3$.**

Take $n=3$, $d = 5 = 2n-1$ — the first case of the conjecture. Let
$$X : x_0^5 + x_1^5 + x_2^5 + x_3^5 = 0 \subset \mathbb{P}^3.$$
$X$ is smooth (the Jacobian $5x_i^4$ vanishes simultaneously only at the origin) and of general type since $K_X = \mathcal{O}_X(d-n-1) = \mathcal{O}_X(1)$ is ample.

Fix $\zeta, \eta$ with $\zeta^5 = \eta^5 = -1$ and consider the line
$$L = \{[\,s : \zeta s : t : \eta t\,] : [s:t] \in \mathbb{P}^1\} \subset \mathbb{P}^3.$$
Substituting: $s^5 + \zeta^5 s^5 + t^5 + \eta^5 t^5 = s^5 - s^5 + t^5 - t^5 = 0$. So $L \subset X$. There are $5 \times 5 = 25$ such lines for this pairing of coordinates, and $3 \times 25 = 75$ in total from the three pairings.

Now $L \cong \mathbb{P}^1$ admits the nonconstant entire curve $\mathbb{C} \to \mathbb{P}^1 \subset X$, $z \mapsto [1 : z]$ in the parameter. By Brody's theorem, **the Fermat quintic is not hyperbolic**. Indeed $d_X \equiv 0$ on $L$: the Kobayashi pseudodistance of $\mathbb{P}^1$ vanishes identically, and $d_X \leq d_L$ by the distance-decreasing property of holomorphic inclusions.

**Consistency with the conjecture.** Count lines on a generic quintic surface. The Grassmannian $G(1,3)$ of lines in $\mathbb{P}^3$ has dimension $4$. Requiring a line $L$ to lie in $X_d$ imposes $d+1$ conditions (the restriction $F|_L$ is a binary form of degree $d$, with $d+1$ coefficients). Expected dimension of the Fano scheme:
$$\dim F(X_d) = 4 - (d+1) = 3 - d.$$
For $d = 5$ this is $-2 < 0$: the generic quintic contains **no** lines. The Fermat surface is exactly a member of the excess-dimensional (non-generic) locus. More strongly, Voisin's theorem gives no rational curves at all on a generic $X_d \subset \mathbb{P}^3$ with $d \geq 5 = 2n-1$, and Clemens-type results bound genus-$1$ curves as well.

**Where the argument stops.** Ruling out *algebraic* curves of low genus is a finite-dimensional computation on the parameter space. Ruling out a transcendental $f : \mathbb{C} \to X_5$ requires jet differentials: one needs a nonzero
$$P \in H^0\big(X_5,\ E_{k,m}T_{X_5}^* \otimes \mathcal{O}_{X_5}(-1)\big).$$
Demailly's Morse-inequality estimate for $X_d \subset \mathbb{P}^3$ certifies such sections only once $d$ is well past $5$; combined with vector-field arguments on the universal family, Păun reaches $d \geq 18$. The interval $5 \leq d \leq 17$ for surfaces in $\mathbb{P}^3$ is the smallest concrete open piece of the Kobayashi conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*