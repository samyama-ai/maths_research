---
id: 09-probability/random-band-matrices-universality
title: "Random Band Matrices Universality"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Band Matrices Universality

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-band-matrices-universality` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $H = H^{(N,W)}$ be an $N \times N$ Hermitian random matrix whose entries $H_{ij}$ are independent (up to symmetry), centered, and vanish unless $|i-j| \le W$ in a periodic distance on $\mathbb{Z}/N\mathbb{Z}$. The **band matrix conjecture** asserts a sharp phase transition at bandwidth $W \sim \sqrt{N}$:

- **Delocalized phase.** If $W \gg N^{1/2}$, the local eigenvalue statistics in the bulk of the spectrum converge to those of the Gaussian Orthogonal/Unitary Ensemble (GOE/GUE) — sine-kernel correlations — and every bulk eigenvector $\psi$ is completely delocalized: $\|\psi\|_\infty^2 \le N^{-1+\varepsilon}$ with high probability.
- **Localized phase.** If $W \ll N^{1/2}$, bulk eigenvalues follow a Poisson point process after rescaling, and bulk eigenvectors are exponentially localized on a scale $\ell \sim W^2$.

A complete resolution requires proving both statements for the full range of $W$ on each side of the threshold, for a general class of entry distributions (e.g. all i.i.d.-profile entries with finite high moments), not merely for Gaussian or block-structured models. The conjecture is the cleanest finite-dimensional avatar of the **Anderson metal–insulator transition**, and in dimension $d = 1$ it is the only known model where a transition is predicted to occur *within* a one-parameter family of mean-field-like operators.

## 2. Mathematical Foundations

**Model.** Fix $N, W$ with $1 \ll W \ll N$. Let $f: \mathbb{R} \to [0,\infty)$ be a symmetric profile with $\sum_{j} f(j/W)/W = 1$, and set the variance profile
$$ s_{ij} = \mathbb{E}|H_{ij}|^2 = \frac{1}{W} f\!\left(\frac{[i-j]_N}{W}\right), \qquad [i-j]_N = \min_{k \in \mathbb{Z}} |i-j+kN|. $$
The simplest case is the flat band $s_{ij} = (2W+1)^{-1} \mathbf{1}\{[i-j]_N \le W\}$. The matrix $S = (s_{ij})$ is doubly stochastic, so the empirical spectral measure converges to the semicircle law
$$ \varrho_{sc}(E) = \frac{1}{2\pi}\sqrt{(4-E^2)_+}, $$
independently of $W$. The transition is therefore invisible at the global scale and lives entirely at the scale of the mean eigenvalue spacing $\Delta \sim N^{-1}$.

**Higher dimensions.** On $\Lambda = (\mathbb{Z}/L\mathbb{Z})^d$ with $N = L^d$, indices are lattice sites and $s_{xy} \asymp W^{-d}\mathbf{1}\{\|x-y\| \le W\}$. The conjectured behaviour is: $d=1$, $\ell \sim W^2$; $d=2$, $\ell \sim e^{cW^2}$ (localization for all $W$ on exponentially large volumes); $d\ge 3$, delocalization for $W \ge W_0(d)$ regardless of $L$.

**Resolvent and self-consistent equations.** With $G(z) = (H-z)^{-1}$, $z = E + \mathrm{i}\eta$, the self-consistent (Dyson/Wigner) equation for the diagonal reads
$$ \frac{1}{G_{ii}} = -z - \sum_j s_{ij} G_{jj} + \mathcal{E}_i, $$
and the fluctuation $\mathcal{E}_i$ is controlled by the resolvent of the **diffusion operator** $\Theta = (1 - m^2 S)^{-1}$, where $m(z) = \frac{1}{2}(-z + \sqrt{z^2-4})$ solves $m = (-z-m)^{-1}$. For $|m|^2 \approx 1$, $\Theta$ behaves as $(\eta + W^{-2}\Delta_{\text{lattice}})^{-1}$: quantum diffusion with diffusion constant $D \asymp W^2$.

**Thouless criterion.** The dimensionless conductance is
$$ g \;=\; \frac{E_{\mathrm{Th}}}{\Delta} \;\asymp\; \frac{D/N^2}{1/N} \;=\; \frac{W^2}{N} \quad (d=1), $$
so $g \gg 1 \iff W \gg \sqrt N$. This heuristic, due to Fyodorov and Mirlin (1991) via the nonlinear $\sigma$-model, is the source of the conjectured threshold.

**Universality target.** For $k \ge 1$ and a smooth compactly supported $O$,
$$ \int O(\alpha_1,\dots,\alpha_k)\Big[ \tfrac{1}{\varrho^k}p_N^{(k)} - \tfrac{1}{\varrho^k}p^{(k)}_{\mathrm{GUE}}\Big]\Big(E + \tfrac{\alpha}{N\varrho}\Big)\,\mathrm{d}\alpha \longrightarrow 0, $$
where $p_N^{(k)}$ is the $k$-point correlation function. **Quantum unique ergodicity (QUE)** is the companion eigenvector statement: for a bulk eigenvector $\psi$ and any set $I$ of size $|I| = \Theta(N)$, $\sum_{i \in I} |\psi_i|^2 \to |I|/N$.

## 3. History & State of the Art (SOTA)

- **1990–91.** Casati, Molinari, Izrailev and independently Fyodorov–Mirlin identify the scaling variable $W^2/N$ numerically and by supersymmetric $\sigma$-model arguments; Fyodorov–Mirlin predict $\ell \sim W^2$ and the $\sqrt N$ threshold.
- **2009.** Schenker proves localization with $\ell \lesssim W^8$, i.e. localization for $W \ll N^{1/8}$, by a fractional-moment/combinatorial expansion.
- **2010.** Sodin resolves the *edge* transition exactly: the largest eigenvalue obeys Tracy–Widom fluctuations iff $W \gg N^{5/6}$, and is Gaussian below.
- **2011–13.** Erdős–Knowles and Erdős–Knowles–Yau–Yin establish delocalization and a diffusion profile for $W \gg N^{4/5}$ (and $W \gg N^{6/7}$ in earlier versions), using the self-consistent equation plus a genuine control of $\Theta$.
- **2013–21.** Shcherbina–Shcherbina develop the rigorous supersymmetric transfer-matrix method for block band matrices with Gaussian entries, obtaining sine-kernel universality for $W \gg N^{6/7}$ and characteristic-polynomial results down to $W \gg N^{1/2}$.
- **2017–20.** Bourgade–Erdős–Yau–Yin and Bourgade–Yang–Yau–Yin prove bulk universality and QUE for $W \gg N^{3/4}$ — the mean-field regime reachable by Dyson-Brownian-motion (DBM) plus generalized resolvent estimates.
- **2021–24.** Yang–Yin and Yang–Yau–Yin develop the **$T$-expansion / self-energy renormalization** machinery, proving delocalization and quantum diffusion for $W \gg L^{\varepsilon}$ in dimensions $d \ge 7$–$8$, and later $d\ge 3$ under conditions.
- **2022–24.** Cipolloni–Peled–Schenker–Shapiro push dynamical localization up to $W \ll N^{1/4}$ in $d=1$.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $d=1$, $W \gg N^{3/4}$ | Bulk sine-kernel universality + QUE + full delocalization | Bourgade–Erdős–Yau–Yin (2017); Bourgade–Yang–Yau–Yin (2019–20) |
| $d=1$, $W \gg N^{4/5}$ | Delocalization with explicit diffusion profile for $\mathbb{E}|G_{xy}|^2$ | Erdős–Knowles–Yau–Yin (2013) |
| Gaussian block band, $W \gg N^{6/7}$ | Sine kernel via SUSY transfer matrices | Shcherbina–Shcherbina (2021) |
| Gaussian block band, $W \gg N^{1/2}$ | Universality of *second correlation function of characteristic polynomials* — the threshold is seen | Shcherbina–Shcherbina (2017) |
| Spectral edge, all $W$ | Sharp transition at $W = N^{5/6}$: Tracy–Widom above, Gaussian below | Sodin (2010) |
| $d=1$, $W \ll N^{1/4}$ | Dynamical (Anderson) localization, exponentially localized eigenvectors | Cipolloni–Peled–Schenker–Shapiro (2024) |
| $d \ge 7$, $W \ge L^{\varepsilon}$ | Delocalization + quantum diffusion for arbitrarily large $L$ | Yang–Yin (2021–22); Yang–Yau–Yin (2022) |
| $2 \times 2$ block / finite number of blocks | Complete local universality | Shcherbina (2013–14) |

## 5. Principal Obstacles

- **Loss of mean-field structure.** DBM-based universality needs an *a priori* input at spectral resolution $\eta \ll N^{-1}$, obtained from delocalization plus QUE. Existing resolvent expansions control $G$ only down to $\eta \gg W^{-1}N^{\varepsilon}\cdot(\text{power of } N/W^2)$, which degrades as $W$ decreases; below $W = N^{3/4}$ the error terms in the self-consistent equation are no longer summable.
- **Non-perturbative fluctuation counting.** The expansion of $\mathbb{E}\,G$ generates diagrams whose number grows factorially; each additional order gains a factor $\Theta(W^{-1})$ but costs a diffusive propagator of size $N/W^2$. At $W \sim \sqrt N$ these exactly balance — the perturbative series has zero radius of convergence at the transition. Renormalizing them (the $T$-expansion and self-energy resummation) works when the loop integral $\sum_{x}|\Theta_{0x}|^2$ converges, i.e. in high dimension, and diverges in $d=1,2$.
- **SUSY rigor barrier.** The supersymmetric transfer-matrix method reproduces the physics exactly but requires Gaussian entries and a block structure; the resulting operator is non-self-adjoint on a non-compact symmetric superspace, and controlling its spectral gap uniformly in $N$ has been achieved only in restricted regimes.
- **No monotonicity or comparison principle.** Unlike percolation or Ising, there is no stochastic ordering in $W$: one cannot deduce delocalization at $W'$ from delocalization at $W < W'$, so a soft "sharp threshold" argument is unavailable.
- **Localization side.** Fractional-moment and multi-scale methods need a large-disorder or weak-coupling smallness parameter; here the natural parameter is $1/W$ but the effective coupling across a distance $\ell$ is $\ell/W^2$, so getting from $\ell \sim W^{1/2}$-type bounds to the true $\ell \sim W^2$ requires resumming all scales below $W^2$ simultaneously.

## 6. The Gap

Proven: delocalization/universality for $W \ge N^{3/4+\varepsilon}$; localization for $W \le N^{1/4-\varepsilon}$. Conjectured threshold: $N^{1/2}$. The open window is
$$ N^{1/4} \;\ll\; W \;\ll\; N^{3/4}, $$
a full factor $N^{1/2}$ wide in bandwidth. The precise missing step on the delocalization side is an **a priori isotropic local law at the optimal scale** $\eta \gg N^{-1+\varepsilon}$ (equivalently, control of $\max_{x,y}|G_{xy}(E+\mathrm{i}\eta)|$ down to the eigenvalue spacing) for $W = N^{1/2+\varepsilon}$, without which the DBM step cannot be initialized. On the localized side, the missing step is an exponential decay estimate valid whenever the *renormalized* coupling $N/W^2$ is large, rather than whenever a bare fractional moment is small.

## 7. Current Research (as of June 2026)

- **Harvard / NYU / UCLA school (Yau, Bourgade, Yin, Yang, Dubova).** Extending the $T$-expansion to low dimension. Yang–Yau–Yin reduced the dimension requirement from $d \ge 8$ to $d \ge 7$ and then to $d \ge 3$ under a block assumption; a 2024–25 series treats $d = 2$ with $W \ge L^{\varepsilon}$ and, in $d=1$, claims delocalization down to $W \gg N^{1/2+\varepsilon}$ — *(frontier — verify)*.
- **Random block Schrödinger operators.** Dubova–Yang analyze $\lambda \Delta + V$ with random block potentials as a laboratory for the same expansion, isolating self-energy renormalization from band geometry.
- **SUSY side (Shcherbina, Shcherbina, Kharkiv/Rutgers).** Rigorous transfer-operator spectral analysis aiming at the $\sqrt N$ threshold for Gaussian blocks; results on characteristic polynomials already reach it.
- **Localization side (Schenker, Peled, Cipolloni, Shapiro).** Improving $W \ll N^{1/4}$ toward $N^{1/2}$ via fractional moments combined with Wegner-type estimates.
- **Non-Hermitian and Lévy analogues.** Band structure combined with heavy tails or complex Ginibre entries, where the transition threshold is expected to shift.

## 8. Future Work

- Prove the isotropic local law at scale $\eta = N^{-1+\varepsilon}$ for $W = N^{1/2+\varepsilon}$; this alone would close the delocalization half via the existing DBM + QUE machinery.
- Establish a **sharp-threshold** or monotonicity statement in $W$, converting any single point of the window into the full transition.
- Make the Fyodorov–Mirlin $\sigma$-model derivation rigorous beyond Gaussian block models — a functional-integral analogue of Ward identities that survives non-Gaussian entries.
- Determine the *critical* behaviour at $W \asymp \sqrt N$ itself: the predicted family of critical statistics interpolating between Poisson and sine kernel, parametrized by $\beta = \lim W^2/N$, is not proved in any regime.
- Settle $d = 2$: prove localization on volumes $L \gg e^{cW^2}$, which would confirm the two-dimensional marginality predicted by scaling theory.

## 9. Key References

- **[Foundational]** Y. V. Fyodorov, A. D. Mirlin. *Scaling properties of localization in random band matrices: a $\sigma$-model approach.* Physical Review Letters **67** (1991), 2405–2409.
- **[Foundational]** J. Schenker. *Eigenvector localization for random band matrices with power law band width.* Communications in Mathematical Physics **290** (2009), 1065–1097.
- **[Foundational]** S. Sodin. *The spectral edge of some random band matrices.* Annals of Mathematics **172** (2010), 2223–2251.
- **[Key]** L. Erdős, A. Knowles, H.-T. Yau, J. Yin. *Delocalization and diffusion profile for random band matrices.* Communications in Mathematical Physics **323** (2013), 367–416.
- **[Key]** P. Bourgade, L. Erdős, H.-T. Yau, J. Yin. *Universality for a class of random band matrices.* Advances in Theoretical and Mathematical Physics **21** (2017), 739–800.
- **[SOTA]** P. Bourgade, F. Yang, H.-T. Yau, J. Yin. *Random band matrices in the delocalized phase, II: Generalized resolvent estimates.* Journal of Statistical Physics **174** (2019), 1189–1221.
- **[SOTA]** P. Bourgade, H.-T. Yau, J. Yin. *Random band matrices in the delocalized phase I: Quantum unique ergodicity and universality.* Communications on Pure and Applied Mathematics **73** (2020), 1526–1596.
- **[SOTA]** M. Shcherbina, T. Shcherbina. *Universality for 1d random band matrices.* Communications in Mathematical Physics **385** (2021), 667–716.
- **[SOTA]** F. Yang, J. Yin. *Delocalization and quantum diffusion of random band matrices in high dimensions I: Self-energy renormalization.* Preprint, arXiv:2104.12048 (2021).
- **[SOTA]** F. Yang, H.-T. Yau, J. Yin. *Delocalization and quantum diffusion of random band matrices in high dimensions II: $T$-expansion.* Communications in Mathematical Physics **396** (2022), 527–622.
- **[SOTA]** G. Cipolloni, R. Peled, J. Schenker, J. Shapiro. *Dynamical localization for random band matrices up to $W \ll N^{1/4}$.* Communications in Mathematical Physics **405** (2024), article 82.
- **[Survey]** P. Bourgade. *Random band matrices.* Proceedings of the International Congress of Mathematicians (Rio de Janeiro, 2018), Vol. IV, 2759–2784.
- **[Survey]** L. Erdős, H.-T. Yau. *A Dynamical Approach to Random Matrix Theory.* Courant Lecture Notes **28**, AMS, 2017.

## 10. Worked Example / Concrete Special Case

**Thouless-criterion computation in $d = 1$.** Take the flat band with $N = 10^6$ and $W = 10^3$, so $W = N^{1/2}$ exactly at the conjectured threshold.

1. *Mean spacing.* The bulk density is $\varrho_{sc}(0) = 1/\pi$, so consecutive eigenvalues near $E = 0$ are separated by $\Delta \approx \pi/N = 3.14 \times 10^{-6}$.
2. *Diffusion constant.* Write $H = W^{-1/2}\tilde H$ with the band profile flat on $|i-j| \le W$. The variance matrix $S$ acts on Fourier modes $e_p(j) = N^{-1/2}e^{2\pi \mathrm{i} p j/N}$ with eigenvalue
$$ \hat s(p) = \frac{1}{2W+1}\sum_{|k|\le W} e^{2\pi \mathrm{i} pk/N} = 1 - \frac{(2\pi p W/N)^2}{6} + O\!\left((pW/N)^4\right). $$
Hence at $z = \mathrm{i}\eta$, $E=0$, where $m = -\mathrm{i}$ and $m^2 = -1$: the diffusion operator is
$$ \Theta(p) = \frac{1}{1 - \hat s(p)\,|m|^2 \, e^{\ldots}} \;\approx\; \frac{1}{\eta + D\,(2\pi p/N)^2}, \qquad D \asymp W^2/3. $$
3. *Thouless energy.* The slowest mode is $p = 1$, giving $E_{\mathrm{Th}} \asymp D (2\pi/N)^2 \asymp W^2/N^2$. With the numbers above, $E_{\mathrm{Th}} \approx 4\pi^2 \cdot 10^6/(3 \cdot 10^{12}) \approx 1.3\times10^{-5}$.
4. *Conductance.* $g = E_{\mathrm{Th}}/\Delta \approx 1.3\times 10^{-5}/3.14\times10^{-6} \approx 4.2$ — an $O(1)$ number. This is the content of the threshold: at $W = \sqrt N$ neither $g \to \infty$ (metal) nor $g \to 0$ (insulator) holds. Doubling to $W = 2\times10^3$ ($=2N^{1/2}$) gives $g \approx 17$; halving to $W = 5\times 10^2$ gives $g \approx 1.05$. Only $W = N^{1/2+\delta}$ makes $g \to \infty$ as $N \to \infty$.
5. *Localization length.* On the insulator side, first-order perturbation theory for a site-$i$ eigenvector gives amplitude $\sim s_{ij}/\Delta_{\text{local}}$ per hop, where the local spacing inside a window of length $\ell$ is $\ell^{-1}$; the resulting recursion is stable precisely when $\ell \lesssim W^2$, reproducing $\ell \sim W^2$.

Contrast with the two extremes: $W = N$ recovers a Wigner matrix ($g \asymp N$, GUE statistics, proven), and $W = O(1)$ is a one-dimensional Anderson model ($g \to 0$, Poisson statistics, proven). The conjecture asserts that the crossover between these two proven endpoints occurs at a single sharp point, $W = \sqrt N$, and the open problem is everything strictly between $N^{1/4}$ and $N^{3/4}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*