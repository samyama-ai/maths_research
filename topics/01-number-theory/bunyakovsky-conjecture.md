---
id: 01-number-theory/bunyakovsky-conjecture
title: "Bunyakovsky Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bunyakovsky Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/bunyakovsky-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Bunyakovsky Conjecture asserts that an irreducible polynomial $f(x)$ with integer coefficients will generate infinitely many prime numbers as $x$ takes on positive integer values, provided it satisfies three necessary conditions. Specifically, for a polynomial $f(x)$ in one variable to yield infinitely many primes:
1. Its leading coefficient must be positive.
2. It must be irreducible over the rational numbers.
3. The sequence of values $f(1), f(2), f(3), \dots$ must have no common prime factor (i.e., their greatest common divisor must be 1).

A complete proof of this conjecture would resolve precisely when a single-variable polynomial can generate infinitely many primes. Currently, the conjecture is strictly proven only for polynomials of degree 1. To resolve the conjecture, one must either prove it for all qualifying polynomials of degree $\ge 2$, or find a single counterexample that satisfies the three conditions but yields only a finite number of primes.

## 2. Mathematical Foundations

Let $f \in \mathbb{Z}[x]$ be a polynomial of degree $d \ge 1$:
$$f(x) = a_d x^d + a_{d-1} x^{d-1} + \dots + a_1 x + a_0$$
where $a_i \in \mathbb{Z}$ for all $i$, and $a_d \neq 0$.

The **fixed divisor** of $f$, denoted $d(f)$, is the greatest common divisor of all integer values produced by the polynomial:
$$d(f) = \gcd(\{ f(n) \mid n \in \mathbb{Z} \})$$
(Equivalently, this can be evaluated over $n \in \mathbb{N}$). 

Bunyakovsky's three necessary conditions can be formally stated as:
1. $a_d > 0$
2. $f(x)$ is irreducible in $\mathbb{Z}[x]$ (which, by Gauss's Lemma, is equivalent to irreducibility in $\mathbb{Q}[x]$ given condition 3).
3. $d(f) = 1$.

If all three conditions hold, the conjecture states that the prime counting function for the polynomial, $\pi_f(x) = \\# \{ n \le x \mid f(n) \text{ is prime} \}$, satisfies:
$$\limsup_{x \to \infty} \pi_f(x) = \infty$$

The **Bateman-Horn conjecture** extends this by predicting a quantitative asymptotic density:
$$\pi_f(x) \sim \frac{C(f)}{d} \int_2^x \frac{dt}{\ln t}$$
where $C(f)$ is a heavily studied infinite product over all primes $p$, defined by:
$$C(f) = \prod_{p \text{ prime}} \left( 1 - \frac{1}{p} \right)^{-1} \left( 1 - \frac{\omega_f(p)}{p} \right)$$
with $\omega_f(p)$ representing the number of solutions to the congruence $f(n) \equiv 0 \pmod p$.

## 3. History & State of the Art (SOTA)

- **1837 (Precursor):** Dirichlet proved his theorem on arithmetic progressions, essentially solving the degree 1 case of the conjecture.
- **1857:** The Russian mathematician Viktor Bunyakovsky explicitly formulated the conjecture for polynomials of arbitrary degree.
- **1904:** L. E. Dickson proposed "Dickson's conjecture" for systems of linear polynomials, generalizing Dirichlet's theorem.
- **1958:** Andrzej Schinzel and Wacław Sierpiński generalized the Bunyakovsky conjecture to systems of polynomials of arbitrary degree, yielding "Schinzel's Hypothesis H."
- **1962:** Paul T. Bateman and Roger A. Horn proposed a quantitative version of Schinzel's Hypothesis H (the Bateman-Horn conjecture), yielding precise heuristic asymptotics.
- **1978:** Henryk Iwaniec proved that $n^2 + 1$ produces infinitely many $P_2$ numbers (numbers with at most two prime factors).
- **1998 & 2001:** While univariate polynomials remained unsolved, breakthrough SOTA methods proved that certain sparse multivariable polynomials capture infinitely many primes, notably $x^2 + y^4$ (Friedlander and Iwaniec, 1998) and $x^3 + 2y^3$ (Heath-Brown, 2001).

For univariate polynomials of degree $\ge 2$, the conjecture remains unproven. The most famous special case is Landau's fourth problem (presented in 1912), asking if $n^2 + 1$ produces infinitely many primes.

## 4. Partial Results / Verified Cases

- **Degree $d=1$:** Fully solved. For $f(x) = ax+b$, the fixed divisor condition $d(f)=1$ simplifies to $\gcd(a,b)=1$. Dirichlet's Theorem on Arithmetic Progressions guarantees that such linear sequences capture infinitely many primes.
- **Almost Primes:** It is a verified theorem that for any irreducible $f \in \mathbb{Z}[x]$ with $d(f)=1$, $f(n)$ takes on infinitely many values that are "almost primes". Specifically, for $f(n) = n^2 + 1$, Iwaniec proved in 1978 that it captures infinitely many $P_2$ numbers (integers that are either prime or the product of exactly two primes).
- **Multivariable Analogues:** While outside the strict single-variable definition of Bunyakovsky's conjecture, modern sieve theory has successfully captured primes in higher-degree polynomials by introducing additional variables. The Friedlander–Iwaniec theorem states that the polynomial $x^2 + y^4$ yields infinitely many primes. 

## 5. Principal Obstacles

The primary theoretical obstacle is the **"parity problem"** in sieve theory, famously identified and formalized by Atle Selberg. 

Traditional sieve methods (such as the Selberg sieve or the combinatorial sieve) are excellent at isolating numbers with a small number of prime factors. However, standard sieves cannot distinguish between integers that have an even number of prime factors and those that have an odd number of prime factors. Because a prime number has exactly one prime factor (an odd amount), a sieve bounded by the parity problem cannot definitively isolate primes from integers with two prime factors (like $p_1 p_2$). 

Breaking the parity barrier typically requires injecting deep bilinear form estimates for the error terms into the sieve. This has been achieved for multivariable polynomials (like $x^2 + y^4$) because the extra variables provide algebraic flexibility and sufficient density to estimate these error terms. A univariate polynomial of degree 2, like $n^2 + 1$, is too "rigid" and sparse: the sequence of values grows too fast ($O(\sqrt{x})$ numbers up to $x$), and the roots modulo $p$ do not provide enough flexibility for current bilinear and analytic bounds to overcome the parity barrier.

## 6. The Gap

The mathematical gap lies strictly between polynomials of degree 1 (linear arithmetic progressions) and degree 2 (quadratics). 

We have proven that $n^2+1$ generates infinitely many $P_2$ numbers, but stepping from $P_2$ to $P_1$ (true primes) requires bypassing the parity problem for an extremely sparse sequence. Dirichlet's theorem applies to sequences of density $O(x)$. Bridging the gap from a density of $O(x)$ down to $O(x^{1/d})$ (for degree $d$) in a single variable without introducing a second variable to smooth out the distribution is the fundamental mathematical barrier that must be crossed.

## 7. Current Research (as of June 2026)

Active research aiming toward the Bunyakovsky conjecture operates on several fronts:
1. **Sieve Theory Innovations:** Building on the breakthroughs of Maynard and Tao regarding prime gaps, researchers are continuously attempting to construct parity-sensitive sieves that can operate on sparser sequences. 
2. **Heuristics and Asymptotics:** Refining the error terms in the Bateman-Horn conjecture and studying the statistical distribution of roots of polynomials modulo primes.
3. *(frontier — verify)* **Higher-order Fourier Analysis and Nilsequences:** Techniques originally developed by Green, Tao, and Ziegler to find linear patterns in primes are being investigated to see if nilsequence distributions can provide the necessary orthogonality to break the parity barrier for nonlinear polynomial evaluations.

## 8. Future Work

Leading analytic number theorists suggest that resolving the degree 2 case (such as $n^2+1$) will likely require an entirely new theoretical framework outside of standard sieve theory. Suggested pathways include:
- Developing a deeply modified sieve that incorporates heavy machinery from algebraic geometry, automorphic forms, or elliptic curves to bound the bilinear error terms in sparse sequences.
- Exploring function field analogues (e.g., polynomials over finite fields $\mathbb{F}_q[t]$), where variations of the Bunyakovsky conjecture are sometimes more tractable, and attempting to translate those structural insights back to $\mathbb{Z}[x]$.

## 9. Key References

- **[Foundational]** V. Bouniakowsky. *Nouveaux théorèmes relatifs à la distinction des nombres premiers et à la décomposition des entiers en facteurs.* Mémoires de l'Académie Impériale des Sciences de St.-Pétersbourg, 1857.
- **[Foundational]** P. T. Bateman and R. A. Horn. *A heuristic asymptotic formula concerning the distribution of prime numbers.* Mathematics of Computation, 1962. [DOI](https://doi.org/10.1090/s0025-5718-1962-0148632-7)
- **[SOTA / Recent]** H. Iwaniec. *Almost-primes represented by quadratic polynomials.* Inventiones mathematicae, 1978. [DOI](https://doi.org/10.1007/bf01578070)
- **[SOTA / Recent]** J. Friedlander and H. Iwaniec. *The polynomial $X^2 + Y^4$ captures its primes.* Annals of Mathematics, 1998. [DOI](https://doi.org/10.2307/121034)
- **[Survey]** P. Ribenboim. *The Little Book of Bigger Primes.* Springer-Verlag, 2004. [DOI](https://doi.org/10.1007/b97621)

## 10. Worked Example / Concrete Special Case

Consider the simplest non-linear case of the conjecture, formalized as Landau's fourth problem. Let $f(x) = x^2 + 1$. We verify if it satisfies Bunyakovsky's three conditions:

1. **Positive Leading Coefficient:** The polynomial can be written as $1 \cdot x^2 + 0 \cdot x + 1$. The leading coefficient is $1$, which is strictly greater than $0$.
2. **Irreducibility:** The polynomial $x^2 + 1$ has no real roots (its roots are $\pm i$). Therefore, it cannot be factored into two linear polynomials with real (and thus rational) coefficients. It is irreducible over $\mathbb{Q}[x]$ and $\mathbb{Z}[x]$.
3. **No Fixed Prime Divisor:** We evaluate the first few values of $f(n)$ for $n \ge 1$:
   - $f(1) = 1^2 + 1 = 2$
   - $f(2) = 2^2 + 1 = 5$
   - $f(3) = 3^2 + 1 = 10$
   
   The set of values begins with $\{2, 5, 10, \dots\}$. The greatest common divisor of the first two values is $\gcd(2, 5) = 1$. Since the $\gcd$ of the entire infinite set of values must divide the $\gcd$ of any of its subsets, the fixed divisor $d(f)$ must be $1$.

Since all three conditions are satisfied, the Bunyakovsky conjecture predicts that $f(x) = x^2 + 1$ will generate infinitely many primes. Empirically, it is easy to find them for small values:
- $x = 1 \implies 2$ (Prime)
- $x = 2 \implies 5$ (Prime)
- $x = 4 \implies 17$ (Prime)
- $x = 6 \implies 37$ (Prime)
- $x = 10 \implies 101$ (Prime)

Despite the ease of finding prime values computationally and overwhelming heuristic support via the Bateman-Horn conjecture, proving that this sequence will indefinitely produce primes remains one of the greatest open problems in modern mathematics.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*