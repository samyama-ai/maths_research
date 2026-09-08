---
id: 03-geometry/borisov-alexeev-borisov-conjecture
title: "Borisov-Alexeev-Borisov Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borisov-Alexeev-Borisov Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/borisov-alexeev-borisov-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**BAB Conjecture.** Fix $d \in \mathbb{Z}_{>0}$ and $\varepsilon \in \mathbb{R}_{>0}$. The class of projective varieties $X$ over an algebraically closed field of characteristic $0$ such that

- $\dim X = d$,
- $X$ is $\varepsilon$-log canonical ($\varepsilon$-lc),
- $-K_X$ is ample (i.e. $X$ is Fano),

forms a **bounded family**: there exist a scheme $S$ of finite type and a projective morphism $\mathcal{X} \to S$ such that every such $X$ is isomorphic to a closed fibre of $\mathcal{X} \to S$.

Equivalently (and this is the working form): there is a constant $C = C(d,\varepsilon)$ with $(-K_X)^d \le C$ and an integer $N = N(d,\varepsilon)$ such that $-N K_X$ is very ample.

A proof must produce boundedness for *all* $\varepsilon > 0$ and *all* $d$; the hypothesis $\varepsilon > 0$ cannot be dropped (Section 10). The conjecture was resolved by **Caucher Birkar** in two papers (2016 preprints; *Annals of Mathematics* 2019 and 2021), work cited in his 2018 Fields Medal.

## 2. Mathematical Foundations

Let $X$ be a normal projective variety with $K_X$ $\mathbb{Q}$-Cartier, and let $f : Y \to X$ be a proper birational morphism from a normal variety. Write
$$K_Y = f^{*}K_X + \sum_{E} a(E,X)\, E ,$$
the sum over prime divisors $E \subset Y$. The number $a(E,X) \in \mathbb{Q}$ is the **discrepancy** of $E$; the **log discrepancy** is
$$A_X(E) := a(E,X) + 1 .$$
For a pair $(X,B)$ with $B = \sum b_i B_i$ an effective $\mathbb{R}$-divisor and $K_X + B$ $\mathbb{Q}$-Cartier, the same formula defines $a(E,X,B)$ and $A_{X,B}(E) = a(E,X,B)+1$.

**Definition (singularity classes).** $(X,B)$ is
$$\text{lc} \iff A_{X,B}(E)\ge 0,\quad \text{klt} \iff A_{X,B}(E) > 0,\quad \varepsilon\text{-lc} \iff A_{X,B}(E)\ge \varepsilon \ \ \forall E,$$
where $E$ ranges over all prime divisors on all birational models of $X$. Terminal $\iff a(E,X)>0$ for exceptional $E$; canonical $\iff a(E,X)\ge 0$. A Gorenstein canonical Fano is $1$-lc.

**Minimal log discrepancy.** $\operatorname{mld}(X) := \inf_E A_X(E)$ over exceptional $E$. Thus $X$ is $\varepsilon$-lc iff $\operatorname{mld}(X)\ge\varepsilon$ (and $X$ has no boundary).

**Fano.** $X$ is Fano if $-K_X$ is ample; **weak Fano** if $-K_X$ is nef and big. The **anticanonical degree** (volume) is
$$\operatorname{vol}(-K_X) = (-K_X)^d .$$

**Log canonical threshold.** For $(X,B)$ lc and $M \ge 0$ an $\mathbb{R}$-Cartier divisor,
$$\operatorname{lct}(X,B;M) = \sup\{ t \ge 0 : (X, B+tM) \text{ is lc}\}.$$

**Complements.** An **$n$-complement** of $K_X + B$ is $B^{+}\ge 0$ with $n(K_X+B^{+})\sim 0$, $(X,B^{+})$ lc, and $nB^{+} \ge n\lfloor B \rfloor + \lfloor (n+1)\{B\}\rfloor$. Birkar's **theory of complements** — for fixed $d$ and finite coefficient set, there is $n = n(d,\Lambda)$ such that every lc Fano type pair of dimension $d$ has an $n$-complement — is the engine of the proof.

**Two structural inputs used throughout:**

1. **ACC for lct** (Hacon–McKernan–Xu 2014): for fixed $d$ and DCC coefficient set $I$, the set of log canonical thresholds $\{\operatorname{lct}(X,B;M)\}$ satisfies the ascending chain condition.
2. **Boundedness $\Leftarrow$ bounded volume + bounded singularities**: an $\varepsilon$-lc Fano $X$ of dimension $d$ with $\operatorname{vol}(-K_X)\le C$ lies in a bounded family (HMX).

## 3. History & State of the Art (SOTA)

- **1992 — Kollár–Miyaoka–Mori.** Smooth Fano varieties of dimension $d$ form a bounded family, via rational connectedness and bend-and-break: $(-K_X)^d \le c(d)$ with a doubly exponential $c(d)$. This is BAB with $\varepsilon = 1$ and $X$ smooth.
- **1992/93 — A. Borisov and L. Borisov.** Toric Fano varieties with canonical (in particular terminal) singularities are bounded, via lattice-point bounds for reflexive-type simplices. The Borisov brothers then conjectured the general $\varepsilon$-lc statement.
- **1994 — Alexeev.** BAB in dimension $2$: $\varepsilon$-lc del Pezzo surfaces are bounded ("Boundedness and $K^2$ for log surfaces"). Independent proof by Alexeev–Mori later gave explicit constants.
- **2000 — Kollár–Miyaoka–Mori–Takagi.** Canonical $\mathbb{Q}$-Fano threefolds are bounded.
- **2009 — Prokhorov–Shokurov.** Complements and the "second main theorem", establishing the boundedness-of-complements program in low dimension.
- **2014 — Hacon–McKernan–Xu.** ACC for lct; BAB reduced to bounding $\operatorname{vol}(-K_X)$; BAB proved for $\varepsilon$-lc Fano with bounded Cartier index or bounded volume.
- **2016–2021 — Birkar.** *Anti-pluricanonical systems on Fano varieties* (Ann. of Math. 190 (2019)) proves boundedness of complements and BAB for $\varepsilon$-lc Fano admitting a suitable bounded structure. *Singularities of linear systems and boundedness of Fano varieties* (Ann. of Math. 193 (2021)) completes the general case. **Status: theorem, characteristic $0$.**

## 4. Partial Results / Verified Cases

The full theorem now subsumes these, but they remain the effective/explicit part of the picture.

| Case | Result | Source |
|---|---|---|
| $d=1$ | Only $\mathbb{P}^1$ | classical |
| $d=2$, any $\varepsilon>0$ | $\varepsilon$-lc del Pezzo surfaces bounded; $K_X^2 \le \max\{9, 2/\varepsilon + 4/\varepsilon^2\}$-type explicit bounds | Alexeev 1994; Alexeev–Mori 2004 |
| $d=3$, smooth | Exactly $105$ deformation families ($17$ with $\rho=1$, $88$ with $\rho\ge2$) | Iskovskikh 1977/78; Mori–Mukai 1981 |
| $d=3$, toric terminal | $634$ varieties; toric canonical: $674{,}688$ | Kasprzyk 2006, 2010 |
| $d=3$, canonical Gorenstein | $(-K_X)^3 \le 72$; bounded | KMMT 2000; Prokhorov |
| $d=3$, terminal $\mathbb{Q}$-Fano | Fano index $\le 19$; explicit lists in many index ranges | Prokhorov 2010 |
| $d=3$, $\varepsilon$-lc | Explicit upper bound for $(-K_X)^3$ as a function of $\varepsilon$ | Jiang 2021 |
| any $d$, toric $\varepsilon$-lc | Bounded, via lattice polytope volume bounds | Borisov–Borisov 1992/93 |
| any $d$, $\varepsilon$-lc with $\operatorname{vol}$ bounded | Bounded | HMX 2014 |
| any $d$, Cartier index bounded | Bounded | HMX 2014 |
| any $d$, $\varepsilon$-lc Fano | **Bounded** (full BAB) | Birkar 2019, 2021 |

## 5. Principal Obstacles

The obstacles that made BAB hard for 25 years, and the one that survives.

- **Volume can only be bounded from above, never from below in a useful way.** The whole difficulty is the single inequality $(-K_X)^d \le C(d,\varepsilon)$. Bend-and-break, which gives the smooth bound of KMM, requires a free rational curve through a general point with controlled $-K_X$-degree; singular $X$ need not carry one with any bounded degree, since the singularities absorb the deformation.
- **Failure of Kodaira vanishing arguments on singular $X$.** Standard boundedness proofs run Kawamata–Viehweg vanishing on a resolution and descend. For $\varepsilon$-lc $X$ the resolution's exceptional divisors have discrepancies accumulating near $-1+\varepsilon$, and the correction terms are not uniformly controlled in $\varepsilon$.
- **Cartier index is unbounded a priori.** For $\varepsilon$-lc Fano the index of $K_X$ is not bounded by any obvious function of $(d,\varepsilon)$ before the theorem is proved — a genuine circularity, since boundedness of index would give boundedness directly.
- **Non-effectivity of ACC.** ACC for lct is proved by contradiction (a hypothetical infinite strictly increasing sequence is shown to violate global ACC after passage to a limit); it yields no computable constants. Birkar's proof inherits this. **The constants $C(d,\varepsilon)$, $N(d,\varepsilon)$ and the complement number $n(d)$ are not effective for $d\ge 4$.**
- **Characteristic $p$.** MMP tools (resolution, vanishing, Nadel-type multiplier ideals) are unavailable or false; BAB in char $p>0$ is open in dimension $\ge 4$.

## 6. The Gap

For characteristic $0$ there is no gap: BAB is a theorem. The residual gaps are:

1. **Effectivity.** Produce explicit $C(d,\varepsilon)$. Known only for $d\le 3$. The precise barrier: replace ACC for lct — used non-constructively in Birkar's boundedness of complements — by an effective statement bounding lct denominators in terms of $d$ and the coefficient set.
2. **Positive and mixed characteristic.** BAB is known for $d\le 3$ over algebraically closed fields of characteristic $p > 5$ *(frontier — verify)*; $d\ge 4$ is open. The step that fails is the MMP with scaling plus vanishing used to lift sections of $-nK_X$.
3. **BAB for generalised pairs and fibrations.** Boundedness of $\varepsilon$-lc Fano *fibrations* $X \to Z$ with bounded base, needed for the full classification programme, is only partially available.

## 7. Current Research (as of June 2026)

- **Effective boundedness.** Chen Jiang (Fudan), Jihao Liu, Yanning Xu and collaborators pursue explicit bounds for $\varepsilon$-lc Fano threefolds and fourfolds, and effective complement numbers $n(d)$. Explicit $n(2)$ is known; $n(3)$ remains conjectural *(frontier — verify)*.
- **K-moduli.** Xu, Zhuang, Liu, Blum, Alper: BAB is the finiteness input making the moduli space of K-semistable Fano varieties of fixed dimension and volume a proper good moduli space. Xu's survey and book set out the architecture.
- **Boundedness beyond Fano.** Birkar's *Boundedness of Fano type fibrations* and work on generalised pairs extend BAB to Calabi–Yau fibrations; Filipazzi, Moraga and Svaldi work on boundedness of elliptic and Calabi–Yau fibrations.
- **Positive characteristic.** Birkar–Waldron, Witaszek, Bernasconi and Tanaka: 3-fold MMP and boundedness in char $p$.
- **Minimal log discrepancy.** The ACC and boundedness conjectures for $\operatorname{mld}$ (Shokurov) remain the main open singularity-theoretic problem in this circle; Han–Liu–Luo and Nakamura have recent progress.

## 8. Future Work

- Prove an effective version of ACC for log canonical thresholds; this is the identified bottleneck for computable $C(d,\varepsilon)$.
- Determine $n(3)$, the optimal complement number in dimension $3$, and produce explicit $(-K_X)^4$ bounds for $\varepsilon$-lc Fano fourfolds.
- Extend BAB to char $p>0$ in dimension $\ge 4$, or to mixed characteristic over a DVR.
- Classify $\varepsilon$-lc Fano threefolds explicitly for small $\varepsilon$ (e.g. $\varepsilon = 1/2$), following the toric templates of Kasprzyk.
- Use BAB to prove finiteness statements in birational geometry: boundedness of birational automorphism groups, Jordan property, and termination of flips in dimension $\ge 4$.

## 9. Key References

- **[Foundational]** J. Kollár, Y. Miyaoka, S. Mori. *Rational connectedness and boundedness of Fano manifolds.* Journal of Differential Geometry 36 (1992), 765–779. [DOI](https://doi.org/10.4310/jdg/1214453188)
- **[Foundational]** A. A. Borisov, L. A. Borisov. *Singular toric Fano varieties.* Matematicheskii Sbornik 183 (1992); Russian Acad. Sci. Sb. Math. 75 (1993), 277–283. [DOI](https://doi.org/10.1070/sm1993v075n01abeh003385)
- **[Foundational]** V. Alexeev. *Boundedness and $K^2$ for log surfaces.* International Journal of Mathematics 5 (1994), 779–810. [DOI](https://doi.org/10.1142/s0129167x94000395)
- **[Foundational]** C. D. Hacon, J. McKernan, C. Xu. *ACC for log canonical thresholds.* Annals of Mathematics 180 (2014), 523–571. [DOI](https://doi.org/10.4007/annals.2014.180.2.3)
- **[SOTA]** C. Birkar. *Anti-pluricanonical systems on Fano varieties.* Annals of Mathematics 190 (2019), 345–463. [DOI](https://doi.org/10.4007/annals.2019.190.2.1)
- **[SOTA]** C. Birkar. *Singularities of linear systems and boundedness of Fano varieties.* Annals of Mathematics 193 (2021), 347–405. [DOI](https://doi.org/10.4007/annals.2021.193.2.1)
- **[SOTA]** C. Jiang. *Boundedness of anticanonical volumes of singular log Fano threefolds.* Communications in Analysis and Geometry 29 (2021), 1–36.
- **[Related]** J. Kollár, Y. Miyaoka, S. Mori, H. Takagi. *Boundedness of canonical $\mathbb{Q}$-Fano 3-folds.* Proceedings of the Japan Academy, Ser. A 76 (2000), 73–77.
- **[Related]** Yu. Prokhorov, V. V. Shokurov. *Towards the second main theorem on complements.* Journal of Algebraic Geometry 18 (2009), 151–199. [DOI](https://doi.org/10.1090/s1056-3911-08-00498-0)
- **[Survey]** J. Kollár. *Singularities of the Minimal Model Program.* Cambridge Tracts in Mathematics 200, Cambridge University Press, 2013.
- **[Survey]** C. Xu. *K-stability of Fano varieties: an algebro-geometric approach.* EMS Surveys in Mathematical Sciences 8 (2021), 265–354. [DOI](https://doi.org/10.4171/emss/51)
- **[Survey]** C. Birkar. *Birational geometry of algebraic varieties.* Proceedings of the ICM 2018, Vol. I, World Scientific, 2018, 563–588.

## 10. Worked Example / Concrete Special Case

**Why $\varepsilon > 0$ is essential: the family $X_n = \mathbb{P}(1,1,n)$.**

Take the weighted projective plane $X_n = \mathbb{P}(1,1,n)$ for $n \ge 1$ — the cone over the rational normal curve of degree $n$ in $\mathbb{P}^n$. It is a normal projective toric surface, klt for every $n$, with one singular point, the cyclic quotient singularity $\tfrac{1}{n}(1,1)$.

**Degree.** On $\mathbb{P}(a_0,a_1,a_2)$ one has $\mathcal{O}(1)^2 = 1/(a_0a_1a_2)$ and $-K = \mathcal{O}(a_0+a_1+a_2)$. Hence
$$(-K_{X_n})^2 = \frac{(1+1+n)^2}{1\cdot 1\cdot n} = \frac{(n+2)^2}{n} \xrightarrow[n\to\infty]{} \infty .$$
So $\{X_n\}$ is an **unbounded** family of klt del Pezzo surfaces. BAB is false with "klt" ($\varepsilon = 0$) in place of "$\varepsilon$-lc".

**Minimal log discrepancy.** Resolve $\tfrac1n(1,1)$ by a single blow-up $f : Y \to X_n$ with exceptional curve $E \cong \mathbb{P}^1$, $E^2 = -n$. Adjunction on $Y$ gives
$$K_Y = f^{*}K_{X_n} + aE, \qquad (K_Y + E)\cdot E = \deg K_E = -2 .$$
Since $f^{*}K_{X_n}\cdot E = 0$, we get $aE\cdot E + E\cdot E = -2$, i.e. $-an - n = -2$, so
$$a = a(E, X_n) = \frac{2}{n} - 1, \qquad A_{X_n}(E) = \frac{2}{n} .$$
For a cyclic quotient $\tfrac1n(1,1)$ this valuation computes the minimum, so $\operatorname{mld}(X_n) = 2/n$.

**BAB in action.** Fix $\varepsilon>0$. Then $X_n$ is $\varepsilon$-lc iff $2/n \ge \varepsilon$, i.e.
$$n \le \frac{2}{\varepsilon},$$
so only finitely many members of the family survive, and for those
$$(-K_{X_n})^2 = \frac{(n+2)^2}{n} \le \frac{(2/\varepsilon + 2)^2}{1} = 4\left(\tfrac{1}{\varepsilon}+1\right)^2 .$$
Concretely, at $\varepsilon = 1/2$: $n \le 4$, and the surfaces are $\mathbb{P}^2$ ($n=1$, degree $9$), $\mathbb{P}(1,1,2)$ (degree $8$), $\mathbb{P}(1,1,3)$ (degree $25/3$), $\mathbb{P}(1,1,4)$ (degree $9$) — a finite, explicitly listable set. At $\varepsilon = 1$ (canonical) only $n \le 2$ survives.

This is exactly the shape of the general theorem: the lower bound $\varepsilon$ on log discrepancies caps the "depth" of the singularities, the cap bounds the anticanonical volume, and bounded volume plus bounded singularities gives a finite-type family. Birkar's contribution is that the second implication — $\varepsilon$-lc $\Rightarrow$ $(-K_X)^d$ bounded — holds in every dimension, proved via boundedness of complements rather than the explicit toric computation available here.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*