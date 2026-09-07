---
id: 09-probability/ginibre-ensemble-circular-law
title: "Ginibre Ensemble Circular Law"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ginibre Ensemble Circular Law

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/ginibre-ensemble-circular-law` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $X_n = (x_{ij})_{i,j\le n}$ have i.i.d. complex entries with $\mathbb{E}x_{11}=0$, $\mathbb{E}|x_{11}|^2=1$, and let $\lambda_1,\dots,\lambda_n$ be the eigenvalues of $n^{-1/2}X_n$. The **empirical spectral distribution** (ESD) is the random probability measure
$$\mu_n \;=\; \frac1n\sum_{k=1}^n \delta_{\lambda_k}\quad\text{on }\mathbb{C}.$$

**Circular law.** Almost surely, $\mu_n \Rightarrow \mu_{\mathrm{circ}}$ weakly, where $\mu_{\mathrm{circ}}$ is the uniform measure on the unit disc,
$$d\mu_{\mathrm{circ}}(z) \;=\; \frac1\pi \,\mathbf{1}_{\{|z|\le 1\}}\, dA(z).$$

The **Ginibre ensemble** is the Gaussian special case $x_{ij}\sim\mathcal{N}_{\mathbb{C}}(0,1)$ (complex Ginibre $\mathrm{Gin}_{\mathbb{C}}(n)$), with real ($\mathrm{Gin}_{\mathbb{R}}$) and quaternion ($\mathrm{Gin}_{\mathbb{H}}$) variants.

The global statement is a **theorem** (Girko 1984 program; Bai 1997 under regularity; Tao–Vu 2010 under the bare $L^2$ hypothesis). What remains open is the *universality package built on top of it*:

1. **Local universality in the bulk and at the edge** for general i.i.d. entries without moment-matching assumptions.
2. **Circular law for structured / constrained ensembles**: random regular digraphs of bounded degree, adjacency matrices of sparse directed graphs with $d = O(1)$, doubly stochastic matrices.
3. **Sharp rate of convergence** $\sup_{\text{convex }B}|\mu_n(B)-\mu_{\mathrm{circ}}(B)|$ and optimal Kolmogorov-type bounds.

A complete resolution of (1) means: for every fixed $z_0$ with $|z_0|<1$, the point process $\{n^{1/2}(\lambda_k - z_0)\}$ converges to the infinite Ginibre point process, for all i.i.d. entries with finite variance (or an explicitly minimal moment condition), with no four-moment matching.

## 2. Mathematical Foundations

**Ginibre joint density.** For $M\sim\mathrm{Gin}_{\mathbb{C}}(n)$ with density $\propto e^{-\operatorname{tr} M^*M}$, the eigenvalues have joint density on $\mathbb{C}^n$
$$p_n(z_1,\dots,z_n) \;=\; \frac{1}{\pi^n\prod_{k=1}^n k!}\;\prod_{i<j}|z_i-z_j|^2 \;\exp\Big(-\sum_{k=1}^n |z_k|^2\Big).$$
This is a $\beta=2$ Coulomb gas at inverse temperature $2$ in a quadratic confining potential.

**Determinantal structure.** The (unscaled) eigenvalue process is determinantal with respect to Lebesgue measure with kernel
$$K_n(z,w) \;=\; \frac{1}{\pi}\, e^{-\frac{|z|^2+|w|^2}{2}} \sum_{k=0}^{n-1}\frac{(z\bar w)^k}{k!},$$
so $\rho_n^{(m)}(z_1,\dots,z_m)=\det\big(K_n(z_i,z_j)\big)_{i,j\le m}$. The one-point function is $\rho^{(1)}_n(z)=K_n(z,z)$; after scaling $z\mapsto \sqrt n\,z$ it converges to $\frac{n}{\pi}\mathbf 1_{|z|<1}$, which is the circular law.

**Local (bulk) limit.** For $|z_0|<1$, $K_n$ converges after rescaling to the **infinite Ginibre kernel**
$$K_\infty(z,w) \;=\; \frac{1}{\pi}\,e^{z\bar w - \frac{|z|^2+|w|^2}{2}},$$
the unique translation-invariant determinantal process of intensity $1/\pi$ in this class (Peres–Virág-type rigidity).

**Girko's Hermitization.** Non-Hermitian spectra are unstable, so one passes to the family of Hermitian matrices
$$H_n(z) \;=\; \begin{pmatrix} 0 & n^{-1/2}X_n - z \\ (n^{-1/2}X_n-z)^* & 0\end{pmatrix},$$
whose spectrum is $\pm s_j(n^{-1/2}X_n - z)$, the singular values. The **logarithmic potential**
$$U_{\mu_n}(z) \;=\; -\int_{\mathbb{C}}\log|z-w|\,d\mu_n(w) \;=\; -\frac1n\log\big|\det(n^{-1/2}X_n - z)\big| \;=\; -\frac1n\sum_{j=1}^n \log s_j$$
determines $\mu_n$ via $\mu_n = \frac{1}{2\pi}\Delta\, U_{\mu_n}$ in the distributional sense. Hence
$$\mu_n \Rightarrow \mu \iff U_{\mu_n}(z)\to U_\mu(z) \text{ for a.e. } z.$$
The limiting singular value law of $n^{-1/2}X_n - z$ is the **deformed quarter-circle** $\nu_z$, and the identity
$$-\int_0^\infty \log s\,d\nu_z(s) \;=\; \begin{cases}\frac{1-|z|^2}{2}-\log|z| \cdot 0 - \tfrac12(|z|^2-1), & |z|\le 1\\ \log|z|,&|z|>1\end{cases}$$
reduces (after simplification) to $U_{\mu_{\mathrm{circ}}}(z)=\frac{1-|z|^2}{2}$ for $|z|\le1$ and $-\log|z|$ for $|z|>1$ — exactly the logarithmic potential of the uniform disc.

**Critical difficulty.** $\log$ is unbounded at $0$ and $\infty$; convergence of $\nu_z$ alone is not enough. One needs uniform integrability of $\log s$ near $s=0$, i.e. quantitative lower bounds on the **smallest singular value** $s_n(n^{-1/2}X_n-z)$.

**Real Ginibre.** $\mathrm{Gin}_{\mathbb{R}}(n)$ has a Pfaffian point process with an atomic component on $\mathbb{R}$; the expected number of real eigenvalues is (Edelman–Kostlan–Shub)
$$\mathbb{E}\,\\#\{\text{real }\lambda\} \;=\; \sqrt{\tfrac{2n}{\pi}}\,\big(1+o(1)\big),$$
a set of density zero, so the circular law is unaffected.

## 3. History & State of the Art (SOTA)

- **1965.** Ginibre computes the joint eigenvalue densities for the complex, real and quaternion Gaussian ensembles.
- **1967.** Mehta derives the circular law for $\mathrm{Gin}_{\mathbb{C}}(n)$ from the determinantal kernel — the first proof, restricted to the Gaussian case.
- **1984.** Girko announces the circular law for general i.i.d. entries and introduces Hermitization plus the logarithmic potential. The argument has recognized gaps (interchange of limits, control of small singular values).
- **1997.** Bai gives the first complete proof beyond Gaussians: bounded density for $x_{11}$ and finite $6$th moment; rate $O(n^{-1/4})$ in a Kolmogorov-type metric.
- **2008–2010.** Götze–Tikhomirov, Pan–Zhou, and Tao–Vu successively weaken the hypotheses, the engine being Rudelson–Vershynin's inverse Littlewood–Offord smallest-singular-value bounds. **Tao–Vu (Ann. Probab. 2010)** prove the circular law assuming only finite variance — the optimal condition — with an appendix by Krishnapur.
- **2014–2015.** Local circular law: Bourgade–Yau–Yin, and Tao–Vu's four-moment theorem for local non-Hermitian statistics, bring the resolution scale down to $n^{-1/2+\varepsilon}$.
- **2018–2023.** Alt–Erdős–Krüger (inhomogeneous/variance-profile circular law), Cipolloni–Erdős–Schröder (edge universality; CLT for linear eigenvalue statistics with an explicit Gaussian-free-field-type limit).

## 4. Partial Results / Verified Cases

| Setting | Status | Source |
|---|---|---|
| $\mathrm{Gin}_{\mathbb{C}}(n)$, all $n$ | Exact finite-$n$ determinantal formulas; circular law with full local statistics | Ginibre 1965; Mehta 1967 |
| $\mathrm{Gin}_{\mathbb{R}}(n)$, $\mathrm{Gin}_{\mathbb{H}}(n)$ | Pfaffian kernels; circular law + real-axis $\sqrt{2n/\pi}$ correction | Edelman 1997; Borodin–Sinclair 2009 |
| i.i.d. entries, bounded density, $\mathbb{E}|x|^6<\infty$ | Proved | Bai 1997 |
| i.i.d. entries, $\mathbb{E}|x|^{2}<\infty$ only | Proved (optimal moment condition) | Tao–Vu 2010 |
| Local law on scales $n^{-1/2+\varepsilon}$, bulk | Proved under sub-exponential tails | Bourgade–Yau–Yin 2014 |
| Edge: spectral radius of Ginibre $\to 1$, fluctuations Gumbel at scale $\sqrt{\gamma_n/(4n)}$, $\gamma_n=\log n-2\log\log n-\log 2\pi$ | Proved | Rider 2003 |
| Edge universality for general i.i.d. entries | Proved | Cipolloni–Erdős–Schröder 2021 |
| Variance profiles $\mathbb{E}|x_{ij}|^2=s_{ij}/n$ (inhomogeneous circular law) | Proved | Alt–Erdős–Krüger 2018 |
| Heavy tails, $\alpha$-stable entries, $\alpha\in(0,2)$ | Limit exists, is *not* circular | Bordenave–Caputo–Chafaï 2011 |
| Sparse i.i.d., $p n \to\infty$ arbitrarily slowly | Circular law holds | Rudelson–Tikhomirov 2019 |
| Random $d$-regular digraphs, $d\gg \log^2 n$ | Circular law holds | Cook 2019; Basak–Cook–Zeitouni |
| Random $d$-regular digraphs, $d = O(1)$ | **Open** | — |
| Linear statistics CLT $\sum f(\lambda_k) - n\int f\,d\mu_{\mathrm{circ}}$ | Proved, limit = $H^1$-noise on the disc + boundary term | Rider–Virág 2007 (Ginibre); Cipolloni–Erdős–Schröder 2023 (i.i.d.) |

## 5. Principal Obstacles

- **No spectral stability.** For Hermitian matrices, Weyl's inequality gives $|\lambda_k(A)-\lambda_k(B)|\le\|A-B\|$. For non-normal matrices this fails catastrophically: the $n\times n$ nilpotent Jordan block has spectrum $\{0\}$, but adding $\varepsilon$ in the corner moves the eigenvalues to the circle $|z|=\varepsilon^{1/n}$, which is $\approx 1$ for $\varepsilon=e^{-n}$. Hence moment methods, resolvent perturbation, and Lindeberg swapping cannot be applied to the spectrum directly.
- **Moment method is blind.** $\frac1n\mathbb{E}\operatorname{tr}(n^{-1/2}X)^k \to 0$ for every $k\ge1$, matching $\int z^k d\mu_{\mathrm{circ}}=0$; but $\mu_{\mathrm{circ}}$ is not determined by its holomorphic moments (any rotationally invariant measure has the same ones). Mixed moments $\operatorname{tr}(X^k (X^*)^l)$ are not spectral. This is why Hermitization is mandatory.
- **The $\log$ singularity.** Hermitization converts the problem to controlling $\frac1n\sum_j\log s_j(n^{-1/2}X-z)$. A single singular value of size $e^{-n^{1+\delta}}$ ruins the estimate. Proving $s_n \ge n^{-C}$ with probability $1-o(1)$ requires anti-concentration (inverse Littlewood–Offord theory), which is combinatorially delicate and degrades badly for discrete or constrained entries.
- **Constrained ensembles break independence.** For $d$-regular digraphs the rows are not independent; row sums are fixed. Anti-concentration arguments lose their independent-summand structure, and for $d=O(1)$ no known method establishes even $s_n>e^{-n^{0.99}}$.
- **Local scale: two-scale mismatch.** A local circular law on scale $\eta$ requires control of $H_n(z)$ near the *hard edge* of its singular spectrum, where the deformed quarter-circle vanishes; the standard Hermitian local-law machinery (self-consistent equations, fluctuation averaging) loses its stability there.

## 6. The Gap

Proven: global convergence $\mu_n\Rightarrow\mu_{\mathrm{circ}}$ under the minimal hypothesis $\mathbb{E}|x_{11}|^2=1$, and local/edge universality under moment or tail conditions (sub-exponential decay, or four-moment matching).

The general statement demands the same conclusions **without** those auxiliary hypotheses, and for **dependent** models. The precise barrier is quantitative invertibility:
$$\mathbb{P}\Big(s_n\big(n^{-1/2}A_n - z\big) \le n^{-C}\Big) \;=\; o(1)$$
for $A_n$ the adjacency matrix of a random $d$-regular digraph with $d$ fixed, uniformly over $z$ in compact sets. Every proof of the circular law reduces to such an estimate; none of the existing techniques (Rudelson–Vershynin least common denominator, Tao–Vu inverse Littlewood–Offord, Basak–Rudelson sparse arguments, Tikhomirov's method for singularity of Bernoulli matrices) delivers it below $d\sim\log n$. Crossing that gap is the exact missing step.

## 7. Current Research (as of June 2026)

- **IST Austria (Erdős group; Cipolloni, Schröder).** Non-Hermitian local laws, eigenvector overlaps, and the "$\log$-correlated field" description of $\log|\det(X-z)|$. Recent work extends CLT and edge universality to inhomogeneous and deformed models. *(frontier — verify)* extensions to matrices with jointly dependent entries.
- **Princeton/NYU (Bourgade, Yau).** Dynamical approach: the **Ginibre flow** (Ornstein–Uhlenbeck evolution of non-Hermitian matrices) plus a "coupling + local relaxation" argument for eigenvalue statistics; the goal is removing four-moment matching entirely.
- **Sparse and combinatorial models (Cook, Basak, Rudelson, Tikhomirov, Litvak–Tikhomirov).** Pushing the circular law for $d$-regular digraphs toward $d=O(1)$; the bounded-degree case is expected to have a *non-circular* limit for very small $d$ due to atoms and cycle structure. *(frontier — verify)* claimed progress at $d\gtrsim \log n/\log\log n$.
- **Coulomb-gas / large-deviations school (Chafaï, Bordenave, Serfaty, Leblé).** Large deviations for $\mu_n$ at speed $n^2$ with the logarithmic-energy rate functional; fluctuation theory for general $\beta$ two-dimensional gases.
- **Applications-driven.** Non-Hermitian random matrices in neural-network dynamics (May–Wigner stability, spectral radius criteria) and in non-Hermitian quantum mechanics / open-system Lindbladians, where the circular law is the reference null model.

## 8. Future Work

- Prove the **local circular law at the optimal scale $n^{-1/2}$** (no $\varepsilon$) with an optimal error, matching the Hermitian state of the art.
- Establish **bulk universality for i.i.d. matrices with only finitely many moments**, removing the sub-exponential and moment-matching hypotheses — the analogue of Erdős–Schlein–Yau for the non-Hermitian setting.
- Settle the **bounded-degree regular digraph** case: either prove the circular law or identify the correct non-circular limit.
- Obtain **sharp convergence rates**: current best global rates are polynomial ($n^{-1/4}$-type); the conjecturally optimal rate for smooth test functions is $O(n^{-1+\varepsilon})$ up to the CLT fluctuation.
- Develop a **rigidity theory** for Ginibre eigenvalues comparable to the Hermitian case, controlling $|\lambda_k - \gamma_k|$ against classical locations in the disc.

## 9. Key References

- **[Foundational]** J. Ginibre. *Statistical Ensembles of Complex, Quaternion, and Real Matrices.* Journal of Mathematical Physics **6** (1965), 440–449.
- **[Foundational]** M. L. Mehta. *Random Matrices.* Academic Press, 1967; 3rd ed., Elsevier, 2004.
- **[Foundational]** V. L. Girko. *Circular Law.* Theory of Probability and Its Applications **29** (1984), 694–706.
- **[Foundational]** Z. D. Bai. *Circular Law.* Annals of Probability **25** (1997), 494–529.
- **[SOTA]** T. Tao, V. Vu (with an appendix by M. Krishnapur). *Random matrices: Universality of ESDs and the circular law.* Annals of Probability **38** (2010), 2023–2065.
- **[SOTA]** F. Götze, A. Tikhomirov. *The circular law for random matrices.* Annals of Probability **38** (2010), 1444–1491.
- **[SOTA]** M. Rudelson, R. Vershynin. *The Littlewood–Offord problem and invertibility of random matrices.* Advances in Mathematics **218** (2008), 600–633.
- **[SOTA]** P. Bourgade, H.-T. Yau, J. Yin. *Local circular law for random matrices.* Probability Theory and Related Fields **159** (2014), 545–595.
- **[SOTA]** T. Tao, V. Vu. *Random matrices: Universality of local spectral statistics of non-Hermitian matrices.* Annals of Probability **43** (2015), 782–874.
- **[SOTA]** J. Alt, L. Erdős, T. Krüger. *Local inhomogeneous circular law.* Annals of Applied Probability **28** (2018), 148–203.
- **[SOTA]** G. Cipolloni, L. Erdős, D. Schröder. *Edge universality for non-Hermitian random matrices.* Probability Theory and Related Fields **179** (2021), 1–28.
- **[SOTA]** G. Cipolloni, L. Erdős, D. Schröder. *Central limit theorem for linear eigenvalue statistics of non-Hermitian random matrices.* Communications on Pure and Applied Mathematics **76** (2023), 946–1034.
- **[SOTA]** M. Rudelson, K. Tikhomirov. *The sparse circular law under minimal assumptions.* Geometric and Functional Analysis **29** (2019), 561–637.
- **[SOTA]** N. Cook. *The circular law for random regular digraphs.* Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **55** (2019), 2111–2167.
- **[Survey]** C. Bordenave, D. Chafaï. *Around the circular law.* Probability Surveys **9** (2012), 1–89.
- **[Related]** A. Edelman, E. Kostlan, M. Shub. *How many eigenvalues of a random matrix are real?* Journal of the American Mathematical Society **7** (1994), 247–267.
- **[Related]** B. Rider. *A limit theorem at the edge of a non-Hermitian random matrix ensemble.* Journal of Physics A **36** (2003), 3401–3409.
- **[Related]** B. Rider, B. Virág. *The noise in the circular law and the Gaussian free field.* International Mathematics Research Notices, 2007.
- **[Related]** A. Borodin, C. D. Sinclair. *The Ginibre ensemble of real random matrices and its scaling limits.* Communications in Mathematical Physics **291** (2009), 177–224.

## 10. Worked Example / Concrete Special Case

**Kostlan's theorem and a two-line proof of the circular law for $\mathrm{Gin}_{\mathbb{C}}(n)$.**

Let $M\sim\mathrm{Gin}_{\mathbb{C}}(n)$ with eigenvalues $z_1,\dots,z_n$ (unscaled). Kostlan (1992) observed that the joint density $p_n$ factorizes in modulus after symmetrization: the *unordered set of moduli* satisfies
$$\{|z_1|,\dots,|z_n|\} \;\stackrel{d}{=}\; \{R_1,\dots,R_n\},\qquad R_k^2 \sim \Gamma(k,1)\ \text{ independent},\ k=1,\dots,n.$$

*Sketch.* Write $\prod_{i<j}|z_i-z_j|^2 = |\det(z_i^{j-1})|^2$ and expand the determinant as a sum over permutations. Integrating over the angles $\theta_i=\arg z_i$ kills every cross-term by orthogonality of $e^{ik\theta}$ on $[0,2\pi)$, leaving
$$\int_{[0,2\pi)^n} \prod_{i<j}|z_i-z_j|^2 \,\frac{d\theta}{(2\pi)^n} \;=\; \frac{1}{n!}\sum_{\sigma\in S_n}\prod_{i} r_i^{2(\sigma(i)-1)}\cdot n! \;\;\Longrightarrow\;\; \text{permanent of } (r_i^{2(j-1)}),$$
which is exactly the symmetrized density of independent radii with $r_k^2\sim\Gamma(k,1)$ (normalizing constants $\prod_k (k-1)!$ match). $\square$

**Consequence.** Fix $t\in(0,1)$ and count eigenvalues of $n^{-1/2}M$ inside the disc $|z|\le t$, i.e. $|z_k|\le t\sqrt n$:
$$\mathbb{E}\,\mu_n(\{|z|\le t\}) \;=\; \frac1n\sum_{k=1}^n \mathbb{P}\big(\Gamma(k,1)\le t^2 n\big).$$
Since $\Gamma(k,1)$ concentrates at $k$ with fluctuation $\sqrt k = O(\sqrt n)$, the summand is $\approx 1$ for $k < t^2 n - C\sqrt n$ and $\approx 0$ for $k > t^2 n + C\sqrt n$. Hence
$$\mathbb{E}\,\mu_n(\{|z|\le t\}) \;=\; t^2 + O(n^{-1/2}).$$
And $t^2$ is precisely $\mu_{\mathrm{circ}}(\{|z|\le t\}) = \frac{1}{\pi}\cdot \pi t^2$. Independence of the radii plus a Borel–Cantelli argument upgrades this to almost-sure convergence, and rotational invariance of $\mathrm{Gin}_{\mathbb{C}}$ fixes the angular distribution as uniform. Together: $\mu_n\Rightarrow \mathrm{Unif}(\mathbb{D})$ a.s.

**Numerical check ($n=4$).** $\mathbb{E}\mu_4(\{|z|\le \tfrac12\}) = \frac14\sum_{k=1}^4 \mathbb{P}(\Gamma(k,1)\le 1)$. With $\mathbb{P}(\Gamma(k,1)\le 1) = 1-e^{-1}\sum_{j<k}1/j!$: values $0.6321,\,0.2642,\,0.0803,\,0.0190$, giving $0.2489$ against the limit $t^2=0.25$ — agreement to $0.5\%$ already at $n=4$.

**What this example does not give.** The argument uses rotational invariance and the exact Gaussian density; both fail for general i.i.d. entries. That is precisely why the general circular law needs Hermitization and smallest-singular-value control (Sections 5–6).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*