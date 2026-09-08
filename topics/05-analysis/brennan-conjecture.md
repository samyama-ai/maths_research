---
id: 05-analysis/brennan-conjecture
title: "Brennan Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brennan Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/brennan-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Omega \subsetneq \mathbb{C}$ be a simply connected domain with at least two boundary points, and let
$$\varphi : \Omega \longrightarrow \mathbb{D} = \{z : |z| < 1\}$$
be a conformal (holomorphic, injective, onto) map, which exists and is unique up to post-composition with a Möbius automorphism of $\mathbb{D}$ by the Riemann mapping theorem.

**Conjecture (Brennan, 1978).** For every such $\Omega$,
$$\int_\Omega |\varphi'(w)|^{p}\, dA(w) < \infty \qquad \text{for all } p \in \left(\tfrac{4}{3},\, 4\right),$$
where $dA$ is two-dimensional Lebesgue measure.

The open interval is optimal: for $p \ge 4$ and for $p \le 4/3$ the integral diverges for the complement of a half-line (Section 10). A complete resolution means either a proof valid for all simply connected $\Omega$ and all $p<4$, or a single domain $\Omega$ and an exponent $p_0 < 4$ with $\int_\Omega|\varphi'|^{p_0}\,dA = \infty$.

## 2. Mathematical Foundations

**Inverse formulation.** Let $f = \varphi^{-1} : \mathbb{D} \to \Omega$ be conformal. Substituting $w = f(z)$, so $dA(w) = |f'(z)|^2\,dA(z)$ and $|\varphi'(f(z))| = |f'(z)|^{-1}$, gives the identity
$$\int_\Omega |\varphi'|^{p}\,dA \;=\; \int_{\mathbb{D}} |f'(z)|^{\,2-p}\,dA(z).$$
So Brennan's conjecture is: **for every univalent $f$ on $\mathbb{D}$, $\int_{\mathbb{D}}|f'|^{t}\,dA < \infty$ for all $t \in (-2, 2/3)$.** Only $t \le 0$, i.e. $p \ge 2$, is open.

**Integral means spectrum.** For univalent $f:\mathbb{D}\to\mathbb{C}$ and $t \in \mathbb{R}$ set
$$\beta_f(t) \;=\; \limsup_{r \to 1^-} \frac{\log \int_0^{2\pi} |f'(re^{i\theta})|^{t}\, d\theta}{\log \frac{1}{1-r}}, \qquad B(t) \;=\; \sup_{f \text{ univalent}} \beta_f(t).$$
Since $\int_{\mathbb{D}}|f'|^t\,dA = \int_0^1\!\!\int_0^{2\pi}|f'(re^{i\theta})|^t\,d\theta\, r\,dr$, finiteness holds when $\beta_f(t) < 1$ and fails when $\beta_f(t) > 1$. Hence:

$$\textbf{Brennan's conjecture} \iff B(t) < 1 \ \ \forall\, t \in (-2,0] \iff B(-2) = 1 .$$

$B$ is convex, $B(0)=0$, and $B(t) \ge |t| - 1$ for $|t| \ge 2$ (Koebe function), with equality for $t$ large.

**Carleson–Jones conjecture.** $B(t) = t^2/4$ for $|t| \le 2$ and $B(t) = |t|-1$ for $|t|\ge 2$. At the transition point $t=-2$ both formulas give $1$, so this stronger statement contains Brennan's.

**Known exact values.** Feng–MacGregor (1976): $B(t) = 3t-1$ for $t \ge 2/5$. Thus $B(t) < 1 \iff t < 2/3$, which proves the sharp lower endpoint $p > 4/3$ and shows $p=4/3$ is unattainable.

**Related quantities.** $B$ controls the dimension spectrum of harmonic measure (Makarov); the asymptotic variance $\Sigma^2$ of Bloch functions satisfies $B(t) \ge \Sigma^2 t^2/4 + o(t^2)$ as $t\to 0$, and $\Sigma^2 \le 1$ is the local ($t\to0$) shadow of Carleson–Jones.

## 3. History & State of the Art (SOTA)

- **Pre-history.** The question of which powers of $|\varphi'|$ are area-integrable goes back to work on approximation by polynomials in Bergman spaces; Brennan's motivation was the study of $L^p$ polynomial approximation and the boundary behaviour of conformal maps.
- **1978.** James E. Brennan, *The integrability of the derivative in conformal mapping* (J. London Math. Soc.), proves integrability for $4/3 < p < 3+\delta$ for an unspecified small $\delta > 0$, and conjectures the full range up to $4$.
- **1985.** Pommerenke's integral-means estimates for univalent functions give explicit, if modest, admissible ranges above $p=3$.
- **1992.** Carleson and Jones (Duke Math. J.) connect the problem to coefficient growth of univalent functions and to the universal spectrum $B(t)$, propose the $t^2/4$ law, and give numerical evidence; their methods yield roughly $p < 3.399$.
- **1999.** Daniel Bertilsson's KTH thesis, *On Brennan's conjecture in conformal mapping*, systematizes the Bergman-space/Bloch-function approach and reaches about $p < 3.421$.
- **2005.** Hedenmalm and Shimorin (Duke Math. J.) use weighted Bergman spaces, a Bergman-space Green function and area-type ("Hele-Shaw"/Bloch) estimates to obtain the record universal range $4/3 < p < 3.422$, together with improved bounds on $B(t)$ near $t=0$.
- **2006.** Kayumov (Ark. Mat.) gives lower bounds showing $B(t) > t^2/4$ for small $t>0$ in the universal (unbounded) class, so the Carleson–Jones identity cannot hold verbatim across the whole range; the value at $t=-2$ is untouched.
- **2015–2019.** Astala–Ivrii–Perälä–Prause bound the asymptotic variance of the Beurling transform ($\Sigma^2 < 1$, numerically $\le 0.88$); Ivrii sharpens Makarov's principle. These constrain $B$ near $0$ but not at $t=-2$.

**SOTA summary:** the universal admissible range is $4/3 < p < 3.422$; the conjectured range is $4/3 < p < 4$; no counterexample or improvement past $3.422$ has been published.

## 4. Partial Results / Verified Cases

- **Full lower range, sharp.** $4/3 < p \le 2$ (equivalently $0 \le t < 2/3$) is a theorem, sharp by Feng–MacGregor's $B(t)=3t-1$ for $t \ge 2/5$.
- **Universal upper range.** $2 < p < 3.422$ for *all* simply connected domains (Hedenmalm–Shimorin 2005), improving $3.421$ (Bertilsson 1999) and $\approx 3.399$ (Carleson–Jones 1992).
- **Smooth and quasiconformally mild boundaries.** If $\partial\Omega$ is $C^{1,\alpha}$, or a chord-arc/Lipschitz curve, $|\varphi'|$ is bounded above and below near $\partial\Omega$ and all $p<4$ are trivially admissible. For quasidisks with dilatation $k$ small, spectrum bounds of the form $\beta_f(t) = O(k^2 t^2)$ (Prause–Smirnov) give the full range $p<4$ once $k$ is below an explicit threshold.
- **Starlike and close-to-convex domains.** Feng–MacGregor's exact spectra for these classes give the complete interval $4/3<p<4$.
- **Dynamically defined domains.** Barański, Volberg and Zdunik (IMRN 1998) verify Brennan's conjecture for the complement of the Mandelbrot set and for basins of attraction of hyperbolic and semi-hyperbolic rational maps, using thermodynamic formalism and the pressure function in place of universal estimates.
- **Uniformly perfect / John domains.** Explicit spectrum estimates in terms of the John constant give ranges strictly better than $3.422$, degenerating to it as the constant degenerates.

## 5. Principal Obstacles

- **No extremal domain.** The exponents $4$ and $4/3$ are forced by the slit plane, but the slit plane is *not* extremal for $B(t)$ at $t=-2$; the conjectural extremal configurations are fractal (snowflake-like, self-similar) and no candidate family has been shown to attain the supremum. Without a known extremizer, variational arguments have nothing to vary around.
- **Convexity gives the wrong endpoint.** $B$ is convex with $B(0)=0$; interpolating between $B(0)=0$ and the exactly known regime $t\ge 2/5$ yields nothing on $t<0$. The two sides of $t=0$ are analytically decoupled, since $t<0$ measures how *slowly* $|f'|$ decays, a quantity Koebe distortion controls only from one side.
- **Area/Bergman methods saturate.** Hedenmalm–Shimorin's weighted Bergman machinery converts the problem into a positivity property of an explicitly weighted Green function. The available weights produce a strict inequality that runs out near $3.42$; pushing further needs a weight family whose positivity is not currently provable.
- **The $t\to 0$ theory does not extrapolate.** Bloch-function variance results ($\Sigma^2 < 1$) pin $B(t)$ near $t=0$ to second order, but $t=-2$ is far outside any asymptotic regime, and Kayumov's lower bounds show the $t^2/4$ ansatz is not exact, so no clean interpolation is legitimate.
- **Multifractal transfer operators are non-uniform.** Thermodynamic formalism works for dynamically self-similar boundaries (hence the Mandelbrot result) but there is no transfer operator attached to a general simply connected domain.

## 6. The Gap

Proved: $B(t) < 1$ for $t > -1.422$, i.e. $p < 3.422$. Conjectured: $B(t) < 1$ for all $t > -2$, i.e. $p<4$. The gap is the closed sub-interval
$$t \in (-2,\, -1.422], \qquad p \in [3.422,\, 4),$$
and the exact statement to be crossed is the single boundary value
$$B(-2) \;\overset{?}{=}\; 1,$$
where $B(-2) \ge 1$ is known from the Koebe function. Equivalently: one must show that no univalent $f$ on $\mathbb{D}$ has $\int_0^{2\pi}|f'(re^{i\theta})|^{-2}\,d\theta$ growing faster than $(1-r)^{-1}$ up to subpolynomial factors. Every current method produces an estimate $B(t) \le \Psi(t)$ with $\Psi(-2) > 1$ strictly; nothing yet forces $\Psi$ to be tangent to $1$ at $t=-2$.

## 7. Current Research (as of June 2026)

- **Bergman-space positivity (KTH Stockholm, Hedenmalm school).** Continued refinement of weighted Bergman kernels and "geometric zero packing" constants; the aim is a weight whose associated quadratic form stays positive down to $t=-2$. Incremental numerical improvements past $3.422$ have circulated but no published record change. *(frontier — verify)*
- **Asymptotic variance and Beurling transform (Helsinki/Aalto, Toronto).** Astala, Ivrii, Perälä, Prause and collaborators bound $\Sigma^2$ well below $1$; work continues on transferring these to global (non-asymptotic) bounds on $B$. Whether $\Sigma^2 < 1$ can be integrated into a bound at $t=-2$ is the live technical question. *(frontier — verify)*
- **Dynamical/fractal models (Warsaw, Michigan State).** Extending the Barański–Volberg–Zdunik framework to broader classes (non-uniformly hyperbolic, Julia sets with parabolic points) to widen the verified class of domains.
- **Numerical spectra.** High-precision computation of $\beta_f(t)$ for lacunary and Julia-set examples (Kayumov, Kraetzer-type constructions) to test whether $B(-2)$ could exceed $1$; all published data are consistent with $B(-2)=1$.
- **Composition-operator formulation.** Kayumov and others reformulate integrability of $|\varphi'|^p$ as boundedness/compactness of composition operators between Bergman spaces, opening operator-theoretic criteria.

## 8. Future Work

- Identify a conjectural extremal domain at $t=-2$ (self-similar snowflake) and compute its spectrum exactly; either it attains $1$ (evidence) or exceeds it (disproof).
- Construct a weighted Bergman metric whose Green function positivity is equivalent, rather than merely sufficient, to $B(-2)=1$ — Hedenmalm's stated program.
- Prove a genuine tangency statement: $B(t) \le 1$ with equality only at $t=-2$, by combining convexity with the exact regime $B(t)=3t-1$, $t\ge 2/5$, and a nontrivial lower-order term.
- Settle the Carleson–Jones conjecture in a neighbourhood of $t=-2$ (weaker than the full identity, which Kayumov's lower bounds already rule out globally).
- Sharpen the quasidisk threshold: prove $\beta_f(t) \le k^2t^2/4 + o(k^2)$ uniformly on $t\in[-2,0]$, which would give Brennan for all quasidisks.

## 9. Key References

- **[Foundational]** J. E. Brennan. *The integrability of the derivative in conformal mapping.* Journal of the London Mathematical Society (2), 18 (1978), 261–272. [DOI](https://doi.org/10.1112/jlms/s2-18.2.261)
- **[Foundational]** B. G. Feng, T. H. MacGregor. *Estimates on integral means of the derivatives of univalent functions.* Journal d'Analyse Mathématique, 29 (1976), 203–231. [DOI](https://doi.org/10.1007/bf02789979)
- **[Foundational]** L. Carleson, P. W. Jones. *On coefficient problems for univalent functions and conformal dimension.* Duke Mathematical Journal, 66 (1992), 169–206. [DOI](https://doi.org/10.1215/s0012-7094-92-06605-1)
- **[SOTA]** H. Hedenmalm, S. Shimorin. *Weighted Bergman spaces and the integral means spectrum of conformal mappings.* Duke Mathematical Journal, 127 (2005), 341–393. [DOI](https://doi.org/10.1215/s0012-7094-04-12725-3)
- **[SOTA]** D. Bertilsson. *On Brennan's conjecture in conformal mapping.* Doctoral thesis, Royal Institute of Technology (KTH), Stockholm, 1999.
- **[Recent]** I. R. Kayumov. *Lower estimates for integral means of univalent functions.* Arkiv för Matematik, 44 (2006), 104–110. [DOI](https://doi.org/10.1007/s11512-005-0009-y)
- **[Recent]** K. Astala, O. Ivrii, A. Perälä, I. Prause. *Asymptotic variance of the Beurling transform.* Geometric and Functional Analysis, 25 (2015), 1647–1687. [DOI](https://doi.org/10.1007/s00039-015-0347-2)
- **[Recent]** H. Hedenmalm. *Bloch functions and asymptotic tail variance.* Advances in Mathematics, 313 (2017), 947–990. [DOI](https://doi.org/10.1016/j.aim.2017.04.016)
- **[Special classes]** K. Barański, A. Volberg, A. Zdunik. *Brennan's conjecture and the Mandelbrot set.* International Mathematics Research Notices, 1998, no. 12, 589–600.
- **[Special classes]** I. Prause, S. Smirnov. *Quasisymmetric distortion spectrum.* Bulletin of the London Mathematical Society, 43 (2011), 267–277. [DOI](https://doi.org/10.1112/blms/bdq098)
- **[Survey]** Ch. Pommerenke. *Boundary Behaviour of Conformal Maps.* Grundlehren der mathematischen Wissenschaften 299, Springer, 1992. [DOI](https://doi.org/10.1007/978-3-662-02770-7)
- **[Survey]** N. G. Makarov. *Fine structure of harmonic measure.* St. Petersburg Mathematical Journal, 10 (1999), 217–268.

## 10. Worked Example / Concrete Special Case

**The slit plane and the Koebe function — why the endpoints are $4/3$ and $4$.**

Take $\Omega = \mathbb{C} \setminus (-\infty, -\tfrac14]$, a simply connected domain. Its conformal map from the disk is the Koebe function
$$f(z) = \frac{z}{(1-z)^2}, \qquad f'(z) = \frac{1+z}{(1-z)^3}, \qquad f(\mathbb{D}) = \Omega .$$
Set $\varphi = f^{-1} : \Omega \to \mathbb{D}$. By the change of variables of Section 2,
$$I(p) := \int_\Omega |\varphi'|^p\,dA \;=\; \int_{\mathbb{D}} |f'(z)|^{2-p}\,dA(z) \;=\; \int_{\mathbb{D}} |1+z|^{\,2-p}\,|1-z|^{\,3(p-2)}\,dA(z).$$

Only the two boundary points $z=\pm 1$ can create divergence; elsewhere the integrand is continuous and bounded on $\overline{\mathbb{D}}$.

*Near $z=-1$.* Here $|1-z| \asymp 2$, so the integrand behaves like $|1+z|^{2-p}$. On a disk of radius $\tfrac12$ around $-1$ intersected with $\mathbb{D}$, using polar coordinates $s=|1+z|$,
$$\int_0^{1/2} s^{2-p}\, s\,ds < \infty \iff 3-p > -1 \iff p < 4 .$$

*Near $z=+1$.* Here $|1+z| \asymp 2$ and the integrand behaves like $|1-z|^{3(p-2)}$. With $s = |1-z|$,
$$\int_0^{1/2} s^{3(p-2)}\, s\,ds < \infty \iff 3(p-2) > -2 \iff p > \tfrac43 .$$

Combining: $I(p) < \infty$ exactly for $\tfrac43 < p < 4$, and $I(4/3) = I(4) = \infty$. The two singular boundary points are geometrically distinct: $z=1$ is the preimage of $\infty$ (where $\Omega$ is "wide", $|\varphi'|$ small), $z=-1$ is the preimage of the slit tip $-\tfrac14$ (where $\Omega$ is "pinched", $|\varphi'|$ large). The upper endpoint $p=4$ comes from the tip.

Spectrum check: $\beta_f(t) = \max(3t-1,\,-t-1)$ for the Koebe function, so $\beta_f(-2) = 1$ — exactly the conjectured value of $B(-2)$. The conjecture asserts the Koebe function is extremal at $t=-2$; the theorems of Section 4 only prove it is extremal for $t \ge 2/5$ and that nothing beats it by more than the gap of Section 6 for $t \in (-2,-1.422]$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*