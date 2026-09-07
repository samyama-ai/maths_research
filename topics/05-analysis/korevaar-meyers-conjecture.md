---
id: 05-analysis/korevaar-meyers-conjecture
title: "Korevaar-Meyers Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Korevaar-Meyers Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/korevaar-meyers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A **Chebyshev-type quadrature formula** for a probability measure $\mu$ is an *equal-weight* rule
$$\int f \, d\mu \;=\; \frac{1}{N}\sum_{j=1}^{N} f(x_j), \qquad x_j \in \operatorname{supp}\mu,$$
required to be exact for every $f$ in a prescribed finite-dimensional space of polynomials. On the unit sphere $S^d \subset \mathbb{R}^{d+1}$ with normalized surface measure $\sigma$, a node set that is exact for all polynomials of total degree $\le t$ is a **spherical $t$-design**.

Korevaar and Meyers (1993) conjectured:

> **(KM)** For each $d \ge 2$ there is a constant $c_d$ such that for every $t \ge 1$ a spherical $t$-design on $S^d$ exists with
> $$N \;\le\; c_d\, t^{\,d} \quad\text{points.}$$

This is optimal in order: the Delsarte–Goethals–Seidel bound forces $N \ge \kappa_d t^d$. The order-$t^d$ form of (KM) was **proved by Bondarenko, Radchenko and Viazovska (Annals of Mathematics, 2013)**.

What remains open — and what this entry tracks — is the **quantitative and general Korevaar–Meyers problem**:

1. **(KM-const)** Determine the optimal constant $c_d^{*} = \limsup_{t\to\infty} N^{*}(d,t)/t^{d}$, where $N^{*}(d,t)$ is the minimal size of a spherical $t$-design. Even for $d=2$ no proof pins $c_2^{*}$ between the lower bound $1/4$ and the conjectured value $1/2$; the Bondarenko–Radchenko–Viazovska constant is non-effective.
2. **(KM-gen)** For a general compact $d$-dimensional domain $K \subset \mathbb{R}^n$ carrying a measure $\mu$, determine the growth exponent $\alpha(\mu)$ in $N^{*}(\mu,t) \asymp t^{\alpha(\mu)}$. This is the actual subject of Korevaar–Meyers' 1994 paper *Chebyshev-type quadrature on multidimensional domains*, and it is unresolved outside dimension one and a short list of homogeneous spaces.
3. **(KM-constr)** Produce an explicit, polynomial-time construction attaining $N = O(t^d)$; all known optimal-order proofs are non-constructive.

A complete resolution means: sharp two-sided asymptotics for $N^{*}(d,t)$ with matching constants, an exact exponent law for general $(K,\mu)$, and effective constructions.

## 2. Mathematical Foundations

Let $\mathcal{P}_t(S^d)$ denote the restriction to $S^d$ of real polynomials of degree $\le t$, with
$$\dim \mathcal{P}_t(S^d) = \binom{d+t}{d} + \binom{d+t-1}{d} \;\sim\; \frac{2\,t^{d}}{d!}.$$
Decompose $\mathcal{P}_t = \bigoplus_{\ell=0}^{t} \mathcal{H}_\ell$, where $\mathcal{H}_\ell$ is the space of spherical harmonics of degree $\ell$, $\dim \mathcal{H}_\ell = h_{\ell,d}$. A set $X=\{x_1,\dots,x_N\}$ is a $t$-design iff
$$\sum_{j=1}^{N} Y(x_j) = 0 \qquad \text{for all } Y \in \mathcal{H}_\ell,\ 1 \le \ell \le t .$$
Equivalently, via the addition formula $\sum_{k} Y_{\ell k}(x)Y_{\ell k}(y) = h_{\ell,d}\, C_\ell^{\lambda}(\langle x,y\rangle)/C_\ell^\lambda(1)$ with $\lambda=(d-1)/2$, $X$ is a $t$-design iff the **Sobolev/Weyl-sum functional**
$$A_t(X) \;=\; \sum_{\ell=1}^{t} \frac{h_{\ell,d}}{N^{2}} \sum_{i,j=1}^{N} \frac{C_\ell^{\lambda}(\langle x_i,x_j\rangle)}{C_\ell^{\lambda}(1)}$$
vanishes; $A_t \ge 0$ always, so $t$-designs are exactly the global minimizers (Sloan–Womersley variational characterization).

**Lower bound (Delsarte–Goethals–Seidel, 1977).** For $t=2e$, $N \ge \binom{d+e}{d}+\binom{d+e-1}{d}$; for $t=2e+1$, $N \ge 2\binom{d+e}{d}$. Asymptotically
$$N^{*}(d,t) \;\ge\; \frac{2}{d!}\Big(\frac{t}{2}\Big)^{d}(1+o(1)) \;=\; \frac{t^d}{2^{d-1}d!}(1+o(1)).$$
For $d=2$ this reads $N \gtrsim t^2/4$.

**Upper bound (BRV, 2013).** $N^{*}(d,t) \le c_d t^{d}$. The proof partitions $S^d$ into $N$ area-regular cells of diameter $O(N^{-1/d})$ (Kuijlaars–Saff / Feige–Schechtman partitions), considers the map sending a point configuration to its vector of harmonic sums, and applies a **topological degree** (Brouwer / Poincaré–Miranda) argument: the map has nonzero degree on a suitable convex body once $N \ge c_d t^d$, hence a zero exists.

**One-dimensional benchmark (Bernstein, Kuijlaars).** For normalized Lebesgue measure on $[-1,1]$, equal-weight quadrature exact to degree $t$ requires $N \asymp t^{2}$, *not* $N\asymp t$. For the arcsine measure $d\mu = \frac{dx}{\pi\sqrt{1-x^2}}$, the Chebyshev nodes $x_j=\cos\frac{(2j-1)\pi}{2N}$ with equal weights are exact to degree $2N-1$, i.e. $N=\lceil (t+1)/2\rceil$. So $\alpha(\mu)$ genuinely depends on $\mu$: it is $1$ for arcsine and $2$ for Lebesgue on an interval. This dichotomy — driven by the density of $\mu$ relative to the equilibrium measure — is the phenomenon (KM-gen) must explain in dimension $d>1$.

## 3. History & State of the Art (SOTA)

- **1937.** S. Bernstein shows equal-weight quadrature on $[-1,1]$ for Lebesgue measure needs $N \asymp t^2$ nodes.
- **1977.** Delsarte, Goethals, Seidel introduce spherical designs and the linear-programming lower bound.
- **1984.** Seymour and Zaslavsky prove *existence* of averaging sets (hence $t$-designs) for all sufficiently large $N$ — with no bound on how large.
- **1991.** G. Wagner gives the first explicit bound, $N = O(t^{d(d+2)})$.
- **1993–94.** Korevaar and Meyers improve this to $N = O\big(t^{(d^2+d)/2}\big)$ by potential theory and a "spherical Faraday cage" analysis of $N$ equal point charges, and state the conjecture $N=O(t^d)$. Their companion paper opens the general multidimensional-domain problem.
- **1993.** Kuijlaars determines minimal node counts for Chebyshev-type quadrature with Jacobi weights, sharpening the $d=1$ picture.
- **2008.** Chen, Frommer, Lang give computer-assisted *interval-arithmetic existence proofs* of $t$-designs on $S^2$ with $N=(t+1)^2$ points for all $t \le 100$.
- **2013.** Bondarenko, Radchenko, Viazovska prove (KM) for all $d$ and all $t$, with a non-effective $c_d$.
- **2015.** The same authors upgrade to **well-separated** designs: $\min_{i\ne j}|x_i-x_j| \ge \lambda_d N^{-1/d}$ together with $N=O(t^d)$.
- **2018–2021.** Etayo–Marzo–Ortega-Cerdà extend optimal-order designs to compact algebraic manifolds; Gariboldi–Gigante prove the analogue on general smooth compact $d$-manifolds with smooth measures.

## 4. Partial Results / Verified Cases

- **All $d\ge 2$, all $t$ (order only):** $N^{*}(d,t) \asymp t^{d}$ (BRV 2013), with well-separation (BRV 2015).
- **$d=1$ (the circle $S^1$):** exact. $N$ equispaced points form an $(N-1)$-design; $N^{*}(1,t)=t+1$, constant $c_1^{*}=1$.
- **$d=2$, small $t$:** octahedron = $3$-design ($N=6$, meets the DGS bound); icosahedron = $5$-design ($N=12$); the $600$-cell projection and other orbits give sporadic tight designs. Tight designs exist only for $t\in\{1,2,3,4,5,7,11\}$ in low dimensions (Bannai–Damerell: tight designs with $t\ge 8$, $t\ne 11$ do not exist on $S^d$, $d\ge2$).
- **$d=2$, $t \le 100$:** rigorous computational existence of $t$-designs with $N=(t+1)^2$ nodes (Chen–Frommer–Lang 2008); Womersley's numerical library extends to $t \le 325$ with $N \approx t^2/2 + t + 1$, i.e. empirically $c_2 \approx 1/2$.
- **Manifolds:** optimal-order designs on compact algebraic manifolds (Etayo–Marzo–Ortega-Cerdà 2018) and on smooth compact Riemannian $d$-manifolds with smooth positive density (Gariboldi–Gigante 2021).
- **$d=1$ intervals:** $\alpha(\mu)=1$ for the arcsine measure, $\alpha(\mu)=2$ for Lebesgue on $[-1,1]$, with full Jacobi-weight classification by Kuijlaars (1993).

## 5. Principal Obstacles

- **The BRV degree argument is inherently non-effective.** The Brouwer-degree/Poincaré–Miranda step certifies a zero of the harmonic-sum map without locating it, and the constant $c_d$ is buried in a chain of estimates on area-regular partitions and Marcinkiewicz–Zygmund inequalities. It yields no algorithm and no realistic numerical constant (the implied $c_2$ is many orders above $1/2$).
- **Linear programming saturates.** The DGS bound is the best output of the Delsarte LP for designs, and it is provably not tight for $t\ge 8$ (no tight designs exist), yet no strengthened LP or semidefinite-programming relaxation has raised the $t^d$ constant. SDP hierarchies that improved sphere *packing* and *code* bounds have not transferred: the design constraint is an equality system, not an inequality system, so positive-definite kernel arguments lose their sign structure.
- **Variational methods stall at nonconvexity.** Minimizing $A_t(X)$ over $X \in (S^d)^N$ is a nonconvex problem with exponentially many critical points; Newton-type solvers converge but produce no proof, and the interval-arithmetic certificates of Chen–Frommer–Lang scale like $N^3$ in the verification step, capping $t$ near $10^2$.
- **Potential theory does not see the exponent in $d>1$.** Korevaar–Meyers' original method — bounding the discrepancy of the potential of $N$ equal charges against the equilibrium potential — is sharp in $d=1$, where the logarithmic kernel and the equilibrium measure interact classically, but loses a factor $t^{(d^2-d)/2}$ in higher dimensions because Riesz potentials do not linearize the polynomial exactness constraints.
- **(KM-gen) lacks a candidate law.** For a domain with boundary, the interplay between the bulk (where $\alpha=d$ is plausible) and the boundary layer (where a Bernstein-type $\alpha=2$ inflation occurs, as on $[-1,1]$) is not understood. There is no conjectural formula for $\alpha(\mu)$ in terms of the density of $\mu$ against the equilibrium measure of $K$.

## 6. The Gap

Proven (Section 4): $\kappa_d t^d \le N^{*}(d,t) \le c_d t^d$ with $\kappa_d = 2^{1-d}/d!$ explicit and $c_d$ non-explicit. Conjectured/desired (Section 1): a single constant. For $d=2$ the gap is the interval
$$\tfrac14 \;\le\; \liminf \frac{N^*(2,t)}{t^2} \;\le\; \limsup \frac{N^*(2,t)}{t^2} \;\le\; c_2 ,$$
with numerics pointing at $1/2$ and no proof of *any* explicit finite $c_2$ from the BRV method. Crossing the gap requires either (a) an effective version of the degree argument — a quantitative inverse function theorem for the harmonic-sum map with controlled Jacobian on an explicit neighbourhood of a well-distributed configuration — or (b) a new lower-bound technique beating DGS, which would have to exploit the equality constraints for $\ell \le t$ jointly rather than one kernel at a time. For (KM-gen) the gap is total: no matching upper and lower exponents are known for any $d$-dimensional domain with boundary, $d\ge 2$.

## 7. Current Research (as of June 2026)

- **Effective constants for $S^2$.** Work in the Vienna/Kyiv circle around the BRV method aims to replace the degree argument by a quantitative Newton–Kantorovich scheme on area-regular partitions, which would give the first explicit $c_2$. *(frontier — verify)*
- **Manifold and measure generalizations.** Gariboldi–Gigante (Milan) and the Barcelona group (Marzo, Ortega-Cerdà, Etayo) continue extending optimal-order designs to lower-regularity measures and to weighted settings; the natural target is Ahlfors-regular sets and doubling measures.
- **QMC and statistics.** Ehler, Gräf and Oates connect designs to optimal Monte Carlo rates on manifolds; design-based cubature is now standard in kernel quadrature and Stein-discrepancy minimization.
- **Numerics.** Womersley's efficient symmetric designs with $N \approx t^2/2$ remain the empirical benchmark; extensions past $t=400$ using structured (rotationally symmetric) ansätze are being reported. *(frontier — verify)*
- **Energy-minimization crossover.** Riesz-energy minimizers and determinantal point processes are studied as candidate near-designs, with the question of whether harmonic ensembles achieve $O(t^d)$ exactness in expectation still open.

## 8. Future Work

- Extract an explicit $c_d$ from the BRV proof by quantifying the degree/homotopy step; even a crude explicit bound would be new.
- Prove or disprove the sharpened conjecture $N^{*}(2,t) = \tfrac12 t^2 + O(t)$, matching Hardin–Sloane-type numerical evidence.
- Develop a deterministic polynomial-time construction of $O(t^d)$-point designs; current explicit constructions (lattice/orbit-based) lose polynomial factors.
- Formulate and test a conjectural exponent law $\alpha(\mu)$ for Chebyshev-type quadrature on $d$-dimensional domains with boundary, guided by the arcsine-vs-Lebesgue dichotomy in $d=1$.
- Combine optimal order, well-separation, and near-optimal Riesz energy in one construction.

## 9. Key References

- **[Foundational]** P. Delsarte, J.-M. Goethals, J. J. Seidel. *Spherical codes and designs.* Geometriae Dedicata 6 (1977), 363–388.
- **[Foundational]** P. D. Seymour, T. Zaslavsky. *Averaging sets: a generalization of mean values and spherical designs.* Advances in Mathematics 52 (1984), 213–240.
- **[Foundational]** G. Wagner. *On averaging sets.* Monatshefte für Mathematik 111 (1991), 69–78.
- **[Foundational]** J. Korevaar, J. L. H. Meyers. *Spherical Faraday cage for the case of equal point charges and Chebyshev-type quadrature on the sphere.* Integral Transforms and Special Functions 1 (1993), 105–117.
- **[Foundational]** J. Korevaar, J. L. H. Meyers. *Chebyshev-type quadrature on multidimensional domains.* Journal of Approximation Theory 79 (1994), 144–164.
- **[Foundational]** A. B. J. Kuijlaars. *The minimal number of nodes in Chebyshev type quadrature formulas.* Indagationes Mathematicae 4 (1993), 339–362.
- **[SOTA]** A. Bondarenko, D. Radchenko, M. Viazovska. *Optimal asymptotic bounds for spherical designs.* Annals of Mathematics 178 (2013), 443–452.
- **[SOTA]** A. Bondarenko, D. Radchenko, M. Viazovska. *Well-separated spherical designs.* Constructive Approximation 41 (2015), 93–112.
- **[SOTA]** L. Gariboldi, G. Gigante. *Optimal asymptotic bounds for designs on manifolds.* Analysis & PDE 14 (2021), 1701–1724.
- **[SOTA]** U. Etayo, J. Marzo, J. Ortega-Cerdà. *Asymptotically optimal designs on compact algebraic manifolds.* Monatshefte für Mathematik 186 (2018), 235–248.
- **[Computational]** X. Chen, A. Frommer, B. Lang. *Computational existence proofs for spherical $t$-designs.* Numerische Mathematik 110 (2008), 725–742.
- **[Computational]** I. H. Sloan, R. S. Womersley. *A variational characterisation of spherical designs.* Journal of Approximation Theory 159 (2009), 308–318.
- **[Survey]** J. Korevaar. *Chebyshev-type quadratures: use of complex analysis and potential theory.* In *Complex Potential Theory* (NATO ASI Series C, vol. 439), Kluwer, 1994.
- **[Survey]** E. Bannai, E. Bannai. *A survey on spherical designs and algebraic combinatorics on spheres.* European Journal of Combinatorics 30 (2009), 1392–1425.

## 10. Worked Example / Concrete Special Case

**Claim.** The 8 vertices of the inscribed cube, $x_j = \tfrac{1}{\sqrt3}(\pm1,\pm1,\pm1)$, form a spherical $3$-design on $S^2$, but not a $4$-design.

*Odd degrees.* The set is invariant under $x \mapsto -x$, so every monomial of odd total degree cancels pairwise. Degrees $1$ and $3$ are exact.

*Degree 2.* Cross terms: $\sum_j x_j y_j = \tfrac13\sum (\pm1)(\pm1) = 0$, matching $\int_{S^2} xy\, d\sigma = 0$. Squares:
$$\frac18\sum_{j=1}^{8} x_j^2 = \frac18 \cdot 8 \cdot \frac13 = \frac13 = \int_{S^2} x^2 \, d\sigma .$$
So the rule is exact through degree $3$.

*Degree 4 fails.* $\frac18\sum_j x_j^4 = \frac18\cdot 8\cdot\frac19 = \frac19$, whereas $\int_{S^2} x^4 d\sigma = \frac{3}{15}=\frac15$. Since $\frac19 \ne \frac15$, the cube is exactly a $3$-design.

*Optimality check.* The DGS bound for $t=2e+1=3$ on $S^2$ ($d=2$, $e=1$) gives $N \ge 2\binom{3}{2} = 6$. The regular octahedron $\{\pm e_1,\pm e_2,\pm e_3\}$ attains it: odd degrees cancel by antipodality, $\frac16\sum x_j^2 = \frac26 = \frac13$, and $\sum x_jy_j = 0$. So $N^{*}(2,3)=6$, and the 8-point cube is suboptimal by two points.

*Where the open problem lives.* At $t=3$ the DGS bound is exact. Asymptotically it gives only $N \gtrsim t^2/4$, while the best constructions (Womersley) need $N \approx t^2/2$. For $t=100$: the bound says $N \ge 2\binom{51}{2}=2550$, numerics deliver a design with $N=5152$. The factor of $2$ between $2550$ and $5152$, persisting for every large $t$, is precisely the unresolved constant $c_2^{*}$ in the Korevaar–Meyers problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*