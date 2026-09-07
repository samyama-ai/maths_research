---
id: 06-pdes/minkowski-problem-torsional-rigidity
title: "Minkowski Problem for Torsional Rigidity"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Minkowski Problem for Torsional Rigidity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/minkowski-problem-torsional-rigidity` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Classical Minkowski theory prescribes the **surface area measure** $S(K,\cdot)$ of a convex body. The torsional analogue replaces it by a measure built from the solution of a boundary value problem on $K$.

For a convex body $K \subset \mathbb{R}^n$ ($n \ge 2$) with nonempty interior, let $u_K$ solve the *torsion problem*
$$\Delta u = -2 \ \text{ in } \operatorname{int} K, \qquad u = 0 \ \text{ on } \partial K,$$
and define the **torsional measure** $\mu_T(K,\cdot)$ on $S^{n-1}$ by
$$\mu_T(K,\omega) \;=\; \int_{\nu_K^{-1}(\omega)} |\nabla u_K|^2 \, d\mathcal{H}^{n-1},\qquad \omega \subseteq S^{n-1} \text{ Borel},$$
where $\nu_K$ is the Gauss map (defined $\mathcal{H}^{n-1}$-a.e. on $\partial K$).

> **Minkowski problem for torsional rigidity.** Given a finite Borel measure $\mu$ on $S^{n-1}$, find necessary and sufficient conditions for the existence of a convex body $K$ with $\mu_T(K,\cdot) = \mu$; decide uniqueness up to translation; and determine the regularity of $\partial K$ from the regularity of $\mu$.

**Resolved core (Colesanti–Fimiani, 2010).** A solution exists iff
$$\int_{S^{n-1}} \xi \, d\mu(\xi) = 0 \quad\text{and}\quad \mu \text{ is not concentrated on a great subsphere,}$$
and it is unique up to translation. A complete resolution of the *full* problem additionally requires: (i) sharp regularity ($\mu = f\,d\mathcal{H}^{n-1}$, $f \in C^\infty$, $f>0$ $\Rightarrow$ $\partial K \in C^\infty$ and strictly convex), and (ii) the $L_p$ and Orlicz extensions, which remain open for $p < 1$ — these are the parts that keep the entry active.

## 2. Mathematical Foundations

**Torsional rigidity.** With $u_K$ as above,
$$T(K) \;=\; \int_K |\nabla u_K|^2\,dx \;=\; 2\int_K u_K\,dx \;=\; \sup_{\substack{v \in W^{1,2}_0(K)\\ v \not\equiv 0}} \frac{\left(2\int_K v\,dx\right)^2}{\int_K |\nabla v|^2 dx}.$$
$T$ is monotone under inclusion and homogeneous of degree $n+2$: $T(\lambda K) = \lambda^{n+2} T(K)$.

**Hadamard variational formula.** For convex bodies $K,L$,
$$\left.\frac{d}{dt}\right|_{t=0^+} T(K + tL) \;=\; (n+2)\int_{S^{n-1}} h_L(\xi)\, d\mu_T(K,\xi),$$
where $h_L(\xi) = \sup_{x\in L}\langle x,\xi\rangle$ is the support function. Taking $L=K$ and using Euler's relation gives the "torsional Minkowski relation"
$$T(K) = \int_{S^{n-1}} h_K \, d\mu_T(K,\cdot).$$
Hence $\mu_T(K,\cdot)$ is homogeneous of degree $n+1$ in $K$ and translation-covariant, forcing the centroid condition $\int \xi\, d\mu_T = 0$.

**Brunn–Minkowski inequality for $T$ (Borell 1985).** For convex bodies $K,L$ and $t\in[0,1]$,
$$T\big((1-t)K + tL\big)^{\frac{1}{n+2}} \;\ge\; (1-t)\,T(K)^{\frac{1}{n+2}} + t\,T(L)^{\frac{1}{n+2}},$$
with equality iff $K$ and $L$ are homothetic (Colesanti–Cuoghi–Salani 2006). This is the exact analogue of the $\tfrac1n$-concavity of volume and is what powers both existence (via a variational argument) and uniqueness.

**The PDE.** If $\partial K$ is $C^2$ and strictly convex with support function $h$, and $\mu = f\,d\mathcal{H}^{n-1}$, the problem becomes a *coupled* Monge–Ampère system: find $h>0$ on $S^{n-1}$ and $u$ on $K = \{x : \langle x,\xi\rangle \le h(\xi)\}$ with
$$\big|\nabla u\big(\nabla h(\xi)\big)\big|^2 \cdot \det\!\big(\nabla^2 h(\xi) + h(\xi) I\big) \;=\; f(\xi), \qquad \xi \in S^{n-1},$$
$$\Delta u = -2 \text{ in } K, \quad u = 0 \text{ on } \partial K.$$
Here $\nabla^2$ is the covariant Hessian on $S^{n-1}$ and $\det(\nabla^2 h + hI)$ is the reciprocal Gauss curvature. The nonlocal factor $|\nabla u|^2$ — which depends on *all* of $h$, not on a jet at $\xi$ — is the entire difficulty.

**$L_p$ variant.** For $p \in \mathbb{R}$ set $d\mu_{T,p}(K,\cdot) = h_K^{1-p}\,d\mu_T(K,\cdot)$, the torsional analogue of Lutwak's $L_p$ surface area measure. The case $p=1$ is classical; $p=0$ is the *logarithmic* (cone-torsion) problem.

## 3. History & State of the Art (SOTA)

- **1951.** Pólya–Szegő collect isoperimetric-type inequalities for $T$; the ball maximizes $T$ among bodies of given volume (Saint-Venant).
- **1985.** Borell proves $(n+2)^{-1}$-concavity of $T$ (Greenian potentials and concavity); Colesanti (2005) reproves and generalizes it for variational functionals.
- **1996.** Jerison solves the Minkowski problem for **electrostatic capacity** in $\mathbb{R}^n$, $n\ge3$ (Acta Math.), building on the Brunn–Minkowski inequality for capacity and its equality case (Caffarelli–Jerison–Lieb). This is the template every later "PDE Minkowski problem" follows.
- **2006.** Colesanti–Cuoghi–Salani settle the equality case for $T$ and for the first Dirichlet eigenvalue.
- **2010.** **Colesanti–Fimiani**, *The Minkowski problem for torsional rigidity* (Indiana Univ. Math. J. 59): existence and uniqueness up to translation under the two classical necessary conditions. Method: minimize $\int_{S^{n-1}} h_Q\,d\mu$ over convex bodies $Q$ with $T(Q)=1$, then use the Brunn–Minkowski inequality to show the minimizer's torsional measure is proportional to $\mu$, and rescale using degree-$(n+1)$ homogeneity.
- **2015.** Colesanti–Nyström–Salani–Xiao–Yang–Zhang extend the Hadamard formula and Minkowski problem to $p$-capacity, $1<p<n$ (Adv. Math.).
- **2019–2024.** $L_p$ and Orlicz torsional Minkowski problems; existence for $p>1$ by the same variational scheme, plus polytopal and discrete cases. Regularity theory lags behind: no analogue of Caffarelli's full regularity is known for the coupled system.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $p=1$, arbitrary finite $\mu$ on $S^{n-1}$, $n\ge2$ | **Solved** (existence + uniqueness up to translation), Colesanti–Fimiani 2010 |
| Uniqueness for $p=1$ | **Solved**, from equality case in Borell's inequality (homothety $+$ same measure $\Rightarrow$ translate) |
| $\mu$ discrete with $\ge n+1$ directions not in a hemisphere | Solved; minimizer is a polytope with the prescribed facet data |
| Rotationally symmetric $\mu = c\,d\mathcal{H}^{n-1}$ | Explicit ball solution (Section 10); unique by symmetry $+$ uniqueness |
| $L_p$, $p>1$ (and $p \neq n+2$ normalization) | Existence known by variational/Aleksandrov-type argument; uniqueness open for general $p$ |
| $L_p$, $0<p<1$ | Existence known for even measures / restricted classes; general case open |
| $p=0$ (logarithmic torsion) | Open even for existence with general even $\mu$ |
| Regularity, $n=2$ | Best understood: the Monge–Ampère equation reduces to an ODE-type equation in $h(\theta)$ with $h''+h>0$; $C^{2,\alpha}$ bootstrapping works once strict convexity is assumed |
| Regularity, $n\ge3$ | Only conditional: $\partial K \in C^{2,\alpha}$ and strictly convex $\Rightarrow$ $C^\infty$ by Schauder bootstrapping. Unconditional regularity **open** |

## 5. Principal Obstacles

- **Nonlocality of the density.** In the classical Minkowski problem the equation is $\det(\nabla^2 h + hI) = f$, a genuine Monge–Ampère equation with local structure. Here the factor $|\nabla u|^2$ at a boundary point depends on the global shape of $K$ through the Green function. Caffarelli's regularity theory (strict convexity from a measure-theoretic condition, then $C^{1,\alpha}$, then $W^{2,p}$) uses affine invariance and sections of solutions — both destroyed by the nonlocal factor, which is *not* affinely covariant.
- **Degeneracy at flat pieces and corners.** Near a corner of $\partial K$, $|\nabla u|$ can vanish or blow up like a power of the opening angle. Ruling out flat pieces in the minimizer therefore requires a quantitative boundary Harnack estimate for $u$ that is uniform over the whole minimizing sequence; no such estimate is available in a form independent of the geometry.
- **No affine invariance.** The Laplacian is not affine-invariant, so the standard normalization (John position + affine rescaling) cannot be combined with the PDE. This is precisely the step that makes classical and $L_p$ Monge–Ampère regularity work.
- **Loss of the Brunn–Minkowski tool for $p<1$.** For $p<1$ the natural inequality would be an $L_p$-Brunn–Minkowski inequality for $T$; it is conjectural (it implies the log-Brunn–Minkowski conjecture-type statements for the torsion functional), so both the existence argument and the uniqueness argument lose their engine.
- **Uniqueness beyond $p=1$.** Uniqueness in the classical case is *equivalent* to the equality case of Borell's inequality. For $p \ne 1$ the corresponding equality analysis is unknown, and counterexamples in the volume case ($L_p$-Minkowski with $p<1$ admits non-unique solutions) suggest uniqueness genuinely fails somewhere.

## 6. The Gap

Existence and uniqueness at $p=1$ are theorems; what remains is a two-part gap.

1. **Regularity gap.** Proven: any minimizer is a convex body with $\mu_T(K,\cdot)=\mu$, and $\partial K$ is $C^\infty$ *if* one assumes a priori that it is $C^{2,\alpha}$ and strictly convex. Needed: a proof that $f \in C^\alpha$, $f > 0$ forces strict convexity of $\partial K$ (no flat facets) and $C^{1,1}$ bounds. The exact missing step is a **Caffarelli-type strict-convexity lemma for the coupled system** — an estimate showing that if $\partial K$ contains a segment, then $|\nabla u|^2\det(\nabla^2h+hI)$ must degenerate on a set of positive measure, contradicting $f>0$.
2. **$L_p$ gap for $p<1$.** Proven: existence for $p>1$ and for even measures in restricted ranges. Needed: either an $L_p$-Brunn–Minkowski inequality
$$T\big((1-t)\cdot_p K +_p t\cdot_p L\big)^{\frac{p}{n+2}} \ge (1-t)T(K)^{\frac{p}{n+2}} + tT(L)^{\frac{p}{n+2}},\qquad 0\le p<1,$$
or a replacement variational functional whose Euler–Lagrange equation is the $L_p$ torsional equation.

## 7. Current Research (as of June 2026)

- **Florence / Italian convex geometry school** (Colesanti and collaborators): variational functionals, Hadamard formulas, and equality cases for Brunn–Minkowski-type inequalities; extensions to the $p$-torsional rigidity of the $p$-Laplacian.
- **US–China Minkowski-problem network** (Lutwak–Yang–Zhang lineage, and groups in Beijing, Wuhan, Hunan): $L_p$, dual, and Orlicz torsional Minkowski problems; polytopal existence for $p \le 0$ by discrete approximation. *(frontier — verify)* Several 2024–2026 preprints claim existence for the Orlicz torsional problem under a growth condition on the Orlicz function.
- **Nonlinear potential theory** (Akman, Lewis, Vogel and coauthors): the Memoirs AMS program on Brunn–Minkowski and Minkowski problems for $\mathcal{A}$-harmonic capacity gives the closest available regularity technology; adapting their boundary Harnack estimates to the torsion setting is an active line. *(frontier — verify)*
- **Regularity via degenerate Monge–Ampère**: attempts to treat $|\nabla u|^2$ as a Hölder coefficient obtained by a fixed-point/continuity method on the space of $C^{2,\alpha}$ bodies. Works locally near the ball; global closure of the continuity path is unproven.

## 8. Future Work

- Prove the strict-convexity lemma in $n=3$ first, where the flat-piece analysis is two-dimensional and the boundary behaviour of $u$ near a segment is computable.
- Establish the equality case of the $L_p$-Brunn–Minkowski inequality for $T$ in the range $p>1$, which would give $L_p$ uniqueness.
- Develop a *stability* version of Borell's inequality: if $T((1-t)K+tL)^{1/(n+2)}$ is within $\varepsilon$ of the linear bound, then $K,L$ are $\delta(\varepsilon)$-close to homothetic in Hausdorff distance. This would yield stability for the Minkowski problem itself.
- Numerically solve the coupled system by alternating a finite-element torsion solve with a Monge–Ampère update on $S^{n-1}$; this would test the conjectured regularity and the $p<1$ non-uniqueness.
- Investigate whether the *first eigenvalue* Minkowski problem ($\lambda_1$ replacing $T$) shares the same obstacles — it does, and a technique working for one is expected to transfer.

## 9. Key References

- **[Foundational]** Colesanti, A.; Fimiani, M. *The Minkowski problem for torsional rigidity.* Indiana University Mathematics Journal, **59** (2010), 1013–1039.
- **[Foundational]** Borell, C. *Greenian potentials and concavity.* Mathematische Annalen, **272** (1985), 155–160.
- **[Foundational]** Jerison, D. *A Minkowski problem for electrostatic capacity.* Acta Mathematica, **176** (1996), 1–47.
- **[Foundational]** Caffarelli, L. A.; Jerison, D.; Lieb, E. H. *On the case of equality in the Brunn–Minkowski inequality for capacity.* Advances in Mathematics, **117** (1996), 193–207.
- **[Foundational]** Colesanti, A.; Cuoghi, P.; Salani, P. *Brunn–Minkowski inequalities for two functionals involving the $p$-Laplace operator.* Applicable Analysis, **85** (2006), 45–66.
- **[Foundational]** Colesanti, A. *Brunn–Minkowski inequalities for variational functionals and related problems.* Advances in Mathematics, **194** (2005), 105–140.
- **[SOTA / Recent]** Colesanti, A.; Nyström, K.; Salani, P.; Xiao, J.; Yang, D.; Zhang, G. *The Hadamard variational formula and the Minkowski problem for $p$-capacity.* Advances in Mathematics, **285** (2015), 1511–1588.
- **[SOTA / Recent]** Akman, M.; Gong, J.; Hineman, J.; Lewis, J.; Vogel, A. *The Brunn–Minkowski inequality and a Minkowski problem for nonlinear capacity.* Memoirs of the American Mathematical Society, **275** (2022), no. 1348.
- **[SOTA / Recent]** Chou, K.-S.; Wang, X.-J. *The $L_p$-Minkowski problem and the Minkowski problem in centroaffine geometry.* Advances in Mathematics, **205** (2006), 33–83.
- **[SOTA / Recent]** Lutwak, E. *The Brunn–Minkowski–Firey theory I: Mixed volumes and the Minkowski problem.* Journal of Differential Geometry, **38** (1993), 131–150.
- **[Survey]** Schneider, R. *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded edition. Cambridge University Press, 2014.
- **[Survey]** Pólya, G.; Szegő, G. *Isoperimetric Inequalities in Mathematical Physics.* Princeton University Press, 1951.
- **[Survey]** Huang, Y.; Lutwak, E.; Yang, D.; Zhang, G. *Geometric measures in the dual Brunn–Minkowski theory and their associated Minkowski problems.* Acta Mathematica, **216** (2016), 325–388.

## 10. Worked Example / Concrete Special Case

**Prescribing a constant density: the ball.**

Take $\mu = c \,d\mathcal{H}^{n-1}$ on $S^{n-1}$ with $c>0$. Both necessary conditions hold ($\int \xi\,d\mu = 0$ by symmetry; $\mu$ has full support). Guess $K = B_R$.

*Step 1 — solve the torsion problem.* On $B_R$, try $u(x) = \dfrac{R^2 - |x|^2}{n}$. Then $u=0$ on $\partial B_R$ and
$$\Delta u = \frac{1}{n}\Delta\big(-|x|^2\big) = \frac{-2n}{n} = -2. \checkmark$$

*Step 2 — boundary gradient.* $\nabla u = -\dfrac{2x}{n}$, so on $\partial B_R$, $|\nabla u| = \dfrac{2R}{n}$, constant.

*Step 3 — torsional measure.* The surface area measure of $B_R$ is $dS(B_R,\xi) = R^{n-1} d\mathcal{H}^{n-1}(\xi)$, so
$$d\mu_T(B_R,\xi) = |\nabla u|^2 \, dS(B_R,\xi) = \frac{4R^2}{n^2}\,R^{n-1}\,d\mathcal{H}^{n-1}(\xi) = \frac{4R^{n+1}}{n^2}\,d\mathcal{H}^{n-1}(\xi).$$
Note the degree-$(n+1)$ homogeneity in $R$, as predicted in Section 2.

*Step 4 — match the data.* Setting $\dfrac{4R^{n+1}}{n^2} = c$ gives the unique radius
$$R = \left(\frac{c\,n^2}{4}\right)^{\frac{1}{n+1}}.$$
By the Colesanti–Fimiani uniqueness theorem, $B_R$ is the *only* solution up to translation.

*Step 5 — consistency with the Minkowski relation.* $h_{B_R} \equiv R$, and
$$\int_{S^{n-1}} h\,d\mu_T = R \cdot \frac{4R^{n+1}}{n^2}\,\omega_n = \frac{4\omega_n R^{n+2}}{n^2},\qquad \omega_n := \mathcal{H}^{n-1}(S^{n-1}).$$
Independently,
$$T(B_R) = \int_{B_R}\frac{4|x|^2}{n^2}dx = \frac{4}{n^2}\,\omega_n\!\int_0^R\! r^{n+1}dr = \frac{4\omega_n R^{n+2}}{n^2(n+2)}.$$
So $\int h\,d\mu_T = (n+2)\,T(B_R)$ — matching the Hadamard formula with $L=K$, since $\left.\frac{d}{dt}\right|_{0}T((1+t)K) = (n+2)T(K)$. ✓

*Sanity check in the plane.* For $n=2$, radius $a$: $T = \frac{4}{4}\cdot\frac{2\pi a^{4}}{4} = \frac{\pi a^{4}}{2}$, the classical torsional rigidity of a circular shaft.

*What this example does not settle.* For a *non-constant* $f$, one cannot write $u$ in closed form; the equation
$$|\nabla u(\nabla h(\xi))|^2 \det(\nabla^2 h + hI)(\xi) = f(\xi)$$
is a genuinely coupled Monge–Ampère/Dirichlet system, and the perturbation $f = c(1+\varepsilon Y_k)$ with $Y_k$ a spherical harmonic already requires linearizing both the Monge–Ampère operator and the Green-function-dependent factor — the source of every obstacle in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*