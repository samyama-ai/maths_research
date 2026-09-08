---
id: 01-number-theory/erdos-conjecture-on-arithmetic-progressions
title: "Erdos Conjecture on Arithmetic Progressions"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Conjecture on Arithmetic Progressions

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-conjecture-on-arithmetic-progressions` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Erdős–Turán, 1936; Erdős' $5000 problem).** Let $A \subseteq \mathbb{N}$ satisfy
$$\sum_{a \in A} \frac{1}{a} = \infty .$$
Then $A$ contains arbitrarily long finite arithmetic progressions: for every $k \ge 3$ there exist $a, d \in \mathbb{N}$, $d \ge 1$, with $a, a+d, \dots, a+(k-1)d \in A$.

The claim is purely about the *size* of $A$ measured by its harmonic series; no structural, algebraic or regularity hypothesis is imposed. A complete proof must handle every $k$ uniformly (the statement for fixed $k$ is the "$k$-AP case"). A disproof requires exhibiting, for some fixed $k$, a set $A$ with divergent reciprocal sum and no $k$-term progression.

The conjecture is strictly stronger than Szemerédi's theorem: positive upper density implies divergence, but not conversely (the primes have zero density and divergent reciprocal sum).

## 2. Mathematical Foundations

For $N \in \mathbb{N}$ and $k \ge 3$ define the **extremal function**
$$r_k(N) = \max\{ |A| : A \subseteq \{1,\dots,N\},\ A \text{ contains no } k\text{-term arithmetic progression}\},$$
and $\delta_k(N) = r_k(N)/N$.

**Szemerédi's theorem (1975).** $\delta_k(N) \to 0$ as $N \to \infty$ for every $k \ge 3$.

**Reduction of the conjecture to a rate.** The Erdős conjecture for a given $k$ follows from any bound of the form
$$r_k(N) \;\ll_k\; \frac{N}{(\log N)^{1+c}}, \qquad c = c(k) > 0. \tag{$\star$}$$
Proof sketch: if $A$ is $k$-AP-free, split into dyadic blocks $A_n = A \cap [2^n, 2^{n+1})$. Each $A_n$ is $k$-AP-free, so $|A_n| \le r_k(2^{n+1})$ and
$$\sum_{a \in A} \frac1a \le \sum_{n \ge 0} \frac{|A_n|}{2^n} \ll \sum_{n\ge 1} \frac{1}{n^{1+c}} < \infty .$$
Thus $(\star)$ contradicts divergence. Conversely, $(\star)$ is not formally necessary — the conjecture could hold with a slower rate along sparse scales — but every known route passes through it.

**Fourier/Gowers framework.** For $f : \mathbb{Z}/N\mathbb{Z} \to \mathbb{C}$, $\widehat{f}(\xi) = \sum_x f(x) e(-x\xi/N)$. Counting 3-APs is a trilinear Fourier expression,
$$\Lambda_3(f) = \frac{1}{N^2}\sum_{x,d} f(x)f(x+d)f(x+2d) = \frac{1}{N^3}\sum_{\xi} \widehat f(\xi)^2 \overline{\widehat f(2\xi)} .$$
For $k \ge 4$ linear Fourier analysis does not control $\Lambda_k$; one uses the **Gowers uniformity norms**
$$\|f\|_{U^s}^{2^s} = \mathbb{E}_{x, h_1, \dots, h_s} \prod_{\omega \in \{0,1\}^s} \mathcal{C}^{|\omega|} f\!\left(x + \omega \cdot h\right),$$
with $\mathcal C$ complex conjugation. Counting $k$-APs is controlled by $\|f\|_{U^{k-1}}$, and the **inverse theorem** (Green–Tao–Ziegler) states that $\|f\|_{U^{s+1}} \ge \delta$ forces correlation $\ge c(\delta)$ with a nilsequence $F(g(n)\Gamma)$ on an $s$-step nilmanifold $G/\Gamma$. The quantitative shape of $c(\delta)$ is what dictates the final bound on $r_k(N)$.

**Behrend's construction (1946).** Points of $\{0,\dots,m-1\}^d$ on a sphere $\sum x_i^2 = R$, read in base $2m$, are 3-AP-free, giving
$$r_3(N) \;\ge\; N \exp\!\left(-c\sqrt{\log N}\right).$$

## 3. History & State of the Art (SOTA)

- **1936** — Erdős and Turán, *On some sequences of integers*, conjecture $\delta_k(N)\to 0$ and pose the reciprocal-sum question.
- **1946** — Behrend's lower bound; Rankin (1961) extends it to $k$-APs: $r_k(N) \ge N\exp(-c(\log N)^{1/(k-1)})$.
- **1953** — Roth: $r_3(N) \ll N/\log\log N$, by the Fourier density-increment method.
- **1975** — Szemerédi proves the general case combinatorially (regularity lemma), with tower-type bounds.
- **1977** — Furstenberg's ergodic-theoretic proof via multiple recurrence; no effective bound.
- **2001** — Gowers: $r_k(N) \ll N (\log\log N)^{-c_k}$, $c_k = 2^{-2^{k+9}}$, the first effective bound for all $k$.
- **2008** — Green–Tao: the primes contain arbitrarily long APs — the flagship *instance* of the conjecture, not a proof of it.
- **2020** — Bloom–Sisask break the logarithmic barrier: $r_3(N) \ll N/(\log N)^{1+c}$. **This settles the $k=3$ case of the Erdős conjecture.**
- **2023** — Kelley–Meka: $r_3(N) \le N\exp(-c(\log N)^{1/11})$, near-Behrend; refined by Bloom–Sisask to exponent $1/9$.
- **2024** — Leng–Sah–Sawhney: $r_k(N) \ll N \exp(-(\log\log N)^{c_k})$ for all $k$, built on quasipolynomial inverse theorems for $U^{s+1}$.

## 4. Partial Results / Verified Cases

- **$k = 3$: proved.** Bloom–Sisask (2020) give $c > 0$ with $r_3(N) \ll N (\log N)^{-1-c}$; by the dyadic argument of §2 every $A$ with divergent $\sum 1/a$ contains a 3-AP. Kelley–Meka/Bloom–Sisask push this to $\exp(-c(\log N)^{1/9})$, within a power of Behrend's $\exp(-c(\log N)^{1/2})$.
- **The primes and dense subsets of the primes:** Green–Tao (2008) and Tao–Ziegler (polynomial patterns, 2008). Any $A \subseteq \mathbb{P}$ with $|A \cap [N]| \gg \pi(N)$ contains arbitrarily long APs.
- **Positive upper density:** Szemerédi's theorem covers all $A$ with $\limsup |A\cap[N]|/N > 0$.
- **Sets of density $\gg 1/(\log N)^{1-\varepsilon}$**: covered for $k=3$ by Roth-type bounds, and for all $k$ only in the far weaker regime $\gg (\log\log N)^{-c_k}$ (Gowers) / $\exp(-(\log\log N)^{c_k})$ (Leng–Sah–Sawhney).
- **Structured sparse sets:** $\{n : n \text{ squarefree}\}$, shifted primes $\mathbb{P}-1$, values of Chebotarev-type sets, and random sets of density $\ge N^{-1/(k-1)+\varepsilon}$ (Conlon–Gowers, Schacht: relative Szemerédi in random hosts) all contain long APs.
- **Consistency checks:** sets with convergent reciprocal sum such as squares, $k$th powers, and Behrend sets inside a *single* scale impose no constraint.

## 5. Principal Obstacles

- **The logarithmic threshold is the natural barrier.** Divergence of $\sum_{a\in A} 1/a$ is exactly the failure of $|A\cap[N]| \ll N/(\log N)^{1+c}$ on average over dyadic scales. All density-increment schemes lose a factor at each iteration; for $k\ge4$ the loss per step is governed by the inverse theorem's quantitative dependence, which is currently *quasipolynomial* — $c(\delta) = \exp(-(\log 1/\delta)^{O(1)})$ — and this compounds into $\log\log$-type savings, not $\log$-type.
- **Fourier analysis is blind for $k\ge4$.** The set $\{n : \|n^2\alpha\| < \varepsilon\}$ is Fourier-uniform yet has anomalous 4-AP counts, so one must run the argument over nilmanifolds; controlling the complexity (dimension, Lipschitz constants) of the nilsequences produced across many increments is where quantitative bleeding occurs.
- **Behrend obstruction.** Any proof must be compatible with $r_3(N) \ge N e^{-c\sqrt{\log N}}$, so the target is a narrow window: better than $(\log N)^{-1}$, impossible to beat $e^{-c\sqrt{\log N}}$. There is little room for lossy arguments.
- **Ergodic proofs are non-quantitative.** Furstenberg-style correspondence discards all effectivity, and the conjecture is intrinsically quantitative.
- **Sparse transference needs a majorant.** The Green–Tao method requires a pseudorandom measure dominating the set (supplied for the primes by sieve weights). An arbitrary $A$ with divergent reciprocal sum carries no such envelope.

## 6. The Gap

Proved: $k=3$ in full, and $k \ge 4$ only for densities down to $\exp(-(\log\log N)^{c_k})$. Required: densities down to $(\log N)^{-1-c}$. The concrete missing step for $k=4$ is a Roth-type bound
$$r_4(N) \ll \frac{N}{(\log N)^{1+c}},$$
which would need either (i) an inverse theorem for $U^3$ with *polynomial* dependence — correlation $\ge \delta^{O(1)}$ with a 2-step nilsequence of complexity $\delta^{-O(1)}$ — or (ii) a Kelley–Meka-style "sifted/almost-periodicity" argument extended past the trilinear setting. Kelley–Meka's method is intrinsically about 3-APs (it exploits the convolution structure of $1_A * 1_A$); no higher-order analogue is known. Even granting all $k$ individually, uniformity in $k$ is a further (mild) step, since the conjecture quantifies over all $k$ for a *single* set.

## 7. Current Research (as of June 2026)

- **Quantitative higher-order Fourier analysis.** Leng, Sah and Sawhney (MIT/Oxford/Columbia circles) obtained quasipolynomial inverse theorems for $U^{s+1}[N]$ and the resulting $r_k(N) \ll N\exp(-(\log\log N)^{c_k})$; work continues on removing the second logarithm. *(frontier — verify)*
- **Extending Kelley–Meka.** Groups around Bloom (Manchester/Oxford), Sisask (Stockholm), Peluse, Kelley and Meka are testing whether the spread/sifting technology admits a $U^3$ analogue; partial transfers exist for corners and for $\{x, x+d, x+d^2\}$-type configurations (Peluse, Prendiville). *(frontier — verify)*
- **Model settings.** $\mathbb{F}_q^n$ analogues (Croot–Lev–Pach–Ellenberg–Gijswijt polynomial method for 3-APs) remain unextended to $k=4$; understanding this obstruction is an active testbed.
- **Nilsequence complexity.** Manners' quantitative inverse theorem and subsequent refinements are being sharpened toward polynomial bounds — the single input that would upgrade $k=4$ to $\log$-type savings.
- **Special sets.** Ongoing work on APs in $\mathbb{P}$-like sets, Piatetski-Shapiro primes and multiplicatively defined sparse sets tests the conjecture in the divergent-but-zero-density regime.

## 8. Future Work

- Prove a polynomial-bound inverse theorem for the $U^3$ norm; this is the consensus prerequisite for $r_4(N) \ll N(\log N)^{-1-c}$ (Green, Tao, Manners).
- Develop a higher-order almost-periodicity / spread-regularity framework generalizing Kelley–Meka.
- Determine the true order of $r_3(N)$: close the gap between $\exp(-c(\log N)^{1/9})$ and Behrend's $\exp(-c(\log N)^{1/2})$; Erdős conjectured Behrend is essentially sharp.
- Attack weaker consequences: does divergence force *infinitely many* 3-APs with bounded common difference structure, or a 4-AP under an extra Fourier-uniformity hypothesis?
- Seek a counterexample construction for large $k$ by iterating Behrend/Rankin sets across scales — currently blocked by cross-scale progressions (see §10).

## 9. Key References

- **[Foundational]** P. Erdős, P. Turán. *On Some Sequences of Integers.* Journal of the London Mathematical Society **11** (1936), 261–264.
- **[Foundational]** K. F. Roth. *On Certain Sets of Integers.* Journal of the London Mathematical Society **28** (1953), 104–109.
- **[Foundational]** E. Szemerédi. *On sets of integers containing no $k$ elements in arithmetic progression.* Acta Arithmetica **27** (1975), 199–245.
- **[Foundational]** H. Furstenberg. *Ergodic behavior of diagonal measures and a theorem of Szemerédi on arithmetic progressions.* Journal d'Analyse Mathématique **31** (1977), 204–256.
- **[Foundational]** F. A. Behrend. *On sets of integers which contain no three terms in arithmetical progression.* Proceedings of the National Academy of Sciences USA **32** (1946), 331–332.
- **[SOTA]** T. Gowers. *A new proof of Szemerédi's theorem.* Geometric and Functional Analysis **11** (2001), 465–588.
- **[SOTA]** B. Green, T. Tao. *The primes contain arbitrarily long arithmetic progressions.* Annals of Mathematics **167** (2008), 481–547.
- **[SOTA]** T. F. Bloom, O. Sisask. *Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions.* arXiv:2007.03528, 2020.
- **[SOTA / Recent]** Z. Kelley, R. Meka. *Strong bounds for 3-progressions.* Proc. 64th IEEE Symposium on Foundations of Computer Science (FOCS), 2023; arXiv:2302.05537.
- **[SOTA / Recent]** T. F. Bloom, O. Sisask. *The Kelley–Meka bounds for sets free of three-term arithmetic progressions.* Essential Number Theory **2** (2023), 15–44.
- **[SOTA / Recent]** J. Leng, A. Sah, M. Sawhney. *Improved bounds for Szemerédi's theorem.* arXiv:2402.17995, 2024.
- **[Recent]** F. Manners. *Quantitative bounds in the inverse theorem for the Gowers $U^{s+1}$-norms over cyclic groups.* arXiv:1811.00718, 2018.
- **[Survey]** T. Tao, V. Vu. *Additive Combinatorics.* Cambridge Studies in Advanced Mathematics 105, Cambridge University Press, 2006.
- **[Survey]** P. Erdős. *Problems and results on combinatorial number theory.* In: A Survey of Combinatorial Theory, North-Holland, 1973.

## 10. Worked Example / Concrete Special Case

**(a) Why $(\star)$ settles $k=3$.** Bloom–Sisask give $r_3(N) \le C N (\log N)^{-1-c}$. Let $A$ be 3-AP-free and $A_n = A\cap[2^n,2^{n+1})$. Then $|A_n| \le r_3(2^{n+1}) \le C\,2^{n+1}/(n+1)^{1+c}(\log 2)^{1+c}$, so
$$\sum_{a\in A}\frac1a \;\le\; \sum_{n\ge0}\frac{|A_n|}{2^n} \;\le\; C' \sum_{n\ge 0}\frac{1}{(n+1)^{1+c}} \;<\; \infty .$$
Contrapositive: divergence forces a 3-AP. $\blacksquare$

**(b) Why the obvious counterexample fails.** Try to build a 3-AP-free set with divergent reciprocal sum by concatenating Behrend sets. Let $B_n \subseteq [2^n, 2^{n+1})$ be a Behrend set, $|B_n| \ge 2^n e^{-c\sqrt{n\log 2}}$, each 3-AP-free. Put $A = \bigcup_n B_n$. Then
$$\sum_{a\in A}\frac1a \;\ge\; \sum_n \frac{|B_n|}{2^{n+1}} \;\ge\; \tfrac12\sum_n e^{-c'\sqrt{n}},$$
and by the integral test $\int_1^\infty e^{-c'\sqrt{t}}\,dt = \frac{2}{c'^2}(1+c')e^{-c'} \cdot$ — finite. Wait: substituting $t = u^2$, $\int_1^\infty e^{-c'\sqrt t}dt = 2\int_1^\infty u e^{-c'u}du < \infty$. So the sum **converges**, and this construction never even reaches the hypothesis.

This is the sharp arithmetic content of the conjecture: Behrend's density $e^{-c\sqrt{\log N}}$ is *below* the divergence threshold $1/\log N$, since $e^{-c\sqrt{\log N}} \cdot \log N \to \infty$ — i.e. Behrend sets are far *denser* than $1/\log N$ per scale, yet the reciprocal sum computed above still converges because the block sum $|B_n|/2^n$ decays like $e^{-c'\sqrt n}$ while divergence needs $\gtrsim 1/n$. Any putative counterexample must therefore be at least as dense as $N/(\log N)\cdot$ (per scale, up to $\log\log$ factors) — comfortably above Behrend, and for $k=3$ now ruled out.

**(c) The primes.** $\sum_{p \le N} 1/p = \log\log N + M + o(1)$ (Mertens) diverges, so the conjecture predicts arbitrarily long prime APs — confirmed by Green–Tao. Explicitly, $5, 11, 17, 23, 29$ is a 5-AP of primes with $d=6$; the known record configurations reach $k=27$. The conjecture asserts this behaviour is forced by size alone, with no use of the multiplicative structure that Green–Tao exploit.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*