---
id: 05-analysis/carleson-conjecture
title: "Carleson Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Carleson Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/carleson-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Carleson's $\varepsilon^2$-conjecture asserts that the tangent points of a planar boundary are characterized, up to a set of length zero, by the finiteness of a scale-invariant square function built from a two-sided flatness coefficient.

Let $\Omega^+ \subset \mathbb{R}^2$ be open, let $\Omega^- = \mathbb{R}^2 \setminus \overline{\Omega^+}$, and write $\partial\Omega = \partial\Omega^+$. For $x \in \partial\Omega$ and $r > 0$ set

$$\varepsilon_\Omega(x,r) \;=\; \frac{1}{r}\,\inf_{L \ni x}\ \max\Big\{ \sup_{y \in H_L^+ \cap \partial B(x,r)} \operatorname{dist}(y,\Omega^+),\ \ \sup_{y \in H_L^- \cap \partial B(x,r)} \operatorname{dist}(y,\Omega^-) \Big\},$$

the infimum over lines $L$ through $x$, with $H_L^\pm$ the two open half-planes bounded by $L$. Thus $\varepsilon_\Omega(x,r)$ measures how badly the circle $\partial B(x,r)$ fails to be split by a diameter into an arc lying in $\Omega^+$ and an arc lying in $\Omega^-$. Always $0 \le \varepsilon_\Omega(x,r) \le 2$.

**Conjecture (Carleson, 1980s).** Up to sets of $\mathcal{H}^1$-measure zero,

$$\Big\{ x \in \partial\Omega : \int_0^1 \varepsilon_\Omega(x,r)^2 \,\frac{dr}{r} < \infty \Big\} \;=\; \tau(\partial\Omega),$$

where $\tau(\partial\Omega)$ is the set of tangent points of $\partial\Omega$.

A complete proof must establish both inclusions modulo $\mathcal{H}^1$-null sets, for arbitrary open $\Omega^+$ — no rectifiability, connectivity, Ahlfors regularity, or corkscrew hypothesis on $\partial\Omega$. A disproof would exhibit a set of positive length of non-tangent points with convergent $\varepsilon^2$ integral (or the reverse).

**Status.** Proved in the plane by Jaye, Tolsa and Villa (*Annals of Mathematics*, 2021). The analogue in $\mathbb{R}^n$, $n \ge 3$, and quantitative/higher-codimension versions remain the live frontier.

## 2. Mathematical Foundations

**Tangent point.** $x \in \partial\Omega$ is a *tangent point* if there is a line $L \ni x$ such that for every $\theta \in (0,1)$ there is $\rho > 0$ with

$$\partial\Omega \cap B(x,\rho) \subset \{ y : \operatorname{dist}(y,L) \le \theta\,|y-x| \},$$

and additionally the two sides separate correctly:

$$B(x,\rho) \cap H_L^+ \cap \{ y : \operatorname{dist}(y,L) > \theta|y-x| \} \subset \Omega^+, \qquad B(x,\rho) \cap H_L^- \cap \{\cdots\} \subset \Omega^-.$$

The tangency requirement is genuinely two-sided: a slit disc has no tangent points on the slit even though the slit is a smooth arc.

**Jones $\beta$-numbers.** For $E \subset \mathbb{R}^2$,

$$\beta_{E,\infty}(x,r) = \frac{1}{r} \inf_{L} \sup_{y \in E \cap B(x,r)} \operatorname{dist}(y,L).$$

Jones' Traveling Salesman Theorem (1990) states that $E$ is contained in a rectifiable curve iff $\sum_{Q} \beta_{E,\infty}(Q)^2 \ell(Q) < \infty$ over dyadic squares. The relation to $\varepsilon$ is one-directional: $\beta_{\partial\Omega,\infty}(x,r) \lesssim \varepsilon_\Omega(x,2r)$ up to constants, but $\varepsilon$ carries strictly more information, since $\beta$ is blind to which side of $L$ the complement occupies. This is exactly why $\beta^2$ characterizes rectifiability while $\varepsilon^2$ is expected to characterize tangency.

**Square function.** Write $\mathcal{E}(x) = \int_0^1 \varepsilon_\Omega(x,r)^2 \frac{dr}{r}$. Finiteness of $\mathcal{E}(x)$ forces $\varepsilon_\Omega(x,r) \to 0$ along a set of scales of full logarithmic density, but *not* for all $r$; the gap between "small on most scales" and "small on all scales" is the analytic heart of the problem.

**Ambient theory used.** Rectifiability of $1$-sets and Besicovitch's structure theorem; the Cauchy transform, Menger curvature $c(x,y,z) = 1/R(x,y,z)$ and the identity
$$\|\mathcal{C}_\mu 1\|_{L^2(\mu)}^2 = \tfrac{1}{6}\iiint c(x,y,z)^2\,d\mu\,d\mu\,d\mu + O(\|\mu\|),$$
David–Semmes uniform rectifiability and corona decompositions; and the two-phase theory of harmonic measure (mutual absolute continuity of $\omega^+$ and $\omega^-$ implies rectifiability).

## 3. History & State of the Art (SOTA)

- **1973.** Carleson, *On the distortion of sets on a Jordan curve under conformal mapping* (Duke Math. J.), develops the quantitative flatness estimates for conformal maps that later motivate the $\varepsilon$-coefficients.
- **1980s.** Carleson formulates the $\varepsilon^2$-conjecture, circulated in problem sessions rather than in a paper. It is recorded as an open problem by Bishop, *Some questions concerning harmonic measure* (IMA Vol. 42, Springer, 1992).
- **1990.** Bishop–Jones, *Harmonic measure and arclength* (Ann. of Math.), and Jones, *Rectifiable sets and the traveling salesman problem* (Invent. Math.), establish the $\beta^2$ paradigm: quadratic square functions of flatness control rectifiability. These are the structural templates for $\varepsilon^2$.
- **1991–2014.** David–Semmes uniform rectifiability (Astérisque 193, 1991); Tolsa's non-homogeneous Calderón–Zygmund theory and the resolution of the Painlevé/Vitushkin problems supply the technology (corona decompositions for non-doubling measures, quasiorthogonality) later required.
- **2017.** Azzam–Mourgoglou–Tolsa (*Comm. Pure Appl. Math.*) prove that mutual absolute continuity of interior and exterior harmonic measure implies rectifiability — the two-phase result closest in spirit to $\varepsilon^2$.
- **2021.** Jaye, Tolsa, Villa, *A proof of Carleson's $\varepsilon^2$-conjecture*, Ann. of Math. **194** (2021), 97–161: full resolution in $\mathbb{R}^2$ with no hypotheses on $\Omega^+$.
- **2023–2026.** Higher-dimensional versions with $\varepsilon$ replaced by spherical-cap analogues, and quantitative (Carleson-measure) reformulations. *(frontier — verify)*

## 4. Partial Results / Verified Cases

- **Smooth and $C^{1,\alpha}$ boundaries.** If $\partial\Omega$ is locally a $C^{1,\alpha}$ graph, $\varepsilon_\Omega(x,r) \lesssim r^\alpha$, so $\mathcal{E}(x) < \infty$ everywhere and every boundary point is a tangent point. Both directions are elementary.
- **Lipschitz and chord-arc domains.** For a Lipschitz graph domain, $\int_0^1\!\!\int \varepsilon^2 \frac{dr}{r}d\mathcal{H}^1$ is a Carleson measure by a direct $\beta$-number comparison; combined with Rademacher's theorem this gives the equivalence $\mathcal{H}^1$-a.e. Same for chord-arc (Ahlfors-regular, two-sided corkscrew) domains, where the David–Semmes corona machinery applies verbatim.
- **The "easy" inclusion, all domains.** $\tau(\partial\Omega) \subset \{\mathcal{E} < \infty\}$ up to null sets follows from rectifiability of the tangent-point set plus a Jones-type $\beta^2$ estimate on each Lipschitz piece; this direction was understood well before 2021.
- **Rectifiable Jordan curves.** For $\partial\Omega$ a rectifiable Jordan curve, Bishop–Jones-type arguments give the equivalence $\mathcal{H}^1$-a.e., since a.e. point already has a tangent.
- **Full generality, $n = 2$.** Jaye–Tolsa–Villa (2021), for arbitrary open $\Omega^+ \subset \mathbb{R}^2$ — including boundaries of infinite length, purely unrectifiable pieces, and sets with no interior regularity.
- **Not covered.** $\mathbb{R}^n$ for $n \ge 3$; codimension $> 1$; effective/quantitative constants.

## 5. Principal Obstacles

- **No regularity to start from.** The hypothesis is only $\int_0^1 \varepsilon^2 \frac{dr}{r} < \infty$ pointwise. There is no Ahlfors regularity, no doubling measure, no corkscrew condition — so the standard David–Semmes corona decomposition, which presupposes a regular measure, is unavailable and must be rebuilt.
- **Pointwise, not Carleson, hypothesis.** Classical square-function theory converts a Carleson-measure bound $\iint \varepsilon^2 \frac{dr}{r} d\mathcal{H}^1 < \infty$ into geometry. Here the finiteness is only pointwise a.e., with no uniform control; exhaustion by level sets destroys the very structure the argument needs.
- **$\beta$-numbers are too weak.** Jones' theorem yields rectifiability, but rectifiable sets need not have tangents in the two-sided sense (the slit disc). Any proof must exploit the *sidedness* built into $\varepsilon$, which is not a metric quantity of $\partial\Omega$ alone but depends on the pair $(\Omega^+,\Omega^-)$.
- **Fourier and perturbative methods fail.** There is no linearization: the conjectured boundary of tangency is a genuine phase transition (the exponent $2$ is sharp; $\int_0^1 \varepsilon^{2+\delta}\frac{dr}{r} < \infty$ is strictly weaker information and does not suffice). Singular-integral machinery enters only through Menger curvature, which is a $2$-dimensional accident.
- **Two-phase rigidity.** Controlling the interaction of $\Omega^+$ and $\Omega^-$ at all scales requires comparison results for harmonic measure that are themselves hard theorems, and whose higher-dimensional analogues are weaker.

## 6. The Gap

In the plane, the gap is closed. The step that was crossed in 2021: from "$\varepsilon^2$ small on average implies flatness at most scales" to "the set where the boundary fails to have a two-sided tangent, yet $\mathcal{E} < \infty$, has zero length." Jaye–Tolsa–Villa achieve this by a stopping-time decomposition adapted to the $\varepsilon$-coefficients rather than to a regular measure, together with a lower bound showing that persistent non-tangential behaviour at a definite proportion of scales forces a quantified contribution to $\sum \varepsilon^2$ — the contradiction being extracted through curvature/quasiorthogonality estimates for the Cauchy transform.

The remaining gap is dimensional. In $\mathbb{R}^n$, $n \ge 3$, the natural $\varepsilon_\Omega(x,r)$ replaces diameters of circles by hyperplanes cutting $\partial B(x,r)$ into two caps. Menger curvature has no $n$-dimensional substitute with a comparable positivity identity, so the final contradiction step has no known replacement.

## 7. Current Research (as of June 2026)

- **Higher dimensions.** Fleschler, Tolsa and Villa have circulated work extending the $\varepsilon^2$-characterization to $\mathbb{R}^n$, $n \ge 3$, substituting the Riesz transform and Tolsa's $\alpha$/$\beta$-coefficient machinery for Menger curvature. *(frontier — verify)*
- **Quantitative forms.** The conjectured Carleson-measure version — if $\partial\Omega$ is Ahlfors regular and $\varepsilon^2 \frac{dr}{r}d\mathcal{H}^1$ is a Carleson measure, then $\partial\Omega$ is uniformly rectifiable with two-sided big pieces — is being pursued as the "uniform" companion. *(frontier — verify)*
- **Harmonic measure two-phase problems.** Groups at UAB/ICREA (Tolsa, Azzam), Georgia Tech/Clemson (Jaye), Oulu and Jyväskylä (Villa, Orponen), and Barcelona–Edinburgh collaborations connect $\varepsilon^2$ to $\omega^+ \ll \omega^- \ll \omega^+$ criteria.
- **Free-boundary applications.** Transfer of $\varepsilon^2$ techniques to one- and two-phase free boundary regularity (Kenig–Toro school) and to the geometry of level sets of harmonic functions.

## 8. Future Work

- Prove or refute the $\varepsilon^2$-characterization in $\mathbb{R}^n$ for $n \ge 3$ without regularity assumptions.
- Establish the quantitative Carleson-measure equivalence and identify sharp constants.
- Determine whether the exponent $2$ can be replaced by $p$ with a matching $\beta_p$-type theory (Tolsa's $\beta_p$ rectifiability results suggest a family of statements for $1 \le p \le 2$).
- Extend to $d$-dimensional sets in $\mathbb{R}^n$ with $d < n-1$, where "two-sided" must be reinterpreted.
- Find a proof of the planar case avoiding Menger curvature, as a route to higher dimensions.

## 9. Key References

- **[Foundational]** L. Carleson. *On the distortion of sets on a Jordan curve under conformal mapping.* Duke Mathematical Journal, 40 (1973), 547–559.
- **[Foundational]** C. J. Bishop. *Some questions concerning harmonic measure.* In *Partial Differential Equations with Minimal Smoothness and Applications*, IMA Volumes in Mathematics and its Applications 42, Springer, 1992, 89–97.
- **[Foundational]** P. W. Jones. *Rectifiable sets and the traveling salesman problem.* Inventiones Mathematicae, 102 (1990), 1–15.
- **[Foundational]** C. J. Bishop, P. W. Jones. *Harmonic measure and arclength.* Annals of Mathematics, 132 (1990), 511–547.
- **[SOTA]** B. Jaye, X. Tolsa, M. Villa. *A proof of Carleson's $\varepsilon^2$-conjecture.* Annals of Mathematics, 194 (2021), 97–161.
- **[SOTA]** J. Azzam, M. Mourgoglou, X. Tolsa. *Mutual absolute continuity of interior and exterior harmonic measure implies rectifiability.* Communications on Pure and Applied Mathematics, 70 (2017), 2121–2163.
- **[Survey]** G. David, S. Semmes. *Singular Integrals and Rectifiable Sets in $\mathbb{R}^n$: Beyond Lipschitz Graphs.* Astérisque 193, Société Mathématique de France, 1991.
- **[Survey]** X. Tolsa. *Analytic Capacity, the Cauchy Transform, and Non-homogeneous Calderón–Zygmund Theory.* Progress in Mathematics 307, Birkhäuser, 2014.
- **[Survey]** P. Mattila. *Geometry of Sets and Measures in Euclidean Spaces: Fractals and Rectifiability.* Cambridge University Press, 1995.

## 10. Worked Example / Concrete Special Case

**A corner has divergent $\varepsilon^2$ integral.** Let $\Omega^+$ be the open sector of aperture $\alpha \in (0,\pi)$ at the origin,
$$\Omega^+ = \{ (\rho,\theta) : \rho > 0,\ 0 < \theta < \alpha \}, \qquad \Omega^- = \mathbb{R}^2 \setminus \overline{\Omega^+}.$$
Fix $x = 0$ and $r > 0$, and let $L_\varphi$ be the line through $0$ at angle $\tfrac{\alpha}{2} + \varphi$, so $H^+_\varphi$ covers angles in $(\tfrac{\alpha}{2}+\varphi-\tfrac{\pi}{2},\ \tfrac{\alpha}{2}+\varphi+\tfrac{\pi}{2})$.

For a point $y \in \partial B(0,r)$ at angle $\theta \notin [0,\alpha]$, the nearest point of $\overline{\Omega^+}$ on the circle is at angular gap $g(\theta) = \min(|\theta|, |\theta - \alpha|)$ mod $2\pi$, and $\operatorname{dist}(y,\Omega^+) = r\sin g(\theta)$ when $g(\theta) \le \pi/2$.

- *Term for $H^+$:* the extreme angles of $H^+_\varphi$ have gaps $\tfrac{\pi}{2}+\varphi-\tfrac{\alpha}{2}$ and $\tfrac{\pi}{2}-\varphi-\tfrac{\alpha}{2}$. The supremum is $r\sin\!\big(\tfrac{\pi}{2}+|\varphi|-\tfrac{\alpha}{2}\big)$, minimized at $\varphi = 0$, giving $r\cos(\alpha/2)$.
- *Term for $H^-$:* since $\alpha < \pi$, the half-plane $H^-_0$ (angles in $(\tfrac{\alpha}{2}+\tfrac{\pi}{2}, \tfrac{\alpha}{2}+\tfrac{3\pi}{2})$) misses $[0,\alpha]$ entirely, so every $y$ there lies in $\overline{\Omega^-}$ and the supremum is $0$.

Hence
$$\varepsilon_\Omega(0,r) = \cos(\alpha/2) \quad \text{for all } r>0, \qquad \int_0^1 \varepsilon_\Omega(0,r)^2 \frac{dr}{r} = \cos^2(\alpha/2)\int_0^1 \frac{dr}{r} = \infty$$
whenever $\alpha \ne \pi$. Scale invariance of the sector makes $\varepsilon$ constant in $r$, so the logarithmic integral diverges. This matches the geometry: the vertex is not a tangent point. For $\alpha = \pi$ (half-plane) one gets $\varepsilon \equiv 0$ and the integral vanishes.

**A $C^{1,\beta}$ point has convergent integral.** If near $x$ the boundary is the graph of $f$ with $f(0)=f'(0)=0$ and $|f'(t)| \le M|t|^\beta$, then choosing $L$ = the tangent line gives $\operatorname{dist}(y,\Omega^\pm) \le \sup_{|t|\le r}|f(t)| \le \tfrac{M}{1+\beta} r^{1+\beta}$ for $y$ on the correct side, so
$$\varepsilon_\Omega(x,r) \le \tfrac{M}{1+\beta}\, r^{\beta}, \qquad \int_0^1 \varepsilon_\Omega(x,r)^2\frac{dr}{r} \le \frac{M^2}{(1+\beta)^2}\int_0^1 r^{2\beta}\frac{dr}{r} = \frac{M^2}{2\beta(1+\beta)^2} < \infty,$$
and $x$ is a tangent point. The conjecture asserts that this dichotomy — divergence at corners, convergence at tangents — persists $\mathcal{H}^1$-a.e. for boundaries with no regularity whatsoever.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*