---
id: 05-analysis/kls-conjecture
title: "KLS Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# KLS Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kls-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mu$ be a log-concave probability measure on $\mathbb{R}^n$ that is **isotropic**: barycenter at the origin and covariance the identity. Its **Cheeger (isoperimetric) constant** is

$$
h_\mu \;=\; \inf_{S \subset \mathbb{R}^n} \frac{\mu^+(\partial S)}{\min\{\mu(S),\,1-\mu(S)\}},
\qquad
\mu^+(\partial S) = \liminf_{\varepsilon \to 0^+}\frac{\mu(S_\varepsilon)-\mu(S)}{\varepsilon},
$$

where $S_\varepsilon$ is the Euclidean $\varepsilon$-neighbourhood and the infimum runs over Borel sets.

**Conjecture (Kannan–Lovász–Simonovits, 1995).** There is a universal constant $c>0$, independent of $n$ and of $\mu$, with $h_\mu \ge c$ for every isotropic log-concave $\mu$ on $\mathbb{R}^n$.

Equivalently, writing $\psi_n = \sup_\mu h_\mu^{-1}$ over isotropic log-concave measures in dimension $n$, the claim is $\psi_n = O(1)$. The name "hyperplane conjecture" for KLS reflects the expected extremal behaviour: among all cuts, an affine half-space should be within a constant factor of optimal.

A proof requires a dimension-free lower bound for **all** log-concave $\mu$; a disproof requires a sequence $\mu_n$ with $h_{\mu_n} \to 0$. Current knowledge: $\psi_n \lesssim \sqrt{\log n}$, so any counterexample must degrade at most logarithmically.

## 2. Mathematical Foundations

**Log-concavity.** $\mu$ is log-concave if $\mu(\lambda A + (1-\lambda)B) \ge \mu(A)^\lambda \mu(B)^{1-\lambda}$ for compact $A,B$ and $\lambda\in[0,1]$. By Borell's theorem, a full-dimensional log-concave measure has density $e^{-V}$ with $V:\mathbb{R}^n\to(-\infty,\infty]$ convex. Uniform measures on convex bodies and Gaussians are the model cases.

**Poincaré form.** For log-concave $\mu$ the Cheeger constant is equivalent, up to universal factors, to the spectral gap: with
$$
\mathrm{Var}_\mu(f) \;\le\; C_P(\mu)\int_{\mathbb{R}^n} |\nabla f|^2 \, d\mu \quad \text{for all locally Lipschitz } f,
$$
one has $\tfrac14 h_\mu^2 \le C_P(\mu)^{-1} \le h_\mu^2$ — the upper bound is Cheeger's inequality, the reverse is Buser–Ledoux in the log-concave setting, sharpened by E. Milman's equivalence of Cheeger, Poincaré, and exponential concentration for convex measures. So KLS $\iff$ $C_P(\mu) = O(1)$ for isotropic log-concave $\mu$.

**The hierarchy.** Let $X\sim\mu$ isotropic log-concave.

- **Thin-shell constant:** $\sigma_n^2 = \sup_\mu \mathrm{Var}\big(|X|\big)$. Conjecturally $\sigma_n = O(1)$ (concentration of $|X|$ on a shell of width $O(1)$ around $\sqrt{n}$).
- **Slicing (Bourgain) constant:** $L_n = \sup_K L_K$ where $L_K = f_K(0)^{1/n}$ for the isotropic log-concave density $f_K$; equivalently every isotropic convex body has a hyperplane section of $(n-1)$-volume $\ge c$.

The implications are
$$
\psi_n \gtrsim \sigma_n \gtrsim L_n,
$$
i.e. KLS $\Rightarrow$ thin shell $\Rightarrow$ slicing. The second implication is Eldan–Klartag (2011); the first is elementary (apply Poincaré to $f(x)=|x|$). Conversely Eldan (2013) proved a near-reverse:
$$
\psi_n^2 \;\lesssim\; \log n \cdot \sup_{k \le n} \sigma_k^2 ,
$$
so thin shell and KLS are equivalent up to a logarithm.

**Localization.** The original KLS engine is the *localization lemma*: an integral inequality $\int f\,d\lambda>0,\ \int g\,d\lambda>0 \Rightarrow \exists$ a segment and a log-affine weight on it satisfying the same inequalities. This reduces $n$-dimensional isoperimetry to one-dimensional log-concave computations. The modern engine is **stochastic localization**: the measure-valued SDE
$$
d\mu_t(x) \;=\; \mu_t(x)\,\langle x - a_t,\ dW_t\rangle,\qquad a_t = \int x\, d\mu_t(x),
$$
which tilts $\mu$ by a Gaussian factor $e^{\langle c_t,x\rangle - t|x|^2/2}$, driving $\mu_t$ towards a Gaussian while controlling the growth of $\mathrm{Cov}(\mu_t)$.

## 3. History & State of the Art (SOTA)

Kannan, Lovász and Simonovits introduced the conjecture in *Isoperimetric problems for convex bodies and a localization lemma* (Discrete & Computational Geometry, 1995), motivated by mixing-time analysis of the ball walk for randomized volume computation. Their own bound was $\psi_n \lesssim \sqrt{n}$ (in isotropic position, $h_\mu \gtrsim 1/\mathbb{E}|X|$-type estimates).

Milestones:

| Year | Result | Bound on $\psi_n$ |
|---|---|---|
| 1995 | Kannan–Lovász–Simonovits, localization | $O(\sqrt n)$ |
| 2007 | Bobkov, isoperimetry via $\mathrm{Var}|X|$ | polynomial improvement over $\sqrt n$ |
| 2010–11 | Fleury; Guédon–Milman thin-shell $\sigma_n\lesssim n^{1/3}$ | improved via Bobkov's reduction |
| 2013 | Eldan, stochastic localization; thin shell $\Rightarrow$ KLS up to polylog | $\tilde O(n^{1/3})$ |
| 2017 | Lee–Vempala | $O(n^{1/4})$ |
| 2021 | Y. Chen | $n^{o(1)}$ |
| 2022 | Klartag–Lehec | polylogarithmic in $n$ |
| 2022 | Jambulapati–Lee–Vempala | reduced polylog exponent |
| 2023 | Klartag | $O(\sqrt{\log n})$ |

In parallel, the weakest member of the hierarchy fell: Klartag and Lehec, building on a heat-flow/Kähler-type estimate of Q. Guan (2024), proved $L_n = O(1)$, resolving Bourgain's slicing problem (2024–25). Thin shell and KLS remain open.

Computationally, KLS-type bounds are not merely aesthetic: the ball walk in a convex body mixes in $O^*(n^2 \psi_n^2)$ steps, and Cousins–Vempala's $O^*(n^3)$ volume algorithm consumes these bounds directly.

## 4. Partial Results / Verified Cases

The conjecture is a **theorem** in the following settings, with dimension-free constants:

- **$n = 1$:** every log-concave probability measure on $\mathbb{R}$ in isotropic position has $h_\mu \ge c$ (Payne–Weinberger / Bobkov); the sharp one-dimensional analysis underpins all localization arguments.
- **Gaussian measure:** $h_\gamma = \sqrt{2/\pi}$, with half-spaces extremal (Sudakov–Tsirelson, Borell 1974–75).
- **Euclidean ball and sphere:** Lévy–Gromov isoperimetric inequality; caps are extremal.
- **The cube $[-\sqrt3,\sqrt3]^n$:** $h = 1/\sqrt3$ for all $n$, coordinate half-space cuts extremal (Hadwiger).
- **$\ell_p^n$ balls, $1\le p\le\infty$:** $h \ge c$ uniformly (Sodin 2008; Latała–Wojtaszczyk 2008), via explicit product representations of the cone measure.
- **Unconditional bodies** (symmetric under all coordinate sign flips): thin-shell bounds of Klartag (2009) and Barthe–Cordero-Erausquin (2013) give $\sigma = O(1)$ up to logarithms, hence KLS up to a $\mathrm{polylog}$ factor.
- **Bodies with many symmetries / revolution bodies:** dimension-free constants whenever the symmetry group acts with few orbits (Klartag–Milman-type symmetrization arguments; Bobkov's revolution-body results).
- **Product measures and their Lipschitz images:** tensorization of the Poincaré inequality gives $C_P$ independent of $n$.

For **general** log-concave measures the best unconditional statement is $\psi_n \le C\sqrt{\log n}$ (Klartag 2023), i.e. $\mathrm{Var}_\mu(f) \le C \log n \int|\nabla f|^2 d\mu$.

## 5. Principal Obstacles

- **No extremal candidate is stable.** Half-spaces are conjecturally near-optimal, but no variational or symmetrization scheme is known that pushes an arbitrary log-concave measure towards a half-space cut while controlling isoperimetry. Steiner symmetrization does not respect log-concave isoperimetric ratios.
- **Localization loses a dimension factor.** The 1995 lemma reduces to one dimension but the reduction is lossy: the needle decomposition sees only one direction of the covariance, and re-assembling $n$ needles reintroduces $\sqrt n$.
- **Fourier/harmonic methods do not apply.** There is no group structure or spectral decomposition available for a general convex body; the relevant operator $L = \Delta - \nabla V\cdot\nabla$ has no explicit eigenbasis, and Bakry–Émery curvature-dimension bounds are vacuous because $\nabla^2 V \succeq 0$ only gives $CD(0,\infty)$ — no positive lower bound on the spectral gap.
- **Stochastic localization saturates.** The Eldan scheme controls $\mathrm{Cov}(\mu_t)$ via a matrix-valued SDE whose quadratic variation is bounded by the operator norm $\|\mathrm{Cov}\|_{op}$; the best a priori control of the third-moment/tilt term costs a $\sqrt{\log n}$ before the process reaches Gaussian time $t \sim 1$. Removing this factor requires a genuinely new estimate on the growth of $\|\mathrm{Cov}(\mu_t)\|_{op}$, not a sharper application of Itô's formula.
- **Thin shell is itself unresolved.** Since $\psi_n \gtrsim \sigma_n$, no route can prove KLS without simultaneously proving the thin-shell conjecture — a central limit statement for convex bodies that resists all known CLT machinery because the coordinates are only weakly dependent in a way not captured by mixing conditions.

## 6. The Gap

Proven: $c \le \psi_n \le C\sqrt{\log n}$. Conjectured: $\psi_n \le C$. The entire remaining gap is the single factor $\sqrt{\log n}$.

Two equivalent formulations of the crossing point:

1. **Thin shell at $O(1)$.** Prove $\mathrm{Var}(|X|) \le C$ for isotropic log-concave $X$. By Eldan's reduction this yields $\psi_n \lesssim \sqrt{\log n}$ — the same as current — so one additionally needs a *lossless* version of the thin-shell $\Rightarrow$ KLS implication, removing the $\log n$ in $\psi_n^2 \lesssim \log n\,\sup_k\sigma_k^2$.
2. **Covariance control in stochastic localization.** Show that along the Eldan process $\|\mathrm{Cov}(\mu_t)\|_{op} \le 2$ for $t \le c$ with probability close to 1, where currently one can only prevent blow-up until $t \sim 1/\log n$.

Neither reduction is known to be reversible without loss; closing the gap means producing a bound that is simultaneously sharp in the shell width and in the localization time.

## 7. Current Research (as of June 2026)

- **Klartag (Weizmann) and Lehec (Poitiers/Paris-Dauphine)** continue the heat-flow line that resolved slicing. The key input, Guan's bound on a complex/real Monge–Ampère-type quantity, is being tested for whether it also controls the thin-shell width. *(frontier — verify)*
- **Y. Chen, Y. T. Lee, S. Vempala, A. Jambulapati (Washington / Georgia Tech / Stanford)** pursue algorithmically-motivated refinements, where any improvement to $\psi_n$ transfers immediately to sampling and volume-computation complexity.
- **Bizeul** and collaborators have developed small-ball and negative-moment estimates for log-concave measures that give an independent route to slicing-type bounds; extending these to isoperimetry is active. *(frontier — verify)*
- **Eldan school (Weizmann):** refinements of stochastic localization with non-Gaussian tilts, and connections to spin-glass free-energy methods and to sampling from non-log-concave measures.
- Applications continue to drive interest: mixing of Hamiltonian Monte Carlo and Riemannian samplers, differential privacy, and matrix-concentration analogues all consume KLS-type bounds.

## 8. Future Work

- Prove the thin-shell conjecture $\sigma_n = O(1)$ outright, then find a lossless transfer to $\psi_n$; Eldan and Klartag have both singled out the $\log n$ in the transfer as the more delicate half.
- Develop a symmetrization or transport scheme reducing an arbitrary log-concave measure to a product measure with bounded Lipschitz distortion — this would immediately tensorize.
- Sharpen the covariance SDE analysis: obtain a supermartingale for $\log\|\mathrm{Cov}(\mu_t)\|_{op}$ rather than the current pathwise bound.
- Settle intermediate classes: general unconditional bodies with a truly dimension-free constant; simplices and their sections; $\psi$-behaviour of random polytopes.
- Extend Guan's heat-flow estimate from the slicing functional to the Poincaré functional, the most direct hope after the 2025 slicing breakthrough.

## 9. Key References

- **[Foundational]** R. Kannan, L. Lovász, M. Simonovits. *Isoperimetric problems for convex bodies and a localization lemma.* Discrete & Computational Geometry, 13 (1995), 541–559. [DOI](https://doi.org/10.1007/bf02574061)
- **[Foundational]** C. Borell. *Convex set functions in $d$-space.* Periodica Mathematica Hungarica, 6 (1975), 111–136.
- **[Foundational]** S. G. Bobkov. *On isoperimetric constants for log-concave probability distributions.* Geometric Aspects of Functional Analysis (GAFA Seminar Notes), Lecture Notes in Math. 1910, Springer, 2007.
- **[Key technique]** R. Eldan. *Thin shell implies spectral gap up to polylog via a stochastic localization scheme.* Geometric and Functional Analysis, 23 (2013), 532–569. [DOI](https://doi.org/10.1007/s00039-013-0214-y)
- **[Key technique]** R. Eldan, B. Klartag. *Approximately gaussian marginals and the hyperplane conjecture.* Contemporary Mathematics 545, AMS, 2011, 55–68. [DOI](https://doi.org/10.1090/conm/545/10764)
- **[Structural]** E. Milman. *On the role of convexity in isoperimetry, spectral gap and concentration.* Inventiones Mathematicae, 177 (2009), 1–43. [DOI](https://doi.org/10.1007/s00222-009-0175-9)
- **[Partial results]** O. Guédon, E. Milman. *Interpolating thin-shell and sharp large-deviation estimates for isotropic log-concave measures.* Geometric and Functional Analysis, 21 (2011), 1043–1068. [DOI](https://doi.org/10.1007/s00039-011-0136-5)
- **[Partial results]** B. Klartag. *A Berry–Esseen type inequality for convex bodies with an unconditional basis.* Probability Theory and Related Fields, 145 (2009), 1–33. [DOI](https://doi.org/10.1007/s00440-008-0158-6)
- **[Partial results]** S. Sodin. *An isoperimetric inequality on the $\ell_p$ balls.* Annales de l'Institut Henri Poincaré (B), 44 (2008), 362–373. [DOI](https://doi.org/10.1214/07-aihp121)
- **[SOTA]** Y. T. Lee, S. S. Vempala. *Eldan's stochastic localization and the KLS hyperplane conjecture: an improved lower bound for expansion.* Proc. 58th IEEE FOCS, 2017. [DOI](https://doi.org/10.1109/focs.2017.96)
- **[SOTA]** Y. Chen. *An almost constant lower bound of the isoperimetric coefficient in the KLS conjecture.* Geometric and Functional Analysis, 31 (2021), 34–61. [DOI](https://doi.org/10.1007/s00039-021-00558-4)
- **[SOTA]** B. Klartag, J. Lehec. *Bourgain's slicing problem and KLS isoperimetry up to polylog.* Geometric and Functional Analysis, 32 (2022), 1134–1159. [DOI](https://doi.org/10.1007/s00039-022-00612-9)
- **[SOTA]** B. Klartag. *Logarithmic bounds for isoperimetry and slices of convex sets.* Ars Inveniendi Analytica, 2023.
- **[SOTA / Recent]** B. Klartag, J. Lehec. *Affirmative resolution of Bourgain's slicing problem using Guan's bound.* arXiv:2412.15044, 2024. [DOI](https://doi.org/10.1007/s00039-025-00718-w)
- **[Survey]** S. Brazitikos, A. Giannopoulos, P. Valettas, B.-H. Vritsiou. *Geometry of Isotropic Convex Bodies.* Mathematical Surveys and Monographs 196, AMS, 2014. [DOI](https://doi.org/10.1090/surv/196)
- **[Survey]** Y. T. Lee, S. S. Vempala. *The Kannan–Lovász–Simonovits conjecture.* Current Developments in Mathematics 2017, International Press, 2019. [DOI](https://doi.org/10.4310/cdm.2017.v2017.n1.a1)

## 10. Worked Example / Concrete Special Case

**The isotropic cube.** Let $Q_n = [-\sqrt3,\sqrt3]^n$ with $\mu$ the uniform probability measure. Each coordinate has variance $\frac{(2\sqrt3)^2}{12} = 1$ and mean $0$, so $\mu$ is isotropic log-concave.

*Upper bound on $h_\mu$.* Cut with the half-space $S = \{x : x_1 \le 0\}$. Then $\mu(S) = 1/2$ and the interface is a facet-parallel slab face of $(n-1)$-volume $(2\sqrt3)^{n-1}$, while $\mathrm{vol}(Q_n) = (2\sqrt3)^n$. Hence

$$
\mu^+(\partial S) = \frac{(2\sqrt3)^{n-1}}{(2\sqrt3)^n} = \frac{1}{2\sqrt3},
\qquad
\frac{\mu^+(\partial S)}{\min\{\mu(S),1-\mu(S)\}} = \frac{1/(2\sqrt3)}{1/2} = \frac{1}{\sqrt3} \approx 0.577 .
$$

By Hadwiger's theorem this half-space cut is optimal for the cube, so $h_\mu = 1/\sqrt3$ — **independent of $n$**. The KLS conjecture asserts this dimension-freeness is universal.

*Cross-check via the spectral gap.* The Neumann Laplacian on an interval of length $L=2\sqrt3$ has first nonzero eigenvalue $\pi^2/L^2 = \pi^2/12$. Tensorization gives $\lambda_1(Q_n) = \pi^2/12 \approx 0.822$ for all $n$, so $C_P = 12/\pi^2$. Cheeger's inequality demands $\lambda_1 \ge h_\mu^2/4 = 1/12 \approx 0.083$ — satisfied with room to spare, confirming the two formulations agree up to universal constants.

*Where the difficulty lives.* Replace $Q_n$ by a general isotropic convex body $K$. There is no product structure to tensorize, and $|X|$ need no longer concentrate: all that is known unconditionally is $\mathrm{Var}(|X|) \lesssim \log n$, so the analogue of the calculation above degrades by $\sqrt{\log n}$. The conjecture is exactly the statement that the cube's behaviour, not the degraded bound, is the truth for every $K$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*