---
id: 10-theoretical-cs/junta-testing-complexity
title: "Junta Testing Complexity"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Junta Testing Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/junta-testing-complexity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A function $f:\{0,1\}^n \to \{0,1\}$ is a **$k$-junta** if there is a set $J \subseteq [n]$ with $|J| \le k$ such that $f(x)$ depends only on $x_J$. The **junta testing problem** asks for the minimum number of black-box queries to $f$ needed to distinguish

- $f$ is a $k$-junta, from
- $f$ is $\varepsilon$-far from every $k$-junta, i.e. $\mathrm{dist}(f, g) := \Pr_{x \sim \{0,1\}^n}[f(x) \ne g(x)] > \varepsilon$ for every $k$-junta $g$,

with error probability $\le 1/3$, and with query complexity **independent of $n$**.

Open questions, in decreasing order of centrality:

1. **Exact $\varepsilon$-dependence (adaptive).** Is the adaptive complexity $\Theta(k\log k + k/\varepsilon)$ for all $\varepsilon$, or can the additive $k/\varepsilon$ term be improved (e.g. to $k + \frac{1}{\varepsilon}\mathrm{polylog}$) for small $\varepsilon$?
2. **Non-adaptive $\varepsilon$-dependence.** The bounds $O(k^{3/2}/\varepsilon)$ and $\tilde\Omega(k^{3/2})$ leave the joint $(k,\varepsilon)$ trade-off unresolved.
3. **Tolerant junta testing.** What is the complexity of distinguishing $\mathrm{dist}(f,\mathcal{J}_k)\le \varepsilon_1$ from $\mathrm{dist}(f,\mathcal{J}_k) \ge \varepsilon_2$? Is a $\mathrm{poly}(k,1/\varepsilon)$-query tolerant tester possible, or is $2^{\Theta(\sqrt{k})}$ the truth?

A complete resolution means matching upper and lower bounds (up to constants, or at worst $\mathrm{polylog}$ factors) in $k$ *and* $\varepsilon$ for each of the adaptive, non-adaptive, and tolerant regimes.

## 2. Mathematical Foundations

Write $\mathcal{J}_k^n$ for the class of $k$-juntas on $n$ variables; $|\mathcal{J}_k^n| \le \binom{n}{k}2^{2^k}$. Identify range $\{0,1\}$ with $\{-1,1\}$ when convenient and use the **Fourier–Walsh expansion**

$$f(x) = \sum_{S \subseteq [n]} \hat f(S)\,\chi_S(x), \qquad \chi_S(x) = \prod_{i\in S}(-1)^{x_i}, \qquad \hat f(S) = \mathbb{E}_x[f(x)\chi_S(x)].$$

Parseval: $\sum_S \hat f(S)^2 = 1$ for Boolean-valued $f$.

**Influence.** For $i \in [n]$, $\mathrm{Inf}_i[f] = \Pr_x[f(x) \ne f(x^{\oplus i})]$, where $x^{\oplus i}$ flips coordinate $i$. For $\pm1$-valued $f$, $\mathrm{Inf}_i[f] = \sum_{S \ni i} \hat f(S)^2$. For a block $I \subseteq [n]$ the **block influence** is

$$\mathrm{Inf}_I[f] \;=\; \mathbb{E}_{x_{\bar I}}\!\big[\mathrm{Var}_{x_I}[f]\big] \;=\; \sum_{S \cap I \neq \emptyset} \hat f(S)^2 .$$

**Independence test on $I$** (the primitive underlying every classical tester): draw $x,y$ uniform, set $z$ with $z_I = y_I$, $z_{\bar I} = x_{\bar I}$, and reject if $f(x) \ne f(z)$. Then

$$\Pr[\text{reject}] = \tfrac12 \,\mathrm{Inf}_I[f] \quad (\pm1\text{ scaling}), \qquad \text{so } \Pr[\text{reject}] = 0 \iff f \text{ does not depend on } I .$$

**Junta approximation.** $f$ is $\varepsilon$-close to a $k$-junta iff there is $J$, $|J|\le k$, with $\mathrm{Inf}_{\bar J}[f] \le O(\varepsilon)$; the optimal $J$-junta approximant is $g(x) = \mathrm{sign}\big(\mathbb{E}_{y}[f(x_J, y_{\bar J})]\big)$, and $\mathrm{dist}(f,g) \le \mathrm{Inf}_{\bar J}[f]$ up to a factor 2. This makes junta testing equivalent to deciding whether the influence mass can be concentrated on $k$ coordinates.

**Structural tool (Friedgut).** Every Boolean $f$ is $\varepsilon$-close to a $2^{O(\mathrm{Inf}[f]/\varepsilon)}$-junta, where $\mathrm{Inf}[f]=\sum_i \mathrm{Inf}_i[f]$ — the reason junta structure is robust enough to test.

**Communication-complexity bridge.** Blais–Brody–Matulef: a $q$-query tester for property $\mathcal{P}$ yields a randomized communication protocol of cost $O(q\cdot c)$ for a related problem, so $\mathrm{CC}$ lower bounds (e.g. $\Omega(k\log k)$ for set-disjointness-like promise problems) transfer to query lower bounds.

## 3. History & State of the Art (SOTA)

- **2002–2004.** Fischer, Kindler, Ron, Safra, Samorodnitsky introduce junta testing ("Testing juntas", FOCS 2002 / JCSS 2004). They give an $\tilde O(k^2)/\varepsilon$-query non-adaptive tester based on randomly partitioning $[n]$ into $\mathrm{poly}(k)$ blocks and running independence tests, and an $\Omega(\sqrt{k})$ lower bound. This established that junta testing is possible with complexity independent of $n$ — the founding result of testing for "structural" function classes.
- **2004.** Chockler and Gutfreund prove an $\Omega(k)$ lower bound for adaptive testers.
- **2008.** Blais gives a non-adaptive tester with $\tilde O(k^{3/2})/\varepsilon$ queries.
- **2009.** Blais ("Testing juntas nearly optimally", STOC 2009) gives an **adaptive** tester with $O(k\log k + k/\varepsilon)$ queries, using binary search over blocks to identify influential coordinates.
- **2011/2012.** Blais, Brody, Matulef prove $\Omega(k\log k)$ for adaptive testing via communication complexity, matching Blais's upper bound for constant $\varepsilon$.
- **2017/2018.** Chen, Servedio, Tan, Waingarten, Xie prove a $\tilde\Omega(k^{3/2})$ **non-adaptive** lower bound, settling the non-adaptive complexity at $\tilde\Theta(k^{3/2})$ for constant $\varepsilon$ and separating adaptive from non-adaptive testing by a polynomial factor.
- **2018.** Sağlam (FOCS 2018) gives a new, tight $\Omega(k\log k)$ lower bound via near-log-convexity of heat-flow quantities, with cleaner constants and broader applicability.
- **2018–2021.** Tolerant and distribution-free variants become the frontier: distribution-free testing (Liu–Chen–Servedio–Sheng–Xie, Bshouty) and junta-distance approximation (De–Mossel–Neeman; Iyer–Tal–Whitmeyer).

## 4. Partial Results / Verified Cases

| Regime | Upper bound | Lower bound | Status |
|---|---|---|---|
| Adaptive, constant $\varepsilon$ | $O(k\log k)$ (Blais 2009) | $\Omega(k\log k)$ (BBM 2012; Sağlam 2018) | **Settled** |
| Adaptive, general $\varepsilon$ | $O(k\log k + k/\varepsilon)$ | $\Omega(k\log k)$, $\Omega(1/\varepsilon)$ | Open in $\varepsilon$ |
| Non-adaptive, constant $\varepsilon$ | $\tilde O(k^{3/2})$ (Blais 2008) | $\tilde\Omega(k^{3/2})$ (CSTWX 2017) | **Settled up to logs** |
| One-sided non-adaptive | $\tilde O(k^{3/2})$ | $\Omega(k \log k)$ | Partially settled |
| $k = 1$ (dictator/constant) | $\Theta(1/\varepsilon)$ | $\Omega(1/\varepsilon)$ | **Settled** |
| $k = O(1)$ | $\Theta(1/\varepsilon)$ | matching | **Settled** |
| Distribution-free, adaptive | $\tilde O(k/\varepsilon)$ (Bshouty 2019) | $\Omega(k)$ | Near-settled |
| Distribution-free, non-adaptive | — | $2^{\Omega(k^{1/3})}$ (LCSSX 2018) | Exponential separation proved |
| Quantum | $\tilde O(\sqrt{k/\varepsilon})$ (ABRW 2016) | $\Omega(\sqrt{k})$ | Near-settled in $k$ |
| Tolerant ($\varepsilon$ vs. $2\varepsilon$) | $2^{\tilde O(\sqrt{k})}/\varepsilon^2$ (Iyer–Tal–Whitmeyer 2021) | $\mathrm{poly}(k)$ only | **Open**, exponential gap |

Additional settled special cases: testing juntas over arbitrary **product distributions** with $\mathrm{poly}(k)/\varepsilon$ queries; testing juntas on non-Boolean domains $[m]^n$ with the same $\tilde O(k^{3/2})$ behaviour; testing whether $f$ is a $k$-junta *within* a known structured class (e.g. symmetric functions, monotone functions) in $O(k/\varepsilon)$ queries.

## 5. Principal Obstacles

- **Fourier analysis is lossy at the block level.** All classical testers detect only whether $\mathrm{Inf}_I[f] > 0$ or is large. This "influence oracle" view is provably weaker than full query access: the $\tilde\Omega(k^{3/2})$ non-adaptive bound shows random-block schemes are optimal, so improving the non-adaptive bound requires abandoning the influence primitive entirely — and no other primitive with $n$-independent cost is known.
- **Adaptivity is hard to lower-bound.** The $\Omega(k\log k)$ bound comes from communication complexity, which converts a $q$-query tester into a protocol; the conversion loses the $\varepsilon$-dependence, because the hard distributions used (random parities on $k$ vs. $2k$ coordinates) are already $\Theta(1)$-far. No known hard-instance family simultaneously encodes $\log k$-bits-per-query information *and* fine distance granularity $\varepsilon$.
- **Tolerance breaks the "zero influence" dichotomy.** In tolerant testing one must *estimate* $\min_{|J|\le k}\mathrm{Inf}_{\bar J}[f]$, a submodular-like minimization over $\binom{n}{k}$ sets. Greedy selection by individual influence fails: parity-like functions have all $\mathrm{Inf}_i$ equal while the optimal $J$ is highly non-uniform. The $2^{\tilde O(\sqrt{k})}$ barrier arises from the need to enumerate "cores" of size $\sqrt{k}$ in the Iyer–Tal–Whitmeyer analysis, and no lower bound rules out $\mathrm{poly}(k)$.
- **Hypercontractivity gives only crude concentration.** Friedgut-type theorems yield junta size $2^{O(\mathrm{Inf}/\varepsilon)}$ — exponential in the parameter — so they cannot be used to certify a $k$-junta approximant at the granularity testing demands.
- **Distribution-free obstacles.** Without the uniform measure, influence has no Fourier meaning; the $2^{\Omega(k^{1/3})}$ non-adaptive lower bound shows this is a real, not technical, barrier.

## 6. The Gap

Section 4 pins the constant-$\varepsilon$ complexity at $\Theta(k\log k)$ (adaptive) and $\tilde\Theta(k^{3/2})$ (non-adaptive). Section 1 asks for the full two-parameter function $q(k,\varepsilon)$. The precise missing steps:

1. **A lower bound of the form $\Omega(k/\varepsilon)$ (or an $o(k/\varepsilon)$ algorithm).** Currently only $\Omega(k\log k + 1/\varepsilon)$ is known; the truth could be $\Theta(k\log k + 1/\varepsilon)$, an additive $k$-factor gap for small $\varepsilon$.
2. **A tolerant lower bound beyond $\mathrm{poly}(k)$.** Between $\mathrm{poly}(k)$ and $2^{\tilde O(\sqrt{k})}$ there is an exponential gap. Closing it needs either a $\mathrm{poly}(k,1/\varepsilon)$ algorithm — which would require a fundamentally new way to certify near-junta structure without core enumeration — or a lower-bound technique that survives *tolerance* (standard Yao-style constructions collapse because both yes- and no-instances must be far from juntas).

## 7. Current Research (as of June 2026)

- **Tolerant testing / distance approximation.** The dominant thread. Work descending from De–Mossel–Neeman (constant-factor junta-distance approximation with $n$-independent queries) and Iyer–Tal–Whitmeyer ($2^{\tilde O(\sqrt{k})}$ additive approximation). Recent work on *non-adaptive* tolerant junta testing via local distance estimators reports near-optimal $k$-dependence for the mild-tolerance regime *(frontier — verify)*.
- **Lower-bound machinery.** Sağlam's heat-flow log-convexity method is being pushed toward $\varepsilon$-sensitive bounds; groups at Columbia (Servedio, Waingarten, Nadimpalli), Boston University, and Charles University are active.
- **Junta testing as a subroutine.** Testing-by-implicit-learning and "junta-first" reductions now underpin testers for monotonicity, low-degree, and unateness; improvements in junta testing propagate directly.
- **Quantum.** Following Ambainis–Belovs–Regev–de Wolf, $\tilde O(\sqrt{k/\varepsilon})$ stands; whether $\Theta(\sqrt{k})$ is tight for all $\varepsilon$ and whether quantum tolerant testing beats $2^{\sqrt{k}}$ are open *(frontier — verify)*.
- **Beyond Boolean.** Juntas over $\mathbb{F}_p^n$, over the Gaussian space (relevant to testing dimension-reduced structure in learning theory), and "$k$-junta up to a symmetry group".

## 8. Future Work

- Design an adaptive tester whose $\varepsilon$-dependence is additive-$1/\varepsilon$ rather than $k/\varepsilon$, by reusing the coordinate-identification phase across accuracy scales.
- Develop a lower-bound framework in which the hard distributions are parameterized by distance, e.g. mixtures of $k$-parities perturbed by noise rate $\varepsilon$, and push these through the communication reduction.
- Prove or refute: tolerant junta testing requires $2^{k^{\Omega(1)}}$ queries. A candidate route is a reduction from approximating the influence-minimizing set, which is NP-hard in the analogous explicit setting.
- Extend the $\tilde\Omega(k^{3/2})$ non-adaptive bound to one-sided error and to the full $\varepsilon$ range.
- Settle distribution-free tolerant junta testing, currently untouched.

## 9. Key References

- **[Foundational]** E. Fischer, G. Kindler, D. Ron, S. Safra, A. Samorodnitsky. *Testing Juntas.* Journal of Computer and System Sciences, 68(4):753–787, 2004 (preliminary version FOCS 2002).
- **[Foundational]** E. Blais. *Testing Juntas Nearly Optimally.* STOC 2009, pp. 151–158.
- **[Foundational]** E. Blais. *Improved Bounds for Testing Juntas.* RANDOM/APPROX 2008, LNCS 5171, pp. 317–330.
- **[Lower bound]** E. Blais, J. Brody, K. Matulef. *Property Testing Lower Bounds via Communication Complexity.* Computational Complexity, 21(2):311–358, 2012 (preliminary version CCC 2011).
- **[Lower bound]** H. Chockler, D. Gutfreund. *A Lower Bound for Testing Juntas.* Information Processing Letters, 90(6):301–305, 2004.
- **[SOTA]** X. Chen, R. A. Servedio, L.-Y. Tan, E. Waingarten, J. Xie. *Settling the Query Complexity of Non-Adaptive Junta Testing.* CCC 2017; Journal of the ACM, 65(6), 2018.
- **[SOTA]** M. Sağlam. *Near Log-Convexity of Measured Heat in (Discrete) Time and Consequences.* FOCS 2018, pp. 967–978.
- **[Tolerant]** A. De, E. Mossel, J. Neeman. *Junta Correlation is Testable.* FOCS 2019, pp. 1549–1563.
- **[Tolerant]** V. Iyer, A. Tal, M. Whitmeyer. *Junta Distance Approximation with Sub-Exponential Queries.* CCC 2021, LIPIcs vol. 200.
- **[Distribution-free]** Z. Liu, X. Chen, R. A. Servedio, Y. Sheng, J. Xie. *Distribution-Free Junta Testing.* STOC 2018, pp. 749–759.
- **[Distribution-free]** N. H. Bshouty. *Almost Optimal Distribution-Free Junta Testing.* CCC 2019, LIPIcs vol. 137.
- **[Quantum]** A. Ambainis, A. Belovs, O. Regev, R. de Wolf. *Efficient Quantum Algorithms for (Gapped) Group Testing and Junta Testing.* SODA 2016, pp. 903–922.
- **[Structural]** E. Friedgut. *Boolean Functions with Low Average Sensitivity Depend on Few Coordinates.* Combinatorica, 18(1):27–35, 1998.
- **[Survey]** O. Goldreich. *Introduction to Property Testing.* Cambridge University Press, 2017 (Ch. 5).
- **[Survey]** R. O'Donnell. *Analysis of Boolean Functions.* Cambridge University Press, 2014 (Ch. 7).

## 10. Worked Example / Concrete Special Case

**Setting.** $n = 4$, $k = 1$, $f(x) = x_1 \oplus x_2$. In $\pm1$ notation $f = \chi_{\{1,2\}}$.

**Step 1 — distance to the class.** A $1$-junta $g$ has Fourier support in $\{\emptyset, \{1\},\{2\},\{3\},\{4\}\}$, so $\hat g(\{1,2\}) = 0$. For $\pm1$-valued $f,g$,
$$\mathrm{dist}(f,g) = \tfrac12\big(1 - \mathbb{E}[fg]\big) = \tfrac12\big(1 - \hat g(\{1,2\})\big) = \tfrac12 .$$
So $f$ is exactly $\tfrac12$-far from $\mathcal{J}_1^4$ — a maximally hard instance for $\varepsilon < 1/2$.

**Step 2 — influences.** $\mathrm{Inf}_1[f] = \mathrm{Inf}_2[f] = 1$, $\mathrm{Inf}_3[f]=\mathrm{Inf}_4[f]=0$. Two coordinates carry influence, one more than $k=1$: this is exactly the signal the tester must find.

**Step 3 — run the tester.** Partition $[4]$ into blocks $I_1=\{1\}, I_2=\{2\}, I_3=\{3\}, I_4=\{4\}$. On block $I$, sample $x,y$ uniform, set $z_I=y_I$, $z_{\bar I}=x_{\bar I}$, and record a "hit" if $f(x)\ne f(z)$. Then
$$\Pr[\text{hit on } I_1] = \Pr[x_1 \ne y_1] = \tfrac12, \quad \Pr[\text{hit on } I_2] = \tfrac12, \quad \Pr[\text{hit on } I_3]=\Pr[\text{hit on } I_4]=0 .$$
Run $t$ independent trials per block and reject if **two or more** blocks register a hit. The probability that $I_1$ registers no hit in $t$ trials is $2^{-t}$; same for $I_2$. By a union bound the tester fails to reject with probability $\le 2\cdot 2^{-t}$, so $t = 3$ (i.e. $2\cdot 4 \cdot 3 = 24$ queries) gives error $\le 1/4$. A genuine $1$-junta produces hits on at most one block, so the tester has one-sided error.

**Step 4 — what the general problem adds.** For general $k$ and unknown $J$, blocks must be *random*: with $s = \Theta(k^2)$ blocks, the $k$ relevant coordinates land in distinct blocks with constant probability (birthday bound), giving the FKRSS $\tilde O(k^2/\varepsilon)$ tester. Blais's non-adaptive refinement lowers this to $\tilde O(k^{3/2}/\varepsilon)$ by re-using overlapping block samples, and the adaptive $O(k\log k + k/\varepsilon)$ tester replaces the per-block scan above with binary search inside a hit-registering block — $\log k$ queries to isolate one relevant coordinate, $k$ coordinates to isolate. The $\tilde\Omega(k^{3/2})$ and $\Omega(k\log k)$ lower bounds say these two schemes are optimal at constant $\varepsilon$; what the $\varepsilon\to0$ regime costs, as in Step 3's $t = \Theta(\log(1/\delta))$ but with distance $\varepsilon$ instead of $1/2$, is exactly what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*