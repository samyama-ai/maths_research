---
id: 05-analysis/density-hypothesis
title: "Density Hypothesis"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Density Hypothesis

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/density-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

For $\tfrac12 \le \sigma \le 1$ and $T \ge 2$, let
$$N(\sigma,T) \;=\; \\#\{\rho = \beta+i\gamma : \zeta(\rho)=0,\ \beta \ge \sigma,\ 0 < \gamma \le T\},$$
counted with multiplicity, where $\zeta$ is the Riemann zeta function.

**Density Hypothesis (DH).** For every $\varepsilon>0$, uniformly in $\sigma \in [\tfrac12,1]$,
$$N(\sigma,T) \;\ll_\varepsilon\; T^{2-2\sigma+\varepsilon}.$$

A proof must supply the bound for *all* $\sigma$ in the closed interval, with the implied constant depending only on $\varepsilon$. A disproof requires exhibiting $\sigma_0 \in (\tfrac12,1)$, $\delta>0$ and an unbounded sequence $T_j \to \infty$ with $N(\sigma_0,T_j) \gg T_j^{2-2\sigma_0+\delta}$.

DH is strictly weaker than the Riemann Hypothesis (RH), which gives $N(\sigma,T)=0$ for $\sigma>\tfrac12$, and strictly weaker than the Lindelöf Hypothesis, which implies DH. It is nonetheless open, and it already yields the RH-quality consequence $p_{n+1}-p_n \ll p_n^{1/2+\varepsilon}$ for consecutive primes.

## 2. Mathematical Foundations

**Zero counting.** By the Riemann–von Mangoldt formula the total zero count in the critical strip up to height $T$ is
$$N(T)=N(\tfrac12,T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T),$$
so $N(\tfrac12,T) \asymp T\log T \ll T^{1+\varepsilon}$: DH holds trivially at $\sigma=\tfrac12$, and trivially at $\sigma=1$ since $\zeta(1+it)\neq0$. The content lies in the interior, where the "trivial" bound is $N(\sigma,T)\le N(T) \ll T\log T$ and DH demands a power saving $T^{1-2(\sigma-1/2)}$ that is *linear* in $\sigma$ on a log-scale.

**Shape of the conjecture.** Writing $N(\sigma,T)\ll T^{A(\sigma)(1-\sigma)+\varepsilon}$, DH is the assertion $A(\sigma)\le 2$ for all $\sigma$. Montgomery's stronger *density conjecture* asserts $N(\sigma,T)\ll T^{1-\sigma+\varepsilon}$, i.e. $A(\sigma)\le 1$.

**Zero detection.** All known approaches convert zeros into large values of Dirichlet polynomials. With $M_X(s)=\sum_{n\le X}\mu(n)n^{-s}$, the product $\zeta(s)M_X(s)$ is close to $1$; a zero $\rho$ with $\beta\ge\sigma$ forces
$$\Big|\sum_{X< n \le N} a_n n^{-\rho}\Big| \;\gg\; 1$$
for a suitable smoothed coefficient sequence $a_n$ with $|a_n|\le d(n)$. Hence
$$N(\sigma,T)\;\ll\; \log^{O(1)}T \cdot \max_{N} R(N,V),$$
where $R(N,V)$ counts $1$-separated $t_1<\dots<t_R$ in $[0,T]$ with $\big|\sum_{n\sim N}a_n n^{-it_r}\big|\ge V$ and $V \approx N^{1-\sigma}$.

**Large-value machinery.** The Halász–Montgomery inequality, in Huxley's form, gives for $|a_n|\le1$ and $G=\sum_{n\sim N}|a_n|^2 \asymp N$:
$$R(N,V) \;\ll\; \big(GNV^{-2} + G^{3}TV^{-6}\big)\log^{2}T .$$
Feeding the first term alone would give DH; the second ("$V^{-6}$") term is the obstruction, and it is exactly here that all progress since 1972 has been made.

**Moment input.** Ingham's route uses the fourth moment $\int_0^T|\zeta(\tfrac12+it)|^4dt \ll T\log^4 T$. In general, if $\mu(\tfrac12)$ denotes the Lindelöf exponent, $\zeta(\tfrac12+it)\ll t^{\mu(1/2)+\varepsilon}$, then $\mu(\tfrac12)=0$ (Lindelöf) implies DH; conversely DH does not imply Lindelöf.

## 3. History & State of the Art (SOTA)

- **1937–1942 (Bohr–Landau, Carlson, Selberg).** Carlson's $N(\sigma,T)\ll T^{4\sigma(1-\sigma)}\log T$ was the first power saving; Selberg (1946) obtained $N(\sigma,T)\ll T^{1-\frac14(\sigma-1/2)}\log T$, strong near $\sigma=\tfrac12$.
- **1940 (Ingham).** $N(\sigma,T)\ll T^{\frac{3(1-\sigma)}{2-\sigma}}\log^{5}T$, i.e. $A(\sigma)=3/(2-\sigma)$; this equals $2$ only at $\sigma=\tfrac12$. It gives $A\le 12/5$ on $[\tfrac34,1]$ and stood as the record on part of that range for 84 years.
- **1969–1972 (Halász, Montgomery, Huxley).** The large-value method yields Huxley's $N(\sigma,T)\ll T^{\frac{3(1-\sigma)}{3\sigma-1}}\log^{44}T$, which beats DH exactly when $\sigma\ge\tfrac56$.
- **1977–1979 (Jutila, Heath-Brown).** Reflection and higher-moment techniques push DH down to $\sigma\ge 11/14 \approx 0.7857$.
- **2000 (Bourgain).** Combining Huxley subdivision, the Halász–Montgomery method and $\ell^2$-decoupling-style ideas, DH is established for $\sigma\ge 25/32 = 0.78125$.
- **2023 (Tao–Trudgian–Yang).** A systematic optimization over exponent pairs, large-value and additive-energy estimates, improving $A(\sigma)$ at many intermediate $\sigma$; accompanied by the Analytic Number Theory Exponent Database.
- **2024 (Guth–Maynard).** A genuinely new large-value estimate for Dirichlet polynomials near $V\approx N^{3/4}$ gives
$$N(\sigma,T)\ll T^{\frac{30}{13}(1-\sigma)+o(1)} \quad (\tfrac34\le\sigma\le1),$$
replacing Ingham's $12/5=2.4$ by $30/13\approx 2.3077$. Still $>2$, so DH itself is untouched, but the consequence $p_{n+1}-p_n \ll p_n^{17/30+\varepsilon}$ improves Huxley's $7/12$.

## 4. Partial Results / Verified Cases

| Range of $\sigma$ | Status | Source |
|---|---|---|
| $\sigma=\tfrac12$ | DH true (trivially, $N(T)\asymp T\log T$) | Riemann–von Mangoldt |
| $\sigma=1$ | DH true ($N(1,T)=0$) | Hadamard–de la Vallée Poussin |
| $\sigma\ge 5/6\approx 0.8333$ | DH proved | Huxley (1972) |
| $\sigma\ge 11/14\approx 0.7857$ | DH proved | Jutila (1977) |
| $\sigma\ge 25/32 = 0.78125$ | DH proved (current record threshold) | Bourgain (2000) |
| $\tfrac34\le\sigma<25/32$ | Best known $A(\sigma)=30/13$ | Guth–Maynard (2024) |
| $\tfrac12<\sigma<\tfrac34$ | Best known interpolation of Ingham/Selberg/Huxley/TTY bounds | various |

Additional verified settings: DH-type bounds hold **on average over families** — for Dirichlet $L$-functions the Bombieri–Gallagher–Montgomery–Huxley log-free density estimates $\sum_{q\le Q}\sum_{\chi \bmod q}^{*} N(\sigma,T,\chi) \ll (Q^2T)^{c(1-\sigma)}$ hold with $c=2$ for all $\sigma\in[\tfrac12,1]$, i.e. the *averaged* density hypothesis is a theorem. Under RH or under Lindelöf, DH follows immediately. Numerically, the first $\sim 10^{13}$ zeros (Gourdon 2004) all lie on $\sigma=\tfrac12$, so DH is verified in every computed range with room to spare.

## 5. Principal Obstacles

- **The $V^{-6}$ term.** In the Halász–Montgomery bound, the term $G^{3}TV^{-6}$ dominates precisely when $N$ is small relative to $T$ — the range $N \approx T^{1/2}$ to $T$ that matters for $\sigma$ near $\tfrac34$. Reducing the exponent $6$ requires genuinely new information about the additive structure of $\{\log n\}$, not just $L^2$ orthogonality.
- **$L^2$ methods are lossy.** Montgomery's argument is essentially a Bessel/almost-orthogonality inequality: it treats the $R$ points $t_r$ as arbitrary well-separated points. It is sharp for *some* coefficient sequences (e.g. $a_n$ mimicking a multiplicative character), so it cannot be improved without using that the coefficients come from $\zeta M_X$.
- **No extremal example.** The bound $T^{2-2\sigma}$ is not known to be attained; the conjecture is calibrated to what the second-moment term alone gives, and there is no structural reason forcing $A(\sigma)=2$ rather than $A(\sigma)=1$ (Montgomery). The absence of a plausible near-extremiser deprives the field of a target to imitate.
- **Fourier-analytic barriers.** Bourgain's and Guth–Maynard's advances come from incidence geometry and decoupling. Decoupling for the moment curve loses at exactly the critical exponent, and the transition regions ($V \approx N^{3/4}$) are where sharp $\ell^2$-decoupling gives no surplus.
- **Zero repulsion is unavailable.** Techniques that would exploit repulsion between zeros off the line (as in Deuring–Heilbronn for exceptional zeros) do not apply to a single $\zeta$; there is no family to average over.

## 6. The Gap

Proven: $A(\sigma)\le 2$ for $\sigma\ge 25/32$ and for $\sigma=\tfrac12$. Conjectured: $A(\sigma)\le 2$ throughout. The gap is the open interval
$$\tfrac12 < \sigma < \tfrac{25}{32},$$
with the hardest point near $\sigma \approx \tfrac34$, where the current record is $A = 30/13 \approx 2.308$ against a target of $2$ — a shortfall of about $13\%$ in the exponent.

Concretely, the missing step is a large-value theorem of the form: for $|a_n|\le 1$, $N \asymp T^{\theta}$ with $\theta\in(\tfrac12,1)$, and $V=N^{1-\sigma}$,
$$R(N,V) \;\ll\; N^{o(1)}\big(N^{2}V^{-2} + T\,N^{?}V^{-?}\big)$$
in which the second term never exceeds $T^{2-2\sigma}$. Equivalently: prove that a Dirichlet polynomial of length $N$ can be large ($\ge N^{1/4}$, say) on at most $\approx N^{3/2}$ separated points of an interval of length $N^{2}$.

## 7. Current Research (as of June 2026)

- **Guth–Maynard programme (MIT / Oxford).** The 2024 large-value estimate is being extended: work on other exponent ranges, on Dirichlet $L$-functions, and on removing the restriction $\sigma\ge\tfrac34$. Whether the method can be iterated to reach $A=2$ near $\sigma=\tfrac34$ is the central question. *(frontier — verify)*
- **Systematic optimisation (Tao, Trudgian, Yang; UCLA / UNSW Canberra).** The Analytic Number Theory Exponent Database mechanises the combination of exponent pairs, large-value theorems, additive-energy bounds and zero-density estimates, producing incremental improvements to $A(\sigma)$ on subintervals and certifying which classical inputs are binding. *(frontier — verify)*
- **Decoupling and incidence geometry (Bourgain school; Demeter, Guth, Maynard, Zahl).** Treating $\{n^{-it}\}$ as points on a moment-type curve and applying $\ell^2$-decoupling / Kakeya-type incidence bounds.
- **Additive energy of large-value sets.** Bounding $E(\{t_r\})$ and using Heath-Brown's higher-moment identities to break the $V^{-6}$ term.
- **Explicit and numerically effective density estimates.** Kadiri, Lumley, Ng, Platt and collaborators produce explicit constants in $N(\sigma,T)$ bounds for use in explicit prime-counting results.

## 8. Future Work

- Prove a **sharp large-value theorem at the critical scale** $N=T^{1/2}$, $V=N^{3/4}$; this single case is expected to unlock $\sigma$ near $\tfrac34$.
- Exploit the **multiplicative structure of $a_n$** (they arise from $\mu * 1$-type convolutions) rather than treating them as arbitrary bounded coefficients — a direction repeatedly urged by Montgomery and by Iwaniec–Kowalski.
- Transfer **decoupling gains from the moment curve** $(t,t^2,\dots,t^k)$ to the "$\log n$" phase setting, where the frequencies are neither equally spaced nor algebraically structured.
- Attack **Montgomery's stronger conjecture $A\le1$** on the range $\sigma$ close to $1$, where the truth is presumably far from $2$ and current bounds are far from optimal.
- Develop a **conditional taxonomy**: identify the weakest subconvexity or moment input ($\int_0^T|\zeta(\tfrac12+it)|^{2k}dt \ll T^{1+\varepsilon}$ for which $k$?) that already yields DH.

## 9. Key References

- **[Foundational]** A. E. Ingham. *On the estimation of $N(\sigma,T)$.* Quarterly Journal of Mathematics (Oxford) 11 (1940), 291–292.
- **[Foundational]** A. Selberg. *Contributions to the theory of the Riemann zeta-function.* Archiv for Mathematik og Naturvidenskab B 48 (1946), 89–155.
- **[Foundational]** H. L. Montgomery. *Topics in Multiplicative Number Theory.* Lecture Notes in Mathematics 227, Springer, 1971.
- **[Foundational]** M. N. Huxley. *On the difference between consecutive primes.* Inventiones Mathematicae 15 (1972), 164–170.
- **[Partial results]** M. Jutila. *Zero-density estimates for $L$-functions.* Acta Arithmetica 32 (1977), 55–62.
- **[Partial results]** D. R. Heath-Brown. *Zero density estimates for the Riemann zeta-function and Dirichlet $L$-functions.* Journal of the London Mathematical Society (2) 19 (1979), 221–232.
- **[Partial results]** J. Bourgain. *On large values estimates for Dirichlet polynomials and the density hypothesis for the Riemann zeta function.* International Mathematics Research Notices 2000, no. 3, 133–146.
- **[SOTA / Recent]** L. Guth and J. Maynard. *New large value estimates for Dirichlet polynomials.* arXiv:2405.20552, 2024.
- **[SOTA / Recent]** T. Tao, T. Trudgian and A. Yang. *New exponent pairs, zero density estimates, and zero additive energy estimates: a systematic approach.* arXiv:2306.05599, 2023.
- **[Survey]** A. Ivić. *The Riemann Zeta-Function: Theory and Applications.* Wiley, 1985; reprinted Dover, 2003 (Chapters 11–12 on density theorems).
- **[Survey]** E. C. Titchmarsh. *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford University Press, 1986 (Chapter IX).
- **[Survey]** H. Iwaniec and E. Kowalski. *Analytic Number Theory.* AMS Colloquium Publications 53, 2004 (Chapters 9–10).

## 10. Worked Example / Concrete Special Case

**Goal: turn a density exponent into a prime-gap exponent.**

Ingham's transfer theorem: if $N(\sigma,T)\ll T^{A(1-\sigma)}\log^{c}T$ uniformly for $\tfrac12\le\sigma\le1$, then for every $\varepsilon>0$,
$$\psi(x+y)-\psi(x) \sim y \quad \text{for } y = x^{\theta},\ \theta = 1-\tfrac{1}{A}+\varepsilon,$$
where $\psi$ is the Chebyshev function. Sketch: the explicit formula gives
$$\psi(x+y)-\psi(x) = y - \sum_{|\gamma|\le T}\frac{(x+y)^{\rho}-x^{\rho}}{\rho} + O\!\Big(\frac{x\log^2 x}{T}\Big),$$
and $|(x+y)^\rho - x^\rho| \le y\,x^{\beta-1}$. Splitting the zeros by $\beta \in [\sigma,\sigma+d\sigma]$ and integrating by parts against $N(\sigma,T)$,
$$\sum_{|\gamma|\le T} y\,x^{\beta-1} \;\ll\; y\,\log^{c+1} T \max_{1/2\le\sigma\le1} x^{\sigma-1}T^{A(1-\sigma)} = y\log^{c+1}T \max_{\sigma}\big(T^{A}x^{-1}\big)^{1-\sigma}.$$
The maximum is $o(1)$ provided $T^{A} \le x^{1-\varepsilon}$, i.e. $T = x^{(1-\varepsilon)/A}$. The error term $x\log^2x/T = o(y)$ then needs $y \ge x^{1-1/A+\varepsilon}$.

**Numbers.**

| $A$ | source | $\theta = 1-1/A$ | prime gap |
|---|---|---|---|
| $3/(2-\sigma)\le 12/5=2.4$ | Ingham 1940 | $1-5/12 = 7/12 \approx 0.5833$ | $p_{n+1}-p_n \ll p_n^{7/12+\varepsilon}$ |
| $30/13\approx 2.3077$ | Guth–Maynard 2024 | $1-13/30 = 17/30 \approx 0.5667$ | $p_{n+1}-p_n \ll p_n^{17/30+\varepsilon}$ |
| $2$ | **Density Hypothesis** | $1-1/2 = 1/2$ | $p_{n+1}-p_n \ll p_n^{1/2+\varepsilon}$ |
| $1$ | Montgomery's conjecture | $0$ | intervals of length $x^{\varepsilon}$ |

So the entire distance between the unconditional record and RH-strength prime gaps is the reduction of $A$ from $30/13$ to $2$.

**Sanity check at $\sigma=3/4$, $T=10^{6}$.** DH predicts $N(3/4,10^{6}) \ll (10^{6})^{1/2+\varepsilon} = 10^{3+6\varepsilon}$; Guth–Maynard give $\ll 10^{6\cdot 30/52} \approx 10^{3.46}$; the trivial bound is $N(10^6)\approx 1.75\times10^{6}$. All three are consistent with the computational fact that $N(3/4,10^6)=0$ (every zero to height $10^6$ is on the critical line), which is far stronger than any of them — the difficulty is entirely one of proof, not of plausibility.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*