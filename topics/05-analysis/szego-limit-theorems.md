---
id: 05-analysis/szego-limit-theorems
title: "Szego Limit Theorems"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Szegő Limit Theorems

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/szego-limit-theorems` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $a$ be a function on the unit circle $\mathbb{T}$ with Fourier coefficients $\hat a_k = \frac{1}{2\pi}\int_{-\pi}^{\pi} a(e^{i\theta})e^{-ik\theta}\,d\theta$, and let
$$D_n(a) = \det\big(\hat a_{j-k}\big)_{j,k=0}^{n-1}$$
be the $n\times n$ Toeplitz determinant. The **Szegő limit problem** asks for the complete asymptotic expansion of $D_n(a)$ as $n\to\infty$, together with the sharp regularity hypotheses on $a$ under which each term is valid.

Three linked questions are open in different regimes:

1. **Sharp-class problem (1D).** For which symbol classes does the strong Szegő expansion $D_n(a)\sim G(a)^n E(a)$ hold, and what replaces $E(a)$ when the symbol leaves that class (zeros, jumps, root-type singularities, unbounded symbols)?
2. **Uniformity / transition problem.** Give asymptotics of $D_n(a)$ that are uniform as Fisher–Hartwig singularities merge, as their parameters degenerate, or as $n$ and the symbol scale together — the regime governed by Painlevé transcendents.
3. **Higher-dimensional problem (Widom's conjecture and beyond).** For a truncated pseudodifferential operator with discontinuous symbol on $\mathbb{R}^d$, $d\ge 2$, determine the full asymptotics of $\operatorname{Tr} h(\text{op})$ beyond the leading two terms, and for test functions $h$ of low regularity.

A complete resolution means: necessary and sufficient conditions on $a$ (resp. on the domain, symbol, and $h$) for each asymptotic form, with explicit constants and error terms.

## 2. Mathematical Foundations

**First (weak) Szegő theorem.** If $a\ge 0$, $a\in L^1(\mathbb{T})$, $\log a\in L^1(\mathbb{T})$, then
$$\lim_{n\to\infty}\frac{D_n(a)}{D_{n-1}(a)} = \lim_{n\to\infty} D_n(a)^{1/n} = G(a) := \exp\Big(\frac{1}{2\pi}\int_{-\pi}^{\pi}\log a(e^{i\theta})\,d\theta\Big) = e^{(\log a)_0}.$$
If $\log a\notin L^1$, the limit is $0$. Equivalently, $\inf_{p}\frac{1}{2\pi}\int|1-p|^2 a\,d\theta = G(a)$, the infimum over polynomials $p$ with $p(0)=0$ (prediction-theoretic form).

**Strong Szegő theorem.** Write $\log a(e^{i\theta}) = \sum_{k\in\mathbb{Z}} (\log a)_k e^{ik\theta}$. If $a$ is nonvanishing with winding number $0$ and
$$\|\log a\|_{B^{1/2}_2}^2 := \sum_{k\in\mathbb{Z}} |k|\,|(\log a)_k|^2 < \infty \quad (\text{plus } \log a\in L^\infty \text{ or } L^1),$$
then
$$\lim_{n\to\infty}\frac{D_n(a)}{G(a)^n} = E(a) = \exp\Big(\sum_{k=1}^{\infty} k\,(\log a)_k (\log a)_{-k}\Big).$$
The relevant symbol algebra is the **Krein algebra** $K = W\cap B^{1/2}_2$ ($W$ = Wiener algebra); $B^{1/2}_2 = H^{1/2}(\mathbb{T})$ is the critical Sobolev space for which the Hilbert–Schmidt condition on Hankel operators holds.

**Operator form.** With $T(a)$ the Toeplitz operator and $H(a)$, $H(\tilde a)$ Hankel operators, the Szegő–Widom identity gives $E(a)=\det\big(T(a)T(a^{-1})\big)$, a well-defined Fredholm determinant precisely when $H(a)H(\tilde a^{-1})$ is trace class, i.e. $\log a\in H^{1/2}$.

**Borodin–Okounkov / Geronimo–Case formula.** For $a=a_+a_-$ with $a_\pm$ analytic and nonvanishing in $|z|^{\pm1}\le 1$,
$$\frac{D_n(a)}{G(a)^n E(a)} = \det\big(I - K_n\big),\qquad K_n = P_n H(b)H(\tilde c)P_n,\ b=a_-a_+^{-1},\ c=a_+a_-^{-1},$$
an exact identity giving exponentially small corrections for analytic symbols.

**Fisher–Hartwig symbols.** Let
$$a(e^{i\theta}) = e^{V(\theta)} \prod_{j=1}^{m} |e^{i\theta}-e^{i\theta_j}|^{2\alpha_j}\, e^{i\beta_j \,\arg\!\big(-e^{i(\theta-\theta_j)}\big)},\qquad \Re\alpha_j>-\tfrac12,\ \beta_j\in\mathbb{C}.$$
The **Fisher–Hartwig conjecture** (1968) predicts
$$D_n(a) \sim e^{nV_0}\, n^{\sum_j(\alpha_j^2-\beta_j^2)}\, E\big(e^{V}\big)\prod_j \frac{G(1+\alpha_j+\beta_j)G(1+\alpha_j-\beta_j)}{G(1+2\alpha_j)}\ \cdot\ (\text{pair terms}),$$
where $G$ is the Barnes $G$-function and the pair terms are explicit powers of $|e^{i\theta_j}-e^{i\theta_k}|$. Distinct FH representations of the same symbol (shifting $\beta_j\mapsto\beta_j+n_j$, $\sum n_j=0$) must be summed — the **generalized FH conjecture** of Basor–Tracy.

**Higher dimensions (Widom's conjecture).** For $\Lambda,\Gamma\subset\mathbb{R}^d$ with piecewise-$C^1$ boundaries, symbol $a$, and $A_\alpha=\chi_\Lambda \,\mathrm{Op}_\alpha(a\chi_\Gamma)\,\chi_\Lambda$ with scaling $\alpha\to\infty$,
$$\operatorname{Tr} h(A_\alpha) = \alpha^d \mathcal{W}_0(h) + \alpha^{d-1}\log\alpha\ \mathcal{W}_1(h) + o(\alpha^{d-1}\log\alpha),$$
$$\mathcal{W}_1(h)=\frac{1}{(2\pi)^{d-1}}\frac{1}{4\pi^2}\int_{\partial\Lambda}\int_{\partial\Gamma}\mathcal{U}\big(h;a(x,\xi)\big)\,|n_x\cdot n_\xi|\,dS_\xi\,dS_x,\quad \mathcal{U}(h;b)=\int_0^1\frac{h(bs)-s\,h(b)}{s(1-s)}\,ds.$$
For $d=1$ this reduces to the $\log n$ correction of the Kac–Akhiezer/Widom formula, the continuous analogue of Szegő's theorems.

## 3. History & State of the Art (SOTA)

- **1915** — Szegő proves the first limit theorem for positive symbols (Math. Ann. 76).
- **1952** — Szegő proves the strong limit theorem for smooth positive symbols, motivated by Onsager's spontaneous magnetization formula for the 2D Ising model.
- **1954** — Kac gives a probabilistic proof; Baxter (1961) and Hirschman weaken hypotheses to $\log a\in W\cap B^{1/2}_2$.
- **1968** — Ibragimov establishes the sharp condition: for $a>0$ with $\log a\in L^1$, $D_n/G^n$ converges to a nonzero limit **iff** $\log a\in H^{1/2}$. This closes the 1D positive-symbol case.
- **1968** — Fisher and Hartwig conjecture the singular asymptotics.
- **1973–1976** — Widom proves the block/matrix-valued Szegő theorem ("Szegő–Widom"), where $E(a)=\det T(a)T(a^{-1})$ is an operator determinant with no scalar closed form.
- **1979–1991** — Basor, Böttcher–Silbermann prove large FH families; Basor–Tracy find counterexamples to the naive FH formula and state the generalized (summed) conjecture.
- **1999–2000** — Borodin–Okounkov formula; alternative proofs by Basor–Widom and Böttcher.
- **2011** — Deift, Its, Krasovsky prove the generalized Fisher–Hartwig conjecture for $\Re\alpha_j>-1/2$, $\beta_j$ with $|\Re\beta_j - \Re\beta_k|<1$, using Riemann–Hilbert steepest descent (Annals of Math. 174).
- **2013** — Sobolev proves Widom's conjecture for piecewise-smooth $\Lambda,\Gamma$ and polynomial/smooth $h$ (Memoirs AMS).
- **2014–2017** — Leschke–Sobolev–Spitzer extend to the non-smooth entropy function, proving the logarithmic scaling of free-fermion Rényi entanglement entropies.

## 4. Partial Results / Verified Cases

- **1D positive symbols, $d=1$:** fully solved. Ibragimov's condition $\sum_k |k||(\log a)_k|^2<\infty$ is necessary and sufficient.
- **Nonvanishing symbols of nonzero winding number:** $D_n(a)=0$ for large $n$ when winding $>0$; asymptotics known for winding $<0$ via Fisher–Hartwig with $\beta$-parameters.
- **Fisher–Hartwig class:** proved for $m$ finite singularities, $\Re\alpha_j>-1/2$, and $\beta_j$ in the non-degenerate window $|\Re(\beta_j-\beta_k)|<1$ (Deift–Its–Krasovsky 2011). Error term $O(n^{-1+\varepsilon})$ for generic parameters.
- **Analytic symbols:** exponentially small corrections, $D_n(a)/(G^nE) = 1+O(\rho^{n})$, via Borodin–Okounkov.
- **Merging singularities:** two singularities separated by distance $t\sim n^{-1}$ — uniform asymptotics in terms of Painlevé V (Claeys–Its–Krasovsky 2011) and Painlevé VI/III in related regimes.
- **Toeplitz+Hankel determinants:** FH asymptotics established for wide symbol classes (Deift–Its–Krasovsky; Basor–Ehrhardt).
- **Higher dimensions:** Widom's conjecture proved for $d\ge 1$, piecewise-$C^1$ $\Lambda$ and $\Gamma$, smooth symbols, and $h$ analytic or $C^\infty$ with $h(0)=0$ (Sobolev 2013); extended to $h(t)=|t|^\gamma$-type and entropy functions $h(t)=-t\log t-(1-t)\log(1-t)$ for the free Fermi gas (Leschke–Sobolev–Spitzer).
- **Block/matrix symbols:** Szegő–Widom holds for $a\in K^{N\times N}$ with $\det a$ nonvanishing and winding $0$.

## 5. Principal Obstacles

- **No scalar formula in the block case.** $E(a)=\det T(a)T(a^{-1})$ is an infinite-dimensional determinant; there is no known evaluation in terms of the Fourier data of $a$ except for special (e.g. commuting or rational) families. Any "closed form" would require solving a matrix Riemann–Hilbert factorization explicitly, which is generically impossible.
- **Critical regularity is exactly $H^{1/2}$.** Below it, Hankel operators leave the Hilbert–Schmidt class and the exponential of the trace-class expansion diverges. Fourier-analytic and perturbative arguments break at this exact borderline; the divergence is logarithmic, so no soft compactness argument recovers it.
- **Degenerate FH parameters.** When $|\Re(\beta_j-\beta_k)|\ge 1$ several FH representations contribute at the same order, and the RH parametrix built from confluent hypergeometric local models loses uniform invertibility. Oscillatory cancellation between representations is not controlled.
- **Riemann–Hilbert methods are one-dimensional.** The steepest-descent machinery relies on a scalar/matrix jump on a contour in $\mathbb{C}$; there is no analogue for $d\ge 2$ truncated pseudodifferential operators, so Widom-type results rely instead on delicate multiscale/commutator estimates that give only the first two terms.
- **Non-smooth $h$ in $d\ge 2$.** Standard approximation of $h$ by polynomials loses control of the $\alpha^{d-1}\log\alpha$ coefficient, since $\mathcal{U}(h;b)$ is not continuous in $h$ in any norm compatible with the trace-norm estimates available.
- **Corner and curvature effects.** For $\partial\Lambda$ with corners the conjectured $\alpha^{d-1}$-order (non-log) term acquires contributions with no known universal formula.

## 6. The Gap

Precisely:

- Proven: FH asymptotics for $\Re\alpha_j>-1/2$ and $|\Re(\beta_j-\beta_k)|<1$. Missing: the degenerate window $|\Re(\beta_j-\beta_k)|\ge 1$, and symbols with infinitely many singularities or with $\alpha_j$ approaching $-1/2$ (where $a\notin L^1$).
- Proven: two-term asymptotics in Widom's conjecture. Missing: the third term $O(\alpha^{d-1})$, whose coefficient is not even conjecturally known for general $h$, and any error bound better than $o(\alpha^{d-1}\log\alpha)$.
- Proven: $E(a)$ as an abstract operator determinant in the block case. Missing: an explicit evaluation, or a proof that none exists.
- Proven: pointwise asymptotics for fixed symbol. Missing: uniformity in the symbol, needed for applications where the symbol depends on $n$ (random matrix gap probabilities, Ising correlations at criticality).

## 7. Current Research (as of June 2026)

- **Riemann–Hilbert school** (Its, Krasovsky, Deift, Claeys, Its' collaborators; Indiana–Purdue, KCL, NYU, Leuven): uniform asymptotics through parameter degenerations; transition kernels connecting Painlevé III/V/VI regimes.
- **Operator-theoretic school** (Basor, Ehrhardt, Böttcher; AIM, UC Santa Cruz, TU Chemnitz): Toeplitz+Hankel and structured determinants, sharp trace-ideal criteria, and Szegő–Widom for symbols with jump discontinuities.
- **Spectral-geometry school** (Sobolev, Spitzer, Leschke; UCL, Bochum, Erlangen): sharpening Widom-type asymptotics for non-smooth $h$ and for domains with corners; connections to entanglement-entropy area-law violations. *(frontier — verify)* Reported progress on third-order terms for smooth strictly convex $\Lambda$ remains unpublished at review time.
- **Integrable probability**: Szegő-type asymptotics as the mechanism behind Tracy–Widom and Gaussian multiplicative chaos limits for characteristic polynomials of $\mathrm{CUE}(n)$; connections to the Fyodorov–Hiary–Keating conjecture.
- **Multivariable Szegő theory**: extensions of the Helson–Lowdenslager first-limit theorem to $\mathbb{T}^d$; no strong Szegő analogue is known there, and the correct substitute for $H^{1/2}$ is open.

## 8. Future Work

- Push the RH analysis through the degenerate FH window by constructing a global parametrix that resolves competing representations simultaneously.
- Develop a "higher-dimensional Riemann–Hilbert" or microlocal transfer-operator method to reach third-order terms in Widom's conjecture.
- Find necessary-and-sufficient conditions for trace-class-ness of $H(b)H(\tilde c)$ in the block/matrix setting, which would give a sharp Szegő–Widom class.
- Determine whether $E(a)$ for $2\times2$ symbols admits a theta-function evaluation when $a$ is algebraic.
- Establish symbol-uniform Szegő asymptotics adequate for $n$-dependent symbols in random-matrix applications.

## 9. Key References

- **[Foundational]** G. Szegő. *Ein Grenzwertsatz über die Toeplitzschen Determinanten einer reellen positiven Funktion.* Mathematische Annalen 76 (1915), 490–503.
- **[Foundational]** G. Szegő. *On certain Hermitian forms associated with the Fourier series of a positive function.* Comm. Sém. Math. Univ. Lund (1952), 228–238.
- **[Foundational]** M. Kac. *Toeplitz matrices, translation kernels and a related problem in probability theory.* Duke Mathematical Journal 21 (1954), 501–509.
- **[Foundational]** I. A. Ibragimov. *A theorem of Gabor Szegő.* Matematicheskie Zametki 3 (1968), 693–702.
- **[Foundational]** M. E. Fisher, R. E. Hartwig. *Toeplitz determinants: some applications, theorems, and conjectures.* Advances in Chemical Physics 15 (1968), 333–353.
- **[Foundational]** H. Widom. *Asymptotic behavior of block Toeplitz matrices and determinants. II.* Advances in Mathematics 21 (1976), 1–29.
- **[Foundational]** H. Widom. *On a class of integral operators with discontinuous symbol.* Toeplitz Centennial, Operator Theory: Advances and Applications 4, Birkhäuser (1982), 477–500.
- **[SOTA]** P. Deift, A. Its, I. Krasovsky. *Asymptotics of Toeplitz, Hankel, and Toeplitz+Hankel determinants with Fisher–Hartwig singularities.* Annals of Mathematics 174 (2011), 1243–1299.
- **[SOTA]** A. V. Sobolev. *Pseudo-differential operators with discontinuous symbols: Widom's conjecture.* Memoirs of the American Mathematical Society 222, no. 1043 (2013).
- **[SOTA]** T. Claeys, A. Its, I. Krasovsky. *Emergence of a singularity for Toeplitz determinants and Painlevé V.* Duke Mathematical Journal 160 (2011), 207–262.
- **[SOTA]** H. Leschke, A. V. Sobolev, W. Spitzer. *Scaling of Rényi entanglement entropies of the free Fermi-gas ground state: a rigorous proof.* Physical Review Letters 112 (2014), 160403.
- **[SOTA]** A. Borodin, A. Okounkov. *A Fredholm determinant formula for Toeplitz determinants.* Integral Equations and Operator Theory 37 (2000), 386–396.
- **[Survey]** B. Simon. *Szegő's Theorem and Its Descendants: Spectral Theory for $L^2$ Perturbations of Orthogonal Polynomials.* Princeton University Press, 2011.
- **[Survey]** A. Böttcher, B. Silbermann. *Analysis of Toeplitz Operators*, 2nd ed. Springer, 2006.
- **[Survey]** P. Deift, A. Its, I. Krasovsky. *Toeplitz matrices and Toeplitz determinants under the impetus of the Ising model: some history and some recent results.* Communications on Pure and Applied Mathematics 66 (2013), 1360–1438.

## 10. Worked Example / Concrete Special Case

Take the pure Fisher–Hartwig symbol with a single singularity at $\theta=0$, no jump ($\beta=0$), and $V\equiv 0$:
$$a_\alpha(e^{i\theta}) = |1-e^{i\theta}|^{2\alpha} = \big(2-2\cos\theta\big)^{\alpha},\qquad \alpha>-\tfrac12 .$$

**Step 1: first Szegő theorem.** $\frac{1}{2\pi}\int_{-\pi}^{\pi}\log|1-e^{i\theta}|\,d\theta = 0$, so $G(a_\alpha)=1$ and $D_n^{1/n}\to 1$. All growth is subexponential.

**Step 2: strong Szegő fails.** $\log a_\alpha = 2\alpha\log|1-e^{i\theta}| = -2\alpha\sum_{k\ge1}\frac{\cos k\theta}{k}$, so $(\log a_\alpha)_{\pm k} = -\alpha/k$ and
$$\sum_{k\ge1} k\,|(\log a_\alpha)_k|^2 = \alpha^2\sum_{k\ge1}\frac1k = \infty .$$
Ibragimov's criterion is violated for every $\alpha\ne 0$, so $D_n(a_\alpha)$ cannot converge; the logarithmic divergence exponentiates into a power of $n$.

**Step 3: exact determinant.** The Toeplitz determinant is a Selberg-type product,
$$D_n(a_\alpha) = \prod_{j=0}^{n-1}\frac{j!\,\Gamma(j+1+2\alpha)}{\Gamma(j+1+\alpha)^2}.$$

**Step 4: asymptotics.** Applying the Barnes $G$-function asymptotic $\prod_{j=0}^{n-1}\Gamma(j+1+c)= G(n+1+c)/G(1+c)$ and $\log G(n+1)\sim \tfrac{n^2}{2}\log n$ gives
$$D_n(a_\alpha) = n^{\alpha^2}\,\frac{G(1+\alpha)^2}{G(1+2\alpha)}\big(1+O(n^{-1})\big),$$
exactly the Fisher–Hartwig prediction with $m=1$, $\beta=0$.

**Step 5: numerical check at $\alpha=1$.** Here $a_1 = 2-2\cos\theta$, with $\hat a_0=2$, $\hat a_{\pm1}=-1$, all others $0$ — the discrete Laplacian matrix. The product telescopes:
$$D_n(a_1)=\prod_{j=0}^{n-1}\frac{j!\,(j+2)!}{\big((j+1)!\big)^2}=\prod_{j=0}^{n-1}\frac{j+2}{j+1}=n+1 .$$
The prediction is $n^{1}\,G(2)^2/G(3) = n\cdot 1/1 = n$, since $G(2)=G(3)=1$. Indeed $D_n = n+1 = n(1+O(n^{-1}))$ — the constant, the exponent $\alpha^2=1$, and the error order all match.

**Step 6: what is open here.** For a *single* singularity everything is exact. Put two singularities at $\pm\theta_0$ with jump parameters $\beta_1=-\beta_2=\beta$: the proved result covers $|\Re(2\beta)|<1$. At $\Re\beta = 1/2$ two FH representations contribute equally, the asymptotics acquire an oscillating factor $\propto \cos(n\theta_0 + \phi)$, and no proof of uniformity through that transition is known. Simultaneously letting $\theta_0\to0$ at rate $n^{-1}$ puts the determinant in the Painlevé V regime of Claeys–Its–Krasovsky — the double limit $\theta_0\to0$ *and* $\Re\beta\to1/2$ remains uncontrolled.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*