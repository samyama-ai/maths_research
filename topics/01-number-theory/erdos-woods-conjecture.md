---
id: 01-number-theory/erdos-woods-conjecture
title: "Erdos-Woods Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Woods Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-woods-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Write $\operatorname{rad}(n)=\prod_{p\mid n}p$ for the **radical** (squarefree kernel) of $n\ge 1$, equivalently the set of primes dividing $n$.

**Conjecture (Erdős, Woods).** There exists a fixed integer $k\ge 1$ such that for all positive integers $x,y$,
$$\operatorname{rad}(x+i)=\operatorname{rad}(y+i)\quad\text{for all } i=0,1,\dots,k \;\Longrightarrow\; x=y .$$

In words: a positive integer is uniquely determined by the list of prime supports of a bounded block of consecutive integers starting at it. Call the statement for a particular $k$ the property $\mathrm{EW}(k)$; $\mathrm{EW}(k)\Rightarrow \mathrm{EW}(k+1)$, so the conjecture asserts $\mathrm{EW}(k)$ for some, hence all sufficiently large, $k$.

A complete proof must exhibit an explicit $k$ and prove injectivity of $x\mapsto(\operatorname{rad}(x),\dots,\operatorname{rad}(x+k))$ on all of $\mathbb{Z}_{>0}$. A disproof must produce, for **every** $k$, a pair $x\ne y$ agreeing on radicals across the whole block $[0,k]$ — a single sporadic pair refutes only one value of $k$.

## 2. Mathematical Foundations

Let $P(n)=\{p \text{ prime}: p\mid n\}$, so $\operatorname{rad}(n)=\prod_{p\in P(n)}p$ and $\operatorname{rad}(n)=\operatorname{rad}(m)\iff P(n)=P(m)$.

**Key divisibility lemma.** Suppose $\operatorname{rad}(x+i)=\operatorname{rad}(y+i)$ for $0\le i\le k$ and put $d=y-x\neq 0$. Since every prime of $x+i$ divides $y+i$,
$$\operatorname{rad}(x+i)\ \big|\ \gcd(x+i,\,y+i)\ \big|\ (y+i)-(x+i)=d \qquad (0\le i\le k).$$
Hence
$$L_k(x):=\operatorname{lcm}\big(\operatorname{rad}(x),\dots,\operatorname{rad}(x+k)\big)\ \Big|\ d, \qquad\text{so}\qquad |d|\ \ge\ L_k(x).$$
Because $\gcd(x+i,x+j)\mid (j-i)$, the radicals overlap only in primes $\le k$, giving
$$L_k(x)\ \ge\ \frac{1}{C_k}\prod_{i=0}^{k}\operatorname{rad}(x+i),\qquad C_k=\prod_{p\le k}p^{\,\lfloor k/p\rfloor}\ \ \text{(crude)} .$$
So the conjecture reduces to a **lower bound for radicals of blocks of consecutive integers**: if $\prod_{i\le k}\operatorname{rad}(x+i)$ is forced to exceed $\max(x,y)$, no admissible $d$ can exist.

**Related combinatorial notion.** $k$ is an **Erdős–Woods number** if there is $a\ge 1$ with
$$\forall i,\ 0<i<k:\quad \gcd(a,a+i)>1 \ \text{ or }\ \gcd(a+i,a+k)>1,$$
i.e. the interval $[a,a+k]$ is "prime-closed": every interior point shares a prime with an endpoint. Sequence: $16,22,34,36,46,56,64,66,70,\dots$ (OEIS A059756).

**Logical background.** Woods studied the structure $\langle \mathbb{N}; S,\perp\rangle$ with successor $S(x)=x+1$ and coprimeness $x\perp y\iff\gcd(x,y)=1$. The truth of the conjecture yields a first-order definition of addition (hence of multiplication) in this structure, making its theory undecidable; the blocks $(\operatorname{rad}(x+i))_{i\le k}$ act as finite "coordinates" pinning down $x$.

## 3. History & State of the Art (SOTA)

- **1980.** Erdős raises the question of pairs of blocks of consecutive integers with identical prime supports (*How many pairs of products of consecutive integers have the same prime factors?*, Amer. Math. Monthly 87 (1980), 391–392).
- **1981.** Alan R. Woods, in his Manchester PhD thesis *Some problems in logic and number theory, and their connections*, isolates the injectivity statement above, proves the implication to definability of $+$ from $(S,\perp)$, and introduces the prime-closed-interval condition. The thesis is the standard source; it was reissued in *New Studies in Weak Arithmetics* (CSLI Publications, 2013).
- **1985.** D. Richard obtains strong definability results in $\langle\mathbb{N};S,\perp\rangle$ (all arithmetical sets of prime powers are definable), showing the logical side is rich independently of the conjecture.
- **1989.** D. L. Dowe proves there are **infinitely many** Erdős–Woods numbers, settling the existence question for prime-closed intervals.
- **1996.** Balasubramanian, Langevin, Shorey and Waldschmidt give effective, Baker-type bounds on the length of two arithmetic progressions with identical prime divisors — the strongest unconditional finiteness input.
- **2003.** Cégielski, Héroult and Richard prove that the set of Erdős–Woods numbers is **recursive** (decidable).
- **Conditional SOTA.** Under the $abc$ conjecture, $\mathrm{EW}(2)$ holds for all but finitely many $x$ (Langevin-style argument; see §4 and §10). The polynomial analogue over $\mathbb{C}[t]$ follows from Mason–Stothers.

The unconditional conjecture is open for **every** $k\ge 2$: no unconditional proof for any $k$, and no counterexample for any $k\ge 2$.

## 4. Partial Results / Verified Cases

- **$k=1$ is false, with an explicit infinite family.** For $n\ge 2$, the pair $x=2^n-2$, $y=2^n(2^n-2)$ satisfies $\operatorname{rad}(x)=\operatorname{rad}(y)$ and $\operatorname{rad}(x+1)=\operatorname{rad}(y+1)$; e.g. $(2,8),(6,48),(14,224)$. Sporadic non-family pairs also exist, e.g. $(75,1215)$: $\operatorname{rad}=15$ for both, and $\operatorname{rad}(76)=\operatorname{rad}(1216)=38$. So $k\ge 2$ is necessary.
- **Conditional theorem ($abc$).** Assume $abc$. Then for every $\varepsilon>0$ there is $C(\varepsilon)$ with $\operatorname{rad}(x(x+1)(x+2))\ge C(\varepsilon)^{-1}x^{2-\varepsilon}$, obtained from $x(x+2)+1=(x+1)^2$. Combined with $L_2(x)\mid y-x$ this forces $y\gg y^{2-\varepsilon}$, impossible for large $y$: **$abc$ implies $\mathrm{EW}(2)$ outside a finite (ineffective) exceptional set.**
- **Function-field case, solved.** Over $\mathbb{C}[t]$ the same computation with the Mason–Stothers theorem ($\deg c\le \deg\operatorname{rad}(abc)-1$ for coprime $a+b=c$) gives the analogue of $\mathrm{EW}(2)$ unconditionally for non-constant polynomials.
- **Fixed $x$.** For each fixed $x$ and $k\ge 2$, the number of $y$ with matching radical blocks is finite and effectively boundable by linear forms in logarithms (Balasubramanian–Langevin–Shorey–Waldschmidt, 1996); the bounds are far too large for a uniform statement.
- **Erdős–Woods numbers.** Least value $k=16$, witnessed by $a=2184=2^3\cdot3\cdot7\cdot13$ with $a+16=2200=2^3\cdot5^2\cdot11$; infinitude proved (Dowe 1989); membership decidable (Cégielski–Héroult–Richard 2003).
- **Computation.** Exhaustive searches over blocks with $x$ in the ranges typically reported in the literature find no pair for $k\ge 2$; the precise search limit is not standardized in print *(verify before quoting a bound)*.

## 5. Principal Obstacles

- **No unconditional lower bound for $\operatorname{rad}$ of consecutive integers.** The whole problem collapses to proving $\prod_{i\le k}\operatorname{rad}(x+i)\gg x^{1+\delta}$ for some $k,\delta$. Unconditionally one can only say $\operatorname{rad}(n)\ge n^{o(1)}$-type statements fail badly: $\operatorname{rad}(n)$ can be as small as $n^{c/\log\log n}$, and nothing rules out several members of a short block being simultaneously near-powerful. This is exactly the strength of $abc$; no known technique reaches it.
- **Baker's method gives the wrong shape of bound.** Linear forms in logarithms bound $y$ in terms of $x$ and the number of primes involved, so results are of the form "for fixed $x$, finitely many $y$". Uniformity in $x$ would need a bound depending on $\log x$ only, which the theory does not provide.
- **Sieve and analytic density arguments miss.** Sieves control the *typical* factorization of a block, but a counterexample is an extremal event of density zero; upper-bound sieves cannot exclude sparse conspiracies, and the constraint "$\operatorname{rad}(x+i)\mid y-x$ for all $i$" is a multiplicative condition invisible to additive Fourier analysis.
- **Powerful-number obstruction.** Counterexamples require $x+i$ and $y+i$ to differ by a highly powerful factor for each $i$ simultaneously. Understanding powerful values of $x+i$ in short blocks is itself an open Diophantine problem (related to the $abc$-equivalent Hall and Szpiro conjectures).
- **The logical route no longer forces progress.** Because definability results in $\langle\mathbb{N};S,\perp\rangle$ were later obtained by other means, the conjecture lost its status as the unique gateway to those consequences, removing a source of technique transfer.

## 6. The Gap

Proven: $\mathrm{EW}(1)$ is false; $\mathrm{EW}(2)$ holds for large $x$ **assuming $abc$**; for each fixed $x$ only finitely many $y$ can match. Conjectured: a single $k$ works for **all** $x$, unconditionally.

The precise missing step is a uniform, unconditional lower bound
$$\operatorname{lcm}\big(\operatorname{rad}(x),\operatorname{rad}(x+1),\dots,\operatorname{rad}(x+k)\big)\;>\;x \qquad\text{for all } x>x_0(k),$$
for some fixed $k$. Everything else in the argument (§2) is elementary. Since $L_k(x)\mid y-x$, such a bound would force $|y-x|>x$ and, applied at $y$ as well, $|y-x|>y$ — a contradiction. Producing this bound for even one $k$ is equivalent in difficulty to a nontrivial case of $abc$-strength radical estimates; conversely no reduction is known that derives it from anything weaker.

## 7. Current Research (as of June 2026)

- **$abc$-conditional cascades.** Work continues on cataloguing consequences of $abc$ and of Szpiro-type inequalities for radicals of consecutive integers; the Erdős–Woods statement is a standard test case. Shinichi Mochizuki's IUT claim to $abc$ remains not accepted by the wider community, so all such consequences stay conditional *(frontier — verify)*.
- **Weak arithmetics / logic school (Paris-Est Créteil, LACL; the *Journées sur les Arithmétiques Faibles* community continuing Cégielski–Richard's programme).** Focus on decidability and definability in $\langle\mathbb{N};S,\perp\rangle$ and on refining the algorithm deciding Erdős–Woods numbers, including complexity of the decision procedure.
- **Computational number theory.** Distributed searches for radical-block collisions and for structured Erdős–Woods witnesses; the density of Erdős–Woods numbers below $N$ and the structure of minimal witnesses $a(k)$ are studied empirically *(frontier — verify)*.
- **Effective Diophantine analysis.** Continued sharpening of $p$-adic linear-form bounds (Shorey–Tijdeman school) applied to "same prime divisors" equations in arithmetic progressions.

## 8. Future Work

- Prove an unconditional bound $\operatorname{rad}(x(x+1)\cdots(x+k))\ge x^{1+\delta}$ for some explicit $k$ and $\delta>0$ — the single decisive target.
- Identify a **weaker-than-$abc$** hypothesis (e.g. an averaged or almost-all radical bound with a controlled exceptional set) that still suffices, then attack it with sieve or determinant methods.
- Extend the Mason–Stothers proof from $\mathbb{C}[t]$ to function fields of positive characteristic and to $\mathbb{Z}$-analogues via Arakelov/Belyi-type geometry, to see which step genuinely requires $abc$.
- Settle whether $\mathrm{EW}(2)$ can fail at all: search for or rule out counterexample families of the shape $y=x\cdot m$ with $\operatorname{rad}(m)\mid\operatorname{rad}(x)$, the mechanism that produces every known $k=1$ example.
- Determine the asymptotic density of Erdős–Woods numbers and the growth of the least witness $a(k)$.

## 9. Key References

- **[Foundational]** P. Erdős. *How many pairs of products of consecutive integers have the same prime factors?* American Mathematical Monthly **87** (1980), 391–392.
- **[Foundational]** A. R. Woods. *Some problems in logic and number theory, and their connections.* PhD thesis, University of Manchester, 1981; reprinted in *New Studies in Weak Arithmetics* (P. Cégielski, C. Cornaros, C. Dimitracopoulos, eds.), CSLI Publications, 2013.
- **[Foundational]** D. Richard. *All arithmetical sets of powers of primes are first-order definable in terms of the successor function and the coprimeness predicate.* Discrete Mathematics **53** (1985), 221–247.
- **[SOTA / Recent]** D. L. Dowe. *On the existence of sequences of co-prime pairs of integers.* Journal of the Australian Mathematical Society (Series A) **47** (1989), 84–89.
- **[SOTA / Recent]** R. Balasubramanian, M. Langevin, T. N. Shorey, M. Waldschmidt. *On the maximal length of two sequences of integers in arithmetic progressions with the same prime divisors.* Monatshefte für Mathematik **121** (1996), 295–307.
- **[SOTA / Recent]** P. Cégielski, F. Heroult, D. Richard. *On the amplitude of intervals of natural numbers whose every element has a common prime divisor with at least an extremity.* Theoretical Computer Science **303** (2003), 53–62.
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory*, 3rd edition, Springer, 2004 — problem **B29**.
- **[Survey]** T. N. Shorey, R. Tijdeman. *Exponential Diophantine Equations.* Cambridge Tracts in Mathematics 87, Cambridge University Press, 1986.

## 10. Worked Example / Concrete Special Case

**Why $k=1$ fails — an infinite family, verified.** Fix $n\ge 2$ and set
$$x=2^n-2,\qquad y=x(x+2)=2^n(2^n-2).$$

1. *Radicals at $i=0$.* $x=2(2^{n-1}-1)$ is even, and $x+2=2^n$ contributes only the prime $2$. Hence
 $$\operatorname{rad}(y)=\operatorname{rad}\big(x\cdot 2^n\big)=\operatorname{rad}(x)=2\operatorname{rad}(2^{n-1}-1).$$
2. *Radicals at $i=1$.* Algebraically $y+1=x(x+2)+1=(x+1)^2$, so
 $$\operatorname{rad}(y+1)=\operatorname{rad}(x+1)=\operatorname{rad}(2^n-1).$$
3. *Distinctness.* $y=x(x+2)>x$ for $x\ge1$.

Instances: $n=2:(2,8)$ with radicals $(2,3)$ and $(2,3)$; $n=3:(6,48)$ with $(6,7)$, since $48=2^4\cdot3$ and $49=7^2$; $n=4:(14,224)$ with $(14,15)$, since $224=2^5\cdot 7$ and $225=15^2$.

**Where the family dies at $i=2$.** $y+2=2^n(2^n-2)+2=2\big(2^{2n-1}-2^{n}+1\big)$, whose odd part $2^{2n-1}-2^n+1>1$ is not a power of $2$, while $x+2=2^n$ has $\operatorname{rad}(x+2)=2$. So $\operatorname{rad}(y+2)\neq\operatorname{rad}(x+2)$ and the pair is not a counterexample to $\mathrm{EW}(2)$. Every known $k=1$ counterexample breaks at the next term in this way.

**The conditional barrier, on the same example.** Take any hypothetical pair with $\operatorname{rad}(x+i)=\operatorname{rad}(y+i)$, $i=0,1,2$, $y>x$, $d=y-x$. By §2, $L_2(x)\mid d$, and the only prime shared between $x,x+1,x+2$ is a possible $2$ in $x$ and $x+2$, so
$$L_2(x)=\operatorname{rad}\big(x(x+1)(x+2)\big).$$
Apply $abc$ to $x(x+2)+1=(x+1)^2$ with $\gcd(x(x+2),1)=1$: for every $\varepsilon>0$,
$$(x+1)^2\ \ll_\varepsilon\ \operatorname{rad}\big(x(x+2)(x+1)^2\big)^{1+\varepsilon}=\operatorname{rad}\big(x(x+1)(x+2)\big)^{1+\varepsilon},$$
so $L_2(x)\gg_\varepsilon x^{2-\varepsilon}$ and likewise $L_2(y)=L_2(x)\gg_\varepsilon y^{2-\varepsilon}$. But $L_2(x)\mid d<y$, giving $y\gg_\varepsilon y^{2-\varepsilon}$ — false once $y$ exceeds a bound depending on $\varepsilon$. Unconditionally, the step $L_2(x)\gg x^{2-\varepsilon}$ is exactly what nobody can prove: that is the gap of §6 in one line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*