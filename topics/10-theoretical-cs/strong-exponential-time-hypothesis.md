---
id: 10-theoretical-cs/strong-exponential-time-hypothesis
title: "Strong Exponential Time Hypothesis"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Strong Exponential Time Hypothesis

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/strong-exponential-time-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

The Strong Exponential Time Hypothesis (SETH), stated by Impagliazzo and Paturi (2001), asserts that Boolean satisfiability on CNF formulas of bounded clause width admits no algorithm with constant savings in the exponent, uniformly over the width.

**SETH.** For every $\varepsilon > 0$ there exists $k \in \mathbb{N}$ such that $k$-SAT on $n$ variables cannot be decided in time $O(2^{(1-\varepsilon)n})$ by any (randomized) algorithm.

Equivalently: $\lim_{k\to\infty} s_k = 1$, where $s_k$ is the infimum of $\delta$ such that $k$-SAT is solvable in $2^{\delta n}\,\mathrm{poly}(n+m)$ time.

A **disproof** requires a single $\varepsilon > 0$ and an algorithm solving $k$-SAT in $O(2^{(1-\varepsilon)n})$ for *every* $k$ — equivalently, by the sparsification lemma, solving CNF-SAT with $m = O(n)$ clauses in $O(2^{(1-\varepsilon)n})$. A **proof** would imply $\mathsf{P} \neq \mathsf{NP}$ and is far beyond current lower-bound technology; SETH is therefore treated as a hardness axiom, not a target for proof. The problem is open in both directions: no refutation, and no proof under weaker assumptions.

## 2. Mathematical Foundations

Let $F$ be a $k$-CNF formula over variables $x_1,\dots,x_n$ with $m$ clauses, each a disjunction of at most $k$ literals. Define
$$
s_k \;=\; \inf\Big\{\delta \ge 0 \;:\; \exists\, \text{algorithm deciding } k\text{-SAT in } O\big(2^{\delta n}\big)\Big\},
\qquad s_\infty \;=\; \lim_{k\to\infty} s_k .
$$
The limit exists because $(s_k)$ is nondecreasing and bounded by $1$.

- **ETH (Exponential Time Hypothesis):** $s_3 > 0$.
- **SETH:** $s_\infty = 1$.

SETH $\Rightarrow$ ETH, but not conversely as far as is known.

**Sparsification Lemma** (Impagliazzo–Paturi–Zane 2001). For all $k$ and $\varepsilon>0$ there is a constant $C = C(k,\varepsilon)$ and an algorithm that, in time $2^{\varepsilon n}\mathrm{poly}(n)$, outputs $k$-CNF formulas $F_1,\dots,F_t$ with $t \le 2^{\varepsilon n}$, each with at most $Cn$ clauses, such that
$$
F \text{ satisfiable} \iff \bigvee_{i=1}^{t} F_i \text{ satisfiable}.
$$
Consequence: $k$-SAT complexity is governed by the *linear-clause-density* regime, and ETH is equivalent to its sparse form.

**Monotonicity theorem** (Impagliazzo–Paturi 2001). If ETH holds, then $s_k < s_{k+1}$ for all $k \ge 3$, and moreover
$$
s_k \;\le\; s_\infty\Big(1 - \frac{d}{k}\Big) + O\!\big(k^{-2}\big)
$$
for an absolute constant $d>0$. Hence the sequence $s_k$ approaches its limit at rate $\Theta(1/k)$; SETH pins that limit at $1$.

**Unbounded width.** For CNF-SAT with $m$ clauses, the best known savings degrade with density: satisfiability is solvable in
$$
2^{\,n\left(1 - \Omega\!\left(1/\log(m/n)\right)\right)}
$$
time (Schuler 2005; Calabro–Impagliazzo–Paturi 2006), which is $2^{n - o(n)}$ when $m$ is superpolynomial in $n$. SETH says no $2^{(1-\varepsilon)n}$ bound with $\varepsilon$ independent of $m/n$ exists even for $m = O(n)$.

**Fine-grained consequences.** SETH's role is as the root of a reduction web. Writing $\mathrm{OV}$ for Orthogonal Vectors — given $A,B \subseteq \{0,1\}^d$ with $|A|=|B|=N$, $d = \omega(\log N)$, decide whether $\exists\, a\in A, b\in B$ with $\langle a,b\rangle = 0$ — SETH implies $\mathrm{OV}$ needs $N^{2-o(1)}$ time (Williams 2005). Downstream, under SETH: edit distance and longest common subsequence on strings of length $N$ need $N^{2-o(1)}$; discrete Fréchet distance needs $N^{2-o(1)}$; $k$-Dominating Set needs $n^{k-o(1)}$; graph diameter cannot be $(3/2-\delta)$-approximated in $m^{2-\delta'}$ time; and dynamic-programming-over-treewidth algorithms for Independent Set, Dominating Set, and $q$-Colouring with running times $2^{tw}$, $3^{tw}$, $q^{tw}$ are optimal.

## 3. History & State of the Art (SOTA)

- **1998–2001.** Impagliazzo and Paturi introduce $s_k$, prove monotonicity, and formulate SETH in *On the complexity of $k$-SAT* (JCSS 2001). With Zane, the sparsification lemma (JCSS 2001) makes ETH/SETH robust to clause density.
- **1999.** Schöning's random-walk algorithm gives $(2 - 2/k)^n$ for $k$-SAT — savings $\Theta(1/k)$, consistent with SETH.
- **2005.** Paturi–Pudlák–Saks–Zane (PPSZ, JACM 2005) achieve $2^{n(1 - \mu_k/k)}$ with $\mu_k \to \pi^2/6 \approx 1.644$, the asymptotically best known savings for large $k$.
- **2005.** Williams shows SETH-hardness of Orthogonal Vectors and 2-CSP via split-and-list, launching fine-grained complexity.
- **2010–2016.** Pătraşcu–Williams (SODA 2010) derive $k$-Dominating Set lower bounds; Lokshtanov–Marx–Saurabh (SODA 2011) prove optimality of treewidth DPs; Cygan et al. (CCC 2012) relate CNF-SAT to Set Cover, Steiner Tree, Hitting Set; Bringmann (FOCS 2014) settles Fréchet distance; Backurs–Indyk (STOC 2015) settle edit distance; Abboud–Backurs–Vassilevska Williams (FOCS 2015) settle LCS.
- **2016.** Abboud–Hansen–Vassilevska Williams–Williams (STOC 2016) strengthen the base assumption to NC-SETH and expose a barrier: even modest improvements over quadratic for LCS would yield new circuit lower bounds.
- **2019–2021.** Hansen–Kaplan–Zamir–Zwick (STOC 2019) give biased-PPSZ, $O(1.30704^n)$ for 3-SAT; Scheder (FOCS 2021) improves the PPSZ analysis to $O(1.306995^n)$.

Current SOTA: no algorithm achieves savings bounded away from $0$ uniformly in $k$; all known savings are $\Theta(1/k)$ or $\Theta(1/\log(m/n))$.

## 4. Partial Results / Verified Cases

- **$k=2$:** 2-SAT is in $\mathrm{P}$ (Aspvall–Plass–Tarjan 1979), so $s_2 = 0$; SETH concerns $k \ge 3$ only.
- **$k=3$:** best known $O(1.306995^n)$, i.e. $s_3 \le 0.3865$. For Unique-3-SAT, PPSZ gives $O(1.3071^n)$ historically and the general/unique gap was closed by Hertli (FOCS 2011).
- **$k=4,5,6$:** $s_k \le 1 - \mu_k/k$ with the biased-PPSZ constants; e.g. 4-SAT in $O(1.469^n)$ and 5-SAT in $O(1.569^n)$ (Hansen–Kaplan–Zamir–Zwick 2019). All strictly below $2^n$, all with savings shrinking like $1/k$.
- **Unique satisfiability:** SETH is equivalent to its promise version. The isolation lemma for $k$-CNFs (Calabro–Impagliazzo–Paturi–Schneider, CCC 2003) shows an $O(2^{(1-\varepsilon)n})$ algorithm for Unique-$k$-SAT yields one for $k$-SAT with $\varepsilon' = \varepsilon - o(1)$.
- **Restricted algorithm classes (unconditional):** tree-like resolution requires $2^{\Omega(n)}$ steps on random $k$-CNFs (Chvátal–Szemerédi 1988; Pudlák–Impagliazzo 2000); general resolution requires $2^{\Omega(n/\Delta)}$ on density-$\Delta$ random formulas (Ben-Sasson–Wigderson 2001). These prove SETH-consistent lower bounds against DPLL/resolution-based solvers, not against arbitrary algorithms.
- **Random instances:** Vyas–Williams (SAT 2019) show the "Super-Strong ETH" — no $2^{o(n)}$-savings on random $k$-SAT at the satisfiability threshold — fails for PPSZ-style algorithms at large $k$, refining what SETH can plausibly claim about average-case instances.
- **Counting version:** $\\#$SETH-style statements are known to be *false* in some structured regimes, e.g. counting satisfying assignments of sparse formulas admits improved savings; and SETH provably fails for certain circuit classes richer than CNF (Williams' ACC-SAT algorithms, JACM 2014, beat brute force for $\mathrm{ACC}^0$ circuits).

## 5. Principal Obstacles

- **Proving SETH implies $\mathsf{P}\neq\mathsf{NP}$.** Any proof needs superpolynomial, indeed $2^{\Omega(n)}$, lower bounds against general algorithms — unavailable. Relativization, natural proofs (Razborov–Rudich), and algebrization all obstruct.
- **Refutation is blocked by exponential-savings barriers.** Improvements to $k$-SAT come from local structure: PPSZ's savings derive from the probability that a random critical clause is resolved by bounded-depth resolution, an effect that decays as $1/k$ because each clause constrains a $2^{-k}$ fraction of the cube. No known technique extracts savings independent of $k$.
- **Density degradation.** Schuler-type width reduction converts CNF-SAT to $k$-SAT at the cost of $2^{n/\log(m/n)}$ overhead; the loss is intrinsic to clause-shortening and no alternative reduction avoids it.
- **Circuit-lower-bound barrier.** Abboud–Hansen–Vassilevska Williams–Williams (2016) show that refuting NC-SETH — SETH for formulas/branching programs rather than CNFs — would imply $\mathsf{NEXP} \not\subseteq \mathsf{NC}^1$ (via Williams' algorithms-to-lower-bounds framework). So progress on the natural strengthening of SETH is at least as hard as a breakthrough circuit lower bound.
- **No self-reducibility leverage.** Unlike PCP-based hardness of approximation, SETH has no known amplification: the constant $\varepsilon$ in the hypothesis cannot be boosted, and reductions from SETH lose all quantitative slack unless they are linear-size.

## 6. The Gap

Proven: $s_k \le 1 - \Theta(1/k)$ for every fixed $k$, and $s_k$ is strictly increasing under ETH. Conjectured: $\sup_k s_k = 1$.

The gap is the *uniformity in $k$*. Every known upper bound has savings $\mu_k/k$ with $\mu_k = O(1)$; SETH fails precisely if some algorithm achieves savings $\varepsilon > 0$ with $\varepsilon$ not depending on $k$. Concretely, refutation requires an algorithm for CNF-SAT on $n$ variables and $Cn$ clauses running in $2^{(1-\varepsilon)n}$ where $\varepsilon$ is independent of $C$ — currently the best is $\varepsilon = \Omega(1/\log C)$. Closing the gap from $\Omega(1/\log C)$ to $\Omega(1)$, or proving no such improvement exists, is the entire content of the problem.

## 7. Current Research (as of June 2026)

- **Fine-grained reduction web.** Groups at MIT (Vassilevska Williams, Williams), Saarbrücken/MPI (Bringmann, Künnemann), Copenhagen (BARC), and Weizmann continue to place problems under SETH: dynamic graph problems, string alignment, computational geometry, and streaming.
- **Deterministic derandomization of PPSZ.** Ongoing work aims to match the randomized $1.307^n$ bound deterministically; partial results exist for Unique-$k$-SAT.
- **Weaker sufficient hypotheses.** There is sustained interest in replacing SETH with the OV Conjecture or with $k$-OV, since consequences hold under strictly weaker assumptions; several 2024–2026 papers derive quadratic lower bounds from OV alone. *(frontier — verify)*
- **SETH versus quantum.** Quantum SETH — no $2^{(1/2-\varepsilon)n}$ quantum algorithm for $k$-SAT beyond Grover — is being used to derive quantum fine-grained lower bounds; formalizations and their consequences remain contested. *(frontier — verify)*
- **Average-case and Super-Strong ETH.** Refinements of the Vyas–Williams programme continue to map which random-instance regimes admit savings. *(frontier — verify)*

## 8. Future Work

- Determine whether SETH is equivalent to the OV Conjecture; a reduction from OV back to CNF-SAT would be a structural breakthrough.
- Find any algorithm with $k$-independent savings for CNF-SAT on formulas of linear density, or prove such savings imply an unlikely collapse.
- Extend the algorithms-to-lower-bounds framework so that a SETH refutation provably yields $\mathsf{NEXP} \not\subseteq \mathsf{NC}^1$-style consequences for CNFs, not just for $\mathrm{NC}^1$ circuits.
- Develop hardness-of-approximation analogues: "Gap-SETH" statements that would yield tight inapproximability in the fine-grained regime.
- Settle whether $s_k$ can be computed or approximated for small $k$ under any plausible assumption; even $s_3$ is not known to be positive without ETH.

## 9. Key References

- **[Foundational]** Russell Impagliazzo and Ramamohan Paturi. *On the Complexity of $k$-SAT.* Journal of Computer and System Sciences, 62(2):367–375, 2001.
- **[Foundational]** Russell Impagliazzo, Ramamohan Paturi, and Francis Zane. *Which Problems Have Strongly Exponential Complexity?* Journal of Computer and System Sciences, 63(4):512–530, 2001.
- **[Foundational]** Ramamohan Paturi, Pavel Pudlák, Michael E. Saks, and Francis Zane. *An Improved Exponential-Time Algorithm for $k$-SAT.* Journal of the ACM, 52(3):337–364, 2005.
- **[Foundational]** Uwe Schöning. *A Probabilistic Algorithm for $k$-SAT and Constraint Satisfaction Problems.* FOCS 1999, pp. 410–414.
- **[SOTA / Recent]** Thomas Dueholm Hansen, Haim Kaplan, Or Zamir, and Uri Zwick. *Faster $k$-SAT Algorithms Using Biased-PPSZ.* STOC 2019, pp. 578–589.
- **[SOTA / Recent]** Dominik Scheder. *PPSZ is Better Than You Think.* FOCS 2021, pp. 205–216.
- **[SOTA / Recent]** Ryan Williams. *A New Algorithm for Optimal 2-Constraint Satisfaction and Its Implications.* Theoretical Computer Science, 348(2–3):357–365, 2005.
- **[SOTA / Recent]** Arturs Backurs and Piotr Indyk. *Edit Distance Cannot Be Computed in Strongly Subquadratic Time (Unless SETH is False).* STOC 2015, pp. 51–58.
- **[SOTA / Recent]** Amir Abboud, Thomas Dueholm Hansen, Virginia Vassilevska Williams, and Ryan Williams. *Simulating Branching Programs with Edit Distance and Friends, or: A Polylog Shaved Is a Lower Bound Made.* STOC 2016, pp. 375–388.
- **[SOTA / Recent]** Marek Cygan, Holger Dell, Daniel Lokshtanov, Dániel Marx, Jesper Nederlof, Yoshio Okamoto, Ramamohan Paturi, Saket Saurabh, and Magnus Wahlström. *On Problems as Hard as CNF-SAT.* ACM Transactions on Algorithms, 12(3):41, 2016.
- **[Survey]** Virginia Vassilevska Williams. *On Some Fine-Grained Questions in Algorithms and Complexity.* Proceedings of the International Congress of Mathematicians (ICM 2018), Vol. IV, pp. 3447–3487.
- **[Survey]** Marek Cygan, Fedor V. Fomin, Łukasz Kowalik, Daniel Lokshtanov, Dániel Marx, Marcin Pilipczuk, Michał Pilipczuk, and Saket Saurabh. *Parameterized Algorithms.* Springer, 2015 (Chapter 14, Lower Bounds Based on ETH/SETH).

## 10. Worked Example / Concrete Special Case

**Claim.** If Orthogonal Vectors on $N$ vectors in $\{0,1\}^d$ is solvable in $N^{2-\varepsilon}\mathrm{poly}(d)$ time for some $\varepsilon>0$, then SETH is false.

**Construction (split-and-list).** Let $F$ be a $k$-CNF with variables $x_1,\dots,x_n$ and clauses $C_1,\dots,C_m$. Split the variables into $X = \{x_1,\dots,x_{n/2}\}$ and $Y = \{x_{n/2+1},\dots,x_n\}$. For each of the $N = 2^{n/2}$ assignments $\alpha$ to $X$, build $a_\alpha \in \{0,1\}^m$ with
$$
a_\alpha[j] = \begin{cases} 0 & \text{if } \alpha \text{ satisfies } C_j,\\ 1 & \text{otherwise,}\end{cases}
$$
and symmetrically $b_\beta \in \{0,1\}^m$ for assignments $\beta$ to $Y$. Then
$$
\langle a_\alpha, b_\beta\rangle = \sum_{j=1}^m a_\alpha[j]\,b_\beta[j] = 0
\iff \text{every clause is satisfied by } \alpha \text{ or } \beta
\iff (\alpha,\beta) \models F .
$$
So $F$ is satisfiable iff the two sets $A = \{a_\alpha\}$, $B = \{b_\beta\}$ contain an orthogonal pair. Applying the sparsification lemma first gives $m = O(n) = O(\log N)$ up to a $2^{o(n)}$ blow-up, so $d$ is polylogarithmic in $N$. An $N^{2-\varepsilon}$ OV algorithm then decides $k$-SAT in
$$
\big(2^{n/2}\big)^{2-\varepsilon}\mathrm{poly}(n) \;=\; 2^{\left(1 - \varepsilon/2\right)n}\mathrm{poly}(n),
$$
with $\varepsilon/2$ independent of $k$ — contradicting SETH.

**Numeric instance.** Take $n=4$, $F = (x_1 \vee x_3)\wedge(\neg x_1 \vee x_4)\wedge(x_2 \vee \neg x_3)$, so $m=3$. With $X=\{x_1,x_2\}$, $Y=\{x_3,x_4\}$:

| $\alpha = (x_1,x_2)$ | $a_\alpha$ | $\beta=(x_3,x_4)$ | $b_\beta$ |
|---|---|---|---|
| $00$ | $(1,0,1)$ | $00$ | $(1,1,0)$ |
| $01$ | $(1,0,0)$ | $01$ | $(1,0,0)$ |
| $10$ | $(0,1,1)$ | $10$ | $(0,1,1)$ |
| $11$ | $(0,1,0)$ | $11$ | $(0,0,1)$ |

Check $\alpha=01$, $\beta=10$: $\langle (1,0,0),(0,1,1)\rangle = 0$. This certifies the assignment $x_1=0,x_2=1,x_3=1,x_4=0$, and indeed $C_1 = (0\vee 1)=1$, $C_2 = (1 \vee 0)=1$, $C_3 = (1 \vee 0)=1$. The $4 \times 4$ inner-product table is exactly the brute-force $2^n$ search reorganized as $N^2$ pair tests with $N = 2^{n/2}$ — which is why shaving the exponent of OV shaves the exponent of SAT.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*