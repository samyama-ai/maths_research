---
id: 05-analysis/dvoretzky-random-covering
title: "The Dvoretzky Covering Problem for Random Arcs"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Dvoretzky Covering Problem for Random Arcs

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/dvoretzky-random-covering` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fix a sequence of lengths $\ell_1 \ge \ell_2 \ge \cdots > 0$ with $\ell_n < 1$. Place arcs $I_n = (\omega_n, \omega_n + \ell_n)$ on the circle $\mathbb{T} = \mathbb{R}/\mathbb{Z}$, where $\omega_1, \omega_2, \dots$ are i.i.d. uniform on $\mathbb{T}$. **Dvoretzky's question (1956):** for which $(\ell_n)$ is
$$\mathbb{P}\Big(\bigcup_{n\ge 1} I_n = \mathbb{T}\Big) = 1 \;?$$

The one-dimensional question with monotone lengths is **solved**: Shepp (1972) proved covering holds a.s. if and only if
$$\sum_{n=1}^{\infty} \frac{1}{n^{2}} \exp\big(\ell_1 + \ell_2 + \cdots + \ell_n\big) = \infty .$$

The problem is catalogued as *partially solved* because the substantive parts remain open:

1. **Dimension $d \ge 2$ (Kahane's problem).** Replace $\mathbb{T}$ by $\mathbb{T}^d$ and the arcs by balls $B(\omega_n, r_n)$ with $r_n \downarrow 0$. No necessary-and-sufficient criterion in terms of $(r_n)$ is known for any $d \ge 2$. A complete solution must produce a condition on $(r_n)$ equivalent to a.s. covering, or prove no such condition exists.
2. **Non-monotone lengths.** Shepp's criterion is proved under $\ell_n \downarrow$. For general $(\ell_n)$ with $\sum \ell_n = \infty$ no criterion is known.
3. **General shapes.** For $\mathbb{T}^d$ with translated (and possibly rotated) copies $A_n$ of prescribed convex sets, covering is not determined by the volumes $|A_n|$ alone; the correct invariant is unidentified.
4. **Exact gauge of the uncovered set.** In the non-covering regime, determine the exact Hausdorff and packing measure functions of $U = \mathbb{T}\setminus\bigcup_n I_n$, not merely its dimension.

## 2. Mathematical Foundations

Let $(\Omega,\mathcal F,\mathbb P)$ carry i.i.d. uniform $\omega_n$. Write
$$L_n = \sum_{k=1}^{n}\ell_k, \qquad U_N = \mathbb{T}\setminus\bigcup_{n\le N} I_n, \qquad U = \bigcap_{N} U_N .$$

**First moment.** For fixed $x\in\mathbb{T}$, the events $\{x\notin I_n\}$ are independent with probability $1-\ell_n$, so by Fubini
$$\mathbb{E}\,|U_N| = \prod_{k=1}^{N}(1-\ell_k) \asymp e^{-L_N}\quad (\ell_k \to 0).$$
Hence $\sum \ell_n = \infty$ forces $\mathbb{E}|U| = 0$: the uncovered set is a.s. Lebesgue-null. Covering is therefore a statement about a *null* set of exceptional points, and $\sum\ell_n=\infty$ is necessary but far from sufficient (Dvoretzky 1956).

**Zero–one law.** The covering event is invariant under permutations of finitely many $\omega_n$ and under rotation; by Hewitt–Savage, $\mathbb{P}(\bigcup I_n = \mathbb{T}) \in \{0,1\}$ (Kahane).

**Shepp's criterion.** With $\ell_n$ non-increasing,
$$\bigcup_{n} I_n = \mathbb{T}\ \text{a.s.} \iff \sum_{n\ge 1} \frac{1}{n^{2}}\,e^{L_n} = \infty. \tag{S}$$
An equivalent Poissonian formulation (Shepp, *Covering the line by random intervals*): if intervals of length $>x$ arrive as a Poisson process on $\mathbb{R}\times(0,1)$ with intensity $dt\,d\mu(x)$ and $\Lambda(x)=\int_x^1 \mu((y,1])\,dy$, then $\mathbb{R}$ is covered a.s. iff
$$\int_0^1 e^{\Lambda(x)}\,dx = \infty .$$

**Uncovered set in the non-covering regime.** If (S) fails, $U\ne\emptyset$ a.s. and, for $\ell_n = c/n$ with $0<c<1$,
$$\dim_H U = \dim_B U = 1-c \quad \text{a.s.}$$
(Fan–Wu 2004; earlier for the Poisson model). More generally $U$ is a random *limsup*-type set; it belongs to Falconer's class of sets with large intersections, so $\dim_H$ is stable under countable intersections of rotated copies.

**Higher dimensions.** On $\mathbb{T}^d$ with balls of radius $r_n \downarrow 0$ and $\Sigma_n = \omega_d\sum_{k\le n} r_k^{\,d}$ (with $\omega_d=|B(0,1)|$), the naive analogue of (S) reads
$$\sum_{n} \frac{1}{n^{\,d+1}}\, e^{\Sigma_n} = \infty . \tag{S$_d$}$$
For $r_n=(a/(\omega_d n))^{1/d}$ this predicts the threshold $a = d$. Sufficiency-type results in this spirit are known (El Hélou 1978; Kahane 1985, Ch. 11), but (S$_d$) is *not* established as a criterion for $d\ge2$ *(frontier — verify)*.

## 3. History & State of the Art (SOTA)

- **1956.** Aryeh Dvoretzky, *On covering a circle by randomly placed arcs* (PNAS), poses the problem and shows $\sum\ell_n=\infty$ does not suffice.
- **1959–1961.** Kahane proves covering for $\ell_n = c/n$, $c>1$; Erdős and Kahane sharpen the sufficient conditions and identify $\ell_n \asymp 1/n$ as the critical scale. Billard and Kahane give logarithmic refinements.
- **1972.** Larry Shepp establishes (S) in full (Israel J. Math.), simultaneously with Mandelbrot's independent conjecture and heuristic derivation (Z. Wahrsch. verw. Geb.). Shepp's companion paper settles the Poissonian line model.
- **1978.** El Hélou treats $\mathbb{T}^q$, giving sufficient covering conditions and Hausdorff dimension bounds for the uncovered set.
- **1985–1990.** Kahane's book *Some Random Series of Functions* (2nd ed., Ch. 11) canonicalises the theory and links it to potential theory and multiplicative chaos; *Recouvrements aléatoires et théorie du potentiel* poses the $d$-dimensional problem explicitly.
- **1986.** Janson's Acta Mathematica paper settles the *equal-size* covering asymptotics in $\mathbb{R}^d$ with sharp constants, the complementary regime to Dvoretzky's.
- **1993–2005.** Fan–Kahane and Barral–Fan compute the multifractal spectrum of covering multiplicities (how many arcs cover a given point).
- **2004.** Fan–Wu compute $\dim_H U = 1-c$ for $\ell_n=c/n$.
- **2008.** Jonasson–Steif introduce dynamical versions (Brownian/Poisson updating of centres) and find exceptional times at which covering fails.
- **2014–2018.** Järvenpää–Järvenpää–Koivusalo–Li–Suomala (affine covering sets in $\mathbb{T}^d$) and Feng–Järvenpää–Järvenpää–Suomala (Ann. Probab. 2018) compute dimensions of random covering sets on Riemannian manifolds for general shapes.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $d=1$, $\ell_n \downarrow$ | **Solved**: criterion (S), Shepp 1972 |
| $\ell_n = c/n$ | Covers a.s. iff $c \ge 1$ (including the critical $c=1$) |
| $\ell_n = \frac{1}{n} - \frac{a}{n\log n}$ | Covers a.s. iff $a \le 1$ (see §10) |
| $\ell_n = c/n$, $0<c<1$ | $\dim_H U = 1-c$; $U$ has large intersection property |
| Poisson line model | **Solved**: $\int_0^1 e^{\Lambda(x)}dx=\infty$ |
| Equal radii, $N$ balls in $\mathbb{T}^d$ | **Solved asymptotically** (Janson 1986): $N$ balls of volume $v$ cover once $Nv-\log N-d\log\log N\to\infty$ |
| $\mathbb{T}^d$, balls, $r_n^d = a/n$ | Covering for $a$ large, failure for $a$ small; critical $a$ **open** for $d\ge 2$ |
| $\mathbb{T}^d$, general shapes | Dimension of $U$ known in many cases (Feng et al. 2018); covering criterion **open** |
| Dynamical circle covering | Exceptional times exist in an explicit window of parameters (Jonasson–Steif 2008) |

## 5. Principal Obstacles

- **First and second moments both fail.** $\mathbb{E}|U|=e^{-L_N+o(1)}\to 0$ regardless of the critical constant, so covering is invisible to the first moment; the second moment of $|U_N|$ is dominated by short-range correlations and does not localise the threshold either. Shepp's proof instead controls the *number and lengths of gaps* of $U_N$ via an exact renewal/Markov computation available only in one dimension.
- **The one-dimensional proof is order-structural.** Shepp's argument uses the linear order of $\mathbb{T}$: after $N$ arcs, $U_N$ is a finite union of intervals whose left endpoints form a tractable point process. On $\mathbb{T}^d$, $U_N$ is a random open set with complicated topology; there is no gap-length renewal structure and no exact recursion.
- **Volume is not the right invariant in $d \ge 2$.** Covering by translated copies of a set $A_n$ depends on shape and orientation, not only on $|A_n|$: aligned thin rectangles behave differently from randomly rotated ones with the same volume. Any $d$-dimensional criterion phrased in $\sum|A_n|$ alone is therefore false in general, and the correct functional (a capacity- or entropy-type quantity) is unknown.
- **Critical cases are logarithmically delicate.** Whether $\ell_n=1/n$ covers is decided by the divergence of $\sum n^{-1}$; perturbations at order $1/(n\log n)$ flip the answer. Soft compactness or ergodic arguments have no resolution at that scale.
- **Potential theory gives the wrong exponent.** Kahane's capacity/energy methods (Frostman-type, working well for hitting problems and for $\dim_H U$) yield conditions off by logarithmic factors precisely at the covering threshold, because covering is a statement about *all* points simultaneously, not about a positive-capacity set of points.

## 6. The Gap

The proven boundary is: **one dimension, monotone lengths**. Everything beyond it is open. The precise steps to be crossed are:

1. **From gaps to geometry.** Shepp's criterion arises from an exact computation of $\mathbb{P}(U_N$ has a gap containing a given point$)$ using the interval structure. Crossing to $d\ge2$ requires a replacement for gap length — a scalar statistic of the random open set $U_N$ whose expectation is computable and whose divergence characterises covering. No candidate has been shown to work.
2. **Monotonicity.** Shepp's proof degrades without $\ell_n\downarrow$; one needs either a rearrangement inequality proving that the decreasing rearrangement is extremal for the covering probability, or a genuinely rearrangement-free proof of (S).
3. **Shape dependence.** A criterion for $\mathbb{T}^d$ must interpolate between the ball case and degenerate shapes; identifying the invariant that reduces to $\ell_n$ when $d=1$ is the conceptual gap.
4. **Critical measure.** For $\ell_n=c/n$, $c<1$, the exact gauge $h$ with $0<\mathcal H^h(U)<\infty$ is not settled in the same generality as the dimension.

## 7. Current Research (as of June 2026)

- **Finnish school (Jyväskylä/Oulu: Järvenpää, Järvenpää, Suomala, Koivusalo, Li, Feng).** Dimension theory of random covering sets on manifolds and for affine/self-similar shapes; the active question is whether their dimension formulas can be upgraded to covering criteria at the critical scale. *(frontier — verify)*
- **French school (Fan, Barral, Durand, following Kahane).** Multifractal analysis of covering multiplicity and large-intersection classes; connections to multiplicative chaos and to Diophantine approximation limsup sets (Duffin–Schaeffer-type analogies). *(frontier — verify)*
- **Dynamical and noise-sensitivity programme (Steif, Jonasson, and successors).** Exceptional times for dynamical circle covering; sharp identification of the parameter window where exceptional times exist remains partially open.
- **Percolation-flavoured approaches.** Comparison of $U_N$ with Boolean-model vacancy and with the "random interlacements"/Brownian-vacant-set literature, aiming to import multi-scale renormalisation into the $d\ge2$ Dvoretzky problem. *(frontier — verify)*
- **Shift-and-cover / Diophantine variants.** Covering with deterministic centres $\{n\alpha\}$ or with dilated arcs (Kahane's "translation" problems) draws work from the metric number theory community.

## 8. Future Work

- Prove or disprove (S$_d$) for balls in $\mathbb{T}^2$; even determining the critical $a$ in $r_n^d = a/n$ would be a landmark.
- Establish a rearrangement inequality: covering probability is monotone under decreasing rearrangement of $(\ell_n)$, removing the monotonicity hypothesis in (S).
- Develop a multi-scale renormalisation for $U_N$ in $d\ge2$ replacing the gap renewal argument.
- Determine exact Hausdorff and packing gauge functions of $U$ for general non-covering $(\ell_n)$, not only for $\ell_n=c/n$.
- Extend the theory to covering by random arcs with dependent centres (e.g. determinantal or hyperuniform point processes), where negative dependence should help covering.
- Quantify the covering time: sharp two-term asymptotics for $\min\{N : \bigcup_{n\le N} I_n = \mathbb{T}\}$ in the boundary case.

## 9. Key References

- **[Foundational]** A. Dvoretzky. *On covering a circle by randomly placed arcs.* Proceedings of the National Academy of Sciences USA, 42 (1956), 199–203.
- **[Foundational]** J.-P. Kahane. *Sur le recouvrement d'un cercle par des intervalles placés au hasard.* C. R. Acad. Sci. Paris, 248 (1959), 184–186.
- **[SOTA]** L. A. Shepp. *Covering the circle with random arcs.* Israel Journal of Mathematics, 11 (1972), 328–345.
- **[SOTA]** L. A. Shepp. *Covering the line with random intervals.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete, 23 (1972), 163–170.
- **[Foundational]** B. B. Mandelbrot. *On Dvoretzky coverings for the circle.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete, 22 (1972), 158–160.
- **[Survey/Book]** J.-P. Kahane. *Some Random Series of Functions.* 2nd edition, Cambridge University Press, 1985 (Chapter 11).
- **[Survey]** J.-P. Kahane. *Recouvrements aléatoires et théorie du potentiel.* Colloquium Mathematicum, 60/61 (1990), 387–411.
- **[SOTA]** S. Janson. *Random coverings in several dimensions.* Acta Mathematica, 156 (1986), 83–118.
- **[SOTA]** A.-H. Fan, J. Wu. *On the covering by small random intervals.* Annales de l'Institut Henri Poincaré (B) Probabilités et Statistiques, 40 (2004), 125–131.
- **[SOTA]** A.-H. Fan, J.-P. Kahane. *Rareté des intervalles recouvrant un point dans un recouvrement aléatoire.* Annales de l'IHP Probabilités et Statistiques, 29 (1993), 453–466.
- **[SOTA]** J. Barral, A.-H. Fan. *Covering numbers of different points in Dvoretzky covering.* Bulletin des Sciences Mathématiques, 129 (2005), 275–317.
- **[SOTA]** J. Jonasson, J. E. Steif. *Dynamical models for circle covering: Brownian motion and Poisson updating.* Annals of Probability, 36 (2008), 739–764.
- **[Recent]** D.-J. Feng, E. Järvenpää, M. Järvenpää, V. Suomala. *Dimensions of random covering sets in Riemann manifolds.* Annals of Probability, 46 (2018), 1542–1596.
- **[Recent]** E. Järvenpää, M. Järvenpää, H. Koivusalo, B. Li, V. Suomala. *Hausdorff dimension of affine random covering sets in torus.* Annales de l'IHP Probabilités et Statistiques, 50 (2014), 1371–1384.

## 10. Worked Example / Concrete Special Case

**Case A: $\ell_n = c/n$, $c>0$.** Then
$$L_n = \sum_{k=1}^{n}\frac{c}{k} = c\log n + c\gamma + O(1/n), \qquad e^{L_n} = e^{c\gamma} n^{c}\,(1+o(1)),$$
with $\gamma$ the Euler–Mascheroni constant. Shepp's series is
$$\sum_{n\ge1} \frac{e^{L_n}}{n^{2}} \asymp \sum_{n\ge1} n^{\,c-2},$$
which diverges iff $c-2 \ge -1$, i.e. **iff $c \ge 1$**. So $\ell_n = 1/n$ covers a.s., while $\ell_n = 0.999/n$ does not. Note $\sum \ell_n = \infty$ for every $c>0$: divergence of the total length is genuinely insufficient.

Contrast with the first moment: $\mathbb{E}|U_N| = \prod_{k\le N}(1-c/k) \asymp N^{-c} \to 0$ for **all** $c>0$. The expected uncovered measure vanishes on both sides of the threshold, so it carries no information about covering — the point of §5.

For $c<1$ the leftover set is a genuine fractal: $\dim_H U = 1-c$ a.s. (Fan–Wu 2004). At $c=0.5$, $U$ is a random set of dimension $1/2$ and zero length that meets every subinterval of $\mathbb{T}$.

**Case B: a critical perturbation.** Take
$$\ell_n = \frac{1}{n} - \frac{a}{n\log n}, \qquad a > 0,\ n\ge 3 .$$
Then $L_n = \log n - a\log\log n + C + o(1)$, so $e^{L_n} \asymp n(\log n)^{-a}$ and
$$\sum_{n\ge3}\frac{e^{L_n}}{n^{2}} \asymp \sum_{n\ge3}\frac{1}{n(\log n)^{a}},$$
which diverges **iff $a \le 1$**. So the circle is covered a.s. for $a=1$ and not covered a.s. for $a=1.01$ — a difference of order $10^{-2}/(n\log n)$ in arc length flips a zero–one event. This is exactly the resolution at which every soft (capacity, entropy, compactness) argument breaks down, and exactly the resolution that no known method reaches on $\mathbb{T}^2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*