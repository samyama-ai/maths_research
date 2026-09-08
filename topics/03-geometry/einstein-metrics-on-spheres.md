---
id: 03-geometry/einstein-metrics-on-spheres
title: "Existence of Einstein Metrics on Spheres and Sphere Theorem Rigidity (Besse Problem)"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existence of Einstein Metrics on Spheres and Sphere Theorem Rigidity (Besse Problem)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/einstein-metrics-on-spheres` · **Status:** open

## 1. Problem Statement / Conjecture

Two linked questions, both posed or collected in Besse's *Einstein Manifolds* (1987, Ch. 0 and Ch. 4):

**(A) Existence / multiplicity.** For which $n$ does the smooth manifold $S^n$ carry an Einstein metric other than the round one (up to scaling and diffeomorphism)? Equivalently, describe the moduli space
$$\mathcal{E}(S^n)=\{\,g \text{ Einstein on } S^n,\ \mathrm{Vol}(g)=1\,\}/\mathrm{Diff}(S^n).$$
It is known to be a single point for $n\le 3$, and infinite for $5\le n\le 9$ and for all odd $n\ge 5$. **Open:** is $\mathcal{E}(S^4)$ a point? Is $\mathcal{E}(S^n)$ infinite (or even non-trivial) for even $n\ge 10$?

**(B) Rigidity of the sphere theorem.** How much pinching forces an Einstein metric to be round? Precisely: find the largest $\delta_n$ such that every Einstein metric on a closed $n$-manifold with sectional curvature $\delta_n \le K \le 1$ is a round sphere or a rank-one symmetric space. The Einstein condition should allow $\delta_n$ far below the $1/4$ of the general sphere theorem; the conjectural answer in dimension 4 is that *any* Einstein metric on $S^4$ with $K>0$ is round.

A complete resolution of (A) in dimension 4 means either an existence proof for a non-round Einstein metric on $S^4$ or a uniqueness theorem with no curvature hypothesis. A resolution of (B) means a sharp pinching constant with an example attaining it.

## 2. Mathematical Foundations

Let $(M^n,g)$ be closed, $n\ge 3$. $g$ is **Einstein** if
$$\mathrm{Ric}(g)=\lambda g,\qquad \lambda\in\mathbb{R},$$
which by the contracted Bianchi identity forces $\lambda = R/n$ with $R$ constant. Einstein metrics are exactly the critical points of the normalized total scalar curvature (Einstein–Hilbert) functional
$$\mathcal{S}(g)=\frac{\int_M R_g\,dV_g}{\mathrm{Vol}(g)^{(n-2)/n}},$$
a functional with infinite Morse index and coindex, so no direct variational existence method applies.

**Decomposition.** The curvature operator splits as
$$\mathrm{Rm}=W+\frac{1}{n-2}\,\mathring{\mathrm{Ric}}\owedge g+\frac{R}{2n(n-1)}\,g\owedge g ,$$
with $W$ the Weyl tensor and $\mathring{\mathrm{Ric}}=\mathrm{Ric}-\frac{R}{n}g$. Einstein means $\mathring{\mathrm{Ric}}\equiv 0$, so the curvature is $W$ plus a constant-curvature term.

**Dimension 4.** Gauss–Bonnet and the signature formula give, for Einstein $g$ on $M^4$,
$$8\pi^2\chi(M)=\int_M\Big(|W|^2+\frac{R^2}{24}\Big)dV,\qquad 12\pi^2\tau(M)=\int_M\big(|W^+|^2-|W^-|^2\big)dV,$$
whence the **Hitchin–Thorpe inequality** $\chi(M)\ge \tfrac{3}{2}|\tau(M)|$. For $S^4$, $\chi=2,\ \tau=0$: no obstruction, and the identity instead yields the sharp bound $\int_M |W|^2 dV \le 16\pi^2$ for any Einstein metric on $S^4$, with equality iff $R=0$ (impossible for positive $\chi$ with $W\equiv0$ excluded) — so the round metric is the unique $W\equiv 0$ point.

**Cohomogeneity-one ansatz** (Böhm). On $S^{p+q+1}$ written as the union of two disc bundles, put
$$g=dt^2+f(t)^2 g_{S^p}+h(t)^2 g_{S^q},\qquad t\in[0,T],$$
which reduces $\mathrm{Ric}=\lambda g$ to a singular boundary-value problem for a nonlinear ODE system in $(f,h)$; smooth closure requires $f(0)=0,\ f'(0)=1,\ h(T)=0,\ h'(T)=-1$.

**Sasakian–Einstein ansatz** (Boyer–Galicki–Kollár). For weights $\mathbf{a}=(a_0,\dots,a_m)$ the Brieskorn link
$$L(\mathbf{a})=\{z_0^{a_0}+\cdots+z_m^{a_m}=0\}\cap S^{2m+1}\subset\mathbb{C}^{m+1}$$
is often diffeomorphic to $S^{2m-1}$; a Sasakian–Einstein metric on it exists when the quotient orbifold admits a positive Kähler–Einstein metric, guaranteed by Kollár's numerical admissibility conditions on $\mathbf{a}$. Such metrics have $\mathrm{Ric}=(2m-2)g$ and are never round for $m\ge 3$ non-standard weights.

## 3. History & State of the Art (SOTA)

- **1960–61, Berger.** First pinching theorems; an Einstein 4-manifold with $K\ge \delta>0$ and $\delta$ above an explicit constant is round.
- **1973, Jensen.** Second homogeneous Einstein metric on $S^{4n+3}$ from the quaternionic Hopf fibration — the first non-round Einstein metric on any sphere.
- **1974, Hitchin.** $\chi\ge\frac32|\tau|$ with rigidity; established 4-dimensional Einstein geometry as topologically constrained.
- **1987, Besse.** *Einstein Manifolds* collects the open problems: which manifolds admit Einstein metrics, and how large is the moduli space on $S^n$.
- **1998, Böhm.** Infinitely many *inhomogeneous* Einstein metrics of positive scalar curvature on $S^n$ for $5\le n\le 9$ (and on $\mathbb{C}P^2\\#\overline{\mathbb{C}P^2}$, products of spheres), by shooting for the cohomogeneity-one ODE.
- **1999, Gursky–LeBrun.** Sharpened 4-dimensional pinching using Seiberg–Witten/Weyl estimates.
- **2005, Boyer–Galicki–Kollár.** Infinitely many Sasakian–Einstein metrics on $S^5$, on all 28 smooth structures on $S^7$, and on $S^{2m+1}$ for every $m\ge 2$; extended to exotic spheres in dimensions 11 and 15.
- **2008–10, Brendle–Schoen, Brendle.** Ricci-flow proof of the differentiable $1/4$-pinched sphere theorem and its rigidity version; Einstein metrics with nonnegative isotropic curvature are locally symmetric.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $n=2,3$ | Einstein $\Leftrightarrow$ constant curvature; $\mathcal{E}(S^n)$ is a point. |
| $n=4$ | **Open.** Round is the only known Einstein metric on $S^4$. |
| $5\le n\le 9$ | Infinitely many inhomogeneous Einstein metrics (Böhm 1998). |
| $n=4k+3$ | Jensen's second homogeneous Einstein metric (1973). |
| odd $n\ge 5$ | Infinitely many Sasakian–Einstein metrics (BGK 2005), including on exotic spheres in $n=7,11,15$. |
| even $n\ge 10$ | **Open** — no non-round Einstein metric known on $S^{10}, S^{12},\dots$ |

Rigidity results actually proven:
- **Obata (1971).** An Einstein metric conformal to the round metric on $S^n$ is round up to a conformal diffeomorphism.
- **Koiso (1980).** The round metric is infinitesimally rigid: $\mathcal{E}(S^n)$ has the round point isolated; the second variation of $\mathcal{S}$ is strictly negative on transverse-traceless directions.
- **Gursky–LeBrun (1999).** An Einstein 4-manifold with $0<\delta\le K\le 1$ and $\delta\ge(\sqrt{1249}-23)/120\approx 0.1023$ is $S^4$ or $\mathbb{C}P^2$ with its symmetric metric.
- **D. Yang (2000).** Analogous rigidity under an $L^2$ curvature-pinching hypothesis rather than a pointwise one.
- **Brendle–Schoen (2008, 2009).** Pointwise $1/4$-pinched $\Rightarrow$ space form; weakly $1/4$-pinched $\Rightarrow$ space form or a rank-one symmetric space (no Einstein hypothesis needed).
- **Brendle (2010).** Einstein with nonnegative isotropic curvature $\Rightarrow$ locally symmetric; in dimension 4 an Einstein metric on $S^4$ with nonnegative sectional curvature is round.

## 5. Principal Obstacles

- **No variational scheme.** $\mathcal{S}$ has infinite index and coindex on the space of metrics; Yamabe-type minimax gives the round metric only when the Yamabe invariant is attained, and $Y(S^4)$ maximality does not distinguish other Einstein critical points.
- **Weyl tensor is unconstrained in dimension 4.** Einstein reduces $\mathrm{Rm}$ to $W$ plus constant curvature, and the only global control is $\int|W|^2\le 16\pi^2$. There is no pointwise mechanism forcing $W\to 0$ without an auxiliary hypothesis (positive curvature, self-duality, harmonic curvature, Kähler).
- **Cohomogeneity-one methods stop at $n=9$.** Böhm's shooting argument relies on the ODE's Lyapunov/rotation-number structure; the number of oscillations required for a smooth closure degenerates once the fibre dimensions exceed the range $p+q+1\le 9$, and the analogous non-existence results of Böhm–Wang–Ziller for homogeneous spaces suggest the obstruction is real, not technical.
- **Even dimensions have no Sasakian analogue.** BGK's method is intrinsically odd-dimensional: it produces metrics as links of hypersurface singularities carrying a contact structure. No comparable algebro-geometric machine exists for $S^{2m}$; the closest, nearly-Kähler or $G_2$-type structures, exist only in special dimensions ($S^6$ carries a nearly-Kähler but not a second Einstein metric).
- **Ricci flow degenerates below $1/4$.** Brendle–Schoen's proof uses invariance of the PIC1/PIC2 cones under the Hamilton ODE; these cones lose invariance below $1/4$-pinching, and Einstein metrics are flow *fixed points*, so no smoothing occurs — the flow argument gives nothing new for Einstein data.
- **No known topological obstruction on $S^4$.** Hitchin–Thorpe, Seiberg–Witten and Gromov's simplicial-volume obstructions are all vacuous on $S^4$; there is nothing to contradict, so uniqueness cannot be topological.

## 6. The Gap

Section 4 gives uniqueness on $S^4$ only under an extra curvature hypothesis: pinching $\ge 0.1023$, nonnegative sectional curvature, nonnegative isotropic curvature, or conformal flatness. Section 1 asks for uniqueness with *no* hypothesis. The exact missing step is a mechanism converting the integral bound $\int_{S^4}|W|^2\,dV\le 16\pi^2$ into $W\equiv 0$ — that is, an $\varepsilon$-regularity or gap theorem showing that no Einstein 4-metric can have small-but-nonzero Weyl energy. Existing arguments control $W^+$ and $W^-$ separately only when a Seiberg–Witten class or a sign of curvature is available.

For even $n\ge 10$ the gap is constructional: known ansätze (cohomogeneity one, Sasakian, homogeneous) have each been pushed to their structural limits without yielding a single non-round metric, and no obstruction has been proved either. Both a construction and a non-existence theorem are plausible.

## 7. Current Research (as of June 2026)

- **4-dimensional gap theorems.** Work continuing from LeBrun's curvature-functional programme on $\int|W^+|^2$ and Einstein moduli in dimension 4, seeking a Weyl-energy gap for positive-scalar-curvature Einstein metrics. No unconditional gap has been established.
- **K-stability transfer.** Following Chen–Donaldson–Sun and Collins–Székelyhidi, existence of Sasakian–Einstein metrics on links is now tied to K-stability of the affine cone; this yields further families on odd spheres and finer moduli descriptions. *(frontier — verify)* Extensions to weighted / irregular Sasakian structures on high-dimensional spheres remain in preprint form.
- **Numerical/computer-assisted searches** for cohomogeneity-one Einstein metrics on $S^n$, $n\ge 10$, using validated ODE shooting with interval arithmetic. *(frontier — verify)* No confirmed solution has been reported.
- **Stability and dynamics.** Böhm–Wang–Ziller-style variational methods for homogeneous Einstein metrics, plus $\nu$-entropy/linear-stability analyses of Jensen and Böhm metrics under Ricci flow, are used to organize the moduli space and to test whether non-round Einstein metrics on spheres are ever dynamically stable.
- **Sub-$1/4$ pinching for Einstein metrics.** Attempts to lower $\delta_4\approx0.1023$ via refined Weitzenböck/Bochner formulas, aiming for the conjectural $\delta_4=0$.

Active groups: Stanford (Brendle school, Ricci flow), Stony Brook (LeBrun, 4-manifold curvature functionals), Münster (Böhm, Wilking, cohomogeneity-one and Ricci flow), New Mexico/Auckland (Boyer–Galicki lineage, Sasakian geometry), Imperial/Oxford (K-stability).

## 8. Future Work

1. Prove or disprove a Weyl-energy gap: does there exist $\varepsilon>0$ such that any Einstein metric on $S^4$ with $0<\int|W|^2<\varepsilon$ is round? Koiso's rigidity gives this infinitesimally; the gap is the non-perturbative version.
2. Extend Böhm's ODE construction past $n=9$, or prove a non-existence theorem for cohomogeneity-one Einstein metrics on $S^n$, $n\ge10$, explaining the cutoff.
3. Find an even-dimensional analogue of the Sasakian link construction — e.g. Einstein metrics on $S^{2m}$ as quotients or as boundaries of special-holonomy cones.
4. Lower the pinching constant in the Gursky–LeBrun theorem toward $0$, ideally by an argument that does not use Seiberg–Witten theory (which is dimension-4 specific and vacuous on $S^4$).
5. Determine whether $\mathcal{E}(S^n)$ is compact for the known infinite families, i.e. whether Böhm/BGK metrics accumulate at orbifold or collapsed limits.

## 9. Key References

- **[Foundational]** A. L. Besse. *Einstein Manifolds.* Ergebnisse der Mathematik und ihrer Grenzgebiete 10, Springer-Verlag, 1987.
- **[Foundational]** G. R. Jensen. *Einstein metrics on principal fibre bundles.* Journal of Differential Geometry 8 (1973), 599–614.
- **[Foundational]** N. Hitchin. *Compact four-dimensional Einstein manifolds.* Journal of Differential Geometry 9 (1974), 435–441.
- **[Foundational]** M. Obata. *The conjectures on conformal transformations of Riemannian manifolds.* Journal of Differential Geometry 6 (1971), 247–258.
- **[Foundational]** N. Koiso. *Rigidity and stability of Einstein metrics — the case of compact symmetric spaces.* Osaka Journal of Mathematics 17 (1980), 51–73.
- **[SOTA]** C. Böhm. *Inhomogeneous Einstein metrics on low-dimensional spheres and other low-dimensional spaces.* Inventiones Mathematicae 134 (1998), 145–176.
- **[SOTA]** C. P. Boyer, K. Galicki, J. Kollár. *Einstein metrics on spheres.* Annals of Mathematics (2) 162 (2005), 557–580.
- **[SOTA]** C. P. Boyer, K. Galicki, J. Kollár, E. Thomas. *Einstein metrics on exotic spheres in dimensions 7, 11, and 15.* Experimental Mathematics 14 (2005), 59–64.
- **[SOTA]** M. Gursky, C. LeBrun. *On Einstein manifolds of positive sectional curvature.* Annals of Global Analysis and Geometry 17 (1999), 315–328.
- **[SOTA]** S. Brendle, R. Schoen. *Manifolds with 1/4-pinched curvature are space forms.* Journal of the American Mathematical Society 22 (2009), 287–307.
- **[SOTA]** S. Brendle, R. Schoen. *Classification of manifolds with weakly 1/4-pinched curvatures.* Acta Mathematica 200 (2008), 1–13.
- **[SOTA]** S. Brendle. *Einstein manifolds with nonnegative isotropic curvature are locally symmetric.* Duke Mathematical Journal 151 (2010), 1–21.
- **[SOTA]** D. Yang. *Rigidity of Einstein 4-manifolds with positive curvature.* Inventiones Mathematicae 142 (2000), 435–450.
- **[SOTA]** C. Böhm, M. Wang, W. Ziller. *A variational approach for compact homogeneous Einstein manifolds.* Geometric and Functional Analysis 14 (2004), 681–733.
- **[Survey]** C. P. Boyer, K. Galicki. *Sasakian Geometry.* Oxford Mathematical Monographs, Oxford University Press, 2008.
- **[Survey]** M. Wang. *Einstein metrics from symmetry and bundle constructions: a survey.* In *Surveys in Differential Geometry* Vol. 17, International Press, 2012.
- **[Survey]** S. Brendle, R. Schoen. *Sphere theorems in geometry.* In *Surveys in Differential Geometry* Vol. 13, International Press, 2009, 49–84.

## 10. Worked Example / Concrete Special Case

**Jensen's second Einstein metric on $S^{4n+3}$, computed explicitly.**

Take the quaternionic Hopf fibration $S^3 \hookrightarrow S^{4n+3}\xrightarrow{\ \pi\ }\mathbb{H}P^n$, a Riemannian submersion with totally geodesic fibres when $S^{4n+3}$ carries the unit round metric $g$. Deform by the **canonical variation**: for $t>0$ set
$$g_t = t\,g|_{\mathcal{V}} \oplus g|_{\mathcal{H}},$$
scaling the $S^3$ fibres only. Besse (9.70) gives, for $g$-unit vertical $U$ and horizontal $X$,
$$r_t(U,U)=r_F(U,U)+t^2|AU|^2,\qquad r_t(X,X)=r_B(X,X)-2t\,|A_X|^2,$$
where $A$ is O'Neill's integrability tensor.

*Calibrate the constants at $t=1$.* The fibre $S^3$ is round of curvature 1, so $r_F=2$. The base $\mathbb{H}P^n$ has $\mathrm{Ric}_B=(4n+8)\check g$. The round total space has $\mathrm{Ric}=(4n+2)g$. Hence
$$2+|AU|^2=4n+2\Rightarrow |AU|^2=4n,\qquad (4n+8)-2|A_X|^2=4n+2\Rightarrow |A_X|^2=3 .$$
(Consistency check on the total $A$-norm: $\dim\mathcal{H}\cdot 3 = 4n\cdot 3 = 12n$ and $\dim\mathcal{V}\cdot 4n = 3\cdot 4n = 12n$. ✓)

*Impose $\mathrm{Ric}(g_t)=\lambda g_t$.* Since $g_t(U,U)=t$ and $g_t(X,X)=1$:
$$2+4n\,t^2=\lambda t,\qquad (4n+8)-6t=\lambda .$$
Eliminating $\lambda$:
$$2+4nt^2=t(4n+8-6t)\ \Longrightarrow\ (4n+6)t^2-(4n+8)t+2=0\ \Longrightarrow\ (2n+3)t^2-(2n+4)t+1=0 .$$
The roots multiply to $1/(2n+3)$ and $t=1$ is visibly a root, so
$$\boxed{\,t_1=1\ (\text{round}),\qquad t_2=\frac{1}{2n+3}\,}$$
with Einstein constant $\lambda_2=4n+8-\dfrac{6}{2n+3}$.

For $n=1$: on $S^7$ this gives $t_2=1/5$, $\lambda_2=54/5$, a homogeneous non-round Einstein metric whose fibres are shrunk by $1/5$. Its sectional curvatures are pinched but not $1/4$-pinched, consistent with Brendle–Schoen. This single computation shows the phenomenon the Besse problem asks about: the round metric is one root of a quadratic, and the other root is a genuinely new Einstein structure. The open question is whether any analogous second root exists on $S^4$ — where there is no fibration to deform — or on $S^{10}$, where the fibration and link constructions both fail.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*