---
id: 03-geometry/busemann-petty-problem
title: "Busemann-Petty Problem"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Busemann–Petty Problem

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/busemann-petty-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $K, L \subset \mathbb{R}^n$ be origin-symmetric convex bodies (compact, convex, nonempty interior, $K = -K$). Suppose every central hyperplane section of $K$ is smaller than the corresponding section of $L$:

$$\operatorname{vol}_{n-1}\big(K \cap \xi^{\perp}\big) \;\le\; \operatorname{vol}_{n-1}\big(L \cap \xi^{\perp}\big) \qquad \text{for all } \xi \in S^{n-1}.$$

**Question (Busemann–Petty, 1956).** Does it follow that $\operatorname{vol}_n(K) \le \operatorname{vol}_n(L)$?

A complete resolution requires, for each $n$, either a proof of the implication or an explicit pair $(K,L)$ satisfying the section hypothesis with $\operatorname{vol}_n(K) > \operatorname{vol}_n(L)$.

**Answer (final form, 1999).** Affirmative for $n \le 4$; negative for $n \ge 5$. Symmetry and convexity are both essential: dropping either gives easy counterexamples in every dimension $n \ge 3$.

## 2. Mathematical Foundations

**Minkowski functional and radial function.** For a star body $K$ with $0$ in its interior,
$$\|x\|_K = \min\{t>0: x \in tK\}, \qquad \rho_K(\theta) = \|\theta\|_K^{-1}, \ \theta \in S^{n-1}.$$
Polar coordinates give $\operatorname{vol}_n(K) = \frac1n \int_{S^{n-1}} \rho_K^n(\theta)\, d\theta$ and, for the section,
$$\operatorname{vol}_{n-1}(K \cap \xi^{\perp}) = \frac{1}{n-1}\int_{S^{n-1}\cap \xi^{\perp}} \rho_K^{n-1}(\theta)\, d\theta .$$

**Spherical Radon transform.** $ (\mathcal{R}f)(\xi) = \int_{S^{n-1}\cap\xi^{\perp}} f(\theta)\,d\theta$, so sections are $\tfrac{1}{n-1}\mathcal{R}\big(\rho_K^{n-1}\big)$.

**Intersection bodies (Lutwak, 1988).** $IK$ is the star body with
$$\rho_{IK}(\xi) = \operatorname{vol}_{n-1}(K \cap \xi^{\perp}).$$
The class $\mathcal{I}_n$ of *intersection bodies* is the closure, in the radial metric, of $\{IK : K \text{ star body}\}$; equivalently $\rho_L = \mathcal{R}\mu$ for a nonnegative even measure $\mu$ on $S^{n-1}$.

**Lutwak's connection.** The Busemann–Petty problem has an affirmative answer in $\mathbb{R}^n$ **iff** every origin-symmetric convex body in $\mathbb{R}^n$ is an intersection body. More precisely: if $K \in \mathcal{I}_n$, the implication holds against every $L$; if $K \notin \mathcal{I}_n$, a counterexample $L$ exists (a small perturbation of $K$).

**Fourier criterion (Koldobsky, 1998).** An origin-symmetric star body $K$ is an intersection body iff the distribution $\|x\|_K^{-1}$ is positive definite, i.e. its Fourier transform (in the sense of distributions on $\mathbb{R}^n$) is a nonnegative measure. This converts a geometric membership question into positivity of
$$\big(\|x\|_K^{-1}\big)^{\wedge}(\xi).$$
Combined with the second-derivative formula for the parallel section function $A_{K,\xi}(t) = \operatorname{vol}_{n-1}(K \cap \{ \langle x,\xi\rangle = t\})$,
$$\big(\|x\|_K^{-n+1}\big)^{\wedge}(\xi) = \pi (n-1)\, A_{K,\xi}(0) \quad\text{and}\quad \big(\|x\|_K^{-2}\big)^{\wedge}(\xi) \ \propto\ -A''_{K,\xi}(0)\ \text{(smooth case)},$$
this yields a single analytic scheme covering all dimensions.

**Ball's cube-slicing theorem (1986).** For $Q = [-1/2,1/2]^n$, $\ \operatorname{vol}_{n-1}(Q\cap\xi^\perp) \le \sqrt{2}$ for all $\xi$, with $1$ as the lower bound. This is the sharpest input to the negative side.

## 3. History & State of the Art

- **1956.** Busemann and Petty pose ten problems in *Math. Scand.*; Problem 1 is the section–volume comparison, arising from Busemann's work on volumes in Minkowski spaces.
- **1975.** Larman and Rogers give the first counterexample, in dimension $n \ge 12$, by a probabilistic construction.
- **1986–88.** Ball's cube-slicing bound $\sqrt2$ gives a clean counterexample for $n \ge 10$; Lutwak introduces intersection bodies and reduces the whole problem to membership in $\mathcal{I}_n$.
- **1990–92.** Giannopoulos and, independently, Bourgain lower the negative range to $n \ge 7$; Papadimitrakis and Gardner reach $n \ge 5$.
- **1994.** Gardner proves the affirmative answer for $n = 3$ using a Radon-transform / point-symmetric section argument (*Annals of Mathematics*).
- **1999.** Zhang proves the affirmative answer for $n = 4$, showing every origin-symmetric convex body in $\mathbb{R}^4$ is an intersection body — reversing his own earlier claim. Simultaneously Gardner, Koldobsky and Schlumprecht give a unified Fourier-analytic solution in all dimensions, based on the sign of $A''_{K,\xi}(0)$ under the Fourier transform.
- **2000–present.** The methodology (Fourier transforms of powers of the Minkowski functional) becomes a standard tool; extensions to lower-dimensional sections, complex bodies, general measures, and $L_p$-analogues follow.

## 4. Partial Results / Verified Cases

| Case | Answer | Source |
|---|---|---|
| $n = 2$ | Yes (trivial: $\rho$-comparison) | classical |
| $n = 3$ | Yes | Gardner 1994 |
| $n = 4$ | Yes | Zhang 1999; GKS 1999 |
| $n \ge 5$ | **No** | Papadimitrakis 1992; Gardner 1994; GKS 1999 |
| $n \ge 7$ | No | Giannopoulos 1990; Bourgain 1991 |
| $n \ge 10$ | No (cube vs. ball) | Ball 1988 |
| $n \ge 12$ | No | Larman–Rogers 1975 |

**Classes with an affirmative answer in every dimension** (i.e. bodies $K \in \mathcal{I}_n$):
- Balls and ellipsoids; more generally, unit balls of $\ell_p^n$ for $0 < p \le 2$ (Koldobsky). For $p > 2$ and $n \ge 5$, $B_p^n \notin \mathcal{I}_n$; in particular the cube $B_\infty^n$ fails for $n\ge5$.
- Bodies of revolution in $\mathbb{R}^4$ (Zhang), and generalized $k$-intersection bodies.
- Small perturbations of the Euclidean ball in any dimension (Bourgain 1991).
- Polar projection bodies $\Pi^*M$ and zonoid-type duals.

**Extensions.**
- *Lower-dimensional sections* ($k$-dimensional, $1\le k \le n-1$): negative for $4 \le k < n$ (Bourgain–Zhang 1999; corrected/extended by Rubin–Zhang 2004). Open for $k = 2, 3$.
- *Complex bodies:* affirmative for complex dimension $n \le 3$, negative for $n \ge 4$ (Koldobsky–König–Zymonopoulou 2008).
- *Arbitrary measures:* Zvavitch (2005) proved the same $n\le4$/$n\ge5$ dichotomy when $\operatorname{vol}$ is replaced by any measure with even continuous density.
- *Isomorphic version:* $\operatorname{vol}_n(K) \le C\,\operatorname{vol}_n(L)$ with $C$ absolute is equivalent to boundedness of the isotropic constant; Klartag–Lehec's 2024–25 resolution of Bourgain's slicing problem therefore settles it affirmatively. *(frontier — verify final published form)*

## 5. Principal Obstacles

The problem is settled for hyperplane sections; the obstacles now concern its surviving relatives and the structural theory behind it.

- **No characterization of $k$-intersection bodies.** Koldobsky's criterion says $K$ is a $k$-intersection body iff $\|x\|_K^{-k}$ is a positive definite distribution. For $k=1$ this is checkable via $A''_{K,\xi}(0)$, whose sign is controlled by convexity in low dimensions. For $k = 2,3$ no comparable second-order geometric quantity is known, so neither positivity proofs nor explicit failures are available.
- **The counterexample machinery needs room.** Bourgain–Zhang's negative construction for $k \ge 4$ uses a perturbation whose Fourier transform must change sign on a set of directions of positive measure; for $k = 2,3$ the perturbation is swallowed by the smoothing of the $k$-plane Radon transform.
- **Dimension is a genuine threshold, not an artifact.** Convexity forces $A_{K,\xi}$ to be $\tfrac{1}{n-1}$-concave; the induced positivity of $-A''_{K,\xi}(0)$-type quantities holds only for $n\le4$. There is no perturbative or interpolation argument that carries the $n=4$ proof upward, and none should exist.
- **Non-symmetric bodies.** Without $K=-K$ the Fourier machinery loses evenness and the Radon transform is no longer injective on the relevant class; the general non-symmetric comparison problem has no clean formulation.

## 6. The Gap

For the original question there is no gap: the answer is complete. The live boundary is:

1. **Lower-dimensional BP for $k = 2, 3$.** Precisely: if $\operatorname{vol}_k(K\cap H) \le \operatorname{vol}_k(L\cap H)$ for all $k$-dimensional central subspaces $H$, does $\operatorname{vol}_n(K)\le\operatorname{vol}_n(L)$? Equivalent to: is every origin-symmetric convex body in $\mathbb{R}^n$ a $k$-intersection body for $k=2,3$? Known false for $k\ge4$, known true for $n\le4$.
2. **Sharp constant in the isomorphic problem.** The best $C$ with $\operatorname{vol}_n(K)\le C\operatorname{vol}_n(L)$ is conjectured to be $\sqrt{2}$-like (attained near cube/ball); current bounds via slicing constants are far larger.

## 7. Current Research (as of June 2026)

- **Fourier/harmonic-analytic school** (Koldobsky, Yaskin, Zvavitch, Zymonopoulou; Missouri–Columbia, Oklahoma, Kent State): positive-definiteness criteria, $k$-intersection bodies, comparison problems for general measures and for the $L_p$-Brunn–Minkowski framework.
- **Slicing-constant program** (Klartag, Lehec, Guan; Weizmann, Paris, and the localization/stochastic-flow community): the affirmative resolution of Bourgain's slicing problem gives dimension-free isomorphic section–volume comparison and is being pushed toward explicit constants. *(frontier — verify)*
- **Geometric tomography** (Gardner and collaborators): dual Brunn–Minkowski theory, stability versions — if sections of $K$ exceed those of $L$ by at most $\varepsilon$, how much can volumes invert.
- **Discrete analogues**: lattice-point versions of Busemann–Petty (counting $|K\cap\xi^\perp\cap\mathbb{Z}^n|$) studied by Alexander, Henk, Zvavitch, with a mostly negative picture already for small $n$. *(frontier — verify)*

## 8. Future Work

- Settle $k=2,3$ in the lower-dimensional problem; a plausible route is a second-order positivity criterion for $\|x\|_K^{-2}$ analogous to $A''_{K,\xi}(0)$, or a random-perturbation counterexample with controlled Fourier sign.
- Determine the optimal constant in the isomorphic Busemann–Petty inequality now that isotropic constants are bounded.
- Extend the dichotomy to log-concave and $s$-concave measures with non-even densities, where Zvavitch's argument does not apply.
- Develop stability and rigidity statements: characterize equality cases in $\operatorname{vol}(K)\le\operatorname{vol}(L)$ for $n\le4$.

## 9. Key References

- **[Foundational]** H. Busemann, C. M. Petty. *Problems on convex bodies.* Mathematica Scandinavica 4 (1956), 88–94.
- **[Foundational]** D. G. Larman, C. A. Rogers. *The existence of a centrally symmetric convex body with central sections that are unexpectedly small.* Mathematika 22 (1975), 164–175.
- **[Foundational]** K. Ball. *Cube slicing in $\mathbb{R}^n$.* Proceedings of the AMS 97 (1986), 465–473.
- **[Foundational]** E. Lutwak. *Intersection bodies and dual mixed volumes.* Advances in Mathematics 71 (1988), 232–261.
- **[Milestone]** J. Bourgain. *On the Busemann–Petty problem for perturbations of the ball.* Geometric and Functional Analysis 1 (1991), 1–13.
- **[Milestone]** M. Papadimitrakis. *On the Busemann–Petty problem about convex, centrally symmetric bodies in $\mathbb{R}^n$.* Mathematika 39 (1992), 258–266.
- **[Milestone]** R. J. Gardner. *A positive answer to the Busemann–Petty problem in three dimensions.* Annals of Mathematics 140 (1994), 435–447.
- **[Milestone]** R. J. Gardner. *Intersection bodies and the Busemann–Petty problem.* Transactions of the AMS 342 (1994), 435–445.
- **[SOTA]** G. Zhang. *A positive solution to the Busemann–Petty problem in $\mathbb{R}^4$.* Annals of Mathematics 149 (1999), 535–543.
- **[SOTA]** R. J. Gardner, A. Koldobsky, T. Schlumprecht. *An analytic solution to the Busemann–Petty problem on sections of convex bodies.* Annals of Mathematics 149 (1999), 691–703.
- **[SOTA]** A. Koldobsky. *Intersection bodies, positive definite distributions, and the Busemann–Petty problem.* American Journal of Mathematics 120 (1998), 827–840.
- **[Extension]** J. Bourgain, G. Zhang. *On a generalization of the Busemann–Petty problem.* In *Convex Geometric Analysis*, MSRI Publications 34, Cambridge University Press, 1999, 65–76.
- **[Extension]** B. Rubin, G. Zhang. *Generalizations of the Busemann–Petty problem for sections of convex bodies.* Journal of Functional Analysis 213 (2004), 473–501.
- **[Extension]** A. Zvavitch. *The Busemann–Petty problem for arbitrary measures.* Mathematische Annalen 331 (2005), 867–887.
- **[Extension]** A. Koldobsky, H. König, M. Zymonopoulou. *The complex Busemann–Petty problem on sections of convex bodies.* Advances in Mathematics 218 (2008), 352–367.
- **[Survey]** R. J. Gardner. *Geometric Tomography.* 2nd edition, Cambridge University Press, 2006.
- **[Survey]** A. Koldobsky. *Fourier Analysis in Convex Geometry.* Mathematical Surveys and Monographs 116, AMS, 2005.
- **[Survey]** A. Koldobsky, V. Yaskin. *The Interface between Convex Geometry and Harmonic Analysis.* CBMS Regional Conference Series 108, AMS, 2008.

## 10. Worked Example / Concrete Special Case

**Ball's counterexample: cube versus ball in $\mathbb{R}^{10}$.**

Take $K = Q = [-\tfrac12,\tfrac12]^{10}$, so $\operatorname{vol}_{10}(Q) = 1$. Ball's theorem gives
$$\operatorname{vol}_{9}(Q\cap\xi^{\perp}) \le \sqrt2 \approx 1.41421 \quad \text{for every } \xi \in S^{9}.$$

Let $L = rB_2^{10}$, a centered Euclidean ball of radius $r$. Its central sections all have volume $\omega_9 r^{9}$, where $\omega_k = \pi^{k/2}/\Gamma(\tfrac k2+1)$. Choose $r$ so the ball's sections dominate the cube's:
$$\omega_9 r^9 = \sqrt2, \qquad \omega_9 = \frac{\pi^{4.5}}{\Gamma(5.5)} = \frac{172.80}{52.3428} = 3.2985,$$
$$r = \left(\frac{1.41421}{3.2985}\right)^{1/9} = (0.42874)^{1/9} = 0.91018 .$$
Then $\operatorname{vol}_{9}(Q\cap\xi^\perp) \le \sqrt2 = \operatorname{vol}_9(L\cap\xi^\perp)$ for all $\xi$: the section hypothesis holds with $K=Q$, $L=rB_2^{10}$.

Now compare volumes, with $\omega_{10} = \pi^5/120 = 2.5502$:
$$\operatorname{vol}_{10}(L) = \omega_{10} r^{10} = 2.5502 \times (0.91018)^{10} = 2.5502 \times 0.39018 = 0.9951 < 1 = \operatorname{vol}_{10}(Q).$$

Every central section of the cube is at most that of the ball, yet the cube has strictly larger volume — a negative answer in $\mathbb{R}^{10}$.

**Why the same computation fails in $\mathbb{R}^9$.** With $\omega_8 = \pi^4/24 = 4.0587$, the radius is $r = (\sqrt2/4.0587)^{1/8} = 0.87653$ and
$$\omega_9 r^9 = 3.2985 \times (0.87653)^{9} = 3.2985 \times 0.30541 = 1.0074 > 1.$$
The ball is now *bigger* than the cube, so no contradiction arises. The cube–ball pair crosses the threshold exactly at $n = 10$; reaching $n = 5$ required replacing the ball by a fine perturbation of the cube and testing membership in $\mathcal{I}_n$ directly — which is what Papadimitrakis, Gardner, and Gardner–Koldobsky–Schlumprecht did.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*