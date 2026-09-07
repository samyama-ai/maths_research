---
id: 06-pdes/keller-segel-blow-up-profile
title: "Keller Segel Blow Up Profile"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Keller–Segel Blow-Up Profile

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/keller-segel-blow-up-profile` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For the Patlak–Keller–Segel chemotaxis system, classify **all** singularity formation: the geometry of the concentration set, the amount of mass concentrated, the universal spatial profile, and the concentration rate $\lambda(t)\to 0$.

The central conjecture in the critical dimension $n=2$ is:

**Conjecture (universality of $8\pi$ aggregation).** Let $u$ be a solution of the parabolic–elliptic system on $\mathbb{R}^2$ (or a bounded domain) blowing up at time $T<\infty$ at a point $x_0$. Then near $x_0$
$$u(x,t) \;=\; \frac{1}{\lambda(t)^2}\,U\!\left(\frac{x-x_0}{\lambda(t)}\right) + \text{lower order},\qquad U(y)=\frac{8}{(1+|y|^2)^2},$$
so exactly $\int U = 8\pi$ concentrates, and the scale obeys the log-corrected law
$$\lambda(t) \;=\; \sqrt{T-t}\;e^{-\sqrt{\tfrac{1}{2}\left|\ln (T-t)\right|}\,+\,O(1)} .$$

A complete resolution requires: (i) proving this for **all** (not just constructed or radial) blow-up solutions; (ii) ruling out or classifying the exceptional higher-mass regimes $8\pi k$, $k\ge 2$, predicted by formal asymptotics; (iii) the analogous classification for the fully parabolic system; and (iv) the classification in dimensions $n\ge 3$, where the scaling is supercritical and both "collapsing ring" and point-concentration mechanisms exist.

## 2. Mathematical Foundations

The parabolic–parabolic (full) Keller–Segel system on $\Omega\subseteq\mathbb{R}^n$:
$$\partial_t u = \Delta u - \nabla\cdot\!\left(u\,\nabla c\right),\qquad \varepsilon\,\partial_t c = \Delta c - \alpha c + u,$$
with $u\ge0$ the cell density, $c$ the chemoattractant. Setting $\varepsilon=0,\ \alpha=0$ gives the **parabolic–elliptic** (simplified) system $-\Delta c = u$, i.e. $c=E_n * u$ with $E_2(x)=-\frac{1}{2\pi}\ln|x|$.

**Scaling.** $u_\lambda(x,t)=\lambda^{2}u(\lambda x,\lambda^2 t)$, $c_\lambda(x,t)=c(\lambda x,\lambda^2 t)$ is a solution. Mass $M=\int u$ is invariant exactly when $n=2$: the system is **mass-critical** in two dimensions, mass-supercritical for $n\ge3$.

**Free energy.** In $\mathbb{R}^2$,
$$\mathcal{F}[u]=\int u\ln u \,dx-\frac{1}{2}\int u\,c\,dx,\qquad \frac{d}{dt}\mathcal{F}[u(t)]=-\int u\left|\nabla\ln u-\nabla c\right|^2 dx\le 0 .$$
The logarithmic Hardy–Littlewood–Sobolev inequality makes $\mathcal{F}$ bounded below precisely for $M\le 8\pi$.

**Virial identity** (finite second moment, $\mathbb{R}^2$):
$$\frac{d}{dt}\int |x|^2 u(x,t)\,dx = 4M-\frac{M^2}{2\pi}.$$

**Stationary profile.** The Liouville equation $\Delta \ln U + U = 0$ has the family
$$U_\lambda(y)=\frac{8\lambda^2}{(\lambda^2+|y|^2)^2},\qquad \int_{\mathbb{R}^2}U_\lambda = 8\pi,$$
which are exactly the self-similar-in-scale steady states; $U=U_1$ is the conjectured blow-up profile. Crucially $\int |y|^2 U\,dy = +\infty$ **logarithmically** — this degeneracy is the analytic source of the $\sqrt{|\ln(T-t)|}$ correction.

**Higher dimensions.** For $n\ge3$ the singular steady state
$$u_s(x)=\frac{2(n-2)}{|x|^2},\qquad c_s(x)=-2\ln|x|$$
solves the parabolic–elliptic system and governs the final-time profile.

## 3. History & State of the Art (SOTA)

- **1953 / 1970.** Patlak's random-walk derivation; Keller and Segel's instability model of *Dictyostelium* aggregation.
- **1992.** Jäger and Luckhaus prove blow-up above a mass threshold via the second-moment argument.
- **1995–2001.** Nagai identifies the sharp threshold $8\pi$ (radial, whole plane / $4\pi$ at boundary points), and gives blow-up criteria.
- **1996.** Herrero and Velázquez, by matched asymptotics plus a rigorous construction on the disk, produce a radial solution with a $8\pi$ Dirac concentration and the rate $\lambda(t)\sim C\sqrt{T-t}\,e^{-\sqrt{|\ln(T-t)|/2}}$. This is the first appearance of the conjectured law.
- **2002.** Velázquez's formal stability analysis identifies the discrete family of unstable modes producing $8\pi k$ concentration.
- **2006.** Blanchet, Dolbeault and Perthame: global existence and dispersion for $M<8\pi$ in $\mathbb{R}^2$; blow-up for $M>8\pi$ with finite second moment.
- **2008.** Blanchet, Carrillo and Masmoudi: at $M=8\pi$ exactly, infinite-time aggregation to a Dirac mass.
- **2014.** Raphaël and Schweyer give the first *stable*, non-radial-perturbation-robust construction of the Herrero–Velázquez regime with sharp modulation analysis.
- **2018–2022.** Ghoul–Masmoudi (minimal-mass infinite-time blow-up, stable) and Collot–Ghoul–Masmoudi–Nguyen (refined asymptotics to all orders, plus $C^{\,\infty}$ description of the regular part) essentially close the *constructive* side in $n=2$.
- **2013–2020.** Winkler establishes finite-time blow-up for the fully parabolic system in $n\ge3$; Mizoguchi does so in $n=2$ for the Cauchy problem, decades after the formal prediction.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$, par.–ell., $M<8\pi$ | global existence, self-similar decay | Blanchet–Dolbeault–Perthame 2006 |
| $n=2$, par.–ell., $M>8\pi$, $\int|x|^2u_0<\infty$ | finite-time blow-up | Jäger–Luckhaus 1992; Nagai 1995 |
| $n=2$, par.–ell., $M=8\pi$ | infinite-time concentration to $8\pi\delta$ | Blanchet–Carrillo–Masmoudi 2008 |
| $n=2$, par.–ell., open set of data | blow-up with profile $U$ and law $\lambda=\sqrt{T-t}e^{-\sqrt{|\ln(T-t)|/2}+O(1)}$, **stable** | Raphaël–Schweyer 2014 |
| $n=2$, refined law | $\lambda(t)= c_0\sqrt{T-t}\,e^{-\sqrt{|\ln(T-t)|/2}}\big(1+o(1)\big)$, explicit $c_0$ involving $e^{-\gamma/2}$; full asymptotic expansion and stability | Collot–Ghoul–Masmoudi–Nguyen 2022 |
| $n=2$, $M=8\pi$ minimal mass | stable infinite-time blow-up with explicit rate | Ghoul–Masmoudi 2018; Dávila–del Pino–Dolbeault–Musso–Wei 2019 |
| $n=2$, mass quantization | concentrated mass is a multiple of $8\pi$ ($4\pi$ at boundary) | Senba–Suzuki; Suzuki 2005 |
| $n=2$, fully parabolic | existence of finite-time blow-up (Cauchy problem) | Mizoguchi 2020 |
| $n\ge3$, par.–ell., radial | final profile bounded by $2(n-2)|x|^{-2}$; sharp pointwise upper estimates | Souplet–Winkler 2019 |
| $n\ge3$ | backward self-similar blow-up profiles exist | Herrero–Medina–Velázquez 1997/1998 |
| $n\ge3$ | "collapsing ring" blow-up: concentration on a shrinking sphere, not a point | Collot–Ghoul–Masmoudi–Nguyen, arXiv 2021 |
| $n\ge3$, fully parabolic | finite-time blow-up for arbitrarily small mass | Winkler 2013 |

## 5. Principal Obstacles

- **No classification of the singular limit.** All sharp $n=2$ results are *constructions*: one builds a solution near a prescribed ansatz and controls a finite-dimensional modulation system. There is no compactness/rigidity theorem saying every blow-up must approach $\{U_\lambda\}$. Liouville-type classification arguments used for harmonic maps or NLS require a monotonicity formula that Keller–Segel does not supply in a usable form — the free energy is monotone but its dissipation is not coercive in a scale-invariant norm.
- **Logarithmic degeneracy.** $\int|y|^2U=\infty$ makes the scaling zero-mode $\Lambda U = -\nabla\cdot(yU)$ only marginally non-integrable. The modulation ODE degenerates to $b_s \approx -2b^2/|\ln b|$, so all estimates carry $|\ln\lambda|$ losses: standard energy methods lose exactly the power one needs.
- **Non-locality.** $\nabla c = \nabla E_n * u$ is a nonlocal operator of order $-1$; the nonlinearity is not a pointwise power, so Giga–Kohn-type similarity-variable arguments and pointwise-comparison/blow-up-rate estimates are unavailable outside radial symmetry.
- **Non-radial and multi-point blow-up.** Almost every sharp statement in $n\ge3$ assumes radial symmetry, which the $|x|^{-2}$ profile and the ring mechanism both use heavily. Non-radial rigidity is open.
- **Fully parabolic system.** With $\varepsilon>0$ there is no elliptic reduction, the free energy loses its variational structure at the profile scale, and the coupled parabolic pair introduces a second timescale; Type I/Type II dichotomy is not known.
- **Supercriticality for $n\ge3$.** Continuum of admissible rates: self-similar (Type I), collapsing ring, and possibly other Type II regimes coexist. No selection principle is proven.

## 6. The Gap

Proved: for an **open set** of data in $n=2$, blow-up occurs with the profile $U$ and the log-corrected rate, with a complete asymptotic expansion. Conjectured: the same holds for **every** blow-up solution.

The precise missing step is a **rigidity theorem for the rescaled flow**: show that for any blow-up solution, the rescaled density $\lambda(t)^2u(x_0+\lambda(t)y,t)$ converges (locally, in a suitably weighted space) to some $U_\mu$, i.e. that the $\omega$-limit set of the renormalized flow is exactly the stationary manifold $\{U_\mu\}$. Equivalently: exclude the formally predicted unstable $8\pi k$, $k\ge2$, regimes, or construct them rigorously and show they are the only alternatives. In $n\ge3$, the gap is the absence of any classification of the concentration set — point versus ring versus higher-dimensional sets.

## 7. Current Research (as of June 2026)

- **Modulation-analysis school** (Masmoudi, Nguyen, Ghoul, Collot, Raphaël, Merle, Schweyer; NYU/Abu Dhabi, Courant, Sorbonne, Nice): pushing the refined-description technique from radial to non-radial data, and to the fully parabolic system.
- **Gluing methods** (del Pino, Musso, Wei, Dávila; Bath, Heriot-Watt, UBC/CUHK): inner–outer parabolic gluing constructs multi-point and infinite-time singularities; expected to yield $8\pi k$ regimes and blow-up with prescribed sets. *(frontier — verify)*
- **Ring and Type II dynamics in $n\ge3$**: stability of the collapsing-ring regime and its co-dimension count remain the active question. *(frontier — verify)*
- **Rigidity / continuation**: Souplet, Winkler, Mizoguchi and collaborators pursue universal a priori pointwise bounds ($u\lesssim |x-x_0|^{-2}$) and weak-solution continuation past blow-up.
- **Optimal transport and gradient-flow viewpoint** (Carrillo, Blanchet, Calvez): Wasserstein gradient-flow structure and JKO discretization for measure-valued continuations.

## 8. Future Work

1. Prove a Liouville theorem for ancient solutions of the rescaled 2D system with mass $\le 8\pi+\epsilon$ — the expected engine of a full classification.
2. Construct the $8\pi k$ regimes rigorously and compute their instability index (formally $k-1$ unstable directions from Velázquez's analysis).
3. Extend the Collot–Ghoul–Masmoudi–Nguyen expansion to $\varepsilon>0$, proving the parabolic–parabolic 2D rate coincides with the parabolic–elliptic one.
4. Establish non-radial rigidity in $n\ge3$: is every blow-up either point-like with the $2(n-2)|x|^{-2}$ profile or a collapsing ring?
5. Characterize the post-blow-up continuation: is the measure-valued solution unique, and does mass detach as a moving Dirac?

## 9. Key References

- **[Foundational]** C. S. Patlak. *Random walk with persistence and external bias.* Bulletin of Mathematical Biophysics 15, 311–338, 1953.
- **[Foundational]** E. F. Keller, L. A. Segel. *Initiation of slime mold aggregation viewed as an instability.* Journal of Theoretical Biology 26, 399–415, 1970.
- **[Foundational]** W. Jäger, S. Luckhaus. *On explosions of solutions to a system of partial differential equations modelling chemotaxis.* Transactions of the AMS 329, 819–824, 1992.
- **[Foundational]** M. A. Herrero, J. J. L. Velázquez. *Singularity patterns in a chemotaxis model.* Mathematische Annalen 306, 583–623, 1996.
- **[Foundational]** T. Nagai. *Blow-up of radially symmetric solutions to a chemotaxis system.* Advances in Mathematical Sciences and Applications 5, 581–601, 1995.
- **[Key]** A. Blanchet, J. Dolbeault, B. Perthame. *Two-dimensional Keller–Segel model: optimal critical mass and qualitative properties of the solutions.* Electronic Journal of Differential Equations 2006, no. 44, 2006.
- **[Key]** A. Blanchet, J. A. Carrillo, N. Masmoudi. *Infinite time aggregation for the critical Patlak–Keller–Segel model in $\mathbb{R}^2$.* Communications on Pure and Applied Mathematics 61, 1449–1481, 2008.
- **[Key]** J. J. L. Velázquez. *Stability of some mechanisms of chemotactic aggregation.* SIAM Journal on Applied Mathematics 62, 1581–1633, 2002.
- **[SOTA]** P. Raphaël, R. Schweyer. *On the stability of critical chemotactic aggregation.* Mathematische Annalen 359, 267–377, 2014.
- **[SOTA]** T. Ghoul, N. Masmoudi. *Minimal mass blowup solutions for the Patlak–Keller–Segel equation.* Communications on Pure and Applied Mathematics 71, 1957–2015, 2018.
- **[SOTA]** C. Collot, T. Ghoul, N. Masmoudi, V. T. Nguyen. *Refined description and stability for singular solutions of the 2D Keller–Segel system.* Communications on Pure and Applied Mathematics 75, 1419–1516, 2022.
- **[SOTA]** C. Collot, T. Ghoul, N. Masmoudi, V. T. Nguyen. *Collapsing-ring blowup solutions for the Keller–Segel system in three dimensions and higher.* arXiv:2112.15518, 2021.
- **[SOTA]** J. Dávila, M. del Pino, J. Dolbeault, M. Musso, J. Wei. *Infinite time blow-up in the Patlak–Keller–Segel system: existence and stability.* arXiv:1911.12417, 2019.
- **[SOTA]** P. Souplet, M. Winkler. *Blow-up profiles for the parabolic–elliptic Keller–Segel system in dimensions $n\ge3$.* Communications in Mathematical Physics 367, 665–681, 2019.
- **[SOTA]** M. Winkler. *Finite-time blow-up in the higher-dimensional parabolic–parabolic Keller–Segel system.* Journal de Mathématiques Pures et Appliquées 100, 748–767, 2013.
- **[SOTA]** N. Mizoguchi. *Finite-time blowup in Cauchy problem of parabolic–parabolic chemotaxis system.* Journal de Mathématiques Pures et Appliquées 136, 2020.
- **[Survey]** D. Horstmann. *From 1970 until present: the Keller–Segel model in chemotaxis and its consequences, I.* Jahresbericht der DMV 105, 103–165, 2003.
- **[Survey]** N. Bellomo, A. Bellouquid, Y. Tao, M. Winkler. *Toward a mathematical theory of Keller–Segel models of pattern formation in biological tissues.* Mathematical Models and Methods in Applied Sciences 25, 1663–1763, 2015.
- **[Book]** T. Suzuki. *Free Energy and Self-Interacting Particles.* Birkhäuser, 2005.

## 10. Worked Example / Concrete Special Case

**Step 1 — the $8\pi$ threshold from the virial identity.** Take $n=2$, parabolic–elliptic, $u_0\ge0$ with $M=\int u_0$ and $I(0)=\int|x|^2u_0<\infty$. Then
$$I'(t)=\int|x|^2\Delta u\,dx-\int|x|^2\nabla\!\cdot\!(u\nabla c)\,dx.$$
The first term is $4M$. For the second, $\nabla c(x)=-\frac{1}{2\pi}\int\frac{x-y}{|x-y|^2}u(y)dy$, so
$$-\int|x|^2\nabla\!\cdot\!(u\nabla c) = 2\int x\cdot\nabla c\,u\,dx = -\frac{1}{\pi}\iint \frac{x\cdot(x-y)}{|x-y|^2}u(x)u(y)\,dx\,dy .$$
Symmetrizing in $x\leftrightarrow y$ replaces $x\cdot(x-y)$ by $\tfrac12|x-y|^2$, giving $-\frac{M^2}{2\pi}$. Hence
$$I(t)=I(0)+\left(4M-\frac{M^2}{2\pi}\right)t .$$
If $M>8\pi$ the bracket is negative, so $I(t)$ would hit $0$ by $t_*=\frac{2\pi I(0)}{M(M-8\pi)}$ while $M$ stays fixed — impossible for a nonnegative smooth solution. Therefore blow-up occurs at some $T\le t_*$.

**Step 2 — why the profile is $U$.** At the blow-up point the solution locally exhausts the critical mass, so the rescaling $v(y,s)=\lambda^2u(x_0+\lambda y,t)$ has mass $\to 8\pi$ and free energy at its minimizing configuration. The Euler–Lagrange equation $\ln v = c_v + \text{const}$, i.e. $\Delta \ln v + v = 0$ with $\int v = 8\pi$, has exactly the Liouville family; normalizing $\lambda$ selects
$$U(y)=\frac{8}{(1+|y|^2)^2},\qquad \int_{\mathbb R^2}U\,dy = 8\pi\int_0^\infty\frac{2r\,dr}{(1+r^2)^2}\cdot\frac{1}{1}=8\pi .$$

**Step 3 — where the $\sqrt{|\ln(T-t)|}$ comes from.** Insert $u(x,t)\approx\lambda(t)^{-2}U\!\big((x-x_0)/\lambda(t)\big)$ and let $b=-\lambda\lambda_t$. Projecting the equation onto the scaling direction $\Lambda U=-\nabla\cdot(yU)$ requires the weight $\int_{|y|\le 1/b}|y|^2U\,dy$, which diverges logarithmically:
$$\int_{|y|\le R}|y|^2U(y)\,dy = 8\pi\!\int_0^R\!\frac{r^3\,dr}{(1+r^2)^2}\cdot\frac{2}{1}\;\sim\;16\pi\ln R .$$
This turns the naive self-similar law $b_s=-b^2$ into $b_s \approx -\dfrac{2b^2}{|\ln b|}$, with $\lambda_s/\lambda=-b$ and $ds=dt/\lambda^2$. Solving: $b(t)\simeq \frac{1}{2}\,\frac{1}{\sqrt{2|\ln(T-t)|}}\cdot\big(1+o(1)\big)$-corrected, and integrating $\lambda_t=-b/\lambda$ gives
$$\lambda(t)=\sqrt{T-t}\;e^{-\sqrt{\frac{|\ln(T-t)|}{2}}+O(1)},$$
which is **faster** than the self-similar scale $\sqrt{T-t}$ by the factor $e^{-\sqrt{|\ln(T-t)|/2}}$ — Type II blow-up. Numerically, at $T-t=10^{-12}$ one has $|\ln(T-t)|\approx 27.6$, so the correction factor is $e^{-3.72}\approx 2.4\times10^{-2}$: the singularity is about forty times sharper than self-similar. This slow, sub-power correction is precisely why the rate is hard to detect numerically and why the general classification remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*