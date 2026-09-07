---
id: 09-probability/geodesic-dimension-of-the-brownian-map
title: "Geodesic Dimension of the Brownian Map"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Geodesic Dimension of the Brownian Map

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/geodesic-dimension-of-the-brownian-map` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(\mathbf{m}_\infty, D)$ be the Brownian map: the random compact metric measure space arising as the Gromov–Hausdorff scaling limit of uniform random planar maps with $n$ faces, rescaled by $n^{-1/4}$. Its Hausdorff dimension is $4$ almost surely.

Call $x \in \mathbf{m}_\infty$ a **geodesic star point of order $k$** if there exist $k$ geodesic paths started at $x$, of positive and equal length, that are pairwise disjoint apart from their common endpoint $x$. Write $\mathcal{G}_k$ for the set of such points. The **geodesic dimension problem** asks for the function
$$
k \longmapsto \dim_H(\mathcal{G}_k), \qquad k \ge 1 ,
$$
and for the maximal order $k_{\max} = \sup\{k : \mathcal{G}_k \neq \emptyset\}$.

**The answer (theorem, Le Gall 2022; upper bounds Miller–Qian 2020).** Almost surely,
$$
\dim_H(\mathcal{G}_k) = 5 - k \quad \text{for } k \in \{1,2,3,4,5\}, \qquad \mathcal{G}_k = \emptyset \text{ for } k \ge 6 .
$$

A complete resolution requires both a first-moment/covering bound $\dim_H \le 5-k$ and a matching lower bound, typically via construction of a random measure carried by $\mathcal{G}_k$ with finite $(5-k)$-energy. The residual open content — what keeps this page live rather than archived — is: (i) exact Hausdorff gauge functions for each $\mathcal{G}_k$; (ii) the analogous spectrum on Brownian disks, Brownian half-plane, Brownian surfaces of higher genus, and for $\gamma$-Liouville quantum gravity with $\gamma \neq \sqrt{8/3}$; (iii) a full classification of geodesic networks between two arbitrary (non-typical) points.

## 2. Mathematical Foundations

**Construction (Brownian snake).** Let $(\mathbf{e}_s)_{s\in[0,1]}$ be a normalized Brownian excursion and $\mathcal{T}_{\mathbf{e}}$ the associated CRT with projection $p:[0,1]\to\mathcal{T}_\mathbf{e}$ and tree metric
$$
d_\mathbf{e}(s,t) = \mathbf{e}_s + \mathbf{e}_t - 2\min_{r \in [s\wedge t,\, s\vee t]} \mathbf{e}_r .
$$
Conditionally on $\mathbf{e}$, let $(Z_a)_{a\in\mathcal{T}_\mathbf{e}}$ be the centered Gaussian field ("Brownian labels") with $Z_\rho = 0$ and $\mathbb{E}[(Z_a - Z_b)^2] = d_\mathbf{e}(a,b)$. Define, for $s,t\in[0,1]$,
$$
D^\circ(s,t) = Z_s + Z_t - 2\max\Big(\min_{r\in[s,t]} Z_r,\ \min_{r\in[t,s]} Z_r\Big),
$$
where $[t,s]$ is the cyclic interval. The Brownian map metric is the largest pseudometric dominated by $D^\circ$:
$$
D(s,t) = \inf\Big\{ \sum_{i=1}^{p} D^\circ(s_{i-1}, s_i) \ :\ p\ge 1,\ s_0 = s,\ s_p = t \Big\},
$$
and $\mathbf{m}_\infty = [0,1]/\{D = 0\}$, with volume measure $\mu$ the pushforward of Lebesgue measure.

**Root distances.** With $\rho = p(s_*)$ the a.s. unique minimizer of $Z$,
$$
D(\rho, x) = Z_x - \min Z \qquad \text{for all } x \in \mathbf{m}_\infty ,
$$
so labels *are* distances from the root. This is the reason the model is analytically tractable.

**Simple geodesics.** For $s\in[0,1]$ define $\Gamma_s(t) = \inf\{ r \ge s : Z_r = Z_s - t \}$ (cyclic order). Then $\theta \mapsto p(\Gamma_s(\theta))$, $0\le \theta \le Z_s - \min Z$, is a geodesic from $p(s)$ to $\rho$. Le Gall (2010) proved that **every** geodesic to $\rho$ is of this form.

**Cactus bound.** For all $x,y$,
$$
D(x,y) \ \ge\ D(\rho,x) + D(\rho,y) - 2 \min_{z \in [\![x,y]\!]_{\mathcal{T}}} D(\rho,z),
$$
the basic tool for forcing geodesics to be disjoint.

**Confluence.** There is a.s. $\varepsilon>0$ such that all geodesics from $\rho$ to points at distance $\ge \varepsilon$ share a common initial segment. Miller–Qian upgraded this to *strong confluence*: a quantitative, all-scales, all-pairs version with polynomial error bounds.

**Dimension.** $\dim_H(\mathbf{m}_\infty, D) = 4$ a.s. (Le Gall 2007); more precisely $\mu(B(x,r)) = r^{4+o(1)}$ uniformly.

## 3. History & State of the Art (SOTA)

- **2006–2007.** Le Gall and Marckert–Mokkadem establish the Brownian map as a subsequential limit; Le Gall proves $\dim_H = 4$ and (with Paulin) that the topology is that of $S^2$.
- **2010.** Le Gall, *Geodesics in large planar maps and in the Brownian map* (Acta Math.): complete description of geodesics to a fixed point. The set of $x$ joined to $\rho$ by at least $2$ distinct geodesics has dimension $2$; at least $3$ geodesics gives a countable dense set (dimension $0$); no point has $4$ or more geodesics to $\rho$. This is the *fixed-target* spectrum $4-2(k-1)$.
- **2013.** Le Gall (*Uniqueness and universality of the Brownian map*) and Miermont (*The Brownian map is the scaling limit of uniform random plane quadrangulations*) independently prove uniqueness of the limit.
- **2017.** Angel–Kolesnik–Miermont, *Stability of geodesics in the Brownian map*: geodesics are stable under perturbation of endpoints away from an exceptional set.
- **2020.** Miller–Qian, *Geodesics in the Brownian map: strong confluence and geometric structure*: strong confluence, structure of geodesic networks, and upper bounds $\dim_H(\mathcal{G}_k) \le 5-k$.
- **2022.** Le Gall, *Geodesic stars in random geometry* (Ann. Probab.): the matching lower bounds, hence $\dim_H(\mathcal{G}_k) = 5-k$ for $1\le k \le 5$ and $\mathcal{G}_6 = \emptyset$. This closes the main question.
- **2021.** Miller–Sheffield's axiomatic characterization identifies the Brownian map with $\sqrt{8/3}$-LQG, transporting these dimension statements into the LQG framework.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $k=1$ | $\dim_H(\mathcal{G}_1) = 4$ (every point) | Le Gall 2007 |
| $k=2$ | $\dim_H = 3$: points interior to some geodesic | Miller–Qian 2020 (ub), Le Gall 2022 (lb) |
| $k=3$ | $\dim_H = 2$ | Le Gall 2022 |
| $k=4$ | $\dim_H = 1$ | Le Gall 2022 |
| $k=5$ | $\dim_H = 0$, set nonempty and uncountable | Le Gall 2022 |
| $k\ge 6$ | $\mathcal{G}_k = \emptyset$ a.s. | Miller–Qian 2020 |
| Fixed target $\rho$, $k$ geodesics *ending* at $\rho$ | $\dim_H = 4-2(k-1)$: $2$ for $k=2$, $0$ for $k=3$, empty for $k \ge 4$ | Le Gall 2010 |
| Two independent $\mu$-typical points | unique geodesic a.s. | Le Gall 2010 |
| Single geodesic | rectifiable, $\dim_H = 1$, length $=$ $D$-distance | immediate from arclength parameterization |
| Brownian disk, interior star points | spectrum $5-k$ persists away from boundary | Le Gall–Riera-type absolute continuity |

Discrete counterparts: for uniform quadrangulations with $n$ faces, the number of $k$-star points inside a ball of radius $r n^{1/4}$ scales as $n^{(5-k)/4}$ — consistent with simulation, not with a published exhaustive enumeration.

## 5. Principal Obstacles

- **No smooth structure.** There is no tangent space, no exponential map, no curvature bound. Comparison and Jacobi-field arguments from Riemannian geometry, and Alexandrov-space methods, are all unavailable: the Brownian map has no curvature bound in the Alexandrov sense.
- **The metric is defined by an infimum over chains.** $D$ is *not* an explicit functional of $(\mathbf{e}, Z)$; only $D(\rho,\cdot)$ has a closed form. Any statement about geodesics between two non-root points must be smuggled in by re-rooting invariance, which handles one distinguished point at a time.
- **Lower bounds need exceptional-point constructions.** Upper bounds follow from first-moment covering estimates: $\mathbb{P}[B(x,\varepsilon)\text{ meets }\mathcal{G}_k] \approx \varepsilon^{k-1}$ combined with $\varepsilon^{-4}$ balls. Lower bounds require building a measure on a set of dimension possibly $0$; second-moment methods demand two-point estimates for star events at distinct locations, which are not independent because of confluence.
- **Confluence fights multiplicity.** Geodesics merge at all scales. To keep $k$ geodesics disjoint one must beat an event of probability decaying polynomially at every scale simultaneously — a multiscale, non-Markovian conditioning.
- **Non-Markovian labels.** The label process $Z$ is Gaussian only conditionally on the tree; the pair $(\mathbf{e},Z)$ has no useful Markov property along the geodesic, so excursion-theoretic decompositions must be built by hand (Le Gall's "spine with $k$ subtrees" representation).

## 6. The Gap

The core spectrum is proven. What is *not* proven:

1. **Exact gauge.** Is there a nontrivial gauge $\varphi$ with $0 < \mathcal{H}^\varphi(\mathcal{G}_k) < \infty$? For $k=5$ (dimension $0$) even the correct logarithmic gauge is unknown. Compare: $\mu$ is the Hausdorff measure of $\mathbf{m}_\infty$ in gauge $r^4 \log\log(1/r)$ (Le Gall 2022).
2. **Networks between two general points.** Miller–Qian classify the possible geodesic networks between two points; a complete dimension spectrum for the set of *pairs* $(x,y)$ realizing each network type is only partially established *(frontier — verify)*.
3. **General $\gamma$-LQG.** For $\gamma \in (0,2)$, $\gamma \neq \sqrt{8/3}$, the metric exists (Ding–Dubédat–Dunlap–Falconet, Gwynne–Miller) with dimension $d_\gamma$ unknown in closed form. The star spectrum should be $d_\gamma - (k-1)\alpha_\gamma$ for some confluence exponent $\alpha_\gamma$ with $\alpha_{\sqrt{8/3}} = 1$; neither $d_\gamma$ nor $\alpha_\gamma$ is known.
4. **Discrete convergence.** No proof that the $k$-star sets of large quadrangulations converge, as sets, to $\mathcal{G}_k$.

## 7. Current Research (as of June 2026)

- **Paris (Le Gall, Riera, Curien) and Cambridge/MIT (Miller, Sheffield, Gwynne):** extension of the star spectrum to Brownian disks, the Brownian plane and Brownian half-plane, using absolute-continuity between the models away from boundaries.
- **LQG metric group (Ding, Gwynne, Dubédat, Falconet, Pfeffer):** exponents for the general $\gamma$ metric; bounds on $d_\gamma$ (e.g. $d_2 = 4$, $d_\gamma$ increasing in $\gamma$) but no exact values.
- **Geodesic networks:** refinements of Miller–Qian's classification, reportedly identifying finitely many network topologies between arbitrary point pairs *(frontier — verify)*.
- **Exact Hausdorff measures:** attempts to extend Le Gall's $r^4\log\log(1/r)$ gauge result for $\mu$ to the lower-dimensional star sets *(frontier — verify)*.
- **Higher-genus and non-orientable Brownian surfaces (Bettinelli, Miermont):** whether the local star spectrum is genus-independent — expected yes, by local absolute continuity.

## 8. Future Work

- Build a canonical measure on $\mathcal{G}_5$ (a $0$-dimensional but uncountable set) and identify its gauge; this is the analogue of the "thick point" measures of Gaussian multiplicative chaos.
- Develop a KPZ-type formula relating the Euclidean dimension of the corresponding $\sqrt{8/3}$-LQG star set to $5-k$, then extrapolate to general $\gamma$.
- Prove a scaling limit for the discrete $k$-star sets of quadrangulations in the Hausdorff-on-Gromov–Hausdorff sense.
- Determine whether the spectrum is *universal* across the Brownian map, disk, plane and higher-genus surfaces — expected, unproven in full.

## 9. Key References

- **[Foundational]** Jean-François Le Gall. *The topological structure of scaling limits of large planar maps.* Inventiones Mathematicae 169 (2007), 621–670.
- **[Foundational]** Jean-François Le Gall. *Geodesics in large planar maps and in the Brownian map.* Acta Mathematica 205 (2010), 287–360.
- **[Foundational]** Jean-François Le Gall. *Uniqueness and universality of the Brownian map.* Annals of Probability 41 (2013), 2880–2960.
- **[Foundational]** Grégory Miermont. *The Brownian map is the scaling limit of uniform random plane quadrangulations.* Acta Mathematica 210 (2013), 319–401.
- **[SOTA]** Jean-François Le Gall. *Geodesic stars in random geometry.* Annals of Probability 50 (2022).
- **[SOTA]** Jason Miller, Wei Qian. *Geodesics in the Brownian map: strong confluence and geometric structure.* arXiv:2008.02242 (2020).
- **[SOTA]** Jason Miller, Scott Sheffield. *An axiomatic characterization of the Brownian map.* Journal de l'École polytechnique — Mathématiques 8 (2021), 609–731.
- **[Related]** Omer Angel, Brett Kolesnik, Grégory Miermont. *Stability of geodesics in the Brownian map.* Annals of Probability 45 (2017), 3451–3479.
- **[Related]** Jian Ding, Ewain Gwynne. *The fractal dimension of Liouville quantum gravity: universality, monotonicity, and bounds.* Communications in Mathematical Physics 374 (2020), 1877–1934.
- **[Survey]** Jean-François Le Gall, Grégory Miermont. *Scaling limits of random trees and planar maps.* Clay Mathematics Proceedings 15 (2012), 155–211.
- **[Survey]** Nicolas Curien. *Peeling Random Planar Maps.* Lecture Notes in Mathematics 2335, Springer, 2023.

## 10. Worked Example / Concrete Special Case

**Deriving $5-k$ by exponent counting, and checking $k=3$.**

*Step 1 — volume.* The Brownian map satisfies $\mu(B(x,\varepsilon)) = \varepsilon^{4+o(1)}$. A minimal $\varepsilon$-cover of $\mathbf{m}_\infty$ therefore uses $N(\varepsilon) = \varepsilon^{-4+o(1)}$ balls.

*Step 2 — cost of a star.* Fix a $\mu$-typical point $x$ and ask for the probability that $B(x,\varepsilon)$ contains a point emitting $k$ disjoint geodesics of length $\ge 1$. Miller–Qian's strong confluence gives the estimate
$$
\mathbb{P}\big[B(x,\varepsilon) \cap \mathcal{G}_k \neq \emptyset\big] = \varepsilon^{(k-1)+o(1)} .
$$
The exponent is $k-1$, not $k$: one geodesic is free (every point lies on a geodesic to $\rho$), and each *additional* disjoint branch costs one factor of $\varepsilon$, because it must avoid merging with the others at every scale down to $\varepsilon$.

*Step 3 — first moment.* The expected number of $\varepsilon$-balls in the cover meeting $\mathcal{G}_k$ is
$$
\mathbb{E}[N_k(\varepsilon)] \approx \varepsilon^{-4} \cdot \varepsilon^{k-1} = \varepsilon^{-(5-k)} .
$$
Hence $\dim_H(\mathcal{G}_k) \le 5-k$ by the standard covering bound, and $\mathcal{G}_k=\emptyset$ once $5-k<0$, i.e. $k \ge 6$.

*Step 4 — sanity checks.*
- $k=1$: $5-1=4$, the full space. ✔
- $k=2$: $5-2=3$. Interior points of geodesics form a set of dimension $3$ — strictly smaller than the ambient $4$, so a $\mu$-typical point is *not* in the interior of any geodesic. This is the quantitative form of "geodesics are rare".
- $k=3$: $5-3=2$. Tripods.
- $k=5$: dimension $0$, nonempty. $k=6$: empty.

*Step 5 — contrast with the fixed-target case.* If instead we demand $k$ geodesics from $x$ all ending at the *fixed* root $\rho$, each extra geodesic costs $\varepsilon^2$, not $\varepsilon$, because it must both stay disjoint near $x$ *and* re-merge at $\rho$. This gives $\varepsilon^{-4}\cdot\varepsilon^{2(k-1)} = \varepsilon^{-(4-2(k-1))}$, i.e. $\dim = 4-2(k-1)$: dimension $2$ for $k=2$, dimension $0$ for $k=3$, empty for $k \ge 4$ — exactly Le Gall's 2010 theorem. The two spectra agreeing with their respective rigorous theorems is the check that the exponent $k-1$ in Step 2 is the right one.

*What the heuristic does not give.* Step 3 is a first moment only; it bounds $\dim_H$ from above. The lower bound requires constructing a random measure $\nu_k$ on $\mathcal{G}_k$ with $\iint D(x,y)^{-s}\,\nu_k(dx)\nu_k(dy) < \infty$ for $s < 5-k$, which is the technical heart of Le Gall (2022) and rests on a spine decomposition of the Brownian snake with $k$ independent label subtrees grafted along the star.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*