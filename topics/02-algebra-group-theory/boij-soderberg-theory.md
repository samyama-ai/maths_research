---
id: 02-algebra-group-theory/boij-soderberg-theory
title: "Boij-Soderberg Theory"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boij–Söderberg Theory

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/boij-soderberg-theory` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $S = k[x_1,\dots,x_n]$ be a polynomial ring over a field, standard graded. Every finitely generated graded $S$-module $M$ has a minimal free resolution
$$0 \to \bigoplus_j S(-j)^{\beta_{p,j}} \to \cdots \to \bigoplus_j S(-j)^{\beta_{0,j}} \to M \to 0,$$
and the **Betti table** $\beta(M) = (\beta_{i,j}(M)) \in \mathbb{Z}^{\,\mathbb{N}\times\mathbb{Z}}$ is a discrete invariant. The classification question: *which tables arise?*

The **Boij–Söderberg conjectures** (2008) answer this up to positive rational scalar. They assert that the rational cone spanned by Betti tables of graded Cohen–Macaulay modules of codimension $c$ is a **simplicial fan** whose extremal rays are the *pure diagrams* $\pi(\mathbf d)$ indexed by strictly increasing degree sequences $\mathbf d = (d_0 < d_1 < \cdots < d_c)$, with the maximal cones spanned by *chains* in the componentwise partial order. Equivalently: every Betti table has a unique expression
$$\beta(M) \;=\; \sum_{t=1}^{r} c_t\, \pi(\mathbf d^{\,t}), \qquad c_t \in \mathbb{Q}_{>0}, \quad \mathbf d^{\,1} < \mathbf d^{\,2} < \cdots < \mathbf d^{\,r}.$$

A complete proof requires two halves: (i) **existence** — for every $\mathbf d$ there is a module with pure resolution of type $\mathbf d$; (ii) **positivity** — every table decomposes as above, i.e. the pure diagrams are the only extremal rays. Both were settled by Eisenbud–Schreyer (2009) for Cohen–Macaulay modules and by Boij–Söderberg (2012) in general. What remains open is the same classification over **non-regular base rings**, in the **multigraded** setting, and at the level of **integral** (not rational) structure.

## 2. Mathematical Foundations

**Pure resolutions.** A resolution is *pure of type* $\mathbf d = (d_0<\cdots<d_c)$ if $\beta_{i,j} \neq 0 \Rightarrow j = d_i$. Herzog–Kühl (1984): if $M$ is Cohen–Macaulay of codimension $c$ with a pure resolution of type $\mathbf d$, the Betti numbers are determined up to scalar:
$$\beta_{i,d_i}(M) \;=\; \beta_{0,d_0}(M)\prod_{j\neq 0,i}\frac{d_j-d_0}{d_j-d_i}.$$
Normalize to the **pure diagram**
$$\pi(\mathbf d)_{i,d_i} \;=\; \prod_{j \neq i} \frac{1}{|d_j - d_i|}, \qquad 0 \le i \le c,$$
all other entries zero. These satisfy the Herzog–Kühl equations $\sum_i (-1)^i \beta_{i,d_i} d_i^{\,q} = 0$ for $0 \le q \le c-1$.

**Partial order.** $\mathbf d \le \mathbf e$ iff $d_i \le e_i$ for all $i$ (padding by $+\infty$ in the non-Cohen–Macaulay setting). Chains in this poset index the maximal cones.

**The decomposition algorithm.** Given $\beta$, let $\mathbf d^1$ be the componentwise minimal degree sequence supported by $\beta$; set $c_1 = \min_i \beta_{i,d^1_i}/\pi(\mathbf d^1)_{i,d^1_i}$, subtract $c_1\pi(\mathbf d^1)$, repeat. Termination with nonnegative coefficients is exactly the positivity half of the theorem.

**Duality with cohomology.** Eisenbud–Schreyer's proof pairs Betti tables against **cohomology tables** $\gamma(\mathcal F) = (h^i(\mathbb{P}^{n-1}, \mathcal F(j)))$ of coherent sheaves. For each $\tau \in \mathbb{Z}$ they define a bilinear form
$$\langle \beta, \gamma\rangle_\tau \;=\; \sum_{j-i \le \tau} \beta_{i,j}\,\gamma_{\,j-i,\,-j} \;-\; \sum_{j-i > \tau} \beta_{i,j}\,\gamma_{\,j-i-1,\,-j},$$
and prove $\langle \beta(M), \gamma(\mathcal F)\rangle_\tau \ge 0$ for all $M$, $\mathcal F$, $\tau$. Each sheaf therefore supplies a supporting hyperplane; **supernatural bundles** (those with $h^i(\mathcal F(j))\neq 0$ for at most one $i$ per $j$, with prescribed root sequence) give exactly the facet equations of the simplicial fan. The duality is perfect: the cone of cohomology tables of sheaves on $\mathbb{P}^{n-1}$ is likewise a fan with supernatural tables as extremal rays.

**Consequence (multiplicity conjecture).** For $S/I$ Cohen–Macaulay of codimension $c$, writing $d_i^{\min} = \min\{j : \beta_{i,j}\neq0\}$ and $d_i^{\max}$ analogously,
$$\frac{1}{c!}\prod_{i=1}^{c} d_i^{\min} \;\le\; e(S/I) \;\le\; \frac{1}{c!}\prod_{i=1}^{c} d_i^{\max},$$
the Herzog–Huneke–Srinivasan conjecture, with equality iff the resolution is pure (Huneke–Miller).

## 3. History & State of the Art (SOTA)

- **1984–85.** Herzog–Kühl compute Betti numbers of pure resolutions; Huneke–Miller prove $e = \frac{1}{c!}\prod d_i$ for pure Cohen–Macaulay resolutions. Herzog and Srinivasan conjecture the two-sided multiplicity bound.
- **2008.** Boij and Söderberg (*J. London Math. Soc.* 78) propose the cone/simplicial-fan picture, prove it *implies* the multiplicity conjecture, and verify low-dimensional cases.
- **2009.** Eisenbud and Schreyer (*J. Amer. Math. Soc.* 22) prove the conjectures for Cohen–Macaulay modules: existence of pure resolutions in all characteristics via the "$\mathbb{P}^1$-pushforward"/Schur-functor construction, positivity via the cohomological pairing. Simultaneously they classify cohomology tables of vector bundles up to scalar.
- **2011.** Eisenbud–Fløystad–Weyman give the $\mathrm{GL}_n$-equivariant construction of pure resolutions in characteristic $0$ (*Ann. Inst. Fourier* 61).
- **2012.** Boij–Söderberg (*Algebra & Number Theory* 6) extend the decomposition to arbitrary (non-Cohen–Macaulay) graded modules, with degree sequences allowed to have $\infty$ entries.
- **2009–present.** The theory becomes a program: integral structure (Erman), local and non-graded analogues (Berkesch–Erman–Kummini–Sam), other base rings, multigraded and toric versions (Boij–Fløystad; Berkesch–Erman–Smith), categorification (Eisenbud–Erman).

## 4. Partial Results / Verified Cases

- **Fully solved:** $S = k[x_1,\dots,x_n]$, standard $\mathbb{Z}$-grading, any field $k$, any characteristic; Cohen–Macaulay modules of every codimension $c \le n$ (Eisenbud–Schreyer 2009) and all finitely generated graded modules (Boij–Söderberg 2012). Existence of pure resolutions holds for **every** strictly increasing $\mathbf d \in \mathbb{Z}^{c+1}$; equivariant models exist in characteristic $0$ for all $\mathbf d$.
- **Cohomology side:** cohomology tables of vector bundles, and of arbitrary coherent sheaves, on $\mathbb{P}^{n-1}$ are classified up to positive rational multiple (Eisenbud–Schreyer 2009; Erman–Sam 2016 for supernatural monad refinements).
- **Integral structure:** the *semigroup* of Betti tables is strictly smaller than the lattice points of the cone; Erman (2009) exhibits explicit non-attainable integral points, and computes the semigroup in codimension $\le 2$ over $k[x,y]$.
- **Other rings, partial answers:** bigraded artinian modules of codimension $2$ over $k[x,y]$ (Boij–Fløystad 2011); modules over a hypersurface/complete-intersection ring where the fan is known to be **non-simplicial** — Gibbons–Jeffries–Mayes–Raicu–Stone–White (2015) give explicit Betti diagrams over complete intersections with two distinct decompositions.
- **Local rings:** Berkesch–Erman–Kummini–Sam (*Math. Ann.* 354, 2012) determine the cone of total Betti sequences of finite-length modules over a regular local ring in the ungraded setting, showing the extremal rays are *not* given by pure sequences.
- **Rational normal curves / toric:** Betti cones computed over the coordinate ring of the rational normal curve of degree $d$; virtual resolutions on $\mathbb{P}^{a}\times\mathbb{P}^{b}$ (Berkesch–Erman–Smith 2020) supply the correct multigraded objects but no full classification.

## 5. Principal Obstacles

- **Existence fails outside the regular case.** Over $S$, pure resolutions of every type are constructed by equivariant methods or by pushforward from $\mathbb{P}^1$. Over a quotient $R = S/f$, resolutions are typically infinite and matrix-factorization periodicity forbids most pure types; the extremal-ray candidates are not modules but limits.
- **No positivity pairing.** The proof of positivity is entirely dual: it needs a class of sheaves (supernatural bundles) whose cohomology tables cut out the facets, plus Beilinson-type functorial machinery. Over singular or multigraded bases the analogous "supernatural" objects either do not exist or fail to span, so the supporting hyperplanes are unknown.
- **Multigraded degeneration.** In $\mathbb{Z}^m$-gradings the Herzog–Kühl equations become underdetermined: a multidegree sequence does not pin down the Betti numbers up to scalar, so "pure diagram" ceases to be a single ray. Local cohomology vanishing on products of projective spaces is governed by several twisting parameters at once.
- **Integrality is arithmetic, not convex.** Rational decomposition gives no control over which integer points are realized; the coefficients $c_t$ have denominators divisible by products $\prod |d_j-d_i|$, and clearing them requires modules of exponentially large rank that may not exist.
- **Local/ungraded loss of information.** Without a grading there is no degree sequence at all; only total Betti numbers survive, and the Buchsbaum–Eisenbud–Horrocks rank conjecture ($\beta_i \ge \binom{c}{i}$) — implied by Boij–Söderberg in the graded case for many situations — remains open ungraded.

## 6. The Gap

Proven: the classification up to positive rational multiple over a *regular* standard-graded ring with a *single* grading. Not proven, and the precise boundary:

1. **Integral realization.** Characterize the semigroup $\{\beta(M)\}\subset$ cone, not just its rational hull. Known only in very small codimension.
2. **Non-regular base.** For $R$ Gorenstein artinian, a complete intersection, or a toric coordinate ring, describe $\mathrm{Cone}(\beta(M))$. The fan is known to be non-simplicial in at least one complete-intersection example, so even the *shape* of the answer is unsettled.
3. **Multigraded.** Identify the extremal rays of the cone of $\mathbb{Z}^m$-graded Betti tables on $\mathbb{P}^{a_1}\times\cdots\times\mathbb{P}^{a_m}$; the codimension-$2$ bigraded case is the only complete answer.
4. **Categorification.** Eisenbud–Erman lift the decomposition to a filtration of complexes; extending this to a functorial statement valid over arbitrary rings is the structural version of the gap.

## 7. Current Research (as of June 2026)

- **Multigraded / virtual resolutions.** Groups around Berkesch (Minnesota), Erman (Hawai‘i), and Smith (Queen's) continue to develop virtual resolutions on smooth toric varieties as the right replacement for minimal free resolutions; a Boij–Söderberg decomposition for virtual Betti tables is the stated target. *(frontier — verify)*
- **Non-regular base rings.** Work extending Boij–Fløystad to short Gorenstein and Koszul rings, using Clements–Lindström and exterior-algebra analogues; partial cone descriptions for quotients by pure powers.
- **Local and totally reflexive modules.** Continuation of Berkesch–Erman–Kummini–Sam on shapes of resolutions over local rings, connected to the Buchsbaum–Eisenbud–Horrocks rank conjecture.
- **Computation.** The `BoijSoederberg` package in *Macaulay2* implements the decomposition algorithm, pure-diagram bases, and the Eisenbud–Schreyer pairing; large-scale searches for non-attainable integral tables continue.
- **Representation-theoretic refinements.** Equivariant and Schur-functor constructions of pure complexes in positive characteristic, and supernatural analogues of Beilinson monads (Erman–Sam).

## 8. Future Work

- Find a positivity pairing that does not rely on $\mathbb{P}^{n-1}$: an intrinsic convexity proof would immediately transport to singular and multigraded settings.
- Determine the semigroup of Betti tables in codimension $3$ over $k[x,y,z]$; this is the smallest case where integrality is genuinely unknown.
- Classify which pure multidegree types are realized on $\mathbb{P}^1\times\mathbb{P}^1$, the minimal multigraded test case.
- Use the categorified duality of Eisenbud–Erman to extract new numerical inequalities on free complexes, aiming at Buchsbaum–Eisenbud–Horrocks.
- Extend the multiplicity bounds to non-Cohen–Macaulay and to quotients of non-regular rings, where the current inequalities are known only for special ideals.

## 9. Key References

- **[Foundational]** J. Herzog, M. Kühl. *On the Betti numbers of finite pure and linear resolutions.* Communications in Algebra 12 (1984), 1627–1646.
- **[Foundational]** C. Huneke, M. Miller. *A note on the multiplicity of Cohen–Macaulay algebras with pure resolutions.* Canadian Journal of Mathematics 37 (1985), 1149–1162. [DOI](https://doi.org/10.4153/cjm-1985-062-4)
- **[Foundational]** M. Boij, J. Söderberg. *Graded Betti numbers of Cohen–Macaulay modules and the multiplicity conjecture.* Journal of the London Mathematical Society (2) 78 (2008), 85–106. [DOI](https://doi.org/10.1112/jlms/jdn013)
- **[SOTA]** D. Eisenbud, F.-O. Schreyer. *Betti numbers of graded modules and cohomology of vector bundles.* Journal of the American Mathematical Society 22 (2009), 859–888. [DOI](https://doi.org/10.1090/s0894-0347-08-00620-6)
- **[SOTA]** M. Boij, J. Söderberg. *Betti numbers of graded modules and the multiplicity conjecture in the non-Cohen–Macaulay case.* Algebra & Number Theory 6 (2012), 437–454. [DOI](https://doi.org/10.2140/ant.2012.6.437)
- **[SOTA]** D. Eisenbud, G. Fløystad, J. Weyman. *The existence of equivariant pure free resolutions.* Annales de l'Institut Fourier 61 (2011), 905–926. [DOI](https://doi.org/10.5802/aif.2632)
- **[Recent]** D. Erman. *The semigroup of Betti diagrams.* Algebra & Number Theory 3 (2009), 341–365. [DOI](https://doi.org/10.2140/ant.2009.3.341)
- **[Recent]** C. Berkesch, D. Erman, M. Kummini, S. V Sam. *Shapes of free resolutions over a local ring.* Mathematische Annalen 354 (2012), 939–954. [DOI](https://doi.org/10.1007/s00208-011-0760-2)
- **[Recent]** C. Berkesch, D. Erman, M. Kummini, S. V Sam. *Poset structures in Boij–Söderberg theory.* International Mathematics Research Notices 2012 (16), 3596–3618. [DOI](https://doi.org/10.1093/imrn/rnr222)
- **[Recent]** D. Eisenbud, D. Erman, F.-O. Schreyer. *Filtering free resolutions.* Compositio Mathematica 149 (2013), 754–772. [DOI](https://doi.org/10.1112/s0010437x12000760)
- **[Recent]** D. Eisenbud, D. Erman. *Categorified duality in Boij–Söderberg theory and invariants of free complexes.* Journal of the European Mathematical Society 19 (2017), 2657–2695. [DOI](https://doi.org/10.4171/jems/725)
- **[Recent]** C. Berkesch, D. Erman, G. G. Smith. *Virtual resolutions for a product of projective spaces.* Algebraic Geometry 7 (2020), 460–481. [DOI](https://doi.org/10.14231/ag-2020-013)
- **[Recent]** C. Gibbons, J. Jeffries, S. Mayes, C. Raicu, B. Stone, B. White. *Nonsimplicial decompositions of Betti diagrams of complete intersections.* Journal of Commutative Algebra 7 (2015), 189–206.
- **[Survey]** G. Fløystad. *Boij–Söderberg theory: introduction and survey.* In: Progress in Commutative Algebra 1, de Gruyter, 2012, 1–54. [DOI](https://doi.org/10.1515/9783110250404.1)
- **[Survey]** D. Eisenbud, F.-O. Schreyer. *Boij–Söderberg theory.* In: Combinatorial Aspects of Commutative Algebra and Algebraic Geometry, Abel Symposia 6, Springer, 2011, 35–48. [DOI](https://doi.org/10.1007/978-3-642-19492-4_3)

## 10. Worked Example / Concrete Special Case

Take $S = k[x,y]$ and $M = S/I$ with $I = (x^2,\,xy,\,y^3)$, an artinian (hence Cohen–Macaulay of codimension $c=2$) module. The minimal free resolution is
$$0 \to S(-3)\oplus S(-4) \xrightarrow{\ \phi\ } S(-2)^2 \oplus S(-3) \to S \to M \to 0,$$
from the syzygies $y\cdot x^2 - x\cdot xy = 0$ (degree $3$) and $y^2\cdot xy - x\cdot y^3 = 0$ (degree $4$). Betti table, in Macaulay2 layout (row $= j-i$):

```
       0   1   2
0:     1   .   .
1:     .   2   1
2:     .   1   1
```

so $\beta_{0,0}=1$, $\beta_{1,2}=2$, $\beta_{1,3}=1$, $\beta_{2,3}=1$, $\beta_{2,4}=1$. The resolution is **not** pure. Apply the decomposition algorithm.

*Step 1.* Minimal degree sequence in the support: $\mathbf d^1=(0,2,3)$, with
$$\pi(0,2,3) = \left(\tfrac{1}{2\cdot3},\ \tfrac{1}{2\cdot1},\ \tfrac{1}{3\cdot1}\right) = \left(\tfrac16,\tfrac12,\tfrac13\right).$$
Ratios $1/\tfrac16=6$, $2/\tfrac12=4$, $1/\tfrac13=3$; take $c_1=3$. Subtract $3\pi(0,2,3)=(\tfrac12,\tfrac32,1)$ at $(0,0),(1,2),(2,3)$. Remainder: $(0,0)\!=\!\tfrac12$, $(1,2)\!=\!\tfrac12$, $(1,3)\!=\!1$, $(2,4)\!=\!1$.

*Step 2.* $\mathbf d^2=(0,2,4)$, $\pi = (\tfrac18,\tfrac14,\tfrac18)$. Ratios $4,\,2,\,8$; take $c_2=2$. Subtract $(\tfrac14,\tfrac12,\tfrac14)$. Remainder: $(0,0)=\tfrac14$, $(1,3)=1$, $(2,4)=\tfrac34$.

*Step 3.* $\mathbf d^3=(0,3,4)$, $\pi=(\tfrac1{12},\tfrac13,\tfrac14)$. All three ratios equal $3$; take $c_3=3$ and the remainder is zero.

Hence the unique decomposition
$$\beta(M) \;=\; 3\,\pi(0,2,3) \;+\; 2\,\pi(0,2,4) \;+\; 3\,\pi(0,3,4),$$
with $(0,2,3) < (0,2,4) < (0,3,4)$ a chain — exactly as the theorem predicts.

*Multiplicity check.* $M$ has $k$-basis $1,x,y,y^2$, so $e(M)=4$. Here $\mathbf d^{\min}=(0,2,3)$ and $\mathbf d^{\max}=(0,3,4)$, giving
$$\tfrac{1}{2!}(2\cdot 3) = 3 \;\le\; 4 \;\le\; \tfrac{1}{2!}(3\cdot 4) = 6,$$
confirming the Herzog–Huneke–Srinivasan bounds, with strict inequality on both sides because the resolution is not pure.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*