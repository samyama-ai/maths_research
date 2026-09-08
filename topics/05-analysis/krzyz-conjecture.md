---
id: 05-analysis/krzyz-conjecture
title: "Krzyz Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Krzyż Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/krzyz-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbb{D}=\{z\in\mathbb{C}:|z|<1\}$ and let

$$\mathcal{B}_0=\Big\{f:\mathbb{D}\to\mathbb{C}\ \text{holomorphic},\ 0<|f(z)|<1\ \text{for all }z\in\mathbb{D}\Big\}$$

be the class of **bounded non-vanishing** analytic functions on the disc, with Taylor expansion $f(z)=\sum_{n\ge 0}a_n z^n$.

**Conjecture (Krzyż, 1968).** For every $f\in\mathcal{B}_0$ and every $n\ge 1$,

$$|a_n|\;\le\;\frac{2}{e}\;=\;0.7357588\ldots$$

with equality only for the rotations $f(z)=\lambda K_n(\mu z)$, $|\lambda|=|\mu|=1$, of

$$K_n(z)=\exp\!\left(\frac{z^n-1}{z^n+1}\right)=\frac1e\left(1+\frac{2}{1}z^n+\cdots\right).$$

A complete solution requires proving the bound for **all** $n$ together with the uniqueness of the extremals; a disproof requires exhibiting one $f\in\mathcal{B}_0$ and one index $n$ with $|a_n|>2/e$. Note that dropping non-vanishing gives only the sharp trivial bound $|a_n|\le 1$ (Schwarz), so the conjecture quantifies exactly how much the omission of the value $0$ costs.

## 2. Mathematical Foundations

**Exponential representation.** Since $\mathbb{D}$ is simply connected and $f$ omits $0$, $\log f$ has a single-valued branch. Put $p=-\log f$. Then $|f|<1\iff \operatorname{Re}p>0$, so

$$f=e^{-p},\qquad p(z)=\sum_{k\ge0}c_kz^k,\ \ \operatorname{Re}p>0 .$$

Herglotz representation: there is a finite positive Borel measure $\mu$ on $\partial\mathbb{D}$ and $\beta\in\mathbb{R}$ with

$$p(z)=i\beta+\int_{\partial\mathbb{D}}\frac{e^{i\theta}+z}{e^{i\theta}-z}\,d\mu(\theta),\qquad c_0=\mu(\partial\mathbb{D})+i\beta,\quad c_k=2\int_{\partial\mathbb{D}}e^{-ik\theta}d\mu(\theta)\ (k\ge1).$$

Hence the **Carathéodory inequality** $|c_k|\le 2\operatorname{Re}c_0$ for all $k\ge1$.

**Coefficient functional.** Writing $t=\operatorname{Re}c_0>0$ and expanding the exponential,

$$a_n=e^{-c_0}\sum_{k=1}^{n}\frac{(-1)^k}{k!}\sum_{\substack{j_1+\cdots+j_k=n\\ j_i\ge1}}c_{j_1}\cdots c_{j_k},\qquad |a_0|=e^{-t}. \tag{2.1}$$

The conjecture is the assertion $\sup_{\mu,\beta}|a_n|=2/e$, a nonlinear extremal problem over the convex cone of positive measures — the functional (2.1) is **not** linear in $\mu$ for $n\ge2$, which is the source of all difficulty.

**Extremal candidate.** For $n=1$, $p(z)=\frac{1-z}{1+z}$ (i.e. $\mu=\delta_{\pi}$ scaled, $t=1$) gives $K_1(z)=e^{-1}\exp\!\big(\tfrac{2z}{1+z}\big)$ whose coefficients are Laguerre values:

$$K_1(z)=\frac1e\sum_{n\ge0}(-1)^nL_n^{(-1)}(2)\,z^n,\qquad \sum_{n\ge0}L_n^{(-1)}(x)t^n=e^{-xt/(1-t)} .$$

Since $L_1^{(-1)}(2)=-2$, $a_1=2/e$. The functions $K_n(z)=K_1(z^n)$ transplant this to the $n$-th coefficient.

**Auxiliary classical facts used throughout:** the Schur–Wiener bound $|a_n|\le 1-|a_0|^2$ for $|f|\le1$, $n\ge1$; Parseval $\sum_n|a_n|^2\le1$; the Riesz–Herglotz theory of the Carathéodory class $\mathcal{P}$; and the extreme-point structure of $\mathcal P$ (the extreme points are $\frac{1+\bar\zeta z}{1-\bar\zeta z}$, $|\zeta|=1$).

## 3. History & State of the Art (SOTA)

- **1968.** Jan Krzyż posed the problem in the problem section of *Annales Polonici Mathematici* 20 (1968), p. 314, asking for $\max|a_n|$ over bounded non-vanishing functions.
- **1977.** Hummel, Scheinberg and Zalcman developed a variational method adapted to $\mathcal{B}_0$, proved existence and boundary-behaviour properties of extremal functions (they satisfy an algebraic differential equation, and the associated measure $\mu$ is singular), and settled $n\le3$.
- **1978.** Horowitz obtained the first uniform improvement over the trivial bound: $|a_n|\le 1-\delta$ for an explicit absolute $\delta>0$ (numerically $\approx 10^{-4}$, i.e. $|a_n|\le 0.9998\ldots$) — a large gap from $2/e$ but a proof that the trivial bound is never attained. *(numerical value as reported — verify)*
- **1981.** Prokhorov and Szynal settled $n=4$.
- **1990.** Ermers' Nijmegen thesis reorganised the variational machinery, reproved $n\le4$ and improved the uniform bound.
- **2003.** Samaris settled $n=5$ by an intricate reduction to a finite-dimensional optimisation.
- **2014.** Martín, Sawyer, Uriarte-Tuero and Vukotić reformulated the problem in operator/Hardy-space language and verified it for structured subclasses.

**SOTA summary:** proven for $1\le n\le5$; for general $n$ only bounds of the form $|a_n|\le 1-\delta$ with $\delta$ tiny; no $n\ge6$ case is verified.

## 4. Partial Results / Verified Cases

- **$n=1,2,3$** — Hummel–Scheinberg–Zalcman (1977).
- **$n=4$** — Prokhorov–Szynal (1981); independently in Ermers (1990).
- **$n=5$** — Samaris (2003).
- **All $n$, weak bound** — $|a_n|\le 1-|a_0|^2<1$ (elementary) and Horowitz's uniform $|a_n|\le1-\delta$.
- **Leading-term case, all $n$.** If $f(z)=F(z^n)$ with $F\in\mathcal{B}_0$ (i.e. $f$ has $n$-fold symmetry), then $a_n$ equals the first coefficient of $F$, so $|a_n|\le 2/e$ by the $n=1$ proof. Equivalently, for arbitrary $f$ the single term $-c_ne^{-c_0}$ in (2.1) always satisfies the bound.
- **Finitely-atomic measures.** For $\mu$ a point mass ($f=\lambda\exp(-t\frac{1+\bar\zeta z}{1-\bar\zeta z})$, $t>0$) and for small numbers of atoms the maximum can be computed and equals $2/e$; numerical optimisation over discrete measures with up to several atoms has produced no violation for $n\le 30$. *(computational, as reported — verify)*
- **Special subclasses.** Typically real, starlike-type and other geometrically restricted subfamilies of $\mathcal{B}_0$, and classes with restricted Herglotz support, satisfy the bound (Prokhorov–Szynal; Martín–Sawyer–Uriarte-Tuero–Vukotić).

## 5. Principal Obstacles

- **Non-linearity of the functional.** For $n=1$, $a_1=-c_1e^{-c_0}$ is linear in $\mu$ after fixing $t$, so extreme-point theory of $\mathcal{P}$ applies directly. For $n\ge2$, (2.1) is a polynomial of degree $n$ in the moments $c_1,\dots,c_n$; maximising over the moment cone is a non-convex problem with no known convexity substitute.
- **Symmetrisation destroys the class.** The usual trick of replacing $f$ by $\frac1n\sum_k f(\varepsilon^k z)$ ($\varepsilon=e^{2\pi i/n}$) isolates $a_n$ but does not preserve non-vanishing. The multiplicative substitute $g=\big(\prod_k f(\varepsilon^kz)\big)^{1/n}$ stays in $\mathcal{B}_0$ but changes the coefficient: it kills exactly the mixed products $c_{j_1}\cdots c_{j_k}$ that carry the difficulty.
- **Variational methods stall.** The HSZ variational equation for an extremal $f$ is a differential equation whose solution space grows with $n$; the number of free parameters (atoms of $\mu$, their arguments and masses) grows linearly, and the resulting semialgebraic system has been solved only up to $n=5$, where the case analysis already runs to many pages.
- **Two competing bounds do not meet.** The bound $|a_n|\le 1-e^{-2t}$ is good for small $t$; the Carathéodory-type bound $|a_n|\lesssim P_n(t)e^{-t}$ is good for large $t$. For $n=1$ they cross exactly at $t=1$ giving $2/e$; for $n\ge 2$ the polynomial $P_n$ produced by (2.1) grows with $n$ (crude estimate $|a_n|\le e^{-t}\sum_k\frac{(2t)^k}{k!}\binom{n-1}{k-1}$), and its maximum over $t$ exceeds $2/e$ badly, so the elementary route gives nothing sharp.
- **No known duality or positivity certificate.** The problem lacks a Toeplitz/positive-definite reformulation of the kind that made the Bieberbach conjecture accessible to Löwner theory plus de Branges' Askey–Gasper inequality; the analogue of the Löwner PDE for $\mathcal{B}_0$ has not yielded a monotone Lyapunov functional.

## 6. The Gap

Proven: $n\le5$ exactly, plus $|a_n|\le1-\delta$ for all $n$. Conjectured: $|a_n|\le 2/e\approx0.7358$. The gap is the interval $(2/e,\,1-\delta)$ — a factor of roughly $1.36$ that is **not** shrinking with better elementary estimates.

Structurally, the missing step is control of the higher convolution terms in (2.1): one must show that

$$\Big|\sum_{k=2}^{n}\frac{(-1)^k}{k!}\sum_{j_1+\cdots+j_k=n}c_{j_1}\cdots c_{j_k}\Big|$$

cannot push $|a_n|$ past the value $2t e^{-t}\big|_{t=1}$ achieved by the single-atom, $n$-fold-symmetric configuration. Equivalently: prove that the maximiser of a degree-$n$ polynomial over the Carathéodory moment body is always the $n$-fold symmetric point-mass configuration — a rigidity statement for which no $n$-uniform argument exists.

## 7. Current Research (as of June 2026)

- **Hardy-space / operator reformulations.** The Martín–Sawyer–Uriarte-Tuero–Vukotić line recasts the bound as an inequality for Hankel- or Toeplitz-type forms associated with $\log(1/f)$, hoping for a positivity certificate valid for all $n$. Active in Madrid (UAM) and Michigan State. *(frontier — verify)*
- **Semidefinite / moment relaxations.** Lasserre-hierarchy relaxations of the trigonometric-moment problem attached to (2.1) give numerically sharp upper bounds for $n\le 10$–$12$; converting a numerical SDP certificate into an exact rational one, and finding an $n$-uniform hierarchy level, is the open computational goal. *(frontier — verify)*
- **Löwner-theoretic attacks.** Reformulation via controlled Löwner–Kufarev evolutions in the non-vanishing class, searching for a de Branges-style monotone functional.
- **Extremal-measure rigidity.** Refining HSZ's result that the extremal Herglotz measure is singular towards "the extremal measure has at most $n$ atoms, equally spaced" — the conjecture would follow from this plus the $n$-fold symmetric computation.
- Periodic announcements of full proofs circulate on preprint servers; none has been accepted by a refereed journal. Treat any claim of a general proof as unverified.

## 8. Future Work

- Prove the rigidity statement: any extremal measure for the $n$-th coefficient functional is a rotation of $n$ equally spaced atoms of equal mass $1/n$ each with total mass $1$.
- Push the uniform bound from $1-10^{-4}$ down to something like $0.9$: even a modest absolute improvement would require a genuinely new mechanism and is regarded by Zalcman and others as the realistic next milestone.
- Settle $n=6$ (and $n=7$) by computer-assisted exact arithmetic on the HSZ variational system — plausible with modern real algebraic geometry (cylindrical algebraic decomposition, positivstellensatz certificates).
- Study the $H^p$ analogues ($\sup|a_n|$ over non-vanishing $f$ with $\|f\|_{H^p}\le1$), where extremals are again $\exp$ of Herglotz integrals and the structure may be more tractable.
- Explore the conjectured link to the "log-coefficient" problems: bounds on the coefficients of $\log(1/f)$ combined with a sharp exponentiation inequality.

## 9. Key References

- **[Foundational]** J. Krzyż. *Coefficient problem for bounded nonvanishing functions.* Annales Polonici Mathematici 20 (1968), p. 314 (problem section).
- **[Foundational]** J. A. Hummel, S. Scheinberg, L. Zalcman. *A coefficient problem for bounded nonvanishing functions.* Journal d'Analyse Mathématique 31 (1977), 169–190. [DOI](https://doi.org/10.1007/bf02813302)
- **[Bounds]** C. Horowitz. *Coefficients of nonvanishing functions in $H^\infty$.* Israel Journal of Mathematics 30 (1978), 285–291.
- **[Cases]** D. V. Prokhorov, J. Szynal. *Coefficient estimates for bounded nonvanishing functions.* Bulletin de l'Académie Polonaise des Sciences, Série Sci. Math. 29 (1981), 223–230.
- **[Thesis]** R. Ermers. *Coefficient Estimates for Bounded Nonvanishing Functions.* Ph.D. thesis, Katholieke Universiteit Nijmegen, 1990.
- **[SOTA]** N. Samaris. *A proof of Krzyż's conjecture for the fifth coefficient.* Complex Variables, Theory and Application 48 (2003), 753–766.
- **[SOTA / Recent]** M. J. Martín, E. T. Sawyer, I. Uriarte-Tuero, D. Vukotić. *The Krzyż conjecture revisited.* Advances in Applied Mathematics 57 (2014), 1–20.
- **[Survey]** D. V. Prokhorov. *Coefficients of holomorphic functions.* Journal of Mathematical Sciences 106 (2001), 3518–3544. [DOI](https://doi.org/10.1023/a:1011975914158)
- **[Background]** P. L. Duren. *Theory of $H^p$ Spaces.* Academic Press, 1970.
- **[Background]** Ch. Pommerenke. *Univalent Functions.* Vandenhoeck & Ruprecht, Göttingen, 1975 (Carathéodory class, Herglotz representation).

## 10. Worked Example / Concrete Special Case

**The case $n=1$, proved in full.** Let $f\in\mathcal{B}_0$, $f=e^{-p}$ with $\operatorname{Re}p>0$, $p(z)=c_0+c_1z+\cdots$. From (2.1),

$$a_0=e^{-c_0},\qquad a_1=-c_1e^{-c_0}.$$

Put $t=\operatorname{Re}c_0>0$. Carathéodory's inequality for functions with positive real part gives $|c_1|\le 2\operatorname{Re}c_0=2t$. Hence

$$|a_1|=|c_1|\,e^{-t}\le 2t\,e^{-t}\le 2\max_{t>0}te^{-t}=\frac{2}{e},$$

the last maximum attained at $t=1$. Equality forces $t=1$ and $|c_1|=2$, i.e. the Herglotz measure is a unit point mass: $p(z)=\frac{1-\bar\zeta z}{1+\bar\zeta z}$ up to rotation, so $f=K_1(\bar\zeta z)$ up to a unimodular factor. $\blacksquare$

**Checking the extremal function's other coefficients.** With $K_1(z)=e^{-1}\exp\!\big(\tfrac{2z}{1+z}\big)=\frac1e\sum_n(-1)^nL_n^{(-1)}(2)z^n$:

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $e\,a_n$ | $1$ | $2$ | $0$ | $-\tfrac{2}{3}$ | $-\tfrac{1}{3}$ |
| $\|a_n\|$ | $0.3679$ | $0.7358$ | $0$ | $0.2453$ | $0.1226$ |

Direct check: $\exp\!\big(\frac{2z}{1+z}\big)=\exp(2z-2z^2+2z^3-\cdots)=1+2z+(-2+2)z^2+(2-4+\tfrac43)z^3+\cdots=1+2z+0\cdot z^2-\tfrac23z^3+\cdots$. So $K_1$ maximises only its **first** coefficient; to make the $n$-th coefficient large one must use $K_n(z)=K_1(z^n)$, whose non-zero coefficients sit in degrees $0,n,2n,\dots$ with $a_n=2/e$.

**Where the $n=1$ proof breaks at $n=2$.** Here $a_2=e^{-c_0}\big(\tfrac{c_1^2}{2}-c_2\big)$. The bounds $|c_1|,|c_2|\le 2t$ give only

$$|a_2|\le e^{-t}\big(2t^2+2t\big),\qquad \max_{t>0}e^{-t}(2t^2+2t)\approx 1.24>1,$$

which is worse than the trivial bound. The true maximum $2/e$ is attained at $c_1=0$, $c_2=-2$ (i.e. $K_2$), so the extremum sits at a point where the two moment constraints are *not* simultaneously saturated — a coupling between $c_1$ and $c_2$ that only the full positive-definiteness of the Toeplitz form $\big(c_{j-k}\big)$ detects. Exploiting that coupling uniformly in $n$ is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*