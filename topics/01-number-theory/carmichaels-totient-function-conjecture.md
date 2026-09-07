---
id: 01-number-theory/carmichaels-totient-function-conjecture
title: "Carmichael's Totient Function Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Carmichael's Totient Function Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/carmichaels-totient-function-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Carmichael's totient function conjecture states that for every positive integer $n$, there exists at least one other positive integer $m \neq n$ such that $\phi(m) = \phi(n)$, where $\phi$ is Euler's totient function. 

In other words, no value of Euler's totient function is assumed exactly once. If we let $A(x)$ denote the number of solutions $m$ to the equation $\phi(m) = x$, then the conjecture asserts that $A(x)$ is never equal to 1. A complete proof requires showing that for all positive integers $v$ in the image of $\phi$, the preimage set $\phi^{-1}(v)$ contains at least two elements. A disproof would require finding a single counterexample $n$ for which $\phi(m) = \phi(n)$ implies $m = n$.

## 2. Mathematical Foundations

Euler's totient function, denoted $\phi(n)$, is an arithmetic function that counts the positive integers up to a given integer $n$ that are relatively prime to $n$.
Formally, we define it as:
$$ \phi(n) = |\{k \in \mathbb{N} : 1 \le k \le n \text{ and } \gcd(k, n) = 1\}| $$

By the fundamental theorem of arithmetic, if $n$ has the unique prime factorization $n = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}$ (where $p_i$ are distinct primes and $k_i > 0$), then the totient function can be computed using Euler's product formula:
$$ \phi(n) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^r p_i^{k_i - 1}(p_i - 1) $$

Let $N(v)$ denote the multiplicity of the value $v$, which is the number of preimages of $v$ under $\phi$:
$$ N(v) = |\{ x \in \mathbb{N} : \phi(x) = v \}| $$
Carmichael's conjecture states that for all $v \in \mathbb{Z}^+$, $N(v) \neq 1$. This implies that the image of $\phi$ (the set of totient numbers) is highly structured and redundant.

## 3. History & State of the Art (SOTA)

The conjecture was first proposed by Robert Carmichael in 1907. Carmichael initially claimed to have a proof of the theorem, but by 1922 he publicly acknowledged a flaw in his logic pointed out by another mathematician. Over the decades, many mathematicians have verified the conjecture computationally up to enormous bounds, relying on sieve methods and properties of primes.

In 1999, Kevin Ford achieved a monumental theoretical result regarding the distribution of values of $N(v)$. He proved that for every integer $k \ge 2$, there exists a value $v$ such that $N(v) = k$. More importantly for Carmichael's conjecture, Ford proved that if there exists an integer $v$ such that $N(v) = 1$, then the smallest such $v$ (and its corresponding counterexample $n$) must be astronomically large, specifically $\phi(n) > 10^{10^{10}}$. This result effectively renders brute-force computational searches for a counterexample completely impossible.

## 4. Partial Results / Verified Cases

While the conjecture remains open for all $n$, massive lower bounds and structural requirements for any potential counterexample $n$ have been established:
- Carmichael (1922) originally proved that any counterexample $n$ must be a multiple of $2^2 \cdot 3^2 \cdot 7 \cdot 43$.
- Victor Klee (1947) extended these algebraic constraints, showing that any counterexample must be divisible by $2^2 \cdot 3^2 \cdot 7^2 \cdot 43^2$.
- Schlafly and Wagon (1994) leveraged Klee's methods with computational algorithms to show any counterexample $n$ must have over $10^{7}$ digits.
- Kevin Ford (1998/1999) established the current state-of-the-art bound, proving that any counterexample $n$, if it exists, must be greater than $10^{10^{10}}$.
- Carl Pomerance (1974) proved that Carmichael's conjecture is unconditionally true if certain properties about the uniform distribution of prime numbers in arithmetic progressions (related to Schinzel's Hypothesis H) hold.

## 5. Principal Obstacles

The primary obstacle to resolving Carmichael's conjecture is our limited understanding of the exact preimages of the totient function, specifically the intricate multiplicative relationships among shifted primes (i.e., integers of the form $p-1$). The value of $\phi(n)$ is entirely determined by the prime factors of $n$. If $N(\phi(n)) = 1$, then $n$ must be an incredibly constrained number such that no other combination of primes $q_i$ can produce the same product $\prod q_i^{a_i-1}(q_i - 1)$. 

Traditional analytic number theory techniques (such as sieve theory, the Hardy-Littlewood circle method, and Dirichlet series) provide excellent asymptotic bounds on the *average* behavior of arithmetic functions. However, they struggle profoundly with exact point-wise equations like $N(v)=1$. We lack the algebraic tools to rule out the existence of a highly pathological set of primes that perfectly avoids generating a duplicate totient value.

## 6. The Gap

The exact boundary of human knowledge lies between the massive lower bound ($10^{10^{10}}$) for a counterexample and an absolute unconditional proof of its non-existence. Ford proved that the set of values $m$ for which $N(\phi(m)) = k$ is infinite for any integer $k \ge 2$, but the singleton case $k=1$ remains entirely elusive. The precise mathematical gap is connecting the deep algebraic constraints on prime factors (required for a counterexample to exist) to an unconditional combinatorial or analytic impossibility theorem. Crossing this barrier likely requires a breakthrough in the prime $k$-tuples conjecture or the structural theory of shifted primes.

## 7. Current Research (as of June 2026)

Active research continues primarily along two fronts:
1.  **Conditional Proofs and Hypothesis H:** Number theorists are connecting the conjecture to other major unproven hypotheses. It is well understood that if a sufficiently strong version of the prime $k$-tuples conjecture (like Dickson's conjecture or Schinzel's Hypothesis H) holds, then Carmichael's conjecture is true. Current work involves exploring whether weaker, more tractable variants of these hypotheses might suffice to prove Carmichael's conjecture unconditionally.
2.  **Sieve Method Enhancements:** Refinements to the intricate sieve methods used by Pomerance and Ford are occasionally proposed to restrict the density of possible prime configurations that could yield a counterexample. *(frontier — verify)* Recent preprints attempt to leverage advances in the study of bounded gaps between primes (e.g., Maynard-Tao methods) to place tighter restrictions on the prime factorization of a hypothetical $n$.

## 8. Future Work

Leading number theorists suggest that an unconditional proof of Carmichael's conjecture will require a completely new approach to the distribution of shifted primes. Future pathways include:
- Establishing a rigid structural or algebraic property of the pre-image set $\phi^{-1}(v)$ that prevents it from ever being a singleton under any prime distribution.
- Finding unconditionally true weakened forms of the prime $k$-tuples conjecture that can restrict the possible prime factorizations of a counterexample to the empty set.
- Exploring connections with algebraic geometry or elliptic curves over finite fields to translate the multiplicative properties of $p-1$ into a more robust geometric problem that avoids the limitations of standard sieve theory.

## 9. Key References

- **[Foundational]** Carmichael, R. D. *On Euler's $\phi$-function*. Bulletin of the American Mathematical Society, 1907.
- **[Foundational]** Klee, V. L. *On a conjecture of Carmichael*. Bulletin of the American Mathematical Society, 1947.
- **[SOTA / Recent]** Ford, K. *The number of solutions of $\phi(x) = m$*. Annals of Mathematics, 1999.
- **[SOTA / Recent]** Pomerance, C. *On Carmichael's conjecture*. Proceedings of the American Mathematical Society, 1974.
- **[Survey]** Schlafly, A., and Wagon, S. *Carmichael's conjecture on the Euler function is valid below $10^{10^7}$*. Mathematics of Computation, 1994.

## 10. Worked Example / Concrete Special Case

To ground the abstract statement, consider the small integers and their totient values to verify that $N(v) \neq 1$.
Let us evaluate $\phi(n)$ for a few small values of $n$:
- $\phi(1) = 1$
- $\phi(2) = 1$
- $\phi(3) = 2$
- $\phi(4) = 2$
- $\phi(5) = 4$
- $\phi(6) = 2$
- $\phi(8) = 4$
- $\phi(10) = 4$
- $\phi(12) = 4$

Notice the preimages for small values of $v$:
- For $v = 1$, the preimages are $\{1, 2\}$, so $N(1) = 2 \neq 1$.
- For $v = 2$, the preimages are $\{3, 4, 6\}$, so $N(2) = 3 \neq 1$.
- For $v = 4$, the preimages are $\{5, 8, 10, 12\}$, so $N(4) = 4 \neq 1$.

In each of these concrete cases, we see that the number of solutions to $\phi(m) = v$ is strictly greater than 1. For example, if we start with $n=3$, its totient is $\phi(3)=2$. Carmichael's conjecture asserts there must be at least one other integer $m \neq 3$ with $\phi(m)=2$. Looking at our calculations, we easily find $m=4$ and $m=6$. This multiplicity of preimages is precisely what Carmichael's conjecture claims must hold for *every* positive integer $n$, ad infinitum.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*