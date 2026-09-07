---
id: 06-pdes/navier-stokes-partial-regularity
title: "Navier Stokes Partial Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Navier–Stokes Partial Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/navier-stokes-partial-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For the three-dimensional incompressible Navier–Stokes equations, Caffarelli, Kohn and Nirenberg (1982) proved that the space-time singular set $\mathcal{S}$ of a *suitable weak solution* has vanishing one-dimensional parabolic Hausdorff measure, $\mathcal{P}^1(\mathcal{S}) = 0$. The open problem has three linked parts.

1. **Sharpness.** Is the exponent $1$ optimal for genuine Navier–Stokes solutions, or can it be lowered? The conjecture of most workers is that $\mathcal{S} = \emptyset$, i.e. suitable weak solutions are smooth — the Clay Millennium Problem. Every improvement of the CKN dimension bound below $1$ would be new; no improvement of the *Hausdorff* bound has been obtained since 1982.
2. **Uniqueness/class.** CKN applies only to suitable weak solutions (those satisfying the local energy inequality). Whether *every* Leray–Hopf weak solution is suitable, and whether Leray–Hopf solutions are unique, is open.
3. **Realizability.** Scheffer's constructions show that CKN is sharp for the weaker *Navier–Stokes inequality*. Does any solution of the actual system attain a nonempty singular set at all?

A complete resolution means either constructing a suitable weak solution with $\mathcal{S}\neq\emptyset$ (and computing $\dim_{\mathcal P}\mathcal{S}$), or proving $\mathcal{S}=\emptyset$ for all suitable weak solutions with $u_0 \in L^2_\sigma(\mathbb{R}^3)$.

## 2. Mathematical Foundations

On $\Omega\times(0,T)$ with $\Omega\subseteq\mathbb{R}^3$:

$$\partial_t u + (u\cdot\nabla)u - \nu\Delta u + \nabla p = f,\qquad \nabla\cdot u = 0,\qquad u(\cdot,0)=u_0 .$$

**Scaling.** For $\lambda>0$, if $(u,p)$ solves the system then so does
$$u^\lambda(x,t)=\lambda\,u(\lambda x,\lambda^2 t),\qquad p^\lambda(x,t)=\lambda^2 p(\lambda x,\lambda^2 t).$$
The energy norm $\|u\|_{L^\infty_t L^2_x}$ scales like $\lambda^{-1/2}$: it is *supercritical*. Invariant (critical) norms include $L^3_x$, $\dot H^{1/2}$, $BMO^{-1}$, $L^p_tL^q_x$ with $\tfrac2p+\tfrac3q=1$.

**Parabolic cylinders and measure.** $Q_r(z_0)=B_r(x_0)\times(t_0-r^2,t_0)$, $z_0=(x_0,t_0)$. The parabolic Hausdorff measure is
$$\mathcal{P}^k(E)=\lim_{\delta\to0}\ \inf\Big\{\sum_i r_i^{\,k}\ :\ E\subseteq\bigcup_i Q_{r_i},\ r_i<\delta\Big\}.$$

**Suitable weak solution.** $u\in L^\infty_tL^2_x\cap L^2_t H^1_x$, $p\in L^{3/2}_{loc}$, solving the equations distributionally and satisfying the **local energy inequality** for all $0\le\varphi\in C_c^\infty$:
$$\int |u|^2\varphi\,dx\Big|_{t} + 2\nu\!\int_0^{t}\!\!\int |\nabla u|^2\varphi \le \int_0^{t}\!\!\int \Big[|u|^2(\partial_t\varphi+\nu\Delta\varphi) + (|u|^2+2p)\,u\cdot\nabla\varphi\Big].$$
Existence of such solutions (Scheffer; CKN; Lin) follows from retarded-mollification or Leray regularization.

**Regular / singular points.** $z_0$ is *regular* if $u\in L^\infty(Q_r(z_0))$ for some $r>0$; $\mathcal{S}$ is the complement.

**CKN $\varepsilon$-regularity theorem.** There is an absolute $\varepsilon_*>0$ such that
$$\limsup_{r\to 0}\ \frac{1}{r}\int_{Q_r(z_0)}|\nabla u|^2\,dx\,dt < \varepsilon_* \ \Longrightarrow\ z_0 \text{ regular.}$$
A companion criterion: $r^{-2}\int_{Q_r}\big(|u|^3+|p|^{3/2}\big)<\varepsilon_*$ implies regularity. Both quantities are scale-invariant under $u\mapsto u^\lambda$.

**Main theorem (CKN 1982).** $\mathcal{P}^1(\mathcal{S})=0$. Consequently, for a.e. fixed $t$, the spatial singular set has Hausdorff dimension $\le 1$, and $\mathcal S$ contains no space-time curve of positive length.

## 3. History & State of the Art

- **1934.** Leray constructs global weak solutions and shows any singular time $T$ obeys $\|u(t)\|_{L^\infty}\gtrsim (T-t)^{-1/2}$; the set of singular times has $\mathcal{H}^{1/2}$ measure zero.
- **1962–69.** Prodi, Serrin, Ladyzhenskaya: $u\in L^p_tL^q_x$, $\tfrac2p+\tfrac3q\le1$, $q>3$ implies smoothness.
- **1976–77.** Scheffer initiates partial regularity: $\mathcal{H}^{5/3}$ of the space-time singular set is zero, and the spatial singular set at fixed time has $\mathcal{H}^1$ measure zero.
- **1982.** Caffarelli–Kohn–Nirenberg, *CPAM* 35: $\mathcal{P}^1(\mathcal S)=0$ — still the best Hausdorff-measure bound after 44 years.
- **1996–98.** Nečas–Růžička–Šverák rule out nontrivial Leray self-similar blow-up in $L^3$; Tsai extends to local energy solutions.
- **1998–2007.** New proofs of CKN with cleaner machinery: Lin (compactness/blow-up), Ladyzhenskaya–Seregin (with weaker pressure hypotheses), Vasseur (De Giorgi iteration), Kukavica.
- **2003.** Escauriaza–Seregin–Šverák close the Serrin endpoint $L^\infty_tL^3_x$ via backward uniqueness for parabolic operators.
- **2007–2012.** Box-counting (fractal) dimension bounds: Robinson–Sadowski $\le 5/3$; Kukavica and Kukavica–Pei push below $5/3$ under mild integrability.
- **2019–2022.** Convex integration: Buckmaster–Vicol produce nonunique finite-energy weak solutions (not suitable, no local energy inequality); Albritton–Brué–Colombo produce nonunique *Leray–Hopf* solutions with body force $f$.
- **2019–2021.** Quantitative regularity: Tao's triple-logarithmic improvement of ESS; Barker–Prange's concentration-based quantitative bounds.

## 4. Partial Results / Verified Cases

- **Dimension bound.** $\mathcal{P}^1(\mathcal{S})=0$ in $3$D for all suitable weak solutions (CKN 1982), interior and — after Seregin (2002) — up to a smooth boundary with no-slip data.
- **Fixed-time slices.** For a.e. $t$, $\dim_{\mathcal H}\{x: (x,t)\in\mathcal S\}\le 1$; at the *first* blow-up time the singular set has $\mathcal H^1$ measure zero (Choe–Lewis 2000 refine this in Morrey scales).
- **Box-counting dimension.** $\dim_B(\mathcal{S})\le 5/3$ in space-time (Robinson–Sadowski 2007); $\le 45/29 \approx 1.552$ under an extra assumption (Kukavica 2009); parabolic fractal dimension bounds in Kukavica–Pei (2012).
- **$2$D.** Global smoothness (Leray, Ladyzhenskaya): $\mathcal S=\emptyset$.
- **Axisymmetric without swirl.** Global regularity (Ukhovskii–Yudovich, Ladyzhenskaya 1968). With swirl: no Type I singularity, i.e. $|u(x,t)|\le C\,\mathrm{dist}^{-1}$ or $\le C(T-t)^{-1/2}$ forces regularity (Seregin–Šverák 2009; Chen–Strain–Tsai–Yau 2008–09).
- **Higher dimensions.** In $\mathbb{R}^4$, at the first blow-up time the singular set has zero $2$-dimensional Hausdorff measure (Dong–Du 2007); boundary analogues in Dong–Gu (2014).
- **Hyperdissipation $(-\Delta)^\alpha$.** Katz–Pavlović (2002): $\dim_{\mathcal H}\mathcal S \le 5-4\alpha$ for $1<\alpha<5/4$; Tao (2009): global regularity for logarithmically supercritical dissipation.
- **Sharpness for the relaxed system.** Scheffer (1985–87) builds solutions of the *Navier–Stokes inequality* with singular sets of positive dimension (up to Hausdorff dimension close to $1$ in space-time); Ożański (2019) sharpens and systematizes these.

## 5. Principal Obstacles

- **Supercriticality.** The only coercive global quantity is $\|u_0\|_{L^2}^2$, which sits *below* every scale-invariant norm. Under $u\mapsto u^\lambda$ the energy shrinks as $\lambda\to0$, so the a priori bound gives no information at small scales; every $\varepsilon$-regularity criterion needs a critical quantity that the energy cannot control.
- **The pressure is nonlocal.** $p = (-\Delta)^{-1}\partial_i\partial_j(u_iu_j)$ is only $L^{3/2}_{loc}$ in the energy class; local estimates leak global information, and the term $\int p\,u\cdot\nabla\varphi$ in the local energy inequality is exactly the one that resists localization.
- **Dimension counting is saturated.** The CKN covering argument converts one unit of $\int|\nabla u|^2$ into one unit of $\sum r_i$. To beat exponent $1$ one needs strictly more than the energy — e.g. control of $\int |\nabla u|^{2+\delta}$ or of $u$ in a Morrey space — and no such bound is known for general data.
- **Fourier methods fail.** The nonlinearity is a bilinear term with no sign and no null structure; paraproduct decompositions produce a $\dot H^{1/2}$-critical loss that only linear-in-time smallness can absorb, so perturbative results are local in time or small-data.
- **Convex integration cuts the other way.** Buckmaster–Vicol and Albritton–Brué–Colombo show the *class* is flexible enough for nonuniqueness once the local energy inequality or the force is relaxed, so rigidity proofs must use suitability essentially — but suitability is exactly one scalar inequality, thin ammunition for a full regularity theorem.

## 6. The Gap

Proven: $\mathcal{P}^1(\mathcal S)=0$; $\dim_B\mathcal S\le 5/3$; no Type I or self-similar blow-up; regularity under any critical Serrin bound including $L^\infty_tL^3_x$.

Wanted: $\mathcal S=\emptyset$, or an example with $\mathcal S\neq\emptyset$.

The exact step: upgrade the *a.e.-scale* smallness that energy dissipation forces (for each $z_0$, $r^{-1}\int_{Q_r}|\nabla u|^2$ is small for *most* $r$) into smallness at *every* small $r$. Equivalently, close a supercritical-to-critical gap: derive from $u\in L^\infty_tL^2\cap L^2_tH^1$ any control of a scale-invariant norm along a sequence $r_j\to0$ at a *fixed* point. Type II blow-up — where $\|u(t)\|_{L^3}\to\infty$ only along sparse scales, permitted by Tao's triple-log bound — is the precise scenario neither ruled out nor realized.

## 7. Current Research (as of June 2026)

- **Quantitative regularity.** Tao's scheme (Carleman-based, epochs of regularity) and Barker–Prange's concentration estimates aim at quantitative lower bounds on blow-up rates in critical norms; the target is to replace triple-log by a power, which would rule out Type II blow-up. Groups at UCLA, Bordeaux/CY Cergy, Oxford/Bath. *(frontier — verify)*
- **Convex integration for suitable solutions.** Whether the local energy inequality obstructs Mikado/intermittent flows is actively contested; work of Buckmaster, Vicol, De Lellis, Colombo, Giri–Kwon–Novack on sharp integrability thresholds. *(frontier — verify)*
- **Sharpness constructions.** Ożański's programme, extending Scheffer, to build genuine forced Navier–Stokes solutions with prescribed singular-set dimension. *(frontier — verify)*
- **Axisymmetric refinements.** Removing the Type I hypothesis for swirl flows via Liouville theorems for ancient solutions (Seregin, Šverák, Koch, Nadirashvili, Tsai school).
- **Computational search.** Numerical hunts for self-similar or discretely self-similar blow-up in axisymmetric geometries (following Hou-type Euler results); no accepted Navier–Stokes candidate. *(frontier — verify)*

## 8. Future Work

- Prove that every Leray–Hopf solution is suitable, or exhibit a non-suitable one — this decides whether CKN covers the Millennium formulation.
- Obtain a Morrey or $L^{2+\delta}$ bound on $\nabla u$ near singular points that beats the covering exponent $1$.
- Establish a Liouville theorem for bounded ancient mild solutions in $\mathbb{R}^3\times(-\infty,0)$; combined with blow-up rescaling this would give $\mathcal S=\emptyset$ under Type I.
- Push hyperdissipation below $\alpha=1$ (Tao's log-supercritical result is $\alpha=1$ with a logarithm) and interpolate.
- Construct any singular suitable weak solution to the unforced system; even a $\mathcal H^{1/2}$-dimensional example would settle sharpness.

## 9. Key References

- **[Foundational]** Leray, J. *Sur le mouvement d'un liquide visqueux emplissant l'espace.* Acta Mathematica 63 (1934), 193–248.
- **[Foundational]** Scheffer, V. *Partial regularity of solutions to the Navier–Stokes equations.* Pacific Journal of Mathematics 66 (1976), 535–552.
- **[Foundational]** Caffarelli, L., Kohn, R., Nirenberg, L. *Partial regularity of suitable weak solutions of the Navier–Stokes equations.* Communications on Pure and Applied Mathematics 35 (1982), 771–831.
- **[Foundational]** Scheffer, V. *A solution to the Navier–Stokes inequality with an internal singularity.* Communications in Mathematical Physics 101 (1985), 47–85.
- **[SOTA]** Lin, F.-H. *A new proof of the Caffarelli–Kohn–Nirenberg theorem.* CPAM 51 (1998), 241–257.
- **[SOTA]** Ladyzhenskaya, O., Seregin, G. *On partial regularity of suitable weak solutions to the three-dimensional Navier–Stokes equations.* Journal of Mathematical Fluid Mechanics 1 (1999), 356–387.
- **[SOTA]** Escauriaza, L., Seregin, G., Šverák, V. *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness.* Russian Mathematical Surveys 58 (2003), 211–250.
- **[SOTA]** Vasseur, A. *A new proof of partial regularity of solutions to Navier–Stokes equations.* NoDEA 14 (2007), 753–785.
- **[SOTA]** Robinson, J. C., Sadowski, W. *Decay of weak solutions and the singular set of the three-dimensional Navier–Stokes equations.* Nonlinearity 20 (2007), 1185–1191.
- **[SOTA]** Kukavica, I. *The fractal dimension of the singular set for solutions of the Navier–Stokes system.* Nonlinearity 22 (2009), 2889–2900.
- **[SOTA]** Katz, N., Pavlović, N. *A cheap Caffarelli–Kohn–Nirenberg inequality for the Navier–Stokes equation with hyper-dissipation.* GAFA 12 (2002), 355–379.
- **[SOTA]** Buckmaster, T., Vicol, V. *Nonuniqueness of weak solutions to the Navier–Stokes equation.* Annals of Mathematics 189 (2019), 101–144.
- **[SOTA]** Albritton, D., Brué, E., Colombo, M. *Non-uniqueness of Leray solutions of the forced Navier–Stokes equations.* Annals of Mathematics 196 (2022), 415–455.
- **[Survey]** Ożański, W. S. *The Partial Regularity Theory of Caffarelli, Kohn, and Nirenberg and its Sharpness.* Lecture Notes in Mathematical Fluid Mechanics, Birkhäuser, 2019.
- **[Survey]** Robinson, J. C., Rodrigo, J. L., Sadowski, W. *The Three-Dimensional Navier–Stokes Equations: Classical Theory.* Cambridge Studies in Advanced Mathematics 157, CUP, 2016.
- **[Survey]** Fefferman, C. *Existence and Smoothness of the Navier–Stokes Equation.* Clay Mathematics Institute Millennium Problem description, 2000.

## 10. Worked Example / Concrete Special Case

**Deriving $\mathcal{P}^1(\mathcal S)=0$ from the $\varepsilon$-criterion.** This is the covering step, and it shows exactly why the exponent is $1$.

Fix a suitable weak solution on $Q_1(0)$ with $E:=\int_{Q_1}|\nabla u|^2 <\infty$. Let $\mathcal S\subset Q_{1/2}$ be the singular set and $\delta>0$.

*Step 1 (contrapositive of $\varepsilon$-regularity).* Every $z\in\mathcal S$ satisfies, for all small $r$,
$$\frac{1}{r}\int_{Q_r(z)}|\nabla u|^2\,dx\,dt \ \ge\ \varepsilon_*.$$

*Step 2 (Vitali).* Pick $r<\delta$. The family $\{Q_r(z)\}_{z\in\mathcal S}$ covers $\mathcal S$; extract a finite disjoint subfamily $Q_r(z_1),\dots,Q_r(z_N)$ such that $\{Q_{5r}(z_i)\}$ covers $\mathcal S$. Disjointness plus Step 1 gives
$$N\varepsilon_* r \ \le\ \sum_{i=1}^N \int_{Q_r(z_i)}|\nabla u|^2 \ \le\ \int_{U_\delta}|\nabla u|^2 =: E_\delta,$$
where $U_\delta$ is the $\delta$-neighbourhood of $\mathcal S$.

*Step 3 (measure).* Using the cover by $Q_{5r}(z_i)$,
$$\mathcal{P}^1_{5r}(\mathcal S)\ \le\ \sum_{i=1}^N (5r)^1 = 5Nr \ \le\ \frac{5E_\delta}{\varepsilon_*}.$$

*Step 4 (conclusion).* $\mathcal S$ has Lebesgue measure zero in space-time (a consequence of $u\in L^{10/3}$ and the same criterion), so by absolute continuity $E_\delta\to0$ as $\delta\to0$. Letting $r\to0$ gives $\mathcal{P}^1(\mathcal S)=0$. $\square$

**Why the exponent is stuck at $1$.** The bookkeeping in Step 2 balances one power of $r$ against one unit of dissipation, because the *scale-invariant* form of $\int|\nabla u|^2$ over $Q_r$ carries exactly the weight $r^{-1}$. To reach exponent $1-\eta$ one would need
$$\frac{1}{r^{1-\eta}}\int_{Q_r(z)}|\nabla u|^2 \ \ge\ \varepsilon_* \quad\text{for } z\in\mathcal S,$$
which is a *stronger* concentration statement than $\varepsilon$-regularity supplies — equivalent to a Morrey-space improvement on $\nabla u$ that no known a priori bound provides. Conversely Scheffer's Navier–Stokes-inequality examples realize singular sets of dimension arbitrarily close to $1$, so any improvement must use the equality (in particular the pressure equation $-\Delta p=\partial_i\partial_j(u_iu_j)$), not just the inequality.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*