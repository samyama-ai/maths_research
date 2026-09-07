---
id: 10-theoretical-cs/ac0-with-parity-versus-np
title: "AC0 with Parity versus NP"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# AC0 with Parity versus NP

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/ac0-with-parity-versus-np` · **Status:** open

## 1. Problem Statement / Conjecture

$\mathrm{AC}^0[\oplus]$ is the class of languages decided by polynomial-size, constant-depth circuits over unbounded fan-in $\{\wedge, \vee, \neg, \oplus\}$ gates, where $\oplus$ computes the parity of its inputs.

The *worst-case, constant-depth* form of the question is closed: $\mathrm{NP} \not\subseteq \mathrm{AC}^0[\oplus]$, since $\mathrm{MAJORITY} \in \mathrm{P} \subseteq \mathrm{NP}$ and Razborov (1987) and Smolensky (1987) proved $\mathrm{MAJORITY} \notin \mathrm{AC}^0[\oplus]$. The open problem is the set of quantitative strengthenings that the polynomial method cannot reach:

- **(Q1) Depth frontier.** Is there a language $L \in \mathrm{NP}$ such that $L$ requires superpolynomial-size $\{\wedge,\vee,\neg,\oplus\}$-circuits of depth $d(n) = \omega(\log n / \log\log n)$? Equivalently, is $\mathrm{NP} \not\subseteq \mathrm{AC}^1[\oplus]$ (depth $O(\log n)$, polynomial size)? Nothing superpolynomial is known past $d = c\log n/\log\log n$.
- **(Q2) Correlation frontier.** Is there $f \in \mathrm{NP}$ (or even $f \in \mathrm{P}$) and $\varepsilon(n) = 2^{-n^{\Omega(1)}}$ such that every depth-$d$, size-$n^{O(1)}$ $\mathrm{AC}^0[\oplus]$ circuit $C$ satisfies
  $$\Big|\Pr_{x \sim \{0,1\}^n}[C(x) = f(x)] - \tfrac{1}{2}\Big| \le \varepsilon(n)\,?$$
  The best explicit bounds remain $n^{-\Theta(1)}$-type, not exponentially small.
- **(Q3) Majority on top.** Prove $\mathrm{NP} \not\subseteq \mathrm{MAJ} \circ \mathrm{AC}^0[\oplus]$, i.e. add a single majority gate above a polynomial-size $\mathrm{AC}^0[\oplus]$ circuit. By the discriminator lemma of Hajnal–Maass–Pudlák–Szegedy–Turán (1993), (Q3) follows from (Q2).

A complete resolution means: an explicit NP language plus an unconditional proof for one of (Q1)–(Q3), or a circuit construction placing SAT inside the corresponding class.

## 2. Mathematical Foundations

**Circuit class.** For a depth bound $d$ and size bound $s$, $\mathrm{AC}^0_d[\oplus]$-$\mathrm{SIZE}(s)$ is the set of Boolean functions computed by circuits with $\le s$ gates, $\le d$ layers, unbounded fan-in gates from $\{\wedge,\vee,\neg,\oplus\}$, inputs $x_1,\dots,x_n$ and their negations. $\mathrm{AC}^0[\oplus] = \bigcup_{d,c} \mathrm{AC}^0_d[\oplus]\text{-}\mathrm{SIZE}(n^c)$.

**Probabilistic polynomials.** For $f:\{0,1\}^n \to \{0,1\}$, a distribution $\mathbf{p}$ over $\mathbb{F}_2[x_1,\dots,x_n]$ has *degree* $\ell$ and *error* $\varepsilon$ if $\deg(p)\le \ell$ for all $p$ in the support and
$$\forall x \in \{0,1\}^n: \quad \Pr_{p \sim \mathbf{p}}[\,p(x) \ne f(x)\,] \le \varepsilon .$$
Over $\mathbb{F}_2$, $\oplus$ has degree $1$ exactly; $\neg y = 1+y$; and $\mathrm{OR}_m$ admits a degree-$\ell$ probabilistic polynomial with error $2^{-\ell}$ (Razborov's construction, §10).

**Razborov–Smolensky approximation lemma.** Every $C \in \mathrm{AC}^0_d[\oplus]$-$\mathrm{SIZE}(s)$ admits a polynomial $p \in \mathbb{F}_2[x]$ with
$$\deg(p) \le \big(\log(10 s)\big)^{d}, \qquad \Pr_{x}[\,p(x) \ne C(x)\,] \le \tfrac{1}{10}.$$

**Smolensky's degree lower bound.** Any $p \in \mathbb{F}_2[x_1,\dots,x_n]$ agreeing with $\mathrm{MAJ}_n$ on a $1-\delta$ fraction of $\{0,1\}^n$, for a fixed small constant $\delta > 0$, has $\deg(p) = \Omega(\sqrt{n})$.

**Consequence.** Combining the two, for every $d$,
$$\mathrm{MAJ}_n \in \mathrm{AC}^0_d[\oplus]\text{-}\mathrm{SIZE}(s) \implies s \ge 2^{\Omega(n^{1/2d})}.$$
The same machinery over $\mathbb{F}_{2^k}$ gives $\mathrm{MOD}_q \notin \mathrm{AC}^0[\oplus]$ for every $q$ not a power of $2$.

**Why the method stops.** The chain is *degree-based*: it certifies only that $\log s \gtrsim n^{1/2d}$. Setting $d = \tfrac{1}{2}\log n/\log\log n$ gives $n^{1/2d} = 2^{\log\log n} = \log n$, i.e. $s \ge n^{\Omega(1)}$ — no superpolynomial content. This is the exact location of the barrier in (Q1).

## 3. History & State of the Art (SOTA)

- **1983–1986.** Furst–Saxe–Sipser, Ajtai, and then Håstad's switching lemma give $\mathrm{PARITY} \notin \mathrm{AC}^0$, with the tight bound $2^{\Omega(n^{1/(d-1)})}$ for depth $d$. This makes $\oplus$ a natural gate to add.
- **1987.** Razborov proves $\mathrm{MAJORITY}$ requires size $2^{\Omega(n^{1/2d})}$ in depth-$d$ $\mathrm{AC}^0[\oplus]$. Smolensky independently develops the algebraic approximation framework and extends it to $\mathrm{AC}^0[p]$ for all primes $p$, showing $\mathrm{MOD}_q \notin \mathrm{AC}^0[p]$ for distinct primes $p,q$.
- **1993.** Smolensky's "On representations by low-degree polynomials" sharpens the $\Omega(\sqrt n)$ degree bound; Beigel surveys the polynomial method.
- **1994–1997.** Razborov–Rudich show that Razborov–Smolensky is a *natural proof* (constructive, large), which explains why it cannot extend to classes containing pseudorandom function candidates — and warns that any technique for (Q1) at higher depth must be non-natural.
- **2011–2014.** Williams proves $\mathrm{NEXP} \not\subseteq \mathrm{ACC}^0$ via nontrivial $\mathrm{ACC}^0$-SAT algorithms, a different (algorithmic, non-natural) route that also covers $\mathrm{AC}^0[\oplus]$ but only for the much larger class $\mathrm{NEXP}$.
- **2018–2020.** Murray–Williams push this to $\mathrm{NQP} = \mathrm{NTIME}[n^{\mathrm{polylog}\,n}] \not\subseteq \mathrm{ACC}^0$; Chen–Ren obtain *average-case* $\mathrm{ACC}^0$ lower bounds for $\mathrm{NQP}$. Neither reaches $\mathrm{NP}$.
- **2019.** Oliveira–Santhanam–Srinivasan ("Parity helps to compute Majority") give depth-$d$ $\mathrm{AC}^0[\oplus]$ circuits for $\mathrm{MAJ}_n$ of size $2^{\tilde O(n^{1/2(d-1)})}$, showing the Razborov–Smolensky exponent is essentially tight.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| Constant depth $d = O(1)$, worst case | **Solved.** $\mathrm{MAJ}, \mathrm{MOD}_3 \notin \mathrm{AC}^0[\oplus]$; size $\ge 2^{\Omega(n^{1/2d})}$ (Razborov 1987, Smolensky 1987). |
| Depth $d = o(\log n/\log\log n)$ | **Solved.** Superpolynomial bounds still follow from the degree chain. |
| Tightness of the exponent | **Solved.** Upper bound $2^{\tilde O(n^{1/2(d-1)})}$ for $\mathrm{MAJ}$ (Oliveira–Santhanam–Srinivasan 2019). |
| $\mathrm{NEXP}$, $\mathrm{NQP}$ vs $\mathrm{ACC}^0 \supseteq \mathrm{AC}^0[\oplus]$ | **Solved,** worst case (Williams 2014) and average case (Chen–Ren 2020). |
| Correlation with $\mathrm{MAJ}$ / $\mathrm{MOD}_3$ | **Partial.** $1/2 + n^{-\Omega(1)}$-type bounds; Kopparty–Srinivasan (certifying polynomials, 2018) give improved bounds and $\\#\mathrm{SAT}$ algorithms for $\mathrm{AC}^0[\oplus]$. |
| Depth 2 ($\oplus \circ \mathrm{AND}$, $\mathrm{AND} \circ \oplus$) | **Solved.** Exponential bounds by rank/degree arguments; inner product has $\mathbb{F}_2$-degree 2 but $\mathrm{MOD}_3$ requires $2^{\Omega(n)}$-size $\mathrm{AND}\circ\oplus$. |
| Pseudorandomness | **Partial.** Servedio–Tan (2019) give PRGs fooling $\mathrm{AC}^0[\oplus]$ with seed length $n^{1-\Omega(1)}$ for polynomial size. |
| Depth $\ge c\log n/\log\log n$ for **any** explicit $f$ | **Open.** No superpolynomial bound known. |

## 5. Principal Obstacles

- **Degree saturation.** The polynomial method converts a size-$s$, depth-$d$ circuit into degree $(\log s)^d$. Since $\mathbb{F}_2$-degree is at most $n$, the argument is vacuous once $(\log s)^d \ge n$, i.e. once $d \gtrsim \log n/\log\log n$ for polynomial $s$. No known algebraic invariant degrades more slowly with depth.
- **Error accumulation.** The union bound over $s$ gates forces error $\ge s\,2^{-\ell}$, capping the achievable *correlation* at $\mathrm{poly}(1/n)$ rather than $2^{-n^{\Omega(1)}}$. This is precisely the gap blocking (Q2) and hence (Q3).
- **Natural proofs.** Razborov–Rudich (1997): the approximation argument is constructive and applies to a $\ge 1/2$ fraction of functions. Any class rich enough to contain candidate PRFs — plausibly $\mathrm{AC}^0[\oplus]$ with $\omega(1)$ depth, certainly $\mathrm{TC}^0$ — is immune to such arguments if the relevant hardness assumptions hold.
- **Algorithmic method does not scale down.** Williams's framework needs a SAT algorithm beating brute force by a superpolynomial factor and a nondeterministic time hierarchy with enough room; the trade-off yields $\mathrm{NEXP}$/$\mathrm{NQP}$, not $\mathrm{NP}$. Shrinking the class costs a corresponding improvement in the SAT algorithm, which is not available.
- **Depth reduction runs the wrong way.** Beigel–Tarui/Yao-style reductions compress $\mathrm{ACC}^0$ to $\mathrm{SYM}\circ\mathrm{AND}$ of quasipolynomial size — a class for which no strong explicit lower bound is known, because symmetric top gates defeat both degree and switching arguments.

## 6. The Gap

Proven (§4): depth $d < c\log n/\log\log n$, worst case, correlation $1/2 + n^{-\Omega(1)}$.
Wanted (§1): depth $\omega(\log n/\log\log n)$, or correlation $1/2 + 2^{-n^{\Omega(1)}}$, or a majority gate on top.

The exact missing step is a hardness measure $\mu$ for Boolean functions with all three properties: (i) $\mu$ is subadditive/multiplicative under composition so that a depth-$d$ circuit has $\mu \le g(s)^d$ with $g$ growing more slowly than $\log s$ raised to depth; (ii) $\mu$ is provably large for an explicit NP function; (iii) $\mu$ is not "large" in the Razborov–Rudich sense, i.e. it is not satisfied by most random functions, or is not efficiently computable from the truth table. Every known $\mu$ ($\mathbb{F}_2$-approximate degree, probabilistic rank, certifying-polynomial degree, sensitivity) fails (i) or (iii).

## 7. Current Research (as of June 2026)

- **Algorithmic method, downward.** Chen–Lyu–Williams-style "almost-everywhere" lower bounds from nontrivial derandomization; the target is to trade the $\mathrm{NQP}$ time bound down toward $\mathrm{NP}$ by improving $\mathrm{ACC}^0$-$\mathrm{SAT}$ from $2^{n - n^{\delta}}$ to $2^{n^{1-\delta}}$. Active at MIT, Tsinghua (IIIS) and Oxford. *(frontier — verify)*
- **Sharper correlation bounds.** Refinements of certifying polynomials and of the coin-problem analysis, aiming at $2^{-n^{\Omega(1)}}$ correlation of $\mathrm{MOD}_3$ with polynomial-size $\mathrm{AC}^0[\oplus]$; Chennai Mathematical Institute / TIFR (Srinivasan and collaborators), Columbia (Servedio, Tan). *(frontier — verify)*
- **Probabilistic rank and rigidity.** Alman–Williams-style tools relating $\mathrm{AC}^0[\oplus]$ approximations to matrix rigidity; a rigid explicit matrix would give new depth-2 and $\mathrm{SYM}\circ\mathrm{AND}$ bounds.
- **Meta-complexity.** MCSP/Kolmogorov-complexity hardness magnification results: weak-looking bounds against $\mathrm{AC}^0[\oplus]$ for MCSP-like problems would already imply $\mathrm{NP} \not\subseteq \mathrm{AC}^0[\oplus]$-type separations at higher depth (Oliveira–Santhanam programme). *(frontier — verify)*

## 8. Future Work

1. **Break the $(\log s)^d$ degree recursion** — find an approximation scheme whose degree grows like $\mathrm{poly}(\log s) \cdot d$ rather than $(\log s)^d$, which would immediately push (Q1) to depth $n^{\Omega(1)}$.
2. **Exponential-error probabilistic polynomials.** Determine the minimum degree of an $\mathbb{F}_2$ probabilistic polynomial for $\mathrm{OR}_n$ with error $2^{-n^{\varepsilon}}$; a tight answer plus a matching Smolensky-type bound resolves (Q2).
3. **Hardness magnification.** Push magnification thresholds for MCSP and Gap-MKtP down to parameters where existing $\mathrm{AC}^0[\oplus]$ techniques apply, taking care that the resulting proof evades the natural-proofs barrier.
4. **Better $\mathrm{AC}^0[\oplus]$ SAT algorithms**, since by Williams's framework these convert directly into lower bounds for smaller nondeterministic classes.

## 9. Key References

- **[Foundational]** A. A. Razborov. *Lower bounds on the size of bounded depth circuits over a complete basis with logical addition.* Mathematical Notes of the Academy of Sciences of the USSR, 41(4):333–338, 1987.
- **[Foundational]** R. Smolensky. *Algebraic methods in the theory of lower bounds for Boolean circuit complexity.* STOC 1987, pp. 77–82.
- **[Foundational]** R. Smolensky. *On representations by low-degree polynomials.* FOCS 1993, pp. 130–138.
- **[Foundational]** J. Håstad. *Almost optimal lower bounds for small depth circuits.* STOC 1986, pp. 6–20.
- **[Barrier]** A. A. Razborov, S. Rudich. *Natural proofs.* Journal of Computer and System Sciences, 55(1):24–35, 1997.
- **[Foundational]** A. Hajnal, W. Maass, P. Pudlák, M. Szegedy, G. Turán. *Threshold circuits of bounded depth.* Journal of Computer and System Sciences, 46(2):129–154, 1993.
- **[SOTA / Recent]** R. Williams. *Nonuniform ACC circuit lower bounds.* Journal of the ACM, 61(1):2, 2014.
- **[SOTA / Recent]** C. D. Murray, R. R. Williams. *Circuit lower bounds for nondeterministic quasi-polytime: an easy witness lemma for NP and NQP.* STOC 2018, pp. 890–901.
- **[SOTA / Recent]** L. Chen, H. Ren. *Strong average-case circuit lower bounds from nontrivial derandomization.* STOC 2020, pp. 1327–1334.
- **[SOTA / Recent]** I. C. Oliveira, R. Santhanam, S. Srinivasan. *Parity helps to compute Majority.* CCC 2019, LIPIcs vol. 137, pp. 23:1–23:17.
- **[SOTA / Recent]** S. Kopparty, S. Srinivasan. *Certifying polynomials for $\mathrm{AC}^0[\oplus]$ circuits, with applications to lower bounds and circuit compression.* Theory of Computing, 14(12):1–24, 2018.
- **[SOTA / Recent]** R. A. Servedio, L.-Y. Tan. *Improved pseudorandom generators from pseudorandom multi-switching lemmas.* RANDOM 2019, LIPIcs vol. 145, pp. 45:1–45:23.
- **[Survey]** E. Viola. *On the power of small-depth computation.* Foundations and Trends in Theoretical Computer Science, 5(1):1–72, 2009.
- **[Survey]** R. Beigel. *The polynomial method in circuit complexity.* Structure in Complexity Theory Conference, 1993, pp. 82–95.
- **[Textbook]** S. Arora, B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009, Chapter 14.

## 10. Worked Example / Concrete Special Case

**Step 1: a degree-$\ell$ probabilistic polynomial for $\mathrm{OR}_m$ over $\mathbb{F}_2$.**
Draw independent uniform subsets $S_1,\dots,S_\ell \subseteq [m]$ and set
$$p(x) \;=\; 1 \;+\; \prod_{i=1}^{\ell}\Big(1 + \sum_{j \in S_i} x_j\Big) \pmod 2 .$$
Each factor has degree $1$, so $\deg p \le \ell$.

- If $x = 0^m$: each inner sum is $0$, every factor is $1$, so $p(x) = 1+1 = 0 = \mathrm{OR}(x)$. **Always correct.**
- If $x \ne 0^m$: fix $j_0$ with $x_{j_0}=1$. Conditioning on $S_i \setminus \{j_0\}$, the sum $\sum_{j\in S_i} x_j$ is uniform in $\mathbb{F}_2$, so each factor is $0$ with probability $1/2$, independently. Hence $\Pr[\text{all factors} = 1] = 2^{-\ell}$, and $p(x) = 1 = \mathrm{OR}(x)$ except with probability $2^{-\ell}$.

$\mathrm{AND}$ follows by De Morgan and $\oplus$ is exactly degree $1$, so **every gate** gets a degree-$\ell$, error-$2^{-\ell}$ approximator.

**Step 2: compose over the circuit.** For $C$ of size $s$ and depth $d$, replace each gate independently. Degrees multiply along a path: $\deg \le \ell^d$. By a union bound over gates and averaging over inputs, some fixed choice $p$ satisfies
$$\Pr_x[p(x) \ne C(x)] \le s\,2^{-\ell}.$$
Choose $\ell = \log(10s)$: error $\le 1/10$, degree $\le (\log 10s)^d$.

**Step 3: apply Smolensky.** If $C$ computes $\mathrm{MAJ}_n$ exactly, then $p$ approximates $\mathrm{MAJ}_n$ within error $1/10$, so $\deg p \ge c\sqrt n$. Therefore
$$(\log 10 s)^d \ \ge\ c\sqrt{n} \quad\Longrightarrow\quad \log s \ \ge\ c'\, n^{1/2d} \quad\Longrightarrow\quad s \ \ge\ 2^{\Omega(n^{1/2d})}.$$

**Step 4: numbers, and where it dies.** Take $n = 2^{24} \approx 1.7\times 10^7$.

| depth $d$ | $n^{1/2d}$ | implied size bound |
|---|---|---|
| $2$ | $2^{6} = 64$ | $2^{\Omega(64)}$ |
| $4$ | $2^{3} = 8$ | $2^{\Omega(8)}$ |
| $6$ | $2^{2} = 4$ | $2^{\Omega(4)}$ |
| $d = \tfrac{\log n}{2\log\log n} \approx 4.9$ | $2^{\log\log n} = \log n = 24$ | $s \ge n^{\Omega(1)}$ only |

At $d = \log n/(2\log\log n)$ the bound collapses to *polynomial*: $\log s \ge c' \log n$. Every gain must come from somewhere other than degree. That collapse, computed here on one line, is the whole content of the gap in §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*