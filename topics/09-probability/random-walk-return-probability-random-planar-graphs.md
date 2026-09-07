---
id: 09-probability/random-walk-return-probability-random-planar-graphs
title: "Return Probability Decay for Random Planar Maps"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Return Probability Decay for Random Planar Maps

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-walk-return-probability-random-planar-graphs` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M, \rho)$ be the Uniform Infinite Planar Triangulation (UIPT) or Quadrangulation (UIPQ), the local (Benjamini–Schramm) limit of a uniformly random triangulation/quadrangulation of the sphere with $n$ faces, rooted at a uniform vertex. Let $(X_k)_{k \ge 0}$ be simple random walk on $M$ started at $\rho$, and let
$$p_n(x,y) = \frac{\mathbf{P}_x(X_n = y)}{\deg(y)}$$
be the (symmetric) heat kernel.

**Conjecture (sharp return probability).** There exist constants $0 < c < C < \infty$ such that for the annealed law,
$$\frac{c}{n} \;\le\; \mathbf{E}\big[\,p_{2n}(\rho,\rho)\,\big] \;\le\; \frac{C}{n}, \qquad n \ge 1,$$
i.e. the spectral dimension is exactly $d_s = 2$ **with no polylogarithmic corrections**. Quenched, the conjecture asserts that almost surely $p_{2n}(\rho,\rho) = n^{-1+o(1)}$ with the $o(1)$ improvable to a bounded ratio of $\log$-powers, and that the matching displacement statement
$$\mathbf{E}\big[\,d_M(\rho, X_n)\,\big] \asymp n^{1/4}$$
holds up to constants.

A complete solution requires: (i) two-sided bounds with explicit constants or explicit $\log$ exponents, replacing the current $n^{-1+o(1)}$; (ii) identification of whether the correction is $1$, $(\log n)^{-a}$, or $(\log n)^{+a}$; (iii) the same for the whole $\gamma$-Liouville quantum gravity (LQG) family $\gamma \in (0,2)$, where the *value* of $d_s$ beyond the exponent-$2$ heuristic is itself disputed. A disproof would exhibit a subpolynomial correction, e.g. $p_{2n}(\rho,\rho) \asymp (n \log n)^{-1}$.

## 2. Mathematical Foundations

**Unimodular random graphs.** A random rooted graph $(G,\rho)$ is *unimodular* if it satisfies the mass-transport principle: for every non-negative $f(G,x,y)$ invariant under rooted isomorphism,
$$\mathbf{E}\Big[\sum_{y \in V} f(G,\rho,y)\Big] = \mathbf{E}\Big[\sum_{y \in V} f(G,y,\rho)\Big].$$
Local limits of finite graphs rooted at uniform vertices are unimodular; UIPT and UIPQ are unimodular with $\mathbf{E}[\deg \rho] < \infty$ (in fact $\deg \rho$ has exponential tails).

**Network reduction.** Regard $M$ as an electrical network with unit conductances. Write $B_r = B_r(\rho)$ for the metric ball, $V(r) = \sum_{x \in B_r} \deg(x)$ for its volume, and $R(r) = R_{\mathrm{eff}}(\rho \leftrightarrow \partial B_r)$ for the effective resistance. The Nash–Williams inequality gives $R(r) \ge \sum_{k<r} |\partial B_k|^{-1}$, and recurrence is equivalent to $R(\infty) = \infty$.

**Volume–resistance exponents.** Suppose $V(r) = r^{d_f + o(1)}$ and $R(r) = r^{\zeta + o(1)}$. The standard Barlow-type heat kernel machinery then yields
$$p_{2n}(\rho,\rho) = n^{-d_s/2 + o(1)}, \qquad d_s = \frac{2 d_f}{d_f + \zeta}, \qquad \mathbf{E}\,d(\rho, X_n) = n^{1/(d_f+\zeta) + o(1)}.$$
For the UIPT/UIPQ, $d_f = 4$ (Angel; Chassaing–Schaeffer/Le Gall: $|B_r| = r^{4+o(1)}$) and the theorem of Gwynne–Miller gives $\zeta = 0$, i.e. $R(r) = r^{o(1)}$. Hence $d_s = 2$ and displacement exponent $1/4$.

**Circle packing / conformal input.** By the Koebe–Andreev–Thurston theorem every finite simple planar triangulation admits a circle packing, unique up to Möbius maps. He–Schramm's dichotomy classifies infinite bounded-degree triangulations as CP-parabolic or CP-hyperbolic. Benjamini–Schramm and Gurel-Gurevich–Nachmias use this to prove recurrence; Lee replaces it by *conformal growth rates*: the infimum over unimodular vertex-weightings $\omega: V \to \mathbb{R}_{>0}$ with $\sum_x \omega(x)^2 \le 1$ of the growth of $\omega$-balls.

**LQG limit.** For $\gamma \in (0,2)$, $\gamma$-LQG is the random measure $\mu_h = \lim_{\varepsilon \to 0} \varepsilon^{\gamma^2/2} e^{\gamma h_\varepsilon(z)} dz$ for $h$ a Gaussian free field. The UIPQ corresponds to $\gamma = \sqrt{8/3}$. Liouville Brownian motion is the time change of planar Brownian motion by the inverse of $F(t) = \int_0^t e^{\gamma h(B_s)} ds$ (Garban–Rhodes–Vargas; Berestycki).

## 3. History & State of the Art (SOTA)

- **1995.** Ambjørn–Watabiki and Ambjørn–Jurkiewicz–Watabiki, from two-dimensional quantum gravity, predict Hausdorff dimension $d_H = 4$ and spectral dimension $d_s = 2$ for dynamical triangulations, with numerical simulations consistent with $d_s \approx 2$.
- **2001.** Benjamini–Schramm prove that distributional limits of finite planar graphs with bounded degree are almost surely recurrent — the structural cornerstone.
- **2003.** Angel–Schramm construct the UIPT; Angel establishes $|B_r| = r^{4+o(1)}$.
- **2013.** Gurel-Gurevich–Nachmias remove the bounded-degree hypothesis, replacing it by an exponential degree tail, proving the UIPT and UIPQ are almost surely **recurrent**.
- **2013.** Benjamini–Curien prove sub-diffusivity: $d(\rho,X_n) = O(n^{1/3+o(1)})$ on the UIPQ, via a stationarity/Talagrand argument. Gill–Rohde independently establish parabolicity of the Riemann surface associated with random planar maps.
- **2021.** Lee proves that for any unimodular random planar graph with $\mathbf{E}[\deg\rho] < \infty$, $p_{2n}(\rho,\rho) \le n^{-1+o(1)}$, so $d_s \le 2$ universally.
- **2021.** Gwynne–Miller (*Annals of Probability*) prove the matching lower bound for the mated-CRT map and, by strong coupling, for the UIPT/UIPQ and other $\gamma$-LQG maps: $p_{2n}(\rho,\rho) = n^{-1+o(1)}$, $R(r) = r^{o(1)}$, and displacement $n^{1/4+o(1)}$. Gwynne–Hutchcroft prove the matching displacement lower bound.

**SOTA in one line:** the exponent is settled ($d_s = 2$); the subpolynomial correction is not.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Bounded-degree unimodular planar | recurrent | Benjamini–Schramm 2001 |
| UIPT, UIPQ (exponential degree tail) | recurrent | Gurel-Gurevich–Nachmias 2013 |
| All unimodular planar, $\mathbf{E}\deg < \infty$ | $p_{2n} \le n^{-1+o(1)}$ | Lee 2021 |
| Mated-CRT map, $\gamma \in (0,2)$ | $p_{2n} = n^{-1+o(1)}$, $R(r) = r^{o(1)}$ | Gwynne–Miller 2021 |
| UIPT ($q$-angulations, $q$ even), UIPQ, Poisson–Voronoi triangulation of $\sqrt{8/3}$-LQG, Tutte-embedded maps | $d_s = 2$, displacement exponent $1/4$ | Gwynne–Miller 2021; Gwynne–Hutchcroft 2021 |
| $\gamma$-LQG maps, general $\gamma$ | displacement exponent $1/d_\gamma$, $d_\gamma$ the LQG dimension | Gwynne–Hutchcroft 2021 |
| Liouville Brownian motion on $\gamma$-LQG, $\gamma < 2$ | $d_s = 2$ (annealed heat kernel exponent) | Rhodes–Vargas 2014; Andres–Kajino 2016 |
| Hyperbolic (PSHT, $\lambda < \lambda_c$) | transient, positive speed, exponential heat kernel decay | Curien 2016; Angel–Hutchcroft–Nachmias–Ray |
| Trees / stable maps ($\alpha \in (1,2)$) | $d_s = 4/3$ for critical Galton–Watson trees conditioned to survive | Barlow–Kumagai 2006 |

Sharp constants are known only in degenerate comparison cases: $\mathbb{Z}^2$ has $p_{2n}(0,0) \sim (\pi n)^{-1}$; the incipient infinite cluster on the tree has $d_s = 4/3$ with $\log$-corrections still open.

## 5. Principal Obstacles

- **The $o(1)$ is baked into the method.** Gwynne–Miller's lower bound routes through the *strong coupling* between mated-CRT maps and UIPQ/UIPT (Gwynne–Holden–Sun, Gwynne–Miller–Sheffield), whose error is only known to be subpolynomial. Any conclusion inherits an $n^{o(1)}$ factor. There is no known coupling with $\log$-order error.
- **Multiplicative chaos moments.** Estimating $\mu_h$ of small balls requires negative and high moments of Gaussian multiplicative chaos. Exact moment formulas (DOZZ, Kupiainen–Rhodes–Vargas) apply to the total mass on a fixed surface, not to the local ball masses along a random walk path, and the tail behavior at the relevant scale contributes exactly the disputed $\log$ factors.
- **No exact solvability for the walk.** The peeling process gives exact enumerative control of the *geometry* (Krikun's skeleton decomposition, Curien–Le Gall), but random walk is not a peeling-adapted observable: the walk backtracks into already-explored regions, destroying the Markov property of the exploration.
- **Resistance is subpolynomial but not bounded.** Only $R(r) = r^{o(1)}$ is proven. Whether $R(r) \asymp 1$, $\asymp \log r$, or $\asymp (\log r)^{a}$ is open, and each alternative shifts the heat kernel by a different $\log$ power. Nash–Williams gives $R(r) \gtrsim \log r$ only when $|\partial B_k| \lesssim k$, which is false here ($|\partial B_k| \approx k^2$), so the natural lower-bound tool is silent.
- **Unbounded degrees break circle packing.** He–Schramm rigidity and the ring lemma require bounded degree; the UIPT's degree tail forces a detour through Lee's conformal growth rates, which are inherently exponent-level, not constant-level, statements.

## 6. The Gap

Proven: $d_s = 2$ as an exponent, i.e. $\lim_{n} \frac{\log p_{2n}(\rho,\rho)}{\log n} = -1$ a.s. and $R(r) = r^{o(1)}$.

Conjectured: $p_{2n}(\rho,\rho) \asymp n^{-1}$ with matching constants (or an identified $\log$ power).

The precise missing step is a **two-sided volume-and-resistance estimate at logarithmic precision**: control of
$$\sup_{r} \frac{R(r)}{(\log r)^{a}} \quad \text{and} \quad \mathbf{E}\big[V(r)\, r^{-4}\big]$$
that is uniform in $r$, together with a coupling of the UIPQ with the mated-CRT map whose error is $O(\mathrm{polylog})$ rather than $n^{o(1)}$. Equivalently: a direct proof on the map itself, bypassing LQG, that produces a parabolic Harnack inequality with $\log$-order error terms.

## 7. Current Research (as of June 2026)

- **Gwynne, Miller, Holden, Sun (Penn/Chicago/MIT/NYU–Shanghai).** Sharpening the mated-CRT coupling; the goal is a polylogarithmic error in the Gwynne–Holden–Sun embedding. *(frontier — verify)*
- **Lee (U. Washington).** Extending conformal growth rates to relations among scaling exponents in unimodular random graphs, aiming at exponent identities $d_s(d_f + \zeta) = 2d_f$ with error control.
- **Nachmias, Gurel-Gurevich, Angel, Ray (Tel Aviv / Hebrew U. / UBC / Bath).** Circle-packing methods for unbounded-degree unimodular maps; sharp Harnack inequalities on random triangulations.
- **Ding, Gwynne, Zhang (Peking / Chicago).** LQG metric-measure heat kernel bounds; the Liouville heat kernel on $\gamma$-LQG is known to satisfy $\exp(-c (d(x,y)^{\beta}/t)^{1/(\beta-1)})$-type bounds with non-matching exponents, and closing that gap is the continuum analogue.
- **Physics side.** Numerical dynamical-triangulation studies (Ambjørn's group, Copenhagen/Utrecht) continue to report $d_s = 2.00 \pm 0.05$, with residual finite-size drift consistent with $\log$ corrections — currently the strongest evidence that the correction is not trivially $1$. *(frontier — verify)*

## 8. Future Work

1. **Direct peeling proof.** Build a resistance-estimate from Krikun's skeleton decomposition, avoiding LQG entirely; this is the most likely route to $\log$-precision.
2. **Prove or disprove $R(r) \asymp 1$.** A bounded-resistance theorem would immediately give $p_{2n} \asymp n^{-1}$ under standard volume-doubling arguments (Barlow, Kumagai).
3. **Elliptic Harnack inequality** for harmonic functions on the UIPT: currently unknown, and would upgrade heat kernel exponents to two-sided sub-Gaussian bounds.
4. **Transfer to LQG.** Determine whether $d_s = 2$ for Liouville Brownian motion holds with constants for all $\gamma \in (0,2)$, and whether the $\gamma \to 2$ limit is singular.
5. **Other universality classes.** Stable maps with $\alpha \in (3/2, 5/2)$ (Le Gall–Miermont): compute $d_s$, expected to be non-$2$ for $\alpha < 2$.

## 9. Key References

- **[Foundational]** I. Benjamini, O. Schramm. *Recurrence of distributional limits of finite planar graphs.* Electronic Journal of Probability 6 (2001), paper 23.
- **[Foundational]** O. Angel, O. Schramm. *Uniform infinite planar triangulations.* Communications in Mathematical Physics 241 (2003), 191–213.
- **[Foundational]** O. Gurel-Gurevich, A. Nachmias. *Recurrence of planar graph limits.* Annals of Mathematics 177 (2013), 761–781.
- **[SOTA]** E. Gwynne, J. Miller. *Random walk on random planar maps: spectral dimension, resistance and displacement.* Annals of Probability 49 (2021), 1097–1128.
- **[SOTA]** E. Gwynne, T. Hutchcroft. *Anomalous diffusion of random walk on random planar maps.* Probability Theory and Related Fields 178 (2021), 567–611.
- **[SOTA]** J. R. Lee. *Conformal growth rates and spectral geometry of distributional limits of graphs.* Annals of Probability 49 (2021), 2671–2731.
- **[Partial]** I. Benjamini, N. Curien. *Simple random walk on the uniform infinite planar quadrangulation: subdiffusivity via pioneer points.* Geometric and Functional Analysis 23 (2013), 501–531.
- **[Physics origin]** J. Ambjørn, J. Jurkiewicz, Y. Watabiki. *On the fractal structure of two-dimensional quantum gravity.* Nuclear Physics B 454 (1995), 313–342.
- **[Continuum]** R. Rhodes, V. Vargas. *Spectral dimension of Liouville quantum gravity.* Annales Henri Poincaré 15 (2014), 2281–2298.
- **[Continuum]** C. Garban, R. Rhodes, V. Vargas. *Liouville Brownian motion.* Annals of Probability 44 (2016), 3076–3110.
- **[Survey]** A. Nachmias. *Planar Maps, Random Walks and Circle Packing.* Lecture Notes in Mathematics 2243, Springer, 2020 (École d'Été de Probabilités de Saint-Flour XLVIII).
- **[Survey]** M. T. Barlow. *Random Walks and Heat Kernels on Graphs.* London Mathematical Society Lecture Note Series 438, Cambridge University Press, 2017.
- **[Survey]** N. Curien. *Peeling Random Planar Maps.* Lecture Notes in Mathematics 2335, Springer, 2023.

## 10. Worked Example / Concrete Special Case

**Step 1: the Euclidean calibration.** On $\mathbb{Z}^2$ the walk decouples into two independent lazy one-dimensional walks, giving exactly
$$p_{2n}(0,0) = \Big(\binom{2n}{n} 2^{-2n}\Big)^2 \sim \frac{1}{\pi n}.$$
Here $d_f = 2$, $R(r) \asymp \log r$ so $\zeta = 0$, and $d_s = 2d_f/(d_f+\zeta) = 2$. Note $R(r)$ is *unbounded* yet the heat kernel has **no** $\log$ correction — the resistance logarithm is absorbed. This is exactly the ambiguity that makes the UIPQ question hard.

**Step 2: the UIPQ exponent computation.** Take $d_f = 4$: the volume of the ball of radius $r$ in the UIPQ satisfies $|B_r| = r^{4+o(1)}$, matching $\mathrm{dim}_H(\text{Brownian map}) = 4$. Take $\zeta = 0$ from Gwynne–Miller's $R(r) = r^{o(1)}$. Then
$$d_s = \frac{2 \cdot 4}{4 + 0} = 2, \qquad \frac{1}{d_f + \zeta} = \frac14 .$$
So $p_{2n}(\rho,\rho) = n^{-1+o(1)}$ and $d(\rho, X_n) = n^{1/4 + o(1)}$. The walk explores a ball of radius $n^{1/4}$ containing $\approx n$ vertices, and spends $\Theta(1)$ fraction of its time near $\rho$ up to subpolynomial factors — the return probability is $\approx 1/|B_{n^{1/4}}| = 1/n$.

**Step 3: where the gap bites.** Insert a hypothetical $R(r) = (\log r)^{a}$. Then for $t \approx r^{4}(\log r)^{a}$,
$$p_{2t}(\rho,\rho) \approx \frac{1}{V(r)} \approx \frac{1}{r^4} \approx \frac{(\log t)^{a}}{t}\cdot\frac{1}{(\log r)^{a}}\Big|_{r = (t/(\log t)^a)^{1/4}} = \frac{C_a (\log t)^{0}}{t}\cdot(1+o(1))?$$
Working it through: $r^4 = t (\log r)^{-a}$ gives $p_{2t} \asymp (\log t)^{a} 4^{-a} / t$. So $a \ne 0$ produces a genuine $(\log t)^{a}$ correction, invisible to every current theorem because all of them tolerate $t^{o(1)}$. Distinguishing $a = 0$ from $a = 1$ is precisely the open problem.

**Step 4: a Nash–Williams check.** In the UIPQ, $|\partial B_k| = k^{2+o(1)}$, so Nash–Williams gives only $R(r) \gtrsim \sum_{k<r} k^{-2-o(1)} = O(1)$ — no lower bound beyond a constant. This confirms the method cannot detect a $\log$ correction, and that a genuinely new estimate is needed.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*