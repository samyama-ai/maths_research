---
id: 09-probability/expected-number-of-real-roots-of-random-polynomials
title: "Expected Number of Real Roots of Random Polynomials"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Expected Number of Real Roots of Random Polynomials

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/expected-number-of-real-roots-of-random-polynomials` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\xi_0,\dots,\xi_n$ be independent identically distributed real random variables and let
$$P_n(x)=\sum_{k=0}^{n}\xi_k x^{k}.$$
Let $N_n$ denote the number of real roots of $P_n$. The problem is to determine the asymptotics of $\mathbb{E}N_n$, its fluctuations, and its large-deviation behaviour, as a function of the coefficient law and of the deterministic scaling profile applied to the coefficients.

Three linked questions:

1. **Expectation and universality.** Is $\mathbb{E}N_n=\tfrac{2}{\pi}\log n + C + o(1)$ with the *same* constant $C=0.6257358072\ldots$ for every mean-zero, unit-variance coefficient law with enough moments (and, more strongly, for the Rademacher law $\xi_k=\pm1$)?
2. **Fluctuations.** Does $N_n$ satisfy a central limit theorem with $\operatorname{Var}N_n\sim \tfrac{4}{\pi}\bigl(1-\tfrac{2}{\pi}\bigr)\log n$ universally?
3. **Persistence.** Is $\mathbb{P}(N_n=0)=n^{-b+o(1)}$ with an explicit exponent $b$, and is $b$ universal?

A complete resolution requires, for each question, either a proof valid for a stated class of coefficient laws or an explicit counterexample law. Items (1) and (2) are now theorems for broad non-Gaussian classes; item (3) is a theorem in the Gaussian case with $b=3/4$ and open in general. Hence the status **solved-recently** with residual open ends recorded in Sections 5–6.

## 2. Mathematical Foundations

**Kac–Rice formula.** For a smooth centred Gaussian process $X$ on an interval with covariance $K(x,y)=\mathbb{E}[X(x)X(y)]$ and $\operatorname{Var}X(x)>0$, the expected number of zeros in $I$ is
$$\mathbb{E}\,N(I)=\int_I \rho(x)\,dx,\qquad \rho(x)=\frac{1}{\pi}\sqrt{\partial_x\partial_y \log K(x,y)\big|_{y=x}} .$$

**Kac ensemble.** For $\xi_k\sim\mathcal{N}(0,1)$ i.i.d., $K(x,y)=\sum_{k=0}^n (xy)^k=\frac{1-(xy)^{n+1}}{1-xy}$, giving the exact density
$$\rho_n(x)=\frac{1}{\pi}\sqrt{\frac{1}{(1-x^2)^2}-\frac{(n+1)^2x^{2n}}{(1-x^{2n+2})^2}},$$
and $\mathbb{E}N_n=2\int_0^\infty \rho_n(x)\,dx$ by the symmetry $x\mapsto 1/x$. As $n\to\infty$, $\rho_n(x)\to \frac{1}{\pi|1-x^2|}$ pointwise for $|x|\ne1$; the logarithmic divergence at $x=\pm1$, cut off at scale $1/n$, produces the $\frac{2}{\pi}\log n$ term. Kac's theorem:
$$\mathbb{E}N_n=\frac{2}{\pi}\log n+C+o(1),\qquad C=0.6257358072\ldots$$

**Other scalings.** With $\xi_k\sim\mathcal{N}(0,\sigma_k^2)$:

- **Kostlan / elliptic:** $\sigma_k^2=\binom{n}{k}$ gives $K(x,y)=(1+xy)^n$ and $\mathbb{E}N_n=\sqrt{n}$ *exactly* (Edelman–Kostlan). This is the $O(n+1)$-invariant ensemble.
- **Weyl / flat:** $\sigma_k^2=1/k!$ gives $\mathbb{E}N_n\sim \tfrac{2}{\pi}\sqrt{n}$.
- **Random trigonometric:** $\sum_{k\le n}(a_k\cos kx+b_k\sin kx)$ on $[0,2\pi]$ has $\mathbb{E}N_n\sim 2n/\sqrt{3}$.

**Persistence.** For the Gaussian Kac ensemble, $p_n:=\mathbb{P}(N_n=0)$. Under the change of variables $x=e^{-t}$ the process becomes asymptotically stationary in $t$ with correlator $\operatorname{sech}$-type decay, and $p_n=n^{-b+o(1)}$ with $b=4\theta$, $\theta$ the persistence exponent of the $2$-dimensional diffusion equation with random initial data.

## 3. History & State of the Art (SOTA)

- **1932–1939.** Bloch–Pólya count real roots for coefficients uniform in $\{-1,0,1\}$, obtaining $O(\sqrt{n})$. Littlewood and Offord (1938–1939) prove $N_n=O(\log^2 n)$ with high probability and $\gg \log n/\log\log n$, for Gaussian, Bernoulli, and uniform coefficients.
- **1943.** Kac derives the exact integral formula and $\mathbb{E}N_n\sim\frac{2}{\pi}\log n$ for Gaussian coefficients.
- **1956.** Erdős and Offord prove $N_n=\frac{2}{\pi}\log n(1+o(1))$ in probability for Rademacher coefficients — the first non-Gaussian result.
- **1971.** Ibragimov and Maslova extend the expectation asymptotic $\frac{2}{\pi}\log n+o(\log n)$ to all mean-zero laws in the domain of attraction of the normal law, and treat non-centred coefficients (where the constant halves to $\frac{1}{\pi}\log n$).
- **1974.** Maslova establishes $\operatorname{Var}N_n\sim\frac{4}{\pi}(1-\frac2\pi)\log n$ and a CLT for $N_n$ in the mean-zero case.
- **1988.** Wilkins gives the full asymptotic expansion $\mathbb{E}N_n=\frac{2}{\pi}\log n+C+\sum_{p\ge1}A_p n^{-p}$ in the Gaussian case, sharpening the $o(1)$.
- **1995.** Edelman and Kostlan's *Bulletin* survey unifies the computations geometrically: the zero density is $1/\pi$ times the speed of the curve $x\mapsto(\sigma_0,\sigma_1x,\dots,\sigma_nx^n)$ projected to the sphere; the Kostlan identity $\mathbb{E}N_n=\sqrt n$ falls out in one line.
- **2002.** Dembo, Poonen, Shao and Zeitouni prove $p_n=n^{-b+o(1)}$ with $b=4\theta$ and $b\in(0.4,2)$, plus the "few roots" analogue.
- **2015–2021.** Tao–Vu (local universality), Do–Nguyen–Vu, and Nguyen–Vu upgrade Erdős–Offord to sharp universality: $\mathbb{E}N_n=\frac{2}{\pi}\log n+C+o(1)$ and a CLT for general coefficient laws with finite $(2+\varepsilon)$-moments.
- **2018.** Poplavskyi and Schehr obtain the exact $2$d-diffusion persistence exponent $\theta=3/16$, hence $b=3/4$ for the Gaussian Kac ensemble.

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| Gaussian Kac, $\sigma_k=1$ | $\mathbb{E}N_n=\frac2\pi\log n+C+\frac{A_1}{n}+\cdots$ (Kac 1943; Wilkins 1988) |
| Kostlan, $\sigma_k^2=\binom nk$ | $\mathbb{E}N_n=\sqrt n$ exactly, all $n\ge1$ |
| Weyl, $\sigma_k^2=1/k!$ | $\mathbb{E}N_n=\frac{2}{\pi}\sqrt n\,(1+o(1))$ |
| $\sigma_k=k^{\alpha}$, $\alpha>-1/2$ | $\mathbb{E}N_n=\bigl(\frac{2}{\pi}\sqrt{2\alpha+1}+o(1)\bigr)\log n$ (Do–Nguyen–Vu, 2018) |
| Rademacher $\pm1$ | $\mathbb{E}N_n=\frac2\pi\log n+C+o(1)$ (Do–Nguyen–Vu 2015; Nguyen–Vu 2021) |
| Any $\xi$ with $\mathbb{E}\xi=0$, $\mathbb{E}\xi^2=1$, $\mathbb{E}|\xi|^{2+\varepsilon}<\infty$ | same expansion; CLT with $\operatorname{Var}N_n\sim\frac{4}{\pi}(1-\frac2\pi)\log n$ |
| Non-centred, $\mathbb{E}\xi\ne0$ | $\mathbb{E}N_n=\frac1\pi\log n+O(1)$ (Ibragimov–Maslova) |
| Gaussian persistence | $\mathbb{P}(N_n=0)=n^{-3/4+o(1)}$; $\mathbb{P}(N_n\le k)$ analogues for fixed $k$ |
| Trigonometric, general i.i.d. | $\mathbb{E}N_n\sim 2n/\sqrt3$ under a weak Cramér condition (Angst–Poly; Flasche) |
| Trigonometric variance | *not* universal — depends on the fourth moment (Bally–Caramellino–Poly, 2019) |

## 5. Principal Obstacles

- **No Kac–Rice outside the Gaussian world.** For discrete coefficients $P_n(x)$ has an atomic law; the Kac–Rice density does not exist, so every non-Gaussian proof must run through comparison rather than through an exact formula.
- **The comparison window is narrow.** Universality proofs partition $\mathbb{R}$ into $\sim\log n$ dyadic windows and apply a Lindeberg swap inside each. Near $|x|=1$ the polynomial's effective number of contributing coefficients is $\Theta(n)$ and the anticoncentration needed is at scale $n^{-1/2}$ — precisely the Littlewood–Offord regime, where sharpness is delicate for lattice laws.
- **Repulsion estimates.** Controlling $\mathbb{E}N_n$ to $o(1)$ requires ruling out clusters of near-multiple roots, i.e. bounds on $\mathbb{P}(|P_n(x)|,|P_n'(x)|$ both small$)$, a two-dimensional small-ball problem that resists standard Esseen inequalities for heavy-tailed or lattice $\xi$.
- **Persistence is not a local statistic.** $\{N_n=0\}$ is a global event of probability $n^{-3/4}$; local universality (Tao–Vu) is blind to events of polynomially small probability, and the Gaussian proof uses an exactly solvable Pfaffian/Fredholm structure with no known discrete analogue.
- **Variance is fragile.** The trigonometric counterexample shows the variance constant can depend on $\mathbb{E}\xi^4$. So no soft argument can deliver variance universality; one must compute the fourth-order cumulant explicitly per model.

## 6. The Gap

Proven: the expectation expansion and the CLT for i.i.d. coefficients with $2+\varepsilon$ moments; the persistence exponent $b=3/4$ for Gaussian coefficients.

Not proven:

1. **Persistence universality.** Is $\mathbb{P}(N_n=0)=n^{-3/4+o(1)}$ for Rademacher coefficients? Even $b$ existing for a non-Gaussian law is open. The barrier is that the Gaussian derivation of $\theta=3/16$ uses the integrable structure of the associated real Ginibre-type kernel.
2. **Minimal moment hypothesis.** Does the expansion survive $\mathbb{E}\xi^2=\infty$ (stable laws)? Ibragimov–Maslova cover domains of attraction of the normal law only at the $o(\log n)$ level.
3. **Second-order term for general scalings.** For $\sigma_k=k^\alpha$ only the leading constant is known; the analogue of Wilkins' constant $C(\alpha)$ is not identified.
4. **Rate of convergence in the CLT.** No Berry–Esseen bound with an explicit power of $\log n$ is known.

## 7. Current Research (as of June 2026)

- **Universality of global statistics.** Groups around Van Vu (Yale), Hoi Nguyen (Ohio State) and Oanh Nguyen (Brown) push Lindeberg exchange toward events of polynomially small probability, aiming at persistence universality. *(frontier — verify)*
- **Cumulant methods for Gaussian fields.** Ancona and Letendre (ENS Lyon), and Louis Gass, develop cumulant asymptotics for zero counts of stationary Gaussian processes, yielding CLTs and moment expansions for Kostlan and trigonometric ensembles.
- **Integrable probability.** Schehr, Majumdar, Poplavskyi and collaborators (LPTMS Orsay, King's College London) extend the diffusion-persistence correspondence to truncated real Ginibre matrices and to $\sigma_k=k^\alpha$ families, seeking a formula $b(\alpha)$. *(frontier — verify)*
- **Real algebraic geometry.** Gayet, Welschinger, Lerario and Stecconi study the expected topology of random real hypersurfaces; the $\sqrt n$ Kostlan count is the one-dimensional shadow of the $n^{d/2}$ expected Betti numbers.
- **Random polynomials over $p$-adic and function fields**, and roots of random polynomials with dependent coefficients (random matrix characteristic polynomials), are active adjacent directions.

## 8. Future Work

- Transfer the exact exponent $3/16$ to discrete coefficient laws by building a swapping scheme adapted to rare events, e.g. through a coupling of the Kac process with the diffusive field at scale $\log n$.
- Compute the fourth cumulant of $N_n$ for the Kac ensemble to obtain a Berry–Esseen rate, following the trigonometric-polynomial template.
- Determine $C(\alpha)$ for the polynomial-growth scalings, extending Wilkins' expansion.
- Extend to random polynomial *systems*: expected number of real solutions of $m$ Kostlan equations in $m$ variables is $n^{m/2}$; the analogue for non-Gaussian systems is open.
- Study the number of real roots of $P_n$ restricted to shrinking intervals near $\pm1$, where the local scaling limit is a non-explicit stationary Gaussian process.

## 9. Key References

- **[Foundational]** M. Kac. *On the average number of real roots of a random algebraic equation.* Bulletin of the American Mathematical Society, 49:314–320, 1943.
- **[Foundational]** J. E. Littlewood and A. C. Offord. *On the number of real roots of a random algebraic equation.* Journal of the London Mathematical Society, 13:288–295, 1938.
- **[Foundational]** P. Erdős and A. C. Offord. *On the number of real roots of a random algebraic equation.* Proceedings of the London Mathematical Society, 6:139–160, 1956.
- **[Foundational]** I. A. Ibragimov and N. B. Maslova. *The mean number of real zeros of random polynomials I, II.* Theory of Probability and Its Applications, 16:228–248 and 485–493, 1971.
- **[Foundational]** N. B. Maslova. *On the variance of the number of real roots of random polynomials.* Theory of Probability and Its Applications, 19:35–52, 1974.
- **[Refinement]** J. E. Wilkins, Jr. *An asymptotic expansion for the expected number of real zeros of a random polynomial.* Proceedings of the American Mathematical Society, 103:1249–1258, 1988.
- **[Survey]** A. Edelman and E. Kostlan. *How many zeros of a random polynomial are real?* Bulletin of the American Mathematical Society, 32(1):1–37, 1995.
- **[Book]** A. T. Bharucha-Reid and M. Sambandham. *Random Polynomials.* Academic Press, 1986.
- **[Persistence]** A. Dembo, B. Poonen, Q.-M. Shao and O. Zeitouni. *Random polynomials having few or no real zeros.* Journal of the American Mathematical Society, 15:857–892, 2002.
- **[SOTA]** M. Poplavskyi and G. Schehr. *Exact persistence exponent for the 2d-diffusion equation and related Kac polynomials.* Physical Review Letters, 121:150601, 2018.
- **[SOTA]** T. Tao and V. Vu. *Local universality of zeroes of random polynomials.* International Mathematics Research Notices, 2015(13):5053–5139, 2015.
- **[SOTA]** Y. Do, H. Nguyen and V. Vu. *Real roots of random polynomials: expectation and repulsion.* Proceedings of the London Mathematical Society, 111(6):1231–1260, 2015.
- **[SOTA]** Y. Do, O. Nguyen and V. Vu. *Roots of random polynomials with coefficients of polynomial growth.* Annals of Probability, 46(5):2407–2494, 2018.
- **[SOTA]** O. Nguyen and V. Vu. *Random polynomials: central limit theorems for the real roots.* Duke Mathematical Journal, 170(17):3745–3813, 2021.
- **[Non-universality]** V. Bally, L. Caramellino and G. Poly. *Non-universality for the variance of the number of real roots of random trigonometric polynomials.* Probability Theory and Related Fields, 174:887–927, 2019.
- **[Related]** G. Schehr and S. N. Majumdar. *Real roots of random polynomials and zero crossing properties of diffusion equation.* Journal of Statistical Physics, 132:235–273, 2008.

## 10. Worked Example / Concrete Special Case

**(a) Kostlan degree $2$: an exact answer.** Take $P_2(x)=\xi_0+\sqrt2\,\xi_1x+\xi_2x^2$ with $\xi_k\sim\mathcal{N}(0,1)$, i.e. $\sigma_k^2=\binom2k=(1,2,1)$. Then
$$K(x,y)=1+2xy+x^2y^2=(1+xy)^2 .$$
Compute the Kac–Rice density: $\log K=2\log(1+xy)$, so
$$\partial_x\partial_y\log K\big|_{y=x}=\partial_x\partial_y\Bigl[\frac{2y}{1+xy}\Bigr]_{y=x}\!\!=\frac{2}{(1+x^2)^2},$$
giving $\rho(x)=\frac{1}{\pi}\frac{\sqrt2}{1+x^2}$ and
$$\mathbb{E}N_2=\int_{-\infty}^{\infty}\frac{\sqrt2}{\pi(1+x^2)}\,dx=\sqrt2 .$$
This matches $\mathbb{E}N_n=\sqrt n$. Geometrically, $\rho$ is the constant curvature density of the projective line: the Kostlan ensemble is rotation-invariant, and $\sqrt n$ is the length of the moment curve divided by $\pi$.

**(b) Kac ensemble: where $\frac{2}{\pi}\log n$ comes from.** With $\sigma_k\equiv1$, $K(x,y)=\frac{1-(xy)^{n+1}}{1-xy}$. For $|x|<1$ fixed and $n\to\infty$, $K\to (1-xy)^{-1}$, so
$$\partial_x\partial_y\log K\big|_{y=x}\longrightarrow \frac{1}{(1-x^2)^2},\qquad \rho_n(x)\longrightarrow\frac{1}{\pi(1-x^2)} .$$
The limit is not integrable at $x=1$; the finite-$n$ correction term $\frac{(n+1)^2x^{2n}}{(1-x^{2n+2})^2}$ cuts the divergence off at $|1-x|\asymp 1/n$. Hence
$$\int_0^{1-1/n}\frac{dx}{\pi(1-x^2)}=\frac{1}{2\pi}\log\frac{1+x}{1-x}\Big|_0^{1-1/n}=\frac{\log n}{2\pi}+O(1).$$
There are four such regions ($x\in(0,1)$, $(1,\infty)$ and their negatives), each contributing $\frac{\log n}{2\pi}$, for a total $\frac{2}{\pi}\log n$. The bounded remainders — the two transition windows of width $1/n$ near $\pm1$, plus the $O(1)$ from the antiderivative — assemble into Kac's constant $C=0.6257\ldots$. Numerically the roots concentrate near $\pm1$: for $n=10^6$ one expects only about $9.4$ real roots, and almost all of them lie within distance $10^{-2}$ of $\pm1$.

**(c) Contrast.** Degree $10^6$: Kostlan gives $10^3$ real roots, Kac gives $\approx9.4$. Same degree, same Gaussian coefficients, different variance profile — a factor of $10^5$. This is why "the expected number of real roots" is a statement about the ensemble, not about degree alone.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*