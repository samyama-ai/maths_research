---
id: 06-pdes/local-isometric-embedding
title: "Local Isometric Embedding"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Local Isometric Embedding

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/local-isometric-embedding` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(M^n, g)$ be a Riemannian manifold with $g$ of class $C^\infty$, and let $p \in M$. Does there exist a neighborhood $U \ni p$ and a $C^\infty$ map $u : U \to \mathbb{R}^{s_n}$, $s_n = \tfrac{n(n+1)}{2}$, with $u^*(\delta) = g$, i.e. $\partial_i u \cdot \partial_j u = g_{ij}$?

The **principal open case is $n = 2$, $s_2 = 3$**: given a smooth Riemannian metric on a neighborhood of the origin in $\mathbb{R}^2$, does it admit a smooth local isometric embedding into $\mathbb{R}^3$? No counterexample is known in the $C^\infty$ category, and no general existence proof is known. The problem is open precisely when the Gauss curvature $K$ vanishes at $p$ in a degenerate way (e.g. to infinite order, or on a set with complicated structure).

A complete resolution requires either (a) a proof that every $C^\infty$ metric germ on a surface embeds isometrically and smoothly in $\mathbb{R}^3$ near each point, or (b) an explicit $C^\infty$ metric germ admitting no $C^2$ local isometric embedding. Regularity is essential: in low finite regularity the answer is already **no** (Pogorelov 1971; Nadirashvili–Yuan 2008), and in the real-analytic category the answer is **yes** in all dimensions (Cartan–Janet).

## 2. Mathematical Foundations

**Gauss–Codazzi system.** An immersion $u : U^2 \to \mathbb{R}^3$ with second fundamental form $h = (h_{ij})$ satisfies

$$\frac{\det h}{\det g} = K(g), \qquad \nabla_i h_{jk} - \nabla_j h_{ik} = 0,$$

where $\nabla$ is the Levi-Civita connection of $g$. Conversely (Bonnet), a symmetric $h$ solving this system on a simply connected $U$ determines an immersion unique up to rigid motion. Local embedding is therefore equivalent to local solvability of a determined nonlinear system of Monge–Ampère type.

**Darboux equation.** If the embedding is sought as a graph, one reduces to a single scalar equation for $z : U \to \mathbb{R}$:

$$\det\big(\nabla^2_g z\big) = K(g)\,\big(\det g\big)\,\big(1 - |\nabla z|_g^2\big), \qquad |\nabla z|_g < 1,$$

with $\nabla^2_g z = \partial_{ij} z - \Gamma^k_{ij}\partial_k z$. In the flat background $g = \delta$ this is $\det(\partial^2_{ij} z) = K(1+|\nabla z|^2)^2$.

**Type.** Linearizing $Q(z) = \det \nabla^2 z$ at $z_0$ gives the operator with cofactor coefficients

$$L v = \big(\mathrm{cof}\,\nabla^2 z_0\big)^{ij}\,\partial_{ij} v = z_{0,yy}v_{xx} - 2z_{0,xy}v_{xy} + z_{0,xx}v_{yy},$$

whose discriminant is $-\det \nabla^2 z_0 \sim -K$. Hence $L$ is **elliptic where $K>0$**, **hyperbolic where $K<0$**, and **degenerate / mixed type where $K$ vanishes**. The problem is thus the local solvability of a degenerate Monge–Ampère equation of mixed type.

**Janet dimension and freeness.** For general $n$, $s_n = n(n+1)/2$ is the number of equations, matching the number of unknown components; the system is determined and the symbol degenerates on the set where $\{\partial_i u\}$ fails to be *free* (i.e. $\{\partial_i u, \partial_{ij}u\}$ linearly independent). In $\mathbb{R}^{s_n + n}$ free maps are generic, the linearized operator is surjective with a tame right inverse, and Nash–Moser applies.

**Theorems relied on.** Cartan–Kähler (analytic case); Nash–Moser implicit function theorem; Hartman–Wintner theory for hyperbolic Darboux equations; Nirenberg's solution of the Weyl problem (elliptic case); Tricomi theory for mixed-type operators.

## 3. History & State of the Art (SOTA)

- **1873** — Schläfli conjectures that every $n$-metric embeds locally in $\mathbb{R}^{n(n+1)/2}$.
- **1926–27** — **Janet** and **Cartan** prove the analytic case: every real-analytic $(M^n,g)$ embeds locally and analytically in $\mathbb{R}^{s_n}$. Cartan's proof uses the Cartan–Kähler theorem; the argument is genuinely analytic and has no $C^\infty$ analogue (the involutive system is not symmetric-hyperbolic).
- **1956** — **Nash** proves global $C^\infty$ embeddings in high codimension; **Gromov** and Günther later reduce the local smooth dimension to $s_n + n$ (and global to $s_n + \max(2n, 5)$ for compact $M$). This makes the *codimension* question sharp only at $s_n$.
- **1971** — **Pogorelov** constructs a $C^{2,1}$ metric on a disk with no $C^2$ local isometric embedding in $\mathbb{R}^3$; curvature changes sign on a wildly oscillating set.
- **1985–87** — **C.-S. Lin** settles $K \ge 0$ and the first degenerate cases via Nash–Moser plus weighted a priori estimates for degenerate elliptic operators.
- **1987–2003** — **Hong–Zuily**, then **Han–Hong–Lin**, settle broad $K \le 0$ classes by degenerate hyperbolic energy estimates.
- **2003–2010** — **Han**, **Khuri**, **Han–Khuri** push into mixed-sign curvature with prescribed vanishing structure.
- **2008** — **Nadirashvili–Yuan** sharpen Pogorelov: a $C^{2,1}$ metric with $K$ changing sign that admits no $C^2$ local embedding, showing the obstruction is not an artifact of Pogorelov's construction.

SOTA: everything known reduces to hypotheses that force the degeneracy set of $K$ to be *finite order* and *geometrically simple* (a point, a curve, or a curve with clean crossing).

## 4. Partial Results / Verified Cases

**Surfaces in $\mathbb{R}^3$, smooth local embedding exists when:**

| Condition on $K$ at $p$ | Author, year |
|---|---|
| $K(p) > 0$ (elliptic Darboux) | classical; Weyl/Nirenberg-type elliptic theory |
| $K(p) < 0$ (hyperbolic Darboux) | classical; Darboux, Hartman–Wintner |
| $K \ge 0$ near $p$, $g \in C^\infty$ | C.-S. Lin, JDG **21** (1985) |
| $K(p) = 0$, $\nabla K(p) \ne 0$ (clean vanishing, sign change across a curve) | C.-S. Lin, CPAM **39** (1986) |
| $K \le 0$, $K$ vanishing to finite order | Hong–Zuily, Invent. Math. **89** (1987) |
| $K \le 0$, $\nabla K \ne 0$ on $\{K=0\}$ relaxed to finite-type degeneracies | Han–Hong–Lin, JDG **63** (2003) |
| $K$ changing sign stably across a curve; $K = x^{2k}h$, $h(p)\ne0$ | Q. Han, Calc. Var. PDE **25** (2006) |
| Further degeneracy classes, e.g. $K$ vanishing to order $m$ with prescribed transversality | M. Khuri, EJDE (2007); Han–Khuri, Comm. Anal. Geom. **18** (2010) |

**Higher dimensions.** Cartan–Janet gives all $n$ in the analytic category. For $n = 3$ into $\mathbb{R}^6$, **Bryant–Griffiths–Yang** (Duke Math. J. **50**, 1983) prove smooth local embedding when the curvature tensor, viewed as a quadratic form on $\Lambda^2$, is nondegenerate (and give a further condition for the degenerate case); **Poole** (Comm. PDE, 2010) handles $n=3$ with cleanly vanishing curvature. For $n \ge 4$ into $\mathbb{R}^{s_n}$ almost nothing is known in the $C^\infty$ category.

**Negative results.** Pogorelov (1971) and Nadirashvili–Yuan (2008): $C^{2,1}$ metrics with no $C^2$ local embedding. So the smooth problem is *not* a formal consequence of any $C^{2,1}$-stable argument.

## 5. Principal Obstacles

- **Type degeneracy is not removable.** At a zero of $K$ the linearized Monge–Ampère operator degenerates from elliptic to hyperbolic. Neither Schauder theory nor hyperbolic energy estimates survive; one needs mixed-type (Tricomi/Keldysh) theory, which is only developed for model degeneracies of finite, prescribed order.
- **Loss of derivatives.** Even where estimates exist, they lose derivatives, forcing Nash–Moser iteration. Nash–Moser requires a *tame* right inverse with uniform loss over a neighborhood of the approximate solution. Every known tameness proof consumes the finite-order hypothesis on $K$.
- **Infinite-order vanishing.** If $K$ vanishes to infinite order at $p$ (e.g. $K = e^{-1/x^2}\sin(1/x)$-type), no weight $x^\alpha$ calibrates the degeneracy; the a priori estimates have no exponent to work with, and unique continuation fails.
- **Wild zero sets.** Pogorelov's and Nadirashvili–Yuan's counterexamples exploit zero sets of $K$ that accumulate and oscillate. In $C^\infty$ such zero sets are still permitted (non-analytic), so any general proof must handle non-stratifiable $\{K=0\}$ — beyond current microlocal or characteristic-variety methods.
- **Analyticity is used essentially.** Cartan–Kähler needs convergent power series; the involutive prolongation of the Gauss–Codazzi system is not hyperbolic, so there is no smooth analogue.
- **Determined system, no slack.** In codimension $s_n$ there is no room to perturb the embedding: the $h$-principle machinery that gives Nash–Kuiper $C^1$ flexibility and Gromov's $\mathbb{R}^{s_n+n}$ result fails exactly at the critical dimension.

## 6. The Gap

Proved cases all assume $K$ has **finite-order, structurally simple vanishing** at $p$: $K \ne 0$; $K$ of one sign; $K = x^m h$ with $h \ne 0$ and $\{K = 0\}$ a smooth curve. The general statement allows an arbitrary smooth $K$, hence:

1. **Infinite-order vanishing** of $K$ at $p$ — no known estimate applies.
2. **Zero sets with infinitely many components accumulating at $p$**, or with cusps/non-transverse self-intersections.
3. **Sign changes of unbounded oscillation** — the regime in which $C^{2,1}$ counterexamples live.

The exact step required: an a priori estimate for the linearized Darboux operator $L v = (\mathrm{cof}\,\nabla^2 z)^{ij}\partial_{ij}v$ that is uniform and tame *without* any lower bound on the vanishing rate of $\det\nabla^2 z$. Equivalently, a mixed-type solvability theory whose loss of derivatives is controlled by $\|K\|_{C^k}$ alone rather than by a degeneracy exponent. Whether such an estimate exists is the crux; the $C^{2,1}$ counterexamples show any proof must exploit $C^\infty$ (or at least high-order) smoothness quantitatively.

## 7. Current Research (as of June 2026)

- **Degenerate Monge–Ampère school (Notre Dame / Stony Brook).** Q. Han and M. Khuri continue to extend the class of admissible vanishing patterns for $K$, combining weighted Nash–Moser schemes with microlocal parametrices for Tricomi-type operators.
- **Mixed-type PDE analysis.** Work extending Keldysh/Tricomi boundary-value theory to variable and higher-order degeneracies, motivated jointly by transonic flow and isometric embedding, remains the main technical engine. *(frontier — verify)*
- **Exterior differential systems.** Continued study of the characteristic variety of the Gauss–Codazzi system in dimensions $n \ge 3$, following Bryant–Griffiths–Yang, aims at a smooth analogue of Cartan–Kähler for hyperbolic-symbol prolongations. *(frontier — verify)*
- **Convex integration.** Post-Nash–Kuiper convex integration (De Lellis, Székelyhidi, Inauen, Cao) has settled $C^{1,\alpha}$ thresholds for isometric embedding; it is widely believed not to reach $C^2$, but its Hölder-threshold techniques inform where counterexamples might live. *(frontier — verify)*
- **Counterexample search.** Refinements of Nadirashvili–Yuan aiming to push the counterexample regularity above $C^{2,1}$ toward $C^{k}$; every increment of $k$ narrows the open gap. *(frontier — verify)*

## 8. Future Work

- Construct a $C^{k}$ (large $k$) or $C^\infty$ metric germ with no $C^2$ local embedding — most experts consider a counterexample at least as likely as a general theorem, given the $C^{2,1}$ obstructions.
- Develop solvability for $\det \nabla^2 z = f$ with $f \ge 0$ vanishing to infinite order on a closed set — the cleanest isolated sub-question, of independent interest in affine geometry.
- Settle $n = 3 \to \mathbb{R}^6$ without curvature nondegeneracy, completing the Bryant–Griffiths–Yang program.
- Determine the sharp regularity threshold $\alpha^*$ such that $C^{2,\alpha}$ metrics always embed and $C^{2,\alpha^-}$ do not, bracketing the smooth problem from below.
- Clarify whether local embeddability is $C^\infty$-generic: is the set of embeddable germs open and dense?

## 9. Key References

- **[Foundational]** M. Janet. *Sur la possibilité de plonger un espace riemannien donné dans un espace euclidien.* Ann. Soc. Polon. Math. **5** (1926), 38–43.
- **[Foundational]** É. Cartan. *Sur la possibilité de plonger un espace riemannien donné dans un espace euclidien.* Ann. Soc. Polon. Math. **6** (1927), 1–7.
- **[Foundational]** J. Nash. *The imbedding problem for Riemannian manifolds.* Annals of Mathematics **63** (1956), 20–63.
- **[Foundational]** A. V. Pogorelov. *An example of a two-dimensional Riemannian metric not admitting a local isometric imbedding in $E^3$.* Dokl. Akad. Nauk SSSR **198** (1971), 42–43.
- **[Key result]** C.-S. Lin. *The local isometric embedding in $\mathbb{R}^3$ of two-dimensional Riemannian manifolds with nonnegative curvature.* J. Differential Geometry **21** (1985), 213–230.
- **[Key result]** C.-S. Lin. *The local isometric embedding in $\mathbb{R}^3$ of 2-dimensional Riemannian manifolds with Gaussian curvature vanishing to finite order.* Comm. Pure Appl. Math. **39** (1986), 867–887.
- **[Key result]** J.-X. Hong, C. Zuily. *Existence of $C^\infty$ local solutions for the Monge–Ampère equation.* Inventiones Mathematicae **89** (1987), 645–661.
- **[Key result]** R. Bryant, P. Griffiths, D. Yang. *Characteristics and existence of isometric embeddings.* Duke Mathematical Journal **50** (1983), 893–994.
- **[SOTA / Recent]** Q. Han, J.-X. Hong, C.-S. Lin. *Local isometric embedding of surfaces with nonpositive Gaussian curvature.* J. Differential Geometry **63** (2003), 475–520.
- **[SOTA / Recent]** Q. Han. *Local isometric embedding of surfaces with Gauss curvature changing sign stably across a curve.* Calculus of Variations and PDE **25** (2006), 79–103.
- **[SOTA / Recent]** N. Nadirashvili, Y. Yuan. *Improving Pogorelov's isometric embedding counterexample.* Calculus of Variations and PDE **32** (2008), 319–323.
- **[SOTA / Recent]** M. Khuri. *Local solvability of degenerate Monge–Ampère equations and applications to geometry.* Electronic Journal of Differential Equations **2007**, No. 65.
- **[Survey]** Q. Han, J.-X. Hong. *Isometric Embedding of Riemannian Manifolds in Euclidean Spaces.* AMS Mathematical Surveys and Monographs **130**, 2006.
- **[Survey]** M. Gromov. *Partial Differential Relations.* Springer, Ergebnisse der Mathematik **9**, 1986.
- **[Survey]** E. G. Poznyak. *Isometric imbeddings of two-dimensional Riemannian metrics in Euclidean spaces.* Russian Mathematical Surveys **28** (1973), 47–77.

## 10. Worked Example / Concrete Special Case

**Clean vanishing produces the Tricomi operator.** Take $\Omega \subset \mathbb{R}^2$ a neighborhood of the origin and the explicit graph

$$z_0(x,y) = \frac{y^2}{2} + \frac{x^3}{6}, \qquad S_0 = \{(x,y,z_0(x,y))\} \subset \mathbb{R}^3.$$

*Step 1 — its curvature.* The Hessian is
$$\nabla^2 z_0 = \begin{pmatrix} x & 0 \\ 0 & 1\end{pmatrix}, \qquad \det \nabla^2 z_0 = x.$$
For a graph, $K = \dfrac{\det \nabla^2 z}{(1+|\nabla z|^2)^2}$, so the induced metric
$$g_0 = \Big(1+\tfrac{x^4}{4}\Big)dx^2 + x^2 y\, dx\,dy + (1+y^2)\,dy^2$$
has Gauss curvature
$$K_0(x,y) = \frac{x}{\big(1 + \tfrac{x^4}{4} + y^2\big)^2}.$$
Thus $K_0(0,y) = 0$ and $\partial_x K_0(0,y) = (1+y^2)^{-2} \ne 0$: curvature vanishes **cleanly** and changes sign across the line $x=0$. This is exactly the configuration covered by Lin (1986).

*Step 2 — linearize.* Perturb $z = z_0 + \varepsilon v$. Since $\det \nabla^2(z_0+\varepsilon v) = \det\nabla^2 z_0 + \varepsilon\, Lv + O(\varepsilon^2)$ with $L$ the cofactor operator of Section 2,
$$L v = z_{0,yy}\,v_{xx} - 2 z_{0,xy}\,v_{xy} + z_{0,xx}\,v_{yy} = v_{xx} + x\,v_{yy}.$$
This is the **Tricomi operator**: elliptic for $x>0$, hyperbolic for $x<0$, degenerate on $x=0$, with characteristics $y \pm \tfrac{2}{3}(-x)^{3/2} = \text{const}$ meeting $\{x=0\}$ tangentially with cusps.

*Step 3 — what the theorem delivers.* To embed a nearby metric $g = g_0 + \delta$ one solves $\det \nabla^2 z = K(g)(\det g)(1-|\nabla z|_g^2)$ by Nash–Moser, which needs a right inverse for $L$ with controlled loss. Tricomi theory supplies weighted estimates of the form
$$\|v\|_{H^{k}_{w}} \le C\big(\|Lv\|_{H^{k+m}_{w}}\big), \qquad w = |x|^{\alpha},$$
where the exponent $\alpha$ and the loss $m$ are dictated by the vanishing order $1$ of $\det\nabla^2 z_0 = x$. Iterating gives a smooth local embedding.

*Step 4 — where it breaks.* Replace $x$ by $\phi(x) = e^{-1/x^2}\sin(1/x)$ for $x \ne 0$, $\phi(0)=0$ — a $C^\infty$ function vanishing to infinite order with zeros accumulating at $0$. Then $L v = v_{xx} + \phi(x)v_{yy}$ switches type infinitely often in every neighborhood of the origin, and no weight $|x|^\alpha$ calibrates the degeneracy: the constant $C$ above blows up for every $\alpha$ and every $m$. No existence theorem covers this $K$, and no counterexample rules it out. This single germ is a faithful miniature of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*