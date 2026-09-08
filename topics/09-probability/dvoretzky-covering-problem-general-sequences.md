---
id: 09-probability/dvoretzky-covering-problem-general-sequences
title: "Dvoretzky's Covering Problem for General Sequences"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dvoretzky's Covering Problem for General Sequences

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/dvoretzky-covering-problem-general-sequences` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{T}=\mathbb{R}/\mathbb{Z}$ and let $(\ell_n)_{n\ge1}\subset(0,1)$ be a deterministic sequence. Place arcs
$$I_n=\big(\omega_n,\ \omega_n+\ell_n\big)\pmod 1,\qquad \omega_1,\omega_2,\dots \ \text{i.i.d. uniform on }\mathbb{T}.$$
**Dvoretzky's covering problem** asks for a necessary and sufficient condition on $(\ell_n)$ for
$$\mathbb{P}\Big(\limsup_{n\to\infty} I_n=\mathbb{T}\Big)=1,$$
i.e. for *every* point of the circle to lie in infinitely many arcs, almost surely.

For arcs on $\mathbb{T}$ this is settled (Shepp, 1972). The open problem — the "general sequences" form — is the same question when the sequence of random sets is no longer a monotone sequence of arcs driven by uniform i.i.d. translations. Three inequivalent generalizations are all open:

- **(G1) General shapes / dimension $d\ge2$.** Given measurable $A_n\subset\mathbb{T}^d$ with $\lambda_d(A_n)\to0$, characterize when $\limsup_n(\omega_n+A_n)=\mathbb{T}^d$ a.s. Even for $A_n$ axis-parallel rectangles with independently varying aspect ratios (Kahane's *random rectangles* problem), no criterion is known.
- **(G2) General translation laws.** Replace the uniform law by an arbitrary Borel probability measure $\mu$ on $\mathbb{T}$ with $\omega_n\sim\mu$ i.i.d.; characterize covering in terms of $(\ell_n)$ and the local structure of $\mu$.
- **(G3) Deterministic / dynamical translation sequences.** Given a deterministic sequence $(x_n)\subset\mathbb{T}$ (e.g. $x_n=n\alpha$, or $x_n=T^n x$ for a hyperbolic map $T$), characterize when $\limsup_n(x_n+I_n)=\mathbb{T}$, or has full Lebesgue measure.

A complete solution means an explicit, checkable condition on the data — a convergence/divergence test of Shepp type — together with a proof that it is both necessary and sufficient. A disproof of the expected form would be a construction showing that no condition depending only on the volumes $\lambda_d(A_n)$ can decide covering.

## 2. Mathematical Foundations

**Covered and uncovered sets.** Write $E=\limsup_n(\omega_n+A_n)=\bigcap_{N\ge1}\bigcup_{n\ge N}(\omega_n+A_n)$ and $U=\mathbb{T}^d\setminus E$. By Fubini and independence, for fixed $t$,
$$\mathbb{P}(t\in E)=1\iff\sum_{n\ge1}\lambda_d(A_n)=\infty,$$
by the second Borel–Cantelli lemma. Hence $\sum_n\lambda_d(A_n)=\infty$ is necessary for covering and gives $\lambda_d(U)=0$ a.s.; but $U$ may be a nonempty set of Hausdorff dimension up to $d$. The whole difficulty is the passage from *almost every point* to *every point*.

**Kolmogorov zero–one law.** $\{E=\mathbb{T}^d\}$ is a tail event in $(\omega_n)$, so its probability is $0$ or $1$. The event is also invariant under permutations of the index set, since "belonging to infinitely many $A_n$" does not depend on the ordering.

**Shepp's criterion (arcs on $\mathbb{T}$).** If $\ell_1\ge\ell_2\ge\cdots$, then $\mathbb{P}(E=\mathbb{T})=1$ if and only if
$$\sum_{n=1}^{\infty}\frac{1}{n^{2}}\exp\big(\ell_1+\ell_2+\cdots+\ell_n\big)=\infty. \tag{S}$$
Equivalently, in Mandelbrot's Poissonian model with intensity $\mathrm d\mu(\ell)$ on $(0,1)$ and $L(x)=\int_x^1\ell\,\mathrm d\mu(\ell)$, covering holds iff $\int_0^1 x^{-2}e^{L(x)}\,\mathrm dx=\infty$.

**Why (S) is not a first-moment statement.** The expected uncovered measure is
$$\mathbb{E}\,\lambda\big(\mathbb{T}\setminus\textstyle\bigcup_{n\le N}I_n\big)=\prod_{n\le N}(1-\ell_n)\longrightarrow0 \quad\text{whenever }\sum\ell_n=\infty,$$
so the first moment never distinguishes covering from non-covering. Shepp's proof runs through the exact distribution of the vacancy of a stationary interval-covering process and a renewal/Laplace-transform identity, whose one-dimensional order structure is essential.

**Dimension of the uncovered set.** For $\ell_n=a/n$ with $0<a<1$,
$$\dim_{\mathrm H}U=1-a\quad\text{a.s.},$$
and $U$ is a set with large intersection in Falconer's sense.

**Higher dimension.** For $N$ i.i.d. uniform translates of $aK$ ($K$ a fixed convex body, $\lambda_d(aK)=a\to0$) in $\mathbb{T}^d$, Janson determined the covering threshold:
$$N a=\log\tfrac1a+d\log\log\tfrac1a+C(K)+o(1),$$
with $C(K)$ explicit in the shape $K$. This is a *fixed-shape, equal-size* result; it does not yield a Shepp-type series test for a general sequence $(A_n)$ of varying shapes.

## 3. History & State of the Art (SOTA)

- **1956.** A. Dvoretzky poses the problem in PNAS, observing that $\sum\ell_n=\infty$ is not sufficient: he constructs divergent $(\ell_n)$ for which $U\neq\emptyset$ a.s.
- **1956–1959.** Kahane, and independently Erdős-inspired work, treat $\ell_n=a/n$: covering for $a>1$, non-covering for $a<1$; the critical case $a=1$ resists.
- **1972.** L. Shepp proves (S), settling the decreasing-arc case on $\mathbb{T}$ completely, including $a=1$ (covering). Mandelbrot's Poissonian reformulation appears the same year and confirms an Erdős conjecture.
- **1978–1990.** El Hélou, and Kahane's *Some Random Series of Functions* (Ch. 11), give sufficient conditions and potential-theoretic reformulations on $\mathbb{T}^d$; the necessary-and-sufficient problem in $d\ge2$ is stated as open.
- **1986.** Janson's *Acta Mathematica* paper gives sharp asymptotics for covering $\mathbb{T}^d$ (and manifolds) by many small copies of a fixed shape, plus general sufficient conditions.
- **2000s–2020s.** Fan–Wu give a short proof of (S); Barral–Fan analyse covering multiplicities; Durand computes the multifractal/large-intersection structure of $U$; Jonasson–Steif study dynamical (time-evolving) versions; Feng–Järvenpää–Järvenpää–Suomala and Ekström–Persson compute Hausdorff dimensions of random limsup sets on manifolds and for general measures.

## 4. Partial Results / Verified Cases

- **Arcs on $\mathbb{T}$, all sequences.** Solved. If $\ell_n\not\to0$ then infinitely many arcs have length $\ge\varepsilon$ and covering is immediate. If $\ell_n\to0$, permutation invariance lets one pass to the decreasing rearrangement $(\ell_n^{*})$ and apply (S). So $d=1$ with arcs is closed; the "general sequence" difficulty is genuinely about shape, dimension, and non-uniform placement.
- **Power scales.** $\ell_n=a/n$: covering iff $a\ge1$. $\ell_n=n^{-1}(\log n)^{-b}$: (S) gives covering iff $b\le0$; more finely, $\ell_n=n^{-1}+c\,n^{-1}(\log n)^{-1}$ covers iff $c\ge1$.
- **$\mathbb{T}^d$, balls of equal size, $N\to\infty$.** Janson's threshold above; also complete for a fixed convex shape with sizes decreasing regularly.
- **$\mathbb{T}^d$, sufficient conditions.** Shepp-type sufficient series criteria (El Hélou, Kahane, Janson) are known for balls with $r_n$ decreasing; they are not known to be necessary.
- **Dimension results.** $\dim_{\mathrm H}U$ is known for balls in $\mathbb{T}^d$ and for affine/self-similar shapes with fixed orientation (Järvenpää–Järvenpää–Koivusalo–Li–Suomala), and for i.i.d. non-uniform centres under a Frostman condition on $\mu$ (Ekström–Persson).
- **(G3), full-measure version, $x_n=n\alpha$.** Kurzweil's theorem (1955): $\limsup_n(n\alpha+I_n)$ has full measure for *every* sequence with $\sum\ell_n=\infty$ if and only if $\alpha$ is badly approximable. Everywhere-covering fails for all irrational $\alpha$ when $\ell_n\to0$ fast enough.
- **(G3), hyperbolic dynamics.** For Gibbs measures under expanding maps, Fan–Schmeling–Troubetzkoy establish a mass transference / multifractal principle giving the size of dynamical $\limsup$ sets, though not an exact covering criterion.

## 5. Principal Obstacles

- **No order structure in $d\ge2$.** Shepp's proof and Fan–Wu's simplification both exploit that the complement of finitely many arcs is a union of intervals whose lengths form a tractable renewal-type Markov chain. In $\mathbb{T}^d$ the vacant set has no such one-dimensional decomposition; its combinatorics (number of components, boundary structure) is itself an open problem.
- **Shape-dependence.** Covering is not a function of volumes alone once shapes vary: long thin rectangles cover "directionally", and Janson's constant $C(K)$ already shows shape enters at the critical scale. Any purely volumetric series test is therefore doomed for (G1); what replaces it is unknown.
- **Second-moment methods are too weak.** The first moment is uninformative (Section 2), and Paley–Zygmund/second-moment arguments give full measure of $E$, not $E=\mathbb{T}^d$. Covering everywhere is a $\Pi^0_2$ statement whose failure is caused by rare, highly correlated vacancy events.
- **Potential theory saturates.** Kahane's reformulation converts covering into the non-existence of a probability measure of finite energy on $U$ against a kernel built from $(\ell_n)$. The kernel is explicit only when the shapes are balls with a regular scale; for irregular sequences the kernel is not comparable to any Riesz kernel.
- **Non-uniform $\mu$ destroys stationarity.** For (G2), the placement process is no longer translation invariant, so the vacancy process is inhomogeneous; local scaling exponents of $\mu$ vary from point to point, so a single scalar series cannot capture covering.

## 6. The Gap

Proven: an exact criterion (S) in the *one-dimensional, arc, uniform i.i.d.* case, plus sharp asymptotics in $\mathbb{T}^d$ for a *single fixed shape at a single scale*. Wanted: a criterion for a *sequence of shapes across scales* in $d\ge2$, and for non-uniform or deterministic placements.

The precise barrier: find the correct replacement for the factor $n^{-2}e^{L_n}$ in (S). In $d=1$ this factor is the probability that a specific gap survives, computable from a renewal identity. In $d\ge2$ the analogous quantity is the probability that the vacant set contains a point after $n$ sets — governed by an extremal, shape-dependent capacity of the family $\{A_k\}_{k\le n}$ that has no closed form. Bridging the gap requires either (i) a Shepp-type exact vacancy identity in $\mathbb{T}^d$, or (ii) a proof that the natural potential-theoretic sufficient condition is also necessary, or (iii) an explicit counterexample showing covering depends on data finer than any capacity of the individual sets.

## 7. Current Research (as of June 2026)

- **Random limsup sets and dimension.** Groups in Jyväskylä and Oulu (Järvenpää, Järvenpää, Suomala, Koivusalo) and in Lund/Uppsala (Persson, Ekström) continue to compute $\dim_{\mathrm H}U$ for affine and rotating shapes, non-uniform measures, and Riemannian manifolds; the rotation-averaged case is markedly better understood than the fixed-orientation case.
- **Dynamical covering / shrinking targets.** Fan, Schmeling, Troubetzkoy and successors push mass-transference principles for Gibbs and non-conformal systems; the analogue of Kurzweil's theorem for general uniquely ergodic systems remains partly open. *(frontier — verify)*
- **Rectangles and anisotropy.** Kahane's random-rectangles question is being attacked with multiscale/percolation-flavoured arguments; sharp criteria in the "thin rectangle" regime are claimed only under regularity assumptions on the aspect ratios. *(frontier — verify)*
- **Dynamical (time-evolving) coverings.** Following Jonasson–Steif, exceptional-times phenomena for critical sequences ($a=1$) are studied with noise-sensitivity tools.
- **Quantitative Borel–Cantelli.** Connections to the (now proved) Duffin–Schaeffer conjecture of Koukoulopoulos–Maynard have renewed interest in transferring GCD-graph techniques to covering problems with deterministic centres. *(frontier — verify)*

## 8. Future Work

- Prove or refute that for balls in $\mathbb{T}^d$ with $r_n$ decreasing, the natural series test
$\sum_n n^{-2}\exp\big(c_d\sum_{k\le n}r_k^{d}\,\cdot\,\Phi(n)\big)=\infty$ (for the right normalisation $\Phi$) is necessary as well as sufficient.
- Develop an exact vacancy identity in $\mathbb{T}^2$ for random rectangles, or show that vacancy exhibits a genuinely two-dimensional (non-renewal) obstruction.
- Characterize the measures $\mu$ for which covering by arcs with i.i.d. $\mu$-centres is decided by $\sum\ell_n^{\,s}$ for the correlation dimension $s$ of $\mu$.
- Extend Kurzweil's badly-approximable characterization to everywhere-covering, and to sequences $x_n=T^nx$ for hyperbolic $T$.
- Build a systematic library of counterexample sequences (in the spirit of Dvoretzky's original construction) that separate candidate criteria in $d\ge2$.

## 9. Key References

- **[Foundational]** A. Dvoretzky. *On covering a circle by randomly placed arcs.* Proceedings of the National Academy of Sciences USA **42** (1956), 199–203.
- **[Foundational]** J.-P. Kahane. *Sur le recouvrement d'un cercle par des intervalles disposés au hasard.* C. R. Acad. Sci. Paris **248** (1959), 184–186.
- **[Foundational]** L. A. Shepp. *Covering the circle with random arcs.* Israel Journal of Mathematics **11** (1972), 328–345.
- **[Foundational]** B. B. Mandelbrot. *On Dvoretzky coverings for the circle.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete **22** (1972), 158–160.
- **[Survey]** J.-P. Kahane. *Some Random Series of Functions*, 2nd edition, Cambridge University Press, 1985 (Chapter 11).
- **[Survey]** J.-P. Kahane. *Random coverings and multiplicative processes.* In: *Fractal Geometry and Stochastics II*, Progress in Probability 46, Birkhäuser, 2000, 125–146.
- **[SOTA]** S. Janson. *Random coverings in several dimensions.* Acta Mathematica **156** (1986), 83–118.
- **[SOTA]** A.-H. Fan, J. Wu. *On the covering by small random intervals.* Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **40** (2004), 125–131.
- **[SOTA]** J. Barral, A.-H. Fan. *Covering numbers of different points in Dvoretzky covering.* Bulletin des Sciences Mathématiques **129** (2005), 275–317.
- **[SOTA]** J. Jonasson, J. E. Steif. *Dynamical models for circle covering: Brownian motion and Poisson updating.* Annals of Probability **36** (2008), 739–764.
- **[SOTA]** A.-H. Fan, J. Schmeling, S. Troubetzkoy. *A multifractal mass transference principle for Gibbs measures with applications to dynamical Diophantine approximation.* Proceedings of the London Mathematical Society **107** (2013), 1173–1219.
- **[SOTA]** E. Järvenpää, M. Järvenpää, H. Koivusalo, B. Li, V. Suomala. *Hausdorff dimension of affine random covering sets in torus.* Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **50** (2014), 1371–1384.
- **[SOTA]** D.-J. Feng, E. Järvenpää, M. Järvenpää, V. Suomala. *Dimensions of random covering sets in Riemann manifolds.* Annals of Probability **46** (2018), 1721–1744.
- **[Related]** J. Kurzweil. *On the metric theory of inhomogeneous diophantine approximation.* Studia Mathematica **15** (1955), 84–112.

## 10. Worked Example / Concrete Special Case

**Case $\ell_n=a/n$, $a>0$, arcs on $\mathbb{T}$.**

Partial sums: $L_n=\sum_{k=1}^n \frac ak=a\log n+a\gamma+O(1/n)$, so $e^{L_n}=C_a\,n^{a}\,(1+o(1))$ with $C_a=e^{a\gamma}$. Shepp's series becomes
$$\sum_{n\ge1}\frac{e^{L_n}}{n^{2}}\ \asymp\ \sum_{n\ge1} n^{a-2}.$$
This diverges iff $a-2\ge-1$, i.e. iff $a\ge1$. Conclusion: the circle is a.s. covered iff $a\ge1$; for $a<1$ the uncovered set $U$ is a.s. nonempty with $\dim_{\mathrm H}U=1-a$ and $\lambda(U)=0$.

Note that $\sum_n \ell_n=\infty$ for every $a>0$, so Borel–Cantelli alone gives $\lambda(U)=0$ for all $a$ and cannot see the transition at $a=1$. The transition is a correlation effect: gaps left by long arcs shield later short arcs.

**Refinement at $a=1$.** Take $\ell_n=\frac1n+\frac{c}{n\log n}$ for $n\ge3$. Then $L_n=\log n+c\log\log n+O(1)$, so
$$\frac{e^{L_n}}{n^{2}}\asymp \frac{(\log n)^{c}}{n},$$
and $\sum_n n^{-1}(\log n)^{c}$ diverges for every $c>-1$; at $c=-1$ it still diverges (harmonic-type $\sum 1/(n\log n)$). Covering therefore persists slightly below the $1/n$ scale, and fails only once $L_n-\log n\to-\infty$ fast enough that $\sum n^{-1}e^{L_n-\log n}<\infty$ — e.g. $\ell_n=\frac1n-\frac{2}{n\log n}$ gives $\sum_n n^{-1}(\log n)^{-2}<\infty$, hence no covering.

**Where the analogy breaks in $d=2$.** Replace arcs by discs of radius $r_n$ with $\pi r_n^2=a/n$, so the areas match the $d=1$ lengths. Every ingredient of the computation above that used the interval structure — the renewal identity for gap lengths — is unavailable, and the corresponding threshold is not known to be $a=1$ for any normalisation. Replacing the discs by $\frac{a}{n}\times 1$ rectangles keeps all areas identical, yet these rectangles are strips of full height and covering behaves like a one-dimensional problem in the horizontal coordinate. Two sequences with identical area sequences thus have different covering thresholds, which is exactly the phenomenon that any general criterion must encode.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*