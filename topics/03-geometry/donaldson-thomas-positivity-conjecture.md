---
id: 03-geometry/donaldson-thomas-positivity-conjecture
title: "Donaldson-Thomas Positivity Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Donaldson-Thomas Positivity Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/donaldson-thomas-positivity-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Donaldson-Thomas (DT) Positivity Conjecture is a foundational proposition in enumerative geometry, representation theory, and string theory. It asserts that the refined (or motivic) Donaldson-Thomas invariants—which mathematically formalize the physical counts of BPS states in string theory—are Laurent polynomials with exclusively non-negative integer coefficients for any 3-dimensional Calabi-Yau (CY3) category. 

More precisely, when the generating series of the moduli spaces of objects (e.g., quiver representations, or coherent sheaves on a CY3 fold) is factorized via the plethystic exponential, the resulting terms $\Omega_{\mathbf{d}}(q^{1/2})$ (known as the BPS invariants or Bogomolov-Kontsevich invariants) are a priori only guaranteed to be rational functions. The Integrality Conjecture states that they are polynomials $\Omega_{\mathbf{d}}(q^{1/2}) \in \mathbb{Z}[q^{\pm 1/2}]$. The Positivity Conjecture strengthens this by claiming that $\Omega_{\mathbf{d}}(q^{1/2}) \in \mathbb{Z}_{\ge 0}[q^{\pm 1/2}]$. Geometrically, this non-negativity is conjectured to hold because these invariants should represent the graded dimensions of a well-defined vector space: the compactly supported cohomology of the space of BPS states.

## 2. Mathematical Foundations

Let $\mathcal{C}$ be a 3-dimensional Calabi-Yau (CY3) category over $\mathbb{C}$. The most tractable and heavily studied class of CY3 categories arises from a finite quiver with potential $(Q, W)$. 

Let $Q = (Q_0, Q_1)$ be a quiver with vertex set $Q_0$ and arrow set $Q_1$. A potential $W$ is a formal linear combination of cyclic paths in $Q$, so $W \in \mathbb{C}Q/[\mathbb{C}Q, \mathbb{C}Q]$. For a fixed dimension vector $\mathbf{d} = (d_i)_{i \in Q_0} \in (\mathbb{Z}_{\ge 0})^{Q_0}$, the space of representations is the affine variety:
$$ \operatorname{Rep}(Q, \mathbf{d}) = \bigoplus_{a \in Q_1} \operatorname{Hom}(\mathbb{C}^{d_{s(a)}}, \mathbb{C}^{d_{t(a)}}) $$
This variety is acted upon by the gauge group $G_{\mathbf{d}} = \prod_{i \in Q_0} \operatorname{GL}(d_i, \mathbb{C})$ via change of basis, resulting in the moduli stack of representations $\mathcal{M}_{\mathbf{d}} = \operatorname{Rep}(Q, \mathbf{d}) / G_{\mathbf{d}}$.

The potential $W$ induces a gauge-invariant regular function $\operatorname{Tr} W_{\mathbf{d}}: \operatorname{Rep}(Q, \mathbf{d}) \to \mathbb{C}$ defined by taking the trace of the cyclic compositions. To define the refined DT invariants, one applies the Deligne-Goresky-MacPherson functor of vanishing cycles, $\phi_{\operatorname{Tr} W_{\mathbf{d}}}$, to the constant perverse sheaf $\underline{\mathbb{Q}}_{\mathcal{M}_{\mathbf{d}}}$. 

The compactly supported BPS cohomology is defined in the derived category of mixed Hodge modules (or constructible sheaves) as:
$$ \mathcal{H}_{\mathbf{d}} = H_c^{\bullet}(\mathcal{M}_{\mathbf{d}}, \phi_{\operatorname{Tr} W_{\mathbf{d}}}(\underline{\mathbb{Q}}_{\mathcal{M}_{\mathbf{d}}}) \otimes \mathbb{L}^{-\dim G_{\mathbf{d}}/2}) $$
where $\mathbb{L}^{1/2}$ is the formal Tate twist (often denoted by the parameter $q^{1/2}$). 

In the Grothendieck ring of mixed Hodge modules $\operatorname{K}_0(\mathrm{MHM}(\mathrm{pt}))$, we construct the motivic Donaldson-Thomas generating series:
$$ \mathcal{Z}(t) = \sum_{\mathbf{d} \in (\mathbb{Z}_{\ge 0})^{Q_0}} [\mathcal{H}_{\mathbf{d}}] t^{\mathbf{d}} $$
The Kontsevich-Soibelman wall-crossing formula dictates that this series factorizes into a plethystic exponential:
$$ \mathcal{Z}(t) = \operatorname{Sym} \left( \sum_{\mathbf{d} \neq 0} \frac{\Omega_{\mathbf{d}}(q^{1/2})}{q^{1/2} - q^{-1/2}} t^{\mathbf{d}} \right) $$
Here, the plethystic operator $\operatorname{Sym}$ for a graded vector space $V$ gives the symmetric algebra $\bigoplus_{n=0}^{\infty} \operatorname{Sym}^n(V)$. 

The **Integrality Conjecture** states that the refined BPS invariants $\Omega_{\mathbf{d}}(q^{1/2})$ lie in $\mathbb{Z}[q^{\pm 1/2}]$. 
The **Positivity Conjecture** states that $\Omega_{\mathbf{d}}(q^{1/2}) \in \mathbb{Z}_{\ge 0}[q^{\pm 1/2}]$. This implies the existence of a $\mathbb{Z}$-bigraded underlying BPS vector space $\mathcal{H}_{\mathrm{BPS}, \mathbf{d}}$ such that $\Omega_{\mathbf{d}}(q^{1/2}) = \sum_{k} \dim(\mathcal{H}_{\mathrm{BPS}, \mathbf{d}}^k) q^{k/2}$.

## 3. History & State of the Art (SOTA)

The enumerative theory of Calabi-Yau threefolds began with Richard Thomas in 1998, who defined the unrefined DT invariants as integer counts of stable ideal sheaves on a CY3 fold. In 2006, the MNOP conjecture linked these integer invariants to Gromov-Witten invariants, establishing their fundamental role in string theory.

The modern landscape was shaped in 2008 when Maxim Kontsevich and Yan Soibelman introduced *motivic* and *refined* DT invariants to systematically understand wall-crossing phenomena. They introduced the plethystic factorization framework and formulated the Integrality Conjecture. 

In 2011, Alexander Efimov proved the Integrality Conjecture for the general class of quivers with potential. Concurrently, Hausel, Letellier, and Rodriguez-Villegas proved the positivity of Kac polynomials for quivers (which correspond to DT invariants of a quiver without potential).

The major milestone for the Positivity Conjecture was achieved in 2015 by Ben Davison and Sven Meinhardt. By leveraging Cohomological Hall Algebras (CoHAs) and the Beilinson-Bernstein-Deligne-Gabber (BBDG) Decomposition Theorem, they proved that for any quiver with a polynomial potential, the Positivity Conjecture holds. 

While the problem for quivers with potential is fully resolved, the SOTA focuses on extending this to arbitrary, non-quiver CY3 categories, such as the bounded derived category of coherent sheaves $D^b \mathrm{Coh}(X)$ on a compact CY3 fold $X$.

## 4. Partial Results / Verified Cases

The Positivity Conjecture is considered **partially-solved** because it has been rigorously proven for several foundational, massive classes of CY3 categories, though it remains open for general Artin stacks over arbitrary CY3 manifolds.

- **Quivers with Potential:** Fully resolved by Davison and Meinhardt (2015). They proved that the CoHA defined by Kontsevich and Soibelman satisfies a Poincaré-Birkhoff-Witt (PBW) theorem, directly yielding a bigraded BPS Lie algebra whose enveloping algebra matches the DT generating series.
- **Kac Polynomials (Empty Potential):** For a quiver $Q$ with zero potential, the unrefined BPS invariants are exactly the Kac polynomials, which count absolutely indecomposable representations over finite fields. Their positivity was proved by Hausel, Letellier, and Rodriguez-Villegas (2011).
- **Toric Calabi-Yau Threefolds:** Verified computationally and theoretically in many cases using the refined topological vertex formalism.
- **Local Surfaces (Categorical DT):** Recent advances by Yukinobu Toda have categorized the DT invariants for local $K3$ and abelian surfaces, providing a geometric framework that inherently implies positivity for rank-0 sheaves (1-dimensional torsion sheaves).

## 5. Principal Obstacles

The primary obstruction to proving the Positivity Conjecture for a general CY3 category $\mathcal{C}$ (e.g., coherent sheaves on a compact CY3 fold) lies in the local-to-global geometry of the moduli stacks. 

For a quiver, the moduli stack $\mathcal{M}_{\mathbf{d}}$ is a global quotient $\operatorname{Rep}(Q, \mathbf{d}) / G_{\mathbf{d}}$, and the potential $\operatorname{Tr} W_{\mathbf{d}}$ is a *globally defined* regular function. This allows the direct, global application of the vanishing cycle functor and the construction of a Cohomological Hall Algebra via pushforward maps.

For a general CY3 category, the moduli stack of objects $\mathfrak{M}$ is a complex Artin stack. By the Darboux theorem for shifted symplectic geometry (Brav, Bussi, and Joyce), $\mathfrak{M}$ carries a $-1$-shifted symplectic structure, meaning it can only be *locally* modeled as the critical locus $\operatorname{Crit}(f: U \to \mathbb{A}^1)$ of a holomorphic function $f$ on a smooth scheme $U$. 

To define the DT invariant, one must glue the local perverse sheaves of vanishing cycles $\phi_f(\underline{\mathbb{Q}}_U)$ across the stack. This requires a highly non-trivial "orientation data" (a choice of square root of the dualizing complex). Even assuming orientation data exists, we lack a global ambient smooth space and a global function. Consequently, one cannot construct a global CoHA multiplication using standard intersection cohomology and BBDG decomposition theorem techniques. Traditional methods of algebraic topology fail because the local charts of the $-1$-shifted symplectic stack are highly non-unique and do not easily admit a global convolution diagram.

## 6. The Gap

The exact boundary separating the proven cases (Section 4) and the general conjecture (Section 1) is the transition from **global critical loci** to **formal/local critical loci**. 

To cross this mathematical barrier, one must generalize the PBW theorem of Cohomological Hall Algebras to a setting where no global representation space exists. The required leap is the construction of a robust theory of *global BPS sheaves* directly on arbitrary $-1$-shifted symplectic Artin stacks, bypassing the need for a global potential function, and proving that these sheaves are pure Hodge modules whose cohomology exhibits the desired positivity. 

## 7. Current Research (as of June 2026)

Active research heavily involves shifting the problem from numerical invariants to *Categorical Donaldson-Thomas Theory*.
- **Categorical DT Theory:** Led heavily by Y. Toda and M. Porta, this school of thought attempts to bypass numerical positivity by defining the BPS invariants directly as objects in a triangulated category (or $\infty$-category) of motives or matrix factorizations. If the invariant is fundamentally a vector space or category, its dimension/rank is automatically positive.
- **Shifted Symplectic Geometry:** Building on Joyce's foundational work, researchers are utilizing derived algebraic geometry to define global CoHAs for local surfaces and specific compact CY3s. 
- *(frontier — verify)* **W-Algebras and BPS Lie Algebras:** Emerging preprints are attempting to identify the hypothetical BPS Lie algebra of compact CY3s with specific vertex operator algebras and W-algebras arising in 2d conformal field theory, offering a Lie-theoretic path to proving non-negativity.

## 8. Future Work

Leading mathematicians suggest that resolving the general Positivity Conjecture requires abandoning the direct attack via vanishing cycles. Future pathways include:
1. **Geometric Langlands Connections:** Interpreting the CoHA of a CY3 category as a generalization of the spherical Hecke algebra, utilizing the geometric Satake equivalence to naturally deduce positivity from representation theory.
2. **CY4 Categories:** Connecting CY3 DT invariants to the Borisov-Joyce invariants of CY4 categories. By defining real derived stacks and utilizing $O(n)$-gauge theories, researchers hope to embed the CY3 problem into a CY4 setting where different index theorems might naturally manifest positivity.

## 9. Key References

- **[Foundational]** Kontsevich, M., & Soibelman, Y. *Stability structures, motivic Donaldson-Thomas invariants and cluster transformations*. arXiv:0811.2435, 2008.
- **[SOTA / Recent]** Davison, B., & Meinhardt, S. *Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras*. Inventiones mathematicae, 2015.
- **[Foundational]** Efimov, A. I. *Quantum cluster variables via vanishing cycles*. arXiv:1112.3601, 2011.
- **[Survey]** Toda, Y. *Survey of categorical Donaldson-Thomas theory*. Proceedings of the International Congress of Mathematicians (ICM), 2022.

## 10. Worked Example / Concrete Special Case

To ground this abstraction, consider the **$m$-Kronecker quiver** $K_m$ and its Calabi-Yau 3-fold completion.

Let $K_m$ be the quiver with two vertices, $1$ and $2$, and $m$ parallel arrows $x_1, \dots, x_m$ from $1 \to 2$. The potential is $W=0$. To study this in a CY3 framework, we construct its CY3 completion $\widetilde{K}_m$ by adding $m$ reverse arrows $y_1, \dots, y_m: 2 \to 1$, and one loop at each vertex: $z_1$ at vertex $1$, and $z_2$ at vertex $2$. The canonical CY3 potential is:
$$ W = \sum_{i=1}^m (x_i y_i z_1 - y_i x_i z_2) $$

Let us compute the refined BPS invariant $\Omega_{\mathbf{d}}(q^{1/2})$ for the simplest non-trivial dimension vector $\mathbf{d} = (1,1)$. 
The representation space of $\widetilde{K}_m$ for $\mathbf{d} = (1,1)$ is $\mathbb{C}^m \times \mathbb{C}^m \times \mathbb{C} \times \mathbb{C}$, parameterized by scalars $(x_i, y_i, z_1, z_2)$.
The gauge group is $G = \mathbb{C}^* \times \mathbb{C}^*$. The diagonal $\mathbb{C}^*$ acts trivially, leaving an effective $\mathbb{C}^*$ action via $(t, 1) \cdot (x_i, y_i, z_1, z_2) = (t x_i, t^{-1} y_i, z_1, z_2)$.

Taking the derivatives of the trace of $W$ to find the critical locus (which governs the vanishing cycles), we get:
1. $\partial_{z_1} W = \sum_{i=1}^m x_i y_i = 0$
2. $\partial_{z_2} W = -\sum_{i=1}^m y_i x_i = 0$ (identical to the first condition)
3. $\partial_{x_i} W = y_i(z_1 - z_2) = 0$
4. $\partial_{y_i} W = x_i(z_1 - z_2) = 0$

On the locus of absolutely indecomposable representations (the BPS states), not all $x_i$ can be zero simultaneously. Therefore, condition 4 forces $z_1 = z_2$. The equations reduce simply to $\sum x_i y_i = 0$. 
By the dimensional reduction theorem in DT theory, the compactly supported cohomology of the vanishing cycles for the CY3 completion $\widetilde{K}_m$ exactly collapses to the intersection cohomology of the moduli space of the original quiver $K_m$. 

For the original $m$-Kronecker quiver $K_m$, the space of $(1,1)$ representations is $\mathbb{A}^m$ (just the coordinates $x_1, \dots, x_m$). The indecomposable representations are those where at least one $x_i \neq 0$, which gives $\mathbb{A}^m \setminus \{0\}$. 
Quotienting by the effective $\mathbb{C}^*$ gauge action, the moduli space of BPS states is exactly the complex projective space:
$$ \mathcal{M}_{(1,1)} = (\mathbb{A}^m \setminus \{0\}) / \mathbb{C}^* \cong \mathbb{P}^{m-1} $$

The refined BPS invariant $\Omega_{(1,1)}(q)$ is the Poincaré polynomial of this moduli space:
$$ \Omega_{(1,1)}(q^{1/2}) = \sum_{k=0}^{m-1} \dim H^{2k}(\mathbb{P}^{m-1}, \mathbb{Q}) q^k = 1 + q + q^2 + \dots + q^{m-1} $$
All coefficients in this polynomial are exactly $1$. Since $1 \ge 0$, this explicitly verifies the Positivity Conjecture for this CY3 geometry. The positive coefficients correspond perfectly to the 1-dimensional Betti numbers of the projective space of BPS states.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*