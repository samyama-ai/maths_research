---
id: 05-analysis/ilin-conjecture
title: "Ilin's Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ilin's Conjecture (Ilyeff–Sendov Conjecture)

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/ilin-conjecture` · **Status:** partially-solved (open in general; proved for all sufficiently large degrees and for degrees $\le 8$)

## 1. Problem Statement / Conjecture

**Naming note.** The conjecture was formulated by Blagovest Sendov (Sofia, c. 1958) and transmitted to the West by Ljubomir Iliev (Ilieff / Ilyeff / "Ilin" in various transliterations). It entered the English literature as **Ilyeff's conjecture** in W. K. Hayman's *Research Problems in Function Theory* (1967, Problem 4.5), and dozens of papers from 1968–1995 carry "Ilieff's conjecture" or "Ilyeff's conjecture" in their titles. It is the same statement now standardly called the **Sendov conjecture**.

**Statement.** Let $n \ge 2$ and let
$$p(z) \;=\; \prod_{j=1}^{n}(z-a_j), \qquad a_j \in \mathbb{C}, \quad |a_j| \le 1 \ \ (1 \le j \le n),$$
be a monic complex polynomial all of whose zeros lie in the closed unit disk $\overline{\mathbb{D}}$. Then for **every** zero $a_k$ there exists a critical point $c$ (i.e. $p'(c)=0$) with
$$|a_k - c| \;\le\; 1 .$$

Equivalently: each closed disk $\overline{D}(a_k,1)$ contains at least one zero of $p'$.

A complete proof must establish this for all degrees $n$, all zero configurations in $\overline{\mathbb{D}}$, and all choices of the distinguished zero $a_k$. A disproof requires one explicit polynomial $p$ with all zeros in $\overline{\mathbb{D}}$ and one zero $a_k$ whose distance to the zero set of $p'$ exceeds $1$. The constant $1$ is sharp: $p(z)=z^n-1$ has $p'(z)=nz^{n-1}$, whose only critical point $0$ is at distance exactly $1$ from every zero.

## 2. Mathematical Foundations

Write $Z(p)=\{a_1,\dots,a_n\}$ (with multiplicity) and $Z(p')=\{c_1,\dots,c_{n-1}\}$, so that
$$p'(z) = n\prod_{k=1}^{n-1}(z-c_k).$$

**Logarithmic derivative.** Away from $Z(p)$,
$$\frac{p'(z)}{p(z)} \;=\; \sum_{j=1}^{n}\frac{1}{z-a_j}.$$

**Gauss–Lucas theorem.** $Z(p') \subset \operatorname{conv}(Z(p))$. Hence all critical points lie in $\overline{\mathbb{D}}$, and the trivial bound $\operatorname{dist}(a_k, Z(p')) \le 2$ is immediate. Ilin's conjecture asserts the factor-two improvement to $1$.

**Key product identity.** If $a=a_1$ is a simple or multiple zero, differentiating the factorisation gives
$$p'(a) \;=\; \prod_{j=2}^{n}(a-a_j) \;=\; n\prod_{k=1}^{n-1}(a-c_k),$$
so
$$\prod_{k=1}^{n-1}|a-c_k| \;=\; \frac{1}{n}\prod_{j=2}^{n}|a-a_j|. \tag{2.1}$$
This converts the conjecture into a statement about a *geometric mean* of distances, and is the source of every elementary bound (see §10).

**Normalisation and extremal problem.** Define
$$M(n) \;=\; \sup\Big\{ \operatorname{dist}\big(a_k, Z(p')\big) \;:\; \deg p = n,\ Z(p)\subset\overline{\mathbb{D}},\ a_k \in Z(p) \Big\}.$$
The supremum is attained (the constraint set is compact and the distance functional continuous), so extremal polynomials exist; the conjecture is $M(n)=1$ for all $n\ge2$. Rotation and the substitution $z \mapsto \lambda z$ with $|\lambda|=1$ let one assume $a_k = a \in [0,1]$.

**Potential-theoretic reformulation.** For a sequence $p_n$ of degree $n$ with zero-counting measures $\mu_n = \frac1n\sum_j \delta_{a_j}$, the normalised logarithmic derivative $\frac1n \frac{p_n'}{p_n}(z) \to \int \frac{d\mu(z)}{z-w}$ is the Cauchy transform of the weak-$*$ limit $\mu$ of $\mu_n$. Zeros of $p_n'$ accumulate on the support of the "derivative measure"; compactness arguments in this space (normal families of subharmonic potentials) drive the modern high-degree proofs.

## 3. History & State of the Art (SOTA)

- **c. 1958–1962** — Sendov formulates the conjecture; it circulates in Bulgarian and Russian schools of approximation theory.
- **1967** — Hayman publishes it as "Ilyeff's conjecture" in *Research Problems in Function Theory*, misattributing it to Iliev. This naming persists for ~25 years.
- **1968–1972** — First wave: Rubinstein settles $|a|=1$ for $n=3$ and related cases; Meir and Sharma, and Schmeisser, obtain low-degree and structural results.
- **1985** — Bojanov, Rahman and Szynal prove cases under symmetry / coefficient restrictions.
- **1990–1991** — Miller develops the theory of *maximal (extremal) polynomials*, giving strong necessary structural conditions on any counterexample.
- **1993** — Vâjâitu and Zaharescu prove the conjecture for zeros $a$ in a "corona" $r_0 \le |a| \le 1$ near the boundary (independently obtained by Brown).
- **1999** — Brown and Xiang prove the conjecture for all polynomials of degree $n \le 8$.
- **2014** — Dégot proves: for each fixed $a$ with $|a|<1$, the conjecture holds for all $n \ge n_0(a)$; the bound degenerates as $|a|\to1$.
- **2020–2022** — Tao removes the dependence on $a$: there is an absolute $n_0$ such that the conjecture holds for **all** polynomials of degree $n \ge n_0$. The proof is not effective in any practical sense.

**State of the art (2026).** Proved for $n \le 8$ and for $n \ge n_0$ (ineffective, astronomically large). Open in the middle range, which is where all the difficulty now sits.

## 4. Partial Results / Verified Cases

- **Degrees $n=2,\dots,8$**: fully proved (Brown–Xiang 1999; earlier degrees by Schmeisser, Rubinstein, Brown). Degree $2$ is a one-line computation (§10). Degrees $6$–$8$ required heavy case analysis with computer-assisted inequality verification.
- **All sufficiently large degrees**: Tao (2022), $n \ge n_0$ absolute.
- **Distinguished zero at the origin, $a_k = 0$**: immediate from (2.1); $\prod_k |c_k| = \frac1n \prod_{j\ge2}|a_j| \le \frac1n < 1$, so some $|c_k| < 1$.
- **$|a_k| = 1$ (boundary zeros)**: proved (Rubinstein 1968 and successors); more generally the corona $1-\varepsilon_0 \le |a_k|\le 1$ (Vâjâitu–Zaharescu 1993).
- **All zeros real**: proved — for real-rooted $p$, $Z(p')$ interlaces $Z(p)$ on $[-1,1]$ and the bound follows from the mean value theorem plus interlacing.
- **All zeros on the unit circle $|a_j|=1$**: proved.
- **$p(z)=z^n + c$, $|c|\le1$, and more generally polynomials with a zero of multiplicity $\ge n-1$**: exact computation.
- **Fixed $|a|<1$ with $n \ge n_0(|a|)$**: Dégot (2014), with explicit but rapidly growing $n_0(|a|)$.
- **Quantitative universal bounds**: $\operatorname{dist}(a,Z(p')) \le 2\,n^{-1/(n-1)}$ for every zero $a$ (see §10), which equals $1$ at $n=2$ and increases to $2$; and bounds of the form $1 + o(1)$ under restrictions on the zero distribution.

## 5. Principal Obstacles

- **The sharp constant is attained.** With $p(z)=z^n-1$ the inequality is an equality for *every* zero simultaneously. No estimate with any slack can work; every argument must be exactly tight at a nontrivial extremal family, which kills all soft/compactness-only proofs.
- **Elementary AM–GM arguments lose a factor of 2.** Identity (2.1) controls only the geometric mean of the $n-1$ distances $|a-c_k|$. A single small factor $|a-a_j|$ can be compensated by others close to $2$, so the bound $2n^{-1/(n-1)} \to 2$ degrades exactly as $n$ grows. Converting mean control into *minimum* control is the missing step.
- **No variational rigidity.** Miller's extremal polynomials satisfy necessary conditions (e.g. each zero of $p$ that is not extremal must be "active"), but the conditions are not strong enough to pin the extremal configuration down to $z^n-1$ up to rotation. The extremal problem is non-convex with many critical configurations.
- **The regime $0<|a|<1$ with $|a|$ moderate is genuinely hard.** Near $|a|=1$ the zeros of $p'$ are pushed inward and boundary methods (Vâjâitu–Zaharescu) apply; near $a=0$ the product identity suffices. In between, both mechanisms are weak simultaneously.
- **Loss of effectivity in the asymptotic proof.** Tao's argument proceeds by contradiction through a compactness/limiting argument: a hypothetical sequence of counterexamples of degrees $n_j\to\infty$ has zero measures converging to normalized Lebesgue measure on the circle plus a Dirac mass, and the contradiction is extracted from a delicate second-order analysis of the limiting log-potential. Compactness gives no bound on $n_0$, so it cannot be met in the middle by finite computation.
- **Degree-by-degree verification does not scale.** Brown–Xiang's degree-$8$ proof is already a large case analysis in $2(n-1)$ real parameters; the semialgebraic systems grow superexponentially, and generic quantifier-elimination / cylindrical algebraic decomposition is infeasible past roughly $n=9$–$10$.

## 6. The Gap

The proved regions are $\{2 \le n \le 8\}$ and $\{n \ge n_0\}$ with $n_0$ ineffective, together with, for every $n$, the sub-cases $a_k=0$, $|a_k|$ near $1$, real zeros, and circle zeros. The gap is the two-parameter region
$$9 \le n < n_0, \qquad 0 < |a_k| < 1-\varepsilon_0 ,$$
with $a_k$ a zero of intermediate modulus and the remaining zeros in general position in $\overline{\mathbb{D}}$.

Crossing it requires one of two things:

1. **Effectivisation.** Convert the compactness step in the high-degree proof into a quantitative estimate producing an explicit $n_0$ (ideally $n_0 \le 15$), then close the finite range by computer-assisted verification. The obstruction is that the limiting argument uses a normal-families extraction with no modulus of continuity.
2. **A uniform-in-$n$ mechanism.** Find a functional $F(p,a)$, monotone under the passage $p \mapsto p'$, that is minimised precisely at $z^n-1$ and certifies $\min_k |a-c_k| \le 1$ directly — i.e. upgrade the geometric-mean identity (2.1) to a genuine minimum bound. No such functional is known.

## 7. Current Research (as of June 2026)

- **Effective high-degree bounds.** Several groups are attempting to make Tao's compactness argument quantitative by replacing weak-$*$ convergence with explicit Wasserstein-metric estimates on the zero-counting measures. *(frontier — verify)* No published explicit $n_0$ exists.
- **Computer-assisted degrees $9$–$10$.** Work using sum-of-squares / Positivstellensatz certificates and interval arithmetic on the Brown–Xiang formulation of the extremal problem. Claims of a complete degree-$9$ verification have circulated in preprint form. *(frontier — verify)*
- **Structure of extremal polynomials.** Continuation of Miller's programme: proving that any extremal polynomial for $M(n)$ has all zeros on the unit circle, which would reduce the conjecture to a compact $(n-1)$-torus problem.
- **Hyperbolic / Möbius-invariant refinements.** Reformulations of the conjecture in the Poincaré metric on $\mathbb{D}$, motivated by the observation that the Gauss–Lucas theorem has a hyperbolic analogue; connections to the Schoenberg conjecture (an $\ell^2$ inequality for critical points) and to Smale's mean value conjecture, which concerns $|p(c)-p(a)|$ rather than $|c-a|$.
- **Groups.** Active work at UCLA (Tao and collaborators, analytic side), the Bulgarian Academy of Sciences (Sendov school, Hausdorff geometry of polynomials), and several computational real-algebraic-geometry groups in Europe.

## 8. Future Work

- Prove that extremal polynomials have all zeros on $\partial\mathbb{D}$ — widely regarded as the most promising structural reduction.
- Produce an explicit $n_0$; even $n_0 = 10^{6}$ would be a qualitative change, converting the problem into a finite (if currently intractable) verification.
- Establish the conjecture for all $n$ under one extra hypothesis, e.g. $p$ has real coefficients, or the zeros lie in a half-disk, or $p$ has at most $k$ distinct zeros for fixed $k$.
- Sharpen the universal bound $2n^{-1/(n-1)}$ to any bound of the form $1 + C/n$; nothing of this strength is known uniformly.
- Settle the "strong Sendov" variants: whether $\overline{D}(a_k,1)$ contains a critical point in its *interior* unless $p(z)=\lambda(z^n-\mu)$ with $|\mu|=1$.

## 9. Key References

- **[Foundational]** W. K. Hayman. *Research Problems in Function Theory.* The Athlone Press, University of London, 1967. (Problem 4.5, "Ilyeff's conjecture".)
- **[Foundational]** Z. Rubinstein. *On a problem of Ilyeff.* Pacific Journal of Mathematics, 26 (1968), 159–161.
- **[Foundational]** A. Meir, A. Sharma. *On Ilyeff's conjecture.* Pacific Journal of Mathematics, 31 (1969), 459–467.
- **[Foundational]** G. Schmeisser. *Bemerkungen zu einer Vermutung von Ilieff.* Mathematische Zeitschrift, 111 (1969), 121–125.
- **[Structural]** B. Bojanov, Q. I. Rahman, J. Szynal. *On a conjecture of Sendov about the critical points of a polynomial.* Mathematische Zeitschrift, 190 (1985), 281–285.
- **[Structural]** M. J. Miller. *Maximal polynomials and the Ilieff–Sendov conjecture.* Transactions of the American Mathematical Society, 321 (1990), 285–303.
- **[Partial]** V. Vâjâitu, A. Zaharescu. *Ilyeff's conjecture on a corona.* Bulletin of the London Mathematical Society, 25 (1993), 49–54.
- **[Partial]** J. E. Brown, G. Xiang. *Proof of the Sendov conjecture for polynomials of degree at most eight.* Journal of Mathematical Analysis and Applications, 232 (1999), 272–292.
- **[SOTA]** J. Dégot. *Sendov conjecture for high degree polynomials.* Proceedings of the American Mathematical Society, 142 (2014), 1337–1349.
- **[SOTA / Recent]** T. Tao. *Sendov's conjecture for sufficiently high degree polynomials.* Acta Mathematica, 229 (2022); preprint arXiv:2012.04125.
- **[Survey]** Q. I. Rahman, G. Schmeisser. *Analytic Theory of Polynomials.* London Mathematical Society Monographs 26, Oxford University Press, 2002. (Chapter on critical points; extensive Sendov/Ilieff bibliography.)
- **[Survey]** Bl. Sendov. *Hausdorff geometry of polynomials.* East Journal on Approximation, 7 (2001), 123–178.
- **[Background]** M. Marden. *Geometry of Polynomials.* 2nd ed., Mathematical Surveys 3, American Mathematical Society, 1966.
- **[Background]** T. Sheil-Small. *Complex Polynomials.* Cambridge Studies in Advanced Mathematics 75, Cambridge University Press, 2002.

## 10. Worked Example / Concrete Special Case

**(a) Degree $2$: complete proof.** Let $p(z)=(z-a_1)(z-a_2)$ with $|a_1|,|a_2|\le1$. Then $p'(z)=2z-(a_1+a_2)$, so the unique critical point is $c=\tfrac{a_1+a_2}{2}$ and
$$|a_1-c| \;=\; \frac{|a_1-a_2|}{2} \;\le\; \frac{|a_1|+|a_2|}{2} \;\le\; 1 .$$
Equality forces $a_2=-a_1$, $|a_1|=1$, i.e. $p(z)=z^2-a_1^2$ — the $n=2$ member of the extremal family $z^n-\mu$.

**(b) The general elementary bound, and where it breaks.** Let $a$ be a zero of $p$, all zeros in $\overline{\mathbb{D}}$. By (2.1),
$$\prod_{k=1}^{n-1}|a-c_k| \;=\; \frac1n\prod_{j=2}^{n}|a-a_j| \;\le\; \frac{2^{\,n-1}}{n},$$
using $|a-a_j|\le|a|+|a_j|\le2$. The minimum is at most the geometric mean:
$$\min_{1\le k\le n-1}|a-c_k| \;\le\; \Big(\frac{2^{\,n-1}}{n}\Big)^{\frac{1}{n-1}} \;=\; \frac{2}{n^{1/(n-1)}} \;=:\; B(n).$$
Numerically: $B(2)=1$, $B(3)=1.1547$, $B(4)=1.2599$, $B(8)=1.4310$, $B(20)=1.4438\cdot\!$ — and $B(n)\to 2$. So this argument **proves the conjecture only for $n=2$** and gets worse, not better, with $n$. That single fact is the cleanest statement of §5–§6: the elementary method controls a product, the conjecture is about a minimum, and the two agree only when there is one critical point.

**(c) The sharp example.** $p(z)=z^3-1$ has zeros $1,\omega,\omega^2$ ($\omega=e^{2\pi i/3}$) and $p'(z)=3z^2$, so $Z(p')=\{0,0\}$ and $\operatorname{dist}(a_k,Z(p'))=1$ for each $k$. Check against (2.1) at $a=1$: $\prod_{k}|1-c_k| = |1-0|^2 = 1$ and $\frac13|1-\omega||1-\omega^2| = \frac13\cdot\sqrt3\cdot\sqrt3 = 1$. ✓

**(d) A slack case.** $p(z)=z^3-z=(z-1)z(z+1)$ has $p'(z)=3z^2-1$, critical points $\pm 1/\sqrt3 \approx \pm0.5774$. Distances: from $1$ to $1/\sqrt3$ is $0.4226$; from $0$ to either is $0.5774$; from $-1$ is $0.4226$. All $\le 1$, with wide margin — real zeros are the easy regime. Perturbing toward $z^3-1$ closes the margin continuously to $0$, and the conjecture asserts it never becomes negative.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*