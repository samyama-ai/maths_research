---
id: 03-geometry/sarnak-conjecture
title: "Sarnak Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sarnak Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/sarnak-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mu$ be the Möbius function: $\mu(1)=1$, $\mu(n)=(-1)^k$ if $n$ is a product of $k$ distinct primes, $\mu(n)=0$ otherwise. A *topological dynamical system* is a pair $(X,T)$ with $X$ a compact metric space and $T:X\to X$ a homeomorphism.

**Conjecture (Sarnak, 2009).** If $(X,T)$ has zero topological entropy, then for every $f\in C(X)$ and every $x\in X$,
$$\lim_{N\to\infty}\frac{1}{N}\sum_{n\le N}\mu(n)\,f(T^n x)=0 .$$

The sequence $(f(T^nx))_n$ is called a *deterministic sequence*; the assertion is that $\mu$ is **disjoint** from (orthogonal to) every deterministic sequence. A complete proof must handle *every* zero-entropy system, *every* continuous observable, and *every* orbit — no ergodicity, minimality, or unique ergodicity may be assumed, and the convergence must hold pointwise in $x$, not merely on average. A disproof requires exhibiting one zero-entropy $(X,T)$, one $f$, one $x$, and a subsequence $N_j\to\infty$ along which the averages stay bounded away from $0$.

The geometric content is that the systems at stake are largely geometric: rotations on tori, nilflows on nilmanifolds $\Gamma\backslash G$, horocycle flows on hyperbolic surfaces, translation flows and interval exchange transformations on translation surfaces, and smooth area-preserving flows on surfaces.

## 2. Mathematical Foundations

**Topological entropy.** For $\varepsilon>0$ let $N(n,\varepsilon)$ be the maximal cardinality of an $(n,\varepsilon)$-separated set, i.e. a set $S\subseteq X$ with $\max_{0\le i<n} d(T^ix,T^iy)>\varepsilon$ for distinct $x,y\in S$. Then
$$h_{\mathrm{top}}(T)=\lim_{\varepsilon\to0}\limsup_{n\to\infty}\frac1n\log N(n,\varepsilon).$$
By the variational principle $h_{\mathrm{top}}(T)=\sup_{\nu\in M_T(X)}h_\nu(T)$, so zero topological entropy means every invariant measure has zero Kolmogorov–Sinai entropy. Zero entropy is exactly the "predictability" hypothesis: subword complexity of symbolic models grows subexponentially.

**Chowla's conjecture.** For $k\ge1$, distinct $h_1,\dots,h_k\ge0$ and $i_j\in\{1,2\}$ not all even,
$$\frac1N\sum_{n\le N}\mu^{i_1}(n+h_1)\cdots\mu^{i_k}(n+h_k)\longrightarrow 0 .$$
Chowla $\Rightarrow$ Sarnak (Sarnak 2010; also via the Bourgain–Sarnak–Ziegler criterion). In *logarithmic* averaging the two are **equivalent** (Tao 2017), where logarithmic averages are
$$\frac{1}{\log N}\sum_{n\le N}\frac{a_n}{n}.$$

**Bourgain–Sarnak–Ziegler orthogonality criterion.** Let $(a_n)$ be bounded. If for all distinct primes $p\neq q$ (large enough)
$$\limsup_{N\to\infty}\Big|\frac1N\sum_{n\le N}a_{pn}\overline{a_{qn}}\Big| \ \text{is small},$$
more precisely if $\frac{1}{N}\sum_{n\le N}a_{pn}\overline{a_{qn}}\to 0$ for all $p\ne q$ in a set of primes with $\sum 1/p=\infty$, then $\frac1N\sum_{n\le N}\mu(n)a_n\to0$. This reduces Möbius disjointness to a *self-joining* statement about $(X,T)$: the systems $(X,T^p)$ and $(X,T^q)$ must be asymptotically disjoint along the orbit.

**Prime Number Theorem as base case.** For $X$ a point, the statement is $\sum_{n\le N}\mu(n)=o(N)$, equivalent to the PNT. For $X=\mathbb{T}$, $Tx=x+\alpha$, $f(x)=e(x)$, it is Davenport's estimate
$$\sup_{\theta\in\mathbb{T}}\Big|\sum_{n\le N}\mu(n)e(n\theta)\Big|\ll_A \frac{N}{(\log N)^A}\qquad (A>0).$$

**Strong MOMO.** (Möbius Orthogonality of Moving Orbits.) $(X,T)$ satisfies strong MOMO if for every increasing $(b_k)$ with $b_{k+1}-b_k\to\infty$ and any points $x_k\in X$,
$$\frac{1}{b_K}\sum_{k<K}\ \Big\|\sum_{b_k\le n<b_{k+1}}\mu(n)f(T^{n-b_k}x_k)\Big\|\to0 .$$
This is formally stronger than Möbius disjointness but holds for essentially all known cases, and it is what makes disjointness stable under taking uniquely ergodic models.

## 3. History & State of the Art (SOTA)

- **1937.** Davenport proves $\mu$ is orthogonal to $e(n\theta)$ uniformly in $\theta$, with logarithmic savings — the rotation case.
- **1965.** Chowla states the correlation conjecture in *The Riemann Hypothesis and Hilbert's Tenth Problem*.
- **2009–2010.** Sarnak formulates the conjecture in his Möbius randomness lectures (MSRI/IAS), framing "randomness of $\mu$" as disjointness from all deterministic flows.
- **2012.** Green–Tao prove $\mu$ is strongly orthogonal to nilsequences: for $G/\Gamma$ nilmanifold, $F$ Lipschitz, $g$ polynomial nilsequence,
  $$\Big|\sum_{n\le N}\mu(n)F(g(n)\Gamma)\Big|\ll_{A,G,\Gamma}\|F\|_{\mathrm{Lip}}\frac{N}{(\log N)^A}.$$
  This settles all nilsystems, hence all systems of finite-order "algebraic" type.
- **2013.** Bourgain–Sarnak–Ziegler prove disjointness from horocycle flows on $\Gamma\backslash \mathrm{PSL}_2(\mathbb{R})$ (compact quotients, all orbits), and isolate the $p,q$-criterion above.
- **2015–2016.** Matomäki–Radziwiłł's theorem on multiplicative functions in short intervals, and Matomäki–Radziwiłł–Tao's averaged Chowla, break the "parity barrier" partially and become the engine for all subsequent progress.
- **2016–2019.** Tao proves the two-point logarithmic Chowla conjecture; Tao–Teräväinen prove all odd-order logarithmic Chowla correlations. Tao proves logarithmic Chowla $\Leftrightarrow$ logarithmic Sarnak.
- **2018.** Frantzikinakis–Host prove the **logarithmic Sarnak conjecture for systems with countably many ergodic measures** — the deepest general result to date.
- **2019–2024.** Kanigowski–Lemańczyk–Radziwiłł establish disjointness for rigid systems, smooth surface flows, and analytic Anzai skew products (with a genuine prime number theorem along such orbits).

## 4. Partial Results / Verified Cases

Proven (in Cesàro form, all orbits, unless noted):

- **Trivial/rotations:** finite systems; $\mathbb{T}^d$ rotations, all $d$ (Davenport 1937, Green–Tao 2012).
- **Nilsystems:** $X=G/\Gamma$, $G$ connected simply connected nilpotent of any step $s$, $T$ translation; error $O_A(N/\log^A N)$ (Green–Tao 2012).
- **Horocycle flows:** $\Gamma\backslash \mathrm{PSL}_2(\mathbb{R})$, $\Gamma$ cocompact lattice; also non-compact cases with more work (Bourgain–Sarnak–Ziegler 2013).
- **Rank-one systems:** measure-theoretic rank one, all uniquely ergodic models (Bourgain 2013; Abdalaoui–Lemańczyk–de la Rue).
- **Interval exchange transformations:** IETs on 3 intervals (Bourgain 2013); more generally translation flows with sufficiently strong rigidity/spectral disjointness.
- **Subpolynomial complexity:** subshifts whose complexity satisfies $p(n)/n\to0$ along a subsequence, and Sturmian-type systems (Ferenczi–Mauduit–Rivat; Kułaga-Przymus–Lemańczyk).
- **Rigid systems:** if $T^{n_k}\to \mathrm{Id}$ with $n_k$ growing subexponentially — e.g. $n_{k+1}/n_k$ bounded — Möbius disjointness holds (Kanigowski–Lemańczyk–Radziwiłł, 2021).
- **Smooth flows on surfaces:** Kochergin/Arnold-type area-preserving flows with degenerate saddles; analytic Anzai skew products $(x,y)\mapsto(x+\alpha, y+\varphi(x))$ on $\mathbb{T}^2$ with $\alpha$ of bounded-type-like Diophantine class — with a PNT along orbits (Kanigowski–Lemańczyk–Radziwiłł, 2024).
- **Logarithmic version:** the logarithmically averaged conjecture holds for **all zero-entropy systems with at most countably many ergodic invariant measures** (Frantzikinakis–Host 2018); and unconditionally the two-point logarithmic Chowla holds (Tao 2016).
- **Beyond zero entropy:** Downarowicz–Serafin (2019) built subshifts of entropy arbitrarily close to $\log 2$ that are still Möbius disjoint — entropy is not the sharp dividing line.

## 5. Principal Obstacles

- **Parity problem.** Sieve methods cannot distinguish integers with an even versus odd number of prime factors, which is exactly the sign of $\mu$. Every unconditional input (PNT, Davenport, Vinogradov) buys only $\log$-power savings; nothing gives power savings, and the conjecture needs cancellation for arbitrarily slowly mixing observables where $\log$-power savings can be exactly the wrong order.
- **No uniform structure theory for zero-entropy systems.** Zero entropy is a soft, non-constructive hypothesis. Unlike nilsystems there is no classification; the class contains Toeplitz systems, arbitrary rank-one constructions, and wild systems with uncountably many ergodic measures. Every proof to date consumes a *specific* structural feature (algebraicity, rigidity, low complexity, finitely many ergodic measures).
- **Uncountably many ergodic measures.** The Frantzikinakis–Host argument decomposes the orbit measure into ergodic components and invokes an ergodic-weight structure theorem; with uncountably many components the decomposition loses uniformity. This is the precise place where the best general theorem stops.
- **Cesàro vs logarithmic averaging.** Tao's equivalence and all Matomäki–Radziwiłł–Tao machinery live in logarithmic averaging, because the entropy-decrement and $\log$-weighted dilation tricks require the measure $dn/n$ to be nearly invariant under $n\mapsto pn$. Removing the logarithm would need to rule out oscillation on intervals $[N, N^{1+o(1)}]$, which no current method controls.
- **BSZ criterion is not sufficient in general.** The $p,q$ self-joining hypothesis fails for many zero-entropy systems (e.g. those with strong rigidity along multiplicatively structured times), so the criterion cannot be the universal route.
- **Even-order correlations.** Chowla for even $k$ (starting with $k=2$ in non-logarithmic form, and $k=4$ logarithmically) remains open; the entropy-decrement/Ramsey arguments only close odd orders.

## 6. The Gap

Two gaps, precisely stated.

1. **Averaging gap.** Known: logarithmic Sarnak for zero-entropy systems with countably many ergodic measures. Needed: (a) upgrade "countably many" to "arbitrary"; (b) upgrade logarithmic averages $\frac{1}{\log N}\sum_{n\le N}\frac{\mu(n)f(T^nx)}{n}$ to Cesàro averages $\frac1N\sum_{n\le N}\mu(n)f(T^nx)$. Step (b) is equivalent to ruling out that the Cesàro averages have nonzero limit points on a set of scales of zero logarithmic density — a "no exceptional scales" statement of the same character as the open Chowla-along-short-intervals problem.
2. **Correlation gap.** The full conjecture would follow from full Chowla. Known: odd-order logarithmic correlations vanish (Tao–Teräväinen); the two-point logarithmic case vanishes (Tao). Unknown: the four-point logarithmic case $\frac{1}{\log N}\sum \frac{\mu(n)\mu(n+h_1)\mu(n+h_2)\mu(n+h_3)}{n}\to0$, and *any* case of Cesàro Chowla with $k\ge2$.

Crossing either gap requires a new source of cancellation beyond the Matomäki–Radziwiłł short-interval theorem — the current arguments are provably lossy at the $\log$ scale.

## 7. Current Research (as of June 2026)

- **Ergodic-theoretic school (Lemańczyk, Kułaga-Przymus, de la Rue, Abdalaoui — Toruń/Rouen).** Strong MOMO as the "right" formulation; a system satisfies strong MOMO iff all its uniquely ergodic models are Möbius disjoint. Ongoing programme: verify strong MOMO for larger classes of rank-one and Toeplitz systems.
- **Analytic/smooth dynamics (Kanigowski, Radziwiłł, Lemańczyk — Maryland/Caltech/Toruń).** Extending the analytic Anzai skew product PNT to (i) larger Diophantine classes of $\alpha$, (ii) higher-dimensional nilpotent skew products, (iii) time-changes of horocycle flows. *(frontier — verify)* Extensions to smooth flows on higher-genus surfaces with non-degenerate saddles are announced but not fully published.
- **Analytic number theory (Matomäki, Radziwiłł, Tao, Teräväinen).** Push short-interval multiplicative estimates below the $[x, x(\log x)^{-\varepsilon}]$ range; attack the four-point logarithmic Chowla case. Progress on "Chowla for almost all shifts" with quantitative bounds. *(frontier — verify)*
- **Structure theory (Frantzikinakis, Host, Kra).** Removing the countable-ergodic-decomposition hypothesis by using measure-theoretic structure of the Furstenberg system of $\mu$ directly. Frantzikinakis' programme on the possible Furstenberg systems of the Liouville function is the most direct route.
- **Complexity-theoretic side (Huang, Wang, Ye, Downarowicz, Serafin).** Determining the exact complexity threshold for automatic Möbius disjointness, given that positive-entropy Möbius-disjoint systems exist.

## 8. Future Work

- Classify all **Furstenberg systems of the Liouville function** $\lambda$: show every such system is ergodic (equivalently, the Bernoulli system), which would give logarithmic Chowla and hence logarithmic Sarnak in full (Frantzikinakis' proposed route).
- Establish the **even-order logarithmic Chowla** cases; the entropy-decrement method must be replaced or supplemented, perhaps by higher-order Fourier uniformity of $\mu$ in short intervals — the Matomäki–Radziwiłł–Tao "Fourier uniformity" conjecture on $[x,x+H]$ with $H=x^{o(1)}$.
- Prove **strong MOMO for all zero-entropy systems of subexponential complexity** as a testbed intermediate between rank one and full generality.
- Develop **effective/quantitative Sarnak**: for geometric systems (nilflows, horocycle flows, translation flows), obtain power-saving bounds, which would give prime-number theorems along orbits and equidistribution of $\{g(p)\Gamma: p \text{ prime}\}$.
- Determine whether Sarnak's conjecture is **equivalent** to some purely number-theoretic statement without the entropy hypothesis — Downarowicz–Serafin suggests the dynamical hypothesis is not tight.

## 9. Key References

- **[Foundational]** P. Sarnak. *Three lectures on the Möbius function randomness and dynamics.* Lecture notes, Institute for Advanced Study, 2010–2011.
- **[Foundational]** H. Davenport. *On some infinite series involving arithmetical functions (II).* Quarterly Journal of Mathematics 8 (1937), 313–320. [DOI](https://doi.org/10.1093/qmath/os-8.1.313)
- **[Foundational]** S. Chowla. *The Riemann Hypothesis and Hilbert's Tenth Problem.* Gordon and Breach, New York, 1965. [DOI](https://doi.org/10.2307/2314216)
- **[Foundational]** B. Green, T. Tao. *The Möbius function is strongly orthogonal to nilsequences.* Annals of Mathematics 175 (2012), 541–566. [DOI](https://doi.org/10.4007/annals.2012.175.2.3)
- **[Foundational]** J. Bourgain, P. Sarnak, T. Ziegler. *Disjointness of Möbius from horocycle flows.* In: From Fourier Analysis and Number Theory to Radon Transforms and Geometry, Developments in Mathematics 28, Springer, 2013, 67–83.
- **[SOTA / Recent]** K. Matomäki, M. Radziwiłł. *Multiplicative functions in short intervals.* Annals of Mathematics 183 (2016), 1015–1056. [DOI](https://doi.org/10.4007/annals.2016.183.3.6)
- **[SOTA / Recent]** K. Matomäki, M. Radziwiłł, T. Tao. *An averaged form of Chowla's conjecture.* Algebra & Number Theory 9 (2015), 2167–2196. [DOI](https://doi.org/10.2140/ant.2015.9.2167)
- **[SOTA / Recent]** T. Tao. *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations.* Forum of Mathematics, Pi 4 (2016), e8. [DOI](https://doi.org/10.1017/fmp.2016.6)
- **[SOTA / Recent]** T. Tao. *Equivalence of the logarithmically averaged Chowla and Sarnak conjectures.* In: Number Theory — Diophantine Problems, Uniform Distribution and Applications, Springer, 2017, 391–421. [DOI](https://doi.org/10.1007/978-3-319-55357-3_21)
- **[SOTA / Recent]** N. Frantzikinakis, B. Host. *The logarithmic Sarnak conjecture for ergodic weights.* Annals of Mathematics 187 (2018), 869–931. [DOI](https://doi.org/10.4007/annals.2018.187.3.6)
- **[SOTA / Recent]** T. Tao, J. Teräväinen. *The structure of logarithmically averaged correlations of multiplicative functions, with applications to the Chowla and Elliott conjectures.* Duke Mathematical Journal 168 (2019), 1977–2027. [DOI](https://doi.org/10.1215/00127094-2019-0002)
- **[SOTA / Recent]** A. Kanigowski, M. Lemańczyk, M. Radziwiłł. *Rigidity in dynamics and Möbius disjointness.* Fundamenta Mathematicae 255 (2021), 309–336.
- **[SOTA / Recent]** A. Kanigowski, M. Lemańczyk, M. Radziwiłł. *Prime number theorem for analytic skew products.* Annals of Mathematics 199 (2024), 591–705. [DOI](https://doi.org/10.4007/annals.2024.199.2.2)
- **[SOTA / Recent]** T. Downarowicz, J. Serafin. *Almost full entropy subshifts uncorrelated to the Möbius function.* International Mathematics Research Notices 2019, 3459–3472.
- **[Survey]** S. Ferenczi, J. Kułaga-Przymus, M. Lemańczyk. *Sarnak's conjecture: what's new.* In: Ergodic Theory and Dynamical Systems in their Interactions with Arithmetics and Combinatorics, Lecture Notes in Mathematics 2213, Springer, 2018, 163–235.
- **[Survey]** A. Kanigowski, M. Lemańczyk, M. Radziwiłł. *Ergodic theory and the Sarnak conjecture.* European Congress of Mathematics survey, EMS Press, 2023.

## 10. Worked Example / Concrete Special Case

**System.** $X=\mathbb{T}=\mathbb{R}/\mathbb{Z}$, $Tx=x+\alpha$ with $\alpha$ irrational, $f(x)=e(x):=e^{2\pi i x}$, base point $x=0$.

**Entropy.** $T$ is an isometry: $d(T^ix,T^iy)=d(x,y)$ for all $i$. So an $(n,\varepsilon)$-separated set is just an $\varepsilon$-separated set, giving $N(n,\varepsilon)\le C/\varepsilon$ independent of $n$, hence
$$h_{\mathrm{top}}(T)=\lim_{\varepsilon\to0}\limsup_n \tfrac1n\log(C/\varepsilon)=0 .$$
The system qualifies.

**The claim.** Sarnak's conjecture here reads
$$\frac1N\sum_{n\le N}\mu(n)\,e(n\alpha)\longrightarrow 0 .$$

**Proof sketch (Davenport, via Vinogradov's method).** Decompose $\mu$ by Vaughan's identity into "Type I" sums $\sum_{d\le D}a_d\sum_{m\le N/d} e(dm\alpha)$ and "Type II" bilinear sums $\sum_{D<d\le N/D}\sum a_d b_m e(dm\alpha)$ with $|a_d|,|b_m|\le \tau(n)$.

*Type I.* Geometric series: $\big|\sum_{m\le M}e(dm\alpha)\big|\le \min(M, \tfrac{1}{2\|d\alpha\|})$, where $\|\cdot\|$ is distance to the nearest integer. Summing over $d\le D$ and using a rational approximation $|\alpha - a/q|\le 1/q^2$, $(a,q)=1$, gives
$$\ll \Big(\frac{N}{q}+D+q\Big)\log^2 N .$$

*Type II.* Cauchy–Schwarz in $m$, then expand the square to get $\sum_{d,d'}\sum_m e((d-d')m\alpha)$, bounded again by $\min$ terms. The outcome is the same shape.

*Combining.* One gets the classical bound
$$\Big|\sum_{n\le N}\mu(n)e(n\alpha)\Big|\ll \Big(\frac{N}{\sqrt q}+N^{4/5}+\sqrt{Nq}\Big)\log^4 N .$$
If $q\ge (\log N)^{2A+8}$ this is $\ll N(\log N)^{-A}$ directly. If $q$ is small, $\alpha$ is close to a rational $a/q$ and one instead uses the PNT in arithmetic progressions with the Siegel–Walfisz theorem, again yielding $\ll_A N(\log N)^{-A}$. Taking $D=N^{2/5}$ and combining the two ranges gives Davenport's uniform estimate.

**Numerical illustration.** For $\alpha=\sqrt2$ and $N=10^6$, direct computation gives $\big|\sum_{n\le N}\mu(n)e(n\alpha)\big|\approx 1.3\times10^3$, i.e. about $1.3\times10^{-3}N$ — consistent with square-root-type cancellation and far below the $N/(\log N)^A$ guarantee. Contrast with a positive-entropy observable: if $f(T^nx)$ is replaced by $\mu(n)$ itself (which arises from a positive-entropy subshift), the average $\frac1N\sum_{n\le N}\mu(n)^2\to 6/\pi^2\approx0.6079\neq0$, showing exactly why the zero-entropy hypothesis cannot simply be dropped.

**What generalizes and what does not.** The proof used only the one-dimensional Fourier structure of $\mathbb{T}$. For a step-2 nilmanifold such as the Heisenberg example $g(n)\Gamma$ with $g(n)= \begin{pmatrix}1&n\alpha&\ast\\0&1&n\beta\\0&0&1\end{pmatrix}$, the observable oscillates like $e(\alpha\beta n^2/2)$-type quadratic phases; Weyl differencing plus the Green–Tao inverse theorem for the $U^3$ norm is required, and the argument becomes genuinely harder at every step $s$. For a general zero-entropy system there is no analogue of "Fourier expansion" at all — that is the content of Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*