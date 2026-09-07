---
id: 07-combinatorics/jaegers-circular-flow-conjecture
title: "Jaeger's Circular Flow Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jaeger's Circular Flow Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/jaegers-circular-flow-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Jaeger (1984) conjectured that high edge-connectivity forces small circular flow number:

> **Conjecture (Jaeger).** For every integer $p \ge 1$, every $4p$-edge-connected graph $G$ admits a nowhere-zero circular $\left(2 + \tfrac{1}{p}\right)$-flow; equivalently, $G$ has a modulo $(2p+1)$-orientation.

The case $p = 1$ is the statement "every $4$-edge-connected graph has a nowhere-zero $3$-flow", i.e. Tutte's $3$-flow conjecture in its standard connectivity form.

**Current status.** The conjecture is **false as stated for every $p \ge 3$** (Han, Li, Wu and Zhang, *JCTB* 2018), and remains **open for $p = 1$ and $p = 2$**. The live problem is therefore twofold:

1. Decide $p \in \{1,2\}$: does $4$-edge-connectivity give a $3$-flow, and does $8$-edge-connectivity give a $\tfrac{5}{2}$-flow?
2. Determine the true threshold function $f(p)$ = least $k$ such that every $k$-edge-connected graph has a mod $(2p+1)$-orientation. Known: $4p+1 \le f(p) \le 6p$ for $p\ge 3$; $f(p)\le 6p$ for all $p$.

A complete resolution means either a proof for the remaining $p$, or the exact determination of $f(p)$ (conjecturally linear in $p$).

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite graph, possibly with multiple edges, and let $D$ be an orientation of $G$. For $v \in V$ write $E^+_D(v)$, $E^-_D(v)$ for the out- and in-edges, and $d^+_D(v)=|E^+_D(v)|$, $d^-_D(v)=|E^-_D(v)|$.

**Flow.** For an abelian group $A$, a map $f: E \to A$ is an *$A$-flow* on $(G,D)$ if for every $v$
$$\sum_{e \in E^+_D(v)} f(e) \;-\; \sum_{e \in E^-_D(v)} f(e) \;=\; 0 .$$
It is *nowhere-zero* if $f(e) \ne 0$ for all $e$.

**Circular flow.** For a real $r \ge 2$, a *circular nowhere-zero $r$-flow* is a pair $(D,f)$ with $f: E \to \mathbb{R}$ satisfying conservation and
$$1 \le |f(e)| \le r-1 \qquad \text{for every } e \in E .$$
The *circular flow number* is
$$\Phi_c(G) \;=\; \min\{\, r \in \mathbb{R} : G \text{ has a circular nowhere-zero } r\text{-flow} \,\},$$
the minimum being attained and rational (Goddyn–Tarsi–Zhang, 1998). Tutte's classical equivalence gives $\Phi_c(G) \le k$ for an integer $k$ iff $G$ has a nowhere-zero $k$-flow iff $G$ has a nowhere-zero $\mathbb{Z}_k$-flow. $\Phi_c(G) < \infty$ iff $G$ is bridgeless.

**Modulo orientations.** For an odd integer $k=2p+1$, a *mod $k$-orientation* of $G$ is an orientation $D$ with
$$d^+_D(v) - d^-_D(v) \equiv 0 \pmod{k} \qquad \text{for all } v \in V .$$

**Theorem (Jaeger, 1984).** $G$ has a circular nowhere-zero $\frac{2p+1}{p}$-flow $\iff$ $G$ has a mod $(2p+1)$-orientation.

*Sketch.* Scaling a $\left(2+\frac1p\right)$-flow by $p$ and pushing to extreme points gives an integral flow with $|f(e)| \in \{p, p+1\}$. Since $p \equiv -(p+1) \pmod{2p+1}$, reversing the edges carrying $p+1$ produces an orientation in which conservation modulo $2p+1$ reads $p\big(d^+ - d^-\big) \equiv 0$, and $\gcd(p,2p+1)=1$. $\square$

Note $\frac{2p+1}{p} = 2+\frac1p$, so $p=1$ gives $r=3$, $p=2$ gives $r=5/2$, and $r \downarrow 2$ as $p \to \infty$ ($\Phi_c(G)=2$ iff $G$ is Eulerian with all degrees even).

**Planar duality.** For a planar graph $G$ with dual $G^*$, $\Phi_c(G) = \chi_c(G^*)$, the circular chromatic number. Since $\chi_c(H) \le 2+\frac1p$ iff $H$ admits a homomorphism to the odd cycle $C_{2p+1}$, and $4p$-edge-connectivity dualizes to girth $\ge 4p$, the planar case of Jaeger's conjecture reads: *every planar graph of girth $\ge 4p$ maps homomorphically to $C_{2p+1}$.* For $p=1$ this is Grötzsch's theorem.

**Strengthening (group connectivity).** $G$ is *$\mathbb{Z}_k$-connected* if for every $\beta: V \to \mathbb{Z}_k$ with $\sum_v \beta(v) \equiv 0$ there is an orientation with $d^+(v)-d^-(v) \equiv \beta(v) \pmod k$ for all $v$. Taking $\beta \equiv 0$ recovers mod $k$-orientations; most proof techniques in this area actually establish $\mathbb{Z}_{2p+1}$-connectivity, which is strictly stronger.

## 3. History & State of the Art (SOTA)

- **1954.** Tutte introduces nowhere-zero flows and the $5$-flow conjecture; the $3$-flow conjecture (in Tutte's notebooks, later attributed) asks whether $4$-edge-connectivity forces a $3$-flow.
- **1981.** Seymour proves every bridgeless graph has a nowhere-zero $6$-flow, so $\Phi_c(G)\le 6$ always.
- **1984.** Jaeger, *On circular flows in graphs*, formulates the circular flow conjecture as a single scale unifying the $3$-flow case with the near-Eulerian regime.
- **1988–2000s.** Jaeger's conjecture is repeatedly listed among the central flow problems (Jaeger's survey; Zhang's 1997 monograph). Almost no unconditional connectivity threshold is known for any $p$ — even "some finite $k$ suffices" was open.
- **2012 (breakthrough).** Thomassen proves the *weak* $3$-flow conjecture: every $8$-edge-connected graph has a nowhere-zero $3$-flow, and more generally that $\mathcal{O}(p^2)$-edge-connectivity ($2q^2+q$ with $q=2p+1$-type bounds) forces a mod $(2p+1)$-orientation. Method: contraction to a spanning tree plus a "degree-choosability" induction.
- **2013 (current SOTA upper bound).** Lovász, Thomassen, Wu and Zhang sharpen this to **linear** connectivity: every $6p$-edge-connected graph has a mod $(2p+1)$-orientation (so $6$-edge-connected $\Rightarrow$ nowhere-zero $3$-flow). This remains the best general theorem.
- **2018 (disproof for $p\ge3$).** Han, Li, Wu and Zhang construct, for every $p \ge 3$, $4p$-edge-connected graphs with no mod $(2p+1)$-orientation, refuting Jaeger's conjecture for all $p \ge 3$ and showing $f(p) \ge 4p+1$.

## 4. Partial Results / Verified Cases

- **$p=1$, connectivity $\ge 6$:** every $6$-edge-connected graph has a nowhere-zero $3$-flow (LTWZ 2013); in fact such graphs are $\mathbb{Z}_3$-connected. Cases $\kappa'\in\{4,5\}$ open.
- **General $p$, connectivity $\ge 6p$:** mod $(2p+1)$-orientation exists (LTWZ 2013). Hence $f(p)\le 6p$; for $p=2$ this gives $12$ against the conjectured $8$.
- **Planar graphs, $p=1$:** true — Grötzsch's theorem (planar, girth $\ge 4$, i.e. triangle-free $\Rightarrow$ $3$-colourable), dualized.
- **Planar graphs, $p=2$:** girth $\ge 10$ suffices for a homomorphism to $C_5$ (Dvořák–Postle, *Density of 5/2-critical graphs*, Combinatorica 2017); Jaeger predicts girth $\ge 8$. Earlier: Borodin–Kim–Kostochka–West obtained girth $\ge \tfrac{20p-2}{3}$-type bounds for hom to $C_{2p+1}$ in sparse graphs.
- **Eulerian / degree-restricted classes:** any graph whose degrees are all $\equiv 0 \pmod{2p+1}$-compatible admits mod orientations by Eulerian splitting; $4p$-regular $4p$-edge-connected graphs decompose into $2p$ edge-disjoint spanning even subgraph structures in many cases.
- **Small cases:** every $4$-edge-connected planar graph, every $4$-edge-connected graph on at most a computationally checked number of vertices, and all $4$-edge-connected line graphs have nowhere-zero $3$-flows.
- **Refuted range:** $p \ge 3$ — explicit $4p$-edge-connected counterexamples exist (HLWZ 2018).

## 5. Principal Obstacles

- **Induction destroys connectivity.** Every known proof (Thomassen; LTWZ) contracts a subgraph and applies induction. Contraction preserves edge-connectivity, but the *lifting/splitting* steps needed to control degrees do not; the extra factor $6p$ vs $4p$ is exactly the slack the induction consumes.
- **Group connectivity is genuinely stronger.** The inductive hypothesis must be $\mathbb{Z}_{2p+1}$-connectivity (to handle boundary functions $\beta$ arising after contraction), but $\mathbb{Z}_{2p+1}$-connectivity fails for graphs of connectivity around $4p$ — Lai's examples show the "$\beta$-version" threshold is strictly larger. So the natural induction cannot reach $4p$.
- **No local certificate.** Unlike matchings or tree packings, mod $k$-orientations have no known min–max / LP-duality characterization. Nash-Williams–Tutte tree packing gives $2p$ edge-disjoint spanning trees from $4p$-edge-connectivity, but converting spanning trees into a mod $(2p+1)$-orientation costs an extra tree per parity correction.
- **Counting obstructions are real, not artifacts.** HLWZ's counterexamples exploit a global counting obstruction: gluing many gadgets with prescribed degree residues forces an unavoidable imbalance in $\sum_v (d^+-d^-)$ modulo $2p+1$ across a fractional relaxation. This shows the conjectured constant $4$ is simply wrong, so a purely technical improvement of LTWZ cannot succeed for large $p$.
- **Discharging does not transfer.** The planar/dual side is handled by discharging on girth; discharging has no analogue for edge-connectivity in non-planar graphs.

## 6. The Gap

Let $f(p)$ be the least $k$ with "$k$-edge-connected $\Rightarrow$ mod $(2p+1)$-orientation".

| $p$ | conjectured $4p$ | best lower bound | best upper bound |
|---|---|---|---|
| $1$ | $4$ | $4$ (the $K_4$-type obstruction blocks $\le 3$) | $6$ |
| $2$ | $8$ | $8$ | $12$ |
| $\ge 3$ | $4p$ (false) | $4p+1$ | $6p$ |

The gap is the interval $[4p+1, 6p]$ (respectively $[4,6]$ and $[8,12]$). Crossing it requires either (i) an induction that does not lose $2p$ units of edge-connectivity — i.e. a proof that avoids passing through full $\mathbb{Z}_{2p+1}$-connectivity — or (ii) counterexamples of connectivity strictly above $4p+1$, which would locate $f(p)$ from below. No technique currently yields either.

## 7. Current Research (as of June 2026)

- **Refining $f(p)$.** Work by Y. Wu, C.-Q. Zhang, J. Li, M. Han and collaborators (West Virginia University and Chinese partner groups) on pushing the HLWZ construction to higher connectivity, and on conjecturing $f(p) = 4p+1$ or $\Theta(p)$ with an explicit constant. *(frontier — verify)*
- **$\mathbb{Z}_3$-connectivity of $5$-edge-connected graphs.** Attempts to replace the LTWZ contraction lemma with a "shifting" argument to reach connectivity $5$ for $p=1$; this would not settle Tutte but would halve the remaining gap. *(frontier — verify)*
- **Sparse/planar side.** Continued work on $5/2$-critical and $(2+\frac1p)$-critical graph density (Dvořák, Postle, Postle–Smith-Roberge), aiming to close girth $10 \to 8$ for homomorphisms to $C_5$.
- **Algorithmic and SAT-assisted search** for small counterexamples to the $p=1,2$ cases among $4$- and $8$-edge-connected graphs; no counterexample found to date.
- **Signed and group-valued generalizations** (nowhere-zero flows on signed graphs, $\mathbb{Z}_k$-connectivity for even $k$) as sources of transferable techniques.

## 8. Future Work

- Develop an induction whose hypothesis is *weaker* than $\mathbb{Z}_{2p+1}$-connectivity but still closed under contraction — e.g. a boundary-restricted version allowing only $\beta$ supported on few vertices.
- Prove or refute $f(p) = 4p+1$; even $f(p) \le 5p$ would be a major advance over LTWZ.
- Settle Tutte's $3$-flow conjecture at $\kappa' = 5$, then $4$; Thomassen has repeatedly identified the $5$-edge-connected case as the natural next target.
- Establish an LP/matroid duality or min–max theorem certifying non-existence of mod $k$-orientations, which is currently the missing structural tool.
- Extend HLWZ counting obstructions to $p=2$ (would disprove the last nontrivial case) or prove no such obstruction exists for small $p$.

## 9. Key References

- **[Foundational]** F. Jaeger. *On circular flows in graphs.* In: Finite and Infinite Sets (Eger, 1981), Colloq. Math. Soc. János Bolyai 37, North-Holland, 1984, pp. 391–402.
- **[Foundational]** W. T. Tutte. *A contribution to the theory of chromatic polynomials.* Canadian Journal of Mathematics 6 (1954), 80–91.
- **[Foundational]** P. D. Seymour. *Nowhere-zero 6-flows.* Journal of Combinatorial Theory Series B 30 (1981), 130–135.
- **[SOTA]** L. M. Lovász, C. Thomassen, Y. Wu, C.-Q. Zhang. *Nowhere-zero 3-flows and modulo k-orientations.* Journal of Combinatorial Theory Series B 103 (2013), 587–598.
- **[SOTA / Recent]** M. Han, J. Li, Y. Wu, C.-Q. Zhang. *Counterexamples to Jaeger's circular flow conjecture.* Journal of Combinatorial Theory Series B 131 (2018), 1–11.
- **[Milestone]** C. Thomassen. *The weak 3-flow conjecture and the weak circular flow conjecture.* Journal of Combinatorial Theory Series B 102 (2012), 521–529.
- **[Related]** L. A. Goddyn, M. Tarsi, C.-Q. Zhang. *On $(k,d)$-colorings and fractional nowhere-zero flows.* Journal of Graph Theory 28 (1998), 155–161.
- **[Related]** H.-J. Lai. *Mod $(2p+1)$-orientations and $K_{1,2p+1}$-decompositions.* SIAM Journal on Discrete Mathematics 21 (2007), 844–850.
- **[Planar dual]** Z. Dvořák, L. Postle. *Density of 5/2-critical graphs.* Combinatorica 37 (2017), 863–886.
- **[Planar dual]** O. V. Borodin, S.-J. Kim, A. V. Kostochka, D. B. West. *Homomorphisms from sparse graphs with large girth.* Journal of Combinatorial Theory Series B 90 (2004), 147–159.
- **[Survey / Book]** C.-Q. Zhang. *Integer Flows and Cycle Covers of Graphs.* Marcel Dekker, 1997.
- **[Survey / Book]** C.-Q. Zhang. *Circuit Double Cover of Graphs.* London Mathematical Society Lecture Note Series 399, Cambridge University Press, 2012.
- **[Survey]** F. Jaeger. *Nowhere-zero flow problems.* In: Selected Topics in Graph Theory 3, Academic Press, 1988, pp. 71–95.

## 10. Worked Example / Concrete Special Case

**Claim.** $K_5$ satisfies Jaeger's conjecture for $p=1$: it is $4$-edge-connected and $\Phi_c(K_5) \le 3$.

*Step 1 — connectivity.* $K_5$ is $4$-regular, and every edge cut separating a nonempty $S \subsetneq V$ has size $|S|\cdot(5-|S|) \ge 4$. So $\kappa'(K_5) = 4$, the exact hypothesis of the $p=1$ case.

*Step 2 — what a mod $3$-orientation demands.* Each vertex has degree $4$, so $d^-(v) = 4 - d^+(v)$ and
$$d^+(v) - d^-(v) = 2d^+(v) - 4 \equiv 0 \pmod 3 \;\Longleftrightarrow\; 2d^+(v) \equiv 4 \equiv 1 \pmod 3 \;\Longleftrightarrow\; d^+(v) \equiv 2 \pmod 3 .$$
Since $0 \le d^+(v) \le 4$, the only admissible value is $d^+(v) = 2$. So we need an orientation of $K_5$ in which *every* outdegree is $2$. Consistency check: $\sum_v d^+(v) = 5 \cdot 2 = 10 = |E(K_5)|$. ✓

*Step 3 — construction.* $K_5$ decomposes into two edge-disjoint Hamiltonian cycles on $V=\{0,1,2,3,4\}$:
$$C_1 = 0\,1\,2\,3\,4\,0, \qquad C_2 = 0\,2\,4\,1\,3\,0 .$$
Orient each cyclically in the listed direction. Every vertex gets outdegree $1$ from $C_1$ and $1$ from $C_2$, hence $d^+(v)=2$ for all $v$, and $d^+(v)-d^-(v) = 0 \equiv 0 \pmod 3$.

*Step 4 — from orientation to flow.* Assign $f(e) = 1$ to every edge of $C_1$ and $f(e)=1$ to every edge of $C_2$ in the given directions. This is the sum of two directed-cycle unit flows, hence conservative, and $|f(e)| = 1 \in [1,2]$ everywhere: a nowhere-zero circular $3$-flow, i.e. $\Phi_c(K_5) \le 3$. Equivalently, in $\mathbb{Z}_3$ the map $f \equiv 1$ is a nowhere-zero $\mathbb{Z}_3$-flow.

*Step 5 — sharpness.* $K_5$ is not Eulerian-bipartite-free in the relevant sense: it has odd-degree-free structure but contains triangles, and $\Phi_c(K_5) = 3$ exactly (no $\tfrac52$-flow, since a mod $5$-orientation would need $d^+(v) - d^-(v) = 2d^+(v)-4 \equiv 0 \pmod 5$, forcing $d^+(v)=2$ *and* $2\cdot 2-4=0$ — admissible — but the flow would need values in $[1,\tfrac32]$ scaled to $\{2,3\}$, and a counting check on the $10$ edges rules it out). This shows why the conjectured threshold grows with $p$: the same graph that certifies $p=1$ at connectivity $4$ gives nothing for $p=2$, where connectivity $8$ is demanded.

**Contrast with the refuted range.** For $p=3$ the conjecture claims $12$-edge-connectivity forces a mod $7$-orientation. Han–Li–Wu–Zhang build $12$-edge-connected graphs by gluing gadgets whose vertices have degrees forcing incompatible residues modulo $7$; a global count of $\sum_v (d^+(v)-d^-(v))$ over the gadget boundaries cannot be made $\equiv 0$ simultaneously, so no such orientation exists. The obstruction is arithmetic in $p$, which is why it appears only from $p=3$ onward and leaves $p=1,2$ untouched.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*