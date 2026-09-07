---
id: 01-number-theory/infinitude-of-wilson-primes
title: "Infinitude of Wilson Primes"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Wilson Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-wilson-primes` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture postulates that there exist infinitely many Wilson primes. A Wilson prime is a prime number $p$ such that $p^2$ divides $(p-1)! + 1$. Equivalently, the congruence $(p-1)! \equiv -1 \pmod{p^2}$ holds. This asserts that the known sequence of Wilson primes ($5, 13, 563, \dots$) does not terminate. A complete proof requires demonstrating a theoretical mechanism or distribution that yields infinitely many such primes, while a disproof would require demonstrating that the set of primes satisfying this congruence is strictly finite.

## 2. Mathematical Foundations

The conjecture is built upon Wilson's Theorem, a fundamental result in elementary number theory which states that for any prime $p$:

$$ (p-1)! \equiv -1 \pmod p $$

Because $(p-1)! + 1$ is guaranteed to be a multiple of $p$, we can define the **Wilson quotient**, $W_p$, as the integer:

$$ W_p = \frac{(p-1)! + 1}{p} $$

A prime $p$ is defined as a Wilson prime if and only if $W_p \equiv 0 \pmod p$.

Theoretical support for the infinitude of Wilson primes relies heavily on probabilistic heuristics. Assuming that the residues of $W_p \pmod p$ are uniformly distributed and behave pseudo-randomly as $p$ varies, the probability that a prime $p$ divides $W_p$ is approximately $1/p$. Applying Mertens' theorems, the expected number of Wilson primes in the interval $[2, x]$ is given by the sum:

$$ \sum_{p \le x} \frac{1}{p} \sim \ln \ln x + O(1) $$

Because $\lim_{x \to \infty} \ln \ln x = \infty$, this heuristic predicts that there are infinitely many Wilson primes, albeit with an exceptionally slow, doubly-logarithmic asymptotic growth rate.

## 3. History & State of the Art (SOTA)

The foundational theorem was first formulated by Ibn al-Haytham (c. 1000 AD) and later independently discovered by John Wilson in the 18th century, with the first formal proof published by Lagrange in 1771.

The investigation into the stronger congruence modulo $p^2$ emerged in the 20th century. 
- The first two Wilson primes, $p = 5$ and $p = 13$, were known from early manual calculations.
- The third Wilson prime, $p = 563$, was discovered by Karl Goldberg in 1953 using the SEAC (Standards Eastern Automatic Computer), marking a significant milestone in computational number theory.

Since Goldberg's discovery, no new Wilson primes have been found. The State of the Art (SOTA) is defined almost entirely by the computational limits of verifying the congruence for massive primes. The algorithmic complexity of computing factorials modulo $p^2$ requires highly optimized Fast Fourier Transform (FFT) polynomial arithmetic. Successive algorithmic improvements have pushed the search boundaries higher over the decades:
- **1997:** Crandall, Dilcher, and Pomerance searched up to $5 \times 10^8$.
- **2004:** McIntosh extended the search up to $5 \times 10^9$.
- **2014:** Costa, Gerbicz, and Harvey introduced a novel algorithm to evaluate $W_p \pmod p$ more efficiently, extending the exhaustive search limit to $2 \times 10^{13}$.

## 4. Partial Results / Verified Cases

There are no partial theoretical results establishing infinite sub-families of Wilson primes, nor are there unconditional lower bounds beyond the known examples.

- **Verified Cases:** The conjecture is solved in the affirmative for exactly three specific mathematical instances: $p \in \{5, 13, 563\}$.
- **Computational Ranges:** The problem has been explicitly evaluated for all primes $p < 2 \times 10^{13}$. It is definitively known that no other Wilson primes exist in this range. The extreme scarcity of verified cases (only three found up to trillions) perfectly aligns with the incredibly slow growth rate predicted by the $\ln \ln x$ heuristic.

## 5. Principal Obstacles

The primary theoretical obstacle is the severe lack of algebraic or geometric structure linking $(p-1)!$ to the modulus $p^2$. Factorials are inherently multiplicative constructs, whereas the modulus $p^2$ relies on additive properties and $p$-adic arithmetic. 

Standard techniques from analytic number theory (such as sieve methods, L-functions, or circle methods) fail because they depend heavily on global generating functions or the properties of polynomials over global fields. The Wilson quotient involves factorial functions, which grow too rapidly and lack a natural, tractable generating function.

Furthermore, Wilson primes lack a direct algebraic analogue. For instance, Fermat quotients $q_p(a) = \frac{a^{p-1}-1}{p}$ (associated with Wieferich primes) can be studied via group theory, units in finite fields, and Galois representations. The Wilson quotient, by contrast, behaves almost entirely pseudo-randomly and lacks this deep structural integration into algebraic number theory.

## 6. The Gap

The gap lies between empirical, statistical heuristic arguments and rigorous proof. Number theorists possess a robust probabilistic model ($\sum 1/p$) and massive computational verification up to $2 \times 10^{13}$, but absolutely zero theoretical techniques to establish an absolute lower bound on the number of Wilson primes as $x \to \infty$. 

To cross this barrier, mathematicians must discover a hidden arithmetic, $p$-adic, or algebraic geometric structure that intrinsically relates the factorial function modulo $p^2$ to well-understood arithmetic objects—similar to how Herbrand's theorem bridges Bernoulli numbers and irregular primes. Until the pseudo-randomness of $W_p \pmod p$ can be bypassed by structural constraints, the conjecture will remain out of reach.

## 7. Current Research (as of June 2026)

Current active research is heavily skewed towards computational optimization.
- **Algorithmic Refinements:** Algorithm designers are continuously working to reduce the complexity of calculating factorials modulo $p^2$, aiming to break the $O(p^{1/2+\epsilon})$ barrier using advanced FFTs over finite rings to push the search bound well beyond $10^{14}$.
- **Theoretical Heuristics:** Number theorists are investigating generalized factorial functions (e.g., Bhargava factorials) and studying the distribution of related rare prime classes—such as Wieferich primes and Wall-Sun-Sun primes—which share the same underlying $\sum 1/p$ probabilistic heuristic. Advances in the equidistribution of these generalized quotients could indirectly inform the Wilson prime problem.

## 8. Future Work

Leading number theorists have suggested several potential pathways to theoretically attack the problem:
- **$p$-adic Analysis:** Establishing a deep, rigorous connection between $W_p \pmod p$ and $p$-adic L-functions or Iwasawa theory.
- **Function Field Analogues:** Investigating function field analogues of Wilson primes, where the arithmetic problem can be translated into the geometry of curves over finite fields, making it susceptible to the powerful tools of algebraic geometry.
- **Conditional Proofs:** Exploring whether assuming overwhelmingly strong, unproven conjectures (such as the Generalized Riemann Hypothesis or the ABC conjecture) might yield conditional lower bounds for the number of Wilson primes.

## 9. Key References

- **[Foundational]** K. Goldberg. *A table of Wilson quotients and the third Wilson prime.* Journal of the London Mathematical Society, 1953.
- **[SOTA / Recent]** E. Costa, R. Gerbicz, D. Harvey. *A search for Wilson primes to $2 \times 10^{13}$.* Mathematics of Computation, 2014. (https://doi.org/10.1090/S0025-5718-2014-02800-7)
- **[Survey]** R. Crandall, K. Dilcher, C. Pomerance. *A search for Wieferich and Wilson primes.* Mathematics of Computation, 1997.

## 10. Worked Example / Concrete Special Case

To ground the abstract definition, we can manually check whether small primes are Wilson primes.

**Testing $p = 5$:**
1. Compute $(p-1)!$: 
   $$ (5-1)! = 4! = 4 \times 3 \times 2 \times 1 = 24 $$
2. Verify Wilson's Theorem ($p$ divides $(p-1)! + 1$):
   $$ 24 + 1 = 25 $$
   Since $25$ is divisible by $5$, the theorem holds.
3. Check the Wilson Prime condition ($p^2$ divides $(p-1)! + 1$):
   $$ p^2 = 5^2 = 25 $$
   Since $25$ divides $25$ exactly, $5$ is a Wilson prime. 
   Equivalently, the Wilson quotient is $W_5 = \frac{24 + 1}{5} = 5$. Because $W_5 \equiv 0 \pmod 5$, $5$ is a Wilson prime.

**Testing $p = 7$:**
1. Compute $(p-1)!$:
   $$ (7-1)! = 6! = 720 $$
2. Verify Wilson's Theorem:
   $$ 720 + 1 = 721 $$
   $721 / 7 = 103$. The theorem holds.
3. Check the Wilson Prime condition:
   The Wilson quotient is $W_7 = 103$. 
   We evaluate $103 \pmod 7$:
   $$ 103 = 7 \times 14 + 5 $$
   Because $W_7 \equiv 5 \pmod 7$ (which is strictly not $0$), $7$ is **not** a Wilson prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*