---
id: 01-number-theory/cohen-lenstra-heuristics
title: "Cohen-Lenstra Heuristics"
topic: 01-number-theory
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cohen-Lenstra Heuristics

> **Topic:** Number Theory · **ID:** `01-number-theory/cohen-lenstra-heuristics` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The Cohen-Lenstra Heuristics form a set of precise conjectures concerning the statistical distribution of ideal class groups of algebraic number fields, primarily quadratic fields. The core conjecture states that for a fixed odd prime $p$, the $p$-Sylow subgroup (or $p$-part) of the ideal class group of a random quadratic field behaves like a "random" finite abelian $p$-group, where the probability of a group occurring is inversely proportional to the size of its automorphism group.

Specifically, as the fundamental discriminant $d \to \infty$:
1. **Imaginary Quadratic Fields:** The probability that the odd part of the class group of an imaginary quadratic field $\mathbb{Q}(\sqrt{-d})$ is isomorphic to a given finite abelian group $G$ of odd order is proportional to $\frac{1}{|\text{Aut}(G)|}$.
2. **Real Quadratic Fields:** The probability that the odd part of the class group of a real quadratic field $\mathbb{Q}(\sqrt{d})$ is isomorphic to $G$ is proportional to $\frac{1}{|G| \cdot |\text{Aut}(G)|}$.

A complete proof requires showing that the natural asymptotic density of discriminants whose fields yield a class group isomorphic to $G$ exactly matches this probability measure for all finite abelian groups $G$ of odd order. 

## 2. Mathematical Foundations

Let $K$ be a quadratic number field and let $\mathcal{O}_K$ be its ring of integers. The ideal class group $\text{Cl}(K)$ is the quotient group of fractional ideals modulo principal ideals. It measures how far $\mathcal{O}_K$ is from being a principal ideal domain. Let $\text{Cl}(K)_p$ denote the $p$-Sylow subgroup of $\text{Cl}(K)$.

Let $\mathcal{S}_p$ be the set of isomorphism classes of finite abelian $p$-groups. For any $G \in \mathcal{S}_p$, the Cohen-Lenstra probability measure is defined using a weighting function based on automorphisms. 

For **imaginary quadratic fields**, the weight assigned to a group $G$ is:
$$ w(G) = \frac{1}{|\text{Aut}(G)|} $$
The total mass of $\mathcal{S}_p$ under this weight is a convergent infinite product:
$$ W = \sum_{H \in \mathcal{S}_p} \frac{1}{|\text{Aut}(H)|} = \prod_{k=1}^{\infty} \left(1 - p^{-k}\right)^{-1} $$
Thus, the Cohen-Lenstra probability that $\text{Cl}(\mathbb{Q}(\sqrt{-d}))_p \cong G$ is conjectured to be:
$$ \mu_{\text{imag}}(G) = \frac{1}{W |\text{Aut}(G)|} = \left( \prod_{k=1}^{\infty} (1 - p^{-k}) \right) \frac{1}{|\text{Aut}(G)|} $$

For **real quadratic fields**, the presence of fundamental units fundamentally alters the statistics. The weight incorporates the size of the group itself:
$$ w^*(G) = \frac{1}{|G| \cdot |\text{Aut}(G)|} $$
The normalizing constant in this case is:
$$ W^* = \sum_{H \in \mathcal{S}_p} \frac{1}{|H| \cdot |\text{Aut}(H)|} = \prod_{k=2}^{\infty} \left(1 - p^{-k}\right)^{-1} $$
Yielding the probability measure:
$$ \mu_{\text{real}}(G) = \frac{1}{W^* |G| |\text{Aut}(G)|} = \left( \prod_{k=2}^{\infty} (1 - p^{-k}) \right) \frac{1}{|G| \cdot |\text{Aut}(G)|} $$

The heuristics are restricted to odd primes ($p \neq 2$) because the 2-part of the class group is constrained by Gauss's Genus Theory, which introduces deterministic structural biases not captured by a purely random model. (Extensions to the 2-part were later formulated by Gerth).

## 3. History & State of the Art (SOTA)

- **1984:** Henri Cohen and Hendrik W. Lenstra Jr. introduce the heuristics based on extensive numerical computations and a profound philosophical insight that nature chooses algebraic objects with a frequency inversely proportional to their symmetries (automorphisms).
- **1990:** Cohen and Jacques Martinet extend the heuristics to higher-degree number fields, though Gunter Malle later identifies structural deviations where roots of unity in the base field cause non-trivial biases.
- **1971:** Predating the full heuristic, Davenport and Heilbronn compute the average number of 3-torsion elements in quadratic class groups, establishing the first rigorously proven moment that matches Cohen-Lenstra.
- **2005:** Manjul Bhargava revolutionizes the field by proving the asymptotic distributions of cubic, quartic, and quintic fields, and evaluating higher moments of class groups, providing robust theoretical backing for the heuristics.
- **2016:** Jordan Ellenberg, Akshay Venkatesh, and Craig Westerland prove the Cohen-Lenstra heuristics for imaginary quadratic extensions over function fields $\mathbb{F}_q(T)$ in the limit as $q \to \infty$, utilizing homological stability of Hurwitz spaces.
- **2017–2022:** Alexander Smith achieves a major breakthrough by proving the distribution of the $2^\infty$-class groups of imaginary quadratic fields, confirming Gerth's extension of the Cohen-Lenstra heuristics.

## 4. Partial Results / Verified Cases

1. **The $3$-torsion ($p=3$):** Davenport and Heilbronn proved that the average size of the 3-torsion subgroup $\text{Cl}(K)[3]$ is exactly $2$ for imaginary quadratic fields and $\frac{4}{3}$ for real quadratic fields. This perfectly matches the first moments predicted by $\mu_{\text{imag}}$ and $\mu_{\text{real}}$.
2. **The 4-rank and 2-part:** Fouvry and Klüners (2006) proved the distribution of the 4-rank of quadratic fields. Alexander Smith (2017) proved the distribution of the entire $2$-part of the class group for imaginary quadratic fields, resolving Gerth's modification of the heuristics.
3. **Function Field Analogues:** For the rational function field $\mathbb{F}_q(T)$, Ellenberg, Venkatesh, and Westerland (2016) established that the Cohen-Lenstra heuristics hold for the $p$-part of the class groups of imaginary quadratic extensions, provided one takes the limit as $q \to \infty$ for fixed degree.

## 5. Principal Obstacles

The central difficulty in resolving the heuristics for number fields is the lack of a suitable geometric structure. 

In the function field case ($\mathbb{F}_q(T)$), a quadratic extension corresponds to a hyperelliptic curve. The class group is isomorphic to the group of $\mathbb{F}_q$-rational points on the curve's Jacobian variety. By utilizing the Weil Conjectures, counting these points translates into studying the étale cohomology of the moduli space of hyperelliptic curves. One can then apply homological stability to bound Betti numbers and derive asymptotic densities.

For number fields $\mathbb{Q}$, there is no analogous geometric object over a finite field. We lack both an equivalent of the Weil Conjectures to link arithmetic distributions to topology, and a Generalized Riemann Hypothesis (GRH) to sharply bound the error terms of analytic number theory approaches. Instead, proof techniques rely on the "Geometry of Numbers" (counting lattice points in fundamental domains of reductive group actions). While highly effective for small degrees (like Davenport-Heilbronn for degree 3 and Bhargava for degrees 4, 5), these methods suffer from exponential explosion in complexity and dimensionality for higher moments or primes $p \ge 5$.

## 6. The Gap

The gap lies between calculating the *first moment* of the distribution (the average size of the $p$-torsion, achieved for $p=3$) and calculating *all moments*, which is required to uniquely determine the full distribution measure $\mu$. Proving the general heuristic for a specific odd prime $p$ (e.g., $p=5$) over $\mathbb{Q}$ requires counting unramified $G$-extensions (for arbitrary $p$-groups $G$) over varying quadratic fields. Currently, no mathematical machinery exists capable of systematically parameterizing and counting these higher-order unramified extensions over $\mathbb{Q}$ as the discriminant tends to infinity.

## 7. Current Research (as of June 2026)

- **Moments and Universality:** Melanie Matchett Wood and collaborators are actively studying the moments of random abelian groups to generalize Cohen-Lenstra to non-abelian Galois groups and broader classes of random algebraic structures.
- **Arithmetic Topology:** Borrowing from the function field successes, researchers are using derived algebraic geometry and arithmetic topology (such as Mazur's analogy between primes and knots) to build spaces where homological stability arguments might apply to $\text{Spec}(\mathbb{Z})$. *(frontier — verify)*
- **Higher Torsion:** Efforts remain heavily focused on evaluating the average size of the $5$-torsion in the class groups of quadratic fields. This is viewed as the next necessary milestone for the geometry of numbers program led by Bhargava and his lineage.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- **Prove the $p=5$ case:** Establishing the average size of $\text{Cl}(K)[5]$ would validate whether geometry of numbers can scale beyond $p=3$.
- **Refining Cohen-Martinet:** Resolving the theoretical discrepancies found by Malle when roots of unity are present in the base field, thereby establishing a universally correct heuristic for any number field and any prime $p$.
- **Function Field Limits:** In the function field case, proving the distribution for a fixed $q$ as the genus $g \to \infty$, rather than the currently proven case of fixing $g$ and letting $q \to \infty$. This order of limits is much closer to the reality of the number field case.

## 9. Key References

- **[Foundational]** Cohen, H., & Lenstra, H. W. *Heuristics on class groups of number fields.* Number Theory, Noordwijkerhout 1983. Lecture Notes in Mathematics, vol 1068. Springer, 1984.
- **[SOTA / Recent]** Ellenberg, J. S., Venkatesh, A., & Westerland, C. *Homological stability for Hurwitz spaces and the "Cohen-Lenstra" conjecture over function fields.* Annals of Mathematics, 2016. [DOI](https://doi.org/10.4007/annals.2016.183.3.1)
- **[SOTA / Recent]** Smith, A. *$2^\infty$-Selmer groups, $2^\infty$-class groups, and heuristics for number fields.* arXiv:1702.02325, 2017.
- **[Survey]** Wood, M. M. *Cohen-Lenstra heuristics and random groups.* Proceedings of the International Congress of Mathematicians (ICM), 2022.

## 10. Worked Example / Concrete Special Case

Let us calculate the conjectured probability that the $3$-part of the class group of an imaginary quadratic field is trivial; that is, the class number is not divisible by $3$. We evaluate the probability for the trivial group $G = \{1\}$.

1. **Calculate the Automorphisms:** The trivial group has exactly 1 automorphism (the identity map). Thus, $|\text{Aut}(\{1\})| = 1$.
2. **Apply the Probability Measure:** We use the imaginary quadratic measure $\mu_{\text{imag}}(G)$ for $p=3$.
   $$ \mu_{\text{imag}}(\{1\}) = \left( \prod_{k=1}^{\infty} (1 - 3^{-k}) \right) \frac{1}{1} $$
3. **Compute the Infinite Product:** We approximate the rapidly converging product:
   $$ \prod_{k=1}^{\infty} (1 - 3^{-k}) = (1 - 1/3) \times (1 - 1/9) \times (1 - 1/27) \times (1 - 1/81) \times \dots $$
   $$ \approx \left(\frac{2}{3}\right) \times \left(\frac{8}{9}\right) \times \left(\frac{26}{27}\right) \times \left(\frac{80}{81}\right) \approx 0.560126 $$
4. **Conclusion:** The Cohen-Lenstra heuristic predicts that approximately **$56.01\%$** of all imaginary quadratic fields have a class number that is coprime to 3.

*Verification:* Exhaustive computational searches over negative fundamental discriminants down to $-10^9$ reveal that the empirical frequency of trivial $3$-class groups is exceedingly close to $56.01\%$, providing striking numerical validation for the abstract weighting mechanism.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*