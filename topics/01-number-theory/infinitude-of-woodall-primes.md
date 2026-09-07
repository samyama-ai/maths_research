---
id: 01-number-theory/infinitude-of-woodall-primes
title: "Infinitude of Woodall Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Woodall Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-woodall-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that there exist infinitely many integer values of $n \ge 1$ such that the Woodall number, defined as $W_n = n \cdot 2^n - 1$, is a prime number. 

A complete proof of this conjecture would require a rigorous mathematical demonstration that the sequence of Woodall primes is unbounded. Conversely, a disproof would require showing that there exists a maximum index $N$ such that for all $n > N$, $W_n$ is strictly composite.

## 2. Mathematical Foundations

A **Woodall number** is an integer of the form:
$$W_n = n \cdot 2^n - 1$$
for any natural number $n \ge 1$. A **Woodall prime** is a Woodall number that is also prime. 

These numbers are intimately related to **Cullen numbers**, which take the form $C_n = n \cdot 2^n + 1$. Woodall primes are sometimes referred to as Cullen primes of the second kind.

The primality of Woodall numbers can be efficiently determined using the **Lucas–Lehmer–Riesel (LLR) test**. For an integer $N = k \cdot 2^n - 1$ (with $k < 2^n$), the test involves a sequence defined by:
$$u_0 = \text{a specific starting value dependent on } k$$
$$u_{i+1} = (u_i^2 - 2) \pmod N$$
The integer $N$ is prime if and only if $u_{n-2} = 0$. For Woodall numbers, we set $k = n$, requiring that $n < 2^n$, which holds for all $n \ge 1$.

Heuristically, the probability that a number $N$ is prime is roughly $1 / \ln(N)$. For Woodall numbers, $\ln(W_n) \approx \ln(n \cdot 2^n) \approx n \ln 2 + \ln n$. If we sum these probabilities over all $n$:
$$\sum_{n=1}^{\infty} \frac{1}{n \ln 2 + \ln n} = \infty$$
Because the harmonic series diverges, prime number heuristics strongly suggest that there should be infinitely many Woodall primes.

## 3. History & State of the Art (SOTA)

Woodall numbers were first systematically studied by Allan J. C. Cunningham and H. J. Woodall in 1917. Woodall originally compiled tables of these numbers, attempting to factor them to find which were composite and which were prime.

Historically, the search for Woodall primes was limited by computational constraints. With the advent of distributed computing and the efficient LLR test, the search has reached massive scales. The PrimeGrid distributed computing project has been instrumental in finding the largest known Woodall primes over the past two decades.

Despite the discovery of exceedingly large Woodall primes, theoretical progress on proving their infinitude has been essentially non-existent. Like the infinitude of Mersenne primes ($2^n - 1$) and regular Cullen primes, this problem sits completely outside the reach of current theoretical machinery.

## 4. Partial Results / Verified Cases

While the infinitude conjecture remains entirely open, the conjecture has been empirically verified up to very large ranges. 

The first few indices $n$ that yield Woodall primes are:
$$n = 2, 3, 6, 30, 75, 81, 115, 464, 90, 949, 25836, \dots$$

Computational searches (predominantly by PrimeGrid) have tested all values of $n$ up to several million. The largest known Woodall primes have indices $n$ in the millions. For example, in 2007, a Woodall prime was found for $n = 3752948$. Later discoveries have verified primes for indices exceeding $n = 10^7$. 

Furthermore, a theorem by Christopher Hooley (1976) adapted to this sequence demonstrates that almost all Woodall numbers are composite. The density of primes in the sequence approaches zero, even if the absolute count of primes is conjectured to be infinite.

## 5. Principal Obstacles

The central obstacle in proving the infinitude of Woodall primes is that the sequence $W_n = n \cdot 2^n - 1$ grows exponentially. Standard analytic number theory and sieve methods, such as the Selberg sieve or the Bombieri-Vinogradov theorem, apply to polynomial sequences or sequences with a high density of elements in intervals (like arithmetic progressions). 

Because $W_n$ grows so quickly, the values become incredibly sparse. To prove that infinitely many primes exist in such a sparse sequence requires ruling out the existence of some subtle, undiscovered algebraic or modular "conspiracy" that ensures every $W_n$ is composite past a certain point. We have no mathematical tools to bound the distribution of primes in integer sequences of the form $f(n)a^n + b$. 

Additionally, we do not fully understand the factorization of $2^n - 1$ or related exponential constructs. Any attempt to show that $n \cdot 2^n - 1$ avoids having small prime factors for infinitely many $n$ stumbles upon the pseudorandom nature of the multiplicative order of $2 \pmod p$.

## 6. The Gap

The gap lies between statistical heuristics and rigorous proof. We know from computational verification (Section 4) that Woodall primes exist for enormous values of $n$, and probabilistic models (Section 2) predict infinitely many. However, the exact mathematical barrier is our inability to trace prime divisors in mixed algebraic-exponential sequences. To bridge this gap, one would need a fundamentally new type of sieve theory capable of operating on exponentially sparse sets, or a breakthrough in the arithmetic geometry of exponential sums.

## 7. Current Research (as of June 2026)

Current research operates on two disparate fronts:
1. **Computational:** Distributed projects like PrimeGrid continue to execute LLR tests on unverified ranges of $n$, pushing the boundary of known Woodall primes and providing more data to refine heuristic models.
2. **Structural & Divisibility:** Theoretical number theorists focus on proving divisibility properties and congruences for Woodall numbers. For instance, studying "Riesel numbers" (where $k \cdot 2^n - 1$ is composite for all $n$) helps map the landscape of the composite instances in similar sequences.

*(frontier — verify)* Recent preprints have begun exploring polynomial analogies over finite fields $\mathbb{F}_q[T]$, looking at sequences like $P \cdot X^P - 1$, where some infinitude theorems for sparse sequences can be proven using geometric tools (like étale cohomology) that are unavailable over $\mathbb{Z}$.

## 8. Future Work

Leading mathematicians suggest that attacking the infinitude of Woodall primes directly is currently intractable. Suggested preliminary research strategies include:
- **Unconditional lower bounds:** Proving that the number of prime factors of $W_n$ tends to infinity, or finding tight bounds on the largest prime factor of $W_n$.
- **Function Field Analogues:** Proving the infinitude of "Woodall irreducibles" in the ring of polynomials over a finite field, which might provide geometric intuition for the integer case.
- **Riesel/Sierpinski connections:** Gaining a definitive understanding of which multipliers $n$ guarantee that $n \cdot 2^n - 1$ is always composite, to better isolate the subset of $n$ that can theoretically yield primes.

## 9. Key References

- **[Foundational]** Cunningham, A. J. C., & Woodall, H. J. "Factorisation of $Q = (2^q \mp q)$ and $(q \cdot 2^q \mp 1)$." *Messenger of Mathematics*, 47, 1-38, 1917.
- **[Foundational]** Riesel, H. "Lucasian Criteria for the Primality of $N=h \cdot 2^n - 1$." *Mathematics of Computation*, 23(108), 869-875, 1969.
- **[SOTA / Recent]** Keller, W. "New Cullen Primes." *Mathematics of Computation*, 64(212), 1733-1741, 1995.
- **[Survey]** Guy, R. K. *Unsolved Problems in Number Theory* (3rd ed.). Springer, 2004. (Section A3 covers Mersenne, Fermat, Cullen, and Woodall numbers).

## 10. Worked Example / Concrete Special Case

We evaluate the Woodall numbers for small values of $n$ to observe the sequence and its prime/composite nature.

**Case $n = 1$:**
$W_1 = 1 \cdot 2^1 - 1 = 2 - 1 = 1$
(Not prime, as 1 is the unit).

**Case $n = 2$:**
$W_2 = 2 \cdot 2^2 - 1 = 2 \cdot 4 - 1 = 8 - 1 = 7$
(7 is a prime number. This is the first Woodall prime).

**Case $n = 3$:**
$W_3 = 3 \cdot 2^3 - 1 = 3 \cdot 8 - 1 = 24 - 1 = 23$
(23 is a prime number. This is the second Woodall prime).

**Case $n = 4$:**
$W_4 = 4 \cdot 2^4 - 1 = 4 \cdot 16 - 1 = 64 - 1 = 63$
We test 63 for primality. It is divisible by 3 (since $6+3=9$). Factoring it yields $63 = 7 \times 9 = 3^2 \times 7$. 
(Composite).

**Case $n = 5$:**
$W_5 = 5 \cdot 2^5 - 1 = 5 \cdot 32 - 1 = 160 - 1 = 159$
Sum of digits is $1+5+9=15$, so it is divisible by 3. $159 = 3 \times 53$.
(Composite).

**Case $n = 6$:**
$W_6 = 6 \cdot 2^6 - 1 = 6 \cdot 64 - 1 = 384 - 1 = 383$
Checking primes up to $\sqrt{383} \approx 19.5$ (i.e., 2, 3, 5, 7, 11, 13, 17, 19): none of these divide 383. Thus, 383 is prime.
(This is the third Woodall prime).

This small manual verification grounds the problem, illustrating that while Woodall primes appear early on ($n=2, 3, 6$), intervening values quickly become composite as $W_n$ grows and falls victim to small prime divisors.