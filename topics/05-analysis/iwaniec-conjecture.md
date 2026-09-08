---
id: 05-analysis/iwaniec-conjecture
title: "Iwaniec Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Iwaniec Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/iwaniec-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $S$ denote the Beurling–Ahlfors transform on $L^p(\mathbb{C})$, $1 < p < \infty$. Iwaniec (1982) conjectured that its operator norm is exactly

$$\|S\|_{L^p(\mathbb{C}) \to L^p(\mathbb{C})} \;=\; p^* - 1, \qquad p^* := \max\Big(p, \tfrac{p}{p-1}\Big),$$

i.e. $\|S\|_p = p-1$ for $p \ge 2$ and $\|S\|_p = \frac{1}{p-1}$ for $1 < p \le 2$.

The lower bound $\|S\|_p \ge p^*-1$ is classical (Lehto 1965) and elementary (Section 10). The conjecture is therefore the **upper bound** $\|S\|_p \le p^*-1$. A complete proof must establish this for every $p \ne 2$; a disproof requires exhibiting a single $p$ and an $f \in L^p(\mathbb{C})$ with $\|Sf\|_p > (p^*-1)\|f\|_p$. No such $f$ is known, and no non-trivial upper bound matching $p^*-1$ has been proven for any $p \ne 2$.

## 2. Mathematical Foundations

**The operator.** For $f \in C_c^\infty(\mathbb{C})$,
$$Sf(z) \;=\; -\frac{1}{\pi}\,\mathrm{p.v.}\!\int_{\mathbb{C}} \frac{f(w)}{(z-w)^2}\, dA(w),$$
a Calderón–Zygmund operator with even kernel, homogeneous of degree $-2$. Its Fourier multiplier is
$$\widehat{Sf}(\xi) \;=\; \frac{\bar\xi}{\xi}\,\hat f(\xi), \qquad \xi \in \mathbb{C}\setminus\{0\},$$
so $|\widehat{S}| \equiv 1$ and $S$ is a unitary operator on $L^2(\mathbb{C})$: $\|S\|_2 = 1 = 2^*-1$. The conjecture is thus an assertion about the exact rate at which the norm degrades off $p=2$.

**Why it matters.** $S$ intertwines the Cauchy–Riemann derivatives: for $g \in W^{1,p}_{\mathrm{loc}}$ with compact support,
$$S\big(\partial_{\bar z} g\big) \;=\; \partial_z g .$$
It is the unique operator doing so, which makes it the fundamental object of the planar Beltrami equation
$$\partial_{\bar z} f(z) \;=\; \mu(z)\, \partial_z f(z), \qquad \|\mu\|_\infty \le k < 1 .$$
Writing $f = z + \mathcal{C}h$ ($\mathcal{C}$ the Cauchy transform) gives $h = \mu + \mu S h$, solvable by Neumann series precisely when $k\,\|S\|_p < 1$. With $\|S\|_p = p^*-1$ this holds exactly on the critical interval
$$1 + k \;<\; p \;<\; 1 + \tfrac{1}{k},$$
the range predicted by Astala's area distortion theorem — so the conjecture is the "operator-theoretic shadow" of sharp quasiconformal regularity.

**In terms of Riesz transforms.** With $R_1, R_2$ the planar Riesz transforms,
$$S \;=\; R_2^2 - R_1^2 + 2i R_1R_2 \;=\; (R_1 + iR_2)^2 ,$$
so the conjecture is a statement about second-order Riesz transforms.

**Martingale side.** Burkholder's theorem: if $(X_n)$ is a real martingale and $(Y_n)$ its transform by a predictable sequence with values in $[-1,1]$, then $\|Y\|_p \le (p^*-1)\|X\|_p$, and $p^*-1$ is sharp. The constant $p^*-1$ in the Iwaniec conjecture is *the same constant*, which is the source of all known upper bounds. The associated Burkholder function on $\mathbb{R}^2\times\mathbb{R}^2$,
$$U_p(x,y) \;=\; p\Big(1-\tfrac{1}{p^*}\Big)^{p-1}\big(|y|-(p^*-1)|x|\big)\,\big(|x|+|y|\big)^{p-1},$$
is the extremal (least) diagonally supersolutionary majorant of $|y|^p - (p^*-1)^p|x|^p$; it is rank-one convex but **not known to be quasiconvex**, and that gap is exactly the gap in the conjecture.

## 3. History & State of the Art (SOTA)

- **1965** — Lehto obtains $\|S\|_p \ge p^*-1$ via radial stretchings; the same examples give the sharp exponent of integrability for quasiconformal derivatives.
- **1982** — Iwaniec, *Extremal inequalities in Sobolev spaces and quasiconformal mappings*, states the conjecture $\|S\|_p = p^*-1$ and proves $\|S\|_p = O(p)$ as $p \to \infty$ (with a non-explicit constant), noting the connection to the Gehring–Reich area-distortion problem.
- **1984** — Burkholder proves the sharp martingale transform inequality with constant $p^*-1$, supplying the conjectured constant's probabilistic meaning.
- **1994** — Astala proves the area distortion theorem (Acta Math.), confirming the *exponents* the conjecture predicts for the Beltrami equation, without the sharp operator norm.
- **1995** — Bañuelos–Wang represent $S$ as a projection of a martingale transform of space–time Brownian motion, obtaining $\|S\|_p \le 4(p^*-1)$.
- **2002–03** — Nazarov–Volberg (heat extension / Bellman function) and, independently, Bañuelos–Méndez-Hernández (orthogonal martingales) reach $\|S\|_p \le 2(p^*-1)$. This bound is stable and gets used heavily (e.g. Petermichl–Volberg's proof that weakly quasiregular maps are quasiregular).
- **2008** — Bañuelos–Janakiraman: $\|S\|_p \le 1.575\,(p^*-1)$ for $p \ge 2$, by exploiting the orthogonality $\langle dX, dY\rangle = 0$ of the two martingale components.
- **2013** — Borichev–Janakiraman–Volberg lower the constant to roughly $1.4(p^*-1)$ in the large-$p$ regime, via a Burkholder-type function for orthogonal martingales whose optimality is tied to zeros of Legendre polynomials.
- **2012** — Astala–Iwaniec–Prause–Saksman (JAMS) prove the Burkholder-integral inequality for quasiconformal maps with $|\partial_{\bar z} f| \le k|\partial_z f|$, $k$ in an explicit range — the first proof of a genuinely sharp Burkholder bound in a nonlinear, non-martingale setting.

Best current unconditional bound: $\|S\|_p \le C(p^*-1)$ with $C$ in the range $1.4$–$1.6$ (regime-dependent). The conjecture asks for $C = 1$.

## 4. Partial Results / Verified Cases

- **$p = 2$:** proven, $\|S\|_2 = 1$, by Plancherel — the only exact value known.
- **All $p \ne 2$:** only $p^*-1 \le \|S\|_p \le 1.575(p^*-1)$ (Bañuelos–Janakiraman, $p\ge2$), improving to $\approx 1.4(p^*-1)$ asymptotically (Borichev–Janakiraman–Volberg). By duality $\|S\|_p = \|S\|_{p'}$, so $p \ge 2$ suffices.
- **Asymptotics:** Dragičević–Volberg establish $\|S\|_p \le C p$ with explicit constants and refined Littlewood–Paley/Bellman asymptotics; the *linear growth* in $p$ predicted by the conjecture is confirmed, only the slope is not.
- **Restricted classes of test functions:** the conjectured bound holds on functions arising as $\partial_{\bar z} f$ for $K$-quasiconformal $f$ in the Astala–Iwaniec–Prause–Saksman range of $k$, i.e. the Burkholder integral $\int U_p(\partial_{\bar z}f, \partial_z f)\,dA \le 0$ for such maps on the disc.
- **Second-order Riesz transforms:** Geiss–Montgomery-Smith–Saksman show the martingale constant $p^*-1$ is a *lower* bound for $\|R_1^2 - R_2^2\|_p$ and identify sharp relations between martingale transforms and these singular integrals; the exact norms remain open.
- **Weak-type endpoints:** sharp or near-sharp weak-$(1,1)$ and weak-type $(p,p)$ constants for $S$ have been computed by Bañuelos–Janakiraman and Osękowski in several regimes; these do not imply the strong-type conjecture.

## 5. Principal Obstacles

- **The martingale method loses a factor.** Every upper bound proceeds by dominating $S$ by a (pair of) martingale transforms via Brownian motion or heat extension. That representation is *not norm-preserving*: the projection back from the martingale to the function level costs a factor, and even with orthogonality constraints the loss appears irreducible below $\approx 1.4$. The obstruction is structural: the martingale model forgets the specific $\bar\xi/\xi$ multiplier and only remembers $|{\cdot}| \le 1$.
- **No Bellman function is known.** For the exact constant one would need the Bellman function of the two-dimensional problem $\sup\{\|Sf\|_p^p : \|f\|_p \le 1, \dots\}$, i.e. a function on a higher-dimensional domain with a PDE-type infinitesimal condition. The heat-extension Bellman argument uses the same $U_p$ as the martingale problem and thus cannot beat it.
- **Rank-one convex $\ne$ quasiconvex (Morrey's problem).** The natural route — prove $\int_{\mathbb{C}} U_p(\partial_{\bar z} g, \partial_z g)\, dA \le 0$ for all $g \in W^{1,p}$ — is exactly the statement that $U_p$ is quasiconvex. $U_p$ is rank-one convex (Burkholder), and in the plane whether rank-one convexity implies quasiconvexity is Morrey's 1952 problem, itself open. Sebestyén–Székelyhidi showed laminate/ lamination-based constructions cannot decide it. So the conjecture sits *inside* an open problem of the calculus of variations.
- **Fourier analysis is blunt.** $|\widehat{S}| = 1$ gives $p=2$ for free and nothing else; interpolation from $p = 2$ and a weak-type endpoint produces constants that blow up like $p$ but with the wrong slope, and Riesz–Thorin cannot recover sharp constants at even integers because $S$ is not positivity-preserving.
- **No extremizers.** The lower bound is attained only in a limit (Section 10); there is no extremal $f$ to perturb, so variational/compactness arguments have no fixed point to work with.

## 6. The Gap

Proven: $p^*-1 \le \|S\|_p \le C_p (p^*-1)$ with $C_p \approx 1.4$–$1.6$ for $p \ne 2$. Conjectured: $C_p = 1$.

The precise missing step is one of the following equivalent statements:

1. **Quasiconvexity of the Burkholder functional:** $\displaystyle\int_{\mathbb{C}} U_p\big(\partial_{\bar z}g,\;\partial_z g\big)\,dA \le 0$ for all $g \in W^{1,p}(\mathbb{C})$ with compact support (known only for $g$ quasiconformal with restricted distortion).
2. **A lossless stochastic representation:** a martingale (or heat-flow) model of $S$ whose transform constant is $p^*-1$ *without* the projection loss — i.e. capturing that the two orthogonal components of $S$ are not independent but rigidly coupled by $\bar\xi/\xi$.

Closing the gap for even a single $p \ne 2$ (say $p = 4$, target $\|S\|_4 = 3$) would be a major advance; no method currently distinguishes one $p$ from another.

## 7. Current Research (as of June 2026)

- **Bellman-function harmonic analysis** (Volberg and collaborators; Vasyunin–Volberg's 2020 monograph codifies the machinery): searching for the true Bellman function of the Beurling problem rather than reusing Burkholder's. Progress is incremental; the obstruction is that the natural domain is at least four-dimensional.
- **Probabilistic sharp inequalities** (Bañuelos, Osękowski, Janakiraman): sharp constants for *orthogonal* martingales, weak-type and $\Phi$-inequalities, and for Fourier multipliers of Lévy type. These give the current best constants and are the most likely source of further decimal improvements.
- **Calculus of variations / Morrey's problem** (Iwaniec, Prause, Saksman, Astala; Székelyhidi and the geometric-analysis school): quasiconvexity of $U_p$ on constrained classes; extending the JAMS 2012 range of $k$ toward $k \to 1$. Widening that range to all $k<1$ would give the conjecture on the quasiconformal class. *(frontier — verify)*
- **Numerical/experimental probing:** discretized and dyadic-model versions of $S$ (Haar-shift approximants) tested for constants exceeding $p^*-1$; none found. *(frontier — verify)*
- Groups: Purdue (Bañuelos), Michigan State (Volberg), Helsinki/Aalto (Astala, Saksman, Prause), Syracuse (Iwaniec), Warsaw (Osękowski).

## 8. Future Work

- Prove quasiconvexity of $U_p$ for the *complex* gradient in the plane, or find a counterexample — either outcome settles a second open problem.
- Push the Astala–Iwaniec–Prause–Saksman method to all $k < 1$ by removing the smallness constraint in the Burkholder integral estimate for principal solutions.
- Look for an exact answer at a distinguished exponent (e.g. $p$ an even integer), where $\|Sf\|_p^p$ expands into finitely many multilinear multiplier integrals that might be estimated by hand.
- Settle the higher-dimensional Iwaniec–Martin analogue for the signature operator, where extra symmetry may help.
- Develop non-martingale sharp techniques: a positivity/heat-semigroup argument keyed to the *specific* multiplier $\bar\xi/\xi$ rather than to its modulus.

## 9. Key References

- **[Foundational]** T. Iwaniec. *Extremal inequalities in Sobolev spaces and quasiconformal mappings.* Zeitschrift für Analysis und ihre Anwendungen 1 (1982), 1–16. [DOI](https://doi.org/10.4171/zaa/37)
- **[Foundational]** O. Lehto. *Remarks on the integrability of the derivatives of quasiconformal mappings.* Ann. Acad. Sci. Fenn. Ser. A I Math. 371 (1965). [DOI](https://doi.org/10.5186/aasfm.1966.371)
- **[Foundational]** D. L. Burkholder. *Boundary value problems and sharp inequalities for martingale transforms.* Annals of Probability 12 (1984), 647–702. [DOI](https://doi.org/10.1214/aop/1176993220)
- **[SOTA]** R. Bañuelos, G. Wang. *Sharp inequalities for martingales with applications to the Beurling–Ahlfors and Riesz transforms.* Duke Math. J. 80 (1995), 575–600. [DOI](https://doi.org/10.1215/s0012-7094-95-08020-x)
- **[SOTA]** F. Nazarov, A. Volberg. *Heat extension of the Beurling operator and estimates for its norm.* St. Petersburg Math. J. 15 (2004), 563–573.
- **[SOTA]** R. Bañuelos, P. J. Méndez-Hernández. *Space-time Brownian motion and the Beurling–Ahlfors transform.* Indiana Univ. Math. J. 52 (2003), 981–990. [DOI](https://doi.org/10.1512/iumj.2003.52.2218)
- **[SOTA]** O. Dragičević, A. Volberg. *Bellman function, Littlewood–Paley estimates and asymptotics for the Ahlfors–Beurling operator in $L^p(\mathbb{C})$.* Indiana Univ. Math. J. 54 (2005), 971–995. [DOI](https://doi.org/10.1512/iumj.2005.54.2554)
- **[SOTA]** R. Bañuelos, P. Janakiraman. *$L^p$-bounds for the Beurling–Ahlfors transform.* Trans. Amer. Math. Soc. 360 (2008), 3603–3612. [DOI](https://doi.org/10.1090/s0002-9947-08-04537-6)
- **[SOTA]** A. Borichev, P. Janakiraman, A. Volberg. *On Burkholder function for orthogonal martingales and zeros of Legendre polynomials.* Amer. J. Math. 135 (2013), 207–236. [DOI](https://doi.org/10.1353/ajm.2013.0004)
- **[SOTA]** K. Astala, T. Iwaniec, I. Prause, E. Saksman. *Burkholder integrals, Morrey's problem and quasiconformal mappings.* J. Amer. Math. Soc. 25 (2012), 507–531. [DOI](https://doi.org/10.1090/s0894-0347-2011-00718-2)
- **[Related]** K. Astala. *Area distortion of quasiconformal mappings.* Acta Math. 173 (1994), 37–60. [DOI](https://doi.org/10.1007/bf02392568)
- **[Related]** S. Geiss, S. Montgomery-Smith, E. Saksman. *On singular integral and martingale transforms.* Trans. Amer. Math. Soc. 362 (2010), 553–575. [DOI](https://doi.org/10.1090/s0002-9947-09-04953-8)
- **[Related]** A. Baernstein II, S. Montgomery-Smith. *Some conjectures about integral means of $\partial f$ and $\bar\partial f$.* In: Complex Analysis and Differential Equations (Uppsala, 1997), Acta Univ. Upsaliensis, 1999, 92–109.
- **[Survey]** R. Bañuelos. *The foundational inequalities of D. L. Burkholder and some of their ramifications.* Illinois J. Math. 54 (2010), 789–868. [DOI](https://doi.org/10.1215/ijm/1336049979)
- **[Book]** K. Astala, T. Iwaniec, G. Martin. *Elliptic Partial Differential Equations and Quasiconformal Mappings in the Plane.* Princeton University Press, 2009.
- **[Book]** A. Osękowski. *Sharp Martingale and Semimartingale Inequalities.* Monografie Matematyczne 72, Birkhäuser, 2012. [DOI](https://doi.org/10.1007/978-3-0348-0370-0)
- **[Book]** V. Vasyunin, A. Volberg. *The Bellman Function Technique in Harmonic Analysis.* Cambridge Studies in Advanced Mathematics 186, Cambridge University Press, 2020.

## 10. Worked Example / Concrete Special Case

**The Lehto lower bound $\|S\|_p \ge p-1$ for $p > 2$, computed explicitly.**

Fix $\beta \in (-1/p, 0)$ and set, formally, $g(z) = z^{1+\beta}\bar z^{\beta} = z\,|z|^{2\beta}$ (well defined and smooth away from the origin). Then
$$\partial_z g = (1+\beta)\,|z|^{2\beta}, \qquad \partial_{\bar z} g = \beta\,\frac{z}{\bar z}\,|z|^{2\beta}.$$
Since $S\partial_{\bar z} = \partial_z$,
$$S\left(\beta \frac{z}{\bar z}|z|^{2\beta}\right) = (1+\beta)|z|^{2\beta}.$$
Set $f_\beta(z) := \frac{z}{\bar z}|z|^{2\beta}$. Because $\left|\frac{z}{\bar z}\right| = 1$ we have $|f_\beta(z)| = |z|^{2\beta} = \frac{1}{1+\beta}|Sf_\beta(z)|\cdot\frac{1+\beta}{1}$, i.e. pointwise
$$|S f_\beta| = \frac{1+\beta}{|\beta|}\,|f_\beta| \cdot |\beta|/\beta\text{-sign aside}, \qquad \frac{|Sf_\beta|}{|f_\beta|} = \frac{1+\beta}{-\beta}\cdot(-1)\ \Rightarrow\ \frac{\|Sf_\beta\|}{\|f_\beta\|} = \frac{1+\beta}{|\beta|}.$$

To make this legitimate, truncate to an annulus: let $\chi_\varepsilon$ be a smooth cutoff equal to $1$ on $\varepsilon < |z| < 1$ and supported in $\varepsilon/2 < |z| < 2$, and put $f = \chi_\varepsilon f_\beta$. Then
$$\|f\|_p^p \;\ge\; \int_{\varepsilon<|z|<1} |z|^{2\beta p}\,dA \;=\; 2\pi \int_\varepsilon^1 r^{2\beta p + 1}\,dr \;=\; \frac{\pi}{\beta p + 1}\big(1 - \varepsilon^{2\beta p+2}\big),$$
which diverges as $\beta \downarrow -1/p$ (equivalently $\varepsilon \downarrow 0$ at the critical exponent, where the integral is $2\pi\log(1/\varepsilon)$). The commutator terms produced by the cutoff are supported on the two fixed annuli $\{\varepsilon/2<|z|<\varepsilon\}$ and $\{1<|z|<2\}$ and contribute $O(1)$ in $L^p$, while the main terms grow like $\log(1/\varepsilon)^{1/p}$. Hence
$$\|S\|_p \;\ge\; \lim_{\varepsilon \to 0}\frac{\|Sf\|_p}{\|f\|_p} \;=\; \frac{|1+\beta|}{|\beta|}\Big|_{\beta = -1/p} \;=\; \frac{1 - 1/p}{1/p} \;=\; p-1 .$$

Duality ($\|S\|_p = \|S\|_{p'}$, as $S^* = \bar S$ has the same norm) gives $\|S\|_p \ge \frac{1}{p-1}$ for $1<p<2$, so $\|S\|_p \ge p^*-1$ in all cases.

**Concrete numbers at $p = 4$.** The above gives $\|S\|_4 \ge 3$. The best proven upper bound is $\|S\|_4 \le 1.575\cdot 3 = 4.725$ (Bañuelos–Janakiraman), improving on $2\cdot 3 = 6$ (Nazarov–Volberg) and $4\cdot 3 = 12$ (Bañuelos–Wang). The conjecture asserts $\|S\|_4 = 3$ exactly. Note that the family $f_\beta$ is *not* extremal for any finite $\varepsilon$: the ratio $\frac{1+\beta}{|\beta|}$ approaches $p-1$ only in the limit $\beta \to -1/p$, where $f_\beta \notin L^p$. This absence of a genuine extremizer is the concrete face of the obstacle described in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*