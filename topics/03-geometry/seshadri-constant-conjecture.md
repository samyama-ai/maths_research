---
id: 03-geometry/seshadri-constant-conjecture
title: "Seshadri Constant Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Seshadri Constant Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/seshadri-constant-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth complex projective variety of dimension $n$, $L$ an ample line bundle on $X$, and $x \in X$. The **Seshadri constant** is
$$\varepsilon(X,L;x) \;=\; \inf_{C \ni x} \frac{L \cdot C}{\operatorname{mult}_x C},$$
the infimum over irreducible curves $C \subset X$ passing through $x$. It measures local positivity of $L$ at $x$.

Three linked open statements are collected under the name "Seshadri constant conjecture":

- **(C1) Very-general lower bound.** For every smooth projective $X$ of dimension $n$, every ample $L$, and $x \in X$ very general (outside a countable union of proper subvarieties),
$$\varepsilon(X,L;x) \;\ge\; 1.$$
Proved for $n = 2$; open for all $n \ge 3$, where the best unconditional bound is $1/n$.

- **(C2) Nagata's conjecture (multi-point case).** For $r \ge 10$ very general points $x_1,\dots,x_r \in \mathbb{P}^2$,
$$\varepsilon\big(\mathbb{P}^2, \mathcal{O}(1); x_1,\dots,x_r\big) \;=\; \frac{1}{\sqrt{r}},$$
i.e. every irreducible plane curve of degree $d$ with multiplicity $m_i$ at $x_i$ satisfies $d\sqrt{r} > \sum_i m_i$.

- **(C3) Rationality.** Is $\varepsilon(X,L;x)$ always rational for a single point $x$? No irrational single-point Seshadri constant is known, and none is known to exist.

A complete resolution means: a proof of (C1) in all dimensions (or an ample $L$ on some $X$ with $\varepsilon(L;1) < 1$), a proof of (C2) for some $r \ge 10$ that is not a perfect square (or a counterexample curve), and a decision on (C3).

## 2. Mathematical Foundations

**Blow-up formulation.** Let $\pi\colon \widetilde{X} \to X$ be the blow-up at $x$ with exceptional divisor $E \cong \mathbb{P}^{n-1}$. Then
$$\varepsilon(X,L;x) \;=\; \sup\{\, t \in \mathbb{R}_{\ge 0} \;:\; \pi^*L - tE \text{ is nef} \,\}.$$
So $\varepsilon$ is the position of a wall of the nef cone of $\widetilde X$; the conjectures are statements about nef cones of blow-ups.

**Seshadri's criterion.** A line bundle $L$ is ample iff there is $\eta > 0$ with $L\cdot C \ge \eta \operatorname{mult}_x C$ for all $x$ and all curves $C$; equivalently $\inf_{x} \varepsilon(X,L;x) > 0$.

**Upper bounds.** Intersecting $(\pi^*L - tE)^n \ge 0$ gives
$$\varepsilon(X,L;x) \;\le\; \sqrt[n]{L^n},$$
and more sharply, for any subvariety $V \ni x$ of dimension $d$,
$$\varepsilon(X,L;x) \;\le\; \left(\frac{L^d \cdot V}{\operatorname{mult}_x V}\right)^{1/d}.$$
Multi-point version: $\varepsilon(X,L;x_1,\dots,x_r) \le (L^n/r)^{1/n}$, which for $\mathbb{P}^2$ is exactly $1/\sqrt{r}$ — so (C2) is purely a lower-bound problem.

**Semicontinuity.** $x \mapsto \varepsilon(X,L;x)$ is lower semicontinuous in the countable Zariski topology; it attains its maximum $\varepsilon(X,L;1)$ at very general points and may drop on proper subvarieties.

**Jet separation.** $\varepsilon(X,L;x) = \lim_{k\to\infty} s(kL;x)/k$, where $s(kL;x)$ is the largest $s$ with $H^0(X,kL) \to H^0(\mathcal{O}_X/\mathfrak{m}_x^{s+1})$ surjective. This links $\varepsilon$ to Fujita-type freeness questions: Demailly's criterion states that $\varepsilon(X,K_X+L;x) > 2n$ for all $x$ implies $K_X + L$ is very ample.

## 3. History & State of the Art (SOTA)

- **1959.** Nagata, disproving Hilbert's 14th problem, proves that for $r = k^2 \ge 16$ very general points in $\mathbb{P}^2$ no curve of degree $d$ has $\sum m_i \ge d\sqrt{r}$; he conjectures the same for all $r \ge 10$.
- **1990–92.** Demailly introduces Seshadri constants in "Singular Hermitian metrics on positive line bundles", using them to quantify local positivity for very ampleness criteria. The invariant is named for Seshadri's ampleness criterion.
- **1991.** Xu proves the key surface inequality bounding degrees of curves with prescribed multiplicities at very general points, the engine behind nearly all lower bounds since.
- **1993.** Ein–Lazarsfeld: on any smooth projective surface, $\varepsilon(X,L;x) \ge 1$ at very general $x$ — case $n=2$ of (C1).
- **1995.** Ein–Küchle–Lazarsfeld: in dimension $n$, $\varepsilon(X,L;x) \ge 1/n$ at very general $x$. This remains the general bound after thirty years.
- **1996–2001.** Exact computations on abelian varieties (Nakamaye; Steffens; Bauer; Bauer–Szemberg), where Pell equations determine $\varepsilon$.
- **1999.** Biran connects submaximal Seshadri constants to symplectic packing obstructions, importing symplectic-geometry techniques.
- **2005–2014.** Nakamaye analyses very general submaximality structurally; Cascini–Nakamaye push threefolds; Ito computes $\varepsilon$ via toric degenerations and Okounkov bodies.

Status: (C1) proved for $n=2$; (C2) proved for perfect-square $r$ and for $r \le 9$; (C3) untouched in the single-point case.

## 4. Partial Results / Verified Cases

- **Surfaces, single point.** $\varepsilon(X,L;x) \ge 1$ for very general $x$ on any smooth surface (Ein–Lazarsfeld 1993). Sharp: equality for $(\mathbb{P}^2,\mathcal{O}(1))$.
- **Dimension $n$.** $\varepsilon(X,L;x) \ge 1/n$ at very general $x$ (Ein–Küchle–Lazarsfeld 1995). On smooth threefolds this has been sharpened above $1/3$ by Cascini–Nakamaye (2014) *(frontier — verify the exact constant)*.
- **$\mathbb{P}^2$, $r$ points, $r \le 9$.** All values known and rational: $1, \tfrac12, \tfrac12, \tfrac12, \tfrac25, \tfrac25, \tfrac38, \tfrac{6}{17}, \tfrac13$ for $r = 1,\dots,9$, computed from $(-1)$-curves on del Pezzo surfaces.
- **$\mathbb{P}^2$, $r = k^2$, $k \ge 4$.** Nagata's conjecture holds (Nagata 1959); extended to further sequences such as $r = 9\cdot 4^k$ by degeneration methods (Ciliberto–Miranda; Evain).
- **$r \ge 10$ general lower bounds.** Xu-type arguments give $\varepsilon \ge 1/\sqrt{r+1}$; explicit specialization and computer-assisted searches (Dumnicki, Harbourne, Roé, Szemberg) improve this for small $r$ but never reach $1/\sqrt r$.
- **Abelian varieties.** $\varepsilon(A,L;x) \ge 1$ for any ample $L$, with equality iff $(A,L)$ splits off an elliptic curve factor (Nakamaye 1996). For a generic principally polarized abelian surface, $\varepsilon(A,\Theta) = 4/3 < \sqrt2$. For abelian surfaces of Picard number 1, $\varepsilon$ is determined by solutions of a Pell equation (Steffens; Bauer).
- **Toric and Mori-dream cases.** $\varepsilon$ at torus-fixed points on toric varieties is a computable polytope invariant; Ito's toric-degeneration bounds give lower bounds on general varieties admitting degenerations.
- **Very ample / adjoint bundles.** For $L$ very ample, $\varepsilon \ge 1$ trivially, so (C1) is only about ample non-very-ample bundles.

## 5. Principal Obstacles

- **Infimum over an uncountable family.** $\varepsilon$ is an infimum over all curves through $x$ of unbounded degree and singularity. There is no a priori bound on the degree of a "submaximal" curve, so no finite computation can certify a lower bound.
- **Failure of vanishing theorems.** Kodaira/Kawamata–Viehweg vanishing yields sections of $kL$ with prescribed multiplicity only when a numerical positivity threshold is met — precisely the threshold one is trying to prove. The argument is circular at the critical value $\varepsilon = 1$ (resp. $1/\sqrt r$).
- **Multiplicity-one loss in the EKL method.** EKL's proof produces a subvariety $Z \ni x$ on which $L$ has small degree and then induces on $\dim Z$; each step of the induction loses a factor, giving $1/n$ rather than $1$. Removing the loss requires controlling the geometry of $Z$, which the method never sees.
- **Irrational conjectural value.** For non-square $r$, $1/\sqrt r$ is irrational, so no single curve or finite linear-algebra certificate can attain it. Any proof must be an asymptotic/limit argument — Nagata's own square-case proof relies on a Cremona-type symmetry that exists only for $r=k^2$.
- **Countably many bad loci.** "Very general" is not Zariski-open; degeneration arguments must control infinitely many families simultaneously, and specialization to special points (Miranda-type examples with arbitrarily small $\varepsilon$) shows the bound genuinely fails without genericity.
- **No dimension-independent tool.** Surface methods use the Hodge index theorem and adjunction on curves; both degenerate in dimension $\ge 3$, where the intersection form is not of signature $(1,\rho-1)$.

## 6. The Gap

For (C1): the proven bound at very general points is $1/n$; the conjecture is $1$. The missing step is showing that if $\varepsilon(X,L;x) < 1$ at a very general $x$, the EKL subvariety $Z \ni x$ with $L^{\dim Z}\cdot Z$ small moves in a covering family and forces a contradiction with the ampleness of $L$ — the induction currently degrades multiplicatively instead of terminating.

For (C2): known lower bounds are of shape $1/\sqrt{r+c}$ with $c > 0$, or $1/\sqrt r$ times a factor $<1$. The gap is the last multiplicative $\sqrt{r/(r+c)}$, exactly where the bound would become non-attained and irrational. Equivalently: the nef cone of $\mathbb{P}^2$ blown up at $r \ge 10$ very general points is conjectured to be circular, $\{ dH - \sum m_iE_i : d \ge \sqrt{r}\,\|m\|_{\ell^2}\text{-type}\}$; proving there are no further extremal rays beyond the known $(-1)$-curves is the barrier.

## 7. Current Research (as of June 2026)

- **Okounkov bodies and Newton–Okounkov degenerations.** Ito's programme computes $\varepsilon$ from infinitesimal Newton–Okounkov bodies; simplices inside the body give lower bounds. Active at Kyoto/Tokyo.
- **K-stability interface.** $\delta$-invariants and stability thresholds bound Seshadri constants of Fano varieties; conversely Seshadri constants bound $\alpha$-invariants. Groups in Beijing, Utah and Edinburgh use this to compute $\varepsilon$ on Fano threefolds *(frontier — verify)*.
- **Computer-assisted Nagata bounds.** Dumnicki–Farnik–Harbourne–Roé–Szemberg and collaborators (Kraków, Barcelona) refine specialization/degeneration to raise lower bounds for $r = 10,11,\dots$; each improvement is numerical, not structural.
- **Positive characteristic and Frobenius.** Frobenius-splitting techniques give characteristic-$p$ analogues; whether they can be lifted to characteristic $0$ via reduction mod $p$ is an active question.
- **Symplectic packing.** Biran-style correspondences continue to translate packing results into Seshadri bounds for $\mathbb{P}^2$ and rational surfaces.
- **SHGH linkage.** The Segre–Harbourne–Gimigliano–Hirschowitz conjecture on dimensions of linear systems with base points implies Nagata; work on SHGH via Cremona reductions is the main structural route.

## 8. Future Work

- Prove (C1) in dimension 3 by classifying the covering families produced by EKL/Nakamaye when $\varepsilon(L;1) < 1$ — the case widely regarded as the decisive test.
- Establish Nagata for a single non-square $r \ge 10$ (e.g. $r = 10$), which would break the perfect-square dependence.
- Decide whether $\varepsilon(X,L;x)$ can be irrational at a single point; a construction would reshape expectations about nef cones of blow-ups.
- Determine whether $\varepsilon(X,L;1)$ is bounded below by a constant depending only on $n$ and $L^n$, rather than on $X$.
- Extend Pell-equation exactness from abelian surfaces to higher-dimensional abelian varieties and to K3 surfaces of general Picard lattice.

## 9. Key References

- **[Foundational]** J.-P. Demailly. *Singular Hermitian metrics on positive line bundles.* In: Complex Algebraic Varieties (Bayreuth 1990), Lecture Notes in Math. 1507, Springer, 1992, 87–104.
- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics 81 (1959), 766–772.
- **[Foundational]** L. Ein, R. Lazarsfeld. *Seshadri constants on smooth surfaces.* Astérisque 218 (1993), 177–186.
- **[Foundational]** L. Ein, O. Küchle, R. Lazarsfeld. *Local positivity of ample line bundles.* Journal of Differential Geometry 42 (1995), 193–219.
- **[Foundational]** G. Xu. *Ample line bundles on smooth surfaces.* Journal für die reine und angewandte Mathematik 417 (1991), 181–185.
- **[Survey]** Th. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. Knutsen, W. Syzdek, T. Szemberg. *A primer on Seshadri constants.* Contemporary Mathematics 496, AMS, 2009, 33–70.
- **[Survey]** R. Lazarsfeld. *Positivity in Algebraic Geometry I.* Ergebnisse der Mathematik 48, Springer, 2004 (Chapter 5).
- **[SOTA / Recent]** M. Nakamaye. *Seshadri constants on abelian varieties.* American Journal of Mathematics 118 (1996), 621–635.
- **[SOTA / Recent]** M. Nakamaye. *Seshadri constants at very general points.* Transactions of the AMS 357 (2005), 3285–3297.
- **[SOTA / Recent]** P. Cascini, M. Nakamaye. *Seshadri constants on smooth threefolds.* Advances in Geometry 14 (2014), 87–103.
- **[SOTA / Recent]** A. Ito. *Seshadri constants via toric degenerations.* Journal für die reine und angewandte Mathematik 695 (2014), 151–174.
- **[SOTA / Recent]** Th. Bauer. *Seshadri constants on algebraic surfaces.* Mathematische Annalen 313 (1999), 547–583.
- **[SOTA / Recent]** A. Steffens. *Remarks on Seshadri constants.* Mathematische Zeitschrift 227 (1998), 505–510.
- **[SOTA / Recent]** P. Biran. *Constructing new ample divisors out of old ones.* Duke Mathematical Journal 98 (1999), 113–135.
- **[SOTA / Recent]** C. Ciliberto, R. Miranda. *Degenerations of planar linear systems.* Journal für die reine und angewandte Mathematik 501 (1998), 191–220.
- **[SOTA / Recent]** B. Harbourne, J. Roé. *Discrete behavior of Seshadri constants on surfaces.* Journal of Pure and Applied Algebra 212 (2008), 616–627.

## 10. Worked Example / Concrete Special Case

**$r = 9$ points in $\mathbb{P}^2$: the conjectural value is attained and provable.**

Let $x_1,\dots,x_9 \in \mathbb{P}^2$ be very general and $L = \mathcal{O}(1)$. Here
$$\varepsilon(L;x_1,\dots,x_9) \;=\; \inf_{C}\frac{\deg C}{\sum_{i=1}^{9}\operatorname{mult}_{x_i}C}.$$

*Upper bound.* The linear system of cubics has dimension $9$, so a cubic $E$ passes through all nine points; for very general points $E$ is smooth and irreducible with $\operatorname{mult}_{x_i}E = 1$. Then
$$\frac{\deg E}{\sum_i \operatorname{mult}_{x_i} E} = \frac{3}{9} = \frac13 = \frac{1}{\sqrt 9}.$$

*Lower bound.* Let $C \ne E$ be irreducible of degree $d$ with multiplicities $m_i \ge 0$. Bézout applied to $C$ and $E$ gives
$$3d \;=\; C\cdot E \;\ge\; \sum_{i=1}^{9} m_i \cdot \operatorname{mult}_{x_i}E \;=\; \sum_{i=1}^{9} m_i,$$
hence $d / \sum_i m_i \ge 1/3$. Therefore $\varepsilon = 1/3$ exactly, the infimum is attained, and the value is rational.

**Why $r = 10$ breaks.** Now the volume bound still gives $\varepsilon \le \sqrt{1/10} = 1/\sqrt{10} \approx 0.31623$, but there is no analogue of $E$: ten very general points lie on no curve of degree $d$ with $\sum m_i = d\sqrt{10}$, since $\sqrt{10}$ is irrational and the ratio $d/\sum m_i$ is rational for every curve. The infimum, if the conjecture holds, is *not attained* — it is approached by an infinite sequence of curves of growing degree. Bézout with a single auxiliary curve can never close the gap; the best comparable argument uses a degree-$d_0$ curve with $\sum m_i = c\,d_0$ for some rational $c < \sqrt{10}$, and yields only $\varepsilon \ge 1/c' $ with $c' > \sqrt{10}$ — e.g. Xu-type input gives $\varepsilon \ge 1/\sqrt{11} \approx 0.3015$, leaving the interval $[0.3015,\, 0.31623]$ undecided. Explicit specialization arguments have narrowed this interval to roughly $[0.313,\,0.31623]$ *(frontier — verify)*, but the endpoint $1/\sqrt{10}$ remains unreached.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*