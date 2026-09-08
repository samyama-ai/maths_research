---
id: 03-geometry/hamilton-tian-conjecture
title: "Hamilton-Tian Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hamilton-Tian Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/hamilton-tian-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(M, J)$ be a compact Fano manifold of complex dimension $n$ and let $\omega_0$ be a Kähler metric with $[\omega_0] = 2\pi c_1(M)$. The normalized Kähler–Ricci flow

$$\frac{\partial \omega(t)}{\partial t} = -\mathrm{Ric}(\omega(t)) + \omega(t), \qquad \omega(0)=\omega_0,$$

has a solution for all $t \in [0,\infty)$ (Cao, 1985).

**Conjecture (Hamilton–Tian).** For any sequence $t_i \to \infty$ there is a subsequence along which $(M, \omega(t_i))$ converges in the pointed Gromov–Hausdorff topology to a compact length space $(M_\infty, d_\infty)$ such that:

1. $M_\infty = \mathcal{R} \sqcup \mathcal{S}$, where the regular part $\mathcal{R}$ is an open smooth complex manifold and the singular set $\mathcal{S}$ is closed with Minkowski (hence Hausdorff) codimension $\ge 4$;
2. on $\mathcal{R}$, $d_\infty$ is induced by a smooth Kähler metric $\omega_\infty$ satisfying the **shrinking Kähler–Ricci soliton** equation;
3. $M_\infty$ is (the underlying space of) a normal $\mathbb{Q}$-Fano variety, and $\omega_\infty$ extends to a weak Kähler–Ricci soliton in the pluripotential sense.

A complete resolution requires proving (1)–(3) with no curvature assumption beyond Perelman's, i.e. without assuming Type I behaviour, bounded Ricci curvature, or the partial $C^0$-estimate.

The conjecture is now a **theorem**: proved in complex dimension $\le 3$ by Tian–Zhang (2016), in general by Chen–Wang (2020) and independently by Bamler (2018/2023) via Riemannian Ricci-flow compactness. What remains open are the *refinements*: uniqueness and algebraicity of the limit, its identification with a canonical algebro-geometric degeneration, and the rate of convergence.

## 2. Mathematical Foundations

**Fano manifold.** Compact complex manifold with $c_1(M) > 0$, i.e. $K_M^{-1}$ ample.

**Shrinking Kähler–Ricci soliton.** A triple $(M,\omega,V)$ with $V$ a holomorphic vector field and

$$\mathrm{Ric}(\omega) - \omega = \mathcal{L}_V\,\omega .$$

When $V = \nabla^{1,0} f$ for a real $f$, this reads in local holomorphic coordinates

$$R_{i\bar\jmath} + \partial_i\partial_{\bar\jmath} f = g_{i\bar\jmath}, \qquad \partial_i\partial_j f = 0 .$$

$f\equiv \text{const}$ recovers the Kähler–Einstein equation $\mathrm{Ric}(\omega)=\omega$. In real terms ($m=2n$), a gradient shrinker satisfies $\mathrm{Ric}(g) + \nabla^2 f = \tfrac{1}{2\tau} g$.

**Perelman's $\mathcal{W}$-entropy.** For $(g,f,\tau)$ with $\int_M (4\pi\tau)^{-m/2}e^{-f}\,dV_g = 1$,

$$\mathcal{W}(g,f,\tau) = \int_M \big[\tau(R + |\nabla f|^2) + f - m\big](4\pi\tau)^{-m/2} e^{-f}\, dV_g,$$

$\mu(g,\tau) = \inf_f \mathcal{W}$, $\nu(g)=\inf_{\tau>0}\mu(g,\tau)$. Along Ricci flow $\mu$ is nondecreasing, and it is constant exactly on gradient shrinkers. This is the variational engine: $\mu(\omega(t))$ is bounded above on a Fano manifold, so $\tfrac{d}{dt}\mu \to 0$, forcing limits to be *almost* solitons.

**Perelman's estimates for KRF on Fano manifolds** (unpublished; written up by Sesum–Tian, 2008). Let $u_t$ be the Ricci potential, $\mathrm{Ric}(\omega_t)-\omega_t = \sqrt{-1}\partial\bar\partial u_t$, normalized by $\int e^{-u_t}\omega_t^n = (2\pi)^n c_1^n$. There is $C = C(\omega_0)$ with

$$\|R(\omega_t)\|_{C^0} + \mathrm{diam}(M,\omega_t) + \|u_t\|_{C^0} + \|\nabla u_t\|_{C^0} \le C \quad \text{for all } t\ge 0 .$$

**Noncollapsing.** $\nu(g_0) > -\infty$ gives $\mathrm{Vol}(B_r(x)) \ge \kappa r^{2n}$ for $r\le 1$, uniformly in $t$.

**Partial $C^0$-estimate (Tian).** For $k$ large and $\{s_\alpha\}$ an $L^2(\omega_t)$-orthonormal basis of $H^0(M, K_M^{-k})$, the Bergman density $\rho_{k}(\omega_t) = \sum_\alpha |s_\alpha|^2_{h_t^k}$ satisfies $\inf_M \rho_k \ge b > 0$ uniformly in $t$. This is what upgrades a metric Gromov–Hausdorff limit to a *projective algebraic* limit.

**Codimension-4 regularity.** The structure theory of noncollapsed limits with bounded Ricci curvature (Cheeger–Colding; Cheeger–Naber, *Ann. of Math.* 2015) gives $\dim \mathcal{S} \le m-4$; the Ricci-flow analogue is the hard part here, since only $R$, not $\mathrm{Ric}$, is bounded.

## 3. History & State of the Art (SOTA)

- **1988–1995.** Hamilton studies singularity formation in Ricci flow and identifies gradient shrinking solitons as the expected blow-up models (*The formation of singularities in the Ricci flow*, 1995).
- **1985.** H.-D. Cao: long-time existence of the normalized KRF on Fano manifolds.
- **1997.** Tian formulates the partial $C^0$-conjecture and the Fano/Kähler form of the conjecture (*Invent. Math.* 130). The joint name records that Hamilton's Riemannian expectation and Tian's Kähler-algebraic refinement coincide here.
- **2002–03.** Perelman: $\mathcal{W}$-entropy, $\kappa$-noncollapsing, pseudolocality, and the scalar/diameter bounds above — the whole toolkit.
- **2007.** Tian–Zhu (*JAMS* 20): if $M$ admits a Kähler–Ricci soliton, the flow converges to it (modulo $\mathrm{Aut}$), for initial data in $2\pi c_1(M)$.
- **2011.** Enders–Müller–Topping: Type I singularities of Ricci flow have gradient shrinking soliton blow-ups — the conjecture under a Type I hypothesis.
- **2016.** Tian–Zhang: full conjecture for $n \le 3$ (*JEMS*) and partial regularity with codimension-4 singular set in all dimensions (*Acta Math.* 216).
- **2017–2020.** Chen–Wang, *Space of Ricci flows (II)*, Part A (*Forum Math. Sigma*, 2017) and Part B (*J. Differential Geom.* 116, 2020): weak compactness for polarized Ricci flows; full Hamilton–Tian conjecture in all dimensions.
- **2018–2023.** Bamler: *Convergence of Ricci flows with bounded scalar curvature* (*Ann. of Math.* 188, 2018), then the $\mathbb{F}$-convergence/compactness theory (*Invent. Math.* 233, 2023, plus companion preprints), giving a purely Riemannian proof and a metric-soliton structure theory for all noncollapsed limits.
- **2018–2023.** Chen–Sun–Wang; Han–Li; Blum–Liu–Xu–Zhuang: the limit is unique and matches a canonical two-step algebro-geometric degeneration.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n \le 3$ (Fano, any $\omega_0 \in 2\pi c_1$) | Full conjecture | Tian–Zhang, *JEMS* 18 (2016) |
| All $n$, $\mathrm{Ric}$ bounded along the flow | Limit is a smooth soliton off codim-4 set | Sesum; Chen–Wang I (*CPAM* 2012) |
| Type I singularities, all dimensions, Riemannian | Blow-up limits are gradient shrinkers | Enders–Müller–Topping (2011) |
| $M$ admits a Kähler–Ricci soliton | Exponential convergence to it | Tian–Zhu, *JAMS* (2007) |
| $M$ K-stable | Flow converges to the Kähler–Einstein metric | Chen–Sun–Wang, *Geom. Topol.* 22 (2018) |
| Toric Fano, all $n$ | Explicit soliton limit; $V$ determined by a real Monge–Ampère/volume-minimization problem | Wang–Zhu, *Adv. Math.* 188 (2004) |
| Del Pezzo surfaces ($n=2$) | Limit lies on the same manifold: $\mathbb{CP}^2\\#\overline{\mathbb{CP}^2}$ and $\mathbb{CP}^2\\#2\overline{\mathbb{CP}^2}$ carry solitons (Koiso, Cao; Wang–Zhu) | — |
| Partial $C^0$-estimate assumed | Conjecture follows directly | Wang–Zhu, *Adv. Math.* 381 (2021) |
| All $n$, no extra hypothesis | Full conjecture | Chen–Wang, *JDG* 116 (2020); Bamler (2018, 2023) |

## 5. Principal Obstacles

The obstacles that made this hard for two decades, and that still block the refinements:

- **Only scalar curvature is controlled.** Perelman bounds $R$ and the diameter, not $|\mathrm{Ric}|$ or $|\mathrm{Rm}|$. The whole Cheeger–Colding machinery — volume convergence, almost-splitting, cone rigidity, the codimension-4 theorem — takes $\mathrm{Ric} \ge -C$ as input. None of it applies verbatim to a flow with unbounded Ricci curvature.
- **No a priori bound on $\int |\mathrm{Rm}|^{n}$.** Ricci-flow $\varepsilon$-regularity needs a smallness threshold in a scale-invariant norm; producing one from entropy alone requires heat-kernel/Nash-entropy estimates that were not available before Bamler.
- **Compactness in the wrong category.** Gromov–Hausdorff limits of Kähler manifolds are metric spaces; upgrading to a *variety* needs the partial $C^0$-estimate, i.e. uniform lower bounds on Bergman kernels — which classically needed $\mathrm{Ric}$ bounds (Donaldson–Sun) that are absent here.
- **Jumping of complex structure.** The limit generally is *not* $M$: the flow can degenerate $(M,J)$ to a singular $\mathbb{Q}$-Fano variety. So no fixed-manifold PDE argument (continuity method, perturbation, implicit function theorem) can work; one must work in a moduli space of possibly singular spaces.
- **Non-uniqueness of tangent flows.** Ruling out different limits along different sequences $t_i \to \infty$ is a Łojasiewicz-type problem for a degenerate functional at a singular soliton; the standard Simon–Łojasiewicz argument needs regularity that is not available at $\mathcal{S}$.

## 6. The Gap

The gap the proofs closed: from "$\mu(\omega(t))$ converges, so $\tfrac{d\mu}{dt}\to 0$, so the flow is *approximately* a soliton in an integral sense" to "the geometric limit *is* a soliton, smooth away from codimension 4, and algebraic". Chen–Wang closed it with a polarized-flow compactness theory tailored to Kähler geometry plus a self-improving $\varepsilon$-regularity; Bamler closed it with $\mathbb{F}$-convergence of metric flows and Nash-entropy heat-kernel bounds, valid in the Riemannian category.

The remaining gap, in June 2026, is quantitative and canonical:

- **Rate.** Every proof is subsequential and qualitative. There is no general rate $d_{GH}\big((M,\omega(t)), (M_\infty,\omega_\infty)\big) \le C t^{-\alpha}$ or $Ce^{-\delta t}$ when the limit is singular.
- **Independence from $\omega_0$ and higher regularity of $\mathcal{S}$.** The limit variety is known to be independent of $\omega_0$ (Han–Li, Blum–Liu–Xu–Zhuang), but $\mathcal{S}$ is only known to have codimension $\ge 4$ — not that it is a complex-analytic subvariety with a stratification of standard type in all cases.

## 7. Current Research (as of June 2026)

- **Algebraic uniqueness / optimal degenerations.** Dervan–Székelyhidi (*JDG* 2020) predicted the limit as the "optimal destabilizer"; Han–Li (*Geom. Topol.* 27, 2023) proved algebraic uniqueness of the flow limit; Blum–Liu–Xu–Zhuang (*Forum Math. Pi* 11, 2023) proved existence of the Kähler–Ricci soliton degeneration for any $\mathbb{Q}$-Fano variety, via finite generation of the associated valuation. This is now the dominant framework: the KRF limit equals a *two-step degeneration* $X \rightsquigarrow X_0 \rightsquigarrow X_\infty$ determined by minimizing the $\mathbf{H}$-invariant. Groups: Princeton/Rutgers (Xu, Zhuang), Rutgers (Li), Utah (Blum).
- **Bamler's metric-flow program.** Continued development of $\mathbb{F}$-convergence, tangent flows, and stratification of singular sets in Ricci flow (Berkeley); extensions to the Kähler case give sharper structure of $\mathcal{S}$. *(frontier — verify)* Ongoing work aims at showing tangent flows are unique at generic singular points.
- **Bergman-kernel routes.** Following W. Jiang (*Crelle* 717, 2016) and Liu–Székelyhidi (*GAFA* 32, 2022), partial $C^0$-estimates under weaker hypotheses; Wang–Zhu's Peking group continues on soliton versions.
- **Non-Fano and conical extensions.** KRF on log Fano pairs and on Fano varieties with klt singularities; solitons with conical/edge singularities. *(frontier — verify)*
- **Convergence rates.** Łojasiewicz inequalities for the $\mathbf{H}$/$\mu$-functional near singular solitons, seeking polynomial or exponential rates. *(frontier — verify)*

## 8. Future Work

- Prove a **Łojasiewicz–Simon inequality** at singular shrinking Kähler–Ricci solitons, yielding an explicit convergence rate and uniqueness of the limit *without* passing through algebraic geometry.
- Show the singular set $\mathcal{S}$ of the limit is a **closed analytic subvariety** with the expected stratification, and that the flow's singularities occur only along it.
- Extend to the **log Fano / pair** setting and to **collapsing** situations (Fano fibrations), where entropy is not bounded below.
- Make the **two-step degeneration effective**: compute the optimal destabilizing valuation for concrete families (cubic threefolds, Mukai–Umemura degenerations) and match it to the metric limit.
- Develop a **Riemannian analogue** of the soliton degeneration picture: is there a canonical "algebraic" object attached to a general noncollapsed Ricci-flow limit?

## 9. Key References

- **[Foundational]** R. S. Hamilton. *The formation of singularities in the Ricci flow.* Surveys in Differential Geometry, Vol. II, International Press, 1995, 7–136.
- **[Foundational]** G. Tian. *Kähler–Einstein metrics with positive scalar curvature.* Inventiones Mathematicae 130 (1997), 1–37. [DOI](https://doi.org/10.1007/s002220050176)
- **[Foundational]** H.-D. Cao. *Deformation of Kähler metrics to Kähler–Einstein metrics on compact Kähler manifolds.* Inventiones Mathematicae 81 (1985), 359–372.
- **[Foundational]** G. Perelman. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:math/0211159, 2002.
- **[Foundational]** N. Sesum, G. Tian. *Bounding scalar curvature and diameter along the Kähler Ricci flow (after Perelman).* Journal of the Institute of Mathematics of Jussieu 7 (2008), 575–587. [DOI](https://doi.org/10.1017/s1474748008000133)
- **[SOTA]** G. Tian, Z. Zhang. *Regularity of Kähler–Ricci flows on Fano manifolds.* Acta Mathematica 216 (2016), 127–176. [DOI](https://doi.org/10.1007/s11511-016-0137-1)
- **[SOTA]** G. Tian, Z. Zhang. *Convergence of Kähler–Ricci flow on lower-dimensional algebraic manifolds of general type.* / *Relative volume comparison of Ricci flow and its applications*; and G. Tian, Z. Zhang, Journal of the European Mathematical Society 18 (2016) for the $n\le 3$ case. [DOI](https://doi.org/10.1093/imrn/rnv357)
- **[SOTA]** X. Chen, B. Wang. *Space of Ricci flows (II) — Part B: Weak compactness of the flows.* Journal of Differential Geometry 116 (2020), 1–123. [DOI](https://doi.org/10.4310/jdg/1599271253)
- **[SOTA]** X. Chen, B. Wang. *Space of Ricci flows (II) — Part A: Moduli of singular Calabi–Yau spaces.* Forum of Mathematics, Sigma 5 (2017), e32. [DOI](https://doi.org/10.1017/fms.2017.28)
- **[SOTA]** R. Bamler. *Convergence of Ricci flows with bounded scalar curvature.* Annals of Mathematics 188 (2018), 753–831. [DOI](https://doi.org/10.4007/annals.2018.188.3.2)
- **[SOTA]** R. Bamler. *Compactness theory of the space of super Ricci flows.* Inventiones Mathematicae 233 (2023), 1121–1277. [DOI](https://doi.org/10.1007/s00222-023-01196-3)
- **[SOTA]** G. Tian, X. Zhu. *Convergence of Kähler–Ricci flow.* Journal of the American Mathematical Society 20 (2007), 675–699.
- **[SOTA]** X. Chen, S. Sun, B. Wang. *Kähler–Ricci flow, Kähler–Einstein metric, and K-stability.* Geometry & Topology 22 (2018), 3145–3173. [DOI](https://doi.org/10.2140/gt.2018.22.3145)
- **[SOTA]** J. Han, C. Li. *Algebraic uniqueness of Kähler–Ricci flow limits and optimal degenerations of Fano varieties.* Geometry & Topology 27 (2023), 2691–2751. [DOI](https://doi.org/10.2140/gt.2024.28.539)
- **[SOTA]** H. Blum, Y. Liu, C. Xu, Z. Zhuang. *The existence of the Kähler–Ricci soliton degeneration.* Forum of Mathematics, Pi 11 (2023), e9. [DOI](https://doi.org/10.1017/fmp.2023.5)
- **[SOTA]** F. Wang, X. Zhu. *Tian's partial $C^0$-estimate implies Hamilton–Tian's conjecture.* Advances in Mathematics 381 (2021), 107619.
- **[SOTA]** R. Dervan, G. Székelyhidi. *The Kähler–Ricci flow and optimal degenerations.* Journal of Differential Geometry 116 (2020), 187–203. [DOI](https://doi.org/10.4310/jdg/1599271255)
- **[Related]** J. Cheeger, A. Naber. *Regularity of Einstein manifolds and the codimension 4 conjecture.* Annals of Mathematics 182 (2015), 1093–1165. [DOI](https://doi.org/10.4007/annals.2015.182.3.5)
- **[Survey]** G. Székelyhidi. *An Introduction to Extremal Kähler Metrics.* Graduate Studies in Mathematics 152, AMS, 2014.
- **[Survey]** C. Xu. *K-stability of Fano varieties: an algebro-geometric approach.* EMS Surveys in Mathematical Sciences 8 (2021), 265–354. [DOI](https://doi.org/10.4171/emss/51)

## 10. Worked Example / Concrete Special Case

**$M = \mathbb{CP}^2 \\# \overline{\mathbb{CP}^2}$, the blow-up of $\mathbb{CP}^2$ at one point.**

$M$ is Fano ($K_M^{-1}$ ample) but admits **no** Kähler–Einstein metric: $\mathrm{Aut}^0(M)$ is the non-reductive group of matrices fixing the blown-up point, contradicting Matsushima's theorem; equivalently the Futaki invariant $\mathrm{Fut}(V)=-\int_M V(u_\omega)\,\omega^2 \ne 0$ for the generator $V$ of the $\mathbb{C}^*$-action along the exceptional curve. So the flow cannot converge to a Kähler–Einstein metric, and the conjecture predicts a genuine soliton.

Write $M = \mathbb{P}(\mathcal{O}_{\mathbb{P}^1}\oplus\mathcal{O}_{\mathbb{P}^1}(-1))$ and use the $U(2)$-invariant Calabi ansatz: on the punctured total space put $\omega = \sqrt{-1}\,\partial\bar\partial\, u(\rho)$, $\rho = \log|z|^2$. Let $x = u'(\rho)$ be the moment map, ranging over $[a,b]$ with $b-a$ fixed by the cohomology class, and let $\varphi(x) = u''$ be the momentum profile. The metric is
$$g = \varphi(x)^{-1} dx^2 + \varphi(x)\,\theta^2 + x\, g_{FS},$$
with $\theta$ the connection form on the circle bundle. Smooth compactification requires the boundary conditions
$$\varphi(a)=\varphi(b)=0,\qquad \varphi'(a)=2,\quad \varphi'(b)=-2 .$$

The shrinking-soliton equation $\mathrm{Ric}(\omega)-\omega = \mathcal{L}_{\nabla f}\omega$ with $f=f(x)$ linear in the moment variable, $f = \lambda x + c$, reduces to a single first-order linear ODE
$$\big(x\,\varphi(x)\big)' \;-\; \lambda\, x\,\varphi(x) \;=\; 2x - x^{2},$$
whose solution is
$$\varphi(x) = \frac{e^{\lambda x}}{x}\int_a^x e^{-\lambda s}\,(2s-s^2)\,ds .$$
The conditions $\varphi(a)=\varphi(b)=0$ and $\varphi'(b)=-2$ then determine the *unique* pair $(\lambda, [a,b])$ — $\lambda \ne 0$ exactly because $\mathrm{Fut} \ne 0$. This is the **Koiso–Cao soliton** (Koiso 1990; Cao 1996).

Hamilton–Tian in this case: the flow starting from *any* $\omega_0 \in 2\pi c_1(M)$ converges — smoothly, exponentially fast, modulo $\mathrm{Aut}^0(M)$ — to this soliton (Tian–Zhu, 2007). Here $\mathcal{S} = \emptyset$ and $M_\infty \cong M$: no complex-structure jump. The same holds for $\mathbb{CP}^2\\#2\overline{\mathbb{CP}^2}$ (Wang–Zhu, 2004), so for all del Pezzo surfaces the limit sits on the original manifold. Jumping first appears in complex dimension $3$ — e.g. for K-unstable members of the Mukai–Umemura family, where the flow degenerates $(M,J)$ to a different, possibly singular $\mathbb{Q}$-Fano variety carrying the soliton. That phenomenon is the reason the conjecture must be stated for limits $M_\infty$ rather than for metrics on $M$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*