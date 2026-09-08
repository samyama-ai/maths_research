---
id: 07-combinatorics/cereceda-conjecture
title: "Cereceda's Conjecture on Recoloring Diameter"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cereceda's Conjecture on Recoloring Diameter

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/cereceda-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G$ be a $d$-degenerate graph on $n$ vertices and let $k \ge d+2$. Consider the *reconfiguration graph* $\mathcal{C}_k(G)$ whose vertices are the proper $k$-colorings of $G$, with two colorings adjacent when they differ on exactly one vertex.

**Cereceda's Conjecture (2007).** For every $d \ge 1$ and every $k \ge d+2$ there is a constant $C = C(d,k)$ such that for every $d$-degenerate graph $G$ on $n$ vertices,
$$\operatorname{diam}\bigl(\mathcal{C}_k(G)\bigr) \le C\,n^2 .$$
The strong form asks for an absolute constant, i.e. $\operatorname{diam}(\mathcal{C}_k(G)) = O(n^2)$ with the implied constant independent of $d$ and $k$.

Connectivity of $\mathcal{C}_k(G)$ for $k \ge d+2$ is already known and easy; the content of the conjecture is the *quadratic* bound on the number of single-vertex recolorings needed. A complete proof must give the quadratic upper bound for all $d$-degenerate $G$ and all $k \ge d+2$; a disproof needs a family of $d$-degenerate graphs with $(d+2)$-recoloring diameter $\omega(n^2)$. The threshold $k = d+2$ is sharp: for $k = d+1$ the reconfiguration graph can be disconnected (e.g. $\mathcal{C}_3$ of a properly 3-colored $C_6$ has frozen colorings), so no finite diameter bound holds.

## 2. Mathematical Foundations

**Degeneracy.** $G$ is *$d$-degenerate* if every subgraph has a vertex of degree $\le d$; equivalently there is an ordering $v_1,\dots,v_n$ (a *degeneracy order*) with
$$\bigl|\{\,j < i : v_jv_i \in E(G)\,\}\bigr| \le d \quad \text{for all } i .$$
Degeneracy $d$ implies $\chi(G) \le d+1$. Forests are $1$-degenerate, planar graphs $5$-degenerate, graphs of treewidth $t$ are $t$-degenerate.

**Reconfiguration graph.** $V(\mathcal{C}_k(G)) = \{c : V(G) \to [k] \mid c(u)\neq c(v) \ \forall uv \in E\}$, and $c \sim c'$ iff $|\{v : c(v)\neq c'(v)\}| = 1$. Write $\mathrm{d}_k(c,c')$ for the graph distance. $\mathcal{C}_k(G)$ is the state space of the Glauber dynamics for the antiferromagnetic $k$-state Potts model at zero temperature; connectivity and diameter control ergodicity and (heuristically) mixing.

**Connectivity theorem (Dyer–Flaxman–Frieze–Vigoda 2006; Cereceda–van den Heuvel–Johnson 2008).** If $G$ is $d$-degenerate and $k \ge d+2$ then $\mathcal{C}_k(G)$ is connected. Proof sketch: in a degeneracy order, $v_i$ has $\le d$ back-neighbours, so at least $2$ colors are free for it; recursively recolor $v_n, v_{n-1},\dots$ to a canonical coloring. The recursion is naive and yields no polynomial bound.

**Lower bound.** There exist $d$-degenerate graphs (already $d=1$, paths) with $\mathrm{d}_{d+2}(c,c') = \Omega(n^2)$, so $n^2$ is the correct order if the conjecture holds (see §10).

**Contrast with small $k$.** Bonsma and Cereceda (2009) proved that for $k \ge 4$ deciding $c \sim^* c'$ in $\mathcal{C}_k(G)$ is PSPACE-complete, and constructed instances with superpolynomial $\mathrm{d}_k(c,c')$. Those graphs have degeneracy $\ge k-1$, i.e. they live exactly at $k \le d+1$, outside the conjecture's regime; the conjecture asserts that one extra color collapses superpolynomial distances to quadratic.

## 3. History & State of the Art (SOTA)

- **2007.** Luis Cereceda formulates the conjecture in his PhD thesis *Mixing graph colourings* (London School of Economics, supervised by Jan van den Heuvel), after observing that all known $d$-degenerate examples with $k \ge d+2$ have quadratic diameter.
- **2008–2011.** Cereceda, van den Heuvel and Johnson develop the $3$-coloring theory: connectivity of $\mathcal{C}_3$ is decidable in polynomial time, and when $\mathcal{C}_3(G)$ is connected its diameter is $O(n^2)$ — the conjecture for $k=3$ in the strongest sense.
- **2014–2018.** Structural cases: Bonamy, Johnson, Lignos, Patel and Paulusma prove quadratic (indeed $O(n^2)$, and linear for chordal graphs with $k \ge \mathrm{tw}+2$) bounds for chordal and chordal bipartite graphs; Bonamy and Bousquet extend this via tree decompositions to bounded-treewidth graphs.
- **2016.** Bousquet and Perarnau, *Fast recolouring of sparse graphs*: for $k \ge 2d+2$ the diameter is $O(n)$ — linear, hence far better than conjectured, but only for twice as many colors.
- **2019–2021.** Feghali gives $O(n\log n)$ bounds for graphs of bounded maximum average degree with $k$ just above the density threshold, and Eiben–Feghali push toward the planar case.
- **2022 (SOTA).** Bousquet and Heinrich, *A polynomial version of Cereceda's conjecture* (JCTB): the first polynomial bound at the conjectured threshold, $\operatorname{diam}(\mathcal{C}_k(G)) = O(n^{d+1})$ for all $k \ge d+2$, together with an $O(n^2)$ bound for $k \ge \tfrac{3}{2}(d+1)$.

## 4. Partial Results / Verified Cases

| Class / regime | Bound | Source |
|---|---|---|
| $k = 3$, $\mathcal{C}_3(G)$ connected (any $G$) | $O(n^2)$ | Cereceda–van den Heuvel–Johnson (2011) |
| $d$-degenerate, $k \ge d+2$ | $O(n^{d+1})$ | Bousquet–Heinrich (2022) |
| $d$-degenerate, $k \ge \lceil 3(d+1)/2\rceil$ | $O(n^2)$ | Bousquet–Heinrich (2022) |
| $d$-degenerate, $k \ge 2d+2$ | $O(n)$ | Bousquet–Perarnau (2016) |
| Chordal, $k \ge \mathrm{tw}+2$ | $O(n^2)$ (linear in many cases) | Bonamy–Johnson–Lignos–Patel–Paulusma (2014) |
| Treewidth $t$, $k \ge t+2$ | $O(n^2)$ | Bonamy–Bousquet (2018) |
| Bounded maximum average degree, $k$ slightly above threshold | $O(n\log n)$ | Feghali (2019, 2021) |
| $d = 1$ (forests), $k \ge 3$ | $\Theta(n^2)$, tight | Cereceda (2007); §10 below |
| List/correspondence versions, $k \ge 2d+2$ | optimal constants in $\Theta(n)$/$\Theta(n^2)$ | Cambie–Cames van Batenburg–Cranston (2023) |

So the conjecture is **proved for $d \le 2$** at the threshold ($d=1$: $k\ge3$; $d=2$: $k\ge4 \ge \lceil 3\cdot 3/2\rceil$ requires $k \ge 5$ — the case $d=2,k=4$ follows instead from the treewidth/chordal machinery only for restricted classes, and is open in general), and **for every $d$ once $k \ge \tfrac32(d+1)$**.

## 5. Principal Obstacles

- **No monotone potential at $k = d+2$.** Every quadratic proof so far builds a potential function or amortized charging scheme in which each vertex is recolored $O(n)$ times. With exactly $d+2$ colors, a vertex low in the degeneracy order may have only $2$ available colors, and freeing one of them can force a cascade through all $d$ back-neighbours. Bousquet–Heinrich's recursion pays a factor $n$ per degeneracy level, giving $n^{d+1}$; removing that per-level factor is exactly the missing idea.
- **Slack is what all fast methods consume.** For $k \ge 2d+2$ every vertex has $\ge d+2$ free colors, so a "recolor to a canonical target, then fix conflicts" strategy terminates in linear time. At $k = d+2$ there is zero slack, and canonical-target arguments have no room to route around blocked vertices.
- **Degeneracy is a global, order-dependent parameter.** Unlike treewidth, it gives no separator structure, so divide-and-conquer (the engine of the bounded-treewidth proofs) does not apply.
- **Markov-chain tools do not transfer.** Rapid mixing results for Glauber dynamics need $k \ge (1+\varepsilon)\Delta$ or path-coupling conditions; they say nothing about worst-case diameter for sparse graphs with maximum degree $\gg d$.
- **Superpolynomial distances exist one color below.** The Bonsma–Cereceda constructions show the landscape is genuinely wild at $k = d+1$, so any proof must use the extra color in an essential, non-local way.

## 6. The Gap

The gap is the interval
$$d+2 \ \le\ k \ <\ \tfrac{3}{2}(d+1),$$
where the best known bound is $O(n^{d+1})$ and the conjectured bound is $O(n^2)$ — a polynomial gap of degree $d-1$. Concretely, for planar graphs ($d = 5$) the conjecture predicts $O(n^2)$ for $k \ge 7$, while the proven bound at $k=7$ is $O(n^6)$; quadratic is known only from $k = 9$ onward. The exact step needed: a recoloring strategy at $k = d+2$ in which the total number of recolorings of the $i$-th back-neighbour layer does not multiply by $n$, i.e. an amortization showing each vertex is touched $O(n)$ times overall rather than $O(n^{\text{depth}})$.

## 7. Current Research (as of June 2026)

- **French school (Bousquet, Bartier, Heinrich, Perarnau, Bonamy; LIRMM / G-SCOP / LIP).** Refining the polynomial-to-quadratic ladder; targets are $k \ge d+3$ and the planar case at $k=7$. *(frontier — verify)* Improvements of the threshold below $\tfrac32(d+1)$ for structured sparse classes have circulated as preprints.
- **Sparse-density approaches (Feghali and coauthors).** Replacing degeneracy by maximum average degree $\mathrm{mad}(G)$, where discharging arguments give near-linear bounds; the hope is that a $\mathrm{mad}$-based proof can be lifted to degeneracy via a decomposition.
- **Optimal-constant program (Cambie, Cames van Batenburg, Cranston).** Determining exact leading constants for list- and correspondence-coloring reconfiguration, which sharpens the extremal examples that any proof must handle.
- **Complexity side.** Whether $\mathrm{d}_{d+2}(c,c')$ is computable in polynomial time for $d$-degenerate graphs; a positive answer at $k=3$ (Cereceda–van den Heuvel–Johnson) has not been extended.
- **Related thresholds.** Bousquet–Feuilloley–Heinrich–Rabie study *short and local* transformations between $(\Delta+1)$-colorings, importing distributed-computing techniques into the diameter question.

## 8. Future Work

1. **Prove $k = d+3$.** Widely viewed as the next milestone: a quadratic bound with one unit of slack would isolate exactly what the last color buys.
2. **Design a global potential.** A function $\Phi$ on colorings, of range $O(n^2)$, that strictly decreases along some canonical recoloring sequence at $k=d+2$; the path example (§10) shows $\Phi$ must have range $\Theta(n^2)$, so no linear-range potential can exist.
3. **Planar graphs at $k=7$.** A self-contained discharging/structural attack exploiting planarity rather than degeneracy alone.
4. **Search for a counterexample.** Exhaustive or SAT-based search over small $d$-degenerate graphs for $(d+2)$-recoloring distances exceeding $Cn^2$; none has been found.
5. **Transfer to Glauber mixing.** Prove that a quadratic diameter at $k=d+2$ implies polynomial mixing for the corresponding chain on $d$-degenerate graphs.

## 9. Key References

- **[Foundational]** Luis Cereceda. *Mixing graph colourings.* PhD thesis, London School of Economics and Political Science, 2007.
- **[Foundational]** L. Cereceda, J. van den Heuvel, M. Johnson. *Connectedness of the graph of vertex-colourings.* Discrete Mathematics 308 (2008), 913–919.
- **[Foundational]** L. Cereceda, J. van den Heuvel, M. Johnson. *Finding paths between 3-colourings.* Journal of Graph Theory 67 (2011), 69–82.
- **[Foundational]** M. Dyer, A. Flaxman, A. Frieze, E. Vigoda. *Randomly colouring sparse random graphs with fewer colours than the maximum degree.* Random Structures & Algorithms 29 (2006), 450–465.
- **[Complexity]** P. Bonsma, L. Cereceda. *Finding paths between graph colourings: PSPACE-completeness and superpolynomial distances.* Theoretical Computer Science 410 (2009), 5215–5226.
- **[Partial]** M. Bonamy, M. Johnson, I. Lignos, V. Patel, D. Paulusma. *Reconfiguration graphs for vertex colourings of chordal and chordal bipartite graphs.* Journal of Combinatorial Optimization 27 (2014), 132–143.
- **[Partial]** N. Bousquet, G. Perarnau. *Fast recolouring of sparse graphs.* European Journal of Combinatorics 52 (2016), 1–11.
- **[Partial]** M. Bonamy, N. Bousquet. *Recoloring graphs via tree decompositions.* European Journal of Combinatorics 69 (2018), 200–213.
- **[Partial]** C. Feghali. *Paths between colourings of sparse graphs.* European Journal of Combinatorics 75 (2019), 169–171.
- **[Partial]** E. Eiben, C. Feghali. *Toward Cereceda's conjecture for planar graphs.* Journal of Graph Theory 94 (2020), 267–277.
- **[SOTA]** N. Bousquet, M. Heinrich. *A polynomial version of Cereceda's conjecture.* Journal of Combinatorial Theory, Series B 155 (2022), 1–16.
- **[Recent]** S. Cambie, W. Cames van Batenburg, D. W. Cranston. *Optimally reconfiguring list and correspondence colourings.* Electronic Journal of Combinatorics, 2023.
- **[Survey]** J. van den Heuvel. *The complexity of change.* In *Surveys in Combinatorics 2013*, London Math. Soc. Lecture Note Series 409, Cambridge University Press, 2013, 127–160.
- **[Survey]** N. Nishimura. *Introduction to reconfiguration.* Algorithms 11 (2018), article 52.
- **[Survey]** N. Bousquet, A. Bonamy, M. Heinrich, M. Rabie et al. *Recolouring graphs: a survey.* (see Nishimura and van den Heuvel above for the standard entry points).

## 10. Worked Example / Concrete Special Case

**Claim.** The path $P_n = v_1v_2\cdots v_n$ is $1$-degenerate, $k = 3 = d+2$, and $\operatorname{diam}(\mathcal{C}_3(P_n)) \ge \lfloor n^2/4 \rfloor$. This shows the conjectured exponent $2$ cannot be lowered.

**Height encoding.** Identify colors with $\mathbb{Z}_3 = \{1,2,3\}$. For a proper coloring $c$ set, for $1 \le i \le n-1$,
$$s_i(c) = \begin{cases} +1 & \text{if } c(v_{i+1}) - c(v_i) \equiv 1 \pmod 3,\\ -1 & \text{if } c(v_{i+1}) - c(v_i) \equiv 2 \pmod 3.\end{cases}$$
Properness forces $s_i \in \{\pm 1\}$, and $c \mapsto (c(v_1), s_1,\dots,s_{n-1})$ is a bijection onto $\mathbb{Z}_3 \times \{\pm1\}^{n-1}$.

**Effect of one recoloring.** An internal vertex $v_j$ ($1<j<n$) can be recolored only when its neighbours share a color, i.e. $s_{j-1} = -s_j$; the move flips both $s_{j-1}$ and $s_j$. Recoloring $v_1$ flips $s_1$ only; recoloring $v_n$ flips $s_{n-1}$ only.

**Potential.** Put $w_i = \min(i,\,n-i)$ and
$$\Phi(c) = \sum_{i=1}^{n-1} w_i\, s_i(c).$$
- Internal move at $v_j$: $\Delta\Phi = -2w_{j-1}s_{j-1} - 2w_j s_j = 2 s_{j-1}(w_j - w_{j-1})$, and $|w_j - w_{j-1}| \le 1$, so $|\Delta\Phi| \le 2$.
- Move at $v_1$: $|\Delta\Phi| = 2w_1 = 2$. Move at $v_n$: $|\Delta\Phi| = 2w_{n-1} = 2$.

So **every** single-vertex recoloring changes $\Phi$ by at most $2$.

**Two extreme colorings.** Let $c^+ = (1,2,3,1,2,3,\dots)$, so $s_i \equiv +1$ and $\Phi(c^+) = \sum_i w_i$. Let $c^- = (1,3,2,1,3,2,\dots)$, so $s_i \equiv -1$ and $\Phi(c^-) = -\sum_i w_i$. Since $\sum_{i=1}^{n-1}\min(i,n-i) = \lfloor n^2/4\rfloor$,
$$\mathrm{d}_3(c^+,c^-) \ \ge\ \frac{|\Phi(c^+)-\Phi(c^-)|}{2} \ =\ \Bigl\lfloor \frac{n^2}{4}\Bigr\rfloor .$$

**Check, $n=3$.** $c^+=(1,2,3)$, $c^-=(1,3,2)$, $w_1=w_2=1$, bound $\ge 2$. Actual distance is $3$: from $(1,2,3)$ vertex $v_2$ is frozen (neighbours colored $1$ and $3$), so one must play $(1,2,3)\to(1,2,1)\to(1,3,1)\to(1,3,2)$.

**Interpretation.** The upper bound $\mathrm{d}_3 = O(n^2)$ for paths follows from the $k=3$ theorem of Cereceda–van den Heuvel–Johnson, so $\operatorname{diam}(\mathcal{C}_3(P_n)) = \Theta(n^2)$. Cereceda's conjecture asserts that this $d=1$ picture persists for every degeneracy: the quadratic barrier of the height function is the *only* obstruction, and no $d$-degenerate family with $k=d+2$ is worse than the humble path.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*