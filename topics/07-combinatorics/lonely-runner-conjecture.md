---
id: 07-combinatorics/lonely-runner-conjecture
title: "Lonely Runner Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lonely Runner Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/lonely-runner-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k \ge 2$ runners start at the same point of a circular track of circumference $1$ and run forever at pairwise distinct constant speeds. A runner is called **lonely** at time $t$ if her distance along the track to every other runner is at least $1/k$.

**Conjecture (Lonely Runner).** For every choice of $k$ distinct speeds, every runner is lonely at some time $t > 0$.

Passing to the frame of the runner under consideration, the $k-1$ relative speeds are distinct and nonzero. Writing $n = k-1$, the conjecture takes its standard analytic form:

**Conjecture (equivalent form).** For all distinct nonzero reals $v_1,\dots,v_n$ there exists $t \in \mathbb{R}$ with
$$\|v_i t\| \;\ge\; \frac{1}{n+1} \qquad \text{for all } i = 1,\dots,n,$$
where $\|x\| = \min_{m \in \mathbb{Z}} |x - m|$ is the distance from $x$ to the nearest integer.

A complete proof must establish this for all $n$ and all speed sets; a disproof requires a single explicit $n$ and speed set $V$ whose **gap of loneliness**
$$\delta(V) \;=\; \sup_{t \in \mathbb{R}} \; \min_{1 \le i \le n} \|v_i t\|$$
satisfies $\delta(V) < 1/(n+1)$. The constant $1/(n+1)$ is optimal: $V = \{1,2,\dots,n\}$ gives $\delta(V) = 1/(n+1)$ exactly.

## 2. Mathematical Foundations

**Reduction to integers.** Since $\delta$ is scale-invariant ($\delta(cV) = \delta(V)$ for $c \neq 0$), invariant under $v_i \mapsto -v_i$, and continuous in the speeds under rational approximation combined with a compactness argument on the torus, it suffices to prove the conjecture for **distinct positive integers** $v_1 < \dots < v_n$. For integer speeds the supremum is attained, and $t$ may be taken in $[0,1)$ with denominator dividing $\mathrm{lcm}$-type quantities determined by $V$.

**Torus formulation.** Let $\mathbb{T} = \mathbb{R}/\mathbb{Z}$ and let $\gamma_V : \mathbb{T} \to \mathbb{T}^n$, $\gamma_V(t) = (v_1 t, \dots, v_n t)$, be the closed orbit of a one-parameter subgroup. Define the open "danger" set
$$B_\varepsilon = \{ x \in \mathbb{T}^n : \|x_i\| < \varepsilon \text{ for some } i \}.$$
The conjecture asserts $\gamma_V(\mathbb{T}) \not\subseteq B_{1/(n+1)}$.

**Trivial bound.** Each set $\{t \in \mathbb{T} : \|v_i t\| < \varepsilon\}$ has Lebesgue measure exactly $2\varepsilon$. A union bound with $\varepsilon = 1/(2n)$ has total measure $1$, and a closed-set/compactness refinement yields
$$\delta(V) \;\ge\; \frac{1}{2n} \quad \text{for every } n\text{-element speed set } V .$$
Improving the constant $\tfrac12$ in $1/(2n)$ to $1$ (asymptotically) is the whole content of the conjecture.

**View-obstruction formulation (Cusick).** Since $\|x\| \ge \frac{1}{n+1}$ is equivalent to $x$ lying within $\frac12 - \frac{1}{n+1}$ of a half-integer, the conjecture says: every ray $\{ t(v_1,\dots,v_n) : t>0 \}$ into the positive orthant meets some closed axis-parallel cube of edge length
$$\frac{n-1}{n+1} \;=\; 1 - \frac{2}{n+1}$$
centred at a point of $\mathbb{Z}^n + (\tfrac12,\dots,\tfrac12)$. Equivalently, cubes of that size placed at half-integer lattice points block all views from the origin.

**Graph-colouring formulation.** For a finite set $D$ of positive integers, the *distance graph* $G(\mathbb{Z},D)$ joins $u \sim v$ iff $|u-v| \in D$. The quantity $\delta(D)$ is the largest $\varepsilon$ for which $\mathbb{Z}$ admits a "$\varepsilon$-regular" colouring by arcs, and the conjecture is equivalent to the statement that every distance graph with $|D| = n$ has *regular chromatic number* at most $n+1$ (Barajas–Serra). A related consequence, isolated by Bienia, Goddyn, Gvozdjak, Sebő and Tarsi, links the problem to nowhere-zero flows in regular matroids.

## 3. History & State of the Art (SOTA)

- **1967 — Wills.** J. M. Wills formulated the problem in the language of simultaneous inhomogeneous Diophantine approximation and proved the case $n = 2$.
- **1972–1974 — Betke–Wills, Cusick.** The case $n = 3$ was settled independently. Cusick introduced the geometric *view-obstruction* framing in 1973 and made the same conjecture from that side.
- **1984 — Cusick–Pomerance.** The case $n = 4$, by a mixture of analytic estimates and machine-assisted case analysis.
- **1998 — Bienia, Goddyn, Gvozdjak, Sebő, Tarsi.** Coined the name "lonely runner", gave a short new proof of $n = 4$, and connected the problem to flows and view obstructions.
- **2001 — Bohman, Holzman, Kleitman.** The case $n = 5$ ("six lonely runners"), a long combinatorial argument; simplified by Renault (2004).
- **2008 — Barajas–Serra.** The case $n = 6$ ("the lonely runner with seven runners"), using the distance-graph/regular-chromatic-number machinery.
- **2018 — Tao.** Proved that for each $n$ the conjecture reduces to a *finite* check: speeds may be assumed bounded by $n^{Cn^2}$. He also gave the first improvement over the trivial constant, of the shape $\delta \ge \frac{1}{2n} + \frac{c\log n}{n^2 (\log\log n)^2}$ — an $O(\log n/\log\log n)$-factor gain, not a constant-factor one.
- **2011–2021 — Dubickas; Czerwiński; Perarnau–Serra; Beck–Hoşten–Schymura; Kravitz.** Improvements in the "many runners" and "generic speeds" regimes, polyhedral/computational reformulations, and structural classification of near-tight instances.

$n = 7$ (eight runners) remains open. No speed set with $\delta(V) < 1/(n+1)$ has ever been found, and extensive searches over integer speed sets support the conjecture, so its status is best described as open but strongly **empirically supported**.

## 4. Partial Results / Verified Cases

- **Full proof for $n \le 6$** (i.e. up to seven runners): $n=1,2$ elementary/Wills; $n=3$ Betke–Wills and Cusick; $n=4$ Cusick–Pomerance and Bienia et al.; $n=5$ Bohman–Holzman–Kleitman, simplified by Renault; $n=6$ Barajas–Serra.
- **Bounded speeds.** For each fixed $n$ the conjecture holds whenever the largest speed is small relative to $n$; Barajas–Serra proved it for speed sets $V \subseteq \{1,\dots,c\,n\}$ for an explicit constant, and Tao's reduction shows only speeds up to $n^{Cn^2}$ need be checked in general.
- **Generic / random speeds.** Czerwiński (2012) showed that for speeds chosen at random from $\{1,\dots,N\}$ the gap is at least $\tfrac12 - \varepsilon$ with probability tending to $1$ — far stronger than $1/(n+1)$. Dubickas (2011) proved the conjecture in the "many runners" regime for speed sets with $v_n$ large compared with $n$ under lacunarity-type hypotheses.
- **Structured speed sets.** The conjecture holds for arithmetic progressions, geometric-type sets, sets with $\gcd$ or divisibility structure, and sets of the form $\{1,\dots,n\}\cup\{\text{extra}\}$ via direct constructions of $t$.
- **Tightness classification.** Kravitz (2021) studied "barely lonely" instances, showing that $\delta(V)$ equal or very close to $1/(n+1)$ forces strong structure on $V$, with $\{1,2,\dots,n\}$ as the canonical extremal set.
- **Finite fields.** Czerwiński–Grytczuk (2008) proved the analogue over $\mathbb{F}_p$ ("invisible runners"), where character-sum methods apply cleanly.

## 5. Principal Obstacles

- **The union bound is exactly tight.** The measures of the $n$ danger arcs sum to exactly $1$ at $\varepsilon = 1/(2n)$. Any proof must exploit *correlations* between the sets $\{\|v_i t\| < \varepsilon\}$, and these correlations are governed by arithmetic relations among the $v_i$ that vary wildly across speed sets.
- **Fourier analysis loses a factor of 2.** Expanding indicator functions of arcs in characters produces main terms controlled by $\sum_i \varepsilon$ and error terms involving $\sum_{m} \hat{1}(m)$ over frequencies with $\sum m_i v_i = 0$. The number of such vanishing linear relations can be large (e.g. $V = \{1,\dots,n\}$), and the error terms are not small enough to beat the trivial bound by more than lower-order factors — precisely the barrier Tao's $\log n/\log\log n$ gain lives at.
- **No compactness across $n$.** Each new $n$ demands its own analysis; the proofs for $n=4,5,6$ are ad hoc case analyses of increasing length (the $n=6$ argument runs to tens of pages) and none of them generalises inductively. Removing one runner reduces $n$ but the target gap $1/(n+1)$ shifts, so induction on $n$ is not available.
- **The finite-check bound is astronomically large.** Tao's $n^{Cn^2}$ ceiling makes exhaustive verification infeasible already at $n = 7$; polyhedral methods (Beck–Hoşten–Schymura) reduce this to lattice-point counting in "lonely runner polyhedra" but the complexity still grows super-exponentially.
- **Extremal instances are non-isolated.** Because $\{1,\dots,n\}$ is exactly tight, no argument with slack can work; the proof must be sharp at a family of hard instances for every $n$.

## 6. The Gap

Proven: the statement for $n \le 6$, plus the universal bound $\delta(V) \ge \frac{1}{2n}(1 + o(1))$ with a $\log n/\log\log n$-type improvement, plus the conjecture for almost all speed sets and for various structured families.

Required: closing the **factor-of-two gap** between the trivial threshold $\frac{1}{2n}$ and the conjectured $\frac{1}{n+1}$, uniformly in $n$ and over all speed sets — in particular for the worst-case sets where the $n$ danger arcs are nearly disjoint on average yet the arithmetic structure is not restrictive enough to force a large gap. Concretely: no known method yields a bound of the form $\delta(V) \ge \frac{c}{n}$ with $c > \tfrac12$, for any $c$, for all $n$. Even $c = 0.51$ would be a landmark.

## 7. Current Research (as of June 2026)

- **Polyhedral and computational attacks.** The lonely-runner-polyhedra programme of Beck, Hoşten and Schymura recasts $\delta(V) \ge 1/(n+1)$ as feasibility of an explicit polyhedron; groups in Berlin/Magdeburg and San Francisco State continue to push the $n = 7$ case with integer-programming and lattice-reduction certificates. *(frontier — verify)*
- **Structural/extremal school.** Following Kravitz, work on "barely lonely" and "very lonely" runners aims to classify all $V$ with $\delta(V)$ below $1/n$, in the hope that the hard cases form a thin, describable family (Princeton/Stanford-affiliated combinatorialists).
- **Analytic school.** Refinements of Tao's approach, seeking a genuine constant-factor improvement over $1/(2n)$ via second-moment methods, sieve-type inclusion–exclusion on correlations, and Bohr-set decompositions of the speed set. No published constant-factor improvement exists. *(frontier — verify)*
- **Graph-theoretic school.** Barajas–Serra–Perarnau's regular chromatic number of distance graphs, and Goddyn's flow-conjecture connections, remain active in Barcelona (UPC) and Vancouver (SFU).
- **Variants.** Shifted lonely runner (runners with distinct starting positions), where counterexamples to the naive $1/k$ bound are known, sharpening what is special about the common start; and $\mathbb{F}_p$/function-field analogues.

## 8. Future Work

- Prove $\delta(V) \ge \frac{c}{n}$ with an absolute $c > 1/2$ for all $n$: a constant-factor beating of the union bound is widely regarded as the decisive first step.
- Reduce Tao's $n^{Cn^2}$ speed bound to something polynomial or singly exponential in $n$, which would make $n = 7$ and possibly $n = 8$ machine-decidable.
- Develop an induction or "runner-removal" scheme robust to the change of target gap, perhaps by proving a weighted or fractional version of the conjecture that is self-improving.
- Complete the classification of near-extremal speed sets, then handle the remaining generic sets by the probabilistic method (Czerwiński's regime) — a two-regime strategy repeatedly proposed but not yet joined at the seam.
- Settle the $n = 7$ case by any means; historically each new case has produced a technique later reused.

## 9. Key References

- **[Foundational]** J. M. Wills. *Zwei Sätze über inhomogene diophantische Approximation von Irrationalzahlen.* Monatshefte für Mathematik 71 (1967), 263–269.
- **[Foundational]** T. W. Cusick. *View-obstruction problems.* Aequationes Mathematicae 9 (1973), 165–170.
- **[Foundational]** U. Betke, J. M. Wills. *Untere Schranken für zwei diophantische Approximations-Funktionen.* Monatshefte für Mathematik 76 (1972), 214–217.
- **[Case $n=4$]** T. W. Cusick, C. Pomerance. *View-obstruction problems, III.* Journal of Number Theory 19 (1984), 131–139.
- **[Naming / flows]** W. Bienia, L. Goddyn, P. Gvozdjak, A. Sebő, M. Tarsi. *Flows, view obstructions, and the lonely runner.* Journal of Combinatorial Theory, Series B 72 (1998), 1–9.
- **[Case $n=5$]** T. Bohman, R. Holzman, D. Kleitman. *Six lonely runners.* Electronic Journal of Combinatorics 8 (2001), \#R3.
- **[Simplification]** J. Renault. *View-obstruction: a shorter proof for 6 lonely runners.* Discrete Mathematics 287 (2004), 93–101.
- **[Case $n=6$]** J. Barajas, O. Serra. *The lonely runner with seven runners.* Electronic Journal of Combinatorics 15 (2008), \#R48.
- **[SOTA]** T. Tao. *Some remarks on the lonely runner conjecture.* Contributions to Discrete Mathematics 13 (2018), 1–31.
- **[SOTA / probabilistic]** S. Czerwiński. *Random runners are very lonely.* Journal of Combinatorial Theory, Series A 119 (2012), 1194–1199.
- **[Related]** S. Czerwiński, J. Grytczuk. *Invisible runners in finite fields.* Information Processing Letters 108 (2008), 64–67.
- **[Many runners]** A. Dubickas. *The lonely runner problem for many runners.* Glasnik Matematicki 46 (2011), 25–30.
- **[Correlations]** G. Perarnau, O. Serra. *Correlation among runners and some results on the lonely runner conjecture.* Electronic Journal of Combinatorics 23 (2016), \#P1.50.
- **[Polyhedral]** M. Beck, S. Hoşten, M. Schymura. *Lonely Runner Polyhedra.* Experimental Mathematics 30 (2021), 296–304.
- **[Structural]** N. Kravitz. *Barely lonely runners and very lonely runners: a refined approach to the Lonely Runner Conjecture.* Combinatorial Theory 1 (2021).
- **[Related, cubes]** Y. G. Chen, T. W. Cusick. *The view-obstruction problem for $n$-dimensional cubes.* Journal of Number Theory 74 (1999), 126–133.

## 10. Worked Example / Concrete Special Case

**The extremal set $V = \{1,2,3\}$ ($n = 3$, four runners).** Target gap $\frac{1}{n+1} = \frac14$.

*Achievability.* Take $t = \tfrac14$:
$$\|1 \cdot \tfrac14\| = \tfrac14, \qquad \|2 \cdot \tfrac14\| = \|\tfrac12\| = \tfrac12, \qquad \|3\cdot \tfrac14\| = \|\tfrac34\| = \tfrac14 .$$
So $\min_i \|v_i t\| = \tfrac14$ and the conjecture holds for this set.

*Optimality — $\delta(\{1,2,3\}) = \tfrac14$ exactly.* Suppose $\min_i \|v_i t\| > \tfrac14$ for some $t$. Replacing $t$ by $1-t$ if necessary (which preserves all $\|v_i t\|$), we may take $t \in (0,\tfrac12]$.

1. $\|t\| > \tfrac14$ forces $t \in (\tfrac14, \tfrac12]$.
2. Then $2t \in (\tfrac12, 1]$. Requiring $\|2t\| > \tfrac14$ excludes $2t \in [\tfrac34, 1]$, so $2t \in (\tfrac12, \tfrac34)$, i.e. $t \in (\tfrac14, \tfrac38)$.
3. Then $3t \in (\tfrac34, \tfrac98)$. Requiring $\|3t\| > \tfrac14$ means $|3t - 1| > \tfrac14$, so $3t > \tfrac54$, i.e. $t > \tfrac{5}{12} \approx 0.4167$.

But step 2 gave $t < \tfrac38 = 0.375$. Contradiction. Hence no $t$ beats $\tfrac14$, and $\delta = \tfrac14$: the bound $1/(n+1)$ cannot be improved.

**A non-extremal contrast: $V = \{1,2,5\}$.** Take $t = \tfrac13$:
$$\|\tfrac13\| = \tfrac13, \qquad \|\tfrac23\| = \tfrac13, \qquad \|\tfrac53\| = \|\tfrac23\| = \tfrac13 .$$
Here $\delta \ge \tfrac13 > \tfrac14$. The general conjecture must therefore be sharp only on the arithmetically rigid sets like $\{1,\dots,n\}$ while remaining valid on all the loose ones — the tension that makes averaging arguments stall at $1/(2n)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*