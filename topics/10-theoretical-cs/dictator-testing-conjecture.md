---
id: 10-theoretical-cs/dictator-testing-conjecture
title: "Dictator Testing Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dictator Testing Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/dictator-testing-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A *dictatorship test* is a randomized procedure that reads $q$ bits of the truth table of a Boolean function $f:\{-1,1\}^n\to\{-1,1\}$, applies a fixed predicate $P:\{-1,1\}^q\to\{0,1\}$ to the answers, and must accept every dictator $f(x)=x_i$ with high probability while rejecting every function that is "far from a dictator" (formalized as having all low influences).

**Dictator Testing Conjecture (optimality form).** For every predicate $P$ and every $q$, the smallest soundness achievable by a $q$-query dictatorship test using $P$ with **perfect completeness** equals the polynomial-time approximability threshold of $\mathrm{Max}\text{-}P$ on *satisfiable* instances. Equivalently: dictatorship tests are a complete characterization of CSP inapproximability, including in the perfect-completeness regime.

Two concrete sub-statements:

- **(C1)** For every $\varepsilon>0$ and every $P$, if a $q$-query perfectly complete dictatorship test with soundness $s$ exists, then it is NP-hard to distinguish satisfiable instances of $\mathrm{Max}\text{-}P$ from instances of value $\le s+\varepsilon$.
- **(C2)** Determine $s^\*(q)$, the optimal soundness of a non-adaptive $q$-query perfectly complete dictatorship test. Known: $s^\*(3)=5/8$. Open for all $q\ge 4$.

A complete resolution means either a proof of (C1) (currently known only under a *d*-to-1-type conjecture with perfect completeness), or a counterexample: a predicate whose optimal dictator test soundness is strictly below the true NP-hardness threshold.

## 2. Mathematical Foundations

Work in $L^2(\{-1,1\}^n,\mu_{\mathrm{unif}})$ with the Fourier–Walsh expansion
$$f(x)=\sum_{S\subseteq[n]}\hat f(S)\,\chi_S(x),\qquad \chi_S(x)=\prod_{i\in S}x_i,\qquad \sum_S \hat f(S)^2=\|f\|_2^2 .$$

**Influences.** $\mathrm{Inf}_i(f)=\sum_{S\ni i}\hat f(S)^2$ and the degree-$d$ truncation $\mathrm{Inf}_i^{\le d}(f)=\sum_{S\ni i,|S|\le d}\hat f(S)^2$.

**Noise operator and stability.** For $\rho\in[-1,1]$, $T_\rho f=\sum_S \rho^{|S|}\hat f(S)\chi_S$ and $\mathbb{S}_\rho(f)=\langle f,T_\rho f\rangle=\sum_S\rho^{|S|}\hat f(S)^2$.

**Test.** A $q$-query test $\mathcal{T}$ is a distribution $\mu$ on $(\{-1,1\}^q)$ applied coordinatewise to produce correlated inputs $x^{(1)},\dots,x^{(q)}\in\{-1,1\}^n$; it accepts iff $P(f(x^{(1)}),\dots,f(x^{(q)}))=1$.

- **Completeness** $c$: every dictator is accepted with probability $\ge c$. *Perfect completeness* is $c=1$, which forces $\mathrm{supp}(\mu)\subseteq P^{-1}(1)$.
- **Soundness** $s$: for all $\varepsilon>0$ there are $\tau>0,d\in\mathbb{N}$ such that $\max_i \mathrm{Inf}_i^{\le d}(f)\le\tau$ implies acceptance probability $\le s+\varepsilon$.

**Majority Is Stablest** (Mossel–O'Donnell–Oleszkiewicz 2010): if $\mathbb{E}[f]=0$ and $\max_i\mathrm{Inf}_i^{\le d}(f)\le\tau$, then for $\rho\in(0,1)$,
$$\mathbb{S}_\rho(f)\le 1-\tfrac{2}{\pi}\arccos\rho+o_{\tau,d}(1),$$
the value attained by $\mathrm{Maj}_n$. This and the underlying **invariance principle** convert low-influence Boolean analysis into Gaussian geometry.

**Pairwise independence** (Austrin–Mossel 2009): if $P^{-1}(1)$ supports a distribution $\mu$ with uniform, pairwise-independent marginals, then $P$ admits a perfectly complete dictator test with soundness $|P^{-1}(1)|/2^q$ — i.e. no better than a random assignment.

**Threshold for $q=3$.** Zwick (1998) gave an SDP-rounding algorithm satisfying $\ge 5/8$ of the constraints of any satisfiable $3$-CSP; $\mathrm{NTW}(a,b,c)=1$ unless exactly two of $a,b,c$ are $1$ has $|P^{-1}(1)|=5$, so $5/8$ is tight there.

## 3. History & State of the Art (SOTA)

- **1993.** Blum–Luby–Rubinfeld linearity test: the ancestor of all local Boolean-function tests.
- **1998.** Bellare–Goldreich–Sudan introduce the *long code* and folding, turning "test a codeword" into "test a dictator". Guruswami–Lewin–Sudan–Trevisan give a $4$-query PCP with perfect completeness and soundness $1/2$.
- **2001.** Håstad's *Some optimal inapproximability results*: $3$-query test with completeness $1-\varepsilon$ and soundness $1/2+\varepsilon$ (Max-3LIN), plus $7/8$ for Max-3SAT. Completeness is *not* perfect — the $\varepsilon$ is essential to his Fourier argument.
- **2002.** Khot's Unique Games Conjecture supplies the outer verifier that makes dictator tests generically composable.
- **2008.** Raghavendra: under UGC, for every CSP the optimal dictator test soundness equals the basic-SDP integrality gap equals the hardness threshold — the conjecture is a **theorem in the imperfect-completeness regime**.
- **2009.** O'Donnell–Wu construct a $3$-bit perfectly complete dictator test with soundness $5/8$ and prove $5/8$ is optimal among all $3$-bit perfectly complete tests; separately they derive $5/8$ hardness for satisfiable $3$-CSPs under Khot's $d$-to-$1$ conjecture.
- **2014.** Håstad proves NP-hardness of approximating Max-NTW beyond $5/8+\varepsilon$ on satisfiable instances, making the $q=3$ case unconditional.
- **2016.** Chan: for imperfect completeness, $\mathrm{Max}\text{-}q\text{-CSP}$ is NP-hard beyond $(q+1)/2^q$, matching Samorodnitsky–Trevisan.
- **2018.** Khot–Minzer–Safra prove the $2$-to-$2$ Games Theorem via near-perfect expansion of pseudorandom sets in the Grassmann graph — but only with completeness $1/2$, not $1$.

## 4. Partial Results / Verified Cases

- **$q=3$, perfect completeness: settled.** $s^\*(3)=5/8$ (O'Donnell–Wu upper bound on test quality; Zwick algorithmic matching; Håstad unconditional NP-hardness for NTW).
- **All predicates, imperfect completeness: settled under UGC.** Raghavendra's theorem, plus Austrin–Mossel's pairwise-independence criterion for approximation resistance.
- **All predicates, imperfect completeness, unconditional for $q$-ary parity-like predicates:** Chan's $(q+1)/2^q$.
- **$q=4$ perfect completeness:** soundness $1/2$ achieved (GLST 1998); best known lower bound on $s^\*(4)$ is far below.
- **Large $q$, perfect completeness:** Håstad–Khot achieve soundness $2^{-q+O(\sqrt q)}$ with $q$ queries; the conjectured truth is $\mathrm{poly}(q)\cdot 2^{-q}$.
- **Unique-Games-style tests ($2$ queries, alphabet $k$):** dictator tests are known to be optimal (Raghavendra, Khot–Kindler–Mossel–O'Donnell for Max-Cut, $\alpha_{GW}\approx0.878$).
- **Monotone / symmetric predicates:** for the class of predicates supporting a pairwise-independent *subgroup*, Chan gives unconditional resistance with imperfect completeness.

## 5. Principal Obstacles

- **Perfect completeness kills the noise.** Every known soundness analysis inserts a noise operator $T_\rho$, $\rho<1$, to kill high-degree Fourier mass; $T_\rho$ costs $\Omega(\varepsilon)$ completeness. With $c=1$ the test distribution must be supported inside $P^{-1}(1)$ and cannot be smoothed, so the high-degree tail is unbounded.
- **The invariance principle needs low degree.** MOO-type theorems apply to $\mathrm{Inf}_i^{\le d}$; without noise there is no way to reduce to degree $\le d$, and a function can be far from every dictator yet have a huge degree-$n$ term (e.g. $\chi_{[n]}$) that a perfectly complete test cannot penalize.
- **No perfect-completeness outer verifier.** UGC instances are inherently non-satisfiable-preserving. The $2$-to-$2$ Games Theorem has completeness $1/2$; the $d$-to-$1$ conjecture *with* perfect completeness is exactly the missing ingredient and remains open. The Grassmann-graph expansion machinery of Khot–Minzer–Safra does not currently yield the $1$-vs-$\varepsilon$ regime.
- **Algorithms interfere.** For satisfiable instances, propagation and SDP + local-consistency rounding (Zwick; Bhangale–Khot–Minzer) beat random assignment for many predicates, so soundness cannot simply equal $|P^{-1}(1)|/2^q$; the correct threshold has no clean combinatorial description for $q\ge4$.

## 6. The Gap

Proven: (i) the dictator-test-to-hardness translation when completeness is $1-\varepsilon$ (under UGC, and unconditionally for select predicates); (ii) the full picture for $q=3$ with perfect completeness. Conjectured: the same translation with $c=1$ for all $q\ge4$.

The exact missing step is a **satisfiability-preserving outer PCP**: a reduction from SAT to a $2$-prover game with perfect completeness, soundness $\varepsilon$, and $d$-to-$1$ (or "rich $2$-to-$1$") projection constraints, whose smoothness suffices to compose with a perfectly complete inner dictator test. Every existing route either sacrifices completeness (parallel repetition with noise, $2$-to-$2$ theorem) or sacrifices soundness. A second, independent gap is the *combinatorial* one: no formula or algorithm is known for $s^\*(q)$, $q\ge4$, even non-constructively.

## 7. Current Research (as of June 2026)

- **Satisfiable $k$-CSPs.** The Bhangale–Khot–Minzer program ("On approximability of satisfiable $k$-CSPs", STOC 2022–2024) develops analysis of Boolean functions over *product* and *non-product* correlated spaces without noise — a direct attack on the perfect-completeness barrier. Their structure theorems for $3$-wise correlations are the most promising new tool. *(frontier — verify)*
- **Grassmann/Johnson expansion.** Groups at NYU (Khot, Minzer), Tel Aviv (Safra), and Weizmann continue pushing toward $d$-to-$1$ with perfect completeness via higher-dimensional expansion. *(frontier — verify)*
- **Sum-of-squares lower bounds.** CMU/Berkeley/Princeton work on SoS degree lower bounds for satisfiable CSPs provides unconditional evidence matching conjectured dictator-test thresholds.
- **Rounding algorithms.** Improved SDP + propagation algorithms for satisfiable $4$-CSPs are being used to *disprove* candidate optimal soundness values, narrowing $s^\*(4)$ from above.

## 8. Future Work

- Settle $s^\*(4)$: construct a perfectly complete $4$-query test with soundness $<1/2$, or prove $1/2$ optimal.
- Prove the $d$-to-$1$ conjecture with perfect completeness; this immediately gives (C1) for a wide class of predicates.
- Develop a noise-free invariance principle: identify a pseudorandomness condition weaker than low degree-$d$ influence that still forces Gaussian behavior.
- Classify *hereditarily approximation resistant* predicates (resistant even on satisfiable instances), extending Håstad's NTW result and the Chan classification.
- Determine whether the perfect-completeness soundness is $\Theta(q^2/2^q)$ or $2^{-q+\omega(1)\sqrt q}$ for large $q$.

## 9. Key References

- **[Foundational]** M. Blum, M. Luby, R. Rubinfeld. *Self-Testing/Correcting with Applications to Numerical Problems.* Journal of Computer and System Sciences 47(3), 1993.
- **[Foundational]** M. Bellare, O. Goldreich, M. Sudan. *Free Bits, PCPs, and Nonapproximability — Towards Tight Results.* SIAM Journal on Computing 27(3), 1998.
- **[Foundational]** J. Håstad. *Some Optimal Inapproximability Results.* Journal of the ACM 48(4), 2001.
- **[Foundational]** U. Zwick. *Approximation Algorithms for Constraint Satisfaction Problems Involving at Most Three Variables per Constraint.* SODA 1998.
- **[Foundational]** S. Khot. *On the Power of Unique 2-Prover 1-Round Games.* STOC 2002.
- **[Foundational]** E. Mossel, R. O'Donnell, K. Oleszkiewicz. *Noise Stability of Functions with Low Influences: Invariance and Optimality.* Annals of Mathematics 171(1), 2010.
- **[SOTA]** R. O'Donnell, Y. Wu. *3-Bit Dictator Testing: 1 vs. 5/8.* SODA 2009.
- **[SOTA]** R. O'Donnell, Y. Wu. *Conditional Hardness for Satisfiable 3-CSPs.* STOC 2009.
- **[SOTA]** J. Håstad. *On the NP-Hardness of Max-Not-2.* SIAM Journal on Computing 43(1), 2014.
- **[SOTA]** S. O. Chan. *Approximation Resistance from Pairwise-Independent Subgroups.* Journal of the ACM 63(3), 2016.
- **[SOTA]** P. Austrin, E. Mossel. *Approximation Resistant Predicates from Pairwise Independence.* Computational Complexity 18(2), 2009.
- **[SOTA]** S. Khot, D. Minzer, M. Safra. *Pseudorandom Sets in Grassmann Graph Have Near-Perfect Expansion.* FOCS 2018.
- **[SOTA]** J. Håstad, S. Khot. *Query Efficient PCPs with Perfect Completeness.* Theory of Computing 1, 2005.
- **[Survey]** R. O'Donnell. *Analysis of Boolean Functions.* Cambridge University Press, 2014.
- **[Survey]** P. Raghavendra. *Optimal Algorithms and Inapproximability Results for Every CSP?* STOC 2008.

## 10. Worked Example / Concrete Special Case

**The NTW test at $q=3$.** Let $\mathrm{NTW}(a,b,c)=0$ iff exactly two of $a,b,c$ equal $+1$; so $|\mathrm{NTW}^{-1}(1)|=5$.

*Step 1 — Fourier expansion of the predicate.* Let $g$ be the indicator of "exactly two $+1$s", supported on $(1,1,-1),(1,-1,1),(-1,1,1)$. Then $\hat g(\emptyset)=3/8$, $\hat g(\{i\})=1/8$, $\hat g(\{i,j\})=-1/8$, $\hat g(\{1,2,3\})=-3/8$, so
$$\mathrm{NTW}(a,b,c)=1-g=\tfrac58-\tfrac18(a+b+c)+\tfrac18(ab+bc+ca)+\tfrac38\,abc .$$

*Step 2 — the test distribution.* Draw each coordinate triple $(x_i,y_i,z_i)$ uniformly from the four points with $x_iy_iz_i=+1$: $(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)$. All four lie in $\mathrm{NTW}^{-1}(1)$, marginals are uniform, and the distribution is pairwise independent: $\mathbb{E}[x_i]=0$, $\mathbb{E}[x_iy_i]=0$, while $\mathbb{E}[x_iy_iz_i]=1$.

*Step 3 — completeness.* For $f=$ dictator $x_i$, the answers are exactly $(x_i,y_i,z_i)$, always in the support, so acceptance probability is $1$. Perfect completeness holds.

*Step 4 — soundness.* Take $f$ folded, so $\mathbb{E}[f]=0$. Pairwise independence gives $\mathbb{E}[f(x)f(y)]=\sum_S\hat f(S)^2\,\mathbb{E}[\chi_S(x)\chi_S(y)]=0$, and likewise for the other pairs. For the triple term, $\mathbb{E}[\chi_S(x)\chi_T(y)\chi_U(z)]=1$ iff $S=T=U$, so
$$\mathbb{E}\big[f(x)f(y)f(z)\big]=\sum_S \hat f(S)^3 .$$
Hence acceptance probability $=\tfrac58+\tfrac38\sum_S\hat f(S)^3$.

*Step 5 — reading off the gap.* For the dictator, $\sum_S\hat f(S)^3=1$ and the value is $1$. For $f=\mathrm{Maj}_n$, $\big|\sum_S\hat f(S)^3\big|\le\max_S|\hat f(S)|=\Theta(n^{-1/2})\to0$, giving $5/8+o(1)$. More generally $\big|\sum_S\hat f(S)^3\big|\le\max_S|\hat f(S)|$, which is small for any function with no large Fourier coefficient — the low-influence regime. So the test separates $1$ from $5/8+\varepsilon$.

The residual difficulty is exactly the perfect-completeness barrier of Section 5: bounding $\max_S|\hat f(S)|$ for *all* low-influence $f$, including $f=\chi_{[n]}$ (for which $\sum_S\hat f(S)^3=1$ and the test accepts with probability $1$), requires folding plus a noise or degree-truncation step that this test cannot afford. O'Donnell–Wu repair this with a carefully weighted mixture supported inside $\mathrm{NTW}^{-1}(1)$; matching that repair for $q\ge4$ is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*