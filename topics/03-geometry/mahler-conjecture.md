---
id: 03-geometry/mahler-conjecture
title: "Mahler Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mahler Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/mahler-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For a convex body $K \subset \mathbb{R}^n$ (compact, convex, non-empty interior) containing the origin in its interior, the **polar body** is
$$K^\circ = \{\, y \in \mathbb{R}^n : \langle x, y \rangle \le 1 \ \ \forall x \in K \,\},$$
and the **volume product** (Mahler volume) is $v(K) = |K| \, |K^\circ|$, where $|\cdot|$ is Lebesgue measure. For general $K$ one takes the Santaló point as origin, i.e. $\mathcal{P}(K) = \min_{z \in \operatorname{int} K} |K| \, |(K-z)^\circ|$. The quantity is affine-invariant: $\mathcal{P}(AK) = \mathcal{P}(K)$ for all $A \in GL_n(\mathbb{R})$.

**Conjecture (Mahler, 1939) — symmetric case.** If $K = -K$, then
$$v(K) \ \ge \ \frac{4^n}{n!},$$
with equality for the cube $[-1,1]^n$ and its polar the cross-polytope.

**Conjecture — general case.** For any convex body $K$,
$$\mathcal{P}(K) \ \ge \ \frac{(n+1)^{n+1}}{(n!)^2},$$
with equality precisely for simplices.

A complete proof must establish the inequality in every dimension $n \ge 4$ (symmetric) / $n \ge 3$ (general) and, ideally, characterise the equality cases: conjecturally the **Hanner polytopes** in the symmetric case, and simplices in the general case. A disproof requires an explicit body, or a family, violating the bound.

## 2. Mathematical Foundations

Let $\|x\|_K = \inf\{t > 0 : x \in tK\}$ be the Minkowski gauge; for symmetric $K$ this is a norm, $K$ is its unit ball, and $K^\circ$ is the unit ball of the dual norm. Thus $v(K)$ is an isomorphic invariant of the $n$-dimensional normed space $X_K = (\mathbb{R}^n, \|\cdot\|_K)$, and Mahler's conjecture asserts that $\ell_\infty^n$ (equivalently $\ell_1^n$) minimises it.

Basic identities and facts:

- **Duality.** $(K^\circ)^\circ = K$; $(AK)^\circ = A^{-\top} K^\circ$, whence affine invariance.
- **Ball.** $|B_2^n| = \pi^{n/2}/\Gamma(\tfrac n2 + 1)$ and $v(B_2^n) = |B_2^n|^2$.
- **Cube.** $|[-1,1]^n| = 2^n$, $|B_1^n| = 2^n/n!$, so $v([-1,1]^n) = 4^n/n!$.
- **Simplex.** For a regular simplex $S$ with centroid at the origin, $\mathcal{P}(S) = (n+1)^{n+1}/(n!)^2$.
- **Hanner polytopes.** The class $\mathcal{H}_n$ generated from $[-1,1]$ by iterating $\ell_1$- and $\ell_\infty$-sums; every $H \in \mathcal{H}_n$ satisfies $v(H) = 4^n/n!$, and $\mathcal{H}_n$ is closed under polarity.

**Upper bound (solved).** The Blaschke–Santaló inequality states
$$\mathcal{P}(K) \ \le \ v(B_2^n) = |B_2^n|^2,$$
with equality **iff** $K$ is an ellipsoid (Santaló 1949; equality case by Petty 1985). So the volume product is pinned above; only the lower ("reverse Santaló") side is open.

**Asymptotic lower bound (solved up to constants).** Bourgain–Milman (1987): there is $c > 0$, independent of $n$, with
$$v(K) \ \ge \ c^n \, v(B_2^n).$$
Since $v(B_2^n)^{1/n} \sim 2\pi e/n$ and $(4^n/n!)^{1/n} \sim 4e/n$, this is the conjecture up to an exponential factor. The best explicit constants give
$$v(K) \ \ge \ \frac{\pi^n}{n!} = \left(\frac{\pi}{4}\right)^{n} \cdot \frac{4^n}{n!},$$
so the conjecture is known up to a multiplicative gap of $(4/\pi)^n \approx 1.273^n$.

## 3. History & State of the Art (SOTA)

Kurt Mahler introduced the volume product while studying transference principles in the geometry of numbers (*Ein Übertragungsprinzip für konvexe Körper*, Časopis pro pěstování matematiky a fysiky **68**, 1939), and in a companion paper (*Ein Minimalproblem für konvexe Polygone*, Mathematica (Zutphen) B **7**, 1939) settled the planar case completely: among convex polygons, and hence all planar bodies, the minimisers are triangles in general and parallelograms in the symmetric case.

Milestones:

| Year | Result |
|---|---|
| 1939 | Mahler: $n = 2$, symmetric and general. |
| 1949 | Santaló: upper bound (with Blaschke's $n\le3$ case). |
| 1981 | Saint-Raymond: unconditional bodies. |
| 1986 | Reisner: zonoids; equality iff cubes. |
| 1987 | Bourgain–Milman: $v(K) \ge c^n v(B_2^n)$. |
| 2008 | Kuperberg: explicit $v(K) \ge \pi^n/n!$ via Gauss linking integrals. |
| 2010 | Nazarov–Petrov–Ryabogin–Zvavitch: cube is a local minimum in the Banach–Mazur metric. |
| 2012 | Nazarov: Bourgain–Milman via Hörmander $\bar\partial$-estimates / Bergman kernels. |
| 2013 | Barthe–Fradelizi: bodies with many hyperplane symmetries. |
| 2014 | Artstein-Avidan–Karasev–Ostrover: Viterbo's symplectic conjecture $\Rightarrow$ Mahler. |
| 2020 | Iriyeh–Shibata: symmetric case in $n = 3$. |
| 2022–23 | Fradelizi–Hubard–Meyer–Roldán-Pensado–Zvavitch: short equipartition proof of the $n=3$ symmetric case. |

## 4. Partial Results / Verified Cases

Proven cases of the conjectured sharp bound:

- **Dimension $n = 2$:** both the symmetric ($v \ge 8$) and general ($\mathcal{P} \ge 27/4$) statements (Mahler 1939).
- **Dimension $n = 3$, symmetric:** $v(K) \ge 32/3$ (Iriyeh–Shibata, *Duke Math. J.* 169, 2020), with a substantially shorter proof by Fradelizi, Hubard, Meyer, Roldán-Pensado and Zvavitch using measure equipartitions by cones. The general (non-symmetric) $n=3$ case remains **open**.
- **Unconditional bodies, all $n$:** if $K$ is symmetric with respect to all $n$ coordinate hyperplanes, $v(K) \ge 4^n/n!$ (Saint-Raymond 1981; equality analysis by Meyer 1986 — equality iff $K$ is a Hanner polytope).
- **Bodies with many hyperplane symmetries:** if the isometry group of $K$ contains reflections whose hyperplanes have trivial common intersection in a suitable sense, the bound holds (Barthe–Fradelizi, *Amer. J. Math.* 135, 2013).
- **Zonoids, all $n$:** $v(Z) \ge 4^n/n!$, equality iff $Z$ is a cube (Reisner 1986); zonoids are exactly the limits of Minkowski sums of segments.
- **Polytopes with few vertices/facets:** shadow-system arguments settle the general conjecture for polytopes with at most $n+2$ vertices (Meyer–Reisner, *Mathematika* 53, 2006).
- **Local minimality:** the cube is a strict local minimum (Nazarov–Petrov–Ryabogin–Zvavitch, *Duke Math. J.* 154, 2010); all Hanner polytopes and the simplex are local minima (Kim, *J. Funct. Anal.* 266, 2014; Kim–Reisner, *Mathematika* 57, 2011).
- **All $n$, up to constants:** $v(K) \ge \pi^n/n!$ for symmetric $K$ (Kuperberg 2008; Nazarov 2012) — the conjecture within a factor $(4/\pi)^n$.

## 5. Principal Obstacles

- **No unique extremiser.** Unlike Blaschke–Santaló, where ellipsoids form a single $GL_n$-orbit, the conjectured minimisers are the Hanner polytopes — a combinatorially rich, exponentially large family ($\ge 2^{n-1}$ non-affinely-equivalent bodies) that is not connected under continuous deformation. Symmetrisation techniques (Steiner, Blaschke, shadow systems) that drive bodies towards ellipsoids therefore have no target to move toward; every known symmetrisation can *increase* the volume product on some bodies.
- **Non-convexity of the functional.** $K \mapsto v(K)$ is neither convex nor concave along Minkowski or shadow-system paths in general, so variational and Brunn–Minkowski-type machinery fails to yield global control. Local minimality proofs are genuinely local: they control second-order perturbations of the gauge but say nothing at Banach–Mazur distance $O(1)$.
- **Analytic methods lose the sharp constant.** The Bourgain–Milman route (via Milman's quotient-of-subspace theorem, or Nazarov's Hörmander $L^2$-$\bar\partial$ estimate on the tube domain $\mathbb{R}^n + i K$) produces an inequality between the Bergman kernel and the volume product where sharpness would require the kernel estimate to be saturated exactly for the cube. The Hörmander estimate is lossy precisely at the polytopal (non-smooth, non-strictly-convex) boundary, which is where the extremiser lives; the loss compounds to $(\pi/4)^n$.
- **Dimension-by-dimension arguments do not induct.** The $n=3$ proofs rely on a topological equipartition of the boundary into four pieces of equal measure by cones, an argument whose Borsuk–Ulam input has no known $n$-dimensional analogue with the required combinatorial rigidity.
- **Discrete-to-continuous transfer.** Reductions to polytopes are available, but the resulting optimisation over vertex configurations is a non-convex semialgebraic problem whose degree grows super-exponentially, defeating exact certification (SOS/Positivstellensatz) beyond very small vertex counts.

## 6. The Gap

Proven: sharpness for $n \le 2$ (all bodies), $n = 3$ (symmetric only), and for structurally restricted classes in all $n$ — unconditional bodies, zonoids, bodies with a large reflection group, polytopes with $\le n+2$ vertices, and local neighbourhoods of Hanner polytopes and the simplex. Asserted: the bound for *arbitrary* symmetric bodies in all $n \ge 4$, and arbitrary bodies in all $n \ge 3$.

The gap is quantitative and structural at once. Quantitatively, the exact deficit is the factor
$$\frac{\pi^n/n!}{4^n/n!} = \left(\frac{\pi}{4}\right)^n,$$
i.e. removing a fixed exponential loss from an analytic inequality that is *not* saturated by any smooth body. Structurally, the missing step is a symmetrisation or flow on the space of convex bodies that (i) does not increase $v$, and (ii) has the Hanner polytopes — not the ball — as its attractors. No such operation is known, and it is unclear whether one can exist given the disconnectedness of the extremal set.

## 7. Current Research (as of June 2026)

- **Complex-analytic / Bergman kernel programme.** Berndtsson's refinements of Nazarov's argument (*Bergman kernels for Paley–Wiener spaces and Nazarov's proof of the Bourgain–Milman theorem*, Pure Appl. Math. Q., 2022) and the Mastrantonis–Rubinstein work extending the Nazarov mechanism to the non-symmetric setting are the most active analytic direction; the aim is to identify the exact loss term in the $\bar\partial$-estimate. *(frontier — verify current constants)*
- **Symplectic route.** Artstein-Avidan, Karasev and Ostrover (*Duke Math. J.* 163, 2014) showed that Viterbo's conjecture, comparing capacity and volume of convex domains in $\mathbb{R}^{2n}$, implies Mahler's for $K \times K^\circ$. Haim-Kislev and Ostrover announced a counterexample to Viterbo's conjecture in 2024 (arXiv:2405.16513), which removes this as a route to a proof but does **not** bear on Mahler's conjecture itself. *(frontier — verify)*
- **Equipartition / combinatorial geometry.** Extending the four-part cone equipartition of the $n=3$ proof to $n = 4$ is an explicit programme of the Fradelizi–Meyer–Zvavitch school (Kent State, Université Gustave Eiffel, Technion, UNAM).
- **Stability and rigidity.** Quantitative stability versions — "if $v(K)$ is close to $4^n/n!$ then $K$ is close to a Hanner polytope" — are being pursued for zonoids and unconditional bodies.
- **Computational search.** Randomised and semidefinite searches over polytopes with $\le 2n+2$ vertices in $n = 4,5$ have found no counterexample and no local minimum other than Hanner polytopes.

## 8. Future Work

- Construct a monotone flow on symmetric convex bodies with Hanner polytopes as attractors — the single most-cited desideratum.
- Isolate and remove the polytopal loss in the Hörmander/Bergman estimate; even improving $\pi/4$ to $1$ for unconditional-adjacent classes would be significant.
- Prove the *general* (non-symmetric) case in $n = 3$, currently the smallest fully open instance.
- Classify all local minima of $v$ in low dimensions; a proof that Hanner polytopes are the *only* local minima in $n=4$ would strongly constrain any counterexample.
- Develop a stability theory strong enough to convert "no local minima elsewhere" into a global statement.

## 9. Key References

- **[Foundational]** K. Mahler. *Ein Übertragungsprinzip für konvexe Körper.* Časopis pro pěstování matematiky a fysiky **68** (1939), 93–102.
- **[Foundational]** K. Mahler. *Ein Minimalproblem für konvexe Polygone.* Mathematica (Zutphen) B **7** (1939), 118–127.
- **[Foundational]** L. A. Santaló. *Un invariante afín para los cuerpos convexos del espacio de n dimensiones.* Portugaliae Mathematica **8** (1949), 155–161.
- **[Foundational]** J. Bourgain, V. D. Milman. *New volume ratio properties for convex symmetric bodies in $\mathbb{R}^n$.* Inventiones Mathematicae **88** (1987), 319–340. [DOI](https://doi.org/10.1007/bf01388911)
- **[Foundational]** S. Reisner. *Zonoids with minimal volume-product.* Mathematische Zeitschrift **192** (1986), 339–346. [DOI](https://doi.org/10.1007/bf01164009)
- **[Foundational]** J. Saint-Raymond. *Sur le volume des corps convexes symétriques.* Séminaire d'Initiation à l'Analyse, Univ. Paris VI, 1980/81.
- **[SOTA]** H. Iriyeh, M. Shibata. *Symmetric Mahler's conjecture for the volume product in the three-dimensional case.* Duke Mathematical Journal **169** (2020), 1077–1134. [DOI](https://doi.org/10.1215/00127094-2019-0072)
- **[SOTA]** M. Fradelizi, A. Hubard, M. Meyer, E. Roldán-Pensado, A. Zvavitch. *Equipartitions and Mahler volumes of symmetric convex bodies.* American Journal of Mathematics **144** (2022), 1201–1219. [DOI](https://doi.org/10.1353/ajm.2022.0027)
- **[SOTA]** G. Kuperberg. *From the Mahler conjecture to Gauss linking integrals.* Geometric and Functional Analysis **18** (2008), 870–892. [DOI](https://doi.org/10.1007/s00039-008-0669-4)
- **[SOTA]** F. Nazarov. *The Hörmander proof of the Bourgain–Milman theorem.* In: Geometric Aspects of Functional Analysis, Lecture Notes in Mathematics **2050**, Springer, 2012, 335–343. [DOI](https://doi.org/10.1007/978-3-642-29849-3_20)
- **[SOTA]** F. Nazarov, F. Petrov, D. Ryabogin, A. Zvavitch. *A remark on the Mahler conjecture: local minimality of the unit cube.* Duke Mathematical Journal **154** (2010), 419–430. [DOI](https://doi.org/10.1215/00127094-2010-042)
- **[SOTA]** S. Artstein-Avidan, R. Karasev, Y. Ostrover. *From symplectic measurements to the Mahler conjecture.* Duke Mathematical Journal **163** (2014), 2003–2022. [DOI](https://doi.org/10.1215/00127094-2794999)
- **[SOTA]** F. Barthe, M. Fradelizi. *The volume product of convex bodies with many hyperplane symmetries.* American Journal of Mathematics **135** (2013), 311–347. [DOI](https://doi.org/10.1353/ajm.2013.0018)
- **[Survey]** M. Fradelizi, M. Meyer, A. Zvavitch. *Volume product.* In: Harmonic Analysis and Convexity (A. Koldobsky, A. Volberg, eds.), De Gruyter, 2023.
- **[Survey]** R. Schneider. *Convex Bodies: The Brunn–Minkowski Theory.* 2nd expanded ed., Cambridge University Press, 2014.
- **[Reference]** C. M. Petty. *Affine isoperimetric problems.* Annals of the New York Academy of Sciences **440** (1985), 113–127.

## 10. Worked Example / Concrete Special Case

Take $n = 2$ and compare three symmetric bodies; the conjectured minimum is $4^2/2! = 8$ and the Santaló maximum is $|B_2^2|^2 = \pi^2 \approx 9.8696$.

**(a) Square.** $K = [-1,1]^2$, $|K| = 4$. Its polar is $K^\circ = \{|y_1| + |y_2| \le 1\}$, of area $2$. So $v(K) = 8$ — the conjectured minimum.

**(b) Regular-type hexagon.** Let $H$ be the hexagon with vertices, in cyclic order,
$$(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).$$
Shoelace: each consecutive pair contributes $x_i y_{i+1} - x_{i+1} y_i = 1$, six pairs, so $|H| = \tfrac12 \cdot 6 = 3$.

The polar is cut out by one linear constraint per vertex of $H$:
$$y_1 \le 1,\quad y_1 + y_2 \le 1,\quad y_2 \le 1,\quad -y_1 \le 1,\quad -y_1 - y_2 \le 1,\quad -y_2 \le 1 .$$
Intersecting consecutive constraints gives the vertices of $H^\circ$:
$$(1,0),\ (0,1),\ (-1,1),\ (-1,0),\ (0,-1),\ (1,-1),$$
and the same shoelace computation gives $|H^\circ| = 3$. Hence
$$v(H) = 3 \cdot 3 = 9 .$$
Note $8 < 9 < \pi^2$: the hexagon sits strictly between the conjectured minimiser and the ball, consistent with both Mahler's bound and Blaschke–Santaló.

**(c) Triangle (non-symmetric).** For the triangle $T$ with vertices $(2,-1),(-1,2),(-1,-1)$ the centroid is the origin and $|T| = \tfrac92$. Its polar is the triangle with vertices $(-1,-1),(2,-1),(-1,2)$ scaled by $-\tfrac12$, i.e. $T^\circ = -\tfrac12 T$, of area $\tfrac14 \cdot \tfrac92 = \tfrac98$. So
$$\mathcal{P}(T) = \tfrac92 \cdot \tfrac98 = \tfrac{81}{16} = 5.0625 .$$
This is **below** the symmetric bound $8$, which is exactly why the two conjectures have different constants. Applying the general formula, $(n+1)^{n+1}/(n!)^2 = 3^3/(2!)^2 = 27/4 = 6.75$; the discrepancy is the reminder that $\mathcal{P}$ must be minimised over the choice of interior point — with the *Santaló point* rather than the centroid the value rises to $27/4$, attaining the general planar minimum.

The essential difficulty is visible already here: the minimiser in (a) is a polytope with non-smooth boundary and non-strictly-convex polar, while every analytic proof technique of Section 5 is sharp only for smooth, strictly convex bodies such as the disc.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*