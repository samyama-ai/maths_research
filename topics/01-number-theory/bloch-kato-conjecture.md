---
id: 01-number-theory/bloch-kato-conjecture
title: "Bloch-Kato Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bloch-Kato Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/bloch-kato-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Bloch-Kato conjecture (also known as the Tamagawa Number Conjecture of Bloch and Kato) is a vast generalization of the Birch and Swinnerton-Dyer conjecture, the analytic class number formula, and Dirichlet's unit theorem. It posits a precise algebraic relationship between the leading term of the $L$-function associated to a motive $M$ evaluated at a critical integer, and the order of a specific, algebraically defined group known as the Bloch-Kato Selmer group.

More formally, for a pure motive $M$ over a number field $K$ and a critical integer $r$, let $L(M, s)$ be its motivic $L$-function. The conjecture predicts that the leading non-zero coefficient of the Taylor expansion of $L(M, s)$ at $s = r$ is given by an explicit formula involving the product of the order of the motivic Tate-Shafarevich group, local Tamagawa factors, and a transcendental regulator (which links the motivic cohomology to Deligne cohomology), divided by the order of the torsion subgroup of the relevant Selmer group. A complete proof requires establishing both the existence (and finiteness) of these algebraic invariants and the exact rational equality relating them to the $L$-value.

## 2. Mathematical Foundations

Let $M$ be a pure motive over a number field $K$ with coefficients in a field $E$. Let $V$ be the associated $p$-adic Galois representation of the absolute Galois group $G_K = \text{Gal}(\overline{K}/K)$. 

Bloch and Kato define local subgroups $H^1_f(K_v, V)$ of the continuous Galois cohomology group $H^1(K_v, V)$ for each place $v$ of $K$. For places $v \nmid p\infty$, this is defined using the inertia group $I_v$:
$$ H^1_f(K_v, V) = \ker\left( H^1(K_v, V) \to H^1(I_v, V) \right) $$

For places $v \mid p$, $H^1_f(K_v, V)$ is defined utilizing Fontaine's $p$-adic Hodge theory, specifically the crystalline period ring $B_{\text{crys}}$:
$$ H^1_f(K_v, V) = \ker\left( H^1(K_v, V) \to H^1(K_v, V \otimes_{\mathbb{Q}_p} B_{\text{crys}}) \right) $$

The global Bloch-Kato Selmer group is then defined as the subgroup of classes locally satisfying these conditions everywhere:
$$ H^1_f(K, V) = \ker\left( H^1(K, V) \to \prod_v \frac{H^1(K_v, V)}{H^1_f(K_v, V)} \right) $$

Let $T \subset V$ be a $G_K$-stable lattice. The Selmer groups with coefficients in $T$ and the divisible module $V/T$ are defined similarly. The core formula of the conjecture states that the leading coefficient of $L(M, s)$ at $s=0$ (after suitable Tate twists) is given by:
$$ \frac{L^*(M, 0)}{\Omega(M) R(M)} = \prod_p \frac{\\# \text{III}(M)(p)}{\\# H^0(K, V/T)(p) \cdot \\# H^0(K, V^*(1)/T^*)(p)} \prod_v c_v(M) $$
where $\Omega(M)$ is a Deligne period, $R(M)$ is the Beilinson-Bloch regulator, $\text{III}(M)$ is the motivic Tate-Shafarevich group (the quotient of the full Selmer group by the image of motivic cohomology), and $c_v(M)$ are the local Tamagawa factors.

## 3. History & State of the Art (SOTA)

The conjecture was formulated by Spencer Bloch and Kazuya Kato in their seminal 1990 paper "L-functions and Tamagawa numbers of motives". It successfully merged and generalized Deligne's conjecture on critical values (which predicted only the rationality of the $L$-value relative to a period) and Beilinson's conjectures (which introduced higher regulators). 

In the 1990s, Jean-Marc Fontaine and Bernadette Perrin-Riou elegantly reformulated the conjecture using the language of Euler systems, $p$-adic $L$-functions, and determinants of perfect complexes, birthing the Equivariant Tamagawa Number Conjecture (ETNC).

Major historical milestones include Kazuya Kato's 2004 construction of Euler systems for modular forms, proving one divisibility of the conjecture for elliptic curves over $\mathbb{Q}$. This was complemented by the 2014 Skinner-Urban proof of the Iwasawa Main Conjecture for $GL_2$, which, under mild hypotheses, implies the full $p$-part of the Bloch-Kato conjecture for modular forms.

## 4. Partial Results / Verified Cases

- **Dirichlet Motives (Number Fields):** For the Tate motive $\mathbb{Q}(0)$ over an abelian extension of $\mathbb{Q}$, the conjecture is unconditionally proven as it is equivalent to the analytic class number formula.
- **Elliptic Curves over $\mathbb{Q}$:** For elliptic curves with complex multiplication (CM), the conjecture was largely proven by Karl Rubin (1991) using Euler systems of elliptic units. For modular elliptic curves without CM of analytic rank 0 or 1, Kato's Euler system, combined with the work of Skinner-Urban on the Iwasawa Main Conjecture, proves the $p$-part of the conjecture for primes of good ordinary reduction.
- **Totally Real Fields:** The equivariant version of the conjecture for Tate motives over totally real fields has seen massive progress, culminating in proofs of the Brumer-Stark conjecture by Dasgupta and Kakde.

## 5. Principal Obstacles

- **Construction of Euler Systems:** The primary tool for bounding Selmer groups and relating them to $L$-functions is the theory of Euler systems (e.g., cyclotomic units, Heegner points). Constructing Euler systems for higher-dimensional Shimura varieties or higher-rank motives remains notoriously difficult, as standard geometric techniques do not easily generalize.
- **Finiteness of Tate-Shafarevich Groups:** The formula relies on the finiteness of $\text{III}(M)$. However, outside of elliptic curves of analytic rank 0 or 1 (where Kolyvagin's theorems apply), the finiteness of $\text{III}(M)$ is completely unknown. Without finiteness, the order is undefined, leaving the rational equality formally unprovable.
- **Supersingular and Ramified Primes:** The $p$-adic Hodge theoretic methods used to relate $p$-adic $L$-functions to Selmer groups face massive structural hurdles for primes of non-ordinary (supersingular) reduction, as the local Galois representations do not admit simple filtrations.

## 6. The Gap

The boundary of current knowledge lies precisely between rank 0 or 1 motives (where Kolyvagin-style systems can be leveraged) and higher-rank motives. To fully resolve the conjecture, the field must cross two massive barriers: 
1. Developing a generalized, systematic mechanism to construct Euler systems (or Kolyvagin systems) for arbitrary motives attached to automorphic representations (such as general $GL_n$).
2. Discovering a purely algebraic proof for the finiteness of the Tate-Shafarevich group for motives of rank $\ge 2$, which currently represents an absolute wall preventing researchers from upgrading $p$-adic divisibility bounds to exact rational equalities.

## 7. Current Research (as of June 2026)

- **Higher Euler Systems:** Active research led by schools surrounding Loeffler, Zerbes, and their collaborators focuses on constructing Euler systems for $GL_2 \times GL_2$, $GL_2 \times GL_2 \times GL_2$, and $GSp_4$, utilizing the geometry of Shimura varieties and cycle classes.
- **$p$-adic $L$-functions for Higher Rank Groups:** The construction of $p$-adic $L$-functions for unitary groups (e.g., by Eischen, Harris, Li, Skinner) is aggressively being used to attack the Iwasawa Main Conjecture for motives over CM fields. *(frontier — verify)*
- **Derived Galois Deformation Rings:** Recent techniques involving derived Galois deformation theory and Taylor-Wiles patching are being adapted to bypass the need for traditional Euler systems, aiming to bound Selmer groups using the cohomology of arithmetic manifolds.

## 8. Future Work

- **Finiteness of $\text{III}$:** The most profound open pathway is finding a geometric or arithmetic mechanism to prove the finiteness of the Tate-Shafarevich group for elliptic curves of rank $\ge 2$.
- **Bipartite Euler Systems:** Generalizing the theory of bipartite Euler systems and anticyclotomic Iwasawa theory to uniformly tackle supersingular primes for motives beyond $GL_2$.
- **The ETNC for Non-Abelian Extensions:** Extending the full Equivariant Tamagawa Number Conjecture to non-abelian Galois extensions, which requires deep advances in non-commutative Iwasawa theory.

## 9. Key References

- **[Foundational]** Bloch, S., & Kato, K. *L-functions and Tamagawa numbers of motives.* The Grothendieck Festschrift, Vol. I (pp. 333-400), Birkhäuser, Boston, 1990.
- **[Foundational]** Fontaine, J. M., & Perrin-Riou, B. *Autour des conjectures de Bloch et Kato: cohomologie galoisienne et valeurs de fonctions L.* Motives (Seattle, WA, 1991), Proc. Sympos. Pure Math, Vol. 55, 1994.
- **[SOTA / Recent]** Skinner, C., & Urban, E. *The Iwasawa main conjectures for $GL_2$.* Inventiones mathematicae, 195(1), 1-277, 2014.
- **[SOTA / Recent]** Loeffler, D., & Zerbes, S. L. *Euler systems for Rankin-Selberg convolutions of modular forms.* Annals of Mathematics, 180(2), 653-717, 2014. [DOI](https://doi.org/10.4007/annals.2014.180.2.6)
- **[Survey]** Flach, M. *The equivariant Tamagawa number conjecture: a survey.* Stark's conjectures: recent work and new directions, Contemp. Math, Vol. 358, 2004. [DOI](https://doi.org/10.1090/conm/358/06537)

## 10. Worked Example / Concrete Special Case

Consider the simplest non-trivial motive: the Tate motive $M = \mathbb{Q}(1)$, which is the motive associated to the multiplicative group $\mathbb{G}_m$ over a number field $K$. 

The associated Galois representation is $V = \mathbb{Q}_p(1)$, the $p$-adic cyclotomic character. The $L$-function of this motive is simply the Dedekind zeta function of $K$, shifted by 1:
$$ L(\mathbb{Q}(1)_K, s) = \zeta_K(s) $$
The critical value of interest is at $s = 0$. By classical complex analysis, the leading term of the Taylor expansion of $\zeta_K(s)$ at $s=0$ is given by:
$$ \lim_{s \to 0} s^{-(r_1 + r_2 - 1)} \zeta_K(s) = -\frac{h_K R_K}{w_K} $$
where $h_K$ is the class number of $K$, $R_K$ is the Dirichlet regulator, $w_K$ is the number of roots of unity in $K$, and $r_1, r_2$ are the number of real and complex embeddings.

In the language of the Bloch-Kato conjecture for $\mathbb{Q}(1)_K$:
- The Selmer group $H^1_f(K, \mathbb{Q}_p(1)/\mathbb{Z}_p(1))$ is canonically isomorphic to the $p$-part of the ideal class group of $K$, whose size connects to $h_K$.
- The global torsion group $H^0(K, \mathbb{Q}_p(1)/\mathbb{Z}_p(1))$ gives the $p$-part of the roots of unity, connecting to $w_K$.
- The Beilinson-Bloch regulator $R(M)$ reduces precisely to the Dirichlet regulator $R_K$.
- The Tate-Shafarevich group $\text{III}(\mathbb{Q}(1)_K)$ is unconditionally trivial.

Substituting these invariant sizes into the general Bloch-Kato formula (see Section 2), the local Tamagawa factors $c_v$ trivially resolve, and the abstract motivic equality simplifies to exactly the classical analytic class number formula. This demonstrates how the Bloch-Kato conjecture elegantly absorbs 19th-century algebraic number theory as its most foundational base case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*