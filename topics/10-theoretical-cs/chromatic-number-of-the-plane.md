---
id: 10-theoretical-cs/chromatic-number-of-the-plane
title: "Chromatic Number of the Plane"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chromatic Number of the Plane (Hadwiger–Nelson Problem)

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/chromatic-number-of-the-plane` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Colour every point of the Euclidean plane so that no two points at distance exactly $1$ receive the same colour. What is the minimum number of colours needed?

Formally, let $G(\mathbb{R}^2)$ be the *unit-distance graph* with vertex set $\mathbb{R}^2$ and edge set $\{\{x,y\} : \|x-y\|_2 = 1\}$. The **chromatic number of the plane** is $\chi = \chi(G(\mathbb{R}^2))$. Known:
$$5 \le \chi(\mathbb{R}^2) \le 7 .$$
A complete solution is either (a) an explicit finite unit-distance graph with chromatic number $6$ or $7$ together with a proof of its chromatic number, plus a matching colouring, or (b) an explicit proper $6$-colouring (resp. $5$-colouring) of $\mathbb{R}^2$ avoiding distance $1$. No topological, measurability, or constructibility restriction is imposed on the colour classes; that omission is essential (Section 5).

## 2. Mathematical Foundations

**Unit-distance graphs.** For $S \subseteq \mathbb{R}^n$, $G(S)$ has vertex set $S$ and $x \sim y$ iff $\|x-y\| = 1$. A proper $k$-colouring is $c : S \to \{1,\dots,k\}$ with $c(x) \neq c(y)$ whenever $x \sim y$; equivalently a partition $\mathbb{R}^2 = A_1 \sqcup \cdots \sqcup A_k$ where each $A_i$ *avoids distance 1*: $\|x-y\| \ne 1$ for all $x,y \in A_i$.

**Compactness.** By the De Bruijn–Erdős theorem (1951), for a graph whose finite subgraphs are all $k$-colourable, the whole graph is $k$-colourable — assuming the axiom of choice (the ultrafilter lemma suffices). Hence
$$\chi(\mathbb{R}^2) = \sup \{ \chi(G) : G \subseteq G(\mathbb{R}^2),\ G \text{ finite} \},$$
so lower bounds are witnessed by *finite* graphs. This is what makes the problem SAT-solver-tractable.

**Measurable and fractional relaxations.** The *measurable chromatic number* $\chi_m(\mathbb{R}^2)$ restricts each $A_i$ to be Lebesgue measurable. The *independence density* is
$$m_1(\mathbb{R}^2) = \sup \Big\{ \limsup_{R\to\infty} \frac{\lambda(A \cap B_R)}{\lambda(B_R)} : A \text{ measurable, avoids distance } 1 \Big\},$$
giving $\chi_m \ge 1/m_1$. The *fractional chromatic number* $\chi_f$ satisfies $\chi_f \le \chi$ and, by a Lovász-type averaging argument, $\chi_f(\mathbb{R}^2) \le 1/m_1(\mathbb{R}^2)$.

**Spectral bound.** For the unit-distance graph, harmonic analysis on $\mathbb{R}^2$ gives the Fourier-analytic obstruction: if $A$ avoids distance $1$ then $\widehat{1_A} \star \widehat{1_A}$ must vanish against the measure $\sigma$ on the unit circle, whose Fourier transform is $\hat\sigma(\xi) = J_0(2\pi\|\xi\|)$. Since $\min_{t} J_0(t) \approx -0.4028$, the naive "$1 - 1/\min \hat\sigma$" Hoffman-type bound yields only $\chi_m \ge 1 + 1/0.4028 \approx 3.48$, i.e. $\chi_m \ge 4$ — weaker than combinatorial arguments.

**Key finite gadget.** A unit equilateral triangle forces three distinct colours; the *unit rhombus* (two unit triangles glued along an edge) has its two apexes at distance $\sqrt{3}$, and under any $3$-colouring they must share a colour. Chaining rhombi is the engine behind every known lower bound.

## 3. History & State of the Art (SOTA)

- **1945.** Hadwiger proves that any cover of $\mathbb{R}^n$ by $n+1$ closed sets has one realizing all distances; the general covering framework begins.
- **1950.** Edward Nelson poses the question ($\chi \ge 4$); John Isbell supplies $\chi \le 7$ almost immediately via a hexagonal tiling. The problem circulates through Erdős, Gardner (*Scientific American*, 1960) and Hadwiger's 1961 "Ungelöste Probleme" column. Attribution history is documented exhaustively by Soifer.
- **1961–2017.** The bounds $4 \le \chi \le 7$ stand unchanged for 57 years. Progress goes sideways: Falconer's measurable bound (1981), Woodall/Townsend results for regions bounded by Jordan curves, the Frankl–Wilson exponential bounds in high dimension, the Shelah–Soifer set-theoretic sensitivity results, and Cranston–Rabern's fractional lower bound $\chi_f \ge 3.8992$ (2017).
- **April 2018.** Aubrey de Grey exhibits a $1581$-vertex, $7877$-edge unit-distance graph with chromatic number $5$, verified by SAT, proving $\chi \ge 5$.
- **2018–2019.** Polymath16 forms within days. Marijn Heule shrinks the witness to $874$, then $633$, then $610$, then $553$, and finally to graphs with $510$ and $509$ vertices via clausal-proof trimming; Exoo–Ismailescu independently give a $517$-vertex graph by a different, human-checkable construction.
- **2022–2025.** Ambrus, Csiszárik, Matolcsi, Varga and Zsámboki push the density bound to $m_1(\mathbb{R}^2) < 0.2470$ by a large-scale LP/fractional-relaxation computation, re-deriving $\chi_m \ge 5$ with room to spare.

Current SOTA: $\chi \in \{5,6,7\}$; $\chi_m \in \{5,6,7\}$; $\chi_f \in [3.8992,\, 4.36]$.

## 4. Partial Results / Verified Cases

- **Upper bound $\chi \le 7$** (Isbell, 1950): regular hexagonal tiling, side $s$ with $1/\sqrt{7} < s < 1/2$, coloured by the standard $7$-cycle pattern.
- **Lower bound $\chi \ge 5$** (de Grey 2018; Exoo–Ismailescu 2020): finite $5$-chromatic unit-distance graphs; smallest published witnesses have $509$–$510$ vertices (Heule, Polymath16). All are verified by DRAT proofs machine-checked independently of the solver.
- **Measurable colourings:** $\chi_m(\mathbb{R}^2) \ge 5$ (Falconer 1981), reproved and strengthened quantitatively by the density bound $m_1 < 0.2470$ (Ambrus et al.).
- **"Nice" colour classes:** if the classes are unions of regions bounded by Jordan curves (or are polygonal/tile-like), at least $6$ colours are needed (Woodall 1973; Townsend, Coulson).
- **Rational and algebraic subspaces:** $\chi(\mathbb{Q}^2) = \chi(\mathbb{Q}^3) = 2$, $\chi(\mathbb{Q}^4) = 4$ (Benda–Perles). $\chi$ of the plane over $\mathbb{Q}(\sqrt{3})$-type lattices is likewise finite and computable.
- **Higher dimensions:** $6 \le \chi(\mathbb{R}^3) \le 15$ (Nechushtan 2002; Coulson 2002); $\chi(\mathbb{R}^4) \ge 9$ (Exoo–Ismailescu 2014). Asymptotically $(1.239\ldots + o(1))^n \le \chi(\mathbb{R}^n) \le (3+o(1))^n$ (Frankl–Wilson 1981, Raigorodskii 2000; Larman–Rogers 1972).
- **Fractional:** $\chi_f(\mathbb{R}^2) \ge 3.8992$ (Cranston–Rabern 2017).

## 5. Principal Obstacles

- **The upper bound has no lower-bound counterpart in method.** Every known $7$-colouring is a periodic tiling. Proving $\chi \le 6$ requires a colouring; a *periodic* $6$-colouring has been ruled out for wide classes of tile shapes, and no non-periodic construction technique exists. If $\chi = 6$ the colouring may be forced to be non-measurable, in which case *no explicit construction can exist* — one would need a choice-theoretic existence proof, a mode of argument absent from the literature.
- **Set-theoretic instability.** Shelah–Soifer (2003) exhibit distance graphs on $\mathbb{R}$ whose chromatic number is $2$ under AC but uncountable in a Solovay model where all sets are measurable. It remains conceivable — though not proven — that $\chi(\mathbb{R}^2)$ itself is not decided by ZF alone. Techniques that implicitly assume regularity of the colour classes therefore cannot settle the unrestricted question.
- **Fourier analysis is too weak.** The relevant spectral quantity is $\min_t J_0(t) \approx -0.4028$, giving only $\chi_m \ge 4$; the circle's Fourier transform decays like $\|\xi\|^{-1/2}$, so no single-frequency obstruction can reach $6$. Multi-frequency / Lasserre hierarchies at feasible degree currently plateau near $\chi_m \ge 5$.
- **Combinatorial search explodes.** Lower bounds via SAT need a $6$-chromatic unit-distance graph. Polymath16 estimates and subsequent searches suggest such a graph, if it exists, needs on the order of $10^4$–$10^6$ vertices; colourability checking is NP-hard and the vertex sets live in a dense subfield of $\mathbb{R}$, so the search space is not finitely generated in any convenient way. Ring-restricted searches (Eisenstein-like lattices, $\mathbb{Z}[\omega, \sqrt{3}]$) that produced the $5$-chromatic graphs have been exhausted at accessible sizes without a $6$-chromatic example.
- **No structural theory of unit-distance graphs.** They have unbounded chromatic number in $\mathbb{R}^n$ but bounded density; there is no analogue of minor-closed structure, no forbidden-subgraph characterization, and the standard chromatic tools (Hadwiger-type minors, Kneser/topological bounds, degeneracy) all give bounds far below $5$.

## 6. The Gap

Proven: a finite $5$-chromatic unit-distance graph exists (509 vertices), so $\chi \ge 5$; and a periodic $7$-colouring exists, so $\chi \le 7$. The unresolved statement is the pair of complementary questions:

1. **Does a $6$-chromatic unit-distance graph exist in $\mathbb{R}^2$?** Equivalently, is there a finite $V \subseteq \mathbb{R}^2$ with $\chi(G(V)) \ge 6$? A "yes" needs one explicit graph plus a UNSAT certificate; a "no" needs a proper $5$-colouring of the plane, currently believed impossible on density grounds ($1/m_1 > 4.04$ only rules out $\le 4$).
2. **If no $6$-chromatic graph exists, exhibit a proper $6$-colouring** of $\mathbb{R}^2$ avoiding distance $1$. The barrier is that all natural constructions (tilings by convex tiles of diameter $<1$) provably need $7$ pieces per period cell for the known parameter ranges, so a $6$-colouring must be non-convex, aperiodic, or non-measurable.

The single crossing step: extend the rhombus-chaining/SAT method from forcing $5$ colours on $509$ points to forcing $6$, or prove an upper-bound theorem certifying $6$-colourability of every finite unit-distance graph.

## 7. Current Research (as of June 2026)

- **Polymath16 legacy searches.** Continued SAT/CDCL searches over vertex sets in $\mathbb{Z}[\omega]$-type rings for $6$-chromatic graphs, with symmetry breaking and clausal-proof trimming (Heule, CMU). No $6$-chromatic example found; negative results now cover large restricted families. *(frontier — verify)*
- **Density and LP hierarchies.** The Ambrus–Csiszárik–Matolcsi–Varga–Zsámboki program pushes $m_1(\mathbb{R}^2)$ downward using large fractional-relaxation LPs on finite point configurations; a bound $m_1 < 1/5$ would give $\chi_m \ge 6$ and is the most concrete near-term target. Groups at Rényi Institute (Budapest) and Bordeaux (Bachoc, Pêcher, Moustrou) lead here.
- **Fractional chromatic number.** Improving $\chi_f \ge 3.8992$ toward $4$ and beyond (Cranston, Rabern and successors); $\chi_f > 4$ would not immediately settle $\chi$ but would refute large classes of proposed $5$-colourings.
- **Set-theoretic angle.** Study of which distance-graph chromatic numbers are ZF-absolute, following Shelah–Soifer and Payne; relevant to whether the problem is answerable by construction at all.
- **Structural results on unit-distance graphs**, including edge-count bounds (Erdős unit-distance problem) and girth/chromatic trade-offs, as indirect constraints on the size of any $6$-chromatic witness.

## 8. Future Work

- Push the LP/semidefinite hierarchy for $m_1(\mathbb{R}^2)$ below $1/5$ to obtain $\chi_m \ge 6$; then attack the gap between $\chi_m$ and $\chi$.
- Search for $6$-chromatic graphs in rings beyond $\mathbb{Z}[\omega,\sqrt{3}]$ — Soifer and de Grey both suggest the right algebraic number field is the missing ingredient.
- Develop *upper*-bound machinery: a theorem that every finite unit-distance graph is $6$-colourable, perhaps via a discharging or degeneracy argument tailored to planar unit-distance structure.
- Settle the analogous question for $\mathbb{R}^3$, where the gap $6 \le \chi \le 15$ is wider and where better lower-bound gadgets may transfer down to the plane.
- Determine whether a $6$-colouring, if it exists, can be taken measurable — a positive answer collapses the problem to a computable search.

## 9. Key References

- **[Foundational]** H. Hadwiger. *Überdeckung des euklidischen Raumes durch kongruente Mengen.* Portugaliae Mathematica 4, 1945, 238–242.
- **[Foundational]** N. G. de Bruijn, P. Erdős. *A colour problem for infinite graphs and a problem in the theory of relations.* Indagationes Mathematicae 13, 1951, 369–373.
- **[Foundational]** D. R. Woodall. *Distances realized by sets covering the plane.* Journal of Combinatorial Theory Series A 14, 1973, 187–200.
- **[Foundational]** K. J. Falconer. *The realization of distances in measurable subsets covering $\mathbb{R}^n$.* Journal of Combinatorial Theory Series A 31, 1981, 184–189.
- **[Foundational]** P. Frankl, R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1, 1981, 357–368.
- **[SOTA / Recent]** A. D. N. J. de Grey. *The chromatic number of the plane is at least 5.* Geombinatorics 28(1), 2018, 18–31.
- **[SOTA / Recent]** M. J. H. Heule. *Computing small unit-distance graphs with chromatic number 5.* Geombinatorics 28(1), 2018, 32–50.
- **[SOTA / Recent]** M. J. H. Heule. *Trimming graphs using clausal proof optimization.* Principles and Practice of Constraint Programming (CP 2019), LNCS 11802, Springer, 251–267.
- **[SOTA / Recent]** G. Exoo, D. Ismailescu. *The chromatic number of the plane is at least 5: a new proof.* Discrete & Computational Geometry 64, 2020, 216–226.
- **[SOTA / Recent]** D. W. Cranston, L. Rabern. *The fractional chromatic number of the plane.* Combinatorica 37, 2017, 837–861.
- **[SOTA / Recent]** G. Ambrus, A. Csiszárik, M. Matolcsi, D. Varga, P. Zsámboki. *The density of planar sets avoiding unit distances.* Mathematical Programming, 2025 (arXiv:2207.14179).
- **[SOTA / Recent]** S. Shelah, A. Soifer. *Axiom of choice and chromatic number of the plane.* Journal of Combinatorial Theory Series A 103, 2003, 387–391.
- **[SOTA / Recent]** O. Nechushtan. *On the space chromatic number.* Discrete Mathematics 256, 2002, 499–507; D. Coulson. *A 15-colouring of 3-space omitting distance one.* Discrete Mathematics 256, 2002, 83–90.
- **[Survey]** A. Soifer. *The Mathematical Coloring Book: Mathematics of Coloring and the Colorful Life of its Creators.* Springer, 2009.
- **[Survey]** A. M. Raigorodskii. *Coloring Distance Graphs and Graphs of Diameters.* In: Thirty Essays on Geometric Graph Theory, Springer, 2013, 429–460.

## 10. Worked Example / Concrete Special Case

**Claim: $\chi(\mathbb{R}^2) \ge 4$, via the Moser spindle (7 vertices, 11 edges).**

*Step 1 — triangles.* If $x,y,z$ form a unit equilateral triangle, all three are pairwise adjacent, so any proper colouring assigns three distinct colours.

*Step 2 — the rhombus lemma.* Let $R = \{a, u, v, b\}$ with $\|a-u\|=\|a-v\|=\|u-v\|=\|b-u\|=\|b-v\|=1$: two unit triangles glued along $uv$. Then $\|a-b\| = \sqrt{3}$. In a $3$-colouring, $\{a,u,v\}$ uses all three colours and $\{b,u,v\}$ uses all three colours; since $u,v$ already consume two colours, $c(a) = c(b)$. **So under any proper 3-colouring, points at distance $\sqrt{3}$ share a colour.**

*Step 3 — the spindle.* Take rhombus $R_1$ with apexes $a, b_1$ and rhombus $R_2 = \rho(R_1)$, where $\rho$ is the rotation about $a$ by the angle $\theta$ with
$$\|b_1 - b_2\| = 2\sqrt{3}\,\sin(\theta/2) = 1 \quad \Longrightarrow \quad \theta = 2\arcsin\!\left(\tfrac{1}{2\sqrt{3}}\right) \approx 33.557^\circ .$$
Concretely: $a=(0,0)$, $u_1=(\tfrac{\sqrt3}{2},\tfrac12)$... more simply, place $b_1 = (\sqrt3, 0)$ and $b_2 = \sqrt3(\cos\theta, \sin\theta) \approx (1.4434, 0.9574)$, so $\|b_1-b_2\| = 1$. The seven points are $a$, the two mid-pairs $\{u_1,v_1\}, \{u_2,v_2\}$, and $b_1, b_2$.

*Step 4 — contradiction.* Suppose a proper $3$-colouring exists. By Step 2 applied to $R_1$ and $R_2$: $c(b_1) = c(a) = c(b_2)$. But $\|b_1 - b_2\| = 1$, so $c(b_1) \ne c(b_2)$. Contradiction. Hence the spindle is $4$-chromatic and $\chi(\mathbb{R}^2) \ge 4$.

*Step 5 — the upper bound, checked.* Tile the plane by regular hexagons of side $s$, coloured in the standard $7$-periodic pattern in which two same-coloured hexagon centres are at distance at least $s\sqrt{7}$. Points inside one hexagon are at distance $< 2s$ (diameter). Choosing $s = 0.45$: within a hexagon the maximum distance is $0.90 < 1$, and distinct same-coloured hexagons have centres $\ge 0.45\sqrt7 \approx 1.1906$ apart, so their points are at distance $\ge 1.1906 - 0.90 = 0.2906$… tightening: the minimum distance between two same-coloured *closed* hexagons is $s\sqrt7 - 2s \cdot \tfrac{?}{}$; assigning boundaries half-open, one checks the minimum realized distance between distinct same-coloured tiles is $s(\sqrt7 - 2) \cdot$ (a positive constant) and the maximum within a tile is $2s$. The standard verification shows all distances of exactly $1$ are avoided for $1/\sqrt7 \approx 0.37796 < s < 0.5$. Hence $\chi(\mathbb{R}^2) \le 7$.

The gap between Step 4's technique (chaining rhombi, mechanized to $509$ vertices to force $5$) and Step 5's tiling is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*