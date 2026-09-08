---
id: 05-analysis/painleve-problem
title: "Painlevé Problem"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Painlevé Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/painleve-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Characterize, in purely geometric and metric terms, the compact sets $E \subset \mathbb{C}$ that are **removable for bounded analytic functions**: for every open $\Omega \supset E$, every bounded holomorphic $f : \Omega \setminus E \to \mathbb{C}$ extends holomorphically to $\Omega$.

By Ahlfors (1947), removability is equivalent to the vanishing of the **analytic capacity** $\gamma(E)$. So the problem is: give a checkable description — in terms of Hausdorff measure/content, densities, projections, or tangent structure — of the class $\{E : \gamma(E) = 0\}$.

A complete solution must supply a condition that (i) is invariant under the natural symmetries of the problem (translations, rotations, dilations, and in fact bilipschitz maps), (ii) is stated without reference to analytic functions or singular integrals, and (iii) is proved equivalent to $\gamma(E)=0$ for **all** compact $E$, including sets of non-$\sigma$-finite $1$-dimensional Hausdorff measure. The problem is classified *partially-solved*: a complete non-geometric characterization (Tolsa 2003, via Menger curvature of measures) exists, and the finite-length case is fully geometric (David 1998), but no purely metric/geometric criterion is known in general.

## 2. Mathematical Foundations

**Analytic capacity.** For compact $E \subset \mathbb{C}$,
$$\gamma(E) = \sup\{|f'(\infty)| : f \in H^\infty(\mathbb{C}^*\setminus E),\ \|f\|_\infty \le 1\},\qquad f'(\infty) = \lim_{z\to\infty} z\bigl(f(z)-f(\infty)\bigr).$$
$E$ is removable $\iff \gamma(E)=0$ (Ahlfors). Equivalently, $\gamma(E) = \sup |\langle T, 1\rangle|$ over distributions $T$ supported in $E$ whose Cauchy potential $T * \tfrac1z$ is bounded by $1$ off $E$.

**Positive analytic capacity.** Restricting to positive measures,
$$\gamma_+(E) = \sup\{\mu(E) : \operatorname{supp}\mu \subset E,\ \|\mu * \tfrac1z\|_{L^\infty(\mathbb{C})} \le 1\}.$$
Trivially $\gamma_+ \le \gamma$.

**Menger curvature.** For distinct $x,y,z \in \mathbb{C}$ let $c(x,y,z) = 1/R(x,y,z)$, the reciprocal circumradius. For a Radon measure $\mu$,
$$c^2(\mu) = \iiint c(x,y,z)^2 \, d\mu(x)\,d\mu(y)\,d\mu(z).$$
**Melnikov's identity** (1995) links this to the Cauchy kernel: for $\mu$ with linear growth $\mu(B(x,r)) \le C r$,
$$\|\mathcal{C}_\varepsilon \mu\|_{L^2(\mu)}^2 = \tfrac16\, c_\varepsilon^2(\mu) + O(\mu(\mathbb{C})),\qquad \mathcal{C}_\varepsilon\mu(z)=\int_{|z-w|>\varepsilon}\frac{d\mu(w)}{z-w}.$$
This is the algebraic accident — positivity of the symmetrized Cauchy kernel — on which the whole modern theory rests.

**Rectifiability.** $E$ with $\mathcal{H}^1(E)<\infty$ is *rectifiable* if $\mathcal{H}^1$-almost all of it lies in a countable union of Lipschitz graphs; *purely unrectifiable* if it meets every such graph in $\mathcal{H}^1$-measure zero. **Besicovitch projection theorem:** $E$ purely unrectifiable with $\mathcal{H}^1(E)<\infty$ $\Rightarrow$ the Favard length $\operatorname{Fav}(E)=\int_0^{\pi}\mathcal{H}^1(\pi_\theta E)\,d\theta$ is $0$.

**Classical bounds.** $\mathcal{H}^1(E)=0 \Rightarrow \gamma(E)=0$ (Painlevé); $\dim_H E > 1 \Rightarrow \gamma(E)>0$ (Frostman + growth estimate). Also $\gamma(E) \ge c\,\operatorname{Fav}(E)$ (Vitushkin). Hence all difficulty is concentrated at $\dim_H E = 1$.

## 3. History & State of the Art (SOTA)

- **1888.** Painlevé proves $\mathcal{H}^1(E)=0 \Rightarrow$ removable, and asks for the exact geometric condition.
- **1947.** Ahlfors introduces $\gamma$ and proves removability $\iff \gamma(E)=0$, converting an extension problem into a capacity problem.
- **1909/1936.** Denjoy conjectures that a compact subset of a rectifiable curve is removable iff it has zero length; proved by Calderón (1977) via $L^2$-boundedness of the Cauchy integral on Lipschitz graphs.
- **1967.** Vitushkin conjectures $\gamma(E) = 0 \iff \operatorname{Fav}(E)=0$.
- **1970.** Garnett, and independently Ivanov, exhibit the four-corner Cantor set: positive finite length, zero analytic capacity.
- **1986.** Mattila (*Ann. of Math.*) disproves Vitushkin's conjecture in general: zero Favard length is not invariant under the dilation-type symmetries that $\gamma$ must respect, so no such equivalence can hold for arbitrary compacta.
- **1995–96.** Melnikov's curvature identity; Melnikov–Verdera's curvature proof of Calderón's theorem; Mattila–Melnikov–Verdera prove Vitushkin's conjecture for Ahlfors–David regular sets.
- **1998.** David proves the **Vitushkin conjecture for sets of finite length**: $\mathcal{H}^1(E)<\infty$ and $E$ purely unrectifiable $\Rightarrow \gamma(E)=0$.
- **2003.** Tolsa (*Acta Math.*) proves $\gamma \approx \gamma_+$ and the **countable semiadditivity** $\gamma(\bigcup_i E_i) \le C\sum_i \gamma(E_i)$, together with the curvature characterization in §6.
- **2005.** Tolsa proves $\gamma$ is invariant under bilipschitz maps (up to constants) — evidence that the sought criterion must be bilipschitz-invariant.
- **2014.** Nazarov–Tolsa–Volberg settle the codimension-1 analogue (Lipschitz harmonic capacity in $\mathbb{R}^{n+1}$) via the Riesz transform, without a curvature identity.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| $\mathcal{H}^1(E)=0$ | $\gamma(E)=0$ (Painlevé, 1888) |
| $\dim_H E>1$ | $\gamma(E)>0$ (Frostman) |
| $E \subset$ rectifiable curve | $\gamma(E)=0 \iff \mathcal{H}^1(E)=0$ (Calderón 1977) |
| $\mathcal{H}^1(E)<\infty$ | $\gamma(E)=0 \iff E$ purely unrectifiable $\iff \operatorname{Fav}(E)=0$ (David 1998) |
| $\mathcal{H}^1$ $\sigma$-finite | Same criterion, by semiadditivity (Tolsa 2003) |
| Ahlfors-regular $E$ ($\mathcal{H}^1(E\cap B(x,r))\approx r$) | $\gamma(E)>0 \iff E$ uniformly rectifiable (MMV 1996) |
| Cantor sets $E(\lambda_n)$ with $\lambda_n$ contraction ratios | $\gamma(E(\lambda_n)) \approx \bigl(\sum_n \lambda_1^{-2}\cdots\lambda_n^{-2} 4^{-n}\bigr)^{-1/2}$-type formula; explicit criterion (Mateu–Tolsa–Verdera, *JAMS* 2003) |
| All compact $E$ | $\gamma \approx \gamma_+$; $\gamma$ semiadditive; $\gamma$ bilipschitz invariant (Tolsa 2003, 2005) |
| Codimension 1 in $\mathbb{R}^{n+1}$, $\mathcal{H}^n$-finite | Removable for Lipschitz harmonic functions $\iff$ purely $n$-unrectifiable (NTV 2014) |

## 5. Principal Obstacles

- **No dimension-1 density.** At $\dim_H E = 1$ with $\mathcal{H}^1(E)=\infty$ and non-$\sigma$-finite, densities $\mu(B(x,r))/r$ oscillate wildly; rectifiability is not even defined, so David's dichotomy has nothing to bite on.
- **Curvature is not geometric enough.** Tolsa's characterization quantifies over *all* measures on $E$ with linear growth and finite curvature. Deciding whether such a measure exists is itself an infinite-dimensional optimization; no known Hausdorff-content or projection quantity is comparable to it.
- **Non-doubling Calderón–Zygmund theory is delicate.** Standard $T(1)/T(b)$ machinery needs doubling; the substitutes (Nazarov–Treil–Volberg, David's local $T(b)$, Tolsa's $\mathrm{RBMO}$) give existence of a good measure only after suppression arguments that lose all quantitative geometry.
- **Vitushkin's projection heuristic is provably wrong.** Mattila's 1986 theorem shows $\{\operatorname{Fav}=0\}$ is not closed under the maps that preserve $\gamma$; and quantitatively $\operatorname{Fav}$ and $\gamma$ decay at different rates on Cantor sets (§10). Integral geometry cannot be the answer.
- **The curvature identity has no higher-dimensional analogue.** For $s$-dimensional Riesz kernels with $s\ne 1$ in the plane, or $s < n$ in $\mathbb{R}^{n+1}$, the symmetrization is not positive, blocking transfer of the planar proofs.
- **Capacity is not subadditive with constant 1**, and no maximum principle is known for $\gamma$, so potential-theoretic templates (Newtonian/Riesz capacity, Wiener criterion) do not apply.

## 6. The Gap

Tolsa's theorem gives, for all compact $E$,
$$\gamma(E) \approx \sup\bigl\{\mu(E) : \operatorname{supp}\mu\subset E,\ \mu(B(x,r))\le r\ \forall x,r,\ c^2(\mu) \le \mu(E)\bigr\}.$$
So $\gamma(E)=0$ iff $E$ carries **no** nonzero measure with linear growth and finite Menger curvature. This is a complete solution of the *analytic* question — it removes all reference to holomorphic functions — but is not the *geometric* description Painlevé asked for.

The gap is exactly this: **for $\mathcal{H}^1$-non-$\sigma$-finite sets, translate "carries a linear-growth measure of finite curvature" into a statement about the metric geometry of $E$** (approximate tangents, $\beta$-numbers, content of projections, or a Wiener-type integral condition). For finite length the translation is David's theorem: it says "finite curvature ⟺ rectifiable". Beyond finite length no rectifiability notion is available, and finding the right substitute — a "measure-theoretic rectifiability at scale" invariant under bilipschitz maps — is the missing step.

## 7. Current Research (as of June 2026)

- **Barcelona school (Tolsa, Mateu, Verdera, Dąbrowski at UAB/ICREA):** quantitative rectifiability via $\beta_p$-coefficients and Riesz-transform characterizations of rectifiability for general (non-regular) measures; extension of the David–Semmes program to arbitrary Radon measures.
- **Riesz transforms in non-integer dimension (Eiderman, Nazarov, Volberg, Jaye):** Wolff-energy methods showing unboundedness of the $s$-Riesz transform for $s$ non-integer, giving capacity-vanishing criteria in the fractional regime.
- **Favard length decay:** upper bounds $\operatorname{Fav}(E_n)\lesssim n^{-p}$ (Nazarov–Peres–Volberg) versus lower bound $\gtrsim \log n / n$ (Bateman–Volberg); determining the true exponent for the four-corner set remains open and is a natural quantitative testbed. *(frontier — verify)* Work of Cladek, Davey, Taylor and collaborators on Favard length of generalized Cantor sets continues to sharpen these.
- **Heisenberg/metric-space analogues:** removability and Riesz transforms in Carnot groups (Chousionis, Fässler, Orponen) as a probe of which parts of the proof are Euclidean.
- Analogous "Painlevé problems" for Lipschitz harmonic capacity in codimension $>1$ and for the heat/caloric setting (Mateu, Prat, Tolsa) are active. *(frontier — verify)*

## 8. Future Work

- Find a **bilipschitz-invariant metric quantity** $\Theta(E)$ with $\Theta(E)=0 \iff \gamma(E)=0$; candidates are Wolff-type energies $\int\!\!\int \bigl(\tfrac{\mu(B(x,r))}{r}\bigr)^{p}\tfrac{d r}{r}d\mu$ and $L^2$ $\beta$-numbers, but no candidate is yet known to be comparable to curvature for non-$\sigma$-finite sets.
- Decide whether **$\gamma$ is semiadditive with constant $1$** and whether a maximum principle holds — both would let one localize the characterization.
- Establish a **sharp Favard-length law** for self-similar Cantor sets, clarifying how far integral geometry can go.
- Develop **curvature-free proofs** of David's theorem (as NTV did in codimension 1), since only such proofs can port to higher codimension.
- Determine whether **continuous analytic capacity $\alpha$ and $\gamma$** admit a common geometric description in the non-$\sigma$-finite regime (Tolsa proved $\alpha\approx\gamma$ in 2004).

## 9. Key References

- **[Foundational]** P. Painlevé. *Sur les lignes singulières des fonctions analytiques.* Annales de la Faculté des Sciences de Toulouse, 1888. [DOI](https://doi.org/10.5802/afst.18)
- **[Foundational]** L. V. Ahlfors. *Bounded analytic functions.* Duke Mathematical Journal 14 (1947), 1–11.
- **[Foundational]** A. G. Vitushkin. *The analytic capacity of sets in problems of approximation theory.* Russian Mathematical Surveys 22 (1967), 139–200. [DOI](https://doi.org/10.1070/rm1967v022n06abeh003763)
- **[Foundational]** A. P. Calderón. *Cauchy integrals on Lipschitz curves and related operators.* PNAS 74 (1977), 1324–1327. [DOI](https://doi.org/10.1073/pnas.74.4.1324)
- **[Structural]** P. Mattila. *Smooth maps, null-sets for integralgeometric measure and analytic capacity.* Annals of Mathematics 123 (1986), 303–309. [DOI](https://doi.org/10.2307/1971273)
- **[Foundational]** M. S. Melnikov. *Analytic capacity: a discrete approach and the curvature of measure.* Sbornik: Mathematics 186 (1995), 827–846.
- **[Foundational]** M. S. Melnikov, J. Verdera. *A geometric proof of the $L^2$ boundedness of the Cauchy integral on Lipschitz graphs.* International Mathematics Research Notices 1995, 325–331.
- **[Foundational]** P. Mattila, M. S. Melnikov, J. Verdera. *The Cauchy integral, analytic capacity, and uniform rectifiability.* Annals of Mathematics 144 (1996), 127–136. [DOI](https://doi.org/10.2307/2118585)
- **[SOTA]** G. David. *Unrectifiable 1-sets have vanishing analytic capacity.* Revista Matemática Iberoamericana 14 (1998), 369–479.
- **[SOTA]** X. Tolsa. *Painlevé's problem and the semiadditivity of analytic capacity.* Acta Mathematica 190 (2003), 105–149. [DOI](https://doi.org/10.1007/bf02393237)
- **[SOTA]** X. Tolsa. *Bilipschitz maps, analytic capacity, and the Cauchy integral.* Annals of Mathematics 162 (2005), 1243–1304. [DOI](https://doi.org/10.4007/annals.2005.162.1243)
- **[SOTA]** J. Mateu, X. Tolsa, J. Verdera. *The planar Cantor sets of zero analytic capacity and the local $T(b)$-theorem.* Journal of the AMS 16 (2003), 19–28. [DOI](https://doi.org/10.1090/s0894-0347-02-00401-0)
- **[SOTA]** F. Nazarov, X. Tolsa, A. Volberg. *On the uniform rectifiability of AD-regular measures with bounded Riesz transform operators: the case of codimension 1.* Acta Mathematica 213 (2014), 237–321. [DOI](https://doi.org/10.1007/s11511-014-0120-7)
- **[SOTA]** F. Nazarov, X. Tolsa, A. Volberg. *The Riesz transform, rectifiability, and removability for Lipschitz harmonic functions.* Publicacions Matemàtiques 58 (2014), 517–532. [DOI](https://doi.org/10.5565/publmat_58214_26)
- **[Related]** D. Bateman, A. Volberg. *An estimate from below for the Buffon needle probability of the four-corner Cantor set.* Mathematical Research Letters 17 (2010), 959–967. [DOI](https://doi.org/10.4310/mrl.2010.v17.n5.a12)
- **[Survey]** X. Tolsa. *Analytic Capacity, the Cauchy Transform, and Non-homogeneous Calderón–Zygmund Theory.* Progress in Mathematics 307, Birkhäuser, 2014. [DOI](https://doi.org/10.1007/978-3-319-00596-6)
- **[Survey]** J. J. Dudziak. *Vitushkin's Conjecture for Removable Sets.* Universitext, Springer, 2010. [DOI](https://doi.org/10.1007/978-1-4419-6709-1)
- **[Survey]** J. Verdera. *Removability, capacity and approximation.* In *Complex Potential Theory*, NATO ASI Series C 439, Kluwer, 1994, 419–473. [DOI](https://doi.org/10.1007/978-94-011-0934-5_10)

## 10. Worked Example / Concrete Special Case

**The four-corner Cantor set.** Let $E_0 = [0,1]^2$. Given $E_{n-1}$, replace each of its $4^{n-1}$ squares of side $4^{-(n-1)}$ by the four corner subsquares of side $4^{-n}$. Then $E_n$ is a union of $4^n$ squares of side $4^{-n}$, and $E = \bigcap_n E_n$ satisfies $\mathcal{H}^1(E) = \sqrt2$.

*Step 1 — the natural measure.* Let $\mu_n$ be the probability measure that is uniform (Lebesgue $\times\, 4^{-n}$-normalized) on $E_n$. Each square carries mass $4^{-n}$ and has diameter $\sqrt2\cdot 4^{-n}$, so
$$\mu_n(B(x,r)) \le C r \quad\text{for all } r \ge 4^{-n},$$
i.e. $\mu_n$ has linear growth down to scale $4^{-n}$.

*Step 2 — the curvature is logarithmically large.* A direct count (Mateu–Tolsa–Verdera) gives
$$c^2(\mu_n) = \iiint c(x,y,z)^2 d\mu_n^3 \approx n .$$
The mechanism: for each scale $k \le n$, triples of points sitting in three distinct children of a common $k$-th generation square contribute $\approx 1$ to the curvature integral, and the $n$ scales contribute independently. Each single scale is "flat enough" to contribute only $O(1)$, but the contributions add.

*Step 3 — optimize the mass.* Put $\lambda = t\,\mu_n$ with $t \in (0,1]$. Since curvature is a triple integral, $c^2(t\mu_n) = t^3 c^2(\mu_n) \approx t^3 n$. Tolsa's criterion asks for $c^2(\lambda) \lesssim \lambda(E_n) = t$, i.e.
$$t^3 n \lesssim t \iff t \lesssim n^{-1/2}.$$
Hence
$$\gamma(E_n) \approx n^{-1/2}.$$

*Step 4 — pass to the limit.* $E \subset E_n$ for every $n$ and $\gamma$ is monotone, so
$$\gamma(E) \le C\, n^{-1/2} \xrightarrow[n\to\infty]{} 0 ,$$
so $\gamma(E)=0$: **$E$ has positive finite length yet is removable** (Garnett 1970; the rate is Mateu–Tolsa–Verdera 2003). Consistently, $E$ is purely unrectifiable and $\operatorname{Fav}(E)=0$ by Besicovitch — matching David's theorem.

*Step 5 — why this also shows projections are the wrong invariant.* For the truncations, the best known bounds are
$$c\,\frac{\log n}{n} \le \operatorname{Fav}(E_n) \le C n^{-p}\quad (p>0),$$
against $\gamma(E_n)\approx n^{-1/2}$. Favard length is (at least) an order of magnitude smaller than analytic capacity here, so even at the quantitative level the two are not comparable — an explicit sign of the failure Mattila proved qualitatively in 1986, and a concrete illustration of the gap in §6: replacing $c^2(\mu)$ by any integral-geometric quantity loses the correct order.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*