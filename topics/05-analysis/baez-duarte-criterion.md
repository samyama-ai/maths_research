---
id: 05-analysis/baez-duarte-criterion
title: "Baez-Duarte Criterion"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Baez-Duarte Criterion

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/baez-duarte-criterion` · **Status:** open

## 1. Problem Statement / Conjecture

The Báez-Duarte criterion is a pair of equivalent reformulations of the Riemann Hypothesis (RH) as a concrete approximation problem in a Hilbert space, together with the still-open task of settling either side of the equivalence.

**(A) Hilbert-space (Nyman–Beurling–Báez-Duarte) form.** In $L^2(0,1)$ set
$$\rho_\theta(t)=\Big\{\frac{\theta}{t}\Big\}-\theta\Big\{\frac1t\Big\},\qquad 0<\theta\le 1,$$
where $\{x\}$ is the fractional part. Then RH holds **iff** the constant function $\mathbf 1=\chi_{(0,1)}$ lies in the closed linear span of $\{\rho_{1/n}: n=2,3,4,\dots\}$ — the *integer reciprocals alone* suffice.

**(B) Sequential Riesz-like form.** Put
$$c_n=\sum_{k=0}^{n}\binom{n}{k}\frac{(-1)^k}{\zeta(2k+2)} .$$
Then RH holds **iff** $c_n=O\!\left(n^{-3/4+\varepsilon}\right)$ for every $\varepsilon>0$.

A resolution means: prove (or refute) the approximation/decay statement by means independent of RH, thereby proving (or refuting) RH; equivalently, produce explicit coefficients $a_n$ making the distance in Section 2 tend to $0$, or exhibit an obstruction. The criteria themselves are **theorems**; what is open is the analytic statement they encode.

## 2. Mathematical Foundations

Let $\mathcal H=L^2\big((0,1),dt\big)$ and let $\mathcal N_{\mathbb N}=\overline{\operatorname{span}}\{\rho_{1/n}:n\ge2\}$. Mellin transform on the critical line maps the problem into a weighted $H^2$ problem: for a Dirichlet polynomial $A_N(s)=\sum_{n\le N}a_n n^{-s}$, define the **Báez-Duarte distance**
$$d_N^2:=\inf_{a_1,\dots,a_N\in\mathbb C}\ \frac1{2\pi}\int_{-\infty}^{\infty}\Big|1-\zeta\big(\tfrac12+it\big)A_N\big(\tfrac12+it\big)\Big|^2\,\frac{dt}{\tfrac14+t^2}.$$

> **Criterion (Báez-Duarte 2003).** RH $\iff \displaystyle\lim_{N\to\infty}d_N=0$.

The sequence $d_N$ is non-increasing and $\ge 0$, so the limit always exists; RH is the statement that the limit is $0$. The quantitative refinement conjectured by Balazard–Saias is
$$d_N^2\ \sim\ \frac{C}{\log N},\qquad C=\sum_{\rho}\frac{1}{|\rho|^2}=2+\gamma-\log 4\pi\approx 0.0461914,$$
the sum over nontrivial zeros $\rho$, $\gamma$ Euler's constant.

For form (B), expanding $1/\zeta(2k+2)=\sum_{m\ge1}\mu(m)m^{-2k-2}$ and summing the binomial gives the closed form
$$c_n=\sum_{m=1}^{\infty}\frac{\mu(m)}{m^{2}}\Big(1-\frac{1}{m^{2}}\Big)^{n}\qquad(n\ge0),$$
so for $n\ge1$ the $m=1$ term vanishes. The Mellin–Barnes representation
$$c_n=-\frac{1}{2\pi i}\int_{(a)}\frac{\Gamma(n+1)\,\Gamma(s)}{\Gamma(n+1+s)}\,\frac{ds}{\zeta(2s+2)}$$
shows that shifting the contour left past $\Re s=-3/4$ is possible exactly when $\zeta(2s+2)$ has no zeros there, i.e. exactly under RH; each nontrivial zero $\rho$ contributes a residue of size $\asymp n^{-\Re\rho/2}\,|\zeta'(\rho)|^{-1}$ (simple zeros), which is $n^{-1/4}$ **relative** to $n^{-1/2}$ only on the critical line.

Underlying classical inputs: the Nyman (1950) and Beurling (1955) closure theorem, the functional equation and Hadamard product for $\zeta$, and the Riesz criterion (1916): RH $\iff \sum_{k\ge1}\frac{(-1)^{k+1}x^{k}}{(k-1)!\,\zeta(2k)}=O(x^{1/4+\varepsilon})$.

## 3. History & State of the Art (SOTA)

- **1916.** M. Riesz gives the first entire-function decay criterion for RH; Hardy–Littlewood give a companion Bessel-series criterion.
- **1950–1955.** B. Nyman's Uppsala thesis, then Beurling's PNAS note, prove RH $\iff$ $\mathbf 1\in\overline{\operatorname{span}}\{\rho_\theta:0<\theta<1\}$ — a *continuum* of translates.
- **1995.** Nikolski, and independently Vasyunin, recast the problem via distance formulae and compute the Gram matrix $\langle\rho_{1/m},\rho_{1/n}\rangle$ in closed form using cotangent (Vasyunin) sums.
- **1998–2000.** Balazard–Saias introduce $d_N$ and the mollifier viewpoint; Báez-Duarte, Balazard, Landreau, Saias prove the lower bound $\liminf_N d_N^2\log N\ \ge\ \sum_\rho 1/|\rho|^2$ and conjecture equality.
- **2002.** Burnol sharpens the lower bound to $\liminf_N d_N^2\log N\ \ge\ \sum_\rho m_\rho^2/|\rho|^2$, where $m_\rho$ is the multiplicity — so a proof of the conjectured asymptotic would prove all zeros simple.
- **2003.** Báez-Duarte proves the discretization (only $\theta=1/n$ needed) and, separately, the sequential criterion $c_n=O(n^{-3/4+\varepsilon})$.
- **2013.** Bettin–Conrey–Farmer analyse an "optimal" choice of Dirichlet coefficients and relate the asymptotic for $d_N$ to twisted second-moment/ratios conjectures for $\zeta$.

## 4. Partial Results / Verified Cases

- **Equivalences proven.** Both (A) and (B) are theorems: the reduction from the continuum $\{\rho_\theta\}$ to $\{\rho_{1/n}\}$ (Báez-Duarte 2003) and the $n^{-3/4+\varepsilon}$ equivalence are unconditional.
- **Unconditional decay.** The trivial bound from $\big|(1-m^{-2})^n\big|\le e^{-n/m^{2}}$ gives $|c_n|\le\sum_{m\ge2}m^{-2}e^{-n/m^{2}}\ll n^{-1/2}$, with the mass coming from $m\asymp\sqrt n$. So $c_n\to0$ is elementary; the exponent $1/2$ is what current unconditional technology delivers (derived; the classical zero-free region improves it only by a sub-polynomial factor).
- **Unconditional lower bounds on $d_N$.** $d_N^2\log N\ge \sum_\rho m_\rho^2/|\rho|^2+o(1)$ (Burnol 2002), refining BBLS (2000). Any nontrivial zero off the critical line forces $\liminf d_N>0$.
- **Zero-free half-plane transfer.** If $\zeta(s)\ne0$ for $\Re s>\sigma_0\ge1/2$, then $c_n\ll n^{-1+\sigma_0/2+\varepsilon}$ and, symmetrically, a decay bound $c_n\ll n^{-\alpha}$ yields a zero-free region $\Re s>2-2\alpha$; the criterion is "graded", not all-or-nothing.
- **Numerics.** Landreau–Richard (2002) computed $d_N$ using Vasyunin's exact Gram matrix for $N$ up to the low hundreds; the data are consistent with $d_N\to0$ but converge far too slowly ($1/\log N$) to test the constant $C$. Wolf (2008) computed $c_n$ to $n\sim10^{5}$–$10^{6}$ with high-precision arithmetic and found oscillatory behaviour matching $n^{-3/4}$ times a slowly varying amplitude.
- **Structural special cases.** Analogues of the Nyman–Beurling–Báez-Duarte setup are proved for Dirichlet $L$-functions and for function-field zeta functions, where RH is a theorem; there the approximation statement holds and the analogue of $C$ is computable.

## 5. Principal Obstacles

- **No unconditional upper bound is possible without proving RH.** Since $d_N\to0$ *is* RH, every upper-bound argument must implicitly contain a proof of RH. This kills the usual "prove a bound, then bootstrap" strategy: there is no safe intermediate target.
- **Mollifier length.** $A_N$ acts as a mollifier of $\zeta$ of length $N$. The known technology (Levinson/Conrey-type mean-value theorems) controls $\int|\zeta A_N|^2$ only for $N\le T^{\vartheta}$ with $\vartheta<1$; the Báez-Duarte problem needs uniformity as $N\to\infty$ against the *whole* critical line at once, i.e. $\vartheta$ effectively unbounded. Twisted second moments beyond $\vartheta=1$ are exactly the barrier.
- **Möbius cancellation of the right strength.** In form (B) the required upgrade from the trivial $n^{-1/2}$ to $n^{-3/4}$ is a square-root-type cancellation in $\sum_m \mu(m)m^{-2}(1-m^{-2})^n$ over the range $m\asymp\sqrt n$. This is a smoothed Mertens-type statement, and every known route to it (contour shift, Perron, sieve) reintroduces the zeros.
- **Weak conditioning.** The Gram matrix of $\{\rho_{1/n}\}_{n\le N}$ is extremely ill-conditioned; the optimal coefficients $a_n$ grow and oscillate, so numerical extrapolation cannot separate $C/\log N$ from $C'/\log N$ with a wrong constant, nor detect a positive limit.
- **Loss of positivity.** Unlike Weil-explicit-formula positivity criteria, the Báez-Duarte distance is an infimum, not a positive-definite quadratic form in test functions; the standard positivity machinery (Weil, Li, de Branges) does not directly apply.

## 6. The Gap

Proven: $c_n\ll n^{-1/2}$ unconditionally, and $\liminf_N d_N^2\log N\ge\sum_\rho m_\rho^2/|\rho|^2>0$. Needed: $c_n\ll n^{-3/4+\varepsilon}$, equivalently $d_N\to0$.

The gap is therefore a single factor of $n^{-1/4}$ — exactly one quarter-power of extra cancellation in a Möbius sum, or equivalently the passage from "the optimal mollifier of length $N$ leaves an $L^2$-residue bounded below" to "the residue tends to $0$". Quantitatively, one must move the admissible contour in the Mellin–Barnes integral from $\Re s=-1/2$ (the abscissa of the possible zeros $\rho$ with $\Re\rho\to1$) to $\Re s=-3/4$ (the critical line's image). No known method crosses a half-plane of zeros without first excluding them.

## 7. Current Research (as of June 2026)

- **Optimal-coefficient programme (Bettin, Conrey, Farmer, and successors).** Replacing the true minimizer by an explicit "Selberg-type" mollifier $a_n=\mu(n)(1-\log n/\log N)$-style, and evaluating the resulting integral against ratios-conjecture predictions, reproduces $C/\log N$ conditionally. Extending this to unconditional upper bounds requires twisted moments past the $\vartheta=1$ barrier *(frontier — verify)*.
- **Vasyunin/cotangent-sum analysis.** The Gram entries involve Vasyunin sums $V(m,n)=\sum_{k}\frac{k}{n}\cot\frac{\pi k m}{n}$; their distribution theory (Bettin–Conrey's period function for $\zeta$) is being pushed to give sharper spectral bounds on the Gram matrix.
- **High-precision numerics on $c_n$.** Independent recomputations to $n\sim10^{7}$ with interval arithmetic aim to fit the predicted oscillation $c_n\approx n^{-3/4}\sum_\rho \Re\big(A_\rho n^{i\gamma_\rho/2}\big)$ driven by low zeros *(frontier — verify)*.
- **Function-field and adelic models.** Transporting the criterion to $\mathbb F_q[T]$ and to Connes–Meyer style adelic spectral realizations, where the "distance" is computable, to identify which structural feature makes the approximation succeed.

## 8. Future Work

- Prove a *conditional-free* upper bound $d_N^2\ll 1/\log^{\delta} N$ for any $\delta>0$ — this alone would prove RH, so effort concentrates instead on identifying the minimal extra input (e.g. a zero-density hypothesis) sufficient.
- Establish the Balazard–Saias asymptotic $d_N^2\log N\to\sum_\rho1/|\rho|^2$ under RH; by Burnol's lower bound this would also give simplicity of all zeros.
- Develop unconditional twisted second-moment estimates $\int_0^T|\zeta(\tfrac12+it)|^2 (m/n)^{-it}dt$ uniform for $mn\le T^{1+\delta}$.
- Find a positivity-preserving variant of $d_N$ (a quadratic form rather than an infimum) to connect the criterion to Weil/Li positivity.
- Explain the observed oscillation of $c_n n^{3/4}$ rigorously as a zero-driven almost-periodic function.

## 9. Key References

- **[Foundational]** M. Riesz. *Sur l'hypothèse de Riemann.* Acta Mathematica **40** (1916), 185–190.
- **[Foundational]** A. Beurling. *A closure problem related to the Riemann zeta-function.* Proceedings of the National Academy of Sciences USA **41** (1955), 312–314. [DOI](https://doi.org/10.1073/pnas.41.5.312)
- **[Foundational]** B. Nyman. *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces.* Doctoral thesis, University of Uppsala, 1950.
- **[Foundational]** L. Báez-Duarte. *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis.* Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. **14** (2003), 5–11.
- **[Foundational]** L. Báez-Duarte. *A sequential Riesz-like criterion for the Riemann hypothesis.* International Journal of Mathematics and Mathematical Sciences **2003**, no. 21, 3527–3537.
- **[SOTA]** L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias. *Notes sur la fonction $\zeta$ de Riemann, 3.* Advances in Mathematics **149** (2000), 130–144.
- **[SOTA]** J.-F. Burnol. *A lower bound in an approximation problem involving the zeros of the Riemann zeta function.* Advances in Mathematics **170** (2002), 56–70. [DOI](https://doi.org/10.1006/aima.2001.2066)
- **[SOTA]** S. Bettin, J. B. Conrey, D. W. Farmer. *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion.* Proceedings of the Steklov Institute of Mathematics **280** (2013), 67–74. [DOI](https://doi.org/10.1134/s0081543813030036)
- **[SOTA]** B. Bagchi. *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis.* Proceedings of the Indian Academy of Sciences (Math. Sci.) **116** (2006), 137–146. [DOI](https://doi.org/10.1007/bf02829783)
- **[Computational]** B. Landreau, F. Richard. *Le critère de Beurling et Nyman pour l'hypothèse de Riemann: aspects numériques.* Experimental Mathematics **11** (2002), 349–360. [DOI](https://doi.org/10.1080/10586458.2002.10504480)
- **[Computational]** M. Wolf. *Evidence in favor of the Báez-Duarte criterion for the Riemann Hypothesis.* Computational Methods in Science and Technology **14** (2008), 47–54.
- **[Structural]** V. I. Vasyunin. *On a biorthogonal system associated with the Riemann hypothesis.* Algebra i Analiz **7** (1995); English transl. St. Petersburg Mathematical Journal **7** (1996), 405–419.
- **[Structural]** N. Nikolski. *Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann $\zeta$-function.* Annales de l'Institut Fourier **45** (1995), 143–159.
- **[Survey]** M. Balazard. *Completeness problems and the Riemann hypothesis: an annotated bibliography.* In *Number Theory for the Millennium I*, A K Peters, 2002, 21–48.

## 10. Worked Example / Concrete Special Case

Compute the first Báez-Duarte coefficients from $c_n=\sum_{k=0}^n\binom nk(-1)^k/\zeta(2k+2)$, using
$1/\zeta(2)=0.6079271$, $1/\zeta(4)=0.9239384$, $1/\zeta(6)=0.9829525$, $1/\zeta(8)=0.9959392$:

$$c_0=0.6079271,\quad c_1=0.6079271-0.9239384=-0.3160113,$$
$$c_2=0.6079271-1.8478768+0.9829525=-0.2569972,$$
$$c_3=0.6079271-2.7718152+2.9488575-0.9959392=-0.2109698 .$$

Now check against the Möbius form. For $n=1$,
$$\sum_{m\ge2}\frac{\mu(m)}{m^2}\Big(1-\frac1{m^2}\Big)=\sum_{m\ge2}\mu(m)\big(m^{-2}-m^{-4}\big)=\Big(\tfrac1{\zeta(2)}-1\Big)-\Big(\tfrac1{\zeta(4)}-1\Big)=-0.3160113,$$
matching $c_1$. The two representations agree, as required.

**Where the difficulty sits.** Bound each term of $c_n=\sum_{m\ge2}\mu(m)m^{-2}(1-m^{-2})^n$ by absolute value, using $(1-m^{-2})^n\le e^{-n/m^2}$:
$$|c_n|\le\sum_{m\ge2}\frac{e^{-n/m^{2}}}{m^{2}}\approx\frac{1}{\sqrt n}\int_0^\infty \frac{e^{-1/u^{2}}}{u^{2}}\,du=\frac{\sqrt\pi}{2\sqrt n}.$$
So the *triangle inequality alone* gives $c_n=O(n^{-1/2})$, and the dominant range is $m\asymp\sqrt n$: for $n=10^4$ the terms with $m\approx100$ carry the mass, each of size $\approx10^{-4}$, and there are $\approx10^2$ of them, giving $10^{-2}=n^{-1/2}$.

RH demands $|c_n|\ll n^{-3/4+\varepsilon}$, i.e. $10^{-3}$ at $n=10^4$: a tenfold cancellation among $\approx10^{2}$ signed Möbius terms, precisely square-root cancellation $\sqrt{10^2}=10$. Numerically $c_3=-0.211$ against $3^{-3/4}=0.439$ (ratio $0.48$), and Wolf's computations find the ratio $c_n n^{3/4}$ staying bounded and oscillating up to $n\sim10^{6}$. Proving that boundedness for all $n$ — nothing more — is the Riemann Hypothesis.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*