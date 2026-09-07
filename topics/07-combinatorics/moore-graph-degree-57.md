---
id: 07-combinatorics/moore-graph-degree-57
title: "Moore Graph of Degree 57 Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Moore Graph of Degree 57 Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/moore-graph-degree-57` · **Status:** open

## 1. Problem Statement / Conjecture

**Question.** Does there exist a graph that is $57$-regular, has diameter $2$ and girth $5$?

Equivalently: does there exist a strongly regular graph with parameters
$$\mathrm{SRG}(3250,\,57,\,0,\,1)?$$
That is, a simple undirected graph $G$ on $3250$ vertices in which every vertex has exactly $57$ neighbours, adjacent vertices have **no** common neighbour (triangle-free), and non-adjacent vertices have **exactly one** common neighbour.

Such a graph is called a *Moore graph of degree $57$ and diameter $2$*. Hoffman and Singleton (1960) proved that a Moore graph of diameter $2$ can only have degree $k \in \{2,3,7,57\}$; the first three exist and are unique (the $5$-cycle, the Petersen graph, the Hoffman–Singleton graph). Only $k=57$ is undecided — hence "the missing Moore graph".

A complete resolution is either (a) an explicit construction of one such graph together with a verification of its parameters, or (b) a proof that no graph with parameters $\mathrm{SRG}(3250,57,0,1)$ exists. A partial resolution would be a classification of all such graphs up to isomorphism if any exist.

## 2. Mathematical Foundations

**Moore bound.** For a $k$-regular graph of diameter $d$, breadth-first search from any vertex gives
$$n \;\le\; 1 + k\sum_{i=0}^{d-1}(k-1)^i \;=\; n_{\mathrm{Moore}}(k,d).$$
For $d=2$ this is $n \le k^2+1$. Graphs attaining the bound are **Moore graphs**; equality forces girth $5$ (for $k\ge 3$) and forces the graph to be strongly regular with $\lambda=0$, $\mu=1$.

**Adjacency algebra.** Let $A$ be the adjacency matrix, $J$ the all-ones matrix, $I$ the identity. Counting walks of length $2$ in a Moore graph of diameter $2$ and degree $k$ gives
$$A^2 + A - (k-1)I = J .$$
On the space orthogonal to the all-ones vector ($JA$-eigenvalue $0$), any eigenvalue $\theta$ satisfies $\theta^2+\theta-(k-1)=0$, so
$$\theta_{\pm} \;=\; \frac{-1 \pm \sqrt{4k-3}}{2},$$
alongside the Perron eigenvalue $k$ with multiplicity $1$.

**Multiplicities.** Write $t=\sqrt{4k-3}$. With $m_+ + m_- = k^2$ and $k + \theta_+m_+ + \theta_-m_- = \operatorname{tr}A = 0$,
$$m_{\pm} \;=\; \frac{1}{2}\left(k^2 \pm \frac{k^2-2k}{\sqrt{4k-3}}\right).$$

**Hoffman–Singleton theorem.** If $t$ is irrational then $m_+=m_-$ forces $k^2-2k=0$, i.e. $k=2$ ($C_5$). Otherwise $t=s\in\mathbb{Z}_{>0}$, $k=(s^2+3)/4$, and $s \mid k(k-2) = (s^4-2s^2-15)/16$, whence $s \mid 15$, so $s\in\{1,3,5,15\}$ and
$$k \in \{1,\,3,\,7,\,57\}.$$

**The case $k=57$.** Then $n = 3250 = 2\cdot 5^3\cdot 13$, $t = 15$, $\theta_+ = 7$, $\theta_- = -8$, and
$$m_+ = 1729, \qquad m_- = 1520, \qquad 1+1729+1520 = 3250 .$$

**Derived invariants (unconditional, if $G$ exists).** Hoffman's ratio bound gives independence number
$$\alpha(G) \;\le\; \frac{n\,(-\theta_-)}{k-\theta_-} \;=\; \frac{3250\cdot 8}{57+8} \;=\; 400,$$
hence $\chi(G) \ge 3250/400 > 8$, i.e. $\chi(G)\ge 9$. The number of $5$-cycles, $6$-cycles, and every local subgraph count is determined by the parameters; $G$ carries a $3$-class... in fact a $2$-class association scheme, and its Krein parameters and absolute bound are all satisfied — no feasibility condition in the standard toolkit (Brouwer–Cohen–Neumaier) excludes it.

## 3. History & State of the Art (SOTA)

- **1960.** A. J. Hoffman and R. R. Singleton, working at IBM, introduce Moore graphs (named for E. F. Moore, who posed the degree/diameter question) and prove the $k\in\{2,3,7,57\}$ classification for diameter $2$, plus $k=2$ only for diameter $3$. They construct the unique $\mathrm{SRG}(50,7,0,1)$ — the Hoffman–Singleton graph — and leave $k=57$ open.
- **1968.** Singleton shows Moore graphs must be regular (no "irregular Moore graph"), removing a degree-of-freedom.
- **1971.** Aschbacher proves there is no rank-$3$ permutation group of degree $3250$ and subdegree $57$: the missing graph cannot have an automorphism group acting with rank $3$ (the way $C_5$, Petersen and Hoffman–Singleton all do).
- **1973.** Damerell, and independently Bannai–Ito, prove that for diameter $d\ge 3$ the only Moore graphs are the odd cycles $C_{2d+1}$. This isolates $k=57,\,d=2$ as the *unique* remaining open case in the entire Moore-graph classification.
- **~1970s.** G. Higman proves a Moore graph of degree $57$ cannot be vertex-transitive; the argument (a fixed-point count for automorphisms of prime order acting on the eigenspaces) circulated in lectures and appears in print in Cameron's texts. Consequence: no such graph is a Cayley graph.
- **2010.** Mačaj and Širáň, combining representation-theoretic constraints with exhaustive computer search over local configurations, prove $|\mathrm{Aut}(G)| \le 375$ and constrain the possible orders and fixed-point structures of automorphisms. Since $375 \ll 3250$, every orbit is tiny relative to the graph.
- **Present.** Existence remains open. No construction, no non-existence proof, and no exhaustive search is within computational reach.

## 4. Partial Results / Verified Cases

- **Full classification for $k \ne 57$, $d=2$:** $k=2$ ($C_5$, $n=5$), $k=3$ (Petersen graph, $n=10$, unique), $k=7$ (Hoffman–Singleton graph, $n=50$, unique — uniqueness by Hoffman–Singleton's own argument and later by Bondy–Murty-style local counting).
- **All diameters $d\ge 3$:** only odd cycles (Damerell 1973; Bannai–Ito 1973). For $d\ge 3$ and $k\ge 3$ no Moore graph exists.
- **Irregular case:** eliminated by Singleton (1968); the analogous $\lambda=0,\mu=1$ *non-regular* problem is the friendship theorem of Erdős–Rényi–Sós (only windmills).
- **Symmetry restrictions on the $k=57$ case:**
  - not rank $3$ (Aschbacher 1971);
  - not vertex-transitive, hence not a Cayley graph, hence not arc-transitive or distance-transitive (Higman);
  - $|\mathrm{Aut}(G)|\le 375$ with strong constraints on element orders (Mačaj–Širáň 2010). In particular no large group can act, and the graph — if it exists — is essentially "generic" and almost asymmetric.
- **Spectral/combinatorial invariants determined:** $n=3250$, spectrum $\{57^1,\,7^{1729},\,(-8)^{1520}\}$, $\alpha(G)\le 400$, $\chi(G)\ge 9$, girth $5$, every edge lies in $0$ triangles, every non-edge in exactly one path of length $2$.

## 5. Principal Obstacles

- **All standard feasibility tests pass.** The integrality, Krein, absolute-bound and Delsarte/LP conditions used to kill most putative strongly regular parameter sets are satisfied by $(3250,57,0,1)$. There is no known linear-programming or semidefinite bound that separates this parameter set from realizable ones.
- **No symmetry to exploit.** Every existence proof for a Moore graph (and most non-existence proofs for SRGs) leans on a group: $C_5$ is cyclic, Petersen is $\mathrm{Kneser}(5,2)$ with $S_5$-symmetry, Hoffman–Singleton is built from the $15$ points and $35$ lines of $\mathrm{PG}(3,2)$ with $\mathrm{P\Sigma U}(3,5)$ acting. Higman's and Mačaj–Širáň's results say precisely that this route is closed for $k=57$: the object, if it exists, has at most $375$ automorphisms on $3250$ vertices. Character-theoretic and orbit-counting methods therefore give almost nothing.
- **Search space is astronomically large.** Exhaustive isomorph-free generation succeeded for $n=50$; for $n=3250$ the number of partial extensions after fixing a few neighbourhoods explodes far beyond any orderly-generation or SAT/CP budget. Canonical-augmentation methods have no known symmetry to prune with — exactly because the graph is nearly asymmetric.
- **No candidate algebraic template.** $57 = 7^2+7+1$ is the number of points of $\mathrm{PG}(2,7)$, and $3250 = 2\cdot 5^3\cdot 13$, but no incidence geometry, code, or difference-set construction is known that produces the right local structure. Attempts to realize the graph as a graph on cosets, a spherical two-distance set, or a rank-$3$-like scheme all fail at the symmetry step.
- **Counting arguments saturate.** Triangle/pentagon/hexagon counts and interlacing (Haemers) yield exactly the invariants above and no contradiction; local analysis of a vertex neighbourhood reduces to a partition of $3192$ vertices into $57$ blocks with one-common-neighbour incidence — a design-like condition too weak to force a contradiction.

## 6. The Gap

Proven: $k=57$ is the only surviving degree; any such graph is an $\mathrm{SRG}(3250,57,0,1)$ with spectrum $\{57^1,7^{1729},(-8)^{1520}\}$ and $|\mathrm{Aut}| \le 375$.

Missing: a decision procedure of any kind that operates *without* symmetry. Concretely, the gap is between (i) parameter-level feasibility, which is fully verified, and (ii) realizability of a global combinatorial object. Crossing it requires either
- a new non-existence obstruction — an invariant that is computable from $(3250,57,0,1)$ and forced to be non-integral, negative, or contradictory (e.g. from the Terwilliger algebra, from a semidefinite hierarchy of level $\ge 3$, or from a topological/homological invariant of the local structure); or
- a construction from a genuinely non-group-theoretic source, since Higman's theorem forbids all transitive constructions.

## 7. Current Research (as of June 2026)

- **Degree/diameter community.** The problem is the flagship open case of the degree/diameter problem tracked in the dynamic survey of Miller and Širáň; groups at the Open University (UK), Slovak University of Technology (Širáň, Mačaj), and Australian/Newcastle collaborators (Miller's school, Pineda-Villavicencio) continue on structural restrictions and near-Moore graphs (defect $1$ and $2$).
- **Automorphism refinement.** Extensions of Mačaj–Širáň seeking to push $|\mathrm{Aut}(G)|$ down to $1$ (proving the graph would be asymmetric) are ongoing; a complete reduction to the trivial group would remove the last algebraic handle and is viewed as a natural next milestone. *(frontier — verify)*
- **Spherical-code / optimization viewpoint.** A line of work recasts the missing graph as an optimal spherical code or as the extremal point of an SDP relaxation — see L. J. Schulman, *The Missing Moore Graph as an Optimal Spherical Code* (preprint/journal, 2017–2019) *(frontier — verify)*. The hope is that higher levels of the Lasserre/sum-of-squares hierarchy over the $\{7,-8\}$ two-distance set detect infeasibility.
- **SAT/CP and algebraic-model search.** Encoding partial configurations as SAT instances with symmetry breaking, following the style of recent computer-assisted combinatorics (Schur numbers, Keller's conjecture), is being explored; current instances are far from closing. *(frontier — verify)*
- **Association-scheme algebra.** Terwilliger-algebra and coherent-configuration methods applied to $\mathrm{SRG}(3250,57,0,1)$ aim at new integrality obstructions beyond Krein.

## 8. Future Work

- Prove $\mathrm{Aut}(G)=1$ unconditionally; this would make the object provably asymmetric and might itself be leveraged into a counting contradiction (an asymmetric graph on $3250$ vertices with this rigidity is a strong statement).
- Develop *localized* non-existence: study the subgraph induced on the $3192$ vertices at distance $2$ from a fixed vertex, which decomposes into $57$ classes of size $56$; find a design-theoretic obstruction to the $\mu=1$ matching between classes.
- Push SDP/SOS hierarchies to level $3$–$4$ for the two-distance spherical realization in $\mathbb{R}^{1520}$ or $\mathbb{R}^{1729}$; a strictly infeasible relaxation would settle the problem.
- Search for constructions from non-classical sources: exceptional near-polygons, generalized quadrangle quotients, or ternary/quinary codes of length related to $3250 = 2\cdot 5^3\cdot 13$.
- Formalize the Hoffman–Singleton classification and the uniqueness of the $k=7$ graph in a proof assistant, as infrastructure for a future computer-assisted verdict at $k=57$.

## 9. Key References

- **[Foundational]** A. J. Hoffman and R. R. Singleton. *On Moore graphs with diameters 2 and 3.* IBM Journal of Research and Development, 4(5):497–504, 1960.
- **[Foundational]** R. R. Singleton. *There is no irregular Moore graph.* American Mathematical Monthly, 75(1):42–43, 1968.
- **[Foundational]** R. M. Damerell. *On Moore graphs.* Mathematical Proceedings of the Cambridge Philosophical Society, 74(2):227–236, 1973.
- **[Foundational]** E. Bannai and T. Ito. *On finite Moore graphs.* Journal of the Faculty of Science, University of Tokyo, Sect. IA Math., 20:191–208, 1973.
- **[Structural]** M. Aschbacher. *The nonexistence of rank three permutation groups of degree 3250 and subdegree 57.* Journal of Algebra, 19(3):538–540, 1971.
- **[SOTA / Recent]** M. Mačaj and J. Širáň. *Search for properties of the missing Moore graph.* Linear Algebra and its Applications, 432(9):2381–2398, 2010.
- **[Survey]** M. Miller and J. Širáň. *Moore graphs and beyond: A survey of the degree/diameter problem.* The Electronic Journal of Combinatorics, Dynamic Survey DS14, 2005 (revised 2013).
- **[Reference]** A. E. Brouwer, A. M. Cohen, A. Neumaier. *Distance-Regular Graphs.* Springer-Verlag, Ergebnisse der Mathematik 18, 1989.
- **[Reference]** C. Godsil and G. Royle. *Algebraic Graph Theory.* Springer, Graduate Texts in Mathematics 207, 2001 (Chapter 5: Moore graphs, Hoffman–Singleton theorem).
- **[Reference]** P. J. Cameron. *Permutation Groups.* London Mathematical Society Student Texts 45, Cambridge University Press, 1999 (contains Higman's non-vertex-transitivity argument).
- **[Related]** P. Erdős, A. Rényi, V. T. Sós. *On a problem of graph theory.* Studia Scientiarum Mathematicarum Hungarica, 1:215–235, 1966 (friendship theorem: the non-regular $\lambda=0,\mu=1$ case).

## 10. Worked Example / Concrete Special Case

**The $k=7$ case, done fully — the template that fails to extend to $57$.**

Set $k=7$. The Moore bound gives $n = 7^2+1 = 50$. With $t=\sqrt{4\cdot 7-3}=\sqrt{25}=5$, the non-principal eigenvalues are
$$\theta_{\pm} = \frac{-1\pm 5}{2} = 2,\,-3,$$
and the multiplicity formula gives
$$m_{\pm} = \frac12\left(49 \pm \frac{49-14}{5}\right) = \frac12(49\pm 7) \;\Rightarrow\; m_+ = 28,\; m_-=21,$$
so the spectrum is $\{7^1, 2^{28}, (-3)^{21}\}$ and $1+28+21=50$. ✓

Hoffman and Singleton realized this graph explicitly: take $5$ pentagons $P_0,\dots,P_4$ and $5$ pentagrams $Q_0,\dots,Q_4$, each on vertex set $\mathbb{Z}_5$, and join vertex $j$ of $P_h$ to vertex $hi+j \bmod 5$ of $Q_i$. Each vertex gets $2$ neighbours inside its own pentagon/pentagram and $5$ across, total $7$. ✓ One checks $\lambda=0,\mu=1$ directly.

**Now repeat the arithmetic for $k=57$.** $n = 57^2+1 = 3250$; $t=\sqrt{225}=15$; $\theta_+=7$, $\theta_-=-8$;
$$m_{\pm} = \frac12\left(3249 \pm \frac{3249-114}{15}\right) = \frac12(3249 \pm 209) \;\Rightarrow\; m_+=1729,\; m_-=1520 .$$
All integers — the arithmetic obstruction that kills $k=4,5,6,8,\dots$ simply does not appear. Every derived quantity is consistent: Hoffman's ratio bound gives $\alpha \le 3250\cdot 8/65 = 400$, and $400 \mid 3250$? No — $3250/400 = 8.125$, so a perfect partition into $9$ independent sets of size $400$ is impossible but $\chi\ge 9$ is not contradictory. The local decomposition also balances: fix a vertex $v$; its $57$ neighbours are pairwise non-adjacent (girth $5$), each has $56$ further neighbours, and $57\times 56 = 3192 = 3250-1-57$. ✓ Every count closes exactly.

That is the whole difficulty in miniature: for $k=7$ the arithmetic closes *and* a construction exists; for $k=57$ the arithmetic closes just as cleanly, and nothing — construction or contradiction — has been found in sixty-six years.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*