---
id: 07-combinatorics/erdos-gyarfas-conjecture
title: "Erdős-Gyárfás Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Gyárfás Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-gyarfas-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Erdős–Gyárfás, 1995).** Every finite simple graph $G$ with minimum degree $\delta(G) \ge 3$ contains a simple cycle whose length is a power of two.

Formally, writing $\mathcal{L}(G) = \{\,\ell : G \text{ contains a cycle } C_\ell\,\}$ for the cycle spectrum of $G$:

$$\delta(G)\ge 3 \;\Longrightarrow\; \mathcal{L}(G)\cap\{4,8,16,32,64,\dots\}\neq\emptyset .$$

(Since a cycle has length $\ge 3$, the relevant powers are $2^k$ with $k\ge 2$.)

A proof must handle all graphs of minimum degree $3$, including sparse cubic graphs of arbitrarily large girth and arbitrarily large order. A disproof requires one explicit finite graph $G$ with $\delta(G)\ge 3$ and $\mathcal{L}(G)\cap\{2^k\}=\emptyset$; because cycle spectra are computable, any such counterexample is finitely verifiable. Erdős offered \$100 for a proof and \$50 for a counterexample; his stated expectation late in life was that the conjecture is **false**, with counterexamples of large girth.

Two immediate remarks fix the scope:

- The degree bound is sharp. $\delta(G)\ge 2$ is insufficient: any cycle $C_n$ with $n$ not a power of two is a $2$-regular counterexample.
- The conjecture is not "cycle lengths are dense". A graph with $\delta\ge3$ may have very few distinct cycle lengths; the claim is only that at least one of the sparse set $\{2^k\}$ is hit.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, simple, undirected, $n=|V|$, $m=|E|$. Standard parameters:

$$\delta(G)=\min_{v\in V}\deg(v),\qquad d(G)=\frac{2m}{n},\qquad g(G)=\min \mathcal{L}(G)\ \ (\text{girth}).$$

**Reduction to edge-minimal graphs.** If $G$ is a counterexample and $e\in E$ with $\delta(G-e)\ge3$, then $G-e$ is also a counterexample, since $\mathcal{L}(G-e)\subseteq\mathcal{L}(G)$. Hence a minimal counterexample is *edge-minimal subject to $\delta\ge3$*: every edge has an endpoint of degree exactly $3$. Cubic graphs are therefore the paradigm case, though not a formal reduction (subdividing edges to cubify changes all cycle lengths).

**Counting bound.** A graph with $\delta\ge3$ has $m\ge \tfrac{3n}{2}$, so it contains at least $m-n+1\ge \tfrac n2+1$ independent cycles (cyclomatic number $\mu(G)=m-n+c$). The obstruction is that these cycles may all have lengths avoiding $\{2^k\}$.

**Even-cycle machinery.** The relevant general tools produce *intervals* of even cycle lengths:

- *Bondy–Simonovits (1974).* If $m > 100k\,n^{1+1/k}$ then $C_{2\ell}\subseteq G$ for every $\ell\in[k,\,kn^{1/k}]$.
- *Sudakov–Verstraëte (2008).* A graph of average degree $d$ and girth $g$ contains cycles of at least $c\,d^{\lfloor (g-1)/2\rfloor}$ consecutive even lengths.
- *Gao–Huo–Liu–Ma (2022).* $\delta(G)\ge k+1$ forces $k$ cycles of consecutive even lengths; if $G$ is additionally $2$-connected and non-bipartite, $k$ cycles of consecutive lengths.

An interval of even lengths $[a,a+2t]$ contains a power of two whenever $t \gtrsim a$, because consecutive powers of two are separated by a multiplicative factor $2$. So interval methods settle the conjecture exactly when the guaranteed interval length is comparable to the shortest cycle length — i.e. when the graph is dense — and say nothing when $\delta=3$ and $a\sim n$.

**Extremal formulation.** Define $f(n)$ as the maximum number of edges of an $n$-vertex graph with no cycle of power-of-two length. The conjecture is equivalent to the statement that every such graph has a vertex of degree $\le 2$, hence (peeling iteratively) is $2$-degenerate and satisfies $f(n)\le 2n-3$.

## 3. History & State of the Art (SOTA)

- **Origin.** Posed by Paul Erdős and András Gyárfás around 1995 and circulated in Erdős's problem lists; recorded in P. Erdős, *Some old and new problems in various branches of combinatorics*, Discrete Mathematics 165/166 (1997), 227–231. The companion paper Erdős–Gyárfás, *Split and balanced colorings of complete graphs*, Discrete Math. 200 (1999), 79–86, is often cited alongside.
- **Late 1990s.** S. E. Shauger, *Results and conjectures on the Erdős–Gyárfás problem*, Congressus Numerantium 134 (1998), obtains the first structural partial results, ruling out counterexamples containing large induced stars under degree hypotheses.
- **2001.** D. P. Daniel and S. E. Shauger, *A result on the Erdős–Gyárfás conjecture in planar graphs*, Congressus Numerantium 153 (2001), 129–139: the conjecture holds for planar claw-free graphs.
- **2004.** K. Markström, *Extremal graphs for some problems on cycles in graphs*, Congressus Numerantium 171 (2004), 179–192: exhaustive computer search shows any counterexample has at least $17$ vertices, and exhibits $24$-vertex cubic graphs whose *only* power-of-two cycle length is $16$ — i.e. the "margin" in the conjecture can be a single length.
- **2013.** C. C. Heckman and R. Krakovski, *Erdős–Gyárfás conjecture for cubic planar graphs*, Electronic Journal of Combinatorics 20(2) (2013), \#P7: the conjecture holds for $3$-connected cubic planar graphs.
- **2014.** P. S. Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi, K. Bibak, *On the Erdős–Gyárfás conjecture in claw-free graphs*, Discussiones Mathematicae Graph Theory 34 (2014), 635–640: the conjecture holds for claw-free graphs with $\delta \ge 3$.
- **Dense/chromatic regimes.** Bondy–Simonovits, Sudakov–Verstraëte, and Kostochka–Sudakov–Verstraëte (*Cycles in triangle-free graphs of large chromatic number*, Combinatorica 37 (2017), 481–494) give power-of-two cycles for free in every regime where the graph is dense, of large chromatic number, or has many short cycles.

**Status as of 2026: open.** No counterexample is known; no proof covers general cubic graphs of large girth.

## 4. Partial Results / Verified Cases

| Class / range | Result | Source |
|---|---|---|
| $n\le 16$, $\delta\ge3$ | No counterexample (exhaustive search) | Markström 2004 |
| $3$-connected cubic **planar** | Conjecture true | Heckman–Krakovski 2013 |
| Planar **claw-free** | Conjecture true | Daniel–Shauger 2001 |
| **Claw-free** ($K_{1,3}$-free), $\delta\ge3$ | Conjecture true | Nowbandegani et al. 2014 |
| $m>100k\,n^{1+1/k}$ (e.g. $m\ge n^{1+\varepsilon}$) | All even lengths in a long interval, hence some $2^k$ | Bondy–Simonovits 1974 |
| Average degree $d$, girth $g$ with $d^{\lfloor(g-1)/2\rfloor}\gtrsim n$ | $\Omega(n)$ consecutive even lengths, hence some $2^k$ | Sudakov–Verstraëte 2008 |
| Triangle-free with chromatic number $k$ | $\Omega(k^2\log k)$ distinct cycle lengths, covering $\{2^j\}$ for large $k$ | Kostochka–Sudakov–Verstraëte 2017 |
| $\delta\ge k+1$ | $k$ cycles of consecutive even lengths (partial: locates an interval, not a power of $2$) | Gao–Huo–Liu–Ma 2022 |
| Random cubic graphs | Cycles of every length $\ell = O(\log n)$ a.a.s., including $2^k$ | Standard small-subgraph / second-moment arguments |

The residual open case is: **cubic (or edge-minimal $\delta=3$), non-planar, high girth, structured (non-random) graphs.**

## 5. Principal Obstacles

- **Sparsity kills counting.** With $m=\tfrac32 n$, the number of cycles can be as small as exponential-in-nothing useful; extremal even-cycle theorems (Bondy–Simonovits, Erdős–Gallai) require superlinear edge counts and give no information at $d=3$.
- **Interval methods scale wrongly.** Every known "many cycle lengths" theorem yields $\Theta(\delta)$ or $\Theta(d^{(g-1)/2})$ consecutive even lengths. Powers of two are multiplicatively spaced: to catch $2^k$ near length $\ell$ one needs an interval of width $\Theta(\ell)$. At $\delta=3$ the guaranteed width is $O(1)$, so the target is missed by a factor of $n$.
- **Girth destroys local structure.** Claw-free and planar proofs are local/discharging arguments: they find a short configuration forcing a $4$- or $8$-cycle. In a cubic graph of girth $\ge 20$ no short cycle exists, so all local certificates vanish and the required cycle has length $2^k \ge 32$, which no discharging scheme currently produces.
- **No algebraic handle.** Cycle lengths mod small integers are accessible (cycle space over $\mathbb{F}_2$, ear decompositions), but "is a power of two" is not a congruence condition and is invisible to $\mathbb{F}_2$ or $\mathbb{Z}_m$ linear algebra, to eigenvalue methods (spectral bounds control girth and even-cycle counts, not exact lengths), and to the regularity method (vacuous at density $o(1)$).
- **Markström's near-misses.** The existence of $24$-vertex cubic graphs whose only power-of-two cycle is $C_{16}$ shows the statement has essentially zero slack; any proof strategy that discards even one candidate length can fail.
- **Expected falsity.** Erdős himself expected a large-girth counterexample. Random cubic graphs are not counterexamples (they contain all short cycle lengths a.a.s.), so a counterexample must be an explicit algebraic or recursive construction — and no known construction family (generalized polygons, Ramanujan graphs, cages, snarks) controls the *entire* cycle spectrum well enough to exclude all of $\{4,8,\dots,2^{\lfloor \log_2 n\rfloor}\}$.

## 6. The Gap

Proven: the conjecture whenever the graph is *locally rich* (claw-free, planar cubic, dense, large chromatic number) or *small* ($n\le16$). Claimed: all graphs with $\delta\ge3$.

The precise barrier: for a cubic graph $G$ of girth $g\ge 10$ and order $n$, no technique produces a *specific* cycle length. The available theorems give a set $S\subseteq\mathcal{L}(G)$ that is an interval of even numbers of width $O(1)$ located at an unknown position in $[g,n]$. Crossing the gap requires either

1. a mechanism that *shifts* a found cycle's length by a controlled amount (an "ear-exchange" or rerouting calculus turning a $C_\ell$ into a $C_{\ell'}$ for a prescribed $\ell'<\ell$, ideally halving), or
2. a probabilistic/entropy argument showing that in any cubic graph the cycle spectrum has upper density bounded below in $[n^{\alpha}, n]$, forcing a power of two;

or, in the negative direction, an explicit construction whose cycle spectrum is provably contained in a power-of-two-free set such as $\{\ell : \ell \equiv 3,5,6 \pmod 7\}$-type residue families.

## 7. Current Research (as of June 2026)

- **Cycle-spectrum school (Ma, Liu, Gao, Huo; USTC / Texas A&M).** The unified framework of *A unified proof of conjectures on cycle lengths in graphs* (IMRN 2022) settled Thomassen's and Bondy–Vince-type conjectures via minimum degree; extending it from "consecutive even lengths" to "multiplicatively spread lengths" is the natural next target. No such extension exists yet. *(frontier — verify)*
- **Extremal/probabilistic (Verstraëte, Sudakov, and collaborators; UCSD, Oxford).** Refinements of the girth-versus-cycle-length trade-off, aimed at lowering the density threshold at which a full interval of even lengths appears.
- **Structural discharging (Heckman and successors; Arizona State).** Attempts to lift the cubic planar proof to bounded genus or to $K_5$-minor-free cubic graphs; the discharging weights used in the planar case rely on Euler's formula and do not survive increased genus. *(frontier — verify)*
- **Computational search.** Extensions of Markström's search using modern cubic-graph generators (`genreg`, `snarkhunter`) push exhaustive verification well past $n=17$ for cubic graphs; catalogued results at larger $n$ have not, to our knowledge, produced a counterexample. *(frontier — verify)*
- **Erdős Problems project.** The problem is tracked as an active open Erdős problem with the stated prize, and remains listed as unsolved.

## 8. Future Work

1. **Genus and minor-closed extensions.** Prove the conjecture for cubic graphs embeddable in the torus, or for cubic $K_{3,3}$-minor-free graphs, replacing Euler-formula discharging with a bounded-genus analogue.
2. **Girth-parameterised attack.** Prove: every cubic graph of girth $\ge g_0$ contains a cycle of length $2^k$ for some $k \le \log_2 n$. Even the weaker "contains a cycle of length in $[\ell,2\ell]$ for every $\ell$ in a range" would suffice.
3. **Search for counterexamples in algebraic families.** Compute cycle spectra of cubic incidence graphs of generalized polygons, LPS Ramanujan graphs, and cyclic lifts of small cubic graphs; lifts are the most promising, since cycle lengths in a $\mathbb{Z}_q$-lift are governed by voltage sums and are partially controllable.
4. **Weakened targets.** Establish the conjecture for the sparser target set $\{2^k\}$ replaced by $\{c\cdot 2^k\}$ for some constant $c$, or prove that $\delta\ge3$ forces a cycle whose length has at most $O(1)$ odd part — this would be the first genuinely multiplicative cycle-length theorem.
5. **Degenerate reformulation.** Prove $f(n)\le 2n-3$ (Section 2) directly by extremal counting, decoupling the problem from cycle-finding.

## 9. Key References

- **[Foundational]** P. Erdős. *Some old and new problems in various branches of combinatorics.* Discrete Mathematics 165/166 (1997), 227–231.
- **[Foundational]** P. Erdős and A. Gyárfás. *Split and balanced colorings of complete graphs.* Discrete Mathematics 200 (1999), 79–86.
- **[Foundational]** J. A. Bondy and M. Simonovits. *Cycles of even length in graphs.* Journal of Combinatorial Theory, Series B 16 (1974), 97–105.
- **[Partial]** S. E. Shauger. *Results and conjectures on the Erdős–Gyárfás problem.* Congressus Numerantium 134 (1998), 61–65.
- **[Partial]** D. P. Daniel and S. E. Shauger. *A result on the Erdős–Gyárfás conjecture in planar graphs.* Congressus Numerantium 153 (2001), 129–139.
- **[Computational]** K. Markström. *Extremal graphs for some problems on cycles in graphs.* Congressus Numerantium 171 (2004), 179–192.
- **[SOTA]** C. C. Heckman and R. Krakovski. *Erdős–Gyárfás conjecture for cubic planar graphs.* Electronic Journal of Combinatorics 20(2) (2013), \#P7.
- **[SOTA]** P. S. Nowbandegani, H. Esfandiari, M. H. Shirdareh Haghighi and K. Bibak. *On the Erdős–Gyárfás conjecture in claw-free graphs.* Discussiones Mathematicae Graph Theory 34(3) (2014), 635–640.
- **[SOTA]** B. Sudakov and J. Verstraëte. *Cycle lengths in sparse graphs.* Combinatorica 28 (2008), 357–372.
- **[SOTA]** J. Gao, Q. Huo, C.-H. Liu and J. Ma. *A unified proof of conjectures on cycle lengths in graphs.* International Mathematics Research Notices 2022(10) (2022), 7615–7653.
- **[Related]** A. Kostochka, B. Sudakov and J. Verstraëte. *Cycles in triangle-free graphs of large chromatic number.* Combinatorica 37 (2017), 481–494.
- **[Survey]** J. Verstraëte. *Extremal problems for cycles in graphs.* In: Recent Trends in Combinatorics, IMA Volumes in Mathematics and its Applications 159, Springer, 2016, 83–116.

## 10. Worked Example / Concrete Special Case

**Claim.** Every cubic graph $G$ of girth $3$ with $n \ge 4$ that contains two triangles sharing a vertex-disjoint connection of length $\le 2$ has a $4$-cycle or an $8$-cycle. Rather than the general claim, take the cleanest concrete instances.

*Instance 1: $K_4$.* $\delta=3$, $\mathcal{L}(K_4)=\{3,4\}$. The four vertices $\{1,2,3,4\}$ give the $4$-cycle $1\!-\!2\!-\!3\!-\!4\!-\!1$ (the complement of the perfect matching $\{13,24\}$). Conjecture verified with $2^2$.

*Instance 2: the Petersen graph $P$.* Cubic, girth $5$, $n=10$, $\mathcal{L}(P)=\{5,6,8,9\}$ (it has no $7$-cycle and no Hamilton cycle). Since $8=2^3\in\mathcal{L}(P)$, the conjecture holds. Explicitly, with the Kneser labelling $V=\binom{[5]}{2}$ and adjacency $A\sim B \iff A\cap B=\emptyset$, the cycle
$$12 - 34 - 15 - 23 - 45 - 13 - 25 - 14 - 12$$
is an $8$-cycle: each consecutive pair is disjoint ($\{1,2\}\cap\{3,4\}=\emptyset$, $\{3,4\}\cap\{1,5\}=\emptyset$, …, $\{1,4\}\cap\{1,2\}$ — note this last pair intersects, so replace the final step by $14-35-12$, giving instead the closed walk of length $9$). Correcting: the standard $8$-cycle is
$$12-34-51-23-45-13-24-35-12,$$
where consecutive pairs are disjoint at every step and $\{3,5\}\cap\{1,2\}=\emptyset$ closes the cycle. All eight vertices are distinct, so $C_8\subseteq P$.

*Why this is not routine.* $P$ is $3$-regular with only four distinct cycle lengths out of the eight conceivable values $3,\dots,10$; exactly one of them, $8$, is a power of two. Delete any single edge from $P$ and $\delta$ drops to $2$, so the conjecture no longer applies. Markström's $24$-vertex examples show the same knife-edge at larger scale: the whole spectrum can meet $\{2^k\}$ in the single value $16$.

*Contrast with $\delta=2$.* The $5$-cycle $C_5$ has $\mathcal{L}=\{5\}$, disjoint from $\{2^k\}$. Adding a chord to $C_5$ raises two vertices to degree $3$ but leaves three vertices of degree $2$, and the spectrum becomes $\{3,4,5\}$ — a $4$-cycle appears the moment the graph is forced towards $\delta=3$. This is the heuristic behind the conjecture: forcing degree $3$ everywhere generates so many overlapping cycles that the multiplicatively sparse set $\{2^k\}$ should still be hit. Making the heuristic quantitative at girth $\ge 10$ is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*