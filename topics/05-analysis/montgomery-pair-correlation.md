---
id: 05-analysis/montgomery-pair-correlation
title: "Montgomery Pair Correlation"
topic: 05-analysis
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Montgomery Pair Correlation Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/montgomery-pair-correlation` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Write the nontrivial zeros of the Riemann zeta function $\zeta(s)$ as $\rho = \beta + i\gamma$. Assume the Riemann Hypothesis (RH), so $\beta = 1/2$ and the ordinates $\gamma$ are real. The counting function is
$$N(T) = \\#\{\rho : 0 < \gamma \le T\} = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + O(\log T),$$
so the mean spacing of ordinates near height $T$ is $2\pi/\log T$. Normalize by setting $\tilde\gamma = \gamma \frac{\log \gamma}{2\pi}$, giving a sequence of mean density $1$.

**Conjecture (Montgomery, 1973).** For fixed real $\alpha < \beta$,
$$\lim_{T\to\infty}\frac{1}{N(T)}\,\\#\left\{(\gamma,\gamma') : 0<\gamma,\gamma'\le T,\ \alpha \le \frac{(\gamma-\gamma')\log T}{2\pi} \le \beta\right\} = \int_\alpha^\beta \left(1 - \left(\frac{\sin \pi u}{\pi u}\right)^2 + \delta(u)\right)du .$$

The term $\delta(u)$ (Dirac mass) accounts for the diagonal $\gamma = \gamma'$. The density $1-\operatorname{sinc}^2$ is exactly the two-point correlation function of the **Gaussian Unitary Ensemble (GUE)** of random Hermitian matrices in the bulk scaling limit; equivalently of the CUE (unitary group with Haar measure).

A complete resolution means an unconditional proof (or disproof) of this limit. A proof conditional on RH alone would already be a landmark, since the conjecture is currently open even under RH. Disproof would follow from establishing the *alternative hypothesis* — that normalized gaps concentrate near half-integers — which is not excluded by any theorem.

## 2. Mathematical Foundations

Montgomery's analysis proceeds through the **form factor**, the Fourier-side statistic
$$F(\alpha) = F(\alpha,T) = \left(\frac{T\log T}{2\pi}\right)^{-1}\sum_{0<\gamma,\gamma'\le T} T^{\,i\alpha(\gamma-\gamma')} w(\gamma-\gamma'),\qquad w(u)=\frac{4}{4+u^2}.$$
The weight $w$ is a smooth cutoff at the scale of the mean spacing. $F$ is real, even, and $F(\alpha)\ge 0$ (it is a squared modulus after applying the explicit formula).

**Theorem (Montgomery 1973).** Assume RH. Then uniformly for $0\le \alpha \le 1-\varepsilon$,
$$F(\alpha,T) = \bigl(1+o(1)\bigr)T^{-2\alpha}\log T + \alpha + o(1) \qquad (T\to\infty).$$

**Montgomery's Strong Hypothesis.** $F(\alpha,T) = 1 + o(1)$ uniformly for $\alpha$ in bounded intervals with $1 \le \alpha \le A$, for every fixed $A$.

The link between $F$ and Section 1 is Fourier duality: for a test function $r$ with $\hat r$ of compact support,
$$\sum_{0<\gamma,\gamma'\le T} r\!\left(\frac{(\gamma-\gamma')\log T}{2\pi}\right) w(\gamma-\gamma') = \frac{T\log T}{2\pi}\int_{-\infty}^{\infty} F(\alpha)\,\hat r(\alpha)\,d\alpha .$$
Since the Fourier transform of $\operatorname{sinc}^2(u)=(\sin\pi u/\pi u)^2$ is the triangle $(1-|\alpha|)_+$, the GUE density $1-\operatorname{sinc}^2+\delta$ has transform
$$\widehat{(1-\operatorname{sinc}^2+\delta)}(\alpha) = \min(|\alpha|,1),$$
which is *exactly* $\alpha$ on $[0,1]$ (Montgomery's theorem) and $1$ beyond (the unproved part).

The arithmetic input is the explicit formula: for $x\ge 1$,
$$\sum_{\gamma}\frac{x^{i\gamma}}{1+(t-\gamma)^2} = -x^{-1/2}\sum_{n\le x}\Lambda(n)\left(\frac{x}{n}\right)^{-1/2+it} - x^{1/2}\sum_{n>x}\Lambda(n)\left(\frac{n}{x}\right)^{-3/2+it} + O(x^{1/2}),$$
so $F(\alpha)$ for $\alpha \ge 1$ is governed by correlations of the von Mangoldt function $\Lambda$ over ranges beyond the Montgomery–Vaughan mean-value range — i.e. by the Hardy–Littlewood prime $k$-tuple conjecture.

## 3. History & State of the Art (SOTA)

- **1972–73.** Montgomery presents the theorem and conjecture at the St. Louis AMS symposium; the celebrated conversation with Freeman Dyson at Princeton identifies $1-\operatorname{sinc}^2$ as the GUE two-point function (Dyson 1962; Mehta's *Random Matrices*).
- **1987–2001.** Odlyzko's computations of zeros near heights $10^{12}$, $10^{20}$, $10^{22}$ show agreement with GUE spacings to several decimal places, including nearest-neighbour spacing densities, not merely pair correlation.
- **1987.** Goldston–Montgomery prove that Montgomery's strong hypothesis is *equivalent* (under RH) to an asymptotic for the variance of primes in short intervals: $\int_1^X \bigl(\psi(x+\delta x)-\psi(x)-\delta x\bigr)^2 dx \sim \tfrac{1}{2}\delta X^2\log(1/\delta)$ in suitable ranges.
- **1994–96.** Hejhal proves the triple correlation for restricted test-function support; Rudnick–Sarnak prove $n$-level correlations for all $n$, for principal automorphic $L$-functions on $\mathrm{GL}_m/\mathbb{Q}$, again with support restrictions — GUE statistics are universal across the family.
- **1995–96.** Bogomolny–Keating derive all $n$-point correlations heuristically from the Hardy–Littlewood conjectures, showing the arithmetic lower-order terms.
- **1999–2001.** Katz–Sarnak place the conjecture in the symmetry-type framework; Conrey, Keating, Snaith and collaborators extend random-matrix predictions to moments and ratios.
- **2000–2020.** Conditional refinements of $F(\alpha)$ beyond $\alpha=1$ (Özlük; Goldston–Gonek–Özlük–Snyder), and Fourier/semidefinite optimization extracting sharper arithmetic consequences (Carneiro–Chandee–Littmann–Milinovich 2017; Chirre–Gonçalves–de Laat 2020).

## 4. Partial Results / Verified Cases

- **Support $|\alpha| \le 1$ (equivalently, test functions $r$ with $\operatorname{supp}\hat r \subseteq [-1,1]$):** proved by Montgomery under RH. This is the sole unconditional-modulo-RH case.
- **Averaged/extended ranges.** Assuming GRH for Dirichlet $L$-functions, Özlük (1996) obtained the pair correlation of zeros averaged over all Dirichlet $L$-functions with $\alpha$-support up to $2$; Goldston–Gonek–Özlük–Snyder (2000) deduced lower bounds $F(\alpha) \ge \tfrac{3}{2}-|\alpha|+o(1)$ type inequalities in $1 \le |\alpha| \le 3/2$ for $\zeta$ itself, under GRH.
- **Higher correlations.** Rudnick–Sarnak (1996): the $n$-level correlation of zeros of any principal $L$-function on $\mathrm{GL}_m/\mathbb{Q}$ matches GUE for test functions whose Fourier support lies in the region $\sum_j |\alpha_j| < 2/m$ ($m=1$: $\zeta$ and Dirichlet $L$-functions).
- **Function fields.** For curves over $\mathbb{F}_q$, Katz–Sarnak prove GUE/monodromy statistics unconditionally in the limit $q \to \infty$ using Deligne equidistribution — the conjecture's analogue is a **theorem** in that setting.
- **Numerics.** Odlyzko: $\sim 10^9$ zeros near the $10^{20}$-th and $10^{22}$-nd zero; empirical pair correlation matches $1-\operatorname{sinc}^2$ with residuals consistent with the Bogomolny–Keating arithmetic lower-order term of size $O(1/\log T)$.
- **Consequences already extracted.** Under RH + pair correlation, at least $2/3$ of zeros are simple (Montgomery 1973); improved by Cheer–Goldston (1993) and further by the Hilbert-space / semidefinite methods of Carneiro–Chandee–Littmann–Milinovich (2017) and Chirre–Gonçalves–de Laat (2020).

## 5. Principal Obstacles

- **The $\alpha > 1$ range is the prime-correlation range.** Via the explicit formula, $F(\alpha,T)$ for $\alpha>1$ requires an asymptotic for $\sum_{n\le x}\Lambda(n)\Lambda(n+h)$ uniformly for $h$ up to $x^{\theta}$ with an error saving a power of $\log$ — the Hardy–Littlewood twin-prime-type conjecture. No unconditional method (sieve, circle method, Vinogradov, dispersion) gives an asymptotic for a *single* shift $h$.
- **Diagonal/off-diagonal barrier.** Montgomery's proof works because for $\alpha<1$ the double sum is dominated by the "diagonal" $n=m$ contribution, controlled by the Montgomery–Vaughan mean value theorem. At $\alpha=1$ the off-diagonal terms become the same size; the transition point is exactly where the method has no cancellation input.
- **Positivity gives only one-sided information.** $F \ge 0$ yields lower bounds on gaps and simple-zero proportions but cannot produce the *upper* bound $F(\alpha)\le 1+o(1)$, which is where the conjecture's rigidity lives.
- **Randomness is not derivable from arithmetic.** GUE behaviour is a statement of *maximal spectral rigidity*; nothing in the Euler product forces it. The alternative hypothesis (normalized gaps $\in \tfrac12\mathbb{Z}$) is compatible with all proved cases and, by Conrey–Iwaniec, is closely tied to the existence of Landau–Siegel zeros — so ruling it out is at least as hard as a major class-number problem.
- **No spectral model.** Hilbert–Pólya remains programmatic: there is no known self-adjoint operator whose spectrum is $\{\gamma\}$, hence no route via genuine random-matrix universality theorems (Erdős–Schlein–Yau, Tao–Vu), which require an actual random matrix.

## 6. The Gap

Everything reduces to a single statement:
$$F(\alpha,T) = 1 + o(1) \quad \text{uniformly for } 1 \le \alpha \le A,\ \text{for each fixed } A>1.$$
Proved: $F(\alpha) \to \alpha$ on $[0,1]$. Conjectured: $F(\alpha)\to 1$ on $[1,\infty)$. The gap is the passage from the Montgomery–Vaughan diagonal range into the off-diagonal range, i.e. from second moments of $\Lambda$ to *shifted convolutions* of $\Lambda$. Concretely: prove
$$\sum_{n \le x} \Lambda(n)\Lambda(n+h) = \mathfrak{S}(h)\,x + O_\varepsilon\!\left(x\,(\log x)^{-B}\right)$$
with $\mathfrak{S}$ the singular series, uniformly for $1\le h\le x^{1-\varepsilon}$ — and the conjecture follows (Goldston–Montgomery, Bogomolny–Keating). No weaker arithmetic input is known to suffice.

## 7. Current Research (as of June 2026)

- **Fourier optimization / semidefinite programming.** Carneiro, Chirre, Gonçalves, Milinovich, Littmann and collaborators convert conditional pair-correlation information into optimal bounds on simple zeros, gaps, and $S(t)$ by solving extremal problems in de Branges / Paley–Wiener spaces. This is the most active line and produces steadily improved constants. *(frontier — verify: numerically improved simple-zero proportions announced in 2024–2026 preprints.)*
- **Alternative hypothesis and Landau–Siegel zeros.** Baluyot (2016) and successors quantify how much of AH survives partial pair-correlation knowledge; connections to Conrey–Iwaniec's class-number work remain the sharpest available leverage.
- **Random matrix refinements.** Bogomolny–Keating-style arithmetic corrections, and the Conrey–Farmer–Keating–Rubinstein–Snaith moment/ratios recipes, are used to predict lower-order terms in $F(\alpha)$ of size $\log^{-1}T$ and to test them numerically (Odlyzko-scale computations extended by Platt and others).
- **Function-field and large-$q$ families.** Groups at Tel Aviv (Rudnick), Bristol/Oxford (Keating, Snaith), and IMPA (Carneiro) study $\mathbb{F}_q[t]$ analogues where correlations are theorems, seeking transferable mechanisms.
- **Shifted convolutions.** Progress on averaged Chowla/Hardy–Littlewood statements (Matomäki–Radziwiłł–Tao) gives correlations *on average over $h$*; adapting these to the fixed-shift uniformity that $F(\alpha)$ demands is an open technical target. *(frontier — verify.)*

## 8. Future Work

1. Prove $F(\alpha)\ge c$ for some $c>0$ on a nontrivial interval $\alpha \in (1, 1+\eta)$ under RH alone (currently needs GRH).
2. Establish an *upper* bound $F(\alpha) \le 1 + \epsilon$ in any range $\alpha>1$; even $F(\alpha) = O(1)$ unconditionally on RH would be new information about prime correlations.
3. Eliminate the alternative hypothesis, ideally by exhibiting a positive proportion of normalized gaps in a forbidden interval such as $(0.2, 0.3)$.
4. Extend the Goldston–Montgomery equivalence into a genuine two-way transfer with the Matomäki–Radziwiłł multiplicative-functions machinery.
5. Find a spectral or dynamical model (Connes' trace formula, quantum-chaotic $xp$-type Hamiltonians of Berry–Keating) for which GUE statistics are a theorem, then match it to $\zeta$.

## 9. Key References

- **[Foundational]** H. L. Montgomery. *The pair correlation of zeros of the zeta function.* In *Analytic Number Theory* (Proc. Sympos. Pure Math. XXIV, St. Louis 1972), AMS, 1973, pp. 181–193.
- **[Foundational]** F. J. Dyson. *Statistical theory of the energy levels of complex systems. I–III.* Journal of Mathematical Physics 3 (1962), 140–156, 157–165, 166–175.
- **[Foundational]** M. L. Mehta. *Random Matrices*, 3rd edition. Elsevier/Academic Press, 2004.
- **[Computational]** A. M. Odlyzko. *On the distribution of spacings between zeros of the zeta function.* Mathematics of Computation 48 (1987), 273–308.
- **[Computational]** A. M. Odlyzko. *The $10^{22}$-nd zero of the Riemann zeta function.* In *Dynamical, Spectral, and Arithmetic Zeta Functions*, Contemporary Mathematics 290, AMS, 2001, pp. 139–144.
- **[Equivalence]** D. A. Goldston, H. L. Montgomery. *Pair correlation of zeros and primes in short intervals.* In *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70, Birkhäuser, 1987, pp. 183–203.
- **[SOTA]** Z. Rudnick, P. Sarnak. *Zeros of principal L-functions and random matrix theory.* Duke Mathematical Journal 81 (1996), 269–322.
- **[SOTA]** D. A. Hejhal. *On the triple correlation of zeros of the zeta function.* International Mathematics Research Notices 1994, no. 7, 293–302.
- **[SOTA]** D. A. Goldston, S. M. Gonek, A. E. Özlük, C. Snyder. *On the pair correlation of zeros of the Riemann zeta-function.* Proceedings of the London Mathematical Society (3) 80 (2000), 31–49.
- **[SOTA]** A. E. Özlük. *On the q-analogue of the pair correlation conjecture.* Journal of Number Theory 59 (1996), 319–351.
- **[SOTA / Recent]** E. Carneiro, V. Chandee, F. Littmann, M. B. Milinovich. *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function.* Journal für die reine und angewandte Mathematik (Crelle) 725 (2017), 143–182.
- **[SOTA / Recent]** A. Chirre, F. Gonçalves, D. de Laat. *Pair correlation estimates for the zeros of the zeta function via semidefinite programming.* Advances in Mathematics 361 (2020), 106926.
- **[SOTA / Recent]** S. Baluyot. *On the pair correlation conjecture and the alternative hypothesis.* Journal of Number Theory 169 (2016), 183–226.
- **[Heuristics]** E. B. Bogomolny, J. P. Keating. *Random matrix theory and the Riemann zeros I, II.* Nonlinearity 8 (1995), 1115–1131; 9 (1996), 911–935.
- **[Survey]** N. M. Katz, P. Sarnak. *Zeroes of zeta functions and symmetry.* Bulletin of the AMS 36 (1999), 1–26.
- **[Survey]** J. B. Conrey. *L-functions and random matrices.* In *Mathematics Unlimited — 2001 and Beyond*, Springer, 2001, pp. 331–352.
- **[Related]** J. B. Conrey, H. Iwaniec. *Spacing of zeros of Hecke L-functions and the class number problem.* Acta Arithmetica 103 (2002), 259–312.
- **[Related]** A. Y. Cheer, D. A. Goldston. *Simple zeros of the Riemann zeta-function.* Proceedings of the AMS 118 (1993), 365–372.

## 10. Worked Example / Concrete Special Case

**Task.** Verify that Montgomery's theorem on $[0,1]$ and the GUE density are literally the same statement, and compute a testable number.

*Step 1 — transform of the sinc-squared term.* With the convention $\hat f(\alpha)=\int f(u)e^{-2\pi i u\alpha}du$, the rectangle $\mathbf{1}_{[-1/2,1/2]}$ has transform $\operatorname{sinc}(\alpha)=\sin(\pi\alpha)/(\pi\alpha)$. Since convolution of the rectangle with itself is the triangle $\Lambda_{\!\triangle}(u)=(1-|u|)_+$, Plancherel/duality gives
$$\int_{-\infty}^{\infty}\left(\frac{\sin \pi u}{\pi u}\right)^2 e^{-2\pi i u \alpha}\,du = (1-|\alpha|)_+ .$$

*Step 2 — transform of the GUE pair-correlation density.* Using $\hat\delta = 1$ and $\hat 1 = \delta$,
$$\widehat{\bigl(1-\operatorname{sinc}^2+\delta\bigr)}(\alpha) = \delta(\alpha) - (1-|\alpha|)_+ + 1 .$$
Away from $\alpha=0$ this equals $1-(1-|\alpha|)_+ = \min(|\alpha|,1)$. So the GUE prediction is precisely
$$F(\alpha) = |\alpha| \ \ (|\alpha|\le 1), \qquad F(\alpha)=1 \ \ (|\alpha|\ge 1).$$
Montgomery's theorem proves the first line (the $T^{-2\alpha}\log T$ term is the $\delta(\alpha)$ diagonal mass, invisible for $\alpha$ bounded away from $0$). The second line is the conjecture. This is the cleanest formulation of the gap in Section 6.

*Step 3 — a number to test.* The predicted expected count of other zeros within one mean spacing of a given zero (on one side) is
$$\int_0^1\left(1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right)du = 1-\int_0^1\operatorname{sinc}^2(u)\,du \approx 1 - 0.4514 = 0.5486 .$$
(Simpson's rule with $h=1/4$ on $\operatorname{sinc}^2$, values $1,\ 0.8106,\ 0.4053,\ 0.0901,\ 0$, gives $0.4511$; refining gives $0.4514$.)

*Step 4 — contrast with independence.* If the normalized ordinates were a Poisson process of density $1$, the same count would be $\int_0^1 1\,du = 1$. The observed deficit — level repulsion, with density vanishing quadratically as $u\to 0$ since $1-\operatorname{sinc}^2(u)=\tfrac{\pi^2u^2}{3}+O(u^4)$ — is what Odlyzko's data at height $10^{22}$ confirms to roughly two decimal places. At height $T=10^{22}$ the mean spacing is $2\pi/\log T \approx 0.124$, so the statistic is measured over gaps of order $10^{-1}$ in $t$; the residual mismatch is of the predicted Bogomolny–Keating size $O(1/\log T)\approx 0.02$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*