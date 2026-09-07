---
id: 07-combinatorics/erdos-rubin-taylor-conjecture
title: "Erdős-Rubin-Taylor Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Rubin-Taylor Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-rubin-taylor-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Erdős, Rubin and Taylor (1979), in the paper that introduced list colouring, asked whether set-colouring choosability scales linearly.

**Conjecture (ERT, 1979).** If a graph $G$ is $(a:b)$-choosable, then $G$ is $(am:bm)$-choosable for every integer $m \ge 1$.

Here $(a:b)$-choosable means: for every assignment of colour lists of size $a$ to the vertices, one can pick a $b$-element subset of each vertex's list so that adjacent vertices receive disjoint subsets. The case $b=1$ is ordinary $k$-choosability ($k$-list-colourability).

**Status.** The conjecture is **false as stated**: Dvořák, Hu and Sereni (2019) constructed a graph that is $4$-choosable (i.e. $(4:1)$-choosable) but not $(8:2)$-choosable, killing the case $a=4$, $b=1$, $m=2$. What survives, and is the live problem, is the classification question:

1. For which pairs $(a,b)$ and which $m$ does the implication hold? (True for $a=2,b=1$, all $m$, by Tuza–Voigt.)
2. Does it hold *eventually*, i.e. is there for each $G$ an $m_0$ such that $(a:b)$-choosable implies $(am:bm)$-choosable for all $m \ge m_0$, or along multiplicative chains $m \mid m'$?
3. Is $3$-choosable $\Rightarrow$ $(6:2)$-choosable? Still open.

A complete resolution means either a proof of the implication for a stated family, or a counterexample construction, in each of these regimes.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite simple graph.

**List assignment.** $L: V \to 2^{\mathbb{N}}$ with $|L(v)| = a$ for all $v$.

**Set colouring.** A map $\varphi$ with $\varphi(v) \subseteq L(v)$, $|\varphi(v)| = b$, and
$$\varphi(u) \cap \varphi(v) = \varnothing \quad \text{for every } uv \in E .$$
$G$ is **$(a:b)$-choosable** if such $\varphi$ exists for every $a$-list assignment $L$. Write $\mathrm{Ch}(G) = \{(a,b) : G \text{ is } (a{:}b)\text{-choosable}\}$.

**Elementary facts.**
- $(a:b)$-choosable $\Rightarrow$ $(a+1:b)$-choosable and $\Rightarrow$ $(a:b')$-choosable is *not* automatic for $b' < b$ in general, though $(a:b)\Rightarrow(a:b-1)$ does hold by deleting a colour only when lists are shrunk consistently; the safe monotonicity is in $a$.
- $\chi_\ell(G) = \min\{a : (a,1) \in \mathrm{Ch}(G)\}$ is the choice number; $\chi(G) \le \chi_\ell(G) \le \Delta(G)+1$.
- The **fractional list chromatic number** is
$$\chi_f^\ell(G) = \inf\Big\{ \tfrac{a}{b} : G \text{ is } (a{:}b)\text{-choosable} \Big\}.$$

**Theorem (Alon–Tuza–Voigt, 1997).** For every graph $G$,
$$\chi_f^{\ell}(G) = \chi_f(G),$$
and the infimum is attained: there exists $b$ with $G$ being $(b\,\chi_f(G) : b)$-choosable. So the *ratio* asymptotics are settled; ERT concerns the much finer question of which individual pairs $(am,bm)$ are realisable.

**Theorem (ERT, 1979 — characterisation of $2$-choosability).** Let the *core* of $G$ be the graph obtained by iteratively deleting vertices of degree $\le 1$. Then $G$ is $2$-choosable iff its core is $K_1$, an even cycle $C_{2k}$, or the theta graph $\theta_{2,2,2k}$ (two vertices joined by three internally disjoint paths of lengths $2,2,2k$).

**Structural reformulation.** $(am:bm)$-choosability of $G$ is equivalent to ordinary list-colourability of a *blow-up*-type hypergraph: the deficiency of the naive reduction — replacing each vertex by $bm$ copies — is that copies of a vertex must draw from the same list, which destroys independence and is precisely why induction on $m$ fails.

## 3. History & State of the Art (SOTA)

- **1979.** Erdős, Rubin and Taylor, *Choosability in graphs*, define $(a:b)$-choosability, characterise $2$-choosable graphs, pose the scaling conjecture and the companion question of ratio monotonicity ("does $(a:b)$-choosable and $a'/b' \ge a/b$ imply $(a':b')$-choosable?"). Vizing had introduced list colouring independently in 1976 for $b=1$.
- **1993–1994.** Voigt exhibits a planar graph that is not $4$-choosable; Thomassen proves every planar graph is $5$-choosable. These fixed $\chi_\ell$ for planar graphs but say nothing about $b \ge 2$.
- **1996.** Tuza and Voigt prove the conjecture for $a=2$: every $2$-choosable graph is $(2m:m)$-choosable for all $m$. This remains the only complete positive instance of the conjecture for a whole choosability class.
- **1997.** Alon, Tuza and Voigt prove $\chi_f^\ell = \chi_f$ with attainment, showing the conjecture is "true in the limit of ratios".
- **2009.** Gutner and Tarsi, *Some results on $(a:b)$-choosability*, give constructions and complexity results ($(a:b)$-choosability testing is $\Pi_2^p$-complete in general, extending Gutner's 1996 hardness result for $3$-choosability of planar graphs), and show that the naive monotonicity heuristics used to attack ERT fail.
- **2019.** Dvořák, Hu and Sereni, *A 4-choosable graph that is not $(8:2)$-choosable* (Advances in Combinatorics), disprove the conjecture. The construction is a carefully engineered gadget graph with a list system in which every $4$-list-colouring extends, but a $2$-fold selection from $8$-lists is blocked by a parity/counting obstruction.

## 4. Partial Results / Verified Cases

- **$a = 2$, all $m$ (complete).** Tuza–Voigt (1996): $2$-choosable $\Rightarrow$ $(2m:m)$-choosable for every $m \ge 1$. Covers even cycles $C_{2k}$, $\theta_{2,2,2k}$, forests, and any graph whose core is one of these.
- **Trees / degenerate graphs.** A $d$-degenerate graph is $(a:b)$-choosable whenever $a \ge (d+1)b$; greedy in a degeneracy order gives $|L(v)| - d\,b \ge b$ free colours. Hence the ERT implication is trivially true for the pairs $(a,b)$ with $a/b \ge d+1$.
- **Complete graphs.** $K_n$ is $(a:b)$-choosable iff $a \ge nb$ (necessity by identical lists), so $\mathrm{Ch}(K_n)$ is exactly ratio-closed and the implication holds.
- **Ratio-asymptotic regime.** By Alon–Tuza–Voigt, every $G$ is $(b\chi_f(G):b)$-choosable for some $b$, and then for all multiples of that $b$; e.g. $C_{2k+1}$ has $\chi_f = 2 + \tfrac1k$ and is $((2k+1)m : km)$-choosable.
- **Refuted case.** $(a,b,m) = (4,1,2)$: Dvořák–Hu–Sereni graph, $4$-choosable but not $(8:2)$-choosable. Their argument also yields $k$-choosable non-$(2k:2)$-choosable graphs for $k \ge 4$ by adding dominating structure.
- **Open small cases.** $3$-choosable $\Rightarrow$ $(6:2)$-choosable; $(4:2)$-choosable $\Rightarrow$ $(8:4)$-choosable; and every case with $m \ge 3$ for $a=3,4$.

## 5. Principal Obstacles

- **No induction on $m$.** A $(am:bm)$-colouring cannot be assembled from $m$ independent $(a:b)$-colourings, because the $m$ copies would have to draw from the same $a$-sublist, and no mechanism forces the lists of size $am$ to split into $m$ lists of size $a$ that are simultaneously good. Every attempted "split-and-recombine" proof breaks at exactly this point.
- **Kernel and orientation methods are $b$-blind.** The Bondy–Boppana–Siegel kernel method and the Alon–Tarsi orientation theorem certify $(a:1)$-choosability from a digraph invariant (kernel-perfect orientation, or $\mathrm{EE}(D) \ne \mathrm{EO}(D)$). Their algebraic proofs use Combinatorial Nullstellensatz on the graph polynomial $\prod_{uv \in E}(x_u - x_v)$, whose variables are *single* colours. There is no known polynomial whose non-vanishing coefficients encode disjointness of $b$-sets, so these certificates give no lower bound on $b$-fold choosability.
- **Probabilistic bounds are ratio-level only.** Local-lemma and entropy-compression arguments control $a/b$ but lose constant factors, so they cannot distinguish $(8:2)$ from $(4:1)$ — precisely the distinction the conjecture is about.
- **Complexity barrier.** $(a:b)$-choosability is $\Pi_2^p$-complete (Gutner–Tarsi), so no polynomial-size certificate is expected, and exhaustive search over $\binom{am}{bm}^{|V|}$ selections is infeasible beyond tiny graphs — the DHS counterexample needed a tailored algebraic obstruction, not search.
- **Sparse counterexample supply.** Only one essentially distinct counterexample family is known; there is no flexible construction toolkit to probe $a=3$ or $m=3$.

## 6. The Gap

Proven: the implication for $a=2$ (all $m$), for degenerate/trivial ratio regimes, and asymptotically in the ratio sense. Refuted: $a=4$, $b=1$, $m=2$.

The gap is the entire middle band $3 \le a/b < \infty$ with small $m$. Concretely, the missing step is a *transfer principle*: a way to convert a $b$-fold selection certificate at parameters $(a,b)$ into one at $(am, bm)$, or a proof that no such principle exists. The DHS counterexample shows the transfer fails for $(4,1)\to(8,2)$ but does not identify the invariant responsible. Nobody knows a graph parameter $\pi$ with
$$\pi(G) \le a/b \iff G \text{ is } (a{:}b)\text{-choosable},$$
and the DHS result proves that $\chi_f^\ell$ alone cannot be it, since $\mathrm{Ch}(G)$ is not determined by ratios. Crossing the gap means describing the true shape of the region $\mathrm{Ch}(G) \subseteq \mathbb{Z}^2_{>0}$ — whether it is eventually a cone, whether it is closed under multiplication by large $m$, and whether $3$-choosability behaves like $2$- or like $4$-choosability.

## 7. Current Research (as of June 2026)

- **Post-DHS classification.** Work by Dvořák and collaborators (Charles University) on refining the gadget to reach $a=3$: whether a $3$-choosable non-$(6:2)$-choosable graph exists is the single most-cited remaining case. *(frontier — verify)*
- **DP-colouring (correspondence colouring).** Dvořák–Postle's DP-colouring is a strictly stronger local-constraint model in which many list phenomena become monotone; groups around Bernshteyn (Georgia Tech / CMU), Kostochka (UIUC) and Kaul–Mudrock (Illinois Tech) study whether the $m$-fold DP analogue is better behaved, which would isolate exactly the "list-specific" reason ERT fails. *(frontier — verify)*
- **Fractional / eventual scaling.** Refinements of Alon–Tuza–Voigt aimed at bounding the least $b$ attaining $\chi_f^\ell = \chi_f$ in terms of $|V(G)|$ or $\Delta$; a polynomial bound would make the "eventual" version of ERT effectively checkable.
- **Planar $b$-fold choosability.** Whether every planar graph is $(5m:m)$-choosable for all $m$, and whether Cranston–Rabern's $9/2$-colourability of planar graphs has a list analogue $((9:2)$-choosability$)$, are actively pursued; Voigt's non-$4$-choosable planar graph rules out ratio $4$. *(frontier — verify)*

## 8. Future Work

- Build an algebraic certificate for $b$-fold list colouring — a polynomial or Nullstellensatz-type criterion generalising Alon–Tarsi to set colourings — which would either prove positive cases or explain the obstruction.
- Determine whether $\mathrm{Ch}(G)$ is closed under $m \mapsto m!$ or other divisibility-structured scalings; a "chain" theorem would salvage most applications of ERT.
- Settle $3$-choosable $\Rightarrow (6:2)$-choosable, the smallest undecided case.
- Extend Tuza–Voigt beyond $a=2$ using the core-structure characterisation: is there a structural classification of $(3:1)$-choosable graphs sharp enough to run the same argument?
- Randomised/computer search over small gadgets with SAT/QBF solvers (the problem sits naturally at $\Pi_2^p$, matching QBF with one alternation).

## 9. Key References

- **[Foundational]** P. Erdős, A. L. Rubin, H. Taylor. *Choosability in graphs.* Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, Congressus Numerantium XXVI, 1979, pp. 125–157.
- **[Foundational]** V. G. Vizing. *Coloring the vertices of a graph in prescribed colors.* Diskret. Analiz 29 (1976), 3–10.
- **[SOTA]** Z. Dvořák, X. Hu, J.-S. Sereni. *A 4-choosable graph that is not (8:2)-choosable.* Advances in Combinatorics, 2019:5.
- **[Partial result]** Zs. Tuza, M. Voigt. *Every 2-choosable graph is (2m:m)-choosable.* Journal of Graph Theory 22 (1996), 245–252.
- **[Partial result]** N. Alon, Zs. Tuza, M. Voigt. *Choosability and fractional chromatic numbers.* Discrete Mathematics 165/166 (1997), 31–38.
- **[Structure/complexity]** S. Gutner, M. Tarsi. *Some results on (a:b)-choosability.* Discrete Mathematics 309 (2009), 2260–2270.
- **[Method]** N. Alon, M. Tarsi. *Colorings and orientations of graphs.* Combinatorica 12 (1992), 125–134.
- **[Related]** C. Thomassen. *Every planar graph is 5-choosable.* Journal of Combinatorial Theory Series B 62 (1994), 180–181.
- **[Related]** M. Voigt. *List colourings of planar graphs.* Discrete Mathematics 120 (1993), 215–219.
- **[Survey]** Zs. Tuza. *Graph colorings with local constraints — a survey.* Discussiones Mathematicae Graph Theory 17 (1997), 161–228.
- **[Survey]** N. Alon. *Restricted colorings of graphs.* In *Surveys in Combinatorics 1993*, LMS Lecture Note Series 187, Cambridge Univ. Press, 1993, pp. 1–33.
- **[Book]** T. R. Jensen, B. Toft. *Graph Coloring Problems.* Wiley, 1995.
- **[Book]** E. R. Scheinerman, D. H. Ullman. *Fractional Graph Theory.* Wiley, 1997.

## 10. Worked Example / Concrete Special Case

**(a) $C_4$ is $2$-choosable, and its $m=2$ instance.** Let $C_4 = v_1v_2v_3v_4$ with $4$-lists (the $(4:2)$ case). Take the adversarial assignment
$$L_1 = L_3 = \{1,2,3,4\}, \quad L_2 = \{1,2,5,6\}, \quad L_4 = \{3,4,5,6\}.$$
Greedy from $v_1$ can fail: choosing $A_1 = \{1,2\}$, $A_2 = \{5,6\}$, $A_3 = \{3,4\}$ leaves $v_4$ needing $2$ colours in $L_4 \setminus (A_3 \cup A_1) = \{5,6\}$ — which works — but the alternative $A_2 = \{5,6\}, A_4 = \{5,6\}$ shows the choices are not independent. A valid selection is
$$A_1 = \{1,2\},\ A_2 = \{5,6\},\ A_3 = \{3,4\},\ A_4 = \{5,6\},$$
with $A_1 \cap A_2 = A_2 \cap A_3 = A_3 \cap A_4 = A_4 \cap A_1 = \varnothing$. The general proof of the $m=2$ case splits on $|L_1 \cap L_3|$: if $|L_1 \cap L_3| \ge 2$, set $A_1 = A_3 = A \subseteq L_1 \cap L_3$ with $|A| = 2$; then $|L_2 \setminus A| \ge 2$ and $|L_4 \setminus A| \ge 2$, so $v_2, v_4$ are fed independently. Symmetrically if $|L_2 \cap L_4| \ge 2$. Tuza–Voigt handle the remaining near-disjoint case for all even cycles and all $m$, giving $(2m:m)$-choosability.

**(b) Why sharpness is delicate: $K_{2,4}$ is not $2$-choosable.** Let the side of size $2$ be $u_1,u_2$ with $L(u_1) = \{1,2\}$, $L(u_2) = \{3,4\}$, and let the four vertices on the other side carry the lists
$$\{1,3\},\ \{1,4\},\ \{2,3\},\ \{2,4\}.$$
Any choice $c(u_1) \in \{1,2\}$, $c(u_2) \in \{3,4\}$ produces the pair $\{c(u_1),c(u_2)\}$, which is exactly one of the four lists; that vertex has no legal colour. So $\chi_\ell(K_{2,4}) \ge 3$, consistent with ERT's core criterion (the core of $K_{2,4}$ is $K_{2,4}$ itself, which is neither an even cycle nor $\theta_{2,2,2k}$).

**(c) The shape of the failure.** The Dvořák–Hu–Sereni graph replaces this hand-sized blocking system by one that is defeated by every $4$-list assignment yet survives, in $2$-fold form, against all $8$-lists: the number of "blocked" $2$-subsets grows like $\binom{8}{2} = 28$ per vertex while the number of usable ones grows only linearly along the gadget, so a counting obstruction that is vacuous at $b=1$ becomes fatal at $b=2$. That asymmetry between $\binom{am}{bm}$ and the linear structure of the gadget is exactly the phenomenon that no ratio-level argument can see.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*