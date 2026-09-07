---
id: 07-combinatorics/hadwiger-nelson-problem
title: "Hadwiger-Nelson Problem"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hadwiger-Nelson Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hadwiger-nelson-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Determine the **chromatic number of the plane**: the least number of colors needed to color every point of $\mathbb{R}^2$ so that no two points at Euclidean distance exactly $1$ receive the same color.

Formally, let $G_2 = (\mathbb{R}^2, E)$ with $\{x,y\} \in E \iff \|x-y\|_2 = 1$. The quantity sought is $\chi(G_2)$, written $\chi(\mathbb{R}^2)$.

Known: $5 \le \chi(\mathbb{R}^2) \le 7$. The open problem is to decide which of $5, 6, 7$ is correct. A complete resolution requires either

- an explicit proper $k$-coloring of $\mathbb{R}^2$ avoiding unit-distance monochromatic pairs for $k \in \{5,6\}$, together with a matching lower bound, or
- a finite unit-distance graph with chromatic number $6$ (resp. $7$), which by compactness forces $\chi(\mathbb{R}^2) \ge 6$ (resp. $=7$).

The problem is sensitive to set-theoretic axioms: the answer for arbitrary (non-measurable) colorings may differ from the answer under measurability or Solovay-type axioms.

## 2. Mathematical Foundations

**Unit-distance graph.** For $S \subseteq \mathbb{R}^n$, the unit-distance graph is $G(S) = (S, \{\{x,y\} : \|x-y\| = 1\})$. A *finite unit-distance graph* is any finite induced subgraph. $\chi(\mathbb{R}^n) := \chi(G(\mathbb{R}^n))$.

**Compactness (de Bruijn–Erdős, 1951).** If every finite subgraph of a graph $G$ is $k$-colorable, then $G$ is $k$-colorable — assuming the axiom of choice (equivalently, the ultrafilter lemma). Hence
$$\chi(\mathbb{R}^2) = \sup\{\chi(H) : H \subseteq G_2 \text{ finite}\}.$$
This reduces the problem to finite combinatorics and makes computer search meaningful.

**Upper bound construction.** Tile $\mathbb{R}^2$ by regular hexagons of diameter $d$ with $\tfrac{\sqrt{3}}{2} < d < 1$, half-open so the tiles partition the plane. Color the tiles with $7$ colors using the standard Eisenstein-lattice pattern: two tiles of the same color have centers at distance $\ge \sqrt{7}\,r$ where $r$ is the circumradius. Choosing $r$ so that $2r < 1 < \sqrt{7}r - 2r$ gives a proper coloring, so $\chi(\mathbb{R}^2) \le 7$.

**Measurable and fractional relaxations.**
- $\chi_m(\mathbb{R}^2)$: least $k$ such that $\mathbb{R}^2 = \bigsqcup_{i=1}^k A_i$ with each $A_i$ Lebesgue measurable and unit-distance-free.
- The *independence density* $m_1(\mathbb{R}^2) := \sup\{\bar\delta(A) : A \text{ measurable, } \|x-y\|\neq 1 \ \forall x,y \in A\}$ satisfies $\chi_m(\mathbb{R}^2) \ge 1/m_1(\mathbb{R}^2)$.
- Fractional chromatic number $\chi_f(\mathbb{R}^2) = 1/m_1(\mathbb{R}^2)$ (Fourier/LP duality on the Euclidean group), and $\chi_f \le \chi$.

**Spectral/LP bound.** For an autocorrelation-positive $f$ with $\hat f \ge 0$, $f(0)=1$, supported spectrally so that $\sum$ of Fourier mass at the unit sphere is controlled, one gets Delsarte-type bounds on $m_1$; this is the analytic engine behind $\chi_f$ estimates.

**Rational and algebraic subfields.** For a subfield $F \subseteq \mathbb{R}$, $\chi(F^n)$ is studied via the quadratic form $\sum (x_i - y_i)^2 = 1$ and the associated Witt/valuation structure at primes $p$; solvability of the form $p$-adically controls which $F^n$ contain unit-distance odd cycles.

## 3. History & State of the Art (SOTA)

- **1950.** Edward Nelson poses the question; Hugo Hadwiger publishes a closely related coloring problem (1945, 1961). John Isbell contributes the $7$-coloring; Hadwiger's hexagonal tiling gives the same bound. The Moser brothers' 1961 "spindle" gives $\chi \ge 4$; Golomb's graph gives an independent $\ge 4$ proof. Gardner popularizes the problem in *Scientific American* (1960).
- **1951.** de Bruijn–Erdős compactness theorem: the problem is equivalent to a statement about finite graphs.
- **1981.** Falconer: $\chi_m(\mathbb{R}^2) \ge 5$ for measurable colorings.
- **2003.** Shelah–Soifer: in a ZF + DC + "all sets Lebesgue measurable" universe, natural analogues of the problem have different answers than under AC — the chromatic number of the plane is axiom-dependent for some distance graphs on $\mathbb{Q}$-structured sets.
- **April 2018.** **Aubrey de Grey**, *The chromatic number of the plane is at least 5* (Geombinatorics 28), exhibits a 5-chromatic unit-distance graph with $1581$ vertices, built from copies of the Moser spindle and a 7-fold "H" assembly, verified by SAT solver. First improvement to the lower bound in 68 years.
- **2018–2020.** Polymath16 (Terence Tao, Dustin Mixon, Marijn Heule, Jaan Parts and others) shrinks the witness: $874 \to 826 \to 610 \to 553 \to 510$ vertices (Heule), then $509$ (Parts, 2020). Exoo–Ismailescu independently construct 5-chromatic unit-distance graphs (*Discrete & Computational Geometry*, 2020).
- **2017.** Cranston–Rabern: $\chi_f(\mathbb{R}^2) \ge 3.8992$ (*Combinatorica*), lifting the previous $3.5$-type bounds; upper bound $\chi_f(\mathbb{R}^2) \le 4.3599$ (Croft-type constructions).
- **2022.** Ambrus, Csiszárik, Matolcsi, Varga, Zsámboki announce $\chi_m(\mathbb{R}^2) \ge 6$ for measurable colorings, via a large-scale polygon-based LP/computer-assisted argument *(frontier — verify)*.

The upper bound $7$ has not moved since 1950.

## 4. Partial Results / Verified Cases

- **Plane, general colorings:** $5 \le \chi(\mathbb{R}^2) \le 7$. Lower bound witnessed by a $509$-vertex unit-distance graph; SAT-verified with independently checkable DRAT proofs (Heule).
- **Measurable colorings:** $\chi_m(\mathbb{R}^2) \ge 5$ (Falconer 1981); $\ge 6$ claimed 2022 *(frontier — verify)*. Also $\chi_m(\mathbb{R}^2) \ge 5$ holds for colorings by Jordan-measurable or by tile-like (bounded-boundary) pieces (Townsend; Woodall).
- **Restricted-shape colorings:** if all color classes are unions of "nice" regions with piecewise-smooth boundary, $\ge 6$ colors are needed (Woodall 1973, Townsend 1979).
- **Fractional:** $3.8992 \le \chi_f(\mathbb{R}^2) \le 4.3599$.
- **Rational subspaces (fully solved):** $\chi(\mathbb{Q}^2) = 2$ and $\chi(\mathbb{Q}^3) = 2$ (Woodall 1973); $\chi(\mathbb{Q}^4) = 4$ (Benda–Perles); $\chi(\mathbb{Q}^n)$ known to grow, with $\chi(\mathbb{Q}^5) \ge 8$.
- **Higher dimensions:** $6 \le \chi(\mathbb{R}^3) \le 15$ (lower bound Nechushtan 2002; upper bound Radoičić–Tóth 2003). $9 \le \chi(\mathbb{R}^4) \le 54$.
- **Asymptotics:** $(1.239\ldots + o(1))^n \le \chi(\mathbb{R}^n) \le (3+o(1))^n$. Exponential lower bound from Frankl–Wilson (1981) forbidden-intersection theorem, sharpened by Raigorodskii (2000); upper bound Larman–Rogers (1972).
- **Girth constraints:** 5-chromatic unit-distance graphs of girth $\ge 4$ and $\ge 5$ exist (Exoo–Ismailescu; Polymath16), ruling out "triangle-density" explanations of the lower bound.
- **Other norms:** for any norm whose unit ball tiles the plane by a lattice, the analogous chromatic number is $4$; so the answer $>4$ for $\ell_2$ is a genuinely Euclidean phenomenon.

## 5. Principal Obstacles

- **The upper bound is combinatorially rigid.** Every known $7$-coloring is a lattice tiling by sets of diameter just under $1$. An improvement to $6$ requires color classes that are *not* bounded-diameter tiles: a unit-distance-free set of upper density $> 1/6 \approx 0.1667$ is needed, but the best known density for a measurable unit-distance-free set is about $0.2293$ (Croft's "tortoise" set) for a *single* class — and no construction is known that packs six such sets to cover the plane. The LP/Fourier bounds ($m_1 \le 0.2568$) leave no room for a clean contradiction but also give no construction.
- **Lower bounds need enormous finite graphs.** Since a $6$-chromatic unit-distance graph, if it exists, plausibly has thousands to millions of vertices, SAT/CDCL search space explodes: the number of candidate vertex sets in $\mathbb{Q}(\sqrt{3},\sqrt{11},\ldots)$-generated point clouds grows super-exponentially, and symmetry breaking is weak because rotations by non-algebraic angles are available.
- **No algebraic invariant.** Unlike Hadwiger's conjecture or Borsuk-type problems, there is no known topological or homological obstruction certifying $\chi \ge 6$; standard tools (Borsuk–Ulam, chromatic-number-of-Kneser-graph machinery) do not apply because the unit-distance graph has no natural simplicial or box-complex structure with computable connectivity.
- **Fourier analysis stalls.** Delsarte-type LP bounds on $m_1(\mathbb{R}^2)$ have been pushed near their theoretical limit; the LP relaxation cannot distinguish $\chi_f$ from $\chi$, and $\chi_f \le 4.36 < 5$ means fractional methods can *never* prove $\chi \ge 5$, let alone $6$.
- **Axiom dependence.** Shelah–Soifer show that some Euclidean coloring problems have different answers in ZFC and in ZF+DC+LM. If $\chi(\mathbb{R}^2)$ is one of them, "the" answer is not a single integer, and the finite-graph route (which uses AC via de Bruijn–Erdős) may be answering a different question than the measurable one.

## 6. The Gap

Proven: a finite unit-distance graph with $\chi = 5$ exists ($509$ vertices), and the hexagonal tiling gives $\chi \le 7$. The entire gap is the two-step interval $\{5,6,7\}$.

Crossing it requires exactly one of:

1. **A 6-chromatic finite unit-distance graph.** All current 5-chromatic witnesses are "tight": deleting almost any vertex drops them to $4$-chromatic. No known family has a parameter whose increase provably raises the chromatic number.
2. **A 6-coloring of $\mathbb{R}^2$.** This needs six unit-distance-free sets of average density $1/6$ covering the plane. Since no unit-distance-free measurable set of density $>1/6$ arising from a *tiling* is known, a valid 6-coloring must use fractal or non-measurable classes — but non-measurable classes cannot be exhibited constructively, and measurable ones may already be excluded if the 2022 $\chi_m \ge 6$ claim holds.
3. **A proof that $\chi = 7$**, i.e. a 7-chromatic finite unit-distance graph. Nothing in the literature suggests where to look.

The sharpest formulation of the gap: is $\sup$ over finite unit-distance graphs of $\chi$ attained at $5$, or does the tower continue?

## 7. Current Research (as of June 2026)

- **Polymath16 legacy and SAT scaling.** Marijn Heule (Carnegie Mellon) continues to develop cube-and-conquer and DRAT-verified pipelines for unit-distance colorability; the effort has shifted from shrinking 5-chromatic graphs to certifying that large structured point sets (e.g. Moser-spindle-closed sets over $\mathbb{Q}(\sqrt{3},\sqrt{11})$) are 5-colorable, thereby ruling out whole search families *(frontier — verify)*.
- **Measurable chromatic number.** Ambrus, Matolcsi and collaborators (Alfréd Rényi Institute, Budapest) pursue polygon-decomposition + LP methods that produced the $\chi_m \ge 6$ claim; the natural target is $\chi_m \ge 7$, which would settle the measurable version entirely *(frontier — verify)*.
- **Fourier/LP and density.** Bellitto, Pêcher, Sédillot (Bordeaux) and de Oliveira Filho–Vallentin (Cologne) push semidefinite hierarchies (Lasserre level 3+) on $m_1(\mathbb{R}^2)$ toward $1/5$, which would prove $\chi_m \ge 5$ by a purely analytic route and possibly beyond.
- **Structured subfields.** Ongoing work computes $\chi(F^2)$ for real quadratic and cyclotomic fields $F$, seeking the minimal field in which a 6-chromatic unit-distance graph can live; all known 5-chromatic graphs embed in $\mathbb{Q}(\sqrt{3},\sqrt{11})$.
- **Set theory.** Soifer and collaborators continue the "conditional chromatic number" program: computing $\chi(\mathbb{R}^2)$ in ZF+DC+LM versus ZFC.

## 8. Future Work

- Construct a unit-distance-free measurable set of upper density $> 1/6$, or prove none exists (this alone would decide the measurable problem's $6$ vs $7$ dichotomy).
- Develop a *combinatorial certificate* for lower bounds that scales: e.g. a Ramsey-type or entropy-compression argument producing 6-chromatic graphs without exhaustive search.
- Extend the girth-based results: does a 5-chromatic unit-distance graph of arbitrarily large girth exist? A positive answer would show local structure is irrelevant and steer search toward global/spectral obstructions.
- Attack $\chi(\mathbb{R}^3)$, where the gap $[6,15]$ is wider but the geometry richer; improvements there may reveal transferable techniques.
- Settle whether $\chi(\mathbb{R}^2)$ is independent of ZFC — Soifer's explicitly stated long-term goal.

## 9. Key References

- **[Foundational]** N. G. de Bruijn and P. Erdős. *A colour problem for infinite graphs and a problem in the theory of relations.* Indagationes Mathematicae 13 (1951), 369–373.
- **[Foundational]** L. Moser and W. Moser. *Solution to Problem 10.* Canadian Mathematical Bulletin 4 (1961), 187–189.
- **[Foundational]** D. R. Woodall. *Distances realized by sets covering the plane.* Journal of Combinatorial Theory, Series A 14 (1973), 187–200.
- **[Foundational]** K. J. Falconer. *The realization of distances in measurable subsets covering $\mathbb{R}^n$.* Journal of Combinatorial Theory, Series A 31 (1981), 184–189.
- **[Foundational]** P. Frankl and R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1 (1981), 357–368.
- **[Foundational]** D. G. Larman and C. A. Rogers. *The realization of distances within sets in Euclidean space.* Mathematika 19 (1972), 1–24.
- **[SOTA / Recent]** A. D. N. J. de Grey. *The chromatic number of the plane is at least 5.* Geombinatorics 28 (2018), 18–31. (arXiv:1804.02385)
- **[SOTA / Recent]** G. Exoo and D. Ismailescu. *The chromatic number of the plane is at least 5: a new proof.* Discrete & Computational Geometry 64 (2020), 216–226.
- **[SOTA / Recent]** M. J. H. Heule. *Computing small unit-distance graphs with chromatic number 5.* Geombinatorics 28 (2018), 32–50.
- **[SOTA / Recent]** J. Parts. *Graph minimization, focusing on the example of 5-chromatic unit-distance graphs in the plane.* Geombinatorics 29 (2020), 137–166.
- **[SOTA / Recent]** D. W. Cranston and L. Rabern. *The fractional chromatic number of the plane.* Combinatorica 37 (2017), 837–861.
- **[SOTA / Recent]** G. Ambrus, A. Csiszárik, M. Matolcsi, D. Varga, P. Zsámboki. *The measurable chromatic number of the plane is at least 6.* arXiv:2209.15265 (2022).
- **[Survey]** A. Soifer. *The Mathematical Coloring Book: Mathematics of Coloring and the Colorful Life of Its Creators.* Springer, 2009.
- **[Survey]** A. M. Raigorodskii. *Coloring Distance Graphs and Graphs of Diameters.* In *Thirty Essays on Geometric Graph Theory* (J. Pach, ed.), Springer, 2013, 429–460.
- **[Survey]** S. Shelah and A. Soifer. *Axiom of choice and chromatic number of the plane.* Journal of Combinatorial Theory, Series A 103 (2003), 387–391.

## 10. Worked Example / Concrete Special Case

**Claim: the Moser spindle proves $\chi(\mathbb{R}^2) \ge 4$.**

*Construction.* Start with a rhombus $R = \{A, B, C, D\}$ made of two unit equilateral triangles glued along an edge: $A=(0,0)$, $B=(1,0)$, $C=(\tfrac12,\tfrac{\sqrt3}{2})$, $D=(\tfrac32,\tfrac{\sqrt3}{2})$. Edges $AB, AC, BC, BD, CD$ all have length $1$. The long diagonal has
$$\|A - D\| = \sqrt{\left(\tfrac32\right)^2 + \left(\tfrac{\sqrt3}{2}\right)^2} = \sqrt{\tfrac94+\tfrac34} = \sqrt{3}.$$

*Key rhombus lemma.* In any proper coloring, $A$ and $D$ get the same color **or** different colors; but if the whole plane is $3$-colored, then in $\{A,B,C\}$ and $\{B,C,D\}$ — both unit triangles — all three colors appear, forcing $\mathrm{col}(A) = \mathrm{col}(D)$. So under a $3$-coloring, **any two points at distance $\sqrt3$ have the same color**.

*Spindle.* Take a second copy $R'$ of the rhombus sharing the apex $A$, rotated about $A$ by the angle $\theta$ chosen so that the two far vertices $D$ and $D'$ satisfy $\|D - D'\| = 1$. Since $\|A-D\| = \|A-D'\| = \sqrt3$, this needs
$$1 = 2\sqrt{3}\,\sin(\theta/2) \implies \theta = 2\arcsin\!\left(\tfrac{1}{2\sqrt3}\right) \approx 33.56^\circ,$$
which is a valid rotation. The resulting graph has $7$ vertices $\{A,B,C,D,B',C',D'\}$ and $11$ edges.

*Contradiction.* Under a hypothetical $3$-coloring: $\mathrm{col}(D) = \mathrm{col}(A)$ and $\mathrm{col}(D') = \mathrm{col}(A)$ by the rhombus lemma, so $\mathrm{col}(D) = \mathrm{col}(D')$. But $\|D - D'\| = 1$, so $D$ and $D'$ must differ. Contradiction. Hence $\chi(\text{Moser spindle}) = 4$ (four colors suffice: it is $4$-colorable by inspection), and by de Bruijn–Erdős $\chi(\mathbb{R}^2) \ge 4$.

*Scaling up.* De Grey's $1581$-vertex graph iterates this idea: it uses a vertex set $H$ closed under a group of rotations, in which every $4$-coloring is forced to be "linear" on a large sublattice, and then a SAT solver certifies that no $4$-coloring of the assembled graph extends. The $509$-vertex minimization by Parts keeps the same forcing skeleton with redundant vertices removed. No analogous forcing lemma is known that would push the argument from $5$ to $6$ — that missing lemma is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*