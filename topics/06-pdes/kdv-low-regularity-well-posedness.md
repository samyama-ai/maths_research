---
id: 06-pdes/kdv-low-regularity-well-posedness
title: "KdV Low Regularity Well Posedness"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# KdV Low Regularity Well-Posedness

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/kdv-low-regularity-well-posedness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the Korteweg–de Vries (KdV) initial value problem
$$\partial_t u + \partial_x^3 u + 6\,u\,\partial_x u = 0, \qquad u(0,\cdot)=u_0 \in H^s(\mathcal{M}), \qquad \mathcal{M}\in\{\mathbb{R},\mathbb{T}\},$$
with $u$ real valued. **The problem:** determine the exact set of exponents $s$ for which the Cauchy problem is well posed, and in which sense.

Three inequivalent notions are in play:

- **(WP-A)** Existence, uniqueness in a stated class, and *continuous* dependence $u_0\mapsto u$ on $H^s$.
- **(WP-B)** Uniformly continuous (equivalently, for KdV, real-analytic) dependence — what any contraction/Picard scheme delivers.
- **(WP-C)** The solution map on Schwartz data extends *continuously* from $H^s\cap\mathcal{S}$ to $H^s$; solutions are limits of classical ones.

The scaling $u\mapsto \lambda^2u(\lambda^3t,\lambda x)$ leaves KdV invariant and fixes $\dot H^{-3/2}$, so $s_c=-3/2$ is the critical exponent and no notion of well-posedness is expected below it. Sharp thresholds are known: $s\ge -1$ for (WP-A)/(WP-C), $s\ge -3/4$ for (WP-B). A full resolution requires either (i) constructing a meaningful solution theory on $-3/2\le s<-1$ in some weaker class (distributional solutions, uniqueness classes, a.s. well-posedness on a measure, or non-Sobolev scales), or (ii) proving that no such theory exists down to $s_c$. A second, arguably harder, component: obtain the same thresholds without using complete integrability.

## 2. Mathematical Foundations

**Function spaces.** $H^s(\mathcal M)$ with $\|f\|_{H^s}^2=\int\langle\xi\rangle^{2s}|\hat f(\xi)|^2\,d\xi$ (sum over $\xi\in\mathbb Z$ on $\mathbb T$). Bourgain's dispersive spaces $X^{s,b}$ are defined by
$$\|u\|_{X^{s,b}}=\big\|\langle\xi\rangle^{s}\langle\tau-\xi^{3}\rangle^{b}\,\tilde u(\tau,\xi)\big\|_{L^2_{\tau,\xi}},$$
$\tilde u$ the space-time Fourier transform. Fourier–Lebesgue spaces $\widehat{H^s_r}$, $\|f\|=\|\langle\xi\rangle^s\hat f\|_{L^{r'}}$, provide an alternative scale.

**Resonance function.** Writing $\xi=\xi_1+\xi_2$, the trilinear resonance is
$$\Omega(\xi_1,\xi_2)=\xi^{3}-\xi_1^{3}-\xi_2^{3}=3\,\xi_1\xi_2(\xi_1+\xi_2).$$
Smallness of $\Omega$ measures how badly the nonlinearity resonates. Note $\Omega$ vanishes when $\xi_1+\xi_2=0$: **high–high interactions producing low output frequency are exactly resonant**. This single algebraic fact drives every threshold below.

**Conservation laws.** $\int u$, $M(u)=\int u^2$, and $H(u)=\int(\tfrac12 u_x^2-u^3)$ control $L^2$ and $H^1$. Below $L^2$ they are useless. Integrability supplies a replacement: KdV is the isospectral flow of $L=-\partial_x^2+u$ (Lax pair), and Killip–Vişan–Zhang showed the perturbation determinant of $L$ generates, for $\kappa$ large, a conserved quantity $A(\kappa;u)$ with
$$A(\kappa;u)\;\approx\;\int \frac{|\hat u(\xi)|^{2}}{4\kappa^{2}+\xi^{2}}\,d\xi \;\approx_\kappa\; \|u\|_{H^{-1}}^{2}$$
uniformly on balls of $H^{-1}$. This is the *a priori* bound that makes $H^{-1}$ reachable.

**Miura map.** $u=v_x+v^2$ (or $v^2-v_x$) maps mKdV solutions to KdV solutions and transfers $H^{s}$ mKdV theory to $H^{s-1}$ KdV theory.

## 3. History & State of the Art (SOTA)

- **1895** Korteweg and de Vries derive the equation for shallow-water waves.
- **1967–75** Inverse scattering (Gardner–Greene–Kruskal–Miura); classical well-posedness in $H^s$, $s\ge 2$ (Temam; Bona–Smith 1975; Kato 1983 with the local smoothing effect).
- **1993** Kenig–Ponce–Vega, via local smoothing and maximal-function estimates, reach $s>3/4$ on $\mathbb R$. Bourgain introduces $X^{s,b}$ spaces and obtains local (hence global) well-posedness in $L^2(\mathbb R)$ and $L^2(\mathbb T)$ with analytic data dependence.
- **1996** Kenig–Ponce–Vega prove the sharp bilinear estimate $\|\partial_x(uv)\|_{X^{s,-1/2}}\lesssim\|u\|_{X^{s,1/2}}\|v\|_{X^{s,1/2}}$ for $s>-3/4$, giving local well-posedness on $\mathbb R$ for $s>-3/4$ and $s\ge-1/2$ on $\mathbb T$.
- **2001–03** Colliander–Keel–Staffilani–Takaoka–Tao introduce the $I$-method and prove global well-posedness for $s>-3/4$ ($\mathbb R$) and $s\ge-1/2$ ($\mathbb T$). Christ–Colliander–Tao show the data-to-solution map is not uniformly continuous below $-3/4$ on $\mathbb R$, so (WP-B) is settled sharply.
- **2006** Kappeler–Topalov, using Birkhoff coordinates for periodic KdV, prove global well-posedness in $H^{-1}(\mathbb T)$ in sense (WP-C).
- **2009** Guo and, independently, Kishimoto reach the endpoint $s=-3/4$ on $\mathbb R$ (global, with modified $X^{s,b}$ and $\bar F^s$-type spaces).
- **2011–12** Molinet proves sharpness: for $s<-1$ the flow map on $\mathbb T$ (and on $\mathbb R$) admits no continuous extension.
- **2015** Buckmaster–Koch construct $H^{-1}(\mathbb R)$ solutions as limits of smooth ones.
- **2019** Killip–Vişan, *KdV is well-posed in $H^{-1}$* (Annals of Mathematics), close the line case by the **method of commuting flows**: approximate KdV by an integrable, $H^{-1}$-tractable flow $H_\kappa$ generated by the perturbation determinant, and pass $\kappa\to\infty$. Combined with Molinet, $s=-1$ is sharp on both $\mathbb R$ and $\mathbb T$ for (WP-A)/(WP-C).

## 4. Partial Results / Verified Cases

| Setting | Threshold | Sense | Reference |
|---|---|---|---|
| $\mathbb R$, $s\ge -1$ | global | (WP-A)/(WP-C) | Killip–Vişan 2019 |
| $\mathbb T$, $s\ge -1$ | global | (WP-C) | Kappeler–Topalov 2006 |
| $\mathbb R$, $s\ge -3/4$ | global, analytic map | (WP-B) | KPV 1996; CKSTT 2003; Guo, Kishimoto 2009 |
| $\mathbb T$, $s\ge -1/2$ | global, analytic map | (WP-B) | Bourgain 1993; CKSTT 2003 |
| $\mathbb R$, $s<-3/4$ | flow not uniformly continuous on bounded sets | — | Christ–Colliander–Tao 2003 |
| $\mathbb R$ and $\mathbb T$, $s<-1$ | flow map has no continuous extension | ill-posed | Molinet 2011, 2012 |
| White-noise data on $\mathbb R$ (regularity $-1/2^-$ locally, not in $H^{-1}(\mathbb R)$) | global flow, measure invariant | a.s. | Killip–Murphy–Vişan 2020 |
| Fourier–Lebesgue $\widehat{H^s_r}$ | well-posed for suitable $(s,r)$ reaching below the $H^{-3/4}$ barrier | analytic | Grünrock 2004; Christ 2005 |

Global-in-time is automatic once local theory plus the conserved $A(\kappa;\cdot)$ (or Birkhoff coordinates on $\mathbb T$) gives an $H^{-1}$ *a priori* bound. Companion sharp results: mKdV on $\mathbb R$ is well posed in $H^s$, $s>-1/2$ (Harrop-Griffiths–Killip–Vişan), matching the Miura correspondence.

## 5. Principal Obstacles

- **Resonant high–high $\to$ low interactions.** With $\Omega=3\xi_1\xi_2\xi$, output at frequency $|\xi|\ll N$ from inputs at $\pm N$ carries modulation $\sim N^2|\xi|$, which degenerates as $\xi\to0$. Negative Sobolev weights *reward* low output frequencies, so the derivative in $\partial_x(u^2)$ cannot compensate. This is precisely what breaks the KPV bilinear estimate at $s=-3/4$ and cannot be repaired inside any $X^{s,b}$-type space.
- **Picard iteration is structurally dead below $-3/4$.** Christ–Colliander–Tao's counterexamples show the second Picard iterate is unbounded relative to the data; since analytic dependence would force iterate bounds, *no* contraction argument, in any Banach space embedding in $H^s$ with $s<-3/4$, can work. Progress to $H^{-1}$ therefore had to abandon fixed-point methods entirely.
- **No coercive classical conservation law below $L^2$.** The only known $H^{-1}$-level *a priori* bound is the perturbation determinant of the Lax operator. It is an artifact of integrability, needs $u$ small in $H^{-1}$ (or a scaling/steps argument), and has no analogue for perturbed equations.
- **Passage to the limit in $u\partial_x u$.** For $u\in H^{-1}$, $u^2$ is not a distribution by any product rule; the nonlinearity has to be interpreted through the flow (commuting flows) or via Birkhoff coordinates, not directly.
- **Compactness fails.** Weak $H^{-1}$ convergence of data does not give convergence of $u^2$; concentration at high frequency is exactly the scaling degeneracy of $s_c=-3/2$.

## 6. The Gap

Two gaps, of different character.

1. **$-3/2 \le s < -1$.** Molinet rules out any *continuous* $H^s$ solution map here, so the question is not "is it well posed" but "what survives": Do limits of smooth solutions exist (perhaps non-uniquely)? Is there a weaker topology, a non-Sobolev scale, or a probability measure on $H^{s}$ for which a flow exists? The one-parameter soliton family (Section 10) is bounded in $\dot H^{-3/2}$ with speeds diverging — the concrete mechanism obstructing any uniformly continuous flow there. Nothing rules out an $L^p$-based or Fourier–Lebesgue theory down to scaling.
2. **Integrability dependence.** Every result at $s<-3/4$ on $\mathbb R$ uses the Lax pair. For $\partial_t u+\partial_x^3u+6uu_x = N(u)$ with a non-integrable perturbation, or variable-coefficient dispersion, the best known thresholds remain at the Picard barrier $-3/4$. Crossing from $-3/4$ to $-1$ by robust (non-integrable) means is the sharpest open technical step.

## 7. Current Research (as of June 2026)

- **Method of commuting flows** (Killip, Vişan, Bringmann, Harrop-Griffiths, and collaborators at UCLA/Bonn) is the dominant technique: applied to mKdV, cubic NLS, fifth-order KdV, and derivative NLS. Extensions to $H^{-1}$-level theory for the full KdV hierarchy and for KdV with steplike/non-decaying data are active. *(frontier — verify)*
- **Non-Sobolev scales.** Chapouto, Forlano, Oh, and Grünrock-school work on Fourier–Lebesgue and modulation spaces aims at the range beyond $H^{-3/4}$ with analytic dependence; sharpness in the $(s,r)$-plane is not settled. *(frontier — verify)*
- **Probabilistic well-posedness.** Invariance of white noise (Quastel–Valkó, Oh, Killip–Murphy–Vişan) and Gibbs-type measures gives almost-sure flows on data rougher than any deterministic threshold; the open question is whether a.s. theory can be pushed to measures supported near $H^{-3/2}$. *(frontier — verify)*
- **Unconditional uniqueness.** Normal-form / infinite-iteration methods (Kwon–Oh–Yoon) give uniqueness in $C_tH^s$ without auxiliary spaces for restricted $s$; unconditional uniqueness at the endpoint $s=-1$ is not established. *(frontier — verify)*
- **Robust low-regularity theory for perturbed KdV** via modified energies and paradifferential normal forms (Molinet, Vento, Pilod, Ifrim–Tataru).

## 8. Future Work

- Decide whether the *deterministic* $H^{-1}$ threshold is genuinely the end of the story, or whether limits of smooth solutions exist (non-uniquely) for $-3/2\le s<-1$; a convex-integration-style non-uniqueness construction for rough KdV would settle the negative side.
- Replace the perturbation determinant by a *modified energy* argument surviving perturbations of the nonlinearity — Ifrim–Tataru's normal-form/energy program is the leading candidate.
- Determine the sharp $(s,r)$ region for $\widehat{H^s_r}$ and its interaction with scaling: is scaling-criticality attainable on a Fourier–Lebesgue scale?
- Quantitative statements at $H^{-1}$: growth of higher Sobolev norms, continuity moduli of the flow, and stability of the $H^{-1}$ solution map under numerical discretization.
- Transfer the technique to quasi-periodic and steplike backgrounds where Birkhoff coordinates are unavailable.

## 9. Key References

- **[Foundational]** J. Bourgain. *Fourier transform restriction phenomena for certain lattice subsets and applications to nonlinear evolution equations, II: The KdV equation.* Geometric and Functional Analysis 3 (1993), 209–262.
- **[Foundational]** C. Kenig, G. Ponce, L. Vega. *A bilinear estimate with applications to the KdV equation.* Journal of the American Mathematical Society 9 (1996), 573–603.
- **[Foundational]** J. Bona, R. Smith. *The initial-value problem for the Korteweg–de Vries equation.* Philosophical Transactions of the Royal Society A 278 (1975), 555–601.
- **[SOTA]** R. Killip, M. Vişan. *KdV is well-posed in $H^{-1}$.* Annals of Mathematics 190 (2019), 249–305.
- **[SOTA]** R. Killip, M. Vişan, X. Zhang. *Low regularity conservation laws for integrable PDE.* Geometric and Functional Analysis 28 (2018), 1062–1090.
- **[SOTA]** J. Colliander, M. Keel, G. Staffilani, H. Takaoka, T. Tao. *Sharp global well-posedness for KdV and modified KdV on $\mathbb R$ and $\mathbb T$.* Journal of the American Mathematical Society 16 (2003), 705–749.
- **[SOTA]** T. Kappeler, P. Topalov. *Global wellposedness of KdV in $H^{-1}(\mathbb T,\mathbb R)$.* Duke Mathematical Journal 135 (2006), 327–360.
- **[Sharpness]** L. Molinet. *Sharp ill-posedness results for the KdV and mKdV equations on the torus.* Advances in Mathematics 230 (2012), 1895–1930.
- **[Sharpness]** L. Molinet. *A note on ill-posedness for the KdV equation.* Differential and Integral Equations 24 (2011), 759–765.
- **[Sharpness]** M. Christ, J. Colliander, T. Tao. *Asymptotics, frequency modulation, and low regularity ill-posedness for canonical defocusing equations.* American Journal of Mathematics 125 (2003), 1235–1293.
- **[Endpoint]** Z. Guo. *Global well-posedness of Korteweg–de Vries equation in $H^{-3/4}(\mathbb R)$.* Journal de Mathématiques Pures et Appliquées 91 (2009), 583–597.
- **[Endpoint]** N. Kishimoto. *Well-posedness of the Cauchy problem for the Korteweg–de Vries equation at the critical regularity.* Differential and Integral Equations 22 (2009), 447–464.
- **[Related]** T. Buckmaster, H. Koch. *The Korteweg–de Vries equation at $H^{-1}$ regularity.* Annales de l'Institut Henri Poincaré C, Analyse Non Linéaire 32 (2015), 1071–1098.
- **[Related]** R. Killip, J. Murphy, M. Vişan. *Invariance of white noise for KdV on the line.* Inventiones Mathematicae 222 (2020), 203–282.
- **[Related]** B. Harrop-Griffiths, R. Killip, M. Vişan. *Sharp well-posedness for the cubic NLS and mKdV in $H^s(\mathbb R)$.* arXiv:2003.05011, 2020.
- **[Survey]** T. Tao. *Nonlinear Dispersive Equations: Local and Global Analysis.* CBMS Regional Conference Series in Mathematics 106, American Mathematical Society, 2006.

## 10. Worked Example / Concrete Special Case

**The soliton family and the critical exponent $s_c=-3/2$.**

For each $c>0$, KdV has the exact travelling wave
$$u_c(t,x)=\frac{c}{2}\operatorname{sech}^{2}\!\Big(\frac{\sqrt c}{2}(x-ct)\Big),\qquad Q_c:=u_c(0,\cdot).$$
Its width is $\sim c^{-1/2}$, amplitude $c/2$, speed $c$. Using $\int\operatorname{sech}^2(y)e^{-iy\eta}dy=\dfrac{\pi\eta}{\sinh(\pi\eta/2)}$ and $a=\sqrt c/2$,
$$\widehat{Q_c}(\xi)=\frac{c}{2a}\cdot\frac{\pi(\xi/a)}{\sinh(\pi\xi/(2a))}=\frac{2\pi\,\xi}{\sinh(\pi\xi/\sqrt c)} .$$
Substituting $\eta=\xi/\sqrt c$ (so $\widehat{Q_c}=2\pi\sqrt c\,\eta/\sinh(\pi\eta)$, $d\xi=\sqrt c\,d\eta$):
$$\|Q_c\|_{\dot H^{s}}^{2}=\frac{1}{2\pi}\int|\xi|^{2s}|\widehat{Q_c}|^{2}d\xi = 2\pi\, c^{\,s+3/2}\int_{\mathbb R}\frac{|\eta|^{2s+2}}{\sinh^{2}(\pi\eta)}\,d\eta = C_s^2\; c^{\,\frac{2s+3}{2}} .$$
Hence
$$\boxed{\;\|Q_c\|_{\dot H^{s}} = C_s\, c^{(2s+3)/4}\;}$$
with $C_s<\infty$ exactly when $-3/2<s<\;$(any positive value): near $\eta=0$ the integrand is $|\eta|^{2s}$, integrable iff $2s>-1$… more precisely $|\eta|^{2s+2}/\sinh^2 \sim |\eta|^{2s}$, integrable iff $s>-1/2$ at the origin only after including the full $\langle\xi\rangle^s$ weight; for the *homogeneous* norm the condition is $2s+2>-1$, i.e. $s>-3/2$.

Numerical read-off at $c=10^4$ (amplitude $5000$, width $\approx 0.02$):

| $s$ | exponent $(2s+3)/4$ | $\|Q_c\|_{\dot H^s}/C_s$ |
|---|---|---|
| $1$ | $1.25$ | $10^{5}$ |
| $0$ ($L^2$) | $0.75$ | $10^{3}$ |
| $-3/4$ | $0.375$ | $\approx 42$ |
| $-1$ | $0.25$ | $10$ |
| $-3/2$ | $0$ | $1$ (scale-invariant) |

**What this shows.** At $s=-3/2$ the whole family $\{Q_c\}_{c>0}$ has *one and the same* norm, yet the solutions travel at speed $c$ and have width $c^{-1/2}$. Two solitons with speeds $c$ and $c'=c+\delta$ decorrelate once $|\delta| t\gtrsim c^{-1/2}$, i.e. after time $t\sim c^{-1/2}/|\delta|$, at which point their $\dot H^{-3/2}$ distance is $\gtrsim C$, while their initial distance $\|Q_c-Q_{c'}\|_{\dot H^{-3/2}}\lesssim |\delta|\,\partial_c(\text{norm})\to 0$ as $\delta\to0$. So at criticality the flow map cannot be uniformly continuous on bounded sets — the scaling obstruction is realized by explicit, elementary solutions.

Moving up the table, the same family is *not* bounded in $H^{-1}$ (norm $\sim c^{1/4}\to\infty$), which is consistent with well-posedness there. The gap of Section 6 is exactly the range between the last row where the family is bounded ($s=-3/2$) and the row where the theory stops ($s=-1$): in $-3/2\le s<-1$ solitons no longer obstruct, Molinet's argument kills continuity of the flow map, and no substitute notion of solution is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*