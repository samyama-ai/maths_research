---
id: 09-probability/harris-kesten-theorem-for-bond-percolation
title: "Harris-Kesten Theorem for Bond Percolation"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Harris-Kesten Theorem for Bond Percolation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/harris-kesten-theorem-for-bond-percolation` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let each edge of the square lattice $\mathbb{Z}^2$ be **open** with probability $p$ and **closed** with probability $1-p$, independently. Let $\theta(p)$ be the probability that the origin lies in an infinite open cluster, and let
$$p_c(\mathbb{Z}^2) = \sup\{p \in [0,1] : \theta(p) = 0\}.$$

**Harris–Kesten Theorem.** $p_c(\mathbb{Z}^2) = 1/2$, and $\theta(1/2) = 0$.

Equivalently: for $p \le 1/2$ every open cluster is almost surely finite; for $p > 1/2$ an infinite open cluster exists almost surely (and is unique). Harris (1960) supplied $\theta(1/2)=0$, hence $p_c \ge 1/2$; Kesten (1980) supplied $p_c \le 1/2$.

The theorem is **proved**. The page is catalogued as `solved-recently` in the sense that the surrounding programme — exact critical values off the self-dual family, critical behaviour in $3 \le d \le 10$, and continuity of $\theta$ at $p_c$ in intermediate dimensions — remains open, and the modern proofs (Bollobás–Riordan 2006; Duminil-Copin–Tassion 2016) are recent. A complete resolution of the open extensions would mean: an exact or provably-transcendental determination of $p_c$ for lattices without self-duality, and a proof that $\theta(p_c)=0$ for all $d \ge 2$.

## 2. Mathematical Foundations

**Model.** Let $\mathbb{E}^2$ be the edge set of $\mathbb{Z}^2$. The probability space is $(\Omega, \mathcal{F}, \mathbb{P}_p)$ with $\Omega = \{0,1\}^{\mathbb{E}^2}$, $\mathcal{F}$ the product $\sigma$-algebra, and $\mathbb{P}_p = \bigotimes_{e} \mu_p$, $\mu_p(1) = p$. Write $x \leftrightarrow y$ for "$x$ and $y$ are joined by an open path", $C_x = \{y : x \leftrightarrow y\}$, and
$$\theta(p) = \mathbb{P}_p(|C_0| = \infty), \qquad \chi(p) = \mathbb{E}_p|C_0|.$$
$\theta$ is non-decreasing (Harris coupling), so $p_c$ is well defined; Kolmogorov's zero–one law gives $\mathbb{P}_p(\exists \text{ infinite cluster}) \in \{0,1\}$.

**Planar duality.** The dual lattice $(\mathbb{Z}^2)^* = \mathbb{Z}^2 + (\tfrac12,\tfrac12)$ is isomorphic to $\mathbb{Z}^2$. Each edge $e$ crosses exactly one dual edge $e^*$; declare $e^*$ open iff $e$ is closed. Then the dual configuration is bond percolation at parameter $1-p$. The topological input is the **circuit lemma**: $C_0$ is finite iff there is a closed dual circuit surrounding the origin. Self-duality of $\mathbb{Z}^2$ at $p = 1/2$ is the source of the value $1/2$.

**Harris/FKG inequality.** For increasing events $A, B$,
$$\mathbb{P}_p(A \cap B) \ \ge \ \mathbb{P}_p(A)\,\mathbb{P}_p(B).$$

**Crossing events.** Let $H(m,n)$ be the event that the rectangle $[0,m]\times[0,n]$ is crossed left–right by an open path, $V(m,n)$ the top–bottom analogue. The **exact self-dual identity**
$$\mathbb{P}_{1/2}\big(H(n+1,n)\big) = \tfrac12$$
holds for every $n \ge 1$: either the rectangle is crossed horizontally by open edges, or its dual is crossed vertically by closed dual edges, exclusively and exhaustively, and the two events are related by the lattice symmetry $p \mapsto 1-p$ at $p=1/2$.

**Russo–Seymour–Welsh (RSW).** For each $k \ge 1$ there is $c_k>0$ with
$$\mathbb{P}_{1/2}\big(H(kn, n)\big) \ \ge \ c_k \qquad \text{for all } n,$$
i.e. crossings of rectangles of fixed aspect ratio have probabilities bounded away from $0$ and $1$ at criticality.

**Russo's formula.** For an increasing event $A$ depending on finitely many edges,
$$\frac{d}{dp}\mathbb{P}_p(A) \;=\; \sum_{e} \mathbb{P}_p\big(e \text{ is pivotal for } A\big).$$

**Sharpness of the phase transition** (Menshikov; Aizenman–Barsky; Duminil-Copin–Tassion): for $p < p_c$ there is $c(p)>0$ with $\mathbb{P}_p(0 \leftrightarrow \partial B_n) \le e^{-c n}$, and for $p>p_c$, $\theta(p) \ge c(p-p_c)$.

**Uniqueness** (Burton–Keane 1989): for every $p$, the infinite cluster is a.s. unique, by an ergodicity plus trifurcation-counting argument.

## 3. History & State of the Art (SOTA)

- **1957.** Broadbent and Hammersley introduce percolation as a model for fluid in a random medium and pose the determination of $p_c$.
- **1960.** Harris proves $\theta(1/2)=0$ using his positive-correlation inequality and a circuit/duality argument, giving $p_c \ge 1/2$. Numerical work had already suggested $1/2$.
- **1978.** Russo, and independently Seymour–Welsh, prove the RSW theorem, the central geometric tool of planar percolation.
- **1980.** Kesten proves $p_c \le 1/2$ by combining RSW with a pivotality/Russo-formula argument, closing the problem. Published in *Comm. Math. Phys.* 74.
- **1981.** Russo gives an alternative proof via his approximate zero–one law. Wierman computes $p_c$ for the triangular ($2\sin(\pi/18) \approx 0.3473$) and hexagonal ($1 - 2\sin(\pi/18)$) lattices using the star–triangle transformation.
- **1982.** Kesten's monograph *Percolation Theory for Mathematicians* consolidates the planar theory.
- **1986–1987.** Menshikov, and Aizenman–Barsky, prove sharpness in all dimensions.
- **2001.** Smirnov proves conformal invariance of crossing probabilities for **site** percolation on the triangular lattice, confirming Cardy's formula; with Lawler–Schramm–Werner this yields the critical exponents ($\theta(p) = (p-p_c)^{5/36+o(1)}$, one-arm exponent $5/48$) for that lattice.
- **2006.** Bollobás and Riordan give a short, self-contained proof of the full Harris–Kesten theorem (about six pages) using a sharp-threshold result of Friedgut–Kalai/Bourgain–Kahn–Kalai–Katznelson–Linial.
- **2016.** Duminil-Copin and Tassion give a proof of sharpness whose two-dimensional specialisation re-derives $p_c=1/2$ in a page.

## 4. Partial Results / Verified Cases

Exact critical values are known only in a short list of planar cases:

| Lattice / model | $p_c$ | Source |
|---|---|---|
| Bond, $\mathbb{Z}^2$ | $1/2$ | Harris 1960 + Kesten 1980 |
| Site, triangular | $1/2$ | Kesten 1982 (self-matching) |
| Bond, triangular | $2\sin(\pi/18)$ | Wierman 1981 |
| Bond, hexagonal | $1-2\sin(\pi/18)$ | Wierman 1981 |
| Bond, bow-tie and other self-dual families | algebraic | Wierman; Ziff |
| Bond, $\mathbb{Z}^2$ with FK/Ising weight $q\ge 1$ | $\sqrt{q}/(1+\sqrt{q})$ | Beffara–Duminil-Copin 2012 |

Beyond planarity: $\theta(p_c)=0$ is proved for $d=2$ (Harris) and for $d \ge 11$ via the lace expansion (Hara–Slade 1990 for $d \ge 19$; Fitzner–van der Hofstad 2017 down to $d \ge 11$), where mean-field exponents $\beta=\gamma=1$, $\delta=2$ also hold and $p_c(\mathbb{Z}^d) = \frac{1}{2d} + \frac{1}{(2d)^2} + \frac{7}{2}(2d)^{-3} + O((2d)^{-4})$ (Hara–Slade expansion). For $d \ge 2$ generally, sharpness, uniqueness, and $\theta$ continuity on $(p_c,1]$ are known. Numerically, $p_c(\mathbb{Z}^3) = 0.2488126\ldots$ and site-$\mathbb{Z}^2$ $p_c = 0.59274605\ldots$, both to nine or more digits by Monte Carlo, with no closed form conjectured.

## 5. Principal Obstacles

The theorem itself is closed; the obstacles concern everything adjacent to it.

- **Self-duality is a two-dimensional accident.** The identity $\mathbb{P}_{1/2}(H(n+1,n))=1/2$ has no analogue in $d \ge 3$, where the dual object is a random surface, not a path. Nothing pins $p_c(\mathbb{Z}^3)$ to an algebraic number, and no exact-solvability structure (Yang–Baxter, star–triangle) survives.
- **No duality for site percolation on $\mathbb{Z}^2$.** The matching lattice of $\mathbb{Z}^2$ (with diagonals) is not isomorphic to $\mathbb{Z}^2$, so the fixed point of $p \mapsto 1-p$ carries no meaning; $p_c \approx 0.5927$ is believed non-algebraic.
- **RSW needs symmetry.** Standard proofs use reflection and rotation invariance of the lattice plus FKG. Extending RSW to inhomogeneous or non-symmetric planar models required substantial new arguments (Tassion 2016).
- **The lace expansion needs a large parameter.** Its convergence requires the bubble diagram to be small, which holds only for $d$ large (currently $\ge 11$) or with spread-out ranges. It says nothing about $d=3$.
- **No renormalisation scheme in $3 \le d \le 10$.** Conformal-invariance techniques are intrinsically planar (SLE, discrete complex analysis); mean-field methods are intrinsically high-dimensional. The middle dimensions have neither, which is why $\theta(p_c)=0$ in $d=3$ is still open after 65 years.

## 6. The Gap

Proven: $p_c(\mathbb{Z}^2)=1/2$ with $\theta(1/2)=0$; exact values for the self-dual/star–triangle planar family; mean-field behaviour for $d \ge 11$.

Not proven: (i) $\theta(p_c)=0$ for $3 \le d \le 10$ — the single most-cited open problem descended from Harris–Kesten; (ii) any exact evaluation of $p_c$ outside the planar exactly-solvable list; (iii) conformal invariance of critical **bond** percolation on $\mathbb{Z}^2$ (Smirnov's proof is specific to the triangular site model, where the colour-swap symmetry of the hexagonal tiling is used); (iv) universality — that bond-$\mathbb{Z}^2$ has the same exponents ($5/36$, $5/48$, $43/18$) as site-triangular. The exact step needed for (i) is a proof that the one-arm probability $\mathbb{P}_{p_c}(0 \leftrightarrow \partial B_n)$ tends to $0$ in $d=3$, for which no mechanism — neither duality nor diagrammatic bound — is currently available.

## 7. Current Research (as of June 2026)

- **Geneva school (Duminil-Copin and collaborators).** Randomised-algorithm and OSSS-inequality proofs of sharpness, extended to dependent models (random-cluster, Ising, Voronoi, Poisson-Boolean). Ongoing work on RSW without symmetry assumptions and on continuity of the phase transition for FK models with $1 \le q \le 4$.
- **Universality of planar percolation.** Efforts to prove conformal invariance for bond-$\mathbb{Z}^2$ via discrete holomorphic observables or via Cardy's formula transported by coupling. Still unresolved *(frontier — verify)*.
- **Lace expansion at lower $d$.** Fitzner–van der Hofstad's non-backtracking expansion reached $d \ge 11$; incremental improvements toward $d \ge 7$ are announced but not published *(frontier — verify)*.
- **$d=3$ critical exponents.** Conformal-bootstrap and rigorous-numerics estimates for 3D percolation ($\beta \approx 0.4181$) sit outside rigorous reach; several groups (IHES, Cambridge, Kyoto) probe whether reflection positivity or a Ward-type identity could constrain them.
- **Boolean-function methods.** Sharp-threshold and noise-sensitivity technology (Kalai, Schramm, Steif; Garban–Steif's monograph) continues to yield quantitative versions of Kesten's argument, including scaling limits of the near-critical and dynamical models.

## 8. Future Work

- Prove $\theta(p_c)=0$ in $d=3$; a proposed route is to establish a suitable "finite-size criterion" plus a supercritical-surface (Wulff) estimate strong enough to exclude an infinite cluster at $p_c$.
- Transport Smirnov's conformal invariance from the triangular site model to bond-$\mathbb{Z}^2$, which would give universality of planar critical exponents.
- Extend RSW to lattices with only a discrete symmetry group, completing a general planar theory of $p_c$ for all doubly-periodic graphs.
- Sharpen the lace-expansion threshold below $d=11$, or find a non-perturbative substitute valid for $d \ge 7$.
- Determine whether $p_c(\mathbb{Z}^3)$ is algebraic; no obstruction or proof strategy is known.

## 9. Key References

- **[Foundational]** S. R. Broadbent and J. M. Hammersley. *Percolation processes I. Crystals and mazes.* Mathematical Proceedings of the Cambridge Philosophical Society **53** (1957), 629–641.
- **[Foundational]** T. E. Harris. *A lower bound for the critical probability in a certain percolation process.* Mathematical Proceedings of the Cambridge Philosophical Society **56** (1960), 13–20.
- **[Foundational]** H. Kesten. *The critical probability of bond percolation on the square lattice equals 1/2.* Communications in Mathematical Physics **74** (1980), 41–59.
- **[Foundational]** L. Russo. *A note on percolation.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete **43** (1978), 39–48.
- **[Foundational]** P. D. Seymour and D. J. A. Welsh. *Percolation probabilities on the square lattice.* Annals of Discrete Mathematics **3** (1978), 227–245.
- **[SOTA / Recent]** B. Bollobás and O. Riordan. *A short proof of the Harris–Kesten theorem.* Bulletin of the London Mathematical Society **38** (2006), 470–484.
- **[SOTA / Recent]** H. Duminil-Copin and V. Tassion. *A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model.* Communications in Mathematical Physics **343** (2016), 725–745.
- **[SOTA / Recent]** V. Beffara and H. Duminil-Copin. *The self-dual point of the two-dimensional random-cluster model is critical for $q \ge 1$.* Probability Theory and Related Fields **153** (2012), 511–542.
- **[SOTA / Recent]** R. Fitzner and R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electronic Journal of Probability **22** (2017), paper 43.
- **[SOTA / Recent]** S. Smirnov. *Critical percolation in the plane: conformal invariance, Cardy's formula, scaling limits.* Comptes Rendus de l'Académie des Sciences, Série I **333** (2001), 239–244.
- **[Survey]** G. Grimmett. *Percolation.* 2nd edition, Grundlehren der mathematischen Wissenschaften **321**, Springer, 1999.
- **[Survey]** B. Bollobás and O. Riordan. *Percolation.* Cambridge University Press, 2006.
- **[Survey]** H. Kesten. *Percolation Theory for Mathematicians.* Birkhäuser, 1982.
- **[Survey]** C. Garban and J. E. Steif. *Noise Sensitivity of Boolean Functions and Percolation.* Cambridge University Press, 2014.
- **[Related]** R. M. Burton and M. Keane. *Density and uniqueness in percolation.* Communications in Mathematical Physics **121** (1989), 501–505.

## 10. Worked Example / Concrete Special Case

**The exact self-dual crossing identity, computed on a small rectangle.**

Take the rectangle $R = [0,2] \times [0,1]$ in $\mathbb{Z}^2$: vertices $(i,j)$ with $i \in \{0,1,2\}$, $j\in\{0,1\}$. Its edges are 4 horizontal ($(0,0)$–$(1,0)$, $(1,0)$–$(2,0)$, and the two at height 1) and 3 vertical, so 7 edges. Let $H$ be the event of an open left–right crossing.

*Duality set-up.* Place the dual rectangle $R^* = [\tfrac12, \tfrac32] \times [-\tfrac12, \tfrac32]$, a $1 \times 2$ dual rectangle rotated $90°$ relative to $R$. Every edge of $R$ crosses exactly one dual edge of $R^*$. The planar-topology fact is:
$$H \text{ fails} \iff R^* \text{ has a top–bottom crossing of closed dual edges}.$$
A left–right open path in $R$ and a top–bottom closed dual path in $R^*$ cannot coexist (they would have to cross at an edge that is both open and closed), and one must occur.

*The computation.* At $p=1/2$ each edge is open or closed with probability $1/2$, so the closed-edge process is itself Bernoulli($1/2$). Since $R^*$ is $R$ rotated by $90°$ and the lattice is invariant under that rotation,
$$\mathbb{P}_{1/2}\big(V^*(R^*)\big) = \mathbb{P}_{1/2}\big(H(R)\big).$$
Combining with $\mathbb{P}_{1/2}(H) + \mathbb{P}_{1/2}(V^*) = 1$ gives
$$\mathbb{P}_{1/2}(H) = \tfrac12,$$
exactly, for every $n$ in the family $H(n+1,n)$.

*Sanity check by enumeration.* Label the horizontal edges $h_1,h_2$ (bottom row), $h_3,h_4$ (top row), and the verticals $v_0,v_1,v_2$ at $x=0,1,2$. A crossing exists iff one of: $\{h_1,h_2\}$ both open; $\{h_3,h_4\}$ both open; $\{h_1, v_1, h_4\}$ open; $\{h_3, v_1, h_2\}$ open; $\{v_0,h_3,h_4\}$; $\{h_1,h_2\}$ via $v_2$; etc. Direct enumeration of the $2^7=128$ configurations gives exactly $64$ crossing configurations, i.e. probability $64/128 = 1/2$, matching the duality argument with no calculation.

*Why this yields the theorem.* Harris's half: if $\theta(1/2)>0$, FKG plus the $1/2$-crossing bound would force, with positive probability, four infinite open arms and a blocking closed dual circuit simultaneously — a contradiction; hence $\theta(1/2)=0$ and $p_c\ge 1/2$. Kesten's half: for $p>1/2$, RSW gives $\mathbb{P}_{1/2}(H(3n,n)) \ge c > 0$, and Russo's formula shows the pivotal count grows fast enough that $\mathbb{P}_p(H(3n,n)) \to 1$ for any fixed $p>1/2$; a renormalisation over dyadic annuli then produces an infinite cluster, so $p_c \le 1/2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*