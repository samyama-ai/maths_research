---
id: 06-pdes/monge-ampere-degenerate-regularity
title: "Monge Ampere Degenerate Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Regularity for the Degenerate Monge–Ampère Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/monge-ampere-degenerate-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ be a bounded convex domain and let $f \ge 0$ on $\overline{\Omega}$. Consider the Dirichlet problem for the real Monge–Ampère operator

$$\det D^2 u = f \quad \text{in } \Omega, \qquad u = \varphi \quad \text{on } \partial\Omega,$$

sought among convex functions $u$, with $\det D^2u$ interpreted in the Alexandrov (Monge–Ampère measure) sense. When $f \ge c > 0$ the equation is uniformly elliptic on the solution and the Caffarelli–Nirenberg–Spruck / Caffarelli theory gives a complete regularity picture. The **degenerate** problem is the case $\inf_\Omega f = 0$.

**Central question.** Determine the sharp modulus of regularity of $u$ in terms of the vanishing structure of $f$, $\varphi$ and $\partial\Omega$. Concretely:

1. *(Sharp scale)* Guan–Trudinger–Wang proved $u \in C^{1,1}(\overline\Omega)$ when $f^{1/(n-1)} \in C^{1,1}(\overline\Omega)$, $\Omega$ uniformly convex, $\varphi \in C^{3,1}$. **Is $f^{1/(n-1)} \in C^{1,1}$ optimal, and what is the sharp interior condition?** In particular, for $f^{1/(n-1)} \in C^{\alpha}$ with $\alpha \in (0,1)$, what is the sharp interior modulus — is it $C^{1,\beta(\alpha,n)}$ for an explicit $\beta$?
2. *(Higher regularity on the degeneracy set)* If $f \ge 0$ is $C^\infty$ and vanishes on a smooth hypersurface $\Sigma \subset \Omega$ to finite order $k$, is $u$ smooth away from $\Sigma$ and $C^{k'}$ across $\Sigma$ for a sharp $k' = k'(k,n)$?
3. *(Sobolev regularity)* For which $n$ and which degeneracy rates does $D^2u \in L^1_{loc}$ or $W^{2,1+\varepsilon}_{loc}$ hold? Mooney showed both fail for degenerate $f$ in $n \ge 3$; the sharp threshold is unknown.

A complete resolution means: a necessary-and-sufficient condition on $(f,\varphi,\Omega)$ for $u \in C^{1,1}$, plus matching counterexamples at each exponent.

## 2. Mathematical Foundations

**Alexandrov solutions.** For convex $u:\Omega \to \mathbb{R}$ the subdifferential is $\partial u(x) = \{p : u(y) \ge u(x) + p\cdot(y-x)\ \forall y\}$. The Monge–Ampère measure is
$$Mu(E) := \big|\partial u(E)\big| = \Big|\bigcup_{x\in E}\partial u(x)\Big|,$$
a Radon measure. $u$ is an Alexandrov solution of $\det D^2u = f$ if $Mu = f\,dx$. For $u \in C^2$ strictly convex, $Mu = \det D^2u\,dx$.

**Affine invariance.** If $A \in GL(n)$ and $v(x) = (\det A)^{-2/n} u(Ax)$ then $\det D^2 v = f(Ax)$. This invariance forces all estimates to be stated in terms of *sections*
$$S_h(x_0) := \{x \in \Omega : u(x) < u(x_0) + p\cdot(x-x_0) + h\},\quad p \in \partial u(x_0),$$
which play the role of balls. John's lemma gives $E \subset S_h \subset nE$ for an ellipsoid $E$; when $f \asymp 1$, $|S_h| \asymp h^{n/2}$.

**Where degeneracy breaks ellipticity.** Linearizing at $u$ gives the coefficient matrix $\operatorname{cof}(D^2u)$, with
$$\lambda_{\min}\big(\operatorname{cof}\,D^2u\big) \cdot \lambda_{\max}(D^2u) \ \le\ \det D^2 u = f .$$
So $f \to 0$ forces the ellipticity ratio of the linearized operator to degenerate: the equation is *degenerate elliptic*, not merely non-uniformly elliptic, and Caffarelli's strict-convexity machinery (which requires $\lambda |E| \le Mu(E) \le \Lambda|E|$) is unavailable.

**The exponent $1/(n-1)$.** If $u$ is flat in $n-1$ directions with Hessian eigenvalue $a$ there and $O(1)$ in the remaining direction, then $\det D^2u \approx a^{n-1}$, so $a \approx f^{1/(n-1)}$. Boundedness of $D^2u$ therefore couples to $f^{1/(n-1)}$, not to $f$ — this is the structural origin of the Guan–Trudinger–Wang hypothesis.

**Main theorems relied upon.**
- *(Caffarelli 1990)* If $0 < \lambda \le f \le \Lambda$, an Alexandrov solution is strictly convex and $C^{1,\alpha}_{loc}$ in $n=2$ and in higher $n$ under localization; if $f \in C^\alpha$ and $u$ is strictly convex then $u \in C^{2,\alpha}_{loc}$, and $f$ continuous gives $u\in W^{2,p}_{loc}$ for all $p<\infty$.
- *(Pogorelov)* $u(x) = |x'|^{2-2/n}(1 + x_n^2)$, $x' = (x_1,\dots,x_{n-1})$, $n \ge 3$, solves $\det D^2u = f$ with $f>0$ smooth near $0$ but $u \notin C^2$ — strict convexity is necessary even in the nondegenerate case.
- *(Alexandrov maximum principle)* $|u(x)|^n \le C_n (\operatorname{diam}\Omega)^{n-1}\operatorname{dist}(x,\partial\Omega)\,Mu(\Omega)$.

## 3. History & State of the Art (SOTA)

- **1953–1971.** Alexandrov and Bakelman develop the generalized-solution theory; existence and uniqueness for $Mu = \mu$ with $\mu$ any finite measure and continuous boundary data on a strictly convex domain hold with no positivity assumption — so *existence* is never the issue, only regularity.
- **1977.** Rauch–Taylor (Rocky Mountain J. Math.) treat $\det D^2u = 0$: solutions are convex envelopes, ruled by segments, and generically not $C^1$ for merely convex data.
- **1984.** Caffarelli–Nirenberg–Spruck (CPAM 37) solve the classical Dirichlet problem for $f>0$, $f^{1/n}$ convex-compatible data, obtaining $C^{2,\alpha}$ and $C^\infty$ solutions; the degenerate case $f \ge 0$ is explicitly left open.
- **1987.** Hong–Zuily (Invent. Math. 89) obtain local $C^\infty$ solvability for degenerate $f$ vanishing to finite order with nondegenerate transversal structure, using Nash–Moser and subelliptic estimates.
- **1990–1991.** Caffarelli's localization, $W^{2,p}$ and $C^{2,\alpha}$ theory settles the nondegenerate interior problem.
- **1995.** Xu-Jia Wang (Proc. AMS 123) constructs counterexamples: $f^{1/(n-1)} \in C^\alpha$, $\alpha<1$, does **not** imply $u \in C^{1,1}$; the $1/(n-1)$-scale is genuinely the right one.
- **1997–1999.** Pengfei Guan (Duke 86) proves interior $C^{1,1}$ estimates for degenerate Monge–Ampère under $f^{1/(n-1)} \in C^{1,1}$; Guan–Trudinger–Wang (Acta Math. 182, 1999) give the definitive global result: $\Omega$ uniformly convex $C^{3,1}$, $\varphi \in C^{3,1}$, $f^{1/(n-1)} \in C^{1,1}$, $f\ge 0$ $\Rightarrow$ a unique convex $u \in C^{1,1}(\overline\Omega)$. This remains SOTA for the global problem.
- **2009.** Daskalopoulos–Savin (CPAM 62) analyze $\det D^2u = |x|^\alpha$ and homogeneous right-hand sides, obtaining sharp $C^{1,\beta}$/$C^{2,\alpha}$ statements for point degeneracy.
- **2013.** De Philippis–Figalli (Invent. Math. 192) and De Philippis–Figalli–Savin (Math. Ann. 357) prove $W^{2,1}$ and $W^{2,1+\varepsilon}$ interior regularity for $0<\lambda\le f\le\Lambda$; Savin (JAMS 26) proves boundary $C^{2,\alpha}$ via boundary localization.
- **2015–2016.** Connor Mooney proves the singular set has zero $\mathcal H^{n-1}$ measure for $f$ bounded between positive constants (CPAM 68, 2015), and constructs degenerate examples with $D^2u \notin L^1$ in $n\ge 3$ (Anal. PDE 9, 2016) — showing the nondegenerate Sobolev theory has no degenerate analogue.

## 4. Partial Results / Verified Cases

- **$n = 2$, $f \ge 0$ with $f^{1/(n-1)} = f \in C^{1,1}$:** $u \in C^{1,1}$ globally (Guan–Trudinger–Wang). In two dimensions the degeneracy set is at most a curve and Alexandrov's classical two-dimensional theory gives strict convexity for $f>0$; singular solutions do not exist for $n=2$ with $f\ge\lambda>0$.
- **All $n\ge2$, $f^{1/(n-1)}\in C^{1,1}(\overline\Omega)$, $\varphi\in C^{3,1}$, $\partial\Omega\in C^{3,1}$ uniformly convex:** unique $u\in C^{1,1}(\overline\Omega)$; the bound $\|D^2u\|_{L^\infty}$ depends only on $\|f^{1/(n-1)}\|_{C^{1,1}}$, $\|\varphi\|_{C^{3,1}}$ and the convexity modulus.
- **Point degeneracy $f(x)=|x|^\alpha$, $\alpha>0$:** homogeneity forces $u \sim |x|^{2+\alpha/2}$ modulo affine maps, hence $u\in C^{2,\alpha/2}$ near the degenerate point for $\alpha/2 \notin \mathbb{Z}$ (Daskalopoulos–Savin, CPAM 2009). Point degeneracy costs nothing.
- **$f \equiv 0$ (fully degenerate):** the solution is the convex envelope of the boundary data; $u \in C^{0,1}$ always, $u\in C^{1,1}$ when $\varphi$ extends to a $C^{1,1}$ convex function, and $u\in C^{1,\alpha}$ results are known in $n=2$. No $C^2$ regularity in general.
- **Finite-order degeneracy with transversality (Hong–Zuily 1987):** $f\ge0$ vanishing to finite order on a hypersurface, with a nondegenerate initial datum, admits *local* $C^\infty$ convex solutions.
- **Complex analogue:** for $\det(\partial\bar\partial u)=f\ge0$ with $f^{1/(n-1)}\in C^{1,1}$, the analogous $C^{1,1}$ statement holds (Guan; and, for the homogeneous complex equation, Bedford–Taylor / Chen's geodesic regularity).
- **Optimality:** $C^{1,1}$ cannot be improved to $C^2$ — explicit examples in Section 10; and $C^\alpha$ control of $f^{1/(n-1)}$, $\alpha<1$, does not give $C^{1,1}$ (Wang 1995).

## 5. Principal Obstacles

- **Loss of uniform ellipticity.** Every interior estimate in the nondegenerate theory (Caffarelli's $C^{1,\alpha}$, $W^{2,p}$, $C^{2,\alpha}$) starts from the two-sided bound $\lambda|E|\le Mu(E)\le\Lambda|E|$, which yields the "engulfing" property of sections and a Krylov–Safonov-type Harnack inequality on the section quasi-metric. With $f\to0$ sections can become arbitrarily eccentric at a fixed scale; the John ellipsoid ratio is unbounded and the affine-invariant Harnack machinery collapses.
- **No strict convexity.** Degenerate $f$ lets the graph of $u$ contain line segments through the interior. On such a segment the linearized operator is not just degenerate but has a nontrivial kernel direction; unique continuation and interior Schauder theory both fail.
- **Third derivatives are not controlled.** Pogorelov's $C^2$ estimate is obtained by differentiating twice and using $\log\det$ concavity; the resulting test function requires $f^{1/n}$ or $f^{1/(n-1)}$ to be semi-convex. Below $C^{1,1}$ regularity of $f^{1/(n-1)}$ the differentiated equation has an unbounded zeroth-order term and the maximum-principle argument produces no bound.
- **The $1/(n-1)$ power is nonlinear and non-perturbative.** The natural quantity $f^{1/(n-1)}$ is not a linear functional of the data, so the problem does not linearize around the degenerate solution; approximation by nondegenerate problems $f_\varepsilon = f+\varepsilon$ gives $\varepsilon$-dependent estimates that blow up exactly at the rate one is trying to control.
- **Sobolev theory has no degenerate substitute.** Mooney's 2016 examples show $D^2u\notin L^1_{loc}$ for degenerate $f$ in $n\ge3$, so one cannot even work in a distributional second-derivative framework; the only available object is the Monge–Ampère measure.
- **Codimension of the degeneracy set matters and is not encoded by any known norm.** $f=|x|^\alpha$ (point) is harmless; $f=|x_1|^\alpha$ (hyperplane) is not. Existing hypotheses are norm-based and blind to this distinction.

## 6. The Gap

Proven (Section 4): $f^{1/(n-1)}\in C^{1,1}\Rightarrow u\in C^{1,1}$, sharp in the sense that $C^2$ fails. Disproven: $f^{1/(n-1)}\in C^{\alpha}$, $\alpha<1$, $\not\Rightarrow u\in C^{1,1}$.

The gap is the entire interval $\alpha \in [1,2)$ — i.e. $f^{1/(n-1)}$ Lipschitz or $C^{1,\alpha}$ but not $C^{1,1}$ — where neither a proof nor a counterexample is known, together with the following two precise missing steps:

1. **A degenerate replacement for the affine-invariant Harnack inequality.** One needs an estimate on sections $S_h$ whose constants depend only on $\|f^{1/(n-1)}\|_{C^{0,1}}$ and the *geometry of $\{f=0\}$*, not on $\inf f$. No such quantity currently exists.
2. **A sharp interior modulus.** For $f^{1/(n-1)}\in C^\alpha$, $0<\alpha<1$, the conjectural answer $u\in C^{1,\beta}$ with $\beta = \beta(\alpha,n)$ has no proof for any $\beta>0$ independent of the structure of $\{f=0\}$, and no matching example pinning $\beta$.

Crossing the gap requires estimating $D^2u$ across the degeneracy set using only one derivative of $f^{1/(n-1)}$ — every current proof consumes two.

## 7. Current Research (as of June 2026)

- **Mooney's school (UC Irvine)** continues the counterexample program: constructions of degenerate solutions with prescribed singular-set dimension, aimed at showing that the $\mathcal H^{n-1}$-null singular set theorem of the nondegenerate case has no degenerate analogue beyond $n=2$. *(frontier — verify)* Preprints circulating in 2025–26 claim degenerate examples with singular set of Hausdorff dimension arbitrarily close to $n-1$.
- **Nam Q. Le (Indiana)** develops the linearized Monge–Ampère theory with degenerate/singular weights, including Harnack and boundary Hölder estimates when $\det D^2u$ is only bounded above; his 2024 AMS graduate text consolidates the degenerate estimates.
- **Guan and collaborators (McGill)** pursue degenerate fully nonlinear Hessian equations $\sigma_k(D^2u)=f\ge0$, where the analogue of the $1/(n-1)$ exponent is $1/(k-1)$; progress there is expected to feed back into $k=n$.
- **Savin, Jhaveri, Le (Columbia / Cornell / Indiana)** work on boundary degeneracy — $f\ge0$ vanishing on $\partial\Omega$, relevant to the Wasserstein/optimal-transport boundary problem and to affine spheres.
- **Complex and geodesic side:** degenerate complex Monge–Ampère regularity (Chu–Tosatti–Weinkove's $C^{1,1}$ for geodesics in the space of Kähler metrics, and the Darvas–Lempert obstruction to $C^2$) informs the real problem through shared Pogorelov-type test functions.
- **Numerics:** monotone finite-difference and semi-Lagrangian schemes (Benamou–Froese–Oberman lineage) are used to probe conjectural moduli on degenerate examples; convergence rates degrade exactly at the conjectured thresholds. *(frontier — verify)*

## 8. Future Work

- Prove or disprove: $f^{1/(n-1)}\in C^{1,\alpha}$ with $\alpha<1$ implies $u\in C^{1,1}$. A single explicit counterexample at $\alpha$ close to $1$ would close the gap from below.
- Develop a *structure-sensitive* hypothesis: a condition on the pair $(f,\{f=0\})$ — e.g. $f^{1/(n-1)}$ semi-convex plus $\{f=0\}$ of codimension $\ge 2$ — under which full $C^{2,\alpha}$ or $C^\infty$ regularity holds. The Daskalopoulos–Savin point-degeneracy result suggests codimension is the operative parameter.
- Extend Mooney's partial-regularity theorem: is the non-strict-convexity set of a degenerate solution $\mathcal H^{n-2}$-rectifiable when $f^{1/(n-1)}$ is Lipschitz?
- Transfer techniques from the complex setting: adapt Chu–Tosatti–Weinkove's $C^{1,1}$ argument for degenerate complex Monge–Ampère to real degenerate data with a lower-order barrier.
- Sharp Sobolev thresholds: identify the critical vanishing rate separating $D^2u \in L^1_{loc}$ from Mooney's non-integrable examples, as a function of $n$.

## 9. Key References

- **[Foundational]** Caffarelli, L., Nirenberg, L., Spruck, J. *The Dirichlet problem for nonlinear second-order elliptic equations. I. Monge–Ampère equation.* Communications on Pure and Applied Mathematics, 37 (1984), 369–402.
- **[Foundational]** Caffarelli, L. *A localization property of viscosity solutions to the Monge–Ampère equation and their strict convexity.* Annals of Mathematics, 131 (1990), 129–134.
- **[Foundational]** Caffarelli, L. *Interior $W^{2,p}$ estimates for solutions of the Monge–Ampère equation.* Annals of Mathematics, 131 (1990), 135–150.
- **[Foundational]** Pogorelov, A. V. *The Minkowski Multidimensional Problem.* V. H. Winston & Sons / Wiley, 1978.
- **[Foundational]** Rauch, J., Taylor, B. A. *The Dirichlet problem for the multidimensional Monge–Ampère equation.* Rocky Mountain Journal of Mathematics, 7 (1977), 345–364.
- **[Key]** Hong, J., Zuily, C. *Existence of $C^\infty$ local solutions for the Monge–Ampère equation.* Inventiones Mathematicae, 89 (1987), 645–661.
- **[Key]** Wang, X.-J. *Some counterexamples to the regularity of Monge–Ampère equations.* Proceedings of the American Mathematical Society, 123 (1995), 841–845.
- **[Key]** Guan, P. *$C^2$ a priori estimates for degenerate Monge–Ampère equations.* Duke Mathematical Journal, 86 (1997), 323–346.
- **[SOTA]** Guan, P., Trudinger, N. S., Wang, X.-J. *On the Dirichlet problem for degenerate Monge–Ampère equations.* Acta Mathematica, 182 (1999), 87–104.
- **[SOTA]** Daskalopoulos, P., Savin, O. *On Monge–Ampère equations with homogeneous right-hand sides.* Communications on Pure and Applied Mathematics, 62 (2009), 639–676.
- **[SOTA]** De Philippis, G., Figalli, A. *$W^{2,1}$ regularity for solutions of the Monge–Ampère equation.* Inventiones Mathematicae, 192 (2013), 55–69.
- **[SOTA]** De Philippis, G., Figalli, A., Savin, O. *A note on interior $W^{2,1+\varepsilon}$ estimates for the Monge–Ampère equation.* Mathematische Annalen, 357 (2013), 11–22.
- **[SOTA]** Savin, O. *Pointwise $C^{2,\alpha}$ estimates at the boundary for the Monge–Ampère equation.* Journal of the American Mathematical Society, 26 (2013), 63–99.
- **[SOTA / Recent]** Mooney, C. *Partial regularity for singular solutions to the Monge–Ampère equation.* Communications on Pure and Applied Mathematics, 68 (2015), 1066–1084.
- **[SOTA / Recent]** Mooney, C. *Some counterexamples to Sobolev regularity for degenerate Monge–Ampère equations.* Analysis & PDE, 9 (2016), 881–891.
- **[Survey]** Trudinger, N. S., Wang, X.-J. *The Monge–Ampère equation and its geometric applications.* In *Handbook of Geometric Analysis, Vol. I*, International Press, 2008, 467–524.
- **[Survey / Book]** Figalli, A. *The Monge–Ampère Equation and Its Applications.* Zurich Lectures in Advanced Mathematics, European Mathematical Society, 2017.
- **[Survey / Book]** Le, N. Q. *Analysis of Monge–Ampère Equations.* Graduate Studies in Mathematics 240, American Mathematical Society, 2024.
- **[Book]** Gutiérrez, C. E. *The Monge–Ampère Equation.* 2nd edition, Birkhäuser, 2016.

## 10. Worked Example / Concrete Special Case

**Goal.** Derive the exponent $1/(n-1)$ from scratch and exhibit a solution that is exactly $C^{1,1}$ and not $C^2$.

Write $x = (x_1, x'')$ with $x'' \in \mathbb{R}^{n-1}$, and take the ansatz
$$u(x) \;=\; \tfrac12\,a(x_1)\,|x''|^2 \;+\; b(x_1),\qquad a \ge 0 .$$
The Hessian is the bordered block matrix
$$D^2u \;=\; \begin{pmatrix} \tfrac12 a''|x''|^2 + b'' & a'(x_1)\,(x'')^{T} \\[2pt] a'(x_1)\,x'' & a(x_1)\,I_{n-1}\end{pmatrix}.$$
By the Schur complement, for $a>0$,
$$\det D^2u \;=\; a^{n-1}\Big(\tfrac12 a''|x''|^2 + b''\Big) \;-\; a^{n-2}\,a'^2\,|x''|^2 .$$
On the axis $x''=0$ this reads
$$\boxed{\,f(x_1,0) \;=\; a(x_1)^{n-1}\,b''(x_1)\,}\qquad\Longrightarrow\qquad a \;=\; \Big(\frac{f}{b''}\Big)^{1/(n-1)} .$$
The Hessian eigenvalue in the $n-1$ flat directions is exactly $a \sim f^{1/(n-1)}$, and the off-diagonal entries are $a'x''$. Hence:

- $u \in C^{1,1}$ near $\{x_1=0\}$ $\iff$ $a$ and $a'$ are bounded $\iff$ $f^{1/(n-1)} \in C^{0,1}$;
- $u \in C^{2}$ $\iff$ $a'$ is continuous $\iff$ $f^{1/(n-1)} \in C^{1}$.

This is precisely why the hypothesis of Guan–Trudinger–Wang is stated for $f^{1/(n-1)}$ and not for $f$.

**Explicit non-$C^2$ solution ($n=2$).** Take $a(x_1)=|x_1|$, $b(x_1)=\tfrac{K}{2}x_1^2$ with $K>0$:
$$u(x_1,x_2) \;=\; \tfrac12 |x_1|\,x_2^{2} \;+\; \tfrac{K}{2}x_1^{2},\qquad
D^2u=\begin{pmatrix} K & \operatorname{sgn}(x_1)\,x_2\\ \operatorname{sgn}(x_1)\,x_2 & |x_1|\end{pmatrix}.$$
Then
$$f \;=\; \det D^2 u \;=\; K|x_1| - x_2^{2},$$
which is $\ge 0$ and vanishes exactly on the parabolas $x_2^2 = K|x_1|$ and on the segment $\{x_1=0,\,x_2=0\}$. On the region $\Omega_K = \{x_2^2 < K|x_1|\}\cap B_1$ (union the axis), $u$ is convex, solves $\det D^2u = f$ with $f \ge 0$ vanishing on $\partial$-degeneracy set, and
$$\|D^2u\|_{L^\infty(\Omega_K)} \le \max(K,1) < \infty, \qquad u_{12} = \operatorname{sgn}(x_1)x_2 \ \text{jumps across } \{x_1=0\}.$$
So $u \in C^{1,1}\setminus C^{2}$. Here $f^{1/(n-1)} = f = K|x_1|-x_2^2$ is Lipschitz but not $C^{1,1}$ across $\{x_1=0\}$ — the example sits exactly in the gap of Section 6 and shows that $C^{1,1}$ is the best possible conclusion.

**Contrast: point degeneracy is harmless.** In $\mathbb{R}^2$ with $f = |x|^\alpha$, homogeneity forces $\det D^2 u$ to be homogeneous of degree $2\beta-4$ if $u$ is homogeneous of degree $\beta$; matching gives $\beta = 2+\alpha/2$, so $u \sim |x|^{2+\alpha/2} h(\theta) \in C^{2,\alpha/2}$. The degeneracy set being a point rather than a curve changes the answer from "$C^{1,1}$, no better" to "$C^{2,\alpha/2}$" — the codimension effect that no existing norm-based hypothesis captures.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*