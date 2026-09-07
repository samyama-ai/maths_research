---
id: 02-algebra-group-theory/dixmiers-unitarizability-problem
title: "Dixmier's Unitarizability Problem"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dixmier's Unitarizability Problem

> **Topic:** 02-algebra-group-theory · **ID:** `02-algebra-group-theory/dixmiers-unitarizability-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Dixmier's Unitarizability Problem is a profound open question at the intersection of abstract harmonic analysis, group theory, and operator algebras. It asks whether the property of amenability for a discrete group is strictly characterized by the unitarizability of all its uniformly bounded representations. 

More precisely, let $G$ be a discrete topological group, and let $\pi: G \to B(H)$ be a strongly continuous representation of $G$ into the algebra of bounded linear operators on a complex Hilbert space $H$. The representation $\pi$ is said to be *uniformly bounded* if its norm is finite, meaning $\sup_{g \in G} \|\pi(g)\| < \infty$. The representation $\pi$ is said to be *unitarizable* if there exists a bounded invertible operator $S \in B(H)$ such that the conjugate representation $g \mapsto S^{-1}\pi(g)S$ is a unitary representation (i.e., takes values in the unitary group $U(H)$).

In 1950, Jacques Dixmier proved that if $G$ is an amenable group, then every uniformly bounded representation of $G$ is unitarizable. 

**The Conjecture:** If every uniformly bounded representation of a discrete group $G$ is unitarizable, then $G$ must be amenable. 

A complete proof of this conjecture requires demonstrating that every non-amenable group admits at least one uniformly bounded representation that cannot be made unitary via similarity. A disproof would require constructing a non-amenable group where all bounded representations are rigidly unitarizable.

## 2. Mathematical Foundations

The formulation and partial resolutions of this problem depend heavily on operator algebras and geometric group theory.

**Representations and Norms:**
Let $H$ be a complex Hilbert space. $B(H)$ denotes the Banach algebra of bounded linear operators on $H$, equipped with the standard operator norm $\|T\| = \sup_{\|x\| \le 1} \|Tx\|$. A representation $\pi: G \to B(H)$ is uniformly bounded if there exists a constant $C > 0$ such that:
$$ \sup_{g \in G} \|\pi(g)\| \le C $$
If $C=1$, $\pi$ is a representation by contractions. If $\pi(g)^* \pi(g) = I$ for all $g \in G$, it is a unitary representation.

**Amenability:**
A discrete group $G$ is amenable if there exists a left-invariant finitely additive probability measure on $G$. Equivalently, there exists a left-invariant state $\mu \in (\ell^\infty(G))^*$ (an invariant mean), such that for all $f \in \ell^\infty(G)$ and $h \in G$:
$$ \mu(\mathbf{1}) = 1, \quad f \ge 0 \implies \mu(f) \ge 0, \quad \mu(h \cdot f) = \mu(f) $$
where $(h \cdot f)(g) = f(h^{-1}g)$. 

**Completely Bounded Maps (Pisier's Framework):**
Let $C^*(G)$ be the full group $C^*$-algebra of $G$. A bounded representation $\pi$ extends to a bounded homomorphism $\tilde{\pi}: \ell^1(G) \to B(H)$. Gilles Pisier demonstrated that $\pi$ is unitarizable if and only if $\tilde{\pi}$ extends to a *completely bounded map* on $C^*(G)$. A map $T: C^*(G) \to B(H)$ is completely bounded if the supremum of the norms of the induced maps $T_n: M_n(C^*(G)) \to M_n(B(H))$ is finite:
$$ \|T\|_{cb} = \sup_{n \ge 1} \|T_n\| < \infty $$
This translates the group-theoretic Unitarizability Problem into the realm of operator spaces and similarity problems for $C^*$-algebras.

## 3. History & State of the Art (SOTA)

- **1950 (The Foundation):** Jacques Dixmier formulates the problem and proves the "amenable implies unitarizable" direction. Using an invariant mean $\mu$, Dixmier averaged the Hilbert space inner product to construct a new invariant inner product, thereby unitarizing the representation. M. M. Day independently proved analogous results for semigroups in the same year.
- **1955 (First Non-Unitarizable Representations):** L. Ehrenpreis and F. I. Mautner proved that the continuous non-amenable group $SL(2, \mathbb{R})$ possesses uniformly bounded representations that are not unitarizable, destroying the early hope that all bounded representations for all groups were unitarizable.
- **1980s (The Free Group Breakthrough):** For discrete groups, proving that the free group on two generators $F_2$ is non-unitarizable was a significant hurdle. This was successfully resolved via analytic continuations of the regular representation and Littlewood functions by V. Mantero and A. Zappa (1983), and subsequently streamlined by T. Pytlik and R. Szwarc (1986), and M. Bożejko (1987).
- **2000s (Operator Space Theory):** G. Pisier unified similarity problems using completely bounded maps, offering a metric characterization of unitarizability via length functions. 
- **2009-2010 (Beyond the von Neumann Conjecture):** Because the Day-von Neumann conjecture is false (not all non-amenable groups contain $F_2$), non-unitarizability of $F_2$ does not solve Dixmier's problem. I. Epstein and N. Monod (2009) proved non-unitarizability for non-amenable groups admitting certain non-amenable actions. Shortly after, N. Monod and N. Ozawa (2010) proved non-unitarizability for free Burnside groups of large odd exponent, which are non-amenable groups fundamentally devoid of $F_2$ subgroups.

## 4. Partial Results / Verified Cases

Dixmier's conjecture has been verified (i.e., proven non-unitarizable) for an overwhelmingly large class of non-amenable groups:

1. **Groups Containing $F_2$:** The property of unitarizability passes to subgroups. If $H \le G$ and $G$ is unitarizable, then $H$ must be unitarizable. Because $F_2$ is definitively non-unitarizable (Bożejko, 1987), any group containing $F_2$ is non-unitarizable. This completely resolves the problem for:
   - All linear groups in characteristic zero (via the Tits Alternative).
   - All non-elementary word-hyperbolic and relatively hyperbolic groups.
   - Mapping class groups of surfaces of high complexity.
2. **Epstein-Monod Groups (2009):** The conjecture holds for any non-amenable group $G$ that admits a minimal, strongly proximal action on a compact space such that the action is not amenable (e.g., groups acting on random forests).
3. **Burnside Groups (Monod-Ozawa, 2010):** Free Burnside groups $B(m, n) = \langle x_1, \dots, x_m \mid w^n = 1 \rangle$ are periodic (torsion) groups, and thus cannot contain $F_2$. For $m \ge 2$ and large odd $n \ge 665$, $B(m,n)$ is non-amenable (Adian, 1979). Monod and Ozawa explicitly constructed non-unitarizable representations for these groups, verifying Dixmier's problem for one of the most famous counterexamples to the von Neumann conjecture.
4. **Groups with non-trivial bounded cohomology:** If a group $G$ has non-vanishing bounded cohomology $H_b^2(G, \ell^2(G)) \neq 0$, it can often be shown to admit non-unitarizable representations via cohomological extension sequences.

## 5. Principal Obstacles

The primary barrier to fully resolving the conjecture is the profound pathological variety of algebraically non-amenable groups. 

To prove that a group is non-unitarizable, mathematicians typically construct a uniformly bounded representation that resists unitarization. The standard techniques for building these representations rely on geometric or dynamical tools:
- **Length functions / Cocycles:** Constructing a derivation from $G$ into a Hilbert space.
- **Random walks:** Exploiting non-trivial Poisson boundaries and harmonic functions.
- **Actions on trees/spaces:** Using geometric properties to induce representations from subgroups.

However, there exist purely "algebraic" non-amenable groups designed to defeat these exact tools. A primary obstacle is the class of **Tarski monsters**—infinite groups where every proper non-trivial subgroup is finite cyclic of prime order $p$. These groups lack meaningful subgroups, do not act naturally on trees, and their random walks are analytically intractable. Furthermore, computing bounded cohomology for such groups is currently beyond the reach of modern techniques. We lack a purely algebraic, universal machine that takes the abstract property of "non-amenability" (lack of an invariant mean) and automatically outputs a bounded, non-unitarizable representation.

## 6. The Gap

The gap resides precisely at the boundary between geometrically/dynamically non-amenable groups (where the conjecture is solved) and pathologically/algebraically non-amenable groups (where it remains open).

Let $\mathcal{U}$ be the class of unitarizable groups, and $\mathcal{A}$ be the class of amenable groups. We know $\mathcal{A} \subseteq \mathcal{U}$. Let $\mathcal{E}$ be the expansive class of non-amenable groups encompassing those with $F_2$, Burnside groups, and Epstein-Monod actions. We know $\mathcal{U} \cap \mathcal{E} = \emptyset$. 

The uncrossed mathematical barrier is determining whether $G \in \mathcal{U}$ when $G \notin \mathcal{A}$ and $G \notin \mathcal{E}$. The resolution requires either a totally novel functional-analytic method to construct derivations for arbitrary non-amenable groups, or proving that some exotic group (like a specific Tarski monster) possesses a rigid bounded representation theory, thereby establishing it as a counterexample.

## 7. Current Research (as of June 2026)

Research continues actively through the lenses of operator algebras, bounded cohomology, and measured group theory:

- **Bounded Cohomology Limitations:** Researchers at EPFL and Kyoto are investigating whether non-amenability universally guarantees the non-vanishing of certain bounded cohomology groups $H_b^n(G; E)$, which would provide a universal engine for generating non-unitarizable representations.
- **Acylindrically Hyperbolic Spaces:** Extending the random walk and boundary theories of Ozawa and Monod to groups acting on generalized non-positively curved spaces. 
- **Property (T) Rigidity:** Investigating the interaction between Kazhdan's Property (T) (which forces unitary representations close to the trivial one to contain invariant vectors) and uniformly bounded representations. The goal is to construct bounded representations on Property (T) groups that lack $F_2$.
- *(frontier — verify)* Active claims exist in measured group theory proposing that every non-amenable group must admit a weakened "tree-like" action on a quasi-tree. If validated, this structural universal could allow the Epstein-Monod framework to resolve the problem completely.

## 8. Future Work

Prominent mathematicians in the field advocate for the following strategic pathways:
- **Thompson's Group $F$:** Resolve the long-standing open problem of the amenability of Thompson's group $F$. If $F$ is proven to be non-amenable, determining its unitarizability would serve as a crucial test case for Dixmier's problem.
- **Tarski Monsters:** Perform a rigorous investigation into the $C^*$-algebras and completely bounded maps of Tarski monsters to determine their unitarizability status.
- **$L^p$-Unitarizability:** Generalize the problem to Banach spaces, asking which groups have the property that all uniformly bounded representations on $L^p$ spaces are similar to isometric representations. This functional analytic widening may yield new invariants.

## 9. Key References

- **[Foundational]** Dixmier, J. *Les moyennes invariantes dans les semi-groupes et leurs applications.* Acta Scientiarum Mathematicarum (Szeged), 12: 213-227, 1950.
- **[Foundational]** Day, M. M. *Means for the bounded functions and ergodicity of the bounded representations of semi-groups.* Transactions of the American Mathematical Society, 69(2): 276-291, 1950.
- **[Foundational]** Ehrenpreis, L., and Mautner, F. I. *Uniformly bounded representations of groups.* Proceedings of the National Academy of Sciences of the United States of America, 41(4): 231-233, 1955.
- **[Foundational]** Bożejko, M. *Uniformly bounded representations of free groups.* Journal für die reine und angewandte Mathematik, 377: 170-186, 1987.
- **[SOTA / Recent]** Epstein, I., and Monod, N. *Non-unitarizable representations and random forests.* Journal of Modern Dynamics, 3(3): 443-452, 2009.
- **[SOTA / Recent]** Monod, N., and Ozawa, N. *The Dixmier problem, lamplighters and Burnside groups.* Journal of Functional Analysis, 258(1): 255-267, 2010.
- **[Survey]** Pisier, G. *Similarity Problems and Completely Bounded Maps.* Lecture Notes in Mathematics 1618, Springer-Verlag, 2001.
- **[Survey]** Pisier, G. *Are unitarizable groups amenable?* Infinite Groups: Geometric, Combinatorial and Dynamical Aspects (Progress in Mathematics, Vol. 248). Birkhäuser, Basel, 2005.

## 10. Worked Example / Concrete Special Case

To ground the abstract problem, we can walk through Dixmier's original 1950 proof for the "Amenable $\implies$ Unitarizable" direction, using the infinite cyclic group $G = \mathbb{Z}$ (which is amenable).

Let $\pi: \mathbb{Z} \to B(H)$ be a uniformly bounded representation on a Hilbert space $H$ with inner product $\langle \cdot, \cdot \rangle$. Because it is uniformly bounded, there exists $C \ge 1$ such that $\|\pi(n)\| \le C$ for all integers $n$. 

Because $\mathbb{Z}$ is abelian, it is amenable. Therefore, there exists a translation-invariant mean (a Banach limit) $\mu$ on the space of bounded sequences $\ell^\infty(\mathbb{Z})$. 
For any two vectors $\xi, \eta \in H$, consider the bounded sequence of complex numbers given by $f(n) = \langle \pi(n)\xi, \pi(n)\eta \rangle$. We define a new inner product on $H$ by averaging over the group:
$$ [\xi, \eta] = \mu \left( n \mapsto \langle \pi(n)\xi, \pi(n)\eta \rangle \right) $$

We must show this new inner product is bounded and equivalent to the original one. 
First, the upper bound:
$$ |\langle \pi(n)\xi, \pi(n)\xi \rangle| \le \|\pi(n)\|^2 \|\xi\|^2 \le C^2 \|\xi\|^2 \implies [\xi, \xi] \le C^2 \|\xi\|^2 $$
Second, the lower bound. For any $n$, $\xi = \pi(-n)\pi(n)\xi$. Taking norms:
$$ \|\xi\| \le \|\pi(-n)\| \|\pi(n)\xi\| \le C \|\pi(n)\xi\| \implies \|\pi(n)\xi\|^2 \ge C^{-2} \|\xi\|^2 $$
Applying the mean $\mu$, which preserves inequalities, yields $[\xi, \xi] \ge C^{-2} \|\xi\|^2$.

Because the norm induced by $[\cdot, \cdot]$ is equivalent to the original norm, there exists by the Riesz Representation Theorem a unique, bounded, strictly positive, invertible self-adjoint operator $T \in B(H)$ such that $[\xi, \eta] = \langle T\xi, \eta \rangle$. Let $S = T^{1/2}$, which is also bounded and invertible. Therefore, $[\xi, \eta] = \langle S\xi, S\eta \rangle$.

Now, let us test if $\pi(k)$ is unitary with respect to the *new* inner product. For any $k \in \mathbb{Z}$:
$$ [\pi(k)\xi, \pi(k)\eta] = \mu \left( n \mapsto \langle \pi(n)\pi(k)\xi, \pi(n)\pi(k)\eta \rangle \right) $$
Because $\pi$ is a representation, $\pi(n)\pi(k) = \pi(n+k)$.
$$ [\pi(k)\xi, \pi(k)\eta] = \mu \left( n \mapsto \langle \pi(n+k)\xi, \pi(n+k)\eta \rangle \right) $$
By the translation invariance of the mean $\mu$, shifting the index by $k$ does not change the average:
$$ \mu \left( n \mapsto \langle \pi(n+k)\xi, \pi(n+k)\eta \rangle \right) = \mu \left( m \mapsto \langle \pi(m)\xi, \pi(m)\eta \rangle \right) = [\xi, \eta] $$

This proves $\pi(k)$ is unitary in the new inner product. Translating this back to the original Hilbert space norm:
$$ \langle S\pi(k)\xi, S\pi(k)\eta \rangle = [\pi(k)\xi, \pi(k)\eta] = [\xi, \eta] = \langle S\xi, S\eta \rangle $$
Substituting $x = S\xi$ and $y = S\eta$ (which is valid since $S$ is invertible and spans $H$), we get:
$$ \langle S\pi(k)S^{-1}x, S\pi(k)S^{-1}y \rangle = \langle x, y \rangle $$
This demonstrates that the conjugated representation $S\pi(k)S^{-1}$ is exactly unitary in the standard inner product of $H$, successfully unitarizing the uniformly bounded representation and verifying Dixmier's property for amenable groups.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*