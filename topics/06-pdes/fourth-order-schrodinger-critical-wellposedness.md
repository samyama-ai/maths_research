---
id: 06-pdes/fourth-order-schrodinger-critical-wellposedness
title: "Sharp Well-posedness Threshold for the Cubic Fourth-Order Schrodinger Equation"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sharp Well-posedness Threshold for the Cubic Fourth-Order Schrödinger Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/fourth-order-schrodinger-critical-wellposedness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the cubic fourth-order (biharmonic) nonlinear Schrödinger equation on $\mathbb{R}^d$,

$$i\partial_t u + \Delta^2 u = \mu |u|^2 u, \qquad u(0,\cdot)=u_0 \in H^s(\mathbb{R}^d), \qquad \mu = \pm 1 .$$

Define the **critical Sobolev index** $s_c = \tfrac{d}{2} - 2$ (the index left invariant by the scaling symmetry) and the **well-posedness threshold**

$$s^*(d) \;=\; \inf\{\, s \in \mathbb{R} \;:\; \text{the Cauchy problem is locally well-posed in } H^s(\mathbb{R}^d) \,\},$$

where "well-posed" means existence, uniqueness in a natural solution space, and **continuous** dependence of the data-to-solution map on bounded sets.

**Conjecture (sharp threshold).** $s^*(d) = s_c = \tfrac d2 - 2$ for every $d \ge 1$; that is, the equation is locally well-posed in $H^s$ for all $s > s_c$ and ill-posed for $s < s_c$, with no intermediate obstruction. In particular, in dimensions $d = 1,2,3$, where $s_c = -\tfrac32, -1, -\tfrac12 < 0$, the equation should be well-posed in Sobolev spaces of **negative** regularity, all the way down to $s_c$.

A complete resolution requires (i) local well-posedness in $H^s$ for every $s \in (s_c, 0)$ when $d \le 3$ and every $s \in (s_c,\infty)$ when $d \ge 5$, or (ii) a proof that some strictly larger threshold $s^*(d) > s_c$ is forced by a genuine ill-posedness mechanism (norm inflation, non-uniqueness, or failure of continuity of the flow map).

## 2. Mathematical Foundations

**Symmetries and conserved quantities.** If $u$ solves the equation, so does

$$u_\lambda(t,x) = \lambda^{2} u(\lambda^4 t, \lambda x), \qquad \|u_\lambda(0)\|_{\dot H^s} = \lambda^{s - (\frac d2 - 2)}\|u_0\|_{\dot H^s},$$

which fixes $s_c = d/2-2$. Conserved are the mass and the energy

$$M(u) = \int_{\mathbb{R}^d}|u|^2\,dx, \qquad E(u) = \tfrac12\int_{\mathbb{R}^d}|\Delta u|^2\,dx + \tfrac{\mu}{4}\int_{\mathbb{R}^d}|u|^4\,dx .$$

The energy space is $H^2$. Hence the cubic problem is **mass-critical** in $d=4$ ($s_c=0$) and **energy-critical** in $d=8$ ($s_c=2$). Crucially, the biharmonic propagator $e^{it\Delta^2}$ admits **no Galilean invariance**: the symbol $|\xi|^4$ is not preserved by frequency translation, unlike $|\xi|^2$ for classical NLS.

**Dispersive and Strichartz estimates.** Stationary phase for the phase $t|\xi|^4$ gives (Ben-Artzi–Koch–Saut, 2000)

$$\|e^{it\Delta^2} f\|_{L^\infty_x} \lesssim |t|^{-d/4}\|f\|_{L^1_x}.$$

Call $(q,r)$ *biharmonic admissible* if $q,r \ge 2$, $(q,r,d)\ne(2,\infty,4)$, and

$$\frac 4q = d\Big(\frac12 - \frac1r\Big).$$

Then $\|e^{it\Delta^2}f\|_{L^q_tL^r_x} \lesssim \|f\|_{L^2_x}$, together with the corresponding inhomogeneous (Duhamel) estimate. Gaining $4/q$ derivatives of integrability per unit of time-integrability — versus $2/q$ for NLS — is the structural advantage exploited throughout.

**Local smoothing / resonance.** Writing the Duhamel term in Fourier variables, the resonance function for three interacting frequencies is

$$\Omega(\xi_1,\xi_2,\xi_3) = |\xi_1|^4 - |\xi_2|^4 + |\xi_3|^4 - |\xi_1-\xi_2+\xi_3|^4,$$

a quartic form. In $d=1$ it factors as $\Omega = 4(\xi_1-\xi_2)(\xi_2-\xi_3)\big(\xi_1^2+\xi_3^2+(\xi_1+\xi_3)^2 + \dots\big)$-type expression, quadratically stronger than the NLS analogue $-2(\xi_1-\xi_2)(\xi_2-\xi_3)$. Bourgain spaces $X^{s,b}$, defined by $\|u\|_{X^{s,b}} = \|\langle\xi\rangle^s\langle\tau - |\xi|^4\rangle^{b}\hat u\|_{L^2_{\tau,\xi}}$, are the natural setting: the extra resonance strength is exactly the resource conjectured to reach $s_c$.

## 3. History & State of the Art (SOTA)

The equation was introduced by **Karpman** (Phys. Rev. E, 1996) and **Karpman–Shagalov** (Physica D, 2000) to model the stabilizing effect of fourth-order dispersion on soliton instabilities in nonlinear optics. Its mathematical study began with **Ben-Artzi–Koch–Saut** (2000), who established the $|t|^{-d/4}$ dispersive decay, and **Pausader**, whose 2007–2009 papers built the modern well-posedness/scattering theory: global well-posedness in $H^2$ for the defocusing cubic problem, and scattering in $5 \le d \le 8$ (radial symmetry used at the energy-critical dimension $d=8$). **Miao–Xu–Zhao** (2009, 2011) removed radiality in high energy-critical dimensions. **Pausader–Shao** (2010) treated the mass-critical problem in high dimensions via concentration-compactness, and **Pausader–Xia** (2013) covered low-dimensional scattering.

Below the energy space, progress has been driven by Strichartz-based fixed points and $X^{s,b}$ methods: the standard subcritical theory yields local well-posedness for $s \ge \max(s_c,0)$, with the critical-index case $s=s_c$ known for small data (Ruzhansky–Wang–Zhang, 2016). The frontier is the strip $s_c < s < 0$ in $d \le 3$, where the classical Galilean ill-posedness argument of **Kenig–Ponce–Vega** (2001) is unavailable. The one clean breakthrough is periodic: **Oh–Wang** (2018) proved global well-posedness of the renormalized cubic 4NLS on $\mathbb{T}$ in $H^s$ for $s > -\tfrac13$.

## 4. Partial Results / Verified Cases

| Regime | Status | Source |
|---|---|---|
| $s \ge \max(s_c,0)$, all $d$, both signs | LWP by Strichartz contraction; subcritical time $T=T(\|u_0\|_{H^s})$ | Standard; see Pausader (2009), Dinh (2018) |
| $s = s_c$, $d \ge 5$, small data | GWP + scattering in $\dot H^{s_c}$; also small-data GWP in modulation spaces $M^s_{2,1}$ | Ruzhansky–Wang–Zhang, JMPA 2016 |
| $s \ge 2$ (energy space), defocusing, all $d$ | GWP; scattering for $5\le d\le 8$ ($d=8$ radial) | Pausader, JFA 2009 |
| Energy-critical $d \ge 9$ (power $|u|^{8/(d-4)}u$), defocusing | GWP + scattering, no radiality | Miao–Xu–Zhao, JDE 2011 |
| Mass-critical, $d \ge 5$, radial, defocusing | GWP + scattering in $L^2$ | Pausader–Shao, JHDE 2010 |
| Periodic $d=1$, renormalized equation | GWP in $H^s(\mathbb{T})$, $s > -\tfrac13$ | Oh–Wang, Forum Math. Sigma 2018 |
| $s < s_c$, all $d$ | Ill-posedness: norm inflation, failure of uniform continuity | Dinh (2018), method of Christ–Colliander–Tao (2003) |
| $d=1$, cubic | Long-range: no linear scattering; modified wave operators exist | Segata (2006); Hayashi–Naumkin (2015) |

Two structural gaps inside this table deserve emphasis: the **mass-critical dimension $d=4$** (cubic $=$ mass-critical) is not covered by Pausader–Shao's high-dimensional argument, and the **non-radial energy-critical case $d=8$** remains conditional in the literature.

## 5. Principal Obstacles

- **No Galilean symmetry.** For cubic NLS on $\mathbb{R}$, ill-posedness below $L^2$ follows by boosting a soliton: Galilean transformations move mass to high frequency at zero $\dot H^s$ cost for $s<0$. The symbol $|\xi|^4$ admits no such family, so the standard machine that *proves* $s^*=0$ for NLS produces nothing here. The threshold is therefore undetermined from both sides.
- **Multilinear estimates fail at negative regularity on $\mathbb{R}^d$.** The trilinear $X^{s,b}$ estimate $\||u|^2u\|_{X^{s,b-1}}\lesssim\|u\|^3_{X^{s,b}}$ breaks down for $s<0$ on high–low interactions: two very high frequencies $\pm N$ nearly cancel, output frequency $O(1)$, and the resonance function degenerates. The gain from the quartic $\Omega$ is invisible in this configuration.
- **No conservation law below $L^2$.** Mass and energy control $H^0$ and $H^2$; nothing controls $H^s$ for $s<0$. Even a local theory would not iterate without a substitute (normal-form energy, or an $I$-method-style almost-conserved quantity), and the fourth-order symbol makes the $I$-method's multiplier commutator estimates significantly worse.
- **Failure of pointwise-in-frequency smoothing.** The biharmonic phase has degenerate Hessian on the set $\{\xi : \nabla|\xi|^4 \text{ singular}\}=\{0\}$ and, more importantly, the level sets $\{|\xi|=\text{const}\}$ are spheres with *non-vanishing* curvature but the phase's radial fourth-order growth ruins uniform bilinear transversality estimates in $d\ge2$, so Bourgain-type $L^4$ refinements do not transfer verbatim from the Schrödinger setting.
- **Renormalization is genuinely needed on $\mathbb{T}$ and unclear on $\mathbb{R}^d$.** Oh–Wang's result is for the *renormalized* equation, obtained by removing a resonant term $2\|u\|_{L^2}^2u$; no analogous subtraction is available on the line, where the $L^2$ norm need not be finite for $H^s$, $s<0$, data.

## 6. The Gap

Proven: LWP for $s \ge \max(s_c,0)$; ill-posedness for $s<s_c$. Conjectured: LWP for all $s>s_c$.

The gap is therefore precisely the strip

$$s_c = \tfrac d2 - 2 \;<\; s \;<\; 0, \qquad d \in \{1,2,3\},$$

of width $2 - d/2$ (i.e. $3/2$, $1$, $1/2$ derivatives in $d=1,2,3$), plus the isolated critical endpoints $s=s_c$ for large data ($d\ge5$), $d=4$ mass-critical large-data theory, and $d=8$ energy-critical without radial symmetry.

The exact step to be crossed: prove a trilinear estimate in a function space $X$ scaling like $H^s$, $s_c<s<0$, that survives high–high–to–low interactions — or construct a solution family exhibiting norm inflation at some $s_0 \in (s_c,0)$, which would refute the conjecture and pin $s^*(d) \ge s_0$.

## 7. Current Research (as of June 2026)

- **Normal-form and modified-energy methods.** The Oh school (Edinburgh) continues to push infinite iterations of Poincaré–Dulac normal forms and para-controlled expansions from $\mathbb{T}$ to $\mathbb{T}^d$ and $\mathbb{R}$; extending $s>-1/3$ on $\mathbb{T}$ toward $s_c=-3/2$ is the stated goal. *(frontier — verify)*
- **Concentration-compactness at the mass-critical dimension $d=4$.** Groups following Pausader–Shao aim to remove the radial assumption and reach $d=4$; the missing ingredient is a linear profile decomposition adapted to $e^{it\Delta^2}$ handling frequency scales and the absence of Galilean cores. *(frontier — verify)*
- **Decoupling and $\ell^2$-refinements.** Bourgain–Demeter decoupling for the quartic hypersurface $\{(\xi,|\xi|^4)\}$ gives sharp $L^p$ Strichartz constants; several preprints attempt to convert these into negative-regularity multilinear bounds. *(frontier — verify)*
- **Random data.** Almost-sure local well-posedness below $s_c$ for randomized initial data is being developed by analogy with NLS/wave results, sidestepping the deterministic threshold entirely.

## 8. Future Work

1. Establish deterministic LWP in $H^s(\mathbb{R})$ for some $s<0$ — even $s>-\varepsilon$ would be the first sub-$L^2$ result on the line and would confirm that the NLS threshold $s^*=0$ is an artifact of Galilean symmetry.
2. Decide the mass-critical dimension $d=4$ for large non-radial data, defocusing and focusing (with the ground-state mass threshold).
3. Produce a norm-inflation example strictly above $s_c$, or prove none exists, by classifying the degenerate frequency interactions of $\Omega$.
4. Develop an $I$-method for $\Delta^2$ with a multiplier adapted to fourth-order dispersion to propagate low-regularity local solutions globally.
5. Transfer the periodic renormalization to the real line via a suitable Wick-type ordering on lattice-approximating tori.

## 9. Key References

- **[Foundational]** V. I. Karpman. *Stabilization of soliton instabilities by higher-order dispersion: Fourth-order nonlinear Schrödinger-type equations.* Physical Review E 53 (1996), R1336–R1339.
- **[Foundational]** V. I. Karpman, A. G. Shagalov. *Stability of solitons described by nonlinear Schrödinger-type equations with higher-order dispersion.* Physica D 144 (2000), 194–210.
- **[Foundational]** M. Ben-Artzi, H. Koch, J.-C. Saut. *Dispersion estimates for fourth order Schrödinger equations.* C. R. Acad. Sci. Paris Sér. I Math. 330 (2000), 87–92.
- **[Foundational]** C. E. Kenig, G. Ponce, L. Vega. *On the ill-posedness of some canonical dispersive equations.* Duke Mathematical Journal 106 (2001), 617–633.
- **[SOTA]** B. Pausader. *The cubic fourth-order Schrödinger equation.* Journal of Functional Analysis 256 (2009), 2473–2517.
- **[SOTA]** B. Pausader. *Global well-posedness for energy critical fourth-order Schrödinger equations in the radial case.* Dynamics of Partial Differential Equations 4 (2007), 197–225.
- **[SOTA]** B. Pausader, S. Shao. *The mass-critical fourth-order Schrödinger equation in high dimensions.* Journal of Hyperbolic Differential Equations 7 (2010), 651–705.
- **[SOTA]** C. Miao, G. Xu, L. Zhao. *Global well-posedness and scattering for the defocusing energy-critical nonlinear Schrödinger equations of fourth order in dimensions $d \ge 9$.* Journal of Differential Equations 251 (2011), 3381–3402.
- **[SOTA / Recent]** T. Oh, Y. Wang. *Global well-posedness of the periodic cubic fourth order NLS in negative Sobolev spaces.* Forum of Mathematics, Sigma 6 (2018), e5.
- **[SOTA / Recent]** M. Ruzhansky, B. Wang, H. Zhang. *Global well-posedness and scattering for the fourth order nonlinear Schrödinger equations with small data in modulation and Sobolev spaces.* Journal de Mathématiques Pures et Appliquées 105 (2016), 31–65.
- **[Recent]** V. D. Dinh. *On well-posedness, regularity and ill-posedness for the nonlinear fourth-order Schrödinger equation.* Bulletin of the Belgian Mathematical Society – Simon Stevin 25 (2018), 415–437.
- **[Related]** J. Segata. *Modified wave operators for the fourth-order non-linear Schrödinger-type equation with cubic non-linearity.* Mathematical Methods in the Applied Sciences 29 (2006), 1785–1800.
- **[Related]** M. Christ, J. Colliander, T. Tao. *Asymptotics, frequency modulation, and low regularity ill-posedness for canonical defocusing equations.* American Journal of Mathematics 125 (2003), 1235–1293.
- **[Survey]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes 10, AMS, 2003.
- **[Survey]** T. Tao. *Nonlinear Dispersive Equations: Local and Global Analysis.* CBMS Regional Conference Series in Mathematics 106, AMS, 2006.

## 10. Worked Example / Concrete Special Case

**Case $d=1$: proof of LWP in $L^2(\mathbb{R})$, and the exact size of the gap.**

*Step 1 — critical index.* $s_c = \tfrac12 - 2 = -\tfrac32$. So the conjecture asserts well-posedness for all $s>-3/2$, while the standard theory stops at $s=0$: a gap of $3/2$ derivatives.

*Step 2 — endpoint Strichartz.* With $d=1$, admissibility reads $4/q = \tfrac12 - \tfrac1r$. Taking $r=\infty$ gives $q=8$:

$$\|e^{it\partial_x^4}u_0\|_{L^8_tL^\infty_x} \lesssim \|u_0\|_{L^2_x}, \qquad \Big\|\int_0^t e^{i(t-t')\partial_x^4}F(t')\,dt'\Big\|_{L^\infty_TL^2_x \cap L^8_TL^\infty_x} \lesssim \|F\|_{L^1_TL^2_x}.$$

*Step 3 — contraction.* Set $\|u\|_{S_T} = \|u\|_{L^\infty_TL^2_x} + \|u\|_{L^8_TL^\infty_x}$ and $\Phi(u)(t) = e^{it\partial_x^4}u_0 - i\mu\int_0^t e^{i(t-t')\partial_x^4}(|u|^2u)(t')dt'$. Hölder in $x$ then in $t$ (using $\|\cdot\|_{L^2_T}\le T^{3/8}\|\cdot\|_{L^8_T}$):

$$\||u|^2u\|_{L^1_TL^2_x} \le \|u\|^2_{L^2_TL^\infty_x}\|u\|_{L^\infty_TL^2_x} \le T^{3/4}\|u\|^2_{L^8_TL^\infty_x}\|u\|_{L^\infty_TL^2_x} \le T^{3/4}\|u\|^3_{S_T}.$$

Hence $\|\Phi(u)\|_{S_T} \le C\|u_0\|_{L^2} + CT^{3/4}\|u\|^3_{S_T}$. On the ball $\|u\|_{S_T}\le 2C\|u_0\|_{L^2}=:2CR$, $\Phi$ is a contraction as soon as $CT^{3/4}(2CR)^2 \le \tfrac12$, i.e.

$$T \;\sim\; \|u_0\|_{L^2}^{-8/3}.$$

The positive power of $T$ is the *subcritical gain*; it exists exactly because $0 > s_c$.

*Step 4 — where it breaks.* Repeat at $s<0$. Scaling $u_\lambda(t,x)=\lambda^2u(\lambda^4t,\lambda x)$ gives $\|u_\lambda(0)\|_{\dot H^s}=\lambda^{s+3/2}\|u_0\|_{\dot H^s}$, so for $-3/2<s<0$ small data at time scale $T$ still has room: scaling alone permits LWP. What fails is the trilinear bound. Take $u_0$ with $\hat u_0 = N^{-s}\mathbf 1_{[N,N+1]} + N^{-s}\mathbf 1_{[-N-1,-N]}$, so $\|u_0\|_{H^s}\sim 1$ while $\|u_0\|_{L^2}\sim N^{-s}\to\infty$. The interaction $\xi_1\approx N$, $\xi_2\approx -N$, $\xi_3\approx N$ outputs frequency $\approx N$ but the resonance $\Omega$ vanishes to high order on this configuration, so no $\langle\tau-\xi^4\rangle$ weight is gained and the $X^{s,b}$ norm of the Duhamel term grows like $N^{-2s}$. For $s<0$ this diverges; for $s=0$ it is bounded. That single divergent configuration — and no Galilean boost to convert it into an actual counterexample — is the whole content of the gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*