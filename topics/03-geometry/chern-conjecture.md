---
id: 03-geometry/chern-conjecture
title: "Chern Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chern Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/chern-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Chern Conjecture on affine manifolds is a fundamental open problem in differential geometry relating the topology of a manifold to the geometric structures it can support. The conjecture states that any closed (compact and without boundary) affine manifold must have a vanishing Euler characteristic. 

Specifically, if $M$ is a real, compact, smooth $n$-dimensional manifold without boundary that admits a flat, torsion-free affine connection, then its topological Euler characteristic $\chi(M)$ must be exactly zero. A complete proof requires demonstrating that the existence of such an affine atlas intrinsically restricts the topological cellular decomposition or cohomology of the manifold, while a disproof would require constructing a pathological compact flat space with $\chi(M) \neq 0$.

## 2. Mathematical Foundations

An **affine manifold** is a smooth manifold $M^n$ equipped with a maximal atlas of charts $\mathcal{A} = \{(U_\alpha, \phi_\alpha)\}$ mapping into $\mathbb{R}^n$, where the transition maps $\phi_\beta \circ \phi_\alpha^{-1}: \phi_\alpha(U_\alpha \cap U_\beta) \to \phi_\beta(U_\alpha \cap U_\beta)$ are locally the restrictions of global affine transformations. An affine transformation of $\mathbb{R}^n$ is an element of the affine group $\operatorname{Aff}(\mathbb{R}^n) \cong \operatorname{GL}(n, \mathbb{R}) \ltimes \mathbb{R}^n$, acting via the mapping $x \mapsto Ax + b$.

By standard differential geometry, admitting an affine atlas is strictly equivalent to equipping the tangent bundle $TM$ with an affine connection $\nabla$ that is both:
1. **Flat:** The Riemann curvature tensor vanishes identically. For all vector fields $X, Y, Z$:
   $$ R^\nabla(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z = 0 $$
2. **Torsion-free:** The torsion tensor vanishes identically. For all vector fields $X, Y$:
   $$ T^\nabla(X, Y) = \nabla_X Y - \nabla_Y X - [X,Y] = 0 $$

Analytic continuation of the local charts yields a global **development map** $\operatorname{dev}: \widetilde{M} \to \mathbb{R}^n$, where $\widetilde{M}$ is the universal cover of $M$. Associated with $\operatorname{dev}$ is the **holonomy representation** $\rho: \pi_1(M) \to \operatorname{Aff}(\mathbb{R}^n)$, representing how the analytic continuation translates along closed loops. The development map is equivariant:
$$ \operatorname{dev}(\gamma \cdot \widetilde{x}) = \rho(\gamma) \operatorname{dev}(\widetilde{x}) \quad \forall \gamma \in \pi_1(M), \, \widetilde{x} \in \widetilde{M} $$

The **Euler characteristic** $\chi(M)$ is a topological invariant defined as the alternating sum of the Betti numbers $b_k = \dim H_k(M; \mathbb{R})$:
$$ \chi(M) = \sum_{k=0}^n (-1)^k b_k $$

The conjecture definitively posits:
$$ \text{If } M \text{ is a closed affine manifold, then } \chi(M) = 0. $$

## 3. History & State of the Art (SOTA)

The conjecture was formulated by Shiing-Shen Chern in 1955, inspired by his earlier seminal work on the generalized Gauss-Bonnet theorem. For a Riemannian manifold $(M, g)$, Chern had proven that the Euler characteristic could be computed via the integral of the Pfaffian of the Riemann curvature 2-form $\Omega$: $\chi(M) = \int_M \operatorname{Pf}(\Omega)$. If a Riemannian manifold is flat ($\Omega = 0$), the integral trivially vanishes. Chern hypothesized that the metric-free existence of a flat, torsion-free connection $\nabla$ must impose the same topological restriction, even though the standard Chern-Weil integral cannot be formed for non-metric connections.

Major historical milestones in the study of the conjecture include:
- **1955:** J. P. Benzécri resolved the conjecture for dimension 2, proving that the torus $T^2$ is the only closed surface admitting an affine structure.
- **1958:** John Milnor established the Milnor-Wood inequality, placing strict cohomological bounds on the Euler class of flat vector bundles and highlighting the rigid topological constraints induced by flat connections.
- **1975:** Bertram Kostant and Dennis Sullivan achieved a massive breakthrough by proving the conjecture for *complete* affine manifolds (where $\operatorname{dev}$ acts as a covering map onto $\mathbb{R}^n$).
- **1977:** John Smillie provided a cautionary topological counterexample for a related flat geometry: he constructed closed manifolds with flat *projective* connections (locally modeled on $\mathbb{RP}^n$) that have $\chi(M) \neq 0$. This established that the affine group $\operatorname{Aff}(\mathbb{R}^n)$ possesses highly specific rigid properties not shared by the broader projective group $\operatorname{PGL}(n+1, \mathbb{R})$.
- **2017:** Bruno Klingler advanced the SOTA by proving the conjecture for special affine manifolds (those whose transition maps preserve a volume form), utilizing modern non-abelian Hodge theory.

## 4. Partial Results / Verified Cases

The Chern conjecture has been rigorously resolved under several specific structural constraints:

1. **Dimension $n = 2$ (Benzécri, 1955):** A closed surface admits an affine structure if and only if it is diffeomorphic to the torus $T^2$. Since $\chi(T^2) = 0$, the conjecture holds unconditionally in dimension 2.
2. **Complete Affine Manifolds (Kostant & Sullivan, 1975):** If the affine manifold is geodesically complete (affine geodesics extend infinitely), the development map $\operatorname{dev}: \widetilde{M} \to \mathbb{R}^n$ is a diffeomorphism. The manifold is a quotient $M = \mathbb{R}^n / \Gamma$ where $\Gamma \subset \operatorname{Aff}(\mathbb{R}^n)$ acts properly discontinuously. Kostant and Sullivan used a spectral argument to show that $1$ is an eigenvalue of the linear part of the holonomy, forcing $\chi(M) = 0$.
3. **Special Affine Manifolds (Klingler, 2017):** If the holonomy representation $\rho$ lands within the special affine group $\operatorname{SL}(n, \mathbb{R}) \ltimes \mathbb{R}^n$, the manifold admits a parallel volume form. Klingler proved that all such compact manifolds have $\chi(M) = 0$.
4. **Radiant Affine Manifolds:** These are affine manifolds whose holonomy group fixes a common point in $\mathbb{R}^n$. Geometrically, this equates to the manifold possessing a global parallel radial vector field. The existence of any nowhere-vanishing vector field instantly guarantees $\chi(M) = 0$ via the Poincaré-Hopf theorem.
5. **Kähler Affine Manifolds:** If a compact complex manifold admits a holomorphic flat affine connection, characteristic class identities force its Euler characteristic to vanish.

## 5. Principal Obstacles

The primary obstacle preventing a general proof is the **inapplicability of Chern-Weil theory** to non-metric connections. The classical Gauss-Bonnet theorem relies on the Euler class $e(TM) \in H^n(M; \mathbb{R})$, constructed using a connection $\nabla$ that is compatible with a Riemannian metric $g$. For a metric connection, the curvature form $\Omega$ takes values in the skew-symmetric Lie algebra $\mathfrak{so}(n)$, which allows for the definition of the Pfaffian $\operatorname{Pf}(\Omega)$. 

However, a generic affine connection $\nabla$ takes values in $\mathfrak{gl}(n, \mathbb{R})$. While it is flat ($\Omega = 0$), it is **not metric-compatible**. To apply standard characteristic class theory, one must reduce the structure group of $TM$ from $\operatorname{GL}(n, \mathbb{R})$ to $\operatorname{O}(n)$, which corresponds to equipping $M$ with a Riemannian metric. Modifying the connection $\nabla$ to be metric-compatible introduces non-zero curvature. The new curvature form $\Omega_g$ is non-zero, and the integral $\int_M \operatorname{Pf}(\Omega_g)$ no longer trivially vanishes. The algebraic flatness of the affine connection is essentially lost when forced into a topological framework that demands orthogonal structure groups.

A severe secondary obstacle is the **pathological geometry of incomplete affine manifolds**. For incomplete affine manifolds, the development map $\operatorname{dev}$ is not a covering map. The image $\operatorname{dev}(\widetilde{M})$ can be a highly complex, non-convex open subset of $\mathbb{R}^n$ with fractal boundaries, and the fundamental group may act with dense orbits. This renders standard covering-space geometry, finite fundamental domain techniques, and discrete subgroup theory fundamentally unusable.

## 6. The Gap

The precise mathematical boundary lies exactly at the intersection of **incompleteness** and **volume-non-preservation**. The Kostant-Sullivan theorem covers the complete case, and Klingler's theorem covers the volume-preserving case. To fully resolve the general conjecture, researchers must prove that the purely algebraic translation dynamics of a compact quotient space strictly bound the top-dimensional cohomology. 

The gap requires either the construction of a secondary invariant that proves the twisted coefficient system determined by $L(\rho): \pi_1(M) \to \operatorname{GL}(n, \mathbb{R})$ intrinsically forces $H^n(M; \mathbb{R}) = 0$, or a dynamical proof that uncovers a nowhere-vanishing global vector field regardless of the pathologies of the development map.

## 7. Current Research (as of June 2026)

Active research heavily bridges ergodic theory, bounded cohomology, and geometric group theory to analyze the holonomy representation $\rho$.
- **Anosov Representations and Rigidity:** Researchers are studying the dynamics of the linear part of the holonomy. *(frontier — verify)* Recent preprints assert that if the linear holonomy group is highly irreducible, bounded cohomology can construct a trivializing class for the Euler bundle, placing strict upper bounds on characteristic numbers.
- **Affine Crystallography:** Research groups (expanding on the works of W. Goldman) are classifying domains of discontinuity for affine actions. By proving structural rigidity results about the boundary of the development image $\partial\operatorname{dev}(\widetilde{M})$, they aim to dynamically average local constant vector fields into a global nowhere-vanishing vector field.
- **Symplectic Affine Geometry:** Exploring the conjecture for Fedosov manifolds (manifolds admitting a symplectic form compatible with the flat connection). The symplectic constraint provides a structural middle-ground between Klingler’s volume-preserving case and the completely general statement.

## 8. Future Work

Leading geometric topologists suggest several pathways to attack the remaining cases:
- **Global Vector Field Construction via Dynamics:** Since $M$ is locally modeled on $\mathbb{R}^n$, it possesses a local notion of "constant vector fields". The grand challenge is to patch these together globally by averaging them over the holonomy group $\Gamma$. Future work must focus on identifying an invariant measure for pathological affine actions to permit this averaging.
- **Bounded Cohomology Obstructions:** Exploiting the bounded continuous cohomology of $\operatorname{GL}(n, \mathbb{R})$ to show that the Euler class, functioning as a primary topological obstruction, must lie in the kernel of the comparison map to standard de Rham cohomology, thus vanishing algebraically.
- **Metric Degeneration Limits:** Constructing sequences of Riemannian metrics $g_i$ whose Levi-Civita connections $\nabla^{g_i}$ converge to the flat affine connection $\nabla$ in a controlled Gromov-Hausdorff sense, analyzing the limit of $\int_M \operatorname{Pf}(\Omega_{g_i})$ as curvature concentrates on singular sets.

## 9. Key References

- **[Foundational]** Benzécri, J. P. *Sur les variétés affines et les espaces projectifs.* Bulletin de la Société Mathématique de France, 1955.
- **[Foundational]** Kostant, B. and Sullivan, D. *The Euler characteristic of an affine space form is zero.* Bulletin of the American Mathematical Society, 1975.
- **[Foundational]** Smillie, J. *Flat manifolds with non-zero Euler characteristic.* Commentarii Mathematici Helvetici, 1977.
- **[SOTA / Recent]** Klingler, B. *Chern's conjecture for special affine manifolds.* Annals of Mathematics, 2017.
- **[Survey]** Goldman, W. M. *Geometric structures on manifolds and varieties of representations.* Geometry and Topology, 2022.

## 10. Worked Example / Concrete Special Case

To physically ground the abstract statement and demonstrate how topology obstructs flat geometry, consider the contrast between the 2-dimensional sphere $S^2$ and the 2-dimensional torus $T^2$.

**The Torus $T^2$:**
Let $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$. It inherits an affine structure directly from the standard affine space $\mathbb{R}^2$. The charts are simply the projections of open sets in $\mathbb{R}^2$, and the transition functions are pure translations (which strictly belong to $\operatorname{Aff}(\mathbb{R}^2)$). The standard flat connection $\nabla$ on $\mathbb{R}^2$ descends smoothly to $T^2$. By basic algebraic topology, the Betti numbers of $T^2$ are $b_0=1$, $b_1=2$, and $b_2=1$. 
$$ \chi(T^2) = b_0 - b_1 + b_2 = 1 - 2 + 1 = 0. $$
This perfectly satisfies the Chern Conjecture. Because $T^2$ is geodesically complete, its compliance is guaranteed by the Kostant-Sullivan theorem.

**The Sphere $S^2$:**
The sphere $S^2$ has Betti numbers $b_0=1$, $b_1=0$, and $b_2=1$. 
$$ \chi(S^2) = 1 - 0 + 1 = 2 \neq 0. $$
According to the Chern Conjecture, $S^2$ cannot possibly admit an affine structure. We can verify this topological obstruction directly. 

Assume, for contradiction, that $S^2$ admits an affine connection $\nabla$. By definition, its curvature tensor vanishes: $R^\nabla = 0$. The holonomy group of $\nabla$ measures the parallel transport of tangent vectors around closed loops. Because $S^2$ is simply connected ($\pi_1(S^2) = 0$), every closed loop is smoothly contractible to a point. The absolute flatness of the connection ($R^\nabla = 0$) guarantees that parallel transport along any contractible loop is the identity mapping on the tangent space. Consequently, the holonomy group is perfectly trivial.

Choose an arbitrary base point $p \in S^2$ and an arbitrary basis $\{e_1, e_2\}$ for the tangent space $T_p S^2$. Because the holonomy is trivial, we can unambiguously parallel transport the vector $e_1$ along any path to any other point $x \in S^2$ to obtain a globally defined, smooth, nowhere-vanishing vector field $E_1(x)$ on $S^2$.

However, the Poincaré-Hopf Index Theorem dictates that the sum of the indices of the isolated zeros of any vector field on a manifold $M$ must equal its Euler characteristic:
$$ \sum_{x_i \text{ (zeros)}} \text{index}(x_i) = \chi(S^2) = 2. $$
This physical constraint means any vector field on $S^2$ must have at least one zero (commonly known as the Hairy Ball Theorem). The existence of the nowhere-vanishing parallel vector field $E_1(x)$ directly contradicts this topological absolute. Therefore, the initial assumption that $S^2$ admits a flat affine connection must be false. This mechanism vividly demonstrates the core philosophy of the Chern Conjecture: non-zero topology intrinsically obstructs flat geometry.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*