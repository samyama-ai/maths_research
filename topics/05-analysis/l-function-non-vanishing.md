---
id: 05-analysis/l-function-non-vanishing
title: "L-function Non-vanishing"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# L-function Non-vanishing

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/l-function-non-vanishing` · **Status:** open

## 1. Problem Statement / Conjecture

Let $L(s,\pi)$ be an $L$-function attached to an automorphic representation $\pi$ (or to a Dirichlet character, modular form, elliptic curve, or motive). Two families of non-vanishing questions are open.

**(A) Central non-vanishing (Chowla's conjecture and its generalizations).** For every primitive Dirichlet character $\chi$ modulo $q$,
$$L\!\left(\tfrac12,\chi\right)\neq 0 .$$
Chowla stated this for real (quadratic) $\chi$; the expected generalization is that $L(\tfrac12,\pi)\neq 0$ for every self-dual $\pi$ whose functional equation has sign $+1$, and more generally that vanishing at $s=\tfrac12$ occurs only when forced by the sign of the functional equation or by an arithmetic reason (Birch–Swinnerton-Dyer rank, a Deligne–Beilinson cycle class).

**(B) Non-vanishing on the edge $\Re s = 1$, effectively.** For $\pi$ unitary cuspidal on $\mathrm{GL}_n/\mathbb{Q}$, $L(1+it,\pi)\neq 0$ is known; what is open is an *effective* zero-free region — in particular the elimination of **Landau–Siegel zeros**: real zeros $\beta$ of $L(s,\chi_d)$ with $\chi_d$ a real primitive character and $\beta > 1 - c/\log|d|$ for an absolute $c>0$.

A complete resolution of (A) means a proof for all $q$ (or a counterexample $\chi$ with $L(\tfrac12,\chi)=0$); of (B), an effective constant $c$ with no exceptional real zero, or an unconditional construction of such a zero.

## 2. Mathematical Foundations

**Dirichlet $L$-functions.** For $\chi$ primitive mod $q$,
$$L(s,\chi)=\sum_{n\ge 1}\frac{\chi(n)}{n^{s}}=\prod_{p}\left(1-\chi(p)p^{-s}\right)^{-1},\qquad \Re s>1 .$$
With $a=\tfrac{1-\chi(-1)}{2}$ and completed function $\Lambda(s,\chi)=(q/\pi)^{(s+a)/2}\Gamma\!\left(\frac{s+a}{2}\right)L(s,\chi)$, one has
$$\Lambda(s,\chi)=\varepsilon(\chi)\,\Lambda(1-s,\overline{\chi}),\qquad \varepsilon(\chi)=\frac{\tau(\chi)}{i^{a}\sqrt{q}},\quad |\varepsilon(\chi)|=1 ,$$
where $\tau(\chi)=\sum_{n \bmod q}\chi(n)e^{2\pi i n/q}$. For real $\chi$, $\varepsilon(\chi)=+1$, so the sign never forces a central zero — this is why Chowla's prediction is clean.

**General setting.** For a unitary cuspidal automorphic representation $\pi$ of $\mathrm{GL}_n(\mathbb{A}_\mathbb{Q})$ with analytic conductor $\mathfrak{q}(\pi)$,
$$\Lambda(s,\pi)=\mathfrak{q}(\pi)^{s/2}\prod_{j=1}^{n}\Gamma_{\mathbb{R}}(s+\mu_j)\,L(s,\pi)=\varepsilon(\pi)\Lambda(1-s,\tilde\pi).$$

**Approximate functional equation.** For $\Lambda$ self-dual with sign $\varepsilon=+1$,
$$L\!\left(\tfrac12,\pi\right)=2\sum_{n\ge1}\frac{\lambda_\pi(n)}{\sqrt n}\,V\!\left(\frac{n}{\sqrt{\mathfrak{q}(\pi)}}\right),$$
with $V$ a smooth cutoff. The sum has effective length $\sqrt{\mathfrak{q}}$: individual evaluation is out of reach, so one studies **moments over families**.

**Mollified moment method.** Let $\mathcal{F}$ be a family with $|\mathcal{F}|\to\infty$, $M(\pi)=\sum_{m\le M}\frac{\mu_\psi(m)\lambda_\pi(m)}{\sqrt m}$ a mollifier. Cauchy–Schwarz gives
$$\\#\{\pi\in\mathcal F: L(\tfrac12,\pi)\neq0\}\ \ge\ \frac{\left|\sum_{\pi}L(\tfrac12,\pi)M(\pi)\right|^{2}}{\sum_{\pi}\left|L(\tfrac12,\pi)M(\pi)\right|^{2}} .$$
The mollifier length $M=|\mathcal F|^{\theta}$ is limited by the available large sieve / Petersson–Kuznetsov input; $\theta$ controls the resulting proportion.

**Symmetry type (Katz–Sarnak).** Families carry a symmetry group $G\in\{U,\ Sp,\ O,\ SO(\text{even}),\ O(\text{odd})\}$ predicting the low-lying zero statistics. Unitary (all $\chi$ mod $q$) and symplectic (quadratic twists) families predict $100\%$ non-vanishing; even orthogonal families predict $0\%$ vanishing but with a *positive count*, e.g. $\asymp X^{3/4}\log^{c}X$ vanishings among quadratic twists $|d|\le X$ of a fixed elliptic curve (Conrey–Keating–Rubinstein–Snaith).

**Class number formula (real $\chi$ at $s=1$).** For a fundamental discriminant $d<0$,
$$L(1,\chi_d)=\frac{2\pi h(d)}{w(d)\sqrt{|d|}}>0 ,$$
which forces non-vanishing at $s=1$ but gives no effective lower bound near $1$ — Siegel's theorem $L(1,\chi_d)\gg_\epsilon |d|^{-\epsilon}$ is ineffective.

## 3. History & State of the Art (SOTA)

- **1837/1839** — Dirichlet: $L(1,\chi)\neq0$ for $\chi\neq\chi_0$, giving primes in arithmetic progressions; the real-character case handled via the class number formula.
- **1896** — Hadamard and de la Vallée Poussin independently: $\zeta(1+it)\neq0$, hence the Prime Number Theorem.
- **1935–36** — Landau, Siegel: at most one exceptional real zero per range; Siegel's ineffective bound.
- **1965** — Chowla conjectures $L(\tfrac12,\chi)\neq0$ for real primitive $\chi$.
- **1976** — Jacquet–Shalika: $L(1+it,\pi)\neq0$ for cuspidal $\pi$ on $\mathrm{GL}_n$.
- **1981** — Waldspurger; Kohnen–Zagier: central values of quadratic twists of modular $L$-functions equal (up to explicit factors) squares of half-integral-weight Fourier coefficients.
- **1990–91** — Bump–Friedberg–Hoffstein, Murty–Murty: for a modular form $f$ of analytic rank $\le1$, infinitely many quadratic twists with $L(\tfrac12,f\otimes\chi_d)\neq0$; combined with Gross–Zagier and Kolyvagin, this resolved the effective class number problem for $h(d)=3$ and gave Goldfeld's effective lower bound.
- **1998** — Ono–Skinner: $\gg X/\log X$ twists with non-vanishing central value.
- **1999–2000** — Iwaniec–Sarnak: $\ge\tfrac13$ of $\chi$ mod $q$ have $L(\tfrac12,\chi)\neq0$; and if the proportion could be pushed past $\tfrac12$ for a suitable family, Landau–Siegel zeros would be eliminated.
- **2000** — Soundararajan: $\ge 87.5\%$ of the quadratic characters $\chi_{8d}$ ($d$ odd, squarefree, positive) have $L(\tfrac12,\chi_{8d})\neq0$.
- **2002** — Conrey–Keating–Rubinstein–Snaith: random-matrix prediction for the *number* of vanishing quadratic twists.
- **2012–2019** — Bui ($34.11\%$), Khan–Ngo ($\tfrac{5}{13}\approx38.5\%$ for special prime moduli), Pratt ($>50.073\%$ on average over moduli $q\le Q$).
- **2015–2017** — Radziwiłł–Soundararajan (moments/distribution of quadratic-twist central values); A. Smith's $2^\infty$-Selmer method, yielding Goldfeld's conjecture for large classes of elliptic curves.

## 4. Partial Results / Verified Cases

| Family | Result | Source |
|---|---|---|
| $\chi$ mod $q$, all primitive | $\ge 1/3$ non-vanishing at $1/2$ | Iwaniec–Sarnak 1999 |
| $\chi$ mod $q$, $q$ prime, $q\equiv 1\ (4)$ special | $\ge 5/13$ | Khan–Ngo 2016 |
| $\chi$ mod $q$, averaged over $q\le Q$ | $>50.073\%$ | Pratt 2019 |
| $\chi_{8d}$, $d>0$ odd squarefree | $\ge 87.5\%$ | Soundararajan 2000 |
| Real $\chi$ at $s=1$ | $L(1,\chi_d)>0$ always (class number formula) | Dirichlet 1839 |
| $\mathrm{GL}_n$ cuspidal, $\Re s=1$ | $L(1+it,\pi)\neq0$ | Jacquet–Shalika 1976 |
| Quadratic twists of a fixed newform $f$ | $\gg X/\log X$ non-vanishing with $|d|\le X$ | Ono–Skinner 1998 |
| $E/\mathbb{Q}$ with full rational $2$-torsion, quadratic twists | $100\%$ have rank $0$ or $1$ (so $50\%$ non-vanishing among even twists) | A. Smith |
| Numerical | $L(\tfrac12,\chi)\neq0$ verified for all primitive $\chi$ with $q$ up to $\sim 10^{5}$–$10^{6}$ | Rubinstein's `lcalc` computations |
| $\zeta$ on $\Re s = 1$ | zero-free with region $1-c/\log^{2/3}t(\log\log t)^{1/3}$ | Vinogradov–Korobov |

No Landau–Siegel zero has ever been found; none is excluded.

## 5. Principal Obstacles

- **No individual access.** The approximate functional equation has length $\sqrt{\mathfrak q}$; subconvexity (Michel–Venkatesh for $\mathrm{GL}_2$) saves a power of $\mathfrak q$ in *size* but never reaches the $0$ threshold, since a bound $|L(\tfrac12,\pi)|\ll \mathfrak q^{\delta}$ says nothing about vanishing. Only lower bounds could, and no unconditional lower bound for an individual central value exists.
- **The $50\%$ barrier for mollified moments.** The proportion is $\theta/(1+\theta)$-shaped in the mollifier length $\theta$; getting past $\tfrac12$ needs $\theta>1$, i.e. a mollifier longer than the family size. The second moment's off-diagonal terms then require cancellation in Kloosterman sums beyond what Weil's bound and the Kuznetsov formula deliver — this is the same wall as the Linnik/Selberg $\theta$-conjecture.
- **Circularity with Siegel zeros.** A Landau–Siegel zero would itself change the arithmetic of the family (it makes $\mu(n)$ and $\Lambda(n)$ behave like a character-twisted sequence), so many non-vanishing arguments only work *because* one assumes no such zero. Iwaniec–Sarnak's theorem makes the coupling explicit and shows the two problems are not independent.
- **Ineffectivity.** Siegel's proof compares two discriminants and cannot produce constants; no known route to $L(1,\chi_d)\gg 1/\log|d|$ effectively except through Gross–Zagier–type inputs that themselves require non-vanishing.
- **Positive-proportion $\ne$ all.** Even a $100\%$ density theorem does not rule out a sparse set of vanishing values; Chowla's conjecture is a statement about *every* $\chi$, and density methods are structurally incapable of it.

## 6. The Gap

Proven: positive-density non-vanishing for large families ($\ge 87.5\%$ symplectic, $\ge 1/3$ unitary), plus every case where the sign is $-1$ and rank $\le1$ arithmetic applies. Conjectured: non-vanishing for *each individual* $\chi$ or $\pi$.

The gap has two precise crossings:

1. **From density to universality.** One needs a lower bound of the form $|L(\tfrac12,\chi)| \gg q^{-A}$ valid for every primitive $\chi$. Nothing in the moment method produces pointwise lower bounds; a genuinely new principle (a positivity, an $\ell$-adic cycle-class construction, or a trace formula with a positive-definite kernel isolating one $\chi$) is required.
2. **From $\theta<1$ to $\theta>1$.** For Dirichlet families, exceeding mollifier length $q$ would simultaneously yield the $>1/2$ proportion and, by Iwaniec–Sarnak, kill Landau–Siegel zeros. This is the concrete, quantified barrier: everything reduces to bilinear/Kloosterman cancellation past the Weil range.

## 7. Current Research (as of June 2026)

- **Longer mollifiers and twisted moments.** Khan, Ngo, Nguyen and collaborators continue pushing two-piece mollifiers and fourth-moment inputs for Dirichlet $L$-functions; incremental gains above $5/13$ for restricted moduli are reported *(frontier — verify)*.
- **Siegel-zero conditional worlds.** Following work of Heath-Brown and the "illusory world" framework, several groups derive strong consequences (twin-prime-type results, Chebotarev improvements) from a hypothetical Siegel zero, with the aim of a contradiction. No contradiction has been reached.
- **Function-field and geometric analogues.** Katz's equidistribution machinery gives complete non-vanishing statements over $\mathbb{F}_q(t)$ for large $q$; transferring the monodromy input to number fields remains blocked.
- **Half-integral weight and theta correspondence.** Effective Waldspurger-type formulas (Baruch–Mao, Popa) convert central values into Fourier coefficients; equidistribution of Heegner points supplies non-vanishing for sub-families.
- **Selmer-group statistics.** Building on A. Smith's $2^\infty$-descent, work extending Goldfeld's conjecture to curves without full $2$-torsion is active *(frontier — verify)*; via BSD this is a non-vanishing statement for $100\%$ of even quadratic twists.
- **Groups.** Stanford (Sarnak school), Michigan/Rutgers analytic number theory, IHÉS/Paris (Michel, Venkatesh circle), Oxford, Bristol (random matrix theory), MSRI/SLMath programs on $L$-functions.

## 8. Future Work

- Prove an unconditional pointwise lower bound $|L(\tfrac12,\chi_d)|\gg |d|^{-1/4+\delta}$, which by Waldspurger's formula reduces to nontrivial lower bounds on half-integral weight Fourier coefficients.
- Obtain cancellation in sums of Kloosterman sums beyond Weil, in the specific bilinear ranges that unlock $\theta>1$ mollifiers.
- Develop a positivity-based framework (analogue of the Riemann–Roch positivity in function fields, or a Bombieri–Weil explicit-formula positivity) that isolates individual central values.
- Prove the effective elimination of Siegel zeros for the *fixed* family of real characters, perhaps via the trace-formula strategy of Iwaniec–Sarnak combined with sieve inputs.
- Extend Katz–Sarnak symmetry predictions into rigorous transfer principles between function-field monodromy and number-field families.

## 9. Key References

- **[Foundational]** J. Hadamard. *Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques.* Bulletin de la Société Mathématique de France 24, 1896.
- **[Foundational]** H. Jacquet, J. Shalika. *A non-vanishing theorem for zeta functions of $GL_n$.* Inventiones Mathematicae 38, 1976.
- **[Foundational]** S. Chowla. *The Riemann Hypothesis and Hilbert's Tenth Problem.* Gordon and Breach, 1965.
- **[Foundational]** J.-L. Waldspurger. *Sur les coefficients de Fourier des formes modulaires de poids demi-entier.* Journal de Mathématiques Pures et Appliquées 60, 1981.
- **[Foundational]** W. Kohnen, D. Zagier. *Values of $L$-series of modular forms at the center of the critical strip.* Inventiones Mathematicae 64, 1981.
- **[SOTA]** K. Soundararajan. *Nonvanishing of quadratic Dirichlet $L$-functions at $s=\tfrac12$.* Annals of Mathematics 152(2), 2000, 447–488.
- **[SOTA]** H. Iwaniec, P. Sarnak. *The non-vanishing of central values of automorphic $L$-functions and Landau–Siegel zeros.* Israel Journal of Mathematics 120, 2000, 155–177.
- **[SOTA]** H. Iwaniec, P. Sarnak. *Dirichlet $L$-functions at the central point.* In: Number Theory in Progress, vol. 2, de Gruyter, 1999.
- **[SOTA]** R. Khan, H. Ngo. *Nonvanishing of Dirichlet $L$-functions.* Algebra & Number Theory 10(10), 2016.
- **[SOTA]** K. Pratt. *Average non-vanishing of Dirichlet $L$-functions at the central point.* Algebra & Number Theory 13(1), 2019.
- **[SOTA]** M. Radziwiłł, K. Soundararajan. *Moments and distribution of central $L$-values of quadratic twists of elliptic curves.* Inventiones Mathematicae 202, 2015.
- **[SOTA]** D. Bump, S. Friedberg, J. Hoffstein. *Nonvanishing theorems for $L$-functions of modular forms and their derivatives.* Inventiones Mathematicae 102, 1990.
- **[SOTA]** K. Ono, C. Skinner. *Non-vanishing of quadratic twists of modular $L$-functions.* Inventiones Mathematicae 134, 1998.
- **[Survey]** H. Iwaniec, E. Kowalski. *Analytic Number Theory.* AMS Colloquium Publications 53, 2004.
- **[Survey]** N. Katz, P. Sarnak. *Zeroes of zeta functions and symmetry.* Bulletin of the AMS 36(1), 1999.
- **[Survey]** J. B. Conrey, J. P. Keating, M. Rubinstein, N. Snaith. *On the frequency of vanishing of quadratic twists of modular $L$-functions.* In: Number Theory for the Millennium I, A K Peters, 2002.

## 10. Worked Example / Concrete Special Case

**Case $\chi_{-4}$: non-vanishing at $s=1$, and the size problem at $s=1/2$.**

Take the real primitive character mod $4$: $\chi_{-4}(1)=1,\ \chi_{-4}(3)=-1,\ \chi_{-4}(\text{even})=0$. Then
$$L(s,\chi_{-4})=1-3^{-s}+5^{-s}-7^{-s}+\cdots$$

*At $s=1$.* The series converges conditionally to the Leibniz value
$$L(1,\chi_{-4})=1-\tfrac13+\tfrac15-\tfrac17+\cdots=\frac{\pi}{4}\approx 0.7854\neq0 .$$
This matches the class number formula with $d=-4$, $h(-4)=1$, $w(-4)=4$:
$$\frac{2\pi h}{w\sqrt{|d|}}=\frac{2\pi\cdot1}{4\cdot2}=\frac{\pi}{4}. \checkmark$$
The formula shows *why* the value is nonzero: it is $2\pi/(w\sqrt{|d|})$ times a **positive integer** $h(d)\ge1$. Non-vanishing is automatic; but the bound it yields, $L(1,\chi_d)\ge 2\pi/(w\sqrt{|d|})$, decays like $|d|^{-1/2}$ — far too weak to exclude a real zero at $1-c/\log|d|$, since by the mean value theorem such a zero would force $L(1,\chi_d)\ll (\log|d|)\cdot c/\log|d| \asymp c$. This is exactly the gap Siegel's ineffective $L(1,\chi_d)\gg_\epsilon|d|^{-\epsilon}$ fills, and why no effective constant is known.

*At $s=1/2$.* Since $\chi_{-4}$ is odd and real, $\varepsilon(\chi_{-4})=+1$ and the approximate functional equation reads
$$L\!\left(\tfrac12,\chi_{-4}\right)=2\sum_{n\ge1}\frac{\chi_{-4}(n)}{\sqrt n}\,V\!\left(\frac{n}{2}\right),$$
a sum of effective length $\sqrt q=2$. Numerically $L(\tfrac12,\chi_{-4})\approx 0.6676\neq0$. For $q=10^{6}$ the same sum has length $10^{3}$ with terms of size $n^{-1/2}$ and square-root cancellation, so the *predicted* size is $O(q^{\epsilon})$ while the trivial bound is $O(q^{1/2})$ — and no argument distinguishes "small" from "zero" for a single $\chi$. That distinction, not the numerics, is the content of Chowla's conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*