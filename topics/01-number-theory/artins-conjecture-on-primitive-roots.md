---
id: 01-number-theory/artins-conjecture-on-primitive-roots
title: "Artin's Conjecture on Primitive Roots"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Artin's Conjecture on Primitive Roots

> **Topic:** Number Theory · **ID:** `01-number-theory/artins-conjecture-on-primitive-roots` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $a$ be an integer which is not a perfect square and is not equal to $-1$. Artin's Conjecture states that $a$ is a primitive root modulo $p$ for infinitely many primes $p$. 

More precisely, let $N_a(x)$ denote the number of primes $p \leq x$ for which $a$ is a primitive root. The conjecture asserts that there exists a positive constant $A(a) > 0$ such that, as $x \to \infty$,
$$ N_a(x) \sim A(a) \frac{x}{\ln x} $$
meaning that $a$ is a primitive root for a strictly positive proportion of all primes.

## 2. Mathematical Foundations

Let $p$ be an odd prime. The multiplicative group of integers modulo $p$, denoted $(\mathbb{Z}/p\mathbb{Z})^\times$, is a cyclic group of order $p-1$. An integer $a$ coprime to $p$ is a *primitive root* modulo $p$ if it generates this group, meaning the multiplicative order of $a$ modulo $p$ is exactly $p-1$.

For $a$ to be a primitive root modulo $p$, $a$ must not be a $q$-th power modulo $p$ for any prime $q$ dividing $p-1$. By algebraic number theory, this condition is equivalent to saying that $p$ does not split completely in the Kummer extension $K_q = \mathbb{Q}(\zeta_q, a^{1/q})$, where $\zeta_q$ is a primitive $q$-th root of unity.

By the Chebotarev Density Theorem, the density of primes splitting completely in $K_q$ is $\frac{1}{[K_q : \mathbb{Q}]}$. Thus, using an inclusion-exclusion argument over the primes $q$ dividing $p-1$, the heuristic density of primes for which $a$ is a primitive root is formulated as:
$$ A(a) = \sum_{k=1}^{\infty} \frac{\mu(k)}{[K_k : \mathbb{Q}]} $$
where $K_k = \mathbb{Q}(\zeta_k, a^{1/k})$ and $\mu$ is the Möbius function. For square-free $a \not\equiv 1 \pmod 4$, this infinite sum evaluates to the universal *Artin constant*:
$$ A = \prod_{q \text{ prime}} \left(1 - \frac{1}{q(q-1)}\right) \approx 0.3739558136\dots $$

## 3. History & State of the Art (SOTA)

Emil Artin originally proposed the conjecture in 1927. In 1932, following computational data from Derrick Henry Lehmer that revealed discrepancies for certain values of $a$ (such as $a=5$), Artin modified his proposed density $A(a)$ to properly account for the algebraic entanglement of the fields $\mathbb{Q}(\zeta_k)$ and $\mathbb{Q}(a^{1/k})$.

The most significant theoretical breakthrough occurred in 1967, when Christopher Hooley published a conditional proof. Hooley proved both the existence of infinitely many primes and the precise asymptotic formula for $N_a(x)$, conditional on the Generalized Riemann Hypothesis (GRH) for the Dedekind zeta functions of the fields $K_k$.

Unconditionally, Rajiv Gupta and M. Ram Murty made immense progress in 1984 by proving that the conjecture fails for at most 13 exceptions. In 1986, Roger Heath-Brown refined their sieve methods to prove that at most two prime exceptions can exist.

## 4. Partial Results / Verified Cases

- **Conditional Proof (Hooley, 1967):** The conjecture is completely solved, including the exact asymptotic density $A(a)$, conditionally upon the Generalized Riemann Hypothesis (GRH).
- **"Almost All" Result (Gallagher, 1967):** Unconditionally, the conjecture holds for *almost all* integers $a$. The number of exceptional integers $a \leq x$ for which the conjecture fails is $o(x)$.
- **At Most Two Exceptions (Heath-Brown, 1986):** Unconditionally, among any three multiplicatively independent non-zero integers $a, b, c$ (where none is a square or $-1$), at least one is a primitive root for infinitely many primes. For example, at least one of $a=2$, $b=3$, or $c=5$ must be a primitive root for infinitely many primes, though we still do not know which one.

## 5. Principal Obstacles

The primary obstacle to an unconditional proof for a specific integer (e.g., $a = 2$) is the limitation of the unconditional Chebotarev Density Theorem. The inclusion-exclusion argument requires summing the error terms from the Chebotarev Density Theorem over extensions $K_q = \mathbb{Q}(\zeta_q, a^{1/q})$ up to $q \approx x^{1/2}$.

Unconditionally, the best known error bounds—derived from zero-free regions of $L$-functions—are vastly too weak to control the tail of this sum. Trying to bypass this with sieve theory runs into the well-known "parity problem", which prevents lower bound sieves from unconditionally distinguishing between numbers with an odd versus an even number of prime factors. Thus, sieve methods fail to produce actual primes directly without external analytic input (like GRH) to break the parity barrier.

## 6. The Gap

The gap lies precisely between the unconditional existential statement ("there are at most two exceptions among multiplicatively independent bases") and the specific statement ("$a = 2$ is a primitive root for infinitely many primes"). We currently lack the mathematical machinery to rule out the possibility that $a=2$ happens to be one of the rare exceptional numbers permitted by Heath-Brown's theorem. Bridging this gap requires either a massive improvement in the zero-density estimates for the Dedekind zeta functions of Kummer extensions (approaching GRH), or a completely novel sieve method that breaks the parity barrier for this specific multiplicative framework.

## 7. Current Research (as of June 2026)

Research continues on two primary fronts: analytic number theory and algebraic geometry. Some analytic researchers focus on improving error terms of the Chebotarev density theorem over Kummer extensions by leveraging bounds on character sums and subconvexity. Other approaches look at the distribution of primes splitting completely in related field extensions to bypass GRH. 
*(frontier — verify)* Recent preprints have explored higher-rank analogues, such as the Lang-Trotter conjecture for elliptic curves, hoping that generalized Galois representations and geometric sieves might eventually reflect backward to provide an unconditional proof for the classical rank-one (multiplicative group) case. 

## 8. Future Work

Leading analytic number theorists suggest that eliminating the final two exceptions will likely require injecting structured bilinear forms into the sieve methods, capturing the deep arithmetic features of the sequence $p-1$. Another long-term strategy is to unconditionally establish partial zero-free regions or zero-density theorems for Artin $L$-functions that are just strong enough to control the sum of the error terms without requiring the full strength of GRH.

## 9. Key References

- **[Foundational]** Artin, E. *Über die Kongruenz $a \equiv b^p \pmod p$*. Mathematische Annalen, 1927.
- **[SOTA / Recent]** Hooley, C. *On Artin's conjecture*. Journal für die reine und angewandte Mathematik, 1967.
- **[SOTA / Recent]** Gupta, R., and Murty, M. R. *A remark on Artin's conjecture*. Inventiones Mathematicae, 1984.
- **[SOTA / Recent]** Heath-Brown, D. R. *Artin's conjecture for primitive roots*. The Quarterly Journal of Mathematics, 1986.
- **[Survey]** Moree, P. *Artin's primitive root conjecture—a survey*. Integers, 2012. [DOI](https://doi.org/10.1515/integers-2012-0043)

## 10. Worked Example / Concrete Special Case

Let us examine the conjecture for the base $a = 2$. Artin's conjecture asserts that 2 is a primitive root for infinitely many primes $p$.

Consider $p = 5$. The multiplicative group is $(\mathbb{Z}/5\mathbb{Z})^\times = \{1, 2, 3, 4\}$, which has order $\varphi(5) = 4$.
We compute the powers of 2 modulo 5:
- $2^1 \equiv 2 \pmod 5$
- $2^2 \equiv 4 \pmod 5$
- $2^3 \equiv 8 \equiv 3 \pmod 5$
- $2^4 \equiv 16 \equiv 1 \pmod 5$

The order of 2 modulo 5 is 4, which equals $p-1$. Thus, 2 **is** a primitive root modulo 5.

Now consider $p = 7$. The order of the group is $\varphi(7) = 6$.
- $2^1 \equiv 2 \pmod 7$
- $2^2 \equiv 4 \pmod 7$
- $2^3 \equiv 8 \equiv 1 \pmod 7$

The order of 2 modulo 7 is 3. Since $3 < 6$, 2 **is not** a primitive root modulo 7. (This failure corresponds to the fact that 2 is a quadratic residue modulo 7, specifically $2 \equiv 3^2 \pmod 7$, meaning 7 splits completely in $K_2 = \mathbb{Q}(\sqrt{2})$).

Artin's conjecture claims that the "success" cases like $p=5$ (along with 11, 13, 19, 29, 37, 53, ...) occur infinitely often and make up an asymptotic proportion of $A \approx 37.39\%$ of all primes.