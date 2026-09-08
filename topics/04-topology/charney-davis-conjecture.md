---
id: 04-topology/charney-davis-conjecture
title: "Charney-Davis Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Charney-Davis Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/charney-davis-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $L$ be a **flag** simplicial complex that triangulates an odd-dimensional sphere $S^{2e-1}$ (equivalently, a flag generalized homology $(2e-1)$-sphere). "Flag" means every set of pairwise adjacent vertices spans a face. Define the **Charney–Davis quantity**

$$\kappa(L) \;=\; \sum_{\sigma \in L} \left(-\tfrac{1}{2}\right)^{|\sigma|} \;=\; \sum_{i=0}^{2e} \left(-\tfrac{1}{2}\right)^{i} f_{i-1}(L),$$

where the sum runs over all faces including $\sigma = \varnothing$, and $f_{i-1}$ counts faces with $i$ vertices.

**Conjecture (Charney–Davis, 1995).** $(-1)^e \kappa(L) \ge 0$.

Equivalently, in terms of the $h$-polynomial (Section 2), $(-1)^e h_L(-1) \ge 0$, since $h_L(-1) = 2^{2e}\kappa(L)$.

A complete proof must handle all flag triangulations of all odd-dimensional spheres — the number of combinatorial types grows superexponentially and no classification exists. A disproof requires one explicit flag homology $(2e-1)$-sphere with $(-1)^e\kappa < 0$; because the statement is a finite rational inequality per complex, a single certified counterexample settles it. The conjecture is *false* for general (non-flag) spheres and for flag complexes that are not spheres, so both hypotheses are essential.

## 2. Mathematical Foundations

**$f$- and $h$-vectors.** For a $(d-1)$-dimensional simplicial complex $L$ with $f_{i-1}$ faces of cardinality $i$,

$$h_L(t) \;=\; \sum_{i=0}^{d} f_{i-1}\, t^{i}(1-t)^{d-i}, \qquad h_L(t)=\sum_{i=0}^d h_i t^i .$$

Setting $t=-1$ gives $h_L(-1) = \sum_i f_{i-1}(-1)^i 2^{d-i} = 2^d \kappa(L)$. For a homology sphere the Dehn–Sommerville relations give $h_i = h_{d-i}$; when $d = 2e$ is even this forces no sign constraint on $h(-1)$, which is exactly why the quantity is interesting.

**$\gamma$-vector.** By Dehn–Sommerville, for $d=2e$ one may write uniquely

$$h_L(t) \;=\; \sum_{i=0}^{e} \gamma_i\, t^{i}(1+t)^{\,2e-2i}, \qquad \gamma_e = (-1)^e h_L(-1).$$

**Gal's conjecture** ($\gamma_i \ge 0$ for all $i$, for every flag homology sphere) therefore strictly implies Charney–Davis. Note $\gamma_0=1$ and $\gamma_1 = f_0 - 2d$.

**Origin in nonpositive curvature.** Let $M^{2e}$ be a closed piecewise Euclidean **cubical** manifold. By Gromov's link condition, $M$ is nonpositively curved (locally CAT(0)) iff the link $\mathrm{Lk}(v)$ of every vertex is a flag simplicial complex; for a manifold these links are flag $(2e-1)$-spheres. A combinatorial Gauss–Bonnet computation gives

$$(-1)^e \chi(M^{2e}) \;=\; (-1)^e \sum_{v \in M^{(0)}} \kappa\big(\mathrm{Lk}(v)\big).$$

Hence the conjecture implies the **Hopf–Chern conjecture** $(-1)^e\chi(M^{2e})\ge 0$ for this class of nonpositively curved spaces, term by term. It is also equivalent, via Davis–Okun, to a special case of the **Singer conjecture** on $\ell^2$-Betti numbers of right-angled Coxeter groups: $b^{(2)}_i(\Sigma_L)=0$ for $i \ne e$, where $\Sigma_L$ is the Davis complex.

**Algebraic side.** For flag $L$ the Stanley–Reisner ring $\mathbb{k}[L]$ has a quadratic monomial ideal, so $\mathbb{k}[L]$ is a quadratic algebra; the conjecture is a statement about the alternating sum of its Hilbert-series numerator coefficients. Leung–Reiner reformulated the polytopal case as a nonnegativity statement for the signature of the associated toric variety.

## 3. History & State of the Art (SOTA)

- **1995.** Ruth Charney and Michael Davis, *The Euler characteristic of a nonpositively curved, piecewise Euclidean manifold* (Pacific J. Math. 171), pose the conjecture as the combinatorial residue of Hopf's problem for cubical CAT(0) manifolds. They verify $d=2$ ($e=1$).
- **2000.** Stanley lists it among his *Positivity problems and conjectures in algebraic combinatorics*, connecting it to the cd-index and to the Neggers–Stanley real-rootedness problem.
- **2001.** Davis–Okun prove the case $e=2$ (flag triangulations of $S^3$) via the Singer conjecture in dimension 4 for right-angled Coxeter groups, using Andreev's theorem and hyperbolization.
- **2002.** Leung–Reiner give the toric-signature reformulation.
- **2004–2005.** Brändén and Reiner–Welker link the conjecture to $(P,\omega)$-partition polynomials; Gal introduces the $\gamma$-vector, proves $\gamma \ge 0$ in dimension $\le 4$, and *disproves* the stronger "real root conjecture" (that $h_L$ has only real roots) for flag spheres of dimension $\ge 5$.
- **2006.** Karu proves nonnegativity of the cd-index for all Gorenstein* posets, which yields Charney–Davis for barycentric subdivisions of regular CW-spheres.
- **2008–2014.** Frohmader settles the flag analogue of the Kruskal–Katona problem; Volodin and Aisbett verify Gal's conjecture for flag nestohedra.
- **Since 2018.** Adiprasito's Lefschetz theorems for spheres settle the $g$-conjecture, but the $g$-theorem does *not* imply Charney–Davis: the latter is a signed alternating statement invisible to unimodality.

Status: open for all $e \ge 3$, i.e. for flag spheres of dimension $5, 7, 9, \dots$. No counterexample is known in any dimension.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| $e=1$ (flag $S^1$) | True. A flag 1-sphere is an $n$-cycle with $n\ge 4$; $-h(-1) = n-4 \ge 0$. |
| $e=2$ (flag $S^3$) | True (Davis–Okun 2001), unconditional after Perelman's geometrization. |
| Dimension $\le 4$ | Gal's stronger conjecture $\gamma_i \ge 0$ holds for all flag homology spheres of dimension $\le 4$. |
| $\gamma_1$, all dimensions | True: a flag $(d-1)$-sphere has $f_0 \ge 2d$ vertices, equality iff it is the boundary of the $d$-dimensional cross-polytope (join of $d$ copies of $S^0$). |
| Barycentric subdivisions | True for $\mathrm{sd}(K)$, $K$ any regular CW-sphere (Karu 2006, via cd-index nonnegativity); Nevo–Petersen–Tenner compute the $\gamma$-vector explicitly. |
| Coxeter complexes | True: $\gamma$ is a nonnegative peak/descent statistic for the finite Coxeter group. |
| Flag nestohedra | True (Volodin 2010; Aisbett 2014), including flag graph-associahedra and permutohedra. |
| Joins and products | Closed under join: $\gamma_{L_1 * L_2} = \gamma_{L_1}\gamma_{L_2}$, so the class of verified spheres is join-closed. |
| Sign-graded / $(P,\omega)$-posets | Brändén (2004) proves the Charney–Davis inequality for order-polynomial-type $W$-polynomials of sign-graded posets. |
| Small vertex counts | Exhaustive enumeration of flag 3- and 4-spheres with few vertices confirms $\gamma \ge 0$; no systematic certified enumeration exists for flag 5-spheres. |

## 5. Principal Obstacles

- **No Lefschetz mechanism for $h(-1)$.** Hard-Lefschetz-type theorems control $h_{i+1}-h_i$ (unimodality, the $g$-theorem). The Charney–Davis quantity is the *alternating* sum $\sum(-1)^i h_i$, which is not a difference of consecutive Hilbert-function values and is not detected by any known Lefschetz element or anisotropy argument.
- **Flagness is a global quadratic condition, not local.** Flagness constrains the Stanley–Reisner ideal to be generated in degree 2, but there is no known face-ring positivity property equivalent to it. Frankl–Füredi–Kalai-type $f$-vector bounds are necessary but far from sufficient: they do not see the sign of $h(-1)$.
- **The $\ell^2$ route stalls above dimension 4.** Davis–Okun's argument uses the Singer conjecture in dimension 4, where hyperbolization and Andreev's theorem supply hyperbolic reflection orbifolds. In dimension $\ge 6$ the Singer conjecture is itself open and there is no analogous geometrization input.
- **Real-rootedness is dead.** The natural strengthening — $h_L$ has only real roots, which would force $\gamma\ge0$ — was killed by Gal in dimension $\ge 5$, exactly where the conjecture becomes open. Analytic/total-positivity techniques thus have no direct handle.
- **No structure theory of flag spheres.** Unlike simplicial polytopes, flag spheres admit no shelling-type or bistellar-move classification with the flag property preserved; induction on dimension breaks because links of flag spheres are flag spheres but the recursion does not control $h(-1)$.

## 6. The Gap

Proven: $e \le 2$ in full generality, plus dimension-unrestricted results for structured families (barycentric subdivisions, Coxeter complexes, nestohedra) whose $\gamma$-vectors carry an *external* combinatorial model (cd-index, descent statistics, building-set operations). Open: an arbitrary flag homology $5$-sphere, with no polytopality, no group symmetry, and no subdivision structure.

The precise missing step is a **certificate for $\gamma_e \ge 0$ intrinsic to the flag condition**. Two candidate forms:
1. A combinatorial interpretation of $\gamma_e$ as the cardinality of a set canonically attached to any flag sphere (as descents do for Coxeter complexes).
2. An algebraic/geometric positivity theorem — e.g. a nonnegativity statement for the signature of the toric variety of a flag rational polytope (Leung–Reiner), or a vanishing theorem $b^{(2)}_i(\Sigma_L)=0$ for $i\ne e$ for all right-angled Coxeter groups.

Neither has been produced in any dimension $\ge 5$.

## 7. Current Research (as of June 2026)

- **Gal's conjecture as the working target.** Most current activity aims at $\gamma_i \ge 0$ rather than the single inequality $\gamma_e \ge 0$, on the grounds that the stronger statement has better inductive behaviour under joins, edge subdivisions and connected sums.
- **Anisotropy / characteristic-$p$ methods.** Following Adiprasito's Lefschetz machinery and the Papadakis–Petrotou anisotropy results for spheres, several groups have tried to adapt biased-pairing arguments to flag complexes. No published derivation of Charney–Davis from anisotropy exists. *(frontier — verify)*
- **Extremal/enumerative attacks.** Work on lower-bound theorems for flag spheres (Nevo–Petersen, Adamaszek, Zheng and collaborators) narrows the shape of a hypothetical counterexample by bounding $\gamma_1,\gamma_2$ and by Kruskal–Katona-type constraints among $\gamma_i$.
- **Geometric group theory.** Davis's school (Ohio State) continues the $\ell^2$-cohomology programme for right-angled Coxeter and Artin groups; the Singer conjecture in dimension 6 is the recognised blocking sub-problem.
- **Computational search.** Flag-sphere generation with symmetry reduction has been used to scan dimension 5 with small vertex counts; all scans so far are consistent with $\gamma\ge0$. *(frontier — verify; no exhaustive certified census published)*

## 8. Future Work

- Prove the Singer conjecture for right-angled Coxeter groups in dimension 6, which would give $e=3$ by the Davis–Okun mechanism.
- Find a "flag Lefschetz" theorem: an algebra structure on $\mathbb{k}[L]$ for flag $L$ whose Hilbert data compute $\gamma$ rather than $h$.
- Establish Gal's conjecture for flag spheres arising as duals of nonpositively curved cube complexes with additional hypotheses (e.g. hyperbolic, or with prescribed automorphism group).
- Extend Karu's cd-index positivity to non-subdivision flag spheres, or find a cd-like invariant supported on flag complexes.
- Settle whether $\gamma_i \ge 0$ can fail while $\gamma_e \ge 0$ holds — separating Gal's conjecture from Charney–Davis would redirect effort.

## 9. Key References

- **[Foundational]** R. Charney, M. Davis. *The Euler characteristic of a nonpositively curved, piecewise Euclidean manifold.* Pacific Journal of Mathematics **171** (1995), 117–137. [DOI](https://doi.org/10.2140/pjm.1995.171.117)
- **[Foundational]** M. W. Davis, B. Okun. *Vanishing theorems and conjectures for the $\ell^2$-homology of right-angled Coxeter groups.* Geometry & Topology **5** (2001), 7–74.
- **[Key]** Ś. R. Gal. *Real root conjecture fails for five- and higher-dimensional spheres.* Discrete & Computational Geometry **34** (2005), 269–284. [DOI](https://doi.org/10.1007/s00454-005-1171-5)
- **[Key]** K. Karu. *The cd-index of fans and posets.* Compositio Mathematica **142** (2006), 701–718. [DOI](https://doi.org/10.1112/s0010437x06001928)
- **[Key]** N. C. Leung, V. Reiner. *The signature of a toric variety.* Duke Mathematical Journal **111** (2002), 253–286. [DOI](https://doi.org/10.1215/s0012-7094-02-11123-5)
- **[Survey]** R. P. Stanley. *Positivity problems and conjectures in algebraic combinatorics.* In *Mathematics: Frontiers and Perspectives*, American Mathematical Society, 2000, 295–319.
- **[Reference]** M. W. Davis. *The Geometry and Topology of Coxeter Groups.* London Mathematical Society Monographs 32, Princeton University Press, 2008.
- **[SOTA / Recent]** E. Nevo, T. K. Petersen. *On $\gamma$-vectors satisfying the Kruskal–Katona bounds.* Discrete & Computational Geometry **45** (2011), 503–521.
- **[SOTA / Recent]** E. Nevo, T. K. Petersen, B. E. Tenner. *The $\gamma$-vector of a barycentric subdivision.* Journal of Combinatorial Theory Series A **118** (2011), 1364–1380. [DOI](https://doi.org/10.1016/j.jcta.2011.01.001)
- **[Related]** P. Brändén. *Sign-graded posets, unimodality of $W$-polynomials and the Charney–Davis conjecture.* Electronic Journal of Combinatorics **11**(2) (2004), #R9. [DOI](https://doi.org/10.37236/1866)
- **[Related]** V. Reiner, V. Welker. *On the Charney–Davis and Neggers–Stanley conjectures.* Journal of Combinatorial Theory Series A **109** (2005), 247–280. [DOI](https://doi.org/10.1016/j.jcta.2004.09.003)
- **[Related]** A. Frohmader. *Face vectors of flag complexes.* Israel Journal of Mathematics **164** (2008), 153–164. [DOI](https://doi.org/10.1007/s11856-008-0024-3)
- **[Related]** N. Aisbett. *Frankl–Füredi–Kalai inequalities on the $\gamma$-vectors of flag nestohedra.* Discrete & Computational Geometry **51** (2014), 323–336. [DOI](https://doi.org/10.1007/s00454-013-9567-0)
- **[Related]** A. Postnikov, V. Reiner, L. Williams. *Faces of generalized permutohedra.* Documenta Mathematica **13** (2008), 207–273. [DOI](https://doi.org/10.4171/dm/248)

## 10. Worked Example / Concrete Special Case

**Step 1: the case $e=1$ (flag circles).** A flag triangulation of $S^1$ is an $n$-cycle $C_n$ with $n \ge 4$ (a triangle $C_3$ is not flag as a sphere — it bounds a 2-face). Here $d=2$, $f_{-1}=1$, $f_0=f_1=n$:

$$h_{C_n}(t) = (1-t)^2 + n\,t(1-t) + n\,t^2 = 1 + (n-2)t + t^2 .$$

So $h(-1) = 1-(n-2)+1 = 4-n$ and $(-1)^1 h(-1) = n-4 \ge 0$. Equality holds exactly for $C_4 = S^0 * S^0$, the boundary of the square (2-dimensional cross-polytope). In $\gamma$-form, $h_{C_n}(t) = (1+t)^2 + (n-4)t$, so $\gamma_1 = n-4$.

Check against $\kappa$ for $C_5$: $\kappa = 1 - \tfrac{5}{2} + 5\cdot\tfrac14 = -\tfrac14$, and $2^2\kappa = -1 = h(-1)$. ✔

**Step 2: a flag 3-sphere, $e=2$.** Take $L = C_5 * C_5$, the simplicial join of two pentagons — a flag triangulation of $S^3$ with $10$ vertices, $25 + 5 + 5 = 35$ edges, $25+25=50$ triangles, $25$ tetrahedra. Joins multiply $h$-polynomials:

$$h_L(t) = \big(1+3t+t^2\big)^2 = 1 + 6t + 11t^2 + 6t^3 + t^4 .$$

Then $h_L(-1) = 1-6+11-6+1 = 1$, and $(-1)^2 h_L(-1) = 1 \ge 0$. ✔ In $\gamma$-form, $\gamma_{C_5}(t)=1+t$, so $\gamma_L(t) = (1+t)^2 = 1+2t+t^2$: $\gamma_0=1$, $\gamma_1 = 10-8 = 2$, $\gamma_2 = 1 = (-1)^2h_L(-1)$. ✔

**Step 3: why the flag hypothesis is needed.** Drop flagness: the boundary of the $4$-simplex, $\partial\Delta^4$, triangulates $S^3$ with $h(t)=1+t+t^2+t^3+t^4$, so $h(-1)=1$ — fine here. But the cyclic $4$-polytope $C(8,4)$ has $h=(1,4,10,4,1)$ giving $h(-1)=1-4+10-4+1=4>0$, while suitable non-flag spheres in dimension 3 can be built with $h(-1)<0$; only the flag condition, which forces $f_0\ge 2d$ and suppresses "large" middle $h_i$ relative to the outer ones, makes the sign uniform. The interpretation via curvature: at each vertex of a cubical $4$-manifold with all links flag $S^3$, the local Gauss–Bonnet contribution is $\kappa(\mathrm{Lk}(v)) = h(-1)/16$; for links $C_5 * C_5$ this is $1/16>0$, and summing over vertices gives $\chi(M^4)>0$ as Hopf predicts.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*