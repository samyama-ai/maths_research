---
id: 05-analysis/fatou-conjecture
title: "Fatou Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 05-analysis/fatou-conjecture
title: "Fatou Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
```

# Fatou Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/fatou-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Fatou Conjecture is a foundational open problem in the field of holomorphic dynamics. It asserts that in the space of all rational maps of a given degree on the Riemann sphere, the maps exhibiting hyperbolic dynamics form a dense open set. 

Formally, let $Rat_d$ denote the space of rational maps of degree $d \ge 2$ defined on the Riemann sphere $\widehat{\mathbb{C}}$. A map $f \in Rat_d$ is said to be *hyperbolic* if the orbit of every critical point of $f$ converges to an attracting (or super-attracting) periodic cycle. 

The conjecture claims that the set of hyperbolic maps $\mathcal{H}_d$ is dense in $Rat_d$ under the natural algebraic topology of the parameter space. For the specific case of polynomials of degree $d$ (the space $Poly_d$), the conjecture states that hyperbolic polynomials are dense in $Poly_d$. In the most famous and widely studied case of quadratic polynomials, parameterized by $P_c(z) = z^2 + c$, the conjecture posits that hyperbolic parameters $c$ are dense in the complex plane $\mathbb{C}$, which is equivalent to asserting that every connected component of the interior of the Mandelbrot set $\mathcal{M}$ is a hyperbolic component.

A complete proof must demonstrate that any structurally stable rational map is hyperbolic, or equivalently, construct arbitrary-precision perturbations that map any non-hyperbolic rational map into a hyperbolic one.

## 2. Mathematical Foundations

The dynamics of a rational map $f: \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$ of degree $d \ge 2$ partitions the Riemann sphere into two fundamental sets. The **Fatou set**, denoted $\mathcal{F}(f)$, is the maximal open set where the family of iterates $\{f^n\}_{n \ge 1}$ forms a normal family in the sense of Montel. The dynamics on $\mathcal{F}(f)$ are stable under small perturbations of the starting point. The **Julia set**, denoted $\mathcal{J}(f) = \widehat{\mathbb{C}} \setminus \mathcal{F}(f)$, is the locus of chaotic dynamics.

A critical point $c \in \widehat{\mathbb{C}}$ is a point where the local topological degree is strictly greater than 1, equivalent to $f'(c) = 0$ in local coordinates. The set of critical points is denoted $Crit(f)$. The post-critical set is defined as:
$$ P(f) = \overline{ \bigcup_{n \ge 1} f^n(Crit(f)) } $$

A rational map $f$ is **hyperbolic** if it is strictly expanding on its Julia set. Equivalently, $f$ is hyperbolic if and only if $P(f) \cap \mathcal{J}(f) = \emptyset$. When this condition holds, every critical point lies in the Fatou set and is asymptotically absorbed by an attracting periodic cycle.

The parameter space $Rat_d$ can be identified with a Zariski open subset of the complex projective space $\mathbb{P}^{2d+1}$. By the Mañé-Sad-Sullivan Theorem, the set of $J$-stable maps—maps for which the Julia set moves continuously under quasi-conformal deformations in parameter space—is dense in $Rat_d$. 

The analytical machinery used to study density relies on the **Measurable Riemann Mapping Theorem**. Given a measurable Beltrami differential $\mu(z)\frac{d\bar{z}}{dz}$ on $\widehat{\mathbb{C}}$ satisfying $\|\mu\|_\infty < 1$, there exists a quasiconformal homeomorphism $\phi: \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$ solving the Beltrami equation:
$$ \frac{\partial \phi}{\partial \bar{z}} = \mu(z) \frac{\partial \phi}{\partial z} $$
If $\mu$ is strictly invariant under pullback by $f$ (i.e., $f^* \mu = \mu$), then the conjugated map $g = \phi \circ f \circ \phi^{-1}$ is another rational map. 

An **invariant line field** on $\mathcal{J}(f)$ is a measurable assignment of 1-dimensional real tangent subspaces $L_z \subset T_z\mathbb{C}$ on a subset of $\mathcal{J}(f)$ of positive Lebesgue measure, such that $Df_z(L_z) = L_{f(z)}$. The presence of such a field permits the construction of a non-trivial invariant Beltrami differential, allowing deformations of the map that preserve the chaotic topology without introducing attracting cycles, thus forming "queer components."

## 3. History & State of the Art (SOTA)

Pierre Fatou introduced the framework of complex dynamics in 1919-1920. In his seminal memoir "Sur les équations fonctionnelles", Fatou conjectured that the structurally stable maps (which he suspected to be maps with attracting cycles) are dense.

For over sixty years, little progress was made until the 1980s, when Adrien Douady, John H. Hubbard, and Dennis Sullivan revolutionized the field. Sullivan (1985) introduced quasiconformal surgery into dynamics, successfully proving Fatou's No Wandering Domains conjecture. This technique provided the principal framework to attack the density of hyperbolicity via the Beltrami equation.

Douady and Hubbard established the study of the Mandelbrot set $\mathcal{M}$ for the family $P_c(z) = z^2 + c$. They proved that if $\mathcal{M}$ is locally connected (the MLC Conjecture), then the Fatou conjecture holds for degree 2 polynomials. 

In the 1990s, Jean-Christophe Yoccoz achieved a massive breakthrough by proving MLC for all finitely renormalizable quadratic polynomials. His method of "Yoccoz puzzles" established rigid topological bounds on the parameter space. 

In 1997, a major milestone was reached when Jacek Graczyk & Grzegorz Świątek, and independently Mikhail Lyubich, proved the density of hyperbolicity for *real* quadratic polynomials (the Real Fatou Conjecture).

The current State of the Art remains firmly blocked at the boundary of complex, infinitely renormalizable maps with unbounded combinatorics. While Kahn and Lyubich (2009) proved MLC for infinitely renormalizable maps with bounded combinatorics, the unbounded case—where critical return times grow erratically—remains the central barrier to a complete proof in dimension one.

## 4. Partial Results / Verified Cases

The Fatou conjecture has been completely resolved in the following rigorous special cases:

1. **Real Quadratics:** Hyperbolic parameters are dense on the real axis within the Mandelbrot set (Graczyk-Świątek, Lyubich, 1997).
2. **Real Polynomials:** Hyperbolicity is dense in the space of real polynomials with all real critical points, extended for arbitrary degree $d$ (Kozlovski, Shen, van Strien, 2007).
3. **Finitely Renormalizable Quadratics:** Yoccoz proved that any parameter $c \in \mathcal{M}$ which is at most finitely renormalizable and has no neutral periodic cycles is a point of local connectivity, implying density of hyperbolicity in those domains.
4. **Bounded Combinatorics:** For infinitely renormalizable quadratic polynomials where the degrees of the successive renormalizations are globally bounded, Kahn and Lyubich (2009) achieved complex a-priori bounds, yielding local connectivity and localized density of hyperbolicity.

## 5. Principal Obstacles

The central obstruction to proving the general Fatou Conjecture is the **No Invariant Line Field (NILF) Conjecture**. NILF asserts that a rational map $f$ cannot carry a measurable invariant line field on its Julia set unless $f$ is a Lattès map (a highly specific, classically understood family of maps derived from torus endomorphisms). 

If a "queer component" (an open subset of parameter space devoid of hyperbolic maps) exists, it is a mathematical certainty that for maps in this component, the Julia set must have strictly positive Lebesgue measure ($Area(\mathcal{J}(f)) > 0$) and must support an invariant line field. 

For decades, it was suspected that Julia sets for $P_c(z)$ always had Lebesgue measure zero, which would trivially disprove the existence of line fields. However, Buff and Chéritat (2012) completely derailed this hope by proving that there exist quadratic parameters $c$ whose Julia sets have strictly positive area. Consequently, one cannot rule out invariant line fields simply by ruling out positive measure.

Analytically, the failure of current methods is linked to the degeneration of "Yoccoz puzzles" in the presence of unbounded combinatorics or non-linearizable irrational indifferent fixed points (Cremer points). The standard technique involves constructing annuli $A_n$ around the critical point. If the sum of the moduli of these annuli diverges ($\sum mod(A_n) = \infty$), quasiconformal rigidity follows. When combinatorics are unbounded, $mod(A_n) \to 0$ too rapidly, the annuli degenerate, and the analytic bounds collapse, preventing the requisite compactness arguments.

## 6. The Gap

The exact mathematical barrier lies between the known geometry of renormalizable polynomials (Section 4) and the wild topological distortions generated by unbounded combinatorics and arbitrary rotational dynamics (Section 1). 

To bridge this gap, one must prove that even when the critical point of an infinitely renormalizable map takes arbitrarily long times to return to the core puzzle piece (causing the relative degree of the polynomial-like return map to skyrocket), the map still retains enough geometric rigidity to forbid an invariant line field. The gap requires a novel metric or conformal invariant that does not degrade to zero when standard conformal moduli degenerate under high-degree pullbacks.

## 7. Current Research (as of June 2026)

Current research is heavily focused on expanding the renormalization theory framework. The introduction of "Pacman Renormalization" by Dudko, Lyubich, and Selinger has provided a promising avenue to handle satellite renormalizations, a major source of unbounded combinatorial complexity.

Another active school of thought investigates the boundary of the Mandelbrot set using techniques derived from Schramm-Loewner Evolution (SLE) and random conformal geometry, attempting to place probabilistic bounds on the existence of queer components. 

Additionally, researchers are pushing towards $Rat_3$ (cubic rational maps), where the parameter space has complex dimension 2. *Frontier claims (verify)* indicate that understanding the intersections of the bifurcation loci for two independent critical points may impose rigidity constraints that paradoxically simplify the line-field obstruction when viewed in higher dimensions.

## 8. Future Work

Leading mathematicians suggest that directly attacking the NILF conjecture via new geometric measure theory methods on the Julia set is the most viable path. Future strategies involve:

1. **Resolving the MLC:** Completing the proof of the Local Connectivity of the Mandelbrot set for the unbounded combinatorics case, which automatically implies the Fatou conjecture for $d=2$.
2. **Generalizing A-Priori Bounds:** Developing robust a-priori bounds for rational maps outside the polynomial locus, specifically addressing the combinatorial explosion caused by multiple wandering critical points.
3. **Measure-Theoretic Ergodicity:** Proving that the action of the rational map on any positive-measure Julia set must be highly ergodic, forcing any hypothetical invariant line field to undergo catastrophic measurable distortion, thereby contradicting its existence.

## 9. Key References

- **[Foundational]** Fatou, P. *Sur les équations fonctionnelles.* Bulletin de la Société Mathématique de France, 1920.
- **[Foundational]** Mañé, R., Sad, P., & Sullivan, D. *On the dynamics of rational maps.* Annales scientifiques de l'École Normale Supérieure, 1983.
- **[SOTA / Recent]** Lyubich, M. *Dynamics of quadratic polynomials, I-II.* Acta Mathematica, 1997.
- **[SOTA / Recent]** Kozlovski, O., Shen, W., & van Strien, S. *Density of hyperbolicity in dimension one.* Annals of Mathematics, 2007.
- **[SOTA / Recent]** Kahn, J., & Lyubich, M. *Local connectivity of Julia sets for infinitely renormalizable quadratic polynomials.* Inventiones Mathematicae, 2009.
- **[SOTA / Recent]** Buff, X., & Chéritat, A. *Quadratic Julia sets with positive area.* Annals of Mathematics, 2012.
- **[Survey]** Milnor, J. *Dynamics in One Complex Variable.* Princeton University Press, 2006.

## 10. Worked Example / Concrete Special Case

To concretize the conjecture, consider the quadratic family $P_c(z) = z^2 + c$. We analyze three specific parameters to observe the transition from hyperbolicity to boundary behavior, and back to hyperbolicity via perturbation.

**Case 1: Hyperbolic ($c = 0$)**
For $P_0(z) = z^2$, the critical point is $c_0 = 0$. The orbit is static: $0 \mapsto 0$. The fixed point at $z=0$ has a multiplier $\lambda = P_0'(0) = 0$. Because $|\lambda| < 1$, the critical point is super-attracting. The Julia set $\mathcal{J}(P_0)$ is the unit circle $S^1$. For any $z \in S^1$, the derivative $|P_0'(z)| = |2z| = 2 > 1$. The map is uniformly expanding on its Julia set, confirming it is hyperbolic.

**Case 2: Hyperbolic ($c = -1$)**
For $P_{-1}(z) = z^2 - 1$, the critical point is $0$. Its orbit is $0 \mapsto -1 \mapsto 0$. This constitutes a super-attracting cycle of period 2. The critical point is absorbed by an attracting cycle, hence $P_{-1}$ is hyperbolic.

**Case 3: Parabolic / Boundary ($c = 1/4$)**
For $P_{1/4}(z) = z^2 + 1/4$, we find the fixed points by solving $z^2 - z + 1/4 = 0$, yielding a double root at $z = 1/2$. The multiplier of this fixed point is $\lambda = P_{1/4}'(1/2) = 2(1/2) = 1$. Because $|\lambda| = 1$, the fixed point is parabolic (neutral), neither strictly attracting nor repelling. The critical point $0$ falls into the basin of this neutral fixed point, meaning $P_{1/4}$ is *not* hyperbolic. It lies exactly on the boundary of the main cardioid of the Mandelbrot set.

**Perturbation to Hyperbolicity**
Consider a microscopic perturbation $c = 1/4 - \epsilon$ for a small real $\epsilon > 0$. The double root splits into two distinct fixed points: $z_\pm = \frac{1 \pm \sqrt{4\epsilon}}{2}$. The multipliers become $\lambda_\pm = P_c'(z_\pm) = 1 \pm \sqrt{4\epsilon}$. 
Notice that $|\lambda_-| = |1 - \sqrt{4\epsilon}| < 1$. The neutral fixed point has bifurcated, birthing an *attracting* fixed point $z_-$. The critical point now strictly converges to $z_-$, meaning $P_{1/4 - \epsilon}$ is hyperbolic. This explicitly demonstrates how a non-hyperbolic map on the boundary is approximated arbitrarily closely by hyperbolic maps, illustrating the topological density mechanism underlying the Fatou Conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*