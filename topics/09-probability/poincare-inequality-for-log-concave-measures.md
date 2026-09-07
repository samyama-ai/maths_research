---
id: 09-probability/poincare-inequality-for-log-concave-measures
title: "Poincare Inequality for Log-Concave Measures"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Poincaré Inequality for Log-Concave Measures (KLS Spectral-Gap Conjecture)

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/poincare-inequality-for-log-concave-measures` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mu$ be a log-concave probability measure on $\mathbb{R}^n$ that is **isotropic**: barycenter at the origin and covariance the identity. The **Poincaré (spectral-gap) constant** $C_P(\mu)$ is the smallest constant such that

$$\operatorname{Var}_\mu(f) \;\le\; C_P(\mu)\int_{\mathbb{R}^n} |\nabla f|^2 \, d\mu \qquad \text{for all locally Lipschitz } f \in L^2(\mu).$$

**Conjecture (Kannan–Lovász–Simonovits, 1995).** There is a universal constant $C$, independent of the dimension $n$ and of $\mu$, with

$$C_P(\mu) \le C \quad \text{for every isotropic log-concave } \mu \text{ on } \mathbb{R}^n .$$

Equivalently, writing $\psi_n$ for the supremum of $\sqrt{C_P(\mu)}$ over all isotropic log-concave measures in dimension $n$, the claim is $\psi_n = O(1)$. In its original isoperimetric form the conjecture asserts a dimension-free Cheeger constant: for every Borel $A$,

$$\mu^+(\partial A) \;\ge\; c\,\min\{\mu(A), 1-\mu(A)\},$$

with $c>0$ universal, where $\mu^+$ is the Minkowski boundary measure.

A complete proof must supply a universal $C$ valid for all $n$ and all isotropic log-concave $\mu$ (including uniform measures on convex bodies). A disproof requires a sequence $\mu_n$ of isotropic log-concave measures with $C_P(\mu_n) \to \infty$. The linear test function $f(x) = \langle x, \theta\rangle$ forces $C_P(\mu) \ge 1$ always, so only the upper bound is at stake.

## 2. Mathematical Foundations

**Log-concavity.** $\mu$ is log-concave if for all compact $A,B$ and $\lambda \in (0,1)$,
$$\mu(\lambda A + (1-\lambda)B) \ge \mu(A)^\lambda \mu(B)^{1-\lambda}.$$
By Borell's theorem, a log-concave measure not supported on a proper affine subspace has density $e^{-V}$ with $V:\mathbb{R}^n \to (-\infty,\infty]$ convex. Uniform measures on convex bodies and Gaussians are log-concave; the class is closed under linear images, marginals (Prékopa–Leindler) and convolution.

**Isotropic normalization.** $\int x \, d\mu = 0$ and $\int x_i x_j \, d\mu = \delta_{ij}$. Any log-concave $\mu$ can be brought to this position by an affine map, and $C_P$ transforms accordingly, so the conjecture is affine-invariant in the normalized form $C_P(\mu)\le C\,\|\operatorname{Cov}(\mu)\|_{\mathrm{op}}$.

**Spectral formulation.** $1/C_P(\mu)$ is the spectral gap $\lambda_1$ of the weighted Laplacian $L f = \Delta f - \langle \nabla V, \nabla f\rangle$, the generator of the Langevin diffusion $dX_t = dB_t - \tfrac12\nabla V(X_t)\,dt$ with invariant measure $\mu$. Equivalently $\|P_t f - \int f d\mu\|_{L^2} \le e^{-t/C_P}\|f\|_{L^2}$: the conjecture asserts dimension-free mixing.

**Cheeger constant.** $\psi_\mu^{-1} := \inf_A \mu^+(\partial A)/\min\{\mu(A),1-\mu(A)\}$. Cheeger's inequality gives $C_P \le 4\psi_\mu^2$; the converse, false in general, **holds** in the log-concave class by E. Milman's theorem (2009): $\psi_\mu \asymp \sqrt{C_P(\mu)}$ up to universal constants, and both are further equivalent to the first-moment concentration profile. Hence the isoperimetric and spectral forms of KLS are the same problem.

**Related conjectures, in order of strength.**
- *Thin-shell (variance) conjecture* (Anttila–Ball–Perissinaki; Bobkov–Koldobsky): $\sigma_n^2 := \sup_\mu \operatorname{Var}_\mu(|X|) = O(1)$, equivalently $\operatorname{Var}(|X|^2) = O(n)$.
- *Slicing / hyperplane conjecture* (Bourgain): the isotropic constant $L_n = \sup_K L_K$ is bounded, where $L_K^2 = |K|^{-1-2/n}\det\operatorname{Cov}(K)^{1/n}$.

Known implications: $\text{KLS} \Rightarrow \text{thin shell} \Rightarrow \text{slicing}$ (Eldan–Klartag, 2011), with $\psi_n \gtrsim \sigma_n \gtrsim 1$. Eldan (2013) proved the near-converse $\psi_n^2 \lesssim \log n \cdot \sup_{k \le n}\sigma_k^2$.

**Brascamp–Lieb inequality.** If $V$ is $C^2$ and strictly convex,
$$\operatorname{Var}_\mu(f) \le \int \langle (\nabla^2 V)^{-1}\nabla f, \nabla f \rangle \, d\mu,$$
which yields $C_P \le 1/\kappa$ for $\kappa$-strongly log-concave $\mu$ (Bakry–Émery). KLS is exactly the regime where no strong convexity is available.

## 3. History & State of the Art (SOTA)

- **1995.** Kannan, Lovász and Simonovits state the conjecture in *Isoperimetric problems for convex bodies and a localization lemma* (Discrete Comput. Geom.), motivated by the mixing time of the ball walk for volume computation. Their localization lemma reduces $n$-dimensional isoperimetry to one-dimensional inequalities on needles.
- **1999–2003.** Bobkov proves $\psi_n \lesssim n^{1/4}\,(\text{diam})^{1/2}$-type bounds and the general estimate $\psi_n \lesssim \sqrt{n}$; Bobkov's bound $\psi_n^2 \lesssim \sigma_n^2 \cdot n^{?}$ variants appear.
- **2006–2007.** Klartag proves the central limit theorem for convex bodies and the first power-saving thin-shell bound $\sigma_n^2 \lesssim n^{-c}$.
- **2013.** Eldan introduces **stochastic localization** and proves thin-shell $\Rightarrow$ KLS up to $\sqrt{\log n}$, giving $\psi_n \lesssim n^{1/3}$ after combining with Guédon–Milman's $\sigma_n \lesssim n^{1/3}$.
- **2017.** Lee and Vempala obtain $\psi_n \lesssim n^{1/4}$ via a refined stochastic-localization potential.
- **2021.** Y. Chen proves $\psi_n \le n^{o(1)}$ — explicitly $\exp(C\sqrt{\log n \log\log n})$ — by iterating Eldan's localization with a bootstrapped covariance control (*An almost constant lower bound of the isoperimetric coefficient in the KLS conjecture*, GAFA).
- **2022.** Klartag–Lehec push to $\psi_n \lesssim \log^4 n$ (polylog); Jambulapati–Lee–Vempala reduce to $\psi_n \lesssim \sqrt{\log n}\,(\log\log n)^{?}$ — the "slightly improved bound".
- **2023.** Klartag obtains $\psi_n \le C\sqrt{\log n}$ and $L_n \lesssim \sqrt[4]{\log n}$ by a direct needle/localization argument (*Logarithmic bounds for isoperimetry and slices of convex sets*, Ars Inveniendi Analytica).
- **2024–2025.** Guan's sharpened bound on the Fisher-information dynamics along stochastic localization is used by Klartag–Lehec to prove the **slicing conjecture** ($L_n \le C$) affirmatively — the weakest of the three conjectures now settled. *(frontier — verify)*

**Current SOTA for the Poincaré constant: $\psi_n \asymp \sqrt{C_P} \le C\sqrt{\log n}$, i.e. $C_P(\mu) \le C\log n$.** The gap to $O(1)$ is a single logarithm.

## 4. Partial Results / Verified Cases

Classes for which a dimension-free bound is proven:

- **Gaussian and strongly log-concave.** $\gamma_n$ has $C_P = 1$ (Chernoff); any $\kappa$-uniformly-convex potential gives $C_P \le 1/\kappa$ by Bakry–Émery.
- **Products.** Poincaré tensorizes exactly: $C_P(\mu_1\otimes\cdots\otimes\mu_n) = \max_i C_P(\mu_i)$. Hence cubes, and all product log-concave measures, satisfy KLS with $C \le \sup_i C_P(\mu_i) \le C_0$ by the one-dimensional bound $C_P(\mu) \le 12\,\operatorname{Var}(\mu)$ for log-concave $\mu$ on $\mathbb{R}$ (Bobkov).
- **Unconditional convex bodies.** Klartag (2009) and Barthe–Cordero-Erausquin give $\psi \lesssim \sqrt{\log n}$; for unconditional bodies with additional $1$-symmetry the constant is $O(1)$.
- **$\ell_p^n$ balls, $1\le p\le\infty$.** Sodin and Latała–Wojtaszczyk: $\psi = O(1)$ uniformly in $n$ and $p$.
- **Rotationally invariant (spherically symmetric) log-concave measures.** Bobkov (2003): $C_P = O(1)$.
- **Simplex, cross-polytope, hypercube.** Explicit universal constants.
- **Bodies with bounded "outer radius" after normalization**, e.g. $\mu$ supported in a ball of radius $O(\sqrt n)$ with a spectral-gap-friendly structure; also convex bodies of small diameter via Payne–Weinberger: for a convex domain $K$ of diameter $D$ with uniform measure, $C_P \le D^2/\pi^2$.
- **Low-dimensional marginals / small $n$.** $n=1$: $C_P \le 12$ (isotropic case, sharp order). $n=2,3$: absolute constants follow from the one-dimensional localization argument of KLS.
- **General case, all $n$:** $C_P(\mu) \le C\log n$ (Klartag 2023; Jambulapati–Lee–Vempala 2022).

## 5. Principal Obstacles

- **Localization degenerates.** The KLS localization lemma reduces to one-dimensional log-concave needles, but the reduction loses information about how needle directions correlate; a naive union over needles reintroduces a $\sqrt n$ or $\log n$ factor. Klartag's needle-decomposition refinement recovered only $\sqrt{\log n}$.
- **No strong convexity.** Bakry–Émery, Brascamp–Lieb and curvature-dimension $CD(\kappa,\infty)$ criteria are vacuous for uniform measures on convex bodies, where $\nabla^2 V \equiv 0$ on the interior. The whole difficulty is that convexity is *flat*.
- **Fisher-information blow-up in stochastic localization.** Eldan's scheme evolves $\mu_t \propto e^{\langle c_t,x\rangle - t|x|^2/2}\,d\mu$; the covariance $A_t$ satisfies a matrix SDE whose operator norm must stay $O(1)$ for time $t \sim 1$. Controlling $\|A_t\|_{\mathrm{op}}$ requires bounding a fourth-moment/Fisher-information functional whose current estimates lose exactly one logarithm.
- **Thin shell is itself open.** The best known is $\sigma_n \lesssim n^{o(1)}$ (or polylog); since $\psi_n \gtrsim \sigma_n$, KLS cannot be proven without also proving the thin-shell conjecture, and Eldan's converse costs $\sqrt{\log n}$.
- **No usable symmetry or transport map.** Caffarelli's contraction theorem gives Lipschitz transport from Gaussians only under strong convexity; there is no known dimension-free Lipschitz map from $\gamma_n$ onto a general isotropic log-concave measure — indeed such a map would immediately prove KLS.

## 6. The Gap

Proven: $1 \le C_P(\mu) \le C \log n$. Conjectured: $C_P(\mu) \le C$. The gap is the single factor $\log n$, and it is not cosmetic — it decomposes as
$$\psi_n^2 \;\lesssim\; \underbrace{\sup_{k\le n}\sigma_k^2}_{\text{thin shell, open}} \times \underbrace{\log n}_{\text{Eldan's reduction loss}},$$
so closing it needs *two* independent advances: (i) a dimension-free thin-shell bound $\operatorname{Var}(|X|)=O(1)$, and (ii) a loss-free version of stochastic localization (or another route) that transfers thin-shell to spectral gap without the logarithmic overhead. The recent resolution of slicing shows that the localization machinery can be made lossless for the weakest of the three conjectures; whether Guan-type Fisher-information bounds can be strengthened enough to reach thin shell is the live question.

## 7. Current Research (as of June 2026)

- **Stochastic localization refinements.** Klartag (Weizmann) and Lehec (Poitiers/Paris-Dauphine) continue the program that settled slicing; the announced goal is transferring the Guan-type entropy/Fisher-information estimate from the isotropic-constant functional to the thin-shell functional. *(frontier — verify)*
- **Algorithmic school.** Vempala (Georgia Tech), Lee (UW), Jambulapati, Chen: KLS bounds drive mixing-time guarantees for sampling from log-concave densities; even $\log n$ improvements change complexity exponents in volume computation and Langevin-based samplers.
- **Functional-inequality school.** Cordero-Erausquin, Barthe, Bobkov, Milman (E. and V.): entropy-based and $B$-theorem approaches, Bochner-type identities with degenerate curvature, and the Gaussian-correlation/Bourgain-type interpolations.
- **Transport approaches.** Search for a $O(1)$-Lipschitz map from $\gamma_n$ to isotropic log-concave measures via Langevin/heat-flow transport (Kim–Milman, Mikulincer–Shenfeld). Current bounds are dimension-dependent.
- **Spectral/heat-kernel bounds on convex domains.** Neumann eigenvalue estimates for convex domains with degenerate boundary geometry.

## 8. Future Work

- Prove the thin-shell conjecture $\sigma_n = O(1)$; combined with a lossless localization it settles KLS.
- Remove the $\log n$ in Eldan's thin-shell $\Rightarrow$ KLS transfer, e.g. by an exponential-supermartingale control on $\|A_t\|_{\mathrm{op}}$ rather than a union bound over dyadic scales.
- Extend Guan's Fisher-information inequality from the slicing functional to higher moments of $|X|$.
- Construct (or rule out) a dimension-free Lipschitz transport $T:\gamma_n \to \mu$ for isotropic log-concave $\mu$.
- Settle KLS for structured subclasses of growing generality: bodies with $O(1)$-symmetry groups, projections of $\ell_p$-balls, random polytopes.
- Sharpen the constant: the conjectured extremizer is believed to be the cube or the simplex; identify the true value of $\lim_n \psi_n$ conditional on boundedness.

## 9. Key References

- **[Foundational]** R. Kannan, L. Lovász, M. Simonovits. *Isoperimetric problems for convex bodies and a localization lemma.* Discrete & Computational Geometry, 13:541–559, 1995.
- **[Foundational]** C. Borell. *Convex set functions in $d$-space.* Periodica Mathematica Hungarica, 6:111–136, 1975.
- **[Foundational]** H. J. Brascamp, E. H. Lieb. *On extensions of the Brunn–Minkowski and Prékopa–Leindler theorems.* Journal of Functional Analysis, 22:366–389, 1976.
- **[Structural]** E. Milman. *On the role of convexity in isoperimetry, spectral gap and concentration.* Inventiones Mathematicae, 177:1–43, 2009.
- **[Structural]** R. Eldan. *Thin shell implies spectral gap up to polylog via a stochastic localization scheme.* Geometric and Functional Analysis, 23:532–569, 2013.
- **[Structural]** R. Eldan, B. Klartag. *Approximately gaussian marginals and the hyperplane conjecture.* Contemporary Mathematics, 545:55–68, 2011.
- **[Partial]** S. G. Bobkov. *Spectral gap and concentration for some spherically symmetric probability measures.* GAFA Seminar Notes, Lecture Notes in Mathematics 1807, Springer, 2003.
- **[Partial]** B. Klartag. *A Berry–Esseen type inequality for convex bodies with an unconditional basis.* Probability Theory and Related Fields, 145:1–33, 2009.
- **[Partial]** R. Latała, J. O. Wojtaszczyk. *On the infimum convolution inequality.* Studia Mathematica, 189:147–187, 2008.
- **[SOTA]** Y. T. Lee, S. S. Vempala. *Eldan's stochastic localization and the KLS hyperplane conjecture: an improved lower bound for expansion.* Proc. IEEE FOCS, 2017.
- **[SOTA]** Y. Chen. *An almost constant lower bound of the isoperimetric coefficient in the KLS conjecture.* Geometric and Functional Analysis, 31:34–61, 2021.
- **[SOTA]** B. Klartag, J. Lehec. *Bourgain's slicing problem and KLS isoperimetry up to polylog.* Geometric and Functional Analysis, 32:1134–1159, 2022.
- **[SOTA]** A. Jambulapati, Y. T. Lee, S. S. Vempala. *A slightly improved bound for the KLS constant.* arXiv:2208.11644, 2022.
- **[SOTA]** B. Klartag. *Logarithmic bounds for isoperimetry and slices of convex sets.* Ars Inveniendi Analytica, 2023.
- **[SOTA]** B. Klartag, J. Lehec. *Affirmative resolution of Bourgain's slicing problem using Guan's bound.* arXiv:2412.15044, 2024. *(frontier — verify)*
- **[Survey]** S. Brazitikos, A. Giannopoulos, P. Valettas, B.-H. Vritsiou. *Geometry of Isotropic Convex Bodies.* AMS Mathematical Surveys and Monographs 196, 2014.
- **[Survey]** Y. T. Lee, S. S. Vempala. *The Kannan–Lovász–Simonovits conjecture.* Current Developments in Mathematics 2017, International Press, 2019.
- **[Textbook]** D. Bakry, I. Gentil, M. Ledoux. *Analysis and Geometry of Markov Diffusion Operators.* Grundlehren 348, Springer, 2014.

## 10. Worked Example / Concrete Special Case

**The isotropic cube.** Take $\mu_n = \mathrm{Unif}(K_n)$ with $K_n = [-\sqrt3, \sqrt3]^n$. Then $|K_n| = (2\sqrt3)^n$ and each coordinate has $\operatorname{Var}(X_i) = (2\sqrt3)^2/12 = 1$, so $\mu_n$ is isotropic.

*Step 1 — one dimension.* For $\mathrm{Unif}([-a,a])$ the Neumann Laplacian on the interval has eigenfunctions $\cos(k\pi(x+a)/(2a))$ with eigenvalues $\lambda_k = (k\pi/2a)^2$. The spectral gap is $\lambda_1 = \pi^2/(2a)^2$, so
$$C_P\big(\mathrm{Unif}([-a,a])\big) = \frac{4a^2}{\pi^2}.$$
With $a=\sqrt3$: $C_P = 12/\pi^2 \approx 1.216$.

*Step 2 — tensorization.* For product measures, decomposing $\operatorname{Var}(f)$ along the Efron–Stein martingale gives
$$\operatorname{Var}_{\mu_n}(f) \le \sum_{i=1}^n \mathbb{E}\big[\operatorname{Var}_{x_i}(f)\big] \le \max_i C_P(\mu^{(i)}) \sum_{i=1}^n \mathbb{E}\big[(\partial_i f)^2\big] = \max_i C_P(\mu^{(i)}) \int |\nabla f|^2 d\mu_n.$$
Hence $C_P(\mu_n) = 12/\pi^2$ for **every** $n$ — dimension-free, exactly as KLS predicts.

*Step 3 — sharpness.* Take $f(x) = x_1$: $\operatorname{Var}(f) = 1$, $\int|\nabla f|^2 d\mu_n = 1$, so $C_P \ge 1$. The extremal function is $f(x) = \cos\big(\pi(x_1+\sqrt3)/(2\sqrt3)\big)$, achieving $12/\pi^2$.

*Step 4 — where the general case breaks.* Replace the cube by an arbitrary isotropic convex body $K$. Tensorization is unavailable (coordinates are dependent), and Payne–Weinberger gives only $C_P \le \operatorname{diam}(K)^2/\pi^2$, which for isotropic bodies can be as large as $\Theta(n)$ — e.g. the isotropic simplex has diameter $\Theta(\sqrt n)$, so this route yields $C_P = O(n)$, off by a factor $n$. Even for the simplex the true answer is $O(1)$, proven by an explicit needle decomposition rather than by any general principle. That gulf — between $O(1)$ for every structured example computed and $O(\log n)$ for the general theorem — is the content of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*