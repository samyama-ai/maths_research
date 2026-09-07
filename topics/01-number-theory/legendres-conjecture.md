---
id: 01-number-theory/legendres-conjecture
title: "Legendre's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Legendre's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/legendres-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Legendre's Conjecture states that for every strictly positive integer $n$, there exists at least one prime number $p$ such that:

$$ n^2 < p < (n+1)^2 $$

A complete proof requires demonstrating that the prime-counting function $\pi(x)$ strictly increases between $x = n^2$ and $x = (n+1)^2$ for all integers $n \ge 1$. Conversely, a disproof would require finding a specific integer $n \ge 1$ for which the interval $(n^2, (n+1)^2)$ contains exclusively composite numbers.

## 2. Mathematical Foundations

Let $\pi(x)$ denote the prime-counting function, which gives the number of primes less than or equal to $x$. Legendre's conjecture is equivalent to establishing the strict inequality:

$$ \pi((n+1)^2 - 1) - \pi(n^2) \ge 1 \quad \text{for all } n \in \mathbb{Z}^+ $$

The conjecture is intimately connected to the study of gaps between consecutive prime numbers. Let $p_k$ denote the $k$-th prime number, and let the $k$-th prime gap be defined as $g_k = p_{k+1} - p_k$.

If Legendre's conjecture holds, the maximum gap between the largest prime $p_k$ smaller than $n^2$ and the subsequent prime $p_{k+1}$ must be strictly bounded by the size of the interval:

$$ (n+1)^2 - n^2 = 2n + 1 $$

Since $n \approx \sqrt{p_k}$, the conjecture implies that gaps between consecutive primes must satisfy:

$$ g_k = p_{k+1} - p_k \le 2\sqrt{p_k} + 1 $$

for all $k$. Stated formally, Legendre's conjecture asserts that the prime gap $g_k$ is bounded by $O(\sqrt{p_k})$. 

Legendre's conjecture is a pillar within a family of conjectures concerning primes in short intervals, which includes Oppermann's conjecture (stating there is a prime between $n^2$ and $n(n+1)$, and another between $n(n+1)$ and $(n+1)^2$), Brocard's conjecture, and Andrica's conjecture ($\sqrt{p_{k+1}} - \sqrt{p_k} < 1$).

## 3. History & State of the Art (SOTA)

Adrien-Marie Legendre proposed this conjecture in 1798 in his *Essai sur la théorie des nombres*. It emerged from early empirical observations of the distribution of prime numbers before the formal proof of the Prime Number Theorem in 1896.

Historically, analytic progress on prime gaps has been the primary vehicle for approaching Legendre's conjecture. In 1930, Hoheisel made the first breakthrough by proving that $p_{k+1} - p_k < p_k^{\theta}$ for $\theta = 32999/33000$. The exponent $\theta$ was successively reduced by mathematicians including Heilbronn, Chudakov, Ingham, and Huxley.

The current state-of-the-art unconditional bound is due to Baker, Harman, and Pintz (2001), who proved that for sufficiently large $x$, the interval $[x, x + x^{0.525}]$ contains at least one prime. That is, $p_{k+1} - p_k = O(p_k^{0.525})$. This is tantalizingly close to the $O(p_k^{0.5})$ bound required to resolve Legendre's conjecture, but the $0.025$ gap in the exponent represents a massive theoretical barrier.

Even assuming the Riemann Hypothesis (RH), the best proven gap bound—established by Harald Cramér in 1920—is $p_{k+1} - p_k = O(\sqrt{p_k} \log p_k)$. The extra $\log p_k$ factor dictates that RH alone is theoretically insufficient to prove Legendre's conjecture. However, Cramér's probabilistic model suggests that maximal gaps are asymptotically $O((\log p_k)^2)$, which strongly supports Legendre's conjecture for large $n$.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, it has been verified for vast computational ranges and weakened analytical classes:

- **Computational Verification:** Exhaustive computational searches for maximal prime gaps have verified the conjecture up to exceptionally large bounds. Projects by Oliveira e Silva et al. (2014) computed prime gaps up to $4 \times 10^{18}$. The maximal prime gap known below $2^{64} \approx 1.84 \times 10^{19}$ is $1550$ (following the prime $18,361,375,334,787,046,697$). This gap of $1550$ is astronomically smaller than the interval length required by Legendre's conjecture at this scale, which is $2\sqrt{2^{64}} = 8.58 \times 10^9$. 
- **Almost-Primes:** Chen Jingrun proved in 1975 that for sufficiently large $n$, the interval $(n^2, (n+1)^2)$ always contains a number that is either a prime or a semiprime (a product of two primes). This represents the strongest approximation of Legendre's conjecture using sieve methods.
- **Asymptotic Density:** It is known that Legendre's conjecture holds for "almost all" intervals $(n^2, (n+1)^2)$ in the sense of asymptotic density. By the Prime Number Theorem in short intervals, the number of integers $n \le X$ for which the interval contains no primes is $o(X)$.

## 5. Principal Obstacles

The primary obstacle to proving Legendre's conjecture is the profound inadequacy of current analytic and combinatorial tools to establish precise error term control over prime counting in intervals of length proportional to $\sqrt{x}$.

**The Parity Problem in Sieve Theory:**
Combinatorial sieve methods (like the Selberg or Rosser-Iwaniec sieves) are fundamentally hindered by the "parity problem," formalized by Atle Selberg. Standard sieves cannot distinguish between integers with an even number of prime factors (like semiprimes) and those with an odd number of prime factors (like primes). Because of this, Chen's theorem can only guarantee a $P_2$ (prime or semiprime) in the interval. Breaking the parity barrier to isolate purely prime numbers requires injecting external analytic information or bilinear forms of error terms, which so far cannot achieve the $O(\sqrt{x})$ bound unconditionally.

**Limitations of the Explicit Formula and the Riemann Hypothesis:**
Analytically, the prime-counting function $\psi(x)$ is linked to the non-trivial zeros $\rho = \beta + i\gamma$ of the Riemann zeta function $\zeta(s)$ via the explicit formula:

$$ \psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \log(2\pi) - \frac{1}{2}\log(1 - x^{-2}) $$

To prove a prime exists in $(x, x + y)$, the main term $y$ must strictly dominate the fluctuation of the sum over the zeros. Assuming the Riemann Hypothesis ($\beta = 1/2$), the sum over the zeros produces an error bounded by $O(\sqrt{x} \log^2 x)$. For Legendre's conjecture, the interval length is $y = 2\sqrt{x}$. Because $2\sqrt{x}$ is asymptotically overpowered by the fluctuation $O(\sqrt{x} \log^2 x)$, the analytic method fails to guarantee a prime. The fluctuation from the zeros could, theoretically, perfectly cancel out the main term in a short interval of this size.

## 6. The Gap

The precise mathematical gap lies between the interval length established by state-of-the-art zero-density estimates and the structural limit of Legendre's boundary:

- **Proven Boundary:** Primes are unconditionally guaranteed in intervals of length $x^{0.525}$ for large $x$.
- **Target Boundary:** Primes must be guaranteed in intervals of length $2\sqrt{x} \approx 2x^{0.5}$ for all $x = n^2$.

To cross this $0.025$ barrier in the exponent, one must either drastically improve the exponent pairs and zero-density estimates $N(\sigma, T)$ for the Riemann zeta function, or invent a revolutionary mechanism to bypass the parity problem for sparse sequences in sieve theory. Furthermore, even if the $0.5$ exponent is analytically achieved, establishing the bound for "sufficiently large $n$" would still leave a potentially massive (though finite) set of small $n$ to be verified computationally, necessitating highly effective (computable) implied constants.

## 7. Current Research (as of June 2026)

Active research continues across several highly specialized analytical domains:
- **Zero-Density Estimates:** Researchers are optimizing zero-density estimates $N(\sigma, T)$ by refining the bounds on mean values of Dirichlet polynomials. Efforts focus on shaving microscopic fractions off the $0.525$ exponent established by Baker, Harman, and Pintz. *(frontier — verify: new multi-dimensional bounds on Dirichlet polynomial coefficients yielding sub-0.525 exponents)*.
- **Multidimensional Sieves:** Following the breakthroughs by Zhang, Maynard, and Tao on bounded gaps between primes, there is intensive research into higher-dimensional sieve weights. While these methods currently excel at proving small gaps exist *infinitely often*, adapting them to prove maximal gaps are *always* $O(\sqrt{x})$ remains a fundamental theoretical challenge.
- **Random Matrix Theory:** Probabilistic models inspired by Montgomery's Pair Correlation Conjecture and random matrix theory are heavily utilized to understand the true localized behavior of the zeta zeros, suggesting that the maximal fluctuation in short intervals is significantly smaller than the $O(\sqrt{x} \log^2 x)$ bound given by a crude application of RH.

## 8. Future Work

Leading mathematicians suggest several long-term strategic pathways:
- **Subconvexity Bounds:** Securing aggressively stronger subconvexity bounds for the Riemann zeta function on the critical line. While subconvexity is directly related to the error term in the Prime Number Theorem, monumental improvements are required to have a localized impact on intervals of size $\sqrt{x}$.
- **Parity-Breaking Mechanisms:** Friedlander and Iwaniec successfully broke the parity barrier to prove the existence of infinitely many primes of the form $X^2 + Y^4$. Expanding these deep analytic techniques—which blend sieve methods with modular forms and exponential sums—to the sequence of intervals $[n^2, (n+1)^2]$ is a highly prized target.
- **Conditional Assumptions beyond RH:** Determining whether Legendre's conjecture can be strictly proven assuming the Generalized Riemann Hypothesis (GRH) combined with powerful zero-spacing conjectures, such as the Pair Correlation Conjecture or explicit linear independence of the ordinates of zeta zeros.

## 9. Key References

- **[Foundational]** Legendre, A.-M. *Essai sur la théorie des nombres*. Duprat, Paris, 1798.
- **[Foundational]** Cramér, H. "Some theorems concerning prime numbers." *Arkiv för Matematik, Astronomi och Fysik*, 15 (1920): 1-33.
- **[SOTA / Recent]** Baker, R. C., Harman, G., and Pintz, J. "The difference between consecutive primes, II." *Proceedings of the London Mathematical Society*, 83(3) (2001): 532-562.
- **[Partial Results]** Chen, J. R. "On the distribution of almost primes in an interval." *Science Sinica*, 18 (1975): 611-627.
- **[Survey]** Iwaniec, H., & Kowalski, E. *Analytic Number Theory*. American Mathematical Society Colloquium Publications, Vol. 53, 2004.

## 10. Worked Example / Concrete Special Case

To ground the conjecture, we can verify Legendre's claim for a small, concrete integer: $n = 4$.

1. **Identify the boundaries of the interval:**
   The lower bound is $n^2 = 4^2 = 16$.
   The upper bound is $(n+1)^2 = 5^2 = 25$.

2. **Formulate the open interval:**
   We are looking for prime numbers within the strict interval $(16, 25)$. This corresponds to checking the finite set of integers: $\{17, 18, 19, 20, 21, 22, 23, 24\}$.

3. **Prime factorization of the set:**
   - $17$ is **prime**.
   - $18 = 2 \times 3^2$ (composite).
   - $19$ is **prime**.
   - $20 = 2^2 \times 5$ (composite).
   - $21 = 3 \times 7$ (composite).
   - $22 = 2 \times 11$ (composite).
   - $23$ is **prime**.
   - $24 = 2^3 \times 3$ (composite).

4. **Conclusion:**
   The prime numbers strictly between $4^2$ and $5^2$ are **$17, 19$, and $23$**. 
   Because the interval contains 3 prime numbers, and $3 \ge 1$, Legendre's conjecture holds unequivocally for $n = 4$. Furthermore, the gap from the lower bound to the first prime is $17 - 16 = 1$, which is comfortably smaller than the theoretical maximum gap permitted by the interval size, $2n = 8$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*