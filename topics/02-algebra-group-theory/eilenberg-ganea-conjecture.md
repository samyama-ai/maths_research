---
id: 02-algebra-group-theory/eilenberg-ganea-conjecture
title: "Eilenberg-Ganea Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Eilenberg-Ganea Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/eilenberg-ganea-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Eilenberg-Ganea Conjecture is a fundamental open problem in geometric group theory and algebraic topology. It posits a strict equality between the algebraic complexity of a discrete group, as measured by its cohomological dimension, and its topological complexity, as measured by its geometric dimension, in the critical case of dimension two. 

Formally, the conjecture states: 
**For any discrete group $G$, if the cohomological dimension of $G$ is exactly 2, then the geometric dimension of $G$ is also exactly 2.**

Symbolically, this is expressed as:
$$ \text{cd}(G) = 2 \implies \text{gd}(G) = 2 $$

A complete proof of this conjecture would require demonstrating that for every group possessing a projective resolution of length 2 over its integral group ring, one can construct an aspherical 2-dimensional CW complex whose fundamental group is $G$. A disproof would require the explicit construction of a group (or proof of its existence) that has a cohomological dimension of 2, but for which any classifying space $K(G, 1)$ requires at least 3 dimensions.

## 2. Mathematical Foundations

The conjecture bridges group cohomology and homotopy theory. To state it formally, we must rigorously define both invariants.

**Cohomological Dimension ($\text{cd}(G)$):**
Let $G$ be a discrete group and $\mathbb{Z}[G]$ be its integral group ring. A $G$-module is equivalent to a left $\mathbb{Z}[G]$-module. The group cohomology $H^n(G; M)$ with coefficients in a $\mathbb{Z}[G]$-module $M$ is defined as the $n$-th cohomology group of the cochain complex $\text{Hom}_{\mathbb{Z}[G]}(P_\bullet, M)$, where $P_\bullet$ is a projective resolution of the trivial $\mathbb{Z}[G]$-module $\mathbb{Z}$:
$$ \cdots \to P_n \xrightarrow{\partial_n} P_{n-1} \xrightarrow{\partial_{n-1}} \cdots \to P_1 \xrightarrow{\partial_1} P_0 \xrightarrow{\epsilon} \mathbb{Z} \to 0 $$
The cohomological dimension is defined as:
$$ \text{cd}(G) = \sup \{ n \in \mathbb{N} \mid \exists \text{ a } \mathbb{Z}[G]\text{-module } M \text{ with } H^n(G; M) \neq 0 \} $$
Equivalently, by standard homological algebra, $\text{cd}(G)$ is the minimum length $n$ (possibly infinite) of a projective resolution of $\mathbb{Z}$ over $\mathbb{Z}[G]$.

**Geometric Dimension ($\text{gd}(G)$):**
An Eilenberg-MacLane space $K(G, 1)$, also known as a classifying space $BG$ (up to homotopy equivalence), is a connected CW complex $X$ such that its fundamental group $\pi_1(X)$ is isomorphic to $G$, and its higher homotopy groups vanish: $\pi_n(X) = 0$ for all $n \ge 2$. Such a space is called *aspherical*. Its universal cover $\tilde{X}$ is a contractible CW complex.
The geometric dimension of $G$ is defined as the minimum dimension of any such CW complex:
$$ \text{gd}(G) = \min \{ \dim(X) \mid X \text{ is a CW complex and } X \simeq K(G, 1) \} $$

**The Eilenberg-Ganea Theorem (1957):**
The foundational theorem established by Samuel Eilenberg and Tudor Ganea gives a global upper bound on the geometric dimension in terms of the cohomological dimension:
$$ \text{gd}(G) \le \max(3, \text{cd}(G)) $$
Because the cellular chain complex of the universal cover $\tilde{X}$ of any $K(G, 1)$ space provides a free (and therefore projective) resolution of $\mathbb{Z}$ over $\mathbb{Z}[G]$, it trivially follows that $\text{cd}(G) \le \text{gd}(G)$. Combined with the Eilenberg-Ganea theorem, this implies $\text{cd}(G) = \text{gd}(G)$ for all cases except possibly when $\text{cd}(G) = 2$.

**The Stallings-Swan Theorem (1968, 1969):**
For dimension 1, a deep result by John R. Stallings and Richard G. Swan shows that $\text{cd}(G) = 1$ if and only if $G$ is a free group. Since a free group has a 1-dimensional $K(G, 1)$ (a bouquet of circles), $\text{cd}(G) = 1 \implies \text{gd}(G) = 1$. The only remaining gap in relating these two invariants is $n=2$.

## 3. History & State of the Art (SOTA)

The Eilenberg-Ganea conjecture originates from their 1957 paper *On the Lusternik-Schnirelmann category of abstract groups*. While calculating the Lusternik-Schnirelmann category of Eilenberg-MacLane spaces, they succeeded in constructing a $K(G,1)$ of dimension $n$ given an algebraic resolution of length $n$, provided $n \ge 3$. They explicitly noted the failure of their construction in dimension 2, framing the question of whether $\text{cd}(G) = 2 \implies \text{gd}(G) = 2$ as an open problem. 

For nearly forty years, the conjecture was approached as an isolated problem in homological algebra. The modern State of the Art was radically redefined in 1997 by Mladen Bestvina and Noel Brady. In their seminal paper *Morse theory and finiteness properties of groups*, they introduced a profound logical dichotomy between the Eilenberg-Ganea conjecture and another famous topological problem, the Whitehead asphericity conjecture (which posits that every connected subcomplex of an aspherical 2-complex is itself aspherical).

Bestvina and Brady constructed a novel family of groups (now called Bestvina-Brady groups or Artin kernel groups) defined as the kernel of a specific homomorphism from a right-angled Artin group (RAAG) to the integers $\mathbb{Z}$. By mapping the RAAG onto a line and utilizing discrete Morse theory on the corresponding CAT(0) cube complex, they related the homological finiteness properties of the group directly to the topological properties of a defining flag complex $\Gamma$. 

Their devastating corollary proved that if the Whitehead conjecture is true, then a specific Bestvina-Brady group possesses a cohomological dimension of 2 but a geometric dimension of 3. Conversely, if the Eilenberg-Ganea conjecture is universally true, then the Whitehead conjecture must be false. This SOTA result proved that at least one of these two bedrock conjectures in topology is unequivocally false.

## 4. Partial Results / Verified Cases

Despite the lack of a general proof, the conjecture has been verified for an extensive array of group classes. The equation $\text{cd}(G) = \text{gd}(G) = 2$ has been confirmed in the following cases:

- **Torsion-Free One-Relator Groups:** By the foundational work of Lyndon (1950), if $G$ is presented with a single relator $G = \langle X \mid r \rangle$ and is torsion-free, its standard presentation complex is inherently aspherical. Thus, $\text{gd}(G) \le 2$, meaning both dimensions coincide perfectly at 2 (unless $G$ is free).
- **Surface Groups and 3-Manifold Groups:** The fundamental groups of closed orientable surfaces of genus $g \ge 2$ have geometric dimension 2, realized by the surfaces themselves. Furthermore, Papakyriakopoulos's Sphere Theorem implies that the fundamental group of any aspherical 3-manifold with boundary (such as non-trivial knot complements) satisfies the conjecture.
- **Elementary Amenable Groups:** Work by Hillman and others has shown that the conjecture holds for all elementary amenable groups. 
- **Solvable Groups:** Gildenhuys showed that finitely generated solvable groups of cohomological dimension 2 have geometric dimension 2.
- **Groups with the $FP_2$ Property:** If the group is finitely presented (type $F_2$) and possesses a finite type projective resolution, significant progress has been made using Wall's finiteness obstructions. 

Crucially, the Bestvina-Brady groups that serve as potential counterexamples are known to be of type $FP$ (they admit a finite projective resolution of finite length) but it is completely unknown if they are of type $F$ (they admit a finite $K(G, 1)$), establishing the frontier of known bounds.

## 5. Principal Obstacles

The persistence of the Eilenberg-Ganea conjecture stems from an asymmetric bottleneck between homological algebra and geometric realization in low dimensions. Specifically, it involves the failure of the Whitney trick and the inability to geometrically bypass the fundamental group $\pi_1$.

When proving the generalized Eilenberg-Ganea theorem for $n \ge 3$, one employs the Hurewicz theorem and Whitehead's theorem. Given an algebraic resolution of length $n$, one starts with a space having the correct fundamental group and systematically adds cells to kill higher homotopy groups, terminating the process at dimension $n$ by utilizing the algebraic vanishing of $H^{n+1}$. In dimension 3 or higher, algebraic cancellations in the chain complex can be realized geometrically by attaching and sliding cells (similar to handle sliding in surgery theory) because there is enough "room" to avoid self-intersections. 

For dimension 2, this geometric process hits a hard barrier. To construct a 2-dimensional $K(G, 1)$, one must add 2-cells to a 1-dimensional skeleton to kill all relations and simultaneously ensure that $\pi_2(X) = 0$. However, adding a 2-cell inherently affects $\pi_1(X)$. There is no space to geometrically realize algebraic homotopies without tangling the paths that define the non-abelian fundamental group.

Furthermore, this algebraic-geometric gap is captured by Wall's D2 problem. Wall defined conditions under which algebraic complexes can be realized geometrically. For $n \ge 3$, if a group $G$ has a projective resolution of length $n$, one can realize a finite CW complex. For $n=2$, this requires that a specific projective module over $\mathbb{Z}[G]$ be stably free. The non-abelian nature of $\mathbb{Z}[G]$ in the $K$-theory group $\tilde{K}_0(\mathbb{Z}[G])$ prevents us from asserting that a projective module of length 2 implies a free module of length 2 that can serve as the cellular chain complex for a 2-dimensional space.

## 6. The Gap

The precise mathematical gap that must be crossed to resolve the conjecture is localized to the properties of the Bestvina-Brady groups $BB_\Gamma$. 

Let $\Gamma$ be a finite flag complex, and $A_\Gamma$ be its associated right-angled Artin group. Let $\phi: A_\Gamma \to \mathbb{Z}$ be the homomorphism sending every standard generator to $1$. The Bestvina-Brady group is the kernel $BB_\Gamma = \ker(\phi)$. 

Bestvina and Brady proved that $BB_\Gamma$ has $\text{cd}(BB_\Gamma) \le 2$ if and only if the complex $\Gamma$ is acyclic (i.e., its reduced homology groups vanish). They also proved that $BB_\Gamma$ is finitely presented if and only if $\Gamma$ is simply connected. 

To construct a counterexample to the Eilenberg-Ganea conjecture, one must find an acyclic flag complex $\Gamma$ such that $BB_\Gamma$ cannot be the fundamental group of an aspherical 2-complex. The gap lies purely in determining the geometric dimension of $BB_\Gamma$ for a carefully chosen acyclic, non-contractible 2-complex $\Gamma$. If the Whitehead conjecture is true, any such $\Gamma$ forces $\text{gd}(BB_\Gamma) = 3$, crossing the gap and disproving Eilenberg-Ganea. If Eilenberg-Ganea is true, no such obstruction exists, meaning the Whitehead conjecture must yield to a counterexample.

## 7. Current Research (as of June 2026)

Research continues to focus aggressively on the Bestvina-Brady dichotomy, searching for counterexamples in both domains. 

- **Bredon Cohomology Analogues *(frontier — verify)*:** Recent research has explored the conjecture in the broader context of Bredon cohomology, which incorporates group actions and families of subgroups. In 2010, researchers (e.g., Martinez-Perez, Nucinkis) established that the Eilenberg-Ganea theorem *fails* for Bredon cohomology with respect to the family of virtually cyclic subgroups. Specifically, they found groups where the Bredon cohomological dimension is 3, but the Bredon geometric dimension is exactly 4. While this does not strictly solve the classical $n=2$ problem, the presence of structural Eilenberg-Ganea gaps in closely related categorical settings provides strong heuristic evidence to modern researchers that the classical Eilenberg-Ganea conjecture is likely false.
- **Computational Homology of RAAGs:** Computational approaches are mapping the subgroups of RAAGs using discrete Morse theory to search for finite 2-complexes that could realize the $BB_\Gamma$ groups geometrically, attempting to forcefully construct a $K(G, 1)$ and thereby disprove the Whitehead conjecture.

## 8. Future Work

Prominent geometric group theorists suggest the following pathways to finally resolve the conjecture:

- **Direct resolution of the Whitehead Conjecture:** The strongest strategy is to directly construct a non-aspherical subcomplex of an aspherical 2-complex. This would sever the logical tie established by Bestvina-Brady, leaving the Eilenberg-Ganea conjecture open, or conversely, proving Whitehead and immediately disproving Eilenberg-Ganea.
- **Wall's D2 Obstructions:** Further study of the projective class groups $\tilde{K}_0(\mathbb{Z}[G])$ for Bestvina-Brady groups to determine if an algebraic obstruction to creating a purely free (rather than projective) length-2 resolution inherently exists.
- **Topological approaches to Artin kernels:** Examining the geometry of the CAT(0) cube complexes upon which RAAGs act to find generalized Morse functions that preserve the asphericity of descending level sets.

## 9. Key References

- **[Foundational]** Eilenberg, S., & Ganea, T. *On the Lusternik-Schnirelmann category of abstract groups.* Annals of Mathematics, 1957.
- **[Foundational]** Stallings, J. R. *On torsion-free groups with infinitely many ends.* Annals of Mathematics, 1968.
- **[Foundational]** Swan, R. G. *Groups of cohomological dimension one.* Journal of Algebra, 1969.
- **[SOTA / Recent]** Bestvina, M., & Brady, N. *Morse theory and finiteness properties of groups.* Inventiones mathematicae, 1997.
- **[Survey]** Brown, K. S. *Cohomology of Groups.* Springer-Verlag, 1982.
- **[SOTA / Recent]** Martinez-Perez, C., & Nucinkis, B. *Bredon cohomological dimension for out(F_n).* Journal of Topology, 2010.

## 10. Worked Example / Concrete Special Case

To ground this abstract conjecture, it is instructive to observe a positive case where $\text{cd}(G) = \text{gd}(G) = 2$. Consider the fundamental group of the closed, orientable surface of genus 2. It has the standard presentation:
$$ G = \langle a, b, c, d \mid [a,b][c,d] = 1 \rangle $$

Where $[a,b] = aba^{-1}b^{-1}$ is the commutator. The standard presentation complex $X$ is formed by taking a single vertex (0-cell), four loops (1-cells) representing the generators $a,b,c,d$, and attaching a single 2-cell along the path specified by the word $[a,b][c,d]$. 

This space $X$ is exactly the genus 2 surface. Since the universal cover of a surface of genus $g \ge 2$ is the hyperbolic plane $\mathbb{H}^2$, which is contractible, $X$ is an aspherical space. Thus $X \simeq K(G, 1)$. Since $X$ is a 2-dimensional CW complex, we know immediately that $\text{gd}(G) \le 2$.

To calculate the cohomological dimension, we look at the cellular chain complex of the universal cover $\tilde{X}$, which yields a free resolution of the trivial module $\mathbb{Z}$ over the group ring $\mathbb{Z}[G]$:
$$ 0 \to C_2(\tilde{X}) \xrightarrow{\partial_2} C_1(\tilde{X}) \xrightarrow{\partial_1} C_0(\tilde{X}) \xrightarrow{\epsilon} \mathbb{Z} \to 0 $$

The ranks of these free modules correspond to the number of cells in $X$. Thus, we have the exact resolution:
$$ 0 \to \mathbb{Z}[G] \xrightarrow{\partial_2} \mathbb{Z}[G]^4 \xrightarrow{\partial_1} \mathbb{Z}[G] \xrightarrow{\epsilon} \mathbb{Z} \to 0 $$

Because the resolution has length 2, $\text{cd}(G) \le 2$. The boundary maps $\partial_1$ and $\partial_2$ can be explicitly computed using Fox free calculus. For instance, the image of the generator of $C_2$ under $\partial_2$ is a vector of Fox derivatives of the relator $r = [a,b][c,d]$:
$$ \partial_2(1) = \left( \frac{\partial r}{\partial a}, \frac{\partial r}{\partial b}, \frac{\partial r}{\partial c}, \frac{\partial r}{\partial d} \right) $$

To strictly show $\text{cd}(G) = 2$, we calculate the second group cohomology with coefficients in the group ring, $H^2(G; \mathbb{Z}[G])$, which is related to the number of ends of the group. For surface groups, $H^2(G; \mathbb{Z}[G]) \cong \mathbb{Z} \neq 0$. Thus, $\text{cd}(G) = 2$.

In this concrete setting, the algebraic complex perfectly matches the geometric CW complex, avoiding the obstacles of Wall's D2 problem and flawlessly satisfying the equation $\text{cd}(G) = \text{gd}(G) = 2$. The conjecture asserts that this harmonious matching must always be possible for any group whose algebraic resolution naturally stops at dimension 2.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*