---
id: 07-combinatorics/erdos-lovasz-tihany-conjecture
title: "Erdős-Lovász Tihany Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Lovász Tihany Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-lovasz-tihany-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Erdős and Lovász, Tihany 1966; published 1968).** Let $G$ be a finite simple graph with
$$\chi(G) > \omega(G),$$
and let $s,t \ge 2$ be integers with $s+t = \chi(G)+1$. Then $V(G)$ admits a partition $V(G) = S \,\dot\cup\, T$ such that
$$\chi(G[S]) \ge s \quad\text{and}\quad \chi(G[T]) \ge t .$$

Here $\chi$ is the chromatic number, $\omega$ the clique number, and $G[X]$ the subgraph induced on $X$.

The hypothesis $\chi(G) > \omega(G)$ is not decorative: for $G = K_n$ any partition has $|S|+|T| = n < s+t$, so one side has chromatic number below its target. The conjecture asserts that complete graphs are the *only* obstruction, i.e. that every graph whose chromatic number strictly exceeds its clique number is "colour-decomposable" in the strongest possible way, since $\chi(G) \le \chi(G[S]) + \chi(G[T])$ always forces $s + t \le \chi(G) + \chi(G)$ and makes $s+t = \chi(G)+1$ the first non-trivial regime.

A complete resolution means either a proof for all pairs $(s,t)$ and all graphs with $\chi > \omega$, or an explicit graph $G$ with $\chi(G) > \omega(G)$ and a pair $(s,t)$, $s+t=\chi(G)+1$, for which every bipartition fails.

## 2. Mathematical Foundations

**Colourings.** A proper $k$-colouring is $c: V(G) \to [k]$ with $c(u) \ne c(v)$ for $uv \in E(G)$; $\chi(G)$ is the least such $k$. $\omega(G)$ is the largest $r$ with $K_r \subseteq G$, $\alpha(G) = \omega(\overline{G})$ the independence number. Basic inequalities:
$$\omega(G) \le \chi(G) \le \Delta(G)+1, \qquad \chi(G) \ge \frac{|V(G)|}{\alpha(G)} .$$

**Subadditivity.** For any partition $V = S \dot\cup T$,
$$\max\{\chi(G[S]), \chi(G[T])\} \le \chi(G) \le \chi(G[S]) + \chi(G[T]),$$
so $\chi(G[S]) + \chi(G[T]) \ge \chi(G)$ holds for free; the conjecture demands the *individual* thresholds $s$ and $t$ with a total of $\chi(G)+1$, one unit above what is automatic.

**Criticality.** $G$ is $k$-vertex-critical if $\chi(G)=k$ and $\chi(G-v) = k-1$ for all $v$; then $\delta(G) \ge k-1$. One may always assume $G$ is $\chi(G)$-vertex-critical, since deleting vertices preserves $\chi > \omega$ only after care, but critical subgraphs are the standard reduction.

**Double-critical graphs.** $G$ with $\chi(G)=k$ is *double-critical* if $\chi(G-x-y) = k-2$ for every edge $xy \in E(G)$. The companion **Erdős–Lovász double-critical conjecture** states that $K_k$ is the only double-critical $k$-chromatic graph. Both problems were posed in the same Tihany problem set and share the same proof technology (Mozhan-type partitions, critical-graph arguments).

**Degeneracy analogue.** The *colouring number* is $\mathrm{col}(G) = 1 + \max_{H \subseteq G}\delta(H)$. Lovász (1966) proved the exact analogue of the conjecture for degrees: if $d_1 + \dots + d_r \ge \Delta(G) - r + 1$, then $V(G)$ splits into $V_1,\dots,V_r$ with $\Delta(G[V_i]) \le d_i$. Consequently the ELT statement with $\chi$ replaced by $\mathrm{col}$ is a theorem, with no clique hypothesis needed. The difficulty is entirely that $\chi$ is not a monotone local parameter.

**Line-graph form.** For a multigraph $H$ with chromatic index $\chi'(H)$ and $L(H)$ its line graph, $\chi(L(H)) = \chi'(H)$ and $\omega(L(H)) \ge \Delta(H)$. ELT restricted to line graphs is therefore an edge-colouring statement: if $\chi'(H) > \Delta(H)$ (and $H$ has no dominating "clique" obstruction), then $E(H)$ splits into $E_1 \dot\cup E_2$ with $\chi'(H_i) \ge s,t$.

## 3. History & State of the Art (SOTA)

- **1966/1968.** Posed by Erdős and Lovász at the Tihany colloquium on graph theory; recorded in the problem section of *Theory of Graphs* (Erdős and Katona, eds., Academic Press, 1968).
- **1969.** Brown and Jung settle the smallest pairs, $(s,t) \in \{(2,2),(2,3),(2,4)\}$, using odd-circuit arguments in critical graphs.
- **1987.** Mozhan and, independently, Stiebitz settle $(3,3)$ and $(3,4)$; Stiebitz adds $(3,5)$ and proves that $K_5$ is the only double-critical $5$-chromatic graph. The technique — now called *Mozhan partitions* — recursively refines a partition into parts of prescribed chromatic number by shifting vertices along colour-alternating structures.
- **2008.** Kostochka and Stiebitz prove the conjecture for line graphs of multigraphs, i.e. in full generality in the edge-colouring formulation.
- **2009.** Balogh, Kostochka, Prince and Stiebitz prove it for quasi-line graphs and for all graphs with $\alpha(G) = 2$.
- **2010.** Kawarabayashi, Pedersen and Toft push the double-critical companion to $k \le 7$ modulo minor-theoretic input, showing double-critical $k$-chromatic graphs with $k \in \{6,7\}$ have $K_k$ minors.
- **2013–2017.** Chudnovsky, Fradkin and Plumettaz cover claw-free graphs with $\alpha(G)\ge 3$, completing the claw-free case; Rolek and Song settle double-criticality for claw-free graphs; Stiebitz publishes a relaxed version of ELT.

No pair $(s,t)$ with $s \ge 4$ is known in general; the conjecture stands open for every $\chi(G) \ge 8$ with unrestricted structure.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $(s,t)=(2,2),(2,3),(2,4)$ | True for all graphs | Brown–Jung 1969 |
| $(s,t)=(3,3),(3,4)$ | True for all graphs | Mozhan 1987; Stiebitz 1987 |
| $(s,t)=(3,5)$ | True for all graphs | Stiebitz 1987 |
| all $(s,t)$, $G$ a line graph of a multigraph | True | Kostochka–Stiebitz 2008 |
| all $(s,t)$, $G$ quasi-line | True | Balogh–Kostochka–Prince–Stiebitz 2009 |
| all $(s,t)$, $\alpha(G)=2$ | True | Balogh–Kostochka–Prince–Stiebitz 2009 |
| all $(s,t)$, $G$ claw-free with $\alpha(G) \ge 3$ | True | Chudnovsky–Fradkin–Plumettaz 2013 |
| $\chi(G) \le 8$ with $s \le 3$ | Covered by the $(2,t),(3,t)$ rows | — |
| relaxed conclusion ($\mathrm{col}$ in place of $\chi$ on one part) | True | Stiebitz 2017 *(exact form — verify)* |
| double-critical companion, $k \le 5$ | $K_k$ is the unique example | Stiebitz 1987 |
| double-critical companion, $k \le 7$ | Unique modulo minor hypotheses | Kawarabayashi–Pedersen–Toft 2010 |

Together the claw-free and $\alpha \le 2$ results mean every known counterexample candidate must have an induced claw $K_{1,3}$ and independence number at least $3$; no such candidate has survived checking.

## 5. Principal Obstacles

- **$\chi$ is not locally certifiable.** Unlike degeneracy or maximum degree, there is no small witness that $\chi(G[S]) \ge s$; Lovász's degree-decomposition proof shifts vertices greedily while monitoring degrees, and no analogous monotone potential exists for chromatic number.
- **Mozhan partitions stall at $s \ge 4$.** The 1987 arguments track a partition $(V_1,V_2)$ and repair defects by moving a vertex and recolouring; the case analysis grows with $\min(s,t)$ because the number of possible "defect configurations" grows super-exponentially, and the induction loses control once both parts need chromatic number $\ge 4$ (no Brooks-type classification is available above $\chi = 3$).
- **Criticality gives too little.** A $\chi$-vertex-critical graph only guarantees $\delta \ge \chi-1$, which is far too weak: expanders with $\chi \gg \omega$ (Kneser graphs, shift graphs, Ramsey-type random graphs) have no clique structure to exploit and no known decomposition scheme.
- **Structural theorems do not extend.** All confirmed classes (line, quasi-line, claw-free, $\alpha=2$) are exactly the classes with a Chudnovsky–Seymour-style structure theorem plus a good understanding of fractional relaxations. General graphs have neither.
- **Probabilistic methods fail on both ends.** Random partitions typically give $\chi(G[S])+\chi(G[T])$ close to $\chi(G)$ only, missing the $+1$; and the conjecture is tight, so no slack absorbs an error term.

## 6. The Gap

Everything proven splits into two families: (i) small fixed $\min(s,t) \le 3$, by finite case analysis; (ii) restricted graph classes closed under structure theorems. The general statement needs a proof for $s,t \ge 4$ on graphs with an induced claw and $\alpha \ge 3$ — precisely where neither induction on $s$ nor structural decomposition is available. The single missing step is a mechanism that converts the *global* inequality $\chi(G) \ge s+t-1$ together with $\chi(G) > \omega(G)$ into a *constructive* bipartition, i.e. an extremal or potential-function argument certifying $\chi(G[S]) \ge s$ without exhibiting a critical subgraph. Even the first unknown pair, $(s,t)=(4,4)$ with $\chi(G)=7$, is open.

## 7. Current Research (as of June 2026)

- **Ilmenau / Odense school (Stiebitz, Schweser, Toft).** Hypergraph and variable-degeneracy generalisations of partition theorems; the 2024 monograph *Brooks' Theorem* consolidates the Mozhan-partition machinery and states ELT as a central open problem.
- **Illinois / Novosibirsk (Kostochka and coauthors).** Extensions of the line-graph and quasi-line arguments toward graphs with bounded "clique cover" structure; also list-colouring analogues where $\chi$ is replaced by the list chromatic number $\chi_\ell$. *(frontier — verify)*
- **Princeton / Columbia (Chudnovsky and coauthors).** Induced-subgraph structure for classes forbidding small claws, aiming at the first claw-containing family with $\alpha \ge 3$. *(frontier — verify)*
- **Central Florida (Song and coauthors).** Continued work on double-critical graphs and minor-based bounds, targeting $k = 8$.
- **Computational search.** Exhaustive checks over vertex-critical graphs of small order have found no counterexample; no published search reaches $\chi \ge 7$ at scale. *(frontier — verify)*

## 8. Future Work

1. **Settle $(4,4)$.** The minimal open pair; a proof would likely reveal the potential function needed in general.
2. **Fractional and list versions.** Prove the conjecture with $\chi_f$ (fractional chromatic number) on both sides; fractional relaxations are LP-dual and may admit a flow or matching argument.
3. **Approximate ELT.** Prove the partition exists for $s+t = \chi(G)+1 - f(\chi)$ with $f$ growing slowly (e.g. $f = O(\log \chi)$); currently even $f$ constant $\ge 1$ appears hard in general.
4. **Push structural classes.** Perfect-graph-adjacent classes (even-hole-free, $P_5$-free) where a structure theorem exists but claws are permitted.
5. **Local-global reduction.** Show a minimal counterexample must be vertex-critical *and* double-critical, joining the two Erdős–Lovász conjectures into one attack.

## 9. Key References

- **[Foundational]** P. Erdős. *Problems.* In: **Theory of Graphs** (Proc. Colloq. Tihany, 1966), P. Erdős and G. Katona (eds.), Academic Press / Akadémiai Kiadó, 1968.
- **[Foundational]** L. Lovász. *On decompositions of graphs.* Studia Scientiarum Mathematicarum Hungarica **1** (1966), 237–238.
- **[Foundational]** W. G. Brown and H. A. Jung. *On odd circuits in chromatic graphs.* Acta Mathematica Academiae Scientiarum Hungaricae **20** (1969), 129–134.
- **[Foundational]** M. Stiebitz. *$K_5$ is the only double-critical 5-chromatic graph.* Discrete Mathematics **64** (1987), 91–93.
- **[Foundational]** N. N. Mozhan. *Twice critical graphs with chromatic number five* (in Russian). Metody Diskretnogo Analiza **46** (1987), 50–59.
- **[SOTA]** A. V. Kostochka and M. Stiebitz. *Partitions and edge colourings of multigraphs.* Electronic Journal of Combinatorics **15** (2008), #N25.
- **[SOTA]** J. Balogh, A. V. Kostochka, N. Prince and M. Stiebitz. *The Erdős–Lovász Tihany conjecture for quasi-line graphs.* Discrete Mathematics **309** (2009), 3985–3991.
- **[SOTA]** K. Kawarabayashi, A. S. Pedersen and B. Toft. *Double-critical graphs and complete minors.* Electronic Journal of Combinatorics **17** (2010), #R87.
- **[SOTA]** M. Chudnovsky, A. O. Fradkin and M. Plumettaz. *On the Erdős–Lovász Tihany conjecture for claw-free graphs.* arXiv:1311.4235 (2013).
- **[SOTA]** M. Stiebitz. *A relaxed version of the Erdős–Lovász Tihany conjecture.* Journal of Graph Theory **85** (2017), 278–287.
- **[SOTA]** M. Rolek and Z-X. Song. *Double-critical graph conjecture for claw-free graphs.* Discrete Mathematics **340** (2017), 1633–1638.
- **[Survey]** T. R. Jensen and B. Toft. **Graph Coloring Problems.** Wiley-Interscience, 1995.
- **[Survey]** M. Stiebitz, T. Schweser and B. Toft. **Brooks' Theorem: Graph Colouring and Critical Graphs.** Springer Monographs in Mathematics, 2024.

## 10. Worked Example / Concrete Special Case

**Case $(s,t)=(2,2)$, $\chi(G)=3$.** The requirement $\chi(G[S]) \ge 2$ means $S$ contains an edge; likewise for $T$. So the statement reads: *every graph with $\chi \ge 3$ and $\chi > \omega$ has two disjoint edges.*

*Proof.* Suppose $G$ has no matching of size $2$. Then all edges pairwise intersect, so $E(G)$ is either a star $K_{1,r}$ (plus isolated vertices) or a triangle (plus isolated vertices). A star has $\chi = 2 = \omega$; a triangle has $\chi = 3 = \omega$. Both violate $\chi > \omega$. Hence a $2$-matching $\{a,b\},\{c,d\}$ exists; take $S=\{a,b\}$, $T = V(G)\setminus S \supseteq \{c,d\}$. $\square$

**Instance.** $G = C_5$ with $V=\{v_1,\dots,v_5\}$, edges $v_iv_{i+1}$ mod $5$. Then $\omega(C_5)=2$, and $\chi(C_5)=3$ (odd cycle), so $\chi > \omega$ and $s+t = 4 = \chi+1$ with $s=t=2$. Take $S=\{v_1,v_2\}$, $T=\{v_3,v_4,v_5\}$. Then $G[S]=K_2$ with $\chi=2 \ge s$, and $G[T]=P_3$ ($v_3v_4v_5$) with $\chi=2 \ge t$. Both targets met.

**Why $\chi > \omega$ is needed.** Take $G=K_6$, so $\chi=\omega=6$ and $s+t=7$; pick $(s,t)=(3,4)$. Any partition has $|S|+|T|=6$, and $\chi(K_6[S])=|S|$, so we would need $|S|\ge 3$ and $|T|\ge 4$, i.e. $6 \ge 7$ — impossible. The clique hypothesis excludes exactly this.

**A step into the unknown.** Replace $C_5$ by the Kneser graph $K(7,2)$ (vertices = $2$-subsets of $[7]$, edges = disjoint pairs): $\omega = 3$, $\chi = 7-2\cdot2+2 = 5$. For $(s,t)=(2,4)$ the conjecture is known (Brown–Jung); the pair $(s,t)=(4,4)$ would first require a graph with $\chi = 7 > \omega$, e.g. $K(11,2)$ with $\chi = 9$ restricted appropriately — and there no proof technique currently applies.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*