---
id: 04-topology/hirschs-conjecture
title: "Hirsch's Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hirsch's Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/hirschs-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $P \subset \mathbb{R}^d$ be a convex polytope of dimension $d$ with exactly $n$ facets. Its **graph** $G(P)$ has the vertices of $P$ as nodes and the edges (1-faces) of $P$ as arcs. The **combinatorial diameter** $\delta(P)$ is the maximum over vertex pairs $u,v$ of the minimum number of edges in a $u$–$v$ path in $G(P)$.

**Hirsch's Conjecture (1957).** For every $d$-polytope $P$ with $n$ facets,
$$\delta(P) \;\le\; n - d .$$

The **unbounded Hirsch conjecture** asserts the same for pointed polyhedra. The **Polynomial Hirsch Conjecture** weakens the claim to: there is a polynomial $f$ with $\delta(P) \le f(n,d)$.

**Status.** The bounded conjecture is **false**. Francisco Santos (announced May 2010; *Annals of Mathematics* 2012) constructed a $43$-dimensional polytope with $86$ facets and diameter at least $44 > 86 - 43$. The unbounded version had already been refuted by Klee and Walkup (1967). A disproof required exhibiting a single $(d,n)$ with a polytope of diameter $> n-d$; Santos did so, and the counterexample has been independently verified computationally. The *polynomial* version — the one that matters for the simplex method — remains **wide open**: no polynomial upper bound on $\delta(P)$ in $n$ and $d$ is known.

## 2. Mathematical Foundations

Let $P = \{x \in \mathbb{R}^d : a_i^{\mathsf T} x \le b_i,\ i = 1,\dots,n\}$ be a simple $d$-polytope (each vertex lies on exactly $d$ facets). Passing to simple polytopes is WLOG: perturbing the $b_i$ can only increase the diameter, so the maximum of $\delta$ over all $d$-polytopes with $n$ facets,
$$H(n,d) \;=\; \max\{\delta(P) : \dim P = d,\ P \text{ has } n \text{ facets}\},$$
is attained on simple polytopes. Hirsch's conjecture is $H(n,d) \le n-d$.

**Dual/topological form.** The boundary complex $\partial P^{*}$ of the polar dual is a simplicial $(d-1)$-sphere with $n$ vertices; $G(P)$ is its **dual graph** (facets adjacent iff they share a ridge). So the conjecture is a statement about *normal* (locally strongly connected) pure simplicial complexes: for a normal simplicial $(d-1)$-complex $C$ with $n$ vertices, is the dual diameter at most $n-d$? This places the problem inside PL topology, not just convexity.

**Non-revisiting path conjecture (Klee–Wolfe).** $P$ satisfies the *non-revisiting property* if any two vertices are joined by a path that, once it leaves a facet, never returns to it. Such a path has length $\le n-d$ (it enters at most $n-d$ new facets), so
$$\text{non-revisiting for all } P \;\Longrightarrow\; \text{Hirsch}.$$
Klee and Walkup proved the two are equivalent.

**$d$-step theorem (Klee–Walkup 1967).** $H(n,d) \le n-d$ for all $n,d$ iff $H(2d,d) = d$ for all $d$. The hard case is $n = 2d$.

**Spindles and the strong $d$-step theorem (Santos 2012).** A **$d$-spindle** is a $d$-polytope $P$ with two distinguished vertices $u,v$ such that every facet contains exactly one of them. Its **length** $\ell(P)$ is the graph distance $\mathrm{dist}_{G(P)}(u,v)$.

> **Theorem (Santos).** If $P$ is a $d$-spindle with $n > 2d$ facets and length $\ell$, then there is an $(n-d)$-polytope with $2(n-d)$ facets and diameter at least $\ell + n - 2d$. In particular, if $\ell > d$ the Hirsch bound is violated.

The proof repeatedly applies the *wedge* (one-point suspension) operation, which raises dimension and facet count by one each while preserving the relevant distance.

**Known bounds.**
- Larman (1970): $H(n,d) \le n \, 2^{d-3}$; Barnette (1974): $H(n,d) \le \tfrac{2}{3}\,2^{d} n$ — linear in $n$, exponential in $d$.
- Kalai–Kleitman (1992): $H(n,d) \le n^{\log_2 d + 2}$ — quasi-polynomial.
- Todd (2014): $H(n,d) \le (n-d)^{\log_2 d}$.
- Sukegawa (2019): $H(n,d) \le (n-d)^{\log_2 O(d/\log d)}$, the current best.
- Lower bound: $H(n,d) \ge (1+\varepsilon)(n-d)$ for some fixed $\varepsilon > 0$ (Santos; $\varepsilon \approx 1/20$ after Matschke–Santos–Weibel).

## 3. History & State of the Art (SOTA)

- **1957.** Warren M. Hirsch communicates the conjecture to George Dantzig, motivated by bounding the number of pivots of the simplex method. Dantzig records it in *Linear Programming and Extensions* (Princeton, 1963).
- **1967.** Klee and Walkup prove the $d$-step and non-revisiting equivalences, verify $d \le 3$, and **disprove the unbounded version** with a $4$-dimensional unbounded polyhedron with $8$ facets and diameter $5 > 8-4$.
- **1970–74.** Larman's $n2^{d-3}$ and Barnette's $\tfrac23 2^d n$ bounds; nothing better in $d$ for two decades.
- **1992.** Kalai and Kleitman give the quasi-polynomial $n^{\log d + 2}$ bound by an elegant two-page recursion on "how far you can get seeing at most half the facets".
- **2010.** Santos announces a $43$-dimensional counterexample at the *Klee memorial* conference (Seattle), built from a $5$-spindle with $48$ facets and length $6$.
- **2012.** Published as *A counterexample to the Hirsch conjecture*, Annals of Mathematics 176(1), 383–412.
- **2015.** Matschke, Santos and Weibel classify $5$-dimensional prismatoids of large width and shrink the counterexample to dimension $20$ with $40$ facets and diameter $21$; they also produce the asymptotic family $\delta \ge (1+\varepsilon)n$.
- **2014–2019.** Todd and then Sukegawa sharpen Kalai–Kleitman; the gap between $(n-d)^{\Theta(\log d)}$ and $\Omega(n)$ is unchanged in essence today.

## 4. Partial Results / Verified Cases

The Hirsch bound $\delta \le n-d$ **holds** in the following settings:

- **Low dimension:** $d \le 3$ (Klee–Walkup 1967). For $3$-polytopes Klee proved the sharper $\delta \le \lfloor 2n/3 \rfloor - 1$.
- **Few facets:** $n - d \le 6$ (Bremner–Deza–Hua–Schewe 2013, by exhaustive enumeration of the relevant combinatorial types; earlier Bremner–Schewe settled $n-d \le 6$ for $d\le 6$). Santos' counterexamples have $n-d = 43$ and $n-d=20$; the exact threshold $n-d$ at which Hirsch first fails is unknown.
- **$0/1$-polytopes:** $\delta(P) \le d$ for any polytope with vertices in $\{0,1\}^d$ (Naddef 1989) — strictly stronger than Hirsch since $n \ge d+1$.
- **Dual transportation polyhedra:** Hirsch holds exactly (Balinski 1984). For $m \times n$ transportation polytopes, Brightwell–van den Heuvel–Stougie and later Borgwardt et al. give linear bounds; network-flow polytopes have $O(mn\log m)$-type bounds.
- **Flag complexes:** any normal flag simplicial complex on $n$ vertices of dimension $d-1$ has dual diameter $\le n-d$ (Adiprasito–Benedetti, *Math. of Operations Research* 2014) — a purely topological/metric-geometric proof via non-revisiting paths and CAT(1) ideas. This includes all order complexes and all polytopes whose duals are flag.
- **Bounded subdeterminants:** if $A \in \mathbb{Z}^{n\times d}$ has all subdeterminants at most $\Delta$ in absolute value, then $\delta \le O(d^4\Delta^2 \log(d\Delta))$ (Bonifas–Di Summa–Eisenbrand–Hähnle–Niemeier 2014); for totally unimodular $A$ ($\Delta=1$) this is polynomial, refining Dyer–Frieze.
- **Lattice polytopes:** for $P \subseteq [0,k]^d$, $\delta(P) \le kd$ (Kleinschmidt–Onn 1992), improved to $\lfloor kd - \tfrac{2}{3}d - (k-3)\rfloor$ for $k \ge 3$ by Deza–Pournin.

## 5. Principal Obstacles

- **No polynomial method exists.** The only technique yielding sub-exponential bounds in $d$ is the Kalai–Kleitman recursion, which is *purely combinatorial*: it uses only that a set of $n$ facets can be split so that one half "covers" the ball of radius $r$. That argument provably cannot give better than $n^{\Theta(\log d)}$ — the same recursion is tight for abstract set systems (Eisenbrand–Hähnle–Razborov–Rothvoß 2010 exhibit *connected layer families* with diameter $\Omega(n^2/\log n)$ satisfying all the combinatorial axioms used). So the barrier is not a missing lemma but the absence of any use of *convexity*.
- **Geometry has no handle.** Linear-programming-style arguments (shadow vertex, potential functions) control the number of pivots for a *specific* objective, not the graph metric. There is no known metric or curvature invariant of $\partial P$ that bounds dual diameter; Adiprasito–Benedetti's success for flag complexes relies on non-positive-curvature-flavoured arguments that break as soon as the dual complex has an empty triangle.
- **Counterexample constructions do not scale.** Santos' spindles gain only a $(1+\varepsilon)$ factor. To disprove the polynomial version one would need spindles with length superlinear in $d$; the $5$-dimensional prismatoid classification shows the small-dimensional supply is essentially exhausted.
- **Topological over-generality.** The dual formulation is a statement about normal simplicial spheres, but simplicial spheres are far more numerous than polytopal ones ($2^{\Theta(n^{\lfloor d/2\rfloor})}$ vs. $2^{O(d^2 n \log n)}$), and non-polytopal spheres violating Hirsch-type bounds exist. Any proof must therefore distinguish polytopes from spheres — a distinction with no known combinatorial characterisation (Steinitz's theorem stops at $d=3$).

## 6. The Gap

The bounded conjecture as literally stated is closed (false). The live gap is quantitative:
$$\Omega\!\left((1+\tfrac{1}{20})(n-d)\right) \;\le\; H(n,d) \;\le\; (n-d)^{\log_2 O(d/\log d)} .$$
The exact step to be crossed: produce either (i) a bound $H(n,d) \le \mathrm{poly}(n,d)$ — which requires an argument that fails on abstract connected layer families, i.e. that genuinely uses linear inequalities; or (ii) a family of polytopes with $\delta$ superlinear in $n$ for fixed ratio $n/d$, which requires spindles of length $\omega(d)$. Both directions are currently blocked at exactly the point identified in Section 5.

## 7. Current Research (as of June 2026)

- **Abstract combinatorial models.** Continued study of connected layer families and Hähnle-type conjectures ($\delta \le d(n/d - 1)$ for abstract models); the Polymath 3 project (Kalai, 2010) remains the reference collection of approaches and failures.
- **Circuit diameter** (Borgwardt, De Loera, Finhold, and collaborators): relaxing edges to circuit walks. The circuit-diameter analogue of Hirsch is open in general but proven for dual transportation and network polyhedra, and is a natural weakening whose resolution would constrain the original. *(frontier — verify)* Recent work reports circuit-diameter bounds of order $O(n)$ for large classes of $0/1$ and totally unimodular polyhedra.
- **Subdeterminant-based bounds.** Ongoing refinement of the $O(d^4\Delta^2\log d\Delta)$ bound; interest is driven by the parallel programme on strongly polynomial LP.
- **Topological combinatorics.** Extensions of the Adiprasito–Benedetti flag-complex theorem to complexes with bounded "non-flagness", and to normal complexes admitting non-positively-curved metrics.
- **Computational search.** Enumeration of $5$- and $6$-dimensional prismatoids and spindles of large width (Weibel, Santos and successors) to lower the dimension of the smallest known counterexample below $20$. *(frontier — verify)* The smallest published counterexample remains $d=20$, $n=40$, $\delta = 21$.
- **Groups:** Universidad de Cantabria (Santos), FU Berlin / discrete geometry, IAS/Hebrew University (Kalai), UC Davis (De Loera), Colorado Denver (Borgwardt), EPFL/Bonn (Eisenbrand).

## 8. Future Work

1. **Settle the Polynomial Hirsch Conjecture**, ideally via a bound of the form $O(n d)$ or $O(n \log d)$. Kalai's stated priority is to find *any* argument using convexity that beats $n^{\log d}$.
2. **Determine the minimum $n-d$ for which Hirsch fails.** Known: $\ge 7$ and $\le 20$. Closing this needs either better enumeration or new small spindles.
3. **Prove or refute Hähnle's conjecture** $H(n,d) \le d(n/d-1)$ for abstract models; it is the natural sharp form consistent with all known data.
4. **Extend the flag-complex theorem.** Adiprasito and Benedetti suggest the correct generality is "normal complexes with a suitable non-positively curved metric"; identifying that class is open.
5. **Diameter of lattice polytopes** in $[0,k]^d$: close the gap between the Deza–Pournin upper bound and the $\Omega(k^{2/3}d)$-type lower bounds.

## 9. Key References

- **[Foundational]** G. B. Dantzig. *Linear Programming and Extensions.* Princeton University Press, 1963.
- **[Foundational]** V. Klee, D. W. Walkup. *The $d$-step conjecture for polyhedra of dimension $d<6$.* Acta Mathematica 117 (1967), 53–78.
- **[Foundational]** D. G. Larman. *Paths on polytopes.* Proceedings of the London Mathematical Society 20 (1970), 161–178.
- **[Foundational]** G. Kalai, D. J. Kleitman. *A quasi-polynomial bound for the diameter of graphs of polyhedra.* Bulletin of the American Mathematical Society 26 (1992), 315–316. [DOI](https://doi.org/10.1090/s0273-0979-1992-00285-9)
- **[SOTA]** F. Santos. *A counterexample to the Hirsch conjecture.* Annals of Mathematics 176(1) (2012), 383–412. [DOI](https://doi.org/10.4007/annals.2012.176.1.7)
- **[SOTA]** B. Matschke, F. Santos, C. Weibel. *The width of five-dimensional prismatoids.* Proceedings of the London Mathematical Society 110(3) (2015), 647–672. [DOI](https://doi.org/10.1112/plms/pdu064)
- **[SOTA]** M. J. Todd. *An improved Kalai–Kleitman bound for the diameter of a polyhedron.* SIAM Journal on Discrete Mathematics 28(4) (2014), 1944–1947. [DOI](https://doi.org/10.1137/140962310)
- **[SOTA]** N. Sukegawa. *An asymptotically improved upper bound on the diameter of polyhedra.* Discrete & Computational Geometry 62 (2019), 690–699. [DOI](https://doi.org/10.1007/s00454-018-0016-y)
- **[SOTA]** K. Adiprasito, B. Benedetti. *The Hirsch conjecture holds for normal flag complexes.* Mathematics of Operations Research 39(4) (2014), 1340–1348. [DOI](https://doi.org/10.1287/moor.2014.0661)
- **[SOTA]** N. Bonifas, M. Di Summa, F. Eisenbrand, N. Hähnle, M. Niemeier. *On sub-determinants and the diameter of polyhedra.* Discrete & Computational Geometry 52 (2014), 102–115. [DOI](https://doi.org/10.1007/s00454-014-9601-x)
- **[Related]** F. Eisenbrand, N. Hähnle, A. Razborov, T. Rothvoß. *Diameter of polyhedra: limits of abstraction.* Mathematics of Operations Research 35(4) (2010), 786–794. [DOI](https://doi.org/10.1287/moor.1100.0470)
- **[Survey]** E. D. Kim, F. Santos. *An update on the Hirsch conjecture.* Jahresbericht der Deutschen Mathematiker-Vereinigung 112(2) (2010), 73–98. [DOI](https://doi.org/10.1365/s13291-010-0001-8)
- **[Survey]** F. Santos. *Recent progress on the combinatorial diameter of polytopes and simplicial complexes.* TOP 21(3) (2013), 426–460. [DOI](https://doi.org/10.1007/s11750-013-0295-7)
- **[Related]** D. Bremner, A. Deza, W. Hua, L. Schewe. *More bounds on the diameters of convex polytopes.* Optimization Methods and Software 28(3) (2013), 442–450. [DOI](https://doi.org/10.1080/10556788.2012.668906)

## 10. Worked Example / Concrete Special Case

**(a) Tightness on the cube.** Take $P = [0,1]^d$: $n = 2d$ facets, dimension $d$. Two vertices $x,y \in \{0,1\}^d$ are adjacent iff they differ in one coordinate, so $\mathrm{dist}(x,y) = \|x-y\|_1$ and
$$\delta([0,1]^d) = d = 2d - d = n - d .$$
The cube meets the Hirsch bound with equality. This is the $d$-step case $n = 2d$ that Klee–Walkup showed is the *only* case that matters: if $\delta \le d$ for all $d$-polytopes with $2d$ facets, Hirsch follows in general.

**(b) Why $n=2d$ is the crux (sketch).** Given a $d$-polytope with $n > 2d$ facets and vertices $u,v$ at distance $> n-d$, one can repeatedly apply a *wedge*: choose a facet $F$ not containing $u$ or $v$, and form $W = \{(x,t) : x \in P,\ 0 \le t \le \lambda(x)\}$ where $\lambda$ is affine and vanishes on $F$. Then $\dim W = d+1$, $W$ has $n+1$ facets, and the distance between the lifted copies of $u,v$ does not drop. So a violation at $(n,d)$ propagates to $(n+1,d+1)$, and the "excess" $n-d$ stays constant — one may normalise to $n = 2d$.

**(c) The counterexample arithmetic.** Santos exhibits a **$5$-spindle** $Q$ with $n = 48$ facets and length $\ell(Q) = 6 > 5 = d$. Apply the strong $d$-step theorem with $d = 5$, $n = 48$, $\ell = 6$:

- new dimension: $n - d = 48 - 5 = 43$;
- new facet count: $2(n-d) = 86$;
- diameter at least $\ell + n - 2d = 6 + 48 - 10 = 44$.

The Hirsch bound for a $43$-polytope with $86$ facets is $86 - 43 = 43 < 44$. The conjecture fails. Concretely, $Q$ is obtained from a $4$-dimensional *prismatoid* (a polytope whose vertices lie on two parallel hyperplanes) of width $6$; the "width" of the prismatoid — the number of steps needed in its normal-fan dual graph to cross from the top facet to the bottom facet — is exactly the spindle length, and Santos' construction produces one with width $6$ using $48$ facets.

The later refinement uses a $5$-spindle with $n = 25$ facets and length $6$, giving $d = 20$, $86 \mapsto 40$ facets, and diameter $\ge 6 + 25 - 10 = 21 > 40 - 20 = 20$: the smallest counterexample known.

**(d) The unbounded case, for contrast.** Klee–Walkup's polyhedron $Q_4$ is $4$-dimensional, pointed, with $8$ facets and two vertices at distance $5 > 8-4 = 4$. It shows that unboundedness alone already breaks the bound at excess $n-d=4$, forty-three years before the bounded case fell.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*