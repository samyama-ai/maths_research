---
id: 06-pdes/plateau-problem-uniqueness
title: "Plateau Problem Uniqueness"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Plateau Problem Uniqueness

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/plateau-problem-uniqueness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Existence for Plateau's problem is settled: every rectifiable Jordan curve $\Gamma \subset \mathbb{R}^3$ bounds a minimal surface of disk type of least area (Douglas 1931, Radó 1930). **Uniqueness is not.** The problem is to decide, for which curves and in what sense the minimizer — or the full set of critical points — is unique or finite.

Three precise questions, all open in the stated generality:

- **(Q1) Analytic finiteness.** Does every real-analytic Jordan curve $\Gamma \subset \mathbb{R}^3$ bound only *finitely many* minimal disks (all conformal harmonic solutions, not just minimizers)?
- **(Q2) Nitsche without analyticity.** Nitsche (1973) proved that a real-analytic Jordan curve with total curvature $\int_\Gamma |\kappa|\,ds \le 4\pi$ bounds exactly one minimal disk. Does the same hold for merely $C^2$ (or $C^{1,1}$) curves?
- **(Q3) Effective genericity.** Morgan (1978) proved that a *generic* $C^{k,\alpha}$ curve in $\mathbb{R}^3$ bounds a unique area-minimizing surface. Is there a checkable, non-Baire criterion — a curvature, torsion, or geometric condition — certifying uniqueness for a given curve?

A complete resolution of (Q1) means either a proof of finiteness or an explicit real-analytic $\Gamma$ bounding a continuum of minimal disks. For (Q2), a proof or a $C^2$ counterexample with two minimal disks and total curvature $\le 4\pi$.

## 2. Mathematical Foundations

Let $D = \{ w = u+iv : |w| < 1 \}$ and let $\Gamma \subset \mathbb{R}^3$ be a Jordan curve. A map $X \in C^0(\bar D, \mathbb{R}^3) \cap C^2(D,\mathbb{R}^3)$ solves Plateau's problem for $\Gamma$ if

$$\Delta X = 0 \quad \text{in } D, \qquad |X_u|^2 = |X_v|^2, \quad \langle X_u, X_v\rangle = 0 \quad \text{in } D,$$

and $X|_{\partial D} : \partial D \to \Gamma$ is a monotone homeomorphism. The conformality relations are equivalent to the vanishing of the Hopf differential

$$\Phi(w) = \langle X_w, X_w \rangle \, dw^2, \qquad X_w = \tfrac12 (X_u - i X_v),$$

which is holomorphic for harmonic $X$; hence $\Phi \equiv 0$ can be tested at a point. Where $\nabla X \neq 0$ the image is a minimal surface, $H \equiv 0$. Zeros of $\nabla X$ are **branch points**; interior branch points of order $m$ satisfy $X_w(w) = a(w-w_0)^m + O(|w-w_0|^{m+1})$ with $\langle a,a\rangle = 0$.

Energy and area,
$$E(X) = \tfrac12\int_D |\nabla X|^2\,du\,dv, \qquad A(X) = \int_D |X_u \wedge X_v|\,du\,dv,$$
satisfy $A(X) \le E(X)$ with equality iff $X$ is conformal. Douglas minimized the boundary functional
$$\mathcal{A}(\gamma) = \frac{1}{16\pi}\int_0^{2\pi}\!\!\int_0^{2\pi} \frac{|\gamma(\theta)-\gamma(\varphi)|^2}{\sin^2\!\big(\tfrac{\theta-\varphi}{2}\big)}\,d\theta\,d\varphi$$
over monotone parametrizations $\gamma$ of $\Gamma$; $\mathcal{A}(\gamma) = E(X_\gamma)$ for the harmonic extension.

**Second variation.** For an immersed minimal $\Sigma$ with unit normal $\nu$ and second fundamental form $A$, normal variations $\varphi\nu$, $\varphi|_{\partial\Sigma}=0$, give
$$\delta^2 A(\varphi,\varphi) = \int_\Sigma \big(|\nabla \varphi|^2 - |A|^2\varphi^2\big)\,d\mu = -\int_\Sigma \varphi\, L\varphi\,d\mu, \qquad L = \Delta_\Sigma + |A|^2 .$$
$\Sigma$ is **nondegenerate** if the Dirichlet problem $L\varphi = 0$, $\varphi|_{\partial\Sigma}=0$ has only $\varphi \equiv 0$; nondegeneracy plus the implicit function theorem gives *local* uniqueness and smooth dependence on $\Gamma$. **Stable** means $\delta^2 A \ge 0$; the Morse index is the number of negative eigenvalues of $L$.

The relevant boundary quantity for Nitsche-type theorems is the total curvature $\tau(\Gamma) = \int_\Gamma |\kappa|\,ds$; by Fenchel, $\tau \ge 2\pi$, and by Fáry–Milnor $\tau > 4\pi$ for knotted $\Gamma$.

## 3. History & State of the Art (SOTA)

- **1930–31.** Radó (*Ann. of Math.* 31) and Douglas (*Trans. AMS* 33) independently solve existence. Radó (*Math. Z.* 32, 1930) proves the first uniqueness theorem: if $\Gamma$ projects bijectively onto a convex plane curve, the minimal disk is unique and is a graph.
- **1930s–50s.** Explicit non-uniqueness: contours (Douglas, Courant, Lévy) bounding several, and even a continuum of, minimal disks. Morse–Tompkins (1939) and Shiffman (1939): if $\Gamma$ bounds two strictly stable minimal disks, it bounds a third, unstable one — so non-uniqueness is never "just two".
- **1973.** Nitsche's uniqueness theorem: real-analytic $\Gamma$ with $\tau(\Gamma) \le 4\pi$ bounds exactly one minimal disk. Tomi proves that a real-analytic $\Gamma$ bounds only finitely many *least-area* disks.
- **1976–78.** Morgan constructs a smooth curve in $\mathbb{R}^4$ bounding a continuum of area-minimizing surfaces, then proves that almost every curve in $\mathbb{R}^3$ (Baire-generic in $C^{k,\alpha}$) bounds a unique area-minimizing surface.
- **1981.** Böhme–Tromba's index theorem: for a generic contour the minimal disks are nondegenerate and, in $\mathbb{R}^n$ with $n \ge 4$, finite in number — a global-analysis (Fredholm, Sard–Smale) framework replacing ad hoc arguments.
- **1982.** Meeks–Yau: for $\Gamma$ on the boundary of a mean-convex body, least-area disks are embedded; this reduces uniqueness questions to the embedded category.
- **2002.** Ekholm–White–Wienholtz: any minimal surface (any genus, branched allowed) bounded by $\Gamma$ with $\tau(\Gamma) \le 4\pi$ is embedded and, for $\tau < 4\pi$, unbranched and unique in its class — removing analyticity from the *embeddedness* half of Nitsche's theorem.
- **2010.** Coskunuzer: generic uniqueness of area-minimizing disks for extreme curves (curves on the boundary of a convex body).

SOTA summary: uniqueness is known under (i) a graph/convex-projection hypothesis, (ii) small total curvature with analyticity, (iii) genericity. Nothing certifies uniqueness for an arbitrary given smooth curve.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\Gamma$ projects bijectively onto a convex plane curve | unique minimal disk, a graph over the convex domain | Radó 1930 |
| $\Gamma$ real-analytic, $\tau(\Gamma) \le 4\pi$ | exactly one minimal disk; embedded | Nitsche 1973 |
| $\Gamma$ rectifiable, $\tau(\Gamma) \le 4\pi$ | every bounded minimal surface, any genus, is embedded ($<4\pi$: unbranched) | Ekholm–White–Wienholtz 2002 |
| $\Gamma$ real-analytic | finitely many least-area disks | Tomi 1973 |
| generic $\Gamma \subset \mathbb{R}^n$, $n \ge 4$ | finitely many minimal disks, all nondegenerate | Böhme–Tromba 1981 |
| generic $\Gamma \subset \mathbb{R}^3$, $C^{k,\alpha}$, $k\ge 3$ | unique area-minimizing surface | Morgan 1978 |
| generic extreme $\Gamma$ (on $\partial K$, $K$ convex) | unique area-minimizing disk | Coskunuzer 2010 |
| $\Gamma$ a small $C^{2,\alpha}$ perturbation of a plane curve | unique, by nondegeneracy + implicit function theorem | standard; Dierkes–Hildebrandt–Tromba |
| $\Gamma \subset \partial K$, $K$ mean-convex | least-area disks embedded, unknotted | Meeks–Yau 1982 |

Sharp non-uniqueness benchmarks: a smooth curve in $\mathbb{R}^4$ with a continuum of minimizers (Morgan 1976); contours in $\mathbb{R}^3$ with three or more minimal disks (Morse–Tompkins/Shiffman mechanism); coaxial-circle boundaries with exactly two catenoids (Section 10).

## 5. Principal Obstacles

- **The problem is not elliptic in $\Gamma$.** The map $\Gamma \mapsto \{\text{minimal disks}\}$ is a Fredholm-index-$0$ setting, not a contraction. Maximum-principle and comparison arguments — the workhorses for uniqueness of Dirichlet problems — apply only when the surfaces are graphs over a common domain. Two minimal disks spanning a knotted or highly non-planar $\Gamma$ generically intersect transversally, and there is no ordering to run a sliding/Alexandrov reflection argument on.
- **Branch points.** In $\mathbb{R}^3$ the moduli space of minimal disks is stratified by branching type. Boundary branch points are not excluded by Gulliver–Osserman–Royden-type theorems in all regimes, and the Fredholm structure degenerates on the branched strata. This is exactly why Böhme–Tromba's finiteness statement is clean for $n \ge 4$ and delicate for $n = 3$.
- **Genericity is non-constructive.** Morgan's and White's transversality results give a residual set in a Baire space. Residual sets carry no measure-theoretic or verifiable content: no algorithm decides whether the circle-like curve on your desk lies in it.
- **Analyticity is used essentially.** Nitsche's proof exploits analytic continuation across $\Gamma$ and unique continuation for the Gauss map; a $C^2$ curve gives no such extension, and the boundary regularity available ($C^{1,\alpha}$ up to $\partial D$) is too weak to run the argument.
- **Degeneracy is a codimension-one phenomenon.** Bifurcation occurs precisely when $L$ has a Dirichlet kernel; the catenoid family shows this happens along explicit one-parameter deformations, so any general uniqueness theorem must contain a mechanism ruling out $\ker L \ne 0$, and no geometric quantity on $\Gamma$ is known to control it beyond total curvature.

## 6. The Gap

Proven: uniqueness under a *geometric smallness or graphicality* hypothesis ($\tau \le 4\pi$ with analyticity; convex projection), or under a *generic* hypothesis. Asserted: a structural dichotomy for every smooth curve.

The precise missing step is a **compactness-plus-transversality statement without genericity**: show that for a fixed real-analytic (or $C^\infty$) $\Gamma$, the solution set $\mathcal{M}(\Gamma) \subset H^{1/2}(\partial D,\Gamma)$ of conformal harmonic disks is finite, i.e. that a degenerate solution ($\ker L \ne 0$) cannot occur in a positive-dimensional family. Equivalently: rule out a nontrivial Jacobi field vanishing on $\partial\Sigma$ arising as the tangent to a curve of solutions with fixed boundary. Tomi 1973 does this for *minimizers* via analyticity of the Douglas functional's critical set; extending it to unstable critical points and to $C^\infty$ boundaries is the open boundary. For (Q2) the gap is narrower: EWW supplies embeddedness and unbranchedness for $\tau < 4\pi$; what remains is to upgrade "every solution is an embedded disk" to "there is only one", without analytic continuation.

## 7. Current Research (as of June 2026)

- **Global analysis / Morse theory schools** (successors of the Tromba–Böhme program; Bonn, Duisburg-Essen, Leipzig): index theorems for boundary-branched strata and Morse-theoretic counts of unstable minimal disks. Structural results are in the Dierkes–Hildebrandt–Tromba volumes; incremental refinements continue.
- **Geometric measure theory** (Stanford/White school): generic uniqueness and finiteness for varying metrics and boundaries, following White's transversality theory; extensions to minimizers in Riemannian $3$-manifolds and to free-boundary Plateau problems.
- **Small-total-curvature program**: attempts to remove analyticity from Nitsche's theorem using EWW's monotonicity/Gauss-map cone arguments rather than analytic continuation. *(frontier — verify)*
- **Asymptotic Plateau problem in $\mathbb{H}^3$** (Coskunuzer and collaborators): generic uniqueness for asymptotic boundaries at infinity; a testbed where the boundary data are more flexible than in $\mathbb{R}^3$.
- **Numerical/computational**: discrete minimal surface solvers (Brakke's Surface Evolver lineage, discrete conformal methods) used to hunt for a real-analytic curve with many minimal disks; no candidate counterexample to (Q1) has been reported. *(frontier — verify)*

## 8. Future Work

- Prove or disprove finiteness of $\mathcal{M}(\Gamma)$ for every real-analytic $\Gamma \subset \mathbb{R}^3$; the natural attack is real-analyticity of the Douglas functional on the boundary-parametrization manifold plus Łojasiewicz-type structure of its critical set.
- Extend Tomi's local-uniqueness argument from least-area disks to all stable disks, then to bounded-index critical points.
- Find an explicit, checkable sufficient condition for uniqueness in terms of $\tau(\Gamma)$, writhe, and torsion — a quantitative substitute for Morgan's genericity.
- Settle whether every $C^2$ curve with $\tau \le 4\pi$ bounds a unique minimal disk; a counterexample would be as informative as a proof.
- Understand the codimension of the non-uniqueness locus in $C^{k,\alpha}$ curve space: is it $1$, as the catenoid bifurcation suggests?

## 9. Key References

- **[Foundational]** T. Radó. *On Plateau's problem.* Annals of Mathematics **31** (1930), 457–469.
- **[Foundational]** T. Radó. *The problem of the least area and the problem of Plateau.* Mathematische Zeitschrift **32** (1930), 763–796.
- **[Foundational]** J. Douglas. *Solution of the problem of Plateau.* Transactions of the AMS **33** (1931), 263–321.
- **[Foundational]** R. Courant. *Dirichlet's Principle, Conformal Mapping, and Minimal Surfaces.* Interscience, 1950.
- **[Foundational]** M. Morse, C. Tompkins. *The existence of minimal surfaces of general critical types.* Annals of Mathematics **40** (1939), 443–472.
- **[Foundational]** M. Shiffman. *The Plateau problem for non-relative minima.* Annals of Mathematics **40** (1939), 834–854.
- **[Uniqueness]** J. C. C. Nitsche. *A new uniqueness theorem for minimal surfaces.* Archive for Rational Mechanics and Analysis **52** (1973), 319–329.
- **[Uniqueness]** F. Tomi. *On the local uniqueness of the problem of least area.* Archive for Rational Mechanics and Analysis **52** (1973), 312–318.
- **[Non-uniqueness]** F. Morgan. *A smooth curve in $\mathbb{R}^4$ bounding a continuum of area minimizing surfaces.* Duke Mathematical Journal **43** (1976), 867–870.
- **[Genericity]** F. Morgan. *Almost every curve in $\mathbb{R}^3$ bounds a unique area minimizing surface.* Inventiones Mathematicae **45** (1978), 253–297.
- **[Structural]** R. Böhme, A. J. Tromba. *The index theorem for classical minimal surfaces.* Annals of Mathematics **113** (1981), 447–499.
- **[SOTA]** T. Ekholm, B. White, D. Wienholtz. *Embeddedness of minimal surfaces with total boundary curvature at most $4\pi$.* Annals of Mathematics **155** (2002), 209–234.
- **[SOTA]** B. Coskunuzer. *Generic uniqueness of area minimizing disks for extreme curves.* American Journal of Mathematics **132** (2010), 1091–1104.
- **[Embeddedness]** W. Meeks III, S.-T. Yau. *The classical Plateau problem and the topological structure of three-dimensional manifolds.* Topology **21** (1982), 409–442.
- **[Transversality]** B. White. *The space of minimal submanifolds for varying Riemannian metrics.* Indiana University Mathematics Journal **40** (1991), 161–200.
- **[Survey]** J. C. C. Nitsche. *Lectures on Minimal Surfaces, Vol. 1.* Cambridge University Press, 1989.
- **[Survey]** U. Dierkes, S. Hildebrandt, F. Sauvigny. *Minimal Surfaces.* Grundlehren 339, Springer, 2nd ed., 2010.
- **[Survey]** U. Dierkes, S. Hildebrandt, A. J. Tromba. *Global Analysis of Minimal Surfaces.* Grundlehren 341, Springer, 2010.
- **[Survey]** M. Struwe. *Plateau's Problem and the Calculus of Variations.* Mathematical Notes 35, Princeton University Press, 1988.

## 10. Worked Example / Concrete Special Case

**Two coaxial circles: exactly two minimal annuli, then none.** Take
$$\Gamma_h = \{ x^2+y^2 = 1, \ z = h \} \cup \{ x^2+y^2 = 1, \ z = -h \}, \qquad h > 0 .$$
Rotationally symmetric minimal surfaces spanning $\Gamma_h$ are catenoids
$$r(z) = c \cosh(z/c), \qquad c > 0,$$
(the profile solves $r r'' = 1 + (r')^2$, the minimal surface of revolution equation). The boundary condition $r(\pm h) = 1$ gives
$$c \cosh(h/c) = 1 .$$
Set $t = h/c$, so $c = 1/\cosh t$ and
$$h = f(t) := \frac{t}{\cosh t}.$$
$f(0)=0$, $f(t) \to 0$ as $t \to \infty$, and $f'(t) = 0$ iff $t \tanh t = 1$, i.e. $t_\ast \approx 1.19968$. Then
$$h_\ast = f(t_\ast) = \frac{1.19968}{\cosh(1.19968)} \approx \frac{1.19968}{1.81017} \approx 0.66274 .$$

Consequently:

- $h < h_\ast$: **two** solutions $t_1 < t_\ast < t_2$, hence two catenoids. The shallow one ($t_1$, larger neck $c_1 = 1/\cosh t_1$) is stable; the deep one ($t_2$) has Morse index $1$. Example $h = 0.5$: solving $t/\cosh t = 0.5$ gives $t_1 \approx 0.5893$ ($c_1 \approx 0.8484$) and $t_2 \approx 2.1268$ ($c_2 \approx 0.2351$). Neck radii $0.8484$ and $0.2351$ — visibly different surfaces with the same boundary.
- $h = h_\ast$: the two merge into a single **degenerate** catenoid, $\ker L \neq 0$ — a fold bifurcation.
- $h > h_\ast$: no catenoid at all; the area-minimizing *current* is the pair of flat disks (Goldschmidt solution), of area $2\pi$.

This is the cleanest picture of the failure mode. Uniqueness fails on a set of boundary data of codimension $0$ (an open interval of $h$), and the transition at $h_\ast$ is exactly the degeneracy $\ker L \ne 0$ that Section 6 must exclude. Note also that $\Gamma_h$ is real-analytic but *not* a Jordan curve, and the surfaces are annuli, not disks; the open questions (Q1)–(Q3) ask whether a connected, disk-type analogue of this bifurcation can persist in a positive-dimensional family. Contrast Radó: if instead $\Gamma$ is a Jordan curve projecting bijectively onto the unit circle in the $xy$-plane, the unique minimal disk is the graph $z = u(x,y)$ solving
$$(1+u_y^2)u_{xx} - 2u_xu_yu_{xy} + (1+u_x^2)u_{yy} = 0, \qquad u|_{\partial D} = \text{given},$$
and uniqueness follows immediately from the maximum principle applied to the difference of two graph solutions — the comparison structure that the catenoid pair, being non-graphical over any common domain, destroys.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*