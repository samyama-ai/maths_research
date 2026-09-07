---
id: 01-number-theory/greenbergs-conjecture
title: "Greenberg's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Greenberg's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/greenbergs-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Greenberg's Conjecture is a central open problem in algebraic number theory, specifically within the domain of Iwasawa theory. It posits that for any totally real number field $k$ and any prime number $p$, the Iwasawa invariants $\mu_p(k)$ and $\lambda_p(k)$ both vanish.

Let $k$ be a totally real number field and let $k_\infty$ be the cyclotomic $\mathbb{Z}_p$-extension of $k$. Let $k_n$ denote the intermediate field such that $[k_n : k] = p^n$, and let $A_n$ be the $p$-Sylow subgroup of the ideal class group of $k_n$. By Iwasawa's Theorem, the order of $A_n$ is given by $|A_n| = p^{e_n}$, where for sufficiently large $n$, 
$$ e_n = \mu p^n + \lambda n + \nu $$
for some integers $\mu, \lambda \ge 0$ and $\nu$. 

Greenberg explicitly conjectured that $\mu = 0$ and $\lambda = 0$. Equivalently, the conjecture states that the $p$-primary part of the ideal class groups $A_n$ is bounded as $n \to \infty$ for the cyclotomic $\mathbb{Z}_p$-extension of any totally real number field.

## 2. Mathematical Foundations

The conjecture is formulated using the machinery of Iwasawa theory. 

Let $p$ be a prime and $k$ a number field. The cyclotomic $\mathbb{Z}_p$-extension $k_\infty / k$ is the unique extension of $k$ with Galois group $\Gamma = \text{Gal}(k_\infty/k) \cong \mathbb{Z}_p$ contained in the field obtained by adjoining all $p$-power roots of unity to $k$.

We define the inverse limit of the $p$-class groups under the norm maps:
$$ X = \varprojlim_{n} A_n $$
The group $\Gamma$ acts on $X$, making $X$ a module over the Iwasawa algebra:
$$ \Lambda = \mathbb{Z}_p[[\Gamma]] \cong \mathbb{Z}_p[[T]] $$
where the isomorphism is given by mapping a chosen topological generator $\gamma \in \Gamma$ to $1 + T$.

Iwasawa proved that $X$ is a finitely generated torsion $\Lambda$-module. By the structure theorem for such modules, there exists a pseudo-isomorphism (a homomorphism with finite kernel and cokernel):
$$ X \sim \left( \bigoplus_{i=1}^s \Lambda / (p^{m_i}) \right) \oplus \left( \bigoplus_{j=1}^t \Lambda / (f_j(T)^{k_j}) \right) $$
where $f_j(T) \in \mathbb{Z}_p[T]$ are distinguished polynomials (monic, with all non-leading coefficients divisible by $p$).

The Iwasawa invariants are defined as:
$$ \mu = \sum_{i=1}^s m_i \quad \text{and} \quad \lambda = \sum_{j=1}^t k_j \deg(f_j) $$

A number field $k$ is called *totally real* if for every embedding $\sigma: k \hookrightarrow \mathbb{C}$, the image $\sigma(k)$ is contained in $\mathbb{R}$. Greenberg's Conjecture states that if $k$ is totally real, then $X$ is finite, which strictly forces $\mu = \lambda = 0$.

## 3. History & State of the Art (SOTA)

The asymptotic formula for the $p$-class group of a $\mathbb{Z}_p$-extension was established by Kenkichi Iwasawa in 1959. For years, the behavior of the invariants $\mu$ and $\lambda$ was mysterious. In 1979, Ferrero and Washington proved that $\mu = 0$ for any abelian extension of $\mathbb{Q}$, leading to the widely accepted generalization that $\mu = 0$ for *all* number fields (the Iwasawa-Iwasawa or Iwasawa-Leopoldt conjecture on $\mu$).

In 1976, Ralph Greenberg published "On the Iwasawa invariants of totally real number fields," where he observed that while $\lambda$ is strictly positive for CM fields (due to the presence of non-trivial $p$-adic $L$-functions that vanish at zero), the algebraic structures governing totally real fields lack this analytic vanishing behavior. He formalized this observation into the conjecture that $\lambda = 0$ for all totally real fields.

To date, the conjecture has been verified computationally for vast ranges of real quadratic fields and small primes, but a general proof remains elusive. The current state of the art relies heavily on Euler systems and class field theory, but these tools primarily restrict success to abelian fields where cyclotomic units or Brumer-Stark units are available.

## 4. Partial Results / Verified Cases

Greenberg's Conjecture is partially solved and empirically verified in several specific regimes:

1. **Abelian Fields with Specific Primes:** It is proven for various abelian fields $k$ over $\mathbb{Q}$ under conditions where $p$ satisfies specific congruence properties or does not split in certain ways (e.g., Vandiver's conjecture holds for $p$ and $k=\mathbb{Q}$).
2. **Computational Verification (Real Quadratic Fields):** For $k = \mathbb{Q}(\sqrt{d})$, the conjecture has been exhaustively verified for small primes ($p = 3, 5, 7$) and fundamental discriminants $d$ up to $10^7$ using algorithmic algebraic number theory and the computation of $p$-adic $L$-functions.
3. **Semi-simple cases:** If $k$ is an abelian extension of $\mathbb{Q}$ and $p \nmid [k:\mathbb{Q}]$, the $\lambda$-invariant vanishes for the $p$-adic components associated with even characters.
4. **Trivial cases via Class Number:** By Nakayama's Lemma, if $p$ does not divide the class number $h(k)$ and exactly one prime of $k$ lies above $p$, then $\lambda = \mu = 0$.

## 5. Principal Obstacles

The fundamental bottleneck in proving Greenberg's Conjecture is the lack of canonical algebraic elements (like an Euler system) for arbitrary, non-abelian totally real number fields. 

In the theory of CM fields or abelian extensions of $\mathbb{Q}$, mathematicians use cyclotomic units or elliptic units to bound the size of the ideal class group via the Iwasawa Main Conjecture. These units provide a tangible bridge between the algebraic object ($X$) and analytic objects ($p$-adic $L$-functions).

For a non-abelian totally real field $k$, there is no naturally occurring, purely algebraic construction of units that behaves well in the $\mathbb{Z}_p$-tower. Without an Euler system, bounding the size of the unramified Iwasawa module $X$ is exceedingly difficult because the "capitulation" of ideal classes (ideals becoming principal when lifted to $k_n$) becomes highly chaotic and nonlinear. Furthermore, $p$-adic analytic methods struggle because they rely on the non-vanishing of $p$-adic $L$-functions at $s=0$, which is intertwined with the still-open Leopoldt's Conjecture.

## 6. The Gap

The exact mathematical barrier is extending the finiteness of $X$ from fields where we have explicit class field theory (abelian extensions) to fields where we do not. The gap lies between knowing that the characteristic ideal of $X$ is generated by a power series related to a $p$-adic $L$-function (via the Iwasawa Main Conjecture, proven by Wiles for totally real fields) and proving that this power series is actually a unit in $\mathbb{Z}_p[[T]]$. Proving it is a unit requires showing that the $p$-adic $L$-function has no zeros in the unit disc of $\mathbb{C}_p$, which current $p$-adic analytic techniques are too weak to guarantee unconditionally.

## 7. Current Research (as of June 2026)

Active research continues in several highly sophisticated directions:
- **Brumer-Stark Units:** Following the landmark proof of the Brumer-Stark conjecture by Dasgupta and Kakde (2023), researchers are attempting to use the newly constructed $p$-adic Stark units to build partial Euler systems for totally real fields. 
- **Non-commutative Iwasawa Theory:** Analyzing the growth of class groups in $p$-adic Lie extensions (rather than just $\mathbb{Z}_p$-extensions) to glean structural constraints on the base commutative tower.
- **Heuristic Modeling:** Extending Cohen-Lenstra heuristics to $\mathbb{Z}_p$-extensions to provide precise probabilistic models of how often the $p$-part of the class group increases, thereby guiding computational searches.
- *(frontier — verify)* Recent preprints claim to bound the $\lambda$-invariant for non-abelian totally real fields of degree $S_3$ by leveraging the Galois equivariance of $p$-adic Stark units, though the full transition to $\lambda=0$ remains incomplete.

## 8. Future Work

Leading number theorists propose several pathways to tackle the problem:
1. **Unconditional Construction of Euler Systems:** Generalizing the Gross-Stark conjecture and constructing a full Euler system over totally real fields using motives or higher algebraic K-theory.
2. **Equivariant Main Conjectures:** Fully resolving the Equivariant Iwasawa Main Conjecture for totally real fields, which could place strict algebraic limits on the $\Lambda$-module $X$.
3. **Function Field Analogues:** Deepening the study of Greenberg's Conjecture in the function field setting (over $\mathbb{F}_q(T)$), where the geometry of curves might offer a geometric intuition for why totally real (or "totally split" infinite places) force $\lambda = 0$.

## 9. Key References

- **[Foundational]** Greenberg, R. *On the Iwasawa invariants of totally real number fields.* American Journal of Mathematics, 1976.
- **[Foundational]** Iwasawa, K. *On $\Gamma$-extensions of algebraic number fields.* Bulletin of the American Mathematical Society, 1959.
- **[Foundational]** Ferrero, B., & Washington, L. C. *The Iwasawa invariant $\mu_p$ vanishes for abelian number fields.* Annals of Mathematics, 1979.
- **[SOTA / Recent]** Dasgupta, S., & Kakde, M. *On the Brumer-Stark Conjecture.* Annals of Mathematics, 2023.
- **[Survey]** Washington, L. C. *Introduction to Cyclotomic Fields* (2nd Ed.). Springer-Verlag, 1997.

## 10. Worked Example / Concrete Special Case

To understand the conjecture, consider a concrete, computationally trivial instance where we can easily verify Greenberg's Conjecture manually.

Let $k = \mathbb{Q}(\sqrt{2})$. This is a real quadratic field, hence it is totally real. 
Let $p = 3$. We examine the cyclotomic $\mathbb{Z}_3$-extension $k_\infty / k$.

1. **Class Number Base Case:** The class number of $k = \mathbb{Q}(\sqrt{2})$ is $h_k = 1$. Therefore, the $3$-Sylow subgroup of the class group of $k$ is trivial ($A_0 = 0$). Thus, $3 \nmid h_k$.
2. **Ramification of $p$:** We check how the prime $p=3$ splits in $k$. The minimal polynomial of $\sqrt{2}$ is $x^2 - 2$. Modulo $3$, we have $x^2 - 2 \equiv x^2 + 1 \pmod 3$. Since $x^2 + 1$ has no roots in $\mathbb{F}_3$, the polynomial is irreducible. Therefore, the prime $3$ is **inert** in $k$. This means there is exactly one prime ideal $\mathfrak{p} = \langle 3 \rangle$ in $k$ lying above $3$.
3. **Lift to the Tower:** Because $\mathfrak{p}$ is the unique prime above $3$, and $3$ is totally ramified in the cyclotomic extension $\mathbb{Q}_\infty / \mathbb{Q}$, the prime $\mathfrak{p}$ is totally ramified in the tower $k_\infty / k$.
4. **Iwasawa's Finiteness Criterion:** A standard application of Nakayama's Lemma in Iwasawa theory states that if $A_0 = 0$ and there is exactly one prime of $k$ above $p$ which totally ramifies in $k_\infty/k$, then the class group $p$-parts $A_n$ remain trivial for all layers $n$. 

Consequently, for $k = \mathbb{Q}(\sqrt{2})$ and $p = 3$:
$$ |A_n| = 1 = 3^0 \quad \text{for all } n \ge 0 $$
Matching this with the formula $|A_n| = 3^{\mu 3^n + \lambda n + \nu}$, we find $e_n = 0$. Thus:
$$ \mu_3(\mathbb{Q}(\sqrt{2})) = 0, \quad \lambda_3(\mathbb{Q}(\sqrt{2})) = 0, \quad \nu_3(\mathbb{Q}(\sqrt{2})) = 0 $$
This provides a rigorous, concrete validation of Greenberg's Conjecture ($\mu=\lambda=0$) for this specific totally real field and prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*