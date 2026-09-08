---
id: 01-number-theory/normal-number-property-of-pi
title: "Normal Number Property of Pi"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Normal Number Property of Pi

> **Topic:** Number Theory · **ID:** `01-number-theory/normal-number-property-of-pi` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture states that the mathematical constant $\pi$ is an *absolutely normal number*. Specifically, it is conjectured that for any integer base $b \ge 2$, the sequence of digits in the base-$b$ expansion of $\pi$ is uniformly distributed. This means that every finite sequence of $k$ digits in base $b$ appears in the expansion of $\pi$ with an asymptotic frequency of $b^{-k}$.

A complete proof would require a rigorous demonstration that for every base $b \ge 2$, the limit of the frequency of any length-$k$ block of digits, as the total number of digits goes to infinity, is exactly $b^{-k}$. A disproof would require demonstrating that for at least one base $b \ge 2$ and at least one sequence of digits, the asymptotic frequency deviates from $b^{-k}$, or that the limit does not exist.

## 2. Mathematical Foundations

Let $x$ be a real number. For an integer base $b \ge 2$, the fractional part of $x$ can be expressed as:
$$ x - \lfloor x \rfloor = \sum_{n=1}^{\infty} \frac{d_n}{b^n} $$
where $d_n \in \{0, 1, \dots, b-1\}$.

Let $S$ be a finite sequence (or string) of length $k$ consisting of digits from $\{0, 1, \dots, b-1\}$. Let $N(S, m)$ denote the number of times the sequence $S$ appears as a contiguous sub-block in the first $m$ digits of the base-$b$ expansion of $x$.

A real number $x$ is said to be **simply normal** to base $b$ if, for every digit $d \in \{0, 1, \dots, b-1\}$:
$$ \lim_{m \to \infty} \frac{N(d, m)}{m} = \frac{1}{b} $$

A real number $x$ is said to be **normal** to base $b$ if, for every integer $k \ge 1$ and every sequence $S$ of length $k$:
$$ \lim_{m \to \infty} \frac{N(S, m)}{m} = \frac{1}{b^k} $$

Equivalently, Émile Borel's definition using Weyl's criterion states that $x$ is normal to base $b$ if and only if the sequence $(b^n x)_{n=1}^{\infty}$ is uniformly distributed modulo 1. This means that for every non-zero integer $h$:
$$ \lim_{N \to \infty} \frac{1}{N} \sum_{n=1}^{N} e^{2\pi i h b^n x} = 0 $$

A number is **absolutely normal** if it is normal to every integer base $b \ge 2$. The conjecture asserts that $\pi$ is absolutely normal.

## 3. History & State of the Art (SOTA)

In 1909, Émile Borel introduced the concept of normal numbers and proved via measure theory that Lebesgue-almost all real numbers are absolutely normal. However, constructing explicit examples of normal numbers proved incredibly difficult. The first artificial example was given by Wacław Sierpiński in 1917, and later, easily computable but contrived ones like Champernowne's constant ($0.123456789101112\dots$) were proven normal in base 10.

Despite knowing that nearly all numbers are normal, for fundamental mathematical constants like $\pi$, $e$, $\sqrt{2}$, and $\ln 2$, there is no proof of normality to *any* base.

Computationally, the normality of $\pi$ has been tested extensively. With the advent of modern computing, $\pi$ has been calculated to over 105 trillion digits in base 10 (as of recent 2024 computing milestones). Statistical tests on these digits consistently fail to reject the null hypothesis of uniformity, strongly supporting the conjecture empirically.

In 2001, David Bailey and Richard Crandall established a major theoretical connection between the normality of constants (specifically in base 16 for $\pi$) and the behavior of certain dynamical systems. They showed that the base-16 normality of $\pi$ logically follows from a specific, highly plausible hypothesis about the uniform distribution of orbits in chaotic discrete dynamical systems, originating from the BBP formula.

## 4. Partial Results / Verified Cases

There are zero mathematically verified cases of normality for $\pi$ in *any* integer base $b$. 

We do not even know if $\pi$ is simply normal to base 10 (i.e., whether each digit 0-9 appears with exactly a 1/10 frequency). In fact, it remains unproven whether any specific digit (e.g., '7') appears infinitely often in the base-10 expansion of $\pi$. (It is trivially known that at least two distinct digits must appear infinitely often, otherwise $\pi$ would be rational).

Computationally, verification is strictly empirical. Statistical evaluations have confirmed the uniform distribution of sequences of digits up to length $k=1, 2, \dots$ for the first $10^{14}$ digits in base 10 and base 16, showing extremely tight adherence to expected $b^{-k}$ frequencies.

## 5. Principal Obstacles

The principal obstacle is the profound lack of a mathematical link between the macroscopic/analytic definition of $\pi$ (e.g., $\pi = \int_{-1}^1 \frac{dx}{\sqrt{1-x^2}}$ or $\pi = 4 \sum_{k=0}^\infty \frac{(-1)^k}{2k+1}$) and the microscopic, base-dependent structure of its digit expansion.

The BBP (Bailey-Borwein-Plouffe) formula, $\pi = \sum_{k=0}^{\infty} \frac{1}{16^k} \left( \frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6} \right)$, allows for the extraction of the $n$-th hexadecimal digit of $\pi$ without calculating preceding digits. However, proving the distribution of these digits requires evaluating sequences governed by $\sum_{k=1}^N 16^k \pi \pmod 1$, which behave like pseudo-random walks.

Current mathematical techniques (including traditional Fourier analysis, perturbation theory, and algebraic number theory) lack the tools to definitively bound the discrepancy of sequences defined by evaluating rational functions modulo 1. There is no existing framework to prove that specific, non-artificial transcendental numbers act as perfect pseudo-random number generators. 

## 6. The Gap

The gap is absolute. The boundary lies strictly between immense computational empirical evidence (trillions of digits tested with standard statistical suites) and a theoretical vacuum (0% proof for any base). The exact mathematical barrier that needs to be crossed is proving the equidistribution modulo 1 of orbits generated by specific recurrence relations derived from series expansions. Moving from "computationally indistinguishable from random" to "provably asymptotically uniform" requires a paradigm shift, likely crossing ergodic theory with Diophantine approximation.

## 7. Current Research (as of June 2026)

Active research on the normality of $\pi$ is pursued by computational number theorists and dynamicists across three main avenues:
1. **Algorithmic Verification:** Extending the digit calculation records and passing them through increasingly rigorous randomness tests (like the Diehard or NIST statistical test suites) to hunt for microscopic, long-range biases.
2. **Bailey-Crandall Dynamics:** Researchers are deeply investigating the Bailey-Crandall hypothesis, trying to prove that the orbit of $x_n = \{16 x_{n-1} + r_n\} \pmod 1$ (where $r_n$ are the rational terms of the BBP series) is strictly equidistributed in the interval $[0, 1)$.
3. **Complexity & Diophantine Approximation:** Seeking bounds on irrationality measures, discrepancy, and block complexity. While weaker than absolute normality, proving that the block complexity function $p(k, \pi, b)$ is maximal (meaning every finite sequence appears at least once) is a major stepping stone.

*(frontier — verify)* Recent preprints in measurable dynamics and $p$-adic analysis attempt to provide conditional proofs of simple normality for restricted classes of periods and transcendental numbers, though extending these methods to $\pi$ unconditionally remains a severe bottleneck.

## 8. Future Work

Open pathways and suggested research strategies include:
- **Proving the Bailey-Crandall Hypothesis:** Establishing that the pseudo-random walks generated by BBP-type series are uniformly distributed, which would immediately prove base-16 normality for $\pi$.
- **Establishing Maximal Complexity:** Before proving exact asymptotic frequencies, proving that the digit sequence of $\pi$ contains every possible finite string of digits in base 10 at least once (i.e., $\pi$ is a disjunctive number).
- **Finding any normal fundamental constant:** Proving that *any* naturally occurring transcendental constant (e.g., $e$, $\ln 2$, $\zeta(3)$) is normal to *any* base would represent a massive breakthrough and provide a template for attacking $\pi$.

## 9. Key References

- **[Foundational]** Borel, É. *Les probabilités dénombrables et leurs applications arithmétiques.* Rendiconti del Circolo Matematico di Palermo, 1909. [DOI](https://doi.org/10.1007/bf03019651)
- **[Foundational]** Bailey, D. H., Borwein, P. B., and Plouffe, S. *On the Rapid Computation of Various Polylogarithmic Constants.* Mathematics of Computation, 1997. [DOI](https://doi.org/10.1090/s0025-5718-97-00856-9)
- **[SOTA / Recent]** Bailey, D. H., and Crandall, R. E. *On the Random Character of Fundamental Constant Expansions.* Experimental Mathematics, 2001. [DOI](https://doi.org/10.1080/10586458.2001.10504441)
- **[Survey]** Bugeaud, Y. *Distribution modulo one and Diophantine approximation.* Cambridge Tracts in Mathematics, Cambridge University Press, 2012.

## 10. Worked Example / Concrete Special Case

While we cannot prove asymptotic normality, we can illustrate what *simple normality* means for $\pi$ in base 10 by examining its first few digits and observing the statistical mechanics.

Let the base $b=10$. The decimal expansion of $\pi$ begins:
$3.14159265358979323846\dots$

Let's look at the sequence of the first $m=20$ digits after the decimal point:
$S_{20} = (1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6)$

We calculate the empirical frequency of the digit $d=5$:
The digit 5 appears at positions 4, 8, and 10.
So, $N(5, 20) = 3$.
The observed frequency is $f_5 = \frac{3}{20} = 0.15$.

If $\pi$ is simply normal in base 10, then as $m \to \infty$, the frequency $f_d = \frac{N(d, m)}{m}$ must converge to $\frac{1}{10} = 0.10$ for all digits $d \in \{0, \dots, 9\}$. 

If we computationally scale this up to $m = 10^{11}$ (one hundred billion digits), the counted occurrences for the digit '5' are $10,000,022,501$. The frequency is:
$$ f_5 = \frac{10,000,022,501}{100,000,000,000} \approx 0.100000225 $$

This perfectly aligns with the expectation for a normal number. The defining challenge of the conjecture is rigorously proving that $\lim_{m\to\infty} \frac{N(d, m)}{m} = 0.1$ holds unconditionally and infinitely, rather than just observing it empirically over truncated finite sets.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*