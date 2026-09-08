---
id: 01-number-theory/erdos-squarefree-conjecture
title: "Erdos Squarefree Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Squarefree Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-squarefree-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Erdős Squarefree Conjecture asserts that the central binomial coefficient $\binom{2n}{n}$ is never a squarefree integer for any integer $n > 4$. A positive integer is considered squarefree if its prime factorization has no repeated prime factors (i.e., it is not divisible by $p^2$ for any prime $p$). 

Thus, the conjecture states that for all $n > 4$, there exists at least one prime $p$ such that $p^2 \mid \binom{2n}{n}$. It postulates that the complete set of positive integers $n$ for which the central binomial coefficient is squarefree is exactly the finite set $\{1, 2, 4\}$.

## 2. Mathematical Foundations

Let $n \in \mathbb{N}$. The central binomial coefficient is formally defined as:
$$ \binom{2n}{n} = \frac{(2n)!}{(n!)^2} $$

The mathematical foundation for analyzing the prime factorization of factorials and binomial coefficients relies heavily on $p$-adic valuations. The $p$-adic valuation $v_p(N)$ denotes the exponent of the highest power of a prime $p$ that divides an integer $N$. An integer $N$ is squarefree if and only if $v_p(N) \le 1$ for all primes $p$.

By Legendre's formula, the $p$-adic valuation of a factorial is given by:
$$ v_p(n!) = \sum_{k=1}^\infty \left\lfloor \frac{n}{p^k} \right\rfloor $$

Applying Legendre's formula to the central binomial coefficient yields:
$$ v_p\left(\binom{2n}{n}\right) = v_p((2n)!) - 2v_p(n!) = \sum_{k=1}^\infty \left( \left\lfloor \frac{2n}{p^k} \right\rfloor - 2\left\lfloor \frac{n}{p^k} \right\rfloor \right) $$

Because $\lfloor 2x \rfloor - 2\lfloor x \rfloor \in \{0, 1\}$ for any real number $x$, the valuation $v_p\left(\binom{2n}{n}\right)$ is exactly the number of terms in this infinite sum that equal 1. 

By Kummer's Theorem, this valuation equivalently corresponds to the number of carries that occur when adding $n$ to itself (i.e., computing $n + n$) in base $p$. To prove that $\binom{2n}{n}$ is not squarefree, one must demonstrate that for every $n > 4$, there exists some prime $p$ for which the base-$p$ addition of $n + n$ produces at least two carries.

## 3. History & State of the Art (SOTA)

The problem was notably popularized by Paul Erdős, appearing prominently in his 1980 book with Ronald Graham, *Old and New Problems and Results in Combinatorial Number Theory*.

- **1985:** András Sárközy achieved the first major theoretical milestone, proving the conjecture for all sufficiently large $n$. Using tools from analytic number theory, Sárközy established that there exists an absolute constant $n_0$ such that for all $n > n_0$, $\binom{2n}{n}$ is not squarefree.
- **1988 & 1991:** In the absence of an explicit bound for $n_0$, J. Goetgheluck (1988) and I. Vardi (1991) leveraged computational methods to verify the conjecture algorithmically up to $n = 3.16 \times 10^{11}$. 
- **1996:** Andrew Granville and Olivier Ramaré published their seminal paper in *Mathematika*, completing the proof. They provided highly explicit bounds on exponential sums over primes, radically shrinking Sárközy's theoretical constant $n_0$ until it overlapped with computational limits, thereby unconditionally proving the conjecture for all $n > 4$.

## 4. Partial Results / Verified Cases

Because the conjecture is fully solved, it is mathematically verified for the entirety of $\mathbb{N}_{>4}$. 

- The central binomial coefficient is explicitly squarefree for exactly three small dimensions/values: 
  - $n = 1 \implies \binom{2}{1} = 2$
  - $n = 2 \implies \binom{4}{2} = 6 = 2 \cdot 3$
  - $n = 4 \implies \binom{8}{4} = 70 = 2 \cdot 5 \cdot 7$
- **Computational bounds:** Prior to the 1996 proof, the most significant verified case was Goetgheluck's algorithmic sweep ensuring no counterexamples existed in the range $4 < n \le 3.16 \times 10^{11}$.
- **Generalizations:** J. W. Sander (1992) verified related partial cases, proving that for any fixed, sufficiently small integer $d$, the shifted binomial coefficients $\binom{2n \pm d}{n}$ are also never squarefree for sufficiently large $n$.

## 5. Principal Obstacles

Prior to its complete resolution, the conjecture remained stubbornly open because standard mathematical techniques in analytic number theory failed to provide computable constants. 

Methods relying on traditional Fourier analysis, the Hardy-Littlewood circle method, and standard Weyl bounds are highly effective at proving asymptotic density or showing that a property holds as $n \to \infty$. However, these techniques intrinsically introduce astronomically large, unspecified "implied constants" (e.g., $O$-notation bottlenecks). 

Sárközy's initial proof relied on bounding exponential sums over primes to show that prime factors $p \approx \sqrt{n}$ heavily divide the binomial coefficient. Because standard prime number theorems and exponential sum estimates lack tight, explicit error terms without assuming the Generalized Riemann Hypothesis (GRH), the threshold $n_0$ generated by these methods was orders of magnitude beyond any computational limit, making a full proof impossible using conventional asymptotic strategies.

## 6. The Gap

The exact boundary that needed to be crossed to fully resolve the conjecture was the numeric chasm between empirical computation and abstract asymptotic thresholds. Specifically, mathematicians needed to close the gap between $n \approx 10^{11}$ (the limit of supercomputers at the time) and $n_0$ (the lower limit of Sárközy's proof, which was virtually uncomputable). 

The exact mathematical step required to cross this barrier was the derivation of completely explicit, sharp analytic inequalities for exponential sums over prime numbers. By optimizing error terms and generating hard bounds, Granville and Ramaré squeezed the theoretical gap to a strictly finite, computationally traversable domain.

## 7. Current Research (as of June 2026)

With the core conjecture definitively solved, active research has shifted toward generalizing the scarcity of squarefree numbers in other combinatorial sequences. 
- **Generalized Catalan Numbers:** Schools of thought are currently analyzing the prime power divisibility of $C_n^{(s)} = \frac{1}{(s-1)n+1} \binom{sn}{n}$ and broader generalized binomial coefficients.
- **Residues Modulo Prime Powers:** Current computational groups are mapping the exact distribution of $p$-adic valuations $v_p\left(\binom{n}{k}\right)$ for arbitrary $k$ across Pascal's triangle. 
- **Anatomy of Integers:** A prominent theoretical direction involves using smooth numbers and the distribution of prime gaps to understand how frequently *adjacent* combinatorial terms share large prime power factors, extending explicit bound techniques to more exotic integer sequences. *(frontier — verify)*

## 8. Future Work

Leading mathematicians have outlined several open pathways extending the Granville-Ramaré framework:
- **Higher-Order Divisibility:** Generalizing the problem to investigate $k$-free values (e.g., cubefree values) of binomial coefficients.
- **Arbitrary Coefficients:** Establishing whether an analogous finite exception set exists for $\binom{n}{k}$ where $k \ge 2$, requiring uniform bounds across two variables rather than the single-variable central coefficient.
- **Polynomial Applications:** Adapting explicit exponential sum bounds to conditionally bound the scarcity of squarefree values for general irreducible polynomials, potentially relying on the $abc$-conjecture framework.

## 9. Key References

- **[Foundational]** Erdős, P., and Graham, R. L. *Old and New Problems and Results in Combinatorial Number Theory.* L'Enseignement Mathématique, 1980.
- **[Foundational]** Sárközy, A. *On divisors of binomial coefficients, I.* Journal of Number Theory, 20(1), 70-80, 1985. [DOI](https://doi.org/10.1016/0022-314x(85)90017-4)
- **[SOTA / Recent]** Goetgheluck, J. *On prime divisors of binomial coefficients.* Mathematics of Computation, 51(183), 325-329, 1988. [DOI](https://doi.org/10.1090/s0025-5718-1988-0942159-6)
- **[SOTA / Recent]** Granville, A., and Ramaré, O. *Explicit bounds on exponential sums and the scarcity of squarefree binomial coefficients.* Mathematika, 43(1), 73-107, 1996. [DOI](https://doi.org/10.1112/s0025579300011608)

## 10. Worked Example / Concrete Special Case

To ground the abstract formulation, consider the base-$p$ carry mechanisms (via Kummer's Theorem) for $n=4$ and $n=5$.

**Case $n=4$ (The last squarefree instance):**
$$ \binom{8}{4} = \frac{8!}{4!4!} = 70 $$
The prime factorization of 70 is $2^1 \cdot 5^1 \cdot 7^1$. Because all prime exponents are strictly equal to 1, $\binom{8}{4}$ is unequivocally squarefree. 
Using Kummer's Theorem for $p=2$: The number 4 in base 2 is $100_2$. 
Adding $100_2 + 100_2 = 1000_2$ yields exactly $1$ carry (at the fours place). Thus, $v_2\left(\binom{8}{4}\right) = 1$. No prime forces a valuation $\ge 2$.

**Case $n=5$ (Not squarefree, crossing the $n>4$ threshold):**
$$ \binom{10}{5} = \frac{10!}{5!5!} = 252 $$
The prime factorization of 252 is $2^2 \cdot 3^2 \cdot 7^1$. The exponents of 2 and 3 are $\ge 2$, meaning it is divisible by $4$ and $9$. It is not squarefree.
Using Kummer's Theorem for $p=2$: The number 5 in base 2 is $101_2$.
$$ \begin{array}{r@{\quad}l} 101_2 \\[-1ex] {}+ 101_2 \\ \hline 1010_2 \end{array} $$
- Adding the ones digit ($1+1=10_2$) generates **1 carry**.
- The twos digit computes $0+0+1 = 1_2$ (no carry).
- Adding the fours digit ($1+1=10_2$) generates **1 carry**.

There is a total of 2 carries. Therefore, $v_2\left(\binom{10}{5}\right) = 2$. Consequently, $2^2 \mid 252$, physically demonstrating the mathematical mechanism that breaks squarefreeness for $n > 4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*