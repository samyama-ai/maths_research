---
id: 07-combinatorics/erdos-distinct-distances-problem
title: "Erdős Distinct Distances Problem"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Distinct Distances Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-distinct-distances-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

For a finite set $P \subset \mathbb{R}^2$ of $n$ points, let
$$\Delta(P) = \{\, \|p-q\|_2 : p,q \in P,\ p \neq q \,\}, \qquad g(n) = \min_{|P|=n} |\Delta(P)|.$$

Erdős (1946) asked for the growth rate of $g(n)$ and conjectured that the $\sqrt{n}\times\sqrt{n}$ integer lattice is extremal, i.e.
$$g(n) = \Theta\!\left(\frac{n}{\sqrt{\log n}}\right).$$

Guth and Katz (2015) proved the matching-up-to-a-logarithm lower bound $g(n) \ge c\,n/\log n$. What remains open is the $\sqrt{\log n}$ gap between $n/\log n$ and $n/\sqrt{\log n}$, the corresponding problem in $\mathbb{R}^d$ for $d \ge 3$ (conjecture: $g_d(n) = \Theta(n^{2/d})$, with a $\log$ correction at $d=2$ only), and the **structural** conjecture that any near-extremal set is essentially a lattice.

A complete resolution means: determine $g(n)$ up to constants (or prove the asymptotic $g(n)\sim c\,n/\sqrt{\log n}$), and settle whether minimizers must be lattice-like.

## 2. Mathematical Foundations

**Distance multiset and energy.** Write $D = |\Delta(P)|$. The quadruple count
$$Q(P) = \\#\{(a,b,c,d) \in P^4 : \|a-b\| = \|c-d\| \neq 0\}$$
satisfies, by Cauchy–Schwarz over the $D$ distance classes,
$$Q(P) \ \ge \ \frac{\big(n(n-1)\big)^2}{D}, \qquad\text{so}\qquad D \ \ge \ \frac{n^4(1+o(1))}{Q(P)}.$$
Bounding $D$ from below is therefore equivalent to bounding the "distance energy" $Q$ from above.

**Elekes–Sharir framework.** Let $G$ be the group of orientation-preserving rigid motions of $\mathbb{R}^2$, a $3$-dimensional Lie group parametrized by $(x,y,\theta)$ (rotation by $\theta$ about the point $(x,y)$; translations at $\theta=0$). For $p,q \in \mathbb{R}^2$ define
$$L_{pq} = \{\, g \in G : g(p) = q \,\}.$$
Under the parametrization $(x,y,\theta)\mapsto \big(x,\,y,\,\cot(\theta/2)\big)$, each $L_{pq}$ becomes a **straight line** in $\mathbb{R}^3$. The key identity is
$$\|a-b\| = \|c-d\| \iff \exists\, g \in G:\ g(a)=c,\ g(b)=d \iff L_{ac} \cap L_{bd} \neq \emptyset .$$
Hence $Q(P)$ is controlled by the number of intersecting pairs among the $N = n^2$ lines $\{L_{pq}\}$.

**Guth–Katz line theorem.** Let $\mathcal{L}$ be $N$ lines in $\mathbb{R}^3$ with at most $N^{1/2}$ in any plane or regular quadric surface. Then the number of points lying on at least $2$ lines is $O(N^{3/2})$, and for $k \ge 3$ the number of points on at least $k$ lines is $O(N^{3/2}/k^2)$. Combined with the symmetry constraints of the Elekes–Sharir lines this gives $Q(P) = O(n^3\log n)$ and thus
$$D \ \ge \ c\,\frac{n}{\log n}.$$

**Tools.** Polynomial partitioning: for $\mathcal{P}$ a set of $m$ points in $\mathbb{R}^d$ and $r>1$ there is $f \ne 0$ of degree $O(r^{1/d})$ whose zero set cuts $\mathbb{R}^d$ into $O(r)$ cells each containing $\le m/r$ points (via the polynomial ham-sandwich theorem). Also used: the flecnode polynomial of Cayley–Salmon (degree $11d-24$) characterizing ruled surfaces, and Bézout-type degree bounds.

**Lattice upper bound.** For $P = \{1,\dots,\sqrt n\}^2$, distinct distances correspond to integers $\le 2n$ that are sums of two squares. By Landau–Ramanujan, their count is $\sim K\,m/\sqrt{\log m}$ with $K = 0.76422\ldots$, giving $|\Delta(P)| = \Theta(n/\sqrt{\log n})$.

## 3. History & State of the Art (SOTA)

- **1946** — Erdős, *On sets of distances of $n$ points*: introduces the problem, proves $g(n) \ge c\,n^{1/2}$ by a pigeonhole/circle argument, and gives the lattice upper bound.
- **1952** — Moser: $g(n) = \Omega(n^{2/3})$.
- **1984** — F. Chung: $\Omega(n^{5/7})$.
- **1992** — Chung, Szemerédi, Trotter: $\Omega(n^{4/5}/\log^c n)$, using incidence geometry.
- **1997** — Székely: $\Omega(n^{4/5})$ by the crossing-number method, removing logs.
- **2001** — Solymosi, Tóth: $\Omega(n^{6/7})$.
- **2003–2004** — Tardos ($n^{0.8641}$) and Katz–Tardos, reaching the exponent $\frac{48-14e}{55-16e} \approx 0.8641$ — the ceiling of the Solymosi–Tóth machinery.
- **2011** — Elekes, Sharir: rigid-motion reformulation turning the problem into a line-incidence question in $\mathbb{R}^3$.
- **2010/2015** — Guth, Katz: $g(n) \ge c\,n/\log n$ (arXiv 2010; *Annals of Mathematics* 181, 2015), via polynomial partitioning plus ruled-surface analysis. This is the SOTA lower bound; no improvement has been published since.
- **Higher dimensions** — Solymosi, Vu (2008): $g_d(n) = \Omega\!\big(n^{\frac{2}{d}-\frac{2}{d(d+2)}}\big)$, still the best general-$d$ bound; the conjectured truth is $\Theta(n^{2/d})$ (upper bound from the $d$-dimensional lattice, no log factor for $d \ge 3$).

## 4. Partial Results / Verified Cases

- **Planar general case:** $c\,n/\log n \le g(n) \le C\,n/\sqrt{\log n}$ — settled up to a factor $\sqrt{\log n}$.
- **Convex position:** Altman (1963) proved that $n$ points in convex position determine at least $\lfloor n/2 \rfloor$ distinct distances, tight for the regular $n$-gon. Erdős's stronger conjecture that some single point of a convex set sees $\lfloor n/2\rfloor$ distinct distances remains open.
- **Points on a line or circle:** trivially $n-1$ and $\lfloor n/2\rfloor$ distances respectively — far above $n/\sqrt{\log n}$, so extremal sets must be genuinely $2$-dimensional.
- **Structure of near-extremal sets:** Sheffer, Zahl, de Zeeuw (*Combinatorica* 36, 2016) proved that if $P$ determines $O(n/\sqrt{\log n})$ distances then no line contains $\Omega(n^{7/8})$ points of $P$ and no circle contains $\Omega(n^{5/6})$ points; the lattice has $O(\sqrt n)$ points per line, so a large gap remains.
- **Small $n$ (exact values):** the minimum number of distinct distances is known exactly by exhaustive/structural search for $n \le 8$ ($g(n) = 1,1,2,2,2,3,4,4$ for $n=2,\dots,9$ in the sequence of known small values); Erdős–Fishburn (*Discrete Math.* 160, 1996) determined the maximum $n$ admitting exactly $k$ distinct distances for $k \le 5$ and conjectured the extremal configurations are triangular-lattice sections.
- **Finite-field analogue:** over $\mathbb{F}_q^2$, Iosevich–Rudnev-type results give $|\Delta(E)| \gtrsim q$ for $|E| \ge C q^{3/2}$ (Erdős–Falconer problem); the conjectured threshold $|E| \gg q$ is open.
- **Pinned distances:** Katz–Tardos give a single point $p \in P$ with $\Omega(n^{0.8641})$ distinct distances to $P$; the Guth–Katz argument does *not* produce a pinned bound of the same strength.

## 5. Principal Obstacles

- **The $\log$ is intrinsic to the method.** Guth–Katz bound the number of $k$-rich points by $O(N^{3/2}/k^2)$ and then sum $\sum_k k^{-1}$-type contributions over dyadic ranges of multiplicity — a genuinely divergent harmonic sum. Removing it requires controlling the *joint distribution* of rich points rather than each richness level separately.
- **Cauchy–Schwarz is lossy.** The energy inequality $D \ge n^4/Q$ is tight only when all distance classes have equal size. In the lattice the class sizes are wildly unbalanced (the multiplicity of a distance $\sqrt m$ is $r_2(m)$, which fluctuates between $0$ and $m^{o(1)}$-large), so any purely energy-based argument cannot reach $n/\sqrt{\log n}$. One needs a higher-moment or entropy substitute that sees the number-theoretic distribution of $r_2$.
- **Polynomial partitioning is degree-limited.** The partitioning polynomial has degree $O(r^{1/3})$ in $\mathbb{R}^3$; points on the zero set must be handled separately using ruled-surface structure. Increasing the degree to sharpen the count destroys the cell-count balance, and the Cayley–Salmon flecnode machinery only classifies *doubly ruled* surfaces (planes and regular quadrics), which is exactly why those two families appear as hypotheses.
- **Fourier-analytic methods fail.** The distance set is not translation-invariant in a way that linearizes; the discrete analogue of Falconer's method loses because $\widehat{\sigma}$-decay arguments require a measure with dimensional regularity, absent for arbitrary $n$-point sets.
- **No structural rigidity theorem.** Proving $g(n) \ge n/\sqrt{\log n}$ plausibly needs "few distances $\Rightarrow$ lattice-like", but the only known route to such rigidity (arithmetic-combinatorial inverse theorems) has no working analogue for distance sets, where the relevant "sumset" lives in a non-abelian group of rigid motions.

## 6. The Gap

Proven: $g(n) \ge c\,n/\log n$ for an unspecified small constant $c$. Conjectured: $g(n) \ge c'\,n/\sqrt{\log n}$. The missing factor is $\sqrt{\log n}$, and the exact obstruction is the dyadic summation over richness levels in the Guth–Katz incidence bound: one must show that a point set achieving the maximum number of $k$-rich rigid motions for *one* value of $k$ cannot simultaneously do so across all $\log n$ scales. Equivalently, in energy language, one must upgrade $Q(P) = O(n^3\log n)$ to $Q(P) = O(n^3\sqrt{\log n})$ — and $n^3\log n$ is *correct* for the lattice, so the improvement cannot come from the energy bound at all; it must come from replacing Cauchy–Schwarz with an argument sensitive to the unevenness of distance multiplicities. In $\mathbb{R}^d$, $d\ge 3$, the gap is far larger: exponent $\frac{2}{d}-\frac{2}{d(d+2)}$ versus the conjectured $\frac{2}{d}$.

## 7. Current Research (as of June 2026)

- **Polynomial method extensions.** Guth's school (MIT) and collaborators continue to push polynomial partitioning into higher dimensions and to incidence problems with curves/varieties; the $d\ge 3$ distinct-distance bound is the flagship target. No improvement over Solymosi–Vu has been confirmed. *(frontier — verify)*
- **Structural / inverse results.** Sheffer, Zahl, de Zeeuw, Raz, Sharir and coauthors work on "few distances implies structure" statements, and on distinct distances between points and lines/curves, where sharper exponents are obtainable.
- **Pinned and bipartite variants.** Improving the pinned-distance exponent beyond $n^{0.8641}$ toward $n/\log n$ is an active and more tractable goal, since the Guth–Katz argument is inherently unpinned.
- **Finite-field and $p$-adic analogues.** Iosevich, Rudnev, Koh, Pham and others study Erdős–Falconer thresholds over $\mathbb{F}_q$; group-action and Rudnev's point–plane incidence theorem are the main tools.
- **Continuous counterpart.** Progress on the Falconer distance conjecture (Guth–Iosevich–Ou–Wang: $\dim_H E > 5/4$ implies positive-measure distance set in the plane) feeds techniques back into the discrete problem, though no transfer has yet closed the $\log$ gap. *(frontier — verify)*

## 8. Future Work

- Replace the Cauchy–Schwarz step by an entropy or higher-moment inequality that accounts for the distribution of distance multiplicities — Katz and Tardos's entropy method is the natural starting point.
- Prove a rigidity theorem: if $|\Delta(P)| = O(n/\sqrt{\log n})$ then $P$ contains a large lattice-like subset. Even a weak version would likely close the gap.
- Extend the Guth–Katz line theorem to a $d$-dimensional incidence theorem for $(d-2)$-flats or to the $6$-dimensional rigid-motion group of $\mathbb{R}^3$, targeting $g_3(n) = \Omega(n^{2/3})$.
- Determine the asymptotic constant: is $g(n)/(n/\sqrt{\log n})$ convergent, and is the value the Landau–Ramanujan constant?
- Settle Erdős's convex-position conjecture (a pinned $\lfloor n/2 \rfloor$ bound) and the Erdős–Fishburn extremal configurations for $k \ge 6$.

## 9. Key References

- **[Foundational]** P. Erdős. *On sets of distances of $n$ points.* American Mathematical Monthly 53 (1946), 248–250.
- **[Foundational]** L. Moser. *On the different distances determined by $n$ points.* American Mathematical Monthly 59 (1952), 85–91.
- **[Milestone]** F. R. K. Chung, E. Szemerédi, W. T. Trotter. *The number of different distances determined by a set of points in the Euclidean plane.* Discrete & Computational Geometry 7 (1992), 1–11.
- **[Milestone]** L. Székely. *Crossing numbers and hard Erdős problems in discrete geometry.* Combinatorics, Probability and Computing 6 (1997), 353–358.
- **[Milestone]** J. Solymosi, Cs. Tóth. *Distinct distances in the plane.* Discrete & Computational Geometry 25 (2001), 629–634.
- **[Milestone]** G. Tardos. *On distinct sums and distinct distances.* Advances in Mathematics 180 (2003), 275–289.
- **[Milestone]** N. H. Katz, G. Tardos. *A new entropy inequality for the Erdős distance problem.* Contemporary Mathematics 342 (2004), 119–126.
- **[Framework]** Gy. Elekes, M. Sharir. *Incidences in three dimensions and distinct distances in the plane.* Combinatorics, Probability and Computing 20 (2011), 571–608.
- **[SOTA]** L. Guth, N. H. Katz. *On the Erdős distinct distances problem in the plane.* Annals of Mathematics 181 (2015), 155–190.
- **[SOTA / higher dim.]** J. Solymosi, V. H. Vu. *Near optimal bounds for the Erdős distinct distances problem in high dimensions.* Combinatorica 28 (2008), 113–125.
- **[Structure]** A. Sheffer, J. Zahl, F. de Zeeuw. *Few distinct distances implies no heavy lines or circles.* Combinatorica 36 (2016), 349–364.
- **[Convex position]** E. Altman. *On a problem of P. Erdős.* American Mathematical Monthly 70 (1963), 148–157.
- **[Small cases]** P. Erdős, P. Fishburn. *Maximum planar sets that determine $k$ distances.* Discrete Mathematics 160 (1996), 115–125.
- **[Survey / Book]** L. Guth. *Polynomial Methods in Combinatorics.* AMS University Lecture Series 64, 2016.
- **[Survey / Book]** J. Garibaldi, A. Iosevich, S. Senger. *The Erdős Distance Problem.* AMS Student Mathematical Library 56, 2011.
- **[Survey / Book]** J. Pach, M. Sharir. *Combinatorial Geometry and Its Algorithmic Applications: The Alcalá Lectures.* AMS Mathematical Surveys and Monographs 152, 2009.

## 10. Worked Example / Concrete Special Case

**The $4\times 4$ lattice, $n = 16$.** Take $P = \{0,1,2,3\}^2$. Every squared distance has the form $i^2 + j^2$ with $0 \le i,j \le 3$, $(i,j) \neq (0,0)$. Enumerating the distinct values:

| $(i,j)$ | $(1,0)$ | $(1,1)$ | $(2,0)$ | $(2,1)$ | $(2,2)$ | $(3,0)$ | $(3,1)$ | $(3,2)$ | $(3,3)$ |
|---|---|---|---|---|---|---|---|---|---|
| $i^2+j^2$ | 1 | 2 | 4 | 5 | 8 | 9 | 10 | 13 | 18 |

So $|\Delta(P)| = 9$, out of $\binom{16}{2} = 120$ pairs — an average multiplicity of $13.3$. Compare the conjectured shape: $n/\sqrt{\log n} = 16/\sqrt{\ln 16} = 16/1.665 = 9.6$. The Guth–Katz bound $c\,n/\log n$ with its unspecified constant says nothing at this size; the example illustrates the *upper* side of the conjecture.

**Why the lattice is efficient.** Distances collapse because $i^2+j^2$ is highly non-injective: the value $25 = 5^2+0^2 = 4^2+3^2$ already has two representations, and by the multiplicativity of $r_2$ the number of representations grows on integers with many prime factors $\equiv 1 \pmod 4$. Scaling to $P = \{1,\dots,m\}^2$ with $n = m^2$: the distinct squared distances are exactly the integers in $[1, 2m^2]$ expressible as a sum of two squares, of which there are $\sim K\cdot 2m^2/\sqrt{\log(2m^2)} = \Theta(n/\sqrt{\log n})$ with $K = 0.76422\ldots$

**Contrast — a set with many distances.** For $P' = \{(2^k,0) : 1 \le k \le 16\}$, all pairwise distances $2^l - 2^k$ are distinct, giving $\binom{16}{2} = 120$ distances. Collinearity is maximally *inefficient*, matching the Sheffer–Zahl–de Zeeuw theorem: a near-extremal set cannot concentrate on a line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*