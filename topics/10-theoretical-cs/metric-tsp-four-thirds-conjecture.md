---
id: 10-theoretical-cs/metric-tsp-four-thirds-conjecture
title: "Metric TSP Four Thirds Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Metric TSP Four Thirds Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/metric-tsp-four-thirds-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be the complete graph on $n=|V|$ vertices with costs $c:E\to\mathbb{R}_{\ge 0}$ satisfying the triangle inequality $c(uv)\le c(uw)+c(wv)$. Let $\mathrm{OPT}(c)$ be the minimum cost of a Hamiltonian cycle, and let $\mathrm{SUBT}(c)$ be the optimum of the Dantzig–Fulkerson–Johnson *subtour elimination LP* (equivalently, the Held–Karp bound).

**Conjecture (integrality gap of the subtour LP).**
$$\sup_{n,\;c\ \mathrm{metric}}\ \frac{\mathrm{OPT}(c)}{\mathrm{SUBT}(c)}\ =\ \frac{4}{3}.$$

The lower bound $\ge 4/3$ is known and easy; the content is the upper bound
$$\mathrm{OPT}(c)\ \le\ \tfrac43\,\mathrm{SUBT}(c)\qquad\text{for every metric } c .$$

A complete proof must exhibit, for every metric instance, a Hamiltonian cycle of cost at most $\tfrac43\mathrm{SUBT}(c)$ (existence suffices; a polynomial-time construction is a strictly stronger, and also desired, statement). A disproof requires a family of metrics with $\mathrm{OPT}/\mathrm{SUBT}\to \rho>4/3$. The related *algorithmic* conjecture — that metric TSP admits a polynomial-time $4/3$-approximation — follows from the constructive form, since $\mathrm{SUBT}$ is computable in polynomial time (ellipsoid method with a min-cut separation oracle).

## 2. Mathematical Foundations

For $S\subsetneq V$, $S\neq\emptyset$, write $\delta(S)=\{uv\in E: |\{u,v\}\cap S|=1\}$ and $x(F)=\sum_{e\in F}x_e$. The subtour elimination LP is

$$
\mathrm{SUBT}(c)=\min\ \sum_{e\in E}c_e x_e
\quad\text{s.t.}\quad
\begin{cases}
x(\delta(v))=2, & v\in V,\\[2pt]
x(\delta(S))\ge 2, & \emptyset\neq S\subsetneq V,\\[2pt]
0\le x_e\le 1, & e\in E .
\end{cases}
$$

Its feasible region is the *subtour polytope* $\mathrm{SEP}_n$; incidence vectors of Hamiltonian cycles are exactly its integral points, so $\mathrm{SUBT}(c)\le\mathrm{OPT}(c)$ and the ratio in Section 1 is the **integrality gap** $\gamma_n=\max_c \mathrm{OPT}(c)/\mathrm{SUBT}(c)$; the conjecture is $\sup_n\gamma_n=4/3$.

Structural facts the problem rests on:

- **Held–Karp duality.** $\mathrm{SUBT}(c)=\max_{\pi\in\mathbb{R}^V}\big(\mathrm{MST}(c_\pi)+2\sum_v\pi_v\big)$ with $c_\pi(uv)=c(uv)-\pi_u-\pi_v$ (Held–Karp 1970). Hence $\mathrm{SUBT}$ dominates the spanning-tree relaxation.
- **Subtour ⊇ spanning trees.** For $x\in\mathrm{SEP}_n$, the scaled vector $\frac{n-1}{n}x$ lies in the spanning tree polytope; consequently $\mathrm{MST}(c)\le\mathrm{SUBT}(c)$ (Wolsey 1980; Shmoys–Williamson 1990).
- **T-joins and matchings.** For $T\subseteq V$ of even size, $\frac12 x$ restricted appropriately is feasible for the $T$-join polyhedron, giving a perfect matching on the odd-degree vertices of any spanning tree of cost $\le\frac12\mathrm{SUBT}(c)$.
- **Christofides–Serdyukov bound.** Combining the two: $\mathrm{OPT}\le \mathrm{MST}+\tfrac12\mathrm{SUBT}\le\tfrac32\mathrm{SUBT}$, so $\gamma_n\le 3/2$ (Wolsey 1980; Shmoys–Williamson 1990).
- **Half-integrality.** Every extreme point of $\mathrm{SEP}_n$ has $x_e\ge 1/n$-type support bounds; the *half-integral* vertices ($x_e\in\{0,\frac12,1\}$) are conjectured to be the worst case for the gap and are the arena of most recent progress.

The known lower bound $\gamma_n\to 4/3$ comes from families of graphic (shortest-path) metrics whose LP optimum is a half-integral vector of value $\approx n$, while every tour costs $\approx \tfrac43 n$.

## 3. History & State of the Art (SOTA)

- **1954.** Dantzig, Fulkerson and Johnson introduce the subtour relaxation while solving a 49-city instance.
- **1970.** Held and Karp give the Lagrangian/1-tree view, making the bound computable and empirically very tight.
- **1976/1978.** Christofides and, independently, Serdyukov give the tree-plus-matching algorithm with ratio $3/2$.
- **1980–1990.** Wolsey, then Shmoys and Williamson, show the $3/2$ analysis holds against $\mathrm{SUBT}$, so $\gamma_n\le 3/2$. The $4/3$ conjecture is folklore from this period (often attributed to Cunningham; recorded by Goemans 1995).
- **1995.** Goemans compares valid inequalities and formalises worst-case gap questions.
- **2011–2014.** Graphic TSP (all costs from an unweighted graph metric) breaks $3/2$: Oveis Gharan–Saberi–Singh $1.5-\varepsilon$, Mömke–Svensson $1.461$, Mucha $13/9$, Sebő–Vygen $7/5$.
- **2020–2022.** Karlin, Klein and Oveis Gharan give a randomized $\left(\tfrac32-\varepsilon_0\right)$-approximation for general metric TSP with $\varepsilon_0>10^{-36}$ (STOC 2021), and then the same improvement for the integrality gap itself (FOCS 2022). This is the first unconditional improvement over $3/2$ in 45 years.
- **SOTA today.** Upper bound $\gamma\le \tfrac32-10^{-36}$; lower bound $\gamma\ge \tfrac43$. Complexity side: metric TSP is APX-hard, NP-hard to approximate within $123/122$ (Karpinski–Lampis–Schmied 2015), so a $4/3$ algorithm would be near the hardness frontier but not contradict it.

## 4. Partial Results / Verified Cases

- **Cubic and subcubic graphs.** For 2-connected cubic graphs, Boyd, Sitters, van der Ster and Stougie (2014) give a $4/3$-approximation and prove the subtour gap is at most $4/3$ for subcubic graphic metrics. Correa, Larré and Soto (2015) push cubic graphs below: $4/3-1/61236$. Van Zuylen (2018) gives $4/3$ for cubic graphs by a simpler argument and $5/4$ for cubic bipartite.
- **Half-integral instances.** Karlin–Klein–Oveis Gharan (STOC 2020) give $1.49993$ for half-integral LP solutions; Gupta, Lee, Li, Mucha, Newman and Sarkar (IPCO 2022) improve to $1.4$ via matroid-based rounding. Haddadan–Newman (2019) obtained $1.4$ for the structured "$\frac12$-integer" family arising from $k$-donuts.
- **Small $n$.** Benoit and Boyd (2008) compute the exact worst-case gap for all $n\le 10$ by enumerating extreme points of $\mathrm{SEP}_n$; every value is strictly below $4/3$ and increases with $n$. Boyd and Elliott-Magwood extended the structural enumeration of extreme points to slightly larger $n$.
- **Two-matching relaxation (Boyd–Carr conjecture).** Schalekamp, Williamson and van Zuylen (2014) prove that the ratio of the minimum cost fractional/integral 2-matching to $\mathrm{SUBT}$ is exactly $4/3$ — the $4/3$ constant is provably correct one relaxation "below" TSP.
- **Path variants.** For $s$–$t$ path TSP, whose LP gap is exactly $3/2$, Zenklusen (2019) achieves $3/2$, matching the gap; Traub–Vygen give $1.5+\varepsilon$ and refinements. This confirms that gap-matching algorithms are attainable in cognate models.
- **Graphic metrics.** $\gamma\le 7/5$ (Sebő–Vygen 2014) for the special case of unweighted graph metrics, the closest general-family approach to $4/3$.

## 5. Principal Obstacles

- **The Christofides barrier is structural, not cosmetic.** The analysis pays $\mathrm{MST}\le\mathrm{SUBT}$ and $\text{matching}\le\frac12\mathrm{SUBT}$; both are individually tight, and tight simultaneously on instances where the tree is a Hamiltonian path. Any improvement must show the two bounds cannot be tight at once — a correlation argument, not a bound-tightening one.
- **Randomized rounding gains are microscopic.** The Karlin–Klein–Oveis Gharan approach samples a spanning tree from the *maximum entropy distribution* with marginals $\frac{n-1}{n}x$ and shows that "half-integral-like" cuts are rarely odd. The gain $\varepsilon_0\sim 10^{-36}$ comes from a case analysis with many losses; the method has no visible route to a constant improvement of size $1/6$.
- **No known $4/3$-supporting combinatorial object.** For the $3/2$ bound the certificate is tree + $T$-join. No relaxation is known whose optimum is provably within $4/3$ of a tour and within $1$ of $\mathrm{SUBT}$. Candidate objects (2-matchings, ear decompositions, cycle covers) each lose more than $1/3$ in the worst case.
- **Parity is the enemy.** All hardness in the analysis concentrates in odd cuts $\delta(S)$ with $x(\delta(S))$ near 2 and an odd number of tree edges. Controlling *all* such cuts simultaneously requires negative-dependence properties of random spanning trees that are known only in weak (strongly Rayleigh) form.
- **Extreme points are not classified.** The vertices of $\mathrm{SEP}_n$ are combinatorially wild for $n\ge 12$; even the conjecture that half-integral vertices maximize the gap is open, so one cannot reduce to a tractable subfamily.

## 6. The Gap

Proven: $\tfrac43\le\gamma\le \tfrac32-10^{-36}$. The entire interval $\left(\tfrac43,\ \tfrac32-10^{-36}\right)$ — width about $0.1667$ — is unresolved, while every improvement since 1976 has moved the upper endpoint by $10^{-36}$.

Two concrete steps would close it:

1. **Half-integral reduction.** Prove that the supremum of $\mathrm{OPT}/\mathrm{SUBT}$ is attained (in the limit) on half-integral extreme points. Then combine with a $4/3$ bound for that class — currently $1.4$, so a further $0.0667$ would be needed there too.
2. **Correlated rounding.** Produce a distribution over spanning trees with marginals $\frac{n-1}{n}x$ such that the expected cost of the parity-correcting $T$-join is at most $\tfrac13\mathrm{SUBT}$ rather than $\tfrac12\mathrm{SUBT}$. Every known bound on this expectation degrades to $\frac12$ on Hamiltonian-path-like trees.

## 7. Current Research (as of June 2026)

- **Maximum-entropy sampling school (University of Washington; Karlin, Klein, Oveis Gharan and students).** Ongoing effort to replace the $10^{-36}$ case analysis with a cleaner argument; the stated goal is a "human-sized" constant such as $1.49$ or $1.4$. *(frontier — verify)*
- **Half-integral rounding (CMU/Warsaw/Bonn; Gupta, Mucha, Newman, Sarkar, Vygen groups).** Matroid intersection and "rainbow" $T$-join rounding for $x\in\{0,\frac12,1\}$; the $1.4$ barrier here mirrors the graphic-TSP $7/5$ barrier and is believed to be an artefact of the ear-decomposition accounting. *(frontier — verify)*
- **Structural polyhedral work.** Classification of extreme points of $\mathrm{SEP}_n$ and of the "fundamental" gap-maximizing families (Boyd's Ottawa group and successors), aiming at a proof that graphic metrics are extremal for the gap.
- **Path and $T$-tour variants (Bonn: Traub, Vygen; ETH: Zenklusen).** These variants have been resolved to their exact LP gaps, and their techniques (dynamic programming over "$\Delta$-narrow" cuts, recursive dedication) are actively being transplanted to the cycle case.
- **Computation.** Concorde-based experiments (Applegate–Bixby–Chvátal–Cook lineage) and later studies of Best-of-Many Christofides report observed gaps below $1.02$ on TSPLIB and random Euclidean instances — strong empirical support that $4/3$ is far from typical, and no instance beating $4/3$ has ever been found.

## 8. Future Work

- Prove or refute that half-integral extreme points maximize the gap; this is the single highest-leverage reduction available.
- Develop stronger negative-dependence tools for max-entropy spanning-tree distributions (beyond strongly Rayleigh) to bound the *joint* probability that many near-minimum cuts are odd.
- Attack the conjecture on graphic metrics first: proving $\gamma\le 4/3$ for unweighted graph metrics would replace $7/5$ and is widely regarded as the realistic next milestone.
- Extend the cubic/subcubic $4/3$ theorems to bounded-degree and then degree-unbounded graphic instances by ear-decomposition refinements (Sebő–Vygen programme).
- Search for better lower bounds: no family beating $4/3$ is known, and a certified computational search over extreme points of $\mathrm{SEP}_n$ for $n\le 20$ would either strengthen belief or refute the conjecture outright.

## 9. Key References

- **[Foundational]** G. Dantzig, R. Fulkerson, S. Johnson. *Solution of a Large-Scale Traveling-Salesman Problem.* Journal of the Operations Research Society of America 2(4), 393–410, 1954.
- **[Foundational]** M. Held, R. M. Karp. *The Traveling-Salesman Problem and Minimum Spanning Trees.* Operations Research 18(6), 1138–1162, 1970.
- **[Foundational]** N. Christofides. *Worst-case Analysis of a New Heuristic for the Travelling Salesman Problem.* Report 388, Graduate School of Industrial Administration, Carnegie Mellon University, 1976. (Reprinted in Operations Research Forum 3, 20, 2022.)
- **[Foundational]** A. I. Serdyukov. *O nekotorykh ekstremal'nykh obkhodakh v grafakh.* Upravlyaemye Sistemy 17, 76–79, 1978.
- **[Foundational]** L. A. Wolsey. *Heuristic Analysis, Linear Programming and Branch and Bound.* Mathematical Programming Study 13, 121–134, 1980.
- **[Foundational]** D. B. Shmoys, D. P. Williamson. *Analyzing the Held-Karp TSP Bound: A Monotonicity Property with Application.* Information Processing Letters 35(6), 281–285, 1990.
- **[Foundational]** M. X. Goemans. *Worst-case Comparison of Valid Inequalities for the TSP.* Mathematical Programming 69, 335–349, 1995.
- **[SOTA / Recent]** A. R. Karlin, N. Klein, S. Oveis Gharan. *A (Slightly) Improved Approximation Algorithm for Metric TSP.* Proc. 53rd ACM Symposium on Theory of Computing (STOC), 32–45, 2021.
- **[SOTA / Recent]** A. R. Karlin, N. Klein, S. Oveis Gharan. *A (Slightly) Improved Bound on the Integrality Gap of the Subtour LP for TSP.* Proc. 63rd IEEE Symposium on Foundations of Computer Science (FOCS), 2022.
- **[SOTA / Recent]** A. R. Karlin, N. Klein, S. Oveis Gharan. *An Improved Approximation Algorithm for TSP in the Half Integral Case.* Proc. 52nd ACM Symposium on Theory of Computing (STOC), 28–39, 2020.
- **[SOTA / Recent]** A. Sebő, J. Vygen. *Shorter Tours by Nicer Ears: 7/5-approximation for the graph-TSP, 3/2 for the path version, and 4/3 for two-edge-connected subgraphs.* Combinatorica 34(5), 597–629, 2014.
- **[SOTA / Recent]** T. Mömke, O. Svensson. *Removing and Adding Edges for the Traveling Salesman Problem.* Journal of the ACM 63(1), Article 2, 2016.
- **[SOTA / Recent]** S. Boyd, R. Sitters, S. van der Ster, L. Stougie. *The Traveling Salesman Problem on Cubic and Subcubic Graphs.* Mathematical Programming 144(1–2), 227–245, 2014.
- **[SOTA / Recent]** J. Correa, O. Larré, J. A. Soto. *TSP Tours in Cubic Graphs: Beyond 4/3.* SIAM Journal on Discrete Mathematics 29(2), 915–939, 2015.
- **[SOTA / Recent]** A. van Zuylen. *Improved Approximations for Cubic and Cubic Bipartite TSP.* Mathematical Programming 172, 399–413, 2018.
- **[SOTA / Recent]** F. Schalekamp, D. P. Williamson, A. van Zuylen. *2-Matchings, the Traveling Salesman Problem, and the Subtour LP: A Proof of the Boyd–Carr Conjecture.* Mathematics of Operations Research 39(2), 403–417, 2014.
- **[SOTA / Recent]** G. Benoit, S. Boyd. *Finding the Exact Integrality Gap for Small Traveling Salesman Problems.* Mathematics of Operations Research 33(4), 921–931, 2008.
- **[SOTA / Recent]** R. Zenklusen. *A 1.5-Approximation for Path TSP.* Proc. 30th ACM-SIAM Symposium on Discrete Algorithms (SODA), 1539–1549, 2019.
- **[SOTA / Recent]** M. Karpinski, M. Lampis, R. Schmied. *New Inapproximability Bounds for TSP.* Journal of Computer and System Sciences 81(8), 1665–1677, 2015.
- **[Survey]** D. P. Williamson, D. B. Shmoys. *The Design of Approximation Algorithms.* Cambridge University Press, 2011 (Chapters 2, 7, 11).
- **[Survey]** J. Vygen. *New Approximation Algorithms for the TSP.* OPTIMA 90, 1–12, 2012.
- **[Survey]** D. L. Applegate, R. E. Bixby, V. Chvátal, W. J. Cook. *The Traveling Salesman Problem: A Computational Study.* Princeton University Press, 2006.

## 10. Worked Example / Concrete Special Case

**Instance.** Let $P$ be the Petersen graph: $3$-regular, $10$ vertices, $15$ edges, $3$-edge-connected, and *hypohamiltonian* (no Hamiltonian cycle, but $P-v$ is Hamiltonian for every $v$). Take $c$ to be its shortest-path metric on $V(P)$, so $c(uv)=1$ for the 15 graph edges and $c(uv)=2$ otherwise (diameter 2).

**LP value.** Set $x_e=\tfrac23$ on each of the 15 graph edges, $x_e=0$ elsewhere.

- Degrees: $x(\delta(v))=3\cdot\tfrac23=2$ for all $v$. ✓
- Cuts: $P$ is 3-edge-connected, so $|\delta_P(S)|\ge 3$ and $x(\delta(S))\ge 3\cdot\tfrac23=2$. ✓
- Cost: $15\cdot\tfrac23\cdot 1=10$.

Conversely, for any feasible $x$, since $c_e\ge 1$ for all $e$,
$$\sum_e c_e x_e\ \ge\ \sum_e x_e\ =\ \tfrac12\sum_{v}x(\delta(v))\ =\ \tfrac12\cdot 2\cdot 10\ =\ 10 .$$
Hence $\mathrm{SUBT}(c)=10$ exactly, attained by the uniform $\tfrac23$ point — a genuine (non-integral) vertex-type solution of the kind conjectured to be extremal.

**Integer optimum.** Any tour has cost $\ge n=10$, with equality iff it uses only cost-1 edges, i.e. iff $P$ is Hamiltonian. It is not, so $\mathrm{OPT}\ge 11$ (costs are integers). Conversely $P$ has a Hamiltonian *path* $v_1\ldots v_{10}$ (9 unit edges), and $c(v_{10}v_1)\le 2$, giving a tour of cost $\le 9+2=11$. So $\mathrm{OPT}(c)=11$.

**Ratio.** $\dfrac{\mathrm{OPT}}{\mathrm{SUBT}}=\dfrac{11}{10}=1.1<\dfrac43$.

**What it shows.** The exact mechanism of the gap is *parity*: the LP buys a fractional 2-factor at rate $2/3$ per edge, while every integral tour is forced to pay one extra unit of "shortcut" because no Hamiltonian cycle exists. Christofides on this instance takes an MST of cost 9, plus a perfect matching on its (at least two) odd-degree vertices of cost $\le 2$, then shortcuts — recovering the optimal 11, well inside $\tfrac43\cdot 10=13.33$.

Scaling this mechanism is exactly the open problem. The known $4/3$ lower-bound families replace the single Petersen obstruction by $k$ obstructions chained so that the forced excess accumulates: the LP stays at $\approx n$ while every tour costs $\approx \tfrac43 n$, driving $\mathrm{OPT}/\mathrm{SUBT}\to 4/3$ (see Boyd–Carr-type half-integral instances and Williamson–Shmoys, Ch. 11). No construction is known that pushes the accumulated excess past $1/3$ per unit of LP cost, and no proof is known that $1/3$ is a ceiling.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*