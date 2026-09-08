---
id: 04-topology/strong-slope-conjecture
title: "Strong Slope Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Strong Slope Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/strong-slope-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $J_{K,n}(q)$ be its colored Jones polynomial. The degrees of $J_{K,n}$ grow like a quadratic quasi-polynomial in $n$. The **Slope Conjecture** (Garoufalidis, 2011) asserts that the quadratic growth rates ("Jones slopes") are boundary slopes of essential surfaces in the knot exterior $E_K = S^3 \setminus \nu(K)$. The **Strong Slope Conjecture** (Kalfagianni–Tran, 2015) asserts more: the *linear* term of the degree also has topological meaning, namely it computes the normalized Euler characteristic $\chi(S)/|\partial S|$ of a surface realizing that slope.

**Conjecture (Strong Slope Conjecture).** For every knot $K \subset S^3$ and every cluster point $4a$ of the quadratic growth rates of $\max\deg_q$ of the colored Jones polynomials, with $b$ the associated linear coefficient (normalization fixed in §2), there is an essential surface $S \subset E_K$ with
$$\text{boundary slope}(S) = 4a, \qquad \frac{\chi(S)}{|\partial S|} = 2b .$$
The same holds for $\min\deg_q$ with the corresponding coefficients $(a^\ast,b^\ast)$. A surface realizing both equalities is called a **Jones surface** for $K$.

A complete proof must produce, for an arbitrary knot, essential surfaces matched to quantum-invariant degree data; a disproof requires a knot whose full list of boundary slopes (or of $(\text{slope},\chi/|\partial|)$ pairs) omits the Jones data. The Strong Slope Conjecture implies the Slope Conjecture.

## 2. Mathematical Foundations

**Colored Jones polynomials.** For $n \ge 1$ let $J_{K,n}(q) \in \mathbb{Z}[q^{\pm1}]$ be the invariant colored by the $n$-dimensional irreducible $\mathfrak{sl}_2$-representation, normalized by $J_{\text{unknot},n} = 1$; $J_{K,2}$ is the Jones polynomial. Let
$$\widetilde J_{K,n}(q) = [n]\, J_{K,n}(q), \qquad [n] = \frac{q^{n/2}-q^{-n/2}}{q^{1/2}-q^{-1/2}},$$
be the unreduced invariant, and set $d_K[n] = \max\deg_q \widetilde J_{K,n} \in \tfrac12\mathbb{Z}$, $d^\ast_K[n] = \min\deg_q \widetilde J_{K,n}$. (Sources differ by this $\tfrac{n-1}{2}$ shift and by indexing colors $n$ vs. $n+1$; the shift is exactly what makes the constant $2$ below correct.)

**Quasi-polynomiality.** Garoufalidis proved that the degree of any $q$-holonomic sequence is eventually a quadratic quasi-polynomial. Since $(J_{K,n})_n$ is $q$-holonomic (Garoufalidis–Lê), there are $p \in \mathbb{N}$ and periodic functions $a,b,c$ of period $p$ with
$$d_K[n] = a(n)\,n^2 + b(n)\,n + c(n) \qquad (n \gg 0).$$

**Jones slopes.** $js_K := \{\,4a(n) : n \gg 0\,\}$, equivalently the set of cluster points of $4\,d_K[n]/n^2$. Likewise $jx_K := \{2b(n)\}$.

**Boundary slopes.** A properly embedded surface $S \subset E_K$ (orientable or not) is *essential* if it is incompressible and $\partial$-incompressible. Its boundary consists of parallel essential curves on $\partial E_K \cong T^2$; in the meridian–longitude basis $(\mu,\lambda)$ each is homologous to $p\mu + q\lambda$, and $p/q \in \mathbb{Q}\cup\{\infty\}$ is the **boundary slope**. Let $bs_K$ be the set of boundary slopes. By Hatcher's theorem, $bs_K$ is finite, and all slopes are even integers when $S$ is orientable.

**Slope Conjecture.** $js_K \subseteq bs_K$ and $js_{K} \cup js_{K^\ast}$-data covers both extremal degrees.

**Strong Slope Conjecture.** For each $n \gg 0$ there is an essential $S \subset E_K$ with boundary slope $4a(n)$ and $\chi(S)/|\partial S| = 2b(n)$; symmetrically for $(a^\ast,b^\ast)$. Note $d^\ast_K[n] = -d_{K^\ast}[n]$ for the mirror $K^\ast$, so the two halves are equivalent.

## 3. History & State of the Art (SOTA)

- **2011.** Garoufalidis, *The Jones slopes of a knot* (Quantum Topology 2), introduces Jones slopes and the Slope Conjecture, verifies it for alternating knots, torus knots, and all knots with at most $9$ crossings, using Hatcher–Oertel boundary slopes of Montesinos knots.
- **2011.** Garoufalidis, *The degree of a $q$-holonomic sequence is a quadratic quasi-polynomial*, supplies the structural input making the statement well-posed.
- **2013.** Futer–Kalfagianni–Purcell, *Guts of Surfaces and the Colored Jones Polynomial*, expresses extremal degrees for adequate links via state surfaces, giving the model case in which the linear term already equals $\chi/|\partial|$ of an essential spanning surface.
- **2015.** Kalfagianni–Tran, *Knot cabling and the degree of the colored Jones polynomial* (New York J. Math. 21), formulates the Strong Slope Conjecture and proves it is preserved under cabling for knots satisfying a positivity condition.
- **2016–2018.** Explicit families: Lee–van der Veen (pretzel knots), Garoufalidis–van der Veen (2-fusion knots via quadratic integer programming), Motegi–Takata (graph knots), Garoufalidis–Lee–van der Veen (Montesinos knots).
- **2020.** Baker–Motegi–Takata prove the Strong Slope Conjecture for twisted generalized Whitehead doubles of a large class of knots, producing satellite examples whose Jones surfaces are not spanning surfaces.

No counterexample is known. The obstruction to a general proof is structural, not numerical.

## 4. Partial Results / Verified Cases

- **Adequate knots** (including all alternating knots and all Montesinos knots with adequate diagrams): proved. For an $A$-adequate diagram $D$ with $c_-$ negative crossings, $4a^\ast = -2c_-$ and the all-$A$ state surface $S_A$ is essential (Ozawa), with $\chi(S_A)/|\partial S_A| = 2b^\ast$. Dually for $B$-adequate diagrams and $4a = 2c_+$.
- **Torus knots** $T(p,q)$, $p,q>0$: $js = \{pq\}$, $jx = \{0\}$; the Jones surface is the cabling annulus, $\chi = 0$, $|\partial S| = 2$.
- **Iterated cables and iterated torus knots**: Kalfagianni–Tran show that if $K$ satisfies the Strong Slope Conjecture with a suitable sign condition on $b$, then every $(p,q)$-cable of $K$ does; hence all iterated cables of adequate knots and of torus knots.
- **Graph knots** (knots in the JSJ-graph-manifold class, i.e. built from torus knots by cabling and connected sum): Motegi–Takata.
- **3-string pretzel knots** $P(a,b,c)$ in explicit ranges of $(a,b,c)$, and Montesinos knots: Lee–van der Veen; Garoufalidis–Lee–van der Veen.
- **2-fusion knots** $K(m_1,m_2)$: an infinite two-parameter family of mostly hyperbolic, non-alternating knots, verified by Garoufalidis–van der Veen with quasi-polynomial periods up to $2$.
- **Twisted generalized Whitehead doubles** of knots satisfying the conjecture, under explicit twisting hypotheses: Baker–Motegi–Takata.
- **Census verification**: all knots with $\le 9$ crossings (Garoufalidis, 2011); tabulated alternating knots to much higher crossing number follow from the adequate case.

## 5. Principal Obstacles

- **No mechanism converts skein data into surfaces.** Extremal degrees are computed from state sums, $R$-matrices, or the $q$-holonomic recursion; essential surfaces come from normal surface theory and hierarchies. There is no functor, exact sequence, or index theorem linking them. In every proved case the link is a *coincidence of formulas*: a diagram whose state surface happens to be essential.
- **Adequacy fails generically.** For adequate knots the top/bottom degrees are given by a single state with no cancellation. For non-adequate knots the extremal terms cancel unpredictably, so the degree is not read off any one surface.
- **Nontrivial quasi-periods.** When the period $p > 1$, distinct residues $n \bmod p$ give *different* slopes and different $b$-values, so a single surface cannot serve; one must produce a matched family, and no construction does this from quantum data.
- **Boundary slopes are hard to compute.** Outside Montesinos knots (Hatcher–Oertel algorithm) there is no practical enumeration of $bs_K$; normal-surface enumeration is exponential and does not directly output $\chi/|\partial|$ for all essential surfaces.
- **The A-polynomial route is blocked.** The AJ conjecture would relate the recursion to the A-polynomial, whose Newton-polygon slopes are boundary slopes (Culler–Shalen theory). But AJ is itself open, it concerns the character variety rather than embedded surfaces, and it says nothing about the linear coefficient $b$.
- **Non-orientable and satellite phenomena.** Jones surfaces may be non-orientable (once-punctured Klein bottles) or have several boundary components; standard Seifert-surface / Thurston-norm technology, which is tuned to orientable surfaces, does not apply.

## 6. The Gap

Proved: for knots with a diagram whose extremal Kauffman states are cancellation-free (adequate), and for knots built from such by cabling/doubling operations whose effect on degrees is governed by an explicit cabling formula, both the quadratic and linear coefficients match an explicit surface.

Conjectured: the same for an arbitrary knot, in particular for hyperbolic non-adequate knots with quasi-period $p > 1$ and no distinguished diagram.

The exact missing step: given only the degree quasi-polynomial $a(n)n^2 + b(n)n + c(n)$ — data extracted from a linear $q$-difference equation — **construct** an essential surface with prescribed slope $4a(n)$ and prescribed $\chi/|\partial| = 2b(n)$. Every current proof runs in the opposite direction (surface first, degree second), and no argument shows the set of realizable pairs $(\text{slope}, \chi/|\partial|)$ must contain the Jones data.

## 7. Current Research (as of June 2026)

- **Michigan State (Kalfagianni and collaborators):** consequences of the conjecture rather than the conjecture itself — Jones-slope diameter bounds on crossing number, and characterizations of adequacy by extremal degree data (Kalfagianni, *A Jones slopes characterization of adequate knots*, Indiana Univ. Math. J., 2018).
- **Nihon University / Kyushu (Motegi, Takata) with Baker:** closure properties — showing the class of knots satisfying the Strong Slope Conjecture is stable under cabling, twisting, and Whitehead doubling, thereby enlarging it from graph knots toward general satellites. *(frontier — verify)* Extensions to Seifert-fibered and general satellite patterns are in circulation.
- **Garoufalidis, van der Veen, Lee:** algorithmic verification — writing $\max\deg$ as the optimum of a parametrized quadratic integer program derived from a state sum, then certifying agreement with Hatcher–Oertel slope data. This scales to infinite families but not to all knots.
- **Quantum-topology/AJ interface:** attempts to derive slope statements from the Newton polygon of the recursion polynomial, and from the "degree of the $\hat{A}$-polynomial". *(frontier — verify)*
- **Machine search:** large-scale checks against SnapPy/Regina normal-surface data for hyperbolic census knots. No counterexample reported.

## 8. Future Work

- Prove the conjecture for all **Montesinos knots** uniformly, where both sides are algorithmically computable, as a template for a general argument.
- Find a **surface-producing construction** from the $q$-difference equation: e.g. interpret the extremal-degree optimization as a normal-surface optimization (a "quantum normal surface" theory), so that the optimizer is a surface, not a number.
- Settle whether $jx_K$ is always realized by a surface of **minimal** $|\chi|$ among those of the given slope; this would tie the conjecture to the Thurston norm and to guts decompositions.
- Understand knots with **quasi-period $p>1$**: describe the family of surfaces indexed by $n \bmod p$ intrinsically.
- Test the conjecture on knots with few boundary slopes but complicated colored Jones behaviour (e.g. hyperbolic knots with small Culler–Shalen norm) as the likeliest source of a counterexample.

## 9. Key References

- **[Foundational]** S. Garoufalidis. *The Jones slopes of a knot.* Quantum Topology 2 (2011), 43–69. [DOI](https://doi.org/10.4171/qt/13)
- **[Foundational]** S. Garoufalidis. *The degree of a $q$-holonomic sequence is a quadratic quasi-polynomial.* Electronic Journal of Combinatorics 18(2) (2011), \#P4. [DOI](https://doi.org/10.37236/2000)
- **[Foundational]** E. Kalfagianni, A. T. Tran. *Knot cabling and the degree of the colored Jones polynomial.* New York Journal of Mathematics 21 (2015).
- **[Foundational]** A. Hatcher. *On the boundary curves of incompressible surfaces.* Pacific Journal of Mathematics 99 (1982), 373–377. [DOI](https://doi.org/10.2140/pjm.1982.99.373)
- **[Foundational]** A. Hatcher, U. Oertel. *Boundary slopes for Montesinos knots.* Topology 28 (1989), 453–480. [DOI](https://doi.org/10.1016/0040-9383(89)90005-0)
- **[Survey]** D. Futer, E. Kalfagianni, J. Purcell. *Guts of Surfaces and the Colored Jones Polynomial.* Lecture Notes in Mathematics 2069, Springer, 2013. [DOI](https://doi.org/10.1007/978-3-642-33302-6)
- **[SOTA / Recent]** C. R. S. Lee, R. van der Veen. *Slopes for pretzel knots.* New York Journal of Mathematics 22 (2016).
- **[SOTA / Recent]** S. Garoufalidis, R. van der Veen. *Quadratic integer programming and the slope conjecture.* New York Journal of Mathematics 22 (2016).
- **[SOTA / Recent]** K. Motegi, T. Takata. *The slope conjecture for graph knots.* Mathematical Proceedings of the Cambridge Philosophical Society 162 (2017), 383–392. [DOI](https://doi.org/10.1017/s0305004116000566)
- **[SOTA / Recent]** K. L. Baker, K. Motegi, T. Takata. *The strong slope conjecture for twisted generalized Whitehead doubles.* Quantum Topology 11 (2020). [DOI](https://doi.org/10.4171/qt/242)
- **[SOTA / Recent]** E. Kalfagianni. *A Jones slopes characterization of adequate knots.* Indiana University Mathematics Journal 67 (2018). [DOI](https://doi.org/10.1512/iumj.2018.67.6285)
- **[Supporting]** M. Ozawa. *Essential state surfaces for knots and links.* Journal of the Australian Mathematical Society 91 (2011), 391–404. [DOI](https://doi.org/10.1017/s1446788712000055)
- **[Supporting]** S. Garoufalidis, T. T. Q. Lê. *The colored Jones function is $q$-holonomic.* Geometry & Topology 9 (2005), 1253–1293. [DOI](https://doi.org/10.2140/gt.2005.9.1253)

## 10. Worked Example / Concrete Special Case

**The figure-eight knot $4_1$.** Habiro's cyclotomic formula gives, with $J_{4_1,1}=1$,
$$J_{4_1,n}(q) \;=\; \sum_{k=0}^{n-1}\ \prod_{j=1}^{k}\left(q^{n}+q^{-n}-q^{j}-q^{-j}\right).$$
Check at $n=2$: $1 + (q^2+q^{-2}-q-q^{-1}) = q^{2}-q+1-q^{-1}+q^{-2}$, the Jones polynomial of $4_1$. ✓

*Degree.* The $k$-th summand has top term $q^{kn}$ (since $j \le k \le n-1 < n$, no other factor contributes degree $\ge n$ per bracket). The maximum over $k$ is at $k=n-1$, giving a unique leading monomial $q^{n(n-1)}$ with coefficient $1$ — no cancellation. Hence
$$\max\deg_q J_{4_1,n} = n^2-n, \qquad \max\deg_q \widetilde J_{4_1,n} = n^2 - n + \tfrac{n-1}{2} = n^2 - \tfrac{n}{2} - \tfrac12 .$$
So the quasi-polynomial has period $1$ with
$$a = 1,\quad b = -\tfrac12,\quad c = -\tfrac12 \;\Longrightarrow\; 4a = 4,\quad 2b = -1 .$$

*Topology.* The standard alternating $4$-crossing diagram is adequate with $c_+=c_-=2$. Its two checkerboard surfaces are once-punctured Klein bottles $S_\pm$, each essential, each with $\chi(S_\pm) = -1$ and $|\partial S_\pm| = 1$, of boundary slopes $+4$ and $-4$. The full boundary slope set is $bs_{4_1} = \{0, \pm 4\}$.

*Verification.* $S_+$ has slope $4 = 4a$ ✓ and $\chi(S_+)/|\partial S_+| = -1 = 2b$ ✓. Amphichirality gives $\min\deg_q \widetilde J = -(n^2 - \tfrac n2 - \tfrac12)$, so $4a^\ast = -4$, $2b^\ast = +1$; the mirror-convention statement is realized by $S_-$. Both Jones surfaces are non-orientable — the Seifert surface (slope $0$, $\chi = -1$) is *not* a Jones surface, which shows the conjecture selects specific surfaces rather than merely asserting membership in $bs_K$.

*Contrast: the right-handed trefoil.* $J_{3_1,1}=1$ and $J_{3_1,2} = -q^4+q^3+q$ force $\max\deg_q J_{3_1,n} = \tfrac32 n^2 - \tfrac12 n - 1$, so for $\widetilde J$: $a=\tfrac32$, $b=0$. Then $4a = 6$ and $2b = 0$: the Jones surface is the cabling annulus of slope $6$, with $\chi = 0$ and $|\partial S| = 2$. Here $|\partial S| \ne 1$, illustrating why the conjecture is stated with the normalized Euler characteristic $\chi(S)/|\partial S|$ rather than $\chi(S)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*