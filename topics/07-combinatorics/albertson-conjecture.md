---
id: 07-combinatorics/albertson-conjecture
title: "Albertson Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Albertson Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/albertson-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Albertson, 2007).** For every integer $r \ge 1$ and every simple graph $G$ with chromatic number $\chi(G) = r$,
$$\operatorname{cr}(G) \;\ge\; \operatorname{cr}(K_r),$$
where $\operatorname{cr}(\cdot)$ denotes the crossing number.

Informally: among all graphs needing $r$ colours, the complete graph $K_r$ is the one that can be drawn in the plane with the fewest crossings. The bound is tight, witnessed by $G = K_r$.

A complete proof must establish the inequality for **all** $r$ and all $r$-chromatic graphs, including those with many more than $r$ vertices. A disproof requires an explicit $r$ and a graph $G$ with $\chi(G) \ge r$ and $\operatorname{cr}(G) < \operatorname{cr}(K_r)$. Note that the statement refers to the *true* value $\operatorname{cr}(K_r)$, which is itself unknown for $r \ge 13$; the conjecture is therefore not contingent on Hill's conjecture, though the two interact (Section 6).

The case $r = 5$ is equivalent to the Four Colour Theorem: $\operatorname{cr}(K_5) = 1$, so the claim "$\chi(G) = 5 \Rightarrow \operatorname{cr}(G) \ge 1$" says exactly that planar graphs are $4$-colourable. Hence any proof of the general conjecture implies the 4CT, which sets a floor on how easy a solution can be.

## 2. Mathematical Foundations

**Drawings and crossing number.** A *drawing* $D$ of a graph $G=(V,E)$ maps vertices to distinct points of $\mathbb{R}^2$ and edges to simple arcs joining their endpoints, with no arc passing through a vertex, no two arcs sharing more than finitely many points, no tangential contacts, and no three arcs through a common point. A *crossing* is a transversal intersection of two arcs at an interior point. Write $\operatorname{cr}(D)$ for the number of crossings and
$$\operatorname{cr}(G) \;=\; \min_{D} \operatorname{cr}(D).$$
An optimal drawing may always be taken *good*: adjacent edges do not cross and no two edges cross twice.

**Chromatic number and criticality.** $\chi(G)$ is the least $k$ with a proper $k$-colouring $c : V \to [k]$. $G$ is *$r$-critical* if $\chi(G) = r$ and $\chi(G - e) < r$ for all $e \in E$. Every $r$-chromatic graph contains an $r$-critical subgraph $H$, and $\operatorname{cr}(G) \ge \operatorname{cr}(H)$ since crossing number is minor-monotone under subgraphs. So one may assume $G$ is $r$-critical, whence
$$\delta(G) \ge r-1, \qquad n = |V| \ge r, \qquad m = |E| \ge \tfrac{(r-1)n}{2}.$$

**Euler bound.** For a simple graph with $n \ge 3$: $\operatorname{cr}(G) \ge m - 3n + 6$.

**Crossing Lemma** (Ajtai–Chvátal–Newborn–Szemerédi 1982; Leighton 1983; constant improved by Pach–Radoičić–Tardos–Tóth and Ackerman): for $m \ge 7n$,
$$\operatorname{cr}(G) \;\ge\; \frac{m^{3}}{29 n^{2}}.$$
Also useful in the sparse regime: $\operatorname{cr}(G) \ge \frac{7}{3}m - \frac{25}{3}(n-2)$ (PRTT 2006) and $\operatorname{cr}(G)\ge 5m - \frac{139}{6}(n-2)$ (Ackerman 2019).

**Crossing numbers of complete graphs.** Hill's construction gives
$$Z(r) \;=\; \frac{1}{4}\Big\lfloor \tfrac r2\Big\rfloor \Big\lfloor \tfrac{r-1}{2}\Big\rfloor \Big\lfloor \tfrac{r-2}{2}\Big\rfloor \Big\lfloor \tfrac{r-3}{2}\Big\rfloor \;\sim\; \frac{r^{4}}{64},$$
and $\operatorname{cr}(K_r) \le Z(r)$; **Hill's conjecture** asserts equality. Guy's counting recursion, obtained by summing over the $r$ copies of $K_{r-1}$ and noting each crossing survives in $r-4$ of them, gives
$$\operatorname{cr}(K_r) \;\ge\; \frac{r}{r-4}\,\operatorname{cr}(K_{r-1}).$$

Small values: $\operatorname{cr}(K_5)=1$, $\operatorname{cr}(K_6)=3$, $\operatorname{cr}(K_7)=9$, $\operatorname{cr}(K_8)=18$, $\operatorname{cr}(K_9)=36$, $\operatorname{cr}(K_{10})=60$, $\operatorname{cr}(K_{11})=100$, $\operatorname{cr}(K_{12})=150$.

## 3. History & State of the Art (SOTA)

Michael O. Albertson stated the conjecture in *Chromatic number, independence ratio, and crossing number* (Ars Mathematica Contemporanea, 2008), as part of a programme relating colouring to non-planarity measures; the conjecture circulated from 2007. It generalises the 4CT in the same spirit as the Hajós and Hadwiger conjectures generalise it via minors/topological minors — but with a *metric* rather than structural hypothesis.

Milestones:

| Year | Authors | Result |
|---|---|---|
| 1977 | Appel–Haken | $r \le 5$ (4CT) |
| 2009 | Oporowski–Zhao | $r = 6, 7$ |
| 2009 | Albertson–Cranston–Fox | $r \le 12$; minimum counterexample has $n < 4r$ vertices |
| 2010 | Barát–Tóth | $r \le 16$; minimum counterexample has $n < 3.57r$ vertices |
| 2019 | Ackerman | $r \le 18$, via an improved crossing lemma for graphs with $\le 4$ crossings per edge |

The record $r \le 18$ has stood since 2019. No asymptotic version — e.g. $\operatorname{cr}(G) \ge (1-o(1))\operatorname{cr}(K_{\chi(G)})$ — is known; the best general bound is off by a constant factor near $3.6$ (Section 6).

## 4. Partial Results / Verified Cases

- **All $r \le 18$** (Ackerman 2019), building on Barát–Tóth ($r \le 16$), Albertson–Cranston–Fox ($r \le 12$), Oporowski–Zhao ($r = 6,7$), and 4CT ($r \le 5$).
- **Bounded counterexample size.** If the conjecture fails for some $r$, a minimum counterexample is $r$-critical with $n < 3.57r$ vertices (Barát–Tóth 2010; ACF 2009 had $n < 4r$). So for each fixed $r$ the conjecture is a *finite* check — but on a class of size superexponential in $r$.
- **Graphs with $n = r$.** Immediate: an $r$-chromatic graph on $r$ vertices is $K_r$.
- **Order-$4$ growth.** For $r$-critical $G$ with $m \ge \tfrac{(r-1)n}{2}$ and $n \ge r$, the Crossing Lemma yields
$$\operatorname{cr}(G) \ge \frac{1}{29 n^{2}}\Big(\frac{(r-1)n}{2}\Big)^{3} = \frac{(r-1)^{3} n}{232} \ge \frac{(r-1)^{3} r}{232} \sim \frac{r^{4}}{232},$$
i.e. at least $\approx 0.276\,Z(r)$ asymptotically. This is the shape of every known general bound.
- **Dense-degree regimes.** If $G$ has $n$ vertices and minimum degree $\ge r-1$ with $n$ substantially larger than $r$ (say $n \ge Cr$ for a suitable absolute $C$), the Crossing Lemma bound $\tfrac{(r-1)^3 n}{232}$ already exceeds $Z(r)$; the conjecture is only open in the narrow band $r \le n < 3.57r$.
- **Related complete-graph data.** $\operatorname{cr}(K_r)=Z(r)$ is verified for $r \le 12$ (Pan–Richter, $K_{11}$ and hence $K_{12}$, 2007), and $\operatorname{cr}(K_n) \ge 0.985\,Z(n)$ for all $n$ (Balogh–Lidický–Salazar 2019, flag algebras).

## 5. Principal Obstacles

- **The conjecture implies the 4CT.** Any purely "soft" counting proof would give a counting proof of the Four Colour Theorem, which is not expected to exist. All proofs for $r \le 18$ therefore *assume* 4CT as an input and bootstrap upward.
- **Counting bounds lose a constant factor.** The Crossing Lemma is tight up to a constant for random-like graphs; feeding in only $\delta \ge r-1$ gives $\asymp r^4/232$ against a target $\asymp r^4/64$. Improving the crossing-lemma constant from $1/29$ to $1/64$ is impossible — the true optimal constant is known to be at most $\approx 1/29$ from explicit examples — so *no* bound of the form $\operatorname{cr}(G) \ge c\,m^3/n^2$ applied to degree information alone can close the gap.
- **Criticality is weakly exploited.** Beyond $\delta \ge r-1$, structural theory of $r$-critical graphs (Gallai trees in the low-degree subgraph, Kostochka–Yancey-type edge bounds) has not been coupled to drawings. Kostochka–Yancey gives $m \ge \frac{(r+1)(r-2)n - r(r-3)}{2(r-1)}$, only a lower-order improvement on $\frac{(r-1)n}{2}$.
- **Crossing number is not minor-monotone and is NP-hard.** Contraction can *increase* crossings, so minor-based colouring machinery (Hadwiger-style, structure theorems) does not transfer. Computing $\operatorname{cr}(G)$ is NP-hard (Garey–Johnson 1983), blocking exhaustive verification even in the band $n < 3.57r$.
- **$\operatorname{cr}(K_r)$ itself is unknown.** For $r \ge 13$ the right-hand side is not a computable closed form, so any inductive scheme must carry inequalities on both sides simultaneously.

## 6. The Gap

Proven: $r \le 18$ exactly, plus $\operatorname{cr}(G) \gtrsim r^4/232$ in general. Needed: $\operatorname{cr}(G) \ge \operatorname{cr}(K_r) \approx r^4/64$.

The precise deficit is a multiplicative factor of about $232/64 \approx 3.6$ in the asymptotic constant, and, for each fixed $r \ge 19$, the finite band of $r$-critical graphs with
$$r \;<\; n \;<\; 3.57\,r .$$
Closing it requires an argument that extracts crossings from *colouring* structure rather than from edge density — the Crossing Lemma provably cannot supply the missing factor. A natural intermediate target, still open: prove $\operatorname{cr}(G) \ge (1-\varepsilon)Z(\chi(G))$ for some $\varepsilon < 1/2$ and all large $r$.

## 7. Current Research (as of June 2026)

- **Flag-algebra / semidefinite bounds on $\operatorname{cr}(K_n)$.** The Balogh–Lidický–Salazar line ($\operatorname{cr}(K_n)\ge 0.985\,Z(n)$) and its bipartite analogues continue at Illinois, Iowa State and UASLP. These tighten the *right-hand* side but do not attack $r$-chromatic $G$ directly.
- **Improved crossing lemmas for restricted crossing patterns.** Ackerman's method — bounding $\operatorname{cr}$ for graphs drawn with at most $k$ crossings per edge — is the mechanism that pushed $16 \to 18$; extending it to $k = 5, 6$ is the most plausible route to $r \le 20$ or so. *(frontier — verify: no published extension past $k=4$ has yielded a new $r$ as of mid-2026.)*
- **Critical-graph structure meets topology.** Combining Kostochka–Yancey edge bounds for $r$-critical graphs with discharging on the planarization of an optimal drawing is under exploration in the Central European (Barát, Tóth, Rényi Institute) and North American (Cranston, VCU) discrete-geometry communities.
- **Variants.** Analogues for the rectilinear crossing number $\overline{\operatorname{cr}}$, the pair crossing number, and the odd crossing number are studied; since $\overline{\operatorname{cr}} \ge \operatorname{cr}$, the rectilinear Albertson statement is *weaker* than the original and also open in general.
- **Computational search.** No counterexample has emerged from searches over small critical graphs; the NP-hardness of $\operatorname{cr}$ limits these to $n \lesssim 20$.

## 8. Future Work

1. **Push the crossing-lemma constant conditionally.** For $r$-critical graphs, prove a bound $\operatorname{cr}(G) \ge c\,m^3/n^2$ with $c$ larger than the universal constant, using the fact that critical graphs have no small separators of low degree.
2. **Colour-classes-as-crossings.** Albertson's own suggestion: extract a $K_r$-like "colour skeleton" (one vertex per colour class, contracted or represented by a connected subgraph) and transfer crossings from $G$ to it. The obstruction is that contraction can lower the crossing number.
3. **Prove the asymptotic form first.** Establishing $\operatorname{cr}(G) \ge (1-o(1))Z(r)$ would be a decisive qualitative advance even without exactness.
4. **Attack the band $r < n < 3.57r$ structurally**, reducing the counterexample bound to $n < (1+\varepsilon)r$, which would essentially force $G = K_r$.
5. **Independence-ratio route.** Albertson's companion results relate $\operatorname{cr}(G)$ to $\alpha(G)/n$; sharpening those could give colouring bounds by fractional relaxation.

## 9. Key References

- **[Foundational]** M. O. Albertson. *Chromatic number, independence ratio, and crossing number.* Ars Mathematica Contemporanea, 1(1):1–6, 2008.
- **[Foundational]** R. K. Guy. *Crossing numbers of graphs.* In *Graph Theory and Applications*, Lecture Notes in Mathematics 303, Springer, 1972, pp. 111–124.
- **[Foundational]** K. Appel and W. Haken. *Every planar map is four colorable.* Contemporary Mathematics 98, American Mathematical Society, 1989.
- **[Partial result]** B. Oporowski and D. Zhao. *Coloring graphs with crossings.* Discrete Mathematics, 309(9):2948–2951, 2009.
- **[Partial result]** M. O. Albertson, D. W. Cranston, and J. Fox. *Crossings, colorings, and cliques.* Electronic Journal of Combinatorics, 16(1):#R45, 2009.
- **[SOTA]** J. Barát and G. Tóth. *Towards the Albertson conjecture.* Electronic Journal of Combinatorics, 17(1):#R73, 2010.
- **[SOTA]** E. Ackerman. *On topological graphs with at most four crossings per edge.* Computational Geometry: Theory and Applications, 85:101574, 2019.
- **[SOTA]** J. Balogh, B. Lidický, and G. Salazar. *Closing in on Hill's conjecture.* SIAM Journal on Discrete Mathematics, 33(3):1261–1276, 2019.
- **[Technique]** J. Pach, R. Radoičić, G. Tardos, and G. Tóth. *Improving the crossing lemma by finding more crossings in sparse graphs.* Discrete & Computational Geometry, 36(4):527–552, 2006.
- **[Technique]** S. Pan and R. B. Richter. *The crossing number of $K_{11}$ is 100.* Journal of Graph Theory, 56(2):128–134, 2007.
- **[Technique]** A. V. Kostochka and M. Yancey. *Ore's conjecture on color-critical graphs is almost true.* Journal of Combinatorial Theory Series B, 109:73–101, 2014.
- **[Hardness]** M. R. Garey and D. S. Johnson. *Crossing number is NP-complete.* SIAM Journal on Algebraic and Discrete Methods, 4(3):312–316, 1983.
- **[Survey]** M. Schaefer. *The graph crossing number and its variants: a survey.* Electronic Journal of Combinatorics, Dynamic Survey DS21, 2013 (updated).
- **[Survey]** L. A. Székely. *A successful concept for measuring non-planarity of graphs: the crossing number.* Discrete Mathematics, 276(1–3):331–352, 2004.

## 10. Worked Example / Concrete Special Case

**Case $r = 6$, restricted to $n = 6$ vertices.**

Let $\chi(G) = 6$ with $|V(G)| = 6$. Each colour class is a single vertex, so all $\binom{6}{2}=15$ pairs are adjacent and $G = K_6$. We verify $\operatorname{cr}(K_6) = 3$, matching $Z(6) = \tfrac14\cdot 3\cdot 2\cdot 2\cdot 1 = 3$.

*Lower bound.* With $n = 6$, $m = 15$, the Euler bound gives
$$\operatorname{cr}(K_6) \;\ge\; m - 3n + 6 \;=\; 15 - 18 + 6 \;=\; 3.$$
*Upper bound.* Hill's cylindrical drawing places three vertices on an inner circle, three on an outer circle, and realises exactly $3$ crossings. Hence $\operatorname{cr}(K_6) = 3$. ∎

**Why the general $r = 6$ case is harder.** Suppose $\chi(G) = 6$ with $n > 6$ and $\operatorname{cr}(G) \le 2$. Fix a drawing with $\le 2$ crossings and delete one edge from each crossing pair, giving $F$ with $|F| \le 2$ and $G - F$ planar, hence $4$-colourable by 4CT. Recolouring one endpoint of each edge of $F$ with a fresh colour yields $\chi(G) \le 6$ — no contradiction. The naive argument gives only $\chi(G) \le 4 + 2\operatorname{cr}(G)$, which is two colours short. Oporowski and Zhao (2009) closed this by analysing the structure of $6$-critical graphs near the crossing edges (minimum degree $\ge 5$ forces the deleted edges' endpoints to have many neighbours in the planar part, restricting the available colours), and the same two-colour deficit is the model for every later case.

**Where the counting bound fails, $r = 7$.** A $7$-critical $G$ has $\delta \ge 6$, so $m \ge 3n$. The Euler bound gives $\operatorname{cr}(G) \ge 3n - 3n + 6 = 6$, and the PRTT bound gives $\tfrac73(3n) - \tfrac{25}{3}(n-2) = \tfrac{25}{3}\cdot 2 = 16\tfrac23$ only for large $n$; at $n = 7$ it yields $49 - \tfrac{125}{3} \approx 7.3$, so $\operatorname{cr}(G) \ge 8$. The target is $\operatorname{cr}(K_7) = 9$. Guy's recursion supplies the last step for $K_7$ itself: $\operatorname{cr}(K_7) \ge \tfrac{7}{3}\operatorname{cr}(K_6) = 7$, refined by case analysis to $9$. The residual gap of $1$ at $r=7$ is the same gap that, amplified, becomes the factor $3.6$ for large $r$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*