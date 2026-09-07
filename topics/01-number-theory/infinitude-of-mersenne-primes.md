---
id: 01-number-theory/infinitude-of-mersenne-primes
title: "Infinitude of Mersenne Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Mersenne Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-mersenne-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there are infinitely many Mersenne primes. A Mersenne prime is a prime number of the form $M_p = 2^p - 1$, where $p$ is itself a prime number. To fully resolve this conjecture, one must provide a rigorous mathematical proof that the sequence of primes of this specific exponential form does not terminate, or conversely, prove that there exists a maximum Mersenne prime.

## 2. Mathematical Foundations

Let $\mathbb{P}$ denote the set of all prime numbers. A **Mersenne number** is an integer of the form:
$$M_n = 2^n - 1$$
for a positive integer $n$.

A trivial algebraic identity states that for any integer $n = a \cdot b$, the polynomial $x^{ab} - 1$ factors as:
$$x^{ab} - 1 = (x^a - 1) \sum_{i=0}^{b-1} x^{i \cdot a}$$
Substituting $x=2$ proves that if $n$ is composite, $M_n$ must also be composite. Therefore, a necessary (but not sufficient) condition for $M_n$ to be prime is that the exponent $n$ must be a prime $p \in \mathbb{P}$. A **Mersenne prime** is a Mersenne number $M_p$ that is prime.

The primary algorithmic foundation for this problem is the **Lucas–Lehmer Test (LLT)**. For an odd prime $p$, define the sequence $(S_k)_{k=0}^{\infty}$ recursively by:
$$S_0 = 4$$
$$S_k \equiv S_{k-1}^2 - 2 \pmod{M_p}$$
The theorem states that $M_p$ is prime if and only if $S_{p-2} \equiv 0 \pmod{M_p}$.

To probabilistically model the distribution of these primes, the **Lenstra–Pomerance–Wagstaff conjecture** relies on heuristic density arguments. It predicts that the number of Mersenne primes less than $x$ is asymptotically approximated by:
$$\mathcal{N}(x) \sim e^{\gamma} \log_2(\log_2(x))$$
where $\gamma$ is the Euler–Mascheroni constant. Equivalently, the expected number of Mersenne primes $M_p$ for $p \le x$ grows as $\sim \frac{e^\gamma}{\log 2} \log x$.

## 3. History & State of the Art (SOTA)

The study of primes of the form $2^p-1$ dates back to antiquity due to their fundamental relationship with perfect numbers via the Euclid–Euler theorem (which states that every even perfect number is of the form $2^{p-1}(2^p-1)$ where $2^p-1$ is a Mersenne prime).

The numbers are named after the 17th-century French monk Marin Mersenne, who popularized them in 1644 in his *Cogitata Physico-Mathematica*. He famously provided a list of primes $p \le 257$ that he claimed yielded prime $M_p$, though his list contained some errors that took centuries to fully resolve.

The deterministic primality test used to discover them was originally formulated by Édouard Lucas in 1856 and rigorously proven and refined by Derrick Henry Lehmer in 1930. The modern state of the art relies heavily on distributed computing. The Great Internet Mersenne Prime Search (GIMPS), founded in 1996 by George Woltman, orchestrates global computing power to run highly optimized LLT and Fermat Probable Prime (PRP) tests on massive candidate exponents.

## 4. Partial Results / Verified Cases

As of October 2024, exactly 52 Mersenne primes have been discovered. The largest known Mersenne prime, which is also the largest known prime number of any kind, is:
$$M_{136279841} = 2^{136279841} - 1$$
It was discovered by Luke Durant via the GIMPS network and contains over 41 million decimal digits. 

The sequence of verified Mersenne prime exponents $p$ begins: 
$p \in \{2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, \dots\}$

The search space is exhaustively verified for all prime exponents up to roughly $p \approx 6 \times 10^7$, with isolated larger primes known above this contiguous verification bound. Despite these massive computational feats, there is no mathematical proof establishing that infinitely many Mersenne primes exist, nor is there a proof that infinitely many Mersenne numbers are composite.

## 5. Principal Obstacles

The fundamental obstacle to proving the infinitude of Mersenne primes lies in the exponential growth of the sequence $M_p = 2^p - 1$.

Modern analytic number theory and sieve theory rely on bounding prime distributions within sequences. Classical sieve methods (such as the Selberg sieve, or tools like the Hardy-Littlewood circle method) are successful only on sequences of polynomial growth (e.g., the Friedlander–Iwaniec theorem for $x^2 + y^4$). 

The sequence of Mersenne numbers is extraordinarily sparse. The number of terms $M_p \le X$ is only $\pi(\log_2(X)) \sim \frac{\log_2(X)}{\log(\log_2(X))}$, which is roughly logarithmic in $X$. At this extreme sparsity, the error terms in any standard sieve estimation vastly exceed the main asymptotic terms, rendering current analytic tools incapable of isolating prime values. Furthermore, $M_p$ lacks an exploitable global algebraic structure that dynamically rules out systematic divisibility by prime factors as $p \to \infty$.

## 6. The Gap

The mathematical gap is the chasm between immense but finite computational verification and an unconditional asymptotic lower bound. We can efficiently verify the primality of specific $M_p$ using deterministic algorithms, and we can heuristically argue for their infinite distribution based on pseudo-random models of primes. 

The exact barrier to cross is the invention of a non-trivial, unconditional lower bound for the greatest prime factor of $2^p-1$, denoted $P^+(2^p-1)$. Proving that $P^+(2^p-1) = 2^p-1$ infinitely often is mathematically identical to the conjecture. Currently, we only have much weaker lower bounds on $P^+(2^n-1)$, derived from theorems like Zsigmondy's theorem or Baker's theorem on linear forms in logarithms, which are entirely insufficient to guarantee primality.

## 7. Current Research (as of June 2026)

Active research progresses along dual tracks:

1. **Algorithmic and Computational Optimization:** GIMPS continues to expand the search frontier. Recent implementations focus on optimizing large-integer arithmetic using giant Discrete Fourier Transforms (DFTs) and transitioning to Fermat Probable Prime (PRP) tests with error-checking tokens. These PRP tests are significantly less vulnerable to hardware faults than the non-resilient LLT.
2. **Heuristic Models:** Refining the Lenstra–Pomerance–Wagstaff heuristics to account for secondary error terms, and analyzing the statistical distribution of the divisors of Mersenne numbers over finite fields.
3. **Complexity Theory:** *(frontier — verify)* Efforts to construct unconditional deterministic polynomial-time primality tests specifically tailored for sparse generalized Mersenne numbers, building upon the theoretic foundations of the AKS primality test.

## 8. Future Work

Leading mathematicians suggest several long-term research strategies:
- **Thin Sieves:** Developing novel "thin sieve" frameworks capable of controlling error terms in exponentially growing, logarithmically sparse sequences.
- **The ABC Conjecture:** Exploring the profound implications of the generalized ABC conjecture on the prime factorizations of expressions of the form $2^p - 1$.
- **Analogous Sequences:** Proving the infinitude of primes in related sequences with similar heuristic density constraints, such as the Wagstaff primes $W_p = \frac{2^p + 1}{3}$ or the Fermat numbers $F_n = 2^{2^n} + 1$, where newly developed techniques might readily transfer.

## 9. Key References

- **[Foundational]** D. H. Lehmer. *An Extended Theory of Lucas' Functions.* Annals of Mathematics, 1930.
- **[Foundational]** S. S. Wagstaff Jr. *Divisors of Mersenne numbers.* Mathematics of Computation, 1983.
- **[SOTA / Recent]** R. Crandall and C. Pomerance. *Prime Numbers: A Computational Perspective.* Springer, 2005.
- **[Survey]** C. Pomerance. *Recent developments in primality testing.* The Mathematical Intelligencer, 1981.

## 10. Worked Example / Concrete Special Case

To illustrate how structural number theory restricts the factors of Mersenne numbers without requiring brute-force division, consider $M_{11} = 2^{11} - 1 = 2047$. We wish to determine if $M_{11}$ is prime.

Any prime factor $q$ of $M_p$ (where $p$ is an odd prime) must satisfy two stringent algebraic conditions:

1. **Modular Order Constraint:** Since $q \mid 2^p - 1$, we have $2^p \equiv 1 \pmod q$. The multiplicative order of $2$ modulo $q$ must divide the exponent $p$. Because $p$ is prime, this order is exactly $p$. By Fermat's Little Theorem, $2^{q-1} \equiv 1 \pmod q$, meaning $p \mid (q - 1)$. Because $q$ is an odd prime, $q-1$ is even, so $q$ must take the form $q = 2kp + 1$ for some integer $k$.
2. **Quadratic Residue Constraint:** Since $p$ is an odd prime, it can be written as $p = 2m + 1$. From $2^{2m+1} \equiv 1 \pmod q$, multiplying both sides by $2$ gives $2^{2m+2} \equiv 2 \pmod q$. This simplifies to $(2^{m+1})^2 \equiv 2 \pmod q$. This shows that $2$ is a perfect square (a quadratic residue) modulo $q$. By the second supplement to the law of quadratic reciprocity, $2$ is a quadratic residue modulo $q$ if and only if $q \equiv \pm 1 \pmod 8$.

Let us apply these filters to $p = 11$. Potential prime factors $q$ must take the form $q = 22k + 1$.
- For $k = 1$, we get $q = 23$. 
- We verify the quadratic residue condition for $q=23$: $23 = 8(3) - 1$, meaning $23 \equiv -1 \pmod 8$. Both conditions are perfectly satisfied.
- We perform a single division to test if $23$ divides $M_{11}$: $2047 \div 23 = 89$.

Thus, $M_{11} = 23 \times 89$, proving it is composite. This algebraic filtering successfully bypasses the need to check all prime numbers up to $\sqrt{2047} \approx 45$. This exact mathematical framework forms the backbone of the modern factoring algorithms used to eliminate candidate Mersenne numbers before running the expensive Lucas-Lehmer test.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*