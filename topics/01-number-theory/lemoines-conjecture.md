---
id: 01-number-theory/lemoines-conjecture
title: "Lemoine's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lemoine's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/lemoines-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Lemoine's conjecture (also frequently referred to as Levy's conjecture) is an additive problem in number theory. It states that every odd integer greater than 5 can be represented as the sum of an odd prime number and an even semiprime. Equivalently, any odd integer $n > 5$ can be expressed as $n = p + 2q$, where $p$ and $q$ are prime numbers. 

A complete proof of the conjecture requires demonstrating that the set of odd integers failing this representation is empty for $n > 5$. A complete disproof would require identifying at least one explicit odd integer $n > 5$ for which no such prime pair $(p, q)$ exists.

## 2. Mathematical Foundations

Let $\mathbb{P}$ denote the set of prime numbers. Lemoine's conjecture asserts that:
$$ \forall n \in 2\mathbb{N} + 1 \text{ such that } n > 5, \exists p, q \in \mathbb{P} \text{ such that } n = p + 2q. $$

This problem belongs to the class of binary additive prime problems, closely related to the Goldbach conjecture. The structural analysis of this equation often relies on the Hardy-Littlewood circle method heuristic. Assuming that the sequence of primes behaves pseudorandomly subject to local congruence obstructions, the number of representations $R(n)$ of an odd integer $n$ as $p + 2q$ is expected to follow an asymptotic formula:
$$ R(n) \sim \mathfrak{S}(n) \frac{n}{\ln^2 n} $$
where $\mathfrak{S}(n)$ is the singular series capturing local arithmetic densities. For $n$ odd, the singular series is non-zero, predicting that $R(n) \to \infty$ as $n \to \infty$. The core mathematical foundation rests on prime distribution, exponential sums over primes, and sieve theory.

## 3. History & State of the Art (SOTA)

The conjecture was first explicitly stated by the French mathematician Émile Lemoine in 1895, documented in the journal *L'Intermédiaire des mathématiciens*. It remained an obscure curiosity until it was independently formulated and published by the Scottish mathematician Hyman Levy in 1963 in *The Mathematical Gazette*, which led to the alternative name "Levy's conjecture."

Historically, progress on binary additive prime problems has been incredibly slow. While ternary problems (like the weak Goldbach conjecture) were resolved, binary problems remain stubbornly open. The current State of the Art involves primarily computational verifications. Exhaustive searches, most notably extending Dann Corbit's 1999 efforts, have computationally verified the conjecture for all odd integers up to $10^{10}$. Specialized probabilistic algorithms, integrating Miller-Rabin primality testing, have verified the conjecture for selected massive integers (up to 1500 digits), showing no counterexamples.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, several partial results and localized cases have been established:
- **Exhaustive Computation:** Verified unconditionally for all odd integers $5 < n \le 10^{10}$.
- **"Almost All" Integers:** Analogous to Montgomery and Vaughan's results for the binary Goldbach conjecture, it can be shown that the exceptional set $E(X)$ of odd integers up to $X$ that *cannot* be written as $p + 2q$ has density zero. Specifically, $|E(X)| = O(X^{1-\delta})$ for some $\delta > 0$.
- **Almost-Prime Approximations:** Using Chen's sieve (the same framework used to prove Chen's Theorem), it is known that every sufficiently large odd integer can be represented as $n = p + 2P_2$, where $P_2$ is an "almost prime" with at most two prime factors.

## 5. Principal Obstacles

The problem remains unsolved because it lies exactly at the intersection of two major methodological barriers in analytical number theory:
1. **The Parity Problem in Sieve Theory:** As identified by Atle Selberg, standard combinatorial sieve methods cannot distinguish between integers with an even or odd number of prime factors. Consequently, while a sieve can easily isolate numbers with at most two prime factors ($P_2$), it cannot inherently cross the parity barrier to guarantee a pure prime ($P_1 = q$) without external analytic input.
2. **Minor Arc Bottlenecks in the Circle Method:** The Hardy-Littlewood circle method is the standard tool for additive problems. It divides the Fourier integral over the unit circle into "major arcs" (where rational approximations yield main terms) and "minor arcs" (the error terms). For ternary problems ($p_1+p_2+p_3$), Vinogradov's mean value theorem provides enough cancellation over the minor arcs. For a binary problem ($p + 2q$), the number of variables is too small, and current bounds on exponential sums over primes are insufficiently sharp to prove that the minor arc contributions do not overwhelm the main term.

## 6. The Gap

The precise mathematical gap is the boundary between $P_2$ (almost-primes) and $q$ (primes), and between "density zero exceptions" and "zero exceptions for $n > 5$." Crossing this barrier requires either a fundamentally new type of sieve that can break the parity problem without relying on existing bilinear forms, or a breakthrough in bounding the $L^1$ norm of the Fourier transform of the primes restricted to minor arcs for two variables.

## 7. Current Research (as of June 2026)

Active research primarily flows through broader additive combinatorics and analytical number theory channels:
- **Computational Mathematics:** Distributed computing groups continue pushing the exhaustive verification bound past $10^{10}$ and optimizing sieve arrays for hardware acceleration.
- **Higher-Order Fourier Analysis:** There are ongoing *(frontier — verify)* attempts to apply Gowers uniformity norms and the machinery of Green-Tao to localized versions of binary prime problems, though this naturally aligns more with arithmetic progressions than direct additive decompositions.
- **Conditional Bounds:** Researchers frequently investigate what improvements to the exceptional set $E(X)$ can be achieved assuming the Generalized Riemann Hypothesis (GRH) or the Elliott-Halberstam conjecture.

## 8. Future Work

Leading mathematicians suggest that proving Lemoine's conjecture will require the same breakthrough machinery needed to resolve the binary Goldbach conjecture and the Twin Prime conjecture. Future research strategies include:
- Establishing a bounded gaps approach to $p + 2q$ using modified Maynard-Tao sieves.
- Exploring non-standard extensions of the circle method that incorporate automorphic forms or utilize deep results from algebraic geometry to extract extra cancellation in two-variable exponential sums.

## 9. Key References

- **[Foundational]** Lemoine, É. *Question 73.* L'Intermédiaire des mathématiciens, Vol. 3, 1896, p. 151.
- **[Foundational]** Levy, H. *On Goldbach's Conjecture.* The Mathematical Gazette, Vol. 47, No. 362, 1963, p. 274.
- **[SOTA / Recent]** Guy, R. K. *Unsolved Problems in Number Theory.* Springer, 3rd ed., 2004. (Section C1 covers Lemoine's conjecture and computational bounds).
- **[Survey]** Halberstam, H., & Richert, H.-E. *Sieve Methods.* Academic Press, 1974. (Provides the foundational context on the parity problem and almost-prime limits applicable to binary additive models).

## 10. Worked Example / Concrete Special Case

To ground the conjecture, consider the small odd integer $n = 47$. According to Lemoine's conjecture, there must exist at least one pair of primes $(p, q)$ such that $47 = p + 2q$. 

We can systematically test prime values for $q$ and check if $p = 47 - 2q$ is prime:
- If $q = 2$, then $p = 47 - 2(2) = 43$. Since $43 \in \mathbb{P}$, the pair $(43, 2)$ is a valid solution.
- If $q = 3$, then $p = 47 - 2(3) = 41$. Since $41 \in \mathbb{P}$, the pair $(41, 3)$ is a valid solution.
- If $q = 5$, then $p = 47 - 2(5) = 37$. Since $37 \in \mathbb{P}$, the pair $(37, 5)$ is a valid solution.
- If $q = 7$, then $p = 47 - 2(7) = 33$. Since $33$ is divisible by 3, this is not a solution.
- If $q = 17$, then $p = 47 - 2(17) = 13$. Since $13 \in \mathbb{P}$, the pair $(13, 17)$ is a valid solution.

This concrete case illustrates that for a given $n$, the representation is not uniquely determined (there are multiple valid pairs), but the conjecture strictly claims that the number of such valid pairs is at least one for all $n > 5$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*