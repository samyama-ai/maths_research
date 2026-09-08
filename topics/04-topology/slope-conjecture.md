---
id: 04-topology/slope-conjecture
title: "Slope Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Slope Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/slope-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $J_{K,n}(q) \in \mathbb{Z}[q^{\pm 1}]$ denote its colored Jones polynomial, normalized so that $J_{\text{unknot},n} = 1$, where $n \ge 1$ indexes the $n$-dimensional irreducible representation of $\mathfrak{sl}_2$. Write $\delta_K(n) = \deg_q J_{K,n}(q)$ for the maximal $q$-degree.

Garoufalidis proved that $\delta_K(n)$ is a **quadratic quasi-polynomial** for $n \gg 0$. The set of **Jones slopes** is the (finite) set of cluster points

$$ js_K \;=\; \left\{ \text{cluster points of } \left( \tfrac{4\,\delta_K(n)}{n^2} \right)_{n \ge 1} \right\}. $$

**Slope Conjecture (Garoufalidis, 2011).** For every knot $K$,
$$ js_K \subseteq bs_K, $$
where $bs_K \subset \mathbb{Q} \cup \{1/0\}$ is the set of boundary slopes of essential (incompressible, $\partial$-incompressible) surfaces properly embedded in the knot exterior $E(K) = S^3 \setminus \nu(K)$.

Applying the statement to the mirror $\overline{K}$, and using $J_{\overline{K},n}(q) = J_{K,n}(q^{-1})$, gives the dual assertion for the minimal degree $\delta^*_K(n)$.

A complete proof must produce, for each knot and each cluster point $a \in js_K$, an essential surface in $E(K)$ with that boundary slope; a disproof requires a knot whose quantum degree slope is not in Hatcher's finite boundary-slope set.

## 2. Mathematical Foundations

**Colored Jones polynomial.** For $n \ge 1$, $J_{K,n}$ is the Reshetikhin–Turaev invariant of $K$ colored by $V_n = \operatorname{Sym}^{n-1}\mathbb{C}^2$; $J_{K,2}$ is the ordinary Jones polynomial. Garoufalidis–Lê proved the sequence $(J_{K,n})_n$ is **$q$-holonomic**: it satisfies a linear recursion
$$ \sum_{j=0}^{d} c_j(q, q^n)\, J_{K,n+j}(q) = 0, \qquad c_j \in \mathbb{Z}[q,q^n]. $$

**Quasi-polynomiality.** A function $\delta:\mathbb{N}\to\mathbb{Q}$ is a quadratic quasi-polynomial of period $\pi$ if
$$ \delta(n) = a(n)\,n^2 + b(n)\,n + c(n), \qquad a(n+\pi)=a(n),\; b(n+\pi)=b(n),\; c(n+\pi)=c(n). $$
Garoufalidis' theorem (2011) says the degree of any $q$-holonomic sequence of this type is eventually such a function. Hence $4\delta_K(n)/n^2 \to \{4a(1),\dots,4a(\pi)\}$ and $js_K$ is finite.

**Boundary slopes.** An embedded surface $S \subset E(K)$ with $\partial S \neq \emptyset$ is essential if incompressible and $\partial$-incompressible. Each boundary curve is isotopic in $\partial E(K) \cong T^2$ to $p\mu + q\lambda$ in the meridian–longitude basis; the slope is $p/q \in \mathbb{Q}\cup\{1/0\}$. **Hatcher's theorem (1982):** $bs_K$ is a finite set. Seifert surfaces give slope $0$; the meridian disk of the solid torus is excluded ($\partial$-compressible).

**Strong Slope Conjecture (Kalfagianni–Tran, 2015).** For each $n$ in a residue class where $\delta_K(n) = a n^2 + b n + c$ with $4a \in js_K$, there is an essential surface $S \subset E(K)$ with boundary slope $4a$ and
$$ \frac{\chi(S)}{|\partial S|} \;=\; b, $$
so the linear coefficient records normalized Euler characteristic, not merely the slope. (Equivalently $2\chi(S)/|\partial S| = 2b$ in the authors' normalization.)

**Adequacy.** A link diagram $D$ is $A$-adequate if the all-$A$ Kauffman state graph has no loops, $B$-adequate dually, adequate if both. For adequate $D$ with $c_\pm$ positive/negative crossings, the checkerboard surfaces are essential (Ozawa) with slopes $2c_+$ and $-2c_-$.

## 3. History & State of the Art (SOTA)

- **1982–1989.** Hatcher proves finiteness of $bs_K$; Hatcher–Thurston classify incompressible surfaces in $2$-bridge complements; Hatcher–Oertel give an algorithm for Montesinos boundary slopes. These make $bs_K$ computable in large families.
- **2005.** Garoufalidis–Lê: $q$-holonomicity of the colored Jones function — the structural input that makes $\delta_K(n)$ tractable.
- **2011.** Garoufalidis, *The Jones slopes of a knot* (Quantum Topology 2, 43–69), states the conjecture, proves quasi-polynomiality of $\delta_K$ in the companion paper, verifies torus knots and all knots with at most $9$ crossings.
- **2011.** Futer–Kalfagianni–Purcell settle the adequate case, identifying Jones slopes with checkerboard-surface slopes.
- **2015–2017.** Cabling formulas (Kalfagianni–Tran), the Strong Slope Conjecture, graph knots (Motegi–Takata), $2$-fusion knots by quadratic integer programming (Garoufalidis–van der Veen), pretzel knots (Lee–van der Veen).
- **2018–2021.** Montesinos knots (Garoufalidis–Lee–van der Veen); twisted generalized Whitehead doubles (Baker–Motegi–Takata); Kalfagianni's converse-type theorem characterizing adequacy by Jones slopes and diameter.

No counterexample is known. The conjecture is verified for every knot on which it has been tested, including the full census up to $9$ crossings and all Montesinos knots.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Torus knots $T(p,q)$ | $js = \{pq\}$, realized by the cabling annulus | Garoufalidis 2011 |
| Alternating knots | $js_K = \{2c_+\}$, $js_{\overline K}$ from $-2c_-$; checkerboard surfaces | Garoufalidis 2011; FKP 2011 |
| Adequate knots (incl. all alternating, most Montesinos) | Slope Conjecture true; degrees computed exactly from state graphs | Futer–Kalfagianni–Purcell 2011 |
| Knots with $\le 9$ crossings | Verified by direct computation | Garoufalidis 2011 |
| Iterated cables of knots satisfying the (strong) conjecture | Closed under cabling, with explicit slope formula $js_{K_{p,q}}$ | Kalfagianni–Tran 2015 |
| Graph knots (obtained from unknot by splicing Seifert-fibered pieces) | Strong Slope Conjecture holds | Motegi–Takata 2017 |
| $2$-fusion knots $K(m_1,m_2)$ | Slopes computed via quadratic integer programming | Garoufalidis–van der Veen 2016 |
| $3$-string pretzel knots $P(a,b,c)$ | Slopes and strong version verified | Lee–van der Veen 2016 |
| All Montesinos knots | Slope Conjecture proven | Garoufalidis–Lee–van der Veen 2018 |
| Twisted generalized Whitehead doubles | Strong Slope Conjecture, including satellites with non-integral slopes | Baker–Motegi–Takata 2020 |

## 5. Principal Obstacles

- **No canonical surface from a state sum.** Only in the adequate case does the Kauffman-bracket skein expansion have a term whose extreme degree survives without cancellation and simultaneously corresponds to an embedded checkerboard surface. For non-adequate diagrams the extremal degree comes from a cancellation-sensitive combination of states, so the natural "geometrize the leading term" strategy has no input.
- **Degrees are not additive under geometric operations.** Boundary slopes behave predictably under cabling and splicing; degrees of colored Jones behave predictably only when one already controls the growth rate of every term, which fails for hyperbolic knots with large volume.
- **Quasi-periodicity has no known topological meaning.** The period $\pi$ of the quasi-polynomial is bounded by the recursion, but no construction turns a residue class mod $\pi$ into a surface. Examples with $\pi > 1$ (e.g. certain $2$-fusion and pretzel knots) are exactly where ad hoc arguments break down.
- **The $A$-polynomial route is conditional.** Newton polygon slopes of the $A$-polynomial are boundary slopes (Culler–Shalen theory), and the AJ conjecture would relate the recursion to $A_K$; but AJ is itself open, and the degree of a $q$-holonomic sequence is not determined by the recursion's Newton polygon alone (degree drops from leading-coefficient vanishing).
- **Non-effective finiteness.** Hatcher's finiteness is not accompanied by a general algorithm to list $bs_K$ outside Montesinos/graph families, so even brute-force verification stalls for a general hyperbolic knot.

## 6. The Gap

Proven: the conjecture for classes whose incompressible surfaces are *combinatorially visible* — adequate diagrams (checkerboard surfaces), Seifert-fibered and splice-decomposable pieces (vertical/horizontal surfaces), Montesinos knots (Hatcher–Oertel edgepath systems), and anything built from these by cabling or doubling.

Unproven: any statement covering a general hyperbolic knot with no adequate diagram and no arborescent structure. The exact missing step is a **degree-to-surface map**: given the extremal $q$-degree data of $(J_{K,n})_n$ — obtained from a recursion or from a state sum with cancellations — construct an essential spanning surface whose boundary slope equals $4a$. Every known proof instead runs the reverse direction, computing $\delta_K$ from a surface already in hand. No mechanism converts asymptotic degree growth into embedded topology, and the vanishing of leading coefficients (the point where degree drops below the naive bound) is precisely the analytic phenomenon that must be shown to be geometric.

## 7. Current Research (as of June 2026)

- **Michigan State (Kalfagianni and collaborators):** strong slope conjecture for satellites and links, and converse statements — Jones slope diameter $\mathrm{js}_K - \mathrm{js}_{\overline K}$ bounds crossing number, characterizing adequate knots. Extensions to Jones slopes of links and to crosscap numbers remain active.
- **Garoufalidis–van der Veen school:** algorithmic computation of $\delta_K(n)$ from certified recursions, plus quadratic integer programming to extract quasi-polynomial data; the practical bottleneck is producing a minimal-order recursion for knots beyond $\sim 12$ crossings. *(frontier — verify)* Machine-assisted verification of the conjecture across the full $\le 12$-crossing census has been reported in preprint form but not uniformly published.
- **Baker–Motegi–Takata:** satellite constructions producing knots with prescribed Jones slopes, used both as test cases and as a source of potential counterexamples with non-integral slopes.
- **Interaction with the AJ conjecture and quantum modularity:** attempts to read slopes off the Newton polygon of the $\hat{A}$-polynomial, and off asymptotics of state integrals. *(frontier — verify)*

## 8. Future Work

- Prove the conjecture for all knots admitting a *near-adequate* diagram, quantifying how much cancellation a state-sum degree argument can tolerate.
- Establish closure of the (strong) conjecture under all satellite operations, not just cables and Whitehead doubles — this would reduce the problem to hyperbolic and Seifert-fibered pieces of the JSJ decomposition.
- Derive the Slope Conjecture as a corollary of AJ plus a no-degree-drop hypothesis, and characterize when degree drop occurs.
- Give an effective algorithm computing $bs_K$ for hyperbolic knots, making systematic falsification tests possible.
- Interpret the quasi-periodicity period $\pi$ topologically, e.g. as the number of essential surfaces realizing a slope, or as torsion in $H_1$ of a branched cover.

## 9. Key References

- **[Foundational]** A. Hatcher. *On the boundary curves of incompressible surfaces.* Pacific Journal of Mathematics 99 (1982), 373–377. [DOI](https://doi.org/10.2140/pjm.1982.99.373)
- **[Foundational]** A. Hatcher, U. Oertel. *Boundary slopes for Montesinos knots.* Topology 28 (1989), 453–480. [DOI](https://doi.org/10.1016/0040-9383(89)90005-0)
- **[Foundational]** S. Garoufalidis, T. T. Q. Lê. *The colored Jones function is $q$-holonomic.* Geometry & Topology 9 (2005), 1253–1293. [DOI](https://doi.org/10.2140/gt.2005.9.1253)
- **[Foundational]** S. Garoufalidis. *The degree of a $q$-holonomic sequence is a quadratic quasi-polynomial.* Electronic Journal of Combinatorics 18(2) (2011), #P4. [DOI](https://doi.org/10.37236/2000)
- **[Foundational]** S. Garoufalidis. *The Jones slopes of a knot.* Quantum Topology 2 (2011), 43–69. [DOI](https://doi.org/10.4171/qt/13)
- **[SOTA]** D. Futer, E. Kalfagianni, J. Purcell. *Slopes and colored Jones polynomials of adequate knots.* Proceedings of the AMS 139 (2011), 1889–1896. [DOI](https://doi.org/10.1090/s0002-9939-2010-10617-2)
- **[SOTA]** E. Kalfagianni, A. T. Tran. *Knot cabling and the degree of the colored Jones polynomial.* New York Journal of Mathematics 21 (2015), 905–941.
- **[SOTA]** S. Garoufalidis, R. van der Veen. *Quadratic integer programming and the slope conjecture.* New York Journal of Mathematics 22 (2016), 907–932.
- **[SOTA]** C. Lee, R. van der Veen. *Slopes for pretzel knots.* Algebraic & Geometric Topology 16 (2016), 3617–3654.
- **[SOTA]** K. Motegi, T. Takata. *The slope conjecture for graph knots.* Mathematical Proceedings of the Cambridge Philosophical Society 162 (2017), 383–392. [DOI](https://doi.org/10.1017/s0305004116000566)
- **[SOTA]** S. Garoufalidis, C. Lee, R. van der Veen. *The slope conjecture for Montesinos knots.* arXiv:1807.00957 (2018).
- **[SOTA]** K. Baker, K. Motegi, T. Takata. *The strong slope conjecture for twisted generalized Whitehead doubles.* Quantum Topology 11 (2020), 545–608. [DOI](https://doi.org/10.4171/qt/242)
- **[Survey]** E. Kalfagianni. *A Jones slopes characterization of adequate knots.* Indiana University Mathematics Journal 67 (2018), 205–219. [DOI](https://doi.org/10.1512/iumj.2018.67.6285)
- **[Survey]** D. Futer, E. Kalfagianni, J. Purcell. *Guts of Surfaces and the Colored Jones Polynomial.* Lecture Notes in Mathematics 2069, Springer, 2013. [DOI](https://doi.org/10.1007/978-3-642-33302-6)

## 10. Worked Example / Concrete Special Case

**Figure-eight knot $4_1$.** Habiro–Lê give the cyclotomic expansion (normalized, $J_{\text{unknot},N}=1$):
$$ J_{4_1,N}(q) \;=\; \sum_{k=0}^{N-1} \prod_{j=1}^{k} \left(q^{(N-j)/2}-q^{-(N-j)/2}\right)\left(q^{(N+j)/2}-q^{-(N+j)/2}\right). $$

Each factor pair contributes top degree $\tfrac{N-j}{2} + \tfrac{N+j}{2} = N$, independent of $j$. So the $k$-th summand has top degree $kN$ and bottom degree $-kN$. The maximum over $0 \le k \le N-1$ is attained at $k=N-1$ with no cancellation of the extreme monomial (the leading coefficient of the top term is $\pm 1$). Hence
$$ \delta_{4_1}(N) = N(N-1) = N^2 - N, \qquad \delta^*_{4_1}(N) = -(N^2-N). $$

The quasi-polynomial has period $\pi = 1$, with $a = 1$, $b = -1$, $c = 0$. Therefore
$$ \frac{4\delta_{4_1}(N)}{N^2} = 4 - \frac{4}{N} \longrightarrow 4, \qquad js_{4_1} = \{4\}, \quad js_{\overline{4_1}} = \{-4\}. $$

**Topological side.** Hatcher–Thurston's classification for $2$-bridge knots gives $bs_{4_1} = \{0, 4, -4\}$: slope $0$ is the genus-one Seifert surface, and $\pm 4$ are realized by the two once-punctured Klein bottles spanning $4_1$. Since $\{4\} \subset bs_{4_1}$, the Slope Conjecture holds.

**Strong version.** For the slope-$4$ surface $S$ (once-punctured Klein bottle): $\chi(S) = -1$ and $|\partial S| = 1$, so
$$ \frac{\chi(S)}{|\partial S|} = -1 = b, $$
matching the linear coefficient of $\delta_{4_1}(N) = N^2 - N$. Both the quadratic and linear data of the colored Jones degree are read off a single embedded surface — this is exactly the correspondence the conjecture asserts in general, and exactly what is unavailable when the extremal degree arises through cancellation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*