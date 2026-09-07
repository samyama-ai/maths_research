---
id: 05-analysis/brascamp-lieb-constants
title: "Brascamp-Lieb Inequalities"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brascamp–Lieb Inequalities

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/brascamp-lieb-constants` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **Brascamp–Lieb (BL) datum** is a pair $(\mathbf{B},\mathbf{p})$ consisting of surjective linear maps $B_j:\mathbb{R}^n\to\mathbb{R}^{n_j}$ and exponents $p_j\ge 0$, $1\le j\le m$. The **Brascamp–Lieb constant** $\mathrm{BL}(\mathbf{B},\mathbf{p})\in(0,\infty]$ is the smallest $C$ with

$$\int_{\mathbb{R}^n}\prod_{j=1}^{m} \bigl(f_j\circ B_j\bigr)^{p_j}\,dx \;\le\; C\prod_{j=1}^{m}\Bigl(\int_{\mathbb{R}^{n_j}} f_j\Bigr)^{p_j}$$

for all non-negative $f_j\in L^1(\mathbb{R}^{n_j})$.

The problem has three parts, of which the first is settled and the other two are open.

1. **(Solved.)** Decide when $\mathrm{BL}<\infty$, compute it, and describe its extremisers.
2. **(Open — regularity.)** Determine the exact regularity of the map $\mathbf{B}\mapsto \mathrm{BL}(\mathbf{B},\mathbf{p})$ on the locus of finiteness. It is continuous but not smooth; no sharp modulus of continuity is known, and no algorithm computing $\mathrm{BL}$ to accuracy $\varepsilon$ in time polynomial in $\log(1/\varepsilon)$ is known.
3. **(Open — nonlinear/curved case.)** Determine when the inequality survives replacing the linear $B_j$ by smooth submersions $B_j:U\subseteq\mathbb{R}^n\to\mathbb{R}^{n_j}$, with a constant uniform over a fixed-size neighbourhood, and with what dependence on the curvature of the fibres. A complete solution must (i) give a checkable criterion on the jets of $(B_j)$ equivalent to a uniform bound, and (ii) control the constant globally, not merely on a neighbourhood shrinking with the datum.

Resolving (3) in the sharp endpoint form would in particular yield the **endpoint multilinear restriction conjecture** of Bennett–Carbery–Tao, still open.

## 2. Mathematical Foundations

**Scaling and finiteness.** Bennett–Carbery–Christ–Tao (2008): $\mathrm{BL}(\mathbf{B},\mathbf{p})<\infty$ iff

$$n=\sum_{j=1}^m p_j n_j \quad\text{(scaling)},\qquad \dim V\le \sum_{j=1}^m p_j \dim (B_j V)\ \ \forall\,V\subseteq\mathbb{R}^n \text{ subspace} \quad\text{(dimension)}.$$

The dimension conditions cut out a polytope in $\mathbf{p}$ for fixed $\mathbf{B}$; it is a polymatroid base polytope, and the extreme points have rational coordinates with bounded denominators.

**Lieb's theorem (Gaussian exhaustion).** Lieb (1990): the supremum is exhausted by centred Gaussians $f_j(y)=e^{-\pi\langle A_jy,y\rangle}$, $A_j$ positive definite. Hence

$$\mathrm{BL}(\mathbf{B},\mathbf{p})=\sup_{A_j>0}\left(\frac{\prod_{j=1}^m (\det A_j)^{p_j}}{\det\bigl(\sum_{j=1}^m p_j B_j^{*}A_jB_j\bigr)}\right)^{1/2}.$$

Writing $A_j=e^{X_j}$ makes $-\log$ of the bracket a *geodesically convex* function on the product of symmetric spaces $\mathrm{PD}(n_j)$, so the computation is a convex program — but one whose sup may be approached only at infinity.

**Geometric case (Ball, Barthe).** If each $B_j$ is the orthogonal projection $P_j$ onto a subspace $V_j\subseteq\mathbb{R}^n$ and

$$\sum_{j=1}^m p_j P_j = I_n,$$

then $\mathrm{BL}(\mathbf{B},\mathbf{p})=1$, with Gaussian extremisers $A_j=I$. Every extremisable datum is equivalent to a geometric one after a change of variables $x\mapsto Cx$, $y_j\mapsto C_jy_j$.

**Rank-one case.** With $n_j=1$, $B_jx=\langle x,u_j\rangle$, $|u_j|=1$: $\sum_j p_j u_j\otimes u_j=I_n$ gives Ball's inequality, whose sharp form underlies the $\sqrt{2}$ bound for hyperplane sections of the cube.

**Reverse form (Barthe).** For $g_j\ge 0$ and $h(x)\ge \prod_j g_j(y_j)^{p_j}$ whenever $x=\sum_j p_jB_j^*y_j$,
$\int h \ge \mathrm{BL}_{-}(\mathbf{B},\mathbf{p})\prod_j(\int g_j)^{p_j}$, and $\mathrm{BL}_-$ is again computed by Gaussians. It interpolates Prékopa–Leindler and the reverse Young inequality.

**Nonlinear localisation.** For submersions $B_j$ near $x_0$, one asks for
$\int_{U}\prod_j (f_j\circ B_j)^{p_j}\le C\prod_j\|f_j\|_1^{p_j}$
with $C=(1+\varepsilon)\,\mathrm{BL}(d\mathbf{B}(x_0),\mathbf{p})$ and $U$ a neighbourhood.

## 3. History & State of the Art

- **1975–76.** Beckner computed the sharp constant in the Hausdorff–Young inequality; Brascamp and Lieb, in *Adv. Math.* 20 (1976), found the sharp constant in Young's convolution inequality and stated the general multi-function inequality, proving Gaussian exhaustion for the rank-one case.
- **1989–90.** Ball proved the rank-one geometric case, motivated by convex geometry. Lieb (Invent. Math. 102, 1990) proved Gaussian exhaustion in full generality, reducing the constant to a finite-dimensional variational problem.
- **1998.** Barthe (Invent. Math. 134) proved the reverse inequality and gave a transportation proof of the geometric case.
- **2004–08.** Carlen–Lieb–Loss developed spherical analogues; Valdimarsson (Israel J. Math. 168, 2008) classified optimisers via the lattice of critical subspaces.
- **2008.** Bennett–Carbery–Christ–Tao (GAFA 17) gave the finiteness criterion, proved local boundedness of the constant, characterised extremisability, and established the heat-flow monotonicity proof.
- **2006–2015.** Bennett–Carbery–Tao (Acta Math. 196, 2006) proved multilinear Kakeya/restriction with $\varepsilon$-loss; Guth (Acta Math. 205, 2010) removed the loss for multilinear Kakeya via the polynomial method. Bourgain–Demeter's $\ell^2$ decoupling theorem (Ann. Math. 182, 2015) made BL-type transversality estimates a standard tool.
- **2017–18.** Bennett–Bez–Cowling–Flock (Bull. LMS 49) proved $\mathbf{B}\mapsto\mathrm{BL}$ is continuous on the finiteness locus. Garg–Gurvits–Oliveira–Wigderson (GAFA 28) gave a polynomial-time algorithm deciding finiteness and computing $\mathrm{BL}$ to multiplicative $(1+\varepsilon)$ in time $\mathrm{poly}(\text{input},1/\varepsilon)$ using operator scaling.
- **2020.** Bennett–Bez–Buschenhenke–Cowling–Flock (Duke Math. J. 169) proved the **local nonlinear Brascamp–Lieb inequality** for every datum with finite constant.

## 4. Partial Results / Verified Cases

- **All linear data.** Finiteness is decidable and $\mathrm{BL}$ is computable to arbitrary multiplicative precision (BCCT 2008 + GGOW 2018). Finiteness testing is polynomial time despite the dimension condition ranging over a continuum of subspaces.
- **Geometric data:** $\sum p_jB_j^*B_j=I_n$ with $B_jB_j^*=I_{n_j}$ gives $\mathrm{BL}=1$ exactly.
- **Loomis–Whitney,** $n$ arbitrary, $B_j$ = coordinate projections $\mathbb{R}^n\to\mathbb{R}^{n-1}$, $p_j=\tfrac1{n-1}$: constant $1$.
- **Young's convolution inequality** ($n=2$, $m=3$, $n_j=1$): constant $\prod_j C_{1/p_j}$ with $C_p=(p^{1/p}/(p')^{1/p'})^{1/2}$; solved in closed form since 1976.
- **Rank-one data** $n_j=1$, all $n,m$: constant and extremisers explicit whenever the datum is extremisable.
- **Nonlinear, local:** for any $C^2$ submersions whose differentials at $x_0$ form a finite BL datum, and any $\varepsilon>0$, there is a neighbourhood $U$ of $x_0$ on which the inequality holds with $(1+\varepsilon)\mathrm{BL}$ (BBBCF 2020). Earlier uniform-neighbourhood results were known for the Loomis–Whitney and rank-one cases.
- **Multilinear Kakeya:** endpoint case proven for all $n$ (Guth 2010); the associated BL constants for the transversal datum are $O(1)$.
- **Forward–reverse (Courtade–Liu, J. Geom. Anal. 31, 2021):** finiteness, structure and extremals characterised for the combined Euclidean forward–reverse family.

## 5. Principal Obstacles

- **Non-compactness of the Gaussian variational problem.** The supremum in Lieb's formula is over the non-compact cone $\prod_j\mathrm{PD}(n_j)$, and for non-extremisable data it is attained only in the limit $A_j\to\partial$. Degenerating along a critical subspace is exactly what makes $\mathrm{BL}$ non-smooth; standard implicit-function or perturbation arguments have no fixed point to perturb around.
- **Combinatorial blow-up of critical subspaces.** Regularity of $\mathbf{B}\mapsto \mathrm{BL}$ is governed by the lattice of subspaces achieving equality in the dimension condition. This lattice changes discontinuously with $\mathbf{B}$, so the constant is only piecewise-analytic with unknown strata; no algebraic parametrisation of the strata is known.
- **Heat-flow monotonicity is fragile.** The BCCT semigroup proof requires exact linearity: $f_j\circ B_j$ heat-evolves to $f_j^{(t)}\circ B_j$ only when $B_j$ is linear. For curved $B_j$ the fibres are not translates and the monotone quantity is destroyed; the induction-on-scales substitute in BBBCF loses a factor per scale, which forces the neighbourhood $U$ to shrink as $\varepsilon\to0$.
- **No sharp transversality invariant.** In the curved case the natural obstruction is second-order (curvature of the level sets), but no scalar invariant is known whose finiteness is *equivalent* to a uniform bound; all current criteria are sufficient only.
- **Complexity.** Operator scaling converges at rate $\mathrm{poly}(1/\varepsilon)$ because the geodesic convexity is not strong; obtaining $\log(1/\varepsilon)$ requires a condition-number bound that fails near non-extremisable data.

## 6. The Gap

Proven: for a *fixed* datum with finite constant, the nonlinear inequality holds on *some* neighbourhood with constant $(1+\varepsilon)\mathrm{BL}$. Wanted: a neighbourhood whose size is bounded below in terms of a finite list of quantitative invariants ($\mathrm{BL}$, $C^2$ norms, transversality), uniformly over families of data. The precise missing step is a **quantitative stability estimate**: a bound of the form

$$|\mathrm{BL}(\mathbf{B},\mathbf{p})-\mathrm{BL}(\mathbf{B}',\mathbf{p})|\le \Phi\bigl(\|\mathbf{B}-\mathbf{B}'\|\bigr)$$

with $\Phi$ explicit and depending only on the finiteness margin $\delta=\min_V\bigl(\sum_jp_j\dim B_jV-\dim V\bigr)$ over non-critical $V$. Continuity is known; no such $\Phi$ is. Without it, the induction-on-scales in the nonlinear argument cannot be iterated a scale-independent number of times, which is exactly what separates the $\varepsilon$-loss multilinear restriction estimate from its endpoint form.

## 7. Current Research (as of June 2026)

- **Birmingham / Saitama / Kiel school** (Bennett, Bez, Buschenhenke, Cowling, Flock): quantitative and global nonlinear BL, and BL with additional Fourier-analytic weights.
- **Regularised / weighted BL:** Maldague's regularised Brascamp–Lieb inequalities (Q. J. Math., 2022) trade sharpness for stability and are being used to make decoupling constants uniform. *(frontier — verify)* Extensions to variable-coefficient decoupling are in preprint circulation.
- **Algorithmic side** (Princeton/IAS, Berkeley, Bonn): non-commutative optimisation — Bürgisser, Franks, Garg, Oliveira, Walter, Wigderson — pushing scaling algorithms toward $\log(1/\varepsilon)$ precision and moment-polytope membership.
- **Beyond $\mathbb{R}^n$:** BL on compact Lie groups, the Heisenberg group, and discrete/graph settings; entropic reformulations connecting to network information theory (Courtade, Liu).
- **Restriction/Kakeya:** after the resolution of the three-dimensional Kakeya set conjecture by Wang and Zahl *(frontier — verify)*, attention has returned to whether BL-based multilinear-to-linear reductions can be made endpoint-sharp in higher dimensions.

## 8. Future Work

- Identify the semi-algebraic stratification of the finiteness locus on which $\mathrm{BL}$ is real-analytic; conjecturally $\mathrm{BL}$ is locally Hölder with exponent determined by the critical-subspace lattice.
- Develop a curvature-adapted monotone functional replacing heat flow, so the nonlinear case is proved directly rather than by induction on scales.
- Prove a strong-convexity / condition-number bound for the Gaussian program under a quantitative extremisability hypothesis, giving a $\log(1/\varepsilon)$ algorithm.
- Establish stability: if a near-extremiser nearly saturates a geometric datum, is it close to a Gaussian in a quantitative sense?
- Push forward–reverse and entropic BL to non-Euclidean base spaces with the Gaussian-exhaustion principle intact.

## 9. Key References

- **[Foundational]** H. J. Brascamp and E. H. Lieb. *Best constants in Young's inequality, its converse, and its generalization to more than three functions.* Advances in Mathematics 20 (1976), 151–173.
- **[Foundational]** E. H. Lieb. *Gaussian kernels have only Gaussian maximizers.* Inventiones Mathematicae 102 (1990), 179–208.
- **[Foundational]** W. Beckner. *Inequalities in Fourier analysis.* Annals of Mathematics 102 (1975), 159–182.
- **[Foundational]** K. Ball. *Volumes of sections of cubes and related problems.* Geometric Aspects of Functional Analysis, Lecture Notes in Mathematics 1376, Springer, 1989, 251–260.
- **[Foundational]** F. Barthe. *On a reverse form of the Brascamp–Lieb inequality.* Inventiones Mathematicae 134 (1998), 335–361.
- **[SOTA]** J. Bennett, A. Carbery, M. Christ, T. Tao. *The Brascamp–Lieb inequalities: finiteness, structure and extremals.* Geometric and Functional Analysis 17 (2008), 1343–1415.
- **[SOTA]** J. Bennett, A. Carbery, T. Tao. *On the multilinear restriction and Kakeya conjectures.* Acta Mathematica 196 (2006), 261–302.
- **[SOTA]** L. Guth. *The endpoint case of the Bennett–Carbery–Tao multilinear Kakeya conjecture.* Acta Mathematica 205 (2010), 263–286.
- **[SOTA]** J. Bennett, N. Bez, M. Cowling, T. Flock. *Behaviour of the Brascamp–Lieb constant.* Bulletin of the London Mathematical Society 49 (2017), 512–518.
- **[SOTA]** A. Garg, L. Gurvits, R. Oliveira, A. Wigderson. *Algorithmic and optimization aspects of Brascamp–Lieb inequalities, via operator scaling.* Geometric and Functional Analysis 28 (2018), 100–145.
- **[Recent]** J. Bennett, N. Bez, S. Buschenhenke, M. Cowling, T. Flock. *On the nonlinear Brascamp–Lieb inequality.* Duke Mathematical Journal 169 (2020), 3291–3338.
- **[Recent]** T. A. Courtade and J. Liu. *Euclidean forward–reverse Brascamp–Lieb inequalities: finiteness, structure and extremals.* Journal of Geometric Analysis 31 (2021), 3300–3350.
- **[Recent]** S. I. Valdimarsson. *Optimisers for the Brascamp–Lieb inequality.* Israel Journal of Mathematics 168 (2008), 253–274.
- **[Survey]** J. Bennett. *Aspects of multilinear harmonic analysis related to transversality.* Contemporary Mathematics 612, American Mathematical Society, 2014, 1–28.
- **[Survey]** E. Carlen, E. H. Lieb, M. Loss. *A sharp analog of Young's inequality on $S^N$ and related entropy inequalities.* Journal of Geometric Analysis 14 (2004), 487–520.

## 10. Worked Example / Concrete Special Case

Take $n=2$, $m=3$, $n_j=1$ and

$$B_1(x,y)=x,\qquad B_2(x,y)=y,\qquad B_3(x,y)=x+y,\qquad p_1=p_2=p_3=\tfrac23 .$$

**Finiteness.** Scaling: $\sum_jp_jn_j=3\cdot\tfrac23=2=n$. ✓ For a line $V=\mathbb{R}v$, all three $\dim B_jV$ equal $1$ unless $v$ lies in $\ker B_j$. The three exceptional lines are $\mathbb{R}e_2,\ \mathbb{R}e_1,\ \mathbb{R}(1,-1)$, each killing exactly one $B_j$, so the condition reads $1\le \tfrac23+\tfrac23=\tfrac43$. ✓ For generic $V$: $1\le 2$. ✓ Hence $\mathrm{BL}<\infty$.

**Gaussian computation.** With $A_j=a_j>0$ scalars,

$$\sum_j p_j B_j^*a_jB_j=\tfrac23\begin{pmatrix} a_1+a_3 & a_3\\ a_3 & a_2+a_3\end{pmatrix},\qquad \det=\tfrac49\,(a_1a_2+a_1a_3+a_2a_3).$$

Lieb's formula gives

$$\mathrm{BL}^2=\sup_{a_j>0}\frac{(a_1a_2a_3)^{2/3}}{\tfrac49(a_1a_2+a_1a_3+a_2a_3)}=\frac94\sup_{a_j>0}\frac{(a_1a_2a_3)^{2/3}}{a_1a_2+a_1a_3+a_2a_3}.$$

By AM–GM, $a_1a_2+a_1a_3+a_2a_3\ge 3\,(a_1a_2a_3)^{2/3}$, with equality iff $a_1=a_2=a_3$. Therefore

$$\mathrm{BL}^2=\frac94\cdot\frac13=\frac34,\qquad \boxed{\ \mathrm{BL}=\frac{\sqrt3}{2}\approx 0.8660\ }$$

and the datum is extremisable, with extremisers the isotropic Gaussians $f_j(t)=e^{-\pi a t^2}$.

**Consistency check.** Substituting $g_j=f_j^{2/3}$ turns the inequality into $\int_{\mathbb{R}^2}g_1(x)g_2(y)g_3(x+y)\,dx\,dy\le C\prod_j\|g_j\|_{3/2}$, i.e. Young's convolution inequality at the symmetric exponent $3/2$. The Brascamp–Lieb–Beckner constant is $C_{3/2}^{3}$ with $C_p=\bigl(p^{1/p}/(p')^{1/p'}\bigr)^{1/2}$; since $C_{3/2}=\bigl(3^{1/3}2^{-2/3}\bigr)^{1/2}$, we get $C_{3/2}^3=3^{1/2}/2=\sqrt3/2$. ✓

**What the open problem adds.** Replace $B_3$ by the curved submersion $\tilde B_3(x,y)=x+y+\tfrac12 x^2$. Its differential at the origin is $B_3$, so BBBCF gives the same bound $(1+\varepsilon)\sqrt3/2$ on *some* neighbourhood $U_\varepsilon$ of $0$. No known argument controls $|U_\varepsilon|$ from below in terms of $\varepsilon$, $\sqrt3/2$ and $\|\tilde B_3\|_{C^2}$ alone — that quantitative bound is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*