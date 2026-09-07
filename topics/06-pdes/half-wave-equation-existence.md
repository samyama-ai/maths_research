---
id: 06-pdes/half-wave-equation-existence
title: "Half Wave Equation Existence"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Half Wave Equation Existence

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/half-wave-equation-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The *half-wave* equations are nonlinear evolution equations whose linear part is the nonlocal, order-one operator $|D| = \sqrt{-\Delta}$, i.e. a first-order equation with the dispersion relation of the wave equation but the complex/Schrödinger-type time derivative. Existence theory splits into three open questions.

**(A) Cubic half-wave on the line — global regularity and norm growth.** For
$$i\,\partial_t u = |D|u - |u|^2u, \qquad u:\mathbb{R}_t\times\mathbb{R}_x\to\mathbb{C},$$
global well-posedness in the energy space $H^{1/2}(\mathbb{R})$ is known. **Open:** are solutions with data in $H^s$, $s>1/2$, uniformly bounded in $H^s$, or do high Sobolev norms grow without bound? The standing conjecture (Gérard–Lenzmann–Pocovnicu–Raphaël) is that there exist solutions with
$$\|u(t)\|_{H^s}\;\sim\;|t|^{2s-1}\qquad (t\to\infty,\; s>1/2),$$
i.e. infinite-time weak turbulence. **Open:** local well-posedness or sharp ill-posedness below $s=1/2$.

**(B) Half-wave maps — global existence in the energy-critical dimension.** For
$$\partial_t \mathbf{u} \;=\; \mathbf{u}\wedge |D|\,\mathbf{u},\qquad \mathbf{u}:\mathbb{R}_t\times\mathbb{R}^d\to\mathbb{S}^2,$$
does every finite-energy datum $\mathbf{u}_0\in \dot H^{1/2}(\mathbb{R}^d;\mathbb{S}^2)$ generate a global solution? Open for **all** $d$ in the large-data case, and open even for small data in $d=1,2,3$. $d=1$ is energy-critical.

**(C) Boson-star / half-wave Hartree equation — the critical mass.** For
$$i\,\partial_t u = \sqrt{-\Delta+m^2}\,u - \big(|x|^{-1}*|u|^2\big)u \quad\text{on } \mathbb{R}^3,$$
blow-up in finite time occurs and a minimal-mass blow-up solution has been constructed. **Open:** the full classification — is every solution with mass below the Chandrasekhar threshold $M_c$ global, and is the blow-up rate universal?

A resolution of (A) or (B) requires either a global-in-time a priori bound (an interaction Morawetz or Lax-pair conserved quantity controlling $H^s$, $s>1/2$) or the construction of an explicit blow-up/unbounded-growth solution.

## 2. Mathematical Foundations

**The operator.** $|D|$ is the Fourier multiplier $\widehat{|D|u}(\xi)=|\xi|\hat u(\xi)$, positive, self-adjoint on $H^1\subset L^2$, homogeneous of degree $1$.

**Scaling.** For (A), $u_\lambda(t,x)=\lambda\,u(\lambda t,\lambda x)$ is a symmetry, and $\|u_\lambda\|_{\dot H^s}=\lambda^{s+1/2}\|u\|_{\dot H^s}$ in $d=1$; the critical exponent is $s_c=-\tfrac12$, so $L^2$ is *subcritical*. Nevertheless $s=1/2$ is the natural threshold, because in $d=1$ the symbol $|\xi|$ is linear: $e^{-it|D|}$ is pure transport at unit speed and produces **no dispersive decay and no smoothing**. All Strichartz gains vanish.

**Conservation laws for (A).**
$$M(u)=\int_{\mathbb{R}}|u|^2,\qquad P(u)=\int \bar u\, D u ,\qquad E(u)=\tfrac12\int \bar u\,|D|u-\tfrac14\int|u|^4 .$$
Gagliardo–Nirenberg in $d=1$ gives $\|u\|_{L^4}^4\le C\|u\|_{L^2}^{3}\|u\|_{\dot H^{1/2}}$; since the energy is *quadratic* in $\|u\|_{\dot H^{1/2}}$ and the potential term only *linear*, coercivity holds for arbitrary mass — this is why (A) has no energy-space blow-up.

**Hardy space and the resonant system.** Let $L^2_+=\{u\in L^2:\ \operatorname{supp}\hat u\subset[0,\infty)\}$ with Szegő projector $\Pi$. On $L^2_+$, $|D|=-i\partial_x=D$. Conjugating (A) by the linear flow and keeping only resonant interactions yields the **cubic Szegő equation**
$$i\,\partial_t u=\Pi(|u|^2u),\qquad u(t)\in L^2_+,$$
a completely integrable system with a Lax pair on Hankel operators $H_u$ (Gérard–Grellier). It is the model whose growth $\|u(t)\|_{H^s}\sim t^{2s-1}$ is *proved*, and which drives the conjecture in (A).

**Half-wave maps.** Equation (B) conserves $E(\mathbf u)=\tfrac12\|\mathbf u\|_{\dot H^{1/2}}^2$ and is the continuum limit of the Haldane–Shastry spin chain. In $d=1$ Lenzmann–Schikorra exhibit a Lax pair and a Bogomol'nyi-type identity: for $\mathbf u$ with values in $\mathbb{S}^2$ and finite energy, degree-$m$ half-harmonic maps saturate $E=2\pi|m|$, and rational traveling solitons exist.

## 3. History & State of the Art (SOTA)

- **2007.** Lenzmann proves local well-posedness for semi-relativistic Hartree equations of critical type; Fröhlich–Lenzmann prove finite-time blow-up for the boson-star equation, giving the first "non-existence of global solutions" results in the half-wave family.
- **2010.** Gérard–Grellier introduce the cubic Szegő equation as the model non-dispersive Hamiltonian PDE and prove growth of Sobolev norms via Hankel-operator spectral theory.
- **2011.** Pocovnicu gives explicit formulas and traveling waves for the Szegő equation on $\mathbb{R}$.
- **2013.** Krieger–Lenzmann–Raphaël construct non-dispersive (traveling-solitary) solutions to the $L^2$-critical half-wave equation and a minimal-mass blow-up solution for the boson-star case.
- **2018.** Lenzmann–Schikorra (*Inventiones*) establish the integrable structure of energy-critical half-wave maps into $\mathbb{S}^2$; Krieger–Sire prove small-data global regularity in high dimensions; Gérard–Lenzmann–Pocovnicu–Raphaël construct a two-soliton solution of the cubic half-wave equation on $\mathbb{R}$ exhibiting a *transient* turbulent regime.
- **2018–2021.** Bellazzini–Georgiev–Visciglia give long-time bounds for semi-relativistic NLS in general dimension; Kiesenhofer–Krieger reach $n=4$ for half-wave maps.
- **2020s.** Berntson–Langmann–Lenzmann connect half-wave maps solitons to spin Calogero–Moser pole dynamics, producing explicit multi-soliton families.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| (A) on $\mathbb{R}$ or $\mathbb{T}$, $s\ge 1/2$ | Local well-posedness; **global** well-posedness in $H^{1/2}$ (mass+energy coercivity, any mass) | Gérard–Grellier; GLPR 2018 |
| (A), $s>1/2$ | Only a priori *exponential-in-time* bound $\|u(t)\|_{H^s}\lesssim e^{C|t|}$ from Gronwall | GLPR 2018 |
| (A), two-soliton data | Explicit solution with $\|u(t)\|_{H^s}$ growing by an arbitrarily large factor on a long but **finite** interval, then returning | GLPR, *Annals of PDE* 4 (2018) |
| Cubic Szegő ($\mathbb{T}$ and $\mathbb{R}$) | Global well-posedness in $H^{1/2}_+$; generic data have $\limsup_t\|u(t)\|_{H^s}=\infty$; explicit rate $t^{2s-1}$ on a $G_\delta$-dense set | Gérard–Grellier 2010, 2017 |
| (B), small data, $d\ge 5$ | Global regularity for data small in a critical Besov space | Krieger–Sire, *Anal. PDE* 11 (2018) |
| (B), small data, $d=4$ | Global regularity | Kiesenhofer–Krieger, 2021 |
| (B), $d=1$ | Lax pair, explicit rational solitons, energy quantization $E=2\pi|m|$ for half-harmonic maps; no global existence theorem | Lenzmann–Schikorra 2018 |
| (C) on $\mathbb{R}^3$ | Blow-up for negative-energy, spherically symmetric data; minimal-mass blow-up with rate $\lambda(t)\sim (T-t)e^{-\sqrt{|\log(T-t)|}}$ | Fröhlich–Lenzmann 2007; Krieger–Lenzmann–Raphaël 2013 |
| $L^2$-critical half-wave, $d=1$ | Traveling non-dispersive solutions $u=e^{it\omega}Q_v(x-vt)$ exist for all $|v|<1$ | Krieger–Lenzmann–Raphaël 2013 |

## 5. Principal Obstacles

- **Zero dispersion in $d=1$.** The group velocity $\nabla_\xi|\xi|=\xi/|\xi|$ is constant in modulus. Wave packets do not spread, so there is no $L^\infty_x$ decay, no local smoothing gain, and no Strichartz estimate with derivative gain. Every tool that makes 1D NLS tractable is unavailable; well-posedness rests on the algebra property of $H^s$, $s>1/2$, plus a commutator estimate at $s=1/2$ — an approach that gives at best exponential-in-time control.
- **No monotonicity formula.** Morawetz and interaction-Morawetz estimates rely on the second-order structure of $-\Delta$; for the order-one nonlocal $|D|$ the virial identity $\frac{d^2}{dt^2}\int x^2|u|^2$ does not close, because $[|D|,x]$ is a bounded but non-positive operator with no sign. Scattering-by-monotonicity is therefore blocked.
- **Integrability is only approximate.** The Szegő equation has a Lax pair; the half-wave equation does not. The Szegő system is the *resonant* limit, valid on times $O(\varepsilon^{-2})$ for data of size $\varepsilon$; beyond that the non-resonant remainder is uncontrolled, so proved Szegő turbulence transfers to the half-wave equation only on finite windows (exactly what GLPR obtain).
- **Energy-critical geometry (B).** In $d=1$, $\dot H^{1/2}$ embeds in BMO but not $L^\infty$, so bubbling analysis à la Struwe requires a concentration-compactness theory for half-harmonic maps with a nonlocal energy — the defect measure has no local (differential) description.
- **Loss of derivatives at $s<1/2$.** The nonlinearity $|u|^2u$ is not controlled by any known multilinear estimate for $|D|$ below $H^{1/2}$; whether failure is genuine ill-posedness (norm inflation) or a defect of method is unknown.

## 6. The Gap

Proven: $H^{1/2}$ global existence for (A), and finite-time growth of $H^s$ by an arbitrarily large factor. Conjectured: *infinite-time* growth at rate $t^{2s-1}$. The gap is a **long-time approximation theorem**: showing that the Szegő resonant dynamics governs half-wave solutions on times far longer than $O(\varepsilon^{-2})$ — equivalently, constructing an almost-conserved quantity or a modified scattering normal form whose remainder is summable over infinitely many turbulent cascades. For (B), the gap is the absence of *any* a priori bound above the critical energy norm in low dimension: the small-data results for $d\ge4$ rely on dispersive decay that is strictly weaker as $d$ falls and vanishes at $d=1$, precisely where the equation is critical and integrable.

## 7. Current Research (as of June 2026)

- **Orsay / Paris-Saclay (Gérard, Grellier and collaborators).** Explicit integration of Szegő-type and Calogero–Moser derivative NLS hierarchies; extending the Hankel-operator machinery to perturbed models to make the resonant approximation quantitative over long times.
- **Basel (Lenzmann) and EPFL (Krieger).** Half-wave maps: explicit multi-soliton solutions from spin Calogero–Moser pole dynamics, soliton (in)stability, and pushing small-data global regularity toward $d=2,3$ *(frontier — verify)*.
- **Integrable-systems community (Berntson, Langmann, Klabbers).** Rational and elliptic solution families for half-wave maps; conjectural complete integrability of the $d=1$ equation in a strong (action–angle) sense *(frontier — verify)*.
- **Dispersive-PDE groups (Bellazzini, Georgiev, Visciglia; Ionescu–Pusateri school).** Modified scattering and normal-form methods for fractional/semi-relativistic equations in dimensions where some decay survives.
- Numerics on unbounded-growth scenarios for (A) support the $t^{2s-1}$ rate but do not reach asymptotic times *(frontier — verify)*.

## 8. Future Work

1. **Almost-conserved quantities.** Construct an $I$-method-type or Lax-pair-deformed functional controlling $\|u\|_{H^s}$, $s>1/2$, whose time derivative is integrable against the two-soliton dynamics.
2. **Rigorous turbulent chaining.** Iterate the GLPR two-soliton construction infinitely often with parameters tuned so growth compounds — a "cascade in time" analogue of Colliander–Keel–Staffilani–Takaoka–Tao's finite cascade for NLS.
3. **Sharp ill-posedness below $H^{1/2}$.** Prove norm inflation for (A) at $s<1/2$ using the transport structure, or find a null-form-type cancellation showing this is not the true threshold.
4. **Concentration-compactness for half-harmonic maps.** Develop a bubble-decomposition for finite-energy $\dot H^{1/2}$ maps into $\mathbb{S}^2$; combine with the $E=2\pi|m|$ quantization to reduce (B) in $d=1$ to a rigidity theorem for solitons.
5. **Classification for (C).** Determine whether the Chandrasekhar mass $M_c$ is exactly the global-existence threshold and whether the KLR blow-up rate is universal.

## 9. Key References

- **[Foundational]** Enno Lenzmann. *Well-posedness for semi-relativistic Hartree equations of critical type.* Mathematical Physics, Analysis and Geometry 10 (2007), 43–64.
- **[Foundational]** Jürg Fröhlich, Enno Lenzmann. *Blowup for nonlinear wave equations describing boson stars.* Communications on Pure and Applied Mathematics 60 (2007), 1691–1705.
- **[Foundational]** Patrick Gérard, Sandrine Grellier. *The cubic Szegő equation.* Annales Scientifiques de l'École Normale Supérieure 43 (2010), 761–810.
- **[Foundational]** Oana Pocovnicu. *Explicit formula for the solution of the Szegő equation on the real line and applications.* Discrete and Continuous Dynamical Systems 31 (2011), 607–649.
- **[SOTA / Recent]** Joachim Krieger, Enno Lenzmann, Pierre Raphaël. *Nondispersive solutions to the $L^2$-critical half-wave equation.* Archive for Rational Mechanics and Analysis 209 (2013), 61–129.
- **[SOTA / Recent]** Patrick Gérard, Enno Lenzmann, Oana Pocovnicu, Pierre Raphaël. *A two-soliton with transient turbulent regime for the cubic half-wave equation on the real line.* Annals of PDE 4 (2018), article 7.
- **[SOTA / Recent]** Enno Lenzmann, Armin Schikorra. *On energy-critical half-wave maps into $\mathbb{S}^2$.* Inventiones Mathematicae 213 (2018), 1–82.
- **[SOTA / Recent]** Joachim Krieger, Yannick Sire. *Small data global regularity for half-wave maps.* Analysis & PDE 11 (2018), 661–682.
- **[SOTA / Recent]** Jacopo Bellazzini, Vladimir Georgiev, Nicola Visciglia. *Long time dynamics for semi-relativistic NLS and half wave in arbitrary dimension.* Mathematische Annalen 371 (2018), 707–740.
- **[Survey]** Patrick Gérard, Sandrine Grellier. *The cubic Szegő equation and Hankel operators.* Astérisque 389, Société Mathématique de France, 2017.
- **[Survey]** Enno Lenzmann. *A short primer on the half-wave maps equation.* Journées Équations aux Dérivées Partielles (2018), exposé no. 4.

## 10. Worked Example / Concrete Special Case

**A traveling soliton of the resonant (Szegő) system on $\mathbb{R}$.** This exhibits the non-dispersive behaviour that drives the whole problem.

Work in the Hardy space $L^2_+$ (Fourier support in $[0,\infty)$; boundary values of functions holomorphic in the upper half-plane). Take the rational ansatz
$$\varphi(x)=\frac{\alpha}{x+i},\qquad \alpha\in\mathbb{C}\setminus\{0\},$$
which is holomorphic in $\{\operatorname{Im}x>0\}$ (its pole sits at $x=-i$), hence $\varphi\in L^2_+$.

*Step 1 — compute the nonlinearity.* $|\varphi|^2\varphi=\dfrac{|\alpha|^2\alpha}{(x+i)^2(x-i)}$. Partial fractions:
$$\frac{1}{(x+i)^2(x-i)}=\frac{A}{x-i}+\frac{B}{x+i}+\frac{C}{(x+i)^2},$$
with $A=\frac{1}{(2i)^2}=-\tfrac14$, $C=\frac{1}{-2i}=\tfrac{i}{2}$, and matching the $x^2$ coefficient of $1=A(x+i)^2+B(x^2+1)+C(x-i)$ gives $A+B=0$, so $B=\tfrac14$. (Check at $x=0$: $-A+B-iC=\tfrac14+\tfrac14+\tfrac12=1$. ✓)

*Step 2 — project.* $\frac{1}{x-i}$ has its pole in the upper half-plane, so it lies in $L^2_-$ and is annihilated by $\Pi$; the other two terms are holomorphic above. Hence
$$\Pi(|\varphi|^2\varphi)=|\alpha|^2\alpha\left[\frac{1/4}{x+i}+\frac{i/2}{(x+i)^2}\right].$$

*Step 3 — match the traveling ansatz.* Put $u(t,x)=e^{-i\omega t}\varphi(x-ct)$ into $i\partial_t u=\Pi(|u|^2u)$. Since $\varphi'(x)=-\alpha/(x+i)^2$,
$$i\partial_t u=e^{-i\omega t}\Big(\omega\varphi-ic\varphi'\Big)=e^{-i\omega t}\left[\frac{\omega\alpha}{x+i}+\frac{ic\alpha}{(x+i)^2}\right].$$
Comparing coefficients of $(x+i)^{-1}$ and $(x+i)^{-2}$:
$$\omega=\frac{|\alpha|^2}{4},\qquad c=\frac{|\alpha|^2}{2}=2\omega .$$

*Conclusion.*
$$\boxed{\;u(t,x)=\frac{\alpha\,e^{-i|\alpha|^2 t/4}}{\big(x-\tfrac{|\alpha|^2}{2}t\big)+i}\;}$$
is an exact global solution of the cubic Szegő equation. It never disperses: $\|u(t)\|_{H^s}$ is constant in $t$, the profile translates rigidly at speed $|\alpha|^2/2$, and mass is $M=\pi|\alpha|^2$.

*Why this is the crux.* A single soliton is stationary in shape; **two** such profiles with nearly resonant parameters interact, and Gérard–Lenzmann–Pocovnicu–Raphaël show the interaction pumps energy into high frequencies, so $\|u(t)\|_{H^s}$ inflates by an arbitrarily large factor. For the exact half-wave equation the same construction works only on a finite window, after which the profile relaxes. Whether the pumping can be made to repeat forever — turning transient turbulence into the conjectured $t^{2s-1}$ growth — is exactly the open half of the existence/regularity problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*