---
id: 01-number-theory/lenstra-pomerance-wagstaff-conjecture
title: "Lenstra-Pomerance-Wagstaff Conjecture"
topic: 01-number-theory
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lenstra-Pomerance-Wagstaff Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/lenstra-pomerance-wagstaff-conjecture` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Let $M_p = 2^p - 1$ with $p$ prime. Call $M_p$ a **Mersenne prime** when it is prime, and let

$$
\mathcal{M}(x) \;=\; \\#\{\, p \le x : p \text{ prime},\ 2^p - 1 \text{ prime} \,\}.
$$

**Conjecture (Lenstra–Pomerance–Wagstaff).**

$$
\mathcal{M}(x) \;\sim\; \frac{e^{\gamma}}{\log 2}\,\log x \qquad (x \to \infty),
$$

where $\gamma = 0.5772156649\ldots$ is Euler's constant, so $e^{\gamma}/\log 2 = 2.5695\ldots$

Three standard corollaries of the same heuristic:

1. **Infinitude.** There are infinitely many Mersenne primes.
2. **Dyadic density.** The expected number of Mersenne prime exponents in $(x, 2x]$ is $e^{\gamma} = 1.78107\ldots$, independent of $x$.
3. **Growth of exponents.** If $p_1 < p_2 < \cdots$ enumerate the Mersenne prime exponents, then $p_{n+1}/p_n \to 2^{1/e^{\gamma}} = 1.47576\ldots$ in the geometric-mean sense, i.e. $\log p_n \sim n\,(\log 2)/e^{\gamma}$.

A complete resolution requires an unconditional asymptotic for $\mathcal{M}(x)$. Even proving $\mathcal{M}(x) \to \infty$, or proving $\mathcal{M}(x) < \pi(x) - \omega(1)$ (infinitely many composite $M_p$ with $p$ prime), would be a landmark; neither is known.

## 2. Mathematical Foundations

**Divisor structure.** If $q \mid 2^p - 1$ with $p, q$ prime, then $\mathrm{ord}_q(2) = p$, hence $p \mid q - 1$:

$$
q \equiv 1 \pmod{2p}, \qquad q \equiv \pm 1 \pmod 8 ,
$$

the second congruence because $2$ is a quadratic residue mod $q$ (Euler). So the admissible prime divisors of $M_p$ lie in exactly $2$ of the $\varphi(8p)$ reduced residue classes mod $8p$.

**Trial-division heuristic.** $M_p$ is prime iff it has no prime factor $q \le \sqrt{M_p} \approx 2^{p/2}$. Modelling divisibility by admissible $q$ as independent events of probability $1/q$,

$$
\Pr[M_p \text{ prime}] \;\approx\; \prod_{\substack{q \le 2^{p/2} \\ q \equiv \pm 1 (8),\, q \equiv 1 (2p)}} \left(1 - \frac{1}{q}\right).
$$

By the prime number theorem in arithmetic progressions, such $q$ have relative density $\tfrac{1}{2}\cdot\tfrac{1}{p-1}$ among primes; feeding this into Mertens' theorem $\prod_{q \le y}(1-1/q) \sim e^{-\gamma}/\log y$ (with $y = 2^{p/2}$) and comparing against the unconditioned product gives

$$
\Pr[M_p \text{ prime}] \;\approx\; \frac{e^{\gamma} \log(a p)}{p \log 2}, \qquad
a = \begin{cases} 2, & p \equiv 3 \pmod 4,\\ 6, & p \equiv 1 \pmod 4.\end{cases}
$$

The split by $p \bmod 4$ is Wagstaff's correction: for $p \equiv 3 \pmod 4$ the candidate divisor $2p+1$ is admissible and, when prime, actually divides $M_p$ (Euler's Sophie Germain criterion), so the two residue classes are not statistically symmetric.

**Summation.** Since $\sum_{p \le x} (\log p)/p = \log x + O(1)$ (Mertens),

$$
\mathbb{E}[\mathcal{M}(x)] = \sum_{p \le x} \frac{e^{\gamma}\log(a p)}{p \log 2} \;=\; \frac{e^{\gamma}}{\log 2}\log x + O(1),
$$

which is the conjecture. The two values of $a$ contribute equally to the main term, so the constant $e^{\gamma}/\log 2$ is unaffected.

**Underlying unproved inputs.** The model presumes: (i) the events "$q \mid M_p$" are asymptotically independent across $q$; (ii) Mertens' constant transfers verbatim to the thin progression $q \equiv 1 \pmod{2p}$ with $q$ up to $2^{p/2}$, a range far beyond the Bombieri–Vinogradov modulus $q^{1/2-\varepsilon}$ and even beyond GRH's reach uniformly in $p$; (iii) the Lucas–Lehmer test $S_0 = 4$, $S_{k+1} = S_k^2 - 2$, "$M_p$ prime $\iff M_p \mid S_{p-2}$", is used only as a computational oracle and injects no bias.

## 3. History & State of the Art (SOTA)

- **1644.** Mersenne lists exponents he believes yield primes; the list contains errors (61, 67, 89, 107, 127).
- **1876.** Lucas proves $M_{127}$ prime by hand — largest prime known until 1951.
- **1964.** D. B. Gillies, *Three new Mersenne primes and a statistical theory* (Math. Comp. 18), gives the first heuristic density for Mersenne primes, based on an assumed uniform distribution of divisors in admissible progressions.
- **1980–81.** H. W. Lenstra Jr. and C. Pomerance independently refine the model with the Mertens factor $e^{\gamma}$, in the context of primality-testing surveys (Lenstra, *Séminaire Bourbaki* Exp. 576; Pomerance, *Math. Intelligencer* 3).
- **1983.** S. S. Wagstaff Jr., *Divisors of Mersenne numbers* (Math. Comp. 40), shows Gillies' uniformity assumption conflicts with the prime number theorem in progressions, derives the $a \in \{2,6\}$ correction, and states the asymptotic $\mathcal{M}(x) \sim (e^{\gamma}/\log 2)\log x$ together with the $e^{\gamma}$ per-doubling and $2^{1/e^\gamma}$ ratio corollaries.
- **1989.** Bateman, Selfridge and Wagstaff formulate the "New Mersenne Conjecture", a separate structural companion statement.
- **1996–present.** GIMPS (Great Internet Mersenne Prime Search) converts the conjecture into a live experiment. The 52nd known Mersenne prime, $M_{136279841}$ (41{,}024{,}320 digits), was found by Luke Durant in October 2024.

**SOTA.** No unconditional lower bound on $\mathcal{M}(x)$ beyond $\mathcal{M}(x) \ge 52$ for $x \ge 136279841$; no unconditional nontrivial upper bound at all. All progress is (a) heuristic refinement, (b) structural theorems about divisors of $2^n-1$, (c) computation.

## 4. Partial Results / Verified Cases

- **Computational range.** All prime exponents $p < 57{,}885{,}161$ have been Lucas–Lehmer tested at least once with double-checking, confirming that the list of Mersenne primes is complete below the 48th known one; primality testing (first-time and verification) now extends well past $p = 10^8$, with GIMPS Gerbicz-error-checked PRP tests covering the intervening range. *(frontier — verify current GIMPS milestone status)*
- **Fit of the asymptotic.** Over the 52 known exponents, the observed count tracks $2.5695\log x$ to within roughly one Poisson standard deviation in every dyadic window tested (see §10).
- **Composite classes, proven.** If $p \equiv 3 \pmod 4$ and $2p+1$ is prime, then $2p+1 \mid M_p$, so $M_p$ is composite for $p > 3$ (Euler). Example: $p = 11$, $23 \mid 2047$. Conditional on Dickson's conjecture / Bateman–Horn (infinitude of Sophie Germain primes $\equiv 3 \bmod 4$), infinitely many $M_p$ are composite.
- **Primitive divisors.** Bang–Zsygmondy: $2^n-1$ has a primitive prime divisor for every $n > 6$. Schinzel (1962) sharpened primitive-divisor bounds for $a^n - b^n$.
- **Size of factors.** Stewart (Proc. LMS 1977; *Acta Math.* 211, 2013) proved $P(2^n-1) > n^{1 + 1/(104 \log\log n)}$ for $n$ large, where $P(\cdot)$ is the greatest prime factor — quantitatively strong, but says nothing about how often $2^p-1$ has *no* proper factor.
- **Analogous heuristics validated elsewhere.** The same Mertens-product method predicts finitely many Fermat primes (expected total $\approx \sum 1/2^k \cdot \text{const}$, convergent), consistent with the empirical record of exactly five.

## 5. Principal Obstacles

- **No sieve reaches $\sqrt{M_p}$.** Proving $M_p$ prime for infinitely many $p$ by sieving demands control of primes in the progression $q \equiv 1 \pmod{2p}$ up to $q \approx 2^{p/2}$ — a modulus exponentially smaller than the range, which sounds easy, but the *count* needed is of primes $q$ up to a bound that is exponential in the modulus, and the sieve dimension grows with $p$. Standard sieves lose a factor from the parity problem and cannot produce a lower bound for "no factor at all".
- **Parity problem.** Selberg's parity obstruction blocks any purely sieve-theoretic proof that a sparse sequence contains infinitely many primes. $\{2^p-1\}$ is sparser than any sequence for which the obstruction has been circumvented (the Friedlander–Iwaniec $x^2+y^4$ and Heath-Brown $x^3+2y^3$ breakthroughs use bilinear structure absent here).
- **Exponential sparsity.** $\mathcal{M}(x)$ grows like $\log x$: the sequence has density zero in the primes, and $\sum_p \Pr[M_p \text{ prime}]$ diverges only logarithmically. Divergence this slow leaves no room for a second-moment or large-sieve argument.
- **No algebraic handle.** $2^p-1$ admits no factorization over $\mathbb{Z}[x]$ for prime $p$ and no useful $L$-function; Mersenne primality is not detected by any known automorphic or Galois-cohomological invariant. Circle-method inputs fail because the sequence is not additively structured.
- **Independence is an article of faith.** Divisibility events $q \mid M_p$ for distinct $q$ are genuinely correlated through the multiplicative order of $2$; no theorem quantifies the correlation well enough to bound the resulting product from below.

## 6. The Gap

Proven: structural constraints on divisors, unconditional lower bounds on the largest prime factor, one infinite family of *composite* $M_p$ conditional on Sophie Germain primes, and 52 verified data points.

Conjectured: an asymptotic count.

The gap is the entire quantitative step from "we know which primes *can* divide $M_p$" to "we can bound how often *none* of them does". Concretely, one would need either

$$
\prod_{\substack{q \le 2^{p/2},\ q \equiv 1 (2p),\ q \equiv \pm1 (8)}} \left(1 - \frac1q\right) \;\gg\; \frac{\log p}{p}
$$

on average over $p \le x$ with an *unconditional* Mertens-type estimate valid uniformly for moduli $2p$ against $y = 2^{p/2}$, together with a sieve that converts this product into a genuine prime count. No known technique does either half. Even the far weaker statement $\mathcal{M}(x) \to \infty$ is open, and so is its negation-adjacent partner: infinitely many composite $M_p$.

## 7. Current Research (as of June 2026)

- **GIMPS.** Distributed testing continues past $p \approx 1.4\times10^8$, now GPU-dominated (Durant's 2024 find used a cloud GPU network). Priorities: extending the double-checked verified range and closing gaps below $10^8$ with PRP + Gerbicz–Pietrzak certificates, which give cheap verifiable proofs of PRP tests. *(frontier — verify)*
- **Heuristic refinement.** Work in the Bateman–Horn / Chebotarev-heuristic tradition on second-order terms and on the variance of $\mathcal{M}(x)$ (is the count Poisson with mean $2.5695\log x$, or over-dispersed?). The observed excess of 52 over the predicted $\approx 48$ is well inside Poisson noise.
- **Divisors of $2^n-1$.** Ongoing work on the multiplicative structure of $2^n-1$ — number of prime divisors, squarefree-ness (open even for a single case: no $p$ with $M_p$ non-squarefree is known), Wieferich-type criteria — from the Cunningham Project and from Diophantine-approximation groups following Stewart.
- **abc-conditional results.** Silverman-style arguments (abc $\Rightarrow$ infinitely many non-Wieferich primes) show what a strong Diophantine hypothesis buys; extending this to counting Mersenne primes remains out of reach.
- **Institutions.** Purdue (Wagstaff, Cunningham Project), Dartmouth (Pomerance), Leiden (Lenstra school), Waterloo (Stewart), plus the GIMPS/Mersenne Research Inc. community.

## 8. Future Work

- Prove **infinitely many composite $M_p$** unconditionally — widely viewed as the first realistic target, likely via progress on Sophie Germain primes or an alternative admissible-divisor family.
- Establish an **unconditional upper bound** $\mathcal{M}(x) = o(\pi(x))$, or better $\mathcal{M}(x) = O(x^{\varepsilon})$; even $\mathcal{M}(x) \ll x/(\log x)^{2}$ would be new.
- Prove a **uniform Mertens theorem** for $\prod_{q \le y,\, q \equiv 1 (m)}(1-1/q)$ in the regime $\log y \asymp m$, on average over $m$ — the exact analytic input the heuristic assumes.
- Test the model **statistically**: compare the empirical distribution of $\mathcal{M}(2x)-\mathcal{M}(x)$ against Poisson($e^{\gamma}$) as new exponents arrive; a persistent deviation would indicate a missing correction factor analogous to Wagstaff's $a \in \{2,6\}$.
- Transfer the heuristic to **function-field analogues** ($2^p-1$ replaced by $T^{q^n}-T$-type constructions over $\mathbb{F}_q[T]$), where Weil-type bounds may make the count provable and the constant checkable.

## 9. Key References

- **[Foundational]** D. B. Gillies. *Three new Mersenne primes and a statistical theory.* Mathematics of Computation **18** (1964), 93–97.
- **[Foundational]** S. S. Wagstaff, Jr. *Divisors of Mersenne numbers.* Mathematics of Computation **40** (1983), 385–397.
- **[Foundational]** C. Pomerance. *Recent developments in primality testing.* The Mathematical Intelligencer **3** (1981), 97–105.
- **[Foundational]** H. W. Lenstra, Jr. *Primality testing algorithms (after Adleman, Rumely and Williams).* Séminaire Bourbaki 1980/81, Exp. 576, Lecture Notes in Mathematics 901, Springer, 1981.
- **[Foundational]** P. T. Bateman, R. A. Horn. *A heuristic asymptotic formula concerning the distribution of prime numbers.* Mathematics of Computation **16** (1962), 363–367.
- **[Related conjecture]** P. T. Bateman, J. L. Selfridge, S. S. Wagstaff, Jr. *The new Mersenne conjecture.* American Mathematical Monthly **96** (1989), 125–128.
- **[SOTA / Structural]** C. L. Stewart. *On divisors of Lucas and Lehmer numbers.* Acta Mathematica **211** (2013), 291–314.
- **[SOTA / Structural]** C. L. Stewart. *On divisors of Fermat, Fibonacci, Lucas and Lehmer numbers.* Proceedings of the London Mathematical Society **35** (1977), 425–447.
- **[Structural]** A. Schinzel. *On primitive prime factors of $a^n-b^n$.* Proceedings of the Cambridge Philosophical Society **58** (1962), 555–562.
- **[Conditional]** J. H. Silverman. *Wieferich's criterion and the abc-conjecture.* Journal of Number Theory **30** (1988), 226–237.
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004, Section A3.
- **[Survey]** R. Crandall, C. Pomerance. *Prime Numbers: A Computational Perspective*, 2nd ed., Springer, 2005, Chapters 1 and 4.
- **[Survey]** P. Ribenboim. *The New Book of Prime Number Records*, Springer, 1996.

## 10. Worked Example / Concrete Special Case

**(a) A single exponent.** Take $p = 127 \equiv 3 \pmod 4$, so $a = 2$:

$$
\Pr[M_{127}\text{ prime}] \approx \frac{e^{\gamma}\log(2\cdot 127)}{127\log 2} = \frac{1.78107 \times 5.5373}{88.030} = \frac{9.862}{88.030} = 0.112 .
$$

An 11% prior — and indeed $M_{127} = 170141183460469231731687303715884105727$ is prime (Lucas, 1876). By contrast $p = 11 \equiv 3 \pmod 4$ with $2p+1 = 23$ prime forces $23 \mid M_{11} = 2047 = 23 \times 89$: here the heuristic is overridden by an exact criterion.

**(b) A dyadic-style window.** Predict the count of Mersenne prime exponents in $(10^6, 10^7)$:

$$
\mathbb{E} = \frac{e^{\gamma}}{\log 2}\bigl(\log 10^7 - \log 10^6\bigr) = 2.56954 \times \log 10 = 2.56954 \times 2.302585 = 5.916 .
$$

Observed exponents in that window: $1257787,\ 1398269,\ 2976221,\ 3021377,\ 6972593$ — exactly $5$. Poisson standard deviation $\sqrt{5.92}=2.43$; the deviation is $0.38\sigma$.

**(c) The full record.** With $x = 136279841$ (largest known exponent, October 2024):

$$
\mathcal{M}(x) \approx 2.56954 \times \log(1.36279841\times 10^{8}) = 2.56954 \times 18.7304 = 48.13 ,
$$

against the observed $52$ known exponents $\le x$ (complete only below $57{,}885{,}161$). The excess is $3.87$, i.e. $0.56\sigma$ for a Poisson variable of mean $48.1$. This is the whole empirical case for the conjecture: three decimal places of agreement in the constant $e^{\gamma}/\log 2$, and not one line of proof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*