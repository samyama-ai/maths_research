---
id: 09-probability/absence-of-percolation-at-criticality-for-3d-lattices
title: "Absence of Percolation at Criticality for 3D Lattices"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Absence of Percolation at Criticality for 3D Lattices

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/absence-of-percolation-at-criticality-for-3d-lattices` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbb{Z}^d$ carry nearest-neighbour bond percolation: each edge is independently *open* with probability $p$ and *closed* with probability $1-p$. Let $\theta(p) = \mathbb{P}_p(|C(0)| = \infty)$ be the probability that the origin's open cluster is infinite, and $p_c(d) = \inf\{p : \theta(p) > 0\}$.

**Conjecture.** $\theta(p_c(d)) = 0$ for every $d \ge 2$; equivalently, $\theta$ is continuous on $[0,1]$.

The conjecture is **open precisely for $3 \le d \le 10$**, and $d = 3$ is the canonical unsolved case. The same statement is open for site percolation on $\mathbb{Z}^3$, for the body-centred and face-centred cubic lattices, and for the diamond lattice.

A complete resolution requires either (i) a proof that $\mathbb{P}_{p_c}$-a.s. every cluster is finite on $\mathbb{Z}^3$ (with the argument not relying on a planar or high-dimensional structure), or (ii) a construction/proof of a lattice in dimension $3 \le d \le 10$ with $\theta(p_c) > 0$, i.e. a *discontinuous* (first-order) percolation transition. The latter would overturn the universally held physical picture and is regarded as the far less likely outcome.

## 2. Mathematical Foundations

**Probability space.** $\Omega = \{0,1\}^{\mathbb{E}^d}$ with $\mathbb{E}^d$ the nearest-neighbour edge set of $\mathbb{Z}^d$, product $\sigma$-algebra, and product measure $\mathbb{P}_p = \prod_{e} \mathrm{Bernoulli}(p)$.

**Key observables.** For $x,y \in \mathbb{Z}^d$ write $\{x \leftrightarrow y\}$ for the event of an open path, and $B_n = [-n,n]^d$.

$$\theta(p) = \mathbb{P}_p(0 \leftrightarrow \infty), \qquad \chi(p) = \mathbb{E}_p|C(0)| = \sum_{x} \tau_p(0,x), \qquad \tau_p(x,y) = \mathbb{P}_p(x \leftrightarrow y).$$

The **one-arm function** is $\pi_n(p) = \mathbb{P}_p(0 \leftrightarrow \partial B_n)$, and by monotone convergence
$$\theta(p) = \lim_{n \to \infty} \pi_n(p).$$
So the conjecture is exactly the statement $\pi_n(p_c) \to 0$: a *quantitative decay* claim, not merely a qualitative one.

**Sharpness of the transition** (Menshikov 1986; Aizenman–Barsky 1987; Duminil-Copin–Tassion 2016): for $p < p_c$ there is $c(p)>0$ with $\pi_n(p) \le e^{-c(p)n}$, and for $p > p_c$ one has $\theta(p) \ge c(p - p_c)$ near $p_c$. Hence $\theta$ is automatically continuous on $[0,1] \setminus \{p_c\}$ (it is real-analytic on $(p_c,1]$), and $\theta$ is right-continuous everywhere. **The only possible discontinuity is at $p_c$ from the right of $0$**, i.e. $\theta(p_c) > 0$.

**Uniqueness.** For every $p$, $\mathbb{P}_p$-a.s. the number of infinite clusters is $0$ or $1$ (Aizenman–Kesten–Newman 1987; Burton–Keane 1989, via the amenability of $\mathbb{Z}^d$ and the trifurcation argument). So $\theta(p_c) > 0$ would mean a *unique* infinite cluster exists at $p_c$.

**Mean-field predictions.** Physicists expect $\theta(p) \sim (p-p_c)^{\beta}$ with $\beta = \beta(d)$, $\beta(2) = 5/36$, $\beta(3) \approx 0.4181$, and $\beta = 1$ for $d \ge d_c = 6$. Any $\beta \in (0,\infty)$ forces $\theta(p_c) = 0$; a discontinuous transition corresponds to $\beta = 0$.

**Two-arms constraint (Cerf 2015).** If $\theta(p_c) > 0$ on $\mathbb{Z}^d$ then the probability that $0$ is connected to $\partial B_n$ by two disjoint open paths cannot decay faster than a fixed power, quantitatively of order $n^{-d(d-1)/2}$ up to constants. Thus a hypothetical critical infinite cluster must be "thick" in a precise sense — a structural obstruction that has not yet been pushed to a contradiction.

## 3. History & State of the Art (SOTA)

- **1957.** Broadbent–Hammersley introduce percolation; continuity of $\theta$ is folklore-conjectured immediately.
- **1960.** Harris proves $\theta(1/2) = 0$ on $\mathbb{Z}^2$, hence $p_c(2) \ge 1/2$.
- **1980.** Kesten proves $p_c(2) = 1/2$, completing $\theta(p_c) = 0$ in $d=2$ (planar duality + RSW crossing estimates).
- **1986–87.** Menshikov, and Aizenman–Barsky, prove sharpness; the problem is thereby reduced to the single point $p_c$.
- **1987–89.** Aizenman–Kesten–Newman and Burton–Keane establish uniqueness of the infinite cluster.
- **1990.** Hara–Slade prove mean-field behaviour ($\beta = 1$, hence $\theta(p_c)=0$) for nearest-neighbour percolation on $\mathbb{Z}^d$, $d \ge 19$, by the **lace expansion** verifying the triangle condition.
- **1990.** Grimmett–Marstrand: $p_c(\text{slab }\mathbb{Z}^2 \times \{0,\dots,k\}) \downarrow p_c(3)$ — the key "supercritical sharpening" tool.
- **1991.** Barsky–Grimmett–Newman: no infinite cluster at criticality in the **half-space** $\mathbb{Z}^{d-1} \times \mathbb{Z}_{\ge 0}$, all $d$.
- **2016.** Duminil-Copin–Sidoravicius–Tassion: no infinite cluster at criticality in **slabs** $\mathbb{Z}^2 \times \{0,\dots,k\}$ for every finite $k$.
- **2016.** Hutchcroft: $\theta(p_c) = 0$ for every quasi-transitive graph of **exponential volume growth** (includes nonamenable Cayley graphs, hyperbolic lattices).
- **2017.** Fitzner–van der Hofstad extend the lace expansion to $d \ge 11$ (via the non-backtracking lace expansion), the current best dimensional threshold.
- **Numerics.** $p_c(\mathbb{Z}^3, \text{bond}) = 0.24881182(10)$, $p_c(\mathbb{Z}^3,\text{site}) = 0.3116077(2)$ (Wang–Zhou–Zhang–Garoni–Deng 2013); Monte Carlo gives $\beta = 0.4181(8)$, $\nu = 0.8762(12)$, fractal dimension $D_f = 2.5230(1)$ — all consistent with a continuous transition and $\theta(p_c) = 0$.

## 4. Partial Results / Verified Cases

| Setting | Status | Source |
|---|---|---|
| $\mathbb{Z}^2$, bond and site; all planar periodic lattices (triangular, honeycomb) | **Proved**, $\theta(p_c)=0$ | Harris 1960; Kesten 1980 |
| $\mathbb{Z}^d$, $d \ge 19$ (nearest-neighbour) | **Proved** with $\beta = 1$ | Hara–Slade 1990 |
| $\mathbb{Z}^d$, $d \ge 11$ | **Proved** with $\beta=1$; one-arm exponent $\pi_n(p_c) \asymp n^{-2}$ | Fitzner–van der Hofstad 2017; Kozma–Nachmias 2011 |
| Spread-out models: range-$L$ percolation, $d > 6$, $L$ large | **Proved** ($\beta=1$) | Hara–Slade 1990 |
| Long-range $\mathbb{Z}^d$ with $\tau$-decay in the mean-field regime | **Proved** | Heydenreich–van der Hofstad–Sakai 2008 |
| Half-space $\mathbb{Z}^{d-1}\times\mathbb{Z}_{\ge0}$, all $d\ge 2$ (in particular the 3D half-space) | **Proved** | Barsky–Grimmett–Newman 1991 |
| Slabs $\mathbb{Z}^2\times\{0,\dots,k\}$, every fixed $k \in \mathbb{N}$ | **Proved** | Duminil-Copin–Sidoravicius–Tassion 2016 |
| Regular trees $\mathbb{T}_k$, $k\ge3$; nonamenable and exponential-growth quasi-transitive graphs | **Proved** | Lyons–Peres; Benjamini–Lyons–Peres–Schramm 1999; Hutchcroft 2016 |
| $\mathbb{Z}^3, \mathbb{Z}^4, \dots, \mathbb{Z}^{10}$ (bond or site); BCC, FCC, diamond lattices | **OPEN** | — |

## 5. Principal Obstacles

- **Planar duality is unavailable.** The $d=2$ proof rests on the exact self-duality of $\mathbb{Z}^2$ at $p=1/2$ and on RSW box-crossing estimates, which convert a hypothetical critical infinite cluster into simultaneous crossings of an annulus by both a primal circuit and a dual circuit. In $d = 3$ the dual object is a *surface*, not a path; no combinatorial control of critical surface events exists.
- **The lace expansion needs a large parameter.** Hara–Slade / Fitzner–van der Hofstad control the two-point function by a convergent expansion whose error terms are governed by the random-walk loop density $\sum_{n\ge1} \mathbb{P}(S_n = 0) = O(d^{-1})$. This is small only for $d \gtrsim 11$; at $d = 3$ loop corrections are $O(1)$ and the expansion diverges. There is no known non-perturbative substitute.
- **$d=3$ is below the critical dimension $d_c = 6$.** Mean-field/triangle-condition methods, hyperscaling-violating bounds, and the differential-inequality machinery of Aizenman–Barsky all lose their sharpness for $d < 6$; the critical exponents are genuinely non-Gaussian, and no rigorous renormalization-group scheme for 3D Bernoulli percolation exists.
- **Slab-to-space is a one-way street.** Grimmett–Marstrand transfers *supercritical* information from slabs to $\mathbb{Z}^3$, but the DCST slab result at criticality does not lift: $p_c(\text{slab}_k) > p_c(3)$ strictly for every $k$, so the slab is *subcritical* at $p = p_c(3)$ and yields no information about $\pi_n(p_c(3))$ as $k, n \to \infty$ jointly.
- **Amenability kills the entropy arguments.** Hutchcroft's exponential-growth proof and the BLPS mass-transport arguments use the isoperimetric gap of nonamenable graphs (positive Cheeger constant). $\mathbb{Z}^3$ is amenable with polynomial growth — exactly the regime where those inputs vanish.
- **No monotonicity in the dimension.** One cannot induct from $d=11$ downwards; $\theta_d(p_c(d))$ is not comparable across $d$ in any usable way.

## 6. The Gap

Proven: $\pi_n(p_c) \to 0$ in $d = 2$, in $d \ge 11$, in half-spaces, and in every fixed slab. Sought: $\pi_n(p_c(3)) \to 0$ in full $\mathbb{Z}^3$.

The precise missing step is a **critical a-priori estimate at $p = p_c$** in dimensions $3 \le d \le 10$: any bound of the form
$$\pi_n(p_c) \le \varepsilon_n \to 0, \qquad\text{or}\qquad \mathbb{P}_{p_c}\big(\text{annulus } B_{2n}\setminus B_n \text{ crossed}\big) \le 1-\delta \ \text{ uniformly in } n,$$
would suffice, since a uniform annulus-crossing deficit iterates multiplicatively to power-law decay. Equivalently, it suffices to prove that at $p_c$ the *two-arms* probability in $B_n$ decays faster than the two-arms lower bound permitted by Cerf's inequality — closing the gap between his $n^{-d(d-1)/2}$ lower bound and any polynomial upper bound with a larger exponent. No method currently produces a *uniform in $n$* critical estimate on $\mathbb{Z}^3$ without an expansion parameter.

## 7. Current Research (as of June 2026)

- **Geneva / IHES school (Duminil-Copin and collaborators).** Extension of the crossing-probability (RSW) technology beyond planarity, and transfer of the random-current continuity proof for the 3D Ising model (Aizenman–Duminil-Copin–Sidoravicius 2015) to Bernoulli percolation and FK-percolation with $q$ near $1$. *(frontier — verify)*
- **Cambridge / Hutchcroft group.** Locality and quantitative-structure results: Easo–Hutchcroft's locality theorem for $p_c$ on transitive graphs, and sharp two-point-function bounds under the $L^2$/triangle condition, aiming at criteria for continuity that do not require exponential growth. *(frontier — verify)*
- **Polynomial-growth programme.** Contreras–Martineau–Tassion-style supercritical-sharpness results for graphs of polynomial growth are being probed for critical-regime analogues; the amenable case remains resistant. *(frontier — verify)*
- **Lace-expansion optimization.** Fitzner–van der Hofstad-type non-backtracking expansions are being pushed below $d=11$; the barrier is believed to be technical down to roughly $d = 7$–$9$, and structural below $d_c = 6$. *(frontier — verify)*
- **Numerical/rigorous hybrids.** Interval-arithmetic and machine-assisted verification of triangle-condition-type inequalities for fixed moderate $d$.

## 8. Future Work

1. **A dimension-free annulus estimate.** Find a substitute for RSW valid in $\mathbb{Z}^3$: e.g. use the Gaussian free field / random-interlacement couplings (Duminil-Copin–Goswami–Raoufi–Severo–Yadin 2020) to obtain uniform crossing bounds for a model with critical behaviour comparable to Bernoulli percolation.
2. **Push the lace expansion to $7 \le d \le 10$.** Combining non-backtracking expansions with rigorous computer-verified bounds on the loop density is the most concrete route to shrinking the open window.
3. **Exploit Cerf's two-arms inequality.** Upgrade $n^{-d(d-1)/2}$ to a contradiction by combining it with the Burton–Keane uniqueness and a suitable "no thick critical cluster" isoperimetric input.
4. **Surface duality in 3D.** Develop a rigorous theory of dual random surfaces (Wilson-loop / plaquette percolation) so that critical primal connections can be blocked by dual surfaces, mimicking planar duality.
5. **Universality bridges.** Prove the equivalence "continuity of the 3D Ising transition $\Rightarrow$ continuity of the 3D percolation transition" via FK representation and $q \to 1$ limits, converting the known Ising result into the percolation statement.

## 9. Key References

- **[Foundational]** T. E. Harris. *A lower bound for the critical probability in a certain percolation process.* Proc. Cambridge Philos. Soc. **56** (1960), 13–20.
- **[Foundational]** H. Kesten. *The critical probability of bond percolation on the square lattice equals 1/2.* Comm. Math. Phys. **74** (1980), 41–59.
- **[Foundational]** M. Aizenman, D. J. Barsky. *Sharpness of the phase transition in percolation models.* Comm. Math. Phys. **108** (1987), 489–526.
- **[Foundational]** M. Aizenman, H. Kesten, C. M. Newman. *Uniqueness of the infinite cluster and continuity of connectivity functions for short and long range percolation.* Comm. Math. Phys. **111** (1987), 505–531.
- **[Foundational]** R. M. Burton, M. Keane. *Density and uniqueness in percolation.* Comm. Math. Phys. **121** (1989), 501–505.
- **[Foundational]** T. Hara, G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Comm. Math. Phys. **128** (1990), 333–391.
- **[Foundational]** G. Grimmett, J. Marstrand. *The supercritical phase of percolation is well behaved.* Proc. Roy. Soc. London Ser. A **430** (1990), 439–457.
- **[Foundational]** D. J. Barsky, G. R. Grimmett, C. M. Newman. *Percolation in half-spaces: equality of critical densities and continuity of the percolation probability.* Probab. Theory Related Fields **90** (1991), 111–148.
- **[SOTA / Recent]** H. Duminil-Copin, V. Sidoravicius, V. Tassion. *Absence of infinite cluster for critical Bernoulli percolation on slabs.* Comm. Pure Appl. Math. **69** (2016), 1397–1411.
- **[SOTA / Recent]** H. Duminil-Copin, V. Tassion. *A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model.* Comm. Math. Phys. **343** (2016), 725–745.
- **[SOTA / Recent]** R. Fitzner, R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electron. J. Probab. **22** (2017), paper 43.
- **[SOTA / Recent]** T. Hutchcroft. *Critical percolation on any quasi-transitive graph of exponential growth has no infinite clusters.* C. R. Math. Acad. Sci. Paris **354** (2016), 944–947.
- **[SOTA / Recent]** R. Cerf. *A lower bound on the two-arms exponent for critical percolation on the lattice.* Ann. Probab. **43** (2015), 2458–2480.
- **[SOTA / Recent]** G. Kozma, A. Nachmias. *Arm exponents in high dimensional percolation.* J. Amer. Math. Soc. **24** (2011), 375–409.
- **[SOTA / Recent]** M. Aizenman, H. Duminil-Copin, V. Sidoravicius. *Random currents and continuity of Ising model's spontaneous magnetization.* Comm. Math. Phys. **334** (2015), 719–742.
- **[SOTA / Recent]** J. Wang, Z. Zhou, W. Zhang, T. M. Garoni, Y. Deng. *Bond and site percolation in three dimensions.* Phys. Rev. E **87** (2013), 052107.
- **[Survey]** G. Grimmett. *Percolation*, 2nd ed. Grundlehren der mathematischen Wissenschaften 321, Springer, 1999.
- **[Survey]** H. Duminil-Copin. *Sixty years of percolation.* Proceedings of the International Congress of Mathematicians (Rio de Janeiro, 2018), Vol. IV, 2829–2856.
- **[Survey]** M. Heydenreich, R. van der Hofstad. *Progress in High-Dimensional Percolation and Random Graphs.* CRM Short Courses, Springer, 2017.

## 10. Worked Example / Concrete Special Case

**Where the conjecture is provable by hand: the binary tree — and exactly why $\mathbb{Z}^3$ resists.**

Take bond percolation on the rooted binary tree $T$ (root $\rho$, every vertex has $2$ children). The open cluster of $\rho$ is a Galton–Watson tree with offspring law $\mathrm{Bin}(2,p)$ and generating function
$$f(s) = \mathbb{E}[s^{\mathrm{Bin}(2,p)}] = (1-p+ps)^2 .$$
The extinction probability $q = \mathbb{P}_p(|C(\rho)| < \infty)$ is the smallest root of $s = f(s)$:
$$s = (1-p+ps)^2 \iff p^2 s^2 - \big(1 - 2p(1-p)\big)s + (1-p)^2 = 0,$$
with roots $s = 1$ and $s = \big(\tfrac{1-p}{p}\big)^2$. Hence
$$\theta(p) = 1 - q = \begin{cases} 0, & p \le \tfrac12,\\[4pt] 1 - \left(\dfrac{1-p}{p}\right)^{2}, & p > \tfrac12,\end{cases} \qquad p_c(T) = \tfrac12 .$$
At criticality $\theta(p_c) = 1 - 1 = 0$: **verified exactly.** The transition is continuous with mean-field exponent — putting $p = \tfrac12 + \varepsilon$,
$$\frac{1-p}{p} = \frac{1/2-\varepsilon}{1/2+\varepsilon} = 1 - 4\varepsilon + O(\varepsilon^2) \implies \theta\big(\tfrac12+\varepsilon\big) = 8\varepsilon + O(\varepsilon^2),$$
so $\beta = 1$.

**Why this fails on $\mathbb{Z}^3$.** The computation used one structural fact: the cluster of $\rho$ decomposes into *independent* subtrees at each child, giving the closed recursion $s = f(s)$. On $\mathbb{Z}^3$ the neighbourhoods of the six neighbours of $0$ overlap — the lattice contains cycles of length $4$ — so the analogous quantities satisfy no fixed-point equation, only inequalities. The naive branching bound treats $\mathbb{Z}^3$ as a $5$-regular tree and yields
$$p_c(\mathbb{Z}^3) \ge \frac{1}{2d-1} = \frac{1}{5} = 0.2 ,$$
versus the numerical value $p_c(\mathbb{Z}^3) = 0.2488118\ldots$. The $24\%$ gap is exactly the cycle contribution; equivalently the loop density $\sum_{n\ge1}\mathbb{P}(S_n=0) \approx 0.51$ for simple random walk on $\mathbb{Z}^3$ is $O(1)$, not small. It is this same $O(1)$ quantity that makes the lace expansion diverge, and hence the same $O(1)$ obstruction that separates the solved cases ($d=2$ by duality, $d\ge11$ by small loop density) from the open $d = 3$ case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*