---
id: 03-geometry/arakelov-adjunction-conjecture
title: "Arakelov's Adjunction Formula Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Arakelov's Adjunction Formula Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/arakelov-adjunction-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Arakelov's *adjunction formula* itself — for a section $\sigma$ of an arithmetic surface, $(\sigma,\sigma)_{\mathrm{Ar}} = -\,(\sigma,\omega)_{\mathrm{Ar}}$ — is a theorem (Arakelov 1974). What is open is its **effective/quantitative form**: the conjecture that the arithmetic self-intersection $\omega^2_{\mathrm{Ar}}$ of the relative dualizing sheaf, which adjunction converts into heights of rational points, is bounded above by the arithmetic discriminant data of the surface. This is the arithmetic analogue of the Bogomolov–Miyaoka–Yau inequality, and is the form in which "Arakelov adjunction" enters Diophantine geometry.

**Conjecture (effective arithmetic adjunction).** Fix $g\ge 2$. There exist constants $c_1(g), c_2(g)$ such that for every number field $K$ and every *semistable* arithmetic surface $\pi:\mathcal{X}\to B=\operatorname{Spec}\mathcal{O}_K$ whose generic fibre is a smooth geometrically connected curve of genus $g$,
$$
\omega^2_{\mathrm{Ar}}(\mathcal X) \;\le\; c_1(g)\Big(\log\big|d_{K/\mathbb Q}\big| \;+\; \log N_{K/\mathbb Q}\,\mathfrak{n}_{\mathcal X}\Big) \;+\; c_2(g)\,[K:\mathbb Q],
$$
where $d_{K/\mathbb Q}$ is the absolute discriminant and $\mathfrak n_{\mathcal X}=\prod_{\mathfrak p}\mathfrak p^{\,\delta_{\mathfrak p}}$ the conductor ($\delta_{\mathfrak p}$ = number of nodes in the geometric fibre at $\mathfrak p$).

A complete solution requires either (i) a proof with explicitly computable $c_1,c_2$, or (ii) a family $\{\mathcal X_n\}$ of fixed genus with $\omega^2_{\mathrm{Ar}}(\mathcal X_n) / \big(\log|d_{K_n}| + \log N\mathfrak n_n + [K_n:\mathbb Q]\big) \to \infty$. Non-effective proofs do not count: by Parshin's covering construction the effective statement implies effective Mordell, effective Szpiro, and $abc$, so the constants are the content.

The complementary **lower** bound (effective Bogomolov: $\omega_a^2 \ge \varepsilon(g) > 0$ with $\varepsilon$ explicit) is also open over number fields and is treated here as the second half of the problem.

## 2. Mathematical Foundations

**Arithmetic surface.** $\pi:\mathcal X\to B=\operatorname{Spec}\mathcal O_K$ regular, flat, projective, of relative dimension $1$, with generic fibre $X/K$ smooth, geometrically connected, of genus $g\ge 2$. *Semistable* means every geometric fibre is reduced with at worst ordinary double points.

**Arakelov divisor.** $\widehat D = D + \sum_{\sigma:K\hookrightarrow\mathbb C} g_\sigma\,F_\sigma$, with $D$ a Weil divisor on $\mathcal X$ and $g_\sigma\in C^\infty(X_\sigma(\mathbb C))$ Green's data at each archimedean place.

**Canonical (Arakelov) metric.** On $X_\sigma(\mathbb C)$, take $\{\alpha_1,\dots,\alpha_g\}$ orthonormal for $\langle\alpha,\beta\rangle=\tfrac{i}{2}\int_{X_\sigma}\alpha\wedge\bar\beta$ and set
$$
\mu_{\mathrm{Ar}} \;=\; \frac{i}{2g}\sum_{k=1}^{g}\alpha_k\wedge\bar\alpha_k, \qquad \int_{X_\sigma}\mu_{\mathrm{Ar}}=1 .
$$
The Arakelov–Green function $g_\sigma(P,Q)$ is the unique solution of
$$
dd^c\, g_\sigma(P,\cdot) \;=\; \mu_{\mathrm{Ar}} - \delta_P, \qquad \int_{X_\sigma} g_\sigma(P,Q)\,\mu_{\mathrm{Ar}}(Q)=0 .
$$

**Intersection pairing.** For Arakelov divisors with disjoint generic support,
$$
(\widehat D,\widehat E)_{\mathrm{Ar}} \;=\; \sum_{\mathfrak p\subset\mathcal O_K} i_{\mathfrak p}(D,E)\log N\mathfrak p \;+\; \sum_{\sigma}\big(g_\sigma(D_\sigma,E_\sigma)+\text{Green terms}\big),
$$
a symmetric $\mathbb R$-valued bilinear form (Arakelov 1974; Faltings 1984).

**Adjunction (theorem).** For a section $\sigma:B\to\mathcal X$ with image $S$, the Arakelov-metrized $\omega_{\mathcal X/B}$ satisfies $\sigma^*\omega_{\mathrm{Ar}}\cong \mathcal O(-S)\big|_S$, hence
$$
(S,S)_{\mathrm{Ar}} + (S,\omega_{\mathrm{Ar}}) = 0,
\qquad\text{so}\qquad
h_{\omega}(P)\;=\;(S_P,\omega_{\mathrm{Ar}})\;=\;-\,(S_P,S_P)_{\mathrm{Ar}} .
$$
This is the mechanism converting a bound on $\omega^2$ into a height bound on rational points.

**Noether formula** (Faltings; Moret-Bailly 1989). For $\pi$ semistable,
$$
12\,\widehat{\deg}\,\pi_*\omega_{\mathrm{Ar}} \;=\; \omega^2_{\mathrm{Ar}} \;+\;\sum_{\mathfrak p}\delta_{\mathfrak p}\log N\mathfrak p \;+\; \sum_{\sigma}\delta_{\mathrm{Fal}}(X_\sigma) \;-\; 4g\,[K:\mathbb Q]\log(2\pi),
$$
with $\delta_{\mathrm{Fal}}$ Faltings' delta invariant. Since $\widehat{\deg}\,\pi_*\omega = [K:\mathbb Q]\,h_{\mathrm{Fal}}(X)$, the conjecture of §1 is equivalent (given control on $\delta_{\mathrm{Fal}}$) to an effective bound on the Faltings height by the conductor.

**Admissible pairing (Zhang 1993).** Replacing $\mu_{\mathrm{Ar}}$ by an admissible metric built from the reduction graphs $\Gamma_{\mathfrak p}$ gives $\omega_a$ with
$$
\omega^2_{\mathrm{Ar}} \;=\; \omega_a^2 \;+\; \sum_{\mathfrak p} \varepsilon(\Gamma_{\mathfrak p})\log N\mathfrak p, \qquad \varepsilon(\Gamma_{\mathfrak p})\ge 0 .
$$

## 3. History & State of the Art (SOTA)

- **1971–74.** S. Yu. Arakelov constructs the intersection theory and proves adjunction (Izv. Akad. Nauk 1974; ICM Vancouver 1974), motivated by his earlier proof of the geometric Shafarevich conjecture.
- **1984.** Faltings, *Calculus on arithmetic surfaces*: Riemann–Roch, the arithmetic Hodge index theorem, positivity $\omega^2_{\mathrm{Ar}}\ge 0$ for semistable surfaces, and the invariant $\delta_{\mathrm{Fal}}$.
- **1989–90.** Moret-Bailly proves the arithmetic Noether formula. Parshin shows an effective bound on $\omega^2$ (equivalently effective Szpiro) implies $abc$ and effective Mordell, via ramified covers; Szpiro states the discriminant–conductor conjecture in the same Astérisque volume.
- **1993–98.** Zhang's admissible pairing; the Bogomolov conjecture is proved *non-effectively* by Ullmo and Zhang (Annals 147, 1998) using equidistribution — the constants are inexplicit, so effective adjunction is untouched.
- **1997–2014.** Exact asymptotics for $\omega^2_{\mathrm{Ar}}$ on modular curves (Abbes–Ullmo; Michel–Ullmo; Mayer), the only infinite families where $\omega^2$ is computed.
- **2011.** Cinkir proves Zhang's graph-invariant conjecture and thereby the **effective Bogomolov conjecture over function fields** of characteristic $0$.
- **2017.** Wilms obtains sharp bounds for $\delta_{\mathrm{Fal}}$ and the Zhang–Kawazumi invariant $\varphi$ in terms of the Arakelov–Green function, tightening the archimedean side of Noether.

Status: over function fields the analogous inequality is a theorem (Arakelov, Parshin, Beauville; geometric Szpiro $\deg\Delta\le 6(2q-2+s)$). Over number fields, no upper bound of the conjectured shape is known for any single genus $g\ge2$ in full generality.

## 4. Partial Results / Verified Cases

- **Positivity.** $\omega^2_{\mathrm{Ar}}\ge 0$ for all semistable arithmetic surfaces of genus $\ge2$ (Faltings 1984); $\omega_a^2\ge 0$ with equality characterised (Zhang 1993).
- **Function fields, all $g\ge2$, char $0$.** Full effective two-sided adjunction: $\omega^2 \le (2g-2)\big(2q-2+s\big)\cdot O(1)$ and effective Bogomolov (Cinkir, *Invent. Math.* 183, 2011). Elliptic case $g=1$: $\deg\Delta\le 6(2q-2+s)$, sharp for Beauville's four-singular-fibre families.
- **Modular curves.** $X_0(N)$, $N$ squarefree: $\omega^2_{\mathrm{Ar}} = 3g\log N + o(g\log N)$ as $N\to\infty$ (Abbes–Ullmo 1997, completed by Michel–Ullmo 1998). $X_1(N)$: analogous asymptotics (Mayer 2014). These are consistent with the conjecture with $c_1(g)\approx 3g$.
- **Genus 2.** Green's functions, $\delta_{\mathrm{Fal}}$ and $\omega^2$ computed explicitly in terms of Igusa invariants for hyperelliptic models (Bost 1987; Bost–Mestre–Moret-Bailly 1990; de Jong 2004), verifying the bound numerically for the tested families.
- **Cyclic covers.** Szpiro's *small points* conjecture — a consequence of effective adjunction — is proved for cyclic covers of $\mathbb P^1$ (Javanpeykar–von Känel, *Doc. Math.* 2015), and Szpiro's discriminant conjecture holds for elliptic curves with a rational point of order $\ge 5$-type constraints (von Känel).
- **Archimedean side.** $\delta_{\mathrm{Fal}}(X)\ge -c(g)$ with explicit $c(g)$, and $\varphi(X)\ge 0$ (Wilms 2017), removing one of the three unbounded terms in Noether.

## 5. Principal Obstacles

- **No arithmetic Yau theorem.** The geometric BMY inequality $c_1^2\le 3c_2$ comes from the Kähler–Einstein metric and Chern-class positivity. Arakelov geometry has $\widehat{c}_1,\widehat{c}_2$ but no arithmetic Aubin–Yau existence theorem, and $\widehat{c}_2$ of the relative tangent complex has no known sign. Every attempted transplant of the differential-geometric proof stalls here.
- **Noether is an identity, not an inequality.** It trades $\omega^2$ for $h_{\mathrm{Fal}}$; bounding $h_{\mathrm{Fal}}$ by the conductor *is* Szpiro's conjecture. The circularity is genuine, not presentational.
- **Cinkir's function-field proof is non-archimedean.** It hinges on invariants $\varphi(\Gamma),\lambda(\Gamma)$ of finite metric graphs, for which combinatorial induction on the number of edges works. The archimedean fibre is a Riemann surface, not a graph; its counterpart $\varphi(X_\sigma)$ resists the induction because there is no "edge count" to induct on.
- **Degeneration is uncontrolled.** As $X_\sigma$ approaches the boundary of $\mathcal M_g$, $g_\sigma(P,Q)$ and $\delta_{\mathrm{Fal}}$ blow up logarithmically; upper bounds uniform over all of $\mathcal M_g(\mathbb C)$ require estimates on theta functions near the boundary that are known only for $g\le 2$ and in special strata.
- **No arithmetic ampleness criterion.** Faltings' Riemann–Roch gives $\widehat{h}^0$ lower bounds only when $\omega^2$ is already known to be large; one cannot bootstrap from sections.
- **Equidistribution is inherently ineffective.** The Ullmo–Zhang proof uses a compactness/limit argument on measures; extracting explicit constants would need effective equidistribution rates for small points, unavailable.

## 6. The Gap

Proven: $0\le\omega^2_{\mathrm{Ar}}$ for all semistable surfaces; exact values for modular families; the full inequality over function fields; the lower bound with *inexplicit* constants over number fields. Conjectured: a **uniform upper bound linear in $\log|d_K| + \log N\mathfrak n$ with a constant depending only on $g$**.

The precise missing step is an archimedean estimate of the form
$$
\delta_{\mathrm{Fal}}(X_\sigma) \;\ge\; -\,c(g)\,\log\!\big(\text{distance to } \partial\overline{\mathcal M_g}\big) \;-\; c'(g)
$$
*matched* to a bound on $\widehat{\deg}\,\pi_*\omega$ by the conductor — equivalently, an arithmetic $\widehat c_2\ge 0$ statement. Nothing weaker suffices: any bound with $c_1$ depending on $\mathcal X$ rather than only on $g$ leaves Szpiro, and hence $abc$, untouched.

## 7. Current Research (as of June 2026)

- **Adelic line bundles.** Yuan–Zhang's arithmetic Hodge index theorem (*Math. Ann.* 367, 2017) and the subsequent adelic-line-bundle framework over quasi-projective bases give a common language for the function-field and number-field cases; the hope is to import Cinkir's induction through the non-archimedean part and isolate the archimedean deficit (Columbia, Berkeley).
- **Archimedean invariants.** Wilms and collaborators (Mainz) continue sharpening $\delta_{\mathrm{Fal}}$, $\varphi$ and $\lambda$ bounds via Riemann theta asymptotics; a uniform genus-$g$ lower bound for $\delta_{\mathrm{Fal}}$ in terms of the Arakelov–Green diameter is the target *(frontier — verify)*.
- **Tropical/metric-graph Arakelov theory.** Baker–Rumely-style potential theory on Berkovich curves, used by Cinkir and Yamaki, is being pushed toward higher-dimensional bases (Kyoto).
- **Effective Mordell computations.** von Känel–Matschke's height-bound machinery for $S$-unit and Mordell equations gives numerical instances against which conjectural $c_1(g)$ can be tested.
- **IUT-based claims.** Mochizuki's inter-universal Teichmüller theory asserts an inequality equivalent to $abc$ and hence to a form of effective adjunction; the proof remains disputed by a substantial part of the community and is not used as a premise here *(frontier — verify)*.

## 8. Future Work

- Prove $\widehat c_2 \ge 0$ (or any effective lower bound) for the relative tangent complex of a semistable arithmetic surface — the direct arithmetic BMY route advocated by Parshin and Soulé.
- Extend Cinkir's edge-induction by treating the archimedean fibre as a limit of metric graphs under maximal degeneration, making the induction uniform in the "hybrid" Berkovich–complex space.
- Compute $\omega^2_{\mathrm{Ar}}$ for a second infinite non-modular family (Fermat curves, Shimura curves) to test whether $c_1(g)=3g$ is asymptotically sharp.
- Effectivize equidistribution of small points, which would yield explicit $\varepsilon(g)$ in the lower half of the problem.
- Settle genus $2$ unconditionally: all archimedean invariants are explicit there, so only the arithmetic input is missing.

## 9. Key References

- **[Foundational]** S. Yu. Arakelov. *An intersection theory for divisors on an arithmetic surface.* Izv. Akad. Nauk SSSR Ser. Mat. **38** (1974), 1179–1192.
- **[Foundational]** G. Faltings. *Calculus on arithmetic surfaces.* Annals of Mathematics **119** (1984), 387–424. [DOI](https://doi.org/10.2307/2007043)
- **[Foundational]** L. Moret-Bailly. *La formule de Noether pour les surfaces arithmétiques.* Inventiones Mathematicae **98** (1989), 491–498. [DOI](https://doi.org/10.1007/bf01393833)
- **[Foundational]** A. N. Parshin. *Application of ramified coverings in the theory of Diophantine equations.* Math. USSR Sbornik **66** (1990), 249–264. [DOI](https://doi.org/10.1070/sm1990v066n01abeh001171)
- **[Foundational]** L. Szpiro. *Discriminant et conducteur des courbes elliptiques.* Astérisque **183** (1990), 7–18.
- **[Foundational]** S. Zhang. *Admissible pairing on a curve.* Inventiones Mathematicae **112** (1993), 171–193. [DOI](https://doi.org/10.1007/bf01232429)
- **[SOTA]** Z. Cinkir. *Zhang's conjecture and the effective Bogomolov conjecture over function fields.* Inventiones Mathematicae **183** (2011), 517–562. [DOI](https://doi.org/10.1007/s00222-010-0282-7)
- **[SOTA]** R. Wilms. *New results on the Arakelov–Green's function and the delta invariant.* Inventiones Mathematicae **209** (2017), 481–539.
- **[SOTA]** X. Yuan, S. Zhang. *The arithmetic Hodge index theorem for adelic line bundles.* Mathematische Annalen **367** (2017), 1123–1171. [DOI](https://doi.org/10.1007/s00208-016-1414-1)
- **[SOTA]** A. Abbes, E. Ullmo. *Auto-intersection du dualisant relatif des courbes modulaires $X_0(N)$.* J. reine angew. Math. **484** (1997), 1–70.
- **[SOTA]** P. Michel, E. Ullmo. *Points de petite hauteur sur les courbes modulaires $X_0(N)$.* Inventiones Mathematicae **131** (1998), 645–674. [DOI](https://doi.org/10.1007/s002220050216)
- **[SOTA]** H. Mayer. *Self-intersection of the relative dualizing sheaf on modular curves $X_1(N)$.* J. Théor. Nombres Bordeaux **26** (2014), 111–161.
- **[SOTA]** A. Javanpeykar, R. von Känel. *Szpiro's small points conjecture for cyclic covers.* Documenta Mathematica **20** (2015). [DOI](https://doi.org/10.4171/dm/475)
- **[Partial]** E. Ullmo. *Positivité et discrétion des points algébriques des courbes.* Annals of Mathematics **147** (1998), 167–179; S. Zhang, *Equidistribution of small points on abelian varieties*, ibid., 159–165.
- **[Survey]** C. Soulé. *Géométrie d'Arakelov des surfaces arithmétiques.* Séminaire Bourbaki, exp. 713, Astérisque **177–178** (1989), 327–343.
- **[Survey / Book]** S. Lang. *Introduction to Arakelov Theory.* Springer-Verlag, 1988. [DOI](https://doi.org/10.1007/978-1-4612-1031-3)
- **[Explicit]** J.-B. Bost, J.-F. Mestre, L. Moret-Bailly. *Sur le calcul explicite des « petits points » des courbes de genre 2.* Astérisque **183** (1990), 69–105.

## 10. Worked Example / Concrete Special Case

**Genus 1 is vacuous; Parshin's cover makes it sharp.** Take $E/\mathbb Q$ of conductor $N=11$, the curve $X_0(11)$:
$$
y^2 + y = x^3 - x^2 - 10x - 20, \qquad \Delta_{\min} = -11^5, \qquad N_E = 11 .
$$
$E$ is semistable with multiplicative reduction only at $11$, so the minimal regular model $\mathcal E\to\operatorname{Spec}\mathbb Z$ has $\delta_{11}=v_{11}(\Delta)=5$ nodes and $\delta_p=0$ elsewhere. Because $g=1$, $\omega_{\mathcal E/\mathbb Z}\cong\pi^*\pi_*\omega$, hence
$$
\omega^2_{\mathrm{Ar}} = (\pi^*\lambda)^2 = 0 ,
$$
and the conjectured inequality is trivially true. Noether then reads
$$
12\,h_{\mathrm{Fal}}(E) \;=\; 0 + 5\log 11 + \delta_{\mathrm{Fal}}(E_{\mathbb C}) - 4\log(2\pi),
$$
so all arithmetic content sits in the discriminant term $5\log 11 = 11.99$ against $\log N_E = 2.398$. The **Szpiro ratio** is
$$
\sigma(E)=\frac{\log|\Delta_{\min}|}{\log N_E}=\frac{5\log 11}{\log 11}=5 .
$$

**Where the conjecture bites.** Parshin's construction attaches to $E$ a semistable curve $Y$ of genus $g=2$ (a double cover of $E$ branched at $2$-torsion, over a field $K$ of bounded degree and controlled discriminant) whose arithmetic surface $\mathcal Y\to\operatorname{Spec}\mathcal O_K$ satisfies
$$
\omega^2_{\mathrm{Ar}}(\mathcal Y) \;\ge\; a\,\log|\Delta_{\min}(E)| \;-\; b\big(\log N_E + 1\big)
$$
for absolute $a>0$, $b$. Feeding in the conjecture's upper bound $\omega^2_{\mathrm{Ar}}(\mathcal Y)\le c_1(2)\big(\log|d_K|+\log N\mathfrak n_{\mathcal Y}\big)+c_2(2)[K:\mathbb Q]$, and using $\log|d_K|+\log N\mathfrak n_{\mathcal Y} = O(\log N_E)$, yields
$$
\log|\Delta_{\min}(E)| \;\le\; C_1\log N_E + C_2 ,
$$
i.e. Szpiro's conjecture with explicit constants, and $\sigma(E)\le C_1$ for every semistable $E/\mathbb Q$. Conjecturally $C_1 = 6+\varepsilon$; the conductor-$11$ curve gives $\sigma=5$, while the largest known ratios (Nitaj's tables) reach $\approx 8.9$ for non-semistable-normalised variants — no example exceeds $6+\varepsilon$ in the semistable normalisation. The gap between "$\omega^2\ge0$" (known) and "$\omega^2\le c_1\log N\mathfrak n$" (conjectured) is exactly the gap between knowing nothing and knowing $abc$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*