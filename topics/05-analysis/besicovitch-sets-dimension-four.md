---
id: 05-analysis/besicovitch-sets-dimension-four
title: "The Dimension of Besicovitch Sets in Four Dimensions"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Dimension of Besicovitch Sets in Four Dimensions

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/besicovitch-sets-dimension-four` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **Besicovitch set** (Kakeya set) in $\mathbb{R}^n$ is a compact set containing a unit line segment in every direction. Besicovitch (1919, 1928) showed such sets can have Lebesgue measure zero. The **Kakeya set conjecture** asserts they cannot be small in dimension:

> **Conjecture (Kakeya, $n=4$).** Every Besicovitch set $E \subset \mathbb{R}^4$ has Hausdorff dimension $\dim_H E = 4$.

The Minkowski (box) version asks for $\dim_M E = 4$; it is formally weaker, since $\dim_H \le \underline{\dim}_M \le \overline{\dim}_M$. A complete resolution means either a proof that $\dim_H E \ge 4 - \varepsilon$ for all $\varepsilon > 0$ and all such $E$, or an explicit construction of a Besicovitch set in $\mathbb{R}^4$ with $\dim_H E < 4$ (which would also refute the maximal-function, restriction and Bochner–Riesz conjectures in $\mathbb{R}^4$).

The status is *partially-solved* in the sense that $n=1,2$ are trivial/classical and $n=3$ was settled by Wang–Zahl (2025); $n=4$ is the first fully open case, and the best unconditional bound is $\dim_H E \ge 3 + \tfrac{1}{40}$ (Katz–Zahl 2021).

## 2. Mathematical Foundations

**Hausdorff dimension.** For $s\ge 0$, $\mathcal{H}^s(E) = \lim_{\delta\to 0}\inf\{\sum_i (\operatorname{diam} U_i)^s : E \subset \bigcup_i U_i,\ \operatorname{diam} U_i \le \delta\}$, and $\dim_H E = \inf\{s : \mathcal{H}^s(E)=0\}$.

**Minkowski dimension.** With $N(E,\delta)$ the number of $\delta$-balls needed to cover $E$,
$$\overline{\dim}_M E = \limsup_{\delta \to 0} \frac{\log N(E,\delta)}{\log(1/\delta)} .$$

**Besicovitch set.** $E\subset\mathbb{R}^n$ compact with: for every $e \in S^{n-1}$ there is $x\in\mathbb{R}^n$ with $\{x + te : t\in[0,1]\}\subset E$.

**$\delta$-discretized form.** Let $\{T_j\}_{j=1}^{M}$, $M \approx \delta^{-(n-1)}$, be $\delta\times 1$ tubes with $\delta$-separated directions. The Kakeya conjecture is equivalent to: for all $\varepsilon>0$,
$$\Big|\bigcup_{j} T_j\Big| \;\gtrsim_\varepsilon\; \delta^{\varepsilon}.$$
A bound $\big|\bigcup_j T_j\big| \gtrsim \delta^{n-d}$ corresponds to a Minkowski dimension lower bound $d$; the Hausdorff statement requires the same estimate uniformly over multi-scale (non-uniform) tube configurations.

**Kakeya maximal function.** For $f\in L^1_{loc}(\mathbb{R}^n)$ and $e \in S^{n-1}$,
$$f^*_\delta(e) = \sup_{x\in\mathbb{R}^n} \frac{1}{|T_e^\delta(x)|}\int_{T_e^\delta(x)} |f|,$$
$T_e^\delta(x)$ the $\delta\times 1$ tube centred at $x$ with axis $e$. The **maximal conjecture** in $\mathbb{R}^4$ is
$$\|f^*_\delta\|_{L^4(S^3)} \lesssim_\varepsilon \delta^{-\varepsilon}\|f\|_{L^4(\mathbb{R}^4)},$$
and implies the set conjecture in $\mathbb{R}^4$.

**Hierarchy.** Restriction $\Rightarrow$ Bochner–Riesz-type $\Rightarrow$ Kakeya maximal $\Rightarrow$ Kakeya set. Fefferman's ball-multiplier theorem (1971) built a counterexample directly from a Besicovitch set, fixing the place of Kakeya at the base of this tower.

**Key structural tools.** The *bush* argument ($\dim \ge (n+1)/2$), Wolff's *hairbrush* ($\dim_H \ge (n+2)/2$, so $\ge 3$ in $\mathbb{R}^4$), Katz–Zahl's *planebrush* (the union of tubes meeting a fixed 2-plane), polynomial partitioning, and the *polynomial Wolff axioms*: a tube family obeys them if for every degree-$D$ algebraic variety $Z$, at most $C_D \delta^{-(n-1)} \cdot (\text{codim factor})$ tubes lie in the $\delta$-neighbourhood of $Z$.

## 3. History & State of the Art (SOTA)

- **1917–1928.** Kakeya's needle problem; Besicovitch's measure-zero solution; Besicovitch (1928) makes the connection explicit.
- **1971.** Davies: every Besicovitch set in $\mathbb{R}^2$ has $\dim_H = 2$. Fefferman: ball multiplier is unbounded on $L^p$, $p\ne 2$.
- **1991.** Bourgain (GAFA): bush-type bound $\dim_H \ge (n+1)/2$ plus arithmetic input.
- **1995.** Wolff: hairbrush bound $\dim_H \ge (n+2)/2$ — in $\mathbb{R}^4$ this gives $3$, and it stood as the unconditional record for over two decades.
- **1999–2002.** Bourgain and Katz–Tao introduce additive-combinatorial (sum-difference / arithmetic Kakeya) methods: bounds like $\frac{13n+12}{25}$, $\frac{4n+3}{7}$, and the Minkowski bound $(2-\sqrt2)(n-4)+3$. These beat Wolff only for $n \ge 5$; at $n=4$ they exactly reproduce $3$.
- **2000–2001.** Katz–Łaba–Tao: $\overline{\dim}_M \ge 5/2 + 10^{-10}$ in $\mathbb{R}^3$; Łaba–Tao: $\varepsilon_n$-improvements to the Minkowski bound in "medium" dimensions $n \ge 4$.
- **2016–2019.** Guth's polynomial partitioning transfers to Kakeya; Guth–Zahl prove Kakeya-type estimates in $\mathbb{R}^4$ for tube families obeying the polynomial Wolff axioms; Katz–Zahl reach $\dim_H \ge 5/2 + \varepsilon_0$ in $\mathbb{R}^3$.
- **2021.** **Katz–Zahl, planebrushes:** $\dim_H E \ge 3 + \frac{1}{40} = 3.025$ for Besicovitch sets in $\mathbb{R}^4$ — the current unconditional record.
- **2025.** **Wang–Zahl** prove the Kakeya set conjecture in $\mathbb{R}^3$ ($\dim_H = 3$), via volume estimates for unions of convex sets and the sticky/SL$_2$ structure theory. $n = 4$ becomes the leading open case.

## 4. Partial Results / Verified Cases

| Result | Setting | Bound in $\mathbb{R}^4$ |
|---|---|---|
| Davies (1971) | $n=2$ | conjecture true ($\dim_H = 2$) |
| Wang–Zahl (2025) | $n=3$ | conjecture true ($\dim_H = 3$) |
| Wolff (1995), hairbrush | all $n$ | $\dim_H \ge (n+2)/2 = 3$ |
| Katz–Tao (2002), arithmetic | $n\ge5$ mainly | $=3$ at $n=4$ (no gain) |
| Łaba–Tao (2001) | Minkowski, $n\ge4$ | $\overline{\dim}_M \ge 3 + \varepsilon_4$ |
| **Katz–Zahl (2021), planebrush** | $n=4$ | $\dim_H \ge 3 + 1/40$ |
| Guth–Zahl (2018) | $n=4$, conditional | improved bounds under polynomial Wolff axioms |
| Hickman–Rogers–Zhang (2022) | $n \ge 5$ | polynomial Wolff axioms verified, better exponents |

Special classes where full dimension $4$ is known in $\mathbb{R}^4$: sets of lines contained in an algebraic variety of bounded degree (via polynomial method / Wolff's finite-field analogue arguments); *sticky* Kakeya sets and self-similar configurations, where the direction-to-position map is approximately Lipschitz across scales (the $\mathbb{R}^3$ sticky theory of Wang–Zahl); Besicovitch sets whose line family carries a group structure such as $\mathrm{SL}_2$-type line sets, analysed by Katz–Wu–Zahl. The finite-field analogue is fully solved in all dimensions by Dvir's polynomial method (Kakeya sets in $\mathbb{F}_q^n$ have $\ge c_n q^n$ points).

## 5. Principal Obstacles

- **Wolff's hairbrush saturates at $(n+2)/2$.** The hairbrush counts tubes meeting a fixed tube; those tubes are essentially confined to a 3-dimensional slab in $\mathbb{R}^4$ and the two-dimensional X-ray estimate used is sharp. No purely incidence-geometric bookkeeping at one scale beats $3$.
- **Arithmetic methods are dimension-inefficient at $n=4$.** The Katz–Tao sum-difference machinery converts Kakeya into $\mathbb{Z}$-valued additive combinatorics; its gains scale with $n$ and vanish at $n=4$.
- **The planebrush loses in codimension 2.** A planebrush controls tubes near a 2-plane; in $\mathbb{R}^4$ the complementary directions form a 1-parameter family and the resulting gain is only $1/40$.
- **Polynomial partitioning does not close the loop.** In $\mathbb{R}^3$ the induction on scales terminates because a degree-$D$ surface containing many lines is essentially a plane or a quadric (ruled-surface classification). In $\mathbb{R}^4$ the varieties containing $2$-parameter families of lines are far richer (quadrics, hypersurfaces with 2-dimensional rulings, Grassmannian sub-varieties), so the "algebraic case" of the induction is not a base case but another open problem.
- **No Hausdorff-to-Minkowski transfer.** Multi-scale, non-uniform configurations (Assouad-type behaviour) must be handled directly; several $\mathbb{R}^4$ arguments give Minkowski gains that do not currently upgrade.
- **The Wang–Zahl $\mathbb{R}^3$ proof is genuinely 3-dimensional.** Its grains/convex-set volume estimates and the sticky reduction use that the space of directions is $S^2$ and that "planes" have codimension 1; the SL$_2$ example, which is the extremal obstruction in $\mathbb{R}^3$, has no classified $\mathbb{R}^4$ counterpart.

## 6. The Gap

Proven: $\dim_H E \ge 3.025$. Conjectured: $\dim_H E = 4$. The gap is $0.975$ — nearly a full unit of dimension, and larger relatively than the $\mathbb{R}^3$ gap ever was after Wolff.

The precise barrier: current arguments extract a lower bound of the form $\frac{n+2}{2} + \varepsilon$, i.e. they exploit *one* auxiliary object (a line, a plane) of dimension $\le 2$ inside the configuration. Reaching $4$ requires a genuine $k$-plane induction: an estimate quantifying how a Besicovitch set in $\mathbb{R}^4$ concentrates near $2$- and $3$-planes at *every* scale simultaneously, plus a classification of the $\mathbb{R}^4$ line families that are extremal for each such concentration (the analogue of the SL$_2$ example). Equivalently: prove the $L^4(S^3)$ Kakeya maximal bound, or an $\mathbb{R}^4$ volume estimate for unions of "grains" (convex sets in a multi-scale family) matching what Wang–Zahl proved in $\mathbb{R}^3$.

## 7. Current Research (as of June 2026)

- **Wang–Zahl programme (NYU / UBC).** Extending the 3D convex-set volume estimates and the sticky reduction to $\mathbb{R}^4$. The stated intermediate goal is a structure theorem for sticky Kakeya sets in $\mathbb{R}^4$; several partial preprints circulate. *(frontier — verify)*
- **Higher-dimensional polynomial Wolff axioms.** Hickman–Rogers–Zhang-style verification combined with Guth–Zahl's $\mathbb{R}^4$ estimates, aiming at an unconditional $\mathbb{R}^4$ bound above $3.1$. *(frontier — verify)*
- **Projection theory input.** Ren–Wang's resolution of the Furstenberg set problem in the plane supplies sharp $L^p$ projection/exceptional-set estimates now being pushed into $\mathbb{R}^3\to\mathbb{R}^4$ slicing arguments.
- **SL$_2$-type and group-theoretic examples.** Katz–Wu–Zahl's construction is being generalised to $\mathbb{R}^4$ to locate the true extremisers; if a $4$-dimensional analogue is more efficient than expected, it constrains any prospective proof.
- **Adjacent conjectures.** Local smoothing and restriction in $\mathbb{R}^4$ (Guth–Wang–Zhang methodology) feed back into Kakeya via decoupling.

## 8. Future Work

- Prove the $\mathbb{R}^4$ **sticky Kakeya conjecture** first; sticky sets are conjecturally the extremal case, as in $\mathbb{R}^3$.
- Develop a **"brush" hierarchy**: bush (point), hairbrush (line), planebrush (2-plane), and a genuine 3-plane brush in $\mathbb{R}^4$, with a scheme that combines gains rather than choosing the best single one.
- Classify **degree-$D$ hypersurfaces in $\mathbb{R}^4$ containing $2$-parameter line families**, to close the algebraic branch of polynomial partitioning.
- Upgrade Minkowski-only gains ($\Lambda$aba–Tao) to Hausdorff via multi-scale/Assouad decompositions.
- Test candidate constructions numerically: search for $\delta$-discretised tube families in $\mathbb{R}^4$ with $|\bigcup T_j| \ll \delta^{1-\varepsilon}$, which would signal a counterexample.

## 9. Key References

- **[Foundational]** A. S. Besicovitch. *On Kakeya's problem and a similar one.* Mathematische Zeitschrift 27, 312–320, 1928.
- **[Foundational]** R. O. Davies. *Some remarks on the Kakeya problem.* Proc. Cambridge Philos. Soc. 69, 417–421, 1971.
- **[Foundational]** C. Fefferman. *The multiplier problem for the ball.* Annals of Mathematics 94, 330–336, 1971.
- **[Foundational]** J. Bourgain. *Besicovitch type maximal operators and applications to Fourier analysis.* Geom. Funct. Anal. 1, 147–187, 1991.
- **[Foundational]** T. Wolff. *An improved bound for Kakeya type maximal functions.* Revista Matemática Iberoamericana 11, 651–674, 1995.
- **[Foundational]** N. H. Katz, I. Łaba, T. Tao. *An improved bound on the Minkowski dimension of Besicovitch sets in $\mathbb{R}^3$.* Annals of Mathematics 152, 383–446, 2000.
- **[Foundational]** I. Łaba, T. Tao. *An improved bound on the Minkowski dimension of Besicovitch sets in medium dimension.* Geom. Funct. Anal. 11, 773–806, 2001.
- **[Foundational]** N. H. Katz, T. Tao. *New bounds for Kakeya problems.* Journal d'Analyse Mathématique 87, 231–263, 2002.
- **[SOTA / Recent]** N. H. Katz, J. Zahl. *A Kakeya maximal function estimate in four dimensions using planebrushes.* Revista Matemática Iberoamericana 37, 317–359, 2021.
- **[SOTA / Recent]** L. Guth, J. Zahl. *Polynomial Wolff axioms and Kakeya-type estimates in $\mathbb{R}^4$.* Proc. London Math. Soc. 117, 192–220, 2018.
- **[SOTA / Recent]** J. Hickman, K. M. Rogers, R. Zhang. *Improved bounds for the Kakeya maximal conjecture in higher dimensions.* American Journal of Mathematics 144, 2022.
- **[SOTA / Recent]** N. H. Katz, J. Zahl. *An improved bound on the Hausdorff dimension of Besicovitch sets in $\mathbb{R}^3$.* J. Amer. Math. Soc. 32, 195–259, 2019.
- **[SOTA / Recent]** H. Wang, J. Zahl. *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions.* arXiv:2502.17655, 2025.
- **[SOTA / Recent]** N. H. Katz, S. Wu, J. Zahl. *Kakeya sets from lines in $\mathrm{SL}_2$.* Ars Inveniendi Analytica, 2023.
- **[Survey]** T. Wolff. *Recent work connected with the Kakeya problem.* In *Prospects in Mathematics*, AMS, 129–162, 1999.
- **[Survey]** T. Tao. *From rotating needles to stability of waves: emerging connections between combinatorics, analysis, and PDE.* Notices of the AMS 48, 294–303, 2001.
- **[Survey]** P. Mattila. *Fourier Analysis and Hausdorff Dimension.* Cambridge University Press, 2015.

## 10. Worked Example / Concrete Special Case

**(a) Building a measure-zero Besicovitch set in $\mathbb{R}^4$.** Let $B\subset\mathbb{R}^2$ be a planar Besicovitch set with $|B|_2=0$ (Besicovitch 1928). Put $E = B \times [0,1]^2 \subset \mathbb{R}^4$, together with the slab $S=\{0\}\times\{0\}\times[0,1]^2$.

*Directions.* Take $u=(u_1,u_2,u_3,u_4)\in S^3$. If $(u_1,u_2)\ne 0$, write $c=|(u_1,u_2)|$ and $v = (u_1,u_2)/c \in S^1$. $B$ contains a unit segment $\{p + s v : s\in[0,1]\}$. Then
$$\{(p,q) + t\,u : t \in [0, \min(1, c^{-1}\cdot 1)]\},\qquad q \in (0,1)^2 \text{ chosen so the last two coordinates stay in } [0,1]^2,$$
lies in $E$ after rescaling $t$, because its first two coordinates trace $p + (tc)v \in B$. If $(u_1,u_2)=0$ the direction is $(0,0,u_3,u_4)$ and the segment lies in $S$.

*Measure.* By Fubini, $|E|_4 = |B|_2 \cdot 1 = 0$, and $|S|_4 = 0$.

*Dimension.* $\dim_H(B\times[0,1]^2) = \dim_H B + 2 = 2+2 = 4$, using $\dim_H B = 2$ (Davies) and the product formula for a set times a cube. So this construction is consistent with the conjecture: it is null but full-dimensional. Every known construction behaves this way — measure zero is easy, dimension deficiency has never been produced.

**(b) Where the hairbrush bound $3$ comes from in $\mathbb{R}^4$.** Discretise: $M \approx \delta^{-3}$ tubes $T_j$ of dimensions $\delta\times 1$, and suppose $|\bigcup_j T_j| = \delta^{4-d}$, so each tube has, on average, $\mu \approx |T_j| \cdot M / \delta^{4-d} = \delta^3\cdot\delta^{-3}/\delta^{4-d} = \delta^{d-4}$ overlap. Fix a tube $T_0$ and let $H$ be the *hairbrush*: all tubes meeting $T_0$. Counting incidences along $T_0$ gives $\\#H \gtrsim \mu\,\delta^{-1} = \delta^{d-5}$. Tubes in $H$ through a fixed $\delta$-ball of $T_0$ are essentially disjoint after the first, and Wolff's two-dimensional X-ray estimate bounds their overlap by $O(\log)$ on the transversal slices, giving
$$\Big|\bigcup_{T\in H} T\Big| \gtrsim \\#H \cdot \delta^{3} \cdot \delta \approx \delta^{d-1}.$$
Since this cannot exceed $\delta^{4-d}$, we need $d-1 \ge 4-d$, i.e. $d \ge 5/2$ — the raw count. Wolff's sharper bookkeeping (angular separation of tubes in the brush, exploited slice by slice) upgrades this to $d \ge (n+2)/2 = 3$ at $n=4$. Katz–Zahl replace the line $T_0$ by a $2$-plane, and the extra parameter buys exactly $1/40$: $d \ge 3.025$. Closing the remaining $0.975$ is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*