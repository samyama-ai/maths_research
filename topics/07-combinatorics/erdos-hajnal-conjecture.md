---
id: 07-combinatorics/erdos-hajnal-conjecture
title: "Erdős-Hajnal Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Hajnal Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-hajnal-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Graphs are finite, simple and undirected. A graph $G$ is **$H$-free** if it has no *induced* subgraph isomorphic to $H$. A **homogeneous set** in $G$ is a vertex set inducing either a clique or an independent (stable) set; write
$$\hom(G) = \max\{\omega(G),\ \alpha(G)\}.$$

**Conjecture (Erdős–Hajnal, 1977/1989).** For every graph $H$ there is a constant $c(H) > 0$ such that every $H$-free graph $G$ on $n$ vertices satisfies
$$\hom(G) \ \ge\ n^{c(H)}.$$

A graph $H$ with this property is said to have the **EH property**. A complete proof must supply, for each $H$, a constant and an argument valid for all $n$; a disproof must exhibit a single $H$ and, for every $c>0$, an infinite family of $H$-free graphs with $\hom(G) = o(n^{c})$.

The point of the conjecture is the contrast with the unrestricted case: by Ramsey's theorem, a general graph on $n$ vertices only guarantees $\hom(G) \ge \tfrac12\log_2 n$, and the random graph $G(n,1/2)$ shows this is tight up to a factor of $2$. Excluding *one* fixed induced subgraph is conjectured to force a jump from logarithmic to polynomial.

## 2. Mathematical Foundations

**Basic parameters.** $\omega(G)$ is the largest clique, $\alpha(G) = \omega(\overline{G})$ the largest stable set, $\chi(G)$ the chromatic number. Since colour classes are stable sets, $n \le \chi(G)\,\alpha(G)$.

**Ramsey baseline.** $R(s,t) \le \binom{s+t-2}{s-1}$ gives $\hom(G)\ge \tfrac12 \log_2 n$; the probabilistic bound $R(t,t) > 2^{t/2}$ (Erdős 1947) shows the logarithmic order is correct in general.

**Erdős–Hajnal theorem (unconditional bound).** For every $H$ there is $c>0$ with every $H$-free $G$ satisfying
$$\hom(G)\ \ge\ e^{\,c\sqrt{\log n}},$$
which is superpolylogarithmic but subpolynomial. This bound stood from 1989 until 2023.

**Substitution.** Given $H_1$ and $H_2$ with $v\in V(H_1)$, the graph $H_1[v \to H_2]$ replaces $v$ by a copy of $H_2$, joining every vertex of $H_2$ to every neighbour of $v$. A class closed under substitution and complementation is generated from $K_1$; the graphs so generated are exactly the **cographs** ($=P_4$-free graphs).

**Substitution lemma (Alon–Pach–Solymosi 2001).** If $H_1$ and $H_2$ have the EH property, so does $H_1[v\to H_2]$. Explicitly, if $\hom \ge n^{c_i}$ for $H_i$-free graphs, one obtains an exponent for the substituted graph depending only on $c_1,c_2$. Complementation is free: $H$ has the EH property iff $\overline{H}$ does, since $\hom(G)=\hom(\overline G)$.

**Equivalent "bipartite-pair" form.** $H$ has the EH property iff there is $c>0$ such that every $H$-free $G$ contains disjoint $A,B$ with $|A|,|B|\ge n^{c}$ and either all or none of the edges between $A$ and $B$ present (a *complete* or *anticomplete* pair). This "strong EH-type" pairing formulation is the working statement in most modern proofs.

**Rödl's theorem (1986).** For every $H$ and $\varepsilon>0$ there is $\delta>0$ such that every $H$-free $G$ contains $S\subseteq V(G)$, $|S|\ge \delta n$, with $G[S]$ of edge density $<\varepsilon$ or $>1-\varepsilon$. Rödl's proof uses the regularity lemma and gives tower-type $\delta$; Fox–Sudakov (2009) gave a stronger "density" version. The **polynomial Rödl conjecture** — that one may take $\delta = \varepsilon^{O(1)}$ — implies EH.

**Tournament form (Alon–Pach–Solymosi).** EH is equivalent to: for every tournament $S$ there is $c>0$ such that every $S$-free tournament on $n$ vertices contains a transitive subtournament on $n^{c}$ vertices.

## 3. History & State of the Art (SOTA)

- **1977.** Erdős and Hajnal state the problem in *On spanned subgraphs of graphs* (Beiträge zur Graphentheorie und deren Anwendungen).
- **1989.** Erdős and Hajnal, *Ramsey-type theorems* (Discrete Applied Mathematics 25, 37–52), give the formal conjecture and prove $\hom(G)\ge e^{c\sqrt{\log n}}$ for $H$-free graphs.
- **2001.** Alon, Pach, Solymosi (*Ramsey-type theorems with forbidden subgraphs*, Combinatorica 21) prove the substitution lemma and the tournament equivalence — the single most productive tool in the area.
- **2008.** Chudnovsky and Safra settle $H=$ bull (JCTB 98), using the structural decomposition of bull-free graphs.
- **2014.** Chudnovsky's survey (*The Erdős–Hajnal conjecture — a survey*, Journal of Graph Theory 75) consolidates the state of knowledge.
- **2019.** Fox, Pach, Suk prove strong bounds under bounded VC dimension (Discrete & Computational Geometry 61).
- **2023.** Chudnovsky, Scott, Seymour, Spirkl settle $H=C_5$ (*Erdős–Hajnal for graphs with no 5-hole*, Proc. LMS), the first "hard" 5-vertex case not reachable by substitution.
- **2023–24.** Bucić, Nguyen, Scott, Seymour improve the *general* bound for the first time since 1989 to
  $$\hom(G)\ \ge\ e^{\,\Omega\!\left(\sqrt{\log n\,\log\log n}\right)} .$$

## 4. Partial Results / Verified Cases

**Settled $H$.**
- $|V(H)|\le 3$: trivial from Ramsey ($\hom \ge n^{1/2}$ for triangle-free, see §10).
- $|V(H)|=4$: all graphs. $H=P_4$ gives cographs, which are perfect, so $\hom(G)\ge\sqrt n$; all other 4-vertex graphs follow by substitution and complementation.
- **All cographs**: closed under substitution/complement, so the Alon–Pach–Solymosi lemma applies with $c$ depending on the cograph's decomposition tree.
- $H=$ **bull** (triangle plus two pendant vertices), Chudnovsky–Safra 2008, exponent $c=1/4$.
- $H=C_5$, Chudnovsky–Scott–Seymour–Spirkl 2023, $\hom(G)\ge n^{c}$ for an explicit $c>0$; the optimal exponent for $C_5$ remains unknown.
- **Pairs**: excluding both $P_5$ and $\overline{P_5}$ (Chudnovsky–Seymour, *Excluding paths and antipaths*, Combinatorica 2015); more generally many $\{H,\overline H\}$ pairs and $\{H, H'\}$ pairs are settled where the single-graph case is not.

**Restricted host classes.**
- **Bounded VC dimension**: every graph of VC dimension $\le d$ has $\hom(G) \ge e^{(\log n)^{1-o(1)}}$ (Fox–Pach–Suk 2019).
- **Semi-algebraic graphs** of bounded description complexity: $\hom(G)\ge n^{\delta}$ (Alon, Pach, Pinchasi, Radoičić, Sharir, JCTA 2005); this covers intersection graphs of semi-algebraic sets in $\mathbb{R}^d$.
- **Tournaments**: infinite families of tournaments with the EH property are known (Berger, Choromanski, Chudnovsky, JCTB 2015), including all tournaments on $\le 5$ vertices and "galaxies".

**Quantitative benchmarks.** For $H=K_k$ the exact exponent is $c(K_k)=1/(k-1)$ (Ramsey lower bound plus Kim/Bohman-type constructions), so $c(H)\to 0$ as $|V(H)|$ grows: no universal constant is possible.

**Smallest open case.** $P_5$ (and, equivalently, $\overline{P_5}$) is the standard smallest open graph.

## 5. Principal Obstacles

- **No induced-subgraph regularity.** Szemerédi regularity controls edge densities, not induced structure; it loses exactly the information EH needs. Worse, its tower-type dependence turns any $\varepsilon$-argument into a $\delta$ that is inverse-tower in $\varepsilon$, which cannot yield a polynomial bound. This is why Rödl's theorem, though qualitatively strong, is quantitatively useless for EH.
- **The $\sqrt{\log n}$ barrier.** The 1989 proof iterates a "one of two densities improves" dichotomy $\sqrt{\log n}$ times; each step costs a constant factor, so the recursion self-limits at $e^{c\sqrt{\log n}}$. Only in 2023 was a $\sqrt{\log\log n}$ factor extracted, by tracking many densities at once rather than one — a refinement of the same recursion, not a new mechanism.
- **No structure theorem for general $H$-free graphs.** The successes ($P_4$, bull, $C_5$) all rest on a bespoke structural decomposition of the class. For $H=P_5$ no such decomposition is known, and the class is provably rich (it contains all triangle-free graphs of large girth, all $C_5$-blowups, etc.).
- **Random constructions block soft arguments.** $H$-free graphs built from $G(n,p)$ with $p$ tuned to $H$'s density have $\hom(G)$ only $n^{o(1)}$ larger than the target, so any proof must be nearly tight; there is no slack for lossy counting.
- **Sparse/pseudorandom obstruction.** Pseudorandom $H$-free graphs are locally indistinguishable from random ones, so local (bounded-radius) arguments cannot detect the polynomial homogeneous set, which must be found globally.

## 6. The Gap

Proven: $\hom(G)\ \ge\ e^{\Omega(\sqrt{\log n \log\log n})}$ for all $H$; and $\hom(G)\ge n^{c(H)}$ for cographs, the bull, $C_5$, and their substitution closure. Conjectured: $\hom(G)\ge n^{c(H)}$ for all $H$.

The gap is a genuine growth-rate gap: $e^{\sqrt{\log n\log\log n}} = n^{o(1)}$, so the general theorem gives *no* polynomial bound for *any* $H$ outside the settled list. Concretely, the missing step is to convert the iterative density dichotomy — which loses a constant per step and is run $\sqrt{\log n}$ times — into one that loses a constant factor over $O(1)$ steps, equivalently to prove the polynomial Rödl conjecture: an $H$-free graph contains an $\varepsilon$-sparse or $\varepsilon$-dense set of size $\varepsilon^{O(1)}n$. Even a bound of the form $e^{(\log n)^{1/2+\delta}}$ for all $H$, with $\delta>0$ absolute, is open.

## 7. Current Research (as of June 2026)

- **The Scott–Seymour–Nguyen–Chudnovsky–Spirkl programme** (Princeton / Oxford / Waterloo) drives most progress: the *Induced subgraph density* preprint series (2023–) attacks EH-type statements by proving polynomial pair-density results for structured $H$, and produced both the $\log\log$ improvement and the $C_5$ theorem.
- **Bounded VC dimension / model-theoretic tameness**: strengthening Fox–Pach–Suk to a polynomial bound under bounded VC dimension, and stability-theoretic versions (NIP/stable graph regularity, Malliaris–Shelah) where regularity has polynomial-size parts. Polynomial bounds in the stable case are known; the NIP case remains the frontier *(frontier — verify)*.
- **Tournament EH**: classifying tournaments with the EH property; recent work extends the "pseudo-celebrity"/forest-based families.
- **$P_5$ specifically**: several groups have announced partial density results for $P_5$-free graphs; no complete resolution is confirmed *(frontier — verify)*.
- **Optimal exponents**: determining $c(H)$ exactly, known only for $H=K_k$ and a few cographs.

## 8. Future Work

- Prove the **polynomial Rödl conjecture**, which implies EH in full.
- Settle $H=P_5$; leading practitioners regard this as the decisive test case, since it lacks any substitution structure yet is small enough for structural analysis.
- Establish the "strong EH" pair version for a new infinite family of $H$ (Alon–Pach–Solymosi note the pair version is strictly stronger and false for some $H$ in its literal form, so the right formulation must be found).
- Determine the correct order of the general bound: is $e^{\Theta(\sqrt{\log n\log\log n})}$ the truth for the current method, or can $e^{(\log n)^{c}}$, $c>1/2$, be reached?
- Compute or bound $c(H)$ for settled $H$; even $c(\text{bull})$ and $c(C_5)$ are not known to be optimal.

## 9. Key References

- **[Foundational]** P. Erdős, A. Hajnal. *Ramsey-type theorems.* Discrete Applied Mathematics 25 (1989), 37–52.
- **[Foundational]** P. Erdős, A. Hajnal. *On spanned subgraphs of graphs.* Beiträge zur Graphentheorie und deren Anwendungen, Oberhof, 1977, 80–96.
- **[Foundational]** N. Alon, J. Pach, J. Solymosi. *Ramsey-type theorems with forbidden subgraphs.* Combinatorica 21 (2001), 155–170.
- **[Foundational]** V. Rödl. *On universality of graphs with uniformly distributed edges.* Discrete Mathematics 59 (1986), 125–134.
- **[Survey]** M. Chudnovsky. *The Erdős–Hajnal conjecture — a survey.* Journal of Graph Theory 75 (2014), 178–190.
- **[Partial]** M. Chudnovsky, S. Safra. *The Erdős–Hajnal conjecture for bull-free graphs.* Journal of Combinatorial Theory Series B 98 (2008), 1301–1310.
- **[Partial]** M. Chudnovsky, P. Seymour. *Excluding paths and antipaths.* Combinatorica 35 (2015), 389–412.
- **[Partial]** N. Alon, J. Pach, R. Pinchasi, R. Radoičić, M. Sharir. *Crossing patterns of semi-algebraic sets.* Journal of Combinatorial Theory Series A 111 (2005), 310–326.
- **[Partial]** J. Fox, J. Pach, A. Suk. *Erdős–Hajnal conjecture for graphs with bounded VC-dimension.* Discrete & Computational Geometry 61 (2019), 809–829.
- **[SOTA]** M. Chudnovsky, A. Scott, P. Seymour, S. Spirkl. *Erdős–Hajnal for graphs with no 5-hole.* Proceedings of the London Mathematical Society 126 (2023), 997–1014.
- **[SOTA]** M. Bucić, T. Nguyen, A. Scott, P. Seymour. *Induced subgraph density. I. A loglog step towards Erdős–Hajnal.* arXiv:2301.10147 (2023).
- **[Related]** J. Fox, B. Sudakov. *Density theorems for bipartite graphs and related Ramsey-type results.* Combinatorica 29 (2009), 153–196.
- **[Related]** E. Berger, K. Choromanski, M. Chudnovsky. *Forcing large transitive subtournaments.* Journal of Combinatorial Theory Series B 112 (2015), 1–17.

## 10. Worked Example / Concrete Special Case

**Case A: $H=K_3$, with the exponent computed exactly.**

Let $G$ be triangle-free on $n$ vertices. If some vertex $v$ has degree $d \ge \sqrt n$, its neighbourhood $N(v)$ is stable (an edge inside $N(v)$ would close a triangle), so $\alpha(G)\ge\sqrt n$. Otherwise every degree is $<\sqrt n$; greedily picking a vertex and deleting its closed neighbourhood builds a stable set of size at least
$$\frac{n}{\Delta+1} \ >\ \frac{n}{\sqrt n + 1}\ \ge\ \tfrac12\sqrt n .$$
Either way $\hom(G)\ge \tfrac12 n^{1/2}$, so $c(K_3)\ge 1/2 - o(1)$. Conversely, Kim's construction ($R(3,t)=\Theta(t^2/\log t)$) yields triangle-free graphs with $\alpha(G)=O(\sqrt{n\log n})$ and $\omega=2$, so the exponent $1/2$ cannot be improved: $c(K_3)=1/2$ exactly.

The same argument for $K_k$-free graphs gives $\alpha(G) \ge n^{1/(k-1)}$ up to logarithmic factors, matched by known Ramsey constructions: $c(K_k)=1/(k-1)$. This shows $c(H)$ must depend on $H$ and tends to $0$.

**Case B: $H=P_4$ (the 4-vertex path).**

A $P_4$-free graph is a cograph, and cographs are perfect, so $\chi(G)=\omega(G)$ for $G$ and every induced subgraph. From $n\le \chi(G)\,\alpha(G) = \omega(G)\,\alpha(G)$,
$$\hom(G)=\max\{\omega,\alpha\} \ \ge\ \sqrt{\omega(G)\alpha(G)}\ \ge\ \sqrt n,$$
so $c(P_4)\ge 1/2$. The bound is tight: take $G$ to be a disjoint union of $\sqrt n$ cliques of size $\sqrt n$ — a cograph with $\omega=\alpha=\sqrt n$.

**Case C: substitution in action.** Let $H = K_1 \cup K_2$ (a vertex plus a disjoint edge, i.e. $K_2$ substituted into one vertex of $\overline{K_2}$). Both $K_2$ and $\overline{K_2}$ trivially have the EH property with exponent $1$. The Alon–Pach–Solymosi lemma then yields a positive exponent for $H$-free graphs without any structural analysis of the class. Iterating this over the cograph decomposition tree settles every cograph — and shows exactly why $P_5$, which is *not* a cograph and admits no nontrivial substitution decomposition, resists the method.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*