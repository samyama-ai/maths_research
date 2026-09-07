---
id: 05-analysis/marstrand-projection-generalizations
title: "Marstrand Projection Generalizations"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Marstrand Projection Generalizations

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/marstrand-projection-generalizations` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Marstrand's 1954 theorem says that for a Borel set $A \subset \mathbb{R}^2$, almost every orthogonal projection preserves dimension: $\dim_H \pi_\theta A = \min(\dim_H A, 1)$ for Lebesgue-a.e. $\theta$. The generalization program asks for **quantitative and structural refinements** of "almost every":

1. **Exceptional-set problem (Falconer/Oberlin).** For $A \subset \mathbb{R}^n$ Borel with $\dim_H A = s$ and $0 \le u \le \min(s,k)$, bound
$$E_u(A) = \{ V \in G(n,k) : \dim_H \pi_V A < u \}.$$
The conjectured sharp bound in the plane ($n=2$, $k=1$) is $\dim_H E_u(A) \le \max(0, 2u - s)$. In general dimension the conjecture is $\dim_H E_u(A) \le k(n-k) + u - s$ when $u \le s$, and the sharp form for all $(n,k,s,u)$ is open.
2. **Restricted families.** If $\gamma \subset G(n,k)$ is a curve or lower-dimensional submanifold, does Marstrand's conclusion still hold for a.e. parameter on $\gamma$? This fails for arbitrary $\gamma$ and is conjectured to hold for all *nondegenerate* $\gamma$.
3. **Non-Euclidean and nonlinear settings.** Projections in Heisenberg groups, along algebraic/nonlinear families, radial projections, and projections of measures rather than sets.

A complete resolution means: sharp exceptional-set dimension bounds in every $(n,k)$; a full nondegeneracy criterion for restricted families; and matching examples showing sharpness.

## 2. Mathematical Foundations

Let $G(n,k)$ be the Grassmannian of $k$-planes in $\mathbb{R}^n$, with $\dim G(n,k) = k(n-k)$, carrying the $O(n)$-invariant measure $\gamma_{n,k}$. For $V \in G(n,k)$ let $\pi_V : \mathbb{R}^n \to V$ be orthogonal projection. In the plane write $\pi_\theta(x) = x \cdot (\cos\theta, \sin\theta)$.

**$s$-energy and Frostman measures.** For a Radon measure $\mu$ with compact support,
$$I_s(\mu) = \iint |x-y|^{-s} \, d\mu(x)\, d\mu(y), \qquad \widehat{\mu}(\xi) = \int e^{-2\pi i \xi \cdot x} d\mu(x).$$
Frostman's lemma: $\dim_H A = \sup\{ s : \exists \mu \in \mathcal{M}(A),\ I_s(\mu) < \infty \}$.

**Kaufman's identity.** For $s < 1$ and $\mu$ on $\mathbb{R}^2$,
$$\int_0^\pi I_s(\pi_{\theta\sharp}\mu)\, d\theta = c_s I_s(\mu) ,$$
because $\int_0^\pi |x\cdot e_\theta|^{-s} d\theta = c_s |x|^{-s}$. Finiteness of the left side for a.e. $\theta$ gives Marstrand's theorem. For $s>1$ the Fourier version gives $\|\pi_{\theta\sharp}\mu\|_{L^2}^2 < \infty$ a.e., hence positive Lebesgue measure.

**Sobolev dimension (Peres–Schlag).** $\dim_S \mu = \sup\{ t : \int |\widehat{\mu}(\xi)|^2 |\xi|^{t-n} d\xi < \infty \}$; transversality of the family $\{\pi_V\}$ transfers Sobolev regularity to a.e. parameter.

**Furstenberg sets.** $F \subset \mathbb{R}^2$ is an $(s,t)$-Furstenberg set if there is a set of lines $\mathcal{L}$ with $\dim_H \mathcal{L} \ge t$ such that $\dim_H(F \cap \ell) \ge s$ for all $\ell \in \mathcal{L}$. The Furstenberg conjecture asserts
$$\dim_H F \ \ge\ \min\Big( s+t,\ \tfrac{3s+t}{2},\ s+1 \Big),$$
and is *dual* to the sharp planar exceptional-set estimate.

**Nondegenerate curves in $\mathbb{R}^3$.** $\gamma : I \to S^2$ is nondegenerate if $\det(\gamma, \gamma', \gamma'') \ne 0$ on $I$. The restricted projections are $\pi_{\gamma(\theta)}(x) = x \cdot \gamma(\theta)$ (onto lines) and $\rho_\theta(x) = $ projection onto $\gamma(\theta)^\perp$ (onto planes).

## 3. History & State of the Art (SOTA)

- **1954** — J. M. Marstrand proves the projection theorem in $\mathbb{R}^2$ by geometric-measure arguments (density and covering).
- **1968** — R. Kaufman gives the potential-theoretic proof above, the template for essentially everything since.
- **1975** — P. Mattila extends to $\pi_V$, $V \in G(n,k)$, and adds slicing counterparts; Kaufman–Mattila produce examples showing $\dim_H E_u(A) \ge u$ is attainable.
- **1982** — K. Falconer proves $\dim_H E_u(A) \le \max(0, k(n-k) + u - s)$ for $u \le \min(s,k)$ in a range, and conjectures the sharp form.
- **2000** — Peres–Schlag develop the transversality/Sobolev-dimension machinery, giving exceptional bounds for large classes of parametrized (nonlinear) families.
- **2003/2010** — Bourgain's discretized ring and sum-product theorems yield the first $\varepsilon$-improvement: for $\dim_H A = s \le 1$ in the plane, $\dim_H E_{s/2}(A) = 0$, and more generally an $\varepsilon(s)$ gain beyond Kaufman's bound.
- **2012** — Hochman–Shmerkin: for self-similar/dynamically defined sets with irrational rotations, *every* projection has full dimension (no exceptions at all).
- **2022–2023** — Orponen–Shmerkin–Wang settle Kaufman- and Falconer-type estimates for **radial** projections and deduce a continuum Beck theorem; Ren–Wang prove the full Furstenberg set conjecture in the plane, which yields the sharp planar exceptional-set bound $\dim_H E_u(A) \le \max(0, 2u-s)$.
- **2022–2024** — Restricted projections in $\mathbb{R}^3$ resolved for nondegenerate curves: Käenmäki–Orponen–Venieri (Kaufman range), Pramanik–Yang–Zahl (general nondegenerate curves), Gan–Guo–Guth–Harris–Maldague–Wang (planes, via $\ell^2$ decoupling for the cone).

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$, $k=1$, all $s$ | **Sharp**: $\dim_H E_u(A) \le \max(0, 2u-s)$ | Ren–Wang 2023 (via Furstenberg) |
| $n=2$, $u=s\le 1$ | $\dim_H E_s(A) \le s$ (Kaufman) | Kaufman 1968 |
| $n=2$, $s>1$, positive measure | $\dim_H\{\theta: |\pi_\theta A| = 0\} \le 2-s$ | Falconer 1982 |
| General $n,k$ | $\dim_H E_u(A) \le k(n-k) + u - s$ for $u\le s$ | Mattila 1975, Falconer 1982 |
| Discretized, $s<1$ | $\varepsilon$-improvement over Kaufman | Bourgain 2010; He 2020 |
| Self-similar sets, dense rotations | $\dim_H \pi_\theta A = \min(\dim A,1)$ for **all** $\theta$ | Hochman–Shmerkin 2012 |
| $\mathbb{R}^3$, nondegenerate curve $\gamma$, lines | a.e. $\theta$: $\dim \pi_{\gamma(\theta)}A = \min(\dim A,1)$ | Pramanik–Yang–Zahl 2022 |
| $\mathbb{R}^3$, nondegenerate curve, planes | a.e. $\theta$: $\dim \rho_\theta A = \min(\dim A,2)$ | Gan–Guo–Guth–Harris–Maldague–Wang 2022 |
| Radial projections $\pi_x(y)=\frac{y-x}{|y-x|}$ | Sharp Kaufman/Falconer analogues in $\mathbb{R}^n$ | Orponen–Shmerkin–Wang 2024; Ren 2023 |
| Heisenberg group $\mathbb{H}^1$ | Marstrand-type bounds, with genuine dimension loss | Balogh–Fässler–Mattila–Tyson 2012 |
| Packing/box dimension | $\dim_P \pi_V A$ constant a.e., but not $=\min(\dim_P A,k)$ | Falconer–Howroyd 1996 |

## 5. Principal Obstacles

- **Kaufman's integral is lossy at the top.** The energy identity $\int I_s(\pi_{\theta\sharp}\mu)\,d\theta = c_s I_s(\mu)$ gives only the $L^1$ average; Chebyshev then yields $\dim E_u \le u$, which is sharp only for the extreme configurations. Any improvement must exploit *structure* of the exceptional set (that it is line-rich), not just integrability — this is exactly the Furstenberg duality, and it is nonlinear.
- **Higher dimensions lack a Furstenberg dual.** Ren–Wang's proof runs on the $\delta$-discretized incidence geometry of points and lines in the plane, using high–low decomposition and induction on scales. In $G(n,k)$ with $k(n-k) > 1$ the dual object is a $k$-plane–incidence problem with no known sharp counting theorem; Kakeya-type obstructions enter.
- **Sum-product barriers.** Bourgain's $\varepsilon$ is not effective in any useful range; the discretized sum-product theorem underlying it produces gains of size $\exp(-C/\varepsilon)$ or worse, so it cannot reach sharp exponents.
- **Restricted families are curvature-dependent.** For a degenerate curve (e.g. $\gamma$ contained in a plane) the theorem is simply false, so any general criterion must quantify nondegeneracy; current proofs consume the full strength of $\ell^2$ decoupling for the cone or of Zahl-style incidence machinery, both tied to specific low-dimensional geometry.
- **Non-Euclidean projections are not group-invariant.** In $\mathbb{H}^n$ the horizontal and vertical projections are not Lipschitz in the same metric, so the transversality hypotheses of Peres–Schlag fail and dimension genuinely drops.

## 6. The Gap

The plane is closed. The gap is everything above it and off it:

1. **$G(n,k)$ for $k(n-k)\ge 2$.** Known: $\dim_H E_u(A) \le k(n-k)+u-s$. Conjectured sharp for all $u \le \min(s,k)$; the missing step is a $k$-plane Furstenberg estimate — i.e. a lower bound on $\dim_H F$ for sets meeting a $t$-dimensional family of $k$-planes in dimension $s$ — with no current technique giving the sharp exponent.
2. **Restricted families beyond curves in $\mathbb{R}^3$.** No general theorem for $m$-dimensional nondegenerate submanifolds of $G(n,k)$; even the correct nondegeneracy condition is conjectural (Fässler–Orponen).
3. **Sharpness examples.** In several regimes it is not known whether the conjectured bound or the known bound is the truth, because no construction matches either.

## 7. Current Research (as of June 2026)

- **Ren–Wang program.** Ren and Wang's Furstenberg resolution has been absorbed into a general "$\delta$-discretized projection" toolkit; extensions to $G(n,1)$ and to $\mathbb{C}^2$ are being pursued. *(frontier — verify)*
- **Higher-rank Furstenberg.** Work of Zahl, Bruce–Ren, and Orponen's group on $(s,t)$-Furstenberg problems for $k$-planes in $\mathbb{R}^n$; partial results in $G(3,2)$. *(frontier — verify)*
- **Decoupling-driven restricted projections.** Gan, Guth, Maldague and collaborators push cone/ moment-curve decoupling to restricted families in $\mathbb{R}^4$ and higher. *(frontier — verify)*
- **Institutions.** Jyväskylä/Helsinki (Orponen, Mattila school), MIT (Guth, Wang), UBC (Pramanik, Zahl), UT Austin/Bar-Ilan (Shmerkin, Hochman).
- **Applications** to the Falconer distance-set problem, Erdős-type incidence problems, and the continuum Beck theorem drive much of the current activity.

## 8. Future Work

- Formulate and prove the sharp **$k$-plane Furstenberg estimate**; this would automatically give the general Falconer exceptional-set conjecture by duality.
- Identify the correct **nondegeneracy invariant** for submanifolds $\gamma \subset G(n,k)$ and prove a restricted Marstrand theorem under it.
- Develop **effective** discretized sum-product bounds with polynomial rather than exponential loss.
- Extend to **nonlinear projections** (algebraic maps, projections along vector fields) and to **Heisenberg / Carnot groups**, where sharp constants are unknown.
- Push the **measure-theoretic** refinements: exact-dimensionality, $L^q$ dimensions, and Fourier dimension of projected measures.

## 9. Key References

- **[Foundational]** J. M. Marstrand. *Some fundamental geometrical properties of plane sets of fractional dimensions.* Proc. London Math. Soc. (3) **4** (1954), 257–302.
- **[Foundational]** R. Kaufman. *On Hausdorff dimension of projections.* Mathematika **15** (1968), 153–155.
- **[Foundational]** P. Mattila. *Hausdorff dimension, orthogonal projections and intersections with planes.* Ann. Acad. Sci. Fenn. Ser. A I Math. **1** (1975), 227–244.
- **[Foundational]** K. J. Falconer. *Hausdorff dimension and the exceptional set of projections.* Mathematika **29** (1982), 109–115.
- **[Structural]** Y. Peres, W. Schlag. *Smoothness of projections, Bernoulli convolutions, and the dimension of exceptions.* Duke Math. J. **102** (2000), 193–251.
- **[Structural]** J. Bourgain. *The discretized sum-product and projection theorems.* J. Anal. Math. **112** (2010), 193–236.
- **[Structural]** M. Hochman, P. Shmerkin. *Local entropy averages and projections of fractal measures.* Ann. of Math. **175** (2012), 1001–1059.
- **[SOTA]** K. Ren, H. Wang. *Furstenberg sets estimate in the plane.* arXiv:2308.08819 (2023).
- **[SOTA]** T. Orponen, P. Shmerkin, H. Wang. *Kaufman and Falconer estimates for radial projections and a continuum version of Beck's theorem.* Geom. Funct. Anal. (2024); arXiv:2209.00348.
- **[SOTA]** S. Gan, S. Guo, L. Guth, T. L. J. Harris, D. Maldague, H. Wang. *On restricted projections to planes in $\mathbb{R}^3$.* arXiv:2207.13844 (2022).
- **[SOTA]** M. Pramanik, T. Yang, J. Zahl. *A Furstenberg-type problem for circles, and a Kaufman-type restricted projection theorem in $\mathbb{R}^3$.* arXiv:2207.02259 (2022).
- **[Related]** Z. Balogh, K. Fässler, P. Mattila, J. Tyson. *Projection and slicing theorems in Heisenberg groups.* Adv. Math. **231** (2012), 569–604.
- **[Related]** K. Falconer, J. Howroyd. *Projection theorems for box and packing dimensions.* Math. Proc. Cambridge Philos. Soc. **119** (1996), 287–295.
- **[Related]** R. Kenyon. *Projecting the one-dimensional Sierpinski gasket.* Israel J. Math. **97** (1997), 221–238.
- **[Survey]** P. Mattila. *Fourier Analysis and Hausdorff Dimension.* Cambridge University Press, 2015.
- **[Survey]** K. Falconer, J. Fraser, X. Jin. *Sixty years of fractal projections.* In *Fractal Geometry and Stochastics V*, Birkhäuser, 2015, 3–25.

## 10. Worked Example / Concrete Special Case

**The four-corner Cantor set.** Let $K = C \times C \subset [0,1]^2$, where $C$ is the middle-half Cantor set (ratio $1/4$, two pieces). Then $\dim_H C = \frac{\log 2}{\log 4} = \frac12$, so
$$\dim_H K = \tfrac12 + \tfrac12 = 1, \qquad 0 < \mathcal{H}^1(K) < \infty .$$

*Marstrand gives:* $\dim_H \pi_\theta K = 1$ for a.e. $\theta$. Since $\mathcal{H}^1(K)<\infty$ and $K$ is purely 1-unrectifiable, **Besicovitch's projection theorem** gives the stronger statement $|\pi_\theta K| = 0$ for a.e. $\theta$ — full dimension, zero length. So "dimension is preserved" is the sharpest true conclusion.

*Exceptional directions exist.* Take $\theta$ with slope $\tan\theta = 1/2$, i.e. projection along direction $(2,1)$. Writing $K$'s points as $\left(\sum_{n\ge1} 3a_n 4^{-n}, \sum_{n\ge1} 3b_n 4^{-n}\right)$ with $a_n,b_n \in \{0,1\}$, the projection onto the unit vector $\frac{1}{\sqrt5}(1,-2)$ is proportional to
$$\sum_{n\ge 1} 3(a_n - 2b_n)\,4^{-n}, \qquad a_n - 2b_n \in \{-2,-1,0,1\}.$$
Four digit values in base 4 with two-bit input: the map $(a_n,b_n)\mapsto a_n-2b_n$ is a bijection onto $\{-2,-1,0,1\}$, so the projection covers a full interval. Hence $|\pi_\theta K| > 0$ in this direction — a genuine *exceptional* direction, but exceptional in the "too large" direction. Kenyon (1997) classified exactly which rational slopes give positive measure for such sets.

*Checking the exceptional-set bound.* Here $s = \dim_H K = 1$. Take $u = 1$. The sharp planar estimate (Kaufman; equality case of Ren–Wang) gives
$$\dim_H\{\theta : \dim_H \pi_\theta K < 1\} \le \max(0, 2u - s) = \max(0, 2\cdot 1 - 1) = 1,$$
which is vacuous — reflecting that at $s=u=1$ the theorem gives nothing beyond measure zero. Take instead $A \subset K$ with $\dim_H A = s = 1/2$ and $u = 1/4$: the bound reads $\dim_H E_{1/4}(A) \le 2(1/4) - 1/2 = 0$, so **every** direction outside a zero-dimensional set projects $A$ to dimension at least $1/4$. Kaufman's classical bound would only have given $\dim_H E_{1/4}(A) \le 1/4$. That gap — $0$ versus $1/4$ — is exactly what Ren–Wang closed in the plane, and exactly what remains open in $G(n,k)$ for $k(n-k) \ge 2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*