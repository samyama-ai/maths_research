---
id: 05-analysis/kakeya-conjecture
title: "Kakeya Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kakeya Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kakeya-conjecture` · **Status:** partially-solved (open for $n \ge 4$; the set version in $\mathbb{R}^3$ was resolved in 2025)

## 1. Problem Statement / Conjecture

A **Besicovitch set** (or **Kakeya set**) in $\mathbb{R}^n$ is a compact set containing a unit line segment in every direction.

**Kakeya set conjecture.** Every Besicovitch set $K \subset \mathbb{R}^n$ has Hausdorff dimension $n$:
$$\dim_H K = n \qquad (n \ge 2).$$
The stronger **Minkowski** version asserts $\dim_M K = n$ (upper box dimension), and the strongest form is the **Kakeya maximal function conjecture** (Section 2).

The conjecture is *not* about measure: Besicovitch showed measure-zero Kakeya sets exist in every $\mathbb{R}^n$, $n \ge 2$. The claim is that such sets cannot be small in the finer scale of Hausdorff dimension. A complete proof must produce, for every $\varepsilon > 0$, a bound $\mathcal{H}^{n-\varepsilon}(K) = \infty$ for all Besicovitch $K$; a disproof requires an explicit set with $\dim_H K < n$.

## 2. Mathematical Foundations

**Hausdorff dimension.** For $s \ge 0$, $\mathcal{H}^s_\delta(E) = \inf\{\sum_i (\mathrm{diam}\, U_i)^s : E \subset \bigcup_i U_i,\ \mathrm{diam}\, U_i \le \delta\}$, $\mathcal{H}^s = \lim_{\delta \to 0}\mathcal{H}^s_\delta$, and $\dim_H E = \inf\{s : \mathcal{H}^s(E) = 0\}$. The **upper Minkowski dimension** is $\dim_M E = n - \liminf_{\delta\to 0} \frac{\log |E_\delta|}{\log \delta}$, where $E_\delta$ is the $\delta$-neighbourhood. Always $\dim_H E \le \dim_M E$.

**Discretised form.** Let $\{e_j\} \subset S^{n-1}$ be a maximal $\delta$-separated set ($\approx \delta^{-(n-1)}$ directions) and let $T_j$ be $\delta \times 1$ tubes with axis direction $e_j$. The Minkowski conjecture is equivalent to
$$\Big| \bigcup_j T_j \Big| \;\ge\; C_\varepsilon\, \delta^{\varepsilon} \qquad \text{for all } \varepsilon>0,$$
i.e. the tubes may overlap at most polylogarithmically on average.

**Kakeya maximal function.** For $f \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$ and $e \in S^{n-1}$, let $T^\delta_e(a)$ be the $\delta\times 1$ tube centred at $a$ with direction $e$, and
$$f^*_\delta(e) \;=\; \sup_{a \in \mathbb{R}^n} \frac{1}{|T^\delta_e(a)|} \int_{T^\delta_e(a)} |f|.$$
**Maximal conjecture:** for every $\varepsilon>0$,
$$\|f^*_\delta\|_{L^n(S^{n-1})} \;\le\; C_\varepsilon\, \delta^{-\varepsilon} \|f\|_{L^n(\mathbb{R}^n)}.$$
This implies both dimension statements; the exponent $n$ is optimal (test against the indicator of a $\delta$-ball). More generally an $L^p \to L^q$ bound with $p \le n$ yields $\dim_H \ge$ an explicit function of $(p,q)$.

**Position in harmonic analysis.** Kakeya sits at the base of a hierarchy:
$$\text{Restriction} \;\Rightarrow\; \text{Bochner–Riesz} \;\Rightarrow\; \text{Kakeya}, \qquad \text{Local smoothing} \Rightarrow \text{Kakeya}.$$
The implication runs through Fefferman's ball-multiplier counterexample (1971) and Bourgain's bush/Córdoba square-function machinery: a Besicovitch set of dimension $<n$ would falsify the restriction conjecture for the sphere and the Bochner–Riesz conjecture, and would obstruct sharp local smoothing for the wave equation and $L^p$ bounds for the Fourier extension operator $\widehat{g\,d\sigma}$.

**Multilinear variant (proved).** Bennett–Carbery–Tao (2006), endpoint by Guth (2010): if $T_1,\dots,T_n$ are families of tubes with directions $\varepsilon$-transverse to the coordinate hyperplanes, then
$$\Big\| \prod_{k=1}^n \sum_{T \in \mathbb{T}_k} \chi_T \Big\|_{L^{\frac{1}{n-1}}(\mathbb{R}^n)} \;\lesssim_\varepsilon\; \prod_{k=1}^n \big(\delta^{n-1}\,\\#\mathbb{T}_k\big)^{\frac{1}{n-1}}.$$

## 3. History & State of the Art (SOTA)

- **1917.** Sōichi Kakeya asks for the minimal area of a plane region in which a unit needle can be reversed continuously.
- **1919/1928.** Besicovitch constructs a compact plane set of measure zero containing a unit segment in every direction (Perron-tree/"sprouting" construction), and derives measure-zero Kakeya *needle* sets. Consequence: the naive minimal-area problem has infimum $0$.
- **1971.** Davies: every plane Besicovitch set has $\dim_H = 2$. The case $n=2$ is closed.
- **1977.** Córdoba: sharp $L^2$ Kakeya maximal bound in the plane, $\|f^*_\delta\|_2 \lesssim (\log 1/\delta)^{1/2}\|f\|_2$.
- **1991.** Bourgain (GAFA) introduces the "bush" argument, giving $\dim_H \ge \frac{n+1}{2} + \varepsilon_n$, and links Kakeya to restriction.
- **1995.** Wolff's **hairbrush** argument: $\dim_H \ge \frac{n+2}{2}$ — in $\mathbb{R}^3$, $\dim \ge 5/2$. This bound stood for all $n$ for years and is still the benchmark for elementary methods.
- **1999–2002.** Katz–Łaba–Tao (Annals 2000) break $5/2$ for Minkowski dimension in $\mathbb{R}^3$ using sticky/plany/grainy structure; Katz–Tao (2002) obtain $\dim_M \ge \frac{4n+3}{7}$ and $\dim_H \ge (2-\sqrt2)(n-4)+3$ for large $n$, beating $\frac{n+2}{2}$ asymptotically.
- **2009.** Dvir's **polynomial method** resolves the finite-field analogue outright.
- **2010–2019.** Guth's polynomial partitioning; Katz–Zahl (JAMS 2019) push $\dim_H \ge 5/2 + \varepsilon_0$ in $\mathbb{R}^3$ with $\varepsilon_0 \approx 10^{-10}$; Zahl (2021) gives $\dim_H \ge 3.059$ in $\mathbb{R}^4$.
- **2025.** **Wang–Zahl** prove the Kakeya *set* conjecture in $\mathbb{R}^3$: every Besicovitch set in $\mathbb{R}^3$ has Hausdorff and Minkowski dimension $3$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n = 2$ | $\dim_H = 2$; maximal conjecture holds with $\log$ loss | Davies 1971; Córdoba 1977 |
| $n = 3$ | $\dim_H = \dim_M = 3$ (set conjecture **solved**) | Wang–Zahl 2025 |
| $n = 3$, sticky sets | Full conjecture for "sticky" Kakeya sets | Wang–Zahl 2022 |
| All $n$ | $\dim_H \ge (n+2)/2$ | Wolff 1995 |
| Large $n$ | $\dim_M \ge (4n+3)/7$; $\dim_H \ge (2-\sqrt2)(n-4)+3$ | Katz–Tao 2002 |
| $n = 4$ | $\dim_H \ge 3.059$ | Zahl 2021 |
| $n \ge 4$ | Improved maximal-function exponents past Wolff's range | Hickman–Rogers–Zhang 2022 |
| $\mathbb{F}_q^n$ | $|K| \ge q^n/2^n$ for any Kakeya set — **solved** | Dvir 2009; Dvir–Kopparty–Saraf–Sudan 2013 |
| Multilinear $\mathbb{R}^n$ | Endpoint transverse estimate — **solved** | Bennett–Carbery–Tao 2006; Guth 2010 |
| Structured families | Sets of lines with algebraic/self-similar structure, SL$_2$ Kakeya, curved Kakeya | Katz–Zahl; Wang–Zahl |

The **maximal function conjecture remains open in every dimension $n \ge 3$**, including $n=3$ where the set conjecture is now a theorem.

## 5. Principal Obstacles

- **Tubes are not points.** Dvir's polynomial method works over $\mathbb{F}_q$ because a low-degree polynomial vanishing on a set must vanish on every line meeting it in $>\deg$ points. Over $\mathbb{R}$ a $\delta$-tube meets a variety in a fuzzy neighbourhood; the "vanishing forces containment" step has no exact analogue, and the loss is exactly a power of $\delta$.
- **No obstruction to near-counterexamples.** Heuristic configurations — sticky, plany, grainy — each individually behave like a lower-dimensional set. Katz–Łaba–Tao's method is to show these three cannot coexist; ruling them out simultaneously requires quantitative incidence geometry that degrades badly as $n$ grows.
- **Fourier analysis is blind to dimension near the top.** $L^2$ methods and the Fourier-transform characterisation of dimension (via Frostman measures and $\int |\hat\mu(\xi)|^2 |\xi|^{s-n} d\xi$) cap out at $s = (n+1)/2$ for measures on Besicovitch sets — the bush bound. Wolff's hairbrush is essentially the limit of purely combinatorial incidence counting.
- **Two-ends/ multiplicity trade-offs.** Bounds derived from tube-intersection counting lose a factor at each induction-on-scales step; the accumulated loss is what leaves $\varepsilon_0 \approx 10^{-10}$ instead of a full $1/2$.
- **Higher dimensions lack a base case.** Wang–Zahl's $\mathbb{R}^3$ argument is built on a three-dimensional volume estimate for unions of convex sets and a sticky-reduction that uses the special structure of line families in $\mathbb{R}^3$ (a $4$-parameter Grassmannian with $2$-dimensional "point–line duality"). No $n \ge 4$ analogue is known.

## 6. The Gap

Proven: $\dim_H K \ge \max\{\frac{n+2}{2},\ (2-\sqrt2)(n-4)+3\}$ for $n \ge 4$; equality with $n$ only for $n \le 3$. The gap for $n = 4$ is $3.059$ vs $4$; asymptotically the proven exponent is $\approx 0.586n$ against the conjectured $n$ — a *constant-factor* deficiency, not an $\varepsilon$.

The precise barrier: current arguments bound the multiplicity of a tube family by counting incidences at a single scale and then inducting. Closing the gap requires a **structure theorem**: any $\delta$-tube family in $\mathbb{R}^n$ with $|\bigcup T| \le \delta^{\varepsilon}$ must be sticky (i.e. the map direction $\mapsto$ tube is Lipschitz after refinement) and hence, by a Wang–Zahl-type induction, self-similar and contradictory. Sticky reduction is known in $\mathbb{R}^3$; extending it to $\mathbb{R}^n$ is the open step. Separately, the maximal conjecture demands a bound uniform over all tube multiplicities, not just for tube families arising from an actual Kakeya set — the set-to-maximal upgrade is not formal.

## 7. Current Research (as of June 2026)

- **Wang–Zahl programme.** Hong Wang (NYU/IHES) and Joshua Zahl (UBC) posted *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* (arXiv:2502.17655, Feb 2025), proving $\dim K = 3$ in $\mathbb{R}^3$; accepted at *Annals of Mathematics* *(frontier — verify)*. Follow-up work targets the $\mathbb{R}^3$ maximal function and $\mathbb{R}^4$ via a higher-dimensional sticky reduction *(frontier — verify)*.
- **Restriction consequences.** Wang–Zahl's improved restriction estimate in $\mathbb{R}^3$ and Guth–Wang–Zhang's local smoothing theorem for the 2+1-dimensional wave equation (Annals 2020) feed back into Kakeya-type estimates.
- **Polynomial partitioning / algebraic methods.** Guth (MIT), Zahl, Katz (Rice), Zhang, Ou; Gromov's algebraic lemma and semialgebraic-set bounds as the engine for $n \ge 4$.
- **Furstenberg-set and projection theory.** Orponen, Shmerkin, Ren–Wang (the $\mathbb{R}^2$ Furstenberg set conjecture, resolved 2023) provide the incidence toolkit that Wang–Zahl reuse.
- **Finite-field and $p$-adic analogues, Assouad/packing variants**, and Keleti's line-segment extension conjecture, as tests for what dimension-theoretic phenomena are real.

## 8. Future Work

1. **Sticky reduction in $\mathbb{R}^n$, $n \ge 4$** — the single most-cited pathway; requires multi-scale self-similarity for line families in higher Grassmannians.
2. **Set $\Rightarrow$ maximal upgrade in $\mathbb{R}^3$**: prove $\|f^*_\delta\|_{L^3(S^2)} \lesssim_\varepsilon \delta^{-\varepsilon}\|f\|_3$, which would give Bochner–Riesz progress in three dimensions.
3. **Quantify the Wang–Zahl argument** to yield explicit $\mathcal{H}^{3-\varepsilon}$ lower bounds and, ideally, a logarithmic-loss statement matching the Besicovitch construction.
4. **Transfer restriction machinery downward**: derive Kakeya for $n=4$ from the multilinear estimate plus a broad/narrow decomposition with an improved narrow term.
5. **Search for a counterexample in large $n$** — no serious candidate exists, but the $0.586n$ vs $n$ gap means no one has verified the conjecture asymptotically.

## 9. Key References

- **[Foundational]** A. S. Besicovitch. *On Kakeya's problem and a similar one.* Mathematische Zeitschrift 27 (1928), 312–320. [DOI](https://doi.org/10.1007/bf01171101)
- **[Foundational]** R. O. Davies. *Some remarks on the Kakeya problem.* Proc. Cambridge Philos. Soc. 69 (1971), 417–421. [DOI](https://doi.org/10.1017/s0305004100046867)
- **[Foundational]** C. Fefferman. *The multiplier problem for the ball.* Annals of Mathematics 94 (1971), 330–336. [DOI](https://doi.org/10.2307/1970864)
- **[Foundational]** A. Córdoba. *The Kakeya maximal function and the spherical summation multipliers.* American J. of Mathematics 99 (1977), 1–22. [DOI](https://doi.org/10.2307/2374006)
- **[Foundational]** J. Bourgain. *Besicovitch type maximal operators and applications to Fourier analysis.* Geometric and Functional Analysis 1 (1991), 147–187. [DOI](https://doi.org/10.1007/bf01896376)
- **[Foundational]** T. Wolff. *An improved bound for Kakeya type maximal functions.* Revista Matemática Iberoamericana 11 (1995), 651–674. [DOI](https://doi.org/10.4171/rmi/188)
- **[Survey]** T. Wolff. *Recent work connected with the Kakeya problem.* In *Prospects in Mathematics* (H. Rossi, ed.), Amer. Math. Soc., 1999, 129–162.
- **[Survey]** P. Mattila. *Fourier Analysis and Hausdorff Dimension.* Cambridge University Press, 2015.
- **[Milestone]** N. Katz, I. Łaba, T. Tao. *An improved bound on the Minkowski dimension of Besicovitch sets in $\mathbb{R}^3$.* Annals of Mathematics 152 (2000), 383–446. [DOI](https://doi.org/10.2307/2661389)
- **[Milestone]** N. Katz, T. Tao. *New bounds for Kakeya problems.* Journal d'Analyse Mathématique 87 (2002), 231–263. [DOI](https://doi.org/10.1007/bf02868476)
- **[Milestone]** J. Bennett, A. Carbery, T. Tao. *On the multilinear restriction and Kakeya conjectures.* Acta Mathematica 196 (2006), 261–302. [DOI](https://doi.org/10.1007/s11511-006-0006-4)
- **[Milestone]** Z. Dvir. *On the size of Kakeya sets in finite fields.* J. Amer. Math. Soc. 22 (2009), 1093–1097. [DOI](https://doi.org/10.1090/s0894-0347-08-00607-3)
- **[Milestone]** L. Guth. *The endpoint case of the Bennett–Carbery–Tao multilinear Kakeya conjecture.* Acta Mathematica 205 (2010), 263–286. [DOI](https://doi.org/10.1007/s11511-010-0055-6)
- **[SOTA]** N. Katz, J. Zahl. *An improved bound on the Hausdorff dimension of Besicovitch sets in $\mathbb{R}^3$.* J. Amer. Math. Soc. 32 (2019), 195–259.
- **[SOTA]** J. Zahl. *New Kakeya estimates using Gromov's algebraic lemma.* Advances in Mathematics 380 (2021), 107596. [DOI](https://doi.org/10.1016/j.aim.2021.107596)
- **[SOTA]** H. Wang, J. Zahl. *Sticky Kakeya sets and the sticky Kakeya conjecture.* arXiv:2210.09581 (2022).
- **[SOTA]** H. Wang, J. Zahl. *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions.* arXiv:2502.17655 (2025).
- **[Textbook]** L. Guth. *Polynomial Methods in Combinatorics.* University Lecture Series 64, Amer. Math. Soc., 2016.

## 10. Worked Example / Concrete Special Case

**The Perron sprouting step, computed.** Let $T$ be a triangle with base $[0,1]\times\{0\}$ and apex $A = (a, h)$, so $|T| = h/2$. Bisect $T$ by the median from $A$ to $(1/2,0)$ into left half $T_1$ and right half $T_2$, each of area $|T|/2$. Now translate $T_2$ leftwards along the $x$-axis by $(1-\alpha)$, for a parameter $\alpha \in [1/2, 1]$.

The union $T_1 \cup (T_2 - (1-\alpha,0))$ consists of a **heart** (a scaled copy of $T$ by factor $\alpha$, sitting on the base, area $\alpha^2 |T|$) plus two **sprouts** above it. A direct area computation gives
$$\big|T_1 \cup (T_2 - (1-\alpha,0))\big| \;=\; \big(2\alpha^2 - 2\alpha + 1\big)\,|T|.$$
Check the endpoints: $\alpha = 1$ (no translation) returns $|T|$; $\alpha = 1/2$ gives $|T|/2$ — half the area, while the *set of directions of segments* contained in the figure is unchanged, because every segment of $T_2$ is merely translated.

**Iterating.** Subdivide the base into $2^k$ equal pieces, forming $2^k$ triangles, and apply the sprouting step at every level of a binary tree with $\alpha = 1/2$ at each merge. The resulting **Perron tree** $P_k$ still contains a segment in every direction subtended by $T$, and satisfies
$$|P_k| \;\lesssim\; \frac{1}{k}\,|T| \;=\; \frac{1}{\log_2 (\text{number of pieces})}\,|T| \;\xrightarrow[k\to\infty]{} 0 .$$
Taking $\delta = 2^{-k}$, the tree is essentially the $\delta$-neighbourhood of a limiting compact set, and
$$\Big|\bigcup_j T_j\Big| \;\approx\; \frac{1}{\log(1/\delta)} \;=\; \delta^{o(1)} .$$

**Reading off the conjecture.** The overlap loss is only *logarithmic* in $\delta$, never a power $\delta^{\varepsilon}$. Since $\dim_M = 2 - \liminf \frac{\log|K_\delta|}{\log\delta}$ and $\log(1/\log(1/\delta))/\log\delta \to 0$, we get $\dim_M K = 2$: measure zero, full dimension. The Kakeya conjecture asserts that this is the *worst* that can happen in every dimension — no Besicovitch set can achieve a genuine power saving $|\bigcup_j T_j| \le \delta^{c}$ with $c>0$. Six decades of work have shown this in $\mathbb{R}^2$ (Davies) and, in 2025, in $\mathbb{R}^3$ (Wang–Zahl); for $n \ge 4$ the best that is excluded is $c > 1 - \frac{3.059}{4} \approx 0.235$ (for $n = 4$), leaving the bulk of the range open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*