---
id: 06-pdes/derivative-nonlinear-schrodinger-global-solutions
title: "Derivative Nonlinear Schrodinger Global Solutions"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Solutions of the Derivative Nonlinear Schrödinger Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/derivative-nonlinear-schrodinger-global-solutions` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The derivative nonlinear Schrödinger equation (DNLS) on the line is

$$i\partial_t u + \partial_x^2 u = -\,i\,\partial_x\!\left(|u|^2 u\right), \qquad u(0,x)=u_0(x), \quad (t,x)\in\mathbb{R}\times\mathbb{R},$$

with $u$ complex-valued. **The problem:** do solutions with *arbitrarily large* initial data exist globally in time, or can the $H^1$ (or $L^2$-critical Sobolev) norm blow up in finite time?

For four decades the only global results required a mass restriction $\|u_0\|_{L^2}^2 < 2\pi$, later $4\pi$. The conjecture — that no mass restriction is needed, the restriction being an artifact of the coercivity proof rather than of the dynamics — was resolved affirmatively:

- **Bahouri–Perelman (2022):** global well-posedness in $H^{1/2}(\mathbb{R})$ for arbitrary data.
- **Harrop-Griffiths–Killip–Ntekoume–Vișan (2022):** global well-posedness in the scaling-critical space $L^2(\mathbb{R})$ for arbitrary data.

A complete resolution requires: existence, uniqueness, continuous dependence on $u_0$ in the topology of the data space, and a global-in-time a priori bound, all uniform on bounded sets of data. What remains open is flagged in §6: the periodic problem at critical regularity, soliton resolution and large-data long-time asymptotics, unconditional uniqueness at low regularity, and the generalized DNLS with higher-power derivative nonlinearity, where blow-up does occur.

## 2. Mathematical Foundations

**Scaling.** If $u$ solves DNLS then so does $u_\lambda(t,x)=\lambda^{1/2}u(\lambda^2 t,\lambda x)$, and $\|u_\lambda\|_{L^2}=\|u\|_{L^2}$. Hence $L^2(\mathbb{R})=\dot H^0$ is the **critical** space: no scaling-subcritical margin exists, and DNLS is "mass-critical" in the sense of derivative-power counting.

**Conservation laws.** Smooth decaying solutions conserve

$$M(u)=\int_{\mathbb{R}}|u|^2\,dx,\qquad
P(u)=\Im\int_{\mathbb{R}}\bar u\,\partial_x u\,dx+\tfrac12\int_{\mathbb{R}}|u|^4\,dx,$$
$$E(u)=\int_{\mathbb{R}}|\partial_x u|^2\,dx+\tfrac32\,\Im\int_{\mathbb{R}}|u|^2\,\bar u\,\partial_x u\,dx+\tfrac12\int_{\mathbb{R}}|u|^6\,dx .$$

$E$ is **not** sign-definite: the cubic-in-$u$, first-order term has no fixed sign, so energy conservation alone gives no $H^1$ bound.

**Gauge transformation (Hayashi–Ozawa).** Set

$$v(t,x)=\mathcal{G}u:=u(t,x)\,\exp\!\Big(i\int_{-\infty}^{x}|u(t,y)|^2\,dy\Big).$$

Then $v$ solves the gauge-equivalent equation

$$i\partial_t v+\partial_x^2 v = -\,i\,v^2\,\partial_x\bar v+\tfrac12|v|^4 v ,$$

in which the worst nonlinear resonance (the derivative falling on the same-frequency factor) is removed. In the gauged variable the energy becomes a difference of definite terms,

$$E(u)=\|\partial_x v\|_{L^2}^2-\tfrac{1}{16}\|v\|_{L^6}^6 .$$

**Sharp Gagliardo–Nirenberg.** For $f\in H^1(\mathbb{R})$,
$$\|f\|_{L^6}^6\le \frac{4}{\pi^2}\,\|f\|_{L^2}^4\,\|\partial_x f\|_{L^2}^2,$$
with equality for the soliton profile; this constant produces the classical $2\pi$ mass threshold (§10).

**Complete integrability.** DNLS is the compatibility condition of the **Kaup–Newell** Lax pair, with $2\times2$ spectral problem $\partial_x\phi=\big(-i\zeta^2\sigma_3+\zeta Q(u)\big)\phi$, $Q(u)=\begin{psmallmatrix}0&u\\ -\bar u&0\end{psmallmatrix}$, $\sigma_3=\mathrm{diag}(1,-1)$. The equation possesses an infinite hierarchy of conservation laws and a two-parameter solitary-wave family
$$u_{\omega,c}(t,x)=\varphi_{\omega,c}(x-ct)\exp\!\Big(i\omega t+\tfrac{i}{2}c(x-ct)-\tfrac{3i}{4}\int_{-\infty}^{x-ct}\varphi_{\omega,c}^2\Big),\qquad -2\sqrt{\omega}<c\le 2\sqrt{\omega}.$$
The endpoint $c=2\sqrt\omega$ gives the **algebraic soliton**, with $\varphi$ decaying only like $|x|^{-1}$ and mass exactly $4\pi$.

## 3. History & State of the Art (SOTA)

- **1978.** Kaup and Newell exhibit the Lax pair and exact solutions; DNLS arises in plasma physics as the model for circularly polarized Alfvén waves propagating along a magnetic field (Mjølhus, Mio et al., 1976).
- **1992–1994.** Hayashi and Hayashi–Ozawa introduce the gauge transform and prove global well-posedness in $H^1(\mathbb{R})$ under $\|u_0\|_{L^2}^2<2\pi$.
- **1999.** Takaoka proves local well-posedness in $H^s(\mathbb{R})$ for $s\ge 1/2$ using $X^{s,b}$ spaces after gauging; Biagioni–Linares (2001) show the solution map fails to be uniformly continuous for $s<1/2$, so $s=1/2$ is the threshold for the standard contraction scheme.
- **2001–2002.** Takaoka ($s>32/33$) and Colliander–Keel–Staffilani–Takaoka–Tao (I-method, $s>1/2$) push global well-posedness below $H^1$ under the same $2\pi$ mass bound. Miao–Wu–Xu (2011) reach the endpoint $H^{1/2}$.
- **2013–2015.** Yifei Wu raises the threshold to $\|u_0\|_{L^2}^2<4\pi$ in $H^1$, using conservation of momentum together with mass and energy in a sharpened variational argument. The value $4\pi$ is exactly the mass of the algebraic soliton, making it the natural variational barrier.
- **2016–2018.** Inverse-scattering approaches: Liu–Perry–Sulem, Pelinovsky–Shimabukuro, and Jenkins–Liu–Perry–Sulem obtain global solutions in weighted Sobolev spaces for arbitrary mass under a **generic** spectral assumption (no spectral singularities / no eigenvalues), and derive long-time asymptotics.
- **2022 (resolution).** Bahouri–Perelman prove unconditional global well-posedness in $H^{1/2}(\mathbb{R})$ with no size restriction, via a profile-decomposition/compactness argument built on the integrable structure. Harrop-Griffiths, Killip, Ntekoume and Vișan then prove global well-posedness in the critical space $L^2(\mathbb{R})$ for arbitrary data, using commuting-flow and Hamiltonian-perturbation machinery (the "method of commuting flows" of Killip–Vișan) to obtain equicontinuity of orbits in $L^2$.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $H^1(\mathbb{R})$, $M(u_0)<2\pi$ | GWP | Hayashi 1993; Hayashi–Ozawa 1992 |
| $H^s(\mathbb{R})$, $s>1/2$, $M<2\pi$ | GWP (I-method) | CKSTT 2002 |
| $H^{1/2}(\mathbb{R})$, $M<2\pi$ | GWP | Miao–Wu–Xu 2011 |
| $H^1(\mathbb{R})$, $M<4\pi$ | GWP | Wu 2013, 2015 |
| $H^{2,2}$ weighted, generic spectral data, any mass | GWP + asymptotics | Jenkins–Liu–Perry–Sulem 2018 |
| $H^{1/2}(\mathbb{R})$, any mass | GWP, unconditional | Bahouri–Perelman 2022 |
| $L^2(\mathbb{R})$ (critical), any mass | GWP | Harrop-Griffiths–Killip–Ntekoume–Vișan 2022 |
| $H^s(\mathbb{T})$, $s\ge 1/2$ | LWP; GWP under mass restriction | Herr 2006; Mosincat–Oh |
| Solitons $\varphi_{\omega,c}$, $-2\sqrt\omega<c<2\sqrt\omega$ | orbital stability in $H^1$ | Colin–Ohta 2006 |
| $c=2\sqrt\omega$ (algebraic soliton) | stability at the degenerate endpoint | Kwon–Wu 2018 |
| gDNLS $i\partial_t u+\partial_x^2u=-i|u|^{2\sigma}\partial_x u$, $\sigma>1$ | finite-time blow-up exists | Liu–Simpson–Sulem 2013 |

## 5. Principal Obstacles

- **No sign-definite energy.** $E(u)$ mixes a positive $\|\partial_x u\|_{L^2}^2$ with a cubic term of indefinite sign. Every classical global-existence argument therefore needs a coercivity inequality, and coercivity holds only below a mass threshold. Above $4\pi$ the standard functional genuinely fails to be positive — the obstruction is real, not merely technical, at the level of the method.
- **Criticality.** $L^2$ is scaling-critical, so there is no room for a subcritical local theory plus conservation. Local existence time depends on the *profile* of $u_0$, not just its norm, and iteration cannot be closed by conservation alone.
- **Derivative loss.** The nonlinearity $\partial_x(|u|^2u)$ costs one derivative, which the Schrödinger group cannot recover: the $1/2$-derivative local smoothing gain of Kenig–Ponce–Vega is not enough for a naive contraction. The gauge transform removes the leading resonance but is nonlocal and only conditionally invertible at low regularity.
- **Non-uniform continuity below $H^{1/2}$.** Biagioni–Linares: Galilean-type modulation of soliton parameters destroys uniform continuity of the data-to-solution map in $H^s$, $s<1/2$, killing all perturbative approaches there.
- **Inverse scattering is not robust.** The Kaup–Newell scattering transform gives exact information but requires decay (weighted spaces) and generic spectral data; solitons and spectral singularities are exactly the non-generic cases, and the map from data to scattering data is not continuous in $L^2$.

The 2022 breakthroughs bypass rather than solve the coercivity problem: they replace it with **equicontinuity** of the orbit, proved from a one-parameter family of commuting Hamiltonian flows (an integrability input) or from concentration-compactness plus rigidity.

## 6. The Gap

Between §4 and §1 the remaining gap on the line has closed for **existence and uniqueness**, but not for **dynamics**:

1. **Soliton resolution.** Is every large $L^2$ solution asymptotically a superposition of solitons plus radiation? Proved only for generic weighted-Sobolev data (Jenkins–Liu–Perry–Sulem); unknown for general $L^2$ or $H^{1/2}$ data, including data supporting eigenvalue collisions.
2. **Periodic critical case.** GWP for arbitrary data in $L^2(\mathbb{T})$ or $H^{1/2}(\mathbb{T})$ — the commuting-flow argument uses dispersive decay on $\mathbb{R}$ and does not transfer.
3. **Below $L^2$.** For $s<0$, the equation is expected to be ill-posed in the norm-inflation sense; a proof at every negative $s$ is not complete.
4. **Non-integrable robustness.** Both proofs use complete integrability. No purely PDE argument (energy/virial/Morawetz) currently gives large-data global existence, so perturbations of DNLS remain open.

## 7. Current Research (as of June 2026)

- **Commuting-flow school** (UCLA/UCSD: Killip, Vișan, Harrop-Griffiths, Ntekoume). Extension of the $L^2$ argument to modified/Chen–Lee–Liu variants of DNLS and to sharp low-regularity thresholds; work on the same method for the periodic problem. *(frontier — verify)*
- **Bahouri–Perelman program** (Paris / Johns Hopkins). Refinement of the profile decomposition to yield quantitative growth bounds and to handle non-generic scattering data. *(frontier — verify)*
- **Riemann–Hilbert analysis** (Perry, Sulem, Pelinovsky, Saalmann). Long-time asymptotics through soliton–soliton and soliton–radiation interaction regimes, including the algebraic-soliton limit and $\bar\partial$-steepest-descent methods at low regularity.
- **Stability theory.** Multi-soliton stability and the degenerate endpoint $c=2\sqrt\omega$; interaction of the $4\pi$ threshold with orbital stability constants (Ohta, Kwon, Wu, Ning).
- **Blow-up for gDNLS.** Numerical and analytical study of finite-time singularity formation for $\sigma>1$, including rate and profile, where the integrable structure is absent (Liu–Simpson–Sulem; Hayashi–Ozawa follow-ups).

## 8. Future Work

- Prove soliton resolution for arbitrary $L^2(\mathbb{R})$ data, combining the equicontinuity machinery with $\bar\partial$-Riemann–Hilbert asymptotics.
- Find a **non-integrable** proof of large-data global existence — e.g. a virial/Morawetz functional or an interaction-type monotonicity that replaces the $4\pi$ coercivity — which would make the result stable under perturbation of the nonlinearity.
- Settle GWP for large data on $\mathbb{T}$ at $s=1/2$ and $s=0$.
- Determine sharp ill-posedness thresholds for $s<0$ (norm inflation, non-existence of a continuous flow).
- Quantify growth of higher Sobolev norms: is $\sup_t\|u(t)\|_{H^s}<\infty$ for all $s\ge1$ and all data, or can $H^s$ norms grow polynomially?
- Analyze blow-up rate and profile for gDNLS with $\sigma>1$, and locate the transition in $\sigma$ between global existence and singularity formation.

## 9. Key References

- **[Foundational]** D. J. Kaup, A. C. Newell. *An exact solution for a derivative nonlinear Schrödinger equation.* Journal of Mathematical Physics **19** (1978), 798–801. [DOI](https://doi.org/10.1063/1.523737)
- **[Foundational]** N. Hayashi, T. Ozawa. *On the derivative nonlinear Schrödinger equation.* Physica D **55** (1992), 14–36.
- **[Foundational]** N. Hayashi. *The initial value problem for the derivative nonlinear Schrödinger equation in the energy space.* Nonlinear Analysis **20** (1993), 823–833. [DOI](https://doi.org/10.1016/0362-546x(93)90071-y)
- **[Local theory]** H. Takaoka. *Well-posedness for the one-dimensional nonlinear Schrödinger equation with the derivative nonlinearity.* Advances in Differential Equations **4** (1999), 561–580. [DOI](https://doi.org/10.57262/ade/1366031032)
- **[Local theory]** H. A. Biagioni, F. Linares. *Ill-posedness for the derivative Schrödinger and generalized Benjamin–Ono equations.* Transactions of the AMS **353** (2001), 3649–3659. [DOI](https://doi.org/10.1090/s0002-9947-01-02754-4)
- **[Global, subcritical mass]** J. Colliander, M. Keel, G. Staffilani, H. Takaoka, T. Tao. *A refined global well-posedness result for Schrödinger equations with derivative.* SIAM Journal on Mathematical Analysis **34** (2002), 64–86. [DOI](https://doi.org/10.1137/s0036141001394541)
- **[SOTA threshold]** Y. Wu. *Global well-posedness for the nonlinear Schrödinger equation with derivative in energy space.* Analysis & PDE **6** (2013), 1989–2002. [DOI](https://doi.org/10.2140/apde.2013.6.1989)
- **[SOTA threshold]** Y. Wu. *Global well-posedness on the derivative nonlinear Schrödinger equation.* Analysis & PDE **8** (2015), 1101–1112. [DOI](https://doi.org/10.2140/apde.2015.8.1101)
- **[Integrable methods]** R. Jenkins, J. Liu, P. Perry, C. Sulem. *Global well-posedness for the derivative nonlinear Schrödinger equation.* Communications in Partial Differential Equations **43** (2018), 1151–1195.
- **[Integrable methods]** D. Pelinovsky, Y. Shimabukuro. *Existence of global solutions to the derivative NLS equation with the inverse scattering transform method.* International Mathematics Research Notices **2018**, 5663–5728. [DOI](https://doi.org/10.1093/imrn/rnx051)
- **[Resolution]** H. Bahouri, G. Perelman. *Global well-posedness for the derivative nonlinear Schrödinger equation.* Inventiones Mathematicae **229** (2022), 639–688. [DOI](https://doi.org/10.1007/s00222-022-01113-0)
- **[Resolution, critical space]** B. Harrop-Griffiths, R. Killip, M. Ntekoume, M. Vișan. *Global well-posedness for the derivative nonlinear Schrödinger equation in $L^2(\mathbb{R})$.* arXiv:2204.12548 (2022).
- **[Stability]** M. Colin, M. Ohta. *Stability of solitary waves for derivative nonlinear Schrödinger equation.* Annales de l'IHP – Analyse Non Linéaire **23** (2006), 753–764.
- **[Blow-up, generalized]** X. Liu, G. Simpson, C. Sulem. *Stability of solitary waves for a generalized derivative nonlinear Schrödinger equation.* Journal of Nonlinear Science **23** (2013), 557–583. [DOI](https://doi.org/10.1007/s00332-012-9161-2)

## 10. Worked Example / Concrete Special Case

**Goal:** derive the classical $2\pi$ threshold — the exact point where the pre-2013 method stops.

Take $u_0\in H^1(\mathbb{R})$ and let $v=\mathcal{G}u$ be the gauged solution. The gauge is an $L^2$-isometry: $|v|=|u|$ pointwise, so $M(v)=M(u)=:m$. Rewriting the energy in $v$ eliminates the indefinite cubic term and leaves

$$E(u)=\|\partial_x v\|_{L^2}^2-\tfrac1{16}\|v\|_{L^6}^6 .$$

Apply the sharp Gagliardo–Nirenberg inequality with $f=v(t)$:

$$\tfrac1{16}\|v\|_{L^6}^6 \;\le\; \tfrac1{16}\cdot\frac{4}{\pi^2}\,\|v\|_{L^2}^4\,\|\partial_x v\|_{L^2}^2 \;=\;\frac{m^2}{4\pi^2}\,\|\partial_x v\|_{L^2}^2 .$$

Therefore, for every $t$ in the maximal interval of existence,

$$E(u_0)=E(u(t))\;\ge\;\Big(1-\frac{m^2}{4\pi^2}\Big)\|\partial_x v(t)\|_{L^2}^2 .$$

If $m=\|u_0\|_{L^2}^2<2\pi$ — note $m$ here denotes $\|u_0\|_{L^2}^2$ in the normalization $\|v\|_{L^2}^4=m^2$ — the bracket $\delta:=1-\frac{m^2}{4\pi^2}$ is strictly positive and

$$\|\partial_x v(t)\|_{L^2}^2\le \delta^{-1}E(u_0)\quad\text{for all }t,$$

a uniform a priori $\dot H^1$ bound. Undoing the gauge costs only $L^2$-controlled factors ($\|\partial_x u\|_{L^2}\lesssim \|\partial_x v\|_{L^2}+\|u\|_{L^2}^5$ by Gagliardo–Nirenberg), so $\|u(t)\|_{H^1}$ stays bounded and Takaoka's local theory iterates forever. **Global existence for $\|u_0\|_{L^2}^2<2\pi$.**

**Where it breaks.** At $m=2\pi$ the constant $\delta$ vanishes; for $m>2\pi$ the right-hand side is negative and the inequality is vacuous. Wu's refinement adds the conserved momentum $P(u)$: minimizing the combined functional $E(u)+\omega M(u)+cP(u)$ over the soliton family shows the true variational obstruction sits at the algebraic soliton, whose mass is
$$\|\varphi_{\omega,2\sqrt\omega}\|_{L^2}^2=4\pi,$$
lifting the threshold from $2\pi$ to $4\pi$. Since no solution actually blows up (Bahouri–Perelman; Harrop-Griffiths–Killip–Ntekoume–Vișan), even $4\pi$ is an artifact: the correct global statement replaces the coercivity bound by equicontinuity of the orbit $\{u(t)\}_{t\in\mathbb{R}}$ in $L^2$, obtained from the commuting Hamiltonian flows of the Kaup–Newell hierarchy.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*