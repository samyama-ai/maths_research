---
id: 06-pdes/ancient-ricci-flow-classification
title: "Rigidity of Ancient Solutions to the Ricci Flow in Higher Dimensions"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rigidity of Ancient Solutions to the Ricci Flow in Higher Dimensions

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/ancient-ricci-flow-classification` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

An **ancient solution** to the Ricci flow is a smooth family of complete metrics $(M^n, g(t))$, $t \in (-\infty, 0)$, with $\partial_t g = -2\,\mathrm{Ric}(g)$, defined for all sufficiently negative time. Perelman's $\kappa$-solutions — ancient, $\kappa$-noncollapsed, bounded curvature, nonnegative curvature operator — are exactly the models for finite-time singularities, so classifying them classifies the singularities.

**Conjecture (higher-dimensional $\kappa$-solution rigidity).** Let $(M^n, g(t))_{t \in (-\infty,0)}$, $n \ge 4$, be a complete, non-flat, $\kappa$-noncollapsed ancient solution with bounded curvature which is *uniformly PIC* and *weakly PIC2*. Then $(M,g(t))$ is, up to scaling and isometry, one of:

1. a quotient of the shrinking round sphere $S^n$;
2. a quotient of the shrinking round cylinder $S^{n-1} \times \mathbb{R}$;
3. the **Bryant soliton** (rotationally symmetric steady gradient soliton on $\mathbb{R}^n$);
4. the **ancient oval**: a compact, rotationally symmetric, non-soliton ancient solution that emerges from a pair of Bryant tips and converges to the round sphere as $t \to 0$.

A complete resolution means a proof of this list under the stated curvature hypotheses in every $n \ge 4$, or a counterexample: a $\kappa$-noncollapsed ancient solution in the class that is not on the list. Weakening the curvature hypotheses to bare nonnegative curvature operator is a separate, strictly harder question, and is **false as stated** without further conditions once one allows Kähler examples and products.

## 2. Mathematical Foundations

**Ricci flow.** For $g(t)$ on $M^n$,
$$\frac{\partial}{\partial t} g_{ij} = -2 R_{ij}, \qquad \partial_t R = \Delta R + 2|\mathrm{Ric}|^2 .$$
Under Uhlenbeck's frame, the curvature operator $\mathrm{Rm}: \Lambda^2 \to \Lambda^2$ satisfies Hamilton's reaction–diffusion equation
$$\partial_t \mathrm{Rm} = \Delta\,\mathrm{Rm} + \mathrm{Rm}^2 + \mathrm{Rm}^{\\#},$$
so any closed convex $O(n)$-invariant cone preserved by the ODE $\frac{d}{dt}S = S^2 + S^{\\#}$ is preserved by the flow (Hamilton's maximum principle for systems).

**Curvature conditions.** $(M,g)$ has *positive isotropic curvature* (PIC) if for all orthonormal $e_1,e_2,e_3,e_4$,
$$R_{1313} + R_{1414} + R_{2323} + R_{2424} - 2R_{1234} > 0 .$$
*PIC2* means $M \times \mathbb{R}^2$ has PIC; *uniformly PIC* means the above exceeds $\theta R$ for a fixed $\theta > 0$. PIC2 $\Rightarrow$ nonnegative sectional curvature; nonnegative curvature operator $\Rightarrow$ weakly PIC2.

**$\kappa$-noncollapsing.** $g(t)$ is $\kappa$-noncollapsed on all scales if $|\mathrm{Rm}| \le r^{-2}$ on $B(p,r)$ implies $\mathrm{vol}\,B(p,r) \ge \kappa r^n$. Perelman's monotonicity of the $\mathcal{W}$-entropy
$$\mathcal{W}(g,f,\tau)=\int_M \big[\tau(R+|\nabla f|^2)+f-n\big](4\pi\tau)^{-n/2}e^{-f}\,d\mu$$
forces this along smooth flows from closed initial data.

**Solitons.** $\mathrm{Ric} + \nabla^2 f = \tfrac{\lambda}{2} g$ gives shrinking ($\lambda>0$), steady ($\lambda=0$), expanding ($\lambda<0$) gradient solitons; the first two are ancient. The **Bryant soliton** is the unique complete rotationally symmetric steady gradient soliton on $\mathbb{R}^n$, with $R \sim c/r$ and volume growth $r^{(n+1)/2}$.

**Model solutions.** The shrinking cylinder is
$$g(t) = 2(n-2)|t|\, g_{S^{n-1}} + dx^2, \qquad t<0,$$
and the round sphere is $g(t) = 2(n-1)|t| \, g_{S^n}$.

**Asymptotic shrinker.** Perelman's reduced volume gives every $\kappa$-solution a nontrivial gradient shrinking soliton as a blow-down limit $\lim_{t \to -\infty} (M, |t|^{-1}g(t))$ (possibly after passing to a subsequence and non-uniquely). Rigidity proofs proceed by (i) identifying that shrinker as a cylinder or sphere, (ii) upgrading the asymptotics to exact rotational symmetry, (iii) ODE-classifying the rotationally symmetric solutions.

## 3. History & State of the Art (SOTA)

- **1982.** Hamilton introduces Ricci flow; ancient solutions appear as the natural rescaling limits of singularities.
- **1990s.** Hamilton develops the singularity-classification program: Type I / Type II, the "cigar" $\left(\mathbb{R}^2, \frac{dx^2+dy^2}{1+x^2+y^2}\right)$ as an obstruction, Harnack inequalities.
- **2002–03.** Perelman: $\mathcal{W}$-entropy, no local collapsing (which rules out the collapsed cigar as a 3D blow-up limit), the canonical neighbourhood theorem, and the compactness of the space of 3D $\kappa$-solutions. Full 3D classification is left open.
- **2012.** Daskalopoulos–Hamilton–Sesum classify compact ancient solutions on surfaces: only the round shrinking $S^2$ and the King–Rosenau solution.
- **2019–2021.** Brendle proves the noncompact 3D case (Bryant soliton is the only non-cylindrical one); Bamler–Kleiner give an independent rotational-symmetry proof; Brendle–Daskalopoulos–Sesum settle the compact 3D case (round $S^3$ or the Perelman oval).
- **2023.** Brendle–Daskalopoulos–Naff–Sesum extend the **compact** classification to all $n \ge 4$ under uniformly PIC + weakly PIC2.
- **Present.** The **noncompact** higher-dimensional case, and dimension 4 without the PIC-type hypotheses, remain open.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n=2$, compact | Round $S^2$ or King–Rosenau | Daskalopoulos–Hamilton–Sesum 2012 |
| $n=3$, noncompact $\kappa$-solution | $S^2\times\mathbb{R}$ (or quotient) or Bryant | Brendle, *Acta Math.* 2020 |
| $n=3$, compact ancient, $\kappa$-noncollapsed | Round $S^3$/quotient or Perelman oval | Brendle–Daskalopoulos–Sesum 2021 |
| $n\ge4$, **compact**, uniformly PIC + weakly PIC2 | Round $S^n$/quotient or higher-dim oval | Brendle–Daskalopoulos–Naff–Sesum 2023 |
| Any $n$, steady gradient soliton, PIC + asymptotically cylindrical | Bryant soliton | Brendle, *JDG* 2014 |
| Any $n$, Type I compact ancient with positive curvature operator | Round sphere | Ni 2010 |
| Any $n$, shrinking soliton with nonneg. curvature operator, asymptotically cylindrical end | Round cylinder (rigidity) | Li–Wang, arXiv 2021 |
| $n\ge 12$, PIC, no ancient-solution input | Surgery classification of PIC manifolds | Brendle, *Ann. of Math.* 2019 |

Additionally: any $\kappa$-solution with $\mathrm{Rm} \ge 0$ and a **compact** asymptotic shrinker is compact; any noncompact $\kappa$-solution with positive curvature operator and Euclidean volume growth is flat (Perelman's argument via reduced volume).

## 5. Principal Obstacles

- **No compactness in the noncompact case.** The compact classification uses the fact that a compact ancient solution has a *unique* backward limit and finite diameter/curvature ratios, allowing the Angenent–Daskalopoulos–Sesum "unique asymptotics" scheme. Noncompact solutions have an infinite neck of unknown geometry and the tip may escape any fixed ball, so no uniform scale exists on which to run a spectral decomposition.
- **The neck-analysis machinery is codimension-dependent.** Brendle's 3D proof exploits that a 3D neck has cross-section $S^2$, whose Lie algebra of Killing fields is $\mathfrak{so}(3)$ and whose linearized-operator kernel is exactly $3+3$-dimensional. For $S^{n-1}$, $n \ge 4$, the space of neutral and unstable modes of the linearization grows, and the extra modes correspond to genuine deformations (e.g. non-round Einstein cross-sections) that must be excluded by curvature hypotheses rather than by dimension count.
- **PIC2 is used non-removably.** Weakly PIC2 rules out non-round Einstein or Kähler cross-sections. Without it, the Feldman–Ilmanen–Knopf shrinking Kähler solitons on line bundles over $\mathbb{CP}^{n-1}$ and products such as $S^2 \times S^2$-type shrinkers give ancient solutions that are not on the list; whether the correct list in dimension 4 with only $\mathrm{Rm}\ge 0$ is finite is not known.
- **Collapsed examples exist.** Yi Lai's flying-wing steady solitons (2024) show that dropping $\kappa$-noncollapsing produces continuous families of non-rotationally-symmetric ancient solutions already in dimension 3, so any proof must consume the noncollapsing hypothesis quantitatively, not merely qualitatively.
- **Uniqueness of the asymptotic shrinker is not known in general.** Perelman's blow-down argument yields a shrinker only along subsequences. Without uniqueness the "cap plus neck" decomposition may not be time-independent.

## 6. The Gap

Everything proven in Section 4 for $n \ge 4$ is either **compact** or **soliton-a-priori**. The exact missing step:

> Show that a noncompact, uniformly PIC, weakly PIC2 $\kappa$-solution in dimension $n \ge 4$ whose asymptotic shrinker is the cylinder $S^{n-1}\times\mathbb{R}$ is **rotationally symmetric**.

Once rotational symmetry is available, the flow reduces to a scalar quasilinear parabolic equation for the warping function and Brendle's 2014 soliton-uniqueness argument closes the case. The obstruction is producing the $\binom{n}{2}$ approximate Killing fields on the neck, solving the associated linear elliptic system for exact Killing fields on the cap region, and showing the error decays through the (now larger) unstable spectrum. In 3D this decay is proved by a delicate Carleman-type estimate on the parabolic cylinder; the $n$-dimensional analogue has been announced only under additional symmetry or additional pinching.

## 7. Current Research (as of June 2026)

- **Columbia / Brendle's school.** Extension of the compact $n\ge 4$ classification to noncompact ancient solutions with uniformly PIC; Naff's cylindrical and pinching estimates for high-dimensional necks are the technical engine. *(frontier — verify)*
- **Bamler's structure theory.** The $\mathbb{F}$-convergence and compactness theory for Ricci flows (Invent. Math. 2023) gives singular-space limits and codimension-4 partial regularity; groups at Berkeley are using it to constrain the possible asymptotic shrinkers of 4D $\kappa$-solutions without PIC hypotheses. *(frontier — verify)*
- **Kähler-Ricci ancient solutions.** Classification of $\kappa$-noncollapsed ancient solutions in the Kähler category (nonnegative bisectional curvature) is more tractable; complex-dimension-2 progress is being pursued as a testing ground for the real 4D case. *(frontier — verify)*
- **Collapsed / low-symmetry solitons.** Following Lai, the classification of 3D steady solitons with $O(2)$ symmetry and the moduli of flying wings clarify exactly which hypotheses in the conjecture are indispensable.

## 8. Future Work

1. **Prove rotational symmetry in the noncompact higher-dimensional case** via a neck-improvement argument robust to $\dim S^{n-1} \ge 3$: the key is a Carleman inequality on $\mathbb{R} \times S^{n-1}$ uniform in $n$.
2. **Remove uniform PIC in dimension 4**, replacing it by $\mathrm{Rm} \ge 0$ plus $\kappa$-noncollapsing, and produce the correct (possibly longer) list including Kähler models.
3. **Uniqueness of asymptotic shrinkers** for $\kappa$-solutions with $\mathrm{Rm} \ge 0$: an entropy-gap or Łojasiewicz-inequality approach at the cylinder.
4. **Classify ancient solutions of bounded but sign-changing curvature** in dimension 4, relevant to Ricci flow with surgery on 4-manifolds.
5. **Quantitative canonical neighbourhoods**: turn the classification into effective curvature-scale estimates usable in a surgery construction for $n \ge 5$.

## 9. Key References

- **[Foundational]** R. S. Hamilton. *Three-manifolds with positive Ricci curvature.* J. Differential Geom. 17 (1982), 255–306.
- **[Foundational]** G. Perelman. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:math/0211159, 2002.
- **[Foundational]** B. Chow, P. Lu, L. Ni. *Hamilton's Ricci Flow.* Graduate Studies in Mathematics 77, AMS, 2006.
- **[SOTA]** S. Brendle. *Ancient solutions to the Ricci flow in dimension 3.* Acta Math. 225 (2020), 1–102.
- **[SOTA]** S. Brendle, P. Daskalopoulos, N. Sesum. *Uniqueness of compact ancient solutions to three-dimensional Ricci flow.* Invent. Math. 226 (2021), 579–651.
- **[SOTA]** S. Brendle, P. Daskalopoulos, K. Naff, N. Sesum. *Uniqueness of compact ancient solutions to the higher-dimensional Ricci flow.* J. reine angew. Math. (Crelle) 795 (2023), 85–138.
- **[SOTA]** S. Brendle. *Rotational symmetry of Ricci solitons in higher dimensions.* J. Differential Geom. 97 (2014), 191–214.
- **[SOTA]** S. Brendle. *Ricci flow with surgery on manifolds with positive isotropic curvature.* Ann. of Math. 190 (2019), 465–559.
- **[SOTA]** R. Bamler, B. Kleiner. *On the rotational symmetry of 3-dimensional $\kappa$-solutions.* J. reine angew. Math. 765 (2020), 233–248.
- **[SOTA]** R. Bamler. *Compactness theory of the space of super Ricci flows.* Invent. Math. 233 (2023), 1121–1277.
- **[SOTA]** Y. Lai. *A family of 3-dimensional steady gradient Ricci solitons that are flying wings.* J. Differential Geom. 126 (2024).
- **[Related]** P. Daskalopoulos, R. Hamilton, N. Sesum. *Classification of ancient compact solutions to the Ricci flow on surfaces.* J. Differential Geom. 91 (2012), 171–214.
- **[Related]** S. Angenent, P. Daskalopoulos, N. Sesum. *Uniqueness of two-convex closed ancient solutions to the mean curvature flow.* Ann. of Math. 192 (2020), 353–436.
- **[Related]** M. Feldman, T. Ilmanen, D. Knopf. *Rotationally symmetric shrinking and expanding gradient Kähler-Ricci solitons.* J. Differential Geom. 65 (2003), 169–209.
- **[Survey]** J. Morgan, G. Tian. *Ricci Flow and the Poincaré Conjecture.* Clay Mathematics Monographs 3, AMS, 2007.

## 10. Worked Example / Concrete Special Case

**The shrinking cylinder and its neck spectrum in $\mathbb{R} \times S^{n-1}$.**

Take $g(t) = r(t)^2 g_{S^{n-1}} + dx^2$ on $\mathbb{R}\times S^{n-1}$. The round $S^{n-1}$ of radius $r$ has $\mathrm{Ric} = \frac{n-2}{r^2}\, (r^2 g_{S^{n-1}})$, and the flat $\mathbb{R}$ factor contributes nothing. So Ricci flow reduces to the ODE
$$\frac{d}{dt}\big(r^2\big) = -2(n-2) \quad \Longrightarrow \quad r(t)^2 = 2(n-2)|t|,$$
giving the ancient solution $g(t) = 2(n-2)|t|\,g_{S^{n-1}} + dx^2$, $t<0$, which is $\kappa$-noncollapsed with $\kappa$ depending only on $n$, has $\mathrm{Rm}\ge 0$ and is weakly PIC2, and satisfies $R = \frac{(n-1)(n-2)}{r^2} = \frac{n-1}{2|t|}$. It is a shrinking soliton with $f = x^2/(4|t|)$ up to constants.

**Linearized stability.** Rescale by $\tilde g = |t|^{-1} g$, $\tau = -\log|t|$, and perturb the neck radius: $r^2 = 2(n-2)\big(1 + u(x,\tau)\big)$ with $x$ the rescaled axial coordinate. To first order,
$$\partial_\tau u = \partial_x^2 u + u =: \mathcal{L}u .$$
On the Gaussian-weighted space $L^2(\mathbb{R}, e^{-x^2/4}dx)$, $\mathcal{L}$ has eigenfunctions the Hermite polynomials $H_k$ with
$$\mathcal{L}H_k = \Big(1-\tfrac{k}{2}\Big)H_k .$$
So there are exactly two **unstable** modes ($k=0$: change of the singular time, eigenvalue $1$; $k=1$: translation along the axis, eigenvalue $\tfrac12$), one **neutral** mode ($k=2$, eigenvalue $0$), and a stable tail $k\ge3$. Solutions asymptotic to the cylinder that are *not* the cylinder must, by the Merle–Zaag alternative, be dominated as $\tau\to-\infty$ by the neutral mode; matching $u \approx -\frac{1}{2}\,\frac{H_2(x)}{|\tau|}$ is precisely the asymptotic profile of the **ancient oval** in the compact case and of the **Bryant soliton** in the noncompact case.

**Where higher dimensions bite.** The computation above only tracked the radius $u$, i.e. deformations preserving the round cross-section. The full linearization acts on symmetric 2-tensors on $\mathbb{R}\times S^{n-1}$ and additionally sees $\mathrm{TT}$-deformations of the metric on $S^{n-1}$. For $n-1 = 2$ there are none ($S^2$ is rigid, $\mathrm{TT}$-tensors on $S^2$ vanish). For $n-1 \ge 4$ the round metric on $S^{n-1}$ admits non-trivial $\mathrm{TT}$-eigenmodes, and these are killed only by invoking weakly PIC2 or uniform PIC — not by the dimension count. This is the concrete reason the 3D argument does not transfer verbatim, and the precise place where the noncompact $n\ge4$ case stalls.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*