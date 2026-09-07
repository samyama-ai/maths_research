---
id: 05-analysis/bourgain-slicing-problem
title: "Bourgain Slicing Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bourgain Slicing Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bourgain-slicing-problem` · **Status:** solved-recently

**Editorial note.** The catalog request listed this entry as `open`. That is no longer accurate: the qualitative conjecture was resolved affirmatively in December 2024 by Klartag and Lehec, building on a heat-flow estimate of Guan. The status field records `solved-recently`; the sharp-constant and extremal-body questions (Sections 6–8) remain open.

## 1. Problem Statement / Conjecture

**Slicing (hyperplane) problem, Bourgain 1986.** Does there exist a universal constant $c>0$, independent of dimension, such that every convex body $K\subset\mathbb{R}^n$ of volume $1$ has a hyperplane section of area at least $c$? Formally:

$$\exists\, c>0 \ \ \forall n\ \ \forall K\subset\mathbb{R}^n \text{ convex},\ |K|=1:\quad \max_{\theta\in S^{n-1},\,t\in\mathbb{R}} \ \big|K\cap\{x:\langle x,\theta\rangle=t\}\big|_{n-1}\ \ge\ c .$$

Equivalently (Section 2): is the isotropic constant $L_n=\sup_{K\subset\mathbb{R}^n}L_K$ bounded uniformly in $n$?

A complete proof requires a dimension-free lower bound $c$ valid for all $n$ and all convex bodies; a disproof requires a sequence $K_n$ with maximal section volume $\to 0$. The question was **answered affirmatively** by Klartag–Lehec (arXiv:2412.15044, 2024), who proved $L_n\le C$ for an explicit universal $C$.

## 2. Mathematical Foundations

Let $K\subset\mathbb{R}^n$ be a convex body (compact, convex, nonempty interior), $|K|$ its Lebesgue measure. Write the covariance matrix of the uniform measure on $K$:

$$\operatorname{Cov}(K)_{ij}=\frac{1}{|K|}\int_K x_ix_j\,dx-\frac{1}{|K|^2}\int_K x_i\,dx\int_K x_j\,dx .$$

The **isotropic constant** is

$$L_K=\left(\frac{\det\operatorname{Cov}(K)}{|K|^{2}}\right)^{1/(2n)},$$

which is invariant under invertible affine maps. $K$ is **isotropic** if $|K|=1$, its barycenter is $0$, and $\operatorname{Cov}(K)=L_K^2\,\mathrm{Id}$, i.e.

$$\int_K\langle x,\theta\rangle^2\,dx=L_K^2\qquad\text{for all }\theta\in S^{n-1}.$$

Every convex body has an isotropic affine image, unique up to orthogonal maps.

**Link to sections (Hensley 1980; Ball 1988).** For $K$ isotropic and any $\theta\in S^{n-1}$,

$$\frac{c_1}{L_K}\ \le\ |K\cap\theta^{\perp}|_{n-1}\ \le\ \frac{c_2}{L_K},$$

with $c_1,c_2>0$ absolute (one may take $c_1=1/\sqrt{12}$-type and $c_2=1/\sqrt{2}$-type constants after normalization). Hence "all sections small" $\iff$ "$L_K$ large", and the slicing problem is exactly the boundedness of $L_n$.

**Log-concave formulation (Ball 1988).** For a log-concave probability density $f=e^{-V}$ on $\mathbb{R}^n$ with $V$ convex, barycenter $0$, set

$$L_f=\big(\sup f\big)^{1/n}\,\big(\det\operatorname{Cov}(f)\big)^{1/(2n)} .$$

Then $\sup_f L_f\asymp \sup_K L_K$: the convex-body and log-concave settings are equivalent up to absolute constants, via Ball's bodies $K_p(f)$.

**Isoperimetric neighbours.** The **thin-shell** constant $\sigma_n$ is the least $\sigma$ with $\operatorname{Var}|X|\le\sigma^2$ for every isotropic log-concave $X$ (normalized $\mathbb{E}|X|^2=n$); the **KLS** constant $\psi_n$ is the reciprocal of the worst Cheeger constant of isotropic log-concave measures. Eldan–Klartag (2011) proved $L_n\lesssim\sigma_n$, and Eldan (2013) proved $\sigma_n\lesssim\psi_n\lesssim\sigma_n\sqrt{\log n}$, so

$$L_n\ \lesssim\ \sigma_n\ \lesssim\ \psi_n .$$

## 3. History & State of the Art (SOTA)

- **1986** — Bourgain poses the problem in *On high-dimensional maximal functions associated to convex bodies* (Amer. J. Math. 108), where boundedness of $L_n$ controls a maximal operator.
- **1989** — Milman–Pajor systematize the isotropic position, prove $L_K\le C$ for unconditional bodies and zonoids, and connect $L_n$ to the isomorphic Busemann–Petty problem.
- **1991** — Bourgain proves $L_n\lesssim n^{1/4}\log n$ using a $\psi_1$/Paley–Zygmund argument on linear functionals.
- **2006** — Klartag removes the logarithm: $L_n\lesssim n^{1/4}$, by an isomorphic perturbation to a body of bounded volume ratio.
- **2011–2013** — Eldan–Klartag reduce slicing to thin-shell; Eldan introduces **stochastic localization**, tying thin-shell to KLS.
- **2021** — Chen: $\psi_n\le n^{o(1)}$, hence $L_n\le n^{o(1)}$ — the first sub-polynomial bound.
- **2022** — Klartag–Lehec: $L_n\lesssim(\log n)^4$; Jambulapati–Lee–Vempala improve the KLS exponent to $(\log n)^{2.2}$.
- **2023** — Klartag: $\psi_n\lesssim\sqrt{\log n}$, hence $L_n\lesssim\sqrt{\log n}$ (*Ars Inveniendi Analytica*).
- **Dec 2024** — Guan proves a sharp heat-flow (Bochner-type) estimate for log-concave measures; days later Klartag–Lehec insert it into the stochastic-localization scheme and obtain $L_n\le C$: **the slicing problem is solved**.

## 4. Partial Results / Verified Cases

Classes where $L_K\le C$ was known long before the general theorem:

- **Unconditional bodies** (symmetric in each coordinate): $L_K\le C$, with $L_K\lesssim 1$ following from a direct volumetric argument (Bourgain; Milman–Pajor 1989).
- **Zonoids** and duals of $\ell_p$-balls, $1\le p\le\infty$; all $\ell_p^n$ balls, for which $L_K$ is computable explicitly and $O(1)$.
- **Bounded outer volume ratio**: if $\mathrm{ovr}(K)=\inf(|\mathcal{E}|/|K|)^{1/n}\le A$ over ellipsoids $\mathcal{E}\supset K$, then $L_K\le CA$ (Ball).
- **Polytopes with few vertices/facets**: $K=\mathrm{conv}(x_1,\dots,x_N)$ with $N\le n^{O(1)}$ gives $L_K\le C\sqrt{\log(N/n)+1}$-type bounds; random polytopes with $N$ i.i.d. Gaussian or uniform vertices satisfy $L_K\le C$ with overwhelming probability (Klartag–Kozma 2009).
- **$\psi_2$-bodies** (all linear functionals subgaussian with constant $b$): $L_K\le Cb$ (Bourgain 2003).
- **Bodies with large symmetry groups**, e.g. invariance under a group acting irreducibly with a suitable orbit structure.
- **Low dimensions**: explicit computation. $n=1$: $L=1/\sqrt{12}\approx0.2887$. $n=2$: the maximum over all planar convex bodies is attained by the triangle, the minimum over symmetric bodies by the square; all values lie in $[0.24,0.32]$.
- **All dimensions, general bodies (2024)**: $L_n\le C$ with $C$ absolute and explicitly extractable (Klartag–Lehec).

## 5. Principal Obstacles

Why the problem resisted for ~38 years:

- **No linear-functional obstruction.** For an isotropic $K$, individual marginals $\langle X,\theta\rangle$ are near-Gaussian (Klartag's central limit theorem for convex bodies), but $L_K$ measures a *determinantal*, $n$-dimensional quantity; controlling one-dimensional data loses $n^{1/4}$-type factors, which is exactly Bourgain's 1991 loss.
- **Fourier methods fail.** The Busemann–Petty circle of ideas (Lutwak, Gardner–Koldobsky–Schlumprecht, Koldobsky's Fourier-analytic sections theory) needs positive-definiteness properties of $\|\cdot\|_K^{-p}$ that hold only for intersection bodies — a class that is *not* all convex bodies for $n\ge 5$.
- **Concentration is too weak.** Any argument routed through a concentration inequality inherits $\sqrt{\log n}$ or worse from union bounds over $S^{n-1}$; the target is a constant, so a *lossless* mechanism is required.
- **Localization is $1$-dimensional.** The Kannan–Lovász–Simonovits localization lemma reduces to one-dimensional log-concave problems but discards the joint geometry; it cannot see the determinant.
- **No extremal candidate is stable.** The conjectured extremizer (the simplex) is not a smooth critical point of a variational problem with an obvious second-order structure, so "reduce to the extremal case" strategies had no compactness handle in growing dimension.

The eventual solution used none of these: it needed a genuinely new differential inequality (Guan) for the Hessian of $\log P_tf$ along the heat semigroup, giving a bound on the growth of the covariance in Eldan's stochastic localization that is dimension-free rather than dimension-lossy.

## 6. The Gap

Before 2024 the gap was the exponent: proven $L_n\lesssim(\log n)^{1/2}$ versus the conjectured $L_n\lesssim 1$ — a factor going to infinity, arising because each iteration of stochastic localization lost a $\sqrt{\log n}$ from a Hessian-trace estimate.

The remaining gap after the resolution is **quantitative**:

1. **Sharp constant.** The Klartag–Lehec constant is far above the conjectured optimum $L_n=L_{\Delta^n}$ (simplex), whose limit is $\approx 0.30$. No matching lower-bound machinery exists.
2. **Extremal body.** It is still unproven that the regular simplex maximizes $L_K$ in each dimension, and that the cube minimizes among symmetric bodies.
3. **KLS conjecture.** $\psi_n\le C$ remains open; the best bound is $\psi_n\lesssim\sqrt{\log n}$ (Klartag 2023). Slicing was implied by KLS, not conversely, so KLS is strictly harder and survives.

## 7. Current Research (as of June 2026)

- **Constant-chasing.** Several groups are optimizing the Guan–Klartag–Lehec pipeline to extract a small explicit $C$; reported values in the low single digits circulate in preprints *(frontier — verify)*.
- **KLS via Guan's estimate.** The central question is whether the same heat-flow Hessian bound can be iterated to remove the last $\sqrt{\log n}$ in the Cheeger constant (Klartag and Lehec; Chen; Lee–Vempala; Jambulapati) *(frontier — verify)*.
- **Structural consequences.** Boundedness of $L_n$ upgrades many conditional theorems to unconditional ones: isomorphic Busemann–Petty, random-matrix covariance estimation for log-concave samples, and volume-distribution results in the Brazitikos–Giannopoulos–Valettas–Vritsiou program.
- **Institutions.** Weizmann Institute (Klartag), Université Côte d'Azur / IUF (Lehec), Duke (Chen), Georgia Tech (Vempala), Athens (Giannopoulos), Tel Aviv, Technion.
- **Algorithmic side.** Improved sampling and volume-computation guarantees for convex bodies follow from any KLS progress; this keeps theoretical CS engaged.

## 8. Future Work

- Prove $L_K\le L_{\Delta^n}$ with equality only for simplices — a sharp isoperimetric-type statement, likely needing a symmetrization or mass-transport argument that respects the determinant.
- Push Guan's Bochner-type inequality to a *sharp* form, aiming at $\psi_n=O(1)$ (full KLS).
- Combine with the Mahler conjecture circle: $L_K$ and the volume product $|K||K^\circ|$ are linked for symmetric bodies, and a dimension-free slicing bound constrains admissible Mahler-extremal behaviour.
- Extend to non-log-concave settings: $s$-concave and $\kappa$-concave measures, and to Riemannian manifolds with $\mathrm{CD}(0,N)$ curvature bounds.
- Develop a purely "isomorphic" proof avoiding stochastic calculus, which would be more portable to functional-analytic problems.

## 9. Key References

- **[Foundational]** J. Bourgain. *On high-dimensional maximal functions associated to convex bodies.* American Journal of Mathematics 108 (1986), 1467–1476.
- **[Foundational]** J. Bourgain. *On the distribution of polynomials on high-dimensional convex sets.* In: Geometric Aspects of Functional Analysis (GAFA Seminar 1989–90), Lecture Notes in Math. 1469, Springer, 1991, 127–137.
- **[Foundational]** K. Ball. *Logarithmically concave functions and sections of convex sets in $\mathbb{R}^n$.* Studia Mathematica 88 (1988), 69–84.
- **[Foundational]** K. Ball. *Cube slicing in $\mathbb{R}^n$.* Proceedings of the AMS 97 (1986), 465–473.
- **[Foundational]** D. Hensley. *Slicing convex bodies — bounds for slice area in terms of the body's covariance.* Proceedings of the AMS 79 (1980), 619–625.
- **[Foundational]** V. Milman, A. Pajor. *Isotropic position and inertia ellipsoids and zonoids of the unit ball of a normed $n$-dimensional space.* GAFA Seminar 1987–88, Lecture Notes in Math. 1376, Springer, 1989, 64–104.
- **[Foundational]** R. Kannan, L. Lovász, M. Simonovits. *Isoperimetric problems for convex bodies and a localization lemma.* Discrete & Computational Geometry 13 (1995), 541–559.
- **[SOTA]** B. Klartag. *On convex perturbations with a bounded isotropic constant.* Geometric and Functional Analysis 16 (2006), 1274–1290.
- **[SOTA]** B. Klartag, G. Kozma. *On the hyperplane conjecture for random convex sets.* Israel Journal of Mathematics 170 (2009), 253–268.
- **[SOTA]** R. Eldan, B. Klartag. *Approximately gaussian marginals and the hyperplane conjecture.* Contemporary Mathematics 545, AMS, 2011, 55–68.
- **[SOTA]** R. Eldan. *Thin shell implies spectral gap up to polylog via a stochastic localization scheme.* Geometric and Functional Analysis 23 (2013), 532–569.
- **[SOTA]** Y. Chen. *An almost constant lower bound of the isoperimetric coefficient in the KLS conjecture.* Geometric and Functional Analysis 31 (2021), 34–61.
- **[SOTA]** B. Klartag, J. Lehec. *Bourgain's slicing problem and KLS isoperimetry up to polylog.* Geometric and Functional Analysis 32 (2022), 1134–1159.
- **[SOTA]** A. Jambulapati, Y. T. Lee, S. S. Vempala. *A slightly improved bound for the KLS constant.* arXiv:2208.11644, 2022.
- **[SOTA]** B. Klartag. *Logarithmic bounds for isoperimetry and slices of convex sets.* Ars Inveniendi Analytica (2023), Paper No. 4.
- **[SOTA / Resolution]** Q. Guan. *A note on Bourgain's slicing problem.* arXiv:2412.09075, 2024.
- **[SOTA / Resolution]** B. Klartag, J. Lehec. *Affirmative Resolution of Bourgain's Slicing Problem using Guan's Bound.* arXiv:2412.15044, 2024.
- **[Survey]** S. Brazitikos, A. Giannopoulos, P. Valettas, B.-H. Vritsiou. *Geometry of Isotropic Convex Bodies.* Mathematical Surveys and Monographs 196, American Mathematical Society, 2014.

## 10. Worked Example / Concrete Special Case

**Cube.** Take $Q=[-\tfrac12,\tfrac12]^n$, so $|Q|=1$ and $Q$ is already isotropic. For any $\theta\in S^{n-1}$,

$$\int_Q\langle x,\theta\rangle^2dx=\sum_i\theta_i^2\int_{-1/2}^{1/2}t^2\,dt=\frac{1}{12}\quad\Longrightarrow\quad L_Q=\frac{1}{\sqrt{12}}\approx 0.2887 .$$

Sections: Hadwiger and Vaaler proved $|Q\cap\theta^\perp|\ge 1$ for every $\theta$, and Ball (1986) proved $|Q\cap\theta^\perp|\le\sqrt2$, attained at $\theta=\tfrac{1}{\sqrt2}(1,1,0,\dots,0)$. So the cube satisfies the slicing bound with $c=1$, uniformly in $n$ — no degeneration.

**Euclidean ball.** Let $B=r_nB_2^n$ with $r_n=|B_2^n|^{-1/n}$, so $|B|=1$. For the unit ball $\int_{B_2^n}x_1^2dx=|B_2^n|/(n+2)$, hence after scaling

$$L_B=\frac{r_n}{\sqrt{n+2}}=\frac{|B_2^n|^{-1/n}}{\sqrt{n+2}} .$$

Using $|B_2^n|^{1/n}=\sqrt{2\pi e/n}\,(1+o(1))$ gives $r_n\approx\sqrt{n/(2\pi e)}$ and

$$L_B\ \longrightarrow\ \frac{1}{\sqrt{2\pi e}}\approx 0.2420 .$$

Its central sections: $|B\cap\theta^\perp|=|B_2^{n-1}|\,r_n^{\,n-1}$. Numerically $1.420$ at $n=10$, $1.611$ at $n=100$, converging to $\sqrt e\approx1.6487$. Again bounded below, uniformly in $n$.

**What the problem asked.** Both examples give sections of order $1$, consistent with $|K\cap\theta^\perp|\asymp 1/L_K$ (with $1/L_Q=3.46$, $1/L_B=4.13$ against measured section volumes $1$–$1.65$). The slicing problem asked whether some *exotic* sequence of bodies could push $L_{K_n}\to\infty$, forcing every hyperplane section of a volume-$1$ body to shrink to zero. The 2024 theorem says no: $L_n\le C$, so every convex body of volume $1$ in every dimension has a central section of area at least $c_1/C>0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*