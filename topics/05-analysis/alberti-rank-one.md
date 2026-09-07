---
id: 05-analysis/alberti-rank-one
title: "Alberti's Rank One Theorem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alberti's Rank One Theorem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/alberti-rank-one` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\Omega\subseteq\mathbb{R}^n$ be open and let $u\in BV(\Omega;\mathbb{R}^m)$, so that the distributional derivative $Du$ is an $\mathbb{R}^{m\times n}$-valued finite Radon measure. Write the Radon–Nikodým decomposition with respect to Lebesgue measure,
$$Du = \nabla u\,\mathcal{L}^n\llcorner\Omega + D^su,\qquad D^su \perp \mathcal{L}^n,$$
and let $M(x)=\dfrac{dD^su}{d|D^su|}(x)$ be the polar (matrix-valued density) of the singular part.

**Rank one property.** For $|D^su|$-a.e. $x\in\Omega$,
$$\operatorname{rank} M(x)=1,\qquad\text{i.e.}\quad M(x)=\xi(x)\otimes\eta(x)=\xi(x)\eta(x)^{\mathsf T}$$
for unit vectors $\xi(x)\in\mathbb{R}^m$, $\eta(x)\in\mathbb{R}^n$.

The statement is a *conjecture-turned-theorem*: posed by Ambrosio and De Giorgi in the late 1980s in connection with lower semicontinuity of functionals on $BV$, proved by Giovanni Alberti in 1993. What remains open is not the Euclidean statement but its natural generalisations: to Carnot groups (notably the first Heisenberg group $\mathbb{H}^1$), to metric measure spaces beyond the currently covered $\mathsf{RCD}$ class, and — in the $\mathcal{A}$-free framework that subsumes it — to the sharp converse question of which wave-cone directions are actually realised by singular parts. A complete resolution of those generalisations means either a proof valid in the stated setting or an explicit counterexample map whose singular polar has rank $\ge 2$ on a set of positive $|D^su|$-measure.

## 2. Mathematical Foundations

**BV functions.** $u\in L^1(\Omega;\mathbb{R}^m)$ is of bounded variation if
$$|Du|(\Omega)=\sup\Big\{\int_\Omega u\cdot\operatorname{div}\varphi\,dx\;:\;\varphi\in C_c^1(\Omega;\mathbb{R}^{m\times n}),\ \|\varphi\|_\infty\le1\Big\}<\infty .$$
The Federer–Vol'pert decomposition splits $D^su=D^ju+D^cu$ into a jump part concentrated on the $(n-1)$-rectifiable jump set $J_u$ and a Cantor part vanishing on $\sigma$-finite $\mathcal{H}^{n-1}$ sets.

**Jump part is automatically rank one.** By Federer–Vol'pert,
$$D^ju=(u^+-u^-)\otimes\nu_u\,\mathcal{H}^{n-1}\llcorner J_u ,$$
so the content of the theorem lies entirely in the Cantor part $D^cu$, where no rectifiable carrier is available.

**Curl-free constraint.** $Du$ satisfies the linear PDE constraint
$$\mathcal{A}(Du)=0,\qquad \mathcal{A}=\operatorname{curl}:\quad \partial_k (Du)_{ij}-\partial_j(Du)_{ik}=0 \ \ \text{in }\mathcal{D}'.$$
For a homogeneous constant-coefficient operator $\mathcal{A}=\sum_{|\alpha|=k}A_\alpha\partial^\alpha$ acting on $\mathbb{R}^d$-valued measures, the **wave cone** is
$$\Lambda_{\mathcal{A}}=\bigcup_{\zeta\in\mathbb{R}^n\setminus\{0\}}\ker \mathbb{A}^k(\zeta),\qquad \mathbb{A}^k(\zeta)=\sum_{|\alpha|=k}A_\alpha\zeta^\alpha .$$
For $\mathcal{A}=\operatorname{curl}$ one computes $\Lambda_{\operatorname{curl}}=\{\xi\otimes\eta\}$, the rank-one matrices. So the rank one theorem is the $\operatorname{curl}$ instance of:

**Theorem (De Philippis–Rindler, 2016).** If $\mu$ is an $\mathbb{R}^d$-valued measure with $\mathcal{A}\mu=0$, then
$$\frac{d\mu}{d|\mu|}(x)\in\Lambda_{\mathcal{A}}\qquad\text{for }|\mu^s|\text{-a.e. }x .$$

**Alberti's original engine.** *Lusin-type theorem for gradients* (Alberti, 1991): for every $f\in L^1(\Omega;\mathbb{R}^{m\times n})$ and $\varepsilon>0$ there is $v\in C^1(\Omega;\mathbb{R}^m)$ with $\mathcal{L}^n(\{\nabla v\ne f\})<\varepsilon$ and $\|\nabla v\|_{L^1}\le C\|f\|_{L^1}$ — a $C^1$ function may have an essentially arbitrary prescribed gradient off a small set. Combined with a delicate covering/blow-up argument this forces rank one on the singular polar.

**Rank-one convexity link.** $h:\mathbb{R}^{m\times n}\to\mathbb{R}$ positively $1$-homogeneous and rank-one convex is convex on $\Lambda_{\operatorname{curl}}$-segments; Kirchheim–Kristensen proved such $h$ are in fact convex, and this yields an independent proof of the rank one theorem.

## 3. History & State of the Art (SOTA)

- **Late 1980s.** Ambrosio and De Giorgi isolate the rank one property as the missing ingredient for lower semicontinuity and relaxation of functionals $\int f(Du)$ on $BV$; it is the $BV$ analogue of the fact that only rank-one oscillations are compatible with gradient structure (Tartar's compensated compactness).
- **1991.** Alberti, *A Lusin type theorem for gradients* (J. Funct. Anal. 100).
- **1993.** Alberti, *Rank one property for derivatives of functions with bounded variation* (Proc. Roy. Soc. Edinburgh Sect. A **123**, 239–274). Full proof in all dimensions $n,m$.
- **2000.** Ambrosio–Fusco–Pallara's monograph records it as Theorem 3.94, together with its use in the chain rule and in BV relaxation.
- **2016.** De Philippis–Rindler, *On the structure of $\mathcal{A}$-free measures and applications* (Annals of Math. **184**), give a proof from a general PDE-constrained structure theorem; the same result settles the long-open **rank one property for $BD$** (bounded deformation): the polar of $E^su$ is $a\odot b$.
- **2016.** Kirchheim–Kristensen (Arch. Ration. Mech. Anal. **221**) give a convex-analytic proof.
- **2019.** Massaccesi–Vittone (J. Eur. Math. Soc. **21**) give a short elementary proof via the coarea formula and the structure of sets of finite perimeter.
- **2019.** Extensions: Don–Massaccesi–Vittone to Carnot groups; Ambrosio–Bruè–Semola to $\mathsf{RCD}(K,N)$ metric measure spaces.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $u\in BV(\Omega;\mathbb{R}^m)$, $\Omega\subseteq\mathbb{R}^n$, all $m,n\ge1$ | **Proved** (Alberti 1993); three independent proofs |
| Jump part $D^ju$, any $m,n$ | Elementary, rank one by Federer–Vol'pert |
| $m=1$ (scalar $BV$) | Trivial: $Du$ is $\mathbb{R}^{1\times n}$, rank $\le 1$ always |
| $BD(\Omega)$: symmetric polar $\in\{a\odot b\}$ | **Proved** (De Philippis–Rindler 2016), open since Ambrosio–Coscia–Dal Maso (1997) |
| $BV^k$, $k$-th order derivatives; general $\mathcal{A}$-free measures | Polar lies in $\Lambda_{\mathcal{A}}$ (De Philippis–Rindler 2016) |
| $\mathsf{RCD}(K,N)$ spaces, $N<\infty$ | **Proved** for $BV$ maps into $\mathbb{R}^m$ (Ambrosio–Bruè–Semola 2019) |
| Heisenberg groups $\mathbb{H}^n$, $n\ge2$; step-2 Carnot groups under structural hypotheses | **Proved** (Don–Massaccesi–Vittone 2019) |
| $\mathbb{H}^1$; general Carnot groups of step $\ge3$ | **Open** |
| Dimensional/rectifiability refinements of the singular set | Arroyo-Rabasa–De Philippis–Hirsch–Rindler (2019) |

## 5. Principal Obstacles

- **No rectifiable carrier for $D^cu$.** The Cantor part lives on sets of Hausdorff dimension strictly between $n-1$ and $n$ that carry no approximate tangent plane. Blow-ups need not converge to a single limit, so the standard "differentiate the measure, identify the tangent object" scheme stalls.
- **Blow-up limits are only $\operatorname{curl}$-free, not gradients of nice maps.** At a $|D^su|$-generic point the tangent measures form a nonempty compact family; extracting rank one requires ruling out every $\operatorname{curl}$-free tangent with a rank-$2$ polar. This is exactly the hard step and it is *global* in nature — no pointwise linear-algebra argument suffices.
- **Ornstein's non-inequality.** There is no control of one set of derivatives by another in $L^1$; hence Calderón–Zygmund and Fourier-multiplier arguments, which work perfectly for $p>1$, are unavailable at the endpoint $p=1$ where singular measures live. Every proof must be $L^1$/measure-theoretic.
- **Failure in non-commutative settings.** In Carnot groups the horizontal derivative does not satisfy a constant-coefficient $\operatorname{curl}$ constraint; the wave cone machinery has no direct analogue. In $\mathbb{H}^1$ the relevant subgraph/perimeter argument used for $n\ge 2$ breaks because the codimension bookkeeping degenerates.
- **In metric spaces** there is no Lusin-type gradient theorem and no linear PDE, so proofs must route through splitting/rectifiability of $\mathsf{RCD}$ boundaries, which is what currently limits the result to finite-dimensional $\mathsf{RCD}$.

## 6. The Gap

The Euclidean gap is closed. The residual gaps are sharply localisable:

1. **$\mathbb{H}^1$.** Prove or refute: for $u\in BV_{\mathbb{H}}(\mathbb{H}^1;\mathbb{R}^m)$ the polar of the singular horizontal derivative has rank one. The step used for $\mathbb{H}^n$, $n\ge2$ — reducing to the intrinsic subgraph being a set of finite $\mathbb{H}$-perimeter with $\mathbb{H}$-rectifiable reduced boundary — fails in $\mathbb{H}^1$ because the known rectifiability theory for finite-perimeter sets in $\mathbb{H}^1$ is incomplete.
2. **Converse to De Philippis–Rindler.** The theorem says the polar lies *in* $\Lambda_{\mathcal{A}}$. It does not say every direction of $\Lambda_{\mathcal{A}}$ occurs, nor does it constrain the *dimension* of the carrying set beyond the estimates of Arroyo-Rabasa–De Philippis–Hirsch–Rindler. A full structure theorem — a classification of admissible pairs (singular measure, polar field) — is the missing statement.
3. **Variable-coefficient $\mathcal{A}$.** The wave cone is defined via the constant-coefficient symbol; for operators with rough coefficients the corresponding "pointwise symbol" claim is not known.

## 7. Current Research (as of June 2026)

- **Vienna / Warwick / Oxford (De Philippis, Rindler, Kristensen, Arroyo-Rabasa, Hirsch).** Structure of $\mathcal{A}$-free measures: dimensional estimates, rectifiability of the concentration set, and applications to Cheeger's conjecture and to the converse question. Ongoing work extends the framework to systems with variable coefficients. *(frontier — verify)*
- **Padova / Trento (Vittone, Don, Massaccesi).** Sub-Riemannian $BV$: rank one in Carnot groups, tightly coupled to progress on the Franchi–Serapioni–Serra Cassano rectifiability programme in $\mathbb{H}^1$. *(frontier — verify)*
- **SNS Pisa / Bonn (Ambrosio, Bruè, Semola, Gigli).** $BV$ and sets of finite perimeter on $\mathsf{RCD}$ spaces; extension of the rank one theorem to spaces with only a measure-contraction property. *(frontier — verify)*
- **Quantitative rank one.** Stability/compactness statements measuring how far the polar can be from rank one at finite scale, motivated by numerical relaxation of $BV$ functionals.

## 8. Future Work

- Complete the rectifiability theory for finite-perimeter sets in $\mathbb{H}^1$; this would immediately transfer the Don–Massaccesi–Vittone argument.
- Formulate and prove a *sharp* structure theorem for $\mathcal{A}$-free measures: identify which subsets of $\Lambda_{\mathcal{A}}$ and which singular measures are realisable, closing the converse direction.
- Extend the wave-cone theorem to $\mathcal{A}$ with Lipschitz or continuous coefficients, and to nonlinear differential constraints appearing in compensated compactness.
- Exploit the rank one property to complete the characterisation of $BV$-lower semicontinuous integrands $f$ with linear growth for which the singular recession term is the correct relaxation.
- Develop a metric formulation valid without curvature bounds, e.g. for PI (Poincaré-inequality) spaces with Alberti representations.

## 9. Key References

- **[Foundational]** G. Alberti. *A Lusin type theorem for gradients.* Journal of Functional Analysis, 100(1):110–118, 1991.
- **[Foundational]** G. Alberti. *Rank one property for derivatives of functions with bounded variation.* Proceedings of the Royal Society of Edinburgh Section A, 123(2):239–274, 1993.
- **[Book]** L. Ambrosio, N. Fusco, D. Pallara. *Functions of Bounded Variation and Free Discontinuity Problems.* Oxford University Press, 2000. (Rank one theorem = Theorem 3.94.)
- **[SOTA]** G. De Philippis, F. Rindler. *On the structure of $\mathcal{A}$-free measures and applications.* Annals of Mathematics, 184(3):1017–1039, 2016.
- **[SOTA]** B. Kirchheim, J. Kristensen. *On rank one convex functions that are homogeneous of degree one.* Archive for Rational Mechanics and Analysis, 221(1):527–558, 2016.
- **[SOTA]** A. Massaccesi, D. Vittone. *An elementary proof of the rank-one theorem for BV functions.* Journal of the European Mathematical Society, 21(10):3255–3258, 2019.
- **[SOTA]** S. Don, A. Massaccesi, D. Vittone. *Rank-one theorem and subgraphs of BV functions in Carnot groups.* Journal of Functional Analysis, 276(3):687–715, 2019.
- **[SOTA]** L. Ambrosio, E. Bruè, D. Semola. *Rigidity of the 1-Bakry–Émery inequality and sets of finite perimeter in RCD spaces.* Geometric and Functional Analysis, 29(4):949–1001, 2019.
- **[SOTA]** A. Arroyo-Rabasa, G. De Philippis, J. Hirsch, F. Rindler. *Dimensional estimates and rectifiability for measures satisfying linear PDE constraints.* Geometric and Functional Analysis, 29(3):639–658, 2019.
- **[Survey]** G. De Philippis, F. Rindler. *On the structure of measures constrained by linear PDEs.* Proceedings of the International Congress of Mathematicians (Rio de Janeiro), Vol. III, 2018.
- **[Context]** L. Ambrosio, G. Coscia, G. Dal Maso. *Fine properties of functions with bounded deformation.* Archive for Rational Mechanics and Analysis, 139(3):201–238, 1997.

## 10. Worked Example / Concrete Special Case

**Setup.** $n=m=2$, $\Omega=(0,1)^2$. Let $g:[0,1]\to[0,1]$ be the Cantor–Vitali function (the devil's staircase): continuous, non-decreasing, $g'=0$ $\mathcal{L}^1$-a.e., and $Dg=\mu_C$ is the Cantor measure, concentrated on the middle-thirds set $C$ with $\mathcal{L}^1(C)=0$, $\mu_C([0,1])=1$.

Define
$$u(x_1,x_2)=\big(g(x_1),\,g(x_2)\big).$$

**Compute $Du$.** Since $u_1$ depends only on $x_1$ and $u_2$ only on $x_2$,
$$Du=\begin{pmatrix} \mu_C\otimes\mathcal{L}^1 & 0\\[2pt] 0 & \mathcal{L}^1\otimes\mu_C\end{pmatrix}
= e_1\otimes e_1\,\mu_1 + e_2\otimes e_2\,\mu_2,$$
with $\mu_1=\mu_C\times\mathcal{L}^1$ and $\mu_2=\mathcal{L}^1\times\mu_C$, both finite positive measures on $(0,1)^2$. The approximate gradient vanishes a.e., so $Du=D^su=D^cu$; total variation $|Du|=\mu_1+\mu_2$ (the two matrix directions are orthonormal, so no cancellation).

**Naive worry.** The "constant" matrix $\operatorname{diag}(1,1)=I$ has rank $2$. If $\mu_1$ and $\mu_2$ overlapped on a set of positive measure, the polar there would be $\tfrac{1}{\sqrt2}I$, rank $2$ — contradicting the theorem.

**Resolution.** $\mu_1$ is concentrated on $C\times(0,1)$ and $\mu_2$ on $(0,1)\times C$. Their common carrier is $C\times C$, and
$$\mu_1(C\times C)=\mu_C(C)\cdot\mathcal{L}^1(C)=1\cdot 0=0,\qquad \mu_2(C\times C)=0 .$$
So $\mu_1\perp\mu_2$. By Radon–Nikodým, for $\mu_1$-a.e. $x$ we get $\frac{d\mu_2}{d(\mu_1+\mu_2)}(x)=0$ and
$$M(x)=\frac{dDu}{d|D^su|}(x)=e_1\otimes e_1,$$
and symmetrically $M(x)=e_2\otimes e_2$ for $\mu_2$-a.e. $x$. Both have rank $1$. ∎

**What this illustrates.** The rank one theorem is not about the *matrix values* appearing in $Du$ — those can be anything — but about the impossibility of two independent rank-one directions *sharing a singular carrier*. Here mutual singularity is visible by hand from $\mathcal{L}^1(C)=0$. Alberti's theorem asserts the same conclusion for arbitrary $u\in BV$, where no product structure exists and the carriers of the competing directions are unknown fractal sets; that is precisely the content the elementary example cannot reach.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*