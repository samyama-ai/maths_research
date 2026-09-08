---
id: 09-probability/bigeodesics-first-passage-percolation
title: "Uniqueness of Bi-Infinite Geodesics in First-Passage Percolation"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Uniqueness of Bi-Infinite Geodesics in First-Passage Percolation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/bigeodesics-first-passage-percolation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Put i.i.d. non-negative weights $(\tau_e)_{e \in E(\mathbb{Z}^d)}$ on the nearest-neighbour edges of $\mathbb{Z}^d$ and define the passage time $T(x,y)$ as the infimum of $\sum_{e \in \gamma} \tau_e$ over lattice paths $\gamma$ from $x$ to $y$. A **bi-infinite geodesic** (bigeodesic) is a doubly infinite path $\dots, v_{-1}, v_0, v_1, \dots$ every finite subpath of which is a geodesic for its endpoints.

**Conjecture (Furstenberg; popularized by Kesten 1986).** For $d = 2$ and any continuous weight distribution with $\mathbb{P}(\tau_e = 0) < p_c(\mathbb{Z}^2) = 1/2$ and suitable moments, almost surely **no** bi-infinite geodesic exists.

The title "uniqueness" refers to the equivalent geometric formulation: for each direction $\theta$ the semi-infinite geodesics coalesce, so that at most one bi-infinite geodesic could be assembled from two coalescing trees, and the conjecture asserts that even this one is absent. A complete resolution requires either (i) a proof of a.s. non-existence for general planar i.i.d. weights with no curvature or solvability assumption, or (ii) an explicit construction of a distribution under which bigeodesics exist with positive probability.

## 2. Mathematical Foundations

Let $\Omega = [0,\infty)^{E(\mathbb{Z}^d)}$ carry the product measure $\mathbb{P} = \mu^{\otimes E}$, $\mu$ the common weight law. Define
$$T(x,y) \;=\; \inf_{\gamma: x \to y} \; \sum_{e \in \gamma} \tau_e .$$

**Shape theorem (Cox–Durrett 1981; Kesten 1986).** If $\mathbb{E}\big[\min\{\tau_{e_1},\dots,\tau_{e_{2d}}\}^d\big] < \infty$ then there is a deterministic norm $g$ on $\mathbb{R}^d$ (the *time constant*) with
$$\lim_{n\to\infty} \frac{T(0,\lfloor nx \rfloor)}{n} = g(x) \quad \text{a.s.,} \qquad \frac{1}{t}\,B(t) \longrightarrow \mathcal{B} = \{x : g(x) \le 1\},$$
where $B(t) = \{x : T(0,x) \le t\}$ and $\mathcal{B}$ is the compact convex **limit shape**.

**Busemann functions.** For a semi-infinite geodesic $\Gamma$ with vertices $v_n$, set
$$B_\Gamma(x,y) \;=\; \lim_{n \to \infty} \big( T(x, v_n) - T(y, v_n) \big),$$
when the limit exists. $B$ is additive, $B(x,y) + B(y,z) = B(x,z)$, and $|B(x,y)| \le T(x,y)$. Along a geodesic $B$ *decreases at the exact rate of the weights*: a path following $-\nabla B$ is a geodesic. Existence of a bigeodesic in direction $\pm\theta$ is essentially equivalent to the existence of a pair of Busemann-type fields $B^+, B^-$ whose gradient flows share a common backward trajectory.

**Curvature assumption.** Most theorems require that $\partial \mathcal{B}$ has a point of *differentiability with uniform curvature*: for some direction $\theta$ and $\kappa > 0$,
$$g(x) \;\ge\; g(\theta)\,\langle x, \hat n_\theta \rangle + \kappa\,\big|x - \langle x, \hat n_\theta\rangle \hat n_\theta\big|^2 \quad \text{near } \theta .$$
No non-trivial curvature statement is proved for any i.i.d. weight law on $\mathbb{Z}^2$.

**KPZ exponents.** Conjecturally $\operatorname{Var} T(0, n e_1) \asymp n^{2/3}$ and geodesic transversal fluctuations $\asymp n^{2/3}$ ($\chi = 1/3$, $\xi = 2/3$, $\chi = 2\xi - 1$). The heuristic for non-existence: a bigeodesic through $0$ of length $2n$ must be optimal among $\sim e^{cn}$ competitors, and the $n^{1/3}$-scale fluctuations of the two halves are asymptotically independent, so the probability that they match at $0$ decays.

## 3. History & State of the Art (SOTA)

- **1965–1980s.** Hammersley–Welsh introduce FPP (1965). Furstenberg raises the bigeodesic question in the context of the "two-sided" structure of the model; Kesten records it as Problem 3 in his Saint-Flour lectures (1986), noting the analogy with ground states of disordered Ising models.
- **1995.** Newman's ICM survey "A surface view of first-passage percolation" frames the geodesic programme: uniform curvature of $\partial \mathcal{B}$ $\Rightarrow$ existence, uniqueness and coalescence of directional semi-infinite geodesics.
- **1996.** Licea–Newman prove, under curvature plus a technical hypothesis, that for Lebesgue-a.e. direction $\theta \in [0,2\pi)$ semi-infinite geodesics in direction $\theta$ are a.s. unique from every vertex and coalesce; hence no bigeodesic has both ends in such directions.
- **1998.** Wehr–Woo: no bi-infinite geodesic in the **half-plane** $\mathbb{Z} \times \mathbb{Z}_{\ge 0}$, for general i.i.d. continuous weights — no curvature assumption.
- **2005–2008.** Hoffman's non-equilibrium ergodic ("Busemann increment") arguments give at least $2$, then at least $4$, distinct coalescing semi-infinite geodesic trees with no curvature input.
- **2014, 2017.** Damron–Hanson construct generalized Busemann functions from subsequential limits of $T(\cdot,v_n) - T(\cdot,v_n')$ and prove: under curvature, no bigeodesic has one end with asymptotic direction in a fixed set of directions of full measure.
- **2018–2022.** Basu–Hoffman–Sly rule out bigeodesics in planar **exponential last-passage percolation** using integrable input; Balázs–Busani–Seppäläinen give a purely probabilistic (queueing/coupling) proof of non-existence of bi-infinite polymers/geodesics in the exponential corner growth model.
- **2020s.** Directed-landscape methods (Dauvergne–Virág) transfer the statement to the KPZ fixed point limit; Alexander obtains general-$d$ structural results.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| Half-plane $\mathbb{Z}\times\mathbb{Z}_{\ge0}$, general continuous i.i.d. | No bigeodesic, a.s. | Wehr–Woo (1998) |
| $\mathbb{Z}^2$, curvature assumption | Unique, coalescing $\theta$-geodesics for a.e. $\theta$; no bigeodesic with both ends directed in that full-measure set | Licea–Newman (1996) |
| $\mathbb{Z}^2$, curvature | No bigeodesic with **one** end asymptotically directed | Damron–Hanson (2017) |
| Exponential LPP on $\mathbb{Z}^2$ (rate-1 i.i.d. $\mathrm{Exp}$ vertex weights, up-right paths) | No bi-infinite geodesic, a.s., **unconditionally** | Basu–Hoffman–Sly (2022); Balázs–Busani–Seppäläinen (2020) |
| Exponential LPP, coalescence quantified: two geodesics at transversal separation $r$ coalesce within distance $O(r^{3})$ up to polynomial corrections | Yes | Basu–Sarkar–Sly (2019); Seppäläinen–Shen (2020) |
| Brownian LPP / directed landscape | Non-existence of bi-infinite geodesics in the directed landscape | Busani–Seppäläinen–Sorensen and Balázs–Busani–Seppäläinen line of work (2022–2024) |
| General $d \ge 3$ | Structural: any bigeodesic has both ends with no asymptotic direction, or a curvature-conditional exclusion | Alexander (2023) |
| Weights with $\mathbb{P}(\tau_e = 0) > p_c$ | Bigeodesics **exist** (zero-weight infinite cluster) — shows the hypothesis $\mathbb{P}(\tau_e=0)<p_c$ is necessary | folklore; see Auffinger–Damron–Hanson (2017) |

## 5. Principal Obstacles

- **No proven curvature.** Every geometric argument in the Newman programme needs strict convexity or uniform curvature of $\partial\mathcal{B}$. For i.i.d. weights on $\mathbb{Z}^2$ it is not even known that $\partial\mathcal{B}$ contains **one** point of differentiability, nor that $\mathcal{B}$ is not a polygon. This is the single hardest input.
- **No proven KPZ exponents.** The heuristic for non-existence uses $\chi=1/3$, $\xi=2/3$ and asymptotic independence of the two halves. For general weights only $\operatorname{Var} T = O(n/\log n)$ (Benjamini–Kalai–Schramm 2003) and sublinear-order lower bounds are known; the conjectural $n^{2/3}$ is out of reach.
- **Integrability is not robust.** The unconditional theorems (BHS, BBS) use exact stationary structure of exponential weights — Burke's property, memorylessness of the queueing map, explicit one-point tail estimates from RSK/Tracy–Widom. Removing exponentiality removes every one of these; no known universality result transfers a geometric conclusion from $\mathrm{Exp}$ weights to arbitrary $\mu$.
- **Burton–Keane fails.** The classical uniqueness-of-infinite-cluster counting argument does not apply: geodesics are not defined by a translation-invariant local rule, and a bigeodesic set need not have the "trifurcation" structure the argument requires.
- **Directionless ends.** Damron–Hanson exclude bigeodesics whose end has an asymptotic direction. A pathological bigeodesic could wander with no limiting direction; ruling this out needs control of geodesic wandering at all scales, which is exactly the missing $\xi = 2/3$ estimate.

## 6. The Gap

Proved: non-existence in the half-plane; non-existence in exponential LPP and in the directed landscape; conditional non-existence under curvature for directed ends. Conjectured: non-existence on $\mathbb{Z}^2$ for **all** continuous i.i.d. $\mu$ with $\mathbb{P}(\tau_e=0)<1/2$.

The gap is a single implication chain with two broken links:

1. **Curvature.** Prove $\partial\mathcal{B}$ is uniformly curved (or at least strictly convex at a positive-measure set of directions) for some non-integrable i.i.d. law. Nothing of this kind is known.
2. **Undirected ends.** Even granting curvature, one must exclude bigeodesics whose ends have no asymptotic direction — equivalently, obtain a quantitative coalescence estimate valid uniformly over directions.

Alternatively, a **universality bridge** from exponential LPP to general FPP would bypass both. No such bridge exists at the level of geodesic geometry.

## 7. Current Research (as of June 2026)

- **Directed landscape / KPZ fixed point.** Dauvergne, Virág and collaborators (Toronto, Montréal) study geodesic networks and exceptional times in the limiting object; non-existence of bigeodesics there is settled, and the effort is to push the invariance principle back to prelimiting non-integrable models. *(frontier — verify)*
- **Stationary horizon.** Busani, Seppäläinen, Sorensen (Bristol, Wisconsin–Madison, Bonn) develop the *stationary horizon* as the universal coupled Busemann process across directions; it gives a unified proof of non-existence in exponential LPP, Brownian LPP and the KPZ fixed point.
- **Queueing/coupling methods.** Balázs (Bristol) and collaborators seek versions of the BBS argument requiring only a *stationary* version of the model, not exact solvability — e.g. for the inverse-gamma polymer and for FPP with weights admitting an explicit stationary cocycle.
- **Curvature attack.** Damron, Hanson, Auffinger and students (Georgia Tech, CUNY) work on differentiability and non-polygonality of $\partial\mathcal{B}$ and on Busemann-measure geometry in general $d$ (Janjigian–Rassoul-Agha–Seppäläinen).
- **General dimension.** Alexander's programme on coalescence and bigeodesics in $d \ge 3$; no unconditional result is known for any $d \ge 3$ model, integrable or not.

## 8. Future Work

- Prove that $\partial\mathcal{B}$ has at least one point of differentiability for some explicit i.i.d. $\mu$ — the most-cited "next step" in Auffinger–Damron–Hanson.
- Establish a coalescence estimate for semi-infinite geodesics in general planar FPP that is uniform in direction, closing the directionless-end case of Damron–Hanson.
- Construct a stationary cocycle / Busemann process for non-solvable planar FPP and rerun the BBS non-existence argument on it.
- Settle $d \ge 3$: even under curvature, existence of bigeodesics in $\mathbb{Z}^3$ is fully open; some experts expect the answer may differ from $d=2$.
- Transfer the directed-landscape non-existence result to prelimit FPP via a geodesic-level invariance principle.
- Exhibit a distribution (possibly heavy-tailed or with atoms below $p_c$) for which bigeodesics provably exist, which would show that "continuous + subcritical" is not sufficient.

## 9. Key References

- **[Foundational]** H. Kesten. *Aspects of First Passage Percolation.* École d'Été de Probabilités de Saint-Flour XIV, Lecture Notes in Mathematics 1180, Springer, 1986.
- **[Foundational]** C. M. Newman. *A surface view of first-passage percolation.* Proceedings of the International Congress of Mathematicians (Zürich 1994), Birkhäuser, 1995, pp. 1017–1023.
- **[Foundational]** C. Licea, C. M. Newman. *Geodesics in two-dimensional first-passage percolation.* Annals of Probability 24 (1996), 399–410.
- **[Foundational]** J. Wehr, J. Woo. *Absence of geodesics in first-passage percolation on a half-plane.* Annals of Probability 26 (1998), 358–367.
- **[Structural]** C. Hoffman. *Geodesics in first passage percolation.* Annals of Applied Probability 18 (2008), 1944–1969.
- **[Structural]** M. Damron, J. Hanson. *Busemann functions and infinite geodesics in two-dimensional first-passage percolation.* Communications in Mathematical Physics 325 (2014), 917–963.
- **[SOTA]** M. Damron, J. Hanson. *Bigeodesics in first-passage percolation.* Communications in Mathematical Physics 349 (2017), 753–776.
- **[SOTA]** R. Basu, C. Hoffman, A. Sly. *Nonexistence of bigeodesics in planar exponential last passage percolation.* Communications in Mathematical Physics 389 (2022), 1–30.
- **[SOTA]** M. Balázs, O. Busani, T. Seppäläinen. *Non-existence of bi-infinite geodesics in the exponential corner growth model.* Forum of Mathematics, Sigma 8 (2020), e46.
- **[SOTA]** R. Basu, S. Sarkar, A. Sly. *Coalescence of geodesics in exactly solvable models of last passage percolation.* Journal of Mathematical Physics 60 (2019), 093301.
- **[SOTA]** K. S. Alexander. *Geodesics, bigeodesics, and coalescence in first passage percolation in general dimension.* Electronic Journal of Probability 28 (2023), paper 14.
- **[Structural]** C. Janjigian, F. Rassoul-Agha, T. Seppäläinen. *Geometry of geodesics through Busemann measures in directed last-passage percolation.* Journal of the European Mathematical Society 25 (2023), 2573–2639.
- **[Survey]** A. Auffinger, M. Damron, J. Hanson. *50 Years of First-Passage Percolation.* AMS University Lecture Series 68, American Mathematical Society, 2017.
- **[Background]** I. Benjamini, G. Kalai, O. Schramm. *First passage percolation has sublinear distance variance.* Annals of Probability 31 (2003), 1970–1978.

## 10. Worked Example / Concrete Special Case

**Coalescence in a $3\times3$ corner-growth box.** Take last-passage percolation with vertex weights $w(i,j)$, up-right paths, $G(i,j) = w(i,j) + \max\{G(i-1,j), G(i,j-1)\}$. Weights (column $i = 1,2,3$ left to right, row $j$ increasing upward):

$$
w \;=\;
\begin{pmatrix}
w(1,3) & w(2,3) & w(3,3)\\
w(1,2) & w(2,2) & w(3,2)\\
w(1,1) & w(2,1) & w(3,1)
\end{pmatrix}
=
\begin{pmatrix}
0.5 & 1.1 & 0.8\\
2.1 & 0.4 & 1.9\\
0.7 & 1.3 & 0.2
\end{pmatrix}.
$$

*Geodesic from $(1,1)$.* Row by row:
$$G(1,1)=0.7,\quad G(2,1)=2.0,\quad G(3,1)=2.2,$$
$$G(1,2)=2.8,\quad G(2,2)=\max(2.8,2.0)+0.4=3.2,\quad G(3,2)=\max(3.2,2.2)+1.9=5.1,$$
$$G(1,3)=3.3,\quad G(2,3)=\max(3.3,3.2)+1.1=4.4,\quad G(3,3)=\max(5.1,4.4)+0.8=5.9 .$$
Backtracking the maximizers gives the unique geodesic
$$\Gamma_1: (1,1)\to(1,2)\to(2,2)\to(3,2)\to(3,3).$$

*Geodesic from $(2,1)$.* With $\tilde G(2,1)=1.3$: $\tilde G(3,1)=1.5$, $\tilde G(2,2)=1.7$, $\tilde G(3,2)=\max(1.7,1.5)+1.9=3.6$, $\tilde G(2,3)=2.8$, $\tilde G(3,3)=\max(3.6,2.8)+0.8=4.4$, giving
$$\Gamma_2: (2,1)\to(2,2)\to(3,2)\to(3,3).$$

The two geodesics start at distinct vertices and **coalesce at $(2,2)$**, sharing every vertex thereafter. This is the finite-volume shadow of the Licea–Newman coalescence theorem: as the target recedes to infinity in a fixed direction, the geodesic trees rooted at all vertices merge into a single one-ended tree $\mathcal{T}^+$.

**Why coalescence kills bigeodesics.** Suppose a bigeodesic $\Gamma$ exists with ends in directions $\theta$ and $-\theta$. Its forward half lies in the tree $\mathcal{T}^+_\theta$ and its backward half in $\mathcal{T}^+_{-\theta}$. Each tree is a.s. one-ended and coalescing, so $\Gamma$ is determined by the pair of trees, and the event "$0 \in \Gamma$" is measurable with respect to translation-covariant fields with density $\rho = \mathbb{P}(0 \in \Gamma)$. If $\rho > 0$, ergodicity forces $\Gamma$ to occupy a positive density of $\mathbb{Z}^2$, while coalescence forces the bigeodesics to be locally finite in number and hence of density $0$ — a contradiction. Making the density step rigorous is exactly where curvature (Licea–Newman) or exact stationarity (Balázs–Busani–Seppäläinen) is currently required; in the exponential case one replaces the density argument by a coupling that shows a stationary bi-infinite polymer would have increment process with an impossible law.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*