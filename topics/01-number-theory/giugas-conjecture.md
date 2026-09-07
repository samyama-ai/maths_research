---
id: 01-number-theory/giugas-conjecture
title: "Giuga's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Giuga's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/giugas-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Giuga's Conjecture (also deeply related to the Agoh–Giuga Conjecture) posits that a positive integer $n > 1$ is a prime number if and only if it satisfies the congruence:

$$ \sum_{i=1}^{n-1} i^{n-1} \equiv -1 \pmod{n} $$

If $n$ is prime, this relation trivially holds as a direct consequence of Fermat's Little Theorem. The conjecture claims the converse: that no composite number can satisfy this congruence. A composite number that satisfies this relation would be a counterexample. The conjecture asserts that the set of such counterexamples is empty.

## 2. Mathematical Foundations

The forward direction of the conjecture rests on **Fermat's Little Theorem**, which states that if $p$ is a prime and $a$ is an integer not divisible by $p$, then $a^{p-1} \equiv 1 \pmod{p}$. Applying this to the sum:
$$ \sum_{i=1}^{p-1} i^{p-1} \equiv \sum_{i=1}^{p-1} 1 = p - 1 \equiv -1 \pmod{p} $$
Thus, all primes satisfy the condition. 

For the converse, Giuseppe Giuga proved that a composite number $n$ satisfies the congruence if and only if for every prime factor $p$ of $n$, two conditions hold simultaneously:
1. $p - 1 \mid n - 1$
2. $p \mid \frac{n}{p} - 1$

The first condition is the exact definition of a **Carmichael number** (a composite number that satisfies Fermat's Little Theorem for all bases coprime to it). The second condition defines what is now known as a **Giuga number** (or equivalently, $p^2 \mid (n - p)$ for all prime factors $p$). 

In 1990, Takashi Agoh formulated an equivalent conjecture using **Bernoulli numbers**, $B_k$, leading to the combined **Agoh–Giuga Conjecture**:
An integer $n > 1$ is prime if and only if:
$$ n B_{n-1} \equiv -1 \pmod{n} $$
The equivalence of the power-sum formulation and the Bernoulli formulation was formally proved by B. C. Kellner.

## 3. History & State of the Art (SOTA)

The conjecture was first proposed in 1950 by the Italian mathematician Giuseppe Giuga in his paper *Su una presumibile proprietà caratteristica dei numeri primi*, where he computationally verified the conjecture for all integers up to $10^{1000}$. 

Takashi Agoh's formulation via Bernoulli numbers in the 1990s linked the conjecture to deeper analytic properties of primes. In 1996, David Borwein, Jonathan M. Borwein, Peter B. Borwein, and Roland Girgensohn made significant structural insights, defining Giuga numbers formally and extending the computational bound for a counterexample to 13,800 digits.

The current State of the Art lower bound was established in 2013 by Borwein, Maitland, and Skerritt, who utilized the structural requirements of Carmichael and Giuga numbers to push the computational search space drastically higher. 

## 4. Partial Results / Verified Cases

While the general conjecture remains open, strong constraints on any potential counterexample have been rigorously proven:
- **Computational Bound:** It is verified that no counterexample exists below $10^{19908}$. Any counterexample must have at least **19,908 decimal digits**.
- **Prime Factors:** Any composite counterexample must have at least **4,771 distinct prime factors**.
- **Square-free:** Any counterexample must be a square-free integer.
- **Oddity:** Any counterexample must be odd, as Carmichael numbers are strictly odd.
- **Independence of Sets:** The sequence of known Giuga numbers begins with 30, 858, 1722, 66198... None of these are Carmichael numbers, further supporting the conjecture that the intersection of the two sets is empty.

## 5. Principal Obstacles

The central difficulty in proving Giuga's conjecture is that it requires demonstrating that the intersection of two sparse but potentially infinite sets of numbers (Carmichael numbers and Giuga numbers) is strictly empty. 
Carmichael numbers are known to be infinite (proved by Alford, Granville, and Pomerance in 1994), and it is widely suspected that Giuga numbers are also infinite. The simultaneous divisibility constraints $p - 1 \mid n - 1$ (multiplicative) and $p \mid \frac{n}{p} - 1$ (which relates closely to additive properties like $\sum_{p|n} \frac{1}{p} - \prod_{p|n} \frac{1}{p} \in \mathbb{N}$) are notoriously difficult to bound simultaneously using standard analytic number theory or sieve methods. Techniques that work on one condition tend to destroy the structure of the other.

## 6. The Gap

The precise gap is making the leap from large computational bounds to a rigorous analytic proof of non-existence. Specifically, one must prove that there is no integer solution $n$ having prime factorization $n = p_1 p_2 \dots p_k$ that simultaneously satisfies the Diophantine-like condition of Giuga numbers:
$$ \sum_{i=1}^k \frac{1}{p_i} - \prod_{i=1}^k \frac{1}{p_i} \in \mathbb{N} $$
and the modular constraint of Carmichael numbers ($p_i - 1 \mid n - 1$ for all $i$). Bridging this gap requires either finding a novel algebraic obstruction that makes these two conditions mutually exclusive or developing new asymptotic sieve theorems that prove the density of their intersection is absolute zero.

## 7. Current Research (as of June 2026)

Active research primarily branches into two camps:
1. **Computational Number Theory:** Developing more efficient algorithms to search for highly composite numbers satisfying the Giuga properties, aiming to increase the 19,908-digit bound. 
2. **Analytic Density Bounds:** Mathematicians such as Luca, Pomerance, and Shparlinski have established bounds on the distribution of Giuga numbers, showing their counting function is $o(\sqrt{x})$.
3. **Generalizations:** There is ongoing work generalizing the congruence to number rings (e.g., Giuga ideals) and exploring its analog using the Carmichael $\lambda(n)$ function, searching for deeper structural constraints. Occasional preprints make claims on the infinitude of Giuga numbers *(frontier — verify)*, but the intersection problem remains untouched analytically.

## 8. Future Work

Leading mathematicians suggest that the most promising pathway to a proof lies in deeply studying the "Giuga equation":
$$ \sum_{p \mid n} \frac{1}{p} - \prod_{p \mid n} \frac{1}{p} = m $$
where $m \ge 1$ is an integer. Understanding the exact solutions to this equation over sets of primes could allow researchers to rule out the possibility of those primes ever forming a Carmichael number. Improving the upper bounds on the number of solutions to this equation for a given $k$ (number of prime factors) is considered a critical next step.

## 9. Key References

- **[Foundational]** Giuga, G. *Su una presumibile proprietà caratteristica dei numeri primi.* Istituto Lombardo di Scienze e Lettere, Rendiconti, Classe di Scienze Matematiche e Naturali, 1950.
- **[Foundational]** Agoh, T. *On Giuga's conjecture.* Manuscripta Mathematica, 1995.
- **[Survey]** Borwein, D., Borwein, J. M., Borwein, P. B., & Girgensohn, R. *Giuga's Conjecture on Primality.* The American Mathematical Monthly, 1996.
- **[SOTA / Recent]** Borwein, J. M., Maitland, C., & Skerritt, M. P. *Computation of an improved lower bound to Giuga's primality conjecture.* Integers, 2013.

## 10. Worked Example / Concrete Special Case

Let us walk through a concrete calculation to illustrate the conjecture's mechanics.

**Case 1: A Prime Number ($n=3$)**
Calculate the sum for $n=3$:
$$ \sum_{i=1}^{2} i^{2} = 1^2 + 2^2 = 1 + 4 = 5 $$
Evaluate modulo 3:
$$ 5 \equiv 2 \equiv -1 \pmod{3} $$
This satisfies the congruence, as expected for a prime.

**Case 2: A Regular Composite Number ($n=4$)**
Calculate the sum for $n=4$:
$$ \sum_{i=1}^{3} i^{3} = 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 $$
Evaluate modulo 4:
$$ 36 \equiv 0 \pmod{4} $$
This does not equal $-1 \pmod{4}$, so $4$ correctly fails the test.

**Case 3: A Giuga Number ($n=30$)**
The smallest Giuga number is $30 = 2 \times 3 \times 5$. We can verify the Giuga condition $p \mid (30/p - 1)$ for its prime factors:
- For $p=2$: $2 \mid (15 - 1 = 14)$
- For $p=3$: $3 \mid (10 - 1 = 9)$
- For $p=5$: $5 \mid (6 - 1 = 5)$

However, to be a counterexample to Giuga's Conjecture, $30$ must *also* be a Carmichael number, requiring $p-1 \mid n-1$ for all prime factors. 
Let's check $p=3$:
$$ p-1 = 2 $$
$$ n-1 = 29 $$
Since $2$ does not divide $29$, $30$ is not a Carmichael number, and thus it is not a counterexample to Giuga's conjecture. This illustrates why finding a counterexample is so difficult: satisfying the fractional/additive Giuga conditions almost inevitably breaks the multiplicative Carmichael conditions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*