---
id: 06-pdes/ancient-mean-curvature-flow-codimension
title: "Rigidity of Ancient Solutions to the Mean Curvature Flow in Higher Codimension"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rigidity of Ancient Solutions to the Mean Curvature Flow in Higher Codimension

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/ancient-mean-curvature-flow-codimension` · **Status:** open

## 1. Problem Statement / Conjecture

Let $F:M^n\times I\to\mathbb{R}^{n+m}$, $m\ge 2$, be a smooth family of immersions of a closed $n$-manifold solving mean curvature flow (MCF)
$$\partial_t F(p,t)=\vec{H}(p,t),$$
where $\vec H$ is the mean curvature vector. The solution is **ancient** if $I=(-\infty,T)$.

**Conjecture (rigidity of pinched ancient solutions).** *Let $n\ge 2$, $m\ge 1$, and let $F$ be a closed ancient solution of MCF in $\mathbb{R}^{n+m}$ with $\vec H\neq 0$ satisfying the quadratic pinching*
$$|A|^2\le c\,|H|^2 \quad\text{on } M\times(-\infty,T),\qquad c<\tfrac{1}{n-1}.$$
*Then $M_t$ is a family of shrinking round spheres $S^n\!\big(\sqrt{-2nt}\big)$ contained in a fixed $(n+1)$-dimensional affine subspace of $\mathbb{R}^{n+m}$.*

Three strengthenings are jointly regarded as the open problem:

1. **Sharp constant.** The result is known only for $c\le c_n$ with $c_n=\frac{4}{3n}$ ($n\ge4$), $c_n=\frac{3(n+1)}{2n(n+2)}$ ($n=2,3$) — the Andrews–Baker constants. Pushing to the conjecturally optimal threshold $\frac{1}{n-1}$ (attained by shrinking cylinders and, for $n=2$, by the Clifford torus) is open.
2. **Noncompact case.** Classify complete noncompact ancient solutions in $\mathbb{R}^{n+m}$ with bounded pinched curvature. No higher-codimension analogue of the Brendle–Choi bowl-soliton uniqueness theorem exists.
3. **Removing pinching.** Replace the pointwise pinching by a scale-invariant hypothesis (bounded entropy, noncollapsing, or $|A|^2\le C|H|^2$ with $C$ arbitrary plus $\vec H \neq 0$).

A complete solution is a proof of the conjecture with the stated constant, or a counterexample: an eternal or ancient pinched solution in codimension $\ge 2$ that is not a shrinking sphere.

## 2. Mathematical Foundations

Let $A$ be the second fundamental form, a section of $T^*M\otimes T^*M\otimes NM$, with components $h^\alpha_{ij}=\langle \bar\nabla_{e_i}e_j,\nu_\alpha\rangle$ in a local frame $\{e_i\}$ of $TM$ and $\{\nu_\alpha\}$ of the normal bundle $NM$. Then $H^\alpha=g^{ij}h^\alpha_{ij}$, $|H|^2=\sum_\alpha (H^\alpha)^2$, $|A|^2=\sum_\alpha g^{ik}g^{jl}h^\alpha_{ij}h^\alpha_{kl}$, and the trace-free part is
$$\mathring A = A-\tfrac1n\, g\otimes \vec H,\qquad |\mathring A|^2=|A|^2-\tfrac1n|H|^2\ \ge 0 .$$

Under MCF (Andrews–Baker, following Huisken and Simons):
$$\partial_t |H|^2=\Delta|H|^2-2|\nabla H|^2+2\sum_{i,j}\Big(\sum_\alpha H^\alpha h^\alpha_{ij}\Big)^{\!2},$$
$$\partial_t |A|^2=\Delta|A|^2-2|\nabla A|^2+2R_1+2R_2,$$
$$R_1=\sum_{\alpha,\beta}\Big(\sum_{i,j}h^\alpha_{ij}h^\beta_{ij}\Big)^{\!2}+\sum_{i,j,\alpha,\beta}\Big(\sum_p h^\alpha_{ip}h^\beta_{pj}-h^\alpha_{jp}h^\beta_{pi}\Big)^{\!2},\qquad
R_2=\sum_{\alpha,\beta,i,j,p}H^\alpha h^\beta_{ij}h^\alpha_{ip}h^\beta_{pj}.$$
The second sum in $R_1$ is $|R^\perp|^2$, the squared norm of the **normal curvature**; it vanishes identically in codimension one and is the source of every genuinely higher-codimension difficulty.

For $c\le c_n$ the set $\{|A|^2\le c|H|^2,\ \vec H\ne0\}$ is preserved: the reaction terms obey
$$R_1+R_2-c\,\Big|\!\sum_\alpha H^\alpha h^\alpha_{ij}\Big|^2_{\text{tr}}\le \big(c-\tfrac1n\big)^{-1}\text{-controlled terms},$$
which is the algebraic core of Andrews–Baker (2010). **Codimension splitting:** write $\omega=\vec H/|H|$, $h^{\,H}_{ij}=\langle A_{ij},\omega\rangle$, and $A^-=A-\omega\otimes h^H$, so $|A|^2=|h^H|^2+|A^-|^2$. A submanifold lies in an $(n+1)$-plane (locally) iff $A^-\equiv0$ and the normal connection restricted to $\mathrm{span}(\omega)$ is flat.

**Ancient solutions** arise as blow-up limits at singularities: rescaling $F_\lambda(p,t)=\lambda\big(F(p,t_0+\lambda^{-2}t)-x_0\big)$ and letting $\lambda\to\infty$ produces, along subsequences, an ancient solution. Rigidity of ancient solutions is therefore equivalent to a classification of singularity models.

## 3. History & State of the Art (SOTA)

- **1984.** Huisken proves closed convex hypersurfaces in $\mathbb{R}^{n+1}$ shrink to round points — the codimension-one template.
- **1994–1999.** Hamilton's Harnack inequality for MCF (1995) and the differential-Harnack technique become the standard tool for extracting rigidity from ancient solutions; Hamilton's isoperimetric-type arguments classify ancient curve-shortening flows in part.
- **2010.** Andrews & Baker prove: closed $M^n\subset\mathbb{R}^{n+m}$ with $|A|^2\le c_n|H|^2$ contracts to a round point. This makes quadratic pinching the working substitute for convexity in higher codimension.
- **2015.** Huisken & Sinestrari classify closed convex uniformly two-convex ancient solutions in $\mathbb{R}^{n+1}$ as shrinking spheres, under a variety of equivalent normalizations (e.g. bounded diameter ratio, or backwards $|A|^2/|H|^2\to1/n$).
- **2019.** Risa & Sinestrari extend ancient-solution rigidity to pinched flows of higher-codimension submanifolds of spheres and to related geometric flows.
- **2019–2021.** Naff proves **codimension estimates** for pinched MCF: for every $\varepsilon>0$ there is $C_\varepsilon$ with $|A^-|^2\le\varepsilon|H|^2+C_\varepsilon$, so blow-up limits of pinched flows are codimension-one. This is the structural breakthrough that makes hypersurface machinery partly available.
- **2021.** Lynch & Nguyen prove the conjecture as stated in §1 for $c\le c_n$ (Andrews–Baker range): every closed pinched ancient solution in $\mathbb{R}^{n+m}$ is a shrinking sphere in an $(n+1)$-plane.
- **Codimension one comparison.** Angenent–Daskalopoulos–Sesum (Annals 2020) classify closed two-convex ancient solutions (spheres and ancient ovals); Brendle–Choi classify noncompact convex ancient solutions (bowl solitons) in $\mathbb{R}^3$ and $\mathbb{R}^{n+1}$. No analogue is known for $m\ge2$.

## 4. Partial Results / Verified Cases

| Setting | Hypothesis | Conclusion | Source |
|---|---|---|---|
| $\mathbb{R}^{n+m}$, closed, $n\ge2$ | $|A|^2\le c_n|H|^2$, $c_n=\frac{4}{3n}$ ($n\ge4$), $\frac{3(n+1)}{2n(n+2)}$ ($n=2,3$) | shrinking round sphere in an $(n+1)$-plane | Lynch–Nguyen 2021 |
| $S^{n+m}$, closed, pinched | $|A|^2\le\frac{1}{n-1}|H|^2+\text{const}$-type pinching | shrinking geodesic sphere or totally geodesic $S^n$ | Risa–Sinestrari 2019 |
| $\mathbb{R}^{n+1}$ (codim 1), closed | convex + uniformly two-convex | shrinking sphere; with noncompact ends, ancient ovals | Huisken–Sinestrari 2015; ADS 2020 |
| $\mathbb{R}^{n+1}$, noncompact | convex, noncollapsed, eternal | bowl soliton | Brendle–Choi 2019, 2021 |
| Curves, $n=1$ | convex ancient CSF in $\mathbb{R}^2$ / $S^2$ | shrinking circle, Angenent oval, equator | Daskalopoulos–Hamilton–Šešum 2010; Bryan–Louie 2016 |
| Any $n,m$ | $|A|^2\le\frac{1}{n}|H|^2+\delta$ with $\delta$ small (near-umbilic) | sphere, by rigidity of $\mathring A=0$ | elementary from §2 |

Also known: closed pinched ancient solutions have backward limits with $|\mathring A|^2/|H|^2\to0$, and their entropy is bounded by that of $S^n$; the type-I blow-up limits of any pinched MCF are shrinking spheres or generalized cylinders lying in an $(n+1)$-plane (Naff).

## 5. Principal Obstacles

- **No maximum principle for convexity.** In codimension $\ge2$ there is no scalar "convexity". The natural substitute — pinching $|A|^2\le c|H|^2$ — is preserved only up to $c_n$, and $c_n$ is dictated by the algebraic inequality controlling $R_1+R_2$, not by geometry. The gap between $c_n$ and $\frac1{n-1}$ is a defect of the algebra, not of the flow.
- **Normal curvature obstruction.** The term $|R^\perp|^2$ in $R_1$ has the wrong sign for pinching arguments: it pushes $|A|^2$ up. Any argument that discards it loses exactly the borderline cases (e.g. the Clifford torus, where $R^\perp\neq0$).
- **No Harnack inequality.** Hamilton's differential Harnack estimate for MCF requires a positive-definite second fundamental form in a single normal direction; there is no known higher-codimension version. Harnack is the engine of every codimension-one eternal-solution rigidity proof (eternal + Harnack + equality case $\Rightarrow$ translator).
- **Noncollapsing fails.** Andrews' inscribed/exscribed ball noncollapsing has no meaning for $m\ge2$ (no separating hypersurface, no inside). Consequently Haslhofer–Kleiner and White-type structure theory is unavailable.
- **Loss of compactness at infinity.** For noncompact ancient solutions the pinching $|A|^2\le c|H|^2$ does not by itself bound $|A|$; without noncollapsing there is no local curvature estimate to run a blow-down.
- **Backward asymptotics.** The proofs in the compact case rely on showing $|\mathring A|\to0$ as $t\to-\infty$ via a Poincaré-type inequality on the rescaled flow. Without an a priori diameter bound the rescaled flow can lose compactness, and the ODE comparison degenerates.

## 6. The Gap

The proven statement is: *closed* ancient solutions with $|A|^2\le c_n|H|^2$ are shrinking spheres. The conjecture is: *closed* ancient solutions with $|A|^2\le c|H|^2$ for any $c<\frac1{n-1}$ are shrinking spheres, plus a classification in the noncompact case.

The exact barrier is threefold:

1. **Preservation.** Show $\{|A|^2\le c|H|^2\}$ is preserved for all $c<\frac1{n-1}$ — this requires a strictly better estimate on $R_1+R_2$ than the Andrews–Baker Cauchy–Schwarz argument, in the presence of nonzero normal curvature. For $n\ge5$ it is not known whether preservation even holds at $c=\frac1{n-1}$.
2. **Codimension reduction with sharp constants.** Naff's estimate $|A^-|^2\le\varepsilon|H|^2+C_\varepsilon$ is proved inside the Andrews–Baker range using the same algebra; extending it to the sharp range is a coupled problem.
3. **Replacing Harnack.** Even granted (1) and (2), the noncompact case needs an eternal-solution rigidity mechanism. In codimension one this is Harnack plus noncollapsing; both inputs are missing for $m\ge2$.

## 7. Current Research (as of June 2026)

- **Lynch–Nguyen programme (Tübingen / Queen Mary London).** High-codimension MCF with surgery, cylindrical and convexity estimates for pinched flows; the ancient rigidity theorem is a corollary of the same estimates. Continuing work targets surgery beyond the $c_n$ threshold.
- **Naff (Princeton / MIT circle).** Codimension estimates and classification of singularity models of pinched flows; extension to ancient solutions in spheres and to Ricci-flow analogues. *(frontier — verify)* Ongoing attempts to prove a Harnack-type estimate for the scalar $|H|$ under pinching.
- **Risa–Sinestrari (Rome Tor Vergata).** Ancient solutions of geometric flows in space forms; rigidity under pinching in $S^{n+m}$ and $\mathbb{H}^{n+m}$.
- **Lei–Xu and collaborators (Zhejiang).** Sharp differentiable-sphere-theorem style pinching constants for MCF of arbitrary codimension, with claimed improvements towards $\frac1{n-1}$ for large $n$. *(frontier — verify)*
- **Brendle–Choi–Daskalopoulos–Sesum school.** Codimension-one ancient classification (ovals, bowls) as the model to be transplanted; the ancient-oval uniqueness proof's Poincaré-inequality method is the main candidate for import.
- **Lagrangian and symplectic MCF (Neves, Wood, Su).** Ancient solutions with the Lagrangian condition — a natural higher-codimension class where the normal bundle is identified with $T^*M$, giving extra structure not available in general.

## 8. Future Work

- Determine the *optimal* preservation constant $c^*_n$ for $\{|A|^2\le c|H|^2\}$ under MCF in codimension $\ge2$; decide whether $c^*_n=\frac1{n-1}$ or is strictly smaller for some $n$.
- Construct a higher-codimension Harnack inequality, e.g. for the scalar $|H|$ under the hypothesis $\nabla^\perp \omega=0$ (parallel mean curvature direction), where the normal bundle splits.
- Classify ancient solutions with **parallel mean curvature vector**, a tractable subclass containing all higher-codimension self-shrinkers of product type.
- Prove or refute existence of an ancient solution in $\mathbb{R}^{4}$ ($n=2$, $m=2$) with $|A|^2/|H|^2\to1$ backward in time and not a sphere — the Clifford-torus borderline.
- Replace pinching with entropy: show that closed ancient solutions in $\mathbb{R}^{n+m}$ with $\lambda(M_t)\le\lambda(S^{n-1}\times\mathbb{R})$ are spheres, an Ilmanen-type entropy programme in higher codimension.
- Develop a Lagrangian analogue: classify ancient Lagrangian MCF in $\mathbb{C}^n$ with almost-calibrated condition.

## 9. Key References

- **[Foundational]** G. Huisken. *Flow by mean curvature of convex surfaces into spheres.* Journal of Differential Geometry 20 (1984), 237–266.
- **[Foundational]** R. S. Hamilton. *Harnack estimate for the mean curvature flow.* Journal of Differential Geometry 41 (1995), 215–226.
- **[Foundational]** B. Andrews, C. Baker. *Mean curvature flow of pinched submanifolds to spheres.* Journal of Differential Geometry 85 (2010), 357–395.
- **[Foundational]** C. Baker. *The mean curvature flow of submanifolds of high codimension.* PhD thesis, Australian National University, 2010 (arXiv:1104.4409).
- **[Foundational]** M.-T. Wang. *Long-time existence and convergence of graphic mean curvature flow in arbitrary codimension.* Inventiones Mathematicae 148 (2002), 525–543.
- **[SOTA / Recent]** S. Lynch, H. T. Nguyen. *Pinched ancient solutions to the high codimension mean curvature flow.* Calculus of Variations and Partial Differential Equations 60 (2021), Paper No. 29.
- **[SOTA / Recent]** K. Naff. *Codimension estimates in mean curvature flow.* arXiv:1906.03340 (2019).
- **[SOTA / Recent]** S. Risa, C. Sinestrari. *Ancient solutions of geometric flows with curvature pinching.* Journal of Geometric Analysis 29 (2019), 1206–1232.
- **[SOTA / Recent]** G. Huisken, C. Sinestrari. *Convex ancient solutions of the mean curvature flow.* Journal of Differential Geometry 101 (2015), 267–287.
- **[SOTA / Recent]** S. Angenent, P. Daskalopoulos, N. Sesum. *Uniqueness of two-convex closed ancient solutions to the mean curvature flow.* Annals of Mathematics (2) 192 (2020), 353–436.
- **[SOTA / Recent]** S. Brendle, K. Choi. *Uniqueness of convex ancient solutions to mean curvature flow in $\mathbb{R}^3$.* Inventiones Mathematicae 217 (2019), 35–76.
- **[SOTA / Recent]** P. Bryan, J. Louie. *Classification of convex ancient solutions to curve shortening flow on the sphere.* Journal of Geometric Analysis 26 (2016), 858–872.
- **[Survey]** C. Mantegazza. *Lecture Notes on Mean Curvature Flow.* Progress in Mathematics 290, Birkhäuser, 2011.
- **[Survey]** R. Haslhofer. *Lectures on curve shortening flow* / K. Ecker. *Regularity Theory for Mean Curvature Flow.* Progress in Nonlinear Differential Equations 57, Birkhäuser, 2004.

## 10. Worked Example / Concrete Special Case

**The Clifford torus in $\mathbb{R}^4$: why $c=\frac1{n-1}$ is the natural threshold ($n=2$, $m=2$).**

Take $M=S^1(r_1)\times S^1(r_2)\subset\mathbb{R}^2\times\mathbb{R}^2=\mathbb{R}^4$. Its normal bundle is spanned by the outward radial fields $\nu_1,\nu_2$ of the two factors. In the frame $e_1$ tangent to the first circle, $e_2$ to the second:
$$h^1_{11}=\tfrac1{r_1},\quad h^2_{22}=\tfrac1{r_2},\quad\text{all other } h^\alpha_{ij}=0 .$$
Hence
$$\vec H=-\tfrac1{r_1}\nu_1-\tfrac1{r_2}\nu_2,\qquad |H|^2=\tfrac1{r_1^2}+\tfrac1{r_2^2},\qquad |A|^2=\tfrac1{r_1^2}+\tfrac1{r_2^2}.$$
So **$|A|^2=|H|^2$ for every $r_1,r_2$**, i.e. exactly the borderline $|A|^2=\frac{1}{n-1}|H|^2$ with $n=2$.

Under MCF each factor shrinks independently: $\dot r_i=-1/r_i$, so $r_i(t)^2=r_i(0)^2-2t$. With $r_1(0)=r_2(0)=\sqrt{2}$ we get the self-shrinking Clifford torus
$$M_t=S^1(\sqrt{-2t})\times S^1(\sqrt{-2t}),\qquad t\in(-\infty,0),$$
a genuinely **ancient, closed, codimension-two solution with $\vec H\neq0$** that is *not* a shrinking sphere and does not lie in any $3$-plane. It satisfies $|A|^2\le c|H|^2$ with $c=1$, and $1=\frac1{n-1}$ for $n=2$. So the conjecture in §1 is sharp: the strict inequality $c<\frac1{n-1}$ cannot be relaxed to $\le$.

**Contrast with the sphere.** For $S^n(\sqrt{-2nt})\subset\mathbb{R}^{n+1}\subset\mathbb{R}^{n+m}$ we have $h_{ij}=\frac1r g_{ij}$, so $|H|^2=n^2/r^2$ and $|A|^2=n/r^2$, giving $|A|^2=\frac1n|H|^2$ — the minimum possible value, and $\mathring A\equiv0$.

**Where the two are separated.** Compute $R_1$ for the torus. The first sum gives $\big(\sum_{ij}h^1_{ij}h^1_{ij}\big)^2+\big(\sum h^2 h^2\big)^2=r_1^{-4}+r_2^{-4}$; the cross terms $\sum_{ij}h^1_{ij}h^2_{ij}=0$. The normal-curvature term $\sum_{ij\alpha\beta}\big(\sum_p h^\alpha_{ip}h^\beta_{pj}-h^\alpha_{jp}h^\beta_{pi}\big)^2$ also vanishes here ($R^\perp=0$ for a flat product torus). Meanwhile $R_2=\sum H^\alpha h^\beta_{ij}h^\alpha_{ip}h^\beta_{pj}=r_1^{-4}+r_2^{-4}$. The evolution of $Q_c=|A|^2-c|H|^2$ then has reaction term $2(R_1+R_2)-2c\sum_{ij}\big(\sum_\alpha H^\alpha h^\alpha_{ij}\big)^2 = 4(r_1^{-4}+r_2^{-4})-2c(r_1^{-4}+r_2^{-4})$, strictly positive for $c<2$. At $c=1$, $Q_1\equiv0$ is preserved only because the gradient and Laplacian terms vanish identically on this homogeneous example — the equality case is exactly the degeneracy the conjecture must rule out for $c$ slightly below $1$. Showing that no *nearby* ancient solution with $c<1$ exists, for all $n$ and $m$, is the content of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*