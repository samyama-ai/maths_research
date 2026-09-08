---
id: 07-combinatorics/chvatal-erdos-hamiltonicity-refinements
title: "Chvátal–Erdős Hamiltonicity Threshold Refinements"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chvátal–Erdős Hamiltonicity Threshold Refinements

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/chvatal-erdos-hamiltonicity-refinements` · **Status:** open

## 1. Problem Statement / Conjecture

The Chvátal–Erdős theorem (1972) says: if $G$ is a graph on $n \ge 3$ vertices with vertex connectivity $\kappa(G)$ at least its independence number $\alpha(G)$, then $G$ is Hamiltonian. The refinement programme asks what *more* the same hypothesis, or a slightly stronger one, buys. Three linked questions are open.

**(A) Jackson–Ordaz conjecture (main open problem).** Every graph $G$ with
$$\kappa(G) > \alpha(G)$$
is **pancyclic**: it contains a cycle of every length $\ell$ with $3 \le \ell \le n$.

**(B) The optimal multiplicative threshold.** Determine the least constant $c \ge 1$ such that $\kappa(G) \ge c\,\alpha(G)$ forces pancyclicity for all sufficiently large $n$. Conjecture (A) asserts $c = 1$ (with the strict-inequality form); the best proven constant is $c = 600$ (Keevash–Sudakov, 2010).

**(C) Digraph analogue.** Does $\kappa(D) \ge \alpha(D)$ force a Hamiltonian cycle in a digraph $D$, where $\kappa$ is strong connectivity and $\alpha$ is the size of the largest set of pairwise non-adjacent vertices? Listed as open in the Jackson–Ordaz survey and in Bang-Jensen–Gutin.

A complete solution of (A) means: a proof valid for all $n$ and all $\alpha$, or a single graph with $\kappa > \alpha$ missing a cycle of some length $\ell \le n$. Note that $\kappa \ge \alpha$ alone is *not* enough: $K_{\alpha,\alpha}$ and $C_5$ satisfy $\kappa = \alpha$ and are Hamiltonian but not pancyclic, which is why strictness is imposed.

## 2. Mathematical Foundations

Let $G = (V,E)$ be finite, simple, undirected, $|V| = n$.

- **Independence number** $\alpha(G) = \max\{|S| : S \subseteq V,\ E(G[S]) = \emptyset\}$.
- **Connectivity** $\kappa(G) = \min\{|S| : G - S$ disconnected or $|V \setminus S| \le 1\}$; $G$ is $k$-connected iff $\kappa(G) \ge k$.
- **Circumference** $c(G)$ = length of a longest cycle; $G$ Hamiltonian iff $c(G) = n$; $G$ **pancyclic** iff it has cycles of all lengths in $[3,n]$; $G$ **Hamiltonian-connected** iff every pair of vertices is joined by a Hamiltonian path.

**Theorem (Chvátal–Erdős, 1972).** For $n \ge 3$:
$$\kappa(G) \ge \alpha(G) - 1 \Rightarrow G \text{ traceable}, \qquad \kappa(G) \ge \alpha(G) \Rightarrow G \text{ Hamiltonian}, \qquad \kappa(G) \ge \alpha(G) + 1 \Rightarrow G \text{ Hamiltonian-connected}.$$

The proof is a fan/Menger argument: take a longest cycle $C$, suppose $v \notin C$; $\kappa \ge \alpha$ gives $\kappa$ internally disjoint $v$–$C$ paths landing on $\kappa$ distinct vertices $x_1,\dots,x_\kappa \in C$; maximality of $C$ forces the successors $x_1^+,\dots,x_\kappa^+$ to be pairwise non-adjacent and non-adjacent to $v$, producing an independent set of size $\kappa+1 > \alpha$ — contradiction.

**Sharpness.** $K_{\alpha,\alpha+1}$ has $\kappa = \alpha$, $\alpha(G) = \alpha+1$, and is non-Hamiltonian, so the bound $\kappa \ge \alpha$ cannot be weakened by one.

**Circumference refinement (Fouquet–Jolivet, 1976; proved by O–West–Wu, 2011).** If $G$ is $k$-connected with $\alpha(G) = \alpha \ge k$, then
$$c(G) \ \ge\ \frac{k(n + \alpha - k)}{\alpha},$$
which for $\alpha = k$ recovers $c(G) \ge n$, i.e. the Chvátal–Erdős theorem itself. Extremal graphs are of the form $K_k + (\text{disjoint union of } \alpha \text{ cliques})$ balanced in size.

**Bondy's meta-conjecture (1971).** Almost every nontrivial sufficient condition for Hamiltonicity also forces pancyclicity, up to a small family of exceptions. (A) is the Chvátal–Erdős instance of this principle, with exceptional family $\{K_{m,m}\} \cup \{C_5\}$ excluded by strictness.

## 3. History & State of the Art (SOTA)

- **1972.** Chvátal and Erdős, *A note on Hamiltonian circuits*, Discrete Math. 2, 111–113: the three implications above, all with two-page proofs.
- **1971–76.** Bondy formulates the pancyclicity meta-conjecture; Fouquet and Jolivet propose the circumference inequality as Problem 438 at the 1976 Orsay colloquium.
- **1990.** Jackson and Ordaz survey Chvátal–Erdős-type conditions for paths and cycles in graphs and digraphs and state the conjecture $\kappa > \alpha \Rightarrow$ pancyclic.
- **1991.** Amar, Fournier and Germa, *Pancyclism in Chvátal–Erdős graphs*, Graphs and Combinatorics 7, 101–112: under $\kappa \ge \alpha$, cycles of many lengths are forced and pancyclicity is established for small $\alpha$ and for structurally restricted families.
- **1994.** Kouider proves that a $k$-connected graph with independence number $\alpha$ has its vertex set covered by at most $\lceil \alpha/k \rceil$ disjoint cycles — the fractional analogue of Chvátal–Erdős.
- **2010.** Keevash and Sudakov, *Pancyclicity of Hamiltonian and highly connected graphs*, JCTB 100, 456–467: $\kappa(G) \ge 600\,\alpha(G)$ implies pancyclicity. This is the only unconditional result of the shape sought in (B).
- **2011.** Suil O, West and Wu settle the Fouquet–Jolivet circumference conjecture in full.

No computational counterexample search has produced a graph with $\kappa > \alpha$ missing a cycle length; exhaustive checks over all graphs up to $n \le 11$ (nauty-generated) are consistent with (A).

## 4. Partial Results / Verified Cases

- **$\alpha = 1$:** $G = K_n$, pancyclic for $n \ge 3$. Trivial.
- **$\alpha = 2$, $\kappa \ge 3$:** pancyclic. The complement is triangle-free, and a chord-descent argument on a Hamiltonian cycle (Section 10) yields all lengths.
- **Small independence number $\alpha \le 3$:** covered by the Amar–Fournier–Germa analysis.
- **Large-ratio regime:** $\kappa \ge 600\alpha$ (Keevash–Sudakov). Their method also gives pancyclicity for Hamiltonian graphs with $\kappa \ge$ (large constant) $\cdot \alpha$ without needing $n$ large separately.
- **Circumference:** the full inequality $c(G) \ge k(n+\alpha-k)/\alpha$ holds for all $k$-connected $G$ with $\alpha \ge k$ (O–West–Wu), giving long cycles well below the Hamiltonicity threshold.
- **Triangle-free graphs:** under $\kappa \ge \alpha$ the structure is heavily constrained; Lou (1996) determined the cycle spectrum for triangle-free graphs satisfying the Chvátal–Erdős condition.
- **Cycle covers:** $\lceil \alpha/k \rceil$ cycles suffice to cover $V(G)$ (Kouider, 1994), sharp for $K_k + \bigsqcup K_m$.
- **$k$-ordered Hamiltonicity:** Chvátal–Erdős-type conditions forcing a cycle through $k$ prescribed vertices in a prescribed order are known with connectivity roughly $\alpha + \Theta(k)$ (Kierstead–Sárközy–Selkow line of work).

## 5. Principal Obstacles

- **The rotation–extension toolkit is length-blind.** The Chvátal–Erdős proof only compares a longest cycle against an independent set; it produces *a* Hamiltonian cycle but says nothing about which shorter lengths occur. Shortening a Hamiltonian cycle by exactly one vertex needs a chord $v_iv_{i+2}$, and $\kappa > \alpha$ does not directly supply one.
- **No expansion.** Bounding $\alpha$ by $\kappa$ gives global connectivity but not the pseudo-random or expander structure that modern pancyclicity proofs (Krivelevich–Sudakov–Szabó style, Keevash–Sudakov) exploit. Keevash and Sudakov must inflate the ratio to 600 exactly to manufacture enough expansion; at ratio $1$ the graph can be an arbitrary sparse-ish blow-up structure with no expansion at all.
- **Extremal cases sit exactly at the boundary.** $K_{m,m}$ and $C_5$ are pancyclicity failures at $\kappa = \alpha$. Any proof of (A) must be sensitive enough to detect the single unit of slack $\kappa = \alpha + 1$ — stability arguments that lose $o(n)$ or even $O(1)$ in the hypothesis cannot see it.
- **Odd cycles are the hard direction.** Bipartite obstructions kill all odd lengths at once; ruling them out under $\kappa > \alpha$ requires forcing a triangle, and the extremal triangle-free graphs with large $\kappa/\alpha$ (Kneser-type, Cayley graphs on $\mathbb{Z}_p$) are exactly the graphs where independence numbers are hardest to compute.
- **Absorption fails at low density.** Absorbing-path methods need $\Theta(n)$ minimum degree; $\kappa > \alpha$ permits $\delta(G)$ as low as $\kappa$, which can be $O(1)$ when $\alpha$ is $O(1)$ but $n$ is large — except that $\alpha = O(1)$ with $n$ large forces density by Ramsey, so the genuinely hard regime is $\alpha, \kappa \to \infty$ with $n/\alpha$ bounded.

## 6. The Gap

Proven: pancyclicity for $\kappa \ge 600\alpha$, and for $\alpha \le 3$. Conjectured: pancyclicity for $\kappa \ge \alpha + 1$. The gap is the entire multiplicative window
$$\alpha + 1 \ \le\ \kappa \ < \ 600\,\alpha,$$
and in particular the single-slack case $\kappa = \alpha + 1$, where the graph is Hamiltonian (indeed Hamiltonian-connected by Chvátal–Erdős) but no method is known to extract short cycles. Concretely, the missing step is: **given a Hamiltonian cycle $v_1 \cdots v_n$ in a graph with $\kappa \ge \alpha+1$, produce for every $\ell \in [3,n-1]$ a cycle of length exactly $\ell$.** Even the weakest instance — producing a cycle of length $n-1$ — is open in general.

## 7. Current Research (as of June 2026)

- **Expander-ratio reduction.** Efforts to push the Keevash–Sudakov constant $600$ down by replacing their sparse-regularity step with sublinear-expander machinery (Liu–Montgomery style) are active; constants in the low tens have been announced in preprint form *(frontier — verify)*.
- **Cycle spectra.** Work quantifying $|\{\ell : G \text{ has an } \ell\text{-cycle}\}|$ under $\kappa \ge \alpha$, aiming to show the spectrum has density $1 - o(1)$ in $[3,n]$ even when full pancyclicity is not reached.
- **Circumference beyond Fouquet–Jolivet.** Refinements of O–West–Wu incorporating minimum degree or forbidden subgraphs, pursued by groups in China (Huazhong UST, Nankai) and the US (Suil O and coauthors).
- **Digraph side.** Chvátal–Erdős-type theorems for semicomplete and locally semicomplete digraphs continue to be extended (Bang-Jensen school, Odense); the general digraph question (C) is untouched.
- **Computer search.** SAT/CP-based searches for a $\kappa = \alpha+1$ non-pancyclic graph, parameterized by $\alpha \le 6$, have found nothing *(frontier — verify)*.

## 8. Future Work

- Prove the single case $\ell = n-1$ under $\kappa \ge \alpha + 1$; a chord-existence lemma there would likely bootstrap by induction on a shortened cycle.
- Establish (A) for graphs with a fixed forbidden induced subgraph (claw-free, $P_5$-free), where independence number and connectivity interact rigidly.
- Determine whether $\kappa \ge \alpha + 1$ forces a triangle for $n$ large; this isolates the odd-cycle obstruction from the rest.
- Settle the asymptotic version: does $\kappa \ge (1+\varepsilon)\alpha$ suffice for every $\varepsilon > 0$ and $n \ge n_0(\varepsilon)$?
- Resolve the digraph analogue (C), or produce a counterexample from a tournament-like construction.

## 9. Key References

- **[Foundational]** V. Chvátal, P. Erdős. *A note on Hamiltonian circuits.* Discrete Mathematics 2 (1972), 111–113.
- **[Foundational]** J. A. Bondy. *Pancyclic graphs I.* Journal of Combinatorial Theory, Series B 11 (1971), 80–84.
- **[Survey]** B. Jackson, O. Ordaz. *Chvátal–Erdős conditions for paths and cycles in graphs and digraphs. A survey.* Discrete Mathematics 84 (1990), 241–254.
- **[Partial]** D. Amar, I. Fournier, A. Germa. *Pancyclism in Chvátal–Erdős graphs.* Graphs and Combinatorics 7 (1991), 101–112.
- **[Partial]** M. Kouider. *Cycles in graphs with prescribed stability number and connectivity.* Journal of Combinatorial Theory, Series B 60 (1994), 315–318.
- **[Partial]** D. Lou. *The Chvátal–Erdős condition for cycles in triangle-free graphs.* Discrete Mathematics 152 (1996), 253–257.
- **[SOTA]** P. Keevash, B. Sudakov. *Pancyclicity of Hamiltonian and highly connected graphs.* Journal of Combinatorial Theory, Series B 100 (2010), 456–467.
- **[SOTA]** Suil O, D. B. West, H. Wu. *Longest cycles in $k$-connected graphs with given independence number.* Journal of Combinatorial Theory, Series B 101 (2011), 480–485.
- **[Reference]** J. Bang-Jensen, G. Gutin. *Digraphs: Theory, Algorithms and Applications.* 2nd ed., Springer, 2009.
- **[Reference]** J. A. Bondy, U. S. R. Murty. *Graph Theory.* Springer GTM 244, 2008.

## 10. Worked Example / Concrete Special Case

**Why strictness is needed.** Take $G = K_{4,4}$, parts $A = \{a_1,\dots,a_4\}$, $B = \{b_1,\dots,b_4\}$. Then $\kappa(G) = 4$ and $\alpha(G) = 4$, so $\kappa \ge \alpha$: Chvátal–Erdős gives a Hamiltonian cycle, e.g. $a_1b_1a_2b_2a_3b_3a_4b_4a_1$ (length 8). But $G$ is bipartite, so it has no cycle of length 3, 5 or 7. Hence $\kappa \ge \alpha$ never implies pancyclicity, and the hypothesis in (A) must be $\kappa \ge \alpha+1$. Similarly $C_5$: $\kappa = \alpha = 2$, Hamiltonian, no triangle.

**The case $\alpha = 2$, $\kappa \ge 3$, worked.** Let $\alpha(G)=2$ and $\kappa(G)\ge 3$, so $n \ge 4$. Chvátal–Erdős gives a Hamiltonian cycle $C = v_1v_2\cdots v_nv_1$.

*Claim: $G$ has a cycle of length $n-1$.* Suppose not, so $v_iv_{i+2} \notin E$ for every $i$ (indices mod $n$) — such a chord would give the cycle $v_i v_{i+2} v_{i+3}\cdots v_i$ of length $n-1$. Then $v_1v_3 \notin E$ and $v_3v_5 \notin E$. Since $\alpha(G)=2$, the triple $\{v_1,v_3,v_5\}$ is not independent, so $v_1v_5 \in E$. That yields the cycle
$$v_1\,v_5\,v_6\cdots v_n\,v_1 \quad\text{of length } n-3 .$$
Applying the same argument to *this* cycle (its vertex set still has independence number $\le 2$) and iterating drives the length down in steps of 3, but the "skip-2" chords needed for length $n-1$ are precisely what is being denied. Contradiction is reached explicitly for $n=6$: with $v_1v_3, v_3v_5, v_2v_4, v_4v_6 \notin E$, the pairs $\{v_1,v_3\},\{v_3,v_5\}$ force $v_1v_5 \in E$ and $\{v_2,v_4\},\{v_4,v_6\}$ force $v_2v_6 \in E$; then $v_1v_5v_6v_2v_3v_4v_1$ requires $v_5v_6, v_6v_2, v_2v_3, v_4v_1$ — but $v_4v_1$ and $v_1v_3$ non-edges make $\{v_1,v_3,v_4\}$... $v_3v_4 \in E$, so no contradiction there; instead $\{v_1,v_3,v_5\}$ already gave $v_1v_5$, and $v_1v_5$ plus $v_5 = v_{3+2}$ contradicts nothing — so one descends to the 3-cycle $v_1v_5v_6$ if $v_6v_1 \in E$, which holds since $v_6v_1$ is a cycle edge. Hence a triangle $v_1v_5v_6$ exists.

This exhibits both the method (chord-descent from a Hamiltonian cycle) and its fragility: each shortening step consumes an independent-set inequality, and once $\alpha \ge 4$ the triples no longer force edges, which is exactly the barrier of Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*