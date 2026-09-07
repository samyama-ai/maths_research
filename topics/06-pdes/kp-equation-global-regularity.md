---
id: 06-pdes/kp-equation-global-regularity
title: "KP Equation Global Regularity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# KP Equation Global Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kp-equation-global-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

The Kadomtsev–Petviashvili (KP) equations are the two weakly transverse perturbations of KdV,
$$\partial_x\big(\partial_t u + \partial_x^3 u + u\,\partial_x u\big) + \sigma\,\partial_y^2 u = 0,\qquad \sigma = +1\ (\text{KP-II}),\quad \sigma=-1\ (\text{KP-I}),$$
for $u:\mathbb{R}_t\times\mathbb{R}^{1+d_y}\to\mathbb{R}$, $d_y\in\{1,2\}$.

**Open problem (global regularity).** Determine, for each sign $\sigma$, each transverse dimension $d_y$, and each nonlinearity $u^p\partial_x u$, whether arbitrary smooth, suitably decaying data generate solutions that stay smooth for all time, and identify the sharp function space in which the flow is globally well posed. Four concrete sub-problems are open:

1. **KP-II, large data at critical regularity.** Is KP-II globally well posed in the scaling-critical space $\dot H^{-1/2,0}(\mathbb{R}^2)$ for arbitrarily large data? Known only for small data.
2. **KP-II in 3D.** Is KP-II ($d_y=2$) globally well posed for large data in the critical space $\dot H^{1/2,0}(\mathbb{R}^3)$, or in any space? No conservation law is subcritical there.
3. **KP-I in 3D.** Extend the two-dimensional energy-space global theory to $d_y=2$.
4. **Generalized KP-I blow-up.** For $\partial_x(\partial_t u+\partial_x^3u+u^p\partial_xu)-\partial_y^2u=0$ with $p\ge 4/3$ ($L^2$-critical and above), prove that finite-time blow-up actually occurs from smooth finite-energy data, and describe the blow-up rate and profile.

A complete resolution means, for each case, either a global-existence theorem with an a priori bound propagating a Sobolev norm, or an explicit solution whose $H^s$ norm becomes infinite in finite time.

## 2. Mathematical Foundations

Write $\partial_x^{-1}$ for the Fourier multiplier $(i\xi)^{-1}$, defined on functions with $\hat u$ vanishing suitably at $\xi=0$ (the "zero-mass" constraint $\int u\,dx=0$ is part of the KP formalism).

**Linear symbol.** With $u\sim e^{i(x\xi+y\eta+t\omega)}$,
$$\omega_\sigma(\xi,\eta) = \xi^3 - \sigma\,\frac{\eta^2}{\xi}.$$
The singularity at $\xi=0$ is the source of every technical difficulty.

**Anisotropic Sobolev spaces.** $\|u\|_{H^{s_1,s_2}}=\big\|\langle\xi\rangle^{s_1}\langle\eta\rangle^{s_2}\hat u\big\|_{L^2}$; homogeneous versions $\dot H^{s,0}$ use $|\xi|^{s}$.

**Scaling.** If $u$ solves KP then so does $u_\lambda(t,x,y)=\lambda^2u(\lambda^3t,\lambda x,\lambda^2y)$, and
$$\|u_\lambda\|_{\dot H^{s,0}} = \lambda^{\,s+3/2-d_y}\|u\|_{\dot H^{s,0}}\quad\Longrightarrow\quad s_{\mathrm{crit}} = d_y - \tfrac32 .$$
So $s_{\rm crit}=-1/2$ in 2D and $s_{\rm crit}=+1/2$ in 3D.

**Conservation laws.** Both signs conserve mass $M(u)=\int u^2$ and the Hamiltonian
$$E_\sigma(u)=\int \Big(\tfrac12 u_x^2 - \tfrac{\sigma}{2}\big(\partial_x^{-1}\partial_y u\big)^2 - \tfrac16 u^3\Big)\,dx\,dy .$$
For KP-I ($\sigma=-1$) the quadratic part is positive definite, defining the **energy space**
$$\mathbb{E}=\{u\in L^2:\ \partial_xu\in L^2,\ \partial_x^{-1}\partial_yu\in L^2\},$$
and $E_{-1}$ is coercive on $\mathbb{E}$ below the ground-state mass threshold. For KP-II the quadratic part is indefinite, so no energy space exists and $L^2$ conservation is the only usable global bound.

**Resonance function.** For a trilinear interaction $\xi_3=\xi_1+\xi_2$, $\eta_3=\eta_1+\eta_2$,
$$\Omega_\sigma = \omega_\sigma(\xi_3,\eta_3)-\omega_\sigma(\xi_1,\eta_1)-\omega_\sigma(\xi_2,\eta_2)= 3\xi_1\xi_2\xi_3 + \sigma\,\frac{(\eta_1\xi_2-\eta_2\xi_1)^2}{\xi_1\xi_2\xi_3}.$$
For KP-II the two terms carry the same sign, giving $|\Omega_{+1}|\ge 3|\xi_1\xi_2\xi_3|$ and strong smoothing in $X^{s,b}$ spaces. For KP-I they cancel on a codimension-one set, and no such lower bound holds.

Both equations are completely integrable (Lax pair, inverse scattering), but IST for KP is only rigorously implemented for restricted data classes, so global regularity is attacked by PDE methods.

## 3. History & State of the Art (SOTA)

- **1970.** Kadomtsev and Petviashvili derive the equations to test transverse stability of the KdV line soliton; $\sigma=-1$ models strong surface tension (Bond number $>1/3$), $\sigma=+1$ weak surface tension.
- **1983–1993.** Ukai and Isaza–Mejía-type classical local theory; Bourgain's $X^{s,b}$ method (GAFA 1993) proves **global well-posedness of KP-II in $L^2(\mathbb{R}^2)$ and $L^2(\mathbb{T}^2)$**, the first genuinely low-regularity global result.
- **2001.** Takaoka–Tzvetkov push KP-II local theory to $H^{s,0}(\mathbb{R}^2)$, $s>-1/3$; Isaza–Mejía obtain comparable negative-index results and, by an I-method argument, global well-posedness for $s>-1/14$.
- **2001–2002.** Molinet–Saut–Tzvetkov show the KP-I flow map is **not** $C^2$, indeed not locally uniformly continuous, on any $H^{s_1,s_2}$ — Picard iteration and $X^{s,b}$ methods are structurally unavailable. They nevertheless prove global well-posedness in the "second energy space" by compactness plus higher conservation laws.
- **2007–2008.** Ionescu–Kenig (periodic) and **Ionescu–Kenig–Tataru** (Invent. Math. 173, 2008) prove global well-posedness of KP-I in the natural energy space $\mathbb{E}$ on $\mathbb{R}^2$, using frequency-localized short-time function spaces adapted to the resonance geometry.
- **2008–2010.** Hadac; then **Hadac–Herr–Koch** establish small-data global well-posedness and scattering for KP-II in the critical $\dot H^{-1/2,0}(\mathbb{R}^2)$ via $U^p/V^p$ spaces, plus small-data results in 3D.
- **2015.** Mizumachi proves nonlinear asymptotic stability of the KP-II line soliton in $\mathbb{R}^2$; Rousset–Tzvetkov had earlier proved transverse nonlinear instability for KP-I, confirming the 1970 heuristic.
- **2012–2021.** Klein–Saut's numerics and monograph map blow-up for generalized KP-I and stability boundaries.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| KP-II, $\mathbb{R}^2$ and $\mathbb{T}^2$, data in $L^2$ | Globally well posed (Bourgain 1993) |
| KP-II, $H^{s,0}(\mathbb{R}^2)$, $s>-1/3$ | Locally well posed (Takaoka–Tzvetkov 2001) |
| KP-II, $H^{s,0}(\mathbb{R}^2)$, $-1/14<s<0$ | Globally well posed (Isaza–Mejía) |
| KP-II, $\dot H^{-1/2,0}(\mathbb{R}^2)$, **small** data | Global + scattering (Hadac–Herr–Koch 2009) |
| KP-II, $\mathbb{R}^3$, small data in critical $\dot H^{1/2,0}$ | Global (Hadac 2008; Hadac–Herr–Koch) |
| KP-I, energy space $\mathbb{E}(\mathbb{R}^2)$, arbitrary data | Globally well posed (Ionescu–Kenig–Tataru 2008) |
| KP-I, second energy space, $\mathbb{R}^2$ and $\mathbb{T}^2$ | Global (Molinet–Saut–Tzvetkov 2002, 2007) |
| KP-I with non-localized (line-soliton) background | Global (Molinet–Saut–Tzvetkov, CMP 2007) |
| gKP-I, $L^2$-subcritical $p<4/3$ | Global in energy space; ground states stable |
| gKP-I, $p\ge 4/3$, data with $E<0$ in a weighted space | Solutions cannot stay in the space for all time (Liu 2001) — instability/virial obstruction, not a proven blow-up |
| Line-soliton transverse stability | KP-II stable (Mizumachi 2015); KP-I unstable (Rousset–Tzvetkov 2009) |

## 5. Principal Obstacles

- **The $\partial_x^{-1}$ singularity.** The symbol $\eta^2/\xi$ blows up as $\xi\to0$. Data are constrained by an antiderivative condition that is not preserved by naive truncation, so standard localization and paraproduct decompositions break the solution class itself.
- **KP-I: failure of Picard iteration.** Molinet–Saut–Tzvetkov's counterexamples show the second Picard iterate is unbounded on every $H^{s_1,s_2}$. Consequently $X^{s,b}$ spaces, normal forms in their standard form, and all contraction-based perturbation theory fail; only short-time (frequency-dependent time-scale) spaces or compactness arguments survive, and those give no scattering and no low-regularity persistence.
- **KP-II: no coercive energy.** The Hamiltonian is indefinite, so above $L^2$ there is nothing to propagate and below $L^2$ nothing conserved. Global theory in $-1/2<s<0$ needs an almost-conservation quantity; the I-method loses too much because the modified energy's error term involves the same resonant $\xi\to0$ region.
- **3D criticality.** In $\mathbb{R}^3$, $s_{\rm crit}=1/2$ while the conserved mass sits at $s=0$, which is *supercritical*. There is no conserved or monotone quantity at or above critical regularity, so large-data global existence has no known mechanism, exactly as for energy-supercritical NLS.
- **Blow-up construction.** For gKP-I no rigidity/compactness machinery of Merle–Raphaël type has been transported: the anisotropic scaling, the nonlocal constraint, and the absence of a Galilean-type symmetry in $y$ block the usual modulation analysis around the ground state.
- **Integrability does not help.** Inverse scattering for KP requires decay and smallness assumptions (nonlocal $\bar\partial$ problems) not implied by finite energy; it yields no a priori Sobolev bound for rough data.

## 6. The Gap

Three sharp boundaries.

- **KP-II 2D:** proven from $s=0$ upward (Bourgain) and down to $s>-1/14$; the target is the full critical range $s\in(-1/2,0)$ plus large data at $s=-1/2$. The missing step is an almost-conserved quantity at negative $s$ that survives the resonant set $\xi_1\xi_2\xi_3\to 0$, or a concentration-compactness/rigidity theorem in $U^p$–$V^p$ spaces (no linear profile decomposition adapted to the KP symbol is currently available at the critical scaling).
- **KP-II 3D:** proven only for small critical data; the gap is the entire large-data regime, with no subcritical conserved quantity to bootstrap.
- **gKP-I, $p\ge4/3$:** proven that negative-energy solutions leave the weighted space; the gap is showing that the mechanism is genuine $H^1$-norm inflation in finite time rather than loss of decay, and constructing a stable blow-up profile. Numerics (Klein–Saut 2012) show self-similar blow-up but there is no proof.

## 7. Current Research (as of June 2026)

- **Critical-space large-data theory for KP-II.** Groups around Herr (Bielefeld) and Koch (Bonn) continue developing $U^p/V^p$ adapted function spaces; the outstanding technical object is a profile decomposition for the KP-II propagator at $\dot H^{-1/2,0}$. *(frontier — verify)*
- **Short-time function spaces for KP-I.** Extensions of the Ionescu–Kenig–Tataru framework to $d_y=2$ and to weighted/non-decaying backgrounds. *(frontier — verify)*
- **Soliton and multi-soliton asymptotic stability.** Following Mizumachi, work on KP-II soliton resolution and on the interaction of line solitons (Y-shaped resonant webs); Saut and collaborators (Paris) on the KP approximation validity for water waves.
- **Numerical analysis.** Klein and coauthors (Dijon) refine spectral computations of gKP-I blow-up rates and of the transition at $p=4/3$.
- **Fractional/other transverse dispersions.** Global theory for "KP-type" equations with $|\partial_x|^\alpha$ dispersion is used as a laboratory for the same obstacle; results here often precede the KP case.

## 8. Future Work

- Build a linear profile decomposition for $e^{it\omega_\sigma(D)}$ respecting the anisotropic scaling and the $\xi$-singularity; combine with a rigidity theorem to upgrade Hadac–Herr–Koch from small to large data.
- Develop an $I$-method whose modified energy is frequency-anisotropic (weights in $\xi$ and $\eta$ separately) to close the $-1/2<s<-1/14$ gap for KP-II.
- Adapt Merle–Raphaël modulation analysis to gKP-I by first proving spectral properties of the linearized operator around the anisotropic ground state (a lump-type solution), which is itself only known numerically for most $p$.
- Import integrable-structure information (higher conserved densities, Bäcklund transformations) as a source of a priori bounds at low regularity, in the style of the KdV $H^{-1}$ well-posedness proofs of Killip–Vişan.

## 9. Key References

- **[Foundational]** B. B. Kadomtsev, V. I. Petviashvili. *On the stability of solitary waves in weakly dispersing media.* Soviet Physics Doklady 15 (1970), 539–541.
- **[Foundational]** J. Bourgain. *On the Cauchy problem for the Kadomtsev–Petviashvili equation.* Geometric and Functional Analysis 3 (1993), 315–341.
- **[SOTA]** A. D. Ionescu, C. E. Kenig, D. Tataru. *Global well-posedness of the KP-I initial-value problem in the energy space.* Inventiones Mathematicae 173 (2008), 265–304.
- **[SOTA]** M. Hadac, S. Herr, H. Koch. *Well-posedness and scattering for the KP-II equation in a critical space.* Annales de l'IHP – Analyse Non Linéaire 26 (2009), 917–941 (with Erratum, 2010).
- **[SOTA]** M. Hadac. *Well-posedness for the Kadomtsev–Petviashvili II equation and generalisations.* Transactions of the AMS 360 (2008), 6555–6572.
- **[Key]** L. Molinet, J.-C. Saut, N. Tzvetkov. *Global well-posedness for the KP-I equation.* Mathematische Annalen 324 (2002), 255–275 (Erratum, Math. Ann. 328, 2004).
- **[Key]** L. Molinet, J.-C. Saut, N. Tzvetkov. *Global well-posedness for the KP-I equation on the background of a non-localized solution.* Communications in Mathematical Physics 272 (2007), 775–810.
- **[Key]** H. Takaoka, N. Tzvetkov. *On the local regularity of the Kadomtsev–Petviashvili-II equation.* International Mathematics Research Notices 2001, no. 2, 77–114.
- **[Key]** P. Isaza, J. Mejía. *Local and global Cauchy problems for the Kadomtsev–Petviashvili (KP-II) equation in Sobolev spaces of negative indices.* Communications in PDE 26 (2001), 1027–1057.
- **[Key]** Y. Liu. *Blow up and instability of solitary-wave solutions to a generalized Kadomtsev–Petviashvili equation.* Transactions of the AMS 353 (2001), 191–208.
- **[Key]** T. Mizumachi. *Stability of line solitons for the KP-II equation in $\mathbb{R}^2$.* Memoirs of the AMS 238 (2015), no. 1125.
- **[Key]** F. Rousset, N. Tzvetkov. *Transverse nonlinear instability for two-dimensional dispersive models.* Annales de l'IHP – Analyse Non Linéaire 26 (2009), 477–496.
- **[Survey]** J.-C. Saut. *Recent results on the generalized Kadomtsev–Petviashvili equations.* Acta Applicandae Mathematicae 39 (1995), 477–487.
- **[Survey/Book]** C. Klein, J.-C. Saut. *Nonlinear Dispersive Equations: Inverse Scattering and PDE Methods.* Applied Mathematical Sciences 209, Springer, 2021.
- **[Computational]** C. Klein, J.-C. Saut. *Numerical study of blow up and stability of solutions of generalized Kadomtsev–Petviashvili equations.* Journal of Nonlinear Science 22 (2012), 763–811.

## 10. Worked Example / Concrete Special Case

**The KdV line soliton inside KP, and where the two signs part company.**

Take the KdV soliton $u_0(t,x)=2\kappa^2\operatorname{sech}^2\!\big(\kappa(x-4\kappa^2t)\big)$, which solves $u_t+u_{xxx}+6uu_x=0$. Since $u_0$ is independent of $y$, $\partial_y^2u_0=0$, so $u_0$ solves both KP-I and KP-II exactly. Global regularity for this datum is trivial; the question is what happens under a transverse perturbation $u_0+\varepsilon e^{i\eta y}v(x)$ with $|\eta|\ll1$.

*Step 1 — the linear symbol.* Insert $e^{i(x\xi+y\eta+t\omega)}$ into $\partial_x(\partial_tu+\partial_x^3u)+\sigma\partial_y^2u=0$:
$$(i\xi)\big(i\omega + (i\xi)^3\big) + \sigma(i\eta)^2 = 0 \;\Longrightarrow\; -\xi\omega + \xi^4 - \sigma\eta^2 = 0 \;\Longrightarrow\; \omega=\xi^3-\sigma\frac{\eta^2}{\xi}.$$
For $|\eta|$ small and $\xi\to0$ the correction $-\sigma\eta^2/\xi$ dominates $\xi^3$: long transverse waves feel an *unbounded* frequency shift. This is the whole difficulty in one line.

*Step 2 — resonances.* With $\xi_3=\xi_1+\xi_2$, $\eta_3=\eta_1+\eta_2$, use $\frac{\eta_3^2}{\xi_3}-\frac{\eta_1^2}{\xi_1}-\frac{\eta_2^2}{\xi_2}=-\frac{(\eta_1\xi_2-\eta_2\xi_1)^2}{\xi_1\xi_2\xi_3}$ (check: $\xi_1=\xi_2=1,\eta_1=1,\eta_2=0$ gives $\tfrac12-1=-\tfrac12$ on both sides). Hence
$$\Omega_\sigma=3\xi_1\xi_2\xi_3+\sigma\frac{(\eta_1\xi_2-\eta_2\xi_1)^2}{\xi_1\xi_2\xi_3}.$$
For **KP-II** ($\sigma=+1$) both terms share the sign of $\xi_1\xi_2\xi_3$, so $|\Omega_{+1}|\ge 3|\xi_1\xi_2\xi_3|$ — a bilinear smoothing estimate follows and Bourgain's contraction closes in $L^2$.
For **KP-I** ($\sigma=-1$) the terms cancel whenever $(\eta_1\xi_2-\eta_2\xi_1)^2 = 3(\xi_1\xi_2\xi_3)^2$, a large resonant set. Along it, the second Picard iterate $\int_0^t e^{(t-s)L}\partial_x(u^2)\,ds$ has an unbounded $H^{s_1,s_2}$ norm: this is the Molinet–Saut–Tzvetkov obstruction, and it is why KP-I needed the entirely different short-time machinery of Ionescu–Kenig–Tataru.

*Step 3 — physical content.* Alexander–Pego–Sachs and Rousset–Tzvetkov show that for KP-I the linearization about $u_0$ has spectrum in the right half-plane for $0<|\eta|<\eta_*(\kappa)$, so the line soliton is transversely unstable; for KP-II, Mizumachi shows it is asymptotically stable. The sign that makes the resonance function coercive is the same sign that makes the soliton stable — which is why the open regularity questions cluster on the KP-I / large-data / 3D side.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*