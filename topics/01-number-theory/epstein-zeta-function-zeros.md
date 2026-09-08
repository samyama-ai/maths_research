---
id: 01-number-theory/epstein-zeta-function-zeros
title: "Multiplicative Structure of Zeros: Zeros of the Epstein Zeta Function"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Multiplicative Structure of Zeros: Zeros of the Epstein Zeta Function

> **Topic:** Number Theory · **ID:** `01-number-theory/epstein-zeta-function-zeros` · **Status:** open

## 1. Problem Statement / Conjecture

Let $Q$ be a positive definite quadratic form in $n$ variables with real coefficients. Its Epstein zeta function is
$$Z_Q(s)=\sum_{\mathbf{m}\in\mathbb{Z}^n\setminus\{0\}} Q(\mathbf{m})^{-s},\qquad \Re s>\tfrac n2 ,$$
continued meromorphically to $\mathbb{C}$ with a single simple pole at $s=n/2$ and a functional equation relating $s$ to $n/2-s$. Although $Z_Q$ has the analytic shape of an $L$-function, it has **no Euler product** unless $Q$ is (up to scaling) associated to a class group of order one. The problem is to determine how the zeros respond to this failure of multiplicativity.

Three linked questions, all open in general:

1. **(RH cases.)** If $Q$ is a binary form of discriminant $D<0$ with class number $h(D)=1$, then $Z_Q(s)=\frac{2}{w}\zeta(s)L(s,\chi_D)$ and all non-trivial zeros should lie on $\Re s=\tfrac12$. This is exactly RH $+$ GRH for $L(s,\chi_D)$; it is unproved for every one of the nine such $D$.
2. **(Off-line density.)** If $h(D)>1$, $Z_Q$ provably has zeros off the critical line. Conjecturally, for every $\tfrac12<\sigma_1<\sigma_2<1$ the count $N_Q(\sigma_1,\sigma_2,T)$ of zeros $\beta+i\gamma$ with $\sigma_1<\beta<\sigma_2$, $0<\gamma<T$ satisfies $N_Q(\sigma_1,\sigma_2,T)\sim c\,T$ with an explicit $c=c(\sigma_1,\sigma_2,Q)>0$, and **all but $o(T)$ of the zeros in $0<\gamma<T$ lie in $|\beta-\tfrac12|<\varepsilon$.**
3. **(Selberg's positive proportion.)** Even when $h(D)>1$, a **positive proportion** of the zeros of $Z_Q$ should lie exactly on $\Re s=\tfrac12$.

A complete resolution means proving (1) for at least one $h=1$ discriminant, and proving (2) and (3) unconditionally for all $Q$ with $h>1$; a disproof of (3) would be a counterexample form for which the critical-line zero count is $o(T)$.

## 2. Mathematical Foundations

**Functional equation (Epstein, 1903).** For $Q(\mathbf{x})=\tfrac12\mathbf{x}^{T}A\mathbf{x}$ with $A$ positive definite symmetric,
$$\Lambda_Q(s):=\pi^{-s}\Gamma(s)Z_Q(s)=(\det A)^{-1/2}\,\Lambda_{Q^{-1}}\!\left(\tfrac n2-s\right),$$
proved by Poisson summation applied to the theta series $\theta_Q(t)=\sum_{\mathbf m\in\mathbb Z^n}e^{-\pi t Q(\mathbf m)}$ via the Mellin transform $\Lambda_Q(s)=\tfrac12\int_0^\infty (\theta_Q(t)-1)t^{s}\frac{dt}{t}$. The critical line is $\Re s=n/4$ after normalizing $\det A=1$; for binary forms it is $\Re s=\tfrac12$ in the classical normalization below.

**Binary forms and the modular picture.** For $Q(x,y)=ax^2+bxy+cy^2$, $D=b^2-4ac<0$, set $z_Q=\dfrac{-b+\sqrt{D}}{2a}\in\mathbb H$, $y_Q=\Im z_Q=\dfrac{\sqrt{|D|}}{2a}$. Then
$$Z_Q(s)=\left(\frac{2}{\sqrt{|D|}}\right)^{s} E(z_Q,s),\qquad E(z,s)=\sum_{(m,n)\neq(0,0)}\frac{y^{s}}{|mz+n|^{2s}},$$
the real-analytic Eisenstein series. $E(\cdot,s)$ is $\mathrm{SL}_2(\mathbb Z)$-invariant and satisfies $\Delta E=s(1-s)E$, so zeros of $Z_Q$ are zeros of an eigenfunction along a fixed point of $\mathbb H$.

**Class-group decomposition.** For $D<0$ a fundamental discriminant with class group $\mathrm{Cl}(D)$ of order $h$ and $w$ roots of unity,
$$\zeta_K(s)=\frac1w\sum_{C\in \mathrm{Cl}(D)}Z_{Q_C}(s)=\zeta(s)L(s,\chi_D),$$
and for each character $\psi$ of $\mathrm{Cl}(D)$, $\sum_C \psi(C)Z_{Q_C}(s)=w\,L(s,\psi)$ with $L(s,\psi)$ a Hecke $L$-function (degree 2, Euler product). Inverting by orthogonality,
$$Z_{Q_C}(s)=\frac{w}{h}\sum_{\psi\in\widehat{\mathrm{Cl}(D)}}\overline{\psi(C)}\,L(s,\psi).$$
So **each individual $Z_Q$ is a finite linear combination of Euler products with the same degree, conductor and $\Gamma$-factor, and is itself an Euler product only when $h=1$.** This is the "multiplicative structure" at issue: Euler products constrain zeros to $\Re s\le \tfrac12$ conjecturally, linear combinations of them do not.

**Chowla–Selberg formula.** $\prod_{C}Z_{Q_C}(s)$ has a closed evaluation at $s=1$ in terms of $\Gamma$-values at rational arguments; equivalently the Kronecker limit formula gives
$$E(z,s)=\frac{\pi}{s-1}+2\pi\big(\gamma-\log 2-\log(\sqrt{y}\,|\eta(z)|^2)\big)+O(s-1),$$
linking the analytic behavior of $Z_Q$ near $s=1$ to the Dedekind $\eta$-function.

**Universality (Voronin, Bagchi).** For $h>1$, $Z_Q$ is universal in the strip $\tfrac12<\sigma<1$: any nonvanishing analytic $f$ on a compact disc there is approximated by $Z_Q(s+i\tau)$ for a set of $\tau$ of positive lower density. Universality forces $\gg T$ zeros in every substrip $\sigma_1<\sigma<\sigma_2\subset(\tfrac12,1)$.

## 3. History & State of the Art (SOTA)

- **1903/1907** — Paul Epstein, *Zur Theorie allgemeiner Zetafunktionen* I, II (Math. Ann. 56, 63): definition, continuation, functional equation.
- **1935** — Potter and Titchmarsh (Proc. LMS): $Z_Q$ has infinitely many zeros on the critical line, and for suitable $Q$ zeros with $\Re s>1$, i.e. outside the region where an Euler product would forbid them.
- **1936** — Davenport and Heilbronn (*On the zeros of certain Dirichlet series* I, II, J. LMS): if $h(D)>1$ (they used one-class-per-genus discriminants such as $D=-20$), $Z_Q$ has infinitely many zeros in $\Re s>1$, hence off the critical line. The proof rests on Bohr's almost-periodicity plus Kronecker's theorem on independence of $\log p$.
- **1949/1967** — Chowla and Selberg, *On Epstein's zeta function* (PNAS 35; J. reine angew. Math. 227).
- **1964** — Bateman and Grosswald (Acta Arith.): if the reduction point has $y_Q$ larger than an explicit constant (their argument gives $y_Q>4.4$), $Z_Q$ has a **real** zero in $(\tfrac12,1)$; conversely for small $y_Q$ the real segment is zero-free.
- **1967** — Stark, *On the zeros of Epstein's zeta function* (Mathematika 14): zero-free regions and the tie to the class-number-one problem.
- **1975–76** — Voronin: universality; infinitude of critical-line zeros for a broad class.
- **1986–95** — Hejhal ("Zeros of Epstein zeta functions and supercomputers", ICM Berkeley 1986) and Bombieri–Hejhal (Duke Math. J. 80, 1995): value distribution and the conditional positive-proportion machinery for linear combinations of Euler products.
- **2005** — Jutila and Srinivas (Bull. LMS 37): gaps between critical-line zeros; $\gg T^{4/5}$-type lower bounds for the critical-line count in ranges.
- **2008** — Bombieri and Mueller, *On the zeros of certain Epstein zeta functions* (Forum Math. 20): sharp quantitative results for two-term combinations.
- **2006** — Sarnak and Strömbergsson (Invent. Math. 165): minima of $E(z,s)$ and heights of flat tori, controlling $Z_Q$ on the real line in dimensions $n=4,8,24$.
- **2010s** — Yoonbok Lee and collaborators: asymptotics $N_Q(\sigma_1,\sigma_2,T)=c\,T+O(T^{1-\delta})$ for off-line zeros of Epstein and related non-Euler-product zeta functions.

## 4. Partial Results / Verified Cases

- **$h(D)=1$, i.e. $D\in\{-3,-4,-7,-8,-11,-19,-43,-67,-163\}$:** $Z_Q=\frac2w\zeta(s)L(s,\chi_D)$; the Riemann hypothesis for $Z_Q$ is *equivalent* to RH $\wedge$ GRH$(\chi_D)$ and is verified numerically far up the critical line (billions of zeros of $\zeta$; comparable heights for the small-conductor $L(s,\chi_D)$).
- **$h(D)>1$:** zeros in $\Re s>1$ exist and number $\gg T$ up to height $T$ (Davenport–Heilbronn; refined by Voronin and by Lee). So the naive RH is **false** for every such form — this part of the problem is settled negatively.
- **Real zeros:** $Z_Q$ has a zero in $(\tfrac12,1)$ whenever $y_Q=\sqrt{|D|}/(2a)$ exceeds an explicit constant (Bateman–Grosswald, $y_Q>4.4$ suffices); for $y_Q$ below an explicit threshold, $Z_Q(\sigma)\ne0$ for $\sigma\in(0,1)$ real.
- **Critical-line counts:** infinitely many zeros on $\Re s=\tfrac12$ for all $Q$ (Potter–Titchmarsh, Voronin); quantitatively $N_Q^{0}(T)\gg T^{4/5-\varepsilon}$ in the best unconditional ranges (Jutila–Srinivas and successors) — short of the conjectured $\gg T$.
- **Conditional positive proportion:** under RH for the constituent Hecke $L$-functions plus a zero-spacing hypothesis, Bombieri–Hejhal give a positive proportion of critical-line zeros for such linear combinations.
- **Higher dimension:** for $n\ge 2$ and $Q$ far from the reduction domain's compact core, $Z_Q$ has real zeros in $(0,n/2)$; for $n=4,8,24$ the extremal lattices $D_4,E_8,\Lambda_{24}$ are proved to minimize $Z_Q(s)$ among unimodular lattices for all $s>0$ (Sarnak–Strömbergsson).

## 5. Principal Obstacles

- **No Euler product ⇒ no zero-detection identity.** All classical critical-line methods (Hardy–Littlewood, Levinson, Conrey mollifiers) use a Dirichlet-series mollifier $M(s)=\sum \mu$-like coefficients approximating $1/Z_Q(s)$. For a **sum** of Euler products, $1/Z_Q$ has no multiplicative coefficients and no short mollifier; the mollified second moment ceases to have a main term one can compute.
- **Almost periodicity works against you.** The same Bohr/Kronecker input that *produces* off-line zeros makes the argument of $Z_Q$ equidistribute; sign-change counting via $\arg Z_Q$ therefore yields only $T^{\theta}$, $\theta<1$, not $cT$.
- **Cancellation between constituents.** Writing $Z_Q=\sum_\psi c_\psi L(s,\psi)$, critical-line zeros arise where the $L(s,\psi)$ nearly cancel. Controlling near-cancellation needs joint value-distribution of the $L(s,\psi)$ at the same height with *effective* error terms; only Selberg-type CLT statements (density-one, non-effective) are available.
- **$h=1$ cases are RH itself.** No route to (1) avoids GRH.
- **Rigidity failure of the spectral picture.** $E(z,s)$ zeros in $s$ for fixed $z$ are not the spectrum of a self-adjoint operator; the Maass–Selberg relation controls $E$ only along $\Re s=\tfrac12$ in $L^2$-average, and it degenerates precisely where zeros are.

## 6. The Gap

Proven: off-line zeros exist and have density $\asymp T$ (Section 4). Proven: on-line zeros are infinite and $\gg T^{4/5-\varepsilon}$. Conjectured: on-line zeros are $\gg T$, and the off-line zeros — despite being $\asymp T$ many — cluster at $\Re s=\tfrac12+o(1)$ so that $N_Q(\sigma_1,\sigma_2,T)=o(N_Q(T))$ for fixed $\sigma_1>\tfrac12$.

The exact missing step: **an unconditional mollified second moment for a linear combination of two or more degree-2 Euler products of equal conductor.** Equivalently, one must evaluate
$$\int_0^T \Big|\sum_\psi c_\psi L(\tfrac12+it,\psi)\Big|^2 |M(\tfrac12+it)|^2\,dt$$
with $M$ a Dirichlet polynomial of length $T^{\theta}$, $\theta>0$ fixed, where the off-diagonal terms mix *different* $\psi$'s. The diagonal (same $\psi$) is standard; the cross terms are shifted-convolution sums for Hecke eigenvalues of two distinct class characters, which no known method evaluates with a power-saving error when the mollifier is long.

## 7. Current Research (as of June 2026)

- **Off-line zero asymptotics.** Lee's program (Incheon National University) gives $c\,T+O(T^{1-\delta})$ asymptotics for zero counts of Epstein and other non-Euler-product Dirichlet series in $(\tfrac12,1)$; recent work extends to joint distribution of several forms of the same discriminant. *(frontier — verify current status of the higher-dimension extension.)*
- **Moment technology for combinations.** Groups working on random-matrix models for linear combinations (Bombieri–Hejhal descendants; Bristol/Oxford analytic-number-theory circles) model $Z_Q$ as a sum of independent characteristic polynomials, predicting the constant in the conjectured $\kappa\cdot T\log T$ critical-line count with $\kappa<1$ strictly. *(frontier — verify)*
- **Geometric/extremal side.** Post-Sarnak–Strömbergsson work on $Z_Q(s)$ minima and lattice-height functionals, tied to sphere-packing rigidity in dimensions 8 and 24 after Viazovska.
- **Computational.** High-precision zero computations for $D=-20,-23,-24$ classes, using the Eisenstein-series representation and rapidly convergent Bessel expansions, mapping the migration of zeros as $y_Q$ grows.
- **Selberg-class framing.** Conditional work on the "degree conjecture" and on which linear combinations can be forced back into the class; $Z_Q$ with $h>1$ is the standard witness that the Selberg class is not closed under addition.

## 8. Future Work

- Build a mollifier adapted to a *sum* of Euler products — e.g. a mollifier for $\prod_\psi L(s,\psi)=\zeta_K(s)\cdot(\text{Artin factors})$ divided out — to convert the problem to a Levinson-type argument for $\zeta_K$ with an entire correction factor.
- Prove effective joint value-distribution (a quantitative multidimensional Selberg CLT with power-saving error) for the family $\{L(s,\psi)\}_{\psi\in\widehat{\mathrm{Cl}(D)}}$; this alone would upgrade $T^{4/5}$ toward $T/\log T$.
- Settle the density conjecture: show $N_Q(\sigma,\infty,T)\ll T^{1-\delta(\sigma)}$ for fixed $\sigma>\tfrac12+\varepsilon$, i.e. that off-line zeros do not escape the immediate neighborhood of $\Re s=\tfrac12$ in positive proportion.
- Extend the Sarnak–Strömbergsson extremality to a full description of the real zeros of $Z_Q$ on the reduction domain in every dimension $n$.

## 9. Key References

- **[Foundational]** P. Epstein. *Zur Theorie allgemeiner Zetafunktionen.* Mathematische Annalen 56 (1903), 615–644; II, Math. Ann. 63 (1907), 205–216.
- **[Foundational]** H. S. A. Potter, E. C. Titchmarsh. *The zeros of Epstein's zeta-functions.* Proceedings of the London Mathematical Society (2) 39 (1935), 372–384.
- **[Foundational]** H. Davenport, H. Heilbronn. *On the zeros of certain Dirichlet series* I, II. Journal of the London Mathematical Society 11 (1936), 181–185 and 307–312.
- **[Foundational]** S. Chowla, A. Selberg. *On Epstein's zeta function (I).* Proceedings of the National Academy of Sciences USA 35 (1949), 371–374; and *On Epstein's zeta-function*, Journal für die reine und angewandte Mathematik 227 (1967), 86–110.
- **[Classical]** P. T. Bateman, E. Grosswald. *On Epstein's zeta function.* Acta Arithmetica 9 (1964), 365–373.
- **[Classical]** H. M. Stark. *On the zeros of Epstein's zeta function.* Mathematika 14 (1967), 47–55.
- **[SOTA]** E. Bombieri, D. A. Hejhal. *On the distribution of zeros of linear combinations of Euler products.* Duke Mathematical Journal 80 (1995), 821–862.
- **[SOTA]** E. Bombieri, J. Mueller. *On the zeros of certain Epstein zeta functions.* Forum Mathematicum 20 (2008), 359–385.
- **[SOTA]** M. Jutila, K. Srinivas. *Gaps between the zeros of Epstein's zeta-functions on the critical line.* Bulletin of the London Mathematical Society 37 (2005), 45–53.
- **[SOTA]** P. Sarnak, A. Strömbergsson. *Minima of Epstein's zeta function and heights of flat tori.* Inventiones Mathematicae 165 (2006), 115–151.
- **[Survey]** A. Terras. *Harmonic Analysis on Symmetric Spaces and Applications I.* Springer-Verlag, 1985 (Epstein zeta, Eisenstein series, Kronecker limit formula).
- **[Survey]** D. A. Hejhal. *Zeros of Epstein zeta functions and supercomputers.* Proceedings of the International Congress of Mathematicians, Berkeley 1986, 1362–1384.
- **[Survey]** A. Ivić. *The Riemann Zeta-Function: Theory and Applications.* Wiley 1985 / Dover 2003 (mollifier and critical-line methods; limits for non-Euler products).

## 10. Worked Example / Concrete Special Case

Take $D=-20$: two classes, one per genus, $w=2$, with reduced forms
$$Q_1(x,y)=x^2+5y^2,\qquad Q_2(x,y)=2x^2+2xy+3y^2 .$$

**Step 1 — decompose.** The trivial character gives $Z_1+Z_2=2\zeta_K(s)=2\zeta(s)L(s,\chi_{-20})$. The genus character attached to the factorization $-20=(-4)\cdot 5$ gives $Z_1-Z_2=2L(s,\chi_{-4})L(s,\chi_{5})$. Hence
$$Z_1(s)=\zeta(s)L(s,\chi_{-20})+L(s,\chi_{-4})L(s,\chi_5),\qquad Z_2(s)=\zeta(s)L(s,\chi_{-20})-L(s,\chi_{-4})L(s,\chi_5).$$
Check at the level of coefficients: $n=1$ gives $r_{Q_1}(1)=2$ (from $(\pm1,0)$) and $r_{Q_2}(1)=0$; the right sides give $1+1=2$ and $1-1=0$. At $n=2$: $Q_1$ never represents $2$, $Q_2$ does via $(\pm1,0)\Rightarrow r=2$; right sides give $a_{\zeta L}(2)+a_{LL}(2)$ with $\chi_{-20}(2)=0$ so $a_{\zeta L}(2)=1$, and $\chi_{-4}(2)=\chi_5(2)=-1$ wait $\chi_5(2)=-1$, $\chi_{-4}(2)=0$, so $a_{LL}(2)=\chi_{-4}(2)+\chi_5(2)=-1$: $1-1=0$ for $Q_1$ and $1+1=2$ for $Q_2$. Consistent after matching signs of the genus character.

**Step 2 — force a zero off the line.** In $\Re s=\sigma>1$ write
$$\frac{Z_2(s)}{\zeta(s)L(s,\chi_{-20})}=1-F(s),\qquad F(s)=\frac{L(s,\chi_{-4})L(s,\chi_5)}{\zeta(s)L(s,\chi_{-20})}=\prod_p \frac{(1-\chi_{-4}(p)p^{-s})^{-1}(1-\chi_5(p)p^{-s})^{-1}}{(1-p^{-s})^{-1}(1-\chi_{-20}(p)p^{-s})^{-1}} .$$
$\log F(s)=\sum_p \sum_k c_k(p)p^{-ks}/k$ is, for fixed $\sigma>1$, a Bohr almost-periodic function of $t$ whose value distribution is governed by the torus $\{(p^{-it})_p\}$. Kronecker's theorem: the $\log p$ are $\mathbb{Q}$-linearly independent, so $(p^{-it})_p$ equidistributes on $\prod_p S^1$. The first Euler factor $p=3$ has $\chi_{-4}(3)=-1$, $\chi_5(3)=-1$, $\chi_{-20}(3)=1$, giving a factor $\frac{(1+3^{-s})^{-2}}{(1-3^{-s})^{-1}(1-3^{-s})^{-1}}$, whose modulus can be pushed above $1$; combining finitely many such primes one produces $t$-values with $F(s)=1$ exactly, hence $Z_2(s)=0$, at points with $\sigma>1$. This is Davenport–Heilbronn's argument, and $\gg T$ such zeros occur up to height $T$.

**Step 3 — real zeros.** For $Q_2$, $y_{Q_2}=\sqrt{20}/(2\cdot 2)\approx1.118$, below the Bateman–Grosswald threshold, so no real zero in $(\tfrac12,1)$ is forced. Contrast $Q(x,y)=x^2+20y^2$ ($D=-80$), where $y_Q=\sqrt{20}\approx4.47>4.4$: here $Z_Q$ **does** have a real zero $\beta\in(\tfrac12,1)$, a zero that no Euler-product $L$-function is conjectured to possess. The two phenomena — off-line complex zeros from Bohr almost-periodicity and forced real zeros from a skewed lattice — are the two concrete ways the loss of multiplicative structure breaks the Riemann hypothesis for $Z_Q$, while the conjectured picture is that they still account for only $o(T)$ of all zeros.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*