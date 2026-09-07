---
id: 01-number-theory/infinitude-of-wieferich-primes
title: "Infinitude of Wieferich Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Wieferich Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-wieferich-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there are infinitely many prime numbers $p$ such that $p^2$ divides $2^{p-1} - 1$. Such primes are known as **Wieferich primes**. 

Formally, the open problem asks for a rigorous mathematical proof or disproof of the statement:
$$ \limsup_{x \to \infty} \left| \{ p \le x \mid p \text{ is prime and } 2^{p-1} \equiv 1 \pmod{p^2} \} \right| = \infty $$

A related and deeply connected open problem is the infinitude of **non-Wieferich primes** (primes $p$ for which $p^2 \nmid 2^{p-1} - 1$). While it is universally expected that almost all primes are non-Wieferich, even this statement remains unconditionally unproven for base 2. A complete resolution of the Wieferich prime problem would require unconditionally demonstrating the existence of infinitely many primes satisfying the congruence $2^{p-1} \equiv 1 \pmod{p^2}$.

## 2. Mathematical Foundations

The foundation of this problem lies in **Fermat's Little Theorem**, which states that for any prime $p$ and integer $a$ coprime to $p$:
$$ a^{p-1} \equiv 1 \pmod{p} $$
Because this congruence holds, the quantity $a^{p-1} - 1$ is always an integer multiple of $p$. This allows us to define the **Fermat quotient** $q_p(a)$ in base $a$:
$$ q_p(a) = \frac{a^{p-1} - 1}{p} $$
By definition, $q_p(a)$ is an integer. We can then ask about the properties of $q_p(a)$ modulo $p$. A prime $p$ is defined as a Wieferich prime if and only if its Fermat quotient in base 2 is congruent to 0 modulo $p$:
$$ q_p(2) \equiv 0 \pmod{p} $$
which is algebraically equivalent to the condition:
$$ 2^{p-1} \equiv 1 \pmod{p^2} $$

The condition naturally arises in the study of algebraic number fields, $p$-adic valuations, and the first case of Fermat's Last Theorem (FLT). For a prime $p$, if the $p$-adic valuation is denoted as $v_p(x)$, a Wieferich prime satisfies $v_p(2^{p-1} - 1) \ge 2$. 

## 3. History & State of the Art (SOTA)

Arthur Wieferich originally introduced these primes in 1909 during his work on Fermat's Last Theorem. He proved a monumental theorem: if the equation $x^p + y^p = z^p$ has solutions in integers $x, y, z$ that are not divisible by $p$ (the "first case" of FLT), then $p$ must be a Wieferich prime. 

Following Wieferich's discovery, massive computational efforts were launched to find such primes. W. Meissner discovered the first Wieferich prime, $p = 1093$, in 1913. N. G. W. H. Beeger found the second, $p = 3511$, in 1922. 

In 1988, J. H. Silverman provided a foundational heuristic suggesting that the number of Wieferich primes up to $x$ should grow asymptotically as $\log \log x$. This implies that while there are infinitely many, they are extremely sparse. Silverman also showed that if the $abc$-conjecture holds, then there are infinitely many *non-Wieferich* primes, and their count up to $x$ is at least $\mathcal{O}(\log x)$.

On the computational front, distributed computing projects (most notably PrimeGrid) have pushed the search limits significantly. As of late 2015, PrimeGrid exhausted the search space up to $4.968 \times 10^{17}$, finding no new Wieferich primes beyond 1093 and 3511. This limit remains the state-of-the-art computational boundary as of 2026.

## 4. Partial Results / Verified Cases

- **Verified Cases:** Only two Wieferich primes have been discovered and verified: $p = 1093$ and $p = 3511$.
- **Computational Lower Bound:** It is rigorously proven by exhaustive computational search that there are no other Wieferich primes in the interval $[2, 4.968 \times 10^{17}]$.
- **Conditional Infinitude of Non-Wieferich Primes:** Assuming the $abc$-conjecture, there are infinitely many non-Wieferich primes (Silverman, 1988). 
- **Sub-classes / Disjoint Sets:** It has been proven that a Mersenne prime (a prime of the form $2^q - 1$) cannot be a Wieferich prime.

## 5. Principal Obstacles

The central difficulty in resolving the conjecture is the pseudo-random behavior of the Fermat quotient $q_p(2) \pmod p$. Current mathematical techniques are deeply ill-equipped to handle constraints modulo $p^2$ when the base $p$ is varying. 

1. **Extreme Sparsity:** If the heuristic density of Wieferich primes is roughly $1/p$, the expected number of Wieferich primes up to $x$ is proportional to $\log \log x$. Sieve methods (such as the Selberg sieve or the large sieve) cannot detect primes in sets this sparse. 
2. **Lack of Algebraic Linkage:** The property $2^{p-1} \equiv 1 \pmod{p^2}$ is a statement about the $p$-adic behavior of an exponential function. Unlike properties linked to the multiplicative group of a finite field, the lift to $\mathbb{Z}/p^2\mathbb{Z}$ does not correspond to a known structural geometric object (like an algebraic curve) over $\mathbb{Q}$ that can be analyzed to force the congruence to hold infinitely often.
3. **Failure of Analytic Density:** Standard analytic number theory tools (e.g., Dirichlet $L$-functions or the Hardy-Littlewood circle method) require periodic functions or well-behaved error terms. The function mapping $p \mapsto q_p(2) \bmod p$ exhibits no known periodicity or uniformity that can be analytically exploited.

## 6. The Gap

The gap is the transition from a robust probabilistic heuristic (which correctly predicts extreme scarcity and implies infinitude) to an unconditional proof. Specifically, mathematics currently lacks any framework or theorem that forces the $p$-adic valuation $v_p(2^{p-1}-1)$ to be strictly greater than $1$ for infinitely many primes $p$. Bridging this gap will likely require an entirely new theory concerning the distribution of Fermat quotients or revolutionary advances in $p$-adic analytic number theory.

## 7. Current Research (as of June 2026)

Current research approaches the problem obliquely, as direct attacks have stalled:
- **Elliptic Wieferich Primes:** Mathematicians are studying the analog of Wieferich primes on elliptic curves, where points of infinite order generate sequences of primes. The extra structural geometry of elliptic curves provides more traction.
- **Function Field Analogs:** Researchers study the Wieferich prime problem over polynomial rings $\mathbb{F}_q[T]$, where the derivative can replace $p$-adic valuation. This yields striking results in the function field setting, though translating these back to $\mathbb{Z}$ is an ongoing obstacle.
- *(frontier — verify)* **Connections to $p$-adic $L$-functions:** There is active exploration into whether the main conjecture of Iwasawa theory and the behavior of $p$-adic $L$-functions at $s=1$ can bound or control the statistics of Fermat quotients for specific families of primes.

## 8. Future Work

Leading mathematicians suggest the following pathways:
- **Unconditional Non-Wieferich Primes:** The most immediate stepping stone is to unconditionally prove that there are infinitely many *non-Wieferich* primes in base 2. Doing so without assuming the $abc$-conjecture would represent a major breakthrough in understanding Fermat quotients.
- **Distribution of $q_p(2)$:** Formally proving that the Fermat quotients $q_p(2) \pmod p$ are uniformly distributed in the interval $[0, p-1]$ as $p \to \infty$. 
- **New Heuristics via Modular Forms:** Investigating if congruences of modular forms can force the existence of Wieferich-like congruences, potentially generating an infinite sequence of primes that satisfy the condition.

## 9. Key References

- **[Foundational]** Wieferich, A. *Zum letzten Fermat'schen Theorem.* Journal für die reine und angewandte Mathematik, 136: 293–302, 1909.
- **[Foundational]** Silverman, J. H. *Wieferich's criterion and the abc-conjecture.* Journal of Number Theory, 30(2): 226–237, 1988.
- **[SOTA / Recent]** Dorais, F. G., & Klyve, D. *A computational search for Wieferich primes.* Mathematics of Computation, 80(276): 2131–2136, 2011.
- **[Survey]** Ribenboim, P. *The New Book of Prime Number Records.* Springer-Verlag, 1996.

## 10. Worked Example / Concrete Special Case

To ground the abstract definition, we evaluate the Wieferich condition for a non-Wieferich prime and for a known Wieferich prime.

**Case 1: $p = 5$ (Non-Wieferich)**
1. The prime is $p = 5$, so we calculate modulo $p^2 = 25$.
2. We evaluate $2^{p-1} = 2^4 = 16$.
3. We check the congruence: $16 \not\equiv 1 \pmod{25}$.
4. Therefore, $5$ is not a Wieferich prime. The Fermat quotient is $q_5(2) = (16-1)/5 = 3$, and $3 \not\equiv 0 \pmod 5$.

**Case 2: $p = 1093$ (Wieferich)**
1. The prime is $p = 1093$, so we calculate modulo $p^2 = 1194649$.
2. We must compute $2^{1092} \pmod{1194649}$. Using binary exponentiation, one calculates the successive squares of 2 modulo $1194649$.
3. The calculation yields precisely:
   $$ 2^{1092} \equiv 1 \pmod{1194649} $$
4. Equivalently, calculating the integer $2^{1092} - 1$ yields a massive number with 329 decimal digits. If we compute the Fermat quotient $q_{1093}(2) = (2^{1092}-1)/1093$, we find that this 326-digit integer is completely divisible by 1093. Thus, $q_{1093}(2) \equiv 0 \pmod{1093}$, proving that $1093$ is indeed a Wieferich prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*