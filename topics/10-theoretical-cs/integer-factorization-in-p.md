---
id: 10-theoretical-cs/integer-factorization-in-p
title: "Integer Factorization in P"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Integer Factorization in P

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/integer-factorization-in-p` · **Status:** open

## 1. Problem Statement / Conjecture

Does there exist a deterministic algorithm that, given the binary representation of an integer $N > 1$, outputs the multiset of prime factors of $N$ in time bounded by a polynomial in $\log N$?

Equivalently, in decision form: is
$$\mathrm{FACT} = \{\,\langle N, k\rangle : N \text{ has a prime divisor } p \le k\,\} \in \mathsf{P}\,?$$
The search and decision versions are polynomial-time equivalent (binary search on $k$, then recursion on $N/p$), so either formulation settles the other.

A resolution requires one of:

- **Positive:** an explicit algorithm with a proven $(\log N)^{O(1)}$ bound on a standard multitape Turing machine or logarithmic-cost RAM, with no unproven hypotheses (or, weakly positive, conditional on GRH).
- **Negative:** an unconditional super-polynomial lower bound on any algorithm for FACT. This would imply $\mathsf{P} \ne \mathsf{NP}$ and is far beyond current lower-bound technology.

The consensus expectation among cryptographers is that no such algorithm exists; among complexity theorists the question is genuinely open, since FACT sits in $\mathsf{NP} \cap \mathsf{coNP}$ and so is very unlikely to be $\mathsf{NP}$-hard.

## 2. Mathematical Foundations

**Input size.** $n = \lceil \log_2 N \rceil$. "Polynomial time" means $n^{O(1)}$ bit operations, not $N^{O(1)}$; trial division costs $N^{1/2}$ operations $= 2^{n/2}$, exponential.

**Subexponential notation.** For $0 \le \alpha \le 1$ and $c>0$,
$$L_N[\alpha, c] = \exp\!\Big( (c+o(1)) \,(\ln N)^{\alpha} (\ln \ln N)^{1-\alpha} \Big).$$
Here $\alpha = 1$ is exponential in $n$, $\alpha = 0$ is polynomial in $n$. Every published classical algorithm has $\alpha \ge 1/3$.

**Current best heuristic bound (General Number Field Sieve).**
$$L_N\big[\tfrac13,\ (64/9)^{1/3}\big], \qquad (64/9)^{1/3} \approx 1.9229,$$
and $L_N[\frac13, (32/9)^{1/3}]$, $(32/9)^{1/3}\approx 1.5263$, for the Special NFS on integers of the form $a^e \pm b$ with small $a,b$ (Buhler–Lenstra–Pomerance 1993).

**The congruence-of-squares principle.** All sieve methods reduce to finding $x \not\equiv \pm y \pmod N$ with
$$x^2 \equiv y^2 \pmod N \quad \Longrightarrow \quad N \mid (x-y)(x+y), \quad \gcd(x-y, N) \text{ a proper divisor with prob. } \ge 1/2 .$$
Relations are collected over a factor base $\mathcal{B} = \{p_1,\dots,p_k\}$ of primes below a bound $B$, and combined by linear algebra over $\mathbb{F}_2$: exponent vectors $v(m) = (e_1 \bmod 2, \dots, e_k \bmod 2)$ for $B$-smooth values $m$, and any nontrivial kernel vector of the $\mathbb{F}_2$-matrix yields a square. The runtime is governed by the Canfield–Erdős–Pomerance smoothness density
$$\Psi(x, x^{1/u}) / x = u^{-u(1+o(1))},$$
whose optimization over $B$ produces the $\alpha = 1/2$ exponent for quadratic-sieve-type methods and $\alpha = 1/3$ once the sieve runs over number-field norms of subexponentially small size.

**Complexity placement.**
- $\mathrm{FACT} \in \mathsf{NP} \cap \mathsf{coNP}$: the full factorization plus Pratt primality certificates verifies both membership and non-membership, using AKS or Pratt (Agrawal–Kayal–Saxena 2004 makes primality itself deterministic polynomial time).
- Under GRH, $\mathrm{FACT} \in \mathsf{UP} \cap \mathsf{coUP}$ (Fellows–Koblitz 1992), since the factorization is unique — so FACT cannot be $\mathsf{NP}$-complete unless $\mathsf{NP} = \mathsf{coNP}$.
- $\mathrm{FACT} \in \mathsf{BQP}$ (Shor 1997), via reduction to order-finding: for random $a$ with $\gcd(a,N)=1$, compute $r = \mathrm{ord}_N(a)$ by quantum phase estimation; if $r$ even and $a^{r/2}\not\equiv -1$, then $\gcd(a^{r/2}-1,N)$ is a proper factor with probability $\ge 1/2$.

## 3. History & State of the Art (SOTA)

- **1801** — Gauss, *Disquisitiones Arithmeticae*, Art. 329, explicitly names distinguishing primes from composites and resolving composites into factors as a central problem "of the dignity of science."
- **1643 / 1926 / 1931** — Fermat's difference-of-squares; Kraitchik's improvement (only $x^2 \equiv y^2 \bmod N$ needed); Lehmer–Powers' continued-fraction method.
- **1975** — Pollard's $p-1$; **1975** Pollard's $\rho$, running in $O(N^{1/4})$ expected time, which factored $F_8$.
- **1978** — Rivest–Shamir–Adleman make the hardness of factoring the basis of public-key cryptography, converting a curiosity into an economically load-bearing assumption.
- **1981** — Dixon's random-squares algorithm: first *rigorous* (unconditional, randomized) subexponential bound $L_N[\frac12, 2\sqrt2]$.
- **1982–85** — Pomerance's quadratic sieve, $L_N[\frac12,1]$ heuristically.
- **1987** — H. W. Lenstra Jr.'s elliptic curve method (ECM): expected $L_p[\frac12,\sqrt2]$ in the *smallest* prime factor $p$, not in $N$.
- **1988–93** — Pollard's number field sieve, developed by Buhler, Lenstra, Pomerance, Adleman, Coppersmith; first $\alpha = 1/3$ algorithm.
- **1992** — Lenstra–Pomerance rigorous $L_N[\frac12,1]$ using class groups of quadratic orders.
- **1994/97** — Shor's quantum polynomial-time algorithm.
- **2002/04** — AKS: PRIMES $\in \mathsf{P}$, removing primality from the list and sharpening the contrast with factoring.
- **2019–20** — RSA-240 (795 bits) and RSA-250 (829 bits) factored by Boudot, Gaudry, Guillevic, Heninger, Thomé, Zimmermann; RSA-250 cost roughly 2700 core-years on 2.1 GHz Xeon Gold cores.

**Bottom line:** the exponent $\alpha$ has moved $1 \to \frac12 \to \frac13$ in fifty years and has not moved since 1993.

## 4. Partial Results / Verified Cases

Polynomial time is achieved on these concrete classes:

| Class | Method | Bound |
|---|---|---|
| $N = m^k$, $k \ge 2$ (perfect powers) | Bernstein 1998 | $O(n \log^{O(1)} n)$ |
| $N$ given $\varphi(N)$, or $\lambda(N)$, or any multiple of $\lambda(N)$ | Miller 1976 (randomized; deterministic under ERH) | $n^{O(1)}$ |
| RSA modulus $N=pq$ given $(e,d)$ with $ed \equiv 1 \bmod \varphi(N)$ | Coron–May 2007 (deterministic, unconditional) | $n^{O(1)}$ |
| $N = pq$ with $\lfloor p \rfloor$ known to within $N^{1/4}$, i.e. half the bits of $p$ | Coppersmith 1997 (LLL on a lattice of shifted polynomials) | $n^{O(1)}$ |
| $N = pq$ with $|p-q| < c\,N^{1/4}$ | Fermat / Lehman | $n^{O(1)}$ |
| $p \mid N$ with $p-1$ (or $p+1$, or $\\#E(\mathbb{F}_p)$) $B$-smooth for $B = n^{O(1)}$ | Pollard $p{-}1$, Williams $p{+}1$, ECM | $n^{O(1)}$ |
| Two moduli sharing a prime | $\gcd$; used by Lenstra et al. 2012 to break $\sim 0.2\%$ of surveyed live RSA keys | $\tilde O(n)$ |
| Any $N$, on a unit-cost RAM with unbounded-precision multiplication | Shamir 1979 | $O(n)$ arithmetic steps |
| Any $N$, on a quantum computer | Shor 1997; Regev 2023 reduces to $\tilde O(n^{3/2})$ gates over $\sqrt{n}+4$ runs | $n^{O(1)}$ |

Computationally, all $N < 2^{64}$ are factorable in microseconds (Hart's one-line factorer, SQUFOF, Pollard $\rho$-Brent); the RSA challenge frontier stands at 829 bits (RSA-250). The largest factor ever extracted by ECM is 83 decimal digits (R. Propper, 2023) *(frontier — verify)*.

## 5. Principal Obstacles

- **The smoothness wall.** Every classical subexponential method optimizes a tradeoff between the *cost of generating* candidate residues and their *probability of being smooth*, $u^{-u}$. NFS pushes the residues down to size $L_N[\frac23,\cdot]$ by working with algebraic norms; a further drop to $\alpha < \frac13$ would need residues of size $L_N[\frac13,\cdot]$ arising from a number field of degree $\sim n^{2/3}$, where the norms *grow back* because of the discriminant. Coppersmith's multiple-polynomial variant shaves the constant to $\approx 1.902$ but not the exponent.
- **No algebraic handle.** Factoring is not known to reduce to any problem with a group structure exploitable by Fourier/character-sum methods *classically*. Shor's success is exactly the observation that the hidden subgroup of $\mathbb{Z}$ underlying order-finding is accessible to a quantum Fourier transform; no classical analogue is known, and the standard sampling arguments show that a classical algorithm cannot extract the period from polynomially many black-box evaluations.
- **Lattice methods saturate at $N^{1/4}$.** Coppersmith's technique solves $f(x) \equiv 0 \bmod p$ for $|x| < p^{1/\deg f}$; for $f(x) = x + \tilde p$ over $N=pq$ this caps at $N^{1/4}$, and Boneh–Durfee-type improvements are provably obstructed for a generic modulus with no side information. The lattice dimension needed to break the bound grows like the entropy of the unknown, i.e. exponentially.
- **Lower bounds are unavailable.** A negative resolution requires super-polynomial circuit lower bounds for a problem in $\mathsf{NP}\cap\mathsf{coNP}$. Natural proofs (Razborov–Rudich) and relativization both bar the known techniques; the natural-proofs barrier is itself derived from the assumed hardness of factoring-like problems, so the obstruction is circular.

## 6. The Gap

Proven: polynomial time on structured inputs where partial arithmetic information (a multiple of the order, half the bits of $p$, a smooth auxiliary group order, a shared prime, a nonstandard machine model) collapses the search space. Sought: polynomial time on a *generic* $N = pq$ with $p, q$ independent random primes of $n/2$ bits, where no such information exists.

The precise barrier is one number: the exponent $\alpha$ in $L_N[\alpha, c]$. Every known classical method has $\alpha \ge \frac13$; the target is $\alpha = 0$. Nothing is known even at $\alpha = 0.32$. No result rules out $\alpha=0$ either — there is no unconditional lower bound better than $\Omega(n)$ (time to read the input) for FACT on any general model. The gap is total in both directions.

## 7. Current Research (as of June 2026)

- **Quantum resource reduction.** Regev's 2023 multidimensional variant ($\tilde O(n^{3/2})$ gates, $\sqrt n + 4$ circuit runs) and the Ragavan–Vaikuntanathan space-efficient implementation are the main lines; Ekerå–Håstad-style analyses continue to sharpen concrete qubit counts. Groups at CWI, MIT, KTH, and Inria are active *(frontier — verify current records)*.
- **NFS constant-factor and record work.** Inria Nancy (Thomé, Gaudry), UC San Diego (Heninger), and the CADO-NFS community. Post-RSA-250 attention is on discrete logarithms and on Tower-NFS variants for pairing-friendly curves rather than on new $\alpha$.
- **Lattice/Coppersmith frontier.** Extensions to multivariate and multi-prime settings (May, Nowakowski, Sarkar), and side-channel-assisted partial-key recovery.
- **Claimed classical breakthroughs.** Periodic preprints asserting polynomial-time factoring — including quantum-annealing/Schnorr-lattice hybrids in the style of the 2022 "sublinear-resource" claims — have not survived scrutiny; the Schnorr 2021 lattice approach was shown not to outperform NFS in practice.
- **Complexity-side.** Work on whether factoring is hard for $\mathsf{P}$ under $\mathsf{NC}^1$ reductions, and on fine-grained/one-way-function characterizations (Liu–Pass style meta-complexity), gives context but no bound.

## 8. Future Work

- **Break $\alpha = 1/3$.** Adleman and Lenstra have repeatedly framed the target as a method producing relations among *smaller* auxiliary quantities than NFS norms — e.g. via higher-genus curves, function fields, or class groups of number fields of growing degree.
- **Derandomize/extend rigorous bounds.** The rigorous frontier is $L_N[\frac12,1]$ (Lenstra–Pomerance); a rigorous $L_N[\frac13,\cdot]$ result, i.e. proving the NFS heuristic on norm smoothness, is a stated open problem and would require smoothness estimates for algebraic norms currently beyond analytic reach.
- **Reduce factoring to a well-studied hard problem in both directions.** Factoring is known to reduce to order-finding and to the RSA problem in special cases; establishing an equivalence with lattice problems or with a natural $\mathsf{NP}\cap\mathsf{coNP}$-complete candidate would relocate the difficulty.
- **Dequantize Shor.** Determine whether the period-finding subroutine admits a classical simulation for the specific structured functions $x \mapsto a^x \bmod N$, or prove an oracle separation ruling it out.

## 9. Key References

- **[Foundational]** R. L. Rivest, A. Shamir, L. Adleman. *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems.* Communications of the ACM 21(2):120–126, 1978.
- **[Foundational]** G. L. Miller. *Riemann's Hypothesis and Tests for Primality.* Journal of Computer and System Sciences 13(3):300–317, 1976.
- **[Foundational]** J. D. Dixon. *Asymptotically Fast Factorization of Integers.* Mathematics of Computation 36(153):255–260, 1981.
- **[Foundational]** H. W. Lenstra Jr. *Factoring Integers with Elliptic Curves.* Annals of Mathematics 126(3):649–673, 1987.
- **[Foundational]** A. K. Lenstra, H. W. Lenstra Jr. (eds.). *The Development of the Number Field Sieve.* Lecture Notes in Mathematics 1554, Springer, 1993.
- **[Foundational]** H. W. Lenstra Jr., C. Pomerance. *A Rigorous Time Bound for Factoring Integers.* Journal of the AMS 5(3):483–516, 1992.
- **[Foundational]** P. W. Shor. *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.* SIAM Journal on Computing 26(5):1484–1509, 1997.
- **[Foundational]** M. Agrawal, N. Kayal, N. Saxena. *PRIMES is in P.* Annals of Mathematics 160(2):781–793, 2004.
- **[Structural]** D. Coppersmith. *Small Solutions to Polynomial Equations, and Low Exponent RSA Vulnerabilities.* Journal of Cryptology 10(4):233–260, 1997.
- **[Structural]** J.-S. Coron, A. May. *Deterministic Polynomial-Time Equivalence of Computing the RSA Secret Key and Factoring.* Journal of Cryptology 20(1):39–50, 2007.
- **[Structural]** M. R. Fellows, N. Koblitz. *Self-Witnessing Polynomial-Time Complexity and Prime Factorization.* Designs, Codes and Cryptography 2(3):231–235, 1992.
- **[Structural]** A. Shamir. *Factoring Numbers in $O(\log n)$ Arithmetic Steps.* Information Processing Letters 8(1):28–31, 1979.
- **[SOTA / Recent]** F. Boudot, P. Gaudry, A. Guillevic, N. Heninger, E. Thomé, P. Zimmermann. *Comparing the Difficulty of Factorization and Discrete Logarithm: A 240-Digit Experiment.* CRYPTO 2020, LNCS 12171, Springer.
- **[SOTA / Recent]** O. Regev. *An Efficient Quantum Factoring Algorithm.* arXiv:2308.06572, 2023.
- **[SOTA / Recent]** D. J. Bernstein. *Detecting Perfect Powers in Essentially Linear Time.* Mathematics of Computation 67(223):1253–1283, 1998.
- **[Survey]** C. Pomerance. *A Tale of Two Sieves.* Notices of the AMS 43(12):1473–1485, 1996.
- **[Survey]** R. Crandall, C. Pomerance. *Prime Numbers: A Computational Perspective.* 2nd ed., Springer, 2005.
- **[Survey]** A. May. *Using LLL-Reduction for Solving RSA and Factorization Problems.* In *The LLL Algorithm*, Springer, 2010, pp. 315–348.

## 10. Worked Example / Concrete Special Case

**(a) Fermat's method — the easy special case.** Let $N = 8051$. Write $N = x^2 - y^2$:
$$\lceil \sqrt{8051}\,\rceil = 90, \quad 90^2 - 8051 = 8100 - 8051 = 49 = 7^2 .$$
So $8051 = 90^2 - 7^2 = (90-7)(90+7) = 83 \cdot 97$. One step, because $|97 - 83| = 14$ is tiny relative to $N^{1/4} \approx 9.5$-scale slack. This is exactly the "$|p-q|$ small" row of Section 4. For a generic $N=pq$ with $p,q$ independent, $|p-q| \approx \sqrt N$ and Fermat needs $\approx N^{1/2}$ steps — worse than trial division.

**(b) Dixon's random squares — the general mechanism.** Let $N = 1649$, factor base $\mathcal{B} = \{2\}$ extended to $\{2,5\}$. Compute $s^2 \bmod N$ for $s$ just above $\sqrt N \approx 40.6$:

$$41^2 = 1681 \equiv 32 = 2^5, \qquad 42^2 = 1764 \equiv 115 = 5\cdot 23, \qquad 43^2 = 1849 \equiv 200 = 2^3 5^2 .$$

Exponent vectors mod 2 over $\mathcal{B}=\{2,5\}$: $v(41) = (1,0)$, $v(43) = (1,0)$. ($42$ is discarded: $23 \notin \mathcal{B}$.) Their sum is $(0,0)$ — a kernel vector. Hence
$$(41\cdot 43)^2 \equiv 32 \cdot 200 = 6400 = 80^2 \pmod{1649}.$$
Set $x = 41\cdot 43 = 1763 \equiv 114$, $y = 80$. Then $x \not\equiv \pm y$, and
$$\gcd(114 - 80,\ 1649) = \gcd(34, 1649) = 17, \qquad 1649 = 17 \cdot 97 .$$

**Why this does not scale.** The relation-collection step succeeded because two of the first three residues were $5$-smooth. For $N$ of $n$ bits, residues near $\sqrt N$ have size $\approx 2^{n/2}$, and the density of $B$-smooth numbers of that size with $B = L_N[\frac12,\frac12]$ is $L_N[\frac12,-\frac12]$ — so about $L_N[\frac12,\frac12]$ trials are needed to gather $|\mathcal{B}|$ relations, plus a sparse linear-algebra solve of the same cost. NFS replaces $2^{n/2}$-sized residues with $L_N[\frac23,\cdot]$-sized algebraic norms and reaches $L_N[\frac13,1.923]$. **The entire open problem is whether the residues can be made polynomially small.** For $N=1649$ the answer was "yes, by luck"; for $N$ = RSA-2048 no method is known that does better than gathering $\approx 2^{112}$-cost relations.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*