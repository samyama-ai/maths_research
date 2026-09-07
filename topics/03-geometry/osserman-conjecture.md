---
id: 03-geometry/osserman-conjecture
title: "Osserman Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Osserman Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/osserman-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(M^n, g)$ be a connected Riemannian manifold with curvature tensor $R$. For a unit tangent vector $X \in T_pM$ the **Jacobi operator** is the symmetric endomorphism
$$R_X : X^{\perp} \to X^{\perp}, \qquad R_X Y = R(Y, X)X .$$

$(M,g)$ is **pointwise Osserman** if for every $p \in M$ the eigenvalues of $R_X$ (with multiplicity) are the same for all unit $X \in T_pM$; it is **globally Osserman** if those eigenvalues are additionally independent of $p$.

**Conjecture (Osserman, 1990).** A pointwise Osserman Riemannian manifold is either flat or locally isometric to a rank-one symmetric space, i.e. locally two-point homogeneous.

The rank-one symmetric spaces are $\mathbb{R}^n$, $S^n$, $\mathbb{RP}^n$, $\mathbb{CP}^m$, $\mathbb{HP}^m$, $\mathbb{OP}^2$ and their noncompact duals $\mathbb{RH}^n$, $\mathbb{CH}^m$, $\mathbb{HH}^m$, $\mathbb{OH}^2$, each with a scaling of the canonical metric. The converse is elementary: their isotropy groups act transitively on unit spheres, so the eigenvalues of $R_X$ cannot depend on $X$. A complete solution therefore requires proving the forward implication in every dimension $n$, or exhibiting a single Osserman metric not locally isometric to one of these.

**Status.** The conjecture is a theorem in all dimensions $n \neq 16$ (Chi 1988; Nikolayevsky 2004, 2005), and in dimension 16 under a multiplicity hypothesis. A full dimension-16 resolution has been announced recently; see §7 for the verification caveat.

## 2. Mathematical Foundations

**Algebraic curvature tensors.** Work at a point with $V = T_pM \cong \mathbb{R}^n$ and inner product $\langle\cdot,\cdot\rangle$. An algebraic curvature tensor $R \in \otimes^4 V^*$ satisfies
$$R(X,Y,Z,W) = -R(Y,X,Z,W) = R(Z,W,X,Y), \qquad R(X,Y,Z,W)+R(Y,Z,X,W)+R(Z,X,Y,W)=0 .$$
$R$ is **Osserman** if $\operatorname{Spec}(R_X)$ is constant on the unit sphere $S(V)$. Since the trace $\operatorname{tr} R_X = \operatorname{Ric}(X,X)$, every Osserman tensor is Einstein; the second symmetric function of the eigenvalues forces $\|R\|^2$-type identities that make the Osserman condition a system of polynomial equations on $R$.

**Clifford structures.** A **Clifford structure** $\mathrm{Cl}(m)$ on $V$ is a family $J_1,\dots,J_m$ of skew-symmetric orthogonal endomorphisms with
$$J_i^2 = -\mathrm{id}, \qquad J_iJ_j + J_jJ_i = 0 \ (i \neq j),$$
equivalently a representation of the Clifford algebra $\mathrm{Cl}_m$ on $V$; it exists on $\mathbb{R}^n$ iff $n$ is a multiple of the Radon–Hurwitz number $\rho(m)$. Given such a family and $\lambda_0, \lambda_1,\dots,\lambda_m \in \mathbb{R}$, the **Clifford-type tensor** is
$$R = \lambda_0 R_1 + \sum_{i=1}^{m} \lambda_i R_{J_i},$$
where $R_1(X,Y)Z = \langle Y,Z\rangle X - \langle X,Z\rangle Y$ and
$$R_{J}(X,Y)Z = \langle JY,Z\rangle JX - \langle JX,Z\rangle JY - 2\langle JX,Y\rangle JZ .$$
Its Jacobi operator is $R_X = \lambda_0(\mathrm{id} - X\otimes X^\flat) + 3\sum_i \lambda_i\, (J_iX)\otimes (J_iX)^\flat$, whose spectrum on $X^\perp$ is $\{\lambda_0 + 3\lambda_i\}$ (multiplicity $1$ each, since the $J_iX$ are orthonormal) together with $\lambda_0$ of multiplicity $n-1-m$ — independent of $X$. So Clifford-type tensors are Osserman.

**Two structural theorems.**
- (Nikolayevsky) For $n \neq 16$, every Osserman algebraic curvature tensor on $\mathbb{R}^n$ is of Clifford type.
- The curvature tensor of $\mathbb{OP}^2$ (and $\mathbb{OH}^2$), $n=16$, is Osserman but **not** of Clifford type: its Jacobi operator has eigenvalues $4c$ with multiplicity $7$ and $c$ with multiplicity $8$, and the eigen-$7$-plane distribution $X \mapsto \ker(R_X - 4c)$ is not spanned by a global anticommuting family.

**Topological constraint.** A Clifford structure $\mathrm{Cl}(m)$ on $\mathbb{R}^n$ gives $m$ pointwise-orthonormal vector fields $X \mapsto J_iX$ on $S^{n-1}$, so $m \le \rho(n)-1$ by Adams' theorem on vector fields on spheres — the bridge from algebra to topology used throughout the proofs.

## 3. History & State of the Art (SOTA)

- **1990.** Robert Osserman poses the question in the expository article *Curvature in the eighties* (Amer. Math. Monthly), after observing that constancy of $\operatorname{Spec}(R_X)$ is exactly what one gets for free from two-point homogeneity.
- **1988.** Quo-Shin Chi (published slightly before Osserman's article, answering the same question) proves the conjecture for globally Osserman manifolds of dimension $n = 4$, $n$ odd, and $n \equiv 2 \bmod 4$, combining the Einstein condition with Chern–Weil / Bochner arguments and, in dimension 4, the identification pointwise Osserman $\iff$ self-dual (or anti-self-dual) Einstein.
- **1991.** Chi treats quaternionic-Kähler cases and dimension 8 under extra curvature hypotheses.
- **1995.** Gilkey, Swann and Vanhecke settle cases where an eigenvalue of $R_X$ has multiplicity $1$ or $n-1$, and relate the problem to isoparametric geodesic spheres; Gilkey's Clifford-module constructions supply the full family of Osserman algebraic curvature tensors.
- **2004–2005.** Yuri Nikolayevsky proves the pointwise conjecture in dimension 8, then in all dimensions $n \neq 8, 16$, by classifying Osserman algebraic curvature tensors as Clifford type and then integrating (a Clifford structure with $m \ge 1$ forces a Kähler, quaternionic-Kähler, or Cayley structure and then local symmetry).
- **2006 onwards.** Nikolayevsky reduces dimension 16 to a narrow window of eigenvalue multiplicities; the residual case is the $\mathbb{OP}^2$-like configuration.
- **Semi-Riemannian contrast.** In Lorentzian signature Osserman $\Rightarrow$ constant curvature (Blažić–Bokan–Gilkey; García-Río–Kupeli–Vázquez-Abal). In signature $(p,q)$ with $p,q \ge 2$ the analogue is **false**: there are Osserman metrics, e.g. nilpotent-Jacobi-operator examples, that are not even locally homogeneous.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n = 2, 3$ | Osserman $\Rightarrow$ constant sectional curvature (curvature determined by Ricci) | classical |
| $n = 4$ | Pointwise Osserman $\iff$ Einstein and (anti-)self-dual $\Rightarrow$ two-point homogeneous | Chi 1988 |
| $n$ odd | Conjecture holds | Chi 1988 |
| $n \equiv 2 \bmod 4$ | Conjecture holds | Chi 1988 |
| $R_X$ has an eigenvalue of multiplicity $1$ or $n-1$ | Conjecture holds | Gilkey–Swann–Vanhecke 1995 |
| $n = 8$ | Conjecture holds (pointwise) | Nikolayevsky 2004 |
| $n \neq 8, 16$ | Conjecture holds (pointwise); every Osserman algebraic curvature tensor is Clifford | Nikolayevsky 2005 |
| $n = 16$, some eigenvalue of $R_X$ of multiplicity $\ge 9$ | Conjecture holds | Nikolayevsky 2006 |
| $n = 16$, multiplicities $(7,8)$ / $(8,7)$ | Residual case; announced resolution, see §7 | — |
| Lorentzian, any $n$ | Osserman $\Rightarrow$ constant curvature | Blažić–Bokan–Gilkey 1997 |
| Signature $(p,q)$, $p,q \ge 2$ | Analogue **false** | García-Río–Kupeli–Vázquez-Lorenzo 2002 |

## 5. Principal Obstacles

- **The octonionic exception is not algebraic-only.** Every proof route in $n \neq 16$ ends by showing the Osserman tensor is Clifford type, which supplies globally defined anticommuting complex structures and hence a holonomy reduction. In $n = 16$ the model $\mathbb{OP}^2$ curvature tensor is Osserman and not Clifford, so the classification statement itself is false and the whole mechanism is unavailable.
- **Multiplicity $(7,8)$ sits exactly at the Adams bound.** For $n=16$, $\rho(16)-1 = 8$, so the topological obstruction that kills large Clifford families elsewhere gives nothing here: $8$ anticommuting structures on $\mathbb{R}^{16}$ do exist. The counting arguments that eliminate multiplicity patterns in other dimensions are vacuous at exactly this pattern.
- **Nonlinearity of the Osserman system.** Constancy of $\operatorname{Spec}(R_X)$ is a system of high-degree polynomial identities on the $\binom{n+1}{2}\!\cdot\!$-dimensional space of curvature tensors; no Gröbner-basis or representation-theoretic decomposition of $\otimes^4(\mathbb{R}^{16})^*$ under $O(16)$ is computationally tractable at this size.
- **Only pointwise data.** Osserman is a condition at each point on the curvature tensor alone; there is no a priori second-order information (no $\nabla R$ constraint) to feed a Cartan-style prolongation, so passing from the algebraic classification to local symmetry requires a separate integration step each time.
- **Failure of signature-blind methods.** Because the pseudo-Riemannian analogue is false, any proof must use positive-definiteness essentially — ruling out purely tensorial identities and forcing genuine spectral/topological input.

## 6. The Gap

Proven: for all $n \neq 16$, the Osserman condition forces a Clifford structure, which forces local two-point homogeneity. In $n = 16$, the same conclusion is proven whenever $R_X$ has an eigenvalue of multiplicity $\ge 9$.

The gap is the single configuration: $n = 16$, $R_X$ with exactly two eigenvalues of multiplicities $7$ and $8$ — the spectral signature of the Cayley plane. One must show that the resulting rank-$7$ eigendistribution $X \mapsto E_{4c}(X) \subset X^\perp$ on the unit sphere $S^{15}$, together with the curvature identities it satisfies, can only be realized by the $\mathbb{OP}^2$/$\mathbb{OH}^2$ curvature tensor, and then that the pointwise Cayley structure integrates to a locally symmetric metric. Both halves — algebraic rigidity of the octonionic model, and integration — must be done without the Clifford crutch.

## 7. Current Research (as of June 2026)

- **Dimension 16 endgame.** Nikolayevsky (La Trobe) and collaborators, notably JeongHyeong Park (Sungkyunkwan), have pursued the residual $(7,8)$ case using the $\mathrm{Spin}(9)$ representation on $\mathbb{R}^{16}$ and Cartan's isoparametric-hypersurface machinery. A proof of the remaining case, completing the conjecture in all dimensions, has been announced in preprint form. *(frontier — verify: confirm the published venue and referee status before citing this as settled.)*
- **$\mathrm{Spin}(9)$ geometry.** Parton, Piccinni and coauthors have developed the differential geometry of $\mathrm{Spin}(9)$-structures on 16-manifolds (canonical 8-form, Clifford systems), the natural language for the octonionic case.
- **Semi-Riemannian and Jacobi–Osserman variants.** Groups at Santiago de Compostela (García-Río, Vázquez-Lorenzo) study Osserman, Ivanov–Petrova, and Szabó-type conditions in indefinite signature, where classification is genuinely open beyond low signature.
- **Affine and Finsler analogues.** Osserman conditions for affine connections without a metric, and for the flag curvature of Finsler metrics, are active and largely unsettled.

## 8. Future Work

- Complete independent verification of the announced dimension-16 argument, and extract from it a uniform proof valid in all dimensions rather than a case split at $16$.
- Classify Osserman algebraic curvature tensors in $n=16$ intrinsically: prove that the only non-Clifford ones are $\mathbb{OP}^2$-type, which would give the geometric statement immediately.
- Settle the **Osserman conjecture for higher-order Jacobi operators** (Stanilov–Videv operators, $k$-plane curvature operators), where classification is open for most $k$.
- Determine which neutral-signature Osserman manifolds with diagonalizable Jacobi operator are locally homogeneous — the natural boundary of the Riemannian theorem.
- Extend to the **Osserman condition on the conformal Weyl tensor** ("conformally Osserman" manifolds), where Nikolayevsky proved classification for $n \neq 16$ and the same residual case persists.

## 9. Key References

- **[Foundational]** R. Osserman. *Curvature in the eighties.* American Mathematical Monthly **97** (1990), 731–756.
- **[Foundational]** Q.-S. Chi. *A curvature characterization of certain locally rank-one symmetric spaces.* Journal of Differential Geometry **28** (1988), 187–202.
- **[Foundational]** Q.-S. Chi. *Quaternionic Kähler manifolds and a curvature characterization of two-point homogeneous spaces.* Illinois Journal of Mathematics **35** (1991), 408–418.
- **[Structural]** P. Gilkey, A. Swann, L. Vanhecke. *Isoparametric geodesic spheres and a conjecture of Osserman concerning the Jacobi operator.* Quarterly Journal of Mathematics Oxford (2) **46** (1995), 299–320.
- **[SOTA]** Y. Nikolayevsky. *Osserman manifolds of dimension 8.* Manuscripta Mathematica **115** (2004), 31–53.
- **[SOTA]** Y. Nikolayevsky. *Osserman conjecture in dimension $n \neq 8, 16$.* Mathematische Annalen **331** (2005), 505–522.
- **[SOTA]** Y. Nikolayevsky. *On Osserman manifolds of dimension 16.* In *Contemporary Geometry and Related Topics*, University of Belgrade, 2006, 379–398.
- **[Survey / Book]** P. Gilkey. *Geometric Properties of Natural Operators Defined by the Riemann Curvature Tensor.* World Scientific, 2001.
- **[Survey / Book]** E. García-Río, D. N. Kupeli, R. Vázquez-Lorenzo. *Osserman Manifolds in Semi-Riemannian Geometry.* Lecture Notes in Mathematics **1777**, Springer, 2002.
- **[Related]** N. Blažić, N. Bokan, P. Gilkey. *A note on Osserman Lorentzian manifolds.* Bulletin of the London Mathematical Society **29** (1997), 227–230.
- **[Tool]** J. F. Adams. *Vector fields on spheres.* Annals of Mathematics **75** (1962), 603–632.

## 10. Worked Example / Concrete Special Case

**Claim.** A complex space form $(M^{2m}, g, J)$ of constant holomorphic sectional curvature $4c$ is globally Osserman, with Clifford data $m=1$, $\lambda_0=c$, $\lambda_1=c$.

Its curvature tensor is
$$R(X,Y)Z = c\big(\langle Y,Z\rangle X - \langle X,Z\rangle Y + \langle JY,Z\rangle JX - \langle JX,Z\rangle JY - 2\langle JX,Y\rangle JZ\big).$$

Fix a unit $X$ and compute $R_XY = R(Y,X)X$ by substituting $(X,Y,Z) \mapsto (Y,X,X)$:
$$R_XY = c\big(\langle X,X\rangle Y - \langle Y,X\rangle X + \langle JX,X\rangle JY - \langle JY,X\rangle JX - 2\langle JY,X\rangle JX\big).$$
Since $J$ is skew, $\langle JX,X\rangle = 0$, so for $Y \perp X$:
$$R_XY = c\big(Y - 3\langle JY,X\rangle JX\big).$$

- Take $Y = JX$ (a unit vector orthogonal to $X$). Then $\langle J(JX), X\rangle = \langle -X,X\rangle = -1$, giving
 $$R_X(JX) = c\,(JX + 3JX) = 4c\,JX .$$
 Eigenvalue $4c$, multiplicity $1$.
- Take $Y \perp X, JX$. Then $\langle JY, X\rangle = -\langle Y, JX\rangle = 0$, so $R_XY = cY$. Eigenvalue $c$, multiplicity $2m-2$.

So $\operatorname{Spec}(R_X) = \{4c^{(1)},\, c^{(2m-2)}\}$ for **every** unit $X$: the manifold is Osserman, matching the general Clifford formula $\{\lambda_0 + 3\lambda_1, \lambda_0\} = \{4c, c\}$ with $J_1 = J$.

**Why this is the whole conjecture in miniature.** Here the eigen-line $\mathbb{R}\,JX = \ker(R_X - 4c)$ is spanned by a single globally defined complex structure $J$, which forces the holonomy into $U(m)$ and, with $\nabla J = 0$, local symmetry: $M$ is locally $\mathbb{CP}^m$, $\mathbb{CH}^m$, or flat. Nikolayevsky's theorem says that in every dimension $n \neq 16$ this pattern is forced — the eigendistributions of $R_X$ always come from an anticommuting family $J_1,\dots,J_m$. In dimension $16$ with multiplicities $(7,8)$ the analogous eigen-$7$-plane $\ker(R_X - 4c)$ of the $\mathbb{OP}^2$ curvature tensor cannot be written as $\operatorname{span}\{J_1X,\dots,J_7X\}$ for anticommuting $J_i$, and the argument above has no substitute.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*