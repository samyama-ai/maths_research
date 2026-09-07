---
id: 03-geometry/coolidge-conjecture
title: "Coolidge Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Coolidge Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/coolidge-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Coolidge Conjecture (more formally known in modern literature as the **Coolidge-Nagata Conjecture**) asserts that every rational cuspidal curve in the complex projective plane $\mathbb{P}^2_{\mathbb{C}}$ is *rectifiable*. Specifically, if $C \subset \mathbb{P}^2_{\mathbb{C}}$ is an irreducible algebraic curve that is birationally equivalent to the projective line (genus zero) and all of its singularities are unibranch (cusps), then there exists a birational automorphism of the projective plane—a Cremona transformation $\Phi: \mathbb{P}^2 \dashrightarrow \mathbb{P}^2$—such that the strict transform of $C$ under $\Phi$ is a smooth line. 

A complete proof of the conjecture requires demonstrating the existence of such a transformation for any arbitrary configuration of cuspidal singularities that a rational plane curve can legally possess, effectively linking the local analytic data of the singularities to the global birational geometry of $\mathbb{P}^2$.

## 2. Mathematical Foundations

The conjecture operates at the intersection of birational geometry and singularity theory over the complex numbers. 

Let the complex projective plane be $\mathbb{P}^2 = \text{Proj}(\mathbb{C}[X,Y,Z])$. An irreducible curve $C = V(F)$ of degree $d$ is a **rational curve** if its geometric genus $g(C)$ is zero. By the genus formula, this requires the singularities to satisfy:
$$ g(C) = \frac{(d-1)(d-2)}{2} - \sum_{p \in \text{Sing}(C)} \delta_p = 0 $$
where $\delta_p$ is the delta-invariant of the singularity at $p$, measuring the number of "hidden" double points.

A point $p \in \text{Sing}(C)$ is a **cuspidal singularity** (or unibranch singularity) if the local analytical ring $\widehat{\mathcal{O}}_{C,p} \cong \mathbb{C}[[X,Y]] / (F)$ is an integral domain. Equivalently, the completion of the local ring is analytically irreducible, meaning the singularity can be parameterized locally by a single Puiseux series $y = \sum_{i \ge k} a_i x^{i/n}$ where $\gcd(n, i_{\min}) = 1$. Topologically, the link of the singularity $K_p = C \cap S^3_{\epsilon}$ is a connected knot rather than a multi-component link. A curve where all singular points are cuspidal is globally homeomorphic to a 2-sphere $S^2$.

A **Cremona transformation** is a rational map $\Phi: \mathbb{P}^2 \dashrightarrow \mathbb{P}^2$ that admits a rational inverse. The set of all such transformations forms the Cremona group $\text{Cr}_2(\mathbb{C}) \cong \text{Aut}(\mathbb{C}(x,y)/\mathbb{C})$. 

The **strict transform** $\widetilde{C}$ of a curve $C$ under a rational map $\Phi$ is the Zariski closure of the image of the curve restricted to the locus where $\Phi$ is a local isomorphism:
$$ \widetilde{C} = \overline{\Phi(C \setminus \text{Base}(\Phi))} $$
The conjecture states that for any rational cuspidal curve $C$, there exists $\Phi \in \text{Cr}_2(\mathbb{C})$ such that $\widetilde{C} \cong \mathbb{P}^1$ and its degree is $1$.

## 3. History & State of the Art (SOTA)

The problem traces its origins to Julian Lowell Coolidge’s 1931 text *A Treatise on Algebraic Plane Curves*. Coolidge observed that since a line in $\mathbb{P}^2$ is smooth (hence unibranch everywhere) and rational, and because Cremona transformations preserve rationality and the unibranch property at general points, any curve Cremona equivalent to a line must necessarily be a rational cuspidal curve. He naturally posited the converse question: whether all rational cuspidal curves arise in this manner.

Masayoshi Nagata formalized and promoted the problem in his foundational 1960 paper *On rational surfaces I*, elevating it to a recognized conjecture. For decades, the problem resisted general proof, with structural insights accumulating slowly through the classification of low-degree curves and isolated topological invariants. 

**State of the Art:** The conjecture is now **solved**. It was definitively proven by Mariusz Koras and Karol Palka in a landmark 2017 paper published in the *Duke Mathematical Journal*. They bypassed classical Cremona combinatorics by utilizing the Log Minimal Model Program (LMMP) applied to the open surface $U = \mathbb{P}^2 \setminus C$. By rigorously analyzing the log Kodaira dimension $\bar{\kappa}(U)$, they demonstrated that the necessary rectifying contractions unconditionally exist.

## 4. Partial Results / Verified Cases

Prior to the full resolution, the conjecture was verified in several specific regimes:
- **Low Degree Bounds ($d \le 5$):** The conjecture was classically known for cubics (which possess exactly one cusp) and quartics (which can possess up to three cusps, such as the 3-cuspidal quartic).
- **Log Kodaira Dimension $\bar{\kappa} \le 1$:** In the 1990s, Flenner and Zaidenberg constructed infinite families of rational cuspidal curves and proved the conjecture for curves whose complement $\mathbb{P}^2 \setminus C$ has log Kodaira dimension $\bar{\kappa} \le 1$.
- **High Number of Cusps:** In 2014, Palka proved the conjecture for rational cuspidal curves possessing 5 or more singular points. (This result was later revealed to be vacuously true).
- **The "At Most 4 Cusps" Theorem:** In a staggering follow-up to the conjecture's resolution, Koras and Palka proved in 2022 that a rational cuspidal curve in $\mathbb{P}^2$ can have **at most four singular points**. Furthermore, they proved that a rational cuspidal curve with exactly four cusps is unique up to projective equivalence—it must be a specific quintic curve. Thus, the classification space of such curves is far more restricted than historically assumed.

## 5. Principal Obstacles

The Coolidge-Nagata conjecture remained open for over 80 years because classical mathematical techniques were unequipped to handle the immense degrees of freedom in the Cremona group.

- **Failure of Algebraic Topology:** The topological properties of the complement $U = \mathbb{P}^2 \setminus C$ (such as the fundamental group $\pi_1(U)$ calculated via the Zariski-van Kampen theorem) fail to distinguish birational embedding classes. Two curves can have homeomorphic complements but entirely different Cremona equivalences.
- **Failure of Perturbation Theory:** One cannot analytically deform or "smooth out" the curve to simplify the problem. Smoothing a cusp decreases the $\delta$-invariant, which inherently breaks the strict rationality condition ($g=0$) by introducing a non-zero genus. The problem is completely rigid.
- **Intractability of the Cremona Group:** Classical Italian algebraic geometry utilized Noether's Theorem, which states that $\text{Cr}_2(\mathbb{C})$ is generated by projective linear transformations and the standard quadratic transformation $\sigma: [X:Y:Z] \mapsto [YZ:XZ:XY]$. However, applying this algorithmically to a curve of degree $d \gg 1$ requires blowing up highly specific "infinitely near" base points located precisely on the curve's singularities to strictly decrease the degree. Without a guiding functional, guessing this exact sequence of blowups for an arbitrary multiplicity sequence is combinatorially impossible.

## 6. The Gap

The exact mathematical barrier was the transition from *the existence of an ad-hoc rectifying map* to *the existence of a rigid, algorithmically verifiable geometric structure on the resolution space*. 

To cross this gap, Koras and Palka shifted the perspective from the curve $C$ itself to the log geometry of the pair $(X, D)$. Let $\pi: X \to \mathbb{P}^2$ be the minimal log resolution of singularities for the curve $C$, and let $D = \pi^{-1}(C)_{red}$ be the reduced boundary divisor with simple normal crossings. The gap was bridged by defining the correct boundary coefficient $\alpha$ to run the Log Minimal Model Program (LMMP) on the pair $(X, \alpha D)$. 

By choosing $\alpha = \frac{1}{2}$ and tracking the cone of curves for $K_X + \frac{1}{2}D$, Koras and Palka rigorously forced the termination of the Cremona process. They proved that the $K_X + \frac{1}{2}D$-LMMP systematically contracts negative curves in a way that eventually dominates the entire surface, proving that no minimal models exist other than those birational to $\mathbb{P}^2$ or a Hirzebruch surface $\mathbb{F}_n$ where the curve is cleanly contracted to a line.

## 7. Current Research (as of June 2026)

With the Coolidge-Nagata conjecture resolved and the strict upper bound of 4 cusps established, contemporary research led by schools like the Polish Academy of Sciences (IMPAN) has pivoted to complete, explicit algebraic classifications.
- **Multiplicity Sequence Bounds:** Researchers are refining the numerical bounds on the multiplicity sequences of curves with 2 or 3 cusps.
- **Rigidity Conjecture:** Investigating whether all rational cuspidal curves (aside from specific low-degree exceptions) have rigid embeddings in $\mathbb{P}^2$.
- **Frontier claims:** *(frontier — verify)* Complete explicit algebraic classification of the parameter spaces and defining polynomials of all rational cuspidal curves of degree $d \ge 10$ possessing exactly 3 cusps.

## 8. Future Work

Leading algebraic geometers articulate several open pathways stemming from this resolution:
1. **Higher-Dimensional Cremona Equivalences:** Generalizing the Coolidge-Nagata framework to rational unibranch surfaces in $\mathbb{P}^3$. Can every such surface be mapped to a plane via a 3-dimensional Cremona transformation?
2. **Applications to the Jacobian Conjecture:** Utilizing the LMMP on open surfaces (specifically $U = \mathbb{P}^2 \setminus C$) to study the topology of fibers of polynomial maps in affine geometry, providing new angles on the Jacobian Conjecture.
3. **Exotic Open Surfaces:** Exploring the existence of non-rectifiable rational cuspidal curves when the ambient space is relaxed from $\mathbb{P}^2$ to a singular rational surface or a Del Pezzo surface with specific ADE singularities.

## 9. Key References

- **[Foundational]** Coolidge, J. L. *A Treatise on Algebraic Plane Curves*. Oxford University Press, 1931. (Dover reprint 1959).
- **[Foundational]** Nagata, M. *On rational surfaces I*. Memoirs of the College of Science, University of Kyoto, Series A: Mathematics, 32(3), 351-370, 1960.
- **[SOTA / Recent]** Koras, M., and Palka, K. *The Coolidge–Nagata conjecture*. Duke Mathematical Journal, 166(16), 3085–3145, 2017.
- **[SOTA / Recent]** Koras, M., and Palka, K. *Complex planar curves homeomorphic to a line have at most four singular points*. Journal de Mathématiques Pures et Appliquées, 158, 255-300, 2022.

## 10. Worked Example / Concrete Special Case

Consider the standard cuspidal cubic curve $C$ in $\mathbb{P}^2$ defined by the homogeneous equation:
$$ Y^2 Z = X^3 $$
This curve has degree $d=3$, genus $g=0$, and a single unibranch cusp at $[0:0:1]$. We will explicitly construct the Cremona transformation that rectifies $C$ to a line.

In the affine chart $Z=1$, the curve is given by $y^2 = x^3$. We define a birational map $\Psi_{aff}: \mathbb{A}^2 \dashrightarrow \mathbb{A}^2$ by:
$$ \Psi_{aff}(x,y) = (u,v) = \left( \frac{y}{x}, \frac{x^3 - y^2}{x^2} \right) $$
Its rational inverse $\Phi_{aff}: \mathbb{A}^2 \dashrightarrow \mathbb{A}^2$ is computed by solving for $x$ and $y$. Note that $y = ux$, yielding $v = (x^3 - u^2 x^2)/x^2 = x - u^2 \implies x = u^2 + v$. Consequently, $y = u(u^2 + v)$. 
Because $\Phi_{aff}(u,v) = (u^2+v, u^3+uv)$ is defined purely by polynomials with an inverse, it is a polynomial automorphism of $\mathbb{A}^2$. Every such automorphism extends to a Cremona transformation of $\mathbb{P}^2$. 

Homogenizing $\Phi_{aff}$ to projective coordinates $[U:V:W] \mapsto [X:Y:Z]$ yields:
$$ \frac{X}{Z} = \left(\frac{U}{W}\right)^2 + \frac{V}{W} = \frac{U^2 W + V W^2}{W^3} \quad \text{and} \quad \frac{Y}{Z} = \left(\frac{U}{W}\right)^3 + \left(\frac{U}{W}\right)\left(\frac{V}{W}\right) = \frac{U^3 + U V W}{W^3} $$
Thus, the Cremona transformation $\Phi: \mathbb{P}^2 \dashrightarrow \mathbb{P}^2$ is explicitly:
$$ \Phi([U:V:W]) = [U^2 W + V W^2 : U^3 + U V W : W^3] $$
We verify that $\Phi$ maps the smooth line defined by $V = 0$ directly onto the cuspidal cubic. Setting $V=0$, the map yields:
$$ X = U^2 W, \quad Y = U^3, \quad Z = W^3 $$
Substituting these into the equation of the cubic $C$:
$$ Y^2 Z = (U^3)^2 (W^3) = U^6 W^3 $$
$$ X^3 = (U^2 W)^3 = U^6 W^3 $$
Since $Y^2 Z = X^3$, the strict transform of the line $V=0$ under $\Phi$ is exactly the cuspidal cubic $C$. The inverse Cremona transformation $\Psi = \Phi^{-1}$ (which maps $C$ to the line $V=0$) successfully rectifies the curve, demonstrating the Coolidge Conjecture for $d=3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*