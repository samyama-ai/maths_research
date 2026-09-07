---
id: 02-algebra-group-theory/iarrobinos-conjecture
title: "Iarrobino's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Iarrobino's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/iarrobinos-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be an algebraically closed field of characteristic $0$, $R = k[x_1,\dots,x_n]$ with the standard grading, and let $\ell_1,\dots,\ell_r \in R_1$ be **general** linear forms. Fix exponents $a_1,\dots,a_r \ge 2$ and set

$$I = (\ell_1^{a_1},\dots,\ell_r^{a_r}) \subset R .$$

**Question.** What is the Hilbert function $t \mapsto \dim_k [R/I]_t$?

Fröberg's conjecture predicts, for $r$ *general forms* of degrees $a_i$, the series obtained by truncating

$$\mathrm{HS}(R/I;z) \;=\; \left[\frac{\prod_{i=1}^{r}(1-z^{a_i})}{(1-z)^n}\right]_{+},$$

where $[\,\sum c_t z^t\,]_+$ replaces all coefficients from the first non-positive one onward by $0$. Powers of linear forms are *not* general forms: they lie on the $r$-th secant variety of the Veronese, and Iarrobino observed that the Fröberg value is systematically violated in a controlled way.

**Iarrobino's Conjecture (1997).** For general $\ell_i$ and $n \ge 3$, the Hilbert function of $R/(\ell_1^{a_1},\dots,\ell_r^{a_r})$ equals the Fröberg value in every degree $t$, **except** for an explicitly described exceptional locus of parameters $(n; a_1,\dots,a_r; t)$ coming from the degenerate geometry of $r$ general points in $\mathbb{P}^{n-1}$ (points on a hyperplane, a rational normal curve, a quadric, …); in those degrees the true dimension exceeds the Fröberg value by an explicit correction term supplied by that geometry. In particular, in the **uniform case** $a_1=\dots=a_r=j$ the conjecture asserts

$$\dim_k [R/I]_t \;=\; \max\left\{0,\ \sum_{i \ge 0} (-1)^i \binom{r}{i}\binom{n-1+t-ij}{\,n-1\,}\right\}$$

for all $(n,j,r,t)$ outside Iarrobino's exceptional list, and gives the exact defect on the list.

A complete resolution means: a proof of the formula off the exceptional list together with a proof that the list is complete, or a counterexample exhibiting a defect that Iarrobino's correction does not account for.

## 2. Mathematical Foundations

**Macaulay inverse systems.** Let $S = k[X_1,\dots,X_n]$ be the divided-power/dual polynomial ring, with $R$ acting on $S$ by contraction, $x_i \circ X^\alpha = X^{\alpha - e_i}$. For a homogeneous ideal $I\subset R$, the inverse system $I^{-1}\subset S$ is the annihilator, and $\dim_k [R/I]_t = \dim_k [I^{-1}]_t$.

**Emsalem–Iarrobino duality.** Let $\ell_i = \sum_j c_{ij}x_j$ correspond to the point $p_i = [c_{i1}:\dots:c_{in}] \in \mathbb{P}^{n-1}$ with homogeneous prime $\wp_i$. Then for $t \ge a_i$ for all $i$,

$$\dim_k \big[\,R/(\ell_1^{a_1+1},\dots,\ell_r^{a_r+1})\,\big]_t \;=\; \dim_k \big[\,\wp_1^{\,t-a_1} \cap \cdots \cap \wp_r^{\,t-a_r}\,\big]_t .$$

So computing Hilbert functions of power ideals is *equivalent* to computing the dimension of the linear system of degree-$t$ hypersurfaces in $\mathbb{P}^{n-1}$ with prescribed multiplicities $t-a_i$ at $r$ general points — the **fat point interpolation problem**.

**Expected dimension.** For $Z = \sum_i m_i p_i$ the naive count is

$$\operatorname{expdim}[\mathcal{I}_Z]_t = \max\left\{0,\ \binom{n-1+t}{n-1} - \sum_{i=1}^r \binom{n-2+m_i}{n-1}\right\},$$

and $\dim \ge \operatorname{expdim}$ always. A system is **special** when the inequality is strict; Iarrobino's conjecture is exactly a prediction of which power ideals are special and by how much.

**Lefschetz properties.** $A = R/I$ Artinian has the **weak Lefschetz property** (WLP) if for general $\ell$ the map $\times \ell: A_t \to A_{t+1}$ has maximal rank for all $t$, and the **strong Lefschetz property** (SLP) if $\times \ell^s$ has maximal rank for all $s,t$. WLP/SLP statements for $R/(\ell_1^j,\dots,\ell_{r}^j)$ are equivalent to instances of the conjecture, since adjoining one more general power is multiplication by $\ell^j$.

## 3. History & State of the Art (SOTA)

- **1978–1985.** Stanley computes Hilbert functions of monomial complete intersections via the hard Lefschetz theorem; Fröberg (1985) formulates the expected Hilbert series for ideals of general forms.
- **1986.** Anick proves Fröberg's conjecture for $n = 3$ (any degrees, general forms).
- **1995.** Emsalem–Iarrobino publish the inverse-system duality above (*Inverse system of a symbolic power I*), transporting power ideals into fat-point geometry. Alexander and Hirschowitz complete the classification of special systems with all $m_i = 2$ (polynomial interpolation with double points), the exceptional cases being $t=2$; $(n-1,t,r) = (2,4,5)$, $(3,4,9)$, $(4,3,7)$, $(4,4,14)$ in $\mathbb{P}^{n-1}$.
- **1997.** Iarrobino, *Inverse system of a symbolic power III: thin algebras and fat points* (Compositio Math. 108, 319–356), states the conjecture, computes the exceptional corrections, and shows that "thin algebras" $R/I$ deviate from Fröberg exactly where the point configuration is degenerate.
- **2000s.** Migliore–Miró-Roig study ideals of general forms and the ubiquity of WLP; Chandler gives short proofs in the double-point case and a geometric re-reading of the Fröberg–Iarrobino package.
- **2010–2013.** Schenck–Seceleanu prove that **every** ideal generated by powers of linear forms in $k[x,y,z]$ gives an algebra with WLP; Harbourne–Schenck–Seceleanu and Migliore–Miró-Roig–Nagel push into $n = 4$ using Gelfand–Tsetlin patterns and monomial-ideal techniques.
- **Present.** No counterexample to Iarrobino's prediction is known; the conjecture is open for $n \ge 3$ in general, and for $n = 3$ it is essentially equivalent to the (still open) Segre–Harbourne–Gimigliano–Hirschowitz conjecture restricted to uniform multiplicities.

## 4. Partial Results / Verified Cases

- **$n \le 2$.** Complete. In $k[x,y]$ any $r$ powers of distinct linear forms have Hilbert function determined by the two smallest exponents; no exceptions occur.
- **$r \le n$.** The $\ell_i$ are linearly independent, so after a change of coordinates $I = (x_1^{a_1},\dots,x_r^{a_r})$ is a complete intersection and the Fröberg series is exact (no truncation needed).
- **$r = n+1$, uniform powers.** $R/(\ell_1^j,\dots,\ell_{n+1}^j) \cong \big(k[x_1,\dots,x_n]/(x_1^j,\dots,x_n^j)\big)/(\ell^j)$; the Stanley–Watanabe theorem (monomial complete intersections have SLP in characteristic $0$) gives the conjectured Hilbert function for all $j$ and all $n$.
- **$a_i = 2$ for all $i$ (squares).** Equivalent by duality to double-point interpolation; settled by Alexander–Hirschowitz (1995), with a shorter proof by Chandler (2001). The four sporadic exceptions match Iarrobino's correction.
- **$n = 3$, arbitrary powers.** $R/(\ell_1^{a_1},\dots,\ell_r^{a_r})$ always has WLP (Schenck–Seceleanu 2010), which pins the Hilbert function in a range of degrees. Uniform-multiplicity planar systems are known for $r \le 9$ general points (Nagata/Harbourne, via $(-1)$-curves and Cremona reduction), for multiplicity $m \le 12$ and any $r$ (Ciliberto–Miranda), and for $r = 4^k$ points (Evain) — each yielding an infinite verified family of the conjecture.
- **$n = 4$.** Extensive families with $r = 5,6,7$ uniform powers are verified (Migliore–Miró-Roig–Nagel, *Algebra & Number Theory* 6 (2012); Harbourne–Schenck–Seceleanu, *JLMS* 84 (2011)), including all $j$ for $r=5$.
- **Computation.** Macaulay2/Singular verifications cover essentially all $(n,j,r,t)$ with $n \le 6$ and $t$ up to roughly $30$; no discrepancy with Iarrobino's prediction has been reported.

## 5. Principal Obstacles

- **Semicontinuity has the wrong direction.** Specializing the $\ell_i$ can only make $\dim[R/I]_t$ larger, so degenerations give *lower* bounds on the ideal only in the degrees where the specialization is already known to be non-special. Producing the matching upper bound needs an explicit surjectivity, which the standard Horace/differential Horace induction supplies only when the residual system is again non-special — precisely what is being proven.
- **Non-genericity of powers.** Fröberg-type arguments treat forms as generic points of $\mathbb{P}(R_j)$. Powers $\ell^j$ occupy the $j$-th Veronese, a subvariety of dimension $n-1$ inside $\binom{n-1+j}{n-1}-1$, so no dimension count on the space of forms transfers.
- **Failure of Lefschetz machinery beyond $n=3$.** The proofs in three variables use the fact that syzygy bundles on $\mathbb{P}^2$ are governed by Grauert–Mülich and by the classification of rank-2 bundles. In $\mathbb{P}^3$ and higher, the associated syzygy bundle can be unstable in ways not controlled by any known splitting criterion, and WLP genuinely fails for some monomial almost complete intersections.
- **Special systems are not classified.** In $\mathbb{P}^2$ the SHGH conjecture asserts every special system is special because of $(-1)$-curves; this is open, and in $\mathbb{P}^{n-1}$, $n \ge 4$, there is not even a conjectural list of the geometric causes of speciality. Iarrobino's exceptional list is therefore not known to be exhaustive.
- **Characteristic.** In characteristic $p$ even the $r=n+1$ uniform case fails (monomial complete intersections lose SLP), so no proof can be characteristic-free.

## 6. The Gap

Proven: the conjecture in $n \le 2$; for $r \le n+1$; for all exponents equal to $2$; and in scattered infinite families for $n = 3,4$ where fat-point geometry is under control. Conjectured: the same statement for all $(n,j,r)$ with $n \ge 3$, $j \ge 3$, $r \ge n+2$.

The exact barrier is a single implication:

> For $r \ge n+2$ general points in $\mathbb{P}^{n-1}$ and uniform multiplicity $m = t-j+1$, the linear system $[\mathcal{I}_Z]_t$ has the expected dimension unless the points impose dependent conditions for one of Iarrobino's listed geometric reasons.

No technique currently produces the *non-existence* of unexpected hypersurfaces for unbounded $m$ and unbounded $r$ simultaneously. Every known method fixes one parameter (multiplicity $\le 12$, or $r \le 9$, or $m = 2$) and inducts on the other.

## 7. Current Research (as of June 2026)

- **Lefschetz-property school** (Migliore, Miró-Roig, Nagel, Schenck, Seceleanu, Harbourne; Notre Dame, Barcelona, Kentucky, Auburn, Nebraska): translating power-ideal Hilbert functions into WLP/SLP statements for monomial almost complete intersections, then into lattice-path and Gelfand–Tsetlin enumeration.
- **Unexpected hypersurfaces** (Cook–Harbourne–Migliore–Nagel and successors): the discovery of "unexpected curves" attached to line arrangements gives a new *source* of exceptional behaviour for power ideals, and the question of whether any such example evades Iarrobino's correction is actively pursued. *(frontier — verify)*
- **Degeneration and tropical methods** for planar systems (Ciliberto–Miranda school, Evain, Dumnicki): extending uniform-multiplicity results past $m = 12$. Recent computational–degeneration hybrids claim uniform multiplicity up to the high teens for all $r$. *(frontier — verify)*
- **Apolarity and secant varieties** (Ottaviani, Bernardi, Oneto): identifiability and rank questions on Veronese varieties feed directly into the dimensions of $[R/I]_t$.
- **Positive characteristic**: systematic tabulation of where the characteristic-$0$ formula fails, via Frobenius powers and Han's theorem on the Hilbert function of $k[x,y,z]/(x^j,y^j,z^j,\ell^j)$.

## 8. Future Work

- Prove the uniform case for $n = 3$ and all $j$, by settling SHGH for equal multiplicities — the most concrete route, since Cremona action on $\mathbb{P}^2$ is fully understood.
- Establish an "asymptotic Iarrobino": show that for fixed $n$ and $r$, the conjectured formula holds for all $j \gg 0$. Nagata-type bounds already give partial asymptotics.
- Find a bundle-theoretic proof: identify the syzygy bundle of $(\ell_1^j,\dots,\ell_r^j)$ and prove semistability, which would give maximal-rank multiplication maps directly.
- Classify unexpected hypersurfaces in $\mathbb{P}^3$ for general points; either extend Iarrobino's list or produce the first counterexample.
- Develop a characteristic-$p$ analogue with an explicit dependence on $p$, $j$, $r$.

## 9. Key References

- **[Foundational]** A. Iarrobino. *Inverse system of a symbolic power III: thin algebras and fat points.* Compositio Mathematica 108 (1997), 319–356.
- **[Foundational]** J. Emsalem, A. Iarrobino. *Inverse system of a symbolic power I.* Journal of Algebra 174 (1995), 1080–1090.
- **[Foundational]** R. Fröberg. *An inequality for Hilbert series of graded algebras.* Mathematica Scandinavica 56 (1985), 117–144.
- **[Foundational]** D. Anick. *Thin algebras of embedding dimension three.* Journal of Algebra 100 (1986), 235–259.
- **[Foundational]** J. Alexander, A. Hirschowitz. *Polynomial interpolation in several variables.* Journal of Algebraic Geometry 4 (1995), 201–222.
- **[Foundational]** R. Stanley. *Weyl groups, the hard Lefschetz theorem, and the Sperner property.* SIAM Journal on Algebraic and Discrete Methods 1 (1980), 168–184.
- **[Foundational]** J. Watanabe. *The Dilworth number of Artinian rings and finite posets with rank function.* Advanced Studies in Pure Mathematics 11 (1987), 303–312.
- **[SOTA / Recent]** H. Schenck, A. Seceleanu. *The weak Lefschetz property and powers of linear forms in $\mathbb{K}[x,y,z]$.* Proceedings of the AMS 138 (2010), 2335–2339.
- **[SOTA / Recent]** B. Harbourne, H. Schenck, A. Seceleanu. *Inverse systems, Gelfand–Tsetlin patterns and the weak Lefschetz property.* Journal of the London Mathematical Society 84 (2011), 712–730.
- **[SOTA / Recent]** J. Migliore, R. Miró-Roig, U. Nagel. *On the weak Lefschetz property for powers of linear forms.* Algebra & Number Theory 6 (2012), 487–526.
- **[SOTA / Recent]** C. Ciliberto, R. Miranda. *Linear systems of plane curves with base points of equal multiplicity.* Transactions of the AMS 352 (2000), 4037–4050.
- **[SOTA / Recent]** K. Chandler. *A brief proof of a maximal rank theorem for generic double points in projective space.* Transactions of the AMS 353 (2001), 1907–1920.
- **[Survey]** J. Migliore, U. Nagel. *Survey article: a tour of the weak and strong Lefschetz properties.* Journal of Commutative Algebra 5 (2013), 329–358.
- **[Survey]** T. Harima, T. Maeno, H. Morita, Y. Numata, A. Wachi, J. Watanabe. *The Lefschetz Properties.* Springer Lecture Notes in Mathematics 2080, 2013.

## 10. Worked Example / Concrete Special Case

Take $n = 3$, $R = k[x,y,z]$, five general linear forms $\ell_1,\dots,\ell_5$, uniform exponent $j = 3$:

$$I = (\ell_1^3,\ \ell_2^3,\ \ell_3^3,\ \ell_4^3,\ \ell_5^3).$$

**Fröberg prediction.** $\dfrac{(1-z^3)^5}{(1-z)^3} = (1-z)^2(1+z+z^2)^5$, whose coefficients are $1,\,3,\,6,\,5,\,0,\,-9,\dots$ — truncating gives the expected Hilbert function $(1,3,6,5,0,0,\dots)$.

**Actual value in degree 4.** Apply Emsalem–Iarrobino duality with $a_i + 1 = 3$, i.e. $a_i = 2$, and $t = 4$, so the multiplicities are $m_i = t - a_i = 2$:

$$\dim_k [R/I]_4 \;=\; \dim_k \big[\wp_1^2 \cap \wp_2^2 \cap \wp_3^2 \cap \wp_4^2 \cap \wp_5^2\big]_4 ,$$

the space of plane quartics singular at $5$ general points of $\mathbb{P}^2$. Naive count: $\dim R_4 = \binom{6}{2} = 15$ conditions available, $5 \times 3 = 15$ conditions imposed, so expected dimension $0$ — matching Fröberg. But five general points in $\mathbb{P}^2$ lie on a **unique smooth conic** $Q$, and $Q^2$ is a quartic that is singular at every point of $Q$, in particular at all five points. Hence

$$\dim_k [R/I]_4 = 1 > 0 .$$

The true Hilbert function is $(1,3,6,5,\mathbf{1},0,0,\dots)$: the Fröberg value fails in exactly one degree, by exactly $1$.

**Checks in the neighbouring degrees.**
- $t = 3$: multiplicities $m_i = 1$, cubics through $5$ general points, $\dim = 10 - 5 = 5$. Fröberg gives $\binom{5}{2} - 5\binom{2}{2} = 10 - 5 = 5$. ✓
- $t = 5$: multiplicities $m_i = 3$; a quintic with five triple points would meet the conic $Q$ in $\ge 15 > 2\cdot 5$ points, so it contains $Q$, and the residual cubic must have five double points — impossible. Dimension $0$, matching Fröberg's $21 - 30 = -9 \mapsto 0$. ✓

This single defect is exactly the $(\mathbb{P}^2, t=4, r=5)$ entry of the Alexander–Hirschowitz exceptional list, and it is the prototype of Iarrobino's correction term: the deviation from Fröberg is produced by a hypersurface (here the double conic) forced on the configuration by the geometry of $r$ general points. The conjecture asserts that *every* deviation, in every $n$, $j$, $r$, has such an explanation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*