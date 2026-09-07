---
id: 06-pdes/navier-stokes-fractional-dissipation
title: "Navier Stokes Fractional Dissipation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Navier–Stokes with Fractional Dissipation (Hyperdissipative and Hypodissipative Regularity)

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/navier-stokes-fractional-dissipation` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Replace the Laplacian in the three-dimensional incompressible Navier–Stokes equations by a fractional power $(-\Delta)^{\alpha}$:

$$\partial_t u + (u\cdot\nabla)u + \nabla p = -\nu(-\Delta)^{\alpha}u,\qquad \nabla\cdot u = 0,\qquad u(\cdot,0)=u_0 .$$

**The problem.** Determine the exact set of exponents $\alpha>0$ for which every divergence-free $u_0\in H^s(\mathbb{R}^3)$ (or $\mathbb{T}^3$), $s$ large, generates a **unique global smooth solution**, and the set for which finite-time blowup or non-uniqueness occurs.

Three sub-questions, in decreasing order of tractability:

1. **(Lions exponent sharpness.)** J.-L. Lions proved global regularity for $\alpha\ge 5/4$. Is $5/4$ sharp for *smooth* solutions — i.e. does there exist $\alpha<5/4$ and smooth $u_0$ whose solution blows up in finite time?
2. **(Supercritical range $1\le\alpha<5/4$.)** Prove global regularity, or exhibit blowup, for the energy-supercritical hyperdissipative range. $\alpha=1$ is the Clay Millennium Problem.
3. **(Hypodissipative range $0<\alpha<1$.)** Determine the threshold below which Leray–Hopf weak solutions are non-unique.

A complete resolution requires, for each $\alpha$, either a global-in-time a priori bound closing the regularity bootstrap for arbitrary smooth data, or an explicit construction of a singularity/second solution.

## 2. Mathematical Foundations

**Fractional Laplacian.** For $f\in\mathcal{S}(\mathbb{R}^3)$, $\widehat{(-\Delta)^{\alpha}f}(\xi)=|\xi|^{2\alpha}\hat f(\xi)$. Write $\Lambda=(-\Delta)^{1/2}$, so the dissipation is $\nu\Lambda^{2\alpha}u$. On $\mathbb{T}^3$ the definition is by Fourier series on $\mathbb{Z}^3\setminus\{0\}$.

**Leray projection.** With $\mathbb{P}=\mathrm{Id}-\nabla\Delta^{-1}\nabla\cdot$, the system becomes
$$\partial_t u + \nu\Lambda^{2\alpha}u = -\mathbb{P}\,\nabla\cdot(u\otimes u).$$

**Energy identity.** Smooth decaying solutions satisfy
$$\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_0^t\|\Lambda^{\alpha}u(s)\|_{L^2}^2\,ds = \tfrac12\|u_0\|_{L^2}^2,$$
because $\int (u\cdot\nabla u)\cdot u = 0$ for $\nabla\cdot u=0$. Hence the **energy class**
$$u\in L^\infty_t L^2_x \cap L^2_t \dot H^{\alpha}_x .$$

**Scaling.** If $u$ solves the system, so does
$$u_\lambda(x,t)=\lambda^{2\alpha-1}u(\lambda x,\lambda^{2\alpha}t),\qquad p_\lambda=\lambda^{4\alpha-2}p(\lambda x,\lambda^{2\alpha}t).$$
The invariant homogeneous Sobolev index is $s_c=\tfrac{n}{2}-2\alpha+1$, so in $n=3$, $s_c=\tfrac52-2\alpha$. The energy norm $\|u\|_{L^2}$ is critical exactly when $s_c=0$, i.e. $\alpha=5/4$: this is the **Lions exponent**. $\alpha>5/4$ is subcritical, $\alpha<5/4$ supercritical.

**Serrin-type criticality.** A norm $L^p_tL^q_x$ is scaling-invariant iff
$$\frac{2\alpha}{p}+\frac{3}{q}=2\alpha-1 .$$

**Fractional Leibniz / commutator.** The bootstrap in $H^s$ uses the Kato–Ponce commutator estimate
$$\big\|\Lambda^s(fg)-f\Lambda^s g\big\|_{L^2}\lesssim \|\nabla f\|_{L^\infty}\|\Lambda^{s-1}g\|_{L^2}+\|\Lambda^s f\|_{L^2}\|g\|_{L^\infty},$$
giving $\tfrac{d}{dt}\|u\|_{H^s}^2 + 2\nu\|\Lambda^{\alpha}u\|_{H^s}^2 \lesssim \|\nabla u\|_{L^\infty}\|u\|_{H^s}^2$, so the Beale–Kato–Majda-type criterion $\int_0^T\|\nabla u\|_{L^\infty}\,dt<\infty$ controls regularity.

## 3. History & State of the Art (SOTA)

- **1934.** Leray constructs global weak solutions for $\alpha=1$; uniqueness/regularity open.
- **1969.** J.-L. Lions, *Quelques méthodes de résolution des problèmes aux limites non linéaires*, proves global existence and uniqueness of smooth solutions for $\alpha\ge \tfrac12+\tfrac n4$ ($=5/4$ in $n=3$). This remains the baseline theorem.
- **1982.** Caffarelli–Kohn–Nirenberg: for $\alpha=1$, the parabolic Hausdorff dimension of the singular set of suitable weak solutions is $0$.
- **2002.** Katz–Pavlović prove a "cheap CKN" inequality: for $1<\alpha<5/4$, the singular set at first blowup time has Hausdorff dimension $\le 5-4\alpha$. At $\alpha=5/4$ this gives dimension $0$, consistent with Lions.
- **2003–2006.** J. Wu develops the generalized-dissipation theory (Besov/critical-space well-posedness, lower bounds for $\int \Lambda^{2\alpha}f\,|f|^{q-2}f$), giving global small-data results in critical Besov spaces $\dot B^{1+3/p-2\alpha}_{p,q}$.
- **2009.** Tao (*Analysis & PDE*) proves global regularity for a **logarithmically supercritical** dissipation $\Lambda^{5/2}/g(\Lambda)$ whenever $\int_1^\infty \frac{ds}{s\,g(s)^4}=\infty$.
- **2014.** Barbato–Morandin–Romito extend the log-supercritical result to a wider class, improving the admissible $g$.
- **2016.** Tao (*JAMS*) constructs an **averaged** 3D Navier–Stokes equation with the same energy identity and finite-time blowup — a formal barrier to any purely energy-based proof at $\alpha=1$.
- **2018–2020.** Convex integration reaches the fractional setting: Colombo–De Lellis–De Rosa (hypodissipative), De Rosa, and Luo–Titi (hyperdissipative, $\alpha<5/4$) show non-uniqueness of weak solutions, proving the Lions exponent sharp *at the weak-solution level*.

**SOTA summary.** Smooth global regularity: proven for $\alpha\ge5/4$; open for all $\alpha<5/4$. Weak-solution uniqueness: false for all $\alpha<5/4$.

## 4. Partial Results / Verified Cases

| Range | Result |
|---|---|
| $\alpha\ge \tfrac12+\tfrac n4$ (i.e. $\alpha\ge5/4$ in $n=3$) | Global well-posedness, smooth solutions, arbitrary data (Lions 1969). Endpoint $\alpha=5/4$ included. |
| $\alpha>5/4$ | Subcritical; higher-regularity and analyticity bootstraps are routine. |
| Log-supercritical: $\Lambda^{5/2}/g(\Lambda)$, $\int^\infty \frac{ds}{s g(s)^4}=\infty$ (e.g. $g(s)=\log(2+s)^{1/4}$) | Global regularity (Tao 2009; improved by Barbato–Morandin–Romito 2014). |
| $1<\alpha<5/4$ | Partial regularity: $\dim_{\mathcal H}(\text{singular set})\le 5-4\alpha$ (Katz–Pavlović 2002). |
| Any $\alpha>0$, small critical data | Global well-posedness for $\|u_0\|_{\dot B^{1+3/p-2\alpha}_{p,q}}$ small (Wu 2005–2006). |
| Any $\alpha\ge1/2$ | Global Leray–Hopf weak solutions exist (energy method + Aubin–Lions compactness). |
| $\alpha<5/4$ | **Non-uniqueness** of weak solutions with prescribed energy profile (Luo–Titi 2020) — Lions exponent is sharp for weak solutions. |
| $0<\alpha<1/3$ | Non-uniqueness of **Leray–Hopf** solutions (Colombo–De Lellis–De Rosa 2018 for $\alpha<1/5$; De Rosa 2019 for $\alpha<1/3$). |
| 2D, any $\alpha>0$ | Global regularity (vorticity is transported with dissipation; $\|\omega\|_{L^\infty}$ maximum principle). |
| Dyadic / shell models at $\alpha<5/4$ | Finite-time blowup proven (Katz–Pavlović 2005; Cheskidov). |

## 5. Principal Obstacles

- **Supercriticality.** For $\alpha<5/4$ the only coercive global quantity — energy — has negative scaling dimension $s_c>0$. Iterating local existence with the energy bound gives existence times $T\sim \|u_0\|^{-\theta}$ that shrink under rescaling; the bootstrap fails at the *first* step, not at some fixable later step. All known a priori quantities (energy, $\|u\|_{L^\infty L^2}$, enstrophy in 2D) are either supercritical or not conserved in 3D.
- **No maximum principle.** The 3D vorticity equation $\partial_t\omega+u\cdot\nabla\omega=\omega\cdot\nabla u-\nu\Lambda^{2\alpha}\omega$ has the vortex-stretching term $\omega\cdot\nabla u$, which is a zeroth-order singular-integral product; it destroys any $L^p$ maximum principle, unlike the 2D or SQG cases.
- **Nonlocality of $\Lambda^{2\alpha}$.** For $\alpha\ne1$ the dissipation is not a differential operator: the Córdoba–Córdoba pointwise inequality $ \Lambda^{2\alpha}(|f|^{p}) \le p|f|^{p-1}\Lambda^{2\alpha} f$ is available, but there is no local energy identity with an exact divergence structure, so De Giorgi–Nash–Moser and CKN localizations require nonlocal tail terms — the source of the loss $5-4\alpha$ in Katz–Pavlović versus dimension $0$ at $\alpha=1$.
- **Tao's barrier.** Any proposed proof that uses only (i) the energy identity, (ii) the bilinear structure's cancellation, and (iii) frequency-localized estimates must fail: Tao's 2016 averaged equation satisfies all three and blows up. This rules out a broad class of "abstract" arguments.
- **Convex integration cuts the other way.** Below $5/4$ the equation admits wild weak solutions, so any regularity proof must use smoothness in an essential (non-weak-limit-stable) way; compactness/weak-limit arguments cannot decide the question.

## 6. The Gap

Proven: global regularity for $\alpha\ge5/4$ and for logarithmic relaxations $\Lambda^{5/2}/g(\Lambda)$ with $\int^\infty ds/(s g(s)^4)=\infty$. Proven false: uniqueness of weak solutions for $\alpha<5/4$.

Open: the entire **power-supercritical** window $\alpha\in(0,5/4)$ for *smooth* solutions. The precise barrier is quantitative. Tao's method gains a factor $g(N)^4$ over criticality on frequency $N$; a power gain $N^{4(5/4-\alpha)}$ is needed. The log-to-power gap corresponds to controlling energy flux across infinitely many dyadic scales at a *fixed* rate rather than a summably-improving one. Equivalently: find a coercive, scaling-critical or subcritical quantity $\mathcal{Q}[u]$ with $\frac{d}{dt}\mathcal{Q}\le C\mathcal{Q}$ for $\alpha<5/4$ — no candidate is known, and Tao's averaged construction shows none can come from energy structure alone.

## 7. Current Research (as of June 2026)

- **Convex integration for stronger topologies.** Following Buckmaster–Vicol and Luo–Titi, groups at EPFL (Colombo), Princeton/NYU (Vicol, Buckmaster) and IAS push non-uniqueness toward the Leray–Hopf class for larger $\alpha$; intermittent Beltrami/Mikado flows with fractional temporal correctors are the main tool. Reaching Leray–Hopf non-uniqueness for $\alpha\in[1/3,1)$ is the stated target. *(frontier — verify)*
- **Partial regularity refinements.** Improving the Katz–Pavlović bound $5-4\alpha$ using nonlocal $\varepsilon$-regularity with tail control; work of Colombo–Haffter (JDE 2021) obtains global regularity below $\alpha=5/4$ for classes of data satisfying a scaling-invariant smallness or symmetry condition.
- **Self-similar and discretely self-similar solutions.** Extending Nečas–Růžička–Šverák and Tsai-type exclusion arguments to $\alpha<5/4$; the fractional Liouville theorem needed is open. *(frontier — verify)*
- **Dyadic and averaged models.** Cheskidov, Dascaliuc, Grujić and collaborators use shell models where blowup at $\alpha<5/4$ is provable, to isolate which cancellation the true equation possesses that the models lack.
- **Numerics.** Spectral simulations of hyperdissipative 3D turbulence (e.g. bottleneck studies) test whether the singular-set dimension bound $5-4\alpha$ is attained; no computation exhibits blowup for $\alpha>1$.

## 8. Future Work

- Convert Tao's logarithmic gain into a power gain by tracking a nonlinear, non-energy quantity (e.g. a weighted enstrophy or a Besov norm with anisotropic weights).
- Prove or disprove a **fractional Liouville theorem**: bounded ancient mild solutions of the $\alpha$-Navier–Stokes on $\mathbb{R}^3\times(-\infty,0)$ with $s_c$-critical bound are constant. This would exclude Type-I self-similar blowup for a range $\alpha<5/4$.
- Sharpen partial regularity from $\dim\le5-4\alpha$ toward $\dim\le 3-2\alpha$ or better, which would give regularity for $\alpha$ near $3/2$ trivially but, if pushed, meaningful structure near $1$.
- Determine the exact hypodissipative threshold: is Leray–Hopf uniqueness false for all $\alpha<1$?
- Establish blowup for $\alpha<5/4$ by importing Tao's averaging construction into a genuine (non-averaged) fractional model — currently the most concrete route to proving sharpness of $5/4$ for smooth solutions.

## 9. Key References

- **[Foundational]** J.-L. Lions. *Quelques méthodes de résolution des problèmes aux limites non linéaires.* Dunod/Gauthier-Villars, Paris, 1969.
- **[Foundational]** J. Leray. *Sur le mouvement d'un liquide visqueux emplissant l'espace.* Acta Mathematica 63 (1934), 193–248.
- **[Foundational]** L. Caffarelli, R. Kohn, L. Nirenberg. *Partial regularity of suitable weak solutions of the Navier–Stokes equations.* Communications on Pure and Applied Mathematics 35 (1982), 771–831.
- **[Foundational]** N. Katz, N. Pavlović. *A cheap Caffarelli–Kohn–Nirenberg inequality for the Navier–Stokes equation with hyper-dissipation.* Geometric and Functional Analysis 12 (2002), 355–379.
- **[SOTA]** T. Tao. *Global regularity for a logarithmically supercritical hyperdissipative Navier–Stokes equation.* Analysis & PDE 2 (2009), 361–366.
- **[SOTA]** D. Barbato, F. Morandin, M. Romito. *Global regularity for a slightly supercritical hyperdissipative Navier–Stokes system.* Analysis & PDE 7 (2014), 2009–2027.
- **[SOTA]** T. Tao. *Finite time blowup for an averaged three-dimensional Navier–Stokes equation.* Journal of the American Mathematical Society 29 (2016), 601–674.
- **[SOTA]** T. Luo, E. S. Titi. *Non-uniqueness of weak solutions to hyperviscous Navier–Stokes equations: on sharpness of J.-L. Lions exponent.* Calculus of Variations and PDE 59 (2020), art. 92.
- **[SOTA]** M. Colombo, C. De Lellis, L. De Rosa. *Ill-posedness of Leray solutions for the hypodissipative Navier–Stokes equations.* Communications in Mathematical Physics 362 (2018), 659–688.
- **[SOTA]** L. De Rosa. *Infinitely many Leray–Hopf solutions for the fractional Navier–Stokes equations.* Communications in Partial Differential Equations 44 (2019), 335–365.
- **[SOTA]** M. Colombo, S. Haffter. *Global regularity for the hyperdissipative Navier–Stokes equation below the critical order.* Journal of Differential Equations 275 (2021), 815–836.
- **[SOTA]** T. Buckmaster, V. Vicol. *Nonuniqueness of weak solutions to the Navier–Stokes equation.* Annals of Mathematics 189 (2019), 101–144.
- **[Survey]** J. Wu. *Lower bounds for an integral involving fractional Laplacians and the generalized Navier–Stokes equations in Besov spaces.* Communications in Mathematical Physics 263 (2006), 803–831.
- **[Survey]** C. L. Fefferman. *Existence and smoothness of the Navier–Stokes equation.* Clay Mathematics Institute Millennium Problem description, 2000.

## 10. Worked Example / Concrete Special Case

**Why $\alpha=5/4$ is exactly the endpoint in $n=3$.**

*Step 1 — energy bound.* Testing with $u$ gives, for $\alpha=5/4$,
$$u\in L^\infty_t L^2_x\cap L^2_t\dot H^{5/4}_x .$$

*Step 2 — Sobolev embedding.* In $\mathbb{R}^3$, $\dot H^{s}\hookrightarrow L^{q}$ with $\frac1q=\frac12-\frac s3$. With $s=\frac54$:
$$\frac1q=\frac12-\frac{5}{12}=\frac{1}{12}\ \Longrightarrow\ q=12 .$$
So the energy identity alone yields $u\in L^2_tL^{12}_x$.

*Step 3 — test against the scaling condition.* The Serrin-type invariant relation is $\frac{2\alpha}{p}+\frac3q=2\alpha-1$. With $\alpha=\frac54$, $p=2$, $q=12$:
$$\frac{2\cdot\frac54}{2}+\frac{3}{12}=\frac54+\frac14=\frac32,\qquad 2\alpha-1=\frac52-1=\frac32 .$$
The two sides agree: the energy class is **exactly scaling-critical** at $\alpha=5/4$. This is precisely why Lions' argument closes at, and only at, $\alpha\ge5/4$.

*Step 4 — the deficit for $\alpha<5/4$.* Repeating Steps 2–3 for general $\alpha\in(1,5/4)$: energy gives $u\in L^2_t\dot H^{\alpha}\hookrightarrow L^2_tL^{q_\alpha}$ with $\frac{1}{q_\alpha}=\frac12-\frac{\alpha}{3}$, hence
$$\frac{2\alpha}{2}+\frac{3}{q_\alpha}=\alpha+\Big(\frac32-\alpha\Big)=\frac32,$$
while criticality demands $2\alpha-1<\frac32$. The energy norm is supercritical by the deficit
$$\delta(\alpha)=\frac32-(2\alpha-1)=\frac52-2\alpha=s_c>0 .$$
For $\alpha=1$ (classical Navier–Stokes), $\delta=\tfrac12$.

*Step 5 — what the deficit costs.* On frequency $N$, the dissipation removes energy at rate $\nu N^{2\alpha}$ while the nonlinearity transfers at rate $\sim N\|u_N\|_{L^\infty}\sim N^{5/2}\|u_N\|_{L^2}$ (Bernstein). The two balance when $N^{2\alpha}\sim N^{5/2}$, i.e. $\alpha=5/4$. For $\alpha<5/4$ the transfer wins by a factor $N^{5/2-2\alpha}=N^{2\delta}$ at high frequency; Tao's 2009 theorem recovers only a factor $g(N)^4$ (logarithmic), not $N^{2\delta}$ (power). That single power-versus-logarithm mismatch is the entire open problem.

*Step 6 — sharpness at the weak level.* Luo–Titi construct, for every $\alpha<5/4$, weak solutions $u\in C^0_t H^{\beta}_x$ with prescribed non-monotone energy $e(t)>0$; taking $e_1\ne e_2$ gives two distinct weak solutions from $u_0=0$. So $5/4$ cannot be lowered without leaving the weak-solution framework — the remaining question is entirely about *smooth* solutions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*