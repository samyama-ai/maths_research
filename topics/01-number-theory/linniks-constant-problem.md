---
id: 01-number-theory/linniks-constant-problem
title: "Linnik's Constant Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Linnik's Constant Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/linniks-constant-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $a$ and $d$ be coprime positive integers with $1 \le a < d$. By Dirichlet's Theorem on arithmetic progressions, the sequence $a, a+d, a+2d, a+3d, \dots$ contains infinitely many prime numbers. Let $p(a,d)$ denote the least prime in this arithmetic progression.

Linnik's Theorem states that there exist absolute constants $c > 0$ and $L > 0$ such that for all valid pairs $(a, d)$:
$$ p(a,d) \le c d^L $$

*Linnik's Constant* is defined as the infimum of all permissible values for $L$. The open problem is to determine the exact value of this infimum. The central **Linnik's Conjecture** asserts that $L = 2$ is permissible. That is, for any $\epsilon > 0$, we have:
$$ p(a,d) \ll_\epsilon d^{2+\epsilon} $$
A stronger version (sometimes known as Schinzel's conjecture on primes in progressions) posits that $p(a,d) < d^2$ for all sufficiently large $d$.

## 2. Mathematical Foundations

The distribution of primes in arithmetic progressions is fundamentally governed by Dirichlet characters and their associated $L$-functions.

Let $\chi$ be a Dirichlet character modulo $d$. The Dirichlet $L$-function is defined for $\Re(s) > 1$ by:
$$ L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} $$
By analytic continuation, $L(s, \chi)$ extends to a meromorphic function on the entire complex plane. The distribution of primes $p \equiv a \pmod d$ is analyzed via the Chebyshev function:
$$ \psi(x; d, a) = \sum_{\substack{n \le x \\ n \equiv a \pmod d}} \Lambda(n) $$
where $\Lambda(n)$ is the von Mangoldt function. The truncated explicit formula links $\psi(x; d, a)$ to the non-trivial zeros $\rho = \beta + i\gamma$ of the $L$-functions $L(s, \chi)$:
$$ \psi(x; d, a) = \frac{x}{\phi(d)} - \frac{1}{\phi(d)} \sum_{\chi \pmod d} \bar{\chi}(a) \sum_{|\gamma| \le T} \frac{x^\rho}{\rho} + O\left(\frac{x \log^2(dx)}{T}\right) $$
To prove $p(a,d) \le c d^L$, one must show that $\psi(x; d, a) > 0$ for $x \ge c d^L$. This requires proving that the sum over zeros $\rho$ does not completely cancel the main term $\frac{x}{\phi(d)}$.

Linnik's proof rests on two foundational pillars:
1. **Log-Free Zero-Density Estimate:** An upper bound on the number of zeros of all $L(s, \chi)$ modulo $d$ in the rectangle $\sigma \ge \alpha$ and $|t| \le T$, denoted $N(\alpha, T, d)$. One requires a bound of the form $N(\alpha, T, d) \ll (dT)^{C(1-\alpha)}$ for an absolute constant $C$.
2. **The Deuring-Heilbronn Phenomenon:** If a real character $\chi \pmod d$ possesses a "Siegel zero" $\beta_1$ exceptionally close to $s=1$, this zero heavily repels other complex zeros away from the line $\Re(s) = 1$.

## 3. History & State of the Art (SOTA)

- **1944:** Yuri Linnik published two seminal papers proving the existence of $L$, bypassing the Generalized Riemann Hypothesis (GRH) via his zero-density estimates and the Deuring-Heilbronn phenomenon.
- **1957:** Pan Cheng-Dong computed the first explicit bound, showing $L \le 10,000$.
- **1977:** M. Jutila introduced a combination of zero-density estimates and sieve methods to drastically lower the bound to $L \le 80$.
- **1979–1989:** Chen Jingrun iteratively improved the bound, culminating in $L \le 13.5$ in 1989.
- **1992:** D. R. Heath-Brown published a breakthrough paper establishing $L \le 5.5$. He introduced a new identity for the Dirichlet series of $1/\zeta(s)$ and refined Burgess bounds for character sums.
- **2011 (Current SOTA):** Triantafyllos Xylouris, extending Heath-Brown's methodology and optimizing the polynomial coefficients in the mollifier method, achieved the current unconditional record: $L \le 5.18$. 

## 4. Partial Results / Verified Cases

- **Conditional on GRH:** If the Generalized Riemann Hypothesis for Dirichlet $L$-functions holds, then all non-trivial zeros lie on the critical line $\Re(s) = 1/2$. The explicit formula then easily yields $p(a,d) \ll \phi(d)^2 (\log d)^2$. Since $\phi(d) < d$, this confirms the $L=2$ conjecture (with a polylogarithmic factor).
- **Almost All Progressions:** By the Bombieri-Vinogradov theorem, the primes are well-distributed on average. It follows that for any $\epsilon > 0$ and for "almost all" $a$ coprime to $d$, we have $p(a,d) \ll d^{1+\epsilon}$.
- **Computational Verification:** For $d \le 10^5$, empirical searches and prime tables verify that $p(a,d) < d^2$. The constant $c$ in Xylouris’s $d^{5.18}$ bound has also been made explicit for large $d$.

## 5. Principal Obstacles

The fundamental bottleneck to reaching $L=2$ unconditionally is the potential existence of **Siegel zeros**. 

If there exists a real character $\chi_1 \pmod d$ with an exceptional zero $\beta_1 = 1 - \delta$ where $\delta \ll \frac{1}{\log d}$, the explicit formula contains a dominant negative term:
$$ - \frac{\chi_1(a)}{\phi(d)} \frac{x^{\beta_1}}{\beta_1} $$
If $\chi_1(a) = 1$, this term subtracts almost $x / \phi(d)$ from the main term $\frac{x}{\phi(d)}$. To guarantee $\psi(x; d, a) > 0$, $x$ must be large enough so that the difference $\frac{x}{\phi(d)} - \frac{x^{\beta_1}}{\phi(d)}$ overcomes all other error terms. This forces $x \approx d^C$ for some $C > 2$. 

While the Deuring-Heilbronn phenomenon shows that a Siegel zero pushes *other* zeros to the left (reducing the contribution of the rest of the zero sum), the Siegel zero itself exacts a heavy toll. Additionally, even if Siegel zeros do not exist, Heath-Brown's parameter optimization is strictly bottlenecked by the exponent $1/4$ in the Burgess bound for short character sums ($\sum_{n \le N} \chi(n) \ll N^{1 - 1/r} d^{(r+1)/4r^2}$). Without improving the Burgess bound or the log-free density constant $C$, current sieve machinery halts at $L \approx 5$.

## 6. The Gap

The gap is precisely the distance between $O(d^{5.18})$ (Xylouris, 2011) and $O(d^{2+\epsilon})$ (Conjectured). Crossing this gap requires one of two monumental breakthroughs:
1. Proving the non-existence of Siegel zeros, which would immediately eliminate the anomalous main-term cancellation.
2. Developing a fundamentally new zero-density estimate $N(\alpha, T, d)$ that brings the log-free constant $C$ close to $2$, combined with sub-convexity bounds that vastly surpass the Burgess bound for Dirichlet $L$-functions.

Standard analytic number theory techniques (mollification, Vaughan's identity, large sieve) have been heavily optimized, suggesting that purely analytic tweaks to existing formulas will not cross the $L=5$ barrier.

## 7. Current Research (as of June 2026)

- **Optimized Mollifiers:** Research groups continue to computationally optimize the continuous polynomial weights used in the mollification of $L$-functions near $\sigma=1$.
- **Sub-convexity and Burgess Bounds:** Minor improvements to character sum bounds modulo prime powers are being generalized, attempting to bypass the strict $1/4$ Burgess barrier.
- **Sieve Method Interactions:** Researchers are exploring parity-breaking techniques in sieve theory (inspired by the work of Maynard and Tao on prime gaps) to detect primes in short intervals of arithmetic progressions without relying exclusively on the $L$-function explicit formula. *(frontier — verify)*

## 8. Future Work

Leading analytic number theorists point toward the following strategies:
- **Siegel Zero Annihilation:** A proof that $1 - \beta \gg d^{-\epsilon}$ for all real characters would trigger a cascade of optimizations in the sieve parameters, potentially lowering $L$ to $< 3$ instantly.
- **Additive Combinatorics:** Bypassing $L$-functions entirely for certain ranges by using higher-order Fourier analysis (Gowers norms) and additive combinatorics on the von Mangoldt function $\Lambda(n)$. While promising for average results, translating this to worst-case bounds for $p(a,d)$ remains a distant goal.

## 9. Key References

- **[Foundational]** Linnik, U. V. *On the least prime in an arithmetic progression I. The basic theorem*. Rec. Math. (Mat. Sbornik) N.S., 15 (57), 139-178, 1944.
- **[Foundational]** Heath-Brown, D. R. *Zero-free regions for Dirichlet L-functions, and the least prime in an arithmetic progression*. Proc. London Math. Soc., 64 (2): 265-338, 1992.
- **[SOTA / Recent]** Xylouris, T. *On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet L-functions*. Acta Arithmetica, 150 (1): 65-91, 2011.
- **[Survey]** Friedlander, J. B., & Iwaniec, H. *Opera de Cribro*. American Mathematical Society (Colloquium Publications Vol. 57), 2010.

## 10. Worked Example / Concrete Special Case

Consider the modulus $d = 109$ and the coprime shift $a = 10$. 
The arithmetic progression is given by $109k + 10$:
$$ 10, 119, 228, 337, 446, \dots $$
Testing for primality, $10$ is even; $119 = 7 \times 17$; $228$ is even. 
The number $337$ is prime. Therefore, the least prime in this progression is:
$$ p(10, 109) = 337 $$
Linnik's conjecture posits that $p(a,d) \ll d^2$. In our case, $d^2 = 109^2 = 11881$. We clearly observe that $337 \ll 11881$, supporting the $L=2$ bound.

**Analytic Illustration of the Obstacle:**
To guarantee theoretically that a prime exists before $x = 1000$, we analyze the main term of the explicit formula. The expected "weight" of primes up to $1000$ in this progression is roughly:
$$ \frac{x}{\phi(109)} = \frac{1000}{108} \approx 9.259 $$
If, hypothetically, there existed an exceptional real Dirichlet character $\chi \pmod{109}$ with a Siegel zero at $\beta_1 = 0.99$ and $\chi(10) = 1$, the negative contribution of this zero would be:
$$ - \frac{1000^{0.99}}{\phi(109) \cdot 0.99} \approx - \frac{933.25}{108 \cdot 0.99} \approx -8.728 $$
The main term ($9.259$) and the Siegel zero term ($-8.728$) nearly cancel out, leaving a tiny residual value ($0.531$). If other complex zeros happen to align negatively, the sum could dip below zero, meaning the formula cannot mathematically guarantee a prime exists at $x = 1000$. To overcome the hypothetical $-x^{0.99}$ term and guarantee positivity without GRH, $x$ must be pushed much higher relative to $d$ (e.g., to $x = d^5$), illustrating why $L$ is currently stuck at $5.18$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*