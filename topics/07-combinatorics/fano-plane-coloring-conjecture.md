---
id: 07-combinatorics/fano-plane-coloring-conjecture
title: "Fano Plane Coloring Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fano Plane Coloring Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/fano-plane-coloring-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $F_7 = PG(2,2)$ be the Fano plane: $7$ points, $7$ lines, each line carrying $3$ points, each point on $3$ lines. A **Fano coloring** of a cubic graph $G$ is a map
$$c : E(G) \longrightarrow \mathrm{Pt}(F_7)$$
such that for every vertex $v$, the three colors on the edges incident with $v$ are three distinct points forming a **line** of $F_7$. Write $\lambda(G)$ for the least number of *distinct lines* realized at vertices, over all Fano colorings of $G$.

> **Conjecture (Máčajová–Škoviera, 2005).** Every bridgeless cubic graph $G$ admits a Fano coloring using at most **four** lines of the Fano plane, i.e. $\lambda(G) \le 4$.

A proof must produce, for every bridgeless cubic $G$, a coloring whose vertex-lines lie in a fixed $4$-element subset of the $7$ lines; a disproof must exhibit one bridgeless cubic graph needing $5$ or more lines. The constant $4$ is best possible: $\lambda(G)\le 3$ forces $G$ to be $3$-edge-colorable (Section 10), so the Petersen graph already has $\lambda = 4$ if the conjecture holds for it.

A companion, strictly weaker statement is the **five-line conjecture** ($\lambda(G)\le 5$ for all bridgeless cubic $G$).

## 2. Mathematical Foundations

Identify $\mathrm{Pt}(F_7)$ with $\mathbb{F}_2^3\setminus\{0\}$ and lines with triples summing to zero:
$$\mathcal{L} = \bigl\{\{x,y,z\} \subset \mathbb{F}_2^3\setminus\{0\} : x+y+z = 0\bigr\}, \qquad |\mathcal{L}| = 7 .$$
Then a Fano coloring is exactly a map $c:E\to\mathbb{F}_2^3\setminus\{0\}$ with
$$\sum_{e \ni v} c(e) = 0 \quad \text{for all } v \in V(G).$$
Distinctness at $v$ is automatic: if two incident edges share a color, the third color is $0$, excluded. Hence

> **Fact.** For cubic $G$, Fano colorings $=$ nowhere-zero $\mathbb{Z}_2^3$-flows.

By Jaeger's $8$-flow theorem (every bridgeless graph has a nowhere-zero $\mathbb{Z}_2^3$-flow), **every bridgeless cubic graph is Fano-colorable**, and bridgelessness is necessary (a bridge carries flow $0$). The content of the conjecture is therefore not existence but *economy*: how few lines suffice.

The Fano plane is the unique Steiner triple system $STS(7)$: a pair $(P,\mathcal{B})$ with $|P|=7$, blocks of size $3$, every pair in exactly one block. Fano coloring is the $STS(7)$ case of $S$-coloring of cubic graphs (Holroyd–Škoviera).

Two covering conjectures for bridgeless cubic graphs frame the problem. Write $\mathcal{M}(G)$ for the set of perfect matchings.

- **Fulkerson (1971), also attributed to Berge.** There exist $M_1,\dots,M_6 \in \mathcal{M}(G)$ with
$$\sum_{i=1}^{6} \mathbf{1}_{M_i}(e) = 2 \quad \text{for every } e \in E(G).$$
- **Berge.** There exist $M_1,\dots,M_5 \in \mathcal{M}(G)$ with $\bigcup_i M_i = E(G)$.

Máčajová and Škoviera proved the translation into line-economy:
$$\text{Fulkerson} \iff \bigl(\lambda(G)\le 4 \ \ \forall G \text{ bridgeless cubic}\bigr), \qquad
\text{Berge} \iff \bigl(\lambda(G)\le 5 \ \ \forall G\bigr).$$
Mazzuoccolo (2011) later proved Berge $\Leftrightarrow$ Fulkerson, so the $4$-line and $5$-line statements are equivalent *as universal statements*, though not necessarily graph by graph.

## 3. History & State of the Art (SOTA)

- **1971.** Fulkerson states the double-cover-by-six-perfect-matchings conjecture in *Blocking and anti-blocking pairs of polyhedra*.
- **1979.** Jaeger's $8$-flow theorem; Seymour's $6$-flow theorem. These give existence of Fano colorings for all bridgeless cubic graphs but no control on lines.
- **1988.** Jaeger proposes the Petersen coloring conjecture, which implies both Fulkerson and Berge, and hence the $4$-line statement.
- **2004.** Holroyd and Škoviera, *Colouring of cubic graphs by Steiner triple systems* (JCTB 91, 57–66): a cubic graph is colorable by a projective system $PG(n,2)$ iff it is bridgeless; they conjecture every bridgeless cubic graph is colorable by *every* non-trivial STS.
- **2005.** Máčajová and Škoviera, *Fano colourings of cubic graphs and the Fulkerson conjecture* (Theoret. Comput. Sci. 349, 112–120): the line-count hierarchy $3 \mid 4 \mid 5 \mid 7$ above; the four-line conjecture is stated here. Their unconditional bound is **six lines** for every bridgeless cubic graph *(verify — the precise unconditional constant should be checked against the printed paper)*.
- **2009.** Král', Máčajová, Pangrác, Raspaud, Sereni, Škoviera, *Projective, affine, and abelian colorings of cubic graphs* (EJC 30, 53–69): structural characterizations separating projective systems (the Fano plane and its higher analogues) from affine and abelian ones.
- **2011.** Mazzuoccolo: Berge $\Leftrightarrow$ Fulkerson, collapsing the $4$-line and $5$-line conjectures at the level of the whole class.

**SOTA summary.** Unconditional: $\lambda(G) \le 7$ trivially, $\le 6$ by Máčajová–Škoviera. Conditional: $\le 5$ $\Leftrightarrow$ Berge, $\le 4$ $\Leftrightarrow$ Fulkerson. Lower: $\lambda(G)\ge 4$ for every non-$3$-edge-colorable $G$.

## 4. Partial Results / Verified Cases

- **$3$-edge-colorable cubic graphs** (equivalently $\chi'(G)=3$, class 1): $\lambda(G)=1$ — a single line suffices. Covers all bridgeless cubic graphs that are planar (Four Color Theorem), Hamiltonian, or $3$-connected with no Petersen minor (Edwards–Sanders–Seymour–Thomas).
- **Petersen graph.** Its six perfect matchings form a Fulkerson cover (each edge lies in exactly two), so $\lambda(P)=4$: the extremal example.
- **Snark families with verified Fulkerson covers**, hence $\lambda = 4$: flower snarks $J_{2k+1}$ and Goldberg snarks (Fouquet–Vanherpe, *On Fulkerson conjecture*, Discuss. Math. Graph Theory 31 (2011)); several Loupekine and Blanuša-type families (Hägglund–Steffen, *Petersen-colourings and some families of snarks*, Ars Math. Contemp. 7 (2014)).
- **Small orders.** Fulkerson covers have been found by computer for all cubic graphs up to the ranges reachable by exhaustive snark generation (all snarks on $\le 36$ vertices in the Brinkmann–Goedgebeur–Hägglund–Markström census), so $\lambda \le 4$ is verified there.
- **Graphs with small oddness.** Cubic graphs whose $2$-factors miss $3$-edge-colorability by two odd circuits (oddness $2$) admit Fulkerson covers in the cases treated by Hägglund–Steffen; these give $\lambda = 4$.
- **Weakenings proved.** Kaiser–Král'–Norine: three perfect matchings covering at least $\tfrac{3}{5}|E|$ in every bridgeless cubic graph. Fan–Raspaud (three perfect matchings with empty intersection) remains open but is implied by the $4$-line statement.

## 5. Principal Obstacles

- **Flow methods are blind to line count.** Existence follows from the $8$-flow theorem, but nowhere-zero flow arguments (partition into $3$ even subgraphs) give no way to constrain the *set* of vertex-lines. There is no known flow-theoretic parameter measuring $\lambda$.
- **Non-locality of the constraint.** The set of admissible lines is global; local reduction/uncoloring arguments that work for edge-colorings (Kempe chains, Vizing fans) do not preserve a fixed $4$-line palette, because switching one vertex's line can force a chain of line changes around a cycle.
- **Equivalence with Fulkerson imports its hardness.** Fulkerson has resisted more than 50 years of polyhedral, matching-theoretic, and structural attack. The perfect matching polytope characterization gives *fractional* Fulkerson covers (Seymour, 1979: the all-$\tfrac13$ vector lies in the matching polytope of any bridgeless cubic graph), but the integrality step — from a fractional cover with denominator $k$ to six integral matchings — is exactly the missing step.
- **No induction on snarks.** Snarks are not closed under the usual reductions in a way that preserves $\lambda$; cyclic $4$- and $5$-edge-cuts allow splitting, but $6$-edge-cuts and beyond do not compose $4$-line colorings.
- **Counting is too weak.** Probabilistic and entropy bounds on the number of perfect matchings (Esperet–Kardoš–King–Král'–Norine: exponentially many perfect matchings in bridgeless cubic graphs) do not force any *balanced* family.

## 6. The Gap

Proven: $\lambda(G) \le 6$ unconditionally, and $\lambda(G) = 1$ for class-1 graphs, $\lambda(G) = 4$ for finitely many verified snark families and censuses. Conjectured: $\lambda(G) \le 4$ for all bridgeless cubic graphs.

The gap is exactly one integrality step. Every bridgeless cubic graph has a fractional Fulkerson cover; the open step is to convert a rational point of the perfect matching polytope into six integral matchings, equivalently to reduce the vertex-line palette from six lines to four. Since a $4$-line palette of "dual frame" type collapses to a $3$-edge-coloring (Section 10), any proof must specifically produce a palette consisting of a pencil of three concurrent lines plus one line off the common point — a very rigid target that no current construction hits for arbitrary $G$.

## 7. Current Research (as of June 2026)

- **Bratislava school (Máčajová, Škoviera and collaborators).** Continued work on perfect matching indices $\mu(G)$ — the least number of perfect matchings covering $E(G)$ — and on cubic graphs not coverable by four perfect matchings; these directly bound line counts.
- **Structural snark theory (Brinkmann, Goedgebeur, Hägglund, Markström, Steffen).** Extending exhaustive generation and Fulkerson-cover verification to larger snark censuses; each extension enlarges the verified range of $\lambda \le 4$. *(frontier — verify current computational limits)*
- **Polyhedral / integrality attacks (Mazzuoccolo, Esperet and coauthors).** Searching for cubic graphs whose edge set is not coverable by four perfect matchings and studying the associated fractional relaxations.
- **Steiner-system colorings.** The general Holroyd–Škoviera $S$-coloring program continues; determining exactly which Steiner triple systems color all bridgeless cubic graphs remains active, with the projective systems $PG(n,2)$ the understood case. *(frontier — verify)*
- **Petersen coloring route.** Work on Jaeger's conjecture (normal $5$-edge-colorings, Bílková–Šámal-style approaches) would, if successful, settle the $4$-line conjecture as a corollary. *(frontier — verify)*

## 8. Future Work

- Prove $\lambda(G)\le 5$ (equivalently Berge) for a structurally defined infinite family beyond known snark families, e.g. all cubic graphs of oddness $\le 4$.
- Find a discharging or entropy argument giving a Fulkerson cover from a fractional one for graphs with large girth.
- Sharpen the unconditional bound from six to five lines by a direct combinatorial argument on vertex-line palettes; by the equivalences this proves Berge, hence Fulkerson.
- Search computationally for a bridgeless cubic graph with $\lambda \ge 5$ among snarks with high cyclic connectivity and oddness, where Fulkerson covers are hardest to build.
- Classify the possible $4$-line palettes further: show that palettes with three concurrent lines suffice, or find an obstruction.

## 9. Key References

- **[Foundational]** D. R. Fulkerson. *Blocking and anti-blocking pairs of polyhedra.* Mathematical Programming 1 (1971), 168–194.
- **[Foundational]** F. Jaeger. *Flows and generalized coloring theorems in graphs.* Journal of Combinatorial Theory Series B 26 (1979), 205–216.
- **[Foundational]** P. D. Seymour. *On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte.* Proceedings of the London Mathematical Society (3) 38 (1979), 423–460.
- **[Foundational]** F. Jaeger. *Nowhere-zero flow problems.* In: L. W. Beineke, R. J. Wilson (eds.), Selected Topics in Graph Theory 3, Academic Press, 1988, 71–95.
- **[Key]** F. Holroyd, M. Škoviera. *Colouring of cubic graphs by Steiner triple systems.* Journal of Combinatorial Theory Series B 91 (2004), 57–66.
- **[Key / statement of the conjecture]** E. Máčajová, M. Škoviera. *Fano colourings of cubic graphs and the Fulkerson conjecture.* Theoretical Computer Science 349 (2005), 112–120.
- **[SOTA / Recent]** G. Mazzuoccolo. *The equivalence of two conjectures of Berge and Fulkerson.* Journal of Graph Theory 68 (2011), 125–128.
- **[SOTA / Recent]** D. Král', E. Máčajová, O. Pangrác, A. Raspaud, J.-S. Sereni, M. Škoviera. *Projective, affine, and abelian colorings of cubic graphs.* European Journal of Combinatorics 30 (2009), 53–69.
- **[SOTA / Recent]** L. Esperet, G. Mazzuoccolo. *On cubic bridgeless graphs whose edge-set cannot be covered by four perfect matchings.* Journal of Graph Theory 77 (2014), 144–157.
- **[SOTA / Recent]** J. Hägglund, E. Steffen. *Petersen-colorings and some families of snarks.* Ars Mathematica Contemporanea 7 (2014), 161–173.
- **[Related]** G. Fan, A. Raspaud. *Fulkerson's conjecture and circuit covers.* Journal of Combinatorial Theory Series B 61 (1994), 133–138.
- **[Related]** T. Kaiser, D. Král', S. Norine. *Unions of perfect matchings in cubic graphs.* In: Topics in Discrete Mathematics, Algorithms and Combinatorics 26, Springer, 2006, 225–230.
- **[Survey]** M. J. Grannell, T. S. Griggs, M. Knor, M. Škoviera. *Colouring cubic graphs by small Steiner triple systems.* Graphs and Combinatorics 23 (2007), 217–229.

## 10. Worked Example / Concrete Special Case

**Claim.** If a Fano coloring of a cubic graph $G$ uses a set $\mathcal{P}$ of at most three lines, or four lines no three of which are concurrent, then $G$ is $3$-edge-colorable. Consequently every snark (bridgeless, non-$3$-edge-colorable) needs $\lambda \ge 4$, with a palette of a very specific shape.

*Case A: all lines of $\mathcal{P}$ pass through a common point $q$.* Two lines always meet, so this covers $|\mathcal{P}| \le 2$; assume $|\mathcal{P}|\le 3$ concurrent. Every vertex-line contains $q$, so exactly one edge at each vertex is colored $q$: $M = c^{-1}(q)$ is a perfect matching. Each line through $q$ is $\{q,p,p+q\}$, so the two non-$q$ edges at a vertex carry the pair $\{p,p+q\}$. Adjacent edges of the $2$-factor $E\setminus M$ share a vertex, hence the same pair; the pair is constant on each circuit, which is therefore alternating and even. Two colors on the $2$-factor plus $M$ give a proper $3$-edge-coloring.

*Case B: $\mathcal{P}$ has no three concurrent lines.* Counting incidences, $|\mathcal{P}|\cdot 3 = 12$ when $|\mathcal{P}| = 4$, and since each point lies on at most two lines of $\mathcal{P}$, exactly six points lie on two lines each and one point $q$ lies on none. So $\mathcal{P}$ is the set of the four lines avoiding $q$. Partition the other six points into pairs $\{p, p+q\}$. No line $L \in \mathcal{P}$ contains both members of a pair, since $p + (p+q) = q$ would force $q \in L$. Hence each $L\in\mathcal{P}$ meets each of the three pairs exactly once, and the three sets
$$c^{-1}\bigl(\{p, p+q\}\bigr), \qquad p \in \{p_1,p_2,p_3\},$$
are perfect matchings partitioning $E(G)$: a proper $3$-edge-coloring. Any triangle of three non-concurrent lines sits inside such a family, so the case $|\mathcal{P}|=3$ non-concurrent is covered too. $\square$

**Consequence for the Petersen graph $P$.** $P$ is a snark, so $\lambda(P) \ge 4$ and any $4$-line palette for $P$ must be of the remaining type: three lines $A,B,C$ through a point $q$, plus one line $D \not\ni q$. Concretely, with $q = 001$,
$$A=\{001,010,011\},\quad B=\{001,100,101\},\quad C=\{001,110,111\},\quad D=\{010,100,110\},$$
where $D$ takes one point from each of the pairs $\{010,011\},\{100,101\},\{110,111\}$ and satisfies $010+100+110=000$. The Petersen graph has exactly six perfect matchings, each edge lying in exactly two of them — a Fulkerson cover — and the Máčajová–Škoviera translation converts this cover into a Fano coloring on the palette $\{A,B,C,D\}$, giving $\lambda(P)=4$. The general conjecture asserts that every bridgeless cubic graph admits such a palette of pencil-plus-one type.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*