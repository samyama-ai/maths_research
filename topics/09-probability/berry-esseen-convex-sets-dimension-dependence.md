---
id: 09-probability/berry-esseen-convex-sets-dimension-dependence
title: "Rate of Convergence in the Multivariate Central Limit Theorem for Convex Sets (Bentkus Problem)"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rate of Convergence in the Multivariate Central Limit Theorem for Convex Sets (Bentkus Problem)

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/berry-esseen-convex-sets-dimension-dependence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $X, X_1, X_2, \dots$ be i.i.d. random vectors in $\mathbb{R}^d$ with $\mathbb{E}X = 0$ and covariance $\mathbb{E}XX^\top = I_d$. Set
$$S_n = \frac{1}{\sqrt n}\sum_{i=1}^n X_i, \qquad Z \sim N(0, I_d), \qquad \beta = \mathbb{E}\lVert X\rVert_2^3 ,$$
and let $\mathcal{C}_d$ denote the class of all measurable convex subsets of $\mathbb{R}^d$. Define the convex-set discrepancy
$$\Delta_n(d) \;=\; \sup_{A \in \mathcal{C}_d}\bigl| \mathbb{P}(S_n \in A) - \mathbb{P}(Z \in A)\bigr| .$$

Bentkus proved $\Delta_n(d) \le C\, d^{1/4}\beta\, n^{-1/2}$ with $C$ absolute. Two questions are open.

- **(Q1) Removability of $d^{1/4}$.** Is there an absolute constant $C$ with $\Delta_n(d) \le C \beta n^{-1/2}$ for all $d, n$ and all such $X$? Equivalently, is the factor $d^{1/4}$ an artifact of the proof method rather than of the problem?
- **(Q2) Sample-size threshold.** For isotropic $X$ with $\lVert X\rVert_2 \le K\sqrt d$ a.s. (or with bounded fourth moments), what is the least exponent $\alpha$ such that $n \gg d^{\alpha}$ forces $\Delta_n(d) \to 0$? The conjectured answer is $\alpha = 1$ (up to logarithms); the third-moment bound above gives only $\alpha = 7/2$, since $\beta \ge d^{3/2}$ always.

A resolution requires either a proof of the $d$-free (or $\sqrt{d/n}$-type) bound valid for all convex $A$ and all isotropic laws, or an explicit sequence of laws and convex sets realizing the larger rate.

## 2. Mathematical Foundations

**Normalization.** By $\mathbb{E}\lVert X\rVert_2^2 = d$ and Jensen, $\beta = \mathbb{E}\lVert X\rVert^3 \ge d^{3/2}$, with equality iff $\lVert X\rVert \equiv \sqrt d$. Hence $d^{1/4}\beta n^{-1/2} \ge d^{7/4}n^{-1/2}$: the Bentkus bound is vacuous unless $n \gtrsim d^{7/2}$.

**Bentkus' theorem.** For independent (not necessarily identically distributed) mean-zero $X_i$ with $\sum_i \mathrm{Cov}(X_i) = I_d$,
$$\sup_{A\in\mathcal{C}_d}\bigl|\mathbb{P}(\textstyle\sum_i X_i \in A) - \mathbb{P}(Z\in A)\bigr| \;\le\; 400\, d^{1/4}\sum_{i=1}^n \mathbb{E}\lVert X_i\rVert^3 .$$

**Gaussian surface area.** For a Borel set $A$, $\gamma(A) = \liminf_{\varepsilon\downarrow 0}\varepsilon^{-1}\bigl(\mathbb{P}(Z\in A^{\varepsilon}) - \mathbb{P}(Z\in A)\bigr)$, where $A^\varepsilon$ is the $\varepsilon$-neighbourhood. The key geometric input is
$$\sup_{A\in\mathcal{C}_d} \gamma(A) \;\asymp\; d^{1/4},$$
with the upper bound $\gamma(A) \le 4 d^{1/4}$ due to Ball (1993) and a matching lower bound $\gamma(A) \ge c\, d^{1/4}$ due to Nazarov (2003), attained by a polytope with $\exp(c\sqrt d)$ facets circumscribing a ball of radius $\approx \sqrt d$.

**Smoothing inequality.** Standard Lindeberg/Stein arguments replace the indicator $\mathbf 1_A$ by a smooth surrogate $h_\varepsilon$ with $\mathbf 1_A \le h_\varepsilon \le \mathbf 1_{A^\varepsilon}$ and derivative bounds $\lVert \partial^k h_\varepsilon\rVert_\infty \lesssim \varepsilon^{-k}$. This costs
$$\mathbb{P}(Z\in A^{\varepsilon}) - \mathbb{P}(Z\in A) \;\le\; \varepsilon\,\gamma(A) \;\lesssim\; \varepsilon\, d^{1/4},$$
which is exactly where the $d^{1/4}$ enters; optimizing $\varepsilon$ against the Lindeberg swap error $\lesssim \beta/(\varepsilon^2 \sqrt n)\cdot\varepsilon$ produces the stated rate.

**Comparison classes.** For hyperrectangles $\mathcal{R}_d = \{\prod_j (a_j,b_j]\}$ the answer is qualitatively different: Chernozhukov–Chetverikov–Kato obtain $\sup_{A\in\mathcal R_d}|\cdot| \to 0$ under $n \gg \mathrm{polylog}(d)$. Since $\mathcal R_d \subset \mathcal C_d$ and $\sup_{A\in\mathcal R_d}\gamma(A)\asymp \sqrt{\log d}$, the polynomial-in-$d$ behaviour for $\mathcal C_d$ is driven by the "round" sets (balls, smooth bodies, many-faceted polytopes).

## 3. History & State of the Art (SOTA)

- **1970s.** Bhattacharya–Rao (*Normal Approximation and Asymptotic Expansions*, 1976) established $\Delta_n(d)\le C(d)\beta n^{-1/2}$ over convex sets, with $C(d)$ obtained from Edgeworth/Fourier methods and growing rapidly in $d$. Nagaev (1976) gave one of the first explicit dimension-dependent remainder estimates.
- **1991.** Götze applied Stein's method for the multivariate CLT over convex sets, yielding a bound with linear-type dimension dependence; the argument was later re-exposited and corrected by Bhattacharya and Holmes (2010).
- **2003–2005.** Bentkus reduced the dimensional factor to $d^{1/4}$, first in *On the dependence of the Berry–Esseen bound on dimension*, then with the explicit constant $400\,d^{1/4}$ in *A Lyapunov-type bound in $\mathbb{R}^d$*. He identified $d^{1/4}$ with Ball's Gaussian-perimeter bound and raised the question of whether it is necessary.
- **2019.** Raič sharpened the constant to
 $$\Delta_n(d) \;\le\; \bigl(42\, d^{1/4} + 16\bigr)\,\beta\, n^{-1/2},$$
 the best known fully explicit third-moment bound.
- **2017–2021.** The high-dimensional bootstrap literature (Chernozhukov–Chetverikov–Kato; Kuchibhotla–Chakrabortty) settled hyperrectangles and *sparsely* convex sets with polylogarithmic dimension dependence, sharpening the contrast with the general convex class.
- **2018–2024.** Transport-based results (Zhai; Eldan–Mikulincer–Zhai) gave near-optimal $\sqrt d$-type rates in Wasserstein-2 distance, and fourth-moment/Stein-kernel arguments (Fang–Koike) lowered the polynomial power of $d$ required for convex sets *(frontier — verify the exact exponent)*.

## 4. Partial Results / Verified Cases

- **Half-spaces ($A=\{ \langle u,x\rangle \le t\}$).** Reduces to the one-dimensional Berry–Esseen theorem: error $\le 0.4690\,\mathbb{E}|\langle u,X\rangle|^3 n^{-1/2}$ (Shevtsova's constant), dimension-free.
- **Hyperrectangles.** $\sup_{A\in\mathcal R_d}|\cdot| \lesssim \bigl(\log^7(dn)/n\bigr)^{1/6}$ under sub-exponential tails (CCK 2017), later improved to $\bigl(\log^5 (dn)/n\bigr)^{1/4}$-type rates; requires only $\log d = o(n^{1/7})$.
- **Sparsely convex sets** (intersections of half-spaces each depending on at most $s$ coordinates): polylogarithmic in $d$, polynomial in $s$ (CCK 2017).
- **Euclidean balls, $d\ge 5$.** With finite fourth moments the rate improves to $O(n^{-1})$ with explicit dimension dependence (Esseen-type cancellation of the odd Edgeworth term); Bentkus–Götze (1996) proved the optimal $O(n^{-1})$ rate for quadratic forms in $d\ge 5$, and Götze–Ulyanov and Götze–Naumov–Spokoiny–Ulyanov give explicit constants for balls and for Gaussian comparison of quadratic forms.
- **Fixed $d$.** For $d$ fixed and $n\to\infty$ the $n^{-1/2}$ rate is sharp and classical; no gap remains.
- **Fourth-moment regime.** Fang–Koike (2024) prove convex-set bounds under a fourth-moment condition that strictly reduce the required $n$-versus-$d$ exponent below $7/2$, and give balls a still smaller exponent *(frontier — verify)*.
- **Smoothing loss is sharp.** Nazarov's $c\,d^{1/4}$ lower bound on convex Gaussian surface area shows no smoothing-based proof can do better than $d^{1/4}$; this is a verified obstruction, not a verified case of the conjecture.

## 5. Principal Obstacles

- **The smoothing barrier is provably tight.** Every known proof (Lindeberg swapping, Stein's method with the multivariate Stein equation $\nabla^2 f - x\cdot\nabla f = h - \mathbb{E}h(Z)$, Fourier smoothing) passes through an $\varepsilon$-neighbourhood of $\partial A$. Ball–Nazarov make the $\varepsilon d^{1/4}$ loss unavoidable *within that scheme*, so removing $d^{1/4}$ demands a genuinely non-smoothing argument.
- **No anticoncentration for $S_n$ itself.** One could avoid the loss by bounding $\mathbb{P}(S_n \in \partial A^\varepsilon)$ directly instead of $\mathbb{P}(Z \in \partial A^\varepsilon)$, but this is circular: such an anticoncentration bound for the non-Gaussian sum is essentially as strong as the CLT being proved. Lattice-supported $X$ (e.g. uniform on $\{\pm1\}^d$) has $S_n$ on a grid of spacing $2/\sqrt n$, so no anticoncentration holds below that scale.
- **Fourier methods break down.** The characteristic function of a convex indicator has no useful decay; Esseen-type smoothing inequalities in $\mathbb{R}^d$ carry constants that blow up with $d$, and the Edgeworth expansion for $\mathcal{C}_d$ requires Cramér-type conditions plus $d$-dependent constants from Bhattacharya–Rao that are worse than $d^{1/4}$.
- **$\beta$ is the wrong functional.** The third absolute moment $\mathbb{E}\lVert X\rVert^3 \ge d^{3/2}$ is insensitive to how the mass is distributed over directions. Any bound stated in $\beta$ alone inherits the $d^{3/2}$ floor, so (Q2) cannot be answered without a different complexity measure (Stein kernels, fourth cumulants, log-concavity).
- **Wasserstein does not transfer.** $W_2(S_n, Z) \lesssim \sqrt{d}\,\log n/\sqrt n$-type bounds do not imply convex-set bounds, because converting $W_2$ to a uniform set-discrepancy again costs the surface-area factor.

## 6. The Gap

Known and sharp: the *geometric* constant $\sup_{A\in\mathcal{C}_d}\gamma(A)\asymp d^{1/4}$. Known upper bound: $\Delta_n(d)\le (42 d^{1/4}+16)\beta n^{-1/2}$. Known lower bounds: only $c\,\beta n^{-1/2} d^{-3/2}$-type, i.e. $c n^{-1/2}$ from one-dimensional projections, plus $\Omega(1/n)$ contributions from balls. **No example is known in which $\Delta_n(d)$ exceeds $C\beta n^{-1/2}$**, and no example is known forcing $n \gg d^{1+\epsilon}$.

The gap is therefore a factor $d^{1/4}$ in (Q1) and a full range of exponents $\alpha \in [1, 7/2]$ in (Q2). Crossing it requires one of:
1. a proof that the swap error and the boundary error can be *correlated* — i.e. that the $\varepsilon$-shell mass that smoothing pays for is not actually charged by $S_n - Z$ discrepancy; or
2. a construction of an isotropic law and a convex body (plausibly Nazarov's many-faceted polytope, or a lattice law aligned with it) whose discrepancy is $\gtrsim d^{1/4}\beta n^{-1/2}$.

## 7. Current Research (as of June 2026)

- **Stein kernels and fourth-moment bounds.** Fang (CUHK) and Koike (Tokyo/Kyoto) drive the program of replacing $\beta$ by fourth-moment and Stein-kernel functionals to lower the $d$-exponent for convex sets and balls *(frontier — verify exponents)*.
- **Log-concave and structured laws.** Under isotropic log-concavity, sharper convex-set rates of the form $\mathrm{poly}(\log)\cdot\sqrt{d/n}$ have been announced, exploiting thin-shell and KLS-type concentration to control the boundary shell *(frontier — verify)*. Progress here is coupled to the KLS conjecture programme (Chen; Klartag–Lehec).
- **Strong approximation / coupling.** Buzun, Naumov and Spokoiny (WIAS Berlin, HSE) pursue Gaussian comparison and strong-approximation bounds for balls and quadratic forms with explicit $d,n$ trade-offs.
- **Transport and martingale embedding.** Eldan, Mikulincer and collaborators (Weizmann, MIT) study whether entropic/martingale couplings can be post-processed into set-discrepancy bounds without paying Gaussian surface area.
- **Bootstrap-driven statistics.** Kuchibhotla, Chakrabortty and coauthors (CMU, Penn) push the hyperrectangle and sparse-convex machinery toward wider classes with controlled Gaussian surface area, e.g. $\mathcal{A}$ with $\gamma(A)\le a$, where the natural conjecture is $\Delta \lesssim a\cdot(\text{polylog}/\sqrt n)$.

## 8. Future Work

- Prove or refute the **surface-area-parametrized conjecture**: $\sup_{\gamma(A)\le a}|\mathbb{P}(S_n\in A)-\mathbb{P}(Z\in A)| \le C a\,\mathrm{polylog}(d)\,n^{-1/2}\cdot\max_i \lVert X_i\rVert_\infty^3$-type bounds. This interpolates the settled hyperrectangle case ($a\asymp\sqrt{\log d}$) and the open convex case ($a\asymp d^{1/4}$).
- **Construct a lower bound** by pairing Nazarov's extremal polytope with a lattice law on $\{\pm 1\}^d$, exploiting the incompatibility of a $2/\sqrt n$ grid with $\exp(c\sqrt d)$ facets.
- **Multiscale smoothing.** Replace a single $\varepsilon$ by a scale decomposition adapted to the local curvature of $\partial A$, paying $\gamma$ only where the swap error is actually large.
- **Non-uniform bounds.** Establish Bentkus-type inequalities that decay in the Gaussian measure of $A$, in the spirit of non-uniform Berry–Esseen theorems, which would sharpen the tail regime that dominates worst-case examples.
- **Settle balls completely**: determine the exact optimal $d$-dependence of the $O(n^{-1})$ rate for centred and non-centred Euclidean balls in all $d$, which is the most tractable proxy for the general problem.

## 9. Key References

- **[Foundational]** R. N. Bhattacharya and R. Ranga Rao. *Normal Approximation and Asymptotic Expansions.* Wiley, 1976; revised edition SIAM Classics in Applied Mathematics 64, 2010.
- **[Foundational]** F. Götze. *On the rate of convergence in the multivariate CLT.* Annals of Probability 19(2), 724–739, 1991.
- **[Foundational]** V. Bentkus. *On the dependence of the Berry–Esseen bound on dimension.* Journal of Statistical Planning and Inference 113(2), 385–402, 2003.
- **[SOTA]** V. Bentkus. *A Lyapunov-type bound in $\mathbb{R}^d$.* Theory of Probability and Its Applications 49(2), 311–323, 2005.
- **[SOTA / Recent]** M. Raič. *A multivariate Berry–Esseen theorem with explicit constants.* Bernoulli 25(4A), 2824–2853, 2019.
- **[Geometry]** K. Ball. *The reverse isoperimetric problem for Gaussian measure.* Discrete & Computational Geometry 10, 411–420, 1993.
- **[Geometry]** F. Nazarov. *On the maximal perimeter of a convex set in $\mathbb{R}^n$ with respect to a Gaussian measure.* In: Geometric Aspects of Functional Analysis, Lecture Notes in Mathematics 1807, Springer, 169–187, 2003.
- **[Balls / quadratic forms]** V. Bentkus and F. Götze. *Optimal rates of convergence in the CLT for quadratic forms.* Annals of Probability 24(1), 466–490, 1996.
- **[Gaussian comparison]** F. Götze, A. Naumov, V. Spokoiny and V. Ulyanov. *Large ball probabilities, Gaussian comparison and anti-concentration.* Bernoulli 25(4A), 2538–2563, 2019.
- **[High-dimensional]** V. Chernozhukov, D. Chetverikov and K. Kato. *Central limit theorems and bootstrap in high dimensions.* Annals of Probability 45(4), 2309–2352, 2017.
- **[Transport]** A. Zhai. *A high-dimensional CLT in $W_2$ distance with near optimal convergence rate.* Probability Theory and Related Fields 170, 821–845, 2018.
- **[Recent]** X. Fang and Y. Koike. *Large-dimensional central limit theorem with fourth-moment error bounds on convex sets and balls.* Annals of Applied Probability, 2024. *(frontier — verify volume/pages)*
- **[Survey]** V. V. Senatov. *Normal Approximation: New Results, New Methods, New Problems.* VSP, Utrecht, 1998.
- **[Survey]** R. N. Bhattacharya and S. Holmes. *An exposition of Götze's estimate of the rate of convergence in the multivariate central limit theorem.* Technical report, Stanford University, 2010.

## 10. Worked Example / Concrete Special Case

**Setup.** Let $X$ be uniform on $\{-1,+1\}^d$, so $\mathbb{E}X=0$, $\mathbb{E}XX^\top = I_d$, and $\lVert X\rVert_2 = \sqrt d$ exactly. Then $\beta = \mathbb{E}\lVert X\rVert^3 = d^{3/2}$, the minimum possible.

**What the theorem gives.** Raič's bound reads
$$\Delta_n(d) \le \frac{(42 d^{1/4}+16)\, d^{3/2}}{\sqrt n}.$$
For $d = 100$ this is $\approx (42\cdot 3.162 + 16)\cdot 1000/\sqrt n \approx 1.49\times 10^{5}/\sqrt n$, which is $<1$ only for $n > 2.2\times 10^{10}$. Generally the bound is vacuous unless $n \gtrsim 1764\, d^{7/2}$.

**What is actually true for one natural set.** Take $A_r = \{x : \lVert x\rVert_2 \le r\}$, the centred ball, and compute the discrepancy exactly to leading order. Write $S_n = (S^{(1)},\dots,S^{(d)})$ with $S^{(j)}$ i.i.d. scaled binomial. For symmetric Bernoulli coordinates,
$$\mathbb{E}\bigl(S^{(j)}\bigr)^2 = 1, \qquad \mathbb{E}\bigl(S^{(j)}\bigr)^4 = 3 - \frac{2}{n},$$
so $\mathrm{Var}\bigl((S^{(j)})^2\bigr) = 2 - 2/n$, versus $2$ for a $\chi^2_1$ coordinate of $Z$. Summing the $d$ independent terms,
$$\mathbb{E}\lVert S_n\rVert^2 = d = \mathbb{E}\lVert Z\rVert^2, \qquad \mathrm{Var}\lVert S_n\rVert^2 = 2d\Bigl(1-\frac1n\Bigr), \qquad \mathrm{Var}\lVert Z\rVert^2 = 2d .$$
Both $\lVert S_n\rVert^2$ and $\lVert Z\rVert^2$ are sums of $d$ i.i.d. terms with matching means and third cumulants up to $O(1/n)$; their standardized laws therefore differ, to leading order, only by a scale factor $\sigma_{S}/\sigma_{Z} = (1-1/n)^{1/2} \approx 1 - \tfrac{1}{2n}$. Comparing $N(d,\sigma^2)$ with $N(d,\sigma^2(1-1/n))$ in Kolmogorov distance,
$$\sup_{r>0}\bigl|\mathbb{P}(\lVert S_n\rVert\le r)-\mathbb{P}(\lVert Z\rVert \le r)\bigr| \;\approx\; \frac{1}{2n}\sup_{u}\,u\,\varphi(u) \;=\; \frac{1}{2n}\cdot\frac{e^{-1/2}}{\sqrt{2\pi}} \;\approx\; \frac{0.121}{n},$$
independent of $d$. For $d=100$, $n=10^3$ the true error over centred balls is about $1.2\times10^{-4}$, while the guaranteed bound at that $n$ is $\approx 4.7\times 10^{3}$ — off by seven orders of magnitude and, more importantly, by every power of $d$.

**The point of the example.** The hard part of $\Delta_n(d)$ is not any single smooth body: centred balls give $O(1/n)$, half-spaces give $O(n^{-1/2})$ with no $d$. The conjectured extremal sets are Nazarov-type polytopes with $\exp(c\sqrt d)$ facets, each facet contributing a boundary slab that the lattice support of $S_n$ (spacing $2/\sqrt n$) can, in principle, systematically over- or under-fill. Whether such a coordinated construction can beat $C\beta n^{-1/2}$ is exactly the open Bentkus problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*