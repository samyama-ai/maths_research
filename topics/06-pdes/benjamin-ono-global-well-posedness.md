---
id: 06-pdes/benjamin-ono-global-well-posedness
title: "Benjamin Ono Global Well Posedness"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Benjamin–Ono Global Well-Posedness at Optimal Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/benjamin-ono-global-well-posedness` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Benjamin–Ono (BO) equation

$$\partial_t u + \mathcal{H}\partial_x^2 u + u\,\partial_x u = 0, \qquad u(0,\cdot)=u_0, \qquad u:\mathbb{R}_t\times M \to \mathbb{R},\; M\in\{\mathbb{R},\mathbb{T}\},$$

with $\mathcal{H}$ the Hilbert transform, models internal waves in a stratified fluid of infinite depth. The problem: **determine the sharp Sobolev exponent $s$ for which the Cauchy problem is globally well-posed in $H^s(M)$** — existence, uniqueness, and continuity of the data-to-solution map $u_0\mapsto u$ on $H^s$, for arbitrarily large data and arbitrarily long times.

The scaling $u_\lambda(t,x)=\lambda u(\lambda^2 t,\lambda x)$ preserves solutions on $\mathbb{R}$ and fixes $\dot H^{-1/2}$, so $s_c=-1/2$ is the critical exponent, and $s>-1/2$ is the conjectured optimal range. A complete resolution requires (i) global-in-time well-posedness for every $s>-1/2$, and (ii) a proof that no reasonable solution map extends continuously to $H^s$ for $s<-1/2$.

Both halves are now theorems: **Killip–Laurens–Vişan (2024)** on $\mathbb{R}$ and $\mathbb{T}$, and **Gérard–Kappeler–Topalov (2023)** on $\mathbb{T}$. The page is retained as *solved-recently* because the endpoint $s=-1/2$, unconditional uniqueness at low regularity, and robustness under perturbation of the integrable structure remain open.

## 2. Mathematical Foundations

**Hilbert transform.** $\widehat{\mathcal{H}f}(\xi) = -i\,\operatorname{sgn}(\xi)\hat f(\xi)$, equivalently $\mathcal{H}f(x)=\frac{1}{\pi}\,\mathrm{p.v.}\!\int \frac{f(y)}{x-y}\,dy$. Then $\mathcal{H}\partial_x^2 = -|D|\partial_x$, and the linear dispersion relation is $\omega(\xi)=\xi|\xi|$, group velocity $\omega'(\xi)=2|\xi|$ — only **one derivative** of smoothing, versus two for KdV.

**Conservation laws.** BO is completely integrable with a Lax pair on the Hardy space $L^2_+ = \{f : \operatorname{supp}\hat f\subset[0,\infty)\}$. Writing $u=\Pi_+u+\overline{\Pi_+u}$, the Lax operator is
$$L_u = D - T_u, \qquad D=-i\partial_x,\quad T_u f = \Pi_+(uf),$$
acting on $L^2_+$; then $\partial_t L_u = [B_u, L_u]$ with $B_u = i(D^2 - 2T_uD - iT_{\partial_x u} \cdots)$ (Nakamura 1979, Fokas–Ablowitz 1983). Classical invariants:
$$M(u)=\int u\,dx,\qquad P(u)=\tfrac12\int u^2dx,\qquad E(u)=\tfrac12\int \big||D|^{1/2}u\big|^2dx-\tfrac16\int u^3dx,$$
with $E$ controlling $H^{1/2}$, and a full hierarchy controlling $H^{n/2}$.

**Low-regularity conservation.** Talbut (2021) constructed a family $\{\alpha(\kappa;u)\}_{\kappa\gg1}$ of conserved quantities with
$$\alpha(\kappa;u)\;\approx\;\int \frac{|\hat u(\xi)|^2}{\kappa+|\xi|}\,d\xi \;\sim\; \kappa^{2s-1}\|u\|_{H^s}^2$$
for $-1/2<s<0$, giving **a priori** $H^s$ bounds down to $s=-1/2$. These come from the perturbation determinant $\det\!\big(1+\kappa^{-1}T_u(L_u+\kappa)^{-1}\big)$.

**Explicit formula (Gérard 2023).** For $u_0\in L^2(\mathbb{R})$ with $\Pi_+$ projection, the solution satisfies
$$\Pi_+u(t,z) \;=\; \frac{1}{2\pi i}\,\Big\langle \big(L_{u_0}+ \tfrac{t}{2\pi}\,\cdots - z\big)^{-1}\Pi_+u_0,\ \Pi_+ \mathbf{1}\Big\rangle \quad (\Im z>0),$$
an exact resolvent representation of the flow in terms of the Lax operator at time $0$ — the BO analogue of the inverse-scattering formula, valid without smallness.

## 3. History & State of the Art

- **1967 / 1975.** Benjamin derives the equation for internal waves in a deep stratified fluid; Ono exhibits the algebraic solitary wave.
- **1979–1983.** Nakamura, Fokas–Ablowitz, Case establish integrability, the Lax pair, and multi-soliton formulas.
- **1986–1991.** Iório: local well-posedness (LWP) in $H^s$, $s>3/2$, by energy methods; Ponce: global well-posedness (GWP) at $s=3/2$.
- **2001.** Molinet–Saut–Tzvetkov: the flow map is **not** $C^2$ (indeed not uniformly continuous) on $H^s(\mathbb{R})$ for **any** $s\in\mathbb{R}$. Perturbative/Picard iteration is dead for BO at every regularity.
- **2003.** Koch–Tzvetkov ($s>5/4$) and Kenig–Koenig ($s>9/8$) push the energy method with local smoothing and refined Strichartz.
- **2004.** Tao's **gauge transformation** $w = \Pi_+(e^{-iF/2}u)$, $\partial_x F=u$, removes the worst high–low interaction; GWP in $H^1(\mathbb{R})$.
- **2007–2008.** Ionescu–Kenig: GWP in $L^2(\mathbb{R})$ (JAMS), in gauge-adapted $\bar F^0$ spaces. Burq–Planchon: $s>1/4$. Molinet: GWP in $L^2(\mathbb{T})$.
- **2012–2019.** Molinet–Pilod simplify the $L^2$ theory and get unconditional uniqueness for $s>1/4$; Ifrim–Tataru give a normal-form/testing-by-wave-packets proof with long-time dispersive decay for small data.
- **2021–2023.** Gérard–Kappeler construct global Birkhoff coordinates on $\mathbb{T}$ (CPAM 2021); Gérard–Kappeler–Topalov prove sharp well-posedness on $H^s(\mathbb{T})$ for $s>-1/2$ and ill-posedness below (Acta Math. 2023). Gérard's explicit formula appears for both $\mathbb{R}$ and $\mathbb{T}$.
- **2024.** Killip–Laurens–Vişan, *Sharp well-posedness for the Benjamin–Ono equation* (Invent. Math.): GWP in $H^s$, $-1/2<s<0$, on **both** the line and the circle, via the **commuting-flow method**.

## 4. Partial Results / Verified Cases

| Setting | Range | Author(s) |
|---|---|---|
| $\mathbb{R}$, LWP energy method | $s>3/2$ | Iório 1986 |
| $\mathbb{R}$, GWP | $s\ge 3/2$ | Ponce 1991 |
| $\mathbb{R}$, LWP | $s>9/8$ | Kenig–Koenig 2003 |
| $\mathbb{R}$, GWP gauge | $s\ge1$ | Tao 2004 |
| $\mathbb{R}$, GWP | $s\ge0$ ($L^2$) | Ionescu–Kenig 2007 |
| $\mathbb{T}$, GWP | $s\ge0$ | Molinet 2008 |
| $\mathbb{R}$, unconditional uniqueness | $s>1/4$ | Molinet–Pilod 2012 |
| $\mathbb{R}$, a priori bounds | $s>-1/2$ | Talbut 2021 |
| $\mathbb{T}$, sharp GWP + ill-posedness | $s>-1/2$ / $s<-1/2$ | Gérard–Kappeler–Topalov 2023 |
| $\mathbb{R}$ and $\mathbb{T}$, sharp GWP | $-1/2<s<0$ | Killip–Laurens–Vişan 2024 |

Also solved: soliton orbital stability in $H^{1/2}$ (Bennett et al.; Kenig–Martel), multi-soliton asymptotic stability, and the zero-dispersion limit via Gérard's formula. Unresolved cases include $s=-1/2$ exactly, and Fourier–Lebesgue or modulation-space data outside the $H^s$ scale.

## 5. Principal Obstacles

1. **Loss of derivative in the nonlinearity.** The transport term $u\partial_x u$ loses one derivative, exactly the amount the dispersion $\xi|\xi|$ can recover — so BO sits at the borderline where local smoothing gains half a derivative but the nonlinearity demands one.
2. **No contraction, at any regularity.** Molinet–Saut–Tzvetkov show the failure of $C^2$ dependence in every $H^s$: the high–low resonance $\hat u(\xi_{\rm low})\hat u(\xi_{\rm high})$ produces an unbounded phase, so $X^{s,b}$/Picard schemes cannot close. Every proof must be non-perturbative (gauge, normal form, or integrability).
3. **Gauge transform breaks below $L^2$.** Tao's gauge needs $\partial_x^{-1}u\in L^\infty$-type control; for $s<0$ the primitive $F$ is not even a function of bounded oscillation, and $e^{-iF/2}$ loses meaning.
4. **Energy methods have no coercive functional below $L^2$.** The hierarchy $\{E_n\}$ controls only $H^{n/2}$, $n\ge0$. Getting below $L^2$ required manufacturing new conserved quantities from the perturbation determinant — the analytic continuation of the Lax spectral data — which is only available *because* BO is integrable.
5. **Integrability is fragile.** All sharp results consume the Lax structure. A generic lower-order perturbation destroys it, and no known non-integrable technique reaches $s<0$.

## 6. The Gap

What is proven (Section 4) covers $s>-1/2$ on $\mathbb{R}$ and $\mathbb{T}$; what is conjectured (Section 1) is exactly that range, so the *scale gap is closed*. The residual gap is threefold:

- **The endpoint $s=-1/2$.** Solitons have $\|u_c\|_{\dot H^{-1/2}}$ independent of $c$ (Section 10), so the critical space carries a non-compact family of solutions at fixed norm; nothing rules out norm inflation exactly at $-1/2$, and nothing proves well-posedness there.
- **Uniqueness class.** GWP for $s<0$ is stated for the limit of smooth solutions; **unconditional** uniqueness in $C_tH^s$ is known only for $s>1/4$ (Molinet–Pilod). Whether every distributional solution in $C_tH^s$, $-1/2<s<1/4$, coincides with the constructed one is open.
- **Structural robustness.** No proof below $s=0$ survives perturbation of the Lax pair. The step to cross is a *non-integrable* mechanism replacing the perturbation-determinant conservation laws.

## 7. Current Research (as of June 2026)

- **Commuting-flow method (UCLA: Killip, Vişan; with Laurens, Ntekoume, Chapouto).** Approximate BO by an integrable flow generated by $\pm\log\det$ of the Lax resolvent, whose difference from BO is *smoothing*; the method has been transferred to KdV, NLS, mKdV and now the **intermediate long wave (ILW)** equation, where sharp $H^s$, $s>-1/2$, results uniform in the depth parameter are being established *(frontier — verify)*.
- **Explicit-formula school (Orsay: Gérard; Zurich/Bern: Kappeler† legacy, Topalov).** Using the resolvent formula to study the **zero-dispersion limit**, soliton resolution, and the structure of the BO flow on $L^2_+$; Gérard's formula yields weak limits described by a Lax-type variational principle.
- **Non-integrable robustness (Ifrim–Tataru, Berkeley/Toronto).** Wave-packet testing and modified energies for BO-type equations with variable coefficients or on domains with boundary; Laurens has treated the half-line and non-integrable perturbations at positive regularity.
- **Probabilistic and quasi-invariance directions.** Invariance of Gibbs-type and white-noise-adjacent measures on $\mathbb{T}$ under BO, built on Birkhoff coordinates *(frontier — verify)*.

## 8. Future Work

1. Settle $s=-1/2$: either construct a norm-inflation sequence from the soliton family plus radiation, or prove critical well-posedness in a Besov refinement $B^{-1/2}_{2,\infty}$-type space.
2. Extend unconditional uniqueness from $s>1/4$ to the whole well-posedness range, likely via normal-form-based estimates in $L^2$-based spaces.
3. Prove GWP below $L^2$ for BO with a non-integrable lower-order perturbation, isolating which part of the commuting-flow argument is genuinely structural.
4. Complete soliton resolution: show every $L^2$ solution decomposes asymptotically into multi-solitons plus dispersive radiation, using the explicit formula's spectral data.
5. Transfer the sharp theory to the two-dimensional and ILW/Benjamin-type analogues, and to the deep-water limit of full water-wave systems.

## 9. Key References

- **[Foundational]** T. B. Benjamin. *Internal waves of permanent form in fluids of great depth.* J. Fluid Mech. **29** (1967), 559–592. [DOI](https://doi.org/10.1017/s002211206700103x)
- **[Foundational]** H. Ono. *Algebraic solitary waves in stratified fluids.* J. Phys. Soc. Japan **39** (1975), 1082–1091. [DOI](https://doi.org/10.1143/jpsj.39.1082)
- **[Foundational]** R. J. Iório Jr. *On the Cauchy problem for the Benjamin–Ono equation.* Comm. Partial Differential Equations **11** (1986), 1031–1081. [DOI](https://doi.org/10.1080/03605308608820456)
- **[Obstruction]** L. Molinet, J.-C. Saut, N. Tzvetkov. *Ill-posedness issues for the Benjamin–Ono and related equations.* SIAM J. Math. Anal. **33** (2001), 982–988. [DOI](https://doi.org/10.1137/s0036141001385307)
- **[Breakthrough]** T. Tao. *Global well-posedness of the Benjamin–Ono equation in $H^1(\mathbb{R})$.* J. Hyperbolic Differ. Equ. **1** (2004), 27–49.
- **[Breakthrough]** A. D. Ionescu, C. E. Kenig. *Global well-posedness of the Benjamin–Ono equation in low-regularity spaces.* J. Amer. Math. Soc. **20** (2007), 753–798. [DOI](https://doi.org/10.1090/s0894-0347-06-00551-0)
- **[Periodic]** L. Molinet. *Global well-posedness in $L^2$ for the periodic Benjamin–Ono equation.* Amer. J. Math. **130** (2008), 635–683. [DOI](https://doi.org/10.1353/ajm.0.0001)
- **[Refinement]** L. Molinet, D. Pilod. *The Cauchy problem for the Benjamin–Ono equation in $L^2$ revisited.* Anal. PDE **5** (2012), 365–395. [DOI](https://doi.org/10.2140/apde.2012.5.365)
- **[Method]** M. Ifrim, D. Tataru. *Well-posedness and dispersive decay of small data solutions for the Benjamin–Ono equation.* Ann. Sci. Éc. Norm. Supér. **52** (2019), 297–335. [DOI](https://doi.org/10.24033/asens.2388)
- **[Integrability]** P. Gérard, T. Kappeler. *On the integrability of the Benjamin–Ono equation on the torus.* Comm. Pure Appl. Math. **74** (2021), 1685–1747. [DOI](https://doi.org/10.1002/cpa.21896)
- **[A priori bounds]** B. Talbut. *Low regularity conservation laws for the Benjamin–Ono equation.* Math. Res. Lett. **28** (2021), 889–905. [DOI](https://doi.org/10.4310/mrl.2021.v28.n3.a11)
- **[SOTA]** P. Gérard, T. Kappeler, P. Topalov. *Sharp well-posedness results of the Benjamin–Ono equation in $H^s(\mathbb{T},\mathbb{R})$ and qualitative properties of its solutions.* Acta Math. **231** (2023), 31–88. [DOI](https://doi.org/10.4310/acta.2023.v231.n1.a2)
- **[SOTA]** P. Gérard. *An explicit formula for the Benjamin–Ono equation.* Tunisian J. Math. **5** (2023), 593–603. [DOI](https://doi.org/10.2140/tunis.2023.5.593)
- **[SOTA]** R. Killip, T. Laurens, M. Vişan. *Sharp well-posedness for the Benjamin–Ono equation.* Invent. Math. **236** (2024), 999–1054. [DOI](https://doi.org/10.1007/s00222-024-01250-8)
- **[Survey]** J.-C. Saut. *Benjamin–Ono and intermediate long wave equations: modeling, IST and PDE.* In *Nonlinear Dispersive Partial Differential Equations and Inverse Scattering*, Fields Institute Communications **83**, Springer, 2019. [DOI](https://doi.org/10.1007/978-1-4939-9806-7_3)

## 10. Worked Example: the soliton family and the exponent $-1/2$

**Setup.** Seek $u(t,x)=\varphi(y)$, $y=x-ct$, for $\partial_t u+\mathcal{H}\partial_x^2u+u\partial_xu=0$. Substituting and integrating once (all terms vanish at $\infty$):
$$-c\varphi + \mathcal{H}\varphi' + \tfrac12\varphi^2 = 0 .$$

**Ansatz.** $\varphi(y)=\dfrac{A}{1+\lambda^2y^2}$, $\lambda>0$. Use the identity $\mathcal{H}\!\left[\frac{1}{1+x^2}\right]=\frac{x}{1+x^2}$ (boundary values of $i/(z+i)$, analytic in the upper half-plane), plus dilation-invariance $\mathcal{H}[g(\lambda\cdot)](y)=(\mathcal{H}g)(\lambda y)$. Then
$$\mathcal{H}\varphi'(y) = A\,\frac{d}{dy}\!\left[\frac{\lambda y}{1+\lambda^2y^2}\right] = A\,\frac{\lambda(1-\lambda^2y^2)}{(1+\lambda^2y^2)^2}.$$
Multiplying the profile equation by $(1+\lambda^2y^2)^2/A$:
$$-c(1+\lambda^2y^2) + \lambda(1-\lambda^2y^2) + \tfrac{A}{2}=0 .$$
Matching the $\lambda^2y^2$ coefficient gives $\lambda=-c$ (so $c<0$), and the constant term gives $A=2(c-\lambda)=4c$. Hence the exact solution
$$\boxed{\,u_c(t,x)=\frac{4c}{1+c^2(x-ct)^2}\,},\qquad c<0 .$$

**Norms.** With $z=|c|y$,
$$\|u_c\|_{L^2}^2 = 16c^2\!\int\!\frac{dy}{(1+c^2y^2)^2} = \frac{16c^2}{|c|}\cdot\frac{\pi}{2}=8\pi|c| .$$
Since $u_c(x)=|c|\,U(|c|x)$ with $U(z)=-4/(1+z^2)$ (at $t=0$), scaling gives for every $s$:
$$\|u_c\|_{\dot H^s} = |c|^{\,s+\frac12}\,\|U\|_{\dot H^s}.$$

**Why $-1/2$ is the threshold.** The exponent $s+\tfrac12$ changes sign exactly at $s=-1/2$:

- $s>-1/2$: $\|u_c\|_{\dot H^s}\to\infty$ as $|c|\to\infty$. Large solitons are large data — consistent with well-posedness.
- $s=-1/2$: $\|u_c\|_{\dot H^{-1/2}}=\|U\|_{\dot H^{-1/2}}$ for **all** $c$. A one-parameter family of solutions of identical critical norm, spreading over all scales — the classical signature of criticality.
- $s<-1/2$: $\|u_c\|_{\dot H^s}\to0$ as $|c|\to\infty$. Arbitrarily *small* data whose solitons travel at speed $|c|\to\infty$ and translate by $|c|t$ in time $t$, so $\|u_c(t)-u_c(0)\|_{H^s}\gtrsim\|u_c\|_{H^s}$ instantly: the flow map cannot be continuous at $0$. This is the mechanism behind the ill-posedness half of Gérard–Kappeler–Topalov.

The Killip–Laurens–Vişan theorem says the first bullet is not merely consistent but sufficient: for every $-1/2<s<0$ and every $u_0\in H^s(M)$, smooth approximations converge in $C_t H^s$ to a unique global solution, with the flow map continuous on $H^s$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*