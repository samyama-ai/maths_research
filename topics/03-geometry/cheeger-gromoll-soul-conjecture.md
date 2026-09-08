---
id: 03-geometry/cheeger-gromoll-soul-conjecture
title: "Cheeger-Gromoll Soul Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cheeger-Gromoll Soul Conjecture

> **Topic:** 03-geometry · **ID:** `03-geometry/cheeger-gromoll-soul-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The **Cheeger-Gromoll Soul Conjecture** posits a profound topological rigidity for complete, non-compact Riemannian manifolds that exhibit non-negative curvature everywhere, provided there is at least one point of strictly positive curvature.

Specifically, let $(M, g)$ be a complete, connected, non-compact Riemannian manifold of dimension $n$ with non-negative sectional curvature $K \ge 0$ everywhere. The conjecture states that if there exists at least one point $p \in M$ where the sectional curvature is strictly positive in all planar directions (i.e., $K(\pi) > 0$ for all $2$-planes $\pi \subset T_p M$), then $M$ is diffeomorphic to the Euclidean space $\mathbb{R}^n$.

This conjecture is intrinsically linked to the foundational **Soul Theorem** (Cheeger and Gromoll, 1972), which guarantees that any complete, non-compact Riemannian manifold with $K \ge 0$ contains a compact, totally geodesic, and totally convex submanifold $S \subset M$ (the "soul"), such that $M$ is diffeomorphic to the normal bundle $\nu(S)$. Within this framework, the Soul Conjecture is equivalent to the statement that the strict positivity condition $K(p) > 0$ at a single point forces the soul $S$ to be zero-dimensional (a single point), meaning its normal bundle is $\mathbb{R}^n$.

## 2. Mathematical Foundations

The problem is rooted in global Riemannian geometry, leveraging comparison theorems to extract topological data from local curvature bounds.

Let $(M, g)$ be a Riemannian manifold with the Levi-Civita connection $\nabla$. The **Riemann curvature tensor** is defined for vector fields $X, Y, Z$ as:
$$R(X,Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z$$
For any point $x \in M$ and any 2-plane $\pi \subset T_xM$ spanned by orthonormal vectors $X, Y$, the **sectional curvature** is:
$$K(\pi) = g(R(X, Y)Y, X)$$
The condition $K \ge 0$ requires $K(\pi) \ge 0$ for all $x \in M$ and all $2$-planes $\pi$.

Because $M$ is assumed complete, the Hopf-Rinow theorem ensures that any two points can be connected by a length-minimizing geodesic, and that geodesics can be extended indefinitely. A **ray** is a unit-speed geodesic $\gamma: [0, \infty) \to M$ that minimizes distance between any two of its points, meaning $d(\gamma(t), \gamma(s)) = |t - s|$ for all $t, s \ge 0$. Because $M$ is non-compact, every point $x \in M$ is the starting point of at least one ray.

For a given ray $\gamma$, the associated **Busemann function** $b_\gamma : M \to \mathbb{R}$ measures the "distance from infinity" and is defined as:
$$b_\gamma(x) = \lim_{t \to \infty} \big( t - d(x, \gamma(t)) \big)$$
Under the assumption $K \ge 0$, Busemann functions are convex and continuous.

A subset $C \subset M$ is **totally convex** if, for any two points $x, y \in C$, every geodesic connecting $x$ and $y$ lies entirely within $C$. By taking the intersection of sub-level sets of Busemann functions over all rays, Cheeger and Gromoll constructed a sequence of compact, totally convex sets $C_t$ that exhaust $M$. The minimal set of this exhaustion is the **soul**, $S$.

Furthermore, there exists a canonical, distance-nonincreasing map known as **Sharafutdinov's retraction** $P: M \to S$. The core mathematical foundation of the conjecture relies on analyzing the metric and smooth properties of $P$.

## 3. History & State of the Art (SOTA)

The history of the Soul Conjecture represents a multi-decade quest to understand the global implications of localized positive curvature.

- **1935 (Cohn-Vossen):** Established the theorem for surfaces ($n=2$). A complete, non-compact surface with $K \ge 0$ everywhere and strictly positive curvature at one point is diffeomorphic to $\mathbb{R}^2$.
- **1969 (Gromoll and Meyer):** Generalized this behavior to higher dimensions, but under the much stricter assumption that $K > 0$ *everywhere*. They proved that complete, open manifolds of strictly positive curvature are diffeomorphic to $\mathbb{R}^n$.
- **1972 (Cheeger and Gromoll):** Published "On the structure of complete manifolds of nonnegative curvature," establishing the Soul Theorem for $K \ge 0$ and articulating the Soul Conjecture. They hypothesized that $K>0$ at a single point is sufficient to shrink the soul to a point.
- **1994 (Grigori Perelman):** Settled the conjecture affirmatively in a celebrated, astonishingly brief 4-page paper. Perelman elegantly bypassed decades of PDE-heavy analytic obstruction by deploying a direct, synthetic geometric argument using Jacobi fields. He demonstrated that Sharafutdinov's retraction $P: M \to S$ is a Riemannian submersion.
- **Post-1994 SOTA:** The theorem stands fully proven. Subsequent research has utilized Perelman's flat-strip geometric insights to study manifolds with lower Ricci curvature bounds and singular Alexandrov spaces.

## 4. Partial Results / Verified Cases

Prior to Perelman's definitive proof in 1994, the conjecture was verified only in several highly restricted, specialized cases:

- **Dimension 2 ($n=2$):** Solved by Cohn-Vossen via the Gauss-Bonnet theorem, leveraging the fact that the total curvature of a non-compact surface dictates its Euler characteristic, restricting the topology to the plane.
- **Strictly Positive Curvature ($K > 0$ everywhere):** The Gromoll-Meyer theorem (1969) successfully proved that universally positive curvature prevents the existence of closed geodesics, forcing the soul to be a point.
- **Rotational Symmetry / Warped Products:** Manifolds possessing a pole (a point where the exponential map is a global diffeomorphism) and global $O(n)$-symmetry automatically satisfy the conjecture, as the symmetry forces the exhaustion sets to be perfect spheres.
- **Codimension 1 Souls:** It was mathematically verified that if the soul $S$ has codimension 1, then the manifold must be diffeomorphic to $S \times \mathbb{R}$. In this scenario, the presence of a point with $K > 0$ strictly prohibits a flat cross-section, reducing the soul to a point and forcing $S \times \mathbb{R} \cong \mathbb{R}$.
- **Dimension 3 ($n=3$):** Explored using early iterations of Hamilton’s Ricci flow. For $K \ge 0$, specific topological restrictions in dimension 3 made the analysis of the soul's codimension tractable, though Ricci flow typically requires strict positivity to avoid singularity formation.

## 5. Principal Obstacles

The persistence of the Soul Conjecture as an open problem for 22 years stemmed from the localized nature of the core assumption.

1. **Local vs. Global Obstruction:** The condition $K(p) > 0$ is localized to a single, arbitrary point $p \in M$. Traditional global theorems in Riemannian geometry (such as the Myers Theorem or the Splitting Theorem) require curvature bounds to be maintained everywhere or asymptotically. A single point of positive curvature is typically "swallowed" by global volume variations, making it impossible to force a rigid structure using standard integration techniques like the Bochner technique.
2. **Lack of Smoothness in Busemann Functions:** The construction of the soul relies on intersecting sub-level sets of Busemann functions $\{b_\gamma \le c\}$. However, the distance function to a ray is generally only Lipschitz and almost everywhere differentiable, not $C^\infty$. Consequently, the boundary of the convex sets (and the resulting soul) lacks the necessary smoothness to apply standard variational formulas of curvature directly without sophisticated approximation techniques.
3. **Rigidity of the Retraction:** Sharafutdinov's retraction $P: M \to S$ was known to be distance-nonincreasing, $d(P(x), P(y)) \le d(x, y)$, but it was generally only Hölder continuous. The lack of strict smoothness made it exceptionally difficult to propagate the positive curvature at point $p$ down to the soul $S$. Toponogov's comparison theorem provides triangle bounds, but could not lift the localized strict curvature constraint to the global bundle.

## 6. The Gap

The precise mathematical boundary between what was proven and the full conjecture lay in the metric properties of the Sharafutdinov retraction $P: M \to S$.

If one could prove that $P$ is a **Riemannian submersion**—a smooth map whose differential preserves the lengths of horizontal vectors—the conjecture would immediately follow via the O'Neill formulas. A Riemannian submersion over a totally geodesic submanifold implies that the horizontal lift of any geodesic in $S$ traces out a "flat strip" (a totally geodesic, flat 2-dimensional half-plane) in $M$. If $S$ had positive dimension, one could take a geodesic in $S$, lift it to pass through the point $p$ (where $K(p)>0$), and obtain a flat 2-plane at $p$. This would yield $K(\pi) = 0$ for that specific plane, directly contradicting $K > 0$ in all directions at $p$.

The gap was proving the existence of these flat strips without assuming $P$ is globally smooth. Perelman bridged this gap by proving the "Flat Strip Theorem". By analyzing the Jacobi equation $J''(t) + R(J, \dot{\gamma})\dot{\gamma} = 0$ along geodesics orthogonal to the sublevel sets of the Busemann function, he showed that the norm $|J(t)|$ is convex and non-decreasing. If the field does not diverge, it must be parallel, yielding zero curvature and explicitly constructing the flat strip without requiring $P$ to be a smooth submersion a priori.

## 7. Current Research (as of June 2026)

With the conjecture affirmatively closed, contemporary geometric research *(as of June 2026)* orbits around generalized, singular, and less rigid environments:

- **Metric Measure and RCD Spaces:** The most active area of research involves generalizing the Cheeger-Gromoll theory to singular spaces with curvature bounded below, specifically Riemannian Curvature-Dimension (RCD) spaces and Alexandrov spaces. Current groups are investigating if non-compact Alexandrov spaces with non-negative curvature admit a topological "soul" and whether Sharafutdinov retractions exist in metric-measure settings. *(frontier — verify)*
- **Non-negative Ricci Curvature ($\text{Ric} \ge 0$):** The soul theorem fails profoundly for $\text{Ric} \ge 0$. Sha and Yang, and later Meng and Wang, constructed complete non-compact manifolds with $\text{Ric} > 0$ that possess infinite topological type. Current research aims to establish bounds on the Betti numbers or find "virtual" souls for manifolds with $\text{Ric} \ge 0$.
- **Moduli Space of Non-negatively Curved Metrics:** Understanding the topology of the space of all complete metrics with $K \ge 0$ on $\mathbb{R}^n$. Researchers at the Max Planck Institute and SUNY Stony Brook are exploring whether this moduli space is contractible or if it possesses infinitely many connected components.
- **Positive Scalar Curvature:** Examining analogies of the soul theorem for manifolds with positive scalar curvature, integrating index theory and the Dirac operator to find topological obstructions on open spin manifolds.

## 8. Future Work

Future mathematical pathways articulated by leaders in differential geometry include:

- **Classification of Souls:** While any compact manifold can be a soul of *some* metric with $K \ge 0$, a major open question remains: precisely which compact manifolds can serve as souls of metrics that have strictly positive curvature in *certain* (but not all) directions?
- **Quantitative Soul Theorems:** Establishing sharp volume growth and diameter bounds in relation to the distance to the soul. How strictly does the geometry of the normal bundle behave at infinity as it flattens out?
- **Lorentzian Geometry and General Relativity:** Extending these ideas to spacetime geometry. The splitting theorems of Cheeger-Gromoll have exact analogs in relativity (e.g., the Geroch-Kronheimer-Penrose theorems), but a rigorous "Lorentzian Soul Conjecture" remains largely speculative, deeply connected to the strong cosmic censorship hypothesis and the topology of black hole horizons.

## 9. Key References

- **[Foundational]** J. Cheeger, D. Gromoll. *On the structure of complete manifolds of nonnegative curvature.* Annals of Mathematics, 96(3), 1972. [DOI](https://doi.org/10.2307/1970819)
- **[Foundational]** D. Gromoll, W. Meyer. *On complete open manifolds of positive curvature.* Annals of Mathematics, 90(1), 1969. [DOI](https://doi.org/10.2307/1970682)
- **[Foundational]** S. Cohn-Vossen. *Kürzeste Wege und Totalkrümmung auf Flächen.* Compositio Mathematica, 2, 1935.
- **[SOTA / Recent]** G. Perelman. *Proof of the soul conjecture of Cheeger and Gromoll.* Journal of Differential Geometry, 40(1), 1994. [DOI](https://doi.org/10.4310/jdg/1214455292)
- **[Survey]** P. Petersen. *Riemannian Geometry* (3rd Edition). Graduate Texts in Mathematics, Springer, 2016.
- **[Survey]** I. Belegradek. *Vector bundles with nonnegative sectional curvature.* Mathematische Annalen, 327(4), 2003.

## 10. Worked Example / Concrete Special Case

Consider the standard paraboloid $M \subset \mathbb{R}^3$, defined by the equation $z = x^2 + y^2$. This is a complete, non-compact 2-manifold. We will demonstrate how the soul formulation reduces $M$ to a point.

**Step 1: Curvature Check**
We calculate the Gaussian curvature $K$ using the standard parametrization $\mathbf{r}(u,v) = (u, v, u^2+v^2)$. 
The first fundamental form coefficients are $E = 1+4u^2$, $F = 4uv$, $G = 1+4v^2$. 
The second fundamental form coefficients are $L = 2/\sqrt{1+4(u^2+v^2)}$, $M=0$, $N = 2/\sqrt{1+4(u^2+v^2)}$.
The Gaussian (sectional) curvature is:
$$K = \frac{LN - M^2}{EG - F^2} = \frac{4}{(1 + 4(x^2 + y^2))^2}$$
Clearly, $K > 0$ for all $(x,y) \in \mathbb{R}^2$. This space satisfies the Soul Conjecture's premise of $K \ge 0$ with $K>0$ at least at one point (in fact, everywhere).

**Step 2: Rays and Busemann Function**
The rays on $M$ are the meridian geodesics extending to infinity from the origin $O=(0,0,0)$. Let $\gamma(t)$ be a ray moving outward. The Busemann function $b_\gamma(x)$ measures the depth from infinity. Because of the rotational symmetry, taking the minimum over all rays yields super-level sets $C_c = \{x \in M : b(x) \ge c\}$, which form a nested sequence of compact "caps" (topological disks).

**Step 3: Finding the Soul**
By intersecting these nested convex sets $C_c$, we exhaust the manifold, shrinking the surface down. Because $K > 0$ everywhere, the sets are strictly convex, meaning their boundary has strict geodesic curvature. When the parameter $c$ reaches its maximum bound, the intersection $\bigcap C_c$ inevitably reduces to a single point—the origin $O$. 

**Conclusion**
The soul $S$ of the paraboloid is the point $O$. The normal bundle of a 0-dimensional point in a 2-manifold is trivially $\mathbb{R}^2$. The exponential map from $O$ provides a global diffeomorphism from $T_O M \cong \mathbb{R}^2$ to the paraboloid $M$. This explicitly illustrates the conjecture: the existence of positive curvature forces the soul to be a 0-dimensional point, yielding $M \cong \mathbb{R}^2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*