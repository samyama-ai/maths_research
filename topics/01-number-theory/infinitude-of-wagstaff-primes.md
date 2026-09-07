---
id: 01-number-theory/infinitude-of-wagstaff-primes
title: "Infinitude of Wagstaff Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Wagstaff Primes

> **Topic:** 01-number-theory · **ID:** `01-number-theory/infinitude-of-wagstaff-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there are infinitely many Wagstaff primes. A Wagstaff prime is a prime number $p$ of the form:

$$ p = \frac{2^q + 1}{3} $$

where $q$ is an odd prime. Formally, the problem requires proving that the set $\mathcal{W} = \{ q \in \mathbb{P} : \frac{2^q+1}{3} \text{ is prime} \}$ has infinite cardinality (where $\mathbb{P}$ denotes the set of prime numbers). A complete proof would analytically demonstrate that the density of such primes is bounded away from zero as $q \to \infty$, or otherwise establish a systematic, deterministic mechanism that generates infinitely many prime instances within the sequence.

## 2. Mathematical Foundations

The foundation of the problem lies in the properties of cyclotomic polynomials and exponential sequences in $\mathbb{Z}$. For any odd prime $q$, a Wagstaff number $W_q$ is defined by evaluating the $2q$-th cyclotomic polynomial $\Phi_{2q}(x)$ at $x=2$:

$$ \Phi_{2q}(x) = \frac{x^q + 1}{x + 1} $$

Evaluating this at $x=2$ yields:

$$ W_q = \Phi_{2q}(2) = \frac{2^q + 1}{3} $$

Because $2 \equiv -1 \pmod 3$, raising $2$ to any odd power $q$ yields $2^q \equiv -1 \pmod 3$. Therefore, $2^q + 1$ is always a multiple of $3$, ensuring that $W_q$ is strictly an integer for all odd integers $q$. A Wagstaff prime is defined as an instance where $W_q \in \mathbb{P}$.

The behavior of these primes is closely modeled by the **Lenstra–Pomerance–Wagstaff heuristic**, originally formulated for Mersenne primes ($2^q - 1$). The heuristic treats the sequence as a quasi-random process where the probability of primality is governed by the Prime Number Theorem. It predicts that the expected number of Wagstaff primes for exponents $q \le x$ grows asymptotically as $e^\gamma \log_2(x)$, where $\gamma$ is the Euler–Mascheroni constant, strongly implying infinitude.

## 3. History & State of the Art (SOTA)

The concept is named after Samuel S. Wagstaff Jr., who in 1983 formalized the probabilistic heuristic regarding the distribution of divisors of Mersenne numbers and related exponential sequences. In 1989, P. T. Bateman, J. L. Selfridge, and Wagstaff proposed the **New Mersenne Conjecture**, which ties together the primality of $q$, $M_q = 2^q - 1$, and $W_q = (2^q + 1)/3$, deeply embedding Wagstaff primes into the broader study of Mersenne-type numbers.

Historically, the search for Wagstaff primes has been driven computationally. The lack of an efficient deterministic primality test analogous to the Lucas–Lehmer test (used for Mersenne primes) means that for extremely large $q$, candidates can only be classified as Probable Primes (PRPs). 

As of recent distributed computing efforts, the state of the art (SOTA) is spearheaded by groups like PrimeGrid. The largest known Wagstaff PRP, discovered in June 2021 by Ryan Propper, is $W_{15135397} = (2^{15135397} + 1)/3$, a number with over 4.5 million decimal digits.

## 4. Partial Results / Verified Cases

While the overarching conjecture of infinitude remains entirely unproven, mathematicians and computational networks have successfully identified and rigorously verified specific prime instances of $W_q$.

- **Small exponents:** The sequence of primes $q$ that yield Wagstaff primes begins with $q \in \{3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 61, 79, 101, 127, 167, 191, 199, 313, 347, \dots\}$.
- **Largest Fully Proven Case:** Because PRPs are not mathematically proven primes, rigorous certification is required via Elliptic Curve Primality Proving (ECPP). ECPP has successfully provided definitive primality certificates for Wagstaff numbers up to $q = 141079$. The number $W_{141079}$ is the largest strictly proven Wagstaff prime to date, possessing 42,469 decimal digits.

## 5. Principal Obstacles

Standard techniques in analytic and algebraic number theory are entirely insufficient to prove the infinitude of Wagstaff primes due to several intractable bottlenecks:

1. **Exponential Sparsity:** The sequence $W_q$ grows exponentially. Traditional sieve methods (such as the Selberg sieve or the Friedlander–Iwaniec theorem) rely on bounding error terms that grow faster than the density of the set they are sieving. For sets of practically zero density in $\mathbb{Z}$, these error terms immediately dominate, rendering the sieves useless.
2. **Absence of Factorization Identities:** Unlike sequences derived from easily factorable polynomials, the polynomial structure $\Phi_{2q}(x)$ has no algebraic subgroups or sub-factorizations in $\mathbb{Z}$ that can be leveraged to force primality conditions, bypassing the analytic difficulties.
3. **Analytic Methodology Failure:** The Hardy-Littlewood circle method and the theory of modular forms excel in additive problems and polynomial properties of fixed degree. They offer no traction on pure exponential sequences like $2^q$.
4. **Computational Limitations:** The lack of a rapid deterministic primality test (such as an $O(q^2)$ or $O(q^3)$ test like Lucas-Lehmer) prevents computational evidence from scaling infinitely. The asymptotic time complexity of ECPP makes it practically impossible to certify modern PRPs with millions of digits.

## 6. The Gap

The precise gap is crossing the boundary between probabilistic heuristic models and rigorous deterministic bounds. We possess strong probabilistic heuristics (such as the Lenstra-Pomerance-Wagstaff heuristic and the Bateman-Horn conjecture) predicting that the sum of the probabilities of primality diverges, thus expecting infinite primes. The exact mathematical barrier is establishing an unconditional, deterministic lower bound proving the existence of at least one prime in infinite sub-intervals of $q$, essentially proving that no local, algebraic, or modular conspiracy forces all subsequent $W_q$ to be composite. Bridging this gap would require a monumental paradigm shift in additive combinatorics or sieve theory applied to sparse exponential sequences.

## 7. Current Research (as of June 2026)

Active research on Wagstaff primes is divided between algorithmic discovery and theoretical bounds:
- **Computational / Algorithmic:** Projects like PrimeGrid continue distributed PRP searches using optimized generalized Fermat prime search algorithms and PRP tests (like the V.R.S. test). Parallel research focuses on attempting to discover a Lucas-Lehmer-equivalent deterministic test specific to numbers of the form $(2^q+1)/3$.
- **Analytic / Heuristic:** Theoreticians continue to refine the New Mersenne Conjecture. * (frontier — verify)* Recent preprints explore using higher-order arithmetic geometry and finite field analysis to unconditionally bound the largest prime factor of $W_q$, aiming to prove that $W_q$ yields infinitely many "almost primes" (numbers with a bounded number of prime factors) as a theoretical stepping stone.

## 8. Future Work

Leading number theorists and computational mathematicians suggest several open pathways:
- **Almost Primes:** Formally proving that there exist infinitely many $W_q$ with at most $k$ prime factors (for some small integer $k > 1$).
- **Deterministic Testing:** Developing a deterministic primality test specific to $W_q$ that operates in polynomial time relative to $q$, bypassing the heavy machinery of ECPP.
- **Greatest Prime Factor:** Establishing an unconditional lower bound on the greatest prime factor of $W_q$, ideally improving upon existing limits derived from unconditional approximations of the ABC conjecture.

## 9. Key References

- **[Foundational]** Wagstaff, S. S., Jr. *Divisors of Mersenne numbers.* Mathematics of Computation, 1983.
- **[Foundational]** Bateman, P. T., Selfridge, J. L., & Wagstaff, S. S., Jr. *The New Mersenne Conjecture.* The American Mathematical Monthly, 1989.
- **[SOTA / Recent]** Morain, F. *Primality proving using elliptic curves: an update.* Algorithmic Number Theory Symposium (ANTS), 2007.

## 10. Worked Example / Concrete Special Case

To concretely illustrate the problem, we can evaluate a small instance to check if it yields a Wagstaff prime.

Let $q = 11$, which is an odd prime. We calculate the Wagstaff number $W_{11}$:

$$ W_{11} = \frac{2^{11} + 1}{3} $$

First, compute $2^{11}$:
$$ 2^{11} = 2048 $$

Next, substitute into the formula:
$$ W_{11} = \frac{2048 + 1}{3} = \frac{2049}{3} = 683 $$

We now test $683$ for primality. Its square root is $\sqrt{683} \approx 26.13$. We need only check divisibility by primes up to $23$ ($p \in \{2, 3, 5, 7, 11, 13, 17, 19, 23\}$):
- Not divisible by 2 (it is odd) or 5 (does not end in 0 or 5).
- Sum of digits is $6 + 8 + 3 = 17$, which is not divisible by $3$.
- $683 = 7 \times 97 + 4$ (not divisible by 7)
- $683 = 11 \times 62 + 1$ (not divisible by 11)
- $683 = 13 \times 52 + 7$ (not divisible by 13)
- $683 = 17 \times 40 + 3$ (not divisible by 17)
- $683 = 19 \times 35 + 18$ (not divisible by 19)
- $683 = 23 \times 29 + 16$ (not divisible by 23)

Since $683$ is not divisible by any prime $p \le \sqrt{683}$, it is prime. Thus, $W_{11} = 683$ is a verified Wagstaff prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*