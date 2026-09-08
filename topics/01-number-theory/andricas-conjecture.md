---
id: 01-number-theory/andricas-conjecture
title: "Andrica's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Andrica's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/andricas-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Andrica's Conjecture is an unresolved proposition regarding the gaps between consecutive prime numbers. It conjectures that for all $n \ge 1$, the inequality 

$$ \sqrt{p_{n+1}} - \sqrt{p_n} < 1 $$

holds, where $p_n$ denotes the $n$-th prime number. 

Equivalently, by rearranging the terms and squaring both sides, the conjecture states that the gap between consecutive primes, $g_n = p_{n+1} - p_n$, is strictly bounded by:

$$ p_{n+1} < (\sqrt{p_n} + 1)^2 $$
$$ g_n < 2\sqrt{p_n} + 1 $$

A complete proof of this conjecture would establish a very tight, unconditional deterministic upper bound on prime gaps, implying that the distance to the next prime can never exceed roughly twice the square root of the current prime.

## 2. Mathematical Foundations

The problem exists within the domain of multiplicative number theory, specifically focusing on the distribution of prime numbers. Let $\mathbb{P} = \{2, 3, 5, 7, 11, \dots\}$ be the set of primes, with $p_n$ being the $n$-th element. 

The prime gap is defined as the difference between two successive primes:
$$ g_n = p_{n+1} - p_n $$

Andrica's conjecture bridges several prominent mathematical concepts regarding prime distribution:
- **Legendre's Conjecture:** Asserts that for every positive integer $m$, there is at least one prime $p$ such that $m^2 < p < (m+1)^2$. Andrica's conjecture implies Legendre's conjecture. If Andrica's statement holds, then a prime $p_n \le m^2$ would force $p_{n+1} < (\sqrt{m^2} + 1)^2 = (m+1)^2$, ensuring a prime falls in the requisite interval.
- **Oppermann's Conjecture:** A stronger proposition asserting that there is always a prime between $m(m-1)$ and $m^2$, as well as between $m^2$ and $m(m+1)$.
- **Cramér's Conjecture:** Models primes probabilistically to conjecture that $g_n = O(\log^2 p_n)$. Since $\log^2 x = o(\sqrt{x})$, Cramér's conjecture asymptotically implies Andrica's conjecture for sufficiently large $n$.

The function under study is often denoted as $A_n = \sqrt{p_{n+1}} - \sqrt{p_n}$. The conjecture claims that $\sup_{n \in \mathbb{N}} A_n < 1$.

## 3. History & State of the Art (SOTA)

The conjecture was formally proposed by the Romanian mathematician Dorin Andrica in 1986. While questions about bounds on prime gaps have been studied since the mid-19th century—starting with Bertrand's postulate (proven by Chebyshev) and extending to Legendre's unproven claim—Andrica's formulation provided a surprisingly clean algebraic phrasing that is easily verifiable for small primes.

Historically, the search for maximal prime gaps (primes $p_n$ for which $g_n > g_k$ for all $k < n$) has provided empirical backing for the conjecture. Computational efforts to find large prime gaps have consistently found that $g_n$ grows on the order of $\log^2 p_n$, which is vastly smaller than the $2\sqrt{p_n} + 1$ threshold permitted by Andrica.

The state of the art in unconditional theoretical bounds on prime gaps was established in 2001 by Baker, Harman, and Pintz, who proved that:
$$ p_{n+1} - p_n = O(p_n^{0.525}) $$
This remains the sharpest unconditional bound, closing in on, but not reaching, the $\theta = 0.5$ exponent required to prove Andrica's conjecture.

## 4. Partial Results / Verified Cases

Because $A_n = \frac{p_{n+1} - p_n}{\sqrt{p_{n+1}} + \sqrt{p_n}}$, the value of $A_n$ shrinks significantly as $n$ grows, provided $p_{n+1} - p_n$ does not grow exceptionally fast. 

1. **Computational Verification:** 
   Extensive computational searches for maximal prime gaps by mathematicians such as Tomas Oliveira e Silva, Siegfried Herzog, and Silvio Pardi have verified prime gaps up to $4 \times 10^{18}$. Over this entire range, $A_n$ remains strictly less than 1.
   
2. **The Maximum Value:**
   Empirical data strongly suggests that the absolute maximum of the sequence $A_n$ occurs very early, specifically at $n=4$, where $p_4 = 7$ and $p_5 = 11$. 
   $$ A_4 = \sqrt{11} - \sqrt{7} \approx 0.670873 $$
   For all other verified $n$, $A_n$ falls below this peak, asymptoting toward 0 as $n \to \infty$.

3. **Asymptotic Dominance:**
   Under the assumption of the Riemann Hypothesis (RH), the error term in the Prime Number Theorem guarantees that $g_n = O(\sqrt{p_n} \log p_n)$. This conditional result narrowly misses Andrica's bound by a logarithmic factor.

## 5. Principal Obstacles

The fundamental barrier to proving Andrica's conjecture lies in the limitations of current analytic number theory techniques—specifically, sieve methods and bounds on Dirichlet polynomials.

To prove Andrica's conjecture, one must establish unconditionally that $g_n = O(p_n^{0.5})$. However, modern sieve theory experiences a structural limitation known as the "parity problem," which prevents sieves alone from distinguishing between integers with an even or odd number of prime factors. 

Furthermore, even if the Riemann Hypothesis were proven tomorrow, it would only yield $g_n = O(\sqrt{p_n} \log p_n)$. The extra $\log p_n$ factor arises from the density of the non-trivial zeroes of the Riemann zeta function $\zeta(s)$ on the critical line. To strip away this logarithmic factor and reach $O(\sqrt{p_n})$, one would need extraordinarily precise control over the *pair correlation* of the zeroes of the zeta function (e.g., proving Montgomery's Pair Correlation Conjecture) or establishing deep bounds in random matrix theory beyond the generalized Riemann Hypothesis.

## 6. The Gap

The exact mathematical barrier is the gap between the known unconditional exponent of $\theta = 0.525$ (or the conditional bound $\theta = 0.5$ with a log-penalty under RH) and the strict bound of $2\sqrt{p_n} + 1$. 

To cross this boundary, mathematicians must rule out the existence of "exceptionally large" prime-free intervals (intervals of size $\ge 2\sqrt{x}$ containing no primes) that might theoretically be caused by a pathological conspiracy in the distribution of the zeroes of the Riemann zeta function. Proving the conjecture requires either a completely novel, non-analytic approach to prime distances or a revolutionary breakthrough in bounding the error term of the explicit formula for $\psi(x)$.

## 7. Current Research (as of June 2026)

Current research generally bypasses direct attacks on Andrica's conjecture, focusing instead on asymptotic and probabilistic bounds on prime gaps. 
- **Improving the Exponent:** Research continues incrementally to lower the exponent in $p_{n+1} - p_n \ll p_n^{\theta}$ below $0.525$.
- **Maynard-Tao Sieve:** The breakthrough work on small gaps between primes (and bounded gaps) by James Maynard and Terence Tao provides powerful structural insights into the clustering of primes, though it does not directly yield deterministic upper bounds on maximal gaps.
- **Generalized Andrica Conjectures:** Some analytic number theorists study the Smarandache-Andrica generalization $p_{n+1}^x - p_n^x < 1$, attempting to determine the exact supremal value of $x$ for which the inequality holds. *(frontier — verify)*

## 8. Future Work

Leading researchers suggest that the path toward proving Andrica's conjecture lies in validating Cramér's conjecture ($g_n \ll \log^2 p_n$) via probabilistic models of prime distribution. If Cramér's bound holds, Andrica's conjecture is trivially satisfied for all sufficiently large $n$. The finite number of cases below the asymptotic threshold could then be resolved computationally.

Future work in bounding Dirichlet polynomials and extending the large sieve inequality is required to push the theoretical barrier of $\theta = 0.525$ closer to the $0.5$ threshold, serving as a stepping stone toward ruling out the anomalous gaps that currently keep the conjecture unproven.

## 9. Key References

- **[Foundational]** Andrica, D. *Note on a conjecture in prime number theory.* Studia Universitatis Babes-Bolyai Mathematica, 31(4): 44-48, 1986.
- **[SOTA / Recent]** Baker, R. C., Harman, G., and Pintz, J. *The difference between consecutive primes, II.* Proceedings of the London Mathematical Society, 83(3): 532-562, 2001. [DOI](https://doi.org/10.1112/plms/83.3.532)
- **[Survey]** Oliveira e Silva, T., Herzog, S., and Pardi, S. *Empirical verification of the even Goldbach conjecture and computation of prime gaps up to $4 \cdot 10^{18}$.* Mathematics of Computation, 83(288): 2033-2060, 2014.
- **[Foundational]** Guy, R. K. *Unsolved Problems in Number Theory (3rd ed.).* Springer-Verlag, Section A8, 2004. [DOI](https://doi.org/10.1017/s0025557200178817)

## 10. Worked Example / Concrete Special Case

To understand the conjecture concretely, we can calculate the value of $A_n = \sqrt{p_{n+1}} - \sqrt{p_n}$ for a few small, consecutive primes to see how the bound of $1$ holds.

**Case 1: The earliest primes ($n=1$)**
Let $p_1 = 2$ and $p_2 = 3$.
$$ A_1 = \sqrt{3} - \sqrt{2} \approx 1.73205 - 1.41421 = 0.31784 $$
Here, $0.31784 < 1$, so the conjecture holds.

**Case 2: The suspected absolute maximum ($n=4$)**
Let $p_4 = 7$ and $p_5 = 11$.
$$ A_4 = \sqrt{11} - \sqrt{7} \approx 3.31662 - 2.64575 = 0.67087 $$
Here, $0.67087 < 1$. This is the largest value of $A_n$ ever observed.

**Case 3: A larger prime gap**
Consider the prime $p_{30} = 113$. The next prime is $p_{31} = 127$. This represents a relatively large prime gap of $g_{30} = 14$.
$$ A_{30} = \sqrt{127} - \sqrt{113} \approx 11.26942 - 10.63014 = 0.63928 $$
Despite the gap of 14, the difference between their square roots is still comfortably below 1. As $n$ gets very large, the difference $\sqrt{p_{n+1}} - \sqrt{p_n}$ shrinks steadily toward zero, making the conjecture overwhelmingly likely to be true, even though an analytic proof remains elusive.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*