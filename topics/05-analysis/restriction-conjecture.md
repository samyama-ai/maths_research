---
id: 05-analysis/restriction-conjecture
title: "Restriction Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Restriction Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/restriction-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $S^{d-1}\subset\mathbb{R}^d$ ($d\ge 2$) be the unit sphere with surface measure $d\sigma$. For $f\in L^q(S^{d-1},d\sigma)$ define the **extension operator**
$$
Ef(x) \;=\; \widehat{f\,d\sigma}(x) \;=\; \int_{S^{d-1}} f(\xi)\, e^{2\pi i\, x\cdot\xi}\, d\sigma(\xi), \qquad x\in\mathbb{R}^d .
$$

**Restriction Conjecture (Stein, 1967).** For $d\ge 2$,
$$
\|Ef\|_{L^p(\mathbb{R}^d)} \;\le\; C_{p,q,d}\,\|f\|_{L^q(S^{d-1})}
$$
holds **if and only if**
$$
p > \frac{2d}{d-1} \qquad\text{and}\qquad \frac{d+1}{p} \le \frac{d-1}{q'},\quad \tfrac1q+\tfrac1{q'}=1 .
$$

The case $q=\infty$ is the core statement: $\|Ef\|_{L^p(\mathbb{R}^d)}\lesssim\|f\|_{L^\infty(S^{d-1})}$ for all $p>\frac{2d}{d-1}$. By duality this is equivalent to the *restriction* estimate $\|\hat g\,|_{S^{d-1}}\|_{L^{q'}(d\sigma)}\lesssim\|g\|_{L^{p'}(\mathbb{R}^d)}$ — meaningful because $\hat g$ for $g\in L^{p'}$ is only defined a.e., yet curvature forces its restriction to $S^{d-1}$ to exist.

A complete resolution means proving the estimate for every $p>\frac{2d}{d-1}$ in some $d\ge 3$ where it is open (all $d\ge 3$), or exhibiting a counterexample in that range. The necessity of the two conditions is elementary (Section 10); only sufficiency is open.

## 2. Mathematical Foundations

**Truncated paraboloid model.** Locally the sphere is equivalent to $\mathbb{P}^{d-1}=\{(\xi,|\xi|^2):|\xi|\le 1\}$, and one studies
$$
E_{\mathbb{P}}f(x) = \int_{|\xi|\le 1} f(\xi)\,e^{2\pi i(x'\cdot\xi + x_d|\xi|^2)}\,d\xi .
$$
The parabolic rescaling symmetry $\xi\mapsto \xi_0+\delta\xi$ makes $\mathbb{P}^{d-1}$ the standard test case; the conjectured range is identical.

**Decay of $\widehat{d\sigma}$.** Stationary phase gives
$$
\widehat{d\sigma}(x) = 2|x|^{-\frac{d-1}{2}}\cos\!\Big(2\pi|x| - \tfrac{(d-1)\pi}{4}\Big) + O\big(|x|^{-\frac{d+1}{2}}\big),
$$
valid because the Gaussian curvature of $S^{d-1}$ is nonvanishing.

**Stein–Tomas theorem.** If $\mu$ is a compactly supported measure with $|\hat\mu(x)|\lesssim (1+|x|)^{-\alpha}$, then $\|\widehat{f d\mu}\|_{L^p}\lesssim\|f\|_{L^2(d\mu)}$ for $p\ge \frac{2\alpha+2}{\alpha}$. For $S^{d-1}$, $\alpha=\frac{d-1}{2}$, giving the sharp $L^2$-based exponent
$$
p \ge p_{ST}(d) = \frac{2(d+1)}{d-1}.
$$

**Kakeya connection.** Restriction $\Rightarrow$ Kakeya: the conjecture for $p>\frac{2d}{d-1}$ implies every Besicovitch set in $\mathbb{R}^d$ has Hausdorff (and Minkowski) dimension $d$. The mechanism is wave-packet decomposition: $Ef$ on a ball $B_R$ decomposes as $\sum_T c_T \psi_T$ over $R^{1/2}\times\cdots\times R^{1/2}\times R$ tubes $T$ dual to $R^{-1/2}$-caps, so $L^p$ bounds control overlap of tube families.

**Multilinear restriction (Bennett–Carbery–Tao, 2006).** If $S_1,\dots,S_d$ are transverse pieces (normals spanning a set of volume $\gtrsim\nu$), then for $p\ge\frac{2d}{d-1}$ and all $\varepsilon>0$,
$$
\Big\|\prod_{j=1}^d E_j f_j\Big\|_{L^{p/d}(B_R)} \lesssim_\varepsilon R^{\varepsilon}\prod_{j=1}^d \|f_j\|_{L^2}.
$$
The multilinear problem is thus essentially **solved**; the difficulty is entirely in transferring it to the linear estimate.

## 3. History & State of the Art (SOTA)

- **1967:** E. M. Stein poses the restriction problem; first published instances in Fefferman's thesis work.
- **1970:** Fefferman (*Acta Math.* 124) proves the $d=2$ case for $p>4$, $q=\infty$; Zygmund (1974) obtains the full $L^q\to L^p$ range for the circle. **$d=2$ is closed.**
- **1971:** Fefferman disproves the ball multiplier conjecture, showing that curvature-free analogues fail and that Besicovitch geometry is intrinsic to the subject.
- **1975:** Tomas proves the $L^2$ restriction theorem for $p>\frac{2(d+1)}{d-1}$; Stein supplies the endpoint.
- **1991:** Bourgain (*GAFA*) gives the first improvement past Stein–Tomas in $d=3$, using Kakeya maximal estimates.
- **1995–2003:** Bilinear era. Wolff's sharp bilinear cone estimate (*Ann. of Math.* 153, 2001) and Tao's sharp bilinear paraboloid estimate (*GAFA* 13, 2003) give linear restriction for $p>\frac{2(d+2)}{d}$ — i.e. $p>10/3$ in $d=3$.
- **2006–2011:** Multilinear era. Bennett–Carbery–Tao prove the multilinear conjecture; Bourgain–Guth (*GAFA* 21, 2011) convert it into linear gains in every $d\ge3$.
- **2016–2018:** Polynomial partitioning. Guth proves $p>3.25$ in $\mathbb{R}^3$ (*JAMS* 29, 2016) and extends the method to all $d\ge3$ (*Acta Math.* 221, 2018).
- **2019–2022:** Hickman–Rogers refine higher-dimensional exponents; Hong Wang's "broom" argument gives $p>3+\frac{3}{13}\approx 3.2308$ in $\mathbb{R}^3$ (*Duke Math. J.* 171, 2022) — the current published record in three dimensions.
- **2025:** Wang–Zahl prove the **Kakeya set conjecture in $\mathbb{R}^3$** (every Besicovitch set in $\mathbb{R}^3$ has Hausdorff dimension 3), removing the necessary geometric obstruction in the first open dimension.

## 4. Partial Results / Verified Cases

| Case | Known range | Source |
|---|---|---|
| $d=2$, all $q$ | Full conjectured range, $p>4$ | Fefferman 1970; Zygmund 1974 |
| All $d$, $q=2$ | $p\ge \frac{2(d+1)}{d-1}$ (sharp for $q=2$) | Tomas 1975; Stein (endpoint) |
| $d=3$, $q=\infty$ | $p>3+\tfrac{3}{13}\approx 3.2308$ (conj. $p>3$) | H. Wang 2022 |
| $d\ge 4$, $q=\infty$ | Guth 2018 exponents, refined by Hickman–Rogers 2019 | — |
| Light cone in $\mathbb{R}^d$, low $d$ | Full conjectured range in low dimensions ($d\le 4$) | Wolff 2001 |
| Finite-field paraboloid | Full range in several cases (e.g. $\mathbb{F}_q^3$ partial) | Mockenhaupt–Tao 2004 |
| Fractal/Salem measures | Stein–Tomas analogue with $\alpha$ = decay rate | Mockenhaupt 2000; Bak–Seeger 2011 |

Additional verified classes: surfaces of finite type and flat convex hypersurfaces (sharp results in $d=2,3$ for many profiles); the estimate for all $p>\frac{2d}{d-1}$ is known for the sphere when $q$ is small enough that the $L^2$ theorem applies after interpolation.

**Non-example.** For hypersurfaces of nonvanishing but *indefinite* second fundamental form (e.g. the hyperbolic paraboloid $\xi_1\xi_2$), the naive analogue of the conjecture fails in part of the range — curvature sign matters, not just nondegeneracy.

## 5. Principal Obstacles

- **$L^2$ orthogonality is exhausted.** Stein–Tomas uses only the decay of $\widehat{d\sigma}$ and is *sharp* for $q=2$ (the Knapp cap saturates it). Any progress below $\frac{2(d+1)}{d-1}$ must use genuinely non-$L^2$ information about how wave packets can overlap.
- **Kakeya is necessary but insufficient.** Restriction implies Kakeya, so no method can beat the Kakeya barrier; but the converse fails. Even with Wang–Zahl's 2025 resolution of Kakeya in $\mathbb{R}^3$, dimension statements are far weaker than the quantitative $L^p$ tube-overlap bounds restriction requires (Kakeya controls only $R^{\varepsilon}$-level multiplicity, not the amplitude/phase interference that restriction sees).
- **Multilinear-to-linear loss.** Bourgain–Guth's transference costs a factor tied to the number of transverse directions; the "broad/narrow" dichotomy handles broad cases via multilinear estimates but leaves *narrow* configurations (all wave packets clustered near a lower-dimensional variety) to be handled by induction on scales, which leaks.
- **Polynomial partitioning stalls at algebraic configurations.** Guth's method reduces to tubes trapped in a neighbourhood of a low-degree variety. Two-dimensional and $SL_2$-type examples — tube families invariant under a matrix group — are consistent with all currently known estimates yet are not extremal for restriction, so the method cannot detect their non-optimality.
- **Two-ends and broom phenomena.** Wolff's two-ends reduction and Wang's brooms exploit that tubes concentrating heavily must fan out at some scale; quantifying this loss efficiently across all scales simultaneously is unresolved.
- **No known sharp example other than the two elementary ones.** Both necessary conditions come from a single cap (Knapp) or the whole sphere (focusing). The absence of a richer family of near-extremizers means the community lacks a target geometry to design a matching argument against.

## 6. The Gap

For $d=3$, $q=\infty$: proven for $p>3+\frac{3}{13}$; conjectured for $p>3$. The open interval is
$$
3 < p \le 3+\tfrac{3}{13}\approx 3.2308,
$$
a gap of $0.2308$ in the exponent — and the endpoint-adjacent regime is exactly where the wave-packet count $R^{(d-1)/2}$ balances against the volume $R^d$, so every scale contributes equally and induction-on-scales gains vanish.

Concretely, the missing step is a bound of the form: for $R^{-1/2}$-separated wave packets $\{T\}$ with $\\#\{T\ni x\}$ large on a set $Y$, either $Y$ is $\varepsilon$-close to a plane-like or $SL_2$-like configuration (which must then be shown to obey a *better* estimate via lower-dimensional decoupling), or the multilinear estimate applies with no loss. Present arguments prove one horn or the other but not a partition of cases that closes at $p=\frac{2d}{d-1}$.

## 7. Current Research (as of June 2026)

- **Post-Kakeya reassessment.** Wang–Zahl's 2025 proof of the three-dimensional Kakeya set conjecture, together with their earlier sticky-Kakeya and $SL_2$ structure theorems, is being mined for quantitative $L^p$ consequences. The consensus is that a *maximal-function* strengthening (Kakeya maximal conjecture in $\mathbb{R}^3$ with $R^\varepsilon$ loss) is the realistic next milestone before restriction moves. *(frontier — verify)*
- **Two-ends Furstenberg inequalities.** Wang–Wu's programme replaces broom counting by Furstenberg-set estimates, reportedly pushing the $\mathbb{R}^3$ exponent below $3+\frac{3}{13}$. *(frontier — verify)*
- **Decoupling-based approaches.** Bourgain–Demeter $\ell^2$ decoupling gives sharp results for exponential sums and Bochner–Riesz-type problems but is $L^2$-based and cannot alone reach the restriction range; hybrid decoupling/partitioning schemes are the active line.
- **Higher-dimensional exponents.** Continued refinement of Guth II and Hickman–Rogers via nested polynomial partitioning and transverse equidistribution, chiefly in the MIT, IAS, NYU/Courant, Edinburgh, Bonn and Wisconsin harmonic-analysis groups.
- **Adjacent settings.** Restriction over finite fields, for fractal measures, for the cone and for degenerate surfaces continue to serve as testbeds where the full conjecture is provable.

## 8. Future Work

- Prove a quantitative Kakeya *maximal* estimate in $\mathbb{R}^3$ with $R^{\varepsilon}$ loss, then attempt a direct transfer to restriction (Tao's long-stated route).
- Develop a structure theorem classifying near-extremal wave-packet configurations up to plane, cone and $SL_2$ types, and prove a strict gain for each type.
- Find the endpoint version at $p=\frac{2d}{d-1}$ with $q$ restrictions, or show the endpoint fails — currently unknown even conditionally.
- Establish restriction for the paraboloid in $\mathbb{R}^3$ conditional on the full Kakeya maximal conjecture — a clean implication that is still not available.
- Exhibit a new counterexample family: any surface beating the Knapp/focusing pair would reshape the conjectured range.

## 9. Key References

- **[Foundational]** C. Fefferman. *Inequalities for strongly singular convolution operators.* Acta Mathematica 124 (1970), 9–36.
- **[Foundational]** C. Fefferman. *The multiplier problem for the ball.* Annals of Mathematics 94 (1971), 330–336.
- **[Foundational]** P. A. Tomas. *A restriction theorem for the Fourier transform.* Bulletin of the AMS 81 (1975), 477–478.
- **[Foundational]** A. Zygmund. *On Fourier coefficients and transforms of functions of two variables.* Studia Mathematica 50 (1974), 189–201.
- **[Foundational]** E. M. Stein. *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals.* Princeton University Press, 1993.
- **[Milestone]** J. Bourgain. *Besicovitch type maximal operators and applications to Fourier analysis.* GAFA 1 (1991), 147–187.
- **[Milestone]** T. Wolff. *A sharp bilinear cone restriction estimate.* Annals of Mathematics 153 (2001), 661–698.
- **[Milestone]** T. Tao. *A sharp bilinear restriction estimate for paraboloids.* GAFA 13 (2003), 1359–1384.
- **[Milestone]** J. Bennett, A. Carbery, T. Tao. *On the multilinear restriction and Kakeya conjectures.* Acta Mathematica 196 (2006), 261–302.
- **[Milestone]** J. Bourgain, L. Guth. *Bounds on oscillatory integral operators based on multilinear estimates.* GAFA 21 (2011), 1239–1295.
- **[SOTA]** L. Guth. *A restriction estimate using polynomial partitioning.* Journal of the AMS 29 (2016), 371–413.
- **[SOTA]** L. Guth. *Restriction estimates using polynomial partitioning II.* Acta Mathematica 221 (2018), 81–142.
- **[SOTA]** J. Hickman, K. M. Rogers. *Improved Fourier restriction estimates in higher dimensions.* Cambridge Journal of Mathematics 7 (2019), 219–282.
- **[SOTA]** H. Wang. *A restriction estimate in $\mathbb{R}^3$ using brooms.* Duke Mathematical Journal 171 (2022), 1749–1822.
- **[SOTA]** H. Wang, J. Zahl. *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions.* arXiv:2502.17655, 2025.
- **[Survey]** T. Tao. *Some recent progress on the restriction conjecture.* In *Fourier Analysis and Convexity*, Birkhäuser, 2004, 217–243.
- **[Survey]** C. Demeter. *Fourier Restriction, Decoupling, and Applications.* Cambridge Studies in Advanced Mathematics 184, Cambridge University Press, 2020.
- **[Survey]** B. Stovall. *Waves, spheres, and tubes: a selection of Fourier restriction problems, methods, and applications.* Notices of the AMS 66 (2019), 1013–1022.

## 10. Worked Example / Concrete Special Case

**Both necessary conditions, computed in $d=3$.**

*(a) Focusing example — forces $p>\frac{2d}{d-1}=3$.* Take $f\equiv 1$ on $S^2$, so $\|f\|_{L^\infty}=1$ and $Ef=\widehat{d\sigma}$. By stationary phase,
$$
\widehat{d\sigma}(x)=2|x|^{-1}\cos\!\big(2\pi|x|-\tfrac{\pi}{2}\big)+O(|x|^{-2}) .
$$
On each spherical shell $\{|x|\in[n+\tfrac18,n+\tfrac38]\}$ the cosine has modulus $\gtrsim 1$, so $|\widehat{d\sigma}(x)|\gtrsim |x|^{-1}$ there. Hence
$$
\int_{|x|\ge1}|\widehat{d\sigma}|^p\,dx \;\gtrsim\; \sum_{n\ge1} n^{-p}\cdot n^{2} \;=\;\sum_{n\ge1} n^{2-p},
$$
which diverges for $p\le 3$. So $p>3$ is necessary — and it is exactly the conjectured threshold. In general $d$: $\int |x|^{-p(d-1)/2}dx<\infty$ near infinity iff $p>\frac{2d}{d-1}$.

*(b) Knapp example — forces the $q$-condition.* Let $\kappa\subset S^{2}$ be a cap of angular radius $\delta$, $f=\mathbf 1_\kappa$, so $\|f\|_{L^q(d\sigma)}=\sigma(\kappa)^{1/q}\approx\delta^{2/q}$ and $\sigma(\kappa)\approx\delta^{2}$. For $\xi\in\kappa$ and $x$ in the dual slab
$$
T_\delta=\{x: |x\cdot e|\le c\delta^{-2},\ |x\cdot e^\perp|\le c\delta^{-1}\},\qquad |T_\delta|\approx \delta^{-4}=\delta^{-(d+1)},
$$
the phase $2\pi x\cdot\xi$ varies by less than $1/10$, so $|Ef|\gtrsim\sigma(\kappa)\approx\delta^{2}$ on $T_\delta$. Therefore
$$
\|Ef\|_{L^p}\;\gtrsim\;\delta^{2}\cdot\delta^{-4/p},\qquad
\frac{\|Ef\|_p}{\|f\|_q}\;\gtrsim\;\delta^{\,2-\frac4p-\frac2q}.
$$
Boundedness as $\delta\to0$ forces $2-\frac4p-\frac2q\ge0$, i.e. $\frac{4}{p}\le 2-\frac2q=\frac{2}{q'}\cdot\! $ — rearranged, $\frac{d+1}{p}\le\frac{d-1}{q'}$ with $d=3$.

*(c) What is actually proven here.* For $q=2$, condition (b) reads $p\ge 4=\frac{2(d+1)}{d-1}$, and Stein–Tomas delivers exactly that. For $q=\infty$, condition (b) reads $p\ge 2$, so (a) is binding and the target is $p>3$; the best theorem gives $p>3+\frac3{13}\approx 3.2308$. The gap between $3$ and $3.2308$ is the entire content of the open problem in $\mathbb{R}^3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*