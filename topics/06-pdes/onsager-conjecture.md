---
id: 06-pdes/onsager-conjecture
title: "Onsager Conjecture"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Onsager Conjecture

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/onsager-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Consider the incompressible Euler equations on $\mathbb{T}^d$ ($d \ge 2$) or $\mathbb{R}^d$:
$$\partial_t u + \operatorname{div}(u \otimes u) + \nabla p = 0, \qquad \operatorname{div} u = 0 .$$
Onsager (1949) asserted a sharp dichotomy at Hölder exponent $1/3$ for weak (distributional) solutions:

- **(a) Rigidity.** If $u \in C^\alpha_{x}$ uniformly in time with $\alpha > 1/3$, then the kinetic energy $E(t) = \tfrac12 \int |u(x,t)|^2\,dx$ is constant in $t$.
- **(b) Flexibility.** For every $\alpha < 1/3$ there exist weak solutions $u \in C^\alpha$ whose energy is not constant — in particular, solutions that strictly dissipate energy.

A complete resolution requires proving both halves. Part (a) was proved in 1994; part (b) was proved by Isett (2018) for $d = 3$, and by Giri–Radu (2024) for $d = 2$. What remains open is the **endpoint** $\alpha = 1/3$ and the sharp scale of function spaces separating the two regimes, together with the physical statement that motivated Onsager: that anomalous dissipation is the zero-viscosity limit of Navier–Stokes turbulence.

## 2. Mathematical Foundations

**Weak solution.** $u \in C^0_t L^2_x$ is a weak solution if for all divergence-free $\varphi \in C_c^\infty$,
$$\int_0^T\!\!\int \big( u \cdot \partial_t \varphi + u\otimes u : \nabla \varphi \big)\,dx\,dt = 0 .$$
The pressure is recovered by $-\Delta p = \operatorname{div}\operatorname{div}(u\otimes u)$.

**Hölder and Besov scales.** $\|u\|_{C^\alpha} = \sup_{x\neq y} |u(x)-u(y)|/|x-y|^\alpha$. The natural scale for the rigidity side is Besov: $u \in B^{s}_{3,\infty}$ iff $\sup_{|h|>0} |h|^{-s}\,\|u(\cdot+h)-u(\cdot)\|_{L^3} < \infty$; $B^{s}_{3,c_0}$ is the subspace where $|h|^{-s}\|\delta_h u\|_{L^3} \to 0$ as $h\to0$.

**Energy flux.** Mollify at scale $\ell$: $u_\ell = u * \varphi_\ell$. Then
$$\partial_t \tfrac12|u_\ell|^2 + \operatorname{div}\big(\cdots\big) = -\,\Pi_\ell, \qquad \Pi_\ell := \nabla u_\ell : \big( (u\otimes u)_\ell - u_\ell \otimes u_\ell \big),$$
where $\tau_\ell = (u\otimes u)_\ell - u_\ell\otimes u_\ell$ is the Reynolds stress. Constantin–E–Titi's commutator identity gives the pointwise bound
$$|\tau_\ell| \lesssim \|\delta_\ell u\|^2, \qquad |\nabla u_\ell| \lesssim \ell^{-1}\|\delta_\ell u\|, \qquad \text{so} \quad \|\Pi_\ell\|_{L^1} \lesssim \ell^{-1}\,\|\delta_\ell u\|^3_{L^3}. \tag{$\star$}$$
If $u \in B^{\alpha}_{3,\infty}$ then $\|\Pi_\ell\|_{L^1} \lesssim \ell^{3\alpha - 1}$, which vanishes exactly when $\alpha > 1/3$.

**Duchon–Robert dissipation measure.** For any weak solution the limit
$$D(u) := \lim_{\ell\to0}\ \tfrac14\!\int \nabla\varphi_\ell(h)\cdot \delta_h u\, |\delta_h u|^2\,dh$$
exists in $\mathcal{D}'$ and satisfies the local balance $\partial_t \tfrac12|u|^2 + \operatorname{div}\big((\tfrac12|u|^2+p)u\big) = -D(u)$. Onsager's dichotomy is the statement that $D(u)\equiv 0$ above $1/3$ and $D(u) \gneq 0$ is attainable below.

**Scaling heuristic.** Kolmogorov 1941 predicts $\|\delta_\ell u\|_{L^3} \sim (\varepsilon \ell)^{1/3}$, i.e. exactly $\alpha = 1/3$, with flux $\varepsilon$ independent of $\ell$ — the borderline case of $(\star)$.

## 3. History & State of the Art (SOTA)

- **1949.** Onsager, *Statistical hydrodynamics* (Nuovo Cimento Suppl.), states the $1/3$ threshold in a single remark; his Fourier-based argument was reconstructed by Eyink (1994).
- **1993–1997.** Scheffer constructs a nontrivial compactly supported weak solution in $L^2(\mathbb{R}^2\times\mathbb{R})$; Shnirelman gives a simpler $L^2(\mathbb{T}^3)$ example and later an energy-decreasing one. These have no Hölder regularity.
- **1994.** Eyink proves conservation under a Fourier-side condition; Constantin–E–Titi prove it for $u \in L^3_t B^{\alpha}_{3,\infty}$, $\alpha>1/3$ — the definitive rigidity statement.
- **2000.** Duchon–Robert introduce the local dissipation measure, giving a distributional form of the result.
- **2008.** Cheskidov–Constantin–Friedlander–Shvydkoy sharpen rigidity to $u \in L^3_t B^{1/3}_{3,c_0}$, the current best.
- **2009–2016.** De Lellis–Székelyhidi import convex integration and Nash–Kuiper iteration into fluids: bounded solutions (2009), $C^{1/10}$ dissipative flows (2013), then Isett $1/5^-$ (2013 thesis), Buckmaster–De Lellis–Székelyhidi $1/5^-$ with prescribed energy, Buckmaster $1/3^-$ for a.e. time (2015), Buckmaster–De Lellis–Isett–Székelyhidi $1/5$-Hölder anomalous dissipation (Annals 2015).
- **2018.** Isett, *A proof of Onsager's conjecture* (Annals of Math. 188): nonconservative solutions in $C^{1/3-\varepsilon}(\mathbb{T}^3\times\mathbb{R})$, using "gluing" of Euler flows to control error concentration in time.
- **2019.** Buckmaster–De Lellis–Székelyhidi–Vicol (CPAM 72) upgrade to *admissible* solutions with strictly decreasing energy, matching the physically relevant sign.
- **2023–2024.** Novack–Vicol, *An intermittent Onsager theorem* (Invent. Math. 233): $L^1_t C^{1/3-\varepsilon}$ solutions satisfying the **local** energy inequality — the "strong Onsager conjecture". Giri–Radu (Invent. Math. 238, 2024) settle the 2D flexibility problem at $C^{1/3-\varepsilon}$ via a Newton–Nash scheme.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $u \in L^3_t B^{\alpha}_{3,\infty}$, $\alpha > 1/3$ | energy conserved | Constantin–E–Titi 1994 |
| $u \in L^3_t B^{1/3}_{3,c_0}$ | energy conserved (sharpest known) | CCFS 2008 |
| $u\in C^\alpha$, $\alpha<1/3$, $d=3$ | nonconservative solutions exist | Isett 2018 |
| same, with $E(t)$ strictly decreasing | admissible dissipative solutions | BDLSV 2019 |
| same, with local energy inequality | strong Onsager, $L^1_tC^{1/3-\varepsilon}$ | Novack–Vicol 2023 |
| $d=2$, $\alpha<1/3$ | nonconservative solutions exist | Giri–Radu 2024 |
| Bounded domains $\Omega\subset\mathbb{R}^3$ | conservation for $\alpha>1/3$ up to boundary | Bardos–Titi 2018; Drivas–Nguyen 2018 |
| Compressible Euler | conservation for $\alpha>1/3$ (all variables) | Feireisl–Gwiazda–Świerczewska-Gwiazda–Wiedemann 2017 |
| Ideal MHD | conservation of energy and cross-helicity, $\alpha>1/3$ | Caflisch–Klapper–Steele 1997 |
| Helicity in 3D Euler | conserved for $\alpha>1/3$ (not $1/2$ as naive scaling suggests) | Chae 2003; De Rosa 2019 |
| Prescribed smooth $E(t)>0$ | realizable by $C^{1/3-\varepsilon}$ solutions | BDLS 2016 |

## 5. Principal Obstacles

- **The endpoint is a logarithmic gap, not a scaling gap.** In $(\star)$ the bound at $\alpha=1/3$ gives $\|\Pi_\ell\|_{L^1} \lesssim 1$, uniformly bounded but not vanishing. Passing to the limit requires equidistribution of the flux ($c_0$ condition) or cancellation; no known estimate produces either from $B^{1/3}_{3,\infty}$ membership alone.
- **Convex integration loses a power at the top of the scale.** Each Nash iteration adds a Mikado/Beltrami perturbation of amplitude $\delta_q^{1/2}$ at frequency $\lambda_q$; the new Reynolds error is $\sim \delta_q^{3/2}\lambda_q / \lambda_{q+1}$ plus a transport error. Closing the loop with $\delta_q = \lambda_q^{-2\beta}$ forces $\beta < 1/3$ strictly. The losses are from (i) the time-derivative/transport error, (ii) the inverse-divergence operator $\mathcal{R}$, which is bounded on $C^\alpha$ but not on $C^{1/3}$ endpoint spaces.
- **Intermittency versus self-similarity.** Convex-integration solutions are highly intermittent: they are large on sets of small measure, so $\|u\|_{L^p}$ scales differently for different $p$. Real turbulence intermittency shifts the critical exponent for $L^p$-based rigidity, and the two constructions disagree about which space is critical.
- **No mechanism for uniqueness or selection.** Flexibility gives infinitely many solutions with the same data; nothing in the method identifies which (if any) arises as a vanishing-viscosity limit of Navier–Stokes. The constructions have no Navier–Stokes ancestry.
- **Fourier analysis is blind to the geometry.** Littlewood–Paley bounds control $\|\Pi_\ell\|_{L^1}$ but cannot detect the sign of $D(u)$; the classical machinery is symmetric under $t\mapsto -t$, while dissipation is not.

## 6. The Gap

The unresolved boundary sits precisely at $\alpha = 1/3$:

1. **Rigidity endpoint.** Is energy conserved for every weak solution in $L^3_t B^{1/3}_{3,\infty}$? Known only in the closure $B^{1/3}_{3,c_0}$; the quotient $B^{1/3}_{3,\infty} \setminus B^{1/3}_{3,c_0}$ is exactly the untested set.
2. **Flexibility endpoint.** Is there a dissipative weak solution with $u \in C^{1/3}$ (or in $L^3_tB^{1/3}_{3,\infty}$)? Convex integration reaches $1/3-\varepsilon$ for every $\varepsilon>0$ but the parameter budget degenerates as $\varepsilon\to0$.
3. **Physical Onsager.** Do Leray–Hopf solutions $u^\nu$ of Navier–Stokes with fixed smooth data satisfy $\limsup_{\nu\to0}\nu\int_0^T\|\nabla u^\nu\|_{L^2}^2 > 0$? Entirely open; the Euler-side flexibility results do **not** settle it.

## 7. Current Research (as of June 2026)

- **Endpoint rigidity.** Work on refined Besov/Orlicz and Lorentz-type spaces, and on whether the local energy inequality plus $B^{1/3}_{3,\infty}$ forces $D(u)\ge 0$ rather than $D(u)=0$. Groups: Cheskidov and collaborators (UIC/Westlake), Shvydkoy (UIC), Drivas (Stony Brook).
- **Anomalous dissipation for passive scalars.** Bruè–De Lellis (2023) and Armstrong–Vicol (2023, *Anomalous diffusion by fractal homogenization*) build velocity fields with genuine anomalous dissipation for advection–diffusion; these are the closest rigorous analogues of the physical conjecture. Extensions to the Navier–Stokes velocity itself are being pursued. *(frontier — verify)*
- **Sharp intermittent thresholds.** Post-Novack–Vicol work aims at $L^p$-based Onsager exponents $1/p + 2/3$-type criteria and at removing the $L^1_t$ (rather than $C^0_t$) time regularity. Vicol (NYU/Yale), Novack (Purdue), Giri, Radu (Princeton/IAS lineage).
- **Boundaries and physical domains.** Onsager-type criteria near walls, where the boundary layer contributes an extra dissipation term (Bardos–Titi–Wiedemann; Drivas–Nguyen).
- **Other systems.** Onsager thresholds for SQG (Isett–Vicol), compressible and relativistic Euler, MHD (magnetic helicity has exponent $0$, not $1/3$), and hypodissipative Navier–Stokes.

## 8. Future Work

- Prove or disprove conservation in $L^3_t B^{1/3}_{3,\infty}$; a counterexample would need flux concentrated on a set of vanishing measure — a genuinely intermittent construction at the endpoint.
- Develop convex integration schemes whose losses are logarithmic rather than power-type, so the exponent budget closes at $\beta = 1/3$.
- Connect flexibility to the vanishing-viscosity limit: construct a family $u^\nu$ solving Navier–Stokes converging to a dissipative Euler solution. De Lellis and Székelyhidi have repeatedly named this the central open problem.
- Establish selection principles (entropy-type admissibility beyond $E(t)$ decreasing) that would restore uniqueness among $C^{1/3-\varepsilon}$ solutions.
- Quantify how intermittency corrections (She–Lévêque-type multifractal spectra) modify the critical exponent in $L^p$-based spaces.

## 9. Key References

- **[Foundational]** L. Onsager. *Statistical hydrodynamics.* Il Nuovo Cimento, Supplemento 6, 279–287, 1949.
- **[Foundational]** P. Constantin, W. E, E. S. Titi. *Onsager's conjecture on the energy conservation for solutions of Euler's equation.* Communications in Mathematical Physics 165, 207–209, 1994.
- **[Foundational]** G. L. Eyink. *Energy dissipation without viscosity in ideal hydrodynamics I. Fourier analysis and local energy transfer.* Physica D 78, 222–240, 1994.
- **[Foundational]** J. Duchon, R. Robert. *Inertial energy dissipation for weak solutions of incompressible Euler and Navier–Stokes equations.* Nonlinearity 13, 249–255, 2000.
- **[SOTA]** A. Cheskidov, P. Constantin, S. Friedlander, R. Shvydkoy. *Energy conservation and Onsager's conjecture for the Euler equations.* Nonlinearity 21, 1233–1252, 2008.
- **[SOTA]** P. Isett. *A proof of Onsager's conjecture.* Annals of Mathematics 188(3), 871–963, 2018.
- **[SOTA]** T. Buckmaster, C. De Lellis, L. Székelyhidi Jr., V. Vicol. *Onsager's conjecture for admissible weak solutions.* Communications on Pure and Applied Mathematics 72(2), 229–274, 2019.
- **[SOTA]** M. Novack, V. Vicol. *An intermittent Onsager theorem.* Inventiones Mathematicae 233, 223–323, 2023.
- **[SOTA / Recent]** V. Giri, R.-O. Radu. *The 2D Onsager conjecture: a Newton–Nash iteration.* Inventiones Mathematicae 238, 691–768, 2024.
- **[Earlier milestone]** T. Buckmaster, C. De Lellis, P. Isett, L. Székelyhidi Jr. *Anomalous dissipation for 1/5-Hölder Euler flows.* Annals of Mathematics 182(1), 127–172, 2015.
- **[Survey]** C. De Lellis, L. Székelyhidi Jr. *On turbulence and geometry: from Nash to Onsager.* Notices of the AMS 66(5), 677–685, 2019.
- **[Survey]** G. L. Eyink, K. R. Sreenivasan. *Onsager and the theory of hydrodynamic turbulence.* Reviews of Modern Physics 78, 87–135, 2006.
- **[Book]** T. Buckmaster, V. Vicol. *Convex integration and phenomenologies in turbulence.* EMS Surveys in Mathematical Sciences 6, 173–263, 2019.

## 10. Worked Example / Concrete Special Case

**Claim (Constantin–E–Titi, worked out).** If $u$ is a weak solution on $\mathbb{T}^3$ with $u \in L^3\big([0,T]; C^\alpha\big)$, $\alpha > 1/3$, then $E(t)=E(0)$.

*Step 1 — mollify.* Let $\varphi_\ell(x)=\ell^{-3}\varphi(x/\ell)$, $\int\varphi=1$. Convolving the equation:
$$\partial_t u_\ell + \operatorname{div}(u_\ell\otimes u_\ell) + \nabla p_\ell = -\operatorname{div}\tau_\ell,\qquad \tau_\ell = (u\otimes u)_\ell - u_\ell\otimes u_\ell .$$
$u_\ell$ is smooth, so pairing with $u_\ell$ and integrating over $\mathbb{T}^3$ kills the transport and pressure terms:
$$\frac{d}{dt}\,\frac12\int |u_\ell|^2 = \int \nabla u_\ell : \tau_\ell \;=:\; -\int \Pi_\ell .$$

*Step 2 — commutator identity.* Writing $\delta_h u(x) = u(x+h)-u(x)$,
$$\tau_\ell(x) = \int \varphi_\ell(h)\,\delta_h u(x)\otimes\delta_h u(x)\,dh \;-\; \Big(\int\varphi_\ell(h)\delta_h u\,dh\Big)^{\otimes 2}.$$
Since $\varphi_\ell$ is supported in $|h|\le \ell$ and $\|\delta_h u\|_\infty \le \|u\|_{C^\alpha}|h|^\alpha$,
$$\|\tau_\ell\|_{L^\infty} \le 2\,\|u\|_{C^\alpha}^2\,\ell^{2\alpha}.$$

*Step 3 — gradient bound.* Because $\int\nabla\varphi_\ell = 0$,
$$\nabla u_\ell(x) = \int \nabla\varphi_\ell(h)\,\delta_h u(x)\,dh, \qquad \|\nabla u_\ell\|_{L^\infty} \le C\,\ell^{-1}\cdot \|u\|_{C^\alpha}\ell^{\alpha} = C\|u\|_{C^\alpha}\ell^{\alpha-1}.$$

*Step 4 — combine.*
$$\Big|\frac{d}{dt}\frac12\int|u_\ell|^2\Big| \le |\mathbb{T}^3|\;\|\nabla u_\ell\|_\infty\|\tau_\ell\|_\infty \le C\,\|u\|_{C^\alpha}^3\,\ell^{3\alpha-1}.$$
For $\alpha > 1/3$ the exponent $3\alpha - 1 > 0$, so integrating on $[0,t]$ and using $\int_0^T\|u\|^3_{C^\alpha}dt<\infty$:
$$\Big|\tfrac12\!\int|u_\ell(t)|^2 - \tfrac12\!\int|u_\ell(0)|^2\Big| \le C\,\ell^{3\alpha-1}\!\int_0^T\!\|u\|^3_{C^\alpha}\,dt \xrightarrow[\ell\to0]{} 0 .$$
Since $u\in C^0_tL^2_x$, $u_\ell \to u$ in $L^2$ uniformly in $t$, giving $E(t)=E(0)$. $\square$

*Where it breaks at $\alpha = 1/3$.* The right-hand side becomes $C\|u\|^3_{C^{1/3}}$, independent of $\ell$ — bounded but not small. Recovering smallness requires $\ell^{-1/3}\|\delta_\ell u\|_{L^3}\to 0$, i.e. exactly membership in $B^{1/3}_{3,c_0}$. That single missing decay is the entire remaining gap on the rigidity side, and Isett's construction shows the flexibility side saturates it from below for every $\varepsilon>0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*