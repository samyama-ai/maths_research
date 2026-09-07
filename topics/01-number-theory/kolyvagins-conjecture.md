---
id: 01-number-theory/kolyvagins-conjecture
title: "Kolyvagin's Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kolyvagin's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/kolyvagins-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Kolyvagin's conjecture posits the non-triviality of the Euler system of Heegner points associated with an elliptic curve, providing a profound link between analytic L-functions and algebraic Selmer groups. 

Let $E$ be an elliptic curve over $\mathbb{Q}$ and $p$ an odd prime. Let $K$ be an imaginary quadratic field satisfying the Heegner hypothesis for $E$ (all prime factors of the conductor $N$ of $E$ split in $K$). By applying derivative operators to Heegner points over ring class fields $K_n$, one constructs a system of cohomology classes $\kappa_n \in H^1(K, E[p])$. 

Let $M(n)$ denote the $p$-divisibility index of the class $\kappa_n$, and let $M_r$ be the minimum of $M(n)$ over all squarefree integers $n$ that are products of $r$ distinct "Kolyvagin primes." The sequence of minimal divisibilities is monotonic: $M_0 \ge M_1 \ge M_2 \ge \dots \ge 0$, and thus stabilizes to a limit $M_\infty$. 

Kolyvagin's conjecture states that this Euler system is non-trivial; strictly, that $M_\infty < \infty$. Equivalently, there exists some integer $n$ (with $r$ prime factors) for which the derived Heegner cohomology class $\kappa_n$ does not vanish in $H^1(K, E[p])$. This non-triviality is the critical step required to bound the size of the $p$-Selmer group of $E$ and verify the $p$-part of the Birch and Swinnerton-Dyer (BSD) conjecture.

## 2. Mathematical Foundations

Let $E/\mathbb{Q}$ be an elliptic curve of conductor $N$ and $p$ an odd prime. Let $K$ be an imaginary quadratic field satisfying the *Heegner hypothesis*: every prime factor $q \mid N$ splits in $K$.

For any squarefree integer $n$, let $K_n$ denote the ring class field of $K$ of conductor $n$. A prime $\ell$ is called a *Kolyvagin prime* if it satisfies:
1. $\ell \nmid Np$
2. $\ell$ is inert in $K$
3. $a_\ell \equiv \ell + 1 \equiv 0 \pmod p$, where $a_\ell = \ell + 1 - \\#E(\mathbb{F}_\ell)$.

Let $\Lambda_r$ be the set of squarefree integers $n$ that are products of $r$ distinct Kolyvagin primes. For $n \in \Lambda_r$, let $y_n \in E(K_n)$ be the associated Heegner point.

We define the *Kolyvagin derivative* $D_\ell$ for each Kolyvagin prime $\ell \mid n$ as:
$$ D_\ell = \sum_{i=1}^{\ell} i \sigma_\ell^i \in \mathbb{Z}[\text{Gal}(K_n/K)] $$
where $\sigma_\ell$ is a fixed generator of $\text{Gal}(K_n/K_{n/\ell})$. The *derived Heegner point* is:
$$ P_n = \left( \prod_{\ell \mid n} D_\ell \right) y_n \in E(K_n) $$

Modulo $p$, the image of $P_n$ is fixed by the Galois group $\text{Gal}(K_n/K)$. By applying the Kummer map, $P_n$ descends to a cohomology class:
$$ \kappa_n \in H^1(K, E[p]) $$
This family $\{\kappa_n\}$ constitutes the *Kolyvagin system*.

Let $M(n)$ denote the $p$-divisibility index of $\kappa_n$, defined as the maximal integer $M$ such that $\kappa_n$ lies in the image of the natural map $H^1(K, E[p^M]) \to H^1(K, E[p])$. 
Define the minimum divisibility at depth $r$:
$$ M_r = \min_{n \in \Lambda_r} M(n) $$

Kolyvagin proved that this sequence is monotonically decreasing:
$$ M_0 \ge M_1 \ge M_2 \ge \dots \ge 0 $$
Therefore, the limit $M_\infty = \lim_{r \to \infty} M_r$ exists. The conjecture asserts that $M_\infty < \infty$.

## 3. History & State of the Art (SOTA)

- **1991:** Victor Kolyvagin introduces the Euler system of Heegner points in his foundational paper to prove that if the analytic rank of an elliptic curve is 0 or 1, the algebraic rank matches and the Shafarevich-Tate group is finite. He formulates the indivisibility conjecture for general ranks.
- **2004:** Benjamin Howard formally structures Kolyvagin's systems in modern Iwasawa-theoretic language.
- **2014:** Wei Zhang achieves a massive breakthrough by proving the conjecture for a wide class of elliptic curves, contingent on a ramification condition at a prime $q \mid N$.
- **2014:** Christopher Skinner uses Zhang's result and Iwasawa theory to prove a converse to the Gross-Zagier-Kolyvagin theorem.
- **SOTA (2020s):** Recent progress by mathematicians like Ashay Burungale, Francesc Castella, and Christopher Skinner extends these results to primes lacking the Taylor-Wiles ramification hypothesis via bipartite Euler systems and the anticyclotomic Iwasawa Main Conjecture.

## 4. Partial Results / Verified Cases

- **Wei Zhang's Theorem:** The conjecture is proven for primes $p \ge 5$ of good ordinary reduction provided that the residual mod $p$ Galois representation $\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \operatorname{GL}_2(\mathbb{F}_p)$ is surjective, and there exists at least one prime $q \parallel N$ where $\bar{\rho}_{E,p}$ is ramified.
- **Supersingular Primes:** Extensions have been proven for certain primes of supersingular reduction utilizing Kobayashi's signed Heegner points and $+/-$ Selmer groups.
- **Empirical Verifications:** The conjecture has been empirically verified for specific curves up to conductor 5000 and small primes using computational frameworks (e.g., by William Stein and Dimitar Jetchev), which explicitly calculate the classes $\kappa_n$ over localized ring class fields.

## 5. Principal Obstacles

The main bottleneck in unconditionally proving the conjecture lies in the local-to-global obstructions inherent in the Taylor-Wiles method and Ribet's level-raising theorems. 

To prove $\kappa_n \neq 0$, mathematicians historically link the Heegner point to a modular form of raised level and study congruences between the original curve $E$ and modular forms associated with this raised level. However, this strategy fails when:
1. **Lack of a Taylor-Wiles Prime:** Zhang’s proof requires the existence of a prime $q \parallel N$ where the residual representation is ramified (to serve as a fulcrum to break symmetries and force congruences). If $E$ has everywhere good reduction or only additive reduction, this geometric handle is missing.
2. **Non-Surjective Galois Representations:** If the residual representation $\bar{\rho}_{E,p}$ is not surjective (e.g., when $E$ has complex multiplication or for small primes $p \in \{2, 3\}$), classical patching and level-raising theorems collapse because the associated Hecke algebras and deformation rings lack required isomorphisms.
3. **Analytic Rank $>1$:** When the analytic rank of $E$ is greater than 1, the basic Heegner point is torsion. Traditional analytic methods (like the Gross-Zagier formula) provide no information about the higher derivatives $\kappa_n$, leaving highly complex algebraic methods as the only path forward.

## 6. The Gap

The precise boundary defining the current gap is the transition from "ordinary primes with specific local ramification behavior and surjective Galois representations" (Section 4) to the fully general statement for all primes $p$ and all elliptic curves $E/\mathbb{Q}$.

To cross this barrier, researchers must either discover a completely new, purely algebraic construction to guarantee Euler system non-vanishing (bypassing modular congruences entirely), or successfully generalize the anticyclotomic Iwasawa Main Conjecture to universally bypass the need for a Taylor-Wiles prime and accommodate non-surjective representations. 

## 7. Current Research (as of June 2026)

- **Bipartite Euler Systems:** Research groups are utilizing pairs of Euler systems—such as coupling Heegner points with Beilinson-Flach elements—to unconditionally bound Selmer groups without relying on a single ramification prime.
- **Iwasawa-Theoretic Inversion:** Instead of using Kolyvagin's conjecture to prove the anticyclotomic Iwasawa Main Conjecture (IMC), current strategies attempt to prove the IMC first via Eisenstein congruences on unitary groups, and then deduce Kolyvagin's conjecture as a corollary.
- **Perfectoid Spaces & Patching:** *(frontier — verify)* Recent preprints explore applying perfectoid geometry and continuous patching over the eigencurve to construct generalized Kolyvagin systems, aiming to circumvent the classical representation-theoretic constraints of the Taylor-Wiles method.
- **Tamagawa Number Refinements:** Ongoing efforts seek exact formulas for $M_\infty$ that perfectly match the $p$-adic valuation of the Tamagawa numbers and the Shafarevich-Tate group, aligning precisely with the refined BSD conjecture.

## 8. Future Work

Leading mathematicians in arithmetic geometry have identified several essential pathways:
- **Supersingular and Small Primes:** Extending the indivisibility theorems unconditionally to $p=2, 3$ and primes of supersingular reduction via $p$-adic Hodge theory.
- **Higher Weight Motives:** Formulating and proving analogous indivisibility conjectures for Euler systems constructed from generalized Heegner cycles on Shimura curves, mapping to higher-dimensional abelian varieties and motives of higher weight.
- **Algorithmic Verification:** Developing direct, non-cohomological algorithms to explicitly compute $M_\infty$ for curves of rank $\ge 2$. This would allow for systematic empirical data collection beyond the small-conductor curves currently accessible.

## 9. Key References

- **[Foundational]** Kolyvagin, V. A. *On the structure of Selmer groups.* Mathematische Annalen, 1991.
- **[SOTA / Recent]** Zhang, W. *Selmer groups and the indivisibility of Heegner points.* Cambridge Journal of Mathematics, 2014.
- **[SOTA / Recent]** Skinner, C. *A converse to a theorem of Gross, Zagier and Kolyvagin.* Annals of Mathematics, 2014.
- **[Survey]** Howard, B. *The Heegner point Kolyvagin system.* Compositio Mathematica, 2004.
- **[Survey]** Gross, B. H. *Kolyvagin's work on modular elliptic curves.* L-functions and Arithmetic (Durham, 1989), London Mathematical Society Lecture Note Series, 1991.

## 10. Worked Example / Concrete Special Case

Consider the elliptic curve $E/\mathbb{Q}$ defined by $y^2 + y = x^3 + x^2 - 2x$ (LMFDB label `389a1`). This curve has conductor $N = 389$ and algebraic rank $2$ over $\mathbb{Q}$.

We choose the imaginary quadratic field $K = \mathbb{Q}(\sqrt{-7})$. The prime 389 splits in $K$, so the Heegner hypothesis is satisfied. Because the analytic rank of $E/K$ is at least 2, the Hasse-Weil $L$-function $L(E/K, s)$ vanishes to order $\ge 2$ at $s=1$. By the Gross-Zagier formula, the basic Heegner point $y_1 \in E(K)$ is torsion. 

Consequently, its divisibility index is infinite: $M_0 = \infty$, meaning the base Kolyvagin class $\kappa_1 = 0$ in $H^1(K, E[p])$ for any prime $p$. 

To study the Selmer group structure via Kolyvagin's conjecture for $p=5$, we must look deeper into the Euler system and examine $M_1$. We search for a Kolyvagin prime $\ell_1$ (a prime satisfying $\ell_1 \nmid 389 \cdot 5$, $\ell_1$ is inert in $K$, and $a_{\ell_1} \equiv \ell_1 + 1 \equiv 0 \pmod 5$). 

Let $\ell_1$ be such a prime. We construct the Heegner point $y_{\ell_1} \in E(K_{\ell_1})$ over the ring class field of conductor $\ell_1$ and apply the Kolyvagin derivative $D_{\ell_1} = \sum_{i=1}^{\ell_1} i \sigma_{\ell_1}^i$. This yields the point $P_{\ell_1}$, from which we extract the cohomology class $\kappa_{\ell_1} \in H^1(K, E[5])$ via the Kummer map.

Kolyvagin's conjecture asserts that for a suitable choice of $\ell_1$, this class $\kappa_{\ell_1}$ is strictly non-trivial. Computational verifications explicitly calculate the Kummer image of $P_{\ell_1}$ and confirm $\kappa_{\ell_1} \neq 0$. This implies $M_1 < \infty$ (and thus $M_\infty < \infty$). 

The non-vanishing of this first-derivative class directly bounds the $\mathbb{Z}_5$-corank of the 5-Selmer group from above by 2. This perfectly matches the lower bound from the known rank, thereby verifying the 5-part of the BSD conjecture for $E$.