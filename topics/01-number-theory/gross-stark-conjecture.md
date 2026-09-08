---
id: 01-number-theory/gross-stark-conjecture
title: "Gross-Stark Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gross-Stark Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/gross-stark-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Gross-Stark conjecture is a $p$-adic analogue of Stark's conjecture regarding the behavior of Artin $L$-functions at $s=0$. It predicts a precise formula for the leading term of the Deligne–Ribet $p$-adic $L$-function associated to a totally even character of a totally real number field, evaluated at $s=0$. 

Let $K$ be a totally real number field, and let $F$ be a finite abelian extension of $K$. Let $\chi$ be a totally even character of the Galois group $G = \text{Gal}(F/K)$. Let $S$ be a finite set of places of $K$ containing the infinite places, all primes ramified in $F$, and all primes above $p$. Let $\omega$ denote the Teichmüller character, and let $L_{p, S}(\chi \omega, s)$ be the Deligne–Ribet $p$-adic $L$-function. 

In the "rank-one" setting, exactly one prime $\mathfrak{p} \in S$ above $p$ splits completely in the field extension cut out by $\chi$. Because of the $p$-adic Euler factor, the $L$-function has an exceptional zero at $s=0$. The rank-one Gross-Stark conjecture claims that the first derivative at this zero satisfies:

$$ L'_{p, S}(\chi \omega, 0) = L_{S \setminus \{\mathfrak{p}\}}(\chi, 0) \cdot \mathscr{L}_p(\chi) $$

where $L_{S \setminus \{\mathfrak{p}\}}(\chi, 0)$ is the algebraic part of the classical complex $L$-function at $s=0$ (with the Euler factor at $\mathfrak{p}$ removed), and $\mathscr{L}_p(\chi)$ is the $p$-adic $\mathscr{L}$-invariant (a $p$-adic regulator constructed from Stark units). A complete proof for higher-rank cases requires generalizing this formula for higher-order derivatives and higher-rank unit determinants.

## 2. Mathematical Foundations

Let $K$ be a totally real field and $p$ a prime number. Let $\chi: \text{Gal}(\bar{K}/K) \to \mathbb{C}_p^\times$ be a totally even Galois character of finite order, cutting out a totally real abelian extension $F_\chi / K$. 

The **Deligne–Ribet $p$-adic $L$-function** $L_{p, S}(\chi\omega, s)$ is a continuous $p$-adic function of $s \in \mathbb{Z}_p$ uniquely characterized by its interpolation property at strictly positive integers $n \equiv 0 \pmod{p-1}$:

$$ L_{p, S}(\chi\omega, 1-n) = L_S(\chi \omega^n, 1-n) $$

where $L_S$ is the complex Artin $L$-function with the Euler factors at primes in $S$ removed. When $\chi(\mathfrak{p}) = 1$ for exactly one prime $\mathfrak{p} \mid p$, the interpolation formula yields an "exceptional zero" at $s=0$, meaning $L_{p, S}(\chi\omega, 0) = 0$. 

The **$p$-adic $\mathscr{L}$-invariant** is defined via class field theory and Stark units. Let $U$ be the group of $S$-units in $F_\chi$. Stark's conjecture (which is known for abelian extensions) implies the existence of a $\mathfrak{p}$-unit $u \in U \otimes \mathbb{Z}$ (the Stark unit) such that its complex regulator evaluates to $L'_{S \setminus \{\mathfrak{p}\}}(\chi, 0)$. The $\mathscr{L}$-invariant is defined algebraically using the Iwasawa $p$-adic logarithm $\log_p$:

$$ \mathscr{L}_p(\chi) = \sum_{\sigma \in \text{Gal}(F_\chi/K)} \chi(\sigma) \log_p(\sigma(u)) $$

## 3. History & State of the Art (SOTA)

Benedict Gross first proposed the conjecture in his 1981 paper "$p$-adic $L$-series at $s=0$". It served as a critical bridge linking $p$-adic $L$-functions to $p$-adic regulators of global units, perfectly mirroring how classical $L$-functions relate to Archimedean regulators via the Dirichlet class number formula.

For decades, the conjecture saw only partial progress. In 2011, Henri Darmon, Samit Dasgupta, and Robert Pollack achieved a breakthrough by proving the rank-one case conditional on the Leopoldt conjecture for the field $F$. Shortly after, Kevin Ventullo successfully removed the reliance on Leopoldt's conjecture. Finally, in 2018, Dasgupta, Kakde, and Ventullo published the full unconditional proof of the rank-one Gross-Stark conjecture in the *Annals of Mathematics* utilizing the deformation theory of Galois representations and Hida families. 

Despite this triumph, the general **higher-rank Gross-Stark conjecture**—where multiple primes split and the $L$-function vanishes to order $r \ge 2$—remains partially solved and a major open problem in contemporary number theory.

## 4. Partial Results / Verified Cases

- **Base field $K=\mathbb{Q}$**: The conjecture holds unconditionally. This follows directly from the Ferrero-Greenberg theorem (1979) on the non-vanishing of the derivative of the Kubota-Leopoldt $p$-adic $L$-function and the classical formula for circular units.
- **The Rank-One Abelian Case**: Proven unconditionally for all totally real number fields $K$ and finite abelian extensions $F/K$ by Dasgupta, Kakde, and Ventullo (2018).
- **Special Cases of Rank Two**: Certain isolated numerical verifications and theoretical simplifications have been achieved, primarily when the relevant Galois groups have specific constraints (e.g., multiquadratic extensions or working away from $p$), but no general structural proof exists for rank $r \ge 2$.

## 5. Principal Obstacles

The primary obstacle to proving the higher-rank Gross-Stark conjecture is the failure of the "Ribet method" (which uses congruences between cusp forms and Eisenstein series) to generalize smoothly to higher-order deformations.

In the rank-one case, the proof relies heavily on constructing a family of Hilbert modular forms (a Hida family) whose constant terms interpolate the $p$-adic $L$-functions, and demonstrating that the derivative at $s=0$ is linked to a single $p$-adic logarithm via Galois cohomology. 

For higher rank $r \ge 2$, the regulator $\mathscr{L}_p(\chi)$ is an $r \times r$ determinant of $p$-adic logarithms (tied closely to Rubin's lattice). Current techniques in the deformation theory of Galois representations struggle to construct these higher-order determinants directly from the Fourier coefficients of modular forms. There is no known arithmetic framework to systematically extract an $r \times r$ determinant of units from the higher-order derivative of an Eisenstein family.

## 6. The Gap

The boundary between the proven rank-one case and the general statement lies precisely in the geometry of modular curves versus higher-rank arithmetic data. To cross this gap, mathematicians must fundamentally link the $r$-th derivative of the Deligne-Ribet $L$-function $L_{p, S}^{(r)}(\chi \omega, 0)$ to the $r$-th exterior power of the unit group $\bigwedge^r U$. Bridging this boundary likely requires a fully developed theory of higher-rank Euler systems or a derived version of Hida theory that can cleanly track higher-order intersection data in cohomology.

## 7. Current Research (as of June 2026)

Active research centers around generalizing exact sequence methods from the rank-one proof to higher-dimensional algebraic cycles.
- **Higher-Rank Euler Systems:** Groups are investigating whether higher-rank Euler systems, such as those constructed from Beilinson-Flach elements, can directly compute the necessary regulator determinants.
- **Derived Deformation Rings:** There is a growing effort to use derived Galois deformation theory—where the tangent complex encodes higher-order derived structures—to naturally capture the $r \times r$ determinant *(frontier — verify)*. 
- **Equivariant Tamagawa Number Conjecture (eTNC):** The higher-rank Gross-Stark conjecture is deeply intertwined with the $p$-part of the eTNC for the Tate motive $\mathbb{Z}(0)$. Many researchers are attempting to prove higher-rank Gross-Stark indirectly by first proving cases of the eTNC.

## 8. Future Work

Leading mathematicians suggest three primary pathways for future exploration:
1.  **Formulating a Derived Ribet's Lemma:** Extending Ribet's construction of extension classes to yield elements in higher cohomology groups that match the components of Rubin's lattice.
2.  **Non-abelian Gross-Stark:** Formulating and proving analogues for Artin characters of non-abelian extensions of totally real fields, where the representation theory and corresponding $L$-functions become significantly more complex.
3.  **Algorithmic Verification:** Developing faster algorithms to compute higher-order derivatives of $p$-adic $L$-functions to provide extensive numerical evidence for rank $r \ge 3$, which can guide theoretical formulations.

## 9. Key References

- **[Foundational]** Gross, B. H. *p-adic L-series at s=0.* Journal of the Faculty of Science, the University of Tokyo, 1981.
- **[SOTA / Recent]** Dasgupta, S., Kakde, M., & Ventullo, K. *On the Gross–Stark conjecture.* Annals of Mathematics, 2018.
- **[Survey]** Darmon, H., Dasgupta, S., & Pollack, R. *Hilbert modular forms and the Gross-Stark conjecture.* Annals of Mathematics, 2011. [DOI](https://doi.org/10.4007/annals.2011.174.1.12)

## 10. Worked Example / Concrete Special Case

Consider the simplest rank-one case where the base field $K = \mathbb{Q}$. Let $p$ be an odd prime and let $\chi$ be a non-trivial even Dirichlet character (so $\chi(-1)=1$) such that $\chi(p) = 1$. The extension $F$ is a real subfield of a cyclotomic field $\mathbb{Q}(\mu_N)^+$.

Because $\chi(p) = 1$, the $p$-adic Euler factor $(1 - \chi(p)p^{-s})$ vanishes at $s=0$. The $p$-adic $L$-function $L_p(\chi \omega, s)$ is the classical Kubota-Leopoldt $p$-adic $L$-function. Because of the missing Euler factor, we have an exceptional zero:

$$ L_p(\chi \omega, 0) = (1 - \chi(p)) L(\chi, 0) = 0 $$

By the classical Stark conjecture over $\mathbb{Q}$ (Dirichlet's class number formula context), the value $L(\chi, 0)$ is related to the logarithm of cyclotomic units. Let $u$ be the cyclotomic unit corresponding to the character $\chi$. Gross's conjecture predicts that the derivative at this exceptional zero is precisely the $p$-adic logarithm of this unit scaled by the classical $L$-value:

$$ L'_p(\chi \omega, 0) = L(\chi, 0) \log_p(\text{Norm}(u)) $$

(up to precise normalizing factors inherent to the character). Here, $\mathscr{L}_p(\chi) = \log_p(\text{Norm}(u))$ is the $p$-adic $\mathscr{L}$-invariant. This specific case is completely solved via the Ferrero-Greenberg theorem, which explicitly computes the derivative of the Kubota-Leopoldt $L$-function using $p$-adic Gamma functions, perfectly matching the $p$-adic logarithm of the cyclotomic unit predicted by Gross.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*