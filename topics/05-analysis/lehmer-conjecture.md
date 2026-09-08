---
id: 05-analysis/lehmer-conjecture
title: "Lehmer Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lehmer Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/lehmer-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f(x) = a_d \prod_{i=1}^{d}(x-\alpha_i) \in \mathbb{Z}[x]$ with $a_d \neq 0$. Its **Mahler measure** is

$$M(f) \;=\; |a_d| \prod_{i=1}^{d} \max(1, |\alpha_i|).$$

For an algebraic number $\alpha$, write $M(\alpha) := M(f_\alpha)$ where $f_\alpha$ is the minimal polynomial of $\alpha$ over $\mathbb{Z}$ (primitive, positive leading coefficient). By Kronecker's theorem, $M(\alpha) = 1$ exactly when $\alpha = 0$ or $\alpha$ is a root of unity.

**Lehmer's conjecture (strong form).** There is an absolute constant $c > 1$ such that for every algebraic number $\alpha$ that is neither $0$ nor a root of unity,
$$M(\alpha) \;\ge\; c.$$
The conjectural optimal value is $c = M(L) = 1.176280818\ldots$, the Mahler measure of **Lehmer's polynomial**
$$L(x) = x^{10} + x^{9} - x^{7} - x^{6} - x^{5} - x^{4} - x^{3} + x + 1 .$$

**Weak form (the "problem" as Lehmer posed it, 1933).** Is $\inf\{M(\alpha) : M(\alpha)>1\} > 1$? Lehmer asked whether $M(f) < 1+\varepsilon$ is achievable for every $\varepsilon>0$ with $M(f)>1$; he did not conjecture an answer.

A complete resolution is either (a) a proof of a bound $M(\alpha) \ge c > 1$ valid for all degrees, or (b) an explicit sequence $\alpha_n$ with $M(\alpha_n) \to 1^{+}$.

## 2. Mathematical Foundations

**Integral form.** By Jensen's formula, for $f \in \mathbb{C}[x]$,
$$\log M(f) \;=\; \int_0^1 \log\bigl|f(e^{2\pi i t})\bigr|\, dt ,$$
so $\log M$ is the $L^0$–mean of $\log|f|$ on the unit circle. This makes $M$ multiplicative: $M(fg)=M(f)M(g)$, and places the problem inside harmonic analysis on $\mathbb{T}$.

**Height form.** The absolute logarithmic Weil height of $\alpha$ of degree $d$ is $h(\alpha) = \frac{1}{d}\log M(\alpha)$. Lehmer's conjecture is equivalent to
$$h(\alpha) \;\ge\; \frac{\log c}{[\mathbb{Q}(\alpha):\mathbb{Q}]} \qquad (\alpha \text{ not } 0 \text{ or a root of unity}),$$
i.e. a sharp lower bound for heights inverse-linear in the degree. This is the "one-dimensional" case of a family of height-gap problems on tori, abelian varieties, and general algebraic groups.

**Special algebraic numbers.**
- $\alpha>1$ is a **Pisot number** if it is a real algebraic integer whose other conjugates lie in $|z|<1$; then $M(\alpha)=\alpha$. The smallest is the plastic number $\theta_0 = 1.3247179\ldots$, root of $x^3-x-1$ (Siegel, 1944).
- $\alpha>1$ is a **Salem number** if it is a real algebraic integer whose conjugates lie in $|z|\le 1$ with at least one on $|z|=1$; then $M(\alpha)=\alpha$ and the minimal polynomial is reciprocal ($x^d f(1/x) = f(x)$). Lehmer's number $\lambda_L = 1.17628\ldots$ is the smallest known Salem number.
- $f$ is **non-reciprocal** if $f(x) \ne \pm x^{\deg f} f(1/x)$.

**Auxiliary machinery.** All known unconditional bounds use: (i) the Frobenius/Fermat congruence $f(x)^p \equiv f(x^p) \pmod p$, which forces $\alpha^p$ to be close to a conjugate of $\alpha$ unless $M(\alpha)$ is large; (ii) resultant and discriminant estimates $\bigl|\mathrm{Res}(f, g)\bigr| \ge 1$ for coprime integer polynomials; (iii) interpolation determinants / auxiliary polynomials of transcendence-theory type. The base identity behind (i)–(ii) is
$$\prod_{i,j} |\alpha_i^{p} - \alpha_j| \;=\; |\mathrm{Res}(f, f_p)| \;\ge\; 1 \quad\text{when } f \nmid f_p,$$
where $f_p$ is the minimal polynomial of $\alpha^p$.

## 3. History & State of the Art (SOTA)

- **1933.** D. H. Lehmer, searching for large primes via Pierce sequences $\Delta_n = \prod_i(\alpha_i^n-1)$, asked for integer polynomials with Mahler measure just above 1, and exhibited $L(x)$ with $M(L)=1.17628\ldots$. No smaller value has been found in ninety-three years.
- **1951.** Breusch proved $M(\alpha) \ge 1.179$ for $\alpha$ a non-reciprocal algebraic *integer* — the first unconditional gap, though it went unnoticed for decades.
- **1971.** Smyth: if $f$ is non-reciprocal and $f(0)\ne 0$, $f(\pm 1) \ne 0$, then $M(f) \ge \theta_0 = 1.3247\ldots$, sharp. This settles Lehmer's problem outside the reciprocal case and is why all remaining difficulty is concentrated on Salem-like polynomials.
- **1979.** Dobrowolski's degree-dependent bound: for $\alpha$ of degree $d \ge 2$,
$$M(\alpha) \;>\; 1 + c\left(\frac{\log\log d}{\log d}\right)^{3},$$
with $c = 1-\varepsilon$ for $d \gg 1$ and $c = 1/1200$ unconditionally. Constant improvements: Cantor–Straus and Louboutin to $9/4$, Dubickas to $64/\pi^2 - \varepsilon$; Voutier (1996) gave the clean effective $c=1/4$ for all $d\ge 2$.
- **1999.** Amoroso–David proved the higher-dimensional analogue (Lehmer's problem for points of $\mathbb{G}_m^n$ up to the expected $\log\log$ loss), transferring Dobrowolski's method to $n$ variables.
- **2007.** Borwein, Dobrowolski, Mossinghoff (Annals of Math.): if all coefficients of $f$ are odd, then $M(f) \ge 5^{1/4} = 1.4953\ldots$ — an unconditional Lehmer-type theorem for an infinite family of arbitrary degree.
- **2019–2021.** Dimitrov proved the **Schinzel–Zassenhaus conjecture**: the house $\overline{|\alpha|} \ge 2^{1/(4d)}$ for non-cyclotomic algebraic integers of degree $d$, using Bost-style slope inequalities and the arithmetic transfer/Hilbert-space method of Dubinin–Chudnovsky. This is the closest structural relative of Lehmer's conjecture to fall.

Status of the main statement: **open**, with no lower bound independent of $d$.

## 4. Partial Results / Verified Cases

Proven unconditionally:

| Class | Bound | Source |
|---|---|---|
| Non-reciprocal $\alpha$ | $M(\alpha)\ge\theta_0=1.3247\ldots$ | Smyth 1971 |
| All $\alpha$ of degree $d$ | $M(\alpha) > 1+\tfrac14(\log\log d/\log d)^3$ | Voutier 1996 |
| $f$ with all coefficients odd | $M(f)\ge 5^{1/4}$ | Borwein–Dobrowolski–Mossinghoff 2007 |
| $\alpha$ with $\mathbb{Q}(\alpha)/\mathbb{Q}$ abelian, or $\alpha \in \mathbb{Q}^{\mathrm{ab}}$ | $h(\alpha)\ge (\log 5)/12$ | Amoroso–Dvornicich 2000 |
| $\alpha$ of bounded degree over $\mathbb{Q}^{\mathrm{ab}}$ | $h(\alpha) \ge c(d) > 0$ | Amoroso–Zannier 2000 |
| $\alpha$ totally real, $\ne 0,\pm1$ | $M(\alpha)\ge \alpha_0^{d}$, $\alpha_0=1.7836\ldots$ | Schinzel 1973 |
| $\alpha$ with $\mathbb{Q}(\alpha)$ having a small ramified prime / Galois group constraints | Lehmer-strength bounds | Amoroso–David; Amoroso–Masser |

Computational verification:
- Mossinghoff (1998, *Math. Comp.*) tabulated all Mahler measures $< 1.3$ for degree $\le 24$; the list is finite and headed by $\lambda_L$.
- Mossinghoff–Rhin–Wu (2008, *Math. Comp.*) proved there is **no** algebraic number of degree $\le 44$ with $1 < M(\alpha) < 1.3$ other than the 47 known values, all $\ge \lambda_L$. Later refinements (Flammang; Wu) push degree ranges and the "$M<1.3$" window further.
- No Salem number smaller than $\lambda_L$ exists of degree $\le 44$ (Mossinghoff–Rhin–Wu); Boyd's earlier searches covered degree $\le 40$ for interval-restricted families.

## 5. Principal Obstacles

- **The reciprocal barrier.** Smyth's argument builds an auxiliary rational function from $f(x)$ and $x^d f(1/x)$; when $f$ is reciprocal these coincide and the construction degenerates. Every known "constant $c>1$" proof dies exactly here, and Salem polynomials — the conjectured extremal family — are reciprocal.
- **The $\log\log$ loss is intrinsic to the $p$-adic method.** Dobrowolski's proof compares $\alpha$ with $\alpha^p$ for primes $p \le P$; the number of usable primes is $\sim P/\log P$ and the auxiliary determinant forces $P \approx d\log d$, producing the $(\log\log d/\log d)^3$ factor. Refining the constant is routine; removing the degree dependence would require a fundamentally non-counting input.
- **No spectral gap on the circle.** $\log M(f)=\int_0^1\log|f|$ is a mean of a function that can be very negative on a small set. Making $M(f)$ near 1 requires $|f|$ near 1 on most of $\mathbb{T}$; nothing in classical Fourier analysis forbids integer polynomials from doing this, because integrality is not a condition visible to $L^2$ methods. Attempts via the Szegő/Toeplitz machinery yield only $M(f)\ge1$.
- **Rigidity absent.** For Salem numbers the conjugates on $|z|=1$ can equidistribute; the limiting measures allowed by known equidistribution theorems (Bilu, Baker–Rumely, Favre–Rivera-Letelier) are compatible with $M \to 1$, so equidistribution alone is a consequence of, not a route to, Lehmer.
- **Transfer failures.** Dimitrov's proof of Schinzel–Zassenhaus controls the *largest* modulus (house), a single conjugate. Mahler measure aggregates all conjugates outside the disk; the Hilbert-space/slope inequality gives no control on the product because the auxiliary function is built for a single extremal point.

## 6. The Gap

Proven: $M(\alpha) \ge 1 + \Theta\!\left((\log\log d/\log d)^3\right)$, tending to $1$ as $d\to\infty$; plus a genuine constant $c>1$ on structured subclasses (non-reciprocal, odd-coefficient, abelian, bounded degree over $\mathbb{Q}^{\mathrm{ab}}$).

Wanted: the same constant uniformly in $d$ for *reciprocal* polynomials with no arithmetic structure imposed.

The precise missing step: an auxiliary construction that, for a reciprocal $f$ of large degree $d$ with $M(f)$ close to $1$, produces a nonzero integer of absolute value $<1$ — i.e. an unconditional non-vanishing/resultant argument that survives the symmetry $f(x)=x^df(1/x)$. Equivalently, one needs $\Omega(d)$ independent arithmetic constraints on the conjugates rather than the $\Theta(d/\log d)$ prime-power constraints the Frobenius method supplies.

## 7. Current Research (as of June 2026)

- **Slope/Arakelov methods after Dimitrov.** Groups around Dimitrov, Habegger, and Bost's school are testing whether the Bost slope inequality plus the Chudnovsky–Dubinin capacity transfer can be pushed from the house to the full Mahler measure. Partial transfer results for Salem numbers with bounded numbers of conjugates off the circle exist *(frontier — verify)*.
- **Dynamical and $p$-adic equidistribution.** Fili, Pottmeyer, Petsche and collaborators pursue Lehmer-type gaps for heights attached to non-archimedean dynamical systems and for fields with small ramification (e.g. $\mathbb{Q}^{tr}$, totally $p$-adic fields), where sharp constants are sometimes obtainable.
- **Computation.** Extensions of Mossinghoff–Rhin–Wu integer-transfinite-diameter and LLL-based searches now certify the $M<1.3$ window for degrees somewhat beyond 44 *(frontier — verify)*; the constant $\lambda_L$ remains unbeaten in searches over $\sim 10^{11}$ candidate polynomials.
- **Geometric shadows.** Because $\lambda_L$ is the smallest known Salem number, it appears as the conjectural minimum of: dilatations of pseudo-Anosov maps on small-genus surfaces (Hironaka, Lanneau–Thiffeault), growth rates of hyperbolic Coxeter groups, and lengths of short geodesics on arithmetic hyperbolic 2- and 3-orbifolds (Neumann–Reid; Chinburg–Friedman). Progress in these areas is a testing ground for the conjecture's plausibility.
- **Higher-dimensional analogues.** Elliptic and abelian Lehmer problems (Laurent for CM curves; Masser; David–Hindry; Galateau–Mahé) continue to yield Dobrowolski-strength bounds, and are the setting where the strongest recent structural theorems appear.

## 8. Future Work

- Find a reciprocal-stable auxiliary construction: replace $f(x)$ vs $x^df(1/x)$ by a genuinely asymmetric object, e.g. a Frobenius twist over an auxiliary quadratic field, or a two-variable auxiliary polynomial as in Amoroso–David.
- Prove the conjecture for Salem numbers of *bounded trace* or bounded numbers of real conjugates — a class where interval arithmetic and the "integer transfinite diameter" already give near-sharp constants.
- Determine whether the set of Salem numbers is closed in $\mathbb{R}$ (a Salem-set analogue of Salem's theorem for Pisot numbers); a positive answer would make $\inf$ attained and convert Lehmer into a finiteness statement.
- Transfer Dimitrov's method to bound $\prod_{|\alpha_i|>1}|\alpha_i|$ rather than $\max_i|\alpha_i|$; identify the correct capacity-theoretic functional whose extremal problem encodes $M$.
- Push exhaustive verification past degree 60 with certified branch-and-bound over the coefficient lattice.

## 9. Key References

- **[Foundational]** D. H. Lehmer. *Factorization of certain cyclotomic functions.* Annals of Mathematics **34** (1933), 461–479. [DOI](https://doi.org/10.2307/1968172)
- **[Foundational]** C. J. Smyth. *On the product of the conjugates outside the unit circle of an algebraic integer.* Bulletin of the London Mathematical Society **3** (1971), 169–175. [DOI](https://doi.org/10.1112/blms/3.2.169)
- **[Foundational]** E. Dobrowolski. *On a question of Lehmer and the number of irreducible factors of a polynomial.* Acta Arithmetica **34** (1979), 391–401. [DOI](https://doi.org/10.4064/aa-34-4-391-401)
- **[Effective bound]** P. Voutier. *An effective lower bound for the height of algebraic numbers.* Acta Arithmetica **74** (1996), 81–95. [DOI](https://doi.org/10.4064/aa-74-1-81-95)
- **[SOTA]** P. Borwein, E. Dobrowolski, M. J. Mossinghoff. *Lehmer's problem for polynomials with odd coefficients.* Annals of Mathematics **166** (2007), 347–366. [DOI](https://doi.org/10.4007/annals.2007.166.347)
- **[SOTA]** F. Amoroso, S. David. *Le problème de Lehmer en dimension supérieure.* Journal für die reine und angewandte Mathematik (Crelle) **513** (1999), 145–179. [DOI](https://doi.org/10.1515/crll.1999.058)
- **[SOTA]** F. Amoroso, U. Zannier. *A relative Dobrowolski lower bound over abelian extensions.* Annali della Scuola Normale Superiore di Pisa **29** (2000), 711–727.
- **[SOTA]** V. Dimitrov. *A proof of the Schinzel–Zassenhaus conjecture on polynomials.* arXiv:1912.12545 (2019).
- **[Computational]** M. J. Mossinghoff. *Polynomials with small Mahler measure.* Mathematics of Computation **67** (1998), 1697–1705. [DOI](https://doi.org/10.1090/s0025-5718-98-01006-0)
- **[Computational]** M. J. Mossinghoff, G. Rhin, Q. Wu. *Minimal Mahler measures.* Experimental Mathematics **17** (2008), 451–458. [DOI](https://doi.org/10.1080/10586458.2008.10128872)
- **[Survey]** C. J. Smyth. *The Mahler measure of algebraic numbers: a survey.* In *Number Theory and Polynomials*, LMS Lecture Note Series 352, Cambridge University Press, 2008, 322–349. [DOI](https://doi.org/10.1017/cbo9780511721274.021)
- **[Survey]** E. Ghate, E. Hironaka. *The arithmetic and geometry of Salem numbers.* Bulletin of the American Mathematical Society **38** (2001), 293–314. [DOI](https://doi.org/10.1090/s0273-0979-01-00902-8)
- **[Book]** P. Borwein. *Computational Excursions in Analysis and Number Theory.* CMS Books in Mathematics, Springer, 2002. [DOI](https://doi.org/10.1007/978-0-387-21652-2)

## 10. Worked Example / Concrete Special Case

**(a) Lehmer's polynomial.** $L(x)$ is reciprocal of degree 10. Substituting $y = x + x^{-1}$ into $x^{-5}L(x)$ gives the degree-5 trace polynomial
$$y^5 + y^4 - 5y^3 - 5y^2 + 4y + 3 = 0 .$$
Its unique root outside $[-2,2]$ is $y_0 = 2.02642\ldots$, and $x + x^{-1} = y_0$ gives
$$\lambda_L = \frac{y_0 + \sqrt{y_0^2-4}}{2} = 1.1762808182599175\ldots,\qquad \lambda_L^{-1}=0.850\ldots$$
The remaining eight roots satisfy $|y|<2$, hence lie on $|x|=1$. So exactly one root has modulus $>1$ and
$$M(L) = 1\cdot \lambda_L = 1.17628081825991750\ldots$$
confirming $\lambda_L$ is a Salem number and $\log M(L) = 0.16235\ldots$, i.e. height $h = 0.016235\ldots$ at degree 10.

**(b) Why Smyth's theorem does not apply.** $x^{10}L(1/x) = L(x)$ exactly, so $L$ is reciprocal and the bound $M\ge\theta_0=1.3247$ is unavailable — consistent with $M(L)=1.176 < \theta_0$. This one line is the whole difficulty of the conjecture in miniature.

**(c) What Dobrowolski gives at $d=10$.** With Voutier's constant,
$$M(\alpha) > 1 + \tfrac14\left(\frac{\log\log 10}{\log 10}\right)^{3} = 1 + \tfrac14\,(0.3622)^3 = 1.0119 ,$$
far below $1.176$. At $d=10^{6}$ the same bound gives $M > 1.00047$. The bound degrades to $1$; the conjecture asserts it should not.

**(d) A near-miss check.** The smallest Pisot number $\theta_0$ (root of $x^3-x-1$) has $M(\theta_0)=\theta_0=1.32472$, and the smallest known Salem numbers after $\lambda_L$ are $1.18836\ldots$ (degree 18) and $1.20002\ldots$ (degree 14). Extensive search over degrees $\le 44$ found no value in $(1,\lambda_L)$ — the empirical basis for taking $c=\lambda_L$ as the conjectured optimum.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*