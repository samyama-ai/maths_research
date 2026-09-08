---
id: 07-combinatorics/chromatic-number-euclidean-space-dimension-n
title: "Chromatic Number of the Plane for Higher Dimensions"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chromatic Number of the Plane for Higher Dimensions

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/chromatic-number-euclidean-space-dimension-n` · **Status:** open

## 1. Problem Statement / Conjecture

For $n \ge 2$, let $G(\mathbb{R}^n)$ be the **unit-distance graph** on $\mathbb{R}^n$: vertex set $\mathbb{R}^n$, with $x \sim y$ iff $\|x-y\|_2 = 1$. The **chromatic number of $n$-space** is
$$\chi(\mathbb{R}^n) \;=\; \chi\big(G(\mathbb{R}^n)\big) \;=\; \min\{k : \exists\, c:\mathbb{R}^n \to [k],\ \|x-y\|=1 \Rightarrow c(x)\neq c(y)\}.$$

**The problem.** Determine $\chi(\mathbb{R}^n)$ exactly for every $n$, and determine the growth rate of $\chi(\mathbb{R}^n)$ as $n \to \infty$.

No value is known for any $n \ge 2$. The Hadwiger–Nelson problem is the case $n=2$, where $5 \le \chi(\mathbb{R}^2) \le 7$. A complete solution in dimension $n$ requires:

1. a **lower bound**: an explicit finite unit-distance graph $H \subset \mathbb{R}^n$ with $\chi(H) = k$, together with
2. a **matching upper bound**: an explicit $k$-colouring of all of $\mathbb{R}^n$ with no monochromatic unit pair.

The asymptotic question is whether $\chi(\mathbb{R}^n) = (c+o(1))^n$ for some constant $c$, and what $c$ is; currently $1.239 \le c \le 3$ is all that is known.

Variants that must be distinguished: the **measurable** chromatic number $\chi_m(\mathbb{R}^n)$ (colour classes Lebesgue measurable), the **polychromatic**/Borel variants, and $\chi(\mathbb{Q}^n)$, $\chi(\mathbb{Z}^n)$ over rational and integer points.

## 2. Mathematical Foundations

**Scale invariance.** The choice of distance $1$ is immaterial: $x \mapsto \lambda x$ is a graph isomorphism $G_1 \to G_\lambda$, so $\chi$ depends only on $n$.

**Compactness (de Bruijn–Erdős).** Assuming the axiom of choice, an infinite graph is $k$-colourable iff every finite subgraph is. Hence
$$\chi(\mathbb{R}^n) \;=\; \sup\{\chi(H) : H \subseteq G(\mathbb{R}^n),\ |V(H)| < \infty\},$$
which reduces lower bounds to finite combinatorics and makes SAT/ILP search meaningful. This step is not ZF-provable: Shelah–Soifer exhibit models of ZF+DC where a related graph on $\mathbb{R}$ has finite-chromatic finite subgraphs but uncountable chromatic number.

**Elementary bounds.** A regular unit simplex on $n+1$ points is a clique, so $\chi(\mathbb{R}^n) \ge n+1$; spindling arguments give $\chi(\mathbb{R}^n)\ge n+2$ for small $n$. Tiling $\mathbb{R}^n$ by suitably scaled cubes of a lattice with a shifted colouring gives finite upper bounds; Larman and Rogers made this efficient:
$$\chi(\mathbb{R}^n) \;\le\; (3+o(1))^n .$$

**Frankl–Wilson mechanism.** Take $p$ prime and vertices $\{0,1\}$-vectors of weight $2p$ in $\mathbb{R}^{4p}$. Two such vectors at Hamming intersection $p$ are at a fixed Euclidean distance. The Frankl–Wilson modular Ray-Chaudhuri–Wilson inequality bounds any set system avoiding intersection $\equiv p \pmod p$ by $\binom{4p}{p-1}$, so each colour class of the corresponding distance graph is small, giving
$$\chi(\mathbb{R}^n) \;\ge\; \binom{4p}{2p}\Big/\binom{4p}{p-1} \;=\; (1.207\ldots + o(1))^n .$$
Raigorodskii replaced $\{0,1\}$-vectors by $\{-1,0,1\}$-vectors and optimised the weight profile, obtaining
$$\chi(\mathbb{R}^n) \;\ge\; (1.239\ldots + o(1))^n .$$

**Measurable/LP relaxation.** Let $m_1(\mathbb{R}^n)$ be the supremum upper density of a Lebesgue-measurable set avoiding distance $1$. Then
$$\chi_m(\mathbb{R}^n) \;\ge\; 1/m_1(\mathbb{R}^n).$$
Fourier analysis bounds $m_1$: for any positive-definite $f$ with $\hat f \ge 0$ supported so that $f(x)\le 0$ on the unit sphere, an averaging (Delsarte/Lovász theta) argument caps $m_1$. This is how $m_1(\mathbb{R}^2) \le 0.2544$ and later $\le 0.247$ were obtained, giving $\chi_m(\mathbb{R}^2)\ge 5$.

## 3. History & State of the Art (SOTA)

- **1950.** Edward Nelson asks for $\chi(\mathbb{R}^2)$; John Isbell finds the 7-colouring by a hexagonal tiling of diameter $<1$. The Moser brothers' spindle (1961) gives $\chi(\mathbb{R}^2)\ge 4$, which stood for 57 years.
- **1972.** Larman and Rogers give the general exponential upper bound $(3+o(1))^n$ and the first systematic small-dimensional bounds, including $\chi(\mathbb{R}^3)\le 27$ and lower bounds for $\chi(\mathbb{R}^n)$.
- **1981.** Frankl and Wilson: $\chi(\mathbb{R}^n)$ grows exponentially — the single most important structural result. Falconer, the same year, proves $\chi_m(\mathbb{R}^2)\ge 5$.
- **2000.** Raigorodskii improves the exponential base to $1.239$.
- **2002–03.** Coulson constructs a 15-colouring of $\mathbb{R}^3$; Radoičić and Tóth give a second proof. Nechushtan proves $\chi(\mathbb{R}^3)\ge 6$.
- **2014–18.** Exoo and Ismailescu, then Cherkashin, Kulikov and Raigorodskii, push small-dimensional lower bounds: $\chi(\mathbb{R}^4)\ge 9$, $\chi(\mathbb{R}^5)\ge 9$, $\chi(\mathbb{R}^6)\ge 11$, $\chi(\mathbb{R}^7)\ge 15$.
- **April 2018.** Aubrey de Grey exhibits a 5-chromatic unit-distance graph on 1581 vertices: $\chi(\mathbb{R}^2)\ge 5$. Polymath16 and Heule's SAT machinery reduce the certificate to 509 vertices.
- **2023.** Ambrus, Csiszárik, Matolcsi, Varga and Zsámboki improve $m_1(\mathbb{R}^2)\le 0.2470$ by a computer-assisted Fourier/LP argument.

Current state, small dimensions:

| $n$ | lower | upper |
|---|---|---|
| 2 | 5 | 7 |
| 3 | 6 | 15 |
| 4 | 9 | $\le 54$ (lattice colouring) |
| 5 | 9 | $\le 3^5$-type bounds |
| 6 | 11 | — |
| 7 | 15 | — |

## 4. Partial Results / Verified Cases

- **Exponential growth is settled qualitatively.** $1.239^n \lesssim \chi(\mathbb{R}^n) \lesssim 3^n$ (Frankl–Wilson; Raigorodskii; Larman–Rogers).
- **$n=2$:** $\chi(\mathbb{R}^2) \in \{5,6,7\}$. Verified by two independent 5-chromatic constructions (de Grey; Exoo–Ismailescu) and by formally checked SAT certificates on 509 vertices.
- **$n=3$:** $6 \le \chi(\mathbb{R}^3)\le 15$; the lower bound is a finite explicit graph (Nechushtan), the upper bound an explicit periodic partition (Coulson).
- **Rational spaces — solved.** Benda and Perles: $\chi(\mathbb{Q}^2)=\chi(\mathbb{Q}^3)=2$, $\chi(\mathbb{Q}^4)=4$. So the difficulty is genuinely about irrational coordinates.
- **Spheres.** For the sphere $S^{n-1}_r$ of radius $r>1/2$, Lovász and later Raigorodskii give exponential lower bounds; for $r$ slightly above $1/2$, $\chi(S^{n-1}_r)\ge n+1$ exactly matches a simplex.
- **Measurable case, $n=2$:** $\chi_m(\mathbb{R}^2)\ge 5$ (Falconer, 1981) — proven 37 years before the combinatorial analogue — and $m_1(\mathbb{R}^2)\le 0.2470$.
- **Other norms.** For many polytopal norms the chromatic number of the plane is exactly 4, showing the Euclidean difficulty is metric-specific.

## 5. Principal Obstacles

- **Upper bounds are constructions, and constructions are scarce.** Every known upper bound comes from an explicit periodic tiling. In $\mathbb{R}^2$ the hexagonal tiling gives 7; no one has produced a 6-colouring, and no argument rules one out. In $\mathbb{R}^n$, $n\ge 3$, the tilings degrade fast: the ratio (inradius)/(diameter) of good space-filling cells decays, forcing exponentially many colours, and no candidate polytope is known to be optimal.
- **Fourier/LP methods bound only the measurable chromatic number.** The Delsarte-type LP and the Lovász theta relaxation of $G(\mathbb{R}^n)$ are inherently about densities of measurable sets. Non-measurable colourings — which de Bruijn–Erdős licenses via choice — are invisible to them, so an LP bound of $1/m_1$ can never certify $\chi$ beyond $\chi_m$, and the two may differ.
- **Frankl–Wilson is lossy.** It bounds independence number in a *specific* $\{0,1\}$/$\{-1,0,1\}$ subgraph, not in $G(\mathbb{R}^n)$. The independence-ratio estimate loses a constant factor in the exponent base at each step; pushing $1.239$ toward the conjectured true base looks to require a genuinely new intersection theorem, not a sharper counting of the same family.
- **Search complexity.** Lower bounds in $\mathbb{R}^n$ for $n\ge 4$ come from spindling and SAT search over graphs whose vertex sets live in high-dimensional algebraic point configurations; the number of candidate configurations grows super-exponentially, and SAT instances for a hypothetical 6-chromatic planar unit-distance graph already exceed current solver reach (Polymath16 estimated the required vertex count in the tens of thousands).
- **No topological or algebraic invariant** is known to obstruct a $k$-colouring of $\mathbb{R}^n$; unlike map colouring there is no Euler-characteristic or minor-theoretic handle, since $G(\mathbb{R}^2)$ contains $K_4$-subdivisions densely and is far from planar.

## 6. The Gap

For $n=2$ the gap is the two-element set $\{6,7\}$: either build a 6-colouring of the plane (necessarily with non-tiling, plausibly non-measurable, colour classes) or find a 6-chromatic finite unit-distance graph. For $n=3$ the gap is $\{7,\dots,15\}$ — nine values, and unlike the plane neither end is believed tight. For $n\ge 4$ the gap is a multiplicative factor growing with $n$.

Asymptotically the gap is the interval $[1.239, 3]$ for the exponential base $c$, and even the *existence* of $\lim_n \chi(\mathbb{R}^n)^{1/n}$ is unproven — it is not known that the sequence is submultiplicative in a usable way (the product construction gives $\chi(\mathbb{R}^{m+n}) \le \chi(\mathbb{R}^m)\chi(\mathbb{R}^n)$ only under extra care with the cross terms, since a unit in $\mathbb{R}^{m+n}$ need not project to a unit in either factor). Closing the gap requires either a new independent-set upper bound valid for arbitrary (non-measurable) colour classes, or a genuinely new colouring scheme beating tilings.

## 7. Current Research (as of June 2026)

- **Polymath16 legacy and SAT.** Marijn Heule's group (Carnegie Mellon) continues to push automated search for unit-distance graphs with high chromatic number, including verified DRAT proofs of 5-chromaticity. Work on 6-chromatic candidates in the plane and on 7-chromatic graphs in $\mathbb{R}^3$ is ongoing. *(frontier — verify)*
- **Moscow school (Raigorodskii and students).** Distance graphs, graphs of diameters, and random-graph-flavoured lower bounds for $\chi(\mathbb{R}^n)$ and $\chi(\mathbb{Q}^n)$; incremental improvements to small-dimensional lower bounds.
- **Fourier/SDP programme.** Bachoc, Oliveira Filho, Vallentin and collaborators refine hierarchies bounding $m_1(\mathbb{R}^n)$ and $\chi_m(\mathbb{R}^n)$; the 2023 Ambrus et al. bound $m_1(\mathbb{R}^2)\le 0.2470$ is the current benchmark, with the natural target being $<1/5$, which would give $\chi_m(\mathbb{R}^2)\ge 6$. *(frontier — verify)*
- **Set-theoretic side.** Continued study, following Shelah–Soifer, of how $\chi(\mathbb{R}^n)$ depends on the axiom system — including models where measurable and general chromatic numbers provably differ.
- **Exoo–Ismailescu style geometric search** for higher-dimensional spindles, aiming at $\chi(\mathbb{R}^4)\ge 10$ and improved bounds for $n=5,6$. *(frontier — verify)*

## 8. Future Work

- Prove $m_1(\mathbb{R}^2) < 1/5$, giving $\chi_m(\mathbb{R}^2) \ge 6$ and separating the measurable problem from the current combinatorial bound.
- Establish or refute the existence of $\lim \chi(\mathbb{R}^n)^{1/n}$; Erdős-style, most experts expect the truth is near the Frankl–Wilson side, i.e. $c$ well below 3.
- Improve the upper bound $\chi(\mathbb{R}^3)\le 15$; even 12 or 13 would be the first movement since 2002.
- Develop a lower-bound technique insensitive to measurability that still exploits Fourier structure — the central methodological ask of the field.
- Systematise spindling in $\mathbb{R}^n$: a general theorem converting a $k$-chromatic graph in $\mathbb{R}^n$ into a $(k+1)$-chromatic graph in $\mathbb{R}^{n+1}$ would immediately propagate the de Grey bound upward.

## 9. Key References

- **[Foundational]** D. G. Larman and C. A. Rogers. *The realization of distances within sets in Euclidean space.* Mathematika 19 (1972), 1–24.
- **[Foundational]** P. Frankl and R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1 (1981), 357–368.
- **[Foundational]** K. J. Falconer. *The realization of distances in measurable subsets covering $\mathbb{R}^n$.* Journal of Combinatorial Theory, Series A 31 (1981), 184–189.
- **[Foundational]** N. G. de Bruijn and P. Erdős. *A colour problem for infinite graphs and a problem in the theory of relations.* Indagationes Mathematicae 13 (1951), 369–373.
- **[SOTA]** A. D. N. J. de Grey. *The chromatic number of the plane is at least 5.* Geombinatorics 28 (2018), 18–31.
- **[SOTA]** G. Exoo and D. Ismailescu. *The chromatic number of the plane is at least 5: a new proof.* Discrete & Computational Geometry 64 (2020), 216–226.
- **[SOTA]** D. Coulson. *A 15-colouring of 3-space omitting distance one.* Discrete Mathematics 256 (2002), 83–90.
- **[SOTA]** O. Nechushtan. *On the space chromatic number.* Discrete Mathematics 256 (2002), 499–507.
- **[SOTA]** A. M. Raigorodskii. *On the chromatic number of a space.* Russian Mathematical Surveys 55 (2000), 351–352.
- **[SOTA]** D. Cherkashin, A. Kulikov and A. Raigorodskii. *On the chromatic numbers of small-dimensional Euclidean spaces.* Discrete Applied Mathematics 243 (2018), 125–131.
- **[SOTA]** G. Ambrus, A. Csiszárik, M. Matolcsi, D. Varga and P. Zsámboki. *The density of planar sets avoiding unit distances.* Mathematical Programming (2023).
- **[Survey]** A. Soifer. *The Mathematical Coloring Book.* Springer, 2009.
- **[Survey]** A. M. Raigorodskii. *Coloring Distance Graphs and Graphs of Diameters.* In: Thirty Essays on Geometric Graph Theory, Springer, 2013, 429–460.
- **[Survey]** C. Bachoc, F. M. de Oliveira Filho and A. Vallentin. *The independence number of graphs on Euclidean spaces.* (Delsarte-LP framework; see also Bachoc–Passuello–Thiery, Discrete & Computational Geometry 53 (2015), 783–808.)

## 10. Worked Example / Concrete Special Case

**The Moser spindle: $\chi(\mathbb{R}^2)\ge 4$, computed explicitly.**

Build two unit rhombi. Start with the unit equilateral triangles $ABC$ and $ACD$ sharing edge $AC$, so $A,B,C,D$ form a rhombus with $|AB|=|BC|=|CA|=|AD|=|DC|=1$ and $|BD|=\sqrt{3}$. Concretely
$$A=(0,0),\quad B=\left(\tfrac12,\tfrac{\sqrt3}{2}\right),\quad C=(1,0),\quad D=\left(\tfrac12,-\tfrac{\sqrt3}{2}\right).$$

*Step 1 (rhombus lemma).* In any proper colouring, $B$ and $D$ are the two vertices of the rhombus not adjacent to each other but both adjacent to $A$ and $C$. With 3 colours, $A,B,C$ is a triangle and uses all three; $D$ is adjacent to $A$ and $C$, so $c(D)=c(B)$. **Conclusion: in any 3-colouring, the two rhombus tips at distance $\sqrt3$ get the same colour.**

*Step 2 (spindle).* Take a second copy of the rhombus, rotated about $A$ by the angle $\theta$ chosen so that the two far tips $D$ and $D'$ are at distance exactly $1$. The far tips lie at distance $\sqrt3$ from $A$; choosing $\theta$ with
$$2\sqrt3\,\sin(\theta/2)=1 \quad\Longrightarrow\quad \theta = 2\arcsin\!\left(\tfrac{1}{2\sqrt3}\right)\approx 33.557^\circ,$$
gives $|DD'|=1$. The union has $7$ vertices and $11$ edges.

*Step 3 (contradiction).* Suppose a 3-colouring exists. By Step 1 applied to each rhombus, $c(D)=c(A)$ and $c(D')=c(A)$ — the tip opposite $A$ shares $A$'s colour. Hence $c(D)=c(D')$. But $|DD'|=1$, so $D\sim D'$ and $c(D)\neq c(D')$. Contradiction. Therefore $\chi(\mathbb{R}^2)\ge 4$.

**Lifting to $\mathbb{R}^n$.** The same two ingredients — a rigid gadget forcing two points at distance $d$ to share a colour, then a rotation setting $d$-apart copies at distance 1 — are exactly what Nechushtan iterates in $\mathbb{R}^3$ (obtaining $\ge 6$) and what de Grey automates in the plane with 1581 vertices (obtaining $\ge 5$). The obstacle in Section 5 is visible here: each spindling step needs a *new* rigid gadget whose forced-monochromatic distance $d$ is realisable by a rotation, and in dimension $n\ge 4$ the space of such configurations is searched only heuristically. Meanwhile the Isbell 7-colouring — tile the plane by regular hexagons of diameter $0.99$, colour by a $7$-cell pattern so that same-coloured hexagons have centres at distance $>1$ apart — remains the only known upper-bound idea, and its $n$-dimensional analogues are what give the weak $3^n$ ceiling.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*