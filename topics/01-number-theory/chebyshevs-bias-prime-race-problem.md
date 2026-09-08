---
id: 01-number-theory/chebyshevs-bias-prime-race-problem
title: "Chebyshev's Bias and Prime Race Densities"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chebyshev's Bias and Prime Race Densities

> **Topic:** Number Theory · **ID:** `01-number-theory/chebyshevs-bias-prime-race-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $q \geq 3$ and let $a_1,\dots,a_r$ be distinct residues coprime to $q$. Write $\pi(x;q,a)=\\#\{p \leq x : p \equiv a \bmod q\}$. Dirichlet's theorem plus the prime number theorem for arithmetic progressions gives $\pi(x;q,a)\sim \operatorname{li}(x)/\varphi(q)$ for every $a$, so the classes tie to first order. The **prime race** (Shanks–Rényi problem) asks about the second-order term: the set
$$P_{q;a_1,\dots,a_r}=\{x \geq 2 : \pi(x;q,a_1) > \pi(x;q,a_2) > \dots > \pi(x;q,a_r)\}.$$

**Open problem.** Prove unconditionally that $P_{q;a_1,\dots,a_r}$ has a logarithmic density
$$\delta(q;a_1,\dots,a_r)=\lim_{X\to\infty}\frac{1}{\log X}\int_{P_{q;a_1,\dots,a_r}\cap[2,X]}\frac{dt}{t},$$
that this density is strictly positive (each ordering occurs on a non-negligible set), and that it is **not** $1/r!$ — quantifying **Chebyshev's bias**: quadratic non-residues lead quadratic residues far more than half the time. The two-class case $r=2$ with $q=4$, $(a_1,a_2)=(3,1)$ is the historical prototype: Chebyshev (1853) observed $\pi(x;4,3)\geq\pi(x;4,1)$ for all small $x$.

A complete resolution must either (i) prove existence, positivity and the explicit values of these densities without assuming the Generalized Riemann Hypothesis (GRH) and the Linear Independence hypothesis (LI), or (ii) exhibit a counterexample — a race whose density fails to exist or takes an unexpected value.

## 2. Mathematical Foundations

For a Dirichlet character $\chi \bmod q$ let $L(s,\chi)=\sum_{n\ge1}\chi(n)n^{-s}$, and let $\psi(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n)$. Orthogonality gives
$$\psi(x;q,a)=\frac{1}{\varphi(q)}\sum_{\chi \bmod q}\bar\chi(a)\,\psi(x,\chi),$$
and the explicit formula, for $\chi \neq \chi_0$, is
$$\psi(x,\chi) = -\sum_{\rho_\chi}\frac{x^{\rho_\chi}}{\rho_\chi}+O(\log^2 x),$$
the sum running over non-trivial zeros $\rho_\chi=\tfrac12+i\gamma_\chi$ of $L(s,\chi)$ (assuming GRH).

Converting from $\psi$ to $\pi$ introduces the prime-power correction that creates the bias. With $c(q,a)=\\#\{t \bmod q : t^2 \equiv a \bmod q\}$,
$$\pi(x;q,a)=\frac{1}{\varphi(q)}\Big(\operatorname{li}(x)-c(q,a)\operatorname{li}(x^{1/2})\Big)+\text{oscillation}+O(x^{1/3}).$$
Squares of primes all lie in classes $a$ with $c(q,a)>0$ (the quadratic residues), so residue classes are systematically *depleted* by $\operatorname{li}(\sqrt{x})\approx 2\sqrt x/\log x$.

Define the normalized error vector
$$E(x;q,a_1,\dots,a_r)=\frac{\log x}{\sqrt{x}}\big(\pi(x;q,a_1),\dots,\pi(x;q,a_r)\big)\varphi(q) - \big(\text{common main term}\big),$$
whose $j$-th coordinate has the shape
$$E_j(x)= -c(q,a_j) + \sum_{\chi\ne\chi_0}\bar\chi(a_j)\sum_{\gamma_\chi>0}\frac{2\,\mathrm{Re}\big(e^{i\gamma_\chi \log x}\big)}{\sqrt{\tfrac14+\gamma_\chi^2}}+o(1).$$

**Hypotheses used.**
- **GRH$_q$**: all non-trivial zeros of every $L(s,\chi)$, $\chi \bmod q$, satisfy $\mathrm{Re}(\rho)=\tfrac12$.
- **LI (Grand Simplicity Hypothesis)**: the multiset $\{\gamma_\chi>0 : \chi \bmod q \text{ primitive}\}$ is linearly independent over $\mathbb{Q}$.

Under GRH$_q$ + LI, the Kronecker–Weyl equidistribution theorem makes $u \mapsto (e^{i\gamma_\chi u})_\chi$ equidistribute on a torus, so $E(e^u;\cdot)$ has a limiting distribution $\mu_{q;a_1,\dots,a_r}$ on $\mathbb{R}^r$: an infinite convolution of scaled arcsine laws, absolutely continuous, with mean vector $(-c(q,a_j))_j$ and covariance built from $\sum_\gamma (\tfrac14+\gamma^2)^{-1}$. Then
$$\delta(q;a_1,\dots,a_r)=\mu_{q;a_1,\dots,a_r}\big(\{y : y_1>\dots>y_r\}\big) .$$

## 3. History & State of the Art (SOTA)

- **1853** — Chebyshev, in a letter to Fuss, asserts $\sum_p (-1)^{(p-1)/2}e^{-p/x}\to-\infty$, i.e. a persistent excess of primes $\equiv 3 \bmod 4$.
- **1914** — Littlewood proves $\pi(x)-\operatorname{li}(x)$ changes sign infinitely often, killing the naive "$\pi(x)<\operatorname{li}(x)$ always" analogue.
- **1918** — Hardy–Littlewood and Landau independently show Chebyshev's assertion in the above $e^{-p/x}$ form is *equivalent* to GRH for $L(s,\chi_{-4})$.
- **1957** — Leech: first sign change of $\pi(x;4,3)-\pi(x;4,1)$ at $x=26861$.
- **1962–** — Knapowski and Turán launch "Comparative prime number theory" (a series in *Acta Math. Hungar.*), posing quantitative sign-change conjectures; several were later disproved under LI.
- **1994** — **Rubinstein–Sarnak**: under GRH + LI, all densities exist, are positive, and are computable. $\delta(4;3,1)=0.9959$, $\delta(3;2,1)=0.9990$; densities $\to 1/2$ as $q\to\infty$ in the two-class residue/non-residue race.
- **1996** — Kaczorowski: unconditional infinitude of sign changes and $\Omega$-results for many races.
- **2000** — Feuerverger–Martin compute three- and four-way densities numerically; asymmetries such as $\delta(8;3,5,7)\ne\delta(8;5,3,7)$ appear.
- **2002** — Ford–Konyagin: if LI fails in specific ways (or zeros lie off the line), three-way races can behave pathologically.
- **2013–2014** — Fiorilli–Martin give an asymptotic formula for two-class densities; Fiorilli exhibits *highly biased* races with $\delta\to1$.
- **2019–2020** — Ford–Harper–Lamzouri (extreme biases with many contestants); Martin–Ng (positivity under weaker hypotheses); Devin (bias for general analytic $L$-functions).

## 4. Partial Results / Verified Cases

- **Conditional full solution ($r$ arbitrary, all $q$).** Under GRH$_q$ + LI, $\delta(q;a_1,\dots,a_r)$ exists, lies in $(0,1)$, and equals $1/r!$ iff $a_1,\dots,a_r$ are all residues or all non-residues (Rubinstein–Sarnak 1994).
- **Unconditional sign changes.** $\pi(x;q,a)-\pi(x;q,b)$ changes sign infinitely often whenever $a$ is a non-residue and $b$ a residue mod $q$ — provable from Landau's method with no hypotheses (Littlewood-type argument); Kaczorowski gives quantitative counts of sign changes in $[T,2T]$.
- **Asymptotics in $q$.** Fiorilli–Martin (2013): for $N$ a non-residue and $R$ a residue mod $q$, under GRH+LI,
 $$\delta(q;N,R)=\frac12+\frac{\rho(q)}{\sqrt{2\pi V(q;N,R)}}+O\!\big(V^{-3/2}\big),\qquad V(q;N,R)\sim 2\varphi(q)\log q,$$
 where $\rho(q)=\\#\{t \bmod q: t^2\equiv1\}$; hence $\delta\to1/2$.
- **Many contestants.** Lamzouri (2012): for fixed $r$, $\delta(q;a_1,\dots,a_r)\to 1/r!$ as $q\to\infty$, with uniformity allowing $r$ to grow slowly with $q$.
- **Extreme cases.** Fiorilli (2014): for suitable $q$ with many small prime factors and $a$ in a rare class, $\delta(q;N,R)$ can be made arbitrarily close to $1$; Ford–Harper–Lamzouri (2019) do the same for $r\ge3$.
- **Computation.** $\pi(x;4,3)>\pi(x;4,1)$ except on a sparse set with first violation at $26861$; for $q=3$ the first $x$ with $\pi(x;3,2)<\pi(x;3,1)$ is $608\,981\,813\,029$ (Bays–Hudson 1978). For $\pi(x)$ vs $\operatorname{li}(x)$, Bays–Hudson (2000) locate a crossover region near $1.398\times10^{316}$.
- **Function fields.** For $\mathbb{F}_q[T]$ and for families of curves, the analogue of GRH is a theorem (Weil), and Cha and collaborators prove unconditional Chebyshev-bias statements — LI must still be assumed or verified case-by-case.

## 5. Principal Obstacles

- **GRH is needed even to define the object.** A single zero with $\mathrm{Re}(\rho)=\beta>1/2$ contributes $x^{\beta-1/2}$ to $E(x)$, which is unbounded; the limiting distribution then does not exist in the usual sense, and Ford–Konyagin show such zeros can force one ordering to occur only finitely often. No known technique produces zero-free regions of the required quality: current results give only $\sigma > 1 - c/\log(q(|t|+2))$, and Siegel zeros are not excluded effectively.
- **LI is out of reach of every current method.** LI is a statement about $\mathbb{Q}$-linear relations among transcendental-looking real numbers $\gamma_\chi$. There is no unconditional proof that even *two* ordinates of distinct $L$-functions are linearly independent, nor that a single $\gamma$ is irrational. Analytic methods (moments, pair correlation, zero-density estimates) control zeros statistically but say nothing about arithmetic relations among them.
- **No effective Diophantine input.** Kronecker–Weyl needs exact independence; quantitative versions require Diophantine-type lower bounds on $|\sum n_\gamma \gamma|$ for integer vectors $n$, which would follow from nothing currently known.
- **Weak forms are not enough.** Replacing LI by "no relations of bounded height" gives existence of a *Cesàro-type* density only along subsequences; the passage to a genuine limit requires uniformity in the tail of the zero sum, where the series $\sum_\gamma(\tfrac14+\gamma^2)^{-1}$ converges only logarithmically slowly.
- **Logarithmic vs natural density.** The natural density of $P_{q;a_1,a_2}$ is not known to exist even under GRH + LI; the $dt/t$ measure is essential to the Kronecker–Weyl argument and cannot be removed by current means.

## 6. The Gap

Proven: everything, *given* GRH$_q$ + LI (Section 4). Unproven: any of it without them. The gap is exactly two implications.

1. **From "no bad zeros" to a bounded oscillation.** One needs GRH for the finitely many $L(s,\chi)$, $\chi \bmod q$ — a special case of GRH that is nonetheless no easier than the general one; even for the single function $L(s,\chi_{-4})$ it is open.
2. **From bounded oscillation to equidistribution.** Even granting GRH, one must rule out $\mathbb{Q}$-linear relations among the $\gamma_\chi$, or else replace equidistribution on the full torus by equidistribution on the (unknown) closure of the orbit. Martin–Ng (2020) narrow this by proving, under GRH alone plus a much weaker independence assumption, that every ordering has positive lower logarithmic density; but the *existence* of the limit and the *exact value* still require full LI.

A disproof would need a demonstrated linear relation among zero ordinates, or an off-line zero — neither is expected.

## 7. Current Research (as of June 2026)

- **Bias for general $L$-functions and Galois extensions.** Devin's framework (2020) axiomatizes Chebyshev bias for analytic $L$-functions; Fiorilli–Jouve extend to Frobenius distributions in families of Galois extensions, where the bias constant is governed by the second moment of characters of the Galois group. Active at Orsay, Montréal (UdeM/UBC), and York.
- **Weakening LI.** Ongoing work replaces LI by "self-sufficient zeros" or by measure-theoretic genericity in families, aiming at density statements valid for almost all $q$. *(frontier — verify)*
- **Function-field models.** Unconditional computation of bias for families of hyperelliptic curves over $\mathbb{F}_q$, using Katz–Sarnak equidistribution to replace LI by a monodromy statement — the most promising route to *unconditional* prime-race theorems in any setting. *(frontier — verify)*
- **Biases beyond primes.** Analogues for sums of two squares, for ranks of elliptic curves in families (Sarnak's letter to Mazur on $\tau(p)$ and rank bias), and for Sato–Tate-type statistics.
- **Numerics.** High-precision evaluation of $\delta(q;a_1,\dots,a_r)$ for $r\ge4$ and large $q$, testing the Fiorilli–Martin asymptotic in the transition range $r\asymp\log q$.

## 8. Future Work

- Prove GRH for the single character $\chi_{-4}$; by Hardy–Littlewood/Landau this settles Chebyshev's original assertion in its $e^{-p/x}$ form.
- Establish any unconditional irrationality/independence result for ordinates of zeros — even "$\gamma_1(\chi_{-4})/\gamma_1(\zeta)\notin\mathbb{Q}$" would be a first.
- Sharpen Martin–Ng: obtain existence (not just positivity) of the density under GRH alone.
- Extend Fiorilli's highly-biased-race classification to a complete description of which $(q;a_1,\dots,a_r)$ maximize $|\delta - 1/r!|$.
- Prove natural-density statements, or show that the natural density genuinely fails to exist.

## 9. Key References

- **[Foundational]** P. L. Chebyshev. *Lettre de M. le professeur Tchébychev à M. Fuss.* Bull. Classe Phys. Acad. Imp. Sci. St. Pétersbourg 11 (1853), 208.
- **[Foundational]** J. E. Littlewood. *Sur la distribution des nombres premiers.* C. R. Acad. Sci. Paris 158 (1914), 1869–1872.
- **[Foundational]** E. Landau. *Über einige ältere Vermutungen und Behauptungen in der Primzahltheorie.* Math. Z. 1 (1918), 1–24 and 213–219.
- **[Foundational]** S. Knapowski, P. Turán. *Comparative prime-number theory I.* Acta Math. Acad. Sci. Hungar. 13 (1962), 299–314.
- **[SOTA]** M. Rubinstein, P. Sarnak. *Chebyshev's bias.* Experimental Mathematics 3 (1994), 173–197.
- **[SOTA]** J. Kaczorowski. *On the Shanks–Rényi race problem.* Acta Arithmetica 74 (1996), 31–46.
- **[SOTA]** A. Feuerverger, G. Martin. *Biases in the Shanks–Rényi prime number race.* Experimental Mathematics 9 (2000), 535–570.
- **[SOTA]** C. Bays, R. H. Hudson. *A new bound for the smallest $x$ with $\pi(x)>\operatorname{li}(x)$.* Mathematics of Computation 69 (2000), 1285–1296.
- **[SOTA]** K. Ford, S. Konyagin. *The prime number race and zeros of L-functions off the critical line.* Duke Mathematical Journal 113 (2002), 313–330.
- **[SOTA]** Y. Lamzouri. *The Shanks–Rényi prime number race with many contestants.* Mathematical Research Letters 19 (2012), 649–666.
- **[SOTA]** D. Fiorilli, G. Martin. *Inequities in the Shanks–Rényi prime number race: an asymptotic formula for the densities.* Journal für die reine und angewandte Mathematik 676 (2013), 121–212.
- **[SOTA]** D. Fiorilli. *Highly biased prime number races.* Algebra & Number Theory 8 (2014), 1733–1767.
- **[Recent]** K. Ford, A. Harper, Y. Lamzouri. *Extreme biases in prime number races with many contestants.* Mathematische Annalen 374 (2019), 517–551.
- **[Recent]** G. Martin, N. Ng. *Inclusive prime number races.* Transactions of the American Mathematical Society 373 (2020), 3561–3607.
- **[Recent]** L. Devin. *Chebyshev's bias for analytic L-functions.* Mathematical Proceedings of the Cambridge Philosophical Society 169 (2020), 103–140.
- **[Survey]** A. Granville, G. Martin. *Prime number races.* American Mathematical Monthly 113 (2006), 1–33.

## 10. Worked Example / Concrete Special Case

**The race mod 4.** There is one non-principal character, $\chi_{-4}$, with $\chi_{-4}(1)=1$, $\chi_{-4}(3)=-1$. Orthogonality gives
$$\psi(x;4,3)-\psi(x;4,1) = -\psi(x,\chi_{-4}) = \sum_{\rho}\frac{x^{\rho}}{\rho}+O(\log^2x),$$
so at the level of $\psi$ the difference is *pure oscillation* with mean zero — no bias.

The bias enters when passing to $\pi$. Every odd prime $p$ has $p^2\equiv1\bmod 8$, hence $p^2\equiv1\bmod 4$. So all $\approx\pi(\sqrt x)$ prime squares $\le x$ are counted by $\psi$ in the class $1$, and are absent from $\pi(x;4,1)$. Equivalently $c(4,1)=\\#\{1,3\}=2$ and $c(4,3)=0$, giving
$$\pi(x;4,1)\approx \tfrac12\operatorname{li}(x)-\operatorname{li}(\sqrt x),\qquad \pi(x;4,3)\approx \tfrac12\operatorname{li}(x),$$
$$\pi(x;4,3)-\pi(x;4,1)\approx \operatorname{li}(\sqrt x)\approx \frac{2\sqrt x}{\log x}.$$

Normalizing, $E(x):=\frac{\log x}{\sqrt x}\big(\pi(x;4,3)-\pi(x;4,1)\big)$ satisfies, under GRH,
$$E(x)=2+2\sum_{\gamma>0}\frac{\cos(\gamma\log x)-2\gamma\sin(\gamma\log x)}{\tfrac14+\gamma^2}+o(1),$$
$\gamma$ running over positive ordinates of $L(s,\chi_{-4})$ (first ordinate $\gamma_1\approx 6.0209$). Under LI the oscillating part is a sum of independent mean-zero terms, with variance
$$V(4;3,1)=4\sum_{\gamma>0}\frac{1}{\tfrac14+\gamma^2}.$$
Each zero contributes little — the first gives $4/(0.25+36.25)\approx0.11$ — and the series converges to $V\approx0.57$ *(derived: the value that reproduces the published density under the normal approximation)*.

Then $\delta(4;3,1)=\Pr[2+X>0]$ where $X$ has mean $0$ and variance $V$. The Gaussian approximation gives
$$\delta(4;3,1)\approx\Phi\!\left(\frac{2}{\sqrt{0.57}}\right)=\Phi(2.65)\approx0.996,$$
matching Rubinstein–Sarnak's exact conditional value $0.9959$. The interpretation: the deterministic head start of $+2$ is roughly $2.6$ standard deviations of the zero-driven noise, so class $3$ leads about $99.6\%$ of the time (logarithmically), yet the noise is unbounded, so class $1$ still takes the lead infinitely often — first at $x=26861$.

**Contrast, mod 8.** Here $c(8,1)=4$ and $c(8,3)=c(8,5)=c(8,7)=0$, so the classes $3,5,7$ are mutually unbiased against each other ($\delta(8;3,5)=\delta(8;5,3)=1/2$) but all strongly beat $1$. This is exactly the residue/non-residue dichotomy of Section 4.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*