---
id: 01-number-theory/fontaine-mazur-conjecture
title: "Fontaine-Mazur Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fontaine-Mazur Conjecture

> **Topic:** 01-number-theory · **ID:** `01-number-theory/fontaine-mazur-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Fontaine-Mazur conjecture posits a profound and rigid connection between the arithmetic of Galois representations and the geometry of algebraic varieties. Specifically, it asserts that any irreducible, continuous, odd, $p$-adic Galois representation of the absolute Galois group of a number field that is unramified almost everywhere and is "potentially semi-stable" at all places dividing $p$, must originate from algebraic geometry. That is, it should appear as a subquotient of the étale cohomology of some proper smooth algebraic variety defined over the number field.

A simpler but central part of this conjecture (often referred to as the Fontaine-Mazur conjecture for unramified representations) asserts that there are no infinite, everywhere unramified, $p$-adic analytic Galois extensions of a number field. In other words, if $F$ is a number field and $F_\infty / F$ is an infinite Galois extension whose Galois group $\operatorname{Gal}(F_\infty / F)$ is a $p$-adic Lie group of dimension $\ge 1$, then this extension must be ramified at some infinite set of primes, or at least ramified at some primes above $p$.

## 2. Mathematical Foundations

Let $F$ be a number field, and let $G_F = \operatorname{Gal}(\overline{F}/F)$ be its absolute Galois group. Let $E$ be a finite extension of $\mathbb{Q}_p$. 
A $p$-adic Galois representation is a continuous group homomorphism:
$$ \rho: G_F \to \operatorname{GL}_n(E) $$

The representation $\rho$ is said to be *unramified* at a finite place $v$ of $F$ if the inertia group $I_v \subset G_F$ at $v$ acts trivially. A fundamental property of representations "coming from geometry" (i.e., arising from the étale cohomology of algebraic varieties) is that they are unramified outside a finite set of places $S$.

At places $v | p$, the condition of coming from geometry translates, via $p$-adic Hodge theory, to the representation being *de Rham*, or more generally, *potentially semi-stable*. Jean-Marc Fontaine introduced the topological period rings $B_{\text{dR}}$, $B_{\text{st}}$, and $B_{\text{cris}}$ to define these conditions. 
For a local field $K/\mathbb{Q}_p$ and a representation $V$ of $G_K$ over $E$, $V$ is de Rham if:
$$ \dim_K (V \otimes_{\mathbb{Q}_p} B_{\text{dR}})^{G_K} = \dim_{\mathbb{Q}_p} V $$
If $V$ is the restriction of a global representation $\rho$ to the decomposition group at $v|p$, we require this local representation to be de Rham.

**Conjecture (Fontaine-Mazur, 1995):**
Let $\rho: G_F \to \operatorname{GL}_n(E)$ be a continuous representation such that:
1. $\rho$ is unramified outside a finite set of places $S$ of $F$.
2. For every place $v | p$ of $F$, the restriction $\rho|_{G_{F_v}}$ is potentially semi-stable (or equivalently, de Rham).

Then there exists a proper smooth variety $X$ over $F$, an integer $i \ge 0$, and a Tate twist $j$, such that $\rho$ is isomorphic to a subquotient of $H^i_{\text{ét}}(X_{\overline{F}}, \mathbb{Q}_p)(j) \otimes_{\mathbb{Q}_p} E$.

For $n=2$ and $F=\mathbb{Q}$, assuming $\rho$ is odd ($\det \rho(c) = -1$ for complex conjugation $c$), this conjecture implies that $\rho$ arises from a classical modular form, directly tying it to the Langlands program.

## 3. History & State of the Art (SOTA)

The conjecture was formulated by Jean-Marc Fontaine and Barry Mazur in their seminal 1995 paper, "Geometric Galois representations." It generalized the modularity theorem (the Taniyama-Shimura-Weil conjecture), which was proved for semistable elliptic curves by Andrew Wiles and Richard Taylor in 1994 to resolve Fermat's Last Theorem. 

The modularity theorem essentially proves the two-dimensional, $F=\mathbb{Q}$ case of the Fontaine-Mazur conjecture for representations arising specifically from elliptic curves. 

Since the 1990s, the primary method of attacking the Fontaine-Mazur conjecture has been via establishing Modularity Lifting Theorems (MLTs). These theorems prove that if a representation is *residually modular* (its reduction modulo $p$ comes from a modular form) and satisfies the Fontaine-Mazur conditions, then it is strictly modular (and thus comes from geometry).

The state of the art includes the work of Mark Kisin (2009), who proved the 2-dimensional case for most representations over $\mathbb{Q}$, and the subsequent vast generalizations by the 10-author paper (Allen et al., 2023) which establishes potential automorphy for higher-dimensional representations over CM fields under certain mild conditions.

## 4. Partial Results / Verified Cases

- **Dimension 1:** Proved completely via Class Field Theory. The de Rham condition for a 1-dimensional character precisely isolates the algebraic Hecke characters (Grössencharacters), which correspond to motives of CM elliptic curves or general Abelian varieties with complex multiplication.
- **Dimension 2, $F = \mathbb{Q}$:** Largely solved for odd representations. Thanks to the work of Wiles, Taylor, Diamond, Conrad, Breuil, and crucially Kisin and Emerton. If $\rho: G_{\mathbb{Q}} \to \operatorname{GL}_2(E)$ is odd, unramified outside finitely many primes, and de Rham at $p$ with distinct Hodge-Tate weights, and if its residual representation $\bar{\rho}$ is modular and satisfies mild technical hypotheses, then $\rho$ is modular and arises from geometry.
- **Potential Automorphy for Higher Dimensions:** Taylor, Harris, and collaborators have proved that many $n$-dimensional representations of $G_F$ (where $F$ is a totally real or CM field) become automorphic (and thus geometric) after restricting to $G_{F'}$ for some totally real or CM extension $F'/F$.
- **Unramified Case for Small Fields:** For certain small number fields (e.g., imaginary quadratic fields with specific class groups), computational verifications by Boston and others have shown that no infinite unramified $p$-adic analytic extensions exist.

## 5. Principal Obstacles

- **Residual Modularity:** Modularity lifting theorems require a starting point: one must know that the mod-$p$ representation $\bar{\rho}$ is *already* modular. For $n=2$ and $F=\mathbb{Q}$, this is Serre's conjecture (proved unconditionally by Khare and Wintenberger in 2009). For higher dimensions or general number fields, there is no unconditional proof that $\bar{\rho}$ is automorphic, creating a massive bootstrap problem.
- **Even Representations over $\mathbb{Q}$:** For $n=2$ and $\rho$ being *even* ($\det \rho(c) = 1$), there is no corresponding classical algebraic modular form. Automorphic forms for this case would be Maass forms, which do not obviously possess Galois representations coming from algebraic geometry. The Fontaine-Mazur conjecture predicts these shouldn't be de Rham unless they are reducible, but proving this remains completely open.
- **Torsion in Cohomology (Calegari-Geraghty Method):** In settings where the locally symmetric spaces lack complex structures (e.g., for arbitrary number fields instead of totally real or CM fields), the associated Galois representations occur only in the torsion of the cohomology. Extending Taylor-Wiles patching to these non-regular, torsion-heavy environments requires highly complex derived algebraic geometry.

## 6. The Gap

The gap lies between *potential* modularity/automorphy and *strict* automorphy, as well as the complete absence of methods for even representations or representations over arbitrary number fields. To fully resolve the conjecture for $n=2$ over $\mathbb{Q}$, one must remove the residual modularity hypothesis completely and handle pathological cases where $\bar{\rho}$ is highly singular. For general $n$ and general $F$, we need a global Langlands correspondence that does not rely strictly on Shimura varieties, since Shimura varieties only exist for specific signature types.

## 7. Current Research (as of June 2026)

Active research is heavily focused on the categorical local Langlands correspondence and derived deformation rings:
- **Derived Taylor-Wiles Patching:** Groups around Calegari, Caraiani, Gee, Geraghty, and Newton are pushing the boundaries of the Calegari-Geraghty method to prove modularity over imaginary quadratic fields using derived structures to handle cohomology torsion phenomena.
- **$p$-adic Langlands and Geometrization:** The work of Scholze (using condensed mathematics and perfectoid spaces) and Fargues (the Fargues-Fontaine curve) is providing a vastly more powerful framework to study Galois representations globally. *(frontier — verify)* The geometrization of the local Langlands correspondence is expected to provide new unconditional global modularity lifting techniques by gluing local $p$-adic Langlands parameters without passing through classical Shimura varieties.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- Removing the Taylor-Wiles condition on residual representations by using higher-dimensional generalizations of Kisin's resolution of deformation rings.
- Proving the unramified Fontaine-Mazur conjecture for specific $p$-adic Lie groups (e.g., $\operatorname{SL}_n(\mathbb{Z}_p)$) over arbitrary number fields using purely group-theoretic and Iwasawa-theoretic bounds.
- Leveraging the categorical Langlands program on the Fargues-Fontaine curve to completely bypass the need for Shimura varieties, thereby finding geometric sources for Galois representations over fields with mixed signatures.

## 9. Key References

- **[Foundational]** Fontaine, J.-M., & Mazur, B. *Geometric Galois representations.* Elliptic curves, modular forms, & Fermat's last theorem (Hong Kong, 1993), Series in Number Theory, Int. Press, 1995.
- **[Foundational]** Kisin, M. *Moduli of finite flat group schemes, and modularity.* Annals of Mathematics, 2009.
- **[SOTA / Recent]** Allen, P., Calegari, F., Caraiani, A., Gee, T., Helm, D., Le Hung, B., Newton, J., Scholze, P., Taylor, R., & Thorne, J. *Potential automorphy over CM fields.* Annals of Mathematics, 2023.
- **[Survey]** Emerton, M. *The Fontaine-Mazur conjecture for $\operatorname{GL}_2$.* Current Developments in Mathematics, 2004.
- **[Survey]** Weston, T. *The Fontaine-Mazur Conjecture.* Expositiones Mathematicae, 2001.

## 10. Worked Example / Concrete Special Case

Consider the easiest non-trivial formulation of the "unramified" Fontaine-Mazur conjecture:
**Claim:** There is no infinite, everywhere unramified pro-$p$ extension of $\mathbb{Q}$.

*Walkthrough:*
1. Suppose $K / \mathbb{Q}$ is a finite unramified Galois extension.
2. By Minkowski's theorem from algebraic number theory, the discriminant of any number field $K \neq \mathbb{Q}$ is strictly greater than 1 in absolute value ($|\Delta_K| > 1$).
3. A fundamental theorem states that a prime ramifies in $K$ if and only if it divides the discriminant $\Delta_K$.
4. Since $|\Delta_K| > 1$, there is at least one prime $p$ dividing $\Delta_K$.
5. Therefore, there is at least one ramified prime in the extension.
6. Thus, there are no non-trivial finite unramified extensions of $\mathbb{Q}$ at all.
7. Consequently, there can be no *infinite* everywhere unramified extension of $\mathbb{Q}$.

While this case is trivial over $\mathbb{Q}$ due to Minkowski's bound, the Fontaine-Mazur conjecture becomes remarkably difficult when we replace $\mathbb{Q}$ with a general number field $F$. A general field $F$ can have everywhere unramified extensions (namely, its Hilbert class field), and one can ask if there can be an *infinite* tower of such extensions whose Galois group is a $p$-adic Lie group. 
For instance, the Golod-Shafarevich theorem proves that infinite unramified pro-$p$ extensions *do* exist for certain number fields $F$, but their Galois groups are not $p$-adic analytic (they are not finite-dimensional $p$-adic Lie groups). The Fontaine-Mazur conjecture insists that if you restrict the Galois group to be a $p$-adic Lie group, the tower must eventually ramify.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*