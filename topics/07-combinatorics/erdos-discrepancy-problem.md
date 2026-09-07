---
id: 07-combinatorics/erdos-discrepancy-problem
title: "Erdős Discrepancy Problem"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Discrepancy Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-discrepancy-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $f:\mathbb{N}\to\{-1,+1\}$ be an arbitrary sign sequence. Erdős conjectured (c. 1932, published 1957) that the partial sums of $f$ along **homogeneous arithmetic progressions** (HAPs) $d, 2d, 3d,\dots$ are always unbounded:

$$\sup_{n,d\ \in\ \mathbb{N}}\ \left|\sum_{i=1}^{n} f(id)\right| \;=\; \infty .$$

Equivalently, for every constant $C$ there is no infinite $\pm1$ sequence with **discrepancy** at most $C$, where the discrepancy of $f$ is the supremum above.

The conjecture was **proved by Terence Tao in 2015** (published in *Discrete Analysis*, 2016). Erdős's \$500 prize problem is therefore closed in its qualitative form. What remains open — and is the live content of this entry — is the **quantitative** version: determine the true growth rate

$$D_f(N) \;=\; \max_{nd\le N}\left|\sum_{i=1}^{n} f(id)\right|$$

minimised over all $\pm 1$ sequences $f$. A complete resolution of the quantitative problem means matching upper and lower bounds for $\min_f D_f(N)$ as $N\to\infty$; the conjectured truth is $\asymp \log N$.

## 2. Mathematical Foundations

**Discrepancy of a set system.** Given a hypergraph $\mathcal{H}$ on a ground set $X$, the discrepancy is $\operatorname{disc}(\mathcal{H})=\min_{f:X\to\{\pm1\}}\max_{S\in\mathcal H}|\sum_{x\in S} f(x)|$. Here $X=\mathbb{N}$ and $\mathcal{H}=\{\,\{d,2d,\dots,nd\}: n,d\ge 1\,\}$. Contrast with Roth's theorem on *all* arithmetic progressions in $\{1,\dots,N\}$, where the discrepancy is $\asymp N^{1/4}$ (Roth 1964, lower bound; Matoušek–Spencer 1996, matching upper bound). Dropping the "homogeneous" restriction thus makes the problem polynomially large; the HAP system is far sparser and its discrepancy is only logarithmic.

**Completely multiplicative functions.** $g:\mathbb{N}\to\{-1,+1\}$ is completely multiplicative if $g(mn)=g(m)g(n)$ for all $m,n$. Examples: the Liouville function $\lambda$, real Dirichlet characters, and "character-like" functions such as $\lambda_3$ defined by $\lambda_3(3)=+1$ and $\lambda_3(p)=\chi_3(p)$ for $p\ne 3$, where $\chi_3$ is the nonprincipal character mod $3$.

**Polymath5 reduction.** It suffices to prove the conjecture for completely multiplicative $g$: if every completely multiplicative $\pm1$ function has unbounded HAP sums, so does every $\pm1$ sequence. The reduction proceeds by showing a bounded-discrepancy $f$ forces a "Fourier-complexity" decomposition whose extremal components are multiplicative (Polymath5, 2010; see Tao 2016, §2).

**Elliott / Chowla input.** For $g$ completely multiplicative and $\pm1$-valued, the logarithmically averaged two-point correlation

$$\frac{1}{\log N}\sum_{n\le N}\frac{g(n)\,g(n+h)}{n}$$

is the object Tao controls. The **logarithmically averaged Chowla conjecture for two-point correlations** — proved by Tao (2016) — states
$$\lim_{N\to\infty}\frac{1}{\log N}\sum_{n\le N}\frac{\lambda(n)\lambda(n+h)}{n}=0\qquad (h\ne0),$$
with an Elliott-type generalisation to any bounded multiplicative $g$ that is not "pretentious" (not close to $n^{it}\chi(n)$ in the Granville–Soundararajan distance).

**Structure of the proof.** Suppose $D_f(N)\le C$ for all $N$. Then $\sum_{n} \frac{|\sum_{i\le n} g(i)|^2}{n}$-type averages stay bounded, forcing $g$ to correlate with a modulated character; the Elliott-type theorem, combined with the Matomäki–Radziwiłł theorem on multiplicative functions in short intervals and an **entropy decrement argument** (bounding the mutual information between $g$ and residues mod $p$ across many primes $p$), yields a contradiction.

## 3. History & State of the Art (SOTA)

- **c. 1932 / 1957.** Erdős poses the question; it appears in "Some unsolved problems," *Michigan Math. J.* 4 (1957). Erdős later attached a \$500 prize.
- **1964.** Roth proves the $N^{1/4}$ lower bound for the (non-homogeneous) AP discrepancy problem, sharpening the contrast with the HAP case.
- **1986.** Erdős–Graham record the problem in *Old and New Problems and Results in Combinatorial Number Theory*.
- **2010.** Borwein, Choi and Coons show the character-like $\lambda_3$ has $D_{\lambda_3}(N)\asymp\log N$ — the best known upper-bound construction, and the source of the conjectured logarithmic truth.
- **2010.** Polymath5 (led by Gowers) reduces the general case to completely multiplicative functions and produces long low-discrepancy sequences by computer search.
- **2014–15.** Konev and Lisitsa settle $C=2$ by SAT solving, with a machine-checked DRUP certificate of roughly 13 GB.
- **2015–16.** Matomäki–Radziwiłł (short intervals) and Matomäki–Radziwiłł–Tao (averaged Chowla) supply the analytic engine; **Tao proves the conjecture** in full.
- **2019–present.** Tao–Teräväinen extend logarithmic Chowla to odd-order correlations; work continues on effectivising the discrepancy growth rate.

## 4. Partial Results / Verified Cases

- **Discrepancy $C=1$.** The longest $\pm1$ sequence with all HAP sums in $\{-1,0,1\}$ has length $11$; e.g. $+,-,-,+,-,+,+,-,-,+,-$. No length-$12$ sequence exists (elementary; see §10).
- **Discrepancy $C=2$.** Konev–Lisitsa (2014) proved by SAT that the maximum length is exactly $1160$: a sequence of length $1160$ with discrepancy $2$ exists and none of length $1161$ does. This was the first computer-verified case beyond hand analysis.
- **Discrepancy $C=3$.** A sequence of length $127{,}645$ with discrepancy $3$ is known (Konev–Lisitsa 2015); the exact maximum length is **not** known. Extrapolation suggests the extremal length for discrepancy $C$ grows roughly like $\exp(cC)$ — consistent with $D(N)\asymp\log N$.
- **Multiplicative case.** For completely multiplicative $g$, unboundedness follows directly from the Elliott-type theorem; and for character-like $g$ the exact rate is known: $D_{\lambda_3}(N)=\log_9 N+O(1)$ (Borwein–Choi–Coons).
- **General case.** Tao (2016): unbounded for every $\pm1$ sequence — the conjecture as stated by Erdős is a theorem. The result also holds for $f$ taking values in the unit sphere of a Hilbert space, and more generally for $f$ bounded away from $0$ in modulus.

## 5. Principal Obstacles

The obstacles now concern the *rate*, not existence.

- **Ineffectivity of the pretentious dichotomy.** The Halász/Granville–Soundararajan machinery separates multiplicative functions into "pretentious" and "non-pretentious" classes using a distance whose relevant parameters are not explicit; Siegel-zero-type ineffectivity propagates into any attempt to extract a numeric growth rate.
- **Entropy decrement is lossy.** Tao's entropy decrement argument gains information at only one prime scale at a time, over a sparse set of primes chosen by pigeonhole. Its quantitative output is of iterated-logarithm strength at best — astronomically weaker than the conjectured $\log N$.
- **Fourier analysis alone is blind to the HAP system.** The HAP hypergraph has $O(N\log N)$ edges of wildly varying size and no translation invariance, so linear-Fourier or eigenvalue (Beck–Fiala, partial colouring, Banaszczyk) methods give nothing better than trivial bounds; the natural $L^2$ relaxation of the HAP matrix has small singular values.
- **Semidefinite relaxations plateau.** The SDP dual certificates found by Polymath5 for the vector-valued relaxation are bounded, showing the $\pm1$ obstruction is not captured by the relaxation — a genuine integrality gap.
- **SAT does not scale.** The search space for discrepancy $C$ grows like $2^{\exp(cC)}$; the $C=3$ instance is already beyond current solvers' reach for the upper bound.

## 6. The Gap

Proved: $\min_f D_f(N)\to\infty$. Conjectured: $\min_f D_f(N)\asymp \log N$.

The upper bound $\min_f D_f(N)\le \log_9 N + O(1)$ is known and explicit (via $\lambda_3$). The gap is entirely on the **lower** side: Tao's proof is a compactness/contradiction argument whose quantitative extraction, if pushed through, yields at best a bound of iterated-logarithm type in $N$, and no clean effective statement has been published. Crossing the gap requires either (a) an effective version of the logarithmically averaged Elliott conjecture with polynomial-in-parameters dependence, or (b) a genuinely combinatorial lower-bound argument for the HAP hypergraph that bypasses multiplicative number theory.

## 7. Current Research (as of June 2026)

- **Effectivising Tao's theorem.** Work on quantitative forms of logarithmic Chowla (Tao–Teräväinen; Helfgott–Radziwiłł's "Expansion, divisibility and parity" approach to $\sum_{n\le N}\lambda(n)$ via expander graphs) is the main route to an explicit discrepancy rate. *(frontier — verify)* No published bound of the form $D(N)\gg (\log\log N)^{c}$ for all $\pm1$ sequences yet exists.
- **Higher-order Chowla.** Tao–Teräväinen established odd-order logarithmic Chowla (Duke, 2019) and later extended the range; groups at Turku (Matomäki, Teräväinen), Oxford, and UCLA continue this programme.
- **Extremal sequence structure.** Interest persists in whether the extremal length $L(C)$ for discrepancy $C$ satisfies $L(C)=\exp(\Theta(C))$; $L(1)=11$, $L(2)=1160$, $L(3)\ge 127{,}645$. *(frontier — verify)* Improved SAT/CDCL and local-search lower bounds for $L(3)$ and $L(4)$ appear periodically in the SAT community.
- **Vector-valued and Banach-space analogues.** Tao's proof covers Hilbert-space-valued sequences; the analogous statement for general uniformly convex Banach spaces remains open.
- **Related hypergraphs.** Discrepancy along $\{d, 2d, \dots\}$ restricted to $d$ in a sparse set (e.g. primes, or $d\le N^{\varepsilon}$) is an active variant where the multiplicative reduction breaks down.

## 8. Future Work

- Extract an explicit lower bound from the entropy decrement argument, even one as weak as $\log\log\log N$; Tao has flagged this as the natural next step.
- Prove the full (non-logarithmically-averaged) Chowla conjecture for two-point correlations, which would remove the averaging losses.
- Find a combinatorial or spectral proof of the $C=3$ upper bound on sequence length, calibrating the $\exp(\Theta(C))$ heuristic.
- Establish a matching $\Omega(\log N)$ lower bound for completely multiplicative $\pm1$ functions alone — a strictly easier subproblem that is still open.
- Determine whether the $\lambda_3$ construction is genuinely extremal, i.e. whether $\min_f D_f(N)=\log_9 N+O(1)$.

## 9. Key References

- **[Foundational]** P. Erdős. *Some unsolved problems.* Michigan Mathematical Journal 4 (1957), 291–300.
- **[Foundational]** P. Erdős, R. L. Graham. *Old and New Problems and Results in Combinatorial Number Theory.* L'Enseignement Mathématique, Geneva, 1980.
- **[Foundational]** K. F. Roth. *Remark concerning integer sequences.* Acta Arithmetica 9 (1964), 257–260.
- **[SOTA]** T. Tao. *The Erdős discrepancy problem.* Discrete Analysis 2016:1, 29 pp.
- **[SOTA]** T. Tao. *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations.* Forum of Mathematics, Pi 4 (2016), e8.
- **[SOTA]** K. Matomäki, M. Radziwiłł. *Multiplicative functions in short intervals.* Annals of Mathematics 183 (2016), 1015–1056.
- **[SOTA]** K. Matomäki, M. Radziwiłł, T. Tao. *An averaged form of Chowla's conjecture.* Algebra & Number Theory 9 (2015), 2167–2196.
- **[SOTA]** T. Tao, J. Teräväinen. *The structure of logarithmic correlations of multiplicative functions, with applications to the Chowla and Elliott conjectures.* Duke Mathematical Journal 168 (2019), 1977–2027.
- **[Computational]** B. Konev, A. Lisitsa. *A SAT attack on the Erdős discrepancy conjecture.* Theory and Applications of Satisfiability Testing (SAT 2014), LNCS 8561, Springer, 219–226.
- **[Computational]** B. Konev, A. Lisitsa. *Computer-aided proof of Erdős discrepancy properties.* Artificial Intelligence 224 (2015), 103–118.
- **[Structural]** P. Borwein, K.-K. S. Choi, M. Coons. *Completely multiplicative functions taking values in $\{-1,1\}$.* Transactions of the American Mathematical Society 362 (2010), 6279–6291.
- **[Survey]** K. Soundararajan. *The Liouville function in short intervals [after Matomäki and Radziwiłł].* Séminaire Bourbaki, Astérisque 390 (2017), Exp. 1119.
- **[Collaborative]** D. H. J. Polymath. *The Erdős discrepancy problem* (Polymath5 project wiki and discussion threads, 2010), archived at michaelnielsen.org/polymath1.

## 10. Worked Example / Concrete Special Case

**Claim.** No $f:\{1,\dots,12\}\to\{\pm1\}$ has $\bigl|\sum_{i=1}^n f(id)\bigr|\le 1$ for all $nd\le 12$.

Write $S_n=\sum_{i\le n}f(i)$ (the $d=1$ sums). Negating $f$ if necessary, take $f(1)=+1$.

1. $|S_2|=|1+f(2)|\le1 \Rightarrow f(2)=-1$, so $S_2=0$.
2. $d=2$, $n=2$: $|f(2)+f(4)|\le1 \Rightarrow f(4)=+1$.
3. $d=4$, $n=2$: $|f(4)+f(8)|\le1 \Rightarrow f(8)=-1$.
4. $S_3=f(3)$, $S_4=f(3)+f(4)=f(3)+1$. If $f(3)=+1$ then $S_4=2$. So $f(3)=-1$, $S_3=-1$, $S_4=0$.
5. $d=3$, $n=2$: $|f(3)+f(6)|\le1 \Rightarrow f(6)=+1$.
6. $S_5=f(5)$, $S_6=f(5)+f(6)=f(5)+1$. Hence $f(5)=-1$, $S_6=0$.
7. $S_7=f(7)$, $S_8=f(7)+f(8)=f(7)-1$. Hence $f(7)=+1$, $S_8=0$.
8. $S_9=f(9)$, $S_{10}=f(9)+f(10)$. From $d=5$, $n=2$: $|f(5)+f(10)|\le1\Rightarrow f(10)=+1$, so $S_{10}=f(9)+1$, forcing $f(9)=-1$.
9. $d=3$, $n=4$: $f(3)+f(6)+f(9)+f(12)=-1+1-1+f(12)=f(12)-1$. Bounded by $1$ forces $f(12)=+1$.
10. $d=6$, $n=2$: $f(6)+f(12)=1+1=2$. Contradiction. $\blacksquare$

So $D_f(12)\ge 2$ for every $\pm1$ sequence, and the length-$11$ sequence $+,-,-,+,-,+,+,-,-,+,-$ shows $12$ is sharp. Pushing the same style of reasoning to discrepancy $2$ requires $1161$ terms and, in practice, a SAT solver — an $88$-fold jump in length for one extra unit of discrepancy, which is exactly the exponential behaviour $L(C)=\exp(\Theta(C))$ that the conjectured $\log N$ rate encodes.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*