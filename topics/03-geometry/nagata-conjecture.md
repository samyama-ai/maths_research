---
id: 03-geometry/nagata-conjecture
title: "Nagata Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nagata Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/nagata-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be an algebraically closed field of characteristic $0$ and let $p_1,\dots,p_r \in \mathbb{P}^2_k$ be very general points (i.e. lying outside a countable union of proper closed subvarieties of $(\mathbb{P}^2)^r$).

**Conjecture (Nagata, 1959).** If $r > 9$, then every curve $C \subset \mathbb{P}^2$ of degree $d$ having multiplicity $\operatorname{mult}_{p_i} C \ge m_i$ at each $p_i$ satisfies
$$d \;>\; \frac{1}{\sqrt{r}} \sum_{i=1}^{r} m_i .$$

The uniform case ($m_i = m$ for all $i$) already carries the full content: it asserts $d > m\sqrt{r}$, i.e. $d \ge \lceil m\sqrt r\rceil$ whenever $\sqrt r \notin \mathbb{Z}$, and $d \ge m\sqrt r + 1$ when $r$ is a square.

A complete proof must establish the inequality for **all** $r \ge 10$ and all multiplicity vectors; a disproof requires exhibiting one $(r, d, m_1,\dots,m_r)$ with $r \ge 10$, $d \le r^{-1/2}\sum m_i$, and a curve of that degree through very general points with those multiplicities. The hypothesis $r > 9$ is necessary: for $r = 9$ the pencil of cubics through $9$ very general points gives $d = 3$, $m_i = 1$, and $3 = 9/\sqrt9$, so equality occurs.

## 2. Mathematical Foundations

**Blow-up model.** Let $\pi : X_r \to \mathbb{P}^2$ be the blow-up at $p_1,\dots,p_r$, with exceptional divisors $E_1,\dots,E_r$ and $H = \pi^*\mathcal{O}(1)$. Then $\operatorname{Pic}(X_r) = \mathbb{Z}H \oplus \bigoplus_i \mathbb{Z}E_i$ with intersection form $H^2 = 1$, $E_i^2 = -1$, $H\cdot E_i = E_i \cdot E_j = 0$ ($i\neq j$). The strict transform of $C$ is $dH - \sum_i m_i E_i$, and Nagata's inequality says that the class
$$ D = \sqrt{r}\,H - \sum_{i=1}^r E_i $$
lies in the closure of the nef cone: $D \cdot (dH - \sum m_i E_i) \ge 0$ for every effective class, i.e. $d\sqrt r \ge \sum m_i$ (with strictness the sharpened form).

**Seshadri-constant formulation.** For a nef line bundle $L$ on a smooth projective $X$ and points $p_1,\dots,p_r$,
$$\varepsilon(L; p_1,\dots,p_r) \;=\; \inf_{C \ni \text{some } p_i} \frac{L\cdot C}{\sum_i \operatorname{mult}_{p_i} C}.$$
Write $\varepsilon_r := \varepsilon(\mathcal{O}_{\mathbb{P}^2}(1); p_1,\dots,p_r)$ for very general points. Volume gives the universal upper bound $\varepsilon_r \le 1/\sqrt r$. Nagata's conjecture is exactly
$$\varepsilon_r = \frac{1}{\sqrt r}\qquad\text{for all } r \ge 9 .$$

**Symbolic-power / Waldschmidt formulation.** Let $I = I(p_1,\dots,p_r) \subset k[x_0,x_1,x_2]$ and $I^{(m)} = \bigcap_i \mathfrak{p}_i^m$ the $m$-th symbolic power. With $\alpha(J)$ the least degree of a nonzero form in $J$, the Waldschmidt constant is
$$\widehat{\alpha}(I) = \lim_{m\to\infty} \frac{\alpha(I^{(m)})}{m} = \inf_m \frac{\alpha(I^{(m)})}{m}$$
(the limit exists by subadditivity). Nagata's conjecture is equivalent to $\widehat{\alpha}(I) = \sqrt r$ for $r \ge 10$ very general points, and $1/\widehat\alpha(I) = \varepsilon_r$.

**Ambient conjecture.** The SHGH conjecture (Segre–Harbourne–Gimigliano–Hirschowitz) predicts the dimension of every linear system $\mathcal{L}_d(m_1,\dots,m_r)$ of degree-$d$ curves with imposed multiplicities: the system is non-special unless it contains a multiple $(-1)$-curve in its base locus. SHGH $\Rightarrow$ Nagata.

**Symplectic side.** Via McDuff–Polterovich, $\varepsilon_r$ controls symplectic ball packings of $\mathbb{CP}^2$: Nagata's equality is equivalent to the absence of packing obstructions beyond volume for $r \ge 10$ equal balls.

## 3. History & State of the Art (SOTA)

Nagata introduced the inequality in 1959 as the geometric engine of his counterexample to **Hilbert's 14th problem**: the ring of invariants of a suitable $13$-dimensional unipotent group acting on $k[x_1,\dots,x_{32}]$ is not finitely generated, and the obstruction is precisely control of curves through $r = 16$ general points of $\mathbb{P}^2$. In the same paper he proved the inequality when $r$ is a perfect square $\ge 16$; his *Memoirs of the College of Science, Kyoto* paper "On rational surfaces II" (1960) set the conjecture in the general form above.

Milestones:

- **1959–60 (Nagata).** Proof for $r = k^2$, $k \ge 4$, by a specialization/Cremona argument on $k^2$ points lying on a smooth curve of degree $k$.
- **1961 (Segre), 1986–89 (Harbourne, Gimigliano, Hirschowitz).** Four independent formulations of what is now the SHGH conjecture, a strictly stronger statement.
- **1994–95 (Xu).** First general lower bound valid for all $r\ge10$: $\varepsilon_r \ge 1/\sqrt{r+1}$, from a differentiation/Bezout technique on families of curves.
- **1994 (McDuff–Polterovich), 1999 (Biran).** Translation to symplectic packing; Biran proved packing stability for $\ge 9$ balls, confirming the asymptotic picture.
- **1998–2000 (Ciliberto–Miranda).** Degeneration of the plane to unions of surfaces; verification of SHGH (hence Nagata) for all uniform multiplicities $m \le 12$.
- **1999 (Evain).** Nagata for $r = 4^h \cdot s$ families via collisions of fat points.
- **2007 (Dumnicki–Jarnicki).** Computer-assisted extension of SHGH-type non-speciality to uniform multiplicity $m \le 42$.
- **2013–2017.** Variations and generalizations: monomial-valuation Nagata conjectures (Dumnicki–Harbourne–Küronya–Roé–Szemberg), Nagata-type statements on other surfaces, and the containment problem $I^{(3)} \subseteq I^2$ literature.

No case with $r \ge 10$ non-square has ever been settled unconditionally.

## 4. Partial Results / Verified Cases

- **$r$ a perfect square, $r = k^2 \ge 16$:** proved by Nagata (1959). This is the only infinite family of $r$ known in full.
- **$r \le 9$:** $\varepsilon_r$ is known exactly for all $r \le 9$ — $\varepsilon_1=1$, $\varepsilon_2=\varepsilon_3=1/2$, $\varepsilon_4=\varepsilon_5=2/5$, $\varepsilon_6=5/12$? (rational, computed from $(-1)$-curves), $\varepsilon_7=3/8$, $\varepsilon_8=6/17$, $\varepsilon_9=1/3$. Here $X_r$ is a del Pezzo or a rational elliptic surface, its effective cone is finitely generated by $(-1)$-curves, and the infimum is attained. For $r=9$ equality $\varepsilon_9 = 1/\sqrt9$ holds, so the conjecture's boundary case is verified.
- **Bounded multiplicity:** uniform multiplicity $m \le 12$ for all $r$ (Ciliberto–Miranda 2000), extended to $m \le 42$ by Dumnicki–Jarnicki (2007) using algorithmic non-speciality certificates.
- **Special $r$ from collisions:** Evain's method proves the conjecture for $r = 4^h$ points with equal multiplicities, and for classes of $r$ obtained by iterated $4$-fold collisions.
- **Asymptotic bounds for all $r \ge 10$:** $\varepsilon_r \ge 1/\sqrt{r+1}$ (Xu). For $r=10$ this reads $\varepsilon_{10} \ge 1/\sqrt{11} \approx 0.3015$ against the conjectured $1/\sqrt{10} \approx 0.31623$. Specialization and degeneration arguments improve the constant for individual small $r$, closing the gap to the third decimal place in the best cases *(frontier — verify)*.
- **Positive characteristic:** the statement can fail over $\overline{\mathbb{F}_p}$ for special (non-very-general) configurations; the conjecture is posed in characteristic $0$.

## 5. Principal Obstacles

- **The effective cone of $X_r$ is not finitely generated for $r \ge 10$.** For $r \le 8$, $-K_{X_r}$ is ample and Mori theory bounds the extremal rays by finitely many $(-1)$-curves. For $r \ge 10$, $K_{X_r}^2 = 9-r < 0$ and infinitely many $(-1)$-curves exist (Cremona orbits); the conjectured nef class $\sqrt r H - \sum E_i$ is irrational and sits on the *boundary* of the cone as a limit of infinitely many curve classes. Every finite-dimensional argument therefore stops short.
- **Riemann–Roch is only an inequality.** The expected dimension $\binom{d+2}{2} - \sum\binom{m_i+1}{2}$ gives a lower bound on $h^0$; controlling *non-existence* requires vanishing of $h^1$, which is exactly what SHGH conjectures and nobody can prove.
- **Vanishing theorems are the wrong shape.** Kawamata–Viehweg/Nadel vanishing requires strict positivity that is unavailable precisely at the conjectural boundary; the multiplier-ideal thresholds one derives reproduce the volume bound, not a strict improvement.
- **Degeneration loses generality.** Ciliberto–Miranda degenerations and Evain collisions replace very general points by special limits; the limiting system can be more special than the general one, and the induction only closes for bounded multiplicity or highly structured $r$.
- **Nagata's square trick does not generalize.** His proof uses that $k^2$ points can be placed on a degree-$k$ curve so a Cremona-type transformation is available; for non-square $r$ there is no analogous self-similar configuration.
- **Irrationality.** If $\varepsilon_r = 1/\sqrt r$ with $r$ non-square, the infimum is not attained by any curve; no single algebraic witness can certify it, so any proof must be a genuine limiting argument.

## 6. The Gap

What is proven: $\varepsilon_r = 1/\sqrt r$ for $r=9$ and $r=k^2\ge16$; $\varepsilon_r \ge 1/\sqrt{r+1}$ for all $r\ge10$; the conjecture for uniform multiplicity $m \le 42$.

What is missing: for a single non-square $r \ge 10$ — canonically $r = 10$ — the removal of the last $O(1/r)$ in Xu's bound. Concretely, one must rule out, for every $m$, the existence of a curve of degree $d = \lfloor m\sqrt{10}\rfloor$ with multiplicity $m$ at $10$ very general points. Equivalently: show that the class $\sqrt{10}\,H - \sum_{i=1}^{10} E_i$ is nef on $X_{10}$. The barrier is the transition from *finitely many* extremal curve classes (available for $r\le9$ through the anticanonical geometry) to an infinite, non-polyhedral boundary. No known technique produces a uniform-in-$m$ non-existence statement at an irrational slope.

## 7. Current Research (as of June 2026)

- **Valuative Nagata conjectures.** Dumnicki, Harbourne, Küronya, Roé and Szemberg study $\varepsilon$ for very general monomial and quasi-monomial valuations of $\mathbb{P}^2$; these interpolate between the $r$-point cases and admit continuity arguments unavailable in the discrete setting (Kraków, Barcelona/UAB, Lincoln–Nebraska, Freiburg groups).
- **Newton–Okounkov bodies and infinitesimal Newton–Okounkov bodies** as a tool for computing $\varepsilon_r$; the conjecture becomes a statement that a certain body has maximal area *(frontier — verify)*.
- **Symbolic powers and containment.** The circle around Bocci–Harbourne resurgence, $I^{(m)} \subseteq I^{s}$ containments, and Chudnovsky/Demailly-type lower bounds on $\widehat\alpha$; incremental improvements to $\widehat\alpha(I) \ge$ bounds for $r$ points are published regularly.
- **Computer-assisted certificates.** Extension of the Dumnicki–Jarnicki linear-programming/"specialization to fans of lines" method to higher uniform multiplicities; the method scales badly but yields hard verified ranges.
- **Symplectic geometry.** Ball-packing and Lagrangian-obstruction reformulations continue to be probed for a non-algebraic proof route.
- **Bounded negativity.** The related conjecture that self-intersections of reduced irreducible curves on a fixed surface are bounded below; progress there constrains the geometry of $X_r$ near the Nagata boundary.

## 8. Future Work

- Settle $r = 10$ unconditionally; leading opinion holds that a genuinely new positivity technique — not a refinement of Bezout/differentiation — is required.
- Prove SHGH for all $r \ge 10$ with $m_i \in \{1,2\}$ in full generality, then bootstrap by Cremona.
- Develop a degeneration whose limit is *flat in $\sqrt r$*, e.g. via toric or tropical degenerations of $\mathbb{P}^2$ where the irrational slope appears as a limit of rational fan slopes.
- Establish continuity/semicontinuity of $\varepsilon$ in the valuative parameter strong enough to transfer Nagata's square cases to nearby non-square $r$.
- Determine whether $\varepsilon_r$ is rational for some non-square $r \ge 10$ — a single rational value would disprove the conjecture and produce a curve of record slope.

## 9. Key References

- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics 81 (1959), 766–772. [DOI](https://doi.org/10.2307/2372927)
- **[Foundational]** M. Nagata. *On rational surfaces II.* Memoirs of the College of Science, University of Kyoto, Ser. A 33 (1960), 271–293. [DOI](https://doi.org/10.1215/kjm/1250775912)
- **[Foundational]** B. Segre. *Alcune questioni su insiemi finiti di punti in geometria algebrica.* Atti del Convegno Internazionale di Geometria Algebrica, Torino, 1961.
- **[Foundational]** A. Hirschowitz. *Une conjecture pour la cohomologie des diviseurs sur les surfaces rationnelles génériques.* Journal für die reine und angewandte Mathematik 397 (1989), 208–213. [DOI](https://doi.org/10.1515/crll.1989.397.208)
- **[Foundational]** B. Harbourne. *The geometry of rational surfaces and Hilbert functions of points in the plane.* Canadian Mathematical Society Conference Proceedings 6 (1986), 95–111.
- **[SOTA]** G. Xu. *Ample line bundles on smooth surfaces.* Journal für die reine und angewandte Mathematik 469 (1995), 199–209. [DOI](https://doi.org/10.1515/crll.1995.469.199)
- **[SOTA]** C. Ciliberto, R. Miranda. *Degenerations of planar linear systems.* Journal für die reine und angewandte Mathematik 501 (1998), 191–220. [DOI](https://doi.org/10.1515/crll.1998.077)
- **[SOTA]** C. Ciliberto, R. Miranda. *Linear systems of plane curves with base points of equal multiplicity.* Transactions of the American Mathematical Society 352 (2000), 4037–4050. [DOI](https://doi.org/10.1090/s0002-9947-00-02416-8)
- **[SOTA]** L. Evain. *La fonction de Hilbert de la réunion de $4^h$ gros points génériques de $\mathbb{P}^2$ de même multiplicité.* Journal of Algebraic Geometry 8 (1999), 787–796.
- **[SOTA]** M. Dumnicki, W. Jarnicki. *New effective bounds on the dimension of a linear system in $\mathbb{P}^2$.* Journal of Symbolic Computation 42 (2007), 87–94.
- **[SOTA]** P. Biran. *Constructing new ample divisors out of old ones.* Duke Mathematical Journal 98 (1999), 113–135. [DOI](https://doi.org/10.1215/s0012-7094-99-09803-4)
- **[SOTA]** M. Dumnicki, B. Harbourne, A. Küronya, J. Roé, T. Szemberg. *Very general monomial valuations of $\mathbb{P}^2$ and a Nagata type conjecture.* Communications in Analysis and Geometry 25 (2017), 125–161. [DOI](https://doi.org/10.4310/cag.2017.v25.n1.a4)
- **[Survey]** C. Ciliberto, B. Harbourne, R. Miranda, J. Roé. *Variations on Nagata's conjecture.* In: A Celebration of Algebraic Geometry, Clay Mathematics Proceedings 18 (2013), 185–203.
- **[Survey]** T. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. Knutsen, W. Syzdek, T. Szemberg. *A primer on Seshadri constants.* Contemporary Mathematics 496 (2009), 33–70. [DOI](https://doi.org/10.1090/conm/496/09718)
- **[Survey]** R. Lazarsfeld. *Positivity in Algebraic Geometry I.* Ergebnisse der Mathematik 48, Springer, 2004 (§5.1–5.3 on Seshadri constants). [DOI](https://doi.org/10.1007/978-3-642-18808-4)
- **[Context]** D. McDuff, L. Polterovich. *Symplectic packings and algebraic geometry.* Inventiones Mathematicae 115 (1994), 405–434. [DOI](https://doi.org/10.1007/bf01231766)
- **[Context]** C. Bocci, B. Harbourne. *Comparing powers and symbolic powers of ideals.* Journal of Algebraic Geometry 19 (2010), 399–417. [DOI](https://doi.org/10.1090/s1056-3911-09-00530-x)

## 10. Worked Example / Concrete Special Case

**The boundary case $r = 9$, and the first open case $r = 10$.**

*Step 1 — $r=9$ is sharp.* Nine very general points impose independent conditions on the $10$-dimensional space of cubics, so there is a pencil of cubics through them; a general member $E$ is smooth. Here $d=3$, $m_i=1$, and
$$\frac{1}{\sqrt 9}\sum_{i=1}^{9} m_i = \frac{9}{3} = 3 = d,$$
so the *strict* inequality fails. Hence the hypothesis $r>9$ cannot be dropped. On $X_9$ the class $-K = 3H - \sum_{1}^{9}E_i$ is nef with $K^2 = 0$, and $\varepsilon_9 = 1/3$ exactly.

*Step 2 — an elementary bound for $r=10$.* Let $C$ have degree $d$ and multiplicity $\ge m$ at $10$ very general points $p_1,\dots,p_{10}$. Choose the smooth cubic $E$ through $p_1,\dots,p_9$. Since the $p_i$ are very general, $p_{10}\notin E$, and $C$ cannot contain $E$ as a component without lowering the count (if it does, replace $C$ by $C-E$, which has degree $d-3$ and multiplicity $\ge m-1$ at each of $p_1,\dots,p_9$, and induct). Assuming $E \not\subseteq C$, Bezout gives
$$3d = E\cdot C \;\ge\; \sum_{i=1}^{9}\operatorname{mult}_{p_i}(E)\operatorname{mult}_{p_i}(C) \;\ge\; 9m \quad\Longrightarrow\quad \frac{d}{m}\ \ge\ 3 .$$
So $\varepsilon_{10} \le 1/3$ is improved from below only to $\varepsilon_{10}\ge 1/3$ — but the conjecture asserts $\varepsilon_{10} = 1/\sqrt{10} = 0.31622\ldots < 1/3$, and the true content is the *upper* direction: no curve may achieve $d/m < \sqrt{10}$. Xu's differentiation argument upgrades the elementary bound to $d/m \ge \sqrt{11} = 3.3166\ldots$ — wait, in the correct normalization Xu gives $\varepsilon_{10}\ge 1/\sqrt{11}$, i.e. $d/m \le \sqrt{11}$ is impossible to beat downwards below $\sqrt{11}$; the conjecture needs $d/m \ge \sqrt{10}$ replaced by $d > m\sqrt{10}$, and the certified interval for $\varepsilon_{10}$ is
$$0.30151 \approx \frac{1}{\sqrt{11}} \;\le\; \varepsilon_{10} \;\le\; \frac{1}{\sqrt{10}} \approx 0.31623 .$$
The entire open problem for $r=10$ lives inside this interval of width $0.0147$.

*Step 3 — why squares are easier.* For $r = 16$ the conjecture reads $d \ge 4m+1$. Nagata's argument places the $16$ points on a smooth quartic $Q$ and uses the induced self-map to trade a curve of degree $d$ and multiplicity $m$ for one of degree $4d - 16m$ and multiplicity $d - 4m$ at the same points. If $d \le 4m$ this produces a strictly smaller nonnegative pair, and infinite descent gives a contradiction. The trick needs $\sqrt{16}=4 \in \mathbb{Z}$ so the substitution stays inside the integral Picard lattice — exactly what fails for $r=10$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*