---
id: 04-topology/cherns-conjecture-on-affine-manifolds
title: "Chern's Conjecture on Affine Manifolds"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chern's Conjecture on Affine Manifolds

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/cherns-conjecture-on-affine-manifolds` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Chern).** Let $M$ be a closed (compact, boundaryless) affine manifold — a smooth manifold equipped with a flat, torsion-free linear connection $\nabla$ on $TM$. Then the Euler characteristic vanishes:
$$\chi(M) = 0.$$

Equivalently, in the $(G,X)$-structure language: if $M$ admits an atlas whose transition maps are restrictions of affine transformations of $\mathbb{R}^n$, then $\chi(M)=0$.

Scope and constraints:

- Only even $n = \dim M$ matters; $\chi = 0$ automatically for odd-dimensional closed manifolds.
- **Torsion-freeness is essential.** Dropping it makes the statement false (Smillie, 1977).
- No completeness, no metric compatibility, and no holonomy restriction is assumed. The holonomy representation $\rho:\pi_1(M)\to \mathrm{Aff}(\mathbb{R}^n)$ may have arbitrarily wild image.
- A **proof** must show $\chi(M)=0$ for every closed affine manifold in every even dimension. A **disproof** is a single closed affine $n$-manifold with $\chi \neq 0$ — the first candidate dimension is $n=4$.

## 2. Mathematical Foundations

**Affine structure.** An affine structure on $M^n$ is a maximal atlas $\{(U_\alpha,\varphi_\alpha)\}$, $\varphi_\alpha: U_\alpha \to \mathbb{R}^n$, with
$$\varphi_\alpha \circ \varphi_\beta^{-1}(x) = A_{\alpha\beta}x + b_{\alpha\beta}, \qquad A_{\alpha\beta}\in \mathrm{GL}(n,\mathbb{R}),\ b_{\alpha\beta}\in\mathbb{R}^n .$$
Pulling back the standard connection of $\mathbb{R}^n$ gives $\nabla$ with curvature $R^\nabla = 0$ and torsion $T^\nabla(X,Y) = \nabla_X Y - \nabla_Y X - [X,Y] = 0$. Conversely, a flat torsion-free $\nabla$ produces such an atlas via affine normal coordinates.

**Developing map and holonomy.** Lifting to the universal cover $\tilde M$ gives an immersion $D:\tilde M \to \mathbb{R}^n$ and $\rho:\pi_1(M)\to\mathrm{Aff}(\mathbb{R}^n) = \mathbb{R}^n \rtimes \mathrm{GL}(n,\mathbb{R})$ with
$$D\circ \gamma = \rho(\gamma)\circ D \quad \forall \gamma\in\pi_1(M).$$
$M$ is **complete** if $D$ is a diffeomorphism onto $\mathbb{R}^n$, i.e. $M = \mathbb{R}^n/\Gamma$ with $\Gamma$ acting properly discontinuously.

**Special affine / radiant.** $M$ is *special* if the linear part $L\circ\rho$ lands in $\mathrm{SL}(n,\mathbb{R})^{\pm}$, equivalently $M$ carries a $\nabla$-parallel volume form $\mathrm{vol}$ with $\nabla \mathrm{vol}=0$. $M$ is *radiant* if $\rho$ has a fixed point in $\mathbb{R}^n$, i.e. $\rho$ is conjugate into $\mathrm{GL}(n,\mathbb{R})$; the obstruction to this is the **radiance obstruction** $c_M \in H^1(\pi_1 M; \mathbb{R}^n_\rho)$ of Goldman–Hirsch.

**Why the usual proof fails.** For a Riemannian metric $g$ with Levi-Civita connection, Chern–Gauss–Bonnet gives
$$\chi(M) = \int_M \mathrm{Pf}\!\left(\frac{\Omega}{2\pi}\right),\qquad \Omega = \text{curvature } 2\text{-form of an } O(n)\text{-connection}.$$
An affine structure gives a flat connection but with structure group $\mathrm{GL}(n,\mathbb{R})$, **not** $O(n)$; the Pfaffian is only $O(n)$-invariant, so the Chern–Weil argument does not apply. What *does* follow from flatness is that all real Pontryagin classes vanish, $p_i(TM)=0$ in $H^{4i}(M;\mathbb{R})$, and that the Euler class is the pullback
$$e(TM) = \rho^*(e) \in H^n(M;\mathbb{R}),\qquad e \in H^n(B\mathrm{GL}(n,\mathbb{R})^{\delta};\mathbb{R}),$$
of a class on the classifying space of $\mathrm{GL}(n,\mathbb{R})$ **as a discrete group**. Chern's conjecture asserts $\rho^*(e)=0$ whenever $\rho$ arises from a torsion-free flat structure. Because $\chi(M) = \langle e(TM),[M]\rangle$, this is exactly the statement above.

## 3. History & State of the Art (SOTA)

- **1950s.** Shiing-Shen Chern raised the question in the course of his work on characteristic classes of $G$-structures; it is recorded in his survey *The geometry of $G$-structures* (Bull. AMS, 1966) and became standard as "Chern's conjecture" after Kostant–Sullivan.
- **1955–1960.** J.-P. Benzécri's thesis and paper classify closed affine surfaces: only the torus and Klein bottle occur, so $\chi=0$ in dimension 2.
- **1958.** Milnor's inequality: an oriented rank-2 bundle $E \to \Sigma_g$ admits a flat connection iff $|e(E)| < g$. Applied to $E=T\Sigma_g$ this re-proves the surface case in one line (see §10).
- **1971–1976.** Wood extends Milnor's bound to $\mathrm{Homeo}^+(S^1)$; Sullivan generalizes Milnor's inequality to affine foliations and higher-dimensional flat bundles.
- **1975.** Kostant–Sullivan: $\chi = 0$ for **complete** affine manifolds. Hirsch–Thurston: vanishing Euler class for flat bundles with amenable (more generally, "class $\mathcal{A}$") holonomy.
- **1977.** Smillie constructs, for each even $n\ge 4$, a closed $n$-manifold with $\chi\neq 0$ whose tangent bundle carries a flat connection **with torsion**. This shows the conjecture is genuinely about torsion-freeness and blocks all purely bundle-theoretic attacks.
- **1984.** Goldman–Hirsch introduce the radiance obstruction; radiant affine manifolds have a nowhere-zero radiant vector field, hence $\chi=0$.
- **2011.** Bucher–Gelander prove the generalized conjecture for closed manifolds locally a product of hyperbolic surfaces, via a sharp Milnor–Wood inequality.
- **2017 (SOTA).** Klingler, *Chern's conjecture for special affine manifolds* (Annals of Mathematics 186, 69–95): $\chi(M)=0$ whenever $M$ is closed affine and carries a parallel volume form. This is the deepest result to date and uses simplicial volume / bounded cohomology together with algebraic-group arguments.

No general case beyond "special" is known; no counterexample is known.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\dim M \le 3$ | $\chi=0$ (dim 2 by classification/Milnor; dims 1,3 trivially odd) | Benzécri 1960; Milnor 1958 |
| Complete affine manifolds $\mathbb{R}^n/\Gamma$, all $n$ | $\chi=0$ | Kostant–Sullivan 1975 |
| Special affine (parallel volume form), all $n$ | $\chi=0$ | Klingler 2017 |
| Radiant affine manifolds | $\chi=0$ (nonvanishing vector field) | Goldman–Hirsch 1984 |
| Amenable / virtually solvable / nilpotent holonomy | $e(TM)=0$ | Hirsch–Thurston 1975; Fried–Goldman–Hirsch 1981 |
| Holonomy in $\mathrm{SL}(2,\mathbb{R})^k$; locally products of surfaces | $\chi=0$; sharp Milnor–Wood $|\chi| \le 2^{-k}|\chi_{\text{top}}|$-type bounds | Bucher–Gelander 2011 |
| Flat bundles over $\Sigma_g$, rank 2 | $|e| < g$ (sharp) | Milnor 1958, Wood 1971 |
| Torsion allowed | **False** for all even $n\ge 4$ | Smillie 1977 |

The smallest open case: a closed affine $4$-manifold with $\chi \neq 0$ and no parallel volume form (necessarily with non-amenable, non-radiant holonomy whose linear part escapes $\mathrm{SL}(4,\mathbb{R})^{\pm}$).

## 5. Principal Obstacles

- **No invariant metric, no Gauss–Bonnet.** The Pfaffian polynomial is $O(n)$-invariant but not $\mathrm{GL}(n,\mathbb{R})$-invariant, so Chern–Weil produces $0$ for Pontryagin classes but says nothing about $e$. Any proof must be topological or dynamical, not curvature-integral.
- **Smillie's obstruction.** Since flat-with-torsion counterexamples exist in every even dimension $\ge 4$, any successful method must *use torsion-freeness*, i.e. must see the developing map, not merely the flat bundle $\rho$. Almost all vanishing theorems for Euler classes (Milnor–Wood, bounded cohomology, amenability) are properties of $\rho$ alone and therefore cannot suffice unaided.
- **Bounded cohomology is not bounded enough.** Milnor–Wood-type arguments show $e$ is a bounded class in $H^n_b$, giving $|\chi(M)| \le C_n \|M\|$ (simplicial volume). This kills the conjecture only when $\|M\|=0$ or $C_n$ is small; the sharp constant $C_n$ for $\mathrm{GL}(n,\mathbb{R})^{\delta}$ in $n \ge 4$ is unknown, and the naive bounds are far too weak.
- **Wildness of developing maps.** $D$ need not be injective or a covering. Non-complete affine structures on tori (Sullivan–Thurston, Fried–Goldman–Hirsch) show developing images can be complicated open subsets of $\mathbb{R}^n$, so no normal-form or convexity hypothesis is available.
- **Loss of algebraic structure without parallel volume.** Klingler's proof exploits that the Zariski closure of a volume-preserving holonomy is a unimodular algebraic group, feeding Ratner-type / algebraic-group rigidity. Dropping the volume form permits determinant characters $\det\circ L\circ\rho : \pi_1 M \to \mathbb{R}^{\times}$ with dense image and destroys this input.
- **Markus's conjecture is itself open.** The statement "compact affine $\Rightarrow$ (complete $\iff$ parallel volume)" would combine with Kostant–Sullivan to recover Klingler's theorem, but is unproved even in dimension 3.

## 6. The Gap

Proven: $\chi=0$ when the holonomy is *volume-preserving* (Klingler), *amenable* (Hirsch–Thurston), or *has a fixed point* (radiant). In each case one has a structure — a $\rho$-invariant measure/volume class, an invariant mean, or an invariant point — from which vanishing is extracted.

The general statement has none of these. The precise missing step: **show that the pullback $\rho^*e \in H^n(M;\mathbb{R})$ vanishes for the holonomy of a torsion-free flat structure whose linear part is not unimodular.** Concretely one must either

1. produce a torsion-free-sensitive refinement of the Milnor–Wood inequality — a bound $|\chi(M)| < f(M)$ where $f$ uses the developing map and defeats Smillie's examples; or
2. prove Markus's conjecture, reducing the non-unimodular case to completeness; or
3. exhibit a closed affine $4$-manifold with $\chi \ne 0$.

## 7. Current Research (as of June 2026)

- **Bounded cohomology of $\mathrm{GL}(n,\mathbb{R})^\delta$.** Extending Bucher–Gelander's sharp Milnor–Wood constants beyond products of surfaces; groups at ETH Zürich, Geneva and Regensburg (Bucher, Monod, Löh school) pursue norms of the Euler class in $H^n_b$. Sharp constants in $n=4$ remain unknown. *(frontier — verify)*
- **Algebraic-group and homogeneous-dynamics methods.** Follow-ups to Klingler's Annals paper attempt to relax "parallel volume" to "unimodular Zariski closure of the linear holonomy", using Ratner/Benoist–Quint machinery on the developing image. *(frontier — verify)*
- **Markus conjecture programme.** Work on compact affine 3- and 4-manifolds, and on the related Auslander conjecture for complete affine manifolds (Abels–Margulis–Soifer resolved dimensions $\le 6$; later work pushes further), continues at Maryland, Bar-Ilan and Bonn. *(frontier — verify)*
- **Special geometries.** Chern's conjecture is known for affine manifolds admitting a compatible complex/symplectic/Hessian structure by ad hoc arguments; a systematic survey of which $G$-structures force vanishing is an active thread, tied to Hessian geometry and mirror symmetry (affine structures with singularities on Calabi–Yau base manifolds).
- **Search for counterexamples.** Computational constructions of affine crystallographic-like groups and of exotic affine structures on 4-manifolds with $\chi\neq0$; no candidate has survived.

## 8. Future Work

- Prove Markus's conjecture in dimension 4; this alone would settle the first open case.
- Find a *torsion-sensitive* invariant: a cochain-level construction of the Euler class using affine normal coordinates that is bounded with constant $< 1$ per simplex, so that $|\chi| < \|M\|/\|\cdot\|$ forces $\chi=0$ where Smillie's flat-with-torsion bundles fail the same bound.
- Compute or bound $\|e\|_\infty$ for $\mathrm{GL}(4,\mathbb{R})^\delta$ and for $\mathrm{Aff}(\mathbb{R}^4)$.
- Extend Klingler's argument to holonomies whose determinant character has discrete or virtually cyclic image (the "almost unimodular" case).
- Classify closed affine 4-manifolds with nilpotent or solvable fundamental group; test whether any construction can be perturbed to $\chi\neq0$.

## 9. Key References

- **[Foundational]** S.-S. Chern. *The geometry of $G$-structures.* Bulletin of the American Mathematical Society **72** (1966), 167–219.
- **[Foundational]** J.-P. Benzécri. *Sur les variétés localement affines et localement projectives.* Bulletin de la Société Mathématique de France **88** (1960), 229–332. [DOI](https://doi.org/10.24033/bsmf.1551)
- **[Foundational]** J. Milnor. *On the existence of a connection with curvature zero.* Commentarii Mathematici Helvetici **32** (1958), 215–223. [DOI](https://doi.org/10.1007/bf02564579)
- **[Foundational]** J. W. Wood. *Bundles with totally disconnected structure group.* Commentarii Mathematici Helvetici **46** (1971), 257–273. [DOI](https://doi.org/10.1007/bf02566843)
- **[Foundational]** B. Kostant and D. Sullivan. *The Euler characteristic of an affine space form is zero.* Bulletin of the American Mathematical Society **81** (1975), 937–938. [DOI](https://doi.org/10.1090/s0002-9904-1975-13896-1)
- **[Foundational]** M. Hirsch and W. Thurston. *Foliated bundles, invariant measures and flat manifolds.* Annals of Mathematics **101** (1975), 369–390. [DOI](https://doi.org/10.1007/bfb0082577)
- **[Foundational]** D. Sullivan. *A generalization of Milnor's inequality concerning affine foliations and affine manifolds.* Commentarii Mathematici Helvetici **51** (1976), 183–189. [DOI](https://doi.org/10.1007/bf02568150)
- **[Foundational]** J. Smillie. *Flat manifolds with non-zero Euler characteristics.* Commentarii Mathematici Helvetici **52** (1977), 453–455. [DOI](https://doi.org/10.1007/bf02567378)
- **[Foundational]** W. Goldman and M. Hirsch. *The radiance obstruction and parallel forms on affine manifolds.* Transactions of the American Mathematical Society **286** (1984), 629–649. [DOI](https://doi.org/10.1090/s0002-9947-1984-0760977-7)
- **[Foundational]** D. Fried, W. Goldman and M. Hirsch. *Affine manifolds with nilpotent holonomy.* Commentarii Mathematici Helvetici **56** (1981), 487–523. [DOI](https://doi.org/10.1007/bf02566225)
- **[SOTA / Recent]** B. Klingler. *Chern's conjecture for special affine manifolds.* Annals of Mathematics (2) **186** (2017), 69–95. [DOI](https://doi.org/10.4007/annals.2017.186.1.2)
- **[SOTA / Recent]** M. Bucher and T. Gelander. *The generalized Chern conjecture for manifolds that are locally a product of surfaces.* Advances in Mathematics **228** (2011), 1503–1542. [DOI](https://doi.org/10.1016/j.aim.2011.06.022)
- **[Survey]** W. Goldman. *Geometric structures on manifolds and varieties of representations.* In *Geometry of Group Representations*, Contemporary Mathematics **74**, AMS, 1988, 169–198. [DOI](https://doi.org/10.1090/conm/074/957518)
- **[Survey]** J. Milnor. *On fundamental groups of complete affinely flat manifolds.* Advances in Mathematics **25** (1977), 178–187. [DOI](https://doi.org/10.1016/0001-8708(77)90004-4)

## 10. Worked Example / Concrete Special Case

**Dimension 2, via Milnor's inequality.** Let $\Sigma_g$ be a closed oriented surface of genus $g$ with an affine structure. Then $T\Sigma_g$ carries a flat $\mathrm{GL}^+(2,\mathbb{R})$-connection, so $T\Sigma_g$ is the flat bundle of some $\rho:\pi_1\Sigma_g \to \mathrm{GL}^+(2,\mathbb{R})$.

Milnor's theorem (1958): an oriented rank-2 bundle $E\to\Sigma_g$, $g\ge 1$, admits a flat connection **iff**
$$|e(E)| < g .$$
For $E = T\Sigma_g$, Poincaré–Hopf gives $e(T\Sigma_g) = \chi(\Sigma_g) = 2-2g$. Check each genus:

- $g=0$: $S^2$. Flatness would need $|2| < 0$ — impossible. (Directly: $\pi_1 = 1$ forces $T S^2$ trivial, contradicting $\chi=2$.)
- $g=1$: $|e| = |2-2\cdot 1| = 0 < 1$. Allowed, and $\chi = 0$. ✔
- $g=2$: $|e| = 2$, need $2 < 2$ — false.
- $g\ge 2$ generally: $|e| = 2g-2 \ge g \iff g \ge 2$, so the inequality fails.

Hence only $g=1$ survives: every closed orientable affine surface is a torus, $\chi=0$. The Klein bottle is the non-orientable case, also $\chi=0$. This matches Benzécri's classification.

**Explicit affine tori.** Two inequivalent structures on $T^2$, both with $\chi=0$:

1. *Complete:* $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, $\rho(\gamma) = x \mapsto x+\gamma$, developing map $D=\mathrm{id}$.
2. *Incomplete (radiant):* let $\Gamma \subset \mathrm{GL}^+(2,\mathbb{R})$ be generated by $A = \mathrm{diag}(2,2)$ and $B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ acting on the half-plane $\Omega=\{(x,y): y>0\}$; the quotient $\Omega/\Gamma$ is a torus with a non-complete affine structure whose developing image is $\Omega \subsetneq \mathbb{R}^2$. Here $D$ is a diffeomorphism onto $\Omega$ only, and $\rho$ fixes $0\in\mathbb{R}^2$, so the radiance obstruction vanishes and the radiant vector field $\sum x_i\partial_{x_i}$ descends to a nowhere-zero field — an independent proof that $\chi=0$.

**Where the argument stops.** In dimension 4 the analogue of Milnor's sharp bound is unavailable: the norm of the Euler class in $H^4_b(\mathrm{GL}(4,\mathbb{R})^\delta;\mathbb{R})$ is not known, and Smillie's flat-with-torsion 4-manifolds with $\chi \ne 0$ prove that no bound depending on $\rho$ alone can be strong enough. Torsion-freeness must enter, and no one knows how to make it enter.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*