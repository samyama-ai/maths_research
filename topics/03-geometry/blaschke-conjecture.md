---
id: 03-geometry/blaschke-conjecture
title: "Blaschke Conjecture on Wiedersehen Manifolds"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Blaschke Conjecture on Wiedersehen Manifolds

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/blaschke-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M,g)$ be a compact connected Riemannian manifold without boundary. Call $(M,g)$ a **Blaschke manifold** if for every $p \in M$ the cut locus $\mathrm{Cut}(p)$ is at constant distance from $p$ — equivalently, the injectivity radius equals the diameter.

**Blaschke conjecture.** Every Blaschke manifold is isometric, up to scaling, to a compact rank-one symmetric space (CROSS) with its canonical metric:
$$S^n,\quad \mathbb{RP}^n,\quad \mathbb{CP}^n,\quad \mathbb{HP}^n,\quad \mathbb{CaP}^2 .$$

The **Wiedersehen** case is the extreme one: $(M,g)$ is a *Wiedersehen manifold* if for each $p$ there is a point $A(p) \neq p$ such that every geodesic issuing from $p$ passes through $A(p)$ (i.e. $\mathrm{Cut}(p) = \{A(p)\}$ is a single point). Blaschke's original question — every Wiedersehen manifold is a round sphere — is the sphere case.

A complete solution means: a proof that the Blaschke condition forces constant-curvature-1-type rigidity in each of the five models, or a counterexample — a Blaschke metric on some manifold not isometric to a CROSS. The sphere and real-projective cases are **theorems**; $\mathbb{CP}^n$, $\mathbb{HP}^n$, $\mathbb{CaP}^2$ remain **open**, which is why this page is marked partially-solved.

## 2. Mathematical Foundations

Let $UM$ denote the unit tangent bundle, $\exp_p$ the exponential map, and for $v \in U_pM$ let
$$c(v) = \sup\{t>0 : d(p,\exp_p(tv)) = t\}$$
be the **cut time**. $\mathrm{Cut}(p) = \exp_p\{c(v)v : v \in U_pM\}$.

**Definition (Blaschke).** $(M,g)$ is Blaschke iff $c(v) \equiv \ell$ is independent of $v \in UM$. Then $\mathrm{inj}(M) = \mathrm{diam}(M) = \ell$, the tangent cut locus at each $p$ is the round sphere $\ell\, U_pM$, and
$$\Sigma_p := \exp_p|_{\ell\, U_pM} : S^{n-1}(\ell) \longrightarrow \mathrm{Cut}(p)$$
is a smooth submersion with connected fibres; $\mathrm{Cut}(p)$ is a closed submanifold. In the CROSS models the fibres are the great spheres $S^{k-1}$ with $k = 1,2,4,8$ ($\mathbb{RP}^n$ gives a double cover; $\mathbb{CP}^n$ the Hopf fibration $S^{2n-1}\to\mathbb{CP}^{n-1}$).

**Wiedersehen** is the case $\dim \mathrm{Cut}(p) = 0$: $\Sigma_p$ collapses $S^{n-1}(\ell)$ to a point, all geodesics are closed of common length $2\ell$, and $A: M \to M$ is a fixed-point-free involutive isometry-candidate.

**Bott–Samelson theorem.** If all geodesics of $(M,g)$ are closed with the same length (a *Besse manifold*), then $H^*(M;\mathbb{Z})$ is a truncated polynomial ring on one generator of degree $k \in \{1,2,4,8\}$, and $\pi_*(M) \otimes \mathbb{Q} \cong \pi_*(\text{model})\otimes\mathbb{Q}$. Every Blaschke manifold is Besse, so it is *modeled on* a unique CROSS in the sense of rational homotopy.

**Berger–Kazdan inequality.** If $(M^n,g)$ is compact with $\mathrm{inj}(M) \ge \pi$, then
$$\mathrm{Vol}(M,g) \;\ge\; \mathrm{Vol}\big(S^n(1)\big) \;=\; \frac{2\pi^{(n+1)/2}}{\Gamma\!\left(\frac{n+1}{2}\right)},$$
with equality if and only if $(M,g)$ is isometric to the unit round sphere. The proof is a pointwise inequality for the Jacobian $\theta(t,v)$ of $\exp_p$ along a geodesic:
$$\int_0^\pi \theta(t,v)^{1/(n-1)}\,dt \cdot \int_0^\pi \theta(\pi-t,-v)^{1/(n-1)}\,dt \;\ge\; \left(\int_0^\pi \sin t\, dt\right)^{2}\Big/\ \cdots$$
integrated over $UM$ (Kazdan's analytic lemma, Appendix E of Besse).

**Weinstein–Yang volume identity.** If $(M^n,g)$ is Wiedersehen with all geodesics of length $2\pi$, then a degree-theoretic argument on the geodesic flow gives the *equality*
$$\mathrm{Vol}(M,g) = \mathrm{Vol}\big(S^n(1)\big).$$
Weinstein (1974) proved this for $n$ even; Yang (1980) for $n$ odd.

Combining the two displays forces the equality case: **a Wiedersehen manifold is a round sphere.**

## 3. History & State of the Art (SOTA)

- **1921.** Wilhelm Blaschke, *Vorlesungen über Differentialgeometrie I*, poses the *Wiedersehensfläche* problem: is a surface on which each point has a "see-again" partner necessarily a round sphere?
- **1954–1963.** Bott and Samelson determine the cohomology of manifolds all of whose geodesics are closed — the topological skeleton of the problem.
- **1963.** L. W. Green settles the surface case $n=2$ (*Auf Wiedersehensflächen*, Ann. of Math.), using integral geometry (Santaló-type formula) plus Gauss–Bonnet.
- **1970s.** Berger reduces the general Wiedersehen case to a volume inequality; Kazdan supplies the analytic proof of that inequality; Weinstein proves the volume identity in even dimensions. Besse's 1978 monograph consolidates everything and states the general Blaschke conjecture for all five models.
- **1980.** C. T. Yang closes the odd-dimensional Wiedersehen case, and (with the associated volume identity for $\mathbb{RP}^n$) the real-projective case.
- **1990.** Yang attacks the *topological* Blaschke conjecture through smooth great-circle fibrations of spheres, building on Gluck–Warner's classification for $S^3$.
- **1994.** Reznikov proves the *weak* Blaschke conjecture for $\mathbb{CP}^n$ — rigidity once the underlying manifold is assumed to be $\mathbb{CP}^n$ with the standard model structure.
- **2017.** Radeschi and Wilking prove the Berger conjecture for $S^n$, $n \ge 4$ (all geodesics closed $\Rightarrow$ all of the same length), reviving the Besse-manifold program with equivariant and mean-curvature-flow-free averaging techniques.

## 4. Partial Results / Verified Cases

| Model | Status | Source |
|---|---|---|
| $S^2$ (Wiedersehen surfaces) | **Proved** | Green 1963 |
| $S^n$, $n$ even | **Proved** | Berger–Kazdan + Weinstein 1974 |
| $S^n$, $n$ odd | **Proved** | Berger–Kazdan + Yang 1980 |
| $\mathbb{RP}^n$, all $n$ | **Proved** | Yang 1980, via the $\mathbb{RP}^n$ Berger–Kazdan inequality |
| $\mathbb{CP}^n$, weak form | **Proved** (topology assumed) | Reznikov 1994 |
| $\mathbb{CP}^n$ full, $\mathbb{HP}^n$, $\mathbb{CaP}^2$ | **Open** | — |

Additional verified fragments:

- Every Blaschke manifold has the integral cohomology ring and rational homotopy of its model CROSS (Bott–Samelson); so no exotic *homotopy type* can occur.
- A Blaschke manifold modeled on $\mathbb{CP}^n$ has $\mathrm{Cut}(p)$ itself a Blaschke manifold modeled on $\mathbb{CP}^{n-1}$, giving an induction whose base case ($n=1$, $\mathbb{CP}^1 = S^2$) is known.
- In dimension 4, a Blaschke manifold modeled on $\mathbb{CP}^2$ is simply connected with $b_2 = 1$ and even intersection form data matching $\mathbb{CP}^2$, hence homeomorphic to $\mathbb{CP}^2$ by Freedman's classification — but smooth and metric rigidity are not implied.
- Zoll spheres (non-round metrics on $S^2$ with all geodesics closed of length $2\pi$) show the *Besse* condition alone is far weaker; they are never Blaschke, confirming the Blaschke hypothesis carries real strength.

## 5. Principal Obstacles

- **No volume identity beyond $S^n$ and $\mathbb{RP}^n$.** The Weinstein–Yang degree argument uses that the "antipodal" map $A$ is a diffeomorphism $M \to M$ (0-dimensional cut locus) or a $\mathbb{Z}_2$-cover. For $\mathbb{CP}^n$-type models the cut map $\Sigma_p$ is a genuine circle fibration; the natural degree invariant lives on a fibration whose base varies with $p$, and no comparable identity $\mathrm{Vol}(M) = \mathrm{Vol}(\mathbb{CP}^n)$ is known.
- **No Berger–Kazdan inequality for the higher models.** Kazdan's inequality is a one-dimensional integral inequality for the Jacobian along a single geodesic. For $\mathbb{CP}^n$ the conjugate/cut structure is anisotropic — Jacobi fields split into a Hopf direction (conjugate at $t=\ell$ with multiplicity 1) and $2n-2$ transverse directions (conjugate at $t=\ell/2$? in the Fubini–Study normalisation, at $\pi/2$ vs $\pi$). Any candidate inequality must handle two conjugate times at once, and the corresponding scalar variational problem is not convex in the way Kazdan's is.
- **Topology does not determine smooth structure.** Bott–Samelson pins down cohomology but not diffeomorphism type; for $\mathbb{HP}^n$ and $\mathbb{CaP}^2$ even the *topological* Blaschke conjecture (is $M$ homeomorphic to the model?) is unresolved, and the relevant sphere-fibration classification (fibrations of $S^{4n-1}$ by great 3-spheres) is far less rigid than the great-circle case.
- **Comparison geometry gives no curvature hypothesis.** Blaschke manifolds carry no a priori sectional curvature bound, so Toponogov, Cheeger–Gromoll, and sphere-theorem machinery are unavailable; the hypothesis is purely about the cut locus.
- **Integral-geometric transforms are underdetermined.** Radon/Funk-transform arguments (Reznikov's route) invert the geodesic-length data only after the underlying model is fixed, which is precisely the assumption one wants to remove.

## 6. The Gap

Proven: rigidity holds when the model is $S^n$ or $\mathbb{RP}^n$, because there the chain
$$\text{Blaschke} \;\Rightarrow\; \mathrm{Vol}(M) = \mathrm{Vol}(\text{model}) \;\Rightarrow\; \text{equality in Berger–Kazdan} \;\Rightarrow\; \text{isometry}$$
is complete. The gap is exactly the two missing links for $k = 2, 4, 8$:

1. **The identity.** Show $\mathrm{Vol}(M,g) = \mathrm{Vol}(\text{model})$ for a Blaschke manifold modeled on $\mathbb{CP}^n$, $\mathbb{HP}^n$, $\mathbb{CaP}^2$ (normalised so $\ell = \pi$ or $\pi/2$ as appropriate). Equivalently, produce a degree/index invariant for the family $\{\Sigma_p\}$ of sphere fibrations.
2. **The inequality with rigidity.** Prove $\mathrm{Vol}(M,g) \ge \mathrm{Vol}(\text{model})$ under the Blaschke condition, with equality only for the canonical metric.

Either alone is insufficient; both together close the conjecture. A weaker but still open intermediate step is the **topological Blaschke conjecture**: $M$ is diffeomorphic to its model.

## 7. Current Research (as of June 2026)

- **Münster school (Wilking and collaborators).** The Radeschi–Wilking method — averaging over the geodesic flow and exploiting the $S^1$-action on the space of geodesics — is the most active line. Its natural next target is the Besse/Blaschke structure on $\mathbb{CP}^n$-type manifolds, where the space of geodesics is a symplectic orbifold. *(frontier — verify)*
- **Radeschi (Notre Dame / Torino) and singular Riemannian foliation techniques.** The cut-locus submersions $\Sigma_p$ are singular Riemannian foliations of round spheres; classification results for such foliations by round spheres could force the Hopf model. *(frontier — verify)*
- **Integrable-systems approach (Kiyohara, Okayama).** Explicit constructions of manifolds with completely integrable geodesic flow and closed geodesics on $\mathbb{CP}^n$-type spaces sharpen where a counterexample could live: none of the known families is Blaschke, which is evidence *for* the conjecture.
- **Symplectic/contact reformulation.** The space of oriented geodesics of a Blaschke manifold is a smooth closed symplectic manifold; rigidity statements for its Hamiltonian $S^1$-actions (Gromov-type or Delzant-type) are being tested as substitutes for the missing volume identity. *(frontier — verify)*
- **4-dimensional case.** Combining Seiberg–Witten/gauge-theoretic rigidity for $\mathbb{CP}^2$ with the Blaschke condition is a concrete, low-dimensional target where the topology is already fixed.

## 8. Future Work

- Find the correct generalisation of the Berger–Kazdan inequality with **two conjugate times**; the model inequality would be a sharp bound on $\int \theta^{1/(n-1)}$ for Jacobian functions vanishing at $\ell$ with prescribed multiplicities $(1, 2n-2)$.
- Establish the topological Blaschke conjecture for $\mathbb{HP}^n$ by classifying smooth fibrations of $S^{4n-1}$ by great 3-spheres, the quaternionic analogue of Gluck–Warner.
- Prove the volume identity via a Chern–Weil / index-theoretic invariant of the family $p \mapsto \Sigma_p$ rather than by degree theory.
- Test the conjecture under auxiliary hypotheses that plausibly hold automatically: non-negative sectional curvature, Einstein, or Kähler; a Kähler Blaschke manifold modeled on $\mathbb{CP}^n$ should be Fubini–Study.
- Reverse the question: classify Besse manifolds first (Berger conjecture in higher models), then specialise to the Blaschke subclass.

## 9. Key References

- **[Foundational]** Blaschke, W. *Vorlesungen über Differentialgeometrie und geometrische Grundlagen von Einsteins Relativitätstheorie I.* Springer, Berlin, 1921.
- **[Foundational]** Bott, R. *On manifolds all of whose geodesics are closed.* Annals of Mathematics **60** (1954), 375–382.
- **[Foundational]** Samelson, H. *On manifolds with many closed geodesics.* Portugaliae Mathematica **22** (1963), 193–196.
- **[Foundational]** Green, L. W. *Auf Wiedersehensflächen.* Annals of Mathematics **78** (1963), 289–299.
- **[Foundational]** Weinstein, A. *On the volume of manifolds all of whose geodesics are closed.* Journal of Differential Geometry **9** (1974), 513–517.
- **[Survey]** Besse, A. L. *Manifolds all of whose Geodesics are Closed.* Ergebnisse der Mathematik und ihrer Grenzgebiete **93**, Springer, 1978. (Includes Kazdan's Appendix E, *An inequality arising in geometry*.)
- **[Foundational]** Yang, C. T. *Odd-dimensional Wiedersehen manifolds and the Blaschke conjecture.* Journal of Differential Geometry, 1980.
- **[SOTA]** Gluck, H., Warner, F. *Great circle fibrations of the three-sphere.* Duke Mathematical Journal **50** (1983), 107–132.
- **[SOTA]** Yang, C. T. *Smooth great circle fibrations and an application to the topological Blaschke conjecture.* Transactions of the American Mathematical Society **320** (1990), 507–524.
- **[SOTA]** Reznikov, A. *The weak Blaschke conjecture for $\mathbb{CP}^n$.* Inventiones Mathematicae **117** (1994), 447–454.
- **[SOTA]** Kiyohara, K. *Two classes of Riemannian manifolds whose geodesic flows are integrable.* Memoirs of the American Mathematical Society **130** (1997), no. 619.
- **[SOTA / Recent]** Radeschi, M., Wilking, B. *On the Berger conjecture for manifolds all of whose geodesics are closed.* Inventiones Mathematicae **210** (2017), 911–962.
- **[Survey]** Cheeger, J., Ebin, D. G. *Comparison Theorems in Riemannian Geometry.* North-Holland, 1975; reprinted AMS Chelsea, 2008. (Cut locus, Jacobi field, and volume comparison background.)

## 10. Worked Example / Concrete Special Case

**The Wiedersehen sphere $S^2$, computed end to end.**

Take $(M^2,g)$ compact, Wiedersehen, normalised so every geodesic is closed of length $2\pi$; then $\ell = \pi$ and $\mathrm{inj}(M) = \pi$.

*Step 1 — Jacobian along a geodesic.* Fix $p$ and $v \in U_pM$. Write $\exp_p^* (d\mathrm{vol}) = \theta(t,v)\, dt\, dv$. Since $n = 2$, the single normal Jacobi field $J$ with $J(0)=0$, $|J'(0)|=1$ satisfies $\theta(t,v) = |J(t)|$ and $\theta(0,v)=0$, $\theta'(0,v)=1$, and $\theta(\pi,v)=0$ because $\exp_p(\pi v) = A(p)$ for every $v$ (all geodesics reconverge).

*Step 2 — Weinstein's identity.* Integrating over $U M$,
$$\mathrm{Vol}(M) = \int_{U_pM}\!\!\int_0^\pi \theta(t,v)\,dt\,dv .$$
The Wiedersehen map $A$ is a diffeomorphism with $A^2 = \mathrm{id}$ and $A$ preserves volume (it is the time-$\pi$ endpoint map of a volume-preserving flow). Weinstein's degree argument yields
$$\mathrm{Vol}(M) = \mathrm{Vol}(S^2(1)) = 4\pi .$$

*Step 3 — Berger–Kazdan for $n=2$.* With $n=2$ the inequality reads: for $\theta \ge 0$ on $[0,\pi]$ with $\theta(0)=\theta(\pi)=0$, $\theta'(0)=1$, arising as $|J|$ for a Jacobi field,
$$\int_0^\pi \theta(t,v)\,dt \cdot \int_0^\pi \theta(t,-v)\,dt \;\ge\; \left(\int_0^\pi \sin t\,dt\right)^2 = 4 .$$
Averaging over $U_pM = S^1$ (Cauchy–Schwarz) and then over $p$ gives $\mathrm{Vol}(M) \ge 4\pi$, with **equality iff** $\theta(t,v) = \sin t$ for all $t, v$.

*Step 4 — Rigidity.* Steps 2 and 3 force equality, so $\theta(t,v) = \sin t$ identically. But $\theta$ solves the Jacobi equation $\theta'' + K(\gamma_v(t))\,\theta = 0$, hence
$$-\sin t + K(\gamma_v(t))\sin t = 0 \quad \Longrightarrow \quad K \equiv 1$$
along every geodesic, i.e. everywhere. A complete simply connected (Wiedersehen $\Rightarrow$ $\pi_1$ trivial here) surface of constant curvature $1$ is the unit round sphere. $\blacksquare$

*Where this breaks for $\mathbb{CP}^n$.* Normalise Fubini–Study so $\ell = \pi/2$ and sectional curvatures lie in $[1,4]$. Along a unit-speed geodesic the Jacobi Jacobian is
$$\theta(t) = \tfrac{1}{2}\sin(2t)\,\big(\sin t\big)^{2n-2},$$
vanishing at $t = \pi/2$ to order 1 in the Hopf direction and *not* vanishing there in the $2n-2$ transverse directions — the transverse conjugate point sits at $t = \pi$. Step 2 fails because $A$ is not a map $M \to M$ but a fibration $U_pM = S^{2n-1} \to \mathbb{CP}^{n-1}$, and Step 3 fails because no proven inequality controls the product of the two integrals when $\theta$ has this mixed vanishing pattern. Those two failures are precisely Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*