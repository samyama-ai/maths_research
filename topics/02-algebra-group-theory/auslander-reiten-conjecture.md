---
id: 02-algebra-group-theory/auslander-reiten-conjecture
title: "Auslander-Reiten Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Auslander-Reiten Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/auslander-reiten-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Auslander-Reiten conjecture is a fundamental open problem in homological algebra and representation theory concerning the characterization of projective modules via the vanishing of extension groups. 

Let $\Lambda$ be an Artin algebra, and let $M$ be a finitely generated left $\Lambda$-module. The conjecture states that if the extension groups vanish for all positive degrees, specifically:
$$ \text{Ext}^i_{\Lambda}(M, M \oplus \Lambda) = 0 \quad \text{for all } i \ge 1 $$
then $M$ must be a projective $\Lambda$-module. 

Equivalently, the condition can be split into two parts: if $\text{Ext}^i_{\Lambda}(M, M) = 0$ for all $i \ge 1$ (meaning $M$ has no higher self-extensions) and $\text{Ext}^i_{\Lambda}(M, \Lambda) = 0$ for all $i \ge 1$, then $M$ is projective. The conjecture essentially claims that only projective modules can be entirely rigid (self-extension free) while simultaneously having trivial extensions with the base algebra.

## 2. Mathematical Foundations

The problem lies at the intersection of module theory, homological algebra, and derived categories.

- **Artin Algebra:** An algebra $\Lambda$ over a commutative Artinian ring $R$ such that $\Lambda$ is a finitely generated $R$-module.
- **Projective Module:** A module $P$ is projective if the functor $\text{Hom}_{\Lambda}(P, -)$ is exact. For finitely generated modules over an Artin algebra, this is equivalent to $P$ being a direct summand of a free module $\Lambda^n$.
- **Projective Resolution and Syzygies:** Every finitely generated $\Lambda$-module $M$ admits a minimal projective resolution:
  $$ \cdots \to P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{d_0} M \to 0 $$
  The $i$-th syzygy of $M$, denoted $\Omega^i(M)$, is defined as $\text{Ker}(d_{i-1})$. 
- **Ext Functors:** The group $\text{Ext}^i_{\Lambda}(M, N)$ is the $i$-th right derived functor of the Hom functor $\text{Hom}_{\Lambda}(-, N)$. It can be computed by taking a projective resolution of $M$, applying $\text{Hom}_{\Lambda}(-, N)$, and taking the $i$-th cohomology of the resulting cochain complex.
- **Commutative Generalization:** The conjecture is also heavily studied in the context of commutative Noetherian local rings $(R, \mathfrak{m}, k)$. In this setting, $\Lambda$ is replaced by $R$, and $M$ is a finitely generated $R$-module.

The conjecture asserts that the homological condition $\text{Ext}^{>0}_{\Lambda}(M, M \oplus \Lambda) = 0$ forces the projective resolution of $M$ to terminate at $P_0$, meaning $\Omega^1(M) = 0$ and $M \cong P_0$.

## 3. History & State of the Art (SOTA)

The conjecture was introduced in 1975 by Maurice Auslander and Idun Reiten in their seminal paper *"On a generalized version of the Nakayama conjecture"*. They proposed it as a structural bridge to approach other massive homological problems of the era.

Historically, the conjecture is part of a hierarchy of homological conjectures. Auslander and Reiten proved that the **Generalized Nakayama Conjecture (GNC)** implies the Auslander-Reiten Conjecture, which in turn implies the original **Nakayama Conjecture** (1958). 

In 1993, Auslander, Ding, and Solberg popularized the translation of this conjecture to commutative Noetherian rings. This opened a parallel track of research in commutative algebra. A major SOTA milestone occurred in 2000 when Avramov and Buchweitz proved the conjecture for commutative complete intersections using the geometric theory of support varieties.

Today, the State of the Art involves analyzing the conjecture through the lens of triangulated categories, specifically the singularity category $D_{sg}(\Lambda) = D^b(\text{mod}-\Lambda) / K^b(\text{proj}-\Lambda)$, where the conjecture translates to questions about the existence of specific rigid objects.

## 4. Partial Results / Verified Cases

The conjecture remains open in general, but it has been verified for several substantial classes of algebras and rings:

1. **Algebras of Finite Representation Type:** Auslander and Reiten (1975) proved it for algebras possessing only finitely many isomorphism classes of indecomposable finitely generated modules.
2. **Symmetric and Self-Injective Algebras:** Also proved by Auslander and Reiten (1975). For these algebras, $\Lambda$ is an injective module over itself.
3. **Algebras of Finite Global Dimension:** Trivially verified, as any module $M$ over such an algebra has finite projective dimension. The condition $\text{Ext}^{>0}_{\Lambda}(M, \Lambda) = 0$ then immediately forces $M$ to be projective by a standard depth argument.
4. **Commutative Complete Intersections:** Proven by Avramov and Buchweitz (2000). E.g., rings of the form $k[[x_1, \dots, x_n]] / (f_1, \dots, f_c)$ where $f_1, \dots, f_c$ is a regular sequence.
5. **Commutative Gorenstein Rings in Low Dimensions:** Proved for Gorenstein local rings of codimension at most 4, and dimension at most 1 (Araya, 2009).
6. **Algebras with Radical Square Zero:** Proved by various authors via explicit structural representation theory of quivers.

## 5. Principal Obstacles

The primary reason the conjecture remains open is the highly erratic behavior of minimal projective resolutions (syzygy growth) over arbitrary Artin algebras of infinite global dimension. 

When analyzing $\text{Ext}^i_{\Lambda}(M, M) = 0$, mathematicians attempt to link the homological properties of $M$ to the geometry of its deformations or its support variety. However, the powerful machinery of **cohomological support varieties**, which works perfectly for complete intersections and group algebras (via the action of Hochschild cohomology), completely breaks down for arbitrary Artin algebras. The Hochschild cohomology ring of a general algebra is rarely Noetherian, meaning standard commutative algebraic geometry cannot be used to bound the complexity of the module $M$.

Without bounded complexity or periodic syzygies (as found in self-injective rings), there is currently no mechanism to prove that the vanishing of $\text{Ext}^i$ prevents the syzygies $\Omega^i(M)$ from growing wildly.

## 6. The Gap

The precise mathematical gap lies between algebras where asymptotic homological behavior is governed by geometric properties (like complete intersections) and wild algebras where modules can have infinite projective dimension without exhibiting any regularity. 

To resolve the conjecture, one must either:
1. Discover a new homological invariant that forces modules with vanishing self-extensions over arbitrary algebras to have finite projective dimension (thereby bridging the gap).
2. Construct a counterexample: an algebra with pathological ideal structure and an infinite-dimensional, fractal-like module $M$ where the syzygies perfectly align to systematically annihilate all self-extensions, yet $M$ is not projective.

## 7. Current Research (as of June 2026)

Active research primarily takes place in the realm of derived categories and higher homological algebra. Key institutions including the University of Bielefeld, Nagoya University, and representations theorists across the UK and Germany are aggressively studying the conjecture.

Recent techniques heavily utilize **silting theory** and **$A_\infty$-algebras**. By mapping the conjecture to the singularity category $D_{sg}(\Lambda)$, researchers are attempting to prove that the only objects $X \in D_{sg}(\Lambda)$ satisfying $\text{Hom}_{D_{sg}}(X, X[i]) = 0$ for all $i > 0$ are isomorphic to the zero object.

A prominent line of attack involves applying Bridgeland stability conditions on the derived categories of Artin algebras to classify rigid modules *(frontier — verify)*. If stability spaces can rule out infinite-dimensional rigid objects in the singularity category, the conjecture holds.

## 8. Future Work

Leading researchers suggest the following pathways:
- **Gorenstein Algebras:** A major intermediate goal is to prove the conjecture for all noncommutative Gorenstein algebras. This would generalize both the self-injective case and the complete intersection case.
- **String and Band Algebras:** Conducting deep computational searches for counterexamples within specific, wild finite-dimensional path algebras over quivers with relations, utilizing algorithmic representation theory tools like the GAP-package QPA (Quivers and Path Algebras).
- **Thick Subcategory Classifications:** Improving the classification of thick tensor ideals in derived categories could provide the necessary constraints on the support of the modules in question.

## 9. Key References

- **[Foundational]** M. Auslander and I. Reiten. *On a generalized version of the Nakayama conjecture*. Proceedings of the American Mathematical Society, Vol. 52, 1975. [DOI](https://doi.org/10.1090/s0002-9939-1975-0389977-6)
- **[Foundational]** M. Auslander, S. Ding, and Ø. Solberg. *Liftings and weak liftings of modules*. Journal of Algebra, Vol. 156, 1993. [DOI](https://doi.org/10.1006/jabr.1993.1076)
- **[SOTA / Recent]** L. L. Avramov and R.-O. Buchweitz. *Support varieties and cohomology over complete intersections*. Inventiones mathematicae, Vol. 142, 2000. [DOI](https://doi.org/10.1007/s002220000090)
- **[SOTA / Recent]** T. Araya. *The Auslander-Reiten conjecture for Gorenstein rings*. Proceedings of the American Mathematical Society, Vol. 137, 2009. [DOI](https://doi.org/10.1090/s0002-9939-08-09757-8)
- **[Survey]** C. Huneke and G. Leuschke. *Two theorems about maximal Cohen-Macaulay modules*. Mathematische Annalen, Vol. 331, 2004.

## 10. Worked Example / Concrete Special Case

To ground the conjecture, we examine a concrete, simple instance where the conjecture's premise holds and forces the module to be projective. 

Let $k$ be a field. Consider the commutative Artinian algebra of dual numbers:
$$ \Lambda = k[x]/(x^2) $$
This algebra is local and self-injective. Its only indecomposable finitely generated modules are $\Lambda$ itself (which is projective) and the simple module $k$ (where $x$ acts as $0$).

Let us test the simple module $M = k$ against the Auslander-Reiten condition. We must compute $\text{Ext}^1_{\Lambda}(k, k)$. First, we construct the minimal projective resolution of $k$:
$$ \cdots \xrightarrow{\cdot x} \Lambda \xrightarrow{\cdot x} \Lambda \xrightarrow{\cdot x} \Lambda \xrightarrow{\pi} k \to 0 $$
where the maps between the copies of $\Lambda$ are multiplication by $x$. 

To compute $\text{Ext}^i_{\Lambda}(k, k)$, we drop the module $k$ and apply the functor $\text{Hom}_{\Lambda}(-, k)$ to the projective resolution. This yields the cochain complex:
$$ 0 \to \text{Hom}_{\Lambda}(\Lambda, k) \xrightarrow{(\cdot x)^*} \text{Hom}_{\Lambda}(\Lambda, k) \xrightarrow{(\cdot x)^*} \text{Hom}_{\Lambda}(\Lambda, k) \to \cdots $$
Since $\text{Hom}_{\Lambda}(\Lambda, k) \cong k$, this complex becomes:
$$ 0 \to k \xrightarrow{(\cdot x)^*} k \xrightarrow{(\cdot x)^*} k \to \cdots $$
Because $x$ annihilates $k$ (i.e., $x \cdot m = 0$ for all $m \in k$), the induced map $(\cdot x)^*$ is identically the zero map. Thus, the complex is simply:
$$ 0 \to k \xrightarrow{0} k \xrightarrow{0} k \to \cdots $$
The cohomology of this complex at degree 1 gives us the Ext group:
$$ \text{Ext}^1_{\Lambda}(k, k) = \frac{\text{Ker}(0)}{\text{Im}(0)} = \frac{k}{0} \cong k \neq 0 $$
Because $\text{Ext}^1_{\Lambda}(k, k) \neq 0$, the simple module $M = k$ *fails* the premise of the conjecture. 

Consequently, the only modules over $\Lambda = k[x]/(x^2)$ that satisfy the vanishing condition $\text{Ext}^{>0}_{\Lambda}(M, M) = 0$ are the direct sums of $\Lambda$ itself. Since $\Lambda$ is a free module, these modules are projective, perfectly confirming the Auslander-Reiten conjecture for this specific algebra.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*