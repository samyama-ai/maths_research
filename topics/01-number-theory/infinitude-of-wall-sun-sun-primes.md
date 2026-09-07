---
id: 01-number-theory/infinitude-of-wall-sun-sun-primes
title: "Infinitude of Wall-Sun-Sun Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Wall-Sun-Sun Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-wall-sun-sun-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The **Wall-Sun-Sun Prime Conjecture** (also known as the Fibonacci-Wieferich Prime Conjecture) asserts that there exist infinitely many prime numbers $p > 5$ such that $p^2$ divides the Fibonacci number $F_{p - \left(\frac{p}{5}\right)}$, where $\left(\frac{p}{5}\right)$ is the Legendre symbol of $p$ modulo 5. 

Primes satisfying this strict divisibility condition are known as **Wall-Sun-Sun primes**. A complete proof of the conjecture requires demonstrating an infinite family of such primes or providing an analytic, density, or algebraic argument guaranteeing their infinite quantity. Conversely, a disproof would require proving that only finitely many (or zero) such primes exist. As of present, not a single Wall-Sun-Sun prime has ever been found.

## 2. Mathematical Foundations

The conjecture resides at the intersection of linear recurrence sequences and elementary number theory, relying heavily on modular arithmetic.

1. **Fibonacci Sequence:** The sequence $(F_n)_{n \geq 0}$ is defined by the linear recurrence $F_n = F_{n-1} + F_{n-2}$ with initial conditions $F_0 = 0$ and $F_1 = 1$.
2. **Legendre Symbol:** For a prime $p > 5$, the Legendre symbol $\left(\frac{p}{5}\right)$ is evaluated as:
   $$ \left(\frac{p}{5}\right) = \begin{cases} 1 & \text{if } p \equiv 1, 4 \pmod 5 \\ -1 & \text{if } p \equiv 2, 3 \pmod 5 \end{cases} $$
3. **Wall's Theorem (1960):** Donald Dines Wall proved that the period of the Fibonacci sequence modulo $p$, denoted $\pi(p)$ (the Pisano period), always divides $p - \left(\frac{p}{5}\right)$. As a direct mathematical consequence, $p$ always divides $F_{p - \left(\frac{p}{5}\right)}$.
4. **Wall-Sun-Sun Condition:** The condition for a Wall-Sun-Sun prime asks whether the $p$-adic valuation of $F_{p - \left(\frac{p}{5}\right)}$ is at least 2. In modular arithmetic, this is the stricter congruence:
   $$ F_{p - \left(\frac{p}{5}\right)} \equiv 0 \pmod{p^2} $$
5. **Heuristic Density:** The quotient $q_p = \frac{F_{p - \left(\frac{p}{5}\right)}}{p} \pmod p$ is known as a Fibonacci quotient. Assuming $q_p$ behaves as a uniformly distributed random integer modulo $p$, the probability that $q_p \equiv 0 \pmod p$ (which is exactly equivalent to $p^2 \mid F_{p - \left(\frac{p}{5}\right)}$) is approximately $1/p$. Thus, the expected number of Wall-Sun-Sun primes up to a bound $x$ is given by Mertens' second theorem:
   $$ \sum_{p \le x} \frac{1}{p} \sim \log \log x $$
   Since $\lim_{x \to \infty} \log \log x = \infty$, probabilistic heuristics predict infinitely many such primes.

## 3. History & State of the Art (SOTA)

- **1960 (Original Inquiry):** Donald Dines Wall studied the periods of the Fibonacci sequence modulo $m$. He theoretically verified that $p \mid F_{p - (p/5)}$ and asked whether $p^2 \mid F_{p - (p/5)}$ is ever possible, noting that he computationally checked primes up to $p = 10^4$ and found none.
- **1992 (Fermat's Last Theorem Connection):** Twin mathematicians Zhi-Hong Sun and Zhi-Wei Sun proved a spectacular theorem: if the first case of Fermat's Last Theorem failed for a prime exponent $p$, then $p$ must be a Wall-Sun-Sun prime. Although Andrew Wiles later proved Fermat's Last Theorem unconditionally (rendering the first case true for all primes), the Sun brothers' discovery cemented the mathematical importance of these primes and triggered massive computational searches.
- **Computational Verifications:**
  - **2007:** R. J. McIntosh and E. L. Roettger searched for Wall-Sun-Sun primes up to $2 \times 10^{14}$.
  - **2011:** F. G. Dorais and D. Klyve extended the rigorous search bound to $9.7 \times 10^{14}$.
  - **2015-Present:** The distributed computing project PrimeGrid has continuously pushed the bound, proving no Wall-Sun-Sun primes exist below $1.46 \times 10^{17}$.

## 4. Partial Results / Verified Cases

Because the conjecture postulates the *existence* of an infinite class of numbers—and because not a single example has yet been found—there are no positive "verified cases" of Wall-Sun-Sun primes themselves. 

Instead, the verified cases consist entirely of negative bounds through exhaustive computational sieving:
- It is rigorously proven that there are **no** Wall-Sun-Sun primes in the interval $5 < p < 1.46 \times 10^{17}$.
- For every single prime in this massive range, the $p$-adic valuation of $F_{p - (p/5)}$ is exactly 1 (meaning $p$ flawlessly divides the sequence term, but $p^2$ strictly does not).

## 5. Principal Obstacles

- **Extremely Slow Growth Rate:** The primary obstacle is the agonizingly slow divergence of the harmonic sum over primes. Based on the $\log \log x$ heuristic, the expected number of Wall-Sun-Sun primes less than the current search bound of $1.46 \times 10^{17}$ is merely $\approx \log \log (1.46 \times 10^{17}) \approx 3.68$. Finding zero primes in a Poisson distribution with an expected value of $\lambda = 3.68$ occurs with probability $e^{-3.68} \approx 2.5\%$. Thus, finding none is statistically unsurprising, but computational hardware limits us from reaching domains where we would expect to find dozens of examples (e.g., $10^{100}$).
- **Lack of Algebraic Structure:** Traditional algebraic geometry and $p$-adic analysis fail because the condition $p^2 \mid F_{p - (p/5)}$ acts as an algebraically pseudo-random property. Unlike elliptic curves, which possess rich Galois representations and complex multiplication that can force torsion points, Lucas sequences evaluated modulo $p^2$ lack a known geometric or topological framework that forces the Fibonacci quotient to cleanly vanish.
- **Ineffective Sieve Methods:** Modern Sieve theory (like the Selberg sieve) is remarkably effective for bounding primes with additive properties (e.g., twin primes) or bounded multiplicative properties. However, it completely fails to control the multiplicative divisibility of exponentially growing additive recurrences evaluated over varying moduli $p^2$.

## 6. The Gap

The gap between current knowledge and a full resolution of the conjecture is two-fold and exceptionally wide:
1. **Existence of a Single Example:** We do not know a single prime $p$ that satisfies the Wall-Sun-Sun condition. The immediate mathematical barrier is proving the existence of at least one such prime unconditionally, without waiting for brute-force computation to stumble upon one.
2. **From One to Infinity:** Even if a supercomputer finds a Wall-Sun-Sun prime tomorrow, crossing the gap to prove that *infinitely many* exist requires a completely new theoretical apparatus. Mathematicians would need to discover an explicit algebraic theorem that lower-bounds the density of primes for which the $p$-adic logarithm of the fundamental unit in the ring of integers $\mathbb{Z}[\frac{1+\sqrt{5}}{2}]$ vanishes modulo $p$.

## 7. Current Research (as of June 2026)

- **Distributed Computing:** Organizations like **PrimeGrid** continue to hold the computational frontier, utilizing massive volunteer computing networks to optimize double-precision modular arithmetic to test primes beyond the $10^{17}$ barrier.
- **Lucas-Wieferich Primes (Generalizations):** Researchers are studying broader classes of Lucas sequences $U_n(P, Q)$ to find generic primes $p$ where $p^2 \mid U_{p - (D/p)}$. By locating examples of generalized Pell-Wieferich primes, mathematicians hope to uncover statistical invariants that map back to the Fibonacci case. *(frontier — verify)*
- **$p$-adic L-functions:** Certain theoretical number theory groups are attempting to connect the vanishing of Fibonacci quotients to the arithmetic of modular curves and the behavior of extraordinary zeroes of $p$-adic L-functions, searching for a deep arithmetic reason for their sparsity.

## 8. Future Work

- **Algorithmic Optimizations:** Developing faster modular multiplication algorithms (such as refined FFT-based approaches optimized for GPU architectures) to push the exhaustive search bound towards $10^{20}$, where the statistical probability of finding at least one prime rises significantly.
- **Heuristic Refinement:** Constructing more rigorous probability models to replace the naive $1/p$ heuristic. Identifying secondary error terms in the prime distribution could theoretically explain the complete dearth of small Wall-Sun-Sun primes and predict the approximate magnitude of the first occurrence.
- **Implications of the ABC Conjecture:** Exploring the explicit consequences of the ABC conjecture (or related effective bounds) on the square-freeness of terms in Lucas sequences, which could potentially constrain or bound the distribution of Wall-Sun-Sun primes.

## 9. Key References

- **[Foundational]** Wall, D. D. *Fibonacci Series Modulo m.* American Mathematical Monthly, 1960.
- **[Foundational]** Sun, Z.-H. and Sun, Z.-W. *Fibonacci numbers and Fermat's last theorem.* Acta Arithmetica, 1992.
- **[SOTA / Recent]** Dorais, F. G. and Klyve, D. *A Wieferich Prime Search up to $6.7 \times 10^{15}$.* Journal of Integer Sequences, 2011.
- **[SOTA / Recent]** McIntosh, R. J. and Roettger, E. L. *A search for Fibonacci-Wieferich and Wolstenholme primes.* Mathematics of Computation, 2007.
- **[Survey]** Ribenboim, P. *My Numbers, My Friends: Popular Lectures on Number Theory.* Springer-Verlag, 2000.

## 10. Worked Example / Concrete Special Case

To understand the conjecture practically, let us test two small primes to see if they satisfy the Wall-Sun-Sun condition.

**Case 1: Test $p = 7$**
1. Determine the Legendre symbol $\left(\frac{7}{5}\right)$. Since $7 \equiv 2 \pmod 5$, we have $\left(\frac{7}{5}\right) = -1$.
2. Compute the target index $k = p - \left(\frac{p}{5}\right) = 7 - (-1) = 8$.
3. Find the Fibonacci number $F_8$. The sequence begins:
   $F_0=0, F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13, F_8=21$.
4. **Check Wall's Theorem:** Does $p \mid F_8$? We evaluate $21 / 7 = 3$. It perfectly divides, confirming Wall's theorem.
5. **Check Wall-Sun-Sun condition:** Does $p^2 \mid F_8$? We evaluate $7^2 = 49$. Since 49 does not divide 21, **$p=7$ is not a Wall-Sun-Sun prime**.

**Case 2: Test $p = 11$**
1. Determine the Legendre symbol $\left(\frac{11}{5}\right)$. Since $11 \equiv 1 \pmod 5$, we have $\left(\frac{11}{5}\right) = 1$.
2. Compute the target index $k = 11 - 1 = 10$.
3. Find the Fibonacci number $F_{10}$. Continuing the sequence:
   $F_9=34, F_{10}=55$.
4. **Check Wall's Theorem:** Does $11 \mid 55$? Yes, $55 / 11 = 5$.
5. **Check Wall-Sun-Sun condition:** Does $11^2 \mid 55$? We evaluate $11^2 = 121$. Since $121 > 55$, it clearly cannot divide it. Thus, **$p=11$ is not a Wall-Sun-Sun prime**.

This exact computation must be scaled to primes larger than $1.46 \times 10^{17}$, with the corresponding $F_k$ possessing hundreds of millions of digits, illustrating why distributed modular arithmetic is required to search for these primes today.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*