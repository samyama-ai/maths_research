---
id: 09-probability/kesten-percolation-threshold-theorem
title: "Kesten Percolation Threshold Theorem"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kesten Percolation Threshold Theorem

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/kesten-percolation-threshold-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Consider Bernoulli bond percolation on the square lattice $\mathbb{Z}^2$: each nearest-neighbour edge is independently **open** with probability $p$ and **closed** with probability $1-p$. Let $\theta(p)$ be the probability that the origin lies in an infinite open cluster, and let
$$p_c = \sup\{p \in [0,1] : \theta(p) = 0\}.$$

**Kesten's theorem (1980).** $p_c(\mathbb{Z}^2, \text{bond}) = \tfrac12$, and moreover $\theta(1/2) = 0$: there is almost surely no infinite open cluster at the critical point.

This settled a conjecture standing since the 1950s (Hammersley; Sykes–Essam). The problem is **solved** for this lattice; the catalog entry tracks it because the natural generalisations remain wide open. Specifically:

- (a) Compute $p_c(\mathbb{Z}^d)$ for $d \ge 3$ in closed form, or prove no closed form exists. No value of $p_c(\mathbb{Z}^d)$, $d\ge 3$, is known even to be irrational or algebraic.
- (b) Prove $\theta(p_c) = 0$ in all dimensions $3 \le d \le 10$ (the "no percolation at criticality" conjecture).
- (c) Prove universality: that the exact threshold $1/2$ and the critical exponents at $p_c$ do not depend on lattice details beyond dimension.

A complete resolution of (b) requires, for each fixed $d$, a proof that $\mathbb{P}_{p_c}(|C_0| = \infty) = 0$ where $C_0$ is the cluster of the origin. A resolution of (a) would require either an exact evaluation or a proof of transcendence/non-algebraicity.

## 2. Mathematical Foundations

**Probability space.** Let $\mathbb{E}^d$ be the edge set of $\mathbb{Z}^d$. Take $\Omega = \{0,1\}^{\mathbb{E}^d}$ with the product $\sigma$-algebra $\mathcal{F}$ and product measure $\mathbb{P}_p = \prod_e \mathrm{Bernoulli}(p)$. Write $C_x$ for the open cluster of $x$ and
$$\theta(p) = \mathbb{P}_p(|C_0| = \infty), \qquad \chi(p) = \mathbb{E}_p|C_0|.$$
$\theta$ is non-decreasing (Harris coupling), so $p_c$ is well defined, and by ergodicity of $\mathbb{P}_p$ under lattice translations plus the Burton–Keane argument the infinite cluster, when it exists, is a.s. unique.

**Planar duality.** For $\mathbb{Z}^2$, the dual lattice $(\mathbb{Z}^2)^* = \mathbb{Z}^2 + (\tfrac12,\tfrac12)$ has each dual edge $e^*$ crossing exactly one primal edge $e$; declare $e^*$ open iff $e$ is closed. Then the dual configuration is Bernoulli$(1-p)$, and
$$\text{no open left–right crossing of a rectangle} \iff \text{a closed dual top–bottom crossing}.$$
At $p=1/2$ the model is **self-dual**.

**Harris–FKG inequality.** For increasing events $A, B$,
$$\mathbb{P}_p(A \cap B) \ge \mathbb{P}_p(A)\,\mathbb{P}_p(B).$$

**Russo's formula.** For an increasing event $A$ depending on finitely many edges,
$$\frac{d}{dp}\mathbb{P}_p(A) = \sum_e \mathbb{P}_p(e \text{ is pivotal for } A).$$

**RSW crossing estimates.** Let $\mathrm{Cross}(m,n)$ be the event of an open left–right crossing of an $m \times n$ rectangle. Russo (1978) and Seymour–Welsh (1978) proved: for each $\kappa > 1$ there is $c(\kappa) > 0$ with
$$\mathbb{P}_{1/2}\big(\mathrm{Cross}(\kappa n, n)\big) \ge c(\kappa) \quad \text{for all } n \ge 1.$$
This "box-crossing property" is the engine of the planar theory.

**Sharpness of the phase transition.** For $p < p_c$ there is $c_p > 0$ with $\mathbb{P}_p(0 \leftrightarrow \partial B_n) \le e^{-c_p n}$, and $\chi(p) < \infty$ (Menshikov 1986; Aizenman–Barsky 1987; short proof by Duminil-Copin–Tassion 2016). Kesten's original argument produced sharpness in $d=2$ as a by-product.

**Mean-field regime.** For $d$ large, the triangle condition
$$\nabla(p_c) = \sum_{x,y} \tau_{p_c}(0,x)\,\tau_{p_c}(x,y)\,\tau_{p_c}(y,0) < \infty, \qquad \tau_p(x,y) = \mathbb{P}_p(x \leftrightarrow y),$$
implies $\theta(p_c)=0$ and mean-field exponents $\beta = \gamma = 1$, $\delta = 2$ (Aizenman–Newman; Barsky–Aizenman; Nguyen).

## 3. History & State of the Art (SOTA)

- **1957.** Broadbent and Hammersley introduce percolation; existence of a nontrivial $p_c \in (0,1)$ for $\mathbb{Z}^d$, $d \ge 2$.
- **1960.** Harris proves $\theta(1/2) = 0$ on $\mathbb{Z}^2$, hence $p_c \ge 1/2$, using the correlation inequality now bearing his name.
- **1964.** Sykes and Essam give a non-rigorous "matching lattice" derivation of $p_c = 1/2$ assuming a single phase transition.
- **1978.** Russo, and independently Seymour–Welsh, prove the RSW crossing lemma.
- **1980.** Kesten proves $p_c = 1/2$ (Comm. Math. Phys. **74**, 41–59), combining RSW, Russo's formula and a careful pivotality/finite-size scaling argument to get the matching upper bound.
- **1982.** Kesten's monograph *Percolation Theory for Mathematicians* consolidates the planar theory; also establishes $p_c^{\text{site}}(\text{triangular}) = 1/2$ and, with the star–triangle transformation, $p_c^{\text{bond}}(\text{triangular}) = 2\sin(\pi/18)$.
- **1986–87.** Menshikov, Aizenman–Barsky: sharpness in all dimensions.
- **1990.** Hara and Slade: lace expansion gives mean-field behaviour and $\theta(p_c) = 0$ for $d \ge 19$.
- **2001.** Smirnov proves conformal invariance and Cardy's formula for critical site percolation on the triangular lattice; with Lawler–Schramm–Werner this yields the exact exponents $\beta = 5/36$, $\nu = 4/3$, one-arm exponent $5/48$.
- **2006.** Bollobás–Riordan: $p_c = 1/2$ for random Voronoi percolation in the plane — the first genuinely non-lattice analogue of Kesten's theorem.
- **2017.** Fitzner–van der Hofstad reduce the mean-field threshold to $d \ge 11$.
- **2020s.** Duminil-Copin and collaborators reprove and extend the planar theory (randomised algorithms / OSSS inequality), and push RSW-type arguments to dependent models (FK-Ising, Voronoi, Poisson–Boolean).

## 4. Partial Results / Verified Cases

Exactly known thresholds — all two-dimensional, all consequences of duality plus RSW:

| Model | $p_c$ | Source |
|---|---|---|
| $\mathbb{Z}^2$ bond | $1/2$ | Kesten 1980 |
| Triangular site | $1/2$ | Kesten 1982 |
| Triangular bond | $2\sin(\pi/18) \approx 0.347296$ | Wierman 1981 |
| Hexagonal bond | $1 - 2\sin(\pi/18) \approx 0.652704$ | Wierman 1981 |
| Bow-tie site | root of an explicit polynomial | Wierman 1984 |
| Planar Voronoi | $1/2$ | Bollobás–Riordan 2006 |
| Poisson–Boolean, self-dual scaling | $1/2$ | Bollobás–Riordan 2006 |

Other verified regimes:
- $\theta(p_c) = 0$ for $d = 2$ (Harris/Kesten), for $d \ge 11$ (Fitzner–van der Hofstad 2017, following Hara–Slade 1990 for $d \ge 19$), and on any tree or nonamenable transitive graph of large enough spectral radius.
- Critical exponents rigorously known only for triangular-lattice site percolation ($d=2$, via SLE$_6$) and in the mean-field regime $d\ge11$.
- $\mathbb{Z}^3$: numerics give $p_c^{\text{bond}} = 0.2488126(5)$ (Wang, Zhou, Zhang, Garoni, Deng 2013) — high-precision but not a theorem; even $p_c(\mathbb{Z}^3) \ne 1/4$ is unproven analytically in a sharp sense.
- Rigorous bounds in $d=3$: $0.2092 \le p_c^{\text{bond}}(\mathbb{Z}^3) \le 0.3117$ (Balister–Bollobás–Walters 2005-style substitution/entanglement arguments give intervals of this order).

## 5. Principal Obstacles

- **Loss of duality above two dimensions.** In $\mathbb{Z}^2$ a path is blocked by a dual path — a $1$-dimensional object dual to a $1$-dimensional object. In $\mathbb{Z}^d$, $d\ge3$, the blocking object is a $(d-1)$-dimensional surface, and no product measure describes it. Every exact planar threshold rests on this coincidence; nothing replaces it.
- **No RSW in $d \ge 3$.** The box-crossing property at $p_c$ is not known for $\mathbb{Z}^3$. Without it one has no scale-invariant a priori estimate, so the standard route to $\theta(p_c)=0$ (uniform crossing bounds $\Rightarrow$ Zhang-type contradiction from five or more infinite clusters) is unavailable.
- **The triangle condition fails to be checkable in low dimension.** The lace expansion is a perturbative expansion whose error terms are controlled only when the number of neighbours $2d$ is large; the current barrier is $d = 11$, and the method degrades continuously — no ingenuity in bookkeeping is expected to reach $d = 4$, let alone $d = 3$, because the expansion's small parameter is genuinely $O(1/d)$.
- **Non-integrability.** Critical planar percolation is exactly solvable in a weak sense (conformal invariance, Coulomb-gas exponents), but no transfer-matrix or Yang–Baxter structure is known in $d = 3$. Numerical $p_c(\mathbb{Z}^3)$ shows no signature of an algebraic value; there is no candidate closed form to prove.
- **Continuity vs. discontinuity at $p_c$.** Ruling out a first-order transition in $d=3$ is exactly the difficulty: sharpness (Menshikov / Duminil-Copin–Tassion) controls $p<p_c$ but says nothing about the value $\theta(p_c)$ itself.

## 6. The Gap

The proven statement is a **planar** one: self-duality at $p=1/2$ plus RSW plus Russo's formula pin $p_c$ to $1/2$ and force $\theta(1/2)=0$. The general statement asks for the value of $p_c$ and the behaviour at $p_c$ on $\mathbb{Z}^d$, $d \ge 3$.

The exact step to be crossed for $\theta(p_c)=0$ in $d=3$: establish a scale-invariant crossing estimate at criticality,
$$\inf_n \mathbb{P}_{p_c}\big(\text{open crossing of } [0,2n]\times[0,n]^2\big) > 0,$$
or an equivalent polynomial (not merely sub-exponential) decay of the one-arm probability $\mathbb{P}_{p_c}(0 \leftrightarrow \partial B_n)$. Currently one knows only $\mathbb{P}_{p_c}(0 \leftrightarrow \partial B_n) \to 0$ under the assumption $\theta(p_c)=0$ — a circular position. For $3 \le d \le 10$ the gap is precisely the interval between the lace-expansion threshold $d\ge11$ and the planar case $d=2$.

## 7. Current Research (as of June 2026)

- **Duminil-Copin's group (IHÉS / Geneva).** Randomised-algorithm and OSSS-inequality proofs of sharpness; extension of RSW machinery to models without independence (FK-percolation with $1\le q\le 4$, Voronoi, Poisson–Boolean). The stated long-term target is an RSW theory in $d=3$ *(frontier — verify)*.
- **Lace expansion at lower $d$.** Fitzner and van der Hofstad (Eindhoven) continue non-backtracking expansions; the incremental route from $d\ge11$ toward $d\ge9$ is under active development, but a proof reaching $d=7$ (the conjectured upper critical dimension is $d_c=6$) is not in sight *(frontier — verify)*.
- **Three-dimensional structure.** Work on slab percolation ($p_c(\text{slab}) = p_c(\mathbb{Z}^3)$, Grimmett–Marstrand 1990) is being reused to attack finite-size scaling at $p_c$ directly.
- **Numerics.** Monte Carlo estimates of $p_c(\mathbb{Z}^d)$ for $3\le d\le 13$ with 8–10 significant digits, feeding $1/d$-expansion checks $p_c \sim \frac{1}{2d-1} + \frac{5}{2(2d-1)^3}+\cdots$.
- **Random geometry.** Kesten-type $1/2$ results for self-dual continuum models (Voronoi, Delaunay, confetti) remain a productive testbed for duality-free arguments.

## 8. Future Work

- Prove a box-crossing property at $p_c$ in $d=3$ under any nontrivial hypothesis; this is the single highest-value target.
- Develop a non-perturbative replacement for the triangle condition valid for $6 < d < 11$, e.g. via a rigorous renormalisation-group treatment of the $\varphi^3$-type field theory in the Fortuin–Kasteleyn representation.
- Prove that $p_c(\mathbb{Z}^3)$ is not algebraic of low degree, or exhibit a structural reason no closed form can exist.
- Establish universality in $d=2$: the exponents are proven only for triangular site percolation; transferring them to $\mathbb{Z}^2$ bond percolation requires conformal invariance beyond Smirnov's setting.
- Extend Kesten's theorem to dependent planar models where self-duality holds only asymptotically (level sets of the Gaussian free field, Voronoi with non-Poissonian seeds).

## 9. Key References

- **[Foundational]** S. R. Broadbent and J. M. Hammersley. *Percolation processes I. Crystals and mazes.* Mathematical Proceedings of the Cambridge Philosophical Society **53**(3), 629–641, 1957.
- **[Foundational]** T. E. Harris. *A lower bound for the critical probability in a certain percolation process.* Mathematical Proceedings of the Cambridge Philosophical Society **56**(1), 13–20, 1960.
- **[Foundational]** H. Kesten. *The critical probability of bond percolation on the square lattice equals $1/2$.* Communications in Mathematical Physics **74**(1), 41–59, 1980.
- **[Foundational]** L. Russo. *A note on percolation.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete **43**(1), 39–48, 1978.
- **[Foundational]** P. D. Seymour and D. J. A. Welsh. *Percolation probabilities on the square lattice.* Annals of Discrete Mathematics **3**, 227–245, 1978.
- **[Book]** H. Kesten. *Percolation Theory for Mathematicians.* Birkhäuser, Progress in Probability and Statistics 2, 1982.
- **[Book]** G. Grimmett. *Percolation.* 2nd edition, Springer, Grundlehren der mathematischen Wissenschaften 321, 1999.
- **[SOTA]** T. Hara and G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Communications in Mathematical Physics **128**(2), 333–391, 1990.
- **[SOTA]** R. Fitzner and R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electronic Journal of Probability **22**, paper 43, 2017.
- **[SOTA]** S. Smirnov. *Critical percolation in the plane: conformal invariance, Cardy's formula, scaling limits.* Comptes Rendus de l'Académie des Sciences, Série I **333**(3), 239–244, 2001.
- **[SOTA]** H. Duminil-Copin and V. Tassion. *A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model.* Communications in Mathematical Physics **343**(2), 725–745, 2016.
- **[SOTA]** B. Bollobás and O. Riordan. *The critical probability for random Voronoi percolation in the plane is $1/2$.* Probability Theory and Related Fields **136**(3), 417–468, 2006.
- **[Survey]** G. Grimmett and I. Manolescu. *Universality for bond percolation in two dimensions.* Annals of Probability **41**(5), 3261–3283, 2013.
- **[Computational]** J. Wang, Z. Zhou, W. Zhang, T. M. Garoni and Y. Deng. *Bond and site percolation in three dimensions.* Physical Review E **87**, 052107, 2013.

## 10. Worked Example / Concrete Special Case

**Self-duality gives an exact crossing probability at $p = 1/2$.**

Take the rectangle $R_n$ consisting of the vertices $\{0,\dots,n\} \times \{0,\dots,n-1\}$ in $\mathbb{Z}^2$, i.e. a grid $(n+1)$ wide and $n$ tall. Let
$$H_n = \{\text{an open left–right crossing of } R_n\}.$$

Superimpose the dual lattice restricted to the matching rectangle $R_n^*$, which is $n$ wide and $n+1$ tall. Planar duality gives the exact dichotomy: **either** there is an open primal horizontal crossing of $R_n$, **or** there is an open dual vertical crossing of $R_n^*$ — never both, and never neither. (Proof: take the lowest open horizontal crossing; if none exists, the closed edges blocking every attempt assemble into a dual top–bottom path.)

Hence
$$\mathbb{P}_p(H_n) + \mathbb{P}_{1-p}(V_n^*) = 1,$$
where $V_n^*$ is the dual vertical-crossing event. At $p = 1/2$ the dual measure equals the primal one, and $R_n^*$ is the $90^\circ$ rotation of $R_n$, so $\mathbb{P}_{1/2}(V_n^*) = \mathbb{P}_{1/2}(H_n)$. Therefore
$$\boxed{\ \mathbb{P}_{1/2}(H_n) = \tfrac12 \quad \text{for every } n \ge 1.\ }$$

**Check at $n=1$.** $R_1$ has vertices $(0,0),(1,0)$ — one horizontal edge. $H_1$ = that edge is open, probability $1/2$. The dual rectangle has one vertical edge; it is open iff the primal edge is closed. Consistent.

**Check at $n=2$.** $R_2$ is a $3\times2$ grid of vertices: 4 horizontal edges, 3 vertical edges, 7 edges total, $2^7 = 128$ configurations. Direct enumeration of left–right crossings from $\{(0,0),(0,1)\}$ to $\{(2,0),(2,1)\}$ gives exactly 64 crossing configurations, so $\mathbb{P}_{1/2}(H_2) = 64/128 = 1/2$, as predicted.

**Why this is not yet the theorem.** The identity fixes crossings of *almost-square* rectangles. Kesten's proof needs crossings of $\kappa n \times n$ rectangles for $\kappa > 1$ to stay bounded below — that is RSW — and then Russo's formula
$$\frac{d}{dp}\mathbb{P}_p(H_n) = \sum_e \mathbb{P}_p(e \text{ pivotal})$$
to show the crossing probability rises from near $0$ to near $1$ across a window of width $O(n^{-\varepsilon})$ around $p=1/2$. Combining that sharp threshold with Harris's $\theta(1/2)=0$ yields $p_c = 1/2$. In $\mathbb{Z}^3$ the very first step — the boxed identity — has no analogue, which is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*