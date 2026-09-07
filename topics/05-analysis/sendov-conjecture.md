---
id: 05-analysis/sendov-conjecture
title: "Sendov Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sendov Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/sendov-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $p$ be a complex polynomial of degree $n \ge 2$ all of whose zeros lie in the closed unit disk $\overline{D}(0,1) = \{z \in \mathbb{C} : |z| \le 1\}$. The conjecture asserts:

> For every zero $a$ of $p$, the closed disk $\overline{D}(a,1)$ contains at least one zero of $p'$.

Equivalently, writing $Z(p') = \{w_1,\dots,w_{n-1}\}$ for the critical points of $p$ (with multiplicity),
$$\min_{1 \le k \le n-1} |a - w_k| \;\le\; 1 \qquad \text{for every } a \in Z(p).$$

A complete proof must establish this for all $n$ and all zero configurations in the disk. A disproof requires one explicit polynomial with all zeros in $\overline{D}(0,1)$ and one zero $a$ with $\operatorname{dist}(a, Z(p')) > 1$. The constant $1$ is sharp: $p(z) = z^n - 1$ has all critical points at $0$, at distance exactly $1$ from each zero.

Normalisation is harmless: the hypothesis and conclusion are invariant under $p(z) \mapsto c\,p(e^{i\theta} z)$, so one may assume $a \in [0,1]$ and $p$ monic.

## 2. Mathematical Foundations

Write $p(z) = c \prod_{j=1}^n (z - z_j)$ with $|z_j| \le 1$, and $p'(z) = nc \prod_{k=1}^{n-1}(z - w_k)$.

**Logarithmic derivative.** Away from $Z(p)$,
$$\frac{p'(z)}{p(z)} = \sum_{j=1}^{n} \frac{1}{z - z_j}.$$
This is the Cauchy transform of the empirical zero measure $\mu_p = \frac1n \sum_j \delta_{z_j}$, scaled by $n$.

**Gauss–Lucas theorem.** $Z(p') \subset \operatorname{conv}\big(Z(p)\big)$. Hence all critical points lie in $\overline{D}(0,1)$ and the trivial bound $\operatorname{dist}(a, Z(p')) \le 2$ holds always. Sendov's conjecture is the assertion that the factor $2$ can be replaced by $1$.

**The key product identity.** If $a = z_1$ is a simple zero, then
$$p'(a) = c\prod_{j \ge 2}(a - z_j) = n\,c \prod_{k=1}^{n-1}(a - w_k),$$
so
$$\prod_{k=1}^{n-1} |a - w_k| = \frac{1}{n} \prod_{j\ge 2} |a - z_j| .$$
Since $|a - z_j| \le 2$, this yields $\min_k |a - w_k| \le \left(2^{n-1}/n\right)^{1/(n-1)} < 2$, the elementary starting point for all quantitative work. Sendov's conjecture is the statement that the *geometric mean* bound can be pushed to a *minimum* bound of $1$.

**Extremal formulation.** Define
$$M(n) \;=\; \sup\Big\{ \operatorname{dist}\big(a, Z(p')\big) \;:\; \deg p = n,\ Z(p) \subset \overline{D}(0,1),\ a \in Z(p) \Big\}.$$
The supremum is attained by compactness. The conjecture is $M(n) = 1$ for all $n \ge 2$; $M(n) \ge 1$ always, via $z^n - 1$. Extremal polynomials are known to satisfy strong structural constraints (Phelps–Rodriguez, Miller): the extremal $a$ lies on the unit circle, all zeros lie on $\partial D(0,1)$ in the classical extremal configurations, and $p$ is a "maximal polynomial" with a critical point exactly at distance $M(n)$.

**Hausdorff-geometry reformulation (Sendov).** With $h$ the Hausdorff distance between compact sets, the conjecture says $h\big(Z(p), Z(p')\big) \le 1$ is implied *one-sidedly*: every zero is within $1$ of the critical set. The reverse inclusion is immediate from Gauss–Lucas.

## 3. History & State of the Art (SOTA)

- **1958–1962.** Blagovest Sendov formulated the conjecture; it circulated orally in Sofia.
- **1967.** Published as Problem 4.5 in W. K. Hayman's *Research Problems in Function Theory*, where it was misattributed to Ljubomir Iliev (Ilyeff). The names "Ilieff conjecture", "Ilieff–Sendov" and "Sendov" all persist in the literature.
- **1968–1969.** First substantive cases: Rubinstein settled $|a| = 1$; Goodman–Rahman–Ratti and Schmeisser independently settled polynomials with all zeros on the unit circle, and low degrees.
- **1985–1993.** Perturbative "corona" results: Bojanov–Rahman–Szynal, then Vâjâitu–Zaharescu, proved the conjecture for $|a|$ in a neighbourhood of $1$ (uniformly in $n$).
- **1988–1999.** Degree-by-degree computer-assisted attacks by J. E. Brown, culminating in Brown–Xiang: true for all $n \le 8$.
- **2014.** Dégot: for each *fixed* $a$ with $0 < |a| < 1$ there is $N(a)$ such that the conjecture holds for $n \ge N(a)$ — but $N(a) \to \infty$ as $|a| \to 1$, so no uniform statement follows.
- **2022.** Terence Tao, *Sendov's conjecture for sufficiently high degree polynomials* (Acta Mathematica): there exists an absolute constant $n_0$ such that the conjecture holds for all $n \ge n_0$. The constant is **ineffective** (obtained by a compactness/contradiction argument on limiting zero measures).

State of the art therefore: **true for $n \le 8$ and for $n \ge n_0$, with $n_0$ unknown.**

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n \le 8$ | True (all configurations) | Brown–Xiang 1999 (extending Brown 1988, 1991) |
| $n \ge n_0$, $n_0$ ineffective | True | Tao 2022 |
| $a = 0$ | Trivially true by Gauss–Lucas | classical |
| $\|a\| = 1$ | True for all $n$ | Rubinstein 1968 |
| all zeros on $\partial D(0,1)$ | True for all $n$ | Goodman–Rahman–Ratti 1969; Schmeisser 1969 |
| $1 - \varepsilon < \|a\| \le 1$, $\varepsilon$ absolute | True for all $n$ | Bojanov–Rahman–Szynal 1985; Vâjâitu–Zaharescu 1993 |
| $p$ with only real zeros | True (critical points interlace) | classical |
| $p(z) = (z-a)(z-b)^{n-1}$ and other 2-distinct-zero families | True by direct computation | classical |
| fixed $a$, $0 < \|a\| < 1$, $n \ge N(a)$ | True | Dégot 2014; effective $N(a)$ by Chalebgwa |
| $\|a\| \le 1$, radius $\left(2^{n-1}/n\right)^{1/(n-1)}$ | Unconditional weaker bound | product identity, §2 |

Extremal-structure results (Phelps–Rodriguez 1972; Miller 1990) show that any counterexample-approaching family must have $|a| = 1$ and highly rigid zero distributions, which is what makes the boundary regime the hard one.

## 5. Principal Obstacles

- **No monotonicity or convexity.** The map from zero configurations to $\operatorname{dist}(a, Z(p'))$ is neither convex nor monotone in any natural parameter, so variational/Lagrange arguments produce systems of algebraic conditions that grow uncontrollably with $n$.
- **Degree-by-degree methods explode.** Brown–Xiang-type arguments reduce to resultant computations and real-algebraic case analysis whose complexity is super-exponential in $n$. Extending $n \le 8$ to $n \le 9$ is a genuine computational wall, not a routine extension.
- **The product identity is lossy.** $\prod_k |a - w_k| = \frac1n \prod_{j \ge 2}|a - z_j|$ controls a geometric mean; converting it to a bound on the *minimum* requires knowing that the $w_k$ do not all sit near a common circle of radius $>1$ around $a$ — precisely the configuration that near-extremal polynomials approach.
- **The two limiting regimes are different problems.** For $|a|$ bounded away from $0$ and $1$, the zeros of a near-extremal $p$ equidistribute and potential-theoretic methods apply. For $|a| \to 1$ the limit object degenerates, and for $|a| \to 0$ the critical points cluster. Uniformity across all three regimes simultaneously is what defeated Dégot's method.
- **Ineffectivity of compactness.** Tao's proof passes to a limit of hypothetical counterexamples along a subsequence, deriving a contradiction with a rigidity statement about the limiting measure. Contradiction-by-compactness gives no numerical $n_0$.

## 6. The Gap

The proven region is $\{n \le 8\} \cup \{n \ge n_0\}$; the conjecture is the whole range. Two distinct steps would close it:

1. **Make $n_0$ effective.** Replace the compactness step in Tao's argument by a quantitative stability estimate: if $\mu_p$ is $\varepsilon$-close (in a suitable Wasserstein or potential metric) to the extremal limiting measure, then $\operatorname{dist}(a, Z(p')) \le 1 + C\varepsilon^{\alpha}$ with explicit $C, \alpha$. Tao's paper explicitly leaves this open.
2. **Cover the middle range $9 \le n < n_0$.** Even with an effective $n_0$, a numerically verified $n_0$ of, say, $10^6$ is far beyond any resultant-based verification. The gap closes only if $n_0$ is brought into computational reach (tens, not thousands) or if a uniform-in-$n$ argument replaces the asymptotic one.

## 7. Current Research (as of June 2026)

- **Effectivisation of Tao's theorem.** The main active thread: extracting explicit constants from the limiting-measure rigidity argument. *(frontier — verify)* No published effective $n_0$ is known to the author of this entry.
- **Quantitative near-extremal analysis** in the regime $|a|$ near $1$, extending Vâjâitu–Zaharescu's corona width $\varepsilon$ toward an absolute constant like $\varepsilon = 0.1$; combining a wide corona with Tao's interior argument would shrink the remaining parameter space.
- **Interval-arithmetic / SDP certificates** for $n = 9, 10$: reformulating the extremal problem as a constrained polynomial optimisation and seeking a sum-of-squares certificate. *(frontier — verify)*
- **Generalisations** studied in parallel: Sendov's own conjecture for higher derivatives $p^{(k)}$ with radius $1$, Schmeisser's conjecture on the Hausdorff distance $h(Z(p), Z(p'))$, and Smale's mean value conjecture, which shares the logarithmic-derivative machinery.
- Groups: Bulgarian Academy of Sciences (Sendov school, Hausdorff geometry of polynomials), UCLA (Tao and collaborators), and analytic-polynomial groups in Canada (Montréal, Rahman school legacy).

## 8. Future Work

- Prove a **stability version of Gauss–Lucas**: quantify how close $Z(p')$ must be to $\partial \operatorname{conv} Z(p)$ when the empirical measure is close to a given measure.
- Establish the **extremal-polynomial rigidity conjecture**: the only polynomials with $\operatorname{dist}(a, Z(p')) = 1$ are $c(z^n - e^{i\theta})$ up to rotation. A proof of uniqueness plus a local-maximum argument would give the conjecture by degree-independent means.
- Attack the **strict-inequality refinement**: if $|a| < 1$ then $\operatorname{dist}(a, Z(p')) < 1$, with a quantitative gap $\le 1 - c(1-|a|)^{\beta}$. Such a bound would immediately handle the interior and reduce everything to the boundary corona.
- Automate the low-degree verification via certified numerics to reach $n \le 12$, narrowing the gap from below.

## 9. Key References

- **[Foundational]** W. K. Hayman. *Research Problems in Function Theory.* Athlone Press, London, 1967. (Problem 4.5; first published statement.)
- **[Foundational]** Z. Rubinstein. *On a problem of Ilyeff.* Pacific Journal of Mathematics **26** (1968), 159–161.
- **[Foundational]** A. W. Goodman, Q. I. Rahman, J. S. Ratti. *On the zeros of a polynomial and its derivative.* Proceedings of the American Mathematical Society **21** (1969), 273–274.
- **[Foundational]** G. Schmeisser. *Bemerkungen zu einer Vermutung von Ilieff.* Mathematische Zeitschrift **111** (1969), 121–125.
- B. D. Bojanov, Q. I. Rahman, J. Szynal. *On a conjecture of Sendov about the critical points of a polynomial.* Mathematische Zeitschrift **190** (1985), 281–285.
- M. J. Miller. *Maximal polynomials and the Ilieff–Sendov conjecture.* Transactions of the American Mathematical Society **321** (1990), 285–303.
- V. Vâjâitu, A. Zaharescu. *Ilyeff's conjecture on a corona.* Bulletin of the London Mathematical Society **25** (1993), 49–54.
- J. E. Brown. *On the Sendov conjecture for sixth degree polynomials.* Proceedings of the American Mathematical Society **113** (1991), 939–946.
- **[SOTA]** J. E. Brown, G. Xiang. *Proof of the Sendov conjecture for polynomials of degree at most eight.* Journal of Mathematical Analysis and Applications **232** (1999), 272–292.
- J. Dégot. *Sendov conjecture for high degree polynomials.* Proceedings of the American Mathematical Society **142** (2014), 1337–1349.
- **[SOTA / Recent]** T. Tao. *Sendov's conjecture for sufficiently high degree polynomials.* Acta Mathematica **229** (2022), 347–392.
- **[Survey]** Q. I. Rahman, G. Schmeisser. *Analytic Theory of Polynomials.* London Mathematical Society Monographs, New Series 26, Oxford University Press, 2002. (Chapter 7 surveys Sendov's conjecture.)
- **[Survey]** Bl. Sendov. *Hausdorff geometry of polynomials.* East Journal on Approximation **7** (2001), 123–178.
- **[Reference]** M. Marden. *Geometry of Polynomials.* 2nd ed., Mathematical Surveys 3, American Mathematical Society, 1966.
- G. L. Phelps, R. S. Rodriguez. *Some properties of extremal polynomials for the Ilieff conjecture.* Kōdai Mathematical Seminar Reports **24** (1972), 172–175.

## 10. Worked Example / Concrete Special Case

**(a) Degree $n = 2$, complete proof.** Let $p(z) = (z-a)(z-b)$ with $|a|, |b| \le 1$. Then $p'(z) = 2z - (a+b)$, so the unique critical point is $w = \tfrac{a+b}{2}$ and
$$|a - w| = \left|a - \tfrac{a+b}{2}\right| = \frac{|a-b|}{2} \le \frac{|a| + |b|}{2} \le 1 .$$
Equality forces $|a| = |b| = 1$ and $b = -a$, i.e. $p(z) = z^2 - a^2$ — the $n=2$ case of the extremal family $z^n - e^{i\theta}$.

**(b) Sharpness for all $n$.** Take $p(z) = z^n - 1$. Its zeros are the $n$-th roots of unity, all on $\partial D(0,1)$. Since $p'(z) = n z^{n-1}$, every critical point equals $0$, and for each zero $a$ with $|a| = 1$,
$$\operatorname{dist}\big(a, Z(p')\big) = |a - 0| = 1 .$$
So the radius $1$ cannot be replaced by any $r < 1$, and $M(n) \ge 1$.

**(c) A non-trivial cubic.** Let
$$p(z) = (z-1)(z-i)(z+i) = z^3 - z^2 + z - 1,$$
with zeros $1, i, -i$, all on the unit circle. Then $p'(z) = 3z^2 - 2z + 1$, whose roots are
$$w_{\pm} = \frac{2 \pm \sqrt{4 - 12}}{6} = \frac{1 \pm i\sqrt{2}}{3}.$$
Check the zero $a = 1$:
$$|1 - w_+| = \left|\frac{2 - i\sqrt2}{3}\right| = \frac{\sqrt{4+2}}{3} = \frac{\sqrt6}{3} \approx 0.8165 \le 1 . \quad\checkmark$$
Check the zero $a = i$:
$$|i - w_+| = \left|\frac{-1 + i(3-\sqrt2)}{3}\right| = \frac{\sqrt{1 + (1.5858)^2}}{3} \approx \frac{1.8748}{3} \approx 0.6249 \le 1 . \quad\checkmark$$
Note that for $a = i$ the *other* critical point is far: $|i - w_-| = \frac{\sqrt{1 + (3+\sqrt2)^2}}{3} \approx 1.511 > 1$. The conjecture only asks for *one* nearby critical point, and this asymmetry is exactly why averaged quantities such as $\prod_k |a - w_k|$ do not settle the problem.

**(d) The elementary bound in action.** For this $p$ and $a = 1$, the identity of §2 gives
$$|1 - w_+|\,|1 - w_-| = \frac{|1-i|\,|1+i|}{3} = \frac{\sqrt2 \cdot \sqrt2}{3} = \frac{2}{3},$$
so $\min_k |1 - w_k| \le \sqrt{2/3} \approx 0.8165$ — here the geometric-mean bound happens to be sharp, but for $n$ large it degrades to $\left(2^{n-1}/n\right)^{1/(n-1)} \to 2$, which is the quantitative reason the elementary approach cannot reach the constant $1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*