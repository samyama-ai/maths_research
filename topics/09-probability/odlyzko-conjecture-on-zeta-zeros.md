---
id: 09-probability/odlyzko-conjecture-on-zeta-zeros
title: "Odlyzko Conjecture on Zeta Zeros"
topic: 09-probability
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Odlyzko Conjecture on Zeta Zeros

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/odlyzko-conjecture-on-zeta-zeros` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Let $\rho = \tfrac12 + i\gamma$ run over the nontrivial zeros of the Riemann zeta function $\zeta(s)$, ordered $0 < \gamma_1 \le \gamma_2 \le \cdots$ (counted with multiplicity, and assuming the Riemann Hypothesis so that all $\gamma_n$ are real). Define the **unfolded** (mean-spacing-one) ordinates

$$\tilde\gamma_n \;=\; \frac{\gamma_n}{2\pi}\log\frac{\gamma_n}{2\pi e}, \qquad \delta_n \;=\; \tilde\gamma_{n+1} - \tilde\gamma_n .$$

**Odlyzko's conjecture (the GUE hypothesis, strong form).** As $N \to \infty$, the empirical local statistics of $\{\tilde\gamma_n\}_{n \le N}$ converge to those of the bulk scaling limit of the Gaussian Unitary Ensemble. Concretely:

1. **Spacings.** $\dfrac{1}{N}\\#\{n \le N : \delta_n \le s\} \to \displaystyle\int_0^s p_{\mathrm{GUE}}(t)\,dt$, where $p_{\mathrm{GUE}}$ is the Gaudin–Mehta density.
2. **All correlations.** For every $k \ge 2$ and every nice $f:\mathbb{R}^{k-1}\to\mathbb{R}$,
$$\frac{1}{N}\sum_{\substack{n_1,\dots,n_k \le N \\ \text{distinct}}} f(\tilde\gamma_{n_1}-\tilde\gamma_{n_2},\dots) \longrightarrow \int_{\mathbb{R}^{k-1}} f(x)\,\det\big(K(x_i-x_j)\big)_{i,j=1}^{k}\,dx,$$
with the sine kernel $K(x) = \frac{\sin \pi x}{\pi x}$.

Equivalently: the zeros form, in the $N\to\infty$ limit, a **determinantal point process with the sine kernel** — the same limit object as eigenvalues of large random Hermitian matrices, or of the $\mathrm{CUE}$ $U(N)$ Haar ensemble.

A complete resolution means proving (2) for all $k$ and unrestricted test functions, or exhibiting a statistic where the limit provably differs. Odlyzko's numerical work also isolates a **finer claim**: that the deviations of the finite-height data from the GUE limit are of size $O(1/\log \gamma)$ and are governed by explicit arithmetic (prime-power) corrections.

## 2. Mathematical Foundations

**Zero counting.** $N(T) = \\#\{\rho : 0 < \gamma \le T\}$ satisfies the Riemann–von Mangoldt formula
$$N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi e} + \frac{7}{8} + S(T) + O(1/T), \qquad S(T)=\tfrac1\pi \arg\zeta(\tfrac12+iT),$$
with $S(T)=O(\log T)$ unconditionally. Hence the mean gap near height $T$ is $2\pi/\log T$, which is what the unfolding above divides out.

**Sine-kernel process.** The limiting process has correlation functions $\rho_k(x_1,\dots,x_k) = \det(K(x_i-x_j))_{i,j\le k}$. The gap probability on an interval of length $s$ is the Fredholm determinant
$$E(0;s) = \det\big(I - K\big|_{[0,s]}\big) = \exp\Big(-\int_0^{\pi s}\frac{\sigma(t)}{t}\,dt\Big),$$
where $\sigma$ solves the Painlevé V $\sigma$-form $(t\sigma'')^2 + 4(t\sigma'-\sigma)(t\sigma'-\sigma+(\sigma')^2)=0$, $\sigma(t)\sim -t/\pi - t^2/\pi^2$ (Jimbo–Miwa–Môri–Sato, 1980). The spacing density is $p_{\mathrm{GUE}}(s) = \frac{d^2}{ds^2}E(0;s)$, with small-$s$ behaviour $p_{\mathrm{GUE}}(s) = \frac{\pi^2}{3}s^2 + O(s^4)$ — **quadratic level repulsion**, the signature feature. The Wigner surmise
$$p_W(s) = \frac{32}{\pi^2}s^2 e^{-4s^2/\pi}$$
approximates $p_{\mathrm{GUE}}$ to within about $1\%$ in the bulk.

**Montgomery's form factor.** For $T$ large set
$$F(\alpha,T) = \Big(\frac{T\log T}{2\pi}\Big)^{-1}\!\!\!\sum_{0<\gamma,\gamma'\le T} T^{i\alpha(\gamma-\gamma')} w(\gamma-\gamma'), \qquad w(u)=\frac{4}{4+u^2}.$$
Montgomery (1973), assuming RH, proved $F(\alpha,T) = |\alpha| + T^{-2|\alpha|}\log T\,(1+o(1)) + o(1)$ uniformly for $|\alpha|\le 1-\varepsilon$, and conjectured $F(\alpha,T)\to 1$ for $|\alpha|>1$. The pair-correlation statement equivalent to $F\equiv 1$ off $[-1,1]$ is
$$\frac{1}{N(T)}\sum_{\substack{0<\gamma,\gamma'\le T\\ \gamma\neq\gamma'}} f\big(\tilde\gamma - \tilde\gamma'\big) \;\longrightarrow\; \int_{\mathbb{R}} f(u)\Big(1 - \Big(\frac{\sin\pi u}{\pi u}\Big)^{2}\Big)du .$$

**Arithmetic source.** The explicit formula couples zeros to primes:
$$\sum_\rho h(\gamma) = \frac{1}{2\pi}\int_{\mathbb R} h(r)\,\Big(\log\tfrac{1}{\pi}+\mathrm{Re}\,\tfrac{\Gamma'}{\Gamma}(\tfrac14+\tfrac{ir}{2})\Big)dr - \frac{1}{\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\hat h(\log n) + \cdots$$
so correlations of zeros are correlations of $\Lambda(n)$; the $|\alpha|>1$ range of $F$ is exactly where off-diagonal prime pairs (Hardy–Littlewood twin-type constants) enter.

## 3. History & State of the Art (SOTA)

- **1961.** Gaudin computes the limiting spacing law for random Hermitian matrices; Mehta–Gaudin develop the determinantal formalism.
- **1972–73.** Montgomery derives the pair-correlation form factor; the Dyson conversation identifies $1-(\sin\pi u/\pi u)^2$ as the GUE pair correlation.
- **1987.** Odlyzko, *Math. Comp.* 48, computes $\sim 10^5$ zeros near $\gamma_{10^{12}}$ and finds close agreement with the Gaudin density and with the pair correlation, including in the $|\alpha|>1$ range Montgomery could not reach. This paper is the origin of the conjecture in its empirical, all-statistics form.
- **1988.** Odlyzko–Schönhage give an $O(T^{1+\varepsilon})$ algorithm for evaluating $\zeta(\tfrac12+it)$ at $T^{1/2}$ points, making very high computations feasible.
- **1994–96.** Hejhal proves the triple correlation for restricted support; Rudnick–Sarnak extend to all $n$-level correlations of any principal automorphic $L$-function, again with restricted support.
- **1995–2001.** Bogomolny–Keating derive, from the Hardy–Littlewood conjecture, the full $n$-point correlations *including* lower-order $1/\log T$ arithmetic terms. Odlyzko (2001, Contemp. Math. 290) reports data around the $10^{22}$-nd zero: raw GUE agreement is good but visibly imperfect, and the Bogomolny–Keating corrections account for the discrepancy.
- **2007–08.** Conrey–Snaith reproduce the same corrections from the $L$-functions ratios conjectures.
- **2021.** Platt–Trudgian verify RH to height $3\times10^{12}$, underwriting the unfolding used at moderate heights.

**Status.** Empirically supported to several decimal places over $\sim22$ orders of magnitude in height; unconditionally proved only for band-limited test functions.

## 4. Partial Results / Verified Cases

- **Pair correlation, $|\alpha| < 1$.** Under RH, Montgomery (1973): the conjecture holds for test functions $f$ with $\mathrm{supp}\,\hat f \subseteq (-1,1)$.
- **Triple correlation.** Hejhal (1994), under RH, for $\hat f$ supported in $\{\sum|\xi_i|<1\}$ (in suitable coordinates).
- **$n$-level correlations, all $n$.** Rudnick–Sarnak (1996), unconditionally for $\zeta$ and for principal $L$-functions of $\mathrm{GL}_m/\mathbb{Q}$, for $\hat f$ supported in $\sum_{j=1}^n |\xi_j| < 2$. This is the strongest general theorem known and covers a genuinely $n$-dimensional, though narrow, cone.
- **Conditional extensions.** Assuming the Hardy–Littlewood prime-pair conjecture in strong uniform form, Goldston–Gonek–Özlük–Snyder push pair correlation past $|\alpha|=1$; Bogomolny–Keating obtain the full correlations heuristically-but-consistently.
- **Equivalences.** Goldston–Montgomery (1987): pair correlation for all $\alpha$ is equivalent to the asymptotic $\int_1^X (\psi(x+\delta x)-\psi(x)-\delta x)^2dx \sim \tfrac12 \delta x^2 \log(1/\delta)$ for $X^{-1}\le\delta\le X^{-\varepsilon}$.
- **Function fields (proved).** Katz–Sarnak (1999): for zeta functions of curves over $\mathbb{F}_q$, the $q\to\infty$ limit of the zero statistics is exactly the corresponding random-matrix law — the GUE-type conjecture is a theorem in this analogue.
- **Numerics.** Odlyzko: $10^5$ zeros near $10^{12}$ (1987); $10^9$ zeros near $10^{22}$ (2001), spacing histogram matching GUE to $\approx 10^{-3}$–$10^{-4}$ and to higher accuracy after the $O(1/\log T)$ arithmetic correction. Zeros verified on the critical line to height $3\times 10^{12}$ (Platt–Trudgian, 2021).

## 5. Principal Obstacles

- **The $|\alpha|=1$ wall.** In Montgomery's derivation, $F(\alpha,T)$ for $|\alpha|<1$ is controlled by the *diagonal* $n=m$ terms in $\sum \Lambda(n)\Lambda(m)(n/m)^{-1/2-iT}$. Past $|\alpha|=1$ the answer is dominated by off-diagonal pairs $n-m=h\neq0$, whose evaluation requires the Hardy–Littlewood conjecture $\sum_{n\le x}\Lambda(n)\Lambda(n+h)\sim \mathfrak{S}(h)x$ **with uniformity in $h$ up to $h \asymp x$** — far beyond anything provable. Sieve methods give upper bounds of the right order but no asymptotics.
- **No spectral realization.** The Hilbert–Pólya program would make GUE statistics a theorem about a self-adjoint operator, but no such operator with the right trace formula is known; the Berry–Keating $xp$ Hamiltonian is formal and lacks a quantization with the correct counting function.
- **Correlations do not control spacings.** Gap distributions are alternating sums over all $k$-point correlations; band-limited knowledge of finitely many $\rho_k$ gives no unconditional inclusion–exclusion bound. Even proving $p(s)\to 0$ as $s\to0$ (level repulsion, i.e. no exceptionally close zeros) is open.
- **Slow convergence hides the target.** The finite-$T$ deviations are $\Theta(1/\log T)$; at $T=10^{22}$, $1/\log T \approx 0.02$. Numerics can never separate "GUE plus arithmetic corrections" from "something else agreeing to that order".
- **Repulsion vs. simplicity.** Not even simplicity of the zeros is known; $\ge 41.7\%$ simple (Pratt–Robles–Zaharescu–Zeindler style mollifier results) is the SOTA, so the point process is not even known to be simple.

## 6. The Gap

The proved region is a **cone of band-limited test functions**, $\sum_j|\xi_j| < 2$ for $n$-level correlations (and $|\xi|<1$ for pairs). The conjecture is a statement about *arbitrary* test functions — equivalently about the process at all frequencies. The single crossing point is:

> Extend the asymptotic evaluation of $\sum_{n\le x}\Lambda(n)\Lambda(n+h)$, uniformly for $h$ up to $x^{1-\varepsilon}$, or find a way to compute $F(\alpha,T)$ for $\alpha>1$ that does not factor through prime-pair asymptotics.

Everything else — all $k$-point correlations, hence all gap and spacing statistics — follows from the Bogomolny–Keating machinery once that off-diagonal input is available. So the gap is not a family of separate problems; it is one arithmetic input of twin-prime strength, sitting under a conjecture that is otherwise structurally understood.

## 7. Current Research (as of June 2026)

- **Ratios and moments.** The Conrey–Farmer–Keating–Rubinstein–Snaith recipe and the $L$-functions ratios conjectures continue to generate lower-order terms testable against Odlyzko-scale data; the agreement to $1/\log T$ and beyond is the strongest quantitative evidence for the conjecture. Groups at Bristol (Keating, Snaith) and AIM lead this line.
- **Extreme-value probability.** The Fyodorov–Hiary–Keating conjecture for $\max_{|h|\le1}|\zeta(\tfrac12+it+ih)|$ predicts branching-random-walk behaviour; Arguin–Belius–Bourgade–Radziwiłł–Soundararajan (2019) proved the leading order. Refinements to the full $\log\log$ term remain active *(frontier — verify)*.
- **Universality transfer.** Techniques from Dyson-Brownian-motion universality (Erdős–Schlein–Yau, Tao–Vu) prove sine-kernel limits for wide matrix classes but have no known arithmetic analogue; attempts to build a stochastic-dynamics model whose stationary law is the zero process are exploratory *(frontier — verify)*.
- **Function-field and random-multiplicative models.** Statistics over families of curves and over random multiplicative functions are used as testbeds where theorems are provable.
- **Computation.** Independent recomputation and extension of Odlyzko's high-height datasets, and rigorous interval-arithmetic zero verification (Platt and successors), remain ongoing.

## 8. Future Work

- Prove level repulsion in weak form: $\\#\{n\le N : \delta_n < \varepsilon\} = o_\varepsilon(N)$ with $\varepsilon$ small — currently open and strictly weaker than the full conjecture.
- Establish pair correlation for $|\alpha| \in (1, 1+\delta)$ for some explicit $\delta>0$ under hypotheses weaker than full Hardy–Littlewood (e.g. an averaged prime-pair conjecture over $h$).
- Develop an unconditional inclusion–exclusion converting band-limited correlation knowledge into one-sided bounds on $E(0;s)$.
- Sharpen the Bogomolny–Keating expansion to $O(1/\log^2 T)$ and test against data near $10^{24}$, where present algorithms are borderline feasible.
- Pursue a genuine spectral interpretation (noncommutative-geometry trace formulae, or a quantized $xp$-type system) that would deliver GUE by symmetry rather than by prime correlations.

## 9. Key References

- **[Foundational]** H. L. Montgomery. *The pair correlation of zeros of the zeta function.* In *Analytic Number Theory*, Proc. Sympos. Pure Math. XXIV, AMS, 1973, 181–193.
- **[Foundational]** M. Gaudin. *Sur la loi limite de l'espacement des valeurs propres d'une matrice aléatoire.* Nuclear Physics 25 (1961), 447–458.
- **[Foundational / Numerics]** A. M. Odlyzko. *On the distribution of spacings between zeros of the zeta function.* Mathematics of Computation 48 (1987), 273–308.
- **[Numerics]** A. M. Odlyzko, A. Schönhage. *Fast algorithms for multiple evaluations of the Riemann zeta function.* Transactions of the AMS 309 (1988), 797–809.
- **[Numerics]** A. M. Odlyzko. *The $10^{22}$-nd zero of the Riemann zeta function.* In *Dynamical, Spectral, and Arithmetic Zeta Functions*, Contemp. Math. 290, AMS, 2001, 139–144.
- **[Theory]** Z. Rudnick, P. Sarnak. *Zeros of principal $L$-functions and random matrix theory.* Duke Mathematical Journal 81 (1996), 269–322.
- **[Theory]** D. A. Hejhal. *On the triple correlation of zeros of the zeta function.* International Mathematics Research Notices 1994, no. 7, 293–302.
- **[Theory]** E. B. Bogomolny, J. P. Keating. *Random matrix theory and the Riemann zeros II: $n$-point correlations.* Nonlinearity 9 (1996), 911–935.
- **[Theory]** M. Jimbo, T. Miwa, Y. Môri, M. Sato. *Density matrix of an impenetrable Bose gas and the fifth Painlevé transcendent.* Physica D 1 (1980), 80–158.
- **[Theory]** D. A. Goldston, H. L. Montgomery. *Pair correlation of zeros and primes in short intervals.* In *Analytic Number Theory and Diophantine Problems*, Birkhäuser, 1987, 183–203.
- **[SOTA / Recent]** J. B. Conrey, N. C. Snaith. *Correlations of eigenvalues and Riemann zeros.* Communications in Number Theory and Physics 2 (2008), 477–536.
- **[SOTA / Recent]** L.-P. Arguin, D. Belius, P. Bourgade, M. Radziwiłł, K. Soundararajan. *Maximum of the Riemann zeta function on a short interval of the critical line.* Comm. Pure Appl. Math. 72 (2019), 500–535.
- **[SOTA / Recent]** D. J. Platt, T. S. Trudgian. *The Riemann hypothesis is true up to $3\cdot10^{12}$.* Bulletin of the LMS 53 (2021), 792–797.
- **[Survey]** N. M. Katz, P. Sarnak. *Zeroes of zeta functions and symmetry.* Bulletin of the AMS 36 (1999), 1–26.
- **[Survey]** P. Bourgade, J. P. Keating. *Quantum chaos, random matrix theory, and the Riemann $\zeta$-function.* Séminaire Poincaré XIV (2010), 115–153.
- **[Book]** M. L. Mehta. *Random Matrices*, 3rd ed. Elsevier/Academic Press, 2004.

## 10. Worked Example / Concrete Special Case

**Unfolding the first four gaps.** Take the first five ordinates:
$$\gamma_1=14.134725,\ \gamma_2=21.022040,\ \gamma_3=25.010858,\ \gamma_4=30.424876,\ \gamma_5=32.935062 .$$
Use the local density $\frac{1}{2\pi}\log\frac{\gamma}{2\pi}$, so $\delta_n \approx (\gamma_{n+1}-\gamma_n)\cdot\frac{1}{2\pi}\log\frac{\gamma_n}{2\pi}$:

| $n$ | $\gamma_{n+1}-\gamma_n$ | $\frac{1}{2\pi}\log\frac{\gamma_n}{2\pi}$ | $\delta_n$ |
|---|---|---|---|
| 1 | 6.887315 | 0.12904 | 0.8887 |
| 2 | 3.988818 | 0.19221 | 0.7667 |
| 3 | 5.414018 | 0.21985 | 1.1902 |
| 4 | 2.510186 | 0.25104 | 0.6302 |

Mean $= 0.869$ — close to the required $1$, with the shortfall an $O(1/\log\gamma)$ effect: at $\gamma\approx 30$, $1/\log\gamma \approx 0.29$, so a $13\%$ deficit is entirely expected. This is precisely why Odlyzko had to go to $\gamma \sim 10^{22}$, where $1/\log\gamma \approx 0.02$.

**Comparing to the prediction.** At $s = 0.8887$ the Wigner surmise gives
$$p_W(0.8887) = \frac{32}{\pi^2}(0.8887)^2 e^{-4(0.8887)^2/\pi} = 3.2423 \times 0.7898 \times e^{-1.0053} = 0.937,$$
while a Poisson (independent-points) model would give $e^{-0.8887} = 0.411$. The two models are separated by a factor $\approx 2.3$ at this spacing, and by far more near $s=0$: as $s\to0$, GUE gives $p(s)\approx \frac{\pi^2}{3}s^2 \to 0$ while Poisson gives $p(0)=1$.

**What the data settles.** In Odlyzko's $10^9$-zero sample near $\gamma_{10^{22}}$, the fraction of gaps with $\delta_n < 0.1$ is on the order of $10^{-4}$, matching $\int_0^{0.1}\frac{\pi^2}{3}s^2ds = \frac{\pi^2}{9}\cdot 10^{-3} \approx 1.1\times10^{-3}$ after the exact kernel is used — and flatly incompatible with Poisson's $\approx 0.095$. So repulsion is not in doubt numerically. Yet no theorem excludes even a positive density of gaps below $0.1$: the four-gap computation above uses only arithmetic, while the $10^9$-gap histogram uses only computation, and the conjecture asks for a proof that neither supplies.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*