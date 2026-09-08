---
id: 03-geometry/obata-conjecture
title: "Obata Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Obata Conjecture (Projective Lichnerowicz–Obata Conjecture)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/obata-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(M^n, g)$ be a connected, complete Riemannian manifold, $n \ge 2$. A diffeomorphism $\varphi: M \to M$ is a **projective transformation** if it maps geodesics to geodesics as *unparametrized* curves. Write $\mathrm{Proj}(M,g)$ for the group of such maps, $\mathrm{Aff}(M,g)$ for those preserving the Levi-Civita connection, and $\mathrm{Iso}(M,g)$ for isometries; $\mathrm{Iso} \subseteq \mathrm{Aff} \subseteq \mathrm{Proj}$.

**Conjecture (Obata; Lichnerowicz, ca. 1970).** If the connected component $\mathrm{Proj}^0(M,g)$ does not consist of affine transformations, then $(M,g)$ has constant positive sectional curvature; i.e. after rescaling $g$, $(M,g)$ is the round sphere $S^n$ or the real projective space $\mathbb{R}P^n$ with the standard metric.

The infinitesimal form: if a complete $(M,g)$ admits a **projective vector field** that is not affine, then $(M,g)$ is a round sphere or $\mathbb{R}P^n$ up to scaling.

A complete proof must (i) handle all dimensions $n \ge 2$, (ii) assume only geodesic completeness (not compactness, not analyticity), and (iii) produce the constant-curvature conclusion globally, not just on an open dense set. A disproof would exhibit a complete Riemannian metric of non-constant curvature with an essential one-parameter projective group.

**Status.** Proven for Riemannian signature (Matveev 2005, 2007). The pseudo-Riemannian analogue remains open in general and is the live part of the problem.

## 2. Mathematical Foundations

**Projective equivalence.** Two metrics $g, \bar g$ on $M$ are projectively equivalent iff their Levi-Civita connections satisfy
$$\bar\Gamma^k_{ij} = \Gamma^k_{ij} + \delta^k_i \phi_j + \delta^k_j \phi_i, \qquad \phi_i = \partial_i \phi, \quad \phi = \tfrac{1}{2(n+1)} \log \left| \frac{\det \bar g}{\det g} \right| .$$
Setting $\varphi = 0$ recovers affine equivalence.

**Sinjukov linearization.** The nonlinear condition above becomes linear under the substitution
$$a_{ij} = e^{2\phi}\, \bar g^{pq} g_{pi} g_{qj}, \qquad e^{2\phi} = \left| \frac{\det \bar g}{\det g}\right|^{1/(n+1)} ,$$
where $a$ is a $g$-symmetric, nondegenerate $(0,2)$-tensor solving
$$\nabla_k a_{ij} = \lambda_i g_{jk} + \lambda_j g_{ik}, \qquad \lambda_i = \tfrac12 \partial_i \big(\mathrm{tr}_g\, a\big). \tag{S}$$
The **degree of mobility** $D(g)$ is the dimension of the solution space of (S); $D(g) \ge 1$ always ($a = g$). $D(g) \ge 2$ iff $g$ admits a nontrivially projectively equivalent metric.

**Projective vector fields.** $v$ is projective iff
$$\mathcal{L}_v \Gamma^k_{ij} = \delta^k_i \psi_j + \delta^k_j \psi_i$$
for some 1-form $\psi = d\psi_0$; $v$ is affine iff $\psi \equiv 0$.

**Obata's equation.** A nonconstant $f \in C^\infty(M)$ on a complete $(M,g)$ with
$$\nabla_i \nabla_j f = -K f\, g_{ij}, \qquad K > 0,$$
forces $(M,g)$ to be the round sphere of radius $1/\sqrt{K}$ (Obata 1962).

**Gallot–Tanno equation.** The third-order equation
$$\nabla_k \nabla_j \nabla_i f = -K\big(2 \nabla_i f\, g_{jk} + \nabla_j f\, g_{ik} + \nabla_k f\, g_{ij}\big) \tag{T}$$
on a complete Riemannian $(M,g)$ with $K>0$ and $f$ nonconstant implies $(M,g)$ is the round sphere of curvature $K$ (Tanno 1978; Gallot 1979). Equation (T) is the engine of the proof: closing the prolongation of (S) when $D(g) \ge 3$ produces exactly (T) for $f = \mathrm{tr}\,a$.

**Local model.** Geodesics of $S^n \subset \mathbb{R}^{n+1}$ are great circles; central (gnomonic) projection sends them to straight lines in $\mathbb{R}^n$, so $PGL(n+1,\mathbb{R})$ acts on $S^n/\pm$ by projective transformations, giving $\dim \mathrm{Proj}(\mathbb{R}P^n) = n(n+2) > \dim \mathrm{Iso} = \binom{n+1}{2}$. This is the unique Riemannian exception.

## 3. History & State of the Art (SOTA)

- **1865 — Beltrami.** Local classification in dimension 2 of metrics whose geodesics go to straight lines; the sphere singled out.
- **1896 — Levi-Civita.** Local normal form for pairs of projectively equivalent Riemannian metrics.
- **1950s — Solodovnikov, Sinjukov.** Solodovnikov proved the conjecture for real-analytic metrics on complete simply connected manifolds of dimension $\ge 3$ admitting an essential projective group. Sinjukov's linearization (S) and his 1979 monograph became the standard toolkit.
- **1958–1971 — Lichnerowicz and Obata.** Lichnerowicz's *Géométrie des groupes de transformations* posed the conformal analogue; Obata's 1971 BAMS announcement stated the family of "conformal/projective essential group $\Rightarrow$ sphere" conjectures. The conformal case was settled by Ferrand (1971, 1996) and Schoen (1995); the projective case stayed open.
- **1978–1979 — Tanno, Gallot.** The third-order rigidity theorem (T), later the pivot of the projective proof.
- **2005 — Matveev.** Dimension 2 settled for complete metrics (*Comment. Math. Helv.* 80).
- **2007 — Matveev.** Full Riemannian proof in all dimensions for complete metrics (*J. Differential Geom.* 75), by splitting on $D(g) = 2$ versus $D(g) \ge 3$.
- **2009–2012 — pseudo-Riemannian program.** Kiosak–Matveev handle complete Einstein metrics and degree of mobility $\ge 3$; Matveev–Rosemann prove the Kähler (Yano–Obata) analogue.
- **2016 — Zeghib.** Discrete projective groups on closed Riemannian manifolds.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$, complete Riemannian | Conjecture true | Matveev 2005 |
| $n \ge 2$, closed Riemannian | Conjecture true | Matveev 2007 |
| $n \ge 2$, complete Riemannian, any $D(g)$ | Conjecture true (full theorem) | Matveev 2007 |
| Real-analytic, complete, simply connected, $n \ge 3$ | True | Solodovnikov 1956 |
| Complete Einstein, any signature, $n \ge 3$ | Geodesically rigid: projectively equivalent $\Rightarrow$ affinely equivalent, unless constant curvature | Kiosak–Matveev 2009 |
| Pseudo-Riemannian, $n \ge 3$, $D(g) \ge 3$ | Conjecture true | Kiosak–Matveev 2010 |
| Closed pseudo-Riemannian, Gallot–Tanno step | Extension of (T) to indefinite signature | Matveev–Mounoud 2010 |
| Kähler $(M^{2n}, g, J)$ closed, c-projective (holomorph-projective) transformations | Yano–Obata conjecture true: $\Rightarrow (\mathbb{C}P^n, g_{FS})$ | Matveev–Rosemann 2012 |
| Closed Kähler, degree of mobility $\ge 3$ | Only $(\mathbb{C}P^n, g_{FS})$ | Fedorova–Kiosak–Matveev–Rosemann 2012 |
| Discrete $\mathrm{Proj}$ on closed Riemannian | $\mathrm{Proj}/\mathrm{Aff}$ finite unless round | Zeghib 2016 |

**Open sub-cases:** complete Lorentzian and general pseudo-Riemannian metrics with $D(g) = 2$; complete (non-closed) pseudo-Riemannian manifolds without Einstein or analyticity assumptions.

## 5. Principal Obstacles

- **Loss of ellipticity/positivity in indefinite signature.** The Riemannian proof integrates along geodesics and uses that eigenvalues of $a$ are real with $g$-orthogonal eigenspaces. In signature $(p,q)$ the endomorphism $A = g^{-1}a$ may have complex eigenvalues and non-trivial Jordan blocks, so the local normal forms (Levi-Civita's splitting) fail wholesale.
- **The $D(g)=2$ case has no closed prolongation.** When the degree of mobility is exactly 2, the system (S) does not prolong to the Gallot–Tanno equation, so the sphere-rigidity engine is unavailable. Matveev's Riemannian argument replaces it with a delicate ODE analysis of the eigenvalue functions of $A$ along complete geodesics — an argument that uses completeness of *Riemannian* geodesics (metric completeness, Hopf–Rinow) which has no pseudo-Riemannian counterpart.
- **Hopf–Rinow failure.** Geodesic completeness in indefinite signature does not give metric completeness, bounded geometry, or divergence of the exponential map; compactness arguments and the escape-to-infinity contradictions used in the Riemannian case simply do not apply.
- **Non-analyticity.** Solodovnikov-type arguments propagate a local conclusion by analytic continuation. For smooth metrics the singular set where the eigenvalue multiplicities of $A$ jump is only closed with empty interior; controlling behaviour across it requires global integrability arguments rather than local PDE.
- **Curvature obstructions are too weak.** The integrability conditions of (S) constrain $R$ only through $W$-type projective curvature; for $n \ge 3$ these do not force constant curvature pointwise, so no purely algebraic shortcut exists.

## 6. The Gap

Riemannian: no gap — the conjecture is a theorem (Matveev 2007). The remaining boundary is the signature.

Precisely: for complete pseudo-Riemannian $(M^n,g)$, $n\ge 3$, the statement is proven when $D(g) \ge 3$ (Kiosak–Matveev 2010), when $g$ is Einstein, and in the closed Kähler c-projective setting. The unresolved step is the **$D(g)=2$ indefinite case**: given a two-dimensional space of solutions of (S) and a non-affine projective vector field, show that geodesic completeness forces constant curvature. The technical crux is a substitute for the Riemannian ODE argument along complete geodesics that tolerates (a) complex-conjugate eigenvalues of $A$, (b) Jordan blocks, and (c) null directions where $\mathrm{tr}\,a$ is not controlled by arclength. No known tool bridges this.

## 7. Current Research (as of June 2026)

- **Jena (Matveev's group)** remains the centre of the projective-metrization program: degree-of-mobility stratification, c-projective geometry, and metrizability of projective structures.
- **c-projective geometry** (Calderbank, Eastwood, Matveev, Neusser) recasts (S) as a BGG (Bernstein–Gelfand–Gelfand) first-BGG operator on a parabolic geometry of type $SL(n+1,\mathbb{R})/P_1$; the conjecture becomes a statement about mobility of normal solutions. This is the main structural reformulation gaining traction.
- **Lorentzian sub-case.** Work combining causal structure with the eigenvalue ODEs aims at complete Lorentzian metrics with $D(g)=2$ *(frontier — verify)*.
- **Integrable systems link.** Projectively equivalent metrics yield commuting quadratic integrals of the geodesic flow (Topalov–Matveev); superintegrability arguments are being used to constrain the $D=2$ case *(frontier — verify)*.
- **Sub-Riemannian and Finsler analogues** (Zeghib; Matveev's Finsler papers) test how far the rigidity persists outside the Riemannian category.

## 8. Future Work

1. Build a signature-independent replacement for the Gallot–Tanno theorem valid for geodesically complete, non-compact indefinite metrics.
2. Classify the local normal forms of $A = g^{-1}a$ with Jordan blocks and complex eigenvalues in the $D(g)=2$ case, then determine which extend to geodesically complete metrics.
3. Settle the Lorentzian conjecture first; the causal structure gives a preferred cone geometry absent in higher signature.
4. Push the BGG/parabolic formulation to a curved-orbit decomposition theorem, which would make the conclusion a statement about holonomy reduction of the projective tractor connection.
5. Extend the discrete-group results (Zeghib) from closed to complete manifolds.

## 9. Key References

- **[Foundational]** M. Obata. *Certain conditions for a Riemannian manifold to be isometric with a sphere.* Journal of the Mathematical Society of Japan 14 (1962), 333–340. [DOI](https://doi.org/10.2969/jmsj/01430333)
- **[Foundational]** M. Obata. *The conjectures on conformal transformations of Riemannian manifolds.* Bulletin of the American Mathematical Society 77 (1971), 269–270. [DOI](https://doi.org/10.4310/jdg/1214430407)
- **[Foundational]** A. Lichnerowicz. *Géométrie des groupes de transformations.* Dunod, Paris, 1958.
- **[Foundational]** E. Beltrami. *Risoluzione del problema: riportare i punti di una superficie sopra un piano in modo che le linee geodetiche vengano rappresentate da linee rette.* Annali di Matematica Pura ed Applicata 7 (1865), 185–204. [DOI](https://doi.org/10.1007/bf03198517)
- **[Foundational]** N. S. Sinjukov. *Geodesic Mappings of Riemannian Spaces.* Nauka, Moscow, 1979.
- **[Foundational]** S. Tanno. *Some differential equations on Riemannian manifolds.* Journal of the Mathematical Society of Japan 30 (1978), 509–531. [DOI](https://doi.org/10.2969/jmsj/03030509)
- **[Foundational]** S. Gallot. *Équations différentielles caractéristiques de la sphère.* Annales scientifiques de l'ENS 12 (1979), 235–267. [DOI](https://doi.org/10.24033/asens.1366)
- **[SOTA]** V. S. Matveev. *Lichnerowicz–Obata conjecture in dimension two.* Commentarii Mathematici Helvetici 80 (2005), 541–570. [DOI](https://doi.org/10.4171/cmh/25)
- **[SOTA]** V. S. Matveev. *Proof of the projective Lichnerowicz–Obata conjecture.* Journal of Differential Geometry 75 (2007), no. 3, 459–502. [DOI](https://doi.org/10.4310/jdg/1175266281)
- **[SOTA]** V. Kiosak, V. S. Matveev. *Complete Einstein metrics are geodesically rigid.* Communications in Mathematical Physics 289 (2009), 383–400. [DOI](https://doi.org/10.1007/s00220-008-0719-7)
- **[SOTA]** V. Kiosak, V. S. Matveev. *Proof of the projective Lichnerowicz conjecture for pseudo-Riemannian metrics with degree of mobility greater than two.* Communications in Mathematical Physics 297 (2010), 401–426. [DOI](https://doi.org/10.1007/s00220-010-1037-4)
- **[SOTA]** V. S. Matveev, S. Rosemann. *Proof of the Yano–Obata conjecture for holomorph-projective transformations.* Journal of Differential Geometry 92 (2012), no. 2, 221–261. [DOI](https://doi.org/10.4310/jdg/1352297807)
- **[SOTA]** A. Fedorova, V. Kiosak, V. S. Matveev, S. Rosemann. *The only Kähler manifold with degree of mobility at least 3 is $(\mathbb{C}P(n), g_{Fubini-Study})$.* Proceedings of the London Mathematical Society 105 (2012), 153–188.
- **[SOTA]** A. Zeghib. *On discrete projective transformation groups of Riemannian manifolds.* Advances in Mathematics 297 (2016), 26–53. [DOI](https://doi.org/10.1016/j.aim.2016.04.002)
- **[Survey]** D. M. J. Calderbank, M. G. Eastwood, V. S. Matveev, K. Neusser. *C-projective geometry.* Memoirs of the American Mathematical Society, 2021.
- **[Survey]** J. Ferrand. *The action of conformal transformations on Riemannian manifolds.* Mathematische Annalen 304 (1996), 277–291. (Conformal analogue.)
- **[Survey]** R. Schoen. *On the conformal and CR automorphism groups.* Geometric and Functional Analysis 5 (1995), 464–481. [DOI](https://doi.org/10.1007/978-3-0348-9102-8_13)

## 10. Worked Example / Concrete Special Case

**The unique exception, computed.** Take $S^n = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ with the round metric $g$, $K=1$.

*Step 1 — Gnomonic chart.* Project the upper hemisphere from the origin onto the affine plane $\{x_{n+1}=1\}$: $u \in \mathbb{R}^n \mapsto (u,1)/\sqrt{1+|u|^2}$. Pulling back $g$ gives
$$g = \frac{\langle du, du\rangle}{1+|u|^2} - \frac{\langle u, du\rangle^2}{(1+|u|^2)^2}.$$
Great circles are intersections of $S^n$ with 2-planes through $0$, whose images are straight lines in $\mathbb{R}^n$. So in this chart **geodesics are straight lines**, and every projective map of $\mathbb{R}P^n$ preserves them.

*Step 2 — An essential projective flow.* Let $\varphi_t(u) = e^{t} u$. Straight lines map to straight lines, so $\varphi_t \in \mathrm{Proj}(S^n/\pm, g)$. But $\varphi_t^* g \ne g$ for $t \ne 0$: at $u = 0$, $g_0 = \langle\cdot,\cdot\rangle$ and $(\varphi_t^*g)_0 = e^{2t}\langle\cdot,\cdot\rangle$. The flow is not affine either, since $\varphi_t^*g$ has different (constant) curvature $e^{-2t}$, and a non-isometric homothety of a complete metric of nonzero curvature cannot preserve the connection while the metrics differ by a non-constant conformal factor in this chart. Explicitly, the generating vector field $v = u^i \partial_i$ satisfies $\mathcal{L}_v \Gamma^k_{ij} = \delta^k_i \psi_j + \delta^k_j \psi_i$ with $\psi \ne 0$. Hence $\dim \mathrm{Proj}^0 = \dim PGL(n+1,\mathbb{R}) = n(n+2)$, strictly larger than $\dim \mathrm{Iso} = n(n+1)/2$.

*Step 3 — Why nothing else works (the rigidity mechanism).* Suppose $(M^n,g)$ complete admits a solution $a$ of (S) with $f := \mathrm{tr}_g\, a$ nonconstant and $D(g) \ge 3$. Prolonging (S) twice gives $\nabla_i \lambda_j = \mu\, g_{ij} + K a_{ij}$ and $\nabla_i \mu = 2K\lambda_i$ for a constant $K$; eliminating yields exactly the Tanno equation
$$\nabla_k\nabla_j\nabla_i f = -K\big(2\nabla_i f\, g_{jk} + \nabla_j f\, g_{ik} + \nabla_k f\, g_{ij}\big).$$
For $K > 0$ and $g$ complete Riemannian, Gallot–Tanno forces $(M,g) \cong S^n(1/\sqrt{K})$. For $K \le 0$ completeness forces $f$ constant (integrate $\nabla\nabla f$ along a unit-speed geodesic: $h(t) = f(\gamma(t))$ satisfies $h''' + 4Kh' = 0$, whose solutions are unbounded for $K \le 0$ unless $h' \equiv 0$, contradicting boundedness of $f$ on compact sets after a Hopf–Rinow argument).

*Step 4 — Sphere check.* On $S^n$ take $f(x) = x_{n+1}$. Then $\nabla_i\nabla_j f = -f g_{ij}$, i.e. Obata's equation with $K=1$, and $\Delta f = -n f$: $f$ is the first spherical harmonic. So the round sphere realizes the equality case, and the corresponding $a_{ij} = c\, g_{ij} + \nabla_i\nabla_j f + f g_{ij}$-type solutions span a space of dimension $n+2 \ge 3$ — the maximal degree of mobility. This is precisely the configuration the conjecture asserts is unique.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*