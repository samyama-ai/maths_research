---
id: 05-analysis/complex-plateau-problem
title: "The Complex Plateau Problem for Strictly Pseudoconvex Boundaries"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Complex Plateau Problem for Strictly Pseudoconvex Boundaries

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/complex-plateau-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The classical Plateau problem asks which curves bound minimal surfaces. Its complex analogue asks which odd-dimensional real submanifolds of $\mathbb{C}^N$ bound complex-analytic ones.

**Existence (settled).** Let $X \subset \mathbb{C}^N$ be a compact, connected, oriented, smooth real submanifold of dimension $2n-1$, $n \ge 2$. Harvey–Lawson: $X$ bounds a complex variety $V$ of dimension $n$ in $\mathbb{C}^N \setminus X$ with $\overline{V} = V \cup X$ if and only if $X$ is *maximally complex*.

**Regularity (open).** Suppose in addition that $X$ is *strictly pseudoconvex* as a CR manifold. The variety $V$ produced above is in general singular, with finitely many isolated normal singularities. The problem is:

> Give an intrinsic CR-invariant necessary and sufficient condition on $X$ under which $V$ is smooth — i.e. $X$ is the boundary of a complex **manifold** with boundary, embedded in $\mathbb{C}^N$.

This is **Yau's complex Plateau problem**. A complete solution must produce an invariant computable from the CR structure $(X, T^{1,0}X)$ alone — not from $V$ — whose vanishing is equivalent to smoothness of $V$. The case $\dim_{\mathbb{R}} X = 3$ ($n=2$) is the principal open case; the answer is known for $\dim_{\mathbb{R}} X \ge 5$ ($n \ge 3$) and, in dimension 5, in sharpened form.

## 2. Mathematical Foundations

**CR structure.** For $X^{2n-1} \subset \mathbb{C}^N$ real, set
$$T^{1,0}X \;=\; \mathbb{C}TX \cap T^{1,0}\mathbb{C}^N ,$$
the induced Cauchy–Riemann bundle. $X$ is a *CR manifold of hypersurface type* if $\dim_{\mathbb{C}} T^{1,0}_p X = n-1$ for all $p$, and *maximally complex* if this holds with $2n-1 = \dim_{\mathbb{R}} X$, i.e. the maximal possible complex tangent dimension. Equivalently, $[T^{1,0}X, T^{1,0}X] \subset T^{1,0}X$ (integrability) plus maximality.

**Levi form.** Choose a real $1$-form $\eta$ annihilating $T^{1,0}X \oplus T^{0,1}X$. The Levi form is the Hermitian form
$$L_\eta(Z, \overline{W}) \;=\; -\,i\, d\eta (Z, \overline{W}), \qquad Z, W \in T^{1,0}X .$$
$X$ is **strictly pseudoconvex** if $L_\eta$ is positive definite for a suitable choice of $\eta$. For $X = \partial\Omega$ with defining function $\rho$, this is positivity of the complex Hessian $\big(\partial^2 \rho / \partial z_j \partial \bar z_k\big)$ restricted to $T^{1,0}X$.

**Maximal complexity in current form.** $X$ (oriented, compact) is maximally complex iff, as a current of integration $[X]$, one has $[X]^{0,q} = 0$ for $q \ne 0, 1$ in the relevant bidegree splitting; equivalently
$$\int_X \varphi = 0 \quad \text{for every smooth } (p,q)\text{-form } \varphi \text{ on } \mathbb{C}^N \text{ with } p+q = 2n-1,\ q \ge n+1 .$$
For $n = 1$ (real curves) maximal complexity is vacuous and is replaced by the **moment condition** $\int_X \omega = 0$ for all holomorphic $(1,0)$-forms $\omega$.

**Kohn–Rossi cohomology.** Let $\overline{\partial}_b$ be the tangential Cauchy–Riemann operator on $(p,q)$-forms on $X$. The Kohn–Rossi groups are
$$H^{p,q}_{KR}(X) \;=\; \frac{\ker \overline{\partial}_b \colon \mathcal{E}^{p,q}(X) \to \mathcal{E}^{p,q+1}(X)}{\operatorname{im} \overline{\partial}_b \colon \mathcal{E}^{p,q-1}(X) \to \mathcal{E}^{p,q}(X)} .$$
These are CR invariants. Kohn's subelliptic $\tfrac12$-estimate for $\square_b = \overline{\partial}_b\overline{\partial}_b^* + \overline{\partial}_b^*\overline{\partial}_b$ holds under **condition $Y(q)$**: the Levi form has at least $\max(n-q, q+1)$ eigenvalues of one sign. For strictly pseudoconvex $X^{2n-1}$, $Y(q)$ holds exactly for $1 \le q \le n-2$; it fails for $q=0$ and $q=n-1$. When $n=2$ no $q$ satisfies $Y(q)$ — the source of every difficulty in dimension 3.

**Singularity invariants.** If $(V,0)$ is a normal isolated surface singularity with resolution $\pi: \tilde V \to V$, its **geometric genus** is $p_g = \dim_{\mathbb{C}} H^1(\tilde V, \mathcal{O}_{\tilde V})$; $(V,0)$ is *rational* iff $p_g = 0$. The Du–Yau **$s$-invariants** measure holomorphic forms:
$$s^{(q)}_{ij}(V) \;=\; \dim_{\mathbb{C}} \frac{\Gamma(V\setminus\{0\}, \Omega^i)}{\text{forms extending across the resolution}} \quad(\text{indexed as in Du–Yau}),$$
finer than $p_g$ because they do not vanish for rational singularities.

## 3. History & State of the Art (SOTA)

- **1965.** Kohn–Rossi prove holomorphic extension from the boundary of a complex manifold, introducing $H^{p,q}_{KR}$. Rossi constructs 3-dimensional strictly pseudoconvex CR manifolds that are *not* embeddable in any $\mathbb{C}^N$.
- **1974–75.** Boutet de Monvel: every compact strictly pseudoconvex CR manifold of dimension $\ge 5$ embeds in $\mathbb{C}^N$. Dimension 3 is excluded — $\overline{\partial}_b$ has non-closed range there.
- **1975, 1977.** Harvey–Lawson solve existence (Parts I and II), including the $n=1$ moment-condition case.
- **1981.** Yau, Part I: for $n \ge 3$, $X$ bounds a complex manifold iff $H^{p,q}_{KR}(X) = 0$ for $1 \le q \le n-2$. This *is* the resolution of the regularity question in dimension $\ge 5$, but the criterion degenerates to an empty condition at $n=2$.
- **1988.** Burns–Epstein define a global $\mathbb{R}$-valued biholomorphic invariant $\mu(X)$ of CR 3-manifolds bounding complex surfaces, computing it via Chern–Moser data.
- **1997–2000.** Dolbeault–Henkin treat boundaries of holomorphic chains in $\mathbb{CP}^n$; Epstein–Henkin establish stability of embeddings for pseudoconcave surfaces.
- **1998.** Luk–Yau exhibit a strictly pseudoconvex $X$ whose Harvey–Lawson variety is singular arbitrarily near the boundary in a controlled sense — an addendum showing boundary regularity claims need care.
- **2007.** Yau, Part II: the first intrinsic criterion in dimension 3, via a CR invariant $\mathfrak{g}(X)$ built from $H^{1}_{KR}$-type data, under a restricted class of singularities.
- **2012.** Du–Yau, Part III: an $s$-invariant criterion resolving the dimension-5 case in the sharp form, and giving new leverage on rational singularities in dimension 3.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| Existence, $\dim X = 2n-1 \ge 3$ | Solved (Harvey–Lawson 1975): maximal complexity |
| Existence, $\dim X = 1$ in $\mathbb{C}^N$ | Solved (Harvey–Lawson 1977): moment condition |
| Regularity, $\dim X \ge 5$ ($n \ge 3$) | Solved (Yau 1981): $H^{p,q}_{KR}(X)=0$, $1 \le q \le n-2$ |
| Regularity, $\dim X = 5$, sharp $s$-invariant form | Solved (Du–Yau 2012) |
| Regularity, $\dim X = 3$, $V$ with quasi-homogeneous singularities | Solved (Yau 2007): criterion $\mathfrak{g}(X) = 0$ |
| Regularity, $\dim X = 3$, $V$ with rational singularities | Partial: $p_g$ fails; $s$-invariants give criteria in subclasses |
| Regularity, $\dim X = 3$, general | **Open** |

Additional settled families: $X = \partial\Omega$ for $\Omega$ strictly convex (bounds the smooth $\Omega$); links of smooth points; $X$ CR-diffeomorphic to the standard $S^{2n-1}$ (rigidity forces the ball, by Chern–Moser flatness plus normality); boundaries of Stein domains with vanishing $H^1(\mathcal{O})$.

## 5. Principal Obstacles

- **Failure of subellipticity at $n = 2$.** Condition $Y(q)$ holds only for $1 \le q \le n-2$, an empty range when $n = 2$. So $\square_b$ has no $\tfrac12$-estimate in any degree, $\overline{\partial}_b$ can have non-closed range, and Kohn–Rossi groups are infinite-dimensional or non-Hausdorff. Yau's Part I criterion is vacuously true for every CR 3-manifold and therefore says nothing.
- **Non-embeddability.** Rossi's examples show abstract strictly pseudoconvex CR 3-manifolds need not embed at all, so no purely local-analytic argument can construct $V$; embeddability must be hypothesized, and it is unstable under deformation (Burns, Bland–Duchamp, Epstein–Henkin).
- **Rational singularities are invisible to $p_g$.** The natural first candidate invariant, geometric genus, vanishes for the entire class of rational singularities — which includes genuinely singular Harvey–Lawson varieties such as the $ADE$ links. Any working criterion must be strictly finer than $p_g$.
- **Intrinsic vs. extrinsic.** The $s$-invariants and $p_g$ are defined on $V$ or its resolution. Turning them into invariants of $X$ requires a Kohn–Rossi realization theorem, which is available only where $\overline{\partial}_b$ analysis works.
- **Perturbation and Fourier methods fail.** The CR structure is a genuinely non-elliptic, non-hypoelliptic system in dimension 3; Hörmander-type hypoellipticity gives no gain, and the Szegő projector's microlocal structure degenerates precisely on the characteristic variety.

## 6. The Gap

Proven: for $n \ge 3$ there is a complete intrinsic answer. For $n=2$ there is an intrinsic answer *conditional on the analytic type of the singularities* of the (a priori unknown) variety $V$ — quasi-homogeneous in Yau 2007, certain rational classes thereafter.

The exact missing step: **define a single CR invariant of an arbitrary compact strictly pseudoconvex embeddable CR 3-manifold $X$ that vanishes iff every singularity of the Harvey–Lawson variety $V$ is smooth, without assuming anything about the analytic type of those singularities.** Concretely, one needs a Kohn–Rossi-side expression for the full collection of $s$-invariants $\{s_{ij}(V,p)\}$ — or a proof that some finite subcollection suffices — in a setting where $\overline{\partial}_b$ has no closed range. Equivalently: bridge the classification of normal surface singularities (Artin, Laufer) with $\overline{\partial}_b$-analysis on the link.

## 7. Current Research (as of June 2026)

- **Du–Yau school (Shanghai / Tsinghua).** Continued extension of the $s$-invariant program to higher-dimensional isolated singularities and to non-quasi-homogeneous surface singularities. *(frontier — verify)* Preprints extending the Part III criterion to links of weighted-homogeneous complete intersections of embedding dimension $\ge 4$.
- **Microlocal / Szegő-kernel approach.** Hsiao, Marinescu and collaborators develop semiclassical expansions of the Szegő projector on CR manifolds with $S^1$-actions, giving embedding and Kodaira-type theorems that bypass closed-range failure. Applying this machinery to detect singularity invariants of $V$ from the kernel asymptotics is an active line. *(frontier — verify)*
- **Deformation theory of CR structures.** Bland–Duchamp normal forms and the Burns–Epstein invariant are used to study which deformations of $S^3$ remain fillable by a smooth manifold; the moduli of fillable structures is a persistent target.
- **Positive-mass and Yamabe-type methods.** The CR Yamabe invariant and CR positive-mass theorem (Cheng–Malchiodi–Yang) give scalar geometric obstructions to filling, which some groups aim to couple with the analytic criteria.
- **Complex Plateau in projective and Levi-flat settings.** Dolbeault–Henkin-type boundary problems in $\mathbb{CP}^n$ and for $q$-concave boundaries continue at Paris and Moscow-descended groups.

## 8. Future Work

- Prove a **closed-range substitute** in dimension 3: identify a canonical Hausdorff quotient of $H^{0,1}_{KR}(X)$ (e.g. via the Szegő projector's range) that is finite-dimensional for embeddable $X$ and computes $p_g$ plus corrections.
- Establish that **finitely many $s$-invariants suffice**: bound the number of $s_{ij}$ needed as a function of the multiplicity or embedding dimension of $(V,p)$.
- Handle the **rational singularity case in full**, since it is exactly where $p_g$ is blind and where the $ADE$ examples live.
- Give **effective/computational tests**: for $X$ presented as a real-algebraic set, decide smoothness of $V$ by elimination or by numerical Szegő-kernel computation.
- Extend to **non-isolated** singularities and to boundaries of higher codimension, where even the Harvey–Lawson structure theory is incomplete.

## 9. Key References

- **[Foundational]** R. Harvey, H. B. Lawson, Jr. *On boundaries of complex analytic varieties, I.* Annals of Mathematics (2) **102** (1975), 223–290.
- **[Foundational]** R. Harvey, H. B. Lawson, Jr. *On boundaries of complex analytic varieties, II.* Annals of Mathematics (2) **106** (1977), 213–238.
- **[Foundational]** J. J. Kohn, H. Rossi. *On the extension of holomorphic functions from the boundary of a complex manifold.* Annals of Mathematics **81** (1965), 451–472.
- **[Foundational]** H. Rossi. *Attaching analytic spaces to an analytic space along a pseudoconcave boundary.* In *Proceedings of the Conference on Complex Analysis (Minneapolis, 1964)*, Springer, 1965.
- **[Foundational]** L. Boutet de Monvel. *Intégration des équations de Cauchy–Riemann induites formelles.* Séminaire Goulaouic–Lions–Schwartz, École Polytechnique, 1974–1975.
- **[SOTA]** S. S.-T. Yau. *Kohn–Rossi cohomology and its application to the complex Plateau problem, I.* Annals of Mathematics (2) **113** (1981), 67–110.
- **[SOTA]** S. S.-T. Yau. *Kohn–Rossi cohomology and its application to the complex Plateau problem, II.* Journal of Differential Geometry **75** (2007), 133–170.
- **[SOTA]** R. Du, S. S.-T. Yau. *Kohn–Rossi cohomology and its application to the complex Plateau problem, III.* Journal of Differential Geometry **90** (2012), 251–266.
- **[SOTA]** H.-S. Luk, S. S.-T. Yau. *Counterexample to boundary regularity of a strongly pseudoconvex CR submanifold: an addendum to the paper of Harvey–Lawson.* Annals of Mathematics (2) **148** (1998), 1153–1154.
- **[Related]** D. Burns, C. L. Epstein. *A global invariant for three-dimensional CR-manifolds.* Inventiones Mathematicae **92** (1988), 333–348.
- **[Related]** C. L. Epstein, G. M. Henkin. *Stability of embeddings for pseudoconcave surfaces and their boundaries.* Acta Mathematica **185** (2000), 161–237.
- **[Related]** P. Dolbeault, G. Henkin. *Chaînes holomorphes de bord donné dans $\mathbb{CP}^n$.* Bulletin de la Société Mathématique de France **125** (1997), 383–445.
- **[Related]** H. Laufer. *On minimally elliptic singularities.* American Journal of Mathematics **99** (1977), 1257–1295.
- **[Survey/Book]** A. Boggess. *CR Manifolds and the Tangential Cauchy–Riemann Complex.* CRC Press, 1991.
- **[Survey/Book]** E. M. Chirka. *Complex Analytic Sets.* Kluwer, 1989.

## 10. Worked Example / Concrete Special Case

Take Brieskorn links. For integers $a_1, a_2, a_3 \ge 2$ let
$$V_{\mathbf a} = \{ z \in \mathbb{C}^3 : z_1^{a_1} + z_2^{a_2} + z_3^{a_3} = 0 \}, \qquad X_{\mathbf a} = V_{\mathbf a} \cap S^5 .$$
$X_{\mathbf a}$ is a compact, connected, strictly pseudoconvex CR 3-manifold embedded in $\mathbb{C}^3$, and it is maximally complex, so Harvey–Lawson applies. By uniqueness of the bounding variety, the only $V$ with $\partial V = X_{\mathbf a}$ is $V_{\mathbf a} \cap \overline{B^6}$, which is singular at $0$. So the answer to "does $X_{\mathbf a}$ bound a complex manifold?" is **no** for every $\mathbf a$ — a good test bed for candidate invariants.

$V_{\mathbf a}$ is quasi-homogeneous with weights $w_i = 1/a_i$. For such a hypersurface singularity the geometric genus is a lattice count:
$$p_g \;=\; \\#\Big\{ (k_1,k_2,k_3) \in \mathbb{Z}_{>0}^3 \ :\ \tfrac{k_1}{a_1} + \tfrac{k_2}{a_2} + \tfrac{k_3}{a_3} \le 1 \Big\}.$$

**Case $\mathbf a = (2,3,7)$.** The minimal weight sum is $\tfrac12 + \tfrac13 + \tfrac17 = \tfrac{41}{42} < 1$, so $(1,1,1)$ qualifies. Increasing any $k_i$ by $1$ adds at least $\tfrac17$, giving $\tfrac{41}{42} + \tfrac17 = \tfrac{47}{42} > 1$. Hence $p_g = 1$. The Milnor number is $\mu = (2-1)(3-1)(7-1) = 12$. Here $p_g \ne 0$ **detects** the singularity: any CR invariant of $X_{(2,3,7)} = \Sigma(2,3,7)$ realizing $p_g$ is nonzero, correctly certifying that no smooth filling exists.

**Case $\mathbf a = (2,3,5)$.** Now $\tfrac12 + \tfrac13 + \tfrac15 = \tfrac{31}{30} > 1$, so no positive lattice point qualifies and $p_g = 0$. Yet $V_{(2,3,5)}$ is the $E_8$ singularity ($\mu = 8$), manifestly not smooth, and $X_{(2,3,5)}$ is the Poincaré homology sphere $\Sigma(2,3,5)$, which bounds no complex manifold in $\mathbb{C}^3$.

**What this shows.** Geometric genus — the obvious analogue of Yau's higher-dimensional Kohn–Rossi condition — is a *sufficient* detector but not a *necessary* one: it is identically zero on the whole class of rational singularities, of which $E_8$ is the extremal example. A correct dimension-3 criterion must separate $X_{(2,3,5)}$ from the round sphere $S^3 = \partial B^4 \subset \mathbb{C}^2$, on which every candidate invariant vanishes. This is exactly what the Du–Yau $s$-invariants are designed to do: $s(V_{E_8}) \ne 0$ while $s = 0$ for the ball, and the open problem is to compute $s$ intrinsically from $\overline{\partial}_b$ on $X$ for an arbitrary strictly pseudoconvex CR 3-manifold.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*