---
id: 09-probability/anderson-localization-for-random-band-matrices
title: "Anderson Localization for Random Band Matrices"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Anderson Localization for Random Band Matrices

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/anderson-localization-for-random-band-matrices` · **Status:** open

## 1. Problem Statement / Conjecture

Let $H = H^{(N,W)}$ be an $N \times N$ Hermitian random matrix whose entries are independent up to symmetry, centered, and supported on a band of width $W$: $\mathbb{E}|H_{ij}|^2 = 0$ whenever $|i-j| > W$ (indices on $\mathbb{Z}_N$). The **Fyodorov–Mirlin conjecture** asserts a sharp phase transition in one dimension at $W \asymp \sqrt{N}$:

- **Localized phase.** If $W \ll N^{1/2}$, then for eigenvalues in the bulk of the spectrum, eigenvectors are exponentially localized on a scale $\ell \asymp W^2$, and the local eigenvalue statistics converge to a Poisson point process.
- **Delocalized phase.** If $W \gg N^{1/2}$, then bulk eigenvectors are completely delocalized ($\|\mathbf{u}\|_\infty^2 = N^{-1+o(1)}$, indeed quantum-ergodic), and the local statistics converge to those of the GUE/GOE sine kernel.

In $d$ dimensions (indices in $\Lambda_L = [1,L]^d \cap \mathbb{Z}^d$, $N = L^d$), the conjectured thresholds are $W \asymp (\log L)^{1/2}$ for $d = 2$ and $W \asymp W_0$ for a dimension-dependent constant $W_0$ when $d \ge 3$.

**What a solution requires.** A complete resolution must (i) prove exponential localization plus Poisson statistics for all $W \le N^{1/2 - \varepsilon}$ in $d=1$, (ii) prove delocalization plus sine-kernel universality for all $W \ge N^{1/2+\varepsilon}$, and ideally (iii) describe the critical window $W \asymp \sqrt{N}$, where the eigenvalue process is conjectured to be a nontrivial one-parameter family interpolating between Poisson and sine.

**Status:** open. Both sides are proven only under strictly stronger constraints on $W$; the localization side is the far weaker one.

## 2. Mathematical Foundations

**The model.** Fix a variance profile $S = (s_{ij})$ with $s_{ij} = \mathbb{E}|H_{ij}|^2$, $\sum_j s_{ij} = 1$, and
$$
s_{ij} \;=\; \frac{1}{\mathcal{Z}}\, f\!\left(\frac{[i-j]_N}{W}\right), \qquad f \ge 0 \text{ compactly supported or fast-decaying},
$$
where $[\cdot]_N$ is the representative in $(-N/2, N/2]$. Two standard cases: $f = \mathbf{1}_{[-1,1]}$ (sharp band, $s_{ij} = (2W+1)^{-1}\mathbf{1}_{|i-j|\le W}$) and $f(x) = e^{-x^2/2}$ (Gaussian profile). Entries are typically Gaussian or satisfy uniform sub-exponential moment bounds.

**Global law.** For $1 \ll W \le N$ the empirical spectral measure converges to the semicircle law $\rho_{sc}(E) = \frac{1}{2\pi}\sqrt{(4-E^2)_+}$, independently of $W$ — the transition is invisible at the macroscopic scale.

**Localization/delocalization observables.**
- Eigenvector localization length via inverse participation ratio: for a normalized eigenvector $\mathbf{u}$, $\mathrm{IPR}(\mathbf{u}) = \sum_{i} |u_i|^4$. Delocalization $\Leftrightarrow \mathrm{IPR} \approx N^{-1}$; localization on scale $\ell$ $\Leftrightarrow \mathrm{IPR} \approx \ell^{-1}$.
- **Dynamical localization:** existence of $C, \mu > 0$ with
$$
\mathbb{E}\sup_{t \in \mathbb{R}} \left| \big( e^{-itH} \big)_{ij} \right| \;\le\; C\, e^{-|i-j|/\mu}, \qquad \mu \asymp W^2 .
$$
- **Quantum unique ergodicity (QUE):** for any deterministic $\mathbf{a}$ with $\sum_i a_i = 0$, $\|\mathbf{a}\|_\infty \le 1$, $\sum_i a_i N|u_i|^2 \to 0$ in probability.

**Resolvent and self-consistent equation.** With $G(z) = (H-z)^{-1}$, $z = E + i\eta$, the self-consistent (Wegner/Vector Dyson) equation is
$$
\frac{1}{m_i(z)} \;=\; -z - \sum_j s_{ij} m_j(z), \qquad m_i \approx m_{sc}(z) = \frac{-z + \sqrt{z^2-4}}{2}.
$$
Fluctuations of $|G_{ij}|^2$ are governed by the **diffusion kernel**: with $S$ the variance matrix and $|m|^2 < 1$,
$$
\mathbb{E}|G_{ij}(E+i\eta)|^2 \;\approx\; \frac{1}{N\eta}\Big[ \frac{1}{1 - |m|^2 S} \Big]_{ij}, \qquad \big(1-|m|^2S\big)^{-1} \sim \big(\eta + D(-\Delta)\big)^{-1},
$$
i.e. a lattice diffusion with constant $D \asymp W^2$. This is the quantitative source of $\ell \asymp W^2$.

**Thouless criterion.** Mean level spacing in the bulk is $\Delta \asymp N^{-1}$. The Thouless energy for diffusion with constant $D \asymp W^2$ on a ring of length $N$ is $E_{\rm Th} \asymp D/N^2 = W^2/N^2$. The dimensionless conductance is
$$
g \;=\; \frac{E_{\rm Th}}{\Delta} \;\asymp\; \frac{W^2}{N},
$$
so $g \gg 1 \iff W \gg \sqrt N$. This is the heuristic that fixes the conjectured threshold.

**Supersymmetric $\sigma$-model.** For Gaussian entries the averaged product of resolvents can be written exactly as a superintegral; in the limit $W \to \infty$ it is expected to reduce to a nonlinear $\sigma$-model on the supermanifold $\mathrm{U}(1,1|2)/(\mathrm{U}(1|1)\times \mathrm{U}(1|1))$ with coupling $\beta \asymp W^2$, whose 1D transfer-operator analysis (Efetov) predicts $\ell \asymp W^2$ and the Poisson–sine crossover at $\ell \asymp N$.

## 3. History & State of the Art (SOTA)

- **1958.** Anderson introduces localization for the random Schrödinger operator on $\mathbb{Z}^d$.
- **1979.** Wegner proposes the **orbital model**: $W$ orbitals per site on $\mathbb{Z}^d$, the natural block version of the band matrix, as a $1/W$-expandable proxy for Anderson localization.
- **1990.** Casati, Molinari and Izrailev give numerics showing that spectral statistics of 1D band matrices depend only on the scaling variable $W^2/N$.
- **1991.** Fyodorov and Mirlin derive, via the supersymmetric $\sigma$-model, $\ell \asymp W^2$ and the sharp transition at $W \asymp \sqrt N$ — the conjecture as stated above.
- **2009–2019 (localization side).** Schenker proves localization for $W \ll N^{1/8}$; Peled–Schenker–Shamis–Sodin treat the Wegner orbital model; Cipolloni–Peled–Schenker–Shapiro push dynamical localization to $W \ll N^{1/4}$.
- **2010–2020 (delocalization side).** Sodin identifies the edge transition at $W \asymp N^{5/6}$ (Tracy–Widom above, Poisson-like below). Erdős–Knowles–Yau–Yin obtain delocalization and quantum diffusion for $W \gg N^{4/5}$; Bao–Erdős reach $W\gg N^{6/7}$ for block models; Bourgade–Erdős–Yau–Yin and Bourgade–Yau–Yin establish QUE and full sine-kernel universality for $W \gg N^{3/4}$ via mean-field reduction.
- **2021–2025.** Yang–Yau–Yin prove delocalization and quantum diffusion in high dimensions $d \ge 7$ for $W \ge L^{\varepsilon}$; Dubova–Yang–Yau–Yin announce delocalization in 1D for $W \gg N^{1/2}$, matching the conjectured threshold on the delocalized side *(frontier — verify)*.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $d=1$, $W \ll N^{1/8}$ | Exponential eigenvector localization, $\ell \lesssim W^8$ | Schenker (2009) |
| $d=1$, $W \ll N^{1/4}$ | Dynamical localization, uniform in $t$ | Cipolloni–Peled–Schenker–Shapiro (2024) |
| Wegner orbital model, $d=1$, $W$ large fixed, $N\to\infty$ | Localization at all energies for the block model with Gaussian orbitals | Peled–Schenker–Shamis–Sodin (2019) |
| $d=1$, $W \gg N^{4/5}$ | Delocalization, quantum diffusion profile | Erdős–Knowles–Yau–Yin (2013) |
| Block band, $W \gg N^{6/7}$ | Delocalization | Bao–Erdős (2017) |
| $d=1$ block model, $W \gg N^{3/4}$ | QUE + bulk sine-kernel universality | Bourgade–Yau–Yin (2020) |
| Spectral edge, $W \gg N^{5/6}$ | Tracy–Widom fluctuations; below, non-TW | Sodin (2010) |
| $d \ge 7$, $W \ge L^{\varepsilon}$ | Delocalization + quantum diffusion for all bulk energies | Yang–Yau–Yin (2021–2024) |
| Characteristic polynomials, special 1D block models | Second-moment transition confirmed at $W \asymp N^{1/2}$ | M. Shcherbina–T. Shcherbina (2017) |
| $W = O(1)$, $N \to \infty$ | Localization (reduces to 1D Anderson/Wegner with fixed-size blocks) | Classical (Kunz–Souillard, Goldsheid–Molchanov–Pastur) |
| $d=1$, $W \gg N^{1/2}$ | Delocalization at the conjectured threshold *(frontier — verify)* | Dubova–Yang–Yau–Yin (2025 preprint) |

## 5. Principal Obstacles

- **Moment/expansion methods stall well below $\sqrt N$.** The localization proofs use fractional-moment or Green-function-expansion bounds in which the small parameter is a power of $W/N^{a}$ with $a$ dictated by the number of resolvent entries that can be decoupled. Each new "path" in the expansion costs a factor of $W$, and combinatorial control degrades polynomially; nothing in the current framework converts $\ell \asymp W^2$ into a proof for $W$ near $N^{1/2}$.
- **No transfer-matrix structure.** For $W=1$ (Jacobi matrices) the Furstenberg theory of products of random $2\times 2$ matrices gives positive Lyapunov exponents. For $W>1$ the transfer matrices are $2W\times 2W$ symplectic, and the relevant Lyapunov exponent is the *smallest positive* one, of size $\asymp W^{-2}$; separating $W$ exponents that are nearly degenerate uniformly in $N$ is beyond current Furstenberg-type results.
- **Multi-scale analysis loses the $W$-dependence.** Fröhlich–Spencer multi-scale analysis and Aizenman–Molchanov fractional moments require an initial-scale estimate whose smallness is exponential in the disorder; band matrices have effective disorder $\asymp W^{-1}$ at the relevant scale, so the induction only starts after a scale $\gg \ell$, which the finite matrix does not provide.
- **The SUSY $\sigma$-model is not a theorem.** The reduction from the exact superintegral to the $\sigma$-model requires a saddle-point analysis on a non-compact supermanifold with a non-positive integrand; it is rigorous only for special block models and for observables (characteristic polynomials, second mixed moments) where the Grassmann sector is controlled. Extending it to $\mathbb{E}|G_{ij}|^2$ — the observable that actually detects localization — is open.
- **Delocalization proofs are perturbative in $\eta$.** Green-function comparison and mean-field reduction control spectral scales $\eta \gg W^{-1}$ or $\eta \gg N^{-1}\cdot(\text{corrections})$; reaching the eigenvalue scale $\eta \asymp N^{-1}$ requires summing an infinite family of diffusive loop corrections whose combinatorics blow up when $g = W^2/N$ is only slightly larger than $1$.

## 6. The Gap

On the delocalization side, the gap has narrowed from $N^{4/5}$ through $N^{3/4}$ to (claimed) $N^{1/2+\varepsilon}$; what remains is the critical window itself and the removal of block/Gaussian structure assumptions.

On the localization side, the gap is a genuine polynomial chasm: proven up to $W \ll N^{1/4}$, conjectured up to $W \ll N^{1/2}$. The missing step is a **non-perturbative lower bound on the smallest positive Lyapunov exponent of the band transfer matrix**, or equivalently a rigorous derivation of the $\sigma$-model transfer operator with spectral gap $\asymp W^{-2}$ for the $|G|^2$ observable. Every existing localization argument produces a localization length bound of the form $\ell \lesssim W^{c}$ with $c > 2$ ($c = 8$ in Schenker; $c=4$ effectively in the $N^{1/4}$ result) — and $c > 2$ is exactly what forces the artificial threshold $N^{2/c}$.

## 7. Current Research (as of June 2026)

- **Harvard / NYU / Courant (Yau, Yin, Bourgade, and collaborators).** Loop-hierarchy and $T$-expansion methods for the diffusive regime; the 1D result at $W \gg N^{1/2}$ and its extension to non-Gaussian entries and general $d$ *(frontier — verify)*.
- **Cipolloni, Peled, Schenker, Shapiro and coauthors.** Fractional-moment and Wegner-orbital techniques on the localization side; efforts to reach $W \ll N^{1/3}$ or $N^{1/2}$ by resumming self-energy corrections *(frontier — verify)*.
- **Shcherbina school (Kyiv/Vienna).** Rigorous SUSY: transfer-operator spectral analysis for block band matrices, extending from characteristic polynomials to genuine correlation functions.
- **Critical-window statistics.** Numerical and heuristic work on the conjectured one-parameter family of limiting point processes at $W = c\sqrt{N}$, and its relation to the critical statistics of the Anderson model at the mobility edge.
- **Non-Hermitian and structured analogues.** Band versions of the elliptic and i.i.d. ensembles, where localization/delocalization is being studied with the same loop-expansion toolkit.

## 8. Future Work

1. **Prove $\ell \asymp W^2$ with the sharp exponent 2** for some class of band matrices at fixed $W$ and $N \to \infty$; this alone would push the localization threshold to $N^{1/2}$.
2. **Make the SUSY $\sigma$-model reduction rigorous for $\mathbb{E}|G_{ij}|^2$** in the 1D block model — widely viewed as the most likely route to the full conjecture.
3. **Identify the critical process** at $W = c\sqrt N$, expected to depend on $c$ and to interpolate between Poisson and sine.
4. **Remove block/Gaussian assumptions** from the $N^{3/4}$–$N^{1/2}$ delocalization results, obtaining universality for sharp-band matrices with general entry distributions.
5. **Lower dimensions $d=2,3$.** Push the high-dimensional ($d\ge7$) diffusion machinery down to $d=3$, and prove the $W \asymp \sqrt{\log L}$ threshold in $d=2$.

## 9. Key References

- **[Foundational]** P. W. Anderson. *Absence of Diffusion in Certain Random Lattices.* Physical Review **109** (1958), 1492–1505.
- **[Foundational]** F. Wegner. *Disordered system with $n$ orbitals per site: $n \to \infty$ limit.* Zeitschrift für Physik B **35** (1979), 207–210.
- **[Foundational]** Y. V. Fyodorov, A. D. Mirlin. *Scaling properties of localization in random band matrices: a $\sigma$-model approach.* Physical Review Letters **67** (1991), 2405–2409.
- **[Numerics]** G. Casati, L. Molinari, F. Izrailev. *Scaling properties of band random matrices.* Physical Review Letters **64** (1990), 1851–1854.
- **[Localization]** J. Schenker. *Eigenvector localization for random band matrices with power law band width.* Communications in Mathematical Physics **290** (2009), 1065–1097.
- **[Localization]** R. Peled, J. Schenker, M. Shamis, S. Sodin. *On the Wegner orbital model.* International Mathematics Research Notices **2019**(4), 1030–1058.
- **[SOTA / Localization]** G. Cipolloni, R. Peled, J. Schenker, J. Shapiro. *Dynamical Localization for Random Band Matrices up to $W \ll N^{1/4}$.* Communications in Mathematical Physics **405** (2024), article 82.
- **[Delocalization]** S. Sodin. *The spectral edge of some random band matrices.* Annals of Mathematics **172** (2010), 2223–2251.
- **[Delocalization]** L. Erdős, A. Knowles, H.-T. Yau, J. Yin. *Delocalization and diffusion profile for random band matrices.* Communications in Mathematical Physics **323** (2013), 367–416.
- **[Delocalization]** Z. Bao, L. Erdős. *Delocalization for a class of random block band matrices.* Probability Theory and Related Fields **167** (2017), 673–776.
- **[SOTA / Universality]** P. Bourgade, H.-T. Yau, J. Yin. *Random band matrices in the delocalized phase I: Quantum unique ergodicity and universality.* Communications on Pure and Applied Mathematics **73** (2020), 1526–1596.
- **[SOTA / High dimensions]** F. Yang, H.-T. Yau, J. Yin. *Delocalization and quantum diffusion of random band matrices in high dimensions.* (Parts I & II), Annals of Probability / arXiv preprints, 2021–2024.
- **[SUSY]** M. Shcherbina, T. Shcherbina. *Characteristic polynomials for 1D random band matrices from the localization side.* Communications in Mathematical Physics **351** (2017), 1009–1044.
- **[Survey]** P. Bourgade. *Random band matrices.* Proceedings of the International Congress of Mathematicians (Rio de Janeiro, 2018), Vol. IV, 2759–2784.
- **[Survey / Book]** L. Erdős, H.-T. Yau. *A Dynamical Approach to Random Matrix Theory.* Courant Lecture Notes **28**, AMS, 2017.
- **[Book]** M. Aizenman, S. Warzel. *Random Operators: Disorder Effects on Quantum Spectra and Dynamics.* Graduate Studies in Mathematics **168**, AMS, 2015.

## 10. Worked Example / Concrete Special Case

**Setup.** Take the sharp 1D band model with $N = 10^6$ and two choices of $W$: $W_- = 100$ and $W_+ = 10^4$. Entries $H_{ij}$, $|i-j| \le W$, are i.i.d. real Gaussians with variance $(2W+1)^{-1}$.

**Step 1 — diffusion constant.** The variance matrix $S$ acts as a convolution; its symbol is
$$
\hat S(p) = \frac{1}{2W+1}\sum_{|k|\le W} e^{ipk} \;=\; 1 - \frac{W(W+1)}{6}p^2 + O(p^4 W^4).
$$
So $1 - \hat S(p) \approx D p^2$ with $D = W(W+1)/6 \asymp W^2/6$. This is the rigorous origin of the $W^2$ scaling.

**Step 2 — Thouless conductance.** Bulk level spacing $\Delta \asymp N^{-1}$; Thouless energy on the ring $\mathbb{Z}_N$ uses the smallest nonzero momentum $p_1 = 2\pi/N$, giving $E_{\rm Th} = D p_1^2 \asymp W^2/N^2$. Hence
$$
g \;=\; \frac{E_{\rm Th}}{\Delta} \;\asymp\; \frac{W^2}{N}.
$$
- $W_- = 100$: $g \approx 10^4/10^6 = 10^{-2} \ll 1$. Localized. Predicted localization length $\ell \asymp W^2 = 10^4 \ll N$; each bulk eigenvector lives on about $10^4$ of the $10^6$ coordinates, $\mathrm{IPR} \approx 10^{-4}$, and adjacent eigenvalues are asymptotically independent (Poisson).
- $W_+ = 10^4$: $g \approx 10^8/10^6 = 10^{2} \gg 1$. Delocalized. Predicted $\mathrm{IPR} \approx N^{-1} = 10^{-6}$, GOE sine-kernel gap statistics.
- Critical: $g \asymp 1 \iff W = \sqrt N = 10^3$.

**Step 3 — what is actually proven for these two numbers.** With $N = 10^6$: the localization theorems require $W \ll N^{1/4} = 31.6$, so $W_- = 100$ is **not** covered — the localized prediction here is conjectural. The classical delocalization theorems require $W \gg N^{3/4} = 31623$, so $W_+ = 10^4$ is also **not** covered by Bourgade–Yau–Yin; it falls inside the newly claimed $W \gg N^{1/2}$ regime *(frontier — verify)*. The example makes the gap concrete: the conjecture separates the plane at $W = N^{1/2}$, while the theorems leave the entire strip $N^{1/4} \ll W \ll N^{1/2}$ untouched.

**Step 4 — the one case that is fully rigorous.** Set $W = 1$, so $H$ is a random real Jacobi (tridiagonal) matrix. Transfer matrices
$$
T_n(E) = \begin{pmatrix} E - H_{nn} & -H_{n,n-1} \\ H_{n,n-1}^{-1} & 0 \end{pmatrix}
$$
are i.i.d. in $\mathrm{SL}_2$-type form; Furstenberg's theorem gives a strictly positive Lyapunov exponent $\gamma(E) > 0$ for every $E$, and the Kotani/Ishii correspondence plus Aizenman–Molchanov fractional moments yield exponential localization with $\ell = 1/\gamma(E) = O(1)$, consistent with $\ell \asymp W^2 = 1$. The whole difficulty of the conjecture is that this $2\times2$ argument has no known analogue when the transfer matrix becomes $2W \times 2W$ and the relevant exponent shrinks like $W^{-2}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*