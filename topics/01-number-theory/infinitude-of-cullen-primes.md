---
id: 01-number-theory/infinitude-of-cullen-primes
title: "Infinitude of Cullen Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Cullen Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-cullen-primes` · **Status:** open

## 1. Problem Statement / Conjecture

A Cullen number is a natural number of the form $C_n = n \cdot 2^n + 1$, where $n$ is a positive integer. A Cullen number that is strictly prime is known as a Cullen prime. 

The **Cullen Primes Conjecture** posits that there exist infinitely many Cullen primes. Formally, the conjecture states that the set:
$$ P_C = \{ n \in \mathbb{N} \mid n \cdot 2^n + 1 \text{ is prime} \} $$
has infinite cardinality. A complete proof must rigorously demonstrate that no finite upper bound exists for the elements of $P_C$, while a disproof would require showing that beyond a certain threshold $N$, all Cullen numbers are composite, most likely via a covering system of congruences.

## 2. Mathematical Foundations

The problem lies at the intersection of exponential Diophantine sequences and primality theory. 

**Proth's Theorem and Cullen Numbers:**
Cullen numbers are a specific subset of Proth numbers, which take the form $N = k \cdot 2^m + 1$ with $k < 2^m$ and $k$ odd. To map a Cullen number $C_n = n \cdot 2^n + 1$ to a Proth number, we factor out the largest power of 2 from $n$. Let $n = k \cdot 2^j$ where $k$ is an odd integer. Then we can rewrite the Cullen number as:
$$ C_n = k \cdot 2^{n+j} + 1 $$
Because $k \le n < 2^n \le 2^{n+j}$, the Proth condition ($k < 2^{n+j}$) is strictly satisfied for all $n \ge 1$. Consequently, Proth's Theorem is unconditionally applicable to all Cullen numbers: $C_n$ is prime if and only if there exists an integer $a$ such that:
$$ a^{(C_n - 1)/2} \equiv -1 \pmod{C_n} $$

**Probabilistic Heuristics (Prime Number Theorem):**
By the Prime Number Theorem, the "probability" that a large integer $N$ is prime is asymptotic to $1 / \ln(N)$. For $C_n$, the natural logarithm is:
$$ \ln(C_n) = \ln(n \cdot 2^n + 1) \sim n \ln 2 + \ln n \sim n \ln 2 $$
Assuming the primality of Cullen numbers behaves as a random sequence modeled by this distribution (with mild adjustments for fixed modular constraints), the expected number of Cullen primes for index $n \le X$ is:
$$ \mathbb{E}(X) \approx \sum_{n=1}^X \frac{1}{n \ln 2} \approx \frac{\ln X}{\ln 2} $$
Since the harmonic series diverges, this heuristic strongly implies that the set of Cullen primes is infinite, and that their distribution grows logarithmically with respect to $X$.

## 3. History & State of the Art (SOTA)

The sequence was first introduced by the Irish Jesuit mathematician James Cullen in 1905, who empirically observed that for $n$ up to 100, almost all values yielded composite numbers. The sole exception in his computational range was $n=1$. 

In 1917, Allan J. C. Cunningham and H. J. Woodall published a factorization study of these numbers, confirming Cullen's intuition about their overwhelming compositeness. It was not until 1958 that Raphael M. Robinson, utilizing the SWAC (Standards Western Automatic Computer), identified the second Cullen prime at $n = 141$.

In 1976, Christopher Hooley proved a landmark theoretical result regarding the density of the sequence: the asymptotic density of composite Cullen numbers is 1. Thus, "almost all" Cullen numbers are composite, which complicates naive sieve approaches. 

Through the 1980s and 1990s, Wilfrid Keller spearheaded algorithmic searches, finding several more Cullen primes. The state of the art is currently dominated by **PrimeGrid**, a massive BOINC-based distributed computing framework, which has pushed the search limits past $n = 10^7$ using highly optimized Fast Fourier Transform (FFT) implementations of Proth's test.

## 4. Partial Results / Verified Cases

Currently, there are exactly 16 known Cullen primes. They correspond to the indices:
$n = 1, 141, 4713, 5795, 6611, 18496, 32292, 32469, 59656, 90825, 262419, 361275, 481899, 1354828, 6328548, 6679881$.

The largest known Cullen prime, $C_{6679881} = 6679881 \cdot 2^{6679881} + 1$, was discovered in 2009 by a PrimeGrid participant. It has 2,010,852 decimal digits, qualifying it as a mega prime.

Additionally, generalized Cullen primes of the form $C_n(b) = n \cdot b^n + 1$ have been studied, and infinitude conjectures remain open for all bases $b \ge 2$.

## 5. Principal Obstacles

The difficulty of the conjecture stems from the mixed polynomial-exponential nature of the sequence $C_n = n \cdot 2^n + 1$. 

1. **Failure of Algebraic Factorization:** Unlike sequences such as Mersenne numbers ($2^p - 1$) which admit deep algebraic structures and divisor constraints (e.g., factors must be of the form $2kp+1$), Cullen numbers lack a global polynomial factorization over $\mathbb{Z}[x]$.
2. **The "Almost All Composite" Barrier:** Hooley's proof that the density of composite Cullen numbers approaches 1 implies that any sieve method attempting to prove infinitude must be sharp enough to isolate a sub-polynomial density of primes. Traditional analytic sieves lose error term control when tracking sets of zero natural density.
3. **Computational Intractability:** Testing $C_n$ for primality scales at best as $O(n \log^2 n)$ using FFT-based Proth testing. As $n$ grows beyond $10^7$, $C_n$ exceeds millions of digits. The exponential explosion in bit-length makes brute-force empirical extrapolation unsustainable.

## 6. The Gap

The exact mathematical gap lies in ruling out the existence of a **covering system** of congruences. 

A covering system for the Cullen sequence would be a finite set of prime numbers $\mathcal{S} = \{p_1, p_2, \dots, p_k\}$ such that for every $n \in \mathbb{N}$, there exists at least one $p_i \in \mathcal{S}$ dividing $n \cdot 2^n + 1$. 

For the Sierpiński problem ($k \cdot 2^n + 1$), such covering systems *do* exist for specific fixed values of $k$. To solve the Cullen conjecture, one must rigorously prove that because the multiplier $k$ varies linearly with $n$, no finite set of primes can form a covering system for $C_n$. Bridging this gap requires novel combinations of arithmetic dynamics and sieve theory capable of analyzing the orbits of $n \cdot 2^n \pmod{p_i}$.

## 7. Current Research (as of June 2026)

- **Distributed Searches:** Projects like PrimeGrid continue to allocate massive computational resources to find higher values of $n$. The bounds have pushed deep into $n > 10^7$.
- **Covering System Non-existence *(frontier — verify)*:** Researchers in additive combinatorics are currently investigating whether variations of the Lovász Local Lemma or Ergodic Ramsey Theory can definitively rule out finite covering systems for sequences of the form $P(n)a^n + 1$ where $P(n)$ is a non-constant polynomial.
- **Generalized Bases:** Studying $C_n(b) = n \cdot b^n + 1$ to locate structural modular obstructions for varying bases, hoping to find a base $b$ where infinitude can be proven or disproven via a covering system, serving as an analogue for $b=2$.

## 8. Future Work

Leading number theorists suggest the following pathways:
- **Lower Bounding Divisors:** Developing a rigorous theory to establish a lower bound on the number of distinct prime factors of $C_n$ as $n \to \infty$.
- **Heuristic Formalization:** Improving the error terms in the Bateman-Horn conjecture as applied to polynomial-exponential functions, providing a more rigorous conditional proof of infinitude.
- **Hardware Acceleration:** Shifting computational efforts from standard CPU/GPU FFT paradigms to specialized ASICs/FPGAs tailored specifically for large-state Proth exponentiation to gather more empirical data points beyond $n=10^8$.

## 9. Key References

- **[Foundational]** Cullen, J. "Question 15897." *Educational Times*, 1905.
- **[Foundational]** Robinson, R. M. "A report on primes of the form $k \cdot 2^n + 1$ and on factors of Fermat numbers." *Proceedings of the American Mathematical Society*, 1958.
- **[Foundational]** Hooley, C. *Applications of sieve methods to the theory of numbers*. Cambridge Tracts in Mathematics, 1976.
- **[SOTA / Recent]** Keller, W. "Primes of the form $n \cdot 2^n + 1$ and $n \cdot 2^n - 1$." *Mathematics of Computation*, 1995.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory*. Springer, 3rd Edition, 2004. (Section A).
- **[Survey]** Ribenboim, P. *The New Book of Prime Number Records*. Springer, 1996. [DOI](https://doi.org/10.1007/978-1-4612-0759-7)

## 10. Worked Example / Concrete Special Case

To ground the exponential growth and Proth's application, let us analyze the first five Cullen numbers:

1. **$n=1$**: $C_1 = 1 \cdot 2^1 + 1 = 3$. This is prime.
2. **$n=2$**: $C_2 = 2 \cdot 2^2 + 1 = 9 = 3 \times 3$. (Composite)
3. **$n=3$**: $C_3 = 3 \cdot 2^3 + 1 = 25 = 5 \times 5$. (Composite)
4. **$n=4$**: $C_4 = 4 \cdot 2^4 + 1 = 65 = 5 \times 13$. (Composite)
5. **$n=5$**: $C_5 = 5 \cdot 2^5 + 1 = 161$. Testing limits up to $\sqrt{161} \approx 12.6$, we test primes $2, 3, 5, 7, 11$. We find $161 = 7 \times 23$. (Composite)

**Applying Proth's Theorem to $n=1$:**
Let's verify $C_1 = 3$ using the computational method.
We write $C_n = k \cdot 2^m + 1$. For $n=1$, $C_1 = 1 \cdot 2^1 + 1$. Here $k=1, m=1$.
The condition $k < 2^m \implies 1 < 2^1$ holds.
Proth's theorem states that if there is an $a$ such that $a^{(N-1)/2} \equiv -1 \pmod N$, then $N$ is prime.
Choose $a = 2$.
Calculate $2^{(3-1)/2} = 2^1 = 2$.
In modulo 3 arithmetic, $2 \equiv -1 \pmod 3$.
Thus, by Proth's Theorem, 3 is prime. This exact modular exponentiation step is what PrimeGrid scales to numbers with millions of digits using highly optimized FFTs.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*