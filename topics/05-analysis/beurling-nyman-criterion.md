---
id: 05-analysis/beurling-nyman-criterion
title: "Beurling-Nyman Criterion"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Beurling-Nyman Criterion

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/beurling-nyman-criterion` · **Status:** open

## 1. Problem Statement / Conjecture

The Beurling–Nyman criterion converts the Riemann Hypothesis (RH) into a **closure (density) problem in a Hilbert space**. For $\theta \in (0,1]$ set

$$\rho_\theta(t) = \left\{\frac{\theta}{t}\right\}, \qquad t > 0,$$

where $\{x\}$ is the fractional part. Each $\rho_\theta \in L^2(0,\infty)$. Let $\mathcal{B}$ be the closed linear span of $\{\rho_\theta : 0 < \theta \le 1\}$ in $L^2(0,\infty)$.

**Criterion (Nyman 1950, Beurling 1955).** RH holds if and only if $\chi_{(0,1)} \in \mathcal{B}$.

The criterion itself is a *theorem*; what is open is the **analytic problem it poses**: to prove (or refute) the approximation statement directly, without assuming RH. Concretely, in Báez-Duarte's discrete form, one must decide whether

$$d_N^2 \;=\; \inf_{c_1,\dots,c_N \in \mathbb{C}} \Big\| \chi_{(0,1)} - \sum_{k=1}^{N} c_k \rho_{1/k} \Big\|_{L^2(0,\infty)}^2 \;\longrightarrow\; 0 \quad (N \to \infty).$$

A complete solution means either an unconditional construction of coefficients $c_k = c_k(N)$ with $d_N \to 0$ (proving RH), or a proof that $\liminf d_N > 0$ (disproving it). The refined **BBLS conjecture** asserts the rate

$$\lim_{N \to \infty} d_N^2 \log N \;=\; \sum_{\rho} \frac{m_\rho^2}{|\rho|^2},$$

the sum over nontrivial zeros $\rho$ with multiplicity $m_\rho$; under RH with simple zeros this equals $2 + \gamma - \log 4\pi \approx 0.0462$.

## 2. Mathematical Foundations

**Mellin transform.** For $f \in L^2(0,\infty)$ write $\widehat{f}(s) = \int_0^\infty f(t)\, t^{s-1}\,dt$. Mellin–Plancherel is an isometry from $L^2(0,\infty)$ onto $L^2$ of the line $\Re s = \tfrac12$:

$$\|f\|_{L^2(0,\infty)}^2 = \frac{1}{2\pi} \int_{-\infty}^{\infty} \big| \widehat{f}(\tfrac12 + i\tau) \big|^2 \, d\tau .$$

**The two key transforms.** For $0 < \Re s < 1$, substituting $u = 1/t$,

$$\int_0^\infty \left\{\frac{1}{t}\right\} t^{s-1}\,dt = \int_0^\infty \{u\}\, u^{-s-1}\,du = -\frac{\zeta(s)}{s},
\qquad \int_0^\infty \chi_{(0,1)}(t)\, t^{s-1}\,dt = \frac{1}{s}.$$

By the scaling $\rho_\theta(t) = \rho_1(t/\theta)$-type dilation, $\widehat{\rho_\theta}(s) = -\theta^{s}\zeta(s)/s$.

**Reformulation on the critical line.** A finite combination $\sum_k c_k \rho_{1/k}$ has Mellin transform $-\zeta(s)D_N(s)/s$ with the Dirichlet polynomial $D_N(s) = \sum_{k \le N} c_k k^{-s}$. Hence

$$d_N^2 \;=\; \inf_{D_N} \; \frac{1}{2\pi}\int_{-\infty}^{\infty}
\Big| 1 - \zeta\big(\tfrac12+i\tau\big) D_N\big(\tfrac12+i\tau\big) \Big|^2 \, \frac{d\tau}{\tfrac14 + \tau^2}.$$

So the problem is: **how well can a Dirichlet polynomial of length $N$ mollify $1/\zeta$ on the critical line, in the weighted $L^2$ norm $d\tau/(\tfrac14+\tau^2)$?**

**Why zeros obstruct.** If $\zeta(\beta_0) = 0$ with $\beta_0 = \beta + i\gamma_0$, $\beta > \tfrac12$, then every $\widehat{f}$ with $f \in \mathcal{B}$ vanishes at $\beta_0$ (the factor $\zeta(s)$ does), while $\widehat{\chi_{(0,1)}}(\beta_0) = 1/\beta_0 \ne 0$; point evaluation at $\beta_0$ is a bounded functional on the Hardy space $H^2$ of the half-plane $\Re s > \tfrac12$, so $\chi_{(0,1)} \notin \mathcal{B}$. The converse direction — no zeros off the line implies density — is the substance of Nyman's thesis.

**Gram data.** The infimum is a finite least-squares problem with
$\langle \rho_{1/j}, \rho_{1/j}\rangle = (\log 2\pi - \gamma)/j$, and off-diagonal entries given by **Vasyunin's formula**, which expresses $\langle \rho_{1/j},\rho_{1/k}\rangle$ through $\log$, $\gamma$, and the cotangent sum
$c_0(h/k) = -\sum_{m=1}^{k-1} \frac{m}{k}\cot\!\big(\frac{\pi m h}{k}\big)$.

## 3. History & State of the Art (SOTA)

- **1950.** Bertil Nyman, in his Uppsala thesis under Beurling, proves the $L^2(0,1)$ density equivalence using the functions $\rho_\theta(t) - \theta\rho_1(t)$.
- **1955.** Arne Beurling, *A closure problem related to the Riemann zeta-function* (PNAS), gives the $L^p$ version: for $1 < p < \infty$, the span is dense in $L^p(0,1)$ iff $\zeta$ has no zeros in $\Re s > 1/p$. RH is the case $p = 2$.
- **1984.** Bercovici–Foias give an operator-theoretic restatement; **1993** Alcántara-Bode recasts it as injectivity of an explicit Hilbert–Schmidt integral operator.
- **1995.** Nikolski derives quantitative distance formulas and localizes zeros; Vasyunin computes the Gram matrix in closed form.
- **1998–2000.** Balazard–Saias and BBLS (Báez-Duarte, Balazard, Landreau, Saias) introduce the quantitative $d_N$ and formulate the $c/\log N$ conjecture.
- **2002.** Burnol proves the unconditional lower bound $\liminf_N d_N^2 \log N \ge \sum_\rho m_\rho^2/|\rho|^2$.
- **2003.** Báez-Duarte's strengthening: it suffices to use the arithmetic dilations $\theta = 1/k$, i.e. honest Dirichlet polynomials.
- **2013.** Bettin–Conrey–Farmer identify the (conditionally) optimal coefficient choice, tying the rate to twisted second moments of $\zeta$.

## 4. Partial Results / Verified Cases

- **The equivalence is a theorem**, in several forms: $L^2$ (Nyman), $L^p$ for $1<p<\infty$ with the half-plane $\Re s > 1/p$ (Beurling), the "Báez-Duarte class" with $\theta \in \{1/k\}_{k\le N}$ (2003; short proof by Bagchi 2006), and vector-valued/Selberg-class extensions (de Roton 2005) where density in $L^2$ is equivalent to the corresponding Grand RH for $L$-functions with a functional equation and Euler product.
- **Unconditional lower bound (Burnol 2002):** $\liminf_N (\log N)\, d_N^2 \ge \sum_\rho m_\rho^2 / |\rho|^2$. Under RH with simple zeros the right side is $2+\gamma-\log 4\pi \approx 0.0462$; the presence of $m_\rho^2$ means multiple zeros would strictly increase the floor.
- **Conditional upper bounds:** assuming RH plus a mild hypothesis on the zeros (simplicity together with a convergence condition on $\sum_\rho |\rho\,\zeta'(\rho)|^{-2}$), one gets $d_N^2 \ll (\log\log N)/\log N$ — off the conjectured truth by one $\log\log$. Bettin–Conrey–Farmer (2013) show that a conjectural asymptotic for the twisted second moment $\int |\zeta(\tfrac12+i\tau)|^2 (h/k)^{i\tau} w(\tau)\,d\tau$, uniform for $h,k \le N$, yields the exact constant $2+\gamma-\log 4\pi$.
- **Explicit small cases:** $d_1^2 = 1 - (1-\gamma)^2/(\log 2\pi - \gamma) \approx 0.8582$ (Section 10). Landreau–Richard (*Experimental Mathematics* 11, 2002) computed $d_N$ for $N \le 100$ using the Vasyunin Gram matrix in high precision; the values decrease but $d_N^2\log N$ remains several times the conjectured limit, consistent with a slowly decaying secondary term rather than with failure of RH.

## 5. Principal Obstacles

- **No constructive mollifier.** The natural guess $c_k = \mu(k)(1 - \log k/\log N)$ (Möbius/Selberg-type) gives $d_N^2 \asymp 1/\log N$ only *conditionally*; unconditionally, controlling $\sum_{k\le N}\mu(k)$-type sums against $\zeta$ on the critical line is exactly as hard as zero-free regions. Any unconditional bound $d_N \to 0$ would already imply RH, so no soft or compactness argument can produce it.
- **The Gram matrix is ill-conditioned.** Its eigenvalues cluster near zero at a rate that makes the least-squares solution numerically and analytically unstable; optimal coefficients grow and oscillate, and truncating or smoothing them destroys the $1/\log N$ gain.
- **Moment barrier.** The exact rate is equivalent to an asymptotic for $\int |\zeta(\tfrac12+it)|^2 (h/k)^{it}\,dt$ **uniform for $h,k$ up to $N$** — beyond the reach of current mean-value technology, which handles $h,k \le T^{\vartheta}$ with $\vartheta$ well below the required range. Classical Fourier/Plancherel arguments transport the problem faithfully but add no arithmetic input.
- **Cotangent sums are erratic.** The Vasyunin sums $c_0(h/k)$ have a distribution governed by continued-fraction behaviour of $h/k$; their large values (Maier–Rassias) obstruct uniform control of the off-diagonal Gram entries.
- **Zero-detection asymmetry.** The "RH false $\Rightarrow$ not dense" direction is a one-line Hardy-space argument; the productive direction requires *building* approximants, and no known method builds them without prior zero-free information.

## 6. The Gap

Proven: the equivalence RH $\iff d_N \to 0$, and the floor $\liminf d_N^2 \log N \ge \sum_\rho m_\rho^2/|\rho|^2$. Unproven: any unconditional upper bound of the form $d_N \le \varepsilon(N) \to 0$.

The precise missing step is a **uniform-in-shift second-moment estimate**: an asymptotic (or even a sufficiently sharp upper bound) for
$$\sum_{h,k \le N} a_h \overline{a_k} \int_{-\infty}^{\infty} \big|\zeta(\tfrac12+i\tau)\big|^2 \Big(\frac{h}{k}\Big)^{i\tau} \frac{d\tau}{\tfrac14+\tau^2}$$
valid for arbitrary coefficient vectors of length $N$, with $N$ unrestricted relative to the effective "conductor" of the weight. Every route to $d_N\to0$ passes through this quadratic form; every current technique for it inserts either RH or a zero-density input.

## 7. Current Research (as of June 2026)

- **Mollifier optimization.** Continuations of Bettin–Conrey–Farmer's programme (AIM; Genoa; Bristol) to find coefficient vectors whose error is controlled by *unconditional* twisted moments over restricted ranges, then to widen the range. Progress is incremental and range-limited. *(frontier — verify)*
- **Cotangent-sum analysis.** Bettin–Conrey reciprocity for $c_0(h/k)$ and the Maier–Rassias moment estimates are used to bound Gram off-diagonals; recent work targets the joint distribution of $c_0$ over Farey fractions. *(frontier — verify)*
- **Generalizations.** de Roton-style extensions to the Selberg class and to Dirichlet $L$-functions serve as testbeds: the same obstacle appears with $\zeta$ replaced by objects where stronger moment results exist.
- **Numerical.** Higher-precision computation of $d_N$ into the range $N \sim 10^3$ with regularized least squares, aimed at separating the conjectured $0.0462/\log N$ main term from $\log\log N/\log^2 N$-scale corrections. *(frontier — verify)*
- **Operator-theoretic.** Revivals of the Alcántara-Bode integral-operator and Bercovici–Foias invariant-subspace framings, seeking spectral criteria for injectivity that bypass moment estimates.

## 8. Future Work

- Prove an **unconditional** upper bound $d_N^2 \ll (\log N)^{-\delta}$ for some $\delta > 0$; this alone would give RH, so the realistic goal is a conditional-but-weaker hypothesis (e.g. a density hypothesis rather than RH) that suffices.
- Establish the twisted second moment uniformly for $h,k \le T^{1/2+\delta}$, extending Conrey-type results; identify the exact threshold $\vartheta$ at which the Nyman–Beurling rate follows.
- Determine whether the *sharp* constant in Burnol's bound is attained, i.e. prove the BBLS conjecture under RH alone, removing the $\log\log N$ loss.
- Exploit the $m_\rho^2$ weighting: a proof that $\liminf d_N^2\log N \le C$ for explicit $C$ would bound multiplicities of zeros — a nontrivial unconditional payoff short of RH.
- Explore whether Beurling's $L^p$ criterion for $p$ near $1$ can yield unconditional zero-free regions in $\Re s > 1/p$.

## 9. Key References

- **[Foundational]** B. Nyman. *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces.* Ph.D. thesis, University of Uppsala, 1950.
- **[Foundational]** A. Beurling. *A closure problem related to the Riemann zeta-function.* Proceedings of the National Academy of Sciences USA, 41 (1955), 312–314.
- **[Foundational]** H. Bercovici, C. Foias. *A real variable restatement of Riemann's hypothesis.* Israel Journal of Mathematics, 48 (1984), 57–68.
- **[Structural]** N. Nikolski. *Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann $\zeta$-function.* Annales de l'Institut Fourier, 45 (1995), 533–577.
- **[Structural]** V. I. Vasyunin. *On a biorthogonal system associated with the Riemann hypothesis.* Algebra i Analiz, 7 (1995), 118–135.
- **[SOTA]** L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias. *Notes sur la fonction $\zeta$ de Riemann, 3.* Advances in Mathematics, 149 (2000), 130–144.
- **[SOTA]** J.-F. Burnol. *A lower bound in an approximation problem involving the zeros of the Riemann zeta function.* Advances in Mathematics, 170 (2002), 56–70.
- **[SOTA]** L. Báez-Duarte. *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis.* Atti della Accademia Nazionale dei Lincei, Rendiconti Lincei Matematica e Applicazioni, 14 (2003), 5–11.
- **[SOTA]** S. Bettin, J. B. Conrey, D. W. Farmer. *An optimal choice of Dirichlet polynomials for the Nyman–Beurling criterion.* Proceedings of the Steklov Institute of Mathematics, 280 (2013), 30–36.
- **[Computational]** B. Landreau, F. Richard. *Le critère de Beurling et Nyman pour l'hypothèse de Riemann: aspects numériques.* Experimental Mathematics, 11 (2002), 349–360.
- **[Survey]** M. Balazard, E. Saias. *The Nyman–Beurling equivalent form for the Riemann hypothesis.* Expositiones Mathematicae, 18 (2000), 131–138.
- **[Survey]** B. Bagchi. *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis.* Proceedings of the Indian Academy of Sciences (Mathematical Sciences), 116 (2006), 137–146.
- **[Related]** J. Alcántara-Bode. *An integral equation formulation of the Riemann hypothesis.* Integral Equations and Operator Theory, 17 (1993), 151–168.
- **[Related]** A. de Roton. *Généralisation du critère de Beurling–Nyman pour l'hypothèse de Riemann.* Transactions of the American Mathematical Society, 357 (2005), 4425–4443.

## 10. Worked Example / Concrete Special Case

**Compute $d_1$ exactly.** Take $N = 1$: approximate $\chi_{(0,1)}$ by a single multiple of $\rho_1(t) = \{1/t\}$.

*Norm of $\rho_1$.* Split at $t=1$. For $t > 1$, $\{1/t\} = 1/t$, so $\int_1^\infty t^{-2}dt = 1$. For $t \in (0,1)$, substitute $u = 1/t$:
$$\int_0^1 \{1/t\}^2 dt = \int_1^\infty \frac{\{u\}^2}{u^2}\,du = \log(2\pi) - \gamma - 1 \approx 0.260661 .$$
Hence $\|\rho_1\|^2 = \log(2\pi) - \gamma \approx 1.260661$.

*Inner product.* $\langle \chi_{(0,1)}, \rho_1\rangle = \int_0^1 \{1/t\}\,dt = 1 - \gamma \approx 0.422784$.

*Least squares.* The optimal coefficient is
$$c^{*} = \frac{1-\gamma}{\log 2\pi - \gamma} \approx 0.335372,$$
and
$$d_1^2 = \|\chi_{(0,1)}\|^2 - \frac{|\langle \chi_{(0,1)},\rho_1\rangle|^2}{\|\rho_1\|^2}
= 1 - \frac{(1-\gamma)^2}{\log 2\pi - \gamma} \approx 1 - 0.141788 = 0.858212,$$
so $d_1 \approx 0.9264$.

**Reading it on the critical line.** With $D_1(s) = c$, the Mellin picture says
$$d_1^2 = \inf_{c}\ \frac{1}{2\pi}\int_{-\infty}^{\infty} \big|1 - c\,\zeta(\tfrac12+i\tau)\big|^2 \frac{d\tau}{\tfrac14+\tau^2},$$
i.e. we are approximating the constant $1$ by a scalar multiple of $\zeta$ itself. Since $\zeta$ vanishes at every critical zero, the error is at least $1$ near each zero height, and the weight $(\tfrac14+\tau^2)^{-1}$ concentrates mass near $\tau=0$ — which is why a single term captures only about $14\%$ of the norm.

**The scale of the problem.** The conjectured asymptotic $d_N^2 \approx 0.0462/\log N$ needs $N$ with $\log N \approx 0.0462/0.01 \approx 4.6$, i.e. $N \approx 100$, merely to reach $d_N^2 \approx 0.01$; and $d_N^2 \le 10^{-3}$ requires $N \approx e^{46} \approx 10^{20}$. The decay is logarithmic, so no computation can be convincing on its own — this is the concrete reason the criterion, though elementary to state, resists both numerical and constructive attack.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*