---
id: 10-theoretical-cs/nc-complexity-of-integer-gcd
title: "NC Complexity of Integer GCD"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NC Complexity of Integer GCD

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/nc-complexity-of-integer-gcd` · **Status:** open

## 1. Problem Statement / Conjecture

Given two $n$-bit integers $a, b \ge 0$, compute $\gcd(a,b)$.

**Open question.** Is the integer GCD problem in $\mathsf{NC}$ — i.e., is there a family of Boolean circuits of size $n^{O(1)}$ and depth $\log^{O(1)} n$ (equivalently, a PRAM algorithm running in $\log^{O(1)} n$ time on $n^{O(1)}$ processors) that outputs $\gcd(a,b)$?

The problem is manifestly in $\mathsf{P}$ (Euclid's algorithm, $O(n)$ arithmetic steps). It is not known to be $\mathsf{P}$-complete, and it is not known to be in $\mathsf{NC}$. Cook (1985) listed it among the handful of natural problems in $\mathsf{P}$ resisting classification; it remains listed as open in Greenlaw–Hoover–Ruzzo (1995).

A complete resolution is either:
1. a uniform circuit family of depth $\log^{O(1)} n$ and polynomial size computing $\gcd$ (or a randomized $\mathsf{RNC}$ version, which would already be a landmark); or
2. a proof that GCD is $\mathsf{P}$-hard under $\mathsf{NC}^1$ (or logspace) many-one reductions, which would place it in $\mathsf{NC}$ only if $\mathsf{NC} = \mathsf{P}$.

## 2. Mathematical Foundations

**Circuit classes.** For $k \ge 1$, $\mathsf{NC}^k$ is the class of languages decided by logspace-uniform families $\{C_n\}$ of fan-in-2 Boolean circuits with $\mathrm{size}(C_n) = n^{O(1)}$ and $\mathrm{depth}(C_n) = O(\log^k n)$; $\mathsf{NC} = \bigcup_k \mathsf{NC}^k$. Then
$$\mathsf{NC}^1 \subseteq \mathsf{L} \subseteq \mathsf{NL} \subseteq \mathsf{TC}^1 \subseteq \mathsf{NC}^2 \subseteq \cdots \subseteq \mathsf{NC} \subseteq \mathsf{P},$$
and $\mathsf{NC} = \mathsf{P}$ is open. Function classes are defined analogously (multi-output circuits).

**Available primitives.** Iterated integer product $\prod_{i=1}^n x_i$, integer division $\lfloor a/b \rfloor$, and $a \bmod b$ are in logspace-uniform $\mathsf{TC}^0 \subseteq \mathsf{NC}^1$ (Hesse–Allender–Barrington 2002), improving Beame–Cook–Hoover (1986), who placed them in $\mathsf{P}$-uniform $\mathsf{NC}^1$. So a single Euclidean step is cheap; the difficulty is the *sequential depth* of the iteration.

**Euclid's iteration.** With $r_0 = a$, $r_1 = b$,
$$r_{i+1} = r_i \bmod r_{i-1}\text{-style recurrence: } r_{i+1} = r_{i-1} - q_i r_i,\qquad q_i = \lfloor r_{i-1}/r_i \rfloor,$$
terminating at $r_{m+1}=0$ with $\gcd(a,b) = r_m$. Lamé's theorem gives $m \le \log_\phi(\sqrt5 \min(a,b)) = O(n)$, with $\phi=(1+\sqrt5)/2$, and consecutive Fibonacci numbers attain it. The quotient sequence $(q_1,\dots,q_m)$ is exactly the continued fraction expansion of $a/b$; its length is $\Theta(n)$ on average, so unrolling is not a route to polylog depth.

**Matrix form.** $\begin{pmatrix} r_i \\ r_{i+1}\end{pmatrix} = M_i \begin{pmatrix} r_{i-1} \\ r_{i}\end{pmatrix}$ with $M_i = \begin{pmatrix} 0 & 1 \\ 1 & -q_i\end{pmatrix} \in \mathrm{GL}_2(\mathbb{Z})$. If the $q_i$ were known in advance, the product $M_m\cdots M_1$ is a prefix computation of depth $O(\log n)$ — but each $q_i$ depends on all earlier ones. This *data dependence*, not arithmetic cost, is the whole problem.

**Contrast: polynomial GCD.** For $f,g \in F[x]$ of degree $\le n$, $\gcd(f,g)$ is read off from the ranks of the subresultant/Sylvester matrices
$$\mathrm{Syl}_k(f,g) \in F^{(2n-k)\times(2n-k)},\qquad \deg\gcd(f,g) = n - \mathrm{rank\ profile},$$
and determinants/ranks over a field are in $\mathsf{NC}^2$. Hence polynomial GCD $\in \mathsf{NC}^2$ (Borodin–von zur Gathen–Hopcroft 1982; von zur Gathen 1984). Over $\mathbb{Z}$ there is **no degree parameter**: the "size" of an integer is its logarithm, not a linear-algebraic rank, and carries destroy the graded structure that makes resultants work.

**$k$-ary reduction (the workhorse of all sublinear algorithms).** Fix $k$ coprime to $\gcd(a,b)$. Given $a,b$ with $b$ invertible mod $k$, there exist $x,y$ with $0<|x|,|y| \le \sqrt{k}$ and
$$xa + yb \equiv 0 \pmod k,$$
by pigeonhole on the $\lceil\sqrt k\rceil^2 > k$ pairs. Replace $a \leftarrow |xa+yb|/k$. Since $\gcd(a,b) \mid xa+yb$ and $\gcd(\gcd(a,b),k)=1$, the true GCD survives; the new pair may acquire *spurious* factors of size $\le \sqrt k$, removed by a final cleanup. Each step destroys about $\tfrac12 \log_2 k$ bits of the total $\|a\|+\|b\|$.

## 3. History & State of the Art (SOTA)

- **1971.** Schönhage's half-GCD gives sequential time $O(M(n)\log n)$ — fast, but inherently sequential in its recursion depth (each half-GCD call needs the previous one's transformation matrix).
- **1982–84.** Borodin–von zur Gathen–Hopcroft and von zur Gathen put *polynomial* GCD, resultants and Padé approximation in $\mathsf{NC}$, sharpening the contrast with $\mathbb{Z}$.
- **1985.** Cook's taxonomy names integer GCD as a natural problem in $\mathsf{P}$ with no known $\mathsf{NC}$ algorithm and no $\mathsf{P}$-hardness proof.
- **1987.** Kannan–Miller–Rudolph give the first *sublinear* parallel GCD: $O\!\left(\dfrac{n\log\log n}{\log n}\right)$ time on a CRCW PRAM with $n^2$ processors — the first break of the $\Theta(n)$ Euclidean barrier.
- **1988.** Adleman–Kompella, "Using smoothness to achieve parallelism": expected time $O(\log n)$ using $\exp(O(\sqrt{n\log n}))$ processors — polylog *depth* at subexponential width, showing the obstruction is not depth alone but the depth–size trade-off.
- **1990.** Chor–Goldreich reach $O(n/\log n)$ time with $n^{1+\epsilon}$ processors, using 2-dimensional lattice reduction to find the $k$-ary multipliers $(x,y)$; this is the shape of the current record.
- **1994–2008.** Sorenson's $k$-ary and "right-shift" GCD algorithms, Cesari's parallel Schönhage implementation, and Sedjelmaci's parallel extended GCD refine constants and processor counts but do not improve the $\Theta(n/\log n)$ time exponent.

**Status of the record (2026):** best known parallel time remains $O(n/\log n)$ with $n^{1+\epsilon}$ processors; best known lower bound is nothing beyond $\Omega(\log n)$ depth (fan-in). The gap between $n/\log n$ and $\log^{O(1)} n$ has not moved in 35 years.

## 4. Partial Results / Verified Cases

- **Polynomial GCD over any field:** in $\mathsf{NC}^2$ (BGH 1982). Also $\gcd$ in $F[x]$ for $F$ finite, and Padé/rational-function reconstruction.
- **Fixed-length inputs:** $\gcd(a,b)$ for $n = O(\log^{c} n')$ bits — trivially in $\mathsf{NC}$ by table lookup / brute-force width $2^{\mathrm{polylog}}$… more usefully, $\gcd(a,b)$ with $b = O(\log^{O(1)} n)$-bit is in $\mathsf{NC}^1$ (compute $a \bmod b$ in $\mathsf{TC}^0$, then a polylog-size Euclid).
- **Smooth inputs:** if $a$ or $b$ is $B$-smooth with $B = \log^{O(1)} n$, factor-and-compare gives $\mathsf{NC}$; Adleman–Kompella exploit exactly this, at $\exp(O(\sqrt{n\log n}))$ processors.
- **Pre-factored inputs:** given factorizations, $\gcd$ is a coordinatewise $\min$ of exponents — $\mathsf{NC}^1$.
- **Small quotient sequences:** if the continued fraction of $a/b$ has $m = \log^{O(1)} n$ terms (e.g. $a/b$ with bounded partial-quotient count, or $b \mid a$-adjacent cases), the $\mathrm{GL}_2(\mathbb{Z})$ product is a prefix scan of depth $O(\log n \cdot m)$ — in $\mathsf{NC}$.
- **Related primitives already resolved:** iterated product, integer division, $a \bmod b$ in uniform $\mathsf{TC}^0$ (Hesse–Allender–Barrington 2002); the *iterated mod* problem $((x \bmod m_1) \bmod m_2)\cdots$ shown to admit an $\mathsf{NC}$ algorithm by Karloff–Ruzzo (1989) — removing a natural candidate for $\mathsf{P}$-hardness.
- **Modular inverse:** in $\mathsf{NC}$ iff extended GCD is (they are $\mathsf{NC}^1$-interreducible); no unconditional $\mathsf{NC}$ algorithm is known for either.

## 5. Principal Obstacles

- **Adaptivity of the quotients.** Every known correct reduction step needs the *current* pair to choose its transformation. Prefix-sum/parallel-prefix techniques require the semigroup elements to be known independently; here $M_i$ is a function of $M_{i-1}\cdots M_1$. Speculative evaluation over all possible quotients costs $\prod_i (q_i+1)$ branches, which is $2^{\Theta(n)}$ in the worst case.
- **Bounded bit-drain per step.** $k$-ary reduction with modulus $k$ drains $\tfrac12\log_2 k$ bits and costs $\mathrm{poly}(k)$ work (or a 2D lattice reduction) to find $(x,y)$. To reach polylog depth one needs $k = 2^{n/\mathrm{polylog}\,n}$, i.e. superpolynomial processor count. This is exactly the Adleman–Kompella trade-off curve; nobody has found a reduction with *poly* cost and *superlogarithmic* bit-drain.
- **No algebraic invariant.** In $F[x]$ the GCD degree is a rank, computable by determinants in $\mathsf{NC}^2$. Over $\mathbb{Z}$ the analogue would be reading $\gcd(a,b)$ from lattice/resultant data of $\mathbb{Z}$-modules, but $\mathbb{Z}$-lattice invariants (Smith normal form of $\begin{pmatrix} a & b\end{pmatrix}$) *are* the GCD — circular. Carry propagation means $\mathbb{Z}$ is not graded; there is no truncation of $a$ that determines the answer.
- **Failure of $\mathsf{P}$-hardness attempts.** Standard $\mathsf{P}$-complete gadgets (circuit value, lexicographically-first orderings) need a mechanism to encode arbitrary Boolean gates into arithmetic on two integers. The GCD problem has only $O(n)$ "state" (the current pair), and the Euclidean transition is a $\mathrm{GL}_2(\mathbb{Z})$ action — too structured to simulate a general circuit. Karloff–Ruzzo's $\mathsf{NC}$ result for iterated mod killed the most natural hardness route.
- **Number-theoretic randomness.** Randomized $\mathsf{RNC}$ attempts stumble on the fact that random shifts/multipliers destroy the GCD unless coprime to the answer — and testing coprimality is the problem itself.

## 6. The Gap

Proven: $\mathsf{TIME} = O(n/\log n)$ with $n^{1+\epsilon}$ processors (Chor–Goldreich); $\mathsf{TIME} = O(\log n)$ with $\exp(O(\sqrt{n\log n}))$ processors (Adleman–Kompella). Sought: $\mathsf{TIME} = \log^{O(1)} n$ with $n^{O(1)}$ processors.

The exact barrier: **produce a reduction map $R$ computable by poly-size, polylog-depth circuits, taking a pair $(a,b)$ of total bit-length $L$ to a pair of total bit-length $L - \Omega(L/\log^{c} L)$ while preserving $\gcd$ up to controllable spurious factors.** All known $R$ achieve drain $O(\log n)$ per poly-size step. Any improvement to drain $n^{\delta}$ per polylog-depth step immediately gives $\mathsf{NC}$ by $O(n^{1-\delta})$… and drain $L/\mathrm{polylog}$ gives it outright. The complementary gap: show that any such $R$ must encode a $\mathsf{P}$-hard computation.

## 7. Current Research (as of June 2026)

- **Lattice-based multiplier search.** Refinements of Chor–Goldreich's 2D reduction to higher-dimensional $\ell$-term relations $\sum_{i\le \ell} x_i a_i \equiv 0 \pmod k$, aiming for larger drain per step; the cost of finding short vectors grows faster than the drain, and no crossing point has been found. *(frontier — verify)*
- **Circuit lower bounds via algebraic proof complexity.** Attempts to show GCD requires $\Omega(n^{\epsilon})$ depth for restricted models (arithmetic circuits over $\mathbb{Z}$ with division, monotone-style restrictions) — active in the algebraic-complexity community (Tel Aviv, Rutgers, IIT Bombay). *(frontier — verify)*
- **Uniform $\mathsf{TC}^0$ number theory.** Following Hesse–Allender–Barrington, work on which number-theoretic functions descend to $\mathsf{TC}^0$; GCD is the canonical remaining target. Groups at Rutgers (Allender) and Chicago.
- **Quantum and smoothness hybrids.** Whether a smoothness-based approach can be derandomized or made poly-processor using ECM-style parallelism; no positive result.
- **Practical parallel GCD.** GPU/SIMD implementations of Sorenson $k$-ary and half-GCD variants achieve constant-factor gains only; the $\Theta(n/\log n)$ depth is unmoved.

## 8. Future Work

- Search for an $\mathsf{NC}$ reduction preserving $\gcd$ with polylog-many spurious factors, e.g. by working simultaneously modulo many small primes and reconstructing via CRT.
- Prove $\mathsf{P}$-hardness for a *promise* or *search* variant (e.g. computing the full continued fraction expansion of $a/b$, or the lexicographically-first Euclidean remainder sequence), then attempt to transfer.
- Determine the exact processor–time trade-off curve: is there $T(P)$ with $T = \tilde O(n / \log P)$ that is provably optimal for $k$-ary-style reductions? A matching lower bound in a restricted "bit-drain" model would formalize the barrier.
- Settle the modular-inverse question for special moduli (smooth, prime-power) as stepping stones.
- Explore whether GCD is complete for some intermediate class between $\mathsf{NC}$ and $\mathsf{P}$ (e.g. via $\mathrm{GL}_2(\mathbb{Z})$-iteration as a natural complete problem).

## 9. Key References

- **[Foundational]** Cook, S. A. *A taxonomy of problems with fast parallel algorithms.* Information and Control, 64(1–3):2–22, 1985.
- **[Foundational]** Borodin, A., von zur Gathen, J., Hopcroft, J. *Fast parallel matrix and GCD computations.* Information and Control, 52(3):241–256, 1982.
- **[Foundational]** von zur Gathen, J. *Parallel algorithms for algebraic problems.* SIAM Journal on Computing, 13(4):802–824, 1984.
- **[SOTA]** Kannan, R., Miller, G., Rudolph, L. *Sublinear parallel algorithm for computing the greatest common divisor of two integers.* SIAM Journal on Computing, 16(1):7–16, 1987.
- **[SOTA]** Chor, B., Goldreich, O. *An improved parallel algorithm for integer GCD.* Algorithmica, 5(1):1–10, 1990.
- **[SOTA]** Adleman, L. M., Kompella, K. *Using smoothness to achieve parallelism.* Proc. 20th ACM Symposium on Theory of Computing (STOC), 528–538, 1988.
- **[SOTA]** Sorenson, J. *Two fast GCD algorithms.* Journal of Algorithms, 16(1):110–144, 1994.
- **[Recent]** Sedjelmaci, S. M. *A parallel extended GCD algorithm.* Journal of Discrete Algorithms, 6(3):526–538, 2008.
- **[Recent]** Cesari, G. *Parallel implementation of Schönhage's integer GCD algorithm.* Algorithmic Number Theory (ANTS-III), LNCS 1423, Springer, 1998.
- **[Related]** Hesse, W., Allender, E., Barrington, D. A. M. *Uniform constant-depth threshold circuits for division and iterated multiplication.* Journal of Computer and System Sciences, 65(4):695–716, 2002.
- **[Related]** Beame, P. W., Cook, S. A., Hoover, H. J. *Log depth circuits for division and related problems.* SIAM Journal on Computing, 15(4):994–1003, 1986.
- **[Related]** Karloff, H. J., Ruzzo, W. L. *The iterated mod problem.* Information and Computation, 80(3):193–204, 1989.
- **[Survey]** Greenlaw, R., Hoover, H. J., Ruzzo, W. L. *Limits to Parallel Computation: P-Completeness Theory.* Oxford University Press, 1995. (GCD listed among open problems.)
- **[Survey]** Knuth, D. E. *The Art of Computer Programming, Vol. 2: Seminumerical Algorithms,* 3rd ed. Addison-Wesley, 1997, §4.5.2–4.5.3.
- **[Foundational]** Schönhage, A. *Schnelle Berechnung von Kettenbruchentwicklungen.* Acta Informatica, 1(2):139–144, 1971.

## 10. Worked Example / Concrete Special Case

Take $a = 127$, $b = 91$ (7 bits each, total $L = 14$ bits). True answer: $127$ is prime, $91 = 7\cdot 13$, so $\gcd = 1$.

**Euclid (sequential, depth 4):**
$$127 = 1\cdot 91 + 36,\quad 91 = 2\cdot 36 + 19,\quad 36 = 1\cdot 19 + 17,\quad 19 = 1\cdot 17 + 2,\ \dots$$
Quotient sequence $(1,2,1,1,8,2)$ — six adaptive steps, each needing the previous remainder.

**$k$-ary reduction with $k = 16$ ($\sqrt k = 4$).** We need $x,y$ with $0<|x|,|y|\le 4$ and $xa + yb \equiv 0 \pmod{16}$. Reduce: $127 \equiv -1$, $91 \equiv 11 \equiv -5 \pmod{16}$. The congruence becomes
$$-x - 5y \equiv 0 \pmod{16} \iff x \equiv -5y \pmod{16}.$$
Scan $y = 1,2,3$: $y=1 \Rightarrow x \equiv 11$ (too big); $y=2 \Rightarrow x \equiv 6$ (too big); $y=3 \Rightarrow x \equiv 1$. So $(x,y) = (1,3)$:
$$xa + yb = 127 + 273 = 400 = 16 \cdot 25.$$
New pair: $(a', b') = (25, 91)$. Total bits $5 + 7 = 12$, a drain of $2 = \tfrac12\log_2 16$ bits — exactly the predicted rate.

**Correctness check.** $g = \gcd(127,91)$ divides $400$, and $\gcd(g,16)=1$, so $g \mid 25$; hence $g \mid \gcd(25,91) = 1$. ✓ (In general $\gcd(a',b')$ may exceed $g$ by a spurious factor $\le \sqrt k = 4$; the algorithm strips such factors at the end by trial division over the $O(\sqrt k)$ candidates — an $\mathsf{NC}$ step when $k$ is polynomial.)

**Why this does not give $\mathsf{NC}$.** The search for $(x,y)$ is over a grid of $k$ pairs, done in $O(1)$ parallel time on $O(k)$ processors (or by 2D lattice reduction in $\mathsf{NC}^1$). With $n$-bit inputs and $k = n^{O(1)}$, each step costs polylog depth and drains $\Theta(\log n)$ bits, so the number of rounds is
$$\frac{2n}{\tfrac12 \log_2 k} = \Theta\!\left(\frac{n}{\log n}\right),$$
which is Chor–Goldreich's bound. To reach depth $\log^{O(1)} n$ one needs $k = 2^{n/\mathrm{polylog}\,n}$, i.e. $\exp(n/\mathrm{polylog}\,n)$ processors for the multiplier search — outside $\mathsf{NC}$. Closing that exponential gap in the modulus size, or proving it cannot be closed, is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*