---
id: 05-analysis/gelfond-conjecture
title: "Gelfond Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 05-analysis/gelfond-conjecture
title: "Gelfond's Sum of Digits Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2024-01
last_reviewed: 2026-06
last_substantive_update: 2026-06
stale_since: ""
provenance: synthesized
```

# Gelfond's Sum of Digits Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/gelfond-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

In 1968, Alexander O. Gelfond formulated three fundamental conjectures concerning the statistical distribution of the sum-of-digits function $s_q(n)$ in an integer base $q \ge 2$. The most prominent parts of the conjecture assert that the sum of digits of values of polynomials with integer coefficients, and the sum of digits of prime numbers, are uniformly distributed in arithmetic progressions.

Specifically, Gelfond conjectured that:

1. **For prime numbers:** Let $m \ge 2$ be an integer. If the coprimality condition $(m, q-1) = 1$ is satisfied, then the number of primes $p \le x$ such that $s_q(p) \equiv a \pmod m$ is asymptotic to $\pi(x)/m$ as $x \to \infty$. 
2. **For polynomials:** Let $P(x) \in \mathbb{Z}[x]$ be a polynomial of degree $d \ge 2$ such that $P(\mathbb{N}) \subset \mathbb{N}$. If $(m, q-1) = 1$, the number of integers $n \le x$ such that $s_q(P(n)) \equiv a \pmod m$ is asymptotic to $x/m$ as $x \to \infty$.
3. **For coprime bases:** If $q_1, \dots, q_k$ are pairwise coprime bases, and $m_1, \dots, m_k$ satisfy $(m_i, q_i - 1) = 1$, then the joint distribution of the congruences $s_{q_i}(n) \equiv a_i \pmod{m_i}$ is asymptotically uniform; meaning the proportion of such integers $n \le x$ approaches $\prod_{i=1}^k (1/m_i)$.

A complete proof required demonstrating that the rigid, additive, fractal-like structure of base-$q$ numeration is statistically orthogonal to the multiplicative sieve structures defining primes and polynomial factorizations.

## 2. Mathematical Foundations

Define $\mathbb{N}$ as the set of non-negative integers. For a fixed integer base $q \ge 2$, every $n \in \mathbb{N}$ admits a unique finite $q$-ary expansion:
$$ n = \sum_{k=0}^{\infty} d_k(n) q^k $$
where the digits satisfy $d_k(n) \in \{0, 1, \dots, q-1\}$ and $d_k(n) = 0$ for all sufficiently large $k$. The sum-of-digits function $s_q : \mathbb{N} \to \mathbb{N}$ is defined as:
$$ s_q(n) = \sum_{k=0}^{\infty} d_k(n) $$

The function $s_q$ is strictly $q$-additive, meaning it satisfies $s_q(a q^k + b) = s_q(a) + s_q(b)$ for any non-negative integers $a, b, k$ where $0 \le b < q^k$. 

To study the distribution of $s_q(n)$ modulo $m$, one employs discrete harmonic analysis, converting the counting problem into the estimation of exponential sums. Let $e(x) = \exp(2\pi i x)$. The indicator function for the congruence class $s_q(n) \equiv a \pmod m$ is given by the discrete Fourier transform:
$$ \frac{1}{m} \sum_{j=0}^{m-1} e\left(\frac{j(s_q(n) - a)}{m}\right) $$

Consequently, proving Gelfond's conjecture for primes reduces to establishing non-trivial bounds on the corresponding Weyl-type exponential sums. Specifically, one must prove that for any integer $j$ not divisible by $m$,
$$ \sum_{p \le x} e\left(\frac{j \cdot s_q(p)}{m}\right) = o(\pi(x)) $$
Equivalently, using the von Mangoldt function $\Lambda(n)$, one must show:
$$ \sum_{n \le x} \Lambda(n) e(\alpha s_q(n)) = o(x) $$
where $\alpha = j/m \in (0, 1)$. For polynomials, the analogous analytic requirement is bounding:
$$ \sum_{n \le x} e(\alpha s_q(P(n))) = o(x) $$

## 3. History & State of the Art (SOTA)

Gelfond introduced these conjectures in his foundational 1968 paper, *Sur les nombres qui ont des propriétés additives et multiplicatives données*. In that same paper, he proved the base cases for linear polynomials $P(n) = cn + d$ and laid the groundwork for analyzing $q$-additive functions via exponential sums.

The conjectures remained an immovable obstacle in analytic number theory for forty years because they necessitated bridging the gap between the multiplicative theory of integers and the arithmetic geometry of digits.
- **Coprime Bases:** Conjecture 3 was solved by J. Bésineau in 1972 using generalized Bohr almost-periodicity, with quantitative error terms provided by D.-J. Kim in 1999.
- **Polynomials (Squares):** The first monumental breakthrough on the non-linear conjectures occurred in 2009, when Christian Mauduit and Joël Rivat proved the case for squares ($P(n) = n^2$). This was published in *Acta Mathematica*.
- **Primes:** In 2010, Mauduit and Rivat achieved the crowning result by entirely resolving the conjecture for prime numbers, published in the *Annals of Mathematics*.
- **General Polynomials:** In 2012, Michael Drmota, alongside Mauduit and Rivat, generalized the polynomial result to apply to any integer polynomial $P(x)$ of arbitrary degree, fully resolving Conjecture 2 (*Journal of the European Mathematical Society*).

These breakthroughs represent the absolute state of the art in combining the Hardy-Littlewood circle method with the harmonic analysis of automatic sequences.

## 4. Partial Results / Verified Cases

Prior to the definitive resolutions by Mauduit, Rivat, and Drmota, several specialized cases and weaker versions of the conjectures were established:
- **Linear Functions:** Gelfond (1968) fully resolved the uniform distribution for $P(n) = cn + d$.
- **Almost Primes:** The sum of digits distribution was proven uniform for numbers with a fixed, small number of prime factors (e.g., $k$-almost primes) via Selberg sieve methods, which are analytically less demanding than detecting strict primes.
- **Carmichael Numbers:** The distribution of the sum of digits of Carmichael numbers was shown to be uniform, serving as an intermediate step toward full primes.
- **Piatetski-Shapiro Sequences:** Uniform distribution of digits was verified for the integer parts of non-integer powers $n^c$ for specific narrow ranges of $c \in (1, 2)$ before the integer polynomial case was solved.

## 5. Principal Obstacles

The fundamental obstacle in Gelfond's conjectures is the total lack of algebraic compatibility between the base-$q$ additive structure and the multiplicative structure of the integers. 

Traditional prime-detecting tools, such as the Prime Number Theorem in arithmetic progressions or Dirichlet $L$-functions, require the target sequence to exhibit multiplicative symmetries or continuous, smooth phases. However, the sequence $s_q(n)$ is a highly erratic, non-differentiable fractal. Its structural self-similarity means that small additive perturbations (like adding 1 to $n$) can trigger catastrophic "carry cascades" that completely rewrite the sum of digits, destroying analytic continuity.

When translating the problem to Fourier analysis, the transform of the $q$-multiplicative function $e(\alpha s_q(n))$ takes the form of an infinite oscillating product:
$$ F_q(\alpha, N) = \prod_{k=0}^{\lfloor \log_q N \rfloor} \left( \frac{1}{q} \sum_{d=0}^{q-1} e(\alpha d q^k) \right) $$
This product does not decay smoothly or uniformly. Classical Weyl differencing—which lowers the degree of a polynomial phase $e(\alpha P(n))$ by shifting and subtracting—fails completely because $s_q(n)$ is not a polynomial; differencing it yields a function that is just as analytically intractable as the original. 

## 6. The Gap

To apply Vinogradov's method to the prime sum $\sum \Lambda(n) e(\alpha s_q(n))$, analytic number theorists use Vaughan's identity to decompose the sum into Type I (linear) and Type II (bilinear) sums. The critical bottleneck lay entirely in bounding the Type II sums, which take the form:
$$ \sum_m \sum_n a_m b_n e(\alpha s_q(mn)) $$
where $a_m$ and $b_n$ are arbitrary bounded weights. For continuous phases, one isolates the variables $m$ and $n$ using Taylor expansions or integration by parts. For $s_q(mn)$, this was impossible because the carries generated by the multiplication $m \times n$ propagate through the base-$q$ expansion unpredictably, irreversibly tangling $m$ and $n$.

The mathematical barrier was crossed by Mauduit and Rivat via the invention of the *carry propagation lemma* and the use of truncated $q$-additive functions. They defined $s_{q, \lambda}(n) = s_q(n \bmod q^\lambda)$, which truncates the sum to only the first $\lambda$ digits. They rigorously proved that for an overwhelmingly large set of integers, the shift difference $s_q(n+r) - s_q(n)$ is identically equal to $s_{q, \lambda}(n+r) - s_{q, \lambda}(n)$. 

This truncation acted as a powerful algebraic smoothing operator. By applying a double large sieve inequality and expressing the truncated digital functions via discrete Fourier transforms on the cyclic group $\mathbb{Z}/q^\lambda\mathbb{Z}$, they successfully decoupled the bilinear variables, achieving the required exponential decay.

## 7. Current Research (as of June 2026)

With the primary conjectures solved, current research centers on multidimensional generalizations, structural bounds, and related sequences:
- **Möbius Disjointness:** Peter Sarnak's conjecture states that the Möbius function $\mu(n)$ is disjoint from zero-entropy dynamical systems. Modulo 2, $e(s_2(n)/2) = (-1)^{s_2(n)}$, which is the classic Thue-Morse sequence. The fact that $\sum_{n \le x} \mu(n) (-1)^{s_2(n)} = o(x)$ is a direct corollary of the Mauduit-Rivat machinery. Modern research focuses on pushing the error term to a polynomial power saving $O(x^{1-\delta})$. *(frontier — verify)*
- **Zeckendorf Expansions:** Expanding the theorems beyond fixed-integer bases to linear recurrent numeration systems, such as Ostrowski numeration and Zeckendorf (Fibonacci) expansions. Recent work by S. Müllner has successfully imported Type II sum techniques into these non-standard digital frameworks.
- **Missing Digits:** While Gelfond focused on the sum of digits, James Maynard's recent breakthrough on primes with restricted digits (e.g., primes containing no '7' in base 10) utilizes different methods (Markov chains and geometry of numbers). Synthesizing Maynard's geometric sieve with Mauduit and Rivat's harmonic analysis remains highly active.

## 8. Future Work

Leading mathematicians have outlined several immediate pathways to extend the Gelfond framework:
- **Prime Tuples:** Proving that the sum of digits of prime tuples (such as twin primes $p$ and $p+2$) are jointly uniformly distributed.
- **Multidimensional Bases:** Establishing the distribution of $s_q(p)$ evaluated over Gaussian primes in $\mathbb{Z}[i]$, or primes in general number fields subject to complex base expansions.
- **Values of Analytic Functions:** Investigating the digit sums of evaluations of entirely different classes of functions, such as the integer parts of exponential functions $s_q(\lfloor e^{\alpha n} \rfloor)$, which completely evade current carry-propagation lemmas.

## 9. Key References

- **[Foundational]** Gelfond, A. O. *Sur les nombres qui ont des propriétés additives et multiplicatives données.* Acta Arithmetica, 1968. (link if stable)
- **[SOTA / Recent]** Mauduit, C., & Rivat, J. *La somme des chiffres des carrés.* Acta Mathematica, 2009.
- **[SOTA / Recent]** Mauduit, C., & Rivat, J. *Sur les chiffres des nombres premiers.* Annals of Mathematics, 2010.
- **[SOTA / Recent]** Drmota, M., Mauduit, C., & Rivat, J. *The sum-of-digits function of polynomial sequences.* Journal of the European Mathematical Society, 2012.

## 10. Worked Example / Concrete Special Case

To ground the necessity of the conditions in Gelfond's Conjecture, consider the specific case of $q = 3$ and $m = 2$. We examine the coprimality constraint $(m, q-1) = 1$. In this scenario, $(2, 3-1) = (2, 2) = 2 \neq 1$.

Why does the uniform distribution fail when this condition is violated? Observe the algebraic property of the sum of digits in base $q$. Because $q \equiv 1 \pmod{q-1}$, we have $q^k \equiv 1 \pmod{q-1}$ for all integers $k \ge 0$. Therefore, evaluating $n$ modulo $q-1$ gives:
$$ n = \sum_{k=0}^\infty d_k 3^k \equiv \sum_{k=0}^\infty d_k = s_3(n) \pmod 2 $$
Thus, $s_3(n)$ is strictly mathematically forced to share the exact same parity as $n$. If we restrict $n$ to prime numbers $p > 2$, every such prime is odd, meaning $p \equiv 1 \pmod 2$. Consequently, for every prime $p > 2$, its base-3 sum of digits must also be definitively odd:
$$ s_3(p) \equiv p \equiv 1 \pmod 2 $$
In this case, the distribution modulo 2 is completely degenerate: 100% of primes $p > 2$ have an odd sum of digits in base 3, and 0% have an even sum. 

Now, consider the Thue-Morse case: $q = 2$ and $m = 2$. Here, $(m, q-1) = (2, 1) = 1$, so the condition is satisfied and Gelfond's conjecture guarantees a uniform distribution. Let's tally the primes up to $x = 20$:
- $p = 2$: binary $10_2 \implies s_2(2) = 1$ (odd)
- $p = 3$: binary $11_2 \implies s_2(3) = 2$ (even)
- $p = 5$: binary $101_2 \implies s_2(5) = 2$ (even)
- $p = 7$: binary $111_2 \implies s_2(7) = 3$ (odd)
- $p = 11$: binary $1011_2 \implies s_2(11) = 3$ (odd)
- $p = 13$: binary $1101_2 \implies s_2(13) = 3$ (odd)
- $p = 17$: binary $10001_2 \implies s_2(17) = 2$ (even)
- $p = 19$: binary $10011_2 \implies s_2(19) = 3$ (odd)

Out of the 8 primes, 3 have an even sum of digits and 5 have an odd sum. Mauduit and Rivat's 2010 breakthrough rigorously proves that as $x \to \infty$, the deeply hidden harmonic cancellation in $\sum_{p \le x} (-1)^{s_2(p)}$ forces these counts to equalize perfectly, with both subsets asymptotically approaching $\pi(x)/2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*